# -*- coding: utf-8 -*-
"""Tema V.1 (B5T01): El personal al servicio de las Administraciones públicas: concepto
y clases. Adquisición y pérdida de la relación de servicio. Régimen jurídico.
Método del I.2: mapa → bloques (I a III) con guía; cada artículo, texto literal del
BOE + ficha de casillas fijas; cierre 1 (preguntas oficiales) y cierre 2 (repaso).
Normas (textos consolidados del BOE): TREBEP (RDLeg 5/2015), arts. 1 a 13 y 62 a 68,
DA 17.ª, disposición derogatoria única y disposiciones finales primera y cuarta;
CE, arts. 23.2, 103.3 y 149.1.18.ª; Ley 30/1984, arts. 1 y 15.1 c); RD 364/1995, art. 25;
RD 707/1979, art. 1."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO["L30"] = "Ley 30/1984"
CORTO["RD364"] = "RD 364/1995"
CORTO["RD707"] = "RD 707/1979"
TB = "TREBEP"

T = Tema("B5T01",
  "Tres preguntas: I. Quién es empleado público y qué clases hay (TREBEP, arts. 8 a 13) · II. Cómo se adquiere y cómo se pierde la condición de funcionario (TREBEP, arts. 62 a 68) · III. Qué normas rigen al personal: el régimen jurídico (CE, arts. 23.2, 103.3 y 149.1.18.ª; TREBEP, arts. 1 a 7; Ley 30/1984 en la AGE). Cada artículo: texto literal del BOE y ficha.",
  ["TREBEP", "Empleados públicos", "Art. 8", "Funcionarios de carrera", "Funcionarios interinos", "Art. 10", "Personal laboral", "Personal eventual", "Personal directivo", "Adquisición", "Art. 62", "Pérdida", "Renuncia", "Jubilación", "Rehabilitación", "Ámbito de aplicación", "Art. 7"])

# =============================================================================
T.ap("s0", "Mapa del tema: tres preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque V, tema 1):
> El personal al servicio de las Administraciones públicas: concepto y clases. Adquisición y pérdida de la relación de servicio. Régimen jurídico.

### El hilo conductor

El epígrafe se lee como **tres preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | TREBEP (RDLeg 5/2015) | Otras normas |
|---|---|---|---|
| **I** | ¿Quién es empleado público y qué clases hay? (concepto y clases) | Arts. 8 a 13; disposición adicional decimoséptima | Ley 30/1984, art. 15.1 c) (AGE) |
| **II** | ¿Cómo se adquiere y cómo se pierde la condición de funcionario? (relación de servicio) | Arts. 62 a 68 | RD 364/1995, art. 25; RD 707/1979, art. 1 |
| **III** | ¿Qué normas rigen al personal? (régimen jurídico) | Arts. 1 a 7; disposición derogatoria única; disposiciones finales primera y cuarta | CE, arts. 23.2, 103.3 y 149.1.18.ª; Ley 30/1984, art. 1 |

!> **La idea que une los tres bloques:** el TREBEP define **quién** trabaja para la Administración y con qué **vínculo** (I: nombramiento de funcionario de carrera o interino, contrato laboral, nombramiento de eventual); para los funcionarios de carrera fija **cómo nace y cómo termina** esa relación (II); y todo ello descansa en un **régimen jurídico** de varias capas: Constitución, TREBEP como norma básica, leyes de Función Pública y, en la AGE, la Ley 30/1984 en lo no derogado (III).

### Cómo está escrito

- Se sigue el orden del epígrafe (concepto y clases → adquisición y pérdida → régimen jurídico) y, dentro de cada bloque, el orden de los artículos.
- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen; para el derecho del art. 23.2 CE: Titulares · Contenido · Límites · Protección · ⚠ Ojo en el examen).
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- Fronteras: derechos, deberes y régimen disciplinario (tema V.2); selección y oferta de empleo (tema V.3); provisión y carrera (tema V.4); situaciones administrativas (tema V.5); personal laboral y convenio (tema V.7); Seguridad Social y clases pasivas (tema V.9).
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Quién es empleado público y qué clases hay? (TREBEP, arts. 8 a 13)", donde(
  "Primera pregunta del tema. Antes de ver cómo se entra y se sale de la función pública, hay que saber **quién** es empleado público y **qué clases** distingue el TREBEP, porque cada clase tiene un vínculo distinto con la Administración.",
  ["1 Concepto y clases de empleados públicos (art. 8)", "2 Funcionarios de carrera (art. 9)", "3 Funcionarios interinos (art. 10 y disposición adicional decimoséptima)", "4 Personal laboral (art. 11; Ley 30/1984, art. 15.1 c)", "5 Personal eventual (art. 12)", "6 Personal directivo profesional (art. 13)", "7 Cuadro de las clases de personal"]))

T.ap("s1", "I.1 Concepto y clases de empleados públicos (art. 8)", f"""
El TREBEP da un concepto **único** de empleado público y lo divide en **cuatro clases**. El personal directivo (art. 13) no es una quinta clase del art. 8 (→ I.6).

{unidad("1.1 Concepto y clasificación (art. 8)",
  lit(TB, "Artículo 8", ["funciones retribuidas en las Administraciones Públicas al servicio de los intereses generales", "Funcionarios de carrera", "Funcionarios interinos", "ya sea fijo, por tiempo indefinido o temporal", "Personal eventual"]),
  fichab("Concepto legal de empleado público y sus clases",
         f"{c(TB, 'Artículo 8', 'quienes desempeñan funciones retribuidas en las Administraciones Públicas al servicio de los intereses generales')}",
         ["::Cuatro clases (8.2):", "Funcionarios de carrera (→ I.2)", "Funcionarios interinos (→ I.3)", "Personal laboral, fijo, por tiempo indefinido o temporal (→ I.4)", "Personal eventual (→ I.5)"],
         "—",
         "Tres notas del concepto: funciones **retribuidas**, **en las Administraciones Públicas** y **al servicio de los intereses generales**. Son **cuatro** clases; el personal laboral puede ser **fijo, por tiempo indefinido o temporal**. El personal **directivo** no figura en la lista del art. 8.2."))}
""", 2)

T.ap("s2", "I.2 Funcionarios de carrera (art. 9)", f"""
{unidad("2.1 Concepto (art. 9.1)",
  lit(TB, "Artículo 9", ["en virtud de nombramiento legal", "relación estatutaria regulada por el Derecho Administrativo", "de carácter permanente"], solo=[1]),
  fichab("Funcionario de carrera: vínculo estatutario y permanente",
         f"Quienes están vinculados {c(TB, 'Artículo 9', 'a una Administración Pública')}",
         [f"::Tres rasgos:", f"Origen: {c(TB, 'Artículo 9', 'en virtud de nombramiento legal')} (no por contrato)", f"Vínculo: {c(TB, 'Artículo 9', 'una relación estatutaria regulada por el Derecho Administrativo')}", f"Servicios: {c(TB, 'Artículo 9', 'servicios profesionales retribuidos de carácter permanente')}"],
         "Carácter **permanente** (frente al temporal del interino, → I.3)",
         "Relación **estatutaria** y regida por el **Derecho Administrativo** (no laboral); nace del **nombramiento**, no de un contrato. Cómo se adquiere y se pierde la condición: → II.1 y → II.2."))}

{unidad("2.2 Funciones reservadas a los funcionarios (art. 9.2)",
  lit(TB, "Artículo 9", ["participación directa o indirecta en el ejercicio de las potestades públicas", "salvaguardia de los intereses generales del Estado y de las Administraciones Públicas", "exclusivamente a los funcionarios públicos"], solo=[2]),
  fichab("Reserva de funciones a los funcionarios públicos",
         c(TB, "Artículo 9", "corresponden exclusivamente a los funcionarios públicos"),
         ["::Funciones reservadas:", "Las que impliquen participación directa o indirecta en el ejercicio de las potestades públicas", "Las de salvaguardia de los intereses generales del Estado y de las Administraciones Públicas"],
         f"{c(TB, 'Artículo 9', 'en los términos que en la ley de desarrollo de cada Administración Pública se establezca')}",
         "Reserva **exclusiva** («En todo caso») a los **funcionarios públicos**. Participación **directa o indirecta**. Es el límite que deben respetar las leyes al fijar los puestos del personal laboral (art. 11.2 → I.4.1)."))}
""", 2)

T.ap("s3", "I.3 Funcionarios interinos (art. 10 y disposición adicional decimoséptima)", f"""
El art. 10 es el que **más se pregunta** del bloque: concepto, **cuatro supuestos** con sus plazos, selección, causas de cese y el límite de **tres años** en vacante.

{unidad("3.1 Concepto y supuestos de nombramiento (art. 10.1)",
  lit(TB, "Artículo 10", ["razones expresamente justificadas de necesidad y urgencia", "con carácter temporal para el desempeño de funciones propias de funcionarios de carrera", "por un máximo de tres años", "durante el tiempo estrictamente necesario", "no podrán tener una duración superior a tres años, ampliable hasta doce meses más", "por plazo máximo de nueve meses, dentro de un periodo de dieciocho meses"], solo=[1, 2, 3, 4, 5]),
  fichab("Funcionario interino: nombramiento temporal para funciones propias de funcionarios de carrera",
         f"Nombrados {c(TB, 'Artículo 10', 'por razones expresamente justificadas de necesidad y urgencia')}",
         ["::Solo en cuatro supuestos (10.1):", "a) Plazas **vacantes** que no puedan cubrir funcionarios de carrera", "b) **Sustitución** transitoria de los titulares", "c) Ejecución de **programas** de carácter temporal", "d) **Exceso o acumulación** de tareas"],
         ["::Plazos máximos:", "a) Vacante: máximo **tres años** (→ I.3.4)", "b) Sustitución: el tiempo **estrictamente necesario**", "c) Programas: **tres años**, ampliable **doce meses** más por las leyes de Función Pública", "d) Acumulación de tareas: **nueve meses** dentro de un periodo de **dieciocho**"],
         "Temporal + funciones **propias** de funcionarios de carrera (no «que no sean propias»). Necesidad **y** urgencia, **expresamente justificadas**. Cuadro de plazos: 3 años / tiempo estrictamente necesario / 3 años + 12 meses / 9 meses en 18. Cayó dos veces en 2025 (→ Cierre 1)."))}

{unidad("3.2 Selección (art. 10.2)",
  lit(TB, "Artículo 10", ["igualdad, mérito, capacidad, publicidad y celeridad", "cobertura inmediata del puesto", "en ningún caso dará lugar al reconocimiento de la condición de funcionario de carrera"], solo=[6]),
  fichab("Procedimientos de selección del interino",
         "La Administración que nombra (el nombramiento en la AGE, en el tema V.3)",
         f"Procedimientos {c(TB, 'Artículo 10', 'serán públicos')}, con los principios de {c(TB, 'Artículo 10', 'igualdad, mérito, capacidad, publicidad y celeridad')}",
         f"Finalidad: {c(TB, 'Artículo 10', 'la cobertura inmediata del puesto')}",
         "Cinco principios: igualdad, mérito, capacidad, publicidad **y celeridad**. El nombramiento **nunca** da la condición de funcionario de carrera."))}

{unidad("3.3 Fin de la interinidad (art. 10.3)",
  lit(TB, "Artículo 10", ["formalizará de oficio", "además de por las previstas en el artículo 63, sin derecho a compensación alguna", "Por la cobertura reglada del puesto por personal funcionario de carrera", "supresión o a la amortización de los puestos asignados", "Por la finalización del plazo autorizado expresamente recogido en su nombramiento", "Por la finalización de la causa que dio lugar a su nombramiento"], solo=[7, 8, 9, 10, 11]),
  fichab("Causas de finalización de la relación de interinidad",
         f"{c(TB, 'Artículo 10', 'la Administración formalizará de oficio la finalización')}",
         ["::Además de las causas del art. 63 (→ II.2.1):", "a) Cobertura reglada del puesto por funcionario de carrera", "b) Razones organizativas: supresión o amortización de los puestos", "c) Fin del plazo autorizado en el nombramiento", "d) Fin de la causa que dio lugar al nombramiento"],
         c(TB, "Artículo 10", "sin derecho a compensación alguna"),
         "**De oficio** y **sin compensación**. Al interino también le alcanzan las causas de pérdida del art. **63** (renuncia, nacionalidad, jubilación, separación, inhabilitación)."))}

{unidad("3.4 El límite de tres años en vacante (art. 10.4)",
  lit(TB, "Artículo 10", ["mecanismos de provisión o movilidad", "transcurridos tres años desde el nombramiento", "salvo que el correspondiente proceso selectivo quede desierto", "siempre que se haya publicado la correspondiente convocatoria dentro del plazo de los tres años", "sin que su cese dé lugar a compensación económica"], solo=[12, 13, 14]),
  fichab("Duración máxima del interino nombrado por vacante (supuesto 10.1 a)",
         "La Administración (cobertura de la vacante); el interino (permanencia excepcional)",
         ["La vacante se cubre por los mecanismos de provisión o movilidad de cada Administración", "A los **tres años** desde el nombramiento: **fin** de la interinidad; la vacante, solo para funcionario de carrera", "Salvo proceso selectivo **desierto**: cabe otro nombramiento de interino", "Excepción: si la convocatoria se publicó **dentro** de los tres años, puede seguir hasta su **resolución** (plazos del art. 70), sin compensación"],
         "**Tres años** desde el nombramiento",
         "Los tres años se cuentan **desde el nombramiento**. La permanencia excepcional exige convocatoria **publicada** dentro de ese plazo; el cese posterior **no** da compensación económica."))}

{unidad("3.5 Régimen aplicable (art. 10.5)",
  lit(TB, "Artículo 10", ["el régimen general del personal funcionario de carrera en cuanto sea adecuado a la naturaleza de su condición temporal", "salvo aquellos derechos inherentes a la condición de funcionario de carrera"], solo=[15]),
  fichab("Qué régimen se aplica al interino",
         "Personal funcionario interino",
         "Régimen general del funcionario de carrera, en lo adecuado a su condición **temporal** y al carácter **extraordinario y urgente** de su nombramiento",
         "—",
         "Se le aplica el régimen de los funcionarios de carrera **en cuanto sea adecuado**, **salvo** los derechos **inherentes** a la condición de funcionario de carrera."))}

{unidad("3.6 Control de la temporalidad (disposición adicional decimoséptima)",
  lit(TB, "da", ["nulo de pleno derecho", "veinte días de sus retribuciones fijas por año de servicio", "hasta un máximo de doce mensualidades", "No habrá derecho a compensación en caso de que la finalización de la relación de servicio sea por causas disciplinarias ni por renuncia voluntaria"], solo=[1, 3, 4, 5], titulo="Disposición adicional decimoséptima. Medidas dirigidas al control de la temporalidad en el empleo público (TREBEP)"),
  fichab("Consecuencias del incumplimiento de los plazos máximos de permanencia como personal temporal",
         "Las Administraciones Públicas (responsables de evitar irregularidades); el personal funcionario interino afectado (compensación)",
         ["Actos, pactos, acuerdos o reglamentos que supongan incumplir los plazos máximos: **nulos de pleno derecho**", "Actuaciones irregulares: exigencia de responsabilidades", "Interino afectado: compensación económica"],
         ["::Compensación (apartado 4):", "**Veinte días** de retribuciones fijas por año de servicio", "Prorrateo por meses de los periodos inferiores a un año", "Máximo **doce mensualidades**", "Nace en la fecha del **cese efectivo**"],
         "Sin compensación si el fin es por **causas disciplinarias** o por **renuncia voluntaria**. La compensación por **incumplir** el plazo máximo (DA 17.ª) no contradice el «sin derecho a compensación alguna» del cese ordinario (10.3)."))}
""", 2)

T.ap("s4", "I.4 Personal laboral (art. 11; Ley 30/1984, art. 15.1 c)", f"""
{unidad("4.1 Concepto, puestos y selección (art. 11)",
  lit(TB, "Artículo 11", ["en virtud de contrato de trabajo formalizado por escrito", "fijo, por tiempo indefinido o temporal", "respetando en todo caso lo establecido en el artículo 9.2", "igualdad, mérito y capacidad", "principio de celeridad"]),
  fichab("Personal laboral: vínculo contractual con la Administración",
         f"Quien {c(TB, 'Artículo 11', 'presta servicios retribuidos por las Administraciones Públicas')} en virtud de contrato",
         [f"Contrato {c(TB, 'Artículo 11', 'formalizado por escrito')}, en cualquiera de las modalidades de la legislación laboral", "Según la duración: fijo, por tiempo indefinido o temporal", "Las leyes de Función Pública fijan los criterios de los puestos que puede desempeñar, respetando el art. 9.2 (→ I.2.2)", f"Selección: procedimientos públicos con {c(TB, 'Artículo 11', 'los principios de igualdad, mérito y capacidad')}; el temporal, también con **celeridad**"],
         "—",
         "**Contrato** (no nombramiento) **formalizado por escrito**. Selección: igualdad, mérito y capacidad (sin «publicidad y celeridad» del interino, salvo la **celeridad** del laboral **temporal**). Su régimen jurídico: art. 7 (→ III.4.2); convenio y detalle, en el tema V.7."))}

{unidad("4.2 Qué puestos puede ocupar en la AGE (Ley 30/1984, art. 15.1 c)",
  lit("L30", "aquince", ["serán desempeñados por funcionarios públicos", "podrán desempeñarse por personal laboral"], solo=[4, 5, 6, 7, 8, 9, 10, 11]),
  fichab("Regla y excepciones en los puestos de la Administración del Estado",
         "Administración del Estado y sus Organismos Autónomos; Entidades Gestoras y Servicios Comunes de la Seguridad Social",
         ["::Regla: puestos desempeñados por **funcionarios públicos**. Excepciones (pueden ser de personal laboral):", "Puestos no permanentes y de necesidades periódicas y discontinuas", "Oficios, vigilancia, custodia, porteo y análogos", "Puestos instrumentales de mantenimiento y conservación, artes gráficas, encuestas, protección civil, comunicación social, expresión artística, servicios sociales y protección de menores", "Conocimientos técnicos especializados sin Cuerpos o Escalas con la preparación necesaria", "Puestos en el extranjero con funciones administrativas de trámite y colaboración y auxiliares", "Funciones auxiliares de carácter instrumental y apoyo administrativo"],
         "—",
         "La regla general en la AGE es el **funcionario**; el laboral es la **excepción** tasada. El art. 15 de la Ley 30/1984 **no** figura entre los artículos que deroga el TREBEP (→ III.5.3)."))}
""", 2)

T.ap("s5", "I.5 Personal eventual (art. 12)", f"""
{unidad("5.1 Concepto, nombramiento y cese (art. 12)",
  lit(TB, "Artículo 12", ["con carácter no permanente", "confianza o asesoramiento especial", "El número máximo se establecerá por los respectivos órganos de gobierno", "El nombramiento y cese serán libres", "cuando se produzca el de la autoridad a la que se preste la función de confianza o asesoramiento", "no podrá constituir mérito para el acceso a la Función Pública o para la promoción interna"]),
  fichab("Personal eventual: confianza o asesoramiento especial",
         f"Nombrado {c(TB, 'Artículo 12', 'en virtud de nombramiento y con carácter no permanente')}; los órganos de gobierno que pueden tenerlo los fijan las leyes de Función Pública",
         [f"Solo {c(TB, 'Artículo 12', 'funciones expresamente calificadas como de confianza o asesoramiento especial')}", "Retribuido con cargo a los créditos presupuestarios consignados para este fin", "Nombramiento y cese **libres**; cese automático con el de la autoridad a la que sirve", "Régimen general de los funcionarios de carrera en lo adecuado a su naturaleza"],
         "Número máximo: lo fijan los **órganos de gobierno**; número y condiciones retributivas, **públicos**",
         "Ser eventual **no es mérito** para el acceso ni para la promoción interna. El cese es **libre** y, **en todo caso**, cuando cesa la autoridad a la que presta la confianza."))}
""", 2)

T.ap("s6", "I.6 Personal directivo profesional (art. 13)", f"""
{unidad("6.1 Principios de su régimen (art. 13)",
  lit(TB, "Artículo 13", ["El Gobierno y los órganos de gobierno de las comunidades autónomas podrán establecer", "funciones directivas profesionales", "principios de mérito y capacidad y a criterios de idoneidad", "publicidad y concurrencia", "eficacia y eficiencia, responsabilidad por su gestión y control de resultados", "no tendrá la consideración de materia objeto de negociación colectiva", "relación laboral de carácter especial de alta dirección"]),
  fichab("Personal directivo profesional",
         f"Regulan su régimen {c(TB, 'Artículo 13', 'El Gobierno y los órganos de gobierno de las comunidades autónomas')}; es directivo quien desarrolla funciones directivas profesionales definidas en las normas de cada Administración",
         ["Designación: **mérito y capacidad** + **idoneidad**, con procedimientos que garanticen **publicidad y concurrencia**", "Evaluación: eficacia y eficiencia, responsabilidad por su gestión y control de resultados según objetivos", "Condiciones de empleo: **no** son materia de negociación colectiva", "Si es personal laboral: relación laboral especial de **alta dirección**"],
         "—",
         "No es una clase del art. 8.2 (→ I.1.1). Sus condiciones **no se negocian** colectivamente. Si es laboral, **alta dirección**. Regulan su régimen el **Gobierno** y los órganos de gobierno de las **comunidades autónomas** («podrán»)."))}
""", 2)

T.ap("s7", "I.7 Cuadro de las clases de personal (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Clase | Artículo | Vínculo | Duración | Funciones | Selección o designación |
|---|---|---|---|---|---|
| Funcionario de carrera | 9 | Nombramiento legal; relación **estatutaria** (Derecho Administrativo) | **Permanente** | Servicios profesionales; en exclusiva, las del 9.2 | Proceso selectivo (→ II.1; tema V.3) |
| Funcionario interino | 10 | Nombramiento | **Temporal** (supuestos y plazos del 10.1) | **Propias** de funcionarios de carrera | Igualdad, mérito, capacidad, publicidad y **celeridad** |
| Personal laboral | 11 | **Contrato** de trabajo por escrito | Fijo, por tiempo indefinido o temporal | Puestos que fijen las leyes de Función Pública (en la AGE, art. 15.1 c Ley 30/1984) | Igualdad, mérito y capacidad (+ celeridad, el temporal) |
| Personal eventual | 12 | Nombramiento **libre** | **No permanente** | Solo **confianza o asesoramiento especial** | Libre; cesa con su autoridad |
| Personal directivo (fuera del 8.2) | 13 | Según su régimen; si es laboral, **alta dirección** | — | Funciones directivas profesionales | Mérito, capacidad e idoneidad; publicidad y concurrencia |

{resumen([
  "Empleado público: funciones **retribuidas**, en las Administraciones Públicas, **al servicio de los intereses generales**; cuatro clases (art. 8).",
  "Carrera: **nombramiento legal**, relación **estatutaria**, servicios **permanentes**; reserva **exclusiva** de las potestades públicas (art. 9).",
  "Interino: **necesidad y urgencia**, **temporal**, funciones **propias** de carrera; vacante 3 años, sustitución el tiempo estrictamente necesario, programas 3 años + 12 meses, tareas 9 meses en 18 (art. 10).",
  "Laboral: **contrato** por escrito; eventual: **confianza o asesoramiento**, cese libre y no es mérito; directivo: mérito, capacidad e idoneidad, sin negociación colectiva (arts. 11 a 13)."],
  "Siguiente: II. ¿Cómo se adquiere y cómo se pierde la condición de funcionario?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Cómo se adquiere y cómo se pierde la condición de funcionario? (TREBEP, arts. 62 a 68)", donde(
  "Segunda pregunta. Ya sabemos qué es un funcionario de carrera; ahora, **cómo nace** su relación de servicio (cuatro requisitos sucesivos), **cómo se extingue** (cinco causas) y **cuándo puede recuperarse** (rehabilitación).",
  ["1 Adquisición: cuatro requisitos sucesivos (art. 62; RD 364/1995, art. 25; RD 707/1979)", "2 Las cinco causas de pérdida (art. 63)", "3 Cada causa: renuncia, nacionalidad, inhabilitación y jubilación (arts. 64 a 67)", "4 Rehabilitación (art. 68) y cuadro"]))

T.ap("s8", "II.1 Adquisición de la condición de funcionario de carrera (art. 62; RD 364/1995, art. 25; RD 707/1979)", f"""
{unidad("1.1 Los cuatro requisitos (art. 62)",
  lit(TB, "Artículo 62", ["cumplimiento sucesivo", "Superación del proceso selectivo", "que será publicado en el Diario Oficial correspondiente", "Acto de acatamiento de la Constitución", "Toma de posesión dentro del plazo que se establezca", "quedarán sin efecto las actuaciones relativas a quienes no acrediten"]),
  fichab("Cómo nace la relación de servicio del funcionario de carrera",
         "El aspirante; nombra el **órgano o autoridad competente**",
         ["::Por este orden («cumplimiento sucesivo»):", "a) Superación del proceso selectivo (tema V.3)", "b) Nombramiento por el órgano o autoridad competente, **publicado** en el Diario Oficial correspondiente", "c) Acatamiento de la Constitución y, en su caso, del Estatuto de Autonomía y del resto del Ordenamiento Jurídico", "d) Toma de posesión"],
         ["Toma de posesión: **dentro del plazo que se establezca** (el art. 62 no fija cuál)", "Sin acreditar requisitos tras el proceso selectivo: **no** pueden ser funcionarios y sus actuaciones **quedan sin efecto** (62.2)"],
         "Son **cuatro** requisitos **sucesivos**. Ni contrato ni alta en nómina: el vínculo nace del **nombramiento**, no de un contrato (eso es del personal laboral, → I.4.1). Cayó en 2025 (→ Cierre 1)."))}

{unidad("1.2 El nombramiento en la AGE (RD 364/1995, art. 25)",
  lit("RD364", "Artículo 25", ["no podrá exceder en ningún caso al de plazas convocadas", "por el Secretario de Estado para la Administración Pública", "será nula de pleno derecho", "deberán publicarse en el «Boletín Oficial del Estado»"]),
  fichab("Nombramiento de los funcionarios de carrera de la Administración General del Estado",
         f"Nombra {c('RD364', 'Artículo 25', 'el Secretario de Estado para la Administración Pública')} (denominación literal del reglamento)",
         "Concluido el proceso selectivo, a los aspirantes que lo hayan superado",
         ["Número de nombrados: **nunca** superior al de plazas convocadas", "Publicación en el **BOE**"],
         "Nombrar a más aspirantes que plazas convocadas es **nulo de pleno derecho**. El Diario Oficial del art. 62.1 b) es, en la AGE, el **BOE**."))}

{unidad("1.3 El juramento o promesa en la toma de posesión (RD 707/1979, art. 1)",
  lit("RD707", "aprimero", ["con una simple afirmativa", "guardar y hacer guardar la Constitución como norma fundamental del Estado"], titulo="Artículo primero (Real Decreto 707/1979, de 5 de abril, por el que se establece la fórmula de juramento en cargos y funciones públicas)"),
  fichab("Fórmula de juramento o promesa en la toma de posesión de cargos o funciones públicas",
         f"{c('RD707', 'aprimero', 'quien haya de dar posesión')} pregunta; contesta {c('RD707', 'aprimero', 'quien haya de tomar posesión')}",
         ["Pregunta de quien da posesión y respuesta con **una simple afirmativa**", "O bien juramento o promesa prestado **personalmente** por quien toma posesión"],
         "—",
         "**Jurar o prometer**: las dos fórmulas valen. El contenido: cumplir fielmente las obligaciones del cargo **con lealtad al Rey** y **guardar y hacer guardar la Constitución**."))}
""", 2)

T.ap("s9", "II.2 Las cinco causas de pérdida (art. 63)", f"""
{unidad("2.1 Lista cerrada de causas (art. 63)",
  lit(TB, "Artículo 63", ["La renuncia a la condición de funcionario", "La pérdida de la nacionalidad", "La jubilación total del funcionario", "que tuviere carácter firme", "inhabilitación absoluta o especial para cargo público"]),
  fichab("Causas de pérdida de la condición de funcionario de carrera",
         "El funcionario de carrera (y, además de las del art. 10.3, el interino → I.3.3)",
         ["a) Renuncia (→ II.3.1)", "b) Pérdida de la nacionalidad (→ II.3.2)", "c) Jubilación **total** (→ II.3.4)", "d) Sanción disciplinaria **firme** de separación del servicio (tema V.2)", "e) Pena principal o accesoria **firme** de inhabilitación absoluta o especial para cargo público (→ II.3.3)"],
         "Separación e inhabilitación: solo si son **firmes**",
         "Son **cinco**. La jubilación ha de ser **total**. La separación y la inhabilitación exigen **firmeza**. Las situaciones administrativas (excedencia, suspensión…) **no** hacen perder la condición (tema V.5)."))}
""", 2)

T.ap("s10", "II.3 Cada causa: renuncia, nacionalidad, inhabilitación y jubilación (arts. 64 a 67)", f"""
{unidad("3.1 Renuncia (art. 64)",
  lit(TB, "Artículo 64", ["habrá de ser manifestada por escrito y será aceptada expresamente por la Administración", "esté sujeto a expediente disciplinario", "auto de procesamiento o de apertura de juicio oral", "no inhabilita para ingresar de nuevo"]),
  fichab("Renuncia voluntaria a la condición de funcionario",
         "La manifiesta el funcionario; la acepta la Administración",
         [f"{c(TB, 'Artículo 64', 'manifestada por escrito')}", f"{c(TB, 'Artículo 64', 'aceptada expresamente por la Administración')}"],
         ["::No puede aceptarse (64.2) si el funcionario:", "Está sujeto a expediente disciplinario", "Tiene dictado auto de procesamiento o de apertura de juicio oral por algún delito"],
         "**Por escrito** + aceptación **expresa**. **No** inhabilita para volver a ingresar por el procedimiento de selección establecido. Cayó en 2025 (→ Cierre 1)."))}

{unidad("3.2 Pérdida de la nacionalidad (art. 65)",
  lit(TB, "Artículo 65", ["que haya sido tenida en cuenta para el nombramiento", "salvo que simultáneamente se adquiera la nacionalidad de alguno de dichos Estados"]),
  fichab("Pérdida de la nacionalidad como causa de pérdida de la condición de funcionario",
         "Funcionario cuya nacionalidad (española, de otro Estado miembro de la UE o de un Estado con libre circulación de trabajadores por tratado) se tuvo en cuenta para el nombramiento",
         "Determina la pérdida de la condición de funcionario",
         "—",
         "Solo cuenta la nacionalidad **tenida en cuenta para el nombramiento**. No se pierde la condición si **simultáneamente** se adquiere la de otro de esos Estados. Es causa que admite **rehabilitación** a solicitud (→ II.4.1)."))}

{unidad("3.3 Pena de inhabilitación (art. 66)",
  lit(TB, "Artículo 66", ["respecto a todos los empleos o cargos que tuviere", "respecto de aquellos empleos o cargos especificados en la sentencia"]),
  fichab("Efectos de la inhabilitación penal firme",
         "El funcionario condenado por sentencia firme",
         ["Inhabilitación **absoluta**: pérdida respecto a **todos** los empleos o cargos", "Inhabilitación **especial**: pérdida respecto de los empleos o cargos **especificados en la sentencia**"],
         "Desde que **adquiere firmeza** la sentencia",
         "Pena **principal o accesoria**, da igual. Absoluta → **todos**; especial → los **de la sentencia**. Rehabilitación solo **excepcional** (→ II.4.1)."))}

{unidad("3.4 Jubilación (art. 67)",
  lit(TB, "Artículo 67", ["Voluntaria, a solicitud del funcionario", "Forzosa, al cumplir la edad legalmente establecida", "incapacidad permanente para el ejercicio de las funciones propias de su cuerpo o escala", "los sesenta y cinco años de edad", "como máximo hasta que se cumpla setenta años de edad", "de forma motivada", "sin coeficiente reductor por razón de la edad"]),
  fichab("Las tres clases de jubilación del funcionario",
         "El funcionario (voluntaria, a solicitud); la Administración (forzosa, de oficio)",
         ["::Clases (67.1):", "a) **Voluntaria**: a solicitud, si reúne los requisitos de su Régimen de Seguridad Social", "b) **Forzosa**: al cumplir la edad legal, declarada **de oficio**", "c) Por **incapacidad permanente** para las funciones de su cuerpo o escala, o por pensión de incapacidad permanente absoluta o total"],
         ["Forzosa: **65 años** (67.3)", "Prolongación: máximo hasta los **70**, en los términos de las leyes de Función Pública; resolución **motivada**", "Funcionarios del **Régimen General** de la Seguridad Social: la edad de la pensión contributiva **sin coeficiente reductor** (67.4)"],
         "**65** de oficio, prolongable hasta **70** (a solicitud; la Administración resuelve motivadamente). Excluidos de esas reglas quienes tengan normas estatales específicas de jubilación. Seguridad Social y clases pasivas: tema V.9."))}
""", 2)

T.ap("s11", "II.4 Rehabilitación (art. 68) y cuadro de la relación de servicio", f"""
{unidad("4.1 Rehabilitación de la condición de funcionario (art. 68)",
  lit(TB, "Artículo 68", ["pérdida de la nacionalidad o jubilación por incapacidad permanente para el servicio", "que le será concedida", "con carácter excepcional", "atendiendo a las circunstancias y entidad del delito cometido", "se entenderá desestimada la solicitud"]),
  fichab("Recuperación de la condición de funcionario perdida",
         ["El interesado la solicita", "La conceden: en los supuestos del 68.1, la Administración (reglada: «le será concedida»); en el del 68.2, los **órganos de gobierno**"],
         ["::Dos supuestos:", "68.1: pérdida de la **nacionalidad** o jubilación por **incapacidad permanente**, desaparecida la causa objetiva → se **concede**", "68.2: condena a **inhabilitación** → **excepcional**, atendiendo a las circunstancias y entidad del delito"],
         "68.2: sin resolución expresa en plazo, **desestimada** (silencio negativo)",
         "Nacionalidad e incapacidad: rehabilitación **debida** a solicitud. Inhabilitación: **excepcional** y con silencio **negativo**. No hay rehabilitación prevista para la renuncia (puede volver a ingresar por selección, → II.3.1) ni para la separación."))}

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Causa de pérdida (art. 63) | Regla clave | ¿Rehabilitación (art. 68)? |
|---|---|---|
| a) Renuncia | Por escrito y aceptada expresamente; no si hay expediente disciplinario, procesamiento o apertura de juicio oral (64) | No prevista; puede volver a ingresar por selección (64.3) |
| b) Pérdida de la nacionalidad | La tenida en cuenta para el nombramiento; salvo adquisición simultánea de otra de esos Estados (65) | **Sí**, a solicitud, desaparecida la causa (68.1) |
| c) Jubilación total | Voluntaria, forzosa (65 años; prolongación hasta 70) o por incapacidad permanente (67) | **Sí**, solo la de **incapacidad permanente** (68.1) |
| d) Separación del servicio firme | Sanción disciplinaria (tema V.2) | No prevista |
| e) Inhabilitación firme | Absoluta: todos los cargos; especial: los de la sentencia (66) | **Excepcional**; silencio negativo (68.2) |

{resumen([
  "Adquisición: **cuatro** requisitos **sucesivos**: proceso selectivo, **nombramiento** publicado, **acatamiento** y **toma de posesión** en plazo (art. 62). En la AGE nombra el Secretario de Estado y se publica en el **BOE** (RD 364/1995, art. 25).",
  "Pérdida: **cinco** causas: renuncia, nacionalidad, jubilación **total**, separación **firme** e inhabilitación **firme** (art. 63).",
  "Renuncia **por escrito** y **aceptada expresamente**; no impide volver a ingresar (art. 64). Jubilación forzosa a los **65**, prolongable hasta los **70** (art. 67).",
  "Rehabilitación: **concedida** tras nacionalidad o incapacidad; **excepcional** tras inhabilitación, con silencio **negativo** (art. 68)."],
  "Siguiente: III. ¿Qué normas rigen al personal? El régimen jurídico")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Qué normas rigen al personal? Régimen jurídico (CE; TREBEP, arts. 1 a 7; Ley 30/1984)", donde(
  "Tercera pregunta. El personal ya está definido y sabemos cómo entra y sale; falta saber **qué normas** le rigen: la Constitución, el TREBEP como norma **básica**, las leyes de Función Pública y, en la AGE, la Ley 30/1984 en lo que sigue vigente.",
  ["1 Fundamento constitucional (CE, arts. 23.2, 103.3 y 149.1.18.ª)", "2 Objeto y fundamentos de actuación del TREBEP (art. 1)", "3 Ámbito de aplicación (arts. 2 a 5)", "4 Leyes de Función Pública y régimen del personal laboral (arts. 6 y 7)", "5 Título competencial, derogación y entrada en vigor; la Ley 30/1984 en la AGE"]))

T.ap("s12", "III.1 Fundamento constitucional (CE, arts. 23.2, 103.3 y 149.1.18.ª)", f"""
{unidad("1.1 Derecho de acceso a las funciones públicas (art. 23.2)",
  lit("CE", "Artículo 23", ["en condiciones de igualdad", "con los requisitos que señalen las leyes"], solo=[2]),
  ficha(f"{c('CE', 'Artículo 23', 'Los ciudadanos')} (sujeto del art. 23.1; el 23.2 sigue con «Asimismo, tienen derecho…»)",
        f"Derecho {c('CE', 'Artículo 23', 'a acceder en condiciones de igualdad a las funciones y cargos públicos')}",
        c("CE", "Artículo 23", "con los requisitos que señalen las leyes"),
        f"Es un derecho de la Sección primera del Capítulo segundo del Título I; el art. 53.2 permite recabar la tutela de esos derechos {c('CE', 'Artículo 53', 'por un procedimiento basado en los principios de preferencia y sumariedad')} y por el recurso de amparo",
        "El art. 23.2 habla de **igualdad**; el art. 103.3 añade **mérito y capacidad** para la función pública (→ III.1.2). Los requisitos los fijan **las leyes**."))}

{unidad("1.2 Reserva de ley del estatuto de los funcionarios (art. 103.3)",
  lit("CE", "Artículo 103", ["La ley regulará el estatuto de los funcionarios públicos", "de acuerdo con los principios de mérito y capacidad"], solo=[3]),
  fichab("Reserva de ley de la función pública",
         "Las Cortes y los Parlamentos autonómicos, por ley (→ III.4.1)",
         ["::La ley regulará:", "El estatuto de los funcionarios públicos", "El acceso a la función pública, según **mérito y capacidad**", "Las peculiaridades del ejercicio de su derecho a sindicación", "El sistema de incompatibilidades", "Las garantías para la imparcialidad en el ejercicio de sus funciones"],
         "—",
         "**Mérito y capacidad** (la **igualdad** está en el 23.2). Es **reserva de ley**: el estatuto no puede regularlo solo un reglamento (tema IV.2)."))}

{unidad("1.3 Competencia del Estado sobre las bases del régimen estatutario (art. 149.1.18.ª)",
  lit("CE", "Artículo 149", ["Las bases del régimen jurídico de las Administraciones públicas y del régimen estatutario de sus funcionarios"], solo=[19]),
  fichab("Título competencial de la legislación básica de función pública",
         "El **Estado**, con competencia exclusiva sobre las **bases**",
         "Las bases garantizarán a los administrados un tratamiento común ante las Administraciones",
         "—",
         "El Estado fija las **bases** del régimen estatutario; el desarrollo corresponde a las leyes de Función Pública de cada Administración (→ III.4.1). El TREBEP se dicta al amparo de este título (→ III.5.1)."))}
""", 2)

T.ap("s13", "III.2 Objeto y fundamentos de actuación del TREBEP (art. 1)", f"""
{unidad("2.1 Objeto y fundamentos (art. 1)",
  lit(TB, "Artículo 1", ["las bases del régimen estatutario de los funcionarios públicos", "determinar las normas aplicables al personal laboral", "Igualdad, mérito y capacidad en el acceso y en la promoción profesional", "garantizadas con la inamovilidad en la condición de funcionario de carrera", "Negociación colectiva y participación, a través de los representantes"]),
  fichab("Para qué sirve el TREBEP y en qué principios se apoya",
         "—",
         ["::Doble objeto:", "Funcionarios: establecer **las bases** de su régimen estatutario (1.1)", "Personal laboral: **determinar las normas aplicables** (1.2)"],
         ["::Fundamentos de actuación (1.3), doce: a) servicio a los ciudadanos y a los intereses generales; b) igualdad, mérito y capacidad en el acceso y la promoción; c) sometimiento pleno a la ley y al Derecho; d) igualdad de trato entre mujeres y hombres; e) objetividad, profesionalidad e imparcialidad, garantizadas con la inamovilidad; f) eficacia en la planificación y gestión de los recursos humanos; g) desarrollo y cualificación profesional permanente; h) transparencia; i) evaluación y responsabilidad en la gestión; j) jerarquía; k) negociación colectiva y participación; l) cooperación entre las Administraciones Públicas"],
         "Para los funcionarios, **bases**; para los laborales, **normas aplicables**. La imparcialidad se garantiza con la **inamovilidad** del funcionario de **carrera**. Son **doce** fundamentos (letras a a l)."))}
""", 2)

T.ap("s14", "III.3 Ámbito de aplicación (arts. 2 a 5)", f"""
{unidad("3.1 Administraciones incluidas y personal con régimen propio (art. 2)",
  lit(TB, "Artículo 2", ["al personal funcionario y en lo que proceda al personal laboral", "Las Universidades Públicas", "personal de investigación", "El personal docente y el personal estatutario de los Servicios de Salud", "se entenderá comprendido el personal estatutario de los Servicios de Salud", "tiene carácter supletorio"]),
  fichab("A quién se aplica el TREBEP",
         ["::Al personal **funcionario** y, en lo que proceda, al **laboral** de:", "a) la Administración General del Estado", "b) las de las comunidades autónomas y de Ceuta y Melilla", "c) las de las entidades locales", "d) los organismos públicos, agencias y demás entidades de derecho público con personalidad jurídica propia vinculadas o dependientes", "e) las Universidades Públicas"],
         ["Personal de **investigación**: normas singulares posibles (2.2)", "Personal **docente** y **estatutario** de los Servicios de Salud: su legislación específica y el TREBEP, salvo el capítulo II del título III (excepto el art. 20) y los arts. 22.3, 24 y 84 (2.3)", "La mención al funcionario de carrera comprende al personal **estatutario** de los Servicios de Salud (2.4)"],
         "—",
         "Al laboral, «**en lo que proceda**». Para el personal **no incluido**, el TREBEP es **supletorio** (2.5). Las Universidades Públicas **sí** están incluidas."))}

{unidad("3.2 Funcionarios de las entidades locales y Policía Local (art. 3)",
  lit(TB, "Artículo 3", ["con respeto a la autonomía local", "Los Cuerpos de Policía Local"]),
  fichab("Régimen del personal funcionario local",
         "Funcionarios de las entidades locales; Cuerpos de Policía Local",
         ["Funcionarios locales: legislación estatal aplicable (incluido el TREBEP) y legislación de las comunidades autónomas, con respeto a la autonomía local", "Policía Local: también el TREBEP y la legislación autonómica, salvo lo establecido para ellos en la Ley Orgánica 2/1986, de Fuerzas y Cuerpos de Seguridad"],
         "—",
         "Dos fuentes: la legislación **estatal** (de la que forma parte el TREBEP) y la **autonómica**, siempre **con respeto a la autonomía local**."))}

{unidad("3.3 Personal con legislación específica propia (art. 4)",
  lit(TB, "Artículo 4", ["sólo se aplicarán directamente cuando así lo disponga su legislación específica", "Personal retribuido por arancel", "Personal del Centro Nacional de Inteligencia", "Personal del Banco de España"]),
  fichab("Personal al que el TREBEP solo se aplica si su ley lo dice",
         ["::Ocho grupos:", "a) Funcionarios de las Cortes Generales y de las asambleas legislativas autonómicas", "b) Funcionarios de los demás Órganos Constitucionales y de los órganos estatutarios autonómicos", "c) Jueces, Magistrados, Fiscales y demás personal de la Administración de Justicia", "d) Personal militar de las Fuerzas Armadas", "e) Personal de las Fuerzas y Cuerpos de Seguridad", "f) Personal retribuido por arancel", "g) Personal del Centro Nacional de Inteligencia", "h) Personal del Banco de España y del Fondo de Garantía de Depósitos de Entidades de Crédito"],
         "El TREBEP solo se les aplica **directamente** cuando lo disponga su legislación específica",
         "—",
         "La clave es «**sólo** se aplicarán directamente cuando así lo disponga su legislación específica». Distinto de la **Policía Local**, a la que el TREBEP sí se aplica (art. 3.2)."))}

{unidad("3.4 Personal de la Sociedad Estatal Correos y Telégrafos (art. 5)",
  lit(TB, "Artículo 5", ["por sus normas específicas y supletoriamente por lo dispuesto en este Estatuto", "por la legislación laboral y demás normas convencionalmente aplicables"]),
  fichab("Régimen del personal de Correos",
         "Personal de la Sociedad Estatal Correos y Telégrafos",
         ["Funcionarios: sus normas específicas y, **supletoriamente**, el TREBEP", "Laborales: legislación laboral y normas convencionales"],
         "—",
         "Para los **funcionarios** de Correos el TREBEP es **supletorio**; su personal **laboral** se rige por la legislación laboral y convencional."))}
""", 2)

T.ap("s15", "III.4 Leyes de Función Pública y régimen del personal laboral (arts. 6 y 7)", f"""
{unidad("4.1 Leyes de Función Pública (art. 6)",
  lit(TB, "Artículo 6", ["las Cortes Generales y las asambleas legislativas de las comunidades autónomas aprobarán"]),
  fichab("Desarrollo legislativo del TREBEP",
         "Las **Cortes Generales** (AGE) y las **asambleas legislativas** de las comunidades autónomas",
         "Leyes reguladoras de la Función Pública de la AGE y de las comunidades autónomas, en desarrollo del TREBEP y en el ámbito de sus competencias",
         "—",
         "El desarrollo es por **ley** (no por reglamento), coherente con la reserva del art. 103.3 CE (→ III.1.2). Mientras no se dicten, rige la disposición final cuarta (→ III.5.2)."))}

{unidad("4.2 Normativa aplicable al personal laboral (art. 7)",
  lit(TB, "Artículo 7", ["además de por la legislación laboral y por las demás normas convencionalmente aplicables, por los preceptos de este Estatuto que así lo dispongan", "nacimiento, adopción, del progenitor diferente de la madre biológica, de lactancia y parental", "no siendo de aplicación a este personal"]),
  fichab("Fuentes del régimen del personal laboral de las Administraciones",
         "Personal laboral al servicio de las Administraciones públicas",
         ["::Se rige por:", "La legislación laboral", "Las demás normas convencionalmente aplicables", "Los preceptos del TREBEP que así lo dispongan"],
         ["::Excepción (permisos):", "Nacimiento, adopción, del progenitor diferente de la madre biológica, lactancia y parental: se rige por el **TREBEP**", "No se le aplican las suspensiones del contrato del Estatuto de los Trabajadores por los mismos supuestos"],
         "Ni «exclusivamente» la legislación laboral, ni el TREBEP «íntegramente»: las **tres** fuentes. En esos **permisos** manda el **TREBEP**, no el Estatuto de los Trabajadores. Cayó en 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s16", "III.5 Título competencial, derogación y entrada en vigor; la Ley 30/1984 en la AGE", f"""
{unidad("5.1 Habilitación competencial (disposición final primera)",
  lit(TB, "dfprimera", ["artículo 149.1.18.ª", "bases del régimen estatutario de los funcionarios", "artículo 149.1.7.ª", "artículo 149.1.13.ª"], titulo="Disposición final primera. Habilitación competencial (TREBEP)"),
  fichab("Títulos competenciales del TREBEP",
         "El Estado",
         ["Art. **149.1.18.ª** CE: bases del régimen estatutario de los funcionarios (→ III.1.3)", "Art. **149.1.7.ª**: legislación laboral", "Art. **149.1.13.ª**: bases y coordinación de la planificación general de la actividad económica"],
         "—",
         "**Tres** títulos: 18.ª (funcionarios), 7.ª (laboral) y 13.ª (economía)."))}

{unidad("5.2 Entrada en vigor diferida y normas vigentes (disposición final cuarta)",
  lit(TB, "dfcuaa", ["producirá efectos a partir de la entrada en vigor de las leyes de Función Pública", "se mantendrán en vigor en cada Administración Pública las normas vigentes sobre ordenación, planificación y gestión de recursos humanos"], solo=[1, 3], titulo="Disposición final cuarta. Entrada en vigor (TREBEP)"),
  fichab("Qué partes del TREBEP esperan a las leyes de Función Pública",
         "Cada Administración Pública",
         ["Capítulos II y III del título III (salvo el art. 25.2) y capítulo III del título V: efectos desde la entrada en vigor de las **leyes de Función Pública**", "Mientras tanto, siguen en vigor las normas vigentes sobre ordenación, planificación y gestión de recursos humanos, **en tanto no se opongan** al TREBEP"],
         "—",
         "Es la razón de que en la AGE sigan aplicándose preceptos de la **Ley 30/1984** (→ III.5.3)."))}

{unidad("5.3 Derogación parcial de la Ley 30/1984 (disposición derogatoria única, b)",
  lit(TB, "ddunica-2", ["con el alcance establecido en el apartado 2 de la disposición final cuarta", "De la Ley 30/1984, de 2 de agosto, de Medidas para la Reforma de la Función Pública"], solo=[1, 3], titulo="Disposición derogatoria única (TREBEP), letra b)"),
  fichab("Qué se deroga de la Ley 30/1984",
         "—",
         "Se derogan **solo** los preceptos enumerados, con el alcance del apartado 2 de la disposición final cuarta",
         "—",
         "La Ley 30/1984 **no** está derogada entera: se derogan los artículos de la lista. Por ejemplo, el art. **15** (puestos que puede ocupar el personal laboral, → I.4.2) y el art. **1** (→ III.5.4) **no** figuran en ella."))}

{unidad("5.4 Ámbito de la Ley 30/1984 (art. 1.1, 2, 4 y 5)",
  lit("L30", "auno", ["Al personal de la Administración Civil del Estado y sus Organismos autónomos", "tiene carácter supletorio"], solo=[1, 2, 3, 4, 5, 7, 8]),
  fichab("A quién se aplica la Ley 30/1984",
         ["Personal de la Administración Civil del Estado y sus Organismos autónomos", "Personal civil al servicio de la Administración Militar y sus Organismos autónomos", "Personal funcionario de la Administración de la Seguridad Social"],
         ["Normas específicas posibles para personal docente e investigador, sanitario, de servicios postales y de telecomunicación y destinado en el extranjero (1.2)", "«Personal al servicio de la Administración del Estado» = el del apartado 1 (1.4)"],
         "—",
         "Es **supletoria** para el personal no incluido en su ámbito (1.5), igual que el TREBEP (art. 2.5 → III.3.1)."))}

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Capa | Norma | Qué aporta |
|---|---|---|
| Constitución | Arts. 23.2, 103.3 y 149.1.18.ª | Acceso en igualdad; reserva de ley con mérito y capacidad; bases estatales |
| Legislación básica | TREBEP (RDLeg 5/2015) | Bases del régimen estatutario (funcionarios) y normas aplicables al personal laboral |
| Desarrollo legislativo | Leyes de Función Pública (art. 6) | Régimen de cada Administración |
| AGE, mientras no hay ley propia | Ley 30/1984 en lo no derogado; normas vigentes de gestión (DF 4.ª.2) | Por ejemplo, art. 15 (RPT y puestos de personal laboral) |
| Personal laboral | Legislación laboral, convenios y preceptos del TREBEP que lo dispongan (art. 7) | Con la excepción de los permisos |

{resumen([
  "CE: acceso en **igualdad** (23.2); **ley** con **mérito y capacidad** (103.3); **bases** estatales (149.1.18.ª).",
  "TREBEP: **bases** del régimen estatutario y **normas aplicables** al laboral; **doce** fundamentos (art. 1). Se aplica a AGE, CC. AA., entes locales, organismos públicos y Universidades Públicas (art. 2); supletorio para el resto.",
  "Art. 4: **ocho** grupos solo si su legislación lo dispone; Correos: supletorio (art. 5). Desarrollo por **leyes** de Función Pública (art. 6).",
  "Laboral: legislación laboral + convenios + TREBEP **que así lo disponga**; permisos de nacimiento, adopción, lactancia y parental, por el **TREBEP** (art. 7).",
  "En la AGE siguen vigentes los preceptos de la Ley 30/1984 **no derogados** (derogatoria única b; DF 4.ª)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX = [
 ("L", 61, "Adquisición de la condición de funcionario (→ II.1.1)", {
   "a": f"No está en el art. 62: el funcionario de carrera se vincula {c(TB, 'Artículo 9', 'en virtud de nombramiento legal')} (art. 9.1); el **contrato** es propio del personal laboral, {c(TB, 'Artículo 11', 'en virtud de contrato de trabajo formalizado por escrito')} (art. 11.1). Por eso es la respuesta (la que **no** es requisito).",
   "b": f"Sí es requisito: art. 62.1 d), {c(TB, 'Artículo 62', 'Toma de posesión dentro del plazo que se establezca')}.",
   "c": f"Sí es requisito: art. 62.1 c), {c(TB, 'Artículo 62', 'Acto de acatamiento de la Constitución y, en su caso, del Estatuto de Autonomía correspondiente y del resto del Ordenamiento Jurídico')}.",
   "d": f"Sí es requisito: art. 62.1 b), {c(TB, 'Artículo 62', 'Nombramiento por el órgano o autoridad competente, que será publicado en el Diario Oficial correspondiente')}."},
   [("contrato", TB, "Artículo 11", "en virtud de contrato de trabajo formalizado por escrito")]),
 ("L", 62, "Renuncia (→ II.3.1)", {
   "a": f"Falso: la renuncia es la primera causa de pérdida, {c(TB, 'Artículo 63', 'La renuncia a la condición de funcionario')} (art. 63 a). La opción mezcla otras causas y omite la renuncia y la nacionalidad.",
   "b": f"Invierte el art. 64.3: {c(TB, 'Artículo 64', 'La renuncia a la condición de funcionario no inhabilita para ingresar de nuevo en la Administración Pública a través del procedimiento de selección establecido')}.",
   "c": f"Literal del art. 64.1: la renuncia {c(TB, 'Artículo 64', 'habrá de ser manifestada por escrito y será aceptada expresamente por la Administración')}.",
   "d": f"Falso: el TREBEP regula la renuncia como causa de pérdida (art. 63 a) y su forma (art. 64); no hay ninguna «obediencia debida» que la impida."},
   [("manifestada por escrito", TB, "Artículo 64", "habrá de ser manifestada por escrito"),
    ("aceptada expresamente por la Administración", TB, "Artículo 64", "será aceptada expresamente por la Administración")]),
 ("P", 78, "Concepto de funcionario interino (→ I.3.1)", {
   "a": f"Cambia dos datos: no es «permanente» sino {c(TB, 'Artículo 10', 'con carácter temporal')}, y las funciones son {c(TB, 'Artículo 10', 'propias de funcionarios de carrera')}.",
   "b": f"Cambia un dato: las funciones no son «que no sean propias», sino {c(TB, 'Artículo 10', 'propias de funcionarios de carrera')}.",
   "c": f"Cambia un dato: el nombramiento no es «permanente», sino {c(TB, 'Artículo 10', 'con carácter temporal')} (lo permanente es del funcionario de carrera, art. 9.1).",
   "d": f"Literal del art. 10.1: {c(TB, 'Artículo 10', 'por razones expresamente justificadas de necesidad y urgencia, son nombrados como tales con carácter temporal para el desempeño de funciones propias de funcionarios de carrera')}."},
   [("con carácter temporal para el desempeño de funciones propias de funcionarios de carrera", TB, "Artículo 10", "son nombrados como tales con carácter temporal para el desempeño de funciones propias de funcionarios de carrera")]),
 ("P", 81, "Régimen jurídico del personal laboral (→ III.4.2)", {
   "a": f"Falso: no «exclusivamente»; también le rigen {c(TB, 'Artículo 7', 'los preceptos de este Estatuto que así lo dispongan')}.",
   "b": f"Literal del art. 7: se rige {c(TB, 'Artículo 7', 'además de por la legislación laboral y por las demás normas convencionalmente aplicables, por los preceptos de este Estatuto que así lo dispongan')}.",
   "c": f"Invierte la excepción: en esos permisos el personal laboral {c(TB, 'Artículo 7', 'se regirá por lo previsto en el presente Estatuto')}, sin aplicar las suspensiones del Estatuto de los Trabajadores.",
   "d": "Falso: el TREBEP no se le aplica «íntegramente» ni «en cualquier materia»; solo sus preceptos **que así lo dispongan**, junto con la legislación laboral y las normas convencionales (art. 7)."},
   [("que así lo dispongan", TB, "Artículo 7", "por los preceptos de este Estatuto que así lo dispongan")]),
 ("X", 67, "Supuestos de nombramiento de interinos (→ I.3.1)", {
   "a": f"Cambia el plazo: la vacante permite el nombramiento {c(TB, 'Artículo 10', 'por un máximo de tres años')}, no de un año.",
   "b": f"Cambia los plazos: los programas temporales {c(TB, 'Artículo 10', 'no podrán tener una duración superior a tres años, ampliable hasta doce meses más')}, no tres meses ampliables un mes.",
   "c": f"Cambia los plazos: el exceso o acumulación de tareas es {c(TB, 'Artículo 10', 'por plazo máximo de nueve meses, dentro de un periodo de dieciocho meses')}, no tres años en cinco.",
   "d": f"Literal del art. 10.1 b): {c(TB, 'Artículo 10', 'La sustitución transitoria de los titulares, durante el tiempo estrictamente necesario')}."},
   [("Sustitución transitoria de los titulares, durante el tiempo estrictamente necesario", TB, "Artículo 10", "La sustitución transitoria de los titulares, durante el tiempo estrictamente necesario")]),
]
bloques = []
for cod, n, tit, por, ap_ in EX:
    bloques += [f"### {('GACE-L' if cod == 'L' else 'GACE-P' if cod == 'P' else 'GACE-L extraordinario')} 2025, pregunta {n} · {tit}", examen(cod, n, por, ap_)]
T.ap("s17", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join(
  ["En los primeros ejercicios de **2025** cayeron **cinco** preguntas de este tema: dos en el turno libre (arts. 62 y 64), dos en promoción interna (arts. 10 y 7) y una en el extraordinario (art. 10). Todas son literales. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal."]
  + bloques + ["### Cómo se pregunta", "!> Las preguntas citan el **artículo** del TREBEP y cambian **un dato**: «permanente» por «temporal», «propias» por «que no sean propias», un **plazo** del art. 10.1 (tres años, nueve meses en dieciocho), o meten un requisito ajeno (el **contrato**, que es del personal laboral). En el art. 7, los distractores son «**exclusivamente**» e «**íntegramente**»."]))

T.ap("s18", "Cierre 2. Repaso en 10 minutos (por bloques)", """
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Concepto y clases | Empleado público (art. 8); carrera (9), interino (10), laboral (11), eventual (12), directivo (13) | Interino: **temporal** + funciones **propias** de carrera; plazos **3 años / tiempo estrictamente necesario / 3 años + 12 meses / 9 meses en 18** |
| II. Adquisición y pérdida | Cuatro requisitos sucesivos (62); cinco causas (63); renuncia (64); jubilación (67); rehabilitación (68) | Renuncia **por escrito** y **aceptada expresamente**; jubilación forzosa a los **65**, hasta **70** |
| III. Régimen jurídico | CE 23.2, 103.3, 149.1.18.ª; TREBEP arts. 1 a 7; DF 1.ª y 4.ª; Ley 30/1984 en la AGE | Laboral: legislación laboral + convenios + TREBEP **que así lo disponga** (art. 7) |

?> **Trampas frecuentes:** «interino con carácter **permanente**» (es **temporal**); «funciones que **no** sean propias de funcionarios de carrera» (son **propias**); «vacante por un máximo de **un año**» (son **tres**); «acumulación de tareas **tres años en cinco**» (**nueve meses en dieciocho**); «la renuncia **impide** volver a ingresar» (**no inhabilita**); «la **firma del contrato**» como requisito del funcionario (es del **laboral**); «el personal laboral se rige **exclusivamente** por la legislación laboral» (también por el **TREBEP** en lo que disponga); «el personal **directivo** es una clase del art. 8» (no lo es).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
Q = [
 (TB, "Artículo 8", "Concepto y clases", "Según el artículo 8.1 del TREBEP, son empleados públicos quienes desempeñan funciones retribuidas en las Administraciones Públicas:",
  ["Al servicio de los intereses generales.", "En virtud de nombramiento legal.", "Con carácter permanente.", "Mediante contrato formalizado por escrito."], "Art. 8.1 TREBEP. Las demás son rasgos de clases concretas (arts. 9 y 11).", "quienes desempeñan funciones retribuidas en las Administraciones Públicas al servicio de los intereses generales"),
 (TB, "Artículo 8", "Concepto y clases", "Según el artículo 8.2 del TREBEP, ¿cuál de las siguientes NO es una de las clases en que se clasifican los empleados públicos?",
  ["Personal directivo profesional.", "Funcionarios interinos.", "Personal eventual.", "Personal laboral."], "El art. 8.2 enumera funcionarios de carrera, funcionarios interinos, personal laboral y personal eventual; el directivo se regula aparte (art. 13).", ["Funcionarios interinos", "Personal eventual"]),
 (TB, "Artículo 8", "Concepto y clases", "Según el artículo 8.2 c) del TREBEP, el personal laboral puede ser:",
  ["Fijo, por tiempo indefinido o temporal.", "Fijo o eventual.", "Fijo, interino o de confianza.", "Permanente o directivo."], "Art. 8.2 c) TREBEP.", "Personal laboral, ya sea fijo, por tiempo indefinido o temporal"),
 (TB, "Artículo 9", "Funcionarios de carrera", "Según el artículo 9.1 del TREBEP, los funcionarios de carrera están vinculados a una Administración Pública por una relación:",
  ["Estatutaria regulada por el Derecho Administrativo.", "Laboral regulada por el Estatuto de los Trabajadores.", "Contractual de carácter administrativo.", "Estatutaria regulada por el Derecho Civil."], "Art. 9.1 TREBEP.", "una relación estatutaria regulada por el Derecho Administrativo"),
 (TB, "Artículo 9", "Funcionarios de carrera", "Según el artículo 9.2 del TREBEP, el ejercicio de las funciones que impliquen la participación directa o indirecta en el ejercicio de las potestades públicas corresponde:",
  ["Exclusivamente a los funcionarios públicos.", "A los funcionarios públicos y al personal laboral fijo.", "Al personal directivo profesional.", "A cualquier empleado público."], "Art. 9.2 TREBEP.", "corresponden exclusivamente a los funcionarios públicos"),
 (TB, "Artículo 10", "Funcionarios interinos", "Según el artículo 10.1 del TREBEP, los funcionarios interinos son nombrados por razones expresamente justificadas de:",
  ["Necesidad y urgencia.", "Necesidad o urgencia.", "Interés público y oportunidad.", "Eficacia y eficiencia."], "Art. 10.1 TREBEP: «necesidad **y** urgencia».", "por razones expresamente justificadas de necesidad y urgencia"),
 (TB, "Artículo 10", "Funcionarios interinos", "Según el artículo 10.1 a) del TREBEP, el nombramiento de interinos por existencia de plazas vacantes, cuando no sea posible su cobertura por funcionarios de carrera, es por un máximo de:",
  ["Tres años.", "Un año.", "Dos años.", "Cinco años."], "Art. 10.1 a) TREBEP.", "por un máximo de tres años"),
 (TB, "Artículo 10", "Funcionarios interinos", "Según el artículo 10.1 c) del TREBEP, los programas de carácter temporal que justifican el nombramiento de interinos no podrán tener una duración superior a:",
  ["Tres años, ampliable hasta doce meses más por las leyes de Función Pública.", "Dos años, ampliable hasta seis meses más.", "Tres años, sin posibilidad de ampliación.", "Cuatro años, ampliable hasta doce meses más."], "Art. 10.1 c) TREBEP.", "no podrán tener una duración superior a tres años, ampliable hasta doce meses más"),
 (TB, "Artículo 10", "Funcionarios interinos", "Según el artículo 10.1 d) del TREBEP, el nombramiento de interinos por exceso o acumulación de tareas tiene un plazo máximo de:",
  ["Nueve meses, dentro de un periodo de dieciocho meses.", "Seis meses, dentro de un periodo de doce meses.", "Doce meses, dentro de un periodo de dieciocho meses.", "Tres años, dentro de un periodo de cinco años."], "Art. 10.1 d) TREBEP.", "por plazo máximo de nueve meses, dentro de un periodo de dieciocho meses"),
 (TB, "Artículo 10", "Funcionarios interinos", "Según el artículo 10.2 del TREBEP, los procedimientos de selección del personal funcionario interino se rigen, en todo caso, por los principios de:",
  ["Igualdad, mérito, capacidad, publicidad y celeridad.", "Igualdad, mérito y capacidad, exclusivamente.", "Publicidad, concurrencia y transparencia.", "Mérito, capacidad e idoneidad."], "Art. 10.2 TREBEP.", "igualdad, mérito, capacidad, publicidad y celeridad"),
 (TB, "Artículo 10", "Funcionarios interinos", "Según el artículo 10.2 del TREBEP, el nombramiento derivado de los procedimientos de selección del personal funcionario interino:",
  ["En ningún caso dará lugar al reconocimiento de la condición de funcionario de carrera.", "Dará lugar a la condición de funcionario de carrera tras tres años de servicios.", "Dará lugar a la condición de funcionario de carrera si se supera un curso selectivo.", "Equivaldrá a la superación del proceso selectivo del art. 62."], "Art. 10.2 TREBEP.", "en ningún caso dará lugar al reconocimiento de la condición de funcionario de carrera"),
 (TB, "Artículo 10", "Funcionarios interinos", "Según el artículo 10.3 del TREBEP, la Administración formalizará la finalización de la relación de interinidad:",
  ["De oficio y sin derecho a compensación alguna.", "A instancia del interesado y con una indemnización de veinte días por año.", "De oficio y con una indemnización de doce días por año.", "Previo expediente disciplinario."], "Art. 10.3 TREBEP.", ["formalizará de oficio", "sin derecho a compensación alguna"]),
 (TB, "Artículo 10", "Funcionarios interinos", "¿Cuál de las siguientes NO es una causa de finalización de la relación de interinidad del artículo 10.3 del TREBEP?",
  ["La obtención de una evaluación del desempeño negativa.", "La cobertura reglada del puesto por personal funcionario de carrera.", "La finalización del plazo autorizado expresamente recogido en su nombramiento.", "La finalización de la causa que dio lugar a su nombramiento."], "Art. 10.3 TREBEP: cobertura reglada, supresión o amortización del puesto, fin del plazo autorizado y fin de la causa (además de las del art. 63).", ["Por la cobertura reglada del puesto por personal funcionario de carrera", "Por la finalización de la causa que dio lugar a su nombramiento"]),
 (TB, "Artículo 10", "Funcionarios interinos", "Según el artículo 10.4 del TREBEP, en el supuesto de vacante, ¿cuándo se producirá el fin de la relación de interinidad?",
  ["Transcurridos tres años desde el nombramiento del personal funcionario interino.", "Transcurridos dos años desde la publicación de la vacante.", "Transcurridos tres años desde la toma de posesión del último funcionario de carrera.", "Transcurridos cinco años desde el nombramiento."], "Art. 10.4 TREBEP (salvo proceso selectivo desierto o convocatoria publicada dentro del plazo).", "transcurridos tres años desde el nombramiento del personal funcionario interino se producirá el fin de la relación de interinidad"),
 (TB, "da", "Funcionarios interinos", "Según la disposición adicional decimoséptima del TREBEP, el incumplimiento del plazo máximo de permanencia dará lugar, para el personal funcionario interino afectado, a una compensación equivalente a:",
  ["Veinte días de sus retribuciones fijas por año de servicio, hasta un máximo de doce mensualidades.", "Treinta y tres días de sus retribuciones por año de servicio, hasta un máximo de veinticuatro mensualidades.", "Doce días de sus retribuciones fijas por año de servicio, sin límite.", "Veinte días de sus retribuciones totales por año de servicio, hasta un máximo de nueve mensualidades."], "DA 17.ª.4 TREBEP.", ["veinte días de sus retribuciones fijas por año de servicio", "hasta un máximo de doce mensualidades"]),
 (TB, "da", "Funcionarios interinos", "Según la disposición adicional decimoséptima del TREBEP, todo acto, pacto o disposición reglamentaria cuyo contenido suponga el incumplimiento de los plazos máximos de permanencia como personal temporal será:",
  ["Nulo de pleno derecho.", "Anulable.", "Válido, aunque generará responsabilidad.", "Irregular no invalidante."], "DA 17.ª.3 TREBEP.", "será nulo de pleno derecho"),
 (TB, "Artículo 11", "Personal laboral", "Según el artículo 11.1 del TREBEP, es personal laboral el que presta servicios retribuidos por las Administraciones Públicas en virtud de:",
  ["Contrato de trabajo formalizado por escrito.", "Nombramiento legal publicado en el Diario Oficial.", "Contrato de trabajo verbal o escrito.", "Nombramiento libre."], "Art. 11.1 TREBEP.", "en virtud de contrato de trabajo formalizado por escrito"),
 (TB, "Artículo 11", "Personal laboral", "Según el artículo 11.3 del TREBEP, los procedimientos de selección del personal laboral serán públicos y se regirán en todo caso por los principios de:",
  ["Igualdad, mérito y capacidad.", "Mérito, capacidad e idoneidad.", "Publicidad y libre designación.", "Confianza y asesoramiento."], "Art. 11.3 TREBEP (el temporal, también por el de celeridad).", "rigiéndose en todo caso por los principios de igualdad, mérito y capacidad"),
 ("L30", "aquince", "Personal laboral", "Según el artículo 15.1 c) de la Ley 30/1984, con carácter general, los puestos de trabajo de la Administración del Estado y de sus Organismos Autónomos serán desempeñados por:",
  ["Funcionarios públicos.", "Personal laboral fijo.", "Personal eventual.", "Funcionarios interinos."], "Art. 15.1 c) Ley 30/1984; el personal laboral es la excepción tasada.", "serán desempeñados por funcionarios públicos"),
 (TB, "Artículo 12", "Personal eventual", "Según el artículo 12.1 del TREBEP, el personal eventual solo realiza funciones expresamente calificadas como de:",
  ["Confianza o asesoramiento especial.", "Dirección profesional.", "Carácter temporal y urgente.", "Inspección y control."], "Art. 12.1 TREBEP.", "sólo realiza funciones expresamente calificadas como de confianza o asesoramiento especial"),
 (TB, "Artículo 12", "Personal eventual", "Según el artículo 12.3 del TREBEP, el cese del personal eventual tendrá lugar, en todo caso:",
  ["Cuando se produzca el de la autoridad a la que se preste la función de confianza o asesoramiento.", "Al finalizar la legislatura.", "A los cuatro años de su nombramiento.", "Cuando se cubra el puesto por un funcionario de carrera."], "Art. 12.3 TREBEP.", "cuando se produzca el de la autoridad a la que se preste la función de confianza o asesoramiento"),
 (TB, "Artículo 12", "Personal eventual", "Según el artículo 12.4 del TREBEP, la condición de personal eventual:",
  ["No podrá constituir mérito para el acceso a la Función Pública o para la promoción interna.", "Constituirá mérito para el acceso a la Función Pública.", "Constituirá mérito solo para la promoción interna.", "Dará preferencia en los concursos de provisión de puestos."], "Art. 12.4 TREBEP.", "no podrá constituir mérito para el acceso a la Función Pública o para la promoción interna"),
 (TB, "Artículo 13", "Personal directivo", "Según el artículo 13.4 del TREBEP, cuando el personal directivo reúna la condición de personal laboral estará sometido a:",
  ["La relación laboral de carácter especial de alta dirección.", "El convenio colectivo único del personal laboral.", "El régimen general de los funcionarios de carrera.", "La relación laboral común."], "Art. 13.4 TREBEP.", "relación laboral de carácter especial de alta dirección"),
 (TB, "Artículo 13", "Personal directivo", "Según el artículo 13.4 del TREBEP, la determinación de las condiciones de empleo del personal directivo:",
  ["No tendrá la consideración de materia objeto de negociación colectiva.", "Será objeto de negociación en la Mesa General de Negociación.", "Se fijará en el convenio colectivo correspondiente.", "Requerirá informe favorable de las Juntas de Personal."], "Art. 13.4 TREBEP.", "no tendrá la consideración de materia objeto de negociación colectiva"),
 (TB, "Artículo 62", "Adquisición", "Según el artículo 62.1 del TREBEP, la condición de funcionario de carrera se adquiere por el cumplimiento:",
  ["Sucesivo de los requisitos que enumera.", "Simultáneo de los requisitos que enumera.", "De cualquiera de los requisitos que enumera.", "De los requisitos que fije cada convocatoria, en el orden que esta determine."], "Art. 62.1 TREBEP: «cumplimiento sucesivo».", "se adquiere por el cumplimiento sucesivo de los siguientes requisitos"),
 (TB, "Artículo 62", "Adquisición", "Según el artículo 62.1 b) del TREBEP, el nombramiento por el órgano o autoridad competente:",
  ["Será publicado en el Diario Oficial correspondiente.", "Será notificado personalmente, sin necesidad de publicación.", "Se formalizará mediante contrato.", "Requerirá informe de la Comisión Superior de Personal."], "Art. 62.1 b) TREBEP.", "Nombramiento por el órgano o autoridad competente, que será publicado en el Diario Oficial correspondiente"),
 ("RD364", "Artículo 25", "Adquisición", "Según el artículo 25.1 del Real Decreto 364/1995, el número de aspirantes que hayan superado el proceso selectivo y sean nombrados funcionarios de carrera:",
  ["No podrá exceder en ningún caso al de plazas convocadas.", "Podrá exceder en un diez por ciento al de plazas convocadas.", "Podrá exceder al de plazas convocadas si hay vacantes dotadas.", "Lo fija libremente el órgano de selección."], "Art. 25.1 RD 364/1995: lo contrario es nulo de pleno derecho.", "cuyo número no podrá exceder en ningún caso al de plazas convocadas"),
 (TB, "Artículo 63", "Pérdida", "Según el artículo 63 del TREBEP, es causa de pérdida de la condición de funcionario de carrera:",
  ["La jubilación total del funcionario.", "La jubilación parcial del funcionario.", "La suspensión firme de funciones.", "La excedencia voluntaria por interés particular."], "Art. 63 c) TREBEP: jubilación **total**.", "La jubilación total del funcionario"),
 (TB, "Artículo 63", "Pérdida", "Según el artículo 63 d) del TREBEP, la sanción disciplinaria de separación del servicio es causa de pérdida de la condición de funcionario:",
  ["Cuando tuviere carácter firme.", "Desde que se incoa el expediente disciplinario.", "Desde que se notifica la propuesta de resolución.", "Solo si va acompañada de pena de inhabilitación."], "Art. 63 d) TREBEP.", "La sanción disciplinaria de separación del servicio que tuviere carácter firme"),
 (TB, "Artículo 64", "Pérdida", "Según el artículo 64.2 del TREBEP, no podrá ser aceptada la renuncia cuando el funcionario:",
  ["Esté sujeto a expediente disciplinario.", "Lleve menos de tres años de servicio.", "Esté en situación de excedencia voluntaria.", "Haya solicitado la prolongación en el servicio activo."], "Art. 64.2 TREBEP (también si se ha dictado auto de procesamiento o de apertura de juicio oral por algún delito).", "cuando el funcionario esté sujeto a expediente disciplinario"),
 (TB, "Artículo 65", "Pérdida", "Según el artículo 65 del TREBEP, la pérdida de la nacionalidad que haya sido tenida en cuenta para el nombramiento determinará la pérdida de la condición de funcionario:",
  ["Salvo que simultáneamente se adquiera la nacionalidad de alguno de los Estados que menciona.", "En todo caso.", "Solo si el funcionario pertenece a un Cuerpo con funciones de autoridad.", "Salvo que el funcionario solicite la excedencia en el plazo de un mes."], "Art. 65 TREBEP.", "salvo que simultáneamente se adquiera la nacionalidad de alguno de dichos Estados"),
 (TB, "Artículo 66", "Pérdida", "Según el artículo 66 del TREBEP, la pena de inhabilitación especial, cuando hubiere adquirido firmeza la sentencia que la imponga, produce la pérdida de la condición de funcionario respecto de:",
  ["Aquellos empleos o cargos especificados en la sentencia.", "Todos los empleos o cargos que tuviere.", "El empleo que desempeñara al cometer el delito y los de su mismo Cuerpo.", "Ningún empleo: solo suspende de funciones."], "Art. 66 TREBEP: la absoluta afecta a todos; la especial, a los especificados en la sentencia.", "respecto de aquellos empleos o cargos especificados en la sentencia"),
 (TB, "Artículo 67", "Jubilación", "Según el artículo 67.3 del TREBEP, la jubilación forzosa se declarará de oficio al cumplir el funcionario:",
  ["Los sesenta y cinco años de edad.", "Los sesenta y siete años de edad.", "Los setenta años de edad.", "Los sesenta años de edad."], "Art. 67.3 TREBEP (con la regla del 67.4 para el Régimen General de la Seguridad Social).", "La jubilación forzosa se declarará de oficio al cumplir el funcionario los sesenta y cinco años de edad"),
 (TB, "Artículo 67", "Jubilación", "Según el artículo 67.3 del TREBEP, se podrá solicitar la prolongación de la permanencia en el servicio activo como máximo hasta que se cumplan:",
  ["Setenta años de edad.", "Sesenta y ocho años de edad.", "Setenta y dos años de edad.", "Sesenta y siete años de edad."], "Art. 67.3 TREBEP.", "como máximo hasta que se cumpla setenta años de edad"),
 (TB, "Artículo 67", "Jubilación", "Según el artículo 67.1 del TREBEP, ¿cuál de las siguientes NO es una modalidad de jubilación de los funcionarios?",
  ["Por mutuo acuerdo con la Administración.", "Voluntaria, a solicitud del funcionario.", "Forzosa, al cumplir la edad legalmente establecida.", "Por la declaración de incapacidad permanente para el ejercicio de las funciones propias de su cuerpo o escala."], "Art. 67.1 TREBEP: voluntaria, forzosa y por incapacidad permanente.", ["Voluntaria, a solicitud del funcionario", "Forzosa, al cumplir la edad legalmente establecida"]),
 (TB, "Artículo 68", "Rehabilitación", "Según el artículo 68.2 del TREBEP, si transcurrido el plazo para resolver la solicitud de rehabilitación de quien perdió la condición de funcionario por inhabilitación no se hubiera dictado resolución expresa:",
  ["Se entenderá desestimada la solicitud.", "Se entenderá estimada la solicitud.", "Se producirá la caducidad del procedimiento.", "Se elevará al Consejo de Ministros."], "Art. 68.2 TREBEP: silencio negativo.", "se entenderá desestimada la solicitud"),
 (TB, "Artículo 68", "Rehabilitación", "Según el artículo 68.1 del TREBEP, en caso de extinción de la relación de servicios por pérdida de la nacionalidad o jubilación por incapacidad permanente, desaparecida la causa objetiva, la rehabilitación solicitada:",
  ["Le será concedida.", "Podrá concederse con carácter excepcional.", "Solo procederá tras superar un nuevo proceso selectivo.", "Requerirá acuerdo del Consejo de Ministros."], "Art. 68.1 TREBEP (la excepcional es la del 68.2, por inhabilitación).", "podrá solicitar la rehabilitación de su condición de funcionario, que le será concedida"),
 ("CE", "Artículo 103", "Régimen jurídico", "Según el artículo 103.3 de la Constitución, la ley regulará el acceso a la función pública de acuerdo con los principios de:",
  ["Mérito y capacidad.", "Igualdad, mérito, capacidad y publicidad.", "Objetividad e imparcialidad.", "Eficacia y jerarquía."], "Art. 103.3 CE (la igualdad está en el art. 23.2).", "de acuerdo con los principios de mérito y capacidad"),
 (TB, "Artículo 1", "Régimen jurídico", "Según el artículo 1.3 e) del TREBEP, la objetividad, profesionalidad e imparcialidad en el servicio están garantizadas con:",
  ["La inamovilidad en la condición de funcionario de carrera.", "La negociación colectiva.", "El régimen de incompatibilidades.", "La evaluación del desempeño."], "Art. 1.3 e) TREBEP.", "garantizadas con la inamovilidad en la condición de funcionario de carrera"),
 (TB, "Artículo 2", "Régimen jurídico", "Según el artículo 2.5 del TREBEP, para todo el personal de las Administraciones Públicas no incluido en su ámbito de aplicación, el Estatuto tiene carácter:",
  ["Supletorio.", "Básico.", "Preferente.", "Excluyente."], "Art. 2.5 TREBEP.", "tiene carácter supletorio para todo el personal de las Administraciones Públicas no incluido en su ámbito de aplicación"),
 (TB, "Artículo 4", "Régimen jurídico", "Según el artículo 4 del TREBEP, ¿a qué personal se aplicarán las disposiciones del Estatuto solo cuando así lo disponga su legislación específica?",
  ["Al personal del Centro Nacional de Inteligencia.", "Al personal funcionario de las entidades locales.", "Al personal de las Universidades Públicas.", "Al personal de los organismos públicos vinculados a la Administración General del Estado."], "Art. 4 g) TREBEP. Los demás están incluidos en el ámbito del art. 2 (y el art. 3 para los locales).", "Personal del Centro Nacional de Inteligencia"),
 (TB, "Artículo 5", "Régimen jurídico", "Según el artículo 5 del TREBEP, el personal funcionario de la Sociedad Estatal Correos y Telégrafos se regirá:",
  ["Por sus normas específicas y supletoriamente por lo dispuesto en el Estatuto.", "Íntegramente por el Estatuto.", "Por la legislación laboral y las normas convencionales.", "Por la Ley 30/1984, sin aplicación del Estatuto."], "Art. 5 TREBEP.", "se regirá por sus normas específicas y supletoriamente por lo dispuesto en este Estatuto"),
 (TB, "Artículo 6", "Régimen jurídico", "Según el artículo 6 del TREBEP, en desarrollo del Estatuto, las leyes reguladoras de la Función Pública de la Administración General del Estado y de las comunidades autónomas las aprobarán:",
  ["Las Cortes Generales y las asambleas legislativas de las comunidades autónomas.", "El Gobierno y los Consejos de Gobierno de las comunidades autónomas.", "El Ministerio competente en materia de función pública.", "La Conferencia Sectorial de Administración Pública."], "Art. 6 TREBEP.", "las Cortes Generales y las asambleas legislativas de las comunidades autónomas aprobarán"),
 (TB, "Artículo 7", "Régimen jurídico", "Según el artículo 7 del TREBEP, en materia de permisos de nacimiento, adopción, del progenitor diferente de la madre biológica, de lactancia y parental, el personal laboral al servicio de las Administraciones públicas se regirá por:",
  ["Lo previsto en el propio Estatuto.", "El texto refundido de la Ley del Estatuto de los Trabajadores.", "El convenio colectivo aplicable.", "Lo que disponga cada Administración por reglamento."], "Art. 7, párrafo segundo, TREBEP.", "el personal laboral al servicio de las Administraciones públicas se regirá por lo previsto en el presente Estatuto"),
 (TB, "dfprimera", "Régimen jurídico", "Según su disposición final primera, las disposiciones del TREBEP que constituyen las bases del régimen estatutario de los funcionarios se dictan al amparo del artículo de la Constitución:",
  ["149.1.18.ª", "149.1.7.ª", "149.1.13.ª", "149.1.1.ª"], "DF 1.ª TREBEP: 18.ª para las bases del régimen estatutario; 7.ª para la legislación laboral; 13.ª para la planificación económica.", "al amparo del artículo 149.1.18.ª de la Constitución, constituyendo aquellas bases del régimen estatutario de los funcionarios"),
]
for k, art, cat, en, ops, ex, fr in Q: T.q(k, art, cat, en, ops, ex, fr)
T.real("L", 61, "Adquisición"); T.real("L", 62, "Pérdida"); T.real("P", 78, "Funcionarios interinos"); T.real("P", 81, "Régimen jurídico"); T.real("X", 67, "Funcionarios interinos")

# Flashcards
for q_, a_, cat in [
  ("Concepto de empleado público (art. 8.1 TREBEP)", "Quienes desempeñan funciones retribuidas en las Administraciones Públicas al servicio de los intereses generales.", "Concepto y clases"),
  ("Clases de empleados públicos (art. 8.2)", "Funcionarios de carrera, funcionarios interinos, personal laboral (fijo, por tiempo indefinido o temporal) y personal eventual.", "Concepto y clases"),
  ("Funcionario de carrera (art. 9.1): vínculo y carácter", "Nombramiento legal; relación estatutaria regulada por el Derecho Administrativo; servicios profesionales retribuidos de carácter permanente.", "Funcionarios de carrera"),
  ("Funciones reservadas en exclusiva a los funcionarios (art. 9.2)", "Las que impliquen participación directa o indirecta en el ejercicio de las potestades públicas o en la salvaguardia de los intereses generales del Estado y de las Administraciones Públicas.", "Funcionarios de carrera"),
  ("Funcionario interino (art. 10.1)", "Nombrado por razones expresamente justificadas de necesidad y urgencia, con carácter temporal, para funciones propias de funcionarios de carrera.", "Funcionarios interinos"),
  ("Los cuatro supuestos de interinidad y sus plazos (art. 10.1)", "Vacante: máx. 3 años · Sustitución: tiempo estrictamente necesario · Programas: 3 años + 12 meses · Exceso o acumulación de tareas: 9 meses en 18.", "Funcionarios interinos"),
  ("Principios de selección del interino (art. 10.2)", "Igualdad, mérito, capacidad, publicidad y celeridad; finalidad: cobertura inmediata del puesto.", "Funcionarios interinos"),
  ("Causas de fin de la interinidad (art. 10.3)", "Cobertura reglada del puesto; supresión o amortización; fin del plazo autorizado; fin de la causa. De oficio y sin compensación (más las del art. 63).", "Funcionarios interinos"),
  ("Compensación por incumplir el plazo máximo de permanencia (DA 17.ª.4)", "20 días de retribuciones fijas por año de servicio, máximo 12 mensualidades; no si el fin es disciplinario o por renuncia voluntaria.", "Funcionarios interinos"),
  ("Personal laboral (art. 11.1)", "Contrato de trabajo formalizado por escrito; fijo, por tiempo indefinido o temporal.", "Personal laboral"),
  ("Personal eventual (art. 12)", "Nombramiento no permanente; solo confianza o asesoramiento especial; nombramiento y cese libres; cesa con su autoridad; no es mérito.", "Personal eventual"),
  ("Personal directivo profesional (art. 13)", "Designación por mérito, capacidad e idoneidad, con publicidad y concurrencia; condiciones no negociables colectivamente; si es laboral, alta dirección.", "Personal directivo"),
  ("Requisitos sucesivos para adquirir la condición de funcionario de carrera (art. 62.1)", "Superar el proceso selectivo; nombramiento publicado en el Diario Oficial; acatamiento de la Constitución (y Estatuto y Ordenamiento); toma de posesión en plazo.", "Adquisición"),
  ("¿Quién nombra a los funcionarios de carrera de la AGE? (RD 364/1995, art. 25)", "El Secretario de Estado para la Administración Pública; publicación en el BOE; nunca más nombrados que plazas convocadas.", "Adquisición"),
  ("Causas de pérdida de la condición de funcionario (art. 63)", "Renuncia; pérdida de la nacionalidad; jubilación total; separación del servicio firme; inhabilitación absoluta o especial firme.", "Pérdida"),
  ("Renuncia (art. 64)", "Por escrito y aceptada expresamente; no se acepta con expediente disciplinario o auto de procesamiento o apertura de juicio oral; no impide volver a ingresar.", "Pérdida"),
  ("Inhabilitación absoluta vs. especial (art. 66)", "Absoluta: pérdida respecto de todos los empleos o cargos. Especial: respecto de los especificados en la sentencia.", "Pérdida"),
  ("Jubilación forzosa (art. 67.3)", "De oficio a los 65 años; prolongación como máximo hasta los 70, en los términos de las leyes de Función Pública.", "Jubilación"),
  ("Rehabilitación (art. 68)", "Nacionalidad o incapacidad permanente: se concede a solicitud, desaparecida la causa. Inhabilitación: excepcional, por los órganos de gobierno; silencio desestimatorio.", "Rehabilitación"),
  ("Normativa del personal laboral (art. 7)", "Legislación laboral, normas convencionales y preceptos del TREBEP que así lo dispongan; los permisos de nacimiento, adopción, lactancia y parental, por el TREBEP.", "Régimen jurídico"),
  ("Personal del art. 4 TREBEP", "Cortes y asambleas; órganos constitucionales y estatutarios; Justicia; militares; Fuerzas y Cuerpos de Seguridad; retribuidos por arancel; CNI; Banco de España y FGD: TREBEP solo si su legislación lo dispone.", "Régimen jurídico"),
  ("Títulos competenciales del TREBEP (DF 1.ª)", "Art. 149.1.18.ª (bases del régimen estatutario), 149.1.7.ª (legislación laboral) y 149.1.13.ª (planificación económica).", "Régimen jurídico"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Empleado público", "Quien desempeña funciones retribuidas en las Administraciones Públicas al servicio de los intereses generales (art. 8.1 TREBEP).", "s1", "Concepto y clases")
T.glos("Funcionario de carrera", "Vinculado a una Administración por nombramiento legal, en relación estatutaria de Derecho Administrativo, para servicios profesionales retribuidos permanentes (art. 9.1).", "s2", "Concepto y clases")
T.glos("Funcionario interino", "Nombrado por necesidad y urgencia expresamente justificadas, con carácter temporal, para funciones propias de funcionarios de carrera, en los cuatro supuestos del art. 10.1.", "s3", "Concepto y clases")
T.glos("Personal laboral", "Quien presta servicios retribuidos por las Administraciones en virtud de contrato de trabajo formalizado por escrito; fijo, por tiempo indefinido o temporal (art. 11.1).", "s4", "Concepto y clases")
T.glos("Personal eventual", "Nombrado con carácter no permanente solo para funciones de confianza o asesoramiento especial; nombramiento y cese libres (art. 12).", "s5", "Concepto y clases")
T.glos("Personal directivo profesional", "Quien desarrolla funciones directivas profesionales definidas en las normas de cada Administración; designación por mérito, capacidad e idoneidad (art. 13).", "s6", "Concepto y clases")
T.glos("Toma de posesión", "Último de los cuatro requisitos sucesivos para adquirir la condición de funcionario de carrera, dentro del plazo que se establezca (art. 62.1 d).", "s8", "Relación de servicio")
T.glos("Acatamiento", "Acto de acatamiento de la Constitución y, en su caso, del Estatuto de Autonomía y del resto del Ordenamiento Jurídico; requisito del art. 62.1 c).", "s8", "Relación de servicio")
T.glos("Renuncia", "Causa de pérdida de la condición de funcionario; por escrito y aceptada expresamente por la Administración; no inhabilita para reingresar (arts. 63 a y 64).", "s10", "Relación de servicio")
T.glos("Inhabilitación absoluta o especial", "Pena que, firme la sentencia, hace perder la condición de funcionario respecto de todos los cargos (absoluta) o de los especificados en la sentencia (especial) (art. 66).", "s10", "Relación de servicio")
T.glos("Jubilación forzosa", "Se declara de oficio a los sesenta y cinco años; cabe solicitar la prolongación hasta los setenta (art. 67.3).", "s10", "Relación de servicio")
T.glos("Rehabilitación", "Recuperación de la condición de funcionario perdida: concedida tras pérdida de nacionalidad o incapacidad permanente; excepcional tras inhabilitación (art. 68).", "s11", "Relación de servicio")
T.glos("Leyes de Función Pública", "Leyes de las Cortes Generales y de las asambleas legislativas autonómicas que desarrollan el TREBEP en cada Administración (art. 6).", "s15", "Régimen jurídico")

# Cronología (fechas de los metadatos del BOE)
T.hito("1978", "Constitución Española (27-12-1978; BOE de 29-12-1978)", "Arts. 23.2, 103.3 y 149.1.18.ª: acceso en igualdad, reserva de ley y bases del régimen estatutario", "normativo", "s12")
T.hito("1979", "Real Decreto 707/1979, de 5 de abril (BOE de 6-4-1979)", "Fórmula de juramento o promesa en la toma de posesión de cargos o funciones públicas", "normativo", "s8")
T.hito("1984", "Ley 30/1984, de 2 de agosto, de medidas para la reforma de la Función Pública (BOE de 3-8-1984)", "Arts. 1 y 15: ámbito y puestos que puede desempeñar el personal laboral en la Administración del Estado", "normativo", "s16")
T.hito("1995", "Real Decreto 364/1995, de 10 de marzo, Reglamento General de Ingreso (BOE de 10-4-1995)", "Art. 25: nombramiento de los funcionarios de carrera de la AGE", "normativo", "s8")
T.hito("2015", "Real Decreto Legislativo 5/2015, de 30 de octubre, texto refundido del Estatuto Básico del Empleado Público (BOE de 31-10-2015)", "Arts. 1 a 13 y 62 a 68: régimen jurídico, clases de personal, adquisición y pérdida", "normativo", "s1")
T.hito("2021", "Ley 20/2021, de 28 de diciembre, de medidas urgentes para la reducción de la temporalidad en el empleo público (BOE de 29-12-2021)", "Redacción vigente del art. 10 (interinos) y de la disposición adicional decimoséptima", "normativo", "s3")
T.hito("2025", "Real Decreto-ley 9/2025, de 29 de julio (BOE de 30-7-2025)", "Redacción vigente del art. 7 (permisos del personal laboral)", "normativo", "s15")

T.publicar()
