# -*- coding: utf-8 -*-
"""Marcas «Examen» de los exámenes GACE anteriores a 2025 (cuestionarios y plantillas de sede.inap.gob.es, ver gace_historico.py).

Solo se marca lo que el propio enunciado deja claro: la pregunta cita «artículo N» de una norma que está en `boe/` (no se adivina nada
de memoria). Cada marca va al tema donde ese artículo está citado literalmente en los apuntes (volcado NIBLO_LITS) y queda en el registro
`marcas_examen.json` con la convocatoria y el n.º de pregunta. Lo que no se puede ubicar así se lista aparte (no se inventa).

Uso:  python3 gace_marcas.py DIR_TXT DIR_LITS     (DIR_TXT = carpeta con los .txt de los PDF; DIR_LITS = volcados de `lit()` por tema)
"""
import os, sys, re, json
ARGV = sys.argv[:]   # plantilla.py recorta sys.argv
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [AQUI, os.path.join(AQUI, "boe")]
import plantilla as P
import gace_historico as G
import marcas_examen as M

# nombre de convocatoria → código corto en las marcas (NOM en plantilla.Tema._marcas_examen)
EXAMENES = {"2024-01L": "L24", "2024-01P": "P24", "2022-01L": "L22", "2022-01P": "P22", "2022-01ST": "ST22",
            "2019-01L": "L19", "2019-01P": "P19", "2019-01ST": "ST19", "2019-01STX": "STX19"}

# «Ley 39/2015», «Real Decreto 364/1995»… → clave de boe/
NUM = {"39/2015": "L39", "40/2015": "L40", "9/2017": "LCSP", "47/2003": "LGP", "6/1985": "LOPJ", "29/1998": "LJCA", "7/1985": "LRBRL",
       "50/1997": "LGOB", "2/1979": "LOTC", "3/1981": "LODP", "58/2003": "LGT", "38/2003": "LGS", "3/2007": "LO3_2007", "1/2004": "LO1_2004",
       "19/2013": "L19_2013", "3/2018": "LOPD", "53/1984": "L53", "364/1995": "RD364", "598/1985": "RD598", "6/1997": "LOFAGE",
       "33/2003": "LPAP", "2/2012": "LOEP", "4/2000": "LOEX", "5/2015": "TREBEP", "2/1980": "LO2_1980", "3/1980": "LO3_1980",
       "20/2013": "L20_2013", "2016/679": "RGPD", "1/2008": "LO1_2008", "6/2013": "LO6_2013", "22/2009": "L22_2009", "8/1989": "L8_1989",
       "2/2014": "L2_2014", "25/2014": "L25_2014", "15/2014": "L15_2014", "5/1985": "LOREG", "2/2023": "L2_2023" if False else "RDL2_2023"}
TXT = [(r"Constituci[oó]n Espa[ñn]ola|la Constituci[oó]n|\bCE\b", "CE"), (r"Tratado de la Uni[oó]n Europea|\bTUE\b", "TUE"),
       (r"Funcionamiento de la Uni[oó]n Europea|\bTFUE\b", "TFUE"), (r"Estatuto B[aá]sico del Empleado P[uú]blico|\bTREBEP\b|\bEBEP\b", "TREBEP"),
       (r"Estatuto de los Trabajadores", "ET"), (r"Expropiaci[oó]n Forzosa", "LEF"), (r"C[oó]digo Civil", "CC"),
       (r"Reglamento del Congreso", "RCD"), (r"Reglamento del Senado", "RS"), (r"Ley General Presupuestaria", "LGP"),
       (r"Ley del Gobierno", "LGOB"), (r"Ley Org[aá]nica del Poder Judicial", "LOPJ"), (r"Ley de Contratos del Sector P[uú]blico", "LCSP"),
       (r"Procedimiento Administrativo Com[uú]n", "L39"), (r"R[eé]gimen Jur[ií]dico del Sector P[uú]blico", "L40"),
       (r"Tribunal Constitucional", "LOTC"), (r"Defensor del Pueblo", "LODP"), (r"Ley General Tributaria", "LGT"),
       (r"Jurisdicci[oó]n Contencioso", "LJCA"), (r"Bases del R[eé]gimen Local", "LRBRL")]
NORMA_NUM = re.compile(r"(?:Ley(?: Org[aá]nica)?|Real Decreto(?:-ley| Legislativo)?|Reglamento \(UE\)|Reglamento)\s+(?:n\.º\s*)?(\d{1,4}/\d{2,4})")
ART = re.compile(r"(?:art[ií]culos?|arts?\.)\s+(\d{1,3})(?:\.\d+|\s*(?:bis|ter))?")


def norma(q):
    """Clave de la primera norma que nombra el enunciado (o None)."""
    cand = []
    for m in NORMA_NUM.finditer(q):
        k = NUM.get(m.group(1))
        if k and k in P.boe.IDS: cand.append((m.start(), k))
    for pat, k in TXT:
        m = re.search(pat, q, re.I)
        if m and k in P.boe.IDS: cand.append((m.start(), k))
    return min(cand)[1] if cand else None


def bloque(k, n):
    for tent in (f"Artículo {n}", f"Art. {n}", f"a{n}", f"art{n}"):
        try:
            b = P.bid(k, tent)
            if b in P.boe.ley(k): return b
        except Exception: pass
    return None


import unicodedata
_STOP = set("sobre segun entre desde hasta cuando donde cuales cuanto cuantos mismo misma estos estas puede podra podran deben deberan tiene tienen sera seran estara ambas todos todas otros otras forma efectos efecto caso casos dicha dichos dicho parte partes dentro cuyo cuya cuyos".split())
def _n(s):
    s = unicodedata.normalize("NFKD", s.lower()); s = "".join(c for c in s if not unicodedata.combining(c)); return re.sub(r"[^a-z0-9 ]", " ", s)
def _toks(s): return set(w for w in _n(s).split() if len(w) >= 5 and w not in _STOP)
SOLO_NORMAS = lambda k: not (k in ("ODOC", "RES2014", "RD633") or k.startswith(("STC", "PCP", "GA_", "DRP", "DTC", "HEUR", "GLOS", "STJ", "DECL", "FEDER", "FEMPA", "FSEP", "REF")))


def por_texto(q, citado, bt):
    """Sin «artículo N» en el enunciado: el bloque citado en los apuntes que contiene casi todo lo que dice la respuesta correcta
    (≥ 80 % de sus palabras clave) y buena parte del enunciado, con ventaja clara sobre el segundo y, si el enunciado nombra la norma, de esa norma."""
    to, tq = _toks(q["o"][q["c"]]), _toks(q["q"])
    if len(to) < 4: return None
    k0 = norma(q["q"])
    if any(m.group(1) not in NUM for m in NORMA_NUM.finditer(q["q"])) or (NORMA_NUM.search(q["q"]) and not k0): return None   # norma que no está en boe/
    sc = []
    for (k, b), bs in bt.items():
        if b == "preambulo" or not SOLO_NORMAS(k) or (k0 and k != k0): continue
        so, sq = len(to & bs) / len(to), len(tq & bs) / max(1, len(tq))
        sc.append((so + 0.5 * sq, so, sq, k, b))
    sc.sort(reverse=True)
    if not sc: return None
    b1, b2 = sc[0], (sc[1][0] if len(sc) > 1 else 0)
    if b1[1] >= (0.8 if k0 else 0.9) and b1[2] >= (0.3 if k0 else 0.5) and b1[0] - b2 >= 0.15: return b1[3], b1[4]
    return None


def main(dtxt, dlits):
    lits = {f[:-5]: json.load(open(os.path.join(dlits, f), encoding="utf-8")) for f in os.listdir(dlits) if f.endswith(".json")}
    citado = {}
    for t, L in lits.items():
        for k, b, _ in L: citado.setdefault((k, b), set()).add(t)
    bt = {}
    for (k, b) in citado:
        try: bt[(k, b)] = _toks(" ".join(P.boe.parrafos(k, b)))
        except Exception: pass
    marcas, sin_art, sin_norma, sin_tema, por_t = [], 0, [], [], []
    tot = 0
    for base, cod in EXAMENES.items():
        for q in G.examen(base, dtxt):
            tot += 1
            if q.get("anulada"): continue
            arts = [int(a) for a in ART.findall(q["q"])]
            if not arts:
                sin_art += 1
                r = por_texto(q, citado, bt) if q.get("c") is not None else None
                if r:
                    for t in sorted(citado[r]): marcas.append({"tema": t, "k": r[0], "bloque": r[1], "ex": [[cod, q["n"]]]}); por_t.append((cod, q["n"], r, q["q"][:70]))
                continue
            k = norma(q["q"])
            if not k: sin_norma.append((cod, q["n"], q["q"][:90])); continue
            for a in dict.fromkeys(arts):
                b = bloque(k, a)
                if not b: continue
                ts = sorted(citado.get((k, b), []))
                if not ts: sin_tema.append((cod, q["n"], k, b)); continue
                for t in ts: marcas.append({"tema": t, "k": k, "bloque": b, "ex": [[cod, q["n"]]]})
    print("preguntas", tot, "· sin «artículo N»:", sin_art, "· sin norma reconocida:", len(sin_norma), "· artículo no citado en ningún tema:", len(sin_tema), "· marcas:", len(marcas))
    print("  de ellas, ubicadas por el texto de la respuesta:", len(por_t))
    return marcas, sin_norma, sin_tema, por_t


if __name__ == "__main__":
    marcas, sn, st, pt = main(ARGV[1], ARGV[2])
    if "--aplicar" in ARGV:
        reg = M.cargar(); M.anadir(reg, marcas)
        reg.sort(key=lambda m: (m["tema"], str(m.get("k")), str(m.get("bloque")), str(m.get("clave"))))
        json.dump({"_formato": "marcas_examen_v1", "marcas": reg}, open(M.RUTA, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
        print("registro:", len(reg), "marcas")
