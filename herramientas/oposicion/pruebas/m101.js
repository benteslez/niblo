const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
const OUT = process.env.SHOTS || '.';
(async () => {
  const b = await chromium.launch(); const errs = [];
  for (const [nombre, vp] of [['esc', { width:1280, height:900 }], ['mov', { width:390, height:800 }]]) {
    const p = await (await b.newContext({ viewport:vp })).newPage();
    p.on('pageerror', e => errs.push(nombre + ' pageerror: ' + e.message)); p.on('console', m => { if (m.type()==='error') errs.push(nombre + ' consola: ' + m.text()); });
    await p.goto('http://localhost:8765/oposicion.html#/bloque/B1'); await p.waitForTimeout(3000);
    console.log(nombre, 'tarjetas fusionadas (debe ser 0):', await p.locator('.tema2.pendiente:has-text("Fusionado")').count());
    await p.screenshot({ path:`${OUT}/${nombre}-b1.png` });
    await p.goto('http://localhost:8765/oposicion.html#/tema/B1T02'); await p.waitForTimeout(1500);
    console.log(nombre, 'I.2 se queda en', await p.evaluate(() => location.hash));
    await p.goto('http://localhost:8765/oposicion.html#/tema/B1T01/leer'); await p.waitForTimeout(2500);
    const txt = await p.locator('.estudio-main').innerText();
    console.log(nombre, 'leer: longitud', txt.length, '· "{{" sin interpretar:', (txt.match(/\{\{/g) || []).length, '· IMPORTANTE:', await p.locator('.pill-imp').count(), '· PRESCINDIBLE:', await p.locator('.pill-pre').count(), '· ce-tag:', await p.locator('.ce-tag').count(), '· literales:', await p.locator('blockquote.literal').count());
    console.log(nombre, 'desborde:', await p.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1));
    await p.screenshot({ path:`${OUT}/${nombre}-leer0.png` });
    for (const t of ['II.2 Los títulos', 'IV.5 Cuadro comparativo']) {
      const h = p.locator(`h2:has-text("${t}"), h3:has-text("${t}")`).first(); if (await h.count()) { await h.evaluate(e => { let n = e; while (n && n.closest) { const d = n.closest('details'); if (!d) break; d.open = true; n = d.parentElement; } e.scrollIntoView({ block:'start' }); }); await p.waitForTimeout(300); await p.screenshot({ path:`${OUT}/${nombre}-leer-${t.slice(0,4).replace(/\W/g,'')}.png` }); } else console.log('no encontrado', t);
    }
  }
  console.log('ERRORES', errs); await b.close();
})();
