const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport:{width:1100,height:900} });
  const errs=[]; p.on('pageerror', e => errs.push(e.message));
  await p.goto('http://localhost:8765/index.html'); await p.waitForTimeout(2500);
  console.log(await p.$$eval('#hub-grid .hub-card', a => a.map(x => x.dataset.area + (x.getAttribute('target')?'(_blank)':'') + ' ' + (x.getAttribute('href')||''))));
  await p.screenshot({ path: __dirname + '/9-niblo.png' });
  const c = p.locator('.hub-card[data-area="oposicion"]');
  if (await c.count()) { await c.click(); await p.waitForTimeout(800); console.log('url', p.url()); }
  console.log('errs', errs); await b.close();
})();
