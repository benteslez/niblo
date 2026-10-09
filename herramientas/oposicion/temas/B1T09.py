# -*- coding: utf-8 -*-
"""Tema I.9 (B1T09): El sector público institucional: entidades que lo integran y
régimen jurídico.
Método del I.2: mapa → bloques (I a IV) con guía; cada artículo, texto literal del
BOE + ficha de casillas fijas; cierre 1 (preguntas oficiales) y cierre 2 (repaso).
Normas (textos consolidados del BOE): Ley 40/2015, de Régimen Jurídico del Sector
Público, arts. 2 y 81 a 139 (Título II); Ley 47/2003, General Presupuestaria, arts. 2
y 3 (clasificación); Ley 7/2025, de la Agencia Estatal de Salud Pública, arts. 1 y 2
(solo para la pregunta oficial relacionada)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO["L7_2025"] = "Ley 7/2025"

T = Tema("B1T09",
  "Cuatro preguntas: I. Qué es el sector público institucional y qué entidades lo integran (Ley 40/2015, arts. 2 y 84; Ley 47/2003, arts. 2 y 3) · II. Qué reglas comunes se aplican a todas (arts. 81 a 83 y 84 bis a 87) · III. Cómo son los organismos públicos: organismos autónomos, entidades públicas empresariales y agencias estatales (arts. 88 a 108 sexies) · IV. Cómo son las demás: autoridades administrativas independientes, sociedades mercantiles estatales, consorcios, fundaciones y fondos (arts. 109 a 114 y 116 a 139). Cada artículo: texto literal del BOE y ficha.",
  ["Ley 40/2015", "Sector público institucional", "Art. 84", "Inventario de Entidades", "Supervisión continua", "Medio propio", "Organismos públicos", "Organismo autónomo", "Entidad pública empresarial", "Agencia estatal", "Contrato de gestión", "Autoridad administrativa independiente", "Sociedad mercantil estatal", "Consorcio", "Fundación del sector público", "Fondos sin personalidad", "LGP art. 3"])

# =============================================================================
T.ap("s0", "Mapa del tema: cuatro preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque I, tema 9):
> 9. El sector público institucional: entidades que lo integran y régimen jurídico.

### El hilo conductor

El epígrafe se lee como **cuatro preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Ley 40/2015 | Otras normas |
|---|---|---|---|
| **I** | ¿Qué es el sector público institucional y qué entidades lo integran? | Arts. 2 y 84 | Ley 47/2003, General Presupuestaria, arts. 2 y 3 |
| **II** | ¿Qué reglas comunes se aplican a todas las entidades? | Arts. 81 a 83 y 84 bis a 87 | — |
| **III** | ¿Cómo son los organismos públicos? (organismos autónomos, entidades públicas empresariales y agencias estatales) | Arts. 88 a 108 sexies | — |
| **IV** | ¿Cómo son las demás entidades? (autoridades administrativas independientes, sociedades mercantiles estatales, consorcios, fundaciones y fondos sin personalidad) | Arts. 109 a 114 y 116 a 139 | — |

!> **La idea que une los cuatro bloques:** además de las Administraciones territoriales, el sector público tiene un **sector público institucional**: entidades creadas por ellas para fines concretos (I). Todas están sometidas a unas **reglas comunes**: principios, inventario, supervisión continua (II). En el Estado son una **lista cerrada** (art. 84): los **organismos públicos** (III), con régimen más o menos administrativo según el tipo, y otras entidades de derecho público o privado (IV). Para cada tipo hay que saber **qué es**, **cómo se crea**, **por qué derecho se rige** y **qué personal tiene**.

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen). En los artículos largos se copian solo los apartados que se citan; lo copiado es literal.
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- Fronteras con otros temas: la Administración General del Estado, sus órganos y su organización territorial (tema I.8); las Comunidades Autónomas (tema I.10) y la Administración local (tema I.11); los contratos del sector público (tema IV.5). Las relaciones interadministrativas (Título III de la Ley 40/2015, arts. 140 y siguientes) no forman parte de este epígrafe.

?> **Aviso sobre los nombres de los Ministerios.** La Ley 40/2015 se cita **literalmente**, como está en el BOE, con los nombres de Ministerios de cada redacción («Ministerio de Hacienda y Administraciones Públicas», «Ministerio de Hacienda y Función Pública», «Política Territorial y Función Pública»): así se preguntan en el examen. Hoy, según el Real Decreto 829/2023, de 20 de noviembre, por el que se reestructuran los departamentos ministeriales [[BOE|https://boe.es/buscar/act.php?id=BOE-A-2023-23537]] (no es norma del tema), la política en materia de {c('RD829_2023', 'Artículo 5', 'hacienda pública, de presupuestos y de gastos')} corresponde al Ministerio de Hacienda (art. 5.1) y la de {c('RD829_2023', 'Artículo 22', 'administración pública, función pública, y gobernanza pública')}, al {c('RD829_2023', 'Artículo 22', 'Ministerio para la Transformación Digital y de la Función Pública')} (art. 22.2) (→ tema I.8, aviso del mapa).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué es el sector público institucional y qué entidades lo integran? (Ley 40/2015, arts. 2 y 84; LGP, arts. 2 y 3)", donde(
  "Primera pregunta del tema. Antes de estudiar cada tipo de entidad hay que saber **dónde está** el sector público institucional dentro del sector público y **qué entidades** lo forman en el Estado.",
  ["1 El sector público y el sector público institucional (art. 2)", "2 El sector público institucional estatal: composición y lista cerrada (art. 84)", "3 La clasificación presupuestaria (LGP, arts. 2 y 3)", "4 Cuadro de las entidades y sus denominaciones"]))

T.ap("s1", "I.1 El sector público y el sector público institucional (Ley 40/2015, art. 2)", f"""
La Ley 40/2015 se aplica a todo el **sector público**: tres Administraciones territoriales y el **sector público institucional**.

{unidad("1.1 Qué comprende el sector público y qué integra el institucional (art. 2.1 y 2)",
  lit("L40", "a2", ["d) El sector público institucional.", "Cualesquiera organismos públicos y entidades de derecho público vinculados o dependientes de las Administraciones Públicas", "Las entidades de derecho privado vinculadas o dependientes de las Administraciones Públicas", "Las Universidades públicas"], solo=list(range(1, 10))),
  fichab("Ámbito subjetivo de la Ley 40/2015",
         ["::Sector público (2.1):", "Administración General del Estado", "Administraciones de las Comunidades Autónomas", "Entidades que integran la Administración Local", "Sector público institucional"],
         ["::Sector público institucional (2.2):", "Organismos públicos y entidades de **derecho público** vinculados o dependientes", "Entidades de **derecho privado** vinculadas o dependientes", "Universidades públicas"],
         "—",
         f"Las entidades de derecho privado quedan sujetas a la Ley en lo que se refiera a ellas, en particular a los principios del art. 3, y {c('L40', 'a2', 'en todo caso, cuando ejerzan potestades administrativas')}. Las Universidades públicas: normativa específica y, **supletoriamente**, la Ley 40/2015."))}

{unidad("1.2 Quiénes son Administraciones Públicas (art. 2.3)",
  lit("L40", "a2", ["los organismos públicos y entidades de derecho público previstos en la letra a) del apartado 2"], solo=[10]),
  fichab("Concepto legal de Administración Pública",
         "Las tres Administraciones territoriales y los organismos públicos y entidades de **derecho público** del sector público institucional",
         "—", "—",
         "Las entidades de **derecho privado** (sociedades, fundaciones) forman parte del sector público institucional, pero **no** son Administraciones Públicas según el art. 2.3."))}
""", 2)

T.ap("s2", "I.2 El sector público institucional estatal: composición y lista cerrada (art. 84)", f"""
{unidad("2.1 Qué entidades lo integran (art. 84.1 y 3)",
  lit("L40", "a84", ["Organismos autónomos.", "Entidades públicas empresariales.", "Agencias estatales.", "Las autoridades administrativas independientes.", "Las sociedades mercantiles estatales.", "Los consorcios.", "Las fundaciones del sector público.", "Los fondos sin personalidad jurídica.", "Las universidades públicas no transferidas."], solo=list(range(1, 12)) + [14]),
  fichab("Composición del sector público institucional estatal",
         "Entidades vinculadas o dependientes de la Administración General del Estado",
         ["::Siete grupos (84.1):", "a) **Organismos públicos**: organismos autónomos, entidades públicas empresariales y agencias estatales", "b) Autoridades administrativas independientes", "c) Sociedades mercantiles estatales", "d) Consorcios", "e) Fundaciones del sector público", "f) Fondos sin personalidad jurídica", "g) Universidades públicas no transferidas"],
         "—",
         "Los **organismos públicos** son solo **tres** clases (OA, EPE y agencias estatales). Las autoridades administrativas independientes, las sociedades, los consorcios y las fundaciones son **letras distintas**, no organismos públicos del art. 84.1 a)."))}

{unidad("2.2 Lista cerrada: no se pueden crear otros tipos (art. 84.2)",
  lit("L40", "a84", ["no podrá, por sí misma ni en colaboración con otras entidades públicas o privadas, crear, ni ejercer el control efectivo, directa ni indirectamente, sobre ningún otro tipo de entidad distinta de las enumeradas en este artículo"], solo=[12, 13]),
  fichab("Prohibición de crear o controlar entidades de otro tipo",
         "La Administración General del Estado y cualquier entidad del sector público institucional estatal",
         ["Ni crear ni ejercer el control efectivo, directo o indirecto, de entidades distintas de las del art. 84", "Excepciones: organismos internacionales o supranacionales, organismos de normalización y acreditación nacionales y sociedades de la Ley 27/1984"],
         "—",
         "La lista del 84.1 es **cerrada** («ningún otro tipo de entidad»), con las excepciones del párrafo segundo."))}
""", 2)

T.ap("s3", "I.3 La clasificación presupuestaria (Ley 47/2003, General Presupuestaria, arts. 2 y 3)", f"""
La Ley General Presupuestaria repite la composición del art. 84 a sus efectos y añade alguna entidad; además divide el sector público estatal en tres sectores (administrativo, empresarial y fundacional), que determinan el régimen presupuestario y contable.

{unidad("3.1 El sector público estatal a efectos de la LGP (art. 2)",
  lit("LGP", "a2", ["Los consorcios adscritos a la Administración General del Estado.", "Las fundaciones del sector público adscritas a la Administración General del Estado.", "mutuas colaboradoras con la Seguridad Social", "esta Ley no será de aplicación a las Cortes Generales"], solo=list(range(1, 19))),
  fichab("Ámbito de la Ley General Presupuestaria",
         "Administración General del Estado y sector público institucional estatal",
         ["Mismos grupos que el art. 84 de la Ley 40/2015, pero los **consorcios** y **fundaciones** solo si están **adscritos** a la Administración General del Estado", "Añade las entidades gestoras, servicios comunes y mutuas colaboradoras con la Seguridad Social, y cualesquiera organismos y entidades de derecho público vinculados o dependientes"],
         "—",
         "No se aplica a las **Cortes Generales**, que gozan de autonomía presupuestaria (art. 72 CE). Cayó en 2025 (→ Cierre 1)."))}

{unidad("3.2 Sector público administrativo, empresarial y fundacional (art. 3)",
  lit("LGP", "a3", ["El sector público administrativo", "El sector público empresarial", "El sector público fundacional"]),
  fichab("División del sector público estatal a efectos presupuestarios",
         "—",
         ["**Administrativo**: AGE, organismos autónomos, autoridades administrativas independientes, universidades no transferidas, entidades de la Seguridad Social y otros entes de derecho público, consorcios y fondos que no produzcan en régimen de mercado o no se financien mayoritariamente con ingresos comerciales", "**Empresarial**: entidades públicas empresariales, sociedades mercantiles estatales y el resto de entes de derecho público, consorcios y fondos", "**Fundacional**: fundaciones del sector público estatal"],
         "—",
         "Organismos autónomos → sector **administrativo**; entidades públicas empresariales y sociedades → sector **empresarial**; fundaciones → **fundacional**."))}
""", 2)

T.ap("s4", "I.4 Cuadro de las entidades y sus denominaciones (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Entidad (art. 84.1) | Naturaleza | Indicación obligatoria en el nombre | Artículo |
|---|---|---|---|
| Organismo autónomo | Derecho público | «organismo autónomo» u «O.A.» | 98.3 |
| Entidad pública empresarial | Derecho público | «entidad pública empresarial» o «E.P.E» | 103.3 |
| Agencia estatal | Derecho público | «Agencia Estatal» | 108 bis.2 |
| Autoridad administrativa independiente | Derecho público | «autoridad administrativa independiente» o «A.A.I.» | 109.3 |
| Sociedad mercantil estatal | Sociedad mercantil | «sociedad mercantil estatal» o «S.M.E.» | 111.2 |
| Consorcio | Derecho público | «consorcio» o «C» | 118.4 |
| Fundación del sector público | Fundación | «fundación del sector público» o «F.S.P.» | 128.2 |
| Fondo carente de personalidad jurídica | Sin personalidad | «fondo carente de personalidad jurídica» o «F.C.P.J» | 137.3 |
| Entidad que sea medio propio | — | «Medio Propio» o «M.P.» | 86.2 |

{resumen([
  "Sector público = AGE + CC. AA. + Administración Local + **sector público institucional** (art. 2.1).",
  "Son **Administraciones Públicas** los organismos públicos y entidades de **derecho público**; no las de derecho privado (art. 2.3).",
  "En el Estado, **lista cerrada** del art. 84: tres clases de **organismos públicos** (OA, EPE, agencias estatales) y otras seis letras.",
  "LGP: sector público **administrativo**, **empresarial** y **fundacional** (art. 3); no se aplica a las **Cortes Generales** (art. 2.3)."],
  "Siguiente: II. ¿Qué reglas comunes se aplican a todas las entidades?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Qué reglas comunes se aplican a todas las entidades? (arts. 81 a 83 y 84 bis a 87)", donde(
  "Segunda pregunta. Antes de los tipos, la Ley fija unas **reglas comunes**: principios de actuación, un **inventario** público de todas las entidades, la **supervisión continua**, la condición de **medio propio** y las **transformaciones**.",
  ["1 Principios y supervisión continua (art. 81)", "2 El Inventario de Entidades del Sector Público (arts. 82 y 83)", "3 Presencia equilibrada y control de eficacia (arts. 84 bis y 85)", "4 Medio propio y transformaciones (arts. 86 y 87)"]))

T.ap("s5", "II.1 Principios generales y supervisión continua (art. 81)", f"""
{unidad("1.1 Principios de actuación y normas aplicables a autonómicas y locales (art. 81)",
  lit("L40", "a81", ["legalidad, eficiencia, estabilidad presupuestaria y sostenibilidad financiera así como al principio de transparencia", "sistema de supervisión continua", "Capítulos I y VI y en los artículos 129 y 134"]),
  fichab("Reglas comunes a todo el sector público institucional (estatal, autonómico y local)",
         "Todas las entidades del sector público institucional; todas las Administraciones Públicas (supervisión de sus entidades dependientes)",
         ["Principios: legalidad, eficiencia, estabilidad presupuestaria, sostenibilidad financiera y transparencia", "Personal (incluido el laboral): sujeto a las limitaciones de la normativa presupuestaria", "Supervisión continua: comprobar si subsisten los motivos de la creación y la sostenibilidad financiera, con propuestas de mantenimiento, transformación o extinción"],
         "—",
         "Para las entidades autonómicas y locales son **básicos** los Capítulos **I y VI** (sector público institucional en general y consorcios) y los arts. **129 y 134** (adscripción y protectorado de fundaciones)."))}
""", 2)

T.ap("s6", "II.2 El Inventario de Entidades del Sector Público Estatal, Autonómico y Local (arts. 82 y 83)", f"""
{unidad("2.1 Qué es y quién lo gestiona (art. 82)",
  lit("L40", "a82", ["registro público administrativo", "dependerá de la Intervención General de la Administración del Estado", "la creación, transformación, fusión o extinción"]),
  fichab("Registro de todas las entidades del sector público institucional, de cualquier naturaleza jurídica",
         f"Integración, gestión y publicación: {c('L40', 'a82', 'Intervención General de la Administración del Estado')}",
         ["Contenido mínimo: naturaleza jurídica, finalidad, financiación, estructura de dominio, condición de medio propio, regímenes de contabilidad, presupuestario y de control, y clasificación en contabilidad nacional", "Se inscriben, al menos, la creación, transformación, fusión o extinción"],
         "—",
         "Es un registro **público** administrativo y depende de la **IGAE** (no de la AIReF ni del Tribunal de Cuentas). Cayó en 2025 (→ Cierre 1)."))}

{unidad("2.2 Inscripción (art. 83)",
  lit("L40", "a83", ["en el plazo de treinta días hábiles a contar desde que ocurra el acto inscribible", "dentro del plazo de 15 días hábiles siguientes a la recepción de la solicitud de inscripción", "Número de Identificación Fiscal definitivo"]),
  fichab("Cómo se inscriben los actos de la entidad",
         "Notifica el titular del **máximo órgano de dirección** de la entidad, a través de la intervención general de la Administración correspondiente",
         ["Notificación (electrónica para la creación) con la documentación justificativa", "Sin la certificación de la inscripción no se asigna el NIF definitivo"],
         ["Notificar: **30 días hábiles** desde el acto (o desde la entrada en vigor de la norma o acto de creación)", "Inscribir: **15 días hábiles** desde la recepción de la solicitud"],
         "**30** días hábiles para notificar; **15** días hábiles para inscribir. La inscripción es requisito para el **NIF definitivo**."))}
""", 2)

T.ap("s7", "II.3 Presencia equilibrada y control de eficacia y supervisión continua (arts. 84 bis y 85)", f"""
{unidad("3.1 Presencia equilibrada entre mujeres y hombres (art. 84 bis)",
  lit("L40", "a8-2", ["no superen el sesenta por ciento ni sean menos del cuarenta por ciento", "órganos colegiados de gobierno"]),
  fichab("Representación equilibrada en la dirección de las entidades estatales",
         "Presidencias, vicepresidencias, direcciones generales, direcciones ejecutivas y asimilados que sean máximos responsables; contratos de alta dirección; órganos colegiados de gobierno",
         "Ningún sexo por encima del 60 % ni por debajo del 40 %, en el ámbito de cada entidad",
         "60 % / 40 %",
         "Se mide **en cada entidad**. Se aplica también a los **órganos colegiados de gobierno**."))}

{unidad("3.2 Control de eficacia y supervisión continua (art. 85)",
  lit("L40", "a85", ["se revisarán cada tres años", "será ejercido por el Departamento al que estén adscritos, a través de las inspecciones de servicios", "a través de la Intervención General de la Administración del Estado"], solo=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  fichab("Dos controles sobre todas las entidades estatales",
         ["**Control de eficacia**: el Departamento de adscripción, a través de las inspecciones de servicios", "**Supervisión continua**: el Ministerio de Hacienda, a través de la IGAE"],
         ["Plan de actuación desde la creación, con planes anuales", "Supervisión: subsistencia de las circunstancias de la creación, sostenibilidad financiera y causa de disolución por incumplimiento de fines", "Ambos controles tienen en cuenta la información económico-financiera, la que suministren las entidades y las propuestas de las inspecciones de servicios (85.4)", "Resultado: informe con recomendaciones de mejora o propuesta de transformación o supresión"],
         "Revisión del plan de actuación: **cada tres años**",
         "Eficacia → **Ministerio de adscripción** (inspecciones de servicios). Supervisión continua → **Hacienda/IGAE**, **desde la creación hasta la extinción**."))}
""", 2)

T.ap("s8", "II.4 Medio propio y servicio técnico; transformaciones (arts. 86 y 87)", f"""
{unidad("4.1 Medio propio y servicio técnico (art. 86)",
  lit("L40", "a86", ["Sea una opción más eficiente que la contratación pública", "Resulte necesario por razones de seguridad pública o de urgencia", "deberá ser informada por la Intervención General de la Administración del Estado"], solo=[1, 2, 3, 4, 5, 6, 7]),
  fichab("Entidades a las que se puede encargar prestaciones sin licitar",
         "Entidades del sector público institucional que cumplan la Ley 9/2017, de Contratos del Sector Público",
         ["Medios suficientes e idóneos en su sector de actividad", "Y además: opción **más eficiente** que la contratación pública, o necesaria por **seguridad pública** o **urgencia**", "La comprobación de esos requisitos forma parte del control de eficacia"],
         "—",
         "Un medio propio **nuevo** necesita memoria justificativa informada por la **IGAE**. En su denominación debe figurar «Medio Propio» o «M.P.» (→ I.4)."))}

{unidad("4.2 Transformaciones (art. 87)",
  lit("L40", "a87", ["podrá transformarse y adoptar la naturaleza jurídica de cualquiera de las entidades citadas", "conservando su personalidad jurídica", "La transformación se llevará a cabo mediante Real Decreto, aunque suponga modificación de la Ley de creación, salvo en el caso de la transformación en agencias estatales que deberá efectuarse por ley"], solo=list(range(1, 11))),
  fichab("Cambio de naturaleza jurídica de una entidad estatal",
         "Organismos autónomos, entidades públicas empresariales, agencias estatales, sociedades mercantiles estatales y fundaciones del sector público estatal",
         ["Conserva su personalidad jurídica: cesión e integración global del activo y del pasivo, con sucesión universal", "Con memoria (justificación, análisis de eficiencia y situación del personal) e informe preceptivo de la IGAE"],
         "Forma: **Real Decreto**, aunque modifique la ley de creación; en **agencia estatal**, por **ley**",
         "Regla: **Real Decreto**. Excepción: transformación **en agencia estatal**, **por ley**. La transformación no es causa de resolución de las relaciones jurídicas."))}

{resumen([
  "Principios: legalidad, eficiencia, estabilidad presupuestaria, sostenibilidad financiera y transparencia; **supervisión continua** de todas las entidades (art. 81).",
  "**Inventario** de Entidades: registro **público** administrativo gestionado por la **IGAE**; notificar en **30** días hábiles e inscribir en **15** (arts. 82 y 83).",
  "Presencia equilibrada **60/40** en cada entidad (art. 84 bis); control de eficacia (Ministerio de adscripción) y supervisión continua (Hacienda/IGAE) (art. 85).",
  "Medio propio: más eficiente o necesario por seguridad o urgencia (art. 86). Transformación por **Real Decreto**; en agencia estatal, por **ley** (art. 87)."],
  "Siguiente: III. ¿Cómo son los organismos públicos?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Cómo son los organismos públicos? (arts. 88 a 108 sexies)", donde(
  "Tercera pregunta. Los **organismos públicos** son la primera letra del art. 84: entidades de derecho público con personalidad propia. La Ley les da un régimen común (creación por ley, estatutos, disolución) y después regula sus tres clases.",
  ["1 Definición, potestades, creación y estatutos (arts. 88 a 93)", "2 Fusión, servicios comunes, disolución y liquidación (arts. 94 a 97)", "3 Organismos autónomos (arts. 98 a 102)", "4 Entidades públicas empresariales (arts. 103 a 108)", "5 Agencias estatales (arts. 108 bis a 108 sexies)", "6 Cuadro comparativo"]))

T.ap("s9", "III.1 Organismos públicos: definición, potestades, creación y estatutos (arts. 88 a 93)", f"""
{unidad("1.1 Definición y actividades (art. 88)",
  lit("L40", "a88", ["régimen de descentralización funcional o de independencia"]),
  fichab("Organismos públicos estatales",
         "Dependientes o vinculados a la Administración General del Estado, directamente o a través de otro organismo público",
         ["Actividades administrativas: fomento, prestación, gestión de servicios públicos o producción de bienes de interés público susceptibles de contraprestación", "Actividades de contenido económico reservadas a las Administraciones Públicas", "Supervisión o regulación de sectores económicos"],
         "—",
         "La razón de ser: **descentralización funcional** o **independencia**."))}

{unidad("1.2 Personalidad jurídica y potestades (art. 89)",
  lit("L40", "a89", ["personalidad jurídica pública diferenciada, patrimonio y tesorería propios, así como autonomía de gestión", "salvo la potestad expropiatoria"]),
  fichab("Qué tienen y qué pueden hacer",
         "Cada organismo público",
         ["Personalidad jurídica pública diferenciada, patrimonio y tesorería propios, autonomía de gestión", "Las potestades administrativas precisas para sus fines, según sus estatutos", "Los estatutos pueden atribuirles la ordenación de aspectos secundarios del funcionamiento", "Sus actos en ejercicio de potestades: recursos administrativos de la Ley 39/2015"],
         "—",
         "Tienen todas las potestades precisas **salvo la expropiatoria**."))}

{unidad("1.3 Estructura organizativa (art. 90.1)",
  lit("L40", "a90", ["Los máximos órganos de gobierno son el Presidente y el Consejo Rector"], solo=[1, 2, 3]),
  fichab("Órganos de los organismos públicos",
         "Órganos de gobierno y ejecutivos que fije el Estatuto",
         "Máximos órganos de gobierno: **Presidente** y **Consejo Rector** (el estatuto puede prever otros)",
         "—",
         "La clasificación de las entidades en **tres grupos** (número máximo de miembros de los órganos de gobierno, directivos y retribuciones) corresponde al Ministro de Hacienda (90.2)."))}

{unidad("1.4 Creación por ley (art. 91)",
  lit("L40", "a91", ["La creación de los organismos públicos se efectuará por Ley", "una propuesta de estatutos y de un plan inicial de actuación"]),
  fichab("Cómo nace un organismo público",
         "Las Cortes, por **ley**; el anteproyecto se eleva al Consejo de Ministros",
         ["La ley fija: tipo de organismo, fines generales y Departamento de dependencia o vinculación; en su caso, recursos y peculiaridades que exijan rango de ley", "El anteproyecto va con propuesta de estatutos, plan inicial de actuación e informe preceptivo favorable de Hacienda"],
         "—",
         "Organismo público → **ley**. Sus **estatutos** → **Real Decreto** (→ III.1.6)."))}

{unidad("1.5 El plan de actuación (art. 92.2)",
  lit("L40", "a92", ["deberá ser aprobado en el último trimestre del año natural", "cada tres años", "paralización de las transferencias"], solo=[7, 8]),
  fichab("Plan inicial y planes anuales de actuación",
         "Aprueba el plan anual el departamento del que dependa o al que esté vinculado el organismo",
         "El plan inicial se actualiza cada año; cada tres años, revisión de la programación estratégica",
         ["Plan anual: aprobado en el **último trimestre** del año natural", "Revisión estratégica: **cada tres años**"],
         "Sin plan anual por causa imputable al organismo → **paralización de las transferencias** de los Presupuestos Generales del Estado, salvo otra decisión del Consejo de Ministros."))}

{unidad("1.6 Estatutos (art. 93)",
  lit("L40", "a93", ["se aprobarán por Real Decreto del Consejo de Ministros a propuesta conjunta del Ministerio de Hacienda y Administraciones Públicas y del Ministerio al que el organismo esté vinculado o sea dependiente", "con carácter previo a la entrada en funcionamiento efectivo"]),
  fichab("Norma de organización de cada organismo",
         "Consejo de Ministros, por **Real Decreto**, a propuesta **conjunta** de Hacienda y del Ministerio de vinculación o dependencia",
         ["Contenido mínimo: funciones y potestades; estructura y actos que agotan la vía administrativa; patrimonio y recursos; régimen de personal, patrimonio, presupuesto y contratación; participación en sociedades mercantiles si es imprescindible"],
         "Aprobados y publicados **antes** de la entrada en funcionamiento efectivo",
         "Propuesta **conjunta** (Hacienda + Ministerio de adscripción). Los estatutos dicen qué actos **agotan la vía administrativa**."))}
""", 2)

T.ap("s10", "III.2 Organismos públicos: fusión, servicios comunes, disolución y liquidación (arts. 94 a 97)", f"""
{unidad("2.1 Fusión (art. 94.1 y 2)",
  lit("L40", "a94", ["de la misma naturaleza jurídica", "La fusión se llevará a cabo mediante norma reglamentaria, aunque suponga modificación de la Ley de creación"], solo=[1, 2, 3]),
  fichab("Unión de organismos públicos",
         "Organismos públicos estatales **de la misma naturaleza jurídica**",
         ["Por extinción e integración en uno nuevo, o por absorción por uno existente", "Con un plan de redimensionamiento que acredite el ahorro"],
         "Forma: **norma reglamentaria**, aunque modifique la ley de creación",
         "Solo entre organismos **de la misma naturaleza**. Si nace un organismo nuevo, debe cumplir el art. 91.2."))}

{unidad("2.2 Gestión compartida de servicios comunes (art. 95)",
  lit("L40", "a95", ["Gestión de bienes inmuebles.", "Asistencia jurídica.", "Publicaciones.", "Contratación pública."]),
  fichab("Servicios que los organismos públicos comparten",
         "Coordina el Ministerio de adscripción, el Ministerio de Hacienda o un organismo público dependiente de este",
         ["La norma de creación incluye la gestión compartida, salvo justificación por eficiencia, seguridad nacional o independencia del organismo", "::Servicios comunes, al menos:", "Gestión de bienes inmuebles", "Sistemas de información y comunicación", "Asistencia jurídica", "Contabilidad y gestión financiera", "Publicaciones", "Contratación pública"],
         "—",
         "Seis servicios comunes «al menos». Los distractores cambian una palabra: bienes **inmuebles** (no muebles), asistencia **jurídica** (no técnica), contratación **pública** (no privada). Cayó en 2025 (→ Cierre 1)."))}

{unidad("2.3 Disolución (art. 96)",
  lit("L40", "a96", ["Cuando así lo acuerde el Consejo de Ministros", "en el plazo de dos meses desde que concurra la causa de disolución", "quedará automáticamente disuelto"]),
  fichab("Fin de un organismo público",
         ["El titular del máximo órgano de dirección comunica la causa al titular del departamento de adscripción", "El Consejo de Ministros acuerda la disolución y designa liquidador"],
         ["::Causas (96.1):", "Transcurso del tiempo señalado en la ley de creación", "Asunción de todos sus fines por servicios de la AGE", "Cumplimiento total de sus fines", "Incumplimiento de fines o no ser el medio más idóneo (control de eficacia o supervisión continua)", "Causa de los estatutos", "Acuerdo del Consejo de Ministros"],
         ["Comunicación: **dos meses** desde que concurra la causa", "Acuerdo del Consejo de Ministros: **dos meses** desde la comunicación"],
         "Si pasan los plazos sin comunicación o sin acuerdo publicado, el organismo queda **automáticamente disuelto**."))}

{unidad("2.4 Liquidación y extinción (art. 97)",
  lit("L40", "a97", ["se entenderá automáticamente iniciada la liquidación", "que le sucederá universalmente en todos sus derechos y obligaciones", "se producirá su extinción automática"], solo=[1, 2, 4, 5]),
  fichab("Liquidación del organismo disuelto",
         "El órgano o entidad designado liquidador; sucede la **Administración General del Estado**",
         "Cesión e integración global del activo y el pasivo en la AGE, que se subroga en las relaciones con los acreedores",
         "—",
         "Disolución → liquidación **automática** → extinción **automática** al formalizarse la liquidación."))}
""", 2)

T.ap("s11", "III.3 Organismos autónomos estatales (arts. 98 a 102)", f"""
{unidad("3.1 Definición (art. 98)",
  lit("L40", "a98", ["entidades de derecho público, con personalidad jurídica propia, tesorería y patrimonio propios y autonomía en su gestión", "organizaciones instrumentales diferenciadas y dependientes", "«O.A.»"]),
  fichab("Organismo público con actividades propias de la Administración",
         "Dependen de la Administración General del Estado, que tiene su dirección estratégica, la evaluación de resultados y el control de eficacia",
         "Fomento, prestacionales, gestión de servicios públicos o producción de bienes de interés público susceptibles de contraprestación",
         "—",
         "Son «organizaciones instrumentales **diferenciadas y dependientes**». En el nombre: «organismo autónomo» u «O.A.»."))}

{unidad("3.2 Régimen jurídico (art. 99)",
  lit("L40", "a99", ["en su ley de creación", "normas de derecho administrativo general y especial", "En defecto de norma administrativa, se aplicará el derecho común"]),
  fichab("Derecho que se aplica a los organismos autónomos",
         "—",
         ["Ley 40/2015, su ley de creación y sus estatutos", "Ley de Procedimiento Administrativo Común, Real Decreto Legislativo 3/2011 y Ley 33/2003", "El resto del **derecho administrativo** general y especial", "Supletoriamente: el derecho común"],
         "—",
         "Régimen **administrativo**; el derecho común, solo **en defecto** de norma administrativa. Cayó en 2025 (→ Cierre 1)."))}

{unidad("3.3 Personal y contratación (art. 100)",
  lit("L40", "a100", ["será funcionario o laboral", "El titular del máximo órgano de dirección del organismo autónomo será el órgano de contratación"]),
  fichab("Personal y contratación de los organismos autónomos",
         "Personal **funcionario o laboral**; órgano de contratación: el titular del **máximo órgano de dirección**",
         ["Personal: Ley 7/2007, de 12 de abril, y demás normativa de funcionarios, y normativa laboral", "Nombramientos de titulares de órganos: normas de la AGE", "Instrucciones de recursos humanos del Ministerio de Hacienda"],
         "—",
         "Personal **funcionario o laboral** (las entidades públicas empresariales, laboral: → III.4.4)."))}

{unidad("3.4 Patrimonio y recursos (art. 101)",
  lit("L40", "a101", ["Las consignaciones específicas que tuvieren asignadas en los presupuestos generales del Estado", "Las donaciones, legados, patrocinios"]),
  fichab("Patrimonio y financiación",
         "—",
         ["Patrimonio propio, distinto del de la Administración; gestión según la Ley 33/2003", "Recursos: patrimonio y sus rentas, consignaciones en los Presupuestos Generales del Estado, transferencias, donaciones y legados, y cualquier otro autorizado"],
         "—",
         "Las **consignaciones de los Presupuestos** son recurso ordinario del organismo autónomo; en las entidades públicas empresariales, solo excepcionalmente (→ III.4.5)."))}

{unidad("3.5 Presupuesto, contabilidad y control (art. 102)",
  lit("L40", "a102", ["Ley 47/2003, de 26 de noviembre"]),
  fichab("Régimen presupuestario", "—", "El de la **Ley General Presupuestaria**", "—",
         "Forman parte del sector público **administrativo** (LGP, art. 3; → I.3.2)."))}
""", 2)

T.ap("s12", "III.4 Entidades públicas empresariales de ámbito estatal (arts. 103 a 108)", f"""
{unidad("4.1 Definición (art. 103)",
  lit("L40", "a103", ["con personalidad jurídica propia, patrimonio propio y autonomía en su gestión, que se financian con ingresos de mercado", "junto con el ejercicio de potestades administrativas", "«E.P.E»"]),
  fichab("Organismo público con actividad susceptible de contraprestación financiado con ingresos de mercado",
         "Dependen de la AGE **o de un organismo autónomo** vinculado o dependiente de ella",
         ["Ejercen potestades administrativas y desarrollan actividades prestacionales, de gestión de servicios o de producción de bienes de interés público, susceptibles de contraprestación", "Se financian con ingresos de mercado (salvo los medios propios personificados)"],
         "—",
         "Personalidad jurídica propia, **patrimonio propio** y autonomía de gestión; se financian con **ingresos de mercado**, no mayoritariamente con los Presupuestos. Cayó en 2025 (→ Cierre 1)."))}

{unidad("4.2 Régimen jurídico (art. 104)",
  lit("L40", "a104", ["se rigen por el Derecho privado, excepto en la formación de la voluntad de sus órganos, en el ejercicio de las potestades administrativas que tengan atribuidas"]),
  fichab("Derecho que se aplica a las entidades públicas empresariales",
         "—",
         ["Regla: **Derecho privado**", "::Excepciones (derecho administrativo):", "Formación de la voluntad de sus órganos", "Ejercicio de las potestades administrativas atribuidas", "Aspectos regulados en la Ley 40/2015, su ley de creación, estatutos y demás normas administrativas"],
         "—",
         "Al revés que el organismo autónomo (→ III.3.2): **Derecho privado** como regla, con excepciones de derecho administrativo."))}

{unidad("4.3 Ejercicio de potestades administrativas (art. 105)",
  lit("L40", "a105", ["sólo pueden ser ejercidas por aquellos órganos de éstas a los que los estatutos se les asigne expresamente esta facultad", "no son asimilables"]),
  fichab("Quién ejerce las potestades en una entidad pública empresarial",
         "Solo los órganos a los que los **estatutos** asignen expresamente esa facultad",
         "—", "—",
         "Sus órganos **no son asimilables** en rango a los de la AGE, salvo excepciones de los estatutos."))}

{unidad("4.4 Personal y contratación (art. 106)",
  lit("L40", "a106", ["se rige por el Derecho laboral", "convocatoria pública basada en los principios de igualdad, mérito y capacidad"], solo=[1, 2, 3, 4, 6, 7, 8]),
  fichab("Personal de las entidades públicas empresariales",
         "Personal **laboral**, salvo los funcionarios de la AGE que presten servicio en ellas",
         ["Directivos: nombrados según los criterios del art. 55.11, por experiencia en puestos de responsabilidad", "Resto del personal: convocatoria pública con igualdad, mérito y capacidad", "Controles del Ministerio de Hacienda sobre gastos de personal", "Contratación: legislación de contratos del sector público"],
         "—",
         "Personal **laboral** (con la excepción de los funcionarios). La ley de creación fija cómo pueden cubrir destinos los funcionarios de la AGE."))}

{unidad("4.5 Patrimonio y financiación (art. 107)",
  lit("L40", "a107", ["Excepcionalmente, cuando así lo prevea la Ley de creación", "se financiarán mayoritariamente con ingresos de mercado", "productor de mercado"], solo=[1, 3, 4, 5, 6, 7, 8, 9, 10]),
  fichab("Financiación de las entidades públicas empresariales",
         "—",
         ["Ingresos de sus operaciones (contraprestación de actividades comerciales), patrimonio y sus rentas", "**Excepcionalmente**, si lo prevé la ley de creación: consignaciones de los Presupuestos, transferencias, donaciones y legados"],
         "Financiación **mayoritaria** con ingresos de mercado (productor de mercado según el Sistema Europeo de Cuentas)",
         "Las consignaciones presupuestarias, solo **excepcionalmente** y si lo prevé la **ley de creación**."))}

{unidad("4.6 Presupuesto, contabilidad y control (art. 108)",
  lit("L40", "a108", ["Ley 47/2003, de 26 de noviembre"]),
  fichab("Régimen presupuestario", "—", "El de la **Ley General Presupuestaria**", "—",
         "Forman parte del sector público **empresarial** (LGP, art. 3; → I.3.2)."))}
""", 2)

T.ap("s13", "III.5 Agencias estatales (arts. 108 bis a 108 sexies)", f"""
Las agencias estatales están en la Ley 40/2015 por la Ley 11/2020, de Presupuestos Generales del Estado para 2021, que añadió los arts. 108 bis a 108 sexies (según los metadatos del texto consolidado del BOE, en vigor desde el 1-1-2021). Están **vigentes** y son la tercera clase de organismo público del art. 84.1 a).

{unidad("5.1 Definición (art. 108 bis)",
  lit("L40", "a1-2", ["creadas por el Gobierno para el cumplimiento de los programas correspondientes a las políticas públicas", "autonomía funcional, responsabilidad por la gestión y control de resultados", "“Agencia Estatal”"]),
  fichab("Organismo público para ejecutar programas de políticas públicas",
         f"{c('L40', 'a1-2', 'creadas por el Gobierno')} (108 bis.1) para los programas de políticas públicas de la AGE; como organismos públicos, su creación se efectúa por ley (art. 91.1 → III.1.4): así, la Ley 7/2025 tiene por objeto {c('L7_2025', 'Artículo 1', 'la creación de la Agencia Estatal de Salud Pública')} (→ Cierre 1)",
         ["Personalidad jurídica pública, patrimonio propio y autonomía de gestión; potestades administrativas", "Mecanismos de autonomía funcional, responsabilidad por la gestión y control de resultados"],
         "—",
         "Su rasgo propio: gestión por **resultados** (contrato de gestión, → III.5.2). Ojo: el art. 87.3 exige **ley** para transformar una entidad en agencia estatal (→ II.4.2)."))}

{unidad("5.2 Régimen jurídico y contrato de gestión (art. 108 ter)",
  lit("L40", "a1-3", ["se rigen por esta ley y, en su marco, por el estatuto propio de cada una de ellas", "contrato plurianual de gestión", "en el plazo de tres meses desde su constitución", "en el último trimestre de la vigencia del anterior", "por Orden conjunta de los Ministerios de adscripción, de Política Territorial y Función Pública y de Hacienda", "Comisión de Control"], solo=list(range(1, 16))),
  fichab("Cómo actúan las agencias estatales",
         ["**Consejo Rector**: aprueba la propuesta de contrato inicial de gestión", "Aprobación del contrato: **Orden conjunta** de los Ministerios de adscripción, de Política Territorial y Función Pública y de Hacienda", "**Comisión de Control**, en el seno del Consejo Rector"],
         ["Régimen: Ley 40/2015, su estatuto y el derecho administrativo general y especial", "Actúan con arreglo al plan de acción anual y al **contrato plurianual de gestión** (objetivos, planes e indicadores, plantilla máxima, recursos, efectos del cumplimiento, cobertura de déficits, modificaciones)"],
         ["Propuesta de contrato inicial: **tres meses** desde la constitución", "Contratos posteriores: en el **último trimestre** de vigencia del anterior", "Aprobación: máximo **tres meses** desde la presentación; si no, sigue vigente el anterior"],
         "**Tres meses** desde la constitución (cayó en 2025, → Cierre 1). Sin aprobación en plazo, **mantiene su vigencia** el contrato anterior."))}

{unidad("5.3 Personal (art. 108 quater)",
  lit("L40", "a1-4", ["mantiene la condición de personal funcionario, estatutario o laboral de origen", "igualdad, mérito y capacidad, así como de acceso al empleo público de las personas con discapacidad", "El órgano ejecutivo de la agencia estatal es el director"], solo=[1, 2, 3, 4, 5, 6, 9, 27]),
  fichab("Personal de las agencias estatales",
         ["Personal integrado al constituirse, el que se incorpora por provisión, el seleccionado por la agencia y el directivo", "**Director**: órgano ejecutivo, nombrado y separado por el Consejo Rector a propuesta del Presidente"],
         ["El personal integrado o incorporado mantiene su condición de origen (funcionario, estatutario o laboral)", "Selección propia: convocatoria pública, igualdad, mérito y capacidad y acceso de personas con discapacidad, dentro de la tasa de reposición"],
         "—",
         "El **director** lo nombra y separa el **Consejo Rector**, a propuesta del **Presidente**."))}

{unidad("5.4 Financiación, endeudamiento y contratación (art. 108 quinquies)",
  lit("L40", "a1-5", ["Las transferencias consignadas en los Presupuestos Generales del Estado", "El recurso al endeudamiento está prohibido a las agencias estatales, salvo que por Ley se disponga lo contrario", "siempre que el saldo vivo no supere el 5 % de su presupuesto"], solo=list(range(1, 10)) + [12, 13]),
  fichab("Recursos de las agencias estatales",
         "—",
         ["Transferencias de los Presupuestos Generales del Estado, ingresos propios por contraprestación, patrimonio y sus rendimientos, aportaciones gratuitas, patrocinios y otros", "Contratación: normativa del sector público; sus sociedades y fundaciones, publicidad y concurrencia"],
         ["Endeudamiento: **prohibido**, salvo ley", "Pólizas de crédito o préstamo por desfases de tesorería: saldo vivo hasta el **5 %** del presupuesto"],
         "Endeudamiento **prohibido** salvo **ley**; pólizas hasta el **5 %** del presupuesto."))}

{unidad("5.5 Presupuesto, cuentas y control (art. 108 sexies)",
  lit("L40", "a1-6", ["El Consejo Rector elaborará y aprobará el anteproyecto de presupuesto", "en el plazo de tres meses desde el cierre del ejercicio económico", "antes del 30 de junio del año siguiente", "corresponde al Tribunal de Cuentas", "control financiero permanente y de auditoría pública"], solo=[1, 23, 24, 25, 26, 27]),
  fichab("Presupuesto y control de las agencias estatales",
         ["Anteproyecto de presupuesto: **Consejo Rector** (→ Ministerio de adscripción → Hacienda)", "Cuentas: las formula el **Director** y las aprueba el **Consejo Rector**", "Control externo: **Tribunal de Cuentas**; interno: **IGAE**"],
         "El presupuesto se integra en los Presupuestos Generales del Estado; control interno por control financiero permanente y auditoría pública",
         ["Formulación de cuentas: **tres meses** desde el cierre del ejercicio", "Aprobación: antes del **30 de junio** del año siguiente", "Remisión a la IGAE: dentro de los **siete meses** siguientes al fin del ejercicio"],
         "Control **externo** → Tribunal de Cuentas; **interno** → IGAE; de **eficacia** → seguimiento del contrato de gestión."))}
""", 2)

T.ap("s14", "III.6 Cuadro comparativo de los organismos públicos (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| | Organismo autónomo | Entidad pública empresarial | Agencia estatal |
|---|---|---|---|
| Definición | Arts. 98 | 103 | 108 bis |
| Depende de | AGE | AGE u organismo autónomo | AGE (políticas públicas) |
| Derecho aplicable | **Administrativo**; derecho común en defecto (99) | **Privado**, salvo voluntad de órganos, potestades y lo regulado (104) | Ley 40/2015, estatuto y derecho administrativo (108 ter.1) |
| Personal | **Funcionario o laboral** (100.1) | **Laboral**, salvo funcionarios (106.1) | Funcionario, estatutario o laboral de origen; selección propia (108 quater) |
| Financiación | Patrimonio, consignaciones de los PGE, transferencias… (101.2) | **Ingresos de mercado**; PGE solo excepcionalmente (107) | Transferencias de los PGE, ingresos propios…; endeudamiento prohibido salvo ley (108 quinquies) |
| Instrumento propio | Plan de actuación (92) | Plan de actuación (92) | **Contrato plurianual de gestión** (108 ter) |
| Sector (LGP, art. 3) | Administrativo | Empresarial | Administrativo o empresarial, según las características del art. 3.1 b) LGP |
| Nombre | «O.A.» | «E.P.E» | «Agencia Estatal» |

Comunes a los tres (arts. 89 a 97): personalidad jurídica pública, potestades **salvo la expropiatoria**, creación por **ley**, estatutos por **Real Decreto**, fusión por **norma reglamentaria**, disolución por las causas del art. 96.

{resumen([
  "Organismos públicos: personalidad pública, patrimonio y tesorería propios; potestades **salvo la expropiatoria**; se crean por **ley** y sus estatutos se aprueban por **Real Decreto** (arts. 89, 91 y 93).",
  "Servicios comunes: bienes **inmuebles**, sistemas de información, asistencia **jurídica**, contabilidad, **publicaciones** y contratación **pública** (art. 95.2).",
  "Organismo autónomo: derecho **administrativo** y personal **funcionario o laboral**; entidad pública empresarial: derecho **privado** (con excepciones), personal **laboral** e **ingresos de mercado**.",
  "Agencia estatal: **contrato de gestión** (propuesta inicial en **tres meses** desde la constitución); endeudamiento prohibido salvo ley."],
  "Siguiente: IV. ¿Cómo son las demás entidades del sector público institucional?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Cómo son las demás entidades? (arts. 109 a 114 y 116 a 139)", donde(
  "Cuarta pregunta. Fuera de los organismos públicos, el art. 84.1 enumera otras entidades: unas de **derecho público** (autoridades administrativas independientes y consorcios), otras **privadas** en su forma (sociedades mercantiles estatales y fundaciones) y los **fondos sin personalidad**.",
  ["1 Autoridades administrativas independientes (arts. 109 y 110)", "2 Sociedades mercantiles estatales (arts. 111 a 114, 116 y 117)", "3 Consorcios (arts. 118 a 127)", "4 Fundaciones del sector público estatal (arts. 128 a 136)", "5 Fondos carentes de personalidad jurídica (arts. 137 a 139)", "6 Cuadro comparativo"]))

T.ap("s15", "IV.1 Autoridades administrativas independientes de ámbito estatal (arts. 109 y 110)", f"""
{unidad("1.1 Definición (art. 109)",
  lit("L40", "a109", ["funciones de regulación o supervisión de carácter externo sobre sectores económicos o actividades determinadas", "lo que deberá determinarse en una norma con rango de Ley", "con independencia de cualquier interés empresarial o comercial", "«A.A.I.»"]),
  fichab("Entidades de derecho público con independencia funcional",
         "Vinculadas a la AGE, con personalidad jurídica propia",
         "Regulación o supervisión **externa** de sectores económicos o actividades determinadas, con independencia funcional o especial autonomía",
         "—",
         "La independencia debe determinarse en una **norma con rango de Ley**. Actúan con independencia de **cualquier interés empresarial o comercial**."))}

{unidad("1.2 Régimen jurídico (art. 110)",
  lit("L40", "a110", ["se regirán por su Ley de creación, sus estatutos y la legislación especial de los sectores económicos sometidos a su supervisión", "supletoriamente", "principio de sostenibilidad financiera"]),
  fichab("Derecho que se aplica a las autoridades administrativas independientes",
         "—",
         ["Primero: su ley de creación, sus estatutos y la legislación especial del sector", "**Supletoriamente** (si es compatible con su naturaleza y autonomía): Ley 40/2015, en particular lo previsto para organismos autónomos, Ley 39/2015, LGP, contratos, patrimonio y demás derecho administrativo", "En defecto de norma administrativa: derecho común"],
         "—",
         "La Ley 40/2015 solo se les aplica **supletoriamente**. Están sujetas a la **sostenibilidad financiera** (LO 2/2012). El art. 85.1 somete a todas las entidades estatales al control de eficacia «sin perjuicio de lo establecido en el artículo 110»."))}
""", 2)

T.ap("s16", "IV.2 Sociedades mercantiles estatales (arts. 111 a 114, 116 y 117)", f"""
{unidad("2.1 Definición (art. 111)",
  lit("L40", "a111", ["sea superior al 50 por 100", "«S.M.E.»"]),
  fichab("Sociedad mercantil bajo control estatal",
         "Participación de la AGE o de entidades del sector público institucional estatal (incluidas otras sociedades estatales)",
         ["Control por participación directa en el capital **superior al 50 %** (se suman las de todas las entidades estatales)", "O control según el art. 4 de la Ley del Mercado de Valores"],
         "Más del **50 %** del capital",
         f"Es {c('L40', 'a111', 'superior al 50 por 100')} (no «igual o superior»); se **suman** las participaciones de todas las entidades estatales."))}

{unidad("2.2 Principios rectores (art. 112)",
  lit("L40", "a112", ["perseguirán la eficiencia, transparencia y buen gobierno"]),
  fichab("Gestión de las sociedades por sus accionistas públicos", "La AGE y las entidades del sector público institucional titulares del capital",
         "Eficiencia, transparencia y buen gobierno; buenas prácticas y códigos de conducta", "—",
         "Sin perjuicio de la **supervisión general del accionista** prevista en la Ley 33/2003."))}

{unidad("2.3 Régimen jurídico (art. 113)",
  lit("L40", "a113", ["por el ordenamiento jurídico privado", "En ningún caso podrán disponer de facultades que impliquen el ejercicio de autoridad pública"]),
  fichab("Derecho que se aplica a las sociedades mercantiles estatales",
         "—",
         ["Ley 40/2015, Ley 33/2003 de Patrimonio y **ordenamiento jurídico privado**", "Salvo en materia presupuestaria, contable, de personal, de control económico-financiero y de contratación"],
         "—",
         "**Nunca** facultades que impliquen ejercicio de **autoridad pública**, aunque excepcionalmente la **ley** puede atribuirles potestades administrativas."))}

{unidad("2.4 Creación y extinción (art. 114)",
  lit("L40", "a114", ["será autorizada mediante acuerdo del Consejo de Ministros", "recaerá en un órgano de la Administración General del Estado o en una entidad integrante del sector público institucional estatal"], solo=[1, 2, 3, 4, 5, 7]),
  fichab("Cómo se crea una sociedad mercantil estatal",
         "**Consejo de Ministros** (autoriza); informe preceptivo favorable de Hacienda o de la IGAE",
         ["Propuesta de estatutos y plan de actuación: razones y ausencia de duplicidades, análisis de eficiencia frente a un organismo público u otras formas, objetivos anuales e indicadores", "Liquidación: un órgano de la AGE o una entidad del sector público institucional estatal"],
         "—",
         "Sociedad → **acuerdo del Consejo de Ministros** (no ley, a diferencia de organismos públicos y fundaciones)."))}

{unidad("2.5 Tutela (art. 116.1 a 4)",
  lit("L40", "a116", ["la tutela funcional", "corresponderá íntegramente al Ministerio de Hacienda y Administraciones Públicas"], solo=[1, 2, 3, 4]),
  fichab("Ministerio que dirige la actividad de la sociedad",
         ["El Ministerio al que el Consejo de Ministros atribuya la **tutela funcional**", "Sin atribución expresa: el **Ministerio de Hacienda**"],
         "El Ministerio de tutela ejerce el control de eficacia, instruye sobre las líneas estratégicas y, excepcionalmente, puede dar instrucciones por interés público",
         "—",
         "Los administradores que cumplan esas instrucciones quedan **exonerados** de responsabilidad si de ellas se derivan consecuencias lesivas (116.6)."))}

{unidad("2.6 Presupuesto, contabilidad, control y personal (art. 117)",
  lit("L40", "a117", ["presupuesto de explotación y capital", "Código de Comercio y el Plan General de Contabilidad", "se regirá por el Derecho laboral"]),
  fichab("Régimen económico y de personal",
         "Control: **IGAE**, sin perjuicio del **Tribunal de Cuentas**",
         ["Presupuesto de explotación y capital y plan de actuación anual, integrados en los Presupuestos Generales del Estado", "Cuentas: Código de Comercio y Plan General de Contabilidad", "Personal, incluido el directivo: **Derecho laboral** y normativa presupuestaria"],
         "—",
         "El **Código de Comercio** aparece aquí solo para la **contabilidad**; el régimen general es el del art. 113 (→ IV.2.3)."))}
""", 2)

T.ap("s17", "IV.3 Consorcios (arts. 118 a 127)", f"""
El Capítulo VI (consorcios) es **básico** también para Comunidades Autónomas y entidades locales (art. 81.3, → II.1.1).

{unidad("3.1 Definición y actividades (art. 118)",
  lit("L40", "a118", ["creadas por varias Administraciones Públicas o entidades integrantes del sector público institucional, entre sí o con participación de entidades privadas", "«consorcio» o su abreviatura «C»"]),
  fichab("Entidad de derecho público de varias Administraciones",
         "Varias Administraciones Públicas o entidades del sector público institucional, entre sí o con entidades privadas",
         ["Actividades de interés común dentro de sus competencias: fomento, prestacionales, gestión común de servicios públicos", "También para gestionar servicios públicos en la cooperación transfronteriza"],
         "—",
         "Personalidad jurídica **propia y diferenciada**; pueden participar **entidades privadas**."))}

{unidad("3.2 Régimen jurídico (art. 119)",
  lit("L40", "a119", ["en la normativa autonómica de desarrollo y sus estatutos", "Código Civil sobre la sociedad civil", "carácter supletorio"]),
  fichab("Derecho que se aplica a los consorcios",
         "—",
         ["Ley 40/2015, normativa autonómica de desarrollo y estatutos", "Separación, disolución y extinción no previstas: **Código Civil** (sociedad civil); liquidación: art. 97 y, en su defecto, Ley de Sociedades de Capital", "Normas de la Ley 7/1985 y de la Ley 27/2013 sobre consorcios locales: **supletorias**"],
         "—",
         "Remisión al **Código Civil** sobre la **sociedad civil**, salvo la **liquidación** (art. 97)."))}

{unidad("3.3 Adscripción (art. 120)",
  lit("L40", "a120", ["Disponga de la mayoría de votos en los órganos de gobierno", "el consorcio no tendrá ánimo de lucro", "en un plazo no superior a seis meses"]),
  fichab("A qué Administración se adscribe el consorcio",
         "Lo determinan los estatutos, según los criterios legales, por orden de prioridad y referidos al primer día del ejercicio presupuestario",
         ["::Criterios por prioridad:", "a) Mayoría de votos en los órganos de gobierno", "b) Nombrar o destituir a la mayoría de los órganos ejecutivos", "c) Nombrar o destituir a la mayoría del personal directivo", "d) Mayor control por normativa especial", "e) Nombrar o destituir a la mayoría del órgano de gobierno", "f) Financiar más del 50 % (o en mayor medida)", "g) Mayor participación en el fondo patrimonial", "h) Más habitantes o extensión territorial"],
         "Cambio de adscripción: modificar los estatutos en **seis meses** como máximo desde el inicio del ejercicio presupuestario siguiente",
         "Consorcio: **seis meses**; fundación: **tres meses** (→ IV.4.2). Con entidades privadas, el consorcio **no tiene ánimo de lucro**. Cayó en 2025 (→ Cierre 1)."))}

{unidad("3.4 Personal (art. 121)",
  lit("L40", "a121", ["habrá de proceder de las Administraciones participantes", "en ningún caso podrán superar"]),
  fichab("Personal de los consorcios",
         "Personal **funcionario o laboral** procedente de las Administraciones participantes",
         ["Régimen jurídico: el de la Administración de adscripción", "Excepcionalmente, contratación propia autorizada por el Ministerio de Hacienda y Función Pública u órgano competente de la Administración de adscripción"],
         "—",
         "Sus retribuciones **no pueden superar** las de puestos equivalentes de la Administración de adscripción."))}

{unidad("3.5 Presupuesto, contabilidad, control y patrimonio (art. 122)",
  lit("L40", "a122", ["régimen de presupuestación, contabilidad y control de la Administración Pública a la que estén adscritos", "al menos, dos de las tres circunstancias siguientes", "Que el número medio de trabajadores empleados durante el ejercicio sea superior a 50"], solo=[1, 3, 4, 5, 6, 12, 13]),
  fichab("Régimen económico de los consorcios",
         "El de la **Administración de adscripción**; auditoría de cuentas por su órgano de control interno",
         ["Forman parte de los presupuestos y de la cuenta general de la Administración de adscripción", "Normas patrimoniales de la Administración de adscripción"],
         ["::Auditoría obligatoria si se dan **dos de tres**:", "Activo superior a 2.400.000 euros", "Ingresos (o cifra de negocios) superiores a 2.400.000 euros", "Más de 50 trabajadores de media"],
         "**Dos de tres** circunstancias: activo y cifra de ingresos de **2.400.000** euros y **50** trabajadores."))}

{unidad("3.6 Creación (art. 123)",
  lit("L40", "a123", ["se crearán mediante convenio", "Que su creación se autorice por ley", "precisará de autorización previa del Consejo de Ministros", "no podrá ser objeto de delegación"]),
  fichab("Cómo se crea un consorcio",
         ["Las Administraciones, organismos o entidades participantes, por **convenio**", "Con la AGE: lo suscribe el titular del departamento ministerial (o el del máximo órgano de dirección del organismo autónomo)"],
         ["::Si participa la AGE o sus entidades:", "Creación **autorizada por ley**", "Convenio con autorización previa del **Consejo de Ministros**", "Estatutos, plan de actuación, proyección presupuestaria **trienal** e informe preceptivo favorable de Hacienda", "Publicación del convenio y los estatutos en el BOE"],
         "—",
         "**Convenio**; con participación estatal, además **ley** que lo autorice y autorización del **Consejo de Ministros**. La suscripción **no se puede delegar**."))}

{unidad("3.7 Contenido de los estatutos (art. 124)",
  lit("L40", "a124", ["Sede, objeto, fines y funciones.", "Causas de disolución."], solo=[1, 2, 3, 4, 5]),
  fichab("Qué deben decir los estatutos del consorcio",
         "—",
         ["Administración de adscripción y régimen orgánico, funcional y financiero", "Sede, objeto, fines y funciones", "Participantes y aportaciones (con cláusulas por incumplimiento de compromisos)", "Órganos de gobierno y administración y régimen de acuerdos", "Causas de disolución"],
         "—",
         "Pueden prever la **suspensión temporal del derecho de voto** de quien incumpla manifiestamente sus obligaciones, en especial de financiación."))}

{unidad("3.8 Derecho de separación y sus efectos (arts. 125 y 126.1)",
  lit("L40", "a125", ["podrán separarse del mismo en cualquier momento siempre que no se haya señalado término para la duración del consorcio"], solo=[1, 2, 4]),
  lit("L40", "a126", ["al menos, dos Administraciones"], solo=[1]),
  fichab("Salida de un miembro del consorcio",
         "Cualquier miembro, por escrito al máximo órgano de gobierno",
         ["Sin término de duración: en **cualquier momento**", "Con duración determinada: antes del fin del plazo si otro miembro incumple sus obligaciones estatutarias"],
         "—",
         "La separación **disuelve** el consorcio, salvo que los demás acuerden continuar y permanezcan **al menos dos Administraciones** (o entidades de más de una Administración)."))}

{unidad("3.9 Disolución (art. 127.1, 2 y 5)",
  lit("L40", "a127", ["En todo caso será causa de disolución que los fines para los que fue creado el consorcio hayan sido cumplidos", "nombrará un liquidador"], solo=[1, 2, 7]),
  fichab("Fin del consorcio",
         "El **máximo órgano de gobierno** acuerda la disolución y nombra liquidador (órgano o entidad de la Administración de adscripción)",
         "Disolución → liquidación y extinción; cabe la cesión global de activos y pasivos a otra entidad del sector público (extinción sin liquidación)",
         "Cesión global: mayoría de los estatutos o, a falta de previsión, **unanimidad**",
         "Siempre es causa de disolución el **cumplimiento de los fines**."))}
""", 2)

T.ap("s18", "IV.4 Fundaciones del sector público estatal (arts. 128 a 136)", f"""
{unidad("4.1 Definición y actividades (art. 128)",
  lit("L40", "a128", ["con una aportación mayoritaria", "en más de un 50 por ciento", "La mayoría de derechos de voto en su patronato", "Las fundaciones no podrán ejercer potestades públicas", "«F.S.P.»"]),
  fichab("Fundaciones bajo control estatal",
         "AGE o entidades del sector público institucional estatal",
         ["::Basta **uno** de estos requisitos:", "a) Aportación **mayoritaria** inicial o posterior", "b) Patrimonio integrado en **más del 50 %** por bienes o derechos aportados o cedidos con carácter permanente", "c) **Mayoría de derechos de voto** en el patronato", "Actividades sin ánimo de lucro para fines de interés general, del ámbito competencial de las entidades fundadoras"],
         "—",
         "**No** pueden ejercer **potestades públicas** ni asumir las competencias propias de las fundadoras (salvo previsión legal expresa). Cabe aportación privada **no mayoritaria**."))}

{unidad("4.2 Adscripción (art. 129)",
  lit("L40", "a129", ["Disponga de mayoría de patronos", "se adscribirá a la Administración General del Estado", "en un plazo no superior a tres meses"]),
  fichab("A qué Administración se adscribe la fundación",
         "Lo determinan los estatutos, según criterios por orden de prioridad referidos al primer día del ejercicio presupuestario",
         ["a) Mayoría de patronos", "b) a d) Nombrar o destituir a la mayoría de órganos ejecutivos, personal directivo o patronato", "e) Financiar más del 50 % (o en mayor medida)", "f) Mayor participación en el fondo patrimonial", "g) Si nada resulta determinante: la AGE y, si no participa, la que decida el patronato"],
         "Cambio de adscripción: estatutos modificados en **tres meses** como máximo desde el inicio del ejercicio presupuestario siguiente",
         "Fundación: **tres meses**; consorcio: **seis** (→ IV.3.3). Régimen presupuestario y de control: el de la Administración de adscripción (129.5). El art. 129 es **básico** (art. 81.3)."))}

{unidad("4.3 Régimen jurídico (art. 130)",
  lit("L40", "a130", ["por la Ley 50/2002, de 26 de diciembre, de Fundaciones", "por el ordenamiento jurídico privado"]),
  fichab("Derecho que se aplica a las fundaciones del sector público estatal",
         "—",
         ["Ley 40/2015", "Ley 50/2002, de Fundaciones", "Legislación autonómica de fundaciones aplicable", "**Ordenamiento jurídico privado**, salvo en materia presupuestaria, contable, de control económico-financiero y de contratación"],
         "—",
         "Se rigen por la **Ley de Fundaciones** y el derecho privado. Cayó en 2025 (→ Cierre 1)."))}

{unidad("4.4 Contratación, presupuesto, control y personal (arts. 131 y 132)",
  lit("L40", "a131", ["legislación sobre contratación del sector público"]),
  lit("L40", "a132", ["presupuesto de explotación y capital", "estarán sometidas al control de la Intervención General de la Administración del Estado", "se regirá por el Derecho laboral"]),
  fichab("Régimen económico y de personal de las fundaciones estatales",
         "Control: **IGAE**, sin perjuicio del Tribunal de Cuentas",
         ["Contratación: legislación de contratos del sector público", "Presupuesto de explotación y capital integrado en los Presupuestos Generales del Estado", "Contabilidad: adaptación del Plan General de Contabilidad a entidades sin fines lucrativos", "Personal, incluido el directivo: **Derecho laboral**"],
         "—",
         "Forman el sector público **fundacional** (LGP, art. 3.3; → I.3.2)."))}

{unidad("4.5 Creación (art. 133)",
  lit("L40", "a133", ["se realizará por ley", "se aprobarán por Real Decreto de Consejo de Ministros"]),
  fichab("Cómo se crea una fundación del sector público estatal",
         ["Las Cortes, por **ley** (creación o adquisición sobrevenida del carácter)", "Estatutos: Real Decreto del Consejo de Ministros a propuesta conjunta de Hacienda y del Ministerio que ejerza el protectorado"],
         "El anteproyecto va con propuesta de estatutos, plan de actuación e informe preceptivo favorable de Hacienda o de la IGAE",
         "—",
         "Fundación → **ley** (como los organismos públicos); sociedad mercantil → acuerdo del **Consejo de Ministros** (→ IV.2.4)."))}

{unidad("4.6 Protectorado y patronato (arts. 134 y 135)",
  lit("L40", "a134", ["El Protectorado de las fundaciones del sector público será ejercido por el órgano de la Administración de adscripción"]),
  lit("L40", "a135", ["la mayoría de miembros del patronato serán designados por los sujetos del sector público estatal"], solo=[1]),
  fichab("Protectorado y composición del patronato",
         ["Protectorado: órgano competente de la Administración de **adscripción**", "Patronato: mayoría designada por el sector público estatal"],
         "El protectorado vela por las obligaciones de la normativa de fundaciones, sin perjuicio del control de eficacia y la supervisión continua",
         "—",
         "El art. 134 es **básico** (art. 81.3, → II.1.1)."))}

{unidad("4.7 Fusión, disolución, liquidación y extinción (art. 136)",
  lit("L40", "a136", ["artículos 94, 96 y 97"]),
  fichab("Fin de las fundaciones estatales", "—", "Se aplica el régimen de los organismos públicos: arts. 94, 96 y 97 (→ III.2)", "—",
         "Remite a los artículos de **organismos públicos**, no a la Ley de Fundaciones."))}
""", 2)

T.ap("s19", "IV.5 Fondos carentes de personalidad jurídica (arts. 137 a 139)", f"""
{unidad("5.1 Creación y extinción (art. 137)",
  lit("L40", "a137", ["se efectuará por Ley", "se extinguirán por norma de rango reglamentario", "«F.C.P.J»"]),
  fichab("Fondos sin personalidad del sector público estatal",
         "Las Cortes (creación por ley); la norma de creación fija su adscripción a la AGE",
         "—",
         ["Creación: **Ley**", "Extinción: **norma reglamentaria**"],
         "Se crean por **ley** y se extinguen por **norma reglamentaria**."))}

{unidad("5.2 Régimen jurídico y presupuestario (arts. 138 y 139)",
  lit("L40", "a138", ["en su norma de creación"]),
  lit("L40", "a139", ["Ley 47/2003, de 26 de noviembre"]),
  fichab("Derecho que se aplica a los fondos",
         "—",
         ["Ley 40/2015, norma de creación y derecho administrativo general y especial", "Presupuesto, contabilidad y control: Ley General Presupuestaria"],
         "—",
         "En la LGP, sector **administrativo** o **empresarial** según sus características (art. 3, → I.3.2)."))}
""", 2)

T.ap("s20", "IV.6 Cuadro comparativo de las demás entidades (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| | Autoridad administrativa independiente | Sociedad mercantil estatal | Consorcio | Fundación del sector público | Fondo sin personalidad |
|---|---|---|---|---|---|
| Naturaleza | Derecho público (109) | Sociedad mercantil (111) | Derecho público (118) | Fundación (128) | Sin personalidad (137) |
| Creación | Independencia fijada en norma con rango de ley (109.1) | Acuerdo del **Consejo de Ministros** (114) | **Convenio**; con la AGE, autorizado por **ley** (123) | **Ley** (133) | **Ley**; extinción reglamentaria (137) |
| Derecho aplicable | Ley de creación, estatutos, legislación sectorial; Ley 40/2015 supletoria (110) | Ley 40/2015, Ley 33/2003 y **derecho privado** (113) | Ley 40/2015, normativa autonómica, estatutos (119) | Ley 40/2015, **Ley 50/2002** y derecho privado (130) | Ley 40/2015, norma de creación y derecho administrativo (138) |
| Personal | — | **Laboral** (117.4) | Funcionario o laboral de las Administraciones participantes (121) | **Laboral** (132.3) | — |
| Potestades | Regulación o supervisión | Nunca autoridad pública; excepcionalmente potestades por ley (113) | — | **No** pueden ejercer potestades públicas (128.2) | — |
| Cambio de adscripción | — | — | Estatutos en **6 meses** (120.4) | Estatutos en **3 meses** (129.4) | — |

{resumen([
  "Autoridades administrativas independientes: regulación o supervisión **externa**; independencia fijada en **norma con rango de ley**; la Ley 40/2015, solo **supletoria**.",
  "Sociedades mercantiles estatales: control por participación **superior al 50 %**; creación por **acuerdo del Consejo de Ministros**; derecho privado; nunca autoridad pública.",
  "Consorcios: varias Administraciones; **convenio** (y ley si participa la AGE); adscripción por criterios; cambio de adscripción en **seis meses**.",
  "Fundaciones: **ley**; Ley 50/2002 y derecho privado; sin potestades públicas; cambio de adscripción en **tres meses**. Fondos: **ley** para crear, **reglamento** para extinguir."],
  "Siguiente: Cierre 1. Preguntas de los exámenes de 2025")}
""", 2)

# =============================================================================
# Preguntas oficiales: porqué de cada opción y coherencia plantilla ↔ ley
EX_L12 = examen("L", 12, {
  "a": f"Literal del art. 82.1: {c('L40', 'a82', 'se configura como un registro público administrativo')} y {c('L40', 'a82', 'dependerá de la Intervención General de la Administración del Estado')}.",
  "b": f"Cambia el órgano: la gestión {c('L40', 'a82', 'dependerá de la Intervención General de la Administración del Estado')}, no de la Autoridad Independiente de Responsabilidad Fiscal.",
  "c": f"Cambia la naturaleza y el órgano: es un {c('L40', 'a82', 'registro público administrativo')} (no «interno») y depende de la IGAE, no del Tribunal de Cuentas.",
  "d": f"Cambia la naturaleza y el órgano: es un {c('L40', 'a82', 'registro público administrativo')} y depende de la IGAE, no de una Subdirección General de Datos del Empleo Público."},
  [("registro público administrativo", "L40", "a82", "se configura como un registro público administrativo"),
   ("Intervención General de la Administración del Estado", "L40", "a82", "dependerá de la Intervención General de la Administración del Estado")])
EX_P4 = examen("P", 4, {
  "a": f"Cambia una palabra: el servicio común es la {c('L40', 'a95', 'Contratación pública')}, no la privada.",
  "b": f"Cambia una palabra: el servicio común es la {c('L40', 'a95', 'Gestión de bienes inmuebles')}, no de bienes muebles.",
  "c": f"Cambia una palabra: el servicio común es la {c('L40', 'a95', 'Asistencia jurídica')}, no la técnica.",
  "d": f"Literal del art. 95.2 e): {c('L40', 'a95', 'Publicaciones')}."},
  [("publicaciones", "L40", "a95", "e) Publicaciones.")])
EX_P5 = examen("P", 5, {
  "a": f"Literal del art. 108 ter.4: {c('L40', 'a1-3', 'aprueba la propuesta de contrato inicial de gestión, en el plazo de tres meses desde su constitución')}.",
  "b": f"Cambia el plazo: son {c('L40', 'a1-3', 'tres meses desde su constitución')}, no seis.",
  "c": f"Cambia el plazo: son {c('L40', 'a1-3', 'tres meses desde su constitución')}, no un año.",
  "d": f"Cambia el plazo: son {c('L40', 'a1-3', 'tres meses desde su constitución')}, no ocho meses."},
  [("tres meses", "L40", "a1-3", "aprueba la propuesta de contrato inicial de gestión, en el plazo de tres meses desde su constitución")])
EX_P6 = examen("P", 6, {
  "a": f"El derecho privado no es el régimen de los organismos autónomos: {c('L40', 'a99', 'En defecto de norma administrativa, se aplicará el derecho común')}. Su patrimonio se gestiona conforme a la Ley 33/2003 (art. 101.1).",
  "b": f"Literal del art. 99: se rigen {c('L40', 'a99', 'en su ley de creación')} y por {c('L40', 'a99', 'el resto de las normas de derecho administrativo general y especial')}.",
  "c": f"El personal de los organismos autónomos {c('L40', 'a100', 'será funcionario o laboral')} (art. 100.1); su régimen jurídico general es el administrativo (art. 99), no el laboral común.",
  "d": "El régimen mercantil no aparece en el art. 99; el derecho privado es la regla de las entidades públicas empresariales (art. 104) y de las sociedades mercantiles estatales (art. 113)."},
  [("ley de creación", "L40", "a99", "en su ley de creación"), ("derecho administrativo", "L40", "a99", "normas de derecho administrativo general y especial")])
EX_P7 = examen("P", 7, {
  "a": f"No son entidades privadas: {c('L40', 'a103', 'Las entidades públicas empresariales son entidades de Derecho público')}.",
  "b": f"Sí tienen personalidad: son entidades {c('L40', 'a103', 'con personalidad jurídica propia')}.",
  "c": f"Literal del art. 103.1: {c('L40', 'a103', 'con personalidad jurídica propia, patrimonio propio y autonomía en su gestión')}.",
  "d": f"Cambia la financiación: {c('L40', 'a103', 'se financian con ingresos de mercado')}, no mayoritariamente con los Presupuestos (estos, solo excepcionalmente, art. 107.2)."},
  [("personalidad jurídica propia", "L40", "a103", "con personalidad jurídica propia, patrimonio propio"), ("patrimonio propio", "L40", "a103", "patrimonio propio y autonomía en su gestión")])
EX_X21 = examen("X", 21, {
  "a": f"Cambia el plazo: tres meses es el de las fundaciones ({c('L40', 'a129', 'en un plazo no superior a tres meses')}, art. 129.4); el del consorcio es de seis.",
  "b": f"Literal del art. 120.4: {c('L40', 'a120', 'en un plazo no superior a seis meses, contados desde el inicio del ejercicio presupuestario siguiente')}.",
  "c": f"Cambia el plazo: {c('L40', 'a120', 'en un plazo no superior a seis meses')}, no ocho.",
  "d": f"Cambia el plazo: {c('L40', 'a120', 'en un plazo no superior a seis meses')}, no diez."},
  [("Seis meses", "L40", "a120", "en un plazo no superior a seis meses")])
EX_X22 = examen("X", 22, {
  "a": f"Las sociedades mercantiles estatales sí integran el sector público institucional (art. 84.1 c), pero no se rigen por el Código de Comercio: {c('L40', 'a113', 'se regirán por lo previsto en esta Ley, por lo previsto en la Ley 33/2003, de 3 de noviembre, y por el ordenamiento jurídico privado')} (el Código de Comercio solo aparece para su contabilidad, art. 117.2).",
  "b": f"Las entidades locales no son sector público institucional: son una de las Administraciones territoriales ({c('L40', 'a2', 'c) Las Entidades que integran la Administración Local.')}, art. 2.1 c).",
  "c": f"Las comunidades autónomas tampoco: son Administraciones territoriales ({c('L40', 'a2', 'b) Las Administraciones de las Comunidades Autónomas.')}, art. 2.1 b).",
  "d": f"Art. 84.1 e): {c('L40', 'a84', 'Las fundaciones del sector público')}; y art. 130: se rigen {c('L40', 'a130', 'por la Ley 50/2002, de 26 de diciembre, de Fundaciones')}."},
  [("fundaciones del sector público", "L40", "a84", "e) Las fundaciones del sector público."), ("Fundaciones", "L40", "a130", "por la Ley 50/2002, de 26 de diciembre, de Fundaciones")])
EX_L45 = examen("L", 45, {
  "a": f"La Ley 7/2025 no crea un organismo autónomo «Instituto de Salud Pública»: {c('L7_2025', 'Artículo 1', 'El objeto de esta ley es la creación de la Agencia Estatal de Salud Pública')}.",
  "b": f"Literal de la Ley 7/2025, art. 1.1: {c('L7_2025', 'Artículo 1', 'la creación de la Agencia Estatal de Salud Pública')}; y art. 2.1: {c('L7_2025', 'Artículo 2', 'reforzar las capacidades del Estado para mejorar la salud de la población')}.",
  "c": f"Cambia el nombre: es la {c('L7_2025', 'Artículo 1', 'Agencia Estatal de Salud Pública')}, no «de Control de Pandemias».",
  "d": f"Cambia el tipo de entidad: es una agencia estatal, con el régimen de {c('L7_2025', 'Artículo 1', 'los artículos 88 a 97 y 108 bis a 108 sexies de la Ley 40/2015')}, no una autoridad administrativa independiente (arts. 109 y 110)."},
  [("Agencia Estatal de Salud Pública", "L7_2025", "Artículo 1", "El objeto de esta ley es la creación de la Agencia Estatal de Salud Pública")])
EX_P84 = examen("P", 84, {
  "a": f"Literal del art. 2.3, párrafo segundo, LGP: {c('LGP', 'a2', 'esta Ley no será de aplicación a las Cortes Generales, que gozan de autonomía presupuestaria')}.",
  "b": f"Incluidos: {c('LGP', 'a2', 'f) Los fondos sin personalidad jurídica.')} (art. 2.2 f).",
  "c": f"Incluidas: {c('LGP', 'a2', 'las mutuas colaboradoras con la Seguridad Social en su función pública de colaboración en la gestión de la Seguridad Social')} (art. 2.2 h).",
  "d": f"Incluidos: {c('LGP', 'a2', 'd) Los consorcios adscritos a la Administración General del Estado.')} (art. 2.2 d)."},
  [("Cortes Generales", "LGP", "a2", "esta Ley no será de aplicación a las Cortes Generales")])

T.ap("s21", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **siete** preguntas de este tema (una en el turno libre, cuatro en promoción interna y dos en el extraordinario) y **dos** relacionadas (la L 45, del tema III.10, sobre la creación de una agencia estatal, y la P 84, del tema VI.1, sobre el ámbito de la Ley General Presupuestaria). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-L 2025, pregunta 12 · Inventario de Entidades (→ II.2.1)", EX_L12,
  "### GACE-P 2025, pregunta 4 · Servicios comunes (→ III.2.2)", EX_P4,
  "### GACE-P 2025, pregunta 5 · Contrato de gestión de las agencias estatales (→ III.5.2)", EX_P5,
  "### GACE-P 2025, pregunta 6 · Régimen jurídico de los organismos autónomos (→ III.3.2)", EX_P6,
  "### GACE-P 2025, pregunta 7 · Entidades públicas empresariales (→ III.4.1)", EX_P7,
  "### GACE-L 2025 extraordinario, pregunta 21 · Cambio de adscripción del consorcio (→ IV.3.3)", EX_X21,
  "### GACE-L 2025 extraordinario, pregunta 22 · Entidades y régimen jurídico (→ I.2.1 y → IV.4.3)", EX_X22,
  "### GACE-L 2025, pregunta 45 · Agencia Estatal de Salud Pública (relacionada; → III.5.1)", EX_L45,
  "### GACE-P 2025, pregunta 84 · Ámbito de la Ley General Presupuestaria (relacionada; → I.3.1)", EX_P84,
  "### Cómo se pregunta",
  "!> Citan el **artículo** de la Ley 40/2015 y cambian **una palabra** (bienes muebles/inmuebles, asistencia técnica/jurídica), **un plazo** (tres o seis meses), **un órgano** (IGAE frente a AIReF o Tribunal de Cuentas) o **el derecho aplicable** (administrativo, privado, laboral, mercantil). Aprende para cada entidad: **qué es**, **cómo se crea**, **qué derecho la rige** y **qué personal tiene**.",
]))

T.ap("s22", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Qué es y quién lo integra | Sector público = 3 Administraciones territoriales + sector público institucional (art. 2); lista cerrada estatal (art. 84); LGP: administrativo, empresarial, fundacional | **Fundaciones del sector público**: Ley 50/2002 (X 22); la LGP no se aplica a las **Cortes Generales** (P 84) |
| II. Reglas comunes | Principios y supervisión continua (81); Inventario (82-83); 60/40 (84 bis); eficacia y supervisión (85); medio propio (86); transformación (87) | Inventario: registro **público**, gestión de la **IGAE** (L 12) |
| III. Organismos públicos | Creación por ley; estatutos por Real Decreto; servicios comunes; OA (derecho administrativo), EPE (derecho privado, ingresos de mercado), agencias (contrato de gestión) | Servicios comunes: **publicaciones** (P 4); contrato de gestión en **tres meses** (P 5); OA: **ley de creación** y derecho administrativo (P 6); EPE: **personalidad y patrimonio propios** (P 7) |
| IV. Demás entidades | AAI (independencia por ley), SME (> 50 %, Consejo de Ministros), consorcios (convenio), fundaciones (ley), fondos (ley/reglamento) | Consorcio: cambio de adscripción en **seis meses** (X 21) |

?> **Trampas frecuentes:** «la transformación en agencia estatal se hace por Real Decreto» (es **por ley**); «los organismos públicos tienen potestad expropiatoria» (es la **excepción**); «la sociedad mercantil estatal se crea por ley» (se autoriza por **acuerdo del Consejo de Ministros**); «participación igual o superior al 50 %» (es **superior al 50 %**); «la fundación modifica los estatutos en seis meses» (son **tres**; seis es el **consorcio**); «las entidades públicas empresariales se financian mayoritariamente con los Presupuestos» (con **ingresos de mercado**); «los fondos sin personalidad se extinguen por ley» (por **norma reglamentaria**).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
T.q("L40", "a2", "Ámbito", "Según el artículo 2.1 de la Ley 40/2015, de Régimen Jurídico del Sector Público, el sector público comprende la Administración General del Estado, las Administraciones de las Comunidades Autónomas, las Entidades que integran la Administración Local y:",
    ["El sector público institucional.", "Las Cortes Generales.", "Los órganos constitucionales del Estado.", "Las corporaciones de derecho público."],
    "Art. 2.1 d) Ley 40/2015.", "d) El sector público institucional.")
T.q("L40", "a2", "Ámbito", "Según el artículo 2.3 de la Ley 40/2015, tienen la consideración de Administraciones Públicas, además de las territoriales:",
    ["Los organismos públicos y entidades de derecho público vinculados o dependientes.", "Todas las entidades del sector público institucional, incluidas las de derecho privado.", "Las sociedades mercantiles estatales.", "Las fundaciones del sector público."],
    "Art. 2.3: solo los organismos públicos y entidades de derecho público de la letra a) del apartado 2.", "así como los organismos públicos y entidades de derecho público previstos en la letra a) del apartado 2")
T.q("L40", "a2", "Ámbito", "Según el artículo 2.2 c) de la Ley 40/2015, las Universidades públicas se regirán:",
    ["Por su normativa específica y supletoriamente por las previsiones de la Ley 40/2015.", "Exclusivamente por la Ley 40/2015.", "Por el derecho privado y supletoriamente por la Ley 40/2015.", "Por la Ley 47/2003 y supletoriamente por su normativa específica."],
    "Art. 2.2 c) Ley 40/2015.", "se regirán por su normativa específica y supletoriamente por las previsiones de la presente Ley")
T.q("L40", "a84", "Composición", "Según el artículo 84.1 de la Ley 40/2015, los organismos públicos vinculados o dependientes de la Administración General del Estado se clasifican en:",
    ["Organismos autónomos, entidades públicas empresariales y agencias estatales.", "Organismos autónomos, entidades públicas empresariales y autoridades administrativas independientes.", "Organismos autónomos, sociedades mercantiles estatales y consorcios.", "Organismos autónomos y entidades públicas empresariales, únicamente."],
    "Art. 84.1 a): tres clases de organismos públicos; las autoridades administrativas independientes son la letra b).", ["1. Organismos autónomos.", "2. Entidades públicas empresariales.", "3. Agencias estatales."])
T.q("L40", "a84", "Composición", "Según el artículo 84.2 de la Ley 40/2015, la Administración General del Estado:",
    ["No podrá crear ni ejercer el control efectivo sobre ningún otro tipo de entidad distinta de las enumeradas en ese artículo.", "Podrá crear otros tipos de entidades si lo autoriza el Consejo de Ministros.", "Podrá crear otros tipos de entidades en colaboración con entidades privadas.", "Podrá ejercer el control indirecto sobre entidades de otro tipo."],
    "Art. 84.2: lista cerrada.", "sobre ningún otro tipo de entidad distinta de las enumeradas en este artículo")
T.q("LGP", "a3", "Composición", "Según el artículo 3 de la Ley 47/2003, General Presupuestaria, las sociedades mercantiles estatales forman parte del:",
    ["Sector público empresarial.", "Sector público administrativo.", "Sector público fundacional.", "Sector público institucional autonómico."],
    "Art. 3.2 b) LGP.", "b) Las sociedades mercantiles estatales.")
T.q("LGP", "a3", "Composición", "Según el artículo 3 de la Ley General Presupuestaria, los organismos autónomos forman parte del:",
    ["Sector público administrativo.", "Sector público empresarial.", "Sector público fundacional.", "Sector público empresarial, si se financian con ingresos de mercado."],
    "Art. 3.1 a) LGP.", "La Administración General del Estado, los organismos autónomos, las autoridades administrativas independientes")
T.q("L40", "a81", "Reglas comunes", "Según el artículo 81.1 de la Ley 40/2015, las entidades del sector público institucional están sometidas en su actuación a los principios de:",
    ["Legalidad, eficiencia, estabilidad presupuestaria y sostenibilidad financiera, así como al de transparencia en su gestión.", "Jerarquía, descentralización, desconcentración y coordinación.", "Legalidad, jerarquía y competencia.", "Eficacia, economía y celeridad."],
    "Art. 81.1 Ley 40/2015.", "legalidad, eficiencia, estabilidad presupuestaria y sostenibilidad financiera así como al principio de transparencia en su gestión")
T.q("L40", "a82", "Inventario", "Según el artículo 82.1 de la Ley 40/2015, la integración y gestión del Inventario de Entidades del Sector Público Estatal, Autonómico y Local y su publicación dependerá de:",
    ["La Intervención General de la Administración del Estado.", "El Tribunal de Cuentas.", "La Autoridad Independiente de Responsabilidad Fiscal.", "La Dirección General de Presupuestos."],
    "Art. 82.1 Ley 40/2015.", "dependerá de la Intervención General de la Administración del Estado")
T.q("L40", "a83", "Inventario", "Según el artículo 83.2 b) de la Ley 40/2015, la inscripción en el Inventario de Entidades del Sector Público se practicará dentro del plazo de:",
    ["15 días hábiles siguientes a la recepción de la solicitud de inscripción.", "30 días hábiles siguientes a la recepción de la solicitud de inscripción.", "Un mes desde la entrada en vigor de la norma de creación.", "10 días naturales desde la recepción de la solicitud."],
    "Art. 83.2 b). Los 30 días hábiles son para notificar (83.1 y 2 a).", "dentro del plazo de 15 días hábiles siguientes a la recepción de la solicitud de inscripción")
T.q("L40", "a8-2", "Reglas comunes", "Según el artículo 84 bis de la Ley 40/2015, en la presencia equilibrada de mujeres y hombres en las entidades del sector público institucional estatal, las personas de cada sexo:",
    ["No superarán el sesenta por ciento ni serán menos del cuarenta por ciento en el ámbito de cada entidad.", "No superarán el setenta por ciento ni serán menos del treinta por ciento.", "Serán exactamente el cincuenta por ciento en cada órgano.", "No superarán el sesenta por ciento en el conjunto del sector público estatal."],
    "Art. 84 bis.1.", "no superen el sesenta por ciento ni sean menos del cuarenta por ciento en el ámbito de cada entidad")
T.q("L40", "a85", "Reglas comunes", "Según el artículo 85.2 de la Ley 40/2015, el control de eficacia de las entidades del sector público institucional estatal será ejercido por:",
    ["El Departamento al que estén adscritos, a través de las inspecciones de servicios.", "La Intervención General de la Administración del Estado.", "El Tribunal de Cuentas.", "El Consejo de Ministros, a propuesta del Ministerio de Hacienda."],
    "Art. 85.2. La supervisión continua, en cambio, corresponde a Hacienda a través de la IGAE (85.3).", "será ejercido por el Departamento al que estén adscritos, a través de las inspecciones de servicios")
T.q("L40", "a87", "Reglas comunes", "Según el artículo 87.3 de la Ley 40/2015, la transformación de una entidad del sector público institucional estatal en agencia estatal deberá efectuarse:",
    ["Por ley.", "Por Real Decreto, aunque suponga modificación de la ley de creación.", "Por Orden del Ministerio de Hacienda.", "Por acuerdo del Consejo de Ministros."],
    "Art. 87.3: regla general Real Decreto; en agencias estatales, por ley.", "salvo en el caso de la transformación en agencias estatales que deberá efectuarse por ley")
T.q("L40", "a89", "Organismos públicos", "Según el artículo 89.2 de la Ley 40/2015, a los organismos públicos les corresponden, dentro de su esfera de competencia, las potestades administrativas precisas para el cumplimiento de sus fines, salvo:",
    ["La potestad expropiatoria.", "La potestad sancionadora.", "La potestad de autoorganización.", "La potestad de ejecución forzosa."],
    "Art. 89.2.", "salvo la potestad expropiatoria")
T.q("L40", "a91", "Organismos públicos", "Según el artículo 91.1 de la Ley 40/2015, la creación de los organismos públicos se efectuará:",
    ["Por Ley.", "Por Real Decreto del Consejo de Ministros.", "Por Orden del Ministerio de adscripción.", "Por acuerdo del Consejo de Ministros."],
    "Art. 91.1.", "La creación de los organismos públicos se efectuará por Ley")
T.q("L40", "a93", "Organismos públicos", "Según el artículo 93.2 de la Ley 40/2015, los estatutos de los organismos públicos se aprobarán:",
    ["Por Real Decreto del Consejo de Ministros a propuesta conjunta del Ministerio de Hacienda y del Ministerio al que el organismo esté vinculado o sea dependiente.", "Por ley, junto con la creación del organismo.", "Por Orden del Ministerio al que el organismo esté vinculado.", "Por el Consejo Rector del propio organismo."],
    "Art. 93.2.", "se aprobarán por Real Decreto del Consejo de Ministros a propuesta conjunta")
T.q("L40", "a94", "Organismos públicos", "Según el artículo 94.2 de la Ley 40/2015, la fusión de organismos públicos estatales se llevará a cabo:",
    ["Mediante norma reglamentaria, aunque suponga modificación de la Ley de creación.", "Mediante ley, en todo caso.", "Mediante acuerdo de los Consejos Rectores de los organismos fusionados.", "Mediante Orden del Ministerio de Hacienda."],
    "Art. 94.2.", "La fusión se llevará a cabo mediante norma reglamentaria, aunque suponga modificación de la Ley de creación")
T.q("L40", "a95", "Organismos públicos", "Según el artículo 95.2 de la Ley 40/2015, ¿cuál de los siguientes se considera un servicio común de los organismos públicos?",
    ["La asistencia jurídica.", "La asistencia técnica.", "La gestión de bienes muebles.", "La contratación privada."],
    "Art. 95.2 c).", "c) Asistencia jurídica.")
T.q("L40", "a96", "Organismos públicos", "Según el artículo 96.2 de la Ley 40/2015, cuando un organismo público incurra en causa de disolución, el titular de su máximo órgano de dirección lo comunicará al titular del departamento de adscripción en el plazo de:",
    ["Dos meses desde que concurra la causa de disolución.", "Un mes desde que concurra la causa de disolución.", "Tres meses desde que concurra la causa de disolución.", "Seis meses desde que concurra la causa de disolución."],
    "Art. 96.2.", "en el plazo de dos meses desde que concurra la causa de disolución")
T.q("L40", "a98", "Organismos autónomos", "Según el artículo 98.3 de la Ley 40/2015, cuando un organismo público tenga la naturaleza jurídica de organismo autónomo deberá figurar en su denominación la indicación «organismo autónomo» o su abreviatura:",
    ["O.A.", "E.P.E.", "A.E.", "O.P."],
    "Art. 98.3.", "deberá figurar en su denominación la indicación «organismo autónomo» o su abreviatura «O.A.»")
T.q("L40", "a100", "Organismos autónomos", "Según el artículo 100 de la Ley 40/2015, el personal al servicio de los organismos autónomos:",
    ["Será funcionario o laboral.", "Se regirá exclusivamente por el Derecho laboral.", "Será exclusivamente funcionario.", "Será estatutario."],
    "Art. 100.1.", "El personal al servicio de los organismos autónomos será funcionario o laboral")
T.q("L40", "a100", "Organismos autónomos", "Según el artículo 100.2 de la Ley 40/2015, el órgano de contratación de un organismo autónomo es:",
    ["El titular del máximo órgano de dirección del organismo autónomo.", "El Ministro del departamento de adscripción.", "El Consejo Rector del organismo.", "La Junta de Contratación del Ministerio de Hacienda."],
    "Art. 100.2.", "El titular del máximo órgano de dirección del organismo autónomo será el órgano de contratación")
T.q("L40", "a104", "Entidades públicas empresariales", "Según el artículo 104 de la Ley 40/2015, las entidades públicas empresariales se rigen por el Derecho privado, excepto en:",
    ["La formación de la voluntad de sus órganos y el ejercicio de las potestades administrativas que tengan atribuidas, entre otros aspectos.", "Su régimen de personal.", "Su régimen de contratación, en todo caso.", "Sus relaciones con terceros."],
    "Art. 104.", "excepto en la formación de la voluntad de sus órganos, en el ejercicio de las potestades administrativas que tengan atribuidas")
T.q("L40", "a106", "Entidades públicas empresariales", "Según el artículo 106.1 de la Ley 40/2015, el personal de las entidades públicas empresariales se rige, con las especificaciones y excepciones previstas:",
    ["Por el Derecho laboral.", "Por la normativa reguladora de los funcionarios públicos.", "Por el Derecho administrativo general.", "Por el Estatuto Marco del personal estatutario."],
    "Art. 106.1.", "El personal de las entidades públicas empresariales se rige por el Derecho laboral")
T.q("L40", "a103", "Entidades públicas empresariales", "Según el artículo 103.2 de la Ley 40/2015, las entidades públicas empresariales dependen:",
    ["De la Administración General del Estado o de un Organismo autónomo vinculado o dependiente de ésta.", "Exclusivamente del Ministerio de Hacienda.", "De una sociedad mercantil estatal.", "De una agencia estatal."],
    "Art. 103.2.", "dependen de la Administración General del Estado o de un Organismo autónomo vinculado o dependiente de ésta")
T.q("L40", "a1-3", "Agencias estatales", "Según el artículo 108 ter.4 de la Ley 40/2015, la aprobación del contrato de gestión de una agencia estatal tiene lugar:",
    ["Por Orden conjunta de los Ministerios de adscripción, de Política Territorial y Función Pública y de Hacienda.", "Por Real Decreto del Consejo de Ministros.", "Por acuerdo del Consejo Rector de la agencia.", "Por resolución del Director de la agencia."],
    "Art. 108 ter.4, párrafo tercero.", "por Orden conjunta de los Ministerios de adscripción, de Política Territorial y Función Pública y de Hacienda")
T.q("L40", "a1-4", "Agencias estatales", "Según el artículo 108 quater.11 de la Ley 40/2015, el director de la agencia estatal es nombrado y separado:",
    ["Por el Consejo Rector a propuesta del Presidente.", "Por el Consejo de Ministros a propuesta del Ministro de adscripción.", "Por el Presidente a propuesta del Consejo Rector.", "Por el Ministro de Hacienda."],
    "Art. 108 quater.11.", "Es nombrado y separado por el Consejo Rector a propuesta del Presidente")
T.q("L40", "a1-5", "Agencias estatales", "Según el artículo 108 quinquies.4 de la Ley 40/2015, para atender desfases temporales de tesorería, las agencias estatales pueden recurrir a pólizas de crédito o préstamo siempre que el saldo vivo no supere:",
    ["El 5 % de su presupuesto.", "El 10 % de su presupuesto.", "El 2 % de su presupuesto.", "El 15 % de su presupuesto."],
    "Art. 108 quinquies.4.", "siempre que el saldo vivo no supere el 5 % de su presupuesto")
T.q("L40", "a109", "Autoridades administrativas independientes", "Según el artículo 109.1 de la Ley 40/2015, la independencia funcional o especial autonomía de una autoridad administrativa independiente deberá determinarse:",
    ["En una norma con rango de Ley.", "En sus estatutos, aprobados por Real Decreto.", "Por acuerdo del Consejo de Ministros.", "Por Orden del Ministerio de vinculación."],
    "Art. 109.1.", "lo que deberá determinarse en una norma con rango de Ley")
T.q("L40", "a111", "Sociedades mercantiles estatales", "Según el artículo 111.1 a) de la Ley 40/2015, es sociedad mercantil estatal aquella en la que la participación directa en su capital social de la Administración General del Estado o de entidades del sector público institucional estatal sea:",
    ["Superior al 50 por 100.", "Igual o superior al 50 por 100.", "Superior al 25 por 100.", "Igual o superior al 75 por 100."],
    "Art. 111.1 a).", "sea superior al 50 por 100")
T.q("L40", "a114", "Sociedades mercantiles estatales", "Según el artículo 114.1 de la Ley 40/2015, la creación de una sociedad mercantil estatal será autorizada:",
    ["Mediante acuerdo del Consejo de Ministros.", "Mediante ley.", "Mediante Real Decreto del Ministerio de Hacienda.", "Por la Junta General de accionistas, sin autorización."],
    "Art. 114.1.", "será autorizada mediante acuerdo del Consejo de Ministros")
T.q("L40", "a113", "Sociedades mercantiles estatales", "Según el artículo 113 de la Ley 40/2015, las sociedades mercantiles estatales:",
    ["En ningún caso podrán disponer de facultades que impliquen el ejercicio de autoridad pública, sin perjuicio de que excepcionalmente la ley pueda atribuirles potestades administrativas.", "Podrán ejercer autoridad pública si lo prevén sus estatutos.", "Se rigen exclusivamente por el Derecho administrativo.", "Podrán ejercer la potestad expropiatoria."],
    "Art. 113.", "En ningún caso podrán disponer de facultades que impliquen el ejercicio de autoridad pública")
T.q("L40", "a118", "Consorcios", "Según el artículo 118.4 de la Ley 40/2015, en la denominación de los consorcios deberá figurar la indicación «consorcio» o su abreviatura:",
    ["C", "CONS.", "C.P.", "E.C."],
    "Art. 118.4.", "la indicación «consorcio» o su abreviatura «C»")
T.q("L40", "a120", "Consorcios", "Según el artículo 120.2 de la Ley 40/2015, el primer criterio, por orden de prioridad, para determinar la Administración a la que queda adscrito un consorcio es que:",
    ["Disponga de la mayoría de votos en los órganos de gobierno.", "Financie en más de un cincuenta por ciento la actividad del consorcio.", "Tenga mayor número de habitantes o extensión territorial.", "Ostente el mayor porcentaje de participación en el fondo patrimonial."],
    "Art. 120.2 a); las demás son las letras f), h) y g).", "a) Disponga de la mayoría de votos en los órganos de gobierno.")
T.q("L40", "a123", "Consorcios", "Según el artículo 123.2 de la Ley 40/2015, en los consorcios en los que participe la Administración General del Estado se requerirá:",
    ["Que su creación se autorice por ley.", "Que su creación se apruebe por Real Decreto, sin necesidad de convenio.", "Que su creación se autorice por Orden del Ministerio de Hacienda.", "Únicamente el informe del Consejo de Estado."],
    "Art. 123.2 a).", "a) Que su creación se autorice por ley.")
T.q("L40", "a126", "Consorcios", "Según el artículo 126.1 de la Ley 40/2015, el ejercicio del derecho de separación produce la disolución del consorcio salvo que el resto de miembros acuerden su continuidad y sigan permaneciendo en él, al menos:",
    ["Dos Administraciones, o entidades u organismos públicos vinculados o dependientes de más de una Administración.", "Tres Administraciones.", "La mitad de sus miembros originarios.", "La Administración de adscripción."],
    "Art. 126.1.", "al menos, dos Administraciones, o entidades u organismos públicos vinculados o dependientes de más de una Administración")
T.q("L40", "a128", "Fundaciones", "Según el artículo 128.2 de la Ley 40/2015, las fundaciones del sector público estatal:",
    ["No podrán ejercer potestades públicas.", "Podrán ejercer potestades públicas si lo prevén sus estatutos.", "Podrán asumir las competencias propias de las entidades fundadoras.", "Deberán realizar sus actividades con ánimo de lucro."],
    "Art. 128.2.", "Las fundaciones no podrán ejercer potestades públicas")
T.q("L40", "a129", "Fundaciones", "Según el artículo 129.4 de la Ley 40/2015, el cambio de adscripción de una fundación del sector público conllevará la modificación de los estatutos en un plazo no superior a:",
    ["Tres meses, contados desde el inicio del ejercicio presupuestario siguiente.", "Seis meses, contados desde el inicio del ejercicio presupuestario siguiente.", "Un mes, contado desde el cambio de adscripción.", "Un año, contado desde el cambio de adscripción."],
    "Art. 129.4. Seis meses es el plazo de los consorcios (art. 120.4).", "en un plazo no superior a tres meses, contados desde el inicio del ejercicio presupuestario siguiente")
T.q("L40", "a133", "Fundaciones", "Según el artículo 133.1 de la Ley 40/2015, la creación de las fundaciones del sector público estatal se realizará:",
    ["Por ley.", "Por acuerdo del Consejo de Ministros.", "Por Real Decreto.", "Por escritura pública otorgada por el Ministerio de adscripción."],
    "Art. 133.1.", "se realizará por ley que establecerá los fines de la fundación")
T.q("L40", "a137", "Fondos", "Según el artículo 137 de la Ley 40/2015, los fondos carentes de personalidad jurídica del sector público estatal se crean por Ley y se extinguirán:",
    ["Por norma de rango reglamentario.", "Por Ley, en todo caso.", "Por acuerdo del Consejo de Ministros.", "Automáticamente al agotarse su dotación."],
    "Art. 137.1 y 2.", "Con independencia de su creación por Ley se extinguirán por norma de rango reglamentario")

for cod, n, cat in [("L", 12, "Inventario"), ("P", 4, "Organismos públicos"), ("P", 5, "Agencias estatales"), ("P", 6, "Organismos autónomos"),
                    ("P", 7, "Entidades públicas empresariales"), ("X", 21, "Consorcios"), ("X", 22, "Composición")]:
    T.real(cod, n, cat)

# Flashcards
for q_, a_, cat in [
  ("¿Qué comprende el sector público según el art. 2.1 de la Ley 40/2015?", "AGE, Administraciones de las CC. AA., Entidades de la Administración Local y sector público institucional.", "Ámbito"),
  ("¿Qué integra el sector público institucional? (art. 2.2)", "Organismos públicos y entidades de derecho público vinculados o dependientes; entidades de derecho privado vinculadas o dependientes; Universidades públicas.", "Ámbito"),
  ("¿Qué entidades integran el sector público institucional estatal? (art. 84.1)", "Organismos públicos (OA, EPE, agencias estatales), autoridades administrativas independientes, sociedades mercantiles estatales, consorcios, fundaciones del sector público, fondos sin personalidad jurídica y universidades públicas no transferidas.", "Composición"),
  ("Sectores del sector público estatal según la LGP (art. 3)", "Administrativo, empresarial y fundacional.", "Composición"),
  ("¿Quién gestiona el Inventario de Entidades del Sector Público? (art. 82)", "La Intervención General de la Administración del Estado; es un registro público administrativo.", "Inventario"),
  ("Plazos de inscripción en el Inventario (art. 83)", "Notificar en 30 días hábiles; inscribir en 15 días hábiles desde la solicitud.", "Inventario"),
  ("Control de eficacia y supervisión continua (art. 85)", "Eficacia: Departamento de adscripción (inspecciones de servicios). Supervisión continua: Hacienda, a través de la IGAE.", "Reglas comunes"),
  ("¿Cómo se transforma una entidad estatal? (art. 87.3)", "Por Real Decreto, aunque modifique la ley de creación; en agencia estatal, por ley.", "Reglas comunes"),
  ("¿Qué potestad no tienen los organismos públicos? (art. 89.2)", "La expropiatoria.", "Organismos públicos"),
  ("Creación de organismos públicos y aprobación de sus estatutos (arts. 91 y 93)", "Creación por Ley; estatutos por Real Decreto del Consejo de Ministros a propuesta conjunta de Hacienda y del Ministerio de vinculación.", "Organismos públicos"),
  ("Servicios comunes de los organismos públicos (art. 95.2)", "Gestión de bienes inmuebles, sistemas de información y comunicación, asistencia jurídica, contabilidad y gestión financiera, publicaciones y contratación pública.", "Organismos públicos"),
  ("Régimen jurídico de los organismos autónomos (art. 99)", "Ley 40/2015, ley de creación, estatutos, Ley 39/2015, contratos, Ley 33/2003 y derecho administrativo; en defecto, derecho común.", "Organismos autónomos"),
  ("Régimen jurídico de las entidades públicas empresariales (art. 104)", "Derecho privado, salvo formación de la voluntad de sus órganos, ejercicio de potestades administrativas y aspectos regulados por normas administrativas.", "Entidades públicas empresariales"),
  ("Personal: OA, EPE, SME y fundaciones", "OA: funcionario o laboral (100.1). EPE: laboral, salvo funcionarios (106.1). SME y fundaciones: Derecho laboral (117.4 y 132.3).", "Personal"),
  ("Agencia estatal: contrato inicial de gestión (art. 108 ter.4)", "Lo propone el Consejo Rector en tres meses desde su constitución; se aprueba por Orden conjunta en un máximo de tres meses.", "Agencias estatales"),
  ("Endeudamiento de las agencias estatales (art. 108 quinquies.4)", "Prohibido salvo ley; pólizas por desfases de tesorería con saldo vivo hasta el 5 % del presupuesto.", "Agencias estatales"),
  ("Autoridad administrativa independiente (arts. 109 y 110)", "Regulación o supervisión externa con independencia fijada por norma con rango de Ley; se rige por su ley de creación, estatutos y legislación sectorial, y supletoriamente por la Ley 40/2015.", "Autoridades administrativas independientes"),
  ("Sociedad mercantil estatal (arts. 111, 113 y 114)", "Participación estatal superior al 50 %; derecho privado; nunca autoridad pública; creación autorizada por acuerdo del Consejo de Ministros.", "Sociedades mercantiles estatales"),
  ("Creación de consorcios con participación de la AGE (art. 123)", "Convenio; creación autorizada por ley; autorización previa del Consejo de Ministros; suscripción indelegable.", "Consorcios"),
  ("Cambio de adscripción: consorcio y fundación", "Consorcio: estatutos en seis meses (120.4). Fundación: tres meses (129.4).", "Consorcios"),
  ("Fundaciones del sector público estatal: creación y régimen (arts. 130 y 133)", "Creación por ley; se rigen por la Ley 40/2015, la Ley 50/2002 de Fundaciones, la legislación autonómica y el derecho privado.", "Fundaciones"),
  ("Fondos carentes de personalidad jurídica (art. 137)", "Creación por Ley; extinción por norma reglamentaria; abreviatura F.C.P.J.", "Fondos"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Sector público institucional", "Organismos públicos y entidades de derecho público, entidades de derecho privado vinculadas o dependientes de las Administraciones y Universidades públicas (Ley 40/2015, art. 2.2).", "s1", "Ámbito")
T.glos("Inventario de Entidades del Sector Público", "Registro público administrativo de todas las entidades del sector público institucional, gestionado por la IGAE (art. 82).", "s6", "Reglas comunes")
T.glos("Supervisión continua", "Control del Ministerio de Hacienda, a través de la IGAE, sobre las entidades estatales desde su creación hasta su extinción (art. 85.3).", "s7", "Reglas comunes")
T.glos("Medio propio y servicio técnico", "Entidad del sector público institucional que cumple los requisitos de la Ley de Contratos del Sector Público y del art. 86; lleva en su nombre «M.P.».", "s8", "Reglas comunes")
T.glos("Organismo público", "Entidad de derecho público con personalidad jurídica pública diferenciada, patrimonio y tesorería propios y autonomía de gestión, creada por ley (arts. 88, 89 y 91).", "s9", "Organismos públicos")
T.glos("Organismo autónomo", "Organismo público que desarrolla actividades propias de la Administración como organización instrumental diferenciada y dependiente; se rige por el derecho administrativo (arts. 98 y 99).", "s11", "Organismos públicos")
T.glos("Entidad pública empresarial", "Organismo público que ejerce potestades administrativas y realiza actividades susceptibles de contraprestación, financiado con ingresos de mercado; se rige por el Derecho privado con excepciones (arts. 103 y 104).", "s12", "Organismos públicos")
T.glos("Agencia estatal", "Organismo público creado para cumplir programas de políticas públicas, con autonomía funcional, responsabilidad por la gestión y control de resultados (art. 108 bis).", "s13", "Organismos públicos")
T.glos("Contrato de gestión", "Contrato plurianual que fija objetivos, planes, recursos y efectos del cumplimiento de una agencia estatal (art. 108 ter).", "s13", "Organismos públicos")
T.glos("Autoridad administrativa independiente", "Entidad de derecho público vinculada a la AGE con funciones de regulación o supervisión externa que requieren independencia funcional, determinada en norma con rango de ley (art. 109).", "s15", "Otras entidades")
T.glos("Sociedad mercantil estatal", "Sociedad mercantil en la que la participación estatal directa en el capital es superior al 50 % o hay control según la Ley del Mercado de Valores (art. 111).", "s16", "Otras entidades")
T.glos("Consorcio", "Entidad de derecho público creada por varias Administraciones o entidades del sector público institucional, entre sí o con entidades privadas, para actividades de interés común (art. 118).", "s17", "Otras entidades")
T.glos("Fundación del sector público estatal", "Fundación con aportación mayoritaria, patrimonio de origen público en más del 50 % o mayoría de votos en el patronato del sector público estatal (art. 128).", "s18", "Otras entidades")
T.glos("Fondo carente de personalidad jurídica", "Fondo del sector público estatal creado por ley y adscrito a la AGE, que se extingue por norma reglamentaria (art. 137).", "s19", "Otras entidades")

# Cronología (fechas de los metadatos del BOE)
T.hito("2003", "Ley 47/2003, de 26 de noviembre, General Presupuestaria (BOE de 27-11-2003)", "Arts. 2 y 3: sector público estatal y su división en administrativo, empresarial y fundacional", "normativo", "s3")
T.hito("2015", "Ley 40/2015, de 1 de octubre, de Régimen Jurídico del Sector Público (BOE de 2-10-2015)", "Título II: organización y funcionamiento del sector público institucional (en vigor, en su redacción original, desde el 2-10-2016)", "normativo", "s0")
T.hito("2020", "Ley 11/2020, de 30 de diciembre, de Presupuestos Generales del Estado para 2021 (BOE de 31-12-2020)", "Añade los arts. 108 bis a 108 sexies (agencias estatales) y da la redacción vigente del art. 84 (en vigor el 1-1-2021)", "normativo", "s13")
T.hito("2024", "Ley Orgánica 2/2024, de 1 de agosto, de representación paritaria y presencia equilibrada de mujeres y hombres (BOE de 2-8-2024)", "Añade el art. 84 bis (presencia equilibrada en las entidades del sector público institucional estatal)", "normativo", "s7")
T.hito("2025", "Ley 7/2025, de 28 de julio, por la que se crea la Agencia Estatal de Salud Pública (BOE de 29-7-2025)", "Crea una agencia estatal con el régimen de los arts. 88 a 97 y 108 bis a 108 sexies de la Ley 40/2015", "normativo", "s13")

T.publicar()
