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
  await A.p.waitForTimeout(1500);
  const r = await A.p.evaluate(() => { const t = estado.temas.B1T02; return t ? { ap:apartados(t).length, sec:t.sections.length, gl:t.glossary.length, tl:t.timeline.length, fc:fcs(t).length, q:qs(t).length, chips:t.etiquetas.length } : null; });
  console.log('importado en A:', JSON.stringify(r), '| servidor tiene B1T02:', DB.temas.has('H1|B1T02'));
  const B = await dispositivo(browser, 'B', 'U1');
  await B.p.waitForTimeout(1200);
  console.log('B lo tiene:', await B.p.evaluate(() => !!estado.temas.B1T02 && estado.temas.B1T02.sections.length), '| filas servidor:', DB.temas.size, '| POSTs:', posts);
  await A.p.goto(BASE + '#/tema/B1T02/leer'); await A.p.waitForTimeout(500);
  await A.p.click('[data-todo="1"]'); await A.p.waitForTimeout(200);
  console.log('tablas renderizadas:', await A.p.locator('.apuntes-tabla').count(), '| apartados:', await A.p.locator('.ap[data-ap]').count(), '| enlaces BOE:', await A.p.locator('.ap-cuerpo a[href*="boe.es"]').count());
  await A.p.screenshot({ path:__dirname + '/t1.png' });
  await A.p.evaluate(() => document.getElementById('sec-s6-7').scrollIntoView()); await A.p.waitForTimeout(200);
  await A.p.screenshot({ path:__dirname + '/t2.png' });
  await A.p.fill('.estudio-lateral [data-buscar]', 'setenta y dos'); await A.p.waitForTimeout(400);
  console.log('búsqueda "setenta y dos":', await A.p.locator('.estudio-lateral [data-busq-n]').innerText());
  await A.p.fill('.estudio-lateral [data-buscar]', '72 horas'); await A.p.waitForTimeout(400);
  console.log('búsqueda "72 horas":', await A.p.locator('.estudio-lateral [data-busq-n]').innerText());
  await A.p.fill('.estudio-lateral [data-buscar]', ''); await A.p.waitForTimeout(300);
  await A.p.click('.estudio-lateral [data-herr="mapa"]'); await A.p.waitForTimeout(300);
  await A.p.screenshot({ path:__dirname + '/t3-mapa.png' });
  await A.p.click('#panel-cerrar'); await A.p.waitForTimeout(300);
  await A.p.click('.estudio-lateral [data-herr="test"]'); await A.p.waitForTimeout(300);
  console.log('test:', (await A.p.locator('#panel .test-cfg .muted').innerText()));
  await A.p.click('#panel-cerrar'); await A.p.waitForTimeout(300);
  // Móvil
  await A.p.setViewportSize({ width:390, height:844 }); await A.p.goto(BASE + '#/tema/B1T02/leer'); await A.p.waitForTimeout(500);
  await A.p.evaluate(() => { alternarApartado(document.querySelector('.ap[data-ap="bII"]'), true); document.getElementById('sec-s5-3').scrollIntoView(); }); await A.p.waitForTimeout(200);
  await A.p.screenshot({ path:__dirname + '/t4-movil.png' });
  console.log('overflow móvil:', await A.p.evaluate(() => document.documentElement.scrollWidth - innerWidth));
  // Recargar: no se reimporta
  await A.p.reload(); await A.p.waitForTimeout(800);
  console.log('tras recargar POSTs:', posts);
  console.log('ERRORES', errores);
  await browser.close();
})();
