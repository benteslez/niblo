# -*- coding: utf-8 -*-
"""Tema VI.1 (B6T01): El presupuesto. Concepto y clases. La Ley General Presupuestaria:
principios generales y estructura. Las leyes de estabilidad presupuestaria.
Método del I.2. Normas (textos consolidados del BOE): CE, arts. 134.2 y 135; Ley 47/2003,
General Presupuestaria (LGP), arts. 1 a 3, 26 a 35 y 64, exposición de motivos y rúbricas
de sus títulos; Ley Orgánica 2/2012, de Estabilidad Presupuestaria y Sostenibilidad
Financiera (LOEP), arts. 1 a 9, 11 a 32 (lo esencial) y disposición derogatoria única;
Ley Orgánica 6/2013, de la AIReF, arts. 1, 2 y 17."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO["LO6_2013"] = "LO 6/2013"


def g(art, frag):
    """Cita literal de la LGP."""
    return c("LGP", "Artículo " + str(art), frag)


def e(art, frag):
    """Cita literal de la LO 2/2012 (LOEP)."""
    return c("LOEP", "Artículo " + str(art), frag)


T = Tema("B6T01",
  "Seis preguntas: I. Qué es el presupuesto y qué clases hay (CE, art. 134.2; LGP, arts. 32 a 35 y 64) · II. Qué es la Ley General Presupuestaria y cómo está estructurada (LGP, arts. 1 a 3 y títulos) · III. Qué principios generales rigen el presupuesto en la LGP (arts. 26 a 31) · IV. Qué son las leyes de estabilidad presupuestaria (CE, art. 135; LO 2/2012, arts. 1 y 2) · V. Qué principios fija la LO 2/2012 (arts. 3 a 9) · VI. Cómo se hacen cumplir: límites, objetivos y medidas (LO 2/2012, arts. 11 a 32; LO 6/2013). Cada artículo: texto literal del BOE y ficha.",
  ["Presupuesto", "Art. 32 LGP", "Presupuestos limitativos", "Presupuestos estimativos", "Universalidad", "Sector público estatal", "Estructura de la LGP", "Principios presupuestarios", "Escenarios plurianuales", "Art. 135 CE", "LO 2/2012", "Estabilidad presupuestaria", "Sostenibilidad financiera", "Regla de gasto", "Límite de deuda", "Medidas coercitivas", "AIReF"])

# =============================================================================
T.ap("s0", "Mapa del tema: seis preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque VI, tema 1):
> El presupuesto. Concepto y clases. La Ley General Presupuestaria: principios generales y estructura. Las leyes de estabilidad presupuestaria.

### El hilo conductor

El epígrafe se lee como **seis preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Constitución | Leyes |
|---|---|---|---|
| **I** | ¿Qué es el presupuesto y qué clases hay? (concepto y clases) | Art. 134.2 | LGP, arts. 32, 33, 34, 35 y 64; exposición de motivos |
| **II** | ¿Qué es la Ley General Presupuestaria y cómo está estructurada? | — | LGP, arts. 1, 2 y 3; títulos I a VII |
| **III** | ¿Qué principios generales rigen el presupuesto en la LGP? | — | LGP, arts. 26 a 31 |
| **IV** | ¿Qué son las leyes de estabilidad presupuestaria? | Art. 135 | LO 2/2012, arts. 1 y 2 y disposición derogatoria única |
| **V** | ¿Qué principios fija la Ley Orgánica 2/2012? | — | LO 2/2012, arts. 3 a 9 |
| **VI** | ¿Cómo se hacen cumplir? (límites, objetivos, medidas y AIReF) | — | LO 2/2012, arts. 11 a 32 (lo esencial); LO 6/2013, arts. 1, 2 y 17 |

!> **La idea que une los seis bloques:** el presupuesto es la **expresión cifrada** de los derechos y obligaciones del sector público estatal para **un año** (I). Lo regula la **Ley General Presupuestaria** (II), que somete la programación y la gestión a unos **principios** (III). Desde 2011 la Constitución impone además la **estabilidad presupuestaria** a todas las Administraciones (IV), y la **Ley Orgánica 2/2012** la desarrolla con sus principios (V) y con **límites, objetivos y medidas** para hacerla cumplir (VI).

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Las exposiciones de motivos se citan literales y se marcan como tales: explican la ley, no son artículos.
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- Fronteras: la Ley de Presupuestos anual, su elaboración, estructura y clasificaciones (CE, art. 134; LGP, arts. 36 y siguientes) son del tema VI.2; las modificaciones de crédito, del tema VI.3; el control (IGAE y Tribunal de Cuentas), del tema VI.4; el gasto, del tema VI.5; la reforma de 2011 del art. 135 CE como reforma constitucional, del tema I.1.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué es el presupuesto y qué clases hay? (CE, art. 134.2; LGP, arts. 32 a 35 y 64)", donde(
  "Primera pregunta del tema. Antes de estudiar la ley que lo regula hay que saber **qué es** el presupuesto según la Constitución y la LGP, y **qué clases** de presupuestos integran los Presupuestos Generales del Estado.",
  ["1 Concepto: CE art. 134.2, LGP art. 32 y el principio de universalidad", "2 Clases: presupuestos limitativos y estimativos (arts. 33 y 64)", "3 Ámbito temporal, créditos y programas (arts. 34 y 35)"]))

T.ap("s1", "I.1 Concepto de presupuesto (CE, art. 134.2; LGP, art. 32)", f"""
{unidad("1.1 Lo que exige la Constitución (art. 134.2)",
  lit("CE", "Artículo 134", ["tendrán carácter anual", "incluirán la totalidad de los gastos e ingresos del sector público estatal", "beneficios fiscales"], solo=[2]),
  fichab("Rasgos constitucionales de los Presupuestos Generales del Estado",
         "—",
         ["Carácter **anual**", "Incluyen **la totalidad** de los gastos e ingresos del sector público estatal", "Consignan el importe de los **beneficios fiscales** de los tributos del Estado"],
         "—",
         "El resto del art. 134 (elaboración por el Gobierno, presentación tres meses antes, prórroga, enmiendas) es del tema VI.2. Aquí interesan las tres notas del 134.2: **anual**, **totalidad** y **beneficios fiscales**."))}

{unidad("1.2 Definición legal (art. 32 LGP)",
  lit("LGP", "Artículo 32", ["expresión cifrada, conjunta y sistemática", "a liquidar durante el ejercicio"]),
  fichab(f"{g(32, 'la expresión cifrada, conjunta y sistemática de los derechos y obligaciones a liquidar durante el ejercicio')}",
         f"{g(32, 'cada uno de los órganos y entidades que forman parte del sector público estatal')} (→ II.1.2)",
         ["**Cifrada**: en importes", "**Conjunta y sistemática**: todos los órganos y entidades en un solo documento ordenado", "Contiene **derechos** (ingresos) y **obligaciones** (gastos)"],
         "Durante **el ejercicio** (→ I.3.1)",
         "Las tres palabras de la definición: **cifrada, conjunta y sistemática**. Habla de derechos y obligaciones **a liquidar**, no de «ingresos y gastos previstos»."))}

{unidad("1.3 El principio de universalidad (exposición de motivos de la LGP)",
  lit("LGP", "preambulo", ["principio de universalidad del presupuesto", "artículo 134 de la Constitución española"], solo=[37], titulo="Exposición de motivos, II (LGP) · no es articulado"),
  fichab("Nombre que la propia LGP da a la exigencia del art. 134.2 de incluir la totalidad de los gastos e ingresos",
         "—",
         f"La LGP lo refleja con {c('LGP', 'preambulo', 'una enumeración completa de las entidades que integran el sector público estatal')} (art. 2 → II.1.2)",
         "—",
         "Universalidad = **totalidad** de ingresos y gastos del sector público estatal (art. 134.2 CE). Lo preguntó la X 92 (→ Cierre 1)."))}
""", 2)

T.ap("s2", "I.2 Clases de presupuestos: limitativos y estimativos (LGP, arts. 33 y 64)", f"""
Los Presupuestos Generales del Estado no son un único presupuesto: integran **dos clases** de presupuestos según la entidad.

{unidad("2.1 Alcance subjetivo y contenido (art. 33)",
  lit("LGP", "Artículo 33", ["carácter limitativo", "presupuestos estimativos", "que, como máximo, pueden reconocer", "La estimación de los beneficios fiscales"]),
  fichab("Qué presupuestos integran los Presupuestos Generales del Estado y qué determinan",
         ["::Dos clases:", "a) **Limitativos**: los órganos del art. 2.3 y las entidades con el régimen de especificaciones y modificaciones de la LGP o cuya normativa dé carácter limitativo a su presupuesto", "b) **Estimativos**: sectores empresarial y fundacional, consorcios, universidades no transferidas, fondos sin personalidad jurídica y el resto del sector público administrativo no incluido en la letra a)"],
         ["::Los PGE determinan (33.2):", "Las obligaciones que **como máximo** pueden reconocer los sujetos con presupuesto limitativo", "Los derechos a reconocer en el ejercicio", "Las operaciones no financieras y financieras de las entidades con presupuesto estimativo", "Los objetivos de cada gestor de programas", "La estimación de los beneficios fiscales de los tributos del Estado"],
         "—",
         "Limitativo = **máximo** de obligaciones. Los **consorcios**, las **universidades no transferidas** y los **fondos sin personalidad jurídica** van con los **estimativos** (letra b), no con los limitativos."))}

{unidad("2.2 Presupuestos de explotación y de capital (art. 64)",
  lit("LGP", "Artículo 64", ["presupuesto de explotación", "presupuesto de capital", "previsión de la cuenta de resultados y del estado de flujos de efectivo"], solo=[1, 4]),
  fichab("Forma de los presupuestos de las sociedades mercantiles estatales y de las entidades públicas empresariales",
         f"{g(64, 'Las sociedades mercantiles estatales y las entidades públicas empresariales')}",
         ["Presupuesto de **explotación** y presupuesto de **capital**", "Constituidos por una previsión de la **cuenta de resultados** y del **estado de flujos de efectivo**; anexo: previsión del **balance**"],
         f"{g(64, 'Los presupuestos de explotación y de capital se integrarán en los Presupuestos Generales del Estado')}",
         "No tienen créditos limitativos: su presupuesto es una **previsión** contable (cuenta de resultados y flujos de efectivo), y se **integra** en los PGE."))}

### Cuadro de las clases de presupuestos (esquema)

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| | Presupuestos limitativos | Presupuestos estimativos |
|---|---|---|
| Quién | Órganos del art. 2.3 y entidades con régimen de especificaciones y modificaciones de la LGP o normativa que dé carácter limitativo | Entidades empresariales y fundacionales, consorcios, universidades no transferidas, fondos sin personalidad jurídica y resto del sector administrativo |
| Qué fijan | Obligaciones que **como máximo** pueden reconocer y derechos a reconocer | Operaciones no financieras y financieras |
| Artículo | 33.1 a) y 33.2 a) y b) | 33.1 b), 33.2 c) y 64 |
""", 2)

T.ap("s3", "I.3 Ámbito temporal, créditos y programas (LGP, arts. 34 y 35)", f"""
{unidad("3.1 El ejercicio presupuestario (art. 34)",
  lit("LGP", "Artículo 34", ["coincidirá con el año natural", "cualquiera que sea el período del que deriven", "hasta el fin del mes de diciembre", "requerirá norma con rango de ley"], solo=[1, 2, 3, 4, 7]),
  fichab("A qué ejercicio se imputan los derechos y las obligaciones",
         "—",
         ["Derechos: los **liquidados** durante el ejercicio, cualquiera que sea el período del que deriven", "Obligaciones: las **reconocidas hasta el fin de diciembre**, si son gastos realizados dentro del ejercicio", "Excepciones: atrasos de personal y resoluciones judiciales (al presupuesto vigente al expedir la orden de pago)"],
         "Ejercicio = **año natural**. Obligaciones de ejercicios anteriores fuera de los supuestos previstos: **norma con rango de ley**",
         "Para los **derechos** basta que se liquiden en el ejercicio (**cualquiera que sea el período del que deriven**); para las **obligaciones**, que el gasto se haya realizado **dentro del ejercicio**."))}

{unidad("3.2 Créditos y programas presupuestarios (art. 35)",
  lit("LGP", "Artículo 35", ["asignaciones individualizadas de gasto", "de carácter plurianual", "programas de apoyo", "la concreción anual de los programas presupuestarios de carácter plurianual"], solo=[1, 2, 3, 4, 5, 6, 7, 8]),
  fichab(f"Crédito: {g(35, 'cada una de las asignaciones individualizadas de gasto')}; programa: conjunto de gastos orientado a objetivos",
         f"Programas {g(35, 'bajo la responsabilidad del titular del centro gestor del gasto')}",
         ["Especificación de los créditos: orgánica, por programas y económica (arts. 40, 43 y 44, tema VI.2)", "Fines de los programas: producción de bienes y servicios, obligaciones específicas o demás actividades", "Servicios horizontales e instrumentales: **programas de apoyo**"],
         "El programa del presupuesto **anual** concreta el programa **plurianual**",
         "El **crédito** es la asignación **individualizada**; el **programa de gasto anual** es la concreción anual del programa **plurianual**."))}

{resumen([
  "Presupuesto: **expresión cifrada, conjunta y sistemática** de derechos y obligaciones a liquidar en el ejercicio (art. 32); **anual** y con la **totalidad** de gastos e ingresos (134.2 CE).",
  "La LGP llama a esa totalidad **principio de universalidad** (exposición de motivos).",
  "Clases: **limitativos** (máximo de obligaciones) y **estimativos** (empresariales, fundacionales, consorcios, universidades no transferidas, fondos) (art. 33); explotación y capital (art. 64).",
  "Ejercicio = **año natural**; créditos y programas (arts. 34 y 35)."],
  "Siguiente: II. ¿Qué es la Ley General Presupuestaria y cómo está estructurada?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Qué es la Ley General Presupuestaria y cómo está estructurada? (LGP, arts. 1 a 3 y títulos)", donde(
  "Segunda pregunta. La norma que regula el presupuesto del Estado es la **Ley 47/2003, General Presupuestaria**. Hay que saber **qué regula**, **a quién se aplica** y **cómo se ordena**.",
  ["1 Objeto y sector público estatal (arts. 1 y 2)", "2 Sectores administrativo, empresarial y fundacional (art. 3)", "3 Estructura de la ley: sus siete títulos"]))

T.ap("s4", "II.1 Objeto y ámbito de la Ley General Presupuestaria (arts. 1 y 2)", f"""
{unidad("1.1 Objeto (art. 1)",
  lit("LGP", "Artículo 1", ["régimen presupuestario, económico-financiero, de contabilidad, intervención y de control financiero"]),
  fichab("Lo que regula la LGP",
         f"{g(1, 'del sector público estatal')}",
         ["Régimen presupuestario", "Régimen económico-financiero", "Contabilidad", "Intervención y control financiero"],
         "—",
         "La LGP es la ley del **sector público estatal**: no regula los presupuestos de las Comunidades Autónomas ni de las entidades locales."))}

{unidad("1.2 El sector público estatal (art. 2)",
  lit("LGP", "Artículo 2", ["La Administración General del Estado.", "Los fondos sin personalidad jurídica.", "Los órganos con dotación diferenciada", "esta Ley no será de aplicación a las Cortes Generales, que gozan de autonomía presupuestaria"]),
  fichab("Quién forma parte del sector público estatal a efectos de la LGP",
         ["::Integran el sector público estatal:", "La **Administración General del Estado**", "El **sector público institucional estatal**: organismos públicos (organismos autónomos, entidades públicas empresariales, agencias estatales), autoridades administrativas independientes, sociedades mercantiles estatales, consorcios y fundaciones adscritos, fondos sin personalidad jurídica, universidades no transferidas, entidades gestoras, servicios comunes y mutuas colaboradoras con la Seguridad Social, y demás entidades de derecho público", "Los **órganos con dotación diferenciada** en los PGE sin personalidad jurídica (2.3)"],
         "Órganos con dotación diferenciada: régimen económico-financiero de la LGP, pero contabilidad y control según sus propias normas",
         "—",
         "La LGP **no se aplica a las Cortes Generales**, que gozan de **autonomía presupuestaria** (art. 72 CE). Las **mutuas colaboradoras** y los **fondos sin personalidad** sí están dentro. Cayó en 2025 (P 84, → Cierre 1)."))}
""", 2)

T.ap("s5", "II.2 Sectores administrativo, empresarial y fundacional (art. 3)", f"""
{unidad("2.1 Los tres sectores (art. 3)",
  lit("LGP", "Artículo 3", ["El sector público administrativo", "El sector público empresarial", "El sector público fundacional", "Que no se financien mayoritariamente con ingresos comerciales"]),
  fichab("División del sector público estatal a efectos de la LGP",
         ["::Tres sectores:", "**Administrativo**: AGE, organismos autónomos, autoridades administrativas independientes, universidades no transferidas, Seguridad Social y órganos del 2.3; y entidades, consorcios y fondos que cumplan alguna de las dos características de la letra b)", "**Empresarial**: entidades públicas empresariales, sociedades mercantiles estatales y el resto de entidades, consorcios y fondos", "**Fundacional**: fundaciones del sector público estatal"],
         f"Criterio para entidades, consorcios y fondos: actividad principal no de mercado o {g(3, 'Que no se financien mayoritariamente con ingresos comerciales')}",
         "—",
         "Basta **una** de las dos características de la letra b) para ir al sector **administrativo**. Las **entidades públicas empresariales** van siempre al **empresarial**."))}
""", 2)

T.ap("s6", "II.3 Estructura de la Ley General Presupuestaria", f"""
{unidad("3.1 La LGP como ley de referencia (exposición de motivos)",
  lit("LGP", "preambulo", ["documento jurídico de referencia", "la Ley General Presupuestaria de 1977 y el posterior texto refundido de 1988"], solo=[17], titulo="Exposición de motivos, I (LGP) · no es articulado"),
  lit("LGP", "preambulo", ["los principios de estabilidad presupuestaria, plurianualidad, transparencia y eficiencia en la asignación"], solo=[50], titulo="Exposición de motivos, III (LGP) · no es articulado"),
  fichab("Lugar de la LGP en el ordenamiento financiero del Estado",
         "Ley 47/2003, de 26 de noviembre (sustituye a la Ley General Presupuestaria de 1977 y al texto refundido de 1988)",
         "—",
         "—",
         "La LGP vigente es la **Ley 47/2003**; sus antecedentes son la ley de **1977** y el texto refundido de **1988**."))}

### Los siete títulos (rúbricas literales del BOE)

| Título | Rúbrica | Contenido principal en este temario |
|---|---|---|
| I | {c('LGP', 'ti', 'Del ámbito de aplicación y de la Hacienda Pública estatal')} | Arts. 1 a 3 (→ II.1 y → II.2) |
| II | {c('LGP', 'tii', 'De los Presupuestos Generales del Estado')} | Principios (→ III.1), concepto y clases (→ I.1), elaboración y estructura (tema VI.2), modificaciones (tema VI.3), gestión (tema VI.5) |
| III | {c('LGP', 'tiii', 'De las relaciones financieras con otras administraciones')} | Unión Europea, comunidades autónomas y entidades locales |
| IV | {c('LGP', 'tiv', 'Del Tesoro Público, de la Deuda del Estado y de las Operaciones Financieras')} | Tesoro y Deuda (tema VI.6) |
| V | {c('LGP', 'tv', 'Contabilidad del sector público estatal')} | Contabilidad y rendición de cuentas |
| VI | {c('LGP', 'tvi', 'Del control de la gestión económico-financiera efectuado por la Intervención General de la Administración del Estado')} | Control interno (tema VI.4) |
| VII | {c('LGP', 'tvii', 'De las responsabilidades')} | Responsabilidades |

### Los capítulos del título II (rúbricas literales del BOE)

| Capítulo | Rúbrica | Artículos que se estudian aquí |
|---|---|---|
| I | {c('LGP', 'ci-2', 'Principios y reglas de programación y de gestión presupuestaria')} | 26 y 27 (→ III.1 y → III.2) |
| II | {c('LGP', 'cii-2', 'Programación presupuestaria y objetivo de estabilidad')} | 28 a 31 (→ III.3) |
| III | {c('LGP', 'ciii', 'Contenido, elaboración y estructura')} | 32 a 35 (→ I.1 a → I.3) |
| IV | {c('LGP', 'civ', 'De los créditos y sus modificaciones')} | Tema VI.3 |
| V | {c('LGP', 'cv', 'De las Entidades Públicas Empresariales, Sociedades Mercantiles Estatales y Fundaciones del sector público Estatal')} | 64 (→ I.2.2) |
| VI | {c('LGP', 'cvi', 'De la Gestión presupuestaria')} | Tema VI.5 |

*La columna de la derecha es de elaboración propia (remisiones), no texto legal.*

{resumen([
  "La LGP regula el régimen presupuestario, económico-financiero, de contabilidad, intervención y control **del sector público estatal** (art. 1).",
  "Sector público estatal: **AGE** + **sector público institucional** + órganos con dotación diferenciada; **no** se aplica a las **Cortes Generales** (art. 2).",
  "Tres sectores: **administrativo**, **empresarial** y **fundacional** (art. 3).",
  "**Siete títulos**: ámbito y Hacienda Pública; PGE; relaciones financieras; Tesoro y Deuda; contabilidad; control de la IGAE; responsabilidades."],
  "Siguiente: III. ¿Qué principios generales rigen el presupuesto en la LGP?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Qué principios generales rigen el presupuesto en la LGP? (arts. 26 a 31)", donde(
  "Tercera pregunta. El capítulo I del título II fija los **principios y reglas** de la programación y de la gestión presupuestaria; el capítulo II los concreta en **escenarios** y **programas plurianuales**.",
  ["1 Principios de programación (art. 26)", "2 Principios y reglas de gestión (art. 27)", "3 Escenarios y programas plurianuales (arts. 28 a 31)"]))

T.ap("s7", "III.1 Principios de programación presupuestaria (art. 26)", f"""
{unidad("1.1 Los siete principios de la programación (art. 26)",
  lit("LGP", "Artículo 26", ["estabilidad presupuestaria, sostenibilidad financiera, plurianualidad, transparencia, eficiencia en la asignación y utilización de los recursos públicos, responsabilidad y lealtad institucional", "supeditarse de forma estricta a las disponibilidades presupuestarias"]),
  fichab("Principios que rigen la programación presupuestaria del sector público estatal",
         "Todos los sujetos del sector público estatal",
         ["::Principios (26.1), con remisión a la LO 2/2012 (→ V.1):", "Estabilidad presupuestaria", "Sostenibilidad financiera", "Plurianualidad", "Transparencia", "Eficiencia en la asignación y utilización de los recursos públicos", "Responsabilidad", "Lealtad institucional"],
         "—",
         "Son **siete** y coinciden con los de la **LO 2/2012** (arts. 3 a 9). Toda norma, acto, contrato o convenio que afecte al gasto debe **valorar sus repercusiones** y **supeditarse de forma estricta** a las disponibilidades presupuestarias (26.2)."))}
""", 2)

T.ap("s8", "III.2 Principios y reglas de gestión presupuestaria (art. 27)", f"""
{unidad("2.1 Presupuesto anual, finalidad de los créditos y destino de los recursos (art. 27.1 a 3)",
  lit("LGP", "Artículo 27", ["régimen de presupuesto anual aprobado por las Cortes Generales", "exclusivamente a la finalidad específica", "nivel de especificación", "salvo que por ley se establezca su afectación a fines determinados"], solo=[1, 2, 3, 4]),
  fichab("Reglas de gestión de los créditos y de los recursos",
         "Estado, organismos autónomos y entidades del sector público estatal **con presupuesto limitativo**",
         ["Presupuesto **anual** aprobado por las **Cortes Generales**, en un **escenario plurianual** (27.1)", "Créditos: **exclusivamente** a la finalidad específica autorizada (27.2)", "Carácter limitativo y vinculante: el del **nivel de especificación** con que aparezcan (27.2)", "Recursos: al **conjunto** de las obligaciones, salvo afectación **por ley** (27.3)"],
         "—",
         "La afectación de recursos a fines determinados solo puede hacerla **una ley**. La vinculación depende del **nivel de especificación** del crédito."))}

{unidad("2.2 Importe íntegro e información (art. 27.4 y 5)",
  lit("LGP", "Artículo 27", ["por su importe íntegro", "salvo que la ley lo autorice de modo expreso", "información suficiente y adecuada"], solo=[5, 6, 8, 9]),
  fichab("Aplicación de derechos y obligaciones al presupuesto",
         "—",
         ["Derechos liquidados y obligaciones reconocidas: por su **importe íntegro**", "No se atienden obligaciones minorando derechos, **salvo autorización expresa de la ley**", "Excepciones: devoluciones de ingresos indebidos, reembolso del coste de garantías y participaciones en la recaudación de tributos"],
         "—",
         "Importe íntegro = el resultante **después de aplicar las exenciones y bonificaciones** que procedan. El presupuesto debe contener **información suficiente y adecuada** para verificar sus principios (27.5)."))}
""", 2)

T.ap("s9", "III.3 Escenarios y programas plurianuales (arts. 28 a 31)", f"""
{unidad("3.1 Escenarios presupuestarios plurianuales (art. 28)",
  lit("LGP", "Artículo 28", ["referidos a los tres ejercicios siguientes", "artículo 15 de la Ley Orgánica 2/2012", "serán confeccionados por el Ministerio de Hacienda", "un escenario de ingresos y un escenario de gastos"], solo=[1, 2, 3, 4]),
  fichab("Programación del sector público estatal con presupuesto limitativo en la que se enmarcan los PGE",
         f"{g(28, 'serán confeccionados por el Ministerio de Hacienda')}, que da cuenta al Consejo de Ministros antes de aprobar el proyecto de PGE",
         ["Definen equilibrios básicos, evolución de ingresos y recursos de las políticas de gasto", "Se ajustan al **objetivo de estabilidad** del Estado y la Seguridad Social (art. 15 LO 2/2012, → VI.2.1)", "Integrados por un escenario de **ingresos** y otro de **gastos**"],
         "Límites para los **tres ejercicios siguientes**",
         "Los confecciona el **Ministerio de Hacienda** (no el Consejo de Ministros, al que solo **da cuenta**). Horizonte: **tres** ejercicios."))}

{unidad("3.2 Programas plurianuales ministeriales y de los centros gestores (arts. 29 y 30)",
  lit("LGP", "Artículo 29", ["referidos a los tres ejercicios siguientes", "se aprobará por el Ministro"], solo=[1, 2, 3]),
  lit("LGP", "Artículo 30", ["se elaborarán por los titulares de los referidos centros"], solo=[1]),
  fichab("Desarrollo de los escenarios en programas por ministerios y centros gestores",
         ["Programa de cada ministerio: lo **aprueba el Ministro**", "Programa de la Seguridad Social: separadamente, el Ministro competente", "Programas de los centros gestores: los elaboran **sus titulares** y se integran en el del ministerio"],
         "Por centros gestores: objetivos, acciones y dotaciones; se remiten **anualmente** al Ministerio de Hacienda",
         "Tres ejercicios siguientes",
         "Escenarios → programas plurianuales ministeriales → programas de los centros gestores."))}

{unidad("3.3 Asignación presupuestaria y objetivos (art. 31)",
  lit("LGP", "Artículo 31", ["se adecuarán a los escenarios presupuestarios plurianuales", "el nivel de cumplimiento de los objetivos en ejercicios anteriores"]),
  fichab("Cómo se vinculan los PGE a los escenarios y las asignaciones a los resultados",
         "El Gobierno determina las restricciones de política económica de cada ejercicio",
         ["Los PGE se **adecuan** a los escenarios plurianuales", "Las asignaciones a los centros gestores tienen en cuenta el **cumplimiento de objetivos** de ejercicios anteriores"],
         "—",
         "Presupuestación orientada a **objetivos**: el cumplimiento **anterior** cuenta para la asignación."))}

{resumen([
  "Programación: **siete principios** (estabilidad, sostenibilidad, plurianualidad, transparencia, eficiencia, responsabilidad y lealtad institucional), conforme a la LO 2/2012 (art. 26).",
  "Gestión: presupuesto **anual** de las Cortes en escenario plurianual; créditos a su **finalidad específica**; recursos al conjunto de obligaciones salvo afectación **por ley**; **importe íntegro** (art. 27).",
  "Escenarios plurianuales del **Ministerio de Hacienda** a **tres** años, ajustados al objetivo de estabilidad (art. 28); programas ministeriales y de centros gestores (arts. 29 a 31)."],
  "Siguiente: IV. ¿Qué son las leyes de estabilidad presupuestaria?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Qué son las leyes de estabilidad presupuestaria? (CE, art. 135; LO 2/2012, arts. 1 y 2)", donde(
  "Cuarta pregunta. La estabilidad presupuestaria tiene **rango constitucional** desde la reforma de 2011 del art. 135. Las «leyes de estabilidad» son las que la regulan: las de 2001 y 2007, derogadas, y la vigente **Ley Orgánica 2/2012**.",
  ["1 El art. 135 de la Constitución", "2 De las leyes de 2001 a la Ley Orgánica 2/2012", "3 Objeto y ámbito de la Ley Orgánica 2/2012 (arts. 1 y 2)"]))

T.ap("s10", "IV.1 El mandato constitucional (art. 135 CE)", f"""
La reforma del art. 135 en 2011 se estudia como reforma constitucional en el tema I.1; aquí, su contenido.

{unidad("1.1 Estabilidad y déficit estructural (art. 135.1 y 2)",
  lit("CE", "Artículo 135", ["Todas las Administraciones Públicas adecuarán sus actuaciones al principio de estabilidad presupuestaria", "márgenes establecidos, en su caso, por la Unión Europea", "Una ley orgánica fijará el déficit estructural máximo", "Las Entidades Locales deberán presentar equilibrio presupuestario"], solo=[1, 2, 3]),
  fichab("Principio de estabilidad presupuestaria y límite de déficit estructural",
         ["Estabilidad: **todas** las Administraciones Públicas", "Déficit estructural: el **Estado** y las **Comunidades Autónomas**", "Equilibrio: las **Entidades Locales**"],
         "El déficit estructural máximo lo fija **una ley orgánica**, en relación con el PIB",
         "No superar los márgenes de la **Unión Europea**",
         "Las **Entidades Locales** no pueden tener déficit estructural: deben presentar **equilibrio**. Cayó en 2025 (P 26, → Cierre 1)."))}

{unidad("1.2 Deuda pública y excepciones (art. 135.3 y 4)",
  lit("CE", "Artículo 135", ["habrán de estar autorizados por ley", "prioridad absoluta", "valor de referencia establecido en el Tratado de Funcionamiento de la Unión Europea", "apreciadas por la mayoría absoluta de los miembros del Congreso de los Diputados"], solo=[4, 5, 6, 7]),
  fichab("Deuda pública: autorización, prioridad de pago, límite y excepciones",
         "Estado y CC. AA.: autorizados **por ley** para emitir deuda; aprecia las excepciones **la mayoría absoluta del Congreso**",
         ["Créditos de intereses y capital de la deuda: siempre incluidos en el estado de gastos; pago con **prioridad absoluta**; sin enmienda ni modificación mientras se ajusten a la ley de emisión", "Volumen de deuda: no superar el valor de referencia del **TFUE**"],
         "Excepciones: catástrofes naturales, recesión económica o emergencia extraordinaria, apreciadas por **mayoría absoluta del Congreso**",
         "Las excepciones las aprecia el **Congreso** por **mayoría absoluta de sus miembros** (no las Cortes ni el Gobierno). La deuda tiene **prioridad absoluta** de pago."))}

{unidad("1.3 La ley orgánica de desarrollo (art. 135.5 y 6)",
  lit("CE", "Artículo 135", ["Una ley orgánica desarrollará los principios a que se refiere este artículo", "La responsabilidad de cada Administración Pública"], solo=[8, 9, 10, 11, 12]),
  fichab("Contenido mínimo de la ley orgánica de estabilidad",
         "Las Cortes, por **ley orgánica** (hoy la LO 2/2012, → IV.3.1)",
         ["Distribución de los límites de déficit y deuda, excepciones y corrección de desviaciones", "Metodología del déficit estructural", "Responsabilidad de cada Administración por incumplimiento"],
         "—",
         "Las **Comunidades Autónomas** aplican el principio en sus propias normas, de acuerdo con sus Estatutos (135.6)."))}
""", 2)

T.ap("s11", "IV.2 De las leyes de 2001 a la Ley Orgánica 2/2012 (antecedentes en el BOE)", f"""
{unidad("2.1 Las leyes de estabilidad anteriores y su derogación",
  lit("LGP", "preambulo", ["Ley 18/2001, de 12 de diciembre, General de Estabilidad Presupuestaria"], solo=[26], titulo="Exposición de motivos, I (LGP, 2003) · no es articulado"),
  lit("LOEP", "ddunica", ["Ley orgánica 5/2001, de 13 de diciembre", "Real Decreto Legislativo 2/2007, de 28 de diciembre"], solo=[1]),
  fichab("Sucesión de las leyes de estabilidad presupuestaria",
         "—",
         ["2001: Ley 18/2001, General de Estabilidad Presupuestaria, y Ley Orgánica 5/2001, complementaria", "2007: texto refundido de la Ley General de Estabilidad Presupuestaria (Real Decreto Legislativo 2/2007)", "2012: Ley Orgánica 2/2012, que deroga la LO 5/2001 y el texto refundido de 2007"],
         "—",
         "La ley vigente es **orgánica** porque el art. 135.5 CE exige **ley orgánica**. Deroga expresamente la **LO 5/2001** y el **texto refundido de 2007**."))}

{unidad("2.2 Qué cambia la Ley Orgánica 2/2012 (preámbulo)",
  lit("LOEP", "preambulo", ["en un texto único", "tanto del Estado como de las Comunidades Autónomas, Corporaciones Locales y Seguridad Social"], solo=[15], titulo="Preámbulo (LO 2/2012) · no es articulado"),
  fichab("Novedad sistemática de la LO 2/2012",
         "Todas las Administraciones Públicas",
         "Una sola ley para la estabilidad y la sostenibilidad de **todas** las Administraciones",
         "—",
         "Antes había dos leyes (ordinaria y orgánica complementaria); ahora un **texto único**."))}
""", 2)

T.ap("s12", "IV.3 Objeto y ámbito de la Ley Orgánica 2/2012 (arts. 1 y 2)", f"""
{unidad("3.1 Objeto (art. 1)",
  lit("LOEP", "Artículo 1", ["vinculan a todos los poderes públicos", "en desarrollo del artículo 135 de la Constitución Española"], solo=[1]),
  fichab("Lo que regula la LO 2/2012",
         f"Los principios {e(1, 'vinculan a todos los poderes públicos')}",
         ["Principios rectores de la política presupuestaria del sector público (→ V.1)", "Procedimientos para aplicarlos: límites de déficit y deuda, excepciones, corrección y responsabilidad (→ VI.1)"],
         "—",
         "Desarrolla el **art. 135 CE**; orientada a la estabilidad y la sostenibilidad **como garantía del crecimiento económico sostenido y la creación de empleo**."))}

{unidad("3.2 Ámbito subjetivo (art. 2)",
  lit("LOEP", "Artículo 2", ["Sistema Europeo de Cuentas Nacionales y Regionales", "Administración central, que comprende el Estado y los organismos de la administración central.", "Administraciones de Seguridad Social."]),
  fichab("Quién forma el sector público a efectos de la LO 2/2012",
         ["::Sector Administraciones Públicas (2.1), con cuatro subsectores:", "a) Administración central: el Estado y los organismos de la administración central", "b) Comunidades Autónomas", "c) Corporaciones Locales", "d) Administraciones de Seguridad Social", "::Resto del sector público (2.2): entidades públicas empresariales, sociedades mercantiles y demás entes no incluidos, solo en las normas que se les refieran"],
         "Delimitación según el **Sistema Europeo de Cuentas** (contabilidad nacional), no según la LGP",
         "—",
         "**Cuatro** subsectores: la Seguridad Social es un subsector **propio**, separado de la Administración central. Cayó en 2025 (X 90, → Cierre 1)."))}

{resumen([
  "Art. 135 CE: **estabilidad** para todas las Administraciones; déficit estructural limitado para **Estado y CC. AA.**; **equilibrio** para las Entidades Locales; **prioridad absoluta** de la deuda; excepciones por **mayoría absoluta del Congreso**.",
  "Leyes de estabilidad: 2001 (Ley 18/2001 y LO 5/2001), texto refundido de 2007 y la vigente **LO 2/2012**, que las deroga.",
  "LO 2/2012: desarrolla el art. 135; sector Administraciones Públicas con **cuatro** subsectores (central, CC. AA., Corporaciones Locales, Seguridad Social)."],
  "Siguiente: V. ¿Qué principios fija la Ley Orgánica 2/2012?")}
""", 2)

# =============================================================================
T.ap("bV", "V. ¿Qué principios fija la Ley Orgánica 2/2012? (arts. 3 a 9)", donde(
  "Quinta pregunta. El capítulo II de la LO 2/2012 define **siete principios generales**; son los mismos que la LGP manda seguir en la programación (art. 26, → III.1).",
  ["1 Estabilidad presupuestaria y sostenibilidad financiera (arts. 3 y 4)", "2 Plurianualidad, transparencia y eficiencia (arts. 5 a 7)", "3 Responsabilidad y lealtad institucional (arts. 8 y 9)"]))

T.ap("s13", "V.1 Estabilidad presupuestaria y sostenibilidad financiera (arts. 3 y 4)", f"""
{unidad("1.1 Principio de estabilidad presupuestaria (art. 3)",
  lit("LOEP", "Artículo 3", ["la situación de equilibrio o superávit estructural", "la posición de equilibrio financiero"]),
  fichab("Definición legal de estabilidad presupuestaria",
         ["Administraciones Públicas: **equilibrio o superávit estructural** (3.2)", "Entidades del art. 2.2: **equilibrio financiero** (3.3)"],
         f"Elaboración, aprobación y ejecución de los presupuestos {e(3, 'en un marco de estabilidad presupuestaria, coherente con la normativa europea')}",
         "—",
         "Es «equilibrio **o** superávit **estructural**», no solo equilibrio ni solo superávit. Cayó en 2025 (L 83, → Cierre 1)."))}

{unidad("1.2 Principio de sostenibilidad financiera (art. 4)",
  lit("LOEP", "Artículo 4", ["la capacidad para financiar compromisos de gasto presentes y futuros", "el periodo medio de pago a los proveedores no supere el plazo máximo", "principio de prudencia financiera"]),
  fichab("Definición legal de sostenibilidad financiera",
         "Administraciones Públicas y demás sujetos de la ley",
         ["Capacidad para financiar compromisos presentes y futuros dentro de los límites de **déficit**, **deuda pública** y **morosidad de deuda comercial**", "Deuda comercial sostenible: periodo medio de pago a proveedores dentro del plazo de la normativa de morosidad", "Operaciones financieras: principio de **prudencia financiera**"],
         "—",
         "La definición de **sostenibilidad** («capacidad para financiar compromisos…») es el distractor típico de la de **estabilidad**."))}
""", 2)

T.ap("s14", "V.2 Plurianualidad, transparencia y eficiencia (arts. 5 a 7)", f"""
{unidad("2.1 Principio de plurianualidad (art. 5)",
  lit("LOEP", "Artículo 5", ["marco presupuestario a medio plazo", "compatible con el principio de anualidad"]),
  fichab("Encuadre de los presupuestos en un marco a medio plazo",
         "Administraciones Públicas y demás sujetos de la ley",
         "Marco presupuestario a **medio plazo** (→ VI.4.1)",
         "—",
         "La plurianualidad es **compatible** con el **principio de anualidad**, que rige la **aprobación y ejecución** de los presupuestos."))}

{unidad("2.2 Principio de transparencia (art. 6)",
  lit("LOEP", "Artículo 6", ["información suficiente y adecuada", "proveer la disponibilidad pública"], solo=[1, 2]),
  fichab("Información sobre la situación financiera y el cumplimiento de objetivos",
         "Corresponde al **Ministerio de Hacienda** proveer la disponibilidad pública de la información económico-financiera",
         "Contabilidad, presupuestos y liquidaciones con información suficiente y adecuada; los presupuestos y cuentas generales integran a **todos** los sujetos de la ley",
         "—",
         "Se instrumenta en el art. 27 de la ley (equivalencia entre presupuesto y contabilidad nacional; líneas fundamentales antes del 1 de octubre)."))}

{unidad("2.3 Principio de eficiencia en la asignación y utilización de los recursos públicos (art. 7)",
  lit("LOEP", "Artículo 7", ["marco de planificación plurianual", "la eficacia, la eficiencia, la economía y la calidad", "deberán valorar sus repercusiones y efectos"]),
  fichab("Orientación de la gestión del gasto público",
         "—",
         ["Políticas de gasto en un marco de planificación plurianual", "Gestión orientada por **eficacia, eficiencia, economía y calidad**", "Normas, actos, contratos y convenios: valorar repercusiones y supeditarse a la estabilidad y sostenibilidad"],
         "—",
         "Cuatro criterios: **eficacia, eficiencia, economía y calidad**."))}
""", 2)

T.ap("s15", "V.3 Responsabilidad y lealtad institucional (arts. 8 y 9)", f"""
{unidad("3.1 Principio de responsabilidad (art. 8)",
  lit("LOEP", "Artículo 8", ["en la parte que les sea imputable", "El Estado no asumirá ni responderá de los compromisos de las Comunidades Autónomas"]),
  fichab("Responsabilidad por incumplimiento y prohibición de rescate",
         "La Administración incumplidora, **en la parte que le sea imputable**, con audiencia previa",
         ["Asume las responsabilidades derivadas de incumplir la ley o los compromisos europeos e internacionales", "El **Estado** no responde de los compromisos de CC. AA. ni de Corporaciones Locales", "Las **CC. AA.** no responden de los de las Corporaciones Locales"],
         "—",
         "Salvedad: las **garantías financieras mutuas** para la realización conjunta de proyectos específicos."))}

{unidad("3.2 Principio de lealtad institucional (art. 9)",
  lit("LOEP", "Artículo 9", ["Valorar el impacto", "Respetar el ejercicio legítimo de las competencias", "Facilitar al resto de Administraciones Públicas la información"]),
  fichab("Deberes recíprocos entre Administraciones",
         "Cada Administración Pública",
         ["Valorar el impacto de sus actuaciones en las demás", "Respetar las competencias ajenas", "Ponderar la totalidad de los intereses públicos implicados", "Facilitar información", "Prestar cooperación y asistencia activas"],
         "—",
         "Son **cinco** deberes (letras a a e)."))}

### Cuadro de los principios (esquema)

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Principio | LO 2/2012 | Clave literal |
|---|---|---|
| Estabilidad presupuestaria | Art. 3 | Equilibrio o superávit estructural |
| Sostenibilidad financiera | Art. 4 | Capacidad para financiar compromisos presentes y futuros dentro de los límites |
| Plurianualidad | Art. 5 | Marco presupuestario a medio plazo, compatible con la anualidad |
| Transparencia | Art. 6 | Información suficiente y adecuada |
| Eficiencia | Art. 7 | Eficacia, eficiencia, economía y calidad |
| Responsabilidad | Art. 8 | Asumir el incumplimiento en la parte imputable; sin rescate |
| Lealtad institucional | Art. 9 | Cinco deberes recíprocos |

{resumen([
  "Estabilidad: **equilibrio o superávit estructural** (art. 3); sostenibilidad: **capacidad para financiar compromisos** dentro de los límites de déficit, deuda y morosidad (art. 4).",
  "Plurianualidad compatible con la **anualidad** (5); transparencia (6); eficiencia: **eficacia, eficiencia, economía y calidad** (7).",
  "Responsabilidad: cada Administración responde de su incumplimiento; el **Estado no responde** de CC. AA. ni Corporaciones Locales (8); lealtad institucional (9)."],
  "Siguiente: VI. ¿Cómo se hacen cumplir? Límites, objetivos y medidas")}
""", 2)

# =============================================================================
T.ap("bVI", "VI. ¿Cómo se hacen cumplir? Límites, objetivos y medidas (LO 2/2012, arts. 11 a 32; LO 6/2013)", donde(
  "Sexta pregunta. Los principios se convierten en **reglas numéricas** (déficit, gasto, deuda), en **objetivos** que fija el Gobierno y aprueban las Cortes, y en **medidas** escalonadas si se incumplen. Vigila la **Autoridad Independiente de Responsabilidad Fiscal**.",
  ["1 Déficit estructural, regla de gasto, límite de deuda y prioridad de pago (arts. 11 a 14)", "2 Objetivos e informes de cumplimiento (arts. 15 a 17)", "3 Medidas preventivas, correctivas y coercitivas (arts. 18 a 26)", "4 Gestión presupuestaria y AIReF (arts. 29 a 32; LO 6/2013)"]))

T.ap("s16", "VI.1 Déficit, regla de gasto y deuda (arts. 11 a 14)", f"""
{unidad("1.1 Instrumentación de la estabilidad: déficit estructural (art. 11)",
  lit("LOEP", "Artículo 11", ["Ninguna Administración Pública podrá incurrir en déficit estructural", "0,4 por ciento", "apreciadas por la mayoría absoluta de los miembros del Congreso de los Diputados", "plan de reequilibrio", "Las Corporaciones Locales deberán mantener una posición de equilibrio o superávit presupuestario"]),
  fichab("Prohibición de déficit estructural y sus excepciones",
         ["Ninguna Administración: sin déficit estructural (11.2)", "Corporaciones Locales y Seguridad Social: **equilibrio o superávit** (11.4 y 5)"],
         ["Déficit estructural = **déficit ajustado del ciclo, neto de medidas excepcionales y temporales**", "Reformas estructurales: hasta el **0,4 %** del PIB en el conjunto de Administraciones", "Excepciones (Estado y CC. AA.): catástrofes naturales, **recesión económica grave** o emergencia extraordinaria → **plan de reequilibrio**"],
         "Excepciones apreciadas por **mayoría absoluta de los miembros del Congreso**; la recesión grave exige tasa de crecimiento real anual **negativa** del PIB",
         "**0,4 %** solo por **reformas estructurales** y para el **conjunto** de Administraciones. Metodología: la de la **Comisión Europea** (11.6)."))}

{unidad("1.2 Regla de gasto (art. 12)",
  lit("LOEP", "Artículo 12", ["no podrá superar la tasa de referencia de crecimiento del Producto Interior Bruto de medio plazo", "Corresponde al Ministerio de Economía y Competitividad calcular", "Los ingresos que se obtengan por encima de lo previsto se destinarán íntegramente a reducir el nivel de deuda pública"], solo=[1, 3, 4, 7]),
  fichab("Límite al crecimiento del gasto computable",
         "Administración central, CC. AA. y Corporaciones Locales; calcula la tasa el **Ministerio de Economía**",
         ["Gasto computable: empleos no financieros (SEC), **excluidos** intereses de la deuda, gasto no discrecional en desempleo, gasto con fondos finalistas de la UE o de otras Administraciones y transferencias de los sistemas de financiación", "Ingresos superiores a lo previsto: **íntegramente** a reducir deuda"],
         "Tasa de referencia del PIB **de medio plazo**",
         "La Seguridad Social **no** aparece en la regla de gasto (12.1). Los **intereses de la deuda** se excluyen del gasto computable."))}

{unidad("1.3 Instrumentación de la sostenibilidad: límite de deuda (art. 13)",
  lit("LOEP", "Artículo 13", ["60 por ciento", "44 por ciento para la Administración central, 13 por ciento para el conjunto de Comunidades Autónomas y 3 por ciento para el conjunto de Corporaciones Locales", "no podrá realizar operaciones de endeudamiento neto", "habrán de estar autorizados por Ley"], solo=[1, 2, 3, 4, 5, 6, 7]),
  fichab("Límite de deuda pública y su reparto",
         "Conjunto de Administraciones Públicas",
         ["Límite global: **60 %** del PIB nacional nominal (o el de la normativa europea)", "Reparto: **44 %** Administración central, **13 %** CC. AA., **3 %** Corporaciones Locales", "Cada CC. AA.: máximo **13 %** de su PIB regional", "Quien supere su límite: **sin endeudamiento neto**"],
         "Superación solo en los casos del art. 11.3, con plan de reequilibrio",
         "**44 + 13 + 3 = 60**. Cayó en 2025 (P 83, → Cierre 1). El Estado y las CC. AA. necesitan **autorización por ley** para emitir deuda."))}

{unidad("1.4 Prioridad absoluta de pago de la deuda pública (art. 14)",
  lit("LOEP", "Artículo 14", ["no podrán ser objeto de enmienda o modificación", "prioridad absoluta frente a cualquier otro gasto"]),
  fichab("Garantía del pago de la deuda",
         "Todas las Administraciones Públicas",
         "Créditos de intereses y capital de la deuda: siempre incluidos en el estado de gastos",
         "—",
         "Prioridad **absoluta** frente a **cualquier otro gasto** (repite el art. 135.3 CE, → IV.1.2)."))}
""", 2)

T.ap("s17", "VI.2 Objetivos de estabilidad y deuda e informes de cumplimiento (arts. 15 a 17)", f"""
{unidad("2.1 Fijación de los objetivos (art. 15)",
  lit("LOEP", "Artículo 15", ["En el primer semestre de cada año", "referidos a los tres ejercicios siguientes", "antes del 1 de abril de cada año", "en un plazo máximo de 15 días", "límite de gasto no financiero", "aprobándose si este los ratifica por mayoría simple", "en el plazo máximo de un mes"], solo=[1, 2, 3, 9, 10, 11, 12, 13]),
  fichab("Objetivos de estabilidad presupuestaria y de deuda pública para el conjunto de Administraciones y cada subsector",
         ["Fija: el **Gobierno**, por acuerdo del Consejo de Ministros, a propuesta del Ministro de Hacienda", "Informan: el **Consejo de Política Fiscal y Financiera** y la **Comisión Nacional de Administración Local**", "Aprueban o rechazan: **Congreso y Senado**, sucesivamente, tras debate en Pleno"],
         "Objetivos en % del PIB nominal para los **tres ejercicios siguientes**; el acuerdo incluye el **límite de gasto no financiero** del Estado",
         ["Primer semestre del año", "Propuestas antes del **1 de abril**; informes en **15 días**", "Rechazo del Senado: el Congreso los aprueba si los ratifica por **mayoría simple**", "Rechazo: nuevo acuerdo del Gobierno en **un mes**"],
         "Si el **Senado** rechaza, basta la **mayoría simple** del Congreso para ratificar. Los proyectos de presupuesto se acomodan a los objetivos aprobados."))}

{unidad("2.2 Informes sobre el cumplimiento (art. 17)",
  lit("LOEP", "Artículo 17", ["Antes del 15 de octubre la Autoridad Independiente de Responsabilidad Fiscal", "Antes del 1 de abril de cada año, la Autoridad Independiente de Responsabilidad Fiscal", "Antes del 15 de abril de cada año, el Ministro de Hacienda", "Antes del 15 de octubre de cada año, el Ministro de Hacienda"], solo=[1, 2, 3, 4]),
  fichab("Calendario de informes de cumplimiento de los objetivos y de la regla de gasto",
         "AIReF y Ministro de Hacienda",
         ["AIReF, antes del **15 de octubre**: proyecto de PGE y líneas fundamentales (art. 27)", "AIReF, antes del **1 de abril**: presupuestos **iniciales**", "Ministro, antes del **15 de abril**: primer informe del ejercicio **anterior**", "Ministro, antes del **15 de octubre**: segundo informe del ejercicio anterior y previsión del corriente"],
         "—",
         "Fechas que se cruzan en los distractores: **15 de octubre**, **1 de abril**, **15 de abril**; y el **15 de julio** de la LO 6/2013 (→ VI.4.5). Se publican para general conocimiento."))}
""", 2)

T.ap("s18", "VI.3 Medidas preventivas, correctivas y coercitivas (arts. 18 a 26)", f"""
{unidad("3.1 Medidas automáticas de prevención (art. 18)",
  lit("LOEP", "Artículo 18", ["no se incumple el objetivo de estabilidad presupuestaria", "por encima del 95 %", "serán las de tesorería"], solo=[1, 3]),
  fichab("Seguimiento de la ejecución y umbral preventivo de deuda",
         "Todas las Administraciones Públicas",
         ["Seguimiento de la ejecución y ajuste del gasto", "Deuda por encima del **95 %** de su límite: solo operaciones de **tesorería**"],
         "—",
         "Umbral **95 %** del límite del art. 13.1."))}

{unidad("3.2 Advertencia de riesgo de incumplimiento (art. 19)",
  lit("LOEP", "Artículo 19", ["formulará una advertencia motivada", "el plazo de un mes"]),
  fichab("Alerta temprana a CC. AA. o Corporaciones Locales",
         "El **Gobierno**, a propuesta del Ministro de Hacienda, previa audiencia",
         "Advertencia motivada y pública; da cuenta al CPFF o a la CNAL",
         "La Administración advertida tiene **un mes** para adoptar medidas; si no, medidas correctivas",
         "Es el Gobierno quien advierte, y solo a **CC. AA.** o **Corporaciones Locales**."))}

{unidad("3.3 Plan económico-financiero (art. 21)",
  lit("LOEP", "Artículo 21", ["en el año en curso y el siguiente"], solo=[1]),
  fichab("Plan para corregir el incumplimiento del objetivo de estabilidad, de deuda o de la regla de gasto",
         "La Administración incumplidora",
         "Contenido mínimo: causas, previsiones tendenciales, medidas, previsiones y supuestos, análisis de sensibilidad (21.2)",
         "Cumplir **en el año en curso y el siguiente**",
         "Plan **económico-financiero** = incumplimiento; plan **de reequilibrio** = situaciones excepcionales del art. 11.3 (art. 22)."))}

{unidad("3.4 Tramitación de los planes (art. 23)",
  lit("LOEP", "Artículo 23", ["en el plazo máximo de un mes", "en el plazo máximo de dos meses", "no podrá exceder de tres meses", "se remitirá a las Cortes Generales"], solo=[1, 3]),
  fichab("Presentación, aprobación y puesta en marcha de los planes",
         "Administración central: el **Gobierno** los elabora y los aprueban las **Cortes** (procedimiento del 15.6)",
         "Previo informe de la AIReF cuando sea preceptivo",
         ["Presentación: **un mes** desde la constatación", "Aprobación: **dos meses** desde la presentación", "Puesta en marcha: no más de **tres meses** desde la constatación"],
         "**1 – 2 – 3**: un mes para presentar, dos para aprobar, tres para ponerlo en marcha."))}

{unidad("3.5 Medidas coercitivas (art. 25)",
  lit("LOEP", "Artículo 25", ["un depósito con intereses en el Banco de España equivalente al 0,2 % de su Producto Interior Bruto nominal", "Si en el plazo de 3 meses desde la constitución del depósito", "multa coercitiva", "comisión de expertos"], solo=[3, 4, 5]),
  fichab("Consecuencias de no presentar, no aprobar o incumplir el plan",
         "La Administración responsable; el **Gobierno** puede enviar una **comisión de expertos**",
         [f"a) No disponibilidad de créditos: {e(25, 'en el plazo de 15 días desde que se produzca el incumplimiento')}", "b) Depósito con intereses en el **Banco de España** del **0,2 %** del PIB nominal, si lo solicita el Ministerio de Hacienda", "Comisión de expertos: propuesta de medidas de **obligado cumplimiento**; conclusiones públicas en **una semana**"],
         ["**3 meses** sin plan o sin medidas: el depósito **no devenga intereses**", "Otros **3 meses**: puede convertirse en **multa coercitiva**"],
         "Plazos del depósito: **3 meses** (sin intereses) + **3 meses** (multa). **15 días** es el de la no disponibilidad. Cayó en 2025 (P 23, → Cierre 1)."))}

{unidad("3.6 Medidas de cumplimiento forzoso (art. 26)",
  lit("LOEP", "Artículo 26", ["artículo 155 de la Constitución Española", "con la aprobación por mayoría absoluta del Senado"], solo=[1, 2]),
  fichab("Último escalón frente a una Comunidad Autónoma incumplidora",
         "El **Gobierno**, conforme al **art. 155 CE**",
         "Requerimiento al Presidente de la Comunidad Autónoma; si no se atiende, medidas de ejecución forzosa e instrucciones a todas las autoridades autonómicas",
         "Aprobación por **mayoría absoluta del Senado**",
         "Aquí la mayoría absoluta es del **Senado** (art. 155), no del Congreso. Para Corporaciones Locales cabe la **disolución** de sus órganos (26.3)."))}
""", 2)

T.ap("s19", "VI.4 Gestión presupuestaria y Autoridad Independiente de Responsabilidad Fiscal (LO 2/2012, arts. 29 a 32; LO 6/2013)", f"""
{unidad("4.1 Plan presupuestario a medio plazo (art. 29)",
  lit("LOEP", "Artículo 29", ["se incluirá en el Programa de Estabilidad", "un periodo mínimo de tres años"], solo=[1, 2]),
  fichab("Marco a medio plazo de los presupuestos anuales",
         "—",
         "Objetivos de estabilidad, deuda y regla de gasto; proyecciones de ingresos y gastos; supuestos; evaluación de la sostenibilidad a largo plazo",
         "Periodo mínimo de **tres años**",
         "Se incluye en el **Programa de Estabilidad**."))}

{unidad("4.2 Límite de gasto no financiero (art. 30)",
  lit("LOEP", "Artículo 30", ["techo de asignación de recursos", "Antes del 1 de agosto de cada año"]),
  fichab("Techo de gasto de cada Administración",
         "Estado, Comunidades Autónomas y Corporaciones Locales, en sus ámbitos",
         "Coherente con el objetivo de estabilidad y la regla de gasto; excluye las transferencias de los sistemas de financiación",
         "Información al CPFF **antes del 1 de agosto**",
         "Lo aprueban también **CC. AA.** y **Corporaciones Locales**, no solo el Estado."))}

{unidad("4.3 Fondo de contingencia (art. 31)",
  lit("LOEP", "Artículo 31", ["necesidades de carácter no discrecional y no previstas"]),
  fichab("Dotación para imprevistos",
         "Estado, CC. AA. y Corporaciones Locales de los arts. 111 y 135 del texto refundido de Haciendas Locales",
         "Dotación diferenciada de créditos; cuantía y condiciones las fija cada Administración (la del Estado: LGP, art. 50, tema VI.2)",
         "—",
         "Necesidades **no discrecionales** y **no previstas**."))}

{unidad("4.4 Destino del superávit (art. 32)",
  lit("LOEP", "Artículo 32", ["a reducir el nivel de endeudamiento neto", "al Fondo de Reserva"], solo=[1, 2]),
  fichab("A qué se aplica el superávit presupuestario",
         ["Estado, CC. AA. y Corporaciones Locales: a **reducir el endeudamiento neto**", "Seguridad Social: prioritariamente al **Fondo de Reserva**"],
         "—",
         "—",
         "La Seguridad Social **no** lo destina a reducir deuda, sino al **Fondo de Reserva**."))}

{unidad("4.5 La Autoridad Independiente de Responsabilidad Fiscal (LO 6/2013, arts. 1, 2 y 17)",
  lit("LO6_2013", "Artículo 1", ["autonomía e independencia funcional"]),
  lit("LO6_2013", "Artículo 2", ["garantizar el cumplimiento efectivo por las Administraciones Públicas del principio de estabilidad presupuestaria"]),
  lit("LO6_2013", "Artículo 17", ["Antes del 15 de julio de cada año"]),
  fichab("Ente que vigila el cumplimiento de la estabilidad presupuestaria",
         f"{c('LO6_2013', 'Artículo 1', 'ente de Derecho Público dotado de personalidad jurídica propia y plena capacidad pública y privada')}",
         "Evaluación continua del ciclo presupuestario, del endeudamiento y de las previsiones económicas, mediante informes, opiniones y estudios",
         "Informe sobre el ejercicio en curso **antes del 15 de julio** (art. 17); además, los de la LO 2/2012 (→ VI.2.2)",
         "Su fin es el principio de estabilidad del **art. 135 CE**. **15 de julio**: ejecución del ejercicio en curso. Cayó en 2025 (L 33, → Cierre 1)."))}

{resumen([
  "Sin **déficit estructural** (0,4 % solo por reformas estructurales); excepciones por **mayoría absoluta del Congreso**; Corporaciones Locales y Seguridad Social en **equilibrio o superávit** (art. 11).",
  "**Regla de gasto**: tasa de referencia del PIB de medio plazo (art. 12). **Deuda**: 60 % = **44 / 13 / 3** (art. 13); **prioridad absoluta** de pago (art. 14).",
  "Objetivos: Gobierno en el **primer semestre**, para **tres** ejercicios; aprueban Congreso y Senado (art. 15). Informes del 17.",
  "Medidas: prevención (95 %), advertencia (**un mes**), plan económico-financiero, coercitivas (**15 días**, depósito del **0,2 %**, **3 + 3 meses**) y cumplimiento forzoso (**art. 155**, mayoría absoluta del **Senado**).",
  "Plan a medio plazo (**tres** años), límite de gasto no financiero, fondo de contingencia, superávit; **AIReF** (LO 6/2013)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_L83 = examen("L", 83, {
  "a": f"Incompleta: el art. 3.2 dice {e(3, 'la situación de equilibrio o superávit estructural')}; falta «o superávit».",
  "b": f"Incompleta: falta el equilibrio; la ley dice {e(3, 'equilibrio o superávit estructural')}.",
  "c": f"Literal del art. 3.2 LO 2/2012: {e(3, 'Se entenderá por estabilidad presupuestaria de las Administraciones Públicas la situación de equilibrio o superávit estructural')}.",
  "d": f"Es la definición de **sostenibilidad financiera** (art. 4.2): {e(4, 'la capacidad para financiar compromisos de gasto presentes y futuros dentro de los límites de déficit')}."},
  [("equilibrio o superávit estructural", "LOEP", "Artículo 3", "Se entenderá por estabilidad presupuestaria de las Administraciones Públicas la situación de equilibrio o superávit estructural")])
EX_P23 = examen("P", 23, {
  "a": f"Quince días es el plazo para aprobar la no disponibilidad de créditos (art. 25.1 a): {e(25, 'en el plazo de 15 días desde que se produzca el incumplimiento')}.",
  "b": f"Literal del art. 25.1 b): {e(25, 'Si en el plazo de 3 meses desde la constitución del depósito no se hubiera presentado o aprobado el plan, o no se hubieran aplicado las medidas, el depósito no devengará intereses')} (3 meses = tres meses).",
  "c": "Treinta días no aparece en el art. 25.1 b): el plazo es de 3 meses.",
  "d": f"Seis meses sería la suma de los dos plazos: tras {e(25, 'un nuevo plazo de 3 meses')} el depósito puede convertirse en multa coercitiva."},
  [("Tres meses", "LOEP", "Artículo 25", "Si en el plazo de 3 meses desde la constitución del depósito no se hubiera presentado o aprobado el plan, o no se hubieran aplicado las medidas, el depósito no devengará intereses")])
EX_P26 = examen("P", 26, {
  "a": f"Falso: {c('CE', 'Artículo 135', 'El Estado y las Comunidades Autónomas no podrán incurrir en un déficit estructural que supere los márgenes establecidos')} (art. 135.2).",
  "b": f"Literal del art. 135.1: {c('CE', 'Artículo 135', 'Todas las Administraciones Públicas adecuarán sus actuaciones al principio de estabilidad presupuestaria')}.",
  "c": f"El art. 135 no condiciona nada a la Unión Europea en ese sentido; y la LO 2/2012 somete a todas: {e(4, 'estarán sujetas al principio de sostenibilidad financiera')}.",
  "d": f"Al revés: el pago de la deuda {c('CE', 'Artículo 135', 'gozará de prioridad absoluta')} (art. 135.3)."},
  [("adecuar sus actuaciones al principio de estabilidad presupuestaria", "CE", "Artículo 135", "Todas las Administraciones Públicas adecuarán sus actuaciones al principio de estabilidad presupuestaria")])
EX_P83 = examen("P", 83, {
  "a": "Cambia el reparto entre Administración central y CC. AA. (47 y 10): la ley dice 44 y 13.",
  "b": "Cambia los tres porcentajes (45, 10 y 5).",
  "c": f"Literal del art. 13.1: {e(13, '44 por ciento para la Administración central, 13 por ciento para el conjunto de Comunidades Autónomas y 3 por ciento para el conjunto de Corporaciones Locales')}.",
  "d": "Cambia los tres porcentajes (40, 15 y 5)."},
  [("44 %", "LOEP", "Artículo 13", "44 por ciento para la Administración central"), ("13 %", "LOEP", "Artículo 13", "13 por ciento para el conjunto de Comunidades Autónomas"), ("3 % para las Corporaciones Locales", "LOEP", "Artículo 13", "3 por ciento para el conjunto de Corporaciones Locales")])
EX_P84 = examen("P", 84, {
  "a": f"Literal del art. 2.3, párrafo segundo, LGP: {c('LGP', 'a2', 'esta Ley no será de aplicación a las Cortes Generales, que gozan de autonomía presupuestaria')}.",
  "b": f"Incluidos: {c('LGP', 'a2', 'f) Los fondos sin personalidad jurídica.')} (art. 2.2 f).",
  "c": f"Incluidas: {c('LGP', 'a2', 'las mutuas colaboradoras con la Seguridad Social en su función pública de colaboración en la gestión de la Seguridad Social')} (art. 2.2 h).",
  "d": f"Incluidos: {c('LGP', 'a2', 'd) Los consorcios adscritos a la Administración General del Estado.')} (art. 2.2 d)."},
  [("Cortes Generales", "LGP", "a2", "esta Ley no será de aplicación a las Cortes Generales")])
EX_X90 = examen("X", 90, {
  "a": f"Le falta un subsector: {e(2, 'd) Administraciones de Seguridad Social.')}",
  "b": f"Le faltan los organismos de la administración central y las Corporaciones Locales: {e(2, 'a) Administración central, que comprende el Estado y los organismos de la administración central.')}",
  "c": f"Le falta un subsector: {e(2, 'b) Comunidades Autónomas.')}",
  "d": f"Literal del art. 2.1: los cuatro subsectores a) a d), {e(2, 'Administración central, que comprende el Estado y los organismos de la administración central')}, Comunidades Autónomas, Corporaciones Locales y Administraciones de Seguridad Social."},
  [("organismos de la administración central", "LOEP", "Artículo 2", "Administración central, que comprende el Estado y los organismos de la administración central"),
   ("Comunidades Autónomas", "LOEP", "Artículo 2", "b) Comunidades Autónomas."),
   ("Corporaciones Locales", "LOEP", "Artículo 2", "c) Corporaciones Locales."),
   ("Administraciones de Seguridad Social", "LOEP", "Artículo 2", "d) Administraciones de Seguridad Social.")])
EX_X92 = examen("X", 92, {
  "a": "No es el nombre que la ley da a esa exigencia: la exposición de motivos de la LGP la llama principio de universalidad.",
  "b": f"La anualidad es otra nota del art. 134.2 ({c('CE', 'Artículo 134', 'tendrán carácter anual')}), que rige la aprobación y ejecución ({e(5, 'el principio de anualidad por el que se rigen la aprobación y ejecución de los Presupuestos')}), no la inclusión de todos los ingresos y gastos.",
  "c": f"Exposición de motivos de la LGP: {c('LGP', 'preambulo', 'Como reflejo del principio de universalidad del presupuesto, consagrado en el artículo 134 de la Constitución española')}; y el art. 134.2 CE: {c('CE', 'Artículo 134', 'incluirán la totalidad de los gastos e ingresos del sector público estatal')}.",
  "d": f"La transparencia se refiere a la información: {e(6, 'deberán contener información suficiente y adecuada')} (art. 6 LO 2/2012)."},
  [("universalidad", "LGP", "preambulo", "Como reflejo del principio de universalidad del presupuesto, consagrado en el artículo 134 de la Constitución española")])
EX_L33 = examen("L", 33, {
  "a": f"15 de octubre es el informe de la AIReF sobre el **proyecto** de PGE: {e(17, 'Antes del 15 de octubre la Autoridad Independiente de Responsabilidad Fiscal hará público')} (LO 2/2012, art. 17.1).",
  "b": f"1 de abril es el informe de la AIReF sobre los presupuestos **iniciales** (LO 2/2012, art. 17.2): {e(17, 'Antes del 1 de abril de cada año, la Autoridad Independiente de Responsabilidad Fiscal')}.",
  "c": f"15 de abril es el primer informe del **Ministro** de Hacienda sobre el ejercicio anterior: {e(17, 'Antes del 15 de abril de cada año, el Ministro de Hacienda')}.",
  "d": f"Literal del art. 17 LO 6/2013: {c('LO6_2013', 'Artículo 17', 'Antes del 15 de julio de cada año, la Autoridad Independiente de Responsabilidad Fiscal informará')}."},
  [("15 de julio", "LO6_2013", "Artículo 17", "Antes del 15 de julio de cada año, la Autoridad Independiente de Responsabilidad Fiscal informará")])

T.ap("s20", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **siete** preguntas válidas de este tema (una en el turno libre, cuatro en promoción interna y dos en el extraordinario; la L 82 fue **anulada**) y **una** relacionada (la L 33, sin tema asignado, sobre la AIReF). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-L 2025, pregunta 83 · Definición de estabilidad presupuestaria (→ V.1.1)", EX_L83,
  "### GACE-P 2025, pregunta 23 · Depósito del art. 25.1 b) (→ VI.3.5)", EX_P23,
  "### GACE-P 2025, pregunta 26 · Art. 135 CE (→ IV.1.1)", EX_P26,
  "### GACE-P 2025, pregunta 83 · Reparto del límite de deuda (→ VI.1.3)", EX_P83,
  "### GACE-P 2025, pregunta 84 · Ámbito de la Ley General Presupuestaria (→ II.1.2)", EX_P84,
  "### GACE-L 2025 extraordinario, pregunta 90 · Sector Administraciones Públicas (→ IV.3.2)", EX_X90,
  "### GACE-L 2025 extraordinario, pregunta 92 · Principio de universalidad (→ I.1.3)", EX_X92,
  "### GACE-L 2025, pregunta 33 · Informe de la AIReF de 15 de julio (relacionada; → VI.4.5)", EX_L33,
  "### Cómo se pregunta",
  "!> La LO 2/2012 se pregunta **con números y fechas**: porcentajes de deuda (44 / 13 / 3), plazos de las medidas (15 días, 3 + 3 meses), fechas de los informes (1 de abril, 15 de abril, 15 de julio, 15 de octubre). Y con **definiciones cruzadas**: la de sostenibilidad como distractor de la de estabilidad.",
]))

T.ap("s21", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Concepto y clases | Expresión cifrada, conjunta y sistemática (32); limitativos y estimativos (33); año natural (34) | **Universalidad** = totalidad de gastos e ingresos (134.2 CE) |
| II. La LGP | Objeto (1); sector público estatal (2); tres sectores (3); siete títulos | **No** se aplica a las **Cortes Generales** |
| III. Principios de la LGP | Siete principios de programación (26); reglas de gestión (27); escenarios a tres años (28) | Créditos **exclusivamente** a su finalidad; afectación solo **por ley** |
| IV. Leyes de estabilidad | Art. 135 CE; leyes de 2001 y 2007 derogadas; LO 2/2012 | **Cuatro** subsectores (central, CC. AA., CC. LL., Seguridad Social) |
| V. Principios de la LO 2/2012 | Estabilidad, sostenibilidad, plurianualidad, transparencia, eficiencia, responsabilidad, lealtad | Estabilidad = **equilibrio o superávit estructural** |
| VI. Cumplimiento | Déficit (11), regla de gasto (12), deuda (13), objetivos (15), medidas (18 a 26), AIReF | Deuda **44 / 13 / 3**; depósito: **3 meses** sin intereses |

?> **Trampas frecuentes:** «estabilidad = equilibrio estructural» (es **equilibrio o superávit**); «las excepciones las aprecia la mayoría absoluta del Senado» (del **Congreso**, art. 135.4 CE y 11.3; el **Senado** aparece en el cumplimiento forzoso del art. 26); «la Seguridad Social destina el superávit a reducir deuda» (al **Fondo de Reserva**); «la LGP se aplica a las Cortes Generales» (gozan de **autonomía presupuestaria**); «los consorcios tienen presupuesto limitativo» (van a los **estimativos**, 33.1 b).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
Q = T.q
Q("LGP", "Artículo 32", "Concepto", "Según el artículo 32 de la Ley 47/2003, General Presupuestaria, los Presupuestos Generales del Estado constituyen la expresión:",
  ["Cifrada, conjunta y sistemática de los derechos y obligaciones a liquidar durante el ejercicio.", "Cifrada, conjunta y sistemática de los ingresos y gastos previstos para los tres ejercicios siguientes.", "Contable y detallada de los ingresos y gastos realizados en el ejercicio anterior.", "Cifrada y separada de los créditos de cada departamento ministerial."],
  "Art. 32 LGP.", "la expresión cifrada, conjunta y sistemática de los derechos y obligaciones a liquidar durante el ejercicio")
Q("CE", "Artículo 134", "Concepto", "Según el artículo 134.2 de la Constitución, los Presupuestos Generales del Estado:",
  ["Tendrán carácter anual e incluirán la totalidad de los gastos e ingresos del sector público estatal.", "Tendrán carácter bienal e incluirán la totalidad de los gastos del sector público estatal.", "Tendrán carácter anual e incluirán solo los gastos e ingresos de la Administración General del Estado.", "Tendrán carácter plurianual y se aprobarán para tres ejercicios."],
  "Art. 134.2 CE.", "tendrán carácter anual, incluirán la totalidad de los gastos e ingresos del sector público estatal")
Q("LGP", "preambulo", "Concepto", "Según la exposición de motivos de la Ley 47/2003, General Presupuestaria, la enumeración completa de las entidades que integran el sector público estatal es reflejo del principio de:",
  ["Universalidad del presupuesto, consagrado en el artículo 134 de la Constitución.", "Anualidad del presupuesto, consagrado en el artículo 135 de la Constitución.", "Estabilidad presupuestaria, consagrado en el artículo 135 de la Constitución.", "Transparencia, consagrado en el artículo 103 de la Constitución."],
  "Exposición de motivos, II, LGP.", "Como reflejo del principio de universalidad del presupuesto, consagrado en el artículo 134 de la Constitución española")
Q("LGP", "Artículo 33", "Clases", "Según el artículo 33.1 b) de la Ley General Presupuestaria, forman parte de los Presupuestos Generales del Estado como presupuestos estimativos los de:",
  ["Los consorcios, las universidades no transferidas y los fondos sin personalidad jurídica.", "Los organismos autónomos.", "Los órganos con dotación diferenciada del artículo 2.3.", "La Administración General del Estado."],
  "Art. 33.1 b) LGP.", "Los presupuestos estimativos de las entidades de los sectores empresarial y fundacional, los consorcios, las universidades no transferidas, los fondos sin personalidad jurídica")
Q("LGP", "Artículo 33", "Clases", "Según el artículo 33.2 a) de la Ley General Presupuestaria, respecto de los sujetos con presupuesto limitativo, los Presupuestos Generales del Estado determinarán:",
  ["Las obligaciones económicas que, como máximo, pueden reconocer.", "Las obligaciones económicas que, como mínimo, deben reconocer.", "Las operaciones no financieras y financieras a realizar.", "La previsión de la cuenta de resultados."],
  "Art. 33.2 a) LGP.", "Las obligaciones económicas que, como máximo, pueden reconocer")
Q("LGP", "Artículo 33", "Clases", "Según el artículo 33.2 e) de la Ley General Presupuestaria, los Presupuestos Generales del Estado determinarán:",
  ["La estimación de los beneficios fiscales que afecten a los tributos del Estado.", "La relación de tributos que se crean en el ejercicio.", "El límite de deuda de las Comunidades Autónomas.", "El objetivo de estabilidad de las Corporaciones Locales."],
  "Art. 33.2 e) LGP.", "La estimación de los beneficios fiscales que afecten a los tributos del Estado")
Q("LGP", "Artículo 64", "Clases", "Según el artículo 64 de la Ley General Presupuestaria, las sociedades mercantiles estatales y las entidades públicas empresariales elaborarán:",
  ["Un presupuesto de explotación y un presupuesto de capital, que se integrarán en los Presupuestos Generales del Estado.", "Un presupuesto limitativo de gastos y un presupuesto estimativo de ingresos.", "Un presupuesto de explotación que no se integra en los Presupuestos Generales del Estado.", "Únicamente una previsión del balance."],
  "Art. 64.1 LGP.", "Los presupuestos de explotación y de capital se integrarán en los Presupuestos Generales del Estado")
Q("LGP", "Artículo 34", "Ámbito temporal", "Según el artículo 34.1 de la Ley General Presupuestaria, el ejercicio presupuestario:",
  ["Coincidirá con el año natural.", "Comenzará el 1 de julio y terminará el 30 de junio.", "Coincidirá con la legislatura.", "Será el que fije cada Ley de Presupuestos."],
  "Art. 34.1 LGP.", "El ejercicio presupuestario coincidirá con el año natural")
Q("LGP", "Artículo 34", "Ámbito temporal", "Según el artículo 34.1 a) de la Ley General Presupuestaria, al ejercicio presupuestario se imputarán los derechos económicos liquidados durante el ejercicio:",
  ["Cualquiera que sea el período del que deriven.", "Siempre que deriven del propio ejercicio.", "Siempre que se hayan ingresado antes del 31 de diciembre del ejercicio anterior.", "Solo si derivan de tributos del Estado."],
  "Art. 34.1 a) LGP.", "Los derechos económicos liquidados durante el ejercicio, cualquiera que sea el período del que deriven")
Q("LGP", "Artículo 34", "Ámbito temporal", "Según el artículo 34.4 de la Ley General Presupuestaria, la imputación a presupuesto de obligaciones de ejercicios anteriores no comprendidas en los supuestos previstos requerirá:",
  ["Norma con rango de ley que la autorice.", "Acuerdo del Consejo de Ministros.", "Informe favorable de la Intervención General.", "Resolución del Ministro de Hacienda."],
  "Art. 34.4 LGP.", "la imputación requerirá norma con rango de ley que la autorice")
Q("LGP", "Artículo 35", "Créditos y programas", "Según el artículo 35.1 de la Ley General Presupuestaria, son créditos presupuestarios:",
  ["Cada una de las asignaciones individualizadas de gasto puestas a disposición de los centros gestores.", "El conjunto de gastos orientado a la consecución de objetivos preestablecidos.", "Las previsiones de ingresos de cada ejercicio.", "Los compromisos de gasto con cargo a ejercicios posteriores."],
  "Art. 35.1 LGP.", "Son créditos presupuestarios cada una de las asignaciones individualizadas de gasto")
Q("LGP", "Artículo 1", "Ley General Presupuestaria", "Según el artículo 1 de la Ley 47/2003, la Ley General Presupuestaria tiene por objeto la regulación del régimen presupuestario, económico-financiero, de contabilidad, intervención y de control financiero:",
  ["Del sector público estatal.", "De todas las Administraciones Públicas.", "De la Administración General del Estado exclusivamente.", "Del sector público estatal, autonómico y local."],
  "Art. 1 LGP.", "de control financiero del sector público estatal")
Q("LGP", "Artículo 2", "Ley General Presupuestaria", "Según el artículo 2.3 de la Ley General Presupuestaria, la ley no será de aplicación a:",
  ["Las Cortes Generales, que gozan de autonomía presupuestaria.", "Las universidades públicas no transferidas.", "Las autoridades administrativas independientes.", "Los fondos sin personalidad jurídica."],
  "Art. 2.3 LGP.", "esta Ley no será de aplicación a las Cortes Generales, que gozan de autonomía presupuestaria")
Q("LGP", "Artículo 3", "Ley General Presupuestaria", "Según el artículo 3 de la Ley General Presupuestaria, las entidades públicas empresariales forman parte del:",
  ["Sector público empresarial.", "Sector público administrativo.", "Sector público fundacional.", "Sector público institucional autonómico."],
  "Art. 3.2 a) LGP.", "El sector público empresarial, integrado por: a) Las entidades públicas empresariales.")
Q("LGP", "Artículo 3", "Ley General Presupuestaria", "Según el artículo 3.1 a) de la Ley General Presupuestaria, los organismos autónomos forman parte del:",
  ["Sector público administrativo.", "Sector público empresarial.", "Sector público fundacional.", "Sector público estimativo."],
  "Art. 3.1 a) LGP.", "El sector público administrativo, integrado por: a) La Administración General del Estado, los organismos autónomos")
Q("LGP", "tvi", "Ley General Presupuestaria", "En la Ley General Presupuestaria, el título VI se dedica:",
  ["Al control de la gestión económico-financiera efectuado por la Intervención General de la Administración del Estado.", "A los Presupuestos Generales del Estado.", "A la contabilidad del sector público estatal.", "Al Tesoro Público y la Deuda del Estado."],
  "Rúbrica del título VI LGP (I: ámbito y Hacienda Pública; II: PGE; III: relaciones financieras; IV: Tesoro y Deuda; V: contabilidad; VII: responsabilidades).", "Del control de la gestión económico-financiera efectuado por la Intervención General de la Administración del Estado")
Q("LGP", "Artículo 26", "Principios de la LGP", "Según el artículo 26.1 de la Ley General Presupuestaria, la programación presupuestaria se regirá, entre otros, por los principios de:",
  ["Estabilidad presupuestaria, sostenibilidad financiera, plurianualidad y transparencia.", "Unidad de caja, especialidad y presupuesto bruto.", "Legalidad, jerarquía y descentralización.", "Anualidad, universalidad y no afectación."],
  "Art. 26.1 LGP: estabilidad, sostenibilidad, plurianualidad, transparencia, eficiencia, responsabilidad y lealtad institucional.", "estabilidad presupuestaria, sostenibilidad financiera, plurianualidad, transparencia")
Q("LGP", "Artículo 27", "Principios de la LGP", "Según el artículo 27.1 de la Ley General Presupuestaria, la gestión del sector público estatal está sometida al régimen de presupuesto:",
  ["Anual aprobado por las Cortes Generales y enmarcado en los límites de un escenario plurianual.", "Plurianual aprobado por el Gobierno.", "Anual aprobado por el Consejo de Ministros.", "Bienal aprobado por las Cortes Generales."],
  "Art. 27.1 LGP.", "régimen de presupuesto anual aprobado por las Cortes Generales y enmarcado en los límites de un escenario plurianual")
Q("LGP", "Artículo 27", "Principios de la LGP", "Según el artículo 27.3 de la Ley General Presupuestaria, los recursos del Estado se destinarán a satisfacer el conjunto de sus respectivas obligaciones, salvo que se establezca su afectación a fines determinados:",
  ["Por ley.", "Por real decreto.", "Por orden del Ministro de Hacienda.", "Por acuerdo de la Comisión Delegada para Asuntos Económicos."],
  "Art. 27.3 LGP.", "salvo que por ley se establezca su afectación a fines determinados")
Q("LGP", "Artículo 27", "Principios de la LGP", "Según el artículo 27.2 de la Ley General Presupuestaria, el carácter limitativo y vinculante de los créditos será el correspondiente:",
  ["Al nivel de especificación con que aparezcan.", "Al nivel de capítulo en todo caso.", "Al nivel de subconcepto en todo caso.", "Al que fije cada centro gestor."],
  "Art. 27.2 LGP.", "El carácter limitativo y vinculante de dichos créditos será el correspondiente al nivel de especificación con que aparezcan")
Q("LGP", "Artículo 27", "Principios de la LGP", "Según el artículo 27.4 de la Ley General Presupuestaria, los derechos liquidados y las obligaciones reconocidas se aplicarán a los presupuestos:",
  ["Por su importe íntegro.", "Por su importe neto.", "Por el saldo resultante de compensar derechos y obligaciones.", "Por el importe recaudado."],
  "Art. 27.4 LGP.", "se aplicarán a los presupuestos por su importe íntegro")
Q("LGP", "Artículo 28", "Principios de la LGP", "Según el artículo 28 de la Ley General Presupuestaria, los escenarios presupuestarios plurianuales:",
  ["Serán confeccionados por el Ministerio de Hacienda y determinarán límites referidos a los tres ejercicios siguientes.", "Serán aprobados por las Cortes Generales para los cinco ejercicios siguientes.", "Serán confeccionados por cada ministerio para los dos ejercicios siguientes.", "Serán elaborados por la Autoridad Independiente de Responsabilidad Fiscal."],
  "Art. 28.1 y 3 LGP.", ["referidos a los tres ejercicios siguientes", "serán confeccionados por el Ministerio de Hacienda"])
Q("LGP", "Artículo 29", "Principios de la LGP", "Según el artículo 29.3 de la Ley General Presupuestaria, el programa plurianual de cada ministerio:",
  ["Se aprobará por el Ministro.", "Se aprobará por el Consejo de Ministros.", "Se aprobará por el Ministro de Hacienda.", "Se aprobará por las Cortes Generales."],
  "Art. 29.3 LGP.", "se aprobará por el Ministro")
Q("CE", "Artículo 135", "Art. 135 CE", "Según el artículo 135.2 de la Constitución, las Entidades Locales deberán presentar:",
  ["Equilibrio presupuestario.", "Un déficit estructural no superior al fijado por ley orgánica.", "Superávit en todo caso.", "Un déficit no superior al 0,4 % de su producto interior bruto."],
  "Art. 135.2 CE.", "Las Entidades Locales deberán presentar equilibrio presupuestario")
Q("CE", "Artículo 135", "Art. 135 CE", "Según el artículo 135.4 de la Constitución, la concurrencia de las situaciones que permiten superar los límites de déficit estructural y de deuda pública será apreciada por:",
  ["La mayoría absoluta de los miembros del Congreso de los Diputados.", "La mayoría absoluta del Senado.", "La mayoría de tres quintos de ambas Cámaras.", "El Gobierno, previo informe del Banco de España."],
  "Art. 135.4 CE.", "apreciadas por la mayoría absoluta de los miembros del Congreso de los Diputados")
Q("CE", "Artículo 135", "Art. 135 CE", "Según el artículo 135.3 de la Constitución, el pago de los créditos para satisfacer los intereses y el capital de la deuda pública de las Administraciones:",
  ["Gozará de prioridad absoluta.", "Gozará de prioridad sobre los gastos de inversión, pero no sobre los de personal.", "Requerirá autorización anual de las Cortes.", "Podrá ser objeto de enmienda en la Ley de Presupuestos."],
  "Art. 135.3 CE.", "su pago gozará de prioridad absoluta")
Q("LOEP", "ddunica", "Leyes de estabilidad", "La Ley Orgánica 2/2012, de Estabilidad Presupuestaria y Sostenibilidad Financiera, derogó:",
  ["La Ley Orgánica 5/2001 y el texto refundido de la Ley General de Estabilidad Presupuestaria de 2007.", "La Ley 47/2003, General Presupuestaria.", "La Ley Orgánica 6/2013, de la Autoridad Independiente de Responsabilidad Fiscal.", "La Ley Orgánica 8/1980, de Financiación de las Comunidades Autónomas."],
  "Disposición derogatoria única LO 2/2012.", ["Queda derogada la Ley orgánica 5/2001, de 13 de diciembre", "Real Decreto Legislativo 2/2007, de 28 de diciembre"])
Q("LOEP", "Artículo 3", "Principios de la LO 2/2012", "Según el artículo 3.3 de la Ley Orgánica 2/2012, para las entidades públicas empresariales y sociedades mercantiles del artículo 2.2 se entenderá por estabilidad presupuestaria:",
  ["La posición de equilibrio financiero.", "La situación de equilibrio o superávit estructural.", "La capacidad para financiar compromisos de gasto presentes y futuros.", "La ausencia de déficit estructural superior al 0,4 %."],
  "Art. 3.3 LO 2/2012.", "se entenderá por estabilidad presupuestaria la posición de equilibrio financiero")
Q("LOEP", "Artículo 4", "Principios de la LO 2/2012", "Según el artículo 4.2 de la Ley Orgánica 2/2012, se entiende que existe sostenibilidad de la deuda comercial cuando:",
  ["El periodo medio de pago a los proveedores no supere el plazo máximo previsto en la normativa sobre morosidad.", "La deuda comercial no supere el 3 % del PIB.", "El periodo medio de pago no supere los noventa días en todo caso.", "No existan facturas pendientes al cierre del ejercicio."],
  "Art. 4.2 LO 2/2012.", "cuando el periodo medio de pago a los proveedores no supere el plazo máximo previsto en la normativa sobre morosidad")
Q("LOEP", "Artículo 5", "Principios de la LO 2/2012", "Según el artículo 5 de la Ley Orgánica 2/2012, el marco presupuestario a medio plazo es compatible con el principio de:",
  ["Anualidad por el que se rigen la aprobación y ejecución de los Presupuestos.", "Universalidad por el que se rige la elaboración de los Presupuestos.", "Especialidad cuantitativa de los créditos.", "Unidad de caja."],
  "Art. 5 LO 2/2012.", "compatible con el principio de anualidad por el que se rigen la aprobación y ejecución de los Presupuestos")
Q("LOEP", "Artículo 7", "Principios de la LO 2/2012", "Según el artículo 7.2 de la Ley Orgánica 2/2012, la gestión de los recursos públicos estará orientada por:",
  ["La eficacia, la eficiencia, la economía y la calidad.", "La legalidad, la jerarquía y la coordinación.", "La transparencia, la publicidad y la concurrencia.", "La estabilidad, la sostenibilidad y la prudencia."],
  "Art. 7.2 LO 2/2012.", "La gestión de los recursos públicos estará orientada por la eficacia, la eficiencia, la economía y la calidad")
Q("LOEP", "Artículo 8", "Principios de la LO 2/2012", "Según el artículo 8.2 de la Ley Orgánica 2/2012, el Estado:",
  ["No asumirá ni responderá de los compromisos de las Comunidades Autónomas, sin perjuicio de las garantías financieras mutuas para la realización conjunta de proyectos específicos.", "Responderá subsidiariamente de los compromisos de las Comunidades Autónomas.", "Asumirá los compromisos de las Corporaciones Locales cuando la Comunidad Autónoma no lo haga.", "Responderá solidariamente de los compromisos de las Comunidades Autónomas ante la Unión Europea."],
  "Art. 8.2 LO 2/2012.", "El Estado no asumirá ni responderá de los compromisos de las Comunidades Autónomas")
Q("LOEP", "Artículo 11", "Límites", "Según el artículo 11.2 de la Ley Orgánica 2/2012, en caso de reformas estructurales con efectos presupuestarios a largo plazo, podrá alcanzarse en el conjunto de Administraciones Públicas un déficit estructural de:",
  ["El 0,4 por ciento del Producto Interior Bruto nacional expresado en términos nominales.", "El 3 por ciento del Producto Interior Bruto nacional.", "El 1 por ciento del Producto Interior Bruto nacional.", "El 0,2 por ciento del Producto Interior Bruto nacional."],
  "Art. 11.2 LO 2/2012.", "un déficit estructural del 0,4 por ciento del Producto Interior Bruto nacional expresado en términos nominales")
Q("LOEP", "Artículo 11", "Límites", "Según el artículo 11.2 de la Ley Orgánica 2/2012, el déficit estructural se define como:",
  ["Déficit ajustado del ciclo, neto de medidas excepcionales y temporales.", "Déficit total del ejercicio, incluidas las medidas temporales.", "Diferencia entre ingresos y gastos financieros.", "Déficit primario, excluidos los intereses de la deuda."],
  "Art. 11.2 LO 2/2012.", "definido como déficit ajustado del ciclo, neto de medidas excepcionales y temporales")
Q("LOEP", "Artículo 12", "Límites", "Según el artículo 12.5 de la Ley Orgánica 2/2012, los ingresos que se obtengan por encima de lo previsto:",
  ["Se destinarán íntegramente a reducir el nivel de deuda pública.", "Se destinarán a financiar nuevos gastos de inversión.", "Se incorporarán al Fondo de Contingencia.", "Se destinarán en un 50 % a reducir deuda."],
  "Art. 12.5 LO 2/2012.", "Los ingresos que se obtengan por encima de lo previsto se destinarán íntegramente a reducir el nivel de deuda pública")
Q("LOEP", "Artículo 13", "Límites", "Según el artículo 13.1 de la Ley Orgánica 2/2012, el límite de deuda pública de cada una de las Comunidades Autónomas no podrá superar:",
  ["El 13 por ciento de su Producto Interior Bruto regional.", "El 3 por ciento de su Producto Interior Bruto regional.", "El 44 por ciento de su Producto Interior Bruto regional.", "El 60 por ciento de su Producto Interior Bruto regional."],
  "Art. 13.1 LO 2/2012.", "no podrá superar el 13 por ciento de su Producto Interior Bruto regional")
Q("LOEP", "Artículo 15", "Objetivos", "Según el artículo 15.6 de la Ley Orgánica 2/2012, si aprobados los objetivos de estabilidad por el Congreso fuesen rechazados por el Senado:",
  ["Se someterán a nueva votación en el Pleno del Congreso, aprobándose si este los ratifica por mayoría simple.", "Quedarán definitivamente rechazados.", "El Congreso deberá ratificarlos por mayoría absoluta.", "Se someterán a una comisión mixta Congreso-Senado."],
  "Art. 15.6 LO 2/2012.", "aprobándose si este los ratifica por mayoría simple")
Q("LOEP", "Artículo 15", "Objetivos", "Según el artículo 15.1 de la Ley Orgánica 2/2012, los objetivos de estabilidad presupuestaria y de deuda pública los fija:",
  ["El Gobierno, mediante acuerdo del Consejo de Ministros, en el primer semestre de cada año.", "El Consejo de Política Fiscal y Financiera, en el segundo semestre.", "El Ministro de Hacienda, mediante orden, antes del 1 de abril.", "La Autoridad Independiente de Responsabilidad Fiscal, en el primer semestre."],
  "Art. 15.1 LO 2/2012.", "En el primer semestre de cada año, el Gobierno, mediante acuerdo del Consejo de Ministros")
Q("LOEP", "Artículo 18", "Medidas", "Según el artículo 18.2 de la Ley Orgánica 2/2012, cuando el volumen de deuda pública se sitúe por encima del 95 % de los límites, las únicas operaciones de endeudamiento permitidas serán:",
  ["Las de tesorería.", "Las de refinanciación a largo plazo.", "Las autorizadas por el Consejo de Ministros.", "Las emisiones de deuda en mercados internacionales."],
  "Art. 18.2 LO 2/2012.", "las únicas operaciones de endeudamiento permitidas a la Administración Pública correspondiente serán las de tesorería")
Q("LOEP", "Artículo 23", "Medidas", "Según el artículo 23.1 de la Ley Orgánica 2/2012, los planes económico-financieros deberán ser aprobados en el plazo máximo de:",
  ["Dos meses desde su presentación.", "Un mes desde su presentación.", "Tres meses desde su presentación.", "Quince días desde su presentación."],
  "Art. 23.1 LO 2/2012.", "Estos planes deberán ser aprobados por dichos órganos en el plazo máximo de dos meses desde su presentación")
Q("LOEP", "Artículo 25", "Medidas", "Según el artículo 25.1 b) de la Ley Orgánica 2/2012, el depósito con intereses en el Banco de España será equivalente:",
  ["Al 0,2 % de su Producto Interior Bruto nominal.", "Al 0,4 % de su Producto Interior Bruto nominal.", "Al 2 % de su presupuesto de gastos.", "Al importe del déficit no corregido."],
  "Art. 25.1 b) LO 2/2012.", "equivalente al 0,2 % de su Producto Interior Bruto nominal")
Q("LOEP", "Artículo 26", "Medidas", "Según el artículo 26.1 de la Ley Orgánica 2/2012, si no se atiende el requerimiento al Presidente de la Comunidad Autónoma, el Gobierno adoptará las medidas necesarias para obligarla a su ejecución forzosa:",
  ["Con la aprobación por mayoría absoluta del Senado.", "Con la aprobación por mayoría absoluta del Congreso.", "Previo dictamen del Consejo de Estado.", "Previo informe favorable del Consejo de Política Fiscal y Financiera."],
  "Art. 26.1 LO 2/2012 (art. 155 CE).", "con la aprobación por mayoría absoluta del Senado")
Q("LOEP", "Artículo 32", "Gestión", "Según el artículo 32.2 de la Ley Orgánica 2/2012, en el caso de la Seguridad Social el superávit se aplicará prioritariamente:",
  ["Al Fondo de Reserva.", "A reducir el endeudamiento neto.", "Al Fondo de Contingencia.", "A incrementar las pensiones."],
  "Art. 32.2 LO 2/2012.", "el superávit se aplicará prioritariamente al Fondo de Reserva")
Q("LOEP", "Artículo 29", "Gestión", "Según el artículo 29.2 de la Ley Orgánica 2/2012, el plan presupuestario a medio plazo abarcará un periodo mínimo de:",
  ["Tres años.", "Dos años.", "Cinco años.", "Cuatro años."],
  "Art. 29.2 LO 2/2012.", "abarcará un periodo mínimo de tres años")
Q("LO6_2013", "Artículo 2", "AIReF", "Según el artículo 2 de la Ley Orgánica 6/2013, la Autoridad Independiente de Responsabilidad Fiscal tiene por objeto garantizar el cumplimiento efectivo por las Administraciones Públicas del principio de:",
  ["Estabilidad presupuestaria previsto en el artículo 135 de la Constitución.", "Legalidad presupuestaria previsto en el artículo 134 de la Constitución.", "Eficacia previsto en el artículo 103 de la Constitución.", "Autonomía financiera previsto en el artículo 156 de la Constitución."],
  "Art. 2 LO 6/2013.", "del principio de estabilidad presupuestaria previsto en el artículo 135 de la Constitución Española")
T.real("L", 83, "Principios de la LO 2/2012"); T.real("P", 23, "Medidas"); T.real("P", 26, "Art. 135 CE"); T.real("P", 83, "Límites")
T.real("P", 84, "Ley General Presupuestaria"); T.real("X", 90, "Leyes de estabilidad"); T.real("X", 92, "Concepto"); T.real("L", 33, "AIReF")

# Flashcards
for q_, a_, cat in [
  ("Definición de Presupuestos Generales del Estado (art. 32 LGP)", "Expresión cifrada, conjunta y sistemática de los derechos y obligaciones a liquidar durante el ejercicio por cada órgano y entidad del sector público estatal.", "Concepto"),
  ("Notas del art. 134.2 CE", "Carácter anual; totalidad de los gastos e ingresos del sector público estatal; importe de los beneficios fiscales de los tributos del Estado.", "Concepto"),
  ("¿Cómo llama la exposición de motivos de la LGP a la inclusión de todos los ingresos y gastos?", "Principio de universalidad del presupuesto, consagrado en el art. 134 CE.", "Concepto"),
  ("Clases de presupuestos en los PGE (art. 33.1 LGP)", "Limitativos (órganos del 2.3 y entidades con régimen limitativo) y estimativos (empresariales, fundacionales, consorcios, universidades no transferidas, fondos sin personalidad y resto del sector administrativo).", "Clases"),
  ("Presupuestos de las sociedades mercantiles estatales y EPE (art. 64 LGP)", "Presupuesto de explotación y de capital (previsión de cuenta de resultados y de flujos de efectivo), integrados en los PGE.", "Clases"),
  ("Ejercicio presupuestario (art. 34 LGP)", "Año natural: derechos liquidados en él (cualquiera que sea su período) y obligaciones reconocidas hasta fin de diciembre por gastos del ejercicio.", "Ámbito temporal"),
  ("¿A quién no se aplica la LGP? (art. 2.3)", "A las Cortes Generales, que gozan de autonomía presupuestaria (art. 72 CE).", "Ley General Presupuestaria"),
  ("Los tres sectores del art. 3 LGP", "Administrativo, empresarial y fundacional.", "Ley General Presupuestaria"),
  ("Títulos de la LGP", "I ámbito y Hacienda Pública estatal; II PGE; III relaciones financieras con otras administraciones; IV Tesoro, Deuda y operaciones financieras; V contabilidad; VI control de la IGAE; VII responsabilidades.", "Ley General Presupuestaria"),
  ("Principios de programación presupuestaria (art. 26 LGP)", "Estabilidad presupuestaria, sostenibilidad financiera, plurianualidad, transparencia, eficiencia, responsabilidad y lealtad institucional.", "Principios de la LGP"),
  ("Reglas de gestión del art. 27 LGP", "Presupuesto anual de las Cortes en escenario plurianual; créditos exclusivamente a su finalidad; recursos al conjunto de obligaciones salvo afectación por ley; importe íntegro.", "Principios de la LGP"),
  ("Escenarios presupuestarios plurianuales (art. 28 LGP)", "Los confecciona el Ministerio de Hacienda; límites para los tres ejercicios siguientes; ajustados al objetivo de estabilidad.", "Principios de la LGP"),
  ("Leyes de estabilidad presupuestaria", "Ley 18/2001 y LO 5/2001; texto refundido (RDLeg 2/2007); vigente: LO 2/2012, que deroga la LO 5/2001 y el texto refundido.", "Leyes de estabilidad"),
  ("Subsectores del sector Administraciones Públicas (art. 2 LO 2/2012)", "Administración central (Estado y organismos), Comunidades Autónomas, Corporaciones Locales y Administraciones de Seguridad Social.", "Leyes de estabilidad"),
  ("Estabilidad presupuestaria (art. 3.2 LO 2/2012)", "Situación de equilibrio o superávit estructural.", "Principios de la LO 2/2012"),
  ("Sostenibilidad financiera (art. 4.2 LO 2/2012)", "Capacidad para financiar compromisos de gasto presentes y futuros dentro de los límites de déficit, deuda pública y morosidad de deuda comercial.", "Principios de la LO 2/2012"),
  ("Déficit estructural permitido por reformas estructurales (art. 11.2)", "0,4 % del PIB nacional nominal para el conjunto de Administraciones.", "Límites"),
  ("Reparto del límite de deuda (art. 13.1)", "60 % del PIB: 44 % Administración central, 13 % CC. AA., 3 % Corporaciones Locales; cada CC. AA., 13 % de su PIB regional.", "Límites"),
  ("¿Quién aprecia las excepciones a los límites de déficit y deuda?", "La mayoría absoluta de los miembros del Congreso de los Diputados (art. 135.4 CE; art. 11.3 LO 2/2012).", "Límites"),
  ("Medidas coercitivas del art. 25", "No disponibilidad en 15 días; depósito del 0,2 % del PIB en el Banco de España (3 meses: sin intereses; otros 3: multa coercitiva); comisión de expertos.", "Medidas"),
  ("Cumplimiento forzoso de una CC. AA. (art. 26)", "Gobierno, por el art. 155 CE, con aprobación por mayoría absoluta del Senado.", "Medidas"),
  ("Destino del superávit (art. 32)", "Estado, CC. AA. y CC. LL.: reducir endeudamiento neto; Seguridad Social: Fondo de Reserva.", "Gestión"),
  ("Informe de la AIReF antes del 15 de julio (art. 17 LO 6/2013)", "Cumplimiento de los objetivos de estabilidad y deuda del ejercicio en curso y de la regla de gasto de todas las Administraciones.", "AIReF"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Presupuestos Generales del Estado", "Expresión cifrada, conjunta y sistemática de los derechos y obligaciones a liquidar durante el ejercicio por el sector público estatal (art. 32 LGP).", "s1", "Concepto")
T.glos("Principio de universalidad", "Nombre que da la exposición de motivos de la LGP a la exigencia del art. 134 CE de incluir la totalidad de los gastos e ingresos del sector público estatal.", "s1", "Concepto")
T.glos("Presupuesto limitativo", "El que fija las obligaciones que, como máximo, pueden reconocer los sujetos del art. 33.1 a) LGP.", "s2", "Clases")
T.glos("Presupuesto estimativo", "El de las entidades empresariales y fundacionales, consorcios, universidades no transferidas, fondos sin personalidad y resto del sector administrativo (art. 33.1 b) LGP).", "s2", "Clases")
T.glos("Crédito presupuestario", "Cada una de las asignaciones individualizadas de gasto puestas a disposición de los centros gestores (art. 35.1 LGP).", "s3", "Créditos y programas")
T.glos("Sector público estatal", "Administración General del Estado, sector público institucional estatal y órganos con dotación diferenciada (art. 2 LGP).", "s4", "Ley General Presupuestaria")
T.glos("Escenarios presupuestarios plurianuales", "Programación del sector público estatal con presupuesto limitativo que fija límites para los tres ejercicios siguientes; los confecciona el Ministerio de Hacienda (art. 28 LGP).", "s9", "Principios de la LGP")
T.glos("Estabilidad presupuestaria", "Situación de equilibrio o superávit estructural de las Administraciones Públicas (art. 3.2 LO 2/2012).", "s13", "Principios de la LO 2/2012")
T.glos("Sostenibilidad financiera", "Capacidad para financiar compromisos de gasto presentes y futuros dentro de los límites de déficit, deuda pública y morosidad de deuda comercial (art. 4.2 LO 2/2012).", "s13", "Principios de la LO 2/2012")
T.glos("Déficit estructural", "Déficit ajustado del ciclo, neto de medidas excepcionales y temporales (art. 11.2 LO 2/2012).", "s16", "Límites")
T.glos("Regla de gasto", "La variación del gasto computable no puede superar la tasa de referencia de crecimiento del PIB de medio plazo (art. 12 LO 2/2012).", "s16", "Límites")
T.glos("Plan económico-financiero", "Plan que formula la Administración que incumple el objetivo de estabilidad, de deuda o la regla de gasto, para cumplir en el año en curso y el siguiente (art. 21 LO 2/2012).", "s18", "Medidas")
T.glos("Límite de gasto no financiero", "Techo de asignación de recursos de los presupuestos del Estado, CC. AA. y Corporaciones Locales (art. 30 LO 2/2012).", "s19", "Gestión")
T.glos("Autoridad Independiente de Responsabilidad Fiscal", "Ente de Derecho Público con personalidad jurídica propia que garantiza el cumplimiento del principio de estabilidad presupuestaria del art. 135 CE (LO 6/2013, arts. 1 y 2).", "s19", "AIReF")

# Cronología (fechas de los metadatos del BOE)
T.hito("1978", "Constitución Española (27-12-1978; BOE de 29-12-1978)", "Art. 134.2: presupuestos anuales que incluyen la totalidad de gastos e ingresos del sector público estatal", "normativo", "s1")
T.hito("2003", "Ley 47/2003, de 26 de noviembre, General Presupuestaria (BOE de 27-11-2003; en vigor el 1-1-2005)", "Concepto, clases y principios del presupuesto del sector público estatal", "normativo", "s4")
T.hito("2011", "Reforma del artículo 135 de la Constitución (27-9-2011; BOE de 27-9-2011)", "Estabilidad presupuestaria con rango constitucional", "normativo", "s10")
T.hito("2012", "Ley Orgánica 2/2012, de 27 de abril, de Estabilidad Presupuestaria y Sostenibilidad Financiera (BOE de 30-4-2012; en vigor el 1-5-2012)", "Desarrolla el art. 135 CE; deroga la LO 5/2001 y el texto refundido de 2007", "normativo", "s12")
T.hito("2013", "Ley Orgánica 6/2013, de 14 de noviembre, de creación de la Autoridad Independiente de Responsabilidad Fiscal (BOE de 15-11-2013)", "Crea la AIReF", "normativo", "s19")

T.publicar()
