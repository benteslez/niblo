# -*- coding: utf-8 -*-
"""Lectura estricta de un cuestionario oficial (pdftotext -layout) y de su
plantilla DEFINITIVA, con una segunda transcripción independiente hecha sobre la
IMAGEN de la plantilla. Misma lógica que examen25L.py, para cualquier examen."""
import re, sys


def leer(ruta_ex, ruta_pl, pie, vista, cabecera_pl):
    TXT = open(ruta_ex, encoding="utf-8").read().replace("\f", "\n")
    PIE = re.compile(pie)
    lineas = [l for l in TXT.split("\n") if not PIE.match(l)]
    qs, cur, op, reserva, avisos = [], None, None, False, []
    esperado = 1
    for l in lineas:
        if l.strip() == "Preguntas de reserva":
            reserva, esperado = True, 1
            continue
        m = re.match(r"^(\d{1,3})\.\s+(.*)$", l)
        o = re.match(r"^\s+([a-d])\)\s+(.*)$", l)
        if m and int(m.group(1)) == esperado:
            cur = {"n": (100 if reserva else 0) + esperado, "reserva": reserva, "q": m.group(2).strip(), "o": {}, "orden": []}
            qs.append(cur); esperado += 1; op = None
        elif o and cur is not None:
            op = o.group(1)
            if op in cur["o"]:
                avisos.append(("OPCIÓN REPETIDA", cur["n"], op))
            cur["o"][op] = o.group(2).strip(); cur["orden"].append(op)
        elif l.strip() and cur is not None:
            t = l.strip()
            destino = (cur["o"], op) if op else (cur, "q")
            prev = destino[0][destino[1]]
            if prev.endswith("-") and not prev.endswith(" -"):
                avisos.append(("GUION AL FINAL DE LÍNEA", cur["n"], prev[-30:] + " | " + t[:30]))
            sep = "" if (prev.endswith("-") and not prev.endswith(" -")) else " "
            destino[0][destino[1]] = prev + sep + t
    limpio = lambda s: re.sub(r"\s+", " ", s).strip()
    for q in qs:
        q["q"] = limpio(q["q"]); q["o"] = {k: limpio(v) for k, v in q["o"].items()}
        if q["orden"] != list("abcd"):
            avisos.append(("OPCIONES NO a-d", q["n"], q["orden"]))
    assert len(qs) == 105 and [q["n"] for q in qs] == list(range(1, 106)), len(qs)
    PL = open(ruta_pl, encoding="utf-8").read()
    assert cabecera_pl in " ".join(PL.split()), "cabecera de la plantilla"
    izq, res = PL.split("Preguntas de reserva")
    plant = {int(n): r for n, r in re.findall(r"(\d{1,3})\.\s+([a-d]|ANULADA)\b", izq)}
    plant.update({100 + int(n): r for n, r in re.findall(r"(\d)\.\s+([a-d])\b", res)})
    assert sorted(plant) == list(range(1, 106)), sorted(set(range(1, 106)) - set(plant))
    assert len(vista) == 105
    for n in range(1, 106):
        v = vista[n - 1]; t = plant[n]
        assert (v == "X" and t == "ANULADA") or v == t, ("PLANTILLA: texto e imagen no coinciden", n, t, v)
    print(ruta_pl, ": texto e imagen coinciden en las 105", file=sys.stderr)
    for q in qs:
        r = plant[q["n"]]
        q["anulada"] = r == "ANULADA"
        q["c"] = None if q["anulada"] else "abcd".index(r)
    for a in avisos:
        print("AVISO", ruta_ex, a, file=sys.stderr)
    return qs, plant, avisos
