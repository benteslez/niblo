// Constitución · Memorizar: tablero, práctica en tres niveles, huecos progresivos, recitado y mini-juegos. Requiere `python3 -m http.server 8765` en la raíz.
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs = []; let fallos = 0;
  const ok = (c, m) => { console.log(c ? 'OK ' : 'FALLA', m); if (!c) fallos++; };
  for (const [nombre, vp] of [['esc', { width:1280, height:900 }], ['mov', { width:390, height:800 }]]) {
    const p = await (await b.newContext({ viewport:vp })).newPage();
    p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type()==='error') errs.push(m.text()); });
    await p.goto('http://localhost:8765/oposicion.html#/ce/memorizar'); await p.waitForTimeout(2500);
    ok(await p.locator('.cem-c').count() === 169, nombre + ': tablero con 169 casillas');
    const et = await p.evaluate(() => { let sin = 0, prop = 0; for (let n = 1; n <= 169; n++) { const e = cemEtq(n); if (!e.t) sin++; if (e.propio) prop++; } return [sin, prop]; });
    ok(et[0] === 0 && et[1] === 117, nombre + ': etiquetas en los 169 (' + et.join(' sin/propias ') + ')');
    // detalle
    await p.locator('.cem-c[data-cema="66"]').click(); await p.waitForTimeout(300);
    const det = await p.locator('#cem-det').innerText();
    ok(/Título III/i.test(det) && /Cortes Generales/i.test(det) && /etiqueta propia/i.test(det), nombre + ': detalle del art. 66');
    // huecos: etapa 0 oculta palabras, revelar las muestra; el recitado compara
    const h = await p.evaluate(() => { const a = cemClozeHTML(66, 0, false), r = cemClozeHTML(66, 0, true), i = cemClozeHTML(66, 2, false); const o0 = cemOcultas(66, 0), o1 = cemOcultas(66, 1); return [(a.match(/cem-h/g) || []).length, (r.match(/cem-r/g) || []).length, /cem-i/.test(i), [...o0].every(k => o1.has(k)), o1.size > o0.size]; });
    ok(h[0] > 0 && h[0] === h[1] && h[2] && h[3] && h[4], nombre + ': huecos progresivos ' + h.join(','));
    const cmp = await p.evaluate(() => { const t = CE_ART[1].p.join(' '); return [cemComparar(1, t).ratio, cemComparar(1, 'España es un Estado').ratio < 0.5, cemComparar(1, t.replace('libertad', 'igualdad')).ratio < 1]; });
    ok(cmp[0] === 1 && cmp[1] && cmp[2], nombre + ': comparación del recitado ' + cmp.join(','));
    // práctica de un artículo: tres tarjetas
    await p.locator('#cem-prac').click(); await p.waitForTimeout(400);
    const niveles = []; 
    for (let i = 0; i < 3; i++) {
      niveles.push(await p.locator('.cem-card .tag.acc').innerText());
      const r = p.locator('#cs-rev'); if (await r.count()) { if (/Comprobar/.test(await r.innerText())) await p.fill('#cs-ta', 'Las Cortes Generales representan al pueblo español'); await r.click(); await p.waitForTimeout(200); }
      await p.locator('[data-cc="5"]').click(); await p.waitForTimeout(200);
    }
    ok(/ubicación/i.test(niveles.join()) && /de qué va/i.test(niveles.join()) && /texto/i.test(niveles.join()), nombre + ': tres niveles ' + niveles.join(' | '));
    ok(/Sesión terminada/.test(await p.locator('#cem-cuerpo').innerText()), nombre + ': fin de sesión');
    const srs = await p.evaluate(() => ['u', 't', 'x'].map(l => !!cemSrs(66, l)));
    ok(srs.every(Boolean), nombre + ': calendario propio por nivel guardado');
    // tablero refleja el estado
    await p.locator('[data-cems="tablero"]').click(); await p.waitForTimeout(300);
    ok(await p.locator('.cem-c[data-cema="66"] .e2, .cem-c[data-cema="66"] .e3').count() >= 1, nombre + ': tablero con el artículo practicado');
    // práctica con selección
    await p.locator('[data-cems="practicar"]').click(); await p.waitForTimeout(300);
    await p.selectOption('#cf-nivel', 'x'); await p.selectOption('#cf-que', 'azar'); await p.selectOption('#cf-dif', '3'); await p.locator('#cf-ir').click(); await p.waitForTimeout(300);
    ok(/Solo iniciales/i.test(await p.locator('.cem-card').innerText()) && await p.locator('.cem-i').count() > 3, nombre + ': dificultad 3 (iniciales)');
    await p.evaluate(() => { CEM.ses = null; });
    // orden aleatorio: sin barajar salen ordenados por artículo; barajando, el mismo conjunto en otro orden
    const ord = await p.evaluate(() => { const c = { nivel:'mezcla', que:'todas', unidad:'P', max:0, dif:'auto', barajar:false }; const a = cemArmar(c).map(x => x.n + x.l), b = cemArmar(Object.assign({}, c, { barajar:true })).map(x => x.n + x.l); let dif = false; for (let k = 0; k < 8 && !dif; k++) dif = JSON.stringify(cemArmar(Object.assign({}, c, { barajar:true })).map(x => x.n + x.l)) !== JSON.stringify(a); return [a[0], a[1], a.length === b.length, [...a].sort().join() === [...b].sort().join(), dif]; });
    ok(ord[0] === '1t' || ord[0] === '1u' || ord[0] === '1x', nombre + ': sin barajar, ordenado por artículo ' + ord.slice(0, 2));
    ok(ord[2] && ord[3] && ord[4], nombre + ': con orden aleatorio, mismo conjunto y otro orden');
    await p.locator('[data-cems="practicar"]').click(); await p.waitForTimeout(200);
    await p.locator('#cf-baj').check(); ok(await p.evaluate(() => CEM.cfg.barajar === true), nombre + ': casilla «Orden aleatorio» guardada');
    await p.locator('#cf-baj').uncheck();
    // juegos
    await p.locator('[data-cems="juegos"]').click(); await p.waitForTimeout(300);
    for (const j of ['ubica', 'rango', 'tema']) {
      await p.locator(`[data-cej="${j}"]`).click(); await p.waitForTimeout(200);
      for (let i = 0; i < 10; i++) { await p.locator('.q-opt').first().click(); await p.locator('#jg-sig').click(); }
      ok(/\/ 10/.test(await p.locator('#cem-cuerpo').innerText()), nombre + ': juego ' + j + ' completo');
      await p.locator('#jg-menu').click(); await p.waitForTimeout(200);
    }
    await p.locator('[data-cej="orden"]').click(); await p.waitForTimeout(200);
    const n = await p.locator('[data-pz]').count();
    for (let i = 0; i < n; i++) await p.locator('[data-pz]').first().click();
    ok(/en su sitio/.test(await p.locator('#cem-cuerpo').innerText()), nombre + ': ordena la estructura (' + n + ' piezas)');
    const ordenOk = await p.evaluate(() => { const J = CEM.juego; return J.puestos.length; });
    ok(ordenOk === n, nombre + ': todas las piezas colocadas');
    ok(!(await p.evaluate(() => document.documentElement.scrollWidth > innerWidth + 2)), nombre + ': sin desbordamiento horizontal');
  }
  console.log('errores de consola:', errs.length ? errs.join(' | ') : 'ninguno'); await b.close(); process.exit(fallos || errs.length ? 1 : 0);
})();
