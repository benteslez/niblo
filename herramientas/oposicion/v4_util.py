# -*- coding: utf-8 -*-
"""Plantilla fija de los apuntes (v4): ley primero + ficha.

Cada artículo (o grupo de artículos de una ley de desarrollo) se presenta así:
    ### n.m Título (art. X)
    > texto literal del BOE (lit)
    => ficha con casillas fijas, siempre en el mismo orden

Ficha de DERECHO:      Titulares · Contenido · Límites · Protección · ⚠ Ojo en el examen
Ficha de INSTITUCIÓN o
PROCEDIMIENTO:         Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen

Una casilla puede ser un texto o una lista; si la lista empieza por "::texto",
ese texto va en la fila y el resto como puntos. Las casillas vacías llevan «—»."""
from fuentes import *

OJO = "⚠ Ojo en el examen"

def _fila(k, v):
    if v is None or v == "":
        v = "—"
    if isinstance(v, (list, tuple)):
        v = list(v)
        cab = v.pop(0)[2:] if v and v[0].startswith("::") else ""
        return [f"=> {k}: {cab}"] + [f"=> - {x}" for x in v]
    return [f"=> {k}: {v}"]

def _ficha(pares):
    out = []
    for k, v in pares:
        out += _fila(k, v)
    for l in out:
        if not l.startswith("=> - "):
            assert l[3:].split(":", 1)[0] in dict(pares), l
    return "\n".join(out)

def ficha(titulares, contenido, limites, proteccion, ojo):
    return _ficha([("Titulares", titulares), ("Contenido", contenido), ("Límites", limites),
                   ("Protección", proteccion), (OJO, ojo)])

def fichab(que, quien, como, plazos, ojo):
    return _ficha([("Qué", que), ("Quién", quien), ("Cómo", como),
                   ("Plazos y mayorías", plazos), (OJO, ojo)])

def unidad(cab, *partes):
    """### cabecera + bloques literales + ficha (en ese orden)."""
    return "### " + cab + "\n\n" + "\n\n".join(p.strip("\n") for p in partes if p)

def guia(*lineas):
    return "\n".join("@> " + l for l in lineas)

def donde(texto, puntos):
    return guia("**▸ Dónde estamos.** " + texto, "**▸ Qué vas a ver.** " + " · ".join(puntos))

def resumen(lineas, siguiente):
    return guia("**▸ En resumen.**", *["• " + l for l in lineas], "**→ " + siguiente + "**")

# Protección: textos fijos según la ubicación (se explican en II.1)
P_S1 = "Máxima (Sección 1.ª): ley orgánica, preferente y sumario, amparo y reforma agravada (→ II.1)"
P_14 = "Casi máxima (art. 14): preferente y sumario y amparo, pero reforma ordinaria (→ II.1)"
P_S2 = "Intermedia (Sección 2.ª): vinculación, reserva de ley con contenido esencial y recurso de inconstitucionalidad; sin amparo (→ II.1)"
P_C3 = "Mínima (Capítulo tercero): informa la legislación, la práctica judicial y la actuación pública; ante los jueces, según su ley de desarrollo (→ II.1)"
P_C1 = "Fuera del Capítulo segundo: el art. 53 no lo menciona"
NO_SUSP = "Suspendible: **no** (no figura en el art. 55)"

# ---------------------------------------------------------------------------
# Preguntas de examen real: enunciado y opciones LITERALES del cuestionario,
# respuesta de la plantilla oficial y explicación opción por opción.
import re as _re
def _cuestionario(ruta="Cuestionario_GACE-L_1ej.txt"):
    qs, cur, op = {}, None, None
    for l in open(ruta, encoding="utf-8").read().replace("\f", "\n").split("\n"):
        if _re.match(r"^\s*2025 - GACE-L\s+Página \d+ de \d+\s*$", l):
            continue   # pie de página
        m = _re.match(r"^(\d{1,3})\.\s+(.*)$", l)
        o = _re.match(r"^\s+([a-d])\)\s+(.*)$", l)
        if m and int(m.group(1)) == len(qs) + 1:   # solo el número siguiente: evita listas internas
            cur = {"q": m.group(2).strip(), "o": {}}; qs[int(m.group(1))] = cur; op = None
        elif o and cur is not None:
            op = o.group(1); cur["o"][op] = o.group(2).strip()
        elif l.strip() and cur is not None:
            if op: cur["o"][op] += " " + l.strip()
            else: cur["q"] += " " + l.strip()
    return qs
def _plantilla(ruta="plantilla.txt"):
    return {int(n): r for n, r in _re.findall(r"(\d{1,3})\.\s+([a-d])\b", open(ruta, encoding="utf-8").read())}
CUEST = _cuestionario()
# Plantilla DEFINITIVA, ya verificada (texto e imagen) en examen25L.py: 1-100 y reserva 101-105.
from examen25L import plant as _pl_def
PLANT = {n: r for n, r in _pl_def.items() if r != "ANULADA"}
PORQUE = {}
# Examen EXTRAORDINARIO (GACE-L 2025): cuestionario y plantilla DEFINITIVA, ya verificada
# (texto e imagen) en examen25X.py. Sus preguntas se identifican como ("X", n).
from examen25X import qs as _qs_x
CUEST_X = {q["n"]: {"q": q["q"], "o": q["o"]} for q in _qs_x}
PLANT_X = {q["n"]: "abcd"[q["c"]] for q in _qs_x if not q["anulada"]}
CONV_X = "GACE-L 2025 extraordinario · 1.er ejercicio"
_CE_PLANO = " ".join(open("ce.txt", encoding="utf-8").read().split())

def rub(division, frag):
    """Rúbrica literal de la CE: se comprueba «división + rúbrica» en el texto
    (p. ej. «CAPÍTULO SEGUNDO» + «Derechos y libertades») y se muestra la rúbrica."""
    assert " ".join((division + " " + frag).split()) in _CE_PLANO, ("RÚBRICA NO LITERAL", division, frag)
    return "«" + frag + "»"

def _plano(f, n):
    """Texto de la fuente donde se busca el apoyo: un artículo (f, n) o la CE entera
    (f == "CE*", para rúbricas de títulos, capítulos y secciones)."""
    return _CE_PLANO if f == "CE*" else " ".join(texto(f, n).split())

def examen(n, porque, apoyo, conv="GACE-L 2025 · 1.er ejercicio", cod="L"):
    """Pregunta real n, interactiva en los apuntes.
    porque: {letra: explicación}, una por opción.
    apoyo: COHERENCIA PLANTILLA ↔ LEY. Lista de (dato, fuente, artículo, fragmento):
      · el fragmento tiene que estar literal en la norma;
      · el dato tiene que estar en la opción que da por buena la plantilla;
      · ningún distractor puede contener todos los datos.
    Si algo falla, el generador se detiene: o la plantilla no casa con la ley
    (posible error de la plantilla → avisar) o falta la fuente."""
    if cod == "X":
        q = CUEST_X[n]; ok = PLANT_X[n]; PORQUE[("X", n)] = dict(porque); conv = CONV_X
    else:
        q = CUEST[n]; ok = PLANT[n]; PORQUE[n] = dict(porque)
    assert sorted(q["o"]) == list("abcd") and sorted(porque) == list("abcd"), n
    assert apoyo, ("SIN APOYO LEGAL PARA LA RESPUESTA DE LA PLANTILLA", n)
    norm = lambda x: " ".join(x.lower().split())
    for dato, f, art_, frag in apoyo:
        assert norm(frag) in norm(_plano(f, art_)), ("APOYO NO LITERAL", n, f, art_, frag)
        assert norm(dato) in norm(q["o"][ok]), ("LA PLANTILLA NO CASA CON LA LEY", n, ok, dato)
    for k in "abcd":
        if k != ok:
            assert not all(norm(d) in norm(q["o"][k]) for d, *_ in apoyo), ("DISTRACTOR IGUAL DE APOYADO", n, k)
    assert all("||" not in x for x in list(q["o"].values()) + list(porque.values())), n
    lin = [f"**📋 Pregunta real · {conv} · n.º {n}**", "«" + q["q"] + "»"]
    for k in "abcd":
        lin.append(f"[{'x' if k == ok else ' '}] {k}) {q['o'][k]} || {porque[k]}")
    lin.append(f"= **Respuesta correcta: {ok})**, según la plantilla definitiva de respuestas, y coherente con el texto legal citado.")
    return "\n".join("%> " + x for x in lin)
