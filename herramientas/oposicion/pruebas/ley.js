const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs=[];
  for (const [nom, vp] of [['d',{width:1280,height:900}],['m',{width:390,height:844}]]) {
    const p = await b.newPage({ viewport:vp }); p.on('pageerror', e => errs.push(e.message));
    await p.goto('http://localhost:8765/oposicion.html#/real'); await p.waitForTimeout(1200);
    await p.click('[data-modo="repaso"]'); await p.waitForTimeout(250); await p.click('dialog [data-empezar]'); await p.waitForTimeout(300);
    // Ir a la pregunta 4 y fallarla
    await p.evaluate(() => { const S = real.ses; const k = S.cola.findIndex(it => it.q.n === 4); const [it] = S.cola.splice(k, 1); S.cola.unshift(it); renderReal(); });
    await p.waitForTimeout(200);
    const jc = await p.evaluate(() => { const it = real.ses.cola[0]; return it.ord.indexOf(it.q.c); });
    await p.locator('.q-opt').nth((jc+1)%4).click(); await p.waitForTimeout(150);
    console.log(nom, 'fallo →', JSON.stringify(await p.evaluate(() => { const d = document.querySelector('.real-ley'); return { abierto:d && d.open, texto:d && d.innerText.replace(/\s+/g,' ') }; })));
    await p.locator('.real-ley').scrollIntoViewIfNeeded(); await p.screenshot({ path:`l-${nom}.png` });
    await p.click('[data-cal="0"]'); await p.waitForTimeout(100);
    // Acierto en la 13 (con dos bloques): plegado
    await p.evaluate(() => { const S = real.ses; const k = S.cola.findIndex(it => it.q.n === 13); const [it] = S.cola.splice(k, 1); S.cola.splice(S.i, 0, it); renderReal(); });
    const j2 = await p.evaluate(() => { const it = real.ses.cola[real.ses.i]; return it.ord.indexOf(it.q.c); });
    await p.locator('.q-opt').nth(j2).click(); await p.waitForTimeout(150);
    console.log(nom, 'acierto 13 →', JSON.stringify(await p.evaluate(() => { const d = document.querySelector('.real-ley'); return { abierto:d.open, bloques:d.querySelectorAll('blockquote').length }; })));
    // Sin texto legal (p. ej. la 17): no aparece nada
    await p.click('[data-cal="5"]'); await p.waitForTimeout(100);
    await p.evaluate(() => { const S = real.ses; const k = S.cola.findIndex(it => it.q.n === 17); const [it] = S.cola.splice(k, 1); S.cola.splice(S.i, 0, it); renderReal(); });
    await p.locator('.q-opt').first().click(); await p.waitForTimeout(100);
    console.log(nom, 'pregunta 17 sin texto legal →', await p.evaluate(() => !document.querySelector('.real-ley')));
    console.log(nom, 'ov', await p.evaluate(()=>document.documentElement.scrollWidth-innerWidth));
    await p.close();
  }
  console.log('ERRORES', errs); await b.close();
})();
