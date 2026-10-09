const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs=[];
  const p = await b.newPage({ viewport:{width:1280,height:900} });
  p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type()==='error') errs.push('consola: '+m.text()); });
  await p.goto('http://localhost:8765/oposicion.html#/global'); await p.waitForTimeout(1500);
  const buscar = async t => { await p.fill('#q', t); await p.waitForTimeout(250); return { st:await p.locator('#st').innerText(), reales:await p.locator('.res-real').count(), primera:(await p.locator('.res-real').first().innerText().catch(()=>'-')).replace(/\s+/g,' ').slice(0,230) }; };
  console.log('Van Gend:', JSON.stringify(await buscar('Van Gend')));
  console.log('Defensor del Pueblo:', JSON.stringify(await buscar('Defensor del Pueblo')));
  await p.screenshot({ path:'b-global.png' });
  console.log('frase literal:', JSON.stringify(await buscar('arbitra y modera')));
  console.log('anulada:', JSON.stringify(await buscar('estabilidad presupuestaria')));
  await p.click('[data-tipo="real"]'); await p.waitForTimeout(200);
  console.log('chip tests reales (sin texto):', JSON.stringify(await buscar('')));
  // Hub del bloque II: solo las suyas
  await p.goto('http://localhost:8765/oposicion.html#/bloque/B1/hub'); await p.waitForTimeout(1200);
  console.log('bloque I, «Consejo Europeo»:', JSON.stringify(await buscar('Consejo Europeo')));
  console.log('bloque I, «Defensor del Pueblo»:', JSON.stringify(await buscar('Defensor del Pueblo')));
  console.log('ERRORES', errs); await b.close();
})();
