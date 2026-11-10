"""Lee la tabla «Calendario día a día» del PDF del menú (pdftotext -bbox) y la
guarda como JSON. Uso: pdftotext -bbox MENU.pdf bbox.html; python3 leer_pdf.py bbox.html calendario_dias.json
Cada palabra va a su columna por la x de la cabecera de su página (Fecha, Cocinar, Desayuno,
Comida, Cena); cada fila empieza en el día de la semana de la columna Fecha."""
import re, sys, json, html, datetime
src = open(sys.argv[1]).read()
pages = re.split(r'<page ', src)[1:]
DIAS = {"Lun","Mar","Mié","Jue","Vie","Sáb","Dom"}
rows = []; cur = None
for pg in pages:
    ws = [(float(a),float(b),float(c),float(d),html.unescape(t)) for a,b,c,d,t in re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', pg)]
    hdr = [w for w in ws if w[4]=="Fecha"]
    if not hdr: continue
    hy = hdr[0][1]
    line = [w for w in ws if abs(w[1]-hy)<2]
    names = {w[4]:w[0] for w in line}
    if "Cocinar" not in names: continue
    xs = [names["Fecha"], names["Cocinar"], names["Desayuno"], names["Comida"], names["Cena"]]
    def col(x):
        c = 0
        for i,b in enumerate(xs):
            if x >= b - 6: c = i
        return c
    body = sorted([w for w in ws if w[1] > hy+5 and not w[4].startswith("Page") and w[1] < 780], key=lambda w:(round(w[1]),w[0]))
    # drop footer words like "Page 7 of 38"
    lines = []
    for w in body:
        if lines and abs(lines[-1][0]-w[1])<2: lines[-1][1].append(w)
        else: lines.append([w[1],[w]])
    for y, lw in lines:
        txt = " ".join(w[4] for w in lw)
        if txt.startswith("Fecha Cocinar"):
            nm = {w[4]: w[0] for w in lw}; xs[:] = [nm["Fecha"], nm["Cocinar"], nm["Desayuno"], nm["Comida"], nm["Cena"]]; continue
        if re.match(r'^(Page \d+ of \d+|Menú semanal de Pablo)', txt) or re.match(r'^(Diciembre|Enero|Febrero|Marzo) 20\d\d$', txt): continue
        f0 = [w for w in lw if col(w[0])==0]
        if f0 and f0[0][4][:1].isupper() and f0[0][4] not in DIAS: cur = None; break
        if f0 and f0[0][4] in DIAS:
            cur = [[],[],[],[],[]]; rows.append(cur)
        if cur is None: continue
        for w in lw: cur[col(w[0])].append(w[4])
def limpia(ws): return re.sub(r'\s+', ' ', " ".join(ws).replace("​","")).strip()
d0 = datetime.date(2026,11,10); out=[]
for i,r in enumerate(rows):
    f = d0 + datetime.timedelta(i)
    fe = limpia(r[0])
    assert int(re.search(r'\d+', fe).group()) == f.day, (fe, f)
    out.append({"fecha": f.isoformat(), "f": fe, "cocinar": re.sub(r'^(Para )?Día de cocinar ?(Para )?', 'Para ', limpia(r[1])) if limpia(r[1]) else "", "de": limpia(r[2]), "c": limpia(r[3]), "ce": limpia(r[4])})
print(len(out), out[-1]["fecha"], file=sys.stderr)
json.dump(out, open(sys.argv[2],"w"), ensure_ascii=False, indent=0)
