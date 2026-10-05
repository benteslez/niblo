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

# =============================================================================
# MAPA
T.ap("s0", "Mapa del tema", f"""
**Epígrafes oficiales** (BOE-A-2025-26262, anexo VII, Bloque I). Este tema **reúne los tres primeros temas del bloque**, igual que la plantilla del plan de estudio y el módulo M101:
> I.1 La Constitución Española de 1978: estructura y contenido. La reforma de la Constitución.
> I.2 Derechos y deberes fundamentales. Su garantía y suspensión. El Defensor del Pueblo.
> I.3 El Tribunal Constitucional. Organización, composición y atribuciones.

### El hilo del tema

| Bloque | Pregunta | Constitución | Otras normas |
|---|---|---|---|
| **I** | ¿Cuándo nace y cuándo se ha reformado? | Fórmula final, disp. final | Cuatro reformas (1992, 2011, 2024, 2026) |
| **II** | ¿Cómo está hecha? | Partes, títulos, capítulos, secciones, disposiciones | — |
| **III** | ¿De qué trata cada artículo? | Arts. 1 a 55 (literales) | — |
| **IV** | ¿Qué niveles de protección tienen los derechos? | Título I, arts. 10 a 52 | — |
| **V** | ¿Cómo se garantizan? | Arts. 53, 54, 81, 161 y 162 | LOTC arts. 32, 33, 41 a 46 |
| **VI** | ¿Cómo se suspenden? | Arts. 55 y 116 | LO 4/1981 |
| **VII** | El Tribunal Constitucional | Título IX, arts. 159 a 165 | LOTC |
| **VIII** | El Defensor del Pueblo | Art. 54 | LO 3/1981 |
| **IX** | ¿Cómo se reforma? | Título X, arts. 166 a 169; art. 87 | Reglamentos del Congreso y del Senado; LO 2/1980 |
| **X** | Preguntas y repaso | — | — |
| **XI** | Cronología e hitos | — | — |

### Cómo estudiar este tema (módulo M101)

- **Mira siempre el epígrafe.** Estudiar «por leyes» está bien al principio, pero el programa dice qué se puede preguntar: aquí se ha quitado lo que no entra.
- La Constitución es la **única** norma en la que hay que aprender la **estructura y el contenido artículo por artículo**: en las demás leyes no se pregunta así.
- **Lectura profunda de los artículos 1 a 55**, cada vez que repases el tema. Gran parte de las preguntas intentan confundirte con **palabras clave** de esos artículos. **No hace falta saberlos literalmente**, pero sí conocer su «música» para que no te cuelen una palabra cambiada.
- **Usa siempre el mismo material.** La memoria visual ayuda a ubicar la información: por eso cada título y capítulo tiene **el mismo color** en los apuntes, en el texto de la Constitución, en el organigrama y en el test.
- Primera vuelta: sabe **de qué trata cada artículo** y **dónde está** en la estructura (¿en qué capítulo? ¿en qué sección?). Después, ve profundizando.
- Se preguntan, sobre todo, la **estructura**, las **garantías** y la **suspensión** de derechos. Según el módulo, el 90 % de las preguntas de este tema son de lo que aquí se desarrolla.

{ir("#/ce/texto", "📜 Constitución completa")} {ir("#/ce/organigrama", "🗺 Organigrama")} {ir("#/ce/test", "🧭 Test Constitución")}

### Las etiquetas de los apuntes

- {IMP} → lo que el módulo marca como «importante» o «atención»: se pregunta mucho o se presta a trampas.
- {PRE} → lo que el módulo dice que **no es necesario** estudiar a fondo. Lleva una nota que explica por qué.
- Los colores de los títulos y capítulos son los de la Constitución completa: {tag("P", "Título preliminar")} {tag("I", "Título I")} {tag("I.2.1", "Sección 1.ª")} {tag("III", "Título III")} {tag("IX", "Título IX")}…

### Avisos: lo que dice la norma prevalece sobre la guía

- **Reforma del art. 69.3.** La guía M101 la sitúa el «20 de mayo de 2026». La reforma es **de 19 de mayo de 2026** (fecha de la sanción del Rey) y se publicó y entró en vigor el **20 de mayo de 2026** (→ I.2).
- **Reformas.** En el vídeo solo se citan las de los arts. 13.2 y 135; la guía añade la del 49 (2024) y la del 69.3 (2026). En total hay **cuatro**.
- **Ley de igualdad.** El vídeo dice que va «por ley orgánica». La LO 3/2007 lo es por su nombre, pero solo tienen carácter orgánico algunos preceptos (→ V.1).
- **Organigrama.** El de la guía rotula el capítulo II del título I con «Art. 14». Aquí se sigue el texto de la CE: el capítulo II comprende los **arts. 14 a 38** (→ II.3).
""")

# =============================================================================
T.ap("bI", "I. ¿Cuándo nace la Constitución y cuándo se ha reformado?", donde(
  "Primera pregunta. Conviene conocer las **fechas** y, sobre todo, **quién hace qué** en cada una: aprobar, ratificar, sancionar, promulgar, publicar y entrar en vigor son cosas distintas.",
  ["1 Las fechas de 1978", "2 Las cuatro reformas"]))

T.ap("s1", "I.1 Las fechas de 1978", f"""
Para recordarlas, ponte en situación: **las Cortes aprueban** el texto en una sesión conjunta; más de un mes después, **el pueblo lo ratifica** en referéndum (preparar el referéndum es lo que más tarda); y todo lo demás ocurre en diciembre del 78: **el Rey sanciona y promulga**, y dos días después **se publica en el BOE y entra en vigor**.

{tabla(["Hecho", "Fecha", "Quién", "Fuente"], [
  ["**Aprobación**", "31 de octubre de 1978", "Las **Cortes Generales**, en sesiones plenarias del Congreso de los Diputados y del Senado", "[[M101]]"],
  ["**Ratificación**", "6 de diciembre de 1978", "El **pueblo español**, en referéndum", "[[M101]]"],
  ["**Sanción y promulgación**", "27 de diciembre de 1978", "El **Rey**, ante las Cortes", "CE (fórmula final)"],
  ["**Publicación en el BOE y entrada en vigor**", "29 de diciembre de 1978", "BOE n.º 311; entra en vigor el **mismo día** de la publicación", "BOE · CE (disp. final)"]])}

{unidad("1.1 La sanción y promulgación: 27 de diciembre",
  lit("CE", "firma", ["GUARDEN Y HAGAN GUARDAR ESTA CONSTITUCIÓN COMO NORMA FUNDAMENTAL DEL ESTADO", "A VEINTISIETE DE DICIEMBRE DE MIL NOVECIENTOS SETENTA Y OCHO"], solo=[0, 1, 2], titulo="Fórmula final de la Constitución"))}

{unidad("1.2 La entrada en vigor: el día de la publicación en el BOE",
  lit("CE", "df", ["entrará en vigor el mismo día de la publicación de su texto oficial"]))}

!> {IMP} **Atención a los verbos.** Las preguntas juegan con quién hace cada cosa: las **Cortes aprueban**, el **pueblo ratifica**, el **Rey sanciona y promulga**, el **BOE publica** y la Constitución **entra en vigor**. Y se agrupan **de dos en dos**: sanción y promulgación (27); publicación y entrada en vigor (29, dos días después). Sepáralos siempre.

?> **Publicar no es entrar en vigor.** Que una norma se publique en el BOE no significa que esté ya en vigor: a veces se pospone. En la Constitución coinciden porque lo dice su disposición final.

**Truco para recordar:** todo empieza el **27** (sanción y promulgación) y **dos días después**, el **29**, pasan otras dos cosas (publicación y entrada en vigor). El 27 se repite en las reformas de 1992 (27 de agosto) y de 2011 (27 de septiembre).
""", 2)

T.ap("s2", "I.2 Las cuatro reformas de la Constitución", f"""
La Constitución se ha reformado **cuatro veces**, siempre por el procedimiento del **art. 167** (→ IX.2). Las fechas son las de la **sanción** del Rey, que figuran al pie de cada reforma; el BOE las publica y entran en vigor, como la propia Constitución, el mismo día de la publicación.

{tabla(["Reforma", "Artículo", "Sanción", "Publicación y entrada en vigor", "Qué cambia"], [
  ["**1992**", "**13.2**", "27 de agosto de 1992", "28 de agosto de 1992", "Los extranjeros pueden tener **sufragio pasivo** (y no solo activo) en las elecciones **municipales**, por reciprocidad. Se añadió «y pasivo»."],
  ["**2011**", "**135**", "27 de septiembre de 2011", "27 de septiembre de 2011", "**Estabilidad presupuestaria**: el artículo se reescribió entero."],
  ["**2024**", "**49**", "15 de febrero de 2024", "17 de febrero de 2024", "Protección de las **personas con discapacidad**: actualiza su lenguaje y su contenido."],
  ["**2026**", "**69.3**", "19 de mayo de 2026", "20 de mayo de 2026", "Circunscripciones del **Senado** en las islas: **Ibiza y Formentera** pasan a elegir cada una su senador."]])}

{unidad("2.1 Reforma del art. 13.2 (1992)",
  lit("CE", "a13", ["sufragio activo y pasivo"], solo=[2]),
  lit("REF1992", "preambulo", ["27 de agosto de 1992"], solo=[ix("REF1992", "preambulo", "Artículo único") + j for j in (0, 1, 2)] + [ix("REF1992", "preambulo", "Madrid,")], titulo="Reforma de la Constitución de 1992 (artículo único)"))}

{unidad("2.2 Reforma del art. 135 (2011)",
  lit("CE", "a135", ["principio de estabilidad presupuestaria"], solo=[1]),
  lit("REF2011", "preambulo", ["garantizar el principio de estabilidad presupuestaria"], solo=[9], titulo="Exposición de motivos de la Reforma de 2011 (extracto)"))}

{unidad("2.3 Reforma del art. 49 (2024)",
  lit("CE", "a49", ["Las personas con discapacidad ejercen los derechos previstos en este Título en condiciones de libertad e igualdad reales y efectivas"], solo=[1, 2]),
  lit("REF2024", "preambulo", ["precisa de una actualización en cuanto a su lenguaje y contenido"], solo=[10], titulo="Preámbulo de la Reforma de 2024 (extracto)"))}

{unidad("2.4 Reforma del art. 69.3 (2026)",
  lit("CE", "a69", ["Ibiza, Formentera, Menorca"], solo=[3]),
  lit("REF2026", "preambulo", ["19 de mayo de 2026"], solo=[ix("REF2026", "preambulo", "Artículo único") + j for j in (0, 1)] + [ix("REF2026", "preambulo", "Madrid,")], titulo="Reforma de la Constitución de 2026 (artículo único y fecha)"))}

!> {IMP} **Para el examen:** artículos reformados **13.2, 135, 49 y 69.3**, y año de cada reforma (**1992, 2011, 2024, 2026**). La del 135 es la más «radical»: se reescribió casi entero, con ocasión de la crisis de la deuda.

?> La **guía M101** da el art. 69.3 el «20 de mayo de 2026»: es la fecha de **publicación y entrada en vigor**. La reforma es de **19 de mayo de 2026** (sanción).
""", 2)

# =============================================================================
# II. ESTRUCTURA
_P = TIT["P"]; _I = TIT["I"]
assert rng(arts(_P)) == "1–9" and rng(arts(_I)) == "10–55"
FILAS_TIT = []
for _t in CEJ["titulos"]:
    _a = arts(_t); assert _a == list(range(_a[0], _a[-1] + 1))
    FILAS_TIT.append([tag(_t["id"], "Título preliminar" if _t["id"] == "P" else "Título " + _t["id"]), _t["nombre"] or "—", f"**{rng(_a)}**", len(_a)])
assert sum(f[3] for f in FILAS_TIT) == 169 and len(FILAS_TIT) == 11

T.ap("bII", "II. ¿Cómo está hecha? Estructura de la Constitución", donde(
  "Segunda pregunta. La Constitución es la **única norma** en la que hay que saber de memoria **cómo se reparten los artículos**: títulos, capítulos y secciones. Sirve de armazón para colgar después el contenido de cada artículo.",
  ["1 Las dos partes: dogmática y orgánica", "2 Los títulos y sus artículos", "3 El Título I por dentro (lo más preguntable)", "4 Los capítulos de los Títulos III y VIII", "5 Las disposiciones: 4-9-1-1"]))

T.ap("s3", "II.1 Las dos partes y la lógica de «las muñecas rusas»", f"""
La Constitución se abre con un **preámbulo** y su articulado se reparte en **dos partes**:

{tabla(["Parte", "Títulos", "Artículos", "De qué trata"], [
  [f"**Parte dogmática**", f"{tag('P', 'Título preliminar')} y {tag('I', 'Título I')}", "**1 a 55**", "Los principios y los **derechos y deberes**: qué es el Estado y qué se reconoce a las personas"],
  [f"**Parte orgánica**", f"{tag('II', 'Títulos II')} a {tag('X', 'X')}", "**56 a 169**", "Cómo se **organiza** el Estado y sus instituciones: Corona, Cortes, Gobierno, Poder Judicial, territorio, Tribunal Constitucional y reforma"]])}

### La lógica de «las muñecas rusas»

Como muchas leyes, la Constitución va **de lo general a lo concreto**: lo primero que aparece es lo más **ideal e inespecífico**, y lo que viene después lo **concreta**. Si tienes esto en la cabeza, la estructura se asimila mejor:

- El **preámbulo** dice a qué aspira el Estado; la Constitución desarrolla esas aspiraciones. Según el módulo, no tiene valor jurídico propio («papel mojado»), pero a la vez es lo más importante porque da el sentido a todo lo demás.
- El **Título preliminar** y el **Título I** son la parte dogmática: sientan las ideas que luego desarrolla la parte orgánica.
- Dentro del Título I ocurre lo mismo: el **art. 10** (la dignidad de la persona, los derechos inviolables…) queda **fuera de los capítulos** y nutre «espiritualmente» todo lo demás; y el **art. 14** (la igualdad ante la ley) queda **fuera de las dos secciones** y se concreta en los derechos que vienen después.

!> {IMP} No es una regla que se cumpla a rajatabla, pero **sirve para ubicar**: lo primero es lo más importante y a la vez lo más genérico; lo que viene después es lo que concreta. Por eso los artículos 10 y 14 quedan «sueltos».

{ir("#/ce/organigrama", "🗺 Ver el organigrama")}
""", 2)

T.ap("s4", "II.2 Los títulos y sus artículos", f"""
{IMP} Hay que saberse **los nombres de los títulos** y **cómo se reparten los artículos** entre ellos. Se pregunta con frecuencia (p. ej., «¿en qué título está el art. 56?», «¿qué artículos comprende el Título VIII?»).

{tabla(["Título", "Nombre (rúbrica del BOE)", "Artículos", "N.º"], FILAS_TIT + [["**Total**", "", "**1–169**", "**169**"]])}

**Números finales de cada título** (para fijar los límites): **9 · 55 · 65 · 96 · 107 · 116 · 127 · 136 · 158 · 165 · 169**.

Los títulos tienen **rúbrica propia** salvo el **Título preliminar**, que no tiene nombre. En total: **11 títulos** (el preliminar y diez numerados), **169 artículos** y **15 disposiciones** (→ II.5).

{ir("#/ce/texto", "📜 Ver el texto completo, con un color por título")}
""", 2)

_c2 = _I["caps"][1]
assert [rng(arts(x)) for x in _I["caps"]] == ["11–13", "14–38", "39–52", "53–54", "55"] and rng(arts(_c2["secs"][0])) == "15–29" and rng(arts(_c2["secs"][1])) == "30–38"
assert _I["arts"][0]["n"] == 10 and _c2["arts"][0]["n"] == 14
T.ap("s5", "II.3 El Título I por dentro (lo más preguntable)", f"""
{IMP} Es **lo más preguntable de la estructura**, sobre todo la división del **capítulo segundo** en secciones. Hay que saberlo «como el padrenuestro».

{tabla(["Unidad", "Nombre (BOE)", "Artículos", "Ojo"], [
  [tag("I", "Título I"), c("CE", "ti", "De los derechos y deberes fundamentales"), "**10 a 55**", "Contiene los derechos, deberes y sus garantías"],
  [tag("I", "Art. 10"), "(dignidad de la persona…)", "**10**", "**Fuera de los capítulos**: va antes del capítulo primero"],
  [tag("I.1", "Capítulo primero"), c("CE", "cprimero", "De los españoles y los extranjeros"), "**11 a 13**", "Nacionalidad, mayoría de edad y extranjeros"],
  [tag("I.2", "Capítulo segundo"), c("CE", "csegundo", "Derechos y libertades"), "**14 a 38**", "El art. **14** queda **fuera de las dos secciones**"],
  [tag("I.2.1", "Sección 1.ª"), c("CE", "s1", "De los derechos fundamentales y de las libertades públicas"), "**15 a 29**", "**Los derechos fundamentales**: la máxima protección"],
  [tag("I.2.2", "Sección 2.ª"), c("CE", "s2", "De los derechos y deberes de los ciudadanos"), "**30 a 38**", "Derechos y deberes de los ciudadanos"],
  [tag("I.3", "Capítulo tercero"), c("CE", "ctercero", "De los principios rectores de la política social y económica"), "**39 a 52**", "Son principios, no derechos fundamentales"],
  [tag("I.4", "Capítulo cuarto"), c("CE", "ccuarto", "De las garantías de las libertades y derechos fundamentales"), "**53 y 54**", "Garantías: arts. 53 y 54 (→ V)"],
  [tag("I.5", "Capítulo quinto"), c("CE", "cquinto", "De la suspensión de los derechos y libertades"), "**55**", "Suspensión (→ VI)"]])}

!> {IMP} **Los dos «sueltos» del título I:** el **art. 10** queda fuera de los capítulos y el **art. 14** queda dentro del capítulo segundo pero **fuera de las secciones primera y segunda**. Si preguntan «¿qué artículos comprende la sección primera?», la respuesta es **15 a 29** (no el 14).

!> {IMP} **La división de los 55 artículos de la parte dogmática, en una línea:** 1-9 · 10 · 11-13 · 14 · **15-29** · 30-38 · 39-52 · 53-54 · 55.

**Truco:** de **15 a 29** es la sección primera del capítulo segundo del título I. Parece un trabalenguas, pero es la clave de muchas preguntas: los derechos de la sección primera son los únicos que tienen **todas** las garantías (→ IV).
""", 2)

T.ap("s6", "II.4 Los capítulos de los Títulos III y VIII", f"""
{PRE} **No pierdas tiempo memorizando la división en capítulos de los Títulos III y VIII.** El módulo la considera prescindible: se pregunta mucho menos que la del Título I. Basta con saber que existen y los límites de los títulos. Aquí está por si quieres consultarla:

{tabla(["Título", "Capítulo", "Nombre (BOE)", "Artículos"], [
  [tag(t["id"], "Título " + t["id"]), tag(f'{t["id"]}.{i + 1}', cp["num"].capitalize().replace("Ítulo", "ítulo")), cp["nombre"], rng(arts(cp))] for t in (TIT["III"], TIT["VIII"]) for i, cp in enumerate(t["caps"])])}

*Nota: en el Título I (11 a 13, 14 a 38, 39 a 52, 53 y 54, 55) la división sí es muy preguntable; en el III y el VIII, no.*
""", 2)

assert sum(1 for d in CEJ["disposiciones"] if "adicional" in d["t"]) == 4 and sum(1 for d in CEJ["disposiciones"] if "transitoria" in d["t"]) == 9
T.ap("s7", "II.5 Las disposiciones: 4-9-1-1", f"""
Tras el artículo 169 vienen **quince disposiciones**, que se agrupan así:

{tabla(["Clase", "Cuántas", "Cuáles"], [
  ["**Adicionales**", "**4**", "Primera a cuarta"],
  ["**Transitorias**", "**9**", "Primera a novena"],
  ["**Derogatoria**", "**1**", "Única"],
  ["**Final**", "**1**", "Única"]])}

{IMP} **Regla mnemotécnica: «4-9-1-1».** Cuatro adicionales, **nueve** transitorias (la Constitución nace en plena **transición**: por eso son las más numerosas), **una** derogatoria y **una** final. Y siempre **en este orden**: adicionales, transitorias, derogatoria y final.

{lit("CE", "dd", ["Queda derogada la Ley 1/1977, de 4 de enero, para la Reforma Política"], solo=[0, 1])}

{lit("CE", "df", ["entrará en vigor el mismo día de la publicación de su texto oficial"])}

!> La **disposición derogatoria** deroga la Ley para la Reforma Política y las Leyes Fundamentales del régimen anterior; la **final** fija la **entrada en vigor** (→ I.1).
""", 2)

T.ap("s8", "II.6 Resumen de la estructura", resumen([
  "**Preámbulo** + **Parte dogmática** (arts. **1-55**: Título preliminar y Título I) + **Parte orgánica** (arts. **56-169**: Títulos II a X) + **15 disposiciones** (4-9-1-1).",
  "**11 títulos**, **169 artículos**. Finales de título: 9 · 55 · 65 · 96 · 107 · 116 · 127 · 136 · 158 · 165 · 169.",
  "**Título I:** art. 10 (suelto) · cap. I (11-13) · cap. II (14-38: art. 14 suelto, **sección 1.ª 15-29**, sección 2.ª 30-38) · cap. III (39-52) · cap. IV (53-54) · cap. V (55).",
  "La división en capítulos de los Títulos III y VIII es " + PRE + "."], "Siguiente: III. ¿De qué trata cada artículo? (arts. 1 a 55)"), 2)

# =============================================================================
# III. CONTENIDO: ARTÍCULOS 1 A 55
KEYU = {}   # artículo → clave de color de su unidad (la más específica)
def _clave(x, k):
    for a in x.get("arts", []): KEYU[a["n"]] = k
    for i, cp in enumerate(x.get("caps", []), 1):
        _clave(cp, f"{k}.{i}")
    for j, s in enumerate(x.get("secs", []), 1): _clave(s, f"{k}.{j}")
for _t in CEJ["titulos"]: _clave(_t, _t["id"])
assert KEYU[10] == "I" and KEYU[14] == "I.2" and KEYU[15] == "I.2.1" and KEYU[30] == "I.2.2" and KEYU[40] == "I.3" and KEYU[55] == "I.5"

def fila_art(n): return [tag(KEYU[n], f"Art. {n}"), rubrica(n) if n <= 52 else "", ""]
def tabla_arts(nums, ojo=None):
    return tabla(["Art.", "De qué trata (título de la guía M101)"], [[tag(KEYU[n], f"Art. {n}"), rubrica(n)] for n in nums])

NOTAS = {
 1: (["Estado social y democrático de Derecho", "la libertad, la justicia, la igualdad y el pluralismo político", "La soberanía nacional reside en el pueblo español", "Monarquía parlamentaria"],
     "Tres ideas, un apartado cada una: **valores superiores** (cuatro: libertad, justicia, igualdad y pluralismo político), **soberanía nacional** del pueblo español y **forma política** (Monarquía parlamentaria)."),
 2: (["indisoluble unidad de la Nación española", "derecho a la autonomía de las nacionalidades y regiones", "solidaridad entre todas ellas"], "Tres ideas: **unidad**, **autonomía** y **solidaridad**."),
 3: (["El castellano es la lengua española oficial del Estado", "Las demás lenguas españolas serán también oficiales en las respectivas Comunidades Autónomas de acuerdo con sus Estatutos"],
     "Del castellano hay **deber de conocerla** y **derecho a usarla**; las demás lenguas son oficiales en su Comunidad **según sus Estatutos**."),
 4: (["tres franjas horizontales, roja, amarilla y roja", "la amarilla de doble anchura"], "Rojo-amarillo-rojo: la franja **amarilla** es la de **doble anchura**."),
 5: (["villa de Madrid"], "La capital es la **villa** de Madrid."),
 6: (["Su estructura interna y funcionamiento deberán ser democráticos"], f"{IMP} **Estructura interna y funcionamiento democráticos**: lo exige la Constitución a los **partidos** (art. 6), a los **sindicatos y asociaciones empresariales** (art. 7), a los **Colegios Profesionales** (art. 36) y a las **organizaciones profesionales** (art. 52)."),
 7: (["libres dentro del respeto a la Constitución y a la ley"], "Mismo esquema que el art. 6: creación y actividad **libres** dentro del respeto a la Constitución y a la ley."),
 8: (["Ejército de Tierra, la Armada y el Ejército del Aire", "Una ley orgánica regulará las bases de la organización militar"], "Tres ejércitos (**Tierra, Armada y Aire**) y **ley orgánica** para las bases de la organización militar."),
 9: (["Los ciudadanos y los poderes públicos están sujetos a la Constitución", "reales y efectivas", "principio de legalidad, la jerarquía normativa, la publicidad de las normas, la irretroactividad de las disposiciones sancionadoras no favorables o restrictivas de derechos individuales, la seguridad jurídica, la responsabilidad y la interdicción de la arbitrariedad de los poderes públicos"],
     f"{IMP} **El art. 9.3 garantiza siete principios:** legalidad · jerarquía normativa · publicidad de las normas · irretroactividad de las sancionadoras no favorables o restrictivas de derechos individuales · seguridad jurídica · responsabilidad · interdicción de la arbitrariedad de los poderes públicos."),
 10: (["La dignidad de la persona", "derechos inviolables", "libre desarrollo de la personalidad", "Declaración Universal de Derechos Humanos"],
      f"El art. 10 queda **fuera de los capítulos**: es el **fundamento** del orden político. Su apartado 2 manda interpretar los derechos **conforme a la Declaración Universal de Derechos Humanos** y a los tratados ratificados por España."),
 11: (["se adquiere, se conserva y se pierde de acuerdo con lo establecido por la ley", "Ningún español de origen podrá ser privado de su nacionalidad"], "La nacionalidad se regula **por ley**; ningún español **de origen** puede ser privado de ella."),
 12: (["dieciocho años"], "Mayoría de edad: **dieciocho años**."),
 13: (["Solamente los españoles serán titulares de los derechos reconocidos en el artículo 23", "La extradición sólo se concederá en cumplimiento de un tratado o de la ley"], "Extranjeros: libertades **según tratados y ley**; sufragio (art. 23) solo para españoles, salvo reciprocidad **en elecciones municipales** (reforma de 1992); extradición y asilo."),
 14: (["Los españoles son iguales ante la ley", "nacimiento, raza, sexo, religión, opinión"], f"{IMP} El art. 14 está **dentro del capítulo II pero fuera de las secciones**. Tiene **tutela preferente y sumaria y amparo**, pero **no** reserva de ley orgánica (→ IV)."),
 15: (["derecho a la vida y a la integridad física y moral", "Queda abolida la pena de muerte"], "Vida e integridad física y moral; sin tortura ni tratos inhumanos o degradantes; **pena de muerte abolida** (salvo leyes penales militares en tiempos de guerra)."),
 16: (["Ninguna confesión tendrá carácter estatal", "Nadie podrá ser obligado a declarar sobre su ideología, religión o creencias"], "Libertad ideológica, religiosa y de culto; **ninguna confesión estatal**; nadie obligado a declarar sobre sus creencias."),
 17: (["setenta y dos horas", "Se garantiza la asistencia de abogado al detenido"], f"{IMP} **Detención preventiva: máximo 72 horas.** El **art. 17.3** (derechos del detenido) es el que **no se puede suspender en el estado de excepción** (→ VI)."),
 18: (["El domicilio es inviolable", "consentimiento del titular o resolución judicial, salvo en caso de flagrante delito", "secreto de las comunicaciones"], "Honor, intimidad e imagen · **domicilio inviolable** (18.2) · **secreto de las comunicaciones** (18.3). Los apartados 2 y 3 son **suspendibles** (→ VI)."),
 19: (["elegir libremente su residencia", "entrar y salir libremente de España"], "Residencia y circulación; entrar y salir de España **sin limitación por motivos políticos o ideológicos**."),
 20: (["Sólo podrá acordarse el secuestro de publicaciones, grabaciones y otros medios de información en virtud de resolución judicial", "no puede restringirse mediante ningún tipo de censura previa"], "Cuatro libertades en el apartado 1; **sin censura previa**; el **secuestro** de publicaciones, solo por **resolución judicial**. Suspendibles: 20.1 a) y d) y 20.5."),
 21: (["no necesitará autorización previa", "comunicación previa a la autoridad"], "Reunión **sin autorización previa**; en lugares de tránsito público y manifestaciones, **comunicación previa**."),
 22: (["resolución judicial motivada", "Se prohíben las asociaciones secretas y las de carácter paramilitar"], "Las asociaciones solo se disuelven o suspenden por **resolución judicial motivada**; se inscriben en un registro **a solo efectos de publicidad**."),
 23: (["participar en los asuntos públicos", "acceder en condiciones de igualdad a las funciones y cargos públicos"], "**23.1** participación política (directa o por representantes); **23.2** acceso a **funciones y cargos públicos** en condiciones de igualdad: el derecho de los opositores."),
 24: (["tutela efectiva de los jueces y tribunales", "Juez ordinario predeterminado por la ley", "presunción de inocencia"], "**Tutela judicial efectiva** sin indefensión (24.1) y las garantías del proceso (24.2): juez predeterminado, defensa, letrado, proceso público sin dilaciones, pruebas, no declarar contra sí mismo, presunción de inocencia."),
 25: (["no constituyan delito, falta o infracción administrativa", "reeducación y reinserción social", "no podrán consistir en trabajos forzados", "La Administración civil no podrá imponer sanciones que, directa o subsidiariamente, impliquen privación de libertad"], "**Legalidad penal** (25.1) · penas orientadas a la **reinserción** (25.2) · la Administración civil **no puede imponer privación de libertad** (25.3)."),
 26: (["Se prohíben los Tribunales de Honor"], "**Tribunales de Honor prohibidos** en la Administración civil y las organizaciones profesionales."),
 27: (["La enseñanza básica es obligatoria y gratuita", "autonomía de las Universidades"], "Derecho a la educación y libertad de enseñanza; enseñanza básica **obligatoria y gratuita**; **autonomía universitaria**."),
 28: (["Todos tienen derecho a sindicarse libremente", "derecho a la huelga de los trabajadores"], "Libertad sindical (28.1) y **huelga** (28.2); la ley asegura los **servicios esenciales**. El 28.2 es **suspendible** (→ VI)."),
 29: (["derecho de petición individual y colectiva, por escrito"], "Petición **individual y colectiva, por escrito**. Los militares, solo **individualmente**. Es el **último** artículo de la sección 1.ª."),
 30: (["objeción de conciencia", "servicio militar obligatorio"], f"**Derecho y deber** de defender a España (30.1). El **30.2** (objeción de conciencia) es el **único** de la sección 2.ª que tiene **amparo** (→ IV)."),
 31: (["capacidad económica", "igualdad y progresividad", "alcance confiscatorio"], "Deber de contribuir a los gastos públicos según la **capacidad económica**, con un sistema tributario **justo, igual y progresivo**, nunca confiscatorio."),
 32: (["plena igualdad jurídica"], "Matrimonio entre el hombre y la mujer con **plena igualdad jurídica**."),
 33: (["derecho a la propiedad privada y a la herencia", "La función social", "utilidad pública o interés social, mediante la correspondiente indemnización"], f"{IMP} La propiedad privada **no es un derecho fundamental** (sección 2.ª): sin amparo ni ley orgánica. Su contenido lo delimita la **función social**; solo se priva de bienes por **utilidad pública o interés social** con **indemnización**."),
 34: (["derecho de fundación para fines de interés general"], "Derecho de fundación para **fines de interés general**."),
 35: (["deber de trabajar y el derecho al trabajo"], "**Deber** de trabajar y **derecho** al trabajo, a la libre elección de profesión, a la promoción y a una remuneración suficiente, **sin discriminación por sexo**."),
 36: (["La estructura interna y el funcionamiento de los Colegios deberán ser democráticos"], "Colegios Profesionales: ley propia y **estructura democrática**."),
 37: (["negociación colectiva laboral", "medidas de conflicto colectivo"], "**Negociación colectiva** (37.1) y **conflicto colectivo** (37.2, suspendible en excepción y sitio)."),
 38: (["libertad de empresa en el marco de la economía de mercado"], "Es el **último** artículo del capítulo II (sección 2.ª). Libertad de empresa en la **economía de mercado**."),
 39: (["protección social, económica y jurídica de la familia"], "**Familia, hijos y madres**. Primer artículo del capítulo tercero: **principios rectores**, no derechos fundamentales."),
 40: (["pleno empleo"], "Progreso social y económico, distribución de la renta, **pleno empleo**, formación, seguridad e higiene, descanso."),
 41: (["régimen público de Seguridad Social para todos los ciudadanos"], "**Régimen público de Seguridad Social**; las prestaciones complementarias son **libres**."),
 42: (["trabajadores españoles en el extranjero"], "La guía M101 lo titula «inmigrantes españoles en el extranjero»; la CE dice **trabajadores españoles en el extranjero** y su **retorno**."),
 43: (["derecho a la protección de la salud"], f"{IMP} La **salud** es un derecho **del capítulo III**: sin amparo ni recurso de inconstitucionalidad por sí mismo; solo se alega ante la jurisdicción ordinaria **según las leyes que lo desarrollen**."),
 44: (["acceso a la cultura"], "**Cultura** y **ciencia e investigación**."),
 45: (["medio ambiente adecuado"], "**Medio ambiente** adecuado: derecho **y deber** de conservarlo."),
 46: (["patrimonio histórico, cultural y artístico"], "Conservación y enriquecimiento del **patrimonio histórico, cultural y artístico**."),
 47: (["derecho a disfrutar de una vivienda digna y adecuada"], f"{IMP} La **vivienda** (como la salud) es del **capítulo III**: se queda fuera de la protección del amparo y de la reserva de ley orgánica (→ V.7)."),
 48: (["juventud"], "**Participación de la juventud**."),
 49: (["personas con discapacidad"], "**Discapacidad**: artículo reformado en **2024** (→ I.2)."),
 50: (["tercera edad"], "**Pensiones** adecuadas y actualizadas y servicios sociales para la **tercera edad**."),
 51: (["consumidores y usuarios"], "**Consumidores y usuarios**."),
 52: (["organizaciones profesionales"], "**Organizaciones profesionales** con estructura interna **democrática**. Es el **último** artículo del capítulo III."),
}
PROXIMO = {}
def arts_lit(ap, nums):
    out = []
    for k, n in enumerate(nums, 1):
        res, nota = NOTAS[n]
        out.append(unidad(f"{ap}.{k} Art. {n} · {rubrica(n)}", lit("CE", f"a{n}", res), nota))
    return "\n\n".join(out)

T.ap("bIII", "III. ¿De qué trata cada artículo? Los artículos 1 a 55", donde(
  "Tercera pregunta. La Constitución no pone título a sus artículos: los títulos que se usan para estudiar son una ayuda. Aquí tienes **de qué trata cada uno** y, debajo, su **texto literal** para la **lectura profunda** que pide el módulo.",
  ["1 Cómo estudiar los artículos", "2 Cuadro: de qué trata cada artículo", "3 a 7 Lectura profunda del texto literal, por unidades"]))

T.ap("s9", "III.1 Cómo estudiar los artículos 1 a 55", f"""
{IMP} **Primera meta:** saber **de qué trata cada artículo** y **dónde está** en la estructura. Preguntan directamente cosas como «¿qué regula el artículo 20?» (la libertad de expresión). La Constitución es la única norma por la que se pregunta así.

- **Del 1 al 38 y del 53 al 55: hay que saber de qué trata cada uno.** Las preguntas se resuelven con eso.
- **Del 39 al 52** (principios rectores): también conviene saber de qué tratan, sobre todo para **distinguirlos de los derechos** de los capítulos anteriores. Los examinadores intentan **meter como derechos fundamentales** cosas que no lo son: la salud, la vivienda, la redistribución de la renta, la **propiedad privada**… (→ V.7).
- A la vez, **ubícalos**: cuando leas el art. 12 pregúntate «¿dónde estaba?» (capítulo I del título I). Ponerte a prueba así es la forma de aprender la estructura.
- Segunda meta, en vueltas posteriores: la **lectura profunda** de los 55 artículos hasta captar la «música», de modo que una palabra cambiada te haga saltar la alarma. **No hace falta saberlos literalmente.**
- Para entrenarlo, usa el {ir("#/ce/test", "🧭 Test Constitución")}: te sale el número y tienes que decir de qué trata.

{ir("#/ce/texto", "📜 Constitución completa")} {ir("#/ce/organigrama", "🗺 Organigrama")}
""", 2)

T.ap("s10", "III.2 Cuadro: de qué trata cada artículo (1 a 55)", f"""
Cada artículo lleva el **color** de su título, capítulo o sección. Los títulos son los de la guía M101 (no son texto de la Constitución).

### {tag("P", "Título preliminar")} · arts. 1 a 9

{tabla_arts(range(1, 10))}

### {tag("I", "Título I")} · art. 10 y {tag("I.1", "capítulo primero")} (arts. 11 a 13)

{tabla_arts(range(10, 14))}

### {tag("I.2", "Capítulo segundo")} · art. 14 y {tag("I.2.1", "sección 1.ª")} (arts. 15 a 29) {IMP}

{tabla_arts(range(14, 30))}

### {tag("I.2.2", "Sección 2.ª")} · arts. 30 a 38

{tabla_arts(range(30, 39))}

### {tag("I.3", "Capítulo tercero")} · arts. 39 a 52

{tabla_arts(range(39, 53))}

### {tag("I.4", "Capítulo cuarto")} y {tag("I.5", "quinto")} · arts. 53 a 55

| Art. | De qué trata |
|---|---|
| {tag("I.4", "Art. 53")} | Vinculación de los poderes públicos, reserva de ley y tutela de los derechos (→ V) |
| {tag("I.4", "Art. 54")} | El Defensor del Pueblo (→ VIII) |
| {tag("I.5", "Art. 55")} | Suspensión de derechos y libertades (→ VI) |

*Los arts. 53 a 55 no figuran en la tabla de la guía: el rótulo es nuestro.*
""", 2)

T.ap("s11", "III.3 Lectura profunda: Título preliminar (arts. 1 a 9)", f"""
Es el {tag("P", "Título preliminar")}: no tiene nombre. Sienta los **principios del Estado**: forma, valores, soberanía, unidad y autonomía, lenguas, símbolos, capital, partidos, sindicatos, Fuerzas Armadas y sujeción a la Constitución.

{arts_lit("3", range(1, 10))}
""", 2)

T.ap("s12", "III.4 Lectura profunda: art. 10 y capítulo primero (arts. 10 a 13)", f"""
{tag("I", "Título I")}: «De los derechos y deberes fundamentales». El **art. 10** va fuera de los capítulos; el {tag("I.1", "capítulo primero")} trata «de los españoles y los extranjeros».

{arts_lit("4", range(10, 14))}
""", 2)

T.ap("s13", "III.5 Lectura profunda: art. 14 y sección 1.ª (arts. 14 a 29)", f"""
{IMP} Los derechos de la {tag("I.2.1", "sección 1.ª")} (arts. **15 a 29**) son los **derechos fundamentales y libertades públicas**: los que tienen **más garantías** (→ IV). El art. 14 va aparte.

{arts_lit("5", range(14, 30))}
""", 2)

T.ap("s14", "III.6 Lectura profunda: sección 2.ª (arts. 30 a 38)", f"""
La {tag("I.2.2", "sección 2.ª")}, «De los derechos y deberes de los ciudadanos», reúne **derechos y deberes** con menos garantías que la sección 1.ª: vinculan a los poderes públicos y se protegen con el recurso de inconstitucionalidad, pero **no** tienen reserva de ley orgánica, ni tutela preferente y sumaria, ni amparo (salvo el art. **30.2**).

{arts_lit("6", range(30, 39))}
""", 2)

T.ap("s15", "III.7 Lectura profunda: capítulo tercero (arts. 39 a 52)", f"""
El {tag("I.3", "capítulo tercero")}, «De los principios rectores de la política social y económica», contiene **principios**, no derechos fundamentales: orientan a los poderes públicos, pero solo se pueden alegar ante la jurisdicción ordinaria **según lo que digan las leyes que los desarrollen** (art. 53.3, → V.7).

{arts_lit("7", range(39, 53))}
""", 2)

# =============================================================================
# IV. NIVELES DE PROTECCIÓN · V. GARANTÍAS
def lx(k, idb, num, resaltar=(), solo=None, extra=""):
    return lit(k, idb, resaltar, solo=solo, titulo=f"Artículo {num}{extra} ({CORTO[k]})")
SI, NO = "✔", "✘"
T.ap("bIV", "IV. Derechos y deberes fundamentales: los niveles de protección", donde(
  "Cuarta pregunta. El Título I no protege igual todos sus artículos: hay **niveles de protección**. Saber a qué artículo corresponde cada garantía es la clave del tema: **las preguntas se resuelven con el cuadro** del apartado IV.2.",
  ["1 Qué contiene el Título I", "2 Cuadro de contenido y garantías", "3 Los deberes"]))

T.ap("s16", "IV.1 Qué contiene el Título I", f"""
{tag("I", "Título I")} se llama **«De los derechos y deberes fundamentales»** (arts. **10 a 55**) y reúne tres cosas: **los derechos y deberes** (arts. 10 a 52), **sus garantías** (cap. IV, arts. 53 y 54) y **su suspensión** (cap. V, art. 55).

Lo primero que hay que entender es que **no todo lo que está en el Título I es un «derecho fundamental»**. El nombre se reserva a los de la {tag("I.2.1", "sección 1.ª")} del capítulo II: «**De los derechos fundamentales y de las libertades públicas**» (arts. 15 a 29). Los demás son derechos y principios con **menos garantías**:

{tabla(["Nivel", "Dónde está", "Qué son", "Garantías"], [
  ["**1.º · Máximo**", f"{tag('I.2.1', 'Sección 1.ª')} · arts. **15 a 29**", "**Derechos fundamentales y libertades públicas**", "**Todas**: ley orgánica, ley, tutela preferente y sumaria, amparo, inconstitucionalidad, vinculación"],
  ["**2.º · Igualdad**", f"{tag('I.2', 'Art. 14')}", "Igualdad ante la ley", "Todas **menos la ley orgánica**: tutela preferente y sumaria, amparo, inconstitucionalidad, vinculación"],
  ["**3.º · Derechos y deberes de los ciudadanos**", f"{tag('I.2.2', 'Sección 2.ª')} · arts. **30 a 38**", "Derechos y deberes", "Vinculación, ley e inconstitucionalidad. **Amparo solo para el art. 30.2**"],
  ["**4.º · Principios rectores**", f"{tag('I.3', 'Capítulo III')} · arts. **39 a 52**", "**Principios**, no derechos fundamentales", "Solo **informan** la legislación, la práctica judicial y la actuación de los poderes públicos; se alegan **según las leyes**"],
  ["Fuera de estos niveles", f"{tag('I', 'Art. 10')} y {tag('I.1', 'capítulo I')} (arts. 11 a 13)", "Fundamento del orden político; nacionalidad y extranjeros", "No están en las garantías del art. 53; los protege el **Defensor del Pueblo** como todo el Título I"]])}

{IMP} **Ojo con lo que intentan colar:** el **derecho al trabajo** (35), la **propiedad privada** (33), la **salud** (43), la **vivienda** (47) o la redistribución equitativa de la renta (40) **no son derechos fundamentales** (los dos primeros son de la sección 2.ª; los demás, del capítulo III).
""", 2)

T.ap("s17", "IV.2 Cuadro de contenido y garantías", f"""
El cuadro cruza **cada unidad del Título I** con **cada garantía**. {IMP} Es **lo más preguntable**: «¿qué derechos pueden ser objeto de recurso de amparo?», «¿cuáles se regulan por ley orgánica?»…

{tabla(["Unidad", "Ley orgánica (art. 81.1)", "Solo por ley (53.1)", "Tutela ordinaria preferente y sumaria (53.2)", "Amparo (53.2)", "Inconstitucionalidad (53.1)", "Vinculan a los poderes públicos (53.1)", "Defensor del Pueblo (54)"], [
  [f"{tag('I', 'Art. 10')} y {tag('I.1', 'cap. I')} (10-13)", NO, NO, NO, NO, NO, NO, SI],
  [f"{tag('I.2', 'Art. 14')}", NO, SI, SI, SI, SI, SI, SI],
  [f"{tag('I.2.1', 'Sección 1.ª')} (15-29)", SI, SI, SI, SI, SI, SI, SI],
  [f"{tag('I.2.2', 'Art. 30.2')} (objeción de conciencia)", NO, SI, NO, SI, SI, SI, SI],
  [f"{tag('I.2.2', 'Sección 2.ª')} (resto: 30-38)", NO, SI, NO, NO, SI, SI, SI],
  [f"{tag('I.3', 'Capítulo III')} (39-52)", NO, NO, NO, NO, NO, "Informan (53.3)", SI]])}

**Cómo leer el cuadro (basado en los arts. 53, 54 y 81):**

- **Por ley orgánica:** solo la **sección 1.ª** (arts. 15 a 29). *Ojo con el art. 81.1: «y las demás previstas en la Constitución»*: hay leyes orgánicas por otras razones (→ V.1).
- **Tutela ante los tribunales ordinarios (preferente y sumaria):** el **art. 14 + la sección 1.ª**.
- **Recurso de amparo:** el **art. 14 + la sección 1.ª + el art. 30.2**.
- **Defensor del Pueblo:** **todo el Título I**.
- **Recurso de inconstitucionalidad y vinculación a los poderes públicos:** todo el **capítulo II** (arts. **14 a 38**).

!> {IMP} **Mnemotecnia de las tres garantías «fuertes»:** la **sección 1.ª (15-29)** las tiene **todas**. El **art. 14** las tiene todas **menos la ley orgánica**. Y el **30.2** solo tiene **amparo** de entre las especiales. Todo lo demás del capítulo II solo vincula, exige ley y puede llegar al **TC por inconstitucionalidad**.

{ir("#/ce/organigrama", "🗺 Ver el organigrama")}
""", 2)

T.ap("s18", "IV.3 Los deberes del Título I", f"""
El título habla de **derechos y deberes**. Los deberes que aparecen en sus artículos son pocos y se reconocen por la palabra «**deber**» en el texto:

{tabla(["Artículo", "Deber", "Texto literal"], [
  [tag("I.2.2", "Art. 30"), "**Defender a España** (y obligaciones militares, objeción de conciencia, servicio civil, grave riesgo o catástrofe)", c("CE", "a30", "Los españoles tienen el derecho y el deber de defender a España")],
  [tag("I.2.2", "Art. 31"), "**Contribuir** al sostenimiento de los gastos públicos", c("CE", "a31", "Todos contribuirán al sostenimiento de los gastos públicos de acuerdo con su capacidad económica")],
  [tag("I.2.2", "Art. 35"), "**Trabajar** (junto al derecho al trabajo)", c("CE", "a35", "Todos los españoles tienen el deber de trabajar y el derecho al trabajo")],
  [tag("I.3", "Art. 45"), "**Conservar el medio ambiente**", c("CE", "a45", "el deber de conservarlo")]])}

Fuera del Título I, el **art. 3.1** impone a todos los españoles el **deber de conocer el castellano**.
""", 2)

# ----------------------------------------------------------------------------- V
T.ap("bV", "V. ¿Cómo se garantizan los derechos? Los mecanismos (arts. 53, 54 y 81)", donde(
  "Quinta pregunta. La Constitución no se limita a reconocer los derechos: dispone **mecanismos para protegerlos**. Se estudian **en este orden**, y después se relaciona cada mecanismo con los artículos que protege (cuadro IV.2).",
  ["1 Reserva de ley (orgánica y ordinaria)", "2 Tutela ante los tribunales ordinarios", "3 Recurso de amparo", "4 Defensor del Pueblo", "5 Recurso de inconstitucionalidad", "6 Vinculación de los poderes públicos", "7 La paradoja del capítulo III", "8 Cuadro resumen"]))

T.ap("s19", "V.1 Reserva de ley: orgánica y ordinaria", f"""
Los derechos son cosas importantes que **no puede regular un reglamento**: solo una **ley**. Hay dos niveles de reserva:

{unidad("1.1 Reserva de ley en todo el capítulo II (art. 53.1)",
  lit("CE", "a53", ["vinculan a todos los poderes públicos", "Sólo por ley", "deberá respetar su contenido esencial", "artículo 161, 1, a)"], solo=[1]),
  fichab("Regulación del ejercicio de los derechos y libertades del capítulo II",
         "**Cualquier derecho del capítulo II** (arts. 14 a 38)",
         ["**Solo por ley**, nunca por reglamento", "Respetando siempre su **contenido esencial**"],
         "—",
         "La reserva de ley (ordinaria) es para **todo el capítulo II**; la de **ley orgánica**, solo para la sección 1.ª."))}

{unidad("1.2 Reserva de ley orgánica (art. 81)",
  lit("CE", "a81", ["desarrollo de los derechos fundamentales y de las libertades públicas", "y las demás previstas en la Constitución", "mayoría absoluta del Congreso"], solo=[1, 2]),
  fichab("Leyes orgánicas",
         "Las Cortes Generales; el Congreso, por mayoría absoluta",
         ["Desarrollo de los **derechos fundamentales y libertades públicas** = **sección 1.ª (arts. 15 a 29)**", "Estatutos de Autonomía y régimen electoral general", "**Y las demás previstas en la Constitución**"],
         "**Mayoría absoluta del Congreso** en una votación final sobre el conjunto del proyecto",
         f"{IMP} Del título I, **solo los arts. 15 a 29** van por ley orgánica; el resto, por **ley ordinaria**. El 81.1 termina con «**y las demás previstas en la Constitución**»: hay otras leyes orgánicas que no son de derechos."))}

**Otras leyes orgánicas previstas en la propia Constitución**, que no están en el art. 81 (y por eso se pregunta):

{tabla(["Artículo", "Ley orgánica de…", "Literal"], [
  [tag("P", "Art. 8.2"), "Bases de la organización militar (Fuerzas Armadas)", c("CE", "a8", "Una ley orgánica regulará las bases de la organización militar")],
  [tag("I.4", "Art. 54"), "El Defensor del Pueblo", c("CE", "a54", "Una ley orgánica regulará la institución del Defensor del Pueblo")],
  [tag("IV", "Art. 116.1"), "Estados de alarma, de excepción y de sitio", c("CE", "a116", "Una ley orgánica regulará los estados de alarma, de excepción y de sitio")],
  [tag("IX", "Art. 165"), "El Tribunal Constitucional", c("CE", "a165", "Una ley orgánica regulará el funcionamiento del Tribunal Constitucional")]])}

!> {IMP} **Atención a la «ley de igualdad».** El vídeo del módulo dice que la ley de igualdad entre mujeres y hombres va por ley orgánica aunque el art. 14 quede fuera de la sección 1.ª. Es cierto que se llama **Ley Orgánica 3/2007**, pero **no toda ella** tiene ese carácter, según su propia disposición final:
{lit("LO3_2007", "dfsegunda", ["disposiciones adicionales primera, segunda y tercera", "El resto de los preceptos contenidos en esta Ley no tienen tal carácter"], solo=[0, 1], titulo="Disposición final segunda (LO 3/2007)")}
""", 2)

T.ap("s20", "V.2 Tutela ante los tribunales ordinarios (procedimiento preferente y sumario)", f"""
{unidad("2.1 Qué dice el art. 53.2",
  lit("CE", "a53", ["Cualquier ciudadano podrá recabar la tutela", "artículo 14 y la Sección primera del Capítulo segundo", "preferencia y sumariedad"], solo=[2]),
  fichab("Tutela ordinaria de los derechos",
         "**Cualquier ciudadano**",
         ["Ante los **tribunales ordinarios**", "Por un procedimiento **preferente y sumario** (rápido y prioritario)"],
         "—",
         f"{IMP} Cubre el **art. 14 y la sección 1.ª** (arts. 15 a 29); **no** el resto del capítulo II. Después, y «en su caso», cabe el **amparo** ante el Tribunal Constitucional (→ V.3)."))}

{unidad("2.2 El procedimiento en la jurisdicción contencioso-administrativa",
  lit("LJCA", "a114", ["procedimiento de amparo judicial", "artículo 53.2 de la Constitución"], solo=[1], titulo="Artículo 114.1 (LJCA)"),
  lit("LJCA", "a115", ["diez días"], solo=[1], titulo="Artículo 115.1 (LJCA)"),
  "En el orden contencioso-administrativo, este procedimiento se llama **«de protección de los derechos fundamentales»** y tiene un **plazo de diez días** para recurrir.")}
""", 2)

T.ap("s21", "V.3 El recurso de amparo", f"""
Es **el último remedio**: se acude al Tribunal Constitucional **cuando ya se ha agotado la vía judicial** (el procedimiento preferente y sumario y los recursos que quepan).

{unidad("3.1 Qué derechos protege (arts. 53.2 y 161.1.b CE; art. 41 LOTC)",
  lit("CE", "a53", ["recurso de amparo ante el Tribunal Constitucional", "objeción de conciencia reconocida en el artículo 30"], solo=[2], titulo="Artículo 53.2 (amparo)"),
  lx("LOTC", "acuarentayuno", 41, ["artículos catorce a veintinueve de la Constitución", "objeción de conciencia reconocida en el artículo treinta"], solo=[1, 2]),
  fichab("Recurso de amparo constitucional",
         "Persona natural o jurídica con interés legítimo, **Defensor del Pueblo** y **Ministerio Fiscal** (art. 162.1.b CE; art. 46 LOTC)",
         ["Frente a violaciones de los derechos de los **arts. 14 a 29** y de la **objeción de conciencia (art. 30.2)**", "Por disposiciones, actos, omisiones o vía de hecho de los poderes públicos"],
         ["Plazos según el origen de la violación (→ 3.2)", "Se admite solo si tiene **especial trascendencia constitucional** (art. 50.1.b LOTC)"],
         f"{IMP} Amparo: **14 + 15 a 29 + 30.2**. Los derechos de la sección 2.ª (salvo el 30.2) y los principios del capítulo III **no** tienen amparo."))}

{unidad("3.2 Los plazos (arts. 42, 43 y 44 LOTC)",
  lx("LOTC", "acuarentaydos", 42, ["tres meses"]),
  lx("LOTC", "acuarentaytres", 43, ["agotado la vía judicial procedente", "veinte días"], solo=[1, 2]),
  lx("LOTC", "acuarentaycuatro", 44, ["Que se hayan agotado todos los medios de impugnación", "30 días"], solo=[1, 2, 3, 4, 5]),
  tabla(["Origen de la violación", "Plazo", "Desde cuándo", "Art. LOTC"], [
    ["Decisiones o actos **sin valor de ley** de las **Cortes** o de las **Asambleas legislativas de las CCAA** (o sus órganos)", "**3 meses**", "Desde que sean **firmes** según las normas internas de la Cámara o Asamblea", "**42**"],
    ["Actos u omisiones del **Gobierno** o de sus autoridades o funcionarios, o de los **órganos ejecutivos colegiados de las CCAA** (o sus autoridades o funcionarios)", "**20 días**", "Desde la notificación de la resolución del **previo proceso judicial** (tras agotar la vía judicial)", "**43**"],
    ["Acto u omisión de un **órgano judicial**", "**30 días**", "Desde la notificación de la resolución del proceso judicial (tras agotar los medios de impugnación)", "**44**"]]),
  f"!> {IMP} **Tres plazos, tres orígenes:** **3 meses** (Cortes y Asambleas), **20 días** (Gobierno y CCAA, tras la vía judicial) y **30 días** (órgano judicial, ¡con la vía judicial agotada!). Lo más preguntable es el de **30 días** y el de **20 días**.")}

{unidad("3.3 Quién lo interpone y cómo se admite (art. 46 y 50 LOTC)",
  lx("LOTC", "acuarentayseis", 46, ["la persona directamente afectada, el Defensor del Pueblo y el Ministerio Fiscal", "quienes hayan sido parte en el proceso judicial correspondiente, el Defensor del Pueblo y el Ministerio Fiscal"], solo=[1, 2, 3]),
  lx("LOTC", "acincuenta", 50, ["especial trascendencia constitucional"], solo=[1, 2, 3, 4, 5, 6], extra=".1"))}
""", 2)

T.ap("s22", "V.4 El Defensor del Pueblo (art. 54)", f"""
{unidad("4.1 El art. 54",
  lit("CE", "a54", ["alto comisionado de las Cortes Generales", "los derechos comprendidos en este Título", "supervisar la actividad de la Administración"]),
  fichab("Garantía institucional de los derechos",
         "El **Defensor del Pueblo**, alto comisionado de las Cortes Generales",
         ["Defiende **los derechos comprendidos en el Título I** (arts. 10 a 52: todos los que haya en el título)", "Supervisa la actividad de la **Administración**, dando cuenta a las Cortes Generales"],
         "—",
         f"{IMP} Defiende **todo el Título I**, no solo la sección 1.ª. Su regulación va por **ley orgánica** (→ VIII)."))}

El Defensor del Pueblo tiene su propio apartado completo más adelante (→ VIII).
""", 2)

T.ap("s23", "V.5 El recurso de inconstitucionalidad", f"""
{unidad("5.1 Qué es y quién lo interpone (arts. 53.1, 161.1.a y 162.1.a CE; art. 32 LOTC)",
  lit("CE", "a161", ["recurso de inconstitucionalidad contra leyes y disposiciones normativas con fuerza de ley"], solo=[1, 2]),
  lit("CE", "a162", ["el Presidente del Gobierno, el Defensor del Pueblo, 50 Diputados, 50 Senadores, los órganos colegiados ejecutivos de las Comunidades Autónomas y, en su caso, las Asambleas de las mismas"], solo=[1, 2]),
  lx("LOTC", "atreintaydos", 32, ["El Presidente del Gobierno", "El Defensor del Pueblo", "Cincuenta Diputados", "Cincuenta Senadores", "previo acuerdo adoptado al efecto"]),
  fichab("Recurso de inconstitucionalidad ante el Tribunal Constitucional",
         ["**Presidente del Gobierno**", "**Defensor del Pueblo**", "**50 Diputados** y **50 Senadores**", "**Órganos ejecutivos** y **Asambleas** de las CCAA, solo contra leyes del Estado que afecten a su ámbito de autonomía"],
         "Contra **leyes y disposiciones normativas con fuerza de ley** (Estatutos, leyes orgánicas y ordinarias, decretos-leyes, decretos legislativos, tratados, reglamentos de las Cámaras)",
         ["**3 meses** desde la publicación de la norma (art. 33.1 LOTC)", "**9 meses** (Presidente del Gobierno y ejecutivos autonómicos) si hay Comisión Bilateral y acuerdo de negociaciones (art. 33.2 LOTC)"],
         "Protege **todo el capítulo II (arts. 14 a 38)** según el art. 53.1; pero el TC puede apoyar su fallo en **cualquier** precepto constitucional (art. 39.2 LOTC)."))}

{unidad("5.2 El plazo (art. 33 LOTC)",
  lx("LOTC", "atreintaytres", 33, ["tres meses", "nueve meses", "Comisión Bilateral de Cooperación"], solo=[1, 2, 3, 4, 5]),
  f"!> {IMP} **Plazo: 3 meses**, y **9 meses** si el Presidente del Gobierno o el ejecutivo autonómico han activado la **Comisión Bilateral** para negociar (conflictos Estado-CCAA). Se cuenta desde la **publicación** de la norma.")}
""", 2)

T.ap("s24", "V.6 Vinculación de los poderes públicos", f"""
{unidad("6.1 Todos los poderes públicos están vinculados",
  lit("CE", "a9", ["Los ciudadanos y los poderes públicos están sujetos a la Constitución"], solo=[1]),
  lit("CE", "a53", ["vinculan a todos los poderes públicos"], solo=[1]),
  fichab("Eficacia directa de los derechos del capítulo II",
         "**Todos los poderes públicos** (legislativo, ejecutivo, judicial y administraciones)",
         "Los derechos del **capítulo II** tienen **eficacia inmediata**: no necesitan una ley que los desarrolle para poder invocarse",
         "—",
         f"{IMP} **Vinculan** los derechos del **capítulo II (14 a 38)**. Los del **capítulo III** no vinculan igual: **informan** (→ V.7)."))}
""", 2)

T.ap("s25", "V.7 La paradoja del capítulo III: principios rectores", f"""
El {tag("I.3", "capítulo III")} se llama «**De los principios rectores de la política social y económica**» y contiene cosas tan importantes como la **salud**, la **vivienda**, la **seguridad social** o el **medio ambiente**. Pero tiene una paradoja: **son derechos sobre el papel, con poca garantía**.

{unidad("7.1 El art. 53.3",
  lit("CE", "a53", ["informarán la legislación positiva, la práctica judicial y la actuación de los poderes públicos", "Sólo podrán ser alegados ante la Jurisdicción ordinaria de acuerdo con lo que dispongan las leyes que los desarrollen"], solo=[3]),
  fichab("Principios rectores del capítulo III",
         "Los **poderes públicos**",
         ["**Informan** la legislación positiva, la práctica judicial y la actuación de los poderes públicos", "Solo se **alegan ante la jurisdicción ordinaria** según las leyes que los desarrollen"],
         "Sin amparo, sin tutela preferente y sumaria, sin ley orgánica, sin recurso de inconstitucionalidad por reconocerlos como derechos; solo cuenta el **Defensor del Pueblo** (art. 54)",
         f"{IMP} **A diferencia** de los derechos del capítulo II, **no pueden exigirse sin una ley que los desarrolle**. Si no hay ley, aunque lo diga la Constitución, no hay acción."))}

{IMP} **Trampa típica:** te presentan como «derechos fundamentales» la **salud** (43), la **vivienda** (47), la **redistribución equitativa de la riqueza** (40) o la **propiedad privada** (33). **No lo son**: los tres primeros son principios del capítulo III; la propiedad privada es un derecho de la sección 2.ª (sin amparo). El **derecho al trabajo** (35), también de la sección 2.ª, tampoco es fundamental.
""", 2)

T.ap("s26", "V.8 Cuadro resumen de las garantías", f"""
{tabla(["Mecanismo", "Qué protege", "Norma", "Quién / ante quién"], [
  ["**Reserva de ley orgánica**", f"{tag('I.2.1', 'Sección 1.ª')} (15-29)", "Art. 81.1", "Cortes Generales; mayoría absoluta del Congreso"],
  ["**Reserva de ley**", f"{tag('I.2', 'Capítulo II')} (14-38), respetando el contenido esencial", "Art. 53.1", "Ley (nunca reglamento)"],
  ["**Tutela ante los tribunales ordinarios** (preferente y sumaria)", f"{tag('I.2', 'Art. 14')} + {tag('I.2.1', 'sección 1.ª')} (14-29)", "Art. 53.2", "Cualquier ciudadano · tribunales ordinarios"],
  ["**Recurso de amparo**", f"{tag('I.2', 'Art. 14')} + {tag('I.2.1', 'sección 1.ª')} + {tag('I.2.2', 'art. 30.2')} (14-29 y 30.2)", "Arts. 53.2 y 161.1.b", "Persona con interés legítimo, Defensor del Pueblo, Ministerio Fiscal · TC"],
  ["**Defensor del Pueblo**", f"{tag('I', 'Título I')} (10-52)", "Art. 54", "Alto comisionado de las Cortes Generales"],
  ["**Recurso de inconstitucionalidad**", f"{tag('I.2', 'Capítulo II')} (14-38)", "Arts. 53.1 y 161.1.a", "Presidente del Gobierno, Defensor del Pueblo, 50 Diputados, 50 Senadores, ejecutivos y asambleas autonómicas · TC"],
  ["**Vinculación de los poderes públicos**", f"{tag('I.2', 'Capítulo II')} (14-38)", "Art. 53.1", "Todos los poderes públicos"]])}

{IMP} **El capítulo III (39-52) solo se toca con el Defensor del Pueblo**: sus principios **informan** la actuación de los poderes públicos y se alegan ante la jurisdicción ordinaria según las leyes que los desarrollen (art. 53.3).
""", 2)

# =============================================================================
# VI. SUSPENSIÓN
T.ap("bVI", "VI. ¿Cómo se suspenden los derechos? Estados de alarma, excepción y sitio (arts. 55 y 116)", donde(
  "Sexta pregunta. La Constitución protege los derechos, pero **se reserva la carta de poder suspenderlos** en situaciones graves. Es el art. 55 (capítulo V, el último del Título I). " + IMP + " **Es muy preguntable: se pregunta por palabras clave y hay que dominarlo bien.**",
  ["1 El art. 55, ordenado", "2 Los tres estados: quién declara y cuánto dura", "3 Qué derechos se pueden suspender", "4 Puntos en común", "5 La suspensión individual (art. 55.2)", "6 Cuadro resumen"]))

T.ap("s27", "VI.1 El art. 55, ordenado", f"""
El art. 55 es un artículo «lioso»: dice «los derechos reconocidos en los artículos 17, 18, apartados 2 y 3, artículos 19…». Leído así no se entiende. Por eso conviene **ordenarlo**: lo que dice, en dos bloques.

{lit("CE", "a55", ["podrán ser suspendidos cuando se acuerde la declaración del estado de excepción o de sitio", "Se exceptúa de lo establecido anteriormente el apartado 3 del artículo 17 para el supuesto de declaración de estado de excepción", "Una ley orgánica podrá determinar", "bandas armadas o elementos terroristas"], solo=[1, 2, 3])}

{tabla(["", "Suspensión **general** (art. 55.1)", "Suspensión **individual** (art. 55.2)"], [
  ["**Cuándo**", "Al **declararse** el estado de **excepción o de sitio**", "**Ley orgánica**, para **personas determinadas**"],
  ["**Alcance**", "**General** (la guía M101 la llama «suspensión general»): se aplica en el ámbito de la declaración", "**Individual**: solo en relación con la actuación de **bandas armadas o elementos terroristas**"],
  ["**Derechos**", "**17**, **18.2**, **18.3**, **19**, **20.1.a)**, **20.1.d)**, **20.5**, **21**, **28.2** y **37.2** (salvo el **17.3** en excepción)", "**17.2**, **18.2** y **18.3**"],
  ["**Garantías**", "Declaración del estado en los términos de la Constitución (art. 116)", "**Intervención judicial** necesaria y **control parlamentario** adecuado"]])}

!> {IMP} **Es el artículo 55 de la Constitución y el capítulo es el quinto**: el art. **55** está en el capítulo **V**, el último del Título I. Las dos cifras son un cinco (5-5).
""", 2)

T.ap("s28", "VI.2 Los tres estados: quién declara y cuánto dura (art. 116)", f"""
Hay **tres estados**, de menor a mayor gravedad: **alarma < excepción < sitio**. La Constitución solo regula lo esencial (art. 116) y **una ley orgánica** lo desarrolla: la **LO 4/1981**.

{lit("CE", "a116", ["Una ley orgánica regulará los estados de alarma, de excepción y de sitio"], solo=[1], titulo="Artículo 116.1")}

{tabla(["", f"{tag('IV', 'ALARMA')}", f"{tag('I.5', 'EXCEPCIÓN')}", f"{tag('X', 'SITIO')}"], [
  ["**Quién declara**", "El **Gobierno**, por **decreto** del Consejo de Ministros", "El **Gobierno**, por **decreto** del Consejo de Ministros, **previa autorización del Congreso**", "El **Congreso**, por **mayoría absoluta**, **a propuesta exclusiva del Gobierno**"],
  ["**Papel del Congreso**", "Se le **da cuenta** (reunido inmediatamente)", "**Autoriza** antes", "**Declara**"],
  ["**Duración**", "**No más de 15 días**", "**No más de 30 días**", "**La que determine el Congreso**"],
  ["**Prórroga**", "Solo con **autorización** del Congreso", "**Otro plazo igual** (30 días), con los **mismos requisitos**", "La que fije el Congreso"],
  ["**Derechos**", "**No se suspende ninguno** (solo limitaciones)", "Se **suspenden** los del art. 55.1, **salvo el 17.3**", "Se **suspenden** los del art. 55.1, **incluido el 17.3**"],
  ["**Artículos**", "CE 116.2; LO 4/1981, arts. 4 a 12", "CE 116.3; LO 4/1981, arts. 13 a 31", "CE 116.4; LO 4/1981, arts. 32 a 36"]])}

{unidad("2.1 Estado de alarma (art. 116.2 CE; art. 6 LO 4/1981)",
  lit("CE", "a116", ["declarado por el Gobierno mediante decreto acordado en Consejo de Ministros por un plazo máximo de quince días", "dando cuenta al Congreso de los Diputados", "sin cuya autorización no podrá ser prorrogado dicho plazo"], solo=[2], titulo="Artículo 116.2"),
  lx("LOEAS", "asexto", 6, ["decreto acordado en Consejo de Ministros", "no podrá exceder de quince días", "Sólo se podrá prorrogar con autorización expresa del Congreso de los Diputados"], solo=[1, 2]),
  lx("LOEAS", "acuao", 4, ["Catástrofes, calamidades o desgracias públicas", "Crisis sanitarias", "Paralización de servicios públicos esenciales", "desabastecimiento de productos de primera necesidad"], solo=[1, 2, 3, 4, 5]),
  lx("LOEAS", "aonce", 11, ["Limitar la circulación o permanencia de personas o vehículos", "requisas temporales", "prestaciones personales obligatorias"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Estado de alarma",
         ["**Gobierno** (decreto del Consejo de Ministros)", "El Presidente de la CA puede **solicitarlo** si solo afecta a su territorio (art. 5 LO 4/1981)"],
         ["Se declara ante **catástrofes, crisis sanitarias, paralización de servicios esenciales o desabastecimiento** (art. 4 LO 4/1981)", "El decreto determina **ámbito territorial, duración y efectos**", "Admite **limitaciones** (circulación, requisas, prestaciones, intervención de industrias, racionamiento…), **no suspensión de derechos**"],
         ["**15 días**", "Prórroga **solo con autorización expresa del Congreso**, que puede fijar el alcance y las condiciones"],
         f"{IMP} En el alarma el Gobierno **da cuenta** al Congreso, pero **la prórroga necesita su autorización**. **Ningún derecho se suspende**: solo se **limitan** algunos."))}

{unidad("2.2 Estado de excepción (art. 116.3 CE; arts. 13 y 14 LO 4/1981)",
  lit("CE", "a116", ["previa autorización del Congreso de los Diputados", "que no podrá exceder de treinta días, prorrogables por otro plazo igual, con los mismos requisitos"], solo=[3], titulo="Artículo 116.3"),
  lx("LOEAS", "atrece", 13, ["solicitar del Congreso de los Diputados autorización para declarar el estado de excepción", "que no podrá exceder de treinta días"], solo=[1, 2, 3, 4, 5, 6, 7]),
  fichab("Estado de excepción",
         ["**Gobierno** (decreto en Consejo de Ministros) **con autorización previa del Congreso**", "El Congreso puede aprobar la solicitud **o modificarla**"],
         ["Se declara cuando el ejercicio de los **derechos y libertades**, las **instituciones democráticas**, los **servicios públicos esenciales** u otro aspecto del **orden público** estén tan alterados que las potestades ordinarias no basten", "La solicitud al Congreso incluye los **derechos cuya suspensión se pide** (solo los del art. 55.1), las medidas, el ámbito y la duración"],
         ["**30 días**", "Prorrogable por **otro plazo igual**, con los **mismos requisitos**"],
         f"{IMP} Declara el **Gobierno**, pero **con autorización previa del Congreso** (en alarma, el Congreso solo recibe cuenta). La autorización y la proclamación deben **determinar los efectos, el ámbito territorial y la duración**."))}

{unidad("2.3 Estado de sitio (art. 116.4 CE; art. 32 LO 4/1981)",
  lit("CE", "a116", ["declarado por la mayoría absoluta del Congreso de los Diputados, a propuesta exclusiva del Gobierno", "El Congreso determinará su ámbito territorial, duración y condiciones"], solo=[4], titulo="Artículo 116.4"),
  lx("LOEAS", "atreintaydos", 32, ["podrá proponer al Congreso de los Diputados la declaración de estado de sitio", "determinará el ámbito territorial, duración y condiciones", "suspensión temporal de las garantías jurídicas del detenido"], solo=[1, 2, 3]),
  fichab("Estado de sitio",
         "**El Congreso**, por **mayoría absoluta**, y solo **a propuesta del Gobierno**",
         ["Se declara ante una **insurrección o acto de fuerza** contra la soberanía o independencia de España, su integridad territorial o el ordenamiento constitucional, que no pueda resolverse por otros medios", "Puede suspender, además, las **garantías jurídicas del detenido** (art. 17.3)"],
         ["**La que determine el Congreso**", "El Congreso fija también el ámbito territorial y las condiciones"],
         f"{IMP} En el sitio **declara el Congreso** (en los otros dos, el Gobierno). Es el **único** en que se pueden suspender las garantías del detenido (**17.3**)."))}

!> {IMP} **Fíjate bien en «quién declara» y «cómo»:** **alarma** → Gobierno, *dando cuenta* al Congreso; **excepción** → Gobierno, *con autorización previa* del Congreso; **sitio** → Congreso, *mayoría absoluta*, *a propuesta exclusiva* del Gobierno. Todo se mueve **entre Gobierno y Congreso**.

**Regla mnemotécnica: 15 – 30 – lo decide el Congreso.** Alarma, 15 días; excepción, 30 días (+30); sitio, el tiempo que decida el Congreso.
""", 2)

T.ap("s29", "VI.3 Qué derechos se pueden suspender en cada estado", f"""
El art. 55.1 enumera los derechos **suspendibles** y el art. 116 dice que solo en **excepción y sitio**. Combinando ambos:

{tabla(["Derecho (art.)", "Alarma", "Excepción", "Sitio"], [
  ["**17** · Libertad y seguridad (detención…)", NO, SI, SI],
  ["**17.3** · Derechos del detenido (información, no declarar, abogado)", NO, f"**{NO}**", f"**{SI}**"],
  ["**18.2** · Inviolabilidad del domicilio", NO, SI, SI],
  ["**18.3** · Secreto de las comunicaciones", NO, SI, SI],
  ["**19** · Libertad de residencia y de circulación", NO, SI, SI],
  ["**20.1.a)** y **d)** · Libertad de expresión e información", NO, SI, SI],
  ["**20.5** · Secuestro de publicaciones solo por resolución judicial", NO, SI, SI],
  ["**21** · Derecho de reunión y manifestación", NO, SI, SI],
  ["**28.2** · Huelga", NO, SI, SI],
  ["**37.2** · Conflicto colectivo", NO, SI, SI]])}

{IMP} **El matiz del 17.3.** El art. 55.1 exceptúa el **apartado 3 del art. 17** «para el supuesto de declaración de estado de excepción». Es decir: en **excepción** el detenido **conserva** sus garantías (información inmediata, no ser obligado a declarar, abogado); en **sitio** pueden **suspenderse**.

{unidad("3.1 Por qué importa el 17.3: lo que dice el art. 17.3",
  lit("CE", "a17", ["Toda persona detenida debe ser informada de forma inmediata", "no pudiendo ser obligada a declarar", "asistencia de abogado"], solo=[3]),
  lx("LOEAS", "adieciseis", 16, ["La detención no podrá exceder de diez días", "los derechos que les reconoce el artículo diecisiete, tres, de la Constitución"], solo=[1]))}

Dos ideas para ayudarte a recordar la lista: **tiene sentido** que se puedan restringir justo estas libertades (circulación, reunión, huelga, comunicaciones, domicilio…) cuando el problema es de **orden público**; no se limitan «a tochomocho».

*Alarma no suspende derechos:* el decreto de alarma solo permite **limitaciones**, como limitar la circulación, requisar bienes o racionar servicios (→ VI.2, art. 11 LO 4/1981).
""", 2)

T.ap("s30", "VI.4 Puntos en común de los tres estados", f"""
{tabla(["Regla", "Qué dice", "Norma"], [
  ["**Ámbito territorial**", "No está preestablecido: lo **determina cada declaración** (decreto o autorización/declaración del Congreso)", "CE 116.2, 116.3 y 116.4"],
  ["**Congreso**", "**No puede disolverse** mientras dure el estado; si no estaba reunido, las Cámaras **quedan convocadas automáticamente**", "CE 116.5"],
  ["**Congreso disuelto o mandato expirado**", "Sus competencias las asume la **Diputación Permanente**", "CE 116.5"],
  ["**Funcionamiento**", "El de las Cámaras y el de los demás poderes constitucionales **no se interrumpe**", "CE 116.5; LO 4/1981, art. 1.4"],
  ["**Responsabilidad**", "No se modifica el principio de **responsabilidad del Gobierno y de sus agentes**", "CE 116.6"],
  ["**Publicación**", "Se publica **de inmediato en el BOE** y se difunde obligatoriamente por medios públicos y los privados que se determinen; **entra en vigor desde el instante de su publicación**", "LO 4/1981, art. 2"],
  ["**Reforma constitucional**", "**No puede iniciarse** durante ninguno de los tres estados (ni en tiempo de guerra)", "CE 169"],
  ["**Regulación**", "Por **ley orgánica**", "CE 116.1"]])}

{lit("CE", "a116", ["No podrá procederse a la disolución del Congreso", "quedando automáticamente convocadas las Cámaras", "no podrán interrumpirse", "las competencias del Congreso serán asumidas por su Diputación Permanente"], solo=[5, 6], titulo="Artículo 116.5")}

{lit("CE", "a116", ["no modificarán el principio de responsabilidad del Gobierno y de sus agentes"], solo=[7], titulo="Artículo 116.6")}

{lx("LOEAS", "asegundo", 2, ["publicada de inmediato en el «Boletín Oficial del Estado»", "difundida obligatoriamente por todos los medios de comunicación públicos y por los privados que se determinen", "entrará en vigor desde el instante mismo de su publicación"])}

{lit("CE", "a169", ["No podrá iniciarse la reforma constitucional en tiempo de guerra o de vigencia de alguno de los estados previstos en el artículo 116"])}

!> {IMP} **Para el examen:** no se puede **disolver el Congreso**, no se **interrumpe** el funcionamiento de las Cámaras ni de los poderes del Estado, no se modifica la **responsabilidad** de los poderes públicos, **no se puede reformar la Constitución** (ni siquiera en alarma) y todo se regula por **ley orgánica**.
""", 2)

T.ap("s31", "VI.5 La suspensión individual (art. 55.2)", f"""
Además de la suspensión general, el art. 55.2 permite una suspensión **individual** de algunos derechos, **para personas determinadas** y en relación con las investigaciones de la actuación de **bandas armadas o elementos terroristas**.

{tabla(["Derecho", "Qué se puede suspender", "Garantía"], [
  [tag("I.2.1", "Art. 17.2"), "La **duración máxima de la detención preventiva** (72 horas)", "**Intervención judicial** y **control parlamentario**"],
  [tag("I.2.1", "Art. 18.2"), "La **inviolabilidad del domicilio**", "Ley **orgánica**"],
  [tag("I.2.1", "Art. 18.3"), "El **secreto de las comunicaciones**", "Responsabilidad **penal** por uso injustificado o abusivo"]])}

{lit("CE", "a55", ["Una ley orgánica podrá determinar la forma y los casos en los que, de forma individual y con la necesaria intervención judicial y el adecuado control parlamentario", "La utilización injustificada o abusiva de las facultades reconocidas en dicha ley orgánica producirá responsabilidad penal"], solo=[2, 3], titulo="Artículo 55.2")}

!> {IMP} La suspensión individual afecta **solo** a tres derechos (**17.2, 18.2 y 18.3**), a diferencia de la general, que afecta a diez. Y siempre **con intervención judicial y control parlamentario**.
""", 2)

T.ap("s32", "VI.6 Cuadro resumen de la suspensión", f"""
{tabla(["Clase", "Supuesto", "Declaración", "Duración", "Derechos que se pueden suspender"], [
  ["**Suspensión general**", f"{tag('I.5', 'Excepción')}", "**Gobierno**, con **autorización del Congreso**", "**30 días**; prórroga por otro plazo igual", "**17** (salvo 17.3) · **18.2** · **18.3** · **19** · **20.1.a)** y **d)** y **20.5** · **21** · **28.2** · **37.2**"],
  ["**Suspensión general**", f"{tag('X', 'Sitio')}", "**Congreso**, mayoría absoluta, a propuesta exclusiva del Gobierno", "La determinada por el **Congreso**", "Los mismos **más el 17.3**"],
  ["**Limitación**", f"{tag('IV', 'Alarma')}", "**Gobierno**, dando cuenta al Congreso", "**15 días**; prórroga con autorización del Congreso", "**Ninguno** (solo se pueden decretar algunas limitaciones)"],
  ["**Suspensión individual**", "Bandas armadas y elementos terroristas (art. 55.2)", "Ley orgánica", "—", "**17.2** (duración máxima de la detención preventiva) · **18.2** · **18.3**"]])}

{resumen([
  "**Art. 55** (capítulo V): suspensión **general** (excepción y sitio: diez derechos, salvo el 17.3 en excepción) e **individual** (bandas armadas y terroristas: 17.2, 18.2, 18.3).",
  "**Quién declara:** alarma → Gobierno (da cuenta); excepción → Gobierno con autorización del Congreso; sitio → Congreso por mayoría absoluta a propuesta del Gobierno.",
  "**Duración:** alarma 15 días; excepción 30 (+30); sitio, la que fije el Congreso.",
  "**En común:** no se disuelve el Congreso, no se interrumpe el funcionamiento de las Cámaras, no se modifica la responsabilidad, no se reforma la Constitución; ley orgánica."], "Siguiente: VII. El Tribunal Constitucional (Título IX)")}
""", 2)

# =============================================================================
# VII. TRIBUNAL CONSTITUCIONAL
T.ap("bVII", "VII. El Tribunal Constitucional (Título IX, arts. 159 a 165)", donde(
  "Séptima pregunta. Tras ver cómo se garantizan los derechos, el **Tribunal Constitucional** es el órgano que garantiza la Constitución: quién lo compone, qué procesos conoce y qué valor tienen sus sentencias. La guía manda **leer detenidamente los arts. 159 a 165**.",
  ["1 Qué es el Tribunal Constitucional", "2 Composición y mandato", "3 Competencias y procedimientos", "4 Las sentencias", "5 Amparo frente a inconstitucionalidad"]))

T.ap("s33", "VII.1 Qué es el Tribunal Constitucional", f"""
{tag("IX", "Título IX")} se llama «**Del Tribunal Constitucional**» (arts. **159 a 165**).

{unidad("1.1 Naturaleza (art. 1 LOTC) y regulación (art. 165 CE)",
  lx("LOTC", "aprimero", 1, ["intérprete supremo de la Constitución", "es independiente de los demás órganos constitucionales", "sometido sólo a la Constitución y a la presente Ley Orgánica", "único en su orden"]),
  lit("CE", "a165", ["Una ley orgánica regulará el funcionamiento del Tribunal Constitucional"]),
  fichab("Tribunal Constitucional",
         "**Intérprete supremo** de la Constitución; **único en su orden**",
         ["**Independiente** de los demás órganos constitucionales", "Sometido **solo** a la Constitución y a su ley orgánica", "Jurisdicción en **todo el territorio**"],
         "—",
         f"{IMP} Está regulado por **ley orgánica** (la **LO 2/1979, del Tribunal Constitucional**, LOTC)."))}
""", 2)

T.ap("s34", "VII.2 Composición y mandato", f"""
{tabla(["Quién propone", "Cuántos", "Cómo", "Norma"], [
  ["**Congreso**", "**4**", "Mayoría de **tres quintos** de sus miembros", "CE 159.1"],
  ["**Senado**", "**4**", "Idéntica mayoría (3/5), **entre las candidaturas presentadas por las Asambleas Legislativas de las CCAA**", "CE 159.1; LOTC 16.1"],
  ["**Gobierno**", "**2**", "—", "CE 159.1"],
  ["**Consejo General del Poder Judicial**", "**2**", "—", "CE 159.1"],
  ["**Total**", "**12 miembros** nombrados **por el Rey**", "", "CE 159.1; LOTC 5"]])}

{unidad("2.1 Los 12 miembros (art. 159 CE)",
  lit("CE", "a159", ["12 miembros nombrados por el Rey", "cuatro a propuesta del Congreso por mayoría de tres quintos", "dos a propuesta del Gobierno, y dos a propuesta del Consejo General del Poder Judicial", "más de quince años de ejercicio profesional", "nueve años", "terceras partes cada tres", "independientes e inamovibles"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Composición y estatuto de los miembros",
         "**12 miembros**, nombrados por el **Rey**: 4 Congreso, 4 Senado, 2 Gobierno, 2 CGPJ",
         ["**Requisitos:** Magistrados y Fiscales, Profesores de Universidad, funcionarios públicos y Abogados, **juristas de reconocida competencia con más de 15 años** de ejercicio profesional", "Presencia **equilibrada** de mujeres y hombres: **al menos un 40 %** de cada sexo en las propuestas (art. 16.1 LOTC)"],
         ["**Mandato: 9 años**", "Renovación **por terceras partes cada 3 años**", "Sin nuevo mandato inmediato salvo que el cargo se hubiera ocupado **3 años o menos** (art. 16.4 LOTC)"],
         f"{IMP} **9 años** de mandato y renovación por **terceras partes cada 3**. Los miembros son **independientes e inamovibles**."))}

{unidad("2.2 Incompatibilidades (art. 159.4 CE; art. 19 LOTC)",
  lit("CE", "a159", ["incompatible: con todo mandato representativo", "con los cargos políticos o administrativos", "con el ejercicio de las carreras judicial y fiscal"], solo=[4, 5]),
  lx("LOTC", "adiecinueve", 19, ["incompatible", "Defensor del Pueblo", "Diputado y Senador", "carrera judicial o fiscal"], solo=[1]),
  "Incompatibilidades principales: **mandato representativo**, **cargo político o administrativo**, **funciones directivas en un partido político o sindicato** (y asociaciones, fundaciones y colegios profesionales según la LOTC), **carreras judicial y fiscal** y cualquier **actividad profesional o mercantil**.")}

{unidad("2.3 El Presidente y el Vicepresidente (art. 160 CE; art. 9 LOTC)",
  lit("CE", "a160", ["nombrado entre sus miembros por el Rey", "a propuesta del mismo Tribunal en pleno", "tres años"]),
  lx("LOTC", "anoveno", 9, ["elige de entre sus miembros por votación secreta a su Presidente", "tres años", "reelegido por una sola vez"], solo=[1, 3, 4]),
  fichab("Presidente del Tribunal Constitucional",
         "Lo elige el **Pleno** de entre sus miembros; lo nombra el **Rey**",
         "**Votación secreta** del Pleno; propuesta al Rey",
         "**3 años**; **reelegible por una sola vez**",
         "El Presidente lo nombra el Rey **a propuesta del propio Tribunal en pleno** (art. 160). El **Vicepresidente** lo elige el Pleno por el mismo procedimiento y periodo (art. 9.4 LOTC)."))}
""", 2)

T.ap("s35", "VII.3 Competencias y procedimientos", f"""
{unidad("3.1 Cuadro de las competencias (art. 161 CE; arts. 2 y 59 LOTC)",
  lit("CE", "a161", ["recurso de inconstitucionalidad contra leyes y disposiciones normativas con fuerza de ley", "recurso de amparo por violación de los derechos y libertades referidos en el artículo 53, 2", "conflictos de competencia entre el Estado y las Comunidades Autónomas o de los de éstas entre sí", "las disposiciones y resoluciones adoptadas por los órganos de las Comunidades Autónomas"], solo=[1, 2, 3, 4, 5, 6]),
  tabla(["Procedimiento", "Lo interpone", "Frente a", "Plazo", "Base"], [
    [f"**Recurso de inconstitucionalidad**", "**50 Diputados**, **50 Senadores**, **Defensor del Pueblo**, **Presidente del Gobierno**, **órganos ejecutivos y Asambleas** de las CCAA", "**Leyes y normas con rango de ley** (decretos-leyes y decretos legislativos incluidos)", "**3 meses** desde la publicación; **9 meses** en los conflictos Estado-CCAA con Comisión Bilateral", "CE 161.1.a, 162.1.a; LOTC 32, 33"],
    [f"**Cuestión de inconstitucionalidad**", "El **órgano judicial** (jueces y tribunales) cuando deba dictar sentencia", "**Norma con rango de ley** aplicable al caso y de cuya validez dependa el fallo", "**Una vez concluso el procedimiento** y dentro del plazo para dictar sentencia", "CE 163; LOTC 35"],
    [f"**Recurso de amparo** (*«último remedio»*, tras el proceso preferente y sumario)", "**Persona natural o jurídica con interés legítimo**, **Ministerio Fiscal** y **Defensor del Pueblo**", "**Actuación de los poderes públicos** (derechos 14, 15 a 29 y 30.2)", "**3 meses · 20 días · 30 días** (→ V.3)", "CE 161.1.b, 162.1.b; LOTC 41 a 46"],
    [f"**Conflicto de competencias**", "El **Gobierno** o el **órgano ejecutivo** de la CA", "Estado ↔ CCAA · CA ↔ CA · **Gobierno ↔ Congreso, Senado o CGPJ** (o entre estos)", "Requerimiento previo de **2 meses**; luego **1 mes**", "CE 161.1.c; LOTC 59 a 63, 73"]]))}

{unidad("3.2 La cuestión de inconstitucionalidad (art. 163 CE; art. 35 LOTC)",
  lit("CE", "a163", ["Cuando un órgano judicial considere", "planteará la cuestión ante el Tribunal Constitucional"]),
  lx("LOTC", "atreintaycinco", 35, ["una norma con rango de Ley aplicable al caso y de cuya validez dependa el fallo", "sólo podrá plantear la cuestión una vez concluso el procedimiento y dentro del plazo para dictar sentencia", "10 días"], solo=[1, 2]),
  fichab("Cuestión de inconstitucionalidad",
         "**Jueces y tribunales** (de oficio o a instancia de parte)",
         "Si el juez duda de que una **norma con rango de ley** aplicable al caso y de cuya validez depende el fallo sea contraria a la Constitución",
         ["**Solo una vez concluso el procedimiento** y **dentro del plazo para dictar sentencia**", "Antes, oye a las partes y al Ministerio Fiscal en **10 días** comunes e improrrogables"],
         f"{IMP} Es el **juez** quien la plantea (no las partes). Las partes solo **alegan** sobre si procede plantearla."))}

{unidad("3.3 Los conflictos de competencia entre el Estado y las Comunidades Autónomas (arts. 59 a 63 LOTC)",
  lx("LOTC", "acincuentaynueve", 59, ["Al Estado con una o más Comunidades Autónomas", "A dos o más Comunidades Autónomas entre sí", "Al Gobierno con el Congreso de los Diputados, el Senado o el Consejo General del Poder Judicial"], solo=[1, 2, 3, 4]),
  lx("LOTC", "asesenta", 60, ["Gobierno o por los órganos colegiados ejecutivos de las Comunidades Autónomas"]),
  lx("LOTC", "asesentaydos", 62, ["en el plazo de dos meses"]),
  lx("LOTC", "asesentaytres", 63, ["dentro de los dos meses siguientes", "en el plazo máximo de un mes", "Dentro del mes siguiente"], solo=[1, 2, 4, 5]),
  tabla(["Quién", "Cómo", "Plazos"], [
    ["**Gobierno** (frente a una disposición o resolución autonómica)", "Plantea el conflicto **directamente** ante el TC o hace antes un **requerimiento previo**", "**2 meses**"],
    ["**Órgano ejecutivo de una CA** (frente al Estado u otra CA)", "**Requerimiento previo** a quien dictó la disposición, resolución o acto", "Requerir dentro de **2 meses**; el requerido contesta en **1 mes**; si no hay satisfacción, **1 mes** para plantear el conflicto"]]))}

{unidad("3.4 Los conflictos entre órganos constitucionales (arts. 59.1.c y 73 LOTC)",
  lx("LOTC", "asetentaytres", 73, ["dentro del mes siguiente a la fecha en que llegue a su conocimiento", "planteará el conflicto ante el Tribunal Constitucional dentro del mes siguiente"], solo=[1, 3]),
  "Enfrentan al **Gobierno** con el **Congreso**, el **Senado** o el **Consejo General del Poder Judicial**, o a estos órganos **entre sí**. Antes hay que **comunicar** la discrepancia y pedir que se revoque (**1 mes**).")}

{unidad("3.5 Los conflictos en defensa de la autonomía local (arts. 59.2 y 75 bis a 75 quater LOTC)",
  lx("LOTC", "asetentaycincobis", "75 bis", ["normas del Estado con rango de ley", "disposiciones con rango de ley de las Comunidades Autónomas", "que lesionen la autonomía local constitucionalmente garantizada"], solo=[1]),
  lx("LOTC", "asetentaycincoter", "75 ter", ["El municipio o provincia que sea destinatario único de la ley", "un séptimo", "un sexto", "al menos la mitad de las existentes"], solo=[1, 2, 3, 4]),
  lx("LOTC", "asetentaycincoquater", "75 quater", ["tres meses", "Dentro del mes siguiente"], solo=[1, 2]),
  "Los plantean **municipios y provincias** contra **normas con rango de ley** (del Estado o de las CCAA) que lesionen la **autonomía local**. Plazos: **3 meses** para pedir el dictamen preceptivo del Consejo de Estado (o del órgano consultivo autonómico) y **1 mes** desde que lo reciben para plantear el conflicto.")}

{unidad("3.6 La impugnación de disposiciones sin fuerza de ley de las CCAA (art. 161.2 CE; arts. 76 y 77 LOTC)",
  lit("CE", "a161", ["El Gobierno podrá impugnar ante el Tribunal Constitucional las disposiciones y resoluciones adoptadas por los órganos de las Comunidades Autónomas", "en un plazo no superior a cinco meses"], solo=[6]),
  lx("LOTC", "asetentayseis", 76, ["Dentro de los dos meses siguientes", "disposiciones normativas sin fuerza de Ley y resoluciones emanadas de cualquier órgano de las Comunidades Autónomas"]),
  "Solo la plantea el **Gobierno**; produce la **suspensión** de la disposición o resolución recurrida, que el Tribunal ratifica o levanta en **menos de cinco meses**.")}
""", 2)

T.ap("s36", "VII.4 Las sentencias y sus efectos", f"""
{unidad("4.1 Valor de las sentencias (art. 164 CE; arts. 38 y 39 LOTC)",
  lit("CE", "a164", ["se publicarán en el boletín oficial del Estado con los votos particulares, si los hubiere", "valor de cosa juzgada a partir del día siguiente de su publicación", "no cabe recurso alguno contra ellas", "plenos efectos frente a todos", "subsistirá la vigencia de la ley en la parte no afectada por la inconstitucionalidad"], solo=[1, 2]),
  lx("LOTC", "atreintayocho", 38, ["valor de cosa juzgada", "vincularán a todos los Poderes Públicos", "efectos generales desde la fecha de su publicación"], solo=[1]),
  lx("LOTC", "atreintaynueve", 39, ["declarará igualmente la nulidad de los preceptos impugnados"], solo=[1]),
  fichab("Sentencias del Tribunal Constitucional",
         "El **Tribunal Constitucional**",
         ["Se **publican en el BOE** con los **votos particulares**, si los hubiere", "No cabe **recurso alguno**", "La parte de la ley **no afectada** por la inconstitucionalidad **mantiene su vigencia**", "Si declaran la **inconstitucionalidad** de una ley, declaran también su **nulidad**"],
         ["**Cosa juzgada** desde el **día siguiente** a su publicación (art. 164.1 CE)", "**Plenos efectos frente a todos**: las que declaran la inconstitucionalidad de una ley o norma con fuerza de ley y **todas las que no se limiten a la estimación subjetiva de un derecho**"],
         f"{IMP} Cinco ideas del art. 164: **BOE con votos particulares**, **cosa juzgada al día siguiente**, **sin recurso**, **efectos frente a todos** (salvo las que solo estiman un derecho subjetivo) y **vigencia de la parte no afectada**. Se refiere a leyes **o normas con fuerza de ley**."))}
""", 2)

T.ap("s37", "VII.5 Recapitulación: amparo frente a inconstitucionalidad", f"""
{tabla(["", "**Recurso de amparo**", "**Recurso de inconstitucionalidad**"], [
  ["**Quién**", "**Afectado** (persona con interés legítimo) · **Ministerio Fiscal** · **Defensor del Pueblo**", "**Presidente del Gobierno** · **Defensor del Pueblo** · **50 Diputados** · **50 Senadores** · **órganos ejecutivos y Asambleas** de las CCAA (en su ámbito)"],
  ["**Contra qué**", "**Actos, omisiones o vía de hecho** de los poderes públicos que violen los derechos **14, 15 a 29 y 30.2**", "**Leyes y normas con rango de ley** (por infringir la Constitución)"],
  ["**Plazo**", "**3 meses · 20 días · 30 días**", "**3 meses** (9 en los casos del art. 33.2 LOTC)"],
  ["**Particularidad**", "**«Último remedio»**: tras agotar la vía judicial", "Lo puede promover el **Defensor del Pueblo**: único legitimado en **ambos**"]])}

{IMP} El **Defensor del Pueblo** es el **único** legitimado a la vez para el **amparo** y para la **inconstitucionalidad** (arts. 162.1 CE; 32 y 46 LOTC; 29 LO 3/1981).
""", 2)

T.ap("s38", "VII.6 Resumen del Tribunal Constitucional", resumen([
  "**12 miembros** nombrados por el **Rey**: 4 Congreso (3/5) · 4 Senado (3/5, entre candidaturas de las Asambleas autonómicas) · 2 Gobierno · 2 CGPJ. **9 años**, renovación por **tercios cada 3**; Presidente **3 años**, reelegible una vez.",
  "**Requisitos:** juristas de reconocida competencia con **más de 15 años**; presencia **equilibrada** (al menos 40 % de cada sexo en las propuestas).",
  "**Competencias:** inconstitucionalidad, cuestión de inconstitucionalidad, amparo, conflictos de competencia (Estado-CCAA y entre órganos constitucionales), defensa de la autonomía local e impugnación del art. 161.2.",
  "**Sentencias:** BOE con votos particulares, cosa juzgada al día siguiente, sin recurso, efectos frente a todos."], "Siguiente: VIII. El Defensor del Pueblo"), 2)

# =============================================================================
# VIII. DEFENSOR DEL PUEBLO
T.ap("bVIII", "VIII. El Defensor del Pueblo (art. 54)", donde(
  "Octava pregunta. El Defensor del Pueblo es la **garantía institucional** de los derechos del Título I. Se estudia el art. 54 y la **LO 3/1981**: cómo se elige, cuánto dura su mandato, qué puede investigar y qué recursos puede interponer.",
  ["1 Qué es", "2 Requisitos y elección", "3 Mandato, adjuntos y estatuto", "4 Funciones y actuación"]))

T.ap("s39", "VIII.1 Qué es el Defensor del Pueblo", f"""
Según el módulo, tiene **cierta inspiración nórdica** (el *ombudsman*). Sus **aspectos constitucionales** son cuatro:

{unidad("1.1 El art. 54 CE y el art. 1 de su ley orgánica",
  lit("CE", "a54", ["alto comisionado de las Cortes Generales", "los derechos comprendidos en este Título", "supervisar la actividad de la Administración, dando cuenta a las Cortes Generales"]),
  lx("LODP", "aprimero", 1, ["alto comisionado de las Cortes Generales", "defensa de los derechos comprendidos en el Título I de la Constitución", "supervisar la actividad de la Administración, dando cuenta a las Cortes Generales"]),
  fichab("Defensor del Pueblo",
         "**Alto comisionado de las Cortes Generales**, **designado por éstas**",
         ["**Defiende todos los derechos del Título I** de la Constitución", "**Supervisa la actividad de la Administración**, dando cuenta a las Cortes Generales", "Regulado por **ley orgánica** (LO 3/1981)"],
         "—",
         f"{IMP} Es un comisionado de las **Cortes Generales** (no del Gobierno) y defiende **todo el Título I**, no solo la sección 1.ª."))}
""", 2)

T.ap("s40", "VIII.2 Requisitos y elección", f"""
{unidad("2.1 Requisitos (art. 3 LO 3/1981)",
  lx("LODP", "atercero", 3, ["cualquier español mayor de edad", "pleno disfrute de sus derechos civiles y políticos"]),
  tabla(["Requisito", "Contenido"], [["**Nacionalidad**", "**Español**"], ["**Edad**", "**Mayor de edad**"], ["**Capacidad**", "**Pleno disfrute de sus derechos civiles y políticos**"]]))}

{unidad("2.2 La elección (art. 2 LO 3/1981)",
  lx("LODP", "asegundo", 2, ["Comisión Mixta Congreso-Senado", "tres quintas partes de los miembros del Congreso", "veinte días", "mayoría absoluta del Senado", "cinco años"], solo=[1, 2, 3, 4, 5, 6]),
  tabla(["Paso", "Qué ocurre", "Mayoría"], [
    ["**1.º**", "La **Comisión Mixta Congreso-Senado** se reúne y **propone** al candidato o candidatos a los Plenos", "**Mayoría simple** (acuerdos de la Comisión)"],
    ["**2.º · Votación A**", "El **Pleno del Congreso** elige; después, el **Senado ratifica** en un plazo máximo de **20 días**", "**3/5 del Congreso** y **3/5 del Senado**"],
    ["**2.º · Votación B** (si no se alcanzan esas mayorías)", "Nueva sesión de la Comisión, que formula sucesivas propuestas **en el plazo máximo de un mes**", "**3/5 del Congreso** y **mayoría absoluta del Senado**"],
    ["**3.º**", "Los **Presidentes del Congreso y del Senado acreditan conjuntamente con sus firmas** el nombramiento, que se publica en el **BOE**; toma posesión ante las **Mesas de ambas Cámaras** reunidas", "—"]]),
  f"!> {IMP} En el Congreso siempre **3/5**; en el Senado, **3/5** la primera vez y **mayoría absoluta** si hay que repetir. El **Presidente del Congreso y el del Senado** firman **conjuntamente** el nombramiento.")}

{unidad("2.3 El nombramiento y la toma de posesión (art. 4 LO 3/1981)",
  lx("LODP", "acuao", 4, ["acreditarán conjuntamente con sus firmas el nombramiento", "Mesas de ambas Cámaras reunidas conjuntamente"]))}
""", 2)

T.ap("s41", "VIII.3 Mandato, adjuntos y estatuto", f"""
{unidad("3.1 Mandato y cese (arts. 2.1 y 5 LO 3/1981)",
  lx("LODP", "aquinto", 5, ["Por renuncia", "Por expiración del plazo de su nombramiento", "Por muerte o por incapacidad sobrevenida", "Por actuar con notoria negligencia", "condenado, mediante sentencia firme, por delito doloso"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Mandato del Defensor del Pueblo",
         "Las **Cortes Generales**",
         "Cesa por **renuncia**, **expiración del plazo**, **muerte o incapacidad**, **notoria negligencia** o **condena firme por delito doloso**",
         ["**5 años**", "La vacante por muerte, renuncia y expiración la declara el **Presidente del Congreso**; en los demás casos, **3/5 de cada Cámara**"],
         "El módulo anota que el mandato es reelegible; la ley orgánica **no regula** la reelección."))}

{unidad("3.2 Los adjuntos (art. 8 LO 3/1981)",
  lx("LODP", "aoctavo", 8, ["Adjunto Primero y un Adjunto Segundo", "El Defensor del Pueblo nombrará y separará a sus Adjuntos previa conformidad de las Cámaras"], solo=[1, 2]),
  "**Dos adjuntos** (**primero** y **segundo**), **nombrados por él** con la **conformidad previa** de las Cámaras (la Comisión Mixta, art. 2.6). Lo sustituyen **por su orden**.")}

{unidad("3.3 Independencia e inviolabilidad (art. 6 LO 3/1981)",
  lx("LODP", "asexto", 6, ["no estará sujeto a mandato imperativo alguno", "No recibirá instrucciones de ninguna Autoridad", "gozará de inviolabilidad"], solo=[1, 2]))}

{unidad("3.4 Incompatibilidades (art. 7 LO 3/1981)",
  lx("LODP", "aseptimo", 7, ["incompatible con todo mandato representativo", "con la afiliación a un partido político"], solo=[1]))}
""", 2)

T.ap("s42", "VIII.4 Funciones y actuación", f"""
{tabla(["Aspecto", "Qué dice", "Norma"], [
  ["**Qué supervisa**", "La actividad de la **Administración** (del Estado y también de las **Comunidades Autónomas**, aunque estas pueden tener sus propios defensores)", "Art. 54 CE; arts. 9 y 12 LO 3/1981"],
  ["**Quién puede dirigirse a él**", "**Toda persona natural o jurídica** con interés legítimo, sin restricción de nacionalidad, residencia, sexo, minoría de edad… · **Diputados y Senadores** individualmente · **comisiones de investigación** · la **Comisión Mixta Congreso-Senado**", "Art. 10"],
  ["**Quién no**", "**Ninguna autoridad administrativa** en asuntos de su competencia", "Art. 10.3"],
  ["**Cómo actúa**", "De **oficio** o a **petición de parte**; **investigación sumaria e informal**; la Administración informa en **15 días**", "Arts. 9.1 y 18.1"],
  ["**Plazo para la queja**", "**Un año** desde que se conocen los hechos; es **gratuita** y no necesita abogado ni procurador", "Art. 15"],
  ["**Recursos**", "Está legitimado para interponer **recurso de inconstitucionalidad** y **recurso de amparo**", "Art. 29; CE 162.1"],
  ["**Resultado**", "Puede formular **advertencias, recomendaciones, recordatorios y sugerencias**; **no puede modificar ni anular** los actos de la Administración", "Arts. 28 y 30"],
  ["**Informes**", "Da cuenta **anualmente** a las Cortes Generales", "Art. 32"]])}

{unidad("4.1 Investigación y límites",
  lx("LODP", "adiez", 10, ["toda persona natural o jurídica que invoque un interés legítimo", "Los Diputados y Senadores individualmente", "las comisiones de investigación", "la Comisión Mixta Congreso-Senado de relaciones con el Defensor del Pueblo", "No podrá presentar quejas ante el Defensor del Pueblo ninguna autoridad administrativa"], solo=[1, 2, 3]),
  lx("LODP", "adieciocho", 18, ["investigación sumaria e informal", "quince días"], solo=[1]),
  lx("LODP", "aveintinueve", 29, ["recursos de inconstitucionalidad y de amparo"]),
  lx("LODP", "aquince", 15, ["en el plazo máximo de un año"], solo=[1]))}

!> {IMP} **Para el examen:** el Defensor puede interponer **a la vez** amparo e inconstitucionalidad; su investigación es **sumaria e informal**; supervisa también a las **CCAA**; los **estados de excepción o sitio no interrumpen** su actividad (art. 11.3, sin perjuicio del art. 55 CE).
""", 2)

T.ap("s43", "VIII.5 Resumen del Defensor del Pueblo", resumen([
  "**Alto comisionado** de las Cortes Generales; defiende los derechos del **Título I** y supervisa la **Administración** (estatal y autonómica); ley orgánica.",
  "**Requisitos:** español, mayor de edad, pleno disfrute de derechos civiles y políticos.",
  "**Elección:** Comisión Mixta propone → **3/5 Congreso** y ratificación **3/5 Senado** (20 días) → si no, **3/5 Congreso + mayoría absoluta Senado** → firma conjunta de los Presidentes y **BOE**.",
  "**5 años**; **dos adjuntos** nombrados por él; **investigación sumaria e informal**; puede interponer **amparo e inconstitucionalidad**."], "Siguiente: IX. La reforma de la Constitución (Título X)"), 2)

# =============================================================================
# IX. REFORMA DE LA CONSTITUCIÓN
T.ap("bIX", "IX. ¿Cómo se reforma la Constitución? Título X (arts. 166 a 169)", donde(
  "Novena pregunta. El **Título X** recoge **dos procedimientos**: el **ordinario o «light»** (art. 167) y el **agravado o «heavy»** (art. 168), para la revisión total o la de las partes más protegidas (la «rigidez» de la Constitución). Los Reglamentos de las Cámaras y la LO 2/1980 completan el procedimiento.",
  ["1 La iniciativa (arts. 87 y 166)", "2 El procedimiento del art. 167 («light»)", "3 El procedimiento del art. 168 («heavy»)", "4 Límites y reglas comunes", "5 Cuadro comparativo"]))

T.ap("s44", "IX.1 La iniciativa de reforma (arts. 87.1 y 2 y 166)", f"""
{unidad("1.1 Los titulares (art. 87.1 y 2)",
  lit("CE", "a87", ["al Gobierno, al Congreso y al Senado", "Las Asambleas de las Comunidades Autónomas", "un máximo de tres miembros"], solo=[1, 2]),
  fichab("Iniciativa a la que remite el art. 166 (→ IX.1.2)",
         ["El **Gobierno**", "El **Congreso** y el **Senado**", "Las **Asambleas de las Comunidades Autónomas**"],
         [f"Asambleas autonómicas: {c('CE', 'Artículo 87', 'solicitar del Gobierno la adopción de un proyecto de ley')} o {c('CE', 'Artículo 87', 'remitir a la Mesa del Congreso una proposición de ley')}"],
         "Las Asambleas delegan ante el Congreso **un máximo de tres** miembros",
         "Las Asambleas autonómicas **no** presentan la iniciativa ante el Senado: la remiten a la **Mesa del Congreso** o la piden al **Gobierno**."))}

{unidad("1.2 Remisión al art. 87 (art. 166)",
  lit("CE", "a166", ["apartados 1 y 2 del artículo 87"]),
  fichab("Quién puede proponer una reforma constitucional",
         "Los titulares de los apartados 1 y 2 del art. 87 (→ IX.1.1)",
         "En los términos de la iniciativa legislativa",
         "—",
         "El art. 166 remite **solo** a los apartados **1 y 2** del art. 87: la **iniciativa popular** (87.3) **no** puede proponer una reforma constitucional."))}

{unidad("1.3 Requisitos de las proposiciones en cada Cámara (Reglamento del Congreso, art. 146.1; Reglamento del Senado, art. 152)",
  lit("RCD", "art146", ["suscritas por dos grupos parlamentarios o por una quinta parte de los miembros de la Cámara"], solo=[1], titulo="Artículo 146.1 (Reglamento del Congreso)"),
  lit("RS", "Artículo 152", ["Cincuenta Senadores que no pertenezcan a un mismo Grupo parlamentario"]),
  fichab("Quién firma una proposición de reforma en cada Cámara",
         ["Congreso: **dos grupos parlamentarios** o **una quinta parte** de los Diputados", "Senado: **cincuenta Senadores** de más de un Grupo parlamentario"],
         "En el Congreso, por las normas de los proyectos y proposiciones de ley (art. 146.1); en el Senado, toma en consideración (art. 153)",
         "—",
         "Congreso: **2 grupos o 1/5**. Senado: **50 Senadores** que **no pertenezcan a un mismo Grupo**."))}
""", 2)

T.ap("s45", "IX.2 El procedimiento del art. 167", f"""
{unidad("2.1 Mayorías, Comisión paritaria y referéndum facultativo (art. 167)",
  lit("CE", "a167", ["mayoría de tres quintos de cada una de las Cámaras", "Comisión de composición paritaria de Diputados y Senadores", "mayoría absoluta del Senado", "por mayoría de dos tercios", "dentro de los quince días siguientes a su aprobación, una décima parte de los miembros de cualquiera de las Cámaras"]),
  fichab("Procedimiento para cualquier reforma que no sea del art. 168",
         ["Las **Cortes Generales** (Congreso y Senado)", "Comisión **paritaria** de Diputados y Senadores, si no hay acuerdo", "**Una décima parte** de los miembros de cualquiera de las Cámaras: piden el referéndum"],
         ["Aprobación por **tres quintos** de **cada** Cámara", "Sin acuerdo: Comisión paritaria → texto votado por Congreso y Senado", "Si aun así no se aprueba: basta la **mayoría absoluta del Senado** y **dos tercios del Congreso**", "Referéndum de ratificación **solo si se solicita**"],
         ["3/5 de cada Cámara", "Alternativa: mayoría absoluta del Senado + 2/3 del Congreso", "Referéndum: lo piden **1/10** de los miembros de cualquier Cámara en **15 días** desde la aprobación"],
         "Dos tercios del **Congreso** (no del Senado) en la vía del 167.2. El referéndum del 167 es **facultativo**; el del 168, **obligatorio** (→ IX.3.1)."))}

{unidad("2.2 La tramitación en el Congreso (Reglamento del Congreso, art. 146.2 a 4)",
  lit("RCD", "art146", ["votación final", "tres quintos de los miembros de la Cámara", "Comisión Mixta paritaria"], solo=[2, 3, 4], titulo="Artículo 146.2 a 4 (Reglamento del Congreso)"),
  fichab("Votación de la reforma del art. 167 en el Congreso",
         "Pleno del Congreso; Comisión Mixta paritaria",
         "Votación final sobre el texto aprobado por el Pleno",
         "**Tres quintos de los miembros** de la Cámara; con la Comisión Mixta, la misma mayoría",
         "El Reglamento la llama **Comisión Mixta paritaria**; la Constitución, «Comisión de composición paritaria de Diputados y Senadores»."))}

{unidad("2.3 La tramitación en el Senado (Reglamento del Senado, arts. 154 y 156)",
  lit("RS", "Artículo 154", ["Comisión Constitucional"], solo=[1]),
  lit("RS", "Artículo 156", ["mayoría favorable de tres quintos de Senadores en una votación final sobre el conjunto", "mayoría absoluta del Senado"]),
  fichab("Votación de la reforma del art. 167 en el Senado",
         "Mesa (califica y admite), **Comisión Constitucional** (dictamen) y Pleno del Senado",
         ["Si el Senado aprueba el mismo texto del Congreso: se comunica al Congreso", "Si difiere: Comisión Mixta paritaria"],
         ["**Tres quintos de Senadores** en una votación final sobre el conjunto", "Texto de la Comisión Mixta: tres quintos; si solo logra la **mayoría absoluta**, se comunica al Congreso (art. 167.2 CE)"],
         "La **mayoría absoluta del Senado** es la que abre la vía del art. 167.2 (dos tercios del Congreso)."))}

{unidad("2.4 El referéndum facultativo (Reglamento del Senado, art. 157; LO 2/1980, arts. 2.3 y 7)",
  lit("RS", "Artículo 157", ["dentro de los quince días siguientes, una décima parte de los miembros del Senado"]),
  lit("LO2_1980", "Artículo segundo", ["Corresponde al Rey convocar a referéndum"], solo=[3]),
  lit("LO2_1980", "Artículo séptimo", ["será condición previa la comunicación por las Cortes Generales al Presidente del Gobierno", "dentro del plazo de treinta días", "dentro de los sesenta días siguientes"]),
  fichab("Ratificación popular de la reforma",
         ["Lo solicita **una décima parte** de los miembros de cualquiera de las Cámaras (en el Senado, por escrito al Presidente)", "Lo convoca el **Rey**, mediante Real Decreto acordado en Consejo de Ministros y refrendado por su Presidente"],
         "Las Cortes comunican al Presidente del Gobierno el proyecto aprobado, con la solicitud del art. 167.3",
         ["Solicitud: **15 días** desde la aprobación", "Convocatoria: dentro de **30 días** desde la comunicación", "Celebración: dentro de los **60 días** siguientes"],
         "Tres plazos distintos: **15** (pedirlo), **30** (convocarlo) y **60** (celebrarlo)."))}
""", 2)

T.ap("s46", "IX.3 El procedimiento del art. 168", f"""
{unidad("3.1 Revisión total o de las partes protegidas (art. 168)",
  lit("CE", "a168", ["revisión total", "al Título preliminar, al Capítulo segundo, Sección primera del Título I, o al Título II", "mayoría de dos tercios de cada Cámara", "disolución inmediata de las Cortes", "deberá ser aprobado por mayoría de dos tercios de ambas Cámaras", "será sometida a referéndum para su ratificación"]),
  fichab("Procedimiento reforzado de reforma",
         ["Las Cortes que aprueban el principio (y quedan disueltas)", "Las **Cámaras elegidas** después", "El **pueblo**, en referéndum obligatorio"],
         ["::Se aplica a:", "La **revisión total**", "Una revisión parcial que afecte al **Título preliminar** (arts. 1 a 9)", "… al **Capítulo segundo, Sección primera, del Título I** (arts. 15 a 29)", "… al **Título II** (la Corona, arts. 56 a 65)"],
         ["1. Principio: **2/3 de cada Cámara** + **disolución inmediata**", "2. Nuevas Cámaras: ratifican y aprueban el nuevo texto por **2/3 de ambas**", "3. **Referéndum** de ratificación, siempre"],
         "No están protegidos el **art. 14** ni la **Sección 2.ª**: la Sección 1.ª empieza en el art. 15 (→ II.3). Tampoco la reforma del Título X. El referéndum es **obligatorio** («será sometida»)."))}

{unidad("3.2 La tramitación en el Congreso (Reglamento del Congreso, art. 147)",
  lit("RCD", "art147", ["las normas previstas para los de totalidad", "las dos terceras partes de los miembros de la Cámara", "Real Decreto de disolución de las Cortes Generales", "las dos terceras partes de los miembros del Congreso"], titulo="Artículo 147 (Reglamento del Congreso)"),
  fichab("Pasos del art. 168 en el Congreso",
         ["Pleno del Congreso", "Presidencia del Congreso: comunica al Senado y al Gobierno", "Gobierno: somete al Rey el Real Decreto de disolución"],
         ["Debate de totalidad sobre el principio de revisión", "Si 2/3 de cada Cámara: Real Decreto de disolución", "Nuevas Cortes: ratificación y tramitación del nuevo texto por el procedimiento legislativo común"],
         "**Dos tercios** de los miembros: para el principio y para el nuevo texto",
         "El nuevo texto se tramita por el **procedimiento legislativo común**; aprobado, la Presidencia del Congreso lo comunica al Gobierno para el **referéndum** (art. 168.3)."))}

{unidad("3.3 La tramitación en el Senado (Reglamento del Senado, arts. 158 y 159)",
  lit("RS", "Artículo 158", ["serán sometidos directamente al Pleno", "dos tercios del número de Senadores"]),
  lit("RS", "Artículo 159", ["por mayoría absoluta de sus miembros", "dos tercios del número de Senadores en una votación final sobre el conjunto del texto"]),
  fichab("Pasos del art. 168 en el Senado",
         "Pleno del Senado (directamente, sin Comisión); el Presidente del Senado comunica al del Congreso",
         ["Principio de reforma: 2/3 de Senadores", "Nueva Cámara: ratifica y tramita el texto", "Aprobación final: 2/3 de Senadores"],
         ["Principio: **dos tercios** de Senadores", "Ratificación por la nueva Cámara: **mayoría absoluta** (Reglamento del Senado)", "Texto: **dos tercios** en votación final sobre el conjunto"],
         "La **mayoría absoluta** para ratificar la decisión la fija el **Reglamento del Senado** (art. 159), no la Constitución."))}
""", 2)

T.ap("s47", "IX.4 Límites y reglas comunes (arts. 75.3, 116.1 y 169; LO 2/1980, art. 4)", f"""
{unidad("4.1 Sin delegación en Comisiones (art. 75.3)",
  lit("CE", "a75", ["la reforma constitucional"], solo=[2, 3]),
  fichab("La reforma constitucional la aprueba el Pleno",
         "El **Pleno** de cada Cámara",
         "No cabe delegar su aprobación en las Comisiones Legislativas Permanentes",
         "—",
         "La **reforma constitucional** encabeza la lista del 75.3, con las cuestiones internacionales, las leyes orgánicas y de bases y los Presupuestos."))}

{unidad("4.2 Límite temporal: guerra y estados del art. 116 (arts. 116.1 y 169)",
  lit("CE", "a116", ["los estados de alarma, de excepción y de sitio"], solo=[1]),
  lit("CE", "a169", ["en tiempo de guerra o de vigencia de alguno de los estados previstos en el artículo 116"]),
  fichab("Cuándo no puede iniciarse una reforma",
         "—",
         ["En tiempo de **guerra**", "Durante la vigencia del estado de **alarma**, de **excepción** o de **sitio** (art. 116)"],
         "—",
         "Lo que se prohíbe es **iniciar** la reforma. Incluye el estado de **alarma**, no solo los de excepción y sitio."))}

{unidad("4.3 El referéndum constitucional y el calendario electoral (LO 2/1980, art. 4)",
  lit("LO2_1980", "Artículo cuarto", ["durante la vigencia de los estados de excepción y sitio", "salvo los previstos en los artículos ciento sesenta y siete y ciento sesenta y ocho de la Constitución"]),
  fichab("Cuándo no puede celebrarse un referéndum",
         "—",
         ["Ninguno durante los estados de **excepción y sitio** ni en los 90 días posteriores a su levantamiento", "Los referendos de reforma (arts. 167 y 168) **sí** pueden coincidir con el periodo de 90 días antes y después de elecciones o de otro referéndum"],
         "**Noventa días**",
         "La excepción del art. 4.2 favorece a los referendos de **reforma constitucional**: no se suspenden por la cercanía de unas elecciones."))}
""", 2)


T.ap("s48", "IX.5 Cuadro comparativo: art. 167 y art. 168", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| | **Art. 167 · general («light»)** | **Art. 168 · agravado («heavy»)** |
|---|---|---|
| **Cuándo** | **Cualquier reforma** no incluida en el 168 (las cuatro hechas: arts. **13.2, 135, 49 y 69.3**) | **Revisión total**, o parcial que afecte al **Título preliminar**, a la **Sección 1.ª del Capítulo II del Título I** o al **Título II** |
| **Iniciativa** | Art. 166 → arts. **87.1 y 87.2** (Gobierno, Congreso, Senado, Asambleas autonómicas) | Igual |
| **Aprobación** | **3/5 de cada Cámara**; si no hay acuerdo, **Comisión paritaria** y nueva votación de 3/5; si aun así no, **mayoría absoluta del Senado + 2/3 del Congreso** | **Principio: 2/3 de cada Cámara** → **disolución inmediata** → las nuevas Cámaras **ratifican** y estudian el texto → **2/3 de ambas** |
| **Referéndum** | **Facultativo**: lo piden **1/10 de los miembros de cualquier Cámara** en **15 días** | **Obligatorio** («ahora sí o sí») |
| **Límite (art. 169)** | No puede iniciarse en tiempo de **guerra** ni en **alarma, excepción o sitio** | Igual |

{IMP} **Lo más preguntable:** quién **queda fuera de la iniciativa** (la **popular**, 87.3), las **mayorías** de cada artículo (**3/5** frente a **2/3**), que el art. 168 supone **disolución inmediata** y **referéndum obligatorio**, que el art. 167 solo tiene referéndum **si lo piden 1/10 en 15 días**, y que **no se puede iniciar** la reforma en guerra ni en alarma, excepción o sitio.

{resumen([
  "Iniciativa: la del **art. 87.1 y 2** (Gobierno, Congreso, Senado y Asambleas autonómicas); **no** la popular.",
  "Art. 167: **3/5 de cada Cámara**; Comisión **paritaria**; o mayoría absoluta del Senado + **2/3 del Congreso**; referéndum **si lo pide 1/10** de una Cámara en **15 días**.",
  "Art. 168: revisión total o del **Título preliminar**, **Sección 1.ª del Cap. II del Título I** o **Título II**: **2/3**, **disolución**, **2/3** de las nuevas Cámaras y **referéndum obligatorio**.",
  "No se puede **iniciar** en guerra ni en los estados del **art. 116**; no se delega en Comisiones (75.3)."],
  "Siguiente: X. Preguntas de examen y repaso")}
""", 2)

# =============================================================================
# X. PREGUNTAS Y REPASO
T.ap("bX", "X. Preguntas de examen y repaso", donde(
  "Para cerrar el tema: las **preguntas de examen** que incluye la guía M101 (con su respuesta) y el **repaso por bloques**. En la pestaña de test del bloque encontrarás el resto de preguntas de este tema, y el **Test Constitución** entrena los artículos 1 a 55.",
  ["1 Preguntas de la guía M101", "2 Repaso por bloques"]))

T.ap("s49", "X.1 Preguntas de la guía M101", f"""
La guía del módulo incluye estas dos preguntas de examen. Intenta responder **antes de mirar la solución**.

**1.** ¿En qué parte de la Constitución Española (en adelante CE) se regula la nacionalidad española?
a) En el Título Preliminar. · b) En el Preámbulo. · c) En el Título Primero. · d) En el Título Segundo.

*Respuesta de la guía: **c)**. Se regula en el **art. 11**, que está en el **capítulo primero del Título I**.* {c("CE", "a11", "La nacionalidad española se adquiere, se conserva y se pierde de acuerdo con lo establecido por la ley")}

**2.** De acuerdo con su Preámbulo, ¿quién ratifica la Constitución Española de 1978?
a) El Rey. · b) El pueblo español. · c) Las Cortes Generales. · d) El Gobierno.

*Respuesta de la guía: **b)**. El Preámbulo cierra con la fórmula* {c("CE", "preambulo", "las Cortes aprueban y el pueblo español ratifica")}*: las Cortes **aprueban**, el pueblo **ratifica**.*
""", 2)

T.ap("s50", "X.2 Repaso por bloques", f"""
{tabla(["Bloque", "Lo imprescindible"], [
  ["**I · Fechas**", "Aprobación **31-10-1978** (Cortes) · ratificación **6-12-1978** (pueblo) · sanción y promulgación **27-12-1978** · BOE y entrada en vigor **29-12-1978**. Reformas: **13.2 (1992)**, **135 (2011)**, **49 (2024)**, **69.3 (2026)**."],
  ["**II · Estructura**", "Dogmática **1-55** / orgánica **56-169** · 11 títulos · **169** artículos · disposiciones **4-9-1-1** · Título I: **10 | 11-13 | 14 | 15-29 | 30-38 | 39-52 | 53-54 | 55**."],
  ["**III · Contenido**", "De qué trata cada artículo del 1 al 55 (→ Test Constitución). Estructura democrática: arts. **6, 7, 36 y 52**. Art. **9.3**: siete garantías."],
  ["**IV · Niveles**", "Sección 1.ª: **todas** las garantías · art. 14: todas menos LO · sección 2.ª: vinculan, ley e inconstitucionalidad (**amparo solo 30.2**) · cap. III: **informan**."],
  ["**V · Garantías**", "LO: **15-29** (art. 81) · tutela preferente y sumaria: **14-29** · amparo: **14-29 + 30.2** · Defensor: **Título I** · inconstitucionalidad y vinculación: **cap. II (14-38)**."],
  ["**VI · Suspensión**", "Alarma: **Gobierno**, **15 días**, sin suspensión · excepción: **Gobierno + autorización del Congreso**, **30 (+30)** · sitio: **Congreso, m. absoluta**, a propuesta del Gobierno. **17.3** solo en sitio."],
  ["**VII · TC**", "**12** (4+4+2+2) · **9 años**, tercios cada 3 · Presidente **3 años** · **15 años** de ejercicio · amparo **3 meses/20 días/30 días** · inconstitucionalidad **3 meses**."],
  ["**VIII · Defensor**", "Alto comisionado de las Cortes · **3/5 + 3/5** (o m. absoluta Senado) · **5 años** · **2 adjuntos** · queja **1 año** · sumaria e informal."],
  ["**IX · Reforma**", "Iniciativa **87.1 y 87.2** (no popular) · **167**: 3/5, paritaria, m. absoluta Senado + 2/3 Congreso, referéndum si **1/10 en 15 días** · **168**: 2/3, disolución, 2/3, referéndum obligatorio · no se inicia en guerra ni estados del 116."]])}

{ir("#/ce/test", "🧭 Hacer el Test Constitución")} {ir("#/ce/organigrama", "🗺 Organigrama")} {ir("#/ce/texto", "📜 Constitución completa")}

{resumen([
  "La Constitución es la **única norma** en que se estudia la **estructura y el contenido artículo por artículo**.",
  "**Los niveles de protección** del Título I son la clave: **cuadro IV.2**.",
  "**Suspensión (art. 55)**: dominar quién declara, cuánto dura y qué derechos se pueden suspender.",
  "**TC, Defensor y reforma**: mayorías, plazos y quién interpone cada recurso."], "Siguiente: XI. Cronología e hitos")}
""", 2)

# =============================================================================
# XI. CRONOLOGÍA E HITOS
T.ap("bXI", "XI. Cronología e hitos", donde(
  "Cierre del tema: las fechas y normas que conviene tener a mano, en orden. Para la jurisprudencia del Tribunal Constitucional se necesita la fuente oficial; se incorporará cuando se aporte.",
  ["1 Línea del tiempo"]))

T.ap("s51", "XI.1 Línea del tiempo", f"""
{tabla(["Fecha", "Hecho", "Por qué importa"], [
  ["**31-10-1978**", "Las **Cortes Generales** aprueban la Constitución en sesión plenaria del Congreso y del Senado", "**Aprobación** (verbo: aprueban)"],
  ["**6-12-1978**", "Referéndum: el **pueblo español** ratifica la Constitución", "**Ratificación**"],
  ["**27-12-1978**", "El **Rey** sanciona y promulga la Constitución ante las Cortes", "**Sanción y promulgación**"],
  ["**29-12-1978**", "**Publicación en el BOE** y **entrada en vigor**", "Entra en vigor el mismo día de su publicación (disposición final)"],
  ["**18-1-1980**", "**LO 2/1980**, de referéndum (BOE 23-1-1980)", "Regula el referéndum constitucional"],
  ["**3-10-1979**", "**LO 2/1979**, del Tribunal Constitucional (BOE 5-10-1979)", "Desarrolla el Título IX"],
  ["**6-4-1981**", "**LO 3/1981**, del Defensor del Pueblo (BOE 7-5-1981)", "Desarrolla el art. 54"],
  ["**1-6-1981**", "**LO 4/1981**, de los estados de alarma, excepción y sitio (BOE 5-6-1981)", "Desarrolla el art. 116"],
  ["**27-8-1992**", "Reforma del **art. 13.2** (BOE 28-8-1992)", "Sufragio **pasivo** municipal"],
  ["**27-9-2011**", "Reforma del **art. 135** (BOE 27-9-2011)", "Estabilidad presupuestaria"],
  ["**15-2-2024**", "Reforma del **art. 49** (BOE 17-2-2024)", "Personas con discapacidad"],
  ["**19-5-2026**", "Reforma del **art. 69.3** (BOE 20-5-2026)", "Islas del Senado: Ibiza y Formentera"]])}

*Fechas de aprobación y ratificación: guía M101. Fechas de las leyes y reformas: texto de cada norma y metadatos del BOE.*
""", 2)

# ---------------------------------------------------------------------------- PREGUNTAS (T.q)
def Q(k, art, cat, q, ops, exp, frags): T.q(k, art, cat, q, ops, exp, frags)
Q("CE", "a11", "Estructura", "¿En qué parte de la Constitución Española se regula la nacionalidad española?", ["En el Título Primero.", "En el Título Preliminar.", "En el Preámbulo.", "En el Título Segundo."],
  "La nacionalidad (art. 11) está en el capítulo primero del **Título I**. El Título preliminar es de principios (arts. 1 a 9), el Preámbulo no tiene artículos y el Título II es de la Corona.", ["La nacionalidad española se adquiere, se conserva y se pierde de acuerdo con lo establecido por la ley"])
Q("CE", "preambulo", "Estructura", "De acuerdo con su Preámbulo, ¿quién ratifica la Constitución Española de 1978?", ["El pueblo español.", "El Rey.", "Las Cortes Generales.", "El Gobierno."],
  "El Preámbulo termina diciendo que las Cortes **aprueban** y el pueblo español **ratifica**. El Rey la sanciona y promulga; el Gobierno no interviene.", ["las Cortes aprueban y el pueblo español ratifica"])
Q("CE", "s1", "Estructura", "La Sección 1.ª del Capítulo segundo del Título I, «De los derechos fundamentales y de las libertades públicas», comprende los artículos:", ["15 a 29.", "14 a 29.", "14 a 38.", "30 a 38."],
  "Es la sección más protegida: arts. **15 a 29**. El art. 14 queda fuera de las secciones; los arts. 30 a 38 son la sección 2.ª; el capítulo II va de 14 a 38.", ["De los derechos fundamentales y de las libertades públicas"])
Q("CE", "ctercero", "Estructura", "¿Qué capítulo del Título I se denomina «De los principios rectores de la política social y económica»?", ["El capítulo tercero.", "El capítulo segundo.", "El capítulo cuarto.", "El capítulo primero."],
  "Es el **capítulo tercero** (arts. 39 a 52). El segundo es «Derechos y libertades», el cuarto «De las garantías…» y el primero «De los españoles y los extranjeros».", ["De los principios rectores de la política social y económica"])
Q("CE", "a14", "Estructura", "El artículo 14 de la Constitución (igualdad ante la ley) se encuentra:", ["En el capítulo segundo del Título I, fuera de las secciones primera y segunda.", "En la sección primera del capítulo segundo del Título I.", "En el capítulo primero del Título I.", "En el Título preliminar."],
  "El art. 14 está dentro del capítulo segundo pero **fuera de las secciones**: la sección 1.ª empieza en el art. 15.", ["Los españoles son iguales ante la ley"])
Q("CE", "a1", "Contenido", "Según el artículo 1.1 de la Constitución, los valores superiores del ordenamiento jurídico son:", ["La libertad, la justicia, la igualdad y el pluralismo político.", "La dignidad de la persona, la libertad, la justicia y la paz social.", "La libertad, la igualdad, la fraternidad y la justicia.", "La justicia, la seguridad, la igualdad y la solidaridad."],
  "Son cuatro: libertad, justicia, igualdad y pluralismo político. La dignidad de la persona es el fundamento del orden político (art. 10.1).", ["la libertad, la justicia, la igualdad y el pluralismo político"])
Q("CE", "a3", "Contenido", "¿Qué artículo de la Constitución declara que el castellano es la lengua española oficial del Estado?", ["El artículo 3.", "El artículo 2.", "El artículo 4.", "El artículo 5."],
  "El art. 3 regula la lengua. El 2 trata de la unidad y la autonomía, el 4 de la bandera y el 5 de la capital.", ["El castellano es la lengua española oficial del Estado"])
Q("CE", "a17", "Contenido", "Según el artículo 17.2 de la Constitución, el plazo máximo de la detención preventiva es de:", ["Setenta y dos horas.", "Veinticuatro horas.", "Cuarenta y ocho horas.", "Diez días."],
  "El detenido debe ser puesto en libertad o a disposición judicial como máximo en **setenta y dos horas**. Los diez días son la detención gubernativa en el estado de excepción (LO 4/1981).", ["en el plazo máximo de setenta y dos horas"])
Q("CE", "a36", "Contenido", "¿A cuál de estas organizaciones exige expresamente la Constitución una estructura interna y un funcionamiento democráticos?", ["A los Colegios Profesionales.", "A las Fuerzas Armadas.", "A las Universidades.", "A las fundaciones."],
  "Lo exigen los arts. 6 (partidos), 7 (sindicatos y asociaciones empresariales), 36 (Colegios Profesionales) y 52 (organizaciones profesionales).", ["La estructura interna y el funcionamiento de los Colegios deberán ser democráticos"])
Q("CE", "a81", "Garantías", "Según el artículo 81.1 de la Constitución, son leyes orgánicas las relativas al desarrollo de:", ["Los derechos fundamentales y de las libertades públicas.", "Todos los derechos del Título I.", "Los principios rectores de la política social y económica.", "Los derechos y deberes de los ciudadanos de la sección 2.ª."],
  "Solo el desarrollo de los **derechos fundamentales y libertades públicas** (sección 1.ª, arts. 15 a 29) exige ley orgánica; el resto del Título I, ley ordinaria.", ["desarrollo de los derechos fundamentales y de las libertades públicas"])
Q("CE", "a81", "Garantías", "La aprobación, modificación o derogación de las leyes orgánicas exige:", ["Mayoría absoluta del Congreso, en una votación final sobre el conjunto del proyecto.", "Mayoría de tres quintos del Congreso y del Senado.", "Mayoría simple del Congreso.", "Mayoría de dos tercios del Congreso."],
  "Art. 81.2: **mayoría absoluta del Congreso** en votación final sobre el conjunto.", ["mayoría absoluta del Congreso, en una votación final sobre el conjunto del proyecto"])
Q("CE", "a53", "Garantías", "¿Para qué derechos prevé el art. 53.2 de la Constitución la tutela ante los tribunales ordinarios por un procedimiento basado en los principios de preferencia y sumariedad?", ["Los del artículo 14 y la Sección primera del Capítulo segundo.", "Todos los del Capítulo segundo.", "Todos los del Título I.", "Los de la Sección segunda del Capítulo segundo."],
  "El art. 53.2 cubre el **art. 14 y la sección 1.ª** del capítulo II (arts. 14 a 29). No todo el capítulo II (vinculan, art. 53.1), ni todo el Título I (Defensor, art. 54).", ["Cualquier ciudadano podrá recabar la tutela de las libertades y derechos reconocidos en el artículo 14 y la Sección primera del Capítulo segundo"])
Q("CE", "a53", "Garantías", "El recurso de amparo ante el Tribunal Constitucional es aplicable, según el art. 53.2 de la Constitución, además de a los derechos del artículo 14 y la Sección primera del Capítulo segundo, a:", ["La objeción de conciencia reconocida en el artículo 30.", "El derecho a la propiedad privada y a la herencia.", "El derecho al trabajo.", "El derecho a la protección de la salud."],
  "Solo la **objeción de conciencia del art. 30.2** de la sección 2.ª tiene amparo. La propiedad (33) y el trabajo (35) son de la sección 2.ª sin amparo; la salud (43) es del capítulo III.", ["Este último recurso será aplicable a la objeción de conciencia reconocida en el artículo 30"])
Q("CE", "a53", "Garantías", "Según el artículo 53.3 de la Constitución, los principios reconocidos en el Capítulo tercero:", ["Solo podrán ser alegados ante la Jurisdicción ordinaria de acuerdo con lo que dispongan las leyes que los desarrollen.", "Podrán ser alegados directamente ante el Tribunal Constitucional mediante recurso de amparo.", "Vinculan a todos los poderes públicos con la misma eficacia que los derechos del capítulo segundo.", "Solo pueden regularse por ley orgánica."],
  "Los principios rectores **informan** la legislación, la práctica judicial y la actuación de los poderes públicos, pero solo se alegan ante la jurisdicción ordinaria según las leyes que los desarrollen.", ["Sólo podrán ser alegados ante la Jurisdicción ordinaria de acuerdo con lo que dispongan las leyes que los desarrollen"])
Q("CE", "a54", "Garantías", "El Defensor del Pueblo, según el artículo 54 de la Constitución, es:", ["Alto comisionado de las Cortes Generales, designado por éstas para la defensa de los derechos comprendidos en el Título I.", "Alto comisionado del Gobierno, designado por el Consejo de Ministros.", "Órgano del Poder Judicial para la defensa de los derechos fundamentales.", "Alto comisionado del Congreso de los Diputados, designado para defender los derechos de la sección 1.ª."],
  "Es comisionado de las **Cortes Generales** (no del Gobierno ni del Congreso solo) y defiende **todos los derechos del Título I**, no solo los de la sección 1.ª.", ["alto comisionado de las Cortes Generales, designado por éstas para la defensa de los derechos comprendidos en este Título"])
Q("LOTC", "acuarentaycuatro", "Garantías", "El plazo para interponer el recurso de amparo frente a una violación originada en un acto u omisión de un órgano judicial es de:", ["30 días, a partir de la notificación de la resolución recaída en el proceso judicial.", "20 días, a partir de la notificación de la resolución recaída en el proceso judicial.", "Tres meses, desde que la resolución sea firme.", "Diez días, a partir de la publicación de la sentencia."],
  "Art. 44.2 LOTC: **30 días**. Los 20 días son para el Gobierno y los órganos ejecutivos de las CCAA (art. 43) y los 3 meses para las Cortes y Asambleas (art. 42).", ["El plazo para interponer el recurso de amparo será de 30 días"])
Q("LOTC", "acuarentaytres", "Garantías", "El plazo para interponer recurso de amparo frente a violaciones originadas por actos del Gobierno o de sus autoridades o funcionarios, una vez agotada la vía judicial, es de:", ["Veinte días siguientes a la notificación de la resolución recaída en el previo proceso judicial.", "Treinta días desde la notificación de la resolución.", "Tres meses desde que sea firme.", "Dos meses desde la publicación del acto."],
  "Art. 43.2 LOTC: **veinte días**. Contra órgano judicial: 30 días (art. 44). Contra decisiones de Cortes o Asambleas sin valor de ley: 3 meses (art. 42).", ["veinte días siguientes a la notificación de la resolución recaída en el previo proceso judicial"])
Q("LOTC", "acuarentaydos", "Garantías", "Las decisiones o actos sin valor de ley de las Cortes que violen derechos susceptibles de amparo podrán ser recurridas en amparo dentro del plazo de:", ["Tres meses desde que, con arreglo a las normas internas de las Cámaras, sean firmes.", "Veinte días desde su notificación.", "Treinta días desde su publicación.", "Un mes desde que sean firmes."],
  "Art. 42 LOTC: **tres meses** desde que sean firmes.", ["tres meses desde que, con arreglo a las normas internas de las Cámaras o Asambleas, sean firmes"])
Q("CE", "a162", "Garantías", "¿Quién NO está legitimado para interponer el recurso de inconstitucionalidad según el artículo 162.1.a) de la Constitución?", ["El Ministerio Fiscal.", "El Defensor del Pueblo.", "Cincuenta Diputados.", "El Presidente del Gobierno."],
  "Están legitimados el Presidente del Gobierno, el Defensor del Pueblo, 50 Diputados, 50 Senadores y los órganos ejecutivos y, en su caso, las Asambleas de las CCAA. El Ministerio Fiscal solo puede interponer amparo.", ["el Presidente del Gobierno, el Defensor del Pueblo, 50 Diputados, 50 Senadores"])
Q("LOTC", "atreintaytres", "Garantías", "El recurso de inconstitucionalidad se formulará dentro del plazo de:", ["Tres meses a partir de la publicación de la ley, disposición o acto con fuerza de ley impugnado.", "Dos meses a partir de su publicación.", "Seis meses a partir de su entrada en vigor.", "Un año a partir de su publicación."],
  "Art. 33.1 LOTC: **tres meses** desde la publicación (nueve meses en los casos del art. 33.2).", ["tres meses a partir de la publicación de la Ley, disposición o acto con fuerza de Ley impugnado"])
Q("CE", "a116", "Suspensión", "¿Quién declara el estado de sitio, según el artículo 116.4 de la Constitución?", ["El Congreso de los Diputados, por mayoría absoluta y a propuesta exclusiva del Gobierno.", "El Gobierno, mediante decreto acordado en Consejo de Ministros.", "El Gobierno, previa autorización del Congreso de los Diputados.", "Las Cortes Generales en sesión conjunta, por mayoría de tres quintos."],
  "El **Congreso** declara el sitio por **mayoría absoluta**, a propuesta **exclusiva** del Gobierno. El Gobierno declara la alarma (decreto) y la excepción (con autorización previa).", ["declarado por la mayoría absoluta del Congreso de los Diputados, a propuesta exclusiva del Gobierno"])
Q("CE", "a116", "Suspensión", "El estado de alarma será declarado por el Gobierno por un plazo máximo de:", ["Quince días, sin cuya autorización del Congreso no podrá ser prorrogado dicho plazo.", "Treinta días, prorrogables por otro plazo igual.", "Quince días, prorrogables libremente por el Gobierno.", "El que determine el Congreso de los Diputados."],
  "Alarma: **quince días**, y la prórroga necesita **autorización del Congreso**. Los 30 días prorrogables son de la excepción; la duración fijada por el Congreso, del sitio.", ["por un plazo máximo de quince días", "sin cuya autorización no podrá ser prorrogado dicho plazo"])
Q("CE", "a116", "Suspensión", "El estado de excepción:", ["Lo declara el Gobierno previa autorización del Congreso, por un plazo máximo de treinta días prorrogables por otro plazo igual.", "Lo declara el Congreso por mayoría absoluta, a propuesta del Gobierno.", "Lo declara el Gobierno dando cuenta al Congreso, por un plazo máximo de quince días.", "Lo declara el Gobierno sin intervención del Congreso, por treinta días no prorrogables."],
  "Excepción: **Gobierno con autorización previa del Congreso**, hasta **30 días** + otro plazo igual con los mismos requisitos.", ["previa autorización del Congreso de los Diputados", "que no podrá exceder de treinta días, prorrogables por otro plazo igual"])
Q("CE", "a55", "Suspensión", "¿Qué apartado de qué artículo queda exceptuado de la suspensión en el estado de excepción, aunque sí puede suspenderse en el de sitio?", ["El apartado 3 del artículo 17.", "El apartado 2 del artículo 18.", "El apartado 2 del artículo 17.", "El apartado 2 del artículo 28."],
  "El 55.1 exceptúa el **17.3** (garantías del detenido) en el estado de excepción; en el de sitio sí puede suspenderse (art. 32.3 LO 4/1981).", ["Se exceptúa de lo establecido anteriormente el apartado 3 del artículo 17 para el supuesto de declaración de estado de excepción"])
Q("CE", "a55", "Suspensión", "¿Cuál de estos derechos puede ser suspendido cuando se declare el estado de excepción o de sitio, según el artículo 55.1 de la Constitución?", ["El derecho de huelga (art. 28.2).", "El derecho a la vida (art. 15).", "La libertad ideológica y religiosa (art. 16).", "El derecho a la educación (art. 27)."],
  "El 55.1 enumera 17, 18.2 y 18.3, 19, 20.1.a) y d) y 20.5, 21, 28.2 y 37.2. Ni la vida, ni la libertad ideológica ni la educación están en la lista.", ["28, apartado 2"])
Q("CE", "a116", "Suspensión", "Mientras estén declarados los estados de alarma, excepción o sitio:", ["No podrá procederse a la disolución del Congreso.", "Podrá disolverse el Congreso si lo pide el Gobierno.", "Queda suspendido el funcionamiento de las Cámaras.", "Se suspende el principio de responsabilidad del Gobierno."],
  "Art. 116.5: **no puede disolverse el Congreso** y no se interrumpe el funcionamiento de las Cámaras ni de los demás poderes; art. 116.6: no se modifica la responsabilidad del Gobierno y sus agentes.", ["No podrá procederse a la disolución del Congreso"])
Q("CE", "a55", "Suspensión", "Según el artículo 55.2 de la Constitución, una ley orgánica podrá determinar los casos en que, de forma individual, pueden ser suspendidos para personas determinadas los derechos de los artículos:", ["17.2, 18.2 y 18.3.", "17, 19 y 21.", "18.1, 20 y 28.2.", "15, 16 y 17.1."],
  "La suspensión **individual** (bandas armadas y elementos terroristas) afecta a **17.2, 18.2 y 18.3**, con intervención judicial y control parlamentario.", ["los derechos reconocidos en los artículos 17, apartado 2, y 18, apartados 2 y 3"])
Q("CE", "a159", "Tribunal Constitucional", "El Tribunal Constitucional se compone de 12 miembros nombrados por el Rey; de ellos, a propuesta del Gobierno:", ["Dos.", "Cuatro.", "Tres.", "Seis."],
  "4 a propuesta del Congreso, 4 del Senado, **2 del Gobierno** y 2 del Consejo General del Poder Judicial.", ["dos a propuesta del Gobierno, y dos a propuesta del Consejo General del Poder Judicial"])
Q("CE", "a159", "Tribunal Constitucional", "Los miembros del Tribunal Constitucional serán designados por un período de:", ["Nueve años y se renovarán por terceras partes cada tres.", "Seis años y se renovarán por mitades cada tres.", "Nueve años y se renovarán por mitades cada cuatro y medio.", "Doce años sin renovación."],
  "Art. 159.3: **nueve años**, renovación **por terceras partes cada tres**.", ["nueve años y se renovarán por terceras partes cada tres"])
Q("CE", "a160", "Tribunal Constitucional", "El Presidente del Tribunal Constitucional es nombrado:", ["Entre sus miembros por el Rey, a propuesta del Tribunal en pleno, por tres años.", "Por el Rey, a propuesta del Gobierno, por nueve años.", "Por el Congreso de los Diputados, por mayoría de tres quintos.", "Por el Consejo General del Poder Judicial, por cinco años."],
  "Art. 160: lo nombra el **Rey**, **entre sus miembros**, a propuesta del **Pleno del Tribunal**, por **tres años**.", ["nombrado entre sus miembros por el Rey, a propuesta del mismo Tribunal en pleno y por un período de tres años"])
Q("CE", "a159", "Tribunal Constitucional", "Los miembros del Tribunal Constitucional deberán ser nombrados entre juristas de reconocida competencia con:", ["Más de quince años de ejercicio profesional.", "Más de diez años de ejercicio profesional.", "Más de veinte años de ejercicio profesional.", "Más de cinco años de ejercicio profesional."],
  "Art. 159.2: **más de quince años** de ejercicio profesional (Magistrados y Fiscales, Profesores de Universidad, funcionarios públicos y Abogados).", ["más de quince años de ejercicio profesional"])
Q("CE", "a164", "Tribunal Constitucional", "Las sentencias del Tribunal Constitucional tienen el valor de cosa juzgada:", ["A partir del día siguiente de su publicación, y no cabe recurso alguno contra ellas.", "Desde la fecha de la sentencia, y cabe recurso ante el Pleno.", "A partir del mes siguiente a su publicación.", "Desde su notificación a las partes, con recurso de súplica."],
  "Art. 164.1: se publican en el BOE con los votos particulares, tienen valor de cosa juzgada **desde el día siguiente a su publicación** y **no cabe recurso alguno**.", ["valor de cosa juzgada a partir del día siguiente de su publicación y no cabe recurso alguno contra ellas"])
Q("CE", "a163", "Tribunal Constitucional", "¿Quién plantea la cuestión de inconstitucionalidad ante el Tribunal Constitucional?", ["Un órgano judicial que considere que una norma con rango de ley aplicable al caso, de cuya validez dependa el fallo, pueda ser contraria a la Constitución.", "Cualquier ciudadano que se considere perjudicado por una ley.", "El Defensor del Pueblo, de oficio.", "El Gobierno, cuando una ley autonómica invada sus competencias."],
  "Art. 163 CE: la plantea el **órgano judicial** (en el proceso, de oficio o a instancia de parte, una vez concluso y dentro del plazo para dictar sentencia: art. 35 LOTC).", ["Cuando un órgano judicial considere"])
Q("CE", "a161", "Tribunal Constitucional", "Cuando el Gobierno impugna ante el Tribunal Constitucional disposiciones y resoluciones adoptadas por los órganos de las Comunidades Autónomas, la impugnación produce la suspensión, pero el Tribunal deberá ratificarla o levantarla en un plazo no superior a:", ["Cinco meses.", "Un mes.", "Tres meses.", "Seis meses."],
  "Art. 161.2: **cinco meses**.", ["en un plazo no superior a cinco meses"])
Q("LODP", "asegundo", "Defensor del Pueblo", "Para la elección del Defensor del Pueblo, el Pleno del Congreso designará a quien obtenga:", ["Una votación favorable de las tres quintas partes de sus miembros, ratificada por la misma mayoría del Senado en un plazo máximo de veinte días.", "Mayoría simple del Congreso, ratificada por el Senado en un mes.", "Dos tercios del Congreso y mayoría absoluta del Senado.", "Mayoría absoluta de cada Cámara reunidas en sesión conjunta."],
  "Art. 2.4 LO 3/1981: **3/5 del Congreso** y ratificación, en **veinte días**, por la misma mayoría del Senado. Si no se alcanzan, el Senado puede ratificar por **mayoría absoluta** (art. 2.5).", ["tres quintas partes de los miembros del Congreso", "en un plazo máximo de veinte días"])
Q("LODP", "asegundo", "Defensor del Pueblo", "El Defensor del Pueblo será elegido por las Cortes Generales para un periodo de:", ["Cinco años.", "Cuatro años.", "Seis años.", "Nueve años."],
  "Art. 2.1 LO 3/1981: **cinco años**.", ["para un periodo de cinco años"])
Q("LODP", "aquince", "Defensor del Pueblo", "Toda queja ante el Defensor del Pueblo se presentará en el plazo máximo de:", ["Un año, contado a partir del momento en que se tuviera conocimiento de los hechos.", "Seis meses desde la notificación del acto.", "Dos meses desde que se agote la vía administrativa.", "Tres años desde que ocurran los hechos."],
  "Art. 15.1 LO 3/1981: **un año** desde que se conocen los hechos; la queja es gratuita y sin abogado ni procurador.", ["en el plazo máximo de un año"])
Q("LODP", "aoctavo", "Defensor del Pueblo", "El Defensor del Pueblo estará auxiliado por:", ["Un Adjunto Primero y un Adjunto Segundo.", "Tres Adjuntos.", "Un único Adjunto.", "Cuatro Adjuntos, uno por cada grupo parlamentario."],
  "Art. 8.1 LO 3/1981: **dos** Adjuntos, a los que nombra y separa él previa conformidad de las Cámaras.", ["Adjunto Primero y un Adjunto Segundo"])
Q("CE", "a166", "Reforma", "La iniciativa de reforma constitucional se ejercerá en los términos previstos en los apartados 1 y 2 del artículo 87. Por tanto, NO puede ejercerla:", ["La iniciativa popular.", "El Gobierno.", "Las Asambleas de las Comunidades Autónomas.", "El Senado."],
  "El art. 166 remite a los apartados 1 y 2 del art. 87 (Gobierno, Congreso, Senado y Asambleas autonómicas); la **iniciativa popular** es el 87.3 y queda fuera.", ["apartados 1 y 2 del artículo 87"])
Q("CE", "a167", "Reforma", "Según el artículo 167 de la Constitución, los proyectos de reforma constitucional deberán ser aprobados por:", ["Una mayoría de tres quintos de cada una de las Cámaras.", "Una mayoría de dos tercios de cada una de las Cámaras.", "Mayoría absoluta del Congreso.", "Mayoría de tres quintos del Congreso y mayoría simple del Senado."],
  "Art. 167.1: **3/5 de cada Cámara**. Los 2/3 son del art. 168 (y del Congreso en el 167.2).", ["una mayoría de tres quintos de cada una de las Cámaras"])
Q("CE", "a167", "Reforma", "Aprobada la reforma por las Cortes Generales por el procedimiento del art. 167, será sometida a referéndum para su ratificación cuando así lo soliciten:", ["Una décima parte de los miembros de cualquiera de las Cámaras, dentro de los quince días siguientes a su aprobación.", "Una quinta parte de los miembros de cualquiera de las Cámaras, dentro del mes siguiente.", "Cincuenta Diputados o cincuenta Senadores, dentro de los treinta días siguientes.", "El Gobierno, dentro de los quince días siguientes."],
  "Art. 167.3: referéndum **facultativo**: **1/10** de los miembros de cualquier Cámara, en **15 días**.", ["una décima parte de los miembros de cualquiera de las Cámaras"])
Q("CE", "a168", "Reforma", "Cuando se propusiere la revisión total de la Constitución o una parcial que afecte al Título preliminar, se procederá a la aprobación del principio por mayoría de:", ["Dos tercios de cada Cámara y a la disolución inmediata de las Cortes.", "Tres quintos de cada Cámara y al referéndum facultativo.", "Mayoría absoluta de cada Cámara y a la convocatoria de elecciones.", "Dos tercios del Congreso y mayoría absoluta del Senado."],
  "Art. 168.1: **2/3 de cada Cámara** y **disolución inmediata** de las Cortes; las nuevas Cámaras ratifican y aprueban el texto por 2/3 y se somete a **referéndum obligatorio**.", ["mayoría de dos tercios de cada Cámara, y a la disolución inmediata de las Cortes"])
Q("CE", "a168", "Reforma", "El procedimiento agravado de reforma del art. 168 se aplica cuando la reforma afecte:", ["Al Título preliminar, al Capítulo segundo, Sección primera del Título I, o al Título II.", "Al Título I completo y al Título II.", "A los artículos 14 a 38 y al Título VIII.", "Al Título preliminar, al Título I y al Título X."],
  "Solo se protege con el 168 la **revisión total**, el **Título preliminar**, la **sección 1.ª del capítulo II del Título I** (15-29, no el 14) y el **Título II** (la Corona).", ["al Título preliminar, al Capítulo segundo, Sección primera del Título I, o al Título II"])
Q("CE", "a169", "Reforma", "No podrá iniciarse la reforma constitucional:", ["En tiempo de guerra o de vigencia de alguno de los estados previstos en el artículo 116.", "Durante los seis meses anteriores a unas elecciones generales.", "Mientras esté disuelto el Congreso.", "En los dos años siguientes a otra reforma."],
  "Art. 169: ni en **tiempo de guerra** ni durante los estados de **alarma, excepción o sitio** (art. 116).", ["en tiempo de guerra o de vigencia de alguno de los estados previstos en el artículo 116"])
Q("CE", "a13", "Reforma", "La reforma constitucional de 1992 modificó el artículo 13.2 para:", ["Reconocer a los extranjeros, por reciprocidad, el derecho de sufragio activo y pasivo en las elecciones municipales.", "Establecer el principio de estabilidad presupuestaria.", "Sustituir el término «disminuidos» por «personas con discapacidad».", "Crear una circunscripción propia en el Senado para la isla de Formentera."],
  "La reforma de 1992 (art. 13.2) añadió el sufragio **pasivo** en las municipales. La de 2011 (135) es la estabilidad presupuestaria; la de 2024 (49), la discapacidad; la de 2026 (69.3), las islas del Senado.", ["sufragio activo y pasivo en las elecciones municipales"])

# ---------------------------------------------------------------------------- FLASHCARDS
FC = [
 ("¿Qué verbo corresponde a cada hecho de 1978: Cortes, pueblo, Rey y BOE?", "Las **Cortes aprueban** (31-10), el **pueblo ratifica** (6-12), el **Rey sanciona y promulga** (27-12) y el **BOE publica** y la Constitución **entra en vigor** (29-12). Preámbulo y fórmula final.", "Fechas"),
 ("¿Qué artículos de la Constitución se han reformado y en qué año?", "**13.2** (1992, sufragio pasivo municipal) · **135** (2011, estabilidad presupuestaria) · **49** (2024, discapacidad) · **69.3** (2026, islas del Senado). Cuatro reformas, por el art. 167.", "Fechas"),
 ("¿Qué es la parte dogmática y la orgánica?", "**Dogmática**: arts. **1 a 55** (Título preliminar y Título I). **Orgánica**: arts. **56 a 169** (Títulos II a X).", "Estructura"),
 ("¿Cuántos títulos, artículos y disposiciones tiene la Constitución?", "**11 títulos** (preliminar + I a X), **169 artículos** y **15 disposiciones**: **4** adicionales, **9** transitorias, **1** derogatoria y **1** final («4-9-1-1»).", "Estructura"),
 ("¿Qué artículos comprende cada capítulo del Título I?", "Art. **10** (suelto) · cap. I **11-13** · cap. II **14-38** (art. 14 suelto, secc. 1.ª **15-29**, secc. 2.ª **30-38**) · cap. III **39-52** · cap. IV **53-54** · cap. V **55**.", "Estructura"),
 ("¿Qué dos artículos del Título I quedan «sueltos» y por qué?", "El **art. 10** (fuera de los capítulos) y el **art. 14** (fuera de las secciones): dicen lo más general (dignidad e igualdad) y se concretan en los derechos siguientes.", "Estructura"),
 ("¿Qué artículos exigen estructura interna y funcionamiento democráticos?", "Art. **6** (partidos), **7** (sindicatos y asociaciones empresariales), **36** (Colegios Profesionales) y **52** (organizaciones profesionales).", "Contenido"),
 ("¿Cuáles son los valores superiores del ordenamiento jurídico (art. 1.1)?", "**Libertad, justicia, igualdad y pluralismo político.** La dignidad de la persona es el fundamento del orden político (art. 10.1).", "Contenido"),
 ("¿Qué garantiza el art. 9.3 de la Constitución?", "Siete principios: **legalidad, jerarquía normativa, publicidad de las normas, irretroactividad** de las disposiciones sancionadoras no favorables o restrictivas de derechos individuales, **seguridad jurídica, responsabilidad** e **interdicción de la arbitrariedad** de los poderes públicos (art. 9.3).", "Contenido"),
 ("¿Cuánto puede durar la detención preventiva (art. 17.2)?", "**72 horas** como máximo; después, libertad o disposición de la autoridad judicial.", "Contenido"),
 ("¿Qué garantizan los apartados 2 y 3 del art. 18?", "**Domicilio inviolable** (18.2) y **secreto de las comunicaciones** (18.3): suspendibles con estado de excepción o sitio (art. 55.1) y en la suspensión individual (art. 55.2).", "Contenido"),
 ("Niveles de protección: ¿qué garantías tiene la sección 1.ª (arts. 15 a 29)?", "**Todas**: ley orgánica (art. 81.1), solo por ley, tutela preferente y sumaria (art. 53.2), amparo, inconstitucionalidad, vinculación a los poderes públicos y Defensor del Pueblo.", "Garantías"),
 ("¿Qué garantías tiene el art. 14?", "**Todas menos la ley orgánica**: tutela preferente y sumaria y amparo (art. 53.2), inconstitucionalidad, vinculación y Defensor.", "Garantías"),
 ("¿Qué garantías tiene la sección 2.ª (arts. 30 a 38)?", "Vinculación, solo por ley e inconstitucionalidad (art. 53.1) y Defensor. **No** tiene ley orgánica, tutela preferente y sumaria ni amparo, **salvo el art. 30.2** (objeción de conciencia).", "Garantías"),
 ("¿Qué garantías tienen los principios rectores del capítulo III (arts. 39 a 52)?", "Solo **informan** la legislación, la práctica judicial y la actuación de los poderes públicos y se alegan ante la jurisdicción ordinaria **según las leyes** que los desarrollen (art. 53.3). Cuenta con el Defensor (art. 54).", "Garantías"),
 ("¿Qué derechos se regulan por ley orgánica según el art. 81.1?", "El desarrollo de los **derechos fundamentales y libertades públicas** (secc. 1.ª, 15-29), los Estatutos de Autonomía, el régimen electoral general **y las demás previstas en la Constitución** (art. 81.1). Mayoría absoluta del Congreso (art. 81.2).", "Garantías"),
 ("¿Qué derechos puede proteger el recurso de amparo?", "El **art. 14**, los de la **sección 1.ª (15-29)** y la **objeción de conciencia (art. 30.2)** (art. 53.2; art. 41 LOTC). Es el «último remedio»: tras agotar la vía judicial.", "Garantías"),
 ("¿Cuáles son los plazos del recurso de amparo?", "**3 meses** (Cortes y Asambleas, art. 42 LOTC) · **20 días** (Gobierno y órganos ejecutivos de las CCAA, art. 43) · **30 días** (órgano judicial, art. 44).", "Garantías"),
 ("¿Quién puede interponer el recurso de inconstitucionalidad y en qué plazo?", "**Presidente del Gobierno, Defensor del Pueblo, 50 Diputados, 50 Senadores** y órganos ejecutivos y Asambleas de las CCAA (art. 162.1.a). **3 meses** desde la publicación (art. 33 LOTC).", "Garantías"),
 ("¿Quién interpone el recurso de amparo?", "**Persona natural o jurídica con interés legítimo**, **Defensor del Pueblo** y **Ministerio Fiscal** (art. 162.1.b; art. 46 LOTC).", "Garantías"),
 ("¿Quién declara cada estado y con qué requisito (art. 116)?", "**Alarma**: Gobierno (decreto), dando cuenta al Congreso. **Excepción**: Gobierno (decreto), **previa autorización del Congreso**. **Sitio**: **Congreso**, **mayoría absoluta**, a propuesta **exclusiva** del Gobierno (art. 116.2 a 116.4).", "Suspensión"),
 ("¿Cuánto dura cada estado?", "**Alarma 15 días** (prórroga con autorización del Congreso) · **Excepción 30 días** prorrogables por otro plazo igual · **Sitio: el que determine el Congreso**. Regla: **15-30-Congreso**.", "Suspensión"),
 ("¿Qué derecho se salva del estado de excepción pero no del de sitio?", "El **art. 17.3** (derechos del detenido): el art. 55.1 lo exceptúa solo «para el supuesto de declaración de estado de excepción».", "Suspensión"),
 ("¿Qué derechos se pueden suspender en excepción y sitio (art. 55.1)?", "**17** (salvo 17.3 en excepción), **18.2**, **18.3**, **19**, **20.1.a) y d)**, **20.5**, **21**, **28.2** y **37.2**.", "Suspensión"),
 ("¿Y en el estado de alarma?", "**Ningún** derecho se suspende: solo se pueden decretar algunas **limitaciones** (circulación, requisas, prestaciones…; art. 11 LO 4/1981).", "Suspensión"),
 ("¿Qué no puede hacerse mientras duren los estados del art. 116?", "**Disolver el Congreso**, **interrumpir** el funcionamiento de las Cámaras y de los demás poderes, modificar la **responsabilidad** del Gobierno y **reformar la Constitución** (arts. 116.5, 116.6 y 169).", "Suspensión"),
 ("¿Qué es la suspensión individual (art. 55.2)?", "Ley orgánica para **personas determinadas** vinculadas a **bandas armadas o terroristas**: derechos **17.2, 18.2 y 18.3**, con intervención judicial y control parlamentario.", "Suspensión"),
 ("¿Cómo se compone el Tribunal Constitucional?", "**12 miembros** nombrados por el Rey: **4 Congreso** (3/5), **4 Senado** (3/5, entre candidaturas de las Asambleas autonómicas), **2 Gobierno** y **2 CGPJ** (art. 159.1; art. 16 LOTC).", "Tribunal Constitucional"),
 ("¿Cuánto dura el mandato en el TC y cómo se renueva?", "**9 años**, renovación **por terceras partes cada 3** (art. 159.3). El Presidente, **3 años**, reelegible una vez (art. 160; art. 9 LOTC).", "Tribunal Constitucional"),
 ("¿Qué requisitos tienen los miembros del TC?", "Magistrados y Fiscales, Profesores de Universidad, funcionarios públicos y Abogados, **juristas de reconocida competencia con más de 15 años** de ejercicio (art. 159.2). Presencia equilibrada: al menos un **40 %** de cada sexo en las propuestas (art. 16 LOTC).", "Tribunal Constitucional"),
 ("¿Qué valor tienen las sentencias del TC (art. 164)?", "**BOE con votos particulares**, **cosa juzgada al día siguiente**, **sin recurso**, **plenos efectos frente a todos** (inconstitucionalidad y las que no se limiten a la estimación subjetiva de un derecho) y **vigencia de la parte no afectada** de la ley.", "Tribunal Constitucional"),
 ("¿Cuándo se plantea la cuestión de inconstitucionalidad?", "Por el **órgano judicial**, **una vez concluso el procedimiento** y dentro del plazo para dictar sentencia, si duda de una norma con rango de ley aplicable cuya validez dependa el fallo (art. 163; art. 35 LOTC).", "Tribunal Constitucional"),
 ("¿Qué conflictos conoce el TC?", "De competencia (Estado-CCAA y CCAA entre sí: art. 161.1.c), **entre órganos constitucionales** (Gobierno, Congreso, Senado, CGPJ), **de defensa de la autonomía local** (art. 59 LOTC) y la impugnación del Gobierno de disposiciones de las CCAA (art. 161.2).", "Tribunal Constitucional"),
 ("¿Qué es y cómo se elige el Defensor del Pueblo?", "**Alto comisionado de las Cortes Generales** (art. 54). La Comisión Mixta propone; **3/5 del Congreso** y ratificación **3/5 del Senado** en 20 días; si no, **3/5 Congreso + mayoría absoluta Senado**. Firman los **dos Presidentes** y se publica en el BOE.", "Defensor del Pueblo"),
 ("¿Cuánto dura el mandato del Defensor del Pueblo y quién lo auxilia?", "**5 años** (art. 2.1 LO 3/1981). **Dos Adjuntos** nombrados por él con conformidad de las Cámaras (art. 8).", "Defensor del Pueblo"),
 ("¿Qué puede y qué no puede hacer el Defensor del Pueblo?", "Investiga de oficio o a petición de parte (**sumaria e informal**), supervisa la Administración **estatal y autonómica**, puede interponer **amparo e inconstitucionalidad**; **no puede anular** actos de la Administración, solo **recomendar y sugerir**. Queja: **1 año** (arts. 9, 12, 15, 18, 28 y 29 LO 3/1981).", "Defensor del Pueblo"),
 ("¿Quién tiene iniciativa de reforma constitucional?", "Los del **art. 87.1 y 87.2** (art. 166): Gobierno, Congreso, Senado y Asambleas de las CCAA. **No** la iniciativa popular (87.3).", "Reforma"),
 ("Reforma por el art. 167: mayorías y referéndum", "**3/5 de cada Cámara**; sin acuerdo, Comisión **paritaria**; si no, **mayoría absoluta del Senado + 2/3 del Congreso**. **Referéndum solo si lo pide 1/10** de los miembros de cualquier Cámara en **15 días** (art. 167).", "Reforma"),
 ("Reforma por el art. 168: ¿cuándo y cómo?", "**Revisión total** o parcial del **Título preliminar**, **sección 1.ª del cap. II del Título I** o **Título II**: principio por **2/3 de cada Cámara**, **disolución inmediata**, las nuevas Cámaras **ratifican** y aprueban por **2/3**, **referéndum obligatorio** (art. 168).", "Reforma"),
 ("¿Cuándo no puede iniciarse una reforma constitucional?", "En **tiempo de guerra** o durante los estados de **alarma, excepción o sitio** (art. 169).", "Reforma"),
]
for q_, a_, cat in FC: T.fc(q_, a_, cat)

# ---------------------------------------------------------------------------- GLOSARIO
GL = [
 ("Parte dogmática", "Arts. 1 a 55 (Título preliminar y Título I): principios y derechos y deberes fundamentales.", "s3", "Estructura"),
 ("Parte orgánica", "Arts. 56 a 169 (Títulos II a X): organización del Estado y sus instituciones.", "s3", "Estructura"),
 ("Disposiciones (4-9-1-1)", "Cuatro adicionales, nueve transitorias, una derogatoria y una final, que cierran la Constitución.", "s7", "Estructura"),
 ("Derechos fundamentales y libertades públicas", "Los de la sección 1.ª del capítulo II del Título I (arts. 15 a 29): los que reciben la máxima protección.", "s5", "Garantías"),
 ("Principios rectores", "Los del capítulo III del Título I (arts. 39 a 52): informan la actuación de los poderes públicos pero no son derechos fundamentales.", "s25", "Garantías"),
 ("Reserva de ley orgánica", "Materias que solo pueden regularse por ley orgánica (art. 81.1): entre ellas, el desarrollo de los derechos fundamentales y libertades públicas.", "s19", "Garantías"),
 ("Contenido esencial", "Núcleo que la ley debe respetar al regular el ejercicio de los derechos y libertades del capítulo II (art. 53.1).", "s19", "Garantías"),
 ("Tutela preferente y sumaria", "Protección ante los tribunales ordinarios, por un procedimiento basado en los principios de preferencia y sumariedad (art. 53.2).", "s20", "Garantías"),
 ("Recurso de amparo", "Recurso ante el Tribunal Constitucional por violación de los derechos del art. 14, la sección 1.ª y el art. 30.2, tras agotar la vía judicial.", "s21", "Garantías"),
 ("Recurso de inconstitucionalidad", "Recurso ante el Tribunal Constitucional contra leyes y normas con fuerza de ley (arts. 161.1.a y 162.1.a).", "s23", "Garantías"),
 ("Cuestión de inconstitucionalidad", "La plantea un órgano judicial ante el TC cuando duda de la constitucionalidad de una norma con rango de ley aplicable al caso (art. 163).", "s35", "Tribunal Constitucional"),
 ("Estado de alarma", "Declarado por el Gobierno por decreto, hasta 15 días, con cuenta al Congreso; no suspende derechos (art. 116.2).", "s28", "Suspensión"),
 ("Estado de excepción", "Declarado por el Gobierno con autorización previa del Congreso, hasta 30 días prorrogables por otro plazo igual (art. 116.3).", "s28", "Suspensión"),
 ("Estado de sitio", "Declarado por el Congreso por mayoría absoluta a propuesta exclusiva del Gobierno; el Congreso fija su duración (art. 116.4).", "s28", "Suspensión"),
 ("Suspensión individual", "Suspensión de los derechos 17.2, 18.2 y 18.3 para personas determinadas, por actuación de bandas armadas o terroristas (art. 55.2).", "s31", "Suspensión"),
 ("Diputación Permanente", "Órgano que asume las competencias del Congreso si está disuelto o ha expirado su mandato durante un estado del art. 116 (art. 116.5).", "s30", "Suspensión"),
 ("Tribunal Constitucional", "Intérprete supremo de la Constitución, único en su orden, de 12 miembros nombrados por el Rey (arts. 159 a 165).", "s33", "Tribunal Constitucional"),
 ("Cosa juzgada", "Efecto de las sentencias del TC desde el día siguiente a su publicación; contra ellas no cabe recurso (art. 164.1).", "s36", "Tribunal Constitucional"),
 ("Defensor del Pueblo", "Alto comisionado de las Cortes Generales para defender los derechos del Título I y supervisar la Administración (art. 54).", "s39", "Defensor del Pueblo"),
 ("Comisión Mixta Congreso-Senado", "Comisión de las Cortes que se relaciona con el Defensor del Pueblo y propone a los Plenos su candidato.", "s40", "Defensor del Pueblo"),
 ("Comisión de composición paritaria", "Comisión de Diputados y Senadores que intenta un texto de acuerdo cuando las Cámaras no aprueban la reforma del art. 167.", "s45", "Reforma"),
 ("Referéndum de ratificación", "Votación del pueblo sobre una reforma ya aprobada: facultativo en el art. 167, obligatorio en el 168.", "s46", "Reforma"),
 ("Iniciativa legislativa popular", "La regula el art. 87.3; no puede ejercerse para reformar la Constitución (art. 166).", "s44", "Reforma"),
 ("Sanción y promulgación", "Actos del Rey que dan validez y publicidad a la norma; la Constitución se sancionó el 27-12-1978.", "s1", "Fechas"),
]
for t_, d_, s_, cat in GL: T.glos(t_, d_, s_, cat)

# ---------------------------------------------------------------------------- HITOS
T.hito("1978", "31-10-1978: las Cortes Generales aprueban la Constitución · 6-12-1978: referéndum de ratificación · 27-12-1978: sanción y promulgación · 29-12-1978: publicación en el BOE y entrada en vigor", "Aprobación, ratificación, sanción y entrada en vigor", "normativo", "s1")
T.hito("1979", "LO 2/1979, de 3 de octubre, del Tribunal Constitucional (BOE de 5-10-1979)", "Desarrolla el Título IX: composición, competencias y procedimientos", "normativo", "s33")
T.hito("1980", "LO 2/1980, de 18 de enero, de referéndum (BOE de 23-1-1980)", "Referéndum de reforma constitucional: arts. 2, 4 y 7", "normativo", "s45")
T.hito("1981", "LO 3/1981, de 6 de abril, del Defensor del Pueblo (BOE de 7-5-1981)", "Desarrolla el art. 54: elección, mandato y funciones", "normativo", "s39")
T.hito("1981", "LO 4/1981, de 1 de junio, de los estados de alarma, excepción y sitio (BOE de 5-6-1981)", "Desarrolla el art. 116", "normativo", "s28")
T.hito("1992", "Reforma del art. 13.2 (27-8-1992; BOE de 28-8-1992)", "Primera reforma: sufragio pasivo en las elecciones municipales", "normativo", "s2")
T.hito("2011", "Reforma del art. 135 (27-9-2011; BOE de 27-9-2011)", "Estabilidad presupuestaria", "normativo", "s2")
T.hito("2024", "Reforma del art. 49 (15-2-2024; BOE de 17-2-2024)", "Personas con discapacidad", "normativo", "s2")
T.hito("2026", "Reforma del art. 69.3 (19-5-2026; BOE de 20-5-2026)", "Circunscripciones del Senado en las islas: Ibiza y Formentera", "normativo", "s2")

T.publicar()
