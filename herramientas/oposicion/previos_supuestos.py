# -*- coding: utf-8 -*-
"""Texto de las cuestiones del 2.º ejercicio (enunciado literal de los PDF) → se añade a temas/examenes_previos.json (`supuestos`).
Las lee el diálogo de la pill «Examen» (refs `SP.<conv>.<I|II|P>.<n>`). Solo hay enunciado: el 2.º ejercicio no tiene plantilla oficial."""
import re, os

FUENTES = {  # clave → (txt, título, sin cabecera «Cuestión N» → numeración «N.-»)
    "L25": ("2025-02L", "GACE-L 2025 · 2.º ejercicio"),
    "LP24": ("2024-02L", "GACE-L y GACE-P 2024 · 2.º ejercicio"),
    "X24": ("2024-02X", "GACE-L extraordinario 2024 · 2.º ejercicio"),
    "LP22": ("2022-02L", "GACE-L y GACE-P 2022 · 2.º ejercicio"),
    "X22": ("2022-02X", "GACE-L extraordinario 2022 · 2.º ejercicio"),
    "L19": ("2019-02L", "GACE-L 2019 · 2.º ejercicio"),
}
RUIDO = re.compile(r"^\s*(Página \d+ de \d+|\d{4}\s*[–-]?\s*GACE[\w\- ]*|GACE\s*[–-]\s*\w+ 2EJ.*|\d{1,2})\s*$")

def _limpia(lineas): return "\n".join(l.rstrip() for l in lineas if not RUIDO.match(l)).strip()

def _trozos(lineas, pat):
    """Cortes en las líneas que cumplen `pat` (grupo 1 = n.º esperado, en orden 1, 2, 3…)."""
    out, esp, ini = {}, 1, None
    for i, l in enumerate(lineas):
        m = pat.match(l)
        if m and int(m.group(1)) == esp:
            if ini is not None: out[esp - 1] = lineas[ini[1]:i]
            ini = (esp, i); esp += 1
    if ini is not None: out[esp - 1] = lineas[ini[1]:]
    return out

def extrae(txt, clave):
    L = txt.split("\n")
    sup = [i for i, l in enumerate(L) if re.match(r"\s*SUPUESTO PR[ÁA]CTICO (I{1,2})\s*$", l)]
    res = {}
    if clave == "L19":   # primera parte: «Pregunta N.»
        a = [i for i, l in enumerate(L) if re.match(r"\s*Primera parte", l)]
        fin = sup[0] if sup else len(L)
        if a: res["P"] = {str(n): _limpia(t) for n, t in _trozos(L[a[0]:fin], re.compile(r"\s*Pregunta (\d+)\.")).items()}
    for k, ini in enumerate(sup):
        nombre = re.match(r"\s*SUPUESTO PR[ÁA]CTICO (I{1,2})", L[ini]).group(1)
        bloque = L[ini + 1: sup[k + 1] if k + 1 < len(sup) else len(L)]
        pat = re.compile(r"\s*Cuesti[oó]n (\d+)\b") if any(re.match(r"\s*Cuesti[oó]n \d+\b", l) for l in bloque) else re.compile(r"\s*(\d)\s*\.(?:-|\s|$)")
        res[nombre] = {str(n): _limpia(t) for n, t in _trozos(bloque, pat).items()}
    return res

def todo(dtxt):
    out = {}
    for clave, (base, titulo) in FUENTES.items():
        d = extrae(open(os.path.join(dtxt, base + ".txt"), encoding="utf-8").read(), clave)
        out[clave] = dict(d, titulo=titulo)
    return out

if __name__ == "__main__":
    import sys
    for c, d in todo(sys.argv[1]).items():
        print("====", c, {k: sorted(v) for k, v in d.items() if k != "titulo"})
