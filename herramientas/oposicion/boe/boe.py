# -*- coding: utf-8 -*-
"""Texto consolidado del BOE (API de datos abiertos): {bloque: (título, [párrafos])}.
Se usa la ÚLTIMA versión de cada bloque (la vigente) y se excluyen las notas."""
import xml.etree.ElementTree as ET, re, os
AQUI = os.path.dirname(os.path.abspath(__file__))
import glob as _glob
# ids.txt y, aparte, ids_*.txt (uno por tarea, para no pisarse): clave → BOE-A-… / CELEX:…
IDS = {}
for _f in sorted(_glob.glob(os.path.join(AQUI, "ids*.txt"))):
    for _l in open(_f):
        if _l.strip():
            _k, _v = _l.split()
            assert IDS.get(_k, _v) == _v, ("clave repetida con otro id", _k)
            IDS[_k] = _v
_cache = {}
import datetime
HOY = datetime.date.today().strftime("%Y%m%d")
# Versiones consolidadas publicadas sin fecha de vigencia que aún no rigen (comprobado en su nota del BOE).
NO_VIGENTES = {("RCD", "art23", "BOE-A-2026-16353")}   # reforma del art. 23.1 RCD: entra en vigor en la XVI legislatura


def ley(k):
    if k in _cache: return _cache[k]
    if os.path.exists(os.path.join(AQUI, k + ".json")):
        # Texto de EUR-Lex (Diario Oficial de la UE), extraído con eurext.js: solo el
        # documento principal (no los protocolos ni los anexos).
        import json
        A = json.load(open(os.path.join(AQUI, k + ".json"), encoding="utf-8"))
        out = {}
        for a in A:
            if a["doc"] != A[0]["doc"]: continue
            assert a["art"] not in out, (k, a["art"])
            out[a["art"]] = (a["art"], [("articulo", a["art"])] + [("parrafo", p) for p in a["ps"]])
        _cache[k] = out
        return out
    raiz = ET.parse(os.path.join(AQUI, k + ".xml")).getroot()
    out = {}
    if raiz.find("data") is None and raiz.find("texto") is not None:
        # Disposición sin texto consolidado: XML del diario (texto original publicado).
        # El BOE parte en dos los párrafos que cruzan de página: se unen si el siguiente
        # empieza en minúscula. Los artículos se agrupan por su encabezado «Artículo N.».
        ps = []
        for p in raiz.find("texto").iter("p"):
            t = " ".join("".join(p.itertext()).split())
            if not t: continue
            if ps and t[0].islower() and not re.match(r"^[a-zñ]\) ", t): ps[-1] = ps[-1] + " " + t
            else: ps.append(t)
        actual = "preambulo"; out[actual] = ("", [])
        for t in ps:
            m = re.match(r"^(Artículo \d+)\.", t)
            if m:
                actual = "a" + m.group(1).split()[1]; out[actual] = (m.group(1), [])
            out[actual][1].append(("parrafo", t))
        _cache[k] = out
        return out
    for b in raiz.iter("bloque"):
        vs = b.findall("version")
        if not vs: continue
        # Solo versiones ya vigentes: fuera las de fecha de vigencia futura y las que el BOE
        # publica sin fecha porque entran en vigor más adelante (NO_VIGENTES).
        ok = [x for x in vs if not ((x.get("fecha_vigencia") or "") > HOY or (k, b.get("id"), x.get("id_norma")) in NO_VIGENTES)]
        v = (ok or vs)[-1]
        ps = []
        def ps_de(nodo):
            for h in nodo:
                if h.tag == "blockquote" and (h.get("class") or "") != "sangrado": continue   # notas del BOE (no son texto legal)
                if h.tag == "p": yield h
                else: yield from ps_de(h)
        for p in ps_de(v):
            cl = p.get("class") or ""
            if cl.startswith("nota"): continue
            t = " ".join("".join(p.itertext()).split())
            if t: ps.append((cl, t))
        out[b.get("id")] = (b.get("titulo") or "", ps)
    _cache[k] = out
    return out
def parrafos(k, bid):
    return [t for cl, t in ley(k)[bid][1]]
def buscar(k, frag):
    n = lambda s: " ".join(s.split()).lower()
    return [(bid, tit) for bid, (tit, ps) in ley(k).items() if n(frag) in n(" ".join(t for _, t in ps))]
def bloque(k, titulo):
    """Id del bloque por su título («Artículo 55 bis», «Artículo séptimo»…)."""
    n = lambda s: " ".join(s.replace("\xa0", " ").split()).lower()
    r = [bid for bid, (tit, _) in ley(k).items() if n(tit) == n(titulo)]
    assert len(r) == 1, (k, titulo, r)
    return r[0]
