const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs=[];
  for (const [nom, vp, dark] of [['d', {width:1280,height:900}, false], ['m', {width:390,height:844}, false], ['o', {width:1280,height:900}, true]]) {
    const ctx = await b.newContext({ viewport:vp, colorScheme: dark?'dark':'light' }); const p = await ctx.newPage();
    p.on('pageerror', e => errs.push(nom+': '+e.message)); p.on('console', m => { if (m.type()==='error') errs.push(nom+' console: '+m.text()); });
    for (const [n,h] of [['inicio','#/'],['bloque','#/bloque/B1'],['hub','#/bloque/B1/hub'],['global','#/global'],['real','#/real']]) {
      if (nom!=='d' && !['inicio','bloque','real'].includes(n)) continue;
      await p.goto('http://localhost:8765/oposicion.html'+h); await p.waitForTimeout(1500);
      const ov = await p.evaluate(()=>document.documentElement.scrollWidth-innerWidth);
      if (ov) errs.push(nom+' '+n+' overflow '+ov);
      await p.screenshot({ path:`h-${nom}-${n}.png`, fullPage: n==='inicio' && nom==='d' });
    }
    await ctx.close();
  }
  console.log('ERRORES', errs); await b.close();
})();
