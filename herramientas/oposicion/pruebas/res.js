const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs=[];
  const p = await b.newPage({ viewport:{width:1280,height:900} }); p.on('pageerror', e => errs.push(e.message));
  await p.goto('http://localhost:8765/oposicion.html#/tema/B1T02/leer'); await p.waitForTimeout(2500);
  await p.click('[data-todo="1"]'); await p.waitForTimeout(500);
  async function sel(frase) {
    return p.evaluate(frase => {
      const caja = [...document.querySelectorAll('.ap-guia')].find(x => x.textContent.includes(frase));
      const w = document.createTreeWalker(caja, NodeFilter.SHOW_TEXT);
      while (w.nextNode()) { const i = w.currentNode.nodeValue.indexOf(frase); if (i >= 0) {
        const r = document.createRange(); r.setStart(w.currentNode, i); r.setEnd(w.currentNode, i + frase.length);
        const s = getSelection(); s.removeAllRanges(); s.addRange(r); document.dispatchEvent(new Event('selectionchange')); 
        caja.scrollIntoView({block:'center'}); return true; } }
      return false;
    }, frase);
  }
  for (const [f, c] of [['Primera pregunta del tema', 'verde'], ['es de hablar de gara', 'azul'], ['reconoce la Constitución', 'amarillo'], ['lugar decide', 'morado']]) {
    await sel(f); await p.waitForTimeout(300);
    await p.click(`#barra-resaltar .res-col[data-col="${c}"]`); await p.waitForTimeout(300);
  }
  console.log(await p.evaluate(() => [...document.querySelectorAll('mark.res')].map(m => [m.textContent, m.dataset.col, getComputedStyle(m).borderBottomColor])));
  await p.locator('mark.res').first().scrollIntoViewIfNeeded(); await p.screenshot({ path:'res.png', clip:{x:0,y:200,width:1280,height:400} });
  console.log('ERRORES', errs); await b.close();
})();
