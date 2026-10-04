# -*- coding: utf-8 -*-
"""Tema VI.5 (B6T05): El procedimiento administrativo de ejecución del presupuesto de gasto.
Órganos competentes. Fases del procedimiento y su relación con la actuación administrativa.
Especial referencia a la contratación administrativa y la gestión de subvenciones. Documentos
contables que intervienen en la ejecución de los gastos y de los pagos. Gestión de la tesorería
del Estado.
Método del I.2. Normas (textos consolidados del BOE): Ley 47/2003, General Presupuestaria
(arts. 21, 46, 69, 73 a 75, 90, 91, 106 a 110 y 112); Ley 9/2017, de Contratos del Sector Público
(arts. 116, 117, 198 y 323); Ley 38/2003, General de Subvenciones (arts. 9, 10 y 34); Orden de
1 de febrero de 1996 por la que se aprueba la Instrucción de operatoria contable a seguir en la
ejecución del gasto del Estado (OIOC); Orden de 1 de febrero de 1996 por la que se aprueban los
documentos contables a utilizar por la Administración General del Estado (ODOC); Orden
PRE/1576/2002, por la que se regula el procedimiento para el pago de obligaciones de la
Administración General del Estado (OPAGO)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO["ODOC"] = "Orden de 1-2-1996, documentos contables"
CORTO["OIOC"] = "Instrucción de operatoria contable, Orden de 1-2-1996"
CORTO["OPAGO"] = "Orden PRE/1576/2002, pago de obligaciones"


def g(art, frag):
    """Cita literal de la LGP."""
    return c("LGP", "Artículo " + str(art), frag)


ESQ = "*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*"

T = Tema("B6T05",
  "Seis preguntas: I. Qué reglas rigen la ejecución del gasto (LGP, arts. 21, 46 y 69) · II. Quién es competente (LGP, arts. 74 y 75; LCSP, art. 323; LGS, art. 10) · III. Qué fases tiene el procedimiento y cómo se relacionan con la actuación administrativa (LGP, art. 73; Instrucción de operatoria contable, reglas 14, 20 a 24 y 27) · IV. Cómo se ejecuta el gasto de los contratos y de las subvenciones (LCSP, arts. 116, 117 y 198; LGS, arts. 9 y 34; reglas 42, 77, 78, 82, 83, 85 y 86) · V. Qué documentos contables intervienen en los gastos y en los pagos (Orden de 1-2-1996 de documentos contables; regla 25; Orden PRE/1576/2002) · VI. Cómo se gestiona la tesorería del Estado (LGP, arts. 90, 91, 106 a 110 y 112; Orden PRE/1576/2002). Cada artículo: texto literal del BOE y ficha.",
  ["Fases del gasto", "Art. 73 LGP", "Aprobación", "Compromiso", "Reconocimiento de la obligación", "Ordenación del pago", "Pago material", "ADOK", "Art. 74 LGP", "12 millones", "Ordenador General de pagos", "Retención de crédito", "Documentos contables", "Documento OK", "Documento MC", "Documento de desglose", "Propuesta de pago", "Tesoro Público", "Unidad de caja", "Art. 91 LGP"])

# =============================================================================
T.ap("s0", "Mapa del tema: seis preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque VI, tema 5):
> El procedimiento administrativo de ejecución del presupuesto de gasto. Órganos competentes. Fases del procedimiento y su relación con la actuación administrativa. Especial referencia a la contratación administrativa y la gestión de subvenciones. Documentos contables que intervienen en la ejecución de los gastos y de los pagos. Gestión de la tesorería del Estado.

### El hilo conductor

El epígrafe se lee como **seis preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Ley 47/2003 (LGP) | Otras normas |
|---|---|---|---|
| **I** | ¿Qué reglas rigen la ejecución del presupuesto de gasto? | Arts. 21, 46 y 69 | — |
| **II** | ¿Quién es competente para gastar y para pagar? | Arts. 74 y 75 | LCSP, art. 323; LGS, art. 10 |
| **III** | ¿Qué fases tiene el procedimiento y cómo se relacionan con la actuación administrativa? | Art. 73 | Instrucción de operatoria contable (Orden de 1-2-1996), reglas 14, 20 a 24 y 27 |
| **IV** | ¿Cómo se ejecuta el gasto de los contratos y de las subvenciones? | — | LCSP, arts. 116, 117 y 198; LGS, arts. 9 y 34; Instrucción, reglas 42, 77, 78, 82, 83, 85 y 86 |
| **V** | ¿Qué documentos contables intervienen en la ejecución de los gastos y de los pagos? | — | Orden de 1-2-1996 de documentos contables, apartados segundo, tercero, quinto a séptimo y anexo I; Instrucción, regla 25; Orden PRE/1576/2002, apartados sexto y séptimo |
| **VI** | ¿Cómo se gestiona la tesorería del Estado? | Arts. 90, 91, 106 a 110 y 112 | Orden PRE/1576/2002, apartados octavo y noveno |

!> **La idea que une los seis bloques:** los créditos son **limitativos** y las obligaciones solo son exigibles si resultan de la ejecución del presupuesto (I). Gastan los **Ministros** y demás titulares de dotaciones diferenciadas; paga el **Ordenador General de pagos**, que es el **Director General del Tesoro y Política Financiera** (II). El gasto recorre cinco fases: **aprobación, compromiso, reconocimiento de la obligación, ordenación del pago y pago material** (III); en los contratos y en las subvenciones cada fase coincide con un acto concreto del expediente (IV). Cada fase se refleja en un **documento contable** (RC, A, D, AD, OK, ADOK…) (V) y el pago lo hace el **Tesoro Público**, que centraliza los fondos por el principio de **unidad de caja** (VI).

?> **Fronteras con otros temas.** El régimen sustantivo de los contratos es de los temas IV.5 y IV.6, y el de las subvenciones, del tema IV.7; los gastos plurianuales y las modificaciones de crédito, del tema VI.3; la fiscalización e intervención, del tema VI.4; los anticipos de caja fija y los pagos a justificar, del tema VI.6. Aquí solo se citan en lo que hace falta para la ejecución del gasto.

### Cómo está escrito

- Cada artículo o regla: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Los esquemas y cuadros **no son texto legal**: resumen los artículos citados.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué reglas rigen la ejecución del presupuesto de gasto? (LGP, arts. 21, 46 y 69)", donde(
  "Primera pregunta del tema. Antes de ver quién gasta y cómo, hay que saber **qué límites** tiene todo gasto público: solo es exigible lo que resulta de la ejecución del presupuesto y nunca puede superarse el crédito.",
  ["1 Exigibilidad de las obligaciones y carácter limitativo de los créditos (arts. 21 y 46)", "2 Principios de la gestión económico-financiera (art. 69)"]))

T.ap("s1", "I.1 Exigibilidad de las obligaciones y carácter limitativo de los créditos (LGP, arts. 21 y 46)", f"""
{unidad("1.1 Cuándo es exigible una obligación de la Hacienda Pública estatal (art. 21.1 y 2)",
  lit("LGP", "Artículo 21", ["cuando resulten de la ejecución de los presupuestos", "el pago no podrá efectuarse si el acreedor no ha cumplido o garantizado su correlativa obligación"], solo=[1, 2]),
  fichab("Fuentes de exigibilidad de las obligaciones del Estado",
         "La Hacienda Pública estatal (deudora) frente a sus acreedores",
         ["::Solo son exigibles si resultan de:", "La ejecución de los presupuestos", "Sentencia judicial firme", "Operaciones no presupuestarias legalmente autorizadas"],
         "—",
         f"Si la obligación tiene por causa prestaciones o servicios, {g(21, 'el pago no podrá efectuarse si el acreedor no ha cumplido o garantizado su correlativa obligación')}: es la base de la exigencia de acreditar la prestación antes de reconocer la obligación (→ III.1.3)."))}

{unidad("1.2 Los créditos para gastos son limitativos (art. 46)",
  lit("LGP", "Artículo 46", ["Los créditos para gastos son limitativos", "siendo nulos de pleno derecho"]),
  fichab("Límite cuantitativo de todo compromiso y obligación",
         "Todos los órganos que gestionan gastos",
         f"No pueden adquirirse compromisos ni obligaciones {g(46, 'por cuantía superior al importe de los créditos autorizados en los estados de gastos')}",
         "—",
         "La sanción es la **nulidad de pleno derecho** de los actos administrativos y de las disposiciones generales **con rango inferior a ley**; y además, responsabilidades (título VII)."))}
""", 2)

T.ap("s2", "I.2 Principios de la gestión económico-financiera (LGP, art. 69)", f"""
{unidad("2.1 Eficacia, eficiencia, objetividad y transparencia (art. 69)",
  lit("LGP", "Artículo 69", ["eficacia en la consecución de los objetivos fijados", "eficiencia en la asignación y utilización de recursos públicos", "objetividad y transparencia"]),
  fichab("Principios a los que se ajusta la gestión económico-financiera del sector público estatal",
         f"{g(69, 'Los sujetos que integran el sector público estatal')}; responden de los objetivos {g(69, 'Los titulares de los entes y órganos administrativos')}",
         ["Eficacia en la consecución de los objetivos", "Eficiencia en la asignación y utilización de los recursos", "En un marco de objetividad y transparencia", "Cooperación y coordinación con otras Administraciones (69.3)"],
         "—",
         "**Eficacia** se refiere a los **objetivos**; **eficiencia**, a los **recursos**. La programación se hace «de acuerdo con las políticas de gasto establecidas por el **Gobierno**»."))}

{resumen([
  "Las obligaciones de la Hacienda estatal solo son exigibles si resultan de la **ejecución de los presupuestos**, de **sentencia judicial firme** o de **operaciones no presupuestarias** autorizadas (21.1).",
  "No se paga si el acreedor no ha **cumplido o garantizado** su obligación (21.2).",
  "Los créditos son **limitativos**: lo que los supere es **nulo de pleno derecho** (46).",
  "Principios: **eficacia** (objetivos), **eficiencia** (recursos), **objetividad y transparencia** (69)."],
  "Siguiente: II. ¿Quién es competente para gastar y para pagar?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Quién es competente para gastar y para pagar? (LGP, arts. 74 y 75; LCSP, art. 323; LGS, art. 10)", donde(
  "Segunda pregunta. La LGP separa a quien **gasta** (aprueba, compromete y reconoce: los Ministros y los demás titulares de dotaciones diferenciadas) de quien **paga** (el Ordenador General de pagos). La LCSP y la LGS designan a los órganos de contratación y de concesión de subvenciones.",
  ["1 Competencias en la gestión de gastos (LGP, art. 74)", "2 La ordenación de pagos (LGP, art. 75)", "3 Órganos de contratación y de concesión de subvenciones (LCSP, art. 323; LGS, art. 10)"]))

T.ap("s3", "II.1 Competencias en materia de gestión de gastos (LGP, art. 74)", f"""
{unidad("1.1 Ministros, organismos autónomos y Seguridad Social (art. 74.1 a 4)",
  lit("LGP", "Artículo 74", ["aprobar y comprometer los gastos propios de sus presupuestos", "interesar del Ordenador general de pagos del Estado la realización de los correspondientes pagos", "a los Secretarios de Estado y Subsecretario del departamento", "así como el reconocimiento y el pago de las obligaciones", "podrán desconcentrarse mediante real decreto acordado en Consejo de Ministros"], solo=[1, 2, 3, 4, 5]),
  fichab("Quién aprueba, compromete y reconoce las obligaciones",
         [f"::Según el ámbito:", f"Estado: {g(74, 'los Ministros y a los titulares de los demás órganos del Estado con dotaciones diferenciadas')}", "Organismos autónomos y entidades con presupuesto limitativo: sus presidentes o directores", "Entidades gestoras y servicios comunes de la Seguridad Social: sus directores"],
         ["Aprueban y comprometen el gasto y reconocen la obligación", "En el Estado y en la Seguridad Social, **interesan** el pago del Ordenador general de pagos", "En los organismos autónomos, además, **pagan** (74.2)"],
         f"Los Ministros fijan los límites por debajo de los cuales la competencia es de los Secretarios de Estado y del Subsecretario; desconcentración {g(74, 'mediante real decreto acordado en Consejo de Ministros')} o delegación",
         "Salvedad: los casos **reservados por la Ley al Consejo de Ministros**. El Ministro no paga: «interesa» el pago del **Ordenador general de pagos** (→ II.2.1)."))}

{unidad("1.2 Convenios y contratos-programa de más de doce millones (art. 74.5)",
  lit("LGP", "Artículo 74", ["autorización del Consejo de Ministros cuando el importe del gasto que de aquellos se derive sea superior a doce millones de euros", "La autorización del Consejo de Ministros implicará la aprobación del gasto que se derive del convenio o contrato-programa"], solo=[6, 7, 8, 9, 10, 11]),
  fichab("Autorización del Consejo de Ministros para convenios y contratos-programa de gasto elevado",
         "El **Consejo de Ministros** autoriza; los órganos competentes para suscribir el convenio lo solicitan",
         ["Autorización previa si el gasto supera **12 millones de euros**", "También para las modificaciones que alteren el importe global, el destino o los calendarios, y para la resolución", "Antes de suscribir: expediente de gasto con el **importe máximo** de las obligaciones (y su distribución por anualidades si es plurianual)"],
         f"Más de **doce millones de euros**; el expediente de gasto se tramita {g(74, 'antes de la elevación del asunto a dicho órgano')}",
         f"{g(74, 'La autorización del Consejo de Ministros implicará la aprobación del gasto')}: no hay una aprobación posterior del Ministro. No se aplica a los convenios del art. 86 (créditos gestionados por las CC. AA.). Cayó en 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s4", "II.2 La ordenación de pagos (LGP, art. 75)", f"""
{unidad("2.1 El Ordenador General de pagos del Estado (art. 75)",
  lit("LGP", "Artículo 75", ["competen al Director General del Tesoro y Política Financiera las funciones de Ordenador General de pagos del Estado", "competen al Director General de la Tesorería General de la Seguridad Social", "Las órdenes de pago se expedirán a favor del acreedor"]),
  fichab("La competencia para ordenar los pagos",
         ["Estado: el **Director General del Tesoro y Política Financiera**, bajo la superior autoridad del Ministro de Economía", "Seguridad Social: el **Director General de la Tesorería General de la Seguridad Social**"],
         [f"Las órdenes de pago se expiden {g(75, 'a favor del acreedor que figura en la correspondiente propuesta de pago')}", "Por Orden del Ministro de Economía, pueden expedirse a favor de Habilitaciones, Cajas pagadoras, Depositarías, entidades colaboradoras y otros agentes mediadores, que actúan como intermediarios"],
         "—",
         "El Ordenador General es un **Director General** (del Tesoro y Política Financiera), no el Ministro ni un Secretario de Estado o General. Cayó en 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s5", "II.3 Órganos de contratación y de concesión de subvenciones (LCSP, art. 323; LGS, art. 10)", f"""
{unidad("3.1 Órganos de contratación de la Administración General del Estado (LCSP, art. 323.1)",
  lit("LCSP", "Artículo 323", ["Los Ministros y los Secretarios de Estado son los órganos de contratación de la Administración General del Estado"], solo=[1, 2]),
  fichab("Quién contrata en nombre de la Administración General del Estado",
         "Los **Ministros** y los **Secretarios de Estado**",
         f"Celebran los contratos {c('LCSP', 'Artículo 323', 'en el ámbito de su competencia')}; si un suministro o servicio afecta a varios órganos de contratación de un departamento, el Ministro (salvo que se atribuya a la Junta de Contratación)",
         "—",
         "El régimen de la contratación es de los temas IV.5 y IV.6; aquí interesa que el órgano de contratación es también el que **aprueba el gasto** al aprobar el expediente (→ IV.1.2)."))}

{unidad("3.2 Órganos competentes para conceder subvenciones (LGS, art. 10.1 y 2)",
  lit("LGS", "Artículo 10", ["previa consignación presupuestaria para este fin", "de cuantía superior a 12 millones de euros", "La referida autorización no implicará la aprobación del gasto"], solo=[1, 2, 3, 5, 6]),
  fichab("Quién concede las subvenciones en la Administración General del Estado",
         ["Los **Ministros** y los **Secretarios de Estado**", "Los presidentes o directores de los organismos y entidades públicas vinculados o dependientes"],
         ["Previa consignación presupuestaria", "Más de 12 millones: autorización previa del **Consejo de Ministros** (o de la Comisión Delegada para Asuntos Económicos si lo prevé la normativa reguladora)", "En concurrencia competitiva, la autorización se obtiene antes de aprobar la convocatoria"],
         "Más de **12 millones de euros**",
         f"Contraste con los convenios del art. 74.5 LGP (→ II.1.2): en subvenciones, la autorización del Consejo de Ministros {c('LGS', 'Artículo 10', 'no implicará la aprobación del gasto')}, que corresponde al órgano competente."))}

{resumen([
  "Aprueban y comprometen el gasto y reconocen la obligación los **Ministros** y demás titulares de dotaciones diferenciadas; fijan los límites para Secretarios de Estado y Subsecretario (74.1).",
  "Convenios y contratos-programa de más de **12 millones**: autoriza el **Consejo de Ministros**, y su autorización **implica la aprobación del gasto** (74.5).",
  "Ordenador General de pagos del Estado: el **Director General del Tesoro y Política Financiera** (75.1).",
  "Contratan los **Ministros y Secretarios de Estado** (LCSP 323.1); conceden subvenciones los **Ministros y Secretarios de Estado**; más de 12 millones, autorización del Consejo de Ministros, que **no** implica la aprobación del gasto (LGS 10)."],
  "Siguiente: III. ¿Qué fases tiene el procedimiento y cómo se relacionan con la actuación administrativa?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Qué fases tiene el procedimiento y cómo se relacionan con la actuación administrativa? (LGP, art. 73; Instrucción de operatoria contable, reglas 14, 20 a 24 y 27)", donde(
  "Tercera pregunta, el núcleo del tema. La LGP define las **cinco fases** de la gestión del gasto; la Instrucción de operatoria contable (Orden de 1 de febrero de 1996) las describe como **actos administrativos** y dice qué documento contable expide el servicio gestor en cada una.",
  ["1 Las fases en la LGP (art. 73)", "2 Las fases como actos administrativos (Instrucción de operatoria contable)", "3 Cuadro de las fases"]))

T.ap("s6", "III.1 Las fases del procedimiento de gestión de los gastos (LGP, art. 73)", f"""
{unidad("1.1 Las cinco fases (art. 73.1)",
  lit("LGP", "Artículo 73", ["Aprobación del gasto", "Compromiso de gasto", "Reconocimiento de la obligación", "Ordenación del pago", "Pago material"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Fases de la gestión del Presupuesto de gastos",
         "Estado, organismos autónomos, entidades del sector público estatal con presupuesto **limitativo** y entidades gestoras y servicios comunes de la Seguridad Social",
         ["a) Aprobación del gasto", "b) Compromiso de gasto", "c) Reconocimiento de la obligación", "d) Ordenación del pago", "e) Pago material"],
         "—",
         "Son **cinco** y en este orden. La LGP dice «**aprobación**»; la Instrucción de operatoria contable la llama «**autorización**» (→ III.2.3) y de ahí la letra A de los documentos."))}

{unidad("1.2 Aprobación y compromiso (art. 73.2 y 3)",
  lit("LGP", "Artículo 73", ["se autoriza la realización de un gasto determinado por una cuantía cierta o aproximada", "sin que implique relaciones con terceros", "la realización de gastos previamente aprobados, por un importe determinado o determinable", "acto con relevancia jurídica para con terceros"], solo=[7, 8, 9, 10]),
  fichab("Las dos primeras fases: reservar el crédito y obligarse frente a terceros",
         "El órgano competente para gastar (→ II.1.1)",
         [f"Aprobación: {g(73, 'reservando a tal fin la totalidad o parte de un crédito presupuestario')}; inicia el procedimiento", f"Compromiso: {g(73, 'tras el cumplimiento de los trámites legalmente establecidos')}; vincula a la Hacienda {g(73, 'a la realización del gasto a que se refiera en la cuantía y condiciones establecidas')}"],
         "Aprobación: cuantía **cierta o aproximada**. Compromiso: importe **determinado o determinable**",
         "La aprobación es **interna** (sin relaciones con terceros); el compromiso es el primer acto **con relevancia jurídica para con terceros**. Los distractores intercambian las dos definiciones (→ Cierre 1)."))}

{unidad("1.3 Reconocimiento de la obligación (art. 73.4)",
  lit("LGP", "Artículo 73", ["se declara la existencia de un crédito exigible contra la Hacienda Pública estatal", "comporta la propuesta de pago correspondiente", "previa acreditación documental ante el órgano competente de la realización de la prestación o el derecho del acreedor"], solo=[11, 12]),
  fichab("La tercera fase: declarar que la Hacienda debe",
         "El órgano competente para gastar (→ II.1.1)",
         [f"Declara {g(73, 'la existencia de un crédito exigible contra la Hacienda Pública estatal o contra la Seguridad Social')}", "Deriva de un gasto **aprobado y comprometido**", "Lleva consigo la **propuesta de pago**"],
         "Previa **acreditación documental** de la prestación o del derecho del acreedor",
         "Definición literal que cayó en 2025 (→ Cierre 1). El «crédito exigible» es el **derecho del acreedor** contra la Hacienda, no un crédito presupuestario."))}

{unidad("1.4 Documentos, extinción de las obligaciones y acumulación de fases (art. 73.5 a 7)",
  lit("LGP", "Artículo 73", ["a propuesta de la Intervención General de la Administración del Estado", "se extinguen por el pago, la compensación, la prescripción o cualquier otro medio", "se acumularán en un solo acto las fases de ejecución precisas"], solo=[13, 14, 15]),
  fichab("Reglas comunes de las fases",
         "La persona titular del Ministerio de Hacienda, a propuesta de la **IGAE**, determina los documentos y requisitos de cada fase",
         ["Las obligaciones se extinguen por el pago, la compensación, la prescripción u otro medio legal (73.6)", f"{g(73, 'Cuando la naturaleza de la operación o gasto así lo determinen')}, se acumulan fases en un solo acto (73.7)"],
         "—",
         "La acumulación de fases explica los documentos **mixtos** AD y ADOK (→ III.2.6)."))}
""", 2)

T.ap("s7", "III.2 Las fases como actos administrativos (Instrucción de operatoria contable, reglas 14, 20 a 24 y 27)", f"""
La Instrucción de operatoria contable (anexo I de la Orden de 1 de febrero de 1996) es la norma que une cada **acto administrativo** del expediente de gasto con su **documento contable**.

{unidad("2.1 Antes de la primera fase: retención de crédito (regla 14.1)",
  lit("OIOC", "regla14", ["Al inicio de la tramitación de un expediente de gasto", "un documento RC, de retención de créditos para gastar", "certificado de existencia de crédito"], solo=[1, 2, 3]),
  fichab("La retención de crédito y el certificado de existencia de crédito",
         "El **Servicio Gestor** solicita; la **oficina de contabilidad** registra y expide el certificado",
         "Documento **RC**: el crédito queda retenido para el gasto y el certificado se incorpora al expediente",
         "Al **inicio** de la tramitación del expediente",
         "La retención **no es una fase** del gasto: es un cambio de situación del crédito previo a la autorización. En los casos del capítulo III de la Instrucción en que no es obligatoria, el gestor valora si la pide."))}

{unidad("2.2 Las fases en la Instrucción (regla 20)",
  lit("OIOC", "regla20", ["Autorización del gasto", "Compromiso del gasto", "Reconocimiento de la obligación", "la Orden que regule los procedimientos para el pago de obligaciones"]),
  fichab("Delimitación de las fases de ejecución",
         "—",
         ["La Instrucción regula tres fases: autorización, compromiso y reconocimiento de la obligación", "La ordenación y ejecución de los pagos se rige por la Orden que regule el pago de obligaciones (la que regula ese procedimiento es la Orden PRE/1576/2002 → VI.3)"],
         "—",
         "La LGP enumera **cinco** fases (→ III.1.1); la Instrucción regula las **tres** primeras y remite el pago a otra Orden."))}

{unidad("2.3 Autorización del gasto: documento A (regla 21)",
  lit("OIOC", "regla21", ["aprueba su realización, determinando su cuantía de forma cierta, o bien de la forma más aproximada posible", "un documento A, de autorización de gastos de ejercicio corriente"], solo=[1, 2]),
  fichab("La autorización como acto administrativo",
         f"{c('OIOC', 'regla21', 'la autoridad competente para gestionar un gasto con cargo a un crédito presupuestario')}; el **Servicio gestor** formula el documento",
         "Se refleja en un **expediente de gasto**; aprobado este, documento **A** de ejercicio corriente y, en su caso, A de ejercicios posteriores",
         "Cuantía cierta o la más aproximada posible",
         "Si hubo retención, el documento A indica que se autoriza **sobre crédito retenido** y cita el RC (regla 27)."))}

{unidad("2.4 Compromiso del gasto: documento D (regla 22)",
  lit("OIOC", "regla22", ["El compromiso de gastos o disposición", "acuerda o concierta con un tercero", "un documento D, de compromiso de gastos de ejercicio corriente"], solo=[1, 2]),
  fichab("El compromiso (o disposición) como acto administrativo",
         "La autoridad competente; el Servicio gestor formula el documento",
         f"Acuerda o concierta con un tercero {c('OIOC', 'regla22', 'la realización de obras, prestaciones de servicios, transferencias, subvenciones, etcétera')} previamente autorizados",
         "—",
         "Compromiso = **disposición** (de ahí la D). Es el acto que mira **a un tercero**."))}

{unidad("2.5 Reconocimiento de la obligación: documento OK (regla 23)",
  lit("OIOC", "regla23", ["según el principio del «servicio hecho»", "llevará implícita la correspondiente propuesta de pago", "el Servicio gestor competente expedirá un documento OK"], solo=[1, 2, 3, 4]),
  fichab("El reconocimiento de la obligación como acto administrativo",
         "La autoridad competente acepta la deuda; el **Servicio gestor** expide el documento",
         ["Obligaciones recíprocas: por el principio del **servicio hecho**", "Obligaciones no recíprocas: por el nacimiento del derecho del tercero en virtud de la Ley o de un acto administrativo", "Lleva implícita la **propuesta de pago** al Ordenador general de Pagos"],
         "Previa acreditación documental de la prestación o del derecho del acreedor",
         "Acordado el reconocimiento, se expide un documento **OK** (O = obligación; K = propuesta de pago). Literal que cayó en 2025 (→ Cierre 1). Solo en la **Deuda Pública** cabe un documento **O** sin propuesta de pago, con un **K** posterior (regla 23.4)."))}

{unidad("2.6 Fases mixtas: AD y ADOK (regla 24)",
  lit("OIOC", "regla24", ["produce los mismos efectos que si dichas fases se acordaran en actos administrativos separados", "se expedirá un documento mixto AD", "se expedirá documento mixto ADOK"]),
  fichab("Acumulación de fases en un solo acto",
         "El órgano competente para todas las fases acumuladas",
         ["Autorización + compromiso en un acto → documento **AD**", "Autorización + compromiso + reconocimiento → documento **ADOK**"],
         "—",
         "Acumular fases **no cambia sus efectos**: es como si se acordaran por separado. Desarrolla el art. 73.7 LGP (→ III.1.4)."))}

{unidad("2.7 El enlace entre operaciones (regla 27)",
  lit("OIOC", "regla27", ["Operaciones de inicio", "Operaciones de continuación", "el reconocimiento de las obligaciones al número del compromiso"], solo=[2, 3, 4, 5, 6]),
  fichab("Cómo se encadenan los documentos de un mismo gasto",
         "El Servicio gestor, al expedir los documentos",
         ["Inicio: RC o autorizaciones sobre crédito disponible (A, AD y ADOK)", "Continuación: fases sucesivas o complementos; citan el número de registro contable de la operación a la que suceden", "Autorización sobre crédito retenido → número del RC; compromiso → número de la autorización; reconocimiento → número del compromiso"],
         "—",
         "**ADOK** sobre crédito disponible es una operación **de inicio**: el gasto empieza y se reconoce en un solo acto."))}
""", 2)

T.ap("s8", "III.3 Cuadro de las fases: acto, contenido y documento (esquema)", f"""
{ESQ}

| Fase (LGP, art. 73) | Nombre en la Instrucción | Qué es | Frente a terceros | Documento |
|---|---|---|---|---|
| (previa) | Retención de crédito | Certificado de existencia de crédito al inicio del expediente | No | RC |
| a) Aprobación | Autorización | Autoriza un gasto por cuantía **cierta o aproximada** y reserva el crédito | **No** | A |
| b) Compromiso | Compromiso o disposición | Acuerda la realización de gastos aprobados, por importe **determinado o determinable** | **Sí** | D |
| a) + b) | Fase mixta | Autorización y compromiso en un acto | Sí | AD |
| c) Reconocimiento | Reconocimiento de la obligación | Declara un **crédito exigible** contra la Hacienda; lleva la propuesta de pago | Sí | OK |
| a) + b) + c) | Fase mixta | Las tres en un acto | Sí | ADOK |
| d) Ordenación del pago | (Orden PRE/1576/2002) | La ordena el **Director General del Tesoro y Política Financiera** | Sí | — (→ VI.3) |
| e) Pago material | (Orden PRE/1576/2002) | Por **transferencia** desde la cuenta del Tesoro | Sí | — (→ VI.3) |

{resumen([
  "Cinco fases: **aprobación, compromiso, reconocimiento de la obligación, ordenación del pago y pago material** (73.1).",
  "Aprobación: cuantía **cierta o aproximada**, sin relación con terceros. Compromiso: importe **determinado o determinable**, con relevancia jurídica **para con terceros** (73.2 y 3).",
  "Reconocimiento: declara la existencia de un **crédito exigible** contra la Hacienda, previa **acreditación documental**, y comporta la **propuesta de pago** (73.4).",
  "La Instrucción: RC al inicio; **A**, **D**, **OK**; mixtos **AD** y **ADOK** con los mismos efectos que las fases separadas (reglas 14 y 21 a 24)."],
  "Siguiente: IV. ¿Cómo se ejecuta el gasto de los contratos y de las subvenciones?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Cómo se ejecuta el gasto de los contratos y de las subvenciones? (LCSP, arts. 116, 117 y 198; LGS, arts. 9 y 34; Instrucción, reglas 42, 77, 78, 82, 83, 85 y 86)", donde(
  "Cuarta pregunta: la «especial referencia» del epígrafe. En los contratos y en las subvenciones cada fase del gasto coincide con un acto del expediente: la **aprobación del expediente** de contratación o de la **convocatoria**, la **adjudicación** o la **concesión**, y la **acreditación** de la prestación o de la actividad subvencionada.",
  ["1 Contratación: el gasto en la LCSP (arts. 116, 117 y 198)", "2 Contratación: los documentos contables (reglas 42, 77 y 78)", "3 Subvenciones: el gasto en la LGS (arts. 9.4 y 34)", "4 Subvenciones: los documentos contables (reglas 82, 83, 85 y 86)", "5 Cuadro: fases y actos en contratos y subvenciones"]))

T.ap("s9", "IV.1 Contratación: el gasto en la LCSP (arts. 116, 117 y 198)", f"""
{unidad("1.1 Certificado de existencia de crédito y fiscalización previa en el expediente (art. 116.3)",
  lit("LCSP", "Artículo 116", ["el certificado de existencia de crédito", "la fiscalización previa de la intervención"], solo=[4, 5]),
  fichab("Documentos presupuestarios del expediente de contratación",
         "El órgano de contratación incorpora los documentos al expediente",
         ["Pliegos de cláusulas administrativas particulares y de prescripciones técnicas", "Certificado de existencia de crédito (en las entidades con presupuesto estimativo, documento equivalente de financiación)", "Fiscalización previa de la intervención, en su caso, en los términos de la LGP"],
         "—",
         "El certificado de existencia de crédito es el que se obtiene con el documento **RC** (→ III.2.1 y → IV.2.2). La fiscalización previa es del tema VI.4."))}

{unidad("1.2 La aprobación del expediente implica la aprobación del gasto (art. 117)",
  lit("LCSP", "Artículo 117", ["Dicha resolución implicará también la aprobación del gasto", "podrán comprometerse créditos con las limitaciones que se determinen en las normas presupuestarias"]),
  fichab("Momento de la aprobación del gasto en los contratos",
         "El **órgano de contratación** (→ II.3.1)",
         ["Resolución motivada que aprueba el expediente y abre el procedimiento de adjudicación", "Esa resolución implica también la **aprobación del gasto**", "Salvo: presupuesto no establecido previamente, o normas de desconcentración o delegación en contrario → aprobación del órgano competente"],
         "Puede ultimarse el expediente (incluso adjudicar y formalizar) aunque la ejecución empiece en el **ejercicio siguiente** (117.2: tramitación anticipada → IV.2.1)",
         "Aprobación del expediente = **fase A**. La resolución se publica en el **perfil de contratante**."))}

{unidad("1.3 Pago del precio en treinta días (art. 198.4)",
  lit("LCSP", "Artículo 198", ["dentro de los treinta días siguientes a la fecha de aprobación de las certificaciones de obra", "dentro de los treinta días siguientes a la entrega efectiva de los bienes o prestación del servicio"], solo=[6, 7]),
  fichab("Plazos de aprobación de la conformidad y de pago",
         "La Administración contratante",
         ["Aprobar las certificaciones o documentos de conformidad: **30 días** desde la entrega o prestación", "Abonar el precio: **30 días** desde la aprobación de las certificaciones o documentos de conformidad", "Si se demora: intereses de demora e indemnización por costes de cobro (Ley 3/2004)"],
         "30 + 30 días; el contratista debe presentar la factura en **30 días** desde la entrega o prestación",
         "La aprobación de la conformidad abre el **reconocimiento de la obligación** (fase O); el pago, la **ordenación y el pago material**."))}
""", 2)

T.ap("s10", "IV.2 Contratación: los documentos contables (Instrucción, reglas 42, 77 y 78)", f"""
{unidad("2.1 Tramitación anticipada de expedientes de contratación (regla 42.1 a 3)",
  lit("OIOC", "regla42", ["condición suspensiva de existencia de crédito adecuado y suficiente", "detallando el importe que del gasto en cuestión corresponde a cada uno de los ejercicios posteriores afectados"], solo=[1, 2, 3, 4, 5, 7]),
  fichab("Gastos cuya ejecución empieza en el ejercicio siguiente",
         "El Servicio gestor expide el RC de tramitación anticipada; el certificado de cumplimiento de límites se obtiene del Sistema de Información Contable",
         ["Pliego: adjudicación y formalización sujetas a la **condición suspensiva** de existencia de crédito", "Certificado de cumplimiento de los límites del art. 47 LGP (documento RC de tramitación anticipada)", "Después: documentos A, D o AD «de tramitación anticipada»"],
         "Se tramita en el ejercicio **anterior** al del comienzo de la ejecución",
         "La regla 42.1 cita el art. 110.2 del texto refundido de 2011; su texto coincide con el del art. 117.2 LCSP (→ IV.1.2). Los límites del art. 47 LGP son del tema VI.3."))}

{unidad("2.2 Compromisos de gasto derivados de los contratos: RC, A y D (regla 77.1 y 2)",
  lit("OIOC", "regla77", ["Al inicio de un expediente de contratación, el Servicio gestor expedirá un documento RC", "una vez que se apruebe el expediente de gasto, el Servicio gestor formulará un documento A", "Cuando se formalicen los contratos, el Servicio gestor competente expedirá el respectivo documento D"], solo=[1, 3, 4]),
  fichab("Documentos de las fases A y D en los contratos",
         "El Servicio gestor",
         ["Inicio del expediente → **RC** (certificado de existencia de crédito)", "Aprobación del expediente de gasto → **A**", "Formalización del contrato → **D**"],
         "—",
         "En los contratos el **compromiso** (D) se documenta con la **formalización** del contrato; la **autorización** (A), con la aprobación del expediente."))}

{unidad("2.3 Reconocimiento de la obligación en los contratos: OK (regla 78.1)",
  lit("OIOC", "regla78", ["se deberá justificar por el contratista el cumplimiento de la prestación contractual", "el Servicio gestor expedirá un documento OK"], solo=[1, 2]),
  fichab("Documento de la fase O en los contratos",
         "El contratista justifica; el Servicio gestor expide el documento",
         "Aprobado el expediente de reconocimiento de la obligación → documento **OK**",
         "—",
         "Antes del OK, el contratista justifica el cumplimiento de la prestación **o la procedencia del abono a cuenta**: es el «servicio hecho» (→ III.2.5)."))}
""", 2)

T.ap("s11", "IV.3 Subvenciones: el gasto en la LGS (arts. 9.4 y 34)", f"""
{unidad("3.1 Requisitos presupuestarios del otorgamiento (art. 9.4)",
  lit("LGS", "Artículo 9", ["La existencia de crédito adecuado y suficiente", "La fiscalización previa de los actos administrativos de contenido económico", "La aprobación del gasto por el órgano competente para ello"], solo=[4, 5, 6, 7, 8, 9]),
  fichab("Requisitos del otorgamiento de una subvención (además de las bases reguladoras)",
         "El órgano concedente (→ II.3.2)",
         ["a) Competencia del órgano concedente", "b) Crédito adecuado y suficiente", "c) Procedimiento de concesión conforme a sus normas", "d) Fiscalización previa de los actos de contenido económico", "e) Aprobación del gasto por el órgano competente"],
         "—",
         "Tres de los cinco requisitos son presupuestarios: **crédito**, **fiscalización previa** y **aprobación del gasto**."))}

{unidad("3.2 Aprobación del gasto, compromiso y pago de la subvención (art. 34.1 a 3)",
  lit("LGS", "Artículo 34", ["Con carácter previo a la convocatoria de la subvención o a la concesión directa de la misma", "La resolución de concesión de la subvención conllevará el compromiso del gasto correspondiente", "El pago de la subvención se realizará previa justificación"], solo=[1, 2, 3]),
  fichab("Las fases del gasto en las subvenciones",
         "El órgano concedente",
         ["Aprobación del gasto (A): **antes** de la convocatoria o de la concesión directa", "Compromiso (D): lo conlleva la **resolución de concesión**", "Pago: previa **justificación** por el beneficiario de la actividad, proyecto u objetivo"],
         "—",
         "La **concesión** = compromiso. Pagos a cuenta y anticipados solo si los prevé la normativa reguladora (34.4); la justificación es del tema IV.7."))}
""", 2)

T.ap("s12", "IV.4 Subvenciones: los documentos contables (Instrucción, reglas 82, 83, 85 y 86)", f"""
{unidad("4.1 Concepto y clases a efectos contables (regla 82)",
  lit("OIOC", "regla82", ["sin contrapartida directa por parte de los beneficiarios", "Subvenciones nominativas", "Subvenciones paccionadas"]),
  fichab("Qué es una subvención para la Instrucción y qué tipos de tramitación hay",
         "Los centros gestores del Presupuesto de Gastos del Estado",
         ["Nominativas", "Paccionadas", "No nominativas sin convocatoria previa de carácter periódico", "No nominativas con convocatoria previa de carácter periódico", "Gestionadas por Comunidades Autónomas"],
         "—",
         f"Rasgos: entregas **dinerarias**, {c('OIOC', 'regla82', 'afectadas a una finalidad específica')} y **sin contrapartida directa**."))}

{unidad("4.2 Subvenciones nominativas: AD u ADOK (regla 83)",
  lit("OIOC", "regla83", ["aparecen con tal carácter en las Leyes de Presupuestos Generales del Estado", "el Servicio gestor formulará un documento AD o ADOK"]),
  fichab("Tramitación contable de las subvenciones nominativas",
         "El Servicio gestor, tras el acuerdo de concesión del órgano competente",
         ["RC potestativo («podrá expedir»)", "Acuerdo de concesión → **AD** o **ADOK**", "Si fue AD, al vencimiento de las obligaciones → **OK**"],
         "—",
         "Como el beneficiario ya está en la ley, autorización y compromiso van **juntos** desde el principio."))}

{unidad("4.3 No nominativas sin convocatoria periódica: ADOK o AD + OK (regla 85.2 a 4)",
  lit("OIOC", "regla85", ["el Servicio gestor expedirá un documento ADOK", "un documento AD por la parte que corresponda al ejercicio corriente"], solo=[3, 4, 5, 6]),
  fichab("Subvenciones que se conceden de forma continuada según se reciben las solicitudes",
         "El Servicio gestor",
         ["Durante la tramitación → **RC**", "Si la actividad se justifica **antes** de la concesión → **ADOK** al concederla", "Si se justifica **después** → **AD** al concederla y **OK** cuando se cumplan las condiciones"],
         "—",
         "El documento depende de **cuándo** se justifica la actividad."))}

{unidad("4.4 No nominativas con convocatoria periódica: A, D y OK (regla 86)",
  lit("OIOC", "regla86", ["existe una convocatoria previa", "aprobación que será previa a la publicación de la convocatoria", "Cuando se apruebe la concesión de las subvenciones, el Servicio gestor expedirá un documento D"], solo=[1, 3, 4, 5]),
  fichab("Subvenciones con convocatoria, plazo de solicitudes y selección de beneficiarios",
         "El Servicio gestor",
         ["Durante la tramitación → **RC**", "Aprobación del expediente de gasto, **antes de publicar la convocatoria** → **A**", "Concesión → **D**", "Cumplidas las condiciones → **OK**"],
         "La aprobación del gasto es **previa a la publicación de la convocatoria** en el BOE",
         "Es el caso en que las tres fases van **separadas**. Concuerda con el art. 34 LGS: gasto aprobado antes de la convocatoria; la concesión conlleva el compromiso (→ IV.3.2)."))}
""", 2)

T.ap("s13", "IV.5 Cuadro: fases y actos en contratos y subvenciones (esquema)", f"""
{ESQ}

| Fase | Contrato (LCSP y reglas 77 y 78) | Subvención con convocatoria (LGS 34 y regla 86) | Subvención nominativa (regla 83) |
|---|---|---|---|
| Retención | RC al inicio del expediente | RC durante la tramitación | RC potestativo |
| A · Aprobación | Aprobación del expediente (117.1 LCSP) | Aprobación del gasto **antes de la convocatoria** | AD o ADOK con el acuerdo de concesión |
| D · Compromiso | Formalización del contrato | **Resolución de concesión** | (incluido en AD/ADOK) |
| O · Reconocimiento | Justificación de la prestación o del abono a cuenta → OK | Cumplimiento de las condiciones → OK | OK al vencimiento (si hubo AD) |
| Pago | 30 días desde la aprobación de la conformidad (198.4 LCSP) | Previa justificación (34.3 LGS) | — |

{resumen([
  "Contratos: certificado de existencia de **crédito** y **fiscalización previa** en el expediente (116.3); la aprobación del expediente **implica la aprobación del gasto** (117.1); pago en **30 días** (198.4).",
  "Documentos de los contratos: **RC** al inicio, **A** al aprobar el expediente, **D** al formalizar, **OK** tras justificar la prestación (reglas 77 y 78).",
  "Subvenciones: aprobación del gasto **antes de la convocatoria** o de la concesión directa; la **concesión conlleva el compromiso**; pago previa **justificación** (LGS 34).",
  "Nominativas: **AD o ADOK**; con convocatoria periódica: **A, D y OK** separados (reglas 83 y 86)."],
  "Siguiente: V. ¿Qué documentos contables intervienen en la ejecución de los gastos y de los pagos?")}
""", 2)

# =============================================================================
T.ap("bV", "V. ¿Qué documentos contables intervienen en la ejecución de los gastos y de los pagos? (Orden de 1-2-1996 de documentos contables; Instrucción, regla 25; Orden PRE/1576/2002)", donde(
  "Quinta pregunta. Toda operación de gasto entra en el Sistema de Información Contable mediante un **documento contable**. La Orden de 1 de febrero de 1996 aprueba los modelos y dice para qué sirve cada uno y quién lo autoriza; la fase de pago se documenta con la **propuesta de pago**.",
  ["1 Normas generales: documentos electrónicos y firma (apartados segundo y tercero)", "2 Documentos del Presupuesto de Gastos (apartados quinto a séptimo)", "3 Claves de operación (anexo I)", "4 Documentos de los pagos: la propuesta de pago (regla 25; Orden PRE/1576/2002)", "5 Cuadro de documentos"]))

T.ap("s14", "V.1 Normas generales: documentos electrónicos y firma (Orden de 1-2-1996, apartados segundo y tercero)", f"""
{unidad("1.1 Aprobación de los documentos y carácter electrónico (apartado segundo)",
  lit("ODOC", "segundo", ["Todos los documentos contables serán electrónicos", "se podrán expedir documentos contables en papel"]),
  fichab("Qué son los documentos contables y en qué soporte se expiden",
         "La Orden aprueba los modelos; la **IGAE** fija el procedimiento de tramitación electrónica y autoriza excepciones",
         f"Son {c('ODOC', 'segundo', 'soporte para el registro de operaciones en el Sistema de Información Contable de la Administración General del Estado')}",
         "—",
         "Regla: **electrónicos**. Papel solo por circunstancias **excepcionales** que determine la **IGAE** a propuesta del responsable de la oficina de contabilidad."))}

{unidad("1.2 Agrupación de facturas en un documento con fase O (apartado tercero.4)",
  lit("ODOC", "tercero", ["cuando la fecha en la que se inicia el cómputo de los plazos para el abono del precio sea la misma para todas ellas"], solo=[1, 5, 6]),
  fichab("Firma y agrupación de facturas",
         f"Firma electrónica de {c('ODOC', 'tercero', 'quien tenga atribuidas las facultades para ello')}",
         ["No se agrupan en un mismo documento con fase O facturas registradas en el Registro Contable de Facturas junto con otras que no lo estén (salvo ADOK de reposición de caja fija)", "Solo se agrupan varias facturas si el cómputo del plazo de pago empieza en la **misma fecha**"],
         "—",
         "La fase **O** es la del reconocimiento de la obligación (OK, ADOK)."))}
""", 2)

T.ap("s15", "V.2 Documentos del Presupuesto de Gastos (Orden de 1-2-1996, apartados quinto a séptimo)", f"""
{unidad("2.1 Concepto y agrupaciones (apartado quinto)",
  lit("ODOC", "quinto", ["operaciones de gestión de créditos presupuestarios y de ejecución del Presupuesto de Gastos", "Presupuesto corriente.", "Ejercicios posteriores.", "Tramitación anticipada."]),
  fichab("Documentos de contabilidad del Presupuesto de Gastos",
         "—",
         ["Gestión de créditos (modificaciones, desgloses, retenciones)", "Ejecución del gasto (fases)"],
         "Agrupaciones: presupuesto corriente, presupuestos cerrados, ejercicios posteriores y tramitación anticipada",
         "Por eso hay documentos A, D y AD **de ejercicio corriente**, **de ejercicios posteriores** y **de tramitación anticipada** (→ V.2.3)."))}

{unidad("2.2 Gestión de los créditos: MC, desglose y RC (apartado sexto.1 a) a d)",
  lit("ODOC", "sexto", ["Se utilizará en las modificaciones presupuestarias que aumenten o disminuyan los créditos", "Documento de desglose", "Se utilizará para solicitar certificado de existencia y retención de crédito"], solo=[1, 2, 3, 4]),
  fichab("Documentos que no son fases del gasto: actúan sobre el crédito",
         "—",
         ["**MC**: modificaciones presupuestarias que aumentan o disminuyen los créditos", "**Documento de desglose**: desglose de aplicaciones presupuestarias y seguimiento de créditos distribuidos a servicios periféricos", "**RC**: certificado de existencia y retención de crédito (no disponibilidad: RC-102; presupuesto del cajero de ACF: RC-110)"],
         "—",
         "Las operaciones de desglose usan el «**Documento de desglose**» (cayó en 2025, → Cierre 1). Las modificaciones de crédito son del tema VI.3."))}

{unidad("2.3 Fases de autorización y compromiso: A, D y AD (apartado sexto.1 e) a j)",
  lit("ODOC", "sexto", ["Se utilizará en las operaciones de autorización del gasto imputables al Presupuesto corriente", "Se utilizará en las operaciones de compromiso de gasto imputables al Presupuesto corriente", "Se utilizará en operaciones de autorización del gasto imputables a Presupuestos futuros"], solo=[8, 9, 10, 11, 12, 13]),
  fichab("Documentos de las fases A y D",
         "—",
         ["**A**: autorización", "**D**: compromiso", "**AD**: autorización y compromiso combinados", "Cada uno, de ejercicio **corriente** o de ejercicios **posteriores** (presupuestos futuros); y de tramitación anticipada (letras k a l´)"],
         "—",
         "El examen mezcla **fase** (autorización/compromiso) y **ejercicio** (corriente/futuros): el D de ejercicio corriente es **compromiso + presupuesto corriente** (→ Cierre 1)."))}

{unidad("2.4 Reconocimiento y propuesta de pago: OK, ADOK, O y K (apartado sexto.1 n) a p)",
  lit("ODOC", "sexto", ["Documento OK: Se utilizará en operaciones de reconocimiento de obligaciones", "Documento ADOK", "exclusivamente en el ámbito de la gestión de la Deuda del Estado"], solo=[20, 21, 22, 23]),
  fichab("Documentos de la fase de reconocimiento",
         "—",
         ["**OK**: reconocimiento de obligaciones (con propuesta de pago)", "**ADOK**: autorización, compromiso y reconocimiento combinados", "**O**: solo en la **Deuda del Estado**, cuando no se propone el pago", "**K**: propuesta de pago en ese supuesto (y en obligaciones anteriores a la Orden sin pago propuesto)"],
         "—",
         "Fuera de la Deuda del Estado no se usa el documento O suelto: el reconocimiento va siempre con la propuesta de pago (**OK**)."))}

{unidad("2.5 Quién autoriza los documentos (apartado séptimo.1)",
  lit("ODOC", "septimo", ["serán autorizados por el Director General de Presupuestos"], solo=[1]),
  fichab("Autorización de los documentos del Presupuesto de Gastos",
         ["MC y RC-102: el **Director General de Presupuestos**", f"Los demás: {c('ODOC', 'septimo', 'el responsable del órgano que tenga encomendada la gestión de los créditos')} (con excepciones: RC de oficio, jefe de contabilidad; PR, quien aprobó la prescripción)"],
         "Mediante firma electrónica (apartado cuarto)",
         "—",
         "Las modificaciones de crédito y la no disponibilidad las autoriza **Presupuestos**, no el gestor."))}
""", 2)

T.ap("s16", "V.3 Claves de operación de los documentos (Orden de 1-2-1996, anexo I)", f"""
{unidad("3.1 Claves del documento MC y de las fases (anexo I, nota 2)",
  lit("ODOC", "ani", ["030 Créditos extraordinarios.", "040 Suplemento de créditos.", "420 Reconocimiento de obligaciones."], solo=[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 31, 32, 33, 35, 36, 38, 39, 40, 52, 53, 55, 56, 57], titulo="Anexo I, nota 2 (Orden de 1-2-1996, documentos contables): claves de operación"),
  fichab("Código numérico de cada operación en el documento contable",
         "El Servicio gestor, al cumplimentar el documento",
         ["MC: **030** crédito extraordinario, **040** suplemento, **050** ampliación, **060/061** transferencias positivas/negativas, **070** incorporación de remanentes, **080** generación por ingresos", "A: 200 / 210 · D: 300 · AD: 220 / 230 · OK: 420 · ADOK: 260 / 270"],
         "—",
         "Para un **crédito extraordinario** se expide un **MC con clave 030** (MC030); 070 es la incorporación y 060 la transferencia positiva (→ Cierre 1)."))}
""", 2)

T.ap("s17", "V.4 Documentos de los pagos: la propuesta de pago (Instrucción, regla 25; Orden PRE/1576/2002, apartados sexto y séptimo)", f"""
{unidad("4.1 Transmisión de las propuestas de pago al Tesoro (regla 25)",
  lit("OIOC", "regla25", ["una vez autorizada por el respectivo jefe de contabilidad, se transmitirá por medios informáticos a la Dirección General del Tesoro y Política Financiera"], solo=[1, 2, 3]),
  fichab("Cómo llegan las propuestas de pago al Ordenador de pagos",
         "Las **oficinas de contabilidad**; autoriza la relación definitiva el **jefe de contabilidad**",
         ["Relación provisional diaria de propuestas", "Comprobación con los documentos; las erróneas quedan en suspenso", "Relación definitiva → Dirección General del Tesoro y Política Financiera"],
         "Cada día, una vez contabilizadas las operaciones del día",
         "Las propuestas de pago nacen con el **OK** (o el ADOK): el reconocimiento lleva implícita la propuesta (→ III.2.5)."))}

{unidad("4.2 Quién propone el pago (Orden PRE/1576/2002, apartado sexto)",
  lit("OPAGO", "sexto", ["propondrán el pago de las mismas a la Dirección General del Tesoro y Política Financiera"], solo=[1, 3, 4, 5]),
  fichab("La propuesta de pago",
         f"{c('OPAGO', 'sexto', 'los órganos de la Administración General del Estado que dicten los actos administrativos de reconocimiento de obligaciones')}",
         "Mediante las propuestas de pago; la oficina de contabilidad las incorpora al Sistema y las pone a disposición del Tesoro",
         "—",
         "Propone quien **reconoce** la obligación; **ordena y paga** la Dirección General del Tesoro y Política Financiera (→ VI.3)."))}

{unidad("4.3 A favor de quién: acreedores directos y agentes mediadores (apartado séptimo.1.1 y 2)",
  lit("OPAGO", "septimo", ["se expedirán a favor de los acreedores directos", "En el procedimiento de pago a través del sistema de anticipos de caja fija", "En el procedimiento de pagos a justificar"], solo=[2, 5, 6, 7, 8, 9, 10]),
  fichab("Destinatario de las propuestas de pago",
         ["Regla: el **acreedor directo**", "Excepción: Cajas pagadoras, Habilitaciones, Pagadurías y otros agentes mediadores"],
         ["Retribuciones de personal", "Clases pasivas", "Anticipos de caja fija", "Pagos a justificar", "Otros que autorice la Dirección General del Tesoro y Política Financiera"],
         "—",
         "Desarrolla el art. 75.3 LGP (→ II.2.1). Caja fija y pagos a justificar son del tema VI.6."))}
""", 2)

T.ap("s18", "V.5 Cuadro de los documentos contables del gasto (esquema)", f"""
{ESQ}

| Documento | Para qué (apartado sexto) | Fase o momento | Autoriza (apartado séptimo) |
|---|---|---|---|
| MC | Modificaciones que aumentan o disminuyen créditos | Gestión del crédito | Director General de Presupuestos |
| Desglose | Desglose de aplicaciones presupuestarias | Gestión del crédito | Gestor de los créditos |
| RC | Certificado de existencia y retención de crédito | Antes de la autorización | Gestor (de oficio: jefe de contabilidad) |
| A | Autorización del gasto | Fase A | Gestor de los créditos |
| D | Compromiso de gasto | Fase D | Gestor de los créditos |
| AD | Autorización + compromiso | Fases A y D | Gestor de los créditos |
| OK | Reconocimiento de obligaciones (con propuesta de pago) | Fase O | Gestor de los créditos |
| ADOK | Autorización + compromiso + reconocimiento | Fases A, D y O | Gestor de los créditos |
| O / K | Reconocimiento sin propuesta / propuesta de pago | Solo Deuda del Estado | Gestor de los créditos |

{resumen([
  "Documentos **electrónicos** con firma electrónica; papel solo excepcionalmente si lo determina la **IGAE** (apartados segundo y tercero).",
  "Gestión del crédito: **MC**, **documento de desglose** y **RC**; fases: **A**, **D**, **AD**, **OK**, **ADOK**; **O** y **K** solo en la Deuda del Estado (apartado sexto).",
  "MC y RC-102 los autoriza el **Director General de Presupuestos**; los demás, el gestor de los créditos (apartado séptimo).",
  "Claves del MC: **030** crédito extraordinario, **040** suplemento, **050** ampliación, **070** incorporación (anexo I).",
  "La **propuesta de pago** la expide quien reconoce la obligación, a favor del **acreedor directo** (salvo agentes mediadores), y llega cada día al **Tesoro** (regla 25; Orden PRE/1576/2002)."],
  "Siguiente: VI. ¿Cómo se gestiona la tesorería del Estado?")}
""", 2)

# =============================================================================
T.ap("bVI", "VI. ¿Cómo se gestiona la tesorería del Estado? (LGP, arts. 90, 91, 106 a 110 y 112; Orden PRE/1576/2002)", donde(
  "Sexta y última pregunta. Las dos últimas fases del gasto (ordenación del pago y pago material) las ejecuta el **Tesoro Público**, que centraliza todos los fondos del Estado (unidad de caja) y gestiona la tesorería a través de cuentas en el **Banco de España**.",
  ["1 El Tesoro Público y sus funciones (arts. 90 y 91)", "2 Gestión de la tesorería: información, criterios, cuentas y medios de pago (arts. 106 a 110 y 112)", "3 Ordenación del pago y pago material (Orden PRE/1576/2002, apartados octavo y noveno)"]))

T.ap("s19", "VI.1 El Tesoro Público y sus funciones (LGP, arts. 90 y 91)", f"""
{unidad("1.1 Qué es el Tesoro Público (art. 90)",
  lit("LGP", "Artículo 90", ["todos los recursos financieros, sean dinero, valores o créditos", "tanto por operaciones presupuestarias como no presupuestarias"]),
  fichab("Concepto de Tesoro Público",
         "Recursos de la Administración General del Estado, sus organismos autónomos y el resto del sector público administrativo estatal (con las exclusiones del art. 2.2 b), d), g) y h) y 2.3)",
         "Todos sus recursos financieros: **dinero, valores o créditos**",
         "—",
         "Incluye las operaciones **presupuestarias y no presupuestarias**."))}

{unidad("1.2 Funciones del Tesoro Público (art. 91)",
  lit("LGP", "Artículo 91", ["Pagar las obligaciones del Estado y recaudar sus derechos", "Servir el principio de unidad de caja", "Distribuir en el tiempo y en el territorio las disponibilidades dinerarias", "Emitir, contraer y gestionar la deuda del Estado", "Responder de los avales contraídos por el Estado"]),
  fichab("Las funciones encomendadas al Tesoro Público",
         "El Tesoro Público",
         ["a) Pagar las obligaciones y recaudar los derechos", "b) **Unidad de caja**: centralizar todos los fondos y valores", "b bis) Gestionar los recursos con operaciones financieras activas o pasivas", "c) Distribuir en el tiempo y en el territorio las disponibilidades dinerarias", "d) Contribuir al buen funcionamiento del sistema financiero nacional", "e) Emitir, contraer y gestionar la deuda del Estado", "f) Responder de los avales del Estado", "g) Las demás relacionadas"],
         "—",
         f"La unidad de caja se sirve {c('LGP', 'Artículo 91', 'mediante la centralización de todos los fondos y valores generados por operaciones presupuestarias y no presupuestarias')}."))}
""", 2)

T.ap("s20", "VI.2 Gestión de la tesorería: información, criterios, cuentas y medios de pago (LGP, arts. 106 a 110 y 112)", f"""
{unidad("2.1 Información y retención de propuestas de pago (art. 106)",
  lit("LGP", "Artículo 106", ["podrá retener las propuestas de pago a favor de las entidades del sector público administrativo estatal"]),
  fichab("Facultades del Tesoro para gestionar la tesorería",
         "La **Dirección General del Tesoro y Política Financiera**",
         ["Recabar datos, previsiones y documentación sobre pagos e ingresos", "Retener propuestas de pago a favor de entidades del sector público administrativo estatal, según sus pagos previstos y su tesorería"],
         "—",
         "La retención del art. 106.2 se refiere a las propuestas de pago **a favor de entidades del sector público administrativo estatal**. Otra cosa es que las propuestas no seleccionadas en un proceso de ordenación queden retenidas para un proceso posterior (→ VI.3.1)."))}

{unidad("2.2 Criterios de ordenación de pagos (art. 107)",
  lit("LGP", "Artículo 107", ["criterios objetivos", "la fecha de recepción, el importe de la operación, la aplicación presupuestaria y la forma de pago"]),
  fichab("Cómo elige el Ordenador qué pagos ordena",
         "El Ordenador de Pagos",
         "Criterios **objetivos**: fecha de recepción, importe, aplicación presupuestaria y forma de pago, entre otros",
         "—",
         "La lista es **abierta** («entre otros»)."))}

{unidad("2.3 Las cuentas del Tesoro en el Banco de España (art. 108.1)",
  lit("LGP", "Artículo 108", ["se canalizarán a través de la cuenta o cuentas que se mantengan en el Banco de España", "requerirá de autorización previa de la Dirección General del Tesoro y Política Financiera"], solo=[1, 2]),
  fichab("Dónde están los fondos del Tesoro",
         "Administración General del Estado, organismos autónomos y resto del sector público administrativo estatal cuyos recursos integran el Tesoro",
         "Ingresos y pagos, con carácter general, por cuentas en el **Banco de España**; conforman la **posición global del Tesoro**",
         "—",
         "Abrir esas cuentas exige autorización previa del **Tesoro**, salvo las autorizadas por la **AEAT** en el sistema tributario y aduanero."))}

{unidad("2.4 Cuentas en otras entidades de crédito (art. 109.1)",
  lit("LGP", "Artículo 109", ["fuera del Banco de España requerirá previa autorización de la Dirección General del Tesoro y Política Financiera", "Transcurridos tres meses desde la solicitud y sin que se notifique la citada autorización, ésta se entenderá no concedida"], solo=[1, 4, 5]),
  fichab("Cuentas de situación de fondos fuera del Banco de España",
         "Autoriza la **Dirección General del Tesoro y Política Financiera**",
         ["Autorización previa con expresión de la finalidad y condiciones de uso", "Contrato con cláusula de exclusión de la compensación y respeto a la inembargabilidad de los fondos públicos"],
         "**Tres meses** sin notificar la autorización → se entiende **no concedida**",
         "Silencio **negativo** a los tres meses."))}

{unidad("2.5 Medios de pago (art. 110)",
  lit("LGP", "Artículo 110", ["transferencia bancaria, cheque, efectivo o cualesquiera otros medios de pago, sean o no bancarios"]),
  fichab("Con qué medios se cobra y se paga",
         "Los Ministros de Economía y de Hacienda, en sus ámbitos, establecen las condiciones",
         "Transferencia bancaria, cheque, efectivo u otros medios, bancarios o no; pueden limitarse ciertos ingresos o pagos a ciertos medios",
         "—",
         "La LGP admite todos los medios; la Orden PRE/1576/2002 fija la **transferencia** como forma general (→ VI.3.2)."))}

{unidad("2.6 Tesorería de los organismos autónomos (art. 112)",
  lit("LGP", "Artículo 112", ["Corresponde al presidente o director del organismo autónomo ordenar los pagos"]),
  fichab("Ordenación de pagos en los organismos autónomos",
         "El **presidente o director** del organismo autónomo",
         "Ordena los pagos de su presupuesto con los criterios del art. 107; canaliza ingresos y pagos según los arts. 108 a 110",
         "—",
         "En los organismos autónomos **no** ordena el Director General del Tesoro: lo hace su presidente o director (concuerda con el art. 74.2 → II.1.1)."))}
""", 2)

T.ap("s21", "VI.3 Ordenación del pago y pago material (Orden PRE/1576/2002, apartados octavo y noveno)", f"""
{unidad("3.1 Criterios de ordenación y retención de propuestas (apartado octavo.2.2)",
  lit("OPAGO", "octavo", ["aplicará los criterios de ordenación de pagos previstos en el artículo 107 de la Ley 47/2003", "quedarán retenidas a la espera de que se efectúe su ordenación en un proceso posterior"], solo=[9, 10]),
  fichab("La fase d): ordenación del pago",
         "La **Dirección General del Tesoro y Política Financiera**",
         "Completa y valida las propuestas con el **Fichero Central de Terceros**; aplica los criterios del art. 107 LGP y de gestión eficiente de tesorería; selecciona las que ordena",
         "—",
         "Las propuestas no ordenadas **no se rechazan**: quedan **retenidas** para un proceso posterior."))}

{unidad("3.2 Formas de pago: transferencia como regla (apartado noveno.1)",
  lit("OPAGO", "noveno", ["mediante transferencia bancaria contra la correspondiente cuenta del Tesoro en el Banco de España", "cheque nominativo no a la orden", "pagos en formalización"], solo=[1, 2]),
  fichab("La fase e): pago material",
         "El Tesoro; el **Director General del Tesoro y Política Financiera** autoriza el cheque",
         ["Regla: **transferencia bancaria** contra la cuenta del Tesoro en el Banco de España o en entidad de crédito autorizada", "Excepción: **cheque nominativo no a la orden**, solo para **personas físicas** y si hay circunstancias que lo justifiquen", "Pagos **en formalización** a conceptos de ingresos o no presupuestarios: sin variación efectiva de tesorería"],
         "—",
         "El cheque es excepcional y solo para **personas físicas**. El pago en formalización **no mueve dinero**."))}

{resumen([
  "Tesoro Público: **todos los recursos financieros** (dinero, valores o créditos) del sector público administrativo estatal, por operaciones presupuestarias y no presupuestarias (90).",
  "Funciones: pagar y recaudar; **unidad de caja**; distribuir en el tiempo y en el territorio; deuda; avales (91).",
  "El Tesoro puede **retener** propuestas de pago a favor de entidades del sector público administrativo estatal (106) y ordena con **criterios objetivos** (107).",
  "Cuentas en el **Banco de España**; fuera de él, autorización del Tesoro (silencio **negativo** a los **tres meses**) (108 y 109).",
  "Pago por **transferencia**; cheque nominativo solo para **personas físicas**; pagos en **formalización** sin movimiento de fondos (Orden PRE/1576/2002)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_L90 = examen("L", 90, {
  "a": f"Literal del art. 73.4 LGP: {g(73, 'El reconocimiento de la obligación es el acto mediante el que se declara la existencia de un crédito exigible contra la Hacienda Pública estatal')}.",
  "b": f"Es la definición del **compromiso** (art. 73.3): {g(73, 'se acuerda, tras el cumplimiento de los trámites legalmente establecidos, la realización de gastos previamente aprobados, por un importe determinado o determinable')}.",
  "c": f"Es la definición de la **aprobación** (art. 73.2): {g(73, 'se autoriza la realización de un gasto determinado por una cuantía cierta o aproximada')}.",
  "d": f"El pago es otra fase distinta y posterior ({g(73, 'Pago material')}); el reconocimiento solo {g(73, 'comporta la propuesta de pago correspondiente')}."},
  [("declara la existencia de un crédito exigible contra la Hacienda Pública estatal", "LGP", "Artículo 73", "se declara la existencia de un crédito exigible contra la Hacienda Pública estatal")])
EX_L91 = examen("L", 91, {
  "a": f"Literal de la regla 23.3: {c('OIOC', 'regla23', 'Una vez acordado el reconocimiento de la obligación, el Servicio gestor competente expedirá un documento OK')}.",
  "b": "«OP» no es un documento del Presupuesto de Gastos en la Orden de documentos contables (apartado sexto): la propuesta de pago va dentro del OK.",
  "c": f"El AD es de autorización y compromiso: {c('OIOC', 'regla24', 'cuando la autorización y el compromiso de gasto se acuerdan en un acto único, se expedirá un documento mixto AD')} (regla 24.2).",
  "d": f"El ADOK es para cuando {c('OIOC', 'regla24', 'en un mismo acto se acumulen la autorización del gasto, su compromiso y el reconocimiento de la obligación')} (regla 24.2), no para el reconocimiento de un gasto ya autorizado y comprometido."},
  [("documento OK", "OIOC", "regla23", "el Servicio gestor competente expedirá un documento OK")])
EX_L92 = examen("L", 92, {
  "a": f"La clave 070 es otra modificación: {c('ODOC', 'ani', '070 Incorporación de remanentes de crédito')}.",
  "b": f"La clave 060 es {c('ODOC', 'ani', '060 Transferencias de créditos positivas')}.",
  "c": f"Literal del anexo I, nota 2 a): {c('ODOC', 'ani', '030 Créditos extraordinarios')}; el documento MC es el de {c('ODOC', 'sexto', 'las modificaciones presupuestarias que aumenten o disminuyan los créditos')}.",
  "d": f"La clave 040 es {c('ODOC', 'ani', '040 Suplemento de créditos')}, no crédito extraordinario."},
  [("030", "ODOC", "ani", "030 Créditos extraordinarios")])
EX_L93 = examen("L", 93, {
  "a": f"Literal del apartado sexto.1 f): {c('ODOC', 'sexto', 'Documento D de ejercicio corriente: Se utilizará en las operaciones de compromiso de gasto imputables al Presupuesto corriente')}.",
  "b": f"Cambia el ejercicio: es el D **de ejercicios posteriores** el que {c('ODOC', 'sexto', 'Se utilizará en operaciones de compromiso de gasto imputables a Presupuestos futuros')} (letra i).",
  "c": f"Cambia la fase: es el documento **A** de ejercicio corriente el que {c('ODOC', 'sexto', 'Se utilizará en las operaciones de autorización del gasto imputables al Presupuesto corriente')} (letra e).",
  "d": f"Cambia fase y ejercicio: es el **AD de ejercicios posteriores**, que {c('ODOC', 'sexto', 'Se utilizará en operaciones que combinen autorización y compromiso de gasto imputables a Presupuestos futuros')} (letra j)."},
  [("compromiso de gasto imputables al presupuesto corriente", "ODOC", "sexto", "Se utilizará en las operaciones de compromiso de gasto imputables al Presupuesto corriente")])
EX_P92 = examen("P", 92, {
  "a": f"El Consejo de Ministros sí autoriza (más de doce millones), pero no aprueba después el órgano de contratación: {g(74, 'La autorización del Consejo de Ministros implicará la aprobación del gasto')}.",
  "b": f"Cambia el órgano: por encima de doce millones se necesita {g(74, 'autorización del Consejo de Ministros')}, no del Ministro; y la aprobación va implícita en ella.",
  "c": f"Cambia el órgano: con 15 millones se supera el umbral de {g(74, 'doce millones de euros')} y autoriza el **Consejo de Ministros**, no el Ministro.",
  "d": f"Art. 74.5 LGP: autorización del Consejo de Ministros {g(74, 'cuando el importe del gasto que de aquellos se derive sea superior a doce millones de euros')}, y {g(74, 'La autorización del Consejo de Ministros implicará la aprobación del gasto')}."},
  [("El Consejo de Ministros autoriza el gasto", "LGP", "Artículo 74", "necesitarán autorización del Consejo de Ministros cuando el importe del gasto que de aquellos se derive sea superior a doce millones de euros"),
   ("implica la aprobación del gasto", "LGP", "Artículo 74", "La autorización del Consejo de Ministros implicará la aprobación del gasto")])
EX_P93 = examen("P", 93, {
  "a": f"El Ministro de Economía es la **superior autoridad** bajo la que actúa el Ordenador: {g(75, 'Bajo la superior autoridad del Ministro de Economía')}; no es el Ordenador.",
  "b": "El art. 75.1 no atribuye la ordenación de pagos a ningún Secretario de Estado.",
  "c": "El art. 75.1 no atribuye la ordenación de pagos a ninguna Secretaría General: la atribuye a un **Director General**.",
  "d": f"Literal del art. 75.1: {g(75, 'competen al Director General del Tesoro y Política Financiera las funciones de Ordenador General de pagos del Estado')}."},
  [("Director General del Tesoro y Política Financiera", "LGP", "Artículo 75", "competen al Director General del Tesoro y Política Financiera las funciones de Ordenador General de pagos del Estado")])
EX_X95 = examen("X", 95, {
  "a": f"Literal del apartado sexto.1 b): {c('ODOC', 'sexto', 'Documento de desglose: Se utilizará en las operaciones de desglose de las aplicaciones presupuestarias')}.",
  "b": "Esa denominación no existe en el apartado sexto de la Orden: el documento se llama «Documento de desglose».",
  "c": f"Sí se utilizan: la Orden prevé un documento específico para {c('ODOC', 'sexto', 'las operaciones de desglose de las aplicaciones presupuestarias')}.",
  "d": "Tienen denominación específica: «Documento de desglose» (apartado sexto.1 b)."},
  [("Documento de desglose", "ODOC", "sexto", "Documento de desglose: Se utilizará en las operaciones de desglose de las aplicaciones presupuestarias")])

T.ap("s22", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **siete** preguntas de este tema: cuatro en el turno libre (fases y documentos contables), dos en promoción interna (competencias del art. 74.5 y Ordenador General de pagos) y una en el extraordinario (documento de desglose). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-L 2025, pregunta 90 · Reconocimiento de la obligación (→ III.1.3)", EX_L90,
  "### GACE-L 2025, pregunta 91 · Documento OK (→ III.2.5)", EX_L91,
  "### GACE-L 2025, pregunta 92 · Documento MC del crédito extraordinario (→ V.3.1)", EX_L92,
  "### GACE-L 2025, pregunta 93 · Documento D de ejercicio corriente (→ V.2.3)", EX_L93,
  "### GACE-P 2025, pregunta 92 · Convenio de 15 millones (→ II.1.2)", EX_P92,
  "### GACE-P 2025, pregunta 93 · Ordenador General de pagos (→ II.2.1)", EX_P93,
  "### GACE-L 2025 extraordinario, pregunta 95 · Documento de desglose (→ V.2.2)", EX_X95,
  "### Cómo se pregunta",
  "!> En las fases, los distractores son **las definiciones de las otras fases** del art. 73 LGP (aprobación ↔ compromiso ↔ reconocimiento). En los documentos, cambian **la fase** (A, D, AD, OK, ADOK) o **el ejercicio** (corriente o posteriores), o **la clave** (030, 040, 060, 070). En los órganos, el **umbral** (doce millones) y **quién** (Consejo de Ministros, Ministro, Director General del Tesoro).",
]))

T.ap("s23", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Reglas | Exigibilidad (21); créditos limitativos (46); principios (69) | Exceder el crédito: **nulidad de pleno derecho** |
| II. Órganos | Ministros aprueban, comprometen y reconocen (74.1); convenios (74.5); Ordenador de pagos (75); LCSP 323; LGS 10 | Convenio de más de **12 millones**: **Consejo de Ministros**, y su autorización **implica la aprobación**; Ordenador: **Director General del Tesoro y Política Financiera** |
| III. Fases | Aprobación, compromiso, reconocimiento, ordenación del pago y pago material (73); reglas 14, 20 a 24 y 27 | Reconocimiento: «declara la existencia de un **crédito exigible**»; documento **OK** |
| IV. Contratos y subvenciones | Aprobación del expediente = aprobación del gasto (LCSP 117); concesión = compromiso (LGS 34); reglas 77, 78, 83, 85 y 86 | Contrato: A al aprobar, **D al formalizar**, OK tras la prestación; pago en **30 días** |
| V. Documentos | MC, desglose, RC, A, D, AD, OK, ADOK, O, K; claves del anexo I; propuesta de pago | **MC030** crédito extraordinario; **D de ejercicio corriente** = compromiso imputable al presupuesto corriente; **documento de desglose** |
| VI. Tesorería | Tesoro Público (90); funciones (91); arts. 106 a 110 y 112; Orden PRE/1576/2002 | **Unidad de caja**; silencio **negativo** a los **3 meses** para cuentas fuera del Banco de España; pago por **transferencia** |

?> **Trampas frecuentes:** «el reconocimiento de la obligación es el acto que acuerda la realización de gastos previamente aprobados» (eso es el **compromiso**); «la aprobación tiene relevancia jurídica para con terceros» (es el **compromiso**); «el Ministro autoriza un convenio de 15 millones» (el **Consejo de Ministros**); «la autorización del Consejo de Ministros en las subvenciones implica la aprobación del gasto» (en las subvenciones **no**; en los convenios del art. 74.5, **sí**); «Ordenador General: el Ministro o el Secretario General del Tesoro» (es el **Director General del Tesoro y Política Financiera**); «documento O para cualquier reconocimiento» (solo en la **Deuda del Estado**); «MC040 para un crédito extraordinario» (040 es el **suplemento**).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
L = "LGP"
T.q(L, "Artículo 73", "Fases del gasto", "Según el artículo 73.1 de la Ley 47/2003, General Presupuestaria, ¿cuál es la primera fase de la gestión del Presupuesto de gastos del Estado?",
    ["Aprobación del gasto.", "Compromiso de gasto.", "Reconocimiento de la obligación.", "Ordenación del pago."], "Art. 73.1 LGP: a) aprobación, b) compromiso, c) reconocimiento, d) ordenación del pago, e) pago material.", "a) Aprobación del gasto.")
T.q(L, "Artículo 73", "Fases del gasto", "Según el artículo 73.1 de la Ley General Presupuestaria, la fase que sigue a la ordenación del pago es:",
    ["El pago material.", "El reconocimiento de la obligación.", "La propuesta de pago.", "La intervención formal del pago."], "Art. 73.1 LGP: d) Ordenación del pago; e) Pago material.", "e) Pago material.")
T.q(L, "Artículo 73", "Fases del gasto", "Según el artículo 73.2 de la Ley General Presupuestaria, la aprobación del gasto:",
    ["Inicia el procedimiento de ejecución del gasto, sin que implique relaciones con terceros ajenos a la Hacienda Pública estatal.", "Vincula a la Hacienda Pública estatal a la realización del gasto en la cuantía y condiciones establecidas.", "Declara la existencia de un crédito exigible contra la Hacienda Pública estatal.", "Es un acto con relevancia jurídica para con terceros."],
    "Art. 73.2 LGP. La vinculación y la relevancia frente a terceros son del compromiso (73.3); el crédito exigible, del reconocimiento (73.4).", "La aprobación inicia el procedimiento de ejecución del gasto, sin que implique relaciones con terceros ajenos a la Hacienda Pública estatal")
T.q(L, "Artículo 73", "Fases del gasto", "Según el artículo 73.3 de la Ley General Presupuestaria, el compromiso es el acto mediante el cual se acuerda la realización de gastos previamente aprobados por un importe:",
    ["Determinado o determinable.", "Cierto o aproximado.", "Máximo y estimado.", "Exigible y líquido."], "Art. 73.3 LGP: «por un importe determinado o determinable». La «cuantía cierta o aproximada» es de la aprobación (73.2).", "por un importe determinado o determinable")
T.q(L, "Artículo 73", "Fases del gasto", "Según el artículo 73.2 de la Ley General Presupuestaria, la aprobación autoriza la realización de un gasto determinado por una cuantía:",
    ["Cierta o aproximada.", "Determinada o determinable.", "Líquida y exigible.", "Máxima, sin reserva de crédito."], "Art. 73.2 LGP.", "se autoriza la realización de un gasto determinado por una cuantía cierta o aproximada")
T.q(L, "Artículo 73", "Fases del gasto", "Según el artículo 73.3 de la Ley General Presupuestaria, ¿qué fase es un acto con relevancia jurídica para con terceros?",
    ["El compromiso.", "La aprobación.", "La retención de crédito.", "La propuesta de pago."], "Art. 73.3 LGP: «El compromiso es un acto con relevancia jurídica para con terceros».", "El compromiso es un acto con relevancia jurídica para con terceros")
T.q(L, "Artículo 73", "Fases del gasto", "Según el artículo 73.4 de la Ley General Presupuestaria, el reconocimiento de obligaciones con cargo a la Hacienda Pública estatal se producirá:",
    ["Previa acreditación documental ante el órgano competente de la realización de la prestación o el derecho del acreedor.", "Previa ordenación del pago por el Director General del Tesoro.", "Previa autorización del Consejo de Ministros en todo caso.", "Una vez realizado el pago material."],
    "Art. 73.4 LGP.", "previa acreditación documental ante el órgano competente de la realización de la prestación o el derecho del acreedor")
T.q(L, "Artículo 73", "Fases del gasto", "Según el artículo 73.7 de la Ley General Presupuestaria, cuando la naturaleza de la operación o gasto así lo determinen:",
    ["Se acumularán en un solo acto las fases de ejecución precisas.", "Se suprimirá la fase de compromiso.", "El pago podrá preceder al reconocimiento de la obligación.", "No será necesaria la existencia de crédito."], "Art. 73.7 LGP.", "se acumularán en un solo acto las fases de ejecución precisas")
T.q(L, "Artículo 73", "Fases del gasto", "Según el artículo 73.5 de la Ley General Presupuestaria, los documentos y requisitos que correspondan a las fases del procedimiento de gasto los determinará la persona titular del Ministerio de Hacienda a propuesta de:",
    ["La Intervención General de la Administración del Estado.", "La Dirección General del Tesoro y Política Financiera.", "El Tribunal de Cuentas.", "La Dirección General de Presupuestos."], "Art. 73.5 LGP.", "a propuesta de la Intervención General de la Administración del Estado")
T.q(L, "Artículo 46", "Reglas", "Según el artículo 46 de la Ley General Presupuestaria, los actos administrativos que adquieran compromisos de gasto por cuantía superior al importe de los créditos autorizados son:",
    ["Nulos de pleno derecho.", "Anulables.", "Válidos, pero exigen un crédito extraordinario.", "Irregulares no invalidantes."], "Art. 46 LGP: «siendo nulos de pleno derecho».", "siendo nulos de pleno derecho los actos administrativos")
T.q(L, "Artículo 21", "Reglas", "Según el artículo 21.1 de la Ley General Presupuestaria, las obligaciones de la Hacienda Pública estatal solo son exigibles cuando resulten de la ejecución de los presupuestos, de operaciones no presupuestarias legalmente autorizadas o de:",
    ["Sentencia judicial firme.", "Cualquier resolución judicial.", "Acuerdo del Consejo de Ministros.", "Reclamación del acreedor no contestada en tres meses."], "Art. 21.1 LGP.", "de sentencia judicial firme")
T.q(L, "Artículo 69", "Reglas", "Según el artículo 69.1 de la Ley General Presupuestaria, la eficiencia en la gestión económico-financiera del sector público estatal se refiere a:",
    ["La asignación y utilización de recursos públicos.", "La consecución de los objetivos fijados.", "La transparencia de la actividad administrativa.", "La cooperación con otras Administraciones públicas."], "Art. 69.1 LGP: eficacia → objetivos; eficiencia → asignación y utilización de recursos.", "de la eficiencia en la asignación y utilización de recursos públicos")
T.q(L, "Artículo 74", "Órganos", "Según el artículo 74.1 de la Ley General Presupuestaria, los Ministros fijarán los límites por debajo de los cuales las competencias de gestión del gasto corresponderán, en su ámbito, a:",
    ["Los Secretarios de Estado y Subsecretario del departamento.", "Los Directores Generales.", "Los Delegados del Gobierno.", "Los Interventores Delegados."], "Art. 74.1 LGP, párrafo segundo.", "a los Secretarios de Estado y Subsecretario del departamento")
T.q(L, "Artículo 74", "Órganos", "Según el artículo 74.2 de la Ley General Presupuestaria, en los organismos autónomos del Estado la aprobación y compromiso del gasto, así como el reconocimiento y el pago de las obligaciones, compete a:",
    ["Sus presidentes o directores.", "El Ministro del que dependan.", "El Director General del Tesoro y Política Financiera.", "El Consejo de Ministros."], "Art. 74.2 LGP.", "compete a los presidentes o directores de los organismos autónomos del Estado")
T.q(L, "Artículo 74", "Órganos", "Según el artículo 74.4 de la Ley General Presupuestaria, las facultades de gestión del gasto podrán desconcentrarse mediante:",
    ["Real decreto acordado en Consejo de Ministros.", "Orden del Ministro de Hacienda.", "Resolución de la Intervención General.", "Ley de Presupuestos Generales del Estado exclusivamente."], "Art. 74.4 LGP.", "podrán desconcentrarse mediante real decreto acordado en Consejo de Ministros")
T.q(L, "Artículo 74", "Órganos", "Según el artículo 74.5 de la Ley General Presupuestaria, la suscripción de convenios por los órganos de los departamentos ministeriales necesitará autorización del Consejo de Ministros cuando el importe del gasto sea superior a:",
    ["Doce millones de euros.", "Seis millones de euros.", "Quince millones de euros.", "Doce millones de euros, IVA excluido, solo si el convenio es plurianual."], "Art. 74.5 LGP.", "superior a doce millones de euros")
T.q(L, "Artículo 75", "Órganos", "Según el artículo 75.2 de la Ley General Presupuestaria, las funciones de Ordenador general de pagos de las Entidades gestoras y Servicios comunes de la Seguridad Social competen a:",
    ["El Director General de la Tesorería General de la Seguridad Social.", "El Director General del Tesoro y Política Financiera.", "El Secretario de Estado de la Seguridad Social.", "El Interventor General de la Seguridad Social."], "Art. 75.2 LGP.", "competen al Director General de la Tesorería General de la Seguridad Social las funciones de Ordenador general de pagos")
T.q("LGS", "Artículo 10", "Órganos", "Según el artículo 10.2 de la Ley 38/2003, General de Subvenciones, la autorización del Consejo de Ministros para conceder subvenciones de cuantía superior a 12 millones de euros:",
    ["No implicará la aprobación del gasto, que corresponderá en todo caso al órgano competente.", "Implicará la aprobación del gasto.", "Implicará la aprobación del gasto y su compromiso.", "Sustituirá a la resolución de concesión."], "Art. 10.2 LGS. Diferencia con los convenios del art. 74.5 LGP, donde la autorización sí implica la aprobación.", "La referida autorización no implicará la aprobación del gasto, que, en todo caso, corresponderá al órgano competente")
T.q("LCSP", "Artículo 323", "Órganos", "Según el artículo 323.1 de la Ley 9/2017, de Contratos del Sector Público, son órganos de contratación de la Administración General del Estado:",
    ["Los Ministros y los Secretarios de Estado.", "Los Subsecretarios y los Directores Generales.", "El Consejo de Ministros y los Ministros.", "Las Juntas de Contratación en todo caso."], "Art. 323.1 LCSP.", "Los Ministros y los Secretarios de Estado son los órganos de contratación de la Administración General del Estado")
T.q("LCSP", "Artículo 117", "Contratación", "Según el artículo 117.1 de la Ley de Contratos del Sector Público, la resolución que aprueba el expediente de contratación implicará también, como regla general:",
    ["La aprobación del gasto.", "El compromiso del gasto.", "El reconocimiento de la obligación.", "La adjudicación del contrato."], "Art. 117.1 LCSP.", "Dicha resolución implicará también la aprobación del gasto")
T.q("LCSP", "Artículo 198", "Contratación", "Según el artículo 198.4 de la Ley de Contratos del Sector Público, la Administración tendrá la obligación de abonar el precio dentro de los:",
    ["Treinta días siguientes a la fecha de aprobación de las certificaciones de obra o de los documentos que acrediten la conformidad.", "Sesenta días siguientes a la fecha de aprobación de las certificaciones de obra.", "Treinta días siguientes a la formalización del contrato.", "Quince días siguientes a la presentación de la factura."], "Art. 198.4 LCSP.", "dentro de los treinta días siguientes a la fecha de aprobación de las certificaciones de obra")
T.q("LGS", "Artículo 34", "Subvenciones", "Según el artículo 34.2 de la Ley General de Subvenciones, la resolución de concesión de la subvención conllevará:",
    ["El compromiso del gasto correspondiente.", "La aprobación del gasto correspondiente.", "El reconocimiento de la obligación y el pago.", "La fiscalización previa del gasto."], "Art. 34.2 LGS. La aprobación del gasto es previa a la convocatoria (34.1).", "La resolución de concesión de la subvención conllevará el compromiso del gasto correspondiente")
T.q("LGS", "Artículo 34", "Subvenciones", "Según el artículo 34.1 de la Ley General de Subvenciones, la aprobación del gasto deberá efectuarse:",
    ["Con carácter previo a la convocatoria de la subvención o a la concesión directa de la misma.", "Una vez dictada la resolución de concesión.", "Al justificar el beneficiario la actividad subvencionada.", "Con el pago de la subvención."], "Art. 34.1 LGS.", "Con carácter previo a la convocatoria de la subvención o a la concesión directa de la misma, deberá efectuarse la aprobación del gasto")
T.q("OIOC", "regla23", "Fases del gasto", "Según la regla 23 de la Instrucción de operatoria contable a seguir en la ejecución del gasto del Estado, el reconocimiento de la obligación en las obligaciones recíprocas se produce según el principio:",
    ["Del «servicio hecho».", "De caja única.", "De devengo anticipado.", "De especialidad cualitativa."], "Regla 23.1.", "según el principio del «servicio hecho»")
T.q("OIOC", "regla24", "Fases del gasto", "Según la regla 24 de la Instrucción de operatoria contable, cuando la autorización y el compromiso de gasto se acuerdan en un acto único se expedirá un documento:",
    ["AD.", "ADOK.", "OK.", "RC."], "Regla 24.2.", "se expedirá un documento mixto AD")
T.q("OIOC", "regla14", "Fases del gasto", "Según la regla 14 de la Instrucción de operatoria contable, para solicitar el certificado de existencia de crédito al inicio de un expediente de gasto, el Servicio Gestor expedirá un documento:",
    ["RC.", "A.", "MC.", "K."], "Regla 14.1.", "el Servicio Gestor expedirá un documento RC")
T.q("OIOC", "regla77", "Contratación", "Según la regla 77 de la Instrucción de operatoria contable, cuando se formalicen los contratos el Servicio gestor competente expedirá el respectivo documento:",
    ["D.", "A.", "OK.", "RC."], "Regla 77.2: aprobado el expediente → A; formalizado el contrato → D.", "Cuando se formalicen los contratos, el Servicio gestor competente expedirá el respectivo documento D")
T.q("OIOC", "regla83", "Subvenciones", "Según la regla 83 de la Instrucción de operatoria contable, una vez dictado el acuerdo de concesión de una subvención nominativa, el Servicio gestor formulará un documento:",
    ["AD o ADOK.", "A.", "RC.", "D de ejercicios posteriores en todo caso."], "Regla 83.3.", "el Servicio gestor formulará un documento AD o ADOK")
T.q("OIOC", "regla86", "Subvenciones", "Según la regla 86 de la Instrucción de operatoria contable, en las subvenciones con convocatoria previa de carácter periódico la aprobación del expediente de gasto será:",
    ["Previa a la publicación de la convocatoria en el «Boletín Oficial del Estado».", "Simultánea a la resolución de concesión.", "Posterior a la justificación de la actividad.", "Posterior a la publicación de la convocatoria."], "Regla 86.3.", "aprobación que será previa a la publicación de la convocatoria")
T.q("ODOC", "sexto", "Documentos contables", "Según la Orden de 1 de febrero de 1996 por la que se aprueban los documentos contables, el documento ADOK se utilizará en operaciones que combinen:",
    ["La autorización, compromiso y reconocimiento de obligaciones.", "La autorización y el compromiso de gasto.", "El reconocimiento de la obligación y el pago material.", "La retención de crédito y la autorización del gasto."], "Apartado sexto.1 ñ).", "Se utilizará en operaciones que combinen la autorización, compromiso y reconocimiento de obligaciones")
T.q("ODOC", "sexto", "Documentos contables", "Según la Orden de 1 de febrero de 1996 de documentos contables, el documento O (reconocimiento de la obligación sin propuesta de pago) se utilizará:",
    ["Exclusivamente en el ámbito de la gestión de la Deuda del Estado.", "En todos los contratos de obras.", "En las subvenciones nominativas.", "En los gastos de personal."], "Apartado sexto.1 o).", "Se utilizará exclusivamente en el ámbito de la gestión de la Deuda del Estado")
T.q("ODOC", "sexto", "Documentos contables", "Según la Orden de 1 de febrero de 1996 de documentos contables, el documento A de ejercicios posteriores se utilizará en:",
    ["Operaciones de autorización del gasto imputables a Presupuestos futuros.", "Operaciones de compromiso de gasto imputables a Presupuestos futuros.", "Operaciones de autorización del gasto imputables al Presupuesto corriente.", "Modificaciones presupuestarias de ejercicios futuros."], "Apartado sexto.1 h).", "Se utilizará en operaciones de autorización del gasto imputables a Presupuestos futuros")
T.q("ODOC", "septimo", "Documentos contables", "Según el apartado séptimo de la Orden de 1 de febrero de 1996 de documentos contables, los documentos MC de «modificación de créditos» serán autorizados por:",
    ["El Director General de Presupuestos.", "El Interventor General de la Administración del Estado.", "El responsable del órgano gestor de los créditos.", "El jefe de contabilidad."], "Apartado séptimo.1.", "serán autorizados por el Director General de Presupuestos")
T.q("ODOC", "segundo", "Documentos contables", "Según el apartado segundo de la Orden de 1 de febrero de 1996 de documentos contables, los documentos contables:",
    ["Serán electrónicos; solo por circunstancias excepcionales que determine la IGAE podrán expedirse en papel.", "Se expedirán en papel y se digitalizarán después.", "Podrán expedirse en papel o en formato electrónico a elección del servicio gestor.", "Serán electrónicos salvo en las Delegaciones de Economía y Hacienda."], "Apartado segundo.2.", "Todos los documentos contables serán electrónicos")
T.q("ODOC", "ani", "Documentos contables", "Según el anexo I de la Orden de 1 de febrero de 1996 de documentos contables, en el documento MC la clave de operación 040 corresponde a:",
    ["Suplemento de créditos.", "Créditos extraordinarios.", "Ampliación de créditos.", "Incorporación de remanentes de crédito."], "Anexo I, nota 2 a): 030 créditos extraordinarios, 040 suplemento, 050 ampliación, 070 incorporación.", "040 Suplemento de créditos.")
T.q("OPAGO", "noveno", "Tesorería", "Según la Orden PRE/1576/2002, el pago de las obligaciones de la Administración General del Estado mediante cheque nominativo no a la orden:",
    ["Es excepcional y solo para personas físicas, autorizado por el Director General del Tesoro y Política Financiera.", "Es la forma general de pago.", "Solo procede para personas jurídicas públicas.", "Lo autoriza el Interventor Delegado del departamento."], "Apartado noveno.1.", "sólo para las personas físicas, el Director General del Tesoro y Política Financiera podrá autorizar el pago mediante cheque nominativo no a la orden")
T.q(L, "Artículo 91", "Tesorería", "Según el artículo 91 de la Ley General Presupuestaria, el principio de unidad de caja se sirve mediante:",
    ["La centralización de todos los fondos y valores generados por operaciones presupuestarias y no presupuestarias.", "La apertura de cuentas en todas las entidades de crédito.", "La descentralización de los fondos en las cajas pagadoras.", "La centralización solo de los fondos presupuestarios."], "Art. 91 b) LGP.", "mediante la centralización de todos los fondos y valores generados por operaciones presupuestarias y no presupuestarias")
T.q(L, "Artículo 90", "Tesorería", "Según el artículo 90 de la Ley General Presupuestaria, constituyen el Tesoro Público:",
    ["Todos los recursos financieros, sean dinero, valores o créditos, tanto por operaciones presupuestarias como no presupuestarias.", "Solo el dinero procedente de operaciones presupuestarias.", "Los valores representativos de la Deuda del Estado.", "Los fondos depositados en la Caja General de Depósitos."], "Art. 90 LGP.", "todos los recursos financieros, sean dinero, valores o créditos")
T.q(L, "Artículo 109", "Tesorería", "Según el artículo 109.1 de la Ley General Presupuestaria, transcurridos tres meses desde la solicitud de autorización para abrir una cuenta fuera del Banco de España sin que se notifique:",
    ["La autorización se entenderá no concedida.", "La autorización se entenderá concedida.", "Deberá reiterarse ante el Ministro de Hacienda.", "La cuenta podrá abrirse con carácter provisional."], "Art. 109.1 LGP: silencio negativo.", "Transcurridos tres meses desde la solicitud y sin que se notifique la citada autorización, ésta se entenderá no concedida")
T.q(L, "Artículo 112", "Tesorería", "Según el artículo 112.1 de la Ley General Presupuestaria, ordenar los pagos en ejecución del Presupuesto de Gastos de un organismo autónomo corresponde a:",
    ["El presidente o director del organismo autónomo.", "El Director General del Tesoro y Política Financiera.", "El Ministro de adscripción.", "El Interventor Delegado en el organismo."], "Art. 112.1 LGP.", "Corresponde al presidente o director del organismo autónomo ordenar los pagos")
T.q(L, "Artículo 107", "Tesorería", "Según el artículo 107 de la Ley General Presupuestaria, en la expedición de las órdenes de pago el Ordenador de Pagos aplicará:",
    ["Criterios objetivos, tales como la fecha de recepción, el importe de la operación, la aplicación presupuestaria y la forma de pago.", "El criterio de oportunidad política que fije el Gobierno.", "Exclusivamente el orden de presentación de las facturas.", "Los criterios que fije cada Ministro gestor."], "Art. 107 LGP.", "El Ordenador de Pagos aplicará criterios objetivos en la expedición de las órdenes de pago")

T.real("L", 90, "Fases del gasto"); T.real("L", 91, "Fases del gasto"); T.real("L", 92, "Documentos contables"); T.real("L", 93, "Documentos contables")
T.real("P", 92, "Órganos"); T.real("P", 93, "Órganos"); T.real("X", 95, "Documentos contables")

# Flashcards
for q_, a_, cat in [
  ("¿Cuándo son exigibles las obligaciones de la Hacienda Pública estatal? (LGP, art. 21.1)", "Cuando resulten de la ejecución de los presupuestos, de sentencia judicial firme o de operaciones no presupuestarias legalmente autorizadas.", "Reglas"),
  ("Consecuencia de comprometer gasto por encima del crédito (LGP, art. 46)", "Nulidad de pleno derecho de los actos y disposiciones de rango inferior a ley, además de responsabilidades.", "Reglas"),
  ("Las cinco fases de la gestión del gasto (LGP, art. 73.1)", "Aprobación, compromiso, reconocimiento de la obligación, ordenación del pago y pago material.", "Fases del gasto"),
  ("Aprobación del gasto (art. 73.2)", "Autoriza un gasto por cuantía cierta o aproximada y reserva crédito; inicia el procedimiento sin relaciones con terceros.", "Fases del gasto"),
  ("Compromiso del gasto (art. 73.3)", "Acuerda la realización de gastos aprobados por importe determinado o determinable; tiene relevancia jurídica para con terceros.", "Fases del gasto"),
  ("Reconocimiento de la obligación (art. 73.4)", "Declara la existencia de un crédito exigible contra la Hacienda; deriva de un gasto aprobado y comprometido y comporta la propuesta de pago.", "Fases del gasto"),
  ("¿Quién aprueba y compromete los gastos del Estado y reconoce las obligaciones? (art. 74.1)", "Los Ministros y los titulares de los demás órganos con dotaciones diferenciadas, salvo lo reservado al Consejo de Ministros.", "Órganos"),
  ("Convenios de más de 12 millones (art. 74.5)", "Autorización del Consejo de Ministros, que implica la aprobación del gasto.", "Órganos"),
  ("Ordenador General de pagos del Estado (art. 75.1)", "El Director General del Tesoro y Política Financiera, bajo la superior autoridad del Ministro de Economía.", "Órganos"),
  ("Subvenciones de más de 12 millones (LGS, art. 10.2)", "Autorización previa del Consejo de Ministros, que no implica la aprobación del gasto.", "Órganos"),
  ("Documento que expide el Servicio gestor al acordar el reconocimiento de la obligación (regla 23)", "Documento OK.", "Fases del gasto"),
  ("Documentos mixtos (regla 24)", "AD (autorización y compromiso) y ADOK (autorización, compromiso y reconocimiento); mismos efectos que las fases separadas.", "Fases del gasto"),
  ("Contratos: ¿qué acto implica la aprobación del gasto? (LCSP, art. 117.1)", "La resolución que aprueba el expediente de contratación.", "Contratación"),
  ("Contratos: documentos de cada fase (reglas 77 y 78)", "RC al inicio; A al aprobar el expediente; D al formalizar el contrato; OK tras justificar la prestación.", "Contratación"),
  ("Subvenciones: aprobación y compromiso del gasto (LGS, art. 34)", "Aprobación antes de la convocatoria o de la concesión directa; la resolución de concesión conlleva el compromiso.", "Subvenciones"),
  ("¿Para qué sirve el documento de desglose? (Orden de 1-2-1996, sexto.1 b)", "Para las operaciones de desglose de las aplicaciones presupuestarias y el seguimiento de créditos distribuidos a servicios periféricos.", "Documentos contables"),
  ("Documento y clave para un crédito extraordinario (anexo I)", "Documento MC, clave 030.", "Documentos contables"),
  ("Documento O (sexto.1 o)", "Reconocimiento sin propuesta de pago, exclusivamente en la gestión de la Deuda del Estado.", "Documentos contables"),
  ("¿Quién autoriza los documentos MC y RC-102? (séptimo.1)", "El Director General de Presupuestos.", "Documentos contables"),
  ("Funciones del Tesoro Público (LGP, art. 91)", "Pagar y recaudar; unidad de caja; gestionar recursos; distribuir disponibilidades en el tiempo y el territorio; sistema financiero; deuda; avales.", "Tesorería"),
  ("Forma general de pago de las obligaciones del Estado (Orden PRE/1576/2002, noveno.1)", "Transferencia bancaria contra la cuenta del Tesoro; cheque nominativo no a la orden solo excepcionalmente y para personas físicas.", "Tesorería"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Créditos limitativos", "No pueden adquirirse compromisos ni obligaciones por encima de los créditos autorizados; lo contrario es nulo de pleno derecho (LGP, art. 46).", "s1", "Reglas")
T.glos("Aprobación del gasto", "Fase que autoriza un gasto determinado por cuantía cierta o aproximada y reserva crédito, sin relaciones con terceros (LGP, art. 73.2); la Instrucción la llama autorización (documento A).", "s6", "Fases del gasto")
T.glos("Compromiso del gasto", "Fase que acuerda la realización de gastos aprobados por importe determinado o determinable; vincula frente a terceros (LGP, art. 73.3); documento D.", "s6", "Fases del gasto")
T.glos("Reconocimiento de la obligación", "Acto que declara la existencia de un crédito exigible contra la Hacienda y comporta la propuesta de pago (LGP, art. 73.4); documento OK.", "s6", "Fases del gasto")
T.glos("Ordenador General de pagos", "Órgano que ordena los pagos del Estado: el Director General del Tesoro y Política Financiera (LGP, art. 75.1).", "s4", "Órganos")
T.glos("Servicio hecho", "Principio por el que se reconoce la obligación recíproca una vez cumplida la prestación por el tercero (Instrucción de operatoria contable, regla 23.1).", "s7", "Fases del gasto")
T.glos("Fases mixtas", "Acumulación de fases en un acto: AD y ADOK, con los mismos efectos que si se acordaran por separado (regla 24).", "s7", "Fases del gasto")
T.glos("Documento RC", "Retención de crédito: certificado de existencia y retención de crédito en los expedientes de gasto (Orden de 1-2-1996, sexto.1 c; regla 14).", "s15", "Documentos contables")
T.glos("Documento MC", "Documento de las modificaciones presupuestarias que aumentan o disminuyen los créditos; lo autoriza el Director General de Presupuestos (Orden de 1-2-1996, sexto y séptimo).", "s15", "Documentos contables")
T.glos("Propuesta de pago", "Solicitud del órgano que reconoce la obligación para que se ordene su pago; va implícita en el reconocimiento (regla 23.3; Orden PRE/1576/2002, sexto).", "s17", "Documentos contables")
T.glos("Tesoro Público", "Todos los recursos financieros (dinero, valores o créditos) del sector público administrativo estatal, por operaciones presupuestarias y no presupuestarias (LGP, art. 90).", "s19", "Tesorería")
T.glos("Unidad de caja", "Principio que sirve el Tesoro centralizando todos los fondos y valores generados por operaciones presupuestarias y no presupuestarias (LGP, art. 91 b).", "s19", "Tesorería")

# Cronología (fechas de los metadatos del BOE)
T.hito("1996", "Orden de 1 de febrero de 1996 por la que se aprueba la Instrucción de operatoria contable a seguir en la ejecución del gasto del Estado (BOE de 8-2-1996)", "Reglas de las fases de ejecución y de sus documentos", "normativo", "s7")
T.hito("1996", "Orden de 1 de febrero de 1996 por la que se aprueban los documentos contables a utilizar por la Administración General del Estado (BOE de 9-2-1996)", "Modelos y usos de los documentos contables", "normativo", "s15")
T.hito("2002", "Orden PRE/1576/2002, de 19 de junio, procedimiento para el pago de obligaciones de la Administración General del Estado (BOE de 26-6-2002)", "Propuestas de pago, ordenación y pago material", "normativo", "s21")
T.hito("2003", "Ley 38/2003, de 17 de noviembre, General de Subvenciones (BOE de 18-11-2003)", "Arts. 9, 10 y 34: requisitos, órganos y fases del gasto en las subvenciones", "normativo", "s11")
T.hito("2003", "Ley 47/2003, de 26 de noviembre, General Presupuestaria (BOE de 27-11-2003)", "Arts. 73 a 75: fases, competencias y ordenación de pagos; arts. 90 y ss.: Tesoro Público", "normativo", "s6")
T.hito("2017", "Ley 9/2017, de 8 de noviembre, de Contratos del Sector Público (BOE de 9-11-2017)", "Arts. 116 y 117: crédito y aprobación del gasto en el expediente de contratación", "normativo", "s9")

T.publicar()
