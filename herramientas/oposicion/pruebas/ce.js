const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
const OUT = process.env.SHOTS || '.';
(async () => {
  const b = await chromium.launch(); const errs = [];
  for (const [nombre, vp] of [['esc', { width:1280, height:900 }], ['mov', { width:390, height:800 }]]) {
    const p = await (await b.newContext({ viewport:vp })).newPage();
    p.on('pageerror', e => errs.push(nombre + ' pageerror: ' + e.message)); p.on('console', m => { if (m.type()==='error') errs.push(nombre + ' consola: ' + m.text()); });
    await p.goto('http://localhost:8765/oposicion.html#/bloque/B1'); await p.waitForTimeout(1500);
    console.log(nombre, 'botones CE:', await p.locator('.ce-botones .dash-card').count());
    await p.click('[data-ir="#/ce/texto"]'); await p.waitForTimeout(1200);
    console.log(nombre, 'artículos:', await p.locator('.ce-art[data-n]').count(), 'bandas:', await p.locator('.ce-band').count(), 'desborde:', await p.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1));
    await p.screenshot({ path:`${OUT}/${nombre}-ce-texto.png` });
    await p.fill('#ce-ir', '17'); await p.waitForTimeout(900); await p.screenshot({ path:`${OUT}/${nombre}-ce-17.png` });
    await p.fill('#ce-q', 'estado de sitio'); await p.waitForTimeout(500);
    console.log(nombre, 'búsqueda:', await p.locator('#ce-cuenta').innerText());
    await p.goto('http://localhost:8765/oposicion.html#/ce/organigrama'); await p.waitForTimeout(1000);
    console.log(nombre, 'og desborde:', await p.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1));
    await p.screenshot({ path:`${OUT}/${nombre}-ce-org.png`, fullPage:true });
    await p.goto('http://localhost:8765/oposicion.html#/ce/test'); await p.waitForTimeout(1000);
    await p.screenshot({ path:`${OUT}/${nombre}-ce-test0.png` });
    await p.click('#ce-frente'); await p.waitForTimeout(800); await p.screenshot({ path:`${OUT}/${nombre}-ce-test1.png` });
    await p.click('#ce-ver'); await p.waitForTimeout(900); await p.screenshot({ path:`${OUT}/${nombre}-ce-test2.png` });
    await p.click('#ce-volver'); await p.waitForTimeout(700);
    await p.click('[data-q="5"]'); await p.waitForTimeout(300);
    console.log(nombre, 'tras calificar, en cola:', await p.locator('.srs-barra').innerText().then(t => t.replace(/\s+/g, ' ')));
    await p.keyboard.press(' '); await p.waitForTimeout(500); await p.keyboard.press('1'); await p.waitForTimeout(300);
    console.log(nombre, 'tras fallar con teclado:', await p.locator('.srs-barra').innerText().then(t => t.replace(/\s+/g, ' ')));
  }
  console.log('ERRORES', errs); await b.close();
})();
