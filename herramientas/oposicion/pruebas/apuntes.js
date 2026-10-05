const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
const OUT = process.env.SHOTS || '.';
(async () => {
  const b = await chromium.launch(); const errs = [];
  const ctx = await b.newContext({ viewport:{ width:1100, height:900 } });
  const p = await ctx.newPage();
  p.on('pageerror', e => errs.push('pageerror: ' + e.message)); p.on('console', m => { if (m.type()==='error') errs.push('consola: ' + m.text()); });
  for (const id of ['B1T01', 'B4T05']) {
    await p.goto('http://localhost:8765/oposicion.html#/tema/' + id + '/leer'); await p.waitForTimeout(3000);
    const html = await p.evaluate(i => { const h = apuntesHTML(i); return h.replace(/<script>addEventListener[\s\S]*?<\/script>/, ''); }, id);
    require('fs').writeFileSync(`${OUT}/apuntes-${id}.html`, html);
    console.log(id, 'longitud HTML', html.length, '| botones en la página:', await p.locator('[data-apuntes]').count());
    const d = await ctx.newPage(); await d.setContent(html, { waitUntil:'load' });
    await d.pdf({ path:`${OUT}/apuntes-${id}.pdf`, format:'A4', printBackground:true, preferCSSPageSize:true });
    await d.close();
  }
  // el botón abre una ventana
  await p.goto('http://localhost:8765/oposicion.html#/tema/B1T01/leer'); await p.waitForTimeout(2500);
  const [nueva] = await Promise.all([ctx.waitForEvent('page'), p.click('[data-apuntes]')]);
  await nueva.waitForLoadState(); await nueva.waitForTimeout(500);
  console.log('ventana nueva:', await nueva.title());
  console.log('ERRORES', errs); await b.close();
})();
