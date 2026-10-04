# -*- coding: utf-8 -*-
"""Tema V.6 (B5T06): El sistema de retribuciones de los funcionarios. Retribuciones
básicas y retribuciones complementarias. Las indemnizaciones por razón del servicio.
Método del I.2. Normas (textos consolidados del BOE): TREBEP (RDLeg 5/2015), arts. 21 a 30,
disposición derogatoria única y disposición final cuarta; Ley 30/1984, arts. 23 y 24;
RDL 6/2023 (libro segundo), arts. 119.4 y 122.7 y disposición transitoria séptima;
Real Decreto 462/2002, sobre indemnizaciones por razón del servicio; Resolución de 20 de
enero de 2014 de la DG de Presupuestos (anexo II, artículo 23)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO.update({"L30": "Ley 30/1984", "RD462": "RD 462/2002", "RDL6": "RDL 6/2023", "RES2014": "Resolución de 20-1-2014"})


def cifra(k, art, v):
    """Cifra copiada de un anexo del BOE (sin comillas): se comprueba que está literal."""
    assert v in texto(k, art), ("CIFRA NO LITERAL", k, art, v)
    return v


T = Tema("B5T06",
  "Cinco preguntas: I. Cómo se ordena el sistema de retribuciones (TREBEP, arts. 21 y 22; Ley 30/1984) · II. Qué son las retribuciones básicas (sueldo, trienios y pagas extraordinarias) · III. Qué son las retribuciones complementarias (TREBEP, art. 24; Ley 30/1984, art. 23.3; RDL 6/2023) · IV. Qué reglas completan el sistema (interinos, prácticas, laborales, retribuciones diferidas y deducciones: arts. 25 a 27, 29 y 30) · V. Las indemnizaciones por razón del servicio (art. 28 y Real Decreto 462/2002). Cada artículo: texto literal del BOE y ficha.",
  ["Retribuciones básicas", "Sueldo", "Trienios", "Pagas extraordinarias", "Retribuciones complementarias", "Complemento de destino", "Complemento específico", "Productividad", "Gratificaciones", "Complemento de desempeño", "Retribuciones diferidas", "Deducción de haberes", "RD 462/2002", "Comisión de servicio", "Dietas", "Residencia eventual", "Asistencias"])

# =============================================================================
T.ap("s0", "Mapa del tema: cinco preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque V, tema 6):
> El sistema de retribuciones de los funcionarios. Retribuciones básicas y retribuciones complementarias. Las indemnizaciones por razón del servicio.

### El hilo conductor

El epígrafe se lee como **cinco preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | TREBEP | Otras normas |
|---|---|---|---|
| **I** | ¿Cómo se ordena el sistema de retribuciones? | Arts. 21 y 22.1 y 5; disposición derogatoria única y disposición final cuarta | Ley 30/1984, arts. 23.1 y 24.2 |
| **II** | ¿Qué son las retribuciones básicas? | Arts. 22.2 y 4 y 23 | Ley 30/1984, arts. 23.2 y 24.1 |
| **III** | ¿Qué son las retribuciones complementarias? | Arts. 22.3 y 24 | Ley 30/1984, art. 23.3; RDL 6/2023, arts. 119.4 y 122.7 y disposición transitoria séptima |
| **IV** | ¿Qué reglas completan el sistema? | Arts. 25, 26, 27, 29 y 30 | — |
| **V** | ¿Qué son las indemnizaciones por razón del servicio? | Art. 28 | Ley 30/1984, art. 23.4; Real Decreto 462/2002; Resolución de 20 de enero de 2014 (anexo II) |

!> **La idea que une los cinco bloques:** el funcionario cobra **retribuciones básicas** (por el **grupo** de su cuerpo y su **antigüedad**: sueldo y trienios) y **complementarias** (por el **puesto**, la **carrera** y el **desempeño**), con cuantías que fija la **ley de presupuestos**. Aparte, **no como retribución** sino como resarcimiento, percibe **indemnizaciones por razón del servicio** (comisiones, desplazamientos, traslados y asistencias), reguladas en la AGE por el **Real Decreto 462/2002**.

?> **Aviso: dos leyes vigentes a la vez.** El TREBEP (arts. 21 a 30) y la **Ley 30/1984** (arts. 23 y 24) regulan las retribuciones con palabras distintas, y el examen de 2025 preguntó **por las dos** (→ Cierre 1). La razón está en la disposición final cuarta del TREBEP (→ I.3). Fíjate siempre en **qué norma** cita el enunciado.

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- No se incluyen las cuantías anuales del sueldo y los trienios: dependen de la ley de presupuestos de cada ejercicio. Sí se copian las cuantías de las dietas que figuran en el anexo II del Real Decreto 462/2002 (→ V.3).
- Fuera de este tema: la carrera profesional y el grado personal (tema V.4), las situaciones administrativas (tema V.5), la negociación colectiva de las retribuciones (tema V.8) y la nómina y su gestión presupuestaria (bloque VI).
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Cómo se ordena el sistema de retribuciones?", donde(
  "Primera pregunta del tema. Antes de ver cada concepto retributivo, hay que saber **quién fija las cuantías**, **en qué dos clases** se dividen las retribuciones y **qué norma** se aplica en la Administración del Estado.",
  ["1 Cuantías e incrementos: la ley de presupuestos (art. 21)", "2 Básicas y complementarias; lo que nunca se puede cobrar (art. 22.1 y 5)", "3 TREBEP y Ley 30/1984: por qué conviven"]))

T.ap("s1", "I.1 Cuantías e incrementos: la ley de presupuestos (TREBEP, art. 21; Ley 30/1984, art. 24.2)", f"""
Las retribuciones de los funcionarios no se pactan individualmente: sus cuantías y sus incrementos se fijan **por ley**, cada año.

{unidad("1.1 Determinación de las cuantías y de los incrementos (TREBEP, art. 21)",
  lit("TREBEP", "Artículo 21", ["deberán reflejarse para cada ejercicio presupuestario en la correspondiente ley de presupuestos", "superior a los límites fijados anualmente en la Ley de Presupuestos Generales del Estado"]),
  fichab("Reserva a la ley de presupuestos de las cuantías y de los incrementos retributivos",
         "Las Cortes (Ley de Presupuestos Generales del Estado) y, en lo suyo, los parlamentos que aprueban la «correspondiente ley de presupuestos»",
         ["::Qué se refleja en la ley de presupuestos cada ejercicio (21.1):", "Las **cuantías** de las retribuciones **básicas**", "El **incremento de las cuantías globales** de las **complementarias**", "El **incremento de la masa salarial** del personal **laboral**"],
         f"Límite (21.2): no cabe un incremento de la masa salarial {c('TREBEP', 'Artículo 21', 'superior a los límites fijados anualmente en la Ley de Presupuestos Generales del Estado para el personal')}",
         "De las básicas, la ley fija las **cuantías**; de las complementarias, el **incremento de las cuantías globales**. El límite del 21.2 lo fija la **LPGE**, aunque se negocie en otra Administración."))}

{unidad("1.2 Cuantías en los Presupuestos (Ley 30/1984, art. 24.2)",
  lit("L30", "aveinticuatro", ["deberá reflejarse para cada ejercicio presupuestario en la correspondiente Ley de Presupuestos Generales del Estado"], solo=[3]),
  fichab("Reflejo presupuestario de las cuantías de los conceptos retributivos (texto de 1984)",
         "Las Cortes (LPGE) y las demás Administraciones en sus Presupuestos",
         "Básicas, complementos de destino, específicos y de productividad: en la LPGE y en los Presupuestos de las demás Administraciones",
         "Para cada ejercicio presupuestario",
         "Misma idea que el art. 21.1 TREBEP, pero la Ley 30/1984 enumera los **complementos** uno por uno."))}
""", 2)

T.ap("s2", "I.2 Básicas y complementarias; lo que nunca se puede cobrar (TREBEP, art. 22.1 y 5; Ley 30/1984, art. 23.1)", f"""
{unidad("2.1 Las dos clases de retribuciones (TREBEP, art. 22.1; Ley 30/1984, art. 23.1)",
  lit("TREBEP", "Artículo 22", ["se clasifican en básicas y complementarias"], solo=[1]),
  lit("L30", "aveintitres", ["son básicas y complementarias"], solo=[1]),
  fichab("Clasificación de las retribuciones de los funcionarios de carrera",
         "Funcionarios **de carrera** (los interinos y los funcionarios en prácticas tienen reglas propias → IV.1)",
         ["Retribuciones **básicas** (→ II.1)", "Retribuciones **complementarias** (→ III.1)"],
         "—",
         "Solo **dos** clases. Las **pagas extraordinarias** no son una tercera clase en el TREBEP (art. 22.4 → II.2); en la Ley 30/1984 figuran **entre las básicas** (art. 23.2 c → II.3). Las **indemnizaciones** no son retribución (→ V.1)."))}

{unidad("2.2 Prohibición de participar en tributos, ingresos o multas (TREBEP, art. 22.5)",
  lit("TREBEP", "Artículo 22", ["participación en tributos o en cualquier otro ingreso de las Administraciones Públicas", "participación o premio en multas impuestas", "aun cuando estuviesen normativamente atribuidas a los servicios"], solo=[5]),
  fichab("Prohibición de percepciones ligadas a ingresos públicos o a multas",
         "Todo funcionario",
         ["No puede percibir **participación en tributos** ni en **cualquier otro ingreso** de las Administraciones como contraprestación de un servicio", "Tampoco **participación o premio en multas** impuestas"],
         "—",
         f"La prohibición rige {c('TREBEP', 'Artículo 22', 'aun cuando estuviesen normativamente atribuidas a los servicios')}."))}
""", 2)

T.ap("s3", "I.3 TREBEP y Ley 30/1984: por qué conviven (disposición derogatoria única y disposición final cuarta)", f"""
{unidad("3.1 La Ley 30/1984: derogación con alcance limitado (TREBEP, disposición derogatoria única, letra b)",
  lit("TREBEP", "ddunica-2", ["con el alcance establecido en el apartado 2 de la disposición final cuarta", "23; 24"], solo=[1, 3], titulo="Disposición derogatoria única (TREBEP), párrafo inicial y letra b)"),
  fichab("Por qué los arts. 23 y 24 de la Ley 30/1984 siguen en el texto consolidado",
         "—",
         f"Los arts. 23 y 24 de la Ley 30/1984 figuran entre los derogados, pero {c('TREBEP', 'ddunica-2', 'con el alcance establecido en el apartado 2 de la disposición final cuarta')}: rigen mientras no se dicten las leyes de Función Pública y no se opongan al Estatuto",
         "—",
         "El texto consolidado del BOE de la Ley 30/1984 mantiene sus arts. 23 y 24, y el examen de 2025 preguntó por ellos (→ Cierre 1). Si el enunciado cita la **Ley 30/1984**, responde con su letra (→ II.3 y → III.2)."))}

{unidad("3.2 Efectos diferidos del capítulo de derechos retributivos (TREBEP, disposición final cuarta)",
  lit("TREBEP", "dfcuaa", ["Lo establecido en los capítulos II y III del título III, excepto el artículo 25.2", "producirá efectos a partir de la entrada en vigor de las leyes de Función Pública que se dicten en desarrollo de este Estatuto", "se mantendrán en vigor en cada Administración Pública las normas vigentes sobre ordenación, planificación y gestión de recursos humanos"], solo=[1, 3]),
  fichab("Entrada en vigor diferida de los derechos retributivos del TREBEP",
         "Cada Administración, con sus leyes de Función Pública de desarrollo",
         ["El **capítulo III del título III** (derechos retributivos: arts. 21 a 30), **salvo el art. 25.2**, produce efectos cuando entren en vigor las leyes de Función Pública de desarrollo (apartado 1)", "Hasta entonces se mantienen las normas vigentes en cada Administración, si no se oponen al Estatuto (apartado 2)"],
         "—",
         "La excepción es el **art. 25.2** (trienios de los interinos por servicios anteriores → IV.1). El capítulo II (carrera) también tiene efectos diferidos (tema V.4)."))}

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| | TREBEP (arts. 22 a 24) | Ley 30/1984 (arts. 23 y 24) |
|---|---|---|
| Clases | Básicas y complementarias | Básicas y complementarias |
| Básicas | Sueldo y trienios | Sueldo, trienios y **pagas extraordinarias** |
| Pagas extraordinarias | Dos al año: una mensualidad de básicas y de la totalidad de las complementarias (salvo productividad y servicios extraordinarios) | Dos al año, importe mínimo de una mensualidad de sueldo y trienios; **junio y diciembre** |
| Complementarias | **Factores** (carrera, puesto, desempeño, servicios extraordinarios); estructura y cuantía, por ley de cada Administración | **Conceptos** cerrados: destino, específico, productividad y gratificaciones |

{resumen([
  "Cuantías de las **básicas** e incremento **global** de las **complementarias**: en la **ley de presupuestos** de cada ejercicio; ningún incremento por encima del límite de la **LPGE** (art. 21).",
  "Dos clases: **básicas** y **complementarias** (art. 22.1); prohibida la participación en **tributos, ingresos o multas** (22.5).",
  "Los derechos retributivos del TREBEP tienen **efectos diferidos** (salvo el **25.2**); la **Ley 30/1984** (arts. 23 y 24) se mantiene con ese alcance."],
  "Siguiente: II. ¿Qué son las retribuciones básicas?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Qué son las retribuciones básicas?", donde(
  "Segunda pregunta. Las retribuciones básicas dependen del **grupo o subgrupo** del cuerpo o escala y de la **antigüedad**: sueldo y trienios. Con ellas se estudian las **pagas extraordinarias**.",
  ["1 Sueldo y trienios (TREBEP, arts. 22.2 y 23)", "2 Pagas extraordinarias (TREBEP, art. 22.4)", "3 La versión de la Ley 30/1984 (arts. 23.2 y 24.1)"]))

T.ap("s4", "II.1 Sueldo y trienios (TREBEP, arts. 22.2 y 23)", f"""
{unidad("1.1 Qué retribuyen las básicas (art. 22.2)",
  lit("TREBEP", "Artículo 22", ["según la adscripción de su cuerpo o escala a un determinado Subgrupo o Grupo de clasificación profesional", "por su antigüedad en el mismo", "los componentes de sueldo y trienios de las pagas extraordinarias"], solo=[2]),
  fichab("Concepto de retribuciones básicas",
         "Funcionarios de carrera",
         ["Retribuyen según el **Subgrupo** (o Grupo, si no tiene Subgrupo) del cuerpo o escala", "Y según la **antigüedad** en él", "Incluyen los componentes de **sueldo y trienios** de las pagas extraordinarias"],
         "—",
         "Las básicas miran al **cuerpo o escala** (no al puesto) y a la **antigüedad**. Lo que retribuye el **puesto** es complementario (→ III.1)."))}

{unidad("1.2 Sueldo y trienios, «única y exclusivamente» (art. 23)",
  lit("TREBEP", "Artículo 23", ["que se fijan en la Ley de Presupuestos Generales del Estado", "única y exclusivamente", "El sueldo asignado a cada Subgrupo o Grupo de clasificación profesional", "por cada tres años de servicio"]),
  fichab("Composición de las retribuciones básicas",
         "Las fija la **Ley de Presupuestos Generales del Estado**",
         ["**Sueldo**: el asignado a cada **Subgrupo** (o Grupo sin Subgrupo)", f"**Trienios**: {c('TREBEP', 'Artículo 23', 'una cantidad, que será igual para cada Subgrupo o Grupo de clasificación profesional')}, {c('TREBEP', 'Artículo 23', 'por cada tres años de servicio')}"],
         "Trienio: cada **tres** años de servicio",
         "Solo sueldo y trienios («**única y exclusivamente**»): ni el complemento de destino ni el específico son básicos. Cayó en 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s5", "II.2 Las pagas extraordinarias (TREBEP, art. 22.4)", f"""
{unidad("2.1 Dos al año: qué incluyen (art. 22.4)",
  lit("TREBEP", "Artículo 22", ["serán dos al año", "una mensualidad de retribuciones básicas y de la totalidad de las retribuciones complementarias", "salvo aquéllas a las que se refieren los apartados c) y d) del artículo 24"], solo=[4]),
  fichab("Pagas extraordinarias en el TREBEP",
         "Funcionarios",
         ["::Cada paga:", "Una mensualidad de retribuciones **básicas**", "Más la **totalidad** de las **complementarias**", "Salvo las del art. 24 **c)** (interés, iniciativa, esfuerzo y rendimiento) y **d)** (servicios extraordinarios) (→ III.1)"],
         "**Dos** al año",
         "En el TREBEP las pagas llevan las complementarias **salvo** las de rendimiento y las de servicios extraordinarios. La Ley 30/1984 da otra fórmula (→ II.3)."))}
""", 2)

T.ap("s6", "II.3 La versión de la Ley 30/1984 (arts. 23.2 y 24.1)", f"""
{unidad("3.1 Sueldo, trienios y pagas extraordinarias (Ley 30/1984, art. 23.2)",
  lit("L30", "aveintitres", ["índice de proporcionalidad asignado a cada uno de los grupos", "una cantidad igual para cada grupo, por cada tres años de servicio", "tendrá derecho a seguir percibiendo los trienios devengados en los grupos anteriores", "se considerará como tiempo de servicios prestados en el nuevo grupo", "se devengarán los meses de junio y diciembre"], solo=[2, 3, 4, 5, 6, 7]),
  fichab("Retribuciones básicas según la Ley 30/1984",
         "Funcionarios del ámbito de la Ley 30/1984",
         ["**Sueldo**: el índice de proporcionalidad de cada **grupo**", "**Trienios**: cantidad igual para cada grupo por cada **tres años** en el Cuerpo o Escala; se conservan los devengados en grupos anteriores; la fracción de trienio se computa en el nuevo grupo", f"**Pagas extraordinarias**: dos al año, {c('L30', 'aveintitres', 'por un importe mínimo cada una de ellas de una mensualidad del sueldo y trienios')}"],
         "Pagas: en **junio y diciembre**",
         "En la Ley 30/1984 las pagas extraordinarias son **retribución básica** (art. 23.2 c). Los trienios de otro grupo **se mantienen**; la fracción de trienio **no se pierde**."))}

{unidad("3.2 Cuantías iguales en todas las Administraciones (Ley 30/1984, art. 24.1)",
  lit("L30", "aveinticuatro", ["serán iguales en todas las Administraciones públicas, para cada uno de los grupos en que se clasifican los cuerpos, escalas, categorías o clases de funcionarios", "según el nivel del complemento de destino que se perciba", "no podrá exceder en más de tres veces"], solo=[1, 2]),
  fichab("Igualdad de las básicas en todas las Administraciones",
         "Todas las Administraciones públicas",
         ["Sueldo y trienios: **iguales en todas las Administraciones** para cada grupo", "Pagas extraordinarias: iguales para cada grupo **según el nivel del complemento de destino** que se perciba", "Tope: el sueldo del grupo A no puede exceder en **más de tres veces** el del grupo E"],
         "—",
         "Pregunta de 2025 (→ Cierre 1): «según el nivel del complemento de destino» se refiere a las **pagas extraordinarias**, no a sueldo y trienios. El «índice de proporcionalidad» es del **sueldo** (art. 23.2 a), no de los trienios."))}

{resumen([
  "Básicas: según el **Subgrupo** del cuerpo o escala y la **antigüedad**; **única y exclusivamente** sueldo y trienios (TREBEP, arts. 22.2 y 23).",
  "Trienio: cantidad **igual para cada Subgrupo** por cada **tres años** de servicio.",
  "Pagas extraordinarias: **dos al año**; en el TREBEP, mensualidad de básicas y de **todas las complementarias salvo 24 c) y d)**; en la Ley 30/1984, mínimo una mensualidad de **sueldo y trienios**, en **junio y diciembre**.",
  "Ley 30/1984: sueldo y trienios **iguales en todas las Administraciones**; sueldo del A, como máximo **tres veces** el del E."],
  "Siguiente: III. ¿Qué son las retribuciones complementarias?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Qué son las retribuciones complementarias?", donde(
  "Tercera pregunta. Las complementarias retribuyen lo que no depende del cuerpo: el **puesto**, la **carrera** y el **desempeño**. El TREBEP da los **factores**; la Ley 30/1984, los **complementos** concretos; el RDL 6/2023 añade, para la Administración del Estado, los complementos de **desempeño** y de **carrera**.",
  ["1 Los factores del TREBEP (arts. 22.3 y 24)", "2 Los cuatro conceptos de la Ley 30/1984 (art. 23.3)", "3 Administración del Estado: complemento de desempeño y complemento de carrera (RDL 6/2023)"]))

T.ap("s7", "III.1 Los factores del TREBEP (arts. 22.3 y 24)", f"""
{unidad("1.1 Qué retribuyen las complementarias (art. 22.3)",
  lit("TREBEP", "Artículo 22", ["las características de los puestos de trabajo, la carrera profesional o el desempeño, rendimiento o resultados alcanzados por el funcionario"], solo=[3]),
  fichab("Concepto de retribuciones complementarias",
         "Funcionarios de carrera",
         ["Las características de los **puestos** de trabajo", "La **carrera** profesional", "El **desempeño, rendimiento o resultados** alcanzados"],
         "—",
         "Puesto, carrera y desempeño: **complementarias**. Grupo y antigüedad: **básicas** (→ II.1)."))}

{unidad("1.2 Cuantía y estructura por ley de cada Administración; factores (art. 24)",
  lit("TREBEP", "Artículo 24", ["se establecerán por las correspondientes leyes de cada Administración Pública", "entre otros", "La progresión alcanzada por el funcionario dentro del sistema de carrera administrativa", "La especial dificultad técnica, responsabilidad, dedicación, incompatibilidad", "El grado de interés, iniciativa o esfuerzo", "Los servicios extraordinarios prestados fuera de la jornada normal de trabajo"]),
  fichab("Factores para fijar las retribuciones complementarias",
         "Las **leyes de cada Administración Pública** fijan cuantía y estructura",
         ["a) **Progresión** en la carrera administrativa", "b) Especial **dificultad técnica, responsabilidad, dedicación, incompatibilidad** del puesto o condiciones del trabajo", "c) **Interés, iniciativa o esfuerzo** y **rendimiento** o resultados", "d) **Servicios extraordinarios** fuera de la jornada normal"],
         "—",
         "La lista es abierta («**entre otros**»). Las letras **c)** y **d)** quedan fuera de las pagas extraordinarias (→ II.2). No es el TREBEP quien fija la cuantía, sino la **ley de cada Administración**."))}
""", 2)

T.ap("s8", "III.2 Los cuatro conceptos de la Ley 30/1984 (art. 23.3)", f"""
{unidad("2.1 Destino, específico, productividad y gratificaciones (Ley 30/1984, art. 23.3)",
  lit("L30", "aveintitres", ["correspondiente al nivel del puesto que se desempeñe", "destinado a retribuir las condiciones particulares de algunos puestos de trabajo", "En ningún caso podrá asignarse más de un complemento específico a cada puesto de trabajo", "el especial rendimiento, la actividad extraordinaria y el interés o iniciativa", "serán de conocimiento público", "en ningún caso podrán ser fijas en su cuantía y periódicas en su devengo"], solo=list(range(8, 15))),
  fichab("Las retribuciones complementarias según la Ley 30/1984",
         ["::Quién fija la productividad individual:", f"{c('L30', 'aveintitres', 'El responsable de la gestión de cada programa de gasto')}, dentro de las dotaciones y de la Ley de Presupuestos"],
         ["a) **Complemento de destino**: según el **nivel del puesto** que se desempeñe", "b) **Complemento específico**: condiciones particulares de algunos puestos (especial dificultad técnica, dedicación, responsabilidad, incompatibilidad, **peligrosidad o penosidad**); solo **uno** por puesto", "c) **Complemento de productividad**: especial rendimiento, actividad extraordinaria e interés o iniciativa; cuantías individuales **de conocimiento público**", "d) **Gratificaciones** por servicios extraordinarios fuera de la jornada normal"],
         f"Productividad: cuantía global con el límite de {c('L30', 'aveintitres', 'un porcentaje sobre los costes totales de personal de cada programa y de cada órgano que se determinará en la Ley de Presupuestos')}",
         "Pregunta de 2025 (→ Cierre 1): dificultad técnica, dedicación, responsabilidad, incompatibilidad, **peligrosidad o penosidad** = **específico**. Las gratificaciones **nunca** pueden ser **fijas y periódicas**. Los niveles de puesto y el grado personal se estudian en el tema V.4."))}
""", 2)

T.ap("s9", "III.3 Administración del Estado: complemento de desempeño y complemento de carrera (RDL 6/2023)", f"""
El libro segundo del Real Decreto-ley 6/2023 regula la función pública de la Administración del Estado. En retribuciones complementarias añade dos complementos.

{unidad("3.1 Complemento de desempeño (RDL 6/2023, art. 119.4)",
  lit("RDL6", "a1-31", ["de acuerdo con el artículo 24.c) del texto refundido de la Ley del Estatuto Básico del Empleado Público", "el complemento de desempeño es el que retribuye el rendimiento o resultados obtenidos por el personal funcionario", "serán de conocimiento del resto del personal de su ámbito"], solo=[10, 11, 12], titulo="Artículo 119.4 (RDL 6/2023, libro segundo). Efectos de la evaluación del desempeño"),
  fichab("Complemento que retribuye el rendimiento en la Administración del Estado",
         "Personal funcionario del ámbito del libro segundo; para el personal laboral, convenios y normativa específica",
         "Retribuye el **rendimiento o resultados** obtenidos, según la **evaluación del desempeño**; desarrolla el **art. 24 c)** del TREBEP",
         "—",
         "Las cantidades son **de conocimiento** del resto del personal de su ámbito y de los representantes sindicales (como la productividad en la Ley 30/1984 → III.2)."))}

{unidad("3.2 Hasta que se implante la evaluación: productividad (RDL 6/2023, disposición transitoria séptima)",
  lit("RDL6", "dt-7", ["Hasta tanto se implemente la evaluación del desempeño", "con arreglo a los mismos modelos, criterios o baremos", "sustituirá a todos los efectos al complemento de productividad"], titulo="Disposición transitoria séptima (RDL 6/2023). Régimen transitorio de retribuciones"),
  fichab("Transición del complemento de productividad al de desempeño",
         "Administración del Estado",
         ["Mientras no se implante la evaluación del desempeño: el complemento de desempeño se rige por los **modelos, criterios o baremos** autorizados para el **complemento de productividad**", "Implantada la evaluación: el de desempeño **sustituye** a todos los efectos al de **productividad**"],
         "—",
         "La sustitución se produce **una vez se implemente** la evaluación del desempeño, no a la entrada en vigor del RDL."))}

{unidad("3.3 Complemento de carrera (RDL 6/2023, art. 122.7)",
  lit("RDL6", "a1-34", ["se retribuirá mediante un complemento de carrera", "será la misma para todo el personal funcionario del mismo grupo o subgrupo de clasificación profesional que tenga reconocido el mismo tramo"], solo=[17], titulo="Artículo 122.7 (RDL 6/2023, libro segundo). Carrera horizontal"),
  fichab("Complemento que retribuye la carrera horizontal en la Administración del Estado",
         "Personal funcionario de carrera de la Administración del Estado",
         "Retribuye la **progresión** en la carrera horizontal (factor del **art. 24 a)** del TREBEP); los tramos se estudian en el tema V.4",
         "—",
         "Cuantía **igual** para el mismo **grupo o subgrupo** y el mismo **tramo**."))}

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Factor del TREBEP (art. 24) | Ley 30/1984 (art. 23.3) | RDL 6/2023 (Administración del Estado) |
|---|---|---|
| a) Progresión en la carrera | — | Complemento de **carrera** (art. 122.7) |
| b) Características del puesto | Complemento de **destino** (nivel) y **específico** | — |
| c) Interés, iniciativa, esfuerzo, rendimiento | Complemento de **productividad** | Complemento de **desempeño** (art. 119.4; disposición transitoria séptima) |
| d) Servicios extraordinarios | **Gratificaciones** | — |

{resumen([
  "Complementarias: **puesto, carrera y desempeño** (TREBEP, art. 22.3); cuantía y estructura por **ley de cada Administración**, con factores **abiertos** (art. 24).",
  "Ley 30/1984: **destino** (nivel del puesto), **específico** (uno por puesto; peligrosidad o penosidad), **productividad** (pública) y **gratificaciones** (nunca fijas y periódicas).",
  "Administración del Estado: complemento de **desempeño**, que sustituirá a la **productividad** cuando se implante la evaluación, y complemento de **carrera** por tramos."],
  "Siguiente: IV. ¿Qué reglas completan el sistema?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Qué reglas completan el sistema? (TREBEP, arts. 25 a 27, 29 y 30)", donde(
  "Cuarta pregunta. Lo visto se refiere a los funcionarios **de carrera**. El TREBEP completa el sistema con lo que cobran los **interinos**, los funcionarios **en prácticas** y el personal **laboral**, con las **retribuciones diferidas** y con la **deducción** de haberes.",
  ["1 Interinos, funcionarios en prácticas y personal laboral (arts. 25 a 27)", "2 Retribuciones diferidas y deducción de retribuciones (arts. 29 y 30)"]))

T.ap("s10", "IV.1 Interinos, funcionarios en prácticas y personal laboral (TREBEP, arts. 25 a 27)", f"""
{unidad("1.1 Funcionarios interinos (art. 25)",
  lit("TREBEP", "Artículo 25", ["las retribuciones básicas y las pagas extraordinarias", "las retribuciones complementarias a que se refieren los apartados b), c) y d) del artículo 24", "categoría de entrada", "tendrán efectos retributivos únicamente a partir de la entrada en vigor del mismo"]),
  ficha("Funcionarios **interinos**",
        ["Retribuciones **básicas** y **pagas extraordinarias** de su Subgrupo o Grupo", "Complementarias del art. 24 **b), c) y d)** (puesto, rendimiento y servicios extraordinarios)", "Las correspondientes a la **categoría de entrada** del cuerpo o escala", "**Trienios** por servicios prestados antes de la entrada en vigor del Estatuto (25.2)"],
        "No perciben las del art. 24 **a)** (progresión en la carrera); los trienios del 25.2 solo tienen efectos retributivos **desde la entrada en vigor** del Estatuto",
        "—",
        "El **art. 25.2** es la única regla de este capítulo que **no** tiene efectos diferidos (disposición final cuarta → I.3.2)."))}

{unidad("1.2 Funcionarios en prácticas (art. 26)",
  lit("TREBEP", "Artículo 26", ["como mínimo", "a las del sueldo del Subgrupo o Grupo"]),
  ficha("Funcionarios **en prácticas**",
        f"Las retribuciones que determine cada Administración, que {c('TREBEP', 'Artículo 26', 'como mínimo, se corresponderán a las del sueldo del Subgrupo o Grupo')} en que aspiren a ingresar",
        "Mínimo: el **sueldo** del Subgrupo **al que aspiran** a ingresar",
        "—",
        "Pregunta de 2025 (→ Cierre 1): el mínimo es **solo el sueldo**; no incluye complemento de destino, específico ni gratificaciones. Es el Subgrupo **al que aspiran**, no el de origen."))}

{unidad("1.3 Personal laboral (art. 27)",
  lit("TREBEP", "Artículo 27", ["la legislación laboral, el convenio colectivo que sea aplicable y el contrato de trabajo", "respetando en todo caso lo establecido en el artículo 21"]),
  ficha("Personal **laboral**",
        ["Legislación **laboral**", "**Convenio colectivo** aplicable", "**Contrato** de trabajo"],
        "Siempre respetando el **art. 21** (límites de la ley de presupuestos → I.1.1)",
        "—",
        "Al laboral no se le aplican las básicas/complementarias de los arts. 22 a 24; sí el **límite de la masa salarial** del art. 21. El convenio de la AGE se estudia en el tema V.7."))}
""", 2)

T.ap("s11", "IV.2 Retribuciones diferidas y deducción de retribuciones (TREBEP, arts. 29 y 30)", f"""
{unidad("2.1 Retribuciones diferidas: planes de pensiones y seguros colectivos (art. 29)",
  lit("TREBEP", "Artículo 29", ["hasta el porcentaje de la masa salarial que se fije en las correspondientes Leyes de Presupuestos Generales del Estado", "planes de pensiones de empleo o contratos de seguro colectivos", "la consideración de retribución diferida"]),
  fichab("Aportaciones a planes de pensiones de empleo o seguros colectivos",
         "Las Administraciones Públicas, para el personal incluido en sus ámbitos",
         ["Financian aportaciones a **planes de pensiones de empleo** o **contratos de seguro colectivos** con cobertura de **jubilación**", f"Esas cantidades {c('TREBEP', 'Artículo 29', 'tendrán a todos los efectos la consideración de retribución diferida')}"],
         "Límite: el **porcentaje de la masa salarial** que fije la **LPGE**",
         "Pregunta de 2025 (→ Cierre 1): se llaman **retribuciones diferidas**; no son básicas, ni complementarias, ni indemnizaciones."))}

{unidad("2.2 Deducción de retribuciones (art. 30)",
  lit("TREBEP", "Artículo 30", ["Sin perjuicio de la sanción disciplinaria que pueda corresponder", "que no tendrá carácter sancionador", "no devengarán ni percibirán las retribuciones correspondientes al tiempo en que hayan permanecido en esa situación", "ni afecte al régimen respectivo de sus prestaciones sociales"]),
  ficha("Todo el personal incluido en el ámbito del Estatuto",
        ["Jornada no realizada → **deducción proporcional** de haberes (30.1)", "Huelga → no se devengan ni perciben las retribuciones del tiempo en huelga (30.2)"],
        ["La deducción **no tiene carácter sancionador**", "Por huelga, la deducción **no afecta** al régimen de **prestaciones sociales**"],
        "Compatible con la **sanción disciplinaria** que pueda corresponder (régimen disciplinario: tema V.2)",
        "Pregunta de 2025 (→ Cierre 1): la deducción **no** es sanción, pero **no excluye** la sanción disciplinaria. El derecho de huelga se estudia en el tema V.8."))}

{resumen([
  "**Interinos**: básicas, pagas extraordinarias y complementarias del 24 **b), c) y d)** (no la de carrera); trienios por servicios previos (25.2, con efectos inmediatos).",
  "**En prácticas**: como mínimo, el **sueldo** del Subgrupo al que **aspiran** a ingresar (26). **Laborales**: legislación laboral, convenio y contrato, respetando el **art. 21** (27).",
  "**Retribución diferida**: aportaciones a **planes de pensiones** o **seguros colectivos**, hasta el porcentaje de la masa salarial que fije la LPGE (29).",
  "**Deducción** proporcional por jornada no realizada, **sin carácter sancionador**; en huelga, sin afectar a las prestaciones sociales (30)."],
  "Siguiente: V. ¿Qué son las indemnizaciones por razón del servicio?")}
""", 2)

# =============================================================================
T.ap("bV", "V. ¿Qué son las indemnizaciones por razón del servicio? (TREBEP, art. 28; Real Decreto 462/2002)", donde(
  "Quinta pregunta. Las indemnizaciones **no retribuyen** el trabajo: **resarcen** los gastos que el servicio ocasiona. El TREBEP y la Ley 30/1984 las reconocen; el **Real Decreto 462/2002** las regula en la Administración General del Estado.",
  ["1 El derecho, los supuestos y el ámbito (TREBEP, art. 28; Ley 30/1984, art. 23.4; RD 462/2002, arts. 1 y 2)", "2 Comisiones de servicio (arts. 3 a 7)", "3 Dietas, residencia eventual y gastos de viaje (arts. 9, 10, 12, 16 y 17 y anexos I y II)", "4 Desplazamientos en el término municipal y traslados de residencia (arts. 20, 22 y 23)", "5 Asistencias (arts. 27, 30, 32 y 33)", "6 Imputación presupuestaria (disposición final primera; Resolución de 20 de enero de 2014)"]))

T.ap("s12", "V.1 El derecho, los supuestos y el ámbito (TREBEP, art. 28; Ley 30/1984, art. 23.4; RD 462/2002, arts. 1 y 2)", f"""
{unidad("1.1 El derecho a las indemnizaciones (TREBEP, art. 28; Ley 30/1984, art. 23.4)",
  lit("TREBEP", "Artículo 28", ["las indemnizaciones correspondientes por razón del servicio"]),
  lit("L30", "aveintitres", ["las indemnizaciones correspondientes por razón del servicio"], solo=[15], titulo="Artículo veintitrés, apartado 4 (Ley 30/1984)"),
  ficha("Los funcionarios",
        "Percibir las **indemnizaciones** correspondientes **por razón del servicio**",
        "En las circunstancias, condiciones y límites del reglamento (en la AGE, el RD 462/2002 → V.1.2)",
        "—",
        "Están fuera de la clasificación básicas/complementarias: el TREBEP las regula en un **artículo propio** (28) y la Ley 30/1984 en un **apartado distinto** (23.4)."))}

{unidad("1.2 Qué da lugar a indemnización y nulidad de lo que no se ajuste (RD 462/2002, art. 1)",
  lit("RD462", "Artículo 1", ["Comisiones de servicio con derecho a indemnización", "Desplazamientos dentro del término municipal por razón de servicio", "Traslados de residencia", "Asistencias por concurrencia a Consejos de Administración u Órganos Colegiados", "se considerará nula"]),
  fichab("Supuestos que dan origen a indemnización o compensación",
         "Personal del ámbito del art. 2 (→ V.1.3)",
         ["a) **Comisiones de servicio** con derecho a indemnización (→ V.2)", "b) **Desplazamientos dentro del término municipal** por razón de servicio (→ V.4)", "c) **Traslados de residencia** (→ V.4)", "d) **Asistencias**: consejos de administración u órganos colegiados, tribunales de oposiciones y concursos, colaboración en centros de formación (→ V.5)"],
         "—",
         f"Lista **cerrada** de cuatro supuestos. Lo que no se ajuste al Real Decreto {c('RD462', 'Artículo 1', 'se considerará nula, no pudiendo surtir efectos en las cajas pagadoras')}. Pregunta de 2025: la **redistribución de efectivos** no está en la lista (→ Cierre 1)."))}

{unidad("1.3 A quién se aplica (RD 462/2002, art. 2)",
  lit("RD462", "Artículo 2", ["El personal, civil y militar", "carácter permanente, interino, temporal o en prácticas, excepto el de carácter laboral", "el personal no vinculado jurídicamente con la Administración"], solo=[1, 2, 3, 4, 5, 6, 7, 8]),
  fichab("Ámbito subjetivo del Real Decreto 462/2002",
         ["Personal civil y militar de la **AGE** y sus organismos públicos", "Personal al servicio de la **Seguridad Social**", "Carreras Judicial y Fiscal y Administración de Justicia, y Corporaciones locales: **según su legislación específica**", "Personal de la **UNED**"],
         ["Incluye al personal **permanente, interino, temporal o en prácticas**", "**Excluye** al **laboral**, que se rige por su convenio colectivo o normativa específica", "Incluye al personal **no vinculado** jurídicamente que preste servicios que den lugar a indemnización"],
         "—",
         "El **laboral** queda fuera (convenio colectivo). El Real Decreto tiene **carácter supletorio** para el personal no incluido (disposición adicional primera)."))}
""", 2)

T.ap("s13", "V.2 Comisiones de servicio (RD 462/2002, arts. 3 a 7)", f"""
{unidad("2.1 Qué es una comisión de servicio con derecho a indemnización (art. 3)",
  lit("RD462", "Artículo 3", ["los cometidos especiales que circunstancialmente se ordenen", "fuera del término municipal donde radique su residencia oficial", "en ningún caso, podrá tener la consideración de comisión de servicio el desplazamiento habitual", "a iniciativa propia"], solo=[1, 2, 5]),
  fichab("Comisión de servicio con derecho a indemnización",
         "El personal del art. 2, por orden de la Administración",
         ["**Cometidos especiales** ordenados **circunstancialmente**", "Desempeñados **fuera del término municipal** de la **residencia oficial** (el de la oficina del puesto habitual)"],
         "—",
         "No son comisión: el **desplazamiento habitual** desde donde se está autorizado a residir hasta el centro de trabajo, ni las comisiones **a iniciativa propia** (salvo decisiones obligadas por la función de **alto cargo**) o con **renuncia expresa**."))}

{unidad("2.2 Quién designa la comisión (art. 4.1 y 3)",
  lit("RD462", "Artículo 4", ["compete al Subsecretario de cada Departamento ministerial o a la autoridad superior del Organismo o Entidad correspondiente", "se hará constar que actúan en comisión de servicio"], solo=[1, 8]),
  fichab("Designación de las comisiones de servicio",
         "El **Subsecretario** de cada Departamento o la **autoridad superior** del organismo o entidad (en Defensa, además, los Jefes de Estado Mayor)",
         "Orden (personal civil) o pasaporte (militar) que hace constar la comisión, si da derecho a dietas o a residencia eventual, el viaje por cuenta del Estado, el destino y el lugar, día y hora de inicio y fin",
         "—",
         "Designa el **Subsecretario**, no el Ministro ni el jefe de la unidad."))}

{unidad("2.3 Duración: un mes en España, tres en el extranjero (art. 5)",
  lit("RD462", "Artículo 5", ["salvo casos excepcionales, no durará más de un mes en territorio nacional y de tres en el extranjero", "concesión de prórroga por el tiempo estrictamente indispensable"]),
  fichab("Duración máxima de la comisión de servicio",
         "Propone la prórroga el **Jefe** correspondiente, razonadamente; la concede la autoridad competente",
         "Si el plazo resulta insuficiente, cabe **prórroga** por el tiempo **estrictamente indispensable**",
         f"{c('RD462', 'Artículo 5', 'no durará más de un mes en territorio nacional y de tres en el extranjero')}, **salvo casos excepcionales**",
         "Cayó **dos veces** en 2025 (→ Cierre 1): **un mes** en territorio nacional y **tres** en el extranjero, «salvo casos excepcionales» y **prorrogable** (no «improrrogable»)."))}

{unidad("2.4 Residencia eventual: más allá de esos límites (art. 6)",
  lit("RD462", "Artículo 6", ["tendrán la consideración de residencia eventual", "no podrá exceder de un año", "La duración de la prórroga no podrá en ningún caso exceder de un año", "se procederá a tramitar la creación del correspondiente puesto de trabajo"]),
  fichab("Comisiones con la consideración de residencia eventual",
         "Prorroga la autoridad que designó la comisión (art. 4.1)",
         ["Comisiones previstas **por encima** de los límites del art. 5, o prórrogas que los excedan: **residencia eventual** desde el comienzo", "Si desde el inicio se prevé **más de un año**: se tramita la **creación del puesto** de trabajo"],
         "Máximo **un año**, prorrogable por el tiempo estrictamente indispensable; la prórroga, **nunca más de un año**",
         "Un mes / tres meses → comisión con **dietas**; por encima → **residencia eventual** (máximo **un año** + prórroga de máximo **un año**)."))}

{unidad("2.5 Cursos convocados por la Administración (art. 7.1)",
  lit("RD462", "Artículo 7", ["contando con autorización expresa", "cualquiera que sea la duración de los mismos", "tendrán derecho a percibir el 50 por 100 de los gastos de manutención"], solo=[1, 2]),
  fichab("Indemnización por asistencia a cursos",
         "Personal que asiste, con **autorización expresa**, a cursos de capacitación, especialización, perfeccionamiento, ascenso o cursos selectivos de **promoción interna**",
         "Como comisión de servicio o como residencia eventual, según decida la **Orden de designación**; siempre que sean **fuera** del término municipal de la residencia oficial",
         "—",
         "Si vuelve a pernoctar a su residencia: sin indemnización, salvo el **50 por 100 de la manutención** si debe almorzar allí, y los gastos de viaje. Los cursos selectivos de **promoción interna** son siempre **residencia eventual** (art. 7.2)."))}
""", 2)

_D = {g: [cifra("RD462", "anii", v) for v in vs] for g, vs in
      {"Grupo 1": ["102,56", "53,34", "155,90"], "Grupo 2": ["65,97", "37,40", "103,37"], "Grupo 3": ["48,92", "28,21", "77,13"]}.items()}

T.ap("s14", "V.3 Dietas, residencia eventual y gastos de viaje (RD 462/2002, arts. 9, 10, 12, 16 y 17 y anexos I y II)", f"""
{unidad("3.1 Las clases de indemnización (art. 9)",
  lit("RD462", "Artículo 9", ["la cantidad que se devenga diariamente para satisfacer los gastos que origina la estancia fuera de la residencia oficial", "plus", "la cantidad que se abona por la utilización de cualquier medio de transporte por razón de servicio"]),
  fichab("Conceptos: dieta, plus, residencia eventual y gastos de viaje",
         "—",
         ["**Dieta**: cantidad **diaria** por la estancia fuera de la residencia oficial en las comisiones del **art. 5**", "**Plus**: la dieta del personal de las **Fuerzas Armadas** o **Fuerzas y Cuerpos de Seguridad** formando **unidad**", "**Indemnización de residencia eventual**: cantidad **diaria** en los casos de los **arts. 6 y 7**", "**Gastos de viaje**: por la utilización de cualquier medio de transporte"],
         "—",
         "Dieta ↔ comisión del art. 5; residencia eventual ↔ arts. 6 y 7. El «plus» es la dieta de quien va **formando unidad**."))}

{unidad("3.2 Cuantía de las dietas: grupos y anexos (art. 10.1 y 2)",
  lit("RD462", "Artículo 10", ["de acuerdo con los grupos que se especifican en el anexo I", "comprenden los gastos de manutención correspondientes a la comida y la cena", "duración superior a cuatro días", "por el importe exacto de las llamadas de teléfono de carácter oficial"], solo=[1, 2, 3, 4]),
  fichab("Dietas de alojamiento y manutención",
         "Según el **grupo** del anexo I: **1** (altos cargos, subdirectores generales y asimilados), **2** (entre otros, funcionarios de la Administración del Estado de cuerpos de los grupos **A y B**) y **3** (entre otros, los de los grupos **C, D y E**)",
         ["Cuantías: **anexo II** (territorio nacional) y **anexo III** (extranjero)", "Comprenden la **manutención** (comida y cena) y los **importes máximos** de alojamiento, desayuno y teléfono", "Alojamiento: lo **realmente gastado y justificado**, sin superar el anexo (art. 10.3)"],
         "Lavado y planchado: si la comisión dura **más de cuatro días** y lo autoriza quien la ordena",
         "Las llamadas **oficiales** se pagan por su **importe exacto**, cualquiera que sea la duración de la comisión."))}

*Cuantías del anexo II del Real Decreto 462/2002 (dietas en territorio nacional, en euros), copiadas del texto consolidado del BOE y comprobadas por programa; son las de la última redacción del anexo II que recoge el texto consolidado (BOE-A-2005-19988, publicada el 3-12-2005), vigente hoy:*

| Grupo (anexo I) | Por alojamiento | Por manutención | Dieta entera |
|---|---|---|---|
""" + "\n".join(f"| {g} | {a} | {m} | {e} |" for g, (a, m, e) in _D.items()) + f"""

{unidad("3.3 Cálculo de las dietas según la duración y la hora (art. 12.1 a 3)",
  lit("RD462", "Artículo 12", ["teniendo la comisión una duración mínima de cinco horas, ésta se inicie antes de las catorce horas y finalice después de las dieciséis horas", "gastos de alojamiento correspondiente a un solo día", "En el día de salida se podrán percibir gastos de alojamiento pero no gastos de manutención", "anterior a las veintidós horas", "En el día de regreso no se podrán percibir gastos de alojamiento ni de manutención", "dietas al 100 por 100"], solo=[1, 3, 4, 5, 6, 7]),
  fichab("Reglas de devengo de las dietas",
         "—",
         ["**Un día natural o menos**: en general, nada; **50 %** de la manutención si dura al menos **cinco horas**, empieza **antes de las 14** y acaba **después de las 16**", "**Hasta 24 horas en dos días naturales**: alojamiento de **un solo día** y manutención como en los días de salida y regreso", "**Más de 24 horas, día de salida**: alojamiento sí; manutención **100 %** si se sale **antes de las 14**, **50 %** si entre las **14 y las 22**", "**Día de regreso**: sin alojamiento; **50 %** de manutención si se termina **después de las 14**", "**Días intermedios**: dietas al **100 %**"],
         "Horas clave: **14, 16 y 22**",
         "Pregunta de 2025 (→ Cierre 1): el día de **salida** da **alojamiento**, no manutención salvo salida antes de las **14** (100 %) o entre las 14 y las **22** (50 %). Los días intermedios, al **100 %** (no al 75 %)."))}

{unidad("3.4 Residencia eventual: hasta el 80 por 100 sin justificar (art. 16.1)",
  lit("RD462", "Artículo 16", ["la misma autoridad que confiera la comisión", "sin que se necesite justificación documental, del 80 por 100 del importe de las dietas enteras", "deberá figurar de forma expresa en la orden"], solo=[1]),
  fichab("Cuantía de la indemnización por residencia eventual",
         "La fija la **misma autoridad** que confiere la comisión",
         "Porcentaje sobre las **dietas enteras** de los anexos II y III, que debe figurar **expresamente** en la orden",
         "Máximo: **80 por 100** de las dietas enteras, **sin justificación documental**",
         "**80 %** y **sin** justificar (frente a la dieta, cuyo alojamiento se justifica)."))}

{unidad("3.5 Gastos de viaje (art. 17.1 a 3)",
  lit("RD462", "Artículo 17", ["viajar por cuenta del Estado", "procurándose que el desplazamiento se efectúe por líneas regulares", "clase turista o clase de cuantía inferior", "podrá autorizar una clase superior", "medios gratuitos del Estado"]),
  fichab("Indemnización por gastos de viaje",
         "La autoridad que ordena la comisión determina el medio y, excepcionalmente, autoriza una clase superior",
         ["Por el importe del **billete o pasaje**, dentro de la clase que corresponde al **grupo**", "**Avión**: clase **turista** o inferior, para todos los grupos", "Alta velocidad: grupo 1, **preferente**; grupos 2 y 3, **turista**"],
         "—",
         "Clase superior: por **urgencia** sin billete de la clase debida, o por **representación** o **duración** del viaje. Con **medios gratuitos** del Estado no hay indemnización."))}
""", 2)

T.ap("s15", "V.4 Desplazamientos en el término municipal y traslados de residencia (RD 462/2002, arts. 20, 22 y 23)", f"""
{unidad("4.1 Desplazamientos dentro del término municipal (art. 20)",
  lit("RD462", "Artículo 20", ["según conformidad expresa del Jefe de la unidad administrativa correspondiente", "dentro del término municipal donde tenga su sede el centro de destino", "preferentemente en medios de transporte público colectivo"]),
  fichab("Resarcimiento de los desplazamientos dentro del término municipal",
         "El personal del Real Decreto, con **conformidad expresa del Jefe de la unidad**",
         ["Gastos de los desplazamientos **por razón del servicio** dentro del término municipal de la sede del centro de destino", "**Preferentemente** en transporte **público colectivo**, salvo que el jefe autorice otro medio", "Con vehículo particular autorizado: la cuantía de las comisiones de servicio"],
         "—",
         "Autoriza el **Jefe de la unidad** (no el Subsecretario, que designa las comisiones → V.2.2). Se paga con cargo al **anticipo de caja fija** o a fondos a justificar (art. 21.2)."))}

{unidad("4.2 Traslados de residencia: familia y caducidad (art. 22.1 y 6)",
  lit("RD462", "Artículo 22", ["el cónyuge y los hijos menores de veintiún años, en cualquier caso", "caducará al transcurrir un año desde la fecha en que aquél nazca", "prórrogas semestrales por un plazo no superior a otros dos años"], solo=[1, 2, 9]),
  fichab("Normas generales de los traslados de residencia",
         "El personal que se traslada y los **familiares** que conviven con él y a sus expensas",
         "Se presume que conviven y viven a sus expensas el **cónyuge** y los **hijos menores de veintiún años**; los demás familiares deben justificarlo",
         f"El derecho {c('RD462', 'Artículo 22', 'caducará al transcurrir un año desde la fecha en que aquél nazca')}, con prórrogas **semestrales** de hasta **otros dos años**",
         "Caducidad: **un año**; prórrogas **semestrales**, máximo **dos años** más."))}

{unidad("4.3 Traslado forzoso: qué se indemniza (art. 23.1 a 3)",
  lit("RD462", "Artículo 23", ["En caso de traslado forzoso que origine cambio del término municipal de residencia oficial", "una indemnización equivalente a tres dietas", "en ningún caso se considerarán los traslados derivados del nombramiento o cese en el desempeño de los puestos por concurso o libre designación", "Los traslados que obedezcan a sanción impuesta al funcionario no darán derecho a indemnización"], solo=[1, 2, 3, 4, 12]),
  fichab("Indemnización por traslado forzoso en territorio nacional",
         "El personal trasladado **forzosamente** con cambio de término municipal de residencia oficial, y su familia",
         ["**Gastos de viaje** (también de la familia)", "**Transporte de mobiliario y enseres**", "**Tres dietas** por el titular y por cada familiar que se traslade"],
         "—",
         "**No** es forzoso el traslado por **concurso o libre designación**; el traslado por **sanción** no da derecho a indemnización. Sí son forzosos, entre otros, los debidos a cambio de residencia oficial o **supresión** de unidades."))}
""", 2)

T.ap("s16", "V.5 Asistencias (RD 462/2002, arts. 27, 30, 32 y 33)", f"""
{unidad("5.1 Qué es una asistencia y límite conjunto (art. 27.1, 3 y 4)",
  lit("RD462", "Artículo 27", ["Concurrencia a las reuniones de órganos colegiados", "tribunales de oposiciones y concursos", "con carácter no permanente ni habitual", "superior al 50 por 100 de las retribuciones anuales", "serán compatibles con las dietas"], solo=[1, 2, 3, 4, 6, 7, 8]),
  fichab("Asistencias: concepto y límite global",
         "Los miembros de órganos colegiados, consejos de administración y tribunales, y los colaboradores no habituales en formación",
         ["a) **Órganos colegiados** y **consejos de administración** de empresas públicas", "b) **Tribunales** de oposiciones y concursos", "c) **Colaboración no permanente ni habitual** en formación y perfeccionamiento"],
         "Los tres tipos juntos: como máximo el **50 por 100** de las retribuciones anuales del puesto (excluida la antigüedad); el exceso se ingresa en el **Tesoro**",
         "Las asistencias son **compatibles** con las dietas si hay desplazamiento."))}

{unidad("5.2 Tribunales de selección: categorías y límites (arts. 30.1 y 2 y 32)",
  lit("RD462", "Artículo 30", ["Categoría primera", "Categoría segunda", "Categoría tercera", "se incrementarán en el 50 por 100 de su importe cuando las asistencias se devenguen por la concurrencia a sesiones que se celebren en sábados o en días festivos"], solo=[1, 2, 3, 4, 5]),
  lit("RD462", "Artículo 32", ["un importe total por año natural superior al 20 por 100 de las retribuciones anuales"], solo=[1]),
  fichab("Asistencias por participar en tribunales",
         f"Los miembros de los tribunales; clasifica los órganos {c('RD462', 'Artículo 30', 'El Ministerio de Administraciones Públicas')} (denominación del texto del Real Decreto)",
         ["Categoría **primera**: acceso a cuerpos del grupo **A**", "Categoría **segunda**: grupos **B y C**", "Categoría **tercera**: grupos **D y E**", "Cuantías: **anexo IV**; **+50 %** en **sábados o festivos**"],
         "Límite anual por tribunales: **20 por 100** de las retribuciones anuales del puesto principal (excluida la antigüedad)",
         "Límites por tipo: órganos colegiados y consejos, **40 %** (art. 28.3); tribunales, **20 %** (32); formación, **25 %** (33.3); los tres juntos, **50 %** (27.3)."))}

{unidad("5.3 Colaboración en formación (art. 33.1 y 3)",
  lit("RD462", "Artículo 33", ["con carácter no permanente ni habitual", "el máximo de setenta y cinco al año", "una cantidad superior al 25 por 100 de las retribuciones anuales"], solo=[1, 4]),
  fichab("Asistencias por colaborar en actividades de formación y perfeccionamiento",
         "Colaboradores **no permanentes ni habituales** de institutos o centros de formación del personal de las Administraciones",
         "Conferencias o cursos ocasionales, congresos, ponencias, seminarios y actividades análogas, según baremos",
         "Máximo **75 horas** al año y **25 por 100** de las retribuciones anuales del puesto principal",
         "**75 horas** y **25 %**."))}
""", 2)

T.ap("s17", "V.6 Imputación presupuestaria (RD 462/2002, disposición final primera; Resolución de 20 de enero de 2014)", f"""
{unidad("6.1 Quién paga: el servicio del que depende la comisión (RD 462/2002, disposición final primera)",
  lit("RD462", "dfprimera", ["Cada Ministerio, Entidad y Organismo sufragará las indemnizaciones", "cualquiera que sea el ramo de la Administración a que pertenezca el personal"]),
  fichab("Crédito al que se imputan las indemnizaciones",
         "El **Ministerio, Entidad u Organismo** del que dependan los servicios",
         "Con los créditos presupuestarios asignados al efecto, cualquiera que sea el ramo al que pertenezca el personal",
         "—",
         "Paga quien **recibe el servicio**, no el órgano de pertenencia del comisionado (salvo las comparecencias como testigo o perito por actuaciones profesionales)."))}

{unidad("6.2 Artículo 23 de la clasificación económica del gasto (Resolución de 20 de enero de 2014, anexo II)",
  lit("RES2014", "ai-2", ["23. Indemnizaciones por razón del servicio"], solo=[169, 170, 171, 172, 173], titulo="Anexo II (Resolución de 20 de enero de 2014, de la Dirección General de Presupuestos): artículo 23 de la clasificación económica"),
  fichab("Imputación del gasto por indemnizaciones en el presupuesto",
         "Dirección General de Presupuestos (códigos de la clasificación económica)",
         "Artículo **23** (capítulo 2): conceptos **230** dietas, **231** locomoción, **232** traslado y **233** otras indemnizaciones",
         "—",
         f"Cayó dos veces en 2025 (relacionada → Cierre 1). No confundir con el artículo {c('RES2014', 'ai-2', '12. Funcionarios')} (retribuciones del capítulo 1). La clasificación económica se estudia en el bloque VI."))}

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Supuesto (RD 462/2002, art. 1) | Qué es | Dato que más cae |
|---|---|---|
| Comisión de servicio | Cometido especial fuera del término municipal de la residencia oficial (art. 3) | **Un mes** en España, **tres** en el extranjero, salvo casos excepcionales (art. 5) |
| Residencia eventual | Comisión que excede esos límites (art. 6) | Máximo **un año** + prórroga de máximo un año; hasta el **80 %** de la dieta entera sin justificar (art. 16) |
| Desplazamiento en el término municipal | Por razón del servicio, con conformidad del Jefe de la unidad (art. 20) | Preferentemente en **transporte público colectivo** |
| Traslado de residencia | Forzoso, con cambio de término municipal (art. 23) | Viaje, mobiliario y **tres dietas** por persona; no por concurso, libre designación ni sanción |
| Asistencias | Órganos colegiados, tribunales y formación (art. 27) | Límites **40 / 20 / 25 / 50 %** |

{resumen([
  "Los funcionarios perciben las **indemnizaciones por razón del servicio** (TREBEP, art. 28): resarcen gastos y no son retribución.",
  "RD 462/2002: **cuatro** supuestos (comisiones, desplazamientos en el término municipal, traslados y asistencias); lo que no se ajuste es **nulo**; el **laboral**, por su convenio.",
  "Comisión: **un mes** (España) o **tres** (extranjero), salvo casos excepcionales; si se excede, **residencia eventual** (máximo un año, hasta el **80 %**).",
  "Dietas: grupos del **anexo I** y cuantías del **anexo II**; día de salida antes de las **14** = manutención al **100 %**; intermedios al **100 %**.",
  "El gasto se imputa al **artículo 23** de la clasificación económica, con cargo al órgano del que dependa el servicio."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
# Cierre 1: preguntas oficiales (plantilla comprobada contra la ley)
EX_P99 = examen("P", 99, {
  "a": f"El complemento de destino **no** es retribución básica: las básicas están integradas {c('TREBEP', 'Artículo 23', 'única y exclusivamente por')} sueldo y trienios; el destino retribuye el puesto (Ley 30/1984, art. 23.3 a).",
  "b": "Añade el complemento de destino, que es complementario; la fórmula «única y exclusivamente» excluye cualquier otro concepto.",
  "c": f"Literal del art. 23: {c('TREBEP', 'Artículo 23', 'El sueldo asignado a cada Subgrupo o Grupo')} y {c('TREBEP', 'Artículo 23', 'Los trienios, que consisten en una cantidad')}.",
  "d": f"Destino y específico son complementarios: retribuyen {c('TREBEP', 'Artículo 22', 'las características de los puestos de trabajo')} (art. 22.3)."},
  [("sueldo", "TREBEP", "Artículo 23", "El sueldo asignado a cada Subgrupo o Grupo de clasificación profesional"),
   ("trienios", "TREBEP", "Artículo 23", "Los trienios, que consisten en una cantidad"),
   ("El sueldo y los trienios", "TREBEP", "Artículo 23", "estarán integradas única y exclusivamente por")])
EX_P100 = examen("P", 100, {
  "a": f"Literal del art. 26: {c('TREBEP', 'Artículo 26', 'como mínimo, se corresponderán a las del sueldo del Subgrupo o Grupo')} en que aspiren a ingresar.",
  "b": "Añade el complemento de destino: el mínimo legal es **solo el sueldo**.",
  "c": "Añade el complemento específico: el mínimo legal es **solo el sueldo**.",
  "d": "Añade gratificaciones extraordinarias, que el art. 26 no menciona: el mínimo es el sueldo del Subgrupo al que se aspira."},
  [("sueldo del Subgrupo", "TREBEP", "Artículo 26", "a las del sueldo del Subgrupo o Grupo"),
   ("en que aspiren a ingresar.", "TREBEP", "Artículo 26", "en que aspiren a ingresar")])
EX_L72 = examen("L", 72, {
  "a": f"Es la regla de las **pagas extraordinarias**, no de los trienios: {c('L30', 'aveinticuatro', 'las cuantías de las pagas extraordinarias serán iguales, en todas las Administraciones públicas, para cada uno de los grupos de clasificación según el nivel del complemento de destino que se perciba')}.",
  "b": f"El índice de proporcionalidad es del **sueldo**: {c('L30', 'aveintitres', 'El sueldo, que corresponde al índice de proporcionalidad asignado a cada uno de los grupos')}. El trienio es {c('L30', 'aveintitres', 'una cantidad igual para cada grupo, por cada tres años de servicio')}.",
  "c": f"Literal del art. 24.1: las cuantías del sueldo y los trienios {c('L30', 'aveinticuatro', 'serán iguales en todas las Administraciones públicas, para cada uno de los grupos en que se clasifican los cuerpos, escalas, categorías o clases de funcionarios')}.",
  "d": "Mezcla el índice de proporcionalidad (propio del sueldo) con el periodo de **tres años** del trienio; la ley no habla de un índice asignado «cada tres años»."},
  [("para cada uno de los grupos en que se clasifican los cuerpos, escalas, categorías o clases de funcionarios", "L30", "aveinticuatro", "serán iguales en todas las Administraciones públicas, para cada uno de los grupos en que se clasifican los cuerpos, escalas, categorías o clases de funcionarios")])
EX_L99 = examen("L", 99, {
  "a": f"El complemento de destino es el {c('L30', 'aveintitres', 'correspondiente al nivel del puesto que se desempeñe')} (art. 23.3 a).",
  "b": f"El de productividad retribuye {c('L30', 'aveintitres', 'el especial rendimiento, la actividad extraordinaria y el interés o iniciativa')} (art. 23.3 c).",
  "c": f"Literal del art. 23.3 b): {c('L30', 'aveintitres', 'El complemento específico destinado a retribuir las condiciones particulares de algunos puestos de trabajo')}.",
  "d": f"Las gratificaciones son {c('L30', 'aveintitres', 'por servicios extraordinarios, fuera de la jornada normal')} (art. 23.3 d)."},
  [("Complemento específico", "L30", "aveintitres", "El complemento específico destinado a retribuir las condiciones particulares de algunos puestos de trabajo en atención a su especial dificultad técnica, dedicación, responsabilidad, incompatibilidad, peligrosidad o penosidad")])
EX_X98 = examen("X", 98, {
  "a": f"Las básicas retribuyen {c('TREBEP', 'Artículo 22', 'según la adscripción de su cuerpo o escala')} a un Subgrupo y la antigüedad (art. 22.2): sueldo y trienios.",
  "b": f"Las complementarias retribuyen {c('TREBEP', 'Artículo 22', 'las características de los puestos de trabajo, la carrera profesional o el desempeño')} (art. 22.3).",
  "c": "Las indemnizaciones resarcen gastos **por razón del servicio** (art. 28), no son aportaciones a planes de pensiones.",
  "d": f"Literal del art. 29: esas cantidades {c('TREBEP', 'Artículo 29', 'tendrán a todos los efectos la consideración de retribución diferida')}."},
  [("Retribuciones diferidas", "TREBEP", "Artículo 29", "Retribuciones diferidas")])
EX_X99 = examen("X", 99, {
  "a": f"Literal del art. 30.1: {c('TREBEP', 'Artículo 30', 'dará lugar a la deducción proporcional de haberes, que no tendrá carácter sancionador')}.",
  "b": f"Sí hay deducción: {c('TREBEP', 'Artículo 30', 'la parte de jornada no realizada dará lugar a la deducción proporcional de haberes')}, sin perjuicio de la sanción disciplinaria.",
  "c": f"Cambia una palabra: la deducción {c('TREBEP', 'Artículo 30', 'no tendrá carácter sancionador')}.",
  "d": f"El art. 30 del TREBEP no prohíbe la deducción, la regula: {c('TREBEP', 'Artículo 30', 'la parte de jornada no realizada dará lugar a la deducción proporcional de haberes')}. La norma de la Unión que cita la opción no aparece en él."},
  [("que no tendrá carácter sancionador", "TREBEP", "Artículo 30", "que no tendrá carácter sancionador")])
EX_L73 = examen("L", 73, {
  "a": f"Sí da lugar: {c('RD462', 'Artículo 1', 'Desplazamientos dentro del término municipal por razón de servicio')} (art. 1.1 b).",
  "b": f"No está entre los supuestos del art. 1.1 del RD 462/2002. La redistribución de efectivos es una adscripción a otro puesto {c('RD364', 'Artículo 59', 'sin que ello suponga cambio de municipio')} (RD 364/1995, art. 59.1).",
  "c": f"Sí da lugar: {c('RD462', 'Artículo 1', 'Traslados de residencia')} (art. 1.1 c).",
  "d": f"Sí da lugar: asistencias {c('RD462', 'Artículo 1', 'por la colaboración en centros de formación y perfeccionamiento del personal de las Administraciones públicas')} (art. 1.1 d)."},
  [("Redistribución de efectivos", "RD364", "Artículo 59", "Redistribución de efectivos"),
   ("Redistribución de efectivos", "RD364", "Artículo 59", "sin que ello suponga cambio de municipio")])
EX_L71 = examen("L", 71, {
  "a": f"Literal del art. 5.1: {c('RD462', 'Artículo 5', 'salvo casos excepcionales, no durará más de un mes en territorio nacional y de tres en el extranjero')}.",
  "b": f"Los plazos son correctos, pero **no** son improrrogables: cabe {c('RD462', 'Artículo 5', 'la concesión de prórroga por el tiempo estrictamente indispensable')} (art. 5.2).",
  "c": "Cambia los plazos: no son quince días y un mes, sino **un mes** y **tres meses**.",
  "d": "Cambia los plazos y la regla: ni dos meses en ambos casos, ni improrrogables."},
  [("Salvo casos excepcionales", "RD462", "Artículo 5", "salvo casos excepcionales"),
   ("un mes en territorio nacional y de tres en el extranjero", "RD462", "Artículo 5", "no durará más de un mes en territorio nacional y de tres en el extranjero")])
EX_X79 = examen("X", 79, {
  "a": f"Literal del art. 5.1: {c('RD462', 'Artículo 5', 'Toda comisión con derecho a indemnización, salvo casos excepcionales, no durará más de un mes en territorio nacional y de tres en el extranjero')}.",
  "b": "Cambia los plazos: no quince días y un mes, sino **un mes** y **tres meses**.",
  "c": "Invierte los plazos: un mes en territorio nacional y **tres** en el extranjero.",
  "d": "Iguala los plazos: en el extranjero son **tres** meses, no uno."},
  [("un mes en territorio nacional y de tres en el extranjero", "RD462", "Artículo 5", "no durará más de un mes en territorio nacional y de tres en el extranjero")])
EX_X80 = examen("X", 80, {
  "a": "Invierte la regla del día de salida (que da alojamiento y no manutención) y cambia las horas: las de la ley son las **14** y las **22** horas.",
  "b": f"Es, con matices, la regla del día de **regreso** (art. 12.3 b), no la del día de salida: {c('RD462', 'Artículo 12', 'En el día de regreso no se podrán percibir gastos de alojamiento ni de manutención')}.",
  "c": f"Literal del art. 12.3 a): {c('RD462', 'Artículo 12', 'En el día de salida se podrán percibir gastos de alojamiento pero no gastos de manutención, salvo que la hora fijada para iniciar la comisión sea anterior a las catorce horas')}.",
  "d": f"Cambia el porcentaje: {c('RD462', 'Artículo 12', 'En los días intermedios entre los de salida y regreso se percibirán dietas al 100 por 100')}."},
  [("En el día de salida se podrán percibir gastos de alojamiento pero no gastos de manutención", "RD462", "Artículo 12", "En el día de salida se podrán percibir gastos de alojamiento pero no gastos de manutención"),
   ("posterior a las catorce horas pero anterior a las veintidós horas", "RD462", "Artículo 12", "cuando dicha hora de salida sea posterior a las catorce horas pero anterior a las veintidós horas")])
EX_L94 = examen("L", 94, {
  "a": f"El artículo 21 es otro: {c('RES2014', 'ai-2', '21. Reparaciones, mantenimiento y conservación')}.",
  "b": f"El artículo 12 es de gastos de personal: {c('RES2014', 'ai-2', '12. Funcionarios')}.",
  "c": f"Literal del anexo II: {c('RES2014', 'ai-2', '23. Indemnizaciones por razón del servicio')}.",
  "d": f"El artículo 14 es {c('RES2014', 'ai-2', '14. Otro personal')}."},
  [("Artículo 23", "RES2014", "ai-2", "23. Indemnizaciones por razón del servicio")])
EX_P96 = examen("P", 96, {
  "a": f"El 12 es {c('RES2014', 'ai-2', '12. Funcionarios')} (capítulo 1, gastos de personal).",
  "b": f"Literal del anexo II: {c('RES2014', 'ai-2', '23. Indemnizaciones por razón del servicio')}.",
  "c": f"El 42 es una transferencia corriente: {c('RES2014', 'ai-2', '42. A la Seguridad Social')}.",
  "d": f"El 60 es una inversión real: {c('RES2014', 'ai-2', '60. Inversión nueva en infraestructura y bienes destinados al uso general')}."},
  [("23", "RES2014", "ai-2", "23. Indemnizaciones por razón del servicio")])

T.ap("s18", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **diez** preguntas de este tema y **dos** relacionadas (imputación presupuestaria de las indemnizaciones). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-P 2025, pregunta 99 · Retribuciones básicas (→ II.1.2)", EX_P99,
  "### GACE-L 2025, pregunta 72 · Trienios en la Ley 30/1984 (→ II.3.2)", EX_L72,
  "### GACE-L 2025, pregunta 99 · Complemento específico (→ III.2.1)", EX_L99,
  "### GACE-P 2025, pregunta 100 · Funcionarios en prácticas (→ IV.1.2)", EX_P100,
  "### GACE-L 2025 extraordinario, pregunta 98 · Retribuciones diferidas (→ IV.2.1)", EX_X98,
  "### GACE-L 2025 extraordinario, pregunta 99 · Deducción de retribuciones (→ IV.2.2)", EX_X99,
  "### GACE-L 2025, pregunta 73 · Supuestos de indemnización (→ V.1.2)", EX_L73,
  "### GACE-L 2025, pregunta 71 · Duración de las comisiones (→ V.2.3)", EX_L71,
  "### GACE-L 2025 extraordinario, pregunta 79 · Duración de las comisiones (→ V.2.3)", EX_X79,
  "### GACE-L 2025 extraordinario, pregunta 80 · Dietas del día de salida (→ V.3.3)", EX_X80,
  "### GACE-L 2025, pregunta 94 · Imputación presupuestaria (relacionada; → V.6.2)", EX_L94,
  "### GACE-P 2025, pregunta 96 · Imputación presupuestaria (relacionada; → V.6.2)", EX_P96,
  "### Cómo se pregunta",
  "!> Dos patrones: (1) **qué ley** cita el enunciado (TREBEP o Ley 30/1984: cambian las palabras y el lugar de las pagas extraordinarias); (2) **plazos y horas** del RD 462/2002 cambiados en los distractores (un mes / tres meses; 14 y 22 horas; 100 % o 50 %). La pregunta de 2025 sobre el límite de los anticipos de caja fija del artículo 23 está **retenida** en el test real (la plantilla no casa con la Ley General Presupuestaria) y no se incluye aquí.",
]))

T.ap("s19", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Sistema | Ley de presupuestos (21); básicas y complementarias (22.1); nada de tributos ni multas (22.5); efectos diferidos y Ley 30/1984 | Límite de la masa salarial: el de la **LPGE** |
| II. Básicas | Grupo y antigüedad; **única y exclusivamente** sueldo y trienios (23); pagas extraordinarias (22.4) | Trienio: igual por Subgrupo, cada **3 años**; Ley 30/1984: pagas en **junio y diciembre** |
| III. Complementarias | Puesto, carrera y desempeño (22.3); factores abiertos (24); destino, específico, productividad y gratificaciones (Ley 30/1984) | **Específico**: peligrosidad o penosidad, uno por puesto |
| IV. Reglas complementarias | Interinos (25), prácticas (26), laborales (27), diferidas (29), deducción (30) | Prácticas: mínimo el **sueldo**; deducción **no sancionadora** |
| V. Indemnizaciones | Art. 28; RD 462/2002: cuatro supuestos, comisiones, dietas, residencia eventual, traslados y asistencias | **Un mes / tres meses**; residencia eventual **80 %**; horas **14 y 22** |

?> **Trampas frecuentes:** «las básicas son sueldo, trienios y **complemento de destino**» (solo sueldo y trienios); «el índice de proporcionalidad corresponde a los **trienios**» (es del **sueldo**); «la deducción de haberes **tiene carácter sancionador**» (no lo tiene); «comisión de un mes en España y tres en el extranjero, **improrrogables**» (cabe prórroga); «en los días intermedios, dietas al **75 %**» (al **100 %**); «el traslado por **concurso** es forzoso» (no lo es); «el personal **laboral** se rige por el RD 462/2002» (por su convenio).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
q = T.q
q("TREBEP", "Artículo 21", "Sistema retributivo", "Según el artículo 21.1 del TREBEP, ¿qué debe reflejarse para cada ejercicio presupuestario en la correspondiente ley de presupuestos respecto de las retribuciones complementarias de los funcionarios?",
  ["El incremento de sus cuantías globales.", "Su cuantía individual para cada funcionario.", "Su estructura y su cuantía para cada puesto de trabajo.", "Nada: las fija cada Administración por acuerdo de su órgano de gobierno."],
  "Art. 21.1: «el incremento de las cuantías globales de las retribuciones complementarias».", "el incremento de las cuantías globales de las retribuciones complementarias de los funcionarios")
q("TREBEP", "Artículo 21", "Sistema retributivo", "Según el artículo 21.2 del TREBEP, no podrán acordarse incrementos retributivos que globalmente supongan un incremento de la masa salarial superior a los límites fijados anualmente:",
  ["En la Ley de Presupuestos Generales del Estado para el personal.", "Por el Consejo de Ministros a propuesta del Ministerio de Hacienda.", "En la Mesa General de Negociación de las Administraciones Públicas.", "En la ley de presupuestos de cada Comunidad Autónoma, sin límite estatal."],
  "Art. 21.2 TREBEP.", "superior a los límites fijados anualmente en la Ley de Presupuestos Generales del Estado para el personal")
q("TREBEP", "Artículo 22", "Sistema retributivo", "Según el artículo 22.1 del TREBEP, las retribuciones de los funcionarios de carrera se clasifican en:",
  ["Básicas y complementarias.", "Básicas, complementarias y extraordinarias.", "Fijas y variables.", "Básicas, complementarias e indemnizaciones."],
  "Art. 22.1 TREBEP.", "se clasifican en básicas y complementarias")
q("TREBEP", "Artículo 22", "Sistema retributivo", "Según el artículo 22.5 del TREBEP, ¿qué no podrá percibirse como contraprestación de cualquier servicio?",
  ["Participación en tributos o en cualquier otro ingreso de las Administraciones Públicas.", "Complemento específico.", "Gratificaciones por servicios extraordinarios.", "Indemnizaciones por razón del servicio."],
  "Art. 22.5: también la participación o premio en multas, aun cuando estuviesen atribuidas a los servicios.", "No podrá percibirse participación en tributos o en cualquier otro ingreso de las Administraciones Públicas como contraprestación de cualquier servicio")
q("TREBEP", "dfcuaa", "Sistema retributivo", "Según la disposición final cuarta del TREBEP, lo establecido en el capítulo III del título III (derechos retributivos), excepto el artículo 25.2, producirá efectos:",
  ["A partir de la entrada en vigor de las leyes de Función Pública que se dicten en desarrollo del Estatuto.", "Desde el día siguiente al de la publicación del Estatuto en el BOE.", "A partir del 1 de enero del año siguiente a su publicación.", "Cuando lo acuerde la Conferencia Sectorial de Administración Pública."],
  "Disposición final cuarta.1 TREBEP.", "producirá efectos a partir de la entrada en vigor de las leyes de Función Pública que se dicten en desarrollo de este Estatuto")
q("TREBEP", "Artículo 22", "Retribuciones básicas", "Según el artículo 22.2 del TREBEP, las retribuciones básicas retribuyen al funcionario según:",
  ["La adscripción de su cuerpo o escala a un Subgrupo o Grupo de clasificación profesional y su antigüedad en el mismo.", "Las características del puesto de trabajo que desempeñe.", "El grado de interés, iniciativa o esfuerzo con que desempeñe su trabajo.", "La progresión alcanzada dentro del sistema de carrera administrativa."],
  "Art. 22.2 TREBEP. Las otras opciones son factores de las complementarias (arts. 22.3 y 24).", ["según la adscripción de su cuerpo o escala a un determinado Subgrupo o Grupo de clasificación profesional", "y por su antigüedad en el mismo"])
q("TREBEP", "Artículo 23", "Retribuciones básicas", "Según el artículo 23 del TREBEP, las retribuciones básicas se fijan:",
  ["En la Ley de Presupuestos Generales del Estado.", "En las leyes de función pública de cada Administración.", "Por real decreto del Consejo de Ministros.", "En los convenios colectivos de cada Administración."],
  "Art. 23 TREBEP.", "Las retribuciones básicas, que se fijan en la Ley de Presupuestos Generales del Estado")
q("TREBEP", "Artículo 23", "Retribuciones básicas", "Según el artículo 23 del TREBEP, los trienios consisten en una cantidad, que será igual para cada Subgrupo o Grupo de clasificación profesional, por cada:",
  ["Tres años de servicio.", "Tres años de servicio en el mismo puesto de trabajo.", "Dos años de servicio.", "Cinco años de servicio."],
  "Art. 23 b) TREBEP.", "por cada tres años de servicio")
q("TREBEP", "Artículo 22", "Retribuciones básicas", "Según el artículo 22.4 del TREBEP, cada paga extraordinaria incluye el importe de una mensualidad de retribuciones básicas y de la totalidad de las retribuciones complementarias, salvo aquellas a las que se refieren:",
  ["Los apartados c) y d) del artículo 24.", "Los apartados a) y b) del artículo 24.", "Los apartados b) y c) del artículo 24.", "Los apartados a) y d) del artículo 24."],
  "Art. 22.4 TREBEP: se excluyen las de rendimiento (24 c) y servicios extraordinarios (24 d).", "salvo aquéllas a las que se refieren los apartados c) y d) del artículo 24")
q("TREBEP", "Artículo 22", "Retribuciones básicas", "Según el artículo 22.4 del TREBEP, las pagas extraordinarias serán:",
  ["Dos al año.", "Tres al año.", "Una al año, prorrateable en doce mensualidades.", "Dos al año, por el importe de una mensualidad de retribuciones básicas exclusivamente."],
  "Art. 22.4 TREBEP: dos al año, con básicas y la totalidad de las complementarias (salvo 24 c y d).", "Las pagas extraordinarias serán dos al año")
q("L30", "aveintitres", "Retribuciones básicas", "Según el artículo 23.2 de la Ley 30/1984, las pagas extraordinarias se devengarán los meses de:",
  ["Junio y diciembre.", "Julio y diciembre.", "Junio y noviembre.", "Enero y julio."],
  "Art. 23.2 c) Ley 30/1984.", "se devengarán los meses de junio y diciembre")
q("L30", "aveintitres", "Retribuciones básicas", "Según el artículo 23.2 de la Ley 30/1984, cuando un funcionario cambie de adscripción a grupo antes de completar un trienio, la fracción de tiempo transcurrido:",
  ["Se considerará como tiempo de servicios prestados en el nuevo grupo.", "Se perderá a efectos de trienios.", "Se abonará como una fracción de trienio del grupo anterior.", "Solo se computará si supera dieciocho meses."],
  "Art. 23.2 b) Ley 30/1984.", "la fracción de tiempo transcurrido se considerará como tiempo de servicios prestados en el nuevo grupo")
q("L30", "aveintitres", "Retribuciones básicas", "Según el artículo 23.2 de la Ley 30/1984, el sueldo corresponde:",
  ["Al índice de proporcionalidad asignado a cada uno de los grupos en que se organizan los Cuerpos y Escalas, Clases o Categorías.", "Al nivel del puesto que se desempeñe.", "A una cantidad igual para cada grupo por cada tres años de servicio.", "A las condiciones particulares de algunos puestos de trabajo."],
  "Art. 23.2 a) Ley 30/1984. Las otras opciones describen el complemento de destino, los trienios y el complemento específico.", "El sueldo, que corresponde al índice de proporcionalidad asignado a cada uno de los grupos en que se organizan los Cuerpos y Escalas, Clases o Categorías")
q("L30", "aveinticuatro", "Retribuciones básicas", "Según el artículo 24.1 de la Ley 30/1984, el sueldo de los funcionarios del grupo A no podrá exceder del sueldo de los funcionarios del grupo E en más de:",
  ["Tres veces.", "Dos veces.", "Cuatro veces.", "Cinco veces."],
  "Art. 24.1 Ley 30/1984.", "no podrá exceder en más de tres veces al sueldo de los funcionarios del grupo E")
q("TREBEP", "Artículo 22", "Retribuciones complementarias", "Según el artículo 22.3 del TREBEP, las retribuciones complementarias son las que retribuyen:",
  ["Las características de los puestos de trabajo, la carrera profesional o el desempeño, rendimiento o resultados alcanzados.", "La adscripción del cuerpo o escala a un Subgrupo y la antigüedad.", "Los gastos que ocasiona el servicio fuera de la residencia oficial.", "Exclusivamente los servicios extraordinarios fuera de la jornada."],
  "Art. 22.3 TREBEP.", "las características de los puestos de trabajo, la carrera profesional o el desempeño, rendimiento o resultados alcanzados por el funcionario")
q("TREBEP", "Artículo 24", "Retribuciones complementarias", "Según el artículo 24 del TREBEP, la cuantía y estructura de las retribuciones complementarias de los funcionarios se establecerán:",
  ["Por las correspondientes leyes de cada Administración Pública.", "Por la Ley de Presupuestos Generales del Estado para todas las Administraciones.", "Por real decreto del Gobierno de la Nación.", "Por acuerdo de la Mesa General de Negociación."],
  "Art. 24 TREBEP.", "se establecerán por las correspondientes leyes de cada Administración Pública")
q("TREBEP", "Artículo 24", "Retribuciones complementarias", "¿Cuál de los siguientes es un factor que, según el artículo 24 del TREBEP, se atiende para fijar las retribuciones complementarias?",
  ["Los servicios extraordinarios prestados fuera de la jornada normal de trabajo.", "La antigüedad en el Subgrupo de clasificación.", "El Subgrupo al que esté adscrito el cuerpo o escala.", "Las aportaciones a planes de pensiones de empleo."],
  "Art. 24 d) TREBEP. La antigüedad y el Subgrupo son propios de las básicas (art. 22.2); los planes de pensiones, de la retribución diferida (art. 29).", "Los servicios extraordinarios prestados fuera de la jornada normal de trabajo")
q("L30", "aveintitres", "Retribuciones complementarias", "Según el artículo 23.3 de la Ley 30/1984, el complemento de destino corresponde:",
  ["Al nivel del puesto que se desempeñe.", "Al grupo del cuerpo o escala del funcionario.", "Al especial rendimiento del funcionario.", "A la peligrosidad o penosidad del puesto."],
  "Art. 23.3 a) Ley 30/1984.", "El complemento de destino correspondiente al nivel del puesto que se desempeñe")
q("L30", "aveintitres", "Retribuciones complementarias", "Según el artículo 23.3 de la Ley 30/1984, ¿cuántos complementos específicos pueden asignarse a cada puesto de trabajo?",
  ["En ningún caso más de uno.", "Hasta dos, si concurren peligrosidad y penosidad.", "Tantos como condiciones particulares concurran en el puesto.", "Uno por cada factor: dificultad técnica, dedicación y responsabilidad."],
  "Art. 23.3 b) Ley 30/1984.", "En ningún caso podrá asignarse más de un complemento específico a cada puesto de trabajo")
q("L30", "aveintitres", "Retribuciones complementarias", "Según el artículo 23.3 de la Ley 30/1984, las cantidades que perciba cada funcionario por complemento de productividad:",
  ["Serán de conocimiento público de los demás funcionarios del Departamento u Organismo interesado así como de los representantes sindicales.", "Serán reservadas y solo las conocerá el interesado.", "Solo se comunicarán a los representantes sindicales.", "Se publicarán en el Boletín Oficial del Estado."],
  "Art. 23.3 c) Ley 30/1984.", "serán de conocimiento público de los demás funcionarios del Departamento u Organismo interesado así como de los representantes sindicales")
q("L30", "aveintitres", "Retribuciones complementarias", "Según el artículo 23.3 de la Ley 30/1984, las gratificaciones por servicios extraordinarios fuera de la jornada normal:",
  ["En ningún caso podrán ser fijas en su cuantía y periódicas en su devengo.", "Serán fijas en su cuantía y se devengarán mensualmente.", "Se integran en el complemento específico.", "Se devengarán en junio y diciembre."],
  "Art. 23.3 d) Ley 30/1984.", "en ningún caso podrán ser fijas en su cuantía y periódicas en su devengo")
q("RDL6", "dt-7", "Retribuciones complementarias", "Según la disposición transitoria séptima del Real Decreto-ley 6/2023, una vez se implemente la evaluación del desempeño, el complemento de desempeño sustituirá a todos los efectos al complemento:",
  ["De productividad.", "Específico.", "De destino.", "De carrera."],
  "Disposición transitoria séptima del RDL 6/2023.", "el complemento de desempeño sustituirá a todos los efectos al complemento de productividad")
q("RDL6", "a1-34", "Retribuciones complementarias", "Según el artículo 122.7 del Real Decreto-ley 6/2023, la progresión alcanzada en el sistema de carrera profesional horizontal se retribuirá mediante:",
  ["Un complemento de carrera.", "Un complemento de destino de nivel superior.", "Un trienio adicional.", "El complemento de productividad."],
  "Art. 122.7 RDL 6/2023: cuantía igual para el mismo grupo o subgrupo y el mismo tramo.", "se retribuirá mediante un complemento de carrera")
q("TREBEP", "Artículo 25", "Interinos, prácticas y laborales", "Según el artículo 25.1 del TREBEP, los funcionarios interinos percibirán las retribuciones complementarias a que se refieren:",
  ["Los apartados b), c) y d) del artículo 24.", "Todos los apartados del artículo 24.", "Los apartados a) y b) del artículo 24.", "Solo el apartado b) del artículo 24."],
  "Art. 25.1 TREBEP: no perciben la del apartado a) (progresión en la carrera).", "las retribuciones complementarias a que se refieren los apartados b), c) y d) del artículo 24")
q("TREBEP", "Artículo 26", "Interinos, prácticas y laborales", "Según el artículo 26 del TREBEP, las retribuciones de los funcionarios en prácticas se corresponderán, como mínimo, a las del sueldo del Subgrupo o Grupo:",
  ["En que aspiren a ingresar.", "Al que pertenezcan antes de iniciar las prácticas.", "Inmediatamente inferior a aquel en que aspiren a ingresar.", "Que fije el órgano de selección."],
  "Art. 26 TREBEP.", "en que aspiren a ingresar")
q("TREBEP", "Artículo 27", "Interinos, prácticas y laborales", "Según el artículo 27 del TREBEP, las retribuciones del personal laboral se determinarán de acuerdo con la legislación laboral, el convenio colectivo aplicable y el contrato de trabajo, respetando en todo caso lo establecido en el artículo:",
  ["21 del Estatuto.", "23 del Estatuto.", "24 del Estatuto.", "28 del Estatuto."],
  "Art. 27 TREBEP: el art. 21 fija los límites de la ley de presupuestos.", "respetando en todo caso lo establecido en el artículo 21 del presente Estatuto")
q("TREBEP", "Artículo 29", "Retribuciones diferidas y deducciones", "Según el artículo 29 del TREBEP, las Administraciones Públicas podrán destinar a financiar aportaciones a planes de pensiones de empleo o contratos de seguro colectivos que incluyan la cobertura de la contingencia de jubilación cantidades hasta:",
  ["El porcentaje de la masa salarial que se fije en las correspondientes Leyes de Presupuestos Generales del Estado.", "El 5 por 100 de las retribuciones básicas.", "El porcentaje que acuerde cada Administración en su Mesa de Negociación.", "La cuantía de una paga extraordinaria al año."],
  "Art. 29 TREBEP.", "hasta el porcentaje de la masa salarial que se fije en las correspondientes Leyes de Presupuestos Generales del Estado")
q("TREBEP", "Artículo 30", "Retribuciones diferidas y deducciones", "Según el artículo 30.2 del TREBEP, la deducción de haberes a quienes ejerciten el derecho de huelga:",
  ["No tendrá carácter de sanción ni afectará al régimen respectivo de sus prestaciones sociales.", "Tendrá carácter de sanción disciplinaria leve.", "Afectará al cómputo de sus prestaciones sociales.", "Solo procederá si la huelga es declarada ilegal."],
  "Art. 30.2 TREBEP.", "sin que la deducción de haberes que se efectúe tenga carácter de sanción, ni afecte al régimen respectivo de sus prestaciones sociales")
q("RD462", "Artículo 1", "Indemnizaciones", "Según el artículo 1.2 del Real Decreto 462/2002, toda concesión de indemnizaciones que no se ajuste en su cuantía o en los requisitos para su concesión a sus preceptos:",
  ["Se considerará nula.", "Será anulable en el plazo de cuatro años.", "Será válida si la autoriza el Subsecretario.", "Deberá ser convalidada por el Ministerio de Hacienda."],
  "Art. 1.2 RD 462/2002: no puede surtir efectos en las cajas pagadoras.", "se considerará nula")
q("RD462", "Artículo 2", "Indemnizaciones", "Según el artículo 2.2 del Real Decreto 462/2002, ¿a qué personal NO se aplica, que se rige en su caso por su convenio colectivo o normativa específica?",
  ["Al personal de carácter laboral.", "Al personal interino.", "Al personal en prácticas.", "Al personal no vinculado jurídicamente con la Administración que preste servicios que den lugar a indemnización."],
  "Art. 2.2 RD 462/2002.", "excepto el de carácter laboral al que se aplicará, en su caso, lo previsto en el respectivo convenio colectivo")
q("RD462", "Artículo 4", "Indemnizaciones", "Según el artículo 4.1 del Real Decreto 462/2002, la designación de las comisiones de servicio con derecho a indemnización compete, con carácter general:",
  ["Al Subsecretario de cada Departamento ministerial o a la autoridad superior del Organismo o Entidad correspondiente.", "Al Ministro de cada Departamento.", "Al Jefe de la unidad administrativa en que preste servicios el comisionado.", "Al Ministerio de Hacienda."],
  "Art. 4.1 RD 462/2002.", "compete al Subsecretario de cada Departamento ministerial o a la autoridad superior del Organismo o Entidad correspondiente")
q("RD462", "Artículo 6", "Indemnizaciones", "Según el artículo 6.2 del Real Decreto 462/2002, la duración de la residencia eventual no podrá exceder, salvo prórroga, de:",
  ["Un año.", "Seis meses.", "Tres meses.", "Dos años."],
  "Art. 6.2 RD 462/2002: la prórroga tampoco puede exceder de un año.", "La duración de la residencia eventual no podrá exceder de un año")
q("RD462", "Artículo 16", "Indemnizaciones", "Según el artículo 16.1 del Real Decreto 462/2002, la cuantía de la indemnización por residencia eventual se fijará, sin que se necesite justificación documental, dentro del límite máximo del:",
  ["80 por 100 del importe de las dietas enteras.", "50 por 100 del importe de las dietas enteras.", "100 por 100 del importe de las dietas enteras.", "75 por 100 del importe de la dieta de manutención."],
  "Art. 16.1 RD 462/2002.", "del 80 por 100 del importe de las dietas enteras")
q("RD462", "Artículo 12", "Indemnizaciones", "Según el artículo 12.1 del Real Decreto 462/2002, en las comisiones de duración igual o inferior a un día natural se percibirá el 50 por 100 de la dieta por manutención cuando, con una duración mínima de cinco horas, la comisión se inicie:",
  ["Antes de las catorce horas y finalice después de las dieciséis horas.", "Antes de las diez horas y finalice después de las catorce horas.", "Antes de las catorce horas y finalice después de las veintidós horas.", "Después de las catorce horas y finalice antes de las dieciséis horas."],
  "Art. 12.1 RD 462/2002.", "ésta se inicie antes de las catorce horas y finalice después de las dieciséis horas")
q("RD462", "Artículo 12", "Indemnizaciones", "Según el artículo 12.3 del Real Decreto 462/2002, en las comisiones de duración superior a veinticuatro horas, en el día de regreso:",
  ["No se podrán percibir gastos de alojamiento ni de manutención, salvo que la comisión concluya después de las catorce horas, en que se percibirá, con carácter general, el 50 por 100 de los gastos de manutención.", "Se percibirán dietas al 100 por 100.", "Se podrán percibir gastos de alojamiento pero no de manutención.", "Se percibirá en todo caso el 50 por 100 de los gastos de alojamiento."],
  "Art. 12.3 b) RD 462/2002.", "En el día de regreso no se podrán percibir gastos de alojamiento ni de manutención, salvo que la hora fijada para concluir la comisión sea posterior a las catorce horas")
q("RD462", "Artículo 17", "Indemnizaciones", "Según el artículo 17.2 del Real Decreto 462/2002, en los viajes en avión se indemnizará por el importe del billete dentro de las tarifas correspondientes a:",
  ["Clase turista o clase de cuantía inferior a la prevista para aquélla.", "Clase preferente para el grupo primero y turista para los demás.", "Clase preferente para todos los grupos.", "La clase que elija el comisionado."],
  "Art. 17.2 a) RD 462/2002: para todos los grupos.", "Avión: clase turista o clase de cuantía inferior a la prevista para aquélla")
q("RD462", "Artículo 20", "Indemnizaciones", "Según el artículo 20.1 del Real Decreto 462/2002, los desplazamientos por razón del servicio dentro del término municipal donde tenga su sede el centro de destino se resarcen según conformidad expresa:",
  ["Del Jefe de la unidad administrativa correspondiente.", "Del Subsecretario del Departamento.", "Del Ministerio de Hacienda.", "Del Delegado del Gobierno."],
  "Art. 20.1 RD 462/2002.", "según conformidad expresa del Jefe de la unidad administrativa correspondiente")
q("RD462", "Artículo 23", "Indemnizaciones", "Según el artículo 23.1 del Real Decreto 462/2002, en caso de traslado forzoso con cambio de término municipal de residencia oficial dentro del territorio nacional, además de los gastos de viaje y de transporte de mobiliario y enseres, se tendrá derecho a una indemnización equivalente a:",
  ["Tres dietas por el titular y cada miembro de su familia que efectivamente se traslade.", "Una dieta por el titular y media por cada miembro de su familia.", "Una mensualidad de retribuciones básicas.", "Cinco dietas por el titular, con independencia de la familia."],
  "Art. 23.1 RD 462/2002.", "una indemnización equivalente a tres dietas por el titular y cada miembro de su familia que efectivamente se traslade")
q("RD462", "Artículo 23", "Indemnizaciones", "Según el artículo 23.3 del Real Decreto 462/2002, los traslados que obedezcan a sanción impuesta al funcionario:",
  ["No darán derecho a indemnización.", "Darán derecho a la mitad de la indemnización por traslado forzoso.", "Darán derecho solo a los gastos de viaje del titular.", "Se indemnizarán como traslado forzoso."],
  "Art. 23.3 RD 462/2002.", "Los traslados que obedezcan a sanción impuesta al funcionario no darán derecho a indemnización")
q("RD462", "Artículo 32", "Indemnizaciones", "Según el artículo 32 del Real Decreto 462/2002, por las asistencias por participación en tribunales y órganos de selección de personal no se podrá percibir un importe total por año natural superior al:",
  ["20 por 100 de las retribuciones anuales, excluidas las de carácter personal derivadas de la antigüedad, que correspondan por el puesto de trabajo principal.", "50 por 100 de las retribuciones anuales del puesto principal.", "40 por 100 de las retribuciones anuales del puesto principal.", "25 por 100 de las retribuciones anuales del puesto principal."],
  "Art. 32 RD 462/2002. El 40 % es el de órganos colegiados (art. 28.3), el 25 % el de formación (art. 33.3) y el 50 % el conjunto (art. 27.3).", "un importe total por año natural superior al 20 por 100 de las retribuciones anuales, excluidas las de carácter personal derivadas de la antigüedad, que correspondan por el puesto de trabajo principal")
q("RD462", "Artículo 30", "Indemnizaciones", "Según el artículo 30.2 del Real Decreto 462/2002, las cuantías de las asistencias a tribunales se incrementarán en el 50 por 100 de su importe cuando se devenguen por la concurrencia a sesiones que se celebren:",
  ["En sábados o en días festivos.", "Fuera del término municipal de la residencia oficial.", "En horario de tarde.", "Durante el mes de agosto."],
  "Art. 30.2 RD 462/2002.", "cuando las asistencias se devenguen por la concurrencia a sesiones que se celebren en sábados o en días festivos")
q("RD462", "Artículo 33", "Indemnizaciones", "Según el artículo 33.1 del Real Decreto 462/2002, las asistencias por colaboración en actividades de formación y perfeccionamiento se podrán abonar siempre que el total de horas del conjunto de estas actividades no supere individualmente el máximo de:",
  ["Setenta y cinco al año.", "Cien al año.", "Cincuenta al año.", "Ciento cincuenta al año."],
  "Art. 33.1 RD 462/2002.", "no supere individualmente el máximo de setenta y cinco al año")

for cod, n, cat in [("P", 99, "Retribuciones básicas"), ("L", 72, "Retribuciones básicas"), ("L", 99, "Retribuciones complementarias"),
                    ("P", 100, "Interinos, prácticas y laborales"), ("X", 98, "Retribuciones diferidas y deducciones"), ("X", 99, "Retribuciones diferidas y deducciones"),
                    ("L", 73, "Indemnizaciones"), ("L", 71, "Indemnizaciones"), ("X", 79, "Indemnizaciones"), ("X", 80, "Indemnizaciones"),
                    ("L", 94, "Indemnizaciones"), ("P", 96, "Indemnizaciones")]:
    T.real(cod, n, cat)

# Flashcards
for q_, a_, cat in [
  ("¿Qué debe reflejar cada año la ley de presupuestos? (TREBEP, art. 21.1)", "Las cuantías de las retribuciones básicas, el incremento de las cuantías globales de las complementarias y el incremento de la masa salarial del personal laboral.", "Sistema retributivo"),
  ("Clases de retribuciones de los funcionarios de carrera (art. 22.1)", "Básicas y complementarias.", "Sistema retributivo"),
  ("¿Qué prohíbe el art. 22.5 TREBEP?", "Percibir participación en tributos o en otros ingresos de las Administraciones como contraprestación de un servicio, y participación o premio en multas.", "Sistema retributivo"),
  ("¿Desde cuándo producen efectos los derechos retributivos del TREBEP? (disposición final cuarta)", "Desde la entrada en vigor de las leyes de Función Pública de desarrollo, salvo el art. 25.2; hasta entonces, las normas vigentes en cada Administración (por eso se aplica la Ley 30/1984, arts. 23 y 24).", "Sistema retributivo"),
  ("¿Qué retribuyen las básicas? (art. 22.2)", "El Subgrupo o Grupo de adscripción del cuerpo o escala y la antigüedad en él.", "Retribuciones básicas"),
  ("Retribuciones básicas (art. 23)", "Única y exclusivamente sueldo y trienios; se fijan en la LPGE.", "Retribuciones básicas"),
  ("Trienio (art. 23 b)", "Cantidad igual para cada Subgrupo o Grupo por cada tres años de servicio.", "Retribuciones básicas"),
  ("Pagas extraordinarias en el TREBEP (art. 22.4)", "Dos al año; cada una, una mensualidad de básicas y de todas las complementarias salvo las del art. 24 c) y d).", "Retribuciones básicas"),
  ("Pagas extraordinarias en la Ley 30/1984 (art. 23.2 c)", "Retribución básica; dos al año, mínimo una mensualidad de sueldo y trienios; se devengan en junio y diciembre.", "Retribuciones básicas"),
  ("¿Qué retribuyen las complementarias? (art. 22.3)", "Las características de los puestos, la carrera profesional y el desempeño, rendimiento o resultados.", "Retribuciones complementarias"),
  ("Factores del art. 24 TREBEP", "a) progresión en la carrera; b) dificultad técnica, responsabilidad, dedicación, incompatibilidad o condiciones del puesto; c) interés, iniciativa, esfuerzo y rendimiento; d) servicios extraordinarios fuera de la jornada.", "Retribuciones complementarias"),
  ("Complementos de la Ley 30/1984 (art. 23.3)", "Destino (nivel del puesto), específico (condiciones particulares; uno por puesto), productividad (rendimiento; pública) y gratificaciones (nunca fijas y periódicas).", "Retribuciones complementarias"),
  ("Complemento de desempeño (RDL 6/2023)", "Retribuye el rendimiento o resultados según la evaluación del desempeño (art. 119.4); sustituirá al de productividad cuando se implante la evaluación (disposición transitoria séptima).", "Retribuciones complementarias"),
  ("¿Qué cobran los interinos? (art. 25)", "Básicas, pagas extraordinarias, complementarias del art. 24 b), c) y d) y las de la categoría de entrada; trienios por servicios previos (25.2).", "Interinos, prácticas y laborales"),
  ("Funcionarios en prácticas (art. 26)", "Como mínimo, el sueldo del Subgrupo o Grupo en que aspiren a ingresar.", "Interinos, prácticas y laborales"),
  ("Retribuciones diferidas (art. 29)", "Aportaciones a planes de pensiones de empleo o seguros colectivos con cobertura de jubilación, hasta el porcentaje de masa salarial que fije la LPGE.", "Retribuciones diferidas y deducciones"),
  ("Deducción de retribuciones (art. 30)", "Proporcional a la jornada no realizada, sin carácter sancionador y sin perjuicio de la sanción disciplinaria; en huelga, sin afectar a las prestaciones sociales.", "Retribuciones diferidas y deducciones"),
  ("Supuestos de indemnización (RD 462/2002, art. 1)", "Comisiones de servicio, desplazamientos en el término municipal, traslados de residencia y asistencias.", "Indemnizaciones"),
  ("Duración máxima de una comisión de servicio (art. 5)", "Salvo casos excepcionales, un mes en territorio nacional y tres en el extranjero; prorrogable por el tiempo estrictamente indispensable.", "Indemnizaciones"),
  ("Residencia eventual (arts. 6 y 16)", "Comisión que excede los límites del art. 5; máximo un año + prórroga de máximo un año; hasta el 80 % de las dietas enteras sin justificación.", "Indemnizaciones"),
  ("Día de salida en comisiones de más de 24 horas (art. 12.3 a)", "Alojamiento sí; manutención solo si sale antes de las 14 (100 %) o entre las 14 y las 22 (50 %).", "Indemnizaciones"),
  ("Traslado forzoso (art. 23.1)", "Gastos de viaje, transporte de mobiliario y enseres y tres dietas por el titular y cada familiar que se traslade.", "Indemnizaciones"),
  ("Límites anuales de las asistencias", "Órganos colegiados y consejos 40 %; tribunales 20 %; formación 25 % (y 75 horas); los tres juntos 50 %.", "Indemnizaciones"),
  ("¿A qué artículo de la clasificación económica se imputan las indemnizaciones por razón del servicio?", "Al artículo 23 (230 dietas, 231 locomoción, 232 traslado, 233 otras indemnizaciones).", "Indemnizaciones"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Retribuciones básicas", "Las que retribuyen al funcionario según el Subgrupo o Grupo de su cuerpo o escala y su antigüedad: sueldo y trienios (TREBEP, arts. 22.2 y 23).", "s4", "Retribuciones básicas")
T.glos("Trienio", "Cantidad igual para cada Subgrupo o Grupo por cada tres años de servicio (TREBEP, art. 23 b).", "s4", "Retribuciones básicas")
T.glos("Pagas extraordinarias", "Dos al año; en el TREBEP, una mensualidad de básicas y de las complementarias salvo las del art. 24 c) y d) (art. 22.4).", "s5", "Retribuciones básicas")
T.glos("Retribuciones complementarias", "Las que retribuyen las características del puesto, la carrera profesional o el desempeño (TREBEP, art. 22.3).", "s7", "Retribuciones complementarias")
T.glos("Complemento de destino", "Complemento correspondiente al nivel del puesto que se desempeñe (Ley 30/1984, art. 23.3 a).", "s8", "Retribuciones complementarias")
T.glos("Complemento específico", "Retribuye las condiciones particulares de algunos puestos (dificultad técnica, dedicación, responsabilidad, incompatibilidad, peligrosidad o penosidad); uno por puesto (Ley 30/1984, art. 23.3 b).", "s8", "Retribuciones complementarias")
T.glos("Complemento de productividad", "Retribuye el especial rendimiento, la actividad extraordinaria y el interés o iniciativa; cuantías de conocimiento público (Ley 30/1984, art. 23.3 c).", "s8", "Retribuciones complementarias")
T.glos("Complemento de desempeño", "En la Administración del Estado, retribuye el rendimiento o resultados según la evaluación del desempeño (RDL 6/2023, art. 119.4).", "s9", "Retribuciones complementarias")
T.glos("Retribución diferida", "Cantidades destinadas a planes de pensiones de empleo o seguros colectivos con cobertura de jubilación (TREBEP, art. 29).", "s11", "Retribuciones diferidas y deducciones")
T.glos("Comisión de servicio", "Cometido especial ordenado circunstancialmente y desempeñado fuera del término municipal de la residencia oficial (RD 462/2002, art. 3).", "s13", "Indemnizaciones")
T.glos("Residencia eventual", "Comisión que excede los límites del art. 5; se indemniza con hasta el 80 % de las dietas enteras (RD 462/2002, arts. 6 y 16).", "s13", "Indemnizaciones")
T.glos("Dieta", "Cantidad que se devenga diariamente por la estancia fuera de la residencia oficial en las comisiones del art. 5 (RD 462/2002, art. 9.1).", "s14", "Indemnizaciones")
T.glos("Asistencia", "Indemnización por concurrir a órganos colegiados o consejos de administración, participar en tribunales o colaborar en formación (RD 462/2002, art. 27).", "s16", "Indemnizaciones")

# Cronología (fechas de los metadatos del BOE)
T.hito("1984", "Ley 30/1984, de 2 de agosto, de medidas para la reforma de la Función Pública (BOE de 3-8-1984)", "Arts. 23 y 24: conceptos retributivos y su cuantía", "normativo", "s6")
T.hito("2002", "Real Decreto 462/2002, de 24 de mayo, sobre indemnizaciones por razón del servicio (BOE de 30-5-2002)", "Comisiones, dietas, traslados y asistencias", "normativo", "s12")
T.hito("2014", "Resolución de 20 de enero de 2014, de la Dirección General de Presupuestos (BOE de 29-1-2014)", "Clasificación económica: artículo 23, indemnizaciones por razón del servicio", "normativo", "s17")
T.hito("2015", "Real Decreto Legislativo 5/2015, de 30 de octubre, texto refundido del Estatuto Básico del Empleado Público (BOE de 31-10-2015)", "Arts. 21 a 30: derechos retributivos", "normativo", "s1")
T.hito("2023", "Real Decreto-ley 6/2023, de 19 de diciembre (BOE de 20-12-2023)", "Libro segundo: complemento de desempeño y complemento de carrera en la Administración del Estado", "normativo", "s9")

T.publicar()
