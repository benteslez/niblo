const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage(); const errs=[]; p.on('pageerror', e => errs.push(e.message));
  await p.goto('http://localhost:8765/oposicion.html'); await p.waitForTimeout(1500);
  const r = await p.evaluate(() => {
    const h = formatear("Dato [[TC|https://www.tribunalconstitucional.es/es/tribunal/Composicion-Organizacion/]] y ley BOE-A-1979-23709.\n\n> [[DOUE]]\n> Artículo 15 TUE\n\n> 1. Texto del BOE.");
    const d = document.createElement('div'); d.innerHTML = h;
    return { pills:[...d.querySelectorAll('.tag-boe')].map(x => x.textContent), links:[...d.querySelectorAll('a')].map(a => a.href.slice(0,60)), plano:textoPlano("Dato [[TC|https://x.es/a]] y [[SEGSOCIAL]].") };
  });
  console.log(JSON.stringify(r), errs); await b.close();
})();
