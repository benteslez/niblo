# -*- coding: utf-8 -*-
"""Tema IV.2 (B4T02): La ley. Tipos de leyes. Reserva de ley. Disposiciones del
Gobierno con fuerza de ley: decreto-ley y decreto legislativo.
Método del I.2: mapa → bloques (I a IV) con guía; cada artículo, texto literal del
BOE + ficha de casillas fijas; cierre 1 (preguntas oficiales) y cierre 2 (repaso)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

T = Tema("B4T02",
  "Cuatro preguntas: I. Qué es la ley y qué tipos hay (arts. 66.2, 75.3, 81, 82.1, 91 y 150 CE) · II. Qué materias exigen ley: la reserva de ley (arts. 30.2, 31.3, 53.1, 81.1, 103.3 y 133 CE) · III. Cómo legisla el Gobierno por delegación: el decreto legislativo (arts. 82 a 85 CE; Ley 50/1997, art. 24; LJCA, art. 1; LOTC, art. 27) · IV. Cómo legisla por urgencia: el decreto-ley (art. 86 y Reglamento del Congreso). Cada artículo: texto literal del BOE y ficha.",
  ["Ley orgánica", "Art. 81", "Leyes del art. 150", "Reserva de ley", "Art. 53.1", "Decreto legislativo", "Arts. 82-85", "Ley de bases", "Texto refundido", "Decreto-ley", "Art. 86", "Convalidación", "RCD art. 151"])

# =============================================================================
T.ap("s0", "Mapa del tema: cuatro preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque IV, tema 2):
> La ley. Tipos de leyes. Reserva de ley. Disposiciones del Gobierno con fuerza de ley: decreto-ley y decreto legislativo.

### El hilo conductor

El epígrafe se lee como **cuatro preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Constitución | Otras normas |
|---|---|---|---|
| **I** | ¿Qué es la ley y qué tipos hay? | Arts. 66.2, 75.3, 91, 81, 82.1 y 150 | — |
| **II** | ¿Qué materias exigen ley? (reserva de ley) | Arts. 53.1, 81.1, 30.2, 31.3, 103.3 y 133 | — |
| **III** | ¿Cómo legisla el Gobierno por delegación? (decreto legislativo) | Arts. 82 a 85 | Ley 50/1997, art. 24.1 a); LJCA, art. 1.1; LOTC, art. 27.2 |
| **IV** | ¿Cómo legisla el Gobierno por urgencia? (decreto-ley) | Art. 86 | Reglamento del Congreso, art. 151 |

!> **La idea que une los cuatro bloques:** la ley la hacen **las Cortes** (I). Hay materias que **solo** puede regular una ley (II). El Gobierno solo puede dictar normas **con rango de ley** por dos vías tasadas: porque las Cortes **le delegan** (III, decreto legislativo) o porque hay **extraordinaria y urgente necesidad** (IV, decreto-ley), y en los dos casos las Cortes conservan el control.

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué es la ley y qué tipos hay? (arts. 66.2, 75.3, 81, 82.1, 91 y 150)", donde(
  "Primera pregunta del tema. Antes de hablar de reserva de ley o de las normas del Gobierno con fuerza de ley, hay que saber **quién** hace la ley y **qué clases** de ley prevé la Constitución.",
  ["1 La ley: las Cortes, la delegación en Comisiones y la sanción del Rey (arts. 66.2, 75.3 y 91)", "2 Leyes orgánicas (arts. 81 y 82.1)", "3 Las leyes del art. 150: marco, de transferencia o delegación y de armonización", "4 Cuadro de los tipos de leyes"]))

T.ap("s1", "I.1 La ley: potestad legislativa de las Cortes, delegación en Comisiones y sanción (arts. 66.2, 75.3 y 91)", f"""
La ley es la norma que aprueban las **Cortes Generales**, titulares de la potestad legislativa del Estado; el Rey la sanciona y promulga.

{unidad("1.1 La potestad legislativa (art. 66.2)",
  lit("CE", "Artículo 66", ["ejercen la potestad legislativa del Estado"], solo=[2]),
  fichab("La potestad de hacer las leyes del Estado",
         f"{c('CE', 'Artículo 66', 'Las Cortes Generales')} (Congreso y Senado)",
         "Por el procedimiento legislativo (→ tema I.5)",
         "—",
         "La potestad legislativa es de las **Cortes**; el Gobierno solo dicta normas con rango de ley en los dos casos tasados (→ III.1 y → IV.1)."))}

{unidad("1.2 Delegación en las Comisiones Legislativas Permanentes y sus excepciones (art. 75.2 y 3)",
  lit("CE", "Artículo 75", ["podrán delegar en las Comisiones Legislativas Permanentes", "las leyes orgánicas y de bases"], solo=[2, 3]),
  fichab("Aprobación de leyes por las Comisiones Legislativas Permanentes y sus excepciones",
         ["Las **Cámaras** delegan; aprueban las **Comisiones Legislativas Permanentes**", "El **Pleno** puede recabar en cualquier momento el debate y votación"],
         ["::No se puede delegar (75.3):", "La **reforma constitucional**", "Las **cuestiones internacionales**", "Las **leyes orgánicas y de bases**", "Los **Presupuestos Generales del Estado**"],
         "—",
         "Las leyes **orgánicas** y **de bases** no se aprueban en Comisión. Cayó en 2025 (→ Cierre 1)."))}

{unidad("1.3 Sanción, promulgación y publicación (art. 91)",
  lit("CE", "Artículo 91", ["en el plazo de quince días"]),
  fichab("Último paso de la ley: sanción, promulgación y orden de publicación",
         c("CE", "Artículo 91", "El Rey"),
         f"{c('CE', 'Artículo 91', 'sancionará')}, {c('CE', 'Artículo 91', 'promulgará')} y {c('CE', 'Artículo 91', 'ordenará su inmediata publicación')}",
         f"Sanción: {c('CE', 'Artículo 91', 'en el plazo de quince días')}",
         "**Quince** días para sancionar; la publicación es **inmediata**. Es el Rey, no el Presidente del Gobierno ni el del Congreso."))}
""", 2)

T.ap("s2", "I.2 Las leyes orgánicas (arts. 81 y 82.1)", f"""
La Constitución distingue la ley **orgánica** de la **ordinaria** por dos rasgos: las **materias** que regula y la **mayoría** que exige.

{unidad("2.1 Materias y mayoría (art. 81)",
  lit("CE", "Artículo 81", ["desarrollo de los derechos fundamentales y de las libertades públicas", "Estatutos de Autonomía", "régimen electoral general", "las demás previstas en la Constitución", "mayoría absoluta del Congreso, en una votación final sobre el conjunto del proyecto"]),
  fichab("Ley de las Cortes reservada a ciertas materias y aprobada por mayoría reforzada",
         "Las Cortes Generales; la mayoría reforzada se exige en el **Congreso**",
         ["::Materias (81.1):", "Desarrollo de los derechos fundamentales y libertades públicas", "Aprobación de los Estatutos de Autonomía", "Régimen electoral general", "Las demás previstas en la Constitución"],
         f"{c('CE', 'Artículo 81', 'mayoría absoluta del Congreso, en una votación final sobre el conjunto del proyecto')}, para aprobarlas, modificarlas o derogarlas",
         "La mayoría absoluta es del **Congreso** y en la **votación final sobre el conjunto**, no en cada artículo ni en el Senado. Vale para aprobar, **modificar o derogar**."))}

{unidad("2.2 Tampoco por delegación en el Gobierno (art. 82.1)",
  lit("CE", "Artículo 82", ["no incluidas en el artículo anterior"], solo=[1]),
  fichab("Límites de procedimiento de la ley orgánica",
         "—",
         ["No cabe delegación legislativa en el Gobierno sobre materias del art. 81 (82.1 → III.1)", "Tampoco cabe delegar su aprobación en las Comisiones Legislativas Permanentes (75.3 → I.1.2)"],
         "—",
         "El «artículo anterior» es el **81**: la ley orgánica la aprueban siempre las **Cortes** (ni el Gobierno por decreto legislativo ni las Comisiones)."))}
""", 2)

T.ap("s3", "I.3 Las leyes del art. 150: marco, de transferencia o delegación y de armonización", f"""
El art. 150 regula tres leyes estatales que **atribuyen, transfieren o armonizan** competencias normativas de las Comunidades Autónomas.

{unidad("3.1 Leyes marco (art. 150.1)",
  lit("CE", "Artículo 150", ["en el marco de los principios, bases y directrices fijados por una ley estatal", "en cada ley marco"], solo=[1]),
  fichab("Las Cortes atribuyen a las Comunidades Autónomas la facultad de dictar normas legislativas en materias estatales",
         f"{c('CE', 'Artículo 150', 'Las Cortes Generales')} → {c('CE', 'Artículo 150', 'todas o a alguna de las Comunidades Autónomas')}",
         f"Dentro de {c('CE', 'Artículo 150', 'los principios, bases y directrices fijados por una ley estatal')}; cada ley marco fija el control de las Cortes",
         "—",
         "Se atribuye la facultad de dictar **normas legislativas**, en materias de **competencia estatal**."))}

{unidad("3.2 Leyes de transferencia o delegación (art. 150.2)",
  lit("CE", "Artículo 150", ["mediante ley orgánica", "transferencia de medios financieros"], solo=[2]),
  fichab("El Estado transfiere o delega en las Comunidades Autónomas facultades de titularidad estatal",
         f"{c('CE', 'Artículo 150', 'El Estado')} → Comunidades Autónomas",
         f"{c('CE', 'Artículo 150', 'mediante ley orgánica')}, solo en facultades {c('CE', 'Artículo 150', 'que por su propia naturaleza sean susceptibles de transferencia o delegación')}",
         "Ley **orgánica** (mayoría absoluta del Congreso, → I.2)",
         "Es la única de las tres que exige **ley orgánica**; prevé la transferencia de **medios financieros** y las formas de control del Estado."))}

{unidad("3.3 Leyes de armonización (art. 150.3)",
  lit("CE", "Artículo 150", ["aun en el caso de materias atribuidas a la competencia de éstas", "por mayoría absoluta de cada Cámara"], solo=[3]),
  fichab("Leyes del Estado que fijan los principios para armonizar las normas autonómicas",
         f"{c('CE', 'Artículo 150', 'El Estado')}; aprecia la necesidad {c('CE', 'Artículo 150', 'las Cortes Generales, por mayoría absoluta de cada Cámara')}",
         f"Cuando {c('CE', 'Artículo 150', 'así lo exija el interés general')}, incluso en materias de competencia autonómica",
         "Mayoría absoluta **de cada Cámara** para apreciar la necesidad",
         "Es el único caso del art. 150 que puede incidir en materias **de las Comunidades**; la mayoría absoluta es de **cada Cámara** (no solo del Congreso)."))}
""", 2)

T.ap("s4", "I.4 Cuadro de los tipos de leyes (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Tipo | Artículo | Quién la aprueba | Mayoría o forma | Rasgo que se pregunta |
|---|---|---|---|---|
| Ley orgánica | 81 | Cortes | Mayoría absoluta del Congreso en votación final | Materias tasadas; ni delegación (82.1) ni Comisiones (75.3) |
| Ley ordinaria | 66.2, 87-91 | Cortes | Mayoría simple | Todo lo no reservado a ley orgánica |
| Ley de bases | 82.2 y 4 | Cortes | Ley ordinaria | Delega en el Gobierno un **texto articulado** (→ III.2) |
| Ley de delegación para refundir | 82.2 y 5 | Cortes | Ley ordinaria | Delega un **texto refundido** (→ III.2) |
| Ley marco | 150.1 | Cortes | Ley ordinaria | Atribuye a las CC. AA. la facultad de dictar normas legislativas |
| Ley de transferencia o delegación | 150.2 | Cortes | **Ley orgánica** | Transfiere o delega facultades estatales |
| Ley de armonización | 150.3 | Cortes | Necesidad apreciada por mayoría absoluta de **cada Cámara** | Armoniza normas autonómicas |

{resumen([
  "La potestad legislativa es de las **Cortes** (66.2); el Rey sanciona en **15 días** y ordena la publicación **inmediata** (91).",
  "Ley orgánica: **materias del 81.1** y **mayoría absoluta del Congreso** en una votación final sobre el conjunto.",
  "Art. 150: ley **marco** (atribuye), de **transferencia o delegación** (por **ley orgánica**) y de **armonización** (mayoría absoluta de **cada Cámara**)."],
  "Siguiente: II. ¿Qué materias exigen ley? La reserva de ley")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Qué materias exigen ley? La reserva de ley", donde(
  "Segunda pregunta. Ya sabemos qué es la ley; ahora, **qué materias solo puede regular una ley**. La Constitución no lo define en un artículo: lo dice materia a materia con fórmulas como «por ley» o «la ley regulará».",
  ["1 La reserva de ley de los derechos (art. 53.1) y la de ley orgánica (art. 81.1)", "2 Otras reservas de ley que se preguntan"]))

T.ap("s5", "II.1 La reserva de ley de los derechos (art. 53.1) y la de ley orgánica (art. 81.1)", f"""
{unidad("1.1 Derechos del Capítulo segundo: «Sólo por ley» (art. 53.1)",
  lit("CE", "Artículo 53", ["Sólo por ley, que en todo caso deberá respetar su contenido esencial"], solo=[1]),
  fichab("Reserva de ley para regular el ejercicio de los derechos y libertades del Capítulo segundo del Título I",
         "Las Cortes, mediante ley (orgánica si se trata del **desarrollo** de derechos fundamentales: art. 81.1)",
         f"La ley {c('CE', 'Artículo 53', 'en todo caso deberá respetar su contenido esencial')}",
         "—",
         "Reserva de **ley** + límite del **contenido esencial**. Además, el decreto-ley no puede **afectar** a los derechos, deberes y libertades del Título I (86.1 → IV.1)."))}

{unidad("1.2 La reserva de ley orgánica (art. 81.1)",
  lit("CE", "Artículo 81", ["Son leyes orgánicas"], solo=[1]),
  fichab("Materias que solo puede regular una ley orgánica",
         "Las Cortes, con la mayoría del 81.2 (→ I.2)",
         "Las del art. 81.1 y **las demás previstas en la Constitución** (por ejemplo, la transferencia o delegación del 150.2 → I.3)",
         "Mayoría absoluta del Congreso en votación final",
         "La lista del 81.1 no es cerrada: añade «las demás previstas en la Constitución»."))}
""", 2)

T.ap("s6", "II.2 Otras reservas de ley que se preguntan", f"""
Ejemplos literales de materias que la Constitución reserva a la ley. Es la técnica que usan las preguntas tipo «¿qué materia tiene reserva de ley?».

{unidad("2.1 Obligaciones militares (art. 30.2)",
  lit("CE", "Artículo 30", ["La ley fijará las obligaciones militares de los españoles"], solo=[2]),
  fichab("Reserva de ley de las obligaciones militares y de la objeción de conciencia", "Las Cortes, por ley", "La ley fija las obligaciones militares y regula la objeción de conciencia y la prestación social sustitutoria", "—",
         "Cayó en 2025 (→ Cierre 1): crear Ministerios, dirigir la política exterior o convocar elecciones **no** se hacen por ley."))}

{unidad("2.2 Prestaciones personales o patrimoniales (art. 31.3)",
  lit("CE", "Artículo 31", ["con arreglo a la ley"], solo=[3]),
  fichab("Reserva de ley de las prestaciones personales o patrimoniales de carácter público", "Las Cortes, por ley",
         "Solo pueden establecerse «con arreglo a la ley»",
         "—", "Incluye las prestaciones **personales** y las **patrimoniales** de carácter público (los tributos, además, en el art. 133 → II.2.4)."))}

{unidad("2.3 Estatuto de los funcionarios (art. 103.3)",
  lit("CE", "Artículo 103", ["La ley regulará el estatuto de los funcionarios públicos"], solo=[3]),
  fichab("Reserva de ley del estatuto de los funcionarios", "Las Cortes, por ley", "Estatuto, acceso por mérito y capacidad, sindicación, incompatibilidades y garantías de imparcialidad", "—",
         "Acceso «de acuerdo con los principios de **mérito y capacidad**» (no «igualdad, mérito y capacidad»: la igualdad está en el art. 23.2)."))}

{unidad("2.4 Tributos, beneficios fiscales y gasto (art. 133)",
  lit("CE", "Artículo 133", ["mediante ley", "en virtud de ley", "de acuerdo con las leyes"]),
  fichab("Reserva de ley tributaria y de gasto", f"{c('CE', 'Artículo 133', 'La potestad originaria para establecer los tributos corresponde exclusivamente al Estado, mediante ley')}; las Comunidades Autónomas y las Corporaciones locales, {c('CE', 'Artículo 133', 'de acuerdo con la Constitución y las leyes')}",
         ["Tributos: potestad originaria del Estado mediante ley (133.1)", "Beneficios fiscales sobre tributos del Estado: en virtud de ley (133.3)", "Obligaciones financieras y gastos: de acuerdo con las leyes (133.4)"],
         "—", "Potestad **originaria**: solo el **Estado**, mediante ley. Las CC. AA. y los entes locales, «de acuerdo con la Constitución y las leyes»."))}

{resumen([
  "La reserva de ley se lee en fórmulas como «Sólo por ley», «La ley regulará», «mediante ley».",
  "Derechos del Capítulo segundo: **sólo por ley**, respetando el **contenido esencial** (53.1).",
  "Ley **orgánica**: materias del 81.1 y las demás previstas en la Constitución.",
  "Ejemplos: obligaciones militares (30.2), prestaciones personales o patrimoniales (31.3), estatuto de los funcionarios (103.3) y tributos (133)."],
  "Siguiente: III. ¿Cómo legisla el Gobierno por delegación? El decreto legislativo")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Cómo legisla el Gobierno por delegación? El decreto legislativo (arts. 82 a 85; Ley 50/1997, art. 24; LJCA, art. 1; LOTC, art. 27)", donde(
  "Tercera pregunta. Las Cortes pueden **delegar** en el Gobierno la potestad de dictar normas con rango de ley. El resultado es el **decreto legislativo**.",
  ["1 La delegación: materias, forma y límites (art. 82.1 y 3)", "2 Ley de bases y texto articulado; ley ordinaria y texto refundido (arts. 82.2, 4 y 5 y 83)", "3 Defensa de la delegación y nombre (arts. 84 y 85; Ley 50/1997, art. 24)", "4 El control del decreto legislativo (art. 82.6; LJCA; LOTC)"]))

T.ap("s7", "III.1 La delegación legislativa: materias, forma y límites (art. 82.1 y 3)", f"""
{unidad("1.1 Qué se delega (art. 82.1)",
  lit("CE", "Artículo 82", ["delegar en el Gobierno la potestad de dictar normas con rango de ley", "no incluidas en el artículo anterior"], solo=[1]),
  fichab("Delegación de la potestad de dictar normas con rango de ley",
         f"{c('CE', 'Artículo 82', 'Las Cortes Generales')} → {c('CE', 'Artículo 82', 'el Gobierno')}",
         f"Sobre {c('CE', 'Artículo 82', 'materias determinadas no incluidas en el artículo anterior')} (nunca materias de ley orgánica)",
         "—",
         "La delegación es **en el Gobierno**; el «artículo anterior» es el **81** (ley orgánica)."))}

{unidad("1.2 Cómo se delega y cuándo se agota (art. 82.3)",
  lit("CE", "Artículo 82", ["de forma expresa para materia concreta y con fijación del plazo para su ejercicio", "se agota por el uso", "No podrá entenderse concedida de modo implícito o por tiempo indeterminado", "subdelegación a autoridades distintas del propio Gobierno"], solo=[3]),
  fichab("Requisitos de la delegación",
         "Las Cortes delegan; el **Gobierno** la ejerce (nunca otras autoridades)",
         ["Expresa", "Para materia concreta", "Con plazo", "Se agota por el uso: con la publicación de la norma"],
         "Plazo: el que fije la ley de delegación (la Constitución no fija uno)",
         "Prohibidas: delegación **implícita**, **por tiempo indeterminado** y **subdelegación** a autoridades distintas del Gobierno."))}
""", 2)

T.ap("s8", "III.2 Ley de bases y texto articulado; ley ordinaria y texto refundido (arts. 82.2, 4 y 5 y 83)", f"""
{unidad("2.1 Dos instrumentos de delegación (art. 82.2)",
  lit("CE", "Artículo 82", ["mediante una ley de bases cuando su objeto sea la formación de textos articulados", "por una ley ordinaria cuando se trate de refundir varios textos legales en uno solo"], solo=[2]),
  fichab("Qué ley delega y qué produce",
         "Las Cortes",
         ["Ley de **bases** → **texto articulado**", "Ley **ordinaria** → **texto refundido** (refundir varios textos legales en uno solo)"],
         "—",
         "Emparejamiento clásico: **bases → articulado**; **ordinaria → refundido**."))}

{unidad("2.2 Contenido de la ley de bases y de la autorización para refundir (art. 82.4 y 5)",
  lit("CE", "Artículo 82", ["delimitarán con precisión el objeto y alcance de la delegación legislativa y los principios y criterios", "si se circunscribe a la mera formulación de un texto único o si se incluye la de regularizar, aclarar y armonizar"], solo=[4, 5]),
  fichab("Qué debe contener cada ley de delegación",
         "Las Cortes",
         ["Ley de bases: objeto y alcance de la delegación, y principios y criterios (82.4)", "Autorización para refundir: ámbito normativo y si es mera formulación de un texto único o incluye **regularizar, aclarar y armonizar** (82.5)"],
         "—",
         f"La facultad de {c('CE', 'Artículo 82', 'regularizar, aclarar y armonizar')} es propia del **texto refundido**, no del articulado."))}

{unidad("2.3 Lo que nunca puede hacer una ley de bases (art. 83)",
  lit("CE", "Artículo 83", ["Autorizar la modificación de la propia ley de bases", "Facultar para dictar normas con carácter retroactivo"]),
  fichab("Prohibiciones de la ley de bases", "Las Cortes, al aprobarla",
         ["No puede autorizar la modificación de la propia ley de bases", "No puede facultar para dictar normas con carácter retroactivo"], "—",
         f"{c('CE', 'Artículo 83', 'en ningún caso')}: son dos prohibiciones absolutas."))}
""", 2)

T.ap("s9", "III.3 Defensa de la delegación y nombre: decretos legislativos (arts. 84 y 85; Ley 50/1997, art. 24)", f"""
{unidad("3.1 El Gobierno puede oponerse a lo que contradiga la delegación (art. 84)",
  lit("CE", "Artículo 84", ["el Gobierno está facultado para oponerse a su tramitación", "proposición de ley para la derogación total o parcial de la ley de delegación"]),
  fichab("Protección de la delegación en vigor frente a proposiciones o enmiendas contrarias",
         f"El Gobierno (se opone); en tal supuesto, {c('CE', 'Artículo 84', 'podrá presentarse una proposición de ley para la derogación total o parcial de la ley de delegación')}",
         "Oposición a la tramitación; como salida, una proposición de ley que derogue total o parcialmente la ley de delegación",
         "—", "Afecta a **proposiciones de ley** y **enmiendas**, no a proyectos del propio Gobierno."))}

{unidad("3.2 Decretos Legislativos (art. 85) y su forma (Ley 50/1997, art. 24.1 a)",
  lit("CE", "Artículo 85", ["Decretos Legislativos"]),
  lit("LGOB", "a24", ["Reales Decretos Legislativos y Reales Decretos-leyes"], solo=[1, 2]),
  fichab("Nombre y forma de la legislación delegada", "El Gobierno (Consejo de Ministros)",
         "Título: **Decretos Legislativos** (CE); forma: **Reales Decretos Legislativos** (Ley del Gobierno)", "—",
         "Cayó dos veces en 2025 (→ Cierre 1): ni «Decretos-leyes» (art. 86), ni «Leyes de bases», ni «Reales Decretos»."))}
""", 2)

T.ap("s10", "III.4 El control del decreto legislativo (art. 82.6; LJCA, art. 1.1; LOTC, art. 27.2)", f"""
{unidad("4.1 Tribunales y fórmulas adicionales (art. 82.6)",
  lit("CE", "Artículo 82", ["Sin perjuicio de la competencia propia de los Tribunales", "fórmulas adicionales de control"], solo=[6]),
  fichab("Control del uso de la delegación", "Los Tribunales y, si la ley de delegación lo prevé, otras fórmulas (p. ej., de las Cortes)",
         "Cada ley de delegación puede añadir fórmulas de control", "—", "Las fórmulas adicionales son **potestativas** («podrán establecer»)."))}

{unidad("4.2 Jurisdicción contencioso-administrativa: el exceso (LJCA, art. 1.1)",
  lit("LJCA", "Artículo 1", ["con los Decretos legislativos cuando excedan los límites de la delegación"], solo=[1]),
  fichab("Control del decreto legislativo por los jueces ordinarios", "Juzgados y Tribunales de lo contencioso-administrativo",
         "Conocen de los decretos legislativos **en lo que excedan** de la delegación", "—",
         f"El juez contencioso solo conoce de los decretos legislativos {c('LJCA', 'Artículo 1', 'cuando excedan los límites de la delegación')}; el control como norma con fuerza de ley es del TC (→ III.4.3)."))}

{unidad("4.3 Tribunal Constitucional (LOTC, art. 27.2 b)",
  lit("LOTC", "aveintisiete", ["con fuerza de Ley", "En el caso de los Decretos legislativos"], solo=[2, 4]),
  fichab("Control de constitucionalidad de las normas con fuerza de ley del Estado", "El Tribunal Constitucional",
         "Recurso y cuestión de inconstitucionalidad contra leyes y disposiciones normativas con fuerza de ley (decretos legislativos y decretos-leyes)", "—",
         "Para los decretos legislativos, la competencia del TC se entiende **sin perjuicio** del art. 82.6 CE (control de los Tribunales ordinarios)."))}

{resumen([
  "Delegan las **Cortes** en el **Gobierno**, de forma **expresa**, para **materia concreta** y con **plazo**; se agota por el uso; nunca en materias de **ley orgánica** (82.1 y 3).",
  "**Ley de bases → texto articulado**; **ley ordinaria → texto refundido** (82.2); la ley de bases no puede autorizar su propia modificación ni normas retroactivas (83).",
  "El resultado se llama **Decreto Legislativo** (85) y adopta la forma de **Real Decreto Legislativo** (Ley 50/1997, art. 24).",
  "Control: Tribunales y fórmulas adicionales (82.6); la jurisdicción contencioso-administrativa, en lo que exceda la delegación; el TC, como norma con fuerza de ley."],
  "Siguiente: IV. ¿Cómo legisla el Gobierno por urgencia? El decreto-ley")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Cómo legisla el Gobierno por urgencia? El decreto-ley (art. 86; Reglamento del Congreso, art. 151)", donde(
  "Cuarta pregunta. Sin delegación de las Cortes, el Gobierno puede dictar normas con rango de ley en caso de **extraordinaria y urgente necesidad**: el **decreto-ley**. Es provisional y el Congreso debe convalidarlo o derogarlo.",
  ["1 Presupuesto y límites materiales (art. 86.1)", "2 Convalidación o derogación por el Congreso (art. 86.2 y Reglamento del Congreso, art. 151)", "3 Tramitación como proyecto de ley (arts. 86.3 y 151.4 y 5)", "4 Cuadro comparativo: decreto legislativo y decreto-ley"]))

T.ap("s11", "IV.1 Presupuesto y límites materiales del decreto-ley (art. 86.1)", f"""
{unidad("1.1 Presupuesto habilitante y materias vedadas (art. 86.1)",
  lit("CE", "Artículo 86", ["En caso de extraordinaria y urgente necesidad", "disposiciones legislativas provisionales", "no podrán afectar al ordenamiento de las instituciones básicas del Estado, a los derechos, deberes y libertades de los ciudadanos regulados en el Título I, al régimen de las Comunidades Autónomas ni al Derecho electoral general"], solo=[1]),
  fichab("Disposiciones legislativas provisionales del Gobierno",
         c("CE", "Artículo 86", "el Gobierno"),
         [f"::Solo {c('CE', 'Artículo 86', 'En caso de extraordinaria y urgente necesidad')}. No pueden afectar a:", "El ordenamiento de las instituciones básicas del Estado", "Los derechos, deberes y libertades de los ciudadanos del Título I", "El régimen de las Comunidades Autónomas", "El Derecho electoral general"],
         "—",
         "Son **cuatro** límites materiales. La necesidad es «extraordinaria **y** urgente» (las dos). Son **provisionales** hasta que el Congreso se pronuncie (→ IV.2)."))}
""", 2)

T.ap("s12", "IV.2 Convalidación o derogación por el Congreso (art. 86.2 y Reglamento del Congreso, art. 151)", f"""
{unidad("2.1 El mandato constitucional (art. 86.2)",
  lit("CE", "Artículo 86", ["inmediatamente sometidos a debate y votación de totalidad al Congreso de los Diputados", "en el plazo de los treinta días siguientes a su promulgación", "convalidación o derogación", "procedimiento especial y sumario"], solo=[2]),
  fichab("Control parlamentario del decreto-ley", "El **Congreso de los Diputados** (convocado al efecto si no está reunido); el Senado no interviene",
         "Debate y votación de **totalidad**; el Congreso se pronuncia **expresamente**: convalidación o derogación",
         f"{c('CE', 'Artículo 86', 'en el plazo de los treinta días siguientes a su promulgación')}",
         "**30 días** desde la **promulgación** (no desde la publicación). Solo el **Congreso**. Debate y votación **de totalidad**."))}

{unidad("2.2 Cómo se vota (Reglamento del Congreso, art. 151.1 a 3 y 6)",
  lit("RCD", "art151", ["en el Pleno de la Cámara o de la Diputación Permanente", "antes de transcurrir los treinta días siguientes a su promulgación", "Un miembro del Gobierno expondrá ante la Cámara las razones", "los votos afirmativos se entenderán favorables a la convalidación y los negativos favorables a la derogación", 'se publicará en el "Boletín Oficial del Estado"'], solo=[1, 2, 3, 6]),
  fichab("Procedimiento de convalidación", "Pleno del Congreso o **Diputación Permanente**; expone un **miembro del Gobierno**",
         ["Debate como los de totalidad", "Votos **afirmativos** = convalidación; **negativos** = derogación", "El acuerdo se publica en el BOE"],
         "Antes de que pasen **30 días** desde la promulgación; puede incluirse en el orden del día en cuanto se publique en el BOE",
         "También puede convalidar la **Diputación Permanente**. Los votos «sí» convalidan."))}
""", 2)

T.ap("s13", "IV.3 Tramitación como proyecto de ley (art. 86.3 y Reglamento del Congreso, art. 151.4 y 5)", f"""
{unidad("3.1 Proyecto de ley por urgencia (art. 86.3)",
  lit("CE", "Artículo 86", ["las Cortes podrán tramitarlos como proyectos de ley por el procedimiento de urgencia"], solo=[3]),
  lit("RCD", "art151", ["la Presidencia preguntará si algún grupo parlamentario desea que se tramite como proyecto de ley", "sin que sean admisibles las enmiendas de totalidad de devolución", "entre legislaturas"], solo=[4, 5]),
  fichab("Conversión del decreto-ley en ley", "Las Cortes (a solicitud de un grupo, decide la Cámara); entre legislaturas, la Diputación Permanente",
         "Tras convalidarlo, como **proyecto de ley** por el procedimiento de **urgencia**; sin enmiendas de totalidad de devolución",
         "Durante el plazo de 30 días del 86.2",
         "Primero se **convalida** y después se pregunta si se tramita como proyecto de ley. No caben enmiendas de **totalidad de devolución**."))}
""", 2)

T.ap("s14", "IV.4 Cuadro comparativo: decreto legislativo y decreto-ley (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| | Decreto legislativo | Decreto-ley |
|---|---|---|
| Artículo | 82 a 85 | 86 |
| Origen | **Delegación** de las Cortes (ley de bases o ley ordinaria) | **Extraordinaria y urgente necesidad** |
| Materias vedadas | Las de **ley orgánica** (82.1) | Instituciones básicas, derechos del Título I, régimen de las CC. AA., Derecho electoral general (86.1) |
| Intervención posterior de las Cortes | Fórmulas adicionales de control si la ley de delegación las prevé (82.6) | **Convalidación o derogación** por el **Congreso** en **30 días** (86.2) |
| Forma (Ley 50/1997, art. 24) | Real Decreto Legislativo | Real Decreto-ley |
| Control judicial | Contencioso, en lo que exceda la delegación; TC | TC |

{resumen([
  "Decreto-ley: **extraordinaria y urgente necesidad**; disposiciones **provisionales**; **cuatro** límites materiales (86.1).",
  "El **Congreso** lo convalida o deroga en **30 días desde la promulgación**, en votación de **totalidad** (86.2); también la **Diputación Permanente** (RCD 151).",
  "Puede tramitarse como **proyecto de ley por urgencia**, sin enmiendas de totalidad de devolución (86.3; RCD 151.4)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_L47 = examen("L", 47, {
  "a": f"«Decretos-leyes» son las disposiciones legislativas provisionales del art. 86, dictadas {c('CE', 'Artículo 86', 'En caso de extraordinaria y urgente necesidad')}, no legislación delegada.",
  "b": "La ley de bases es la ley de las Cortes que **otorga** la delegación (art. 82.2), no la disposición del Gobierno que la ejerce.",
  "c": f"Literal del art. 85: {c('CE', 'Artículo 85', 'recibirán el título de Decretos Legislativos')}.",
  "d": "Las leyes marco son leyes de las Cortes que atribuyen facultades normativas a las Comunidades Autónomas (art. 150.1)."},
  [("Decretos Legislativos", "CE", "Artículo 85", "Las disposiciones del Gobierno que contengan legislación delegada recibirán el título de Decretos Legislativos")])
EX_P47 = examen("P", 47, {
  "a": f"«Decretos-leyes»: art. 86, {c('CE', 'Artículo 86', 'disposiciones legislativas provisionales')} por extraordinaria y urgente necesidad.",
  "b": f"Literal del art. 85: {c('CE', 'Artículo 85', 'recibirán el título de Decretos Legislativos')}.",
  "c": "«Reales Decretos» es la forma de las normas reglamentarias del Consejo de Ministros (Ley 50/1997, art. 24.1 c); la legislación delegada adopta la de Reales Decretos Legislativos (art. 24.1 a).",
  "d": "Los reglamentos no tienen rango de ley; el art. 85 se refiere a la legislación **delegada**, con rango de ley."},
  [("Decretos Legislativos", "CE", "Artículo 85", "Las disposiciones del Gobierno que contengan legislación delegada recibirán el título de Decretos Legislativos")])
EX_P44 = examen("P", 44, {
  "a": f"No es reserva de ley: corresponde al Presidente del Gobierno {c('LGOB', 'a2', 'Crear, modificar y suprimir, por Real Decreto, los Departamentos Ministeriales')} (Ley 50/1997, art. 2.2 j).",
  "b": f"No es reserva de ley: {c('CE', 'Artículo 97', 'El Gobierno dirige la política interior y exterior')} (art. 97).",
  "c": f"No es reserva de ley: es función del Rey {c('CE', 'Artículo 62', 'convocar elecciones en los términos previstos en la Constitución')} (art. 62 b).",
  "d": f"Literal del art. 30.2: {c('CE', 'Artículo 30', 'La ley fijará las obligaciones militares de los españoles')}."},
  [("obligaciones militares de los españoles", "CE", "Artículo 30", "La ley fijará las obligaciones militares de los españoles")])
EX_L7 = examen("L", 7, {
  "a": f"Literal del art. 75.3: quedan exceptuadas de la delegación en Comisiones {c('CE', 'Artículo 75', 'las leyes orgánicas y de bases')}.",
  "b": "Una ley ordinaria sectorial no está en la lista de excepciones del art. 75.3: puede delegarse.",
  "c": "La delegación del art. 75.2 alcanza a la aprobación de **proyectos o proposiciones** de ley: una proposición ordinaria puede delegarse.",
  "d": f"Es justo lo que permite el art. 75.2: {c('CE', 'Artículo 75', 'El Pleno podrá, no obstante, recabar en cualquier momento el debate y votación')}."},
  [("ley orgánica", "CE", "Artículo 75", "las leyes orgánicas y de bases")])

T.ap("s15", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **tres** preguntas de este tema (dos sobre el art. 85 y una sobre la reserva de ley) y **una** relacionada. Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-L 2025, pregunta 47 · Decretos Legislativos (→ III.3.2)", EX_L47,
  "### GACE-P 2025, pregunta 47 · Decretos Legislativos (→ III.3.2)", EX_P47,
  "### GACE-P 2025, pregunta 44 · Reserva de ley (→ II.2.1)", EX_P44,
  "### GACE-L 2025, pregunta 7 · Delegación en Comisiones (relacionada; → I.1.2)", EX_L7,
  "### Cómo se pregunta",
  "!> El art. 85 se pregunta con distractores que son **otras figuras del tema**: decretos-leyes (86), leyes de bases (82.2), leyes marco (150.1). Saber **qué produce cada una** resuelve la pregunta.",
]))

T.ap("s16", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. La ley y sus tipos | Potestad legislativa de las Cortes (66.2); sanción del Rey (91); ley orgánica (81); leyes del 150 | LO: **mayoría absoluta del Congreso** en **votación final**; sanción en **15 días** |
| II. Reserva de ley | «Sólo por ley» y contenido esencial (53.1); ley orgánica (81.1); ejemplos (30.2, 31.3, 103.3, 133) | **Obligaciones militares** por ley (30.2) |
| III. Decreto legislativo | Delegación expresa, materia concreta, plazo; bases → articulado; ordinaria → refundido; arts. 83-85 | **Decretos Legislativos** (85); nunca materias de LO (82.1) |
| IV. Decreto-ley | Extraordinaria y urgente necesidad; cuatro límites; convalidación | **30 días desde la promulgación**; solo el **Congreso** |

?> **Trampas frecuentes:** «treinta días desde la **publicación**» (es desde la **promulgación**); «el **Senado** convalida» (solo el **Congreso**); «la ley de bases produce un texto **refundido**» (produce un texto **articulado**); «mayoría absoluta **de ambas Cámaras**» para la ley orgánica (es del **Congreso**).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
T.q("CE", "Artículo 81", "Ley orgánica", "Según el artículo 81.2 de la Constitución, la aprobación, modificación o derogación de las leyes orgánicas exigirá:",
    ["Mayoría absoluta del Congreso, en una votación final sobre el conjunto del proyecto.", "Mayoría absoluta de ambas Cámaras, en una votación final sobre el conjunto del proyecto.", "Mayoría de tres quintos del Congreso en cada artículo del proyecto.", "Mayoría absoluta del Congreso en la votación de totalidad inicial."],
    "Art. 81.2 CE: «mayoría absoluta del Congreso, en una votación final sobre el conjunto del proyecto».", "mayoría absoluta del Congreso, en una votación final sobre el conjunto del proyecto")
T.q("CE", "Artículo 81", "Ley orgánica", "¿Cuál de las siguientes materias corresponde a ley orgánica según el artículo 81.1 de la Constitución?",
    ["El régimen electoral general.", "La regulación de los tributos locales.", "Los Presupuestos Generales del Estado.", "La legislación básica sobre medio ambiente."],
    "Art. 81.1 CE: desarrollo de derechos fundamentales y libertades públicas, Estatutos de Autonomía, régimen electoral general y demás previstas en la Constitución.", "el régimen electoral general")
T.q("CE", "Artículo 81", "Ley orgánica", "Según el artículo 81.1 de la Constitución, son leyes orgánicas las que aprueben:",
    ["Los Estatutos de Autonomía.", "Los Reglamentos de las Cámaras.", "Los Presupuestos de las Comunidades Autónomas.", "Los textos refundidos."],
    "Art. 81.1 CE: «las que aprueben los Estatutos de Autonomía».", "las que aprueben los Estatutos de Autonomía")
T.q("CE", "Artículo 91", "La ley", "Según el artículo 91 de la Constitución, el Rey sancionará las leyes aprobadas por las Cortes Generales en el plazo de:",
    ["Quince días.", "Diez días.", "Un mes.", "Veinte días."], "Art. 91 CE: «en el plazo de quince días».", "en el plazo de quince días")
T.q("CE", "Artículo 66", "La ley", "Según el artículo 66.2 de la Constitución, la potestad legislativa del Estado la ejercen:",
    ["Las Cortes Generales.", "El Gobierno y las Cortes Generales.", "El Congreso de los Diputados.", "El Rey, a propuesta de las Cortes Generales."], "Art. 66.2 CE.", "Las Cortes Generales ejercen la potestad legislativa del Estado")
T.q("CE", "Artículo 150", "Leyes del art. 150", "Según el artículo 150.2 de la Constitución, el Estado podrá transferir o delegar en las Comunidades Autónomas facultades correspondientes a materia de titularidad estatal mediante:",
    ["Ley orgánica.", "Ley marco.", "Ley de armonización.", "Ley ordinaria aprobada por mayoría absoluta de cada Cámara."], "Art. 150.2 CE: «mediante ley orgánica».", "mediante ley orgánica")
T.q("CE", "Artículo 150", "Leyes del art. 150", "Según el artículo 150.3 de la Constitución, la apreciación de la necesidad de dictar leyes de armonización corresponde:",
    ["A las Cortes Generales, por mayoría absoluta de cada Cámara.", "Al Congreso, por mayoría absoluta.", "Al Gobierno, previo dictamen del Consejo de Estado.", "Al Senado, por mayoría de tres quintos."], "Art. 150.3 CE.", "Corresponde a las Cortes Generales, por mayoría absoluta de cada Cámara, la apreciación de esta necesidad")
T.q("CE", "Artículo 150", "Leyes del art. 150", "Según el artículo 150.1 de la Constitución, las Cortes Generales podrán atribuir a las Comunidades Autónomas la facultad de dictar normas legislativas, en materias de competencia estatal, en el marco de los principios, bases y directrices fijados por:",
    ["Una ley estatal.", "Un real decreto del Gobierno.", "Una ley orgánica de transferencia.", "Los Estatutos de Autonomía."], "Art. 150.1 CE (ley marco).", "en el marco de los principios, bases y directrices fijados por una ley estatal")
T.q("CE", "Artículo 53", "Reserva de ley", "Según el artículo 53.1 de la Constitución, el ejercicio de los derechos y libertades del Capítulo segundo del Título I solo podrá regularse:",
    ["Por ley, que en todo caso deberá respetar su contenido esencial.", "Por ley o por reglamento, respetando su contenido esencial.", "Por ley orgánica, en todo caso.", "Por real decreto-ley, en caso de urgencia."], "Art. 53.1 CE.", "Sólo por ley, que en todo caso deberá respetar su contenido esencial")
T.q("CE", "Artículo 133", "Reserva de ley", "Según el artículo 133.1 de la Constitución, la potestad originaria para establecer los tributos corresponde:",
    ["Exclusivamente al Estado, mediante ley.", "Al Estado y a las Comunidades Autónomas, mediante ley.", "Al Gobierno, mediante real decreto.", "A las Cortes y a las Corporaciones locales."], "Art. 133.1 CE.", "corresponde exclusivamente al Estado, mediante ley")
T.q("CE", "Artículo 31", "Reserva de ley", "Según el artículo 31.3 de la Constitución, las prestaciones personales o patrimoniales de carácter público solo podrán establecerse:",
    ["Con arreglo a la ley.", "Mediante ley orgánica.", "Por real decreto acordado en Consejo de Ministros.", "Mediante ordenanza fiscal."], "Art. 31.3 CE.", "Sólo podrán establecerse prestaciones personales o patrimoniales de carácter público con arreglo a la ley")
T.q("CE", "Artículo 103", "Reserva de ley", "Según el artículo 103.3 de la Constitución, el acceso a la función pública se regulará por la ley de acuerdo con los principios de:",
    ["Mérito y capacidad.", "Igualdad, mérito y capacidad.", "Publicidad y concurrencia.", "Objetividad e imparcialidad."], "Art. 103.3 CE: «de acuerdo con los principios de mérito y capacidad».", "de acuerdo con los principios de mérito y capacidad")
T.q("CE", "Artículo 82", "Decreto legislativo", "Según el artículo 82.1 de la Constitución, las Cortes Generales podrán delegar en el Gobierno la potestad de dictar normas con rango de ley sobre materias determinadas:",
    ["No incluidas en el artículo 81 (leyes orgánicas).", "Incluidas en el artículo 81, con mayoría absoluta.", "Relativas al régimen electoral general.", "Relativas a los derechos fundamentales, con autorización del Senado."], "Art. 82.1 CE: «materias determinadas no incluidas en el artículo anterior».", "materias determinadas no incluidas en el artículo anterior")
T.q("CE", "Artículo 82", "Decreto legislativo", "Según el artículo 82.2 de la Constitución, cuando el objeto de la delegación sea la formación de textos articulados, deberá otorgarse mediante:",
    ["Una ley de bases.", "Una ley ordinaria.", "Una ley orgánica.", "Un acuerdo del Pleno del Congreso."], "Art. 82.2 CE.", "mediante una ley de bases cuando su objeto sea la formación de textos articulados")
T.q("CE", "Artículo 82", "Decreto legislativo", "Según el artículo 82.2 de la Constitución, cuando se trate de refundir varios textos legales en uno solo, la delegación legislativa deberá otorgarse mediante:",
    ["Una ley ordinaria.", "Una ley de bases.", "Una ley orgánica.", "Un real decreto legislativo."], "Art. 82.2 CE.", "por una ley ordinaria cuando se trate de refundir varios textos legales en uno solo")
T.q("CE", "Artículo 82", "Decreto legislativo", "Según el artículo 82.3 de la Constitución, la delegación legislativa se agota:",
    ["Por el uso que de ella haga el Gobierno mediante la publicación de la norma correspondiente.", "A los seis meses de su otorgamiento.", "Con la convalidación del Congreso.", "Al finalizar la legislatura en la que se otorgó."], "Art. 82.3 CE.", "La delegación se agota por el uso que de ella haga el Gobierno mediante la publicación de la norma correspondiente")
T.q("CE", "Artículo 82", "Decreto legislativo", "Según el artículo 82.3 de la Constitución, la delegación legislativa:",
    ["No podrá permitir la subdelegación a autoridades distintas del propio Gobierno.", "Podrá entenderse concedida de modo implícito.", "Podrá otorgarse por tiempo indeterminado.", "Podrá subdelegarse en los Ministros."], "Art. 82.3 CE.", "Tampoco podrá permitir la subdelegación a autoridades distintas del propio Gobierno")
T.q("CE", "Artículo 82", "Decreto legislativo", "Según el artículo 82.5 de la Constitución, la autorización para refundir textos legales especificará si se circunscribe a la mera formulación de un texto único o si incluye la de:",
    ["Regularizar, aclarar y armonizar los textos legales que han de ser refundidos.", "Modificar y derogar los textos legales que han de ser refundidos.", "Desarrollar reglamentariamente los textos legales refundidos.", "Dictar normas con carácter retroactivo."], "Art. 82.5 CE.", "regularizar, aclarar y armonizar los textos legales que han de ser refundidos")
T.q("CE", "Artículo 83", "Decreto legislativo", "Según el artículo 83 de la Constitución, las leyes de bases no podrán en ningún caso:",
    ["Facultar para dictar normas con carácter retroactivo.", "Delimitar el objeto y alcance de la delegación.", "Fijar los principios y criterios de la delegación.", "Establecer fórmulas adicionales de control."], "Art. 83 b) CE. Las demás son contenido propio o posible de la ley de bases (82.4 y 6).", "Facultar para dictar normas con carácter retroactivo")
T.q("CE", "Artículo 84", "Decreto legislativo", "Según el artículo 84 de la Constitución, cuando una proposición de ley o una enmienda fuere contraria a una delegación legislativa en vigor:",
    ["El Gobierno está facultado para oponerse a su tramitación.", "La Mesa del Congreso deberá inadmitirla.", "El Senado podrá vetarla por mayoría absoluta.", "La delegación quedará automáticamente derogada."], "Art. 84 CE.", "el Gobierno está facultado para oponerse a su tramitación")
T.q("CE", "Artículo 85", "Decreto legislativo", "Según el artículo 85 de la Constitución, las disposiciones del Gobierno que contengan legislación delegada recibirán el título de:",
    ["Decretos Legislativos.", "Decretos-leyes.", "Leyes de bases.", "Reales Decretos."], "Art. 85 CE.", "recibirán el título de Decretos Legislativos")
T.q("LJCA", "Artículo 1", "Decreto legislativo", "Según el artículo 1.1 de la Ley 29/1998, reguladora de la Jurisdicción Contencioso-administrativa, los Juzgados y Tribunales de este orden conocerán de las pretensiones que se deduzcan en relación con los Decretos legislativos:",
    ["Cuando excedan los límites de la delegación.", "En todo caso.", "Solo si no han sido convalidados por el Congreso.", "Nunca: su control corresponde en exclusiva al Tribunal Constitucional."], "Art. 1.1 LJCA.", "con los Decretos legislativos cuando excedan los límites de la delegación")
T.q("CE", "Artículo 86", "Decreto-ley", "Según el artículo 86.1 de la Constitución, el Gobierno podrá dictar decretos-leyes:",
    ["En caso de extraordinaria y urgente necesidad.", "En caso de extraordinaria o urgente necesidad.", "Cuando lo autorice una ley de bases.", "Durante el estado de alarma."], "Art. 86.1 CE: «extraordinaria **y** urgente necesidad».", "En caso de extraordinaria y urgente necesidad")
T.q("CE", "Artículo 86", "Decreto-ley", "Según el artículo 86.1 de la Constitución, los decretos-leyes NO podrán afectar a:",
    ["El régimen de las Comunidades Autónomas.", "La organización de los Ministerios.", "Las subvenciones públicas.", "Las retribuciones de los funcionarios."], "Art. 86.1 CE: instituciones básicas del Estado, derechos del Título I, régimen de las Comunidades Autónomas y Derecho electoral general.", "al régimen de las Comunidades Autónomas")
T.q("CE", "Artículo 86", "Decreto-ley", "Según el artículo 86.2 de la Constitución, los decretos-leyes deberán ser sometidos a debate y votación de totalidad al Congreso en el plazo de:",
    ["Los treinta días siguientes a su promulgación.", "Los treinta días siguientes a su publicación.", "Los quince días siguientes a su promulgación.", "Los dos meses siguientes a su publicación."], "Art. 86.2 CE: «treinta días siguientes a su promulgación».", "en el plazo de los treinta días siguientes a su promulgación")
T.q("CE", "Artículo 86", "Decreto-ley", "Según el artículo 86.2 de la Constitución, el pronunciamiento sobre la convalidación o derogación de un decreto-ley corresponde:",
    ["Al Congreso de los Diputados.", "A las Cortes Generales en sesión conjunta.", "Al Senado.", "Al Congreso y al Senado sucesivamente."], "Art. 86.2 CE.", "El Congreso habrá de pronunciarse expresamente dentro de dicho plazo sobre su convalidación o derogación")
T.q("CE", "Artículo 86", "Decreto-ley", "Según el artículo 86.3 de la Constitución, durante el plazo de convalidación las Cortes podrán tramitar los decretos-leyes:",
    ["Como proyectos de ley por el procedimiento de urgencia.", "Como proposiciones de ley por el procedimiento ordinario.", "Como leyes orgánicas.", "En lectura única ante el Senado."], "Art. 86.3 CE.", "las Cortes podrán tramitarlos como proyectos de ley por el procedimiento de urgencia")
T.q("RCD", "art151", "Decreto-ley", "Según el artículo 151.3 del Reglamento del Congreso de los Diputados, en la votación sobre un Real Decreto-ley:",
    ["Los votos afirmativos se entienden favorables a la convalidación y los negativos favorables a la derogación.", "Los votos afirmativos se entienden favorables a la derogación.", "Las abstenciones se computan como votos favorables a la convalidación.", "Se requiere mayoría absoluta para la convalidación."], "Art. 151.3 RCD.", "los votos afirmativos se entenderán favorables a la convalidación y los negativos favorables a la derogación")
T.q("RCD", "art151", "Decreto-ley", "Según el artículo 151.1 del Reglamento del Congreso, el debate y votación sobre la convalidación o derogación de un Real Decreto-ley se realizará:",
    ["En el Pleno de la Cámara o de la Diputación Permanente.", "En la Comisión competente por razón de la materia.", "En el Pleno del Senado.", "En la Junta de Portavoces."], "Art. 151.1 RCD.", "se realizará en el Pleno de la Cámara o de la Diputación Permanente")
T.q("RCD", "art151", "Decreto-ley", "Según el artículo 151.4 del Reglamento del Congreso, si un Real Decreto-ley convalidado se tramita como proyecto de ley:",
    ["Se tramita por el procedimiento de urgencia, sin que sean admisibles las enmiendas de totalidad de devolución.", "Se tramita por el procedimiento ordinario, con todas las enmiendas.", "Solo se admiten enmiendas de totalidad de devolución.", "Se tramita en lectura única."], "Art. 151.4 RCD.", "se tramitará como proyecto de ley por el procedimiento de urgencia, sin que sean admisibles las enmiendas de totalidad de devolución")
T.q("LGOB", "a24", "Decreto legislativo", "Según el artículo 24.1 a) de la Ley 50/1997, del Gobierno, ¿qué forma revisten las decisiones del Gobierno que aprueban las normas previstas en los artículos 82 y 86 de la Constitución?",
    ["Reales Decretos Legislativos y Reales Decretos-leyes, respectivamente.", "Reales Decretos-leyes y Reales Decretos Legislativos, respectivamente.", "Acuerdos del Consejo de Ministros.", "Reales Decretos acordados en Consejo de Ministros."], "Art. 24.1 a) Ley 50/1997: el 82 da Reales Decretos Legislativos y el 86, Reales Decretos-leyes.", "Reales Decretos Legislativos y Reales Decretos-leyes, las decisiones que aprueban, respectivamente, las normas previstas en los artículos 82 y 86 de la Constitución")
T.real("L", 47, "Decreto legislativo"); T.real("P", 47, "Decreto legislativo"); T.real("P", 44, "Reserva de ley"); T.real("L", 7, "Ley orgánica")

# Flashcards
for q_, a_, cat in [
  ("¿Quién ejerce la potestad legislativa del Estado?", "Las Cortes Generales (art. 66.2 CE).", "La ley"),
  ("¿En qué plazo sanciona el Rey las leyes?", "Quince días; las promulga y ordena su inmediata publicación (art. 91).", "La ley"),
  ("Materias de ley orgánica (art. 81.1)", "Desarrollo de derechos fundamentales y libertades públicas; Estatutos de Autonomía; régimen electoral general; las demás previstas en la Constitución.", "Ley orgánica"),
  ("Mayoría de la ley orgánica (art. 81.2)", "Mayoría absoluta del Congreso, en una votación final sobre el conjunto del proyecto (para aprobar, modificar o derogar).", "Ley orgánica"),
  ("¿Qué leyes no pueden delegarse en las Comisiones Legislativas Permanentes? (art. 75.3)", "Reforma constitucional, cuestiones internacionales, leyes orgánicas y de bases y Presupuestos Generales del Estado.", "Ley orgánica"),
  ("Ley del art. 150.2", "Transferencia o delegación de facultades estatales a las CC. AA., mediante ley orgánica.", "Leyes del art. 150"),
  ("Ley de armonización (art. 150.3): ¿quién aprecia la necesidad y con qué mayoría?", "Las Cortes Generales, por mayoría absoluta de cada Cámara.", "Leyes del art. 150"),
  ("Reserva de ley de los derechos del Capítulo segundo (art. 53.1)", "Sólo por ley, que en todo caso deberá respetar su contenido esencial.", "Reserva de ley"),
  ("¿Qué ley delega la formación de un texto articulado?", "Una ley de bases (art. 82.2).", "Decreto legislativo"),
  ("¿Qué ley delega un texto refundido?", "Una ley ordinaria (art. 82.2).", "Decreto legislativo"),
  ("Requisitos de la delegación legislativa (art. 82.3)", "Expresa, para materia concreta y con plazo; se agota por el uso; ni implícita, ni por tiempo indeterminado, ni subdelegable fuera del Gobierno.", "Decreto legislativo"),
  ("¿Qué no puede hacer nunca una ley de bases? (art. 83)", "Autorizar la modificación de la propia ley de bases y facultar para dictar normas con carácter retroactivo.", "Decreto legislativo"),
  ("Título de la legislación delegada (art. 85)", "Decretos Legislativos.", "Decreto legislativo"),
  ("¿Quién controla el decreto legislativo en lo que excede de la delegación?", "La jurisdicción contencioso-administrativa (art. 1.1 LJCA), sin perjuicio del TC.", "Decreto legislativo"),
  ("Presupuesto del decreto-ley (art. 86.1)", "Extraordinaria y urgente necesidad.", "Decreto-ley"),
  ("Límites materiales del decreto-ley (art. 86.1)", "Instituciones básicas del Estado; derechos, deberes y libertades del Título I; régimen de las CC. AA.; Derecho electoral general.", "Decreto-ley"),
  ("Plazo y órgano de convalidación del decreto-ley (art. 86.2)", "Congreso de los Diputados, en los 30 días siguientes a su promulgación.", "Decreto-ley"),
  ("¿Qué significan los votos afirmativos en la convalidación? (RCD 151.3)", "Convalidación; los negativos, derogación.", "Decreto-ley"),
  ("Tramitación de un decreto-ley como proyecto de ley (art. 86.3; RCD 151.4)", "Por el procedimiento de urgencia; sin enmiendas de totalidad de devolución.", "Decreto-ley"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Ley orgánica", "Ley de las Cortes para las materias del art. 81.1 y las demás previstas en la Constitución; exige mayoría absoluta del Congreso en una votación final sobre el conjunto.", "s2", "Tipos de leyes")
T.glos("Ley marco", "Ley estatal que atribuye a las CC. AA. la facultad de dictar normas legislativas en materias estatales, en el marco de sus principios, bases y directrices (art. 150.1).", "s3", "Tipos de leyes")
T.glos("Ley de armonización", "Ley estatal que fija los principios para armonizar normas autonómicas cuando lo exija el interés general; necesidad apreciada por mayoría absoluta de cada Cámara (art. 150.3).", "s3", "Tipos de leyes")
T.glos("Reserva de ley", "Exigencia constitucional de que una materia la regule una ley (p. ej., «Sólo por ley» en el art. 53.1).", "s5", "Reserva de ley")
T.glos("Contenido esencial", "Límite que la ley reguladora de los derechos del Capítulo segundo debe respetar en todo caso (art. 53.1).", "s5", "Reserva de ley")
T.glos("Delegación legislativa", "Habilitación de las Cortes al Gobierno para dictar normas con rango de ley sobre materias determinadas no reservadas a ley orgánica (art. 82).", "s7", "Decreto legislativo")
T.glos("Ley de bases", "Ley de delegación para la formación de textos articulados; fija objeto, alcance, principios y criterios (art. 82.2 y 4).", "s8", "Decreto legislativo")
T.glos("Texto refundido", "Norma del Gobierno que refunde varios textos legales en uno solo, por delegación mediante ley ordinaria (art. 82.2 y 5).", "s8", "Decreto legislativo")
T.glos("Decreto Legislativo", "Título de las disposiciones del Gobierno que contienen legislación delegada (art. 85); forma: Real Decreto Legislativo.", "s9", "Decreto legislativo")
T.glos("Decreto-ley", "Disposición legislativa provisional del Gobierno en caso de extraordinaria y urgente necesidad, sujeta a convalidación del Congreso (art. 86).", "s11", "Decreto-ley")
T.glos("Convalidación", "Pronunciamiento expreso del Congreso, en los 30 días siguientes a la promulgación, que mantiene el decreto-ley; la alternativa es la derogación (art. 86.2).", "s12", "Decreto-ley")

# Cronología (fechas de los metadatos del BOE)
T.hito("1978", "Constitución Española (27-12-1978; BOE de 29-12-1978)", "Arts. 81 a 86: ley orgánica, delegación legislativa y decreto-ley", "normativo", "s1")
T.hito("1979", "Ley Orgánica 2/1979, de 3 de octubre, del Tribunal Constitucional (BOE de 5-10-1979)", "Art. 27.2: control de las normas con fuerza de ley", "normativo", "s10")
T.hito("1982", "Reglamento del Congreso de los Diputados, aprobado por el Pleno el 10 de febrero de 1982 (BOE de 5-3-1982)", "Art. 151: procedimiento de convalidación de los decretos-leyes", "normativo", "s12")
T.hito("1997", "Ley 50/1997, de 27 de noviembre, del Gobierno (BOE de 28-11-1997)", "Art. 24.1 a): forma de Real Decreto Legislativo y de Real Decreto-ley", "normativo", "s9")
T.hito("1998", "Ley 29/1998, de 13 de julio, de la Jurisdicción Contencioso-administrativa (BOE de 14-7-1998)", "Art. 1.1: control de los decretos legislativos que exceden la delegación", "normativo", "s10")

T.publicar()
