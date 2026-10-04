# -*- coding: utf-8 -*-
"""Tema V.3 (B5T03): Planificación de recursos humanos. Ofertas de empleo público.
Selección de personal. Las competencias en materia de personal.
Método del I.2: mapa → bloques (I a IV) con guía; cada artículo, texto literal del
BOE + ficha de casillas fijas; cierre 1 (preguntas oficiales) y cierre 2 (repaso).
Normas (textos consolidados del BOE): TREBEP (RDLeg 5/2015), arts. 10.2, 11.3, 12.3,
55 a 61, 69 a 71 y 100; Real Decreto-ley 6/2023, libro segundo (arts. 106 a 110, 112,
114 y 115); Real Decreto 364/1995 (Reglamento General de Ingreso), arts. 3 a 33;
Ley 30/1984, arts. 3 (salvo 3.2 e y f), 4, 5, 9 y 13 (apartados 1 y 5); Real Decreto
2169/1984 (atribución de competencias en materia de personal), arts. 3 a 13."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO["RDL6"] = "RDL 6/2023"
CORTO["RD364"] = "RD 364/1995"
CORTO["L30"] = "Ley 30/1984"
CORTO["RD2169"] = "RD 2169/1984"

T = Tema("B5T03",
  "Cuatro preguntas: I. Cómo planifica la Administración sus recursos humanos (TREBEP, arts. 69 y 71; RDL 6/2023, arts. 106 a 110) · II. Qué es la oferta de empleo público y en qué plazos se ejecuta (TREBEP, art. 70; RDL 6/2023, art. 108; RD 364/1995, arts. 7 a 9) · III. Cómo se selecciona al personal (TREBEP, arts. 55 a 61; RDL 6/2023, arts. 112, 114 y 115; RD 364/1995) · IV. Quién tiene las competencias en materia de personal (TREBEP, art. 100; Ley 30/1984; RD 2169/1984). Cada artículo: texto literal del BOE y ficha.",
  ["Planificación", "RDL 6/2023", "Oferta de empleo público", "Tres años", "Promoción interna 30 %", "Selección", "Art. 55 TREBEP", "Órganos de selección", "Oposición", "Concurso-oposición", "RD 364/1995", "Personal laboral fijo", "Competencias en materia de personal", "RD 2169/1984"])

AVISO_364 = "?> **Aviso de vigencia (RD 364/1995).** El Reglamento General de Ingreso es de **1995**: anterior al TREBEP (2015) y al Real Decreto-ley 6/2023. Se cita literal, tal como figura en el texto consolidado del BOE, y las denominaciones de órganos son las de su texto («Ministro para las Administraciones Públicas», «Secretario de Estado para la Administración Pública»…). Cuando la norma con rango de ley regula lo mismo de otra forma, la ficha lo señala."

# =============================================================================
T.ap("s0", "Mapa del tema: cuatro preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque V, tema 3):
> Planificación de recursos humanos. Ofertas de empleo público. Selección de personal. Las competencias en materia de personal.

### El hilo conductor

El epígrafe se lee como **cuatro preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | TREBEP (norma básica) | Administración del Estado |
|---|---|---|---|
| **I** | ¿Cómo planifica la Administración sus recursos humanos? | Arts. 69 y 71 | RDL 6/2023, arts. 106, 107, 109 y 110; Ley 30/1984, art. 13 |
| **II** | ¿Qué es la oferta de empleo público y en qué plazos se ejecuta? | Art. 70 | RDL 6/2023, art. 108; RD 364/1995, arts. 7 a 9 |
| **III** | ¿Cómo se selecciona al personal? | Arts. 10.2, 11.3, 55 a 61 | RDL 6/2023, arts. 112, 114 y 115; RD 364/1995, arts. 3 a 33 |
| **IV** | ¿Quién tiene las competencias en materia de personal? | Art. 100 | Ley 30/1984, arts. 3, 4, 5 y 9; RD 2169/1984, arts. 3 a 13 |

!> **La idea que une los cuatro bloques:** la Administración **planifica** cuánto personal necesita (I); las plazas de nuevo ingreso con dotación se recogen en la **oferta de empleo público**, que obliga a convocar y fija plazos (II); las plazas se cubren con procesos **selectivos** abiertos, con publicidad, órganos de selección imparciales y sistemas tasados (III); y cada paso lo decide un **órgano** concreto: el Gobierno aprueba la oferta, los Departamentos convocan, el Secretario de Estado nombra (IV).

### Las normas del tema

- **TREBEP** (texto refundido aprobado por el Real Decreto Legislativo 5/2015): las bases para todas las Administraciones.
- **Real Decreto-ley 6/2023**, libro segundo: las reglas propias de la **Administración del Estado** sobre planificación estratégica, oferta y acceso (art. 105.3 y 5).
- **Real Decreto 364/1995**: Reglamento General de Ingreso del personal de la Administración General del Estado (su título III, provisión de puestos, es del tema V.4).
- **Ley 30/1984** y **Real Decreto 2169/1984**: reparto de las competencias en materia de personal en la Administración del Estado. De la Ley 30/1984 solo se citan preceptos que no figuran en la lista de la disposición derogatoria única del TREBEP.

{AVISO_364}

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- Fronteras: clases de personal y adquisición de la condición de funcionario (tema V.1); provisión de puestos, promoción interna y carrera (tema V.4); personal laboral (tema V.7); acceso de personas con discapacidad (tema V.10).
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Cómo planifica la Administración sus recursos humanos? (TREBEP, arts. 69 y 71; RDL 6/2023, arts. 106 a 110)", donde(
  "Primera pregunta del tema. Antes de ofertar plazas o seleccionar a nadie, la Administración tiene que saber **cuánto personal necesita, con qué perfil y dónde**. El TREBEP fija los objetivos e instrumentos de la planificación para todas las Administraciones; el Real Decreto-ley 6/2023 la convierte en **planificación estratégica** para la Administración del Estado.",
  ["1 Objetivos, planes y registros de personal (TREBEP, arts. 69 y 71; Ley 30/1984, art. 13)", "2 La planificación estratégica en la Administración del Estado (RDL 6/2023, arts. 106, 107, 109 y 110)"]))

T.ap("s1", "I.1 Objetivos, planes y registros de personal (TREBEP, arts. 69 y 71; Ley 30/1984, art. 13)", f"""
{unidad("1.1 Objetivos e instrumentos de la planificación (TREBEP, art. 69)",
  lit("TREBEP", "Artículo 69", ["eficacia en la prestación de los servicios", "eficiencia en la utilización de los recursos económicos disponibles", "podrán aprobar Planes para la ordenación de sus recursos humanos", "suspensión de incorporaciones de personal externo", "La previsión de la incorporación de recursos humanos a través de la Oferta de empleo público"]),
  fichab("Planificación de los recursos humanos de las Administraciones Públicas",
         f"{c('TREBEP', 'Artículo 69', 'Cada Administración Pública')}, según sus propias normas (69.3)",
         ["::Planes para la ordenación de los recursos humanos (69.2), con medidas como:", "a) Análisis de disponibilidades y necesidades de personal (número de efectivos y perfiles o cualificación)", "b) Previsiones sobre organización del trabajo y estructuras de puestos", "c) Movilidad: incluso suspender incorporaciones de personal externo o convocar concursos limitados a personal de ciertos ámbitos", "d) Promoción interna, formación y movilidad forzosa", "e) Previsión de incorporaciones a través de la Oferta de empleo público (→ II.1)"],
         "—",
         f"Objetivo doble: {c('TREBEP', 'Artículo 69', 'eficacia en la prestación de los servicios')} y {c('TREBEP', 'Artículo 69', 'eficiencia en la utilización de los recursos económicos disponibles')}. Los planes son **potestativos** («podrán aprobar») e incluyen «**entre otras, algunas**» de las medidas: la lista no es cerrada."))}

{unidad("1.2 Registros de personal y gestión integrada (TREBEP, art. 71; Ley 30/1984, art. 13.1 y 5)",
  lit("TREBEP", "Artículo 71", ["Cada Administración Pública constituirá un Registro", "Mediante convenio de Conferencia Sectorial", "gestión integrada de recursos humanos"]),
  lit("L30", "Artículo trece", ["En la Dirección General de la Función Pública existirá un Registro Central", "no figurará ningún dato relativo a su raza, religión u opinión", "libre acceso a su expediente individual"], solo=[1, 6, 7]),
  fichab("Registro de los datos del personal de cada Administración",
         f"Cada Administración; en la del Estado, el Registro Central, {c('L30', 'Artículo trece', 'En la Dirección General de la Función Pública')}",
         ["Se inscriben los datos del personal de los arts. 2 y 5 del TREBEP (71.1) y puede incluir información agregada del resto de su sector público (71.2)", "Contenidos mínimos comunes: por **convenio de Conferencia Sectorial** (71.3)", "Registro Central: inscripción de **todo** el personal de la Administración del Estado y anotación preceptiva de los actos que afecten a su vida administrativa (Ley 30/1984, art. 13.1)"],
         "—",
         "En el expediente no figura ningún dato de **raza, religión u opinión**, y el personal tiene **libre acceso** a su expediente (Ley 30/1984, art. 13.5). Si una Entidad Local no tiene capacidad, cooperan la AGE y las Comunidades Autónomas (71.5)."))}
""", 2)

T.ap("s2", "I.2 La planificación estratégica en la Administración del Estado (RDL 6/2023, arts. 106, 107, 109 y 110)", f"""
El libro segundo del Real Decreto-ley 6/2023 se aplica a la **Administración del Estado** (AGE, sus organismos y entidades vinculados o dependientes: art. 105.5) y empieza por la planificación.

{unidad("2.1 La planificación como principio de organización (RDL 6/2023, art. 106)",
  lit("RDL6", "Artículo 106", ["planes de actuación o instrumentos de planificación estratégica equivalentes"]),
  fichab("Principio general: la Administración del Estado actúa conforme a planes",
         "La Administración del Estado",
         c("RDL6", "Artículo 106", "conforme a planes de actuación o instrumentos de planificación estratégica equivalentes"),
         "—",
         "Es el primer artículo del título I del libro segundo, «Planificación estratégica de los recursos humanos»."))}

{unidad("2.2 La planificación estratégica de los recursos humanos (RDL 6/2023, art. 107)",
  lit("RDL6", "Artículo 107", ["escenario plurianual de empleo público", "periódicamente revisable", "articular la oferta de empleo público", "planes de ámbito general y planes específicos de los departamentos ministeriales u organismos públicos", "dictará normas y directrices", "negociación colectiva previa", "evaluación posterior"]),
  fichab("Fundamento de actuación en materia de función pública de la Administración del Estado",
         f"La Administración del Estado; {c('RDL6', 'Artículo 107', 'El departamento ministerial con competencias en materia de función pública')} dicta normas y directrices para elaborarla",
         ["Establece el **escenario plurianual** de empleo público, dentro de las previsiones presupuestarias (107.1)", "Contenido mínimo: criterios y medidas para la **oferta de empleo público**, la movilidad, la provisión, la promoción interna, los itinerarios formativos y los objetivos de desempeño (107.3)", "Se estructura en **planes de ámbito general** y **planes específicos** de departamentos u organismos, sin perjuicio de planes de reestructuración de sectores (107.4)"],
         f"{c('RDL6', 'Artículo 107', 'periódicamente revisable')}; negociación colectiva **previa** y evaluación **posterior** (107.5)",
         "Plurianual y revisable. Todos los instrumentos de planificación pasan por **negociación colectiva previa** y **evaluación posterior**."))}

{unidad("2.3 Las relaciones de puestos de trabajo (RDL 6/2023, art. 109)",
  lit("RDL6", "Artículo 109", ["instrumentos técnicos de planificación", "son públicas", "naturaleza funcionarial, laboral y eventual", "lenguaje no sexista"]),
  fichab("Instrumento técnico de planificación para organizar, racionalizar y ordenar el personal",
         "La Administración del Estado",
         ["Incluyen, de forma conjunta o separada, **todos** los puestos de naturaleza funcionarial, laboral y eventual (109.1)", "Puestos ordenados por denominaciones tipo y características análogas (109.2)", "En ámbitos específicos, otros instrumentos de ordenación pueden sustituirlas (109.3)"],
         "—",
         "Las RPT son **públicas** e incluyen también los puestos de personal **eventual**. Su uso para la provisión de puestos es del tema V.4."))}

{unidad("2.4 Estructuración de puestos y áreas funcionales (RDL 6/2023, art. 110)",
  lit("RDL6", "Artículo 110", ["grado de responsabilidad exigida", "análisis acerca del perfil de competencias", "adscritos a una o varias áreas funcionales", "Reglamentariamente se determinarán las áreas funcionales"]),
  fichab("Ordenación de los puestos de trabajo",
         "La Administración del Estado; las áreas funcionales y sus cuerpos o escalas, por reglamento (110.3)",
         ["Niveles según el **grado de responsabilidad** (110.1)", "Crear, modificar o suprimir un puesto exige un **análisis del perfil de competencias** (110.2)", "Con carácter general, puestos **adscritos a una o varias áreas funcionales** (110.3), que pueden agruparse por características comunes (110.4)", "Puestos de personal laboral: según su normativa específica (110.5)"],
         "—",
         "Pregunta oficial relacionada (→ Cierre 1): los puestos se adscriben a **áreas funcionales**, no a la oferta de empleo público, a perfiles profesionales ni al Registro Central de Personal."))}

{resumen([
  "TREBEP: planificar sirve a la **eficacia** de los servicios y la **eficiencia** de los recursos; los **Planes** de ordenación son potestativos y la oferta de empleo público es una de sus medidas (69).",
  "Cada Administración tiene un **Registro** de personal; contenidos mínimos por **convenio de Conferencia Sectorial** (71); en la AGE, Registro Central en la Dirección General de la Función Pública (Ley 30/1984, art. 13).",
  "RDL 6/2023: planificación **estratégica**, **plurianual** y revisable, con planes generales y específicos, **negociación colectiva previa** y **evaluación posterior** (107).",
  "RPT: instrumentos técnicos de planificación, **públicas**, con puestos funcionariales, laborales y eventuales (109); puestos adscritos a **áreas funcionales** (110)."],
  "Siguiente: II. ¿Qué es la oferta de empleo público y en qué plazos se ejecuta?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Qué es la oferta de empleo público y en qué plazos se ejecuta? (TREBEP, art. 70; RDL 6/2023, art. 108; RD 364/1995, arts. 7 a 9)", donde(
  "Segunda pregunta. La planificación detecta necesidades; las que deben cubrirse con **personal de nuevo ingreso** y tienen **dotación presupuestaria** van a la **oferta de empleo público**. Es el paso que obliga a convocar los procesos selectivos y fija los plazos que más se preguntan.",
  ["1 La oferta en el TREBEP y en el RDL 6/2023 (TREBEP, art. 70; RDL 6/2023, art. 108)", "2 La oferta en el Reglamento General de Ingreso y cuadro de plazos (RD 364/1995, arts. 7 a 9)"]))

T.ap("s3", "II.1 La oferta de empleo público (TREBEP, art. 70; RDL 6/2023, art. 108)", f"""
{unidad("1.1 Contenido, efectos y plazo de ejecución (TREBEP, art. 70)",
  lit("TREBEP", "Artículo 70", ["con asignación presupuestaria", "hasta un diez por cien adicional", "dentro del plazo improrrogable de tres años", "se aprobará anualmente por los órganos de Gobierno", "deberá ser publicada en el Diario oficial correspondiente"]),
  fichab("Instrumento que recoge las necesidades de personal de nuevo ingreso",
         f"La aprueban {c('TREBEP', 'Artículo 70', 'anualmente')} los {c('TREBEP', 'Artículo 70', 'órganos de Gobierno de las Administraciones Públicas')}",
         ["Recoge las necesidades **con asignación presupuestaria** que deban cubrirse con **personal de nuevo ingreso** (70.1)", "Obliga a convocar los procesos selectivos de las plazas comprometidas **y hasta un 10 % adicional**, fijando el plazo máximo para convocar (70.1)", "Se publica en el **Diario oficial** correspondiente (70.2)", "Puede contener medidas derivadas de la planificación (70.3)"],
         f"Ejecución: {c('TREBEP', 'Artículo 70', 'dentro del plazo improrrogable de tres años')}",
         "**Tres años** e **improrrogable** (cayó en 2025, → Cierre 1). Hasta un **diez por cien adicional**. Puede ser la oferta «o **instrumento similar**»."))}

{unidad("1.2 La oferta en la Administración del Estado: definición, convocatorias y plazos (RDL 6/2023, art. 108.1 y 2)",
  lit("RDL6", "Artículo 108", ["es el acto por el que definen y cuantifican los efectivos", "en el mismo año natural de la publicación", "en el plazo máximo de dos años desde su publicación, y las respectivas fases de oposición en un año, salvo causa justificada", "no hayan transcurrido más de tres años desde la publicación de la oferta"], solo=[1, 2, 3, 4]),
  fichab("Acto que define y cuantifica los efectivos según las necesidades de los departamentos y las políticas prioritarias del Gobierno",
         f"Administración del Estado; para reconvocar plazas, informe previo {c('RDL6', 'Artículo 108', 'del departamento con competencias en materia de función pública')}",
         ["Incluye las necesidades con asignación presupuestaria de **nuevo ingreso**; puede contener medidas de la planificación estratégica (108.2)", "Las plazas no cubiertas pueden convocarse de nuevo, identificando de qué convocatoria y oferta proceden; pueden asignarse a otros cuerpos o escalas, preferentemente del mismo grupo o subgrupo"],
         ["::Plazos (108.2):", "Convocatorias: publicadas en el **mismo año natural** que la oferta en el BOE", "Ejecución de las convocatorias: **2 años** desde su publicación", "Fases de oposición: **1 año**, salvo causa justificada", "Reconvocar plazas no cubiertas: si no han pasado **más de 3 años** desde la publicación de la oferta"],
         "Para la AGE: convocatoria **2 años**, oposición **1 año** (cayó en 2025, → Cierre 1). El límite de **3 años** del RDL 6/2023 cuenta desde la publicación de la **oferta** y es para **volver a convocar** plazas no cubiertas."))}

{unidad("1.3 Promoción interna y reserva para personas con discapacidad en la oferta (RDL 6/2023, art. 108.3 y 4)",
  lit("RDL6", "Artículo 108", ["no inferior al treinta por ciento de las plazas de acceso libre para promoción interna", "no inferior al diez por ciento de las plazas convocadas", "dos por ciento de los efectivos totales", "al menos el dos por ciento de las plazas ofertadas"], solo=[5, 6, 7, 8]),
  fichab("Cupos obligatorios de la oferta de la Administración del Estado",
         "Administración del Estado",
         ["**Promoción interna**: no menos del **30 %** de las plazas de acceso libre (108.3)", "**Discapacidad**: reserva de no menos del **10 %** de las plazas convocadas, para alcanzar progresivamente el **2 %** de los efectivos totales (108.4)", "Dentro del 10 %: al menos el **2 %** de las plazas ofertadas para discapacidad **intelectual** (108.4)", "La reserva se calcula sobre el total de la oferta y puede concentrarse en ciertas convocatorias (108.4)"],
         "—",
         "**30 %** para promoción interna (cayó en 2025, → Cierre 1). Discapacidad: **10 %** en la AGE (RDL 6/2023) frente al **7 %** del TREBEP (art. 59, → III.1.6). El acceso de las personas con discapacidad se estudia en el tema V.10."))}
""", 2)

T.ap("s4", "II.2 La oferta en el Reglamento General de Ingreso y cuadro de plazos (RD 364/1995, arts. 7 a 9)", f"""
{AVISO_364}

{unidad("2.1 Objeto de la oferta (RD 364/1995, art. 7)",
  lit("RD364", "Artículo 7", ["no puedan ser cubiertas con los efectivos de personal existentes", "siempre que exista crédito presupuestario"]),
  fichab("Necesidades que van a la oferta",
         "—",
         f"Las necesidades {c('RD364', 'Artículo 7', 'que no puedan ser cubiertas con los efectivos de personal existentes')}",
         "Cobertura conveniente **durante el ejercicio**",
         "Dos condiciones: **crédito presupuestario** y conveniencia de cubrirlas **en el ejercicio**."))}

{unidad("2.2 Aprobación (RD 364/1995, art. 8)",
  lit("RD364", "Artículo 8", ["por el Gobierno a propuesta del Ministro para las Administraciones Públicas con informe favorable del Ministerio de Economía y Hacienda", "en el primer trimestre de cada año", "para ámbitos administrativos específicos"]),
  fichab("Aprobación de la oferta de empleo público de la Administración General del Estado",
         f"{c('RD364', 'Artículo 8', 'el Gobierno')}, {c('RD364', 'Artículo 8', 'a propuesta del Ministro para las Administraciones Públicas con informe favorable del Ministerio de Economía y Hacienda')} (denominaciones del texto)",
         "Oferta general; y, excepcionalmente, ofertas para **ámbitos administrativos específicos** si hay necesidades urgentes (8.2)",
         c("RD364", "Artículo 8", "en el primer trimestre de cada año"),
         "La aprueba el **Gobierno** (también art. 3.2 g de la Ley 30/1984, → IV.2.1), no el Ministro ni el Secretario de Estado. Plazo: **primer trimestre**."))}

{unidad("2.3 Competencia para convocar (RD 364/1995, art. 9)",
  lit("RD364", "Artículo 9", ["los Departamentos a los que figuren adscritos los correspondientes Cuerpos y Escalas", "previo informe favorable de la Dirección General de la Función Pública"]),
  fichab("Convocatoria de los procesos selectivos tras la oferta",
         c("RD364", "Artículo 9", "los Departamentos a los que figuren adscritos los correspondientes Cuerpos y Escalas de funcionarios"),
         "Convocan los procedimientos selectivos para las vacantes previstas",
         f"Una vez {c('RD364', 'Artículo 9', 'Aprobada la oferta de empleo público')}; {c('RD364', 'Artículo 9', 'previo informe favorable de la Dirección General de la Función Pública')}",
         "Convoca el **Departamento de adscripción** del cuerpo, con informe **favorable** de la Dirección General de la Función Pública."))}

### 2.4 Cuadro de plazos de la oferta (esquema)

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Plazo o cupo | Norma | Dato |
|---|---|---|
| Ejecución de la oferta | TREBEP, art. 70.1 | **3 años**, improrrogable |
| Plazas que se pueden convocar | TREBEP, art. 70.1 | Las comprometidas **+ hasta un 10 %** |
| Aprobación de la oferta de la AGE | RD 364/1995, art. 8.1 | **Primer trimestre** de cada año, por el Gobierno |
| Publicación de las convocatorias (AGE) | RDL 6/2023, art. 108.2 | **Mismo año natural** que la oferta |
| Ejecución de las convocatorias (AGE) | RDL 6/2023, art. 108.2 | **2 años** desde su publicación; fase de oposición, **1 año** |
| Reconvocar plazas no cubiertas (AGE) | RDL 6/2023, art. 108.2 | Si no han pasado **más de 3 años** desde la oferta |
| Promoción interna (AGE) | RDL 6/2023, art. 108.3 | **≥ 30 %** de las plazas de acceso libre |
| Discapacidad | TREBEP, art. 59.1 / RDL 6/2023, art. 108.4 | **≥ 7 %** (TREBEP) / **≥ 10 %** (AGE); 2 % intelectual |

{resumen([
  "La oferta recoge las necesidades **con asignación presupuestaria** de **nuevo ingreso**; obliga a convocar las plazas **y hasta un 10 % más**; se aprueba **anualmente** y se publica en el diario oficial (TREBEP, art. 70).",
  "Ejecución: **tres años improrrogables** (TREBEP). En la AGE, convocatorias en el **mismo año** de la oferta y ejecutadas en **dos años**, con la fase de oposición en **uno** (RDL 6/2023, art. 108.2).",
  "AGE: **30 %** para promoción interna y **10 %** para personas con discapacidad (RDL 6/2023, art. 108.3 y 4).",
  "La aprueba el **Gobierno** en el **primer trimestre**; convoca el **Departamento** de adscripción del cuerpo con informe favorable de la Dirección General de la Función Pública (RD 364/1995, arts. 8 y 9)."],
  "Siguiente: III. ¿Cómo se selecciona al personal?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Cómo se selecciona al personal? (TREBEP, arts. 10.2, 11.3 y 55 a 61; RDL 6/2023, arts. 112, 114 y 115; RD 364/1995)", donde(
  "Tercera pregunta, la más extensa. Aprobada la oferta, las plazas se cubren mediante **procesos selectivos**: con qué **principios** y **requisitos** se accede, quién **selecciona**, con qué **sistemas** y cómo se tramita el **procedimiento** en la Administración General del Estado hasta el nombramiento.",
  ["1 Principios y requisitos de acceso (TREBEP, arts. 10.2, 11.3 y 55 a 59; RDL 6/2023, art. 112)", "2 Los órganos de selección (TREBEP, art. 60; RDL 6/2023, art. 115; RD 364/1995, arts. 10 a 13)", "3 Los sistemas selectivos (TREBEP, art. 61; RDL 6/2023, art. 114.1 a 9; RD 364/1995, arts. 4 y 5)", "4 El procedimiento selectivo en la AGE (RDL 6/2023, art. 114.10 a 12; RD 364/1995, arts. 3 y 15 a 26)", "5 Funcionarios interinos y personal laboral en la AGE (RD 364/1995, arts. 27 a 33)"]))

T.ap("s5", "III.1 Principios y requisitos de acceso (TREBEP, arts. 10.2, 11.3 y 55 a 59; RDL 6/2023, art. 112)", f"""
{unidad("1.1 Procedimientos públicos también para interinos y personal laboral (TREBEP, arts. 10.2 y 11.3)",
  lit("TREBEP", "Artículo 10", ["Los procedimientos de selección del personal funcionario interino serán públicos", "igualdad, mérito, capacidad, publicidad y celeridad"], solo=[6]),
  lit("TREBEP", "Artículo 11", ["Los procedimientos de selección del personal laboral serán públicos", "principio de celeridad"], solo=[3]),
  fichab("Publicidad de la selección del personal temporal y laboral",
         "Funcionarios interinos y personal laboral (fijo y temporal)",
         ["Interinos: igualdad, mérito, capacidad, publicidad y **celeridad**; finalidad, la cobertura inmediata del puesto (10.2)", "Laborales: igualdad, mérito y capacidad; los **temporales**, además, celeridad (11.3)"],
         "—",
         f"La selección es **pública** para funcionarios de carrera, interinos y laborales (cayó en 2025, → Cierre 1). El personal **eventual** no se selecciona así: {c('TREBEP', 'Artículo 12', 'El nombramiento y cese serán libres')} (art. 12.3; tema V.1). El nombramiento de interino nunca da la condición de funcionario de carrera."))}

{unidad("1.2 Principios rectores (TREBEP, art. 55)",
  lit("TREBEP", "Artículo 55", ["igualdad, mérito y capacidad", "seleccionarán a su personal funcionario y laboral", "Publicidad de las convocatorias y de sus bases", "Transparencia", "Imparcialidad y profesionalidad", "Independencia y discrecionalidad técnica", "Adecuación entre el contenido de los procesos selectivos y las funciones o tareas a desarrollar", "Agilidad, sin perjuicio de la objetividad"]),
  ficha(c("TREBEP", "Artículo 55", "Todos los ciudadanos"),
        ["::Derecho de acceso al empleo público según los principios constitucionales de **igualdad, mérito y capacidad** (55.1). Además (55.2):", "a) Publicidad de las convocatorias y de sus bases", "b) Transparencia", "c) Imparcialidad y profesionalidad de los miembros de los órganos de selección", "d) Independencia y discrecionalidad técnica de los órganos de selección", "e) Adecuación entre el contenido de los procesos y las funciones o tareas", "f) Agilidad, sin perjuicio de la objetividad"],
        "De acuerdo con el TREBEP y el resto del ordenamiento jurídico (55.1)",
        "Las Administraciones seleccionan a su personal **funcionario y laboral** mediante procedimientos que garanticen estos principios (55.2)",
        "Son **seis** principios del 55.2, que se suman a los constitucionales. La **imparcialidad y profesionalidad** son de los **miembros**; la **independencia y discrecionalidad técnica**, de la **actuación** de los órganos de selección."))}

{unidad("1.3 Requisitos generales (TREBEP, art. 56)",
  lit("TREBEP", "Artículo 56", ["Tener la nacionalidad española", "Poseer la capacidad funcional", "Tener cumplidos dieciséis años", "Sólo por ley podrá establecerse otra edad máxima", "No haber sido separado mediante expediente disciplinario", "Poseer la titulación exigida", "dos lenguas oficiales", "relación objetiva y proporcionada", "de manera abstracta y general"]),
  ficha("Quienes quieran participar en los procesos selectivos",
        ["a) Nacionalidad española (salvo el art. 57)", "b) Capacidad funcional para las tareas", "c) **Dieciséis años** cumplidos y no exceder, en su caso, la edad máxima de jubilación forzosa", "d) No haber sido separado por expediente disciplinario ni estar inhabilitado", "e) Titulación exigida"],
        f"Requisitos específicos solo si guardan {c('TREBEP', 'Artículo 56', 'relación objetiva y proporcionada con las funciones asumidas y las tareas a desempeñar')}, fijados {c('TREBEP', 'Artículo 56', 'de manera abstracta y general')} (56.3)",
        "Las Administraciones prevén personal capacitado para las Comunidades Autónomas con **dos lenguas oficiales** (56.2)",
        "**16 años**, no 18. Otra edad máxima distinta de la de jubilación forzosa: **sólo por ley**."))}

{unidad("1.4 Nacionales de otros Estados (TREBEP, art. 57)",
  lit("TREBEP", "Artículo 57", ["en igualdad de condiciones que los españoles a los empleos públicos", "participación en el ejercicio del poder público", "menores de veintiún años o mayores de dicha edad dependientes", "extranjeros con residencia legal en España podrán acceder a las Administraciones Públicas, como personal laboral", "Sólo por ley de las Cortes Generales o de las asambleas legislativas de las comunidades autónomas"]),
  ficha(["Nacionales de Estados miembros de la UE (como **funcionarios**)", "Cónyuges no separados de derecho, y descendientes menores de 21 años o mayores dependientes (57.2)", "Personas incluidas en tratados de la UE sobre libre circulación de trabajadores (57.3)", "Extranjeros con residencia legal (solo como **personal laboral**, 57.4)"],
        "Acceso en igualdad de condiciones que los españoles",
        [f"Excluidos los empleos que impliquen {c('TREBEP', 'Artículo 57', 'participación en el ejercicio del poder público')} o la salvaguardia de los intereses del Estado; los órganos de gobierno determinan esas agrupaciones (57.1)", "Eximir del requisito de nacionalidad para ser funcionario: solo por **ley** de las Cortes o de las asambleas autonómicas (57.5)"],
        "—",
        "Los extranjeros con residencia legal acceden como **laborales**, no como funcionarios. Descendientes: menores de **21** años o mayores dependientes."))}

{unidad("1.5 Funcionarios españoles de Organismos Internacionales (TREBEP, art. 58)",
  lit("TREBEP", "Artículo 58", ["siempre que posean la titulación requerida y superen los correspondientes procesos selectivos", "Podrán quedar exentos"]),
  ficha("Funcionarios de nacionalidad española de Organismos Internacionales",
        ["Acceso con los requisitos y condiciones que fije cada Administración", "Posible exención de las pruebas sobre conocimientos ya exigidos en su puesto internacional"],
        "Deben tener la titulación y superar el proceso selectivo",
        "—",
        "No hay acceso directo: **superan el proceso selectivo**, aunque puedan quedar exentos de algunas pruebas."))}

{unidad("1.6 Personas con discapacidad (TREBEP, art. 59)",
  lit("TREBEP", "Artículo 59", ["no inferior al siete por ciento de las vacantes", "dos por ciento de los efectivos totales", "discapacidad intelectual", "adaptaciones y ajustes razonables de tiempos y medios"]),
  ficha("Personas con discapacidad (art. 4.2 del texto refundido de la Ley General de derechos de las personas con discapacidad)",
        ["Cupo de reserva en las ofertas: **no inferior al 7 %** de las vacantes (59.1)", "De ese mínimo, **al menos el 2 %** de las plazas ofertadas para discapacidad **intelectual** (59.1)"],
        "Deben superar los procesos selectivos y acreditar la discapacidad y la compatibilidad con las tareas",
        "Adaptaciones y ajustes razonables de tiempos y medios en el proceso y adaptaciones en el puesto (59.2)",
        "TREBEP **7 %**; en la AGE, el RDL 6/2023 eleva la reserva al **10 %** (→ II.1.3). El desarrollo se estudia en el tema V.10."))}

{unidad("1.7 Principios rectores del acceso en la Administración del Estado (RDL 6/2023, art. 112)",
  lit("RDL6", "Artículo 112", ["adaptable", "mixto", "social", "planificación y seguimiento de los procesos selectivos", "promoviendo el uso de medios electrónicos", "La accesibilidad", "independencia, discrecionalidad técnica y confidencialidad", "con independencia de la situación socioeconómica"]),
  ficha("Personas aspirantes al empleo público de la Administración del Estado",
        ["::Modelo de selección **adaptable, mixto** (conocimientos y competencias) y **social** (112.1). Garantías (112.2):", "a) Publicidad de convocatorias y bases, y de la planificación y seguimiento de los procesos; transparencia", "b) Adecuación del contenido a las funciones, valoradas por competencias profesionales", "c) Agilidad y eficiencia, con medios electrónicos", "d) Accesibilidad", "e) Imparcialidad y profesionalidad de los miembros; independencia, discrecionalidad técnica y **confidencialidad** de su actuación", "f) Igualdad de acceso con independencia de la situación socioeconómica"],
        "Los principios de igualdad, mérito y capacidad y los del art. 55 del TREBEP (112.1)",
        "—",
        "El RDL 6/2023 añade, frente al art. 55 TREBEP, la **confidencialidad**, la **accesibilidad** y la igualdad con independencia de la **situación socioeconómica**."))}
""", 2)

T.ap("s6", "III.2 Los órganos de selección (TREBEP, art. 60; RDL 6/2023, art. 115; RD 364/1995, arts. 10 a 13)", f"""
{unidad("2.1 Composición y exclusiones (TREBEP, art. 60)",
  lit("TREBEP", "Artículo 60", ["serán colegiados", "imparcialidad y profesionalidad", "paridad entre mujer y hombre", "El personal de elección o de designación política, los funcionarios interinos y el personal eventual", "siempre a título individual"]),
  fichab("Órganos que desarrollan y califican los procesos selectivos",
         ["::Pueden formar parte: quienes no estén excluidos. **No** pueden (60.2):", "Personal de elección o de designación política", "Funcionarios interinos", "Personal eventual"],
         ["Órganos **colegiados** (60.1)", "Composición según imparcialidad y profesionalidad; se tiende a la **paridad** entre mujer y hombre (60.1)", "Pertenencia **a título individual**, nunca en representación o por cuenta de nadie (60.3)"],
         "—",
         "Tres exclusiones en el TREBEP: **políticos**, **interinos** y **eventuales**. La paridad es una tendencia («se tenderá»)."))}

{unidad("2.2 Los órganos de selección en la Administración del Estado (RDL 6/2023, art. 115)",
  lit("RDL6", "Artículo 115", ["como órganos colegiados", "presencia equilibrada entre mujeres y hombres", "alto cargo", "el personal laboral no fijo", "a título individual", "órganos o comités especializados, permanentes y renovables", "El Instituto Nacional de Administración Pública"]),
  fichab("Órganos de selección de la Administración del Estado",
         ["::**No** pueden formar parte (115.2):", "Altos cargos (Ley 3/2015)", "Personal de elección o designación política", "Personal funcionario interino", "Personal laboral **no fijo**", "Personal eventual"],
         ["Actúan con sujeción a las Leyes 39/2015 y 40/2015 (115.1)", "Imparcialidad, profesionalidad y especialización; agilidad y celeridad; **presencia equilibrada** entre mujeres y hombres; se promueve la participación de personas con discapacidad (115.2)", "Pertenencia a título individual (115.3)", "Pueden crearse órganos o comités especializados, permanentes y renovables (115.4)", "Formación de sus miembros por el INAP y otros centros; se valora al conformarlos (115.5)"],
         "—",
         "Frente al TREBEP, el RDL 6/2023 excluye también a los **altos cargos** y al **personal laboral no fijo**, y exige **presencia equilibrada** (no solo «se tenderá, asimismo, a la paridad entre mujer y hombre»)."))}

{AVISO_364}

{unidad("2.3 Tribunales y Comisiones Permanentes de Selección (RD 364/1995, arts. 10 a 12)",
  lit("RD364", "Artículo 10", ["los Tribunales y las Comisiones Permanentes de Selección"]),
  lit("RD364", "Artículo 11", ["en cada orden de convocatoria", "número impar de miembros, funcionarios de carrera, no inferior a cinco", "el mismo número de miembros suplentes", "nivel de titulación igual o superior"]),
  lit("RD364", "Artículo 12", ["el elevado número de aspirantes", "por Orden del Ministerio para las Administraciones Públicas"]),
  fichab("Las dos clases de órganos de selección de la AGE",
         ["**Tribunales**: nombrados en cada orden de convocatoria (salvo excepción justificada)", "**Comisiones Permanentes de Selección**: para cuerpos con elevado número de aspirantes y nivel de titulación o especialización que lo aconseje; se crean por Orden ministerial (12.2); número **impar** de miembros, funcionarios de carrera con titulación igual o superior, designados libremente según la Orden de creación (12.3)"],
         ["Tribunal: número **impar** de miembros, **funcionarios de carrera**, **no inferior a cinco**, con igual número de suplentes", "Todos con titulación **igual o superior** a la exigida para el ingreso", "Se vela por el principio de especialidad"],
         "Tribunal: mínimo **cinco** miembros, número impar",
         "Impar y **no inferior a cinco**; mismo número de **suplentes**; todos **funcionarios de carrera**."))}

{unidad("2.4 Reglas adicionales de composición y funcionamiento (RD 364/1995, art. 13.1 a 3)",
  lit("RD364", "Artículo 13", ["mayoritariamente por funcionarios pertenecientes al mismo Cuerpo o Escala", "en los cinco años anteriores", "asesores especialistas"], solo=[1, 2, 3]),
  fichab("Limitaciones para formar parte de los órganos de selección",
         ["No pueden formarlos **mayoritariamente** funcionarios del mismo Cuerpo o Escala que se selecciona (13.1)", "No pueden formar parte quienes hayan preparado aspirantes en los **cinco años** anteriores a la convocatoria (13.2)", "Pueden incorporar **asesores especialistas**, que colaboran solo en sus especialidades técnicas (13.3)"],
         "—",
         "Preparación de aspirantes: **cinco años** anteriores a la publicación de la convocatoria",
         "«mayoritariamente» del mismo cuerpo: lo prohibido es la **mayoría**, no que haya alguno. Preparadores: **5 años**."))}
""", 2)

T.ap("s7", "III.3 Los sistemas selectivos (TREBEP, art. 61; RDL 6/2023, art. 114.1 a 9; RD 364/1995, arts. 4 y 5)", f"""
{unidad("3.1 Carácter abierto, pruebas y valoración de méritos (TREBEP, art. 61.1 a 5)",
  lit("TREBEP", "Artículo 61", ["carácter abierto y garantizarán la libre concurrencia", "igualdad de oportunidades entre sexos", "la conexión entre el tipo de pruebas a superar", "puntuación proporcionada que no determinará, en ningún caso, por sí misma el resultado", "órganos especializados y permanentes", "pruebas psicotécnicas"], solo=[1, 2, 3, 4, 5, 6, 7]),
  fichab("Reglas comunes de los procesos selectivos",
         "Las Administraciones Públicas y sus órganos de selección; pueden encomendar la organización a Institutos o Escuelas de Administración Pública (61.4)",
         ["Procesos **abiertos** y de **libre concurrencia**, salvo promoción interna y medidas de discriminación positiva (61.1)", "Conexión entre las pruebas y las tareas de los puestos; pruebas prácticas si son precisas (61.2)", "Pruebas: conocimientos y capacidad analítica (oral o escrita), habilidades y destrezas, lenguas extranjeras y, en su caso, pruebas físicas (61.2)", "Pueden completarse con cursos, prácticas, exposición curricular, psicotécnicos o entrevistas; y reconocimientos médicos (61.5)"],
         "Méritos: puntuación **proporcionada**, que **nunca** determina por sí misma el resultado (61.3)",
         "La valoración de méritos «no determinará, **en ningún caso**, por sí misma el resultado»."))}

{unidad("3.2 Sistemas de funcionarios de carrera y de personal laboral fijo; aprobados y plazas (TREBEP, art. 61.6 a 8)",
  lit("TREBEP", "Artículo 61", ["Los sistemas selectivos de funcionarios de carrera serán los de oposición y concurso-oposición", "Sólo en virtud de ley podrá aplicarse, con carácter excepcional, el sistema de concurso", "Los sistemas selectivos de personal laboral fijo serán los de oposición, concurso-oposición", "o concurso de valoración de méritos", "excepto cuando así lo prevea la propia convocatoria", "relación complementaria"], solo=[8, 9, 10, 11, 12, 13]),
  fichab("Sistemas selectivos según la clase de personal",
         ["Funcionarios de carrera: **oposición** y **concurso-oposición**; **concurso** solo por **ley** y con carácter **excepcional** (61.6)", "Personal laboral fijo: **oposición**, **concurso-oposición** o **concurso de valoración de méritos** (61.7)"],
         ["No se pueden proponer **más aprobados que plazas**, salvo que lo prevea la convocatoria (61.8)", "Si hay renuncias antes del nombramiento o la toma de posesión, el órgano convocante puede pedir una **relación complementaria** (61.8)", "Las Administraciones pueden negociar la colaboración de las organizaciones sindicales en los procesos de personal laboral (61.7)"],
         "—",
         "Laboral fijo: **tres** sistemas, incluido el concurso de méritos (cayó en 2025, → Cierre 1). Funcionarios: el concurso exige **ley** y es **excepcional**."))}

{unidad("3.3 Los procesos de selección en la Administración del Estado (RDL 6/2023, art. 114.1 a 3)",
  lit("RDL6", "Artículo 114", ["de forma territorializada", "territorios no peninsulares", "ejercicios teóricos y prácticos", "exposición curricular", "se deberá justificar la selección de unos u otros tipos de pruebas"], solo=[1, 2, 3, 4, 5, 6, 7]),
  fichab("Diseño de los procesos selectivos de la Administración del Estado",
         "Administración del Estado (órgano convocante)",
         ["Abiertos y de libre concurrencia, con los principios del art. 112 (114.1)", "Pruebas **territorializadas**, salvo razones justificadas, atendiendo a los territorios no peninsulares (114.2)", "Conocimientos, habilidades y competencias, con ejercicios **teóricos y prácticos**, orales o escritos; posibles pruebas físicas, de idiomas o de TIC (114.3)", "Si lo requieren los cometidos: exposición curricular, psicotécnicos, psicométricos, entrevistas; reconocimientos médicos (114.3)"],
         "—",
         "La convocatoria **debe justificar** el tipo de pruebas elegido (114.3)."))}

{unidad("3.4 Oposición, concurso, concurso-oposición y curso selectivo (RDL 6/2023, art. 114.4 a 9)",
  lit("RDL6", "Artículo 114", ["oposición, concurso-oposición y, excepcionalmente, el de concurso", "fijar su orden de prelación", "consiste exclusivamente en la valoración de los méritos", "cuando así se establezca por ley", "Para la valoración de la fase de concurso será necesario haber superado la fase de oposición", "personal funcionario en prácticas"], solo=[8, 9, 10, 11, 12, 13, 14, 15]),
  fichab("Los sistemas selectivos en la Administración del Estado",
         "Órganos de selección; organizaciones sindicales en el marco de los convenios para el personal laboral (114.9)",
         ["**Oposición**: una o más pruebas de conocimientos, competencias o habilidades para determinar la capacidad y fijar el orden de prelación (114.5)", "**Concurso**: **exclusivamente** valoración de méritos conforme a baremo; para funcionarios, solo **excepcionalmente** y **por ley** (114.6)", "**Concurso-oposición**: sucesión de ambos; fase de concurso **proporcionada**; para valorarla hay que **haber superado la oposición** (114.7)", "**Curso selectivo** (funcionarios de carrera): periodo formativo o de prácticas evaluable; el aspirante es **funcionario en prácticas** (114.8)"],
         "—",
         "En el concurso-oposición de la AGE, la fase de concurso **solo se valora a quien supera la oposición**."))}

{unidad("3.5 Sistemas y pruebas en el Reglamento General de Ingreso (RD 364/1995, arts. 4 y 5)",
  lit("RD364", "Artículo 4", ["La oposición será el sistema ordinario de ingreso", "excepcionalmente, del concurso", "la sucesiva celebración de los dos sistemas anteriores"]),
  lit("RD364", "Artículo 5", ["al menos uno deberá tener carácter práctico"]),
  fichab("Sistemas de ingreso del personal funcionario de la AGE",
         "—",
         ["Oposición, concurso-oposición o concurso **libres**, con igualdad, mérito, capacidad y publicidad (4.1)", "Pruebas de conocimientos generales o específicos; pueden incluir test psicotécnicos, entrevistas y otros sistemas objetivos (5.2)"],
         "—",
         f"{c('RD364', 'Artículo 4', 'La oposición será el sistema ordinario de ingreso')}. Si hay varios ejercicios, **al menos uno práctico**, salvo excepciones justificadas (5.2). El concurso para funcionarios requiere hoy **ley** (TREBEP, art. 61.6, → III.3.2)."))}
""", 2)

T.ap("s8", "III.4 El procedimiento selectivo en la AGE (RDL 6/2023, art. 114.10 a 12; RD 364/1995, arts. 3 y 15 a 26)", f"""
{unidad("4.1 Aprobados, bases mínimas y toma de posesión (RDL 6/2023, art. 114.10 a 12)",
  lit("RDL6", "Artículo 114", ["un número superior de personas aprobadas al de plazas convocadas, excepto cuando así lo prevea la propia convocatoria", "relación complementaria", "antes de la de toma de posesión", "relaciones de posibles personas candidatas", "Las bases de la convocatoria vincularán", "El porcentaje de plazas reservadas", "dentro del plazo de quince días naturales a partir de la publicación del nombramiento, que será de un mes cuando suponga cambio de localidad de residencia", "al día siguiente al del nombramiento"], solo=[16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),
  fichab("Del final del proceso a la toma de posesión en la Administración del Estado",
         "Órgano convocante y órganos de selección; el departamento de función pública puede elaborar un **modelo de bases comunes** (114.11)",
         ["No más aprobados que plazas, salvo previsión de la convocatoria; **relación complementaria** si hay renuncias y se propusieron tantos como plazas (114.10)", "El órgano de selección elabora **relaciones de posibles candidatos** a interinos o laborales temporales (114.10)", "**Convocatoria pública con bases** que vinculan a convocante, órganos de selección y participantes; contenido mínimo: plazas y oferta, requisitos, sistema y programa, órgano de selección, curso selectivo, cupos de reserva (114.11)"],
         ["::Toma de posesión (114.12):", "Funcionario de carrera: **15 días naturales** desde la publicación del nombramiento; **un mes** si cambia de localidad de residencia", "Interino y eventual: **al día siguiente** del nombramiento"],
         "**15 días naturales** / **1 mes** con cambio de localidad. La relación complementaria se pide **antes de la toma de posesión**."))}

{AVISO_364}

{unidad("4.2 Régimen y publicación de las convocatorias (RD 364/1995, arts. 3 y 15)",
  lit("RD364", "Artículo 3", ["mediante convocatoria pública"]),
  lit("RD364", "Artículo 15", ["se publicarán en el «Boletín Oficial del Estado»", "de carácter unitario", "bases generales", "vinculan a la Administración y a los Tribunales", "solamente podrán ser modificadas"]),
  fichab("La convocatoria como ley del proceso selectivo",
         "El Departamento convocante; bases generales con informe favorable de la Dirección General de la Función Pública (15.3)",
         ["Ingreso mediante **convocatoria pública**, regido por sus bases (art. 3)", "Convocatoria y bases se publican en el **BOE** (15.1)", "Convocatorias **unitarias** o para cuerpos o escalas determinados (15.2)", "Las bases **vinculan** a la Administración, a los órganos de selección y a los participantes (15.4)"],
         "—",
         "Publicadas, las bases solo se modifican con sujeción estricta a la ley de procedimiento (15.5)."))}

{unidad("4.3 Contenido mínimo de las convocatorias (RD 364/1995, art. 16)",
  lit("RD364", "Artículo 16", ["Número y características de las plazas convocadas", "no se podrá declarar superado el proceso selectivo a un número de aspirantes superior al de plazas convocadas", "un plazo mínimo de setenta y dos horas y máximo de cuarenta y cinco días naturales"]),
  fichab("Lo que toda convocatoria debe contener",
         "Órgano convocante",
         "Plazas, declaración de no superar el número de plazas, órgano de solicitudes, requisitos, sistema selectivo, pruebas y méritos, órgano de selección, calificación, programa, duración máxima, orden de actuación, prácticas o curso selectivo (letras a a l)",
         ["::Entre ejercicios (16 j):", "Mínimo **72 horas**", "Máximo **45 días naturales**"],
         "Entre un ejercicio y el siguiente: **72 horas** como mínimo y **45 días naturales** como máximo."))}

{unidad("4.4 Orden de actuación y solicitudes (RD 364/1995, arts. 17 y 18)",
  lit("RD364", "Artículo 17", ["mediante un único sorteo público"]),
  lit("RD364", "Artículo 18", ["en el plazo de veinte días naturales", "bastará con que los aspirantes manifiesten en sus solicitudes", "referidas siempre a la fecha de expiración del plazo de presentación"]),
  fichab("Antes de las pruebas: sorteo y solicitudes",
         "Sorteo: **Secretaría de Estado para la Administración Pública** (según el texto); modelo oficial de solicitud aprobado por esa misma Secretaría de Estado",
         ["Un **único sorteo público** anual, previo anuncio en el BOE, fija el orden de actuación en todas las pruebas de ingreso del año (17)", "Para ser admitido basta **manifestar** en la solicitud que se reúnen las condiciones (18.2)"],
         f"Solicitudes: {c('RD364', 'Artículo 18', 'en el plazo de veinte días naturales a partir del siguiente al de publicación de la convocatoria')} en el BOE",
         "**20 días naturales**. Los requisitos se cumplen a la **fecha de expiración del plazo** de solicitudes."))}

{unidad("4.5 Listas de admitidos y anuncios de las pruebas (RD 364/1995, arts. 20 y 21)",
  lit("RD364", "Artículo 20", ["en el plazo máximo de un mes", "un plazo de diez días hábiles para subsanación"], solo=[1]),
  lit("RD364", "Artículo 21", ["no será obligatoria la publicación", "con doce horas, al menos, de antelación", "de veinticuatro horas, si se trata de uno nuevo"]),
  fichab("Admisión y calendario de las pruebas",
         "La autoridad convocante (listas); el órgano de selección (anuncios)",
         ["Resolución de admitidos y excluidos, publicada en el BOE, con lugar y fecha del primer ejercicio (20.1)", "Iniciado el proceso, los anuncios siguientes no tienen que ir al BOE: se publican en los locales de la prueba anterior (21)"],
         ["Lista: máximo **un mes** desde que expira el plazo de solicitudes", "Subsanación: **10 días hábiles**", "Anuncios: **12 horas** (mismo ejercicio) o **24 horas** (ejercicio nuevo) de antelación"],
         "Subsanación en días **hábiles** (10), solicitudes en días **naturales** (20)."))}

{unidad("4.6 Relación de aprobados y documentación (RD 364/1995, arts. 22 y 23)",
  lit("RD364", "Artículo 22", ["por orden de puntuación", "deberán ser motivados", "Sólo en el primer caso"]),
  lit("RD364", "Artículo 23", ["dentro del plazo de veinte días naturales", "no podrán ser nombrados", "estarán exentos de justificar las condiciones y requisitos ya acreditados"]),
  fichab("Cierre de la fase de pruebas",
         "Los Tribunales o Comisiones Permanentes publican la relación; la autoridad competente la publica en el BOE (22.1)",
         ["Actos que ponen fin al proceso: **motivados**; en la discrecionalidad técnica, la motivación se refiere a las normas y bases (22.2)", "Quien no presenta los documentos o no reúne los requisitos **no puede ser nombrado** (23.2)", "Los ya funcionarios solo acreditan con certificación lo no justificado antes (23.3)"],
         "Documentación: **20 días naturales** desde la publicación en el BOE de las relaciones definitivas de aprobados (23.1)",
         "Según el art. 22.3 del reglamento, solo con **curso selectivo** puede haber más aprobados que plazas en las pruebas; el RDL 6/2023 permite superar el número si lo prevé la convocatoria (→ III.4.1)."))}

{unidad("4.7 Prácticas, nombramiento y primer destino (RD 364/1995, arts. 24 a 26)",
  lit("RD364", "Artículo 24", ["nombrará funcionarios en prácticas", "perderán el derecho a su nombramiento como funcionarios de carrera"], solo=[1, 2]),
  lit("RD364", "Artículo 25", ["serán nombrados funcionarios de carrera por el Secretario de Estado para la Administración Pública", "nula de pleno derecho"]),
  lit("RD364", "Artículo 26", ["según el orden obtenido en el proceso selectivo", "carácter definitivo"], solo=[1, 2]),
  fichab("Del aprobado al funcionario de carrera",
         ["Funcionarios en prácticas: los nombra **la autoridad convocante** (24.1)", f"Funcionarios de carrera: {c('RD364', 'Artículo 25', 'el Secretario de Estado para la Administración Pública')} (25.1)"],
         ["Quien no supera el curso selectivo pierde el derecho al nombramiento, por resolución **motivada** (24.1)", "Nombramientos publicados en el **BOE** (25.2)", "Primer destino según las peticiones y el **orden** obtenido en el proceso (26.1)"],
         "—",
         "Nombra **el Secretario de Estado** (no el Ministro ni el Subsecretario; también art. 6.3 del RD 2169/1984, → IV.3.2). Nombrar más que plazas: **nulo de pleno derecho**. El primer destino es **definitivo**, equivalente al obtenido por concurso. La adquisición de la condición de funcionario se estudia en el tema V.1."))}
""", 2)

T.ap("s9", "III.5 Funcionarios interinos y personal laboral en la AGE (RD 364/1995, arts. 27 a 33)", f"""
{AVISO_364}

{unidad("5.1 Selección y nombramiento de funcionarios interinos (RD 364/1995, art. 27)",
  lit("RD364", "Artículo 27", ["por el Subsecretario del Departamento", "máxima agilidad", "requisitos generales de titulación", "aplicación supletoria"]),
  fichab("Nombramiento de personal funcionario interino",
         f"{c('RD364', 'Artículo 27', 'el Subsecretario del Departamento al que figuren adscritos los correspondientes Cuerpos y Escalas')}, o el Director general de la Función Pública para los cuerpos dependientes de la Secretaría de Estado",
         ["Principios de **mérito y capacidad** y máxima **agilidad** (27.1)", "Mismos requisitos de titulación y condiciones que los funcionarios de carrera (27.2)", "Normas de selección de funcionarios de carrera: **supletorias** (27.3)"],
         "—",
         "Al interino lo nombra el **Subsecretario**; al de carrera, el **Secretario de Estado** (→ III.4.7). La selección de interinos es pública (TREBEP, art. 10.2, → III.1.1)."))}

{unidad("5.2 Personal laboral fijo: convocatoria, sistemas, órganos de selección y solicitudes (RD 364/1995, arts. 28 a 31)",
  lit("RD364", "Artículo 28", ["previo informe favorable de la Dirección General de la Función Pública", "se regirá por sus convenios colectivos"]),
  lit("RD364", "Artículo 29", ["Los sistemas selectivos serán la oposición, el concurso-oposición y el concurso"]),
  lit("RD364", "Artículo 30", ["se constituirán en cada convocatoria", "designado a propuesta de la representación de los trabajadores"]),
  lit("RD364", "Artículo 31", ["En el plazo máximo de un mes"]),
  fichab("Selección del personal laboral fijo de nuevo ingreso",
         f"Convocan {c('RD364', 'Artículo 28', 'Los Departamentos ministeriales')}, con informe favorable de la Dirección General de la Función Pública",
         ["De acuerdo con la oferta de empleo público (28.1)", "Promoción interna y vacantes de quien no es de nuevo ingreso: por **convenio colectivo** o normativa específica (28.2)", "Convocatorias según el título I y los criterios generales de selección; en el BOE se anuncian, al menos, las plazas por categorías y el lugar de las bases (29)", "Sistemas: oposición, concurso-oposición y concurso (29)"],
         ["Órgano de selección: número **impar**, **al menos uno** a propuesta de la representación de los trabajadores (30)", "Solicitud en el modelo oficial; fecha, lugar y hora de las pruebas en el BOE en el plazo máximo de **un mes** desde que termina el plazo de instancias (31)"],
         "En el laboral, el órgano de selección tiene **al menos un miembro** propuesto por los **trabajadores**. Los tres sistemas coinciden con el art. 61.7 del TREBEP (→ III.3.2). El régimen del personal laboral se estudia en el tema V.7."))}

{unidad("5.3 Propuesta de aprobados y adquisición de la condición de laboral fijo (RD 364/1995, arts. 32 y 33)",
  lit("RD364", "Artículo 32", ["en ningún caso podrá exceder del número de plazas convocadas", "nula de pleno derecho"]),
  lit("RD364", "Artículo 33", ["no tendrán derecho a percepción económica alguna", "Transcurrido el período de prueba"]),
  fichab("Del aprobado al contrato fijo",
         "El órgano competente formaliza los contratos (33.1)",
         ["Propuesta de candidatos sin exceder las plazas convocadas; si las excede, **nula de pleno derecho** (32)", "Contrato previa justificación de capacidad y requisitos; sin retribución hasta la formalización e incorporación (33.1)"],
         "Condición de **laboral fijo**: al superar el **período de prueba** fijado en la convocatoria (33.2)",
         "El laboral **fijo** se adquiere tras el **período de prueba**, no con la firma del contrato."))}

{resumen([
  "Selección **pública** para funcionarios de carrera, **interinos** y **laborales**; el eventual es de libre nombramiento (TREBEP, arts. 10.2, 11.3, 12.3 y 55).",
  "Principios: igualdad, mérito y capacidad + **seis** del art. 55.2; requisitos del art. 56 (**16 años**, nacionalidad salvo art. 57, titulación…).",
  "Órganos de selección **colegiados**, a **título individual**, sin políticos, interinos ni eventuales (TREBEP); en la AGE tampoco **altos cargos** ni **laborales no fijos** (RDL 6/2023). Tribunal: impar, **mínimo cinco**, funcionarios de carrera (RD 364/1995).",
  "Funcionarios: **oposición** y **concurso-oposición**; concurso solo por **ley**. Laboral fijo: oposición, concurso-oposición o **concurso de valoración de méritos** (TREBEP, art. 61).",
  "AGE: solicitudes en **20 días naturales**; subsanación **10 días hábiles**; documentación **20 días naturales**; nombra el **Secretario de Estado**; toma de posesión **15 días naturales** (un mes con cambio de localidad)."],
  "Siguiente: IV. ¿Quién tiene las competencias en materia de personal?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Quién tiene las competencias en materia de personal? (TREBEP, art. 100; Ley 30/1984; RD 2169/1984)", donde(
  "Cuarta pregunta. Ya hemos visto que el Gobierno **aprueba** la oferta, los Departamentos **convocan** y el Secretario de Estado **nombra**. Este bloque ordena **quién decide qué** en materia de personal: primero la cooperación entre Administraciones; después, en la Administración del Estado, los órganos de la Ley 30/1984 y el reparto detallado del Real Decreto 2169/1984.",
  ["1 Cooperación entre Administraciones (TREBEP, art. 100)", "2 Órganos superiores de la función pública del Estado (Ley 30/1984, arts. 3, 4, 5 y 9)", "3 El reparto de competencias: Gobierno, Ministros, Secretario de Estado y Director general de la Función Pública (RD 2169/1984, arts. 3, 5, 6 y 7)", "4 Departamentos, Ministros, Subsecretarios y personal laboral y eventual (RD 2169/1984, arts. 8 a 13) y cuadro"]))

T.ap("s10", "IV.1 Cooperación entre Administraciones (TREBEP, art. 100)", f"""
{unidad("1.1 Conferencia Sectorial de Administración Pública y Comisión de Coordinación del Empleo Público (TREBEP, art. 100)",
  lit("TREBEP", "Artículo 100", ["La Conferencia Sectorial de Administración Pública", "Se crea la Comisión de Coordinación del Empleo Público como órgano técnico y de trabajo dependiente de la Conferencia Sectorial de Administración Pública", "efectividad de los principios constitucionales en el acceso al empleo público", "elaborará sus propias normas de organización y funcionamiento"]),
  fichab("Órganos de cooperación en materia de administración pública y de empleo público",
         ["**Conferencia Sectorial de Administración Pública**: AGE, Comunidades Autónomas, Ceuta y Melilla y Administración Local (representantes designados por la FEMP) (100.1)", "**Comisión de Coordinación del Empleo Público**: titulares de los órganos directivos de recursos humanos de esas Administraciones y representantes locales designados por la FEMP (100.3)"],
         ["::La Comisión coordina la política de personal entre Administraciones y le corresponde (100.2):", "a) Impulsar la efectividad de los principios constitucionales en el **acceso** al empleo público", "b) Estudiar los proyectos de legislación básica de empleo público e informar otros proyectos normativos", "c) Elaborar estudios e informes, que se remiten a los sindicatos de la Mesa General de Negociación de las Administraciones Públicas"],
         "—",
         "La Comisión de Coordinación del Empleo Público es un órgano **técnico y de trabajo** que **depende de la Conferencia Sectorial**. Elabora sus propias normas de funcionamiento (100.4)."))}
""", 2)

T.ap("s11", "IV.2 Órganos superiores de la función pública del Estado (Ley 30/1984, arts. 3, 4, 5 y 9)", f"""
Preceptos de la Ley 30/1984 que **no** están en la lista de la disposición derogatoria única del TREBEP (las letras e y f del art. 3.2 sí están en ella y no se citan). Las denominaciones de los Ministerios son las del texto consolidado del BOE.

{unidad("2.1 El Gobierno (Ley 30/1984, art. 3)",
  lit("L30", "Artículo tres", ["dirige la política de personal", "potestad reglamentaria", "Aprobar la oferta de empleo de la Administración del Estado", "estructura en grados"], solo=[1, 2, 3, 4, 5, 6, 9, 10, 11]),
  fichab("Dirección de la política de personal y potestad reglamentaria en función pública de la Administración del Estado",
         c("L30", "Artículo tres", "El Gobierno"),
         ["a) Directrices para el ejercicio de las competencias de personal de los órganos del Estado", "b) Instrucciones para negociar con la representación sindical de los funcionarios y aprobación expresa y formal de los Acuerdos", "c) Instrucciones para la negociación colectiva con el personal laboral", "d) Normas y directrices anuales del régimen retributivo", "g) **Aprobar la oferta de empleo** de la Administración del Estado", "h) Estructura en grados, intervalos de niveles por Cuerpo o Escala y criterios generales de promoción profesional"],
         "—",
         "Quien **aprueba** la oferta de empleo del Estado es el **Gobierno** (3.2 g; también RD 364/1995, art. 8, → II.2.2). Ejerce la **función ejecutiva** y la **potestad reglamentaria** en función pública."))}

{unidad("2.2 El Ministro de la Presidencia (Ley 30/1984, art. 4)",
  lit("L30", "Artículo cuatro", ["el desarrollo general, la coordinación y el control de la ejecución de la política del Gobierno en materia de personal", "Proponer al Gobierno el proyecto de Ley de Bases"]),
  fichab("Desarrollo, coordinación y control de la política de personal",
         f"{c('L30', 'Artículo cuatro', 'Ministro de la Presidencia')} (denominación del texto)",
         ["a) Proponer al Gobierno los proyectos de normas de general aplicación a la Función Pública (los de regímenes especiales, a iniciativa del Ministerio competente)", "b) Planes para mejorar el rendimiento, la formación y la promoción del personal", "c) Velar por el cumplimiento de las normas de general aplicación en materia de personal", "d) Las demás que le atribuya la legislación"],
         "—",
         "El Gobierno **dirige**; el Ministro **desarrolla, coordina y controla** la ejecución."))}

{unidad("2.3 El Ministro de Hacienda y la Comisión Superior de Personal (Ley 30/1984, arts. 5 y 9)",
  lit("L30", "Artículo cinco", ["las directrices a que deberán ajustarse los gastos de personal", "autorizar cualquier medida relativa al personal que pueda suponer modificaciones en el gasto"]),
  lit("L30", "Artículo nueve", ["Organo colegiado de coordinación, documentación y asesoramiento", "El Gobierno, por Real Decreto, regulará su composición y funciones"]),
  fichab("Control del gasto de personal y órgano colegiado de coordinación",
         [f"{c('L30', 'Artículo cinco', 'Ministro de Economía y Hacienda')} (denominación del texto)", "Comisión Superior de Personal (órgano colegiado)"],
         ["Hacienda: propone las directrices de los **gastos de personal** y **autoriza** toda medida de personal que modifique el gasto (art. 5)", "Comisión Superior de Personal: coordinación, documentación y asesoramiento para la política de personal del Estado; composición y funciones por Real Decreto (art. 9)"],
         "—",
         "Toda medida de personal que suponga **modificación del gasto** necesita autorización de **Hacienda**."))}
""", 2)

T.ap("s12", "IV.3 El reparto de competencias: Gobierno, Ministros, Secretario de Estado y Director general de la Función Pública (RD 2169/1984, arts. 3, 5, 6 y 7)", f"""
El **Real Decreto 2169/1984**, de atribución de competencias en materia de personal, desarrolla la Ley 30/1984 (art. 1). Se cita su texto consolidado del BOE, sin los apartados que figuran como «(Derogado)»; las denominaciones de órganos son las de su texto. Su art. 2 reproduce las competencias del Gobierno del art. 3 de la Ley 30/1984 (→ IV.2.1).

{unidad("3.1 Lo que el Ministro propone al Gobierno (RD 2169/1984, art. 3) y Hacienda (art. 5)",
  lit("RD2169", "Artículo 3", ["La aprobación de la Oferta de Empleo Público", "Las normas reguladoras del Registro Central de Personal", "La separación del servicio, previa la instrucción de expediente disciplinario", "Las convocatorias de pruebas unitarias de selección", "La convocatoria de concursos unitarios de traslados"]),
  lit("RD2169", "Artículo 5", ["autorizar cualquier medida relativa al personal que pueda suponer modificaciones en el gasto"]),
  fichab("Propuestas al Gobierno en materia de personal funcionario",
         "Propone el Ministro de la Presidencia (denominación del texto); decide el **Gobierno**",
         ["::Entre otras propuestas:", "Proyectos de normas de general aplicación a la Función Pública (3.1)", "**Aprobación de la Oferta de Empleo Público** (3.4)", "Grados e intervalos de niveles (3.5); adscripción de Cuerpos y Escalas (3.6)", "Normas del **Registro Central de Personal** (3.8)", "**Separación del servicio**, previo expediente, a iniciativa del Departamento (3.13)", "Convocatorias de **pruebas unitarias** de selección (3.14) y de **concursos unitarios** de traslados (3.15)"],
         "—",
         "La **separación del servicio** la acuerda el **Gobierno** a propuesta del Ministro: por eso los Ministros tienen la potestad disciplinaria **excepto la separación** (→ IV.4.2). Hacienda autoriza toda medida que modifique el gasto (art. 5)."))}

{unidad("3.2 Secretario de Estado para la Administración Pública y Director general de la Función Pública (RD 2169/1984, arts. 6 y 7)",
  lit("RD2169", "Artículo 6", ["El nombramiento de funcionarios de carrera y la expedición de los correspondientes títulos administrativos", "La aprobación de las bases de las convocatorias de los concursos para provisión de puestos de trabajo", "cursos de selección, formación y perfeccionamiento"], solo=[1, 2, 4, 5, 6, 7, 10]),
  lit("RD2169", "Artículo 7", ["El control de las propuestas de inscripciones en el Registro Central de Personal", "no atribuidos a los Departamentos ministeriales"], solo=[1, 2, 5]),
  fichab("Competencias de los órganos centrales de función pública",
         ["Secretario de Estado para la Administración Pública (denominación del texto)", "Director general de la Función Pública"],
         ["SE: régimen jurídico e inspección de la Función Pública (6.1)", "SE: **nombramiento de funcionarios de carrera** y expedición de títulos (6.3)", "SE: **bases** de las convocatorias de los concursos de provisión (6.4)", "SE: racionalización de Cuerpos y Escalas (6.5); cursos de selección, formación y perfeccionamiento (6.6)", "DG: control de las propuestas de inscripción en el **Registro Central de Personal** (7.1) y actos de gestión no atribuidos a los Departamentos (7.4)"],
         "—",
         "Nombra a los funcionarios de carrera el **Secretario de Estado** (coincide con el RD 364/1995, art. 25, → III.4.7). Las **bases** de los concursos las aprueba el SE; la **convocatoria** y resolución, los Ministros (→ IV.4.2)."))}
""", 2)

T.ap("s13", "IV.4 Departamentos, Ministros, Subsecretarios y personal laboral y eventual (RD 2169/1984, arts. 8 a 13) y cuadro", f"""
{unidad("4.1 Los Departamentos respecto de sus Cuerpos (RD 2169/1984, art. 8)",
  lit("RD2169", "Artículo 8", ["Informar la adscripción concreta de los Cuerpos o Escalas", "serán ejercidas por el Subsecretario del Departamento respectivo"], solo=[1, 2, 6]),
  fichab("Competencias del Departamento de adscripción de los Cuerpos o Escalas",
         "El **Subsecretario** del Departamento (y el Director general de la Función Pública para los Cuerpos dependientes de la Secretaría de Estado)",
         "Informar la adscripción concreta de los Cuerpos o Escalas bajo su dependencia",
         "—",
         "Los demás apartados del art. 8 figuran como «(Derogado)» en el texto consolidado."))}

{unidad("4.2 Ministros y Secretarios de Estado (RD 2169/1984, art. 9)",
  lit("RD2169", "Artículo 9", ["La provisión de los puestos de trabajo de libre designación, previa convocatoria pública", "La convocatoria de los concursos para la provisión de puestos de trabajo", "excepto la separación del servicio", "La propuesta de la relación de puestos de trabajo"]),
  fichab("Competencias sobre los funcionarios destinados en el Departamento o en sus unidades",
         "Los **Ministros** (funcionarios destinados en su Departamento) y los **Secretarios de Estado** (en las unidades adscritas)",
         ["Provisión de puestos de **libre designación**, previa convocatoria pública", "**Convocar y resolver** los concursos de provisión, con las bases aprobadas (art. 6.4)", "**Potestad disciplinaria**, excepto la separación del servicio", "**Propuesta** de la RPT", "Premios o recompensas; representantes en las Comisiones de análisis de los programas de gasto"],
         "—",
         "Disciplina: los Ministros, **todo salvo la separación** (que acuerda el Gobierno, → IV.3.1). La RPT: los Ministros la **proponen**. La provisión se estudia en el tema V.4."))}

{unidad("4.3 Los Subsecretarios (RD 2169/1984, arts. 10 y 11)",
  lit("RD2169", "Artículo 10", ["Ejercer la jefatura y asumir la inspección de personal", "Reconocer la adquisición y cambio de grados personales", "Todos aquellos actos de administración y gestión ordinaria del personal"]),
  lit("RD2169", "Artículo 11", ["Dar posesión y cese", "Declarar las jubilaciones forzosas y por incapacidad física", "La concesión de permisos o licencias", "El reconocimiento de trienios"]),
  fichab("Superior dirección y gestión ordinaria del personal del Ministerio",
         ["**Subsecretarios** (art. 10)", "Subsecretarios (servicios centrales) y Delegados del Gobierno y Gobernadores civiles (servicios periféricos) (art. 11, según el texto)"],
         ["Art. 10: jefatura e inspección de personal; grados personales; servicios especiales y servicio en CC. AA.; comisión de servicios con cambio de localidad; asistencia a cursos; **gestión ordinaria** no atribuida a otros órganos", "Art. 11: comisión de servicios de menos de seis meses sin cambio de Ministerio ni de localidad; **toma de posesión y cese**; **jubilaciones** forzosas y por incapacidad; compatibilidades (propuesta e informe); **permisos y licencias**; **trienios**; excedencias voluntarias que no sean por interés particular; desempeño provisional de puestos en los casos del art. 21.2 c) de la Ley 30/1984 (en los Organismos Autónomos, sus Directores) (11.8)"],
         "Comisión de servicios del art. 11: **inferior a seis meses**",
         "El Subsecretario tiene la competencia **residual**: los actos de gestión ordinaria no atribuidos a otro órgano (10.6)."))}

{unidad("4.4 Personal laboral y personal eventual (RD 2169/1984, arts. 12 y 13)",
  lit("RD2169", "Artículo 12", ["Proponer al Gobierno la aprobación de la oferta de empleo público", "Establecer los criterios generales para su selección", "Las restantes competencias serán ejercidas por los Subsecretarios"]),
  lit("RD2169", "Artículo 13", ["Corresponde a los Ministros y a los Secretarios de Estado el nombramiento y cese del personal eventual"]),
  fichab("Competencias sobre el personal laboral y el eventual",
         ["Laboral: el Ministerio de la Presidencia (denominación del texto); el resto, los **Subsecretarios** del Departamento donde presta servicios", "Eventual: **Ministros y Secretarios de Estado**"],
         ["Laboral (art. 12): coordinación y control generales; **proponer al Gobierno la oferta** y la racionalización de plantillas; **criterios generales de selección**; puestos de la RPT para personal laboral", "Eventual (art. 13): **nombramiento y cese**"],
         "—",
         "El personal eventual lo nombran y cesan **Ministros y Secretarios de Estado**; nombramiento y cese son libres (TREBEP, art. 12.3)."))}

### 4.5 Cuadro: quién hace qué en la selección y la gestión del personal de la AGE (esquema)

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Acto | Órgano | Norma |
|---|---|---|
| Dirigir la política de personal; potestad reglamentaria | **Gobierno** | Ley 30/1984, art. 3.1 |
| Aprobar la oferta de empleo público | **Gobierno** (a propuesta del Ministro que designa cada texto) | Ley 30/1984, art. 3.2 g; RD 364/1995, art. 8; RD 2169/1984, art. 3.4 |
| Convocar los procesos selectivos | **Departamento** de adscripción del Cuerpo (informe favorable de la DG de la Función Pública) | RD 364/1995, art. 9 |
| Nombrar funcionarios de carrera | **Secretario de Estado** para la Administración Pública | RD 364/1995, art. 25; RD 2169/1984, art. 6.3 |
| Nombrar funcionarios interinos | **Subsecretario** del Departamento | RD 364/1995, art. 27 |
| Separación del servicio | **Gobierno**, a propuesta del Ministro | RD 2169/1984, art. 3.13 |
| Resto de la potestad disciplinaria | **Ministros** y Secretarios de Estado | RD 2169/1984, art. 9.3 |
| Medidas de personal que modifiquen el gasto | Autoriza **Hacienda** | Ley 30/1984, art. 5; RD 2169/1984, art. 5 |
| Permisos, licencias, trienios, toma de posesión | **Subsecretarios** (y Delegados del Gobierno en la periferia) | RD 2169/1984, art. 11 |
| Personal eventual: nombramiento y cese | **Ministros** y Secretarios de Estado | RD 2169/1984, art. 13 |

{resumen([
  "Cooperación: **Conferencia Sectorial de Administración Pública** y, dependiente de ella, la **Comisión de Coordinación del Empleo Público** (TREBEP, art. 100).",
  "El **Gobierno** dirige la política de personal y **aprueba la oferta**; el Ministro (de la Presidencia, según el texto) **desarrolla, coordina y controla**; **Hacienda** autoriza lo que modifique el gasto (Ley 30/1984, arts. 3 a 5).",
  "El **Secretario de Estado** nombra a los funcionarios de carrera y aprueba las bases de los concursos; los **Ministros** convocan y resuelven concursos y libre designación y ejercen la disciplina **salvo la separación** (Gobierno).",
  "Los **Subsecretarios** llevan la jefatura de personal y la gestión ordinaria: posesión y cese, permisos, trienios, jubilaciones; el **eventual** lo nombran Ministros y Secretarios de Estado (RD 2169/1984)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_L65 = examen("L", 65, {
  "a": f"Un año es el plazo de la **fase de oposición** en la AGE (RDL 6/2023, art. 108.2: {c('RDL6', 'Artículo 108', 'las respectivas fases de oposición en un año')}), no el de ejecución de la oferta del art. 70.",
  "b": f"Dos años es el plazo de ejecución de las **convocatorias** en la AGE ({c('RDL6', 'Artículo 108', 'en el plazo máximo de dos años desde su publicación')}), no el de la oferta en el TREBEP.",
  "c": f"Literal del art. 70.1: {c('TREBEP', 'Artículo 70', 'la ejecución de la oferta de empleo público o instrumento similar deberá desarrollarse dentro del plazo improrrogable de tres años')}.",
  "d": f"Ningún plazo de cuatro años: el art. 70.1 dice {c('TREBEP', 'Artículo 70', 'tres años')}."},
  [("Tres años", "TREBEP", "Artículo 70", "deberá desarrollarse dentro del plazo improrrogable de tres años")])
EX_X72 = examen("X", 72, {
  "a": f"Cambia los dos plazos: el art. 108.2 dice {c('RDL6', 'Artículo 108', 'dos años desde su publicación')} y la fase de oposición {c('RDL6', 'Artículo 108', 'en un año')}. Los tres años son el plazo del TREBEP para ejecutar la **oferta** (art. 70.1).",
  "b": f"Acierta la fase de oposición (un año), pero la convocatoria se ejecuta {c('RDL6', 'Artículo 108', 'en el plazo máximo de dos años desde su publicación')}, no en tres.",
  "c": f"Acierta los dos años de la convocatoria, pero la fase de oposición es {c('RDL6', 'Artículo 108', 'en un año')}, no «en esos dos años».",
  "d": f"Literal del art. 108.2: {c('RDL6', 'Artículo 108', 'Las convocatorias deberán ejecutarse en el plazo máximo de dos años desde su publicación, y las respectivas fases de oposición en un año, salvo causa justificada')}."},
  [("dos años desde su publicación", "RDL6", "Artículo 108", "Las convocatorias deberán ejecutarse en el plazo máximo de dos años desde su publicación"),
   ("fases de oposición en un año", "RDL6", "Artículo 108", "y las respectivas fases de oposición en un año, salvo causa justificada")])
EX_X75 = examen("X", 75, {
  "a": f"El porcentaje es mayor: {c('RDL6', 'Artículo 108', 'no inferior al treinta por ciento de las plazas de acceso libre para promoción interna')}.",
  "b": f"Literal del art. 108.3: {c('RDL6', 'Artículo 108', 'La oferta de empleo público incluirá un porcentaje no inferior al treinta por ciento de las plazas de acceso libre para promoción interna')}.",
  "c": f"El diez por ciento es la reserva para **personas con discapacidad** en la AGE: {c('RDL6', 'Artículo 108', 'un porcentaje no inferior al diez por ciento de las plazas convocadas para ser cubiertas entre personas con discapacidad')} (108.4), no la de promoción interna.",
  "d": f"Ningún cinco por ciento en el art. 108: la promoción interna es {c('RDL6', 'Artículo 108', 'no inferior al treinta por ciento')}."},
  [("treinta por ciento", "RDL6", "Artículo 108", "un porcentaje no inferior al treinta por ciento de las plazas de acceso libre para promoción interna")])
EX_X70 = examen("X", 70, {
  "a": f"Es lo que resulta del TREBEP: las Administraciones {c('TREBEP', 'Artículo 55', 'seleccionarán a su personal funcionario y laboral mediante procedimientos')} con publicidad (55.2 a); {c('TREBEP', 'Artículo 10', 'Los procedimientos de selección del personal funcionario interino serán públicos')} (10.2) y {c('TREBEP', 'Artículo 11', 'Los procedimientos de selección del personal laboral serán públicos')} (11.3).",
  "b": f"Para el interino no es potestativo: {c('TREBEP', 'Artículo 10', 'Los procedimientos de selección del personal funcionario interino serán públicos')}.",
  "c": f"Para el laboral la publicidad no se excluye: {c('TREBEP', 'Artículo 11', 'Los procedimientos de selección del personal laboral serán públicos')}. Lo que se puede negociar es la colaboración sindical en el desarrollo de los procesos (61.7), no suprimir la publicidad.",
  "d": f"El personal eventual no se selecciona por procedimientos públicos: {c('TREBEP', 'Artículo 12', 'El nombramiento y cese serán libres')} (art. 12.3)."},
  [("interino, o de personal laboral", "TREBEP", "Artículo 10", "Los procedimientos de selección del personal funcionario interino serán públicos"),
   ("personal laboral", "TREBEP", "Artículo 11", "Los procedimientos de selección del personal laboral serán públicos"),
   ("personal funcionario", "TREBEP", "Artículo 55", "seleccionarán a su personal funcionario y laboral")])
EX_X81 = examen("X", 81, {
  "a": f"Le falta la oposición: {c('TREBEP', 'Artículo 61', 'Los sistemas selectivos de personal laboral fijo serán los de oposición, concurso-oposición')}… {c('TREBEP', 'Artículo 61', 'o concurso de valoración de méritos')}.",
  "b": "Le faltan la oposición y el concurso-oposición: el art. 61.7 enumera tres sistemas, no uno.",
  "c": f"Literal del art. 61.7: {c('TREBEP', 'Artículo 61', 'Los sistemas selectivos de personal laboral fijo serán los de oposición, concurso-oposición, con las características establecidas en el apartado anterior, o concurso de valoración de méritos')}.",
  "d": "Solo uno de los tres sistemas del art. 61.7; faltan la oposición y el concurso de valoración de méritos."},
  [("Oposición, concurso-oposición", "TREBEP", "Artículo 61", "Los sistemas selectivos de personal laboral fijo serán los de oposición, concurso-oposición"),
   ("concurso de valoración de méritos", "TREBEP", "Artículo 61", "o concurso de valoración de méritos")])
EX_L66 = examen("L", 66, {
  "a": f"La oferta de empleo público recoge necesidades de **nuevo ingreso** (art. 108.2); los puestos no se adscriben a ella: {c('RDL6', 'Artículo 110', 'los puestos de trabajo estarán adscritos a una o varias áreas funcionales')}.",
  "b": f"Literal del art. 110.3: {c('RDL6', 'Artículo 110', 'Con carácter general, los puestos de trabajo estarán adscritos a una o varias áreas funcionales')}.",
  "c": f"El perfil de competencias se analiza para **crear, modificar o suprimir** un puesto ({c('RDL6', 'Artículo 110', 'análisis acerca del perfil de competencias necesario para su desempeño')}, 110.2), pero la adscripción es a **áreas funcionales**.",
  "d": f"En el Registro Central se **inscribe al personal** (Ley 30/1984, art. 13.1: {c('L30', 'Artículo trece', 'se inscribirá a todo el personal al servicio de la Administración del Estado')}); los puestos no se adscriben a él."},
  [("una o varias áreas funcionales", "RDL6", "Artículo 110", "los puestos de trabajo estarán adscritos a una o varias áreas funcionales")])

T.ap("s14", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **cinco** preguntas de este tema (una en el turno libre y cuatro en el extraordinario) y **una** relacionada. Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-L 2025, pregunta 65 · Plazo de ejecución de la oferta (→ II.1.1)", EX_L65,
  "### GACE-L 2025 extraordinario, pregunta 72 · Plazos de las convocatorias en la AGE (→ II.1.2)", EX_X72,
  "### GACE-L 2025 extraordinario, pregunta 75 · Promoción interna en la oferta (→ II.1.3)", EX_X75,
  "### GACE-L 2025 extraordinario, pregunta 70 · Publicidad de la selección (→ III.1.1)", EX_X70,
  "### GACE-L 2025 extraordinario, pregunta 81 · Sistemas selectivos del personal laboral fijo (→ III.3.2)", EX_X81,
  "### GACE-L 2025, pregunta 66 · Áreas funcionales (relacionada; → I.2.4)", EX_L66,
  "### Cómo se pregunta",
  "!> Los **plazos** se preguntan cruzando normas: **tres años** para ejecutar la oferta (TREBEP, art. 70), **dos años** para ejecutar la convocatoria y **uno** para la fase de oposición en la AGE (RDL 6/2023, art. 108.2). Y los **porcentajes**: **30 %** promoción interna, **10 %** discapacidad en la AGE, **7 %** en el TREBEP.",
]))

T.ap("s15", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Planificación | Objetivos y Planes (TREBEP 69); Registros (71); planificación estratégica plurianual (RDL 6/2023, 107); RPT y áreas funcionales (109 y 110) | Puestos adscritos a **áreas funcionales**; planificación con **negociación previa** y **evaluación posterior** |
| II. Oferta de empleo público | Necesidades con dotación y de nuevo ingreso; + 10 %; anual y publicada (TREBEP 70); AGE: RDL 6/2023, 108; RD 364/1995, 7 a 9 | **3 años** improrrogables (oferta); **2 años** convocatoria y **1 año** oposición (AGE); **30 %** promoción interna |
| III. Selección | Publicidad para carrera, interinos y laborales; arts. 55 a 61; RDL 6/2023, 112, 114 y 115; RD 364/1995 | Laboral fijo: **oposición, concurso-oposición o concurso de méritos**; tribunal **impar, mínimo cinco**; solicitudes **20 días naturales** |
| IV. Competencias | Conferencia Sectorial y Comisión de Coordinación (TREBEP 100); Gobierno, Ministro, Hacienda (Ley 30/1984); RD 2169/1984 | **Gobierno** aprueba la oferta; **Secretario de Estado** nombra funcionarios de carrera; separación: **Gobierno** |

?> **Trampas frecuentes:** «la oferta se ejecuta en **dos** años» (son **tres**, art. 70; los dos años son de la **convocatoria** en la AGE); «**20 %** para promoción interna» (es **30 %**); «el concurso es sistema ordinario de los funcionarios» (solo por **ley** y **excepcionalmente**); «los **interinos** pueden formar parte del tribunal» (no: art. 60.2); «los extranjeros con residencia legal pueden ser **funcionarios**» (solo **laborales**, art. 57.4); «la selección del laboral puede no ser pública por convenio» (es **pública**, art. 11.3); «nombra a los funcionarios de carrera el **Subsecretario**» (es el **Secretario de Estado**).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
P = T.q
P("TREBEP", "Artículo 69", "Planificación", "Según el artículo 69.1 del TREBEP, la planificación de los recursos humanos en las Administraciones Públicas tendrá como objetivo contribuir a la consecución de:",
  ["La eficacia en la prestación de los servicios y la eficiencia en la utilización de los recursos económicos disponibles.", "La estabilidad presupuestaria y la sostenibilidad financiera de las Administraciones Públicas.", "La reducción del gasto de personal y la amortización de las plazas vacantes.", "La igualdad de trato y la estabilidad en el empleo del personal temporal."],
  "Art. 69.1 TREBEP.", "contribuir a la consecución de la eficacia en la prestación de los servicios y de la eficiencia en la utilización de los recursos económicos disponibles")
P("TREBEP", "Artículo 69", "Planificación", "Según el artículo 69.2 del TREBEP, los Planes para la ordenación de los recursos humanos podrán incluir, como medida de movilidad:",
  ["La suspensión de incorporaciones de personal externo a un determinado ámbito.", "La supresión de la oferta de empleo público durante tres años.", "El cese del personal funcionario interino de todos los ámbitos.", "La integración del personal laboral fijo en cuerpos de funcionarios."],
  "Art. 69.2 c) TREBEP.", "la suspensión de incorporaciones de personal externo a un determinado ámbito")
P("TREBEP", "Artículo 71", "Planificación", "Según el artículo 71.3 del TREBEP, los contenidos mínimos comunes de los Registros de personal se establecerán:",
  ["Mediante convenio de Conferencia Sectorial.", "Mediante real decreto del Gobierno.", "Por acuerdo de la Mesa General de Negociación.", "Por orden del Ministerio de Hacienda."],
  "Art. 71.3 TREBEP.", "Mediante convenio de Conferencia Sectorial se establecerán los contenidos mínimos comunes de los Registros de personal")
P("L30", "Artículo trece", "Planificación", "Según el artículo 13.5 de la Ley 30/1984, en la documentación individual del personal de las Administraciones Públicas no figurará ningún dato relativo a su:",
  ["Raza, religión u opinión.", "Titulación académica.", "Grado personal consolidado.", "Situación administrativa."],
  "Art. 13.5 Ley 30/1984.", "no figurará ningún dato relativo a su raza, religión u opinión")
P("RDL6", "Artículo 107", "Planificación", "Según el artículo 107.5 del Real Decreto-ley 6/2023, los instrumentos de planificación estratégica de los recursos humanos deberán ser objeto de:",
  ["Negociación colectiva previa y evaluación posterior.", "Informe previo del Consejo de Estado.", "Aprobación por las Cortes Generales.", "Publicación en el Diario Oficial de la Unión Europea."],
  "Art. 107.5 RDL 6/2023.", "deberán ser objeto de negociación colectiva previa en los ámbitos correspondientes y de evaluación posterior")
P("RDL6", "Artículo 107", "Planificación", "Según el artículo 107.1 del Real Decreto-ley 6/2023, a través de la planificación estratégica de los recursos humanos la Administración del Estado establece:",
  ["El escenario plurianual de empleo público.", "El escenario anual de empleo público.", "El presupuesto de gastos de personal.", "La relación de puestos de trabajo de cada departamento."],
  "Art. 107.1 RDL 6/2023: «escenario plurianual de empleo público».", "establece el escenario plurianual de empleo público")
P("RDL6", "Artículo 109", "Planificación", "Según el artículo 109.1 del Real Decreto-ley 6/2023, las relaciones de puestos de trabajo:",
  ["Son públicas y han de incluir todos los puestos de naturaleza funcionarial, laboral y eventual existentes.", "Son reservadas y solo incluyen los puestos de naturaleza funcionarial.", "Son públicas, pero excluyen los puestos de personal eventual.", "Solo incluyen los puestos vacantes dotados presupuestariamente."],
  "Art. 109.1 RDL 6/2023.", ["Las relaciones de puestos de trabajo son públicas", "todos los puestos de trabajo de naturaleza funcionarial, laboral y eventual existentes"])
P("TREBEP", "Artículo 70", "Oferta de empleo público", "Según el artículo 70.1 del TREBEP, la Oferta de empleo público comportará la obligación de convocar los correspondientes procesos selectivos para las plazas comprometidas y hasta:",
  ["Un diez por cien adicional.", "Un veinte por cien adicional.", "Un cinco por cien adicional.", "Un treinta por cien adicional."],
  "Art. 70.1 TREBEP.", "hasta un diez por cien adicional")
P("TREBEP", "Artículo 70", "Oferta de empleo público", "Según el artículo 70.2 del TREBEP, la Oferta de empleo público o instrumento similar:",
  ["Se aprobará anualmente por los órganos de Gobierno de las Administraciones Públicas y deberá ser publicada en el Diario oficial correspondiente.", "Se aprobará cada tres años por las Cortes Generales y se publicará en el Boletín Oficial del Estado.", "Se aprobará anualmente por la Mesa General de Negociación y no requiere publicación.", "Se aprobará cada dos años por el órgano competente en materia de función pública."],
  "Art. 70.2 TREBEP.", "que se aprobará anualmente por los órganos de Gobierno de las Administraciones Públicas, deberá ser publicada en el Diario oficial correspondiente")
P("TREBEP", "Artículo 70", "Oferta de empleo público", "Según el artículo 70.1 del TREBEP, son objeto de la Oferta de empleo público las necesidades de recursos humanos:",
  ["Con asignación presupuestaria, que deban proveerse mediante la incorporación de personal de nuevo ingreso.", "Sin asignación presupuestaria, que deban cubrirse mediante promoción interna.", "Que deban cubrirse mediante concurso de provisión de puestos.", "Que deban cubrirse con personal eventual."],
  "Art. 70.1 TREBEP.", "Las necesidades de recursos humanos, con asignación presupuestaria, que deban proveerse mediante la incorporación de personal de nuevo ingreso serán objeto de la Oferta de empleo público")
P("RDL6", "Artículo 108", "Oferta de empleo público", "Según el artículo 108.2 del Real Decreto-ley 6/2023, las convocatorias deberán publicarse:",
  ["En el mismo año natural de la publicación en el BOE de la oferta de empleo público en la que se incluyan las plazas.", "En el primer trimestre del año siguiente al de la publicación de la oferta.", "En el plazo de tres años desde la publicación de la oferta.", "En el plazo de dos años desde la aprobación de la oferta."],
  "Art. 108.2 RDL 6/2023.", "Las convocatorias deberán publicarse en el mismo año natural de la publicación en el «Boletín Oficial del Estado» de la oferta de empleo público")
P("RDL6", "Artículo 108", "Oferta de empleo público", "Según el artículo 108.2 del Real Decreto-ley 6/2023, las plazas no cubiertas en la ejecución de una convocatoria podrán convocarse nuevamente siempre que no hayan transcurrido más de:",
  ["Tres años desde la publicación de la oferta.", "Dos años desde la publicación de la convocatoria.", "Un año desde la finalización de la fase de oposición.", "Cuatro años desde la aprobación de la oferta."],
  "Art. 108.2 RDL 6/2023.", "siempre que no hayan transcurrido más de tres años desde la publicación de la oferta")
P("RDL6", "Artículo 108", "Oferta de empleo público", "Según el artículo 108.4 del Real Decreto-ley 6/2023, en la oferta de empleo público de la Administración del Estado se reservará para personas con discapacidad un porcentaje no inferior al:",
  ["Diez por ciento de las plazas convocadas.", "Siete por ciento de las plazas convocadas.", "Cinco por ciento de las plazas convocadas.", "Treinta por ciento de las plazas convocadas."],
  "Art. 108.4 RDL 6/2023 (el TREBEP, art. 59, fija el 7 % con carácter general).", "se reservará un porcentaje no inferior al diez por ciento de las plazas convocadas")
P("RD364", "Artículo 8", "Oferta de empleo público", "Según el artículo 8.1 del Real Decreto 364/1995, la oferta de empleo público será aprobada, en su caso, por el Gobierno:",
  ["En el primer trimestre de cada año.", "En el último trimestre de cada año.", "En el primer semestre de cada año.", "Antes del 1 de octubre de cada año."],
  "Art. 8.1 RD 364/1995.", "en el primer trimestre de cada año")
P("RD364", "Artículo 9", "Oferta de empleo público", "Según el artículo 9 del Real Decreto 364/1995, aprobada la oferta de empleo público, convocan los procedimientos selectivos de acceso:",
  ["Los Departamentos a los que figuren adscritos los correspondientes Cuerpos y Escalas, previo informe favorable de la Dirección General de la Función Pública.", "El Gobierno, a propuesta del Ministro de Hacienda.", "La Dirección General de la Función Pública, previo informe de los Departamentos.", "El Instituto Nacional de Administración Pública, en todo caso."],
  "Art. 9 RD 364/1995.", "los Departamentos a los que figuren adscritos los correspondientes Cuerpos y Escalas de funcionarios procederán a la convocatoria")
P("TREBEP", "Artículo 55", "Selección", "¿Cuál de los siguientes NO figura entre los principios del artículo 55.2 del TREBEP para los procedimientos de selección?",
  ["Antigüedad de los aspirantes en la Administración.", "Transparencia.", "Agilidad, sin perjuicio de la objetividad, en los procesos de selección.", "Publicidad de las convocatorias y de sus bases."],
  "Art. 55.2 TREBEP: publicidad, transparencia, imparcialidad y profesionalidad, independencia y discrecionalidad técnica, adecuación y agilidad.", ["Publicidad de las convocatorias y de sus bases", "Transparencia", "Agilidad, sin perjuicio de la objetividad, en los procesos de selección"])
P("TREBEP", "Artículo 56", "Selección", "Según el artículo 56.1 c) del TREBEP, para participar en los procesos selectivos será necesario tener cumplidos:",
  ["Dieciséis años.", "Dieciocho años.", "Veintiún años.", "Catorce años."],
  "Art. 56.1 c) TREBEP.", "Tener cumplidos dieciséis años")
P("TREBEP", "Artículo 56", "Selección", "Según el artículo 56.1 c) del TREBEP, una edad máxima para el acceso al empleo público distinta de la edad de jubilación forzosa:",
  ["Sólo podrá establecerse por ley.", "Podrá establecerse en cada convocatoria.", "Podrá establecerse por real decreto.", "No podrá establecerse en ningún caso."],
  "Art. 56.1 c) TREBEP.", "Sólo por ley podrá establecerse otra edad máxima, distinta de la edad de jubilación forzosa, para el acceso al empleo público")
P("TREBEP", "Artículo 57", "Selección", "Según el artículo 57.4 del TREBEP, los extranjeros con residencia legal en España podrán acceder a las Administraciones Públicas:",
  ["Como personal laboral, en igualdad de condiciones que los españoles.", "Como personal funcionario, en igualdad de condiciones que los españoles.", "Como personal funcionario interino únicamente.", "Como personal eventual únicamente."],
  "Art. 57.4 TREBEP.", "los extranjeros con residencia legal en España podrán acceder a las Administraciones Públicas, como personal laboral, en igualdad de condiciones que los españoles")
P("TREBEP", "Artículo 57", "Selección", "Según el artículo 57.5 del TREBEP, podrá eximirse del requisito de la nacionalidad por razones de interés general para el acceso a la condición de personal funcionario:",
  ["Sólo por ley de las Cortes Generales o de las asambleas legislativas de las comunidades autónomas.", "Por real decreto del Gobierno.", "Por las bases de cada convocatoria.", "Por acuerdo de la Conferencia Sectorial de Administración Pública."],
  "Art. 57.5 TREBEP.", "Sólo por ley de las Cortes Generales o de las asambleas legislativas de las comunidades autónomas podrá eximirse del requisito de la nacionalidad")
P("TREBEP", "Artículo 59", "Selección", "Según el artículo 59.1 del TREBEP, en las ofertas de empleo público se reservará para personas con discapacidad un cupo no inferior al:",
  ["Siete por ciento de las vacantes.", "Diez por ciento de las vacantes.", "Cinco por ciento de las vacantes.", "Dos por ciento de las vacantes."],
  "Art. 59.1 TREBEP (en la AGE, el RDL 6/2023 lo eleva al 10 %).", "se reservará un cupo no inferior al siete por ciento de las vacantes")
P("TREBEP", "Artículo 60", "Órganos de selección", "Según el artículo 60.2 del TREBEP, NO podrán formar parte de los órganos de selección:",
  ["Los funcionarios interinos.", "Los funcionarios de carrera.", "Los funcionarios de otras Administraciones Públicas.", "Los funcionarios jubilados."],
  "Art. 60.2 TREBEP: personal de elección o designación política, funcionarios interinos y personal eventual.", "El personal de elección o de designación política, los funcionarios interinos y el personal eventual no podrán formar parte de los órganos de selección")
P("TREBEP", "Artículo 60", "Órganos de selección", "Según el artículo 60.3 del TREBEP, la pertenencia a los órganos de selección será siempre:",
  ["A título individual, no pudiendo ostentarse en representación o por cuenta de nadie.", "En representación de las organizaciones sindicales más representativas.", "En representación del órgano convocante.", "A título individual o en representación de la Administración que designe."],
  "Art. 60.3 TREBEP.", "La pertenencia a los órganos de selección será siempre a título individual, no pudiendo ostentarse ésta en representación o por cuenta de nadie")
P("RDL6", "Artículo 115", "Órganos de selección", "Según el artículo 115.2 del Real Decreto-ley 6/2023, ¿quién NO puede formar parte de los órganos de selección de la Administración del Estado?",
  ["El personal laboral no fijo.", "El personal funcionario de carrera.", "El personal laboral fijo.", "Las personas con discapacidad."],
  "Art. 115.2 RDL 6/2023: altos cargos, personal de elección o designación política, funcionarios interinos, personal laboral no fijo y personal eventual.", "el personal funcionario interino, el personal laboral no fijo y el personal eventual")
P("RD364", "Artículo 11", "Órganos de selección", "Según el artículo 11 del Real Decreto 364/1995, los Tribunales estarán constituidos por un número impar de miembros, funcionarios de carrera:",
  ["No inferior a cinco.", "No inferior a tres.", "No inferior a siete.", "No superior a cinco."],
  "Art. 11 RD 364/1995.", "Estarán constituidos por un número impar de miembros, funcionarios de carrera, no inferior a cinco")
P("RD364", "Artículo 13", "Órganos de selección", "Según el artículo 13.2 del Real Decreto 364/1995, no podrán formar parte de los órganos de selección los funcionarios que hubiesen realizado tareas de preparación de aspirantes a pruebas selectivas en los:",
  ["Cinco años anteriores a la publicación de la correspondiente convocatoria.", "Dos años anteriores a la publicación de la correspondiente convocatoria.", "Diez años anteriores a la publicación de la correspondiente convocatoria.", "Tres años anteriores a la celebración de la primera prueba."],
  "Art. 13.2 RD 364/1995.", "en los cinco años anteriores a la publicación de la correspondiente convocatoria")
P("TREBEP", "Artículo 61", "Sistemas selectivos", "Según el artículo 61.6 del TREBEP, los sistemas selectivos de funcionarios de carrera serán:",
  ["Los de oposición y concurso-oposición; sólo en virtud de ley podrá aplicarse, con carácter excepcional, el de concurso.", "Los de oposición, concurso-oposición y concurso, indistintamente.", "Los de concurso-oposición y, con carácter excepcional, el de oposición.", "Los de oposición y concurso; el concurso-oposición solo para promoción interna."],
  "Art. 61.6 TREBEP.", ["Los sistemas selectivos de funcionarios de carrera serán los de oposición y concurso-oposición", "Sólo en virtud de ley podrá aplicarse, con carácter excepcional, el sistema de concurso"])
P("TREBEP", "Artículo 61", "Sistemas selectivos", "Según el artículo 61.3 del TREBEP, en los procesos selectivos que incluyan la valoración de méritos, dicha valoración:",
  ["Tendrá una puntuación proporcionada que no determinará, en ningún caso, por sí misma el resultado del proceso selectivo.", "Podrá determinar por sí misma el resultado del proceso selectivo si así lo prevé la convocatoria.", "Supondrá, como máximo, el cincuenta por ciento de la puntuación total.", "Solo se aplicará a los aspirantes de promoción interna."],
  "Art. 61.3 TREBEP.", "sólo podrán otorgar a dicha valoración una puntuación proporcionada que no determinará, en ningún caso, por sí misma el resultado del proceso selectivo")
P("TREBEP", "Artículo 61", "Sistemas selectivos", "Según el artículo 61.8 del TREBEP, los órganos de selección no podrán proponer el acceso a la condición de funcionario de un número superior de aprobados al de plazas convocadas:",
  ["Excepto cuando así lo prevea la propia convocatoria.", "En ningún caso.", "Excepto cuando lo autorice la Mesa General de Negociación.", "Excepto en los procesos de promoción interna."],
  "Art. 61.8 TREBEP.", "excepto cuando así lo prevea la propia convocatoria")
P("RDL6", "Artículo 114", "Sistemas selectivos", "Según el artículo 114.7 del Real Decreto-ley 6/2023, en el sistema de concurso-oposición, para la valoración de la fase de concurso será necesario:",
  ["Haber superado la fase de oposición.", "Haber superado el curso selectivo.", "Acreditar al menos dos años de servicios previos.", "Haber obtenido la puntuación máxima en la fase de oposición."],
  "Art. 114.7 RDL 6/2023.", "Para la valoración de la fase de concurso será necesario haber superado la fase de oposición")
P("RDL6", "Artículo 114", "Sistemas selectivos", "Según el artículo 114.12 del Real Decreto-ley 6/2023, la toma de posesión del personal funcionario de carrera se deberá efectuar dentro del plazo de:",
  ["Quince días naturales a partir de la publicación del nombramiento, que será de un mes cuando suponga cambio de localidad de residencia.", "Un mes a partir de la publicación del nombramiento, en todo caso.", "Tres días hábiles, o un mes si implica cambio de residencia.", "Veinte días naturales desde el día siguiente al del nombramiento."],
  "Art. 114.12 RDL 6/2023.", "dentro del plazo de quince días naturales a partir de la publicación del nombramiento, que será de un mes cuando suponga cambio de localidad de residencia")
P("RD364", "Artículo 4", "Sistemas selectivos", "Según el artículo 4.1 del Real Decreto 364/1995, el sistema ordinario de ingreso del personal funcionario será:",
  ["La oposición.", "El concurso-oposición.", "El concurso.", "La libre designación."],
  "Art. 4.1 RD 364/1995.", "La oposición será el sistema ordinario de ingreso")
P("RD364", "Artículo 16", "Procedimiento selectivo", "Según el artículo 16 j) del Real Decreto 364/1995, desde la total conclusión de un ejercicio o prueba hasta el comienzo del siguiente deberá transcurrir un plazo:",
  ["Mínimo de setenta y dos horas y máximo de cuarenta y cinco días naturales.", "Mínimo de cuarenta y ocho horas y máximo de treinta días naturales.", "Mínimo de veinticuatro horas y máximo de dos meses.", "Mínimo de setenta y dos horas y máximo de cuarenta y cinco días hábiles."],
  "Art. 16 j) RD 364/1995.", "un plazo mínimo de setenta y dos horas y máximo de cuarenta y cinco días naturales")
P("RD364", "Artículo 18", "Procedimiento selectivo", "Según el artículo 18.1 del Real Decreto 364/1995, la solicitud para participar en los procedimientos de ingreso deberá presentarse en el plazo de:",
  ["Veinte días naturales a partir del siguiente al de publicación de la convocatoria en el BOE.", "Veinte días hábiles a partir del siguiente al de publicación de la convocatoria en el BOE.", "Un mes a partir de la publicación de la convocatoria en el BOE.", "Diez días hábiles a partir de la publicación de la convocatoria en el BOE."],
  "Art. 18.1 RD 364/1995.", "deberá presentarse en el plazo de veinte días naturales a partir del siguiente al de publicación de la convocatoria respectiva")
P("RD364", "Artículo 20", "Procedimiento selectivo", "Según el artículo 20.1 del Real Decreto 364/1995, en la resolución que aprueba la lista de admitidos y excluidos se señalará un plazo para subsanación de:",
  ["Diez días hábiles.", "Diez días naturales.", "Veinte días naturales.", "Quince días hábiles."],
  "Art. 20.1 RD 364/1995.", "señalándose un plazo de diez días hábiles para subsanación")
P("RD364", "Artículo 25", "Procedimiento selectivo", "Según el artículo 25.1 del Real Decreto 364/1995, los aspirantes que hubieran superado el proceso selectivo serán nombrados funcionarios de carrera por:",
  ["El Secretario de Estado para la Administración Pública.", "El Subsecretario del Departamento convocante.", "El Consejo de Ministros.", "El Presidente del Tribunal calificador."],
  "Art. 25.1 RD 364/1995 (también art. 6.3 RD 2169/1984).", "serán nombrados funcionarios de carrera por el Secretario de Estado para la Administración Pública")
P("RD364", "Artículo 30", "Procedimiento selectivo", "Según el artículo 30 del Real Decreto 364/1995, los órganos de selección del personal laboral deberán estar formados por un número impar de miembros, de los cuales:",
  ["Uno, al menos, será designado a propuesta de la representación de los trabajadores.", "La mayoría serán designados a propuesta de la representación de los trabajadores.", "Ninguno podrá ser designado a propuesta de la representación de los trabajadores.", "Todos serán funcionarios de carrera del mismo Cuerpo."],
  "Art. 30 RD 364/1995.", "uno de los cuales, al menos, será designado a propuesta de la representación de los trabajadores")
P("RD364", "Artículo 33", "Procedimiento selectivo", "Según el artículo 33.2 del Real Decreto 364/1995, el personal seleccionado adquirirá la condición de personal laboral fijo:",
  ["Transcurrido el período de prueba que se determine en cada convocatoria, si lo supera satisfactoriamente.", "Con la firma del contrato de trabajo.", "Con la publicación de la relación de aprobados en el BOE.", "Al superar el curso selectivo en el INAP."],
  "Art. 33.2 RD 364/1995.", "Transcurrido el período de prueba que se determine en cada convocatoria, el personal que lo supere satisfactoriamente adquirirá la condición de personal laboral fijo")
P("TREBEP", "Artículo 100", "Competencias", "Según el artículo 100.2 del TREBEP, la Comisión de Coordinación del Empleo Público es:",
  ["Un órgano técnico y de trabajo dependiente de la Conferencia Sectorial de Administración Pública.", "Un órgano consultivo dependiente del Consejo de Estado.", "Un órgano de negociación colectiva con las organizaciones sindicales.", "Un órgano colegiado dependiente de la Comisión Superior de Personal."],
  "Art. 100.2 TREBEP.", "como órgano técnico y de trabajo dependiente de la Conferencia Sectorial de Administración Pública")
P("L30", "Artículo tres", "Competencias", "Según el artículo 3.2 de la Ley 30/1984, corresponde en particular al Gobierno:",
  ["Aprobar la oferta de empleo de la Administración del Estado.", "Nombrar a los funcionarios de carrera.", "Conceder los permisos y licencias de los funcionarios.", "Convocar los concursos de provisión de puestos de trabajo."],
  "Art. 3.2 g) Ley 30/1984.", "Aprobar la oferta de empleo de la Administración del Estado")
P("L30", "Artículo cinco", "Competencias", "Según el artículo 5 de la Ley 30/1984, corresponde al Ministro de Economía y Hacienda:",
  ["Autorizar cualquier medida relativa al personal que pueda suponer modificaciones en el gasto.", "Aprobar la oferta de empleo de la Administración del Estado.", "Dirigir la política de personal de la Administración del Estado.", "Nombrar a los funcionarios de carrera."],
  "Art. 5 Ley 30/1984.", "autorizar cualquier medida relativa al personal que pueda suponer modificaciones en el gasto")
P("RD2169", "Artículo 9", "Competencias", "Según el artículo 9 del Real Decreto 2169/1984, corresponde a los Ministros, en relación con los funcionarios destinados en su Departamento:",
  ["El ejercicio de las potestades disciplinarias, excepto la separación del servicio.", "El ejercicio de todas las potestades disciplinarias, incluida la separación del servicio.", "El nombramiento de los funcionarios de carrera.", "La aprobación de la oferta de empleo público."],
  "Art. 9.3 RD 2169/1984 (la separación la propone al Gobierno el Ministro de la Presidencia, según el art. 3.13).", "El ejercicio de las potestades disciplinarias, excepto la separación del servicio")
P("RD2169", "Artículo 11", "Competencias", "Según el artículo 11 del Real Decreto 2169/1984, corresponde a los Subsecretarios, respecto a los funcionarios destinados en los Servicios Centrales de los Ministerios:",
  ["El reconocimiento de trienios.", "La separación del servicio.", "El nombramiento de funcionarios de carrera.", "La aprobación de las relaciones de puestos de trabajo."],
  "Art. 11.6 RD 2169/1984.", "El reconocimiento de trienios")
P("RD2169", "Artículo 13", "Competencias", "Según el artículo 13 del Real Decreto 2169/1984, el nombramiento y cese del personal eventual corresponde a:",
  ["Los Ministros y los Secretarios de Estado.", "Los Subsecretarios.", "El Consejo de Ministros.", "El Director general de la Función Pública."],
  "Art. 13 RD 2169/1984.", "Corresponde a los Ministros y a los Secretarios de Estado el nombramiento y cese del personal eventual")
T.real("L", 65, "Oferta de empleo público"); T.real("X", 72, "Oferta de empleo público"); T.real("X", 75, "Oferta de empleo público")
T.real("X", 70, "Selección"); T.real("X", 81, "Sistemas selectivos"); T.real("L", 66, "Planificación")

# Flashcards
for q_, a_, cat in [
  ("Objetivo de la planificación de recursos humanos (TREBEP, art. 69.1)", "Eficacia en la prestación de los servicios y eficiencia en la utilización de los recursos económicos disponibles.", "Planificación"),
  ("¿Cómo se fijan los contenidos mínimos comunes de los Registros de personal? (TREBEP, art. 71.3)", "Mediante convenio de Conferencia Sectorial.", "Planificación"),
  ("Planificación estratégica en la AGE (RDL 6/2023, art. 107)", "Escenario plurianual de empleo público, periódicamente revisable; planes generales y específicos; negociación colectiva previa y evaluación posterior.", "Planificación"),
  ("¿A qué se adscriben con carácter general los puestos de trabajo? (RDL 6/2023, art. 110.3)", "A una o varias áreas funcionales.", "Planificación"),
  ("¿Qué recoge la oferta de empleo público? (TREBEP, art. 70.1)", "Las necesidades de recursos humanos con asignación presupuestaria que deban cubrirse con personal de nuevo ingreso; obliga a convocar las plazas y hasta un 10 % adicional.", "Oferta de empleo público"),
  ("Plazo de ejecución de la oferta (TREBEP, art. 70.1)", "Tres años, improrrogable.", "Oferta de empleo público"),
  ("Plazos de las convocatorias en la AGE (RDL 6/2023, art. 108.2)", "Publicación en el mismo año natural que la oferta; ejecución en dos años desde su publicación y fase de oposición en un año, salvo causa justificada.", "Oferta de empleo público"),
  ("Cupos de la oferta en la AGE (RDL 6/2023, art. 108.3 y 4)", "Promoción interna: no menos del 30 % de las plazas de acceso libre. Discapacidad: no menos del 10 % de las plazas convocadas (al menos 2 % intelectual).", "Oferta de empleo público"),
  ("¿Quién aprueba la oferta de empleo de la AGE y cuándo? (RD 364/1995, art. 8)", "El Gobierno, en el primer trimestre de cada año.", "Oferta de empleo público"),
  ("Principios del art. 55.2 TREBEP", "Publicidad de convocatorias y bases; transparencia; imparcialidad y profesionalidad de los miembros; independencia y discrecionalidad técnica; adecuación de los procesos a las funciones; agilidad sin perjuicio de la objetividad.", "Selección"),
  ("Requisitos generales de acceso (TREBEP, art. 56.1)", "Nacionalidad (salvo art. 57); capacidad funcional; 16 años y no exceder la edad de jubilación forzosa; no separado ni inhabilitado; titulación.", "Selección"),
  ("¿Quiénes no pueden formar parte de los órganos de selección? (TREBEP, art. 60.2)", "Personal de elección o designación política, funcionarios interinos y personal eventual (en la AGE, además, altos cargos y laborales no fijos: RDL 6/2023, art. 115.2).", "Órganos de selección"),
  ("Composición de los Tribunales (RD 364/1995, art. 11)", "Número impar de miembros, funcionarios de carrera, no inferior a cinco, con igual número de suplentes y titulación igual o superior a la exigida.", "Órganos de selección"),
  ("Sistemas selectivos de funcionarios de carrera (TREBEP, art. 61.6)", "Oposición y concurso-oposición; el concurso, solo por ley y con carácter excepcional.", "Sistemas selectivos"),
  ("Sistemas selectivos de personal laboral fijo (TREBEP, art. 61.7)", "Oposición, concurso-oposición o concurso de valoración de méritos.", "Sistemas selectivos"),
  ("Plazos del procedimiento de ingreso en la AGE (RD 364/1995)", "Solicitudes: 20 días naturales; lista de admitidos: máximo un mes; subsanación: 10 días hábiles; entre ejercicios: 72 horas a 45 días naturales; documentación: 20 días naturales.", "Procedimiento selectivo"),
  ("Toma de posesión del funcionario de carrera (RDL 6/2023, art. 114.12)", "15 días naturales desde la publicación del nombramiento; un mes si supone cambio de localidad de residencia. Interinos y eventuales: al día siguiente.", "Procedimiento selectivo"),
  ("¿Quién nombra a los funcionarios de carrera de la AGE?", "El Secretario de Estado para la Administración Pública (RD 364/1995, art. 25; RD 2169/1984, art. 6.3).", "Competencias"),
  ("Competencias del Gobierno en personal (Ley 30/1984, art. 3)", "Dirige la política de personal, ejerce la función ejecutiva y la potestad reglamentaria en función pública; aprueba la oferta de empleo; fija directrices retributivas; aprueba la estructura en grados.", "Competencias"),
  ("Potestad disciplinaria de los Ministros (RD 2169/1984, art. 9.3)", "Todas las potestades disciplinarias excepto la separación del servicio, que acuerda el Gobierno a propuesta del Ministro (art. 3.13).", "Competencias"),
  ("Comisión de Coordinación del Empleo Público (TREBEP, art. 100.2)", "Órgano técnico y de trabajo dependiente de la Conferencia Sectorial de Administración Pública; coordina la política de personal entre Administraciones.", "Competencias"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Planes para la ordenación de los recursos humanos", "Instrumentos potestativos de planificación de cada Administración, con medidas de análisis de necesidades, organización, movilidad, promoción, formación y previsión de la oferta (TREBEP, art. 69.2).", "s1", "Planificación")
T.glos("Registro Central de Personal", "Registro de la Administración del Estado, en la Dirección General de la Función Pública, en el que se inscribe a todo su personal y se anotan los actos que afectan a su vida administrativa (Ley 30/1984, art. 13.1).", "s1", "Planificación")
T.glos("Planificación estratégica de los recursos humanos", "Fundamento de actuación en función pública de la Administración del Estado: escenario plurianual de empleo público, revisable, con planes generales y específicos (RDL 6/2023, art. 107).", "s2", "Planificación")
T.glos("Área funcional", "Ámbito al que, con carácter general, se adscriben los puestos de trabajo para facilitar su gestión, las competencias y la formación (RDL 6/2023, art. 110.3).", "s2", "Planificación")
T.glos("Oferta de empleo público", "Instrumento, aprobado anualmente por los órganos de Gobierno, que recoge las necesidades de personal de nuevo ingreso con asignación presupuestaria y obliga a convocar los procesos selectivos (TREBEP, art. 70).", "s3", "Oferta de empleo público")
T.glos("Discrecionalidad técnica", "Margen de los órganos de selección en la valoración, garantizado junto con su independencia (TREBEP, art. 55.2 d); la motivación de esos actos se refiere a las normas y bases (RD 364/1995, art. 22.2).", "s5", "Selección")
T.glos("Órgano de selección", "Órgano colegiado que desarrolla y califica los procesos selectivos; sus miembros actúan a título individual (TREBEP, art. 60). En la AGE: Tribunales y Comisiones Permanentes de Selección (RD 364/1995, art. 10).", "s6", "Órganos de selección")
T.glos("Oposición", "Sistema selectivo de una o más pruebas de conocimientos, competencias o habilidades para determinar la capacidad y fijar el orden de prelación (RDL 6/2023, art. 114.5).", "s7", "Sistemas selectivos")
T.glos("Concurso", "Sistema selectivo que consiste exclusivamente en la valoración de méritos conforme a baremo; para funcionarios, solo excepcionalmente y por ley (TREBEP, art. 61.6; RDL 6/2023, art. 114.6).", "s7", "Sistemas selectivos")
T.glos("Concurso-oposición", "Celebración sucesiva de concurso y oposición; la fase de concurso es proporcionada y solo se valora a quien supera la oposición (RDL 6/2023, art. 114.7).", "s7", "Sistemas selectivos")
T.glos("Relación complementaria", "Relación de aspirantes que siguen a los propuestos, que el órgano convocante puede pedir si hay renuncias, para su posible nombramiento (TREBEP, art. 61.8; RDL 6/2023, art. 114.10).", "s8", "Procedimiento selectivo")
T.glos("Funcionario en prácticas", "Condición del aspirante durante el curso selectivo o periodo de prácticas (RDL 6/2023, art. 114.8; RD 364/1995, art. 24).", "s8", "Procedimiento selectivo")
T.glos("Comisión de Coordinación del Empleo Público", "Órgano técnico y de trabajo dependiente de la Conferencia Sectorial de Administración Pública que coordina la política de personal entre Administraciones (TREBEP, art. 100.2).", "s10", "Competencias")

# Cronología (fechas de los metadatos del BOE)
T.hito("1984", "Ley 30/1984, de 2 de agosto, de medidas para la reforma de la Función Pública (BOE de 3-8-1984)", "Arts. 3 a 5, 9 y 13: órganos superiores de la función pública y Registro Central de Personal", "normativo", "s11")
T.hito("1984", "Real Decreto 2169/1984, de 28 de noviembre, de atribución de competencias en materia de personal (BOE de 7-12-1984)", "Reparto de competencias entre Gobierno, Ministros, Secretario de Estado, Subsecretarios y Director general de la Función Pública", "normativo", "s12")
T.hito("1995", "Real Decreto 364/1995, de 10 de marzo, Reglamento General de Ingreso del personal al servicio de la AGE (BOE de 10-4-1995)", "Oferta, órganos de selección, convocatorias y nombramiento en la AGE", "normativo", "s8")
T.hito("2015", "Real Decreto Legislativo 5/2015, de 30 de octubre, texto refundido del Estatuto Básico del Empleado Público (BOE de 31-10-2015)", "Arts. 55 a 61 (acceso) y 69 a 71 (planificación y oferta)", "normativo", "s3")
T.hito("2023", "Real Decreto-ley 6/2023, de 19 de diciembre (BOE de 20-12-2023)", "Libro segundo: planificación estratégica, oferta de empleo y acceso en la Administración del Estado", "normativo", "s2")

T.publicar()
