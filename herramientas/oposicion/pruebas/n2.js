const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage(); const e = [];
  p.on('pageerror', x => e.push(x.message)); await p.goto('http://localhost:8765/index.html'); await p.waitForTimeout(2500);
  console.log('Niblo errores:', e, '| adoptarTokensGuardados:', await p.evaluate(() => typeof adoptarTokensGuardados)); await b.close(); })();
