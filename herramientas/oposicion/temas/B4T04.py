# -*- coding: utf-8 -*-
"""Tema IV.4 (B4T04): El acto administrativo: concepto, clases y elementos. Eficacia y
validez de los actos administrativos. Su motivación y notificación.
Método del I.2: mapa → bloques (I a V) con guía; cada artículo, texto literal del
BOE + ficha de casillas fijas; cierre 1 (preguntas oficiales) y cierre 2 (repaso)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

T = Tema("B4T04",
  "Cinco preguntas: I. Qué es el acto administrativo, qué clases distingue la ley y cuáles son sus elementos (arts. 34, 36 y 37 Ley 39/2015; art. 8 Ley 40/2015) · II. Cuándo produce efectos y cómo se ejecuta: eficacia (arts. 38, 39 y 97 a 100) · III. Cuándo es inválido y cómo se salva: validez (arts. 47 a 52) · IV. Cuándo hay que motivar (art. 35) · V. Cómo llega al interesado: notificación y publicación (arts. 40 a 46). Cada artículo: texto literal del BOE y ficha.",
  ["Acto administrativo", "Ley 39/2015", "Título III", "Elementos del acto", "Art. 34", "Forma", "Inderogabilidad singular", "Eficacia", "Art. 39", "Ejecutoriedad", "Ejecución forzosa", "Nulidad", "Art. 47", "Anulabilidad", "Art. 48", "Convalidación", "Motivación", "Art. 35", "Notificación", "Arts. 40-46", "Publicación"])

ESQ = "*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*"

# =============================================================================
T.ap("s0", "Mapa del tema: cinco preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque IV, tema 4):
> El acto administrativo: concepto, clases y elementos. Eficacia y validez de los actos administrativos. Su motivación y notificación.

### El hilo conductor

El epígrafe se lee como **cinco preguntas encadenadas**. Casi todo está en el **Título III de la Ley 39/2015** («De los actos administrativos», arts. 34 a 52). Cada pregunta es un bloque de los apuntes:

| Bloque | Pregunta | Ley 39/2015 | Otras normas |
|---|---|---|---|
| **I** | ¿Qué es el acto administrativo, qué clases distingue la ley y cuáles son sus elementos? | Arts. 34, 36 y 37 (clases: arts. 24.2, 112.1 y 114) | Ley 40/2015, art. 8 (competencia) |
| **II** | ¿Cuándo produce efectos y cómo se ejecuta? (eficacia) | Arts. 38 y 39; 97 a 100 | — |
| **III** | ¿Cuándo es inválido y cómo se salva? (validez) | Arts. 47 a 52 | Ley 40/2015, art. 23.4 |
| **IV** | ¿Cuándo hay que motivar? (motivación) | Art. 35 | — |
| **V** | ¿Cómo llega el acto al interesado? (notificación y publicación) | Arts. 40 a 46 | — |

!> **La idea que une los cinco bloques:** el acto lo dicta el **órgano competente**, con el contenido y la forma que exige la ley (I). Desde que se dicta **se presume válido y produce efectos**, y la Administración puede **ejecutarlo por sí misma** (II). Si tiene un vicio, la ley distingue el más grave (**nulidad**) del ordinario (**anulabilidad**), y procura **salvar** lo que se pueda (III). Ciertos actos deben **motivarse** (IV), y el acto llega al interesado por la **notificación** o la **publicación**, que condicionan su eficacia (V).

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- La Ley 39/2015 **no define** el acto administrativo ni enumera sus «clases»: lo que aquí se dice sobre concepto y clases es un **esquema** que se deduce de los artículos citados, no doctrina.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué es el acto administrativo, qué clases distingue la ley y cuáles son sus elementos?", donde(
  "Primera pregunta del tema. Antes de estudiar sus efectos o sus vicios hay que saber **qué rasgos** da la ley al acto administrativo, **qué tipos** de actos distingue y **qué requisitos** (elementos) debe reunir.",
  ["1 Concepto y clases que se deducen de la ley (arts. 24.2, 112.1 y 114)", "2 Elementos: competencia, contenido, procedimiento y forma (arts. 34, 36 y 37; Ley 40/2015, art. 8)", "3 Cuadro de clases y elementos"]))

T.ap("s1", "I.1 Concepto y clases que se deducen de la ley (arts. 24.2, 112.1 y 114)", f"""
{ESQ}

**Concepto.** La Ley 39/2015 no da una definición; de sus artículos se deducen estos **rasgos legales** del acto administrativo:

- Lo dictan las **Administraciones Públicas**, {c('L39', 'Artículo 34', 'bien de oficio o a instancia del interesado')}, y lo produce {c('L39', 'Artículo 34', 'el órgano competente')} (art. 34.1 → I.2.1).
- Está **sujeto al Derecho Administrativo**: {c('L39', 'Artículo 39', 'Los actos de las Administraciones Públicas sujetos al Derecho Administrativo se presumirán válidos')} (art. 39.1 → II.1.2) y {c('L39', 'Artículo 38', 'serán ejecutivos con arreglo a lo dispuesto en esta Ley')} (art. 38 → II.1.1).
- Es distinto de la **disposición de carácter general** (reglamento): las {c('L39', 'Artículo 37', 'resoluciones administrativas de carácter particular')} no pueden vulnerarla (art. 37.1 → I.2.3).

**Clases.** La ley usa estas categorías (el cuadro completo, en → I.3):

{unidad("1.1 Actos expresos y presuntos: la estimación por silencio (art. 24.2)",
  lit("L39", "Artículo 24", ["tiene a todos los efectos la consideración de acto administrativo finalizador del procedimiento", "tiene los solos efectos de permitir a los interesados la interposición del recurso"], solo=[4]),
  fichab("Valor del silencio administrativo como acto",
         "El interesado, ante la falta de resolución expresa en plazo",
         ["Estimación por silencio: **acto administrativo** finalizador del procedimiento", "Desestimación por silencio: solo permite **recurrir** (administrativa o contencioso-administrativamente)"],
         "—",
         f"Solo la **estimación** por silencio es un acto. La ley habla de {c('L39', 'Artículo 47', 'actos expresos o presuntos')} (art. 47.1 f → III.1.1). El régimen del silencio es del tema IV.11."))}

{unidad("1.2 Resoluciones y actos de trámite; actos de trámite cualificados (art. 112.1)",
  lit("L39", "Artículo 112", ["Contra las resoluciones y los actos de trámite, si estos últimos deciden directa o indirectamente el fondo del asunto, determinan la imposibilidad de continuar el procedimiento, producen indefensión o perjuicio irreparable", "La oposición a los restantes actos de trámite"], solo=[1, 2]),
  fichab("Distinción entre la resolución (pone fin al procedimiento) y los actos de trámite",
         "Los interesados (recurren)",
         ["::Son recurribles en alzada o reposición:", "Las **resoluciones**", "Los actos de trámite que deciden directa o indirectamente el **fondo** del asunto", "Los que determinan la **imposibilidad de continuar** el procedimiento", "Los que producen **indefensión** o **perjuicio irreparable** a derechos e intereses legítimos"],
         "—",
         "Los **restantes** actos de trámite no se recurren por separado: la oposición se alega para que se tenga en cuenta en la **resolución** que ponga fin al procedimiento. Los recursos son del tema IV.12."))}

{unidad("1.3 Actos que ponen fin a la vía administrativa (art. 114)",
  lit("L39", "Artículo 114", ["Las resoluciones de los recursos de alzada", "carezcan de superior jerárquico", "responsabilidad patrimonial", "Los actos administrativos de los miembros y órganos del Gobierno", "Ministros y los Secretarios de Estado", "Director general o superior"]),
  fichab("Actos contra los que ya no cabe recurso de alzada",
         "Según el órgano que los dicta o el procedimiento que resuelven",
         ["::Entre otros (114.1):", "Resoluciones de los recursos de **alzada**", "Resoluciones de órganos **sin superior jerárquico**, salvo que una Ley establezca lo contrario", "Resolución de los procedimientos de **responsabilidad patrimonial**", "En el ámbito **estatal** (114.2): miembros y órganos del Gobierno; **Ministros y Secretarios de Estado**; órganos con nivel de **Director general** o superior en materia de **personal**"],
         "—",
         f"La notificación debe indicar {c('L39', 'Artículo 40', 'si pone fin o no a la vía administrativa')} (art. 40.2 → V.1.1). El Director general pone fin a la vía solo en materia de **personal**."))}
""", 2)

T.ap("s2", "I.2 Elementos: competencia, contenido, procedimiento y forma (arts. 34, 36 y 37; Ley 40/2015, art. 8)", f"""
El art. 34 reúne en dos apartados los **elementos** del acto: quién lo dicta (órgano **competente**), cómo (**requisitos y procedimiento**) y qué dice (**contenido**). El art. 36 añade la **forma**; la **motivación**, que también es un requisito, tiene su propio bloque (→ IV.1).

{unidad("2.1 Producción y contenido (art. 34)",
  lit("L39", "Artículo 34", ["por el órgano competente", "ajustándose a los requisitos y al procedimiento establecido", "se ajustará a lo dispuesto por el ordenamiento jurídico y será determinado y adecuado a los fines de aquéllos"]),
  fichab("Cómo se produce el acto y qué debe decir",
         f"{c('L39', 'Artículo 34', 'el órgano competente')} (elemento subjetivo)",
         ["::Elementos que exige la ley:", "Órgano **competente**", "**Requisitos** y **procedimiento** establecidos", "**Contenido** ajustado al ordenamiento jurídico, **determinado** y **adecuado a los fines**"],
         "—",
         f"Iniciación **de oficio o a instancia** del interesado. Contenido «determinado y **adecuado a los fines**». La LJCA define la desviación de poder como {c('LJCA', 'Artículo 70', 'el ejercicio de potestades administrativas para fines distintos de los fijados por el ordenamiento jurídico')} (art. 70.2); en la Ley 39/2015 es causa de **anulabilidad** (art. 48.1 → III.1.2)."))}

{unidad("2.2 Forma (art. 36)",
  lit("L39", "Artículo 36", ["por escrito a través de medios electrónicos", "a menos que su naturaleza exija otra forma más adecuada de expresión y constancia", "por el titular del órgano inferior o funcionario que la reciba oralmente", "podrán refundirse en un único acto"]),
  fichab("Forma de exteriorizar el acto",
         "El órgano competente; si actúa de forma verbal, deja constancia escrita el **órgano inferior o funcionario** que lo recibe",
         ["Regla: **por escrito** a través de **medios electrónicos**", "Excepción: otra forma si la **naturaleza** del acto lo exige", "Actos verbales: constancia escrita **cuando sea necesaria**; de las **resoluciones** verbales, el titular autoriza una relación", "Actos de la misma naturaleza (nombramientos, concesiones, licencias): pueden **refundirse** en uno"],
         "—",
         "La constancia del acto verbal la firma quien **lo recibe**, no el titular de la competencia; el titular solo autoriza la **relación** de resoluciones verbales."))}

{unidad("2.3 Inderogabilidad singular (art. 37)",
  lit("L39", "Artículo 37", ["no podrán vulnerar lo establecido en una disposición de carácter general", "aunque aquéllas procedan de un órgano de igual o superior jerarquía", "Son nulas"]),
  fichab("Límite del contenido del acto: respetar los reglamentos",
         "Cualquier órgano, aunque sea de **igual o superior jerarquía** al que dictó la disposición general",
         "La resolución de carácter **particular** no puede vulnerar la disposición de carácter **general**",
         "—",
         "La consecuencia es la **nulidad** (37.2), no la anulabilidad. Vale aunque la resolución la dicte el **mismo** órgano o uno **superior**."))}

{unidad("2.4 La competencia (Ley 40/2015, art. 8.1)",
  lit("L40", "Artículo 8", ["La competencia es irrenunciable", "salvo los casos de delegación o avocación", "no suponen alteración de la titularidad de la competencia"], solo=[1, 2]),
  fichab("Elemento subjetivo: el órgano que tiene atribuida la competencia",
         "Los órganos administrativos que la tengan atribuida **como propia**",
         ["Es **irrenunciable**", "Excepciones al ejercicio por el titular: **delegación** o **avocación**, en los términos de la ley", "Delegación de competencias, encomienda de gestión, delegación de firma y suplencia **no alteran la titularidad**"],
         "—",
         "Si el órgano es **manifiestamente incompetente por razón de la materia o del territorio**, el acto es **nulo** (art. 47.1 b → III.1.1); la incompetencia **no determinante de nulidad** puede convalidarla el órgano competente cuando sea **superior jerárquico** del que dictó el acto (art. 52.3 → III.2.4)."))}
""", 2)

T.ap("s3", "I.3 Cuadro de clases y elementos (esquema)", f"""
{ESQ}

| Clase (según la ley) | Artículo | Por qué importa |
|---|---|---|
| **De oficio** / **a instancia** del interesado | 34.1 | Forma de iniciación |
| **Expresos** / **presuntos** (silencio) | 47.1 f, 24.2 | La estimación por silencio es acto finalizador; la desestimación solo abre el recurso |
| **Resoluciones** / **actos de trámite** (cualificados o no) | 112.1 | Solo resoluciones y trámites cualificados son recurribles en alzada o reposición |
| **Ponen fin** / **no ponen fin** a la vía administrativa | 114, 40.2 | Recurso procedente; se indica en la notificación |
| **Resoluciones de carácter particular** / disposiciones de carácter general | 37.1 | Inderogabilidad singular |
| Destinatario determinado / **pluralidad indeterminada** de personas | 45.1 a) | Se publican en lugar de notificarse |
| **Limitativos** de derechos / **favorables** al interesado | 35.1 a), 39.3 | Los primeros se motivan; los segundos admiten eficacia retroactiva |
| Dictados en ejercicio de **potestades discrecionales** | 35.1 i) | Se motivan |
| **Escritos** / **verbales** | 36 | Constancia escrita del acto verbal |
| **Nulos** / **anulables** | 47, 48 | Grado de invalidez (→ III.1) |

| Elemento | Qué exige la ley | Artículo | Vicio típico |
|---|---|---|---|
| Subjetivo: **competencia** | Órgano competente; competencia irrenunciable | 34.1; Ley 40/2015, 8.1 | Incompetencia manifiesta por materia o territorio: **nulidad** (47.1 b) |
| Objetivo: **contenido** | Ajustado al ordenamiento, determinado y adecuado a los fines | 34.2 | Contenido imposible: **nulidad** (47.1 c); desviación de poder: **anulabilidad** (48.1) |
| **Procedimiento** | El establecido | 34.1 | Prescindir total y absolutamente de él: **nulidad** (47.1 e) |
| **Forma** | Escrita y electrónica; motivación cuando proceda | 36, 35 | Defecto de forma: anulabilidad **solo** si falta un requisito indispensable o hay indefensión (48.2) |

{resumen([
  "La ley no define el acto: lo dicta la **Administración**, **de oficio o a instancia** del interesado, el **órgano competente**, sujeto al **Derecho Administrativo** (34.1, 38, 39.1).",
  "Clases que la ley usa: expresos y **presuntos** (24.2); **resoluciones** y actos de **trámite cualificados** (112.1); actos que **ponen fin a la vía administrativa** (114).",
  "Elementos: **competencia** (irrenunciable, Ley 40/2015 art. 8), **procedimiento**, **contenido** determinado y adecuado a los fines (34) y **forma** escrita electrónica (36).",
  "**Inderogabilidad singular**: una resolución particular no puede vulnerar un reglamento, aunque venga de un órgano igual o superior; si lo hace, es **nula** (37)."],
  "Siguiente: II. ¿Cuándo produce efectos el acto y cómo se ejecuta? La eficacia")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Cuándo produce efectos el acto y cómo se ejecuta? La eficacia (arts. 38, 39 y 97 a 100)", donde(
  "Segunda pregunta. El acto ya existe: ahora, **desde cuándo** produce efectos, si puede tener efectos **hacia atrás** y cómo puede la Administración **imponerlo** si el interesado no lo cumple.",
  ["1 Ejecutividad y efectos: presunción de validez, demora y retroactividad (arts. 38 y 39)", "2 Ejecutoriedad y ejecución forzosa (arts. 97 a 100)"]))

T.ap("s4", "II.1 Ejecutividad y efectos (arts. 38 y 39)", f"""
{unidad("1.1 Ejecutividad (art. 38)",
  lit("L39", "Artículo 38", ["serán ejecutivos"]),
  fichab("Los actos administrativos son ejecutivos",
         "Las Administraciones Públicas, respecto de sus actos **sujetos al Derecho Administrativo**",
         "«con arreglo a lo dispuesto en esta Ley» (excepciones del art. 98.1 → II.2.2)",
         "—",
         "Ejecutividad (art. 38) y **ejecutoriedad** (art. 98) son dos artículos distintos: el 98 enumera cuándo el acto **no** es inmediatamente ejecutivo."))}

{unidad("1.2 Presunción de validez y producción de efectos (art. 39.1 y 2)",
  lit("L39", "Artículo 39", ["se presumirán válidos y producirán efectos desde la fecha en que se dicten", "salvo que en ellos se disponga otra cosa", "La eficacia quedará demorada", "notificación, publicación o aprobación superior"], solo=[1, 2]),
  fichab("Desde cuándo produce efectos el acto",
         "—",
         ["Regla: efectos **desde la fecha en que se dicten**, salvo que el acto disponga otra cosa", "Se **presumen válidos**", "Eficacia **demorada**: cuando lo exija el **contenido** del acto o esté supeditada a **notificación, publicación o aprobación superior**"],
         "Desde la fecha en que se dicta",
         "Efectos desde que se **dicta**, no desde que se notifica (salvo que la eficacia esté supeditada a la notificación). Lo que se presume es la **validez** del acto."))}

{unidad("1.3 Eficacia retroactiva (art. 39.3)",
  lit("L39", "Artículo 39", ["Excepcionalmente", "cuando se dicten en sustitución de actos anulados", "cuando produzcan efectos favorables al interesado", "no lesione derechos o intereses legítimos de otras personas"], solo=[3]),
  fichab("Excepción: efectos hacia atrás",
         "El órgano que dicta el acto («podrá otorgarse»)",
         ["::Dos supuestos:", "Actos dictados **en sustitución de actos anulados**", "Actos que producen **efectos favorables** al interesado, siempre que los supuestos de hecho **ya existieran** en la fecha a la que se retrotrae y no se **lesionen** derechos o intereses legítimos de **otras personas**"],
         "—",
         "Es **excepcional** y **potestativa**. Los requisitos (supuesto de hecho previo y no lesionar a terceros) se exigen para los actos **favorables**. La convalidación se remite a este apartado (art. 52.2 → III.2.4)."))}

{unidad("1.4 Eficacia frente a otros órganos y otras Administraciones (art. 39.4 y 5)",
  lit("L39", "Artículo 39", ["deberán ser observadas por el resto de los órganos administrativos", "aunque no dependan jerárquicamente entre sí o pertenezcan a otra Administración", "podrá requerir a ésta previamente para que anule o revise el acto", "quedará suspendido el procedimiento para dictar resolución"], solo=[4, 5]),
  fichab("Vinculación de los demás órganos y requerimiento a otra Administración",
         "Todos los órganos administrativos (39.4); la Administración que debe dictar un acto basado en otro de **otra Administración** que considera ilegal (39.5)",
         ["Los actos dictados en ejercicio de la propia competencia **deben ser observados** por los demás órganos", "Si el acto base de otra Administración es ilegal: **requerimiento** previo (art. 44 LJCA) y, si se rechaza, **recurso contencioso-administrativo**"],
         "Mientras tanto, **queda suspendido** el procedimiento para dictar resolución",
         "La vinculación alcanza también a órganos **sin dependencia jerárquica** y de **otra Administración**."))}
""", 2)

T.ap("s5", "II.2 Ejecutoriedad y ejecución forzosa (arts. 97 a 100)", f"""
Los arts. 97 a 105 están en el Título IV (procedimiento), pero desarrollan la **eficacia** del acto: la Administración puede **ejecutarlo por sí misma**, incluso por la fuerza.

{unidad("2.1 Título: primero la resolución, después la ejecución material (art. 97)",
  lit("L39", "Artículo 97", ["sin que previamente haya sido adoptada la resolución que le sirva de fundamento jurídico", "estará obligado a notificar al particular interesado la resolución que autorice la actuación administrativa"]),
  fichab("Exigencia de un acto previo que sirva de título a la ejecución",
         "Las Administraciones Públicas; el órgano que ordena la ejecución material **notifica** la resolución",
         ["Ninguna actuación material de ejecución que **limite derechos** sin resolución **previa** que le sirva de fundamento jurídico", "Obligación de **notificar** al interesado la resolución que la autoriza"],
         "—",
         "Sin resolución previa, la actuación material carece de fundamento jurídico."))}

{unidad("2.2 Ejecutoriedad (art. 98.1)",
  lit("L39", "Artículo 98", ["serán inmediatamente ejecutivos", "Se produzca la suspensión de la ejecución del acto", "contra la que quepa algún recurso en vía administrativa, incluido el potestativo de reposición", "Una disposición establezca lo contrario", "Se necesite aprobación o autorización superior"], solo=[1, 2, 3, 4, 5]),
  fichab("Los actos son inmediatamente ejecutivos, salvo excepciones",
         "—",
         ["::No son inmediatamente ejecutivos cuando:", "Se **suspende** la ejecución", "Es una resolución **sancionadora** contra la que cabe algún **recurso en vía administrativa**, incluido el **potestativo de reposición**", "Una **disposición** establece lo contrario", "Se necesita **aprobación o autorización superior**"],
         "—",
         "La sanción no es ejecutiva mientras quepa recurso **administrativo**, también el **potestativo de reposición**: no hace falta esperar al contencioso."))}

{unidad("2.3 Ejecución forzosa (art. 99)",
  lit("L39", "Artículo 99", ["previo apercibimiento", "salvo en los supuestos en que se suspenda la ejecución de acuerdo con la Ley, o cuando la Constitución o la Ley exijan la intervención de un órgano judicial"]),
  fichab("La Administración impone el acto sin acudir al juez",
         "Las Administraciones Públicas, por sus **órganos competentes**",
         "**Previo apercibimiento**",
         "—",
         "Dos excepciones: ejecución **suspendida** de acuerdo con la Ley y casos en que la Constitución o la Ley exigen **intervención judicial**."))}

{unidad("2.4 Medios de ejecución forzosa (art. 100)",
  lit("L39", "Artículo 100", ["respetando siempre el principio de proporcionalidad", "Apremio sobre el patrimonio", "Ejecución subsidiaria", "Multa coercitiva", "Compulsión sobre las personas", "el menos restrictivo de la libertad individual", "la oportuna autorización judicial"]),
  fichab("Los cuatro medios con los que se ejecuta",
         "Las Administraciones Públicas; para entrar en el domicilio, **consentimiento** del titular o **autorización judicial**",
         ["**Apremio sobre el patrimonio** (cantidad líquida, art. 101)", "**Ejecución subsidiaria** (actos no personalísimos, a costa del obligado, art. 102)", "**Multa coercitiva** (cuando lo autoricen las Leyes, art. 103)", "**Compulsión sobre las personas** (obligaciones personalísimas de no hacer o soportar, art. 104)"],
         "—",
         f"Son **cuatro** y siempre con **proporcionalidad**; si caben varios, {c('L39', 'Artículo 100', 'el menos restrictivo de la libertad individual')}. No son medios: el «lanzamiento», el «arresto» ni el «embargo judicial» (→ Cierre 1)."))}

{resumen([
  "Ejecutividad: los actos sujetos al Derecho Administrativo **son ejecutivos** (38) y se **presumen válidos**; producen efectos **desde la fecha en que se dictan** (39.1).",
  "Eficacia **demorada** si lo exige el contenido o depende de **notificación, publicación o aprobación superior** (39.2); **retroactiva** solo excepcionalmente (sustitución de actos anulados o efectos favorables, 39.3).",
  "Inmediatamente ejecutivos **salvo** suspensión, sanción recurrible en vía administrativa, disposición en contra o aprobación superior (98.1).",
  "Ejecución forzosa **previo apercibimiento** (99) por **cuatro medios**: apremio, ejecución subsidiaria, multa coercitiva y compulsión; el menos restrictivo (100)."],
  "Siguiente: III. ¿Cuándo es inválido el acto y cómo se salva? La validez")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Cuándo es inválido el acto y cómo se salva? La validez (arts. 47 a 52)", donde(
  "Tercera pregunta. El acto se presume válido (→ II.1), pero puede tener vicios. La ley distingue dos grados: **nulidad de pleno derecho** (lista cerrada de vicios graves) y **anulabilidad** (cualquier otra infracción). Después fija reglas para **salvar** lo que se pueda.",
  ["1 Nulidad de pleno derecho y anulabilidad (arts. 47 y 48; Ley 40/2015, art. 23.4)", "2 Límites, conversión, conservación y convalidación (arts. 49 a 52)", "3 Cuadro: nulidad y anulabilidad"]))

T.ap("s6", "III.1 Nulidad de pleno derecho y anulabilidad (arts. 47 y 48; Ley 40/2015, art. 23.4)", f"""
{unidad("1.1 Nulidad de pleno derecho (art. 47)",
  lit("L39", "Artículo 47", ["susceptibles de amparo constitucional", "manifiestamente incompetente por razón de la materia o del territorio", "contenido imposible", "infracción penal", "prescindiendo total y absolutamente del procedimiento legalmente establecido", "reglas esenciales para la formación de la voluntad de los órganos colegiados", "carezca de los requisitos esenciales para su adquisición", "disposición con rango de Ley", "las disposiciones administrativas"]),
  fichab("El vicio más grave: lista tasada de causas",
         "Afecta a **actos** (47.1) y a **disposiciones** administrativas (47.2)",
         ["::Actos nulos (47.1):", "a) Lesionan derechos y libertades **susceptibles de amparo constitucional**", "b) Órgano **manifiestamente incompetente** por razón de la **materia** o del **territorio**", "c) Contenido **imposible**", "d) Constitutivos de **infracción penal** o dictados como consecuencia de ésta", "e) Dictados prescindiendo **total y absolutamente** del procedimiento, o de las reglas esenciales de formación de la voluntad de los **órganos colegiados**", "f) Actos expresos o **presuntos** que adquieren facultades o derechos sin los **requisitos esenciales**", "g) Los que establezca una disposición **con rango de Ley**"],
         "—",
         "La incompetencia que causa nulidad es la **manifiesta** y por **materia o territorio** (no por jerarquía). El procedimiento se omite «**total y absolutamente**». La letra g) exige **rango de Ley** (no basta un reglamento)."))}

{unidad("1.2 Anulabilidad (art. 48)",
  lit("L39", "Artículo 48", ["cualquier infracción del ordenamiento jurídico, incluso la desviación de poder", "cuando el acto carezca de los requisitos formales indispensables para alcanzar su fin o dé lugar a la indefensión de los interesados", "cuando así lo imponga la naturaleza del término o plazo"]),
  fichab("El vicio ordinario: cualquier otra infracción",
         "Actos de la Administración",
         ["Regla: **cualquier infracción** del ordenamiento jurídico, **incluso la desviación de poder**", "**Defecto de forma**: solo si faltan requisitos formales **indispensables** para alcanzar su fin o hay **indefensión**", "Actuación **fuera de plazo**: solo si lo impone la **naturaleza** del término o plazo"],
         "—",
         "La **desviación de poder** es causa de **anulabilidad**, no de nulidad. El defecto de forma y la actuación fuera de plazo solo anulan en los casos del 48.2 y del 48.3."))}

{unidad("1.3 Actuar con motivo de abstención no invalida necesariamente el acto (Ley 40/2015, art. 23.4)",
  lit("L40", "Artículo 23", ["no implicará, necesariamente, y en todo caso, la invalidez"], solo=[9]),
  fichab("Efecto de no abstenerse sobre la validez del acto",
         "Autoridades y personal en quienes concurren motivos de abstención",
         "Su intervención **no implica necesariamente** la invalidez del acto",
         "—",
         f"No hay invalidez automática; la no abstención {c('L40', 'Artículo 23', 'dará lugar a la responsabilidad que proceda')} (23.5)."))}
""", 2)

T.ap("s7", "III.2 Límites, conversión, conservación y convalidación (arts. 49 a 52)", f"""
Cuatro técnicas para que el vicio de un acto **no arrastre** más de lo necesario.

{unidad("2.1 Límites a la extensión de la invalidez (art. 49)",
  lit("L39", "Artículo 49", ["no implicará la de los sucesivos en el procedimiento que sean independientes del primero", "salvo que la parte viciada sea de tal importancia que sin ella el acto administrativo no hubiera sido dictado"]),
  fichab("La invalidez no se contagia a lo independiente",
         "—",
         ["Actos **sucesivos** del procedimiento **independientes** del viciado: se mantienen", "Partes **independientes** del acto: se mantienen, salvo que sin la parte viciada el acto **no se hubiera dictado**"],
         "—",
         "Vale tanto para la **nulidad** como para la **anulabilidad**."))}

{unidad("2.2 Conversión de actos viciados (art. 50)",
  lit("L39", "Artículo 50", ["contengan los elementos constitutivos de otro distinto producirán los efectos de éste"]),
  fichab("El acto viciado vale como otro distinto",
         "Actos **nulos o anulables**",
         "Si contienen los **elementos constitutivos** de otro acto distinto, producen los efectos de **éste**",
         "—",
         "Se aplica a actos **nulos** y **anulables** (a diferencia de la convalidación, solo para anulables)."))}

{unidad("2.3 Conservación de actos y trámites (art. 51)",
  lit("L39", "Artículo 51", ["dispondrá siempre la conservación", "cuyo contenido se hubiera mantenido igual de no haberse cometido la infracción"]),
  fichab("Se conservan los actos que no habrían cambiado",
         "El órgano que **declara la nulidad o anula** las actuaciones",
         "Conserva los actos y trámites cuyo contenido habría sido **igual** sin la infracción",
         "—",
         "Es obligatoria: «dispondrá **siempre**»."))}

{unidad("2.4 Convalidación (art. 52)",
  lit("L39", "Artículo 52", ["podrá convalidar los actos anulables", "producirá efecto desde su fecha", "incompetencia no determinante de nulidad", "cuando sea superior jerárquico del que dictó el acto viciado", "mediante el otorgamiento de la misma por el órgano competente"]),
  fichab("La Administración subsana el vicio del acto anulable",
         "La Administración; si el vicio es de **incompetencia**, el órgano competente que sea **superior jerárquico** del que dictó el acto; si falta una **autorización**, el órgano competente para otorgarla",
         ["Solo actos **anulables**, **subsanando** sus vicios", "Incompetencia **no determinante de nulidad**: convalida el superior jerárquico competente", "Falta de **autorización**: se convalida otorgándola"],
         "Efecto **desde su fecha**, salvo la retroactividad del art. 39.3 (→ II.1.3)",
         "Los actos **nulos no se convalidan**. El efecto es **desde la fecha** de la convalidación, no desde su publicación ni desde el acto viciado. Cayó **dos veces** en 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s8", "III.3 Cuadro: nulidad y anulabilidad (esquema)", f"""
{ESQ}

| | Nulidad de pleno derecho | Anulabilidad |
|---|---|---|
| Artículo | 47 | 48 |
| Causas | Lista **tasada** (47.1 a-g) y disposiciones (47.2) | **Cualquier** infracción del ordenamiento, **incluso la desviación de poder** |
| Incompetencia | **Manifiesta**, por **materia o territorio** (47.1 b) | La no determinante de nulidad (52.3) |
| Procedimiento y forma | Prescindir **total y absolutamente** del procedimiento (47.1 e) | Defecto de forma solo si falta un requisito **indispensable** o hay **indefensión** (48.2) |
| Fuera de plazo | — | Solo si lo impone la **naturaleza** del plazo (48.3) |
| Resoluciones que vulneran un reglamento | **Nulas** (37.2) | — |
| Conversión (50) | Sí | Sí |
| Convalidación (52) | **No** | **Sí** |

La revisión de oficio y los recursos que permiten declarar la nulidad o anular el acto son del tema IV.12.

{resumen([
  "**Nulidad**: lista tasada del 47.1 (derechos amparables, incompetencia **manifiesta por materia o territorio**, contenido imposible, infracción penal, prescindir **total y absolutamente** del procedimiento, adquisición sin requisitos esenciales, las que diga una ley).",
  "**Anulabilidad**: **cualquier** otra infracción, **incluso la desviación de poder**; defecto de forma y retraso solo en los casos del 48.2 y 48.3.",
  "Para salvar el acto: la invalidez no alcanza a lo **independiente** (49); **conversión** (50); **conservación** obligatoria (51); **convalidación** solo de **anulables**, con efecto **desde su fecha** (52)."],
  "Siguiente: IV. ¿Cuándo hay que motivar? La motivación")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Cuándo hay que motivar? La motivación (art. 35)", donde(
  "Cuarta pregunta. La motivación es la explicación de **por qué** se dicta el acto. La ley no exige motivar todos los actos: enumera **cuáles** y **cómo**.",
  ["1 Actos que deben motivarse y motivación en los procedimientos selectivos (art. 35)"]))

T.ap("s9", "IV.1 Actos que deben motivarse (art. 35)", f"""
{unidad("1.1 La lista del art. 35.1",
  lit("L39", "Artículo 35", ["con sucinta referencia de hechos y fundamentos de derecho", "Los actos que limiten derechos subjetivos o intereses legítimos", "procedimientos de arbitraje y los que declaren su inadmisión", "Los actos que se separen del criterio seguido en actuaciones precedentes o del dictamen de órganos consultivos", "Los acuerdos de suspensión de actos", "Los acuerdos de aplicación de la tramitación de urgencia, de ampliación de plazos y de realización de actuaciones complementarias", "Los actos que rechacen pruebas propuestas por los interesados", "Las propuestas de resolución en los procedimientos de carácter sancionador", "potestades discrecionales"], solo=list(range(1, 11))),
  fichab("Deber de motivar ciertos actos",
         "El órgano que dicta el acto",
         ["::Con **sucinta** referencia de **hechos y fundamentos de derecho**:", "a) Actos que **limiten** derechos subjetivos o intereses legítimos", "b) Los que resuelven **revisión de oficio**, **recursos** y **arbitraje**, y los que declaran su **inadmisión**", "c) Los que se **separan** del criterio precedente o del **dictamen** de órganos consultivos", "d) **Suspensión** de actos y **medidas provisionales** (art. 56)", "e) **Urgencia**, **ampliación de plazos** y **actuaciones complementarias**", "f) Los que **rechacen** pruebas", "g) Terminación por **imposibilidad material** sobrevenida y **desistimiento** de la Administración en procedimientos de oficio", "h) **Propuestas** de resolución sancionadoras y resoluciones **sancionadoras** o de **responsabilidad patrimonial**", "i) Actos **discrecionales** y los que deba motivar una disposición expresa"],
         "—",
         "Las trampas cambian el **sentido**: se motivan los actos que **limitan** derechos, que **se separan** del criterio o del dictamen, que **rechazan** pruebas (no los que las aceptan, ni los que siguen el criterio). La motivación es «**sucinta**»."))}

{unidad("1.2 Procedimientos selectivos y de concurrencia competitiva (art. 35.2)",
  lit("L39", "Artículo 35", ["de conformidad con lo que dispongan las normas que regulen sus convocatorias", "quedar acreditados en el procedimiento los fundamentos de la resolución"], solo=[11]),
  fichab("Motivación de los actos que ponen fin a procedimientos selectivos y de concurrencia competitiva",
         "El órgano que resuelve el procedimiento selectivo o de concurrencia",
         "Según las **normas que regulen sus convocatorias**",
         "—",
         "Siempre deben quedar **acreditados en el procedimiento** los fundamentos de la resolución."))}

{resumen([
  "No se motiva todo: solo la lista del **art. 35.1** (a-i), con **sucinta** referencia de **hechos y fundamentos de derecho**.",
  "Claves de la lista: actos que **limitan** derechos; revisión de oficio, **recursos** y su inadmisión; **separarse** del precedente o del **dictamen**; suspensión y medidas provisionales; **urgencia**, **ampliación de plazos** y actuaciones complementarias; **rechazo** de pruebas; sanciones y responsabilidad patrimonial; actos **discrecionales**.",
  "Procedimientos **selectivos** y de **concurrencia competitiva**: como digan sus **convocatorias**, acreditando los fundamentos (35.2)."],
  "Siguiente: V. ¿Cómo llega el acto al interesado? Notificación y publicación")}
""", 2)

# =============================================================================
T.ap("bV", "V. ¿Cómo llega el acto al interesado? Notificación y publicación (arts. 40 a 46)", donde(
  "Quinta pregunta. La eficacia del acto puede depender de su notificación o publicación (→ II.1.2). La ley fija **qué** debe contener la notificación, **en qué plazo**, **por qué medio** se practica, qué pasa si **no se puede** practicar y cuándo el acto se **publica** en lugar de notificarse.",
  ["1 La notificación: quién, plazo y contenido (art. 40)", "2 Cómo se practica: en papel y por medios electrónicos (arts. 41 a 43)", "3 Notificación infructuosa y publicación (arts. 44 a 46)"]))

T.ap("s10", "V.1 La notificación: quién, plazo y contenido (art. 40)", f"""
{unidad("1.1 Obligación, plazo y contenido (art. 40)",
  lit("L39", "Artículo 40", ["El órgano que dicte las resoluciones y actos administrativos los notificará", "dentro del plazo de diez días a partir de la fecha en que el acto haya sido dictado", "el texto íntegro de la resolución", "surtirán efecto a partir de la fecha en que el interesado realice actuaciones que supongan el conocimiento", "el intento de notificación debidamente acreditado"]),
  fichab("Comunicación del acto a los interesados cuyos derechos e intereses afecta",
         f"{c('L39', 'Artículo 40', 'El órgano que dicte las resoluciones y actos administrativos')}",
         ["::Contenido (40.2):", "**Texto íntegro** de la resolución", "Si pone fin o no a la **vía administrativa**", "**Recursos** procedentes, en vía administrativa y judicial", "**Órgano** ante el que presentarlos y **plazo** para interponerlos"],
         "**Diez días** desde que el acto se dicta (40.2)",
         "Notificación **defectuosa** (con texto íntegro pero sin los demás requisitos): efecto desde que el interesado actúa mostrando **conocimiento** o **interpone recurso** (40.3). Para cumplir el **plazo máximo** del procedimiento basta el **texto íntegro** y el **intento acreditado** (40.4)."))}
""", 2)

T.ap("s11", "V.2 Cómo se practica: en papel y por medios electrónicos (arts. 41 a 43)", f"""
{unidad("2.1 Condiciones generales (art. 41)",
  lit("L39", "Artículo 41", ["preferentemente por medios electrónicos", "comparecencia espontánea del interesado", "entrega directa de un empleado público", "Las que contengan medios de pago a favor de los obligados, tales como cheques", "dando por efectuado el trámite y siguiéndose el procedimiento", "La falta de práctica de este aviso no impedirá que la notificación sea considerada plenamente válida", "la de aquélla que se hubiera producido en primer lugar"]),
  fichab("Medio de notificación y requisitos de validez",
         "Las Administraciones; el interesado no obligado elige y puede cambiar el medio en cualquier momento",
         ["Regla: **preferentemente electrónica**; obligatoria para los **obligados** a relacionarse electrónicamente", "En papel: **comparecencia espontánea** en oficinas de registro o **entrega directa** por un empleado público", "**Nunca** electrónica: elementos no convertibles en formato electrónico y **medios de pago** (cheques)", "Válida si deja constancia de envío, recepción, fechas y horas, contenido íntegro e identidad de remitente y destinatario", "**Rechazo**: se da por efectuado el trámite", "**Aviso** al dispositivo o correo: su falta **no invalida** la notificación"],
         "—",
         "Si se notifica por **varios cauces**, vale la fecha de la **primera**. El correo electrónico del interesado sirve para **avisos**, **no** para practicar notificaciones."))}

{unidad("2.2 Notificaciones en papel (art. 42)",
  lit("L39", "Artículo 42", ["puestas a disposición del interesado en la sede electrónica", "cualquier persona mayor de catorce años", "por una sola vez y en una hora distinta dentro de los tres días siguientes", "antes de las quince horas", "al menos un margen de diferencia de tres horas"]),
  fichab("Práctica de la notificación en el domicilio",
         "El interesado o, si no está, **cualquier persona mayor de catorce años** que esté en el domicilio y haga constar su identidad",
         ["Toda notificación en papel se pone también a disposición en la **sede electrónica**", "Si nadie la recoge: **segundo intento**, una sola vez y en **hora distinta**", "Si el primero fue antes de las **15:00**, el segundo después (y viceversa), con **3 horas** de margen", "Si falla el segundo: anuncio (art. 44 → V.3.1)"],
         "Segundo intento dentro de los **tres días** siguientes",
         "**Catorce** años (no dieciocho). Dos intentos como **máximo** antes del anuncio en el BOE."))}

{unidad("2.3 Notificaciones electrónicas (art. 43)",
  lit("L39", "Artículo 43", ["comparecencia en la sede electrónica", "dirección electrónica habilitada única", "en el momento en que se produzca el acceso a su contenido", "diez días naturales desde la puesta a disposición", "Punto de Acceso General electrónico"]),
  fichab("Práctica de la notificación por medios electrónicos",
         "El interesado o su representante **debidamente identificado**",
         ["Por **comparecencia en la sede electrónica**, por la **dirección electrónica habilitada única** o por ambos", "Se entiende **practicada** cuando se **accede** al contenido", "Acceso también desde el **Punto de Acceso General** electrónico"],
         "Se entiende **rechazada** a los **diez días naturales** desde la puesta a disposición sin acceso (si es obligatoria o elegida)",
         "**Diez días naturales**, no hábiles. Para el plazo máximo del procedimiento basta la **puesta a disposición** (43.3)."))}
""", 2)

T.ap("s12", "V.3 Notificación infructuosa y publicación (arts. 44 a 46)", f"""
{unidad("3.1 Notificación infructuosa (art. 44)",
  lit("L39", "Artículo 44", ["un anuncio publicado en el «Boletín Oficial del Estado»", "con carácter facultativo"]),
  fichab("Notificación por anuncio cuando no se puede notificar",
         "Las Administraciones",
         ["::Procede cuando:", "Los interesados son **desconocidos**", "Se ignora el **lugar** de la notificación", "Intentada, **no se ha podido** practicar"],
         "—",
         "El anuncio va **siempre** en el **BOE**; el del boletín autonómico o provincial, tablón de edictos o consulado es **previo y facultativo**."))}

{unidad("3.2 Publicación (art. 45)",
  lit("L39", "Artículo 45", ["surtiendo ésta los efectos de la notificación", "pluralidad indeterminada de personas", "procedimiento selectivo o de concurrencia competitiva", "careciendo de validez las que se lleven a cabo en lugares distintos", "los mismos elementos que el artículo 40.2 exige", "en el diario oficial que corresponda", "se entenderá cumplida por su publicación en el Diario oficial correspondiente"]),
  fichab("Publicación del acto en lugar de, o además de, la notificación",
         "Cuando lo establezcan las normas del procedimiento o lo aconsejen razones de interés público apreciadas por el **órgano competente**",
         ["::Publicación obligatoria, con efectos de notificación:", "Destinatarios: **pluralidad indeterminada** de personas, o notificación individual **insuficiente** (en ese caso, adicional)", "Actos de procedimientos **selectivos** o de **concurrencia competitiva**: en el medio que indique la **convocatoria**"],
         "—",
         "Mismo contenido que la notificación (40.2). Se publica en el **diario oficial** de la Administración de que procede el acto; el tablón de anuncios se entiende cumplido con el **Diario oficial**."))}

{unidad("3.3 Indicación de notificaciones y publicaciones (art. 46)",
  lit("L39", "Artículo 46", ["lesiona derechos o intereses legítimos", "una somera indicación del contenido del acto"]),
  fichab("Publicación abreviada para proteger derechos",
         "El **órgano competente**, si aprecia que el anuncio o la publicación **lesiona derechos o intereses legítimos**",
         "Publica en el Diario oficial solo una **somera indicación** del contenido y del lugar donde comparecer para conocerlo",
         "Comparecencia en el plazo que se establezca",
         "Las formas complementarias de difusión son **facultativas** y no excluyen la publicación en el Diario oficial."))}

{resumen([
  "Notifica el **órgano que dicta** el acto, en **diez días**, con **texto íntegro**, si pone fin a la vía, **recursos**, órgano y plazo (40.2).",
  "Preferentemente **electrónica**; en papel, cualquier persona **mayor de 14 años** en el domicilio; segundo intento en **3 días** y en franja distinta (42).",
  "Electrónica: practicada al **acceder**; **rechazada** a los **10 días naturales** (43). Infructuosa: anuncio en el **BOE** (44).",
  "Publicación con efectos de notificación: **pluralidad indeterminada** de personas y procedimientos **selectivos** (45); **somera indicación** si lesiona derechos (46)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_L49 = examen("L", 49, {
  "a": f"Literal del art. 48.1: son anulables los actos que incurran en {c('L39', 'Artículo 48', 'cualquier infracción del ordenamiento jurídico, incluso la desviación de poder')}.",
  "b": f"Es causa de **nulidad**, no de anulabilidad: art. 47.1 a), {c('L39', 'Artículo 47', 'Los que lesionen los derechos y libertades susceptibles de amparo constitucional')}.",
  "c": f"Es causa de **nulidad**: art. 47.1 e), {c('L39', 'Artículo 47', 'Los dictados prescindiendo total y absolutamente del procedimiento legalmente establecido')}.",
  "d": "La «inexistencia jurídica» no figura en el art. 48 (ni en el 47): la Ley 39/2015 solo regula la nulidad de pleno derecho y la anulabilidad."},
  [("cualquier infracción del ordenamiento jurídico, incluso la desviación de poder", "L39", "Artículo 48", "Son anulables los actos de la Administración que incurran en cualquier infracción del ordenamiento jurídico, incluso la desviación de poder")])
EX_P53 = examen("P", 53, {
  "a": f"Cambia el sentido: se motivan {c('L39', 'Artículo 35', 'Los actos que se separen del criterio seguido en actuaciones precedentes o del dictamen de órganos consultivos')} (35.1 c), no los que **no** se separen.",
  "b": f"Cambia el sentido: se motivan {c('L39', 'Artículo 35', 'Los actos que rechacen pruebas propuestas por los interesados')} (35.1 f), no los que las aceptan.",
  "c": f"Cambia el sentido: se motivan {c('L39', 'Artículo 35', 'Los actos que limiten derechos subjetivos o intereses legítimos')} (35.1 a), no los que **no** los limitan.",
  "d": f"Literal del art. 35.1 e): {c('L39', 'Artículo 35', 'Los acuerdos de aplicación de la tramitación de urgencia, de ampliación de plazos y de realización de actuaciones complementarias')}."},
  [("Los acuerdos de aplicación de la tramitación de urgencia, de ampliación de plazos y de realización de actuaciones complementarias", "L39", "Artículo 35", "Los acuerdos de aplicación de la tramitación de urgencia, de ampliación de plazos y de realización de actuaciones complementarias")])
EX_P54 = examen("P", 54, {
  "a": f"Cambia «anulables» por «nulos»: {c('L39', 'Artículo 52', 'La Administración podrá convalidar los actos anulables, subsanando los vicios de que adolezcan')} (52.1).",
  "b": f"Cambia el momento: {c('L39', 'Artículo 52', 'El acto de convalidación producirá efecto desde su fecha')} (52.2), no desde su publicación en el BOE.",
  "c": f"Literal del art. 52.3: {c('L39', 'Artículo 52', 'Si el vicio consistiera en incompetencia no determinante de nulidad, la convalidación podrá realizarse por el órgano competente cuando sea superior jerárquico del que dictó el acto viciado')}.",
  "d": f"Invierte la regla: {c('L39', 'Artículo 52', 'podrá ser convalidado el acto mediante el otorgamiento de la misma por el órgano competente')} (52.4)."},
  [("incompetencia no determinante de nulidad, la convalidación podrá realizarse por el órgano competente cuando sea superior jerárquico del que dictó el acto viciado", "L39", "Artículo 52", "Si el vicio consistiera en incompetencia no determinante de nulidad, la convalidación podrá realizarse por el órgano competente cuando sea superior jerárquico del que dictó el acto viciado")])
EX_P55 = examen("P", 55, {
  "a": f"La incompetencia por razón de **jerarquía** no está en la lista de nulidad del art. 47.1 b) (que solo recoge la manifiesta {c('L39', 'Artículo 47', 'por razón de la materia o del territorio')}); es, por tanto, {c('L39', 'Artículo 52', 'incompetencia no determinante de nulidad')}, convalidable por el órgano competente {c('L39', 'Artículo 52', 'cuando sea superior jerárquico del que dictó el acto viciado')} (52.3).",
  "b": f"Es acto **nulo** (art. 47.1 e: {c('L39', 'Artículo 47', 'prescindiendo total y absolutamente del procedimiento legalmente establecido')}), y solo se convalidan {c('L39', 'Artículo 52', 'los actos anulables')}.",
  "c": f"La ley sitúa la incompetencia por razón del **territorio** (junto a la de la materia) entre las causas de **nulidad**: {c('L39', 'Artículo 47', 'Los dictados por órgano manifiestamente incompetente por razón de la materia o del territorio')} (47.1 b). ⚠ Matiz: la opción no dice «manifiestamente», y una incompetencia territorial no manifiesta sería anulable; pero el único supuesto de incompetencia que el art. 52.3 menciona expresamente como convalidable es el **jerárquico**, y por eso la plantilla da la a).",
  "d": f"Es acto **nulo**: {c('L39', 'Artículo 47', 'Los que sean constitutivos de infracción penal o se dicten como consecuencia de ésta')} (47.1 d)."},
  [("incompetente", "L39", "Artículo 52", "Si el vicio consistiera en incompetencia no determinante de nulidad"),
   ("jerarqu", "L39", "Artículo 52", "cuando sea superior jerárquico del que dictó el acto viciado")])
EX_P62 = examen("P", 62, {
  "a": f"El «lanzamiento» no está entre los cuatro medios del art. 100.1: {c('L39', 'Artículo 100', 'Apremio sobre el patrimonio')}, ejecución subsidiaria, multa coercitiva y compulsión sobre las personas.",
  "b": f"Literal del art. 100.1 b): {c('L39', 'Artículo 100', 'Ejecución subsidiaria')}.",
  "c": f"El «arresto personal» no es un medio de ejecución forzosa; el más cercano es la {c('L39', 'Artículo 100', 'Compulsión sobre las personas')}, que la ley solo admite {c('L39', 'Artículo 104', 'en los casos en que la ley expresamente lo autorice')} (art. 104.1).",
  "d": f"No es «embargo judicial»: la ejecución forzosa la hace la propia Administración; el medio patrimonial es el {c('L39', 'Artículo 100', 'Apremio sobre el patrimonio')} (art. 100.1 a)."},
  [("Ejecución subsidiaria", "L39", "Artículo 100", "b) Ejecución subsidiaria.")])

T.ap("s13", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **cinco** preguntas válidas de este tema (otra, la 52 de promoción interna, fue **anulada**). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-L 2025, pregunta 49 · Anulabilidad (→ III.1.2)", EX_L49,
  "### GACE-P 2025, pregunta 53 · Motivación (→ IV.1.1)", EX_P53,
  "### GACE-P 2025, pregunta 54 · Convalidación (→ III.2.4)", EX_P54,
  "### GACE-P 2025, pregunta 55 · Convalidación (→ III.2.4)", EX_P55,
  "### GACE-P 2025, pregunta 62 · Medios de ejecución forzosa (→ II.2.4)", EX_P62,
  "### Cómo se pregunta",
  "!> Las preguntas de este tema copian el artículo y cambian **una palabra**: «nulos» por «anulables», «desde su fecha» por «desde su publicación», «rechacen» por «acepten», «se separen» por «no se separen». Los distractores de anulabilidad son **causas de nulidad** del art. 47.",
]))

T.ap("s14", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Concepto, clases y elementos | Órgano competente, requisitos y procedimiento; contenido determinado y adecuado a los fines (34); forma escrita electrónica (36); inderogabilidad singular (37) | Resolución particular que vulnera un reglamento: **nula** (37.2) |
| II. Eficacia | Ejecutivos (38); presunción de validez y efectos desde que se dictan (39); excepciones a la ejecutividad inmediata (98); ejecución forzosa (99-100) | **Cuatro medios** de ejecución forzosa (100.1); efectos **desde la fecha en que se dicten** |
| III. Validez | Nulidad tasada (47); anulabilidad general (48); límites, conversión, conservación (49-51); convalidación (52) | **Desviación de poder** = anulabilidad; solo se convalidan los **anulables**, con efecto **desde su fecha** |
| IV. Motivación | Lista del 35.1 (a-i); selectivos según convocatoria (35.2) | Se motivan los que **limitan** derechos, **se separan** del criterio, **rechazan** pruebas, **urgencia y ampliación de plazos** |
| V. Notificación y publicación | 10 días y contenido (40); electrónica preferente (41); papel (42); electrónica (43); BOE (44); publicación (45-46) | **10 días** para cursarla; **14 años**; **10 días naturales** para el rechazo electrónico |

?> **Trampas frecuentes:** «la Administración podrá convalidar los actos **nulos**» (solo los **anulables**); «la convalidación produce efecto desde su **publicación**» (desde **su fecha**); «la desviación de poder es causa de **nulidad**» (es de **anulabilidad**); «incompetencia por razón de la **jerarquía**» como causa de nulidad (solo **materia o territorio**, y manifiesta); «se motivan los actos que **acepten** pruebas» (los que las **rechacen**); «la notificación se cursará en **quince** días» (son **diez**); «persona mayor de **dieciocho** años» (es de **catorce**); «diez días **hábiles**» en la notificación electrónica (son **naturales**).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
A = "Artículo"
T.q("L39", f"{A} 34", "Elementos del acto", "Según el artículo 34.1 de la Ley 39/2015, los actos administrativos que dicten las Administraciones Públicas, bien de oficio o a instancia del interesado, se producirán:",
    ["Por el órgano competente ajustándose a los requisitos y al procedimiento establecido.", "Por el superior jerárquico del órgano instructor, ajustándose al procedimiento establecido.", "Por cualquier órgano de la Administración actuante, previo informe del órgano competente.", "Por el órgano instructor, ajustándose a los requisitos establecidos en la convocatoria."],
    "Art. 34.1 Ley 39/2015.", "se producirán por el órgano competente ajustándose a los requisitos y al procedimiento establecido")
T.q("L39", f"{A} 34", "Elementos del acto", "Según el artículo 34.2 de la Ley 39/2015, el contenido de los actos se ajustará a lo dispuesto por el ordenamiento jurídico y será:",
    ["Determinado y adecuado a los fines de aquéllos.", "Proporcionado y suficiente para los fines de aquéllos.", "Determinado o determinable y adecuado al interés del solicitante.", "Motivado en todo caso con sucinta referencia de hechos."],
    "Art. 34.2 Ley 39/2015: «determinado y adecuado a los fines de aquéllos».", "será determinado y adecuado a los fines de aquéllos")
T.q("L39", f"{A} 36", "Elementos del acto", "Según el artículo 36.1 de la Ley 39/2015, los actos administrativos se producirán:",
    ["Por escrito a través de medios electrónicos, a menos que su naturaleza exija otra forma más adecuada de expresión y constancia.", "Por escrito en soporte papel, salvo que el interesado elija los medios electrónicos.", "Por escrito a través de medios electrónicos en todo caso, sin excepción.", "De forma verbal, salvo que el interesado solicite su constancia escrita."],
    "Art. 36.1 Ley 39/2015.", "Los actos administrativos se producirán por escrito a través de medios electrónicos, a menos que su naturaleza exija otra forma más adecuada de expresión y constancia")
T.q("L39", f"{A} 36", "Elementos del acto", "Según el artículo 36.2 de la Ley 39/2015, cuando los órganos administrativos ejerzan su competencia de forma verbal, la constancia escrita del acto, cuando sea necesaria, se efectuará y firmará por:",
    ["El titular del órgano inferior o funcionario que la reciba oralmente.", "El titular de la competencia que dictó el acto verbal.", "El secretario del órgano que dictó el acto.", "El interesado, en presencia de un funcionario."],
    "Art. 36.2 Ley 39/2015.", "se efectuará y firmará por el titular del órgano inferior o funcionario que la reciba oralmente")
T.q("L39", f"{A} 37", "Elementos del acto", "Según el artículo 37.2 de la Ley 39/2015, las resoluciones administrativas que vulneren lo establecido en una disposición reglamentaria son:",
    ["Nulas.", "Anulables.", "Válidas si proceden de un órgano de superior jerarquía al que dictó la disposición.", "Irregulares no invalidantes."],
    "Art. 37.2 Ley 39/2015: «Son nulas».", "Son nulas las resoluciones administrativas que vulneren lo establecido en una disposición reglamentaria")
T.q("L39", f"{A} 37", "Elementos del acto", "Según el artículo 37.1 de la Ley 39/2015, las resoluciones administrativas de carácter particular no podrán vulnerar lo establecido en una disposición de carácter general:",
    ["Aunque aquéllas procedan de un órgano de igual o superior jerarquía al que dictó la disposición general.", "Salvo que procedan de un órgano de superior jerarquía al que dictó la disposición general.", "Salvo que procedan del mismo órgano que dictó la disposición general.", "Salvo que se dicten en ejercicio de potestades discrecionales."],
    "Art. 37.1 Ley 39/2015 (inderogabilidad singular).", "aunque aquéllas procedan de un órgano de igual o superior jerarquía al que dictó la disposición general")
T.q("L40", f"{A} 8", "Elementos del acto", "Según el artículo 8.1 de la Ley 40/2015, la competencia es irrenunciable y se ejercerá por los órganos administrativos que la tengan atribuida como propia, salvo los casos de:",
    ["Delegación o avocación, cuando se efectúen en los términos previstos en ésta u otras leyes.", "Encomienda de gestión o delegación de firma.", "Suplencia o sustitución temporal.", "Desconcentración acordada por el superior jerárquico."],
    "Art. 8.1 Ley 40/2015.", "salvo los casos de delegación o avocación, cuando se efectúen en los términos previstos en ésta u otras leyes")
T.q("L39", f"{A} 24", "Clases de actos", "Según el artículo 24.2 de la Ley 39/2015, la estimación por silencio administrativo:",
    ["Tiene a todos los efectos la consideración de acto administrativo finalizador del procedimiento.", "Tiene los solos efectos de permitir a los interesados la interposición del recurso que resulte procedente.", "Solo tiene la consideración de acto administrativo si se expide certificado.", "Carece de efectos hasta que la Administración dicte resolución expresa."],
    "Art. 24.2 Ley 39/2015. La opción b) describe la **desestimación** por silencio.", "La estimación por silencio administrativo tiene a todos los efectos la consideración de acto administrativo finalizador del procedimiento")
T.q("L39", f"{A} 112", "Clases de actos", "Según el artículo 112.1 de la Ley 39/2015, la oposición a los actos de trámite que no deciden el fondo, ni impiden continuar el procedimiento, ni producen indefensión o perjuicio irreparable:",
    ["Podrá alegarse por los interesados para su consideración en la resolución que ponga fin al procedimiento.", "Podrá articularse mediante recurso de alzada.", "Podrá articularse mediante recurso potestativo de reposición.", "No podrá alegarse en ningún momento del procedimiento."],
    "Art. 112.1, párrafo segundo, Ley 39/2015.", "La oposición a los restantes actos de trámite podrá alegarse por los interesados para su consideración en la resolución que ponga fin al procedimiento")
T.q("L39", f"{A} 114", "Clases de actos", "Según el artículo 114.2 de la Ley 39/2015, en el ámbito estatal ponen fin a la vía administrativa los actos emanados de los órganos directivos con nivel de Director general o superior:",
    ["En relación con las competencias que tengan atribuidas en materia de personal.", "En todo caso.", "En relación con las competencias que tengan atribuidas en materia de contratación.", "Solo cuando actúen por delegación del Ministro."],
    "Art. 114.2 c) Ley 39/2015.", "en relación con las competencias que tengan atribuidas en materia de personal")
T.q("L39", f"{A} 39", "Eficacia", "Según el artículo 39.1 de la Ley 39/2015, los actos de las Administraciones Públicas sujetos al Derecho Administrativo se presumirán válidos y producirán efectos:",
    ["Desde la fecha en que se dicten, salvo que en ellos se disponga otra cosa.", "Desde la fecha de su notificación, en todo caso.", "Desde el día siguiente al de su publicación en el diario oficial.", "Desde que adquieran firmeza en vía administrativa."],
    "Art. 39.1 Ley 39/2015.", "producirán efectos desde la fecha en que se dicten, salvo que en ellos se disponga otra cosa")
T.q("L39", f"{A} 39", "Eficacia", "Según el artículo 39.2 de la Ley 39/2015, la eficacia del acto quedará demorada cuando así lo exija su contenido o esté supeditada a:",
    ["Su notificación, publicación o aprobación superior.", "Su firmeza en vía administrativa.", "El dictamen del Consejo de Estado.", "La expedición del certificado de silencio."],
    "Art. 39.2 Ley 39/2015.", "esté supeditada a su notificación, publicación o aprobación superior")
T.q("L39", f"{A} 39", "Eficacia", "Según el artículo 39.3 de la Ley 39/2015, excepcionalmente podrá otorgarse eficacia retroactiva a los actos:",
    ["Cuando se dicten en sustitución de actos anulados.", "Cuando impongan sanciones, si así lo motiva el órgano.", "Cuando limiten derechos subjetivos, si lo exige el interés público.", "Solo cuando lo autorice una norma con rango de ley."],
    "Art. 39.3 Ley 39/2015: sustitución de actos anulados y efectos favorables al interesado.", "cuando se dicten en sustitución de actos anulados")
T.q("L39", f"{A} 39", "Eficacia", "Según el artículo 39.3 de la Ley 39/2015, la eficacia retroactiva de los actos que produzcan efectos favorables al interesado exige que los supuestos de hecho necesarios existieran ya en la fecha a que se retrotraiga la eficacia y que ésta:",
    ["No lesione derechos o intereses legítimos de otras personas.", "Sea autorizada por el superior jerárquico.", "No supere el plazo de un año.", "Sea informada favorablemente por la Abogacía del Estado."],
    "Art. 39.3 Ley 39/2015.", "ésta no lesione derechos o intereses legítimos de otras personas")
T.q("L39", f"{A} 39", "Eficacia", "Según el artículo 39.5 de la Ley 39/2015, cuando una Administración deba dictar un acto que tenga por base otro dictado por una Administración distinta y entienda que es ilegal, podrá requerirla para que lo anule o revise; mientras tanto:",
    ["Quedará suspendido el procedimiento para dictar resolución.", "Podrá dictar resolución sin tener en cuenta el acto requerido.", "El acto requerido quedará automáticamente suspendido.", "Deberá solicitar dictamen del Consejo de Estado."],
    "Art. 39.5 Ley 39/2015.", "En estos casos, quedará suspendido el procedimiento para dictar resolución")
T.q("L39", f"{A} 98", "Ejecución", "Según el artículo 98.1 de la Ley 39/2015, NO serán inmediatamente ejecutivos los actos administrativos cuando:",
    ["Se trate de una resolución de un procedimiento de naturaleza sancionadora contra la que quepa algún recurso en vía administrativa, incluido el potestativo de reposición.", "Pongan fin a la vía administrativa.", "Se hayan dictado por un órgano colegiado.", "Hayan sido notificados por medios electrónicos."],
    "Art. 98.1 b) Ley 39/2015.", "Se trate de una resolución de un procedimiento de naturaleza sancionadora contra la que quepa algún recurso en vía administrativa, incluido el potestativo de reposición")
T.q("L39", f"{A} 99", "Ejecución", "Según el artículo 99 de la Ley 39/2015, las Administraciones Públicas podrán proceder a la ejecución forzosa de los actos administrativos:",
    ["Previo apercibimiento.", "Previa autorización judicial en todo caso.", "Previo dictamen del Consejo de Estado.", "Sin necesidad de apercibimiento previo."],
    "Art. 99 Ley 39/2015.", "podrán proceder, previo apercibimiento, a la ejecución forzosa")
T.q("L39", f"{A} 100", "Ejecución", "Según el artículo 100.2 de la Ley 39/2015, si fueran varios los medios de ejecución admisibles:",
    ["Se elegirá el menos restrictivo de la libertad individual.", "Se elegirá el más rápido y eficaz.", "Elegirá el interesado.", "Se aplicarán todos de forma sucesiva."],
    "Art. 100.2 Ley 39/2015.", "se elegirá el menos restrictivo de la libertad individual")
T.q("L39", f"{A} 100", "Ejecución", "Según el artículo 100.3 de la Ley 39/2015, si para la ejecución forzosa fuese necesario entrar en el domicilio del afectado, las Administraciones Públicas deberán obtener:",
    ["El consentimiento del mismo o, en su defecto, la oportuna autorización judicial.", "La autorización del Delegado del Gobierno.", "La autorización judicial en todo caso, aunque el afectado consienta.", "El informe previo del Ministerio Fiscal."],
    "Art. 100.3 Ley 39/2015.", "deberán obtener el consentimiento del mismo o, en su defecto, la oportuna autorización judicial")
T.q("L39", f"{A} 47", "Validez", "Según el artículo 47.1 de la Ley 39/2015, son nulos de pleno derecho los actos dictados por órgano manifiestamente incompetente por razón de:",
    ["La materia o del territorio.", "La materia o de la jerarquía.", "La jerarquía o del territorio.", "La cuantía o de la materia."],
    "Art. 47.1 b) Ley 39/2015.", "Los dictados por órgano manifiestamente incompetente por razón de la materia o del territorio")
T.q("L39", f"{A} 47", "Validez", "Según el artículo 47.1 de la Ley 39/2015, ¿cuál de los siguientes actos es nulo de pleno derecho?",
    ["El que tenga un contenido imposible.", "El que incurra en desviación de poder.", "El dictado fuera del tiempo establecido para ello.", "El que carezca de alguno de los requisitos formales."],
    "Art. 47.1 c) Ley 39/2015. Las demás son supuestos del art. 48 (anulabilidad).", "Los que tengan un contenido imposible")
T.q("L39", f"{A} 47", "Validez", "Según el artículo 47.1 a) de la Ley 39/2015, son nulos de pleno derecho los actos que lesionen:",
    ["Los derechos y libertades susceptibles de amparo constitucional.", "Cualquier derecho reconocido en el Título I de la Constitución.", "Los derechos subjetivos o intereses legítimos de los interesados.", "Los principios rectores de la política social y económica."],
    "Art. 47.1 a) Ley 39/2015.", "Los que lesionen los derechos y libertades susceptibles de amparo constitucional")
T.q("L39", f"{A} 47", "Validez", "Según el artículo 47.1 g) de la Ley 39/2015, también son nulos de pleno derecho los actos en cualquier otro caso que se establezca expresamente en:",
    ["Una disposición con rango de Ley.", "Una disposición reglamentaria.", "Una orden ministerial.", "Una instrucción del superior jerárquico."],
    "Art. 47.1 g) Ley 39/2015.", "Cualquier otro que se establezca expresamente en una disposición con rango de Ley")
T.q("L39", f"{A} 48", "Validez", "Según el artículo 48.2 de la Ley 39/2015, el defecto de forma sólo determinará la anulabilidad cuando el acto:",
    ["Carezca de los requisitos formales indispensables para alcanzar su fin o dé lugar a la indefensión de los interesados.", "Haya sido dictado fuera de plazo.", "No haya sido notificado en el plazo de diez días.", "No esté motivado, en todo caso."],
    "Art. 48.2 Ley 39/2015.", "cuando el acto carezca de los requisitos formales indispensables para alcanzar su fin o dé lugar a la indefensión de los interesados")
T.q("L39", f"{A} 48", "Validez", "Según el artículo 48.3 de la Ley 39/2015, la realización de actuaciones administrativas fuera del tiempo establecido para ellas:",
    ["Sólo implicará la anulabilidad del acto cuando así lo imponga la naturaleza del término o plazo.", "Determinará en todo caso la nulidad de pleno derecho del acto.", "Determinará en todo caso la anulabilidad del acto.", "No afectará nunca a la validez del acto."],
    "Art. 48.3 Ley 39/2015.", "sólo implicará la anulabilidad del acto cuando así lo imponga la naturaleza del término o plazo")
T.q("L39", f"{A} 49", "Validez", "Según el artículo 49.1 de la Ley 39/2015, la nulidad o anulabilidad de un acto:",
    ["No implicará la de los sucesivos en el procedimiento que sean independientes del primero.", "Implicará la de todos los actos sucesivos del procedimiento.", "Implicará la de los actos anteriores del procedimiento.", "Implicará la de los sucesivos, salvo que se convaliden."],
    "Art. 49.1 Ley 39/2015.", "no implicará la de los sucesivos en el procedimiento que sean independientes del primero")
T.q("L39", f"{A} 50", "Validez", "Según el artículo 50 de la Ley 39/2015, los actos nulos o anulables que contengan los elementos constitutivos de otro distinto:",
    ["Producirán los efectos de éste.", "Deberán ser convalidados por el superior jerárquico.", "Carecerán de todo efecto.", "Producirán sus efectos propios hasta su revisión de oficio."],
    "Art. 50 Ley 39/2015 (conversión).", "contengan los elementos constitutivos de otro distinto producirán los efectos de éste")
T.q("L39", f"{A} 51", "Validez", "Según el artículo 51 de la Ley 39/2015, el órgano que declare la nulidad o anule las actuaciones:",
    ["Dispondrá siempre la conservación de aquellos actos y trámites cuyo contenido se hubiera mantenido igual de no haberse cometido la infracción.", "Podrá disponer la conservación de los actos y trámites si lo solicita el interesado.", "Retrotraerá en todo caso las actuaciones al inicio del procedimiento.", "Dispondrá la conservación solo de los actos favorables al interesado."],
    "Art. 51 Ley 39/2015.", "dispondrá siempre la conservación de aquellos actos y trámites cuyo contenido se hubiera mantenido igual de no haberse cometido la infracción")
T.q("L39", f"{A} 52", "Validez", "Según el artículo 52.1 de la Ley 39/2015, la Administración podrá convalidar:",
    ["Los actos anulables, subsanando los vicios de que adolezcan.", "Los actos nulos y anulables, subsanando los vicios de que adolezcan.", "Los actos nulos, previo dictamen del Consejo de Estado.", "Solo los actos dictados por órgano incompetente por razón del territorio."],
    "Art. 52.1 Ley 39/2015.", "La Administración podrá convalidar los actos anulables, subsanando los vicios de que adolezcan")
T.q("L39", f"{A} 52", "Validez", "Según el artículo 52.4 de la Ley 39/2015, si el vicio consistiese en la falta de alguna autorización:",
    ["Podrá ser convalidado el acto mediante el otorgamiento de la misma por el órgano competente.", "El acto será nulo de pleno derecho.", "El acto no podrá convalidarse.", "Solo podrá convalidarlo el órgano que dictó el acto viciado."],
    "Art. 52.4 Ley 39/2015.", "podrá ser convalidado el acto mediante el otorgamiento de la misma por el órgano competente")
T.q("L39", f"{A} 35", "Motivación", "Según el artículo 35.1 de la Ley 39/2015, los actos que deban ser motivados lo serán:",
    ["Con sucinta referencia de hechos y fundamentos de derecho.", "Con exhaustiva referencia de hechos y fundamentos de derecho.", "Con referencia a los fundamentos de derecho, sin necesidad de mencionar los hechos.", "Mediante remisión al informe del órgano instructor, en todo caso."],
    "Art. 35.1 Ley 39/2015.", "Serán motivados, con sucinta referencia de hechos y fundamentos de derecho")
T.q("L39", f"{A} 35", "Motivación", "Según el artículo 35.1 de la Ley 39/2015, ¿cuál de los siguientes actos debe ser motivado?",
    ["Los actos que rechacen pruebas propuestas por los interesados.", "Los actos que admitan las pruebas propuestas por los interesados.", "Los actos que sigan el criterio seguido en actuaciones precedentes.", "Los actos que acuerden la tramitación ordinaria del procedimiento."],
    "Art. 35.1 f) Ley 39/2015.", "Los actos que rechacen pruebas propuestas por los interesados")
T.q("L39", f"{A} 35", "Motivación", "Según el artículo 35.1 h) de la Ley 39/2015, deben motivarse, en los procedimientos de carácter sancionador:",
    ["Las propuestas de resolución.", "Los acuerdos de iniciación únicamente.", "Las diligencias de notificación.", "Los actos de mero trámite que no causen indefensión."],
    "Art. 35.1 h) Ley 39/2015: propuestas de resolución en los sancionadores y actos que resuelvan procedimientos sancionadores o de responsabilidad patrimonial.", "Las propuestas de resolución en los procedimientos de carácter sancionador")
T.q("L39", f"{A} 35", "Motivación", "Según el artículo 35.2 de la Ley 39/2015, la motivación de los actos que pongan fin a los procedimientos selectivos y de concurrencia competitiva se realizará:",
    ["De conformidad con lo que dispongan las normas que regulen sus convocatorias.", "Con referencia exhaustiva a la puntuación de cada aspirante, en todo caso.", "Solo si lo solicita algún interesado.", "Mediante informe del órgano de selección publicado en el BOE."],
    "Art. 35.2 Ley 39/2015.", "se realizará de conformidad con lo que dispongan las normas que regulen sus convocatorias")
T.q("L39", f"{A} 40", "Notificación", "Según el artículo 40.2 de la Ley 39/2015, toda notificación deberá ser cursada dentro del plazo de:",
    ["Diez días a partir de la fecha en que el acto haya sido dictado.", "Quince días a partir de la fecha en que el acto haya sido dictado.", "Diez días a partir de la fecha en que el acto haya sido firmado por el interesado.", "Un mes a partir de la fecha en que el acto haya sido dictado."],
    "Art. 40.2 Ley 39/2015.", "dentro del plazo de diez días a partir de la fecha en que el acto haya sido dictado")
T.q("L39", f"{A} 40", "Notificación", "Según el artículo 40.3 de la Ley 39/2015, las notificaciones que, conteniendo el texto íntegro del acto, omitiesen alguno de los demás requisitos:",
    ["Surtirán efecto a partir de la fecha en que el interesado realice actuaciones que supongan el conocimiento del contenido y alcance del acto, o interponga cualquier recurso que proceda.", "Serán nulas de pleno derecho.", "Surtirán efecto a los seis meses de su práctica.", "No surtirán efecto en ningún caso."],
    "Art. 40.3 Ley 39/2015.", "surtirán efecto a partir de la fecha en que el interesado realice actuaciones que supongan el conocimiento del contenido y alcance de la resolución o acto objeto de la notificación, o interponga cualquier recurso que proceda")
T.q("L39", f"{A} 40", "Notificación", "Según el artículo 40.4 de la Ley 39/2015, a los solos efectos de entender cumplida la obligación de notificar dentro del plazo máximo de duración de los procedimientos, será suficiente la notificación que contenga, cuando menos:",
    ["El texto íntegro de la resolución, así como el intento de notificación debidamente acreditado.", "Un extracto de la resolución y el intento de notificación.", "La indicación de los recursos que procedan.", "El texto íntegro de la resolución y la firma del interesado."],
    "Art. 40.4 Ley 39/2015.", "el texto íntegro de la resolución, así como el intento de notificación debidamente acreditado")
T.q("L39", f"{A} 41", "Notificación", "Según el artículo 41.2 de la Ley 39/2015, en ningún caso se efectuarán por medios electrónicos las notificaciones:",
    ["Que contengan medios de pago a favor de los obligados, tales como cheques.", "Dirigidas a personas jurídicas.", "Que pongan fin a la vía administrativa.", "Que se practiquen en procedimientos sancionadores."],
    "Art. 41.2 b) Ley 39/2015.", "Las que contengan medios de pago a favor de los obligados, tales como cheques")
T.q("L39", f"{A} 41", "Notificación", "Según el artículo 41.5 de la Ley 39/2015, cuando el interesado o su representante rechace la notificación de una actuación administrativa:",
    ["Se hará constar en el expediente, dando por efectuado el trámite y siguiéndose el procedimiento.", "Se repetirá la notificación en el plazo de tres días.", "Se publicará un anuncio en el Boletín Oficial del Estado.", "Se suspenderá el procedimiento hasta que la acepte."],
    "Art. 41.5 Ley 39/2015.", "dando por efectuado el trámite y siguiéndose el procedimiento")
T.q("L39", f"{A} 41", "Notificación", "Según el artículo 41.7 de la Ley 39/2015, cuando el interesado fuera notificado por distintos cauces, se tomará como fecha de notificación:",
    ["La de aquélla que se hubiera producido en primer lugar.", "La de aquélla que se hubiera producido en último lugar.", "La de la notificación electrónica, en todo caso.", "La que elija el interesado."],
    "Art. 41.7 Ley 39/2015.", "se tomará como fecha de notificación la de aquélla que se hubiera producido en primer lugar")
T.q("L39", f"{A} 42", "Notificación", "Según el artículo 42.2 de la Ley 39/2015, cuando la notificación se practique en el domicilio del interesado y éste no se halle presente, podrá hacerse cargo de ella:",
    ["Cualquier persona mayor de catorce años que se encuentre en el domicilio y haga constar su identidad.", "Cualquier persona mayor de dieciocho años que se encuentre en el domicilio.", "Solo un familiar del interesado mayor de edad.", "El portero o conserje de la finca, en todo caso."],
    "Art. 42.2 Ley 39/2015.", "cualquier persona mayor de catorce años que se encuentre en el domicilio y haga constar su identidad")
T.q("L39", f"{A} 42", "Notificación", "Según el artículo 42.2 de la Ley 39/2015, si nadie se hiciera cargo de la notificación en el domicilio, el intento se repetirá por una sola vez y en una hora distinta dentro de:",
    ["Los tres días siguientes.", "Los cinco días siguientes.", "Los diez días siguientes.", "Las veinticuatro horas siguientes."],
    "Art. 42.2 Ley 39/2015.", "intento que se repetirá por una sola vez y en una hora distinta dentro de los tres días siguientes")
T.q("L39", f"{A} 43", "Notificación", "Según el artículo 43.2 de la Ley 39/2015, cuando la notificación por medios electrónicos sea de carácter obligatorio o haya sido expresamente elegida por el interesado, se entenderá rechazada cuando hayan transcurrido sin acceder a su contenido:",
    ["Diez días naturales desde la puesta a disposición de la notificación.", "Diez días hábiles desde la puesta a disposición de la notificación.", "Quince días naturales desde el envío del aviso.", "Cinco días hábiles desde la puesta a disposición de la notificación."],
    "Art. 43.2 Ley 39/2015: diez días **naturales**.", "se entenderá rechazada cuando hayan transcurrido diez días naturales desde la puesta a disposición de la notificación sin que se acceda a su contenido")
T.q("L39", f"{A} 43", "Notificación", "Según el artículo 43.2 de la Ley 39/2015, las notificaciones por medios electrónicos se entenderán practicadas:",
    ["En el momento en que se produzca el acceso a su contenido.", "En el momento de su puesta a disposición en la sede electrónica.", "Al enviarse el aviso al correo electrónico del interesado.", "Al día siguiente de su puesta a disposición."],
    "Art. 43.2 Ley 39/2015.", "Las notificaciones por medios electrónicos se entenderán practicadas en el momento en que se produzca el acceso a su contenido")
T.q("L39", f"{A} 44", "Notificación", "Según el artículo 44 de la Ley 39/2015, cuando los interesados sean desconocidos, se ignore el lugar de la notificación o, intentada, no se hubiese podido practicar, la notificación se hará por medio de un anuncio publicado en:",
    ["El «Boletín Oficial del Estado».", "El boletín oficial de la provincia del último domicilio.", "El tablón de edictos del Ayuntamiento del último domicilio.", "La sede electrónica del órgano que dictó el acto, exclusivamente."],
    "Art. 44 Ley 39/2015. Los demás anuncios son previos y facultativos.", "la notificación se hará por medio de un anuncio publicado en el «Boletín Oficial del Estado»")
T.q("L39", f"{A} 45", "Publicación", "Según el artículo 45.1 de la Ley 39/2015, los actos administrativos serán en todo caso objeto de publicación, surtiendo ésta los efectos de la notificación:",
    ["Cuando el acto tenga por destinatario a una pluralidad indeterminada de personas.", "Cuando el acto ponga fin a la vía administrativa.", "Cuando el interesado lo solicite expresamente.", "Cuando el acto limite derechos subjetivos."],
    "Art. 45.1 a) Ley 39/2015.", "Cuando el acto tenga por destinatario a una pluralidad indeterminada de personas")
T.q("L39", f"{A} 46", "Publicación", "Según el artículo 46 de la Ley 39/2015, si el órgano competente apreciase que la publicación de un acto lesiona derechos o intereses legítimos:",
    ["Se limitará a publicar en el Diario oficial que corresponda una somera indicación del contenido del acto y del lugar donde los interesados podrán comparecer.", "No publicará el acto y lo notificará personalmente a cada interesado.", "Publicará el acto íntegro solo en la sede electrónica.", "Suspenderá la eficacia del acto hasta que los interesados comparezcan."],
    "Art. 46 Ley 39/2015.", "se limitará a publicar en el Diario oficial que corresponda una somera indicación del contenido del acto y del lugar donde los interesados podrán comparecer")
T.real("L", 49, "Validez"); T.real("P", 53, "Motivación"); T.real("P", 54, "Validez"); T.real("P", 55, "Validez"); T.real("P", 62, "Ejecución")

# Flashcards
for q_, a_, cat in [
  ("Elementos del acto según el art. 34", "Órgano competente; requisitos y procedimiento establecidos; contenido ajustado al ordenamiento, determinado y adecuado a los fines.", "Elementos del acto"),
  ("Forma de los actos (art. 36.1)", "Por escrito a través de medios electrónicos, salvo que su naturaleza exija otra forma más adecuada.", "Elementos del acto"),
  ("¿Quién firma la constancia escrita de un acto verbal? (art. 36.2)", "El titular del órgano inferior o funcionario que la reciba oralmente.", "Elementos del acto"),
  ("Inderogabilidad singular (art. 37)", "Una resolución particular no puede vulnerar una disposición general, aunque proceda de órgano igual o superior; si vulnera un reglamento, es nula.", "Elementos del acto"),
  ("¿Qué vale la estimación por silencio? (art. 24.2)", "A todos los efectos, acto administrativo finalizador del procedimiento.", "Clases de actos"),
  ("Actos de trámite recurribles (art. 112.1)", "Los que deciden directa o indirectamente el fondo, impiden continuar el procedimiento o producen indefensión o perjuicio irreparable.", "Clases de actos"),
  ("¿Desde cuándo producen efectos los actos? (art. 39.1)", "Desde la fecha en que se dicten, salvo que en ellos se disponga otra cosa; se presumen válidos.", "Eficacia"),
  ("Eficacia demorada (art. 39.2)", "Cuando lo exija el contenido o esté supeditada a notificación, publicación o aprobación superior.", "Eficacia"),
  ("Eficacia retroactiva (art. 39.3)", "Excepcional: actos en sustitución de actos anulados y actos favorables (supuesto de hecho previo y sin lesionar a terceros).", "Eficacia"),
  ("Excepciones a la ejecutividad inmediata (art. 98.1)", "Suspensión; sanción recurrible en vía administrativa (incluida la reposición); disposición en contra; aprobación o autorización superior.", "Ejecución"),
  ("Medios de ejecución forzosa (art. 100.1)", "Apremio sobre el patrimonio, ejecución subsidiaria, multa coercitiva y compulsión sobre las personas.", "Ejecución"),
  ("Causas de nulidad de pleno derecho (art. 47.1)", "Derechos amparables; incompetencia manifiesta por materia o territorio; contenido imposible; infracción penal; prescindir total y absolutamente del procedimiento; adquisición sin requisitos esenciales; las que diga una ley.", "Validez"),
  ("Anulabilidad (art. 48.1)", "Cualquier infracción del ordenamiento jurídico, incluso la desviación de poder.", "Validez"),
  ("¿Cuándo anula el defecto de forma? (art. 48.2)", "Solo si faltan requisitos formales indispensables para alcanzar su fin o hay indefensión.", "Validez"),
  ("Conversión (art. 50)", "El acto nulo o anulable con los elementos de otro distinto produce los efectos de éste.", "Validez"),
  ("Convalidación (art. 52)", "Solo actos anulables; efecto desde su fecha (salvo 39.3); incompetencia no determinante de nulidad: el superior jerárquico competente; falta de autorización: otorgándola.", "Validez"),
  ("Forma de la motivación (art. 35.1)", "Con sucinta referencia de hechos y fundamentos de derecho.", "Motivación"),
  ("Plazo y contenido de la notificación (art. 40.2)", "Diez días desde que se dicta; texto íntegro, si pone fin a la vía, recursos, órgano y plazo.", "Notificación"),
  ("Notificación en papel en el domicilio (art. 42.2)", "Persona mayor de 14 años; si nadie, segundo intento una vez, en hora distinta, dentro de 3 días (franja de mañana/tarde, 3 h de margen).", "Notificación"),
  ("Notificación electrónica: ¿cuándo se practica y cuándo se rechaza? (art. 43.2)", "Practicada al acceder al contenido; rechazada a los 10 días naturales sin acceso.", "Notificación"),
  ("Notificación infructuosa (art. 44)", "Anuncio en el Boletín Oficial del Estado (previo y facultativo, en otros boletines o tablones).", "Notificación"),
  ("Publicación obligatoria (art. 45.1)", "Pluralidad indeterminada de destinatarios y procedimientos selectivos o de concurrencia competitiva.", "Publicación"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Acto administrativo", "En la Ley 39/2015 (que no lo define): el que dicta el órgano competente de una Administración Pública, de oficio o a instancia del interesado, sujeto al Derecho Administrativo (arts. 34, 38 y 39).", "s1", "Concepto y clases")
T.glos("Acto de trámite cualificado", "Acto de trámite recurrible porque decide directa o indirectamente el fondo, impide continuar el procedimiento o produce indefensión o perjuicio irreparable (art. 112.1).", "s1", "Concepto y clases")
T.glos("Inderogabilidad singular", "Prohibición de que una resolución particular vulnere una disposición general, aunque proceda de órgano igual o superior; si vulnera un reglamento es nula (art. 37).", "s2", "Elementos")
T.glos("Competencia", "Elemento subjetivo del acto: irrenunciable; la ejerce el órgano que la tiene atribuida como propia, salvo delegación o avocación (Ley 40/2015, art. 8.1).", "s2", "Elementos")
T.glos("Ejecutividad", "Cualidad de los actos sujetos al Derecho Administrativo de ser ejecutivos con arreglo a la Ley 39/2015 (art. 38).", "s4", "Eficacia")
T.glos("Eficacia demorada", "Aplazamiento de los efectos del acto cuando lo exige su contenido o depende de notificación, publicación o aprobación superior (art. 39.2).", "s4", "Eficacia")
T.glos("Ejecución forzosa", "Ejecución del acto por la propia Administración, previo apercibimiento, mediante apremio, ejecución subsidiaria, multa coercitiva o compulsión (arts. 99 y 100).", "s5", "Eficacia")
T.glos("Nulidad de pleno derecho", "Grado máximo de invalidez, por las causas tasadas del art. 47.1 (y para disposiciones, 47.2). No admite convalidación.", "s6", "Validez")
T.glos("Anulabilidad", "Invalidez por cualquier infracción del ordenamiento jurídico, incluso la desviación de poder (art. 48.1).", "s6", "Validez")
T.glos("Conversión", "Efecto por el que el acto nulo o anulable que contiene los elementos de otro distinto produce los efectos de éste (art. 50).", "s7", "Validez")
T.glos("Convalidación", "Subsanación por la Administración de los vicios de un acto anulable; produce efecto desde su fecha (art. 52).", "s7", "Validez")
T.glos("Motivación", "Expresión, con sucinta referencia de hechos y fundamentos de derecho, de las razones del acto en los casos del art. 35.", "s9", "Motivación")
T.glos("Notificación", "Comunicación del acto a los interesados cuyos derechos e intereses afecta, en diez días y con el contenido del art. 40.2.", "s10", "Notificación")
T.glos("Dirección electrónica habilitada única", "Uno de los sistemas para practicar notificaciones electrónicas, junto con la comparecencia en la sede electrónica (art. 43.1).", "s11", "Notificación")
T.glos("Publicación", "Medio de dar a conocer el acto en el diario oficial; sustituye a la notificación en los casos del art. 45.1.", "s12", "Publicación")

# Cronología (fechas de los metadatos del BOE)
T.hito("2015", "Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas (BOE de 2-10-2015)", "Título III (arts. 34 a 52): los actos administrativos", "normativo", "s1")
T.hito("2015", "Ley 40/2015, de 1 de octubre, de Régimen Jurídico del Sector Público (BOE de 2-10-2015)", "Art. 8: la competencia; art. 23: abstención", "normativo", "s2")
T.hito("2016", "Entrada en vigor de las Leyes 39/2015 y 40/2015 (2-10-2016)", "Deroga la Ley 30/1992, de Régimen Jurídico de las Administraciones Públicas y del Procedimiento Administrativo Común (disposición derogatoria única)", "normativo", "s6")
T.hito("2021", "Efectos de las previsiones sobre registro electrónico y punto de acceso general electrónico de la Ley 39/2015 (2-4-2021)", "Disposición final séptima: el Punto de Acceso General permite acceder a las notificaciones (art. 43.4)", "normativo", "s11")

T.publicar()
