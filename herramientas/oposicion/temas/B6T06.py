# -*- coding: utf-8 -*-
"""Tema VI.6 (B6T06): Gastos para la compra de bienes y servicios. Gastos de inversión.
Gastos de transferencias: corrientes y de capital. Anticipos de caja fija. Pagos «a
justificar». Justificación de libramientos.
Método del I.2. Normas (textos consolidados del BOE): Ley 47/2003, General Presupuestaria
(arts. 40, 43, 78, 79, 151, 153, 176 y 177 y disposiciones adicionales quinta y octava);
Resolución de 20 de enero de 2014, de la Dirección General de Presupuestos (clasificación
económica: anexos II y IV); Real Decreto 725/1989, sobre anticipos de Caja fija; Real
Decreto 640/1987, sobre pagos librados «a justificar»; CE, art. 9.3."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO.update({"RD725": "RD 725/1989", "RD640": "RD 640/1987", "RES2014": "Resolución de 20-1-2014"})

A2 = "Anexo II (Resolución de 20 de enero de 2014, de la Dirección General de Presupuestos): clasificación económica del gasto"
A4 = "Anexo IV (Resolución de 20 de enero de 2014, de la Dirección General de Presupuestos): código de la clasificación económica de los gastos"

T = Tema("B6T06",
  "Cuatro preguntas: I. Cómo se clasifican los gastos en bienes y servicios, las inversiones y las transferencias (LGP, arts. 40 y 43; Resolución de 20-1-2014) · II. Qué son los anticipos de caja fija y qué límites tienen (LGP, art. 78 y disp. adicional quinta.3; RD 725/1989) · III. Cuándo se libran pagos «a justificar» y cómo se gestionan (LGP, art. 79 y disp. adicional octava; RD 640/1987) · IV. Cómo se justifican los libramientos (LGP, arts. 78.5, 79.4 a 6, 151, 153, 176 y 177; RD 725/1989, arts. 7 y 9; RD 640/1987, arts. 8 a 10 y 12). Cada artículo: texto literal del BOE y ficha.",
  ["Clasificación económica", "Capítulo 2", "Bienes y servicios", "Artículo 23", "Capítulo 6", "Inversiones reales", "Capítulo 4", "Capítulo 7", "Transferencias", "Anticipos de caja fija", "7 por ciento", "RD 725/1989", "Pagos a justificar", "RD 640/1987", "Cuenta justificativa", "Tres meses", "Cajero pagador"])

# =============================================================================
T.ap("s0", "Mapa del tema: cuatro preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque VI, tema 6):
> Gastos para la compra de bienes y servicios. Gastos de inversión. Gastos de transferencias: corrientes y de capital. Anticipos de caja fija. Pagos «a justificar». Justificación de libramientos.

### El hilo conductor

El epígrafe se lee como **cuatro preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Ley 47/2003 (LGP) | Otras normas |
|---|---|---|---|
| **I** | ¿Cómo se clasifican los gastos en bienes y servicios, las inversiones y las transferencias? | Arts. 40.1 c) y 43 | Resolución de 20-1-2014 (DG de Presupuestos), anexos II y IV: capítulos 2, 4, 6 y 7 |
| **II** | ¿Qué son los anticipos de caja fija y qué límites tienen? | Art. 78.1 a 4; disp. adicional quinta.3 | RD 725/1989, arts. 1 a 6 y 8 |
| **III** | ¿Cuándo se libran pagos «a justificar» y cómo se gestionan? | Art. 79.1 a 3; disp. adicional octava | RD 640/1987, arts. 1 y 3 a 7 |
| **IV** | ¿Cómo se justifican los libramientos? | Arts. 78.5, 79.4 a 6, 151, 153, 176 y 177 | RD 725/1989, arts. 7 y 9; RD 640/1987, arts. 8 a 10 y 12 |

!> **La idea que une los cuatro bloques:** los tres primeros gastos del epígrafe son **capítulos** de la clasificación económica: bienes y servicios (**2**), transferencias corrientes (**4**), inversiones reales (**6**) y transferencias de capital (**7**) (I). La regla general es pagar **después** de acreditar la prestación; hay dos vías para mover fondos **antes**: el **anticipo de caja fija**, fondo **extrapresupuestario y permanente** para gastos periódicos o repetitivos del capítulo 2 (II), y el **pago a justificar**, libramiento **presupuestario** cuando no puede aportarse antes la documentación (III). En los dos casos hay que **justificar** después lo recibido (IV).

?> **Fronteras con otros temas.** La estructura general del presupuesto y las clasificaciones orgánica y por programas son del tema VI.2; las modificaciones de crédito, del tema VI.3; el control (Intervención y Tribunal de Cuentas), del tema VI.4; las fases de ejecución del gasto y los documentos contables, del tema VI.5. Aquí solo se citan en lo que hace falta.

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Cómo se clasifican los gastos en bienes y servicios, las inversiones y las transferencias? (LGP, arts. 40 y 43; Resolución de 20-1-2014)", donde(
  "Primera pregunta del tema. Los «gastos para la compra de bienes y servicios», los «de inversión» y los «de transferencias» son **capítulos** de la **clasificación económica** del presupuesto de gastos. La LGP fija los capítulos y su nivel de vinculación; la Resolución de 20 de enero de 2014 de la Dirección General de Presupuestos define qué gasto va a cada uno.",
  ["1 La clasificación económica y su especificación (LGP, arts. 40.1 c y 43)", "2 Gastos corrientes en bienes y servicios: capítulo 2", "3 Gastos de inversión: capítulo 6", "4 Transferencias corrientes y de capital: capítulos 4 y 7", "5 Cuadro de los cuatro capítulos"]))

T.ap("s1", "I.1 La clasificación económica y su especificación (LGP, arts. 40.1 c y 43)", f"""
La LGP ordena los créditos por **capítulos** y dice a qué **nivel** se especifican en el presupuesto del Estado. Ese nivel es el que se pregunta.

{unidad("1.1 Operaciones corrientes, de capital y financieras (LGP, art. 40.1 c)",
  lit("LGP", "Artículo 40", ["los gastos corrientes en bienes y servicios", "las transferencias corrientes", "las inversiones reales y las transferencias de capital", "Los capítulos se desglosarán en artículos y estos, a su vez, en conceptos que podrán dividirse en subconceptos"], solo=[4, 5, 6, 8, 9]),
  fichab("La clasificación económica de los estados de gastos",
         "La propia LGP fija los grupos; los códigos los establece la Dirección General de Presupuestos (Resolución de 20-1-2014)",
         ["::Agrupa los créditos por capítulos:", "Operaciones **corrientes**: personal, **bienes y servicios**, gastos financieros y **transferencias corrientes**", "Operaciones **de capital**: **inversiones reales** y **transferencias de capital**", "Fondo de Contingencia y operaciones financieras (activos y pasivos)", "Desglose: capítulo → artículo → concepto → subconcepto"],
         "—",
         "Bienes y servicios y transferencias **corrientes** son operaciones **corrientes**; inversiones reales y transferencias **de capital**, operaciones **de capital**. El último nivel (subconcepto) es potestativo: los conceptos «podrán dividirse»."))}

{unidad("1.2 A qué nivel se especifican los créditos (LGP, art. 43)",
  lit("LGP", "Artículo 43", ["los gastos corrientes en bienes y servicios, que se especificarán a nivel de artículo", "las inversiones reales a nivel de capítulo"], solo=[1, 2, 3, 4, 5, 6, 7, 8]),
  fichab("Nivel de especificación de los créditos en el presupuesto del Estado",
         "—",
         ["Regla general: **concepto**", "Gastos de personal y **gastos corrientes en bienes y servicios**: **artículo**", "**Inversiones reales**: **capítulo**", "Excepciones del art. 43.2: atenciones protocolarias, gastos reservados, arrendamientos de edificios, créditos ampliables, nominativos, los que fije la Ley de Presupuestos y créditos extraordinarios"],
         "—",
         "Cayó dos veces en 2025 (→ Cierre 1): bienes y servicios a nivel de **artículo**; inversiones reales a nivel de **capítulo**. Las transferencias siguen la regla general (**concepto**)."))}
""", 2)

T.ap("s2", "I.2 Gastos corrientes en bienes y servicios: capítulo 2 (Resolución de 20-1-2014)", f"""
El capítulo 2 es el de los «gastos para la compra de bienes y servicios» del epígrafe. La Resolución lo define por las **características** del bien y por lo que **no** puede imputarse a él.

{unidad("2.1 Qué gastos van al capítulo 2 (anexo IV)",
  lit("RES2014", "ai-4", ["que no originen un aumento de capital o del patrimonio público", "a) Ser bienes fungibles", "b) Tener una duración previsiblemente inferior al ejercicio presupuestario", "c) No ser susceptibles de inclusión en inventario", "d) Ser, previsiblemente, gastos reiterativos", "cualquier tipo de retribución"], solo=[181, 182, 183, 184, 185, 186, 187, 188, 189], titulo=A4 + ", capítulo 2"),
  fichab("Gastos corrientes en bienes y servicios necesarios para la actividad, que no aumentan el capital o el patrimonio público",
         "Estado, organismos autónomos, agencias estatales y otros organismos públicos",
         ["::Bienes que reúnan **alguna** de estas características:", "Fungibles", "Duración previsiblemente inferior al ejercicio", "No inventariables", "Gastos previsiblemente reiterativos", "También: bienes inmateriales reiterativos, no amortizables y no ligados a inversiones"],
         "—",
         f"Basta **una** de las cuatro características ({c('RES2014', 'ai-4', 'algunas de las características siguientes')}). Nunca retribuciones del personal propio: esas van al capítulo 1."))}

{unidad("2.2 Los artículos del capítulo 2 (anexo II)",
  lit("RES2014", "ai-2", ["23. Indemnizaciones por razón del servicio"], solo=[98, 99, 108, 117, 169, 174, 176, 180], titulo=A2 + ", capítulo 2"),
  fichab("Los artículos en que se desglosa el capítulo 2",
         "—",
         ["20 Arrendamientos y cánones", "21 Reparaciones, mantenimiento y conservación", "22 Material, suministros y otros", "**23 Indemnizaciones por razón del servicio**", "24 Gastos de publicaciones", "25 Conciertos de asistencia sanitaria", "27 Compras, suministros y otros gastos relacionados con la actividad"],
         "El capítulo 2 se especifica a **nivel de artículo** (LGP, art. 43.1 → I.1.2)",
         "Las indemnizaciones por razón del servicio (dietas, locomoción, traslado) son **artículo 23**, del capítulo 2, no del capítulo 1 de personal. Cayó dos veces en 2025 (→ Cierre 1)."))}

{unidad("2.3 Reparaciones y grandes reparaciones (anexo IV, artículo 21)",
  lit("RES2014", "ai-4", ["las grandes reparaciones que supongan un incremento de la productividad, capacidad, rendimiento, eficiencia o alargamiento de la vida útil del bien se imputarán al capítulo 6"], solo=[210, 217], titulo=A4 + ", artículo 21"),
  fichab("Frontera entre el capítulo 2 (conservación) y el capítulo 6 (inversión)",
         "—",
         ["Mantenimiento, reparación y conservación ordinarios: **artículo 21** (capítulo 2)", "Grandes reparaciones que aumentan productividad, capacidad, rendimiento, eficiencia o vida útil: **capítulo 6**"],
         "—",
         "La regla se da «Como norma general». La clave es si la reparación **mejora o alarga** el bien (→ I.3)."))}

{unidad("2.4 Indemnizaciones por razón del servicio (anexo IV, artículo 23)",
  lit("RES2014", "ai-4", ["altos cargos y asimilados, y su séquito, funcionarios, personal laboral fijo y eventual y otro personal", "asistencia a tribunales y órganos colegiados"], solo=[382, 383, 384, 385, 386, 387, 388, 389, 391, 392, 393], titulo=A4 + ", artículo 23"),
  fichab("Resarcimiento de gastos causados por el servicio",
         "Altos cargos y asimilados y su séquito, funcionarios, personal laboral fijo y eventual y otro personal",
         ["Conceptos: 230 Dietas · 231 Locomoción · 232 Traslado · 233 Otras indemnizaciones", "Incluye asistencias a tribunales y órganos colegiados"],
         "—",
         "Su régimen es materia del tema V.6; aquí solo interesa **dónde se imputan**: artículo **23** del capítulo **2**."))}
""", 2)

T.ap("s3", "I.3 Gastos de inversión: capítulo 6 (Resolución de 20-1-2014)", f"""
{unidad("3.1 Qué gastos van al capítulo 6 (anexo IV)",
  lit("RES2014", "ai-4", ["destinados a la creación o adquisición de bienes de capital", "bienes de naturaleza inventariable", "gastos de naturaleza inmaterial que tengan carácter amortizable", "Un gasto se considerará amortizable cuando contribuya al mantenimiento de la actividad del sujeto que lo realiza en ejercicios futuros"], solo=[525, 526, 527, 528, 529], titulo=A4 + ", capítulo 6"),
  fichab("Inversiones reales: gastos de capital realizados directamente por la propia Administración",
         "Estado, organismos autónomos, agencias estatales y otros organismos públicos, **directamente**",
         ["Creación o adquisición de bienes de capital", "Bienes **inventariables** para el funcionamiento operativo de los servicios", "Gastos inmateriales **amortizables**", "Leasing cuando se transfieren riesgos y ventajas (sobre todo si se ejercerá la opción de compra): solo la recuperación del coste; la carga financiera, al concepto 359"],
         "Se especifican a **nivel de capítulo** (LGP, art. 43.1 → I.1.2)",
         "**Directamente** por la Administración: si el dinero se da a otro sin contrapartida para que invierta él, es **transferencia de capital** (capítulo 7 → I.4.2). Inventariable → capítulo 6; no inventariable → capítulo 2."))}

{unidad("3.2 Los artículos del capítulo 6 (anexo II)",
  lit("RES2014", "ai-2", [], solo=[224, 225, 228, 231, 233, 235, 237, 239, 241], titulo=A2 + ", capítulo 6"),
  fichab("Desglose de las inversiones reales",
         "—",
         ["60 y 61: infraestructura y bienes de **uso general** (nueva / de reposición)", "62 y 63: asociada al **funcionamiento operativo** de los servicios (nueva / de reposición)", "64: inversiones de carácter **inmaterial**", "65 a 67: las mismas categorías, en **inversiones militares**"],
         "—",
         "Par = **nueva**, impar = **reposición** (60/61 y 62/63). El 64 es inmaterial (estudios, campañas, propiedad industrial, software de varios ejercicios)."))}

{unidad("3.3 Inversión nueva y de reposición (anexo IV, artículos 60 a 64)",
  lit("RES2014", "ai-4", ["que incrementen el stock de capital público", "Mantener o reponer los bienes deteriorados", "Prorrogar la vida útil del bien", "susceptibles de producir sus efectos en varios ejercicios futuros"], solo=[530, 531, 537, 538, 539, 540, 546, 547, 557, 558, 559, 560, 561, 565, 566, 567], titulo=A4 + ", artículos 60 a 64"),
  fichab("Criterios para elegir el artículo de inversión",
         "—",
         ["**Nueva** (60 y 62): incrementa el stock de capital público", "**Reposición** (61 y 63): mantener o reponer bienes deteriorados, prorrogar su vida útil o aumentar su eficacia; en el 63, también reponer los bienes que han devenido inútiles por su uso normal", "**Inmaterial** (64): gastos no materializados en activos que producen efectos en varios ejercicios"],
         "—",
         "Uso **general** (60-61: infraestructura y bienes destinados al uso general) frente a funcionamiento **operativo** de los servicios (62-63: edificios, mobiliario, equipos informáticos de la propia Administración)."))}
""", 2)

T.ap("s4", "I.4 Transferencias corrientes y de capital: capítulos 4 y 7 (Resolución de 20-1-2014)", f"""
Las transferencias son pagos **sin contrapartida directa**. Lo que separa el capítulo 4 del 7 es **a qué destina el receptor** los fondos.

{unidad("4.1 Transferencias corrientes: capítulo 4 (anexo IV)",
  lit("RES2014", "ai-4", ["sin contrapartida directa por parte de los agentes receptores, los cuales destinan estos fondos a financiar gastos de naturaleza corriente", "Prestaciones sociales, que comprenden pensiones a funcionarios y familias, de carácter civil y militar", "se imputarán en función del beneficiario final de las mismas"], solo=[478, 479, 480, 481, 482, 483, 484, 485], titulo=A4 + ", capítulo 4"),
  fichab("Pagos sin contrapartida directa para financiar gastos corrientes del receptor",
         "Paga: Estado, organismos autónomos, agencias estatales y otros organismos públicos · Recibe: el agente que indica cada artículo (40 a 49)",
         ["Pagos condicionados o no, sin contrapartida directa", "Indemnizaciones por el funcionamiento de los servicios públicos (si no van a otro capítulo)", "Pensiones a funcionarios y familias, civiles y militares", "Subvenciones en especie de carácter corriente"],
         "Se desagregan a nivel de concepto y/o subconcepto (agente receptor y/o finalidad)",
         "«Pagos, condicionados **o no**»: la condición no los saca del capítulo. Se imputan por el **beneficiario final**. Las **pensiones** de funcionarios van al capítulo **4**, no al 1."))}

{unidad("4.2 Transferencias de capital: capítulo 7 (anexo IV)",
  lit("RES2014", "ai-4", ["los cuales destinan estos fondos a financiar operaciones de capital", "Subvenciones en especie de capital"], solo=[581, 582, 583, 584, 585, 586], titulo=A4 + ", capítulo 7"),
  fichab("Pagos sin contrapartida directa para financiar operaciones de capital del receptor",
         "Paga: Estado, organismos autónomos, agencias estatales y otros organismos públicos · Recibe: el agente de cada artículo (70 a 79)",
         ["Pagos condicionados o no, sin contrapartida directa", "Subvenciones en especie de capital", "Imputación por el beneficiario final"],
         "Se desagregan a nivel de concepto y/o subconcepto",
         "Mismo esquema que el capítulo 4; cambia el **destino**: operaciones **de capital** (7) frente a gastos **corrientes** (4). Compárese con el capítulo 6: allí invierte **la propia** Administración (→ I.3.1)."))}

{unidad("4.3 Artículos por agente receptor (anexo II)",
  lit("RES2014", "ai-2", ["48. A familias e instituciones sin fines de lucro", "49. Al exterior"], solo=[210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220], titulo=A2 + ", capítulo 4"),
  lit("RES2014", "ai-4", ["sin contrapartida directa a agentes situados fuera del territorio nacional", "cuotas y contribuciones a organismos internacionales"], solo=[515, 516, 517], titulo=A4 + ", artículo 49"),
  fichab("El segundo dígito identifica al receptor; el primero, si es corriente (4) o de capital (7)",
         "—",
         ["x0 Administración del Estado · x1 organismos autónomos · x2 Seguridad Social · x3 agencias estatales y otros organismos públicos", "x4 sociedades, entidades públicas empresariales, fundaciones y resto del sector público · x5 comunidades autónomas · x6 entidades locales", "x7 empresas privadas · x8 familias e instituciones sin fines de lucro · x9 exterior"],
         "—",
         "El capítulo 7 repite la serie (70 a 79). Las **cuotas a organismos internacionales** van al artículo 49 (o 79): «al exterior»."))}
""", 2)

T.ap("s5", "I.5 Cuadro de los cuatro capítulos del epígrafe (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Capítulo | Nombre | Operación | Rasgo que lo define | Nivel de especificación (LGP, art. 43.1) |
|---|---|---|---|---|
| **2** | Gastos corrientes en bienes y servicios | Corriente | Fungible, menos de un ejercicio, no inventariable o reiterativo; no aumenta el patrimonio | **Artículo** |
| **4** | Transferencias corrientes | Corriente | Sin contrapartida directa; el receptor financia gasto **corriente** | Concepto (regla general) |
| **6** | Inversiones reales | De capital | Bienes de capital, inventariables o inmateriales amortizables, **directamente** por la Administración | **Capítulo** |
| **7** | Transferencias de capital | De capital | Sin contrapartida directa; el receptor financia operaciones **de capital** | Concepto (regla general) |

{resumen([
  "Clasificación económica: **corrientes** (cap. 1 a 4), Fondo de Contingencia (5), **de capital** (6 y 7) y financieras (8 y 9) (LGP, art. 40.1 c; numeración de los capítulos: Resolución de 20-1-2014, anexo II).",
  "Bienes y servicios a nivel de **artículo**; inversiones reales a nivel de **capítulo**; el resto, de **concepto** (art. 43.1).",
  "Capítulo 2: basta **una** característica (fungible, menos de un año, no inventariable, reiterativo). Indemnizaciones por razón del servicio: **artículo 23**.",
  "Transferencias: **sin contrapartida directa**; capítulo 4 si financian gasto corriente, 7 si financian operaciones de capital; el segundo dígito es el **receptor**."],
  "Siguiente: II. ¿Qué son los anticipos de caja fija y qué límites tienen?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Qué son los anticipos de caja fija y qué límites tienen? (LGP, art. 78 y disp. adicional quinta.3; RD 725/1989)", donde(
  "Segunda pregunta. Muchos gastos del capítulo 2 son pequeños y repetitivos (dietas, material, locomoción). Para pagarlos al momento, la caja recibe un **fondo permanente** que se repone a medida que se gasta: el **anticipo de caja fija**.",
  ["1 Concepto y normas reguladoras (LGP, art. 78.1; RD 725/1989, art. 1)", "2 Límites cuantitativos (LGP, art. 78.3; RD 725/1989, art. 2; disp. adicional quinta.3) y fondos de maniobra", "3 Concesión, situación y disposición de los fondos (RD 725/1989, arts. 3, 4 y 6)", "4 Gestión de los pagos y contabilidad (RD 725/1989, arts. 5 y 8)"]))

T.ap("s6", "II.1 Concepto y normas reguladoras (LGP, art. 78.1; RD 725/1989, art. 1)", f"""
{unidad("1.1 Quién dicta las normas y qué es un anticipo de caja fija (LGP, art. 78.1)",
  lit("LGP", "Artículo 78", ["previo informe de su Intervención Delegada en ambos casos", "provisiones de fondos de carácter extrapresupuestario y permanente", "gastos periódicos o repetitivos"], solo=[1, 2]),
  fichab("Provisión de fondos extrapresupuestaria y permanente para gastos periódicos o repetitivos del capítulo 2",
         f"Normas: {c('LGP', 'Artículo 78', 'los ministros y los presidentes o directores de los organismos autónomos')}, previo informe de la **Intervención Delegada** · Reciben los fondos: pagadurías, cajas y habilitaciones",
         ["Las normas fijan los gastos que se pueden pagar así, los conceptos presupuestarios, los límites de cada uno y su aplicación al presupuesto", "Atención **inmediata** del gasto y **posterior** aplicación al capítulo 2 del presupuesto del año"],
         "—",
         "**Extrapresupuestario** y **permanente** (no «presupuestario», no «temporal»). Se aplica al capítulo de **gastos corrientes en bienes y servicios** del año en que se realicen."))}

{unidad("1.2 El concepto en el reglamento (RD 725/1989, art. 1)",
  lit("RD725", "a1", ["carácter extrapresupuestario y permanente", "dietas, gastos de locomoción, material no inventariable, conservación, tracto sucesivo", "no tendrán la consideración de pagos a justiciar"]),
  fichab("Definición reglamentaria del anticipo de caja fija",
         "Pagadurías, Cajas y Habilitaciones",
         ["Mismo concepto que la LGP", "Ejemplos: dietas, locomoción, material no inventariable, conservación, tracto sucesivo y similares", "No son pagos «a justificar» (→ III.1)"],
         "—",
         "Cayó en 2025 (→ Cierre 1) con los cuatro cruces: presupuestario/extrapresupuestario × permanente/temporal. La errata «justiciar» está en el BOE."))}
""", 2)

T.ap("s7", "II.2 Límites cuantitativos y fondos de maniobra (LGP, art. 78.2 a 4; RD 725/1989, art. 2; disp. adicional quinta.3)", f"""
{unidad("2.1 El 7 por ciento y sus excepciones (LGP, art. 78.3)",
  lit("LGP", "Artículo 78", ["el siete por ciento del total de créditos del capítulo destinado a gastos corrientes en bienes y servicios", "hasta un máximo del 14 por ciento", "hasta un máximo del 10 por ciento de los créditos del artículo 23"], solo=[4, 5, 6]),
  fichab("Tope de la cuantía global de los anticipos de caja fija",
         "Cada ministerio u organismo autónomo; excepciones: Agencia Española de Cooperación Internacional y Ministerio del Interior (programa 222A)",
         ["General: **7 %** de los créditos del **capítulo 2** del presupuesto vigente", "AECI: hasta el **14 %** del capítulo 2", "Interior, programa 222A «Seguridad ciudadana»: hasta el **10 % de los créditos del artículo 23**, solo para gestionar ese artículo"],
         "Porcentajes sobre el presupuesto **vigente en cada momento**",
         "El 7 % es sobre el **capítulo 2** (no sobre el total del presupuesto). El 10 % no es un límite general: es sobre el **artículo 23** del programa **222A** de **Interior**. La pregunta X-96 de 2025 (7 % / 10 %) lleva la marca **Discrepancia** en el test real: ninguna opción reproduce esta regla (→ Cierre 1)."))}

{unidad("2.2 Fondos de maniobra de la Seguridad Social (LGP, art. 78.2 y 4)",
  lit("LGP", "Artículo 78", ["fondos de maniobra", "del tres por ciento", "hasta un siete por ciento"], solo=[3, 7, 8]),
  fichab("Equivalente de la caja fija en las entidades gestoras y servicios comunes de la Seguridad Social",
         "Normas: Director General de la **Tesorería General de la Seguridad Social**, previo informe de la Intervención General de la Seguridad Social · Elevación del porcentaje: el «Ministro de Trabajo y Asuntos Sociales» (denominación de la ley)",
         "Fondos de maniobra asignados a los centros de gestión de cada entidad",
         "Máximo **3 %** del capítulo 2; elevable hasta el **7 %**",
         "En la Seguridad Social no se llaman anticipos de caja fija sino **fondos de maniobra**: 3 % (elevable al 7 %)."))}

{unidad("2.3 Quién establece el sistema y límites por pago (RD 725/1989, art. 2)",
  lit("RD725", "a2", ["mediante acuerdo de los titulares", "del 7 por 100", "por importe inferior a 600 euros", "pagos individualizados superiores a 5.000 euros", "ni fraccionarse un único gasto en varios pagos"]),
  fichab("Implantación del sistema y límites de cada pago",
         f"{c('RD725', 'a2', 'Los Departamentos ministeriales y los Organismos autónomos')}, por acuerdo de sus titulares",
         ["Establecido el sistema, no se tramitan libramientos presupuestarios a perceptores directos por menos de **600 euros** en esos conceptos (salvo reposición)", "Con cargo al anticipo, ningún pago individualizado de más de **5.000 euros**, salvo teléfono, energía eléctrica, combustibles o indemnizaciones por razón del servicio", "Ni acumular pagos en un justificante ni fraccionar un gasto"],
         "Límite global: **7 por 100** del capítulo 2 (como la LGP)",
         "Dos cifras: **600** € (por debajo, se paga por caja fija y no por libramiento directo) y **5.000** € (por encima, no se paga por caja fija, salvo las cuatro excepciones)."))}

{unidad("2.4 Anticipo de caja fija de Defensa en el exterior (LGP, disposición adicional quinta.3)",
  lit("LGP", "Disposición adicional quinta", ["no podrá exceder del 2,5 por ciento del total de los créditos de inversiones reales"], solo=[5, 6]),
  fichab("Anticipo especial para material militar y servicios complementarios adquiridos en el exterior",
         "Ministerio de Defensa; normas reglamentarias a propuesta conjunta de Hacienda y Defensa",
         "Para adquisiciones de material militar y servicios complementarios en el exterior",
         "Máximo **2,5 %** de los créditos de **inversiones reales** (capítulo 6) del Ministerio",
         "Única caja fija cuyo límite se calcula sobre **inversiones reales**, no sobre el capítulo 2."))}
""", 2)

T.ap("s8", "II.3 Concesión, situación y disposición de los fondos (RD 725/1989, arts. 3, 4 y 6)", f"""
{unidad("3.1 Distribución por cajas e informe del Interventor (RD 725/1989, art. 3)",
  lit("RD725", "a3", ["acordar la distribución territorial y por Cajas pagadoras", "informe favorable del Interventor delegado respectivo, circunscrito a que se respete el citado límite del 7 por 100", "deberá reintegrar"], solo=[1, 2, 6, 7]),
  fichab("Reparto del anticipo entre las cajas pagadoras",
         "Las autoridades que establecen el sistema (titulares de ministerios y organismos autónomos); informe favorable del **Interventor delegado**; en los organismos autónomos ordenan los pagos sus Presidentes o Directores",
         ["Distribución territorial y por cajas, y sus modificaciones", "Si se suprime una caja, el pagador **reintegra** el anticipo; no hay traspaso directo a la caja que asuma sus funciones"],
         "Siempre dentro del **7 por 100**",
         "El informe del Interventor se **circunscribe** a comprobar el límite del 7 por 100."))}

{unidad("3.2 Dónde están los fondos (RD 725/1989, art. 4)",
  lit("RD725", "a4", ["«Tesoro Público. Provisión de Fondos»", "el carácter de fondos públicos y formarán parte integrante del Tesoro Público"], solo=[1, 2, 5]),
  fichab("Situación de los fondos del anticipo",
         "Cajas pagadoras",
         ["Cuentas en el **Banco de España**, agrupación «Tesoro Público. Provisión de Fondos»", "Si hay causas que lo justifiquen, en cuentas de **entidades de crédito**, con autorización"],
         "—",
         "Son **fondos públicos** e integran el **Tesoro Público** (también lo dice la LGP, art. 78.5 → IV.1.1)."))}

{unidad("3.3 Cómo se dispone de los fondos (RD 725/1989, art. 6)",
  lit("RD725", "a6", ["cheques nominativos o transferencias bancarias", "firmas mancomunadas", "De la custodia de estos fondos será directamente responsable del Cajero pagador"]),
  fichab("Disposición de fondos de las cuentas del anticipo",
         "Firman **mancomunadamente** el Cajero pagador y el funcionario que designe el Jefe de la Unidad; autorizan el efectivo los Jefes de Departamento y Presidentes o Directores",
         ["Cheques nominativos o transferencias", "Efectivo en caja para necesidades imprevistas y gastos de menor cuantía", "Posibles subcajas dependientes de una caja central"],
         "—",
         "Firma **mancomunada** (dos firmas); una misma persona no puede hacer **ambas** sustituciones. Del efectivo responde **directamente** el Cajero pagador."))}
""", 2)

T.ap("s9", "II.4 Gestión de los pagos y contabilidad (RD 725/1989, arts. 5 y 8)", f"""
{unidad("4.1 El «Páguese» (RD 725/1989, art. 5)",
  lit("RD725", "a5", ["El «Páguese» del Órgano de gestión correspondiente, dirigido al cajero"]),
  fichab("Tramitación de cada gasto pagado por caja fija",
         "El **órgano de gestión** ordena; el **cajero** paga",
         "Se sigue la tramitación de cada gasto, con constancia documental; el «Páguese» figura, como mínimo, en facturas, recibos o justificantes",
         "—",
         "El pago por caja fija no suprime la tramitación del gasto: el «Páguese» lo da el **órgano de gestión**, no el cajero."))}

{unidad("4.2 Contabilidad auxiliar (RD 725/1989, art. 8)",
  lit("RD725", "a8", ["contabilidad auxiliar detallada", "control contable de las órdenes de pago expedidas para reponer anticipos de Caja fija"]),
  fichab("Registro contable de los anticipos",
         "Cajas pagadoras; oficinas de contabilidad de ministerios y organismos autónomos; normas de la **IGAE**",
         ["Cajas: contabilidad auxiliar detallada, separando los anticipos de otros cobros, pagos o custodia", "Oficinas de contabilidad: control de las órdenes de pago de reposición"],
         "—",
         "Las normas contables las establece la **Intervención General de la Administración del Estado**."))}

{resumen([
  "Anticipo de caja fija: provisión de fondos **extrapresupuestaria y permanente** a pagadurías, cajas y habilitaciones para gastos **periódicos o repetitivos** del **capítulo 2** (LGP, art. 78.1; RD 725/1989, art. 1).",
  "Normas: ministros y presidentes o directores de organismos autónomos, previo informe de la **Intervención Delegada**.",
  "Límite global: **7 %** del capítulo 2 (AECI hasta el **14 %**; Interior 222A, hasta el **10 % del artículo 23**); Seguridad Social: fondos de maniobra del **3 %** (elevable al **7 %**); Defensa en el exterior: **2,5 %** de inversiones reales.",
  "Por pago: libramientos directos de menos de **600 €** no; pagos por caja fija de más de **5.000 €** no, salvo teléfono, energía, combustibles e indemnizaciones por razón del servicio."],
  "Siguiente: III. ¿Cuándo se libran pagos «a justificar» y cómo se gestionan?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Cuándo se libran pagos «a justificar» y cómo se gestionan? (LGP, art. 79 y disp. adicional octava; RD 640/1987)", donde(
  "Tercera pregunta. La regla es que la obligación se reconoce y se paga **después** de acreditar la prestación. El pago «a justificar» es la **excepción**: el dinero sale antes y los documentos se presentan después. A diferencia de la caja fija, se **aplica al presupuesto** desde el principio.",
  ["1 Cuándo se libra un pago a justificar (LGP, art. 79.1 y 2; disp. adicional octava)", "2 Ejercicio al que se imputa y calendario (LGP, art. 79.3)", "3 Normas, fiscalización y cajas pagadoras (RD 640/1987, arts. 1, 3 y 4)", "4 Situación de los fondos y pagos (RD 640/1987, arts. 5 a 7)"]))

T.ap("s10", "III.1 Cuándo se libra un pago a justificar (LGP, art. 79.1 y 2; disp. adicional octava)", f"""
{unidad("1.1 Los supuestos (LGP, art. 79.1 y 2)",
  lit("LGP", "Artículo 79", ["excepcionalmente, no pueda aportarse la documentación justificativa", "en el extranjero", "en localidad donde no exista dependencia", "designarán el órgano competente para gestionar dichos pagos"], solo=[1, 2, 3]),
  fichab("Libramiento de fondos presupuestarios antes de justificar la obligación",
         f"Autorizan (supuesto del 79.2): {c('LGP', 'Artículo 79', 'los ministros, presidentes o directores de los organismos autónomos o de las entidades gestoras y servicios comunes de la Seguridad Social')}, que designan el órgano gestor",
         ["::Tres supuestos:", "Excepcionalmente, no puede aportarse la documentación justificativa en el momento del art. 73.4 (reconocimiento de la obligación)", "Servicios y prestaciones que han tenido o van a tener lugar **en el extranjero**", "Gastos en una **localidad donde no exista dependencia** del ministerio u organismo"],
         "—",
         f"Es **excepcional**. La designación del órgano gestor implica competencia para los gastos y pagos y para {c('LGP', 'Artículo 79', 'la formación, rendición y justificación de las correspondientes cuentas')}."))}

{unidad("1.2 Un caso especial: las Confederaciones Hidrográficas (LGP, disposición adicional octava)",
  lit("LGP", "Disposición adicional octava", ["obras declaradas de emergencia y por administración", "a los presidentes de las respectivas confederaciones hidrográficas", "deberán ser aprobadas por la autoridad que dispuso la expedición"]),
  fichab("Fondos a justificar para obras de emergencia, por administración y expropiaciones de las Confederaciones",
         "Propone el libramiento el Ministerio (Dirección General de Obras Hidráulicas y Calidad de las Aguas); ordenan los pagos materiales los **presidentes** de las Confederaciones",
         "Obras de emergencia y por administración, y expropiaciones",
         "—",
         "Las cuentas las aprueba **la autoridad que dispuso** la expedición de los libramientos."))}
""", 2)

T.ap("s11", "III.2 Ejercicio al que se imputa y calendario (LGP, art. 79.3)", f"""
{unidad("2.1 Temporalidad, calendario y reintegro (LGP, art. 79.3)",
  lit("LGP", "Artículo 79", ["exclusivamente se podrán imputar las obligaciones derivadas de las actuaciones realizadas y exigibles en el ejercicio presupuestario al que corresponde el libramiento aprobado", "el Consejo de Ministros podrá acordar", "un calendario de las actuaciones", "carta de pago demostrativa de su reintegro"], solo=[4, 5, 6, 7]),
  fichab("Regla de anualidad aplicada a los libramientos a justificar",
         "Excepción para gastos en el extranjero: **Consejo de Ministros**; reintegro: el **cajero pagador**",
         ["Solo obligaciones de actuaciones realizadas y exigibles en el **ejercicio** del libramiento (art. 49)", "Toda propuesta de pago a justificar incluye un **calendario** de actuaciones", "Si del calendario resultan gastos plurianuales: expediente que desglose las anualidades", "Lo no invertido en el ejercicio se justifica con **carta de pago** de su reintegro al Tesoro"],
         "Excepción: fondos para gastos **en el extranjero** pueden atender gastos del ejercicio **siguiente**, si lo acuerda el Consejo de Ministros por interés general",
         "El calendario es **obligatorio** en **todas** las propuestas, «cualquiera que sea su finalidad». La excepción del ejercicio siguiente es solo para el **extranjero** y la acuerda el **Consejo de Ministros**."))}
""", 2)

T.ap("s12", "III.3 Normas, fiscalización y cajas pagadoras (RD 640/1987, arts. 1, 3 y 4)", f"""
?> **Aviso de vigencia.** El RD 640/1987 desarrolla la Ley General Presupuestaria de 1977 y cita normas de su época (Ley 46/1985, Ministerio de Economía y Hacienda). Se cita **literal** como está en el BOE; sus arts. 2 y 11 (anticipos de caja fija) están derogados por el RD 725/1989 ({c('RD725', 'dd', 'en especial los artículos 2.º y 11, del Real Decreto 640/1987')}).

{unidad("3.1 Normas de cada ministerio y límites (RD 640/1987, art. 1)",
  lit("RD640", "a1", ["previo informe del Interventor Delegado", "No se podrán expedir órdenes de pago «a justificar» a favor de las Cajas pagadoras cuando transcurridos los plazos reglamentarios"], solo=[1, 2, 3]),
  fichab("Quién regula la expedición y cuándo se bloquea",
         "Ministros y Presidentes o Directores de organismos autónomos, previo informe del **Interventor Delegado**",
         ["Cada uno dicta las normas para expedir órdenes de pago a justificar con cargo a su presupuesto", "Se ajustan al plan de disposición de fondos del Tesoro"],
         "—",
         "Una caja que **no ha justificado** en plazo fondos anteriores **no puede recibir** nuevas órdenes de pago a justificar."))}

{unidad("3.2 Base y fiscalización de la orden de pago (RD 640/1987, art. 3)",
  lit("RD640", "a3", ["se aplicarán a los correspondientes créditos presupuestarios", "Si existe crédito y el propuesto es el adecuado"]),
  fichab("Requisitos de la orden de pago a justificar",
         "La **autoridad competente para autorizar** el gasto dicta la orden o resolución; la Intervención fiscaliza",
         ["::La fiscalización comprueba:", "a) Orden o resolución de autoridad competente", "b) Existencia de crédito adecuado", "c) Adaptación a las normas del art. 1.1", "d) Situación de la caja pagadora (si tiene fondos sin justificar)"],
         "—",
         "Se **aplican a los créditos presupuestarios**: es la gran diferencia con la caja fija, que es **extrapresupuestaria** (→ II.1.1)."))}

{unidad("3.3 Cajas pagadoras y Unidad Central (RD 640/1987, art. 4)",
  lit("RD640", "a4", ["Cajero pagador con nombramiento expreso", "una Unidad Central", "censo de las Cajas pagadoras"], solo=[1, 2, 4, 5, 6]),
  fichab("Organización de los pagos a justificar",
         "Cajas pagadoras de ministerios y organismos autónomos, cada una con un **Cajero pagador** nombrado expresamente; **Unidad Central** dependiente de la Subsecretaría si hay varias cajas",
         ["Las órdenes de pago se expiden **a favor de las Cajas pagadoras**", "La Unidad Central coordina las cajas y lleva el **censo** de cajas y cajeros", "Cabe una Caja Pagadora Central única"],
         "—",
         "La orden se expide a favor de la **caja**, no del acreedor final."))}
""", 2)

T.ap("s13", "III.4 Situación de los fondos y pagos (RD 640/1987, arts. 5 a 7)", f"""
{unidad("4.1 Cuentas de los fondos (RD 640/1987, art. 5)",
  lit("RD640", "a5", ["«Tesoro Público.-Anticipo de fondos a justificar»", "el carácter de fondos públicos"], solo=[1, 3, 6, 7]),
  fichab("Dónde se sitúan los fondos librados a justificar",
         "Cajas pagadoras",
         ["Cuentas en el Banco de España, agrupación «Tesoro Público.-Anticipo de fondos a justificar»", "Con causa justificada, en entidades de crédito, con convenio y autorización del Ministerio", "Los intereses se ingresan en el Tesoro o en la tesorería del organismo"],
         "—",
         "Son **fondos públicos**."))}

{unidad("4.2 Disposición y pagos (RD 640/1987, arts. 6 y 7)",
  lit("RD640", "a6", ["firmas mancomunadas"]),
  lit("RD640", "a7", ["no podrán exceder de los pagos que se prevea realizar durante un mes"]),
  fichab("Cómo paga el cajero con fondos a justificar",
         "Acuerdan los gastos los **gestores competentes**; paga el **Cajero pagador**; el efectivo lo autorizan Ministros y Presidentes o Directores",
         ["Cheques nominativos o transferencias, con firmas mancomunadas", "El gestor ordena al cajero el pago y lo hace constar en el justificante", "Efectivo para indemnizaciones por razón de servicio y atenciones de menor cuantía"],
         "Efectivo: no más de lo que se prevea pagar **durante un mes**",
         "Del efectivo es **directamente responsable** el Cajero pagador. Límite del efectivo: pagos previstos de **un mes**."))}

{resumen([
  "Pago a justificar: **excepcional**, cuando no puede aportarse la documentación antes del reconocimiento de la obligación; también para gastos **en el extranjero** y en **localidades sin dependencia** (LGP, art. 79.1 y 2).",
  "Es **presupuestario**: se aplica al crédito desde el libramiento (RD 640/1987, art. 3).",
  "Solo obligaciones del **ejercicio** del libramiento; **calendario** obligatorio; lo no invertido se reintegra con **carta de pago**; excepción para el **extranjero** por acuerdo del **Consejo de Ministros** (art. 79.3).",
  "Se libra a favor de **Cajas pagadoras**; una caja con fondos sin justificar en plazo no puede recibir más (RD 640/1987, arts. 1.3 y 4)."],
  "Siguiente: IV. ¿Cómo se justifican los libramientos?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Cómo se justifican los libramientos? (LGP, arts. 78.5, 79.4 a 6, 151, 153, 176 y 177; RD 725/1989; RD 640/1987)", donde(
  "Cuarta pregunta. Todo fondo que sale antes de acreditar el gasto tiene que **justificarse** después: el anticipo de caja fija, mediante cuentas para **reponer** los fondos; el pago a justificar, mediante una **cuenta justificativa** en plazo. Si no se justifica, hay **responsabilidad**.",
  ["1 Justificación y reposición de los anticipos de caja fija (LGP, art. 78.5; RD 725/1989, arts. 7 y 9)", "2 Cuenta justificativa de los pagos a justificar (LGP, art. 79.4 a 6)", "3 Contabilidad, control y cuentas en el RD 640/1987 (arts. 8, 9, 10 y 12)", "4 Fiscalización y responsabilidad (LGP, arts. 151, 153, 176 y 177)", "5 Cuadro comparativo: anticipo de caja fija y pago a justificar"]))

T.ap("s14", "IV.1 Justificación y reposición de los anticipos de caja fija (LGP, art. 78.5; RD 725/1989, arts. 7 y 9)", f"""
{unidad("1.1 Los fondos forman parte del Tesoro y se justifican (LGP, art. 78.5)",
  lit("LGP", "Artículo 78", ["formarán parte del Tesoro Público", "justificarán su aplicación y situación conforme se establezca reglamentariamente"], solo=[9]),
  fichab("Deber de justificar los anticipos de caja fija y los fondos de maniobra",
         "Las unidades administrativas responsables de estos fondos",
         "Justifican su **aplicación** y su **situación**, según el reglamento (RD 725/1989)",
         "—",
         "Los fondos forman parte del **Tesoro Público** (o del patrimonio de la Seguridad Social)."))}

{unidad("1.2 Cuentas, reposición e imputación al presupuesto (RD 725/1989, art. 7)",
  lit("RD725", "a7", ["necesariamente, en el mes de diciembre de cada año", "serán aprobadas por los Jefes de las Unidades Administrativas", "a favor del Cajero pagador", "pudiendo utilizar procedimientos de muestreo", "en un plazo de quince días"], solo=[1, 2, 4, 6, 7, 8, 9]),
  fichab("Rendición de cuentas del cajero y reposición del anticipo",
         "Rinde: el **Cajero pagador** · Aprueban: los **Jefes de las Unidades Administrativas** a las que estén adscritas las cajas · Examina: la **Intervención delegada**, central o territorial · Destino final de la cuenta: el **Tribunal de Cuentas**",
         ["Cuentas con facturas y justificantes originales", "Con lo justificado se expiden los documentos contables a favor del cajero, con imputación al presupuesto (así **se repone** el anticipo)", "La Intervención examina, incluso por muestreo, e informa"],
         ["::Plazos:", "Cuentas: cuando lo aconsejen las necesidades de tesorería y **necesariamente en diciembre**", "Alegaciones o subsanación del órgano gestor: **quince días**; da cuenta al Interventor en **quince días**"],
         "Cayó en 2025 (→ Cierre 1): **diciembre**. Enero, abril, julio y octubre son los meses de los **estados de situación de tesorería** (art. 9 → IV.1.3), no de la rendición de cuentas."))}

{unidad("1.3 Estados de situación de tesorería y comprobaciones (RD 725/1989, art. 9)",
  lit("RD725", "a9", ["en las primeras quincenas de los meses de enero, abril, julio y octubre", "en cualquier momento"]),
  fichab("Control periódico de las cajas",
         "Las autoridades del art. 2.1 fijan la periodicidad; copias al Interventor delegado y a la Unidad central; los **Interventores** pueden comprobar",
         "Estados de situación de tesorería referidos al último día del trimestre anterior; extraordinarios cuando lo acuerden los Jefes de Unidad",
         "Como mínimo, **trimestral**: primeras quincenas de **enero, abril, julio y octubre**",
         "No confundir: estados de tesorería **trimestrales** (art. 9) frente a cuenta **obligatoria en diciembre** (art. 7)."))}
""", 2)

T.ap("s15", "IV.2 Cuenta justificativa de los pagos a justificar (LGP, art. 79.4 a 6)", f"""
{unidad("2.1 Obligados, plazos y ampliación (LGP, art. 79.4)",
  lit("LGP", "Artículo 79", ["quedan obligados a rendir cuenta justificativa", "El plazo de rendición de las cuentas será de tres meses", "en el plazo de seis meses", "ampliar estos plazos a seis y doce meses respectivamente"], solo=[8]),
  fichab("Rendición de la cuenta justificativa",
         f"Rinden: {c('LGP', 'Artículo 79', 'Los perceptores de estas órdenes de pago a justificar')} · Pueden ampliar: el **Ministro** (o en quien delegue) y los presidentes o directores de organismos autónomos y de entidades gestoras y servicios comunes de la Seguridad Social, a propuesta del órgano gestor y con informe de la Intervención",
         "Cuenta justificativa de la aplicación de las cantidades recibidas",
         ["General: **tres meses**", "Expropiaciones y pagos en el extranjero: **seis meses**", "Ampliación excepcional: a **seis** y **doce** meses, respectivamente"],
         "**3** meses (regla) / **6** (expropiaciones y extranjero); ampliables **excepcionalmente** a **6** y **12**. Amplía el **Ministro**, no el Interventor."))}

{unidad("2.2 Responsables y aprobación de la cuenta (LGP, art. 79.5 y 6)",
  lit("LGP", "Artículo 79", ["son responsables", "de la custodia y uso de los fondos y de la rendición de la cuenta", "En el curso de los dos meses siguientes"], solo=[9, 10]),
  fichab("Responsabilidad del perceptor y aprobación o reparo",
         "Responsables: los **perceptores** de las órdenes de pago a justificar · Aprueba o repara: la **autoridad competente**",
         ["Los perceptores responden de la **custodia**, el **uso** de los fondos y la **rendición** de la cuenta", "Después se aprueba la cuenta o se pone reparo"],
         "Aprobación o reparo: en los **dos meses** siguientes a la aportación de los justificantes",
         "Cayó en 2025 (→ Cierre 1): el responsable es **el perceptor**, no el Ministro (que solo **amplía** plazos) ni el Subsecretario. **Dos meses** para aprobar o reparar."))}
""", 2)

T.ap("s16", "IV.3 Contabilidad, control y cuentas en el RD 640/1987 (arts. 8, 9, 10 y 12)", f"""
{unidad("3.1 Libro registro y estados de tesorería (RD 640/1987, arts. 8 y 9)",
  lit("RD640", "a8", ["Libro registro de órdenes de pago «a justificar»"], solo=[2, 3]),
  lit("RD640", "a9", ["en las primeras quincenas de los meses de enero, abril, julio y octubre"], solo=[1, 2, 3, 4]),
  fichab("Control de la situación de los fondos librados a justificar",
         "Oficinas de contabilidad (Libro registro, modelo de la IGAE); Jefes de Unidad y Cajeros (estados de tesorería); **Interventores Delegados** (comprobaciones)",
         ["Libro registro de órdenes de pago a justificar, clasificadas por ejercicios y cajas", "Estados de situación de tesorería, como mínimo trimestrales"],
         "Primeras quincenas de **enero, abril, julio y octubre**",
         "Los mismos meses que en la caja fija (→ IV.1.3)."))}

{unidad("3.2 Plazos del reglamento (RD 640/1987, art. 10)",
  lit("RD640", "a10", ["dentro del mes siguiente a la inversión de las mismas y en todo caso en el plazo de tres meses desde la percepción"], solo=[1, 2]),
  clave(f"**Aviso.** Este artículo es de 1987 y no coincide del todo con el art. 79.4 de la LGP de 2003 (→ IV.2.1): el reglamento atribuye la ampliación a {c('RD640', 'a10', 'El Director general del Tesoro y Política Financiera')}, mientras que la ley la atribuye al Ministro (o en quien delegue) y fija ampliaciones a seis y doce meses. La Constitución {c('CE', 'Artículo 9', 'garantiza el principio de legalidad, la jerarquía normativa')} (art. 9.3): el dato que se estudia es el de la **ley**."),
  fichab("Plazo reglamentario de justificación",
         "Los Cajeros pagadores",
         "Justifican dentro del mes siguiente a la inversión y, en todo caso, en tres meses desde la percepción",
         "**Tres meses** desde la percepción (coincide con la LGP)",
         "Coincide el plazo general de **tres meses**; para las ampliaciones, la LGP (art. 79.4)."))}

{unidad("3.3 La cuenta justificativa: forma y tramitación (RD 640/1987, art. 12)",
  lit("RD640", "a12", ["en el debe el importe percibido y en el haber el de las obligaciones satisfechas", "carta de pago demostrativa de su reintegro", "mediante procedimientos de auditoria o de muestreo", "la aprobación de las mismas por la autoridad que dispuso la expedición", "las enviará al Tribunal de Cuentas"], solo=[1, 2, 4, 5, 7, 8, 9]),
  fichab("Formación, intervención, aprobación y envío de la cuenta",
         "Forman y rinden: los **Cajeros pagadores** · Conforman: los **Jefes de las Unidades** · Interviene: la **Intervención Delegada** · Aprueba: **la autoridad que dispuso la expedición** · Destino: el **Tribunal de Cuentas**",
         ["Debe: importe percibido · Haber: obligaciones satisfechas", "Lo no invertido: carta de pago de su reintegro", "Facturas y documentos originales", "Intervención por auditoría o muestreo; la Unidad Central recaba la aprobación y la envía al Tribunal de Cuentas"],
         "—",
         "Aprueba **quien dispuso la expedición** de las órdenes de pago; el destino final es el **Tribunal de Cuentas**."))}
""", 2)

T.ap("s17", "IV.4 Fiscalización y responsabilidad (LGP, arts. 151, 153, 176 y 177)", f"""
{unidad("4.1 Gastos no sujetos a fiscalización previa (LGP, art. 151 c y último párrafo)",
  lit("LGP", "Artículo 151", ["los gastos menores de 5.000 euros cuyo pago se realice mediante el procedimiento especial de anticipo de caja fija", "Tampoco estarán sometidos a fiscalización previa los gastos menores de 5.000 euros que se realicen con cargo a fondos librados a justificar"], solo=[1, 4, 9]),
  fichab("Exención de fiscalización previa ligada a caja fija y a pagos a justificar en el extranjero",
         "La Intervención (función interventora, tema VI.4)",
         ["Gastos de menos de **5.000 €** pagados por **anticipo de caja fija**", "Gastos de menos de **5.000 €** con fondos a justificar para servicios o prestaciones **en el extranjero**"],
         "Umbral: **5.000 euros**",
         "En pagos a justificar, la exención es solo para gastos **en territorio extranjero**."))}

{unidad("4.2 Requisitos de fiscalización y de intervención de las cuentas (LGP, art. 153)",
  lit("LGP", "Artículo 153", ["Reglamentariamente se determinarán"]),
  fichab("Remisión al reglamento del control de pagos a justificar y anticipos de caja fija",
         "La norma reglamentaria a la que remite la ley",
         ["Requisitos de la fiscalización previa de las órdenes de pago a justificar", "Requisitos de la constitución, modificación y reposiciones de los anticipos de caja fija", "Procedimiento de intervención de sus cuentas justificativas"],
         "—",
         "La LGP no fija esos requisitos: los **remite al reglamento**."))}

{unidad("4.3 No justificar genera responsabilidad (LGP, arts. 176 y 177.1 e)",
  lit("LGP", "Artículo 176", ["por dolo o culpa graves", "estarán obligados a indemnizar"]),
  lit("LGP", "Artículo 177", ["No justificar la inversión de los fondos a los que se refieren los artículos 78 y 79 de esta ley"], solo=[1, 6, 8]),
  fichab("Responsabilidad patrimonial por no justificar",
         "Autoridades y demás personal que actúen con **dolo o culpa graves**",
         "No justificar la inversión de los fondos de los arts. **78** (caja fija) y **79** (a justificar) es una de las infracciones del art. 177",
         "—",
         "Obligación de **indemnizar** a la Hacienda Pública estatal, con independencia de la responsabilidad penal o disciplinaria. Exige **dolo o culpa graves**."))}
""", 2)

T.ap("s18", "IV.5 Cuadro comparativo: anticipo de caja fija y pago a justificar (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| | Anticipo de caja fija | Pago «a justificar» |
|---|---|---|
| Norma | LGP, art. 78; RD 725/1989 | LGP, art. 79; RD 640/1987 |
| Naturaleza | **Extrapresupuestario** y **permanente** | **Presupuestario**: se aplica al crédito al librarse |
| Para qué | Gastos **periódicos o repetitivos** del **capítulo 2** | Documentación no disponible antes del pago; extranjero; localidad sin dependencia |
| Límite | **7 %** del capítulo 2 (14 % AECI; 10 % del art. 23 en Interior 222A) | Créditos del ejercicio; calendario de actuaciones |
| Justificación | Cuentas para **reponer**; **necesariamente en diciembre** | Cuenta justificativa en **3 meses** (6 en expropiaciones y extranjero); ampliable a 6 y 12 |
| Aprobación | Jefes de las Unidades Administrativas | Autoridad competente, en **2 meses** (RD 640/1987: la que dispuso la expedición) |
| Fiscalización previa | No, para gastos de menos de **5.000 €** | Sí; no para gastos de menos de 5.000 € en el extranjero |
| No justificar | Responsabilidad (LGP, art. 177.1 e) | Responsabilidad (LGP, art. 177.1 e) |

{resumen([
  "Caja fija: cuentas cuando lo exija la tesorería y **necesariamente en diciembre**; aprueban los **Jefes de Unidad**; con lo justificado se **repone** el anticipo (RD 725/1989, art. 7).",
  "Pago a justificar: cuenta en **3 meses** (6 en expropiaciones y extranjero), ampliable por el **Ministro** a 6 y 12; responsables, los **perceptores**; aprobación o reparo en **2 meses** (LGP, art. 79.4 a 6).",
  "Estados de situación de tesorería: como mínimo en las primeras quincenas de **enero, abril, julio y octubre** (en los dos regímenes).",
  "No justificar la inversión de los fondos de los arts. 78 y 79 es **infracción** que obliga a indemnizar (LGP, art. 177.1 e)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_L95 = examen("L", 95, {
  "a": f"«Cuentadante» no es el término de la ley: el art. 79.5 hace responsables a {c('LGP', 'Artículo 79', 'Los perceptores de las órdenes de pago a justificar')}.",
  "b": f"El Ministro (o en quien delegue) y los presidentes o directores son quienes {c('LGP', 'Artículo 79', 'podrán, excepcionalmente, ampliar estos plazos')} de rendición (art. 79.4), no los responsables de los fondos.",
  "c": "El Subsecretario no aparece en el art. 79: la responsabilidad es del perceptor.",
  "d": f"Literal del art. 79.5: {c('LGP', 'Artículo 79', 'Los perceptores de las órdenes de pago a justificar son responsables, en los términos previstos en esta ley, de la custodia y uso de los fondos y de la rendición de la cuenta')}."},
  [("perceptor", "LGP", "Artículo 79", "Los perceptores de las órdenes de pago a justificar son responsables, en los términos previstos en esta ley, de la custodia y uso de los fondos y de la rendición de la cuenta")])
EX_P94 = examen("P", 94, {
  "a": f"Cambia «extrapresupuestario» por «presupuestario». El art. 1 dice {c('RD725', 'a1', 'de carácter extrapresupuestario y permanente')}: no se aplican al presupuesto al librarse (eso es propio del pago a justificar).",
  "b": f"Literal del art. 1 del RD 725/1989: {c('RD725', 'a1', 'Se entienden por anticipos de Caja fija las provisiones de fondos de carácter extrapresupuestario y permanente')}.",
  "c": f"Cambia los dos rasgos: ni «presupuestario» ni «temporal»; son {c('RD725', 'a1', 'de carácter extrapresupuestario y permanente')}.",
  "d": f"Cambia «permanente» por «temporal». El fondo es {c('RD725', 'a1', 'permanente')} y se repone a medida que se gasta (art. 7)."},
  [("carácter extrapresupuestario y permanente", "RD725", "a1", "provisiones de fondos de carácter extrapresupuestario y permanente")])
EX_P95 = examen("P", 95, {
  "a": f"Enero es uno de los meses de los estados de situación de tesorería ({c('RD725', 'a9', 'en las primeras quincenas de los meses de enero, abril, julio y octubre')}, art. 9), no de la rendición obligatoria de cuentas.",
  "b": "Marzo no aparece en el RD 725/1989.",
  "c": f"Octubre también es un mes de los estados de tesorería del art. 9 ({c('RD725', 'a9', 'enero, abril, julio y octubre')}), no de la rendición de cuentas.",
  "d": f"Literal del art. 7.1: {c('RD725', 'a7', 'necesariamente, en el mes de diciembre de cada año')}."},
  [("diciembre", "RD725", "a7", "necesariamente, en el mes de diciembre de cada año")])
EX_L96 = examen("L", 96, {
  "a": f"Literal del art. 43.1: {c('LGP', 'Artículo 43', 'las inversiones reales a nivel de capítulo')}.",
  "b": f"A nivel de artículo se especifican {c('LGP', 'Artículo 43', 'los créditos destinados a gastos de personal y los gastos corrientes en bienes y servicios')}, no las inversiones reales.",
  "c": f"El concepto es la regla general: {c('LGP', 'Artículo 43', 'los créditos se especificarán a nivel de concepto')}, salvo personal, bienes y servicios e inversiones reales.",
  "d": "El subconcepto no es nivel de especificación en el art. 43.1; es un desglose posible de los conceptos (art. 40.1 c)."},
  [("Capítulo", "LGP", "Artículo 43", "las inversiones reales a nivel de capítulo")])
EX_P87 = examen("P", 87, {
  "a": "El subconcepto no es nivel de especificación en el art. 43.1.",
  "b": f"El concepto es la regla general ({c('LGP', 'Artículo 43', 'los créditos se especificarán a nivel de concepto')}), pero el capítulo 2 es una de sus salvedades.",
  "c": f"Literal del art. 43.1: {c('LGP', 'Artículo 43', 'los gastos corrientes en bienes y servicios, que se especificarán a nivel de artículo')}.",
  "d": f"A nivel de capítulo se especifican solo {c('LGP', 'Artículo 43', 'las inversiones reales a nivel de capítulo')}."},
  [("Artículo", "LGP", "Artículo 43", "los gastos corrientes en bienes y servicios, que se especificarán a nivel de artículo")])
EX_L94 = examen("L", 94, {
  "a": f"El artículo 21 es otro artículo del capítulo 2: {c('RES2014', 'ai-2', '21. Reparaciones, mantenimiento y conservación')}.",
  "b": f"El artículo 12 es de gastos de personal (capítulo 1): {c('RES2014', 'ai-2', '12. Funcionarios')}.",
  "c": f"Literal del anexo II: {c('RES2014', 'ai-2', '23. Indemnizaciones por razón del servicio')}.",
  "d": f"El artículo 14 es {c('RES2014', 'ai-2', '14. Otro personal')} (capítulo 1)."},
  [("Artículo 23", "RES2014", "ai-2", "23. Indemnizaciones por razón del servicio")])
EX_P96 = examen("P", 96, {
  "a": f"El 12 es {c('RES2014', 'ai-2', '12. Funcionarios')} (capítulo 1, gastos de personal).",
  "b": f"Literal del anexo II: {c('RES2014', 'ai-2', '23. Indemnizaciones por razón del servicio')}.",
  "c": f"El 42 es una transferencia corriente: {c('RES2014', 'ai-2', '42. A la Seguridad Social')}.",
  "d": f"El 60 es una inversión real: {c('RES2014', 'ai-2', '60. Inversión nueva en infraestructura y bienes destinados al uso general')}."},
  [("23", "RES2014", "ai-2", "23. Indemnizaciones por razón del servicio")])

T.ap("s19", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **tres** preguntas de este tema (pagos a justificar y anticipos de caja fija) y **cuatro** relacionadas (nivel de especificación del art. 43 LGP y artículo 23 de la clasificación económica). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-L 2025, pregunta 95 · Responsables de los pagos a justificar (→ IV.2.2)", EX_L95,
  "### GACE-P 2025, pregunta 94 · Concepto de anticipo de caja fija (→ II.1.2)", EX_P94,
  "### GACE-P 2025, pregunta 95 · Rendición de cuentas de la caja fija (→ IV.1.2)", EX_P95,
  "### GACE-L 2025, pregunta 96 · Inversiones reales: nivel de capítulo (relacionada; → I.1.2)", EX_L96,
  "### GACE-P 2025, pregunta 87 · Bienes y servicios: nivel de artículo (relacionada; → I.1.2)", EX_P87,
  "### GACE-L 2025, pregunta 94 · Indemnizaciones por razón del servicio: artículo 23 (relacionada; → I.2.2)", EX_L94,
  "### GACE-P 2025, pregunta 96 · Indemnizaciones por razón del servicio: artículo 23 (relacionada; → I.2.2)", EX_P96,
  "### Pregunta con discrepancia",
  f"?> **GACE-L 2025 extraordinario, pregunta 96** (límite de los anticipos de caja fija imputables al artículo 23): no se incluye en estos apuntes. En el test real se mantiene la respuesta de la plantilla con la marca **Discrepancia**. La plantilla oficial da la b) («10% del total de créditos del capítulo destinado a gastos corrientes en bienes y servicios.»), pero el art. 78.3 LGP fija el límite general en {c('LGP', 'Artículo 78', 'el siete por ciento del total de créditos del capítulo destinado a gastos corrientes en bienes y servicios')} y el 10 % lo calcula sobre {c('LGP', 'Artículo 78', 'los créditos del artículo 23')} y solo para el programa 222A del Ministerio del Interior (→ II.2.1). Ninguna opción reproduce la ley.",
  "### Cómo se pregunta",
  "!> En caja fija y pagos a justificar los distractores cambian **una palabra** (presupuestario/extrapresupuestario, permanente/temporal), **un mes** (diciembre frente a enero, abril, julio y octubre), **un porcentaje** (7, 10, 14) o **un órgano** (el perceptor frente al Ministro). En la clasificación económica, el **número** del artículo o el **nivel** de especificación.",
]))

T.ap("s20", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Clasificación económica | Capítulos 2 (bienes y servicios), 4 (transferencias corrientes), 6 (inversiones reales) y 7 (transferencias de capital); art. 43 LGP | Bienes y servicios: nivel de **artículo**; inversiones reales: nivel de **capítulo**; indemnizaciones por razón del servicio: **artículo 23** |
| II. Anticipos de caja fija | Fondo **extrapresupuestario y permanente** para gastos periódicos o repetitivos del capítulo 2 | **7 %** del capítulo 2 (AECI 14 %; Interior 222A: 10 % del art. 23); pagos de más de **5.000 €** no |
| III. Pagos a justificar | Excepcionales; **presupuestarios**; extranjero y localidad sin dependencia; calendario obligatorio | Solo obligaciones **del ejercicio**; excepción del extranjero por **Consejo de Ministros** |
| IV. Justificación | Caja fija: cuentas y reposición; a justificar: cuenta justificativa; responsabilidad | Caja fija: **diciembre**; a justificar: **3 meses** (6), ampliables a 6 y 12; responsables, los **perceptores**; aprobación en **2 meses** |

?> **Trampas frecuentes:** «anticipo de caja fija **presupuestario**» o «**temporal**» (es **extrapresupuestario y permanente**); «límite del **10 %** del capítulo 2» (es el **7 %**; el 10 % es del **artículo 23** en Interior 222A); «cuentas de caja fija necesariamente en **enero**» (en **diciembre**; enero, abril, julio y octubre son los estados de tesorería); «el **Ministro** es responsable de la custodia» (lo son los **perceptores**; el Ministro **amplía** plazos); «inversiones reales a nivel de **concepto**» (a nivel de **capítulo**); «indemnizaciones por razón del servicio en el capítulo **1**» (capítulo **2**, artículo **23**).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
T.q("LGP", "Artículo 40", "Clasificación económica", "Según el artículo 40.1 c) de la Ley 47/2003, General Presupuestaria, en los créditos para operaciones de capital se distinguirán:",
    ["Las inversiones reales y las transferencias de capital.", "Los gastos corrientes en bienes y servicios y las inversiones reales.", "Las transferencias corrientes y las transferencias de capital.", "Los activos financieros y los pasivos financieros."],
    "Art. 40.1 c) LGP: «En los créditos para operaciones de capital se distinguirán las inversiones reales y las transferencias de capital». Bienes y servicios y transferencias corrientes son operaciones corrientes; activos y pasivos, financieras.", "En los créditos para operaciones de capital se distinguirán las inversiones reales y las transferencias de capital")
T.q("LGP", "Artículo 40", "Clasificación económica", "Según el artículo 40.1 c) de la Ley General Presupuestaria, en los créditos para operaciones corrientes se distinguirán los gastos de personal, los gastos corrientes en bienes y servicios, los gastos financieros y:",
    ["Las transferencias corrientes.", "Las inversiones reales.", "Las transferencias de capital.", "El Fondo de Contingencia."],
    "Art. 40.1 c) LGP.", "En los créditos para operaciones corrientes se distinguirán los gastos de personal, los gastos corrientes en bienes y servicios, los gastos financieros y las transferencias corrientes")
T.q("LGP", "Artículo 43", "Clasificación económica", "Según el artículo 43.1 de la Ley General Presupuestaria, en el presupuesto del Estado los créditos para inversiones reales se especificarán a nivel de:",
    ["Capítulo.", "Artículo.", "Concepto.", "Subconcepto."], "Art. 43.1 LGP: «las inversiones reales a nivel de capítulo».", "las inversiones reales a nivel de capítulo")
T.q("LGP", "Artículo 43", "Clasificación económica", "Según el artículo 43.1 de la Ley General Presupuestaria, en el presupuesto del Estado los créditos para gastos corrientes en bienes y servicios se especificarán a nivel de:",
    ["Artículo.", "Capítulo.", "Concepto.", "Subconcepto."], "Art. 43.1 LGP: bienes y servicios (y personal) a nivel de artículo.", "los gastos corrientes en bienes y servicios, que se especificarán a nivel de artículo")
T.q("LGP", "Artículo 43", "Clasificación económica", "Según el artículo 43.1 de la Ley General Presupuestaria, como regla general los créditos del presupuesto del Estado se especificarán a nivel de:",
    ["Concepto.", "Capítulo.", "Artículo.", "Subconcepto."], "Art. 43.1 LGP: «En el presupuesto del Estado los créditos se especificarán a nivel de concepto, salvo…».", "En el presupuesto del Estado los créditos se especificarán a nivel de concepto")
T.q("RES2014", "ai-4", "Bienes y servicios", "Según el código de la clasificación económica de los gastos (Resolución de 20 de enero de 2014, anexo IV), el capítulo 2 recoge los gastos corrientes en bienes y servicios necesarios para el ejercicio de las actividades:",
    ["Que no originen un aumento de capital o del patrimonio público.", "Que originen un aumento del patrimonio público.", "Que sean susceptibles de amortización.", "Que se realicen sin contrapartida directa."],
    "Anexo IV, capítulo 2: «que no originen un aumento de capital o del patrimonio público». Lo amortizable es capítulo 6; sin contrapartida, capítulos 4 y 7.", "que no originen un aumento de capital o del patrimonio público")
T.q("RES2014", "ai-4", "Bienes y servicios", "Según el anexo IV de la Resolución de 20 de enero de 2014, NO es una de las características de los bienes cuya adquisición se imputa al capítulo 2:",
    ["Ser susceptibles de inclusión en inventario.", "Ser bienes fungibles.", "Tener una duración previsiblemente inferior al ejercicio presupuestario.", "Ser, previsiblemente, gastos reiterativos."],
    "Anexo IV, capítulo 2: la característica es «No ser susceptibles de inclusión en inventario». Lo inventariable va al capítulo 6.", "c) No ser susceptibles de inclusión en inventario")
T.q("RES2014", "ai-4", "Bienes y servicios", "Según el anexo IV de la Resolución de 20 de enero de 2014, las grandes reparaciones que supongan un alargamiento de la vida útil del bien se imputarán, como norma general:",
    ["Al capítulo 6.", "Al artículo 21 del capítulo 2.", "Al capítulo 7.", "Al artículo 22 del capítulo 2."],
    "Anexo IV, artículo 21: «las grandes reparaciones que supongan un incremento de la productividad, capacidad, rendimiento, eficiencia o alargamiento de la vida útil del bien se imputarán al capítulo 6».", "alargamiento de la vida útil del bien se imputarán al capítulo 6")
T.q("RES2014", "ai-2", "Bienes y servicios", "Según el anexo II de la Resolución de 20 de enero de 2014, el artículo 22 de la clasificación económica del gasto corresponde a:",
    ["Material, suministros y otros.", "Arrendamientos y cánones.", "Reparaciones, mantenimiento y conservación.", "Indemnizaciones por razón del servicio."],
    "Anexo II: 20 arrendamientos y cánones; 21 reparaciones; 22 material, suministros y otros; 23 indemnizaciones por razón del servicio.", "22. Material, suministros y otros")
T.q("RES2014", "ai-2", "Bienes y servicios", "Según el anexo II de la Resolución de 20 de enero de 2014, el concepto 230 del capítulo 2 corresponde a:",
    ["Dietas.", "Locomoción.", "Traslado.", "Otras indemnizaciones."], "Anexo II: 230 Dietas; 231 Locomoción; 232 Traslado; 233 Otras indemnizaciones.", "230. Dietas")
T.q("RES2014", "ai-4", "Inversiones reales", "Según el anexo IV de la Resolución de 20 de enero de 2014, un gasto se considerará amortizable cuando:",
    ["Contribuya al mantenimiento de la actividad del sujeto que lo realiza en ejercicios futuros.", "Tenga una duración previsiblemente inferior al ejercicio presupuestario.", "Se realice sin contrapartida directa por parte del receptor.", "Sea previsiblemente reiterativo."],
    "Anexo IV, capítulo 6. Las otras opciones describen el capítulo 2 o las transferencias.", "Un gasto se considerará amortizable cuando contribuya al mantenimiento de la actividad del sujeto que lo realiza en ejercicios futuros")
T.q("RES2014", "ai-4", "Inversiones reales", "Según el anexo IV de la Resolución de 20 de enero de 2014, las inversiones en infraestructura y bienes destinados al uso general que incrementen el stock de capital público se imputan al artículo:",
    ["60.", "61.", "62.", "64."], "Anexo IV: artículo 60, inversión nueva en infraestructura y bienes destinados al uso general. El 61 es de reposición; el 62, asociada al funcionamiento operativo; el 64, inmaterial.", "Se incluyen en este artículo aquellas inversiones en infraestructura y bienes destinados al uso general que incrementen el stock de capital público")
T.q("RES2014", "ai-2", "Inversiones reales", "Según el anexo II de la Resolución de 20 de enero de 2014, el artículo 63 de la clasificación económica del gasto es:",
    ["Inversión de reposición asociada al funcionamiento operativo de los servicios.", "Inversión nueva asociada al funcionamiento operativo de los servicios.", "Inversión de reposición en infraestructura y bienes destinados al uso general.", "Gastos de inversiones de carácter inmaterial."],
    "Anexo II: 62 nueva y 63 de reposición, asociadas al funcionamiento operativo; 61 reposición de uso general; 64 inmaterial.", "63. Inversión de reposición asociada al funcionamiento operativo de los servicios")
T.q("RES2014", "ai-4", "Transferencias", "Según el anexo IV de la Resolución de 20 de enero de 2014, se aplican al capítulo 4 los pagos efectuados sin contrapartida directa por parte de los agentes receptores, los cuales destinan estos fondos a financiar:",
    ["Gastos de naturaleza corriente.", "Operaciones de capital.", "Inversiones reales de la propia Administración.", "Activos financieros."],
    "Anexo IV, capítulo 4: «a financiar gastos de naturaleza corriente». Si financian operaciones de capital, capítulo 7.", "los cuales destinan estos fondos a financiar gastos de naturaleza corriente")
T.q("RES2014", "ai-4", "Transferencias", "Según el anexo IV de la Resolución de 20 de enero de 2014, las transferencias de capital del capítulo 7 son pagos:",
    ["Condicionados o no, sin contrapartida directa por parte de los agentes receptores.", "Siempre condicionados, con contrapartida directa del receptor.", "Destinados a la adquisición directa de bienes inventariables por la Administración.", "Destinados exclusivamente a otras Administraciones Públicas."],
    "Anexo IV, capítulo 7: «Pagos, condicionados o no, … sin contrapartida directa por parte de los agentes receptores, los cuales destinan estos fondos a financiar operaciones de capital».", ["Pagos, condicionados o no", "sin contrapartida directa por parte de los agentes receptores, los cuales destinan estos fondos a financiar operaciones de capital"])
T.q("RES2014", "ai-4", "Transferencias", "Según el anexo IV de la Resolución de 20 de enero de 2014, las transferencias y subvenciones, tanto dinerarias como en especie, se imputarán en función:",
    ["Del beneficiario final de las mismas.", "Del órgano que las concede.", "Del programa de gasto del que procedan.", "De su importe."], "Anexo IV, capítulos 4 y 7.", "se imputarán en función del beneficiario final de las mismas")
T.q("RES2014", "ai-4", "Transferencias", "Según el anexo IV de la Resolución de 20 de enero de 2014, las prestaciones sociales que comprenden pensiones a funcionarios y familias, de carácter civil y militar, se aplican al capítulo:",
    ["4.", "1.", "2.", "7."], "Anexo IV, capítulo 4: «Prestaciones sociales, que comprenden pensiones a funcionarios y familias, de carácter civil y militar».", "Prestaciones sociales, que comprenden pensiones a funcionarios y familias, de carácter civil y militar")
T.q("RES2014", "ai-4", "Transferencias", "Según el anexo IV de la Resolución de 20 de enero de 2014, las cuotas y contribuciones a organismos internacionales se imputan, en el capítulo 4, al artículo:",
    ["49 «Al exterior».", "48 «A familias e instituciones sin fines de lucro».", "44 «A sociedades, entidades públicas empresariales, fundaciones y resto de entes del sector público».", "40 «A la Administración del Estado»."],
    "Anexo IV, artículo 49: «A este artículo se imputarán también las cuotas y contribuciones a organismos internacionales».", "A este artículo se imputarán también las cuotas y contribuciones a organismos internacionales")
T.q("RES2014", "ai-2", "Transferencias", "Según el anexo II de la Resolución de 20 de enero de 2014, el artículo 75 de la clasificación económica del gasto corresponde a transferencias de capital:",
    ["A Comunidades Autónomas.", "A Entidades Locales.", "A empresas privadas.", "Al exterior."], "Anexo II: 75 A Comunidades Autónomas; 76 A Entidades Locales; 77 A empresas privadas; 79 Al exterior.", "75. A Comunidades Autónomas")
T.q("LGP", "Artículo 78", "Anticipos de caja fija", "Según el artículo 78.1 de la Ley General Presupuestaria, se entienden por anticipos de caja fija las provisiones de fondos de carácter:",
    ["Extrapresupuestario y permanente.", "Presupuestario y permanente.", "Extrapresupuestario y temporal.", "Presupuestario y temporal."], "Art. 78.1 LGP (y art. 1 RD 725/1989).", "provisiones de fondos de carácter extrapresupuestario y permanente")
T.q("LGP", "Artículo 78", "Anticipos de caja fija", "Según el artículo 78.1 de la Ley General Presupuestaria, los anticipos de caja fija se destinan a la atención inmediata y posterior aplicación al capítulo de:",
    ["Gastos corrientes en bienes y servicios.", "Gastos de personal.", "Inversiones reales.", "Transferencias corrientes."], "Art. 78.1 LGP.", "posterior aplicación al capítulo de gastos corrientes en bienes y servicios del presupuesto del año en que se realicen")
T.q("LGP", "Artículo 78", "Anticipos de caja fija", "Según el artículo 78.1 de la Ley General Presupuestaria, las normas que regulan los pagos satisfechos mediante anticipos de caja fija las establecen los ministros y los presidentes o directores de los organismos autónomos, previo informe de:",
    ["Su Intervención Delegada.", "La Dirección General del Tesoro.", "El Tribunal de Cuentas.", "La Dirección General de Presupuestos."], "Art. 78.1 LGP: «previo informe de su Intervención Delegada en ambos casos».", "previo informe de su Intervención Delegada en ambos casos")
T.q("LGP", "Artículo 78", "Anticipos de caja fija", "Según el artículo 78.3 de la Ley General Presupuestaria, la cuantía global de los anticipos de caja fija no podrá superar para cada ministerio u organismo autónomo:",
    ["El siete por ciento del total de créditos del capítulo destinado a gastos corrientes en bienes y servicios del presupuesto vigente en cada momento.", "El diez por ciento del total de créditos del capítulo destinado a gastos corrientes en bienes y servicios.", "El siete por ciento del total de créditos de su presupuesto de gastos.", "El catorce por ciento del total de créditos del capítulo destinado a gastos corrientes en bienes y servicios."],
    "Art. 78.3 LGP. El 14 % es solo para la Agencia Española de Cooperación Internacional.", "el siete por ciento del total de créditos del capítulo destinado a gastos corrientes en bienes y servicios del presupuesto vigente en cada momento")
T.q("LGP", "Artículo 78", "Anticipos de caja fija", "Según el artículo 78.3 de la Ley General Presupuestaria, ¿qué organismo está autorizado para que la cuantía global de sus anticipos de caja fija exceda del siete por ciento, hasta un máximo del 14 por ciento?",
    ["La Agencia Española de Cooperación Internacional.", "La Agencia Estatal de Administración Tributaria.", "El Ministerio de Defensa.", "La Tesorería General de la Seguridad Social."], "Art. 78.3 LGP, párrafo segundo.", "Se autoriza a la Agencia Española de Cooperación Internacional para que la cuantía global de los anticipos de caja fija pueda exceder del siete por ciento")
T.q("LGP", "Artículo 78", "Anticipos de caja fija", "Según el artículo 78.4 de la Ley General Presupuestaria, la cuantía global de los fondos de maniobra asignados a los centros de gestión de una misma entidad de la Seguridad Social no podrá exceder del:",
    ["Tres por ciento de los créditos del capítulo destinado a gastos corrientes de bienes y servicios.", "Siete por ciento de los créditos del capítulo destinado a gastos corrientes de bienes y servicios.", "Diez por ciento de los créditos del artículo 23.", "Dos y medio por ciento de los créditos de inversiones reales."],
    "Art. 78.4 LGP: tres por ciento, elevable hasta un siete por ciento por el Ministro.", "no podrá exceder del tres por ciento de los créditos del capítulo destinado a gastos corrientes de bienes y servicios")
T.q("LGP", "Disposición adicional quinta", "Anticipos de caja fija", "Según la disposición adicional quinta de la Ley General Presupuestaria, el anticipo de caja fija para adquisiciones de material militar y servicios complementarios del Ministerio de Defensa en el exterior no podrá exceder del:",
    ["2,5 por ciento del total de los créditos de inversiones reales del Presupuesto de Gastos de dicho ministerio.", "7 por ciento del total de los créditos del capítulo 2 de dicho ministerio.", "2,5 por ciento del total de los créditos del capítulo 2 de dicho ministerio.", "10 por ciento del total de los créditos de inversiones reales de dicho ministerio."],
    "Disp. adicional quinta.3 LGP.", "no podrá exceder del 2,5 por ciento del total de los créditos de inversiones reales del Presupuesto de Gastos de dicho ministerio")
T.q("RD725", "a2", "Anticipos de caja fija", "Según el artículo 2 del Real Decreto 725/1989, sobre anticipos de Caja fija, no podrán realizarse con cargo al anticipo pagos individualizados superiores a 5.000 euros, excepto los destinados a:",
    ["Gastos de teléfono, energía eléctrica, combustibles o indemnizaciones por razón del servicio.", "Material de oficina no inventariable.", "Arrendamientos de edificios.", "Reparaciones de inmuebles."], "Art. 2.3 RD 725/1989.", "excepto los destinados a gastos de teléfono, energía eléctrica, combustibles o indemnizaciones por razón del servicio")
T.q("RD725", "a2", "Anticipos de caja fija", "Según el artículo 2.3 del Real Decreto 725/1989, cuando el sistema de anticipos de caja fija se haya establecido en un Ministerio u Organismo autónomo, no podrán tramitarse libramientos aplicados al presupuesto a favor de perceptores directos, excepto los de reposición del anticipo, por importe inferior a:",
    ["600 euros.", "5.000 euros.", "3.000 euros.", "1.000 euros."], "Art. 2.3 RD 725/1989.", "por importe inferior a 600 euros")
T.q("RD725", "a3", "Anticipos de caja fija", "Según el artículo 3 del Real Decreto 725/1989, los acuerdos de distribución de los anticipos de caja fija por Cajas pagadoras habrán de ser objeto de informe favorable del Interventor delegado, circunscrito a:",
    ["Que se respete el límite del 7 por 100.", "La adecuación del crédito.", "La existencia de justificantes de los pagos anteriores.", "La oportunidad del gasto."], "Art. 3.2 RD 725/1989.", "circunscrito a que se respete el citado límite del 7 por 100")
T.q("RD725", "a6", "Anticipos de caja fija", "Según el artículo 6 del Real Decreto 725/1989, las disposiciones de fondos de las cuentas de los anticipos de caja fija se autorizarán con las firmas:",
    ["Mancomunadas del Cajero pagador y del funcionario que designe el Jefe de la Unidad Administrativa a la que esté adscrita la Caja pagadora.", "Del Cajero pagador, exclusivamente.", "Del Interventor delegado y del Cajero pagador.", "Del Jefe de la Unidad Administrativa, exclusivamente."], "Art. 6.1 RD 725/1989.", "autorizados con las firmas mancomunadas del Cajero pagador y del funcionario que designe el Jefe de la Unidad Administrativa a la que esté adscrita la Caja pagadora")
T.q("LGP", "Artículo 79", "Pagos a justificar", "Según el artículo 79.1 de la Ley General Presupuestaria, podrán tramitarse propuestas de pagos presupuestarios y librarse fondos con el carácter de a justificar cuando:",
    ["Excepcionalmente, no pueda aportarse la documentación justificativa de las obligaciones en el momento previsto en el apartado 4 del artículo 73.", "Se trate de gastos periódicos o repetitivos del capítulo 2.", "El importe del gasto sea inferior a 5.000 euros.", "Lo solicite el acreedor de la Administración."],
    "Art. 79.1 LGP. Los gastos periódicos o repetitivos son los de la caja fija (art. 78).", "Cuando, excepcionalmente, no pueda aportarse la documentación justificativa de las obligaciones en el momento previsto en el apartado 4 del artículo 73")
T.q("LGP", "Artículo 79", "Pagos a justificar", "Según el artículo 79.3 de la Ley General Presupuestaria, ¿quién podrá acordar que, con los fondos librados a justificar para gastos en el extranjero imputados a un presupuesto, sean atendidos gastos realizados en el ejercicio siguiente?",
    ["El Consejo de Ministros.", "El Ministro de Hacienda.", "La Intervención General de la Administración del Estado.", "El Director General del Tesoro."], "Art. 79.3 LGP.", "No obstante el Consejo de Ministros podrá acordar que, con los fondos librados a justificar para gastos en el extranjero imputados a un presupuesto, sean atendidos gastos realizados en el ejercicio siguiente")
T.q("LGP", "Artículo 79", "Pagos a justificar", "Según el artículo 79.3 de la Ley General Presupuestaria, en todas las propuestas de pago a justificar, cualquiera que sea su finalidad, será obligatorio incluir:",
    ["Un calendario de las actuaciones que se pretenda financiar con el correspondiente libramiento.", "Un informe previo del Tribunal de Cuentas.", "La autorización del Consejo de Ministros.", "Las facturas de los gastos que se vayan a atender."], "Art. 79.3 LGP, párrafo segundo.", "se incluya un calendario de las actuaciones que se pretenda financiar con el correspondiente libramiento")
T.q("LGP", "Artículo 79", "Pagos a justificar", "Según el artículo 79.3 de la Ley General Presupuestaria, la cantidad no invertida de los libramientos a justificar en el ejercicio en que se aprobaran será justificada:",
    ["Mediante carta de pago demostrativa de su reintegro al tesoro público por el cajero pagador correspondiente.", "Mediante certificado del Interventor delegado.", "Con su incorporación automática al ejercicio siguiente.", "Mediante declaración responsable del perceptor."], "Art. 79.3 LGP, último párrafo.", "será justificada mediante carta de pago demostrativa de su reintegro al tesoro público por el cajero pagador correspondiente")
T.q("RD640", "a7", "Pagos a justificar", "Según el artículo 7.2 del Real Decreto 640/1987, sobre pagos librados «a justificar», las cantidades de efectivo que se autoricen en las Cajas pagadoras no podrán exceder:",
    ["De los pagos que se prevea realizar durante un mes.", "De los pagos que se prevea realizar durante un trimestre.", "De 5.000 euros.", "Del 7 por 100 de los créditos del capítulo 2."], "Art. 7.2 RD 640/1987.", "no podrán exceder de los pagos que se prevea realizar durante un mes")
T.q("RD640", "a1", "Pagos a justificar", "Según el artículo 1.3 del Real Decreto 640/1987, no se podrán expedir órdenes de pago «a justificar» a favor de las Cajas pagadoras cuando:",
    ["Transcurridos los plazos reglamentarios o los de prórroga, no se haya justificado la inversión de los fondos percibidos con anterioridad.", "Su importe supere el 7 por 100 de los créditos del capítulo 2.", "Los gastos se vayan a realizar en el extranjero.", "No exista dependencia del ministerio en la localidad."], "Art. 1.3 RD 640/1987.", "cuando transcurridos los plazos reglamentarios o los de prórroga, en su caso, no se haya justificado la inversión de los fondos percibidos con anterioridad")
T.q("LGP", "Artículo 79", "Justificación", "Según el artículo 79.4 de la Ley General Presupuestaria, con carácter general el plazo de rendición de las cuentas de los pagos a justificar será de:",
    ["Tres meses.", "Seis meses.", "Un mes.", "Dos meses."], "Art. 79.4 LGP: tres meses; seis para expropiaciones y pagos en el extranjero.", "El plazo de rendición de las cuentas será de tres meses")
T.q("LGP", "Artículo 79", "Justificación", "Según el artículo 79.4 de la Ley General Presupuestaria, las cuentas correspondientes a pagos de expropiaciones y pagos en el extranjero podrán ser rendidas en el plazo de:",
    ["Seis meses.", "Tres meses.", "Doce meses.", "Dos meses."], "Art. 79.4 LGP.", "excepto las correspondientes a pagos de expropiaciones y pagos en el extranjero que podrán ser rendidas en el plazo de seis meses")
T.q("LGP", "Artículo 79", "Justificación", "Según el artículo 79.4 de la Ley General Presupuestaria, el Ministro, o en quien éste delegue, podrá excepcionalmente ampliar los plazos de rendición de las cuentas de los pagos a justificar:",
    ["A seis y doce meses respectivamente.", "A cuatro y ocho meses respectivamente.", "A seis meses en todo caso.", "A doce y veinticuatro meses respectivamente."], "Art. 79.4 LGP.", "podrán, excepcionalmente, ampliar estos plazos a seis y doce meses respectivamente")
T.q("LGP", "Artículo 79", "Justificación", "Según el artículo 79.6 de la Ley General Presupuestaria, la aprobación o reparo de la cuenta de un pago a justificar se llevará a cabo por la autoridad competente en el curso de:",
    ["Los dos meses siguientes a la fecha de aportación de los documentos justificativos.", "Los tres meses siguientes a la fecha de aportación de los documentos justificativos.", "El mes siguiente a la percepción de los fondos.", "Los seis meses siguientes al libramiento."], "Art. 79.6 LGP.", "En el curso de los dos meses siguientes a la fecha de aportación de los documentos justificativos")
T.q("RD725", "a7", "Justificación", "Según el artículo 7.2 del Real Decreto 725/1989, las cuentas de los gastos atendidos con anticipos de caja fija serán aprobadas por:",
    ["Los Jefes de las Unidades Administrativas a las que las Cajas estén adscritas.", "El Interventor delegado.", "El Tribunal de Cuentas.", "El Director General del Tesoro y Política Financiera."], "Art. 7.2 RD 725/1989. La Intervención las examina (7.4) y el destino final es el Tribunal de Cuentas.", "serán aprobadas por los Jefes de las Unidades Administrativas a las que las Cajas estén adscritas")
T.q("RD725", "a9", "Justificación", "Según el artículo 9 del Real Decreto 725/1989, los estados de situación de Tesorería de las Cajas pagadoras se formularán, como mínimo, en las primeras quincenas de los meses de:",
    ["Enero, abril, julio y octubre.", "Marzo, junio, septiembre y diciembre.", "Enero y julio.", "Diciembre de cada año."], "Art. 9.1 RD 725/1989. Diciembre es el mes de la rendición obligatoria de cuentas (art. 7.1).", "en las primeras quincenas de los meses de enero, abril, julio y octubre")
T.q("RD640", "a12", "Justificación", "Según el artículo 12 del Real Decreto 640/1987, en las cuentas justificativas de la inversión de los fondos librados a justificar figurará:",
    ["En el debe el importe percibido y en el haber el de las obligaciones satisfechas.", "En el debe las obligaciones satisfechas y en el haber el importe percibido.", "Solo el importe de las obligaciones satisfechas.", "Solo el saldo no invertido."], "Art. 12.1 RD 640/1987.", "figurará en el debe el importe percibido y en el haber el de las obligaciones satisfechas con cargo a aquél")
T.q("LGP", "Artículo 151", "Justificación", "Según el artículo 151 de la Ley General Presupuestaria, no están sometidos a fiscalización previa los gastos cuyo pago se realice mediante el procedimiento especial de anticipo de caja fija cuando sean menores de:",
    ["5.000 euros.", "3.000 euros.", "6.000 euros.", "600 euros."], "Art. 151 c) LGP.", "los gastos menores de 5.000 euros cuyo pago se realice mediante el procedimiento especial de anticipo de caja fija")
T.q("LGP", "Artículo 177", "Justificación", "Según el artículo 177.1 de la Ley General Presupuestaria, constituye una infracción que puede generar responsabilidad patrimonial:",
    ["No justificar la inversión de los fondos a los que se refieren los artículos 78 y 79 de esta ley.", "Solicitar la ampliación del plazo de rendición de una cuenta justificativa.", "Constituir un anticipo de caja fija por debajo del 7 por ciento.", "Librar fondos a justificar para gastos en el extranjero."], "Art. 177.1 e) LGP.", "No justificar la inversión de los fondos a los que se refieren los artículos 78 y 79 de esta ley")
T.real("L", 95, "Justificación"); T.real("P", 94, "Anticipos de caja fija"); T.real("P", 95, "Justificación")
T.real("L", 96, "Clasificación económica")

# Flashcards
for q_, a_, cat in [
  ("Operaciones corrientes y de capital en la clasificación económica (LGP, art. 40.1 c)", "Corrientes: personal, bienes y servicios, gastos financieros y transferencias corrientes. De capital: inversiones reales y transferencias de capital.", "Clasificación económica"),
  ("Nivel de especificación en el presupuesto del Estado (LGP, art. 43.1)", "Regla: concepto. Personal y bienes y servicios: artículo. Inversiones reales: capítulo.", "Clasificación económica"),
  ("Características de los bienes del capítulo 2 (Resolución de 20-1-2014, anexo IV)", "Alguna de estas: fungibles; duración previsiblemente inferior al ejercicio; no inventariables; previsiblemente reiterativos.", "Bienes y servicios"),
  ("Artículos del capítulo 2", "20 Arrendamientos y cánones · 21 Reparaciones, mantenimiento y conservación · 22 Material, suministros y otros · 23 Indemnizaciones por razón del servicio · 24 Gastos de publicaciones · 25 Conciertos de asistencia sanitaria · 27 Compras, suministros y otros gastos relacionados con la actividad.", "Bienes y servicios"),
  ("¿Dónde se imputan las grandes reparaciones que alargan la vida útil del bien?", "Al capítulo 6, como norma general (anexo IV, artículo 21).", "Bienes y servicios"),
  ("¿Qué es el capítulo 6?", "Inversiones reales: gastos realizados directamente por la Administración para crear o adquirir bienes de capital, bienes inventariables y gastos inmateriales amortizables.", "Inversiones reales"),
  ("Artículos 60 a 64", "60 nueva y 61 reposición (uso general); 62 nueva y 63 reposición (funcionamiento operativo); 64 inmaterial.", "Inversiones reales"),
  ("Capítulo 4 frente a capítulo 7", "Ambos: pagos sin contrapartida directa. El 4 financia gastos corrientes del receptor; el 7, operaciones de capital.", "Transferencias"),
  ("¿En función de qué se imputan las transferencias y subvenciones?", "Del beneficiario final.", "Transferencias"),
  ("Concepto de anticipo de caja fija (LGP, art. 78.1; RD 725/1989, art. 1)", "Provisión de fondos extrapresupuestaria y permanente a pagadurías, cajas y habilitaciones, para gastos periódicos o repetitivos del capítulo 2 del año.", "Anticipos de caja fija"),
  ("¿Quién dicta las normas de los anticipos de caja fija?", "Los ministros y los presidentes o directores de los organismos autónomos, previo informe de su Intervención Delegada (LGP, art. 78.1).", "Anticipos de caja fija"),
  ("Límites de los anticipos de caja fija (LGP, art. 78.3)", "7 % del capítulo 2; AECI hasta el 14 %; Interior (programa 222A) hasta el 10 % de los créditos del artículo 23.", "Anticipos de caja fija"),
  ("Fondos de maniobra de la Seguridad Social (LGP, art. 78.4)", "Hasta el 3 % del capítulo 2; elevable al 7 % por el «Ministro de Trabajo y Asuntos Sociales» (así lo nombra la ley).", "Anticipos de caja fija"),
  ("Límites por pago (RD 725/1989, art. 2.3)", "No libramientos directos de menos de 600 €; no pagos por caja fija de más de 5.000 €, salvo teléfono, energía eléctrica, combustibles e indemnizaciones por razón del servicio.", "Anticipos de caja fija"),
  ("¿Cuándo se rinden las cuentas de caja fija? (RD 725/1989, art. 7.1)", "Cuando lo aconseje la tesorería y, necesariamente, en diciembre.", "Justificación"),
  ("Supuestos de pagos a justificar (LGP, art. 79.1 y 2)", "Documentación no disponible antes del reconocimiento de la obligación; servicios en el extranjero; gastos en localidad sin dependencia.", "Pagos a justificar"),
  ("Pagos a justificar: ¿a qué ejercicio?", "Solo obligaciones realizadas y exigibles en el ejercicio del libramiento; para el extranjero, el Consejo de Ministros puede permitir gastos del ejercicio siguiente (LGP, art. 79.3).", "Pagos a justificar"),
  ("Plazo de rendición de la cuenta justificativa (LGP, art. 79.4)", "Tres meses; seis en expropiaciones y pagos en el extranjero; ampliables excepcionalmente a seis y doce meses.", "Justificación"),
  ("¿Quién responde de la custodia y uso de los fondos a justificar? (LGP, art. 79.5)", "Los perceptores de las órdenes de pago a justificar.", "Justificación"),
  ("Plazo para aprobar o reparar la cuenta (LGP, art. 79.6)", "Dos meses desde la aportación de los documentos justificativos.", "Justificación"),
  ("Fiscalización previa y caja fija (LGP, art. 151 c)", "No se fiscalizan previamente los gastos de menos de 5.000 € pagados por anticipo de caja fija.", "Justificación"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Clasificación económica", "Clasificación de los créditos por capítulos que separa operaciones corrientes, de capital, financieras y el Fondo de Contingencia (LGP, art. 40.1 c).", "s1", "Clasificación económica")
T.glos("Gastos corrientes en bienes y servicios", "Capítulo 2: gastos necesarios para la actividad que no originan un aumento de capital o del patrimonio público.", "s2", "Bienes y servicios")
T.glos("Indemnizaciones por razón del servicio", "Artículo 23 del capítulo 2: dietas, locomoción, traslado y otras indemnizaciones.", "s2", "Bienes y servicios")
T.glos("Inversiones reales", "Capítulo 6: gastos realizados directamente por la Administración para crear o adquirir bienes de capital, bienes inventariables y gastos inmateriales amortizables.", "s3", "Inversiones reales")
T.glos("Gasto amortizable", "El que contribuye al mantenimiento de la actividad del sujeto que lo realiza en ejercicios futuros (anexo IV, capítulo 6).", "s3", "Inversiones reales")
T.glos("Transferencias corrientes", "Capítulo 4: pagos sin contrapartida directa con los que el receptor financia gastos de naturaleza corriente.", "s4", "Transferencias")
T.glos("Transferencias de capital", "Capítulo 7: pagos sin contrapartida directa con los que el receptor financia operaciones de capital.", "s4", "Transferencias")
T.glos("Anticipo de caja fija", "Provisión de fondos extrapresupuestaria y permanente a pagadurías, cajas y habilitaciones para gastos periódicos o repetitivos del capítulo 2 (LGP, art. 78).", "s6", "Anticipos de caja fija")
T.glos("Fondo de maniobra", "Equivalente del anticipo de caja fija en las entidades gestoras y servicios comunes de la Seguridad Social (LGP, art. 78.2 y 4).", "s7", "Anticipos de caja fija")
T.glos("Pago a justificar", "Libramiento presupuestario de fondos sin la documentación justificativa previa, en los supuestos del art. 79 LGP.", "s10", "Pagos a justificar")
T.glos("Caja pagadora", "Unidad a favor de la cual se expiden las órdenes de pago a justificar, con un Cajero pagador nombrado expresamente (RD 640/1987, art. 4).", "s12", "Pagos a justificar")
T.glos("Cuenta justificativa", "Cuenta que rinden los perceptores de fondos a justificar sobre su aplicación: debe, importe percibido; haber, obligaciones satisfechas (LGP, art. 79.4; RD 640/1987, art. 12).", "s15", "Justificación")
T.glos("Carta de pago", "Documento que justifica el reintegro al Tesoro de la cantidad no invertida (LGP, art. 79.3; RD 640/1987, art. 12).", "s11", "Justificación")

# Cronología (fechas de los metadatos del BOE)
T.hito("1987", "Real Decreto 640/1987, de 8 de mayo, sobre pagos librados «a justificar» (BOE de 21-5-1987)", "Desarrollo reglamentario de los pagos a justificar", "normativo", "s12")
T.hito("1989", "Real Decreto 725/1989, de 16 de junio, sobre anticipos de Caja fija (BOE de 24-6-1989)", "Los anticipos de caja fija dejan de ser pagos a justificar: operaciones extrapresupuestarias", "normativo", "s6")
T.hito("2003", "Ley 47/2003, de 26 de noviembre, General Presupuestaria (BOE de 27-11-2003; en vigor el 1-1-2005)", "Arts. 40, 43, 78 y 79: clasificación económica, anticipos de caja fija y pagos a justificar", "normativo", "s1")
T.hito("2014", "Resolución de 20 de enero de 2014, de la Dirección General de Presupuestos (BOE de 29-1-2014)", "Códigos de la clasificación económica de gastos e ingresos", "normativo", "s2")

T.publicar()
