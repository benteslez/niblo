const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs=[];
  const ctx = await b.newContext({ viewport:{width:1280,height:900} }); const p = await ctx.newPage();
  p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type()==='error') errs.push('consola: '+m.text()); });
  await p.goto('http://localhost:8765/_prueba_real.html#/real'); await p.waitForTimeout(1500);
  await p.screenshot({ path:'s-inicio.png' });
  // 1 · SM-2 idéntico al de vocabulario
  const sm = await p.evaluate(() => {
    let s = null; const out = [];
    for (const q of [5,5,5,0,3,5,0,0,0]) { s = srsSiguiente(s, q); out.push(q+'→'+s.i+'d e'+s.e.toFixed(2)+' r'+s.r); }
    return out.join(' | ');
  });
  console.log('SM-2:', sm);
  // 2 · ventana de selección: por defecto turno libre y el último año
  await p.click('[data-modo="repaso"]'); await p.waitForTimeout(300);
  const sel = async () => p.evaluate(() => { const d = document.querySelector('dialog.real-dlg'); return { anios:[...d.querySelectorAll('[data-anio]')].filter(i=>i.checked).map(i=>i.dataset.anio), acc:[...d.querySelectorAll('[data-acc].active')].map(b=>b.dataset.acc), pills:d.querySelector('.real-pills').innerText.replace(/\s+/g,' ') }; });
  console.log('por defecto:', JSON.stringify(await sel()));
  await p.screenshot({ path:'s-dlg.png' });
  await p.click('dialog [data-anio="2024"]'); await p.click('dialog [data-anio="2025"]'); await p.waitForTimeout(150);
  console.log('cambio a 2024:', JSON.stringify(await sel()));
  await p.click('dialog button[value="cancel"]'); await p.waitForTimeout(150);
  await p.reload(); await p.waitForTimeout(1200);
  await p.click('[data-modo="repaso"]'); await p.waitForTimeout(300);
  console.log('tras recargar (recuerda):', JSON.stringify(await sel()));
  // vuelvo a 2025 libre y empiezo
  await p.click('dialog [data-ultimo-anio]'); await p.waitForTimeout(150);
  await p.click('dialog [data-empezar]'); await p.waitForTimeout(300);
  const clave = async () => p.evaluate(() => { const S = real.ses, it = S.cola[S.i]; return it ? { n:it.q.n, c:it.q.c } : null; });
  // P1: acierto seguro (tecla de la letra correcta + 3)
  let q = await clave(); await p.keyboard.press('abcd'[q.c]); await p.waitForTimeout(100);
  console.log('intervalos ofrecidos:', await p.locator('.srs-rate').innerText().then(t=>t.replace(/\s+/g,' ')));
  await p.screenshot({ path:'s-ok.png' });
  await p.keyboard.press('3'); await p.waitForTimeout(100);
  // P2: fallo
  q = await clave(); await p.locator('.q-opt').nth((q.c+1)%4).click(); await p.waitForTimeout(100);
  console.log('fallo ofrece:', await p.locator('.srs-rate').innerText().then(t=>t.replace(/\s+/g,' ')));
  await p.screenshot({ path:'s-ko.png' });
  await p.click('[data-cal="0"]'); await p.waitForTimeout(100);
  // P3: duda → y deshacer
  q = await clave(); await p.locator('.q-opt').nth(q.c).click(); await p.click('[data-cal="3"]'); await p.waitForTimeout(100);
  await p.click('#srs-deshacer'); await p.waitForTimeout(100);
  const tras = await p.evaluate(() => ({ i:real.ses.i, n:real.ses.cola[real.ses.i].q.n, srs:!!srsDe(real.ses.cola[real.ses.i].x, real.ses.cola[real.ses.i].q) }));
  console.log('deshacer vuelve a la 3 y sin SRS:', JSON.stringify(tras));
  // ★ y 💤
  await p.click('#srs-star'); const nPausa = await p.evaluate(() => real.ses.cola.length); await p.click('#srs-pausa'); await p.waitForTimeout(100);
  console.log('pausa quita de la cola:', nPausa, '→', await p.evaluate(() => real.ses.cola.length));
  await p.click('#srs-salir'); await p.waitForTimeout(200);
  console.log('resumen:', (await p.locator('#real-cuerpo').innerText()).replace(/\s+/g,' ').slice(0,200));
  await p.click('#r-fin'); await p.waitForTimeout(200);
  console.log('estado guardado:', JSON.stringify(await p.evaluate(() => { const x = TESTS_REALES.examenes[0]; return x.preguntas.slice(0,4).map(q => ({ n:q.n, d:(progreso(claveReal(x,q))||{}).d })); })));
  console.log('portada:', (await p.locator('#real-cuerpo').innerText()).replace(/\s+/g,' ').slice(0,420));
  await p.screenshot({ path:'s-portada.png' });
  // Hoy la fallada no toca (mañana); "Solo falladas" sí la trae
  await p.click('[data-modo="repaso"]'); await p.waitForTimeout(200);
  await p.click('dialog [data-fl="falladas"]'); await p.waitForTimeout(150);
  console.log('solo falladas:', JSON.stringify(await sel()));
  await p.click('dialog button[value="cancel"]');
  // Simulamos que pasa un día: la fallada vuelve
  await p.evaluate(() => { const x = TESTS_REALES.examenes[0]; x.preguntas.forEach(q => { const v = progreso(claveReal(x,q)); if (v && v.d && v.d.nx) { v.d.nx = hoyISO(); } }); });
  await p.click('[data-modo="repaso"]'); await p.waitForTimeout(200);
  await p.click('dialog [data-fl="todas"]'); await p.waitForTimeout(150);
  console.log('al día siguiente:', JSON.stringify(await sel()));
  await p.click('dialog button[value="cancel"]');
  // 3 · Examen oficial libre 2025 (12 preguntas → 12/100 de 90 min)
  await p.click('[data-modo="examen"]'); await p.waitForTimeout(200);
  console.log('examen libre:', await p.locator('dialog .real-cond').innerText(), '|', await p.locator('dialog .real-pills').innerText().then(t=>t.replace(/\s+/g,' ')));
  await p.screenshot({ path:'s-dlg-ex.png' });
  await p.click('dialog [data-empezar]'); await p.waitForTimeout(300);
  console.log('reloj:', await p.locator('#sim-reloj').innerText());
  // 6 bien, 3 mal, 3 blanco
  const plan = await p.evaluate(() => real.ex.qs.map(it => it.q.c));
  for (let k = 0; k < 9; k++) { await p.locator('.sim-mapa [data-k]').nth(k).click(); await p.locator('.q-opt').nth(k < 6 ? plan[k] : (plan[k]+1)%4).click(); }
  p.once('dialog', d => d.accept()); await p.click('#sim-entregar'); await p.waitForTimeout(300);
  console.log('resultado libre:', (await p.locator('.resultado').innerText()).replace(/\s+/g,' '));
  await p.screenshot({ path:'s-res.png' });
  await p.click('#r-fin');
  // 4 · Promoción interna: −1/4
  await p.click('[data-modo="examen"]'); await p.waitForTimeout(200);
  await p.click('dialog [data-acc="libre"]'); await p.click('dialog [data-acc="promocion"]'); await p.waitForTimeout(150);
  console.log('examen PI:', await p.locator('dialog .real-cond').innerText());
  await p.click('dialog [data-acc="libre"]'); await p.waitForTimeout(150);
  console.log('dos accesos:', await p.locator('dialog .real-cond').innerText(), '| botón:', await p.locator('dialog [data-empezar]').isDisabled());
  console.log('ERRORES', errs); await b.close();
})();
