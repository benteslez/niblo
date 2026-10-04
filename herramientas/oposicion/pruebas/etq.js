const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs=[];
  for (const [nom, vp] of [['d',{width:1280,height:900}],['m',{width:390,height:844}]]) {
    const p = await b.newPage({ viewport:vp }); p.on('pageerror', e => errs.push(e.message));
    await p.goto('http://localhost:8765/oposicion.html#/real'); await p.waitForTimeout(1200);
    await p.click('[data-modo="repaso"]'); await p.waitForTimeout(250); await p.click('dialog [data-empezar]'); await p.waitForTimeout(300);
    await p.evaluate(() => { const S = real.ses; const k = S.cola.findIndex(it => it.q.n === 4); const [it] = S.cola.splice(k, 1); S.cola.unshift(it); renderReal(); });
    const jc = await p.evaluate(() => { const it = real.ses.cola[0]; return it.ord.indexOf(it.q.c); });
    await p.locator('.q-opt').nth((jc+1)%4).click(); await p.waitForTimeout(150);
    const r1 = await p.evaluate(() => ({ etq:[...document.querySelectorAll('.q-opt')].map(o => (o.querySelector('.q-etq')||{}).innerText||'').filter(Boolean), boe:!!document.querySelector('.real-ley .tag-boe') }));
    console.log(nom, 'repaso fallo', JSON.stringify(r1));
    await p.screenshot({ path:`etq-${nom}.png` });
    await p.click('[data-cal="0"]'); await p.waitForTimeout(100);
    const j2 = await p.evaluate(() => { const it = real.ses.cola[real.ses.i]; return it.ord.indexOf(it.q.c); });
    await p.locator('.q-opt').nth(j2).click(); await p.waitForTimeout(150);
    console.log(nom, 'repaso acierto', JSON.stringify(await p.evaluate(() => [...document.querySelectorAll('.q-etq')].map(x=>x.innerText))));
    // apuntes I.2
    await p.goto('http://localhost:8765/oposicion.html#/tema/B1T02/leer'); await p.waitForTimeout(2500); await p.click('[data-todo="1"]'); await p.waitForTimeout(500); await p.locator('blockquote.literal').first().scrollIntoViewIfNeeded(); await p.screenshot({path:`boe-${nom}.png`});
    console.log(nom, 'apuntes', JSON.stringify(await p.evaluate(() => ({ lit:document.querySelectorAll('blockquote.literal').length, boe:document.querySelectorAll('blockquote.literal .lit-boe').length }))));
    console.log(nom, 'ov', await p.evaluate(()=>document.documentElement.scrollWidth-innerWidth));
    await p.close();
  }
  console.log('ERRORES', errs); await b.close();
})();
