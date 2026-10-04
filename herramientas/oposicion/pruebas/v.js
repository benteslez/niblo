const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('http://localhost:8765/oposicion.html'); await p.waitForTimeout(500);
  const r = await p.evaluate(() => ({
    verde: TEMAS.filter(t => semaforo(t)==='verde').map(t=>t.c).join(', '),
    ambar: TEMAS.filter(t => semaforo(t)==='ambar').map(t=>t.c).join(', '),
    act: TEMAS.filter(t => t.v[0]==='ACTUALIZAR').map(t=>t.c).join(', '),
    boe: TEMAS.filter(t => t.f[0]==='BOE').map(t=>t.c).join(', '),
    boet: TEMAS.filter(t => t.f[0]==='BOE+T').map(t=>t.c).join(', '),
    inst: TEMAS.filter(t => t.f[0]==='INST').map(t=>t.c).join(', '),
    boeIds: [...new Set(TEMAS.flatMap(t => (t.n+t.i+t.p+t.v[1]).match(/BOE-A-\d{4}-\d+/g)||[]))].length,
    n: TEMAS.length, porBloque: BLOQUES.map(b=>b.total).join('/')
  }));
  const pdf = {
    verde: 'I.2, I.4, I.9, I.10, I.11, IV.2, IV.4, IV.8, IV.10, IV.12, V.2, V.5, V.8, V.10, VI.3, VI.6',
    ambar: 'I.1, I.3, I.5, I.6, III.8, IV.6, IV.11, IV.13, V.1, V.3, V.4, V.7, VI.7',
    act: 'I.8, II.5, III.1, III.2, III.5, III.6, III.7, III.10, IV.5, V.6, VI.2, VI.8',
    boe: 'I.1, I.2, I.3, I.4, I.5, I.6, I.8, I.9, I.10, I.11, III.8, IV.2, IV.4, IV.5, IV.6, IV.8, IV.10, IV.11, IV.12, IV.13, V.1, V.2, V.3, V.4, V.5, V.6, V.7, V.8, V.10, VI.3, VI.6, VI.7',
    boet: 'I.7, II.2, II.3, II.4, III.4, III.5, III.6, III.7, III.9, IV.1, IV.3, IV.7, IV.9, V.9, VI.1, VI.2, VI.4, VI.5, VI.8',
    inst: 'II.1, II.5, II.6, III.1, III.2, III.3, III.10'
  };
  for (const k in pdf) console.log(k, r[k] === pdf[k] ? 'OK' : 'DIFERENTE\n  app: ' + r[k] + '\n  pdf: ' + pdf[k]);
  console.log('temas', r.n, r.porBloque, 'ids BOE distintos', r.boeIds);
  await b.close();
})();
