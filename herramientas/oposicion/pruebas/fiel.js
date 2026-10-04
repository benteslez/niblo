const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs=[]; const fallos=[];
  for (const [nom, vp, touch] of [['escritorio',{width:1280,height:900},false],['movil',{width:390,height:844},true]]) {
    const ctx = await b.newContext({ viewport:vp, hasTouch:touch, isMobile:touch }); const p = await ctx.newPage(); p.on('pageerror', e => errs.push(e.message));
    await p.goto('http://localhost:8765/oposicion.html#/real'); await p.waitForTimeout(1300);
    // Respuesta correcta según el JSON publicado, por texto
    const correctas = await p.evaluate(() => Object.fromEntries(TESTS_REALES.examenes[0].preguntas.filter(q=>!q.anulada).map(q => [q.n, q.o[q.c]])));
    await p.click('[data-modo="repaso"]'); await p.waitForTimeout(250); await p.click('dialog [data-empezar]'); await p.waitForTimeout(300);
    let vistas = 0, k = 0;
    while (await p.locator('.q-opt').count() && k < 400) {
      k++;
      const n = await p.evaluate(() => real.ses.cola[real.ses.i].q.n);
      const textos = await p.locator('.q-opt span:last-child').allInnerTexts();
      const jBuena = textos.findIndex(t => t.trim() === correctas[n].trim());
      if (jBuena < 0) { fallos.push(`${nom} n${n}: la correcta no está entre las opciones`); break; }
      const acierto = vistas % 2 === 0;            // alterno: acertar / fallar
      const j = acierto ? jBuena : (jBuena + 1 + (vistas % 3)) % textos.length;
      const via = vistas % 4 === 1 && !touch ? 'teclado' : 'clic';
      if (via === 'teclado') await p.keyboard.press('abcd'[j]); else if (touch) await p.locator('.q-opt').nth(j).tap(); else await p.locator('.q-opt').nth(j).click();
      await p.waitForTimeout(30);
      const r = await p.evaluate(() => ({ fb:document.querySelector('.q-fb').innerText, verdes:[...document.querySelectorAll('.q-opt.bien')].map(x=>x.querySelector('span:nth-child(2)').innerText.trim()), rojas:[...document.querySelectorAll('.q-opt.mal')].map(x=>x.querySelector('span:nth-child(2)').innerText.trim()) }));
      const okEsperado = j === jBuena;
      if (r.verdes.length !== 1 || r.verdes[0] !== correctas[n].trim()) fallos.push(`${nom} n${n}: verde «${r.verdes}» ≠ correcta «${correctas[n]}»`);
      if (okEsperado !== r.fb.startsWith('✓')) fallos.push(`${nom} n${n}: dice ${r.fb.slice(0,20)} y debía ser ${okEsperado ? 'correcta' : 'incorrecta'}`);
      if (!okEsperado && (r.rojas.length !== 1 || r.rojas[0] !== textos[j].trim())) fallos.push(`${nom} n${n}: roja «${r.rojas}» ≠ marcada «${textos[j]}»`);
      const letra = r.fb.match(/la correcta es la ([a-d])\)/);
      if (letra && 'abcd'.indexOf(letra[1]) !== jBuena) fallos.push(`${nom} n${n}: el texto dice ${letra[1]}) y la correcta mostrada es ${'abcd'[jBuena]})`);
      const orig = r.fb.match(/en el examen original, la ([a-d])/);
      const cOrig = await p.evaluate(nn => 'abcd'[TESTS_REALES.examenes[0].preguntas.find(q=>q.n===nn).c], n);
      if (!orig || orig[1] !== cOrig) fallos.push(`${nom} n${n}: letra original ${orig && orig[1]} ≠ ${cOrig}`);
      await p.click(okEsperado ? '[data-cal="5"]' : '[data-cal="0"]'); await p.waitForTimeout(20);
      vistas++;
    }
    console.log(nom, 'preguntas comprobadas en repaso:', vistas);
    await p.click('#r-fin').catch(()=>{}); await p.waitForTimeout(200);
    // Examen oficial: responder por TEXTO y comprobar la nota
    await p.click('[data-modo="examen"]'); await p.waitForTimeout(250); await p.click('dialog [data-empezar]'); await p.waitForTimeout(300);
    let bien = 0, mal = 0;
    const N = await p.evaluate(() => real.ex.qs.length);
    for (let i = 0; i < N; i++) {
      const n = await p.evaluate(() => real.ex.qs[real.ex.i].q.n);
      const textos = await p.locator('.q-opt span:last-child').allInnerTexts();
      const jb = textos.findIndex(t => t.trim() === correctas[n].trim());
      const j = i % 3 === 2 ? (jb + 1) % 4 : jb; if (j === jb) bien++; else mal++;
      if (touch) await p.locator('.q-opt').nth(j).tap(); else await p.locator('.q-opt').nth(j).click();
      await p.waitForTimeout(15);
      if (i + 1 < N) { await p.click('#sim-sig'); await p.waitForTimeout(15); }
    }
    p.once('dialog', d => d.accept()); await p.click('#sim-entregar'); await p.waitForTimeout(300);
    const res = (await p.locator('.resultado').innerText()).replace(/\s+/g,' ');
    const esperado = (bien - mal/3).toFixed(2).replace('.', ',');
    console.log(nom, `examen: marcadas ${bien} bien y ${mal} mal → esperado ${esperado} · app: ${res.match(/Puntuación directa ([\d,]+)/)[1]} · ${res.match(/\d+ aciertos?, \d+ errores?/)[0]}`);
    if (!res.includes(esperado)) fallos.push(`${nom}: nota del examen distinta`);
    await ctx.close();
  }
  console.log('FALLOS:', fallos.length ? fallos : 'ninguno'); console.log('ERRORES', errs); await b.close();
})();
