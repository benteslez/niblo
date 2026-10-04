const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs=[];
  for (const [nom, vp, dark] of [['m', {width:390,height:844}, false], ['d', {width:1280,height:900}, false], ['o', {width:1280,height:900}, true]]) {
    const ctx = await b.newContext({ viewport:vp, colorScheme: dark?'dark':'light' }); const p = await ctx.newPage(); p.on('pageerror', e => errs.push(e.message));
    await p.goto('http://localhost:8765/oposicion.html#/tema/B1T02/leer'); await p.waitForTimeout(2500);
    await p.click('[data-todo="1"]'); await p.waitForTimeout(500);
    const q = p.locator('.ap-quiz').first();
    const antes = await q.evaluate(x => ({ ops:x.querySelectorAll('.qz-op').length, expVis:[...x.querySelectorAll('.qz-exp,.qz-sol')].filter(e=>!e.hidden).length, verde:x.querySelectorAll('.bien').length, texto:x.innerText.includes('Respuesta correcta') }));
    await q.scrollIntoViewIfNeeded(); await p.evaluate(()=>scrollBy(0,-70)); await p.waitForTimeout(150);
    if (nom==='d') await p.screenshot({ path:'qz-antes.png' });
    await q.locator('.qz-op').nth(2).click(); await p.waitForTimeout(200);   // c) incorrecta
    const tras = await q.evaluate(x => ({ mal:[...x.querySelectorAll('.qz-op.mal')].map(b=>b.innerText.slice(0,3)), bien:[...x.querySelectorAll('.qz-op.bien')].map(b=>b.innerText.slice(0,3)), expVis:[...x.querySelectorAll('.qz-exp,.qz-sol')].filter(e=>!e.hidden).length, res:x.querySelector('.qz-res')?.innerText, deshab:[...x.querySelectorAll('.qz-op')].every(b=>b.disabled) }));
    await p.screenshot({ path:`qz-${nom}-mal.png` });
    await q.locator('.qz-otra').click(); await p.waitForTimeout(150);
    await q.locator('.qz-op').nth(0).click(); await p.waitForTimeout(150);   // a) correcta
    const ok = await q.evaluate(x => ({ mal:x.querySelectorAll('.qz-op.mal').length, res:x.querySelector('.qz-res')?.innerText }));
    if (nom!=='o') await p.screenshot({ path:`qz-${nom}-bien.png` });
    console.log(nom, JSON.stringify({antes, tras, ok, n:await p.locator('.ap-quiz').count(), ov:await p.evaluate(()=>document.documentElement.scrollWidth-innerWidth)}));
    await ctx.close();
  }
  console.log('ERRORES', errs); await b.close();
})();
