# -*- coding: utf-8 -*-
"""Tema I.7 (B1T07): El Poder Judicial. El principio de unidad jurisdiccional. El Consejo
General del Poder Judicial. La organización judicial española.
Método del I.2: mapa → bloques (I a IV) con guía; cada artículo, texto literal del
BOE + ficha de casillas fijas; cierre 1 (preguntas oficiales) y cierre 2 (repaso).
Normas (textos consolidados del BOE, versión vigente): CE, arts. 117 a 127 y 152.1;
LO 6/1985, del Poder Judicial (LOPJ), tras la LO 3/2024 y la LO 1/2025; LO 1/2025,
disposiciones adicional primera y transitorias primera, segunda y sexta."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO["LO1_2025"] = "LO 1/2025"
L = "LOPJ"

T = Tema("B1T07",
  "Cuatro preguntas: I. Qué es el Poder Judicial y cómo actúa (arts. 117.1 a 4, 118 a 122.1 y 124 a 127 CE; LOPJ, arts. 1, 2, 182, 183 y 185) · II. Qué significa el principio de unidad jurisdiccional (art. 117.5 y 6 CE; LOPJ, arts. 3, 4 y 9) · III. Qué es el Consejo General del Poder Judicial, cómo se compone y qué hace (arts. 122 y 123 CE; LOPJ, Libro VIII) · IV. Cómo se organizan los Juzgados y Tribunales (LOPJ, arts. 26, 29, 30, 32 a 34, 53 a 59, 61, 62 a 66, 70 a 74, 80 a 82, 84, 95, 99 a 102 y 439 ter; LO 1/2025). Cada artículo: texto literal del BOE y ficha.",
  ["Poder Judicial", "Arts. 117-127 CE", "LOPJ", "Unidad jurisdiccional", "Jurisdicción militar", "Órdenes jurisdiccionales", "CGPJ", "Art. 122 CE", "Vocales", "Tres quintos", "Tribunal Supremo", "Audiencia Nacional", "Tribunales Superiores de Justicia", "Audiencias Provinciales", "Tribunales de Instancia", "Tribunal Central de Instancia", "Jueces de paz", "LO 1/2025", "Ministerio Fiscal"])

# Cuadros (esquemas) con citas literales
TAB1 = f"""| Precepto | Texto literal |
|---|---|
| Art. 125 | {c('CE', 'Artículo 125', 'Tribunales consuetudinarios y tradicionales')} |
| Art. 136.2 | El Tribunal de Cuentas, {c('CE', 'Artículo 136', 'sin perjuicio de su propia jurisdicción')} |"""
TAB2 = """| Orden | Conoce de | Apartado |
|---|---|---|
| Civil | Materias propias + todas las no atribuidas a otro orden (**residual**) | 9.2 |
| Penal | Causas y juicios criminales (salvo jurisdicción militar) | 9.3 |
| Contencioso-administrativo | Actuación administrativa sujeta al derecho administrativo, disposiciones generales de rango inferior a la ley, reales decretos legislativos (en los términos del art. 82.6 CE), inactividad, vía de hecho, responsabilidad patrimonial | 9.4 |
| Social | Rama social del derecho y Seguridad Social | 9.5 |"""
TAB3 = """| Órgano | Composición | Mandato | Rasgo que se pregunta |
|---|---|---|---|
| Pleno | Presidente + 20 Vocales | El del Consejo (5 años) | Nombramientos discrecionales; TC por tres quintos; quórum 12 / 10 + Presidente |
| Comisión Permanente | Presidente + 7 Vocales (4 + 3) | Anual | Nombramientos reglados; alzada ante el Pleno |
| Comisión Disciplinaria | 7 Vocales (4 + 3) | 5 años | Infracciones graves y muy graves, salvo separación |
| Asuntos Económicos | 3 Vocales | Anual | Control financiero y contable |
| Igualdad | 3 Vocales | Anual | Impacto de género |"""
# =============================================================================
T.ap("s0", "Mapa del tema: cuatro preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque I, tema 7):
> 7. El Poder Judicial. El principio de unidad jurisdiccional. El Consejo General del Poder Judicial. La organización judicial española.

### El hilo conductor

El epígrafe se lee como **cuatro preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Constitución | LOPJ y otras normas |
|---|---|---|---|
| **I** | ¿Qué es el Poder Judicial y cómo actúa? | Arts. 117.1 a 4, 118 a 122.1 y 124 a 127 | LOPJ, arts. 1, 2, 182, 183 y 185 |
| **II** | ¿Qué significa el principio de unidad jurisdiccional? | Art. 117.5 y 6 | LOPJ, arts. 3, 4 y 9 |
| **III** | ¿Qué es el Consejo General del Poder Judicial, cómo se compone y qué hace? | Arts. 122.2 y 3 y 123.2 | LOPJ (Libro VIII), arts. 558, 560, 561, 566 a 570 bis, 578, 579, 581, 582, 585 a 587, 589, 595, 599 a 604, 609, 610 y 638 |
| **IV** | ¿Cómo se organizan los Juzgados y Tribunales? | Arts. 123.1 y 152.1 | LOPJ, arts. 26, 29, 30, 32 a 34, 53 a 59, 61, 62 a 66, 70 a 74, 80 a 82, 84, 95, 99 a 102 y 439 ter; LO 1/2025 |

!> **La idea que une los cuatro bloques:** la justicia la administran **Jueces y Magistrados** independientes, inamovibles, responsables y sometidos únicamente al imperio de la ley (I). Todos forman **una sola jurisdicción**, de la que solo se separa la militar en el ámbito estrictamente castrense (II). Ese Poder Judicial tiene un **órgano de gobierno** propio, el **CGPJ** (III), y se organiza en una **planta** de órganos que va de los jueces de paz al **Tribunal Supremo** (IV).

?> **Aviso de vigencia (LO 1/2025).** La LOPJ vigente ya no habla de Juzgados de Primera Instancia, de Instrucción, de lo Penal, etc., sino de **Tribunales de Instancia** organizados en **Secciones**, y de un **Tribunal Central de Instancia** en lugar de los Juzgados Centrales (→ IV.6). Algunos artículos que no se reformaron (por ejemplo, los de los jueces de paz) conservan la terminología antigua: se citan literalmente, como están en el BOE.

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen; o, si es un derecho, Titulares · Contenido · Límites · Protección · ⚠ Ojo en el examen).
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué es el Poder Judicial y cómo actúa? (arts. 117.1 a 4, 118 a 122.1 y 124 a 127 CE; LOPJ, arts. 1, 2, 182, 183 y 185)", donde(
  "Primera pregunta del tema. El Título VI de la Constitución («Del Poder Judicial») dice **de dónde emana** la justicia, **quién** la administra, con qué **garantías** y con qué **reglas** de actuación. La LOPJ lo repite y lo desarrolla.",
  ["1 La justicia, los jueces y la potestad jurisdiccional (art. 117.1 a 4; LOPJ, arts. 1 y 2)", "2 Principios de la actuación judicial (arts. 118 a 121; LOPJ, arts. 182, 183 y 185)", "3 Cuerpo único, Ministerio Fiscal, participación ciudadana, policía judicial e incompatibilidades (arts. 122.1 y 124 a 127)"]))

T.ap("s1", "I.1 La justicia, los jueces y la potestad jurisdiccional (art. 117.1 a 4; LOPJ, arts. 1 y 2)", f"""
{unidad("1.1 De dónde emana la justicia y quién la administra (art. 117.1; LOPJ, art. 1)",
  lit("CE", "Artículo 117", ["La justicia emana del pueblo y se administra en nombre del Rey", "independientes, inamovibles, responsables y sometidos únicamente al imperio de la ley"], solo=[1]),
  lit(L, "aprimero", ["sometidos únicamente a la Constitución y al imperio de la ley"]),
  fichab("Origen de la justicia y estatuto básico de quienes la administran",
         f"{c('CE', 'Artículo 117', 'Jueces y Magistrados integrantes del poder judicial')}",
         ["::Cuatro notas:", "Independientes", "Inamovibles", "Responsables", "Sometidos únicamente al imperio de la ley (la LOPJ añade: «a la Constitución»)"],
         "—",
         "La justicia **emana del pueblo** y se administra **en nombre del Rey** (no «emana del Rey»). Son **cuatro** notas: independencia, inamovilidad, responsabilidad y sumisión a la ley."))}

{unidad("1.2 Inamovilidad (art. 117.2)",
  lit("CE", "Artículo 117", ["no podrán ser separados, suspendidos, trasladados ni jubilados"], solo=[2]),
  fichab("Garantía de inamovilidad", "Jueces y Magistrados",
         "Solo pueden ser separados, suspendidos, trasladados o jubilados por las causas y con las garantías de la ley",
         "—",
         "Son **cuatro** situaciones: separación, suspensión, traslado y jubilación; siempre «por alguna de las causas y con las garantías previstas **en la ley**»."))}

{unidad("1.3 La potestad jurisdiccional: exclusiva y limitada (art. 117.3 y 4; LOPJ, art. 2)",
  lit("CE", "Artículo 117", ["juzgando y haciendo ejecutar lo juzgado", "corresponde exclusivamente a los Juzgados y Tribunales determinados por las leyes", "en garantía de cualquier derecho"], solo=[3, 4]),
  lit(L, "asegundo", ["y en los tratados internacionales"]),
  fichab("La función de juzgar y hacer ejecutar lo juzgado",
         f"{c('CE', 'Artículo 117', 'exclusivamente a los Juzgados y Tribunales determinados por las leyes')}",
         ["Juzgar y **hacer ejecutar** lo juzgado, en todo tipo de procesos", "Según las normas de **competencia y procedimiento** de las leyes", "Ninguna otra función, salvo las que les atribuya **expresamente la ley en garantía de cualquier derecho** (117.4)"],
         "—",
         "La potestad incluye **ejecutar** lo juzgado. La LOPJ añade los Tribunales determinados **en los tratados internacionales**. Las funciones extra solo **por ley** y **en garantía de cualquier derecho**."))}
""", 2)

T.ap("s2", "I.2 Principios de la actuación judicial (arts. 118 a 121; LOPJ, arts. 182, 183 y 185)", f"""
{unidad("2.1 Obligación de cumplir las resoluciones y de colaborar (art. 118)",
  lit("CE", "Artículo 118", ["Es obligado cumplir las sentencias y demás resoluciones firmes", "prestar la colaboración requerida"]),
  fichab("Deber de cumplimiento y de colaboración", "Todos (la Constitución no distingue entre poderes públicos y particulares)",
         ["Cumplir las sentencias y demás resoluciones **firmes**", "Prestar la colaboración requerida **en el curso del proceso** y **en la ejecución** de lo resuelto"],
         "—", "Se refiere a las resoluciones **firmes**, y la colaboración se extiende **al proceso y a la ejecución**."))}

{unidad("2.2 Gratuidad de la justicia (art. 119)",
  lit("CE", "Artículo 119", ["cuando así lo disponga la ley", "en todo caso, respecto de quienes acrediten insuficiencia de recursos para litigar"]),
  ficha(f"Quienes {c('CE', 'Artículo 119', 'acrediten insuficiencia de recursos para litigar')} (en todo caso) y los demás supuestos que disponga la ley",
        "Justicia gratuita",
        "Fuera del caso de insuficiencia de recursos, solo «cuando así lo disponga la ley»",
        "—",
        "La justicia **no es gratuita siempre**: lo es cuando lo diga la ley y, **en todo caso**, para quien acredite **insuficiencia de recursos para litigar**."))}

{unidad("2.3 Publicidad, oralidad y motivación (art. 120)",
  lit("CE", "Artículo 120", ["serán públicas, con las excepciones que prevean las leyes de procedimiento", "predominantemente oral, sobre todo en materia criminal", "siempre motivadas y se pronunciarán en audiencia pública"]),
  fichab("Reglas de las actuaciones judiciales", "Juzgados y Tribunales",
         ["Actuaciones **públicas**, salvo las excepciones de las leyes de procedimiento (120.1)", "Procedimiento **predominantemente oral**, sobre todo en materia **criminal** (120.2)", "Sentencias **siempre motivadas** y pronunciadas **en audiencia pública** (120.3)"],
         "—",
         "Oralidad «**predominante**» (no exclusiva), «sobre todo en materia **criminal**». La motivación de las sentencias es **siempre**."))}

{unidad("2.4 Días y horas hábiles; cómputo de plazos (LOPJ, arts. 182, 183 y 185)",
  lit(L, "acientoochentaydos", ["los sábados y domingos", "desde las ocho de la mañana a las ocho de la tarde"]),
  lit(L, "acientoochentaytres", ["los días del mes de agosto", "desde el 24 de diciembre hasta el 6 de enero del año siguiente, ambos inclusive"]),
  lit(L, "acientoochentaycinco", ["quedarán excluidos los inhábiles"]),
  fichab("Tiempo hábil de las actuaciones judiciales", "Juzgados y Tribunales; el CGPJ puede habilitar días por reglamento",
         ["Inhábiles: sábados, domingos, fiesta nacional y festivos laborales de la Comunidad Autónoma o localidad (182.1)", "Inhábiles: **agosto** y del **24 de diciembre al 6 de enero**, ambos inclusive, salvo actuaciones urgentes (183)", "Horas hábiles: de **8 a 20 h**, salvo que la ley disponga lo contrario (182.2)", "Plazos por días: se **excluyen** los inhábiles; si el último es inhábil, se prorroga al primer hábil (185)"],
         "Horas hábiles: de las **ocho** a las **ocho**",
         "Cayó en 2025 (→ Cierre 1): **24 de diciembre a 6 de enero** (no «julio y agosto»), horas de **8 a 20** (no de 7 a 19) y los inhábiles se **excluyen** (no «se incluyen»)."))}

{unidad("2.5 Responsabilidad del Estado por error judicial y funcionamiento anormal (art. 121)",
  lit("CE", "Artículo 121", ["error judicial", "funcionamiento anormal de la Administración de Justicia", "a cargo del Estado"]),
  ficha("Quienes sufran daños por error judicial o por funcionamiento anormal de la Administración de Justicia",
        "Derecho a una **indemnización a cargo del Estado**",
        f"{c('CE', 'Artículo 121', 'conforme a la ley')}",
        "Reclamación de indemnización conforme a la ley (LOPJ, arts. 292 y siguientes)",
        "Dos títulos: **error judicial** y **funcionamiento anormal**. Paga el **Estado** (no el juez)."))}
""", 2)

T.ap("s3", "I.3 Cuerpo único, Ministerio Fiscal, participación ciudadana, policía judicial e incompatibilidades (arts. 122.1 y 124 a 127)", f"""
{unidad("3.1 La LOPJ y el Cuerpo único de Jueces y Magistrados (art. 122.1)",
  lit("CE", "Artículo 122", ["La ley orgánica del poder judicial", "que formarán un Cuerpo único"], solo=[1]),
  fichab("Reserva de ley orgánica para la organización judicial y el estatuto de los jueces",
         "Las Cortes, mediante la **ley orgánica del poder judicial** (hoy, LO 6/1985)",
         ["Constitución, funcionamiento y gobierno de los Juzgados y Tribunales", "Estatuto jurídico de los Jueces y Magistrados **de carrera** (Cuerpo **único**)", "Estatuto del personal al servicio de la Administración de Justicia"],
         "Ley **orgánica**",
         f"Los Jueces y Magistrados de carrera forman un **Cuerpo único**. La LOPJ lo articula en tres categorías: {c(L, 'adoscientosnoventaynueve', 'Magistrado del Tribunal Supremo')}, Magistrado y Juez (art. 299)."))}

{unidad("3.2 El Ministerio Fiscal (art. 124)",
  lit("CE", "Artículo 124", ["promover la acción de la justicia en defensa de la legalidad", "unidad de actuación y dependencia jerárquica", "legalidad e imparcialidad", "nombrado por el Rey, a propuesta del Gobierno, oído el Consejo General del Poder Judicial"]),
  fichab("Órgano que promueve la acción de la justicia",
         ["El Ministerio Fiscal, por medio de **órganos propios**", f"El Fiscal General del Estado: {c('CE', 'Artículo 124', 'nombrado por el Rey, a propuesta del Gobierno, oído el Consejo General del Poder Judicial')}"],
         ["::Misión (124.1):", "Promover la acción de la justicia en defensa de la legalidad, de los derechos de los ciudadanos y del interés público tutelado por la ley", "De oficio o a petición de los interesados", "Velar por la independencia de los Tribunales y procurar ante éstos la satisfacción del interés social"],
         "—",
         "Cayó dos veces en 2025 (→ Cierre 1). **Cuatro** principios: **unidad de actuación** y **dependencia jerárquica**; **legalidad** e **imparcialidad** (no «independencia» ni «objetividad»). FGE: lo nombra el **Rey**, a propuesta del **Gobierno**, **oído** el CGPJ."))}

{unidad("3.3 Acción popular, Jurado y Tribunales consuetudinarios (art. 125)",
  lit("CE", "Artículo 125", ["la acción popular", "la institución del Jurado", "en los Tribunales consuetudinarios y tradicionales"]),
  ficha("Los ciudadanos",
        ["Ejercer la **acción popular**", "Participar en la Administración de Justicia mediante el **Jurado**", "Participar en los **Tribunales consuetudinarios y tradicionales**"],
        f"El Jurado, {c('CE', 'Artículo 125', 'en la forma y con respecto a aquellos procesos penales que la ley determine')}",
        "—",
        "El Jurado se limita a los **procesos penales** que determine la ley. Son **tres** formas de participación."))}

{unidad("3.4 La policía judicial (art. 126)",
  lit("CE", "Artículo 126", ["depende de los Jueces, de los Tribunales y del Ministerio Fiscal"]),
  fichab("Policía al servicio de la investigación del delito", "Depende de los Jueces, de los Tribunales y del Ministerio Fiscal",
         f"En sus funciones de {c('CE', 'Artículo 126', 'averiguación del delito y descubrimiento y aseguramiento del delincuente')}", "—",
         "Depende **también del Ministerio Fiscal** (no solo de los jueces)."))}

{unidad("3.5 Incompatibilidades y asociación profesional (art. 127)",
  lit("CE", "Artículo 127", ["no podrán desempeñar otros cargos públicos, ni pertenecer a partidos políticos o sindicatos", "asociación profesional", "total independencia"]),
  fichab("Límites del estatuto de jueces y fiscales en activo", "Jueces, Magistrados y **Fiscales**, mientras estén **en activo**",
         ["No pueden desempeñar otros cargos públicos", "No pueden pertenecer a **partidos políticos** ni **sindicatos**", "La ley regula su **asociación profesional** y el régimen de incompatibilidades"],
         "—",
         "Pueden **asociarse profesionalmente**, pero no afiliarse a partidos ni sindicatos. La prohibición alcanza también a los **Fiscales**."))}

{resumen([
  "La justicia **emana del pueblo** y se administra **en nombre del Rey** por jueces **independientes, inamovibles, responsables y sometidos únicamente al imperio de la ley** (117.1).",
  "Potestad jurisdiccional: **juzgar y hacer ejecutar lo juzgado**, **exclusivamente** por los Juzgados y Tribunales (117.3).",
  "Actuaciones **públicas**, procedimiento **predominantemente oral**, sentencias **siempre motivadas** (120); inhábiles **agosto** y del **24 de diciembre al 6 de enero** (LOPJ 183).",
  "Ministerio Fiscal: **unidad de actuación y dependencia jerárquica**, **legalidad e imparcialidad**; FGE nombrado por el **Rey** a propuesta del **Gobierno**, oído el **CGPJ** (124)."],
  "Siguiente: II. ¿Qué significa el principio de unidad jurisdiccional?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Qué significa el principio de unidad jurisdiccional? (art. 117.5 y 6 CE; LOPJ, arts. 3, 4 y 9)", donde(
  "Segunda pregunta. Ya sabemos quién administra la justicia; ahora, **cuántas jurisdicciones** hay. La Constitución responde con el **principio de unidad jurisdiccional**: una sola jurisdicción, con la única especialidad de la **militar** y la prohibición de **Tribunales de excepción**.",
  ["1 Unidad jurisdiccional, jurisdicción militar y prohibición de Tribunales de excepción (art. 117.5 y 6; LOPJ, art. 3)", "2 Extensión de la jurisdicción y órdenes jurisdiccionales (LOPJ, arts. 4 y 9)"]))

T.ap("s4", "II.1 Unidad jurisdiccional, jurisdicción militar y prohibición de Tribunales de excepción (art. 117.5 y 6; LOPJ, art. 3)", f"""
{unidad("1.1 El principio y la jurisdicción militar (art. 117.5)",
  lit("CE", "Artículo 117", ["El principio de unidad jurisdiccional es la base de la organización y funcionamiento de los Tribunales", "en el ámbito estrictamente castrense y en los supuestos de estado de sitio"], solo=[5]),
  fichab("Una sola jurisdicción como base de la organización y funcionamiento de los Tribunales",
         "Todos los Tribunales; la jurisdicción militar, según la ley",
         ["Unidad jurisdiccional: **base** de la organización y funcionamiento de los Tribunales", "Jurisdicción militar: solo en el ámbito **estrictamente castrense** y en los supuestos de **estado de sitio**, de acuerdo con los principios de la Constitución"],
         "—",
         "La jurisdicción militar no rompe la unidad: es la única excepción que menciona el 117.5, y con **dos** ámbitos tasados (castrense y estado de **sitio**, no de alarma ni de excepción)."))}

{unidad("1.2 Prohibición de los Tribunales de excepción (art. 117.6)",
  lit("CE", "Artículo 117", ["Se prohíben los Tribunales de excepción"], solo=[6]),
  fichab("Garantía del juez ordinario", "—", "Prohibición absoluta de Tribunales de excepción", "—",
         "Es una prohibición **sin excepciones**: la Constitución no prevé ningún supuesto en que puedan crearse."))}

{unidad("1.3 La jurisdicción es única (LOPJ, art. 3)",
  lit(L, "atercero", ["La jurisdicción es única", "sin perjuicio de las potestades jurisdiccionales reconocidas por la Constitución a otros órganos", "integrante del Poder Judicial del Estado", "en el ámbito estrictamente castrense y, en su caso, en las materias que establezca la declaración del estado de sitio"]),
  fichab("Desarrollo legal del principio de unidad",
         ["Jueces, juezas y Tribunales previstos en la LOPJ", "Órganos de la **jurisdicción militar**, **integrante del Poder Judicial del Estado**"],
         ["Jurisdicción **única** (3.1)", "Salvo las potestades jurisdiccionales que la **Constitución** reconoce **a otros órganos** (3.1)", "La jurisdicción militar se basa **en el principio de unidad jurisdiccional** (3.2)"],
         "—",
         "Cayó en 2025 (→ Cierre 1): la jurisdicción militar actúa en el ámbito **estrictamente castrense** y, en su caso, en las materias de la declaración del **estado de sitio**; no en todo lo que afecte a militares."))}

{unidad("1.4 Otras potestades jurisdiccionales que reconoce la Constitución (art. 136.2 CE y esquema)",
  lit("CE", "Artículo 136", ["sin perjuicio de su propia jurisdicción"], solo=[3, 4], titulo="Artículo 136.2"),
  fichab("Potestades jurisdiccionales reconocidas por la Constitución a otros órganos (art. 3.1 LOPJ)", "—",
         "Las que la Constitución menciona expresamente: la «propia jurisdicción» del Tribunal de Cuentas (136.2) y los Tribunales consuetudinarios y tradicionales (125; → I.3.3). Cuadro de abajo", "—",
         "La Constitución regula el Tribunal Constitucional aparte, en su Título IX (tema I.3), no en el Título VI."),
  "*Esquema de elaboración propia: recoge las menciones literales de la Constitución a funciones jurisdiccionales fuera de los Juzgados y Tribunales; no es texto legal.*",
  TAB1)}
""", 2)

T.ap("s5", "II.2 Extensión de la jurisdicción y órdenes jurisdiccionales (LOPJ, arts. 4 y 9)", f"""
{unidad("2.1 Extensión de la jurisdicción (LOPJ, art. 4)",
  lit(L, "acuarto", ["a todas las personas, a todas las materias y a todo el territorio español"]),
  fichab("Alcance de la jurisdicción", "—", "Todas las personas, todas las materias y todo el territorio español", "—",
         "Tres «todas»: **personas**, **materias** y **territorio**, en la forma de la Constitución y las leyes."))}

{unidad("2.2 Los órdenes jurisdiccionales y la improrrogabilidad (LOPJ, art. 9)",
  lit(L, "anoveno", ["exclusivamente en aquellos casos en que les venga atribuida por esta u otra ley", "de todas aquellas que no estén atribuidas a otro orden jurisdiccional", "las causas y juicios criminales", "sujeta al derecho administrativo", "dentro de la rama social del derecho", "La jurisdicción es improrrogable"], solo=list(range(1, 10))),
  fichab("Reparto de la jurisdicción única en cuatro órdenes",
         ["Civil (9.2)", "Penal (9.3)", "Contencioso-administrativo (9.4; tema IV.13)", "Social (9.5)"],
         ["El **civil** es el orden **residual**: conoce de lo suyo y de lo no atribuido a otro orden", "Penal: causas y juicios criminales, salvo los de la jurisdicción militar", "Contencioso: actuación de las Administraciones sujeta al derecho administrativo, reglamentos y decretos legislativos (82.6 CE)", "Social: rama social del derecho, conflictos individuales y colectivos y Seguridad Social"],
         "La falta de jurisdicción se aprecia **de oficio**, con audiencia de las partes y del Ministerio Fiscal",
         "Orden **residual** = **civil** (no el contencioso). La jurisdicción es **improrrogable** y la resolución que aprecia su falta indica siempre el orden competente."))}

{unidad("2.3 Cuadro de los órdenes jurisdiccionales (esquema)",
  "*Esquema de elaboración propia: resume el art. 9 LOPJ; no es texto legal.*",
  TAB2)}

{resumen([
  "El **principio de unidad jurisdiccional** es la **base** de la organización y funcionamiento de los Tribunales (117.5).",
  "Jurisdicción **militar**: integrante del Poder Judicial; ámbito **estrictamente castrense** y **estado de sitio** (117.5; LOPJ 3.2).",
  "**Se prohíben** los Tribunales de excepción (117.6).",
  "Jurisdicción **única** (LOPJ 3.1) que se extiende a **todas** las personas, materias y territorio (art. 4) y se reparte en **cuatro** órdenes; el **civil** es el residual; es **improrrogable** (art. 9)."],
  "Siguiente: III. ¿Qué es el Consejo General del Poder Judicial, cómo se compone y qué hace?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Qué es el Consejo General del Poder Judicial, cómo se compone y qué hace? (arts. 122 y 123.2 CE; LOPJ, Libro VIII)", donde(
  "Tercera pregunta. Los jueces son independientes al juzgar, pero alguien tiene que **gobernar** el Poder Judicial: nombramientos, ascensos, inspección, disciplina. La Constitución lo encarga al **Consejo General del Poder Judicial**, no al Gobierno.",
  ["1 Naturaleza y atribuciones (art. 122.2; LOPJ, arts. 558, 560 y 561)", "2 Composición y designación de los Vocales (art. 122.3; LOPJ, arts. 566 a 570 bis y 578)", "3 Estatuto de los Vocales (LOPJ, arts. 579, 581 y 582)", "4 El Presidente y el Vicepresidente (art. 123.2; LOPJ, arts. 585 a 587 y 589)", "5 Órganos del Consejo y recursos contra sus actos (LOPJ, arts. 595, 599 a 604, 609, 610 y 638)"]))

T.ap("s6", "III.1 Naturaleza y atribuciones (art. 122.2; LOPJ, arts. 558, 560 y 561)", f"""
{unidad("1.1 Órgano de gobierno del Poder Judicial (art. 122.2)",
  lit("CE", "Artículo 122", ["El Consejo General del Poder Judicial es el órgano de gobierno del mismo", "en particular en materia de nombramientos, ascensos, inspección y régimen disciplinario"], solo=[2]),
  fichab("Órgano de gobierno del Poder Judicial", "El Consejo General del Poder Judicial (CGPJ)",
         ["La ley orgánica fija su estatuto, el régimen de incompatibilidades de sus miembros y sus funciones", "En particular: **nombramientos**, **ascensos**, **inspección** y **régimen disciplinario**"],
         "Ley **orgánica**",
         "Es órgano de **gobierno** del Poder Judicial, no órgano jurisdiccional: no juzga. Las **cuatro** materias del 122.2 se preguntan."))}

{unidad("1.2 Ámbito y sede (LOPJ, art. 558)",
  lit(L, "aquinientoscincuentayocho", ["en todo el territorio nacional", "tiene su sede en la villa de Madrid"]),
  fichab("Ámbito territorial y sede", "El CGPJ", "Ejerce sus competencias en **todo el territorio nacional**", "—", "Sede: **villa de Madrid**."))}

{unidad("1.3 Atribuciones (LOPJ, art. 560.1, 1.ª a 9.ª y 16.ª)",
  lit(L, "aquinientossesenta", ["Proponer el nombramiento, en los términos previstos por la presente Ley Orgánica, de dos Magistrados del Tribunal Constitucional", "Ser oído por el Gobierno antes del nombramiento del Fiscal General del Estado", "Interponer el conflicto de atribuciones entre órganos constitucionales del Estado", "Ejercer la alta inspección de Tribunales"], solo=list(range(1, 11)) + list(range(18, 33)), titulo="Artículo 560 (LOPJ), apartado 1, atribuciones 1.ª a 9.ª y 16.ª (fragmento)"),
  fichab("Qué hace el CGPJ (selección de las 25 atribuciones del art. 560.1)", "El CGPJ",
         ["Propone el nombramiento del **Presidente del TS y del CGPJ**, de Jueces y Magistrados y de **dos Magistrados del TC**", "Es **oído** antes del nombramiento del **Fiscal General del Estado**", "Interpone el **conflicto de atribuciones** entre órganos constitucionales", "Formación, destinos, ascensos, situaciones y **régimen disciplinario** de los jueces; **alta inspección** de Tribunales", f"Potestad reglamentaria {c(L, 'aquinientossesenta', 'en el marco estricto de desarrollo de las previsiones de la Ley Orgánica del Poder Judicial')} (16.ª)"],
         "—",
         f"Sus reglamentos nunca pueden {c(L, 'aquinientossesenta', 'afectar o regular directa o indirectamente los derechos y deberes de personas ajenas al mismo')}. Propone **dos** Magistrados del TC (art. 159.1 CE, tema I.3)."))}

{unidad("1.4 Informes sobre anteproyectos (LOPJ, art. 561)",
  lit(L, "aquinientossesentayuno", ["Modificaciones de la Ley Orgánica del Poder Judicial", "Leyes penales y normas sobre régimen penitenciario", "en el plazo improrrogable de treinta días", "el plazo será de quince días", "se tendrá por cumplido dicho trámite"], solo=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
  fichab("Función consultiva sobre normas que afectan a la Justicia", "El CGPJ (lo aprueba el Pleno: art. 599.1.12.ª)",
         "Informa los **anteproyectos de ley y disposiciones generales** de las materias tasadas (LOPJ, demarcación, plantilla, estatutos, normas procesales, organización de los Tribunales, leyes penales y penitenciarias, y otras que se estimen oportunas)",
         ["**30 días**, improrrogable; **15** si es urgente", "Prórroga excepcional: **15 días** (o **10** si es urgente)", "Sin informe en plazo: **se tiene por cumplido** el trámite"],
         "Informe en **30** días (**15** urgente). Si no lo emite, el trámite **se tiene por cumplido**."))}
""", 2)

T.ap("s7", "III.2 Composición y designación de los Vocales (art. 122.3; LOPJ, arts. 566 a 570 bis y 578)", f"""
{unidad("2.1 Composición constitucional (art. 122.3)",
  lit("CE", "Artículo 122", ["por veinte miembros nombrados por el Rey por un período de cinco años", "doce entre Jueces y Magistrados de todas las categorías judiciales", "cuatro a propuesta del Congreso de los Diputados, y cuatro a propuesta del Senado, elegidos en ambos casos por mayoría de tres quintos de sus miembros", "con más de quince años de ejercicio en su profesión"], solo=[3]),
  fichab("Quiénes forman el CGPJ",
         ["El **Presidente del Tribunal Supremo**, que lo preside", "**Veinte** miembros nombrados por el **Rey** por **cinco años**"],
         ["**12** entre Jueces y Magistrados de todas las categorías, en los términos de la ley orgánica", "**4** a propuesta del **Congreso** y **4** a propuesta del **Senado**, entre abogados y otros juristas de reconocida competencia"],
         "Congreso y Senado: **tres quintos** de sus miembros · juristas: **más de 15 años** de ejercicio · mandato: **5 años**",
         "**20 + Presidente**. Los 8 juristas: 4 + 4, por **tres quintos**. No confundir con el **TC** (12 miembros, 9 años)."))}

{unidad("2.2 Composición legal y designación por las Cámaras (LOPJ, arts. 566 y 567)",
  lit(L, "aquinientossesentayseis", ["doce serán Jueces o Magistrados en servicio activo en la carrera judicial y ocho juristas de reconocida competencia"]),
  lit(L, "aquinientossesentaysiete", ["serán designadas por las Cortes Generales", "Cada una de las Cámaras elegirá, por mayoría de tres quintos de sus miembros, a diez Vocales", "como mínimo un cuarenta por ciento de cada uno de los sexos", "comparecer ante la Comisión de nombramientos", "Las Cámaras designarán un suplente por cada uno de los vocales titulares", "En ningún caso podrá recaer la designación de Vocales del Consejo General del Poder Judicial en Vocales del Consejo saliente"], solo=[1, 2, 3, 4, 5, 6, 7, 8]),
  fichab("Cómo se designan los veinte Vocales",
         "Las **Cortes Generales**: cada Cámara elige **diez** Vocales",
         ["Por Cámara: **4** juristas (más de 15 años de experiencia) + **6** del turno judicial", "Comparecencia previa ante la **Comisión de nombramientos**, en audiencia pública", "Un **suplente** por cada titular", "Juristas: no pueden serlo los jueces en activo (salvo otra situación al menos el año anterior) ni, en los **cinco años** anteriores, ministros, secretarios de Estado, consejeros autonómicos, presidentes de corporación local o parlamentarios"],
         "**Tres quintos** de cada Cámara · al menos **40 %** de cada sexo entre los diez de cada Cámara",
         "Los **doce** del turno judicial también los eligen **las Cámaras** (6 + 6), entre candidatos avalados (art. 574). Nunca pueden ser Vocales los del **Consejo saliente**."))}

{unidad("2.3 Proporción del turno judicial (LOPJ, art. 578.3)",
  lit(L, "aquinientossetentayocho", ["tres Magistrados del Tribunal Supremo; tres Magistrados con más de veinticinco años de antigüedad en la carrera judicial y seis Jueces o Magistrados sin sujeción a antigüedad"], solo=[3]),
  fichab("Reparto mínimo de los doce Vocales judiciales", "Las Cámaras, al designarlos",
         ["**3** Magistrados del Tribunal Supremo", "**3** Magistrados con más de **25 años** de antigüedad", "**6** Jueces o Magistrados sin sujeción a antigüedad"],
         "—", "3 + 3 + 6 = 12. Si falta candidato en una categoría, la vacante **acrece** la siguiente."))}

{unidad("2.4 Renovación, nombramiento y constitución (LOPJ, arts. 568 y 569)",
  lit(L, "aquinientossesentayocho", ["se renovará en su totalidad cada cinco años", "cuatro meses antes de la expiración del mencionado plazo"], solo=[1, 2, 3, 4]),
  lit(L, "aquinientossesentaynueve", ["nombrados por el Rey mediante Real Decreto", "dentro de los cinco días posteriores a la expiración del anterior Consejo"]),
  fichab("Renovación del Consejo", ["Presidentes del Congreso y del Senado: adoptan las medidas para la renovación en plazo", "El **Rey** nombra a los Vocales por **Real Decreto**"],
         "Renovación **total** cada cinco años desde su constitución; juramento o promesa ante el Rey y sesión constitutiva",
         ["Cada **5 años**, desde la constitución", "Inicio del proceso: **4 meses** antes de expirar el plazo", "Toma de posesión y sesión constitutiva: en los **5 días** posteriores a la expiración del anterior Consejo"],
         "Renovación **en su totalidad** (no por mitades ni por tercios, como el TC)."))}

{unidad("2.5 Si las Cámaras no designan a tiempo: el Consejo en funciones (LOPJ, arts. 570 y 570 bis)",
  lit(L, "aquinientossetenta", ["con los diez Vocales designados por la otra Cámara", "el Consejo saliente continuará en funciones hasta la toma de posesión del nuevo"], solo=[1, 2]),
  lit(L, "aq", ["la actividad del mismo se limitará a la realización de las siguientes atribuciones", "Proponer el nombramiento de dos Magistrados del Tribunal Constitucional"], solo=[1, 2, 3, 4]),
  fichab("Régimen del CGPJ cuando no se renueva en plazo", "Consejo saliente, en funciones",
         ["Si falta una sola Cámara: se constituye con los **10** Vocales de la otra y los salientes de la Cámara incumplidora (570.1)", "Si faltan las dos: el Consejo saliente sigue **en funciones** y **no** puede elegirse nuevo Presidente (570.2)", "En funciones, solo las atribuciones tasadas del art. 570 bis (entre ellas, proponer **dos Magistrados del TC** y ser oído sobre el **FGE**)"],
         "—",
         "En funciones **no** hace nombramientos discrecionales del art. 560.1.2.ª: la lista del 570 bis es **cerrada**, más lo indispensable para su funcionamiento ordinario."))}
""", 2)

T.ap("s8", "III.3 Estatuto de los Vocales (LOPJ, arts. 579, 581 y 582)", f"""
{unidad("3.1 Dedicación exclusiva e incompatibilidades (LOPJ, art. 579.1 y 2)",
  lit(L, "aquinientossetentaynueve", ["con dedicación exclusiva", "a excepción de la mera administración del patrimonio personal o familiar", "será la de servicios especiales"], solo=[1, 2]),
  fichab("Régimen de los Vocales", "Vocales del CGPJ",
         ["**Dedicación exclusiva**: incompatibles con cualquier otro puesto, profesión o actividad, salvo la administración del patrimonio personal o familiar", "Se les aplican además las incompatibilidades de los jueces (art. 389)", "Funcionarios: situación de **servicios especiales**"],
         "—", "Situación administrativa: **servicios especiales** (no excedencia)."))}

{unidad("3.2 Sin mandato imperativo (LOPJ, art. 581)",
  lit(L, "aquinientosochentayuno", ["no estarán ligados por mandato imperativo"]),
  fichab("Independencia de los Vocales respecto de quien los designa", "Vocales del CGPJ", "No están ligados por mandato imperativo", "—",
         "Aunque los designen las Cámaras, **no** reciben instrucciones de ellas."))}

{unidad("3.3 Cese (LOPJ, art. 582)",
  lit(L, "aquinientosochentaydos", ["por el transcurso de los cinco años para los que fueron nombrados", "renuncia aceptada por el Presidente", "mediante mayoría de tres quintos"]),
  fichab("Causas tasadas de cese de los Vocales", "Pleno del CGPJ (aprecia incapacidad, incompatibilidad o incumplimiento grave); el Presidente acepta la renuncia",
         ["Transcurso de los **cinco años**", "**Renuncia** aceptada por el Presidente", "**Incapacidad**, **incompatibilidad** o **incumplimiento grave** de los deberes del cargo", "Vocales judiciales: dejar el servicio activo o la carrera judicial (salvo servicios especiales)"],
         "Pleno: **tres quintos**",
         f"Cesan {c(L, 'aquinientosochentaydos', 'sólo')} por estas causas; la incapacidad, incompatibilidad o incumplimiento la aprecia el **Pleno** por **tres quintos**."))}
""", 2)

T.ap("s9", "III.4 El Presidente y el Vicepresidente (art. 123.2; LOPJ, arts. 585 a 587 y 589)", f"""
{unidad("4.1 Nombramiento del Presidente del Tribunal Supremo (art. 123.2)",
  lit("CE", "Artículo 123", ["será nombrado por el Rey, a propuesta del Consejo General del Poder Judicial"], solo=[2]),
  fichab("Nombramiento del Presidente del TS", "El **Rey**, a propuesta del **CGPJ**", "En la forma que determine la ley", "—",
         "Propone el **CGPJ** (no el Gobierno). Es a la vez Presidente del **CGPJ** (art. 122.3)."))}

{unidad("4.2 Primera autoridad judicial (LOPJ, art. 585)",
  lit(L, "aquinientosochentaycinco", ["es la primera autoridad judicial de la Nación"]),
  fichab("Posición del Presidente", "Presidente del TS y del CGPJ", "Ostenta la representación del Poder Judicial y del CGPJ", "—", "**Primera autoridad judicial de la Nación**."))}

{unidad("4.3 Requisitos y elección (LOPJ, art. 586)",
  lit(L, "aquinientosochentayseis", ["con más de veinticinco años de antigüedad en el ejercicio de su profesión", "sin que cada Vocal pueda proponer más de un nombre", "entre tres y siete días más tarde", "mayoría de tres quintos de los miembros del Pleno", "refrendado por el Presidente del Gobierno"]),
  fichab("Elección del Presidente del TS y del CGPJ",
         ["Elige el **Pleno** del CGPJ; nombra el **Rey** por Real Decreto refrendado por el **Presidente del Gobierno**", "Candidatos: Magistrado del TS con requisitos para ser Presidente de Sala, o **jurista** de reconocida competencia con más de **25 años**"],
         ["Candidaturas en la sesión constitutiva (presidida por el Vocal **de más edad**); cada Vocal propone **un solo** nombre", "Votación **nominal** en sesión entre **3 y 7 días** después", "Juramento o promesa ante el Rey; posesión ante el **Pleno del TS**"],
         "**Tres quintos** de los miembros del Pleno",
         "Puede ser Presidente un **jurista no juez** con más de **25** años de ejercicio (los Vocales juristas: más de **15**)."))}

{unidad("4.4 Mandato (LOPJ, art. 587)",
  lit(L, "aquinientosochentaysiete", ["coincidirá con la del Consejo que lo haya elegido", "por una sola vez"]),
  fichab("Duración del mandato del Presidente", "Presidente del TS y del CGPJ", "El de su Consejo", "Reelección **una sola vez**",
         "Su mandato **coincide** con el del Consejo (cinco años) y solo cabe **una** reelección."))}

{unidad("4.5 El Vicepresidente del Tribunal Supremo (LOPJ, art. 589)",
  lit(L, "aquinientosochentaynueve", ["por mayoría de tres quintos del Pleno del Consejo General del Poder Judicial, a propuesta del Presidente", "al menos con siete días de antelación"], solo=[1, 2, 3]),
  fichab("Elección del Vicepresidente del TS", "Pleno del CGPJ, a propuesta del Presidente",
         "En el primer Pleno ordinario tras la elección del Presidente; propuesta comunicada a los Vocales con **7 días** de antelación y hecha pública",
         "**Tres quintos** del Pleno; cese por causa justificada, también por **tres quintos**",
         "Debe ser **Magistrado del TS** en servicio activo con requisitos para ser Presidente de Sala."))}
""", 2)

T.ap("s10", "III.5 Órganos del Consejo y recursos contra sus actos (LOPJ, arts. 595, 599 a 604, 609, 610 y 638)", f"""
{unidad("5.1 Pleno y Comisiones (LOPJ, art. 595)",
  lit(L, "aquinientosnoventaycinco", ["en Pleno o a través de las Comisiones", "Permanente, de Calificación, Disciplinaria, de Asuntos Económicos, de Igualdad y de Supervisión y Control de Protección de Datos"]),
  fichab("Cómo actúa el CGPJ", "Presidencia, Pleno y Comisiones",
         ["::Seis Comisiones:", "Permanente", "De Calificación", "Disciplinaria", "De Asuntos Económicos", "De Igualdad", "De Supervisión y Control de Protección de Datos"],
         "—", "Son **seis** Comisiones legales; el Pleno puede crear otras por **tres quintos** (art. 599.3)."))}

{unidad("5.2 El Pleno (LOPJ, arts. 599.1 y 600)",
  lit(L, "aquinientosnoventaynueve", ["por mayoría de tres quintos, de los dos Magistrados del Tribunal Constitucional", "en el plazo máximo de tres meses", "Todos los nombramientos o propuestas de nombramientos y promociones que impliquen algún margen de discrecionalidad o apreciación de méritos", "La aprobación de la Memoria anual"], solo=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], titulo="Artículo 599.1 (LOPJ). Competencias del Pleno"),
  lit(L, "aseiscientos", ["una vez al mes", "si lo solicitaren cinco Vocales", "al menos la presencia de doce de sus miembros", "la presencia de diez Vocales y el Presidente"]),
  fichab("Órgano principal del CGPJ", "Presidente y los veinte Vocales",
         ["Propone por **tres quintos** a los **dos** Magistrados del TC (en **tres meses** desde que vence el mandato anterior)", "Propone al Presidente del TS y del CGPJ e informa sobre el **FGE**", "Nombramientos **discrecionales**", "Reglamentos, presupuesto, **Memoria anual**, separación de jueces, alzadas contra la Disciplinaria y la Permanente, informes sobre anteproyectos"],
         ["Sesión ordinaria: **una vez al mes**", "Extraordinaria: si lo decide el Presidente o lo piden **cinco** Vocales", "Quórum para elegir Presidente: **doce** miembros; en los demás casos, **diez Vocales y el Presidente**"],
         "Quórum: **12** para elegir Presidente; **10 + Presidente** en lo demás. Sesión ordinaria **mensual**."))}

{unidad("5.3 La Comisión Permanente (LOPJ, arts. 601 y 602)",
  lit(L, "aseiscientosuno", ["elegirá anualmente", "otros siete Vocales: cuatro de los nombrados por el turno judicial y tres de los designados por el turno de juristas de reconocida competencia"], solo=[1, 2]),
  lit(L, "aseiscientosdos", ["Preparar las sesiones del Pleno", "por tener carácter íntegramente reglado", "recurribles en alzada ante el Pleno"], solo=[1, 2, 3, 4, 10]),
  fichab("Comisión que prepara y ejecuta los acuerdos del Pleno",
         "Presidente + **7** Vocales (4 judiciales y 3 juristas), elegidos **anualmente** por el Pleno",
         ["Prepara las sesiones del Pleno y vela por la ejecución de sus acuerdos", "Nombramientos **íntegramente reglados**, jubilación forzosa por edad y situaciones administrativas de jueces"],
         "Renovación **anual**",
         "Nombramientos **reglados** → Permanente; **discrecionales** → Pleno. Sus acuerdos: **alzada ante el Pleno**."))}

{unidad("5.4 La Comisión Disciplinaria (LOPJ, arts. 603 y 604)",
  lit(L, "aseiscientostres", ["será de cinco años", "siete Vocales: cuatro del turno judicial y tres del turno de juristas de reconocida competencia"], solo=[1, 2]),
  lit(L, "aseiscientoscuatro", ["infracciones graves y muy graves", "con la sola excepción de aquellos supuestos en que la sanción propuesta fuere de separación del servicio", "en el plazo de un mes, en alzada ante el Pleno"], solo=[1, 2]),
  fichab("Comisión que sanciona a Jueces y Magistrados", "**7** Vocales (4 judiciales y 3 juristas), elegidos por el Pleno para **cinco años**",
         "Resuelve los expedientes por infracciones **graves y muy graves**, salvo si se propone la **separación** (la decide el Pleno: art. 599.1.10.ª)",
         "Mandato: **5 años** · alzada ante el Pleno: **1 mes**",
         "La Permanente se renueva **cada año**; la Disciplinaria tiene mandato de **cinco años**. La **separación** la acuerda el **Pleno**."))}

{unidad("5.5 Comisiones de Asuntos Económicos y de Igualdad (LOPJ, arts. 609 y 610)",
  lit(L, "aseiscientosnueve", ["integrada por tres Vocales"], solo=[2]),
  lit(L, "aseiscientosdiez", ["integrada por tres Vocales"], solo=[2]),
  fichab("Otras Comisiones", "Tres Vocales cada una, elegidos anualmente por el Pleno",
         ["Asuntos Económicos: estudios económicos y control de la actividad financiera y contable de la gerencia", "Igualdad: asesora al Pleno sobre igualdad entre mujeres y hombres e informes de impacto de género de los reglamentos"],
         "—", "**Tres** Vocales cada una (la Permanente y la Disciplinaria, **siete**)."))}

{unidad("5.6 Recursos contra los acuerdos del Pleno y de la Comisión Permanente (LOPJ, art. 638.2)",
  lit(L, "aseiscientostreintayocho", ["pondrán fin a la vía administrativa", "recurribles ante la Sala de lo Contencioso-Administrativo del Tribunal Supremo"], solo=[2]),
  fichab("Control judicial de los actos del CGPJ", "Sala de lo Contencioso-Administrativo del **Tribunal Supremo** (una sección especial)",
         "Los acuerdos del Pleno y de la Permanente **agotan la vía administrativa** y se recurren ante la Sala Tercera del TS", "—",
         "Va al **Tribunal Supremo** (no a la Audiencia Nacional ni al TSJ de Madrid)."))}

{unidad("5.7 Cuadro de los órganos del CGPJ (esquema)",
  "*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*",
  TAB3)}

{resumen([
  "El CGPJ es el **órgano de gobierno** del Poder Judicial: nombramientos, ascensos, inspección y régimen disciplinario (122.2).",
  "**Presidente del TS** + **20 Vocales** nombrados por el **Rey** por **5 años**: 12 judiciales y 8 juristas (122.3); cada Cámara elige **10** por **tres quintos** (LOPJ 567).",
  "Presidente del TS y del CGPJ: lo elige el Pleno por **tres quintos**; lo nombra el **Rey**; reelegible **una vez** (586 y 587).",
  "Pleno (discrecionales), Permanente (reglados), Disciplinaria (graves y muy graves, salvo separación); sus acuerdos, ante la Sala Tercera del **TS** (638)."],
  "Siguiente: IV. ¿Cómo se organizan los Juzgados y Tribunales?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Cómo se organizan los Juzgados y Tribunales? (LOPJ, arts. 26, 29, 30, 32 a 34, 53 a 59, 61, 62 a 66, 70 a 74, 80 a 82, 84, 95, 99 a 102 y 439 ter; LO 1/2025)", donde(
  "Cuarta pregunta. La **organización judicial española** es la **planta** de órganos que ejercen la potestad jurisdiccional y su reparto por el **territorio**. Tras la LO 1/2025, los antiguos Juzgados se han transformado en **Tribunales de Instancia**.",
  ["1 Los órganos y el territorio (LOPJ, arts. 26, 29, 30 y 32 a 34)", "2 El Tribunal Supremo (art. 123.1 CE; LOPJ, arts. 53 a 59 y 61)", "3 La Audiencia Nacional (LOPJ, arts. 62 a 66)", "4 Los Tribunales Superiores de Justicia (art. 152.1 CE; LOPJ, arts. 70 a 74)", "5 Las Audiencias Provinciales (LOPJ, arts. 80 a 82)", "6 Los Tribunales de Instancia y el Tribunal Central de Instancia (LOPJ, arts. 84 y 95; LO 1/2025)", "7 Jueces de paz y Oficinas de Justicia en los municipios (LOPJ, arts. 99 a 102 y 439 ter)", "8 Cuadro de la organización judicial"]))

T.ap("s11", "IV.1 Los órganos y el territorio (LOPJ, arts. 26, 29, 30 y 32 a 34)", f"""
{unidad("1.1 Órganos que ejercen la potestad jurisdiccional (LOPJ, art. 26)",
  lit(L, "aveintiseis", ["Jueces y juezas de paz", "Tribunales de Instancia", "Tribunal Central de Instancia"]),
  fichab("Planta de la organización judicial",
         ["::Siete clases de órganos:", "Jueces y juezas de paz", "Tribunales de Instancia", "Audiencias Provinciales", "Tribunales Superiores de Justicia", "Tribunal Central de Instancia", "Audiencia Nacional", "Tribunal Supremo"],
         "—", "—",
         "Lista vigente tras la LO 1/2025: ya **no** aparecen los Juzgados de Primera Instancia, de Instrucción, de lo Penal, etc., ni los Juzgados Centrales."))}

{unidad("1.2 Planta y organización territorial (LOPJ, arts. 29 y 30)",
  lit(L, "aveintinueve", ["La planta de los tribunales se establecerá por ley", "al menos, cada cinco años"], solo=[1]),
  lit(L, "atreinta", ["en Municipios, Partidos, Provincias y Comunidades Autónomas"]),
  fichab("Planta y demarcación", "Las Cortes (planta por **ley**), previo informe del **CGPJ** para su revisión",
         "El Estado se organiza judicialmente en **municipios, partidos, provincias y Comunidades Autónomas**",
         "Revisión de la planta: al menos **cada cinco años**",
         "**Cuatro** demarcaciones. El **partido judicial** es la propia de los Tribunales de Instancia (→ IV.6)."))}

{unidad("1.3 El partido judicial, la provincia y la Comunidad Autónoma (LOPJ, arts. 32 a 34)",
  lit(L, "atreintaydos", ["uno o más municipios limítrofes, pertenecientes a una misma provincia", "podrá coincidir con la demarcación provincial"]),
  lit(L, "atreintaytres", ["La provincia se ajustará a los límites territoriales"]),
  lit(L, "atreintaycuatro", ["será el ámbito territorial de los Tribunales Superiores de Justicia"]),
  fichab("Las demarcaciones judiciales", "—",
         ["Partido: uno o más municipios **limítrofes** de una **misma provincia**", "Provincia: los límites de la provincia administrativa", "Comunidad Autónoma: ámbito de los **TSJ**"],
         "—", "El partido nunca abarca municipios de **provincias distintas**; sí puede **coincidir** con la provincia."))}
""", 2)

T.ap("s12", "IV.2 El Tribunal Supremo (art. 123.1 CE; LOPJ, arts. 53 a 59 y 61)", f"""
{unidad("2.1 Órgano jurisdiccional superior (art. 123.1 CE; LOPJ, art. 53)",
  lit("CE", "Artículo 123", ["con jurisdicción en toda España, es el órgano jurisdiccional superior en todos los órdenes, salvo lo dispuesto en materia de garantías constitucionales"], solo=[1]),
  lit(L, "acincuentaytres", ["con sede en la villa de Madrid", "ningún otro podrá tener el título de Supremo"]),
  fichab("Cúspide de la organización judicial", "Tribunal Supremo, con sede en **Madrid**",
         "Órgano jurisdiccional **superior en todos los órdenes**, con jurisdicción en toda España",
         "—",
         "Salvo en **garantías constitucionales** (que corresponden al TC). **Ningún otro** órgano puede llamarse «Supremo»."))}

{unidad("2.2 Composición y Salas (LOPJ, arts. 54 y 55)",
  lit(L, "acincuentaycuatro", ["de su Presidente, de los Presidentes de Sala y los Magistrados que determine la ley"]),
  lit(L, "acincuentaycinco", ["Primera: De lo Civil.", "Segunda: De lo Penal.", "Tercera: De lo Contencioso-Administrativo.", "Cuarta: De lo Social.", "Quinta: De lo Militar"]),
  fichab("Estructura del Tribunal Supremo", "Presidente, Presidentes de Sala y Magistrados",
         ["Sala **Primera**: Civil", "Sala **Segunda**: Penal", "Sala **Tercera**: Contencioso-Administrativa", "Sala **Cuarta**: Social", "Sala **Quinta**: Militar (con su legislación específica)"],
         "—", "Numeración fija: **1.ª Civil, 2.ª Penal, 3.ª Contencioso, 4.ª Social, 5.ª Militar**."))}

{unidad("2.3 Qué conoce cada Sala (LOPJ, arts. 56 a 59 y 61; fragmentos)",
  lit(L, "acincuentayseis", ["De los recursos de casación, revisión y otros extraordinarios en materia civil que establezca la ley"], solo=[1, 2], titulo="Artículo 56 (LOPJ), fragmento"),
  lit(L, "acincuentaysiete", ["De los recursos de casación, revisión y otros extraordinarios en materia penal que establezca la ley", "De la instrucción y enjuiciamiento de las causas contra"], solo=[1, 2, 3, 4], titulo="Artículo 57.1 (LOPJ), fragmento"),
  lit(L, "acincuentayocho", ["En única instancia, de los recursos contencioso-administrativos contra actos y disposiciones del Consejo de Ministros, de las Comisiones Delegadas del Gobierno y del Consejo General del Poder Judicial"], solo=[1, 2, 3], titulo="Artículo 58 (LOPJ), fragmento"),
  lit(L, "acincuentaynueve", ["de los recursos de casación y revisión y otros extraordinarios que establezca la ley en materias propias de este orden jurisdiccional"]),
  lit(L, "asesentayuno", ["el Presidente del Tribunal Supremo, los Presidentes de Sala y el Magistrado más antiguo y el más moderno de cada una de ellas", "De los procesos de declaración de ilegalidad y consecuente disolución de los partidos políticos"], solo=[1, 7], titulo="Artículo 61.1 (LOPJ), fragmento"),
  fichab("Reparto de asuntos entre las Salas del TS", "Cada Sala en su orden; la Sala del art. 61 en asuntos especiales",
         "Sobre todo, recursos de **casación** y **revisión**; en única instancia, los asuntos de aforados y del Consejo de Ministros", "—",
         "Los recursos contra el **Consejo de Ministros** y el **CGPJ** van a la **Sala Tercera** en única instancia. La ilegalización de partidos, a la **Sala del 61**."))}
""", 2)

T.ap("s13", "IV.3 La Audiencia Nacional (LOPJ, arts. 62 a 66)", f"""
{unidad("3.1 Sede, jurisdicción y composición (LOPJ, arts. 62 y 63)",
  lit(L, "asesentaydos", ["con sede en la villa de Madrid, tiene jurisdicción en toda España"]),
  lit(L, "asesentaytres", ["tendrá la consideración de Presidente de Sala del Tribunal Supremo"]),
  fichab("Tribunal con jurisdicción en toda España", "Presidente, Presidentes de Sala y magistrados",
         "Sede en **Madrid**; jurisdicción en **toda España**", "—",
         "Su Presidente tiene la consideración de **Presidente de Sala del TS** y es Presidente **nato** de todas sus Salas."))}

{unidad("3.2 Salas (LOPJ, arts. 64 y 64 bis)",
  lit(L, "asesentaycuatro", ["De Apelación.", "De lo Penal.", "De lo Contencioso-Administrativo.", "De lo Social."], solo=[1, 2, 3, 4, 5]),
  lit(L, "asesentaycuatrobis", ["contra las resoluciones de la Sala de lo Penal"], solo=[1]),
  fichab("Estructura de la Audiencia Nacional",
         ["::Cuatro Salas:", "De Apelación", "De lo Penal", "De lo Contencioso-Administrativo", "De lo Social"],
         "La Sala de **Apelación** conoce de los recursos de esta clase contra las resoluciones de la Sala de **lo Penal**",
         "—",
         "Cayó en 2025 (→ Cierre 1): la Sala de Apelación revisa a la Sala **de lo Penal** (no a la Social ni a la Contencioso). La AN **no** tiene Sala de lo Civil."))}

{unidad("3.3 Qué conocen las Salas de lo Penal y de lo Contencioso (LOPJ, arts. 65 y 66; fragmentos)",
  lit(L, "asesentaycinco", ["Delitos contra el titular de la Corona", "Delitos cometidos fuera del territorio nacional", "la resolución de los procedimientos judiciales de extradición pasiva"], solo=[1, 2, 3, 7, 13], titulo="Artículo 65 (LOPJ), Sala de lo Penal (fragmento)"),
  lit(L, "asesentayseis", ["contra disposiciones y actos de los Ministros, Ministras, Secretarios y Secretarias de Estado"], solo=[1, 2], titulo="Artículo 66 (LOPJ), Sala de lo Contencioso-Administrativo (fragmento)"),
  fichab("Competencias que caracterizan a la AN", "Salas de lo Penal y de lo Contencioso-Administrativo",
         ["Penal: delitos contra la Corona y altos organismos, delitos cometidos fuera del territorio nacional y otros del art. 65; **extradición pasiva**", "Contencioso: en única instancia, actos de **Ministros y Secretarios de Estado** no atribuidos al Tribunal Central de Instancia (tema IV.13)"],
         "—", "La **extradición pasiva** es de la AN «sea cual fuere el lugar de residencia» del afectado."))}
""", 2)

T.ap("s14", "IV.4 Los Tribunales Superiores de Justicia (art. 152.1 CE; LOPJ, arts. 70 a 74)", f"""
{unidad("4.1 Culminan la organización judicial en la Comunidad Autónoma (art. 152.1 CE; LOPJ, arts. 70 y 71)",
  lit("CE", "Artículo 152", ["Un Tribunal Superior de Justicia, sin perjuicio de la jurisdicción que corresponde al Tribunal Supremo, culminará la organización judicial en el ámbito territorial de la Comunidad Autónoma", "se agotarán ante órganos judiciales radicados en el mismo territorio"], solo=[2, 3], titulo="Artículo 152.1, párrafos segundo y tercero"),
  lit(L, "asetenta", ["culminará la organización judicial en el ámbito territorial de aquélla"]),
  lit(L, "asetentayuno", ["tomará el nombre de la Comunidad Autónoma"]),
  fichab("Órgano judicial superior en cada Comunidad Autónoma", "Un TSJ por Comunidad Autónoma",
         ["Culmina la organización judicial en la Comunidad, **sin perjuicio** de la jurisdicción del TS", "Las sucesivas instancias se agotan, en su caso, en órganos del mismo territorio (salvo el art. 123: TS)"],
         "—", "El TSJ **culmina**, pero **no es la última instancia** en todo: queda a salvo la jurisdicción del **Tribunal Supremo**."))}

{unidad("4.2 Salas y Presidente (LOPJ, art. 72)",
  lit(L, "asetentaydos", ["de lo Civil y Penal, de lo Contencioso-Administrativo y de lo Social", "tendrá la consideración de Magistrado del Tribunal Supremo mientras desempeñe el cargo"]),
  fichab("Estructura del TSJ", "Presidente, Presidentes de Sala y Magistrados",
         ["::Tres Salas:", "De lo Civil y Penal (una sola Sala)", "De lo Contencioso-Administrativo", "De lo Social"],
         "—", "**Tres** Salas: Civil y Penal van **juntas**. El Presidente del TSJ preside la Sala de lo Civil y Penal y tiene la consideración de **Magistrado del TS**."))}

{unidad("4.3 Competencias destacadas (LOPJ, arts. 73 y 74; fragmentos)",
  lit(L, "asetentaytres", ["El conocimiento de los recursos de apelación contra las resoluciones dictadas en primera instancia por las Audiencias Provinciales"], solo=[9, 12], titulo="Artículo 73.3 (LOPJ), Sala de lo Civil y Penal como Sala de lo Penal (fragmento)"),
  lit(L, "asetentaycuatro", ["Las disposiciones generales emanadas de las comunidades autónomas y de las Entidades locales"], solo=[1, 3], titulo="Artículo 74.1 (LOPJ), Sala de lo Contencioso-Administrativo (fragmento)"),
  fichab("Algunas competencias de las Salas del TSJ", "Salas de lo Civil y Penal y de lo Contencioso-Administrativo",
         ["Penal: **apelación** contra las resoluciones de primera instancia de las **Audiencias Provinciales**", "Contencioso: en única instancia, **disposiciones generales** autonómicas y locales (tema IV.13)"],
         "—", "Los **reglamentos** autonómicos y locales se recurren ante el **TSJ**, no ante la Sección de lo Contencioso del Tribunal de Instancia."))}
""", 2)

T.ap("s15", "IV.5 Las Audiencias Provinciales (LOPJ, arts. 80 a 82)", f"""
{unidad("5.1 Sede y composición (LOPJ, arts. 80.1 y 81.1)",
  lit(L, "aochenta", ["tendrán su sede en la capital de la provincia, de la que tomarán su nombre"], solo=[1, 2]),
  lit(L, "aochentayuno", ["se compondrán de un Presidente y dos o más magistrados"], solo=[1]),
  fichab("Tribunal provincial de los órdenes civil y penal", "Presidente y dos o más magistrados; puede tener Secciones (también fuera de la capital)",
         "Sede en la **capital de la provincia**; jurisdicción en toda ella", "—",
         "Pueden crearse **Secciones** fuera de la capital, con uno o varios partidos judiciales adscritos."))}

{unidad("5.2 Competencias (LOPJ, art. 82.1 y 2; fragmentos)",
  lit(L, "aochentaydos", ["De las causas por delito, a excepción de los que la ley atribuye al conocimiento de las Secciones de lo Penal de los Tribunales de Instancia", "De los recursos que establezca la ley contra las resoluciones dictadas en primera instancia por las Secciones Civiles de los Tribunales de Instancia de la provincia"], solo=[1, 2, 3, 9, 10], titulo="Artículo 82.1 y 2 (LOPJ), fragmento"),
  fichab("Qué conocen las Audiencias Provinciales", "Audiencia Provincial",
         ["Penal: **enjuiciamiento** de las causas por delito no atribuidas a las Secciones de lo Penal de los Tribunales de Instancia; recursos contra Instrucción y Penal", "Civil: **recursos** contra las resoluciones de primera instancia de las Secciones Civiles"],
         "—", "En **civil** la Audiencia Provincial solo conoce de **recursos**; en **penal** también **enjuicia**."))}
""", 2)

T.ap("s16", "IV.6 Los Tribunales de Instancia y el Tribunal Central de Instancia (LOPJ, arts. 84 y 95; LO 1/2025)", f"""
{unidad("6.1 El Tribunal de Instancia (LOPJ, art. 84.1 a 3)",
  lit(L, "aochentaycuatro", ["Habrá un Tribunal de Instancia en cada partido judicial, con sede en su capital", "una Sección Única, de Civil y de Instrucción", "Cada Tribunal de Instancia contará con una Presidencia"], solo=list(range(1, 17))),
  fichab("Órgano judicial de primera instancia del partido",
         "Un Tribunal de Instancia **por partido judicial**, con sede en su capital y **Presidencia** propia",
         ["**Sección Única** de Civil y de Instrucción (o Sección Civil y Sección de Instrucción, según la Ley de Demarcación y Planta)", "Además, Secciones de Familia, Infancia y Capacidad; Mercantil; Violencia sobre la Mujer; Violencia contra la Infancia y la Adolescencia; Penal; Menores; Vigilancia Penitenciaria; Contencioso-Administrativo; Social"],
         "Presidencia de Sección: dos o más Secciones, **ocho** o más plazas en la Sección y **doce** o más en el Tribunal",
         "Las antiguas clases de Juzgados son hoy **Secciones** de un único **Tribunal de Instancia** por partido; la adscripción de los jueces a las Secciones es **funcional** (84.4)."))}

{unidad("6.2 El Tribunal Central de Instancia (LOPJ, art. 95)",
  lit(L, "anoventaycinco", ["En la Villa de Madrid y con jurisdicción en todo el territorio nacional existirá un Tribunal Central de Instancia", "Sección de Instrucción", "Sección de lo Penal", "Sección de Menores", "Sección de Vigilancia Penitenciaria", "Sección de lo Contencioso-Administrativo"], solo=[1, 2, 5, 6, 7, 8], titulo="Artículo 95 (LOPJ), fragmento"),
  fichab("Órgano de instancia con jurisdicción en toda España", "Tribunal Central de Instancia, en **Madrid**",
         ["::Cinco Secciones:", "Instrucción (instruye las causas de la Sala de lo Penal de la AN)", "Penal", "Menores", "Vigilancia Penitenciaria", "Contencioso-Administrativo"],
         "—", "Sustituye a los antiguos **Juzgados Centrales**. No tiene Sección Civil ni Social."))}

{unidad("6.3 La transformación de los Juzgados (LO 1/2025, disposiciones transitorias primera y segunda y adicional primera)",
  lit("LO1_2025", "dt", ["El día 1 de julio de 2025", "El día 1 de octubre de 2025", "El día 31 de diciembre de 2025, los restantes Juzgados"], solo=[3, 4, 5, 6], titulo="Disposición transitoria primera (LO 1/2025). Constitución de los Tribunales de Instancia (fragmento)"),
  lit("LO1_2025", "dt-2", ["El día 31 de diciembre de 2025, el Tribunal Central de Instancia se constituirá"], titulo="Disposición transitoria segunda (LO 1/2025). Constitución del Tribunal Central de Instancia"),
  lit("LO1_2025", "da", ["se entenderán referidas a las Secciones del orden jurisdiccional correspondiente de los Tribunales de Instancia"], titulo="Disposición adicional primera (LO 1/2025). Menciones a Juzgados y Tribunales"),
  fichab("Paso de los Juzgados a los Tribunales de Instancia", "Los Juzgados existentes se transforman en Secciones; los Juzgados Centrales, en Secciones del Tribunal Central de Instancia",
         ["Transformación escalonada en **tres fases**", "Las referencias de las leyes a los antiguos Juzgados se entienden hechas a las **Secciones** correspondientes"],
         ["**1-7-2025**: Primera Instancia e Instrucción y Violencia sobre la Mujer en partidos sin otros Juzgados", "**1-10-2025**: Primera Instancia, Instrucción y Violencia sobre la Mujer en los partidos que indica", "**31-12-2025**: los restantes Juzgados y el **Tribunal Central de Instancia**"],
         "Fechas que se preguntan: **1 de julio**, **1 de octubre** y **31 de diciembre de 2025**."))}
""", 2)

T.ap("s17", "IV.7 Jueces de paz y Oficinas de Justicia en los municipios (LOPJ, arts. 99 a 102 y 439 ter)", f"""
{unidad("7.1 Un juez de paz donde no haya Tribunal de Instancia (LOPJ, arts. 99 y 100)",
  lit(L, "anoventaynueve", ["En cada municipio donde no exista Tribunal de Instancia"]),
  lit(L, "acien", ["en el orden civil", "por delito leve"]),
  fichab("Justicia de paz", "Un juez o jueza de paz en cada municipio **sin Tribunal de Instancia**",
         ["Civil: los procesos que la ley determine", "Penal: en primera instancia, procesos por **delito leve** que les atribuya la ley"], "—",
         "Solo en municipios **sin** Tribunal de Instancia. En penal, **delitos leves**."))}

{unidad("7.2 Nombramiento y requisitos (LOPJ, arts. 101 y 102)",
  lit(L, "acientouno", ["para un periodo de cuatro años por la Sala de Gobierno del Tribunal Superior de Justicia", "por el Pleno del Ayuntamiento, con el voto favorable de la mayoría absoluta de sus miembros", "Si en el plazo de tres meses"], solo=[1, 2, 4]),
  lit(L, "acientodos", ["aun no siendo licenciados en Derecho"]),
  fichab("Cómo se elige y nombra al juez de paz",
         ["Elige: el **Pleno del Ayuntamiento**", "Nombra: la **Sala de Gobierno del TSJ**"],
         ["Entre quienes lo soliciten y reúnan las condiciones; si no hay solicitantes, el Pleno elige libremente", "Si el Ayuntamiento no propone en **tres meses**, designa la Sala de Gobierno", "No hace falta ser **licenciado en Derecho**"],
         "Mandato: **4 años** · Pleno: **mayoría absoluta** · plazo del Ayuntamiento: **3 meses**",
         "Elige el **Ayuntamiento** (mayoría absoluta), **nombra** la **Sala de Gobierno del TSJ**, por **cuatro** años."))}

{unidad("7.3 Oficinas de Justicia en los municipios (LOPJ, art. 439 ter.1 y 2; LO 1/2025, disposición transitoria sexta)",
  lit(L, "ar", ["sin estar integradas en la estructura de la Oficina judicial", "En cada municipio donde no tenga su sede un Tribunal de Instancia existirá una Oficina de Justicia"], solo=[1, 2]),
  lit("LO1_2025", "dt-6", ["los Juzgados de Paz se transformarán en Oficinas de Justicia en los municipios"], solo=[1], titulo="Disposición transitoria sexta (LO 1/2025). Implantación de las Oficinas de Justicia en los municipios (apartado 1)"),
  fichab("Unidad de servicio a la ciudadanía en los municipios sin Tribunal de Instancia",
         "Una Oficina de Justicia en cada municipio sin sede de Tribunal de Instancia; en ella dispone de medios el juez o jueza de paz",
         ["No forma parte de la **Oficina judicial**", "Presta servicios a la ciudadanía del municipio y asiste al juez de paz (art. 439 quater)", "Los antiguos **Juzgados de Paz** se transforman en Oficinas de Justicia en la fecha de constitución de cada Tribunal de Instancia"],
         "—",
         "El **juez de paz** subsiste (arts. 99 a 103); lo que se transforma es el **Juzgado de Paz** (la oficina) en **Oficina de Justicia en el municipio**."))}
""", 2)

T.ap("s18", "IV.8 Cuadro de la organización judicial (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Órgano | Ámbito y sede | Composición o Salas/Secciones | Artículos |
|---|---|---|---|
| Tribunal Supremo | Toda España; Madrid | 5 Salas: Civil, Penal, Contencioso, Social, Militar | 123 CE; LOPJ 53-61 |
| Audiencia Nacional | Toda España; Madrid | 4 Salas: Apelación, Penal, Contencioso, Social | LOPJ 62-66 |
| Tribunal Central de Instancia | Toda España; Madrid | Secciones: Instrucción, Penal, Menores, Vigilancia Penitenciaria, Contencioso | LOPJ 95 |
| Tribunal Superior de Justicia | Comunidad Autónoma | 3 Salas: Civil y Penal, Contencioso, Social | 152.1 CE; LOPJ 70-74 |
| Audiencia Provincial | Provincia; capital | Presidente y dos o más magistrados; Secciones | LOPJ 80-82 |
| Tribunal de Instancia | Partido judicial; capital del partido | Sección Única (o Civil e Instrucción) y Secciones especializadas | LOPJ 84-94 |
| Juez o jueza de paz | Municipio sin Tribunal de Instancia | Unipersonal; 4 años; con Oficina de Justicia en el municipio | LOPJ 99-103 y 439 ter |

{resumen([
  "Siete órganos (LOPJ 26): jueces de paz, **Tribunales de Instancia**, Audiencias Provinciales, TSJ, **Tribunal Central de Instancia**, Audiencia Nacional y Tribunal Supremo.",
  "Territorio: **municipio, partido, provincia y Comunidad Autónoma** (LOPJ 30); planta por **ley**, revisada al menos cada **cinco años** (29).",
  "TS: **superior en todos los órdenes** salvo garantías constitucionales; **cinco** Salas. AN: **cuatro** Salas; la de **Apelación** revisa a la de **lo Penal**. TSJ: **culmina** la organización en la Comunidad; **tres** Salas.",
  "LO 1/2025: los Juzgados pasan a ser **Secciones** de los Tribunales de Instancia (1-7, 1-10 y **31-12-2025**); los Juzgados de Paz, **Oficinas de Justicia en los municipios**."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_L10 = examen("L", 10, {
  "a": f"El art. 3.2 no extiende la jurisdicción militar a todo lo que afecte a militares: la limita {c(L, 'atercero', 'en el ámbito estrictamente castrense')}.",
  "b": f"Literal del art. 3.2 LOPJ: {c(L, 'atercero', 'administran Justicia en el ámbito estrictamente castrense y, en su caso, en las materias que establezca la declaración del estado de sitio')}.",
  "c": f"No se limita a lo disciplinario: actúa {c(L, 'atercero', 'de acuerdo con la Constitución y lo dispuesto en las leyes penales, procesales y disciplinarias militares')}.",
  "d": f"El estado de sitio no es su único ámbito: es un ámbito añadido «en su caso» al {c(L, 'atercero', 'estrictamente castrense')}."},
  [("estrictamente castrense", L, "atercero", "administran Justicia en el ámbito estrictamente castrense"),
   ("en las materias que establezca la declaración del estado de sitio", L, "atercero", "en las materias que establezca la declaración del estado de sitio")])
EX_X18 = examen("X", 18, {
  "a": f"Cambia el órgano recurrido: la Sala de Apelación solo revisa a la Sala de lo Penal. Las apelaciones contra los antiguos Juzgados de lo Contencioso van a los TSJ ({c(L, 'asetentaycuatro', 'Conocerán, en segunda instancia, de las apelaciones promovidas contra sentencias y autos dictados en las Secciones de lo Contencioso-Administrativo de los Tribunales de Instancia')}, art. 74.2) o, si eran Centrales, a la Sala de lo Contencioso de la AN (art. 66 c).",
  "b": f"Literal del art. 64 bis.1: {c(L, 'asesentaycuatrobis', 'La Sala de Apelación de la Audiencia Nacional conocerá de los recursos de esta clase que establezca la ley contra las resoluciones de la Sala de lo Penal')}.",
  "c": "Cambia la Sala: el art. 64 bis habla de la Sala **de lo Penal**, no de la Social.",
  "d": "Cambia la Sala (Social en vez de **Penal**) y la ley de referencia: el art. 64 bis se remite a «la ley», no solo a la LOPJ."},
  [("resoluciones de la Sala de lo Penal", L, "asesentaycuatrobis", "contra las resoluciones de la Sala de lo Penal")])
EX_X105 = examen("X", 105, {
  "a": f"No son inhábiles julio y agosto: el art. 183 declara inhábiles {c(L, 'acientoochentaytres', 'los días del mes de agosto')} y del 24 de diciembre al 6 de enero.",
  "b": f"Cambia las horas: {c(L, 'acientoochentaydos', 'Son horas hábiles desde las ocho de la mañana a las ocho de la tarde')} (art. 182.2).",
  "c": f"Cambia una palabra: en los plazos por días {c(L, 'acientoochentaycinco', 'quedarán excluidos los inhábiles')} (art. 185.1), no «incluidos».",
  "d": f"Literal del art. 183: {c(L, 'acientoochentaytres', 'todos los días desde el 24 de diciembre hasta el 6 de enero del año siguiente, ambos inclusive, para todas las actuaciones judiciales, excepto las que se declaren urgentes por las leyes procesales')}."},
  [("desde el 24 de diciembre hasta el 6 de enero del año siguiente, ambos inclusive", L, "acientoochentaytres", "desde el 24 de diciembre hasta el 6 de enero del año siguiente, ambos inclusive")])
EX_X19 = examen("X", 19, {
  "a": f"Cambia el último principio: el art. 124.2 dice {c('CE', 'Artículo 124', 'legalidad e imparcialidad')}, no «objetividad».",
  "b": f"Cambia dos datos: «independencia» en lugar de {c('CE', 'Artículo 124', 'dependencia jerárquica')}, y «objetividad» en lugar de imparcialidad.",
  "c": f"Literal del art. 124.2: {c('CE', 'Artículo 124', 'conforme a los principios de unidad de actuación y dependencia jerárquica y con sujeción, en todo caso, a los de legalidad e imparcialidad')}.",
  "d": f"Cambia una palabra: «independencia jerárquica» no existe; el art. 124.2 dice {c('CE', 'Artículo 124', 'dependencia jerárquica')}."},
  [("actuación, dependencia jerárquica", "CE", "Artículo 124", "unidad de actuación y dependencia jerárquica"),
   ("legalidad e imparcialidad", "CE", "Artículo 124", "legalidad e imparcialidad")])
EX_L9 = examen("L", 9, {
  "a": f"No lo nombra el Congreso ni el informe del CGPJ es vinculante: {c('CE', 'Artículo 124', 'será nombrado por el Rey')}, solo **oído** el CGPJ.",
  "b": f"Invierte los papeles: propone el **Gobierno** y es **oído** el CGPJ ({c('CE', 'Artículo 124', 'a propuesta del Gobierno, oído el Consejo General del Poder Judicial')}).",
  "c": f"Literal del art. 124.4: {c('CE', 'Artículo 124', 'El Fiscal General del Estado será nombrado por el Rey, a propuesta del Gobierno, oído el Consejo General del Poder Judicial')}.",
  "d": "El art. 124.4 no exige ninguna autorización del Senado; el trámite previo es oír al **CGPJ**."},
  [("a propuesta del Gobierno, oído el Consejo General del Poder Judicial", "CE", "Artículo 124", "nombrado por el Rey, a propuesta del Gobierno, oído el Consejo General del Poder Judicial")])

T.ap("s19", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **cuatro** preguntas de este tema (una en el turno libre y tres en el extraordinario, una de ellas de reserva) y **una** relacionada (el nombramiento del Fiscal General del Estado, art. 124.4 CE, sin tema asignado). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-L 2025, pregunta 10 · Jurisdicción militar (→ II.1.3)", EX_L10,
  "### GACE-L 2025 extraordinario, pregunta 18 · Sala de Apelación de la Audiencia Nacional (→ IV.3.2)", EX_X18,
  "### GACE-L 2025 extraordinario, pregunta 19 · Principios del Ministerio Fiscal (→ I.3.2)", EX_X19,
  "### GACE-L 2025 extraordinario, pregunta 105 (de reserva) · Días y horas hábiles (→ I.2.4)", EX_X105,
  "### GACE-L 2025, pregunta 9 · Nombramiento del Fiscal General del Estado (relacionada; → I.3.2)", EX_L9,
  "### Cómo se pregunta",
  "!> Las preguntas de este tema copian **literalmente** un apartado y cambian **una palabra** en los distractores: «independencia» por «dependencia», «objetividad» por «imparcialidad», «Social» por «Penal», «incluidos» por «excluidos», «siete» por «ocho». Hay que leer cada opción contra la letra de la norma.",
]))

T.ap("s20", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Poder Judicial | Justicia que **emana del pueblo**; jueces independientes, inamovibles, responsables y sometidos a la ley; potestad jurisdiccional exclusiva (117); principios (118-121); Cuerpo único (122.1); Ministerio Fiscal (124) | Inhábiles **agosto** y **24-XII a 6-I** (LOPJ 183); MF: **dependencia jerárquica** e **imparcialidad** |
| II. Unidad jurisdiccional | Base de la organización (117.5); prohibición de Tribunales de excepción (117.6); jurisdicción única (LOPJ 3); cuatro órdenes (LOPJ 9) | Militar: **estrictamente castrense** y **estado de sitio** |
| III. CGPJ | Órgano de gobierno (122.2); Presidente del TS + 20 Vocales, 5 años (122.3); cada Cámara 10 por tres quintos (LOPJ 567); Pleno y Comisiones | **12 + 4 + 4**; Presidente elegido por **tres quintos**, reelegible **una vez** |
| IV. Organización judicial | TS, AN, TSJ, AP, Tribunales de Instancia, Tribunal Central de Instancia, jueces de paz (LOPJ 26) | Sala de **Apelación** de la AN → recursos contra la **Sala de lo Penal** (64 bis) |

?> **Trampas frecuentes:** «la justicia emana **del Rey**» (emana **del pueblo**); «el orden residual es el **contencioso**» (es el **civil**); «el FGE lo nombra el Rey a propuesta **del CGPJ**» (a propuesta **del Gobierno**, **oído** el CGPJ); «los Vocales juristas con más de **diez** años» (más de **quince**); «el CGPJ se renueva **por mitades**» (en su **totalidad** cada cinco años); «el Presidente del TS lo propone **el Gobierno**» (lo propone el **CGPJ**); «la AN tiene Sala de lo **Civil**» (no: Apelación, Penal, Contencioso y Social).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
Q = [
 ("CE", "Artículo 117", "Poder Judicial", "Según el artículo 117.1 de la Constitución, la justicia:",
  ["Emana del pueblo y se administra en nombre del Rey.", "Emana del Rey y se administra en nombre del pueblo.", "Emana de las Cortes Generales y se administra en nombre del Rey.", "Emana del pueblo y se administra en nombre del Estado."],
  "Art. 117.1 CE.", "La justicia emana del pueblo y se administra en nombre del Rey"),
 ("CE", "Artículo 117", "Poder Judicial", "Según el artículo 117.1 de la Constitución, los Jueces y Magistrados integrantes del poder judicial son independientes, inamovibles, responsables y sometidos únicamente:",
  ["Al imperio de la ley.", "A la Constitución y al Consejo General del Poder Judicial.", "A las instrucciones del Tribunal Supremo.", "Al Gobierno y a la ley."],
  "Art. 117.1 CE: «sometidos únicamente al imperio de la ley».", "sometidos únicamente al imperio de la ley"),
 ("CE", "Artículo 117", "Poder Judicial", "Según el artículo 117.3 de la Constitución, el ejercicio de la potestad jurisdiccional en todo tipo de procesos corresponde:",
  ["Exclusivamente a los Juzgados y Tribunales determinados por las leyes.", "Al Consejo General del Poder Judicial y a los Juzgados y Tribunales.", "A los Juzgados y Tribunales y al Ministerio Fiscal.", "Exclusivamente al Tribunal Supremo y a los Tribunales Superiores de Justicia."],
  "Art. 117.3 CE.", "corresponde exclusivamente a los Juzgados y Tribunales determinados por las leyes"),
 ("CE", "Artículo 117", "Poder Judicial", "Según el artículo 117.4 de la Constitución, los Juzgados y Tribunales no ejercerán más funciones que las jurisdiccionales y las que expresamente les sean atribuidas por ley:",
  ["En garantía de cualquier derecho.", "En materia de gobierno del Poder Judicial.", "A propuesta del Consejo General del Poder Judicial.", "En materia electoral, exclusivamente."],
  "Art. 117.4 CE.", "las que expresamente les sean atribuidas por ley en garantía de cualquier derecho"),
 ("CE", "Artículo 117", "Unidad jurisdiccional", "Según el artículo 117.5 de la Constitución, la base de la organización y funcionamiento de los Tribunales es:",
  ["El principio de unidad jurisdiccional.", "El principio de jerarquía.", "El principio de especialización.", "El principio de independencia judicial."],
  "Art. 117.5 CE.", "El principio de unidad jurisdiccional es la base de la organización y funcionamiento de los Tribunales"),
 ("CE", "Artículo 117", "Unidad jurisdiccional", "Según el artículo 117.5 de la Constitución, la ley regulará el ejercicio de la jurisdicción militar en el ámbito estrictamente castrense y en los supuestos de:",
  ["Estado de sitio.", "Estado de alarma.", "Estado de excepción.", "Conflicto armado declarado por las Cortes."],
  "Art. 117.5 CE.", "en el ámbito estrictamente castrense y en los supuestos de estado de sitio"),
 ("CE", "Artículo 117", "Unidad jurisdiccional", "Según el artículo 117.6 de la Constitución:",
  ["Se prohíben los Tribunales de excepción.", "Los Tribunales de excepción solo pueden crearse por ley orgánica.", "Los Tribunales de excepción pueden crearse durante el estado de sitio.", "Los Tribunales de excepción requieren autorización del Congreso."],
  "Art. 117.6 CE.", "Se prohíben los Tribunales de excepción"),
 ("CE", "Artículo 119", "Poder Judicial", "Según el artículo 119 de la Constitución, la justicia será gratuita cuando así lo disponga la ley y, en todo caso:",
  ["Respecto de quienes acrediten insuficiencia de recursos para litigar.", "En los procesos penales.", "En los procesos ante el Tribunal Supremo.", "Respecto de los funcionarios públicos en el ejercicio de sus cargos."],
  "Art. 119 CE.", "en todo caso, respecto de quienes acrediten insuficiencia de recursos para litigar"),
 ("CE", "Artículo 120", "Poder Judicial", "Según el artículo 120 de la Constitución, el procedimiento será:",
  ["Predominantemente oral, sobre todo en materia criminal.", "Exclusivamente oral en materia criminal.", "Predominantemente escrito, salvo en materia criminal.", "Predominantemente oral, sobre todo en materia civil."],
  "Art. 120.2 CE.", "El procedimiento será predominantemente oral, sobre todo en materia criminal"),
 ("CE", "Artículo 120", "Poder Judicial", "Según el artículo 120.3 de la Constitución, las sentencias:",
  ["Serán siempre motivadas y se pronunciarán en audiencia pública.", "Serán motivadas cuando lo exija la ley.", "Se pronunciarán siempre por escrito y sin audiencia pública.", "Serán motivadas solo en materia criminal."],
  "Art. 120.3 CE.", "Las sentencias serán siempre motivadas y se pronunciarán en audiencia pública"),
 ("CE", "Artículo 121", "Poder Judicial", "Según el artículo 121 de la Constitución, los daños causados por error judicial darán derecho a una indemnización a cargo:",
  ["Del Estado, conforme a la ley.", "Del juez o magistrado responsable.", "Del Consejo General del Poder Judicial.", "De la Comunidad Autónoma con competencias en Justicia."],
  "Art. 121 CE.", "darán derecho a una indemnización a cargo del Estado, conforme a la ley"),
 ("CE", "Artículo 124", "Ministerio Fiscal", "Según el artículo 124.2 de la Constitución, el Ministerio Fiscal ejerce sus funciones con sujeción, en todo caso, a los principios de:",
  ["Legalidad e imparcialidad.", "Legalidad y objetividad.", "Independencia e imparcialidad.", "Jerarquía y oportunidad."],
  "Art. 124.2 CE.", "con sujeción, en todo caso, a los de legalidad e imparcialidad"),
 ("CE", "Artículo 125", "Poder Judicial", "Según el artículo 125 de la Constitución, los ciudadanos podrán participar en la Administración de Justicia mediante la institución del Jurado:",
  ["En la forma y con respecto a aquellos procesos penales que la ley determine.", "En todos los procesos penales por delito grave.", "En los procesos civiles y penales que la ley determine.", "En los procesos ante la Audiencia Nacional."],
  "Art. 125 CE.", "en la forma y con respecto a aquellos procesos penales que la ley determine"),
 ("CE", "Artículo 126", "Poder Judicial", "Según el artículo 126 de la Constitución, la policía judicial depende, en sus funciones de averiguación del delito:",
  ["De los Jueces, de los Tribunales y del Ministerio Fiscal.", "Del Ministerio del Interior.", "Exclusivamente de los Jueces y Tribunales.", "Del Consejo General del Poder Judicial."],
  "Art. 126 CE.", "La policía judicial depende de los Jueces, de los Tribunales y del Ministerio Fiscal"),
 ("CE", "Artículo 127", "Poder Judicial", "Según el artículo 127.1 de la Constitución, los Jueces y Magistrados, así como los Fiscales, mientras se hallen en activo:",
  ["No podrán pertenecer a partidos políticos o sindicatos.", "No podrán pertenecer a asociaciones profesionales.", "Podrán pertenecer a sindicatos, pero no a partidos políticos.", "Podrán desempeñar otros cargos públicos con autorización del CGPJ."],
  "Art. 127.1 CE.", "no podrán desempeñar otros cargos públicos, ni pertenecer a partidos políticos o sindicatos"),
 (L, "atercero", "Unidad jurisdiccional", "Según el artículo 3.1 de la Ley Orgánica del Poder Judicial, la jurisdicción:",
  ["Es única y se ejerce por los jueces, las juezas y los Tribunales previstos en esa ley orgánica.", "Es plural y se reparte entre la ordinaria y la militar.", "Es única y se ejerce por el Consejo General del Poder Judicial.", "Es única, sin excepción alguna."],
  "Art. 3.1 LOPJ (con la salvedad de las potestades jurisdiccionales que la Constitución reconoce a otros órganos).", "La jurisdicción es única y se ejerce por los jueces, las juezas y los Tribunales previstos en esta ley orgánica"),
 (L, "acuarto", "Unidad jurisdiccional", "Según el artículo 4 de la Ley Orgánica del Poder Judicial, la jurisdicción se extiende:",
  ["A todas las personas, a todas las materias y a todo el territorio español.", "A los ciudadanos españoles en todo el territorio nacional.", "A todas las materias, salvo las militares.", "A todas las personas residentes en España."],
  "Art. 4 LOPJ.", "La jurisdicción se extiende a todas las personas, a todas las materias y a todo el territorio español"),
 (L, "anoveno", "Unidad jurisdiccional", "Según el artículo 9.2 de la Ley Orgánica del Poder Judicial, además de las materias que les son propias, conocerán de todas aquellas que no estén atribuidas a otro orden jurisdiccional los Tribunales del orden:",
  ["Civil.", "Contencioso-administrativo.", "Penal.", "Social."],
  "Art. 9.2 LOPJ: el orden civil es el residual.", "del orden civil conocerán, además de las materias que les son propias, de todas aquellas que no estén atribuidas a otro orden jurisdiccional"),
 (L, "anoveno", "Unidad jurisdiccional", "Según el artículo 9.6 de la Ley Orgánica del Poder Judicial, la jurisdicción es:",
  ["Improrrogable.", "Prorrogable por acuerdo de las partes.", "Prorrogable por decisión del Ministerio Fiscal.", "Prorrogable en el orden civil."],
  "Art. 9.6 LOPJ.", "La jurisdicción es improrrogable"),
 ("CE", "Artículo 122", "CGPJ", "Según el artículo 122.3 de la Constitución, el Consejo General del Poder Judicial estará integrado por el Presidente del Tribunal Supremo, que lo presidirá, y por:",
  ["Veinte miembros nombrados por el Rey por un período de cinco años.", "Veinte miembros nombrados por el Rey por un período de nueve años.", "Doce miembros nombrados por el Rey por un período de cinco años.", "Veinte miembros elegidos por las Cortes por un período de cuatro años."],
  "Art. 122.3 CE.", "por veinte miembros nombrados por el Rey por un período de cinco años"),
 ("CE", "Artículo 122", "CGPJ", "Según el artículo 122.3 de la Constitución, los miembros del CGPJ propuestos por el Congreso y el Senado se elegirán entre abogados y otros juristas de reconocida competencia con más de:",
  ["Quince años de ejercicio en su profesión.", "Diez años de ejercicio en su profesión.", "Veinte años de ejercicio en su profesión.", "Veinticinco años de ejercicio en su profesión."],
  "Art. 122.3 CE.", "con más de quince años de ejercicio en su profesión"),
 ("CE", "Artículo 122", "CGPJ", "Según el artículo 122.3 de la Constitución, los cuatro miembros del CGPJ propuestos por el Congreso de los Diputados son elegidos por mayoría de:",
  ["Tres quintos de sus miembros.", "Dos tercios de sus miembros.", "Mayoría absoluta de sus miembros.", "Mayoría simple de los presentes."],
  "Art. 122.3 CE.", "elegidos en ambos casos por mayoría de tres quintos de sus miembros"),
 ("CE", "Artículo 122", "CGPJ", "Según el artículo 122.2 de la Constitución, el Consejo General del Poder Judicial es:",
  ["El órgano de gobierno del Poder Judicial.", "El órgano jurisdiccional superior en todos los órdenes.", "El órgano consultivo del Gobierno en materia de justicia.", "El órgano de representación de las asociaciones judiciales."],
  "Art. 122.2 CE.", "El Consejo General del Poder Judicial es el órgano de gobierno del mismo"),
 (L, "aquinientossesentaysiete", "CGPJ", "Según el artículo 567.2 de la Ley Orgánica del Poder Judicial, cada una de las Cámaras elegirá, por mayoría de tres quintos de sus miembros:",
  ["Diez Vocales: cuatro juristas y seis del turno judicial.", "Diez Vocales: seis juristas y cuatro del turno judicial.", "Doce Vocales del turno judicial.", "Cuatro Vocales juristas, correspondiendo los demás a los jueces."],
  "Art. 567.2 LOPJ.", "a diez Vocales, cuatro entre juristas de reconocida competencia con más de quince años de ejercicio en su profesión y seis correspondientes al turno judicial"),
 (L, "aquinientossesentayocho", "CGPJ", "Según el artículo 568.1 de la Ley Orgánica del Poder Judicial, el Consejo General del Poder Judicial se renovará:",
  ["En su totalidad cada cinco años.", "Por mitades cada cinco años.", "Por terceras partes cada tres años.", "En su totalidad cada cuatro años, con cada legislatura."],
  "Art. 568.1 LOPJ.", "se renovará en su totalidad cada cinco años"),
 (L, "aquinientosochentayuno", "CGPJ", "Según el artículo 581 de la Ley Orgánica del Poder Judicial, los Vocales del Consejo General del Poder Judicial:",
  ["No estarán ligados por mandato imperativo.", "Estarán ligados por las instrucciones de la Cámara que los designó.", "Estarán sometidos a las instrucciones del Presidente del Tribunal Supremo.", "Representarán a las asociaciones judiciales que los avalaron."],
  "Art. 581 LOPJ.", "no estarán ligados por mandato imperativo"),
 (L, "aquinientosochentayseis", "CGPJ", "Según el artículo 586.3 de la Ley Orgánica del Poder Judicial, el Presidente del Tribunal Supremo y del CGPJ es elegido por el Pleno con el apoyo de:",
  ["La mayoría de tres quintos de los miembros del Pleno.", "La mayoría absoluta de los miembros del Pleno.", "La mayoría de dos tercios de los miembros del Pleno.", "La mayoría simple de los Vocales presentes."],
  "Art. 586.3 LOPJ.", "obtenga el apoyo de la mayoría de tres quintos de los miembros del Pleno"),
 (L, "aquinientosochentaysiete", "CGPJ", "Según el artículo 587.2 de la Ley Orgánica del Poder Judicial, el Presidente del Tribunal Supremo y del Consejo General del Poder Judicial:",
  ["Podrá ser reelegido y nombrado, por una sola vez, para un nuevo mandato.", "No podrá ser reelegido.", "Podrá ser reelegido sin limitación.", "Podrá ser reelegido dos veces."],
  "Art. 587.2 LOPJ.", "podrá ser reelegido y nombrado, por una sola vez, para un nuevo mandato"),
 ("CE", "Artículo 123", "CGPJ", "Según el artículo 123.2 de la Constitución, el Presidente del Tribunal Supremo será nombrado por el Rey a propuesta:",
  ["Del Consejo General del Poder Judicial.", "Del Gobierno.", "Del Congreso de los Diputados.", "Del Pleno del Tribunal Supremo."],
  "Art. 123.2 CE.", "a propuesta del Consejo General del Poder Judicial"),
 (L, "aseiscientos", "CGPJ", "Según el artículo 600.1 de la Ley Orgánica del Poder Judicial, el Pleno del Consejo General del Poder Judicial se reunirá en sesión ordinaria:",
  ["Una vez al mes.", "Una vez a la semana.", "Una vez cada tres meses.", "Dos veces al año."],
  "Art. 600.1 LOPJ.", "a convocatoria del Presidente, una vez al mes"),
 (L, "aseiscientosuno", "CGPJ", "Según el artículo 601.2 de la Ley Orgánica del Poder Judicial, la Comisión Permanente está compuesta por el Presidente y:",
  ["Otros siete Vocales: cuatro del turno judicial y tres del turno de juristas.", "Otros cinco Vocales: tres del turno judicial y dos del turno de juristas.", "Otros siete Vocales: cuatro del turno de juristas y tres del turno judicial.", "Todos los Vocales del turno judicial."],
  "Art. 601.2 LOPJ.", "otros siete Vocales: cuatro de los nombrados por el turno judicial y tres de los designados por el turno de juristas de reconocida competencia"),
 (L, "aseiscientostreintayocho", "CGPJ", "Según el artículo 638.2 de la Ley Orgánica del Poder Judicial, los acuerdos del Pleno y de la Comisión Permanente del CGPJ son recurribles ante:",
  ["La Sala de lo Contencioso-Administrativo del Tribunal Supremo.", "La Sala de lo Contencioso-Administrativo de la Audiencia Nacional.", "El Tribunal Constitucional, en recurso de amparo directo.", "La Sala de lo Contencioso-Administrativo del Tribunal Superior de Justicia de Madrid."],
  "Art. 638.2 LOPJ.", "serán recurribles ante la Sala de lo Contencioso-Administrativo del Tribunal Supremo"),
 (L, "aquinientossesentayuno", "CGPJ", "Según el artículo 561.2 de la Ley Orgánica del Poder Judicial, el CGPJ emitirá su informe sobre los anteproyectos de ley sometidos a su informe en el plazo improrrogable de:",
  ["Treinta días; quince si se hace constar la urgencia.", "Dos meses; un mes si se hace constar la urgencia.", "Quince días; diez si se hace constar la urgencia.", "Un mes, sin posibilidad de reducción."],
  "Art. 561.2 LOPJ.", "emitirá su informe en el plazo improrrogable de treinta días. Si en la orden de remisión se hiciere constar la urgencia del informe, el plazo será de quince días"),
 (L, "aveintiseis", "Organización judicial", "Según el artículo 26 de la Ley Orgánica del Poder Judicial, ¿cuál de los siguientes es uno de los Tribunales a los que se atribuye el ejercicio de la potestad jurisdiccional?",
  ["El Tribunal Central de Instancia.", "Los Juzgados Centrales de Instrucción.", "Los Juzgados de Primera Instancia.", "El Consejo General del Poder Judicial."],
  "Art. 26 LOPJ, tras la LO 1/2025.", "e) Tribunal Central de Instancia"),
 (L, "atreinta", "Organización judicial", "Según el artículo 30 de la Ley Orgánica del Poder Judicial, el Estado se organiza territorialmente, a efectos judiciales, en:",
  ["Municipios, Partidos, Provincias y Comunidades Autónomas.", "Municipios, Comarcas, Provincias y Comunidades Autónomas.", "Partidos, Provincias y Comunidades Autónomas.", "Municipios, Provincias, Regiones y Comunidades Autónomas."],
  "Art. 30 LOPJ.", "en Municipios, Partidos, Provincias y Comunidades Autónomas"),
 (L, "acincuentaycinco", "Organización judicial", "Según el artículo 55 de la Ley Orgánica del Poder Judicial, la Sala Tercera del Tribunal Supremo es la de:",
  ["Lo Contencioso-Administrativo.", "Lo Social.", "Lo Penal.", "Lo Militar."],
  "Art. 55 LOPJ: Primera, Civil; Segunda, Penal; Tercera, Contencioso-Administrativo; Cuarta, Social; Quinta, Militar.", "Tercera: De lo Contencioso-Administrativo"),
 (L, "asesentaycuatro", "Organización judicial", "Según el artículo 64.1 de la Ley Orgánica del Poder Judicial, ¿cuál de las siguientes Salas NO forma parte de la Audiencia Nacional?",
  ["De lo Civil.", "De Apelación.", "De lo Penal.", "De lo Social."],
  "Art. 64.1 LOPJ: Apelación, Penal, Contencioso-Administrativo y Social.", "De Apelación."),
 (L, "asetentaydos", "Organización judicial", "Según el artículo 72.1 de la Ley Orgánica del Poder Judicial, el Tribunal Superior de Justicia estará integrado por las Salas:",
  ["De lo Civil y Penal, de lo Contencioso-Administrativo y de lo Social.", "De lo Civil, de lo Penal, de lo Contencioso-Administrativo y de lo Social.", "De Apelación, de lo Civil y Penal y de lo Contencioso-Administrativo.", "De lo Civil y Penal y de lo Contencioso-Administrativo y Social."],
  "Art. 72.1 LOPJ.", "de lo Civil y Penal, de lo Contencioso-Administrativo y de lo Social"),
 (L, "aochentaycuatro", "Organización judicial", "Según el artículo 84.1 de la Ley Orgánica del Poder Judicial, habrá un Tribunal de Instancia:",
  ["En cada partido judicial, con sede en su capital.", "En cada provincia, con sede en su capital.", "En cada municipio de más de 7.000 habitantes.", "En cada Comunidad Autónoma, con sede en la del Tribunal Superior de Justicia."],
  "Art. 84.1 LOPJ.", "Habrá un Tribunal de Instancia en cada partido judicial, con sede en su capital"),
 ("LO1_2025", "dt-2", "Organización judicial", "Según la disposición transitoria segunda de la Ley Orgánica 1/2025, el Tribunal Central de Instancia se constituirá:",
  ["El día 31 de diciembre de 2025.", "El día 1 de julio de 2025.", "El día 1 de octubre de 2025.", "El día 3 de abril de 2025."],
  "Disposición transitoria segunda LO 1/2025.", "El día 31 de diciembre de 2025, el Tribunal Central de Instancia se constituirá"),
 (L, "acientouno", "Organización judicial", "Según el artículo 101 de la Ley Orgánica del Poder Judicial, los Jueces de Paz y sus sustitutos serán nombrados:",
  ["Para un periodo de cuatro años por la Sala de Gobierno del Tribunal Superior de Justicia.", "Para un periodo de cinco años por el Consejo General del Poder Judicial.", "Para un periodo de cuatro años por el Pleno del Ayuntamiento.", "Con carácter indefinido por el Ministerio de Justicia."],
  "Art. 101.1 LOPJ: los elige el Pleno del Ayuntamiento y los nombra la Sala de Gobierno del TSJ.", "serán nombrados para un periodo de cuatro años por la Sala de Gobierno del Tribunal Superior de Justicia"),
 (L, "acientouno", "Organización judicial", "Según el artículo 101.2 de la Ley Orgánica del Poder Judicial, los Jueces de Paz serán elegidos por el Pleno del Ayuntamiento con el voto favorable de:",
  ["La mayoría absoluta de sus miembros.", "La mayoría de dos tercios de sus miembros.", "La mayoría simple de los concejales presentes.", "La mayoría de tres quintos de sus miembros."],
  "Art. 101.2 LOPJ.", "con el voto favorable de la mayoría absoluta de sus miembros"),
]
for q in Q: T.q(*q)
T.real("L", 10, "Unidad jurisdiccional"); T.real("X", 18, "Organización judicial"); T.real("X", 19, "Ministerio Fiscal"); T.real("X", 105, "Poder Judicial"); T.real("L", 9, "Ministerio Fiscal")

# Flashcards
for q_, a_, cat in [
  ("¿De dónde emana la justicia y en nombre de quién se administra? (art. 117.1)", "Emana del pueblo y se administra en nombre del Rey.", "Poder Judicial"),
  ("Cuatro notas de los Jueces y Magistrados (art. 117.1)", "Independientes, inamovibles, responsables y sometidos únicamente al imperio de la ley.", "Poder Judicial"),
  ("¿En qué consiste la potestad jurisdiccional? (art. 117.3)", "Juzgar y hacer ejecutar lo juzgado; corresponde exclusivamente a los Juzgados y Tribunales determinados por las leyes.", "Poder Judicial"),
  ("Reglas del art. 120 CE", "Actuaciones públicas (con excepciones legales); procedimiento predominantemente oral, sobre todo en materia criminal; sentencias siempre motivadas y en audiencia pública.", "Poder Judicial"),
  ("Días inhábiles del art. 183 LOPJ", "Los de agosto y del 24 de diciembre al 6 de enero, ambos inclusive, salvo actuaciones urgentes.", "Poder Judicial"),
  ("Horas hábiles (LOPJ, art. 182.2)", "De las ocho de la mañana a las ocho de la tarde, salvo que la ley disponga lo contrario.", "Poder Judicial"),
  ("Principios del Ministerio Fiscal (art. 124.2)", "Unidad de actuación y dependencia jerárquica; con sujeción, en todo caso, a legalidad e imparcialidad.", "Ministerio Fiscal"),
  ("Nombramiento del Fiscal General del Estado (art. 124.4)", "El Rey, a propuesta del Gobierno, oído el CGPJ.", "Ministerio Fiscal"),
  ("Principio de unidad jurisdiccional (art. 117.5)", "Es la base de la organización y funcionamiento de los Tribunales.", "Unidad jurisdiccional"),
  ("Ámbito de la jurisdicción militar (art. 117.5 CE; LOPJ 3.2)", "El estrictamente castrense y, en su caso, las materias de la declaración del estado de sitio.", "Unidad jurisdiccional"),
  ("Orden jurisdiccional residual (LOPJ 9.2)", "El civil.", "Unidad jurisdiccional"),
  ("Composición del CGPJ (art. 122.3)", "Presidente del TS y 20 miembros nombrados por el Rey por cinco años: 12 entre Jueces y Magistrados; 4 a propuesta del Congreso y 4 del Senado por tres quintos, entre juristas con más de 15 años.", "CGPJ"),
  ("¿Cuántos Vocales elige cada Cámara? (LOPJ 567.2)", "Diez, por tres quintos: cuatro juristas y seis del turno judicial.", "CGPJ"),
  ("Proporción mínima del turno judicial (LOPJ 578.3)", "Tres Magistrados del TS, tres Magistrados con más de 25 años de antigüedad y seis Jueces o Magistrados sin sujeción a antigüedad.", "CGPJ"),
  ("Elección del Presidente del TS y del CGPJ (LOPJ 586)", "Por el Pleno, por tres quintos, en votación nominal; lo nombra el Rey por Real Decreto refrendado por el Presidente del Gobierno.", "CGPJ"),
  ("Quórum del Pleno del CGPJ (LOPJ 600)", "Para elegir Presidente, doce miembros; en los demás casos, diez Vocales y el Presidente.", "CGPJ"),
  ("Composición de la Comisión Permanente (LOPJ 601)", "Presidente y siete Vocales (cuatro judiciales y tres juristas), elegidos anualmente.", "CGPJ"),
  ("¿Ante quién se recurren los acuerdos del Pleno y de la Permanente del CGPJ? (LOPJ 638.2)", "Ante la Sala de lo Contencioso-Administrativo del Tribunal Supremo.", "CGPJ"),
  ("Salas del Tribunal Supremo (LOPJ 55)", "Primera, Civil; Segunda, Penal; Tercera, Contencioso-Administrativo; Cuarta, Social; Quinta, Militar.", "Organización judicial"),
  ("Salas de la Audiencia Nacional (LOPJ 64)", "Apelación, Penal, Contencioso-Administrativo y Social.", "Organización judicial"),
  ("¿De qué conoce la Sala de Apelación de la AN? (LOPJ 64 bis)", "De los recursos de esta clase que establezca la ley contra las resoluciones de la Sala de lo Penal.", "Organización judicial"),
  ("Salas del TSJ (LOPJ 72)", "De lo Civil y Penal, de lo Contencioso-Administrativo y de lo Social.", "Organización judicial"),
  ("¿Dónde hay un Tribunal de Instancia? (LOPJ 84.1)", "En cada partido judicial, con sede en su capital.", "Organización judicial"),
  ("Jueces de paz: quién elige, quién nombra y por cuánto tiempo (LOPJ 101)", "Elige el Pleno del Ayuntamiento por mayoría absoluta; nombra la Sala de Gobierno del TSJ; cuatro años.", "Organización judicial"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Potestad jurisdiccional", "Juzgar y hacer ejecutar lo juzgado; corresponde exclusivamente a los Juzgados y Tribunales determinados por las leyes (art. 117.3 CE).", "s1", "Poder Judicial")
T.glos("Inamovilidad", "Garantía de que los Jueces y Magistrados no pueden ser separados, suspendidos, trasladados ni jubilados sino por las causas y con las garantías de la ley (art. 117.2 CE).", "s1", "Poder Judicial")
T.glos("Error judicial", "Título, junto con el funcionamiento anormal de la Administración de Justicia, del derecho a indemnización a cargo del Estado (art. 121 CE).", "s2", "Poder Judicial")
T.glos("Ministerio Fiscal", "Órgano que promueve la acción de la justicia en defensa de la legalidad; actúa por unidad de actuación y dependencia jerárquica, con sujeción a legalidad e imparcialidad (art. 124 CE).", "s3", "Ministerio Fiscal")
T.glos("Unidad jurisdiccional", "Principio que es la base de la organización y funcionamiento de los Tribunales: la jurisdicción es única (art. 117.5 CE; LOPJ, art. 3).", "s4", "Unidad jurisdiccional")
T.glos("Jurisdicción militar", "Integrante del Poder Judicial del Estado; administra Justicia en el ámbito estrictamente castrense y, en su caso, en las materias de la declaración del estado de sitio (LOPJ, art. 3.2).", "s4", "Unidad jurisdiccional")
T.glos("Orden jurisdiccional", "Cada uno de los cuatro bloques en que se reparte la jurisdicción: civil (residual), penal, contencioso-administrativo y social (LOPJ, art. 9).", "s5", "Unidad jurisdiccional")
T.glos("Consejo General del Poder Judicial", "Órgano de gobierno del Poder Judicial: Presidente del TS y veinte Vocales nombrados por el Rey por cinco años (art. 122 CE; LOPJ, Libro VIII).", "s6", "CGPJ")
T.glos("Turno judicial", "Los doce Vocales del CGPJ elegidos entre Jueces y Magistrados en servicio activo; cada Cámara elige seis (LOPJ, arts. 566, 567 y 578).", "s7", "CGPJ")
T.glos("Consejo en funciones", "Situación del CGPJ cuando ninguna Cámara ha designado a tiempo a sus Vocales: sigue el saliente con las atribuciones tasadas del art. 570 bis LOPJ.", "s7", "CGPJ")
T.glos("Comisión Permanente", "Comisión del CGPJ formada por el Presidente y siete Vocales, elegidos anualmente; prepara el Pleno y decide los nombramientos reglados (LOPJ, arts. 601 y 602).", "s10", "CGPJ")
T.glos("Planta judicial", "Conjunto de órganos judiciales que se establece por ley y se revisa al menos cada cinco años (LOPJ, art. 29).", "s11", "Organización judicial")
T.glos("Partido judicial", "Unidad territorial integrada por uno o más municipios limítrofes de una misma provincia; en cada uno hay un Tribunal de Instancia (LOPJ, arts. 32 y 84).", "s11", "Organización judicial")
T.glos("Tribunal de Instancia", "Órgano judicial de cada partido, con sede en su capital, organizado en Secciones (Sección Única de Civil y de Instrucción y Secciones especializadas) (LOPJ, art. 84; LO 1/2025).", "s16", "Organización judicial")
T.glos("Oficina de Justicia en el municipio", "Unidad no integrada en la Oficina judicial que presta servicios a la ciudadanía en cada municipio sin sede de Tribunal de Instancia (LOPJ, art. 439 ter).", "s17", "Organización judicial")

# Cronología (fechas de los metadatos del BOE)
T.hito("1978", "Constitución Española (27-12-1978; BOE de 29-12-1978)", "Título VI, «Del Poder Judicial» (arts. 117 a 127)", "normativo", "s1")
T.hito("1985", "Ley Orgánica 6/1985, de 1 de julio, del Poder Judicial (BOE de 2-7-1985)", "Desarrolla el Título VI: unidad jurisdiccional, organización de los Tribunales y CGPJ", "normativo", "s4")
T.hito("2003", "Ley Orgánica 19/2003, de 23 de diciembre, de modificación de la LOPJ (BOE de 26-12-2003)", "Redacción vigente del art. 64 bis (Sala de Apelación de la Audiencia Nacional)", "normativo", "s13")
T.hito("2013", "Ley Orgánica 4/2013, de 28 de junio, de reforma del Consejo General del Poder Judicial (BOE de 29-6-2013)", "Redacción vigente del art. 566 (composición del CGPJ)", "normativo", "s7")
T.hito("2021", "Ley Orgánica 4/2021, de 29 de marzo (BOE de 30-3-2021), y Ley Orgánica 8/2022, de 27 de julio (BOE de 28-7-2022)", "Régimen del CGPJ en funciones (art. 570 bis)", "normativo", "s7")
T.hito("2024", "Ley Orgánica 3/2024, de 2 de agosto, de reforma de la LOPJ (BOE de 5-8-2024)", "Redacción vigente del art. 567 (designación de los Vocales)", "normativo", "s7")
T.hito("2025", "Ley Orgánica 1/2025, de 2 de enero, de medidas en materia de eficiencia del Servicio Público de Justicia (BOE de 3-1-2025)", "Tribunales de Instancia, Tribunal Central de Instancia y Oficinas de Justicia en los municipios", "normativo", "s16")

T.publicar()
