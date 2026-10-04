const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs=[];
  const ctx = await b.newContext({ viewport:{width:1280,height:900} }); const p = await ctx.newPage();
  p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type()==='error') errs.push('consola: '+m.text()); });
  await p.goto('http://localhost:8765/oposicion.html#/real'); await p.waitForTimeout(1500);
  console.log('portada:', (await p.locator('#real-cuerpo').innerText()).replace(/\s+/g,' ').slice(0,700));
  await p.screenshot({ path:'k-portada.png' });
  // Datos cargados = plantilla
  console.log('datos:', JSON.stringify(await p.evaluate(() => { const x = TESTS_REALES.examenes[0]; return { n:x.preguntas.length, anul:x.preguntas.filter(q=>q.anulada).map(q=>q.n), res:x.preguntas.filter(q=>q.reserva).map(q=>q.nr), c1:'abcd'[x.preguntas[0].c], c82:x.preguntas[81].c, c101:'abcd'[x.preguntas[100].c] }; })));
  // SRS para test
  console.log('SRS:', await p.evaluate(() => { let s=null, o=[]; for (const q of [5,5,5,5]) { s=srsSiguiente(s,q); o.push(q+'→'+s.i); } s=srsSiguiente(s,0); o.push('0→'+s.i); s=srsSiguiente(s,5); o.push('5 tras fallo→'+s.i); s=srsSiguiente(s,3); o.push('3→'+s.i); let t=null; t=srsSiguiente(t,3); o.push('nueva dudada→'+t.i); return o.join(' | '); }));
  // Ventana: por defecto 2025 + turno libre
  await p.click('[data-modo="repaso"]'); await p.waitForTimeout(300);
  console.log('ventana:', JSON.stringify(await p.evaluate(() => { const d=document.querySelector('dialog'); return { anios:[...d.querySelectorAll('[data-anio]')].filter(i=>i.checked).map(i=>i.dataset.anio), acc:[...d.querySelectorAll('[data-acc].active')].map(b=>b.dataset.acc), pills:d.querySelector('.real-pills').innerText.replace(/\s+/g,' ') }; })));
  await p.selectOption('dialog [data-op="max"]', '20'); await p.waitForTimeout(150);
  await p.click('dialog [data-empezar]'); await p.waitForTimeout(400);
  console.log('pantalla completa:', await p.evaluate(() => ({ capa:!!document.querySelector('.real-full'), cubre:(()=>{const r=document.querySelector('.real-full').getBoundingClientRect(); return r.top===0&&r.height===innerHeight;})(), cabeceraTapada: getComputedStyle(document.querySelector('.real-full')).zIndex })));
  await p.screenshot({ path:'k-repaso.png' });
  // Barajado: la correcta no siempre en la misma letra
  const pos = await p.evaluate(() => real.ses.cola.map(it => it.ord.indexOf(it.q.c)));
  console.log('posición mostrada de la correcta en las 20:', pos.join(''));
  // Fallar la 1.ª → vuelve en la sesión 4 después
  const cur = async () => p.evaluate(() => { const it = real.ses.cola[real.ses.i]; return { n:it.q.n, jc:it.ord.indexOf(it.q.c), len:real.ses.cola.length, i:real.ses.i }; });
  let q = await cur(); const n1 = q.n;
  await p.locator('.q-opt').nth((q.jc+1)%4).click(); await p.waitForTimeout(100);
  console.log('fallo:', (await p.locator('#fb').innerText()).replace(/\s+/g,' '));
  await p.click('[data-cal="0"]'); await p.waitForTimeout(100);
  console.log('tras fallar: cola', (await cur()).len, '· vuelve en la posición', await p.evaluate(n => real.ses.cola.findIndex((it,k) => k>0 && it.q.n===n), n1));
  // 3 aciertos seguros
  for (let k=0;k<3;k++) { q = await cur(); await p.keyboard.press('abcd'[q.jc]); await p.waitForTimeout(80); await p.keyboard.press('3'); await p.waitForTimeout(80); }
  q = await cur(); console.log('reaparece la fallada:', q.n === n1, '· chips:', (await p.locator('.q-meta .tags').innerText()).replace(/\s+/g,' '));
  await p.keyboard.press('abcd'[(q.jc+1)%4]); await p.waitForTimeout(80);
  console.log('mismo error:', (await p.locator('.srs-cf').innerText().catch(()=>'-')));
  await p.screenshot({ path:'k-cf.png' });
  await p.keyboard.press('1'); await p.waitForTimeout(80);
  // deshacer quita la reinserción
  const antes = (await cur()).len; await p.click('#srs-deshacer'); await p.waitForTimeout(80); console.log('deshacer: cola', antes, '→', (await cur()).len);
  await p.click('#srs-salir'); await p.waitForTimeout(200);
  console.log('resumen:', (await p.locator('#real-cuerpo').innerText()).replace(/\s+/g,' ').slice(0,260));
  await p.screenshot({ path:'k-resumen.png', fullPage:true });
  await p.click('#r-fin'); await p.waitForTimeout(200);
  console.log('capa cerrada:', await p.evaluate(() => !document.querySelector('.real-full') && !document.body.classList.contains('real-abierto')));
  // Rebelde: simular 3 fallos
  console.log('rebelde:', await p.evaluate(() => { const x=TESTS_REALES.examenes[0], q=x.preguntas[5]; calificar(x,q,0,1); calificar(x,q,0,1); calificar(x,q,0,2); const r1=rebelde(x,q); const enCola = colaRepaso(Object.assign(cfgReal(),{filtro:"todas"})).some(it=>it.q===q); calificar(x,q,5); calificar(x,q,5); return { rebelde:r1, siempreEnCola:enCola, trasDosSeguras:rebelde(x,q) }; }));
  // Examen oficial completo 2025 libre
  await p.click('[data-modo="examen"]'); await p.waitForTimeout(250);
  console.log('examen:', (await p.locator('dialog .real-pills').innerText()).replace(/\s+/g,' '));
  await p.click('dialog [data-empezar]'); await p.waitForTimeout(400);
  console.log('reloj:', await p.locator('#sim-reloj').innerText(), '· preguntas', await p.evaluate(() => real.ex.qs.length), '· orden', await p.evaluate(() => real.ex.qs.slice(0,5).map(it=>it.q.n).join(',')));
  // 70 bien, 20 mal, resto en blanco
  await p.evaluate(() => { const E = real.ex; E.qs.forEach((it,k) => { E.resp[k] = k < 70 ? it.q.c : k < 90 ? (it.q.c+1)%4 : null; }); pintarExamen(document.getElementById('real-cuerpo')); });
  await p.screenshot({ path:'k-examen.png' });
  p.once('dialog', d => d.accept()); await p.click('#sim-entregar'); await p.waitForTimeout(300);
  console.log('resultado:', (await p.locator('.resultado').innerText()).replace(/\s+/g,' '));
  console.log('ERRORES', errs); await b.close();
})();
