const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage({viewport:{width:1100,height:900}}); const errs=[];
 p.on('pageerror', e => errs.push(e.message));
 await p.goto('http://localhost:8765/oposicion.html#/bloque/B5/hub'); await p.waitForTimeout(2500);
 await p.click('[data-tab="fc"]'); await p.waitForTimeout(500);
 let n=0, hallado=0;
 for (let i=0;i<400 && hallado<3;i++) {
   const hay = await p.locator('#fc').count(); if(!hay) break;
   await p.evaluate(()=>document.getElementById('fc').click()); await p.waitForTimeout(30);
   const chips = await p.locator('.fc-const .chip-art').count();
   if (chips) { hallado++; console.log('tarjeta con chips:', (await p.locator('.fc-q').innerText()).slice(0,80), '|', (await p.locator('.fc-const').allInnerTexts()).join(' / ').replace(/\n/g,' '));
     if (hallado===1) { await p.screenshot({path:'/tmp/claude-0/-home-user-niblo/d4a06324-57c5-5c80-9659-94fd013c3913/scratchpad/shots/chips.png'}); console.log(JSON.stringify(await p.locator('.fc-const .chip-art').first().evaluate(e=>{const r=e.getBoundingClientRect();const c=document.querySelector('.fc-cara.atras').getBoundingClientRect();return {r:[r.x,r.y,r.width,r.height],c:[c.x,c.y,c.width,c.height], vis:getComputedStyle(e).visibility}}))); await p.locator('.fc-const .chip-art').first().click(); await p.waitForTimeout(300); console.log('modal:', (await p.locator('dialog.pl-dlg').innerText()).replace(/\s+/g,' ').slice(0,300)); await p.screenshot({path:'/tmp/claude-0/-home-user-niblo/d4a06324-57c5-5c80-9659-94fd013c3913/scratchpad/shots/modal.png'}); await p.keyboard.press('Escape'); await p.waitForTimeout(200);} }
   await p.evaluate(()=>document.getElementById('fc-no').click()); n++;
 }
 console.log('recorridas', n, 'errores', errs); await b.close(); })();
