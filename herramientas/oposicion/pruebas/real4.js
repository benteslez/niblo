const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch(); const errs=[];
  const ctx = await b.newContext({ viewport:{width:1280,height:900} }); const p = await ctx.newPage();
  p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type()==='error') errs.push('consola: '+m.text()); });
  await p.goto('http://localhost:8765/oposicion.html#/real'); await p.waitForTimeout(1300);
  await p.click('[data-modo="examen"]'); await p.waitForTimeout(250);
  console.log('ventana examen:', (await p.locator('dialog').innerText()).replace(/\s+/g,' ').slice(-520));
  await p.screenshot({ path:'k-dlg-ex.png' });
  await p.click('dialog [data-empezar]'); await p.waitForTimeout(300);
  console.log('examen:', await p.evaluate(() => ({ n:real.ex.qs.length, ultima:real.ex.qs[99].q.n + (real.ex.qs[99].q.reserva?' (reserva '+real.ex.qs[99].q.nr+')':''), hay82:real.ex.qs.some(it=>it.q.n===82), min:Math.round((real.ex.fin-real.ex.inicio)/60000) })));
  await p.evaluate(() => { const E = real.ex; E.qs.forEach((it,k) => { E.resp[k] = k < 70 ? it.q.c : k < 90 ? (it.q.c+1)%4 : null; }); });
  p.once('dialog', d => d.accept()); await p.click('#sim-entregar'); await p.waitForTimeout(300);
  console.log('resultado:', (await p.locator('.resultado').innerText()).replace(/\s+/g,' ').slice(0,140));
  await p.click('#r-fin'); await p.waitForTimeout(200);
  // Inicio: alineación
  await p.goto('http://localhost:8765/oposicion.html#/'); await p.waitForTimeout(1200);
  console.log('títulos alineados (x):', await p.evaluate(() => [...document.querySelectorAll('.dash-t')].map(e => Math.round(e.getBoundingClientRect().left)).join(' / ')));
  await p.locator('.dash-card').first().scrollIntoViewIfNeeded(); await p.screenshot({ path:'k-dash.png' });
  // Resaltado de colores
  await p.goto('http://localhost:8765/oposicion.html#/tema/B1T02/leer'); await p.waitForTimeout(2000);
  await p.click('[data-todo="1"]'); await p.waitForTimeout(400);
  const sel = async (txt) => { await p.evaluate(t => { const el=[...document.querySelectorAll('[data-cuerpo] p')].find(x=>x.textContent.includes(t)); const tn=[...el.childNodes].find(n=>n.nodeType===3 && n.textContent.includes(t)) || el.firstChild; const r=document.createRange(); const i=tn.textContent.indexOf(t); r.setStart(tn,Math.max(0,i)); r.setEnd(tn,Math.max(0,i)+t.length); el.scrollIntoView({block:'center'}); const s=getSelection(); s.removeAllRanges(); s.addRange(r); document.dispatchEvent(new Event('selectionchange')); }, txt); await p.waitForTimeout(200); };
  await sel('La Constitución tiene una');
  console.log('barra:', await p.evaluate(() => { const b=document.getElementById('barra-resaltar'); return { visible:!b.hidden, colores:[...b.querySelectorAll('.res-col')].map(x=>x.dataset.col).join(','), defecto:b.querySelector('.btn-resaltar').dataset.resCol }; }));
  await p.locator('#barra-resaltar').screenshot({ path:'k-barra.png' }).catch(()=>{});
  await p.screenshot({ path:'k-barra-ctx.png' });
  await p.click('#barra-resaltar .res-col[data-col="verde"]'); await p.waitForTimeout(300);
  await sel('Elige un bloque') .catch(()=>{});
  console.log('marca verde:', await p.evaluate(() => [...document.querySelectorAll('mark.res')].map(m=>m.dataset.col+':'+m.textContent.slice(0,25))));
  await p.reload(); await p.waitForTimeout(2000); await p.click('[data-todo="1"]'); await p.waitForTimeout(300);
  await sel('parte dogmática');
  console.log('tras recargar, por defecto:', await p.evaluate(() => document.querySelector('#barra-resaltar .btn-resaltar').dataset.resCol), '· marcas:', await p.evaluate(() => [...document.querySelectorAll('mark.res')].map(m=>m.dataset.col)));
  console.log('ERRORES', errs); await b.close();
})();
