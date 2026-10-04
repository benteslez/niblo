# -*- coding: utf-8 -*-
"""Coherencia plantilla DEFINITIVA ↔ texto legal, en las preguntas cuya norma
está en las fuentes literales del proyecto (BOE). Para cada una: el dato
decisivo tiene que estar LITERAL en el artículo y en la opción que da por
buena la plantilla, y ningún distractor puede contener todos los datos."""
import json, sys
sys.argv = [sys.argv[0]]
import fuentes
from examen25L import qs, plant
CE = " ".join(open("ce.txt", encoding="utf-8").read().split())
norm = lambda x: " ".join(x.lower().replace("«", "").replace("»", "").split())
def plano(f, n): return CE if f == "CE*" else " ".join(fuentes.texto(f, n).split())
APOYO = {
  1:  [("De los derechos y deberes fundamentales", "CE*", None, "TÍTULO I De los derechos y deberes fundamentales")],
  2:  [("plazo máximo de un mes", "LO3", "segundo", "en el plazo máximo de un mes"),
       ("mayoría absoluta en el Senado", "LO3", "segundo", "al alcanzarse la mayoría absoluta del Senado")],
  3:  [("4 el Congreso", "CE", 159, "cuatro a propuesta del Congreso"), ("2 el Gobierno", "CE", 159, "dos a propuesta del Gobierno"),
       ("2 el Consejo General del Poder Judicial", "CE", 159, "dos a propuesta del Consejo General del Poder Judicial")],
  4:  [("representantes designados por los grupos políticos con representación parlamentaria", "CE", 99, "representantes designados por los Grupos políticos con representación parlamentaria")],
  5:  [("Ejercer el derecho de gracia con arreglo a la ley", "CE", 62, "Ejercer el derecho de gracia con arreglo a la ley"),
       ("no podrá autorizar indultos generales".replace("no podrá", "sin que esta pueda"), "CE", 62, "que no podrá autorizar indultos generales")],
  6:  [("funcionamiento regular de las instituciones", "CE", 56, "arbitra y modera el funcionamiento regular de las instituciones")],
  7:  [("ley orgánica", "CE", 75, "leyes orgánicas y de bases")],
  9:  [("a propuesta del Gobierno, oído el Consejo General del Poder Judicial", "CE", 124, "a propuesta del Gobierno, oído el Consejo General del Poder Judicial")],
  13: [("Marina mercante", "CE", 149, "Marina mercante")],
  14: [("prohíbe", "CE", 145, "En ningún caso se admitirá la federación de Comunidades Autónomas")],
  15: [("Cabildos o Consejos", "CE", 141, "Cabildos o Consejos")],
  47: [("Decretos Legislativos", "CE", 85, "Decretos Legislativos")],
  60: [("derecho o interés legítimo", "LJCA", 19, "Las personas físicas o jurídicas que ostenten un derecho o interés legítimo")],
}
# Pregunta 5: el dato de la opción d) («sin que esta pueda autorizar indultos generales») parafrasea
# «que no podrá autorizar indultos generales»; se comprueba aparte, en las dos direcciones.
APOYO[5] = [APOYO[5][0], ("indultos generales", "CE", 62, "que no podrá autorizar indultos generales")]
Q = {q["n"]: q for q in qs}
for n, ap in APOYO.items():
    q = Q[n]; ok = "abcd"[q["c"]]
    for dato, f, a, frag in ap:
        assert norm(frag) in norm(plano(f, a)), ("APOYO NO LITERAL", n, f, a, frag)
        assert norm(dato) in norm(q["o"][ok]), ("LA PLANTILLA NO CASA CON LA LEY", n, ok, dato)
    for k in "abcd":
        if k != ok:
            assert not all(norm(d) in norm(q["o"][k]) for d, *_ in ap), ("DISTRACTOR IGUAL DE APOYADO", n, k)
print("coherentes con el texto legal:", sorted(APOYO), file=sys.stderr)
json.dump(sorted(APOYO), open("verif25L.json", "w"))
