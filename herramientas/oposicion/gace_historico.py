# -*- coding: utf-8 -*-
"""Lee los cuestionarios y plantillas de los exámenes GACE anteriores a 2025 (PDF de sede.inap.gob.es, volcados a .txt con pymupdf)
→ lista de preguntas {n, q, o:[a,b,c,d], c} con la respuesta de la plantilla. Los de 2018 son imágenes (sin capa de texto)."""
import re, json, os, sys

PIE = re.compile(r"\s*(?:\d{4}\s+GACE-[\w\-]+|\d{2}/GACE-\w+\s+\d+\s*/\s*\d+|GACEPI\s+\d{4}\s+\d+-\d+)\s*$")   # pie de página pegado al final de una opción
def _pie(t): return PIE.sub("", t).strip()

def preguntas(txt):
    txt = re.sub(r"\n\s*\d{4}\s*-\s*GACE[^\n]*\n\s*Página \d+ de \d+\s*\n", "\n", txt)
    txt = re.sub(r"Página \d+ de \d+", "", txt)
    # número de pregunta: «N.» en su línea o seguido de texto, en orden creciente
    marcas, pos, esperado = [], 0, 1
    while True:
        m = None
        for c in re.compile(r"(?m)^\s*%d\.\s*(?=\S|\n)" % esperado).finditer(txt, pos):
            if re.search(r"(?ms)^\s*a\)", txt[c.end(): c.end() + 1500]): m = c; break
        if not m: break
        marcas.append((esperado, m.start(), m.end())); pos = m.end(); esperado += 1
    out = []
    for i, (n, a, b) in enumerate(marcas):
        cuerpo = txt[b: marcas[i + 1][1] if i + 1 < len(marcas) else len(txt)]
        partes = re.split(r"(?m)^\s*([abcd])\)\s*", cuerpo)
        if len(partes) < 9: out.append({"n": n, "q": " ".join(cuerpo.split()), "o": [], "raw": True}); continue
        q = _pie(" ".join(partes[0].split())); o = []
        for j in range(1, len(partes), 2): o.append(_pie(" ".join(partes[j + 1].split())))
        out.append({"n": n, "q": q, "o": o[:4]})
    return out

def plantilla(txt):
    t = " ".join(txt.split())
    return {int(n): l.lower() for n, l in re.findall(r"(\d{1,3})\.\s*([abcdABCD]|ANULADA)\b", t)}

def examen(base, dir_="."):
    q = preguntas(open(os.path.join(dir_, base + ".txt"), encoding="utf-8").read())
    pf = os.path.join(dir_, base + "-plantilla.txt")
    P = plantilla(open(pf, encoding="utf-8").read()) if os.path.exists(pf) else {}
    for x in q:
        l = P.get(x["n"]); x["c"] = "abcd".index(l) if l in list("abcd") else None; x["anulada"] = (l == "anulada")
    return q

if __name__ == "__main__":
    d = sys.argv[1]
    for b in sorted(f[:-4] for f in os.listdir(d) if re.match(r"\d{4}-01(L|P|X|ST|STX)\.txt$", f)):
        q = examen(b, d); print(b, len(q), "sin opciones:", sum(1 for x in q if not x["o"]), "sin plantilla:", sum(1 for x in q if x["c"] is None))
