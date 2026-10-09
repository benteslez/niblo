const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs=[];
  for (const [nom, vp, dark] of [['m',{width:390,height:844},false],['o',{width:390,height:844},true]]) {
    const ctx = await b.newContext({ viewport:vp, colorScheme:dark?'dark':'light' }); const p = await ctx.newPage(); p.on('pageerror', e => errs.push(e.message));
    await p.goto('http://localhost:8765/oposicion.html#/real'); await p.waitForTimeout(1200);
    await p.click('[data-modo="repaso"]'); await p.waitForTimeout(300);
    await p.screenshot({ path:`s-${nom}-dlg.png` });
    await p.click('dialog [data-empezar]'); await p.waitForTimeout(300);
    await p.locator('.q-opt').nth(0).click(); await p.waitForTimeout(150);
    await p.screenshot({ path:`s-${nom}-ses.png` });
    console.log(nom, 'ov', await p.evaluate(()=>document.documentElement.scrollWidth-innerWidth));
    await ctx.close();
  }
  console.log('ERRORES', errs); await b.close();
})();
