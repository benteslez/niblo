# -*- coding: utf-8 -*-
"""Tema IV.11 (B4T11): Las Leyes del Procedimiento Administrativo Común de las
Administraciones Públicas y del Régimen Jurídico del Sector Público. Procedimiento
administrativo común y su alcance: iniciación, ordenación, instrucción y terminación.
La obligación de resolver. El silencio administrativo.
Método del I.2: mapa → bloques (I a VI) con guía; cada artículo, texto literal del
BOE + ficha de casillas fijas; cierre 1 (preguntas oficiales) y cierre 2 (repaso)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

T = Tema("B4T11",
  "Seis preguntas: I. Qué regulan las Leyes 39/2015 y 40/2015 y a quién se aplican (arts. 1 y 2 de cada una) · II. Cómo empieza el procedimiento: iniciación (arts. 54 a 64, 66, 68 y 69) · III. Cómo avanza: ordenación, términos y plazos (arts. 29 a 33 y 70 a 74) · IV. Cómo se averiguan los hechos: instrucción (arts. 75 a 80, 82 y 83) · V. Cómo acaba: terminación y tramitación simplificada (arts. 84 a 90 y 93 a 96) · VI. Qué pasa si la Administración no resuelve: obligación de resolver y silencio (arts. 21 a 25). Cada artículo: texto literal del BOE y ficha.",
  ["Ley 39/2015", "Ley 40/2015", "Ámbito subjetivo", "Iniciación", "Medidas provisionales", "Denuncia", "Subsanación", "Declaración responsable", "Términos y plazos", "Días hábiles", "Ordenación", "Instrucción", "Prueba", "Informes", "Audiencia", "Información pública", "Terminación", "Desistimiento", "Caducidad", "Tramitación simplificada", "Obligación de resolver", "Art. 21", "Silencio administrativo", "Art. 24"])

ESQ = "*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*"

# =============================================================================
T.ap("s0", "Mapa del tema: seis preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque IV, tema 11):
> Las Leyes del Procedimiento Administrativo Común de las Administraciones Públicas y del Régimen Jurídico del Sector Público. Procedimiento administrativo común y su alcance: iniciación, ordenación, instrucción y terminación. La obligación de resolver. El silencio administrativo.

### El hilo conductor

El epígrafe se lee como **seis preguntas encadenadas**. Casi todo está en la **Ley 39/2015** (Títulos II y IV). Cada pregunta es un bloque de los apuntes:

| Bloque | Pregunta | Ley 39/2015 | Otras normas |
|---|---|---|---|
| **I** | ¿Qué regulan las dos leyes y a quién se aplican? | Arts. 1 y 2 | Ley 40/2015, arts. 1 y 2 |
| **II** | ¿Cómo empieza el procedimiento? (iniciación) | Arts. 54 a 64, 66, 68 y 69 | — |
| **III** | ¿Cómo avanza? (ordenación, términos y plazos) | Arts. 29 a 33 y 70 a 74 | — |
| **IV** | ¿Cómo se averiguan los hechos? (instrucción) | Arts. 75 a 80, 82 y 83 | — |
| **V** | ¿Cómo acaba? (terminación y tramitación simplificada) | Arts. 84 a 90 y 93 a 96 | — |
| **VI** | ¿Qué pasa si la Administración no resuelve a tiempo? (obligación de resolver y silencio) | Arts. 21 a 25 | — |

!> **La idea que une los seis bloques:** la Ley 39/2015 regula **cómo** decide la Administración y la Ley 40/2015 **cómo se organiza** (I). El procedimiento **empieza** de oficio o a solicitud (II), **avanza** impulsado de oficio y con plazos que obligan a todos (III), **reúne** alegaciones, pruebas e informes y oye a los interesados (IV) y **acaba** normalmente con una resolución (V). Si la resolución no llega en plazo, la Administración **sigue obligada a resolver** y la ley da un sentido al silencio (VI).

### Fronteras con otros temas

- Requisitos, eficacia, notificación e invalidez del acto, y su ejecución: tema IV.4.
- Especialidades del procedimiento de responsabilidad patrimonial (arts. 61.4, 65, 67, 81, 82.5, 86.5, 91, 92 y 96.4): tema IV.10.
- Derechos de las personas, interesados, abstención y recusación, revisión de oficio y recursos: tema IV.12.

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué regulan las dos leyes y a quién se aplican? (Ley 39/2015 y Ley 40/2015, arts. 1 y 2)", donde(
  "Primera pregunta del tema. Antes de estudiar el procedimiento, hay que saber **qué regula cada ley** y **a qué entidades se aplica**: las dos leyes definen el sector público con la misma lista.",
  ["1 La Ley 39/2015: objeto y ámbito subjetivo (arts. 1 y 2)", "2 La Ley 40/2015: objeto y ámbito subjetivo (arts. 1 y 2)", "3 Cuadro comparativo de las dos leyes"]))

T.ap("s1", "I.1 La Ley 39/2015, del Procedimiento Administrativo Común: objeto y ámbito (arts. 1 y 2)", f"""
{unidad("1.1 Objeto de la Ley (art. 1)",
  lit("L39", "Artículo 1", ["los requisitos de validez y eficacia de los actos administrativos", "el procedimiento administrativo común a todas las Administraciones Públicas, incluyendo el sancionador y el de reclamación de responsabilidad de las Administraciones Públicas", "Solo mediante ley", "Reglamentariamente podrán establecerse especialidades del procedimiento"]),
  fichab("La ley del **procedimiento administrativo común** a todas las Administraciones Públicas",
         "Las Administraciones Públicas (→ I.1.2)",
         ["::Objeto (1.1):", "Requisitos de validez y eficacia de los actos administrativos (tema IV.4)", "Procedimiento administrativo común, incluido el **sancionador** y el de **reclamación de responsabilidad**", "Principios de la iniciativa legislativa y de la potestad reglamentaria"],
         f"Trámites adicionales o distintos: {c('L39', 'Artículo 1', 'Solo mediante ley, cuando resulte eficaz, proporcionado y necesario')}; por reglamento, solo especialidades",
         f"No hay procedimientos sancionador y de responsabilidad **separados**: están **dentro** del común. Por reglamento solo caben especialidades sobre {c('L39', 'Artículo 1', 'órganos competentes, plazos propios del concreto procedimiento por razón de la materia, formas de iniciación y terminación, publicación e informes a recabar')}."))}

{unidad("1.2 Ámbito subjetivo de aplicación (art. 2)",
  lit("L39", "Artículo 2", ["que quedarán sujetas a lo dispuesto en las normas de esta Ley que específicamente se refieran a las mismas, y en todo caso, cuando ejerzan potestades administrativas", "se regirán por su normativa específica y supletoriamente por las previsiones de esta Ley", "Tienen la consideración de Administraciones Públicas", "y supletoriamente por la presente Ley"]),
  fichab("A quién se aplica la ley: el **sector público**",
         ["::Sector público (2.1):", "Administración General del Estado", "Administraciones de las Comunidades Autónomas", "Entidades que integran la Administración Local", "Sector público institucional (2.2): organismos y entidades de derecho público; entidades de derecho privado vinculadas o dependientes; Universidades públicas"],
         ["Entidades de derecho privado: solo las normas que se refieran a ellas y, en todo caso, cuando ejerzan potestades administrativas", "Universidades públicas: su normativa específica y, supletoriamente, esta Ley", "Corporaciones de Derecho Público: su normativa específica en las funciones públicas atribuidas o delegadas y, supletoriamente, esta Ley (2.4)"],
         "—",
         "**Sector público** no es lo mismo que **Administraciones Públicas**: según el 2.3, son Administraciones Públicas las territoriales y los organismos y entidades de **derecho público** de la letra a); no las entidades de **derecho privado** ni las Universidades (letras b y c)."))}
""", 2)

T.ap("s2", "I.2 La Ley 40/2015, de Régimen Jurídico del Sector Público: objeto y ámbito (arts. 1 y 2)", f"""
{unidad("2.1 Objeto (art. 1)",
  lit("L40", "Artículo 1", ["las bases del régimen jurídico de las Administraciones Públicas", "los principios del sistema de responsabilidad de las Administraciones Públicas y de la potestad sancionadora", "la organización y funcionamiento de la Administración General del Estado y de su sector público institucional"], titulo="Artículo 1. Objeto (Ley 40/2015)"),
  fichab("La ley del **régimen jurídico** del sector público",
         "Las Administraciones Públicas (bases) y, en su organización, la Administración General del Estado y su sector público institucional",
         ["::Objeto:", "Bases del régimen jurídico de las Administraciones Públicas", "Principios de la responsabilidad patrimonial (tema IV.10) y de la potestad sancionadora", "Organización y funcionamiento de la AGE y de su sector público institucional"],
         "—",
         "La Ley 40/2015 regula los **principios** de la potestad sancionadora y de la responsabilidad; el **procedimiento** para ejercerlas está en la Ley 39/2015 (→ I.1.1). La organización que regula es la de la **AGE**, no la de las Comunidades Autónomas."))}

{unidad("2.2 Ámbito subjetivo (art. 2)",
  lit("L40", "Artículo 2", ["en particular a los principios previstos en el artículo 3", "Tienen la consideración de Administraciones Públicas"], titulo="Artículo 2. Ámbito Subjetivo (Ley 40/2015)"),
  fichab("A quién se aplica: el mismo **sector público** que en la Ley 39/2015",
         "AGE, Administraciones de las Comunidades Autónomas, Entidades de la Administración Local y sector público institucional",
         "Entidades de derecho privado vinculadas o dependientes: las normas que se refieran a ellas, en particular los principios del art. 3, y en todo caso cuando ejerzan potestades administrativas; Universidades públicas: normativa específica y supletoriamente esta Ley",
         "—",
         "La lista es **la misma** que la del art. 2 de la Ley 39/2015. Diferencias de texto: la Ley 40/2015 añade para las entidades de derecho privado los **principios del art. 3** y no tiene el apartado sobre las **Corporaciones de Derecho Público** (art. 2.4 Ley 39/2015)."))}
""", 2)

T.ap("s3", "I.3 Cuadro comparativo de las dos leyes (esquema)", f"""
{ESQ}

| | Ley 39/2015 (LPAC) | Ley 40/2015 (LRJSP) |
|---|---|---|
| Objeto (art. 1) | Validez y eficacia de los actos; **procedimiento administrativo común** (incluido sancionador y de responsabilidad); principios de la iniciativa legislativa y la potestad reglamentaria | **Bases del régimen jurídico** de las AA. PP.; principios de la responsabilidad y de la potestad sancionadora; **organización** y funcionamiento de la AGE y su sector público institucional |
| Sector público (art. 2.1) | AGE, CC. AA., Administración Local y sector público institucional | Igual |
| Entidades de derecho privado | Normas que se les refieran y, en todo caso, cuando ejerzan potestades administrativas | Igual, «en particular» los principios del art. 3 |
| Universidades públicas | Normativa específica y supletoriamente la Ley | Igual |
| Corporaciones de Derecho Público | Normativa específica y supletoriamente la Ley (2.4) | Sin apartado propio |
| Administraciones Públicas (art. 2.3) | Territoriales + organismos y entidades de derecho público | Igual |

{resumen([
  "La **Ley 39/2015** regula el **procedimiento administrativo común**, que incluye el **sancionador** y el de **responsabilidad**; los trámites adicionales o distintos, **solo mediante ley** (art. 1).",
  "La **Ley 40/2015** regula las **bases del régimen jurídico**, los principios de responsabilidad y sanción y la **organización de la AGE** (art. 1).",
  "Las dos se aplican al mismo **sector público** (art. 2); son **Administraciones Públicas** las territoriales y los organismos y entidades de **derecho público**."],
  "Siguiente: II. ¿Cómo empieza el procedimiento? La iniciación")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Cómo empieza el procedimiento? La iniciación (arts. 54 a 64, 66, 68 y 69)", donde(
  "Segunda pregunta. El procedimiento empieza **de oficio** (por decisión de la Administración) o **a solicitud del interesado**. Antes de empezar caben actuaciones previas y, si urge, medidas provisionales.",
  ["1 Clases de iniciación y actuaciones previas (arts. 54 y 55)", "2 Medidas provisionales y acumulación (arts. 56 y 57)", "3 Iniciación de oficio: propia iniciativa, orden superior, petición razonada y denuncia (arts. 58 a 62)", "4 Especialidades de los procedimientos sancionadores (arts. 63 y 64)", "5 Iniciación a solicitud del interesado: solicitud, subsanación, declaración responsable y comunicación (arts. 66, 68 y 69)"]))

T.ap("s4", "II.1 Clases de iniciación y actuaciones previas (arts. 54 y 55)", f"""
{unidad("1.1 Clases de iniciación (art. 54)",
  lit("L39", "Artículo 54", ["de oficio o a solicitud del interesado"]),
  fichab("Las dos formas de empezar un procedimiento",
         "La Administración (de oficio) o el interesado (a solicitud)",
         ["De oficio: arts. 58 a 65 (→ II.3)", "A solicitud del interesado: arts. 66 a 69 (→ II.5)"],
         "—",
         "Solo **dos** clases. La denuncia, la orden superior y la petición razonada **no** son clases distintas: son formas de iniciación **de oficio** (art. 58)."))}

{unidad("1.2 Información y actuaciones previas (art. 55)",
  lit("L39", "Artículo 55", ["Con anterioridad al inicio del procedimiento", "conocer las circunstancias del caso concreto y la conveniencia o no de iniciar el procedimiento", "funciones de investigación, averiguación e inspección"]),
  fichab("Período de información o actuaciones previas, antes de iniciar",
         f"{c('L39', 'Artículo 55', 'el órgano competente')}; en los sancionadores, los órganos con funciones de investigación, averiguación e inspección (o el que se determine)",
         ["Fin general: conocer las circunstancias y la conveniencia o no de iniciar", "En los sancionadores: hechos, posibles responsables y circunstancias relevantes"],
         "—",
         "Es **potestativo** («podrá abrir») y **anterior** al procedimiento: todavía no hay procedimiento iniciado."))}
""", 2)

T.ap("s5", "II.2 Medidas provisionales y acumulación (arts. 56 y 57)", f"""
{unidad("2.1 Medidas provisionales (art. 56)",
  lit("L39", "Artículo 56", ["el órgano administrativo competente para resolver", "proporcionalidad, efectividad y menor onerosidad", "en los casos de urgencia inaplazable", "dentro de los quince días siguientes a su adopción", "quedarán sin efecto si no se inicia el procedimiento en dicho plazo", "perjuicio de difícil o imposible reparación", "se extinguirán cuando surta efectos la resolución administrativa que ponga fin al procedimiento"]),
  fichab("Medidas para asegurar la eficacia de la resolución que pueda recaer",
         ["Iniciado el procedimiento: el órgano competente para **resolver** (56.1)", "Antes de iniciarlo: el órgano competente para **iniciar o instruir**, solo en urgencia inaplazable (56.2)"],
         ["De oficio o a instancia de parte, de forma motivada", "Principios de proporcionalidad, efectividad y menor onerosidad", "Lista del 56.3 (suspensión de actividades, fianzas, embargo preventivo, depósito…) y otras previstas en las leyes", "Prohibidas: las que causen perjuicio de difícil o imposible reparación o violen derechos amparados por las leyes (56.4)"],
         "Las anteriores a la iniciación se confirman, modifican o levantan en el acuerdo de iniciación, **dentro de los quince días** siguientes a su adopción; si no, quedan sin efecto",
         "Distingue **quién**: iniciado el procedimiento, el que **resuelve**; antes, el que **inicia o instruye**. Se extinguen cuando **surte efectos** la resolución que pone fin al procedimiento."))}

{unidad("2.2 Acumulación (art. 57)",
  lit("L39", "Artículo 57", ["identidad sustancial o íntima conexión", "siempre que sea el mismo órgano quien deba tramitar y resolver el procedimiento", "no procederá recurso alguno"]),
  fichab("Unir varios procedimientos en uno",
         "El órgano que inicie o tramite el procedimiento, de oficio o a instancia de parte",
         "Con procedimientos con los que guarde **identidad sustancial o íntima conexión**, si el mismo órgano tramita y resuelve",
         "—",
         "Contra el acuerdo de acumulación **no cabe recurso**. Requisito: **mismo órgano** para tramitar y resolver."))}
""", 2)

T.ap("s6", "II.3 Iniciación de oficio (arts. 58 a 62)", f"""
{unidad("3.1 Las cuatro vías de la iniciación de oficio y la propia iniciativa (arts. 58 y 59)",
  lit("L39", "Artículo 58", ["por acuerdo del órgano competente", "bien por propia iniciativa o como consecuencia de orden superior, a petición razonada de otros órganos o por denuncia"]),
  lit("L39", "Artículo 59", ["conocimiento directo o indirecto"]),
  fichab("Iniciación por decisión de la propia Administración",
         c("L39", "Artículo 58", "acuerdo del órgano competente"),
         ["Propia iniciativa (59)", "Orden superior (60)", "Petición razonada de otros órganos (61)", "Denuncia (62)"],
         "—",
         "Sea cual sea la vía, quien inicia es **siempre el órgano competente**, por **acuerdo**. La orden, la petición o la denuncia solo lo **mueven** a iniciar."))}

{unidad("3.2 Orden superior (art. 60)",
  lit("L39", "Artículo 60", ["superior jerárquico del competente para la iniciación"]),
  fichab("Iniciación ordenada por el superior jerárquico",
         c("L39", "Artículo 60", "un órgano administrativo superior jerárquico del competente para la iniciación del procedimiento"),
         "En los sancionadores la orden expresa, en lo posible, los presuntos responsables, los hechos y su tipificación, y el lugar y la fecha",
         "—",
         "La emite el **superior jerárquico**; la **petición razonada** (→ II.3.3) viene, en cambio, de un órgano **sin competencia** para iniciar."))}

{unidad("3.3 Petición razonada de otros órganos (art. 61)",
  lit("L39", "Artículo 61", ["cualquier órgano administrativo que no tiene competencia para iniciar el mismo", "La petición no vincula al órgano competente"], solo=[1, 2, 3]),
  fichab("Propuesta de iniciación de un órgano sin competencia para iniciar",
         "Cualquier órgano que conozca los hechos, ocasionalmente o por sus funciones de inspección, averiguación o investigación",
         "Propuesta al órgano competente; en los sancionadores, con el mismo contenido que la orden superior",
         "—",
         f"{c('L39', 'Artículo 61', 'La petición no vincula')}, pero si no se inicia hay que **comunicar los motivos** al órgano que la formuló. Su contenido en la responsabilidad patrimonial (61.4): tema IV.10."))}

{unidad("3.4 Denuncia (art. 62)",
  lit("L39", "Artículo 62", ["cualquier persona, en cumplimiento o no de una obligación legal", "deberá eximir al denunciante del pago de la multa", "deberá reducir el importe del pago de la multa", "no confiere, por sí sola, la condición de interesado"]),
  fichab("Puesta en conocimiento de unos hechos que pueden justificar la iniciación de oficio",
         c("L39", "Artículo 62", "cualquier persona, en cumplimiento o no de una obligación legal"),
         ["Identidad del denunciante y relato de los hechos; si pueden ser infracción, fecha y, si es posible, presuntos responsables (62.2)", "Si invoca un perjuicio al patrimonio público, la no iniciación se motiva y se notifica (62.3)", "Denunciante que participó en la infracción: **exención** si es el primero en aportar pruebas (con requisitos) o **reducción** si aporta valor añadido significativo; en ambos casos, cese en la infracción y sin destruir pruebas (62.4)"],
         "—",
         "La denuncia **no convierte en interesado** al denunciante (62.5). Ni es anónima: debe expresar la **identidad** de quien la presenta."))}
""", 2)

T.ap("s7", "II.4 Especialidades de los procedimientos sancionadores (arts. 63 y 64)", f"""
{unidad("4.1 Iniciación siempre de oficio y separación de fases (art. 63)",
  lit("L39", "Artículo 63", ["se iniciarán siempre de oficio", "la debida separación entre la fase instructora y la sancionadora, que se encomendará a órganos distintos", "En ningún caso se podrá imponer una sanción sin que se haya tramitado el oportuno procedimiento", "en tanto no haya recaído una primera resolución sancionadora, con carácter ejecutivo"]),
  fichab("Reglas propias del inicio del procedimiento sancionador",
         "El órgano competente según las normas reguladoras; instruye y resuelve **órganos distintos**",
         ["Siempre de oficio, por acuerdo", "Separación entre fase instructora y sancionadora", "Ninguna sanción sin procedimiento", "Infracción continuada: no se inician nuevos procedimientos hasta una primera resolución sancionadora ejecutiva"],
         "—",
         "**Siempre de oficio**: nunca a solicitud del interesado. La separación exige **órganos distintos** para instruir y para sancionar."))}

{unidad("4.2 Acuerdo de iniciación del sancionador (art. 64)",
  lit("L39", "Artículo 64", ["entendiendo en todo caso por tal al inculpado", "con expresa indicación del régimen de recusación de los mismos", "éste podrá ser considerado propuesta de resolución", "Pliego de cargos"]),
  fichab("Contenido mínimo del acuerdo de iniciación",
         "Se comunica al **instructor** y se notifica a los interesados (siempre al inculpado); al denunciante, si lo prevén las normas",
         ["Presuntos responsables", "Hechos, posible calificación y sanciones", "Instructor y, en su caso, Secretario, con su régimen de recusación", "Órgano competente para resolver y su norma, con la posibilidad de reconocer la responsabilidad (art. 85 → V.1.2)", "Medidas provisionales acordadas", "Derecho de alegaciones y audiencia y plazos"],
         "—",
         "Si el inculpado **no alega** y el acuerdo tiene un pronunciamiento preciso sobre la responsabilidad, puede valer como **propuesta de resolución**. Si al iniciar no hay elementos para calificar, se califica después en un **Pliego de cargos**."))}
""", 2)

T.ap("s8", "II.5 Iniciación a solicitud del interesado (arts. 66, 68 y 69)", f"""
La solicitud en la responsabilidad patrimonial y el plazo para reclamar (art. 67) son del tema IV.10.

{unidad("5.1 Contenido de la solicitud (art. 66)",
  lit("L39", "Artículo 66", ["Hechos, razones y petición en que se concrete, con toda claridad, la solicitud", "su correspondiente código de identificación", "podrán ser formuladas en una única solicitud", "éstos serán de uso obligatorio por los interesados"]),
  fichab("Qué debe contener la solicitud de iniciación",
         "El interesado (y, en su caso, su representante)",
         ["Nombre y apellidos del interesado y, en su caso, del representante", "Medio electrónico o lugar para notificar", "Hechos, razones y petición", "Lugar y fecha", "Firma o acreditación de la voluntad", "Órgano, centro o unidad y su código de identificación"],
         "—",
         "Varias personas con pretensiones de contenido y fundamento **idéntico o sustancialmente similar** pueden presentar **una única solicitud**. Los modelos de presentación masiva son de uso **voluntario**; los modelos **específicos** de un procedimiento, **obligatorios**."))}

{unidad("5.2 Subsanación y mejora de la solicitud (art. 68)",
  lit("L39", "Artículo 68", ["en un plazo de diez días", "se le tendrá por desistido de su petición", "procedimientos selectivos o de concurrencia competitiva", "hasta cinco días", "modificación o mejora voluntarias"]),
  fichab("Corrección de la solicitud que no reúne los requisitos",
         "Requiere el órgano; subsana el interesado",
         ["Requerimiento con advertencia: si no subsana, se le tiene por **desistido**, previa resolución (art. 21)", "Mejora voluntaria a petición del órgano, con acta sucinta (68.3)", "Obligados a relacionarse electrónicamente que presentan en papel: subsanación electrónica; vale como fecha la de la subsanación (68.4)"],
         "**Diez días**; ampliables **hasta cinco días** más, salvo en procedimientos **selectivos o de concurrencia competitiva**",
         "La consecuencia es el **desistimiento** (no la caducidad), y exige **resolución**. Ampliación: **cinco** días, nunca en selectivos ni de concurrencia competitiva."))}

{unidad("5.3 Declaración responsable y comunicación (art. 69)",
  lit("L39", "Artículo 69", ["manifiesta, bajo su responsabilidad, que cumple con los requisitos establecidos en la normativa vigente", "ponen en conocimiento de la Administración Pública competente sus datos identificativos", "desde el día de su presentación", "sin que sea posible la exigencia de ambas acumulativamente"]),
  fichab("Documentos que permiten ejercer un derecho o iniciar una actividad sin autorización previa",
         "El interesado los suscribe o presenta; la Administración conserva sus facultades de comprobación, control e inspección",
         ["Declaración responsable: manifiesta que cumple los requisitos, que tiene la documentación y que la mantendrá (69.1)", "Comunicación: pone en conocimiento datos identificativos u otros relevantes (69.2)", "Inexactitud, falsedad u omisión esencial: imposibilidad de continuar la actividad (69.4)"],
         "Efectos **desde el día de su presentación**; la comunicación puede ser posterior al inicio si la legislación lo prevé",
         "Se exige **una u otra**, **nunca las dos** acumulativamente (69.6). Estos procedimientos quedan **fuera** de la obligación de resolver (art. 21.1 → VI.1.1)."))}

{resumen([
  "Dos clases de iniciación: **de oficio** o **a solicitud** (54); antes, actuaciones previas potestativas (55).",
  "Medidas provisionales: las acuerda quien **resuelve**; antes de iniciar, solo por **urgencia inaplazable**, a confirmar en **15 días** (56). Acumulación sin recurso (57).",
  "De oficio, siempre por **acuerdo del órgano competente**: propia iniciativa, orden superior, petición razonada (no vincula) o denuncia (no da la condición de interesado) (58 a 62).",
  "Sancionadores: **siempre de oficio**, con **órganos distintos** para instruir y sancionar (63); el acuerdo de iniciación puede valer como propuesta (64).",
  "Solicitud: subsanación en **10 días** (+5) o **desistimiento** (68); declaración responsable o comunicación, eficaces **desde su presentación** (69)."],
  "Siguiente: III. ¿Cómo avanza el procedimiento? Ordenación, términos y plazos")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Cómo avanza el procedimiento? Ordenación, términos y plazos (arts. 29 a 33 y 70 a 74)", donde(
  "Tercera pregunta. Iniciado el procedimiento, hay que **ordenarlo**: se forma un expediente, se impulsa de oficio y cada trámite tiene un plazo. Las reglas de cómputo de los plazos están en los arts. 29 a 33; las de ordenación, en los arts. 70 a 74.",
  ["1 Términos y plazos: obligatoriedad, cómputo, registros, ampliación y urgencia (arts. 29 a 33)", "2 Ordenación: expediente, impulso, concentración, cumplimiento de trámites y cuestiones incidentales (arts. 70 a 74)"]))

T.ap("s9", "III.1 Términos y plazos (arts. 29 a 33)", f"""
{unidad("1.1 Obligatoriedad de términos y plazos (art. 29)",
  lit("L39", "Artículo 29", ["obligan a las autoridades y personal al servicio de las Administraciones Públicas", "así como a los interesados en los mismos"]),
  fichab("Los plazos obligan a todos",
         "Autoridades y personal de las Administraciones y **también los interesados**",
         "Los fijados en esta u otras leyes",
         "—",
         "Obligan **a ambas partes**: a la Administración y a los interesados."))}

{unidad("1.2 Cómputo de plazos (art. 30)",
  lit("L39", "Artículo 30", ["no podrán tener una duración superior a veinticuatro horas", "excluyéndose del cómputo los sábados, los domingos y los declarados festivos", "a partir del día siguiente", "El plazo concluirá el mismo día", "se entenderá que el plazo expira el último día del mes", "se entenderá prorrogado al primer día hábil siguiente", "se considerará inhábil en todo caso", "deberá publicarse antes del comienzo de cada año"]),
  fichab("Cómo se cuentan los plazos",
         "Reglas generales, salvo que una ley o el Derecho de la Unión Europea dispongan otro cómputo; calendario de inhábiles: AGE y CC. AA. (este incluye los de sus Entidades Locales)",
         ["Horas: hábiles; de hora en hora y de minuto en minuto; máximo **24 horas** (si no, en días)", "Días: **hábiles**; se excluyen **sábados, domingos y festivos**; si son naturales por ley o Derecho de la UE, se dice en la notificación", "Días: desde el **día siguiente** a la notificación o publicación (o al silencio)", "Meses o años: desde el día siguiente; terminan **el mismo día** del mes o año de vencimiento; si no lo hay, el **último día del mes**", "Último día inhábil: prórroga al **primer día hábil siguiente**", "Hábil en un sitio e inhábil en otro (residencia del interesado / sede del órgano): **inhábil** en todo caso"],
         "Calendario de inhábiles publicado **antes del comienzo de cada año**",
         "Los **sábados** son inhábiles. Los plazos por horas no pasan de **24 horas**. El día hábil o inhábil a efectos de plazos **no** decide por sí solo la apertura de las oficinas ni la jornada (30.8)."))}

{unidad("1.3 Cómputo de plazos en los registros (art. 31)",
  lit("L39", "Artículo 31", ["por la fecha y hora oficial de la sede electrónica de acceso", "todos los días del año durante las veinticuatro horas", "se entenderá realizada en la primera hora del primer día hábil siguiente", "Este será el único calendario de días inhábiles"]),
  fichab("Reglas del registro electrónico para contar plazos",
         "Cada Administración u Organismo, con su sede electrónica",
         ["Presentación **todos los días del año, 24 horas**", "Presentación en día inhábil: se entiende hecha en la **primera hora del primer día hábil siguiente** (salvo norma que permita recibir en inhábil)", "Plazos que debe cumplir la Administración: desde la fecha y hora de presentación en el registro"],
         "Rige la **fecha y hora oficial de la sede electrónica**",
         "El calendario de la sede es el **único** que se aplica en los registros electrónicos; **no** se aplica la regla del art. 30.6 (hábil en un sitio e inhábil en otro)."))}

{unidad("1.4 Ampliación de plazos (art. 32)",
  lit("L39", "Artículo 32", ["que no exceda de la mitad de los mismos", "misiones diplomáticas y oficinas consulares", "En ningún caso podrá ser objeto de ampliación un plazo ya vencido", "no serán susceptibles de recurso", "ciberincidente"]),
  fichab("Alargar un plazo de trámite",
         "La Administración, de oficio o a petición de los interesados, salvo precepto en contrario",
         ["Si las circunstancias lo aconsejan y no se perjudican derechos de tercero; el acuerdo se notifica", "Siempre por el máximo en procedimientos de misiones diplomáticas y oficinas consulares, trámites en el extranjero o interesados residentes fuera de España", "Incidencia técnica: ampliación de los plazos no vencidos, publicada en la sede (32.4)", "Ciberincidente grave: ampliación general de plazos (32.5)"],
         "Hasta **la mitad** del plazo; petición y decisión **antes del vencimiento**",
         "Nunca se amplía un plazo **ya vencido**. Contra el acuerdo de ampliación o su denegación **no cabe recurso** (sí contra la resolución final)."))}

{unidad("1.5 Tramitación de urgencia (art. 33)",
  lit("L39", "Artículo 33", ["Cuando razones de interés público lo aconsejen", "se reducirán a la mitad los plazos establecidos para el procedimiento ordinario, salvo los relativos a la presentación de solicitudes y recursos", "No cabrá recurso alguno"]),
  fichab("Procedimiento con plazos reducidos",
         "Se acuerda de oficio o a petición del interesado",
         "Por razones de **interés público**",
         "Plazos **a la mitad**, salvo los de **presentación de solicitudes y recursos**",
         "No se reducen los plazos de **solicitudes y recursos**. Contra el acuerdo de urgencia **no cabe recurso**. No confundir con la **tramitación simplificada** (art. 96 → V.5.1)."))}
""", 2)

T.ap("s10", "III.2 Ordenación del procedimiento (arts. 70 a 74)", f"""
{unidad("2.1 Expediente administrativo (art. 70)",
  lit("L39", "Artículo 70", ["el conjunto ordenado de documentos y actuaciones que sirven de antecedente y fundamento a la resolución administrativa", "Los expedientes tendrán formato electrónico", "completo, foliado, autentificado y acompañado de un índice", "No formará parte del expediente administrativo la información que tenga carácter auxiliar o de apoyo"]),
  fichab("El soporte del procedimiento",
         "El órgano que tramita",
         ["Formato **electrónico**; agregación ordenada de documentos, pruebas, dictámenes, informes, acuerdos y notificaciones, con índice numerado al remitirlo", "Debe constar copia electrónica certificada de la resolución", "Remisión: completo, foliado, autentificado y con índice autentificado"],
         "—",
         "**No** forman parte del expediente la información auxiliar, notas, borradores, opiniones, resúmenes, comunicaciones e informes internos ni los juicios de valor, **salvo** los informes preceptivos y facultativos solicitados antes de la resolución."))}

{unidad("2.2 Impulso (art. 71)",
  lit("L39", "Artículo 71", ["sometido al principio de celeridad", "se impulsará de oficio en todos sus trámites", "el orden riguroso de incoación en asuntos de homogénea naturaleza", "responsabilidad disciplinaria", "serán responsables directos de la tramitación del procedimiento"]),
  fichab("El procedimiento avanza por sí mismo",
         "De oficio; responden el órgano instructor o los titulares de las unidades",
         ["Principio de **celeridad**; impulso **de oficio** en todos los trámites y por medios electrónicos, con transparencia y publicidad", "Despacho por **orden riguroso de incoación** en asuntos homogéneos, salvo orden motivada del titular de la unidad"],
         "—",
         "El principio del art. 71 es la **celeridad** (cayó en 2025 → Cierre 1). Alterar el orden sin orden motivada da lugar a **responsabilidad disciplinaria** y, en su caso, **remoción** del puesto."))}

{unidad("2.3 Concentración de trámites (art. 72)",
  lit("L39", "Artículo 72", ["De acuerdo con el principio de simplificación administrativa", "se acordarán en un solo acto"]),
  fichab("Un solo acto para varios trámites",
         "El órgano que tramita",
         "Se acuerdan en un solo acto los trámites que admitan impulso simultáneo y no exijan cumplimiento sucesivo; al pedir trámites a otros órganos se indica el plazo legal",
         "—",
         "El principio de este artículo es la **simplificación administrativa** (no la celeridad, que es del art. 71)."))}

{unidad("2.4 Cumplimiento de trámites (art. 73)",
  lit("L39", "Artículo 73", ["en el plazo de diez días a partir del siguiente al de la notificación del correspondiente acto", "concediéndole un plazo de diez días para cumplimentarlo", "decaídos en su derecho al trámite correspondiente", "antes o dentro del día que se notifique la resolución"]),
  fichab("Plazo general de los trámites a cargo de los interesados",
         "Los interesados",
         ["Plazo general: **diez días** desde el siguiente a la notificación, salvo norma con plazo distinto", "Acto del interesado defectuoso: se le da un plazo de **diez días** para cumplimentarlo"],
         "**Diez días** (73.1 y 73.2)",
         "Si no cumplen, **pueden** ser declarados **decaídos** en su derecho al trámite; pero su actuación vale si se produce antes o **dentro del día** en que se notifique la resolución que da por transcurrido el plazo. Cayó en 2025 (→ Cierre 1)."))}

{unidad("2.5 Cuestiones incidentales (art. 74)",
  lit("L39", "Artículo 74", ["no suspenderán la tramitación del mismo, salvo la recusación"]),
  fichab("Incidentes durante el procedimiento",
         "—",
         "Se resuelven sin parar el procedimiento, incluso las que se refieran a la nulidad de actuaciones",
         "—",
         "La **única** que suspende es la **recusación** (y suspende también el plazo para resolver: art. 22.2 c → VI.2.1)."))}

{resumen([
  "Los plazos obligan a la Administración **y** a los interesados (29).",
  "Días **hábiles** (sin sábados, domingos ni festivos), desde el **día siguiente**; meses, de fecha a fecha; último día inhábil → **primer hábil siguiente** (30).",
  "Registro electrónico: **24 horas** todos los días; lo presentado en inhábil, a la **primera hora del primer hábil** (31).",
  "Ampliación: hasta **la mitad**, antes del vencimiento y sin recurso (32). Urgencia: plazos **a la mitad**, salvo solicitudes y recursos (33).",
  "Expediente **electrónico** (70); impulso de oficio y **celeridad** (71); concentración por **simplificación** (72); trámites de los interesados en **10 días** (73); solo la **recusación** suspende (74)."],
  "Siguiente: IV. ¿Cómo se averiguan los hechos? La instrucción")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Cómo se averiguan los hechos? La instrucción (arts. 75 a 80, 82 y 83)", donde(
  "Cuarta pregunta. La instrucción reúne lo necesario para decidir: alegaciones, pruebas e informes. Termina con la **audiencia** a los interesados y, si procede, la **información pública**.",
  ["1 Actos de instrucción y alegaciones (arts. 75 y 76)", "2 Prueba (arts. 77 y 78)", "3 Informes (arts. 79 y 80)", "4 Participación de los interesados: audiencia e información pública (arts. 82 y 83)"]))

T.ap("s11", "IV.1 Actos de instrucción y alegaciones (arts. 75 y 76)", f"""
{unidad("1.1 Actos de instrucción (art. 75)",
  lit("L39", "Artículo 75", ["se realizarán de oficio y a través de medios electrónicos, por el órgano que tramite el procedimiento", "compatible, en la medida de lo posible, con sus obligaciones laborales o profesionales", "principios de contradicción y de igualdad de los interesados"]),
  fichab("Actuaciones para determinar, conocer y comprobar los hechos",
         "El órgano que tramita, **de oficio**; los interesados pueden proponer actuaciones",
         ["Por medios electrónicos", "Si requieren a los interesados: en la forma más conveniente para ellos y compatible con sus obligaciones laborales o profesionales"],
         "—",
         "El instructor garantiza los principios de **contradicción** e **igualdad** de los interesados."))}

{unidad("1.2 Alegaciones (art. 76)",
  lit("L39", "Artículo 76", ["en cualquier momento del procedimiento anterior al trámite de audiencia", "En todo momento podrán los interesados alegar los defectos de tramitación"]),
  fichab("Aportaciones de los interesados durante la instrucción",
         "Los interesados",
         ["Alegaciones, documentos y otros elementos de juicio, que se tienen en cuenta en la propuesta de resolución", "Defectos de tramitación (paralización, infracción de plazos, omisión de trámites): en todo momento"],
         "Alegaciones: hasta el **trámite de audiencia**",
         "Alegar es posible **antes de la audiencia**; los **defectos de tramitación**, en **todo momento**, y pueden dar lugar a responsabilidad disciplinaria."))}
""", 2)

T.ap("s12", "IV.2 La prueba (arts. 77 y 78)", f"""
{unidad("2.1 Medios y período de prueba (art. 77)",
  lit("L39", "Artículo 77", ["cualquier medio de prueba admisible en Derecho", "por un plazo no superior a treinta días ni inferior a diez", "por un plazo no superior a diez días", "manifiestamente improcedentes o innecesarias, mediante resolución motivada", "vincularán a las Administraciones Públicas", "harán prueba de éstos salvo que se acredite lo contrario", "se entenderá que éste tiene carácter preceptivo"]),
  fichab("Cómo se acreditan los hechos",
         "El **instructor** abre el período de prueba y admite o rechaza las pruebas",
         ["Cualquier medio admisible en Derecho; valoración según la Ley de Enjuiciamiento Civil", "Se abre si la Administración no tiene por ciertos los hechos alegados o la naturaleza del procedimiento lo exige", "Discriminación alegada con indicios fundados: la justificación corresponde a quien se impute (77.3 bis)", "Sancionadores: vinculan los hechos probados por resoluciones judiciales penales firmes", "Documentos de funcionarios con condición de autoridad: prueba de los hechos salvo prueba en contrario", "Prueba consistente en un informe de un órgano administrativo: se entiende **preceptivo**"],
         "Período ordinario: **de 10 a 30 días**; extraordinario, a petición de los interesados: **hasta 10 días**",
         "Solo se rechazan pruebas **manifiestamente improcedentes o innecesarias**, por **resolución motivada**."))}

{unidad("2.2 Práctica de la prueba (art. 78)",
  lit("L39", "Artículo 78", ["con antelación suficiente", "puede nombrar técnicos para que le asistan", "podrá exigir el anticipo de los mismos"]),
  fichab("Cómo se practica la prueba admitida",
         "La Administración comunica; el interesado puede nombrar técnicos",
         ["Comunicación con antelación suficiente: lugar, fecha y hora", "Pruebas a petición del interesado con gastos que no deba soportar la Administración: anticipo, a reserva de liquidación"],
         "—",
         "El anticipo de gastos se exige por pruebas pedidas **por el interesado**."))}
""", 2)

T.ap("s13", "IV.3 Los informes (arts. 79 y 80)", f"""
El informe preceptivo del servicio y el dictamen del Consejo de Estado en la responsabilidad patrimonial (art. 81) son del tema IV.10.

{unidad("3.1 Petición de informes (art. 79)",
  lit("L39", "Artículo 79", ["los que se juzguen necesarios para resolver", "se concretará el extremo o extremos"]),
  fichab("Qué informes se piden",
         "El órgano que tramita",
         ["Los **preceptivos** por disposiciones legales y los que se juzguen **necesarios**", "Se cita el precepto que los exige o se fundamenta su conveniencia", "La petición concreta los extremos sobre los que se pide"],
         "—",
         "Hay que **citar el precepto** que lo exige o **fundamentar** la conveniencia de pedirlo."))}

{unidad("3.2 Emisión de informes (art. 80)",
  lit("L39", "Artículo 80", ["los informes serán facultativos y no vinculantes", "en el plazo de diez días", "se podrán proseguir las actuaciones salvo cuando se trate de un informe preceptivo", "El informe emitido fuera de plazo podrá no ser tenido en cuenta"]),
  fichab("Carácter, plazo y falta de emisión",
         "El órgano informante",
         ["Regla: **facultativos y no vinculantes**, salvo disposición expresa en contrario", "Por medios electrónicos", "Falta de emisión: se prosigue, salvo informe preceptivo (entonces cabe suspender el plazo para resolver: art. 22.1 d → VI.2.1)", "Informe de otra Administración por sus competencias no emitido a tiempo: se puede proseguir"],
         "**Diez días**, salvo otro plazo permitido o exigido",
         "Doble regla por defecto: **facultativos** y **no vinculantes**. El emitido fuera de plazo **podrá no** tenerse en cuenta."))}
""", 2)

T.ap("s14", "IV.4 Audiencia e información pública (arts. 82 y 83)", f"""
{unidad("4.1 Trámite de audiencia (art. 82)",
  lit("L39", "Artículo 82", ["inmediatamente antes de redactar la propuesta de resolución", "será anterior a la solicitud del informe del órgano competente para el asesoramiento jurídico", "en un plazo no inferior a diez días ni superior a quince", "se tendrá por realizado el trámite", "Se podrá prescindir del trámite de audiencia"], solo=[1, 2, 3, 4, 5]),
  fichab("Puesta de manifiesto del expediente a los interesados",
         "Los interesados o sus representantes (con los límites de la Ley 19/2013)",
         ["Instruido el procedimiento, **inmediatamente antes** de redactar la propuesta de resolución", "**Antes** de pedir el informe jurídico o el dictamen del Consejo de Estado u órgano consultivo autonómico", "Si renuncian a alegar antes del vencimiento, el trámite se tiene por realizado"],
         "Plazo para alegar: **no inferior a 10 días ni superior a 15**",
         "Se puede **prescindir** de la audiencia si no figuran ni se tienen en cuenta otros hechos, alegaciones o pruebas que los del interesado. La audiencia al contratista en la responsabilidad (82.5): tema IV.10."))}

{unidad("4.2 Información pública (art. 83)",
  lit("L39", "Artículo 83", ["cuando la naturaleza de éste lo requiera, podrá acordar un período de información pública", "se publicará un anuncio en el Diario oficial correspondiente", "en ningún caso podrá ser inferior a veinte días", "no otorga, por sí misma, la condición de interesado", "una respuesta razonada"]),
  fichab("Apertura del expediente a cualquier persona",
         "Lo acuerda el órgano al que corresponda la **resolución**; participa **cualquier persona** física o jurídica",
         ["Anuncio en el **Diario oficial** correspondiente; expediente disponible en la sede electrónica", "Quien alega tiene derecho a una **respuesta razonada** (puede ser común)", "No comparecer no impide recurrir la resolución"],
         "Alegaciones: **nunca menos de 20 días**",
         "Comparecer **no da**, por sí solo, la condición de **interesado** (igual que la denuncia, art. 62.5 → II.3.4). Es **potestativa** («podrá acordar»)."))}

{resumen([
  "La instrucción es **de oficio** y electrónica, con **contradicción e igualdad** (75); alegaciones **hasta la audiencia** (76).",
  "Prueba: período de **10 a 30 días** (extraordinario, hasta 10); solo se rechazan las **manifiestamente improcedentes o innecesarias** (77).",
  "Informes: por defecto **facultativos y no vinculantes**, en **10 días** (80).",
  "Audiencia: **inmediatamente antes** de la propuesta, plazo de **10 a 15 días** (82). Información pública: anuncio en diario oficial, **mínimo 20 días**, y no da la condición de interesado (83)."],
  "Siguiente: V. ¿Cómo acaba el procedimiento? La terminación")}
""", 2)

# =============================================================================
T.ap("bV", "V. ¿Cómo acaba el procedimiento? Terminación y tramitación simplificada (arts. 84 a 90 y 93 a 96)", donde(
  "Quinta pregunta. El procedimiento termina normalmente con la **resolución**, pero también por desistimiento, renuncia, caducidad, imposibilidad material o acuerdo. Si es sencillo, puede seguir la **tramitación simplificada**.",
  ["1 Formas de terminación; terminación de los sancionadores y terminación convencional (arts. 84 a 86)", "2 La resolución (arts. 87 a 90)", "3 Desistimiento y renuncia (arts. 93 y 94)", "4 Caducidad (art. 95)", "5 Tramitación simplificada (art. 96)"]))

T.ap("s15", "V.1 Formas de terminación (arts. 84 a 86)", f"""
{unidad("1.1 Terminación (art. 84)",
  lit("L39", "Artículo 84", ["la resolución, el desistimiento, la renuncia al derecho en que se funde la solicitud", "y la declaración de caducidad", "la imposibilidad material de continuarlo por causas sobrevenidas"]),
  fichab("Cómo puede acabar un procedimiento",
         "—",
         ["Resolución", "Desistimiento", "Renuncia al derecho, cuando no esté prohibida", "Declaración de caducidad", "Imposibilidad material de continuarlo por causas sobrevenidas (84.2), con resolución **motivada**"],
         "—",
         "La imposibilidad material **termina** el procedimiento (no lo suspende). La renuncia, **solo si no está prohibida**. Cayó en 2025 (→ Cierre 1)."))}

{unidad("1.2 Terminación en los procedimientos sancionadores (art. 85)",
  lit("L39", "Artículo 85", ["si el infractor reconoce su responsabilidad", "el pago voluntario por el presunto responsable, en cualquier momento anterior a la resolución", "reducciones de, al menos, el 20 % sobre el importe de la sanción propuesta", "condicionada al desistimiento o renuncia de cualquier acción o recurso en vía administrativa"]),
  fichab("Reconocimiento de responsabilidad y pago voluntario",
         "El presunto infractor; aplica las reducciones el órgano competente para resolver",
         ["Reconocimiento de la responsabilidad: se puede resolver imponiendo la sanción", "Pago voluntario antes de la resolución (sanción solo pecuniaria, o pecuniaria y otra no pecuniaria improcedente): termina el procedimiento, salvo reposición e indemnización"],
         "Reducciones de **al menos el 20 %**, acumulables, si la sanción es solo pecuniaria; el porcentaje puede incrementarse reglamentariamente",
         "Las reducciones deben figurar en la **notificación de iniciación** y exigen **desistir o renunciar** a recursos en **vía administrativa**."))}

{unidad("1.3 Terminación convencional (art. 86)",
  lit("L39", "Artículo 86", ["acuerdos, pactos, convenios o contratos", "ni versen sobre materias no susceptibles de transacción", "la consideración de finalizadores de los procedimientos administrativos", "la aprobación expresa del Consejo de Ministros", "no supondrán alteración de las competencias"], solo=[1, 2, 3, 4]),
  fichab("Terminación por acuerdo con los interesados",
         "Las Administraciones Públicas con personas de Derecho público o privado; el Consejo de Ministros u órgano autonómico equivalente aprueba los que versen sobre materias de su competencia directa",
         ["Límites: no contrarios al ordenamiento, no sobre materias no susceptibles de transacción, y para satisfacer el interés público", "Pueden **terminar** el procedimiento o insertarse en él con carácter previo, vinculante o no, a la resolución", "Contenido mínimo: partes, ámbito personal, funcional y territorial, y plazo de vigencia"],
         "—",
         "No alteran las **competencias** de los órganos ni las **responsabilidades** de autoridades y funcionarios. En estos casos no hay obligación de resolver (art. 21.1 → VI.1.1). El acuerdo en la responsabilidad patrimonial (86.5): tema IV.10."))}
""", 2)

T.ap("s16", "V.2 La resolución (arts. 87 a 90)", f"""
Las especialidades de la resolución en la responsabilidad patrimonial y la competencia para resolverla (arts. 91 y 92) son del tema IV.10.

{unidad("2.1 Actuaciones complementarias (art. 87)",
  lit("L39", "Artículo 87", ["mediante acuerdo motivado", "No tendrán la consideración de actuaciones complementarias los informes que preceden inmediatamente a la resolución final", "un plazo de siete días", "en un plazo no superior a quince días", "quedará suspendido"]),
  fichab("Actuaciones indispensables antes de resolver",
         "El órgano competente para **resolver**, por acuerdo motivado notificado a los interesados",
         "Solo las **indispensables** para resolver; no lo son los informes que preceden inmediatamente a la resolución final",
         "Práctica: **no más de 15 días**; alegaciones tras ellas: **7 días**; el plazo para resolver queda **suspendido** (art. 22.2 b → VI.2.1)",
         "**Siete** días para alegar, **quince** para practicarlas. La suspensión del plazo para resolver es **obligatoria**."))}

{unidad("2.2 Contenido de la resolución (art. 88)",
  lit("L39", "Artículo 88", ["decidirá todas las cuestiones planteadas por los interesados y aquellas otras derivadas del mismo", "por un plazo no superior a quince días", "sin que en ningún caso pueda agravar su situación inicial", "Expresarán, además, los recursos que contra la misma procedan", "En ningún caso podrá la Administración abstenerse de resolver so pretexto de silencio, oscuridad o insuficiencia de los preceptos legales", "La aceptación de informes o dictámenes servirá de motivación", "será necesario que el instructor eleve al órgano competente para resolver una propuesta de resolución"]),
  fichab("Qué debe decidir y expresar la resolución",
         "El órgano competente para resolver; si no instruye él, con **propuesta** del instructor",
         ["Todas las cuestiones planteadas y las derivadas; las conexas no planteadas, oyendo antes a los interesados (máximo 15 días)", "A solicitud del interesado: **congruente** con lo pedido, sin **agravar** su situación inicial", "Decisión motivada en los casos del art. 35 (tema IV.4); recursos, órgano y plazo", "Se dicta **electrónicamente**", "Cabe **inadmitir** solicitudes de derechos no previstos o manifiestamente carentes de fundamento"],
         "Cuestiones conexas: **no más de 15 días** para alegar",
         "Nunca cabe abstenerse de resolver por **silencio, oscuridad o insuficiencia** de los preceptos. En los procedimientos a solicitud del interesado, la resolución **no puede agravar** su situación inicial."))}

{unidad("2.3 Propuesta de resolución en los sancionadores (art. 89)",
  lit("L39", "Artículo 89", ["sin que sea necesaria la formulación de la propuesta de resolución", "que ha prescrito la infracción", "formulará una propuesta de resolución que deberá ser notificada a los interesados"]),
  fichab("Archivo o propuesta al terminar la instrucción del sancionador",
         "El **órgano instructor**",
         ["Archivo sin propuesta si: no existen los hechos; no resultan acreditados; no son, de modo manifiesto, infracción; no hay responsable identificado o está exento; o ha prescrito la infracción", "Si no, propuesta motivada con hechos probados, calificación, infracción, responsables, sanción propuesta, valoración de pruebas y medidas provisionales"],
         "La propuesta se notifica con plazo para alegar",
         "La propuesta del sancionador **se notifica** a los interesados (art. 88.7)."))}

{unidad("2.4 Resolución en los sancionadores (art. 90)",
  lit("L39", "Artículo 90", ["no se podrán aceptar hechos distintos de los determinados en el curso del procedimiento", "en el plazo de quince días", "será ejecutiva cuando no quepa contra ella ningún recurso ordinario en vía administrativa"], solo=[1, 2, 3]),
  fichab("Contenido y ejecutividad de la resolución sancionadora",
         "El órgano competente para resolver",
         ["Valoración de las pruebas, hechos, responsables, infracciones y sanciones, o declaración de inexistencia", "No caben hechos distintos de los determinados en el procedimiento", "Si el órgano ve mayor gravedad que la propuesta: se notifica al inculpado para alegar"],
         "Alegaciones por mayor gravedad: **15 días**",
         "La resolución sancionadora es **ejecutiva** cuando **no cabe recurso ordinario en vía administrativa**; mientras, caben disposiciones cautelares."))}
""", 2)

T.ap("s17", "V.3 Desistimiento y renuncia (arts. 93 y 94)", f"""
{unidad("3.1 Desistimiento por la Administración (art. 93)",
  lit("L39", "Artículo 93", ["En los procedimientos iniciados de oficio", "motivadamente"]),
  fichab("La Administración abandona un procedimiento que ella inició",
         "La Administración",
         "Motivadamente, en los supuestos y con los requisitos previstos en las Leyes",
         "—",
         "Solo en procedimientos **iniciados de oficio** y solo cuando **las Leyes** lo prevean."))}

{unidad("3.2 Desistimiento y renuncia por los interesados (art. 94)",
  lit("L39", "Artículo 94", ["desistir de su solicitud", "renunciar a sus derechos", "sólo afectará a aquellos que la hubiesen formulado", "aceptará de plano", "en el plazo de diez días desde que fueron notificados", "podrá limitar los efectos del desistimiento o la renuncia al interesado y seguirá el procedimiento"]),
  fichab("El interesado abandona su solicitud (desistimiento) o su derecho (renuncia)",
         "Todo interesado; si son varios, solo afecta a quienes la formulen",
         ["Desistir de la solicitud; renunciar a los derechos si no está prohibido", "Por cualquier medio que permita su constancia, con las firmas que correspondan", "La Administración la **acepta de plano** y declara concluso el procedimiento"],
         "Terceros interesados personados pueden instar la continuación en **10 días** desde que se les notifica",
         "Si hay **interés general** o conviene esclarecer la cuestión, la Administración puede limitar los efectos al interesado y **seguir**. El desistimiento en nombre de otro exige **acreditar la representación** (art. 5.3; cayó en 2025 → Cierre 1)."))}
""", 2)

T.ap("s18", "V.4 La caducidad (art. 95)", f"""
{unidad("4.1 Requisitos y efectos de la caducidad (art. 95)",
  lit("L39", "Artículo 95", ["por causa imputable al mismo", "transcurridos tres meses, se producirá la caducidad del procedimiento", "No podrá acordarse la caducidad por la simple inactividad del interesado", "no producirá por sí sola la prescripción", "los procedimientos caducados no interrumpirán el plazo de prescripción", "alegaciones, proposición de prueba y audiencia al interesado", "Podrá no ser aplicable la caducidad"]),
  fichab("Fin del procedimiento a solicitud del interesado paralizado por su culpa",
         "La Administración advierte y acuerda el archivo; el interesado puede recurrir",
         ["Paralización por causa **imputable al interesado** → advertencia → archivo notificado", "No cabe por simple inactividad en trámites no indispensables (solo pierde el trámite)", "Nuevo procedimiento si no hay prescripción: se pueden incorporar actos y trámites, pero se repiten alegaciones, prueba y audiencia"],
         "**Tres meses** desde la advertencia",
         "La caducidad **no** produce por sí sola la **prescripción**, pero el procedimiento caducado **no interrumpe** la prescripción. Puede no aplicarse si hay **interés general**. La caducidad de los iniciados de oficio está en el art. 25 (→ VI.4.1)."))}
""", 2)

T.ap("s19", "V.5 Tramitación simplificada (art. 96)", f"""
{unidad("5.1 Tramitación simplificada del procedimiento administrativo común (art. 96)",
  lit("L39", "Artículo 96", ["razones de interés público o la falta de complejidad del procedimiento", "Si alguno de ellos manifestara su oposición expresa, la Administración deberá seguir la tramitación ordinaria", "en el plazo de cinco días desde su presentación", "se entenderá desestimada la solicitud", "calificar la infracción como leve", "deberán ser resueltos en treinta días", "durante el plazo de cinco días", "únicamente cuando la resolución vaya a ser desfavorable para el interesado", "suspensión automática del plazo para resolver", "en el plazo de quince días", "deberá ser tramitado de manera ordinaria"], solo=[1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]),
  fichab("Procedimiento abreviado con trámites tasados",
         "Las Administraciones, de oficio o a solicitud del interesado; el órgano de tramitación puede volver a la ordinaria en cualquier momento anterior a la resolución",
         ["Causa: interés público o falta de complejidad", "De oficio: se notifica; la **oposición expresa** de un interesado obliga a la ordinaria (salvo en sancionadores por infracción **leve**)", "Trámites: inicio; subsanación; alegaciones en **5 días**; audiencia solo si la resolución va a ser **desfavorable**; informes jurídico y del CGPJ y dictamen consultivo, si son preceptivos; resolución", "Dictamen contrario al fondo de la propuesta: se sigue la tramitación ordinaria", "Trámite no previsto: tramitación ordinaria"],
         "Resolución en **30 días** desde el siguiente a la notificación del acuerdo; solicitud del interesado: desestimación en **5 días**, sin recurso (silencio desestimatorio); dictamen en **15 días** si se pide",
         "**Treinta** días para resolver; **cinco** para alegar. En los sancionadores por infracción **leve**, el interesado **no puede oponerse**. La simplificada en la responsabilidad patrimonial (96.4): tema IV.10."))}

{resumen([
  "Ponen fin al procedimiento: **resolución, desistimiento, renuncia y caducidad**, y la **imposibilidad material** sobrevenida (84).",
  "Sancionadores: reconocimiento o **pago voluntario**, con reducciones de **al menos el 20 %** (85). Terminación **convencional**, con límites (86).",
  "Resolución: todas las cuestiones, **congruente** y sin **agravar** al solicitante; nunca abstenerse de resolver (88).",
  "Desistimiento de la Administración solo **de oficio** y si las Leyes lo prevén (93); el del interesado se acepta **de plano** (94).",
  "Caducidad a solicitud del interesado: paralización imputable y **tres meses** tras la advertencia (95). Simplificada: **30 días** (96)."],
  "Siguiente: VI. ¿Qué pasa si la Administración no resuelve a tiempo? Obligación de resolver y silencio")}
""", 2)

# =============================================================================
T.ap("bVI", "VI. ¿Qué pasa si la Administración no resuelve a tiempo? Obligación de resolver y silencio (arts. 21 a 25)", donde(
  "Sexta pregunta. La Administración está **obligada a resolver** en un plazo máximo. Si no lo hace, la ley da un **sentido al silencio**: estimatorio o desestimatorio en los procedimientos a solicitud del interesado; desestimación o caducidad en los de oficio.",
  ["1 La obligación de resolver y el plazo máximo (art. 21)", "2 Suspensión y ampliación del plazo máximo (arts. 22 y 23)", "3 El silencio en los procedimientos iniciados a solicitud del interesado (art. 24)", "4 La falta de resolución en los procedimientos iniciados de oficio (art. 25)", "5 Cuadro del silencio administrativo"]))

T.ap("s20", "VI.1 La obligación de resolver y el plazo máximo (art. 21)", f"""
{unidad("1.1 Obligación de resolver (art. 21)",
  lit("L39", "Artículo 21", ["está obligada a dictar resolución expresa y a notificarla en todos los procedimientos cualquiera que sea su forma de iniciación", "los supuestos de terminación del procedimiento por pacto o convenio", "Este plazo no podrá exceder de seis meses salvo que una norma con rango de Ley establezca uno mayor", "éste será de tres meses", "desde la fecha del acuerdo de iniciación", "desde la fecha en que la solicitud haya tenido entrada en el registro electrónico", "dentro de los diez días siguientes a la recepción de la solicitud", "responsabilidad disciplinaria"]),
  fichab("Deber de dictar y notificar resolución expresa",
         "La Administración; responden el personal que despacha los asuntos y los titulares de los órganos que instruyen y resuelven",
         ["En **todos** los procedimientos, de oficio o a solicitud", "Prescripción, renuncia, caducidad, desistimiento o desaparición del objeto: la resolución declara la circunstancia", "Excepciones: terminación por **pacto o convenio** y derechos sometidos solo a **declaración responsable o comunicación**", "Información al interesado del plazo y del efecto del silencio: en el acuerdo de iniciación o en una comunicación en 10 días desde la entrada de la solicitud", "Muchas solicitudes: se pueden habilitar medios personales y materiales (21.5)"],
         ["::Plazo máximo para notificar:", "El de la norma del procedimiento; **no más de seis meses** salvo norma con rango de ley o Derecho de la UE", "Si la norma no lo fija: **tres meses**", "Cómputo: de oficio, desde el **acuerdo de iniciación**; a solicitud, desde la **entrada en el registro electrónico** del órgano competente"],
         "El plazo es para **notificar** (no solo para dictar). Seis meses es el **techo** que solo supera una **ley** o el Derecho de la UE; tres meses, el plazo **supletorio**. El incumplimiento genera **responsabilidad disciplinaria**."))}
""", 2)

T.ap("s21", "VI.2 Suspensión y ampliación del plazo máximo (arts. 22 y 23)", f"""
{unidad("2.1 Suspensión del plazo máximo para resolver (art. 22)",
  lit("L39", "Artículo 22", ["se podrá suspender en los siguientes casos", "Este plazo de suspensión no podrá exceder en ningún caso de tres meses", "se suspenderá en los siguientes casos", "Cuando los interesados promuevan la recusación"]),
  fichab("Paradas del reloj del plazo máximo",
         "El órgano que tramita; las peticiones y respuestas se comunican a los interesados",
         ["::Potestativa («se podrá suspender», 22.1):", "Requerimiento de subsanación o aportación de documentos", "Pronunciamiento previo y preceptivo de un órgano de la UE", "Procedimiento no finalizado en la UE que condicione la resolución", "Informes preceptivos (máximo tres meses)", "Pruebas técnicas o análisis contradictorios o dirimentes propuestos por los interesados", "Negociaciones para un pacto o convenio (art. 86)", "Pronunciamiento previo indispensable de un órgano jurisdiccional", "**Obligatoria** («se suspenderá», 22.2): requerimiento a otra Administración para anular o revisar un acto base (art. 39.5); actuaciones complementarias (art. 87); recusación"],
         "Informes preceptivos: la suspensión **no puede exceder de tres meses**; si no llega el informe, se prosigue",
         "Distingue las **potestativas** (22.1) de las **obligatorias** (22.2: requerimiento entre Administraciones, actuaciones complementarias y **recusación**)."))}

{unidad("2.2 Ampliación del plazo máximo para resolver y notificar (art. 23)",
  lit("L39", "Artículo 23", ["Excepcionalmente", "no pudiendo ser éste superior al establecido para la tramitación del procedimiento", "no cabrá recurso alguno"]),
  fichab("Alargar el plazo máximo para resolver",
         "El órgano competente para resolver (a propuesta, en su caso, del instructor) o su superior jerárquico",
         "**Excepcionalmente**, de forma motivada y agotados los medios personales y materiales del art. 21.5; el acuerdo se notifica",
         "La ampliación **no puede superar** el plazo establecido para el procedimiento",
         "Contra el acuerdo que resuelve sobre la ampliación **no cabe recurso alguno**. No confundir con la ampliación de plazos de **trámite** del art. 32 (→ III.1.4), que es hasta la **mitad**."))}
""", 2)

T.ap("s22", "VI.3 El silencio en los procedimientos iniciados a solicitud del interesado (art. 24)", f"""
{unidad("3.1 Regla y excepciones (art. 24.1)",
  lit("L39", "Artículo 24", ["legitima al interesado o interesados para entenderla estimada por silencio administrativo", "una norma con rango de ley o una norma de Derecho de la Unión Europea o de Derecho internacional aplicable en España", "razones imperiosas de interés general", "derecho de petición, a que se refiere el artículo 29 de la Constitución", "facultades relativas al dominio público o al servicio público", "impliquen el ejercicio de actividades que puedan dañar el medio ambiente", "responsabilidad patrimonial de las Administraciones Públicas", "procedimientos de impugnación de actos y disposiciones", "revisión de oficio iniciados a solicitud de los interesados", "se entenderá estimado el mismo"], solo=[1, 2, 3]),
  fichab("Sentido del silencio cuando el procedimiento lo inició el interesado",
         "El interesado o interesados, al vencer el plazo máximo sin resolución expresa notificada",
         ["::Regla: **estimatorio**, salvo norma con rango de ley, Derecho de la UE o internacional. En acceso a actividades, el silencio negativo exige **razones imperiosas de interés general**. **Desestimatorio** en:", "Derecho de **petición** (art. 29 CE)", "Transferencia de facultades sobre el **dominio público** o el **servicio público**", "Actividades que puedan **dañar el medio ambiente**", "**Responsabilidad patrimonial** (tema IV.10)", "**Impugnación** de actos y disposiciones y **revisión de oficio** a solicitud del interesado"],
         "—",
         "Excepción a la excepción: la **alzada** contra una desestimación **por silencio** se entiende **estimada** si no se resuelve en plazo, salvo en las materias del párrafo anterior. Cayó en 2025: medio ambiente (→ Cierre 1)."))}

{unidad("3.2 Efectos del silencio y resolución tardía (art. 24.2 a 4)",
  lit("L39", "Artículo 24", ["tiene a todos los efectos la consideración de acto administrativo finalizador del procedimiento", "tiene los solos efectos de permitir a los interesados la interposición del recurso", "sólo podrá dictarse de ser confirmatoria del mismo", "sin vinculación alguna al sentido del silencio", "producen efectos desde el vencimiento del plazo máximo", "en el plazo de quince días desde que expire el plazo máximo"], solo=[4, 5, 6, 7, 8]),
  fichab("Qué vale el silencio y qué puede hacer después la Administración",
         "Cualquiera puede verse afectado: los actos por silencio se hacen valer ante la Administración y ante **cualquier persona** física o jurídica, pública o privada",
         ["Estimación: **acto administrativo finalizador** del procedimiento", "Desestimación: solo permite **recurrir** (administrativa o contencioso-administrativamente)", "Resolución tardía tras estimación: solo **confirmatoria**", "Resolución tardía tras desestimación: **sin vinculación** al sentido del silencio", "Prueba: cualquier medio, incluido el **certificado** de silencio"],
         "Efectos desde el **vencimiento** del plazo máximo; certificado **de oficio** en **15 días** desde que expira el plazo (o a petición, en cualquier momento)",
         "La estimación por silencio es un **acto** (tema IV.4); la desestimación solo sirve para **recurrir**. Tras el silencio positivo, la Administración ya **no puede denegar** por resolución tardía."))}
""", 2)

T.ap("s23", "VI.4 La falta de resolución en los procedimientos iniciados de oficio (art. 25)", f"""
{unidad("4.1 Desestimación o caducidad (art. 25)",
  lit("L39", "Artículo 25", ["no exime a la Administración del cumplimiento de la obligación legal de resolver", "podrán entender desestimadas sus pretensiones por silencio administrativo", "se producirá la caducidad", "ordenará el archivo de las actuaciones", "se interrumpirá el cómputo del plazo para resolver"]),
  fichab("Efectos del vencimiento del plazo en los procedimientos de oficio",
         "Los interesados que hubieren **comparecido** (procedimientos favorables); la Administración (procedimientos de gravamen)",
         ["Procedimientos de los que puedan derivarse derechos o situaciones **favorables**: **desestimación** por silencio", "Potestades **sancionadoras** o de intervención con efectos **desfavorables o de gravamen**: **caducidad** y archivo (efectos del art. 95 → V.4.1)"],
         "Paralización imputable al interesado: se **interrumpe** el cómputo del plazo",
         "En los de oficio **no hay silencio positivo**. El vencimiento **no exime** de resolver. Favorables → desestimación; gravamen → **caducidad**."))}
""", 2)

T.ap("s24", "VI.5 Cuadro del silencio administrativo (esquema)", f"""
{ESQ}

| Procedimiento | Al vencer el plazo sin resolución notificada | Artículo |
|---|---|---|
| A solicitud del interesado (regla) | **Estimación** por silencio | 24.1 |
| A solicitud: petición (art. 29 CE), dominio o servicio público, medio ambiente, responsabilidad patrimonial | **Desestimación** | 24.1 |
| A solicitud: impugnación de actos y disposiciones, revisión de oficio | **Desestimación** | 24.1 |
| Alzada contra una desestimación por silencio | **Estimación** (salvo las materias anteriores) | 24.1 |
| De oficio, favorable al interesado | **Desestimación** (interesados comparecidos) | 25.1 a) |
| De oficio, sancionador o de gravamen | **Caducidad** | 25.1 b) |
| Solicitud de tramitación simplificada | Desestimación en 5 días | 96.3 |

{resumen([
  "La Administración debe **dictar y notificar** resolución expresa siempre, salvo pacto o convenio y declaración responsable o comunicación (21.1).",
  "Plazo máximo: el de su norma, **hasta seis meses** salvo ley o Derecho de la UE; si no hay, **tres meses** (21.2 y 3).",
  "Suspensión potestativa (22.1) u obligatoria (22.2); ampliación excepcional, sin recurso (23).",
  "A solicitud: silencio **estimatorio** como regla, con excepciones tasadas (24.1); la estimación es **acto**, la desestimación solo abre el **recurso** (24.2).",
  "De oficio: **desestimación** si es favorable; **caducidad** si es de gravamen (25)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_L57 = examen("L", 57, {
  "a": f"El art. 73.1 no dice cinco días: {c('L39', 'Artículo 73', 'en el plazo de diez días a partir del siguiente al de la notificación del correspondiente acto')}. Cinco días son, por ejemplo, las alegaciones de la tramitación simplificada (art. 96.6 c).",
  "b": f"Cambia el plazo: tres días no aparece en el art. 73; el plazo general es {c('L39', 'Artículo 73', 'de diez días')}.",
  "c": f"Literal del art. 73.1: {c('L39', 'Artículo 73', 'deberán realizarse en el plazo de diez días a partir del siguiente al de la notificación del correspondiente acto, salvo en el caso de que en la norma correspondiente se fije plazo distinto')}.",
  "d": f"Cambia el plazo: veinte días es el mínimo de la información pública ({c('L39', 'Artículo 83', 'en ningún caso podrá ser inferior a veinte días')}, art. 83.2), no el de los trámites del art. 73."},
  [("diez días", "L39", "Artículo 73", "Los trámites que deban ser cumplimentados por los interesados deberán realizarse en el plazo de diez días a partir del siguiente al de la notificación del correspondiente acto")])
EX_L58 = examen("L", 58, {
  "a": f"Cambia la materia: el art. 24.1 dice {c('L39', 'Artículo 24', 'en los procedimientos de responsabilidad patrimonial de las Administraciones Públicas')}, no «sancionadora». Además, los sancionadores {c('L39', 'Artículo 63', 'se iniciarán siempre de oficio')} (art. 63.1): no son a solicitud del interesado.",
  "b": f"Cambia el derecho: el silencio es desestimatorio en el derecho {c('L39', 'Artículo 24', 'de petición, a que se refiere el artículo 29 de la Constitución')}, no en el de asociación del art. 22.",
  "c": f"Literal del art. 24.1: el silencio tendrá efecto desestimatorio en los procedimientos que {c('L39', 'Artículo 24', 'impliquen el ejercicio de actividades que puedan dañar el medio ambiente')}.",
  "d": f"Cambia el dominio: la ley habla de {c('L39', 'Artículo 24', 'facultades relativas al dominio público o al servicio público')}, no al dominio privado."},
  [("dañar el medio ambiente", "L39", "Artículo 24", "impliquen el ejercicio de actividades que puedan dañar el medio ambiente")])
EX_P72 = examen("P", 72, {
  "a": f"Aportar documentación no está en la lista del art. 5.3, que exige acreditar la representación {c('L39', 'Artículo 5', 'Para formular solicitudes, presentar declaraciones responsables o comunicaciones, interponer recursos, desistir de acciones y renunciar a derechos en nombre de otra persona')}.",
  "b": f"Al revés: {c('L39', 'Artículo 5', 'Para los actos y gestiones de mero trámite se presumirá aquella representación')}.",
  "c": f"Literal del art. 5.3: para {c('L39', 'Artículo 5', 'desistir de acciones y renunciar a derechos en nombre de otra persona, deberá acreditarse la representación')}.",
  "d": "Subsanar defectos formales no figura entre los actos del art. 5.3 que exigen acreditar la representación."},
  [("desistir de acciones", "L39", "Artículo 5", "desistir de acciones y renunciar a derechos en nombre de otra persona, deberá acreditarse la representación")])
EX_P73 = examen("P", 73, {
  "a": f"El art. 84.1 no exige que la resolución sea firme, y la Administración solo puede desistir {c('L39', 'Artículo 93', 'En los procedimientos iniciados de oficio')} y {c('L39', 'Artículo 93', 'en los supuestos y con los requisitos previstos en las Leyes')} (art. 93).",
  "b": f"Literal del art. 84.1: {c('L39', 'Artículo 84', 'Pondrán fin al procedimiento la resolución, el desistimiento')}, la renuncia {c('L39', 'Artículo 84', 'y la declaración de caducidad')}.",
  "c": f"Cambia el efecto: la imposibilidad material no suspende, termina: {c('L39', 'Artículo 84', 'También producirá la terminación del procedimiento la imposibilidad material de continuarlo por causas sobrevenidas')} (art. 84.2).",
  "d": f"Cambia la condición: la renuncia pone fin al procedimiento {c('L39', 'Artículo 84', 'cuando tal renuncia no esté prohibida por el ordenamiento jurídico')}, y la Administración {c('L39', 'Artículo 94', 'aceptará de plano el desistimiento o la renuncia')} (art. 94.4): no hace falta conformidad expresa."},
  [("la resolución, el desistimiento", "L39", "Artículo 84", "Pondrán fin al procedimiento la resolución, el desistimiento"),
   ("declaración de caducidad", "L39", "Artículo 84", "y la declaración de caducidad")])
EX_X62 = examen("X", 62, {
  "a": f"La simplificación administrativa es el principio del art. 72 (concentración de trámites): {c('L39', 'Artículo 72', 'De acuerdo con el principio de simplificación administrativa')}; no el del art. 71.",
  "b": f"Literal del art. 71.1: {c('L39', 'Artículo 71', 'El procedimiento, sometido al principio de celeridad, se impulsará de oficio en todos sus trámites')}.",
  "c": f"La proporcionalidad aparece en las medidas provisionales ({c('L39', 'Artículo 56', 'de acuerdo con los principios de proporcionalidad, efectividad y menor onerosidad')}, art. 56.1), no en el art. 71.",
  "d": "La eficiencia no figura en el art. 71, que nombra la celeridad y, para el impulso, la transparencia y la publicidad."},
  [("celeridad", "L39", "Artículo 71", "El procedimiento, sometido al principio de celeridad")])

T.ap("s25", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **cinco** preguntas de este tema: plazo de los trámites (art. 73), silencio (art. 24), representación (art. 5), terminación (art. 84) e impulso (art. 71). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-L 2025, pregunta 57 · Cumplimiento de trámites (→ III.2.4)", EX_L57,
  "### GACE-L 2025, pregunta 58 · Silencio desestimatorio (→ VI.3.1)", EX_L58,
  "### GACE-P 2025, pregunta 72 · Representación para desistir (art. 5; tema IV.12, y → V.3.2)",
  "La representación es materia del tema IV.12 (interesados). Texto del art. 5.3 que resuelve la pregunta:",
  lit("L39", "Artículo 5", ["desistir de acciones y renunciar a derechos en nombre de otra persona, deberá acreditarse la representación", "Para los actos y gestiones de mero trámite se presumirá aquella representación"], solo=[3]),
  EX_P72,
  "### GACE-P 2025, pregunta 73 · Terminación (→ V.1.1)", EX_P73,
  "### GACE-L 2025 extraordinario, pregunta 62 · Impulso y celeridad (→ III.2.2)", EX_X62,
  "### Cómo se pregunta",
  "!> Las preguntas de este tema citan el **artículo** y cambian **un dato**: el plazo (diez días frente a tres, cinco o veinte), la materia (patrimonial frente a sancionadora; petición frente a asociación; dominio público frente a privado) o el principio (celeridad del art. 71 frente a simplificación del art. 72). Saber **qué dice cada artículo** y **qué está en el de al lado** resuelve la pregunta.",
]))

T.ap("s26", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Las dos leyes | Ley 39: procedimiento común (incluidos sancionador y responsabilidad); Ley 40: bases del régimen jurídico y organización de la AGE; mismo sector público | Trámites adicionales **solo mediante ley** (1.2); Administraciones Públicas = territoriales + entidades de **derecho público** (2.3) |
| II. Iniciación | De oficio (acuerdo del órgano competente: propia iniciativa, orden superior, petición razonada, denuncia) o a solicitud | Medidas previas: confirmar en **15 días**; subsanación en **10 días** (+5) o **desistimiento**; sancionador **siempre de oficio** |
| III. Ordenación y plazos | Días hábiles sin sábados; expediente electrónico; impulso de oficio | Trámites en **10 días** (73); **celeridad** (71); ampliación hasta **la mitad** (32); urgencia a **la mitad** salvo solicitudes y recursos (33) |
| IV. Instrucción | Alegaciones, prueba, informes, audiencia, información pública | Prueba **10-30 días**; informes **facultativos y no vinculantes** en **10 días**; audiencia **10-15 días**; información pública **mínimo 20 días** |
| V. Terminación | Resolución, desistimiento, renuncia, caducidad, imposibilidad material; convencional; simplificada | Reducción **≥ 20 %** (85); caducidad a los **3 meses** (95); simplificada en **30 días** (96) |
| VI. Resolver y silencio | Obligación de resolver y notificar; plazos; silencio | Máximo **6 meses** (salvo ley o UE); supletorio **3 meses**; silencio positivo como regla a solicitud; de oficio: desestimación o **caducidad** |

?> **Trampas frecuentes:** «sábados hábiles» (son **inhábiles**, art. 30.2); «la imposibilidad material **suspende** el procedimiento» (lo **termina**, 84.2); «silencio desestimatorio en la responsabilidad **sancionadora**» (es la **patrimonial**, 24.1); «el principio del art. 71 es la **simplificación**» (es la **celeridad**; la simplificación es del 72); «la denuncia da la condición de interesado» (no, 62.5); «el plazo máximo nunca supera seis meses» (sí, si lo fija una **ley** o el Derecho de la UE, 21.2); «la caducidad interrumpe la prescripción» (los procedimientos caducados **no** la interrumpen, 95.3).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
L = "L39"
for k, art, cat, enun, ops, expl, frag in [
 (L, "Artículo 1", "Las dos leyes", "Según el artículo 1.1 de la Ley 39/2015, el procedimiento administrativo común que regula incluye:",
  ["El sancionador y el de reclamación de responsabilidad de las Administraciones Públicas.", "Solo el sancionador; el de responsabilidad se regula en la Ley 40/2015.", "El de elaboración de los Presupuestos Generales del Estado.", "El recurso contencioso-administrativo."],
  "Art. 1.1 Ley 39/2015: «incluyendo el sancionador y el de reclamación de responsabilidad de las Administraciones Públicas».", "incluyendo el sancionador y el de reclamación de responsabilidad de las Administraciones Públicas"),
 (L, "Artículo 1", "Las dos leyes", "Según el artículo 1.2 de la Ley 39/2015, podrán incluirse trámites adicionales o distintos a los contemplados en esta Ley:",
  ["Solo mediante ley, cuando resulte eficaz, proporcionado y necesario, y de manera motivada.", "Mediante real decreto acordado en Consejo de Ministros.", "Mediante orden del Ministro competente por razón de la materia.", "Por acuerdo motivado del órgano instructor."],
  "Art. 1.2 Ley 39/2015: «Solo mediante ley…».", "Solo mediante ley, cuando resulte eficaz, proporcionado y necesario para la consecución de los fines propios del procedimiento, y de manera motivada"),
 (L, "Artículo 2", "Las dos leyes", "Según el artículo 2.3 de la Ley 39/2015, tienen la consideración de Administraciones Públicas, además de las territoriales:",
  ["Los organismos públicos y entidades de derecho público vinculados o dependientes de las Administraciones Públicas.", "Las entidades de derecho privado vinculadas o dependientes de las Administraciones Públicas.", "Todas las entidades del sector público institucional, sin excepción.", "Las Corporaciones de Derecho Público."],
  "Art. 2.3: son Administraciones Públicas las territoriales y los organismos públicos y entidades de derecho público de la letra a) del apartado 2.", "así como los organismos públicos y entidades de derecho público previstos en la letra a) del apartado 2 anterior"),
 (L, "Artículo 2", "Las dos leyes", "Según el artículo 2.2 c) de la Ley 39/2015, las Universidades públicas:",
  ["Se regirán por su normativa específica y supletoriamente por las previsiones de esta Ley.", "Se regirán exclusivamente por esta Ley.", "Quedan excluidas del ámbito de aplicación de esta Ley.", "Se regirán por esta Ley y supletoriamente por su normativa específica."],
  "Art. 2.2 c) Ley 39/2015.", "Las Universidades públicas, que se regirán por su normativa específica y supletoriamente por las previsiones de esta Ley"),
 (L, "Artículo 54", "Iniciación", "Según el artículo 54 de la Ley 39/2015, los procedimientos podrán iniciarse:",
  ["De oficio o a solicitud del interesado.", "Solo de oficio.", "Solo a solicitud del interesado.", "De oficio, previa autorización del superior jerárquico."],
  "Art. 54 Ley 39/2015.", "Los procedimientos podrán iniciarse de oficio o a solicitud del interesado"),
 (L, "Artículo 56", "Iniciación", "Según el artículo 56.2 de la Ley 39/2015, las medidas provisionales adoptadas antes de la iniciación del procedimiento deberán ser confirmadas, modificadas o levantadas en el acuerdo de iniciación, que deberá efectuarse:",
  ["Dentro de los quince días siguientes a su adopción.", "Dentro de los diez días siguientes a su adopción.", "Dentro del mes siguiente a su adopción.", "Dentro de los tres días siguientes a su adopción."],
  "Art. 56.2: «dentro de los quince días siguientes a su adopción».", "dentro de los quince días siguientes a su adopción"),
 (L, "Artículo 56", "Iniciación", "Según el artículo 56.1 de la Ley 39/2015, las medidas provisionales se adoptarán de acuerdo con los principios de:",
  ["Proporcionalidad, efectividad y menor onerosidad.", "Celeridad, eficacia y economía.", "Jerarquía, descentralización y coordinación.", "Publicidad, transparencia y eficiencia."],
  "Art. 56.1 Ley 39/2015.", "de acuerdo con los principios de proporcionalidad, efectividad y menor onerosidad"),
 (L, "Artículo 58", "Iniciación", "Según el artículo 58 de la Ley 39/2015, NO es una de las formas de iniciación de oficio:",
  ["La solicitud del interesado.", "La orden superior.", "La petición razonada de otros órganos.", "La denuncia."],
  "Art. 58: de oficio, por propia iniciativa, orden superior, petición razonada de otros órganos o denuncia. La solicitud del interesado es la otra clase de iniciación (art. 54).", "bien por propia iniciativa o como consecuencia de orden superior, a petición razonada de otros órganos o por denuncia"),
 (L, "Artículo 61", "Iniciación", "Según el artículo 61.2 de la Ley 39/2015, la petición razonada de otros órganos:",
  ["No vincula al órgano competente para iniciar el procedimiento, que debe comunicar los motivos por los que, en su caso, no procede la iniciación.", "Vincula al órgano competente para iniciar el procedimiento.", "Vincula al órgano competente si procede de un órgano con funciones de inspección.", "No vincula y no exige comunicar nada al órgano que la formuló."],
  "Art. 61.2 Ley 39/2015.", "La petición no vincula al órgano competente para iniciar el procedimiento, si bien deberá comunicar al órgano que la hubiera formulado los motivos"),
 (L, "Artículo 63", "Iniciación", "Según el artículo 63.1 de la Ley 39/2015, los procedimientos de naturaleza sancionadora:",
  ["Se iniciarán siempre de oficio por acuerdo del órgano competente.", "Podrán iniciarse a solicitud de la persona perjudicada.", "Se iniciarán de oficio o a solicitud del interesado.", "Se instruirán y resolverán por el mismo órgano."],
  "Art. 63.1: siempre de oficio y con separación entre fase instructora y sancionadora, encomendadas a órganos distintos.", "se iniciarán siempre de oficio por acuerdo del órgano competente"),
 (L, "Artículo 68", "Iniciación", "Según el artículo 68.1 de la Ley 39/2015, si la solicitud de iniciación no reúne los requisitos exigidos, se requerirá al interesado para que la subsane en un plazo de:",
  ["Diez días, con indicación de que, si no lo hiciera, se le tendrá por desistido de su petición.", "Quince días, con indicación de que, si no lo hiciera, se producirá la caducidad.", "Cinco días, con indicación de que, si no lo hiciera, se le tendrá por desistido de su petición.", "Diez días, con indicación de que, si no lo hiciera, se entenderá desestimada la solicitud."],
  "Art. 68.1: diez días; si no subsana, se le tiene por desistido, previa resolución.", "en un plazo de diez días, subsane la falta o acompañe los documentos preceptivos, con indicación de que, si así no lo hiciera, se le tendrá por desistido de su petición"),
 (L, "Artículo 68", "Iniciación", "Según el artículo 68.2 de la Ley 39/2015, el plazo de subsanación de la solicitud podrá ampliarse prudencialmente:",
  ["Hasta cinco días, siempre que no se trate de procedimientos selectivos o de concurrencia competitiva.", "Hasta diez días, siempre que no se trate de procedimientos selectivos o de concurrencia competitiva.", "Hasta cinco días, solo en los procedimientos selectivos o de concurrencia competitiva.", "Hasta la mitad del plazo, en cualquier procedimiento."],
  "Art. 68.2 Ley 39/2015.", "Siempre que no se trate de procedimientos selectivos o de concurrencia competitiva, este plazo podrá ser ampliado prudencialmente, hasta cinco días"),
 (L, "Artículo 69", "Iniciación", "Según el artículo 69.3 de la Ley 39/2015, las declaraciones responsables y las comunicaciones permitirán el reconocimiento o ejercicio de un derecho o el inicio de una actividad:",
  ["Desde el día de su presentación.", "Desde que la Administración las compruebe.", "Transcurridos diez días desde su presentación.", "Desde que se notifique su admisión."],
  "Art. 69.3: «desde el día de su presentación», sin perjuicio de las facultades de comprobación.", "desde el día de su presentación"),
 (L, "Artículo 69", "Iniciación", "Según el artículo 69.6 de la Ley 39/2015, para iniciar una misma actividad u obtener el reconocimiento de un mismo derecho:",
  ["Únicamente será exigible una declaración responsable o una comunicación, sin que sea posible exigir ambas acumulativamente.", "Podrán exigirse acumulativamente una declaración responsable y una comunicación.", "Será exigible en todo caso una declaración responsable y, además, una autorización.", "Será exigible siempre una comunicación previa y una posterior."],
  "Art. 69.6 Ley 39/2015.", "sin que sea posible la exigencia de ambas acumulativamente"),
 (L, "Artículo 30", "Términos y plazos", "Según el artículo 30.2 de la Ley 39/2015, cuando los plazos se señalen por días, se entiende que estos son hábiles, excluyéndose del cómputo:",
  ["Los sábados, los domingos y los declarados festivos.", "Los domingos y los declarados festivos.", "Solo los declarados festivos.", "Los sábados y los domingos, pero no los festivos locales."],
  "Art. 30.2: se excluyen los sábados, los domingos y los declarados festivos.", "excluyéndose del cómputo los sábados, los domingos y los declarados festivos"),
 (L, "Artículo 30", "Términos y plazos", "Según el artículo 30.1 de la Ley 39/2015, los plazos expresados por horas no podrán tener una duración superior a:",
  ["Veinticuatro horas, en cuyo caso se expresarán en días.", "Cuarenta y ocho horas.", "Setenta y dos horas.", "Doce horas."],
  "Art. 30.1 Ley 39/2015.", "no podrán tener una duración superior a veinticuatro horas, en cuyo caso se expresarán en días"),
 (L, "Artículo 30", "Términos y plazos", "Según el artículo 30.4 de la Ley 39/2015, en los plazos fijados en meses, si en el mes de vencimiento no hubiera día equivalente a aquel en que comienza el cómputo:",
  ["Se entenderá que el plazo expira el último día del mes.", "Se entenderá que el plazo expira el primer día del mes siguiente.", "El plazo se prorrogará al primer día hábil del mes siguiente.", "El plazo se computará por días naturales."],
  "Art. 30.4 Ley 39/2015.", "se entenderá que el plazo expira el último día del mes"),
 (L, "Artículo 31", "Términos y plazos", "Según el artículo 31.2 b) de la Ley 39/2015, a efectos del cumplimiento de plazos por los interesados fijados en días hábiles, la presentación en el registro electrónico en un día inhábil se entenderá realizada:",
  ["En la primera hora del primer día hábil siguiente, salvo que una norma permita expresamente la recepción en día inhábil.", "En la última hora del día hábil anterior.", "En el mismo día inhábil, a todos los efectos.", "En la primera hora del segundo día hábil siguiente."],
  "Art. 31.2 b) Ley 39/2015.", "la presentación en un día inhábil se entenderá realizada en la primera hora del primer día hábil siguiente salvo que una norma permita expresamente la recepción en día inhábil"),
 (L, "Artículo 32", "Términos y plazos", "Según el artículo 32.1 de la Ley 39/2015, la Administración podrá conceder una ampliación de los plazos establecidos que no exceda:",
  ["De la mitad de los mismos.", "De la tercera parte de los mismos.", "Del doble de los mismos.", "De diez días."],
  "Art. 32.1: «que no exceda de la mitad de los mismos».", "una ampliación de los plazos establecidos, que no exceda de la mitad de los mismos"),
 (L, "Artículo 33", "Términos y plazos", "Según el artículo 33.1 de la Ley 39/2015, la tramitación de urgencia reduce a la mitad los plazos establecidos para el procedimiento ordinario, salvo:",
  ["Los relativos a la presentación de solicitudes y recursos.", "Los relativos a la emisión de informes.", "Los del trámite de audiencia.", "Los del período de prueba."],
  "Art. 33.1 Ley 39/2015.", "salvo los relativos a la presentación de solicitudes y recursos"),
 (L, "Artículo 70", "Ordenación", "Según el artículo 70.4 de la Ley 39/2015, NO formarán parte del expediente administrativo:",
  ["Las notas, borradores y opiniones.", "Los dictámenes.", "Las notificaciones.", "Los informes preceptivos solicitados antes de la resolución que ponga fin al procedimiento."],
  "Art. 70.4: queda fuera la información auxiliar o de apoyo (notas, borradores, opiniones…), salvo los informes preceptivos y facultativos solicitados antes de la resolución. Dictámenes y notificaciones forman el expediente (70.2).", "notas, borradores, opiniones"),
 (L, "Artículo 71", "Ordenación", "Según el artículo 71.2 de la Ley 39/2015, en el despacho de los expedientes se guardará:",
  ["El orden riguroso de incoación en asuntos de homogénea naturaleza, salvo orden motivada en contrario del titular de la unidad administrativa.", "El orden que fije discrecionalmente el instructor.", "El orden de entrada en el registro general del Ministerio, sin excepciones.", "El orden de antigüedad de los interesados."],
  "Art. 71.2 Ley 39/2015.", "se guardará el orden riguroso de incoación en asuntos de homogénea naturaleza, salvo que por el titular de la unidad administrativa se dé orden motivada en contrario"),
 (L, "Artículo 74", "Ordenación", "Según el artículo 74 de la Ley 39/2015, las cuestiones incidentales que se susciten en el procedimiento:",
  ["No suspenderán la tramitación del mismo, salvo la recusación.", "Suspenderán siempre la tramitación del mismo.", "Suspenderán la tramitación cuando se refieran a la nulidad de actuaciones.", "No suspenderán la tramitación del mismo, salvo la abstención."],
  "Art. 74: no suspenden, incluso las que se refieran a la nulidad de actuaciones, salvo la recusación.", "no suspenderán la tramitación del mismo, salvo la recusación"),
 (L, "Artículo 76", "Instrucción", "Según el artículo 76.1 de la Ley 39/2015, los interesados podrán aducir alegaciones y aportar documentos u otros elementos de juicio:",
  ["En cualquier momento del procedimiento anterior al trámite de audiencia.", "Solo en el plazo de diez días desde el acuerdo de iniciación.", "En cualquier momento, incluso después de dictada la resolución.", "Solo durante el período de prueba."],
  "Art. 76.1 Ley 39/2015.", "en cualquier momento del procedimiento anterior al trámite de audiencia"),
 (L, "Artículo 77", "Instrucción", "Según el artículo 77.2 de la Ley 39/2015, el período de prueba se abrirá por un plazo:",
  ["No superior a treinta días ni inferior a diez.", "No superior a quince días ni inferior a cinco.", "No superior a veinte días ni inferior a diez.", "No superior a dos meses ni inferior a quince días."],
  "Art. 77.2 Ley 39/2015; el período extraordinario, no superior a diez días.", "por un plazo no superior a treinta días ni inferior a diez"),
 (L, "Artículo 77", "Instrucción", "Según el artículo 77.3 de la Ley 39/2015, el instructor del procedimiento solo podrá rechazar las pruebas propuestas por los interesados:",
  ["Cuando sean manifiestamente improcedentes o innecesarias, mediante resolución motivada.", "Cuando lo estime conveniente, sin necesidad de motivación.", "Cuando sean improcedentes, previo informe del servicio jurídico.", "En ningún caso."],
  "Art. 77.3 Ley 39/2015.", "sólo podrá rechazar las pruebas propuestas por los interesados cuando sean manifiestamente improcedentes o innecesarias, mediante resolución motivada"),
 (L, "Artículo 80", "Instrucción", "Según el artículo 80 de la Ley 39/2015, salvo disposición expresa en contrario, los informes serán:",
  ["Facultativos y no vinculantes, y se emitirán en el plazo de diez días.", "Preceptivos y no vinculantes, y se emitirán en el plazo de diez días.", "Facultativos y vinculantes, y se emitirán en el plazo de quince días.", "Preceptivos y vinculantes, y se emitirán en el plazo de un mes."],
  "Art. 80.1 y 2 Ley 39/2015.", ["los informes serán facultativos y no vinculantes", "en el plazo de diez días"]),
 (L, "Artículo 82", "Instrucción", "Según el artículo 82.2 de la Ley 39/2015, en el trámite de audiencia los interesados podrán alegar y presentar los documentos y justificaciones que estimen pertinentes en un plazo:",
  ["No inferior a diez días ni superior a quince.", "No inferior a cinco días ni superior a diez.", "No inferior a quince días ni superior a treinta.", "De veinte días."],
  "Art. 82.2 Ley 39/2015.", "en un plazo no inferior a diez días ni superior a quince"),
 (L, "Artículo 83", "Instrucción", "Según el artículo 83 de la Ley 39/2015, el plazo para formular alegaciones en el período de información pública:",
  ["En ningún caso podrá ser inferior a veinte días.", "En ningún caso podrá ser inferior a diez días.", "No podrá ser superior a quince días.", "Será de un mes en todo caso."],
  "Art. 83.2 Ley 39/2015.", "en ningún caso podrá ser inferior a veinte días"),
 (L, "Artículo 85", "Terminación", "Según el artículo 85.3 de la Ley 39/2015, cuando la sanción tenga únicamente carácter pecuniario, en caso de reconocimiento de responsabilidad o pago voluntario se aplicarán reducciones de:",
  ["Al menos, el 20 % sobre el importe de la sanción propuesta, acumulables entre sí.", "Al menos, el 50 % sobre el importe de la sanción propuesta, no acumulables.", "Como máximo, el 20 % sobre el importe de la sanción propuesta.", "Al menos, el 10 % sobre el importe de la sanción propuesta, no acumulables."],
  "Art. 85.3 Ley 39/2015.", "reducciones de, al menos, el 20 % sobre el importe de la sanción propuesta, siendo éstos acumulables entre sí"),
 (L, "Artículo 87", "Terminación", "Según el artículo 87 de la Ley 39/2015, las actuaciones complementarias deberán practicarse en un plazo:",
  ["No superior a quince días, concediéndose a los interesados siete días para alegar tras su finalización.", "No superior a diez días, concediéndose a los interesados quince días para alegar.", "No superior a un mes, sin trámite de alegaciones.", "No superior a quince días, concediéndose a los interesados diez días para alegar."],
  "Art. 87: siete días para alegaciones; práctica en no más de quince días; el plazo para resolver queda suspendido.", ["un plazo de siete días", "deberán practicarse en un plazo no superior a quince días"]),
 (L, "Artículo 88", "Terminación", "Según el artículo 88.2 de la Ley 39/2015, en los procedimientos tramitados a solicitud del interesado, la resolución:",
  ["Será congruente con las peticiones formuladas por éste, sin que en ningún caso pueda agravar su situación inicial.", "Podrá agravar su situación inicial si así lo exige el interés público.", "Podrá pronunciarse sobre cuestiones no planteadas sin oír al interesado.", "Será congruente con la propuesta del instructor, aunque agrave la situación inicial del interesado."],
  "Art. 88.2 Ley 39/2015.", "la resolución será congruente con las peticiones formuladas por éste, sin que en ningún caso pueda agravar su situación inicial"),
 (L, "Artículo 94", "Terminación", "Según el artículo 94.4 de la Ley 39/2015, la Administración aceptará de plano el desistimiento o la renuncia y declarará concluso el procedimiento, salvo que terceros interesados personados insten su continuación en el plazo de:",
  ["Diez días desde que fueron notificados del desistimiento o renuncia.", "Quince días desde que fueron notificados del desistimiento o renuncia.", "Cinco días desde la presentación del desistimiento.", "Un mes desde que fueron notificados del desistimiento o renuncia."],
  "Art. 94.4 Ley 39/2015.", "en el plazo de diez días desde que fueron notificados del desistimiento o renuncia"),
 (L, "Artículo 95", "Terminación", "Según el artículo 95.1 de la Ley 39/2015, en los procedimientos iniciados a solicitud del interesado paralizados por causa imputable al mismo, la Administración le advertirá que se producirá la caducidad transcurridos:",
  ["Tres meses.", "Seis meses.", "Un mes.", "Diez días."],
  "Art. 95.1 Ley 39/2015.", "transcurridos tres meses, se producirá la caducidad del procedimiento"),
 (L, "Artículo 95", "Terminación", "Según el artículo 95.3 de la Ley 39/2015, la caducidad:",
  ["No producirá por sí sola la prescripción de las acciones, pero los procedimientos caducados no interrumpirán el plazo de prescripción.", "Producirá por sí sola la prescripción de las acciones del particular.", "Interrumpirá el plazo de prescripción de las acciones.", "Impedirá en todo caso iniciar un nuevo procedimiento con el mismo objeto."],
  "Art. 95.3 Ley 39/2015.", "La caducidad no producirá por sí sola la prescripción de las acciones del particular o de la Administración, pero los procedimientos caducados no interrumpirán el plazo de prescripción"),
 (L, "Artículo 96", "Terminación", "Según el artículo 96.6 de la Ley 39/2015, salvo que reste menos para su tramitación ordinaria, los procedimientos tramitados de manera simplificada deberán ser resueltos en:",
  ["Treinta días, a contar desde el siguiente al que se notifique al interesado el acuerdo de tramitación simplificada.", "Tres meses, a contar desde el acuerdo de iniciación.", "Quince días, a contar desde la presentación de la solicitud.", "Treinta días, a contar desde la presentación de la solicitud."],
  "Art. 96.6 Ley 39/2015.", "deberán ser resueltos en treinta días, a contar desde el siguiente al que se notifique al interesado el acuerdo de tramitación simplificada del procedimiento"),
 (L, "Artículo 21", "Obligación de resolver", "Según el artículo 21.2 de la Ley 39/2015, el plazo máximo en el que debe notificarse la resolución expresa:",
  ["No podrá exceder de seis meses salvo que una norma con rango de Ley establezca uno mayor o así venga previsto en el Derecho de la Unión Europea.", "No podrá exceder de tres meses en ningún caso.", "No podrá exceder de seis meses salvo que un reglamento establezca uno mayor.", "No podrá exceder de un año en ningún caso."],
  "Art. 21.2 Ley 39/2015.", "Este plazo no podrá exceder de seis meses salvo que una norma con rango de Ley establezca uno mayor o así venga previsto en el Derecho de la Unión Europea"),
 (L, "Artículo 21", "Obligación de resolver", "Según el artículo 21.3 de la Ley 39/2015, cuando las normas reguladoras de los procedimientos no fijen el plazo máximo, este será de:",
  ["Tres meses.", "Seis meses.", "Un mes.", "Dos meses."],
  "Art. 21.3: «éste será de tres meses».", "Cuando las normas reguladoras de los procedimientos no fijen el plazo máximo, éste será de tres meses"),
 (L, "Artículo 21", "Obligación de resolver", "Según el artículo 21.3 b) de la Ley 39/2015, en los procedimientos iniciados a solicitud del interesado, el plazo máximo para resolver se cuenta:",
  ["Desde la fecha en que la solicitud haya tenido entrada en el registro electrónico de la Administración u Organismo competente para su tramitación.", "Desde la fecha del acuerdo de iniciación.", "Desde la fecha en que el interesado firmó la solicitud.", "Desde el día siguiente a la notificación del acuerdo de admisión."],
  "Art. 21.3: de oficio, desde el acuerdo de iniciación; a solicitud, desde la entrada en el registro electrónico del órgano competente.", "desde la fecha en que la solicitud haya tenido entrada en el registro electrónico de la Administración u Organismo competente para su tramitación"),
 (L, "Artículo 22", "Obligación de resolver", "Según el artículo 22.1 d) de la Ley 39/2015, cuando se soliciten informes preceptivos, la suspensión del plazo máximo para resolver:",
  ["No podrá exceder en ningún caso de tres meses.", "No podrá exceder en ningún caso de seis meses.", "Durará hasta la recepción del informe, sin límite.", "No podrá exceder de diez días."],
  "Art. 22.1 d) Ley 39/2015; si no se recibe el informe, prosigue el procedimiento.", "Este plazo de suspensión no podrá exceder en ningún caso de tres meses"),
 (L, "Artículo 24", "Silencio", "Según el artículo 24.1 de la Ley 39/2015, en los procedimientos iniciados a solicitud del interesado, el vencimiento del plazo máximo sin haberse notificado resolución expresa legitima al interesado para entenderla, con carácter general:",
  ["Estimada por silencio administrativo.", "Desestimada por silencio administrativo.", "Caducada.", "Suspendida hasta que se dicte resolución expresa."],
  "Art. 24.1: regla del silencio estimatorio, salvo norma con rango de ley, Derecho de la UE o internacional que establezca lo contrario.", "legitima al interesado o interesados para entenderla estimada por silencio administrativo"),
 (L, "Artículo 24", "Silencio", "Según el artículo 24.3 a) de la Ley 39/2015, en los casos de estimación por silencio administrativo, la resolución expresa posterior a la producción del acto:",
  ["Sólo podrá dictarse de ser confirmatoria del mismo.", "Se adoptará sin vinculación alguna al sentido del silencio.", "Podrá ser denegatoria si existen razones de interés general.", "No podrá dictarse en ningún caso."],
  "Art. 24.3 a); la letra b) (sin vinculación) es para la desestimación por silencio.", "la resolución expresa posterior a la producción del acto sólo podrá dictarse de ser confirmatoria del mismo"),
 (L, "Artículo 24", "Silencio", "Según el artículo 24.4 de la Ley 39/2015, el certificado acreditativo del silencio producido se expedirá de oficio por el órgano competente para resolver en el plazo de:",
  ["Quince días desde que expire el plazo máximo para resolver el procedimiento.", "Diez días desde que expire el plazo máximo para resolver el procedimiento.", "Un mes desde la presentación de la solicitud.", "Veinte días desde que el interesado lo pida."],
  "Art. 24.4 Ley 39/2015.", "Este certificado se expedirá de oficio por el órgano competente para resolver en el plazo de quince días desde que expire el plazo máximo para resolver el procedimiento"),
 (L, "Artículo 25", "Silencio", "Según el artículo 25.1 b) de la Ley 39/2015, en los procedimientos iniciados de oficio en que la Administración ejercite potestades sancionadoras, el vencimiento del plazo máximo sin resolución expresa notificada producirá:",
  ["La caducidad.", "La desestimación por silencio administrativo.", "La estimación por silencio administrativo.", "La prescripción de la infracción."],
  "Art. 25.1 b): caducidad y archivo de las actuaciones, con los efectos del art. 95.", "se producirá la caducidad"),
]:
    T.q(k, art, cat, enun, ops, expl, frag)
T.real("L", 57, "Ordenación"); T.real("L", 58, "Silencio"); T.real("P", 72, "Terminación"); T.real("P", 73, "Terminación"); T.real("X", 62, "Ordenación")

# Flashcards
for q_, a_, cat in [
  ("¿Qué procedimientos incluye el procedimiento común de la Ley 39/2015? (art. 1.1)", "El sancionador y el de reclamación de responsabilidad de las Administraciones Públicas.", "Las dos leyes"),
  ("¿Cómo pueden añadirse trámites adicionales o distintos? (art. 1.2)", "Solo mediante ley, cuando resulte eficaz, proporcionado y necesario, y de manera motivada.", "Las dos leyes"),
  ("¿Quiénes son Administraciones Públicas? (art. 2.3)", "AGE, CC. AA., Entidades de la Administración Local y los organismos públicos y entidades de derecho público vinculados o dependientes.", "Las dos leyes"),
  ("Formas de iniciación de oficio (art. 58)", "Propia iniciativa, orden superior, petición razonada de otros órganos o denuncia; siempre por acuerdo del órgano competente.", "Iniciación"),
  ("Medidas provisionales antes de iniciar (art. 56.2)", "Solo por urgencia inaplazable; se confirman, modifican o levantan en el acuerdo de iniciación, dentro de 15 días.", "Iniciación"),
  ("¿La denuncia da la condición de interesado? (art. 62.5)", "No, por sí sola.", "Iniciación"),
  ("Subsanación de la solicitud (art. 68)", "10 días (ampliables hasta 5, salvo selectivos o concurrencia competitiva); si no, desistimiento previa resolución.", "Iniciación"),
  ("Días hábiles (art. 30.2)", "Se excluyen sábados, domingos y festivos.", "Términos y plazos"),
  ("Plazos por horas (art. 30.1)", "Hábiles; de hora en hora y de minuto en minuto; máximo 24 horas.", "Términos y plazos"),
  ("Ampliación de plazos de trámite (art. 32)", "Hasta la mitad; antes del vencimiento; sin recurso.", "Términos y plazos"),
  ("Tramitación de urgencia (art. 33)", "Plazos a la mitad, salvo presentación de solicitudes y recursos; sin recurso.", "Términos y plazos"),
  ("Principio del art. 71 / del art. 72", "Celeridad (impulso de oficio) / simplificación administrativa (concentración de trámites).", "Ordenación"),
  ("Plazo general de los trámites de los interesados (art. 73.1)", "Diez días desde el siguiente a la notificación, salvo norma con plazo distinto.", "Ordenación"),
  ("Período de prueba (art. 77.2)", "Entre 10 y 30 días; extraordinario, hasta 10 días.", "Instrucción"),
  ("Informes por defecto (art. 80)", "Facultativos y no vinculantes; en 10 días.", "Instrucción"),
  ("Audiencia e información pública (arts. 82 y 83)", "Audiencia: 10 a 15 días, inmediatamente antes de la propuesta. Información pública: no menos de 20 días.", "Instrucción"),
  ("Formas de terminación (art. 84)", "Resolución, desistimiento, renuncia (si no está prohibida), caducidad e imposibilidad material sobrevenida.", "Terminación"),
  ("Caducidad del procedimiento a solicitud (art. 95)", "Paralización imputable al interesado; advertencia; a los 3 meses, archivo. No interrumpe la prescripción.", "Terminación"),
  ("Tramitación simplificada (art. 96.6)", "Resolución en 30 días; alegaciones en 5; audiencia solo si la resolución es desfavorable.", "Terminación"),
  ("Plazo máximo para resolver (art. 21)", "El de la norma; no más de 6 meses salvo ley o Derecho de la UE; si no se fija, 3 meses.", "Obligación de resolver"),
  ("Silencio desestimatorio a solicitud (art. 24.1)", "Petición (art. 29 CE), dominio o servicio público, medio ambiente, responsabilidad patrimonial, impugnación y revisión de oficio.", "Silencio"),
  ("Efectos del silencio (art. 24.2)", "Estimación: acto finalizador. Desestimación: solo permite recurrir.", "Silencio"),
  ("Vencimiento del plazo en procedimientos de oficio (art. 25)", "Favorables: desestimación. Sancionadores o de gravamen: caducidad.", "Silencio"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Procedimiento administrativo común", "Procedimiento común a todas las Administraciones Públicas que regula la Ley 39/2015, incluidos el sancionador y el de reclamación de responsabilidad (art. 1.1).", "s1", "Las dos leyes")
T.glos("Sector público institucional", "Organismos públicos y entidades de derecho público, entidades de derecho privado vinculadas o dependientes y Universidades públicas (art. 2.2 de ambas leyes).", "s1", "Las dos leyes")
T.glos("Medidas provisionales", "Medidas para asegurar la eficacia de la resolución que pudiera recaer, adoptadas de forma motivada y proporcionada (art. 56).", "s5", "Iniciación")
T.glos("Petición razonada", "Propuesta de iniciación formulada por un órgano sin competencia para iniciar; no vincula (art. 61).", "s6", "Iniciación")
T.glos("Denuncia", "Acto por el que cualquier persona pone en conocimiento de un órgano administrativo un hecho que pudiera justificar la iniciación de oficio; no da por sí sola la condición de interesado (art. 62).", "s6", "Iniciación")
T.glos("Declaración responsable", "Documento en el que el interesado manifiesta, bajo su responsabilidad, que cumple los requisitos, dispone de la documentación y la mantendrá (art. 69.1).", "s8", "Iniciación")
T.glos("Expediente administrativo", "Conjunto ordenado de documentos y actuaciones que sirven de antecedente y fundamento a la resolución, así como las diligencias para ejecutarla; formato electrónico (art. 70).", "s10", "Ordenación")
T.glos("Trámite de audiencia", "Puesta de manifiesto del procedimiento a los interesados, inmediatamente antes de la propuesta de resolución, con plazo de 10 a 15 días para alegar (art. 82).", "s14", "Instrucción")
T.glos("Información pública", "Período acordado por el órgano que resuelve para que cualquier persona examine el expediente y alegue, con un mínimo de 20 días (art. 83).", "s14", "Instrucción")
T.glos("Terminación convencional", "Fin del procedimiento, o trámite previo a la resolución, mediante acuerdos, pactos, convenios o contratos con los interesados (art. 86).", "s15", "Terminación")
T.glos("Caducidad", "Terminación por paralización imputable al interesado durante tres meses tras advertencia (art. 95), o por vencimiento del plazo en los procedimientos de oficio de gravamen (art. 25.1 b).", "s18", "Terminación")
T.glos("Tramitación simplificada", "Tramitación abreviada, por interés público o falta de complejidad, que se resuelve en 30 días con trámites tasados (art. 96).", "s19", "Terminación")
T.glos("Obligación de resolver", "Deber de la Administración de dictar resolución expresa y notificarla en todos los procedimientos, salvo las excepciones del art. 21.1.", "s20", "Obligación de resolver")
T.glos("Silencio administrativo", "Efecto que la ley atribuye al vencimiento del plazo máximo sin resolución expresa notificada: estimación o desestimación (arts. 24 y 25).", "s22", "Silencio")

# Cronología (fechas de los metadatos del BOE)
T.hito("2015", "Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas (BOE de 2-10-2015)", "Arts. 21 a 25 (obligación de resolver y silencio), 29 a 33 (plazos) y 54 a 96 (procedimiento)", "normativo", "s1")
T.hito("2015", "Ley 40/2015, de 1 de octubre, de Régimen Jurídico del Sector Público (BOE de 2-10-2015)", "Arts. 1 y 2: objeto y ámbito subjetivo", "normativo", "s2")
T.hito("2016", "Entrada en vigor de las Leyes 39/2015 y 40/2015 (2-10-2016, fecha de vigencia del BOE)", "Aplicación del procedimiento común y del régimen jurídico del sector público", "normativo", "s3")

T.publicar()
