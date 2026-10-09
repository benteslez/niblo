const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs = [];
  for (const [nom, vp] of [['m', {width:390,height:844}], ['d', {width:1280,height:900}]]) {
    const p = await b.newPage({ viewport:vp }); p.on('pageerror', e => errs.push(e.message));
    await p.goto('http://localhost:8765/oposicion.html#/tema/B1T02/leer'); await p.waitForTimeout(1500);
    const n = await p.locator('blockquote.literal').count();
    // abrir apartado 4.1 (literal)
    const cab = p.locator('text=Sección 2.ª').first(); if (await cab.count()) { await cab.click().catch(()=>{}); }
    await p.waitForTimeout(400);
    const bq = p.locator('blockquote.literal:visible').first();
    if (await bq.count()) await bq.scrollIntoViewIfNeeded();
    await p.screenshot({ path:`lit-${nom}.png` });
    const ov = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth);
    console.log(nom, 'bloques literales', n, 'overflow', ov);
    await p.close();
  }
  const p = await b.newPage({ viewport:{width:390,height:844} }); p.on('pageerror', e => errs.push(e.message));
  await p.goto('http://localhost:8765/oposicion.html#/bloque/B1/hub'); await p.waitForTimeout(1500);
  const t = p.locator('text=Test').first(); await t.click().catch(()=>{}); await p.waitForTimeout(400);
  const chip = p.locator('[data-modo="reales"]'); console.log('chip reales:', await chip.count() ? await chip.innerText() : 'NO');
  if (await chip.count()) { await chip.click(); await p.waitForTimeout(200); await p.click('#t-go'); await p.waitForTimeout(300);
    console.log('etiqueta:', await p.locator('.q-meta .tag.hot').innerText().catch(()=>'NO'));
    await p.locator('.q-opt').first().click(); await p.waitForTimeout(200);
    console.log('fb:', (await p.locator('.q-fb').innerText()).slice(0,300));
    await p.screenshot({ path:'real-m.png' }); }
  console.log('ERRORES', errs); await b.close();
})();
