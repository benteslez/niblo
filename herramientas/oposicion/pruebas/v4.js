const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs = [];
  const p = await b.newPage({ viewport:{width:390,height:844} }); p.on('pageerror', e => errs.push(e.message));
  await p.goto('http://localhost:8765/oposicion.html#/bloque/B6'); await p.waitForTimeout(1500);
  await p.screenshot({ path:'epi-bloque.png' });
  await p.goto('http://localhost:8765/oposicion.html#/tema/B6T05'); await p.waitForTimeout(800);
  await p.screenshot({ path:'epi-ficha.png' });
  await p.goto('http://localhost:8765/oposicion.html#/tema/B1T02/leer'); await p.waitForTimeout(800);
  await p.screenshot({ path:'epi-leer.png' });
  console.log('overflow', await p.evaluate(() => document.documentElement.scrollWidth - innerWidth), 'bq', await p.locator('blockquote.literal').count());
  await p.goto('http://localhost:8765/oposicion.html#/'); await p.waitForTimeout(500);
  console.log('ERRORES', errs); await b.close();
})();
