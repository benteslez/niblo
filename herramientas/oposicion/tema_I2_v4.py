# -*- coding: utf-8 -*-
"""Tema I.2 (B1T02), versión 4: estructura fija.
Mapa → cuatro bloques (I a IV), cada uno con «Dónde estamos» y «En resumen»;
cada artículo: texto literal (lit) + ficha de casillas fijas (v4_util).
Toda cita «…» pasa por c() y todo bloque por lit(): si algo no es literal, se
detiene. Preguntas, glosario, flashcards y cronología se reutilizan (verificados)."""
import json, sys, re
import fuentes
from v4_util import resumen
import v4_p1, v4_p2, v4_p3, v4_p4, v4_p5, v4_p6   # rellenan fuentes.S en orden
S = fuentes.S
v3 = json.load(open("B1T02_v3.json", encoding="utf-8"))
viejas = {s["id"]: s for s in v3["sections"]}

# IV.8 La institución hoy (dato que caduca) + cierre del bloque IV
cuerpo = viejas["s7-5"]["body"] + "\n\n" + resumen([
    "El Defensor del Pueblo es **alto comisionado de las Cortes Generales** para defender los derechos del Título I **supervisando a la Administración** (art. 54).",
    "Elección: Comisión Mixta propone; **3/5 del Congreso** y ratificación por **3/5 del Senado**; si no, en **un mes**, 3/5 del Congreso y **mayoría absoluta del Senado**. Mandato de **5 años**.",
    "Persuade, no anula: advertencias, recomendaciones, recordatorios y sugerencias; respuesta en **un mes**; informe anual a las Cortes.",
    "Está legitimado para la **inconstitucionalidad**, el **amparo** y el ***habeas corpus*** (bloque II) y no se detiene en **excepción ni sitio** (bloque III)."],
    "Fin del tema. Para fijarlo: Cierre 1 (preguntas reales de 2025) y Cierre 2 (repaso por bloques); después, el test.")
S.append({"id": "s7-5", "title": "IV.8 La institución hoy (dato que caduca)", "body": cuerpo, "nivel": 2})

from v4_examen import EX1, EX2, EX10, EX10_NOTA, EX_X4, EX_X5, EX_X6
cierre1 = "\n\n".join([
    "En los primeros ejercicios de **2025** cayeron **cinco** preguntas de este tema y **una** relacionada: en el turno libre (GACE-L), **dos** (Título I y elección del Defensor del Pueblo) y la relacionada (jurisdicción militar y estado de sitio); en el extraordinario, **tres** (suspensión del art. 55.1, plazo de respuesta al Defensor del Pueblo y art. 54). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
    "### GACE-L 2025, pregunta 1 · Título I (→ I.1.1)", EX1,
    "### GACE-L 2025, pregunta 2 · Elección del Defensor del Pueblo (→ IV.2.1)", EX2,
    "### GACE-L 2025, pregunta 10 · Jurisdicción militar y estado de sitio (relacionada; → III.6.2)", EX10, EX10_NOTA,
    "### GACE-L extraordinario 2025, pregunta 4 · Derechos que no se suspenden (→ III.2)", EX_X4,
    "### GACE-L extraordinario 2025, pregunta 5 · Plazo de respuesta al Defensor del Pueblo (→ IV.6.1)", EX_X5,
    "### GACE-L extraordinario 2025, pregunta 6 · Qué institución supervisa la Administración (→ IV.1.1)", EX_X6,
    "### Cómo se pregunta",
    "Casi todas las preguntas empiezan por «Según el artículo X…». Las cuatro opciones comparten estructura y difieren en **un plazo, una mayoría, un órgano o una palabra** (en la 2: «un mes» frente a «quince días», «absoluta» frente a «simple»). Por eso hay que estudiar el **texto literal**.",
    "**Plantillas:** *Plantilla definitiva de respuestas del primer ejercicio* (GACE-L 2025): respecto a la provisional, solo cambia la pregunta 82, que queda **anulada**; las de este tema no cambian. Extraordinario: *plantilla definitiva de respuestas del primer ejercicio extraordinario*."])
S.append({"id": "s8", "title": "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "body": cierre1, "nivel": 1})

# Cierre 2: el repaso, agrupado por bloques
filas = [l for l in viejas["s9"]["body"].split("\n") if l.startswith("| ") and not l.startswith("| Artículo")]
def bloque_de(f):
    k = f.split("|")[1].strip()
    if k.startswith(("LO 3/1981", "Ley 36/1985")): return "IV"
    if k.startswith(("LO 4/1981", "LECrim")) or k in ("55.1", "55.2", "116.2", "116.3", "116.4"): return "III"
    if k.startswith(("LJCA", "LOTC", "LO 6/1984")) or k in ("53.1", "53.2", "81.2", "86.1", "169"): return "II"
    return "I"
cab = "| Artículo | Dato literal clave | Trampa típica |\n|---|---|---|"
nombres = {"I": "I. Qué derechos y deberes hay", "II": "II. Cómo se protegen", "III": "III. Cuándo pueden suspenderse", "IV": "IV. Quién vela por ellos"}
partes = []
for b in ("I", "II", "III", "IV"):
    fs = [f for f in filas if bloque_de(f) == b]
    assert fs, b
    partes.append(f"### {nombres[b]}\n\n{cab}\n" + "\n".join(fs))
assert sum(len(p.split("\n")) - 4 for p in partes) == len(filas)
S.append({"id": "s9", "title": "Cierre 2. Repaso en 10 minutos (por bloques)", "body": "\n\n".join(partes), "nivel": 1})

orden = ["s0",
         "bI", "s1", "s2", "s3", "s3-1", "s3-2", "s3-3", "s3-4", "s4", "s4-1", "s4-2", "s4-4", "s4-3",
         "bII", "s5", "s5-1", "s5-4", "s5-5", "s5-6", "s5-3",
         "bIII", "s6", "s6-1", "s6-3", "s6-4", "s6-5", "s6-6", "s6-7", "s6-8", "s6-2",
         "bIV", "s7", "s7-1", "s7-2", "s7-3", "s7-7", "s7-4", "s7-6", "s7-5",
         "s8", "s9"]
por_id = {s["id"]: s for s in S}
assert sorted(por_id) == sorted(orden) and len(S) == len(orden), (sorted(set(por_id) ^ set(orden)))
S = [por_id[i] for i in orden]

# Remisiones «→ II.4.2»: el apartado (y el subapartado) tienen que existir
titulos = {s["title"].split(" ")[0]: s for s in S}
for s in S:
    for m in re.finditer(r"→ (I{1,3}|IV)\.(\d+)(?:\.(\d+))?", s["body"]):
        clave = f"{m.group(1)}.{m.group(2)}"
        assert clave in titulos, ("REMISIÓN ROTA", s["id"], m.group(0))
        if m.group(3):
            sub = f"### {m.group(2)}.{m.group(3)} "
            assert sub in titulos[clave]["body"], ("REMISIÓN ROTA", s["id"], m.group(0))

data = dict(v3)
data["sections"] = S
ids = set(orden)
# Cada término del glosario y cada hito apuntan al apartado donde ahora se explican
GLOS = {"Recurso de amparo": "s5-6", "Derechos fundamentales y libertades públicas": "s3-1", "Principios rectores": "s4-2",
        "Contenido esencial": "s5", "Reserva de ley": "s5", "Actitud hostil y entorpecedora": "s7-7"}
data["glossary"] = [dict(g, section=GLOS.get(g["t"], g["section"])) for g in data["glossary"]]
assert all(any(g["t"] == k for g in data["glossary"]) for k in GLOS)
CRONO = {"2024": "s4-4", "LO 4/1981": "s6-3"}
for t in data["timeline"]:
    for k, v in CRONO.items():
        if t["y"] == k or t["txt"].startswith(k):
            t["target"] = v
for g in data["glossary"]: assert g["section"] in ids, g
for t in data["timeline"]: assert t["target"] in ids, t
# Test: las preguntas reales llevan en la corrección el porqué de cada opción
from v4_util import CUEST, PLANT, PORQUE, CUEST_X, PLANT_X, CONV_X
# Preguntas del extraordinario (X4 a X6): literales del cuestionario, respuesta de la plantilla
# definitiva y el mismo porqué de los apuntes; van detrás de las dos del turno libre.
CAT_X = {4: "Art. 55.1 CE", 5: "Art. 30.1 LO 3/1981", 6: "Art. 54 CE"}
nuevas = []
for n, cat in CAT_X.items():
    ok = PLANT_X[n]; P = PORQUE[("X", n)]
    nuevas.append({"q": CUEST_X[n]["q"], "o": [CUEST_X[n]["o"][k] for k in "abcd"], "c": "abcd".index(ok),
                   "e": f"Respuesta {ok}) según la plantilla definitiva. " + " ".join(("✅ " if k == ok else "✗ ") + f"{k}) " + P[k] for k in "abcd").replace("**", ""),
                   "cat": cat, "real": f"Examen {CONV_X} · pregunta {n}"})
assert not any("extraordinario" in q.get("real", "") for q in data["questions"])
data["questions"] = data["questions"][:2] + nuevas + data["questions"][2:]
for q in data["questions"]:
    if "extraordinario" in q.get("real", ""): continue
    m = re.search(r"pregunta (\d+)$", q.get("real", ""))
    if not m: continue
    n = int(m.group(1)); assert n in PORQUE, n
    assert q["q"] == CUEST[n]["q"] and q["o"] == [CUEST[n]["o"][k] for k in "abcd"], ("NO LITERAL", n)
    assert q["c"] == "abcd".index(PLANT[n]), ("PLANTILLA", n)
    q["e"] = f"Respuesta {PLANT[n]}) según la plantilla definitiva. " + " ".join(
        ("✅ " if k == PLANT[n] else "✗ ") + f"{k}) " + PORQUE[n][k] for k in "abcd").replace("**", "")
data["subtitle"] = "Cuatro preguntas: I. Qué derechos y deberes hay (arts. 9.2 y 10-52) · II. Cómo se protegen (art. 53, LJCA, habeas corpus y LOTC) · III. Cuándo pueden suspenderse (arts. 55 y 116, LO 4/1981 y LECrim) · IV. Quién vela por ellos (Defensor del Pueblo). Cada artículo: texto literal del BOE y ficha."
print("apartados", len(S), "| preguntas", len(data["questions"]), "| glosario", len(data["glossary"]), "| fc", len(data["flashcards"]), file=sys.stderr)
json.dump(data, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False)
