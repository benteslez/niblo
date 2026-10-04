// Uso: node tema.js B4T02  → comprueba un tema publicado en temas/ (escritorio y móvil)
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
const ID = process.argv[2];
(async () => {
  const b = await chromium.launch(); const errs = [];
  for (const [w,h] of [[1280,900],[390,844]]) {
    const p = await b.newPage({ viewport:{width:w,height:h} });
    p.on('pageerror', e => errs.push(e.message));
    await p.goto('http://localhost:8765/oposicion.html#/real'); await p.waitForTimeout(2500);
    const r = await p.evaluate(() => {
      const X = TESTS_REALES.examenes.find(x => x.id === 'GACE-X-2025-1'), P = TESTS_REALES.examenes.find(x => x.id === 'GACE-P-2025-1');
      const q96 = X.preguntas.find(q => q.n === 96), q31 = X.preguntas.find(q => q.n === 31);
      const cont = document.createElement('div'); cont.className = 'card'; cont.id = 'prueba-disc';
      cont.innerHTML = `<div class="q-meta"><span class="tags">${chipsReal({x:X, q:q96})}</span></div>` + leyHTML(q96, false) + leyHTML(q31, true);
      document.querySelector('main, #app, body').prepend(cont);
      return { discX: X.preguntas.filter(q => q.disc).map(q => q.n), discP: P.preguntas.filter(q => q.disc).map(q => q.n),
               ret96: !!q96.retenida, fuera96: fuera(q96), c96: q96.c,
               pill: cont.querySelectorAll('.tag-disc').length, bloques: cont.querySelectorAll('.disc-lit').length,
               leyPlegada: !cont.querySelector('details.real-ley').open, texto: cont.querySelector('.disc-lit').innerText.slice(0, 120) };
    });
    console.log(w, JSON.stringify(r));
    await p.locator('#prueba-disc').screenshot({ path: `/tmp/claude-0/-home-user-niblo/d4a06324-57c5-5c80-9659-94fd013c3913/scratchpad/disc-${w}.png` });
  }
  console.log('ERRORES', JSON.stringify(errs)); await b.close();
})();
