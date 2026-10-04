// Extrae artículos de un HTML de EUR-Lex: [{doc, art, ps:[...]}]
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const [ , , ent, sal] = process.argv;
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + require('path').resolve(ent));
  const arts = await p.evaluate(() => {
    document.querySelectorAll('a[id^="ntc"], .note-tag, .oj-note-tag').forEach(a => a.remove());
    const limpio = el => el.textContent.replace(/ /g, ' ').replace(/\s+/g, ' ').trim();
    const out = []; let doc = '', cur = null; const vistos = new Set();
    for (const el of document.querySelectorAll('p.doc-ti, p.ti-art, p.normal, p.sti-art, p.oj-doc-ti, p.oj-ti-art, p.oj-normal, p.oj-sti-art')) {
      if (el.matches('p.doc-ti, p.oj-doc-ti')) { if (!el.closest('table')) doc = limpio(el); continue; }
      if (el.matches('p.ti-art, p.oj-ti-art')) { cur = { doc, art: limpio(el), ps: [] }; out.push(cur); continue; }
      if (!cur) continue;
      if (el.matches('p.sti-art, p.oj-sti-art')) { cur.sti = limpio(el); continue; }
      const tr = el.closest('tr');
      if (tr) { if (vistos.has(tr)) continue; vistos.add(tr); cur.ps.push([...tr.children].map(limpio).filter(Boolean).join(' ')); }
      else cur.ps.push(limpio(el));
    }
    return out;
  });
  require('fs').writeFileSync(sal, JSON.stringify(arts, null, 0));
  console.log(sal, arts.length, [...new Set(arts.map(a => a.doc))].slice(0, 6));
  await b.close();
})();
