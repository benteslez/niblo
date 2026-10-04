const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
const S = __dirname;
(async () => {
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport:{ width:390, height:844 } });
  const page = await ctx.newPage();
  const errs = [];
  page.on('pageerror', e => errs.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error') errs.push('console: ' + m.text()); });
  await page.goto('http://localhost:8765/oposicion.html');
  await page.waitForTimeout(800);
  console.log('bloques', await page.locator('.mod-card').count());
  await page.screenshot({ path:S+'/1-inicio.png', fullPage:true });
  await page.click('.mod-card[data-b="B4"] .btn-primary');
  await page.waitForTimeout(300);
  console.log('temas B4', await page.locator('.tema2').count());
  await page.screenshot({ path:S+'/2-bloque.png', fullPage:true });
  await page.click('[data-tema="B4T11"]');
  await page.waitForTimeout(300);
  console.log('links BOE', await page.locator('a[href*="boe.es/buscar/act.php"]').count());
  await page.screenshot({ path:S+'/3-tema.png', fullPage:true });
  // Cargar un tema de ejemplo como HTML con TEMARIO_DATA (id por código romano)
  const html = `<!DOCTYPE html><html><head><script>window.TEMARIO_DATA={"IV.11":{"title":"LPAC","subtitle":"Prueba","sections":[{"id":"s1","title":"1. Intro"},{"id":"s1-1","title":"1.1 Sub"}],
   "glossary":[{"t":"Silencio administrativo","d":"Ficción legal ante la falta de resolución expresa.","cat":"procedimiento","section":"s1"},{"t":"Ñandú","d":"Prueba eñe"}],
   "timeline":[{"y":"2015","txt":"Ley 39/2015","cons":"Nueva LPAC","cat":"normativo","target":"s1"},{"y":"1992","txt":"Ley 30/1992","cons":"Antigua LRJPAC","cat":"normativo"}],
   "flashcards":[{"cat":"Plazos","q":"Plazo máximo general para resolver","a":"3 meses (art. 21.3 LPAC)"},{"q":"q2","a":"a2"}],
   "questions":[{"q":"Plazo general máximo de resolución si la norma no fija otro","o":["1 mes","3 meses","6 meses","10 días"],"c":1,"e":"Art. 21.3"},{"q":"Mala","o":["a"],"c":0},{"q":"Tres opciones","o":["x","y","z"],"c":2,"e":"z"}]}};<\/script></head><body><section id="s1">Hola</section></body></html>`;
  await page.evaluate(async (h) => { await procesarArchivos([new File([h], 'IV11.html', { type:'text/html' })]); }, html);
  await page.waitForTimeout(1500);
  console.log('cargados', await page.evaluate(() => Object.keys(estado.temas)), 'preguntas validas', await page.evaluate(() => estado.temas.B4T11 && estado.temas.B4T11.questions.length));
  await page.screenshot({ path:S+'/4-tema-cargado.png', fullPage:true });
  // Hub del bloque: cada pestaña
  await page.goto('http://localhost:8765/oposicion.html#/bloque/B4/hub');
  await page.waitForTimeout(800);
  for (const tab of ['buscar','crono','glosario','fc','test','progreso']) {
    await page.click(`[data-tab="${tab}"]`); await page.waitForTimeout(150);
  }
  await page.click('[data-tab="glosario"]'); await page.click('.letra[data-l="Ñ"]');
  console.log('glosario Ñ', await page.locator('#res .res').count());
  await page.click('[data-tab="buscar"]'); await page.fill('#q', 'silencio');
  console.log('busqueda', await page.locator('#res .res').count());
  await page.click('[data-tab="fc"]'); await page.click('#fc'); await page.click('#fc-si');
  console.log('fc known', await page.evaluate(() => Object.keys(prog.mapa).filter(k => prog.mapa[k].s)));
  await page.click('[data-tab="test"]'); await page.click('#t-go');
  for (let i=0;i<5;i++) { const opt = page.locator('.q-opt').first(); if (!(await opt.count())) break; await opt.click(); await page.click('#t-sig'); }
  console.log('resultado', (await page.locator('.resultado').innerText()).replace(/\n/g,' | '));
  await page.screenshot({ path:S+'/5-test.png', fullPage:true });
  await page.goto('http://localhost:8765/oposicion.html#/global'); await page.waitForTimeout(600);
  await page.click('[data-tab="progreso"]');
  await page.screenshot({ path:S+'/6-global.png', fullPage:true });
  await page.goto('http://localhost:8765/oposicion.html#/guia'); await page.waitForTimeout(600);
  console.log('guia botones', await page.locator('.lista-temas button').count());
  await page.screenshot({ path:S+'/7-guia.png', fullPage:true });
  // Persistencia tras recarga
  await page.reload(); await page.waitForTimeout(800);
  console.log('tras recarga', await page.evaluate(() => Object.keys(estado.temas)));
  // Plantilla -> se vuelve a cargar
  const [dl] = await Promise.all([page.waitForEvent('download'), page.evaluate(() => { const a=document.createElement('a'); a.href=URL.createObjectURL(new Blob([`<script>window.TEMARIO_DATA={"B1T03":{"glossary":[{"t":"x","d":"y"}]}}<\/script>`],{type:'text/html'})); a.download='B1T03_estudio.html'; document.body.appendChild(a); a.click(); })]);
  const p = await dl.path(); const txt = require('fs').readFileSync(p,'utf8');
  await page.evaluate(async (h) => { await procesarArchivos([new File([h], 'B1T03_estudio.html')]); }, txt);
  await page.waitForTimeout(1200);
  console.log('plantilla recargada', await page.evaluate(() => Object.keys(estado.temas)));
  // Oscuro, escritorio
  await page.setViewportSize({ width:1280, height:900 });
  await page.goto('http://localhost:8765/oposicion.html'); await page.click('#btn-tema'); await page.waitForTimeout(400);
  await page.screenshot({ path:S+'/8-oscuro.png', fullPage:false });
  // overflow horizontal en móvil
  await page.setViewportSize({ width:360, height:800 });
  for (const h of ['#/', '#/bloque/B3', '#/tema/B3T10', '#/guia', '#/bloque/B4/hub']) {
    await page.goto('http://localhost:8765/oposicion.html' + h); await page.waitForTimeout(400);
    const ov = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
    console.log('overflow', h, ov);
  }
  console.log('ERRORES', errs);
  await browser.close();
})();
