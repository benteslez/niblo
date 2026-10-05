// Test de tema: filtro «Academia», reales del test global en «De examen real» y progreso independiente.
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
const OUT = process.env.SHOTS || '/tmp';
(async () => {
  const b = await chromium.launch(); const errs = []; const ok = (c, m) => { console.log((c ? 'OK  ' : 'FALLA ') + m); if (!c) process.exitCode = 1; };
  const p = await (await b.newContext({ viewport:{ width:1000, height:900 } })).newPage();
  p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type()==='error') errs.push(m.text()); });
  await p.goto('http://localhost:8765/oposicion.html#/bloque/B1/hub'); await p.waitForTimeout(3000);
  await p.click('[data-tab="test"]'); await p.waitForTimeout(500);
  const chip = async m => (await p.locator(`[data-modo="${m}"] .badge`).innerText().catch(() => '0'));
  console.log('Todos los temas del bloque: academia', await chip('academia'), 'reales', await chip('reales'));
  for (const t of ['B1T01', 'B1T02', 'B1T03']) {
    await p.click('[data-tt="todos"]'); await p.click(`[data-tt="${t}"]`); await p.waitForTimeout(200);
    console.log(t, 'preguntas', await p.locator(`[data-tt="${t}"] .badge`).innerText(), '· disp:', await p.locator('.test-cfg .muted').innerText());
  }
  // Solo I.1 con filtro Academia
  await p.click('[data-tt="todos"]'); await p.click('[data-tt="B1T01"]');
  await p.click('[data-modo="academia"]'); await p.waitForTimeout(200);
  const n = parseInt(await p.locator('.test-cfg .muted').innerText(), 10); ok(n === 18, 'I.1 academia = 18 (' + n + ')');
  await p.selectOption('#tn', '50'); await p.click('#t-go'); await p.waitForTimeout(300);
  ok(await p.locator('.tag:has-text("Academia")').count() === 1, 'etiqueta Academia');
  // responder bien y mal: la explicación sale siempre
  const qtxt = await p.locator('.q-txt').innerText();
  const opts = p.locator('.q-opt'); await opts.nth(0).click();
  const fb = await p.locator('.q-fb').innerText(); ok(/Solución de la academia/.test(fb), 'explicación visible tras responder: ' + fb.slice(0, 90).replace(/\n/g, ' '));
  ok(!/\*\*/.test(fb), 'sin asteriscos de negrita'); ok(/documento original, la correcta es la [abcd]\)/.test(fb), 'letra original');
  await p.screenshot({ path:`${OUT}/ac1.png` });
  // Reales del tema I.3
  await p.reload(); await p.waitForTimeout(3000);
  await p.click('[data-tab="test"]'); await p.waitForSelector('[data-tt="B1T03"]', { timeout:15000 }); await p.click('[data-tt="B1T03"]'); await p.click('[data-modo="reales"]'); await p.waitForTimeout(200);
  console.log('I.3 reales:', await p.locator('.test-cfg .muted').innerText());
  await p.selectOption('#tn', '50'); await p.click('#t-go'); await p.waitForTimeout(300);
  ok(await p.locator('.tag:has-text("Examen real")').count() === 1, 'etiqueta Examen real');
  const q1 = await p.locator('.q-txt').innerText();
  // fallar a propósito: elegir una incorrecta (la que no sea correcta según la pista tras clic)
  await p.locator('.q-opt').nth(0).click();
  const fb2 = await p.locator('.q-fb').innerText(); console.log('feedback real:', fb2.slice(0, 160).replace(/\n/g, ' '));
  ok(await p.locator('details.real-ley').count() === 1, 'texto legal presente');
  await p.screenshot({ path:`${OUT}/ac2.png` });
  // independencia: el progreso global del test real (R:…) no cambia
  const claves = await p.evaluate(() => Object.keys(prog.mapa));
  ok(claves.some(k => /^B1T03:q:/.test(k)) && !claves.some(k => k.startsWith('R:')), 'progreso con clave del tema (B1T03:q:…) y ninguna R:… del test real global: ' + claves.filter(k => /:q:|^R:/.test(k)).join(', '));
  console.log('ERRORES', errs); await b.close();
})();
