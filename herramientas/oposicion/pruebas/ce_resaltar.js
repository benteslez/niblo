// Resaltados con colores en la Constitución (#/ce/texto). Requiere `python3 -m http.server 8765` en la raíz.
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs = []; let fallos = 0;
  const ok = (c, m) => { console.log(c ? 'OK ' : 'FALLA', m); if (!c) fallos++; };
  for (const [nombre, vp] of [['esc', { width:1280, height:900 }], ['mov', { width:390, height:800 }]]) {
    const ctx = await b.newContext({ viewport:vp }); const p = await ctx.newPage();
    p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type()==='error') errs.push(m.text()); });
    p.on('dialog', d => d.accept());
    await p.goto('http://localhost:8765/oposicion.html#/ce/texto/66'); await p.waitForTimeout(2800);
    const sel = async (art, ini, fin) => p.evaluate(([art, ini, fin]) => {
      const cont = document.querySelector(`[data-cer="a${art}"]`); const w = document.createTreeWalker(cont, NodeFilter.SHOW_TEXT); const n = w.nextNode();
      const r = document.createRange(); r.setStart(n, ini); r.setEnd(n, fin); const s = getSelection(); s.removeAllRanges(); s.addRange(r); document.dispatchEvent(new Event('selectionchange')); return r.toString();
    }, [art, ini, fin]);
    ok(await p.locator('[data-cer]').count() > 150, nombre + ': contenedores resaltables ' + await p.locator('[data-cer]').count());
    const t = await sel(66, 3, 20); await p.waitForTimeout(200);
    ok(await p.locator('#barra-resaltar-ce:not([hidden])').count() === 1 && await p.locator('#barra-resaltar-ce .res-col').count() === 5, nombre + ': aparece la barra con 5 colores («' + t.trim() + '»)');
    await p.locator('#barra-resaltar-ce [data-col="azul"].res-col').click(); await p.waitForTimeout(300);
    ok(await p.locator('mark.res[data-col="azul"]').count() >= 1, nombre + ': resaltado en azul');
    const t2 = await sel(67, 5, 30); await p.waitForTimeout(200);
    await p.locator('#barra-resaltar-ce [data-col="verde"].res-col').click(); await p.waitForTimeout(300);
    ok(await p.locator('mark.res[data-col="verde"]').count() >= 1 && await p.locator('mark.res').evaluateAll(m => new Set(m.map(x => x.dataset.col)).size) === 2, nombre + ': dos colores distintos');
    const col = await p.locator('mark.res[data-col="azul"]').first().evaluate(e => getComputedStyle(e).borderBottomColor);
    const col2 = await p.locator('mark.res[data-col="verde"]').first().evaluate(e => getComputedStyle(e).borderBottomColor);
    ok(col !== col2, nombre + ': los colores se ven distintos ' + col + ' / ' + col2);
    // persiste al recargar
    await p.reload(); await p.waitForTimeout(2800);
    ok(await p.locator('mark.res').count() >= 2, nombre + ': persisten al recargar');
    // quitar
    await p.locator('mark.res[data-col="azul"]').first().click(); await p.waitForTimeout(300);
    ok(await p.locator('mark.res[data-col="azul"]').count() === 0 && await p.locator('mark.res[data-col="verde"]').count() >= 1, nombre + ': pulsar quita solo ese resaltado');
    // una selección fuera del texto de un artículo no muestra la barra
    await p.evaluate(() => { const h = document.querySelector('.ce-nav'); const r = document.createRange(); r.selectNodeContents(h); const s = getSelection(); s.removeAllRanges(); s.addRange(r); document.dispatchEvent(new Event('selectionchange')); });
    await p.waitForTimeout(150);
    ok(await p.locator('#barra-resaltar-ce:not([hidden])').count() === 0, nombre + ': sin barra fuera del texto de los artículos');
    // los resaltados no afectan al apartado de los temas (otra clave)
    ok(await p.evaluate(() => Object.keys(prog.mapa).filter(k => k.startsWith('CE:res:')).length >= 1), nombre + ': guardado con clave CE:res:');
    await ctx.close();
  }
  console.log('errores de consola:', errs.length ? errs.join(' | ') : 'ninguno'); await b.close(); process.exit(fallos || errs.length ? 1 : 0);
})();
