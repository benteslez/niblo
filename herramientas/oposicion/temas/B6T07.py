# -*- coding: utf-8 -*-
"""Tema VI.7 (B6T07): Los ingresos públicos: concepto y clasificación. El sistema
tributario español: régimen actual. Especial referencia al régimen de tasas y precios públicos.
Método del I.2. Normas (textos consolidados del BOE): Ley 47/2003, General Presupuestaria
(arts. 5, 10, 19, 27 y 41); CE, arts. 31, 133 y 134.7; Ley 58/2003, General Tributaria
(arts. 1 a 4, 7, 8, 10, 20 a 22 y 36 y disposición adicional primera); Ley 8/1989, de Tasas
y Precios Públicos."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO["L8_1989"] = "Ley 8/1989"

T = Tema("B6T07",
  "Cuatro preguntas: I. Qué son los ingresos públicos y cómo se clasifican (LGP, arts. 5, 10, 19, 27 y 41; CE, art. 31.3; LGT, disposición adicional primera) · II. Cómo es el sistema tributario español (CE, arts. 31.1, 133 y 134.7; LGT, arts. 1 a 4, 7, 8, 10, 20 a 22 y 36) · III. Qué son las tasas y cómo se regulan (Ley 8/1989, arts. 1, 2 y 6 a 23) · IV. Qué son los precios públicos y en qué se diferencian de las tasas (Ley 8/1989, arts. 24 a 27). Cada artículo: texto literal del BOE y ficha.",
  ["Ingresos públicos", "Hacienda Pública estatal", "Derechos de naturaleza pública", "Clasificación económica", "Prestaciones patrimoniales", "Tributo", "Tasas", "Contribuciones especiales", "Impuestos", "Potestad tributaria", "Reserva de ley tributaria", "Hecho imponible", "Devengo", "Exención", "Ley 8/1989", "Precios públicos", "Memoria económico-financiera"])

# =============================================================================
T.ap("s0", "Mapa del tema: cuatro preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque VI, tema 7):
> Los ingresos públicos: concepto y clasificación. El sistema tributario español: régimen actual. Especial referencia al régimen de tasas y precios públicos.

### El hilo conductor

El epígrafe se lee como **cuatro preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Normas |
|---|---|---|
| **I** | ¿Qué son los ingresos públicos y cómo se clasifican? | Ley 47/2003, General Presupuestaria (LGP), arts. 5, 10.1, 19.1, 27.3 y 4 y 41; CE, art. 31.3; Ley 58/2003, General Tributaria (LGT), disposición adicional primera |
| **II** | ¿Cómo es el sistema tributario español? (régimen actual) | CE, arts. 31.1, 133 y 134.7; LGT, arts. 1, 2, 3, 4, 7, 8, 10, 20, 21, 22 y 36 |
| **III** | ¿Qué son las tasas y cómo se regulan? | LGT, art. 2.2 a); Ley 8/1989, de Tasas y Precios Públicos, arts. 1, 2 y 6 a 23 |
| **IV** | ¿Qué son los precios públicos y en qué se diferencian de las tasas? | Ley 8/1989, arts. 24 a 27 y disposición adicional séptima |

!> **La idea que une los cuatro bloques:** la Hacienda Pública estatal tiene derechos de **naturaleza pública** (los tributos y los que derivan de **potestades administrativas**) y de **naturaleza privada** (I). Los **tributos** son el ingreso público típico: los crea la **ley**, se clasifican en **tasas, contribuciones especiales e impuestos** y se rigen por la **LGT** (II). Las **tasas** son tributos (III); los **precios públicos** no lo son: son **contraprestaciones** por servicios que también presta el **sector privado** y que se solicitan **voluntariamente** (IV).

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- No se incluyen cifras de recaudación ni la lista de impuestos concretos del sistema: no están en las normas de este tema.
- Fuera de este tema: los principios presupuestarios y la estructura de los Presupuestos (temas VI.1 y VI.2) y los gastos (temas VI.3 a VI.6).
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué son los ingresos públicos y cómo se clasifican?", donde(
  "Primera pregunta del tema. Antes de hablar de tributos, hay que saber **de quién** son los ingresos (la Hacienda Pública estatal), **qué clases de derechos** la integran y **cómo se ordenan** en el presupuesto.",
  ["1 La Hacienda Pública estatal y sus derechos (LGP, arts. 5, 10 y 19)", "2 Los ingresos en el presupuesto: no afectación y clasificación (LGP, arts. 27 y 41)", "3 Las prestaciones patrimoniales de carácter público (CE, art. 31.3; LGT, disposición adicional primera)"]))

T.ap("s1", "I.1 La Hacienda Pública estatal y sus derechos (LGP, arts. 5, 10.1 y 19.1)", f"""
La LGP no define «ingreso público» en un artículo: parte de los **derechos de contenido económico** de la Hacienda Pública estatal y los divide en **públicos** y **privados**.

{unidad("1.1 Concepto y clases de derechos (LGP, art. 5)",
  lit("LGP", "Artículo 5", ["conjunto de derechos y obligaciones de contenido económico", "derechos de naturaleza pública y de naturaleza privada", "que deriven del ejercicio de potestades administrativas"]),
  fichab("La Hacienda Pública estatal y la clasificación de sus derechos",
         f"Titular: {c('LGP', 'Artículo 5', 'la Administración General del Estado y a sus organismos autónomos')}",
         ["::Dos clases de derechos (5.2):", f"De naturaleza pública: {c('LGP', 'Artículo 5', 'los tributos y los demás derechos de contenido económico')} que deriven del ejercicio de potestades administrativas", "De naturaleza privada: los demás (→ I.1.3)"],
         "—",
         "La Hacienda Pública estatal es la de la **AGE y sus organismos autónomos** (no todo el sector público estatal). Lo que hace **pública** a un derecho es que derive de **potestades administrativas**; los tributos se citan expresamente."))}

{unidad("1.2 Prerrogativas de los derechos de naturaleza pública (LGP, art. 10.1)",
  lit("LGP", "Artículo 10", ["gozará de las prerrogativas establecidas para los tributos en la Ley General Tributaria"], solo=[1]),
  fichab("Régimen de cobro de los derechos de naturaleza pública",
         "La Hacienda Pública estatal",
         f"Cobranza {c('LGP', 'Artículo 10', 'conforme a los procedimientos administrativos correspondientes')}",
         "—",
         "Todos los derechos de naturaleza pública (no solo los tributos) gozan de las **prerrogativas de los tributos** de la LGT y del Reglamento General de Recaudación."))}

{unidad("1.3 Derechos de naturaleza privada (LGP, art. 19.1)",
  lit("LGP", "Artículo 19", ["con sujeción a las normas y procedimientos del derecho privado"], solo=[1]),
  fichab("Régimen de los derechos de naturaleza privada",
         "La Hacienda Pública estatal",
         "Su efectividad se rige por el **derecho privado**",
         "—",
         "Contraste con el 10.1: los **públicos** se cobran por procedimientos **administrativos** y con prerrogativas; los **privados**, por el **derecho privado**."))}
""", 2)

T.ap("s2", "I.2 Los ingresos en el presupuesto: no afectación y clasificación (LGP, arts. 27.3 y 4 y 41)", f"""
{unidad("2.1 Los recursos no se afectan y se aplican por su importe íntegro (LGP, art. 27.3 y 4)",
  lit("LGP", "Artículo 27", ["se destinarán a satisfacer el conjunto de sus respectivas obligaciones", "salvo que por ley se establezca su afectación a fines determinados", "por su importe íntegro"], solo=[4, 5]),
  fichab("Dos reglas de gestión de los ingresos: no afectación (27.3) y presupuesto bruto (27.4)",
         "El Estado, sus organismos autónomos y las entidades del sector público estatal con presupuesto limitativo",
         ["Los recursos financian el **conjunto** de las obligaciones", "Los derechos liquidados se aplican por su **importe íntegro**, sin minorarlos para atender obligaciones"],
         "—",
         "La afectación a un fin concreto solo cabe **por ley**. La minoración de derechos solo si **la ley lo autoriza de modo expreso**."))}

{unidad("2.2 Estructura de los estados de ingresos (LGP, art. 41)",
  lit("LGP", "Artículo 41", ["clasificaciones orgánica y económica", "separando los corrientes, los de capital, y las operaciones financieras", "impuestos directos y cotizaciones sociales, impuestos indirectos, tasas, precios públicos y otros ingresos, transferencias corrientes e ingresos patrimoniales", "enajenación de inversiones reales y transferencias de capital", "activos financieros y pasivos financieros"]),
  fichab("Cómo se clasifican los ingresos en los Presupuestos Generales del Estado",
         "Los estados de ingresos de los presupuestos del art. 33.1 a) LGP",
         ["::Dos clasificaciones:", "**Orgánica**: AGE, cada organismo autónomo, Seguridad Social y otras entidades", "**Económica**: corrientes, de capital y operaciones financieras"],
         "—",
         "Los **gastos** tienen tres clasificaciones (orgánica, por programas y económica: art. 40); los **ingresos**, solo **dos** (orgánica y económica). Las **tasas y precios públicos** son ingresos **corrientes**; los **activos y pasivos financieros**, operaciones **financieras**."))}

*Esquema de elaboración propia: resume el art. 41 LGP; no es texto legal.*

| Ingresos | Lo que se distingue (art. 41 b) |
|---|---|
| Corrientes | Impuestos directos y cotizaciones sociales · impuestos indirectos · tasas, precios públicos y otros ingresos · transferencias corrientes · ingresos patrimoniales |
| De capital | Enajenación de inversiones reales · transferencias de capital |
| Operaciones financieras | Activos financieros · pasivos financieros |
""", 2)

T.ap("s3", "I.3 Las prestaciones patrimoniales de carácter público (CE, art. 31.3; LGT, disposición adicional primera)", f"""
{unidad("3.1 Reserva de ley (CE, art. 31.3)",
  lit("CE", "Artículo 31", ["con arreglo a la ley"], solo=[3]),
  fichab("Reserva de ley de las prestaciones personales o patrimoniales de carácter público",
         "El legislador: solo «con arreglo a la ley»",
         "Solo pueden establecerse con arreglo a la ley",
         "—",
         "Es la base de la disposición adicional primera de la LGT (→ I.3.2): tributos y prestaciones **no tributarias** necesitan ley."))}

{unidad("3.2 Tributarias y no tributarias (LGT, disposición adicional primera)",
  lit("LGT", "daprimera", ["que se exigen con carácter coactivo", "podrán tener carácter tributario o no tributario", "tasas, contribuciones especiales e impuestos", "fines de interés general", "gestión indirecta"]),
  fichab("Clasificación de las prestaciones patrimoniales de carácter público",
         "—",
         ["**Tributarias**: tasas, contribuciones especiales e impuestos (art. 2 LGT → II.3.1)", "**No tributarias**: las demás exigidas coactivamente para fines de interés general; en particular, las de servicios gestionados mediante **personificación privada** o **gestión indirecta** (concesión, sociedades de economía mixta, entidades públicas empresariales, sociedades de capital íntegramente público…)"],
         "—",
         f"Lo que define la prestación patrimonial de carácter público es la **coactividad**: {c('LGT', 'daprimera', 'que se exigen con carácter coactivo')}. Las tarifas de los concesionarios son prestaciones **no tributarias** (también lo dice el art. 2 de la Ley 8/1989 → III.1.1)."))}

*Esquema de elaboración propia: resume los artículos citados en este bloque; no es texto legal.*

| Criterio | Clases | Artículo |
|---|---|---|
| Naturaleza del derecho | De naturaleza **pública** (tributos y derechos derivados de potestades administrativas) · de naturaleza **privada** | LGP, art. 5.2 |
| Clasificación económica del presupuesto | Corrientes · de capital · operaciones financieras | LGP, art. 41 b) |
| Prestaciones patrimoniales coactivas | Tributarias (tasas, contribuciones especiales, impuestos) · no tributarias | LGT, disp. adic. 1.ª |

{resumen([
  "Hacienda Pública estatal = derechos y obligaciones de contenido económico de la **AGE y sus organismos autónomos**; sus derechos son de naturaleza **pública** o **privada** (LGP 5).",
  "Los públicos se cobran por procedimientos **administrativos** con las **prerrogativas de los tributos** (10.1); los privados, por **derecho privado** (19.1).",
  "Los recursos financian el **conjunto** de obligaciones salvo afectación **por ley**; se aplican por su **importe íntegro** (27.3 y 4).",
  "Estados de ingresos: clasificación **orgánica** y **económica** (corrientes, de capital, financieros) (41).",
  "Prestaciones patrimoniales de carácter público: **coactivas**; **tributarias** o **no tributarias** (LGT, disp. adic. 1.ª)."],
  "Siguiente: II. ¿Cómo es el sistema tributario español?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Cómo es el sistema tributario español? (régimen actual)", donde(
  "Segunda pregunta. El ingreso público típico es el **tributo**. La Constitución fija los principios y quién puede crearlos; la **Ley General Tributaria** da el concepto, las clases, las fuentes, la reserva de ley y los elementos de la obligación tributaria.",
  ["1 Las bases constitucionales (CE, arts. 31.1, 133 y 134.7)", "2 La LGT: objeto, concepto de tributo y principios (arts. 1 a 3)", "3 Las clases de tributos (art. 2.2)", "4 Potestad tributaria, fuentes, reserva de ley y vigencia (arts. 4, 7, 8 y 10)", "5 Elementos de la obligación tributaria (arts. 20 a 22 y 36)"]))

T.ap("s4", "II.1 Las bases constitucionales del sistema tributario (CE, arts. 31.1, 133 y 134.7)", f"""
{unidad("1.1 El deber de contribuir y los principios (art. 31.1)",
  lit("CE", "Artículo 31", ["de acuerdo con su capacidad económica", "igualdad y progresividad", "en ningún caso, tendrá alcance confiscatorio"], solo=[1]),
  fichab("Deber de contribuir y principios del sistema tributario",
         c("CE", "Artículo 31", "Todos"),
         ["Según su **capacidad económica**", "Sistema tributario **justo**", "Principios de **igualdad** y **progresividad**", "**Nunca** alcance confiscatorio"],
         "—",
         "La Constitución dice «igualdad y progresividad»; la LGT (art. 3.1 → II.2.3) amplía la lista. «En ningún caso» confiscatorio: es un límite absoluto."))}

{unidad("1.2 La potestad tributaria (art. 133)",
  lit("CE", "Artículo 133", ["corresponde exclusivamente al Estado, mediante ley", "de acuerdo con la Constitución y las leyes", "deberá establecerse en virtud de ley"]),
  fichab("Quién puede establecer tributos y beneficios fiscales",
         ["Potestad **originaria**: el Estado (133.1)", "Comunidades Autónomas y Corporaciones locales: de acuerdo con la Constitución y las leyes (133.2)"],
         ["Tributos: mediante ley", "Beneficios fiscales sobre tributos del Estado: en virtud de ley (133.3)"],
         "—",
         "Originaria = **exclusivamente el Estado**. La LGT repite la regla y la extiende a las **demás entidades de derecho público** (art. 4 → II.4.1)."))}

{unidad("1.3 La Ley de Presupuestos y los tributos (art. 134.7)",
  lit("CE", "Artículo 134", ["no puede crear tributos", "cuando una ley tributaria sustantiva así lo prevea"], solo=[7]),
  fichab("Límite material de la Ley de Presupuestos en materia tributaria",
         "Las Cortes, al aprobar la Ley de Presupuestos",
         ["No puede **crear** tributos", "Puede **modificarlos** si una **ley tributaria sustantiva** lo prevé"],
         "—",
         "Crear: **nunca**. Modificar: solo con previsión de una ley tributaria **sustantiva**. Por eso la Ley 8/1989 permite que las Leyes de Presupuestos modifiquen la cuantía de las tasas (art. 19.5 → III.4.1)."))}
""", 2)

T.ap("s5", "II.2 La Ley General Tributaria: objeto, concepto de tributo y principios (LGT, arts. 1 a 3)", f"""
{unidad("2.1 Objeto y ámbito de la LGT (art. 1.1)",
  lit("LGT", "Artículo 1", ["los principios y las normas jurídicas generales del sistema tributario español", "a todas las Administraciones tributarias"], solo=[1, 2]),
  fichab("La LGT como ley general del sistema tributario",
         "Se aplica a **todas** las Administraciones tributarias",
         "Con el alcance del art. 149.1.1.ª, 8.ª, 14.ª y 18.ª CE; sin perjuicio del Convenio (Navarra) y del Concierto Económico (País Vasco)",
         "—",
         "La LGT no se aplica solo al Estado: es de aplicación a **todas** las Administraciones tributarias."))}

{unidad("2.2 Concepto y fines del tributo (art. 2.1)",
  lit("LGT", "Artículo 2", ["ingresos públicos que consisten en prestaciones pecuniarias exigidas por una Administración pública", "con el fin primordial de obtener los ingresos necesarios para el sostenimiento de los gastos públicos", "instrumentos de la política económica general"], solo=[1, 2]),
  fichab("Qué es un tributo",
         f"Lo exige {c('LGT', 'Artículo 2', 'una Administración pública')}",
         ["::Rasgos (2.1):", "Ingreso público", "Prestación **pecuniaria**", "Exigida por realizar el supuesto de hecho al que **la ley** vincula el deber de contribuir"],
         "—",
         "Fin **primordial**: financiar el gasto público; además **pueden** servir como instrumento de **política económica** y para los fines de la Constitución (fines extrafiscales)."))}

{unidad("2.3 Principios de ordenación y de aplicación (art. 3)",
  lit("LGT", "Artículo 3", ["justicia, generalidad, igualdad, progresividad, equitativa distribución de la carga tributaria y no confiscatoriedad", "cualquier instrumento extraordinario de regularización fiscal", "proporcionalidad, eficacia y limitación de costes indirectos"]),
  fichab("Principios del sistema tributario",
         "El legislador (ordenación) y la Administración tributaria (aplicación)",
         ["**Ordenación** (3.1): capacidad económica; justicia, generalidad, igualdad, progresividad, equitativa distribución de la carga tributaria y no confiscatoriedad", "Prohibición de **instrumentos extraordinarios de regularización fiscal** que minoren la deuda devengada", "**Aplicación** (3.2): proporcionalidad, eficacia y limitación de costes indirectos; respeto de los derechos y garantías de los obligados"],
         "—",
         "No confundir las dos listas: **ordenación** (justicia, generalidad, igualdad, progresividad…) y **aplicación** (proporcionalidad, eficacia, limitación de costes indirectos)."))}
""", 2)

T.ap("s6", "II.3 Las clases de tributos: tasas, contribuciones especiales e impuestos (LGT, art. 2.2)", f"""
{unidad("3.1 Tres clases de tributos (art. 2.2)",
  lit("LGT", "Artículo 2", ["cualquiera que sea su denominación", "Tasas", "Contribuciones especiales", "Impuestos", "utilización privativa o el aprovechamiento especial del dominio público", "beneficio o de un aumento de valor de sus bienes", "sin contraprestación"], solo=[3, 4, 5, 6]),
  fichab("Clasificación legal de los tributos",
         "—",
         ["**Tasas**: utilización privativa o aprovechamiento especial del dominio público, o servicios o actividades en régimen de derecho público que afecten o beneficien de modo particular al obligado, no voluntarios o no prestados por el sector privado (→ III.1.2)", "**Contribuciones especiales**: beneficio o aumento de valor de los bienes del obligado por obras públicas o por el establecimiento o ampliación de servicios públicos", "**Impuestos**: sin contraprestación; hecho imponible que pone de manifiesto la capacidad económica del contribuyente"],
         "—",
         "Tres clases, **cualquiera que sea su denominación**: lo que cuenta es el hecho imponible, no el nombre. Los **precios públicos no son tributos** (→ IV.1). Cayó en 2025 en dos exámenes (→ Cierre 1)."))}

*Esquema de elaboración propia: resume el art. 2.2 LGT; no es texto legal.*

| Tributo | Clave del hecho imponible | Palabra que lo delata |
|---|---|---|
| Tasa | Dominio público o servicio/actividad pública que beneficia **de modo particular** | «utilización privativa», «aprovechamiento especial», «no sean de solicitud o recepción voluntaria» |
| Contribución especial | **Beneficio** o **aumento de valor** de los bienes por obras o servicios públicos | «obras públicas», «aumento de valor» |
| Impuesto | Negocios, actos o hechos que muestran **capacidad económica** | «sin contraprestación» |
""", 2)

T.ap("s7", "II.4 Potestad tributaria, fuentes, reserva de ley y vigencia (LGT, arts. 4, 7, 8 y 10)", f"""
{unidad("4.1 Potestad tributaria (art. 4)",
  lit("LGT", "Artículo 4", ["corresponde exclusivamente al Estado, mediante ley", "de acuerdo con la Constitución y las leyes", "cuando una ley así lo determine"]),
  fichab("Quién puede establecer o exigir tributos",
         ["Estado: potestad **originaria**, mediante ley", "Comunidades autónomas y entidades locales: establecer y exigir, de acuerdo con la Constitución y las leyes", "Demás entidades de derecho público: **exigir**, cuando una ley lo determine"],
         "—", "—",
         "Las demás entidades de derecho público solo pueden **exigir** tributos (no establecerlos) y solo **cuando una ley** lo determine."))}

{unidad("4.2 Fuentes del ordenamiento tributario (art. 7)",
  lit("LGT", "Artículo 7", ["Por la Constitución", "ordenanzas fiscales", "revestirán la forma de orden ministerial", "Tendrán carácter supletorio"]),
  fichab("Orden de las fuentes de los tributos",
         "El Ministro de Hacienda, para las disposiciones de desarrollo en el ámbito estatal (orden ministerial)",
         ["Constitución", "Tratados o convenios internacionales (en particular, para evitar la doble imposición)", "Normas de la Unión Europea y de organismos del art. 93 CE", "LGT, leyes de cada tributo y demás leyes tributarias", "Reglamentos de desarrollo y, en el ámbito local, **ordenanzas fiscales**", "Supletorias: derecho administrativo general y derecho común (7.2)"],
         "—",
         "La orden ministerial solo cabe **cuando lo disponga expresamente** la ley o el reglamento que desarrolla. Las **ordenanzas fiscales** son del ámbito **local**."))}

{unidad("4.3 Reserva de ley tributaria (art. 8)",
  lit("LGT", "Artículo 8", ["Se regularán en todo caso por ley", "la fijación del tipo de gravamen", "El establecimiento, modificación, supresión y prórroga de las exenciones", "El establecimiento y modificación de las infracciones y sanciones tributarias", "La condonación de deudas y sanciones tributarias"]),
  fichab("Materias que solo puede regular una ley",
         "El legislador: «en todo caso por ley»",
         ["Hecho imponible, devengo, base, tipo y demás elementos de la cuantía (a)", "Pagos a cuenta (b); obligados del art. 35.2 y responsables (c)", "Beneficios fiscales (d); recargos e intereses de demora (e); prescripción y caducidad (f)", "Infracciones y sanciones (g); declaraciones y autoliquidaciones (h)", "Condonación, moratorias y quitas (k); actos reclamables en vía económico-administrativa (l)"],
         "—",
         "«Se regularán **en todo caso** por ley»: son trece letras (a a m). La **condonación** de deudas y sanciones también exige ley."))}

{unidad("4.4 Entrada en vigor y retroactividad (art. 10)",
  lit("LGT", "Artículo 10", ["a los veinte días naturales de su completa publicación", "no tendrán efecto retroactivo", "cuando su aplicación resulte más favorable para el interesado"]),
  fichab("Ámbito temporal de las normas tributarias",
         "—",
         ["Vigencia por **plazo indefinido**, salvo que se fije uno determinado", "**Sin efecto retroactivo**, salvo que se disponga lo contrario", "Infracciones, sanciones y recargos: retroactivas respecto de actos **no firmes** si son más favorables"],
         f"Entrada en vigor: {c('LGT', 'Artículo 10', 'a los veinte días naturales de su completa publicación')}, si la norma no dice otra cosa",
         "**Veinte días naturales** (no hábiles) desde la **completa** publicación; es la regla supletoria."))}
""", 2)

T.ap("s8", "II.5 Elementos de la obligación tributaria (LGT, arts. 20 a 22 y 36)", f"""
{unidad("5.1 Hecho imponible (art. 20)",
  lit("LGT", "Artículo 20", ["el presupuesto fijado por la ley para configurar cada tributo", "supuestos de no sujeción"]),
  fichab("El presupuesto que hace nacer la obligación tributaria principal",
         "Lo fija **la ley** (art. 8 a → II.4.3)",
         "Su realización origina el nacimiento de la obligación tributaria principal (pagar la cuota: art. 19)",
         "—",
         "Definición literal preguntada en 2025 (→ Cierre 1). La ley puede completar el hecho imponible con **supuestos de no sujeción**."))}

{unidad("5.2 Devengo y exigibilidad (art. 21)",
  lit("LGT", "Artículo 21", ["el momento en el que se entiende realizado el hecho imponible", "en un momento distinto al del devengo del tributo"]),
  fichab("Cuándo nace la obligación y cuándo se puede exigir",
         "—",
         ["**Devengo**: momento en que se entiende realizado el hecho imponible y nace la obligación principal; su fecha determina las circunstancias relevantes", "**Exigibilidad**: la ley de cada tributo puede situarla en un momento distinto del devengo"],
         "—",
         "Hecho imponible = **el qué** (presupuesto); devengo = **el cuándo** (momento)."))}

{unidad("5.3 Exenciones (art. 22)",
  lit("LGT", "Artículo 22", ["a pesar de realizarse el hecho imponible"]),
  fichab("Supuestos de exención",
         "La ley (art. 8 d → II.4.3)",
         "Se realiza el hecho imponible, pero la ley exime de la obligación tributaria principal",
         "—",
         "**Exención**: hay hecho imponible y la ley exime. **No sujeción**: no hay hecho imponible (art. 20.2)."))}

{unidad("5.4 Sujeto pasivo, contribuyente y sustituto (art. 36)",
  lit("LGT", "Artículo 36", ["Es sujeto pasivo el obligado tributario que, según la ley, debe cumplir la obligación tributaria principal", "Es contribuyente el sujeto pasivo que realiza el hecho imponible", "en lugar del contribuyente"], solo=[1, 3, 4, 5]),
  fichab("Quién debe pagar el tributo",
         ["**Sujeto pasivo**: quien debe cumplir la obligación principal y las formales inherentes", "**Contribuyente**: el sujeto pasivo que **realiza el hecho imponible**", "**Sustituto**: el sujeto pasivo que, por imposición de la ley, está obligado **en lugar del contribuyente**"],
         "El sustituto puede exigir al contribuyente lo pagado, salvo que la ley señale otra cosa",
         "—",
         "El contribuyente **realiza** el hecho imponible; el sustituto **no** lo realiza, pero paga en su lugar."))}

{resumen([
  "CE: todos contribuyen según su **capacidad económica**, con un sistema **justo**, de **igualdad y progresividad**, nunca **confiscatorio** (31.1); potestad **originaria** del **Estado** mediante ley (133.1); la Ley de Presupuestos **no puede crear** tributos (134.7).",
  "Tributo: ingreso público, **prestación pecuniaria** exigida por una Administración pública, para sostener el gasto público (LGT 2.1).",
  "Tres clases: **tasas, contribuciones especiales e impuestos**, cualquiera que sea su denominación (2.2).",
  "Fuentes (7), reserva de ley (8) y vigencia a los **veinte días naturales** sin retroactividad salvo previsión (10).",
  "Hecho imponible (20), devengo (21), exención (22), contribuyente y sustituto (36)."],
  "Siguiente: III. ¿Qué son las tasas y cómo se regulan?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Qué son las tasas y cómo se regulan? (Ley 8/1989)", donde(
  "Tercera pregunta: la «especial referencia» del epígrafe. La **Ley 8/1989, de Tasas y Precios Públicos**, regula estos dos recursos en el ámbito estatal y se aplica supletoriamente a Comunidades Autónomas y Haciendas Locales. Las tasas son **tributos**: les aplica también la LGT.",
  ["1 Objeto de la ley, concepto y principios de las tasas (arts. 1, 2, 6, 7 y 8)", "2 Fuentes, establecimiento por ley, previsión presupuestaria y devolución (arts. 9 a 12)", "3 Elementos de la tasa: hecho imponible, devengo, sujetos y beneficios (arts. 13 a 18)", "4 Cuantía, memoria económico-financiera, pago y gestión (arts. 19 a 23)"]))

T.ap("s9", "III.1 Objeto de la ley, concepto y principios de las tasas (Ley 8/1989, arts. 1, 2, 6, 7 y 8)", f"""
{unidad("1.1 Objeto y exclusiones (arts. 1 y 2)",
  lit("L8_1989", "Artículo 1", ["Tasas", "Precios públicos"]),
  lit("L8_1989", "Artículo 2", ["Las cotizaciones al sistema de la Seguridad Social", "que son prestaciones patrimoniales de carácter público no tributarias"]),
  fichab("Qué recursos regula la Ley 8/1989 y cuáles quedan fuera",
         "—",
         ["::Regula dos recursos de Derecho público: tasas y precios públicos (art. 1). No se aplica a:", "Cotizaciones a la Seguridad Social y las de naturaleza idéntica recaudadas con ellas", "Contraprestaciones de entes públicos que actúan según normas de derecho privado", "Recursos de las Cámaras de Comercio, Industria y Navegación", "Tarifas de los usuarios a concesionarios de obras y servicios (prestaciones patrimoniales de carácter público no tributarias → I.3.2)"],
         "—",
         "El BOE marca con **[Sic]** la segunda letra c) del art. 2: el texto tiene dos letras c). Las **cotizaciones sociales** no son tasas."))}

{unidad("1.2 Concepto de tasa (art. 6)",
  lit("L8_1989", "Artículo 6", ["Tasas son los tributos", "no sean de solicitud o recepción voluntaria", "no se presten o realicen por el sector privado"]),
  fichab("La tasa como tributo",
         "La exige la Administración; la paga el obligado tributario al que se refiere, afecta o beneficia de modo particular",
         ["::Hecho imponible:", "Utilización privativa o aprovechamiento especial del **dominio público**", "Prestación de **servicios** o realización de **actividades** en régimen de derecho público que se refieran, afecten o beneficien de modo particular al obligado, cuando **no sean de solicitud o recepción voluntaria** o **no se presten por el sector privado**"],
         "—",
         "Es la **misma definición** que el art. 2.2 a) LGT (→ II.3.1). Basta **una** de las dos condiciones: no voluntaria **o** no prestada por el sector privado."))}

{unidad("1.3 Principios de equivalencia y de capacidad económica (arts. 7 y 8)",
  lit("L8_1989", "Artículo 7", ["tenderán a cubrir el coste del servicio o de la actividad"]),
  lit("L8_1989", "Artículo 8", ["cuando lo permitan las características del tributo"]),
  fichab("Criterios para fijar el importe de las tasas",
         "—",
         ["**Equivalencia** (7): tienden a cubrir el coste del servicio o actividad", "**Capacidad económica** (8): se tiene en cuenta cuando lo permitan las características del tributo"],
         "—",
         "Las tasas «**tenderán** a cubrir» el coste (no «que cubra, como mínimo, los costes», que es lo de los **precios públicos**, art. 25.1 → IV.1.2)."))}
""", 2)

T.ap("s10", "III.2 Fuentes, establecimiento por ley, previsión presupuestaria y devolución (Ley 8/1989, arts. 9 a 12)", f"""
{unidad("2.1 Fuentes normativas de las tasas (art. 9)",
  lit("L8_1989", "Artículo 9", ["Por los Tratados o Convenios Internacionales", "por la Ley General Tributaria y la Ley General Presupuestaria", "se aplicará supletoriamente"]),
  fichab("Orden de las normas que rigen las tasas",
         "—",
         ["Tratados o Convenios Internacionales publicados", "Ley 8/1989, LGT y LGP, en cuanto no preceptúen lo contrario", "En su caso, la Ley propia de cada tasa", "Normas reglamentarias de desarrollo"],
         "—",
         "La Ley 8/1989 es **supletoria** para las tasas de las **Comunidades Autónomas** y las **Haciendas Locales** (9.2)."))}

{unidad("2.2 Establecimiento y regulación: con arreglo a Ley (art. 10)",
  lit("L8_1989", "Artículo 10", ["deberá realizarse con arreglo a Ley", "se podrán concretar mediante norma reglamentaria las cuantías exigibles"]),
  fichab("Cómo se crea una tasa",
         "La ley; la norma reglamentaria, solo para concretar cuantías si la ley lo autoriza",
         ["Establecimiento y elementos esenciales: **con arreglo a Ley**", "Elementos esenciales: los del capítulo II (arts. 13 a 20 → III.3 y III.4)", "Cuantías: por norma reglamentaria, **cuando se autorice por Ley** y con subordinación a sus criterios"],
         "—",
         "Pregunta de 2025 (→ Cierre 1): las tasas se establecen **por Ley** (no por Real Decreto, ni por ley orgánica, ni por Orden: la Orden es para los **precios públicos**, art. 26 → IV.2.1)."))}

{unidad("2.3 Previsión presupuestaria y devolución (arts. 11 y 12)",
  lit("L8_1989", "Artículo 11", ["ha de estar prevista en los Presupuestos"]),
  lit("L8_1989", "Artículo 12", ["por causas no imputables al sujeto pasivo"]),
  fichab("Dos reglas generales de las tasas",
         "Los Entes públicos (previsión) y el sujeto pasivo (devolución)",
         ["La exacción ha de estar **prevista en los Presupuestos** (11)", "Se **devuelve** la tasa si no se realiza el hecho imponible por causas **no imputables** al sujeto pasivo (12)"],
         "—",
         "La devolución procede cuando la causa **no es imputable al sujeto pasivo**; si no se realiza por causa suya, no hay devolución por este artículo."))}
""", 2)

T.ap("s11", "III.3 Elementos de la tasa: hecho imponible, devengo, sujetos y beneficios (Ley 8/1989, arts. 13 a 18)", f"""
{unidad("3.1 Hecho imponible y aplicación territorial (arts. 13 y 14)",
  lit("L8_1989", "Artículo 13", ["La expedición de certificados o documentos a instancia de parte", "La participación como aspirantes en oposiciones, concursos o pruebas selectivas", "en los órdenes civil, contencioso-administrativo y social"]),
  lit("L8_1989", "Artículo 14", ["fuera del territorio nacional"]),
  fichab("Por qué servicios y actividades pueden establecerse tasas",
         "—",
         ["Licencias, visados, matrículas o autorizaciones; certificados a instancia de parte; registros oficiales", "Servicios académicos, portuarios y aeroportuarios, sanitarios, controles aduaneros", "Participación en **oposiciones**, concursos o pruebas selectivas", "Potestad jurisdiccional en los órdenes **civil, contencioso-administrativo y social**", "Cláusula general: servicios o actividades que se refieran, afecten o beneficien a personas determinadas (n)"],
         "—",
         "La tasa judicial del art. 13 m) se refiere a los órdenes **civil, contencioso-administrativo y social** (no al penal). Se exige aunque el servicio se preste **fuera del territorio nacional** (14)."))}

{unidad("3.2 Devengo (art. 15)",
  lit("L8_1989", "Artículo 15", ["cuando se inicie la prestación del servicio o la realización de la actividad", "Cuando se presente la solicitud que inicie la actuación o el expediente", 'mediante anuncios en el "Boletín Oficial del Estado"']),
  fichab("Cuándo se devenga la tasa",
         "—",
         ["Al conceder la utilización o el aprovechamiento, o al iniciarse el servicio o la actividad (cabe depósito previo)", "Al presentar la solicitud que inicia el expediente: **sin pago, no se tramita**"],
         "Tasas periódicas: tras notificar el alta, las sucesivas liquidaciones pueden notificarse **colectivamente** por anuncios en el BOE",
         "Si se devenga con la **solicitud**, el expediente no se tramita sin el pago."))}

{unidad("3.3 Sujeto pasivo y responsables (arts. 16 y 17)",
  lit("L8_1989", "Artículo 16", ["las personas físicas o jurídicas beneficiarias", "herencias yacentes, comunidades de bienes"]),
  lit("L8_1989", "Artículo 17", ["responderán solidariamente de las tasas, las Entidades o Sociedades aseguradoras de riesgos", "serán responsables subsidiarios los propietarios"]),
  fichab("Quién paga la tasa y quién responde",
         ["**Sujetos pasivos**: personas físicas o jurídicas beneficiarias del dominio público o a quienes afecten o beneficien los servicios o actividades; en su caso, herencias yacentes, comunidades de bienes y entes sin personalidad", "**Responsables solidarios**: aseguradoras de riesgos que motiven el servicio", "**Responsables subsidiarios**: propietarios de inmuebles, en tasas por servicios a usuarios u ocupantes"],
         "—", "—",
         "Aseguradoras: **solidarios**. Propietarios de inmuebles: **subsidiarios**."))}

{unidad("3.4 Exenciones y bonificaciones (art. 18)",
  lit("L8_1989", "Artículo 18", ["no se admitirá, en materia de tasas, beneficio tributario alguno", "Tratados o Acuerdos Internacionales"]),
  fichab("Beneficios tributarios en las tasas",
         "Solo a favor del Estado y los demás Entes públicos territoriales o institucionales, o por Tratados o Acuerdos Internacionales",
         "Regla general: **ningún** beneficio tributario",
         "—",
         "Sin perjuicio del art. 8 (capacidad económica). Los únicos beneficiarios posibles son **entes públicos** o los que resulten de **tratados**."))}
""", 2)

T.ap("s12", "III.4 Cuantía, memoria económico-financiera, pago y gestión (Ley 8/1989, arts. 19 a 23)", f"""
{unidad("4.1 Elementos cuantitativos (art. 19)",
  lit("L8_1989", "Artículo 19", ["tomando como referencia el valor de mercado correspondiente o el de la utilidad derivada de aquélla", "no podrá exceder, en su conjunto, del coste real o previsible del servicio o actividad", "Las Leyes de Presupuestos Generales del Estado podrán modificar la cuantía de las tasas"]),
  fichab("Cómo se calcula el importe de la tasa",
         "La ley de cada tasa; las Leyes de Presupuestos pueden modificar su cuantía (19.5)",
         ["Dominio público: valor de mercado o utilidad derivada", "Servicios o actividades: **no puede exceder** del coste real o previsible (o, en su defecto, del valor de la prestación)", "Costes directos e indirectos, financieros, amortización y mantenimiento", "Cuota: cantidad fija, tipo de gravamen sobre una base, o ambos"],
         "—",
         "Tasa por servicio: **tope** = coste real o previsible **en su conjunto**. Las Leyes de Presupuestos **pueden modificar la cuantía** (no crear la tasa: CE 134.7 → II.1.3)."))}

{unidad("4.2 Memoria económico-financiera (art. 20)",
  lit("L8_1989", "Artículo 20", ["una memoria económico-financiera", "la nulidad de pleno derecho de las disposiciones reglamentarias que determinen las cuantías de las tasas", "reintegro del coste total"]),
  fichab("Requisito de toda propuesta de nueva tasa o de modificación de cuantías",
         "Quien elabore la propuesta",
         ["Memoria sobre el coste o valor del recurso o actividad y la justificación de la cuantía", "Destrucción o deterioro del dominio público no previsto: reintegro del coste de reconstrucción o reparación, además de la tasa"],
         "—",
         "Sin memoria: **nulidad de pleno derecho** de las disposiciones **reglamentarias** que fijen las cuantías."))}

{unidad("4.3 Pago, gestión y autoliquidación (arts. 21 a 23)",
  lit("L8_1989", "Artículo 21", ["en efectivo o mediante el empleo de efectos timbrados"]),
  lit("L8_1989", "Artículo 22", ["corresponde al Ministerio de Economía y Hacienda", "los principios y procedimientos de la Ley General Tributaria"]),
  lit("L8_1989", "Artículo 23", ["cuando así se prevea reglamentariamente"]),
  fichab("Cómo se pagan y se gestionan las tasas",
         "Gestión: el «Ministerio de Economía y Hacienda» (denominación de la ley, de 1989), con posible participación reglamentaria de otros departamentos y entes",
         ["Pago en efectivo o con efectos timbrados (21)", "Gestión con los principios y procedimientos de la **LGT**: liquidación, recaudación, inspección y revisión (22.3)", "Autoliquidación e ingreso en el Tesoro cuando lo prevea un reglamento (23)"],
         "—",
         "Como son **tributos**, en su gestión se aplica **en todo caso** la LGT (en los precios públicos, en cambio, la LGP: art. 27.7 → IV.2.2)."))}

{resumen([
  "La Ley 8/1989 regula **tasas y precios públicos** (1); no se aplica, entre otros, a las **cotizaciones sociales** ni a las tarifas de los concesionarios (2).",
  "Tasa = **tributo** por dominio público o por servicios o actividades no voluntarios o no prestados por el sector privado (6); **tiende** a cubrir el coste (7).",
  "Se establece **con arreglo a Ley**; el reglamento solo concreta cuantías si la ley lo autoriza (10).",
  "Ningún beneficio tributario salvo entes públicos o tratados (18); importe **no superior al coste** del servicio (19.2); las Leyes de Presupuestos pueden modificar la cuantía (19.5).",
  "Sin **memoria económico-financiera**, nulidad de pleno derecho de los reglamentos que fijen cuantías (20); gestión conforme a la **LGT** (22)."],
  "Siguiente: IV. ¿Qué son los precios públicos y en qué se diferencian de las tasas?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Qué son los precios públicos y en qué se diferencian de las tasas? (Ley 8/1989, arts. 24 a 27)", donde(
  "Cuarta pregunta. El título III de la Ley 8/1989 regula los **precios públicos**: no son tributos, sino **contraprestaciones pecuniarias**. Por eso no exigen ley para establecerse y su cuantía busca **cubrir, como mínimo**, los costes.",
  ["1 Concepto y cuantía (arts. 24 y 25)", "2 Establecimiento, administración y cobro (arts. 26 y 27; disposición adicional séptima)", "3 Cuadro comparativo: tasas y precios públicos"]))

T.ap("s13", "IV.1 Concepto y cuantía de los precios públicos (Ley 8/1989, arts. 24 y 25)", f"""
{unidad("1.1 Concepto (art. 24)",
  lit("L8_1989", "Artículo 24", ["contraprestaciones pecuniarias", "prestándose también tales servicios o actividades por el sector privado, sean de solicitud voluntaria"]),
  fichab("Qué es un precio público",
         "Lo pagan los administrados que solicitan voluntariamente el servicio o la actividad",
         ["Contraprestación **pecuniaria**", "Por servicios o actividades en régimen de **Derecho público**", "Que **también presta el sector privado** y", "Que son de **solicitud voluntaria**"],
         "—",
         "Hacen falta las **dos** condiciones a la vez (sector privado **y** solicitud voluntaria). Si falta una, es **tasa** (→ III.1.2). Nunca grava el uso del **dominio público**."))}

{unidad("1.2 Cuantía (art. 25)",
  lit("L8_1989", "Artículo 25", ["que cubra, como mínimo, los costes económicos", "razones sociales, benéficas, culturales o de interés público", "previa adopción de las previsiones presupuestarias oportunas"]),
  fichab("Cómo se fija el importe del precio público",
         "—",
         ["Regla: nivel que cubra, **como mínimo**, los costes económicos, o equivalente a la utilidad derivada", "Excepción: inferior por razones **sociales, benéficas, culturales o de interés público**, previa previsión presupuestaria para cubrir la parte subvencionada"],
         "—",
         "Precio público: **como mínimo** el coste. Tasa por servicio: **como máximo** el coste (art. 19.2 → III.4.1)."))}
""", 2)

T.ap("s14", "IV.2 Establecimiento, administración y cobro de los precios públicos (Ley 8/1989, arts. 26 y 27; disposición adicional séptima)", f"""
{unidad("2.1 Establecimiento y modificación (art. 26)",
  lit("L8_1989", "Artículo 26", ["Por Orden del Departamento ministerial del que dependa el órgano que ha de percibirlos", "Directamente por los organismos públicos, previa autorización del Departamento ministerial del que dependan", "memoria económico-financiera"]),
  fichab("Quién establece o modifica la cuantía de los precios públicos",
         ["El **Departamento ministerial** del que dependa el órgano que los percibe, por **Orden** y a propuesta de este", "Los **organismos públicos**, directamente, **previa autorización** de su Departamento"],
         "Con **memoria económico-financiera** que justifique el importe y el grado de cobertura de los costes",
         "—",
         "No hace falta **ley**: basta una **Orden** ministerial (o el propio organismo con autorización). Es el distractor de la pregunta de 2025 sobre las tasas (→ Cierre 1)."))}

{unidad("2.2 Administración y cobro (art. 27) y aplicación supletoria (disposición adicional séptima)",
  lit("L8_1989", "Artículo 27", ["por los Departamentos y organismos públicos que hayan de percibirlos", "desde que se inicie la prestación de servicios", "procedimiento administrativo de apremio", "Ley General Presupuestaria"]),
  lit("L8_1989", "septima", ["aplicación supletoria"]),
  fichab("Cómo se cobran los precios públicos",
         "Los **Departamentos y organismos públicos** que hayan de percibirlos",
         ["Exigibles desde que se inicia la prestación; cabe **anticipo o depósito previo**", "Pago en efectivo o con efectos timbrados", "Devolución si el servicio no se presta por causas no imputables al obligado (en espectáculos, canje de entradas)", "Deudas: por **procedimiento administrativo de apremio**", "En lo no previsto: **LGP** y demás normas aplicables"],
         "—",
         "Aunque no son tributos, las deudas por precios públicos pueden cobrarse **por apremio**. El título III es **supletorio** para Comunidades Autónomas y Haciendas Locales (disposición adicional séptima)."))}
""", 2)

T.ap("s15", "IV.3 Cuadro comparativo: tasas y precios públicos (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados de la Ley 8/1989 y de la LGT; no es texto legal.*

| | Tasa | Precio público |
|---|---|---|
| Naturaleza | **Tributo** (LGT 2.2 a; Ley 8/1989, art. 6) | **Contraprestación pecuniaria**, no tributo (art. 24) |
| Dominio público | Sí: utilización privativa o aprovechamiento especial | No |
| Servicios o actividades | No voluntarios **o** no prestados por el sector privado | Prestados **también** por el sector privado **y** de solicitud voluntaria |
| Establecimiento | **Con arreglo a Ley** (art. 10) | **Orden** del Departamento u organismo con autorización (art. 26) |
| Cuantía | Tiende a cubrir el coste; **no puede exceder** del coste del servicio (arts. 7 y 19.2) | Cubre **como mínimo** los costes (art. 25.1) |
| Memoria económico-financiera | Sí (art. 20) | Sí (art. 26.2) |
| Gestión y cobro | Ministerio de Economía y Hacienda, con la **LGT** (art. 22) | Departamentos y organismos que los perciben; **LGP** en lo no previsto (art. 27) |
| Beneficios | Ninguno, salvo entes públicos y tratados (art. 18) | Precios inferiores al coste por razones sociales, benéficas, culturales o de interés público (art. 25.2) |

{resumen([
  "Precio público: **contraprestación pecuniaria** por servicios o actividades que **también presta el sector privado** y que son de **solicitud voluntaria** (24).",
  "Cuantía: **como mínimo** los costes; menos solo por razones sociales, benéficas, culturales o de interés público (25).",
  "Se establece por **Orden** del Departamento o directamente por el organismo con autorización, con **memoria económico-financiera** (26).",
  "Lo cobran los Departamentos y organismos; cabe **apremio**; supletoriamente, la **LGP** (27)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_L97 = examen("L", 97, {
  "a": f"Las tasas gravan el dominio público o servicios y actividades públicas: {c('LGT', 'Artículo 2', 'utilización privativa o el aprovechamiento especial del dominio público')} (art. 2.2 a); no el beneficio por obras públicas.",
  "b": f"Los precios públicos no son tributos: son {c('L8_1989', 'Artículo 24', 'contraprestaciones pecuniarias')} (Ley 8/1989, art. 24).",
  "c": f"Los impuestos son {c('LGT', 'Artículo 2', 'tributos exigidos sin contraprestación')}, ligados a la capacidad económica (art. 2.2 c); el enunciado describe un beneficio por obras o servicios.",
  "d": f"Literal del art. 2.2 b): {c('LGT', 'Artículo 2', 'Contribuciones especiales son los tributos cuyo hecho imponible consiste en la obtención por el obligado tributario de un beneficio o de un aumento de valor de sus bienes')}."},
  [("Contribuciones especiales", "LGT", "Artículo 2", "Contribuciones especiales son los tributos cuyo hecho imponible consiste en la obtención por el obligado tributario de un beneficio o de un aumento de valor de sus bienes")])
EX_P97 = examen("P", 97, {
  "a": f"Tasas: {c('LGT', 'Artículo 2', 'utilización privativa o el aprovechamiento especial del dominio público')} o servicios que beneficien de modo particular (art. 2.2 a).",
  "b": f"Literal del art. 2.2 b): {c('LGT', 'Artículo 2', 'Contribuciones especiales son los tributos cuyo hecho imponible consiste en la obtención por el obligado tributario de un beneficio o de un aumento de valor de sus bienes')}.",
  "c": f"Impuestos: {c('LGT', 'Artículo 2', 'tributos exigidos sin contraprestación cuyo hecho imponible está constituido por negocios, actos o hechos que ponen de manifiesto la capacidad económica del contribuyente')} (art. 2.2 c).",
  "d": f"Los precios públicos no están en el art. 2 LGT: no son tributos, sino {c('L8_1989', 'Artículo 24', 'contraprestaciones pecuniarias')} (Ley 8/1989, art. 24)."},
  [("Contribuciones especiales", "LGT", "Artículo 2", "Contribuciones especiales son los tributos cuyo hecho imponible consiste en la obtención por el obligado tributario de un beneficio o de un aumento de valor de sus bienes")])
EX_L98 = examen("L", 98, {
  "a": f"Literal del art. 10.1: el establecimiento de las tasas {c('L8_1989', 'Artículo 10', 'deberá realizarse con arreglo a Ley')}.",
  "b": f"El reglamento solo puede concretar cuantías cuando se autorice por Ley: {c('L8_1989', 'Artículo 10', 'se podrán concretar mediante norma reglamentaria las cuantías exigibles')} (art. 10.3); el establecimiento no.",
  "c": "La Ley 8/1989 exige ley, no ley orgánica: el art. 10.1 dice «con arreglo a Ley», sin más.",
  "d": f"Es el régimen de los **precios públicos**: {c('L8_1989', 'Artículo 26', 'El establecimiento o modificación de la cuantía de los precios públicos se hará')} por Orden del Departamento o directamente por los organismos públicos (art. 26.1)."},
  [("Ley.", "L8_1989", "Artículo 10", "El establecimiento de las tasas, así como la regulación de los elementos esenciales de cada una de ellas, deberá realizarse con arreglo a Ley.")])
EX_P98 = examen("P", 98, {
  "a": f"Devengo: {c('LGT', 'Artículo 21', 'el momento en el que se entiende realizado el hecho imponible')} (art. 21.1); es un momento, no el presupuesto.",
  "b": f"Literal del art. 20.1: {c('LGT', 'Artículo 20', 'El hecho imponible es el presupuesto fijado por la ley para configurar cada tributo y cuya realización origina el nacimiento de la obligación tributaria principal')}.",
  "c": f"Exigibilidad: la ley puede situarla {c('LGT', 'Artículo 21', 'en un momento distinto al del devengo del tributo')} (art. 21.2).",
  "d": f"Exención: supuestos en que, {c('LGT', 'Artículo 22', 'a pesar de realizarse el hecho imponible, la ley exime del cumplimiento de la obligación tributaria principal')} (art. 22)."},
  [("Hecho imponible", "LGT", "Artículo 20", "El hecho imponible es el presupuesto fijado por la ley para configurar cada tributo y cuya realización origina el nacimiento de la obligación tributaria principal")])

T.ap("s16", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **cuatro** preguntas de este tema que se pueden comprobar contra el texto legal: dos sobre las clases de tributos, una sobre el establecimiento de las tasas y una sobre el hecho imponible. Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-L 2025, pregunta 97 · Contribuciones especiales (→ II.3.1)", EX_L97,
  "### GACE-P 2025, pregunta 97 · Contribuciones especiales (→ II.3.1)", EX_P97,
  "### GACE-L 2025, pregunta 98 · Establecimiento de las tasas (→ III.2.2)", EX_L98,
  "### GACE-P 2025, pregunta 98 · Hecho imponible (→ II.5.1)", EX_P98,
  "*Nota: el ejercicio extraordinario de 2025 (pregunta 97) preguntó qué fuente **no** constituye un ingreso público según la LGP (la plantilla da «Préstamos entre entidades privadas»). No se reproduce aquí: la LGP no enumera literalmente las fuentes de sus opciones, así que su respuesta no puede comprobarse contra un fragmento literal de la ley. La clasificación económica de los ingresos que sí recoge la LGP está en → I.2.2.*",
  "### Cómo se pregunta",
  "!> Las clases de tributos se preguntan copiando la **definición literal** del art. 2.2 LGT y poniendo como distractores las **otras clases** y los **precios públicos**. Las tasas se preguntan por su **forma de establecimiento** (ley) frente a la de los **precios públicos** (Orden).",
]))

T.ap("s17", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Ingresos públicos | Hacienda Pública estatal (LGP 5); derechos públicos y privados; no afectación (27.3); clasificación orgánica y económica (41); prestaciones patrimoniales (LGT, disp. adic. 1.ª) | Derechos de naturaleza **pública** = tributos y los que derivan de **potestades administrativas** |
| II. Sistema tributario | CE 31.1, 133 y 134.7; tributo (LGT 2.1); clases (2.2); principios (3); potestad (4); fuentes (7); reserva de ley (8); vigencia (10); hecho imponible, devengo, exención (20-22) | **Contribuciones especiales**: beneficio o aumento de valor por obras o servicios públicos; **hecho imponible**: presupuesto fijado por la ley |
| III. Tasas | Tributo (art. 6); con arreglo a Ley (10); hecho imponible (13); sin beneficios (18); coste máximo (19.2); memoria (20); gestión con la LGT (22) | Se establecen **por Ley** |
| IV. Precios públicos | Contraprestación por servicios también privados y voluntarios (24); como mínimo el coste (25); Orden (26); apremio (27.6) | Se establecen **por Orden** del Departamento |

?> **Trampas frecuentes:** «los precios públicos son una clase de tributo» (los tributos son **tasas, contribuciones especiales e impuestos**); «las tasas se establecen por Orden ministerial» (eso es de los **precios públicos**; las tasas, **con arreglo a Ley**); «las tasas cubren como mínimo el coste» (eso es de los precios públicos; la tasa **no puede exceder** del coste); «las normas tributarias entran en vigor a los veinte días **hábiles**» (son **naturales**); «la Ley de Presupuestos puede crear tributos» (**no puede crearlos**; puede modificarlos si una ley tributaria sustantiva lo prevé); «exención = no se realiza el hecho imponible» (en la exención **sí** se realiza).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
Q = T.q
# Bloque I
Q("LGP", "Artículo 5", "Ingresos públicos", "Según el artículo 5.1 de la Ley 47/2003, General Presupuestaria, la Hacienda Pública estatal está constituida por el conjunto de derechos y obligaciones de contenido económico cuya titularidad corresponde a:",
  ["La Administración General del Estado y a sus organismos autónomos.", "Todas las entidades del sector público estatal.", "El Estado, las Comunidades Autónomas y las entidades locales.", "La Administración General del Estado exclusivamente."],
  "Art. 5.1 LGP.", "cuya titularidad corresponde a la Administración General del Estado y a sus organismos autónomos")
Q("LGP", "Artículo 5", "Ingresos públicos", "Según el artículo 5.2 de la Ley General Presupuestaria, los derechos de la Hacienda Pública estatal se clasifican en:",
  ["Derechos de naturaleza pública y de naturaleza privada.", "Derechos tributarios y no tributarios.", "Derechos corrientes y de capital.", "Derechos ordinarios y extraordinarios."],
  "Art. 5.2 LGP.", "Los derechos de la Hacienda Pública estatal se clasifican en derechos de naturaleza pública y de naturaleza privada")
Q("LGP", "Artículo 5", "Ingresos públicos", "Según el artículo 5.2 de la Ley General Presupuestaria, son derechos de naturaleza pública de la Hacienda Pública estatal los tributos y los demás derechos de contenido económico cuya titularidad corresponde a la Administración General del Estado y sus organismos autónomos que deriven:",
  ["Del ejercicio de potestades administrativas.", "De contratos sujetos al derecho privado.", "De la gestión de su patrimonio privado.", "De cualquier negocio jurídico celebrado por ellos."],
  "Art. 5.2 LGP.", "que deriven del ejercicio de potestades administrativas")
Q("LGP", "Artículo 19", "Ingresos públicos", "Según el artículo 19.1 de la Ley General Presupuestaria, la efectividad de los derechos de naturaleza privada de la Hacienda Pública estatal se llevará a cabo:",
  ["Con sujeción a las normas y procedimientos del derecho privado.", "Con las prerrogativas establecidas para los tributos en la Ley General Tributaria.", "Mediante el procedimiento administrativo de apremio en todo caso.", "Conforme al Reglamento General de Recaudación exclusivamente."],
  "Art. 19.1 LGP.", "con sujeción a las normas y procedimientos del derecho privado")
Q("LGP", "Artículo 27", "Ingresos públicos", "Según el artículo 27.3 de la Ley General Presupuestaria, los recursos del Estado se destinarán a satisfacer el conjunto de sus respectivas obligaciones:",
  ["Salvo que por ley se establezca su afectación a fines determinados.", "Salvo que el Ministro de Hacienda acuerde su afectación a fines determinados.", "Sin excepción alguna.", "Salvo que el Consejo de Ministros los afecte mediante real decreto."],
  "Art. 27.3 LGP.", "salvo que por ley se establezca su afectación a fines determinados")
Q("LGP", "Artículo 41", "Clasificación de los ingresos", "Según el artículo 41 de la Ley General Presupuestaria, los estados de ingresos de los Presupuestos Generales del Estado se estructurarán siguiendo las clasificaciones:",
  ["Orgánica y económica.", "Orgánica, por programas y económica.", "Económica y funcional.", "Por programas y territorial."],
  "Art. 41 LGP.", "se estructurarán siguiendo las clasificaciones orgánica y económica")
Q("LGP", "Artículo 41", "Clasificación de los ingresos", "Según el artículo 41 b) de la Ley General Presupuestaria, en los ingresos de capital se distinguirán:",
  ["Enajenación de inversiones reales y transferencias de capital.", "Tasas, precios públicos y otros ingresos.", "Activos financieros y pasivos financieros.", "Impuestos directos e impuestos indirectos."],
  "Art. 41 b) LGP.", "En los ingresos de capital se distinguirán: enajenación de inversiones reales y transferencias de capital")
Q("LGP", "Artículo 41", "Clasificación de los ingresos", "Según el artículo 41 b) de la Ley General Presupuestaria, las tasas y los precios públicos se incluyen entre los ingresos:",
  ["Corrientes.", "De capital.", "Por operaciones financieras.", "Extraordinarios."],
  "Art. 41 b) LGP: «En los ingresos corrientes se distinguirán: impuestos directos y cotizaciones sociales, impuestos indirectos, tasas, precios públicos y otros ingresos…».", "En los ingresos corrientes se distinguirán: impuestos directos y cotizaciones sociales, impuestos indirectos, tasas, precios públicos y otros ingresos")
Q("LGT", "daprimera", "Prestaciones patrimoniales", "Según la disposición adicional primera de la Ley General Tributaria, las prestaciones patrimoniales de carácter público exigidas por la prestación de un servicio en régimen de concesión tienen la consideración de:",
  ["Prestaciones patrimoniales de carácter público no tributarias.", "Tasas.", "Precios públicos.", "Contribuciones especiales."],
  "Disp. adic. 1.ª.2 LGT.", ["prestaciones patrimoniales de carácter público no tributarias", "en régimen de concesión"])
Q("LGT", "daprimera", "Prestaciones patrimoniales", "Según la disposición adicional primera de la Ley General Tributaria, son prestaciones patrimoniales de carácter público aquellas a las que se refiere el artículo 31.3 de la Constitución que se exigen:",
  ["Con carácter coactivo.", "Con carácter voluntario.", "Solo por las Comunidades Autónomas.", "Mediante contrato privado."],
  "Disp. adic. 1.ª.1 LGT.", "que se exigen con carácter coactivo")
# Bloque II
Q("CE", "Artículo 31", "Sistema tributario", "Según el artículo 31.1 de la Constitución, el sistema tributario justo estará inspirado en los principios de:",
  ["Igualdad y progresividad.", "Igualdad y proporcionalidad.", "Generalidad y eficacia.", "Legalidad y seguridad jurídica."],
  "Art. 31.1 CE.", "inspirado en los principios de igualdad y progresividad")
Q("CE", "Artículo 133", "Sistema tributario", "Según el artículo 133.3 de la Constitución, todo beneficio fiscal que afecte a los tributos del Estado deberá establecerse:",
  ["En virtud de ley.", "Mediante real decreto.", "Mediante orden del Ministro de Hacienda.", "Mediante ley orgánica."],
  "Art. 133.3 CE.", "Todo beneficio fiscal que afecte a los tributos del Estado deberá establecerse en virtud de ley")
Q("CE", "Artículo 134", "Sistema tributario", "Según el artículo 134.7 de la Constitución, la Ley de Presupuestos:",
  ["No puede crear tributos; podrá modificarlos cuando una ley tributaria sustantiva así lo prevea.", "Puede crear y modificar tributos libremente.", "Puede crear tributos cuando una ley tributaria sustantiva así lo prevea.", "No puede crear ni modificar tributos en ningún caso."],
  "Art. 134.7 CE.", "La Ley de Presupuestos no puede crear tributos. Podrá modificarlos cuando una ley tributaria sustantiva así lo prevea")
Q("LGT", "Artículo 2", "Sistema tributario", "Según el artículo 2.1 de la Ley General Tributaria, los tributos son los ingresos públicos que consisten en prestaciones pecuniarias exigidas por:",
  ["Una Administración pública.", "El Estado exclusivamente.", "Cualquier entidad del sector público empresarial.", "Las Cortes Generales."],
  "Art. 2.1 LGT.", "prestaciones pecuniarias exigidas por una Administración pública")
Q("LGT", "Artículo 2", "Clases de tributos", "Según el artículo 2.2 de la Ley General Tributaria, los tributos, cualquiera que sea su denominación, se clasifican en:",
  ["Tasas, contribuciones especiales e impuestos.", "Tasas, precios públicos e impuestos.", "Impuestos directos, impuestos indirectos y tasas.", "Tasas, contribuciones especiales, impuestos y precios públicos."],
  "Art. 2.2 LGT.", "se clasifican en tasas, contribuciones especiales e impuestos")
Q("LGT", "Artículo 2", "Clases de tributos", "Según el artículo 2.2 de la Ley General Tributaria, los tributos exigidos sin contraprestación cuyo hecho imponible está constituido por negocios, actos o hechos que ponen de manifiesto la capacidad económica del contribuyente son:",
  ["Impuestos.", "Tasas.", "Contribuciones especiales.", "Precios públicos."],
  "Art. 2.2 c) LGT.", "Impuestos son los tributos exigidos sin contraprestación")
Q("LGT", "Artículo 2", "Clases de tributos", "Según el artículo 2.2 a) de la Ley General Tributaria, son tasas los tributos cuyo hecho imponible consiste, entre otros supuestos, en:",
  ["La utilización privativa o el aprovechamiento especial del dominio público.", "La obtención de un aumento de valor de los bienes por la realización de obras públicas.", "Negocios, actos o hechos que ponen de manifiesto la capacidad económica.", "La compra voluntaria de bienes producidos por empresas públicas."],
  "Art. 2.2 a) LGT.", "Tasas son los tributos cuyo hecho imponible consiste en la utilización privativa o el aprovechamiento especial del dominio público")
Q("LGT", "Artículo 3", "Sistema tributario", "Según el artículo 3.2 de la Ley General Tributaria, la aplicación del sistema tributario se basará en los principios de:",
  ["Proporcionalidad, eficacia y limitación de costes indirectos derivados del cumplimiento de obligaciones formales.", "Justicia, generalidad e igualdad.", "Progresividad y no confiscatoriedad.", "Capacidad económica y equitativa distribución de la carga tributaria."],
  "Art. 3.2 LGT (las otras opciones son principios de ordenación, art. 3.1).", "La aplicación del sistema tributario se basará en los principios de proporcionalidad, eficacia y limitación de costes indirectos derivados del cumplimiento de obligaciones formales")
Q("LGT", "Artículo 4", "Sistema tributario", "Según el artículo 4.3 de la Ley General Tributaria, las demás entidades de derecho público (distintas del Estado, las comunidades autónomas y las entidades locales):",
  ["Podrán exigir tributos cuando una ley así lo determine.", "En ningún caso podrán exigir tributos.", "Podrán establecer tributos mediante reglamento.", "Podrán exigir tributos cuando lo autorice el Ministro de Hacienda."],
  "Art. 4.3 LGT.", "Las demás entidades de derecho público podrán exigir tributos cuando una ley así lo determine")
Q("LGT", "Artículo 7", "Sistema tributario", "Según el artículo 7.1 e) de la Ley General Tributaria, en el ámbito tributario local los tributos se regirán, específicamente, por:",
  ["Las correspondientes ordenanzas fiscales.", "Los Estatutos de Autonomía.", "Los decretos de alcaldía.", "Las órdenes del Ministro de Hacienda."],
  "Art. 7.1 e) LGT.", "específicamente en el ámbito tributario local, por las correspondientes ordenanzas fiscales")
Q("LGT", "Artículo 7", "Sistema tributario", "Según el artículo 7.2 de la Ley General Tributaria, tendrán carácter supletorio en materia tributaria:",
  ["Las disposiciones generales del derecho administrativo y los preceptos del derecho común.", "Las ordenanzas fiscales.", "Los convenios para evitar la doble imposición.", "Las normas de la Unión Europea."],
  "Art. 7.2 LGT.", "Tendrán carácter supletorio las disposiciones generales del derecho administrativo y los preceptos del derecho común")
Q("LGT", "Artículo 8", "Sistema tributario", "Según el artículo 8 de la Ley General Tributaria, ¿cuál de las siguientes materias se regulará en todo caso por ley?",
  ["La condonación de deudas y sanciones tributarias.", "La aprobación de los modelos de autoliquidación.", "La organización interna de la Agencia Estatal de Administración Tributaria.", "El horario de atención al público de las oficinas tributarias."],
  "Art. 8 k) LGT.", "La condonación de deudas y sanciones tributarias y la concesión de moratorias y quitas")
Q("LGT", "Artículo 10", "Sistema tributario", "Según el artículo 10.1 de la Ley General Tributaria, si en ellas no se dispone otra cosa, las normas tributarias entrarán en vigor:",
  ["A los veinte días naturales de su completa publicación en el boletín oficial que corresponda.", "A los veinte días hábiles de su publicación.", "Al día siguiente de su publicación.", "Al mes de su publicación."],
  "Art. 10.1 LGT.", "Las normas tributarias entrarán en vigor a los veinte días naturales de su completa publicación en el boletín oficial que corresponda")
Q("LGT", "Artículo 10", "Sistema tributario", "Según el artículo 10.2 de la Ley General Tributaria, las normas que regulen el régimen de infracciones y sanciones tributarias y el de los recargos tendrán efectos retroactivos:",
  ["Respecto de los actos que no sean firmes cuando su aplicación resulte más favorable para el interesado.", "En todo caso.", "Respecto de los actos firmes y no firmes.", "Nunca."],
  "Art. 10.2 LGT.", "tendrán efectos retroactivos respecto de los actos que no sean firmes cuando su aplicación resulte más favorable para el interesado")
Q("LGT", "Artículo 21", "Obligación tributaria", "Según el artículo 21.1 de la Ley General Tributaria, el momento en el que se entiende realizado el hecho imponible y en el que se produce el nacimiento de la obligación tributaria principal es:",
  ["El devengo.", "La exigibilidad.", "La liquidación.", "La exención."],
  "Art. 21.1 LGT.", "El devengo es el momento en el que se entiende realizado el hecho imponible")
Q("LGT", "Artículo 22", "Obligación tributaria", "Según el artículo 22 de la Ley General Tributaria, son supuestos de exención aquellos en que:",
  ["A pesar de realizarse el hecho imponible, la ley exime del cumplimiento de la obligación tributaria principal.", "No llega a realizarse el hecho imponible.", "La Administración condona la deuda una vez liquidada.", "El obligado tributario renuncia al pago por causa justificada."],
  "Art. 22 LGT.", "a pesar de realizarse el hecho imponible, la ley exime del cumplimiento de la obligación tributaria principal")
Q("LGT", "Artículo 36", "Obligación tributaria", "Según el artículo 36.2 de la Ley General Tributaria, es contribuyente:",
  ["El sujeto pasivo que realiza el hecho imponible.", "El sujeto pasivo que, en lugar de otro, está obligado a cumplir la obligación tributaria principal.", "La persona a quien la ley obliga a retener e ingresar parte de los pagos que realiza.", "El responsable solidario de la deuda tributaria."],
  "Art. 36.2 LGT.", "Es contribuyente el sujeto pasivo que realiza el hecho imponible")
# Bloque III
Q("L8_1989", "Artículo 2", "Tasas", "Según el artículo 2 de la Ley 8/1989, de Tasas y Precios Públicos, los preceptos de esta ley no serán aplicables a:",
  ["Las cotizaciones al sistema de la Seguridad Social.", "Las tasas por expedición de certificados.", "Los precios públicos de los organismos autónomos.", "Las tasas por servicios portuarios."],
  "Art. 2 a) Ley 8/1989.", "Las cotizaciones al sistema de la Seguridad Social")
Q("L8_1989", "Artículo 7", "Tasas", "Según el artículo 7 de la Ley 8/1989 (principio de equivalencia), las tasas:",
  ["Tenderán a cubrir el coste del servicio o de la actividad que constituya su hecho imponible.", "Cubrirán, como mínimo, el doble del coste del servicio.", "Se fijarán exclusivamente según la capacidad económica del obligado.", "Se fijarán libremente por el órgano que las perciba."],
  "Art. 7 Ley 8/1989.", "Las tasas tenderán a cubrir el coste del servicio o de la actividad que constituya su hecho imponible")
Q("L8_1989", "Artículo 10", "Tasas", "Según el artículo 10.3 de la Ley 8/1989, mediante norma reglamentaria se podrán concretar las cuantías exigibles para cada tasa:",
  ["Cuando se autorice por Ley, con subordinación a los criterios o elementos de cuantificación que determine la misma.", "En todo caso, sin necesidad de autorización legal.", "Solo mediante Orden del Departamento que perciba la tasa.", "Nunca: las cuantías solo pueden fijarse por ley orgánica."],
  "Art. 10.3 Ley 8/1989.", "Cuando se autorice por Ley, con subordinación a los criterios o elementos de cuantificación que determine la misma")
Q("L8_1989", "Artículo 12", "Tasas", "Según el artículo 12 de la Ley 8/1989, procederá la devolución de las tasas que se hubieran exigido cuando no se realice su hecho imponible:",
  ["Por causas no imputables al sujeto pasivo.", "Por cualquier causa, incluida la renuncia del sujeto pasivo.", "Solo por causa de fuerza mayor declarada judicialmente.", "Por causas imputables al sujeto pasivo."],
  "Art. 12 Ley 8/1989.", "cuando no se realice su hecho imponible por causas no imputables al sujeto pasivo")
Q("L8_1989", "Artículo 13", "Tasas", "Según el artículo 13 m) de la Ley 8/1989, podrán establecerse tasas por el ejercicio de la potestad jurisdiccional en los órdenes:",
  ["Civil, contencioso-administrativo y social.", "Civil, penal y contencioso-administrativo.", "Penal y militar.", "Todos los órdenes jurisdiccionales."],
  "Art. 13 m) Ley 8/1989.", "Por el ejercicio de la potestad jurisdiccional en los órdenes civil, contencioso-administrativo y social")
Q("L8_1989", "Artículo 17", "Tasas", "Según el artículo 17.1 de la Ley 8/1989, responderán solidariamente de las tasas:",
  ["Las Entidades o Sociedades aseguradoras de riesgos que motiven actuaciones o servicios administrativos que constituyan el hecho imponible de una tasa.", "Los propietarios de los inmuebles en todo caso.", "Los funcionarios que gestionen la tasa.", "Las Comunidades Autónomas en cuyo territorio se preste el servicio."],
  "Art. 17.1 Ley 8/1989.", "responderán solidariamente de las tasas, las Entidades o Sociedades aseguradoras de riesgos")
Q("L8_1989", "Artículo 18", "Tasas", "Según el artículo 18 de la Ley 8/1989, en materia de tasas:",
  ["No se admitirá beneficio tributario alguno, salvo a favor del Estado y los demás Entes públicos territoriales o institucionales o como consecuencia de Tratados o Acuerdos Internacionales.", "Podrán establecerse bonificaciones por orden ministerial.", "Se admitirán exenciones a favor de cualquier persona física con escasa capacidad económica.", "Cada órgano gestor podrá conceder exenciones discrecionalmente."],
  "Art. 18 Ley 8/1989.", "no se admitirá, en materia de tasas, beneficio tributario alguno, salvo a favor del Estado y los demás Entes públicos territoriales o institucionales")
Q("L8_1989", "Artículo 19", "Tasas", "Según el artículo 19.2 de la Ley 8/1989, el importe de las tasas por la prestación de un servicio o por la realización de una actividad:",
  ["No podrá exceder, en su conjunto, del coste real o previsible del servicio o actividad de que se trate.", "Deberá cubrir, como mínimo, el coste del servicio o actividad.", "Se fijará tomando como referencia el valor de mercado del dominio público.", "Podrá superar el coste en un veinte por ciento."],
  "Art. 19.2 Ley 8/1989.", "no podrá exceder, en su conjunto, del coste real o previsible del servicio o actividad de que se trate")
Q("L8_1989", "Artículo 19", "Tasas", "Según el artículo 19.5 de la Ley 8/1989, la cuantía de las tasas podrá ser modificada por:",
  ["Las Leyes de Presupuestos Generales del Estado.", "Orden del Departamento ministerial que las perciba.", "Resolución del organismo que preste el servicio.", "Acuerdo de la Comisión Delegada del Gobierno para Asuntos Económicos."],
  "Art. 19.5 Ley 8/1989.", "Las Leyes de Presupuestos Generales del Estado podrán modificar la cuantía de las tasas")
Q("L8_1989", "Artículo 20", "Tasas", "Según el artículo 20.1 de la Ley 8/1989, la falta de la memoria económico-financiera en una propuesta de establecimiento o modificación de una tasa determinará:",
  ["La nulidad de pleno derecho de las disposiciones reglamentarias que determinen las cuantías de las tasas.", "La anulabilidad de la ley que establezca la tasa.", "Una mera irregularidad no invalidante.", "La devolución automática de las tasas ingresadas."],
  "Art. 20.1 Ley 8/1989.", "La falta de este requisito determinará la nulidad de pleno derecho de las disposiciones reglamentarias que determinen las cuantías de las tasas")
# Bloque IV
Q("L8_1989", "Artículo 24", "Precios públicos", "Según el artículo 24 de la Ley 8/1989, tendrán la consideración de precios públicos las contraprestaciones pecuniarias que se satisfagan por la prestación de servicios o la realización de actividades efectuadas en régimen de Derecho público cuando:",
  ["Prestándose también tales servicios o actividades por el sector privado, sean de solicitud voluntaria por parte de los administrados.", "No se presten por el sector privado, aunque sean de solicitud voluntaria.", "Sean de solicitud o recepción obligatoria para los administrados.", "Consistan en la utilización privativa del dominio público."],
  "Art. 24 Ley 8/1989.", "prestándose también tales servicios o actividades por el sector privado, sean de solicitud voluntaria por parte de los administrados")
Q("L8_1989", "Artículo 25", "Precios públicos", "Según el artículo 25.1 de la Ley 8/1989, los precios públicos se determinarán a un nivel que cubra:",
  ["Como mínimo, los costes económicos originados por la realización de las actividades o la prestación de los servicios.", "Como máximo, el cincuenta por ciento de los costes.", "Exclusivamente los costes directos de personal.", "Como máximo, los costes económicos del servicio."],
  "Art. 25.1 Ley 8/1989.", "a un nivel que cubra, como mínimo, los costes económicos originados por la realización de las actividades o la prestación de los servicios")
Q("L8_1989", "Artículo 26", "Precios públicos", "Según el artículo 26.1 de la Ley 8/1989, el establecimiento o modificación de la cuantía de los precios públicos se hará:",
  ["Por Orden del Departamento ministerial del que dependa el órgano que ha de percibirlos y a propuesta de éste, o directamente por los organismos públicos, previa autorización del Departamento ministerial del que dependan.", "Por Ley.", "Por Real Decreto acordado en Consejo de Ministros.", "Por la Ley de Presupuestos Generales del Estado en todo caso."],
  "Art. 26.1 Ley 8/1989.", ["Por Orden del Departamento ministerial del que dependa el órgano que ha de percibirlos y a propuesta de éste", "Directamente por los organismos públicos, previa autorización del Departamento ministerial del que dependan"])
Q("L8_1989", "Artículo 27", "Precios públicos", "Según el artículo 27.6 de la Ley 8/1989, las deudas por precios públicos:",
  ["Podrán exigirse mediante el procedimiento administrativo de apremio, conforme a la normativa vigente.", "Solo pueden reclamarse ante la jurisdicción civil.", "No pueden exigirse coactivamente.", "Se exigen exclusivamente mediante compensación."],
  "Art. 27.6 Ley 8/1989.", "Las deudas por precios públicos podrán exigirse mediante el procedimiento administrativo de apremio")
Q("L8_1989", "Artículo 27", "Precios públicos", "Según el artículo 27.1 de la Ley 8/1989, la administración y cobro de los precios públicos se realizará por:",
  ["Los Departamentos y organismos públicos que hayan de percibirlos.", "La Agencia Estatal de Administración Tributaria en todo caso.", "La Intervención General de la Administración del Estado.", "El Tribunal de Cuentas."],
  "Art. 27.1 Ley 8/1989.", "La administración y cobro de los precios públicos se realizará por los Departamentos y organismos públicos que hayan de percibirlos")

T.real("L", 97, "Clases de tributos"); T.real("P", 97, "Clases de tributos"); T.real("L", 98, "Tasas"); T.real("P", 98, "Obligación tributaria")

# Flashcards
for q_, a_, cat in [
  ("¿Qué es la Hacienda Pública estatal? (LGP, art. 5.1)", "El conjunto de derechos y obligaciones de contenido económico cuya titularidad corresponde a la AGE y a sus organismos autónomos.", "Ingresos públicos"),
  ("Derechos de naturaleza pública de la Hacienda Pública estatal (LGP, art. 5.2)", "Los tributos y los demás derechos de contenido económico de la AGE y sus organismos autónomos que deriven del ejercicio de potestades administrativas.", "Ingresos públicos"),
  ("Régimen de los derechos de naturaleza privada (LGP, art. 19.1)", "Normas y procedimientos del derecho privado.", "Ingresos públicos"),
  ("Clasificaciones de los estados de ingresos (LGP, art. 41)", "Orgánica y económica (corrientes, de capital y operaciones financieras).", "Clasificación de los ingresos"),
  ("Ingresos corrientes (LGP, art. 41 b)", "Impuestos directos y cotizaciones sociales, impuestos indirectos, tasas, precios públicos y otros ingresos, transferencias corrientes e ingresos patrimoniales.", "Clasificación de los ingresos"),
  ("Prestaciones patrimoniales de carácter público (LGT, disp. adic. 1.ª)", "Las del art. 31.3 CE exigidas con carácter coactivo; tributarias (tasas, contribuciones especiales, impuestos) o no tributarias.", "Prestaciones patrimoniales"),
  ("Principios del sistema tributario en la CE (art. 31.1)", "Capacidad económica; sistema justo inspirado en la igualdad y la progresividad; nunca confiscatorio.", "Sistema tributario"),
  ("¿Puede la Ley de Presupuestos crear tributos? (CE, art. 134.7)", "No. Puede modificarlos cuando una ley tributaria sustantiva así lo prevea.", "Sistema tributario"),
  ("Concepto de tributo (LGT, art. 2.1)", "Ingresos públicos que consisten en prestaciones pecuniarias exigidas por una Administración pública por realizar el supuesto de hecho al que la ley vincula el deber de contribuir.", "Sistema tributario"),
  ("Clases de tributos (LGT, art. 2.2)", "Tasas, contribuciones especiales e impuestos, cualquiera que sea su denominación.", "Clases de tributos"),
  ("Contribuciones especiales (LGT, art. 2.2 b)", "Tributos cuyo hecho imponible es el beneficio o aumento de valor de los bienes del obligado por obras públicas o por el establecimiento o ampliación de servicios públicos.", "Clases de tributos"),
  ("Principios de aplicación del sistema tributario (LGT, art. 3.2)", "Proporcionalidad, eficacia y limitación de costes indirectos derivados del cumplimiento de obligaciones formales.", "Sistema tributario"),
  ("Potestad tributaria (LGT, art. 4)", "Originaria: el Estado, mediante ley. CC. AA. y entidades locales: de acuerdo con la Constitución y las leyes. Demás entes de derecho público: exigir cuando una ley lo determine.", "Sistema tributario"),
  ("Entrada en vigor de las normas tributarias (LGT, art. 10.1)", "A los veinte días naturales de su completa publicación, si no disponen otra cosa.", "Sistema tributario"),
  ("Hecho imponible (LGT, art. 20.1)", "Presupuesto fijado por la ley para configurar cada tributo y cuya realización origina el nacimiento de la obligación tributaria principal.", "Obligación tributaria"),
  ("Devengo y exención (LGT, arts. 21 y 22)", "Devengo: momento en que se entiende realizado el hecho imponible. Exención: se realiza el hecho imponible pero la ley exime.", "Obligación tributaria"),
  ("¿Cómo se establecen las tasas? (Ley 8/1989, art. 10.1)", "Con arreglo a Ley (establecimiento y elementos esenciales).", "Tasas"),
  ("Tope del importe de la tasa por servicios (Ley 8/1989, art. 19.2)", "No puede exceder, en su conjunto, del coste real o previsible del servicio o actividad.", "Tasas"),
  ("Beneficios tributarios en las tasas (Ley 8/1989, art. 18)", "Ninguno, salvo a favor del Estado y demás Entes públicos o por Tratados o Acuerdos Internacionales.", "Tasas"),
  ("Concepto de precio público (Ley 8/1989, art. 24)", "Contraprestación pecuniaria por servicios o actividades en régimen de Derecho público que también presta el sector privado y que son de solicitud voluntaria.", "Precios públicos"),
  ("¿Cómo se establecen los precios públicos? (Ley 8/1989, art. 26.1)", "Por Orden del Departamento ministerial, o directamente por los organismos públicos con autorización de su Departamento.", "Precios públicos"),
  ("Cuantía de los precios públicos (Ley 8/1989, art. 25)", "Como mínimo, los costes económicos; inferior por razones sociales, benéficas, culturales o de interés público.", "Precios públicos"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Hacienda Pública estatal", "Conjunto de derechos y obligaciones de contenido económico cuya titularidad corresponde a la AGE y a sus organismos autónomos (LGP, art. 5.1).", "s1", "Ingresos públicos")
T.glos("Derechos de naturaleza pública", "Tributos y demás derechos de contenido económico de la AGE y sus organismos autónomos que derivan del ejercicio de potestades administrativas (LGP, art. 5.2).", "s1", "Ingresos públicos")
T.glos("Clasificación económica de los ingresos", "Agrupación de los ingresos en corrientes, de capital y operaciones financieras (LGP, art. 41 b).", "s2", "Ingresos públicos")
T.glos("Prestación patrimonial de carácter público", "La del art. 31.3 CE exigida con carácter coactivo; puede ser tributaria o no tributaria (LGT, disp. adic. 1.ª).", "s3", "Ingresos públicos")
T.glos("Tributo", "Ingreso público consistente en una prestación pecuniaria exigida por una Administración pública como consecuencia del supuesto de hecho al que la ley vincula el deber de contribuir (LGT, art. 2.1).", "s5", "Sistema tributario")
T.glos("Contribución especial", "Tributo cuyo hecho imponible es el beneficio o aumento de valor de los bienes del obligado por obras o servicios públicos (LGT, art. 2.2 b).", "s6", "Sistema tributario")
T.glos("Impuesto", "Tributo exigido sin contraprestación cuyo hecho imponible pone de manifiesto la capacidad económica del contribuyente (LGT, art. 2.2 c).", "s6", "Sistema tributario")
T.glos("Reserva de ley tributaria", "Materias que se regulan en todo caso por ley: elementos esenciales del tributo, beneficios fiscales, infracciones y sanciones, condonación, etc. (LGT, art. 8).", "s7", "Sistema tributario")
T.glos("Hecho imponible", "Presupuesto fijado por la ley para configurar cada tributo y cuya realización origina el nacimiento de la obligación tributaria principal (LGT, art. 20.1).", "s8", "Sistema tributario")
T.glos("Devengo", "Momento en el que se entiende realizado el hecho imponible y nace la obligación tributaria principal (LGT, art. 21.1).", "s8", "Sistema tributario")
T.glos("Tasa", "Tributo por la utilización privativa o el aprovechamiento especial del dominio público o por servicios o actividades en régimen de derecho público no voluntarios o no prestados por el sector privado (Ley 8/1989, art. 6).", "s9", "Tasas")
T.glos("Memoria económico-financiera", "Estudio sobre el coste o valor del recurso o actividad que debe acompañar a la propuesta de nueva tasa o de modificación de cuantías; su falta determina la nulidad de pleno derecho de los reglamentos de cuantías (Ley 8/1989, art. 20).", "s12", "Tasas")
T.glos("Precio público", "Contraprestación pecuniaria por servicios o actividades en régimen de Derecho público que también presta el sector privado y son de solicitud voluntaria (Ley 8/1989, art. 24).", "s13", "Precios públicos")

# Cronología (fechas de los metadatos del BOE)
T.hito("1978", "Constitución Española (27-12-1978; BOE de 29-12-1978)", "Arts. 31, 133 y 134.7: deber de contribuir, potestad tributaria y límites de la Ley de Presupuestos", "normativo", "s4")
T.hito("1989", "Ley 8/1989, de 13 de abril, de Tasas y Precios Públicos (BOE de 15-4-1989)", "Régimen jurídico de las tasas y los precios públicos", "normativo", "s9")
T.hito("1998", "Ley 25/1998, de 13 de julio, de modificación del Régimen Legal de las Tasas Estatales y Locales y de Reordenación de las Prestaciones Patrimoniales de Carácter Público (BOE de 14-7-1998)", "Da la redacción vigente, entre otros, de los arts. 10, 24 y 26 de la Ley 8/1989", "normativo", "s10")
T.hito("2003", "Ley 47/2003, de 26 de noviembre, General Presupuestaria (BOE de 27-11-2003)", "Arts. 5 y 41: derechos de la Hacienda Pública estatal y estructura de los estados de ingresos", "normativo", "s1")
T.hito("2003", "Ley 58/2003, de 17 de diciembre, General Tributaria (BOE de 18-12-2003; en vigor el 1-7-2004)", "Concepto y clases de tributos y principios del sistema tributario", "normativo", "s5")
T.hito("2017", "Ley 9/2017, de 8 de noviembre, de Contratos del Sector Público (BOE de 9-11-2017)", "Da la redacción vigente de la disposición adicional primera de la LGT y del art. 2 de la Ley 8/1989 (prestaciones patrimoniales de carácter público no tributarias)", "normativo", "s3")

T.publicar()
