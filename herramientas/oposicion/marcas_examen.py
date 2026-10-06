# -*- coding: utf-8 -*-
"""Registro de marcas «Examen» (petición del usuario, 6-10-2026).

Una marca por cada artículo o cuestión que resuelve la respuesta correcta de una pregunta de los exámenes oficiales (test y supuestos),
asignada al tema en cuestión AUNQUE ESTÉ APAGADO o aún no tenga el temario de la academia. El registro (`marcas_examen.json`) es
ADITIVO: este script solo añade o completa, nunca borra. `Tema._marcas_examen` (plantilla.py) coloca cada marca al publicar el tema:
las de artículo (`k` + `bloque`) donde esté citado literalmente ese artículo; las de teoría (`clave`) en la unidad (`### N.M título`,
regex) o el apartado (`sec:<id>`) que corresponda. Al regenerar un tema con el temario de la academia las marcas no se pierden: se recolocan
solas, y si el artículo ya no está citado, queda pendiente en el registro.

Uso:  python3 marcas_examen.py            (añade lo nuevo de leyes25L/P/X, tests_reales.json y marcas_examen_manuales.py)
      python3 marcas_examen.py --lits DIR  (con volcados NIBLO_LITS de cada tema: asigna tema a las preguntas sin tema por su texto)
"""
import os, sys, json, importlib
ARGV = sys.argv[:]   # plantilla.py recorta sys.argv
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [AQUI, os.path.join(AQUI, "boe")]
RUTA = os.path.join(AQUI, "marcas_examen.json")
import plantilla as P   # P.bid(k, b): identificador canónico del bloque (el mismo que registra lit())
ROM = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6}


# Preguntas sin `tema` en tests_reales.json: tema al que se asigna la marca (por dónde se estudia esa norma). Las que no están aquí siguen
# en SIN_TEMA y se informan al usuario: ET a48/a49 (permisos del Estatuto de los Trabajadores, P24 y X47) y RD 126/2026 (SMI, P25).
ASIGNA = {("CE", "a139"): "B1T10", ("CE", "a9"): "B1T01", ("L22_2009", "preambulo"): "B1T10", ("L39", "a133"): "B4T03", ("L40", "a9"): "B1T08",
          ("LGP", "a43"): "B6T02", ("LO6_2013", "a17"): "B6T01", ("RD1051", "anii"): "B3T09", ("RDL6", "a1-22"): "B5T03",
          ("RES2014", "ai-2"): "B6T06", ("RES2014", "ai-4"): "B6T06", ("TFUE", "Artículo 3"): "B2T01", ("TREBEP", "a48"): "B5T02",
          ("TREBEP", "a49"): "B5T02", ("TUE", "Artículo 5"): "B2T01", ("CE", "a124"): "B1T07"}


# Marcas de test que se colocan mejor por apartado (clave en marcas_examen_manuales.py): el artículo no se cita literal en ese tema.
DESCARTA = {("B1T03", "CE", "a162"), ("B1T01", "CE", "tviii")}


def tema_id(cod):
    if not cod: return None
    b, n = cod.split("."); return f"B{ROM[b]}T{int(n):02d}"


def cargar():
    return json.load(open(RUTA, encoding="utf-8"))["marcas"] if os.path.exists(RUTA) else []


def clave(m): return (m["tema"], m.get("k"), m.get("bloque"), m.get("clave"))


def anadir(marcas, nuevas):
    """Fusiona sin borrar nada: mismas marcas → se unen las preguntas (`ex`) y se conserva la nota."""
    idx = {clave(m): m for m in marcas}
    for n in nuevas:
        m = idx.get(clave(n))
        if m is None: marcas.append(n); idx[clave(n)] = n; continue
        for e in n["ex"]:
            if e not in m["ex"]: m["ex"].append(e)
        if n.get("nota") and not m.get("nota"): m["nota"] = n["nota"]
    return marcas


def _bloques_ley(q):
    """(norma, bloque canónico) de cada bloque de texto legal (`ley`) de la pregunta, leído del título «Norma · artículo N»."""
    import re
    rev = {}
    for k, v in P.boe.IDS.items(): rev.setdefault(v, []).append(k)
    out, sin = [], []
    for b in q.get("ley") or []:
        m = re.search(r"·\s*(.+)$", b["t"]); tit = m.group(1) if m else b["t"]
        cand = re.match(r"(?i)(art[ií]culo|t[ií]tulo|disposici[oó]n|anexo)\s+([^\s,.;()]+)", tit)
        res = None
        for k in rev.get(b["f"], []):
            for tent in ([cand.group(1).capitalize() + " " + cand.group(2)] if cand else []) + [tit]:
                try:
                    r = P.bid(k, tent)
                    if r in P.boe.ley(k): res = (k, r); break
                except Exception: pass
            if res: break
        (out if res else sin).append(res or (b["f"], tit))
    return out, sin


def del_test(lits=None):
    """Marcas de las preguntas de test: (tema, norma, bloque) de la respuesta, con la pregunta que lo cita."""
    t = json.load(open(os.path.join(AQUI, "tests_reales.json"), encoding="utf-8"))
    leyes = {c: importlib.import_module("leyes25" + c).LEY for c in "LPX"}
    out, sin_bloque = [], []
    for e in t["examenes"]:
        c = e["id"][5]
        for q in e["preguntas"]:
            n = int(q["n"])
            if q.get("anulada"): continue
            bl, sin = _bloques_ley(q)
            for (k, bloque, *_r) in leyes[c].get(n, []):
                x = (k, P.bid(k, bloque))
                if x not in bl: bl.append(x)
            if not bl: sin_bloque.append((c, n, q.get("tema"), sin))
            for (k, bloque) in bl:
                tid = tema_id(q.get("tema"))
                if tid is None and lits:
                    tids = sorted(tt for tt, L in lits.items() if any(a == k and b == bloque for a, b, _ in L))
                    tid = tids[0] if len(tids) == 1 else None
                if tid is None: tid = ASIGNA.get((k, bloque), "SIN_TEMA")
                if (tid, k, bloque) in DESCARTA: continue
                out.append({"tema": tid, "k": k, "bloque": bloque, "ex": [[c, n]]})
    if os.environ.get("NIBLO_VER_SIN"): print("sin bloque resuelto:", sin_bloque)
    return out


def main():
    lits = None
    if "--lits" in ARGV:
        d = ARGV[ARGV.index("--lits") + 1]
        lits = {f[:-5]: json.load(open(os.path.join(d, f), encoding="utf-8")) for f in os.listdir(d) if f.endswith(".json")}
    marcas = cargar()
    anadir(marcas, del_test(lits))
    try:
        import marcas_examen_manuales as MM
        anadir(marcas, MM.MARCAS)
    except ImportError: pass
    marcas.sort(key=lambda m: (m["tema"], str(m.get("k")), str(m.get("bloque")), str(m.get("clave"))))
    json.dump({"_formato": "marcas_examen_v1", "marcas": marcas}, open(RUTA, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    por = {}
    for m in marcas: por[m["tema"]] = por.get(m["tema"], 0) + 1
    print(len(marcas), "marcas;", len(por), "temas;", "sin tema:", por.get("SIN_TEMA", 0))


if __name__ == "__main__": main()
