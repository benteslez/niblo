const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs=[];
  const p = await b.newPage({ viewport:{width:1280,height:900} }); p.on('pageerror', e => errs.push(e.message));
  for (const [n,h] of [['inicio','#/'],['bloque','#/bloque/B1'],['hub','#/bloque/B1/hub'],['global','#/global'],['tema','#/tema/B1T02']]) {
    await p.goto('http://localhost:8765/oposicion.html'+h); await p.waitForTimeout(1800);
    await p.screenshot({ path:`a0-${n}.png`, fullPage:false });
  }
  console.log('ERRORES', errs); await b.close();
})();
