# -*- coding: utf-8 -*-
"""Tema IV.6 (B4T06): Los contratos regulados por la Ley de Contratos del Sector
Público (II). Tipos. Características generales.
Método del I.2: mapa → bloques (I a V) con guía; cada artículo, texto literal del
BOE + ficha de casillas fijas; cierre 1 (preguntas oficiales) y cierre 2 (repaso).
La parte general (preparación, adjudicación, efectos, modificación, extinción,
invalidez y recursos) es del tema IV.5: aquí solo se remite a él."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

def L(art, *res, solo=None, titulo=None):
    return lit("LCSP", f"Artículo {art}", list(res), solo=solo, titulo=titulo)
def C(art, frag): return c("LCSP", f"Artículo {art}", frag)
U = unidad
T29 = "Artículo 29. Plazo de duración de los contratos y de ejecución de la prestación (LCSP)"

T = Tema("B4T06",
  "Cinco preguntas: I. Qué tipos de contrato define la Ley 9/2017 (arts. 12 a 18 y 34.2) · II. Qué tiene de propio el contrato de obras (arts. 231 a 246) · III. Qué tienen de propio las concesiones de obras y de servicios (arts. 29.6, 247, 248, 251, 254, 256 a 258, 261, 263, 264, 267, 270, 279, 280, 283 a 285, 287 a 291, 294, 296 y 297) · IV. Qué tiene de propio el suministro (arts. 29.4 y 5 y 298 a 307) · V. Qué tiene de propio el contrato de servicios (arts. 308 a 315). Cada artículo: texto literal del BOE y ficha.",
  ["LCSP", "Tipos de contrato", "Arts. 12-18", "Contrato de obras", "Concesión de obras", "Concesión de servicios", "Riesgo operacional", "Suministro", "Servicios", "Contrato mixto", "Proyecto y replanteo", "Plazo de garantía", "Estudio de viabilidad", "Arts. 231-315"])

# =============================================================================
T.ap("s0", "Mapa del tema: cinco preguntas", """
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque IV, tema 6):
> Los contratos regulados por la Ley de Contratos del Sector Público (II). Tipos. Características generales.

### El hilo conductor

El epígrafe se lee como **cinco preguntas encadenadas**. La primera responde a «Tipos»; las otras cuatro, a «Características generales» de cada tipo, que la Ley 9/2017, de Contratos del Sector Público (LCSP), regula en el Libro II, Título II:

| Bloque | Pregunta | Artículos de la LCSP |
|---|---|---|
| **I** | ¿Qué tipos de contrato define la Ley? | Arts. 12 a 18 y 34.2 |
| **II** | ¿Qué tiene de propio el contrato de obras? | Arts. 231 a 246 |
| **III** | ¿Qué tienen de propio las concesiones de obras y de servicios? | Arts. 29.6, 247, 248, 251, 254, 256 a 258, 261, 263, 264, 267, 270, 279, 280 y 283 (obras) y 284, 285, 287 a 291, 294, 296 y 297 (servicios) |
| **IV** | ¿Qué tiene de propio el contrato de suministro? | Arts. 29.4 y 5 y 298 a 307 |
| **V** | ¿Qué tiene de propio el contrato de servicios? | Arts. 308 a 315 |

!> **La idea que une los cinco bloques:** la Ley define **cinco tipos** (obras, concesión de obras, concesión de servicios, suministro y servicios) y el **mixto**. Las dos **concesiones** se distinguen de la obra y del servicio porque el contratista cobra **explotando** la obra o el servicio y asume el **riesgo operacional**. Cada tipo tiene sus reglas propias de preparación, ejecución y resolución, que se suman a las generales.

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- La parte general de los contratos (concepto, clases, preparación, adjudicación, efectos, modificación, extinción, invalidez y recursos) es el tema anterior: cuando hace falta, se indica «ver tema IV.5».
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
# BLOQUE I
T.ap("bI", "I. ¿Qué tipos de contrato define la Ley? (arts. 12 a 18 y 34.2)", donde(
  "Primera pregunta del tema. Antes de ver las reglas propias de cada contrato hay que saber **cómo los define la Ley**: el tipo decide qué normas se aplican.",
  ["1 Calificación, obras y concesión de obras (arts. 12 a 14)", "2 Concesión de servicios, suministro y servicios (arts. 15 a 17)", "3 Contratos mixtos (arts. 18 y 34.2)", "4 Cuadro de los tipos de contrato"]))

T.ap("s1", "I.1 Calificación, contrato de obras y concesión de obras (arts. 12 a 14)", "\n\n".join([
"La Ley califica los contratos por su **objeto**: si encaja en una de sus definiciones, se rige por ella.",
U("1.1 Calificación de los contratos (art. 12)",
  L(12, "se calificarán de acuerdo con las normas contenidas en la presente sección"),
  fichab("Regla para saber qué tipo de contrato es cada uno",
         f"Los contratos {C(12, 'que celebren las entidades pertenecientes al sector público')}",
         ["::Dos grupos:", "Obras, concesión de obras, concesión de servicios, suministro y servicios: por las definiciones de los arts. 13 a 18", f"Los restantes: {C(12, 'según las normas de derecho administrativo o de derecho privado que les sean de aplicación')}"],
         "—",
         "Son **cinco** tipos definidos más el **mixto** (art. 18). El carácter administrativo o privado de cada contrato (arts. 25 a 27): ver tema IV.5.")),
U("1.2 Contrato de obras (art. 13)",
  L(13, "La ejecución de una obra", "tenga por objeto un bien inmueble", "obra completa"),
  fichab("Contrato cuyo objeto es una obra: el resultado de trabajos de construcción o de ingeniería civil sobre un inmueble",
         "Entidad del sector público contratante y contratista",
         ["::Objeto (13.1):", "a) Ejecutar una obra (sola o con la redacción del proyecto) o los trabajos del Anexo I", "b) Realizar, por cualquier medio, una obra que cumpla los requisitos de la entidad que ejerza una influencia decisiva en su tipo o proyecto", "También es obra modificar la forma o sustancia del terreno o de su vuelo, o mejorar el medio físico o natural (13.2)"],
         "—",
         f"Regla de la **obra completa** (13.3): la {C(13, 'susceptible de ser entregada al uso general o al servicio correspondiente')}. Cabe contratar partes por proyectos independientes si son de utilización independiente o pueden definirse sustancialmente, con autorización previa del órgano de contratación.")),
U("1.3 Contrato de concesión de obras (art. 14)",
  L(14, "únicamente en el derecho a explotar la obra", "riesgo operacional", "riesgo de demanda o el de suministro"),
  fichab("Contrato de obras en el que el concesionario cobra explotando la obra",
         "Entidad del sector público concedente y concesionario",
         ["::Contraprestación (14.1):", f"O bien {C(14, 'únicamente en el derecho a explotar la obra')}", f"O bien en {C(14, 'dicho derecho acompañado del de percibir un precio')}", "Puede incluir adecuación, reforma y modernización, reposición y gran reparación (14.2) y obras accesorias o vinculadas (14.3)"],
         "Duración máxima: 40 años (→ III.1.1)",
         f"La clave es el **riesgo operacional** (14.4): de **demanda**, de **suministro** o ambos. Existe cuando {C(14, 'no esté garantizado que, en condiciones normales de funcionamiento, el mismo vaya a recuperar las inversiones realizadas')}; la pérdida posible no puede ser {C(14, 'meramente nominal o desdeñable')}.")),
]), 2)

T.ap("s2", "I.2 Concesión de servicios, suministro y servicios (arts. 15 a 17)", "\n\n".join([
U("2.1 Contrato de concesión de servicios (art. 15)",
  L(15, "la gestión de un servicio cuya prestación sea de su titularidad o competencia", "riesgo operacional"),
  fichab("Contrato por el que se encomienda la gestión de un servicio y el concesionario cobra explotándolo",
         f"{C(15, 'uno o varios poderes adjudicadores')} encomiendan a {C(15, 'una o varias personas, naturales o jurídicas')}",
         [f"{C(15, 'a título oneroso')}", "Contrapartida: el derecho a explotar los servicios, solo o con el de percibir un precio", "Transfiere al concesionario el riesgo operacional, en los términos del art. 14.4 (→ I.1.3)"],
         "Duración máxima: 40, 25 o 10 años (→ III.1.1)",
         "Concedente: **poderes adjudicadores**; objeto: un servicio **de su titularidad o competencia**. Lo que la separa del contrato de servicios es la **explotación** con **riesgo operacional**.")),
U("2.2 Contrato de suministro (art. 16)",
  L(16, "productos o bienes muebles", "propiedades incorporales o valores negociables", "programas de ordenador desarrollados a medida, que se considerarán contratos de servicios"),
  fichab("Contrato para adquirir o arrendar productos o bienes muebles",
         "Entidad del sector público adquirente y empresario",
         ["::Objeto (16.1): adquisición, arrendamiento financiero o arrendamiento, con o sin opción de compra. Siempre son suministro (16.3):", "a) Entregas sucesivas por precio unitario sin cuantía total definida, por depender de las necesidades del adquirente", "b) Equipos y sistemas de telecomunicaciones o de tratamiento de la información, sus dispositivos y programas (salvo programas a medida)", "c) Fabricación con características peculiares fijadas por la entidad contratante", "d) Adquisición de energía primaria o transformada"],
         "Duración máxima de los de prestación sucesiva y del arrendamiento de bienes muebles: 5 años (→ IV.1.1)",
         f"Programas de ordenador **a medida** = **servicios**. No es suministro el contrato sobre **propiedades incorporales o valores negociables**. La fabricación es suministro {C(16, 'aun cuando esta se obligue a aportar, total o parcialmente, los materiales precisos')}.")),
U("2.3 Contrato de servicios (art. 17)",
  L(17, "prestaciones de hacer", "ejercicio de la autoridad inherente a los poderes públicos"),
  fichab("Contrato de prestaciones de hacer: una actividad o un resultado distinto de una obra o un suministro",
         "Entidad del sector público y contratista",
         ["Desarrollo de una actividad, u obtención de un resultado distinto de una obra o un suministro", "Incluye el servicio ejecutado de forma sucesiva y por precio unitario"],
         "Duración máxima de los de prestación sucesiva: 5 años (→ IV.1.1)",
         f"Límite: {C(17, 'No podrán ser objeto de estos contratos los servicios que impliquen ejercicio de la autoridad inherente a los poderes públicos')}. El mismo límite rige en la concesión de servicios (art. 284.1, → III.5.1).")),
]), 2)

T.ap("s3", "I.3 Contratos mixtos (arts. 18 y 34.2)", "\n\n".join([
U("3.1 Contrato mixto y norma aplicable a su adjudicación (art. 18)",
  L(18, "se atenderá al carácter de la prestación principal", "el objeto principal se determinará en función de cuál sea el mayor de los valores estimados de los respectivos servicios o suministros", "supere los 50.000 euros"),
  fichab("Contrato con prestaciones de otro u otros contratos de distinta clase",
         "Entidad del sector público; solo en las condiciones del art. 34.2 (→ I.3.2)",
         ["::Normas de adjudicación (18.1):", "Obras, suministros o servicios entre sí: prestación principal", "Servicios + suministros, o servicios especiales del anexo IV + otros servicios: el mayor valor estimado", "Con concesiones: no separables → prestación principal; separables y contrato único → normas de obras, suministros o servicios si su valor supera los umbrales de los arts. 20, 21 y 22; si no, las de las concesiones", "Efectos, cumplimiento y extinción: art. 122.2 (ver tema IV.5)"],
         "Obra de más de **50.000 euros** dentro del mixto: proyecto (arts. 231 y ss.); con elementos de concesión: estudio de viabilidad y, en su caso, anteproyecto (arts. 247, 248 y 285)",
         "Servicios + suministros: decide el **mayor valor estimado**, no el orden en el pliego ni el número de unidades. Cayó en 2025 (→ Cierre 1).")),
U("3.2 Cuándo cabe un contrato mixto (art. 34.2)",
  lit("LCSP", "Artículo 34", ["directamente vinculadas entre sí", "unidad funcional"], solo=[2]),
  fichab("Límite para fusionar prestaciones de distintos contratos",
         "Entidad contratante",
         "Solo si las prestaciones están directamente vinculadas y son complementarias, de modo que exijan tratarlas como una unidad funcional",
         "—",
         "No basta la conveniencia: hacen falta **vinculación directa** y **complementariedad** que exijan tratarlas como **unidad funcional** para una necesidad o un fin institucional propio.")),
]), 2)

T.ap("s4", "I.4 Cuadro de los tipos de contrato (esquema)", "\n\n".join([
"*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*",
"""| Tipo | Art. | Objeto | Cómo cobra el contratista | Dato que se pregunta |
|---|---|---|---|---|
| Obras | 13 | Obra: resultado sobre un **bien inmueble** | Precio | Obra **completa** |
| Concesión de obras | 14 | Prestaciones del art. 13 | Derecho a **explotar** la obra (solo o con precio) | **Riesgo operacional** (demanda o suministro) |
| Concesión de servicios | 15 | Gestión de un servicio de titularidad o competencia del poder adjudicador | Derecho a **explotar** el servicio (solo o con precio) | Riesgo operacional (art. 14.4) |
| Suministro | 16 | Adquisición o arrendamiento de **bienes muebles** | Precio | Programas **a medida** = servicios; energía, fabricación |
| Servicios | 17 | Prestaciones **de hacer** | Precio | Nunca ejercicio de **autoridad** |
| Mixto | 18 | Prestaciones de varios tipos | — | Servicios + suministros: **mayor valor estimado** |""",
resumen([
  "La Ley define **cinco** tipos y el **mixto**; los demás contratos se califican por el derecho administrativo o privado que les sea aplicable (art. 12).",
  "Obras: resultado sobre un **inmueble**, y obra **completa**. Suministro: **bienes muebles**. Servicios: prestaciones **de hacer**, nunca con ejercicio de autoridad.",
  "Concesiones: el contratista cobra **explotando** la obra o el servicio y asume el **riesgo operacional** (de demanda o de suministro).",
  "Mixto: solo con prestaciones vinculadas y complementarias (34.2); servicios + suministros se rigen por el de **mayor valor estimado**."],
  "Siguiente: II. ¿Qué tiene de propio el contrato de obras?"),
]), 2)

# =============================================================================
# BLOQUE II
T.ap("bII", "II. ¿Qué tiene de propio el contrato de obras? (arts. 231 a 246)", donde(
  "Segunda pregunta. Ya sabemos qué es un contrato de obras; ahora, sus **reglas propias**: el **proyecto** antes de adjudicar, el **replanteo**, la ejecución y modificación, la **recepción**, la **garantía** y la **resolución**.",
  ["1 Proyecto, supervisión y replanteo (arts. 231 a 236)", "2 Ejecución y modificación (arts. 237 a 242)", "3 Recepción, garantía, vicios ocultos y resolución (arts. 243 a 246)"]))

T.ap("s5", "II.1 Actuaciones preparatorias: proyecto, supervisión y replanteo (arts. 231 a 236)", "\n\n".join([
U("1.1 El proyecto de obras (art. 231)",
  L(231, "elaboración, supervisión, aprobación y replanteo"),
  fichab("El proyecto: requisito previo para adjudicar un contrato de obras; define con precisión su objeto",
         f"La aprobación corresponde {C(231, 'al órgano de contratación salvo que tal competencia esté específicamente atribuida a otro órgano por una norma jurídica')}",
         ["Elaboración → supervisión → aprobación → replanteo", "Si se adjudican juntos proyecto y obra, la ejecución queda condicionada a esos trámites (231.2)"],
         "—",
         "Cuatro trámites, en este orden: **elaboración, supervisión, aprobación y replanteo**. La aprobación es del **órgano de contratación**, salvo norma que la atribuya a otro.")),
U("1.2 Clasificación de las obras (art. 232)",
  L(232, "afecten fundamentalmente a la estructura resistente"),
  fichab("Clasificación de las obras a efectos de elaborar los proyectos",
         "—",
         ["::Cuatro grupos (232.1):", "a) Primer establecimiento, reforma, restauración, rehabilitación o gran reparación", "b) Reparación simple", "c) Conservación y mantenimiento", "d) Demolición"],
         "—",
         "Reparación por causas **fortuitas o accidentales**: **gran** reparación si afecta fundamentalmente a la **estructura resistente**; si no, **simple**. Menoscabo por el **natural uso**: **conservación**. Restauración: **mantiene** la funcionalidad; rehabilitación: le da **una nueva**.")),
U("1.3 Contenido de los proyectos (art. 233)",
  L(233, "inferiores a 500.000 euros de presupuesto base de licitación", "estudio geotécnico", solo=list(range(1, 12))),
  fichab("Documentos que debe tener todo proyecto de obras",
         "Redactor del proyecto; si la Administración contrató íntegramente su elaboración, responde en los términos de la Ley (233.4)",
         ["::Contenido mínimo (233.1):", "Memoria", "Planos de conjunto y de detalle", "Pliego de prescripciones técnicas particulares", "Presupuesto", "Programa de desarrollo de los trabajos o plan de obra", "Referencias para el replanteo", "Estudio (o estudio básico) de seguridad y salud", "La documentación que prevean otras normas"],
         "Por debajo de **500.000 euros** (primer establecimiento, reforma o gran reparación) y en los demás grupos del art. 232 se pueden simplificar, refundir o suprimir documentos; el de seguridad y salud, solo si lo prevé su normativa",
         f"Salvo que sea incompatible con la naturaleza de la obra, {C(233, 'el proyecto deberá incluir un estudio geotécnico de los terrenos')} (233.3).")),
U("1.4 Contratación conjunta de proyecto y obra (art. 234)",
  L(234, "tendrá carácter excepcional", solo=[1, 2, 3, 4, 5]),
  fichab("El empresario redacta el proyecto y ejecuta la obra",
         "El contratista presenta el proyecto; el órgano de contratación lo supervisa, aprueba y replantea",
         ["::Solo en dos supuestos justificados en el expediente (234.1):", "a) Motivos de orden técnico que obliguen a vincular al empresario a los estudios", "b) Dimensión excepcional o dificultades técnicas singulares", "Antes de licitar, la Administración redacta el anteproyecto o documento similar (o, por causas justificadas, solo las bases técnicas)"],
         "—",
         "Es **excepcional**. Si no hay acuerdo sobre los precios, el contratista queda **exonerado** de ejecutar las obras y solo tiene derecho al pago de la **redacción del proyecto**.")),
U("1.5 Supervisión de proyectos (art. 235)",
  L(235, "igual o superior a 500.000 euros, IVA excluido"),
  fichab("Informe de supervisión del proyecto antes de aprobarlo",
         "Las oficinas o unidades de supervisión de proyectos, a solicitud del órgano de contratación",
         "Verifican que se han tenido en cuenta las disposiciones generales y la normativa técnica aplicables",
         "Preceptivo con presupuesto base de licitación **igual o superior a 500.000 euros**, IVA excluido; por debajo, facultativo",
         "Por debajo de 500.000 euros el informe es **facultativo**, salvo obras que afecten a la **estabilidad, seguridad o estanqueidad**: entonces es **preceptivo**.")),
U("1.6 Replanteo del proyecto (art. 236)",
  L(236, "comprobar la realidad geométrica de la misma y la disponibilidad de los terrenos precisos"),
  fichab("Replanteo: comprobación previa de la obra y de los terrenos",
         "Órgano de contratación",
         "Se comprueban la realidad geométrica de la obra, la disponibilidad de los terrenos y los supuestos básicos del proyecto; después el proyecto se incorpora al expediente",
         "Tras aprobar el proyecto y **antes** de aprobar el expediente de contratación",
         "En obras **hidráulicas, de transporte y de carreteras** se dispensa la disponibilidad previa de los terrenos, pero no pueden empezar sin formalizar la **ocupación** conforme a la Ley de Expropiación Forzosa.")),
]), 2)

T.ap("s6", "II.2 Ejecución y modificación del contrato de obras (arts. 237 a 242)", "\n\n".join([
U("2.1 Comprobación del replanteo (art. 237)",
  L(237, "no podrá ser superior a un mes desde la fecha de su formalización"),
  fichab("Acta con la que empieza la ejecución de la obra",
         "El servicio de la Administración encargado de las obras, en presencia del contratista; firman ambas partes",
         "Se comprueba el replanteo hecho antes de la licitación y se levanta acta; un ejemplar va al órgano que celebró el contrato",
         "El plazo del contrato, que no puede superar **un mes desde la formalización**, salvo casos excepcionales justificados",
         "La ejecución **comienza** con el acta de comprobación del replanteo. Su demora injustificada es causa de resolución (→ II.3.3).")),
U("2.2 Ejecución de las obras y responsabilidad del contratista (art. 238)",
  L(238, "hasta que se cumpla el plazo de garantía"),
  fichab("Cómo se ejecutan las obras",
         "El contratista, con las instrucciones de la Dirección facultativa",
         "Con estricta sujeción al pliego de cláusulas administrativas particulares y al proyecto",
         "Responde de los defectos de construcción hasta que se cumpla el **plazo de garantía**",
         "Las instrucciones **verbales** solo vinculan si se **ratifican por escrito** en el más breve plazo posible.")),
U("2.3 Fuerza mayor (art. 239)",
  L(239, "siempre que no exista actuación imprudente por parte del contratista"),
  fichab("Indemnización al contratista por daños de fuerza mayor",
         "El contratista, si no hay actuación imprudente por su parte",
         ["::Casos de fuerza mayor (239.2):", "a) Incendios causados por la electricidad atmosférica", "b) Fenómenos naturales de efectos catastróficos", "c) Destrozos violentos en tiempo de guerra, robos tumultuosos o alteraciones graves del orden público"],
         "—",
         "El incendio ha de estar causado por la **electricidad atmosférica**. La misma lista sirve para el reequilibrio de las concesiones (arts. 270 y 290, → III.3.4).")),
U("2.4 Certificaciones y abonos a cuenta (art. 240)",
  L(240, "mensualmente, en los primeros diez días siguientes al mes al que correspondan", solo=[1, 3]),
  fichab("Pago de la obra mientras se ejecuta",
         "La Administración expide las certificaciones; cobra el contratista",
         ["Certificaciones de la obra ejecutada conforme a proyecto en el periodo", "Abonos a cuenta por operaciones preparatorias (instalaciones, acopio de materiales o equipos de maquinaria pesada), asegurados con garantía"],
         "Mensuales, en los **diez** primeros días siguientes al mes al que correspondan, salvo previsión contraria del pliego",
         "Son **pagos a cuenta**: se rectifican en la medición final y no suponen **aprobación y recepción** de las obras.")),
U("2.5 Obras a tanto alzado y con precio cerrado (art. 241)",
  L(241, "precio cerrado", solo=[1, 2, 3, 4, 5, 6]),
  fichab("Retribución sin precios unitarios",
         "El órgano de contratación, en el pliego",
         ["Tanto alzado: sin precios unitarios", "Precio cerrado: el precio ofertado no varía y no se abonan las modificaciones para corregir errores u omisiones del proyecto"],
         "Precio cerrado: abono **mensual**, en proporción a la obra ejecutada en el mes",
         "Requisitos del precio cerrado: previsto en el **pliego**; unidades **definidas en el proyecto y replanteadas** antes de la licitación; acceso de los interesados al **terreno**.")),
U("2.6 Modificación del contrato de obras (art. 242)",
  L(242, "no tendrá derecho a reclamar indemnización alguna", "plazo mínimo de tres días hábiles", "10 por ciento del precio del contrato inicial", "3 por ciento del presupuesto primitivo", "20 por ciento del precio inicial del contrato", solo=[1, 2, 4, 5, 6, 7, 8, 9, 10, 11]),
  fichab("Reglas propias de la modificación en obras (el régimen general de modificación: ver tema IV.5)",
         "Órgano de contratación; el Director facultativo pide autorización para modificar el proyecto",
         ["Obligatorias para el contratista si se acuerdan conforme al art. 206", "Unidades nuevas: precios fijados por la Administración con audiencia del contratista; si no los acepta, se pueden contratar con otro, ejecutar directamente o resolver", "Expediente: redacción y aprobación técnica, audiencia del contratista y del redactor (mínimo tres días) y aprobación por el órgano de contratación"],
         ["::Cifras:", "Audiencia sobre precios nuevos: mínimo **tres días hábiles**", "No es modificación el exceso de mediciones de hasta el **10 %** del precio del contrato inicial", "Ni los precios nuevos que no suban el precio global ni afecten a más del **3 %** del presupuesto primitivo", "Continuación provisional (Ministro): hasta el **20 %** del precio inicial"],
         "Si se **suprimen o reducen** unidades de obra, el contratista **no** tiene derecho a indemnización.")),
]), 2)

T.ap("s7", "II.3 Recepción, plazo de garantía, vicios ocultos y resolución (arts. 243 a 246)", "\n\n".join([
U("3.1 Recepción y plazo de garantía (art. 243)",
  L(243, "Dentro del plazo de tres meses contados a partir de la recepción", "supere los doce millones de euros", "no supere en ningún caso los cinco meses", "no podrá ser inferior a un año salvo casos especiales"),
  fichab("Recepción de las obras terminadas y plazo de garantía",
         "Concurren un facultativo de la Administración, el director de las obras y el contratista (asistido, si quiere, de su facultativo)",
         "Si las obras están en buen estado se dan por recibidas, con acta, y empieza el plazo de garantía; si no, se señalan los defectos y un plazo para remediarlos",
         ["::Plazos:", "Certificación final: **tres meses** desde la recepción", "Obras de valor estimado superior a **doce millones** con liquidación y medición especialmente complejas: ampliable si lo prevén los pliegos, sin superar **cinco meses**", "Garantía: la del pliego, **no inferior a un año** salvo casos especiales", "Informe del director: en los **quince días** anteriores al fin de la garantía; pago de lo pendiente: **sesenta días**"],
         "Sin plazo de garantía: sondeos y prospecciones infructuosos o dragados (243.4). Cabe recepción **parcial** por fases (243.5). Cayó en 2025 (→ Cierre 1).")),
U("3.2 Responsabilidad por vicios ocultos (art. 244)",
  L(244, "quince años a contar desde la recepción", "dos años"),
  fichab("Responsabilidad del contratista después del plazo de garantía",
         "El contratista, si la ruina o los deterioros graves se deben a su incumplimiento del contrato",
         "Responde de los daños por ruina o deterioros graves incompatibles con la función de la obra, y de los daños materiales por vicios en los elementos estructurales",
         ["::Plazos:", "Responsabilidad: **quince años** desde la recepción", "Prescripción de las acciones por daños materiales: **dos años** desde que se producen o manifiestan"],
         "Pasados **quince** años sin daño, la responsabilidad queda **totalmente extinguida**. Cayó en 2025 (→ Cierre 1).")),
U("3.3 Causas de resolución del contrato de obras (art. 245)",
  L(245, "superior a cuatro meses", "superior a ocho meses"),
  fichab("Causas de resolución propias de las obras (las generales: ver tema IV.5)",
         "—",
         ["::Además de las generales:", "a) Demora injustificada en la comprobación del replanteo", "b) Suspensión de la iniciación de las obras por más de cuatro meses", "c) Suspensión de las obras por más de ocho meses por parte de la Administración", "d) Desistimiento"],
         "**4** meses (iniciación) · **8** meses (obras ya iniciadas)",
         "4 meses = **antes** de empezar; 8 meses = obras **iniciadas**. Los mismos plazos rigen en suministro y servicios (→ IV.3.1 y → V.3.1).")),
U("3.4 Efectos de la resolución (art. 246)",
  L(246, "2 por cien", "3 por cien", "6 por cien", solo=[1, 2, 3, 4]),
  fichab("Liquidación e indemnización al resolver el contrato de obras",
         "Órgano de contratación, citando al contratista a la comprobación y medición",
         "Comprobación, medición y liquidación de las obras realizadas, con los saldos a favor o en contra del contratista",
         ["::Indemnización al contratista (IVA excluido):", "Demora en la comprobación del replanteo: **2 %** del precio de adjudicación", "Desistimiento antes de iniciar o suspensión de la iniciación por más de 4 meses: **3 %** del precio de adjudicación", "Desistimiento con obras iniciadas o suspensión por más de 8 meses: **6 %** del precio de las obras dejadas de realizar (beneficio industrial)"],
         "**2 – 3 – 6**: replanteo, antes de empezar, ya empezadas. El 6 % se calcula sobre las obras **dejadas de realizar**.")),
resumen([
  "Antes de adjudicar: **proyecto** (elaboración, supervisión, aprobación y replanteo); supervisión preceptiva desde **500.000 euros**.",
  "La ejecución empieza con el **acta de comprobación del replanteo** (máximo **un mes** desde la formalización); certificaciones **mensuales**.",
  "Recepción → certificación final en **3 meses** (hasta **5** si supera 12 millones y es compleja) → garantía de **un año** como mínimo → vicios ocultos **15 años**.",
  "Resolución: suspensión de la iniciación más de **4** meses o de la obra más de **8**; indemnizaciones del **2, 3 y 6 %**."],
  "Siguiente: III. ¿Qué tienen de propio las concesiones de obras y de servicios?"),
]), 2)

# =============================================================================
# BLOQUE III
T.ap("bIII", "III. ¿Qué tienen de propio las concesiones de obras y de servicios? (arts. 29.6, 247, 248, 251, 254, 256 a 258, 261, 263, 264, 267, 270, 279, 280, 283 a 285, 287 a 291, 294, 296 y 297)", donde(
  "Tercera pregunta. Las concesiones son contratos **largos**, en los que el concesionario **financia y explota** y asume el **riesgo operacional**. Por eso tienen reglas propias: estudio de viabilidad, tarifas, equilibrio económico, secuestro, rescate y reversión. La Ley regula a fondo la de obras y la aplica, en lo no previsto, a la de servicios.",
  ["1 Duración y actuaciones preparatorias (arts. 29.6, 247 y 248)", "2 Concesión de obras: ejecución, derechos y prerrogativas (arts. 251, 254, 256 a 258 y 261)", "3 Secuestro, penalidades, tarifas y equilibrio económico (arts. 263, 264, 267 y 270)", "4 Extinción de la concesión de obras (arts. 279, 280 y 283)", "5 Concesión de servicios: ámbito, pliegos y obligaciones (arts. 284, 285 y 287 a 289)", "6 Concesión de servicios: equilibrio, reversión y resolución (arts. 290, 291, 294, 296 y 297)"]))

T.ap("s8", "III.1 Duración y actuaciones preparatorias de la concesión (arts. 29.6, 247 y 248)", "\n\n".join([
U("1.1 Duración de las concesiones (art. 29.6)",
  L(29, "Cuarenta años", "Veinticinco años", "Diez años", "15 por ciento de su duración inicial", solo=list(range(13, 22)), titulo=T29 + " · apartado 6"),
  fichab("Plazo de las concesiones de obras y de servicios",
         "Se fija en el pliego de cláusulas administrativas particulares",
         "Duración limitada, según las obras y servicios; si pasa de cinco años, no más de lo razonable para recuperar las inversiones con un rendimiento sobre el capital invertido",
         ["::Máximos, con prórrogas incluidas:", "**40 años**: concesión de obras, y de servicios que comprenda la ejecución de obras y la explotación de servicio", "**25 años**: concesión de servicios no relacionada con servicios sanitarios", "**10 años**: concesión de servicios sanitarios (sin obras)", "Ampliación para reequilibrar: hasta un **15 %** de la duración inicial (arts. 270 y 290)"],
         "No computan las suspensiones por causa imputable a la Administración concedente o por fuerza mayor; el retraso imputable al concesionario no amplía el plazo.")),
U("1.2 Estudio de viabilidad (art. 247)",
  L(247, "estudio de viabilidad", "por el plazo de un mes, prorrogable por idéntico plazo", "equivaldrá a la no aceptación del estudio", "5 puntos porcentuales adicionales"),
  fichab("Estudio previo y obligatorio a la decisión de construir y explotar una obra en concesión",
         "Lo acuerda y aprueba el órgano que corresponda de la Administración concedente; se admite la iniciativa privada",
         ["::Contenido mínimo (247.2), entre otros puntos:", "Finalidad y justificación de las obras", "Ventajas de la concesión frente a otros tipos contractuales", "Previsiones de demanda y rentabilidad", "Riesgos operativos y tecnológicos", "Coste de la inversión y sistema de financiación", "Valor actual neto, para evaluar el riesgo operacional"],
         ["::Plazos:", "Información pública: **un mes**, prorrogable por otro", "Informe de otras Administraciones (obra fuera del planeamiento): **un mes**", "Estudio de iniciativa privada: decisión en **tres meses** (o plazo mayor fijado, nunca superior a **seis**); el silencio equivale a la **no aceptación**"],
         "El autor privado de un estudio que acaba en concesión tiene **5 puntos porcentuales** más en la licitación; si no gana, resarcimiento de gastos **+5 %**. Puede sustituirse por un estudio de viabilidad **económico-financiera**. Cayó en 2025 (→ Cierre 1).")),
U("1.3 Anteproyecto de construcción y explotación (art. 248)",
  L(248, "podrá acordar la redacción del correspondiente anteproyecto", solo=[1, 2, 3, 4, 5, 6, 7, 8]),
  fichab("Documento técnico y económico de la obra en concesión",
         "La Administración concedente, una vez aprobado el estudio de viabilidad",
         ["::Contenido mínimo (248.2):", "Memoria", "Planos de situación generales y de conjunto", "Presupuesto, con el coste de las expropiaciones", "Estudio del régimen de utilización y explotación (financiación y régimen tarifario)"],
         "Información pública: **un mes**, prorrogable por otro",
         "El anteproyecto es **potestativo** («podrá acordar»); el estudio de viabilidad, **obligatorio**. Al aprobarlo, la Administración insta el reconocimiento de la **utilidad pública** a efectos expropiatorios.")),
]), 2)

T.ap("s9", "III.2 Concesión de obras: ejecución, derechos y prerrogativas (arts. 251, 254, 256 a 258 y 261)", "\n\n".join([
U("2.1 Efectos, cumplimiento y extinción (art. 251)",
  L(251, "excluidos los artículos 208 y 210"),
  fichab("Régimen de efectos, cumplimiento y extinción de la concesión de obras",
         "—",
         "Por la LCSP (régimen general: ver tema IV.5), con exclusiones",
         "—",
         "Nunca se aplican los arts. **208 y 210**; los arts. **192.2, 193 y 195** solo en la **fase de construcción**. La misma regla para la concesión de servicios (art. 286).")),
U("2.2 Riesgo y ventura (art. 254)",
  L(254, "a riesgo y ventura del concesionario"),
  fichab("Principio de riesgo y ventura en la ejecución de las obras",
         "El concesionario, salvo en la parte de obra que ejecute la Administración (régimen general del contrato de obras)",
         "Ejecuta a su riesgo y ventura y asume además el riesgo operacional",
         "—",
         "Fuerza mayor con mayores costes: se **ajusta el plan económico-financiero**; si impide por completo las obras: **resolución**, con abono de lo ejecutado y de los mayores costes de endeudamiento con terceros.")),
U("2.3 Comprobación de las obras (art. 256)",
  L(256, "llevará implícita la autorización para la apertura de las mismas al uso público", solo=[1, 2, 4]),
  fichab("Acta de comprobación al terminar las obras",
         "La Administración concedente",
         "Acta de comprobación con un documento de valoración de la obra ejecutada, que hace constar la inversión realizada",
         "Desde la aprobación del acta empieza la **fase de explotación** (y la garantía de la obra ejecutada por terceros)",
         "Aprobar el acta de comprobación = autorizar la **apertura al uso público**.")),
U("2.4 Derechos del concesionario (art. 257)",
  L(257, "percibir la tarifa por uso", "se incorporarán al dominio público", solo=[1, 2, 3, 4, 5, 6, 7, 8, 9]),
  fichab("Derechos del concesionario de obras",
         "El concesionario",
         ["Explotar las obras y percibir la tarifa", "Mantenimiento del equilibrio económico (art. 270)", "Utilizar los bienes de dominio público necesarios", "Pedir a la Administración las expropiaciones, servidumbres y desahucios necesarios", "Ceder e hipotecar la concesión, con autorización previa", "Titulizar sus derechos de crédito"],
         "—",
         "Los bienes y derechos expropiados que quedan afectos a la concesión pasan al **dominio público**. Ceder e hipotecar exige **autorización previa** del órgano de contratación.")),
U("2.5 Obligaciones del concesionario (art. 258)",
  L(258, "igualdad, universalidad y no discriminación"),
  fichab("Obligaciones generales del concesionario de obras",
         "El concesionario",
         ["Ejecutar y explotar las obras, asumiendo el riesgo operacional", "Admitir a todo usuario (igualdad, universalidad y no discriminación), con la tarifa que proceda", "Cuidar del buen orden y la calidad de las obras", "Indemnizar los daños a terceros que le sean imputables", "Proteger el dominio público vinculado a la concesión"],
         "—",
         "El concesionario puede dictar instrucciones para el buen orden, pero los **poderes de policía** siguen siendo del órgano de contratación.")),
U("2.6 Prerrogativas de la Administración (art. 261)",
  L(261, "Establecer, en su caso, las tarifas máximas", solo=list(range(1, 13))),
  fichab("Prerrogativas y derechos del órgano de contratación en la concesión de obras",
         "El órgano de contratación o el que determine la legislación específica",
         ["Interpretar, modificar por interés público y resolver", "Restablecer el equilibrio económico a favor del interés público (art. 270)", "Fijar las tarifas máximas", "Vigilar, inspeccionar e imponer penalidades", "Asumir la explotación en caso de secuestro o intervención", "Policía del uso y explotación; condiciones temporales de uso por interés general"],
         "—",
         "Las tarifas que fija la Administración son **máximas** (→ III.3.3).")),
]), 2)

T.ap("s10", "III.3 Secuestro, penalidades, tarifas y equilibrio económico (arts. 263, 264, 267 y 270)", "\n\n".join([
U("3.1 Secuestro o intervención de la concesión (art. 263)",
  L(263, "previa audiencia del concesionario", "de tres años"),
  fichab("La Administración asume temporalmente la explotación",
         "El órgano de contratación, previa audiencia del concesionario; designa uno o varios interventores",
         ["::Supuestos (263.1):", "El concesionario no puede hacer frente temporalmente, con grave daño social, a la explotación por causas ajenas a él", "Incumplimiento grave que ponga en peligro la explotación", "Se notifica y, si no corrige la deficiencia en el plazo fijado, se ejecuta"],
         "Temporal; como máximo **tres años**, prórrogas incluidas",
         "La explotación intervenida es **por cuenta y riesgo del concesionario**. Si al terminar el plazo no garantiza sus obligaciones, se **resuelve** el contrato.")),
U("3.2 Penalidades y multas coercitivas (art. 264)",
  L(264, "10 por cien del presupuesto total de la obra", "20 por cien de los ingresos", "3.000 euros", solo=[1, 2, 3, 7]),
  fichab("Sanciones económicas por incumplimientos del concesionario",
         "El órgano de contratación, según el catálogo de incumplimientos leves y graves de los pliegos",
         "Penalidades proporcionales al incumplimiento y a la importancia económica de la explotación; además, multas coercitivas si persiste el incumplimiento tras requerimiento",
         ["::Límites:", "Fase de construcción: **10 %** del presupuesto total de la obra", "Fase de explotación: **20 %** anual de los ingresos del año anterior", "Si el daño es mayor, el límite sube hasta el valor del daño", "Multa coercitiva: **3.000 euros** diarios, a falta de legislación específica"],
         "**10 %** en construcción / **20 %** en explotación. Las penalidades del art. 264 se aplican también a la concesión de servicios si son compatibles (art. 293.2).")),
U("3.3 Retribución: la tarifa (art. 267)",
  L(267, "prestación patrimonial de carácter público no tributario", "carácter de máximas", solo=[1, 2, 3, 4, 5, 6]),
  fichab("Retribución del concesionario por el uso de las obras",
         "La pagan los usuarios o la Administración; la fija el órgano de contratación en la adjudicación",
         ["Tarifa: prestación patrimonial de carácter público no tributario", "Puede pagarla la Administración según la disponibilidad o la utilización (con índices de corrección automáticos si hay pagos por disponibilidad)", "Ingresos de la zona comercial vinculada"],
         "Revisión de tarifas: Capítulo II del Título III del Libro I (ver tema IV.5)",
         "Las tarifas son **máximas**: el concesionario puede aplicar tarifas **inferiores**. Los ingresos por aportaciones públicas, tarifas y zona comercial se **separan contablemente**.")),
U("3.4 Mantenimiento del equilibrio económico (art. 270)",
  L(270, "incumplimiento de las previsiones de la demanda", "15 por ciento de su duración inicial", "5 por ciento del importe neto de la cifra de negocios", solo=list(range(1, 14))),
  fichab("Restablecimiento del equilibrio económico de la concesión de obras",
         "A favor de la parte que corresponda (concesionario o interés público)",
         ["::Procede (270.2):", "a) Modificación de las obras por la Administración (art. 262)", "b) Actuaciones obligatorias de la Administración concedente que rompan de forma directa y sustancial la economía del contrato", "Fuerza mayor (casos del art. 239) que la rompa de forma directa y sustancial", "Medidas: tarifas, retribución, reducción del plazo u otras cláusulas económicas"],
         "Prórroga: hasta el **15 %** de la duración inicial (casos de la letra b) y del último párrafo del apartado 2, si más del **50 %** de la retribución procede de tarifas de los usuarios). Desistimiento por onerosidad: incremento de costes de al menos el **5 %** de la cifra de negocios",
         "**Nunca** hay reequilibrio por **incumplimiento de las previsiones de la demanda**: es el riesgo operacional. El desistimiento por onerosidad extraordinaria no da indemnización a ninguna parte.")),
]), 2)

T.ap("s11", "III.4 Extinción de la concesión de obras (arts. 279, 280 y 283)", "\n\n".join([
U("4.1 Causas de resolución (art. 279)",
  L(279, "superior a seis meses", "El rescate de la explotación de las obras", "más eficaz y eficiente que la concesional"),
  fichab("Causas de resolución propias de la concesión de obras",
         "—",
         ["::Además de las del art. 211, salvo sus letras d) y e) (ver tema IV.5):", "a) Ejecución hipotecaria desierta o imposible por falta de interesados autorizados", "b) Demora de más de seis meses de la Administración en entregar la contraprestación, los terrenos o los medios auxiliares", "c) Rescate", "d) Supresión de la explotación por interés público", "e) Imposibilidad de explotación por acuerdos posteriores de la Administración", "f) Secuestro más largo que el máximo del art. 263.3 sin garantizar las obligaciones"],
         "Demora de la Administración: más de **seis meses**",
         "**Rescate**: decisión unilateral por interés público, **pese a la buena gestión** del concesionario, para gestionar directamente; hay que acreditar que la gestión directa es **más eficaz y eficiente**.")),
U("4.2 Efectos de la resolución (art. 280)",
  L(280, "criterio de amortización lineal", solo=[1, 2, 3, 4]),
  fichab("Qué se abona al concesionario al resolver",
         "La Administración concedente",
         ["Causa imputable a la Administración: inversiones (expropiaciones, obras y bienes necesarios) según su grado de amortización lineal, más daños y perjuicios", "Causa no imputable a la Administración: el valor de la concesión (art. 281)", "Causa imputable al concesionario: se le incauta la garantía e indemniza el exceso de daños"],
         "La cantidad se fija en **tres meses**, salvo otro plazo del pliego",
         "Amortización **lineal**. No es imputable a la Administración la resolución por las letras a), b) y f) del art. 211 ni por las a) y f) del art. 279.")),
U("4.3 Destino de las obras a la extinción (art. 283)",
  L(283, "no podrán ser objeto de embargo"),
  fichab("Entrega de las obras a la Administración al terminar la concesión",
         "El concesionario entrega; se levanta acta de recepción formal (art. 243)",
         "Entrega en buen estado de conservación y uso de las obras, los bienes e instalaciones necesarios para la explotación y los de la zona comercial",
         "—",
         "Los pliegos pueden prever la **demolición** y reposición del terreno. Los bienes que vayan a revertir son **inembargables**.")),
]), 2)

T.ap("s12", "III.5 Concesión de servicios: ámbito, pliegos y obligaciones (arts. 284, 285 y 287 a 289)", "\n\n".join([
U("5.1 Ámbito de la concesión de servicios (art. 284)",
  L(284, "siempre que sean susceptibles de explotación económica por particulares", "ejercicio de la autoridad inherente a los poderes públicos"),
  fichab("Gestión indirecta de servicios mediante concesión",
         "La Administración, sobre servicios de su titularidad o competencia",
         ["Servicios susceptibles de explotación económica por particulares", "Servicios públicos: antes debe establecerse su régimen jurídico (asunción como propia, alcance de las prestaciones y aspectos jurídicos, económicos y administrativos)", "El contrato fija el ámbito funcional y territorial"],
         "—",
         "Nunca mediante concesión los servicios que impliquen **ejercicio de la autoridad** inherente a los poderes públicos.")),
U("5.2 Estudio de viabilidad en la concesión de servicios (art. 285.2)",
  L(285, "tendrán carácter vinculante en los supuestos en que concluyan en la inviabilidad del proyecto", solo=[8, 9]),
  fichab("Actuación previa obligatoria de la concesión de servicios",
         "Órgano de contratación",
         ["Estudio de viabilidad o, en su caso, estudio de viabilidad económico-financiera", "Si hay obras: además, cuando proceda, anteproyecto y proyecto"],
         "—",
         "El estudio solo **vincula** cuando concluye la **inviabilidad** del proyecto. Los pliegos (285.1) deben prever la división en **lotes**, fijar, en su caso, las tarifas y el canon, y atribuir siempre el **riesgo operacional** al contratista.")),
U("5.3 Ejecución de la concesión de servicios (art. 287)",
  L(287, "poderes de policía", "únicamente podrán ser objeto de hipoteca"),
  fichab("Cómo presta el servicio el concesionario",
         "El concesionario; la Administración conserva los poderes de policía si es un servicio público",
         "Con estricta sujeción al contrato y en sus plazos; y, en su caso, ejecutando las obras según el proyecto aprobado",
         "—",
         "Hipoteca **solo** si la concesión conlleva **obras o instalaciones fijas** y en garantía de deudas relacionadas con la concesión.")),
U("5.4 Obligaciones generales del concesionario de servicios (art. 288)",
  L(288, "deberá seguir prestando el servicio hasta que se formalice el nuevo contrato"),
  fichab("Obligaciones del concesionario de servicios",
         "El concesionario",
         ["Prestar el servicio con la continuidad convenida y garantizar su uso", "Cuidar del buen orden del servicio", "Indemnizar los daños a terceros, salvo los imputables a la Administración", "No discriminar por nacionalidad en los suministros derivados"],
         "Tras extinguirse por cumplimiento: sigue prestando el servicio **hasta que se formalice** el nuevo contrato",
         "La continuidad se mantiene hasta la **formalización** del nuevo contrato, no hasta su adjudicación.")),
U("5.5 Prestaciones económicas (art. 289)",
  L(289, "tarifas", "canon o participación"),
  fichab("Contraprestación del concesionario de servicios",
         "La percibe el concesionario, directamente de los usuarios o de la propia Administración",
         ["Retribución en función de la utilización del servicio", "Tarifas: prestación patrimonial de carácter público no tributario, revisables conforme al Libro I", "Contabilidad diferenciada de ingresos y gastos"],
         "—",
         "Si el pliego lo establece, es el **concesionario** quien paga a la Administración un **canon o participación**.")),
]), 2)

T.ap("s13", "III.6 Concesión de servicios: equilibrio, reversión y resolución (arts. 290, 291, 294, 296 y 297)", "\n\n".join([
U("6.1 Modificación y equilibrio económico (art. 290)",
  L(290, "únicamente por razones de interés público", "15 por ciento de su duración inicial", solo=[1, 2, 3, 4, 5, 6, 7, 8, 9]),
  fichab("Modificación del servicio y restablecimiento del equilibrio",
         "La Administración; compensa a la parte que corresponda",
         ["Puede modificar las características del servicio y las tarifas solo por interés público y en los casos de la Ley", "Reequilibrio: por modificación, por actuaciones obligatorias de la Administración o por fuerza mayor (art. 239)"],
         "Ampliación del plazo: hasta el **15 %** de la duración inicial, respetando los máximos legales",
         "Igual que en obras: **no** hay reequilibrio por incumplimiento de las **previsiones de la demanda**; los acuerdos sin trascendencia económica no dan indemnización.")),
U("6.2 Reversión (art. 291)",
  L(291, "revertirá a la Administración"),
  fichab("Vuelta del servicio a la Administración al terminar la concesión",
         "El contratista entrega las obras e instalaciones; la Administración prepara la entrega",
         "Entrega en el estado de conservación y funcionamiento adecuados",
         "Durante un **periodo prudencial** anterior, fijado en el pliego",
         "Los bienes que vayan a revertir **no pueden ser embargados**.")),
U("6.3 Causas y efectos de la resolución (art. 294)",
  L(294, "más eficaz y eficiente que la concesional"),
  fichab("Causas de resolución propias de la concesión de servicios",
         "—",
         ["::Además de las del art. 211, salvo sus letras d) y e):", "a) Ejecución hipotecaria desierta o imposible", "b) Demora de más de seis meses de la Administración en la contraprestación o los medios auxiliares", "c) Rescate para la gestión directa", "d) Supresión del servicio por interés público", "e) Imposibilidad de explotación por acuerdos posteriores de la Administración", "f) Secuestro más largo que el máximo del art. 263.3"],
         "Demora de la Administración: más de **seis meses**",
         "Son prácticamente las **mismas** causas que en la concesión de obras (art. 279). Efectos: art. 295, paralelo al 280 (→ III.4.2).")),
U("6.4 Subcontratación (art. 296)",
  L(296, "solo podrá recaer sobre prestaciones accesorias"),
  fichab("Límite de la subcontratación en la concesión de servicios", "El concesionario", "Con el régimen general de los arts. 215 a 217 (ver tema IV.5)", "—",
         "Solo **prestaciones accesorias**: la prestación principal del servicio no se subcontrata.")),
U("6.5 Regulación supletoria (art. 297)",
  L(297, "respecto al contrato de concesión de obras"),
  fichab("Norma supletoria de la concesión de servicios", "—", "En lo no previsto, la regulación de la concesión de obras, si es compatible", "—",
         "Además, el art. 293 remite expresamente al secuestro (art. 263) y a las penalidades (art. 264) de la concesión de obras.")),
"### Cuadro comparativo de las dos concesiones (esquema)",
"*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*",
"""| | Concesión de obras | Concesión de servicios |
|---|---|---|
| Definición | Art. 14 | Art. 15 |
| Duración máxima | 40 años | 40 (con obras), 25 o 10 (sanitarios) años (art. 29.6) |
| Actuación previa | Estudio de viabilidad obligatorio; anteproyecto potestativo (arts. 247 y 248) | Estudio de viabilidad, vinculante si concluye la inviabilidad (art. 285.2) |
| Retribución | Tarifa máxima (art. 267) | Tarifas; canon si lo prevé el pliego (art. 289) |
| Hipoteca | Con autorización (arts. 257 y 273) | Solo con obras o instalaciones fijas (art. 287.3) |
| Reequilibrio | Art. 270; prórroga hasta el 15 % | Art. 290; ampliación hasta el 15 % |
| Secuestro | Máximo tres años (art. 263) | Mismo régimen (art. 293) |
| Al terminar | Entrega de las obras (art. 283) | Reversión del servicio (art. 291) |""",
resumen([
  "Duración máxima: **40** años (obras, y servicios con obras), **25** (servicios) y **10** (servicios sanitarios); ampliación de hasta un **15 %** para reequilibrar.",
  "Antes de la concesión: **estudio de viabilidad** (información pública de **un mes**, prorrogable); anteproyecto potestativo.",
  "Tarifas **máximas**; reequilibrio por modificación, actuación obligatoria de la Administración o fuerza mayor, **nunca** por la demanda.",
  "Secuestro hasta **3 años**; rescate solo si la gestión directa es **más eficaz y eficiente**; bienes reversibles **inembargables**."],
  "Siguiente: IV. ¿Qué tiene de propio el contrato de suministro?"),
]), 2)

# =============================================================================
# BLOQUE IV
T.ap("bIV", "IV. ¿Qué tiene de propio el contrato de suministro? (arts. 29.4 y 5 y 298 a 307)", donde(
  "Cuarta pregunta. El suministro tiene por objeto **bienes muebles**: sus reglas propias tratan de la **entrega**, quién paga el **transporte**, el **riesgo** antes de la entrega, el pago (incluso con otros bienes) y la resolución.",
  ["1 Duración, arrendamiento y fabricación (arts. 29.4 y 5, 298 y 299)", "2 Ejecución: entrega, pago, gastos y garantía (arts. 300 a 305)", "3 Resolución (arts. 306 y 307)"]))

T.ap("s14", "IV.1 Duración, arrendamiento y fabricación (arts. 29.4 y 5, 298 y 299)", "\n\n".join([
U("1.1 Duración de los suministros y servicios (art. 29.4 y 5)",
  L(29, "cinco años", solo=[7, 12], titulo=T29 + " · apartados 4 (párrafo primero) y 5"),
  fichab("Plazo máximo de los suministros y servicios de prestación sucesiva y de los arrendamientos de muebles",
         "El órgano de contratación, al fijar la duración y acordar las prórrogas",
         "Incluye las prórrogas",
         "**Cinco años**, con prórrogas, tanto en los suministros y servicios de prestación sucesiva como en el arrendamiento de bienes muebles",
         "El 29.4 admite excepciones (recuperación de inversiones, mantenimiento exclusivo, servicios a las personas) y una prórroga de hasta nueve meses mientras empieza la ejecución del nuevo contrato (29.4, párrafos segundo a quinto; no se copian aquí).")),
U("1.2 Arrendamiento (art. 298)",
  L(298, "asumirá durante el plazo de vigencia del contrato la obligación del mantenimiento"),
  fichab("Especialidad del suministro en forma de arrendamiento",
         "El arrendador o empresario",
         "Mantiene el objeto arrendado durante la vigencia del contrato",
         "—",
         "El **canon de mantenimiento** se fija **separadamente** del precio del arriendo.")),
U("1.3 Contratos de fabricación (art. 299)",
  L(299, "salvo las relativas a su publicidad y procedimiento de adjudicación"),
  fichab("Régimen del suministro de fabricación", "El órgano de contratación decide en el pliego qué normas de obras aplica",
         "Se aplican directamente las normas generales y especiales del contrato de obras que determine el pliego", "—",
         "Publicidad y adjudicación: **siempre** las del **suministro**; el resto, las de **obras** que fije el pliego.")),
]), 2)

T.ap("s15", "IV.2 Ejecución del suministro: entrega, pago, gastos y garantía (arts. 300 a 305)", "\n\n".join([
U("2.1 Entrega y recepción (art. 300)",
  L(300, "salvo que esta hubiere incurrido en mora al recibirlos"),
  fichab("Entrega de los bienes y reparto del riesgo",
         "El contratista entrega; la Administración recibe",
         "En el tiempo y lugar fijados y conforme a las prescripciones técnicas y cláusulas administrativas",
         "Entre la entrega y la recepción formal, la custodia es de la **Administración**",
         "Pérdidas o averías **antes de la entrega**: sin indemnización para el adjudicatario, **salvo mora** de la Administración en recibir. Perecederos recibidos: responde la Administración de su gestión, uso o caducidad.")),
U("2.2 Pago del precio (art. 301)",
  L(301, "10 por ciento del precio del contrato"),
  fichab("Derecho del adjudicatario al precio",
         "El adjudicatario",
         "Cobra los suministros efectivamente entregados y formalmente recibidos",
         "Con precios unitarios, se pueden aumentar las unidades hasta el **10 %** del precio sin expediente de modificación, si lo prevé el pliego y hay financiación",
         "El 10 % exige previsión en el **pliego** y financiación acreditada en el expediente originario.")),
U("2.3 Pago en metálico y en otros bienes (art. 302)",
  L(302, "50 por cien del precio total", solo=[1, 3, 4]),
  fichab("Pago de parte del precio con bienes de la Administración",
         "Órgano de contratación (pliego y acuerdo de entrega)",
         "Parte en dinero y parte en bienes de la misma clase, por razones técnicas o económicas justificadas",
         "Los bienes entregados no pueden superar el **50 %** del precio total",
         "El acuerdo de entrega supone por sí solo la **baja en el inventario** y, en su caso, la **desafectación**; su valor es un elemento de la adjudicación.")),
U("2.4 Facultades de la Administración en la fabricación (art. 303)",
  L(303, "inspeccionar y de ser informada del proceso de fabricación"),
  fichab("Control de la Administración durante la fabricación", "La Administración",
         "Inspección, información, análisis, ensayos y pruebas de materiales, sistemas de control de calidad e instrucciones", "—",
         "Puede **ordenar o realizar por sí misma** análisis, ensayos y pruebas.")),
U("2.5 Gastos de entrega y recepción (art. 304)",
  L(304, "serán de cuenta del contratista"),
  fichab("Quién paga la entrega y el transporte", "El contratista, salvo pacto en contrario",
         "Bienes no aptos para recibirse: se hace constar en el acta y se dan instrucciones para subsanar o suministrar de nuevo", "—",
         "Entrega **y** transporte al lugar convenido: **contratista**, salvo **pacto en contrario**. Cayó en 2025 (→ Cierre 1).")),
U("2.6 Vicios o defectos durante el plazo de garantía (art. 305)",
  L(305, "rechazar los bienes dejándolos de cuenta del contratista"),
  fichab("Garantía de los bienes suministrados",
         "La Administración reclama; el contratista repone o repara y tiene derecho a ser oído",
         ["Reposición de los bienes inadecuados o su reparación, si basta", "Si no son aptos y no bastará reponer o reparar: rechazo antes de expirar la garantía, sin pagar o recuperando el precio"],
         "Terminada la garantía sin reparos ni denuncia, el contratista queda **exento** de responsabilidad",
         "El rechazo debe hacerse **antes de que expire** el plazo de garantía.")),
]), 2)

T.ap("s16", "IV.3 Resolución del contrato de suministro (arts. 306 y 307)", "\n\n".join([
U("3.1 Causas de resolución (art. 306)",
  L(306, "por plazo superior a cuatro meses", "por un plazo superior a ocho meses"),
  fichab("Causas de resolución propias del suministro (las generales: ver tema IV.5)", "—",
         ["a) Desistimiento antes de iniciar el suministro o suspensión de la iniciación por más de cuatro meses, por causa imputable a la Administración", "b) Desistimiento una vez iniciado o suspensión por más de ocho meses acordada por la Administración"],
         "**4** meses (iniciación, desde la fecha señalada en el contrato para la entrega) · **8** meses (iniciado), salvo plazo menor del pliego",
         "Los mismos **4 y 8 meses** que en obras (→ II.3.3) y servicios (→ V.3.1); en suministro y servicios el pliego puede fijar uno **menor** (en obras, no).")),
U("3.2 Efectos de la resolución (art. 307)",
  L(307, "3 por ciento", "6 por ciento"),
  fichab("Efectos de la resolución del suministro", "Las partes",
         "Devolución recíproca de bienes y pagos; si no es posible o conveniente, la Administración paga lo entregado y recibido de conformidad",
         ["::Indemnización (IVA excluido):", "Letra a) del art. 306: **3 %** del precio de adjudicación", "Letra b): **6 %** del precio de los suministros dejados de realizar (beneficio industrial)"],
         "Los mismos **3 y 6 %** que en obras; el 2 % por demora en el replanteo es solo de obras.")),
resumen([
  "Duración máxima: **cinco años** con prórrogas (suministros de prestación sucesiva y arrendamiento de muebles).",
  "Arrendamiento: el **arrendador** mantiene el bien; fabricación: normas de **obras** salvo publicidad y adjudicación.",
  "Riesgo **antes de la entrega**: del contratista, salvo mora de la Administración; gastos de entrega y transporte: **contratista**, salvo pacto.",
  "Pago con otros bienes: hasta el **50 %**; aumento de unidades sin modificación: hasta el **10 %**. Resolución: **4 y 8 meses**; **3 y 6 %**."],
  "Siguiente: V. ¿Qué tiene de propio el contrato de servicios?"),
]), 2)

# =============================================================================
# BLOQUE V
T.ap("bV", "V. ¿Qué tiene de propio el contrato de servicios? (arts. 308 a 315)", donde(
  "Quinta pregunta. El contrato de servicios es el de **prestaciones de hacer**. Sus reglas propias tratan de la **propiedad intelectual**, la prohibición de usarlo para **contratar personal**, el precio, los servicios a la ciudadanía y la responsabilidad del **redactor de proyectos** de obra.",
  ["1 Contenido, límites y precio (arts. 308 a 310)", "2 Ejecución y servicios con prestaciones directas a la ciudadanía (arts. 311 y 312)", "3 Resolución y contratos de elaboración de proyectos (arts. 313 a 315)"]))

T.ap("s17", "V.1 Contenido, límites y precio de los contratos de servicios (arts. 308 a 310)", "\n\n".join([
U("1.1 Contenido y límites (art. 308)",
  L(308, "llevarán aparejada la cesión de este a la Administración contratante", "instrumentar la contratación de personal", "consolidación de las personas"),
  fichab("Límites propios del contrato de servicios",
         "Entidad contratante y contratista",
         ["Productos con propiedad intelectual o industrial: se cede el derecho a la Administración, salvo que los pliegos o el contrato digan otra cosa", "Aplicaciones informáticas: objeto definible por componentes de prestación", "Redacción de proyectos y dirección de obra: conjuntamente si separarlas merma la calidad (motivado)"],
         "—",
         "**En ningún caso** sirve para contratar personal (tampoco los menores) ni cabe la **consolidación** como personal de la entidad al extinguirse.")),
U("1.2 Determinación del precio (art. 309)",
  L(309, "10 por ciento del precio del contrato"),
  fichab("Sistemas de precio de los servicios",
         "El pliego de cláusulas administrativas",
         "Por componentes de la prestación, unidades de ejecución o de tiempo, tanto alzado, honorarios por tarifas o una combinación",
         "Con unidades de ejecución: no es modificación la variación de unidades hasta el **10 %** del precio, si lo prevé el pliego",
         "En servicios complejos con inversiones que pasen al patrimonio de la entidad cabe un sistema de retribución que las compense (309.2).")),
U("1.3 Actividades docentes (art. 310)",
  L(310, "no serán de aplicación a la preparación y adjudicación del contrato", "bastará la designación o nombramiento por autoridad competente"),
  fichab("Régimen especial de cursos, seminarios, conferencias y actividades similares",
         "Personas físicas que realizan la actividad",
         "La LCSP no se aplica a su preparación y adjudicación; cabe pago parcial anticipado con garantía, sin cesión",
         "—",
         "Solo si las imparten **personas físicas**. Para acreditar el contrato basta la **designación o nombramiento**.")),
]), 2)

T.ap("s18", "V.2 Ejecución y servicios con prestaciones directas a la ciudadanía (arts. 311 y 312)", "\n\n".join([
U("2.1 Ejecución, responsabilidad y cumplimiento (art. 311)",
  L(311, "responsable de la calidad técnica de los trabajos"),
  fichab("Cómo se ejecuta y se da por cumplido el contrato de servicios",
         "El contratista, con las instrucciones del responsable del contrato (o, si no lo hay, de los servicios del órgano de contratación)",
         ["La Administración comprueba si la prestación se ajusta a lo pactado y exige subsanar defectos", "Si no se adecua por vicios imputables al contratista: rechazo, sin pago o recuperando el precio"],
         "Terminada la garantía sin reparos: el contratista queda **exento** de responsabilidad (salvo arts. 314 y 315)",
         "Los contratos **de mera actividad o de medios** se extinguen al cumplirse el **plazo** o sus prórrogas.")),
U("2.2 Servicios con prestaciones directas a favor de la ciudadanía (art. 312)",
  L(312, "no podrán ser objeto de embargo", "dependencias o instalaciones diferenciadas"),
  fichab("Reglas para los servicios que se prestan directamente a los ciudadanos",
         "La Administración y el adjudicatario",
         ["Régimen jurídico previo del servicio", "Obligaciones de continuidad, buen orden, indemnización y entrega de obras e instalaciones", "Poderes de policía de la Administración", "Secuestro o intervención si hay perturbación grave no reparable por otros medios"],
         "—",
         "Bienes afectos **inembargables**; prestación en **dependencias diferenciadas** para evitar la confusión de plantillas; resolución también por las letras c), d) y f) del art. 294.")),
]), 2)

T.ap("s19", "V.3 Resolución y contratos de elaboración de proyectos de obra (arts. 313 a 315)", "\n\n".join([
U("3.1 Causas y efectos de la resolución (art. 313)",
  L(313, "3 por ciento", "6 por ciento"),
  fichab("Resolución propia de los contratos de servicios (las causas generales: ver tema IV.5)", "—",
         ["a) Desistimiento antes de iniciar o suspensión de la iniciación por más de cuatro meses (causa imputable al órgano de contratación)", "b) Desistimiento iniciada la prestación o suspensión por más de ocho meses", "c) Los contratos complementarios se resuelven con el principal"],
         ["::Indemnización (IVA excluido):", "Letras a) y c): **3 %** del precio de adjudicación", "Letra b): **6 %** de los servicios dejados de prestar"],
         "En todo caso se paga lo **realizado y recibido**. Mismos 4 y 8 meses que obras y suministro (→ II.3.3 y → IV.3.1), salvo plazo **menor** en el pliego.")),
U("3.2 Subsanación de errores del proyecto (art. 314)",
  L(314, "no podrá exceder de dos meses", "25 por ciento del precio del contrato", "un mes improrrogable", "la mitad del precio del contrato"),
  fichab("Contrato de servicios de elaboración íntegra de un proyecto de obra: corrección de deficiencias",
         "El órgano de contratación exige; el contratista subsana",
         ["Primer plazo de subsanación (máx. dos meses)", "Si no corrige: resolución (garantía + 25 %) o nuevo plazo (un mes improrrogable + penalidad del 25 %)", "Nuevo incumplimiento: resolución + indemnización igual al precio + pérdida de la garantía"],
         "**2 meses** · **1 mes** improrrogable · **25 %**",
         "Si el contratista **renuncia** antes del último plazo: indemnización de la **mitad del precio** y pierde la garantía.")),
U("3.3 Desviaciones y responsabilidad por defectos del proyecto (art. 315)",
  L(315, "más de un 20 por ciento", "cinco veces el precio pactado por el proyecto", "diez años"),
  fichab("Responsabilidad del redactor del proyecto de obra",
         "El contratista consultor (redactor del proyecto)",
         ["::Desviación del presupuesto de ejecución por errores u omisiones suyos:", "Más del 20 % y menos del 30 %: 30 % del precio", "Más del 30 % y menos del 40 %: 40 %", "Más del 40 %: 50 %"],
         "Pago en **un mes**; responsabilidad por daños: **50 %** de los daños, hasta **cinco veces** el precio, exigible durante **diez años** desde la recepción del proyecto",
         "El umbral es una desviación de **más del 20 %**, por **exceso o por defecto**. Si lo no previsto es del estudio geotécnico y encarece más del 10 % el precio inicial, el 20 % se sustituye por el **10 %** (art. 233.4).")),
resumen([
  "Servicios: cesión de la **propiedad intelectual** salvo pacto; **nunca** para contratar personal ni con consolidación.",
  "Precio por componentes, unidades, tanto alzado u honorarios; variación de unidades hasta el **10 %** sin ser modificación.",
  "Servicios a la ciudadanía: régimen jurídico previo, bienes **inembargables**, dependencias **diferenciadas**.",
  "Proyectos de obra: subsanación en **2 meses**; desviaciones de más del **20 %** se indemnizan (30, 40 o 50 %); responsabilidad por **diez años**."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test."),
]), 2)

# =============================================================================
# Cierre 1: preguntas oficiales
EX_P59 = examen("P", 59, {
  "a": "El art. 18.1 no atiende al orden de las prestaciones en el pliego: para servicios y suministros manda mirar el valor estimado.",
  "b": f"Literal del art. 18.1 a): {C(18, 'el objeto principal se determinará en función de cuál sea el mayor de los valores estimados de los respectivos servicios o suministros')}.",
  "c": "No se aplican siempre las normas de servicios: decide la prestación de mayor valor estimado, que puede ser el suministro.",
  "d": "Es lo contrario de la ley: el criterio es precisamente el valor estimado, no el número de unidades."},
  [("mayor de los valores estimados", "LCSP", "Artículo 18", "el objeto principal se determinará en función de cuál sea el mayor de los valores estimados de los respectivos servicios o suministros")])
EX_P60 = examen("P", 60, {
  "a": "Cambia quién paga: el art. 304.1 pone los gastos a cargo del contratista, no de la Administración.",
  "b": f"Literal del art. 304.1: {C(304, 'Salvo pacto en contrario, los gastos de la entrega y transporte de los bienes objeto del suministro al lugar convenido serán de cuenta del contratista')}.",
  "c": "El art. 304.1 no separa entrega y transporte: ambos gastos son del contratista.",
  "d": "Invierte y separa los gastos: ni la entrega es de la Administración ni el art. 304.1 distingue entre entrega y transporte."},
  [("entrega y transporte", "LCSP", "Artículo 304", "los gastos de la entrega y transporte de los bienes objeto del suministro"),
   ("de cuenta del contratista", "LCSP", "Artículo 304", "serán de cuenta del contratista")])
EX_X54 = examen("X", 54, {
  "a": f"Literal del art. 244.1: responderá {C(244, 'durante un plazo de quince años a contar desde la recepción')}.",
  "b": "Diez años no es el plazo del art. 244 (diez años es el de la responsabilidad del redactor del proyecto, art. 315.2).",
  "c": "Cinco años no aparece en el art. 244: el plazo es de quince años.",
  "d": f"Sí hay plazo: {C(244, 'Transcurrido el plazo de quince años')} sin daño, {C(244, 'quedará totalmente extinguida cualquier responsabilidad del contratista')}."},
  [("Quince años", "LCSP", "Artículo 244", "durante un plazo de quince años a contar desde la recepción")])
EX_X55 = examen("X", 55, {
  "a": "El plazo de tres meses sí puede ampliarse en este caso (valor estimado de más de doce millones y operaciones especialmente complejas): no es improrrogable.",
  "b": f"Art. 243.1: con valor estimado que {C(243, 'supere los doce millones de euros')} y liquidación y medición especialmente complejas, el plazo de tres meses {C(243, 'podrá ser ampliado, siempre que no supere en ningún caso los cinco meses')}.",
  "c": f"El plazo general no es de un mes: {C(243, 'Dentro del plazo de tres meses contados a partir de la recepción')}.",
  "d": "Cambia los dos datos: el plazo es de tres meses (no dos) y el tope de la ampliación, cinco meses (no tres)."},
  [("no supere en ningún caso los cinco meses", "LCSP", "Artículo 243", "podrá ser ampliado, siempre que no supere en ningún caso los cinco meses")])
EX_X57 = examen("X", 57, {
  "a": "«Estudio de compatibilidad» no es la denominación del art. 247.",
  "b": f"Literal del art. 247.1: {C(247, 'el órgano que corresponda de la Administración concedente acordará la realización de un estudio de viabilidad de las mismas')}.",
  "c": "«Estudio de eficacia económica» no existe en el art. 247 (lo que cabe es sustituirlo por un estudio de viabilidad económico-financiera, art. 247.6).",
  "d": "«Estudio de legalidad» no es la denominación del art. 247."},
  [("Estudio de viabilidad", "LCSP", "Artículo 247", "acordará la realización de un estudio de viabilidad de las mismas")])

T.ap("s20", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **cinco** preguntas de este tema: dos en promoción interna (contrato mixto y suministro) y tres en el extraordinario (obras y concesión de obras). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-P 2025, pregunta 59 · Contrato mixto de servicios y suministros (→ I.3.1)", EX_P59,
  "### GACE-P 2025, pregunta 60 · Gastos de entrega y transporte en el suministro (→ IV.2.5)", EX_P60,
  "### GACE-L 2025 extraordinario, pregunta 54 · Vicios ocultos en la obra (→ II.3.2)", EX_X54,
  "### GACE-L 2025 extraordinario, pregunta 55 · Certificación final de la obra (→ II.3.1)", EX_X55,
  "### GACE-L 2025 extraordinario, pregunta 57 · Estudio de viabilidad de la concesión de obras (→ III.1.2)", EX_X57,
  "### Cómo se pregunta",
  "!> Las cinco preguntas citan el **artículo** y piden el **dato literal**: un plazo (quince años, tres y cinco meses), quién paga (el contratista) o el criterio (el mayor valor estimado). Los distractores cambian ese dato.",
]))

T.ap("s21", "Cierre 2. Repaso en 10 minutos (por bloques)", """
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Tipos | Cinco tipos + mixto (arts. 12-18); riesgo operacional en las concesiones; mixto solo con prestaciones vinculadas (34.2) | Servicios + suministros: **mayor valor estimado**; programas a medida = **servicios** |
| II. Obras | Proyecto (elaboración, supervisión, aprobación, replanteo); comprobación del replanteo; certificaciones; recepción y garantía; vicios ocultos | Certificación final **3 meses** (5 si más de 12 millones y compleja); garantía mínima **1 año**; vicios ocultos **15 años** |
| III. Concesiones | Estudio de viabilidad; tarifas máximas; equilibrio económico; secuestro; rescate; reversión | **40 / 25 / 10 años**; secuestro máximo **3 años**; nunca reequilibrio por la demanda |
| IV. Suministro | Arrendamiento, fabricación, entrega, pago con otros bienes, garantía | Entrega y transporte: **contratista**; otros bienes hasta el **50 %** |
| V. Servicios | Propiedad intelectual, prohibición de contratar personal, precio, servicios a la ciudadanía, proyectos de obra | Desviación de más del **20 %**; responsabilidad del proyectista **10 años** |

?> **Trampas frecuentes:** «la certificación final se aprueba en tres meses **improrrogables**» (se puede ampliar hasta **cinco** si el valor supera **doce millones** y es compleja); «los gastos de transporte son de la **Administración**» (son del **contratista**, salvo pacto); «vicios ocultos: **diez** años» (son **quince**; los diez son del redactor del proyecto); «se restablece el equilibrio si la **demanda** es menor de la prevista» (nunca); «el anteproyecto es obligatorio» (lo obligatorio es el **estudio de viabilidad**).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
def Q(art, cat, enun, ops, expl, frag):
    T.q("LCSP", f"Artículo {art}", cat, enun, ops, expl, frag)

Q(13, "Tipos de contrato", "Según el artículo 13.2 de la Ley 9/2017, de Contratos del Sector Público, por «obra» se entenderá el resultado de un conjunto de trabajos de construcción o de ingeniería civil, destinado a cumplir por sí mismo una función económica o técnica, que tenga por objeto:",
  ["Un bien inmueble.", "Un bien mueble o inmueble.", "Un bien de dominio público.", "Una infraestructura de transporte."], "Art. 13.2 LCSP: «que tenga por objeto un bien inmueble».", "que tenga por objeto un bien inmueble")
Q(13, "Tipos de contrato", "Según el artículo 13.3 de la Ley 9/2017, los contratos de obras se referirán a:",
  ["Una obra completa.", "Una fase de obra técnicamente independiente.", "Una obra cuyo presupuesto no supere 500.000 euros.", "Una obra con proyecto aprobado por el Consejo de Ministros."], "Art. 13.3 LCSP: «Los contratos de obras se referirán a una obra completa».", "Los contratos de obras se referirán a una obra completa")
Q(14, "Tipos de contrato", "Según el artículo 14.1 de la Ley 9/2017, en el contrato de concesión de obras la contraprestación a favor del concesionario consiste:",
  ["O bien únicamente en el derecho a explotar la obra, o bien en dicho derecho acompañado del de percibir un precio.", "Únicamente en el precio que abone la Administración.", "En el precio que abonen los usuarios, garantizado en todo caso por la Administración.", "En una subvención de capital que cubra la totalidad de la inversión."],
  "Art. 14.1 LCSP.", "o bien únicamente en el derecho a explotar la obra")
Q(14, "Tipos de contrato", "Según el artículo 14.4 de la Ley 9/2017, el derecho de explotación de las obras deberá implicar la transferencia al concesionario de un riesgo operacional que abarque:",
  ["El riesgo de demanda o el de suministro, o ambos.", "Únicamente el riesgo de construcción.", "El riesgo financiero, pero no el de demanda.", "Ningún riesgo, si la Administración garantiza la recuperación de la inversión."],
  "Art. 14.4 LCSP: «abarcando el riesgo de demanda o el de suministro, o ambos».", "abarcando el riesgo de demanda o el de suministro, o ambos")
Q(15, "Tipos de contrato", "Según el artículo 15.1 de la Ley 9/2017, en el contrato de concesión de servicios encomiendan la gestión del servicio:",
  ["Uno o varios poderes adjudicadores.", "Exclusivamente las Administraciones territoriales.", "Solo la Administración General del Estado.", "Cualquier persona jurídica privada titular del servicio."],
  "Art. 15.1 LCSP: «uno o varios poderes adjudicadores encomiendan a título oneroso…».", "uno o varios poderes adjudicadores encomiendan a título oneroso")
Q(16, "Tipos de contrato", "Según el artículo 16.1 de la Ley 9/2017, son contratos de suministro los que tienen por objeto la adquisición, el arrendamiento financiero, o el arrendamiento, con o sin opción de compra, de:",
  ["Productos o bienes muebles.", "Bienes muebles o inmuebles.", "Propiedades incorporales o valores negociables.", "Bienes inmuebles."], "Art. 16.1 LCSP. Las propiedades incorporales y los valores negociables están excluidos (16.2).", "con o sin opción de compra, de productos o bienes muebles")
Q(16, "Tipos de contrato", "Según el artículo 16.3.b) de la Ley 9/2017, los contratos de adquisición de programas de ordenador desarrollados a medida se considerarán:",
  ["Contratos de servicios.", "Contratos de suministro.", "Contratos mixtos.", "Contratos de concesión de servicios."], "Art. 16.3 b) LCSP.", "programas de ordenador desarrollados a medida, que se considerarán contratos de servicios")
Q(17, "Tipos de contrato", "Según el artículo 17 de la Ley 9/2017, no podrán ser objeto de los contratos de servicios:",
  ["Los servicios que impliquen ejercicio de la autoridad inherente a los poderes públicos.", "Los servicios que se ejecuten de forma sucesiva y por precio unitario.", "Las prestaciones dirigidas a la obtención de un resultado distinto de una obra o suministro.", "Las prestaciones de hacer consistentes en el desarrollo de una actividad."],
  "Art. 17 LCSP. Las demás opciones son, literalmente, objeto posible del contrato de servicios.", "No podrán ser objeto de estos contratos los servicios que impliquen ejercicio de la autoridad inherente a los poderes públicos")
Q(18, "Contrato mixto", "Según el artículo 18.1.a) de la Ley 9/2017, cuando un contrato mixto comprenda prestaciones propias de dos o más contratos de obras, suministros o servicios, para determinar las normas de adjudicación se atenderá:",
  ["Al carácter de la prestación principal.", "A la prestación de mayor duración.", "A la prestación que figure en primer lugar en el pliego.", "En todo caso, a las normas del contrato de obras."], "Art. 18.1 a) LCSP (con la regla especial del mayor valor estimado para servicios y suministros).", "se atenderá al carácter de la prestación principal")
Q(18, "Contrato mixto", "Según el artículo 18.3 de la Ley 9/2017, cuando un elemento del contrato mixto sea una obra, deberá elaborarse un proyecto y tramitarse conforme a los artículos 231 y siguientes si la obra supera:",
  ["50.000 euros.", "40.000 euros.", "15.000 euros.", "500.000 euros."], "Art. 18.3 LCSP.", "supere los 50.000 euros, deberá elaborarse un proyecto")
T.q("LCSP", "Artículo 34", "Contrato mixto", "Según el artículo 34.2 de la Ley 9/2017, solo podrán fusionarse prestaciones correspondientes a diferentes contratos en un contrato mixto cuando esas prestaciones:",
  ["Se encuentren directamente vinculadas entre sí y mantengan relaciones de complementariedad que exijan su consideración como una unidad funcional.", "No superen en conjunto los umbrales de regulación armonizada.", "Lo autorice previamente el Consejo de Ministros.", "Correspondan al mismo tipo contractual."],
  "Art. 34.2 LCSP.", "se encuentren directamente vinculadas entre sí y mantengan relaciones de complementariedad")
Q(231, "Contrato de obras", "Según el artículo 231.1 de la Ley 9/2017, la adjudicación de un contrato de obras requerirá la previa elaboración, supervisión, aprobación y ______ del correspondiente proyecto:",
  ["Replanteo.", "Publicación.", "Fiscalización.", "Información pública."], "Art. 231.1 LCSP.", "elaboración, supervisión, aprobación y replanteo del correspondiente proyecto")
Q(232, "Contrato de obras", "Según el artículo 232.4 de la Ley 9/2017, las obras de reparación tendrán la calificación de gran reparación cuando:",
  ["Afecten fundamentalmente a la estructura resistente.", "Su presupuesto supere los 500.000 euros.", "El menoscabo se produzca en el tiempo por el natural uso del bien.", "Doten al inmueble de una nueva funcionalidad."], "Art. 232.4 LCSP. El menoscabo por el natural uso da obras de conservación (232.5); la nueva funcionalidad es la rehabilitación (232.7).", "Cuando afecten fundamentalmente a la estructura resistente tendrán la calificación de gran reparación")
Q(234, "Contrato de obras", "Según el artículo 234.1 de la Ley 9/2017, la contratación conjunta de la elaboración del proyecto y la ejecución de las obras correspondientes tendrá carácter:",
  ["Excepcional.", "Ordinario.", "Preferente cuando el presupuesto supere los 500.000 euros.", "Obligatorio en las obras hidráulicas."], "Art. 234.1 LCSP.", "tendrá carácter excepcional")
Q(235, "Contrato de obras", "Según el artículo 235 de la Ley 9/2017, el informe de las oficinas o unidades de supervisión de proyectos es preceptivo cuando el presupuesto base de licitación del contrato de obras sea:",
  ["Igual o superior a 500.000 euros, IVA excluido.", "Igual o superior a 300.000 euros, IVA incluido.", "Superior a 1.000.000 de euros, IVA excluido.", "Superior a 40.000 euros, IVA excluido."], "Art. 235 LCSP (por debajo, facultativo salvo estabilidad, seguridad o estanqueidad).", "sea igual o superior a 500.000 euros, IVA excluido")
Q(237, "Contrato de obras", "Según el artículo 237 de la Ley 9/2017, la comprobación del replanteo se hará dentro del plazo consignado en el contrato, que no podrá ser superior, salvo casos excepcionales justificados, a:",
  ["Un mes desde la fecha de su formalización.", "Un mes desde la fecha de su adjudicación.", "Dos meses desde la fecha de su formalización.", "Quince días desde la fecha de su adjudicación."], "Art. 237 LCSP.", "no podrá ser superior a un mes desde la fecha de su formalización")
Q(240, "Contrato de obras", "Según el artículo 240.1 de la Ley 9/2017, a los efectos del pago, la Administración expedirá certificaciones de la obra ejecutada:",
  ["Mensualmente, en los primeros diez días siguientes al mes al que correspondan.", "Mensualmente, en los primeros quince días siguientes al mes al que correspondan.", "Trimestralmente, en el mes siguiente al trimestre.", "Al terminar cada fase de la obra."], "Art. 240.1 LCSP.", "mensualmente, en los primeros diez días siguientes al mes al que correspondan")
Q(242, "Contrato de obras", "Según el artículo 242.1 de la Ley 9/2017, en caso de que la modificación del contrato de obras suponga supresión o reducción de unidades de obra, el contratista:",
  ["No tendrá derecho a reclamar indemnización alguna.", "Tendrá derecho a una indemnización del 3 por cien del precio de adjudicación.", "Tendrá derecho al 6 por cien del precio de las unidades suprimidas.", "Podrá oponerse a la modificación."], "Art. 242.1 LCSP.", "el contratista no tendrá derecho a reclamar indemnización alguna")
Q(242, "Contrato de obras", "Según el artículo 242.4 de la Ley 9/2017, no tendrá la consideración de modificación el exceso de mediciones, siempre que en global no represente un incremento del gasto superior al:",
  ["10 por ciento del precio del contrato inicial.", "20 por ciento del precio del contrato inicial.", "3 por ciento del presupuesto primitivo.", "15 por ciento del precio del contrato inicial."], "Art. 242.4 i LCSP (el 3 % es el límite de los precios nuevos; el 20 %, el de la continuación provisional).", "superior al 10 por ciento del precio del contrato inicial")
Q(243, "Contrato de obras", "Según el artículo 243.1 de la Ley 9/2017, el órgano de contratación deberá aprobar la certificación final de las obras ejecutadas dentro del plazo de:",
  ["Tres meses contados a partir de la recepción.", "Un mes contado a partir de la recepción.", "Tres meses contados a partir del fin del plazo de garantía.", "Seis meses contados a partir de la recepción."], "Art. 243.1 LCSP.", "Dentro del plazo de tres meses contados a partir de la recepción")
Q(243, "Contrato de obras", "Según el artículo 243.3 de la Ley 9/2017, el plazo de garantía de las obras se establecerá en el pliego de cláusulas administrativas particulares y no podrá ser inferior a:",
  ["Un año, salvo casos especiales.", "Dos años, salvo casos especiales.", "Seis meses.", "Cinco años."], "Art. 243.3 LCSP.", "no podrá ser inferior a un año salvo casos especiales")
Q(244, "Contrato de obras", "Según el artículo 244.2 de la Ley 9/2017, las acciones para exigir la responsabilidad por daños materiales dimanantes de vicios o defectos de la construcción prescribirán en el plazo de:",
  ["Dos años a contar desde que se produzcan o se manifiesten dichos daños.", "Quince años a contar desde la recepción.", "Cinco años a contar desde que se produzcan los daños.", "Un año a contar desde la expiración del plazo de garantía."], "Art. 244.2 LCSP (los quince años son el plazo de responsabilidad, 244.1).", "prescribirán en el plazo de dos años a contar desde que se produzcan o se manifiesten dichos daños")
Q(245, "Contrato de obras", "Según el artículo 245 de la Ley 9/2017, es causa de resolución del contrato de obras la suspensión de la iniciación de las obras por plazo superior a:",
  ["Cuatro meses.", "Seis meses.", "Ocho meses.", "Dos meses."], "Art. 245 b) LCSP (ocho meses es la suspensión de las obras ya iniciadas).", "La suspensión de la iniciación de las obras por plazo superior a cuatro meses")
Q(246, "Contrato de obras", "Según el artículo 246.2 de la Ley 9/2017, si se demorase injustificadamente la comprobación del replanteo, dando lugar a la resolución del contrato, el contratista solo tendrá derecho a una indemnización equivalente al:",
  ["2 por cien del precio de la adjudicación, IVA excluido.", "3 por cien del precio de la adjudicación, IVA excluido.", "6 por cien del precio de las obras dejadas de realizar.", "5 por cien del precio de la adjudicación, IVA incluido."], "Art. 246.2 LCSP.", "una indemnización equivalente al 2 por cien del precio de la adjudicación, IVA excluido")
T.q("LCSP", "Artículo 29", "Concesiones", "Según el artículo 29.6 de la Ley 9/2017, la duración de los contratos de concesión de obras, incluidas las posibles prórrogas, no podrá exceder de:",
  ["Cuarenta años.", "Veinticinco años.", "Cincuenta años.", "Diez años."], "Art. 29.6 a) LCSP.", "Cuarenta años para los contratos de concesión de obras")
T.q("LCSP", "Artículo 29", "Concesiones", "Según el artículo 29.6 de la Ley 9/2017, la duración de los contratos de concesión de servicios que comprendan la explotación de un servicio no relacionado con la prestación de servicios sanitarios no podrá exceder, incluidas las prórrogas, de:",
  ["Veinticinco años.", "Cuarenta años.", "Diez años.", "Quince años."], "Art. 29.6 b) LCSP (40 años si comprenden obras; 10 si son sanitarios).", "Veinticinco años en los contratos de concesión de servicios")
Q(247, "Concesiones", "Según el artículo 247.3 de la Ley 9/2017, la Administración concedente someterá el estudio de viabilidad a información pública por el plazo de:",
  ["Un mes, prorrogable por idéntico plazo.", "Veinte días hábiles, improrrogables.", "Dos meses, improrrogables.", "Quince días, prorrogables por otros quince."], "Art. 247.3 LCSP.", "por el plazo de un mes, prorrogable por idéntico plazo")
Q(247, "Concesiones", "Según el artículo 247.5 de la Ley 9/2017, presentado por un particular un estudio de viabilidad, el silencio de la Administración equivaldrá a:",
  ["La no aceptación del estudio.", "La aceptación del estudio.", "La decisión de tramitarlo en el plazo de seis meses.", "La caducidad del procedimiento."], "Art. 247.5 LCSP.", "El silencio de la Administración o de la entidad que corresponda equivaldrá a la no aceptación del estudio")
Q(263, "Concesiones", "Según el artículo 263.3 de la Ley 9/2017, la duración del secuestro o intervención de la concesión no podrá exceder:",
  ["De tres años, incluidas las posibles prórrogas.", "De dos años, sin posibilidad de prórroga.", "De cinco años, incluidas las posibles prórrogas.", "De un año, prorrogable por otro."], "Art. 263.3 LCSP.", "sin que pueda exceder, incluidas las posibles prórrogas, de tres años")
Q(264, "Concesiones", "Según el artículo 264.2 de la Ley 9/2017, durante la fase de construcción de la concesión de obras, el límite máximo de las penalidades no podrá exceder del:",
  ["10 por cien del presupuesto total de la obra.", "20 por cien del presupuesto total de la obra.", "20 por cien de los ingresos del año anterior.", "5 por cien del presupuesto total de la obra."], "Art. 264.2 LCSP (el 20 % de los ingresos del año anterior es el límite anual en la fase de explotación).", "no podrá exceder del 10 por cien del presupuesto total de la obra durante su fase de construcción")
Q(267, "Concesiones", "Según el artículo 267.2 de la Ley 9/2017, las tarifas que abonen los usuarios por la utilización de las obras en concesión tendrán el carácter de:",
  ["Máximas, y los concesionarios podrán aplicar tarifas inferiores.", "Mínimas, y los concesionarios podrán aplicar tarifas superiores.", "Fijas, sin que el concesionario pueda alterarlas.", "Orientativas, salvo que el pliego las declare obligatorias."], "Art. 267.2 LCSP.", "Las tarifas tendrán el carácter de máximas y los concesionarios podrán aplicar tarifas inferiores")
Q(270, "Concesiones", "Según el artículo 270.2 de la Ley 9/2017, no existirá en ningún caso derecho al restablecimiento del equilibrio económico financiero de la concesión de obras por:",
  ["Incumplimiento de las previsiones de la demanda recogidas en el estudio de la Administración o en el del concesionario.", "Una modificación de las obras acordada por la Administración.", "Causas de fuerza mayor que determinen de forma directa la ruptura sustancial de la economía del contrato.", "Actuaciones obligatorias de la Administración concedente que determinen de forma directa la ruptura sustancial de la economía del contrato."],
  "Art. 270.2 LCSP: las otras tres son, literalmente, los supuestos en que sí procede.", "no existirá derecho al restablecimiento del equilibrio económico financiero por incumplimiento de las previsiones de la demanda")
Q(279, "Concesiones", "Según el artículo 279.c) de la Ley 9/2017, el rescate de la concesión de obras requerirá además la acreditación de que:",
  ["La gestión directa es más eficaz y eficiente que la concesional.", "El concesionario ha incumplido gravemente sus obligaciones.", "La concesión ha superado la mitad de su plazo.", "El Consejo de Estado ha emitido dictamen favorable."], "Art. 279 c) LCSP: el rescate procede «no obstante la buena gestión de su titular».", "dicha gestión directa es más eficaz y eficiente que la concesional")
Q(284, "Concesiones", "Según el artículo 284.1 de la Ley 9/2017, la Administración podrá gestionar indirectamente, mediante contrato de concesión de servicios, los servicios de su titularidad o competencia:",
  ["Siempre que sean susceptibles de explotación económica por particulares.", "Siempre que su valor estimado no supere el umbral de regulación armonizada.", "Solo si se trata de servicios de competencia local.", "Aunque impliquen ejercicio de la autoridad inherente a los poderes públicos."], "Art. 284.1 LCSP.", "siempre que sean susceptibles de explotación económica por particulares")
Q(285, "Concesiones", "Según el artículo 285.2 de la Ley 9/2017, el estudio de viabilidad que precede a la concesión de servicios tendrá carácter vinculante:",
  ["En los supuestos en que concluya en la inviabilidad del proyecto.", "En todo caso.", "En los supuestos en que concluya en la viabilidad del proyecto.", "Solo si el contrato comprende la ejecución de obras."], "Art. 285.2 LCSP.", "tendrán carácter vinculante en los supuestos en que concluyan en la inviabilidad del proyecto")
Q(287, "Concesiones", "Según el artículo 287.3 de la Ley 9/2017, las concesiones de servicios únicamente podrán ser objeto de hipoteca:",
  ["Cuando conlleven la realización de obras o instalaciones fijas necesarias para la prestación del servicio, y en garantía de deudas relacionadas con la concesión.", "En cualquier caso, previa autorización del órgano de contratación.", "Cuando la concesión supere los cinco años de duración.", "Solo en garantía de deudas ajenas a la concesión."], "Art. 287.3 LCSP.", "únicamente podrán ser objeto de hipoteca en los casos en que conlleven la realización de obras o instalaciones fijas")
Q(296, "Concesiones", "Según el artículo 296 de la Ley 9/2017, en el contrato de concesión de servicios la subcontratación:",
  ["Solo podrá recaer sobre prestaciones accesorias.", "Está prohibida en todo caso.", "Puede alcanzar la totalidad de la prestación principal.", "Solo cabe en los servicios públicos de carácter económico."], "Art. 296 LCSP.", "la subcontratación solo podrá recaer sobre prestaciones accesorias")
Q(298, "Suministro", "Según el artículo 298 de la Ley 9/2017, en el contrato de arrendamiento, la obligación del mantenimiento del objeto durante el plazo de vigencia del contrato corresponde:",
  ["Al arrendador o empresario.", "A la Administración arrendataria.", "A ambas partes por mitad.", "A un tercero designado por el órgano de contratación."], "Art. 298 LCSP.", "el arrendador o empresario asumirá durante el plazo de vigencia del contrato la obligación del mantenimiento")
Q(300, "Suministro", "Según el artículo 300.2 de la Ley 9/2017, por las pérdidas, averías o perjuicios ocasionados en los bienes antes de su entrega a la Administración, el adjudicatario del suministro:",
  ["No tendrá derecho a indemnización, salvo que la Administración hubiere incurrido en mora al recibirlos.", "Tendrá derecho a indemnización en todo caso.", "Tendrá derecho a indemnización si se deben a fuerza mayor.", "Tendrá derecho a que la Administración asuma la mitad de las pérdidas."], "Art. 300.2 LCSP: «Cualquiera que sea el tipo de suministro».", "el adjudicatario no tendrá derecho a indemnización por causa de pérdidas, averías o perjuicios ocasionados en los bienes antes de su entrega a la Administración, salvo que esta hubiere incurrido en mora al recibirlos")
Q(302, "Suministro", "Según el artículo 302.1 de la Ley 9/2017, cuando el pago del precio de un suministro consista parte en dinero y parte en la entrega de otros bienes de la misma clase, el importe de estos no podrá superar:",
  ["El 50 por cien del precio total.", "El 25 por cien del precio total.", "El 20 por cien del precio total.", "El 10 por cien del precio total."], "Art. 302.1 LCSP.", "sin que, en ningún caso, el importe de estos pueda superar el 50 por cien del precio total")
Q(306, "Suministro", "Según el artículo 306.b) de la Ley 9/2017, es causa de resolución del contrato de suministro la suspensión del suministro acordada por la Administración, una vez iniciada su ejecución, por un plazo superior a:",
  ["Ocho meses, salvo que en el pliego se señale otro menor.", "Cuatro meses, salvo que en el pliego se señale otro menor.", "Seis meses, salvo que en el pliego se señale otro mayor.", "Un año, en todo caso."], "Art. 306 b) LCSP (cuatro meses es la suspensión de la iniciación, letra a).", "la suspensión del suministro por un plazo superior a ocho meses acordada por la Administración, salvo que en el pliego se señale otro menor")
Q(308, "Servicios", "Según el artículo 308.2 de la Ley 9/2017, la entidad contratante podrá instrumentar la contratación de personal a través del contrato de servicios:",
  ["En ningún caso, incluidos los contratos menores.", "Solo mediante contratos menores.", "Previa autorización del Ministerio de Hacienda.", "Cuando el contrato no supere un año de duración."], "Art. 308.2 LCSP.", "En ningún caso la entidad contratante podrá instrumentar la contratación de personal a través del contrato de servicios, incluidos los que por razón de la cuantía se tramiten como contratos menores")
Q(308, "Servicios", "Según el artículo 308.1 de la Ley 9/2017, salvo que se disponga otra cosa en los pliegos o en el documento contractual, los contratos de servicios que tengan por objeto el desarrollo y la puesta a disposición de productos protegidos por un derecho de propiedad intelectual o industrial:",
  ["Llevarán aparejada la cesión de este a la Administración contratante.", "Dejarán el derecho en todo caso en el contratista.", "Exigirán un contrato de suministro adicional para su cesión.", "Solo permitirán a la Administración un uso temporal del producto."], "Art. 308.1 LCSP.", "llevarán aparejada la cesión de este a la Administración contratante")
Q(314, "Servicios", "Según el artículo 314.1 de la Ley 9/2017, cuando el contrato de servicios consista en la elaboración íntegra de un proyecto de obra, el plazo que se otorgue al contratista para subsanar los defectos que le sean imputables no podrá exceder de:",
  ["Dos meses.", "Un mes.", "Tres meses.", "Quince días."], "Art. 314.1 LCSP (el segundo plazo es de un mes improrrogable, 314.4).", "otorgándole al efecto el correspondiente plazo que no podrá exceder de dos meses")
Q(315, "Servicios", "Según el artículo 315.2 de la Ley 9/2017, la indemnización derivada de la responsabilidad exigible al autor del proyecto por defectos del mismo será exigible dentro del término de:",
  ["Diez años, contados desde la recepción del proyecto por la Administración.", "Quince años, contados desde la recepción de la obra.", "Cinco años, contados desde la aprobación del proyecto.", "Dos años, contados desde que se manifiesten los daños."], "Art. 315.2 LCSP.", "será exigible dentro del término de diez años, contados desde la recepción del mismo por la Administración")

T.real("P", 59, "Contrato mixto"); T.real("P", 60, "Suministro"); T.real("X", 54, "Contrato de obras"); T.real("X", 55, "Contrato de obras"); T.real("X", 57, "Concesiones")

# Flashcards
for q_, a_, cat in [
  ("¿Qué cinco tipos de contrato define la LCSP (art. 12)?", "Obras, concesión de obras, concesión de servicios, suministro y servicios (además, el mixto: art. 18).", "Tipos de contrato"),
  ("¿Qué es «obra» según el art. 13.2?", "El resultado de un conjunto de trabajos de construcción o de ingeniería civil, destinado a cumplir por sí mismo una función económica o técnica, que tenga por objeto un bien inmueble.", "Tipos de contrato"),
  ("¿Qué distingue la concesión de obras del contrato de obras? (art. 14)", "La contraprestación: el derecho a explotar la obra (solo o con un precio), con transferencia al concesionario del riesgo operacional.", "Tipos de contrato"),
  ("¿Qué riesgo abarca el riesgo operacional? (art. 14.4)", "El riesgo de demanda o el de suministro, o ambos.", "Tipos de contrato"),
  ("Programas de ordenador a medida: ¿suministro o servicios? (art. 16.3 b)", "Servicios.", "Tipos de contrato"),
  ("Contrato mixto de servicios y suministros: ¿cómo se fija el objeto principal? (art. 18.1 a)", "Por el mayor de los valores estimados de los respectivos servicios o suministros.", "Contrato mixto"),
  ("Trámites del proyecto antes de adjudicar una obra (art. 231)", "Elaboración, supervisión, aprobación y replanteo.", "Contrato de obras"),
  ("¿Desde qué importe es preceptivo el informe de supervisión del proyecto? (art. 235)", "Presupuesto base de licitación igual o superior a 500.000 euros, IVA excluido (y, por debajo, si afecta a estabilidad, seguridad o estanqueidad).", "Contrato de obras"),
  ("Plazo de la comprobación del replanteo (art. 237)", "El del contrato, no superior a un mes desde la formalización, salvo casos excepcionales justificados.", "Contrato de obras"),
  ("Certificación final de la obra (art. 243.1)", "Tres meses desde la recepción; ampliable hasta cinco meses si el valor estimado supera doce millones y la liquidación y medición son especialmente complejas.", "Contrato de obras"),
  ("Plazo de garantía mínimo de las obras (art. 243.3)", "Un año, salvo casos especiales.", "Contrato de obras"),
  ("Responsabilidad por vicios ocultos (art. 244)", "Quince años desde la recepción; las acciones prescriben a los dos años desde que se producen o manifiestan los daños.", "Contrato de obras"),
  ("Indemnizaciones por resolución del contrato de obras (art. 246)", "2 % (demora en el replanteo), 3 % (antes de iniciar o suspensión de la iniciación más de 4 meses), 6 % de lo dejado de realizar (iniciadas o suspensión más de 8 meses).", "Contrato de obras"),
  ("Duración máxima de las concesiones (art. 29.6)", "40 años (obras, y servicios con obras); 25 años (servicios); 10 años (servicios sanitarios).", "Concesiones"),
  ("¿Qué estudio precede a la concesión de obras? (art. 247)", "El estudio de viabilidad (información pública de un mes, prorrogable por otro).", "Concesiones"),
  ("Duración máxima del secuestro o intervención (art. 263.3)", "Tres años, incluidas las prórrogas.", "Concesiones"),
  ("¿Cuándo nunca hay reequilibrio económico de la concesión? (arts. 270.2 y 290.4)", "Por incumplimiento de las previsiones de la demanda.", "Concesiones"),
  ("¿Qué es el rescate? (art. 279 c)", "La declaración unilateral por interés público que pone fin a la concesión, pese a la buena gestión, para gestionarla directamente; exige acreditar que la gestión directa es más eficaz y eficiente.", "Concesiones"),
  ("Gastos de entrega y transporte en el suministro (art. 304.1)", "De cuenta del contratista, salvo pacto en contrario.", "Suministro"),
  ("Pago del suministro con otros bienes (art. 302)", "Bienes de la misma clase; nunca más del 50 % del precio total.", "Suministro"),
  ("¿Puede usarse el contrato de servicios para contratar personal? (art. 308.2)", "En ningún caso, tampoco mediante contratos menores.", "Servicios"),
  ("Responsabilidad del redactor del proyecto (art. 315)", "Desviación de más del 20 %: indemnización del 30, 40 o 50 %; por daños, el 50 % hasta cinco veces el precio, durante diez años desde la recepción del proyecto.", "Servicios"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Obra", "Resultado de un conjunto de trabajos de construcción o de ingeniería civil, destinado a cumplir por sí mismo una función económica o técnica, que tiene por objeto un bien inmueble (art. 13.2).", "s1", "Tipos de contrato")
T.glos("Obra completa", "La susceptible de ser entregada al uso general o al servicio correspondiente; es a la que se refieren los contratos de obras (art. 13.3).", "s1", "Tipos de contrato")
T.glos("Riesgo operacional", "Riesgo de demanda o de suministro, o ambos, que asume el concesionario: no está garantizado que recupere las inversiones ni cubra los costes de la explotación (art. 14.4).", "s1", "Tipos de contrato")
T.glos("Contrato de fabricación", "Suministro de cosas elaboradas con características peculiares fijadas por la entidad contratante (art. 16.3 c); se le aplican normas del contrato de obras salvo en publicidad y adjudicación (art. 299).", "s2", "Tipos de contrato")
T.glos("Contrato mixto", "El que contiene prestaciones correspondientes a otro u otros de distinta clase (art. 18), solo admisible si están vinculadas y son complementarias (art. 34.2).", "s3", "Contrato mixto")
T.glos("Replanteo", "Comprobación de la realidad geométrica de la obra y de la disponibilidad de los terrenos, tras aprobar el proyecto (art. 236); la ejecución comienza con el acta de comprobación del replanteo (art. 237).", "s5", "Contrato de obras")
T.glos("Precio cerrado", "Modalidad del tanto alzado en que el precio ofertado no varía ni se abonan las modificaciones para corregir errores u omisiones del proyecto (art. 241.2).", "s6", "Contrato de obras")
T.glos("Plazo de garantía", "Periodo que empieza con la recepción de las obras, fijado en el pliego y no inferior a un año salvo casos especiales (art. 243).", "s7", "Contrato de obras")
T.glos("Estudio de viabilidad", "Estudio que acuerda la Administración concedente antes de decidir construir y explotar unas obras en concesión (art. 247); también precede a la concesión de servicios (art. 285.2).", "s8", "Concesiones")
T.glos("Secuestro o intervención", "Asunción temporal por el órgano de contratación de la explotación de la concesión, por cuenta y riesgo del concesionario, durante un máximo de tres años (art. 263).", "s10", "Concesiones")
T.glos("Tarifa", "Retribución por la utilización de las obras o servicios en concesión; prestación patrimonial de carácter público no tributario (arts. 267.1 y 289.2); en la concesión de obras, las que abonan los usuarios son máximas (art. 267.2).", "s10", "Concesiones")
T.glos("Rescate", "Declaración unilateral del órgano contratante, por interés público, que da por terminada la concesión pese a la buena gestión de su titular, para gestionarla directamente (art. 279 c).", "s11", "Concesiones")
T.glos("Reversión", "Vuelta del servicio a la Administración al finalizar el plazo de la concesión, con entrega de obras e instalaciones (art. 291).", "s13", "Concesiones")

# Cronología (fechas de los metadatos del BOE)
T.hito("2014", "Directivas 2014/23/UE y 2014/24/UE, de 26 de febrero de 2014 (citadas en el título de la Ley 9/2017)", "La Ley 9/2017 las transpone al ordenamiento español", "normativo", "s1")
T.hito("2017", "Ley 9/2017, de 8 de noviembre, de Contratos del Sector Público (BOE de 9-11-2017)", "Arts. 12 a 18: tipos de contrato; Libro II, Título II: reglas de cada tipo", "normativo", "s1")
T.hito("2018", "Corrección de errores de la Ley 9/2017 (BOE de 24-5-2018)", "Incluida en el texto consolidado", "normativo", "s0")
T.hito("2018", "Entrada en vigor de la Ley 9/2017 (9-3-2018)", "A los cuatro meses de su publicación (disposición final decimosexta)", "normativo", "s1")

T.publicar()
