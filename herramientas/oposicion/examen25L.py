# -*- coding: utf-8 -*-
"""Examen GACE-L 2025, primer ejercicio: cuestionario y plantilla DEFINITIVA.
Extracción literal (pdftotext -layout) con comprobaciones estrictas."""
import re, json, sys
TXT = open("ex25L.txt", encoding="utf-8").read().replace("\f", "\n")
PIE = re.compile(r"^\s*2025 - GACE-L\s+Página \d+ de \d+\s*$")
lineas = [l for l in TXT.split("\n") if not PIE.match(l)]
qs, cur, op, reserva, avisos = [], None, None, False, []
esperado = 1
for l in lineas:
    if l.strip() == "Preguntas de reserva":
        reserva, esperado = True, 1; continue
    m = re.match(r"^(\d{1,3})\.\s+(.*)$", l)
    o = re.match(r"^\s+([a-d])\)\s+(.*)$", l)
    if m and int(m.group(1)) == esperado:
        cur = {"n": (100 if reserva else 0) + esperado, "reserva": reserva, "q": m.group(2).strip(), "o": {}, "orden": []}
        qs.append(cur); esperado += 1; op = None
    elif o and cur is not None:
        op = o.group(1)
        if op in cur["o"]: avisos.append(("OPCIÓN REPETIDA", cur["n"], op))
        cur["o"][op] = o.group(2).strip(); cur["orden"].append(op)
    elif l.strip() and cur is not None:
        t = l.strip()
        destino = (cur["o"], op) if op else (cur, "q")
        prev = destino[0][destino[1]]
        if prev.endswith("-") and not prev.endswith(" -"):
            avisos.append(("GUION AL FINAL DE LÍNEA", cur["n"], prev[-30:] + " | " + t[:30]))
        # Palabra compuesta partida tras su guion («Contencioso-|administrativa»): se une sin espacio.
        sep = "" if (prev.endswith("-") and not prev.endswith(" -")) else " "
        destino[0][destino[1]] = prev + sep + t
def limpio(s): return re.sub(r"\s+", " ", s).strip()
for q in qs:
    q["q"] = limpio(q["q"]); q["o"] = {k: limpio(v) for k, v in q["o"].items()}
    if q["orden"] != list("abcd"): avisos.append(("OPCIONES NO a-d", q["n"], q["orden"]))
assert len(qs) == 105, len(qs)
assert [q["n"] for q in qs] == list(range(1, 106))
# Plantilla definitiva (texto)
PL = open("pl25L.txt", encoding="utf-8").read()
assert "PLANTILLA DEFINITIVA" in PL
izq, res = PL.split("Preguntas de reserva")
plant = {int(n): r for n, r in re.findall(r"(\d{1,3})\.\s+([a-d]|ANULADA)\b", izq)}
plant.update({100 + int(n): r for n, r in re.findall(r"(\d)\.\s+([a-d])\b", res)})
assert sorted(plant) == list(range(1, 106)), sorted(set(range(1, 106)) - set(plant))
# Segunda fuente, independiente: transcrita a mano de la IMAGEN de la plantilla
# (filas de diez: 1-10, 11-20, … ; X = ANULADA; después las 5 de reserva).
VISTA = ("acacdbadcb" "aacacdabca" "cadbccdcad" "dbdcacadad" "bdabbdccab"
         "cbbddccccc" "acadcbcbba" "acbbbbcdbb" "aXcccccaaa" "acacdadacc" "bacdb")
assert len(VISTA) == 105
for n in range(1, 106):
    v = VISTA[n - 1]; t = plant[n]
    assert (v == "X" and t == "ANULADA") or v == t, ("PLANTILLA: texto e imagen no coinciden", n, t, v)
print("plantilla: texto e imagen coinciden en las 105", file=sys.stderr)
for q in qs:
    r = plant[q["n"]]
    q["anulada"] = r == "ANULADA"
    q["c"] = None if q["anulada"] else "abcd".index(r)
for a in avisos: print("AVISO", a, file=sys.stderr)
if __name__ == "__main__":
    json.dump(qs, open("q25L.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(qs), "preguntas;", sum(q["anulada"] for q in qs), "anuladas;", sum(q["reserva"] for q in qs), "de reserva", file=sys.stderr)
