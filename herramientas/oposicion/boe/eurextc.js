// Extrae artículos de un TEXTO CONSOLIDADO de EUR-Lex (CELEX:0…, clases title-article-norm / norm /
// grid-list): [{doc, art, sti, ps:[...]}], con el mismo formato que eurext.js (textos del DO).
// Se quitan las marcas de modificación (▼M1, ▼B…) y las llamadas a notas; solo artículos (no anexos).
const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const [ , , ent, sal] = process.argv;
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + require('path').resolve(ent));
  const arts = await p.evaluate(() => {
    document.querySelectorAll('p.modref, p.arrow, a.anchorarrow, a[id^="ntc"], .note-tag, .oj-note-tag, p.footnote').forEach(a => a.remove());
    // Llamadas a notas «&nbsp;(<a id="src.E0004">4</a>)»: fuera la llamada y sus paréntesis.
    document.querySelectorAll('a[id^="src.E"]').forEach(a => {
      const pr = a.previousSibling, nx = a.nextSibling;
      if (pr && pr.nodeType === 3) pr.textContent = pr.textContent.replace(/[\s\u00a0]*\($/, '');
      if (nx && nx.nodeType === 3) nx.textContent = nx.textContent.replace(/^\)/, '');
      a.remove();
    });
    const limpio = el => el.textContent.replace(/ /g, ' ').replace(/\s+/g, ' ').trim();
    const out = [];
    for (const t of document.querySelectorAll('p.title-article-norm')) {
      // Con marcado ELI, el artículo es su div.eli-subdivision; sin él, los hermanos que siguen
      // al título hasta el siguiente artículo o anexo.
      const caja = t.closest('div.eli-subdivision');
      let hijos = [];
      if (caja) hijos = [...caja.children];
      else for (let x = t.nextElementSibling; x && !x.matches('p.title-article-norm, p[class^="title-annex"]') && !x.querySelector('p.title-article-norm'); x = x.nextElementSibling) hijos.push(x);
      const sti = caja ? caja.querySelector('p.stitle-article-norm') : hijos.find(x => x.matches('p.stitle-article-norm'));
      const cur = { doc: 'principal', art: limpio(t), sti: sti ? limpio(sti) : '', ps: [] };
      const pre = { v: '' };
      const pon = txt => { txt = (pre.v + txt).replace(/\s+/g, ' ').trim(); pre.v = ''; if (txt) cur.ps.push(txt); };
      const rec = n => {
        if (n.nodeType !== 1) return;
        if (n.matches('p.title-article-norm, div.eli-title, p.stitle-article-norm')) return;
        if (n !== caja && n.matches('div.eli-subdivision') && n.querySelector('p.title-article-norm')) return;
        if (n.matches('div.grid-list')) {
          const c1 = n.querySelector('.grid-list-column-1'), c2 = n.querySelector('.grid-list-column-2');
          pre.v += (c1 ? limpio(c1) : '') + ' '; if (c2) [...c2.children].forEach(rec); else pon(''); return;
        }
        if (n.matches('div.norm') && n.querySelector(':scope > span.no-parag')) {
          pre.v += limpio(n.querySelector(':scope > span.no-parag')) + ' ';
          [...n.children].filter(x => !x.matches('span.no-parag')).forEach(rec); return;
        }
        if (n.matches('table')) { n.querySelectorAll('tr').forEach(tr => pon([...tr.children].map(limpio).filter(Boolean).join(' '))); return; }
        if (n.matches('p') || (n.matches('div') && !n.querySelector('p, div, table'))) { pon(limpio(n)); return; }
        [...n.children].forEach(rec);
      };
      hijos.forEach(rec);
      out.push(cur);
    }
    return out;
  });
  require('fs').writeFileSync(sal, JSON.stringify(arts, null, 0));
  console.log(sal, arts.length);
  await b.close();
})();
