const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs=[];
  for (const [nom, vp, oscuro] of [['m', {width:390,height:844}, false], ['d', {width:1280,height:900}, false], ['o', {width:1280,height:900}, true]]) {
    const ctx = await b.newContext({ viewport:vp, colorScheme: oscuro ? 'dark' : 'light' });
    const p = await ctx.newPage(); p.on('pageerror', e => errs.push(e.message));
    await p.goto('http://localhost:8765/oposicion.html#/tema/B1T02/leer'); await p.waitForTimeout(2500);
    await p.click('[data-todo="1"]'); await p.waitForTimeout(500);
    const info = await p.evaluate(() => ({ aps:document.querySelectorAll('.ap[data-ap]').length, fichas:document.querySelectorAll('.ap-caja.ap-ficha').length, filas:document.querySelectorAll('.fi-fila').length, ojo:document.querySelectorAll('.fi-fila.ojo').length, guias:document.querySelectorAll('.ap-caja.ap-guia').length, lit:document.querySelectorAll('blockquote.literal').length, filasSinClave:[...document.querySelectorAll('.fi-k')].filter(x=>!x.textContent.trim()).length, ov:document.documentElement.scrollWidth-innerWidth, indice:[...document.querySelectorAll('[data-ancla]')].slice(0,6).map(x=>x.textContent+'|'+x.className) }));
    console.log(nom, JSON.stringify(info));
    const shots = nom==='o' ? [[1,'.ap-caja.ap-ficha >> nth=6']] : [[1,'.ap-caja.ap-guia >> nth=0'],[2,'.ap-caja.ap-ficha >> nth=6'],[3,'.ap-caja.ap-ficha >> nth=40']];
    for (const [i,sel] of shots) {
      await p.locator(sel).scrollIntoViewIfNeeded(); await p.waitForTimeout(250);
      await p.evaluate(s => { const el=document.querySelector('.ap-caja.ap-ficha'); }, sel);
      await p.screenshot({ path:`f-${nom}-${i}.png` });
    }
    await ctx.close();
  }
  console.log('ERRORES', errs); await b.close();
})();
