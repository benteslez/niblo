# -*- coding: utf-8 -*-
"""Tema I.1 (B1T01): La Constitución Española de 1978: estructura y contenido. La reforma
de la Constitución.
Método del I.2: mapa → bloques (I a IV) con guía; cada artículo, texto literal del BOE +
ficha de casillas fijas; cierre 1 (preguntas oficiales) y cierre 2 (repaso).
Normas (textos del BOE): CE (preámbulo, títulos, arts. 1 a 9, 75, 87, 95, 116, 166 a 169 y
disposiciones); Reglamento del Congreso (arts. 146 y 147); Reglamento del Senado (arts. 152 a
159); LO 2/1980, de referéndum (arts. 2, 4 y 7); Reformas de la Constitución de 1992, 2011,
2024 y 2026 (texto publicado en el BOE). La estructura (títulos, capítulos, secciones, número de
artículos y de disposiciones) se calcula sobre el texto consolidado del BOE y se comprueba."""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO["RS"] = "Reglamento del Senado"
CORTO["LO2_1980"] = "LO 2/1980, de referéndum"
CE_URL = "https://www.boe.es/buscar/act.php?id=BOE-A-1978-31229"

# -----------------------------------------------------------------------------
# Estructura de la Constitución calculada sobre el texto consolidado del BOE
def _estructura():
    L = boe.ley("CE"); tits = []; disp = {"adicional": [], "transitoria": [], "derogatoria": [], "final": []}
    t = cap = sec = None
    for b, (tit, ps) in L.items():
        txt = [p for _, p in ps]
        if tit.startswith("TÍTULO"):
            t = {"b": b, "num": txt[0], "rub": txt[1] if len(txt) > 1 else None, "arts": [], "caps": []}; tits.append(t); cap = sec = None
        elif tit.startswith("CAPÍTULO"):
            cap = {"b": b, "num": txt[0], "rub": txt[1], "arts": [], "secs": []}; t["caps"].append(cap); sec = None
        elif tit.startswith("SECCIÓN"):
            sec = {"b": b, "rub": txt[0], "arts": []}; cap["secs"].append(sec)
        elif re.fullmatch(r"Artículo \d+", tit):
            n = int(tit.split()[1]); t["arts"].append(n)
            if cap: cap["arts"].append(n)
            if sec: sec["arts"].append(n)
        elif tit.startswith("Disposición"):
            t = cap = sec = None
            for k in disp:
                if tit.startswith("Disposición " + k): disp[k].append(b)
    return tits, disp
TITS, DISP = _estructura()
TIT = {t["num"]: t for t in TITS}
def rango(a): assert a == list(range(a[0], a[-1] + 1)), a; return f"{a[0]} a {a[-1]}" if len(a) > 1 else str(a[0])
# Comprobaciones de lo que se afirma en los apuntes
TODOS = [n for t in TITS for n in t["arts"]]
assert TODOS == list(range(1, 170)), "La CE no tiene 169 artículos correlativos"
assert len(TITS) == 11 and TITS[0]["num"] == "TÍTULO PRELIMINAR" and TITS[0]["rub"] is None
assert [len(DISP[k]) for k in ("adicional", "transitoria", "derogatoria", "final")] == [4, 9, 1, 1], DISP
assert rango(TIT["TÍTULO PRELIMINAR"]["arts"]) == "1 a 9" and rango(TIT["TÍTULO X"]["arts"]) == "166 a 169"
assert [len(TIT[x]["caps"]) for x in ("TÍTULO I", "TÍTULO III", "TÍTULO VIII")] == [5, 3, 3]
assert sum(len(t["caps"]) for t in TITS) == 11 and sum(len(cp["secs"]) for t in TITS for cp in t["caps"]) == 2
assert max(len(t["arts"]) for t in TITS) == len(TIT["TÍTULO I"]["arts"]) and 103 in TIT["TÍTULO IV"]["arts"]
assert TIT["TÍTULO I"]["arts"][0] == 10 and TIT["TÍTULO I"]["caps"][0]["arts"][0] == 11   # el art. 10 va antes del Capítulo primero
assert TIT["TÍTULO I"]["caps"][1]["arts"][0] == 14 and TIT["TÍTULO I"]["caps"][1]["secs"][0]["arts"][0] == 15   # el art. 14, antes de la Sección 1.ª

DONDE = {"TÍTULO PRELIMINAR": "Este tema (→ II.1 a → II.4)", "TÍTULO I": "Tema I.2", "TÍTULO II": "Tema I.4",
         "TÍTULO III": "Tema I.5 (la ley y sus clases, tema IV.2)", "TÍTULO IV": "Tema I.6", "TÍTULO V": "Tema I.6",
         "TÍTULO VI": "Tema I.7", "TÍTULO VII": "Por partes (p. ej., art. 133 en el tema IV.2 y art. 135 en el VI.1)",
         "TÍTULO VIII": "Temas I.10 y I.11", "TÍTULO IX": "Tema I.3", "TÍTULO X": "Este tema (→ III.1 a → III.5)"}
def _rub(t): return c("CE", t["b"], t["rub"]) if t["rub"] else "(sin rúbrica)"
TABLA_TITULOS = "\n".join(["| Título | Rúbrica (literal) | Artículos | Capítulos | Se estudia en |", "|---|---|---|---|---|"] + [
    f"| **{t['num'].replace('TÍTULO ', '')}** | {_rub(t)} | {rango(t['arts'])} | {len(t['caps']) or '—'} | {DONDE[t['num']]} |" for t in TITS])
# I.2.1 (estructura) sin la columna «Se estudia en», que es la de II.5 (contenido): evita el cuadro duplicado
TABLA_ESTRUCTURA = "\n".join(["| Título | Rúbrica (literal) | Artículos | Capítulos |", "|---|---|---|---|"] + [
    f"| **{t['num'].replace('TÍTULO ', '')}** | {_rub(t)} | {rango(t['arts'])} | {len(t['caps']) or '—'} |" for t in TITS])
def _filas_caps(t):
    out = []
    for cp in t["caps"]:
        out.append(f"| {t['num'].replace('TÍTULO ', 'Título ')} | {cp['num'].capitalize()}: {c('CE', cp['b'], cp['rub'])} | {rango(cp['arts'])} |")
        for s in cp["secs"]:
            out.append(f"| | ↳ {c('CE', s['b'], s['rub'])} | {rango(s['arts'])} |")
    return out
TABLA_CAPS = "\n".join(["| Título | Capítulo o sección (rúbrica literal) | Artículos |", "|---|---|---|"] +
                       _filas_caps(TIT["TÍTULO I"]) + _filas_caps(TIT["TÍTULO III"]) + _filas_caps(TIT["TÍTULO VIII"]))

T = Tema("B1T01",
  "Cuatro preguntas: I. Cómo está hecha la Constitución: preámbulo, once títulos, 169 artículos y disposiciones · II. Qué dice: el Título preliminar (arts. 1 a 9) y qué regula cada título · III. Cómo se reforma: Título X (arts. 166 a 169), Reglamentos de las Cámaras y LO 2/1980 · IV. Cuándo se ha reformado: art. 95 y las reformas de 1992, 2011, 2024 y 2026. Cada artículo: texto literal del BOE y ficha.",
  ["Estructura de la CE", "Preámbulo", "Título preliminar", "Valores superiores", "Art. 9.3", "Disposiciones adicionales", "Disposiciones transitorias", "Reforma constitucional", "Art. 167", "Art. 168", "Art. 169", "Referéndum", "Art. 95", "Reformas de la CE"])

# =============================================================================
T.ap("s0", "Mapa del tema: cuatro preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque I, tema 1):
> La Constitución Española de 1978: estructura y contenido. La reforma de la Constitución.

### El hilo conductor

El epígrafe se lee como **cuatro preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Constitución | Otras normas |
|---|---|---|---|
| **I** | ¿Cómo está hecha? (estructura) | Fórmula de promulgación, Preámbulo, Títulos preliminar y I a X, disposiciones adicionales, transitorias, derogatoria y final | — |
| **II** | ¿Qué dice? (contenido) | Título preliminar, arts. 1 a 9; rúbricas de los Títulos I a X | — |
| **III** | ¿Cómo se reforma? | Título X, arts. 166 a 169; arts. 75.3, 87.1 y 2 y 116 | Reglamento del Congreso, arts. 146 y 147; Reglamento del Senado, arts. 152, 154 y 156 a 159; LO 2/1980, arts. 2, 4 y 7 |
| **IV** | ¿Cuándo se ha reformado? | Art. 95; arts. 13.2, 135, 49 y 69.3 (reformados) | Reformas de la Constitución de 1992, 2011, 2024 y 2026 |

!> **La idea que une los cuatro bloques:** la Constitución tiene una **estructura** fija (I) que hay que saber de memoria: once títulos, 169 artículos y quince disposiciones. Su **contenido** empieza por el Título preliminar, que fija la forma del Estado y sus principios (II); los demás títulos se estudian en sus temas. Para cambiarla hay dos **procedimientos de reforma** (III): el del art. 167 y el del art. 168, más exigente, para la revisión total o la de las partes protegidas. Y se ha **reformado** cuatro veces, siempre por artículos sueltos (IV).

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Los cuadros de estructura copian **literalmente** las rúbricas del BOE; los números de artículo y de disposiciones se han **contado sobre el texto consolidado** del BOE.
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Cómo está hecha la Constitución? Estructura", donde(
  "Primera pregunta del tema. Antes de entrar en lo que dice la Constitución hay que saber **cómo está ordenada**: qué la encabeza, en cuántos títulos se divide y qué disposiciones la cierran. Es lo que se pregunta como «estructura».",
  ["1 Fórmula de promulgación y Preámbulo", "2 El articulado: once títulos y 169 artículos", "3 La parte final: 4 adicionales, 9 transitorias, 1 derogatoria y 1 final", "4 Cuadro de la estructura"]))

T.ap("s1", "I.1 Fórmula de promulgación y Preámbulo", f"""
La Constitución se abre con dos textos sin número de artículo: la **fórmula de promulgación** del Rey y el **Preámbulo**.

{unidad("1.1 La fórmula de promulgación",
  lit("CE", "preambulo", ["LAS CORTES HAN APROBADO Y EL PUEBLO ESPAÑOL RATIFICADO"], solo=[0, 1], titulo="Fórmula de promulgación (encabezamiento de la Constitución)"),
  fichab("Encabezamiento con el que el Rey da a conocer la Constitución",
         ["El Rey: «DON JUAN CARLOS I, REY DE ESPAÑA»", "Las Cortes: han aprobado", "El pueblo español: ha ratificado"],
         f"Dirigida {c('CE', 'preambulo', 'A TODOS LOS QUE LA PRESENTE VIEREN Y ENTENDIEREN')}",
         "—",
         "Aprobación de las **Cortes** + ratificación del **pueblo español**. Lo mismo repite el Preámbulo (→ I.1.2)."))}

{unidad("1.2 El Preámbulo",
  lit("CE", "preambulo", ["La Nación española", "en uso de su soberanía", "las Cortes aprueban y el pueblo español ratifica"], solo=list(range(3, 12)), titulo="Preámbulo"),
  fichab("Declaración de la voluntad de la Nación española que precede al articulado",
         f"{c('CE', 'preambulo', 'La Nación española')}, {c('CE', 'preambulo', 'en uso de su soberanía')}",
         ["::Seis objetivos («proclama su voluntad de»):", "**Garantizar** la convivencia democrática", "**Consolidar** un Estado de Derecho (imperio de la ley como expresión de la voluntad popular)", "**Proteger** a todos los españoles y pueblos de España en el ejercicio de los derechos humanos, sus culturas y tradiciones, lenguas e instituciones", "**Promover** el progreso de la cultura y de la economía", "**Establecer** una sociedad democrática avanzada", "**Colaborar** en unas relaciones pacíficas y de eficaz cooperación entre todos los pueblos de la Tierra"],
         "—",
         f"Quien proclama es la **Nación española**. Cierre literal: {c('CE', 'preambulo', 'las Cortes aprueban y el pueblo español ratifica')}: ni el Gobierno ni el Rey aprueban, y no lo hacen «conjuntamente». Cayó en 2025 (X 3, → Cierre 1)."))}
""", 2)

T.ap("s2", "I.2 El articulado: once títulos y 169 artículos", f"""
{unidad("2.1 Los títulos (rúbricas literales)",
  "*Cuadro de elaboración propia: las rúbricas están copiadas literalmente del BOE; los artículos de cada título se han contado sobre el texto consolidado. No es texto legal. Dónde se estudia cada título: → II.5.*",
  TABLA_ESTRUCTURA,
  fichab("División del articulado de la Constitución",
         "—",
         [f"::Un **Título preliminar** (sin rúbrica) y **diez títulos** numerados (I a X): {len(TODOS)} artículos correlativos", "Título I: el más largo (arts. 10 a 55)", "Título X: el último (arts. 166 a 169), la reforma"],
         "—",
         "Rúbricas que más se confunden: **VII** «Economía y Hacienda», **VIII** «De la Organización Territorial del Estado», **IX** «Del Tribunal Constitucional», **X** «De la reforma constitucional». El Título VIII cayó en 2025 (X 1, → Cierre 1)."))}

{unidad("2.2 Capítulos y secciones",
  "*Cuadro de elaboración propia: rúbricas literales del BOE; artículos contados sobre el texto consolidado. Solo los Títulos I, III y VIII se dividen en capítulos.*",
  TABLA_CAPS,
  fichab("Subdivisión interna de los títulos",
         "—",
         ["Título I: **cinco** capítulos; el segundo, con **dos secciones**", "Título III: **tres** capítulos", "Título VIII: **tres** capítulos", "Los demás títulos no tienen capítulos"],
         "—",
         f"El **art. 10** va antes del Capítulo primero y el **art. 14**, antes de la Sección 1.ª. La rúbrica del Título I es {c('CE', 'ti', 'De los derechos y deberes fundamentales')}; la de la Sección 2.ª, {c('CE', 's2', 'De los derechos y deberes de los ciudadanos')} (L 1, → Cierre 1)."))}
""", 2)

_DT = [("primera-2", "En los territorios dotados de un régimen provisional de autonomía"),
       ("segunda-2", "Los territorios que en el pasado hubiesen plebiscitado afirmativamente proyectos de Estatuto de autonomía"),
       ("tercera-2", "La iniciativa del proceso autonómico por parte de las Corporaciones locales"),
       ("cuarta-2", "En el caso de Navarra"),
       ("quinta", "Las ciudades de Ceuta y Melilla podrán constituirse en Comunidades Autónomas"),
       ("sexta", "Cuando se remitieran a la Comisión Constitucional del Congreso varios proyectos de Estatuto"),
       ("septima", "Los organismos provisionales autonómicos se considerarán disueltos"),
       ("octava", "Las Cámaras que han aprobado la presente Constitución"),
       ("novena", "A los tres años de la elección por vez primera de los miembros del Tribunal Constitucional")]
assert [b for b, _ in _DT] == DISP["transitoria"]
_ORD = ["Primera", "Segunda", "Tercera", "Cuarta", "Quinta", "Sexta", "Séptima", "Octava", "Novena"]
TABLA_DT = "\n".join(["| Disposición transitoria | Comienza (literal) |", "|---|---|"] + [f"| {_ORD[i]} | {c('CE', b, f)}… |" for i, (b, f) in enumerate(_DT)])

T.ap("s3", "I.3 La parte final: disposiciones adicionales, transitorias, derogatoria y final", f"""
Tras el art. 169 vienen **{len(DISP['adicional'])} disposiciones adicionales**, **{len(DISP['transitoria'])} transitorias**, **{len(DISP['derogatoria'])} derogatoria** y **{len(DISP['final'])} final** (contadas sobre el texto del BOE). Cayó en 2025 (X 2, → Cierre 1).

{unidad("3.1 Las cuatro disposiciones adicionales",
  lit("CE", "primera", ["derechos históricos de los territorios forales"]),
  lit("CE", "segunda", ["no perjudica las situaciones amparadas por los derechos forales"]),
  lit("CE", "tercera", ["informe previo de la Comunidad Autónoma"]),
  lit("CE", "cuarta", ["más de una Audiencia Territorial"]),
  fichab("Reglas especiales que acompañan al articulado",
         ["Territorios forales (1.ª y 2.ª)", "Archipiélago canario (3.ª)", "Comunidades Autónomas con más de una Audiencia Territorial (4.ª)"],
         ["1.ª Amparo y respeto de los derechos históricos de los territorios forales; actualización en el marco de la Constitución y de los Estatutos", "2.ª La mayoría de edad del art. 12 no perjudica los derechos forales de Derecho privado", "3.ª Régimen económico y fiscal canario: informe previo de la Comunidad Autónoma", "4.ª Mantenimiento de varias Audiencias Territoriales"],
         "—",
         "Son **cuatro**. Los **derechos históricos de los territorios forales** están en la **adicional primera** (no en una transitoria)."))}

{unidad("3.2 Las nueve disposiciones transitorias",
  "*Cuadro de elaboración propia: las primeras palabras de cada disposición, literales del BOE.*",
  TABLA_DT,
  fichab("Reglas para el paso al nuevo régimen constitucional",
         "—",
         ["1.ª a 7.ª: el **proceso autonómico** (regímenes provisionales de autonomía, Navarra, Ceuta y Melilla, organismos provisionales)", "8.ª: las **Cámaras** que aprobaron la Constitución", "9.ª: la primera **renovación del Tribunal Constitucional**"],
         f"8.ª: el mandato de las primeras Cámaras no se extiende {c('CE', 'octava', 'más allá del 15 de junio de 1981')}",
         f"Son **nueve**. **Ceuta y Melilla** están en la **quinta**: {c('CE', 'quinta', 'mediante una ley orgánica')}."))}

{unidad("3.3 La disposición derogatoria",
  lit("CE", "dd", ["Queda derogada la Ley 1/1977, de 4 de enero, para la Reforma Política", "En tanto en cuanto pudiera conservar alguna vigencia"]),
  fichab("Derogación expresa de las leyes fundamentales anteriores",
         "—",
         [f"::Apartado 1: {c('CE', 'dd', 'Queda derogada la Ley 1/1977, de 4 de enero, para la Reforma Política')} y, en tanto no lo estuvieran ya:", "Ley de Principios del Movimiento Nacional (1958)", "Fuero de los Españoles (1945)", "Fuero del Trabajo (1938)", "Ley Constitutiva de las Cortes (1942)", "Ley de Sucesión en la Jefatura del Estado (1947)", "Ley Orgánica del Estado (1967) y Ley de Referéndum Nacional (1945)", "Apartado 2: Ley de 25 de octubre de 1839 (Álava, Guipúzcoa y Vizcaya)"],
         "—",
         "Hay **una sola** disposición derogatoria, con **tres** apartados. La primera ley que cita es la **Ley para la Reforma Política** (1977)."))}

{unidad("3.4 La disposición final y la fórmula de cierre",
  lit("CE", "df", ["entrará en vigor el mismo día de la publicación de su texto oficial"]),
  lit("CE", "firma", ["COMO NORMA FUNDAMENTAL DEL ESTADO", "A VEINTISIETE DE DICIEMBRE DE MIL NOVECIENTOS SETENTA Y OCHO"], solo=[0, 1, 2], titulo="Fórmula final y fecha (Constitución)"),
  fichab("Entrada en vigor de la Constitución",
         "—",
         f"{c('CE', 'df', 'Se publicará también en las demás lenguas de España')}",
         f"Entrada en vigor: {c('CE', 'df', 'el mismo día de la publicación de su texto oficial en el boletín oficial del Estado')} (sin *vacatio legis*)",
         "Una **sola** disposición final. Fecha de la Constitución: **27 de diciembre de 1978**; su publicación en el BOE es de 29 de diciembre de 1978 (metadatos del BOE, → cronología)."))}
""", 2)

T.ap("s4", "I.4 Cuadro de la estructura (esquema)", f"""
*Esquema de elaboración propia: resume la estructura contada sobre el texto del BOE; no es texto legal.*

| Parte | Qué contiene | Cuántos |
|---|---|---|
| Fórmula de promulgación | El Rey: las Cortes han aprobado y el pueblo español ratificado | — |
| Preámbulo | La Nación española proclama su voluntad (seis objetivos) | — |
| Título preliminar | Arts. 1 a 9 | 9 artículos |
| Títulos I a X | Arts. 10 a 169 | 160 artículos |
| Disposiciones adicionales | Territorios forales, Canarias, Audiencias Territoriales | **{len(DISP['adicional'])}** |
| Disposiciones transitorias | Proceso autonómico, primeras Cámaras, primera renovación del TC | **{len(DISP['transitoria'])}** |
| Disposición derogatoria | Ley para la Reforma Política y leyes fundamentales anteriores | **{len(DISP['derogatoria'])}** |
| Disposición final | Entrada en vigor el día de su publicación en el BOE | **{len(DISP['final'])}** |

{resumen([
  "Encabezan la Constitución la **fórmula de promulgación** y el **Preámbulo**: las Cortes **aprueban** y el pueblo español **ratifica**.",
  "**Once títulos** (preliminar y I a X) y **169 artículos**; capítulos solo en los Títulos **I** (5), **III** (3) y **VIII** (3).",
  "Parte final: **4** adicionales, **9** transitorias, **1** derogatoria y **1** final; entra en vigor el **mismo día** de su publicación."],
  "Siguiente: II. ¿Qué dice? El contenido")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Qué dice? El contenido: Título preliminar y materia de cada título", donde(
  "Segunda pregunta. El **Título preliminar** (arts. 1 a 9) es el único que se estudia entero en este tema: define el Estado y sus principios. Los demás títulos tienen tema propio; aquí basta saber **qué regula cada uno**.",
  ["1 El Estado: forma, soberanía y unidad (arts. 1 y 2)", "2 Lenguas, bandera y capital (arts. 3 a 5)", "3 Partidos, sindicatos y Fuerzas Armadas (arts. 6 a 8)", "4 Sujeción a la Constitución y garantías (art. 9)", "5 Qué regula cada título y dónde se estudia"]))

T.ap("s5", "II.1 El Estado: forma, soberanía y unidad (arts. 1 y 2)", f"""
{unidad("1.1 Estado social y democrático de Derecho; soberanía; Monarquía parlamentaria (art. 1)",
  lit("CE", "Artículo 1", ["Estado social y democrático de Derecho", "la libertad, la justicia, la igualdad y el pluralismo político", "La soberanía nacional reside en el pueblo español", "Monarquía parlamentaria"]),
  fichab("Definición del Estado, de su soberanía y de su forma política",
         f"{c('CE', 'Artículo 1', 'La soberanía nacional reside en el pueblo español, del que emanan los poderes del Estado')}",
         ["::Tres apartados:", "1. Estado **social y democrático de Derecho**; **cuatro** valores superiores: libertad, justicia, igualdad y pluralismo político", "2. Soberanía nacional: en el **pueblo español**", "3. Forma política: **Monarquía parlamentaria**"],
         "—",
         "Valores **superiores** son **cuatro** (libertad, justicia, igualdad, pluralismo político): la seguridad jurídica o la dignidad no están en esa lista. La forma política es la **Monarquía parlamentaria** (la Corona, tema I.4)."))}

{unidad("1.2 Unidad de la Nación y derecho a la autonomía (art. 2)",
  lit("CE", "Artículo 2", ["indisoluble unidad de la Nación española", "derecho a la autonomía de las nacionalidades y regiones", "la solidaridad entre todas ellas"]),
  fichab("Fundamento de la Constitución y principios de la organización territorial",
         "La Nación española; las **nacionalidades y regiones** que la integran",
         ["Unidad: la Constitución se fundamenta en la indisoluble unidad de la Nación española", "Autonomía: la reconoce y garantiza a las nacionalidades y regiones", "Solidaridad entre todas ellas"],
         "—",
         "Tres principios: **unidad**, **autonomía** y **solidaridad**. La autonomía es de las «**nacionalidades y regiones**» (no de las «Comunidades Autónomas», que es la expresión del Título VIII; temas I.10 y I.11)."))}
""", 2)

T.ap("s6", "II.2 Lenguas, bandera y capital (arts. 3 a 5)", f"""
{unidad("2.1 Las lenguas (art. 3)",
  lit("CE", "Artículo 3", ["El castellano es la lengua española oficial del Estado", "el deber de conocerla y el derecho a usarla", "de acuerdo con sus Estatutos", "patrimonio cultural"]),
  ficha(["Castellano: todos los españoles", "Demás lenguas españolas: oficiales en las respectivas Comunidades Autónomas"],
        ["Castellano: lengua española **oficial del Estado**; **deber de conocerla** y **derecho a usarla**", "Las demás lenguas españolas: **también oficiales** en sus Comunidades Autónomas", "Modalidades lingüísticas: patrimonio cultural, objeto de especial respeto y protección"],
        f"La cooficialidad, {c('CE', 'Artículo 3', 'de acuerdo con sus Estatutos')}",
        "—",
        "Del castellano hay **deber de conocerla** y **derecho a usarla**. Las otras lenguas son oficiales **en sus Comunidades** y según sus **Estatutos**, no en todo el Estado."))}

{unidad("2.2 La bandera (art. 4)",
  lit("CE", "Artículo 4", ["tres franjas horizontales, roja, amarilla y roja", "siendo la amarilla de doble anchura que cada una de las rojas", "junto a la bandera de España"]),
  fichab("Bandera de España y banderas de las Comunidades Autónomas",
         "Los **Estatutos** pueden reconocer banderas y enseñas propias de las Comunidades Autónomas",
         f"Las autonómicas se usan {c('CE', 'Artículo 4', 'junto a la bandera de España en sus edificios públicos y en sus actos oficiales')}",
         "—",
         "Franja **amarilla** de **doble anchura** que **cada una** de las rojas. Las enseñas autonómicas las reconocen los **Estatutos** («podrán»)."))}

{unidad("2.3 La capital (art. 5)",
  lit("CE", "Artículo 5", ["la villa de Madrid"]),
  fichab("Capital del Estado", "—", c("CE", "Artículo 5", "La capital del Estado es la villa de Madrid"), "—",
         "La Constitución dice «**villa** de Madrid»."))}
""", 2)

T.ap("s7", "II.3 Partidos políticos, sindicatos y Fuerzas Armadas (arts. 6 a 8)", f"""
{unidad("3.1 Los partidos políticos (art. 6)",
  lit("CE", "Artículo 6", ["expresan el pluralismo político", "instrumento fundamental para la participación política", "Su estructura interna y funcionamiento deberán ser democráticos"]),
  fichab("Función constitucional de los partidos",
         "Los partidos políticos",
         ["Expresan el **pluralismo político**", "Concurren a la formación y manifestación de la **voluntad popular**", "Son **instrumento fundamental** para la participación política"],
         f"Creación y actividad: {c('CE', 'Artículo 6', 'libres dentro del respeto a la Constitución y a la ley')}; estructura interna y funcionamiento: **democráticos**",
         "Tres funciones literales. El pluralismo político es, además, un **valor superior** (art. 1.1 → II.1.1)."))}

{unidad("3.2 Sindicatos y asociaciones empresariales (art. 7)",
  lit("CE", "Artículo 7", ["Los sindicatos de trabajadores y las asociaciones empresariales", "intereses económicos y sociales que les son propios"]),
  fichab("Función constitucional de los sindicatos y de las asociaciones empresariales",
         c("CE", "Artículo 7", "Los sindicatos de trabajadores y las asociaciones empresariales"),
         f"{c('CE', 'Artículo 7', 'contribuyen a la defensa y promoción de los intereses económicos y sociales que les son propios')}",
         "Creación y actividad libres dentro del respeto a la Constitución y a la ley; estructura y funcionamiento **democráticos**",
         "El art. 7 menciona también a las **asociaciones empresariales**, no solo a los sindicatos. La exigencia de estructura **democrática** es común a los arts. 6 y 7."))}

{unidad("3.3 Las Fuerzas Armadas (art. 8)",
  lit("CE", "Artículo 8", ["el Ejército de Tierra, la Armada y el Ejército del Aire", "garantizar la soberanía e independencia de España, defender su integridad territorial y el ordenamiento constitucional", "Una ley orgánica"]),
  fichab("Composición y misión de las Fuerzas Armadas",
         c("CE", "Artículo 8", "el Ejército de Tierra, la Armada y el Ejército del Aire"),
         ["::Misión:", "Garantizar la soberanía e independencia de España", "Defender su integridad territorial", "Defender el ordenamiento constitucional"],
         "Las bases de la organización militar: por **ley orgánica** (8.2)",
         "Las Fuerzas Armadas están en el **Título preliminar** (art. 8), no en el Título IV. Su organización militar: **ley orgánica**."))}
""", 2)

T.ap("s8", "II.4 Sujeción a la Constitución y garantías (art. 9)", f"""
{unidad("4.1 Sujeción a la Constitución e igualdad real (art. 9.1 y 2)",
  lit("CE", "Artículo 9", ["Los ciudadanos y los poderes públicos están sujetos a la Constitución", "sean reales y efectivas"], solo=[1, 2]),
  fichab("Fuerza vinculante de la Constitución y mandato a los poderes públicos",
         ["Sujetos a la Constitución: **los ciudadanos y los poderes públicos** (9.1)", "Mandato del 9.2: **los poderes públicos**"],
         ["Promover las condiciones para que la libertad y la igualdad sean **reales y efectivas**", "Remover los obstáculos que impidan o dificulten su plenitud", "Facilitar la participación de todos los ciudadanos en la vida política, económica, cultural y social"],
         "—",
         "La sujeción alcanza a **ciudadanos y poderes públicos**, y no solo a la Constitución: también " + c("CE", "Artículo 9", "al resto del ordenamiento jurídico") + "."))}

{unidad("4.2 Los principios que garantiza la Constitución (art. 9.3)",
  lit("CE", "Artículo 9", ["no favorables o restrictivas de derechos individuales", "la interdicción de la arbitrariedad de los poderes públicos"], solo=[3]),
  fichab("Principios del Estado de Derecho que la Constitución garantiza",
         "—",
         ["::Literalmente, la Constitución garantiza:", "El principio de legalidad", "La jerarquía normativa", "La publicidad de las normas", "La irretroactividad de las disposiciones sancionadoras no favorables o restrictivas de derechos individuales", "La seguridad jurídica", "La responsabilidad", "La interdicción de la arbitrariedad de los poderes públicos"],
         "—",
         "Lo irretroactivo son las disposiciones sancionadoras **no favorables o restrictivas**: el art. 9.3 no prevé ninguna salvedad por «interés general». Cayó en 2025 (P 51, → Cierre 1)."))}
""", 2)

T.ap("s9", "II.5 Qué regula cada título y dónde se estudia (esquema)", f"""
*Cuadro de elaboración propia: rúbricas literales del BOE; la columna «Se estudia en» remite al programa. No es texto legal.*

{TABLA_TITULOS}

!> En el examen, la **rúbrica** del título suele bastar para situar un artículo: el Título IV es «Del Gobierno y de la Administración» (incluye la Administración Pública, art. 103) y el Título V regula las **relaciones** entre el Gobierno y las Cortes Generales.

{resumen([
  "Art. 1: Estado **social y democrático de Derecho**; **cuatro valores superiores**; soberanía en el **pueblo español**; **Monarquía parlamentaria**.",
  "Art. 2: **unidad**, **autonomía** de nacionalidades y regiones y **solidaridad**. Arts. 3 a 5: lenguas, bandera, **villa de Madrid**.",
  "Arts. 6 a 8: partidos, sindicatos y asociaciones empresariales (estructura **democrática**); Fuerzas Armadas (**ley orgánica**).",
  "Art. 9: sujeción de **ciudadanos y poderes públicos**; igualdad **real y efectiva**; siete garantías del 9.3."],
  "Siguiente: III. ¿Cómo se reforma? Título X")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Cómo se reforma? Título X (arts. 166 a 169)", donde(
  "Tercera pregunta. La Constitución prevé **dos procedimientos** de reforma: el del **art. 167** y el del **art. 168**, mucho más exigente, para la revisión total o la que afecte a sus partes protegidas. Los Reglamentos de las Cámaras y la LO 2/1980 completan el procedimiento.",
  ["1 La iniciativa (arts. 87 y 166)", "2 El procedimiento del art. 167", "3 El procedimiento del art. 168", "4 Límites y reglas comunes (arts. 75.3, 116.1 y 169; LO 2/1980, art. 4)", "5 Cuadro comparativo"]))

T.ap("s10", "III.1 La iniciativa de reforma (arts. 87.1 y 2 y 166)", f"""
{unidad("1.1 Los titulares (art. 87.1 y 2)",
  lit("CE", "Artículo 87", ["al Gobierno, al Congreso y al Senado", "Las Asambleas de las Comunidades Autónomas", "un máximo de tres miembros"], solo=[1, 2]),
  fichab("Iniciativa a la que remite el art. 166 (→ III.1.2)",
         ["El **Gobierno**", "El **Congreso** y el **Senado**", "Las **Asambleas de las Comunidades Autónomas**"],
         [f"Asambleas autonómicas: {c('CE', 'Artículo 87', 'solicitar del Gobierno la adopción de un proyecto de ley')} o {c('CE', 'Artículo 87', 'remitir a la Mesa del Congreso una proposición de ley')}"],
         "Las Asambleas delegan ante el Congreso **un máximo de tres** miembros",
         "Las Asambleas autonómicas **no** presentan la iniciativa ante el Senado: la remiten a la **Mesa del Congreso** o la piden al **Gobierno**."))}

{unidad("1.2 Remisión al art. 87 (art. 166)",
  lit("CE", "Artículo 166", ["apartados 1 y 2 del artículo 87"]),
  fichab("Quién puede proponer una reforma constitucional",
         "Los titulares de los apartados 1 y 2 del art. 87 (→ III.1.1)",
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

T.ap("s11", "III.2 El procedimiento del art. 167", f"""
{unidad("2.1 Mayorías, Comisión paritaria y referéndum facultativo (art. 167)",
  lit("CE", "Artículo 167", ["mayoría de tres quintos de cada una de las Cámaras", "Comisión de composición paritaria de Diputados y Senadores", "mayoría absoluta del Senado", "por mayoría de dos tercios", "dentro de los quince días siguientes a su aprobación, una décima parte de los miembros de cualquiera de las Cámaras"]),
  fichab("Procedimiento para cualquier reforma que no sea del art. 168",
         ["Las **Cortes Generales** (Congreso y Senado)", "Comisión **paritaria** de Diputados y Senadores, si no hay acuerdo", "**Una décima parte** de los miembros de cualquiera de las Cámaras: piden el referéndum"],
         ["Aprobación por **tres quintos** de **cada** Cámara", "Sin acuerdo: Comisión paritaria → texto votado por Congreso y Senado", "Si aun así no se aprueba: basta la **mayoría absoluta del Senado** y **dos tercios del Congreso**", "Referéndum de ratificación **solo si se solicita**"],
         ["3/5 de cada Cámara", "Alternativa: mayoría absoluta del Senado + 2/3 del Congreso", "Referéndum: lo piden **1/10** de los miembros de cualquier Cámara en **15 días** desde la aprobación"],
         "Dos tercios del **Congreso** (no del Senado) en la vía del 167.2. El referéndum del 167 es **facultativo**; el del 168, **obligatorio** (→ III.3.1)."))}

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

T.ap("s12", "III.3 El procedimiento del art. 168", f"""
{unidad("3.1 Revisión total o de las partes protegidas (art. 168)",
  lit("CE", "Artículo 168", ["revisión total", "al Título preliminar, al Capítulo segundo, Sección primera del Título I, o al Título II", "mayoría de dos tercios de cada Cámara", "disolución inmediata de las Cortes", "deberá ser aprobado por mayoría de dos tercios de ambas Cámaras", "será sometida a referéndum para su ratificación"]),
  fichab("Procedimiento reforzado de reforma",
         ["Las Cortes que aprueban el principio (y quedan disueltas)", "Las **Cámaras elegidas** después", "El **pueblo**, en referéndum obligatorio"],
         ["::Se aplica a:", "La **revisión total**", "Una revisión parcial que afecte al **Título preliminar** (arts. 1 a 9)", "… al **Capítulo segundo, Sección primera, del Título I** (arts. 15 a 29)", "… al **Título II** (la Corona, arts. 56 a 65)"],
         ["1. Principio: **2/3 de cada Cámara** + **disolución inmediata**", "2. Nuevas Cámaras: ratifican y aprueban el nuevo texto por **2/3 de ambas**", "3. **Referéndum** de ratificación, siempre"],
         "No están protegidos el **art. 14** ni la **Sección 2.ª**: la Sección 1.ª empieza en el art. 15 (→ I.2.2). Tampoco la reforma del Título X. El referéndum es **obligatorio** («será sometida»)."))}

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

T.ap("s13", "III.4 Límites y reglas comunes (arts. 75.3, 116.1 y 169; LO 2/1980, art. 4)", f"""
{unidad("4.1 Sin delegación en Comisiones (art. 75.3)",
  lit("CE", "Artículo 75", ["la reforma constitucional"], solo=[2, 3]),
  fichab("La reforma constitucional la aprueba el Pleno",
         "El **Pleno** de cada Cámara",
         "No cabe delegar su aprobación en las Comisiones Legislativas Permanentes",
         "—",
         "La **reforma constitucional** encabeza la lista del 75.3, con las cuestiones internacionales, las leyes orgánicas y de bases y los Presupuestos."))}

{unidad("4.2 Límite temporal: guerra y estados del art. 116 (arts. 116.1 y 169)",
  lit("CE", "Artículo 116", ["los estados de alarma, de excepción y de sitio"], solo=[1]),
  lit("CE", "Artículo 169", ["en tiempo de guerra o de vigencia de alguno de los estados previstos en el artículo 116"]),
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

T.ap("s14", "III.5 Cuadro comparativo: art. 167 y art. 168 (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| | Art. 167 | Art. 168 |
|---|---|---|
| Cuándo | Cualquier reforma no incluida en el 168 | Revisión **total**, o parcial del **Título preliminar**, **Cap. 2.º Sección 1.ª del Título I** o **Título II** |
| Iniciativa | Art. 166 → art. 87.1 y 2 | Igual |
| Aprobación | **3/5 de cada Cámara**; o mayoría absoluta del Senado + **2/3 del Congreso** | Principio: **2/3 de cada Cámara** y **disolución**; nuevas Cámaras: ratifican y aprueban por **2/3 de ambas** |
| Desacuerdo | Comisión paritaria de Diputados y Senadores | — |
| Referéndum | **Facultativo**: 1/10 de los miembros de cualquier Cámara, en 15 días | **Obligatorio** |
| Límite (art. 169) | No en guerra ni en alarma, excepción o sitio | Igual |

{resumen([
  "Iniciativa: la del **art. 87.1 y 2** (Gobierno, Congreso, Senado y Asambleas autonómicas); **no** la popular.",
  "Art. 167: **3/5 de cada Cámara**; Comisión **paritaria**; o mayoría absoluta del Senado + **2/3 del Congreso**; referéndum **si lo pide 1/10** de una Cámara en **15 días**.",
  "Art. 168: revisión total o del **Título preliminar**, **Sección 1.ª del Cap. 2.º del Título I** o **Título II**: **2/3**, **disolución**, **2/3** de las nuevas Cámaras y **referéndum obligatorio**.",
  "No se puede **iniciar** en guerra ni en los estados del **art. 116**; no se delega en Comisiones (75.3)."],
  "Siguiente: IV. ¿Cuándo se ha reformado la Constitución?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Cuándo se ha reformado? Art. 95 y las cuatro reformas", donde(
  "Cuarta pregunta. La Constitución exige reformarla **antes** de celebrar un tratado contrario a ella (art. 95). Se ha modificado **cuatro veces**, siempre un solo artículo o apartado.",
  ["1 Tratados contrarios a la Constitución (art. 95)", "2 Las reformas de 1992, 2011, 2024 y 2026", "3 Cuadro de las reformas"]))

T.ap("s15", "IV.1 Tratados contrarios a la Constitución (art. 95)", f"""
{unidad("1.1 Previa revisión constitucional (art. 95)",
  lit("CE", "Artículo 95", ["exigirá la previa revisión constitucional", "El Gobierno o cualquiera de las Cámaras"]),
  fichab("Prioridad de la Constitución sobre los tratados",
         "Pueden requerir al TC: **el Gobierno o cualquiera de las Cámaras**",
         "Si un tratado contiene estipulaciones contrarias a la Constitución, primero se **revisa la Constitución** y después se celebra el tratado",
         "—",
         "La revisión es **previa**. Fue el origen de la reforma de 1992 (→ IV.2.1)."))}
""", 2)

T.ap("s16", "IV.2 Las reformas de 1992, 2011, 2024 y 2026", f"""
> [[BOE|{CE_URL}]]
> **Dato del análisis del texto consolidado de la Constitución en el BOE (no es texto legal):** la Constitución se ha modificado por cuatro reformas: art. 13.2 (Reforma de 27 de agosto de 1992), art. 135 (Reforma de 27 de septiembre de 2011), art. 49 (Reforma de 15 de febrero de 2024) y art. 69.3 (Reforma de 19 de mayo de 2026).

Las cuatro empiezan con la misma fórmula ({c('REF2024', 'preambulo', 'Sabed: Que las Cortes Generales han aprobado y Yo vengo en sancionar la siguiente Reforma de la Constitución')}), tienen un **artículo único** y una **disposición final única**: entran en vigor el mismo día de su publicación en el BOE.

{unidad("2.1 Reforma de 1992: art. 13.2 (sufragio pasivo en las elecciones municipales)",
  lit("REF1992", "preambulo", ["y pasivo"], solo=[3, 12, 13, 14, 15, 16], titulo="Reforma del artículo 13, apartado 2, de la Constitución Española, de 27 de agosto de 1992"),
  fichab("Primera reforma: añade el sufragio **pasivo** en las elecciones municipales",
         "Las **Cortes Generales** aprueban; el **Rey** sanciona",
         f"Su exposición de motivos invoca {c('REF1992', 'preambulo', 'el fondo de poder constituyente que les confiere el artículo 167 de la Constitución')}",
         "Entrada en vigor: el día de su publicación (BOE de 28-8-1992)",
         "Origen: el **Tratado de la Unión Europea** y el requerimiento del Gobierno al TC por la vía del **art. 95.2** (lo cuenta su exposición de motivos). Artículo reformado: **13.2** (Título I)."))}

{unidad("2.2 Reforma de 2011: art. 135 (estabilidad presupuestaria)",
  lit("REF2011", "preambulo", ["principio de estabilidad presupuestaria", "antes del 30 de junio de 2012", "a partir de 2020"], solo=[3] + list(range(10, 30)), titulo="Reforma del artículo 135 de la Constitución Española, de 27 de septiembre de 2011"),
  fichab("Segunda reforma: nueva redacción del art. 135 (Título VII)",
         "Las **Cortes Generales** aprueban; el **Rey** sanciona",
         "Artículo único (nuevo art. 135, cuyo texto vigente se estudia en el tema VI.1) y **disposición adicional única**",
         ["Ley orgánica del art. 135: aprobada **antes del 30 de junio de 2012**", "Límites de déficit estructural: en vigor **a partir de 2020**", "Entrada en vigor de la reforma: el día de su publicación (BOE de 27-9-2011)"],
         "Es la única de las cuatro con **disposición adicional**. El art. 135 está en el **Título VII**, que no es parte protegida del art. 168."))}

{unidad("2.3 Reforma de 2024: art. 49 (personas con discapacidad)",
  lit("REF2024", "preambulo", ["Las personas con discapacidad ejercen los derechos previstos en este Título"], solo=[3, 12, 13, 14, 15, 16, 17, 18], titulo="Reforma del artículo 49 de la Constitución Española, de 15 de febrero de 2024"),
  fichab("Tercera reforma: nueva redacción del art. 49 (Capítulo tercero del Título I)",
         "Las **Cortes Generales** aprueban; el **Rey** sanciona",
         "Artículo único: nuevo art. 49, en dos apartados",
         "Entrada en vigor: el día de su publicación (BOE de 17-2-2024)",
         "El art. 49 está en el **Capítulo tercero** del Título I, fuera de la Sección 1.ª del Capítulo segundo protegida por el art. 168."))}

{unidad("2.4 Reforma de 2026: art. 69.3 (un Senador para Formentera)",
  lit("REF2026", "preambulo", ["Ibiza, Formentera", "quedará pospuesta hasta la convocatoria de las primeras elecciones al Senado"], solo=[3, 17, 18, 19, 20, 21, 22, 23], titulo="Reforma del apartado 3 del artículo 69 de la Constitución Española, de 19 de mayo de 2026"),
  fichab("Cuarta reforma: Ibiza y Formentera, circunscripciones separadas para el Senado",
         "Las **Cortes Generales** aprueban; el **Rey** sanciona",
         "Artículo único (nuevo art. 69.3) y **disposición transitoria única**",
         ["Eficacia de las nuevas circunscripciones: desde las **primeras elecciones al Senado** convocadas tras su entrada en vigor", "Entrada en vigor de la reforma: el día de su publicación (BOE de 20-5-2026)"],
         f"Antes de la reforma, según su preámbulo, {c('REF2026', 'preambulo', 'la agrupación de islas Ibiza-Formentera elegiría un Senador')}. El art. 69 está en el **Título III**."))}
""", 2)

T.ap("s17", "IV.3 Cuadro de las reformas (esquema)", f"""
*Esquema de elaboración propia: resume los textos de las reformas publicados en el BOE; no es texto legal.*

| Reforma | Artículo | Título de la CE | Qué cambia | Disposiciones propias | BOE |
|---|---|---|---|---|---|
| 27-8-1992 | 13.2 | I, Cap. 1.º | Sufragio **activo y pasivo** de extranjeros en elecciones municipales | Final única | 28-8-1992 |
| 27-9-2011 | 135 | VII | **Estabilidad presupuestaria** | Adicional única y final única | 27-9-2011 |
| 15-2-2024 | 49 | I, Cap. 3.º | **Personas con discapacidad** | Final única | 17-2-2024 |
| 19-5-2026 | 69.3 | III | **Formentera**, circunscripción propia al Senado | Transitoria única y final única | 20-5-2026 |

!> Ninguna de las cuatro reformas afecta a las partes protegidas por el **art. 168** (Título preliminar, Sección 1.ª del Capítulo segundo del Título I y Título II).

{resumen([
  "Un tratado contrario a la Constitución exige **previa revisión constitucional** (art. 95.1); el TC lo declara a requerimiento del **Gobierno** o de **cualquiera de las Cámaras**.",
  "Cuatro reformas: **13.2** (1992), **135** (2011), **49** (2024) y **69.3** (2026); todas con **artículo único** y entrada en vigor el día de su publicación."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)
# Comprobación de lo que dice el cuadro de las reformas: artículos afectados fuera de las partes del art. 168
_prot = set(TIT["TÍTULO PRELIMINAR"]["arts"]) | set(TIT["TÍTULO I"]["caps"][1]["secs"][0]["arts"]) | set(TIT["TÍTULO II"]["arts"])
assert not ({13, 135, 49, 69} & _prot)
assert 13 in TIT["TÍTULO I"]["caps"][0]["arts"] and 49 in TIT["TÍTULO I"]["caps"][2]["arts"] and 135 in TIT["TÍTULO VII"]["arts"] and 69 in TIT["TÍTULO III"]["arts"]
assert rango(TIT["TÍTULO I"]["caps"][1]["secs"][0]["arts"]) == "15 a 29" and rango(TIT["TÍTULO II"]["arts"]) == "56 a 65"

# =============================================================================
EX_X1 = examen("X", 1, {
  "a": f"«Economía y Hacienda» es la rúbrica del **Título VII**: {c('CE', 'tvii', 'Economía y Hacienda')}.",
  "b": f"Rúbrica literal del Título VIII: {c('CE', 'tviii', 'De la Organización Territorial del Estado')}.",
  "c": f"«Del Poder Judicial» es el **Título VI**: {c('CE', 'tvi', 'Del Poder Judicial')}.",
  "d": f"«De la reforma constitucional» es el **Título X**: {c('CE', 'tx', 'De la reforma constitucional')}."},
  [("Organización Territorial del Estado", "CE", "tviii", "De la Organización Territorial del Estado")])
EX_X2 = examen("X", 2, {
  "a": f"Contadas sobre el texto del BOE: adicionales de la primera a la {c('CE', 'cuarta', 'Disposición adicional cuarta')}; transitorias de la primera a la {c('CE', 'novena', 'Disposición transitoria novena')}; una {c('CE', 'dd', 'Disposición derogatoria')} y una {c('CE', 'df', 'Disposición final')}.",
  "b": "Invierte los números: las adicionales son **4** (la última es la cuarta) y las transitorias **9** (la última es la novena).",
  "c": "Solo hay **una** disposición derogatoria y **una** final; las adicionales son **4** y las transitorias **9**.",
  "d": "Acierta las 4 adicionales y la derogatoria, pero las transitorias son **9** y la final es **una sola**."},
  [("4 disposiciones adicionales", "CE", "cuarta", "Disposición adicional cuarta"), ("9 disposiciones transitorias", "CE", "novena", "Disposición transitoria novena"),
   ("1 disposición derogatoria", "CE", "dd", "Disposición derogatoria"), ("1 disposición final", "CE", "df", "Disposición final")])
EX_X3 = examen("X", 3, {
  "a": f"El Gobierno no interviene: {c('CE', 'preambulo', 'las Cortes aprueban y el pueblo español ratifica')}. Al pueblo le corresponde ratificar, no al Gobierno sancionar.",
  "b": "No lo hacen «conjuntamente»: cada uno hace una cosa distinta (las Cortes **aprueban**, el pueblo **ratifica**).",
  "c": f"Literal del Preámbulo: {c('CE', 'preambulo', 'En consecuencia, las Cortes aprueban y el pueblo español ratifica la siguiente')} Constitución.",
  "d": f"El Gobierno no aparece en el Preámbulo; la fórmula de promulgación también dice {c('CE', 'preambulo', 'QUE LAS CORTES HAN APROBADO Y EL PUEBLO ESPAÑOL RATIFICADO')}."},
  [("Las Cortes aprueban y el pueblo español ratifica", "CE", "preambulo", "las Cortes aprueban y el pueblo español ratifica")])
EX_P51 = examen("P", 51, {
  "a": f"Es al revés: se garantiza {c('CE', 'Artículo 9', 'la irretroactividad de las disposiciones sancionadoras no favorables o restrictivas de derechos individuales')}; el art. 9.3 no prevé ninguna salvedad por interés general.",
  "b": f"Literal del art. 9.3: {c('CE', 'Artículo 9', 'la interdicción de la arbitrariedad de los poderes públicos')}.",
  "c": f"No está en el art. 9.3: es un principio de actuación de las Administraciones de la Ley 40/2015 ({c('L40', 'a3', 'Servicio efectivo a los ciudadanos')}, art. 3.1 a).",
  "d": f"El art. 9.3 garantiza {c('CE', 'Artículo 9', 'el principio de legalidad, la jerarquía normativa')}, no una reserva de ley orgánica; las materias de ley orgánica las fija el art. 81.1."},
  [("interdicción de la arbitrariedad de los poderes públicos", "CE", "Artículo 9", "la interdicción de la arbitrariedad de los poderes públicos")])
EX_L1 = examen("L", 1, {
  "a": f"Rúbrica literal del Título I: {c('CE', 'ti', 'De los derechos y deberes fundamentales')}.",
  "b": f"Es la rúbrica de la **Sección 2.ª** del Capítulo segundo: {c('CE', 's2', 'De los derechos y deberes de los ciudadanos')}.",
  "c": f"Es la rúbrica del **Capítulo primero**: {c('CE', 'cprimero', 'De los españoles y los extranjeros')}.",
  "d": f"Es la rúbrica del **Capítulo segundo**: {c('CE', 'csegundo', 'Derechos y libertades')}."},
  [("De los derechos y deberes fundamentales", "CE", "ti", "De los derechos y deberes fundamentales")])

T.ap("s18", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **tres** preguntas de este tema (las tres en el ejercicio extraordinario: Título VIII, número de disposiciones y Preámbulo) y **dos** relacionadas (rúbrica del Título I y art. 9.3). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-X 2025, pregunta 1 · Rúbrica del Título VIII (→ I.2.1)", EX_X1,
  "### GACE-X 2025, pregunta 2 · Disposiciones de la Constitución (→ I.3)", EX_X2,
  "### GACE-X 2025, pregunta 3 · El Preámbulo (→ I.1.2)", EX_X3,
  "### GACE-L 2025, pregunta 1 · Rúbrica del Título I (relacionada; → I.2.2)", EX_L1,
  "### GACE-P 2025, pregunta 51 · Art. 9.3 (relacionada; → II.4.2)", EX_P51,
  "### Cómo se pregunta",
  "!> La **estructura** se pregunta con distractores que **cambian el número** (4 adicionales / 9 transitorias) o **la rúbrica de otro título o capítulo**. El art. 9.3 y el Preámbulo, con una **palabra cambiada** («retroactividad», «conjuntamente»). Saber el texto literal resuelve la pregunta.",
]))

T.ap("s19", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Estructura | Fórmula de promulgación; Preámbulo; Título preliminar y I a X; 169 artículos; disposiciones | **4** adicionales, **9** transitorias, **1** derogatoria, **1** final; Título VIII = Organización Territorial |
| II. Contenido | Arts. 1 a 9: Estado, soberanía, Monarquía parlamentaria, unidad y autonomía, lenguas, bandera, capital, partidos, sindicatos, FF. AA., art. 9 | **Cuatro** valores superiores; garantías del **9.3** |
| III. Reforma | Iniciativa (166 → 87.1 y 2); art. 167; art. 168; límites (169) | 167: **3/5**, referéndum si lo pide **1/10** en **15 días**; 168: **2/3**, disolución, referéndum **obligatorio** |
| IV. Reformas | Art. 95; reformas de 1992, 2011, 2024 y 2026 | Arts. **13.2**, **135**, **49** y **69.3** |

?> **Trampas frecuentes:** «el pueblo español **aprueba**» (lo **ratifica**; aprueban las Cortes); «**9** adicionales y **4** transitorias» (es al revés); «la **seguridad** como valor superior» (son libertad, justicia, igualdad y pluralismo político); «el art. **14** está protegido por el art. 168» (la protección empieza en la Sección 1.ª, art. 15); «el referéndum del 167 es **obligatorio**» (es **facultativo**); «**dos tercios del Senado**» en el 167.2 (son dos tercios del **Congreso** con mayoría absoluta del Senado); «la **iniciativa popular** puede proponer la reforma» (el art. 166 remite solo al 87.1 y 2).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
Q = [
 ("CE", "preambulo", "Preámbulo", "Según el Preámbulo de la Constitución Española, ¿quién, «en uso de su soberanía», proclama su voluntad?",
  ["La Nación española.", "El pueblo español, representado por las Cortes.", "Las Cortes Generales.", "El Rey, en nombre de la Nación española."],
  "Preámbulo: «La Nación española, … en uso de su soberanía, proclama su voluntad de».", ["La Nación española", "en uso de su soberanía, proclama su voluntad de"]),
 ("CE", "preambulo", "Preámbulo", "Según el Preámbulo de la Constitución Española, la Nación española proclama su voluntad de consolidar un Estado de Derecho que asegure:",
  ["El imperio de la ley como expresión de la voluntad popular.", "La primacía de la Constitución sobre los tratados internacionales.", "La separación de poderes como garantía de la libertad.", "La soberanía del pueblo como fuente de todo poder."],
  "Preámbulo: «Consolidar un Estado de Derecho que asegure el imperio de la ley como expresión de la voluntad popular».", "Consolidar un Estado de Derecho que asegure el imperio de la ley como expresión de la voluntad popular"),
 ("CE", "preambulo", "Preámbulo", "Según el Preámbulo de la Constitución Española, la Nación española proclama su voluntad de establecer:",
  ["Una sociedad democrática avanzada.", "Un Estado social y democrático de Derecho.", "Una Monarquía parlamentaria.", "Un orden económico de libre mercado."],
  "Preámbulo: «Establecer una sociedad democrática avanzada». El Estado social y democrático de Derecho y la Monarquía parlamentaria están en el art. 1, no en el Preámbulo.", "Establecer una sociedad democrática avanzada"),
 ("CE", "tx", "Estructura", "El Título X de la Constitución Española se denomina:",
  ["De la reforma constitucional.", "Del Tribunal Constitucional.", "De la Organización Territorial del Estado.", "De las relaciones entre el Gobierno y las Cortes Generales."],
  "Rúbrica del Título X: «De la reforma constitucional». IX: Tribunal Constitucional; VIII: Organización Territorial; V: relaciones Gobierno-Cortes.", "De la reforma constitucional"),
 ("CE", "tv", "Estructura", "El Título V de la Constitución Española se denomina:",
  ["De las relaciones entre el Gobierno y las Cortes Generales.", "Del Gobierno y de la Administración.", "De las Cortes Generales.", "Economía y Hacienda."],
  "Rúbrica del Título V. El IV es «Del Gobierno y de la Administración»; el III, «De las Cortes Generales»; el VII, «Economía y Hacienda».", "De las relaciones entre el Gobierno y las Cortes Generales"),
 ("CE", "tvii", "Estructura", "¿Qué título de la Constitución Española lleva por rúbrica «Economía y Hacienda»?",
  ["El Título VII.", "El Título VI.", "El Título VIII.", "El Título IV."],
  "Título VII: «Economía y Hacienda» (arts. 128 a 136).", "Economía y Hacienda"),
 ("CE", "ctercero", "Estructura", "El Capítulo tercero del Título I de la Constitución Española se denomina:",
  ["De los principios rectores de la política social y económica.", "De las garantías de las libertades y derechos fundamentales.", "De la suspensión de los derechos y libertades.", "Derechos y libertades."],
  "Capítulo tercero del Título I: «De los principios rectores de la política social y económica». El cuarto es el de las garantías y el quinto el de la suspensión.", "De los principios rectores de la política social y económica"),
 ("CE", "ctercero-3", "Estructura", "En el Título VIII de la Constitución Española, el Capítulo tercero se denomina:",
  ["De las Comunidades Autónomas.", "De la Administración Local.", "Principios generales.", "De la Organización Territorial del Estado."],
  "Título VIII: Capítulo primero «Principios generales», segundo «De la Administración Local», tercero «De las Comunidades Autónomas».", "De las Comunidades Autónomas"),
 ("CE", "primera", "Disposiciones", "Según la Constitución Española, ¿qué disposición declara que «La Constitución ampara y respeta los derechos históricos de los territorios forales»?",
  ["La disposición adicional primera.", "La disposición transitoria primera.", "La disposición adicional segunda.", "La disposición final."],
  "Disposición adicional primera.", "La Constitución ampara y respeta los derechos históricos de los territorios forales"),
 ("CE", "tercera", "Disposiciones", "Según la disposición adicional tercera de la Constitución Española, la modificación del régimen económico y fiscal del archipiélago canario requerirá:",
  ["Informe previo de la Comunidad Autónoma o, en su caso, del órgano provisional autonómico.", "Ley orgánica aprobada por mayoría absoluta del Congreso.", "Referéndum de los electores de las islas.", "Acuerdo de los Cabildos insulares."],
  "Disposición adicional tercera.", "requerirá informe previo de la Comunidad Autónoma o, en su caso, del órgano provisional autonómico"),
 ("CE", "dd", "Disposiciones", "Según la disposición derogatoria de la Constitución Española, queda derogada, en primer lugar:",
  ["La Ley 1/1977, de 4 de enero, para la Reforma Política.", "La Ley Orgánica 2/1980, sobre regulación de las distintas modalidades de referéndum.", "El Código Civil en lo que se oponga a la Constitución.", "La Ley de Régimen Local."],
  "Disposición derogatoria, apartado 1.", "Queda derogada la Ley 1/1977, de 4 de enero, para la Reforma Política"),
 ("CE", "df", "Disposiciones", "Según su disposición final, la Constitución Española entró en vigor:",
  ["El mismo día de la publicación de su texto oficial en el boletín oficial del Estado.", "A los veinte días de su publicación en el boletín oficial del Estado.", "El día de su ratificación en referéndum.", "El día de su sanción por el Rey."],
  "Disposición final: «entrará en vigor el mismo día de la publicación de su texto oficial en el boletín oficial del Estado».", "entrará en vigor el mismo día de la publicación de su texto oficial en el boletín oficial del Estado"),
 ("CE", "quinta", "Disposiciones", "Según la disposición transitoria quinta de la Constitución Española, las ciudades de Ceuta y Melilla podrán constituirse en Comunidades Autónomas si así lo autorizan las Cortes Generales mediante:",
  ["Una ley orgánica.", "Una ley de armonización.", "Un acuerdo del Senado por mayoría absoluta.", "Una ley marco."],
  "Disposición transitoria quinta: «así lo autorizan las Cortes Generales, mediante una ley orgánica».", "así lo autorizan las Cortes Generales, mediante una ley orgánica"),
 ("CE", "Artículo 1", "Título preliminar", "Según el artículo 1.1 de la Constitución Española, son valores superiores de su ordenamiento jurídico:",
  ["La libertad, la justicia, la igualdad y el pluralismo político.", "La libertad, la justicia, la igualdad y la seguridad jurídica.", "La dignidad de la persona, la libertad y la igualdad.", "La justicia, la solidaridad, la igualdad y el pluralismo político."],
  "Art. 1.1 CE: cuatro valores superiores.", "la libertad, la justicia, la igualdad y el pluralismo político"),
 ("CE", "Artículo 1", "Título preliminar", "Según el artículo 1.3 de la Constitución Española, la forma política del Estado español es:",
  ["La Monarquía parlamentaria.", "La Monarquía constitucional.", "El Estado social y democrático de Derecho.", "La Monarquía hereditaria."],
  "Art. 1.3 CE.", "La forma política del Estado español es la Monarquía parlamentaria"),
 ("CE", "Artículo 1", "Título preliminar", "Según el artículo 1.2 de la Constitución Española, la soberanía nacional reside en:",
  ["El pueblo español, del que emanan los poderes del Estado.", "Las Cortes Generales, que representan al pueblo español.", "La Nación española, de la que emana la Corona.", "El Rey, como Jefe del Estado."],
  "Art. 1.2 CE.", "La soberanía nacional reside en el pueblo español, del que emanan los poderes del Estado"),
 ("CE", "Artículo 2", "Título preliminar", "Según el artículo 2 de la Constitución Española, la Constitución reconoce y garantiza el derecho a la autonomía de:",
  ["Las nacionalidades y regiones que integran la Nación española.", "Los municipios y las provincias.", "Los territorios forales.", "Las Comunidades Autónomas que se constituyan."],
  "Art. 2 CE: «el derecho a la autonomía de las nacionalidades y regiones que la integran».", "reconoce y garantiza el derecho a la autonomía de las nacionalidades y regiones que la integran"),
 ("CE", "Artículo 3", "Título preliminar", "Según el artículo 3.1 de la Constitución Española, respecto del castellano todos los españoles tienen:",
  ["El deber de conocerla y el derecho a usarla.", "El derecho a conocerla y el deber de usarla.", "El derecho a conocerla y a usarla.", "El deber de conocerla y de usarla ante las Administraciones Públicas."],
  "Art. 3.1 CE.", "Todos los españoles tienen el deber de conocerla y el derecho a usarla"),
 ("CE", "Artículo 4", "Título preliminar", "Según el artículo 4.1 de la Constitución Española, en la bandera de España la franja amarilla es:",
  ["De doble anchura que cada una de las rojas.", "De igual anchura que cada una de las rojas.", "De triple anchura que cada una de las rojas.", "De doble anchura que las dos rojas juntas."],
  "Art. 4.1 CE.", "siendo la amarilla de doble anchura que cada una de las rojas"),
 ("CE", "Artículo 6", "Título preliminar", "Según el artículo 6 de la Constitución Española, los partidos políticos:",
  ["Son instrumento fundamental para la participación política.", "Son el único cauce de participación política.", "Se crean previa autorización del Ministerio del Interior.", "Deben tener una estructura interna jerárquica."],
  "Art. 6 CE: «son instrumento fundamental para la participación política»; creación libre y estructura democrática.", "son instrumento fundamental para la participación política"),
 ("CE", "Artículo 7", "Título preliminar", "Según el artículo 7 de la Constitución Española, los sindicatos de trabajadores y las asociaciones empresariales contribuyen a:",
  ["La defensa y promoción de los intereses económicos y sociales que les son propios.", "La formación y manifestación de la voluntad popular.", "La participación de todos los ciudadanos en la vida política.", "La defensa del ordenamiento constitucional."],
  "Art. 7 CE. La formación de la voluntad popular es función de los partidos (art. 6).", "contribuyen a la defensa y promoción de los intereses económicos y sociales que les son propios"),
 ("CE", "Artículo 8", "Título preliminar", "Según el artículo 8.2 de la Constitución Española, las bases de la organización militar se regularán por:",
  ["Una ley orgánica.", "Una ley ordinaria.", "Un real decreto del Gobierno.", "Las Reales Ordenanzas."],
  "Art. 8.2 CE.", "Una ley orgánica regulará las bases de la organización militar"),
 ("CE", "Artículo 9", "Título preliminar", "Según el artículo 9.1 de la Constitución Española, están sujetos a la Constitución y al resto del ordenamiento jurídico:",
  ["Los ciudadanos y los poderes públicos.", "Solo los poderes públicos.", "Los españoles y los extranjeros residentes.", "Las Administraciones Públicas."],
  "Art. 9.1 CE.", "Los ciudadanos y los poderes públicos están sujetos a la Constitución y al resto del ordenamiento jurídico"),
 ("CE", "Artículo 9", "Título preliminar", "Según el artículo 9.2 de la Constitución Española, corresponde a los poderes públicos promover las condiciones para que la libertad y la igualdad del individuo y de los grupos en que se integra sean:",
  ["Reales y efectivas.", "Plenas e iguales.", "Formales y materiales.", "Libres y solidarias."],
  "Art. 9.2 CE.", "sean reales y efectivas"),
 ("CE", "Artículo 166", "Reforma", "Según el artículo 166 de la Constitución Española, la iniciativa de reforma constitucional se ejercerá en los términos previstos en:",
  ["Los apartados 1 y 2 del artículo 87.", "Los apartados 1, 2 y 3 del artículo 87.", "El apartado 3 del artículo 87.", "El artículo 92."],
  "Art. 166 CE: solo 87.1 y 2 (no la iniciativa popular del 87.3).", "en los términos previstos en los apartados 1 y 2 del artículo 87"),
 ("CE", "Artículo 167", "Reforma", "Según el artículo 167.1 de la Constitución Española, los proyectos de reforma constitucional deberán ser aprobados por una mayoría de:",
  ["Tres quintos de cada una de las Cámaras.", "Dos tercios de cada una de las Cámaras.", "Mayoría absoluta de cada una de las Cámaras.", "Tres quintos del Congreso y mayoría absoluta del Senado."],
  "Art. 167.1 CE.", "deberán ser aprobados por una mayoría de tres quintos de cada una de las Cámaras"),
 ("CE", "Artículo 167", "Reforma", "Según el artículo 167.1 de la Constitución Española, si no hubiera acuerdo entre ambas Cámaras sobre un proyecto de reforma constitucional, se intentará obtenerlo mediante:",
  ["Una Comisión de composición paritaria de Diputados y Senadores.", "La Comisión Constitucional del Congreso.", "Una sesión conjunta de las Cortes Generales.", "Un dictamen del Consejo de Estado."],
  "Art. 167.1 CE.", "mediante la creación de una Comisión de composición paritaria de Diputados y Senadores"),
 ("CE", "Artículo 167", "Reforma", "Según el artículo 167.2 de la Constitución Española, de no lograrse la aprobación mediante la Comisión paritaria, el Congreso podrá aprobar la reforma:",
  ["Por mayoría de dos tercios, siempre que el texto hubiere obtenido el voto favorable de la mayoría absoluta del Senado.", "Por mayoría absoluta, siempre que el texto hubiere obtenido el voto favorable de tres quintos del Senado.", "Por mayoría de tres quintos, sin necesidad de votación en el Senado.", "Por mayoría de dos tercios, siempre que el texto hubiere obtenido el voto favorable de dos tercios del Senado."],
  "Art. 167.2 CE.", "siempre que el texto hubiere obtenido el voto favorable de la mayoría absoluta del Senado, el Congreso, por mayoría de dos tercios, podrá aprobar la reforma"),
 ("CE", "Artículo 167", "Reforma", "Según el artículo 167.3 de la Constitución Española, la reforma aprobada por las Cortes Generales será sometida a referéndum para su ratificación cuando así lo soliciten:",
  ["Dentro de los quince días siguientes a su aprobación, una décima parte de los miembros de cualquiera de las Cámaras.", "Dentro de los treinta días siguientes a su aprobación, una quinta parte de los miembros de cualquiera de las Cámaras.", "Dentro de los quince días siguientes a su aprobación, una décima parte de los miembros de ambas Cámaras.", "Dentro del mes siguiente a su aprobación, el Gobierno o una décima parte de los Diputados."],
  "Art. 167.3 CE.", "dentro de los quince días siguientes a su aprobación, una décima parte de los miembros de cualquiera de las Cámaras"),
 ("CE", "Artículo 168", "Reforma", "Según el artículo 168.1 de la Constitución Española, ¿cuál de las siguientes reformas parciales exige el procedimiento de ese artículo?",
  ["La que afecte al Título II.", "La que afecte al Título III.", "La que afecte al Capítulo tercero del Título I.", "La que afecte al Título VIII."],
  "Art. 168.1 CE: revisión total o parcial que afecte al Título preliminar, al Capítulo segundo, Sección primera del Título I, o al Título II.", "al Capítulo segundo, Sección primera del Título I, o al Título II"),
 ("CE", "Artículo 168", "Reforma", "Según el artículo 168.1 de la Constitución Española, cuando se propusiere la revisión total de la Constitución se procederá a la aprobación del principio por:",
  ["Mayoría de dos tercios de cada Cámara, y a la disolución inmediata de las Cortes.", "Mayoría de tres quintos de cada Cámara, y a la convocatoria de referéndum.", "Mayoría absoluta del Congreso, y a la disolución inmediata de las Cortes.", "Mayoría de dos tercios del Congreso, y a la disolución del Congreso."],
  "Art. 168.1 CE.", "se procederá a la aprobación del principio por mayoría de dos tercios de cada Cámara, y a la disolución inmediata de las Cortes"),
 ("CE", "Artículo 168", "Reforma", "Según el artículo 168.3 de la Constitución Española, aprobada la reforma por las Cortes Generales por este procedimiento:",
  ["Será sometida a referéndum para su ratificación.", "Será sometida a referéndum solo si lo solicita una décima parte de los miembros de cualquiera de las Cámaras.", "Será sancionada por el Rey sin necesidad de referéndum.", "Será sometida al Tribunal Constitucional antes de su ratificación."],
  "Art. 168.3 CE: referéndum obligatorio (en el 167 es facultativo).", "Aprobada la reforma por las Cortes Generales, será sometida a referéndum para su ratificación."),
 ("CE", "Artículo 169", "Reforma", "Según el artículo 169 de la Constitución Española, no podrá iniciarse la reforma constitucional:",
  ["En tiempo de guerra o de vigencia de alguno de los estados previstos en el artículo 116.", "Solo durante la vigencia del estado de sitio.", "Durante el último año de la legislatura.", "Mientras esté en funciones el Gobierno."],
  "Art. 169 CE.", "No podrá iniciarse la reforma constitucional en tiempo de guerra o de vigencia de alguno de los estados previstos en el artículo 116"),
 ("CE", "Artículo 75", "Reforma", "Según el artículo 75.3 de la Constitución Española, la aprobación de la reforma constitucional:",
  ["No puede delegarse en las Comisiones Legislativas Permanentes.", "Puede delegarse en la Comisión Constitucional de cada Cámara.", "Puede delegarse en las Comisiones si el Pleno no la recaba.", "Corresponde a la Diputación Permanente entre legislaturas."],
  "Art. 75.3 CE: quedan exceptuados de la delegación en Comisiones «la reforma constitucional»…", "Quedan exceptuados de lo dispuesto en el apartado anterior la reforma constitucional"),
 ("RCD", "art146", "Reforma", "Según el artículo 146.1 del Reglamento del Congreso, las proposiciones de reforma constitucional deberán ir suscritas por:",
  ["Dos grupos parlamentarios o una quinta parte de los miembros de la Cámara.", "Un grupo parlamentario o quince Diputados.", "Tres grupos parlamentarios o una décima parte de los miembros de la Cámara.", "La mayoría absoluta de los miembros de la Cámara."],
  "Art. 146.1 RCD.", "deberán ir suscritas por dos grupos parlamentarios o por una quinta parte de los miembros de la Cámara"),
 ("RS", "Artículo 152", "Reforma", "Según el artículo 152 del Reglamento del Senado, podrán presentar proposiciones articuladas de reforma constitucional:",
  ["Cincuenta Senadores que no pertenezcan a un mismo Grupo parlamentario.", "Veinticinco Senadores de cualquier Grupo parlamentario.", "Dos Grupos parlamentarios.", "Una décima parte de los Senadores."],
  "Art. 152 RS.", "Cincuenta Senadores que no pertenezcan a un mismo Grupo parlamentario podrán presentar proposiciones articuladas de reforma constitucional"),
 ("RS", "Artículo 159", "Reforma", "Según el artículo 159 del Reglamento del Senado, en el procedimiento del artículo 168 de la Constitución la nueva Cámara que resulte elegida deberá ratificar la reforma propuesta por:",
  ["Mayoría absoluta de sus miembros.", "Mayoría de dos tercios de sus miembros.", "Mayoría de tres quintos de sus miembros.", "Mayoría simple de los presentes."],
  "Art. 159 RS.", "deberá ratificar, por mayoría absoluta de sus miembros, la reforma propuesta"),
 ("LO2_1980", "Artículo séptimo", "Reforma", "Según el artículo 7 de la Ley Orgánica 2/1980, recibida la comunicación de las Cortes Generales del proyecto de reforma constitucional que haya de ser objeto de ratificación popular, se procederá a la convocatoria del referéndum dentro del plazo de:",
  ["Treinta días, y a su celebración dentro de los sesenta días siguientes.", "Quince días, y a su celebración dentro de los treinta días siguientes.", "Sesenta días, y a su celebración dentro de los noventa días siguientes.", "Treinta días, y a su celebración dentro de los ciento veinte días siguientes."],
  "Art. 7 LO 2/1980.", "se procederá, en todo caso, a la convocatoria dentro del plazo de treinta días y a su celebración dentro de los sesenta días siguientes"),
 ("CE", "Artículo 95", "Reformas", "Según el artículo 95.1 de la Constitución Española, la celebración de un tratado internacional que contenga estipulaciones contrarias a la Constitución exigirá:",
  ["La previa revisión constitucional.", "La autorización de las Cortes por mayoría absoluta.", "El dictamen previo del Consejo de Estado.", "Su aprobación por ley orgánica."],
  "Art. 95.1 CE.", "exigirá la previa revisión constitucional"),
 ("REF2026", "preambulo", "Reformas", "La Reforma de la Constitución Española de 19 de mayo de 2026 modificó:",
  ["El apartado 3 del artículo 69.", "El apartado 2 del artículo 13.", "El artículo 49.", "El artículo 135."],
  "Reforma de 19 de mayo de 2026: «El apartado 3 del artículo 69 de la Constitución Española queda redactado como sigue». 13.2 (1992), 135 (2011) y 49 (2024) son las otras tres.", "El apartado 3 del artículo 69 de la Constitución Española queda redactado como sigue"),
 ("REF2011", "preambulo", "Reformas", "Según la disposición adicional única de la Reforma del artículo 135 de la Constitución Española, de 27 de septiembre de 2011, los límites de déficit estructural establecidos en el artículo 135.2 entrarán en vigor:",
  ["A partir de 2020.", "A partir de 2012.", "El mismo día de la publicación de la reforma.", "A partir de 2015."],
  "Reforma de 2011, disposición adicional única, apartado 3.", "Los límites de déficit estructural establecidos en el artículo 135.2 de la Constitución Española entrarán en vigor a partir de 2020"),
 ("REF1992", "preambulo", "Reformas", "La Reforma de la Constitución Española de 27 de agosto de 1992 modificó el artículo 13.2 para permitir, por tratado o ley y atendiendo a criterios de reciprocidad, el derecho de sufragio en las elecciones municipales:",
  ["Activo y pasivo.", "Solo activo.", "Solo pasivo.", "Activo y pasivo, también en las elecciones autonómicas."],
  "Nuevo art. 13.2: «el derecho de sufragio activo y pasivo en las elecciones municipales».", "para el derecho de sufragio activo y pasivo en las elecciones municipales"),
]
for k, art, cat, en, ops, ex, fr in Q: T.q(k, art, cat, en, ops, ex, fr)
T.real("X", 1, "Estructura"); T.real("X", 2, "Disposiciones"); T.real("X", 3, "Preámbulo"); T.real("P", 51, "Título preliminar")

# Flashcards
for q_, a_, cat in [
  ("¿Quién aprueba y quién ratifica la Constitución, según el Preámbulo?", "Las Cortes aprueban y el pueblo español ratifica.", "Preámbulo"),
  ("¿Quién proclama su voluntad en el Preámbulo?", "La Nación española, en uso de su soberanía.", "Preámbulo"),
  ("¿Cuántos títulos y artículos tiene la Constitución?", "Título preliminar y Títulos I a X (once); 169 artículos.", "Estructura"),
  ("¿Qué títulos tienen capítulos?", "El I (cinco capítulos; el segundo con dos secciones), el III (tres) y el VIII (tres).", "Estructura"),
  ("Rúbricas de los Títulos VII, VIII, IX y X", "VII Economía y Hacienda; VIII De la Organización Territorial del Estado; IX Del Tribunal Constitucional; X De la reforma constitucional.", "Estructura"),
  ("¿Cuántas disposiciones tiene la Constitución?", "4 adicionales, 9 transitorias, 1 derogatoria y 1 final.", "Disposiciones"),
  ("¿Qué disposición ampara los derechos históricos de los territorios forales?", "La adicional primera.", "Disposiciones"),
  ("¿Cuándo entró en vigor la Constitución?", "El mismo día de la publicación de su texto oficial en el BOE (disposición final).", "Disposiciones"),
  ("Valores superiores (art. 1.1)", "Libertad, justicia, igualdad y pluralismo político.", "Título preliminar"),
  ("Garantías del art. 9.3", "Legalidad, jerarquía normativa, publicidad de las normas, irretroactividad de las disposiciones sancionadoras no favorables o restrictivas de derechos individuales, seguridad jurídica, responsabilidad e interdicción de la arbitrariedad de los poderes públicos.", "Título preliminar"),
  ("Misión de las Fuerzas Armadas (art. 8.1)", "Garantizar la soberanía e independencia de España, defender su integridad territorial y el ordenamiento constitucional.", "Título preliminar"),
  ("Iniciativa de reforma (art. 166)", "La del art. 87.1 y 2: Gobierno, Congreso, Senado y Asambleas de las Comunidades Autónomas. No la popular.", "Reforma"),
  ("Mayoría del art. 167.1", "Tres quintos de cada una de las Cámaras.", "Reforma"),
  ("Vía alternativa del art. 167.2", "Mayoría absoluta del Senado y dos tercios del Congreso.", "Reforma"),
  ("Referéndum del art. 167.3", "Facultativo: lo piden, en 15 días desde la aprobación, una décima parte de los miembros de cualquiera de las Cámaras.", "Reforma"),
  ("¿Qué partes protege el art. 168?", "Revisión total, Título preliminar, Capítulo segundo Sección primera del Título I y Título II.", "Reforma"),
  ("Pasos del art. 168", "Principio por 2/3 de cada Cámara y disolución inmediata; las nuevas Cámaras ratifican y aprueban el texto por 2/3; referéndum obligatorio.", "Reforma"),
  ("Límite del art. 169", "No puede iniciarse en tiempo de guerra ni durante los estados de alarma, excepción o sitio.", "Reforma"),
  ("Plazos de la LO 2/1980 para el referéndum de reforma (art. 7)", "Convocatoria en 30 días desde la comunicación de las Cortes; celebración en los 60 días siguientes.", "Reforma"),
  ("Tratado contrario a la Constitución (art. 95.1)", "Exige la previa revisión constitucional.", "Reformas"),
  ("Las cuatro reformas de la Constitución", "Art. 13.2 (1992), art. 135 (2011), art. 49 (2024) y art. 69.3 (2026).", "Reformas"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Fórmula de promulgación", "Encabezamiento de la Constitución en que el Rey hace saber que las Cortes han aprobado y el pueblo español ratificado la Constitución.", "s1", "Estructura")
T.glos("Preámbulo", "Texto sin número de artículo en que la Nación española, en uso de su soberanía, proclama su voluntad (seis objetivos).", "s1", "Estructura")
T.glos("Título preliminar", "Primera división del articulado (arts. 1 a 9), sin rúbrica; protegido por el art. 168.", "s2", "Estructura")
T.glos("Rúbrica", "Nombre de un título, capítulo o sección (p. ej., Título VIII «De la Organización Territorial del Estado»).", "s2", "Estructura")
T.glos("Disposición transitoria", "Regla para el paso al nuevo régimen; la Constitución tiene nueve (proceso autonómico, primeras Cámaras, primera renovación del TC).", "s3", "Disposiciones")
T.glos("Valores superiores", "Los cuatro que propugna el Estado social y democrático de Derecho: libertad, justicia, igualdad y pluralismo político (art. 1.1).", "s5", "Título preliminar")
T.glos("Monarquía parlamentaria", "Forma política del Estado español (art. 1.3).", "s5", "Título preliminar")
T.glos("Interdicción de la arbitrariedad", "Garantía del art. 9.3: prohibición de la arbitrariedad de los poderes públicos.", "s8", "Título preliminar")
T.glos("Iniciativa de reforma", "Facultad de proponer la reforma constitucional; corresponde a los titulares del art. 87.1 y 2 (art. 166).", "s10", "Reforma")
T.glos("Comisión paritaria", "Comisión de Diputados y Senadores en igual número que busca el acuerdo entre las Cámaras en el art. 167 (Comisión Mixta paritaria en los Reglamentos).", "s11", "Reforma")
T.glos("Referéndum de ratificación", "Votación popular sobre la reforma aprobada: facultativo en el art. 167.3 y obligatorio en el art. 168.3.", "s11", "Reforma")
T.glos("Revisión total", "Reforma de toda la Constitución; sigue el procedimiento del art. 168.", "s12", "Reforma")
T.glos("Previa revisión constitucional", "Reforma de la Constitución exigida antes de celebrar un tratado con estipulaciones contrarias a ella (art. 95.1).", "s15", "Reformas")

# Cronología (fechas de los metadatos del BOE)
T.hito("1978", "Constitución Española (27-12-1978; BOE de 29-12-1978)", "Entra en vigor el día de su publicación (disposición final)", "normativo", "s3")
T.hito("1980", "Ley Orgánica 2/1980, de 18 de enero, sobre regulación de las distintas modalidades de referéndum (BOE de 23-1-1980)", "Arts. 4 y 7: referéndum de reforma constitucional", "normativo", "s11")
T.hito("1982", "Reglamento del Congreso de 10 de febrero de 1982 (así denominado desde su reforma de 22-7-2025; BOE de 5-3-1982)", "Arts. 146 y 147: reforma constitucional", "normativo", "s11")
T.hito("1992", "Reforma del artículo 13, apartado 2, de la Constitución (27-8-1992; BOE de 28-8-1992)", "Primera reforma: sufragio activo y pasivo en elecciones municipales", "normativo", "s16")
T.hito("1994", "Texto refundido del Reglamento del Senado (3-5-1994; BOE de 13-5-1994)", "Arts. 152 a 159: revisión constitucional", "normativo", "s12")
T.hito("2011", "Reforma del artículo 135 de la Constitución (27-9-2011; BOE de 27-9-2011)", "Estabilidad presupuestaria", "normativo", "s16")
T.hito("2024", "Reforma del artículo 49 de la Constitución (15-2-2024; BOE de 17-2-2024)", "Personas con discapacidad", "normativo", "s16")
T.hito("2026", "Reforma del apartado 3 del artículo 69 de la Constitución (19-5-2026; BOE de 20-5-2026)", "Formentera elige un Senador propio", "normativo", "s16")

T.publicar()
