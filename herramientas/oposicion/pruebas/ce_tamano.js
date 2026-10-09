// Deslizador de tamaño del texto en la Constitución y botones A−/A+ en Memorizar. Requiere `python3 -m http.server 8765` en la raíz.
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs = []; let fallos = 0;
  const ok = (c, m) => { console.log(c ? 'OK ' : 'FALLA', m); if (!c) fallos++; };
  for (const [nombre, vp] of [['esc', { width:1280, height:900 }], ['mov', { width:390, height:800 }]]) {
    const ctx = await b.newContext({ viewport:vp }); const p = await ctx.newPage();
    p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type()==='error') errs.push(m.text()); });
    await p.goto('http://localhost:8765/oposicion.html#/ce/texto/66'); await p.waitForTimeout(2800);
    const fs = () => p.locator('.ce-txt p').first().evaluate(e => parseFloat(getComputedStyle(e).fontSize));
    const base = await fs();
    ok(base === 15 && await p.locator('#ce-fs').count() === 1, nombre + ': deslizador presente, tamaño base ' + base + ' px');
    await p.locator('#ce-fs').fill('150'); await p.waitForTimeout(150);
    ok(Math.abs(await fs() - 22.5) < 0.1 && /150/.test(await p.locator('#ce-fs-v').innerText()), nombre + ': al 150 % el texto mide ' + await fs() + ' px');
    await p.locator('#ce-fs').fill('80'); await p.waitForTimeout(150);
    ok(Math.abs(await fs() - 12) < 0.1, nombre + ': al 80 % mide ' + await fs() + ' px');
    await p.locator('#ce-fs').fill('150'); await p.reload(); await p.waitForTimeout(2800);
    ok(Math.abs(await fs() - 22.5) < 0.1 && await p.locator('#ce-fs').inputValue() === '150', nombre + ': se recuerda al recargar');
    ok(!(await p.evaluate(() => document.documentElement.scrollWidth > innerWidth + 2)), nombre + ': sin desbordamiento horizontal con el texto grande');
    // Memorizar: A− y A+ en la tarjeta
    await p.evaluate(() => { CEM.cfg.pc = false; CEM.ses = null; CEM.sub = 'practicar'; CEM.cfg.dif = '1'; CEM.ses = { cola:[{ n:66, l:'x', rein:0 }], i:0, bien:0, mal:0, rev:false, tot:1 }; }); await p.goto('http://localhost:8765/oposicion.html#/ce/memorizar'); await p.waitForTimeout(2500);
    await p.evaluate(() => { CEM.sub = 'practicar'; CEM.cfg.dif = '1'; CEM.ses = { cola:[{ n:66, l:'x', rein:0 }], i:0, bien:0, mal:0, rev:false, tot:1 }; ceVerMem(document.getElementById('ce-cuerpo')); }); await p.waitForTimeout(300);
    const t0 = await p.locator('.cem-txt').evaluate(e => parseFloat(getComputedStyle(e).fontSize));
    await p.locator('[data-ce-fs="10"]').click(); await p.waitForTimeout(100);
    const t1 = await p.locator('.cem-txt').evaluate(e => parseFloat(getComputedStyle(e).fontSize));
    ok(t1 > t0 && await p.evaluate(() => ceFs()) === 160, nombre + ': A+ agranda el texto de Memorizar (' + t0 + ' → ' + t1 + ' px)');
    await p.locator('[data-ce-fs="-10"]').click(); await p.locator('[data-ce-fs="-10"]').click(); await p.waitForTimeout(100);
    ok(await p.evaluate(() => ceFs()) === 140, nombre + ': A− lo reduce');
    await ctx.close();
  }
  console.log('errores de consola:', errs.length ? errs.join(' | ') : 'ninguno'); await b.close(); process.exit(fallos || errs.length ? 1 : 0);
})();
