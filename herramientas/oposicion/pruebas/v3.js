const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch();
  for (const [nom, vp] of [['m', {width:390,height:844}], ['d', {width:1280,height:900}]]) {
    const p = await b.newPage({ viewport:vp });
    await p.goto('http://localhost:8765/oposicion.html#/tema/B1T02/leer'); await p.waitForTimeout(2500);
    console.log(nom, await p.evaluate(() => ({ bq:document.querySelectorAll('blockquote.literal').length, aps:document.querySelectorAll('.ap-cuerpo').length, det:document.querySelectorAll('details').length, h:location.hash, t:document.body.innerText.includes('Artículo 30.') })));
    const el = p.locator('blockquote.literal').nth(20);
    if (await el.count()) { await p.click('[data-todo="1"]'); await p.waitForTimeout(300); await el.scrollIntoViewIfNeeded(); await p.waitForTimeout(300); }
    await p.screenshot({ path:`lit-${nom}.png` });
    await p.close();
  }
  await b.close();
})();
