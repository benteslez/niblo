# -*- coding: utf-8 -*-
"""Tema V.7 (B5T07): El personal laboral al servicio de las Administraciones públicas: su
régimen jurídico. El IV Convenio Único para el personal laboral al servicio de la
Administración General del Estado: ámbito de aplicación y sistema de clasificación.
Método del I.2. Normas (textos consolidados del BOE): TREBEP (RDLeg 5/2015), arts. 1, 2, 7,
8, 9, 11, 19, 27, 51, 77, 83, 92 y 93, disposición derogatoria única y disposición final
cuarta; Estatuto de los Trabajadores (RDLeg 2/2015), arts. 1, 3 y 22; Ley 30/1984, art. 15;
RDL 6/2023, art. 109; IV Convenio Único (Resolución de 13 de mayo de 2019), arts. 1 a 4,
7 a 12, 15, 16, 19 y 124, disposiciones adicionales primera y duodécima, disposición
transitoria primera y anexo II."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO.update({"CONV": "IV Convenio Único", "ET": "Estatuto de los Trabajadores", "L30": "Ley 30/1984", "RDL6": "RDL 6/2023"})

T = Tema("B5T07",
  "Cuatro preguntas: I. Quién es personal laboral y qué normas lo rigen (TREBEP, arts. 1, 2, 7, 8 y 11; Estatuto de los Trabajadores, arts. 1 y 3) · II. Qué puestos ocupa y qué preceptos del TREBEP le alcanzan (TREBEP, arts. 9.2, 11, 19, 27, 51, 77, 83, 92 y 93; Ley 30/1984, art. 15; RDL 6/2023, art. 109) · III. A quién se aplica el IV Convenio Único (arts. 1 a 4 y 124) · IV. Cómo clasifica al personal (Estatuto de los Trabajadores, art. 22; Convenio, arts. 7 a 19 y anexo II). Cada artículo: texto literal del BOE y ficha.",
  ["Personal laboral", "TREBEP art. 7", "TREBEP art. 11", "Fijo, indefinido o temporal", "Art. 9.2 TREBEP", "Ley 30/1984 art. 15", "Relación de puestos de trabajo", "IV Convenio Único", "Ámbito de aplicación", "Personal excluido", "Grupos profesionales", "M3 a E0", "Familias profesionales", "Especialidades", "Comisión Paritaria", "Comisión Negociadora"])

# =============================================================================
T.ap("s0", "Mapa del tema: cuatro preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque V, tema 7):
> El personal laboral al servicio de las Administraciones públicas: su régimen jurídico. El IV Convenio Único para el personal laboral al servicio de la Administración General del Estado: ámbito de aplicación y sistema de clasificación.

### El hilo conductor

El epígrafe se lee como **cuatro preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Normas |
|---|---|---|
| **I** | ¿Quién es personal laboral y qué normas lo rigen? | TREBEP, arts. 1.2, 2.1, 7, 8.2 c) y 11.1; Estatuto de los Trabajadores, arts. 1 y 3.1 |
| **II** | ¿Qué puestos ocupa y qué preceptos del TREBEP le alcanzan? | TREBEP, arts. 9.2, 11.2 y 3, 19, 27, 51, 77, 83, 92 y 93; Ley 30/1984, art. 15.1; RDL 6/2023, art. 109.1 |
| **III** | ¿A quién se aplica el IV Convenio Único? (ámbito de aplicación) | IV Convenio Único, arts. 1, 2, 3, 4 y 124; disposición adicional duodécima |
| **IV** | ¿Cómo se clasifica al personal? (sistema de clasificación) | Estatuto de los Trabajadores, art. 22; IV Convenio Único, arts. 7 a 11, 12, 15, 16 y 19; disposición adicional primera, disposición transitoria primera y anexo II |

!> **La idea que une los cuatro bloques:** el personal laboral presta servicios a la Administración por un **contrato de trabajo**, no por nombramiento. Por eso se rige por la **legislación laboral** y los **convenios colectivos**, y solo por los preceptos del **TREBEP** que así lo digan (I). Ocupa los puestos que no implican **potestades públicas**; en la AGE, solo los exceptuados por la Ley 30/1984 (II). En la AGE su convenio es el **IV Convenio Único**, que fija a quién se aplica (III) y lo ordena en **grupos, familias y especialidades** (IV).

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen; o, si es un derecho, Titulares · Contenido · Límites · Protección · ⚠ Ojo en el examen).
- Los esquemas y cuadros **no son texto legal**: resumen los artículos citados.
- Fronteras con otros temas: la selección se estudia en el tema V.3, la provisión en el V.4, las retribuciones en el V.6, la negociación colectiva y la representación en el V.8, y el régimen disciplinario en el V.2. Aquí solo se ve **qué norma** rige al personal laboral en cada materia.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Quién es personal laboral y qué normas lo rigen? (TREBEP, arts. 1, 2, 7, 8 y 11; ET, arts. 1 y 3)", donde(
  "Primera pregunta del tema. Antes de entrar en el convenio, hay que saber **qué es** el personal laboral de las Administraciones y **qué normas** se le aplican: la legislación laboral, los convenios y solo algunos preceptos del TREBEP.",
  ["1 Concepto y clases de personal laboral (TREBEP, arts. 8.2 c y 11.1; ET, art. 1)", "2 Régimen jurídico: qué normas le rigen (TREBEP, arts. 1.2, 2.1 y 7; ET, art. 3.1)"]))

T.ap("s1", "I.1 Concepto y clases de personal laboral (TREBEP, arts. 8.2 c y 11.1; ET, art. 1)", f"""
El personal laboral es una de las **cuatro clases** de empleados públicos. Lo que lo distingue es el **contrato de trabajo**.

{unidad("1.1 Una clase de empleado público (TREBEP, art. 8)",
  lit("TREBEP", "Artículo 8", ["Personal laboral, ya sea fijo, por tiempo indefinido o temporal"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("El personal laboral como clase de empleado público",
         f"Quienes {c('TREBEP', 'Artículo 8', 'desempeñan funciones retribuidas en las Administraciones Públicas al servicio de los intereses generales')}",
         ["::Cuatro clases (8.2):", "Funcionarios de carrera", "Funcionarios interinos", "**Personal laboral**: fijo, por tiempo indefinido o temporal", "Personal eventual"],
         "—",
         "El personal laboral es **empleado público** igual que el funcionario. Sus tres modalidades son **fijo, por tiempo indefinido o temporal** (no «interino», que es de funcionarios). El concepto y las clases en general, en el tema V.1."))}

{unidad("1.2 Concepto de personal laboral (TREBEP, art. 11.1)",
  lit("TREBEP", "Artículo 11", ["contrato de trabajo formalizado por escrito", "modalidades de contratación de personal previstas en la legislación laboral", "fijo, por tiempo indefinido o temporal"], solo=[1]),
  fichab("Empleado público vinculado por contrato de trabajo",
         f"Quien {c('TREBEP', 'Artículo 11', 'presta servicios retribuidos por las Administraciones Públicas')}",
         ["Vínculo: **contrato de trabajo formalizado por escrito**", "Modalidades: las de la **legislación laboral**", "Según la duración del contrato: fijo, por tiempo indefinido o temporal"],
         "—",
         "Tres notas: **contrato** (no nombramiento, que es el del funcionario: art. 9.1), **por escrito** y en una modalidad de la **legislación laboral**. La duración del contrato da la clase."))}

{unidad("1.3 Trabajador por cuenta ajena; los funcionarios, excluidos (ET, art. 1.1 y 1.3 a)",
  lit("ET", "Artículo 1", ["voluntariamente presten sus servicios retribuidos por cuenta ajena y dentro del ámbito de organización y dirección de otra persona", "La relación de servicio de los funcionarios públicos"], solo=[1, 3, 4]),
  fichab("Ámbito del Estatuto de los Trabajadores",
         "Trabajadores por cuenta ajena; la Administración actúa como **empleador**",
         ["Incluye a quien presta servicios **voluntarios, retribuidos, por cuenta ajena** y bajo la dirección de otro (1.1)", "Excluye la relación de servicio de los **funcionarios públicos** y la del personal de las Administraciones regulada por normas **administrativas o estatutarias** al amparo de una ley (1.3 a)"],
         "—",
         "El personal laboral de las Administraciones **sí** entra en el Estatuto de los Trabajadores; el funcionario **no**. La exclusión alcanza a quien se rija por normas administrativas o estatutarias **al amparo de una ley**."))}
""", 2)

T.ap("s2", "I.2 Régimen jurídico: qué normas le rigen (TREBEP, arts. 1.2, 2.1 y 7; ET, art. 3.1)", f"""
{unidad("2.1 El TREBEP también se ocupa del personal laboral (arts. 1.2 y 2.1)",
  lit("TREBEP", "Artículo 1", ["determinar las normas aplicables al personal laboral"], solo=[2]),
  lit("TREBEP", "Artículo 2", ["en lo que proceda al personal laboral"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Objeto y ámbito del TREBEP respecto del personal laboral",
         "Personal laboral de la AGE, de las comunidades autónomas y de Ceuta y Melilla, de las entidades locales, de los organismos y entidades de derecho público y de las Universidades Públicas",
         ["Respecto de los funcionarios, el TREBEP establece las **bases** de su régimen estatutario (1.1)", "Respecto del personal laboral, **determina las normas aplicables** (1.2)"],
         "—",
         f"Se aplica al funcionario y {c('TREBEP', 'Artículo 2', 'en lo que proceda al personal laboral')}: no se le aplica entero (→ I.2.2)."))}

{unidad("2.2 La regla: legislación laboral, convenios y los preceptos del TREBEP que así lo dispongan (art. 7)",
  lit("TREBEP", "Artículo 7", ["además de por la legislación laboral y por las demás normas convencionalmente aplicables, por los preceptos de este Estatuto que así lo dispongan", "se regirá por lo previsto en el presente Estatuto"]),
  fichab("Normativa aplicable al personal laboral de las Administraciones",
         "Personal laboral al servicio de las Administraciones públicas",
         ["::Tres fuentes (párrafo 1.º):", "La **legislación laboral**", "Las demás **normas convencionalmente aplicables** (convenios colectivos)", "Los **preceptos del TREBEP que así lo dispongan** (→ II.2)", "::Excepción (párrafo 2.º): en permisos de nacimiento, adopción, del progenitor diferente de la madre biológica, de lactancia y parental rige el **TREBEP**, no las suspensiones del contrato del Estatuto de los Trabajadores"],
         "—",
         "Cayó en 2025 (→ Cierre 1). No se rige **solo** por la legislación laboral y los convenios, ni el TREBEP se le aplica **íntegramente**: solo los preceptos **que así lo dispongan**. Y en los **permisos por nacimiento, adopción, lactancia y parental**, el TREBEP desplaza al Estatuto de los Trabajadores."))}

{unidad("2.3 Fuentes de la relación laboral (ET, art. 3.1)",
  lit("ET", "Artículo 3", ["Por las disposiciones legales y reglamentarias del Estado", "Por los convenios colectivos", "Por la voluntad de las partes, manifestada en el contrato de trabajo", "Por los usos y costumbres locales y profesionales"], solo=[1, 2, 3, 4, 5]),
  fichab("Las fuentes de la relación laboral, también para el personal laboral público",
         "—",
         ["Disposiciones legales y reglamentarias del Estado", "Convenios colectivos", "Voluntad de las partes en el contrato, sin condiciones menos favorables o contrarias a las leyes y convenios", "Usos y costumbres locales y profesionales"],
         "—",
         "El contrato **no** puede fijar condiciones **menos favorables** que la ley o el convenio. Para el personal laboral de la AGE, el convenio es el **IV Convenio Único** (→ III.1)."))}

{resumen([
  "Personal laboral: presta servicios retribuidos a las Administraciones por **contrato de trabajo formalizado por escrito**; puede ser **fijo, por tiempo indefinido o temporal** (TREBEP, arts. 8.2 c y 11.1).",
  "El Estatuto de los Trabajadores le alcanza; excluye a los **funcionarios** (ET, art. 1.3 a).",
  "Régimen (TREBEP, art. 7): **legislación laboral + convenios + preceptos del TREBEP que así lo dispongan**; en los permisos de nacimiento, adopción, lactancia y parental, el **TREBEP**."],
  "Siguiente: II. ¿Qué puestos ocupa y qué preceptos del TREBEP le alcanzan?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Qué puestos ocupa y qué preceptos del TREBEP le alcanzan?", donde(
  "Segunda pregunta. El art. 7 dice que al personal laboral se le aplican los preceptos del TREBEP «que así lo dispongan». Hay que saber **qué puestos** puede ocupar (y cuáles no) y **cuáles son esos preceptos**.",
  ["1 Qué puestos puede desempeñar (TREBEP, arts. 9.2 y 11.2; Ley 30/1984, art. 15.1; RDL 6/2023, art. 109.1)", "2 Los preceptos del TREBEP que se refieren al personal laboral (arts. 11.3, 19, 27, 51, 77, 83, 92 y 93)"]))

T.ap("s3", "II.1 Qué puestos puede desempeñar el personal laboral (TREBEP, arts. 9.2 y 11.2; Ley 30/1984, art. 15.1; RDL 6/2023, art. 109.1)", f"""
{unidad("1.1 Lo que nunca puede hacer: las funciones reservadas a funcionarios (TREBEP, art. 9.2)",
  lit("TREBEP", "Artículo 9", ["participación directa o indirecta en el ejercicio de las potestades públicas o en la salvaguardia de los intereses generales", "corresponden exclusivamente a los funcionarios públicos"], solo=[2]),
  fichab("Reserva de funciones a los funcionarios públicos",
         "Solo los **funcionarios públicos**",
         ["Funciones que impliquen participación directa o indirecta en el ejercicio de **potestades públicas**", "Funciones de **salvaguardia de los intereses generales** del Estado y de las Administraciones"],
         "—",
         f"La reserva es **exclusiva** y se aplica {c('TREBEP', 'Artículo 9', 'En todo caso')}. Es el límite que el art. 11.2 obliga a respetar (→ II.1.2)."))}

{unidad("1.2 Quién fija los puestos laborales (TREBEP, art. 11.2)",
  lit("TREBEP", "Artículo 11", ["Las leyes de Función Pública que se dicten en desarrollo de este Estatuto", "respetando en todo caso lo establecido en el artículo 9.2"], solo=[2]),
  fichab("Criterios para determinar los puestos que puede desempeñar el personal laboral",
         "Las **leyes de Función Pública** de desarrollo del TREBEP",
         "Establecen los **criterios** para determinar qué puestos pueden ser desempeñados por personal laboral",
         "—",
         "No lo deciden los convenios ni el Estatuto de los Trabajadores, sino las **leyes de Función Pública**, y siempre con el límite del **art. 9.2**."))}

{unidad("1.3 En la AGE: la regla general y las excepciones (Ley 30/1984, art. 15.1 c)",
  lit("L30", "Artículo quince", ["serán desempeñados por funcionarios públicos", "podrán desempeñarse por personal laboral", "vigilancia, custodia, porteo y otros análogos", "cuando no existan Cuerpos o Escalas de funcionarios", "en el extranjero", "funciones auxiliares de carácter instrumental y apoyo administrativo"], solo=[4, 5, 6, 7, 8, 9, 10, 11, 12]),
  fichab("Puestos de la Administración del Estado que pueden desempeñarse por personal laboral",
         "Administración del Estado y sus Organismos Autónomos; Entidades Gestoras y Servicios Comunes de la Seguridad Social",
         ["::Regla: los puestos son de **funcionarios públicos**. Excepciones (pueden ser laborales):", "No permanentes y de necesidades periódicas y discontinuas", "Oficios; vigilancia, custodia, porteo y análogos", "Instrumentales (mantenimiento y conservación, artes gráficas, encuestas, protección civil, comunicación social), expresión artística, servicios sociales y protección de menores", "Conocimientos técnicos especializados sin Cuerpo o Escala de funcionarios con esa preparación", "En el extranjero, de trámite y colaboración y auxiliares", "Funciones auxiliares de carácter instrumental y apoyo administrativo", "::Además, los Organismos Públicos de Investigación pueden contratar personal laboral según la Ley 13/1986"],
         "—",
         f"El art. 15 sigue vigente: no figura entre los preceptos de la Ley 30/1984 que deroga el TREBEP ({c('TREBEP', 'ddunica-2', '14.4 y 5; 16; 17')}…), y la disposición final cuarta.2 del TREBEP mantiene {c('TREBEP', 'dfcuaa', 'las normas vigentes sobre ordenación, planificación y gestión de recursos humanos en tanto no se opongan a lo establecido en este Estatuto')}. La regla es el **funcionario**; el laboral es la **excepción**."))}

{unidad("1.4 Los puestos laborales figuran en la relación de puestos de trabajo (Ley 30/1984, art. 15.1 a, b y f; RDL 6/2023, art. 109.1)",
  lit("L30", "Artículo quince", ["aquellos otros que puedan desempeñarse por personal laboral", "la categoría profesional y régimen jurídico aplicable cuando sean desempeñados por personal laboral", "la formalización de nuevos contratos de personal laboral fijo"], solo=[2, 3, 15, 16]),
  lit("RDL6", "Artículo 109", ["todos los puestos de trabajo de naturaleza funcionarial, laboral y eventual existentes"], solo=[1, 2]),
  fichab("La relación de puestos de trabajo (RPT) y el personal laboral",
         "La Administración del Estado",
         ["La RPT comprende también los puestos que pueden desempeñarse por personal laboral (Ley 30/1984, 15.1 a; RDL 6/2023, 109.1)", "Para los puestos laborales indica la **categoría profesional** y el **régimen jurídico** aplicable (15.1 b)", "Los nuevos contratos de **personal laboral fijo** exigen que el puesto figure en la RPT (15.1 f)"],
         "—",
         "La exigencia de figurar en la RPT **no** rige para tareas **no permanentes** con contratos de **duración determinada** con cargo a créditos de personal laboral eventual o al capítulo de inversiones (15.1 f, párrafo 2.º)."))}
""", 2)

T.ap("s4", "II.2 Los preceptos del TREBEP que se refieren al personal laboral (arts. 11.3, 19, 27, 51, 77, 83, 92 y 93)", f"""
Son los preceptos «que así lo dispongan» del art. 7 (→ I.2.2). En cada materia dicen **qué norma** manda: el propio TREBEP, la legislación laboral o el convenio. El desarrollo de cada materia está en su tema.

{unidad("2.1 Selección: pública, con igualdad, mérito y capacidad (art. 11.3)",
  lit("TREBEP", "Artículo 11", ["serán públicos", "igualdad, mérito y capacidad", "principio de celeridad"], solo=[3]),
  fichab("Procedimientos de selección del personal laboral",
         "La Administración que contrata",
         ["Procedimientos **públicos**", "Principios de **igualdad, mérito y capacidad**, en todo caso", "Temporal: además, **celeridad**, para atender razones justificadas de **necesidad y urgencia**"],
         "—",
         f"La **celeridad** es solo para el personal laboral **temporal**. Los sistemas selectivos del personal laboral fijo ({c('TREBEP', 'Artículo 61', 'oposición, concurso-oposición')}… {c('TREBEP', 'Artículo 61', 'o concurso de valoración de méritos')}: art. 61.7) se estudian en el tema V.3."))}

{unidad("2.2 Carrera y promoción (art. 19)",
  lit("TREBEP", "Artículo 19", ["tendrá derecho a la promoción profesional", "a través de los procedimientos previstos en el Estatuto de los Trabajadores o en los convenios colectivos"]),
  ficha("El personal laboral",
         "Derecho a la **promoción profesional** (19.1)",
         "Se hace efectiva por los procedimientos del **Estatuto de los Trabajadores** o de los **convenios colectivos** (19.2)",
         "—",
         "Cayó en 2025 (→ Cierre 1): el personal laboral **sí** tiene derecho a la promoción, pero por los procedimientos del **Estatuto de los Trabajadores o de los convenios**, no por los del TREBEP. La carrera de los funcionarios, en el tema V.4."))}

{unidad("2.3 Retribuciones (art. 27)",
  lit("TREBEP", "Artículo 27", ["la legislación laboral, el convenio colectivo que sea aplicable y el contrato de trabajo", "respetando en todo caso lo establecido en el artículo 21"]),
  fichab("Determinación de las retribuciones del personal laboral",
         "—",
         "Según la **legislación laboral**, el **convenio colectivo** aplicable y el **contrato de trabajo**",
         f"Límite: el art. 21 (incremento de la masa salarial, que debe reflejarse {c('TREBEP', 'Artículo 21', 'para cada ejercicio presupuestario en la correspondiente ley de presupuestos')})",
         "Tres fuentes (ley laboral, convenio, contrato) y un límite: el **art. 21** (leyes de presupuestos). Las retribuciones, en el tema V.6."))}

{unidad("2.4 Jornada, permisos y vacaciones (art. 51)",
  lit("TREBEP", "Artículo 51", ["se estará a lo establecido en este capítulo y en la legislación laboral correspondiente"]),
  fichab("Norma aplicable a la jornada, permisos y vacaciones del personal laboral",
         "—", "El **capítulo V del título III del TREBEP** (jornada, permisos y vacaciones) **y** la legislación laboral", "—",
         "Aquí el TREBEP **sí** se aplica (junto con la legislación laboral); recuerda además la regla especial de los permisos del art. 7 (→ I.2.2). Jornada y permisos, en el tema V.2."))}

{unidad("2.5 Clasificación (art. 77)",
  lit("TREBEP", "Artículo 77", ["de conformidad con la legislación laboral"]),
  fichab("Clasificación del personal laboral",
         "—", "Conforme a la **legislación laboral**: grupos profesionales del art. 22 del Estatuto de los Trabajadores (→ IV.1)", "—",
         "El personal laboral **no** se clasifica en los subgrupos A1, A2, C1… del funcionario: se clasifica **conforme a la legislación laboral** y, en la AGE, en los grupos **M3 a E0** del Convenio (→ IV.2)."))}

{unidad("2.6 Provisión de puestos y movilidad (art. 83)",
  lit("TREBEP", "Artículo 83", ["de conformidad con lo que establezcan los convenios colectivos", "en su defecto por el sistema de provisión de puestos y movilidad del personal funcionario de carrera"]),
  fichab("Provisión y movilidad del personal laboral",
         "—", "Lo que establezcan los **convenios colectivos**", "—",
         "Si el convenio no lo regula, se aplica **supletoriamente** el sistema de los **funcionarios de carrera**. La provisión, en el tema V.4."))}

{unidad("2.7 Situaciones (art. 92)",
  lit("TREBEP", "Artículo 92", ["se regirá por el Estatuto de los Trabajadores y por los Convenios Colectivos", "en lo que resulte compatible con el Estatuto de los Trabajadores"]),
  fichab("Situaciones del personal laboral",
         "—", ["Rigen el **Estatuto de los Trabajadores** y los **convenios colectivos**", "Los convenios **pueden** extenderle el capítulo de situaciones del TREBEP, en lo compatible con el Estatuto de los Trabajadores"], "—",
         "El capítulo de situaciones del TREBEP no se le aplica directamente: solo si lo dice el **convenio**. Las situaciones de los funcionarios, en el tema V.5."))}

{unidad("2.8 Régimen disciplinario (art. 93.1 y 4)",
  lit("TREBEP", "Artículo 93", ["Los funcionarios públicos y el personal laboral quedan sujetos al régimen disciplinario establecido en el presente título", "en lo no previsto en el presente título, por la legislación laboral"], solo=[1, 4]),
  fichab("Régimen disciplinario del personal laboral",
         "Funcionarios y personal laboral",
         ["El título VII del TREBEP se aplica **también** al personal laboral (93.1)", "En lo no previsto, la **legislación laboral** (93.4)"],
         "—",
         f"Sanción propia del laboral: {c('TREBEP', 'Artículo 96', 'Despido disciplinario del personal laboral, que sólo podrá sancionar la comisión de faltas muy graves')} (art. 96.1 b). El régimen disciplinario, en el tema V.2."))}

### 2.9 Cuadro: qué norma rige cada materia (esquema)

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Materia | Artículo del TREBEP | Qué se aplica al personal laboral |
|---|---|---|
| Régimen general | 7 | Legislación laboral + convenios + preceptos del TREBEP que así lo dispongan |
| Permisos de nacimiento, adopción, lactancia y parental | 7, párrafo 2.º | El TREBEP (no las suspensiones del Estatuto de los Trabajadores) |
| Selección | 11.3 y 61.7 | Procedimientos públicos; igualdad, mérito y capacidad (temporal: también celeridad) |
| Carrera y promoción | 19 | Estatuto de los Trabajadores o convenios |
| Retribuciones | 27 | Legislación laboral, convenio y contrato, respetando el art. 21 |
| Negociación, representación y participación | 32.1 | {c('TREBEP', 'Artículo 32', 'se regirá por la legislación laboral, sin perjuicio de los preceptos de este capítulo que expresamente les son de aplicación')} (tema V.8) |
| Jornada, permisos y vacaciones | 51 | El capítulo del TREBEP y la legislación laboral |
| Clasificación | 77 | Legislación laboral |
| Provisión y movilidad | 83 | Convenios; en su defecto, el sistema de los funcionarios de carrera |
| Situaciones | 92 | Estatuto de los Trabajadores y convenios |
| Régimen disciplinario | 93 | El título VII del TREBEP; en lo no previsto, la legislación laboral |

{resumen([
  "Las funciones con **potestades públicas** o de salvaguardia de los intereses generales son **exclusivas** de los funcionarios (TREBEP, art. 9.2).",
  "Los criterios de los puestos laborales los fijan las **leyes de Función Pública** (art. 11.2). En la AGE, la regla es el **funcionario** y el laboral, la excepción (Ley 30/1984, art. 15.1 c).",
  "Los nuevos contratos de **personal laboral fijo** exigen que el puesto figure en la **RPT** (art. 15.1 f).",
  "Preceptos del TREBEP: promoción por el **ET o los convenios** (19); retribuciones según ley laboral, convenio y contrato (27); clasificación según la **legislación laboral** (77); provisión según **convenio** y, en su defecto, el sistema funcionarial (83); situaciones según **ET y convenios** (92)."],
  "Siguiente: III. ¿A quién se aplica el IV Convenio Único?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿A quién se aplica el IV Convenio Único? Ámbito de aplicación (arts. 1 a 4 y 124)", donde(
  "Tercera pregunta. En la AGE, la norma convencional del art. 7 TREBEP es el **IV Convenio colectivo único para el personal laboral de la Administración General del Estado** (registrado y publicado por Resolución de 13 de mayo de 2019, de la Dirección General de Trabajo). Su título I regula el **ámbito de aplicación y vigencia**.",
  ["1 Personal incluido (art. 1)", "2 Personal excluido (art. 2)", "3 Vigencia, carácter unitario y derecho supletorio (arts. 3, 4 y 124; disposición adicional duodécima)"]))

T.ap("s5", "III.1 Personal incluido (art. 1)", f"""
{unidad("1.1 La regla y los ámbitos añadidos (art. 1.1 y 2)",
  lit("CONV", "Artículo 1", ["al personal laboral de la Administración General del Estado y sus organismos autónomos", "La Administración de Justicia no transferida", "El Consejo de Seguridad Nuclear", "La Agencia Española de Protección de Datos", "El Museo Nacional Centro de Arte Reina Sofía", "Trabajo Penitenciario y Formación para el Empleo"], solo=[1, 2, 3, 4, 5, 6, 7, 8]),
  fichab("Ámbito personal del IV Convenio Único",
         "Personal laboral",
         ["::Regla (1.1): la **AGE y sus organismos autónomos**. Además (1.2):", "La **Administración de Justicia no transferida**", "La **Administración de la Seguridad Social**, incluido, en el INGESA, el personal de los Servicios Centrales y de las Direcciones Territoriales y/o Provinciales", "El **Consejo de Seguridad Nuclear**", "La **Agencia Española de Protección de Datos**", "El **Museo Nacional Centro de Arte Reina Sofía**", "**Trabajo Penitenciario y Formación para el Empleo**"],
         "—",
         "Cayó en 2025 (→ Cierre 1): el **Reina Sofía**, la **AEPD** y el **CSN** están **incluidos**; el personal en el **exterior**, **excluido** (→ III.2)."))}

{unidad("1.2 Inclusión de nuevo personal (art. 1.3)",
  lit("CONV", "Artículo 1", ["la mayoría del colectivo afectado manifieste su conformidad", "Subcomisión Paritaria correspondiente", "Comisión Paritaria para su aprobación", "Dirección General de Costes de Personal y Pensiones Públicas", "Dirección General de la Función Pública"], solo=[9]),
  fichab("Procedimiento para incluir personal nuevo en el Convenio",
         "Colectivo afectado (conformidad); Subcomisión Paritaria (trata la propuesta); **Comisión Paritaria** (aprueba)",
         ["Conformidad de la **mayoría** del colectivo, individualmente o a través de sus representantes", "Propuesta tratada en la **Subcomisión Paritaria** y elevada a la **Comisión Paritaria**", "Previo informe favorable de la **DG de Costes de Personal y Pensiones Públicas** y de la **DG de la Función Pública**"],
         "Mayoría del colectivo afectado",
         "Aprueba la **Comisión Paritaria** (no la Comisión Negociadora, que es la que modifica la **clasificación**: → IV.4.1). Los informes favorables son **dos**."))}
""", 2)

T.ap("s6", "III.2 Personal excluido (art. 2)", f"""
{unidad("2.1 Quién queda fuera del Convenio (art. 2)",
  lit("CONV", "Artículo 2", ["El personal laboral que presta servicios en el exterior", "otros Convenios colectivos de la Administración General del Estado", "El personal de alta dirección", "expresamente fuera de Convenio", "no citadas expresamente en el artículo 1", "El profesorado de religión"]),
  fichab("Personal excluido del IV Convenio Único",
         "—",
         ["a) Personal laboral en el **exterior**", "b) Personal de **otros convenios** colectivos de la AGE", "c) Personal de **alta dirección** (ET, art. 2.1 a)", "d) Personal con contrato regulado por la normativa de **contratación administrativa** o en instrumentos excluidos por la Ley 9/2017", "e) Profesionales con **minuta o presupuesto** para una obra o servicio concreto", "f) Personal contratado **expresamente fuera de Convenio** (excepcional, informando a la Comisión Paritaria)", "g) Personal de **entidades del sector público no citadas** en el art. 1", "h) **Profesorado de religión** de los convenios con la Santa Sede y otras confesiones"],
         "—",
         "**Ocho** exclusiones. La que cae: el personal laboral en el **exterior** (letra a). Ojo: la Ley 30/1984 sí permite puestos laborales en el extranjero (→ II.1.3), pero **no** se rigen por este Convenio."))}
""", 2)

T.ap("s7", "III.3 Vigencia, carácter unitario y derecho supletorio (arts. 3, 4 y 124; disposición adicional duodécima)", f"""
{unidad("3.1 Entrada en vigor, vigencia, denuncia y prórroga (art. 3)",
  lit("CONV", "Artículo 3", ["el día siguiente de su publicación", "desde el día 1 de enero de 2019", "hasta el 31 de diciembre de 2021", "dentro de los dos meses inmediatos anteriores a la terminación de su vigencia", "En el plazo de un mes", "se prorrogará automáticamente por períodos anuales", "se mantendrá la vigencia de la totalidad de su contenido"]),
  fichab("Ámbito temporal del Convenio",
         "Cualquiera de las partes (denuncia); la Comisión Negociadora (se constituye tras la denuncia)",
         ["Entrada en vigor: el **día siguiente** de su publicación en el BOE; efectos económicos desde el **1 de enero de 2019**", "Vigencia hasta el **31 de diciembre de 2021**", "Sin denuncia expresa: **prórroga automática por períodos anuales**", "Denunciado: se mantiene **todo** su contenido hasta que otro lo sustituya"],
         "Denuncia: en los **dos meses** anteriores al fin de la vigencia; Comisión Negociadora: en **un mes** desde la recepción de la comunicación",
         "La vigencia inicial terminaba el **31-12-2021**. Desde entonces, sin denuncia expresa, se **prorroga por períodos anuales**; denunciado, se mantiene la vigencia de **la totalidad** de su contenido (no solo de las cláusulas normativas) hasta que otro lo sustituya (3.3)."))}

{unidad("3.2 Un todo orgánico e indivisible (art. 4.1 a 3)",
  lit("CONV", "Artículo 4", ["forma un todo orgánico e indivisible", "considerado globalmente", "compensan y sustituyen a todas las existentes en el III Convenio único"], solo=[1, 2, 3]),
  fichab("Unidad del Convenio, nulidad y relación con el III Convenio único",
         "Las partes; la jurisdicción social (anulación)",
         ["Se aplica **globalmente**: es un todo orgánico e indivisible", "Anulación **total**: se negocia uno nuevo y, mientras, se aplica el anterior", "Anulación **parcial**: se negocia la parte anulada y el resto sigue vigente", "Sus condiciones **compensan y sustituyen** a las del **III Convenio único**"],
         "—",
         "El apartado 4 del art. 4 figura en el BOE como **(Anulado)**: no se cita como vigente."))}

{unidad("3.3 Derecho supletorio (art. 124) y condición presupuestaria (disposición adicional duodécima)",
  lit("CONV", "Artículo 124", ["se estará a lo dispuesto en el Estatuto de los Trabajadores"]),
  lit("CONV", "Disposición adicional duodécima", ["condicionada a la existencia de las disponibilidades presupuestarias necesarias"], titulo="Disposición adicional duodécima (IV Convenio Único)"),
  fichab("Qué se aplica en lo no previsto y de qué depende la efectividad del Convenio",
         "—",
         ["Lo no previsto: el **Estatuto de los Trabajadores** y demás disposiciones legales o reglamentarias aplicables (124)", "Efectividad condicionada a las **disponibilidades presupuestarias** (DA 12.ª)"],
         "—",
         "Supletorio: el **Estatuto de los Trabajadores**, no el TREBEP. Coincide con el orden del art. 7 TREBEP (→ I.2.2)."))}

{resumen([
  "Se aplica al personal laboral de la **AGE y sus organismos autónomos** y, además, al de la **Administración de Justicia no transferida**, la **Seguridad Social**, el **CSN**, la **AEPD**, el **Reina Sofía** y **Trabajo Penitenciario y Formación para el Empleo** (art. 1).",
  "Nuevo personal: conformidad de la **mayoría** del colectivo y aprobación de la **Comisión Paritaria** (art. 1.3).",
  "Excluidos, entre otros: personal en el **exterior**, de **otros convenios** de la AGE, de **alta dirección**, **fuera de Convenio** y de entidades **no citadas** en el art. 1 (art. 2).",
  "Vigencia hasta el **31-12-2021** y **prórroga anual automática** sin denuncia; denunciado, se mantiene **todo** su contenido (art. 3). Supletorio: el **Estatuto de los Trabajadores** (art. 124)."],
  "Siguiente: IV. ¿Cómo se clasifica al personal? El sistema de clasificación")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Cómo se clasifica al personal? El sistema de clasificación (ET, art. 22; Convenio, arts. 7 a 19 y anexo II)", donde(
  "Cuarta pregunta. El art. 77 TREBEP remite la clasificación del personal laboral a la **legislación laboral** (→ II.2.5): el Estatuto de los Trabajadores exige **grupos profesionales** fijados por la negociación colectiva, y el título III del IV Convenio Único los define.",
  ["1 La base legal: grupos profesionales (ET, art. 22)", "2 El sistema del Convenio: grupos, familias y especialidades (arts. 7, 8 y 9)", "3 Las especialidades (art. 10)", "4 Quién decide sobre la clasificación (arts. 11, 12, 15, 16 y 19)", "5 Encuadramiento y colectivos del anexo II (DA 1.ª, DT 1.ª y anexo II)"]))

T.ap("s8", "IV.1 La base legal: clasificación por grupos profesionales (ET, art. 22)", f"""
{unidad("1.1 Sistema de clasificación profesional (ET, art. 22.1, 2 y 4)",
  lit("ET", "Artículo 22", ["Mediante la negociación colectiva o, en su defecto, acuerdo entre la empresa y los representantes de los trabajadores", "por medio de grupos profesionales", "agrupe unitariamente las aptitudes profesionales, titulaciones y contenido general de la prestación"], solo=[1, 2, 4]),
  fichab("El sistema de clasificación profesional en la legislación laboral",
         "La **negociación colectiva** o, en su defecto, el acuerdo entre la empresa y los representantes de los trabajadores; trabajador y empresario asignan el grupo",
         ["Clasificación **por grupos profesionales** (22.1)", "Grupo profesional: aptitudes profesionales, titulaciones y contenido general de la prestación (22.2)", "El contrato asigna un grupo y fija las funciones (todas o algunas del grupo) (22.4)"],
         "—",
         "La definición del Convenio de **grupo profesional** (art. 7.3 → IV.2.1) reproduce la del art. 22.2 ET. El art. 22.3 añade que la definición de los grupos debe garantizar la **ausencia de discriminación** entre mujeres y hombres."))}
""", 2)

T.ap("s9", "IV.2 El sistema del Convenio: grupos, familias y especialidades (arts. 7, 8 y 9)", f"""
{unidad("2.1 Sistema de clasificación (art. 7)",
  lit("CONV", "Artículo 7", ["grupos profesionales, familias profesionales y/o especialidades", "Sistema Educativo y con el Sistema Nacional de Cualificaciones Profesionales", "agrupa unitariamente las aptitudes profesionales, las titulaciones y el contenido general de la prestación laboral", "criterios de afinidad de la competencia profesional", "determina el contenido concreto de la prestación laboral", "solo podrá modificarse a través de los procedimientos previstos en el mismo"]),
  fichab("Estructura del sistema de clasificación del IV Convenio Único",
         "Personal laboral del ámbito del Convenio",
         ["::Tres niveles (7.1):", "**Grupo profesional**: aptitudes, titulaciones y contenido general de la prestación (7.3)", "**Familia profesional**: titulaciones, cualificaciones, profesiones, oficios y ocupaciones afines (7.4)", "**Especialidad**: contenido **concreto** de la prestación y perfil de cada puesto (7.5)", "::Se relaciona con el **Sistema Educativo** y el **Sistema Nacional de Cualificaciones Profesionales**"],
         "—",
         "Finalidades (7.1): ordenar los puestos por titulación, formación y capacitación, ordenar la **movilidad** y favorecer la **promoción**. La clasificación **solo** se modifica por los procedimientos del propio Convenio (7.6 → IV.4.1)."))}

{unidad("2.2 Los seis grupos profesionales (art. 8)",
  lit("CONV", "Artículo 8", ["Grupo profesional M3", "Grupo profesional M2", "Grupo profesional M1", "Grupo profesional E2: Título de Bachiller o Técnico o equivalentes", "Grupo profesional E1", "Grupo profesional E0: Sin titulación prevista en el sistema educativo", "las acordadas por la autoridad competente en materia de Educación", "título de Doctor", "previa aprobación por la Comisión Paritaria", "anexos II y IV"]),
  fichab("Grupos profesionales por la titulación exigida para el ingreso",
         "—",
         ["**M3**: Nivel **3** del Marco Español de Cualificaciones para la Educación Superior (MECES)", "**M2**: Nivel **2** del MECES", "**M1**: Nivel **1** del MECES", "**E2**: **Bachiller o Técnico**", "**E1**: **Graduado en ESO o Título Profesional Básico**", "**E0**: **sin titulación** prevista en el sistema educativo"],
         "Puestos que requieran el **título de Doctor**: lo indica la convocatoria y se adecúan las retribuciones, **previa aprobación de la Comisión Paritaria** (8.3)",
         "Cayó **dos** veces en 2025 (→ Cierre 1): **E2 = Bachiller o Técnico**. Las equivalencias las acuerda la **autoridad competente en materia de Educación** (8.2). Esta clasificación **no** se aplica al personal de los **anexos II y IV** (8.4 → IV.5.3)."))}

{unidad("2.3 Familias profesionales (art. 9)",
  lit("CONV", "Artículo 9", ["por la autoridad competente dentro del Sistema Nacional de Cualificaciones y Formación Profesional", "la Administración determinará las familias profesionales"]),
  fichab("Las familias profesionales del Convenio",
         "Las define la autoridad competente del Sistema Nacional de Cualificaciones y Formación Profesional; la **Administración** determina las coincidentes con sus necesidades",
         "Se toman las del Sistema Nacional de Cualificaciones y Formación Profesional",
         "—",
         "El Convenio **no** crea familias propias: usa las del Sistema Nacional de Cualificaciones."))}
""", 2)

T.ap("s10", "IV.3 Las especialidades (art. 10)", f"""
{unidad("3.1 Cada puesto, una especialidad; qué determina en cada grupo (art. 10)",
  lit("CONV", "Artículo 10", ["Todos los puestos de trabajo tendrán asignada una especialidad", "Para los Grupos M3 y M2 la especialidad determinará la titulación o titulaciones universitarias exigidas para el ingreso", "Formación Profesional de Grado Superior", "Formación Profesional de Grado Medio", "Formación Profesional de Grado Básico", "por la Comisión Ejecutiva de la Comisión Interministerial de Retribuciones, previa aprobación por la Comisión Paritaria", "durante los cinco años inmediatamente siguientes"]),
  fichab("La especialidad y lo que determina",
         "Creación de especialidades sin título o cualificación de referencia (E2, E1 y E0): la **Comisión Ejecutiva de la Comisión Interministerial de Retribuciones**, previa aprobación de la **Comisión Paritaria**; titulación afín (10.7): la **Comisión Paritaria**, a propuesta del Departamento u Organismo",
         ["Todos los puestos tienen asignada una especialidad (10.1)", "**M3 y M2**: la titulación **universitaria** exigida (10.2)", "**M1**: título de **FP de Grado Superior** o cualificación de **Nivel 3** (10.3)", "**E2**: título de **FP de Grado Medio** o cualificación de **Nivel 2** (10.4)", "**E1**: título de **FP de Grado Básico** o cualificación de **Nivel 1** (10.5)", "**E0**: unidades de competencia de cualificaciones de **Nivel 1** (10.6)"],
         "Titulación afín transitoria: hasta que se implante la titulación y, en su caso, durante los **cinco años** siguientes a su implantación efectiva (10.7)",
         "Para la movilidad por **concurso abierto y permanente**, la especialidad reconocida se entiende acreditada, salvo titulación o formación **habilitante** (10.1). Cruce típico: M1 ↔ Grado Superior/Nivel 3; E2 ↔ Grado Medio/Nivel 2; E1 ↔ Grado Básico/Nivel 1."))}
""", 2)

T.ap("s11", "IV.4 Quién decide sobre la clasificación (arts. 11, 12, 15, 16 y 19)", f"""
{unidad("4.1 Modificación de la clasificación de un colectivo (art. 11)",
  lit("CONV", "Artículo 11", ["cambio en el contenido de la prestación laboral", "sólo podrá ser aprobada por la Comisión Negociadora del Convenio", "a propuesta de la correspondiente Subcomisión Paritaria", "previo informe favorable de la Comisión Paritaria"]),
  fichab("Modificación de la clasificación profesional de determinados colectivos",
         "Aprueba la **Comisión Negociadora**; propone la **Subcomisión Paritaria** del colectivo; informa favorablemente la **Comisión Paritaria**",
         "Solo si un **cambio en el contenido de la prestación** ha modificado las aptitudes profesionales y/o las titulaciones necesarias, y con ellas los factores del encuadramiento",
         "Informe **favorable** de la Comisión Paritaria",
         "Cayó en 2025 (→ Cierre 1): **aprueba la Comisión Negociadora** (no la Paritaria, ni la Subcomisión, ni la Mesa General). Orden: Subcomisión **propone** → Paritaria **informa** → Negociadora **aprueba**."))}

{unidad("4.2 Comisión Negociadora y Comisión Paritaria (art. 12)",
  lit("CONV", "Artículo 12", ["órgano encargado de la negociación", "artículo 88 del Estatuto de los Trabajadores", "órgano máximo de interpretación, vigilancia, seguimiento, estudio y aplicación"]),
  fichab("Los dos órganos del Convenio",
         ["**Comisión Negociadora**: negocia en el marco del Convenio (ET, art. 88)", "**Comisión Paritaria**: representantes de las **partes firmantes**"],
         "La Paritaria interpreta, vigila, sigue, estudia y aplica lo pactado durante la vigencia",
         "—",
         "Paritaria = **órgano máximo de interpretación** y vigilancia; Negociadora = **negociación**. Por eso la modificación de la clasificación (que es negociar) la aprueba la Negociadora (→ IV.4.1)."))}

{unidad("4.3 Funciones de la Comisión Paritaria sobre la clasificación (art. 15 a, i y r)",
  lit("CONV", "Artículo 15", ["Interpretar la totalidad del articulado", "Aprobar la creación o modificación de especialidades según lo dispuesto en el artículo 10", "título de Doctor"], solo=[1, 2, 10, 19]),
  fichab("Funciones de la Comisión Paritaria relacionadas con la clasificación",
         "Comisión Paritaria",
         ["Interpretar el Convenio y vigilar y exigir su cumplimiento (a)", "Aprobar la **creación o modificación de especialidades** (i → IV.3.1)", "Aprobar la adecuación retributiva de los puestos que requieran el **título de Doctor** (r → IV.2.2)"],
         f"Expedientes de la Comisión y de la Subcomisión Paritaria: {c('CONV', 'Artículo 15', 'en el plazo máximo de tres meses')}; transcurrido sin resolución, {c('CONV', 'Artículo 15', 'se entenderán desestimados')} (letra u)",
         "Las especialidades las aprueba la **Paritaria**; la modificación de la clasificación de un **colectivo**, la **Negociadora** (→ IV.4.1)."))}

{unidad("4.4 Reuniones de la Comisión Paritaria (art. 16.2)",
  lit("CONV", "Artículo 16", ["al menos una vez al mes", "cuando lo soliciten al menos siete de las personas que componen la parte social o de la Administración", "por medios electrónicos"], solo=[3]),
  fichab("Funcionamiento de la Comisión Paritaria: reuniones",
         "La Comisión Paritaria (que funciona en Pleno y en Comisión Permanente: 16.1)",
         ["Ordinarias: **al menos una vez al mes**", "Extraordinarias: a solicitud de **al menos siete** personas de la parte social o de la Administración", "Por medios electrónicos, si lo acuerdan las partes por circunstancias extraordinarias"],
         "Ordinaria mensual; extraordinaria con **siete** solicitantes",
         f"Cayó en 2025 como pregunta de reserva (→ Cierre 1): **siete**, no cinco ni seis. La Comisión se compone de {c('CONV', 'Artículo 14', 'quince personas en representación de cada una de las partes')} (art. 14.2)."))}

{unidad("4.5 Subcomisiones Paritarias (art. 19.1 y 2)",
  lit("CONV", "Artículo 19", ["Dependiente de la Comisión Paritaria, y como órgano delegado de la misma", "en el ámbito de cada Departamento", "no podrá ser superior a quince"], solo=[1, 2, 3]),
  fichab("Subcomisiones Paritarias",
         "Una por **Departamento** y en el CSN, CSIC, CIEMAT, Entidades Gestoras de la Seguridad Social, Administración de Justicia e Instituciones Penitenciarias; otras, por acuerdo de la Comisión Paritaria",
         "Órgano **delegado** de la Comisión Paritaria: vigilancia, estudio y aplicación del Convenio en su ámbito",
         "Representantes por cada parte: **no más de quince**",
         "La Subcomisión **propone** la modificación de la clasificación de su colectivo (→ IV.4.1) y trata la inclusión de nuevo personal (→ III.1.2)."))}
""", 2)

T.ap("s12", "IV.5 Encuadramiento y colectivos del anexo II (DA 1.ª, DT 1.ª y anexo II)", f"""
{unidad("5.1 Encuadramiento del personal del III Convenio (disposición adicional primera)",
  lit("CONV", "Disposición adicional primera", ["se realizará de la forma que figura en el anexo I"]),
  fichab("Paso del III al IV Convenio único", "Personal del III Convenio único", "Se encuadra en los nuevos grupos según el **anexo I**", "—",
         "El anexo I es la tabla de correspondencias; el BOE lo publica en forma de cuadro, por lo que no se reproduce aquí."))}

{unidad("5.2 Puestos con funciones reservadas a funcionarios o no requeridas (disposición transitoria primera)",
  lit("CONV", "Disposición transitoria primera", ["no habrá convocatorias de acceso libre", "reservadas al personal funcionario", "anexo II", "se promoverán procesos de promoción interna a los Cuerpos o Escalas de funcionarios de carrera"]),
  fichab("Régimen de los puestos cuyo desempeño ya no se requiere en el ámbito del Convenio",
         "Personal laboral fijo de esos puestos",
         ["Sin **convocatorias de acceso libre** para puestos con funciones reservadas a funcionarios o no requeridas por la organización", "Las actividades se relacionan en el **anexo II**, que fija su clasificación, promoción, movilidad y retribuciones", "Para el personal laboral fijo en funciones reservadas a funcionarios: **promoción interna** a Cuerpos o Escalas de funcionarios de carrera"],
         "—",
         "Conecta con el art. 9.2 TREBEP (→ II.1.1): lo reservado a funcionarios no se cubre con nuevo personal laboral por acceso libre."))}

{unidad("5.3 Clasificación propia de los colectivos del anexo II (anexo II, a y b)",
  lit("CONV", "ANEXO II", ["Gestión de Recursos Humanos", "Gestión Económica", "Gestión Administrativa", "no le resultará de aplicación la regulación contenida en los títulos III y VI"], solo=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], titulo="Anexo II, a) Conjunto de actividades (IV Convenio Único)"),
  lit("CONV", "ANEXO II", ["G1:", "G2:", "G3:", "G4:"], solo=[22, 23, 24, 25, 26], titulo="Anexo II, b) Clasificación profesional (IV Convenio Único)"),
  fichab("Colectivos que conservan una clasificación propia (G1 a G4)",
         "Personal laboral que, a la entrada en vigor del Convenio, ocupaba puestos con alguna de las funciones del anexo II",
         ["No se le aplican los títulos **III** (clasificación profesional) y **VI** del Convenio", "Se clasifica en **G1, G2, G3 y G4**, según la titulación y su grupo en el III Convenio único"],
         "—",
         "Por eso el art. 8.4 excluye a este personal de los grupos M3 a E0 (→ IV.2.2). Entre sus actividades están la **gestión de recursos humanos, económica y administrativa**."))}

### 5.4 Cuadro de los grupos profesionales (esquema)

*Esquema de elaboración propia: resume los arts. 8 y 10 del IV Convenio Único; no es texto legal.*

| Grupo | Titulación para el ingreso (art. 8.1) | Qué determina la especialidad (art. 10) |
|---|---|---|
| **M3** | Nivel 3 del MECES | Titulación universitaria |
| **M2** | Nivel 2 del MECES | Titulación universitaria |
| **M1** | Nivel 1 del MECES | FP de Grado Superior o cualificación de Nivel 3 |
| **E2** | Bachiller o Técnico | FP de Grado Medio o cualificación de Nivel 2 |
| **E1** | Graduado en ESO o Título Profesional Básico | FP de Grado Básico o cualificación de Nivel 1 |
| **E0** | Sin titulación prevista en el sistema educativo | Unidades de competencia de Nivel 1 |

{resumen([
  "El ET exige clasificar **por grupos profesionales** mediante la **negociación colectiva** (art. 22).",
  "El Convenio se estructura en **grupos profesionales, familias profesionales y/o especialidades** (art. 7).",
  "Seis grupos por titulación: **M3, M2, M1** (niveles 3, 2 y 1 del MECES), **E2** (Bachiller o Técnico), **E1** (ESO o Título Profesional Básico) y **E0** (sin titulación) (art. 8).",
  "Todo puesto tiene una **especialidad**; las especialidades las aprueba la **Comisión Paritaria** (arts. 10 y 15 i).",
  "Modificar la clasificación de un colectivo: propone la **Subcomisión Paritaria**, informa la **Comisión Paritaria** y aprueba la **Comisión Negociadora** (art. 11).",
  "El personal del **anexo II** conserva los grupos **G1 a G4** (art. 8.4 y anexo II)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_L74 = examen("L", 74, {
  "a": f"Nivel 1 del MECES es la titulación del grupo **M1**: {c('CONV', 'Artículo 8', 'Grupo profesional M1: Título clasificado en el Nivel 1 del Marco Español de Cualificaciones para la Educación Superior o equivalentes')}.",
  "b": f"Literal del art. 8.1 d): {c('CONV', 'Artículo 8', 'Grupo profesional E2: Título de Bachiller o Técnico o equivalentes')}.",
  "c": f"Nivel 3 del MECES es la del grupo **M3**: {c('CONV', 'Artículo 8', 'Grupo profesional M3: Título clasificado en el Nivel 3')}.",
  "d": f"Nivel 2 del MECES es la del grupo **M2**: {c('CONV', 'Artículo 8', 'Grupo profesional M2: Título clasificado en el Nivel 2')}."},
  [("Título de Bachiller o Técnico o equivalentes", "CONV", "Artículo 8", "Grupo profesional E2: Título de Bachiller o Técnico o equivalentes")])
EX_P79 = examen("P", 79, {
  "a": f"E1 exige {c('CONV', 'Artículo 8', 'Título de Graduado en Educación Secundaria Obligatoria o Título Profesional Básico o equivalentes')}.",
  "b": f"Literal del art. 8.1 d): {c('CONV', 'Artículo 8', 'Grupo profesional E2: Título de Bachiller o Técnico o equivalentes')}.",
  "c": f"M1 exige un {c('CONV', 'Artículo 8', 'Título clasificado en el Nivel 1 del Marco Español de Cualificaciones para la Educación Superior')}.",
  "d": f"M2 exige un {c('CONV', 'Artículo 8', 'Título clasificado en el Nivel 2 del Marco Español de Cualificaciones para la Educación Superior')}."},
  [("E2", "CONV", "Artículo 8", "Grupo profesional E2: Título de Bachiller o Técnico o equivalentes")])
EX_P80 = examen("P", 80, {
  "a": f"La Comisión Paritaria solo emite el **informe favorable** previo: {c('CONV', 'Artículo 11', 'previo informe favorable de la Comisión Paritaria')}.",
  "b": f"La Subcomisión Paritaria **propone**: {c('CONV', 'Artículo 11', 'a propuesta de la correspondiente Subcomisión Paritaria')}.",
  "c": f"Literal del art. 11.2: {c('CONV', 'Artículo 11', 'sólo podrá ser aprobada por la Comisión Negociadora del Convenio')}.",
  "d": f"La Mesa General de Negociación es un órgano de negociación del TREBEP (art. 36.3: {c('TREBEP', 'Artículo 36', 'se constituirá en la Administración General del Estado')}…), no un órgano del Convenio; el art. 11 no la menciona."},
  [("Comisión Negociadora", "CONV", "Artículo 11", "sólo podrá ser aprobada por la Comisión Negociadora del Convenio")])
EX_P104 = examen("P", 104, {
  "a": f"«Una vez al mes» es la periodicidad mínima de las reuniones **ordinarias**: {c('CONV', 'Artículo 16', 'con carácter ordinario al menos una vez al mes')}.",
  "b": f"Cambia el número: el art. 16.2 exige {c('CONV', 'Artículo 16', 'al menos siete')}, no cinco.",
  "c": f"Cambia el número: el art. 16.2 exige {c('CONV', 'Artículo 16', 'al menos siete')}, no seis.",
  "d": f"Literal del art. 16.2: {c('CONV', 'Artículo 16', 'con carácter extraordinario, cuando lo soliciten al menos siete de las personas que componen la parte social o de la Administración')}."},
  [("al menos siete", "CONV", "Artículo 16", "cuando lo soliciten al menos siete de las personas que componen la parte social o de la Administración")])
EX_X82 = examen("X", 82, {
  "a": f"Incluido expresamente: {c('CONV', 'Artículo 1', 'El Museo Nacional Centro de Arte Reina Sofía')} (art. 1.2 e).",
  "b": f"Incluido expresamente: {c('CONV', 'Artículo 1', 'La Agencia Española de Protección de Datos')} (art. 1.2 d).",
  "c": f"Incluido expresamente: {c('CONV', 'Artículo 1', 'El Consejo de Seguridad Nuclear')} (art. 1.2 c).",
  "d": f"Excluido por el art. 2 a): {c('CONV', 'Artículo 2', 'El personal laboral que presta servicios en el exterior')}."},
  [("en el exterior", "CONV", "Artículo 2", "El personal laboral que presta servicios en el exterior")])
EX_P81 = examen("P", 81, {
  "a": f"Falta la tercera fuente: también le rigen {c('TREBEP', 'Artículo 7', 'los preceptos de este Estatuto que así lo dispongan')}; no es «exclusivamente» la legislación laboral y los convenios.",
  "b": f"Literal del art. 7: se rige {c('TREBEP', 'Artículo 7', 'además de por la legislación laboral y por las demás normas convencionalmente aplicables, por los preceptos de este Estatuto que así lo dispongan')}.",
  "c": f"Es al revés: en esos permisos {c('TREBEP', 'Artículo 7', 'se regirá por lo previsto en el presente Estatuto')}, no por el Estatuto de los Trabajadores.",
  "d": f"El TREBEP no se le aplica íntegramente: solo {c('TREBEP', 'Artículo 7', 'los preceptos de este Estatuto que así lo dispongan')}, y el art. 2.1 lo aplica {c('TREBEP', 'Artículo 2', 'en lo que proceda al personal laboral')}."},
  [("que así lo dispongan", "TREBEP", "Artículo 7", "por los preceptos de este Estatuto que así lo dispongan")])
EX_P82 = examen("P", 82, {
  "a": f"Al revés: {c('TREBEP', 'Artículo 19', 'El personal laboral tendrá derecho a la promoción profesional')} (art. 19.1).",
  "b": f"Cambia la norma: los procedimientos no son los del Estatuto Básico, sino {c('TREBEP', 'Artículo 19', 'los procedimientos previstos en el Estatuto de los Trabajadores o en los convenios colectivos')}.",
  "c": f"Literal del art. 19.2: {c('TREBEP', 'Artículo 19', 'se hará efectiva a través de los procedimientos previstos en el Estatuto de los Trabajadores o en los convenios colectivos')}.",
  "d": "El art. 19 no prevé la libre designación: remite a los procedimientos del Estatuto de los Trabajadores o de los convenios colectivos."},
  [("procedimientos previstos en el Estatuto de los Trabajadores o en los convenios colectivos", "TREBEP", "Artículo 19", "a través de los procedimientos previstos en el Estatuto de los Trabajadores o en los convenios colectivos")])

T.ap("s13", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **cinco** preguntas de este tema (cuatro de ellas sobre el sistema de clasificación y el ámbito del Convenio, y una de reserva sobre la Comisión Paritaria) y **dos** relacionadas sobre el régimen jurídico del personal laboral en el TREBEP. Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-L 2025, pregunta 74 · Titulación del grupo E2 (→ IV.2.2)", EX_L74,
  "### GACE-P 2025, pregunta 79 · Grupo que exige Bachiller o Técnico (→ IV.2.2)", EX_P79,
  "### GACE-P 2025, pregunta 80 · Quién modifica la clasificación (→ IV.4.1)", EX_P80,
  "### GACE-P 2025, pregunta 104 (reserva) · Reuniones extraordinarias de la Comisión Paritaria (→ IV.4.4)", EX_P104,
  "### GACE-L 2025 extraordinario, pregunta 82 · Personal excluido del Convenio (→ III.2.1)", EX_X82,
  "### GACE-P 2025, pregunta 81 · Normativa aplicable al personal laboral (relacionada; → I.2.2)", EX_P81,
  "### GACE-P 2025, pregunta 82 · Carrera y promoción del personal laboral (relacionada; → II.2.2)", EX_P82,
  "### Cómo se pregunta",
  "!> Las preguntas del Convenio son de **dato exacto**: la titulación de cada grupo (los distractores son las de los grupos vecinos), el **órgano** que decide (Negociadora, Paritaria o Subcomisión) y el **número** (siete). Las del TREBEP juegan con **qué norma** rige: «exclusivamente», «íntegramente» o «el Estatuto Básico» en lugar del Estatuto de los Trabajadores o los convenios.",
]))

T.ap("s14", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Concepto y régimen | Contrato de trabajo por escrito; fijo, por tiempo indefinido o temporal (8 y 11.1); legislación laboral + convenios + TREBEP «que así lo dispongan» (7) | Art. 7: **tres fuentes**; permisos de nacimiento, adopción, lactancia y parental por el **TREBEP** |
| II. Puestos y preceptos del TREBEP | Potestades públicas, solo funcionarios (9.2); criterios por leyes de Función Pública (11.2); AGE: regla funcionario, excepciones (L30, 15.1 c); arts. 19, 27, 51, 77, 83, 92, 93 | Promoción por el **ET o los convenios** (19.2) |
| III. Ámbito del Convenio | AGE y OO. AA. + Justicia no transferida, Seguridad Social, CSN, AEPD, Reina Sofía, Trabajo Penitenciario (1); ocho exclusiones (2); vigencia y prórroga (3) | Excluido: personal en el **exterior** (2 a) |
| IV. Clasificación | Grupos, familias y/o especialidades (7); M3, M2, M1, E2, E1, E0 (8); especialidades (10); modificación (11); órganos (12, 15, 16, 19); anexo II | **E2 = Bachiller o Técnico**; modifica la clasificación la **Comisión Negociadora**; Paritaria extraordinaria con **siete** |

?> **Trampas frecuentes:** «el personal laboral se rige **exclusivamente** por la legislación laboral» (también por los preceptos del TREBEP que así lo dispongan); «personal laboral **interino**» (es fijo, por tiempo indefinido o temporal); «la promoción del laboral, por los procedimientos **del TREBEP**» (es por los del **ET o los convenios**); «el personal en el **exterior** está incluido» (está **excluido**); «E2: nivel 1 del MECES» (eso es **M1**); «la clasificación la modifica la **Comisión Paritaria**» (la **Negociadora**, previo informe favorable de la Paritaria); «extraordinaria con **cinco** solicitantes» (son **siete**).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
T.q("TREBEP", "Artículo 8", "Concepto", "Según el artículo 8.2 c) del TREBEP, el personal laboral puede ser:",
    ["Fijo, por tiempo indefinido o temporal.", "Fijo o interino.", "De carrera, interino o eventual.", "Fijo, eventual o de alta dirección."],
    "Art. 8.2 c) TREBEP: «Personal laboral, ya sea fijo, por tiempo indefinido o temporal».", "Personal laboral, ya sea fijo, por tiempo indefinido o temporal")
T.q("TREBEP", "Artículo 11", "Concepto", "Según el artículo 11.1 del TREBEP, es personal laboral el que presta servicios retribuidos por las Administraciones Públicas en virtud de:",
    ["Contrato de trabajo formalizado por escrito.", "Nombramiento legal.", "Contrato administrativo de servicios.", "Nombramiento de carácter no permanente."],
    "Art. 11.1 TREBEP. El nombramiento es propio de los funcionarios (art. 9.1) y del personal eventual (art. 12.1).", "en virtud de contrato de trabajo formalizado por escrito")
T.q("TREBEP", "Artículo 11", "Concepto", "Según el artículo 11.1 del TREBEP, el contrato del personal laboral podrá ser fijo, por tiempo indefinido o temporal en función de:",
    ["La duración del contrato.", "El grupo profesional.", "La Administración contratante.", "El sistema selectivo utilizado."],
    "Art. 11.1 TREBEP: «En función de la duración del contrato éste podrá ser fijo, por tiempo indefinido o temporal».", "En función de la duración del contrato éste podrá ser fijo, por tiempo indefinido o temporal")
T.q("ET", "Artículo 1", "Concepto", "Según el artículo 1.3 a) del Estatuto de los Trabajadores, se excluye del ámbito regulado por esa ley:",
    ["La relación de servicio de los funcionarios públicos.", "La relación del personal laboral fijo de las Administraciones Públicas.", "La relación del personal laboral temporal de las Administraciones Públicas.", "La relación del personal laboral de los organismos autónomos."],
    "Art. 1.3 a) ET. El personal laboral de las Administraciones sí está incluido.", "La relación de servicio de los funcionarios públicos")
T.q("TREBEP", "Artículo 1", "Régimen jurídico", "Según el artículo 1.2 del TREBEP, el Estatuto tiene asimismo por objeto, respecto del personal laboral al servicio de las Administraciones Públicas:",
    ["Determinar las normas aplicables a ese personal.", "Establecer las bases de su régimen estatutario.", "Aprobar su convenio colectivo.", "Fijar sus retribuciones."],
    "Art. 1.2 TREBEP. Las «bases del régimen estatutario» son las de los funcionarios (art. 1.1).", "Asimismo tiene por objeto determinar las normas aplicables al personal laboral al servicio de las Administraciones Públicas")
T.q("TREBEP", "Artículo 2", "Régimen jurídico", "Según el artículo 2.1 del TREBEP, el Estatuto se aplica al personal laboral al servicio de las Administraciones Públicas:",
    ["En lo que proceda.", "En todo caso y en su integridad.", "Solo en materia de retribuciones.", "Nunca: solo se aplica al personal funcionario."],
    "Art. 2.1 TREBEP: «al personal funcionario y en lo que proceda al personal laboral».", "en lo que proceda al personal laboral")
T.q("TREBEP", "Artículo 7", "Régimen jurídico", "Según el artículo 7 del TREBEP, el personal laboral al servicio de las Administraciones públicas se rige:",
    ["Por la legislación laboral, por las demás normas convencionalmente aplicables y por los preceptos del Estatuto que así lo dispongan.", "Exclusivamente por la legislación laboral y por los convenios colectivos.", "Por el Estatuto Básico del Empleado Público y, supletoriamente, por la legislación laboral.", "Por los convenios colectivos y, supletoriamente, por el Estatuto Básico del Empleado Público."],
    "Art. 7 TREBEP, párrafo primero.", "además de por la legislación laboral y por las demás normas convencionalmente aplicables, por los preceptos de este Estatuto que así lo dispongan")
T.q("TREBEP", "Artículo 7", "Régimen jurídico", "Según el artículo 7 del TREBEP, en materia de permisos de nacimiento, adopción, del progenitor diferente de la madre biológica, de lactancia y parental, el personal laboral al servicio de las Administraciones públicas se regirá:",
    ["Por lo previsto en el Estatuto Básico del Empleado Público.", "Por el Estatuto de los Trabajadores.", "Por el convenio colectivo aplicable.", "Por el contrato de trabajo."],
    "Art. 7 TREBEP, párrafo segundo: no se le aplican las suspensiones del contrato del Estatuto de los Trabajadores.", "se regirá por lo previsto en el presente Estatuto")
T.q("TREBEP", "Artículo 9", "Puestos", "Según el artículo 9.2 del TREBEP, el ejercicio de las funciones que impliquen la participación directa o indirecta en el ejercicio de las potestades públicas corresponde:",
    ["Exclusivamente a los funcionarios públicos.", "A los funcionarios públicos y al personal laboral fijo.", "Al personal directivo profesional.", "A los funcionarios públicos y, excepcionalmente, al personal laboral por tiempo indefinido."],
    "Art. 9.2 TREBEP.", "corresponden exclusivamente a los funcionarios públicos")
T.q("TREBEP", "Artículo 11", "Puestos", "Según el artículo 11.2 del TREBEP, los criterios para la determinación de los puestos de trabajo que pueden ser desempeñados por personal laboral los establecerán:",
    ["Las leyes de Función Pública que se dicten en desarrollo del Estatuto.", "Los convenios colectivos.", "Las relaciones de puestos de trabajo de cada departamento.", "El Estatuto de los Trabajadores."],
    "Art. 11.2 TREBEP, respetando en todo caso el art. 9.2.", "Las leyes de Función Pública que se dicten en desarrollo de este Estatuto establecerán los criterios para la determinación de los puestos de trabajo que pueden ser desempeñados por personal laboral")
T.q("TREBEP", "Artículo 11", "Preceptos del TREBEP", "Según el artículo 11.3 del TREBEP, la selección del personal laboral temporal se regirá, además de por los principios de igualdad, mérito y capacidad, por el principio de:",
    ["Celeridad.", "Libre designación.", "Antigüedad.", "Discrecionalidad técnica."],
    "Art. 11.3 TREBEP.", "En el caso del personal laboral temporal se regirá igualmente por el principio de celeridad")
T.q("L30", "Artículo quince", "Puestos", "Según el artículo 15.1 c) de la Ley 30/1984, con carácter general, los puestos de trabajo de la Administración del Estado y de sus Organismos Autónomos serán desempeñados por:",
    ["Funcionarios públicos.", "Personal laboral fijo.", "Funcionarios públicos o personal laboral, indistintamente.", "Personal laboral, salvo los reservados a Cuerpos o Escalas."],
    "Art. 15.1 c) Ley 30/1984: la regla es el funcionario; el personal laboral, la excepción.", "Con carácter general, los puestos de trabajo de la Administración del Estado y de sus Organismos Autónomos así como los de las Entidades Gestoras y Servicios Comunes de la Seguridad Social, serán desempeñados por funcionarios públicos")
T.q("L30", "Artículo quince", "Puestos", "Según el artículo 15.1 c) de la Ley 30/1984, ¿cuál de los siguientes puestos de la Administración del Estado puede desempeñarse por personal laboral?",
    ["Los de vigilancia, custodia, porteo y otros análogos.", "Los que impliquen el ejercicio de potestades públicas.", "Los de jefatura de las unidades administrativas.", "Todos los puestos de los servicios centrales."],
    "Art. 15.1 c) Ley 30/1984, segundo guion.", "los puestos cuyas actividades sean propias de oficios, así como los de vigilancia, custodia, porteo y otros análogos")
T.q("L30", "Artículo quince", "Puestos", "Según el artículo 15.1 f) de la Ley 30/1984, la formalización de nuevos contratos de personal laboral fijo requerirá:",
    ["Que los correspondientes puestos figuren detallados en las relaciones de puestos de trabajo.", "La autorización previa del Consejo de Ministros.", "El informe favorable de la Comisión Paritaria.", "Que los puestos figuren en el convenio colectivo."],
    "Art. 15.1 f) Ley 30/1984.", "la formalización de nuevos contratos de personal laboral fijo, requerirán que los correspondientes puestos figuren detallados en las respectivas relaciones")
T.q("RDL6", "Artículo 109", "Puestos", "Según el artículo 109.1 del Real Decreto-ley 6/2023, las relaciones de puestos de trabajo de la Administración del Estado han de incluir:",
    ["Todos los puestos de trabajo de naturaleza funcionarial, laboral y eventual existentes.", "Solo los puestos de naturaleza funcionarial.", "Los puestos funcionariales y eventuales; los laborales, en el convenio colectivo.", "Solo los puestos vacantes."],
    "Art. 109.1 RDL 6/2023.", "todos los puestos de trabajo de naturaleza funcionarial, laboral y eventual existentes")
T.q("TREBEP", "Artículo 19", "Preceptos del TREBEP", "Según el artículo 19.2 del TREBEP, la carrera profesional y la promoción del personal laboral se harán efectivas a través de los procedimientos previstos en:",
    ["El Estatuto de los Trabajadores o los convenios colectivos.", "El Estatuto Básico del Empleado Público.", "Las leyes de Función Pública.", "Los reglamentos de provisión de puestos de trabajo."],
    "Art. 19.2 TREBEP.", "a través de los procedimientos previstos en el Estatuto de los Trabajadores o en los convenios colectivos")
T.q("TREBEP", "Artículo 27", "Preceptos del TREBEP", "Según el artículo 27 del TREBEP, las retribuciones del personal laboral se determinarán de acuerdo con la legislación laboral, el convenio colectivo aplicable y el contrato de trabajo, respetando en todo caso lo establecido en:",
    ["El artículo 21 del Estatuto.", "El artículo 22 del Estatuto de los Trabajadores.", "El artículo 7 del Estatuto.", "El artículo 51 del Estatuto."],
    "Art. 27 TREBEP.", "respetando en todo caso lo establecido en el artículo 21 del presente Estatuto")
T.q("TREBEP", "Artículo 77", "Preceptos del TREBEP", "Según el artículo 77 del TREBEP, el personal laboral se clasificará:",
    ["De conformidad con la legislación laboral.", "En los subgrupos A1, A2, C1 y C2.", "De conformidad con las leyes de Función Pública.", "Según el nivel de complemento de destino."],
    "Art. 77 TREBEP.", "El personal laboral se clasificará de conformidad con la legislación laboral")
T.q("TREBEP", "Artículo 83", "Preceptos del TREBEP", "Según el artículo 83 del TREBEP, la provisión de puestos y movilidad del personal laboral se realizará conforme a los convenios colectivos aplicables y, en su defecto:",
    ["Por el sistema de provisión de puestos y movilidad del personal funcionario de carrera.", "Por el Estatuto de los Trabajadores exclusivamente.", "Por libre designación.", "Por acuerdo de la Comisión Paritaria."],
    "Art. 83 TREBEP.", "en su defecto por el sistema de provisión de puestos y movilidad del personal funcionario de carrera")
T.q("TREBEP", "Artículo 92", "Preceptos del TREBEP", "Según el artículo 92 del TREBEP, las situaciones del personal laboral se regirán:",
    ["Por el Estatuto de los Trabajadores y por los Convenios Colectivos que les sean de aplicación.", "Por el capítulo de situaciones del Estatuto Básico, en todo caso.", "Por el Reglamento de situaciones administrativas de los funcionarios.", "Por el contrato de trabajo exclusivamente."],
    "Art. 92 TREBEP; los convenios pueden extenderle el capítulo del TREBEP en lo compatible con el ET.", "El personal laboral se regirá por el Estatuto de los Trabajadores y por los Convenios Colectivos que les sean de aplicación")
T.q("TREBEP", "Artículo 93", "Preceptos del TREBEP", "Según el artículo 93.4 del TREBEP, el régimen disciplinario del personal laboral se regirá, en lo no previsto en el título VII del Estatuto, por:",
    ["La legislación laboral.", "El Reglamento de Régimen Disciplinario de los funcionarios.", "La Ley 39/2015.", "El contrato de trabajo."],
    "Art. 93.4 TREBEP.", "El régimen disciplinario del personal laboral se regirá, en lo no previsto en el presente título, por la legislación laboral")
T.q("CONV", "Artículo 1", "Ámbito del Convenio", "Según el artículo 1.1 del IV Convenio Único, este será de aplicación al personal laboral de:",
    ["La Administración General del Estado y sus organismos autónomos.", "Todas las Administraciones Públicas.", "La Administración General del Estado y todas las entidades del sector público estatal.", "La Administración General del Estado, excluidos sus organismos autónomos."],
    "Art. 1.1 IV Convenio Único.", "será de aplicación al personal laboral de la Administración General del Estado y sus organismos autónomos")
T.q("CONV", "Artículo 1", "Ámbito del Convenio", "Según el artículo 1.2 del IV Convenio Único, se incluye en su ámbito de aplicación el personal laboral que preste servicios en:",
    ["La Administración de Justicia no transferida.", "La Administración de Justicia transferida a las comunidades autónomas.", "Las entidades del sector público no citadas en el artículo 1.", "El exterior."],
    "Art. 1.2 a) IV Convenio Único. Las entidades no citadas y el exterior están excluidos (art. 2 a y g).", "La Administración de Justicia no transferida")
T.q("CONV", "Artículo 1", "Ámbito del Convenio", "Según el artículo 1.3 del IV Convenio Único, la inclusión en su ámbito de aplicación de nuevo personal exigirá:",
    ["Que la mayoría del colectivo afectado manifieste su conformidad a la integración.", "La unanimidad del colectivo afectado.", "Un acuerdo del Consejo de Ministros.", "Una modificación del Convenio aprobada por la Comisión Negociadora."],
    "Art. 1.3 IV Convenio Único; la propuesta se eleva a la Comisión Paritaria para su aprobación.", "exigirá que la mayoría del colectivo afectado manifieste su conformidad a la integración")
T.q("CONV", "Artículo 1", "Ámbito del Convenio", "Según el artículo 1.3 del IV Convenio Único, la propuesta de inclusión de nuevo personal se elevará para su aprobación a:",
    ["La Comisión Paritaria.", "La Comisión Negociadora.", "La Dirección General de la Función Pública.", "La Mesa General de Negociación de la Administración General del Estado."],
    "Art. 1.3 IV Convenio Único: se trata en la Subcomisión Paritaria y se eleva a la Comisión Paritaria, previo informe favorable de dos Direcciones Generales.", "se elevará a la Comisión Paritaria para su aprobación")
T.q("CONV", "Artículo 2", "Ámbito del Convenio", "Según el artículo 2 del IV Convenio Único, queda excluido de su ámbito de aplicación:",
    ["El personal de alta dirección contemplado en el artículo 2.1.a) del Estatuto de los Trabajadores.", "El personal laboral del Consejo de Seguridad Nuclear.", "El personal laboral de los organismos autónomos.", "El personal laboral de la Agencia Española de Protección de Datos."],
    "Art. 2 c) IV Convenio Único. El CSN, la AEPD y los organismos autónomos están incluidos (art. 1).", "El personal de alta dirección contemplado en el artículo 2.1.a) del texto refundido de la Ley del Estatuto de los Trabajadores")
T.q("CONV", "Artículo 2", "Ámbito del Convenio", "Según el artículo 2 f) del IV Convenio Único, las contrataciones de personal formalizadas expresamente fuera de Convenio se realizarán:",
    ["De forma excepcional, e informando a la Comisión Paritaria.", "Libremente, sin necesidad de informar a nadie.", "Con autorización previa de la Comisión Negociadora.", "Previo informe favorable de la Subcomisión Paritaria."],
    "Art. 2 f) IV Convenio Único.", "Estas contrataciones se realizarán de forma excepcional, e informando a la Comisión Paritaria")
T.q("CONV", "Artículo 3", "Ámbito del Convenio", "Según el artículo 3.3 del IV Convenio Único, de no efectuarse denuncia expresa, el Convenio:",
    ["Se prorrogará automáticamente por períodos anuales.", "Perderá su vigencia el 31 de diciembre de 2021.", "Se prorrogará automáticamente por períodos bienales.", "Se mantendrá solo en su contenido normativo."],
    "Art. 3.3 IV Convenio Único.", "el Convenio se prorrogará automáticamente por períodos anuales")
T.q("CONV", "Artículo 3", "Ámbito del Convenio", "Según el artículo 3.2 del IV Convenio Único, el Convenio podrá ser denunciado por cualquiera de las partes:",
    ["Dentro de los dos meses inmediatos anteriores a la terminación de su vigencia.", "Dentro del mes inmediato anterior a la terminación de su vigencia.", "Dentro de los tres meses inmediatos anteriores a la terminación de su vigencia.", "En cualquier momento de su vigencia."],
    "Art. 3.2 IV Convenio Único.", "dentro de los dos meses inmediatos anteriores a la terminación de su vigencia")
T.q("CONV", "Artículo 4", "Ámbito del Convenio", "Según el artículo 4.1 del IV Convenio Único, el Convenio, a efectos de su aplicación:",
    ["Forma un todo orgánico e indivisible y será considerado globalmente.", "Se aplicará por títulos independientes.", "Se aplicará de forma supletoria al III Convenio único.", "Se aplicará cláusula a cláusula según la condición más favorable."],
    "Art. 4.1 IV Convenio Único.", "forma un todo orgánico e indivisible y, a efectos de su aplicación, será considerado globalmente")
T.q("CONV", "Artículo 124", "Ámbito del Convenio", "Según el artículo 124 del IV Convenio Único, en todo lo no previsto en el Convenio se estará a lo dispuesto en:",
    ["El Estatuto de los Trabajadores y demás disposiciones legales o reglamentarias que resulten de aplicación.", "El Estatuto Básico del Empleado Público, exclusivamente.", "El III Convenio único.", "Los acuerdos de la Mesa General de Negociación."],
    "Art. 124 IV Convenio Único.", "se estará a lo dispuesto en el Estatuto de los Trabajadores y demás disposiciones legales o reglamentarias que resulten de aplicación")
T.q("ET", "Artículo 22", "Clasificación", "Según el artículo 22.1 del Estatuto de los Trabajadores, el sistema de clasificación profesional de los trabajadores se establecerá por medio de:",
    ["Grupos profesionales.", "Categorías profesionales.", "Cuerpos y escalas.", "Niveles de complemento de destino."],
    "Art. 22.1 ET, mediante la negociación colectiva o, en su defecto, acuerdo entre la empresa y los representantes de los trabajadores.", "se establecerá el sistema de clasificación profesional de los trabajadores por medio de grupos profesionales")
T.q("CONV", "Artículo 7", "Clasificación", "Según el artículo 7.1 del IV Convenio Único, el sistema de clasificación se estructura en:",
    ["Grupos profesionales, familias profesionales y/o especialidades.", "Grupos, subgrupos y categorías profesionales.", "Cuerpos, escalas y especialidades.", "Grupos profesionales y niveles retributivos."],
    "Art. 7.1 IV Convenio Único.", "se estructura en grupos profesionales, familias profesionales y/o especialidades")
T.q("CONV", "Artículo 7", "Clasificación", "Según el artículo 7 del IV Convenio Único, ¿qué elemento del sistema de clasificación determina el contenido concreto de la prestación laboral y establece el perfil profesional de cada puesto?",
    ["La especialidad.", "El grupo profesional.", "La familia profesional.", "El nivel de cualificación."],
    "Art. 7.5 IV Convenio Único. El grupo agrupa el contenido «general» (7.3) y la familia, por afinidad de la competencia (7.4).", "La especialidad determina el contenido concreto de la prestación laboral y establece el perfil profesional de cada puesto")
T.q("CONV", "Artículo 8", "Clasificación", "Según el artículo 8.1 del IV Convenio Único, el grupo profesional M3 exige:",
    ["Título clasificado en el Nivel 3 del Marco Español de Cualificaciones para la Educación Superior o equivalentes.", "Título clasificado en el Nivel 2 del Marco Español de Cualificaciones para la Educación Superior o equivalentes.", "Título de Bachiller o Técnico o equivalentes.", "Título clasificado en el Nivel 1 del Marco Español de Cualificaciones para la Educación Superior o equivalentes."],
    "Art. 8.1 a) IV Convenio Único.", "Grupo profesional M3: Título clasificado en el Nivel 3 del Marco Español de Cualificaciones para la Educación Superior o equivalentes")
T.q("CONV", "Artículo 8", "Clasificación", "Según el artículo 8.1 del IV Convenio Único, el grupo profesional E1 exige:",
    ["Título de Graduado en Educación Secundaria Obligatoria o Título Profesional Básico o equivalentes.", "Título de Bachiller o Técnico o equivalentes.", "Sin titulación prevista en el sistema educativo.", "Título clasificado en el Nivel 1 del Marco Español de Cualificaciones para la Educación Superior o equivalentes."],
    "Art. 8.1 e) IV Convenio Único.", "Grupo profesional E1: Título de Graduado en Educación Secundaria Obligatoria o Título Profesional Básico o equivalentes")
T.q("CONV", "Artículo 8", "Clasificación", "Según el artículo 8.1 del IV Convenio Único, ¿qué grupo profesional no exige titulación prevista en el sistema educativo?",
    ["E0.", "E1.", "E2.", "M1."],
    "Art. 8.1 f) IV Convenio Único.", "Grupo profesional E0: Sin titulación prevista en el sistema educativo")
T.q("CONV", "Artículo 8", "Clasificación", "Según el artículo 8.3 del IV Convenio Único, cuando se requiera el título de Doctor para el desempeño de un puesto, se adecuarán sus características retributivas previa aprobación por:",
    ["La Comisión Paritaria.", "La Comisión Negociadora.", "La Comisión Ejecutiva de la Comisión Interministerial de Retribuciones.", "La Subcomisión Paritaria del departamento."],
    "Art. 8.3 IV Convenio Único (y art. 15 r).", "previa aprobación por la Comisión Paritaria")
T.q("CONV", "Artículo 9", "Clasificación", "Según el artículo 9 del IV Convenio Único, las familias profesionales serán las definidas como tal por:",
    ["La autoridad competente dentro del Sistema Nacional de Cualificaciones y Formación Profesional.", "La Comisión Paritaria del Convenio.", "La Comisión Negociadora del Convenio.", "Cada Subcomisión Paritaria en su ámbito."],
    "Art. 9 IV Convenio Único; la Administración determina las que coinciden con sus necesidades organizativas.", "Las familias profesionales serán las definidas como tal por la autoridad competente dentro del Sistema Nacional de Cualificaciones y Formación Profesional")
T.q("CONV", "Artículo 10", "Clasificación", "Según el artículo 10.2 del IV Convenio Único, para los grupos M3 y M2 la especialidad determinará:",
    ["La titulación o titulaciones universitarias exigidas para el ingreso.", "El título de Formación Profesional de Grado Superior exigido.", "La cualificación profesional de Nivel 3 exigida.", "La familia profesional del puesto."],
    "Art. 10.2 IV Convenio Único. El Grado Superior y el Nivel 3 corresponden al grupo M1 (10.3).", "Para los Grupos M3 y M2 la especialidad determinará la titulación o titulaciones universitarias exigidas para el ingreso")
T.q("CONV", "Artículo 10", "Clasificación", "Según el artículo 10.4 c) del IV Convenio Único, para el resto de puestos del grupo E2, la creación de la especialidad se llevará a cabo por:",
    ["La Comisión Ejecutiva de la Comisión Interministerial de Retribuciones, previa aprobación por la Comisión Paritaria.", "La Comisión Paritaria, previo informe de la Comisión Ejecutiva de la Comisión Interministerial de Retribuciones.", "La Comisión Negociadora, a propuesta de la Subcomisión Paritaria.", "La Dirección General de la Función Pública."],
    "Art. 10.4 c) IV Convenio Único.", "la creación de la especialidad se llevará a cabo por la Comisión Ejecutiva de la Comisión Interministerial de Retribuciones, previa aprobación por la Comisión Paritaria")
T.q("CONV", "Artículo 11", "Órganos", "Según el artículo 11.2 del IV Convenio Único, la modificación de la clasificación profesional de determinados colectivos se aprueba a propuesta de:",
    ["La Subcomisión Paritaria correspondiente a la que pertenezca ese colectivo.", "La Comisión Paritaria.", "La Dirección General de la Función Pública.", "La mayoría del colectivo afectado."],
    "Art. 11.2 IV Convenio Único: aprueba la Comisión Negociadora, a propuesta de la Subcomisión Paritaria y previo informe favorable de la Comisión Paritaria.", "a propuesta de la correspondiente Subcomisión Paritaria correspondiente a la que pertenezca ese colectivo")
T.q("CONV", "Artículo 12", "Órganos", "Según el artículo 12.3 del IV Convenio Único, el órgano máximo de interpretación, vigilancia, seguimiento, estudio y aplicación de lo pactado es:",
    ["La Comisión Paritaria.", "La Comisión Negociadora.", "La Subcomisión Paritaria de cada Departamento.", "La Dirección General de Trabajo."],
    "Art. 12.3 IV Convenio Único.", "La Comisión Paritaria es el órgano máximo de interpretación, vigilancia, seguimiento, estudio y aplicación de lo pactado")
T.q("CONV", "Artículo 16", "Órganos", "Según el artículo 16.2 del IV Convenio Único, la Comisión Paritaria se reunirá con carácter ordinario:",
    ["Al menos una vez al mes.", "Al menos una vez al trimestre.", "Al menos una vez a la semana.", "Al menos una vez al semestre."],
    "Art. 16.2 IV Convenio Único.", "La Comisión Paritaria se reunirá con carácter ordinario al menos una vez al mes")
T.q("CONV", "Artículo 19", "Órganos", "Según el artículo 19.2 del IV Convenio Único, el número de representantes de cada una de las partes en las Subcomisiones Paritarias:",
    ["No podrá ser superior a quince.", "No podrá ser inferior a quince.", "Será de siete.", "Será de treinta."],
    "Art. 19.2 IV Convenio Único.", "cuyo número, por cada una de las partes, no podrá ser superior a quince")
T.real("L", 74, "Clasificación"); T.real("P", 79, "Clasificación"); T.real("P", 80, "Órganos"); T.real("P", 104, "Órganos"); T.real("X", 82, "Ámbito del Convenio")

# Flashcards
for q_, a_, cat in [
  ("¿Qué es el personal laboral? (TREBEP, art. 11.1)", "El que presta servicios retribuidos por las Administraciones Públicas en virtud de contrato de trabajo formalizado por escrito, en cualquiera de las modalidades de la legislación laboral.", "Concepto"),
  ("Modalidades del personal laboral (arts. 8.2 c y 11.1)", "Fijo, por tiempo indefinido o temporal, en función de la duración del contrato.", "Concepto"),
  ("¿Por qué normas se rige el personal laboral de las Administraciones? (art. 7)", "Por la legislación laboral, por las demás normas convencionalmente aplicables y por los preceptos del TREBEP que así lo dispongan.", "Régimen jurídico"),
  ("¿Qué permisos del personal laboral se rigen por el TREBEP y no por el ET? (art. 7)", "Los de nacimiento, adopción, del progenitor diferente de la madre biológica, de lactancia y parental.", "Régimen jurídico"),
  ("¿Qué funciones corresponden exclusivamente a los funcionarios? (art. 9.2)", "Las que impliquen la participación directa o indirecta en el ejercicio de las potestades públicas o en la salvaguardia de los intereses generales.", "Puestos"),
  ("¿Quién fija los criterios de los puestos que puede ocupar el personal laboral? (art. 11.2)", "Las leyes de Función Pública que se dicten en desarrollo del TREBEP, respetando el art. 9.2.", "Puestos"),
  ("Regla general de los puestos de la AGE (Ley 30/1984, art. 15.1 c)", "Son desempeñados por funcionarios públicos; el personal laboral solo en los puestos exceptuados (no permanentes, oficios, vigilancia, custodia, porteo, instrumentales, técnicos sin Cuerpo, extranjero, auxiliares de apoyo administrativo).", "Puestos"),
  ("¿Qué exige la formalización de nuevos contratos de personal laboral fijo? (Ley 30/1984, art. 15.1 f)", "Que los puestos figuren detallados en las relaciones de puestos de trabajo.", "Puestos"),
  ("Carrera y promoción del personal laboral (art. 19)", "Tiene derecho a la promoción profesional; se hace efectiva por los procedimientos del Estatuto de los Trabajadores o de los convenios colectivos.", "Preceptos del TREBEP"),
  ("Provisión y movilidad del personal laboral (art. 83)", "Según los convenios colectivos y, en su defecto, por el sistema de provisión y movilidad del personal funcionario de carrera.", "Preceptos del TREBEP"),
  ("Clasificación del personal laboral (art. 77)", "De conformidad con la legislación laboral.", "Preceptos del TREBEP"),
  ("Ámbito del IV Convenio Único (art. 1.1)", "Personal laboral de la AGE y sus organismos autónomos.", "Ámbito del Convenio"),
  ("Ámbitos añadidos al Convenio (art. 1.2)", "Administración de Justicia no transferida; Administración de la Seguridad Social; Consejo de Seguridad Nuclear; AEPD; Museo Nacional Centro de Arte Reina Sofía; Trabajo Penitenciario y Formación para el Empleo.", "Ámbito del Convenio"),
  ("Exclusiones del Convenio que más caen (art. 2)", "Personal laboral en el exterior; de otros convenios de la AGE; de alta dirección; contratado fuera de Convenio; de entidades del sector público no citadas en el art. 1.", "Ámbito del Convenio"),
  ("Vigencia del IV Convenio Único (art. 3)", "Hasta el 31-12-2021; denuncia en los dos meses anteriores; sin denuncia, prórroga automática por períodos anuales; denunciado, se mantiene todo su contenido.", "Ámbito del Convenio"),
  ("Derecho supletorio del Convenio (art. 124)", "El Estatuto de los Trabajadores y demás disposiciones legales o reglamentarias aplicables.", "Ámbito del Convenio"),
  ("Estructura del sistema de clasificación (art. 7.1)", "Grupos profesionales, familias profesionales y/o especialidades.", "Clasificación"),
  ("Grupos profesionales y titulación (art. 8.1)", "M3, M2 y M1: niveles 3, 2 y 1 del MECES; E2: Bachiller o Técnico; E1: Graduado en ESO o Título Profesional Básico; E0: sin titulación.", "Clasificación"),
  ("¿Quién aprueba la creación o modificación de especialidades? (art. 15 i)", "La Comisión Paritaria.", "Órganos"),
  ("Modificación de la clasificación de un colectivo (art. 11.2)", "La aprueba la Comisión Negociadora, a propuesta de la Subcomisión Paritaria y previo informe favorable de la Comisión Paritaria.", "Órganos"),
  ("Reuniones de la Comisión Paritaria (art. 16.2)", "Ordinarias, al menos una vez al mes; extraordinarias, cuando lo soliciten al menos siete personas de la parte social o de la Administración.", "Órganos"),
  ("Personal del anexo II del Convenio", "Conserva una clasificación propia (G1 a G4) y no se le aplican los títulos III y VI (art. 8.4 y anexo II).", "Clasificación"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Personal laboral", "Empleado público que presta servicios retribuidos a las Administraciones en virtud de contrato de trabajo formalizado por escrito; fijo, por tiempo indefinido o temporal (TREBEP, art. 11.1).", "s1", "Concepto")
T.glos("Normas convencionalmente aplicables", "Las pactadas en la negociación colectiva (convenios); una de las tres fuentes del régimen del personal laboral (TREBEP, art. 7).", "s2", "Régimen jurídico")
T.glos("Potestades públicas", "Funciones cuyo ejercicio corresponde exclusivamente a los funcionarios públicos (TREBEP, art. 9.2); límite a los puestos laborales (art. 11.2).", "s3", "Puestos")
T.glos("Relación de puestos de trabajo", "Instrumento técnico de ordenación del personal; incluye los puestos funcionariales, laborales y eventuales (Ley 30/1984, art. 15.1; RDL 6/2023, art. 109.1).", "s3", "Puestos")
T.glos("IV Convenio Único", "IV Convenio colectivo único para el personal laboral de la Administración General del Estado, registrado y publicado por Resolución de 13 de mayo de 2019 de la Dirección General de Trabajo.", "s5", "Ámbito del Convenio")
T.glos("Personal fuera de Convenio", "Personal cuya relación se formaliza expresamente fuera del Convenio; contratación excepcional, informando a la Comisión Paritaria (art. 2 f).", "s6", "Ámbito del Convenio")
T.glos("Denuncia del Convenio", "Comunicación de cualquiera de las partes, en los dos meses anteriores al fin de la vigencia; sin ella, prórroga anual automática (art. 3).", "s7", "Ámbito del Convenio")
T.glos("Grupo profesional", "Agrupa unitariamente las aptitudes profesionales, las titulaciones y el contenido general de la prestación laboral (Convenio, art. 7.3; ET, art. 22.2).", "s9", "Clasificación")
T.glos("Familia profesional", "Agrupa titulaciones, cualificaciones, profesiones, oficios y ocupaciones por afinidad de la competencia profesional (art. 7.4); las define la autoridad competente del Sistema Nacional de Cualificaciones (art. 9).", "s9", "Clasificación")
T.glos("Especialidad", "Determina el contenido concreto de la prestación laboral y el perfil profesional de cada puesto (art. 7.5); todo puesto tiene una (art. 10.1).", "s10", "Clasificación")
T.glos("Comisión Negociadora", "Órgano encargado de la negociación en el marco del Convenio único (art. 12.2); aprueba la modificación de la clasificación de un colectivo (art. 11.2).", "s11", "Órganos")
T.glos("Comisión Paritaria", "Órgano máximo de interpretación, vigilancia, seguimiento, estudio y aplicación del Convenio (art. 12.3); quince personas por cada parte (art. 14.2).", "s11", "Órganos")
T.glos("Subcomisión Paritaria", "Órgano delegado de la Comisión Paritaria en cada Departamento y en otros ámbitos (art. 19.1).", "s11", "Órganos")
T.glos("Encuadramiento", "Integración del personal del III Convenio único en los grupos del IV Convenio, según su anexo I (disposición adicional primera).", "s12", "Clasificación")

# Cronología (fechas de los metadatos del BOE)
T.hito("1984", "Ley 30/1984, de 2 de agosto, de medidas para la reforma de la Función Pública (BOE de 3-8-1984)", "Art. 15.1: puestos de la Administración del Estado que pueden desempeñarse por personal laboral", "normativo", "s3")
T.hito("2015", "Real Decreto Legislativo 2/2015, de 23 de octubre, texto refundido de la Ley del Estatuto de los Trabajadores (BOE de 24-10-2015)", "Arts. 1, 3 y 22: ámbito, fuentes y clasificación profesional", "normativo", "s8")
T.hito("2015", "Real Decreto Legislativo 5/2015, de 30 de octubre, texto refundido de la Ley del Estatuto Básico del Empleado Público (BOE de 31-10-2015)", "Arts. 7 y 11: régimen y concepto del personal laboral", "normativo", "s2")
T.hito("2019", "Resolución de 13 de mayo de 2019, de la Dirección General de Trabajo, por la que se registra y publica el IV Convenio colectivo único para el personal laboral de la AGE (BOE de 17-5-2019)", "Entra en vigor el día siguiente de su publicación; efectos económicos desde el 1-1-2019 (art. 3.1)", "normativo", "s7")
T.hito("2023", "Real Decreto-ley 6/2023, de 19 de diciembre (BOE de 20-12-2023)", "Art. 109: relaciones de puestos de trabajo de la Administración del Estado, con los puestos laborales", "normativo", "s3")

T.publicar()
