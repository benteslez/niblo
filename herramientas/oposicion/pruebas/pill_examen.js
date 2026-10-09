// La pill «Examen» (y su frase) abre un diálogo con la pregunta y la respuesta de la plantilla. Requiere `python3 -m http.server 8765` en la raíz.
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
const OUT = process.env.SHOTS || '.';
(async () => {
  const b = await chromium.launch(); const errs = []; let fallos = 0;
  const ok = (c, m) => { console.log(c ? 'OK ' : 'FALLA', m); if (!c) fallos++; };
  for (const [nombre, vp] of [['esc', { width:1280, height:900 }], ['mov', { width:390, height:800 }]]) {
    const p = await (await b.newContext({ viewport:vp })).newPage();
    p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type()==='error') errs.push(m.text()); });
    await p.goto('http://localhost:8765/oposicion.html#/tema/B1T01/leer'); await p.waitForTimeout(2500);
    const pills = p.locator('.pill-exa[data-ex]');
    ok(await pills.count() > 5, nombre + ': pills clicables ' + await pills.count());
    await p.evaluate(() => irASeccion('s2', true)); await p.waitForTimeout(800);
    const con = p.locator('p:has(> .pill-exa[data-ex="P24.48"])'); await con.first().scrollIntoViewIfNeeded();
    await con.first().locator('strong').first().click();
    await p.waitForSelector('dialog.ex-dlg[open]', { timeout:4000 });
    const txt = await p.locator('dialog.ex-dlg').innerText();
    ok(/GACE-P 2024/.test(txt) && /artículo 49/.test(txt) && /entornos universalmente accesibles\. ✔/.test(txt), nombre + ': diálogo P24.48 con respuesta marcada');
    await p.screenshot({ path:`${OUT}/${nombre}-pill-dlg.png` });
    await p.keyboard.press('Escape'); await p.waitForTimeout(200);
    // 2025: sale de tests-reales
    const l = p.locator('.pill-exa[data-ex*="X."]:visible').first();
    if (await l.count()) { await l.click(); await p.waitForSelector('dialog.ex-dlg[open]'); const t = await p.locator('dialog.ex-dlg').innerText(); ok(/2025/.test(t) && /✔/.test(t), nombre + ': pregunta de 2025'); await p.keyboard.press('Escape'); }
  }
  console.log('errores de consola:', errs.length ? errs.join(' | ') : 'ninguno'); await b.close(); process.exit(fallos || errs.length ? 1 : 0);
})();
