# -*- coding: utf-8 -*-
"""Preguntas de los exámenes anteriores a 2025 que cita alguna marca «Examen» → temas/examenes_previos.json
(el diálogo de la pill «Examen» las lee al pulsarla; las de 2025 salen de `tests-reales` en oposicion.html).
Texto literal del cuestionario y respuesta de la plantilla (gace_historico.py). Solo las preguntas citadas por el registro.
Uso:  python3 previos_datos.py DIR_TXT     (tras añadir marcas con gace_marcas.py)"""
import os, sys, json
ARGV = sys.argv[:]
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [AQUI, os.path.join(AQUI, "boe")]
import gace_historico as G
from gace_marcas import EXAMENES

TITULOS = {"L24": "GACE-L 2024", "P24": "GACE-P 2024", "L22": "GACE-L 2022", "P22": "GACE-P 2022", "ST22": "GACE-E 2022",
           "L19": "GACE-L 2019", "P19": "GACE-P 2019", "ST19": "GACE-E 2019", "STX19": "GACE-E 2019 extraordinario",
           "L13": "GACE-L 2013", "P13": "GACE-P 2013", "L11": "GACE-L 2011", "P11": "GACE-P 2011", "L08": "GACE-L 2008", "P08": "GACE-P 2008"}

def main(dtxt):
    reg = json.load(open(os.path.join(AQUI, "marcas_examen.json"), encoding="utf-8"))["marcas"]
    citadas = {}
    for m in reg:
        for e in m["ex"]:
            if not isinstance(e, str) and e[0] in TITULOS: citadas.setdefault(e[0], set()).add(int(e[1]))
    out = {"_formato": "examenes_previos_v1", "examenes": {}}
    for base, cod in EXAMENES.items():
        if cod not in citadas: continue
        qs = {q["n"]: q for q in G.examen(base, dtxt)}
        pre = {}
        for n in sorted(citadas[cod]):
            q = qs.get(n)
            if not q or not q["o"]: print("FALTA", cod, n); continue
            pre[str(n)] = {"q": q["q"], "o": q["o"], "c": q["c"], "anulada": bool(q.get("anulada"))} if q.get("c") is not None or q.get("anulada") else {"q": q["q"], "o": q["o"], "c": None}
        out["examenes"][cod] = {"titulo": TITULOS[cod] + " · 1.er ejercicio", "preguntas": pre}
    import previos_supuestos as PS
    out["supuestos"] = PS.todo(dtxt)
    ruta = os.path.join(AQUI, "..", "..", "temas", "examenes_previos.json")
    json.dump(out, open(ruta, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    print({c: len(v["preguntas"]) for c, v in out["examenes"].items()}, os.path.getsize(ruta), "bytes")

if __name__ == "__main__": main(ARGV[1])
