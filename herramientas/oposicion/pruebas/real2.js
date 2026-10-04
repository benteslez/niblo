const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs=[];
  const p = await b.newPage({ viewport:{width:390,height:844} }); p.on('pageerror', e => errs.push(e.message));
  await p.goto('http://localhost:8765/_prueba_real.html#/real'); await p.waitForTimeout(1200);
  await p.screenshot({ path:'r-m-cfg.png', fullPage:true });
  await p.click('[data-md="simulacro"]'); await p.selectOption('#rn','0'); await p.click('#r-go'); await p.waitForTimeout(300);
  await p.locator('.q-opt').nth(1).click();
  await p.screenshot({ path:'r-m-sim.png' });
  await p.waitForTimeout(7500);
  console.log('tras agotar tiempo:', (await p.locator('#real-cuerpo').innerText()).replace(/\s+/g,' ').slice(0,120));
  console.log('ov', await p.evaluate(()=>document.documentElement.scrollWidth-innerWidth), 'ERRORES', errs); await b.close();
})();
