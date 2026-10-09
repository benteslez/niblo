const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs=[];
  for (const [nom, vp] of [['m', {width:390,height:844}], ['d', {width:1280,height:900}]]) {
    const p = await b.newPage({ viewport:vp }); p.on('pageerror', e => errs.push(e.message));
    await p.goto('http://localhost:8765/oposicion.html#/tema/B1T02/leer'); await p.waitForTimeout(2000);
    await p.click('[data-todo="1"]'); await p.waitForTimeout(400);
    const info = await p.evaluate(() => ({ h4:document.querySelectorAll('h4.ap-h').length, cajas:document.querySelectorAll('.ap-caja').length, lit:document.querySelectorAll('blockquote.literal').length, aps:document.querySelectorAll('.ap[data-ap]').length, ov:document.documentElement.scrollWidth-innerWidth }));
    console.log(nom, JSON.stringify(info));
    for (const [i,sel] of [[1,'h4.ap-h >> nth=8'],[2,'.ap-caja.trampa >> nth=3'],[3,'h4.ap-h >> nth=40']]) {
      await p.locator(sel).scrollIntoViewIfNeeded(); await p.waitForTimeout(200);
      await p.screenshot({ path:`ap-${nom}-${i}.png` });
    }
    await p.close();
  }
  console.log('ERRORES', errs); await b.close();
})();
