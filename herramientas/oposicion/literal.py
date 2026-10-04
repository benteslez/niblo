# -*- coding: utf-8 -*-
"""Extrae artículos LITERALES de los PDF consolidados del BOE (salida de
pdftotext -layout). Reconstruye los párrafos como en el BOE: un párrafo
empieza en una línea sangrada y sigue en las líneas sin sangría."""
import re, unicodedata

RUIDO = re.compile(r"^\f?\s*(Página \d+|BOLETÍN OFICIAL DEL ESTADO|LEGISLACIÓN CONSOLIDADA)\s*$")

def cargar(ruta):
    lineas = []
    for l in open(ruta, encoding="utf-8").read().split("\n"):
        l = l.replace("\f", "")
        if not l.strip() or RUIDO.match(l):
            continue
        lineas.append(l.rstrip())
    return lineas

def _texto_consolidado(lineas):
    """Solo el texto (tras «TEXTO CONSOLIDADO»), sin el índice."""
    for i, l in enumerate(lineas):
        if l.strip() == "TEXTO CONSOLIDADO":
            return lineas[i + 1:]
    return lineas

RUBRICAS = {}

def articulos(ruta):
    """{nombre_articulo: [párrafos]} en orden. Nombre tal como aparece:
    'Artículo 116.', 'Artículo primero.', 'Disposición final única. …'."""
    lineas = _texto_consolidado(cargar(ruta))
    cab = re.compile(r"^(Artículo [0-9a-záéíóúñ ]+\.|Disposici[oó]n [^.]+\..*)$")
    # Algunas leyes llevan la rúbrica en la misma línea: «Artículo primero. Prerrogativas y garantías.»
    cab_rub = re.compile(r"^(Artículo [0-9a-záéíóúñ ]+\.) ([A-ZÁÉÍÓÚ].*)$")
    out, actual, parrafos = {}, None, []
    def cerrar():
        if actual: out[actual] = parrafos[:]
    for l in lineas:
        sangria = len(l) - len(l.lstrip())
        t = l.strip()
        if sangria == 0 and cab.match(t):
            cerrar(); actual, parrafos = t, []; continue
        m = cab_rub.match(t) if sangria == 0 else None
        if m:
            cerrar(); actual, parrafos = m.group(1), []; RUBRICAS[(ruta, actual)] = m.group(2); continue
        if actual is None:
            continue
        # Encabezados centrados (TÍTULO, CAPÍTULO, Sección…) cierran el artículo.
        if sangria >= 12:
            cerrar(); actual, parrafos = None, []; continue
        if sangria >= 3 or not parrafos:
            parrafos.append(t)
        else:
            sep = "" if parrafos[-1].endswith("-") else " "
            parrafos[-1] = parrafos[-1] + sep + t
    cerrar()
    return out

def palabras(txt):
    return re.findall(r"[0-9A-Za-zÀ-ÿ]+", txt)
