const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
const OUT = process.env.SHOTS || '.';
(async () => {
  const b = await chromium.launch(); const errs = [];
  for (const [nombre, vp] of [['esc', { width:1280, height:900 }], ['mov', { width:390, height:800 }]]) {
    const ctx = await b.newContext({ viewport:vp, hasTouch: nombre==='mov' }); const p = await ctx.newPage();
    p.on('pageerror', e => errs.push(nombre + ' pageerror: ' + e.message)); p.on('console', m => { if (m.type()==='error') errs.push(nombre + ' consola: ' + m.text()); });
    await p.goto('http://localhost:8765/oposicion.html'); await p.waitForTimeout(1500);
    // inicio: botones y cronómetro visible abajo-izquierda
    console.log(nombre, 'botones inicio:', await p.locator('.dash-card.plan, .dash-card.registro').count(), 'crono:', JSON.stringify(await p.locator('#cr .cr-pill').boundingBox()));
    await p.screenshot({ path:`${OUT}/${nombre}-inicio.png` });
    // plan
    await p.click('.dash-card.plan'); await p.waitForTimeout(500);
    console.log(nombre, 'filas plantilla:', await p.locator('.pl-fila:not(.pl-bh):not(.pl-nv):not(.pl-tot)').count(), 'negras:', await p.locator('.pl-c.neg').count(), 'partidas:', await p.locator('.pl-c.par').count());
    console.log(nombre, 'desborde horizontal página:', await p.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1));
    await p.screenshot({ path:`${OUT}/${nombre}-plantilla.png`, fullPage:true });
    // abrir un tema desde plantilla, cronómetro cuenta ese tema
    await p.click('.pl-fila:has-text("La Corona") .pl-t a'); await p.waitForTimeout(400);
    console.log(nombre, 'destino crono:', await p.locator('#cr-d').innerText());
    await p.click('#cr-go'); await p.waitForTimeout(2300);
    await p.goto('http://localhost:8765/oposicion.html#/tema/B4T04'); await p.waitForTimeout(500);
    console.log(nombre, 'tras cambiar de tema:', await p.locator('#cr-d').innerText(), await p.locator('#cr-t').innerText());
    await p.click('#cr-go'); await p.waitForTimeout(300);
    await p.goto('http://localhost:8765/oposicion.html#/plan'); await p.waitForTimeout(500);
    console.log(nombre, 'casillas con tiempo:', await p.locator('.pl-c.hecho').count(), (await p.locator('.pl-c.hecho').allInnerTexts()).join('|'));
    // pestañas
    for (const t of ['orden', 'encaje', 'supuestos', 'guia']) { await p.goto('http://localhost:8765/oposicion.html#/plan/' + t); await p.waitForTimeout(400);
      console.log(nombre, t, 'desborde:', await p.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1), 'pills:', await p.locator('.pill-critica').count());
      await p.screenshot({ path:`${OUT}/${nombre}-${t}.png`, fullPage:true }); }
    // supuestos persistencia
    await p.goto('http://localhost:8765/oposicion.html#/plan/supuestos'); await p.waitForTimeout(300);
    await p.fill('input[data-sup="TL2018|1|I"]', '7,5'); await p.locator('input[data-sup="TL2018|1|I"]').blur();
    await p.fill('textarea[data-supa="TL2018|I"]', 'LCSP 118'); await p.locator('textarea[data-supa="TL2018|I"]').blur();
    await p.reload(); await p.waitForTimeout(800);
    console.log(nombre, 'persistencia supuesto:', await p.inputValue('input[data-sup="TL2018|1|I"]'), await p.inputValue('textarea[data-supa="TL2018|I"]'));
    // registro
    await p.goto('http://localhost:8765/oposicion.html#/registro'); await p.waitForTimeout(500);
    console.log(nombre, 'registro hoy:', (await p.locator('.rg-det').innerText()).replace(/\s+/g, ' ').slice(0, 200), 'desborde:', await p.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1));
    await p.screenshot({ path:`${OUT}/${nombre}-registro.png`, fullPage:true });
    await p.click('#rg-add'); await p.waitForTimeout(200); await p.selectOption('#an-f', 'B4T04'); await p.click('#an-ok'); await p.waitForTimeout(300);
    console.log(nombre, 'tras añadir 1 h:', (await p.locator('.rg-kpis').innerText()).replace(/\s+/g, ' ').slice(0, 160));
    // dark
    await p.emulateMedia({ colorScheme:'dark' }); await p.goto('http://localhost:8765/oposicion.html#/plan'); await p.waitForTimeout(400);
    await p.screenshot({ path:`${OUT}/${nombre}-plantilla-oscuro.png` });
    await ctx.close();
  }
  console.log('ERRORES', errs); await b.close();
})();
