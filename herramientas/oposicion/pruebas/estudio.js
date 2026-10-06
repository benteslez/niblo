// Repaso rápido, Detecta el cambio, errores por tipo, plazos y mayorías, frecuencia y vigencia. Requiere `python3 -m http.server 8765` en la raíz.
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs = []; let fallos = 0;
  const ok = (c, m) => { console.log(c ? 'OK ' : 'FALLA', m); if (!c) fallos++; };
  for (const [nombre, vp] of [['esc', { width:1280, height:900 }], ['mov', { width:390, height:800 }]]) {
    const p = await (await b.newContext({ viewport:vp })).newPage();
    p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type()==='error') errs.push(m.text()); });
    await p.goto('http://localhost:8765/oposicion.html#/tema/B1T02/leer'); await p.waitForTimeout(2500);
    // tipos de error
    const t = await p.evaluate(() => [tipoError('un plazo de tres meses', 'un plazo de seis meses'), tipoError('mayoría absoluta del Congreso', 'mayoría simple del Congreso'), tipoError('el Senado', 'el Congreso de los Diputados'), tipoError('quince miembros', 'doce miembros'), tipoError('la ley regulará', 'el reglamento regulará')]);
    ok(t.join() === 'plazo,mayoria,organo,cifra,otro', nombre + ': clasificación ' + t.join());
    // frases y mutaciones
    const nf = await p.evaluate(() => frasesLiterales(estado.temas.B1T02).length);
    ok(nf > 10, nombre + ': frases alterables ' + nf);
    const mut = await p.evaluate(() => { const r = mutaciones('El Senado decidirá por mayoría absoluta en el plazo de dos meses.'); return r.map(x => x.tipo).sort().join(); });
    ok(mut === 'mayoria,organo,plazo', nombre + ': mutaciones ' + mut);
    // paneles del lector
    for (const [h, re] of [['rapido', /Ojo en el examen|En resumen|Examen/], ['cambio', /fiel|alterad/], ['vigencia', /auditor/i]]) {
      await p.evaluate(x => abrirPanel(x), h); await p.waitForTimeout(500);
      const txt = await p.locator('#panel-cuerpo').innerText();
      ok(re.test(txt), nombre + ': panel ' + h + ' (' + txt.length + ' car.)');
    }
    // Detecta el cambio: contestar y comprobar el registro
    await p.evaluate(() => { CAMBIO.id = null; abrirPanel('cambio'); }); await p.waitForTimeout(400);
    await p.locator('[data-cm="fiel"]').click(); await p.waitForTimeout(200);
    ok(await p.locator('#cm-fb .q-fb').count() === 1, nombre + ': corrección de Detecta el cambio');
    await p.evaluate(() => cerrarPanel(true));
    // vistas globales
    for (const [tab, re] of [['plazos', /Plazos y mayor/], ['frecuencia', /preguntas en/], ['errores', /Errores|fallos|errores/], ['vigencia', /Última auditoría/]]) {
      await p.goto('http://localhost:8765/oposicion.html#/datos/' + tab); await p.waitForTimeout(1200);
      const txt = await p.locator('#vista, main').first().innerText();
      ok(re.test(txt), nombre + ': datos/' + tab);
    }
    await p.goto('http://localhost:8765/oposicion.html#/datos/plazos'); await p.waitForTimeout(1000);
    ok(await p.locator('#dt-cuerpo tbody tr').count() > 5, nombre + ': plazos con filas ' + await p.locator('#dt-cuerpo tbody tr').count());
    const wide = await p.evaluate(() => document.documentElement.scrollWidth > innerWidth + 2);
    ok(!wide, nombre + ': sin desbordamiento horizontal');
  }
  console.log('errores de consola:', errs.length ? errs.join(' | ') : 'ninguno'); await b.close(); process.exit(fallos || errs.length ? 1 : 0);
})();
