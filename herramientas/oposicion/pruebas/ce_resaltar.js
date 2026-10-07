// Resaltados con colores en la Constitución (#/ce/texto). Requiere `python3 -m http.server 8765` en la raíz.
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs = []; let fallos = 0;
  const ok = (c, m) => { console.log(c ? 'OK ' : 'FALLA', m); if (!c) fallos++; };
  for (const [nombre, vp] of [['esc', { width:1280, height:900 }], ['mov', { width:390, height:800 }]]) {
    const ctx = await b.newContext({ viewport:vp }); const p = await ctx.newPage();
    p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type()==='error') errs.push(m.text()); });
        await p.goto('http://localhost:8765/oposicion.html#/ce/texto/66'); await p.waitForTimeout(2800);
    const sel = async (art, ini, fin) => p.evaluate(([art, ini, fin]) => {
      const cont = document.querySelector(`[data-cer="a${art}"]`); const w = document.createTreeWalker(cont, NodeFilter.SHOW_TEXT); const n = w.nextNode();
      const r = document.createRange(); r.setStart(n, ini); r.setEnd(n, fin); const s = getSelection(); s.removeAllRanges(); s.addRange(r); document.dispatchEvent(new Event('selectionchange')); return r.toString();
    }, [art, ini, fin]);
    ok(await p.locator('[data-cer]').count() > 150, nombre + ': contenedores resaltables ' + await p.locator('[data-cer]').count());
    const t = await sel(66, 3, 20); await p.waitForTimeout(200);
    ok(await p.locator('#barra-resaltar-ce:not([hidden])').count() === 1 && await p.locator('#barra-resaltar-ce .res-col').count() === 5, nombre + ': aparece la barra con 5 colores («' + t.trim() + '»)');
    const pos = await p.evaluate(() => { const r = getSelection().getRangeAt(0).getBoundingClientRect(), b = document.getElementById('barra-resaltar-ce').getBoundingClientRect(); return { selBottom:r.bottom, selTop:r.top, barTop:b.top, barBottom:b.bottom, alto:innerHeight }; });
    ok(pos.barTop > pos.selBottom, nombre + ': la barra sale por debajo de la selección (' + Math.round(pos.selBottom) + ' → ' + Math.round(pos.barTop) + ')');
    ok(pos.barBottom <= pos.alto, nombre + ': cabe en pantalla');
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
    // pulsar un resaltado abre un menú: cambiar de color o quitarlo
    await p.locator('mark.res[data-col="azul"]').first().click(); await p.waitForTimeout(200);
    ok(await p.locator('#menu-res').count() === 1 && await p.locator('#menu-res .res-col').count() === 5 && await p.locator('#menu-res [data-mr-del]').count() === 1, nombre + ': el menú ofrece 5 colores y «Quitar»');
    ok(await p.locator('#menu-res .res-col.on').getAttribute('data-col') === 'azul', nombre + ': marca el color actual');
    await p.locator('#menu-res [data-mr-col="rosa"]').click(); await p.waitForTimeout(250);
    ok(await p.locator('mark.res[data-col="rosa"]').count() === 1 && await p.locator('mark.res[data-col="azul"]').count() === 0 && await p.locator('#menu-res').count() === 0, nombre + ': cambia de azul a rosa y se cierra');
    await p.reload(); await p.waitForTimeout(2800);
    ok(await p.locator('mark.res[data-col="rosa"]').count() === 1, nombre + ': el color nuevo persiste');
    await p.locator('mark.res[data-col="rosa"]').first().click(); await p.waitForTimeout(200);
    await p.locator('#menu-res [data-mr-del]').click(); await p.waitForTimeout(250);
    ok(await p.locator('mark.res[data-col="rosa"]').count() === 0 && await p.locator('mark.res[data-col="verde"]').count() >= 1, nombre + ': «Quitar» borra solo ese resaltado');
    await p.locator('mark.res[data-col="verde"]').first().click(); await p.waitForTimeout(150);
    await p.keyboard.press('Escape'); await p.waitForTimeout(100);
    ok(await p.locator('#menu-res').count() === 0 && await p.locator('mark.res[data-col="verde"]').count() >= 1, nombre + ': Esc cierra el menú sin cambios');
    // en los apuntes de un tema funciona igual
    await p.goto('http://localhost:8765/oposicion.html#/tema/B1T02/leer'); await p.waitForTimeout(2800);
    const ap = await p.evaluate(() => { const t = estado.temas.B1T02, s = t.sections.find(x => /derechos/i.test(x.body) && x.body.length > 400); const k = 'B1T02:res:testmenu'; const sec = s.id; const frase = (String(s.body).match(/[A-Za-zÁÉÍÓÚáéíóúñ]{6,} [A-Za-zÁÉÍÓÚáéíóúñ]{6,}/) || [''])[0]; return { sec, frase }; });
    if (ap.frase) {
      await p.evaluate(a => { irASeccion(a.sec, true); marcarProg('B1T02:res:testmenu', true, { sec:a.sec, x:a.frase, col:'amarillo' }); pintarResaltados('B1T02'); }, ap); await p.waitForTimeout(500);
      const m = p.locator('mark.res[data-col="amarillo"]').first();
      if (await m.count()) {
        await m.scrollIntoViewIfNeeded(); await m.click(); await p.waitForTimeout(200);
        await p.locator('#menu-res [data-mr-col="verde"]').click(); await p.waitForTimeout(250);
        ok(await p.locator('mark.res[data-col="verde"]').count() >= 1, nombre + ': en los apuntes también cambia de color');
        await p.evaluate(() => marcarProg('B1T02:res:testmenu', false, null));
      } else ok(false, nombre + ': no se pudo crear el resaltado de prueba en los apuntes');
    }
    await p.goto('http://localhost:8765/oposicion.html#/ce/texto/66'); await p.waitForTimeout(2800);
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
