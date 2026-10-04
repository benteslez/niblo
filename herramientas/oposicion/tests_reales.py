# -*- coding: utf-8 -*-
"""Genera el bloque «tests-reales» de oposicion.html a partir de los exámenes
verificados. Cada examen se extrae y comprueba en su propio módulo."""
import json, sys
sys.argv = [sys.argv[0]]
from examen25L import qs as Q25L
import verif25L   # coherencia plantilla ↔ ley (se detiene si algo no casa)
# Tema del programa de cada pregunta: solo cuando el epígrafe la cubre sin duda (None = sin clasificar).
TEMA25L = {1:"I.2",2:"I.2",3:"I.3",4:"I.6",5:"I.4",6:"I.4",7:"I.5",8:"I.6",9:None,10:"I.7",11:"I.8",12:"I.9",13:"I.10",14:"I.10",15:"I.11",16:"I.11",
  17:"II.6",18:"II.1",19:"II.2",20:"II.2",21:"II.2",22:"II.3",23:"II.3",24:"II.4",25:"II.4",26:"II.5",27:None,28:None,29:"II.6",30:"II.6",
  31:"III.1",32:"III.1",33:None,34:"III.3",35:"III.4",36:None,37:"III.5",38:"III.6",39:"III.7",40:"III.8",41:"III.8",42:None,43:"III.9",44:"III.10",45:"III.10",
  46:"IV.1",47:"IV.2",48:None,49:"IV.4",50:"IV.5",51:"IV.5",52:"IV.5",53:"IV.7",54:"IV.8",55:"IV.9",56:"IV.10",57:"IV.11",58:"IV.11",59:"IV.12",60:"IV.13",
  61:"V.1",62:"V.1",63:"V.4",64:"V.2",65:"V.3",66:None,67:"V.4",68:"V.4",69:"V.5",70:"V.5",71:"V.6",72:"V.6",73:"V.6",74:"V.7",75:"V.8",76:"V.8",77:"V.9",78:"V.9",79:"V.9",80:"V.10",81:"V.10",
  82:"VI.1",83:"VI.1",84:"VI.2",85:"VI.2",86:"VI.3",87:"VI.3",88:"VI.4",89:"VI.4",90:"VI.5",91:"VI.5",92:"VI.5",93:"VI.5",94:None,95:"VI.6",96:None,97:"VI.7",98:"VI.7",99:"V.6",100:"VI.8",
  101:"III.6",102:"II.6",103:"III.9",104:"V.8",105:"V.9"}
assert sorted(TEMA25L) == list(range(1, 106))
# ---- Texto legal LITERAL para aprender al fallar: solo de las normas cuyo texto
# consolidado está en las fuentes (BOE). Cada bloque: (norma, artículo, párrafos, título, negritas).
import fuentes
BOE_ID = {"CE":"BOE-A-1978-31229", "LO3":"BOE-A-1981-10325", "LJCA":"BOE-A-1998-16718", "LO4":"BOE-A-1981-12774", "LOTC":"BOE-A-1979-23709"}
LEY25L = {
  2:  [("LO3", "segundo", [3, 4], "Ley Orgánica 3/1981, del Defensor del Pueblo · artículo segundo, apartados cuatro y cinco", ["en el plazo máximo de un mes", "al alcanzarse la mayoría absoluta del Senado"])],
  3:  [("CE", 159, [0], "Constitución Española · artículo 159.1", ["cuatro a propuesta del Congreso", "cuatro a propuesta del Senado", "dos a propuesta del Gobierno", "dos a propuesta del Consejo General del Poder Judicial"])],
  4:  [("CE", 99, [0], "Constitución Española · artículo 99.1", ["previa consulta con los representantes designados por los Grupos políticos con representación parlamentaria"])],
  5:  [("CE", 62, list(range(11)), "Constitución Española · artículo 62", ["Ejercer el derecho de gracia con arreglo a la ley, que no podrá autorizar indultos generales"])],
  6:  [("CE", 56, [0], "Constitución Española · artículo 56.1", ["arbitra y modera el funcionamiento regular de las instituciones"])],
  7:  [("CE", 75, [1, 2], "Constitución Española · artículo 75.2 y 3", ["leyes orgánicas y de bases"])],
  9:  [("CE", 124, [3], "Constitución Española · artículo 124.4", ["a propuesta del Gobierno, oído el Consejo General del Poder Judicial"])],
  13: [("CE", 149, [0, 20], "Constitución Española · artículo 149.1.20.ª (competencia exclusiva del Estado)", ["Marina mercante"]),
       ("CE", 148, [0, 3, 11, 20], "Constitución Española · artículo 148.1 (competencias que pueden asumir las Comunidades Autónomas)", ["Ordenación del territorio, urbanismo y vivienda", "la pesca fluvial", "Asistencia social"])],
  14: [("CE", 145, [0], "Constitución Española · artículo 145.1", ["En ningún caso se admitirá la federación de Comunidades Autónomas"])],
  15: [("CE", 141, [3], "Constitución Española · artículo 141.4", ["Cabildos o Consejos"])],
  47: [("CE", 85, [0], "Constitución Española · artículo 85", ["Decretos Legislativos"])],
  60: [("LJCA", 19, [0, 1], "Ley 29/1998, reguladora de la Jurisdicción Contencioso-administrativa · artículo 19.1 a)", ["Las personas físicas o jurídicas que ostenten un derecho o interés legítimo"])],
}
CE_PLANO = " ".join(open("ce.txt", encoding="utf-8").read().split())
def bloque_ley(f, n, solo, titulo, negritas):
    ps = fuentes.SRC[f][fuentes.art(f, n)]
    out, usados = [], set()
    for i in solo:
        t = ps[i]
        for r in negritas:
            if r in t and r not in usados:
                t = t.replace(r, "**" + r + "**", 1); usados.add(r)
        out.append(t)
    assert not set(negritas) - usados, ("NEGRITA NO LITERAL", f, n, set(negritas) - usados)
    return {"t": titulo, "f": BOE_ID[f], "p": out}
LEYES = {n: [bloque_ley(*b) for b in bs] for n, bs in LEY25L.items()}
# Pregunta 1: rúbricas literales (no es un artículo); se comprueban en el texto de la CE.
RUB1 = [("TÍTULO I", "De los derechos y deberes fundamentales"), ("CAPÍTULO PRIMERO", "De los españoles y los extranjeros"),
        ("CAPÍTULO SEGUNDO", "Derechos y libertades"), ("Sección 2.ª", "De los derechos y deberes de los ciudadanos")]
for d_, r_ in RUB1: assert (d_ + " " + r_) in CE_PLANO, (d_, r_)
LEYES[1] = [{"t": "Constitución Española · rúbricas del Título I", "f": BOE_ID["CE"],
             "p": ["**TÍTULO I. De los derechos y deberes fundamentales**", "CAPÍTULO PRIMERO. De los españoles y los extranjeros",
                   "CAPÍTULO SEGUNDO. Derechos y libertades", "Sección 2.ª De los derechos y deberes de los ciudadanos"]}]
# Normas descargadas de boe.es / EUR-Lex: texto literal y coherencia plantilla ↔ ley (verif_examen).
import os, importlib
sys.path.insert(0, "boe")
import verif_examen
import leyes25L
for n_, b_ in verif_examen.verificar(leyes25L, Q25L).items():
    assert n_ not in LEYES, n_
    LEYES[n_] = b_
assert verif_examen.mutacion(leyes25L, Q25L)[0] == []

import discrepancias   # boe/discrepancias.py: plantilla ≠ norma → se mantiene la plantilla con aviso
DISC = discrepancias.comprobar()

def preguntas(qs, tema, leyes, n_anuladas, retenidas={}, disc={}):
    out = []
    for q in qs:
        p = {"n": q["n"], "q": q["q"], "o": [q["o"][k] for k in "abcd"], "c": q["c"]}
        if tema[q["n"]]: p["tema"] = tema[q["n"]]
        if q["reserva"]: p["reserva"] = True; p["nr"] = q["n"] - 100     # número dentro de la reserva
        if q["anulada"]: p["anulada"] = True
        if q["n"] in leyes: p["ley"] = leyes[q["n"]]
        if q["n"] in disc: p["disc"] = {"t": disc[q["n"]]["t"], "p": disc[q["n"]]["p"]}
        elif q["n"] in retenidas: p["retenida"] = retenidas[q["n"]]
        out.append(p)
    assert sum(1 for p in out if p.get("anulada")) == n_anuladas and sum(1 for p in out if p.get("reserva")) == 5
    return out

examenes = [{
    "id": "GACE-L-2025-1", "titulo": "GACE-L 2025", "anio": 2025, "acceso": "libre",
    "ejercicio": "Primer ejercicio", "plantilla": "definitiva",
    "fuente": "Cuestionario oficial «2025 - GACE-L» y plantilla definitiva de respuestas del primer ejercicio (ingreso libre)",
    "preguntas": preguntas(Q25L, TEMA25L, LEYES, 1)}]

# Otros exámenes: cuestionario (examen25X.py) + especificación (boe/leyes25X.py), si existen.
OTROS = [
  ("P", {"id": "GACE-P-2025-1", "titulo": "GACE-P 2025", "anio": 2025, "acceso": "promocion", "ejercicio": "Primer ejercicio", "plantilla": "definitiva",
         "fuente": "Cuestionario oficial «2025 - GACE-P» y plantilla definitiva de respuestas del primer ejercicio (promoción interna)"}, 1),
  ("X", {"id": "GACE-X-2025-1", "titulo": "GACE-L 2025 extraordinario", "anio": 2025, "acceso": "extraordinaria", "ejercicio": "Primer ejercicio extraordinario", "plantilla": "definitiva",
         "fuente": "Cuestionario oficial «2025 - GACE-L EXTRAORDINARIO» y plantilla definitiva de respuestas del primer ejercicio extraordinario (ingreso libre)"}, 0),
]
for cod, meta, n_anul in OTROS:
    if not os.path.exists(f"boe/leyes25{cod}.py"): continue
    E_ = importlib.import_module("examen25" + cod); L_ = importlib.import_module("leyes25" + cod)
    ley_ = verif_examen.verificar(L_, E_.qs)
    assert verif_examen.mutacion(L_, E_.qs)[0] == []
    sin = set(getattr(L_, "SIN_LEY", {})) | set(getattr(L_, "RETENIDA", {}))
    falta = [q["n"] for q in E_.qs if not q["anulada"] and q["n"] not in ley_ and q["n"] not in sin]
    assert not falta, (cod, "preguntas sin especificar", falta)
    examenes.append(dict(meta, preguntas=preguntas(E_.qs, L_.TEMA, ley_, n_anul, getattr(L_, "RETENIDA", {}), DISC.get(cod, {}))))

datos = {"_formato": "tests_reales_v1", "examenes": examenes}
open("tests_reales.json", "w", encoding="utf-8").write(json.dumps(datos, ensure_ascii=False, separators=(",", ":")))
for x in examenes:
    ps = x["preguntas"]
    print("test real", x["id"], ":", len(ps), "preguntas;", sum(1 for p in ps if p.get("tema")), "con tema;", sum(1 for p in ps if p.get("ley")), "con texto legal", file=sys.stderr)
