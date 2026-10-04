const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs=[];
  const p = await b.newPage({ viewport:{width:390,height:844} }); p.on('pageerror', e => errs.push(e.message));
  await p.goto('http://localhost:8765/oposicion.html#/real'); await p.waitForTimeout(1200);
  await p.click('[data-modo="repaso"]'); await p.waitForTimeout(250); await p.click('dialog [data-empezar]'); await p.waitForTimeout(300);
  const res = {};
  for (const n of [23, 102, 58]) {
    await p.evaluate(n => { const S = real.ses; const k = S.cola.findIndex(it => it.q.n === n); const [it] = S.cola.splice(k, 1); S.cola.splice(S.i, 0, it); renderReal(); }, n);
    const jc = await p.evaluate(() => { const it = real.ses.cola[real.ses.i]; return it.ord.indexOf(it.q.c); });
    await p.locator('.q-opt').nth((jc+1)%4).click(); await p.waitForTimeout(150);
    res[n] = await p.evaluate(() => { const d = document.querySelector('.real-ley'); return d && { abierto:d.open, etq:[...d.querySelectorAll('.tag-boe')].map(x=>x.textContent).join(','), href:d.querySelector('.ley-t a').href, bloques:d.querySelectorAll('blockquote').length, neg:d.querySelectorAll('strong').length, ini:d.innerText.replace(/\s+/g,' ').slice(0,160) }; });
    if (n === 23) { await p.locator('.real-ley').scrollIntoViewIfNeeded(); await p.screenshot({ path:'n58.png' }); }
    res[n].ov = await p.evaluate(()=>document.documentElement.scrollWidth-innerWidth);
    await p.click('[data-cal="0"]'); await p.waitForTimeout(100);
  }
  console.log(JSON.stringify(res, null, 1)); console.log('ERRORES', errs); await b.close();
})();
