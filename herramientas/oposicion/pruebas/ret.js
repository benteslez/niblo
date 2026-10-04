const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage(); const errs=[]; p.on('pageerror', e => errs.push(e.message));
  await p.goto('http://localhost:8765/oposicion.html#/real'); await p.waitForTimeout(1500);
  const r = await p.evaluate(() => {
    const X = TESTS_REALES.examenes.find(x => x.id === 'GACE-X-2025-1');
    const c = Object.assign({}, cfgReal(), { anios:[2025], accesos:['extraordinaria'], filtro:'todas', bloque:'todos' });
    const ex = examenCompleto(c), sel = preguntasSel(c, 'repaso');
    const P = Object.assign({}, c, { accesos:['promocion'] });
    return { examenes:TESTS_REALES.examenes.map(x => x.id + ':' + x.preguntas.length), exX:ex.length, tiene96:ex.some(it => it.q.n === 96), reservas:ex.filter(it => it.q.reserva).map(it => it.q.nr),
             repaso96:sel.some(it => (it.q || it).n === 96), exP:examenCompleto(P).length, resP:examenCompleto(P).filter(it => it.q.reserva).map(it => it.q.nr) };
  });
  console.log(JSON.stringify(r)); console.log('ERRORES', errs); await b.close();
})();
