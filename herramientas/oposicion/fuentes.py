# -*- coding: utf-8 -*-
"""Fuentes literales comunes (módulo).
El texto de la norma se extrae por programa de los PDF consolidados del BOE
(literal.py) y se comprueba palabra a palabra. Cada pregunta del test lleva el
fragmento literal en que se basa y se verifica que existe en el artículo."""
import json, sys, re
from literal import articulos

SRC = {
    "CE":  articulos("BOE-A-1978-31229.txt"),
    "LO4": articulos("BOE-A-1981-12774.txt"),
    "LO3": articulos("BOE-A-1981-10325.txt"),
    "LOTC": articulos("BOE-A-1979-23709.txt"),
    "LJCA": articulos("BOE-A-1998-16718.txt"),
    "HC":  articulos("BOE-A-1984-11620.txt"),
    "L36": articulos("BOE-A-1985-23210.txt"),
}
import lecrim as _lecrim
SRC["LEC"] = _lecrim.articulos("lecrim.txt")[0]
NOMBRE = {"CE": "CE", "LO4": "LO 4/1981", "LO3": "LO 3/1981", "LOTC": "LOTC", "LJCA": "LJCA", "HC": "LO 6/1984", "L36": "Ley 36/1985", "LEC": "LECrim"}
# Fórmula de promulgación al final de la última disposición: no es texto normativo.
# Y encabezados de sección que el extractor pega al artículo anterior.
for _f in SRC.values():
    for _k, _ps in _f.items():
        _i = next((i for i, x in enumerate(_ps) if x.startswith("Por tanto")), None)
        if _i is not None:
            del _ps[_i:]
        _ps[:] = [x for x in _ps if not re.match(r"^Sección \d+\.ª ", x)]

def art(f, n):
    """Clave del artículo: n puede ser número (CE) o 'primero', 'dos'… (LO)."""
    k = f"Artículo {n}."
    if k not in SRC[f]:
        k = next((x for x in SRC[f] if x.startswith(str(n))), None)
    assert k in SRC[f], (f, n)
    return k

def texto(f, n):
    return " ".join(SRC[f][art(f, n)])

def lit(f, n, resaltar=(), solo=None, titulo=None):
    """Bloque de texto literal. resaltar: fragmentos LITERALES que se ponen en
    negrita (se comprueba que existen). solo: índices de párrafos a mostrar."""
    k = art(f, n)
    ps = SRC[f][k]
    if solo is not None:
        ps = [ps[i] for i in solo]
    out = []
    usados = set()
    for p in ps:
        for r in resaltar:
            if r in p and r not in usados:
                p = p.replace(r, "**" + r + "**", 1); usados.add(r)
        out.append(p)
    falta = [r for r in resaltar if r not in usados]
    assert not falta, (f, n, falta)
    cab = titulo or (k + (" (" + NOMBRE[f] + ")" if f != "CE" else ""))
    return "\n".join(["> **" + cab + "**"] + ["> " + p for p in out])

def bloque(*partes):
    return "\n\n".join(p.strip("\n") for p in partes if p)


def _n(s): return " ".join(s.split())

def c(f, n, frag):
    """Cita literal en línea: comprueba que el fragmento existe en el artículo
    y lo devuelve entre comillas latinas. Admite «…» para unir dos trozos."""
    t = _n(texto(f, n))
    for parte in frag.split("…"):
        p = _n(parte.replace("**", "")).strip()
        if p:
            assert p in t, ("CITA NO LITERAL", f, n, p)
    return "«" + frag + "»"

S = []
def ap(id, title, body, nivel=1):
    S.append({"id": id, "title": title, "body": body.strip("\n"), "nivel": nivel})
