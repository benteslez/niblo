// «Descargar apuntes» de la Constitución: casillas para incluir tus resaltados y las leyendas. Requiere `python3 -m http.server 8765` en la raíz.
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs = []; let fallos = 0;
  const ok = (c, m) => { console.log(c ? 'OK ' : 'FALLA', m); if (!c) fallos++; };
  for (const [nombre, vp] of [['esc', { width:1280, height:900 }], ['mov', { width:390, height:800 }]]) {
    const ctx = await b.newContext({ viewport:vp }); const p = await ctx.newPage();
    p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type()==='error') errs.push(m.text()); });
    await p.goto('http://localhost:8765/oposicion.html#/ce/texto'); await p.waitForTimeout(2800);
    ok(await p.locator('[data-ce-pdf="res"]:checked').count() === 1 && await p.locator('[data-ce-pdf="ley"]:checked').count() === 1, nombre + ': dos casillas, marcadas por defecto');
    // un resaltado propio en el art. 1
    await p.evaluate(() => { marcarProg('CE:res:test1', true, { sec:'a1', x:'Estado social y democrático', col:'verde' }); });
    const gen = o => p.evaluate(async o => { await ceCargar(); const m = CEV.m103; CEV.m103 = o.ley; try { return ceApuntesHTML(o); } finally { CEV.m103 = m; } }, o);
    const todo = await gen({ res:true, ley:true }), sinRes = await gen({ res:false, ley:true }), sinLey = await gen({ res:true, ley:false });
    ok(/mark class="res" data-col="verde"/.test(todo), nombre + ': con resaltados salen en el documento');
    ok(!/mark class="res"/.test(sinRes), nombre + ': sin la casilla no salen');
    ok(/Cómo estudiar los/.test(todo) && /m103-pill/.test(todo) && /m103-nota/.test(todo), nombre + ': con leyendas: sección 1, pills y comentarios');
    ok(!/Cómo estudiar los/.test(sinLey) && !/<div class="ca-h">[^]*?m103-pill/.test(sinLey.slice(sinLey.indexOf('Constitución completa'))) && !/class="m103-nota/.test(sinLey) && !/<mark class="m103-/.test(sinLey) && /<mark class="m103-/.test(todo), nombre + ': sin leyendas: nada de la academia');
    const secs = s => [...s.matchAll(/<div class="k">Sección (\d)<\/div>/g)].map(x => +x[1]).join('');
    ok(secs(todo) === '123456' && secs(sinLey) === '12345', nombre + ': numeración de secciones ' + secs(todo) + ' / ' + secs(sinLey));
    ok(/data-cer="pre"/.test(sinLey) && /Estado social y democrático/.test(sinLey), nombre + ': el texto literal sigue completo');
    // la casilla guarda la preferencia
    await p.locator('[data-ce-pdf="ley"]').uncheck(); await p.locator('[data-ce-pdf="res"]').uncheck();
    ok(await p.evaluate(() => { const o = cePdfOpc(); return o.ley === false && o.res === false; }), nombre + ': preferencia guardada');
    await p.reload(); await p.waitForTimeout(2500);
    ok(await p.locator('[data-ce-pdf]:checked').count() === 0, nombre + ': se recuerda al recargar');
    ok(!(await p.evaluate(() => document.documentElement.scrollWidth > innerWidth + 2)), nombre + ': sin desbordamiento horizontal');
    await ctx.close();
  }
  console.log('errores de consola:', errs.length ? errs.join(' | ') : 'ninguno'); await b.close(); process.exit(fallos || errs.length ? 1 : 0);
})();
