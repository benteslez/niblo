// Uso: node tema.js B4T02  → comprueba un tema publicado en temas/ (escritorio y móvil)
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
const ID = process.argv[2];
(async () => {
  const b = await chromium.launch(); const errs = [];
  for (const [nom, vp] of [['d', {width:1280,height:900}], ['m', {width:390,height:844}]]) {
    const p = await b.newPage({ viewport:vp }); p.on('pageerror', e => errs.push(e.message));
    await p.goto(`http://localhost:8765/oposicion.html#/tema/${ID}/leer`); await p.waitForTimeout(2500);
    await p.click('[data-todo="1"]'); await p.waitForTimeout(500);
    const info = await p.evaluate(() => ({ aps:document.querySelectorAll('.ap[data-ap]').length, fichas:document.querySelectorAll('.ap-caja.ap-ficha').length, guias:document.querySelectorAll('.ap-caja.ap-guia').length,
      lit:document.querySelectorAll('blockquote.literal').length, boe:document.querySelectorAll('blockquote.literal .tag-boe').length, quiz:document.querySelectorAll('.ap-quiz').length,
      tablas:document.querySelectorAll('table.apuntes-tabla').length, filasSinClave:[...document.querySelectorAll('.fi-k')].filter(x=>!x.textContent.trim()).length, ov:document.documentElement.scrollWidth-innerWidth,
      crudo:[...document.querySelectorAll('.ap-cuerpo')].map(x=>x.innerText).join(' ').match(/\[\[|\*\*|=>|@>|%>|!>|\?>/g) }));
    // Pregunta interactiva: pulsar una incorrecta
    const q = p.locator('.ap-quiz').first(); await q.scrollIntoViewIfNeeded();
    await q.locator('.qz-op[data-ok="0"]').first().click(); await p.waitForTimeout(200);
    info.quizTras = await q.evaluate(x => ({ exp:[...x.querySelectorAll('.qz-exp')].filter(e=>!e.hidden).length, verde:x.querySelectorAll('.qz-op.bien,.qz-op.ok').length }));
    await p.screenshot({ path:`/tmp/${ID}-${nom}.png` });
    await p.locator('blockquote.literal').nth(3).scrollIntoViewIfNeeded(); await p.screenshot({ path:`/tmp/${ID}-${nom}-lit.png` });
    console.log(nom, JSON.stringify(info));
    await p.close();
  }
  // Test del tema
  const p = await b.newPage(); p.on('pageerror', e => errs.push(e.message));
  await p.goto(`http://localhost:8765/oposicion.html#/tema/${ID}`); await p.waitForTimeout(2500);
  console.log('preguntas del tema:', await p.evaluate(id => estado.temas[id] && estado.temas[id].questions.length, ID));
  console.log('ERRORES', errs); await b.close();
})();
