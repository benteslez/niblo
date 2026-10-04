# -*- coding: utf-8 -*-
"""Tema I.5 (B1T05): El poder legislativo. Las Cortes Generales. Composición y
atribuciones del Congreso de los Diputados y del Senado.
Método del I.2: mapa → bloques (I a VI) con guía; cada artículo, texto literal del
BOE + ficha de casillas fijas; cierre 1 (preguntas oficiales) y cierre 2 (repaso).
Normas (textos consolidados del BOE): CE, Título III, capítulo I (arts. 66 a 80) y
arts. 87 a 94; LO 5/1985 (LOREG), arts. 162 y 165; Reglamento del Congreso (RCD) y
texto refundido del Reglamento del Senado (RS) en composición y órganos."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO["RS"] = "Reglamento del Senado"
CORTO["LOREG"] = "LOREG"

T = Tema("B1T05",
  "Seis preguntas: I. Qué son las Cortes Generales (arts. 66 y 67 CE) · II. Cómo se compone el Congreso (art. 68; LOREG, art. 162; Reglamento del Congreso, arts. 1 a 5) · III. Cómo se compone el Senado (art. 69; LOREG, art. 165; Reglamento del Senado, arts. 2 a 5) · IV. Qué estatuto tienen Diputados y Senadores (arts. 70 y 71) · V. Cómo se organizan y funcionan las Cámaras (arts. 72 a 80 y Reglamentos) · VI. Qué atribuciones tienen (arts. 66.2 y 87 a 94). Cada artículo: texto literal del BOE y ficha.",
  ["Cortes Generales", "Art. 66", "Bicameralismo", "Congreso: art. 68", "LOREG art. 162", "Senado: art. 69", "LOREG art. 165", "Inelegibilidad: art. 70", "Inviolabilidad e inmunidad", "Reglamentos de las Cámaras", "Mesa", "Grupos parlamentarios", "Junta de Portavoces", "Diputación Permanente", "Comisiones", "Iniciativa legislativa", "Veto del Senado", "Tratados: art. 94"])

# =============================================================================
T.ap("s0", "Mapa del tema: seis preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque I, tema 5):
> El poder legislativo. Las Cortes Generales. Composición y atribuciones del Congreso de los Diputados y del Senado.

### El hilo conductor

El epígrafe se lee como **seis preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Constitución | Otras normas |
|---|---|---|---|
| **I** | ¿Qué son las Cortes Generales? | Arts. 66.1 y 3 y 67 | — |
| **II** | ¿Cómo se compone el Congreso? | Art. 68 | LOREG, art. 162; Reglamento del Congreso, arts. 1 a 5 |
| **III** | ¿Cómo se compone el Senado? | Art. 69 | LOREG, art. 165; Reglamento del Senado, arts. 2 a 5 |
| **IV** | ¿Qué estatuto tienen Diputados y Senadores? | Arts. 70 y 71 | — |
| **V** | ¿Cómo se organizan y funcionan las Cámaras? | Arts. 72 a 80 | Reglamento del Congreso, arts. 23 a 39, 46 y 57; Reglamento del Senado, arts. 7, 27, 35, 43, 45, 48 y 49 |
| **VI** | ¿Qué atribuciones tienen? | Arts. 66.2, 87 a 90 y 92 a 94 (y cuadro de las atribuciones repartidas por la Constitución) | — |

!> **La idea que une los seis bloques:** las Cortes **representan al pueblo español** y son **dos Cámaras** (I). El **Congreso** se elige por provincias con criterios de **representación proporcional** (II); el **Senado** es la Cámara de **representación territorial**, con Senadores elegidos y Senadores **designados por las Comunidades Autónomas** (III). Sus miembros tienen un estatuto propio (IV) y las Cámaras se organizan con **autonomía** (V). Sus atribuciones: **legislar, aprobar los Presupuestos y controlar al Gobierno** (VI), con un claro **predominio del Congreso**.

### Fronteras con otros temas

- Tipos de leyes, ley orgánica (art. 81), decreto legislativo y decreto-ley (arts. 82 a 86) y sanción del Rey (art. 91): tema IV.2.
- Relaciones Gobierno-Cortes (investidura, cuestión de confianza, moción de censura, arts. 99 y 108 a 116): tema I.6. Aquí solo se sitúan en el cuadro de atribuciones (→ VI.5).
- Tribunal Constitucional (tema I.3), Corona (tema I.4), Defensor del Pueblo (tema I.2) y reforma constitucional (tema I.1): solo se mencionan cuando las Cortes intervienen.

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué son las Cortes Generales? (arts. 66 y 67)", donde(
  "Primera pregunta del tema. El Título III de la Constitución («De las Cortes Generales») se abre con su **definición**: a quién representan, de qué Cámaras se forman y qué reglas comunes tienen sus miembros.",
  ["1 Representación, dos Cámaras e inviolabilidad (art. 66.1 y 3)", "2 Reglas comunes a los parlamentarios (art. 67)"]))

T.ap("s1", "I.1 Representación, dos Cámaras e inviolabilidad (art. 66.1 y 3)", f"""
Las funciones de las Cortes (art. 66.2) se estudian con las atribuciones (→ VI.1.1).

{unidad("1.1 Representan al pueblo español y son dos Cámaras (art. 66.1)",
  lit("CE", "Artículo 66", ["representan al pueblo español", "el Congreso de los Diputados y el Senado"], solo=[1]),
  fichab("Las Cortes Generales: órgano que representa al pueblo español",
         f"{c('CE', 'Artículo 66', 'el Congreso de los Diputados y el Senado')}",
         "Bicameralismo: dos Cámaras (composición → II y → III)",
         "—",
         "Representan al **pueblo español** (no a las Comunidades Autónomas: la representación **territorial** es la del **Senado**, art. 69.1 → III.1.1)."))}

{unidad("1.2 Inviolabilidad de las Cortes (art. 66.3)",
  lit("CE", "Artículo 66", ["inviolables"], solo=[3]),
  fichab("Garantía de la institución", "Las Cortes Generales", "—", "—",
         "No confundir la inviolabilidad **de las Cortes** (66.3) con la **de Diputados y Senadores** por sus opiniones (71.1 → IV.2.1)."))}
""", 2)

T.ap("s2", "I.2 Reglas comunes a los parlamentarios (art. 67)", f"""
{unidad("2.1 Nadie puede estar en las dos Cámaras (art. 67.1)",
  lit("CE", "Artículo 67", ["miembro de las dos Cámaras simultáneamente", "acumular el acta de una Asamblea de Comunidad Autónoma con la de Diputado al Congreso"], solo=[1]),
  fichab("Prohibición de doble mandato",
         "Diputados, Senadores y miembros de las Asambleas autonómicas",
         ["No se puede ser **Diputado y Senador** a la vez", "No se puede acumular el acta autonómica con la de **Diputado**"],
         "—",
         "La prohibición de acumular el acta autonómica se refiere al acta de **Diputado al Congreso**; el artículo no la extiende al acta de Senador."))}

{unidad("2.2 Prohibición del mandato imperativo (art. 67.2)",
  lit("CE", "Artículo 67", ["no estarán ligados por mandato imperativo"], solo=[2]),
  fichab("Libertad del representante", c("CE", "Artículo 67", "Los miembros de las Cortes Generales"), "—", "—",
         "Vale para **los miembros de las Cortes**: Diputados y Senadores."))}

{unidad("2.3 Reuniones sin convocatoria reglamentaria (art. 67.3)",
  lit("CE", "Artículo 67", ["no vincularán a las Cámaras", "ni ostentar sus privilegios"], solo=[3]),
  fichab("Ineficacia de las reuniones de parlamentarios no convocadas reglamentariamente", "Los parlamentarios reunidos sin convocatoria reglamentaria",
         ["No vinculan a las Cámaras", "No pueden ejercer sus funciones ni ostentar sus privilegios"], "—",
         "Relaciónalo con el art. 79.1: para adoptar acuerdos las Cámaras deben estar **reunidas reglamentariamente** (→ V.6.1)."))}

{resumen([
  "Las Cortes **representan al pueblo español** y están formadas por **Congreso y Senado** (66.1); son **inviolables** (66.3).",
  "Nadie puede ser miembro de **las dos Cámaras** ni acumular el acta autonómica con la de **Diputado** (67.1).",
  "**Sin mandato imperativo** (67.2); las reuniones **sin convocatoria reglamentaria** no vinculan (67.3)."],
  "Siguiente: II. ¿Cómo se compone el Congreso?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Cómo se compone el Congreso? (art. 68; LOREG, art. 162; Reglamento del Congreso, arts. 1 a 5)", donde(
  "Segunda pregunta. La Constitución fija una **horquilla** de Diputados, la **circunscripción** y el criterio **proporcional**; la LOREG concreta el número y el reparto, y el Reglamento del Congreso regula la **sesión constitutiva**.",
  ["1 Composición y elección (art. 68; LOREG, art. 162)", "2 La sesión constitutiva (Reglamento del Congreso, arts. 1 a 5)"]))

T.ap("s3", "II.1 Composición y elección del Congreso (art. 68; LOREG, art. 162)", f"""
{unidad("1.1 Número de Diputados y sufragio (art. 68.1; LOREG, art. 162.1)",
  lit("CE", "Artículo 68", ["un mínimo de 300 y un máximo de 400 Diputados", "sufragio universal, libre, igual, directo y secreto"], solo=[1]),
  lit("LOREG", "acientosesentaydos", ["trescientos cincuenta Diputados"], solo=[1], titulo="Artículo 162.1 (LO 5/1985, del Régimen Electoral General)"),
  fichab("Composición numérica del Congreso",
         "La Constitución fija la horquilla; la ley electoral, el número exacto",
         "Sufragio universal, libre, igual, directo y secreto",
         "Horquilla constitucional: **300 a 400**; número legal: **350**",
         "**300-400** es la Constitución; **350** es la **LOREG**. Los cinco caracteres del sufragio: universal, libre, igual, directo y secreto."))}

{unidad("1.2 Circunscripción, reparto y proporcionalidad (art. 68.2 y 3; LOREG, art. 162.2 y 3)",
  lit("CE", "Artículo 68", ["La circunscripción electoral es la provincia", "estarán representadas cada una de ellas por un Diputado", "asignando una representación mínima inicial a cada circunscripción"], solo=[2, 3]),
  lit("LOREG", "acientosesentaydos", ["un mínimo inicial de dos Diputados", "en proporción a su población"], solo=[2, 3, 4, 5, 6], titulo="Artículo 162.2 y 3 (LO 5/1985, del Régimen Electoral General)"),
  fichab("Cómo se reparten los escaños del Congreso entre circunscripciones",
         "La ley (LOREG) distribuye; el Decreto de convocatoria especifica los Diputados de cada circunscripción (art. 162.4 LOREG)",
         ["Circunscripción: la **provincia**", "Ceuta y Melilla: **un** Diputado cada una", "Mínimo inicial de **dos** por provincia; los **248** restantes, en proporción a la población", "Elección con criterios de **representación proporcional**"],
         "—",
         "La Constitución dice «representación mínima inicial»; el **dos** lo pone la **LOREG**. Ceuta y Melilla: **un** Diputado (pero **dos** Senadores, 69.4 → III.1.4)."))}

{unidad("1.3 Duración del mandato (art. 68.4)",
  lit("CE", "Artículo 68", ["cuatro años", "o el día de la disolución de la Cámara"], solo=[4]),
  fichab("Legislatura del Congreso", "El Congreso y cada Diputado", "El mandato termina por el transcurso de los cuatro años o por la disolución", "**Cuatro años** desde la elección",
         "Dos causas de fin del mandato: **cuatro años** después de la elección o **disolución**."))}

{unidad("1.4 Electores y elegibles (art. 68.5)",
  lit("CE", "Artículo 68", ["todos los españoles que estén en pleno uso de sus derechos políticos", "fuera del territorio de España"], solo=[5, 6]),
  fichab("Sufragio activo y pasivo", c("CE", "Artículo 68", "todos los españoles que estén en pleno uso de sus derechos políticos"),
         "La ley reconoce y el Estado facilita el voto de los españoles en el extranjero", "—",
         "Electores **y** elegibles: los **españoles** en pleno uso de sus derechos políticos."))}

{unidad("1.5 Elecciones y convocatoria del Congreso electo (art. 68.6)",
  lit("CE", "Artículo 68", ["entre los treinta días y sesenta días desde la terminación del mandato", "dentro de los veinticinco días siguientes a la celebración de las elecciones"], solo=[7]),
  fichab("Plazos electorales constitucionales", "—", "—",
         ["Elecciones: entre **30 y 60 días** desde la terminación del mandato", "Convocatoria del Congreso electo: dentro de los **25 días** siguientes a las elecciones"],
         "**30-60** días para las elecciones; **25** días para convocar el Congreso electo. La sesión constitutiva se celebra el día que señale el Real Decreto de convocatoria (→ II.2.1)."))}
""", 2)

T.ap("s4", "II.2 La sesión constitutiva del Congreso (Reglamento del Congreso, arts. 1 a 5)", f"""
{unidad("2.1 Convocatoria y Mesa de edad (Reglamento del Congreso, arts. 1 y 2)",
  lit("RCD", "a1", ["en sesión constitutiva el día y hora señalados en el Real Decreto de convocatoria"]),
  lit("RCD", "art2", ["de mayor edad", "los dos más jóvenes"]),
  fichab("Sesión constitutiva del Congreso: quién la preside al principio",
         "Preside la diputada o diputado electos **de mayor edad** presente; ocupan las Secretarías los **dos más jóvenes**",
         "Se reúne el día y hora del **Real Decreto de convocatoria**", "—",
         "Mesa de edad del Congreso: **mayor edad + dos más jóvenes**. En el Senado son **cuatro** los Secretarios más jóvenes (→ III.2.1). Cayó en 2025 (→ Cierre 1)."))}

{unidad("2.2 Elección de la Mesa y juramento (Reglamento del Congreso, arts. 3 y 4)",
  lit("RCD", "art3", ["a la elección de la Mesa del Congreso"]),
  lit("RCD", "art4", ["el juramento o promesa de acatar la Constitución", "La Presidencia declarará constituido el Congreso", "al Rey o a la Reina, al Senado y al Gobierno"]),
  fichab("Desarrollo de la sesión constitutiva",
         "La Presidencia de edad; después, la Presidencia elegida",
         ["Lectura del Real Decreto de convocatoria, de la relación de electos y de los recursos contencioso-electorales", "Elección de la Mesa (art. 37 → V.2.2)", "Juramento o promesa de acatar la Constitución, por orden alfabético", "Declaración de constitución y comunicación al Rey o a la Reina, al Senado y al Gobierno"],
         "—",
         "Primero se elige la **Mesa** y después se presta el **juramento o promesa**. La constitución se comunica al **Rey**, al **Senado** y al **Gobierno**."))}

{unidad("2.3 Sesión de apertura de la legislatura (Reglamento del Congreso, art. 5)",
  lit("RCD", "art5", ["quince días"]),
  fichab("Solemne sesión de apertura", "—", "—", "Dentro de los **quince días** siguientes a la sesión constitutiva",
         "**Quince** días desde la sesión **constitutiva** (no desde las elecciones)."))}

{resumen([
  "Congreso: **300 a 400** Diputados (CE) y **350** (LOREG); sufragio universal, libre, igual, directo y secreto (68.1).",
  "Circunscripción: la **provincia**; Ceuta y Melilla, **un** Diputado; **representación proporcional**; mínimo inicial de **dos** por provincia (LOREG 162).",
  "Mandato de **cuatro años**; elecciones entre **30 y 60 días** tras el fin del mandato; Congreso convocado en **25 días** (68.4 y 6).",
  "Sesión constitutiva presidida por el electo de **mayor edad** con los **dos más jóvenes**; apertura en **15 días** (RCD 2 y 5)."],
  "Siguiente: III. ¿Cómo se compone el Senado?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Cómo se compone el Senado? (art. 69; LOREG, art. 165; Reglamento del Senado, arts. 2 a 5)", donde(
  "Tercera pregunta. El Senado es la Cámara de **representación territorial** y mezcla dos tipos de Senadores: los **elegidos** por los votantes (provincias, islas, Ceuta y Melilla) y los **designados** por las Comunidades Autónomas.",
  ["1 Composición (art. 69; LOREG, art. 165)", "2 La constitución del Senado (Reglamento del Senado, arts. 2 a 5)", "3 Cuadro comparativo de la composición de las dos Cámaras"]))

T.ap("s5", "III.1 Composición del Senado (art. 69; LOREG, art. 165)", f"""
{unidad("1.1 Cámara de representación territorial (art. 69.1)",
  lit("CE", "Artículo 69", ["Cámara de representación territorial"], solo=[1]),
  fichab("Naturaleza del Senado", "El Senado", "—", "—",
         "Es la Cámara de representación **territorial** (66.1: las Cortes, en conjunto, representan al **pueblo español**)."))}

{unidad("1.2 Senadores de las provincias (art. 69.2; LOREG, art. 165.1)",
  lit("CE", "Artículo 69", ["cuatro Senadores", "una ley orgánica"], solo=[2]),
  lit("LOREG", "acientosesentaycinco", ["cuatro Senadores"], solo=[1], titulo="Artículo 165.1 (LO 5/1985, del Régimen Electoral General)"),
  fichab("Elección directa en las provincias", "Los votantes de cada provincia",
         "Sufragio universal, libre, igual, directo y secreto", "**Cuatro** Senadores por provincia",
         "**Cuatro** por provincia (no tres). El art. 69.2 remite a una **ley orgánica** (la LOREG)."))}

{unidad("1.3 Senadores de las islas (art. 69.3; LOREG, art. 165.2)",
  lit("CE", "Artículo 69", ["cada isla con Cabildo o Consejo Insular constituirá una circunscripción", "correspondiendo tres a cada una de las islas mayores", "uno a cada una de las siguientes islas"], solo=[3]),
  lit("LOREG", "acientosesentaycinco", ["tres en Gran Canaria, Mallorca y Tenerife"], solo=[2], titulo="Artículo 165.2 (LO 5/1985, del Régimen Electoral General)"),
  fichab("Elección en las provincias insulares", "Los votantes de cada isla con Cabildo o Consejo Insular",
         ["Cada isla con Cabildo o Consejo Insular es una **circunscripción**", "Islas mayores (Gran Canaria, Mallorca y Tenerife): **tres** cada una", "Ibiza, Formentera, Menorca, Fuerteventura, La Gomera, El Hierro, Lanzarote y La Palma: **uno** cada una"],
         "—",
         "Islas **mayores** = **Gran Canaria, Mallorca y Tenerife** (Menorca no: elige **uno**). Cayó en 2025 (→ Cierre 1)."))}

{unidad("1.4 Senadores de Ceuta y Melilla (art. 69.4)",
  lit("CE", "Artículo 69", ["dos Senadores"], solo=[4]),
  fichab("Elección en Ceuta y Melilla", "Las poblaciones de Ceuta y Melilla", "—", "**Dos** Senadores cada una",
         "Ceuta y Melilla: **dos** Senadores cada una, pero **un** Diputado (68.2 → II.1.2)."))}

{unidad("1.5 Senadores designados por las Comunidades Autónomas (art. 69.5; LOREG, art. 165.4)",
  lit("CE", "Artículo 69", ["un Senador y otro más por cada millón de habitantes", "a la Asamblea legislativa o, en su defecto, al órgano colegiado superior", "la adecuada representación proporcional"], solo=[5]),
  lit("LOREG", "acientosesentaycinco", ["el censo de población de derecho vigente en el momento de celebrarse las últimas elecciones generales al Senado"], solo=[4], titulo="Artículo 165.4 (LO 5/1985, del Régimen Electoral General)"),
  fichab("Designación autonómica de Senadores",
         "La **Asamblea legislativa** de la Comunidad Autónoma (en su defecto, según la Constitución, su órgano colegiado superior)",
         "Según los **Estatutos**, que aseguran la adecuada representación proporcional",
         "**Un** Senador **y otro más por cada millón** de habitantes; población: censo de derecho vigente en las últimas elecciones generales al Senado (LOREG)",
         "Los designan las **Comunidades Autónomas** (no se eligen por sufragio directo). Fórmula: **uno + uno por cada millón**."))}

{unidad("1.6 Duración del mandato (art. 69.6)",
  lit("CE", "Artículo 69", ["cuatro años"], solo=[6]),
  fichab("Legislatura del Senado", "El Senado y cada Senador", "Termina por el transcurso de los cuatro años o por la disolución", "**Cuatro años**",
         "Misma regla que el Congreso (68.4 → II.1.3)."))}
""", 2)

T.ap("s6", "III.2 La constitución del Senado (Reglamento del Senado, arts. 2 a 5)", f"""
{unidad("2.1 Junta Preparatoria y Mesa de edad (Reglamento del Senado, arts. 2 y 3)",
  lit("RS", "a2", ["Junta Preparatoria", "El que figure primero en la lista de presentación de credenciales"]),
  lit("RS", "a3", ["el Senador de más edad de entre los presentes", "los cuatro más jóvenes"]),
  fichab("Primera reunión de los Senadores",
         ["::Junta Preparatoria:", "La abre el primero en la lista de presentación de **credenciales**", "Mesa de edad: el Senador **de más edad** y, como Secretarios, los **cuatro más jóvenes**"],
         "El Letrado Mayor lee la convocatoria y se da cuenta de las impugnaciones",
         "El día que señale el Decreto de convocatoria",
         "Senado: **cuatro** Secretarios más jóvenes; Congreso: **dos** (→ II.2.1)."))}

{unidad("2.2 Constitución definitiva o interina (Reglamento del Senado, art. 4)",
  lit("RS", "a4", ["un veinte por ciento o más de los escaños", "su constitución será interina", "sólo se ocupará del examen de las incompatibilidades"]),
  fichab("Cuándo se constituye el Senado con carácter interino", "El Senado",
         "Si las impugnaciones contra Senadores de elección directa afectan al **20 %** o más de sus escaños, la constitución es **interina**",
         "Interinidad hasta que se confirme al menos el **80 %**; iniciativa para tratar otros temas: un Grupo parlamentario o **veinticinco** Senadores",
         "El 20 % se calcula sobre los Senadores **de elección directa**. Durante la interinidad, solo **incompatibilidades** (salvo lo indispensable)."))}

{unidad("2.3 Composición de la Mesa del Senado (Reglamento del Senado, art. 5)",
  lit("RS", "a5", ["el Presidente, dos Vicepresidentes y cuatro Secretarios"]),
  fichab("Mesa del Senado", "El Pleno la elige en la sesión de constitución", "Por papeletas (art. 6 RS)", "**1 + 2 + 4 = 7** miembros",
         "Senado: **dos** Vicepresidentes; Congreso: **cuatro** Vicepresidencias (→ V.2.2)."))}
""", 2)

T.ap("s7", "III.3 Cuadro comparativo: composición del Congreso y del Senado (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| | Congreso | Senado |
|---|---|---|
| Naturaleza | Las Cortes representan al pueblo español (66.1) | Cámara de **representación territorial** (69.1) |
| Número | **300 a 400** (68.1); **350** (LOREG 162.1) | No lo fija una cifra cerrada: suma de elegidos y designados (69.2 a 5) |
| Circunscripción | La **provincia** (68.2) | Provincia; **isla** con Cabildo o Consejo Insular; Ceuta y Melilla (69.2 a 4) |
| Por provincia | Mínimo inicial de **2** + reparto por población (LOREG 162) | **4** (69.2) |
| Ceuta y Melilla | **1** cada una (68.2) | **2** cada una (69.4) |
| Criterio | **Representación proporcional** (68.3) | — |
| Designados | — | Comunidades Autónomas: **1 + 1 por cada millón** (69.5) |
| Mandato | **4 años** (68.4) | **4 años** (69.6) |
| Mesa de edad | Mayor edad + **2** más jóvenes (RCD 2) | Más edad + **4** más jóvenes (RS 3) |

{resumen([
  "Senado: Cámara de **representación territorial** (69.1).",
  "**Cuatro** Senadores por provincia; **tres** en Gran Canaria, Mallorca y Tenerife; **uno** en las demás islas citadas; **dos** en Ceuta y Melilla (69.2 a 4).",
  "Las Comunidades Autónomas designan **un** Senador **y otro más por cada millón** de habitantes, a través de su Asamblea legislativa (69.5).",
  "Junta Preparatoria y Mesa de edad con **cuatro** Secretarios; constitución **interina** si las impugnaciones afectan al **20 %** de los escaños de elección directa; Mesa de **siete** (RS 2 a 5)."],
  "Siguiente: IV. ¿Qué estatuto tienen Diputados y Senadores?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Qué estatuto tienen Diputados y Senadores? (arts. 70 y 71)", donde(
  "Cuarta pregunta. La Constitución fija quién **no puede** ser parlamentario (inelegibilidad e incompatibilidad) y qué **prerrogativas** protegen a los que lo son.",
  ["1 Inelegibilidad, incompatibilidad y control de las actas (art. 70)", "2 Inviolabilidad, inmunidad, fuero y asignación (art. 71)"]))

T.ap("s8", "IV.1 Inelegibilidad, incompatibilidad y control de las actas (art. 70)", f"""
{unidad("1.1 Causas que la ley electoral comprenderá en todo caso (art. 70.1)",
  lit("CE", "Artículo 70", ["en todo caso", "con la excepción de los miembros del Gobierno", "en activo", "Juntas Electorales"]),
  fichab("Causas mínimas de inelegibilidad e incompatibilidad",
         "Las determina **la ley electoral**; la Constitución fija un mínimo",
         ["::Comprenderán en todo caso a:", "Los componentes del Tribunal Constitucional", "Los altos cargos de la Administración del Estado que determine la ley, **salvo los miembros del Gobierno**", "El Defensor del Pueblo", "Los Magistrados, Jueces y Fiscales **en activo**", "Los militares profesionales y miembros de las Fuerzas y Cuerpos de Seguridad y Policía **en activo**", "Los miembros de las Juntas Electorales"],
         "—",
         "Los **miembros del Gobierno** están **exceptuados**: pueden ser Diputados o Senadores. Cayó en 2025 (→ Cierre 1). Jueces, Fiscales y militares: solo **en activo**."))}

{unidad("1.2 Control judicial de las actas (art. 70.2)",
  lit("CE", "Artículo 70", ["control judicial"], solo=[8]),
  fichab("Validez de actas y credenciales", "Los Tribunales, en los términos de la ley electoral", "Control **judicial**", "—",
         "La validez de las actas está sometida a control **judicial**, no a la propia Cámara ni al Tribunal Constitucional."))}
""", 2)

T.ap("s9", "IV.2 Inviolabilidad, inmunidad, fuero y asignación (art. 71)", f"""
{unidad("2.1 Inviolabilidad (art. 71.1)",
  lit("CE", "Artículo 71", ["inviolabilidad", "por las opiniones manifestadas en el ejercicio de sus funciones"], solo=[1]),
  fichab("Irresponsabilidad por las opiniones", "Diputados y Senadores", "Cubre las **opiniones** manifestadas **en el ejercicio de sus funciones**", "—",
         "Inviolabilidad = **opiniones** en el ejercicio de las funciones. No confundir con la **inmunidad** (71.2)."))}

{unidad("2.2 Inmunidad (art. 71.2)",
  lit("CE", "Artículo 71", ["Durante el período de su mandato", "en caso de flagrante delito", "sin la previa autorización de la Cámara respectiva"], solo=[2]),
  fichab("Protección frente a la detención y el proceso", "Diputados y Senadores; autoriza **la Cámara respectiva**",
         ["Detención: **solo** en caso de **flagrante delito**", "Inculpación o procesamiento: con **previa autorización** de la Cámara respectiva"],
         "Durante el **período de su mandato**",
         "La autorización la da **la Cámara respectiva** (no el Tribunal Supremo ni el Congreso para los Senadores)."))}

{unidad("2.3 Fuero: la Sala de lo Penal del Tribunal Supremo (art. 71.3)",
  lit("CE", "Artículo 71", ["la Sala de lo Penal del Tribunal Supremo"], solo=[3]),
  fichab("Órgano competente en las causas contra parlamentarios", c("CE", "Artículo 71", "la Sala de lo Penal del Tribunal Supremo"), "—", "—",
         "Sala de lo **Penal** del **Tribunal Supremo** (no la Audiencia Nacional ni los Tribunales Superiores de Justicia)."))}

{unidad("2.4 Asignación (art. 71.4)",
  lit("CE", "Artículo 71", ["fijada por las respectivas Cámaras"], solo=[4]),
  fichab("Retribución de los parlamentarios", "La fija **cada Cámara**", "—", "—",
         "La asignación la fijan **las respectivas Cámaras**, no una ley ni el Gobierno."))}

{resumen([
  "La **ley electoral** fija las causas de inelegibilidad e incompatibilidad; la Constitución incluye en todo caso al TC, altos cargos (**salvo miembros del Gobierno**), Defensor del Pueblo, jueces y fiscales **en activo**, militares y policías **en activo** y Juntas Electorales (70.1).",
  "Actas y credenciales: **control judicial** (70.2).",
  "Inviolabilidad por las **opiniones** (71.1); inmunidad: detención solo en **flagrante delito** y procesamiento con **autorización de la Cámara** (71.2); **Sala de lo Penal del TS** (71.3); asignación fijada por **cada Cámara** (71.4)."],
  "Siguiente: V. ¿Cómo se organizan y funcionan las Cámaras?")}
""", 2)

# =============================================================================
T.ap("bV", "V. ¿Cómo se organizan y funcionan las Cámaras? (arts. 72 a 80; Reglamentos del Congreso y del Senado)", donde(
  "Quinta pregunta. Las Cámaras se dan sus propias normas (**autonomía**), eligen sus órganos de gobierno y funcionan en **Pleno** y en **Comisiones**, con reglas comunes de **períodos de sesiones, quórum, mayorías y publicidad**.",
  ["1 Autonomía de las Cámaras (art. 72)", "2 Órganos de gobierno: grupos, Mesa, Presidencia y Junta de Portavoces (Reglamentos)", "3 Períodos de sesiones y sesiones conjuntas (arts. 73 y 74)", "4 Pleno, Comisiones y peticiones (arts. 75 a 77; Reglamentos)", "5 La Diputación Permanente (art. 78; Reglamentos)", "6 Quórum, mayorías y publicidad (arts. 79 y 80)"]))

T.ap("s10", "V.1 Autonomía de las Cámaras (art. 72)", f"""
{unidad("1.1 Reglamentos, presupuestos y personal (art. 72.1)",
  lit("CE", "Artículo 72", ["establecen sus propios Reglamentos", "aprueban autónomamente sus presupuestos", "de común acuerdo", "una votación final sobre su totalidad, que requerirá la mayoría absoluta"], solo=[1]),
  fichab("Autonomía normativa, presupuestaria y de personal",
         "Cada Cámara (el Estatuto del Personal, las dos **de común acuerdo**)",
         ["Reglamento propio", "Presupuesto propio, aprobado autónomamente", "Estatuto del Personal de las Cortes Generales, de común acuerdo"],
         "Reglamentos y su reforma: **votación final sobre su totalidad** por **mayoría absoluta**",
         "Mayoría **absoluta** en **votación final sobre la totalidad** (no tres quintos). Los Reglamentos no son leyes orgánicas."))}

{unidad("1.2 Presidentes, Mesas y sesiones conjuntas (art. 72.2)",
  lit("CE", "Artículo 72", ["eligen sus respectivos Presidentes y los demás miembros de sus Mesas", "presididas por el Presidente del Congreso", "por mayoría absoluta de cada Cámara"], solo=[2]),
  fichab("Autonomía orgánica",
         ["Cada Cámara elige su Presidente y su Mesa", "Sesiones conjuntas: las preside el **Presidente del Congreso**"],
         "Las sesiones conjuntas se rigen por un **Reglamento de las Cortes Generales**",
         "Reglamento de las Cortes Generales: **mayoría absoluta de cada Cámara**",
         "Sesiones conjuntas: Presidente **del Congreso**. Reglamento de cada Cámara: mayoría absoluta **de esa Cámara**; Reglamento de las Cortes: mayoría absoluta **de cada Cámara**."))}

{unidad("1.3 Poderes administrativos y de policía (art. 72.3)",
  lit("CE", "Artículo 72", ["todos los poderes administrativos y facultades de policía"], solo=[3]),
  fichab("Autoridad interna de cada Cámara", "Los **Presidentes** de las Cámaras, en nombre de ellas", "En el interior de sus respectivas sedes", "—",
         "Corresponden al **Presidente** (no a la Mesa ni al Gobierno)."))}
""", 2)

T.ap("s11", "V.2 Órganos de gobierno: grupos, Mesa, Presidencia y Junta de Portavoces (Reglamentos)", f"""
La Constitución solo prevé que cada Cámara elija su Presidente y su Mesa (art. 72.2 → V.1.2); el resto lo regulan los Reglamentos.

?> **Aviso de vigencia (art. 23.1 del Reglamento del Congreso).** El BOE recoge una nueva redacción del art. 23.1 (Reforma del Reglamento de 23 de julio de 2026, BOE-A-2026-16353) que, según la nota del propio BOE, **entra en vigor en la XVI legislatura**. Por eso aquí solo se cita lo que coincide en las dos redacciones (el mínimo de **quince** y la prohibición de grupos separados de un mismo partido), y no los porcentajes de votos.

{unidad("2.1 Grupos parlamentarios del Congreso (Reglamento del Congreso, arts. 23 a 25)",
  lit("RCD", "art24", ["dentro de los cinco días siguientes a la sesión constitutiva"], solo=[1]),
  lit("RCD", "art25", ["quedarán incorporados al Grupo Mixto", "más de un Grupo Parlamentario"]),
  fichab("Grupos parlamentarios del Congreso",
         f"Diputados {c('RCD', 'art23', 'en número no inferior a quince')} (art. 23.1)",
         ["Escrito a la **Mesa** dentro de los **cinco días** siguientes a la sesión constitutiva (art. 24.1)", "Quien no se integre en un grupo pasa al **Grupo Mixto** (art. 25.1)", "Nadie puede estar en más de un grupo (art. 25.2)"],
         "Mínimo general: **15** Diputados; plazo: **5 días**",
         f"{c('RCD', 'art23', 'En ningún caso pueden constituir grupo parlamentario separado quienes pertenezcan a un mismo partido')} (art. 23.2). Congreso **15**; Senado **10** (→ V.2.4)."))}

{unidad("2.2 La Mesa del Congreso y la elección de su Presidencia (Reglamento del Congreso, arts. 30 y 37)",
  lit("RCD", "art30", ["órgano rector de la Cámara", "cuatro Vicepresidencias y cuatro Secretarías"]),
  lit("RCD", "art37", ["la mayoría absoluta de los miembros de la Cámara", "entre quienes hayan alcanzado las dos mayores votaciones"], solo=[1, 2]),
  fichab("Órgano rector del Congreso",
         "Presidencia, **cuatro** Vicepresidencias y **cuatro** Secretarías (9 miembros)",
         ["Presidencia: un solo nombre en la papeleta; **mayoría absoluta** en primera votación; si no, segunda votación entre los **dos** más votados", "Vicepresidencias y Secretarías: un solo nombre; las **cuatro** personas más votadas"],
         "Presidencia: **mayoría absoluta** de los miembros; en segunda votación, **más votos**",
         "Mesa del Congreso: **1 + 4 + 4**. Senado: **1 + 2 + 4** (→ III.2.3). Se elige en la sesión constitutiva (→ II.2.2)."))}

{unidad("2.3 Junta de Portavoces del Congreso (Reglamento del Congreso, art. 39)",
  lit("RCD", "art39", ["Junta de Portavoces", "a petición de dos grupos parlamentarios o de la quinta parte de los miembros de la Cámara", "voto ponderado"], solo=[1, 4]),
  fichab("Órgano de los portavoces de los grupos",
         "Portavoces de los grupos; la preside y convoca el **Presidente del Congreso**",
         "Convocatoria: a iniciativa propia o a petición de **dos** grupos o de **la quinta parte** de los miembros de la Cámara",
         "Decisiones por **voto ponderado**",
         "**Voto ponderado** (cada portavoz pesa según su grupo). La Mesa decide **oída** la Junta de Portavoces en muchas materias (p. ej., art. 31.1.6.º y 40.1 RCD)."))}

{unidad("2.4 Grupos parlamentarios del Senado (Reglamento del Senado, art. 27)",
  lit("RS", "a27", ["al menos, de diez Senadores", "a un número inferior a seis", "no podrán formar más de un Grupo parlamentario"], solo=[1, 2, 3]),
  fichab("Grupos parlamentarios del Senado", "Al menos **diez** Senadores",
         ["Nadie en más de un grupo", "Los de un mismo partido, federación, coalición o agrupación no pueden formar más de un grupo", "Constitución: relación nominal en la Presidencia en **cinco días hábiles** desde la constitución del Senado (art. 28.1 RS)"],
         "Disolución si baja de **seis**, al final del período de sesiones",
         "Senado: **10** para constituir y disolución por debajo de **6**. Congreso: **15** (→ V.2.1)."))}

{unidad("2.5 La Mesa y el Presidente del Senado (Reglamento del Senado, arts. 35 y 7)",
  lit("RS", "a35", ["órgano rector del Senado", "Letrado Mayor"], solo=[1, 2]),
  lit("RS", "a7", ["mayoría absoluta de los miembros de la Cámara acreditados hasta el momento", "las dos mayores votaciones"]),
  fichab("Órgano rector del Senado",
         "La Mesa (Presidente, dos Vicepresidentes y cuatro Secretarios → III.2.3), bajo la autoridad y dirección del **Presidente**; la asiste el **Letrado Mayor**",
         "Presidente: un solo nombre por papeleta; **mayoría absoluta** de los miembros acreditados; si no, nueva votación",
         "Presidente: mayoría absoluta en la primera votación; en la segunda, **más votos**",
         "La mayoría absoluta se calcula sobre los miembros **acreditados hasta el momento** ante la Cámara."))}

{unidad("2.6 Junta de Portavoces del Senado (Reglamento del Senado, art. 43)",
  lit("RS", "a43", ["el Presidente de la Cámara, que la convoca, preside y dirige"], solo=[1]),
  fichab("Órgano de los portavoces del Senado", "El Presidente del Senado y los Portavoces de los Grupos parlamentarios",
         "La Junta es **oída** para fijar el calendario y el orden del día del Pleno, entre otras cosas (art. 44 RS)", "—",
         "En las dos Cámaras la Junta de Portavoces la **preside el Presidente** de la Cámara."))}
""", 2)

T.ap("s12", "V.3 Períodos de sesiones y sesiones conjuntas (arts. 73 y 74)", f"""
{unidad("3.1 Sesiones ordinarias y extraordinarias (art. 73)",
  lit("CE", "Artículo 73", ["dos períodos ordinarios de sesiones", "de septiembre a diciembre", "de febrero a junio", "a petición del Gobierno, de la Diputación Permanente o de la mayoría absoluta de los miembros de cualquiera de las Cámaras", "sobre un orden del día determinado"]),
  fichab("Calendario de las Cámaras",
         ["::Pueden pedir sesiones extraordinarias:", "El Gobierno", "La Diputación Permanente", "La mayoría absoluta de los miembros de cualquiera de las Cámaras"],
         "Extraordinarias: con **orden del día determinado** y se clausuran al agotarlo",
         ["Ordinarios: **septiembre a diciembre** y **febrero a junio**", "Extraordinarias: a petición de la **mayoría absoluta** de los miembros de una Cámara (o del Gobierno o la Diputación Permanente)"],
         "**Enero** y **julio-agosto** quedan fuera de los períodos ordinarios. No pueden pedirlas el Rey, el Presidente del Congreso ni una minoría de parlamentarios."))}

{unidad("3.2 Sesión conjunta (art. 74.1)",
  lit("CE", "Artículo 74", ["competencias no legislativas que el Título II atribuye expresamente"], solo=[1]),
  fichab("Cuándo se reúnen Congreso y Senado juntos", "Ambas Cámaras (presididas por el Presidente del Congreso, 72.2)",
         "Para las competencias **no legislativas** que el **Título II** (la Corona) atribuye expresamente a las Cortes Generales (tema I.4)", "—",
         "Sesión conjunta = competencias **no legislativas** del **Título II**."))}

{unidad("3.3 Decisiones por mayoría de cada Cámara y Comisión Mixta (art. 74.2)",
  lit("CE", "Artículo 74", ["los artículos 94, 1, 145, 2 y 158, 2", "por mayoría de cada una de las Cámaras", "por el Congreso", "por el Senado", "Comisión Mixta compuesta de igual número de Diputados y Senadores", "decidirá el Congreso por mayoría absoluta"], solo=[2]),
  fichab("Decisiones de las Cortes adoptadas por separado en cada Cámara",
         "Congreso y Senado; si no hay acuerdo, una **Comisión Mixta** paritaria; en último término, el **Congreso**",
         ["Tratados del art. **94.1** → empieza el **Congreso**", "Acuerdos de cooperación entre Comunidades (**145.2**) y Fondo de Compensación (**158.2**) → empieza el **Senado**"],
         ["Mayoría de cada una de las Cámaras", "Si la Comisión Mixta no logra la aprobación: **mayoría absoluta del Congreso**"],
         "Es uno de los pocos casos en que el **Senado** inicia el procedimiento (145.2 y 158.2). La última palabra es del **Congreso** por mayoría **absoluta**."))}
""", 2)

T.ap("s13", "V.4 Pleno, Comisiones y peticiones (arts. 75 a 77; Reglamentos)", f"""
{unidad("4.1 Pleno y Comisiones; delegación legislativa en Comisiones (art. 75)",
  lit("CE", "Artículo 75", ["en Pleno y por Comisiones", "Comisiones Legislativas Permanentes", "recabar en cualquier momento", "la reforma constitucional, las cuestiones internacionales, las leyes orgánicas y de bases y los Presupuestos Generales del Estado"]),
  fichab("Competencia legislativa plena de las Comisiones",
         "Las Cámaras delegan en las **Comisiones Legislativas Permanentes**; el Pleno puede recabar",
         ["La Comisión aprueba el proyecto o la proposición de ley", "El **Pleno** puede **recabar en cualquier momento** el debate y votación"],
         "—",
         ["::No se puede delegar (75.3):", "Reforma constitucional", "Cuestiones internacionales", "Leyes **orgánicas** y **de bases**", "Presupuestos Generales del Estado"]))}

{unidad("4.2 Comisiones según los Reglamentos (Reglamento del Congreso, art. 46.2 y 3; Reglamento del Senado, art. 49)",
  lit("RCD", "art46", ["Reglamento", "Estatuto", "Peticiones", "dentro de los diez días siguientes a la sesión constitutiva"], solo=[25, 26, 27, 28, 29]),
  lit("RS", "a49", ["Permanentes y de Investigación o Especiales", "la Comisión General de las Comunidades Autónomas, la Comisión General de las Entidades Locales"], solo=[1, 2, 12]),
  fichab("Clases de Comisiones",
         "Las forman los miembros que designen los grupos, en proporción a su importancia numérica (art. 40.1 RCD; art. 51.1 RS)",
         ["Congreso: Comisiones Permanentes Legislativas (lista del art. 46.1) y otras Comisiones Permanentes (art. 46.2), entre ellas **Reglamento, Estatuto y Peticiones**; se constituyen en **diez días** desde la sesión constitutiva", "Senado: Permanentes (Legislativas y no Legislativas) y de Investigación o Especiales; son Legislativas la **Comisión General de las Comunidades Autónomas**, la **Comisión General de las Entidades Locales** y las que apruebe el Pleno"],
         "Senado: el acuerdo del Pleno sobre las Comisiones Legislativas requiere **mayoría absoluta**",
         "La **Comisión General de las Comunidades Autónomas** es propia del **Senado** (Cámara territorial)."))}

{unidad("4.3 Comisiones de investigación y obligación de comparecer (art. 76)",
  lit("CE", "Artículo 76", ["sobre cualquier asunto de interés público", "no serán vinculantes para los Tribunales", "comunicado al Ministerio Fiscal", "Será obligatorio comparecer"]),
  fichab("Comisiones de investigación",
         c("CE", "Artículo 76", "El Congreso y el Senado, y, en su caso, ambas Cámaras conjuntamente"),
         ["Sobre **cualquier asunto de interés público**", "Conclusiones **no vinculantes** para los Tribunales; el resultado puede comunicarse al **Ministerio Fiscal**", "Comparecer es **obligatorio**; la ley regula las sanciones"],
         "—",
         "Las conclusiones **no vinculan** a los Tribunales ni afectan a las resoluciones judiciales. Pueden ser de **una** Cámara o **conjuntas**."))}

{unidad("4.4 Peticiones a las Cámaras (art. 77)",
  lit("CE", "Artículo 77", ["siempre por escrito", "prohibida la presentación directa por manifestaciones ciudadanas", "El Gobierno está obligado a explicarse sobre su contenido"]),
  fichab("Derecho de petición ante las Cámaras", "Peticiones individuales y colectivas; las Cámaras pueden remitirlas al Gobierno",
         "**Siempre por escrito**; nunca por presentación directa en manifestaciones", "—",
         "El Gobierno debe explicarse **siempre que las Cámaras lo exijan**."))}
""", 2)

T.ap("s14", "V.5 La Diputación Permanente (art. 78; Reglamentos)", f"""
{unidad("5.1 Composición y funciones (art. 78)",
  lit("CE", "Artículo 78", ["un mínimo de veintiún miembros", "presididas por el Presidente de la Cámara respectiva", "de acuerdo con los artículos 86 y 116", "velar por los poderes de las Cámaras cuando éstas no estén reunidas", "hasta la constitución de las nuevas Cortes Generales"]),
  fichab("Órgano que asegura la continuidad de cada Cámara",
         "Una en **cada** Cámara; preside el **Presidente de la Cámara**; mínimo de **21** miembros que representan a los grupos en proporción a su importancia numérica",
         ["Pedir sesiones extraordinarias (art. 73 → V.3.1)", "Asumir las facultades de los arts. **86** (decretos-leyes) y **116** (estados excepcionales) si las Cámaras están disueltas o expiró su mandato", "Velar por los poderes de las Cámaras cuando no estén reunidas"],
         "Sigue en funciones hasta la constitución de las nuevas Cortes; después **da cuenta** a la Cámara",
         "**Veintiún** miembros **como mínimo**. Hay **dos** Diputaciones Permanentes, una por Cámara."))}

{unidad("5.2 La Diputación Permanente del Congreso (Reglamento del Congreso, art. 57)",
  lit("RCD", "art57", ["Decretos-leyes", "estados de alarma, excepción y sitio", "artículo 73, 2"]),
  fichab("Funciones de la Diputación Permanente del Congreso", "La Diputación Permanente del Congreso",
         ["Velar por los poderes de la Cámara cuando no esté reunida", "Disolución o expiración del mandato: facultades del art. 86 (decretos-leyes) y competencias del art. 116 (alarma, excepción y sitio)", "Entre períodos de sesiones: pedir sesiones extraordinarias (art. 73.2)"],
         "—",
         "La convalidación de decretos-leyes con la Cámara disuelta corresponde a la Diputación Permanente **del Congreso** (tema IV.2)."))}

{unidad("5.3 La Diputación Permanente del Senado (Reglamento del Senado, arts. 45.1 y 48.2)",
  lit("RS", "a45", ["un mínimo de veintiún miembros"], solo=[1]),
  lit("RS", "a48", ["tramitar como proyectos de ley decretos convalidados por el Congreso de los Diputados", "Velar por los poderes de la Cámara cuando no esté reunida"], solo=[5, 6, 7, 8]),
  fichab("Funciones de la Diputación Permanente del Senado", "Presidida por el Presidente del Senado; mínimo de **21** miembros",
         ["Acordar sesiones extraordinarias", "Con las Cortes disueltas: tramitar como proyectos de ley los decretos convalidados por el Congreso, si este lo acordó (art. 86.3 CE)", "Velar por los poderes de la Cámara"],
         "—",
         "Se constituye **tan pronto como** se constituye definitivamente la Cámara (art. 45.1 RS)."))}
""", 2)

T.ap("s15", "V.6 Quórum, mayorías y publicidad (arts. 79 y 80)", f"""
{unidad("6.1 Quórum, mayoría y voto personal (art. 79)",
  lit("CE", "Artículo 79", ["con asistencia de la mayoría de sus miembros", "por la mayoría de los miembros presentes", "personal e indelegable"]),
  fichab("Reglas para adoptar acuerdos",
         "Las Cámaras, reunidas reglamentariamente",
         "Voto **personal e indelegable**",
         ["Quórum: asistencia de la **mayoría de sus miembros**", "Acuerdo: **mayoría de los miembros presentes**", "Salvo mayorías especiales de la Constitución, de las leyes orgánicas y de los Reglamentos (para elección de personas)"],
         "Quórum = mayoría de los **miembros**; acuerdo = mayoría de los **presentes**. Las mayorías especiales para **elegir personas** pueden ponerlas los **Reglamentos**."))}

{unidad("6.2 Publicidad de las sesiones plenarias (art. 80)",
  lit("CE", "Artículo 80", ["serán públicas", "por mayoría absoluta o con arreglo al Reglamento"]),
  fichab("Publicidad del Pleno", "Cada Cámara", "Sesiones plenarias públicas salvo acuerdo en contrario", "Acuerdo en contrario: **mayoría absoluta** o con arreglo al Reglamento",
         "La regla de publicidad del art. 80 es de las sesiones **plenarias**."))}

{resumen([
  "Autonomía: **Reglamentos** propios aprobados por **mayoría absoluta** en votación final sobre la totalidad; sesiones conjuntas presididas por el **Presidente del Congreso** (72).",
  "Órganos: grupos (**15** Diputados; **10** Senadores), **Mesa** (Congreso 1+4+4; Senado 1+2+4), **Junta de Portavoces** (Congreso: **voto ponderado**) (Reglamentos).",
  "Períodos: **septiembre-diciembre** y **febrero-junio**; extraordinarias a petición del Gobierno, la Diputación Permanente o la **mayoría absoluta** de una Cámara (73).",
  "Art. 74.2: tratados del 94.1 (empieza el **Congreso**), 145.2 y 158.2 (empieza el **Senado**); Comisión Mixta; decide el **Congreso por mayoría absoluta**.",
  "No se delega en Comisiones: reforma constitucional, cuestiones internacionales, leyes orgánicas y de bases, Presupuestos (75.3).",
  "Diputación Permanente: **21** como mínimo, preside el Presidente de la Cámara (78). Quórum: mayoría de los **miembros**; acuerdos: mayoría de los **presentes**; voto **personal e indelegable** (79)."],
  "Siguiente: VI. ¿Qué atribuciones tienen?")}
""", 2)

# =============================================================================
T.ap("bVI", "VI. ¿Qué atribuciones tienen? (art. 66.2; arts. 87 a 90 y 92 a 94)", donde(
  "Sexta pregunta. El art. 66.2 resume las funciones de las Cortes: **legislar, aprobar los Presupuestos y controlar al Gobierno**. Aquí se ve cómo intervienen Congreso y Senado en la ley (iniciativa y tramitación), en el referéndum y en los tratados, y un cuadro de lo que la Constitución atribuye a cada Cámara.",
  ["1 Las funciones de las Cortes (art. 66.2)", "2 La iniciativa legislativa (arts. 87 a 89)", "3 Congreso y Senado en la tramitación de la ley (art. 90)", "4 Referéndum consultivo y tratados internacionales (arts. 92 a 94)", "5 Cuadro de atribuciones de cada Cámara"]))

T.ap("s16", "VI.1 Las funciones de las Cortes (art. 66.2)", f"""
{unidad("1.1 Legislar, aprobar los Presupuestos y controlar al Gobierno (art. 66.2)",
  lit("CE", "Artículo 66", ["ejercen la potestad legislativa del Estado", "aprueban sus Presupuestos", "controlan la acción del Gobierno", "las demás competencias que les atribuya la Constitución"], solo=[2]),
  fichab("Las funciones de las Cortes Generales", "Las Cortes Generales (Congreso y Senado)",
         ["Potestad **legislativa** del Estado (→ VI.2 y → VI.3; tipos de leyes: tema IV.2)", "Aprobación de los **Presupuestos** (art. 134; bloque VI del programa)", "**Control** de la acción del Gobierno (arts. 108 a 116; tema I.6)", "Las demás que les atribuya la Constitución (→ VI.5)"],
         "—",
         "Son **cuatro** incisos: legislar, aprobar los Presupuestos, controlar al Gobierno y **las demás** competencias constitucionales."))}
""", 2)

T.ap("s17", "VI.2 La iniciativa legislativa (arts. 87 a 89)", f"""
{unidad("2.1 Quién tiene la iniciativa (art. 87)",
  lit("CE", "Artículo 87", ["al Gobierno, al Congreso y al Senado", "solicitar del Gobierno la adopción de un proyecto de ley o remitir a la Mesa del Congreso una proposición de ley", "un máximo de tres miembros", "no menos de 500.000 firmas acreditadas", "materias propias de ley orgánica, tributarias o de carácter internacional, ni en lo relativo a la prerrogativa de gracia"]),
  fichab("Titulares de la iniciativa legislativa",
         ["::Iniciativa:", "**Gobierno**, **Congreso** y **Senado** (87.1)", "**Asambleas de las Comunidades Autónomas**: piden al Gobierno un proyecto o remiten a la **Mesa del Congreso** una proposición (87.2)", "**Iniciativa popular**: regulada por ley orgánica (87.3)"],
         "Las Asambleas autonómicas delegan ante el Congreso **un máximo de tres** miembros para defender la proposición",
         "Iniciativa popular: **no menos de 500.000 firmas** acreditadas",
         ["::Iniciativa popular excluida en:", "Materias propias de **ley orgánica**", "Materias **tributarias**", "Materias de carácter **internacional**", "La **prerrogativa de gracia**"]))}

{unidad("2.2 Proyectos de ley (art. 88)",
  lit("CE", "Artículo 88", ["aprobados en Consejo de Ministros", "que los someterá al Congreso", "exposición de motivos y de los antecedentes necesarios"]),
  fichab("Iniciativa del Gobierno", "El **Consejo de Ministros** los aprueba y los somete al **Congreso**",
         "Con **exposición de motivos** y **antecedentes** necesarios", "—",
         "Proyecto = iniciativa del **Gobierno**; proposición = de las Cámaras, Asambleas autonómicas o iniciativa popular. Los proyectos van **al Congreso**."))}

{unidad("2.3 Proposiciones de ley (art. 89)",
  lit("CE", "Artículo 89", ["la prioridad debida a los proyectos de ley", "se remitirán al Congreso para su trámite en éste como tal proposición"]),
  fichab("Tramitación de las proposiciones de ley", "Las Cámaras, según sus Reglamentos",
         ["Los proyectos tienen **prioridad**, pero sin impedir la iniciativa del art. 87", "Las tomadas en consideración por el **Senado** se remiten al **Congreso**"], "—",
         "La tramitación legislativa empieza **siempre en el Congreso**: incluso las proposiciones tomadas en consideración por el Senado se remiten al Congreso."))}
""", 2)

T.ap("s18", "VI.3 Congreso y Senado en la tramitación de la ley (art. 90)", f"""
La mayoría de la ley orgánica (art. 81), el decreto-ley (art. 86) y la sanción del Rey en quince días (art. 91) se estudian en el tema IV.2.

{unidad("3.1 El Senado: veto o enmiendas en dos meses (art. 90.1 y 2)",
  lit("CE", "Artículo 90", ["dará inmediata cuenta del mismo al Presidente del Senado", "en el plazo de dos meses, a partir del día de la recepción del texto", "mediante mensaje motivado", "El veto deberá ser aprobado por mayoría absoluta", "ratifique por mayoría absoluta, en caso de veto, el texto inicial, o por mayoría simple, una vez transcurridos dos meses desde la interposición del mismo", "aceptándolas o no por mayoría simple"], solo=[1, 2]),
  fichab("Papel del Senado y última palabra del Congreso",
         "El Presidente del Congreso da cuenta al Presidente del Senado; el Senado delibera; el Congreso decide",
         ["Senado: **veto** (mayoría **absoluta**) o **enmiendas**, mediante **mensaje motivado**", "Congreso ante el veto: ratifica el texto inicial por **mayoría absoluta** o, pasados **dos meses** desde la interposición, por **mayoría simple**", "Congreso ante las enmiendas: las acepta o no por **mayoría simple**"],
         ["Senado: **dos meses** desde la **recepción** del texto", "Veto: **mayoría absoluta** del Senado"],
         "El veto se **levanta** en el Congreso: inmediatamente por **mayoría absoluta**, o por **mayoría simple** tras **dos meses**. Las enmiendas se aceptan o rechazan por **mayoría simple**."))}

{unidad("3.2 Proyectos urgentes: veinte días naturales (art. 90.3)",
  lit("CE", "Artículo 90", ["veinte días naturales", "declarados urgentes por el Gobierno o por el Congreso de los Diputados"], solo=[3]),
  fichab("Reducción del plazo del Senado", "Declaran la urgencia el **Gobierno** o el **Congreso**", "—",
         "De **dos meses** a **veinte días naturales**",
         "**Veinte días naturales** (no hábiles). La urgencia la declaran el **Gobierno** o el **Congreso** (no el Senado). Cayó en 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s19", "VI.4 Referéndum consultivo y tratados internacionales (arts. 92 a 94)", f"""
{unidad("4.1 Autorización del referéndum consultivo (art. 92.1 y 2)",
  lit("CE", "Artículo 92", ["decisiones políticas de especial trascendencia", "mediante propuesta del Presidente del Gobierno, previamente autorizada por el Congreso de los Diputados"], solo=[1, 2]),
  fichab("Intervención de las Cortes en el referéndum consultivo",
         "Convoca el **Rey**, a propuesta del **Presidente del Gobierno**, previamente autorizada por el **Congreso**",
         "Referéndum **consultivo** de todos los ciudadanos sobre decisiones políticas de especial trascendencia",
         "—",
         "La autorización es del **Congreso** (no de las Cortes en sesión conjunta ni del Senado)."))}

{unidad("4.2 Tratados de atribución de competencias (art. 93)",
  lit("CE", "Artículo 93", ["Mediante ley orgánica", "Corresponde a las Cortes Generales o al Gobierno, según los casos"]),
  fichab("Autorización de tratados que atribuyen competencias constitucionales",
         "Las Cortes, mediante **ley orgánica**; garantía de cumplimiento: Cortes o Gobierno, según los casos",
         "Atribución a una organización o institución internacional del ejercicio de competencias derivadas de la Constitución",
         "Ley orgánica (mayoría absoluta del Congreso en votación final: tema IV.2)",
         "Art. 93: **ley orgánica**. Art. 94.1: **autorización** de las Cortes (→ VI.4.3)."))}

{unidad("4.3 Tratados que requieren autorización previa de las Cortes (art. 94)",
  lit("CE", "Artículo 94", ["requerirá la previa autorización de las Cortes Generales", "Tratados de carácter político", "carácter militar", "integridad territorial del Estado", "obligaciones financieras para la Hacienda Pública", "modificación o derogación de alguna ley", "serán inmediatamente informados"]),
  fichab("Autorización de las Cortes para obligarse por tratados",
         "Las **Cortes Generales** (autorización previa); para los demás tratados, Congreso y Senado son **informados**",
         ["::Requieren autorización previa (94.1):", "Políticos", "Militares", "Que afecten a la integridad territorial o a los derechos y deberes fundamentales del Título I", "Que impliquen obligaciones financieras para la Hacienda Pública", "Que modifiquen o deroguen una ley o exijan medidas legislativas"],
         "Por mayoría de cada Cámara, empezando por el **Congreso** (art. 74.2 → V.3.3)",
         "Los tratados **no** incluidos en el 94.1 solo exigen **informar inmediatamente** a las Cámaras (94.2)."))}
""", 2)

T.ap("s20", "VI.5 Cuadro de atribuciones de cada Cámara (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal. Los procedimientos se estudian en el tema que se indica.*

| Quién | Atribución | Texto de la Constitución |
|---|---|---|
| **Congreso** | Responsabilidad política del Gobierno (art. 108; tema I.6) | {c('CE', 'Artículo 108', 'El Gobierno responde solidariamente en su gestión política ante el Congreso de los Diputados')} |
| **Congreso** | Investidura (art. 99.3; tema I.6) | {c('CE', 'Artículo 99', 'Si el Congreso de los Diputados, por el voto de la mayoría absoluta de sus miembros, otorgare su confianza')} |
| **Congreso** | Cuestión de confianza (art. 112; tema I.6) | {c('CE', 'Artículo 112', 'la mayoría simple de los Diputados')} |
| **Congreso** | Moción de censura (art. 113.1; tema I.6) | {c('CE', 'Artículo 113', 'mediante la adopción por mayoría absoluta de la moción de censura')} |
| **Congreso** | Convalidación o derogación de decretos-leyes (art. 86.2; tema IV.2) | {c('CE', 'Artículo 86', 'El Congreso habrá de pronunciarse expresamente dentro de dicho plazo sobre su convalidación o derogación')} |
| **Congreso** | Autorizar el referéndum consultivo (art. 92.2 → VI.4.1) | {c('CE', 'Artículo 92', 'previamente autorizada por el Congreso de los Diputados')} |
| **Congreso** | Estados de alarma (prórroga), excepción y sitio (art. 116; temas I.2 y I.6) | {c('CE', 'Artículo 116', 'sin cuya autorización no podrá ser prorrogado dicho plazo')}; {c('CE', 'Artículo 116', 'previa autorización del Congreso de los Diputados')}; {c('CE', 'Artículo 116', 'El estado de sitio será declarado por la mayoría absoluta del Congreso de los Diputados')} |
| **Congreso** | Recibir los Presupuestos (art. 134.3) | {c('CE', 'Artículo 134', 'El Gobierno deberá presentar ante el Congreso de los Diputados los Presupuestos Generales del Estado')} |
| **Senado** | Aprobar las medidas del art. 155 (organización territorial: temas I.10 y I.11) | {c('CE', 'Artículo 155', 'con la aprobación por mayoría absoluta del Senado')} |
| **Senado** | Iniciar el procedimiento de los arts. 145.2 y 158.2 (→ V.3.3) | {c('CE', 'Artículo 74', 'y en los otros dos, por el Senado')} |
| **Las dos Cámaras** | Proponer Magistrados del Tribunal Constitucional (art. 159.1; tema I.3) | {c('CE', 'Artículo 159', 'cuatro a propuesta del Congreso por mayoría de tres quintos de sus miembros; cuatro a propuesta del Senado, con idéntica mayoría')} |
| **Las dos Cámaras** | Proponer Vocales del CGPJ (art. 122.3; tema I.7) | {c('CE', 'Artículo 122', 'cuatro a propuesta del Congreso de los Diputados, y cuatro a propuesta del Senado, elegidos en ambos casos por mayoría de tres quintos de sus miembros')} |
| **Las dos Cámaras** | Pedir información y ayuda al Gobierno; interpelaciones y preguntas (arts. 109 y 111; tema I.6) | {c('CE', 'Artículo 109', 'Las Cámaras y sus Comisiones podrán recabar')}; {c('CE', 'Artículo 111', 'están sometidos a las interpelaciones y preguntas que se le formulen en las Cámaras')} |
| **Cortes Generales** | Examen, enmienda y aprobación de los Presupuestos (art. 134.1) | {c('CE', 'Artículo 134', 'a las Cortes Generales, su examen, enmienda y aprobación')} |
| **Cortes Generales** | Defensor del Pueblo (art. 54; tema I.2) | {c('CE', 'Artículo 54', 'alto comisionado de las Cortes Generales')} |
| **Cortes Generales** | Tribunal de Cuentas (art. 136.1) | {c('CE', 'Artículo 136', 'Dependerá directamente de las Cortes Generales')} |
| **Cortes Generales** | Reforma constitucional (art. 167.1; tema I.1) | {c('CE', 'Artículo 167', 'mayoría de tres quintos de cada una de las Cámaras')} |

!> **Predominio del Congreso:** la Constitución le da en exclusiva la relación de confianza con el Gobierno (investidura, cuestión de confianza, moción de censura), la convalidación de los decretos-leyes, la autorización del referéndum y de los estados de excepción y sitio, y la **última palabra** en la ley (art. 90.2 → VI.3.1) y en el art. 74.2 (→ V.3.3). La atribución propia del Senado más preguntada es el **art. 155** (mayoría absoluta).

{resumen([
  "Las Cortes **legislan**, **aprueban los Presupuestos**, **controlan al Gobierno** y tienen las demás competencias constitucionales (66.2).",
  "Iniciativa: **Gobierno, Congreso y Senado**; las **Asambleas autonómicas** (Gobierno o Mesa del **Congreso**, hasta **tres** miembros); iniciativa **popular** con **500.000** firmas y materias excluidas (87).",
  "Senado: **dos meses** (veinte días naturales si es urgente) para **vetar** (mayoría absoluta) o **enmendar**; el Congreso levanta el veto por mayoría **absoluta** o **simple** pasados dos meses (90).",
  "Referéndum consultivo autorizado por el **Congreso** (92.2); tratados del 93 por **ley orgánica**; los del 94.1, con **autorización previa** de las Cortes."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_X12 = examen("X", 12, {
  "a": f"Sí es causa: el art. 70.1 a) comprende {c('CE', 'Artículo 70', 'A los componentes del Tribunal Constitucional')}.",
  "b": f"Sí es causa: el art. 70.1 d) comprende {c('CE', 'Artículo 70', 'A los Magistrados, Jueces y Fiscales en activo')}.",
  "c": f"Sí es causa: el art. 70.1 f) comprende {c('CE', 'Artículo 70', 'A los miembros de las Juntas Electorales')}.",
  "d": f"Correcta: el art. 70.1 b) incluye a los altos cargos de la Administración del Estado {c('CE', 'Artículo 70', 'con la excepción de los miembros del Gobierno')}."},
  [("miembro del Gobierno", "CE", "Artículo 70", "A los altos cargos de la Administración del Estado que determine la ley, con la excepción de los miembros del Gobierno")])
EX_X13 = examen("X", 13, {
  "a": f"El Presidente saliente no preside: la sesión la preside {c('RCD', 'art2', 'la diputada o diputado electos de mayor edad presente en la Cámara')}.",
  "b": f"Correcta: art. 2 RCD, {c('RCD', 'art2', 'presidida inicialmente por la diputada o diputado electos de mayor edad presente en la Cámara, con la asistencia de los dos más jóvenes, que ocuparán las Secretarías')}. El texto vigente (reforma de 2025) usa lenguaje inclusivo; el contenido es el mismo.",
  "c": f"Invierte los criterios: preside el de **mayor edad** y asisten {c('RCD', 'art2', 'los dos más jóvenes')}.",
  "d": f"El criterio es la **edad**, no la antigüedad en la Cámara, y son **dos** los que ocupan las Secretarías: {c('RCD', 'art2', 'con la asistencia de los dos más jóvenes')}."},
  [("electo de mayor edad", "RCD", "art2", "presidida inicialmente por la diputada o diputado electos de mayor edad presente en la Cámara"),
   ("dos más jóvenes", "RCD", "art2", "con la asistencia de los dos más jóvenes, que ocuparán las Secretarías")])
EX_X14 = examen("X", 14, {
  "a": f"Falta **Tenerife**, que también es isla mayor: {c('CE', 'Artículo 69', 'correspondiendo tres a cada una de las islas mayores')} (Gran Canaria, Mallorca y Tenerife).",
  "b": f"**Menorca** elige uno: {c('CE', 'Artículo 69', 'uno a cada una de las siguientes islas: Ibiza, Formentera, Menorca')}; y falta Tenerife.",
  "c": f"Sobra **Menorca**, que elige uno: {c('CE', 'Artículo 69', 'uno a cada una de las siguientes islas: Ibiza, Formentera, Menorca')}.",
  "d": f"Correcta: art. 69.3, {c('CE', 'Artículo 69', 'correspondiendo tres a cada una de las islas mayores')} —Gran Canaria, Mallorca y Tenerife—; igual en la LOREG: {c('LOREG', 'acientosesentaycinco', 'tres en Gran Canaria, Mallorca y Tenerife')}."},
  [("Gran Canaria, Mallorca y Tenerife", "CE", "Artículo 69", "correspondiendo tres a cada una de las islas mayores −Gran Canaria, Mallorca y Tenerife−")])
EX_L7 = examen("L", 7, {
  "a": f"Correcta: art. 75.3, quedan exceptuadas de la delegación en Comisiones {c('CE', 'Artículo 75', 'las leyes orgánicas y de bases')}.",
  "b": "Una ley ordinaria sectorial no está en la lista de excepciones del art. 75.3: puede delegarse.",
  "c": f"El art. 75.2 permite delegar {c('CE', 'Artículo 75', 'la aprobación de proyectos o proposiciones de ley')}: una proposición ordinaria puede delegarse.",
  "d": f"Es justo lo que permite el art. 75.2: {c('CE', 'Artículo 75', 'El Pleno podrá, no obstante, recabar en cualquier momento el debate y votación')}."},
  [("ley orgánica", "CE", "Artículo 75", "las leyes orgánicas y de bases")])
EX_P45 = examen("P", 45, {
  "a": f"No es exclusiva de las Cámaras: {c('CE', 'Artículo 87', 'La iniciativa legislativa corresponde al Gobierno, al Congreso y al Senado')} (y también a las Asambleas autonómicas y a la iniciativa popular).",
  "b": f"Correcta: art. 87.2, las Asambleas podrán {c('CE', 'Artículo 87', 'remitir a la Mesa del Congreso una proposición de ley')}.",
  "c": f"Es al revés: {c('CE', 'Artículo 87', 'En todo caso se exigirán no menos de 500.000 firmas acreditadas')}.",
  "d": f"Está excluida: {c('CE', 'Artículo 87', 'No procederá dicha iniciativa en materias propias de ley orgánica, tributarias')}…"},
  [("remitir a la Mesa del Congreso una proposición de ley", "CE", "Artículo 87", "remitir a la Mesa del Congreso una proposición de ley")])
EX_P48 = examen("P", 48, {
  "a": f"Las Asambleas no presentan **proyectos** (son del Gobierno, art. 88) ni van al Senado con cinco miembros: delegan {c('CE', 'Artículo 87', 'un máximo de tres miembros de la Asamblea')}.",
  "b": f"Correcta: literal del art. 87.2, {c('CE', 'Artículo 87', 'solicitar del Gobierno la adopción de un proyecto de ley o remitir a la Mesa del Congreso una proposición de ley, delegando ante dicha Cámara un máximo de tres miembros de la Asamblea encargados de su defensa')}.",
  "c": f"Cambia la Cámara (Senado) y el número (cinco): es la {c('CE', 'Artículo 87', 'Mesa del Congreso')} y {c('CE', 'Artículo 87', 'un máximo de tres miembros')}.",
  "d": f"Cambia solo la Cámara: la proposición se remite a la {c('CE', 'Artículo 87', 'Mesa del Congreso')}, no a la del Senado."},
  [("remitir a la Mesa del Congreso una proposición de ley", "CE", "Artículo 87", "remitir a la Mesa del Congreso una proposición de ley"),
   ("un máximo de tres miembros de la Asamblea", "CE", "Artículo 87", "delegando ante dicha Cámara un máximo de tres miembros de la Asamblea encargados de su defensa")])
EX_P46 = examen("P", 46, {
  "a": f"Dos meses es el plazo **ordinario**: {c('CE', 'Artículo 90', 'El Senado en el plazo de dos meses, a partir del día de la recepción del texto')}.",
  "b": "Un mes no aparece en el art. 90: el plazo es de dos meses o, si hay urgencia, de veinte días naturales.",
  "c": f"Correcta: art. 90.3, el plazo {c('CE', 'Artículo 90', 'se reducirá al de veinte días naturales en los proyectos declarados urgentes por el Gobierno o por el Congreso de los Diputados')}.",
  "d": "Diez días no aparece en el art. 90: la reducción es a veinte días naturales."},
  [("veinte días", "CE", "Artículo 90", "se reducirá al de veinte días naturales en los proyectos declarados urgentes por el Gobierno o por el Congreso de los Diputados")])

T.ap("s21", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **siete** preguntas de este tema: tres en el extraordinario (arts. 69.3 y 70.1 y Reglamento del Congreso, art. 2), una en el turno libre (art. 75.3) y tres en promoción interna (arts. 87 y 90.3). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-L 2025 extraordinario, pregunta 12 · Inelegibilidad e incompatibilidad (→ IV.1.1)", EX_X12,
  "### GACE-L 2025 extraordinario, pregunta 13 · Sesión constitutiva del Congreso (→ II.2.1)", EX_X13,
  "### GACE-L 2025 extraordinario, pregunta 14 · Senadores de las islas (→ III.1.3)", EX_X14,
  "### GACE-L 2025, pregunta 7 · Delegación en Comisiones (→ V.4.1)", EX_L7,
  "### GACE-P 2025, pregunta 45 · Iniciativa legislativa (→ VI.2.1)", EX_P45,
  "### GACE-P 2025, pregunta 48 · Iniciativa de las Asambleas autonómicas (→ VI.2.1)", EX_P48,
  "### GACE-P 2025, pregunta 46 · Proyectos urgentes en el Senado (→ VI.3.2)", EX_P46,
  "### Cómo se pregunta",
  "!> Los distractores cambian **un dato del artículo**: la Cámara (Congreso/Senado), un número (tres/cinco miembros; dos/cuatro Secretarios; dos meses/veinte días), una isla (Menorca/Tenerife) o la excepción de la lista (los **miembros del Gobierno** del art. 70.1 b). Memoriza las cifras y las excepciones.",
]))

T.ap("s22", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Las Cortes Generales | Representan al pueblo español; Congreso y Senado; inviolables (66); sin doble Cámara ni mandato imperativo (67) | No acumular el acta autonómica con la de **Diputado** |
| II. Congreso | 300-400 (CE) y 350 (LOREG); provincia; proporcional; 4 años; 30-60 días; 25 días (68); sesión constitutiva (RCD 1-5) | Mesa de edad: **mayor edad + dos más jóvenes** |
| III. Senado | Representación territorial; 4 por provincia; 3/1 en islas; 2 Ceuta y Melilla; CC. AA.: 1 + 1 por millón (69); Junta Preparatoria (RS 2-5) | Islas mayores: **Gran Canaria, Mallorca y Tenerife** |
| IV. Estatuto | Inelegibilidades mínimas (70.1); control judicial de actas (70.2); inviolabilidad, inmunidad, Sala de lo Penal del TS, asignación (71) | **Miembros del Gobierno**: exceptuados |
| V. Organización y funcionamiento | Reglamentos por mayoría absoluta (72); grupos, Mesa, Junta de Portavoces; períodos (73); 74.2; Comisiones (75-77); Diputación Permanente (78); 79 y 80 | No delegables en Comisiones (75.3); 21 miembros (78); quórum y mayoría (79) |
| VI. Atribuciones | Legislar, Presupuestos, control (66.2); iniciativa (87-89); veto y enmiendas del Senado (90); referéndum y tratados (92-94) | Asambleas autonómicas → **Mesa del Congreso**, **tres** miembros; urgencia: **veinte días naturales** |

?> **Trampas frecuentes:** «las Asambleas autonómicas remiten a la Mesa del **Senado**» (es la del **Congreso**); «el Senado dispone de **un mes** en los proyectos urgentes» (son **veinte días naturales**); «la sesión conjunta la preside el Presidente **del Senado**» (del **Congreso**); «los Reglamentos de las Cámaras se aprueban por **tres quintos**» (por **mayoría absoluta**); «la Diputación Permanente tiene **veinte** miembros» (mínimo **veintiuno**); «los miembros del Gobierno son inelegibles» (están **exceptuados**); «Menorca elige **tres** Senadores» (elige **uno**); «la inmunidad permite procesar sin autorización» (hace falta la **previa autorización de la Cámara respectiva**).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
Q = T.q
Q("CE", "Artículo 66", "Cortes Generales", "Según el artículo 66.1 de la Constitución, las Cortes Generales:",
  ["Representan al pueblo español y están formadas por el Congreso de los Diputados y el Senado.", "Representan a las Comunidades Autónomas y están formadas por el Congreso y el Senado.", "Representan al pueblo español y están formadas por el Congreso, el Senado y el Gobierno.", "Son la Cámara de representación territorial."],
  "Art. 66.1 CE. La representación territorial es la del Senado (art. 69.1).", "Las Cortes Generales representan al pueblo español y están formadas por el Congreso de los Diputados y el Senado")
Q("CE", "Artículo 66", "Cortes Generales", "Según el artículo 66.2 de la Constitución, las Cortes Generales:",
  ["Ejercen la potestad legislativa del Estado, aprueban sus Presupuestos y controlan la acción del Gobierno.", "Ejercen la potestad legislativa del Estado y elaboran sus Presupuestos.", "Ejercen la potestad legislativa y reglamentaria del Estado.", "Dirigen la política interior y exterior y controlan la acción del Gobierno."],
  "Art. 66.2 CE. La elaboración de los Presupuestos corresponde al Gobierno (art. 134.1).", "ejercen la potestad legislativa del Estado, aprueban sus Presupuestos, controlan la acción del Gobierno")
Q("CE", "Artículo 67", "Cortes Generales", "Según el artículo 67.1 de la Constitución, nadie podrá acumular el acta de una Asamblea de Comunidad Autónoma con la de:",
  ["Diputado al Congreso.", "Concejal.", "Diputado provincial.", "Miembro del Parlamento Europeo."], "Art. 67.1 CE.", "ni acumular el acta de una Asamblea de Comunidad Autónoma con la de Diputado al Congreso")
Q("CE", "Artículo 67", "Cortes Generales", "Según el artículo 67.2 de la Constitución, los miembros de las Cortes Generales:",
  ["No estarán ligados por mandato imperativo.", "Estarán ligados por las instrucciones de su grupo parlamentario.", "Estarán ligados por el mandato de sus electores.", "Estarán ligados por las instrucciones del partido por el que concurrieron."], "Art. 67.2 CE.", "no estarán ligados por mandato imperativo")
Q("CE", "Artículo 68", "Congreso", "Según el artículo 68.1 de la Constitución, el Congreso se compone de:",
  ["Un mínimo de 300 y un máximo de 400 Diputados.", "Un mínimo de 350 y un máximo de 400 Diputados.", "350 Diputados.", "Un mínimo de 250 y un máximo de 350 Diputados."], "Art. 68.1 CE. Los 350 los fija la LOREG (art. 162.1).", "un mínimo de 300 y un máximo de 400 Diputados")
Q("LOREG", "acientosesentaydos", "Congreso", "Según el artículo 162 de la Ley Orgánica 5/1985, del Régimen Electoral General, a cada provincia le corresponde un mínimo inicial de:",
  ["Dos Diputados.", "Un Diputado.", "Tres Diputados.", "Cuatro Diputados."], "Art. 162.2 LOREG.", "A cada provincia le corresponde un mínimo inicial de dos Diputados")
Q("CE", "Artículo 68", "Congreso", "Según el artículo 68.2 de la Constitución, las poblaciones de Ceuta y Melilla estarán representadas en el Congreso cada una de ellas por:",
  ["Un Diputado.", "Dos Diputados.", "Tres Diputados.", "Cuatro Diputados."], "Art. 68.2 CE (en el Senado, dos Senadores: art. 69.4).", "Las poblaciones de Ceuta y Melilla estarán representadas cada una de ellas por un Diputado")
Q("CE", "Artículo 68", "Congreso", "Según el artículo 68.6 de la Constitución, las elecciones tendrán lugar:",
  ["Entre los treinta días y sesenta días desde la terminación del mandato.", "Entre los quince y treinta días desde la terminación del mandato.", "Dentro de los veinticinco días siguientes a la terminación del mandato.", "Entre los treinta días y noventa días desde la terminación del mandato."], "Art. 68.6 CE.", "Las elecciones tendrán lugar entre los treinta días y sesenta días desde la terminación del mandato")
Q("CE", "Artículo 68", "Congreso", "Según el artículo 68.6 de la Constitución, el Congreso electo deberá ser convocado:",
  ["Dentro de los veinticinco días siguientes a la celebración de las elecciones.", "Dentro de los quince días siguientes a la celebración de las elecciones.", "Dentro de los treinta días siguientes a la proclamación de electos.", "Dentro del mes siguiente a la celebración de las elecciones."], "Art. 68.6 CE.", "El Congreso electo deberá ser convocado dentro de los veinticinco días siguientes a la celebración de las elecciones")
Q("CE", "Artículo 68", "Congreso", "Según el artículo 68.3 de la Constitución, la elección de los Diputados se verificará en cada circunscripción atendiendo a criterios de:",
  ["Representación proporcional.", "Representación mayoritaria.", "Representación territorial.", "Voto limitado."], "Art. 68.3 CE.", "La elección se verificará en cada circunscripción atendiendo a criterios de representación proporcional")
Q("RCD", "art5", "Congreso", "Según el artículo 5 del Reglamento del Congreso de los Diputados, la solemne sesión de apertura de la legislatura tendrá lugar dentro del plazo de:",
  ["Los quince días siguientes a la celebración de la sesión constitutiva.", "Los quince días siguientes a la celebración de las elecciones.", "Los veinticinco días siguientes a la sesión constitutiva.", "El mes siguiente a la sesión constitutiva."], "Art. 5 RCD.", "Dentro del plazo de los quince días siguientes a la celebración de la sesión constitutiva")
Q("CE", "Artículo 69", "Senado", "Según el artículo 69.1 de la Constitución, el Senado es:",
  ["La Cámara de representación territorial.", "La Cámara de segunda lectura.", "La Cámara de representación de las provincias.", "La Cámara de representación del pueblo español."], "Art. 69.1 CE.", "El Senado es la Cámara de representación territorial")
Q("CE", "Artículo 69", "Senado", "Según el artículo 69.2 de la Constitución, en cada provincia se elegirán:",
  ["Cuatro Senadores.", "Tres Senadores.", "Dos Senadores.", "Cinco Senadores."], "Art. 69.2 CE.", "En cada provincia se elegirán cuatro Senadores")
Q("CE", "Artículo 69", "Senado", "Según el artículo 69.4 de la Constitución, las poblaciones de Ceuta y Melilla elegirán cada una de ellas:",
  ["Dos Senadores.", "Un Senador.", "Tres Senadores.", "Cuatro Senadores."], "Art. 69.4 CE.", "Las poblaciones de Ceuta y Melilla elegirán cada una de ellas dos Senadores")
Q("CE", "Artículo 69", "Senado", "Según el artículo 69.5 de la Constitución, las Comunidades Autónomas designarán además:",
  ["Un Senador y otro más por cada millón de habitantes de su respectivo territorio.", "Dos Senadores y otro más por cada millón de habitantes de su respectivo territorio.", "Un Senador por cada quinientos mil habitantes de su respectivo territorio.", "Un Senador por cada provincia de su respectivo territorio."], "Art. 69.5 CE.", "Las Comunidades Autónomas designarán además un Senador y otro más por cada millón de habitantes de su respectivo territorio")
Q("RS", "a3", "Senado", "Según el artículo 3 del Reglamento del Senado, tras la Junta Preparatoria se formará una Mesa que presidirá el Senador de más edad de entre los presentes y de la que serán Secretarios:",
  ["Los cuatro más jóvenes.", "Los dos más jóvenes.", "Los dos de más edad tras el Presidente.", "Los cuatro primeros en presentar la credencial."], "Art. 3 RS (en el Congreso, los dos más jóvenes: art. 2 RCD).", "de la que serán Secretarios los cuatro más jóvenes")
Q("RS", "a5", "Senado", "Según el artículo 5 del Reglamento del Senado, la Mesa del Senado está formada por:",
  ["El Presidente, dos Vicepresidentes y cuatro Secretarios.", "El Presidente, cuatro Vicepresidentes y cuatro Secretarios.", "El Presidente, dos Vicepresidentes y dos Secretarios.", "El Presidente, un Vicepresidente y cuatro Secretarios."], "Art. 5.1 RS.", "que estará formada por el Presidente, dos Vicepresidentes y cuatro Secretarios")
Q("RCD", "art30", "Organización", "Según el artículo 30.2 del Reglamento del Congreso de los Diputados, la Mesa del Congreso estará compuesta por:",
  ["La Presidencia del Congreso, cuatro Vicepresidencias y cuatro Secretarías.", "La Presidencia del Congreso, dos Vicepresidencias y cuatro Secretarías.", "La Presidencia del Congreso, cuatro Vicepresidencias y dos Secretarías.", "La Presidencia del Congreso y los portavoces de los grupos parlamentarios."], "Art. 30.2 RCD.", "La Mesa estará compuesta por la Presidencia del Congreso, cuatro Vicepresidencias y cuatro Secretarías")
Q("RS", "a27", "Organización", "Según el artículo 27.1 del Reglamento del Senado, cada Grupo parlamentario estará compuesto, al menos, de:",
  ["Diez Senadores.", "Quince Senadores.", "Cinco Senadores.", "Seis Senadores."], "Art. 27.1 RS (en el Congreso, quince Diputados: art. 23.1 RCD).", "Cada Grupo parlamentario estará compuesto, al menos, de diez Senadores")
Q("RCD", "art39", "Organización", "Según el artículo 39.4 del Reglamento del Congreso de los Diputados, las decisiones de la Junta de Portavoces se adoptarán siempre:",
  ["En función del criterio de voto ponderado.", "Por mayoría simple de los portavoces presentes.", "Por mayoría absoluta de los portavoces.", "Por unanimidad."], "Art. 39.4 RCD.", "Las decisiones de la Junta de Portavoces se adoptarán siempre en función del criterio de voto ponderado")
Q("RCD", "art37", "Organización", "Según el artículo 37.1 del Reglamento del Congreso de los Diputados, en la elección de la Presidencia resultará elegida en primera votación la persona que obtenga:",
  ["El voto de la mayoría absoluta de los miembros de la Cámara.", "El voto de la mayoría de tres quintos de los miembros de la Cámara.", "El voto de la mayoría simple de los presentes.", "El voto de la mayoría de dos tercios de los miembros de la Cámara."], "Art. 37.1 RCD.", "Resultará elegida la persona que obtenga el voto de la mayoría absoluta de los miembros de la Cámara")
Q("CE", "Artículo 70", "Estatuto de los parlamentarios", "Según el artículo 70.1 de la Constitución, las causas de inelegibilidad e incompatibilidad de los Diputados y Senadores comprenderán, en todo caso:",
  ["Al Defensor del Pueblo.", "A los miembros del Gobierno.", "A los Alcaldes.", "A los funcionarios de carrera en activo."], "Art. 70.1 c) CE. Los miembros del Gobierno están exceptuados (70.1 b).", "c) Al Defensor del Pueblo.")
Q("CE", "Artículo 70", "Estatuto de los parlamentarios", "Según el artículo 70.2 de la Constitución, la validez de las actas y credenciales de los miembros de ambas Cámaras estará sometida al control:",
  ["Judicial, en los términos que establezca la ley electoral.", "De la Junta Electoral Central, sin recurso.", "Del Tribunal Constitucional, en única instancia.", "De la Mesa de cada Cámara."], "Art. 70.2 CE.", "estará sometida al control judicial, en los términos que establezca la ley electoral")
Q("CE", "Artículo 71", "Estatuto de los parlamentarios", "Según el artículo 71.2 de la Constitución, durante el período de su mandato los Diputados y Senadores solo podrán ser detenidos:",
  ["En caso de flagrante delito.", "Con autorización del Tribunal Supremo.", "Con autorización de la Mesa de la Cámara respectiva.", "En caso de delito grave."], "Art. 71.2 CE.", "sólo podrán ser detenidos en caso de flagrante delito")
Q("CE", "Artículo 71", "Estatuto de los parlamentarios", "Según el artículo 71.3 de la Constitución, en las causas contra Diputados y Senadores será competente:",
  ["La Sala de lo Penal del Tribunal Supremo.", "La Sala de lo Penal de la Audiencia Nacional.", "El Tribunal Superior de Justicia de su circunscripción.", "El Tribunal Constitucional."], "Art. 71.3 CE.", "En las causas contra Diputados y Senadores será competente la Sala de lo Penal del Tribunal Supremo")
Q("CE", "Artículo 71", "Estatuto de los parlamentarios", "Según el artículo 71.4 de la Constitución, la asignación de los Diputados y Senadores será fijada:",
  ["Por las respectivas Cámaras.", "Por la Ley de Presupuestos Generales del Estado.", "Por el Gobierno, a propuesta del Ministerio de Hacienda.", "Por las Cortes Generales en sesión conjunta."], "Art. 71.4 CE.", "Los Diputados y Senadores percibirán una asignación que será fijada por las respectivas Cámaras")
Q("CE", "Artículo 72", "Organización", "Según el artículo 72.1 de la Constitución, los Reglamentos de las Cámaras y su reforma serán sometidos a una votación final sobre su totalidad, que requerirá:",
  ["La mayoría absoluta.", "La mayoría de tres quintos.", "La mayoría simple.", "La mayoría de dos tercios."], "Art. 72.1 CE.", "Los Reglamentos y su reforma serán sometidos a una votación final sobre su totalidad, que requerirá la mayoría absoluta")
Q("CE", "Artículo 72", "Organización", "Según el artículo 72.2 de la Constitución, las sesiones conjuntas de las Cámaras serán presididas por:",
  ["El Presidente del Congreso.", "El Presidente del Senado.", "El Rey.", "El de mayor edad de los dos Presidentes."], "Art. 72.2 CE.", "Las sesiones conjuntas serán presididas por el Presidente del Congreso")
Q("CE", "Artículo 73", "Funcionamiento", "Según el artículo 73.1 de la Constitución, las Cámaras se reunirán anualmente en dos períodos ordinarios de sesiones:",
  ["De septiembre a diciembre y de febrero a junio.", "De septiembre a diciembre y de enero a junio.", "De octubre a diciembre y de febrero a julio.", "De septiembre a enero y de marzo a junio."], "Art. 73.1 CE.", "el primero, de septiembre a diciembre, y el segundo, de febrero a junio")
Q("CE", "Artículo 73", "Funcionamiento", "Según el artículo 73.2 de la Constitución, las Cámaras podrán reunirse en sesiones extraordinarias a petición de:",
  ["El Gobierno, la Diputación Permanente o la mayoría absoluta de los miembros de cualquiera de las Cámaras.", "El Rey, el Gobierno o la Diputación Permanente.", "El Gobierno o la quinta parte de los miembros de cualquiera de las Cámaras.", "Los Presidentes de las Cámaras, exclusivamente."], "Art. 73.2 CE.", "a petición del Gobierno, de la Diputación Permanente o de la mayoría absoluta de los miembros de cualquiera de las Cámaras")
Q("CE", "Artículo 74", "Funcionamiento", "Según el artículo 74.2 de la Constitución, si no hubiera acuerdo entre Senado y Congreso y el texto de la Comisión Mixta no se aprueba en la forma establecida:",
  ["Decidirá el Congreso por mayoría absoluta.", "Decidirá el Senado por mayoría absoluta.", "Decidirán las Cortes Generales en sesión conjunta.", "Decidirá el Congreso por mayoría de tres quintos."], "Art. 74.2 CE.", "Si no se aprueba en la forma establecida, decidirá el Congreso por mayoría absoluta")
Q("CE", "Artículo 75", "Funcionamiento", "Según el artículo 75.3 de la Constitución, ¿cuál de las siguientes materias NO puede delegarse en las Comisiones Legislativas Permanentes?",
  ["Los Presupuestos Generales del Estado.", "Una ley ordinaria de contratos.", "Una proposición de ley ordinaria.", "Un proyecto de ley ordinaria declarado urgente."], "Art. 75.3 CE: reforma constitucional, cuestiones internacionales, leyes orgánicas y de bases y Presupuestos Generales del Estado.", "las leyes orgánicas y de bases y los Presupuestos Generales del Estado")
Q("CE", "Artículo 76", "Funcionamiento", "Según el artículo 76.1 de la Constitución, las conclusiones de las Comisiones de investigación:",
  ["No serán vinculantes para los Tribunales.", "Serán vinculantes para los Tribunales.", "Vincularán al Ministerio Fiscal.", "Tendrán fuerza de cosa juzgada."], "Art. 76.1 CE.", "Sus conclusiones no serán vinculantes para los Tribunales")
Q("CE", "Artículo 77", "Funcionamiento", "Según el artículo 77.1 de la Constitución, las Cámaras pueden recibir peticiones individuales y colectivas:",
  ["Siempre por escrito, quedando prohibida la presentación directa por manifestaciones ciudadanas.", "Por escrito u oralmente.", "Solo a través de los grupos parlamentarios.", "Siempre por escrito, permitiéndose la presentación directa por manifestaciones ciudadanas autorizadas."], "Art. 77.1 CE.", "siempre por escrito, quedando prohibida la presentación directa por manifestaciones ciudadanas")
Q("CE", "Artículo 78", "Diputación Permanente", "Según el artículo 78.1 de la Constitución, en cada Cámara habrá una Diputación Permanente compuesta por:",
  ["Un mínimo de veintiún miembros.", "Un máximo de veintiún miembros.", "Un mínimo de quince miembros.", "Veinticinco miembros."], "Art. 78.1 CE.", "compuesta por un mínimo de veintiún miembros")
Q("CE", "Artículo 78", "Diputación Permanente", "Según el artículo 78.2 de la Constitución, las Diputaciones Permanentes estarán presididas por:",
  ["El Presidente de la Cámara respectiva.", "El Vicepresidente primero de la Cámara respectiva.", "El Presidente del Congreso, en ambos casos.", "El Diputado o Senador de mayor edad."], "Art. 78.2 CE.", "Las Diputaciones Permanentes estarán presididas por el Presidente de la Cámara respectiva")
Q("CE", "Artículo 79", "Funcionamiento", "Según el artículo 79 de la Constitución, para adoptar acuerdos las Cámaras deben estar reunidas reglamentariamente y con asistencia de:",
  ["La mayoría de sus miembros.", "Un tercio de sus miembros.", "Las dos terceras partes de sus miembros.", "La mayoría de los grupos parlamentarios."], "Art. 79.1 CE.", "con asistencia de la mayoría de sus miembros")
Q("CE", "Artículo 79", "Funcionamiento", "Según el artículo 79.3 de la Constitución, el voto de Senadores y Diputados es:",
  ["Personal e indelegable.", "Personal y delegable en otro miembro de su grupo.", "Secreto en todo caso.", "Delegable en el portavoz del grupo."], "Art. 79.3 CE.", "El voto de Senadores y Diputados es personal e indelegable")
Q("CE", "Artículo 87", "Atribuciones", "Según el artículo 87.1 de la Constitución, la iniciativa legislativa corresponde:",
  ["Al Gobierno, al Congreso y al Senado.", "Exclusivamente al Gobierno.", "Al Gobierno y al Congreso.", "Al Congreso y al Senado."], "Art. 87.1 CE.", "La iniciativa legislativa corresponde al Gobierno, al Congreso y al Senado")
Q("CE", "Artículo 87", "Atribuciones", "Según el artículo 87.3 de la Constitución, NO procederá la iniciativa popular en materia:",
  ["Tributaria.", "De vivienda.", "De sanidad.", "De medio ambiente."], "Art. 87.3 CE: materias propias de ley orgánica, tributarias o de carácter internacional y prerrogativa de gracia.", "No procederá dicha iniciativa en materias propias de ley orgánica, tributarias o de carácter internacional")
Q("CE", "Artículo 88", "Atribuciones", "Según el artículo 88 de la Constitución, los proyectos de ley serán aprobados:",
  ["En Consejo de Ministros, que los someterá al Congreso.", "En Consejo de Ministros, que los someterá al Senado.", "Por el Presidente del Gobierno, que los someterá a las Cortes Generales.", "Por la Comisión General de Secretarios de Estado y Subsecretarios."], "Art. 88 CE.", "Los proyectos de ley serán aprobados en Consejo de Ministros, que los someterá al Congreso")
Q("CE", "Artículo 90", "Atribuciones", "Según el artículo 90.2 de la Constitución, el veto del Senado a un proyecto de ley deberá ser aprobado por:",
  ["Mayoría absoluta.", "Mayoría simple.", "Mayoría de tres quintos.", "Mayoría de dos tercios."], "Art. 90.2 CE.", "El veto deberá ser aprobado por mayoría absoluta")
Q("CE", "Artículo 90", "Atribuciones", "Según el artículo 90.2 de la Constitución, el Senado puede oponer su veto o introducir enmiendas a un proyecto de ley ordinaria u orgánica en el plazo de:",
  ["Dos meses, a partir del día de la recepción del texto.", "Un mes, a partir del día de la recepción del texto.", "Dos meses, a partir de la aprobación por el Congreso.", "Veinte días hábiles, a partir de la recepción del texto."], "Art. 90.2 CE.", "El Senado en el plazo de dos meses, a partir del día de la recepción del texto")
Q("CE", "Artículo 92", "Atribuciones", "Según el artículo 92.2 de la Constitución, el referéndum consultivo será convocado por el Rey, mediante propuesta del Presidente del Gobierno, previamente autorizada por:",
  ["El Congreso de los Diputados.", "Las Cortes Generales en sesión conjunta.", "El Senado.", "El Consejo de Estado."], "Art. 92.2 CE.", "mediante propuesta del Presidente del Gobierno, previamente autorizada por el Congreso de los Diputados")
Q("CE", "Artículo 94", "Atribuciones", "Según el artículo 94.1 de la Constitución, requerirá la previa autorización de las Cortes Generales la prestación del consentimiento del Estado para obligarse por:",
  ["Tratados o convenios de carácter militar.", "Cualquier tratado o convenio internacional.", "Tratados o convenios de carácter cultural.", "Tratados o convenios de cooperación técnica sin obligaciones financieras."], "Art. 94.1 b) CE. Los demás tratados solo exigen informar a las Cámaras (94.2).", "b) Tratados o convenios de carácter militar.")
T.real("X", 12, "Estatuto de los parlamentarios"); T.real("X", 13, "Congreso"); T.real("X", 14, "Senado"); T.real("L", 7, "Funcionamiento")
T.real("P", 45, "Atribuciones"); T.real("P", 48, "Atribuciones"); T.real("P", 46, "Atribuciones")

# Flashcards
for q_, a_, cat in [
  ("¿Qué representan las Cortes Generales y de qué Cámaras se forman? (art. 66.1)", "Al pueblo español; Congreso de los Diputados y Senado.", "Cortes Generales"),
  ("Funciones de las Cortes (art. 66.2)", "Potestad legislativa del Estado, aprobar sus Presupuestos, controlar la acción del Gobierno y las demás que les atribuya la Constitución.", "Cortes Generales"),
  ("Horquilla constitucional y número legal de Diputados", "300 a 400 (art. 68.1 CE); 350 (art. 162.1 LOREG).", "Congreso"),
  ("Plazos del art. 68.6", "Elecciones entre 30 y 60 días desde la terminación del mandato; Congreso electo convocado en los 25 días siguientes a las elecciones.", "Congreso"),
  ("¿Quién preside inicialmente la sesión constitutiva del Congreso? (RCD 2)", "La diputada o diputado electos de mayor edad presente, con los dos más jóvenes en las Secretarías.", "Congreso"),
  ("Senadores por provincia, islas mayores, otras islas y Ceuta y Melilla (art. 69)", "4 por provincia; 3 en Gran Canaria, Mallorca y Tenerife; 1 en Ibiza, Formentera, Menorca, Fuerteventura, La Gomera, El Hierro, Lanzarote y La Palma; 2 en Ceuta y 2 en Melilla.", "Senado"),
  ("Senadores designados por las Comunidades Autónomas (art. 69.5)", "Un Senador y otro más por cada millón de habitantes; los designa la Asamblea legislativa (o, en su defecto, el órgano colegiado superior).", "Senado"),
  ("Mesa de edad del Senado (RS 3)", "El Senador de más edad de entre los presentes y, como Secretarios, los cuatro más jóvenes.", "Senado"),
  ("Mesa del Congreso y Mesa del Senado", "Congreso: Presidencia, 4 Vicepresidencias y 4 Secretarías (RCD 30.2). Senado: Presidente, 2 Vicepresidentes y 4 Secretarios (RS 5.1).", "Organización"),
  ("Mínimo para formar grupo parlamentario", "Congreso: 15 Diputados (RCD 23.1). Senado: 10 Senadores (RS 27.1).", "Organización"),
  ("¿Qué miembros quedan exceptuados de la inelegibilidad de los altos cargos? (art. 70.1 b)", "Los miembros del Gobierno.", "Estatuto de los parlamentarios"),
  ("Inviolabilidad e inmunidad (art. 71.1 y 2)", "Inviolabilidad por las opiniones en el ejercicio de sus funciones; inmunidad: detención solo en flagrante delito e inculpación o procesamiento con previa autorización de la Cámara respectiva.", "Estatuto de los parlamentarios"),
  ("Tribunal competente en las causas contra Diputados y Senadores (art. 71.3)", "La Sala de lo Penal del Tribunal Supremo.", "Estatuto de los parlamentarios"),
  ("Mayoría para los Reglamentos de las Cámaras y para el Reglamento de las Cortes (art. 72)", "Reglamento de cada Cámara: mayoría absoluta en votación final sobre su totalidad. Reglamento de las Cortes Generales: mayoría absoluta de cada Cámara.", "Organización"),
  ("Períodos ordinarios de sesiones (art. 73.1)", "De septiembre a diciembre y de febrero a junio.", "Funcionamiento"),
  ("Art. 74.2: ¿qué decisiones y quién empieza?", "Tratados del 94.1 (empieza el Congreso), 145.2 y 158.2 (empieza el Senado); mayoría de cada Cámara; Comisión Mixta; si no, decide el Congreso por mayoría absoluta.", "Funcionamiento"),
  ("Materias no delegables en Comisiones (art. 75.3)", "Reforma constitucional, cuestiones internacionales, leyes orgánicas y de bases y Presupuestos Generales del Estado.", "Funcionamiento"),
  ("Diputación Permanente (art. 78)", "Una por Cámara; mínimo 21 miembros; la preside el Presidente de la Cámara; arts. 73, 86 y 116 y velar por los poderes de la Cámara.", "Diputación Permanente"),
  ("Quórum y mayoría para los acuerdos (art. 79)", "Asistencia de la mayoría de sus miembros; aprobación por la mayoría de los miembros presentes; voto personal e indelegable.", "Funcionamiento"),
  ("Iniciativa de las Asambleas de las Comunidades Autónomas (art. 87.2)", "Solicitar del Gobierno un proyecto de ley o remitir a la Mesa del Congreso una proposición, delegando un máximo de tres miembros.", "Atribuciones"),
  ("Iniciativa popular (art. 87.3)", "Ley orgánica; no menos de 500.000 firmas; no en materias de ley orgánica, tributarias, internacionales ni prerrogativa de gracia.", "Atribuciones"),
  ("Plazos y mayorías del Senado en la tramitación de la ley (art. 90)", "Dos meses (veinte días naturales si es urgente) para vetar (mayoría absoluta) o enmendar; el Congreso levanta el veto por mayoría absoluta o, pasados dos meses, por mayoría simple.", "Atribuciones"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Cortes Generales", "Órgano que representa al pueblo español, formado por el Congreso de los Diputados y el Senado (art. 66.1 CE).", "s1", "Cortes Generales")
T.glos("Mandato imperativo", "Vinculación del representante a instrucciones ajenas; la Constitución la prohíbe a los miembros de las Cortes (art. 67.2).", "s2", "Cortes Generales")
T.glos("Circunscripción electoral", "Ámbito territorial en que se eligen los representantes: para el Congreso, la provincia (art. 68.2); para el Senado, también cada isla con Cabildo o Consejo Insular (art. 69.3).", "s3", "Congreso")
T.glos("Sesión constitutiva", "Primera sesión de la Cámara tras las elecciones, en la que se elige la Mesa y se presta juramento o promesa (RCD, arts. 1 a 4).", "s4", "Congreso")
T.glos("Junta Preparatoria", "Reunión inicial de los Senadores, el día señalado en el Decreto de convocatoria, antes de constituirse el Senado (RS, art. 2).", "s6", "Senado")
T.glos("Senadores de designación autonómica", "Los que designan las Comunidades Autónomas: un Senador y otro más por cada millón de habitantes (art. 69.5).", "s5", "Senado")
T.glos("Inelegibilidad e incompatibilidad", "Causas que impiden ser elegido o ejercer el cargo de Diputado o Senador; las fija la ley electoral con el mínimo del art. 70.1.", "s8", "Estatuto de los parlamentarios")
T.glos("Inviolabilidad", "Prerrogativa de Diputados y Senadores por las opiniones manifestadas en el ejercicio de sus funciones (art. 71.1).", "s9", "Estatuto de los parlamentarios")
T.glos("Inmunidad", "Prerrogativa por la que Diputados y Senadores solo pueden ser detenidos en flagrante delito y no pueden ser inculpados ni procesados sin autorización de su Cámara (art. 71.2).", "s9", "Estatuto de los parlamentarios")
T.glos("Mesa", "Órgano rector de cada Cámara (RCD, art. 30; RS, art. 35); la eligen las propias Cámaras (art. 72.2 CE).", "s11", "Organización")
T.glos("Grupo parlamentario", "Agrupación de parlamentarios reconocida por el Reglamento (Congreso, mínimo quince; Senado, mínimo diez); los no integrados pasan al Grupo Mixto.", "s11", "Organización")
T.glos("Junta de Portavoces", "Órgano formado por los portavoces de los grupos y presidido por el Presidente de la Cámara; en el Congreso decide por voto ponderado (RCD, art. 39; RS, art. 43).", "s11", "Organización")
T.glos("Comisión Mixta", "Comisión de igual número de Diputados y Senadores que intenta el acuerdo entre las Cámaras en los casos del art. 74.2.", "s12", "Funcionamiento")
T.glos("Diputación Permanente", "Órgano de cada Cámara, de al menos veintiún miembros, que vela por sus poderes cuando no está reunida y asume funciones de los arts. 86 y 116 si está disuelta (art. 78).", "s14", "Diputación Permanente")
T.glos("Veto del Senado", "Oposición del Senado a un proyecto aprobado por el Congreso, por mayoría absoluta y mensaje motivado, en dos meses (art. 90.2).", "s18", "Atribuciones")

# Cronología (fechas de los metadatos del BOE)
T.hito("1978", "Constitución Española (27-12-1978; BOE de 29-12-1978)", "Título III, capítulo I (arts. 66 a 80) y arts. 87 a 94: las Cortes Generales", "normativo", "s1")
T.hito("1982", "Reglamento del Congreso de los Diputados de 10 de febrero de 1982 (publicado por Resolución de 24-2-1982; BOE de 5-3-1982)", "Sesión constitutiva, grupos, Mesa, Junta de Portavoces, Comisiones y Diputación Permanente del Congreso", "normativo", "s4")
T.hito("1985", "Ley Orgánica 5/1985, de 19 de junio, del Régimen Electoral General (BOE de 20-6-1985)", "Arts. 162 y 165: 350 Diputados y reparto de los Senadores", "normativo", "s3")
T.hito("1994", "Texto refundido del Reglamento del Senado aprobado por la Mesa del Senado el 3-5-1994 (BOE de 13-5-1994)", "Junta Preparatoria, Mesa, grupos, Comisiones y Diputación Permanente del Senado", "normativo", "s6")
T.hito("2025", "Reforma del Reglamento del Congreso de 22 de julio de 2025 (BOE-A-2025-15844; BOE de 31-7-2025)", "Nueva redacción, entre otros, de los arts. 2, 23 y 30 RCD (Presidencia, Vicepresidencias y Secretarías)", "normativo", "s11")

T.publicar()
