const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => { const b = await chromium.launch(); const e = [];
  for (const [w, h, f] of [[1140, 1100, 'i-escritorio'], [390, 1500, 'i-movil']]) {
    const p = await b.newPage({ viewport:{ width:w, height:h } }); p.on('pageerror', x => e.push(x.message));
    await p.goto('http://localhost:8765/oposicion.html'); await p.waitForTimeout(600);
    await p.evaluate(async () => { const t = normalizarTema('B4T11', { sections:[{ id:'a', title:'Uno', body:'x' }, { id:'b', title:'Dos', body:'y' }], flashcards:[{ q:'q', a:'a' }, { q:'q2', a:'a2' }] }, '', null); await guardarTema(t); marcarProg('B4T11:sec:a', true); marcarFc(claveFc('B4T11', t.flashcards[0]), true); render(); });
    await p.waitForTimeout(300); await p.screenshot({ path:__dirname + '/' + f + '.png', fullPage:false });
    console.log(f, 'overflow', await p.evaluate(() => document.documentElement.scrollWidth - innerWidth));
  }
  console.log('errores', e); await b.close(); })();
