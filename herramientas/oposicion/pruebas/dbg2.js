const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage(); const log=[];
  p.on('console', m => log.push(m.type()+': '+m.text())); p.on('pageerror', e => log.push('ERR '+e.message));
  p.on('requestfinished', r => { if (r.url().includes('temas')) log.push('req '+r.url()); });
  await p.goto('http://localhost:8765/oposicion.html#/tema/B1T02/leer'); await p.waitForTimeout(4000);
  console.log(log.join('\n'));
  console.log(await p.evaluate(() => ({ temas:Object.keys(estado.temas), hash:location.hash, h1:(document.querySelector('h1,h2')||{}).textContent, todo:!!document.querySelector('[data-todo]') })));
  await b.close();
})();
