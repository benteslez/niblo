const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs=[];
  for (const [nom, vp] of [['d',{width:2000,height:1120}],['l',{width:1280,height:800}],['m',{width:390,height:844}]]) {
    const p = await b.newPage({ viewport:vp }); p.on('pageerror', e => errs.push(e.message));
    await p.goto('http://localhost:8765/oposicion.html#/real'); await p.waitForTimeout(1200);
    await p.click('[data-modo="repaso"]'); await p.waitForTimeout(250); await p.click('dialog [data-empezar]'); await p.waitForTimeout(400);
    const m = await p.evaluate(() => { const r = document.querySelector('.real-full-in').getBoundingClientRect(); return { arriba:Math.round(r.top), abajo:Math.round(innerHeight - r.bottom), izq:Math.round(r.left), der:Math.round(innerWidth - r.right) }; });
    console.log(nom, 'márgenes', JSON.stringify(m));
    await p.screenshot({ path:`c-${nom}.png` });
    // Examen (contenido alto): ¿se desplaza sin cortarse?
    await p.click('#srs-salir'); await p.waitForTimeout(150); await p.click('#r-fin'); await p.waitForTimeout(200);
    await p.click('[data-modo="examen"]'); await p.waitForTimeout(250); await p.click('dialog [data-empezar]'); await p.waitForTimeout(400);
    const e = await p.evaluate(() => { const f = document.querySelector('.real-full'), r = document.querySelector('.real-full-in').getBoundingClientRect(); return { alto:Math.round(r.height), pantalla:innerHeight, topeVisible:Math.round(r.top) >= 0, desplazable:f.scrollHeight > f.clientHeight }; });
    console.log(nom, 'examen', JSON.stringify(e));
    if (nom==='m') await p.screenshot({ path:'c-m-ex.png' });
    await p.close();
  }
  console.log('ERRORES', errs); await b.close();
})();
