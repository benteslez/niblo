# -*- coding: utf-8 -*-
# Tema I.2 (v4) · Parte 4: bloque II, las garantías.
from v4_util import *

ap("bII", "II. ¿Cómo se protegen? (art. 53 y su desarrollo)", f"""
{donde("Ya sabes qué derechos hay y en qué nivel está cada uno (bloque I). Ahora, **qué mecanismos** aseguran que se respeten y **cuáles corresponden a cada nivel**.",
       ["1 El art. 53 y el mapa de garantías", "2 Garantías normativas (81, 86, 161-162, 167-169)", "3 Procedimiento preferente y sumario (LJCA)", "4 *Habeas corpus* (LO 6/1984)", "5 Recurso de amparo (LOTC)", "6 Cuadro de síntesis"])}

**Orden de estudio.** Primero el art. 53, que reparte las garantías; después cada garantía en el orden de sus artículos; las leyes de desarrollo (LJCA, LO 6/1984, LOTC), en el orden de sus propios artículos. La garantía **institucional** (Defensor del Pueblo, art. 54) tiene bloque propio (→ IV).
""")

# ---------------------------------------------------------------------------
ap("s5", "II.1 El art. 53: las garantías según el nivel del derecho", f"""
### 1.1 Qué es una garantía y qué tipos hay

Reconocer un derecho no basta: hacen falta **mecanismos que aseguren su respeto**. El Capítulo cuarto, «De las garantías de las libertades y derechos fundamentales» (arts. 53 y 54), los recoge junto con otros preceptos. La doctrina los clasifica en tres tipos:

| Tipo | Qué hace | Dónde | Apartado |
|---|---|---|---|
| **Normativas** | Protegen los derechos **frente al legislador** | Arts. 53.1, 81, 86.1, 161.1 a), 167-169 | → II.2 |
| **Jurisdiccionales** | Permiten acudir a un **tribunal** | Arts. 53.2, 17.4, 161.1 b) y 162.1 b) | → II.3 a II.5 |
| **Institucionales** | Encargan su defensa a una **institución** | Art. 54 (Defensor del Pueblo) y art. 124 (Ministerio Fiscal) | → IV y II.1.3 |

{unidad("1.2 Las garantías de las libertades y derechos (art. 53)",
  lit("CE", 53, ["vinculan a todos los poderes públicos", "Sólo por ley, que en todo caso deberá respetar su contenido esencial", "artículo 161, 1, a)", "preferencia y sumariedad", "recurso de amparo ante el Tribunal Constitucional", "objeción de conciencia reconocida en el artículo 30", "informarán la legislación positiva, la práctica judicial y la actuación de los poderes públicos"]),
  fichab("El precepto que **gradúa** las garantías según el lugar del derecho en el Título I",
         ["53.1 → **todo el Capítulo segundo** (arts. 14 a 38)", "53.2 → **art. 14 y Sección 1.ª**; para el amparo, también la **objeción de conciencia** (art. 30)", "53.3 → **Capítulo tercero** (arts. 39 a 52)"],
         ["53.1: vinculan a **todos los poderes públicos**; **reserva de ley** que respete el **contenido esencial**; tutela por el recurso de inconstitucionalidad (art. 161.1 a)", "53.2: ante los tribunales ordinarios, procedimiento de **preferencia y sumariedad**; y, en su caso, **recurso de amparo** ante el TC", "53.3: **informan** la legislación, la práctica judicial y la actuación de los poderes públicos; solo alegables según sus leyes de desarrollo"],
         "—",
         ["53.1 remite al «artículo 161, 1, a)», es decir, al recurso de **inconstitucionalidad**, no al de amparo", "53.2 dice «**Cualquier ciudadano**»", "El amparo llega a la objeción de conciencia; el procedimiento preferente y sumario, **no**"]))}

**Dos ideas que el art. 53.1 condensa** (doctrina, no texto legal):
- **Reserva de ley:** solo una norma con rango de ley puede regular el ejercicio de estos derechos; un reglamento no puede hacerlo por sí solo.
- **Contenido esencial:** ni siquiera la ley puede vaciar el núcleo del derecho. La STC 11/1981 [[TC|https://hj.tribunalconstitucional.es/es-ES/Resolucion/Show/11]] lo define como las facultades sin las cuales el derecho se desnaturaliza o deja de ser reconocible.

### 1.3 Otra garantía institucional: el Ministerio Fiscal (art. 124.1)

Además del Defensor del Pueblo (→ IV), el art. 124.1 encomienda al Ministerio Fiscal {c("CE", 124, "promover la acción de la justicia en defensa de la legalidad, de los derechos de los ciudadanos y del interés público tutelado por la ley")}. Por eso está legitimado en el amparo (→ II.5) y en el *habeas corpus* (→ II.4).
""", 2)

# ---------------------------------------------------------------------------
ap("s5-1", "II.2 Garantías normativas (arts. 81, 86, 161, 162 y 167 a 169)", f"""
Las garantías normativas limitan al **legislador**: quién puede regular los derechos, con qué norma y cómo se controla. Se ven en el orden de sus artículos.

{unidad("2.1 Ley orgánica (art. 81)",
  lit("CE", 81, ["desarrollo de los derechos fundamentales y de las libertades públicas", "mayoría absoluta del Congreso, en una votación final sobre el conjunto del proyecto"]),
  fichab("Reserva de **ley orgánica** para el desarrollo de los derechos fundamentales y libertades públicas",
         "Las Cortes; la mayoría la exige al **Congreso**",
         "Aprobación, modificación o derogación en una **votación final sobre el conjunto del proyecto**",
         "**Mayoría absoluta del Congreso**",
         ["«De los derechos fundamentales y de las libertades públicas» es la rúbrica de la **Sección 1.ª**. Que no alcance al art. 14 ni a la Sección 2.ª es **doctrina del TC** (STC 76/1983 [[TC|https://hj.tribunalconstitucional.es/es-ES/Resolucion/Show/204]]; para la objeción de conciencia, STC 160/1987 [[TC|https://hj.tribunalconstitucional.es/es-ES/Resolucion/Show/892]]), no texto literal", "Mayoría **absoluta**, no tres quintos"]))}

{unidad("2.2 Prohibición del decreto-ley (art. 86.1)",
  lit("CE", 86, ["extraordinaria y urgente necesidad", "a los derechos, deberes y libertades de los ciudadanos regulados en el Título I"], solo=[0], titulo="Artículo 86.1"),
  fichab("Límite material del decreto-ley",
         "El Gobierno",
         "En caso de extraordinaria y urgente necesidad puede dictar decretos-leyes, que **no podrán afectar** a los derechos, deberes y libertades del Título I (ni a otras materias que enumera)",
         "—",
         "La prohibición alcanza a **todo el Título I**, no solo a la Sección 1.ª."))}

{unidad("2.3 Control de constitucionalidad de las leyes (arts. 161.1 y 162.1 CE; art. 32.1 LOTC)",
  lit("CE", 161, ["Del recurso de inconstitucionalidad contra leyes y disposiciones normativas con fuerza de ley", "Del recurso de amparo por violación de los derechos y libertades referidos en el artículo 53, 2"], solo=[0, 1, 2], titulo="Artículo 161.1 a) y b)"),
  lit("CE", 162, ["el Defensor del Pueblo, 50 Diputados, 50 Senadores", "así como el Defensor del Pueblo y el Ministerio Fiscal"]),
  lit("LOTC", "treinta y dos", ["El Defensor del Pueblo."], solo=[0, 1, 2, 3, 4], titulo="Artículo treinta y dos.1 (LOTC)"),
  fichab("Recurso de **inconstitucionalidad** (161.1 a) contra la ley que vulnera un derecho; y recurso de **amparo** (161.1 b), que se estudia en → II.5",
         ["Inconstitucionalidad (162.1 a): Presidente del Gobierno, **Defensor del Pueblo**, 50 Diputados, 50 Senadores, órganos colegiados ejecutivos de las CC. AA. y, en su caso, sus Asambleas", "Amparo (162.1 b): toda persona natural o jurídica con interés legítimo, **Defensor del Pueblo** y **Ministerio Fiscal**"],
         "Ante el Tribunal Constitucional",
         "—",
         ["El **Defensor del Pueblo** es el único que está en **las dos** listas", "El Ministerio Fiscal, solo en la de amparo; los 50 Diputados o Senadores, solo en la de inconstitucionalidad"]))}

{unidad("2.4 Rigidez constitucional (arts. 167 a 169)",
  lit("CE", 168, ["al Capítulo segundo, Sección primera del Título I", "mayoría de dos tercios de cada Cámara", "disolución inmediata de las Cortes", "referéndum"]),
  lit("CE", 169, ["en tiempo de guerra o de vigencia de alguno de los estados previstos en el artículo 116"]),
  fichab("Protección de los derechos frente a la propia reforma de la Constitución",
         ["Reforma **agravada** (168): revisión total o parcial que afecte al Título preliminar, a la **Sección 1.ª** del Capítulo segundo del Título I o al Título II", "Reforma **ordinaria** (167): el resto, incluidos el **art. 14**, la **Sección 2.ª** y el **Capítulo tercero**"],
         ["168: aprobación del principio, **disolución** de las Cortes, ratificación y estudio del nuevo texto por las nuevas Cámaras y **referéndum** obligatorio", "169: no puede **iniciarse** la reforma en tiempo de guerra ni con un estado del art. 116 en vigor"],
         "168: **dos tercios** de cada Cámara (para el principio y para el nuevo texto)",
         "El art. 14 tiene amparo, pero su reforma es **ordinaria**: el 168 solo nombra la Sección primera."))}
""", 2)

# ---------------------------------------------------------------------------
ap("s5-4", "II.3 El procedimiento preferente y sumario (LJCA, arts. 114 a 122)", f"""
Desarrolla la primera vía del art. 53.2 frente a la **Administración**: es el Capítulo I del Título V de la Ley 29/1998, de 13 de julio, reguladora de la Jurisdicción Contencioso-administrativa (BOE-A-1998-16718), «Procedimiento para la protección de los derechos fundamentales de la persona».

{unidad("3.1 Objeto y carácter preferente (art. 114)",
  lit("LJCA", 114, ["artículo 53.2 de la Constitución española", "A todos los efectos, la tramitación de estos recursos tendrá carácter preferente"]),
  fichab(f"El {c('LJCA', 114, 'procedimiento de amparo judicial de las libertades y derechos, previsto en el artículo 53.2 de la Constitución española')}",
         "Quien recurra la actuación administrativa que lesiona un derecho susceptible de amparo",
         f"Solo pretensiones para {c('LJCA', 114, 'restablecer o preservar los derechos o libertades por razón de los cuales el recurso hubiere sido formulado')}",
         "Tramitación **preferente** «a todos los efectos»",
         "Es el «amparo **judicial**» (ante los jueces ordinarios); el amparo **constitucional** es el de la LOTC (→ II.5)."))}

{unidad("3.2 Tramitación (arts. 115 a 121)",
  lit("LJCA", 115, ["será de diez días", "el plazo de diez días se iniciará transcurridos veinte días"]),
  lit("LJCA", 116, ["en el plazo máximo de cinco días", "en el plazo de cinco días", "por plazo de cuarenta y ocho horas"]),
  lit("LJCA", 117, ["antes de transcurrir cinco días"]),
  lit("LJCA", 118, ["plazo improrrogable de ocho días"]),
  lit("LJCA", 119, ["plazo común e improrrogable de ocho días"]),
  lit("LJCA", 120, ["no será en ningún caso superior a veinte días comunes"]),
  lit("LJCA", 121, ["en el plazo de cinco días", "incluso la desviación de poder", "apelación en un solo efecto"]),
  fichab("Un proceso contencioso **abreviado**, con plazos muy cortos",
         "El recurrente; el órgano administrativo; el Ministerio Fiscal; los demandados",
         ["La sentencia estima el recurso si la actuación incurre en cualquier infracción del ordenamiento, **incluso la desviación de poder**, y vulnera un derecho susceptible de amparo (121.2)", f"Contra las sentencias de los Juzgados, {c('LJCA', 121, 'siempre la apelación en un solo efecto')}"],
         ["1 Interposición: **10 días** (115.1); si hubo inactividad, recurso potestativo o vía de hecho sin requerimiento, empiezan **transcurridos 20 días**", "2 Remisión del expediente: máximo **5 días** (116.1); emplazamiento: **5 días** (116.2); expediente tardío: alegaciones en **48 horas** (116.5)", "3 Posible inadmisión: comparecencia antes de **5 días** (117.2)", "4 Demanda: **8 días**, improrrogable (118)", "5 Alegaciones del Fiscal y demandados: **8 días**, común e improrrogable (119)", "6 Prueba: no más de **20 días** comunes (120)", "7 Sentencia: **5 días** (121.1)"],
         "Diez días para recurrir, no los dos meses del recurso contencioso ordinario. Apelación «en un **solo** efecto»."))}

{unidad("3.3 Especialidad del derecho de reunión (art. 122)",
  lit("LJCA", 122, ["dentro de las cuarenta y ocho horas siguientes", "plazo improrrogable de cuatro días", "resolverá sin ulterior recurso"]),
  fichab("Recurso urgente contra la **prohibición o modificación** de una reunión (art. 21 CE → I.5.2)",
         "Los promotores que no aceptan la prohibición o la modificación propuesta por la autoridad",
         f"Audiencia con el representante de la Administración, el Ministerio Fiscal y los promotores; el tribunal solo puede {c('LJCA', 122, 'mantener o revocar la prohibición o las modificaciones propuestas')}",
         ["Recurso: **48 horas** desde la notificación", "Audiencia y resolución: plazo improrrogable de **4 días**", "**Sin ulterior recurso**"],
         "48 horas, **no** 72. La resolución no admite recurso."))}

**Notas del texto consolidado (BOE):**
- Los arts. 116, 119 y 122 dicen «letrado o letrada de la Administración de Justicia»; los arts. 117 y 118 conservan «Secretario judicial».
- Según la **disposición adicional primera de la LO 1/2025, de 2 de enero** (BOE-A-2025-76), las referencias a los Juzgados de lo Contencioso-Administrativo se entienden hechas a las Secciones correspondientes de los **Tribunales de Instancia**.
""", 2)

# ---------------------------------------------------------------------------
ap("s5-5", "II.4 El habeas corpus (art. 17.4 CE y LO 6/1984)", f"""
El art. 17.4 CE ordena: {c("CE", 17, "La ley regulará un procedimiento de «habeas corpus» para producir la inmediata puesta a disposición judicial de toda persona detenida ilegalmente")}. Lo desarrolla la **Ley Orgánica 6/1984, de 24 de mayo**, reguladora del procedimiento de «Habeas Corpus» (BOE-A-1984-11620; última modificación: 14 de noviembre de 2024). Es la garantía judicial **específica de la libertad personal** (art. 17 → I.4.3).

{unidad("4.1 Objeto y supuestos de detención ilegal (art. 1)",
  lit("HC", "primero", ["inmediata puesta a disposición de la Autoridad judicial competente"]),
  fichab("Procedimiento rápido para que un juez compruebe de inmediato la legalidad de una privación de libertad",
         "Cualquier persona detenida ilegalmente",
         ["::Cuatro supuestos de detención ilegal:", "a) sin supuesto legal o sin las formalidades y requisitos de las leyes", f"b) {c('HC', 'primero', 'Las que estén ilícitamente internadas en cualquier establecimiento o lugar')}", f"c) retenidas más del plazo legal sin libertad ni entrega {c('HC', 'primero', 'al Juez más próximo al lugar de la detención')}", "d) sin respeto de los derechos que la Constitución y las leyes procesales garantizan al detenido"],
         "—",
         "También es ilegal la detención **legal en su origen** si se prolonga más de lo debido (c) o no se respetan los derechos del detenido (d)."))}

{unidad("4.2 Competencia (art. 2)",
  lit("HC", "segundo", ["el Juez de Instrucción del lugar en que se encuentre la persona privada de libertad", "Juez Central de Instrucción", "Juez Togado Militar de Instrucción"]),
  fichab("Qué juez conoce del *habeas corpus*",
         ["Regla: el **Juez de Instrucción del lugar donde se encuentre** la persona privada de libertad", "Si no consta, el del lugar de la detención; en defecto de ambos, el del lugar de las últimas noticias", "Detención por terrorismo (ley orgánica del art. 55.2 CE): el **Juez Central de Instrucción**", "Jurisdicción Militar: el **Juez Togado Militar de Instrucción** de la circunscripción de la detención"],
         "—",
         "—",
         ["El juez es el del lugar **donde esté** el detenido, no el de la detención (salvo que aquel no conste)", f"Tribunales de Instancia: el texto consolidado de la LO 6/1984 no lleva nota (la LECrim y la LJCA sí), pero la disposición adicional primera de la LO 1/2025 (BOE-A-2025-76) es general: {c('LO1_2025', 'Disposición adicional primera', 'Las referencias realizadas en las leyes y en el resto de disposiciones de nuestro ordenamiento jurídico a los Juzgados de … de Instrucción … se entenderán referidas a las Secciones del orden jurisdiccional correspondiente de los Tribunales de Instancia')}; y {c('LO1_2025', 'Disposición adicional primera', 'La misma consideración tendrán las referencias a los Juzgados Centrales respecto de las correspondientes Secciones del Tribunal Central de Instancia')}. En el examen, la letra de la LO 6/1984: «Juez de Instrucción» y «Juez Central de Instrucción»"]))}

{unidad("4.3 Legitimación e iniciación (arts. 3 a 5)",
  lit("HC", "tercero", ["El Ministerio Fiscal.", "El Defensor del Pueblo.", "de oficio"]),
  lit("HC", "cuarto", ["no siendo preceptiva la intervención de Abogado ni de Procurador"]),
  lit("HC", "quinto", []),
  fichab("Quién puede pedirlo y cómo se pide",
         ["El privado de libertad, su cónyuge o persona unida por análoga relación de afectividad, descendientes, ascendientes, hermanos y, en su caso, representantes legales o de apoyo", "El **Ministerio Fiscal**", "El **Defensor del Pueblo**", "El **abogado defensor**", "**De oficio**, el juez competente"],
         ["Por **escrito o comparecencia**, sin Abogado ni Procurador (art. 4)", f"Quien custodia al detenido pone la solicitud {c('HC', 'quinto', 'inmediatamente en conocimiento del Juez competente')} (art. 5)"],
         "—",
         "No es preceptiva la intervención de **Abogado ni Procurador**. Lo puede iniciar el juez **de oficio**."))}

{unidad("4.4 Tramitación y resolución (arts. 6 a 9)",
  lit("HC", "sexto", ["no cabrá recurso alguno"]),
  lit("HC", "séptimo", ["En el plazo de veinticuatro horas"]),
  lit("HC", "octavo", ["mediante auto motivado"]),
  lit("HC", "noveno", ["temeridad o mala fe"]),
  lit("HC", "Disposición final", []),
  fichab("Las fases: admisión, actuaciones, resolución y responsabilidades",
         "El Juez; el Ministerio Fiscal; la autoridad que detuvo; el detenido y su abogado",
         ["Admisión (6): previo traslado al Fiscal, auto de incoación o de denegación, **sin recurso**", "Actuaciones (7): el juez hace presentar al detenido o va donde esté; oye al detenido, a su abogado, al Fiscal y a la autoridad; admite pruebas", "Resolución (8), por **auto motivado**: **archivo** si la detención es legal; si no, **libertad**, otro establecimiento o custodia, o **puesta inmediata a disposición judicial**", "Responsabilidades (9): testimonio para perseguir delitos; costas al solicitante si hubo **temeridad o mala fe**"],
         "Todo en **24 horas** desde el auto de incoación (7)",
         "**24 horas**, no 72. Contra el auto de incoación o denegación **no cabe recurso**."))}
""", 2)

# ---------------------------------------------------------------------------
ap("s5-6", "II.5 El recurso de amparo constitucional (LOTC, arts. 41 a 58)", f"""
Segunda vía del art. 53.2: el **Título III** de la Ley Orgánica 2/1979, de 3 de octubre, del Tribunal Constitucional (BOE-A-1979-23709; última modificación: 2 de agosto de 2024), «Del recurso de amparo constitucional». Es **subsidiario**: frente a actos del Gobierno o de los jueces, antes hay que agotar la vía judicial.

{unidad("5.1 Objeto (art. 41)",
  lit("LOTC", "cuarenta y uno", ["artículos catorce a veintinueve", "objeción de conciencia reconocida en el artículo treinta"]),
  fichab("Recurso ante el TC por lesión de derechos fundamentales",
         f"Protege los {c('LOTC', 'cuarenta y uno', 'artículos catorce a veintinueve de la Constitución')} y la objeción de conciencia del art. 30, frente a los **poderes públicos** (Estado, CC. AA., demás entes públicos, funcionarios y agentes)",
         f"Contra {c('LOTC', 'cuarenta y uno', 'disposiciones, actos jurídicos, omisiones o simple vía de hecho')}; solo pretensiones para restablecer o preservar el derecho",
         "—",
         "Arts. **14 a 29** + **30** (objeción). No llega a los arts. 31 a 38."))}

{unidad("5.2 Las tres vías según el origen de la lesión y la legitimación (arts. 42 a 46)",
  lit("LOTC", "cuarenta y dos", ["dentro del plazo de tres meses"]),
  lit("LOTC", "cuarenta y tres", ["una vez que se haya agotado la vía judicial procedente", "veinte días siguientes a la notificación"]),
  lit("LOTC", "cuarenta y cuatro", ["será de 30 días"]),
  lit("LOTC", "cuarenta y cinco", []),
  lit("LOTC", "cuarenta y seis", ["la persona directamente afectada, el Defensor del Pueblo y el Ministerio Fiscal", "quienes hayan sido parte en el proceso judicial correspondiente"]),
  fichab("Tres amparos distintos según **quién** causó la lesión",
         ["Art. 42 (**Parlamentos**): legitimados la persona **directamente afectada**, el Defensor del Pueblo y el Ministerio Fiscal", "Arts. 43 y 44 (**Gobierno** y **jueces**): quienes fueron **parte en el proceso judicial**, el Defensor del Pueblo y el Ministerio Fiscal"],
         ["42: decisiones o actos **sin valor de ley** de las Cortes o de las Asambleas autonómicas, que sean **firmes**", "43: actos del **Gobierno**, sus autoridades o funcionarios, o de órganos ejecutivos autonómicos: antes, **agotar la vía judicial**", f"44: acto u omisión **inmediato y directo de un órgano judicial**: agotar los recursos, imputación directa al juez y {c('LOTC', 'cuarenta y cuatro', 'Que se haya denunciado formalmente en el proceso, si hubo oportunidad')}", "Si recurren el Defensor o el Fiscal, la Sala lo comunica a los posibles agraviados y lo anuncia en el BOE (46.2)"],
         ["Parlamentos: **3 meses** desde que el acto es firme", "Gobierno: **20 días** desde la notificación de la resolución judicial", "Jueces: **30 días** desde la notificación de la resolución judicial"],
         ["No intercambiar **20** (Gobierno) y **30** (jueces)", "*Así en el BOE:* el art. 45 figura «(Derogado)», aunque el 46.1 a) sigue citándolo; el art. 46.2 dice «lo comunicara», sin tilde"]))}

{unidad("5.3 Tramitación (arts. 47 a 52)",
  lit("LOTC", "cuarenta y siete", ["intervendrá en todos los procesos de amparo"]),
  lit("LOTC", "cuarenta y ocho", []),
  lit("LOTC", "cuarenta y nueve", ["especial trascendencia constitucional del recurso", "en el plazo de 10 días"]),
  lit("LOTC", "cincuenta", ["por unanimidad de sus miembros", "recurridas en súplica por el Ministerio Fiscal en el plazo de tres días"]),
  lit("LOTC", "cincuenta y uno", ["no podrá exceder de diez días"]),
  lit("LOTC", "cincuenta y dos", ["no podrá exceder de veinte días", "en el plazo de 10 días"]),
  fichab("De la demanda a la sentencia",
         ["Conocen las **Salas** y, en su caso, las **Secciones** (48)", "El **Ministerio Fiscal** interviene **en todos** los procesos de amparo (47.2)"],
         ["Demanda (49): hechos, preceptos infringidos y amparo pedido; **siempre** justificar la **especial trascendencia constitucional**", "Admisión (50): la **Sección**, por **unanimidad**, mediante **providencia**; si hay mayoría sin unanimidad, decide la **Sala**", "Especial trascendencia: importancia para la interpretación, aplicación o eficacia de la Constitución y para el contenido de los derechos", "Sentencia (52): la Sala puede deferirla a una Sección si hay doctrina consolidada"],
         ["Subsanar defectos de la demanda: **10 días** (49.4)", "Súplica contra la inadmisión: **solo el Fiscal**, en **3 días** (50.3)", "Remisión de actuaciones: no más de **10 días**; comparecencia: **10 días** (51)", "Alegaciones: no más de **20 días**; sentencia: **10 días** (52)"],
         "Admisión: **Sección**, **unanimidad**, **providencia** (no auto ni mayoría). Súplica: **solo el Ministerio Fiscal**."))}

{unidad("5.4 La sentencia (arts. 53 a 55)",
  lit("LOTC", "cincuenta y tres", []),
  lit("LOTC", "cincuenta y cuatro", []),
  lit("LOTC", "cincuenta y cinco", ["se elevará la cuestión al Pleno"]),
  fichab("Qué puede decidir el TC",
         "La Sala o, en su caso, la Sección",
         ["Dos fallos: **otorgamiento** o **denegación** del amparo (53)", "Frente a los jueces, solo dice si hubo violación y cómo repararla; nada más sobre la actuación judicial (54)", "Si otorga: **nulidad** del acto, **reconocimiento** del derecho y **restablecimiento** del recurrente en su integridad (55.1)", "Si la lesión viene de **la ley aplicada**: eleva la cuestión al **Pleno**, con suspensión del plazo para sentenciar (55.2)"],
         "—",
         "La doctrina llama al 55.2 «autocuestión de inconstitucionalidad»; el término **no** es literal."))}

{unidad("5.5 Suspensión del acto impugnado (arts. 56 a 58)",
  lit("LOTC", "cincuenta y seis", ["no suspenderá los efectos", "en el plazo de cinco días"]),
  lit("LOTC", "cincuenta y siete", []),
  lit("LOTC", "cincuenta y ocho", ["dentro del plazo de un año"]),
  fichab("Si el amparo paraliza o no el acto recurrido",
         "La Sala o la Sección; los Jueces o Tribunales, para la indemnización",
         ["Regla: interponer el amparo **no suspende** (56.1)", "Excepción: se suspende si la ejecución haría perder al amparo su finalidad, salvo perturbación grave de un interés constitucional o de derechos de terceros; puede pedirse hasta la sentencia", "La suspensión o su denegación pueden **modificarse** por circunstancias sobrevenidas (57)"],
         ["Urgencia excepcional: suspensión en la propia admisión, impugnable en **5 días** (56.6)", "Indemnización por la suspensión o su denegación: **1 año** desde la publicación de la sentencia del TC (58)"],
         "La regla es que **no** suspende."))}
""", 2)

# ---------------------------------------------------------------------------
ap("s5-3", "II.6 Cuadro de síntesis de la protección", f"""
Con todo el bloque II visto, el art. 53 se resume así:

| Ubicación | Vinculación, reserva de ley y contenido esencial (53.1) | Ley orgánica (81) | Preferente y sumario (53.2) | Amparo ante el TC | Reforma de la CE |
|---|---|---|---|---|---|
| Art. 14 | Sí | No (STC 76/1983 [[TC]]) | Sí | Sí | Ordinaria (167) |
| Sección 1.ª (arts. 15-29) | Sí | Sí | Sí | Sí | Agravada (168) |
| Art. 30 (objeción de conciencia) | Sí | No (STC 160/1987 [[TC]]) | No | **Sí** | Ordinaria |
| Resto de la Sección 2.ª (arts. 30-38) | Sí | No (STC 76/1983 [[TC]]) | No | No | Ordinaria |
| Capítulo tercero (arts. 39-52) | No: «informarán» (53.3) | No | No | No | Ordinaria |

*Ley orgánica: el art. 81 no lo precisa; es doctrina del TC, no texto legal:* STC 76/1983 [[TC|https://hj.tribunalconstitucional.es/es-ES/Resolucion/Show/204]] (art. 14 y Sección 2.ª) y STC 160/1987 [[TC|https://hj.tribunalconstitucional.es/es-ES/Resolucion/Show/892]] (objeción de conciencia).

**Comunes a todo el Título I:** prohibición del **decreto-ley** (86.1); **recurso de inconstitucionalidad** contra las leyes; supervisión del **Defensor del Pueblo**, que defiende {c("CE", 54, "los derechos comprendidos en este Título")} (art. 54 → IV).

{resumen(["El **art. 53** reparte las garantías: 53.1 para todo el Capítulo segundo, 53.2 para el art. 14 y la Sección 1.ª (y el amparo, también para la objeción de conciencia), 53.3 para el Capítulo tercero.",
          "**Normativas** (frente al legislador): ley orgánica (81), prohibición del decreto-ley (86.1), recurso de inconstitucionalidad (161-162) y rigidez (167-169).",
          "**Jurisdiccionales**: procedimiento preferente y sumario (LJCA, 10 días), *habeas corpus* (LO 6/1984, 24 horas) y amparo constitucional (LOTC: 3 meses, 20 días o 30 días).",
          "El **Defensor del Pueblo** está legitimado en tres de ellas: inconstitucionalidad, amparo y *habeas corpus*."],
         "Siguiente: bloque III. Los derechos están protegidos, pero en situaciones extraordinarias algunos pueden **suspenderse**: cuáles, cuándo y con qué controles.")}
""", 2)
