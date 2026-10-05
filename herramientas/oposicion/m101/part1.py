# -*- coding: utf-8 -*-
"""Tema I.1 + I.2 + I.3 (B1T01), FUSIONADO como en la plantilla del plan de estudio y los módulos de la academia (M101):
La CE de 1978 (estructura y contenido; arts. 1 a 55) · Derechos y deberes fundamentales, su garantía y suspensión ·
El Tribunal Constitucional · El Defensor del Pueblo · La reforma de la Constitución.

Prioridades y avisos («IMPORTANTE», «PRESCINDIBLE») tomados de la guía M101 y de la transcripción de su vídeo,
aportadas por el usuario; los títulos de artículo (tabla de la p. 10) son de esa guía, NO de la CE. Todo texto de
norma es LITERAL del BOE consolidado vigente y lo comprueba el generador (lit/c/T.q). Si la guía o la transcripción
discrepan de la norma vigente, prevalece la norma (ver «Avisos» en el mapa).
Normas: CE; LO 2/1979 (LOTC); LO 3/1981 (Defensor del Pueblo); LO 4/1981 (estados de alarma, excepción y sitio);
Reglamentos del Congreso y del Senado; LO 2/1980 (referéndum); LO 3/2007; Reformas de la CE (1992, 2011, 2024, 2026)."""
import os, sys, re, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO.update({"LOEAS": "LO 4/1981", "LODP": "LO 3/1981, del Defensor del Pueblo", "LOTC": "LOTC", "RS": "Reglamento del Senado",
              "LO2_1980": "LO 2/1980, de referéndum", "LO3_2007": "LO 3/2007", "REF1992": "Reforma de 1992", "REF2011": "Reforma de 2011",
              "REF2024": "Reforma de 2024", "REF2026": "Reforma de 2026", "RCD": "Reglamento del Congreso"})
CEJ = json.load(open(os.path.join(RAIZ, "temas", "ce.json"), encoding="utf-8"))
IMP, PRE = "{{IMPORTANTE}}", "{{PRESCINDIBLE}}"
def tag(k, t): return "{{c:%s~%s}}" % (k, t)
def tabla(cab, filas):
    return "\n".join(["| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)] + ["| " + " | ".join(str(x) for x in f) + " |" for f in filas])
def ir(destino, texto): return "{{ir:%s|%s}}" % (destino, texto)
def arts(t):
    out = list(a["n"] for a in t.get("arts", []))
    for cp in t.get("caps", []):
        out += arts(cp)
    for s in t.get("secs", []): out += arts(s)
    return out
def ix(k, b, pre):
    r = [i for i, x in enumerate(boe.parrafos(k, b)) if x.startswith(pre)]
    assert r, (k, b, pre); return r[0]
TIT = {t["id"]: t for t in CEJ["titulos"]}
def rng(l): return f"{l[0]}–{l[-1]}" if len(l) > 1 else str(l[0])
assert sorted(sum((arts(t) for t in CEJ["titulos"]), [])) == list(range(1, 170))
RUB = {a["n"]: a["t"] for t in CEJ["titulos"] for a in [] }
def rubrica(n):
    for t in CEJ["titulos"]:
        stack = [t]
        while stack:
            x = stack.pop()
            for a in x.get("arts", []):
                if a["n"] == n: return a.get("t", "")
            stack += x.get("caps", []) + x.get("secs", [])
    return ""

T = Tema("B1T01",
  "La Constitución de 1978 (estructura y arts. 1 a 55), los derechos y deberes fundamentales con su garantía y suspensión, el Tribunal Constitucional, el Defensor del Pueblo y la reforma de la Constitución. Tema fusionado I.1 + I.2 + I.3 según la plantilla y el módulo M101.",
  ["Constitución Española", "Estructura de la CE", "Arts. 1 a 55", "Garantías", "Suspensión de derechos", "Tribunal Constitucional", "Defensor del Pueblo", "Reforma constitucional", "Módulo M101"])
T.meta["title"] = "La Constitución de 1978 · Derechos y deberes · Tribunal Constitucional"
