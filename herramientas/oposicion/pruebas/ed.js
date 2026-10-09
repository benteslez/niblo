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
  const p = A.p;
  await p.setViewportSize({ width:390, height:844 });
  await p.goto(BASE + '#/tema/B1T02'); await p.waitForTimeout(400);
  await p.screenshot({ path:__dirname + '/e1-ficha.png', fullPage:true });
  await p.click('text=Empezar a desarrollar'); await p.waitForTimeout(300);
  console.log('ruta', await p.evaluate(() => location.hash), '| creado sin escribir?', await p.evaluate(() => !!estado.temas.B1T02));
  await p.click('[data-acc="anadir"]');
  await p.fill('.ed-item[data-i] [data-k="title"]', '1. Los derechos fundamentales en la CE');
  await p.fill('.ed-item[data-i] [data-k="body"]', 'El **Título I** (arts. 10-55) regula los derechos.\n\n- Sección 1.ª: derechos fundamentales y libertades públicas\n- Sección 2.ª: derechos y deberes de los ciudadanos\n\nLO 4/1981 BOE-A-1981-12774.');
  await p.click('[data-acc="anadir-sub"]');
  await p.locator('.ed-item[data-i]').nth(1).locator('[data-k="title"]').fill('1.1 Garantías (art. 53)');
  await p.locator('.ed-item[data-i]').nth(1).locator('[data-k="body"]').fill('Reserva de ley, recurso de amparo y *principios rectores*.');
  await p.click('[data-edtab="fc"]');
  await p.click('[data-acc="pegar"]');
  await p.fill('#ed-pegar-txt', 'Artículos del Título I | 10 a 55\n¿Quién nombra al Defensor del Pueblo? | Las Cortes Generales (art. 54 CE)\nlínea sin separador');
  await p.click('[data-acc="pegar-ok"]');
  await p.click('[data-edtab="test"]');
  await p.click('[data-acc="anadir"]');
  await p.fill('.ed-item [data-k="q"]', '¿Qué artículo regula la suspensión de derechos?');
  for (const [j, v] of [[0,'Art. 53'],[1,'Art. 55'],[2,'Art. 116'],[3,'']]) await p.fill(`.ed-item [data-k="o.${j}"]`, v);
  await p.check('.ed-item input[type=radio][value="1"]');
  await p.screenshot({ path:__dirname + '/e2-test.png', fullPage:true });
  await p.click('[data-acc="anadir"]');      // pregunta vacía a medias
  await p.fill('.ed-item >> nth=1 >> [data-k="q"]', 'Pregunta a medias');
  await p.waitForTimeout(900);
  const t = await p.evaluate(() => { const t = estado.temas.B1T02; return { sec:t.sections.length, fc:t.flashcards.length, fcOk:fcs(t).length, q:t.questions.length, qOk:qs(t).length, c:qs(t)[0] && qs(t)[0].c, o:qs(t)[0] && qs(t)[0].o.length }; });
  console.log('guardado', JSON.stringify(t));
  await p.click('text=Listo'); await p.waitForTimeout(300);
  await p.screenshot({ path:__dirname + '/e3-ficha-llena.png', fullPage:true });
  await p.click('text=Leer apuntes'); await p.waitForTimeout(300);
  await p.click('[data-todo="1"]');
  console.log('lectura: apartados', await p.locator('.ap[data-ap]').count(), 'sub h3', await p.locator('.ap-sub h3').count(), 'li', await p.locator('.ap-cuerpo li').count(), 'strong', await p.locator('.ap-cuerpo strong').count(), 'boe', await p.locator('.ap-cuerpo a[href*="BOE-A-1981-12774"]').count(), 'em', await p.locator('.ap-cuerpo em').count());
  await p.screenshot({ path:__dirname + '/e4-leer.png', fullPage:true });
  // Llega a B
  const ms = await esperar(async () => await B.p.evaluate(() => !!(estado.temas.B1T02 && estado.temas.B1T02.sections.length === 2 && estado.temas.B1T02.flashcards.length === 2)));
  console.log('llega a B en', ms, 'ms');
  // Test en hub con la pregunta válida (3 opciones)
  await p.goto(BASE + '#/bloque/B1/hub'); await p.click('[data-tab="test"]');
  console.log('test disponibles:', await p.locator('#t-go').isEnabled(), (await p.locator('.test-cfg .muted').innerText()));
  // B escribe mientras llega un cambio de A: no se pierde el foco ni lo escrito
  await B.p.goto(BASE + '#/tema/B1T02/editar'); await B.p.waitForTimeout(300);
  await B.p.locator('.ed-item [data-k="body"]').first().click();
  await B.p.keyboard.press('Control+End'); await B.p.keyboard.type(' Añadido en B.');
  await p.evaluate(() => { const t = estado.temas.B1T02; t.glossary.push({ t:'Amparo', d:'Recurso ante el TC' }); guardarTema(t); });
  await B.p.waitForTimeout(2500);
  console.log('B sigue escribiendo:', await B.p.evaluate(() => document.activeElement.dataset.k), '| texto conservado:', await B.p.evaluate(() => estado.temas.B1T02.sections[0].body.endsWith('Añadido en B.')));
  await B.p.click('text=Listo'); await B.p.waitForTimeout(2500);
  console.log('A tiene lo de B:', await p.evaluate(() => estado.temas.B1T02.sections[0].body.endsWith('Añadido en B.')), '| y conserva su glosario:', await p.evaluate(() => estado.temas.B1T02.glossary.map(g => g.t).join()), '| B igual:', await B.p.evaluate(() => estado.temas.B1T02.glossary.map(g => g.t).join()));
  // Los dos sin conexión: A añade glosario, B añade una flashcard. Al volver, ambos.
  await A.ctx.setOffline(true); await B.ctx.setOffline(true); await p.waitForTimeout(300);
  await p.goto(BASE + '#/tema/B1T02/editar'); await p.click('[data-edtab="glosario"]'); await p.click('[data-acc="anadir"]');
  await p.fill('.ed-item >> nth=-1 >> [data-k="t"]', 'Defensor del Pueblo'); await p.fill('.ed-item >> nth=-1 >> [data-k="d"]', 'Alto comisionado de las Cortes (art. 54 CE)');
  await B.p.goto(BASE + '#/tema/B1T02/editar'); await B.p.click('[data-edtab="fc"]'); await B.p.click('[data-acc="anadir"]');
  await B.p.fill('.ed-item >> nth=-1 >> [data-k="q"]', 'Mayoría para elegir al Defensor'); await B.p.fill('.ed-item >> nth=-1 >> [data-k="a"]', '3/5 de cada Cámara');
  await p.click('text=Listo'); await B.p.click('text=Listo'); await p.waitForTimeout(900);
  await B.ctx.setOffline(false); await B.p.waitForTimeout(2500);
  await A.ctx.setOffline(false);
  const ok = await esperar(async () => {
    const f = x => x.evaluate(() => { const t = estado.temas.B1T02; return t.glossary.map(g => g.t).sort().join('+') + ' / ' + t.flashcards.length + ' fc'; });
    const a = await f(p), b = await f(B.p); return a === b && a.includes('Defensor') && a.includes('3 fc') ? a : false;
  }, 15000);
  const f = x => x.evaluate(() => { const t = estado.temas.B1T02; return t.glossary.map(g => g.t).sort().join('+') + ' / ' + t.flashcards.length + ' fc / pendientes ' + nPendientes(); });
  console.log('sin conexión, partes distintas → A:', await f(p), '| B:', await f(B.p), '| convergen en', ok, 'ms');
  console.log('servidor:', DB.temas.get('H1|B1T02').datos.glossary.map(g => g.t).join('+'), '/', DB.temas.get('H1|B1T02').datos.flashcards.length, 'fc');
  console.log('ERRORES', errores);
  await browser.close();
})();
