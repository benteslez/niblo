# -*- coding: utf-8 -*-
"""Tema VI.3 (B6T03): Gastos plurianuales. Modificaciones de los créditos iniciales.
Transferencias de crédito. Créditos extraordinarios. Suplementos de crédito. Ampliaciones
de créditos. Incorporaciones de créditos. Generaciones de créditos.
Método del I.2. Norma (texto consolidado del BOE): Ley 47/2003, General Presupuestaria
(LGP), arts. 47 a 63 (con cita del art. 22.2 a de la Ley 38/2003, General de Subvenciones)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *


def g(art, frag):
    """Cita literal de la LGP."""
    return c("LGP", "Artículo " + str(art), frag)


T = Tema("B6T03",
  "Seis preguntas: I. Cómo se comprometen gastos para ejercicios futuros (LGP, arts. 47, 47 bis y 48) · II. Qué modificaciones de crédito hay, con qué se financian y qué es una transferencia (arts. 49 a 52) · III. Cómo crecen los créditos por ingresos o por obligaciones: generaciones y ampliaciones (arts. 53 y 54) · IV. Qué se hace si no hay crédito o no basta: créditos extraordinarios y suplementos (arts. 55 a 57) · V. Cómo pasan los remanentes al ejercicio siguiente: incorporaciones (arts. 58 y 59) · VI. Quién autoriza cada modificación (arts. 60 a 63). Cada artículo: texto literal del BOE y ficha.",
  ["Gastos plurianuales", "Art. 47 LGP", "Art. 47 bis", "Modificaciones de crédito", "Transferencias", "Generaciones", "Créditos ampliables", "Créditos extraordinarios", "Suplementos de crédito", "Fondo de Contingencia", "Incorporaciones", "Anticipos de Tesorería", "Competencias"])

# =============================================================================
T.ap("s0", "Mapa del tema: seis preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque VI, tema 3):
> Gastos plurianuales. Modificaciones de los créditos iniciales. Transferencias de crédito. Créditos extraordinarios. Suplementos de crédito. Ampliaciones de créditos. Incorporaciones de créditos. Generaciones de créditos.

### El hilo conductor

El epígrafe se lee como **seis preguntas encadenadas**, en el orden de los artículos de la Ley General Presupuestaria. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Ley 47/2003, General Presupuestaria |
|---|---|---|
| **I** | ¿Cómo se comprometen gastos para ejercicios futuros? (gastos plurianuales) | Arts. 47, 47 bis y 48 |
| **II** | ¿Qué modificaciones de los créditos iniciales hay, con qué se financian y qué es una transferencia? | Arts. 49, 50, 51 y 52 |
| **III** | ¿Cómo crecen los créditos por ingresos o por obligaciones? (generaciones y ampliaciones) | Arts. 53 y 54 |
| **IV** | ¿Qué se hace si no hay crédito o no basta? (créditos extraordinarios y suplementos) | Arts. 55, 56 y 57 |
| **V** | ¿Cómo pasan los remanentes al ejercicio siguiente? (incorporaciones) | Arts. 58 y 59 |
| **VI** | ¿Quién autoriza cada modificación? (y los anticipos de Tesorería) | Arts. 60, 61, 62 y 63 |

!> **La idea que une los seis bloques:** los créditos para gastos son limitativos (art. 46, tema VI.5) y se gastan en su ejercicio (art. 49, → II.1.1). El tema estudia las dos válvulas de esa regla: comprometer gasto **para ejercicios futuros** con límites (I) y **cambiar los créditos** durante el ejercicio, solo por las cinco vías del art. 51 (II a V), cada una con su órgano competente (VI).

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- Fronteras: la estructura del presupuesto y la especificación de los créditos (arts. 39 a 44) son del tema VI.2; el carácter limitativo de los créditos (art. 46) y los documentos contables de las modificaciones, del tema VI.5.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Cómo se comprometen gastos para ejercicios futuros? Gastos plurianuales (arts. 47, 47 bis y 48)", donde(
  "Primera pregunta del tema. Un crédito vale para su ejercicio, pero muchos gastos (una obra, un arrendamiento) duran varios años. La LGP permite **comprometer** gasto para ejercicios posteriores dentro de **límites** de años y de porcentajes.",
  ["1 Compromisos de gasto plurianual: requisitos, límites y excepciones (art. 47)", "2 Qué pasa si después no hay crédito suficiente (art. 47 bis)", "3 Inmuebles con pago aplazado y obras de abono total (art. 48)"]))

T.ap("s1", "I.1 Compromisos de gasto de carácter plurianual (art. 47)", f"""
{unidad("1.1 Requisitos y límites (art. 47.1 y 2)",
  lit("LGP", "Artículo 47", ["siempre que su ejecución se inicie en el propio ejercicio", "no será superior a cuatro", "el 70 por ciento", "el 60 por ciento", "el 50 por ciento", "retención adicional de crédito del 10 por ciento del importe de adjudicación", "carga financiera de la Deuda y de los arrendamientos de inmuebles"], solo=[1, 2, 3, 4]),
  fichab(f"{g(47, 'compromisos de gastos que hayan de extenderse a ejercicios posteriores a aquel en que se autoricen')}",
         "Los límites los fija la ley; solo el Gobierno puede excepcionarlos (→ I.1.2)",
         ["::Requisitos:", "Que la ejecución se inicie en el propio ejercicio", "Que no se superen los límites y anualidades del apartado 2", "Obras plurianuales (salvo abono total del precio): retención adicional del 10 % del importe de adjudicación, que computa dentro de los porcentajes"],
         ["::Máximo **cuatro** ejercicios; porcentajes sobre el **crédito inicial** de la operación:", "Ejercicio inmediato siguiente: **70 %**", "Segundo ejercicio: **60 %**", "Ejercicios tercero y cuarto: **50 %**"],
         "**4** ejercicios y **70 / 60 / 50 / 50**. No se aplican a la **carga financiera de la Deuda** ni a los **arrendamientos de inmuebles** (incluidos los contratos mixtos de arrendamiento y adquisición). La retención de las obras es del **10 % de la adjudicación**."))}

{unidad("1.2 Excepciones acordadas por el Gobierno (art. 47.3)",
  lit("LGP", "Artículo 47", ["El Gobierno, en casos especialmente justificados", "previo informe de la Dirección General de Presupuestos"], solo=[5]),
  fichab("Excepción a los límites del art. 47.2",
         f"{g(47, 'El Gobierno')}; eleva la propuesta {g(47, 'el Ministro de Hacienda, a iniciativa del ministerio correspondiente')}",
         ["Modificar los porcentajes", "Incrementar el número de anualidades", "Autorizar compromisos para ejercicios posteriores aunque no exista crédito inicial"],
         "Previo informe de la Dirección General de Presupuestos sobre su coherencia con la programación de los arts. 28 y 29",
         f"Solo {g(47, 'en casos especialmente justificados')} y lo acuerda el **Gobierno** (Consejo de Ministros): el Ministro de Hacienda solo **eleva la propuesta**."))}

{unidad("1.3 Escenarios, subvenciones y tramitación anticipada (art. 47.4 a 6)",
  lit("LGP", "Artículo 47", ["contabilización separada", "No podrán adquirirse compromisos de gasto con cargo a ejercicios futuros", "aun cuando su ejecución, ya sea en una o en varias anualidades, deba iniciarse en ejercicios posteriores"], solo=[6, 7, 8, 9]),
  fichab("Reglas que completan el régimen de los compromisos plurianuales",
         "—",
         ["Se especifican en los **escenarios presupuestarios plurianuales** y se contabilizan por separado (47.4)",
          f"Nunca con cargo a ejercicios futuros en las subvenciones del art. 22.2 a) de la Ley General de Subvenciones (47.5), que son {c('LGS', 'Artículo 22', 'Las previstas nominativamente en los Presupuestos Generales del Estado')}",
          "Tramitación anticipada de contratos, encargos a medios propios y convenios: puede llegar a la adjudicación y formalización aunque la ejecución empiece en ejercicios posteriores (47.6)"],
         "En la tramitación anticipada se cumplen los límites y anualidades o importes de los apartados 2 a 5",
         "La tramitación anticipada es la única salvedad a que la ejecución empiece **en el propio ejercicio**: permite **formalizar** el contrato, el encargo o el convenio. Subvenciones **nominativas**: sin compromisos para ejercicios futuros."))}
""", 2)

T.ap("s2", "I.2 Modificación y resolución de compromisos plurianuales (art. 47 bis)", f"""
Si un ejercicio posterior llega sin crédito suficiente para lo comprometido, la ley fija **qué hacer y en qué orden**.

{unidad("2.1 Falta de crédito en un ejercicio posterior (art. 47 bis)",
  lit("LGP", "Artículo 47 bis", ["no autorizase créditos suficientes", "comunicar tal circunstancia al tercero", "la reprogramación de las obligaciones asumidas por cada parte", "acordará la resolución del negocio", "valorará el presupuesto de gastos autorizado y el grado de ejecución del objeto del negocio"]),
  fichab("Qué hacer cuando la Ley de Presupuestos de un ejercicio posterior no autoriza créditos suficientes para un compromiso plurianual",
         g("47 bis", "El órgano competente para aprobar y comprometer el gasto"),
         ["::Tres pasos, por este orden:", "1.º Comunicarlo al tercero", "2.º Reprogramar las obligaciones de cada parte y reajustar anualidades, si lo permiten las disponibilidades de crédito", "3.º Si no es posible, resolver el negocio, fijando en su caso las compensaciones"],
         f"Comunicación {g('47 bis', 'tan pronto como se tenga conocimiento de ello')}",
         "Orden: **comunicar → reprogramar → resolver**; la resolución es el último paso. Si la obligación estaba **condicionada** a la existencia de crédito, antes de resolver se valoran **soluciones alternativas** y se notifica **de forma fehaciente** al tercero."))}

""", 2)

T.ap("s2b", "I.3 Inmuebles con pago aplazado y obras de abono total (art. 48)", f"""
{unidad("3.1 Adquisiciones y obras con pago aplazado (art. 48)",
  lit("LGP", "Artículo 48", ["cuyo importe exceda de seis millones de euros", "pueda ser inferior al 25 por ciento del precio", "en los cuatro ejercicios siguientes", "abono total"]),
  fichab("Compromisos plurianuales especiales: compra directa de inmuebles con pago diferido y contratos de obras de abono total",
         "—",
         ["Inmuebles adquiridos directamente por más de **seis millones de euros**: puede diferirse el vencimiento del pago del precio", "Desembolso inicial a la firma de la escritura: **no inferior al 25 %** del precio", "Resto: en los **cuatro ejercicios siguientes**, dentro de los porcentajes del art. 47 (→ I.1.1)", "Obras bajo la modalidad de **abono total**: se les aplica el procedimiento del art. 47 (48.2)"],
         "Cuatro ejercicios siguientes, con los límites porcentuales del art. 47",
         f"**Más de 6 millones**, **25 %** como mínimo a la firma y **cuatro** ejercicios. Las obras de abono total siguen el art. 47, pero sin la retención adicional del 10 %: {g(47, 'con excepción de los realizados bajo la modalidad de abono total del precio')} (47.2)."))}

{resumen([
  "Gastos plurianuales: ejecución iniciada **en el propio ejercicio**; máximo **cuatro** ejercicios; **70 / 60 / 50 / 50 %** del crédito inicial (47.1 y 2).",
  "Obras: retención adicional del **10 %** de la adjudicación; sin límites la **Deuda** y los **arrendamientos de inmuebles** (47.2).",
  "Excepciones: el **Gobierno**, en casos especialmente justificados, a propuesta del Ministro de Hacienda (47.3).",
  "Sin crédito en un ejercicio posterior: **comunicar**, **reprogramar** y, si no cabe, **resolver** (47 bis).",
  "Inmuebles de más de **6 millones**: pago diferido con **25 %** a la firma y el resto en **cuatro** ejercicios; obras de abono total: procedimiento del art. 47 (48)."],
  "Siguiente: II. ¿Qué modificaciones de los créditos iniciales hay, con qué se financian y qué es una transferencia?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Qué modificaciones de los créditos iniciales hay, con qué se financian y qué es una transferencia? (arts. 49 a 52)", donde(
  "Segunda pregunta. Los créditos valen para su ejercicio y lo no gastado se anula (art. 49); para las necesidades imprevistas, el presupuesto del Estado reserva un **Fondo de Contingencia** (art. 50). Aprobado el presupuesto, la **cuantía** y la **finalidad** de los créditos solo cambian por las vías que enumera el art. 51. La primera es la **transferencia**: mover dotación de un crédito a otro.",
  ["1 Temporalidad de los créditos y Fondo de Contingencia (arts. 49 y 50)", "2 Las cinco modificaciones de los créditos iniciales (art. 51)", "3 Transferencias de crédito: concepto, restricciones y excepciones (art. 52)"]))

T.ap("s2c", "II.1 Temporalidad de los créditos y Fondo de Contingencia (arts. 49 y 50)", f"""
{unidad("1.1 Temporalidad de los créditos (art. 49)",
  lit("LGP", "Artículo 49", ["que se realicen en el propio ejercicio presupuestario", "quedarán anulados de pleno derecho"]),
  fichab("Regla por la que los créditos de un presupuesto solo atienden gastos de su propio ejercicio",
         "—",
         ["Solo obligaciones por gastos que se realicen **en el propio ejercicio** (salvedades del art. 34.2 y 3)", "Créditos no afectados a obligaciones ya reconocidas el **último día** del ejercicio: **anulados de pleno derecho**"],
         "Último día del ejercicio presupuestario",
         "La anulación tiene una salvedad expresa: las **incorporaciones** del art. 58 (→ V.1)."))}

{unidad("1.2 Fondo de Contingencia de ejecución presupuestaria (art. 50)",
  lit("LGP", "Artículo 50", ["necesidades inaplazables, de carácter no discrecional", "por importe del dos por ciento del total de gastos para operaciones no financieras", "El Fondo únicamente financiará", "En ningún caso podrá utilizarse el Fondo", "mediante acuerdo del Consejo de Ministros", "un informe trimestral"]),
  fichab("Sección del presupuesto del Estado para necesidades inaplazables y no discrecionales sin dotación adecuada",
         ["Aplicación del Fondo: **acuerdo del Consejo de Ministros**, a propuesta del Ministro de Hacienda (el texto cita al de Economía y Hacienda), **antes** de autorizar la modificación", "Informe a las Cortes: el **Gobierno**, a través de su Oficina Presupuestaria"],
         ["::Cuantía:", "**2 %** del total de gastos para operaciones no financieras, excluidos los destinados a financiar a CC. AA. y EE. LL. por sus sistemas de financiación", "::Solo financia (salvo los casos del art. 59 → V.2):", "a) Ampliaciones (art. 54 → III.2)", "b) Créditos extraordinarios y suplementos (art. 55 → IV.1)", "c) Incorporaciones (art. 58 → V.1)"],
         "Informe **trimestral** a las Cortes",
         "**2 %** (el **1 %** es el límite de los anticipos de Tesorería, → VI.1.1). **Nunca** para gastos que deriven de **decisiones discrecionales** sin cobertura presupuestaria. Solo financia **ampliaciones, créditos extraordinarios y suplementos e incorporaciones**."))}
""", 2)

T.ap("s3", "II.2 Las modificaciones de los créditos iniciales (art. 51)", f"""
{unidad("2.1 Lista cerrada (art. 51)",
  lit("LGP", "Artículo 51", ["La cuantía y finalidad", "sólo podrán ser modificadas durante el ejercicio"]),
  fichab("Modificaciones de la cuantía y finalidad de los créditos de los presupuestos de gastos",
         "Cada figura tiene su órgano competente (→ VI.4)",
         ["::Solo mediante:", "a) Transferencias (→ II.3)", "b) Generaciones (→ III.1)", "c) Ampliaciones (→ III.2)", "d) Créditos extraordinarios y suplementos de crédito (→ IV.1)", "e) Incorporaciones (→ V.1)"],
         f"{g(51, 'durante el ejercicio')}, dentro de los límites y con el procedimiento de los artículos siguientes",
         "Cinco letras (créditos extraordinarios y suplementos van juntos en la **d**). **No** son modificaciones de crédito los **gastos plurianuales** (art. 47) ni las «redistribuciones»: lo preguntaron L 86 y P 89 (→ Cierre 1)."))}

### Cuadro de las modificaciones (esquema)

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Figura | Qué hace | Artículo |
|---|---|---|
| Transferencia | Traspasa dotaciones entre créditos (no aumenta el total) | 52 |
| Generación | Incrementa créditos por ingresos no previstos o superiores a los previstos | 53 |
| Ampliación | Incrementa un crédito **ampliable** hasta el importe de las obligaciones | 54 |
| Crédito extraordinario | Dota un gasto inaplazable para el que **no existe crédito adecuado** | 55 a 57 |
| Suplemento de crédito | Aumenta un crédito **insuficiente y no ampliable** para un gasto inaplazable | 55 a 57 |
| Incorporación | Lleva al ejercicio remanentes de crédito del **ejercicio anterior** | 58 |
""", 2)

T.ap("s4", "II.3 Transferencias de crédito (art. 52)", f"""
{unidad("3.1 Concepto y restricciones (art. 52.1)",
  lit("LGP", "Artículo 52", ["traspasos de dotaciones entre créditos", "ni desde créditos para operaciones de capital a créditos para operaciones corrientes", "entre créditos de distintas secciones presupuestarias", "No minorarán créditos extraordinarios o créditos que se hayan suplementado o ampliado en el ejercicio"], solo=[1, 2, 3, 4, 5, 6]),
  fichab(f"{g(52, 'traspasos de dotaciones entre créditos')}, {g(52, 'incluso con la creación de créditos nuevos')}",
         "Ministros, Ministro de Hacienda o Gobierno, según el caso (→ VI.4)",
         ["::Restricciones:", "a) No desde créditos para operaciones financieras al resto, ni de capital a corrientes", "b) No entre distintas secciones presupuestarias (salvo el programa de contratación centralizada)", "c) No minoran créditos extraordinarios ni créditos suplementados o ampliados en el ejercicio (salvo ampliables de la Seguridad Social y sección 06 Deuda Pública)", "d) Seguridad Social: los créditos ampliables solo se minoran para financiar otros ampliables"],
         "—",
         "La dirección prohibida es **de capital a corrientes** y **desde financieras** al resto. No se puede **minorar** lo que ya se ha **incrementado** en el ejercicio (extraordinarios, suplementados o ampliados)."))}

{unidad("3.2 Excepciones y subvenciones nominativas (art. 52.2 y 3)",
  lit("LGP", "Artículo 52", ["reorganizaciones administrativas o traspaso de competencias a comunidades autónomas", "programa de imprevistos", "En ningún caso las transferencias podrán crear créditos destinados a subvenciones nominativas"], solo=[7, 8]),
  fichab("Casos en que no rigen las restricciones del art. 52.1, y límite de las subvenciones nominativas",
         "Las transferencias entre distintas secciones por reorganizaciones administrativas las autoriza el Gobierno (→ VI.1.2)",
         ["::No se aplican las restricciones a las transferencias:", "Por reorganizaciones administrativas o traspaso de competencias a comunidades autónomas", "Derivadas de convenios o acuerdos de colaboración entre departamentos ministeriales, órganos del Estado con secciones diferenciadas u organismos autónomos", "Para cumplir la Ley 16/1985, del Patrimonio Histórico Español", "Las que se realicen desde el programa de imprevistos"],
         "—",
         f"Las transferencias **no** pueden crear ni aumentar subvenciones **nominativas**, {g(52, 'salvo que sean conformes con lo dispuesto en la Ley General de Subvenciones o se trate de subvenciones o aportaciones a otros entes del sector público')}."))}

{resumen([
  "Los créditos atienden gastos del **propio ejercicio**; lo no afectado a obligaciones se **anula** el último día, salvo incorporación (49). **Fondo de Contingencia**: **2 %** del gasto no financiero; solo financia ampliaciones, créditos extraordinarios y suplementos e incorporaciones, por acuerdo del **Consejo de Ministros** (50).",
  "La cuantía y finalidad de los créditos solo cambian por **cinco** vías: transferencias, generaciones, ampliaciones, créditos extraordinarios y suplementos, e incorporaciones (51).",
  "Transferencia = **traspaso de dotaciones entre créditos**, incluso creando créditos nuevos (52.1).",
  "Prohibido: desde **financieras** al resto, de **capital a corrientes**, entre **secciones** y minorar lo **incrementado** en el ejercicio (52.1), salvo las excepciones del 52.2.",
  "Nunca crear o aumentar **subvenciones nominativas**, con las salvedades del 52.3."],
  "Siguiente: III. ¿Cómo crecen los créditos? Generaciones y ampliaciones")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Cómo crecen los créditos por ingresos o por obligaciones? Generaciones y ampliaciones (arts. 53 y 54)", donde(
  "Tercera pregunta. Dos figuras **aumentan** créditos sin pasar por las Cortes: la **generación**, porque entran ingresos no previstos, y la **ampliación**, porque el crédito es ampliable y las obligaciones superan lo consignado.",
  ["1 Generaciones de crédito (art. 53)", "2 Créditos ampliables (art. 54)"]))

T.ap("s5", "III.1 Generaciones de crédito (art. 53)", f"""
{unidad("1.1 Concepto y supuestos (art. 53.1 y 2)",
  lit("LGP", "Artículo 53", ["ingresos no previstos o superiores a los contemplados en el presupuesto inicial", "Ventas de bienes y prestación de servicios", "Enajenaciones de inmovilizado", "Reembolsos de préstamos", "Ingresos legalmente afectados", "reintegros de pagos indebidos realizados con cargo a créditos del presupuesto corriente"], solo=[1, 2, 3, 4, 5, 6, 7, 8]),
  fichab(f"Modificaciones que {g(53, 'incrementan los créditos como consecuencia de la realización de determinados ingresos no previstos o superiores a los contemplados en el presupuesto inicial')}",
         "Según el supuesto: ministros, Ministro de Hacienda o presidentes y directores (→ VI.4)",
         ["::Ingresos realizados en el propio ejercicio por:", "a) Aportaciones para financiar conjuntamente gastos de los fines del organismo o entidad", "b) Ventas de bienes y prestación de servicios", "c) Enajenaciones de inmovilizado", "d) Reembolsos de préstamos", "e) Ingresos legalmente afectados a actuaciones determinadas", "f) Reintegros de pagos indebidos con cargo a créditos del presupuesto corriente"],
         "Ingresos del **propio ejercicio** (excepción del último trimestre del anterior: → III.1.2)",
         "**Seis** supuestos tasados. Los reintegros solo generan si el pago indebido se hizo con cargo al presupuesto **corriente**."))}

{unidad("1.2 Cuándo y en qué créditos (art. 53.3 a 5)",
  lit("LGP", "Artículo 53", ["La generación sólo podrá realizarse cuando se hayan efectuado los correspondientes ingresos que la justifican", "únicamente en aquellos créditos destinados a cubrir gastos de la misma naturaleza", "únicamente podrán dar lugar a generaciones en aquellos créditos destinados a la concesión de nuevos préstamos", "los ingresos realizados en el último trimestre del ejercicio anterior"], solo=[9, 10, 11, 12, 13]),
  fichab("Momento y destino de la generación",
         "—",
         ["Regla: cuando se hayan **efectuado** los ingresos", "Organismos autónomos y Seguridad Social, supuesto a): basta el reconocimiento del derecho o un compromiso firme de aportación, si el ingreso se prevé en el propio ejercicio", "Ventas y servicios → créditos para gastos de la misma naturaleza", "Inmovilizado → créditos de operaciones de la misma naturaleza económica", "Reembolso de préstamos → solo créditos para nuevos préstamos"],
         f"Excepcionalmente, {g(53, 'los ingresos realizados en el último trimestre del ejercicio anterior')} (53.5)",
         "El **reconocimiento del derecho** basta solo en organismos autónomos y Seguridad Social y solo en el supuesto **a)**. El reembolso de préstamos genera **solo** para conceder **nuevos préstamos**."))}
""", 2)

T.ap("s6", "III.2 Créditos ampliables (art. 54)", f"""
{unidad("2.1 Créditos ampliables del Estado (art. 54.1)",
  lit("LGP", "Artículo 54", ["Excepcionalmente", "pensiones de Clases Pasivas del Estado", "derivadas de normas con rango de ley, que de modo taxativo y debidamente explicitados se relacionen en el estado de gastos", "hasta el importe que alcancen las respectivas obligaciones", "obligaciones derivadas de la Deuda del Estado"], solo=[1, 2]),
  fichab(f"Créditos cuya cuantía {g(54, 'podrá ser incrementada')} {g(54, 'hasta el importe que alcancen las respectivas obligaciones')}",
         "Las ampliaciones del art. 54.1 las autoriza el Ministro de Hacienda (→ VI.2)",
         ["::Son ampliables:", "Los de pensiones de Clases Pasivas del Estado", "Los de obligaciones específicas del ejercicio derivadas de normas con rango de ley, relacionados taxativamente en el estado de gastos de los Presupuestos Generales del Estado", "Los de la Deuda del Estado y de sus organismos autónomos (intereses, amortizaciones y gastos de emisión, conversión, canje o amortización)"],
         "Obligaciones **del respectivo ejercicio**",
         "La condición de ampliable es **excepcional**: hace falta **norma con rango de ley** y relación **taxativa** en el estado de gastos."))}

{unidad("2.2 Créditos ampliables de la Seguridad Social (art. 54.2)",
  lit("LGP", "Artículo 54", ["En todo caso se consideran ampliables", "pensiones de todo tipo", "ingreso mínimo vital", "capitales-renta", "Fondo de Reserva de la Seguridad Social", "sistema de protección por cese de actividad"], solo=[3, 4, 5, 6, 7, 8, 9, 10, 11]),
  fichab("Créditos de los Presupuestos de la Seguridad Social que la ley considera ampliables en todo caso",
         "Autorizan las ampliaciones los presidentes y directores de las entidades de la Seguridad Social (art. 63.3 b → VI.3.2)",
         ["a) Pensiones de todo tipo, incapacidad temporal, protección a la familia, nacimiento y cuidado de menor, riesgos durante el embarazo y la lactancia, cuidado de menores con cáncer u otra enfermedad grave, ingreso mínimo vital y entregas únicas (con los requisitos de la letra a)", "b) Subsidios de garantía de ingresos mínimos, de movilidad y de ayuda de tercera persona", "c) Constitución de capitales-renta para el pago de pensiones", "d) Fondo de Reserva y Fondo de Prevención y Rehabilitación de la Seguridad Social", "e) Aportaciones de las Mutuas", "f) Recargos de prestaciones previamente ingresados", "g) Transferencias de derechos al sistema de pensiones de la Unión Europea", "h) Sistema de protección por cese de actividad"],
         f"{g(54, 'en la cuantía resultante de las obligaciones que se reconozcan y liquiden')}",
         "Pensiones de todo tipo, capitales-renta, Fondo de Reserva, cese de actividad… **son ampliables**: en la pregunta oficial P 88 (→ Cierre 1) lo que **no** se amplía es lo **previamente minorado** (→ III.2.3)."))}

{unidad("2.3 Financiación y prohibición de ampliar lo minorado (art. 54.3 y 4)",
  lit("LGP", "Artículo 54", ["con cargo al Fondo de Contingencia", "con baja en otros créditos del presupuesto no financiero", "No podrán ampliarse créditos que hayan sido previamente minorados"], solo=[12, 13, 14, 15, 16]),
  fichab("Cómo se financian las ampliaciones y qué créditos no pueden ampliarse",
         "—",
         ["Estado: Fondo de Contingencia (art. 50 → II.1.2) o baja en otros créditos del presupuesto no financiero", "Organismos autónomos: remanente de tesorería no aplicado, mayores ingresos o baja en otros créditos del presupuesto no financiero del organismo", "Seguridad Social: remanente de tesorería no aplicado, mayores ingresos o baja en otros créditos del presupuesto"],
         "—",
         f"{g(54, 'No podrán ampliarse créditos que hayan sido previamente minorados')}, {g(54, 'salvo en el ámbito de las entidades que integran el sistema de la Seguridad Social y en el de la sección 06 ' + chr(34) + 'Deuda Pública' + chr(34))} (con la condición del texto) {g(54, 'o cuando la minoración resulte de un traspaso de competencias a las Comunidades Autónomas')}."))}

{resumen([
  "Generación: **ingresos no previstos o superiores** a los previstos, en **seis** supuestos tasados, y solo cuando el ingreso se ha **efectuado** (53).",
  "Reembolso de préstamos → solo **nuevos préstamos**; excepcionalmente generan los ingresos del **último trimestre** del ejercicio anterior (53.4 y 5).",
  "Ampliables del Estado: **Clases Pasivas**, obligaciones de **normas con rango de ley** relacionadas taxativamente y **Deuda** (54.1); de la Seguridad Social, la lista del 54.2.",
  "Se financian con el **Fondo de Contingencia** o bajas en créditos no financieros; **no** se amplía lo **previamente minorado** (54.3 y 4)."],
  "Siguiente: IV. ¿Qué se hace si no hay crédito o no basta? Créditos extraordinarios y suplementos")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Qué se hace si no hay crédito o no basta? Créditos extraordinarios y suplementos (arts. 55 a 57)", donde(
  "Cuarta pregunta. Si un gasto no puede esperar al ejercicio siguiente y no hay crédito (o el que hay es insuficiente y no ampliable), y ninguna otra figura del art. 51 sirve, se tramita un **crédito extraordinario** o un **suplemento de crédito**. La ley distingue el **Estado**, los **organismos autónomos** y la **Seguridad Social**.",
  ["1 Estado: cuándo proceden, financiación y ley o Consejo de Ministros (art. 55)", "2 Organismos autónomos (art. 56)", "3 Seguridad Social (art. 57)", "4 Cuadro comparativo"]))

T.ap("s7", "IV.1 Créditos extraordinarios y suplementos de crédito del Estado (art. 55)", f"""
{unidad("1.1 Cuándo proceden y cómo se financian (art. 55.1)",
  lit("LGP", "Artículo 55", ["que no pueda demorarse hasta el ejercicio siguiente", "no exista crédito adecuado", "sea insuficiente y no ampliable el consignado", "mediante baja en los créditos del Fondo de Contingencia", "se financiará con Deuda Pública"], solo=[1, 2, 3]),
  fichab("Crédito **extraordinario** (no existe crédito adecuado) o **suplementario** (el consignado es insuficiente y no ampliable) con cargo al Presupuesto del Estado",
         "Las Cortes, por ley, o el Consejo de Ministros, según el caso (→ IV.1.2)",
         ["::Requisitos (todos):", "Gasto que no puede demorarse hasta el ejercicio siguiente", "Sin crédito adecuado, o insuficiente y no ampliable", "Dotación imposible con las demás figuras del art. 51", "Financiación: operaciones no financieras → Fondo de Contingencia u otros créditos no financieros; operaciones financieras → Deuda Pública o baja en créditos de la misma naturaleza"],
         "—",
         "Es la figura **subsidiaria**: solo si no cabe ninguna otra del art. 51. **Extraordinario** = no hay crédito adecuado; **suplemento** = hay crédito pero es insuficiente y **no ampliable**."))}

{unidad("1.2 Ley o Consejo de Ministros (art. 55.2 y 3)",
  lit("LGP", "Artículo 55", ["la remisión de un proyecto de ley a las Cortes Generales", "dictamen del Consejo de Estado", "El Consejo de Ministros autorizará", "cuando se financien con cargo al Fondo de Contingencia"], solo=[4, 5, 6, 7, 8]),
  fichab("Quién concede los créditos extraordinarios y suplementos del Estado",
         ["**Cortes Generales**, por ley: el Ministro de Hacienda propone al Consejo de Ministros la remisión del proyecto, previo informe de la Dirección General de Presupuestos y dictamen del Consejo de Estado", "**Consejo de Ministros**: los financiados con el Fondo de Contingencia (55.3; art. 61 d → VI.1.2)"],
         ["::Van a proyecto de ley:", "a) Obligaciones de ejercicios anteriores sin crédito anulado en el de procedencia (se financien con Fondo de Contingencia o con baja)", "b) Obligaciones del propio ejercicio financiadas con baja en otros créditos", "c) Los que afecten a operaciones financieras"],
         "—",
         "La llave es la **financiación**: **Fondo de Contingencia → Consejo de Ministros**; **baja en otros créditos → ley**. Excepción: obligaciones de ejercicios anteriores **sin crédito anulado** → **ley** aunque se financien con el Fondo."))}
""", 2)

T.ap("s8", "IV.2 Créditos extraordinarios y suplementarios de los organismos autónomos (art. 56)", f"""
{unidad("2.1 Financiación (art. 56.1 y 2)",
  lit("LGP", "Artículo 56", ["únicamente podrá realizarse con cargo a la parte del remanente de tesorería al fin del ejercicio anterior que no haya sido aplicada", "con mayores ingresos sobre los previstos inicialmente", "se acordarán conjuntamente"], solo=[1, 2, 3]),
  fichab("Créditos extraordinarios y suplementos en el presupuesto de un organismo autónomo",
         "—",
         ["::Solo dos fuentes:", "Remanente de tesorería del ejercicio anterior no aplicado en el presupuesto del organismo", "Mayores ingresos sobre los previstos inicialmente"],
         "—",
         "Sin Fondo de Contingencia ni baja en otros créditos: «**únicamente**» remanente o mayores ingresos. Si hace falta modificar también el presupuesto del Estado, ambas modificaciones se acuerdan **conjuntamente** por el procedimiento del Estado."))}

{unidad("2.2 Competencia (art. 56.3 a 5)",
  lit("LGP", "Artículo 56", ["hasta un importe del 10 % del correspondiente capítulo de su presupuesto inicial de gastos, cuando no supere la cuantía de 500.000 euros", "no se alcance el 20 % del correspondiente capítulo de su presupuesto inicial de gastos ni se supere la cuantía de 1.000.000 de euros", "Al Consejo de Ministros en los restantes casos", "No se computarán para la determinación de dichos límites las modificaciones que se financien con incremento en la aportación del Estado"], solo=[4, 5, 6, 7, 8, 9, 10]),
  fichab("Quién autoriza los créditos extraordinarios y suplementos de los organismos autónomos",
         ["**Presidente o Director**: hasta el **10 %** del capítulo y sin superar **500.000 euros** (excluidos gastos de personal y créditos del art. 44.2), dando cuenta a su Ministro y al de Hacienda", "**Ministro de Hacienda**: superado alguno de esos límites, sin llegar al **20 %** ni superar **1.000.000 de euros**; también los excluidos, dentro de esos límites", "**Consejo de Ministros**: los restantes casos"],
         "Los límites se refieren al conjunto de las modificaciones del ejercicio, computadas por separado para gastos de personal y créditos del art. 44.2 y para el resto",
         "Capítulo que no existe en el presupuesto inicial (56.5): Presidente o Director hasta 500.000 euros; Ministro hasta 1.000.000; Consejo de Ministros, el resto",
         "**10 % y 500.000 €** → Presidente o Director; **20 % y 1.000.000 €** → Ministro de Hacienda; el resto → Consejo de Ministros. Cayó en 2025 (L 87, → Cierre 1). No computan las financiadas con **incremento de la aportación del Estado**."))}

{unidad("2.3 Informe a las Cortes y obligaciones de ejercicios anteriores (art. 56.6 y 7)",
  lit("LGP", "Artículo 56", ["un informe trimestral", "se remitirá un proyecto de Ley a las Cortes Generales"], solo=[11, 12]),
  fichab("Control de las Cortes y casos que exigen ley",
         "Ministro de Hacienda (informe); Cortes Generales (ley)",
         ["Informe a las Cortes, a través de su Oficina Presupuestaria, de los créditos tramitados por este artículo", "Obligaciones de ejercicios anteriores sin crédito anulado en el de procedencia → proyecto de ley, con el procedimiento del art. 55"],
         "Informe **trimestral**",
         "Igual que en el Estado: obligaciones de ejercicios anteriores **sin crédito anulado** → **ley**."))}
""", 2)

T.ap("s9", "IV.3 Créditos extraordinarios y suplementos de crédito de la Seguridad Social (art. 57)", f"""
{unidad("3.1 Financiación y competencia (art. 57.1 a 3)",
  lit("LGP", "Artículo 57", ["con mayores ingresos sobre los previstos inicialmente", "al Gobierno cuando su importe sea superior al dos por ciento del presupuesto inicial de gastos de la respectiva Entidad", "no será preceptivo el informe del Ministerio de Economía y Hacienda"], solo=[1, 2, 3, 4, 5]),
  fichab("Créditos extraordinarios y suplementos en las entidades de la Seguridad Social",
         ["**Gobierno**: importe superior al **2 %** del presupuesto inicial de gastos de la entidad", "**Ministro** (el texto cita al de Trabajo y Asuntos Sociales y, para el Instituto Nacional de Gestión Sanitaria, al de Sanidad y Consumo): hasta ese porcentaje", "Previo informe del Ministerio de Economía y Hacienda, salvo en las Mutuas (se le da cuenta después)"],
         "Remanente de tesorería no aplicado o mayores ingresos; si proceden de mayores aportaciones del Estado, basta el reconocimiento del derecho por la entidad",
         "Límite del **2 %** del presupuesto inicial de gastos de la entidad, referido al conjunto de las modificaciones del ejercicio (sin contar las financiadas con más aportación del Estado)",
         "En la Seguridad Social el límite es un **porcentaje (2 %) del presupuesto de la entidad**, sin cuantía en euros; en los organismos autónomos son **10 % / 20 % del capítulo** y **500.000 / 1.000.000 €** (→ IV.2.2)."))}

{unidad("3.2 Informe a las Cortes y obligaciones de ejercicios anteriores (art. 57.4 y 5)",
  lit("LGP", "Artículo 57", ["un informe trimestral", "propondrá al Consejo de Ministros la remisión de un proyecto de ley a las Cortes Generales"], solo=[6, 7]),
  fichab("Control de las Cortes y casos que exigen ley en la Seguridad Social",
         "El Ministro competente (informe y propuesta); Cortes Generales (ley)",
         ["Informe a las Cortes, a través de su Oficina Presupuestaria", "Obligaciones de ejercicios anteriores sin crédito anulado → proyecto de ley, previo informe de la Dirección General de Presupuestos y dictamen del Consejo de Estado"],
         "Informe **trimestral**",
         "Mismo esquema que el Estado y los organismos autónomos: lo de ejercicios anteriores **sin crédito anulado** va a **ley**."))}
""", 2)

T.ap("s10", "IV.4 Cuadro comparativo: Estado, organismos autónomos y Seguridad Social (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| | Estado (art. 55) | Organismos autónomos (art. 56) | Seguridad Social (art. 57) |
|---|---|---|---|
| Financiación | Fondo de Contingencia u otros no financieros; en operaciones financieras, Deuda Pública o baja | **Solo** remanente de tesorería no aplicado o mayores ingresos | **Solo** remanente de tesorería no aplicado o mayores ingresos |
| Autoriza sin ley | Consejo de Ministros, si se financia con el **Fondo de Contingencia** | Presidente o Director (**10 %** y **500.000 €**); Ministro de Hacienda (**20 %** y **1.000.000 €**); Consejo de Ministros | Ministro (hasta el **2 %**); Gobierno (más del **2 %**) |
| Exige ley | Ejercicios anteriores sin crédito anulado; baja en otros créditos; operaciones financieras | Ejercicios anteriores sin crédito anulado | Ejercicios anteriores sin crédito anulado |
| Informe a las Cortes | — | Trimestral | Trimestral |

{resumen([
  "Crédito **extraordinario**: no hay crédito adecuado; **suplemento**: el crédito es insuficiente y **no ampliable**; en los dos casos, gasto que **no puede demorarse** y sin otra figura posible (55.1).",
  "Estado: **Fondo de Contingencia → Consejo de Ministros**; **baja en otros créditos**, operaciones **financieras** u obligaciones anteriores sin crédito anulado → **ley**, con dictamen del **Consejo de Estado** (55.2 y 3).",
  "Organismos autónomos: **10 % / 500.000 €** (Presidente o Director), **20 % / 1.000.000 €** (Ministro de Hacienda), resto **Consejo de Ministros** (56.3).",
  "Seguridad Social: **Gobierno** si supera el **2 %** del presupuesto inicial de la entidad; si no, el **Ministro** (57.2)."],
  "Siguiente: V. ¿Cómo pasan los remanentes al ejercicio siguiente? Las incorporaciones")}
""", 2)

# =============================================================================
T.ap("bV", "V. ¿Cómo pasan los remanentes al ejercicio siguiente? Incorporaciones (arts. 58 y 59)", donde(
  f"Quinta pregunta. Los créditos no comprometidos al cerrar el ejercicio {c('LGP', 'Artículo 49', 'quedarán anulados de pleno derecho, sin perjuicio de lo establecido en el artículo 58 de esta ley')} (art. 49.2, → II.1.1). La **incorporación** es esa salvedad: lleva remanentes del ejercicio anterior al corriente.",
  ["1 Incorporaciones de crédito: supuestos y financiación (art. 58)", "2 Modificaciones excluidas de las reglas de financiación (art. 59)"]))

T.ap("s11", "V.1 Incorporaciones de crédito (art. 58)", f"""
{unidad("1.1 Supuestos (art. 58, primer párrafo)",
  lit("LGP", "Artículo 58", ["No obstante lo dispuesto en el artículo 49", "los remanentes de crédito del ejercicio anterior", "Cuando así lo disponga una norma de rango legal", "en sus párrafos a) y e)", "en el último mes del ejercicio presupuestario anterior"], solo=[1, 2, 3, 4, 5]),
  fichab("Incorporación a los créditos de un ejercicio de los remanentes de crédito del ejercicio anterior",
         "El Ministro de Hacienda (art. 62.1 c → VI.2)",
         ["::Solo en cuatro casos:", "a) Cuando lo disponga una norma de rango legal", "b) Remanentes de las generaciones del art. 53.2 a) y e)", "c) Retenciones para financiar créditos extraordinarios o suplementos cuyo pago se anticipó y cuyas leyes de concesión quedaron pendientes de aprobación al final del ejercicio", "d) Créditos extraordinarios y suplementos concedidos por norma con rango de ley en el último mes del ejercicio anterior"],
         "Remanentes del **ejercicio anterior**; en la letra d), concedidos en el **último mes** de ese ejercicio",
         "De las generaciones solo se incorporan las de los párrafos **a) y e)** (aportaciones para financiar conjuntamente e ingresos legalmente afectados). Último **mes**, no último trimestre (el trimestre es de las generaciones, 53.5)."))}

{unidad("1.2 Financiación (art. 58, párrafos finales)",
  lit("LGP", "Artículo 58", ["mediante baja en el Fondo de Contingencia", "únicamente podrán realizarse con cargo a la parte del remanente de tesorería"], solo=[6, 7, 8]),
  fichab("Cómo se financian las incorporaciones",
         "—",
         ["Estado: baja en el Fondo de Contingencia (art. 50) o en otros créditos de operaciones no financieras", "Organismos autónomos y entidades de la Seguridad Social: únicamente remanente de tesorería no aplicado", "Seguridad Social: pueden incorporarse los remanentes de créditos extraordinarios y suplementos autorizados en el último mes del ejercicio anterior"],
         "—",
         "Organismos autónomos y Seguridad Social: **solo remanente de tesorería** (no mayores ingresos, a diferencia de los créditos extraordinarios del art. 56.2)."))}
""", 2)

T.ap("s12", "V.2 Modificaciones excluidas de las reglas de financiación (art. 59)", f"""
{unidad("2.1 Exclusión de la aplicación al Fondo de Contingencia (art. 59)",
  lit("LGP", "Artículo 59", ["al pago de la Deuda Pública", "no reduzcan la capacidad de financiación del Estado en el ejercicio", "con excepción de los créditos extraordinarios y suplementos de crédito a que se refiere el artículo 58.c) anterior"]),
  fichab("Modificaciones cuya financiación no se rige por los arts. 50, 54 y 58",
         "—",
         ["Las relativas al pago de la Deuda Pública", "Las que afectan a créditos para financiar a Comunidades Autónomas y Entidades Locales según sus sistemas de financiación", "Las que no reducen la capacidad de financiación del Estado en el ejercicio (art. 27 de la Ley Orgánica 2/2012)"],
         "—",
         "Excepción dentro de la excepción: sí se aplican las reglas a los créditos extraordinarios y suplementos del **art. 58 c)**."))}

{resumen([
  "Los créditos no afectados a obligaciones reconocidas se **anulan** al final del ejercicio, salvo lo que se **incorpora** (arts. 49.2 y 58).",
  "Cuatro supuestos de incorporación: **norma con rango legal**; generaciones **53.2 a) y e)**; retenciones del **58 c)**; créditos extraordinarios y suplementos concedidos por ley en el **último mes** (58).",
  "Financiación: Estado, **Fondo de Contingencia** o bajas en créditos no financieros; organismos autónomos y Seguridad Social, **solo remanente de tesorería** (58).",
  "Deuda Pública, financiación de CC. AA. y EE. LL. y modificaciones que no reducen la capacidad de financiación quedan fuera de esas reglas (59)."],
  "Siguiente: VI. ¿Quién autoriza cada modificación?")}
""", 2)

# =============================================================================
T.ap("bVI", "VI. ¿Quién autoriza cada modificación? (arts. 60 a 63)", donde(
  "Sexta pregunta. La LGP reparte la competencia en escalera: **Gobierno** (arts. 60 y 61), **Ministro de Hacienda** (art. 62) y **ministros, presidentes y directores** (art. 63). Es lo que más se pregunta en este tema.",
  ["1 El Gobierno: anticipos de Tesorería (art. 60) y modificaciones reservadas (art. 61)", "2 El Ministro de Hacienda (art. 62)", "3 Ministros, presidentes y directores (art. 63)", "4 Cuadro de competencias"]))

T.ap("s13", "VI.1 El Gobierno: anticipos de Tesorería y competencias (arts. 60 y 61)", f"""
{unidad("1.1 Anticipos de Tesorería (art. 60)",
  lit("LGP", "Artículo 60", ["Con carácter excepcional", "el límite máximo en cada ejercicio del uno por ciento de los créditos autorizados al Estado", "hubiera dictaminado favorablemente el Consejo de Estado", "se hubiera promulgado una ley", "dispondrá la cancelación del anticipo de Tesorería"]),
  fichab("Anticipo de fondos para gastos inaplazables mientras se tramita un crédito extraordinario o un suplemento",
         g(60, "el Gobierno, a propuesta del Ministro de Economía"),
         ["a) Iniciado el expediente de crédito extraordinario o suplemento, con dictamen favorable del Consejo de Estado", "b) Promulgada una ley que establezca obligaciones que exijan crédito extraordinario o suplemento", "Si financia necesidades de un organismo autónomo, autoriza a pagarlas mediante operaciones de Tesorería"],
         "Máximo en cada ejercicio: **1 %** de los créditos autorizados al Estado por la Ley de Presupuestos Generales del Estado",
         f"**1 %**, no 2 % (el Fondo de Contingencia es {c('LGP', 'Artículo 50', 'por importe del dos por ciento del total de gastos para operaciones no financieras')}, → II.1.2). Si las Cortes no aprueban la ley, el Gobierno cancela el anticipo con cargo a los créditos {g(60, 'cuya minoración ocasione menos trastornos para el servicio público')}."))}

{unidad("1.2 Modificaciones reservadas al Gobierno (art. 61)",
  lit("LGP", "Artículo 61", ["a propuesta del Ministro de Hacienda y a iniciativa de los ministros afectados", "entre distintas secciones presupuestarias como consecuencia de reorganizaciones administrativas"]),
  fichab("Modificaciones que solo puede autorizar el Gobierno",
         f"{g(61, 'Corresponde al Gobierno')}, {g(61, 'a propuesta del Ministro de Hacienda y a iniciativa de los ministros afectados')}",
         ["a) Transferencias entre distintas secciones por reorganizaciones administrativas (→ II.3.2)", "b) Créditos extraordinarios y suplementos de organismos autónomos del art. 56.3 c), los «restantes casos» (→ IV.2.2)", "c) Créditos extraordinarios y suplementos de la Seguridad Social reservados al Gobierno por el art. 57.2, más del 2 % (→ IV.3.1)", "d) Créditos extraordinarios y suplementarios del art. 55.3, financiados con el Fondo de Contingencia (→ IV.1.2)"],
         "—",
         "Transferencias **entre secciones** → solo por **reorganizaciones administrativas** y las autoriza el **Gobierno**."))}
""", 2)

T.ap("s14", "VI.2 El Ministro de Hacienda (art. 62)", f"""
{unidad("2.1 Competencias del Ministro de Hacienda (art. 62)",
  lit("LGP", "Artículo 62", ["Las incorporaciones de remanentes reguladas en el artículo 58", "Las ampliaciones de crédito previstas en el artículo 54.1", "cuando exista informe negativo de la Intervención Delegada"]),
  fichab("Modificaciones que autoriza el Ministro de Hacienda",
         g(62, "Corresponde al Ministro de Hacienda"),
         ["a) Transferencias no reservadas al Consejo de Ministros que no puedan acordar los ministros (art. 63)", "b) Generaciones del art. 53.2 c) y, en el Presupuesto del Estado, las de los párrafos b) y e)", "c) Incorporaciones del art. 58", "d) Ampliaciones del art. 54.1 (salvo las de las entidades de la Seguridad Social, art. 63.3)", "e) Créditos extraordinarios y suplementos de organismos autónomos del art. 56.3 b)", "Además: acordar o denegar las modificaciones de ministros y organismos autónomos remitidas en discrepancia por informe negativo de la Intervención Delegada (62.2)"],
         "—",
         "**Incorporaciones** y **ampliaciones del 54.1** → **Ministro de Hacienda**. Resuelve las **discrepancias** con la Intervención Delegada en las modificaciones de los ministros."))}
""", 2)

T.ap("s15", "VI.3 Ministros, presidentes y directores (art. 63)", f"""
{unidad("3.1 Ministros y órganos con sección propia (art. 63.1)",
  lit("LGP", "Artículo 63", ["previo informe favorable de la Intervención Delegada", "Transferencias entre créditos de un mismo programa o entre programas de un mismo servicio", "en los párrafos a), d) y f) del apartado 2 del artículo 53"], solo=[1, 2, 3, 4, 5]),
  fichab("Modificaciones que autorizan los titulares de los ministerios",
         ["Los titulares de los ministerios", "Los presidentes de los órganos del Estado con secciones diferenciadas, en su presupuesto (sin perjuicio de la autonomía presupuestaria de las Cortes)", "Para el Presupuesto de la Seguridad Social, el Ministro que cita el texto ejerce las competencias que el art. 62 da al de Hacienda, con las salvedades del párrafo"],
         ["a) Transferencias dentro de un mismo programa o entre programas de un mismo servicio, incluso creando créditos nuevos de bienes corrientes y servicios o inversiones reales previstos en la clasificación económica, sin afectar a personal ni incrementar los créditos del art. 43.2", "b) Generaciones del art. 53.2 a), d) y f), aunque los ingresos sean del último trimestre del ejercicio anterior"],
         "Previo informe **favorable** de la Intervención Delegada",
         "Ministro: transferencias **dentro del programa o entre programas del mismo servicio** y generaciones **a), d) y f)**. Los presidentes de los **Órganos Constitucionales** no tienen el límite de gastos de personal de la letra a)."))}

{unidad("3.2 Organismos autónomos, Seguridad Social y comunicación a Presupuestos (art. 63.2 a 4)",
  lit("LGP", "Artículo 63", ["quienes podrán avocarlas en todo o en parte", "Las ampliaciones del artículo 54", "a la Dirección General de Presupuestos del Ministerio de Hacienda para instrumentar su ejecución"], solo=[6, 7, 8, 9, 10, 11, 12, 13]),
  fichab("Modificaciones que autorizan presidentes y directores de organismos y entidades",
         ["Presidentes y directores de los organismos autónomos y entidades del art. 3.1: las del art. 56, las generaciones del 53.2 b) y e) y las de los ministros en su presupuesto (avocables por el Ministro)", "Presidentes y directores de las entidades de la Seguridad Social: generaciones (salvo 53.2 c), ampliaciones del art. 54 y transferencias del 63.3 c)"],
         ["Las competencias de las entidades de la Seguridad Social son avocables por el Ministro que cita el texto", "Transferencias que pasan de la modalidad contributiva a la no contributiva y universal: informe favorable del Ministerio de Hacienda"],
         "Autorizadas, los acuerdos que afectan al presupuesto del Estado o de sus organismos se remiten a la Dirección General de Presupuestos",
         "En la Seguridad Social, las **ampliaciones** (todas las del art. 54) las autorizan sus **presidentes y directores**; en el Estado, las del 54.1, el **Ministro de Hacienda**."))}
""", 2)

T.ap("s16", "VI.4 Cuadro de competencias (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Modificación | Ministros / presidentes y directores (arts. 56, 57 y 63) | Ministro de Hacienda (art. 62) | Gobierno / Consejo de Ministros (arts. 55, 56, 57 y 61) | Cortes (ley) |
|---|---|---|---|---|
| Transferencias | Mismo programa o programas de un mismo servicio | Las no reservadas al Consejo de Ministros que no puedan acordar los ministros | Entre secciones por reorganizaciones administrativas | — |
| Generaciones | Ministros: 53.2 a), d) y f); organismos autónomos: b) y e); Seguridad Social: todas salvo c) | 53.2 c); en el Estado, b) y e) | — | — |
| Ampliaciones | Seguridad Social: las del art. 54 | Las del 54.1 | — | — |
| Créditos extraordinarios y suplementos | Organismos autónomos: Presidente o Director (10 % y 500.000 €); Seguridad Social: Ministro (hasta 2 %) | Organismos autónomos: hasta 20 % y 1.000.000 € | Estado: con Fondo de Contingencia; organismos autónomos: resto; Seguridad Social: más del 2 % | Estado: baja en otros créditos, operaciones financieras y obligaciones anteriores sin crédito anulado |
| Incorporaciones | — | Las del art. 58 | — | — |
| Anticipos de Tesorería | — | — | Gobierno, hasta el 1 % (art. 60) | — |

{resumen([
  "**Gobierno**: anticipos de Tesorería (**1 %**), transferencias **entre secciones** por reorganización, créditos extraordinarios del Estado con **Fondo de Contingencia**, de OO. AA. por encima de los límites y de la Seguridad Social por encima del **2 %** (60 y 61).",
  "**Ministro de Hacienda**: **incorporaciones**, **ampliaciones del 54.1**, transferencias que no pueden acordar los ministros, generaciones 53.2 c) y discrepancias con la Intervención (62).",
  "**Ministros**: transferencias **dentro del programa o del servicio** y generaciones **a), d) y f)**, previo informe **favorable** de la Intervención Delegada (63.1).",
  "**Presidentes y directores**: en OO. AA., las del art. 56 y generaciones b) y e); en la Seguridad Social, generaciones, **ampliaciones** y ciertas transferencias (63.2 y 3)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX = [
 ("L", 86, "Qué no es modificación presupuestaria (→ II.2.1)", {
   "a": f"Sí es modificación: art. 51 {g(51, 'c) Ampliaciones')}.",
   "b": f"Sí es modificación: art. 51 {g(51, 'd) Créditos extraordinarios y suplementos de crédito')}.",
   "c": f"El gasto plurianual no está en la lista cerrada del art. 51: es un compromiso de gasto que se extiende a ejercicios posteriores (art. 47, {g(47, 'Compromisos de gasto de carácter plurianual')}).",
   "d": f"Sí es modificación: art. 51 {g(51, 'e) Incorporaciones')}."},
  [("plurianual", "LGP", "Artículo 47", "Compromisos de gasto de carácter plurianual")]),
 ("L", 87, "Créditos extraordinarios de los organismos autónomos (→ IV.2.2)", {
   "a": f"Cambia la cuantía: el Presidente o Director llega {g(56, 'cuando no supere la cuantía de 500.000 euros')}; el 1.000.000 de euros es el tope del Ministro de Hacienda (56.3 b).",
   "b": f"Cambia el porcentaje: es {g(56, 'hasta un importe del 10 % del correspondiente capítulo')}, no el 50 %.",
   "c": f"Literal del art. 56.3 a): {g(56, 'A los Presidentes o Directores de los organismos hasta un importe del 10 % del correspondiente capítulo de su presupuesto inicial de gastos, cuando no supere la cuantía de 500.000 euros')}.",
   "d": f"Cambia el porcentaje y la cuantía: ni 25 % ni un millón; el Ministro de Hacienda actúa cuando {g(56, 'no se alcance el 20 % del correspondiente capítulo de su presupuesto inicial de gastos ni se supere la cuantía de 1.000.000 de euros')}."},
  [("10 %", "LGP", "Artículo 56", "hasta un importe del 10 % del correspondiente capítulo"), ("500.000 euros", "LGP", "Artículo 56", "cuando no supere la cuantía de 500.000 euros")]),
 ("P", 88, "Créditos que no pueden ampliarse (→ III.2.3)", {
   "a": f"Son ampliables en todo caso (54.2 c): {g(54, 'Los que amparan la constitución de capitales-renta para el pago de pensiones')}.",
   "b": f"Son ampliables en todo caso (54.2 h): {g(54, 'Los destinados al sistema de protección por cese de actividad')}.",
   "c": f"Literal del art. 54.4: {g(54, 'No podrán ampliarse créditos que hayan sido previamente minorados')}.",
   "d": f"Son ampliables en todo caso (54.2 a): {g(54, 'Los destinados al pago de pensiones de todo tipo')}."},
  [("previamente minorados", "LGP", "Artículo 54", "No podrán ampliarse créditos que hayan sido previamente minorados")]),
 ("P", 89, "Qué no es modificación de los créditos iniciales (→ II.2.1)", {
   "a": f"Sí es modificación: art. 51 {g(51, 'a) Transferencias')}.",
   "b": f"Sí es modificación: art. 51 {g(51, 'b) Generaciones')}.",
   "c": f"Sí es modificación: art. 51 {g(51, 'e) Incorporaciones')}.",
   "d": f"Las «redistribuciones» no figuran en el art. 51, que es una lista cerrada: los créditos {g(51, 'sólo podrán ser modificadas durante el ejercicio')} mediante transferencias, generaciones, ampliaciones, créditos extraordinarios y suplementos, e incorporaciones."},
  [("redistribuciones", "LGP", "Artículo 51", "sólo podrán ser modificadas durante el ejercicio, dentro de los límites y con arreglo al procedimiento establecido en los artículos siguientes, mediante")]),
]
bloques = []
for cod, n, tit, por, ap_ in EX:
    bloques += [f"### {'GACE-L' if cod == 'L' else 'GACE-P'} 2025, pregunta {n} · {tit}", examen(cod, n, por, ap_)]
T.ap("s17", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join(
  ["En los primeros ejercicios de **2025** cayeron **cuatro** preguntas de este tema (dos sobre la lista de modificaciones del art. 51, una sobre los créditos ampliables y una sobre la competencia en los organismos autónomos). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal."]
  + bloques + ["### Cómo se pregunta", "!> Dos patrones: «¿cuál **no** es…?», con una figura que **no** está en la lista cerrada del art. 51 (gasto plurianual, redistribución) o que la ley **excluye** (crédito previamente minorado); y la **escalera de competencias**, cambiando un **porcentaje** o una **cuantía** (10 % / 20 %, 500.000 / 1.000.000 €)."]))

T.ap("s18", "Cierre 2. Repaso en 10 minutos (por bloques)", """
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Gastos plurianuales | Ejecución iniciada en el ejercicio; límites del art. 47.2; excepciones del Gobierno; art. 47 bis; inmuebles y obras de abono total (art. 48) | **4** ejercicios; **70 / 60 / 50 / 50 %**; obras: retención del **10 %**; inmuebles: más de **6 millones** y **25 %** a la firma |
| II. Modificaciones y transferencias | Temporalidad (art. 49); Fondo de Contingencia (art. 50); lista cerrada del art. 51; transferencias y sus restricciones (art. 52) | Fondo de Contingencia: **2 %**; **cinco** figuras; no de **capital a corrientes** ni entre **secciones** |
| III. Generaciones y ampliaciones | Seis supuestos de generación; créditos ampliables del Estado y de la Seguridad Social | Reembolso de préstamos → **nuevos préstamos**; **no** se amplía lo **previamente minorado** |
| IV. Créditos extraordinarios y suplementos | Requisitos y financiación; Estado, OO. AA. y Seguridad Social | **Fondo de Contingencia → Consejo de Ministros**; OO. AA.: **10 % / 500.000 €** y **20 % / 1.000.000 €**; Seguridad Social: **2 %** |
| V. Incorporaciones | Cuatro supuestos; financiación (art. 58); exclusiones (art. 59) | Generaciones **a) y e)**; ley en el **último mes** |
| VI. Competencias | Gobierno (60 y 61), Ministro de Hacienda (62), ministros y presidentes (63) | Anticipos de Tesorería: **1 %**; incorporaciones: **Ministro de Hacienda** |

?> **Trampas frecuentes:** «el gasto plurianual es una modificación de crédito» (no está en el art. 51); «cinco ejercicios» o «80 % el primer año» (son **cuatro** y **70 %**); «transferencias de corrientes a capital prohibidas» (lo prohibido es **de capital a corrientes**); «el Presidente del organismo hasta 1.000.000 €» (son **500.000 €**; el millón es del Ministro de Hacienda); «anticipos de Tesorería hasta el 2 %» (es el **1 %**; el 2 % es el Fondo de Contingencia); «se incorporan los créditos extraordinarios del último trimestre» (es el **último mes**).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
Q = [
 ("Artículo 47", "Gastos plurianuales", "Según el artículo 47.1 de la Ley General Presupuestaria, podrán adquirirse compromisos de gastos que hayan de extenderse a ejercicios posteriores a aquel en que se autoricen, siempre que:",
  ["Su ejecución se inicie en el propio ejercicio y no superen los límites y anualidades fijados.", "Su ejecución se inicie en el ejercicio siguiente.", "Exista informe favorable del Consejo de Estado.", "Se financien con cargo al Fondo de Contingencia."], "Art. 47.1 LGP.", "siempre que su ejecución se inicie en el propio ejercicio y que no superen los límites y anualidades fijados"),
 ("Artículo 47", "Gastos plurianuales", "Según el artículo 47.2 de la Ley General Presupuestaria, el número de ejercicios a que pueden aplicarse los gastos plurianuales no será superior a:",
  ["Cuatro.", "Tres.", "Cinco.", "Seis."], "Art. 47.2 LGP.", "El número de ejercicios a que pueden aplicarse los gastos no será superior a cuatro"),
 ("Artículo 47", "Gastos plurianuales", "Según el artículo 47.2 de la Ley General Presupuestaria, el gasto que se impute al ejercicio inmediato siguiente no podrá exceder de la cantidad que resulte de aplicar al crédito inicial el:",
  ["70 por ciento.", "60 por ciento.", "50 por ciento.", "80 por ciento."], "Art. 47.2 LGP: 70 % el inmediato siguiente, 60 % el segundo y 50 % el tercero y el cuarto.", "en el ejercicio inmediato siguiente, el 70 por ciento"),
 ("Artículo 47", "Gastos plurianuales", "Según el artículo 47.2 de la Ley General Presupuestaria, en los ejercicios tercero y cuarto el porcentaje aplicable al crédito inicial es el:",
  ["50 por ciento.", "60 por ciento.", "70 por ciento.", "40 por ciento."], "Art. 47.2 LGP.", "y en los ejercicios tercero y cuarto, el 50 por ciento"),
 ("Artículo 47", "Gastos plurianuales", "Según el artículo 47.2 de la Ley General Presupuestaria, en los contratos de obra de carácter plurianual (salvo los de abono total del precio) se efectuará una retención adicional de crédito:",
  ["Del 10 por ciento del importe de adjudicación, en el momento en que ésta se realice.", "Del 10 por ciento del presupuesto de licitación, al aprobarse el expediente.", "Del 5 por ciento del importe de adjudicación, al formalizarse el contrato.", "Del 20 por ciento del importe de adjudicación, en el último ejercicio."], "Art. 47.2 LGP.", "se efectuará una retención adicional de crédito del 10 por ciento del importe de adjudicación, en el momento en que ésta se realice"),
 ("Artículo 47", "Gastos plurianuales", "Según el artículo 47.2 de la Ley General Presupuestaria, las limitaciones de anualidades y porcentajes NO son de aplicación a los compromisos derivados de:",
  ["La carga financiera de la Deuda y los arrendamientos de inmuebles.", "Los contratos de obra de carácter plurianual.", "Las subvenciones de concurrencia competitiva.", "Los encargos a medios propios."], "Art. 47.2 LGP.", "Estas limitaciones no serán de aplicación a los compromisos derivados de la carga financiera de la Deuda y de los arrendamientos de inmuebles"),
 ("Artículo 47", "Gastos plurianuales", "Según el artículo 47.3 de la Ley General Presupuestaria, en casos especialmente justificados podrá acordar la modificación de los porcentajes o incrementar el número de anualidades:",
  ["El Gobierno.", "El Ministro de Hacienda.", "La Dirección General de Presupuestos.", "El titular del ministerio correspondiente."], "Art. 47.3 LGP: el Gobierno; el Ministro de Hacienda eleva la propuesta.", "El Gobierno, en casos especialmente justificados, podrá acordar la modificación de los porcentajes anteriores"),
 ("Artículo 47", "Gastos plurianuales", "Según el artículo 47.5 de la Ley General Presupuestaria, no podrán adquirirse compromisos de gasto con cargo a ejercicios futuros cuando se trate de:",
  ["Subvenciones a las que resulte de aplicación el artículo 22.2.a) de la Ley General de Subvenciones.", "Contratos de obra.", "Arrendamientos de inmuebles.", "Convenios."], "Art. 47.5 LGP (subvenciones nominativas).", "No podrán adquirirse compromisos de gasto con cargo a ejercicios futuros cuando se trate de la concesión de subvenciones a las que resulte de aplicación lo dispuesto en el artículo 22.2.a)"),
 ("Artículo 47 bis", "Gastos plurianuales", "Según el artículo 47 bis de la Ley General Presupuestaria, si la Ley de Presupuestos de un ejercicio posterior no autoriza créditos suficientes para un compromiso plurianual, el órgano competente deberá en primer lugar:",
  ["Comunicar tal circunstancia al tercero, tan pronto como se tenga conocimiento de ello.", "Acordar la resolución del negocio.", "Solicitar un crédito extraordinario.", "Suspender la ejecución hasta el ejercicio siguiente."], "Art. 47 bis, 1.º LGP.", "estará obligado a comunicar tal circunstancia al tercero, tan pronto como se tenga conocimiento de ello"),
 ("Artículo 47 bis", "Gastos plurianuales", "Según el artículo 47 bis de la Ley General Presupuestaria, cuando no resulte posible la reprogramación de las obligaciones, el órgano competente:",
  ["Acordará la resolución del negocio, fijando las compensaciones que, en su caso, procedan.", "Solicitará un anticipo de Tesorería.", "Mantendrá las obligaciones sin crédito hasta el ejercicio siguiente.", "Remitirá un proyecto de ley a las Cortes Generales."], "Art. 47 bis, 3.º LGP.", "el órgano competente acordará la resolución del negocio siguiendo el procedimiento establecido en las correspondientes normas, y fijando las compensaciones que, en su caso, procedan"),
 ("Artículo 48", "Gastos plurianuales", "Según el artículo 48.1 de la Ley General Presupuestaria, podrá ser diferido el vencimiento de la obligación de pago del precio de compra de bienes inmuebles adquiridos directamente cuyo importe exceda de:",
  ["Seis millones de euros, sin que el desembolso inicial a la firma de la escritura pueda ser inferior al 25 por ciento del precio.", "Seis millones de euros, sin que el desembolso inicial a la firma de la escritura pueda ser inferior al 50 por ciento del precio.", "Tres millones de euros, sin que el desembolso inicial a la firma de la escritura pueda ser inferior al 25 por ciento del precio.", "Un millón de euros, sin que el desembolso inicial a la firma de la escritura pueda ser inferior al 10 por ciento del precio."], "Art. 48.1 LGP: el resto puede distribuirse en los cuatro ejercicios siguientes, dentro de los porcentajes del art. 47.", ["cuyo importe exceda de seis millones de euros", "pueda ser inferior al 25 por ciento del precio"]),
 ("Artículo 49", "Modificaciones de crédito", "Según el artículo 49.2 de la Ley General Presupuestaria, los créditos para gastos que en el último día del ejercicio presupuestario no estén afectados al cumplimiento de obligaciones ya reconocidas:",
  ["Quedarán anulados de pleno derecho, sin perjuicio de lo establecido en el artículo 58.", "Se incorporarán automáticamente al ejercicio siguiente.", "Se transferirán al Fondo de Contingencia.", "Quedarán retenidos hasta el 31 de marzo del ejercicio siguiente."], "Art. 49.2 LGP; la salvedad son las incorporaciones del art. 58.", "quedarán anulados de pleno derecho, sin perjuicio de lo establecido en el artículo 58 de esta ley"),
 ("Artículo 50", "Fondo de Contingencia", "Según el artículo 50.1 de la Ley General Presupuestaria, el presupuesto del Estado incluirá una sección bajo la rúbrica «Fondo de Contingencia de ejecución presupuestaria» por importe:",
  ["Del dos por ciento del total de gastos para operaciones no financieras.", "Del uno por ciento del total de gastos para operaciones no financieras.", "Del dos por ciento del total de gastos del presupuesto, incluidas las operaciones financieras.", "Del cinco por ciento del total de gastos para operaciones no financieras."], "Art. 50.1 LGP (excluidos los gastos destinados a financiar a CC. AA. y EE. LL. por sus sistemas de financiación). El 1 % es el límite de los anticipos de Tesorería (art. 60).", "por importe del dos por ciento del total de gastos para operaciones no financieras"),
 ("Artículo 50", "Fondo de Contingencia", "Según el artículo 50.1 de la Ley General Presupuestaria, el Fondo de Contingencia únicamente financiará, cuando proceda, salvo los supuestos del artículo 59:",
  ["Las ampliaciones de crédito, los créditos extraordinarios y suplementos de crédito y las incorporaciones de crédito.", "Las transferencias de crédito y las generaciones de crédito.", "Los anticipos de Tesorería y las generaciones de crédito.", "Cualquier modificación de crédito, incluidas las derivadas de decisiones discrecionales de la Administración."], "Art. 50.1 a) a c) LGP; nunca gastos derivados de decisiones discrecionales sin cobertura presupuestaria.", ["a) Las ampliaciones de crédito reguladas en el artículo 54.", "b) Los créditos extraordinarios y suplementos de crédito", "c) Las incorporaciones de crédito"]),
 ("Artículo 50", "Fondo de Contingencia", "Según el artículo 50.2 de la Ley General Presupuestaria, la aplicación del Fondo de Contingencia se aprobará:",
  ["Mediante acuerdo del Consejo de Ministros, previamente a la autorización de las respectivas modificaciones de crédito.", "Mediante orden del Ministro de Hacienda, después de autorizar las modificaciones de crédito.", "Por la Dirección General de Presupuestos, previo informe de la Intervención General.", "Por las Cortes Generales, mediante ley."], "Art. 50.2 LGP (a propuesta del Ministro de Economía y Hacienda, según el texto).", "mediante acuerdo del Consejo de Ministros, previamente a la autorización de las respectivas modificaciones de crédito"),
 ("Artículo 51", "Modificaciones de crédito", "Según el artículo 51 de la Ley General Presupuestaria, la cuantía y finalidad de los créditos contenidos en los presupuestos de gastos sólo podrán ser modificadas durante el ejercicio mediante, entre otras:",
  ["Generaciones.", "Anticipos de caja fija.", "Compromisos de gasto plurianuales.", "Retenciones de crédito."], "Art. 51 LGP: transferencias, generaciones, ampliaciones, créditos extraordinarios y suplementos, e incorporaciones.", "b) Generaciones"),
 ("Artículo 52", "Transferencias", "Según el artículo 52.1 de la Ley General Presupuestaria, las transferencias son:",
  ["Traspasos de dotaciones entre créditos.", "Modificaciones que incrementan los créditos por ingresos no previstos.", "Incorporaciones de remanentes del ejercicio anterior.", "Incrementos de créditos ampliables hasta el importe de las obligaciones."], "Art. 52.1 LGP.", "Las transferencias son traspasos de dotaciones entre créditos"),
 ("Artículo 52", "Transferencias", "Según el artículo 52.1 a) de la Ley General Presupuestaria, NO podrán realizarse transferencias:",
  ["Desde créditos para operaciones de capital a créditos para operaciones corrientes.", "Desde créditos para operaciones corrientes a créditos para operaciones de capital.", "Entre créditos de un mismo programa.", "Con creación de créditos nuevos."], "Art. 52.1 a) LGP.", "ni desde créditos para operaciones de capital a créditos para operaciones corrientes"),
 ("Artículo 52", "Transferencias", "Según el artículo 52.1 b) de la Ley General Presupuestaria, la prohibición de transferencias entre créditos de distintas secciones presupuestarias no afectará a los créditos:",
  ["Del programa de contratación centralizada.", "De gastos de personal.", "De operaciones financieras.", "Destinados a subvenciones nominativas."], "Art. 52.1 b) LGP.", "Esta restricción no afectará a los créditos del programa de contratación centralizada"),
 ("Artículo 52", "Transferencias", "Según el artículo 52.1 c) de la Ley General Presupuestaria, las transferencias no minorarán:",
  ["Créditos extraordinarios o créditos que se hayan suplementado o ampliado en el ejercicio.", "Créditos para operaciones corrientes.", "Créditos de un mismo programa.", "Créditos del programa de imprevistos."], "Art. 52.1 c) LGP.", "No minorarán créditos extraordinarios o créditos que se hayan suplementado o ampliado en el ejercicio"),
 ("Artículo 52", "Transferencias", "Según el artículo 52.3 de la Ley General Presupuestaria, en ningún caso las transferencias podrán, salvo las excepciones que prevé:",
  ["Crear créditos destinados a subvenciones nominativas o aumentar los ya existentes.", "Crear créditos nuevos.", "Realizarse desde el programa de imprevistos.", "Derivarse de convenios entre departamentos ministeriales."], "Art. 52.3 LGP (salvo conformidad con la LGS o subvenciones o aportaciones a otros entes del sector público).", "En ningún caso las transferencias podrán crear créditos destinados a subvenciones nominativas o aumentar los ya existentes"),
 ("Artículo 53", "Generaciones", "Según el artículo 53.1 de la Ley General Presupuestaria, las generaciones son modificaciones que incrementan los créditos como consecuencia de:",
  ["La realización de determinados ingresos no previstos o superiores a los contemplados en el presupuesto inicial.", "Traspasos de dotaciones desde otros créditos.", "Obligaciones derivadas de normas con rango de ley.", "Remanentes de crédito del ejercicio anterior."], "Art. 53.1 LGP.", "incrementan los créditos como consecuencia de la realización de determinados ingresos no previstos o superiores a los contemplados en el presupuesto inicial"),
 ("Artículo 53", "Generaciones", "Según el artículo 53.2 de la Ley General Presupuestaria, podrán dar lugar a generaciones los ingresos realizados en el propio ejercicio como consecuencia de:",
  ["Enajenaciones de inmovilizado.", "Emisiones de Deuda Pública.", "Remanentes de crédito del ejercicio anterior.", "Bajas en el Fondo de Contingencia."], "Art. 53.2 c) LGP.", "c) Enajenaciones de inmovilizado"),
 ("Artículo 53", "Generaciones", "Según el artículo 53.4 de la Ley General Presupuestaria, los ingresos procedentes de reembolso de préstamos únicamente podrán dar lugar a generaciones en:",
  ["Créditos destinados a la concesión de nuevos préstamos.", "Cualquier crédito del mismo programa.", "Créditos para gastos de personal.", "Créditos para operaciones corrientes de la misma sección."], "Art. 53.4 LGP.", "únicamente podrán dar lugar a generaciones en aquellos créditos destinados a la concesión de nuevos préstamos"),
 ("Artículo 53", "Generaciones", "Según el artículo 53.5 de la Ley General Presupuestaria, con carácter excepcional podrán generar crédito en el Presupuesto del ejercicio:",
  ["Los ingresos realizados en el último trimestre del ejercicio anterior.", "Los ingresos realizados en el último mes del ejercicio anterior.", "Los ingresos previstos para el ejercicio siguiente.", "Los ingresos realizados en el último semestre del ejercicio anterior."], "Art. 53.5 LGP.", "los ingresos realizados en el último trimestre del ejercicio anterior"),
 ("Artículo 53", "Generaciones", "Según el artículo 53.3 de la Ley General Presupuestaria, como regla general la generación sólo podrá realizarse:",
  ["Cuando se hayan efectuado los correspondientes ingresos que la justifican.", "Cuando se haya aprobado la previsión de ingresos.", "Cuando se haya iniciado el expediente de ingreso.", "Cuando lo informe la Intervención General."], "Art. 53.3 LGP (con la excepción de organismos autónomos y Seguridad Social en el supuesto a).", "La generación sólo podrá realizarse cuando se hayan efectuado los correspondientes ingresos que la justifican"),
 ("Artículo 54", "Ampliaciones", "Según el artículo 54.1 de la Ley General Presupuestaria, excepcionalmente tendrán la condición de ampliables los créditos destinados:",
  ["Al pago de pensiones de Clases Pasivas del Estado.", "A gastos de personal funcionario.", "A subvenciones nominativas.", "A inversiones reales."], "Art. 54.1 LGP.", "Excepcionalmente tendrán la condición de ampliables los créditos destinados al pago de pensiones de Clases Pasivas del Estado"),
 ("Artículo 54", "Ampliaciones", "Según el artículo 54.2 de la Ley General Presupuestaria, en todo caso se consideran ampliables, en los Presupuestos de la Seguridad Social, los créditos:",
  ["Destinados a dotar el Fondo de Reserva de la Seguridad Social.", "Destinados a gastos de personal de las entidades gestoras.", "Destinados a atenciones protocolarias y representativas.", "Que hayan sido previamente minorados."], "Art. 54.2 d) LGP.", "Los destinados a dotar el Fondo de Reserva de la Seguridad Social"),
 ("Artículo 54", "Ampliaciones", "Según el artículo 54.3 de la Ley General Presupuestaria, las ampliaciones de crédito que afecten a operaciones del presupuesto del Estado se financiarán:",
  ["Con cargo al Fondo de Contingencia o con baja en otros créditos del presupuesto no financiero.", "Exclusivamente con Deuda Pública.", "Con cargo al remanente de tesorería del Estado.", "Con anticipos de Tesorería."], "Art. 54.3 LGP.", "se financiarán con cargo al Fondo de Contingencia, conforme a lo previsto en el artículo 50 de esta ley, o con baja en otros créditos del presupuesto no financiero"),
 ("Artículo 55", "Créditos extraordinarios y suplementos", "Según el artículo 55.1 de la Ley General Presupuestaria, procede tramitar un crédito extraordinario o suplementario cuando haya de realizarse con cargo al Presupuesto del Estado algún gasto:",
  ["Que no pueda demorarse hasta el ejercicio siguiente.", "Que pueda demorarse hasta el ejercicio siguiente.", "Que exceda del dos por ciento del presupuesto.", "Que se haya comprometido con carácter plurianual."], "Art. 55.1 LGP.", "algún gasto que no pueda demorarse hasta el ejercicio siguiente"),
 ("Artículo 55", "Créditos extraordinarios y suplementos", "Según el artículo 55.1 b) de la Ley General Presupuestaria, si la necesidad surgiera en operaciones financieras del Presupuesto, el crédito extraordinario o suplementario se financiará:",
  ["Con Deuda Pública o con baja en otros créditos de la misma naturaleza.", "Con baja en los créditos del Fondo de Contingencia.", "Con el remanente de tesorería.", "Con mayores ingresos sobre los previstos."], "Art. 55.1 b) LGP.", "se financiará con Deuda Pública o con baja en otros créditos de la misma naturaleza"),
 ("Artículo 55", "Créditos extraordinarios y suplementos", "Según el artículo 55.2 de la Ley General Presupuestaria, la remisión a las Cortes del proyecto de ley de crédito extraordinario o suplemento se propone por el Ministro de Hacienda:",
  ["Previo informe de la Dirección General de Presupuestos y dictamen del Consejo de Estado.", "Previo informe de la Intervención General y dictamen del Consejo de Estado.", "Previo informe del Tribunal de Cuentas.", "Previo dictamen de la Comisión de Presupuestos del Congreso."], "Art. 55.2 LGP.", "previo informe de la Dirección General de Presupuestos y dictamen del Consejo de Estado"),
 ("Artículo 55", "Créditos extraordinarios y suplementos", "Según el artículo 55.3 de la Ley General Presupuestaria, el Consejo de Ministros autorizará los créditos extraordinarios y suplementos de crédito para atender obligaciones del ejercicio corriente:",
  ["Cuando se financien con cargo al Fondo de Contingencia.", "Cuando se financien con baja en otros créditos.", "Cuando afecten a operaciones financieras.", "En todo caso, cualquiera que sea su financiación."], "Art. 55.3 LGP (con baja en otros créditos u operaciones financieras: proyecto de ley, 55.2).", "cuando se financien con cargo al Fondo de Contingencia"),
 ("Artículo 56", "Créditos extraordinarios y suplementos", "Según el artículo 56.2 de la Ley General Presupuestaria, la financiación de los créditos extraordinarios o suplementarios de los organismos autónomos únicamente podrá realizarse:",
  ["Con cargo al remanente de tesorería no aplicado del ejercicio anterior o con mayores ingresos sobre los previstos inicialmente.", "Con baja en el Fondo de Contingencia.", "Con Deuda Pública.", "Con anticipos de Tesorería del Estado."], "Art. 56.2 LGP.", "únicamente podrá realizarse con cargo a la parte del remanente de tesorería al fin del ejercicio anterior que no haya sido aplicada en el presupuesto del organismo, o con mayores ingresos sobre los previstos inicialmente"),
 ("Artículo 56", "Créditos extraordinarios y suplementos", "Según el artículo 56.3 b) de la Ley General Presupuestaria, la autorización de créditos extraordinarios o suplementarios de los organismos autónomos corresponde al Ministro de Hacienda cuando, superándose alguno de los límites del Presidente o Director:",
  ["No se alcance el 20 % del correspondiente capítulo ni se supere la cuantía de 1.000.000 de euros.", "No se alcance el 10 % del correspondiente capítulo ni se supere la cuantía de 500.000 euros.", "No se alcance el 25 % del correspondiente capítulo ni se supere la cuantía de 2.000.000 de euros.", "Se supere el 20 % del correspondiente capítulo."], "Art. 56.3 b) LGP.", "no se alcance el 20 % del correspondiente capítulo de su presupuesto inicial de gastos ni se supere la cuantía de 1.000.000 de euros"),
 ("Artículo 56", "Créditos extraordinarios y suplementos", "Según el artículo 56.6 de la Ley General Presupuestaria, el Ministro de Hacienda remitirá a las Cortes Generales un informe de los créditos extraordinarios y suplementos de crédito de los organismos autónomos con periodicidad:",
  ["Trimestral.", "Mensual.", "Semestral.", "Anual."], "Art. 56.6 LGP.", "un informe trimestral de los créditos extraordinarios y suplementos de crédito"),
 ("Artículo 57", "Créditos extraordinarios y suplementos", "Según el artículo 57.2 de la Ley General Presupuestaria, la autorización de créditos extraordinarios o suplementarios de las entidades de la Seguridad Social corresponde al Gobierno cuando su importe sea superior:",
  ["Al dos por ciento del presupuesto inicial de gastos de la respectiva Entidad.", "Al diez por ciento del correspondiente capítulo.", "A 1.000.000 de euros.", "Al cinco por ciento del presupuesto inicial de gastos de la respectiva Entidad."], "Art. 57.2 LGP.", "al Gobierno cuando su importe sea superior al dos por ciento del presupuesto inicial de gastos de la respectiva Entidad"),
 ("Artículo 58", "Incorporaciones", "Según el artículo 58 de la Ley General Presupuestaria, podrán incorporarse los remanentes que resulten de créditos extraordinarios y suplementos de crédito concedidos mediante norma con rango de ley:",
  ["En el último mes del ejercicio presupuestario anterior.", "En el último trimestre del ejercicio presupuestario anterior.", "En cualquier momento del ejercicio anterior.", "En el primer mes del ejercicio corriente."], "Art. 58 d) LGP.", "Los que resulten de créditos extraordinarios y suplementos de crédito que hayan sido concedidos mediante norma con rango de ley en el último mes del ejercicio presupuestario anterior"),
 ("Artículo 58", "Incorporaciones", "Según el artículo 58 b) de la Ley General Presupuestaria, podrán incorporarse los remanentes procedentes de las generaciones del artículo 53.2:",
  ["En sus párrafos a) y e).", "En sus párrafos b) y c).", "En todos sus párrafos.", "En sus párrafos d) y f)."], "Art. 58 b) LGP.", "Los procedentes de las generaciones a que se refiere el apartado 2 del artículo 53, en sus párrafos a) y e)"),
 ("Artículo 58", "Incorporaciones", "Según el artículo 58 de la Ley General Presupuestaria, las incorporaciones de crédito en el presupuesto de los organismos autónomos únicamente podrán realizarse:",
  ["Con cargo a la parte del remanente de tesorería que al fin del ejercicio anterior no haya sido aplicada al presupuesto del organismo.", "Con baja en el Fondo de Contingencia.", "Con Deuda Pública.", "Con baja en créditos de operaciones financieras."], "Art. 58 LGP.", "únicamente podrán realizarse con cargo a la parte del remanente de tesorería que al fin del ejercicio anterior no haya sido aplicada al presupuesto del organismo"),
 ("Artículo 60", "Anticipos de Tesorería", "Según el artículo 60.1 de la Ley General Presupuestaria, los anticipos de Tesorería tienen como límite máximo en cada ejercicio:",
  ["El uno por ciento de los créditos autorizados al Estado por la Ley de Presupuestos Generales del Estado.", "El dos por ciento de los créditos autorizados al Estado por la Ley de Presupuestos Generales del Estado.", "El cinco por ciento de los créditos autorizados al Estado por la Ley de Presupuestos Generales del Estado.", "El diez por ciento de los créditos autorizados al Estado por la Ley de Presupuestos Generales del Estado."], "Art. 60.1 LGP.", "con el límite máximo en cada ejercicio del uno por ciento de los créditos autorizados al Estado por la Ley de Presupuestos Generales del Estado"),
 ("Artículo 60", "Anticipos de Tesorería", "Según el artículo 60.1 a) de la Ley General Presupuestaria, puede concederse un anticipo de Tesorería cuando, iniciada la tramitación del expediente de crédito extraordinario o suplemento de crédito:",
  ["Hubiera dictaminado favorablemente el Consejo de Estado.", "Lo hubiera informado favorablemente la Intervención General.", "Lo solicite el organismo autónomo interesado.", "Lo hubiera aprobado el Congreso de los Diputados."], "Art. 60.1 a) LGP.", "hubiera dictaminado favorablemente el Consejo de Estado"),
 ("Artículo 61", "Competencias", "Según el artículo 61 de la Ley General Presupuestaria, la autorización de las transferencias entre distintas secciones presupuestarias como consecuencia de reorganizaciones administrativas corresponde:",
  ["Al Gobierno.", "Al Ministro de Hacienda.", "A los titulares de los ministerios afectados.", "A la Dirección General de Presupuestos."], "Art. 61 a) LGP.", "Autorizar las transferencias entre distintas secciones presupuestarias como consecuencia de reorganizaciones administrativas"),
 ("Artículo 62", "Competencias", "Según el artículo 62 de la Ley General Presupuestaria, la autorización de las incorporaciones de remanentes reguladas en el artículo 58 corresponde:",
  ["Al Ministro de Hacienda.", "Al Gobierno.", "A los titulares de los ministerios.", "A las Cortes Generales."], "Art. 62.1 c) LGP.", "Las incorporaciones de remanentes reguladas en el artículo 58"),
 ("Artículo 62", "Competencias", "Según el artículo 62.2 de la Ley General Presupuestaria, cuando exista informe negativo de la Intervención Delegada y el titular de la competencia lo remita en discrepancia, acordar o denegar la modificación presupuestaria corresponde:",
  ["Al Ministro de Hacienda.", "Al Consejo de Ministros.", "Al Tribunal de Cuentas.", "Al Consejo de Estado."], "Art. 62.2 LGP.", "Acordar o denegar las modificaciones presupuestarias, en los supuestos de competencia de los titulares de los ministerios y organismos autónomos, cuando exista informe negativo de la Intervención Delegada"),
 ("Artículo 63", "Competencias", "Según el artículo 63.1 de la Ley General Presupuestaria, los titulares de los ministerios podrán autorizar las modificaciones presupuestarias que les atribuye este artículo previo informe:",
  ["Favorable de la Intervención Delegada competente.", "Del Consejo de Estado.", "De la Dirección General de Presupuestos.", "Del Tribunal de Cuentas."], "Art. 63.1 LGP.", "previo informe favorable de la Intervención Delegada competente"),
 ("Artículo 63", "Competencias", "Según el artículo 63.1 b) de la Ley General Presupuestaria, los titulares de los ministerios podrán autorizar las generaciones de crédito de los párrafos del artículo 53.2:",
  ["a), d) y f).", "b) y e).", "c).", "a) y e)."], "Art. 63.1 b) LGP.", "Generaciones de crédito en los supuestos contemplados en los párrafos a), d) y f) del apartado 2 del artículo 53"),
 ("Artículo 63", "Competencias", "Según el artículo 63.4 de la Ley General Presupuestaria, una vez autorizadas las modificaciones presupuestarias, los acuerdos que afecten al presupuesto del Estado o de sus organismos se remitirán para instrumentar su ejecución:",
  ["A la Dirección General de Presupuestos del Ministerio de Hacienda.", "A la Intervención General de la Administración del Estado.", "Al Tribunal de Cuentas.", "A las Cortes Generales."], "Art. 63.4 LGP.", "se remitirán a la Dirección General de Presupuestos del Ministerio de Hacienda para instrumentar su ejecución"),
]
for art, cat, enun, ops, expl, frag in Q: T.q("LGP", art, cat, enun, ops, expl, frag)
for cod, n, *_ in EX: T.real(cod, n, "Preguntas oficiales")

# Flashcards
for q_, a_, cat in [
  ("Requisitos de los compromisos de gasto plurianual (art. 47.1)", "Que su ejecución se inicie en el propio ejercicio y que no superen los límites y anualidades del art. 47.2.", "Gastos plurianuales"),
  ("Límites de los gastos plurianuales (art. 47.2)", "Máximo cuatro ejercicios; sobre el crédito inicial: 70 % el inmediato siguiente, 60 % el segundo y 50 % el tercero y el cuarto.", "Gastos plurianuales"),
  ("Retención adicional en obras plurianuales (art. 47.2)", "10 % del importe de adjudicación, en el momento de adjudicar (salvo abono total del precio); computa dentro de los porcentajes.", "Gastos plurianuales"),
  ("¿A qué compromisos no se aplican los límites del art. 47.2?", "A la carga financiera de la Deuda y a los arrendamientos de inmuebles (incluidos los mixtos de arrendamiento y adquisición).", "Gastos plurianuales"),
  ("¿Quién puede excepcionar los límites de los gastos plurianuales? (art. 47.3)", "El Gobierno, en casos especialmente justificados, a propuesta del Ministro de Hacienda e iniciativa del ministerio, previo informe de la Dirección General de Presupuestos.", "Gastos plurianuales"),
  ("Pasos del art. 47 bis si falta crédito en un ejercicio posterior", "1.º Comunicarlo al tercero; 2.º reprogramar y reajustar anualidades; 3.º si no es posible, resolver con compensaciones.", "Gastos plurianuales"),
  ("Inmuebles con pago aplazado (art. 48.1)", "Compra directa de más de seis millones de euros: desembolso inicial no inferior al 25 % a la firma de la escritura y el resto en los cuatro ejercicios siguientes, con los límites del art. 47.", "Gastos plurianuales"),
  ("Fondo de Contingencia (art. 50)", "2 % del total de gastos para operaciones no financieras; solo financia ampliaciones, créditos extraordinarios y suplementos e incorporaciones; su aplicación la aprueba el Consejo de Ministros antes de la modificación; informe trimestral a las Cortes.", "Fondo de Contingencia"),
  ("Las cinco modificaciones de crédito (art. 51)", "Transferencias, generaciones, ampliaciones, créditos extraordinarios y suplementos de crédito, e incorporaciones.", "Modificaciones de crédito"),
  ("Restricciones de las transferencias (art. 52.1)", "No desde financieras al resto ni de capital a corrientes; no entre secciones; no minorar créditos extraordinarios, suplementados o ampliados en el ejercicio.", "Transferencias"),
  ("Supuestos de generación de crédito (art. 53.2)", "Aportaciones para financiar conjuntamente gastos; ventas de bienes y servicios; enajenaciones de inmovilizado; reembolsos de préstamos; ingresos legalmente afectados; reintegros de pagos indebidos del presupuesto corriente.", "Generaciones"),
  ("¿En qué créditos generan los reembolsos de préstamos? (art. 53.4)", "Únicamente en créditos destinados a la concesión de nuevos préstamos.", "Generaciones"),
  ("Créditos ampliables del Estado (art. 54.1)", "Pensiones de Clases Pasivas; obligaciones específicas del ejercicio derivadas de normas con rango de ley relacionadas taxativamente; Deuda del Estado y de sus organismos autónomos.", "Ampliaciones"),
  ("¿Qué créditos no pueden ampliarse? (art. 54.4)", "Los previamente minorados (salvo Seguridad Social, sección 06 Deuda Pública en las condiciones legales o minoración por traspaso de competencias a CC. AA.).", "Ampliaciones"),
  ("Crédito extraordinario y suplemento: diferencia (art. 55.1)", "Extraordinario: no existe crédito adecuado. Suplemento: el consignado es insuficiente y no ampliable. En ambos, gasto que no puede demorarse.", "Créditos extraordinarios y suplementos"),
  ("¿Cuándo autoriza el Consejo de Ministros un crédito extraordinario del Estado? (art. 55.3)", "Cuando se financia con el Fondo de Contingencia (obligaciones del ejercicio o de ejercicios anteriores con crédito anulado).", "Créditos extraordinarios y suplementos"),
  ("Competencia en organismos autónomos (art. 56.3)", "Presidente o Director: hasta 10 % del capítulo y 500.000 €; Ministro de Hacienda: hasta 20 % y 1.000.000 €; Consejo de Ministros: el resto.", "Créditos extraordinarios y suplementos"),
  ("Competencia en la Seguridad Social (art. 57.2)", "Gobierno si supera el 2 % del presupuesto inicial de gastos de la entidad; si no, el Ministro.", "Créditos extraordinarios y suplementos"),
  ("Supuestos de incorporación (art. 58)", "Norma con rango legal; generaciones del 53.2 a) y e); retenciones para créditos extraordinarios o suplementos anticipados pendientes de ley; créditos extraordinarios y suplementos concedidos por ley en el último mes.", "Incorporaciones"),
  ("Límite de los anticipos de Tesorería (art. 60)", "1 % de los créditos autorizados al Estado por la Ley de Presupuestos Generales del Estado, cada ejercicio.", "Anticipos de Tesorería"),
  ("¿Quién autoriza las incorporaciones y las ampliaciones del 54.1?", "El Ministro de Hacienda (art. 62.1 c y d).", "Competencias"),
  ("¿Qué transferencias autorizan los ministros? (art. 63.1 a)", "Entre créditos de un mismo programa o entre programas de un mismo servicio, con informe favorable de la Intervención Delegada y sin afectar a personal.", "Competencias"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Compromiso de gasto plurianual", "Compromiso de gasto que se extiende a ejercicios posteriores a aquel en que se autoriza, con los límites de años y porcentajes del art. 47 LGP.", "s1", "Gastos plurianuales")
T.glos("Tramitación anticipada", "Tramitación de contratos, encargos o convenios que puede llegar a la adjudicación y formalización aunque la ejecución empiece en ejercicios posteriores (art. 47.6 LGP).", "s1", "Gastos plurianuales")
T.glos("Reprogramación", "Reajuste de las anualidades de un compromiso plurianual cuando una Ley de Presupuestos posterior no autoriza créditos suficientes (art. 47 bis LGP).", "s2", "Gastos plurianuales")
T.glos("Fondo de Contingencia de ejecución presupuestaria", "Sección del presupuesto del Estado, del 2 % del gasto no financiero, para necesidades inaplazables y no discrecionales; financia ampliaciones, créditos extraordinarios y suplementos e incorporaciones (art. 50 LGP).", "s2c", "Fondo de Contingencia")
T.glos("Modificación de crédito", "Cambio de la cuantía o finalidad de los créditos iniciales durante el ejercicio, solo por las cinco vías del art. 51 LGP.", "s3", "Modificaciones de crédito")
T.glos("Transferencia de crédito", "Traspaso de dotaciones entre créditos, incluso con creación de créditos nuevos, con las restricciones del art. 52 LGP.", "s4", "Transferencias")
T.glos("Generación de crédito", "Incremento de créditos como consecuencia de ingresos no previstos o superiores a los del presupuesto inicial (art. 53 LGP).", "s5", "Generaciones")
T.glos("Crédito ampliable", "Crédito que, por excepción, puede incrementarse hasta el importe de las obligaciones (art. 54 LGP).", "s6", "Ampliaciones")
T.glos("Crédito extraordinario", "Modificación para un gasto que no puede demorarse y para el que no existe crédito adecuado (art. 55 LGP).", "s7", "Créditos extraordinarios y suplementos")
T.glos("Suplemento de crédito", "Modificación para un gasto que no puede demorarse cuando el crédito consignado es insuficiente y no ampliable (art. 55 LGP).", "s7", "Créditos extraordinarios y suplementos")
T.glos("Remanente de tesorería", "Fuente de financiación de las modificaciones de organismos autónomos y Seguridad Social: la parte del remanente al fin del ejercicio anterior no aplicada en su presupuesto (arts. 56, 57 y 58 LGP).", "s8", "Créditos extraordinarios y suplementos")
T.glos("Incorporación de crédito", "Paso de remanentes de crédito del ejercicio anterior a los créditos del ejercicio, en los casos del art. 58 LGP.", "s11", "Incorporaciones")
T.glos("Anticipo de Tesorería", "Anticipo excepcional concedido por el Gobierno para gastos inaplazables mientras se tramita un crédito extraordinario o suplemento, hasta el 1 % de los créditos autorizados al Estado (art. 60 LGP).", "s13", "Anticipos de Tesorería")

# Cronología (fechas de los metadatos del BOE)
T.hito("2003", "Ley 47/2003, de 26 de noviembre, General Presupuestaria (BOE de 27-11-2003)", "Arts. 47 y 51 a 63: gastos plurianuales y modificaciones de crédito", "normativo", "s1")
T.hito("2012", "Ley 17/2012, de 27 de diciembre, de Presupuestos Generales del Estado para el año 2013 (BOE de 28-12-2012)", "Introduce el art. 47 bis (en vigor el 1-1-2013)", "normativo", "s2")
T.hito("2013", "Ley 22/2013, de 23 de diciembre, de Presupuestos Generales del Estado para el año 2014 (BOE de 26-12-2013)", "Da la redacción vigente de los arts. 55 y 56 (en vigor el 1-1-2014)", "normativo", "s7")
T.hito("2021", "Ley 19/2021, de 20 de diciembre, por la que se establece el ingreso mínimo vital (BOE de 21-12-2021)", "Da la redacción vigente del art. 54 (en vigor el 1-1-2022)", "normativo", "s6")
T.hito("2021", "Ley 22/2021, de 28 de diciembre, de Presupuestos Generales del Estado para el año 2022 (BOE de 29-12-2021)", "Da la redacción vigente del art. 47 (en vigor el 1-1-2022)", "normativo", "s1")
T.hito("2022", "Ley 31/2022, de 23 de diciembre, de Presupuestos Generales del Estado para el año 2023 (BOE de 24-12-2022)", "Da la redacción vigente del art. 58 (en vigor el 1-1-2023)", "normativo", "s11")

T.publicar()
