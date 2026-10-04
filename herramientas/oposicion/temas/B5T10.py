# -*- coding: utf-8 -*-
"""Tema V.10 (B5T10): Acceso al empleo público y provisión de puestos de trabajo de las
personas con discapacidad.
Método del I.2. Normas (textos consolidados del BOE): RDLeg 1/2013 (Ley General de derechos
de las personas con discapacidad, arts. 2 m y 4); TREBEP, art. 59; RDL 6/2023 (libro II,
función pública de la Administración del Estado: arts. 108, 113 y 115 y disposición
adicional decimoquinta); Real Decreto 2271/2004; Orden PJC/804/2025."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO.update({"LGD": "RDLeg 1/2013", "RD2271": "RD 2271/2004", "RDL6": "RDL 6/2023", "OPJC804": "Orden PJC/804/2025"})

T = Tema("B5T10",
  "Cuatro preguntas: I. Quién es persona con discapacidad y qué principios rigen su acceso (RDLeg 1/2013; RD 2271/2004; RDL 6/2023) · II. Cuántas plazas se reservan (TREBEP, art. 59; RDL 6/2023, art. 108; RD 2271/2004) · III. Cómo se adapta el proceso selectivo (Orden PJC/804/2025) · IV. Qué pasa después del ingreso: destino, adaptación del puesto y formación. Cada artículo: texto literal del BOE y ficha.",
  ["Discapacidad", "33 por ciento", "Cupo de reserva", "7 % (TREBEP)", "10 % (AGE)", "Discapacidad intelectual", "Ajustes razonables", "Adaptación de tiempos", "Adaptación de medios", "Orden PJC/804/2025", "Alteración del orden de prelación", "Adaptación del puesto", "Unidades de inclusión"])

T.ap("s0", "Mapa del tema: cuatro preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque V, tema 10):
> Acceso al empleo público y provisión de puestos de trabajo de las personas con discapacidad.

### El hilo conductor

| Bloque | Pregunta | Normas |
|---|---|---|
| **I** | ¿Quién es persona con discapacidad y qué principios rigen? | RDLeg 1/2013, arts. 2 m) y 4; RD 2271/2004, art. 1; RDL 6/2023, art. 113.1 y 2 |
| **II** | ¿Cuántas plazas se reservan y cómo? | TREBEP, art. 59.1; RDL 6/2023, arts. 108.4 y 113.3; RD 2271/2004, arts. 2 a 6 |
| **III** | ¿Cómo se adapta el proceso selectivo? | TREBEP, art. 59.2; RDL 6/2023, arts. 113.4 y 115.2; RD 2271/2004, arts. 7 y 8; Orden PJC/804/2025 |
| **IV** | ¿Qué pasa después del ingreso? (provisión, puesto y formación) | RD 2271/2004, arts. 9 a 13; RDL 6/2023, disposición adicional decimoquinta |

!> **La idea que une los cuatro bloques:** la persona con discapacidad (grado **igual o superior al 33 %**) accede al empleo público en **igualdad de condiciones**, con dos herramientas: un **cupo de reserva** de plazas y las **adaptaciones y ajustes razonables** de tiempos y medios. Una vez dentro, puede pedir **alterar el orden** para elegir destino y la **adaptación del puesto**.

?> **Aviso: tres porcentajes de reserva en tres normas vigentes.** El RD 2271/2004 dice «**no inferior al cinco por ciento**» (texto de 2004, no actualizado); el TREBEP, norma básica, «**no inferior al siete por ciento**» (art. 59.1); y el RDL 6/2023, para la **Administración del Estado**, «**no inferior al diez por ciento**» (art. 108.4). Se citan los tres literalmente (→ II.2). En el examen, fíjate en **qué norma** cita el enunciado.
""")

# =============================================================================
T.ap("bI", "I. ¿Quién es persona con discapacidad y qué principios rigen su acceso?", donde(
  "Primera pregunta del tema: el **concepto** legal de persona con discapacidad (y de ajuste razonable) y los **principios** que inspiran su acceso al empleo público.",
  ["1 Concepto de persona con discapacidad y de ajuste razonable (RDLeg 1/2013, arts. 2 m y 4)", "2 Derecho de acceso y principios (RD 2271/2004, art. 1; RDL 6/2023, art. 113.1 y 2)"]))

T.ap("s1", "I.1 Concepto de persona con discapacidad y de ajuste razonable (RDLeg 1/2013, arts. 2 m y 4)", f"""
{unidad("1.1 Ajustes razonables (art. 2 m)",
  lit("LGD", "Artículo 2", ["que no impongan una carga desproporcionada o indebida", "en igualdad de condiciones con las demás"], solo=[14], titulo="Artículo 2 m) (RDLeg 1/2013, Ley General de derechos de las personas con discapacidad)"),
  fichab("Definición legal de ajuste razonable", "—",
         "Modificaciones y adaptaciones **necesarias y adecuadas** del ambiente físico, social y actitudinal a las necesidades de la persona, en un **caso particular**",
         "—", "Límite: que **no** impongan una **carga desproporcionada o indebida**. La Orden PJC/804/2025 remite a esta definición (→ III.3.1)."))}

{unidad("1.2 Quién es persona con discapacidad (art. 4)",
  lit("LGD", "Artículo 4", ["previsiblemente permanentes", "un grado de discapacidad igual o superior al 33 por ciento", "pensión de incapacidad permanente en el grado de total, absoluta o gran invalidez", "tendrá validez en todo el territorio nacional"], solo=[1, 3, 4, 5, 6]),
  ficha(["::Personas con discapacidad:", "Concepto general: deficiencias físicas, mentales, intelectuales o sensoriales **previsiblemente permanentes** que, con las barreras, pueden impedir su participación plena (4.1)", "A efectos de la ley: grado reconocido **igual o superior al 33 por ciento** (4.2)"],
        "Equiparación al 33 % (a ciertos efectos): pensionistas de **incapacidad permanente total, absoluta o gran invalidez** y de clases pasivas por incapacidad (4.2, párrafo 2.º)",
        "El grado lo reconoce el **órgano competente**; la acreditación vale en **todo el territorio nacional** (4.3)",
        "—",
        "El umbral que usan todas las normas de este tema es el **33 %**. El art. 59.1 TREBEP remite precisamente al **apartado 2** de este artículo (→ II.1)."))}
""", 2)

T.ap("s2", "I.2 Derecho de acceso y principios (RD 2271/2004, art. 1; RDL 6/2023, art. 113.1 y 2)", f"""
{unidad("2.1 Derecho de acceso y principios del RD 2271/2004 (art. 1)",
  lit("RD2271", "Artículo 1", ["tendrán derecho a acceder al empleo público", "igual o superior al 33 por ciento", "igualdad de oportunidades, no discriminación, accesibilidad universal y compensación de desventajas"]),
  ficha("Las personas con **cualquier tipo de discapacidad**",
        "Derecho a **acceder al empleo público** en las condiciones del real decreto",
        "Ámbito: el personal del art. 1.1 de la Ley 30/1984 (Administración del Estado); **supletorio** para el resto del sector público (disposición adicional única)",
        "—",
        "**Cuatro** principios: igualdad de oportunidades, no discriminación, accesibilidad universal y **compensación de desventajas**. Nota: el art. 1.1 remite aún a la Ley 51/2003 y habla de «minusvalía»; hoy rige el concepto del RDLeg 1/2013 (→ I.1.2), que usa «persona con discapacidad»."))}

{unidad("2.2 Principios del RDL 6/2023 para la Administración del Estado (art. 113.1 y 2)",
  lit("RDL6", "a1-25", ["igualdad de oportunidades, no discriminación y accesibilidad universal", "en igualdad de condiciones que el resto de las personas aspirantes", "la compatibilidad con el desempeño de las funciones y tareas genéricas"], solo=[1, 2], titulo="Artículo 113. Acceso al empleo público de personas con discapacidad (RDL 6/2023)"),
  fichab("Acceso de las personas con discapacidad en la Administración del Estado",
         "Personas con discapacidad, como **personal funcionario o laboral**",
         "Participan en los procesos selectivos **en igualdad de condiciones** que el resto",
         "—",
         "Deben acreditar **dos** cosas: el **grado** de discapacidad y la **compatibilidad** con las funciones y tareas genéricas."))}

{resumen([
  "Persona con discapacidad: grado reconocido **igual o superior al 33 %** (RDLeg 1/2013, art. 4.2); acreditación válida en todo el territorio.",
  "Ajuste razonable: adaptación necesaria y adecuada que **no** imponga una **carga desproporcionada o indebida** (art. 2 m).",
  "Principios: igualdad de oportunidades, no discriminación, accesibilidad universal (y compensación de desventajas en el RD 2271/2004).",
  "Se acredita el **grado** y la **compatibilidad** con las tareas (RDL 6/2023, art. 113.2)."],
  "Siguiente: II. ¿Cuántas plazas se reservan y cómo?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Cuántas plazas se reservan y cómo? (TREBEP, art. 59.1; RDL 6/2023; RD 2271/2004)", donde(
  "Segunda pregunta. La reserva de plazas: el **porcentaje** que fija cada norma, la parte para **discapacidad intelectual** y cómo se distribuyen y acumulan las plazas.",
  ["1 La reserva básica del TREBEP (art. 59.1)", "2 La reserva en la Administración del Estado (RDL 6/2023, arts. 108.4 y 113.3)", "3 El desarrollo del RD 2271/2004 (arts. 2 a 6)"]))

T.ap("s3", "II.1 La reserva básica del TREBEP (art. 59.1)", f"""
{unidad("1.1 Cupo no inferior al siete por ciento (art. 59.1)",
  lit("TREBEP", "Artículo 59", ["un cupo no inferior al siete por ciento de las vacantes", "apartado 2 del artículo 4", "el dos por ciento de los efectivos totales en cada Administración Pública", "al menos, el dos por ciento de las plazas ofertadas lo sea para ser cubiertas por personas que acrediten discapacidad intelectual"], solo=[1, 2]),
  fichab("Reserva de plazas en todas las Administraciones (norma básica)",
         "Personas con discapacidad del art. 4.2 del RDLeg 1/2013 que **superen** el proceso y acrediten discapacidad y **compatibilidad**",
         ["Cupo **no inferior al 7 %** de las vacantes de la oferta", "Dentro del 7 %, **al menos el 2 %** de las plazas para **discapacidad intelectual**; el resto, para cualquier otra discapacidad", "Objetivo: alcanzar progresivamente el **2 % de los efectivos totales** de cada Administración"],
         "7 % de reserva · 2 % intelectual · objetivo 2 % de efectivos",
         "Dos «2 %» distintos: el **2 % de las plazas** (intelectual) y el **2 % de los efectivos** (objetivo). La reserva es «**no inferior**» (mínimo)."))}
""", 2)

T.ap("s4", "II.2 La reserva en la Administración del Estado (RDL 6/2023, arts. 108.4 y 113.3)", f"""
{unidad("2.1 Cupo no inferior al diez por ciento (art. 108.4)",
  lit("RDL6", "a1-20", ["un porcentaje no inferior al diez por ciento de las plazas convocadas", "al menos el dos por ciento de las plazas ofertadas lo sea para ser cubiertas por personas que acrediten discapacidad intelectual", "pudiendo concentrarse las plazas reservadas"], solo=[6, 7, 8], titulo="Artículo 108. Oferta de Empleo Público (RDL 6/2023), apartado 4"),
  fichab("Reserva en la oferta de empleo público de la Administración del Estado",
         "Personas con discapacidad que superen las pruebas y acrediten discapacidad y compatibilidad",
         ["Cupo **no inferior al 10 %** de las plazas convocadas", "Dentro del 10 %, **al menos el 2 %** para **discapacidad intelectual**", "La reserva se calcula sobre el **total** de la oferta y puede **concentrarse** en los cuerpos, escalas o categorías que mejor se adapten"],
         "10 % de reserva · 2 % intelectual · objetivo 2 % de efectivos",
         "**AGE: 10 %** (RDL 6/2023); **básico: 7 %** (TREBEP). La reserva puede **concentrarse** en determinadas convocatorias."))}

{unidad("2.2 Convocatorias específicas para discapacidad intelectual (art. 113.3)",
  lit("RDL6", "a1-25", ["igual o superior al treinta y tres por cien", "mediante la convocatoria de pruebas selectivas específicas e independientes"], solo=[3], titulo="Artículo 113. Acceso al empleo público de personas con discapacidad (RDL 6/2023), apartado 3"),
  fichab("Plazas para personas con discapacidad intelectual", "Personas con discapacidad intelectual con grado **igual o superior al 33 %**",
         "Pruebas selectivas **específicas e independientes**", "—",
         "El umbral es el mismo **33 %** (pregunta oficial X 88, → Cierre 1), no un porcentaje mayor."))}

*Cuadro de los porcentajes de reserva (esquema de elaboración propia sobre los artículos citados; no es texto legal).*

| Norma | Ámbito | Reserva mínima | Discapacidad intelectual |
|---|---|---|---|
| RD 2271/2004, art. 2.1 | Administración del Estado (texto de 2004) | 5 % de las vacantes | — |
| TREBEP, art. 59.1 | Todas las Administraciones (básico) | **7 %** de las vacantes | al menos 2 % de las plazas |
| RDL 6/2023, art. 108.4 | Administración del Estado | **10 %** de las plazas convocadas | al menos 2 % de las plazas |
""", 2)

T.ap("s5", "II.3 El desarrollo del RD 2271/2004 (arts. 2 a 6)", f"""
{unidad("3.1 Reserva y forma de optar (art. 2)",
  lit("RD2271", "Artículo 2", ["no inferior al cinco por ciento", "habrá de formularse en la solicitud de participación", "dentro de las convocatorias de plazas de ingreso ordinario o convocarse en un turno independiente"]),
  fichab("Opción por el cupo y tipos de convocatoria",
         "El aspirante opta; en la AGE, el Ministerio competente en función pública decide el tipo de convocatoria (texto: «Ministerio de Administraciones Públicas»)",
         ["La opción se hace **en la solicitud**, con declaración expresa del grado", "Plazas reservadas **dentro de la convocatoria ordinaria** o en **turno independiente**"],
         "Texto del RD: 5 % (→ II.2 para el porcentaje vigente en el Estado)",
         "La opción por el cupo se formula **en la solicitud de participación**, no después."))}

{unidad("3.2 Convocatoria ordinaria con reserva (art. 3)",
  lit("RD2271", "Artículo 3", ["será incluido por su orden de puntuación en el sistema de acceso general", "no alcanzaran la tasa del tres por ciento de las plazas convocadas", "se acumularán al cupo del cinco por ciento de la oferta siguiente, con un límite máximo del 10 por ciento", "Las pruebas selectivas tendrán idéntico contenido para todos los aspirantes"]),
  fichab("Funcionamiento de la reserva dentro de la convocatoria ordinaria",
         "El Ministerio competente distribuye la reserva entre cuerpos, escalas o categorías",
         ["Aspirante del cupo que aprueba sin plaza y con más nota que otros del acceso general → entra por su orden en el **acceso general** (3.2)", "**Acumulación**: si las plazas cubiertas no llegan al **3 %** de las convocadas, las no cubiertas se acumulan al cupo del **5 %** de la **oferta siguiente**, con un **límite del 10 %** (3.2)", "Pruebas de **idéntico contenido**, con adaptaciones; relación final **única** por puntuación (3.3)"],
         "3 % (tasa) · 5 % (cupo) · 10 % (límite)",
         "Tres cifras en la misma frase: **tres**, **cinco** y **10** por ciento (pregunta oficial X 104, → Cierre 1)."))}

{unidad("3.3 Turno independiente, promoción interna y personal temporal (arts. 4 a 6)",
  lit("RD2271", "Artículo 4", ["convocatorias independientes, no supeditadas a las ordinarias", "el mismo contenido y grado de exigencia"]),
  lit("RD2271", "Artículo 5", ["no inferior al cinco por ciento de las vacantes", "se acumularán a las del turno ordinario de promoción interna"]),
  lit("RD2271", "Artículo 6", ["20 plazas o más en un mismo ámbito de participación", "se acumularán a las libres"]),
  fichab("Otras modalidades de reserva",
         "El órgano convocante solicita las convocatorias independientes al Ministerio competente",
         ["**Turno independiente**: mismas pruebas y exigencia que las ordinarias, con adaptaciones (art. 4)", "**Promoción interna**: reserva **no inferior al 5 %**; las desiertas se acumulan al **turno ordinario de promoción interna** (art. 5)", "**Personal temporal** con fase de oposición y **20 plazas o más**: reserva del 5 %; las vacantes se acumulan a las **libres** (art. 6)"],
         "Temporal: a partir de **20 plazas** en un mismo ámbito",
         "Destino de las plazas no cubiertas: en el **ordinario**, a la **oferta siguiente** (con límites); en **promoción interna**, al turno ordinario de **promoción interna**; en el **temporal**, a las **libres**."))}

{resumen([
  "TREBEP: reserva **no inferior al 7 %**, con al menos el **2 %** de las plazas para discapacidad **intelectual** (art. 59.1).",
  "Administración del Estado: **no inferior al 10 %**, con el mismo 2 % intelectual y posibilidad de **concentrar** plazas (RDL 6/2023, art. 108.4); discapacidad intelectual con **33 %**: pruebas **específicas e independientes** (art. 113.3).",
  "RD 2271/2004: opción en la **solicitud**; acumulación si no se llega al **3 %** → al cupo del **5 %** de la oferta siguiente, máximo **10 %** (art. 3.2).",
  "Promoción interna: desiertas al turno de promoción interna; temporal (20 o más plazas): a las libres."],
  "Siguiente: III. ¿Cómo se adapta el proceso selectivo?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Cómo se adapta el proceso selectivo? (TREBEP, art. 59.2; RDL 6/2023; RD 2271/2004; Orden PJC/804/2025)", donde(
  "Tercera pregunta. La igualdad real en las pruebas se consigue con **adaptaciones de tiempos y medios** y otros **ajustes razonables**: quién los pide, quién decide y en qué consisten.",
  ["1 El mandato general (TREBEP, art. 59.2; RDL 6/2023, arts. 113.4 y 115.2)", "2 Admisión y adaptaciones en el RD 2271/2004 (arts. 7 y 8)", "3 Los criterios de la Orden PJC/804/2025"]))

T.ap("s6", "III.1 El mandato general (TREBEP, art. 59.2; RDL 6/2023, arts. 113.4 y 115.2)", f"""
{unidad("1.1 Adaptaciones en el proceso y en el puesto (TREBEP, art. 59.2)",
  lit("TREBEP", "Artículo 59", ["las adaptaciones y ajustes razonables de tiempos y medios en el proceso selectivo", "las adaptaciones en el puesto de trabajo"], solo=[3]),
  fichab("Obligación de cada Administración", "**Cada Administración Pública**",
         ["**Durante** el proceso: adaptaciones y ajustes razonables de **tiempos y medios**", "**Después**: adaptaciones en el **puesto de trabajo**"], "—",
         "Dos momentos: el **proceso selectivo** y el **puesto de trabajo** (→ IV)."))}

{unidad("1.2 Prótesis, adaptaciones y órganos de selección en el Estado (RDL 6/2023, arts. 113.4 y 115.2)",
  lit("RDL6", "a1-25", ["permitiéndose el uso de prótesis, incluidas las auditivas", "realizará las adaptaciones precisas, incluidas medidas de accesibilidad, ajustes razonables y otros apoyos"], solo=[4], titulo="Artículo 113. Acceso al empleo público de personas con discapacidad (RDL 6/2023), apartado 4"),
  lit("RDL6", "a1-27", ["Se promoverá, igualmente, la participación en los mismos de personas con discapacidad"], solo=[2, 3], titulo="Artículo 115. Órganos de selección (RDL 6/2023), apartado 2"),
  fichab("Medidas de la Administración del Estado", "La **Administración del Estado**; los órganos de selección",
         ["Adaptaciones y ajustes de **tiempo y medios** en los procesos", "Uso de **prótesis, incluidas las auditivas**, por quien las precise y lo acredite", "Tras el proceso: adaptaciones del **puesto** (accesibilidad, ajustes y apoyos)", "Se **promueve** la participación de personas con discapacidad en los **órganos de selección**, en particular si hay turno de reserva"],
         "—", "Las **prótesis auditivas** se mencionan expresamente. La presencia en los tribunales se «**promoverá**» (no es obligatoria)."))}
""", 2)

T.ap("s7", "III.2 Admisión y adaptaciones en el RD 2271/2004 (arts. 7 y 8)", f"""
{unidad("2.1 Admisión en igualdad de condiciones (art. 7)",
  lit("RD2271", "Artículo 7", ["serán admitidas en igualdad de condiciones que los demás aspirantes"]),
  fichab("Admisión a las pruebas", "Personas con discapacidad aspirantes en la AGE", "Admisión **en igualdad de condiciones**", "—", "No hay requisitos de admisión distintos por la discapacidad."))}

{unidad("2.2 Adaptaciones de tiempos y medios (art. 8)",
  lit("RD2271", "Artículo 8", ["incluyendo los cursos de formación o períodos de prácticas", "la correspondiente petición concreta en la solicitud de participación", "la concesión de un tiempo adicional", "de los medios materiales y humanos", "no se otorgará de forma automática", "guarde relación directa con la prueba a realizar"]),
  fichab("Adaptaciones y ajustes razonables en las pruebas",
         "Aspirantes con grado **igual o superior al 33 %** que lo **soliciten**; el órgano de selección puede pedir informe a los órganos técnicos",
         ["**Tiempos**: tiempo **adicional** para los ejercicios (8.3)", "**Medios**: medios materiales y humanos, asistencias y apoyos, ayudas técnicas y tecnologías asistidas, accesibilidad de la información y del recinto (8.4)", "Alcanzan también a los **cursos de formación** y **prácticas** (8.1)", "Petición **concreta** en la **solicitud** (8.2)"],
         "—",
         "**No** se conceden de forma **automática**: solo si la discapacidad guarda **relación directa** con la prueba (8.5)."))}
""", 2)

T.ap("s8", "III.3 Los criterios de la Orden PJC/804/2025", f"""
{unidad("3.1 Objeto, ajustes y ámbito (arts. 1 a 3)",
  lit("OPJC804", "a1", ["en el ámbito del personal civil de la Administración del Estado"], titulo="Artículo 1. Objeto (Orden PJC/804/2025)"),
  lit("OPJC804", "a2", ["el artículo 2 letra m)", "de los medios materiales y humanos", "La concesión de un tiempo adicional", "no resueltas mediante las adaptaciones genéricas de medios y tiempos"], titulo="Artículo 2. Definición de ajustes razonables (Orden PJC/804/2025)"),
  fichab("Criterios generales de adaptación en el personal civil del Estado",
         "Procesos de acceso al empleo público del **personal civil** de la Administración del Estado (art. 3)",
         ["Ajustes razonables: los del art. 2 m) del RDLeg 1/2013 (→ I.1.1)", "a) **Medios**: materiales y humanos, asistencias, productos de apoyo, tecnologías asistidas y accesibilidad", "b) **Tiempo adicional**", "c) Otros **ajustes razonables** no resueltos con las adaptaciones genéricas"],
         "—", "Tres tipos: **medios**, **tiempos** y **otros ajustes**."))}

{unidad("3.2 Personas beneficiarias (art. 4)",
  lit("OPJC804", "a4", ["igual o superior al 33 por ciento", "aun sin contar con un reconocimiento oficial del grado de discapacidad", "solo las adaptaciones de medios y otros ajustes razonables"], titulo="Artículo 4. Personas beneficiarias (Orden PJC/804/2025)"),
  fichab("Quién puede pedir adaptaciones",
         ["Personas con grado **igual o superior al 33 %** (art. 4.2 RDLeg 1/2013)", "Personas **sin reconocimiento oficial** que acrediten su necesidad de apoyo por cualquier medio admitido en Derecho"],
         "Sin grado reconocido: **solo** adaptaciones de **medios** y otros ajustes (no de **tiempos**)", "—",
         "Sin reconocimiento oficial **no** cabe la adaptación de **tiempos**."))}

{unidad("3.3 Medios humanos y recursos de autonomía personal (arts. 5 y 6)",
  lit("OPJC804", "a5", ["Asistente personal", "personas sordas, con discapacidad auditiva y sordociegas"], titulo="Artículo 5. Adaptaciones de medios humanos (Orden PJC/804/2025)"),
  lit("OPJC804", "a6", ["tendrán derecho a portar y usar sin restricciones los productos de apoyo, órtesis y prótesis", "perro de asistencia", "en un plazo no inferior a diez días hábiles"], titulo="Artículo 6. Garantía de recursos y apoyos para la autonomía personal (Orden PJC/804/2025)"),
  fichab("Medios humanos y apoyos personales",
         "La persona con discapacidad; el órgano de selección puede pedir acreditación",
         ["**Medios humanos** (art. 5): **asistente personal**; personal de accesibilidad para personas sordas, con discapacidad auditiva y sordociegas; otro personal de apoyo con regulación específica", "Derecho a **portar y usar** productos de apoyo, órtesis y prótesis; acceso con **perro de asistencia** (art. 6)"],
         "Acreditación del recurso: plazo **no inferior a 10 días hábiles**",
         "El **asistente personal** es medio **humano** (pregunta oficial L 81, → Cierre 1); el tiempo adicional y los productos de apoyo **no** lo son."))}

{unidad("3.4 Petición y concesión (arts. 7 y 8)",
  lit("OPJC804", "a7", ["formular petición concreta en la solicitud de participación", "Dictamen Técnico Facultativo"], titulo="Artículo 7. Petición de adaptación de medios y tiempos y ajustes razonables (Orden PJC/804/2025)"),
  lit("OPJC804", "a8", ["guarde relación con la prueba a realizar", "Corresponde a los órganos de selección resolver", "Criterios generales para las adaptaciones de tiempos en pruebas orales y escritas según deficiencias y grados de discapacidad", "en el plazo de diez días hábiles", "del modo más favorable a la garantía de la igualdad de oportunidades"], titulo="Artículo 8. Criterios y procesos aplicables para la concesión (Orden PJC/804/2025)"),
  fichab("Procedimiento de las adaptaciones",
         ["La persona aspirante lo pide **en la solicitud**, con el **Dictamen Técnico Facultativo**", "Resuelven los **órganos de selección**", "Pueden pedir informes a órganos técnicos, a las **unidades de inclusión** (→ IV.2.2) y a organizaciones de la discapacidad"],
         ["Solo si la discapacidad **guarda relación** con la prueba (8.2)", "Baremo de **tiempos** en los anexos (8.3)", "Casos no previstos: del modo **más favorable** a la igualdad de oportunidades (8.7)"],
         "Informe de los órganos técnicos: **10 días hábiles**",
         "Decide el **órgano de selección**, no el órgano convocante. Documento clave: **Dictamen Técnico Facultativo**."))}

{resumen([
  "TREBEP, art. 59.2: cada Administración adapta **tiempos y medios** en el proceso y, después, el **puesto**.",
  "RD 2271/2004, art. 8: adaptaciones a petición, **no automáticas**, solo si la discapacidad tiene **relación directa** con la prueba.",
  "Orden PJC/804/2025: medios, tiempos y otros ajustes; sin grado reconocido, **solo medios** y ajustes; medios humanos: **asistente personal** y otros.",
  "Resuelve el **órgano de selección**, con el **Dictamen Técnico Facultativo**; en caso de duda, lo más favorable a la igualdad."],
  "Siguiente: IV. ¿Qué pasa después del ingreso?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Qué pasa después del ingreso? Provisión, adaptación del puesto y formación (RD 2271/2004, arts. 9 a 13; RDL 6/2023)", donde(
  "Cuarta pregunta. Superado el proceso, la **provisión de puestos**: elección del destino, **adaptación del puesto**, formación y seguimiento.",
  ["1 Elección de destino y adaptación del puesto (RD 2271/2004, arts. 9 y 10)", "2 Formación, colaboración, seguimiento y unidades de inclusión (RD 2271/2004, arts. 11 a 13; RDL 6/2023, disposición adicional decimoquinta)"]))

T.ap("s9", "IV.1 Elección de destino y adaptación del puesto (RD 2271/2004, arts. 9 y 10)", f"""
{unidad("1.1 Alteración del orden de prelación (art. 9)",
  lit("RD2271", "Artículo 9", ["podrán solicitar al órgano convocante la alteración del orden de prelación para la elección de las plazas", "por motivos de dependencia personal, dificultades de desplazamiento u otras análogas"]),
  fichab("Elección de destino de quien ingresa por el cupo",
         "Quienes ingresen habiendo sido admitidos en la convocatoria **ordinaria** con plazas reservadas; decide el **órgano convocante**",
         "Pedir la **alteración del orden de prelación** para elegir plaza dentro del ámbito territorial de la convocatoria",
         "—",
         "Motivos: **dependencia personal**, **dificultades de desplazamiento** u otras análogas, **acreditados**. No se pide «un destino en la provincia de residencia» (pregunta oficial L 80, → Cierre 1)."))}

{unidad("1.2 Adaptación del puesto (art. 10)",
  lit("RD2271", "Artículo 10", ["podrán pedir la adaptación del puesto o de los puestos de trabajo", "un informe expedido por el órgano competente en la materia", "será el encargado de la valoración, la realización y la financiación de las adaptaciones"]),
  fichab("Adaptación del puesto de trabajo",
         "Empleados públicos con discapacidad; valora, realiza y **financia** el **ministerio u organismo** de adscripción del puesto",
         ["Se pide en las solicitudes de **destino** (nuevo ingreso o promoción interna) o de **provisión**", "Con **informe** del órgano competente sobre procedencia y compatibilidad", "La compatibilidad se valora **teniendo en cuenta** las adaptaciones posibles"],
         "—", "Paga la adaptación el **ministerio u organismo** al que está adscrito el **puesto**."))}
""", 2)

T.ap("s10", "IV.2 Formación, colaboración, seguimiento y unidades de inclusión (RD 2271/2004, arts. 11 a 13; RDL 6/2023, disposición adicional decimoquinta)", f"""
{unidad("2.1 Formación, colaboración e informe anual (arts. 11 a 13)",
  lit("RD2271", "Artículo 11", ["igual o superior al 33 por ciento", "que sólo podrá denegar cuando suponga una carga desproporcionada", "cursos de formación destinados únicamente a personas con discapacidad"]),
  lit("RD2271", "Artículo 12", ["proyectos de empleo con apoyo"]),
  lit("RD2271", "Artículo 13", ["un informe balance", "a la Comisión Superior de Personal y al Consejo Nacional de la Discapacidad"]),
  fichab("Medidas de integración en el empleo",
         "La Administración; el Ministerio competente elabora el informe",
         ["**Formación**: la discapacidad del 33 % es **criterio de valoración** para los cursos; adaptaciones en los cursos; cursos **solo** para personas con discapacidad (art. 11)", "**Convenios o contratos**, también con asociaciones, para proyectos de **empleo con apoyo** (art. 12)", "**Indicadores** y **informe balance anual** (art. 13)"],
         "Informe balance: **anual**",
         "La adaptación en los cursos solo se deniega por **carga desproporcionada**. El informe va a la **Comisión Superior de Personal** y al **Consejo Nacional de la Discapacidad**."))}

{unidad("2.2 Unidades de inclusión del personal con discapacidad (RDL 6/2023, disposición adicional decimoquinta)",
  lit("RDL6", "da-15", ["En cada uno de los departamentos ministeriales se constituirá una unidad de inclusión", "adscritas a la Subsecretaría", "asegurar las medidas de adaptación de puesto de trabajo"], titulo="Disposición adicional decimoquinta (RDL 6/2023). Unidades de inclusión del personal con discapacidad"),
  fichab("Unidades de inclusión", "Una en **cada departamento ministerial**, adscrita a la **Subsecretaría**",
         ["Apoyo especializado en inclusión", "Asegurar la **adaptación del puesto** y el desarrollo profesional", "Seguimiento de las medidas de las ofertas de empleo y **estadísticas**"],
         "—", "Una **por ministerio**, adscrita a la **Subsecretaría**. Pueden informar a los órganos de selección (→ III.3.4)."))}

{resumen([
  "Quien ingresa por el cupo en la convocatoria ordinaria puede pedir **alterar el orden de prelación** para elegir plaza, por **dependencia personal, dificultades de desplazamiento** u otras análogas (art. 9).",
  "Adaptación del **puesto**: se pide con informe; la valora, realiza y **financia** el ministerio u organismo del puesto (art. 10).",
  "Formación con criterio preferente y adaptaciones; empleo con apoyo; **informe balance anual** (arts. 11 a 13).",
  "**Unidades de inclusión** en cada ministerio, adscritas a la **Subsecretaría** (RDL 6/2023, disposición adicional decimoquinta)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX = [
 ("L", 80, "Alteración del orden de prelación (→ IV.1.1)", {
   "a": "El art. 9 no prevé pedir un destino en la **provincia** de residencia: lo que se pide es alterar el **orden de prelación** dentro del ámbito de la convocatoria.",
   "b": f"Literal del art. 9: {c('RD2271', 'Artículo 9', 'podrán solicitar al órgano convocante la alteración del orden de prelación para la elección de las plazas dentro del ámbito territorial que se determine en la convocatoria, por motivos de dependencia personal, dificultades de desplazamiento u otras análogas')}.",
   "c": "Tampoco un destino en la **Comunidad Autónoma** de residencia: el objeto es el **orden de prelación**.",
   "d": "Tampoco un destino en la **ciudad** de residencia: el objeto es el **orden de prelación**."},
   [("alteración del orden de prelación", "RD2271", "Artículo 9", "la alteración del orden de prelación para la elección de las plazas"),
    ("dificultades de desplazamiento", "RD2271", "Artículo 9", "dificultades de desplazamiento")]),
 ("L", 81, "Adaptaciones de medios humanos (→ III.3.3)", {
   "a": f"Literal del art. 5 a): {c('OPJC804', 'a5', 'Asistente personal')}.",
   "b": f"Es la adaptación de **tiempos**, no de medios humanos: {c('OPJC804', 'a2', 'La concesión de un tiempo adicional para la realización de los ejercicios correspondientes a las pruebas selectivas')} (art. 2.2 b).",
   "c": "Los **medios materiales** son una adaptación de medios del art. 2.2 a), pero no de medios **humanos** (art. 5).",
   "d": "Los **productos de apoyo y tecnologías asistidas** están en el art. 2.2 a), no entre los medios **humanos** del art. 5."},
   [("Un asistente personal", "OPJC804", "a5", "Asistente personal")]),
 ("X", 88, "Discapacidad intelectual: grado del 33 % (→ II.2.2)", {
   "a": f"Literal del art. 113.3: {c('RDL6', 'a1-25', 'siempre que éstas tengan reconocido un grado de discapacidad igual o superior al treinta y tres por cien')}.",
   "b": "Cambia el porcentaje: la ley dice **treinta y tres**, no cuarenta y dos.",
   "c": "Cambia el porcentaje: la ley dice **treinta y tres**, no cincuenta y uno.",
   "d": "Cambia el porcentaje: la ley dice **treinta y tres**, no sesenta."},
   [("treinta y tres por cien", "RDL6", "a1-25", "igual o superior al treinta y tres por cien")]),
 ("X", 104, "Acumulación de las plazas no cubiertas (→ II.3.2)", {
   "a": f"Literal del art. 3.2 del RD 2271/2004: {c('RD2271', 'Artículo 3', 'Si las plazas reservadas y que han sido cubiertas por las personas con discapacidad no alcanzaran la tasa del tres por ciento de las plazas convocadas, las plazas no cubiertas se acumularán al cupo del cinco por ciento de la oferta siguiente, con un límite máximo del 10 por ciento')}.",
   "b": "Cambia la tasa (cincuenta por ciento) y el cupo (diez por ciento): el RD dice **tres** y **cinco**.",
   "c": "Invierte la regla: las plazas **sí** se acumulan a la oferta siguiente.",
   "d": "Cambia la tasa (cinco), el cupo (diez) y el límite (50 por ciento): el RD dice **tres**, **cinco** y **10**."},
   [("tasa del tres por ciento", "RD2271", "Artículo 3", "no alcanzaran la tasa del tres por ciento de las plazas convocadas"),
    ("cupo del cinco por ciento de la oferta siguiente, con un límite máximo del 10 por ciento", "RD2271", "Artículo 3", "se acumularán al cupo del cinco por ciento de la oferta siguiente, con un límite máximo del 10 por ciento")]),
]
bloques = []
for cod, n, tit, por, ap_ in EX:
    bloques += [f"### {('GACE-L' if cod == 'L' else 'GACE-P' if cod == 'P' else 'GACE-L extraordinario')} 2025, pregunta {n} · {tit}", examen(cod, n, por, ap_)]
T.ap("s11", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join(
  ["En los primeros ejercicios de **2025** cayeron **cuatro** preguntas de este tema (dos en el turno libre y dos en el extraordinario), todas literales. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal."]
  + bloques + ["### Cómo se pregunta", "!> Cambian **porcentajes** (33 %, 3/5/10 %), el **objeto** de lo que se pide (orden de prelación frente a «un destino en la provincia») o el **tipo** de adaptación (medios humanos frente a tiempos o medios materiales). Fíjate en la **norma** que cita el enunciado: la reserva es del 5 % en el RD 2271/2004, del 7 % en el TREBEP y del 10 % en el RDL 6/2023."]))

T.ap("s12", "Cierre 2. Repaso en 10 minutos (por bloques)", """
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Concepto y principios | Grado **≥ 33 %** (RDLeg 1/2013, art. 4.2); ajuste razonable sin carga desproporcionada | Acreditar **grado** y **compatibilidad** |
| II. Reserva | TREBEP **7 %** (2 % intelectual); AGE **10 %** (RDL 6/2023); RD 2271/2004 **5 %** | Acumulación: **3 %** → cupo del **5 %**, máximo **10 %**; intelectual con **33 %**, pruebas **específicas e independientes** |
| III. Adaptaciones | Tiempos, medios y otros ajustes; no automáticas; resuelve el **órgano de selección** | Medios humanos: **asistente personal** |
| IV. Después del ingreso | Orden de prelación; adaptación del puesto; formación; unidades de inclusión | Alteración del orden por **dependencia personal** o **dificultades de desplazamiento** |

?> **Trampas frecuentes:** «la reserva del TREBEP es del 10 %» (es del **7 %**; el 10 % es del Estado, RDL 6/2023); «discapacidad intelectual: 51 %» (**33 %**); «las adaptaciones se conceden automáticamente» (**no**; solo si la discapacidad guarda relación con la prueba); «se pide un destino en la provincia de residencia» (se pide **alterar el orden de prelación**); «las plazas no cubiertas se pierden» (se **acumulan**).
""")

# =============================================================================
Q = [
 ("LGD", "Artículo 4", "Concepto", "Según el artículo 4.2 del texto refundido de la Ley General de derechos de las personas con discapacidad, tendrán la consideración de personas con discapacidad, a los efectos de esa ley, aquellas a quienes se les haya reconocido un grado de discapacidad:",
  ["Igual o superior al 33 por ciento.", "Superior al 33 por ciento.", "Igual o superior al 45 por ciento.", "Igual o superior al 65 por ciento."], "Art. 4.2 RDLeg 1/2013.", "un grado de discapacidad igual o superior al 33 por ciento"),
 ("LGD", "Artículo 4", "Concepto", "Según el artículo 4.3 del texto refundido de la Ley General de derechos de las personas con discapacidad, la acreditación del grado de discapacidad:",
  ["Tendrá validez en todo el territorio nacional.", "Solo tendrá validez en la comunidad autónoma que la expida.", "Deberá renovarse cada cinco años.", "Corresponde en todo caso al Ministerio de Sanidad."], "Art. 4.3 RDLeg 1/2013.", "tendrá validez en todo el territorio nacional"),
 ("LGD", "Artículo 2", "Concepto", "Según el artículo 2 m) del texto refundido de la Ley General de derechos de las personas con discapacidad, los ajustes razonables son las modificaciones y adaptaciones necesarias y adecuadas que:",
  ["No impongan una carga desproporcionada o indebida.", "Se apliquen con carácter general a todas las personas con discapacidad.", "Impongan cualquier carga, sea cual sea su coste.", "Sustituyan a la accesibilidad universal."], "Art. 2 m) RDLeg 1/2013.", "que no impongan una carga desproporcionada o indebida"),
 ("RD2271", "Artículo 1", "Concepto", "Según el artículo 1.3 del Real Decreto 2271/2004, el acceso de las personas con discapacidad al empleo público se inspirará en los principios de igualdad de oportunidades, no discriminación, accesibilidad universal y:",
  ["Compensación de desventajas.", "Mérito exclusivo.", "Discrecionalidad técnica.", "Preferencia absoluta."], "Art. 1.3 RD 2271/2004.", "igualdad de oportunidades, no discriminación, accesibilidad universal y compensación de desventajas"),
 ("RDL6", "a1-25", "Concepto", "Según el artículo 113.2 del Real Decreto-ley 6/2023, las personas con discapacidad podrán participar en los procesos selectivos en igualdad de condiciones que el resto, debiendo acreditar:",
  ["El grado de discapacidad, así como la compatibilidad con el desempeño de las funciones y tareas genéricas consustanciales a las mismas.", "Solo el grado de discapacidad.", "Solo la compatibilidad con las funciones del puesto.", "Un informe favorable del órgano de selección."], "Art. 113.2 RDL 6/2023.", "debiendo acreditar el grado de discapacidad, así como la compatibilidad con el desempeño de las funciones y tareas genéricas consustanciales a las mismas"),
 ("TREBEP", "Artículo 59", "Reserva", "Según el artículo 59.1 del texto refundido del Estatuto Básico del Empleado Público, en las ofertas de empleo público se reservará para personas con discapacidad un cupo no inferior al:",
  ["Siete por ciento de las vacantes.", "Cinco por ciento de las vacantes.", "Diez por ciento de las vacantes.", "Dos por ciento de las vacantes."], "Art. 59.1 TREBEP.", "un cupo no inferior al siete por ciento de las vacantes"),
 ("TREBEP", "Artículo 59", "Reserva", "Según el artículo 59.1 del texto refundido del Estatuto Básico del Empleado Público, la reserva del mínimo del siete por ciento se realizará de manera que, al menos, para personas que acrediten discapacidad intelectual se destine:",
  ["El dos por ciento de las plazas ofertadas.", "El cinco por ciento de las plazas ofertadas.", "El uno por ciento de las plazas ofertadas.", "La mitad de las plazas reservadas."], "Art. 59.1, párrafo segundo, TREBEP.", "al menos, el dos por ciento de las plazas ofertadas lo sea para ser cubiertas por personas que acrediten discapacidad intelectual"),
 ("TREBEP", "Artículo 59", "Reserva", "Según el artículo 59.1 del texto refundido del Estatuto Básico del Empleado Público, la reserva de plazas para personas con discapacidad persigue alcanzar progresivamente:",
  ["El dos por ciento de los efectivos totales en cada Administración Pública.", "El siete por ciento de los efectivos totales en cada Administración Pública.", "El cinco por ciento de los efectivos totales del sector público.", "El diez por ciento de los efectivos de la Administración General del Estado."], "Art. 59.1 TREBEP.", "de modo que progresivamente se alcance el dos por ciento de los efectivos totales en cada Administración Pública"),
 ("RDL6", "a1-20", "Reserva", "Según el artículo 108.4 del Real Decreto-ley 6/2023, en la oferta de empleo público de la Administración del Estado se reservará para personas con discapacidad un porcentaje no inferior al:",
  ["Diez por ciento de las plazas convocadas.", "Siete por ciento de las plazas convocadas.", "Cinco por ciento de las plazas convocadas.", "Treinta por ciento de las plazas convocadas."], "Art. 108.4 RDL 6/2023.", "un porcentaje no inferior al diez por ciento de las plazas convocadas"),
 ("RDL6", "a1-20", "Reserva", "Según el artículo 108.4 del Real Decreto-ley 6/2023, la reserva para personas con discapacidad se hará sobre el número total de las plazas incluidas en la oferta de empleo público:",
  ["Pudiendo concentrarse las plazas reservadas en aquellas convocatorias de cuerpos, escalas o categorías que se adapten mejor a sus capacidades y competencias.", "Debiendo distribuirse por igual entre todas las convocatorias.", "Sin que puedan concentrarse en ninguna convocatoria.", "Solo en las convocatorias de promoción interna."], "Art. 108.4, párrafo tercero, RDL 6/2023.", "pudiendo concentrarse las plazas reservadas para personas con discapacidad en aquellas convocatorias que se refieran a cuerpos, escalas o categorías que se adapten mejor a sus capacidades y competencias"),
 ("RD2271", "Artículo 2", "Reserva", "Según el artículo 2.1 del Real Decreto 2271/2004, la opción a las plazas reservadas para personas con discapacidad habrá de formularse:",
  ["En la solicitud de participación en las convocatorias.", "Tras la publicación de la lista de aprobados.", "Antes de la celebración del primer ejercicio, en escrito aparte.", "En el momento de la elección de destino."], "Art. 2.1 RD 2271/2004.", "La opción a estas plazas reservadas habrá de formularse en la solicitud de participación en las convocatorias"),
 ("RD2271", "Artículo 2", "Reserva", "Según el artículo 2.2 del Real Decreto 2271/2004, las plazas reservadas para personas con discapacidad:",
  ["Podrán incluirse dentro de las convocatorias de plazas de ingreso ordinario o convocarse en un turno independiente.", "Deberán convocarse siempre en un turno independiente.", "Solo podrán incluirse en las convocatorias de promoción interna.", "Se convocarán siempre junto con las de personal temporal."], "Art. 2.2 RD 2271/2004.", "podrán incluirse dentro de las convocatorias de plazas de ingreso ordinario o convocarse en un turno independiente"),
 ("RD2271", "Artículo 3", "Reserva", "Según el artículo 3.2 del Real Decreto 2271/2004, si un aspirante del cupo de reserva supera los ejercicios pero no obtiene plaza, y su puntuación es superior a la de otros aspirantes del sistema de acceso general:",
  ["Será incluido por su orden de puntuación en el sistema de acceso general.", "Quedará excluido del proceso selectivo.", "Pasará a una bolsa de interinos.", "Obtendrá plaza en la siguiente convocatoria sin examen."], "Art. 3.2 RD 2271/2004.", "será incluido por su orden de puntuación en el sistema de acceso general"),
 ("RD2271", "Artículo 3", "Reserva", "Según el artículo 3.3 del Real Decreto 2271/2004, las pruebas selectivas para quienes opten por el turno de reserva para personas con discapacidad:",
  ["Tendrán idéntico contenido para todos los aspirantes, sin perjuicio de las adaptaciones previstas.", "Tendrán un contenido reducido.", "Consistirán únicamente en la valoración de méritos.", "Serán de menor dificultad que las del turno general."], "Art. 3.3 RD 2271/2004.", "Las pruebas selectivas tendrán idéntico contenido para todos los aspirantes"),
 ("RD2271", "Artículo 5", "Reserva", "Según el artículo 5.2 del Real Decreto 2271/2004, en las convocatorias por promoción interna, las plazas reservadas para personas con discapacidad que queden desiertas:",
  ["Se acumularán a las del turno ordinario de promoción interna.", "Se acumularán a las de acceso libre.", "Se acumularán a la oferta siguiente.", "Se amortizarán."], "Art. 5.2 RD 2271/2004.", "Las plazas reservadas que queden desiertas se acumularán a las del turno ordinario de promoción interna"),
 ("RD2271", "Artículo 6", "Reserva", "Según el artículo 6.1 del Real Decreto 2271/2004, en las convocatorias de personal temporal que incluyan fase de oposición se reservará cupo para personas con discapacidad cuando se convoquen en un mismo ámbito de participación:",
  ["20 plazas o más.", "10 plazas o más.", "50 plazas o más.", "Cualquier número de plazas."], "Art. 6.1 RD 2271/2004.", "en las que se convoquen 20 plazas o más en un mismo ámbito de participación"),
 ("TREBEP", "Artículo 59", "Adaptaciones", "Según el artículo 59.2 del texto refundido del Estatuto Básico del Empleado Público, ¿quién adoptará las medidas precisas para establecer las adaptaciones y ajustes razonables de tiempos y medios en el proceso selectivo?",
  ["Cada Administración Pública.", "El Ministerio competente en materia de discapacidad, para todas las Administraciones.", "El Consejo Nacional de la Discapacidad.", "Las organizaciones representativas de las personas con discapacidad."], "Art. 59.2 TREBEP.", "Cada Administración Pública adoptará las medidas precisas"),
 ("RDL6", "a1-25", "Adaptaciones", "Según el artículo 113.4 del Real Decreto-ley 6/2023, durante la realización de los procesos selectivos se permitirá a quienes las precisen y lo acrediten el uso de:",
  ["Prótesis, incluidas las auditivas.", "Teléfonos móviles.", "Textos legales anotados.", "Calculadoras programables, en todo caso."], "Art. 113.4 RDL 6/2023.", "permitiéndose el uso de prótesis, incluidas las auditivas"),
 ("RDL6", "a1-27", "Adaptaciones", "Según el artículo 115.2 del Real Decreto-ley 6/2023, respecto de la participación de personas con discapacidad en los órganos de selección:",
  ["Se promoverá, en particular en aquellos procesos en los que exista turno de reserva para este colectivo.", "Será obligatoria en todos los órganos de selección.", "Está prohibida para garantizar la imparcialidad.", "Solo se admite en procesos de personal laboral."], "Art. 115.2 RDL 6/2023.", "Se promoverá, igualmente, la participación en los mismos de personas con discapacidad, en particular en aquellos procesos en los que exista turno de reserva para este colectivo"),
 ("RD2271", "Artículo 8", "Adaptaciones", "Según el artículo 8.3 del Real Decreto 2271/2004, la adaptación de tiempos consiste en:",
  ["La concesión de un tiempo adicional para la realización de los ejercicios.", "La celebración de los ejercicios en fechas distintas.", "La exención de alguno de los ejercicios.", "La reducción del número de preguntas."], "Art. 8.3 RD 2271/2004.", "La adaptación de tiempos consiste en la concesión de un tiempo adicional para la realización de los ejercicios"),
 ("RD2271", "Artículo 8", "Adaptaciones", "Según el artículo 8.5 del Real Decreto 2271/2004, la adaptación de tiempos y medios:",
  ["No se otorgará de forma automática, sino únicamente en aquellos casos en que la discapacidad guarde relación directa con la prueba a realizar.", "Se otorgará de forma automática a todo aspirante con discapacidad.", "Se otorgará solo a quienes tengan un grado de discapacidad superior al 65 por ciento.", "Se otorgará solo en la fase de concurso."], "Art. 8.5 RD 2271/2004.", "La adaptación no se otorgará de forma automática, sino únicamente en aquellos casos en que la discapacidad guarde relación directa con la prueba a realizar"),
 ("RD2271", "Artículo 8", "Adaptaciones", "Según el artículo 8.1 del Real Decreto 2271/2004, las adaptaciones y ajustes razonables de tiempo y medios se establecerán en las pruebas selectivas:",
  ["Incluyendo los cursos de formación o períodos de prácticas.", "Excluyendo los cursos de formación y los períodos de prácticas.", "Solo en los ejercicios orales.", "Solo en la fase de oposición."], "Art. 8.1 RD 2271/2004.", "incluyendo los cursos de formación o períodos de prácticas"),
 ("OPJC804", "a4", "Adaptaciones", "Según el artículo 4.2 de la Orden PJC/804/2025, las personas aspirantes que, sin contar con un reconocimiento oficial del grado de discapacidad, acrediten formalmente su situación de necesidad de apoyo, podrán solicitar:",
  ["Solo las adaptaciones de medios y otros ajustes razonables.", "Todas las adaptaciones, incluidas las de tiempos.", "Solo las adaptaciones de tiempos.", "Ninguna adaptación."], "Art. 4.2 Orden PJC/804/2025.", "podrán solicitar en estos casos solo las adaptaciones de medios y otros ajustes razonables"),
 ("OPJC804", "a6", "Adaptaciones", "Según el artículo 6 de la Orden PJC/804/2025, cuando la persona con discapacidad no cuente con un informe oficial que acredite la necesidad de uso del recurso y apoyo, el órgano de selección podrá solicitar esta acreditación en un plazo:",
  ["No inferior a diez días hábiles.", "No superior a cinco días hábiles.", "De un mes.", "De quince días naturales."], "Art. 6 Orden PJC/804/2025.", "en un plazo no inferior a diez días hábiles"),
 ("OPJC804", "a7", "Adaptaciones", "Según el artículo 7.2 de la Orden PJC/804/2025, para que el órgano de selección valore la procedencia de lo solicitado, la persona candidata deberá adjuntar:",
  ["El Dictamen Técnico Facultativo emitido por el órgano técnico de calificación del grado de discapacidad competente.", "Un certificado médico de su médico de cabecera.", "Una declaración responsable sin documentación adicional.", "Un informe de la unidad de inclusión del ministerio convocante."], "Art. 7.2 Orden PJC/804/2025.", "la persona candidata deberá adjuntar el Dictamen Técnico Facultativo emitido por el órgano técnico de calificación del grado de discapacidad competente"),
 ("OPJC804", "a8", "Adaptaciones", "Según el artículo 8.2 de la Orden PJC/804/2025, ¿a quién corresponde resolver sobre la procedencia y concreción de la adaptación?",
  ["A los órganos de selección.", "Al órgano convocante.", "A la Secretaría de Estado de Función Pública.", "Al IMSERSO."], "Art. 8.2 Orden PJC/804/2025.", "Corresponde a los órganos de selección resolver sobre la procedencia y concreción de la adaptación"),
 ("OPJC804", "a8", "Adaptaciones", "Según el artículo 8.6 de la Orden PJC/804/2025, los órganos técnicos deberán remitir los dictámenes o informes solicitados por los órganos de selección en el plazo de:",
  ["Diez días hábiles desde la recepción de la solicitud.", "Cinco días hábiles desde la recepción de la solicitud.", "Un mes desde la recepción de la solicitud.", "Quince días naturales desde la recepción de la solicitud."], "Art. 8.6 Orden PJC/804/2025.", "en el plazo de diez días hábiles desde la recepción de la solicitud"),
 ("RD2271", "Artículo 10", "Provisión", "Según el artículo 10.2 del Real Decreto 2271/2004, la valoración, la realización y la financiación de las adaptaciones del puesto de trabajo corresponden:",
  ["Al ministerio u organismo al que esté adscrito el puesto de trabajo.", "Al empleado con discapacidad.", "Al Ministerio de Trabajo, en todo caso.", "A la comunidad autónoma de residencia del empleado."], "Art. 10.2 RD 2271/2004.", "El ministerio u organismo al que esté adscrito el puesto de trabajo será el encargado de la valoración, la realización y la financiación de las adaptaciones"),
 ("RD2271", "Artículo 11", "Provisión", "Según el artículo 11.2 del Real Decreto 2271/2004, la Administración solo podrá denegar la adaptación solicitada para participar en cursos de formación:",
  ["Cuando suponga una carga desproporcionada.", "Cuando el curso sea presencial.", "Cuando el grado de discapacidad sea inferior al 65 por ciento.", "En ningún caso."], "Art. 11.2 RD 2271/2004.", "que sólo podrá denegar cuando suponga una carga desproporcionada"),
 ("RD2271", "Artículo 13", "Provisión", "Según el artículo 13.2 del Real Decreto 2271/2004, el informe balance anual sobre el acceso de personas con discapacidad al empleo público se elevará, para su conocimiento:",
  ["A la Comisión Superior de Personal y al Consejo Nacional de la Discapacidad.", "A las Cortes Generales.", "Al Consejo de Ministros y al Defensor del Pueblo.", "Al Consejo de Estado."], "Art. 13.2 RD 2271/2004.", "se elevará, para su conocimiento, a la Comisión Superior de Personal y al Consejo Nacional de la Discapacidad"),
 ("RDL6", "da-15", "Provisión", "Según la disposición adicional decimoquinta del Real Decreto-ley 6/2023, las unidades de inclusión del personal con discapacidad quedarán adscritas:",
  ["A la Subsecretaría de cada departamento ministerial, a través de alguno de sus órganos directivos dependientes.", "A la Secretaría de Estado de Función Pública.", "Al Gabinete del Ministro.", "A la Dirección General de la Función Pública, para todos los ministerios."], "Disposición adicional decimoquinta.2 RDL 6/2023.", "quedarán adscritas a la Subsecretaría a través de alguno de sus órganos directivos dependientes"),
]
for k, art, cat, enun, ops, expl, frag in Q: T.q(k, art, cat, enun, ops, expl, frag)
for cod, n, *_ in EX: T.real(cod, n, "Preguntas oficiales")

for q_, a_, cat in [
  ("Persona con discapacidad a efectos legales (RDLeg 1/2013, art. 4.2)", "Grado reconocido igual o superior al 33 %; equiparados: pensionistas de incapacidad permanente total, absoluta o gran invalidez y de clases pasivas por incapacidad.", "Concepto"),
  ("Ajuste razonable (art. 2 m)", "Adaptación necesaria y adecuada a un caso particular que no imponga una carga desproporcionada o indebida.", "Concepto"),
  ("Qué se acredita para acceder (RDL 6/2023, art. 113.2)", "El grado de discapacidad y la compatibilidad con las funciones y tareas.", "Concepto"),
  ("Reserva del TREBEP (art. 59.1)", "No inferior al 7 % de las vacantes; al menos el 2 % de las plazas para discapacidad intelectual; objetivo: 2 % de los efectivos.", "Reserva"),
  ("Reserva en la Administración del Estado (RDL 6/2023, art. 108.4)", "No inferior al 10 % de las plazas convocadas; al menos el 2 % para discapacidad intelectual; puede concentrarse.", "Reserva"),
  ("Discapacidad intelectual (RDL 6/2023, art. 113.3)", "Con grado igual o superior al 33 %: pruebas selectivas específicas e independientes.", "Reserva"),
  ("Acumulación de plazas no cubiertas (RD 2271/2004, art. 3.2)", "Si no se cubre el 3 % de las convocadas, las no cubiertas se acumulan al cupo del 5 % de la oferta siguiente, con un límite del 10 %.", "Reserva"),
  ("Plazas desiertas en promoción interna y en personal temporal (arts. 5 y 6)", "Promoción interna: al turno ordinario de promoción interna. Temporal (20 o más plazas): a las libres.", "Reserva"),
  ("Adaptación de tiempos (RD 2271/2004, art. 8.3)", "Tiempo adicional para los ejercicios.", "Adaptaciones"),
  ("¿Son automáticas las adaptaciones? (art. 8.5)", "No: solo si la discapacidad guarda relación directa con la prueba.", "Adaptaciones"),
  ("Medios humanos (Orden PJC/804/2025, art. 5)", "Asistente personal; personal de accesibilidad para personas sordas, con discapacidad auditiva y sordociegas; otro personal de apoyo.", "Adaptaciones"),
  ("Sin grado reconocido (Orden, art. 4.2)", "Solo adaptaciones de medios y otros ajustes razonables (no de tiempos).", "Adaptaciones"),
  ("Quién resuelve las adaptaciones (Orden, art. 8.2)", "Los órganos de selección.", "Adaptaciones"),
  ("Elección de destino del cupo (RD 2271/2004, art. 9)", "Alteración del orden de prelación por dependencia personal, dificultades de desplazamiento u otras análogas, acreditadas.", "Provisión"),
  ("Adaptación del puesto (art. 10)", "Se pide con informe; la valora, realiza y financia el ministerio u organismo del puesto.", "Provisión"),
  ("Unidades de inclusión (RDL 6/2023, disposición adicional decimoquinta)", "Una en cada ministerio, adscrita a la Subsecretaría.", "Provisión"),
]: T.fc(q_, a_, cat)

T.glos("Persona con discapacidad", "A efectos legales, la que tiene reconocido un grado de discapacidad igual o superior al 33 % (RDLeg 1/2013, art. 4.2).", "s1", "Concepto")
T.glos("Ajuste razonable", "Modificación o adaptación necesaria y adecuada a un caso particular que no impone una carga desproporcionada o indebida (RDLeg 1/2013, art. 2 m).", "s1", "Concepto")
T.glos("Cupo de reserva", "Porcentaje mínimo de plazas de la oferta de empleo público para personas con discapacidad: 7 % (TREBEP, art. 59.1) y 10 % en la Administración del Estado (RDL 6/2023, art. 108.4).", "s3", "Reserva")
T.glos("Turno independiente", "Convocatoria con plazas reservadas solo a personas con discapacidad, no supeditada a la ordinaria (RD 2271/2004, arts. 2.2 y 4).", "s5", "Reserva")
T.glos("Adaptación de tiempos", "Concesión de tiempo adicional para realizar los ejercicios (RD 2271/2004, art. 8.3).", "s7", "Adaptaciones")
T.glos("Adaptación de medios", "Puesta a disposición de medios materiales y humanos, apoyos, ayudas técnicas y accesibilidad (RD 2271/2004, art. 8.4).", "s7", "Adaptaciones")
T.glos("Dictamen Técnico Facultativo", "Documento del órgano técnico de calificación del grado de discapacidad que se adjunta a la petición de adaptaciones (Orden PJC/804/2025, art. 7.2).", "s8", "Adaptaciones")
T.glos("Alteración del orden de prelación", "Facultad de quien ingresa por el cupo de pedir que se altere el orden para elegir plaza, por motivos acreditados (RD 2271/2004, art. 9).", "s9", "Provisión")
T.glos("Unidad de inclusión del personal con discapacidad", "Unidad de cada ministerio, adscrita a la Subsecretaría, para la inclusión y la adaptación de puestos (RDL 6/2023, disposición adicional decimoquinta).", "s10", "Provisión")

T.hito("2004", "Real Decreto 2271/2004, de 3 de diciembre (BOE de 17-12-2004)", "Acceso al empleo público y provisión de puestos de las personas con discapacidad", "normativo", "s2")
T.hito("2013", "Real Decreto Legislativo 1/2013, de 29 de noviembre (BOE de 3-12-2013)", "Ley General de derechos de las personas con discapacidad: concepto (art. 4) y ajustes razonables (art. 2 m)", "normativo", "s1")
T.hito("2023", "Real Decreto-ley 6/2023, de 19 de diciembre (BOE de 20-12-2023)", "Reserva del 10 % en la Administración del Estado (art. 108.4) y unidades de inclusión", "normativo", "s4")
T.hito("2025", "Orden PJC/804/2025, de 23 de julio (BOE de 25-7-2025)", "Criterios generales de adaptación de medios y tiempos y otros ajustes razonables", "normativo", "s8")

T.publicar()
