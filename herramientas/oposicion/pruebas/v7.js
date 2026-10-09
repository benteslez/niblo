const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs=[];
  for (const [nom, vp] of [['m', {width:390,height:844}], ['d', {width:1280,height:900}]]) {
    const p = await b.newPage({ viewport:vp }); p.on('pageerror', e => errs.push(e.message));
    await p.goto('http://localhost:8765/oposicion.html#/tema/B1T02/leer'); await p.waitForTimeout(2500);
    await p.click('[data-todo="1"]'); await p.waitForTimeout(500);
    const n = await p.evaluate(() => [...document.querySelectorAll('.ap-caja.trampa')].filter(x=>x.textContent.includes('Pregunta real')).length);
    console.log(nom, 'recuadros de pregunta real:', n, 'ov', await p.evaluate(()=>document.documentElement.scrollWidth-innerWidth));
    const loc = p.locator('.ap-caja.trampa', { hasText:'Pregunta real' }).first();
    await loc.scrollIntoViewIfNeeded(); await p.evaluate(()=>scrollBy(0,-80)); await p.waitForTimeout(200);
    await p.screenshot({ path:`ex-${nom}.png` });
    await p.close();
  }
  console.log('ERRORES', errs); await b.close();
})();
