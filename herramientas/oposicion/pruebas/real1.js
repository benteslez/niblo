const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs=[], cons=[];
  const p = await b.newPage({ viewport:{width:1280,height:900} });
  p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type()==='error') cons.push(m.text()); });
  await p.goto('http://localhost:8765/_prueba_real.html#/real'); await p.waitForTimeout(1500);
  const txt = async () => (await p.locator('#real-cuerpo').innerText()).replace(/\s+/g,' ');
  console.log('cfg:', (await txt()).slice(0,400));
  await p.screenshot({ path:'r-cfg.png' });
  // Práctica: 3 preguntas en orden del examen
  await p.selectOption('#rn', '10'); await p.click('#r-go'); await p.waitForTimeout(300);
  await p.locator('.q-opt').nth(1).click(); await p.waitForTimeout(150);    // n1: correcta c=1 → bien
  console.log('p1:', await p.locator('.q-fb').innerText());
  await p.click('#r-sig'); await p.locator('.q-opt').nth(0).click(); await p.waitForTimeout(150);  // n2: c=2 → mal
  console.log('p2:', await p.locator('.q-fb').innerText(), '| marcas:', await p.evaluate(()=>[...document.querySelectorAll('.q-opt')].map(b=>b.className.replace('q-opt','').trim()).join(',')));
  await p.screenshot({ path:'r-prac.png' });
  await p.click('#r-sig'); await p.click('#r-salir'); await p.waitForTimeout(200);
  console.log('resultado práctica:', (await txt()).slice(0,200));
  await p.click('#r-fin'); await p.waitForTimeout(200);
  console.log('tras práctica:', (await txt()).match(/Solo las que fallé \d+/)?.[0]);
  // Falladas
  await p.click('[data-fl="falladas"]'); await p.waitForTimeout(150);
  console.log('falladas disponibles:', (await txt()).match(/\d+ preguntas? disponibles?/)?.[0]);
  await p.click('[data-fl="todas"]');
  // Filtro por bloque
  await p.click('[data-bq="B1"]'); await p.waitForTimeout(150);
  console.log('bloque I:', (await txt()).match(/\d+ preguntas? disponibles?/)?.[0]);
  await p.click('[data-bq="todos"]');
  // Simulacro
  await p.click('[data-md="simulacro"]'); await p.waitForTimeout(150);
  console.log('simulacro disp:', (await txt()).match(/\d+ preguntas? disponibles?/)?.[0]);
  await p.selectOption('#rn', '0'); await p.click('#r-go'); await p.waitForTimeout(300);
  console.log('reloj:', await p.locator('#sim-reloj').innerText());
  // n1 c=1 bien, n2 c=2 bien, n3 c=3 mal(0), n4 blanco, n5 c=1 → marcar y desmarcar (blanco)
  const marca = async (k, i) => { await p.locator('.sim-mapa [data-k]').nth(k).click(); await p.locator('.q-opt').nth(i).click(); };
  await marca(0,1); await marca(1,2); await marca(2,0); await marca(4,1); await p.locator('.q-opt').nth(1).click();
  await p.screenshot({ path:'r-sim.png' });
  p.once('dialog', d => d.accept());
  await p.click('#sim-entregar'); await p.waitForTimeout(300);
  console.log('resultado simulacro:', (await txt()).slice(0,260));
  await p.screenshot({ path:'r-res.png', fullPage:true });
  console.log('ERRORES', errs, 'CONSOLA', cons); await b.close();
})();
