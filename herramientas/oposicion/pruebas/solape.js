// Uso: node tema.js B4T02  → comprueba un tema publicado en temas/ (escritorio y móvil)
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
const ID = process.argv[2];
(async () => {
  const b = await chromium.launch();
  for (const [w,h] of [[1280,900],[390,844]]) {
    const p = await b.newPage({ viewport:{width:w,height:h} });
    for (const ID of (process.argv.slice(2).length ? process.argv.slice(2) : ['B2T01','B4T13','B2T06','B4T10'])) {
      await p.goto(`http://localhost:8765/oposicion.html#/tema/${ID}/leer`); await p.waitForTimeout(2500); await p.click('[data-todo="1"]'); await p.waitForTimeout(600);
      const r = await p.evaluate(() => {
        let n=0, mal=0, ej=[];
        for (const bq of document.querySelectorAll('blockquote.literal')) {
          const pill = bq.querySelector('.lit-boe'); const p1 = bq.querySelector('p'); if (!pill||!p1) continue;
          n++; const a=pill.getBoundingClientRect();
          const rng=document.createRange(); rng.selectNodeContents(p1);
          for (const c of rng.getClientRects()) { if (a.left<c.right && c.left<a.right && a.top<c.bottom && c.top<a.bottom) { mal++; ej.push(pill.textContent+': '+p1.textContent.slice(0,40)); break; } }
        }
        return {n, mal, ej:ej.slice(0,3)};
      });
      console.log(w, ID, JSON.stringify(r));
    }
  }
  await b.close();
})();
