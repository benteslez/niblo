const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
const BASE = 'http://localhost:8765/oposicion.html';
const SUPA = 'https://mock.supabase.co';
const b64 = o => Buffer.from(JSON.stringify(o)).toString('base64url');
const jwt = (sub, exp) => b64({alg:'HS256'}) + '.' + b64({ sub, exp }) + '.firma';
const ahora = () => Math.floor(Date.now()/1000);

/* ---------------- Supabase simulado ---------------- */
const DB = { temas:new Map(), prog:new Map() };
const subs = new Set();       // { ws, hogar, uid }
let refrescos = 0, posts = 0;
const isoPg = () => new Date().toISOString().replace('Z', '+00:00');
function uidDe(req) { const a = req.headers()['authorization'] || ''; try { return JSON.parse(Buffer.from(a.split(' ')[1].split('.')[1], 'base64url')).sub; } catch { return null; } }
function avisar(tabla, fila) {
  for (const s of subs) {
    if (tabla === 'oposicion_temas' && fila.hogar_id !== s.hogar) continue;
    if (tabla === 'oposicion_progreso' && fila.user_id !== s.uid) continue;
    s.ws.send(JSON.stringify({ topic:s.topic, event:'postgres_changes', payload:{ data:{ table:tabla, type:'UPDATE' } }, ref:null }));
  }
}
const PARTES = ['meta','sections','glossary','timeline','flashcards','questions'];
function mezclaServidor(old, nw) {          // = trigger oposicion_temas_mezcla (010)
  if (nw.borrado || old.borrado || !nw.datos || !old.datos) return Date.parse(nw.modificado) < Date.parse(old.modificado) ? null : nw;
  const m = JSON.parse(JSON.stringify(old.datos)); m.mod = m.mod || {};
  for (const k of PARTES) {
    const mn = (nw.datos.mod && nw.datos.mod[k]) || Date.parse(nw.modificado), mo = (old.datos.mod && old.datos.mod[k]) || Date.parse(old.modificado);
    if (mn > mo) { if (k === 'meta') ['title','subtitle','fileName','html','cargado'].forEach(c => m[c] = nw.datos[c] ?? null); else m[k] = nw.datos[k] || []; m.mod[k] = mn; } else m.mod[k] = mo;
  }
  if (JSON.stringify(m) === JSON.stringify(old.datos) && Date.parse(nw.modificado) <= Date.parse(old.modificado)) return null;
  return Object.assign({}, nw, { datos:m, modificado:new Date(Math.max(Date.parse(nw.modificado), Date.parse(old.modificado))).toISOString() });
}
function upsert(mapa, clave, fila, tabla) {
  const old = mapa.get(clave);
  if (old && tabla === 'oposicion_temas') { fila = mezclaServidor(old, fila); if (!fila) return; }
  else if (old && Date.parse(fila.modificado) < Date.parse(old.modificado)) return;   // trigger LWW
  const n = Object.assign({}, fila, { actualizado:isoPg() });
  mapa.set(clave, n); avisar(tabla, n);
}
async function rutaREST(route) {
  const req = route.request(); const u = new URL(req.url()); const uid = uidDe(req);
  if (u.pathname === '/auth/v1/token') {
    refrescos++;
    const body = JSON.parse(req.postData()); const sub = body.refresh_token.split(':')[1];
    return route.fulfill({ json:{ access_token:jwt(sub, ahora()+3600), refresh_token:'rt' + refrescos + ':' + sub } });
  }
  if (!uid) return route.fulfill({ status:401, body:'no auth' });
  if (u.pathname === '/rest/v1/hogares') return route.fulfill({ json:[{ id:'H1' }] });
  const tabla = u.pathname.split('/').pop();
  const mapa = tabla === 'oposicion_temas' ? DB.temas : DB.prog;
  if (req.method() === 'GET') {
    let filas = [...mapa.values()];
    for (const [k, v] of u.searchParams) {
      if (['select','order','limit','offset'].includes(k)) continue;
      const [op, val] = [v.slice(0, v.indexOf('.')), v.slice(v.indexOf('.')+1)];
      if (op === 'eq') filas = filas.filter(f => String(f[k]) === val);
      if (op === 'gte') filas = filas.filter(f => Date.parse(f[k]) >= Date.parse(val));
    }
    if (tabla === 'oposicion_progreso') filas = filas.filter(f => f.user_id === uid);   // RLS
    filas.sort((a, b) => Date.parse(a.actualizado) - Date.parse(b.actualizado));
    const off = +u.searchParams.get('offset') || 0, lim = +u.searchParams.get('limit') || 1000;
    return route.fulfill({ json:filas.slice(off, off + lim) });
  }
  if (req.method() === 'POST') {
    posts++;
    let filas = JSON.parse(req.postData()); if (!Array.isArray(filas)) filas = [filas];
    for (const f of filas) {
      if (tabla === 'oposicion_progreso') { if (f.user_id !== uid) return route.fulfill({ status:403, body:'RLS' }); upsert(mapa, f.user_id + '|' + f.tarjeta, f, tabla); }
      else upsert(mapa, f.hogar_id + '|' + f.tema_id, f, tabla);
    }
    return route.fulfill({ status:201, body:'' });
  }
  route.fulfill({ status:400 });
}
async function rutaWS(ws) {
  let reg = null;
  ws.onMessage(m => {
    const msg = JSON.parse(m);
    if (msg.event === 'phx_join') {
      const pc = msg.payload.config.postgres_changes;
      const sub = JSON.parse(Buffer.from(msg.payload.access_token.split('.')[1], 'base64url')).sub;
      reg = { ws, topic:msg.topic, uid:sub, hogar:pc[0].filter.split('eq.')[1] };
      subs.add(reg);
      ws.send(JSON.stringify({ topic:msg.topic, event:'phx_reply', ref:msg.ref, payload:{ status:'ok', response:{ postgres_changes:pc.map((x, i) => Object.assign({ id:i }, x)) } } }));
    } else if (msg.event === 'heartbeat') ws.send(JSON.stringify({ topic:'phoenix', event:'phx_reply', ref:msg.ref, payload:{ status:'ok', response:{} } }));
  });
  ws.onClose(() => subs.delete(reg));
}

/* ---------------- Dispositivos ---------------- */
const errores = [];
async function dispositivo(browser, nombre, uid, exp) {
  const ctx = await browser.newContext({ viewport:{ width:1100, height:900 } });
  await ctx.route(SUPA + '/**', rutaREST);
  await ctx.routeWebSocket(/wss:\/\/mock\.supabase\.co\/.*/, rutaWS);
  await ctx.addInitScript(([url, tok, rt, uid]) => {
    try { if (location.protocol === 'about:' || window.top !== window) return; } catch (e) { return; }
    if (!localStorage.getItem('recetas:supabase'))
      localStorage.setItem('recetas:supabase', JSON.stringify({ url, anonKey:'anon', token:tok, refreshToken:rt, email:uid + '@x', userId:uid }));
  }, [SUPA, jwt(uid, exp || ahora() + 3600), 'rt0:' + uid, uid]);
  const p = await ctx.newPage();
  p.on('pageerror', e => errores.push(nombre + ': ' + e.message));
  p.on('console', m => { if (m.type() === 'error') errores.push(nombre + ' console: ' + m.text()); });
  await p.goto(BASE); await p.waitForTimeout(1200);
  return { ctx, p };
}
const pill = p => p.$eval('#sync-pill', e => e.dataset.estado + ' · ' + e.textContent.trim());
const temasDe = p => p.evaluate(() => Object.keys(estado.temas).sort().join(','));
const sabidasTot = p => p.evaluate(() => Object.values(estado.temas).reduce((n, t) => n + sabidasDe(t), 0));
async function esperar(fn, ms = 6000) { const t0 = Date.now(); while (Date.now() - t0 < ms) { if (await fn()) return Date.now() - t0; await new Promise(r => setTimeout(r, 100)); } return -1; }
const TEMA = `<!DOCTYPE html><html><head><script>window.TEMARIO_DATA={"IV.11":{"title":"LPAC","flashcards":[{"q":"Plazo general para resolver","a":"3 meses"},{"q":"Silencio en procedimientos a solicitud","a":"Estimatorio, con excepciones"}],"questions":[],"glossary":[{"t":"Silencio","d":"x"}]}};<\/script></head><body></body></html>`;


(async () => {
  const browser = await chromium.launch();
  const A = await dispositivo(browser, 'A', 'U1');
  const B = await dispositivo(browser, 'B', 'U1');
  const C = await dispositivo(browser, 'C', 'U2');
  const p = A.p;
  await p.evaluate(async () => {
    const t = normalizarTema('B4T11', {
      subtitle:'Ley 39/2015 y Ley 40/2015: procedimiento común, obligación de resolver y silencio',
      etiquetas:['LPAC', 'LRJSP', 'Silencio', 'Art. 21', 'Art. 24'],
      sections:[
        { id:'s1', nivel:1, title:'Contextualización', body:'Las leyes **39/2015** y **40/2015** sustituyeron a la Ley 30/1992 (BOE-A-2015-10565).\n\nObjetivos:\n- Administración electrónica\n- Simplificación' },
        { id:'s2', nivel:1, title:'La obligación de resolver', body:'La Administración está obligada a dictar resolución expresa en todos los procedimientos (art. 21 LPAC).' },
        { id:'s2a', nivel:2, title:'2.1 Plazos', body:'El plazo máximo no puede exceder de *seis meses* salvo ley o norma UE. Si no se fija, es de tres meses.' },
        { id:'s3', nivel:1, title:'El silencio administrativo', body:'En procedimientos iniciados a solicitud del interesado el silencio es, como regla general, estimatorio (art. 24).' }
      ],
      glossary:[{ t:'Silencio administrativo', d:'Ficción legal ante la falta de resolución expresa', section:'s3' }, { t:'Plazo máximo', d:'Seis meses salvo excepción', section:'s2a' }],
      timeline:[{ y:'1992', txt:'Ley 30/1992', cons:'Régimen anterior' }, { y:'2015', txt:'Leyes 39 y 40/2015', cons:'Régimen actual' }],
      flashcards:[{ q:'Plazo supletorio para resolver', a:'Tres meses' }, { q:'Regla general del silencio a solicitud', a:'Estimatorio' }],
      questions:[{ q:'Plazo máximo para resolver salvo ley', o:['3 meses','6 meses','1 año','10 días'], c:1, e:'Art. 21.2' }, { q:'Silencio a solicitud, regla general', o:['Desestimatorio','Estimatorio'], c:1, e:'Art. 24' }]
    }, '', null);
    await guardarTema(t);
  });
  await p.waitForTimeout(1500);
  await p.goto(BASE + '#/tema/B4T11/leer'); await p.waitForTimeout(500);
  console.log('apartados', await p.locator('.ap[data-ap]').count(), '| chips', await p.locator('.hero-chips span').count(), '| lateral visible', await p.locator('.estudio-lateral').isVisible());
  await p.click('.ap[data-ap="s2"] [data-toggle-btn]');
  await p.click('.ap[data-ap="s1"] [data-rep]');
  console.log('lectura A', await p.locator('.estudio-lateral [data-lectura-pct]').innerText());
  const t1 = await esperar(async () => await B.p.evaluate(() => repasada('B4T11', 's1')));
  console.log('repasada llega a B en', t1, 'ms | C (otra persona):', await C.p.evaluate(() => repasada('B4T11', 's1')));
  // B tiene la página abierta y recibe en vivo
  await B.p.goto(BASE + '#/tema/B4T11/leer'); await B.p.waitForTimeout(400);
  await p.click('.ap[data-ap="s3"] [data-rep]');
  await esperar(async () => (await B.p.locator('.estudio-lateral [data-lectura-pct]').innerText()) === '67%');
  console.log('B ve el % en vivo:', await B.p.locator('.estudio-lateral [data-lectura-pct]').innerText(), '| marca s3 en B:', await B.p.locator('.ap[data-ap="s3"]').getAttribute('class'));
  // Resaltar seleccionando texto
  await p.evaluate(() => {
    const el = document.querySelector('[data-cuerpo="s2a"] p'); const tn = [...el.childNodes].find(n => n.nodeType === 3 && n.nodeValue.includes('no puede exceder'));
    const r = document.createRange(); const i = tn.nodeValue.indexOf('no puede exceder'); r.setStart(tn, i); r.setEnd(tn, i + 'no puede exceder'.length);
    getSelection().removeAllRanges(); getSelection().addRange(r);
  });
  await p.waitForTimeout(150);
  console.log('botón resaltar visible', await p.locator('#barra-resaltar .btn-resaltar').isVisible());
  await p.click('#barra-resaltar .btn-resaltar');
  console.log('marcas res', await p.locator('mark.res').count());
  await esperar(async () => (await B.p.locator('mark.res').count()) > 0);
  console.log('resaltado en B en vivo:', await B.p.locator('mark.res').innerText());
  // Búsqueda
  await p.fill('.estudio-lateral [data-buscar]', 'silencio'); await p.waitForTimeout(500);
  console.log('búsqueda', await p.locator('.estudio-lateral [data-busq-n]').innerText(), '| abierto s3:', (await p.locator('.ap[data-ap="s3"]').getAttribute('class')).includes('abierto'));
  await p.screenshot({ path:__dirname + '/x1-escritorio.png', fullPage:false });
  await p.fill('.estudio-lateral [data-buscar]', ''); await p.waitForTimeout(400);
  // Herramientas
  for (const h of ['glosario','resaltados','test','fc','aleatorio','progreso','mapa','crono','voz']) {
    await p.click(`.estudio-lateral [data-herr="${h}"]`); await p.waitForTimeout(260);
    const txt = (await p.locator('#panel-cuerpo').innerText()).replace(/\s+/g, ' ').slice(0, 70);
    console.log('  ·', h, '→', txt);
    if (h === 'mapa' || h === 'progreso') await p.screenshot({ path:__dirname + `/x-${h}.png` });
    await p.click('#panel-cerrar'); await p.waitForTimeout(260);
  }
  // Test en el panel: fallar a propósito y luego modo "solo falladas"
  await p.click('.estudio-lateral [data-herr="test"]'); await p.waitForTimeout(250);
  await p.click('#t-go');
  for (let i = 0; i < 2; i++) { await p.locator('.q-opt').first().click(); await p.click('#t-sig'); }
  console.log('resultado test:', (await p.locator('.resultado').innerText()).split('\n')[0]);
  await p.click('#t-fin');
  console.log('chip falladas:', await p.locator('[data-modo="falladas"]').innerText());
  await p.click('#panel-cerrar'); await p.waitForTimeout(300);
  await esperar(async () => (await B.p.evaluate(() => resultadosTest(d => d.amb === 't:B4T11').length)) === 1);
  console.log('resultado del test en B:', await B.p.evaluate(() => JSON.stringify(resultadosTest(d => d.amb === 't:B4T11').map(x => x.a + '/' + x.n))), '| en C:', await C.p.evaluate(() => resultadosTest().length));
  // Móvil
  await p.setViewportSize({ width:390, height:844 }); await p.waitForTimeout(300);
  await p.goto(BASE + '#/tema/B4T11/leer'); await p.waitForTimeout(400);
  await p.screenshot({ path:__dirname + '/x2-movil.png', fullPage:false });
  await p.click('#fab-herr'); await p.waitForTimeout(300);
  await p.screenshot({ path:__dirname + '/x3-movil-panel.png', fullPage:false });
  await p.click('#panel [data-herr="fc"]'); await p.waitForTimeout(300);
  await p.screenshot({ path:__dirname + '/x4-movil-fc.png', fullPage:false });
  await p.click('#panel-cerrar'); await p.waitForTimeout(300);
  const ov = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth);
  console.log('overflow móvil', ov);
  // Oscuro
  await B.p.setViewportSize({ width:1280, height:900 });
  await B.p.evaluate(() => document.documentElement.setAttribute('data-tema', 'oscuro')); await B.p.click('.ap[data-ap="s1"] [data-toggle-btn]'); await B.p.waitForTimeout(300);
  await B.p.screenshot({ path:__dirname + '/x5-oscuro.png', fullPage:false });
  console.log('ERRORES', errores);
  await browser.close();
})();
