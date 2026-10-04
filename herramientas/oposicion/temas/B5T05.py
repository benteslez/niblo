# -*- coding: utf-8 -*-
"""Tema V.5 (B5T05): Situaciones administrativas del personal al servicio de las
administraciones públicas. Incompatibilidades.
Método del I.2: mapa → bloques (I a IV) con guía; cada artículo, texto literal del
BOE + ficha de casillas fijas; cierre 1 (preguntas oficiales) y cierre 2 (repaso).
Normas (textos consolidados del BOE): TREBEP (RDLeg 5/2015), arts. 85 a 92, disposición
derogatoria única y disposición final cuarta; Real Decreto 365/1995 (Reglamento de
Situaciones Administrativas de los Funcionarios Civiles de la AGE), en lo que no se opone
al TREBEP; Ley 53/1984, de Incompatibilidades; Real Decreto 598/1985."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO.update({"RD365": "RD 365/1995", "RD598": "RD 598/1985", "L53": "Ley 53/1984"})
R598 = lambda n: f"Artículo {n} (RD 598/1985)"

T = Tema("B5T05",
  "Cuatro preguntas: I. En qué situaciones puede estar el personal (TREBEP, arts. 85 y 92 y disposición final cuarta.2; RD 365/1995, arts. 1 y 2) · II. Cuándo se está en servicio activo, en servicios especiales o en servicio en otras Administraciones (TREBEP, arts. 86 a 88; RD 365/1995) · III. Excedencias, suspensión de funciones y reingreso (TREBEP, arts. 89 a 91; RD 365/1995) · IV. Incompatibilidades: actividades públicas y privadas (Ley 53/1984; RD 598/1985). Cada artículo: texto literal del BOE y ficha.",
  ["Situaciones administrativas", "Art. 85 TREBEP", "Servicio activo", "Servicios especiales", "Servicio en otras AA. PP.", "Excedencia", "Interés particular", "Cuidado de familiares", "Suspensión de funciones", "RD 365/1995", "Incompatibilidades", "Ley 53/1984", "Segundo puesto", "Actividades privadas", "RD 598/1985"])

# =============================================================================
T.ap("s0", "Mapa del tema: cuatro preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque V, tema 5):
> Situaciones administrativas del personal al servicio de las administraciones públicas. Incompatibilidades.

### El hilo conductor

El epígrafe se lee como **cuatro preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | TREBEP | Otras normas |
|---|---|---|---|
| **I** | ¿En qué situaciones puede hallarse el personal? | Arts. 85 y 92; disposición final cuarta.2 | RD 365/1995, arts. 1 y 2 |
| **II** | ¿Cuándo se está en servicio activo, en servicios especiales o en servicio en otras Administraciones? | Arts. 86, 87 y 88 | RD 365/1995, arts. 3, 6, 9 y 11 |
| **III** | ¿Cuándo se deja de prestar servicio? Excedencias, suspensión y reingreso | Arts. 89, 90 y 91 | RD 365/1995, arts. 12, 13, 15, 18, 19, 21, 22 y 23 |
| **IV** | ¿Qué otras actividades puede ejercer el personal? Incompatibilidades | — | Ley 53/1984, arts. 1 a 16 y 18 a 20; RD 598/1985, arts. 5, 6, 8, 9, 11, 14 y 17 |

!> **La idea que une los cuatro bloques:** el funcionario de carrera está siempre en **una** situación administrativa (I). Mientras presta servicios, está en **servicio activo**, en **servicios especiales** o en **servicio en otras Administraciones** (II). Si deja de prestarlos, está en **excedencia** o en **suspensión de funciones**, y vuelve por el **reingreso** (III). Y, esté donde esté, la regla general es la **incompatibilidad**: un solo puesto en el sector público y actividades privadas solo con reconocimiento previo (IV).

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen; en los derechos, Titulares · Contenido · Límites · Protección · ⚠ Ojo en el examen).
- El **TREBEP** es la norma básica. Del **RD 365/1995** (reglamento de la AGE, de 1995) se citan solo los artículos que no contradicen el TREBEP, porque sigue en vigor en tanto no se oponga a él (→ I.3.3).
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- Fronteras: la comisión de servicios y la provisión de puestos son del tema V.4; los permisos y el régimen disciplinario, del tema V.2; las retribuciones, del tema V.6.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿En qué situaciones puede hallarse el personal? (TREBEP, arts. 85 y 92 y disposición final cuarta.2; RD 365/1995, arts. 1 y 2)", donde(
  "Primera pregunta del tema. Antes de estudiar cada situación hay que saber **cuáles hay**: las cinco del TREBEP para los funcionarios de carrera, la remisión del personal laboral al Estatuto de los Trabajadores y la lista del reglamento de la Administración General del Estado.",
  ["1 Las situaciones de los funcionarios de carrera (art. 85)", "2 Situaciones del personal laboral (art. 92)", "3 El Reglamento de situaciones de la AGE (RD 365/1995) y su vigencia"]))

T.ap("s1", "I.1 Las situaciones de los funcionarios de carrera (TREBEP, art. 85)", f"""
{unidad("1.1 Las cinco situaciones (art. 85.1)",
  lit("TREBEP", "a85", ["a) Servicio activo.", "b) Servicios especiales.", "c) Servicio en otras Administraciones Públicas.", "d) Excedencia.", "e) Suspensión de funciones."], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Lista básica de situaciones administrativas de los funcionarios de carrera",
         c("TREBEP", "a85", "Los funcionarios de carrera"),
         ["::Siempre en una de estas cinco:", "Servicio activo (→ II.1)", "Servicios especiales (→ II.2)", "Servicio en otras Administraciones Públicas (→ II.3)", "Excedencia (→ III.1)", "Suspensión de funciones (→ III.6)"],
         "—",
         "Son **cinco**. La **comisión de servicios** no es una situación: es una forma de provisión (tema V.4) y quien está en ella sigue en **servicio activo** (→ II.1.2). Cayó dos veces en 2025 (→ Cierre 1)."))}

{unidad("1.2 Otras situaciones que pueden crear las leyes de función pública (art. 85.2)",
  lit("TREBEP", "a85", ["podrán regular otras situaciones administrativas", "imposibilidad transitoria de asignar un puesto de trabajo", "garantías de índole retributiva"], solo=[7, 8, 9, 10]),
  fichab("Habilitación para añadir situaciones",
         f"{c('TREBEP', 'a85', 'Las leyes de Función Pública que se dicten en desarrollo de este Estatuto')}",
         ["::Cuando concurra, entre otras, alguna de estas circunstancias:", "Razones organizativas, de reestructuración interna o exceso de personal (imposibilidad transitoria de asignar puesto o conveniencia de incentivar el cese en el servicio activo)", "Acceso a otros cuerpos o escalas sin situación prevista, o paso a organismos o entidades del sector público en régimen distinto al de funcionario de carrera"],
         "—",
         "La lista del 85.1 **no es cerrada**: las leyes «**podrán** regular otras situaciones». Las situaciones propias del reglamento de la AGE (→ III.5) son anteriores al TREBEP y siguen vigentes en tanto no se opongan a él (→ I.3.3)."))}
""", 2)

T.ap("s2", "I.2 Situaciones del personal laboral (TREBEP, art. 92)", f"""
{unidad("2.1 Remisión al Estatuto de los Trabajadores y a los convenios (art. 92)",
  lit("TREBEP", "a92", ["por el Estatuto de los Trabajadores y por los Convenios Colectivos", "en lo que resulte compatible con el Estatuto de los Trabajadores"]),
  fichab("Régimen de las situaciones del personal laboral",
         "El **personal laboral** al servicio de las Administraciones Públicas",
         f"Se rige por el Estatuto de los Trabajadores y por los convenios colectivos; los convenios {c('TREBEP', 'a92', 'podrán determinar la aplicación de este capítulo')}",
         "—",
         "El capítulo de situaciones del TREBEP es de los **funcionarios**; al laboral solo se le aplica si **su convenio** lo dice y en lo **compatible** con el Estatuto de los Trabajadores. Personal laboral: tema V.7."))}
""", 2)

T.ap("s3", "I.3 El Reglamento de situaciones de la AGE (RD 365/1995) y su vigencia", f"""
{unidad("3.1 Ámbito de aplicación (RD 365/1995, art. 1.1)",
  lit("RD365", "a1", ["funcionarios de la Administración general del Estado y sus Organismos autónomos"], solo=[1]),
  fichab("A quién se aplica el Reglamento",
         c("RD365", "a1", "los funcionarios de la Administración general del Estado y sus Organismos autónomos"),
         "Los comprendidos en el ámbito de la Ley 30/1984",
         "—",
         "Es un reglamento **de la AGE** (no básico). Por eso recoge situaciones que el TREBEP no nombra."))}

{unidad("3.2 Las situaciones del Reglamento (RD 365/1995, art. 2)",
  lit("RD365", "a2", ["d) Expectativa de destino.", "e) Excedencia forzosa.", "g) Excedencia voluntaria por servicios en el sector público.", "j) Excedencia voluntaria incentivada."]),
  fichab("Lista reglamentaria de situaciones en la AGE",
         "Los funcionarios de la AGE",
         ["::Además de las del TREBEP con otros nombres, el Reglamento recoge:", "Expectativa de destino (→ III.5.1)", "Excedencia forzosa (→ III.5.2)", "Excedencia voluntaria por servicios en el sector público (→ III.5.3)", "Excedencia voluntaria incentivada (→ III.5.4)"],
         "—",
         "El Reglamento (1995) llama «**Servicio en Comunidades Autónomas**» a lo que el TREBEP llama «**Servicio en otras Administraciones Públicas**». Si el enunciado cita el TREBEP, la lista es la del art. 85.1 (→ I.1.1)."))}

{unidad("3.3 Qué sigue vigente (TREBEP, disposición final cuarta.2 y disposición derogatoria única)",
  lit("TREBEP", "dfcuaa", ["se mantendrán en vigor en cada Administración Pública las normas vigentes sobre ordenación, planificación y gestión de recursos humanos en tanto no se opongan a lo establecido en este Estatuto"], solo=[3]),
  fichab("Vigencia de las normas anteriores al TREBEP",
         "Cada Administración Pública (en la AGE, el RD 365/1995)",
         f"De la Ley 30/1984 quedan derogados, entre otros, los artículos {c('TREBEP', 'ddunica-2', '29, a excepción del último párrafo de sus apartados 5, 6 y 7')} (disposición derogatoria única, letra b), con el alcance de la disposición final cuarta.2",
         "Hasta que se dicten las leyes de Función Pública y sus reglamentos",
         "El RD 365/1995 sigue aplicándose en la AGE **en tanto no se oponga** al TREBEP. Donde choca (por ejemplo, el cuidado de hijos), manda el **TREBEP**: estos apuntes citan el TREBEP en esos casos."))}

{resumen([
  "Cinco situaciones del funcionario de carrera (TREBEP 85.1): **servicio activo, servicios especiales, servicio en otras AA. PP., excedencia y suspensión de funciones**.",
  "Las leyes de función pública **pueden crear otras** (85.2). La **comisión de servicios no es una situación**.",
  "Personal **laboral**: Estatuto de los Trabajadores y convenios (92).",
  "En la AGE, el **RD 365/1995** añade expectativa de destino, excedencia forzosa, voluntaria por servicios en el sector público e incentivada, y sigue vigente **en tanto no se oponga** al TREBEP."],
  "Siguiente: II. ¿Cuándo se está en servicio activo, en servicios especiales o en servicio en otras Administraciones?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Cuándo se está en servicio activo, en servicios especiales o en servicio en otras Administraciones? (TREBEP, arts. 86 a 88)", donde(
  "Segunda pregunta. Tres situaciones en las que el funcionario **sigue prestando servicios**: en su puesto (servicio activo), en un cargo que la ley protege (servicios especiales) o en otra Administración (servicio en otras Administraciones Públicas).",
  ["1 Servicio activo (art. 86; RD 365/1995, art. 3)", "2 Servicios especiales (art. 87; RD 365/1995, arts. 6 y 9)", "3 Servicio en otras Administraciones Públicas (art. 88; RD 365/1995, art. 11)"]))

T.ap("s4", "II.1 Servicio activo (TREBEP, art. 86; RD 365/1995, art. 3)", f"""
{unidad("1.1 Quién está en servicio activo y qué supone (art. 86)",
  lit("TREBEP", "a86", ["cualquiera que sea la Administración u organismo público o entidad en el que se encuentren destinados y no les corresponda quedar en otra situación", "gozan de todos los derechos inherentes a su condición de funcionarios"]),
  fichab("Situación de quien presta servicios como funcionario",
         "Funcionarios que prestan servicios en su condición de funcionarios públicos",
         f"Situación **residual**: se está en ella si {c('TREBEP', 'a86', 'no les corresponda quedar en otra situación')}",
         "—",
         "Es la única situación con **todos** los derechos y **todos** los deberes. Da igual la Administración o entidad de destino."))}

{unidad("1.2 Supuestos de servicio activo en la AGE (RD 365/1995, art. 3)",
  lit("RD365", "a3", ["Cuando se encuentren en comisión de servicios.", "salvo que desempeñen cargo retribuido y de dedicación exclusiva en las mismas", "durante el plazo posesorio"], solo=[1, 2, 4, 8, 10, 11, 13]),
  fichab("Casos en que el funcionario de la AGE sigue en servicio activo",
         "Funcionarios de la AGE y sus organismos autónomos",
         ["Desempeñan un puesto adscrito según la relación de puestos de trabajo", "Están en **comisión de servicios**", "Son miembros de Corporaciones Locales sin cargo retribuido y de dedicación exclusiva", "Están en el plazo posesorio tras obtener otro puesto", "Están en las dos primeras fases de reasignación de efectivos", "Cesación progresiva de actividades"],
         "—",
         "**Comisión de servicios = servicio activo** (art. 3 c). Concejal sin dedicación exclusiva = servicio activo; con cargo retribuido y dedicación exclusiva = servicios especiales (→ II.2.1)."))}
""", 2)

T.ap("s5", "II.2 Servicios especiales (TREBEP, art. 87; RD 365/1995, arts. 6 y 9)", f"""
{unidad("2.1 Cuándo se declaran (art. 87.1)",
  lit("TREBEP", "a87", ["por periodo determinado superior a seis meses", "si perciben retribuciones periódicas por la realización de la función", "Cuando se desempeñen cargos electivos retribuidos y de dedicación exclusiva", "y no opten por permanecer en la situación de servicio activo", "Cuando sean activados como reservistas voluntarios"], solo=list(range(1, 14))),
  fichab("Situación del funcionario que pasa a desempeñar ciertos cargos o funciones",
         "Funcionarios de carrera; se declara («serán declarados»)",
         ["Miembros del Gobierno y de órganos de gobierno autonómicos, de instituciones de la UE u organizaciones internacionales y altos cargos (a)", "Misión superior a **seis meses** en organismos internacionales o cooperación (b)", "Diputados, Senadores y parlamentarios autonómicos **si perciben retribuciones periódicas** (e)", "Cargos electivos locales **retribuidos y de dedicación exclusiva** (f)", "CGPJ, órganos constitucionales y estatutarios (g y h)", "Personal eventual que **no opte** por el servicio activo (i)", "Asesores de grupos parlamentarios (k) y reservistas voluntarios activados (l)"],
         "Misión internacional: **más de seis meses**",
         "Parlamentarios: solo si **cobran retribuciones periódicas**. Personal eventual: servicios especiales **salvo que opte** por el servicio activo. Doce supuestos (letras a a l)."))}

{unidad("2.2 Retribuciones, cómputo del tiempo y reingreso (art. 87.2 a 4)",
  lit("TREBEP", "a87", ["percibirán las retribuciones del puesto o cargo que desempeñen y no las que les correspondan como funcionarios de carrera", "sin perjuicio del derecho a percibir los trienios", "a efectos de ascensos, reconocimiento de trienios, promoción interna y derechos en el régimen de Seguridad Social", "al menos, a reingresar al servicio activo en la misma localidad"], solo=[14, 15, 16]),
  fichab("Efectos de los servicios especiales",
         "El funcionario en servicios especiales; cada Administración puede añadir derechos según el cargo",
         ["Cobra las retribuciones **del cargo**, no las de funcionario, pero conserva el derecho a los **trienios**", "El tiempo computa para ascensos, trienios, promoción interna y Seguridad Social", "Derecho, **al menos**, a reingresar **en la misma localidad**, con la categoría, nivel o escalón consolidados"],
         "—",
         "Es la situación que **protege la carrera**: computa todo el tiempo. Excepción: quien ejerce el **derecho de transferencia** al régimen de las instituciones europeas."))}

{unidad("2.3 Declaración (RD 365/1995, art. 6.1)",
  lit("RD365", "a6", ["de oficio o a instancia del interesado", "con efectos desde el momento en que se produjo"], solo=[1]),
  fichab("Cómo se pasa a servicios especiales en la AGE",
         "La Administración, de oficio, o el interesado, a instancia propia",
         "Una vez verificado el supuesto que la ocasiona",
         "Efectos: desde el momento en que se produjo el supuesto",
         "Efectos **retroactivos** al hecho que la causa, no a la fecha de la resolución."))}

{unidad("2.4 Reingreso al cesar en el cargo (RD 365/1995, art. 9)",
  lit("RD365", "a9", ["en el plazo de un mes", "en la situación de excedencia voluntaria por interés particular", "hasta su nueva constitución"]),
  fichab("Obligación de pedir el reingreso",
         "Quien pierde la condición que motivó los servicios especiales",
         "Solicitar el reingreso al servicio activo; si no lo pide, pasa a excedencia voluntaria por interés particular",
         f"{c('RD365', 'a9', 'en el plazo de un mes')}",
         "**Un mes**; si no, **excedencia voluntaria por interés particular**. Parlamentarios en disolución o fin de mandato: pueden seguir en servicios especiales **hasta la nueva constitución** (también art. 87.1 e TREBEP)."))}
""", 2)

T.ap("s6", "II.3 Servicio en otras Administraciones Públicas (TREBEP, art. 88; RD 365/1995, art. 11)", f"""
{unidad("3.1 Quién pasa a esta situación (art. 88.1)",
  lit("TREBEP", "a88", ["en virtud de los procesos de transferencias o por los procedimientos de provisión de puestos de trabajo", "en una Administración Pública distinta"], solo=[1]),
  fichab("Situación del funcionario destinado en otra Administración",
         "Funcionarios de carrera que obtienen destino en una Administración Pública distinta",
         "Por **transferencias** o por **procedimientos de provisión** de puestos",
         "—",
         "Se mantiene aunque la Administración de destino los **integre** como personal propio por disposición legal."))}

{unidad("3.2 Funcionarios transferidos a las comunidades autónomas (art. 88.2)",
  lit("TREBEP", "a88", ["hallándose en la situación de servicio activo en la Función Pública de la comunidad autónoma en la que se integran", "como si se hallaran en servicio activo"], solo=[2, 3, 4, 5]),
  fichab("Integración de los funcionarios transferidos",
         "Funcionarios transferidos a las comunidades autónomas",
         ["En la comunidad autónoma: **servicio activo**, integrados plenamente", "Se respeta su Grupo o Subgrupo y sus derechos económicos de carrera", "En la Administración de origen mantienen todos sus derechos **como si** estuvieran en servicio activo"],
         "—",
         "Doble posición: **servicio activo** en la comunidad autónoma y **servicio en otras AA. PP.** en la de origen. Igualdad entre todos los funcionarios propios de la comunidad."))}

{unidad("3.3 Destinados por provisión: régimen y reingreso (art. 88.3 y 4)",
  lit("TREBEP", "a88", ["se rigen por la legislación de la Administración en la que estén destinados de forma efectiva", "se les computará como de servicio activo en su cuerpo o escala de origen"], solo=[6, 7]),
  fichab("Régimen de quien obtuvo puesto en otra Administración por provisión",
         "Funcionarios destinados en otra Administración por concurso o libre designación",
         ["Se rigen por la legislación de la Administración de **destino**", "Conservan la condición de funcionario de la de **origen** y pueden concursar en ella", "Al reingresar, se les reconocen los progresos de carrera (convenios de Conferencia Sectorial o, en su defecto, la Administración de reingreso)"],
         "—",
         "El tiempo en la otra Administración computa **como servicio activo** en el cuerpo o escala de origen."))}

{unidad("3.4 Separación del servicio de los destinados en comunidades autónomas (RD 365/1995, art. 11)",
  lit("RD365", "a11", ["conservarán su condición de funcionarios de la Administración del Estado en la situación de servicio en Comunidades Autónomas", "se acordará por el Ministro del Departamento al que esté adscrito el Cuerpo o Escala al que pertenezca el funcionario"]),
  fichab("Funcionarios de la AGE destinados en comunidades autónomas por concurso, libre designación o reasignación",
         "Funcionarios de la AGE destinados en comunidades autónomas",
         "Se les aplica la normativa de la comunidad autónoma de destino (promoción, retribuciones, situaciones, incompatibilidades y régimen disciplinario)",
         "—",
         "Excepción: la **separación del servicio** la acuerda el **Ministro** del Departamento del Cuerpo o Escala, previo expediente incoado por la comunidad autónoma."))}

{resumen([
  "**Servicio activo**: situación residual, con todos los derechos y deberes (86). En la AGE, también en **comisión de servicios** y en el plazo posesorio (RD 365/1995, art. 3).",
  "**Servicios especiales**: doce supuestos (87.1); se cobra **el cargo** y se conservan los **trienios**; el tiempo computa; reingreso **al menos en la misma localidad** (87.2 y 3).",
  "En la AGE, al perder el cargo: reingreso en **un mes** o **excedencia voluntaria por interés particular** (RD 365/1995, art. 9).",
  "**Servicio en otras AA. PP.**: por transferencias o provisión; legislación de **destino**; el tiempo computa como servicio activo en el cuerpo de origen (88)."],
  "Siguiente: III. ¿Cuándo se deja de prestar servicio? Excedencias, suspensión de funciones y reingreso")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Cuándo se deja de prestar servicio? Excedencias, suspensión de funciones y reingreso (TREBEP, arts. 89 a 91)", donde(
  "Tercera pregunta. El funcionario puede dejar de prestar servicios sin perder su condición: por **excedencia** (voluntaria o por razones protegidas) o por **suspensión de funciones** (sanción o medida cautelar). La vuelta se llama **reingreso**.",
  ["1 Modalidades de excedencia y excedencia por interés particular (art. 89.1 y 2)", "2 Agrupación familiar (art. 89.3)", "3 Cuidado de familiares (art. 89.4)", "4 Violencia de género o sexual y violencia terrorista (art. 89.5 y 6)", "5 Situaciones propias del reglamento de la AGE (RD 365/1995, arts. 12, 13, 15, 18 y 19)", "6 Suspensión de funciones (art. 90; RD 365/1995, arts. 21 y 22)", "7 Reingreso (art. 91; RD 365/1995, art. 23)", "8 Cuadro de efectos de las situaciones"]))

T.ap("s7", "III.1 Modalidades de excedencia y excedencia voluntaria por interés particular (TREBEP, art. 89.1 y 2)", f"""
{unidad("1.1 Las cinco modalidades (art. 89.1)",
  lit("TREBEP", "a89", ["a) Excedencia voluntaria por interés particular.", "b) Excedencia voluntaria por agrupación familiar.", "c) Excedencia por cuidado de familiares.", "d) Excedencia por razón de violencia de género o de violencia sexual.", "e) Excedencia por razón de violencia terrorista."], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Clases de excedencia de los funcionarios de carrera",
         "Funcionarios de carrera",
         ["Voluntaria por interés particular (→ III.1.2)", "Voluntaria por agrupación familiar (→ III.2)", "Por cuidado de familiares (→ III.3)", "Por razón de violencia de género o de violencia sexual (→ III.4)", "Por razón de violencia terrorista (→ III.4)"],
         "—",
         "Solo **dos** son «voluntarias» en el TREBEP (interés particular y agrupación familiar). Las otras tres protegen una situación personal y **reservan el puesto**."))}

{unidad("1.2 Excedencia voluntaria por interés particular (art. 89.2)",
  lit("TREBEP", "a89", ["durante un periodo mínimo de cinco años inmediatamente anteriores", "quedará subordinada a las necesidades del servicio debidamente motivadas", "No podrá declararse cuando al funcionario público se le instruya expediente disciplinario", "Procederá declarar de oficio", "no devengarán retribuciones"], solo=[7, 8, 9, 10, 11]),
  fichab("Excedencia que se pide por motivos propios",
         "Funcionarios de carrera con cinco años de servicios efectivos; la Administración la concede (o la declara de oficio)",
         ["A petición, subordinada a las **necesidades del servicio** debidamente motivadas", "**De oficio** si, acabada la causa de otra situación, no se pide el reingreso en plazo", "No se declara si se instruye **expediente disciplinario**"],
         "**Cinco años** de servicios efectivos inmediatamente anteriores, en cualquier Administración (las leyes de función pública pueden fijar un periodo menor y periodos mínimos de permanencia)",
         "**Sin retribuciones** y **sin cómputo** del tiempo para ascensos, trienios y Seguridad Social. No es un derecho incondicionado: depende de las necesidades del servicio."))}
""", 2)

T.ap("s8", "III.2 Excedencia voluntaria por agrupación familiar (TREBEP, art. 89.3)", f"""
{unidad("2.1 Requisitos y efectos (art. 89.3)",
  lit("TREBEP", "a89", ["sin el requisito de haber prestado servicios efectivos", "cuyo cónyuge resida en otra localidad", "de carácter definitivo"], solo=[12, 13]),
  fichab("Excedencia para reunirse con el cónyuge destinado en otra localidad",
         "Funcionarios cuyo cónyuge resida en otra localidad por desempeñar un puesto **definitivo** como funcionario de carrera o laboral fijo en el sector público, órganos constitucionales, Poder Judicial, la Unión Europea u organizaciones internacionales",
         "Se concede («Podrá concederse») sin exigir servicios previos",
         "Sin periodo mínimo de servicios",
         "No exige los **cinco años**. Mismos efectos que la de interés particular: **sin retribuciones ni cómputo**. El puesto del cónyuge tiene que ser **definitivo**."))}
""", 2)

T.ap("s9", "III.3 Excedencia por cuidado de familiares (TREBEP, art. 89.4)", f"""
{unidad("3.1 Cuidado de hijos y de familiares (art. 89.4)",
  lit("TREBEP", "a89", ["de duración no superior a tres años para atender al cuidado de cada hijo", "hasta el segundo grado inclusive de consanguinidad o afinidad", "será único por cada sujeto causante", "podrá limitar su ejercicio simultáneo", "se reservará, al menos, durante dos años", "en la misma localidad y de igual retribución"], solo=list(range(14, 20))),
  ficha("Funcionarios de carrera (cada uno; si dos lo generan por el mismo sujeto causante, la Administración puede limitar el disfrute simultáneo por razones justificadas del servicio)",
        ["::Excedencia de hasta **tres años**:", "Por cada hijo (por naturaleza, adopción, guarda con fines de adopción o acogimiento permanente), desde el nacimiento o la resolución", "Por un familiar a cargo hasta el **segundo grado** de consanguinidad o afinidad que no pueda valerse por sí mismo y no desempeñe actividad retribuida"],
        "Periodo **único** por sujeto causante: uno nuevo pone fin al anterior",
        ["El tiempo computa para trienios, carrera y Seguridad Social", "Reserva del **mismo puesto** al menos **dos años**; después, puesto en la misma localidad y de igual retribución", "Puede hacer cursos de formación"],
        "Es un **derecho** («tendrán derecho»), no se subordina a las necesidades del servicio. Ojo: el RD 365/1995 (art. 14, de 1995) no recoge el cuidado de familiares; manda el TREBEP (→ I.3.3)."))}
""", 2)

T.ap("s10", "III.4 Excedencia por violencia de género o sexual y por violencia terrorista (TREBEP, art. 89.5 y 6)", f"""
{unidad("4.1 Violencia de género o sexual (art. 89.5)",
  lit("TREBEP", "a89", ["sin tener que haber prestado un tiempo mínimo de servicios previos", "Durante los seis primeros meses tendrán derecho a la reserva del puesto de trabajo", "por tres meses, con un máximo de dieciocho", "Durante los dos primeros meses"], solo=[20, 21, 22, 23]),
  ficha("Las funcionarias víctimas de violencia de género o de violencia sexual",
        "Excedencia para hacer efectiva su protección o su asistencia social integral, sin tiempo mínimo de servicios ni plazo de permanencia",
        "—",
        ["Reserva del puesto los **seis primeros meses**, computables a efectos de antigüedad, carrera y Seguridad Social", "Prórroga por periodos de **tres meses**, con un **máximo de dieciocho**, si las actuaciones judiciales lo exigen", "Retribuciones íntegras los **dos primeros meses**"],
        "Tres cifras que se cruzan en el examen: **2** meses cobrando, **6** meses de reserva, prórrogas de **3** hasta **18**."))}

{unidad("4.2 Violencia terrorista (art. 89.6)",
  lit("TREBEP", "a89", ["previo reconocimiento del Ministerio del Interior o de sentencia judicial firme", "en las mismas condiciones que las víctimas de violencia de género o de violencia sexual"], solo=[24, 25]),
  ficha("Funcionarios que hayan sufrido daños físicos o psíquicos por la actividad terrorista y los amenazados (art. 5 de la Ley 29/2011)",
        "Excedencia en las mismas condiciones que la de violencia de género o sexual",
        f"Requiere {c('TREBEP', 'a89', 'previo reconocimiento del Ministerio del Interior o de sentencia judicial firme')}",
        "Se mantiene mientras sea necesaria para la protección y asistencia social integral",
        "Remite a las condiciones del 89.5: misma reserva, prórrogas y retribuciones."))}
""", 2)

T.ap("s11", "III.5 Situaciones propias del reglamento de la AGE (RD 365/1995, arts. 12, 13, 15, 18 y 19)", f"""
Son situaciones del reglamento de la AGE (de 1995) que siguen vigentes en tanto no se opongan al TREBEP (disposición final cuarta.2: → I.3.3); el art. 85.2 TREBEP, por su parte, permite que las leyes de Función Pública regulen otras (→ I.1.2).

{unidad("5.1 Expectativa de destino (art. 12)",
  lit("RD365", "a12", ["un período máximo de un año", "el 50 por 100 del complemento específico", "esta situación se equipara a la de servicio activo"], solo=[1, 2, 7, 8]),
  fichab("Situación de quien no obtiene puesto en las dos primeras fases de la reasignación de efectivos",
         f"Funcionarios afectados por un procedimiento de reasignación de efectivos que no obtienen puesto en sus dos primeras fases; {c('RD365', 'a12', 'se adscribirán al Ministerio para las Administraciones Públicas')}. Declara la situación la Secretaría de Estado para la Administración Pública (art. 12.4)",
         "Deben aceptar puestos similares en su provincia, concursar y hacer cursos de capacitación (art. 12.3)",
         "Máximo **un año**; después, **excedencia forzosa**",
         "Cobran retribuciones básicas, complemento de destino y el **50 %** del complemento específico; a los demás efectos (incluidas las incompatibilidades) se equipara al **servicio activo**."))}

{unidad("5.2 Excedencia forzosa (art. 13.1 y 6)",
  lit("RD365", "a13", ["por el transcurso del período máximo establecido para la misma", "no se le conceda en el plazo de seis meses", "las retribuciones básicas"], solo=[1, 2, 3, 8]),
  fichab("Excedencia no voluntaria",
         "Funcionarios procedentes de expectativa de destino o de suspensión firme sin puesto reservado",
         ["Expectativa de destino: por agotar el año o por incumplir sus obligaciones", "Suspensión firme sin reserva: si pide el reingreso y no se le concede en **seis meses**"],
         "Seis meses desde la extinción de la responsabilidad penal o disciplinaria",
         "A diferencia de la voluntaria, **cobra** las retribuciones básicas y computa para **derechos pasivos y trienios**."))}

{unidad("5.3 Excedencia voluntaria por prestación de servicios en el sector público (art. 15.1 y 3)",
  lit("RD365", "a15", ["en servicio activo en otro cuerpo o escala de cualquiera de las Administraciones públicas, salvo que hubieran obtenido la oportuna compatibilidad", "con carácter de funcionario interino o de personal laboral temporal no habilitará", "en el plazo máximo de un mes"], solo=[1, 4]),
  fichab("Excedencia de quien pasa a otro cuerpo o a personal laboral fijo del sector público",
         "Funcionarios de carrera en servicio activo en otro cuerpo o escala, o laborales fijos del sector público, salvo compatibilidad",
         "De oficio o a instancia de parte",
         "Dura mientras se mantenga la relación; al cesar, reingreso en **un mes** o pasa a excedencia voluntaria por interés particular",
         "**No** sirve un puesto de **interino** o de **laboral temporal**. Es la excedencia a la que se pasa por no optar en una incompatibilidad (Ley 53/1984, art. 10 → IV.2.6)."))}

{unidad("5.4 Excedencia voluntaria incentivada (art. 18.1, 4 y 5)",
  lit("RD365", "a18", ["una duración de cinco años", "impedirá desempeñar puestos de trabajo en el sector público", "con un máximo de doce mensualidades"], solo=[1, 4, 5]),
  fichab("Excedencia con indemnización para reducir efectivos",
         "Funcionarios en las dos primeras fases de reasignación de efectivos, a su solicitud (y, con derecho, los de expectativa de destino o excedencia forzosa por un Plan de Empleo)",
         "A solicitud del funcionario",
         "**Cinco años**; si no pide el reingreso en el mes siguiente, excedencia voluntaria por interés particular",
         "Una mensualidad por año de servicios, **máximo doce**, sin pagas extraordinarias ni productividad. No puede trabajar en el **sector público** durante esos cinco años."))}

{unidad("5.5 Efectos de la excedencia voluntaria (art. 19)",
  lit("RD365", "a19", ["no producen, en ningún caso, reserva de puesto de trabajo", "no devengarán retribuciones"]),
  fichab("Qué supone cualquier excedencia voluntaria en la AGE",
         "Funcionarios en cualquier modalidad de excedencia voluntaria",
         ["Sin reserva de puesto", "Sin retribuciones (salvo la mensualidad de la incentivada)", "Sin cómputo para promoción, trienios y derechos pasivos"],
         "—",
         "La voluntaria **nunca** reserva puesto; la de **cuidado de familiares** sí (→ III.3.1)."))}
""", 2)

T.ap("s12", "III.6 Suspensión de funciones (TREBEP, art. 90; RD 365/1995, arts. 21 y 22)", f"""
{unidad("6.1 Efectos, clases y límites (art. 90)",
  lit("TREBEP", "a90", ["privado durante el tiempo de permanencia en la misma del ejercicio de sus funciones", "cuando exceda de seis meses", "no podrá exceder de seis años", "no podrá prestar servicios en ninguna Administración Pública", "con carácter provisional"]),
  fichab("Privación temporal de funciones y derechos",
         "El funcionario suspenso; la impone una sentencia penal o una sanción disciplinaria (firme) o se acuerda como medida cautelar (provisional)",
         ["**Firme**: por sentencia en causa criminal o por sanción disciplinaria", "**Provisional**: durante un procedimiento judicial o expediente disciplinario", "No puede prestar servicios en ninguna Administración ni en sus entes durante la pena o sanción"],
         "Pierde el puesto si la suspensión **excede de seis meses**; la firme por sanción disciplinaria, **máximo seis años**",
         "**Seis meses** (pérdida del puesto) y **seis años** (máximo de la sanción). Régimen disciplinario: tema V.2."))}

{unidad("6.2 Suspensión provisional (RD 365/1995, art. 21)",
  lit("RD365", "a21", ["no pudiendo exceder esta suspensión de seis meses", "el 75 por 100 de su sueldo, trienios y pagas extraordinarias", "se computará como de servicio activo"], solo=[1, 3, 4, 5]),
  fichab("Medida cautelar durante un procedimiento judicial o disciplinario",
         "La acuerda, en el expediente disciplinario, la autoridad que ordenó su incoación",
         ["Cobra el **75 %** del sueldo, trienios y pagas extraordinarias y toda la prestación por hijo a cargo", "Si no se declara firme: el tiempo computa como servicio activo y se reincorpora con todos sus derechos"],
         "En expediente disciplinario, máximo **seis meses**, salvo paralización imputable al interesado",
         "**75 %** y **seis meses**. Si la paralización es culpa del interesado, pierde toda retribución mientras dure."))}

{unidad("6.3 Suspensión firme y reingreso (RD 365/1995, art. 22)",
  lit("RD365", "a22", ["excepto cuando la suspensión firme no exceda de seis meses", "con un mes de antelación", "en la situación de excedencia voluntaria por interés particular", "en el plazo de seis meses"]),
  fichab("Suspensión impuesta por condena criminal o sanción disciplinaria",
         "El funcionario condenado o sancionado",
         ["Durante la suspensión no cabe cambio de situación", "Pide el reingreso **un mes antes** de acabar la suspensión; si no, excedencia voluntaria por interés particular", "Si no se le concede en **seis meses**, excedencia forzosa (→ III.5.2)"],
         "Reingreso con efectos desde la extinción de la responsabilidad",
         "Coherente con el art. 90.1 TREBEP: hasta **seis meses** conserva el puesto; si excede, lo pierde."))}
""", 2)

T.ap("s13", "III.7 Reingreso al servicio activo (TREBEP, art. 91; RD 365/1995, art. 23)", f"""
{unidad("7.1 Remisión al reglamento (art. 91)",
  lit("TREBEP", "a91", ["Reglamentariamente se regularán los plazos, procedimientos y condiciones", "con respeto al derecho a la reserva del puesto de trabajo en los casos en que proceda"]),
  fichab("Vuelta al servicio activo desde otra situación",
         "Funcionarios de carrera en cualquier otra situación; lo regula cada Administración por reglamento",
         "Según la situación de procedencia, respetando la reserva de puesto cuando proceda",
         "Los que fije el reglamento (en la AGE, por ejemplo, un mes al cesar en servicios especiales: → II.2.4)",
         "El TREBEP **no fija plazos** de reingreso: los deja al **reglamento**."))}

{unidad("7.2 Cambios de situación sin reingreso previo (RD 365/1995, art. 23)",
  lit("RD365", "a23", ["deberán ser siempre comunicados al Registro Central de Personal", "sin necesidad del reingreso previo al servicio activo"]),
  fichab("Requisitos de los cambios de situación en la AGE",
         "El órgano que declara la situación; se comunica al **Registro Central de Personal**",
         ["Se puede pasar de una situación a otra sin reingresar antes, si se cumplen los requisitos", "Con derecho a reserva, se puede concursar sin cambiar de situación"],
         "—",
         "Comunicación **siempre** al Registro Central de Personal; **no** hace falta reingreso previo."))}
""", 2)

T.ap("s14", "III.8 Cuadro de efectos de las situaciones (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Situación | Retribuciones | Cómputo del tiempo | Reserva de puesto |
|---|---|---|---|
| Servicio activo (86) | Todas | Sí | — (desempeña el puesto) |
| Servicios especiales (87) | Las del cargo + trienios | Ascensos, trienios, promoción interna y Seguridad Social | Reingreso al menos en la misma localidad (87.3) |
| Servicio en otras AA. PP. (88) | Las de la Administración de destino | Como servicio activo en el cuerpo de origen (88.3) | — |
| Voluntaria por interés particular (89.2) | No | No | No |
| Voluntaria por agrupación familiar (89.3) | No | No | No |
| Cuidado de familiares (89.4) | No | Trienios, carrera y Seguridad Social | Mismo puesto 2 años; después, misma localidad e igual retribución |
| Violencia de género o sexual (89.5) | Íntegras los 2 primeros meses | Los 6 primeros meses (y prórrogas) | 6 meses, prorrogables por 3 hasta 18 |
| Suspensión de funciones (90) | No (provisional: 75 %, RD 365/1995, art. 21) | No (salvo provisional no confirmada) | Se pierde si excede de 6 meses |

{resumen([
  "Excedencia: **cinco** modalidades (89.1). Interés particular: **cinco años** de servicios, necesidades del servicio, nunca con expediente disciplinario abierto; **sin sueldo ni cómputo**.",
  "Cuidado de familiares: **hasta tres años** por sujeto causante; computa; reserva del puesto **dos años**.",
  "Violencia de género o sexual: **2** meses cobrando, **6** de reserva, prórrogas de **3** hasta **18**; la terrorista, en las mismas condiciones.",
  "AGE: expectativa de destino (**un año**), excedencia forzosa, voluntaria por servicios en el sector público e incentivada (**cinco años**, máximo **doce** mensualidades).",
  "Suspensión: pérdida del puesto si **excede de seis meses**; firme disciplinaria, **máximo seis años**; provisional, **75 %**. Reingreso: lo regula el **reglamento** (91)."],
  "Siguiente: IV. ¿Qué otras actividades puede ejercer el personal? Incompatibilidades")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Qué otras actividades puede ejercer el personal? Incompatibilidades (Ley 53/1984; RD 598/1985)", donde(
  "Cuarta pregunta. Esté en la situación que esté, el empleado público tiene limitado lo que puede hacer **además** de su puesto. La Ley 53/1984 parte de la **incompatibilidad** y enumera las excepciones; el RD 598/1985 la desarrolla para la Administración del Estado.",
  ["1 Principios y ámbito (Ley 53/1984, arts. 1 y 2)", "2 Actividades públicas: el segundo puesto (arts. 3 a 10; RD 598/1985, arts. 5, 6 y 14)", "3 Actividades privadas (arts. 11 a 15; RD 598/1985, arts. 8, 9 y 11)", "4 Disposiciones comunes (arts. 16 y 18 a 20; RD 598/1985, art. 17)", "5 Cuadro de las incompatibilidades"]))

T.ap("s15", "IV.1 Principios y ámbito de aplicación (Ley 53/1984, arts. 1 y 2)", f"""
{unidad("1.1 Los tres principios (art. 1)",
  lit("L53", "aprimero", ["de un segundo puesto de trabajo, cargo o actividad en el sector público, salvo en los supuestos previstos en la misma", "más de una remuneración", "comprometer su imparcialidad o independencia"]),
  fichab("Principios del régimen de incompatibilidades",
         "Todo el personal del ámbito de la ley (→ IV.1.2)",
         ["Un solo puesto en el **sector público**, salvo los supuestos de la ley (1.1)", "Una sola **remuneración** con cargo a presupuestos públicos, salvo los supuestos de la ley (1.2)", "Incompatibilidad con toda actividad, pública o privada, que impida o menoscabe los deberes o comprometa la **imparcialidad o independencia** (1.3)"],
         "—",
         "«Sector público» incluye a los **miembros electivos** de Asambleas autonómicas y Corporaciones Locales y a los **altos cargos**. «Remuneración» es cualquier derecho económico, fijo o variable, periódico u ocasional."))}

{unidad("1.2 A quién se aplica (art. 2)",
  lit("L53", "asegundo", ["en más de un 50 por cien con subvenciones", "superior al 50 por 100", "cualquiera que sea la naturaleza jurídica de la relación de empleo"]),
  fichab("Ámbito subjetivo de la ley",
         ["::Todo el personal, funcionario o laboral, de:", "La Administración del Estado (personal civil y militar), las comunidades autónomas y las Corporaciones Locales y sus organismos", "La Seguridad Social, el Banco de España y las instituciones financieras públicas", "Entidades, fundaciones y consorcios financiados en **más de un 50 %** con fondos públicos", "Empresas con participación pública **superior al 50 %**", "Personal retribuido por arancel"],
         "—",
         "—",
         "Se aplica «**cualquiera que sea la naturaleza jurídica de la relación de empleo**»: funcionarios, laborales, interinos, eventuales."))}
""", 2)

T.ap("s16", "IV.2 Actividades públicas: el segundo puesto (Ley 53/1984, arts. 3 a 10; RD 598/1985, arts. 5, 6 y 14)", f"""
{unidad("2.1 Regla general y pensiones (art. 3)",
  lit("L53", "atercero", ["para las funciones docente y sanitaria", "la previa y expresa autorización de compatibilidad", "en razón del interés público", "es incompatible con la percepción de pensión de jubilación o retiro"]),
  fichab("Cuándo cabe un segundo puesto público",
         "Lo autoriza el órgano competente (→ IV.2.6), siempre de forma previa y expresa",
         ["Solo en los casos de la ley: funciones **docente y sanitaria**, cargos electivos (art. 5), investigación y asesoramiento (art. 6) y los que fije el Gobierno por interés público", "La autorización **no modifica** la jornada ni el horario de los dos puestos", "Se concede **en razón del interés público**"],
         "—",
         "El puesto público es incompatible con cobrar **pensión de jubilación o retiro**: la pensión queda **en suspenso** (salvo jubilación parcial con tiempo parcial en el ámbito laboral)."))}

{unidad("2.2 Docencia universitaria y sector sanitario o investigador (art. 4.1 y 2)",
  lit("L53", "acuarto", ["como Profesor universitario asociado en régimen de dedicación no superior a la de tiempo parcial", "siempre que los dos puestos vengan reglamentariamente autorizados como de prestación a tiempo parcial"], solo=[1, 2]),
  fichab("Compatibilidades del ámbito docente",
         "Personal del ámbito de la ley (profesor asociado); personal docente e investigador de la Universidad (segundo puesto sanitario o investigador)",
         ["Profesor universitario **asociado** a tiempo parcial como máximo", "PDI de la Universidad: segundo puesto sanitario o investigador, dentro de su área, si los dos son a tiempo parcial"],
         "—",
         "Profesor **asociado**: dedicación **no superior a tiempo parcial**. Es además excepción a la prohibición del art. 16.1 (→ IV.4.1)."))}

{unidad("2.3 Cargos electivos (art. 5)",
  lit("L53", "aquinto", ["salvo que perciban retribuciones periódicas por el desempeño de la función", "salvo que desempeñen en las mismas cargos retribuidos en régimen de dedicación exclusiva", "sólo podrá percibirse la retribución correspondiente a una de las dos actividades"]),
  fichab("Compatibilidad del puesto con cargos electivos",
         "Todo el personal del ámbito de la ley («Por excepción»)",
         ["Miembros de **Asambleas Legislativas autonómicas**, salvo que cobren retribuciones periódicas o lo declaren incompatible", "Miembros de **Corporaciones locales**, salvo cargos retribuidos en **dedicación exclusiva**", "Solo una retribución, más dietas, indemnizaciones o asistencias por la otra; en dedicación parcial local, retribuciones fuera de la jornada"],
         "—",
         "Concejal **sin** dedicación exclusiva: compatible (y sigue en **servicio activo**, → II.1.2); **con** dedicación exclusiva retribuida: incompatible (pasa a **servicios especiales**, → II.2.1). Cayó en 2025 (→ Cierre 1)."))}

{unidad("2.4 Investigación y asesoramiento (art. 6.1)",
  lit("L53", "asexto", ["de investigación de carácter no permanente, o de asesoramiento científico o técnico en supuestos concretos", "por la asignación del encargo en concurso público"], solo=[1, 2]),
  fichab("Compatibilidad excepcional para investigar o asesorar",
         "Todo el personal del ámbito de la ley («excepcionalmente»)",
         "Actividades no propias del personal de las Administraciones; la excepción se acredita por **concurso público** o por requerir **especiales calificaciones** que solo tiene ese personal",
         "—",
         "Investigación **no permanente** y asesoramiento en **supuestos concretos**: nunca con carácter general."))}

{unidad("2.5 Límites retributivos (art. 7)",
  lit("L53", "aseptimo", ["la remuneración prevista en los Presupuestos Generales del Estado para el cargo de Director General", "Un 30 por 100, para los funcionarios del grupo A", "Un 50 por 100, para los funcionarios del grupo E", "no se computarán a efectos de trienios ni de derechos pasivos"]),
  fichab("Tope de lo que se cobra por los dos puestos públicos",
         "Requisito para autorizar; superarlo exige acuerdo expreso del Gobierno, del órgano competente autonómico o del Pleno de la Corporación Local",
         ["La suma no puede superar la retribución del **Director General** en los PGE", "Ni la del puesto principal (dedicación ordinaria) incrementada: A **30 %**, B **35 %**, C **40 %**, D **45 %**, E **50 %**"],
         "Cómputo anual",
         "Escala de **5 en 5** desde el **30 %** (A) al **50 %** (E). El segundo puesto **no** computa para trienios ni derechos pasivos; pagas extraordinarias y prestaciones familiares, por **uno** solo. Cayó en 2025 (→ Cierre 1)."))}

{unidad("2.6 Consejos de administración, competencia y opción (arts. 8 a 10)",
  lit("L53", "aoctavo", ["sólo podrá percibir las dietas o indemnizaciones", "No se podrá pertenecer a más de dos Consejos de Administración"]),
  lit("L53", "anoveno", ["corresponde al Ministerio de la Presidencia, a propuesta de la Subsecretaría del Departamento correspondiente"], solo=[1]),
  lit("L53", "adiez", ["dentro del plazo de toma de posesión", "se entenderá que optan por el nuevo puesto", "en los diez primeros días"]),
  fichab("Consejos de administración en representación pública; quién autoriza; qué pasa si se accede a otro puesto",
         "Autoriza o deniega el segundo puesto (art. 9): el Ministerio de la Presidencia, a propuesta de la Subsecretaría, el órgano competente autonómico o el Pleno de la Corporación Local, según el puesto **principal**, con informe favorable del competente para el **segundo**",
         ["Consejos de administración en representación del sector público: solo **dietas o indemnizaciones** por asistencia; lo demás, a la Tesorería; máximo **dos** consejos (art. 8)", "Nuevo puesto incompatible: **optar** en el plazo de toma de posesión (art. 10)"],
         "Opción: dentro del plazo de **toma de posesión**; si el segundo puesto admite compatibilidad, pedirla en los **diez primeros días** de ese plazo",
         "Sin opción, se entiende que se opta por el **nuevo** puesto y se pasa a **excedencia voluntaria** en el anterior (→ III.5.3)."))}

{unidad("2.7 Plazo e informe en la Administración del Estado (RD 598/1985, arts. 5 y 6.1)",
  lit("RD598", "art5", ["en el plazo de tres meses", "no superior a un mes"], titulo=R598(5)),
  lit("RD598", "art6", ["informe favorable de la autoridad correspondiente al segundo puesto"], solo=[1], titulo=R598(6)),
  fichab("Procedimiento de autorización del segundo puesto público",
         "Resuelve el Ministerio de la Presidencia (art. 5); informe favorable de la autoridad del segundo puesto (art. 6.1)",
         "A solicitud del interesado",
         "**Tres meses** desde la solicitud, prorrogables por resolución motivada **un mes** como máximo",
         "Segundo puesto **público**: tres meses. No confundir con el reconocimiento de actividades **privadas**: dos meses (Ley 53/1984, art. 14 → IV.3.4)."))}

{unidad("2.8 Qué es tiempo parcial (RD 598/1985, art. 14)",
  lit("RD598", "art14", ["que no supere las treinta horas semanales"], titulo=R598(14)),
  fichab("Definición reglamentaria de jornada a tiempo parcial", "—",
         "A efectos de la Ley 53/1984 y del RD 598/1985", "Hasta **treinta** horas semanales",
         "Tiempo parcial = **no más de 30 horas** semanales."))}
""", 2)

T.ap("s17", "IV.3 Actividades privadas (Ley 53/1984, arts. 11 a 15; RD 598/1985, arts. 8, 9 y 11)", f"""
{unidad("3.1 Actividades relacionadas con el propio Departamento (art. 11)",
  lit("L53", "aonce", ["que se relacionen directamente con las que desarrolle el Departamento, Organismo o Entidad donde estuviera destinado", "las actividades particulares que, en ejercicio de un derecho legalmente reconocido, realicen para sí los directamente interesados"]),
  fichab("Prohibición general de actividades privadas relacionadas con el destino",
         "Todo el personal del ámbito de la ley; el Gobierno, por **Real Decreto**, puede fijar incompatibilidades por colectivos (11.2)",
         "No puede ejercer, por sí o por sustitución, actividades privadas (también profesionales) que se relacionen **directamente** con las de su Departamento, Organismo o Entidad",
         "—",
         "Excepción: las actividades que haga **para sí** en ejercicio de un derecho legalmente reconocido."))}

{unidad("3.2 Lo que nunca se puede hacer (art. 12)",
  lit("L53", "adoce", ["En todo caso", "haya intervenido en los dos últimos años", "La participación superior al 10 por 100 en el capital", "igual o superior a la mitad de la jornada semanal ordinaria"]),
  fichab("Actividades privadas prohibidas en todo caso",
         "Todo el personal del ámbito de la ley",
         ["Actividades privadas en asuntos en que intervenga, haya intervenido en los **dos últimos años** o tenga que intervenir", "Consejos de administración de empresas privadas relacionadas con su Departamento", "Cargos en empresas concesionarias, contratistas o con participación o aval público", "Participación **superior al 10 %** en el capital de esas empresas"],
         "Actividad privada con presencia de la mitad de la jornada o más: solo si la actividad pública es de **tiempo parcial**",
         "**Dos años** y **10 %**: las dos cifras del art. 12. «En todo caso»: no cabe reconocer compatibilidad."))}

{unidad("3.3 Segundo puesto público más actividad privada (art. 13)",
  lit("L53", "atrece", ["siempre que la suma de jornadas de ambos sea igual o superior a la máxima en las Administraciones Públicas"]),
  fichab("Límite de quien ya tiene dos puestos públicos", "Quien tiene autorizada la compatibilidad para un segundo puesto o actividad públicos",
         "No se le reconoce compatibilidad para actividades privadas", "Si la suma de jornadas es **igual o superior** a la máxima en las Administraciones Públicas",
         "La prohibición depende de la **suma de jornadas** de los dos puestos públicos."))}

{unidad("3.4 Reconocimiento previo de compatibilidad (art. 14)",
  lit("L53", "acatorce", ["requerirá el previo reconocimiento de compatibilidad", "que se dictará en el plazo de dos meses", "quedarán automáticamente sin efecto en caso de cambio de puesto en el sector público"]),
  fichab("Procedimiento para ejercer actividades privadas",
         "Resuelve el Ministerio de la Presidencia, a propuesta del Subsecretario; el órgano competente autonómico; o el Pleno de la Corporación Local",
         ["Resolución **motivada** que reconoce la compatibilidad o declara la incompatibilidad", "No puede modificar jornada ni horario", "Quien tiene dos puestos públicos debe pedir el reconocimiento con **ambos**"],
         "**Dos meses**",
         "El reconocimiento **caduca automáticamente** si cambia de puesto en el sector público. Privadas: **reconocimiento**; segundo puesto público: **autorización**."))}

{unidad("3.5 Prohibición de usar la condición pública (art. 15)",
  lit("L53", "aquince", ["no podrá invocar o hacer uso de su condición pública"]),
  fichab("Prohibición de invocar la condición pública", "Todo el personal del ámbito de la ley",
         "No puede usarla para una actividad mercantil, industrial o profesional", "—", "Prohibición absoluta, sin excepciones."))}

{unidad("3.6 Reconocimiento previo y actividades relacionadas en la Administración del Estado (RD 598/1985, arts. 8 y 9)",
  lit("RD598", "art8", ["requisito previo imprescindible"], titulo=R598(8)),
  lit("RD598", "art9", ["sometidos a informe, decisión, ayuda financiera o control"], titulo=R598(9)),
  fichab("Desarrollo reglamentario de los arts. 11 y 14 de la ley",
         "Personal del ámbito del RD 598/1985",
         ["Sin reconocimiento previo no puede **comenzar** la actividad privada (art. 8)", "No hay compatibilidad con actividades relacionadas con asuntos sometidos a **informe, decisión, ayuda financiera o control** de su Departamento u organismo (art. 9)"],
         "—",
         "El reconocimiento es **previo**: no se puede empezar y pedirlo después."))}

{unidad("3.7 Actividades privadas incompatibles por colectivos (RD 598/1985, art. 11)",
  lit("RD598", "art11", ["servicios de gestoría administrativa", "con el ejercicio de la profesión de Procurador", "El personal destinado en unidades de contratación o adquisiciones"], solo=[1, 2, 3, 7], titulo=R598(11)),
  fichab("Lista reglamentaria del art. 11.2 de la ley",
         "El Gobierno, por Real Decreto (art. 11.2 de la Ley 53/1984)",
         ["Cualquier personal: **gestoría administrativa**, **Procurador** o actividades con presencia ante los Tribunales en horario de trabajo", "Personal de **contratación**: empresas que suministren, presten servicios o ejecuten obras gestionados por su unidad"],
         "—",
         "La lista completa tiene ocho apartados (letrados, arquitectos e ingenieros, personal sanitario…)."))}
""", 2)

T.ap("s18", "IV.4 Disposiciones comunes (Ley 53/1984, arts. 16 y 18 a 20; RD 598/1985, art. 17)", f"""
{unidad("4.1 Complemento específico y actividades privadas (art. 16)",
  lit("L53", "adieciseis", ["No podrá autorizarse o reconocerse compatibilidad", "Se exceptúan de la prohibición enunciada en el apartado 1", "cuya cuantía no supere el 30 por 100 de su retribución básica"]),
  fichab("Prohibición ligada a la retribución del puesto y su excepción",
         "Personal funcionario, eventual y laboral; retribuido por arancel; personal directivo",
         ["Excepciones (16.3): profesor universitario **asociado** e investigación o asesoramiento del art. 6", "Excepción para actividades privadas (16.4): complemento específico **no superior al 30 %** de la retribución básica, sin contar la antigüedad"],
         "—",
         f"La redacción del apartado 1 procede del TREBEP (disposición final tercera), que, según su disposición final cuarta.1, {c('TREBEP', 'dfcuaa', 'producirá efectos en cada Administración Pública a partir de la entrada en vigor del capítulo III del título III')} con las leyes de Función Pública; {c('TREBEP', 'dfcuaa', 'Hasta que se hagan efectivos esos supuestos la autorización o denegación de compatibilidades continuará rigiéndose por la actual normativa')}. El **30 %** del 16.4 es el dato que más cae."))}

{unidad("4.2 Inscripción en los Registros de Personal (art. 18)",
  lit("L53", "adieciocho", ["se inscribirán en los Registros de Personal correspondientes"]),
  fichab("Constancia registral de las compatibilidades", "Los Registros de Personal",
         "Se inscriben todas las resoluciones de compatibilidad (segundo puesto público o actividades privadas)", "—",
         "En el segundo puesto **público**, sin inscripción no pueden acreditarse **haberes**."))}

{unidad("4.3 Actividades exceptuadas (art. 19)",
  lit("L53", "adiecinueve", ["Quedan exceptuadas del régimen de incompatibilidades", "ni supongan más de setenta y cinco horas al año", "La participación en Tribunales calificadores", "La producción y creación literaria, artística, científica y técnica"]),
  fichab("Actividades que no necesitan autorización ni reconocimiento",
         "Todo el personal del ámbito de la ley",
         ["Administración del patrimonio personal o familiar", "Cursos y conferencias en centros oficiales de formación de funcionarios o profesorado, no permanentes ni habituales, hasta **75 horas al año**", "Tribunales calificadores de pruebas selectivas", "Producción y creación literaria, artística, científica y técnica, y sus publicaciones", "Participación ocasional en medios de comunicación, congresos, seminarios y cursos"],
         "Docencia en centros oficiales: **setenta y cinco horas al año** como máximo",
         "Ocho letras (a a h). Si no se cumplen sus requisitos, hay que pedir autorización o reconocimiento (RD 598/1985, art. 17.3 → IV.4.5)."))}

{unidad("4.4 Incumplimiento y control (art. 20)",
  lit("L53", "aveinte", ["será sancionado conforme al régimen disciplinario de aplicación", "quedando automáticamente revocada la autorización o reconocimiento de compatibilidad", "Inspección General de Servicios de la Administración Pública"]),
  fichab("Consecuencias del incumplimiento",
         "Los órganos de dirección, inspección o jefatura de cada servicio; en la Administración del Estado coordina la **Inspección General de Servicios de la Administración Pública**",
         ["Sanción disciplinaria, sin perjuicio de la ejecutividad de la incompatibilidad", "La actividad compatible no excusa el deber de residencia, la asistencia ni la diligencia"],
         "—",
         "Falta **grave o muy grave** en el puesto → la compatibilidad queda **automáticamente revocada**."))}

{unidad("4.5 Preparación de oposiciones y requisitos de las excepciones (RD 598/1985, art. 17)",
  lit("RD598", "art17", ["sin necesidad de autorización o reconocimiento de compatibilidad", "setenta y cinco horas anuales", "deberá solicitarse la correspondiente autorización o reconocimiento de compatibilidad"], titulo=R598(17)),
  fichab("Desarrollo del art. 19 de la ley",
         "Personal del ámbito del RD 598/1985",
         ["Las actividades del art. 19 no necesitan autorización si cumplen sus requisitos", "Preparar oposiciones es incompatible con formar parte de órganos de selección"],
         "Preparación para el acceso: hasta **75 horas anuales** y sin incumplir el horario",
         "Quien **prepara** oposiciones no puede ser **tribunal**."))}
""", 2)

T.ap("s19", "IV.5 Cuadro de las incompatibilidades (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| | Segundo puesto público | Actividad privada |
|---|---|---|
| Regla | Prohibido salvo los casos de la ley (arts. 1.1 y 3) | Prohibida si se relaciona con el destino (art. 11) o en los casos del art. 12 |
| Acto | **Autorización** previa y expresa (art. 3) | **Reconocimiento** previo (art. 14; RD 598/1985, art. 8) |
| Quién resuelve (Estado) | Ministerio de la Presidencia, a propuesta de la Subsecretaría (art. 9) | Ministerio de la Presidencia, a propuesta del Subsecretario (art. 14) |
| Plazo | Tres meses, prorrogables un mes (RD 598/1985, art. 5) | Dos meses (art. 14) |
| Límites | Retribución del Director General y +30 % a +50 % según grupo (art. 7) | Complemento específico no superior al 30 % de la retribución básica (art. 16.4) |
| Excepciones | Cargos electivos sin dedicación exclusiva ni retribuciones periódicas (art. 5) | Actividades del art. 19 (75 horas, tribunales, creación…) |

{resumen([
  "Principios: **un solo puesto** público, **una sola remuneración**, nada que comprometa la **imparcialidad o independencia** (1). Se aplica a todo el personal, sea cual sea su relación (2).",
  "Segundo puesto público: **autorización** previa y expresa, por interés público (3); docencia, sanidad, cargos electivos (5), investigación (6); límites: Director General y **30 % a 50 %** (7).",
  "Opción en el plazo de **toma de posesión**; sin opción, el **nuevo** puesto y excedencia voluntaria en el anterior (10).",
  "Privadas: **reconocimiento previo** en **dos meses** (14); prohibidas las del art. 12 (**dos años**, **10 %**); excepción del complemento específico **≤ 30 %** (16.4); exceptuadas las del art. 19 (**75 horas**)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_L69 = examen("L", 69, {
  "a": f"Sí es situación: letra d) del art. 85.1 TREBEP, {c('TREBEP', 'a85', 'd) Excedencia.')}",
  "b": f"No es una situación administrativa: no figura en el art. 85.1 TREBEP. Es una forma de provisión de puestos (tema V.4) y quien está en ella sigue en servicio activo: RD 365/1995, art. 3, {c('RD365', 'a3', 'c) Cuando se encuentren en comisión de servicios.')}",
  "c": f"Sí es situación: letra b) del art. 85.1 TREBEP, {c('TREBEP', 'a85', 'b) Servicios especiales.')}",
  "d": f"Sí es situación: letra e) del art. 85.1 TREBEP, {c('TREBEP', 'a85', 'e) Suspensión de funciones.')}"},
  [("Comisión de servicios", "RD365", "a3", "Cuando se encuentren en comisión de servicios")])
EX_X77 = examen("X", 77, {
  "a": f"Sí es situación: art. 85.1 d) TREBEP, {c('TREBEP', 'a85', 'd) Excedencia.')}",
  "b": f"No es una situación administrativa (no está en el art. 85.1 TREBEP): es una forma de provisión, y el funcionario en comisión sigue en servicio activo (RD 365/1995, art. 3: {c('RD365', 'a3', 'Cuando se encuentren en comisión de servicios')}).",
  "c": f"Sí es situación: art. 85.1 b) TREBEP, {c('TREBEP', 'a85', 'b) Servicios especiales.')}",
  "d": f"Sí es situación: art. 85.1 a) TREBEP, {c('TREBEP', 'a85', 'a) Servicio activo.')}"},
  [("Comisión de servicios", "RD365", "a3", "Cuando se encuentren en comisión de servicios")])
EX_L70 = examen("L", 70, {
  "a": f"Literal del art. 5.1 b): {c('L53', 'aquinto', 'Miembros de las Corporaciones locales, salvo que desempeñen en las mismas cargos retribuidos en régimen de dedicación exclusiva')}.",
  "b": f"La compatibilidad no se basa en ninguna «primacía» del sufragio pasivo: es una excepción tasada de la ley ({c('L53', 'aquinto', 'Por excepción, el personal incluido en el ámbito de aplicación de esta Ley podrá compatibilizar sus actividades')}) y tiene un límite (la dedicación exclusiva retribuida).",
  "c": f"Sí es compatible como regla. Y no existe una «excedencia por cargo electo»: con cargo retribuido y de dedicación exclusiva el funcionario pasa a servicios especiales (TREBEP, art. 87.1 f: {c('TREBEP', 'a87', 'Cuando se desempeñen cargos electivos retribuidos y de dedicación exclusiva')}).",
  "d": "El art. 5 no distingue por población del municipio: el único límite es el cargo retribuido en régimen de dedicación exclusiva."},
  [("dedicación exclusiva", "L53", "aquinto", "Miembros de las Corporaciones locales, salvo que desempeñen en las mismas cargos retribuidos en régimen de dedicación exclusiva")])
EX_X78 = examen("X", 78, {
  "a": f"El 40 por 100 es el del grupo C: {c('L53', 'aseptimo', 'Un 40 por 100, para los funcionarios del grupo C')}.",
  "b": f"Literal del art. 7.1: {c('L53', 'aseptimo', 'Un 30 por 100, para los funcionarios del grupo A o personal de nivel equivalente')}.",
  "c": f"El 50 por 100 es el del grupo E: {c('L53', 'aseptimo', 'Un 50 por 100, para los funcionarios del grupo E')}.",
  "d": "El 80 por 100 no figura en el art. 7.1: la escala va del 30 por 100 (grupo A) al 50 por 100 (grupo E)."},
  [("30 por 100", "L53", "aseptimo", "Un 30 por 100, para los funcionarios del grupo A o personal de nivel equivalente")])

T.ap("s20", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **cuatro** preguntas de este tema: dos sobre las situaciones administrativas (turno libre y extraordinario) y dos sobre incompatibilidades. Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-L 2025, pregunta 69 · Situaciones del art. 85 TREBEP (→ I.1.1)", EX_L69,
  "### GACE-L 2025 extraordinario, pregunta 77 · Situaciones administrativas (→ I.1.1)", EX_X77,
  "### GACE-L 2025, pregunta 70 · Cargo electivo local (→ IV.2.3)", EX_L70,
  "### GACE-L 2025 extraordinario, pregunta 78 · Límites retributivos (→ IV.2.5)", EX_X78,
  "### Cómo se pregunta",
  "!> Las situaciones se preguntan con un **intruso**: la comisión de servicios (forma de provisión) mezclada con las cinco del art. 85.1. En incompatibilidades caen las **cifras** (30 % a 50 %, 10 %, dos años, 75 horas) y las **excepciones** del art. 5 (dedicación exclusiva, retribuciones periódicas).",
]))

T.ap("s21", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Qué situaciones hay | Cinco del art. 85.1; las leyes pueden crear otras (85.2); laborales: ET y convenios (92); RD 365/1995 en la AGE | La **comisión de servicios** no es situación |
| II. Servicio activo, servicios especiales, otras AA. PP. | Servicio activo residual (86); doce supuestos de servicios especiales (87); transferencias y provisión (88) | Misión **superior a seis meses**; parlamentarios **con retribuciones periódicas**; reingreso en **un mes** (RD 365/1995) |
| III. Excedencias y suspensión | Interés particular (5 años), agrupación familiar, cuidado de familiares (3 años), violencia (6 meses, hasta 18); suspensión | Suspensión: **6 meses** (pérdida del puesto) y **6 años** (máximo disciplinario) |
| IV. Incompatibilidades | Un puesto, una remuneración, imparcialidad (1); segundo puesto (3 a 10); privadas (11 a 15); comunes (16 a 20) | **30 %** del grupo A (art. 7); complemento específico **≤ 30 %** (16.4); **75 horas** (19) |

?> **Trampas frecuentes:** «la comisión de servicios es una situación administrativa» (es forma de provisión; se está en **servicio activo**); «la excedencia por interés particular exige **tres** años» (son **cinco**); «la excedencia por cuidado de familiares no reserva puesto» (lo reserva **dos años**); «el concejal con dedicación exclusiva es compatible» (no: pasa a **servicios especiales**); «el 30 % es del grupo **E**» (es del **A**; el E, 50 %); «reconocimiento de actividades privadas en **tres** meses» (son **dos**; tres es el segundo puesto **público** en el RD 598/1985).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
Q = [
 ("TREBEP", "a85", "Situaciones", "Según el artículo 85.1 del texto refundido del Estatuto Básico del Empleado Público, ¿cuál de las siguientes es una situación administrativa de los funcionarios de carrera?",
  ["Servicio en otras Administraciones Públicas.", "Comisión de servicios.", "Atribución temporal de funciones.", "Adscripción provisional."], "Art. 85.1 c) TREBEP. Las otras tres son formas de provisión de puestos.", "c) Servicio en otras Administraciones Públicas."),
 ("TREBEP", "a85", "Situaciones", "Según el artículo 85.2 del texto refundido del Estatuto Básico del Empleado Público, ¿quién puede regular otras situaciones administrativas de los funcionarios de carrera?",
  ["Las leyes de Función Pública que se dicten en desarrollo del Estatuto.", "Los convenios colectivos de cada Administración.", "Las órdenes ministeriales de cada Departamento.", "Nadie: la lista del artículo 85.1 es cerrada."], "Art. 85.2 TREBEP.", "Las leyes de Función Pública que se dicten en desarrollo de este Estatuto podrán regular otras situaciones administrativas"),
 ("TREBEP", "a92", "Situaciones", "Según el artículo 92 del texto refundido del Estatuto Básico del Empleado Público, el personal laboral se regirá, en materia de situaciones:",
  ["Por el Estatuto de los Trabajadores y por los Convenios Colectivos que les sean de aplicación.", "Por el capítulo de situaciones del propio Estatuto, en todo caso.", "Por el Reglamento de situaciones administrativas de los funcionarios.", "Por los acuerdos de la Mesa General de Negociación, exclusivamente."], "Art. 92 TREBEP.", "El personal laboral se regirá por el Estatuto de los Trabajadores y por los Convenios Colectivos que les sean de aplicación"),
 ("TREBEP", "a86", "Servicio activo", "Según el artículo 86.2 del texto refundido del Estatuto Básico del Empleado Público, los funcionarios de carrera en situación de servicio activo:",
  ["Gozan de todos los derechos inherentes a su condición de funcionarios y quedan sujetos a los deberes y responsabilidades derivados de la misma.", "Gozan solo de los derechos retributivos inherentes a su condición.", "Quedan sujetos a los deberes de su condición, pero no al régimen de responsabilidades.", "Gozan de los derechos que fije cada convenio colectivo."], "Art. 86.2 TREBEP.", "gozan de todos los derechos inherentes a su condición de funcionarios y quedan sujetos a los deberes y responsabilidades derivados de la misma"),
 ("RD365", "a3", "Servicio activo", "Según el artículo 3 del Reglamento de Situaciones Administrativas de los Funcionarios Civiles de la Administración General del Estado (Real Decreto 365/1995), el funcionario que se encuentra en comisión de servicios está en situación de:",
  ["Servicio activo.", "Servicios especiales.", "Excedencia voluntaria por servicios en el sector público.", "Expectativa de destino."], "Art. 3 c) RD 365/1995.", "Cuando se encuentren en comisión de servicios"),
 ("TREBEP", "a87", "Servicios especiales", "Según el artículo 87.1 b) del texto refundido del Estatuto Básico del Empleado Público, se declara en servicios especiales al funcionario autorizado para realizar una misión en organismos internacionales por periodo determinado:",
  ["Superior a seis meses.", "Superior a tres meses.", "Superior a un año.", "De cualquier duración."], "Art. 87.1 b) TREBEP.", "para realizar una misión por periodo determinado superior a seis meses"),
 ("TREBEP", "a87", "Servicios especiales", "Según el artículo 87.1 e) del texto refundido del Estatuto Básico del Empleado Público, los funcionarios que acceden a la condición de miembros de las asambleas legislativas de las comunidades autónomas pasan a servicios especiales:",
  ["Si perciben retribuciones periódicas por la realización de la función.", "En todo caso.", "Solo si lo solicitan expresamente.", "Solo si la asamblea tiene más de cien miembros."], "Art. 87.1 e) TREBEP.", "si perciben retribuciones periódicas por la realización de la función"),
 ("TREBEP", "a87", "Servicios especiales", "Según el artículo 87.1 i) del texto refundido del Estatuto Básico del Empleado Público, el funcionario de carrera designado como personal eventual por ocupar un puesto de confianza o asesoramiento político:",
  ["Será declarado en servicios especiales, salvo que opte por permanecer en servicio activo.", "Pasará siempre a excedencia voluntaria por interés particular.", "Permanecerá siempre en servicio activo.", "Pasará a la situación de servicio en otras Administraciones Públicas."], "Art. 87.1 i) TREBEP.", "Cuando sean designados como personal eventual por ocupar puestos de trabajo con funciones expresamente calificadas como de confianza o asesoramiento político y no opten por permanecer en la situación de servicio activo"),
 ("TREBEP", "a87", "Servicios especiales", "Según el artículo 87.2 del texto refundido del Estatuto Básico del Empleado Público, quienes se encuentren en situación de servicios especiales percibirán:",
  ["Las retribuciones del puesto o cargo que desempeñen y no las que les correspondan como funcionarios de carrera, sin perjuicio del derecho a percibir los trienios.", "Las retribuciones que les correspondan como funcionarios de carrera, más las del cargo.", "Las retribuciones que les correspondan como funcionarios de carrera, sin trienios.", "Únicamente los trienios que tengan reconocidos."], "Art. 87.2 TREBEP.", "percibirán las retribuciones del puesto o cargo que desempeñen y no las que les correspondan como funcionarios de carrera, sin perjuicio del derecho a percibir los trienios"),
 ("TREBEP", "a87", "Servicios especiales", "Según el artículo 87.3 del texto refundido del Estatuto Básico del Empleado Público, quienes se encuentren en situación de servicios especiales tendrán derecho, al menos, a reingresar al servicio activo:",
  ["En la misma localidad, en las condiciones y con las retribuciones correspondientes a la categoría, nivel o escalón de la carrera consolidados.", "En el mismo puesto de trabajo que ocupaban, en todo caso.", "En cualquier localidad del territorio nacional.", "En un puesto de libre designación de nivel superior."], "Art. 87.3 TREBEP.", "al menos, a reingresar al servicio activo en la misma localidad"),
 ("RD365", "a9", "Servicios especiales", "Según el artículo 9.1 del Real Decreto 365/1995, quienes pierdan la condición en virtud de la cual hubieran sido declarados en servicios especiales deberán solicitar el reingreso al servicio activo en el plazo de:",
  ["Un mes.", "Quince días.", "Tres meses.", "Seis meses."], "Art. 9.1 RD 365/1995; de no hacerlo, excedencia voluntaria por interés particular.", "deberán solicitar el reingreso al servicio activo en el plazo de un mes"),
 ("TREBEP", "a88", "Otras Administraciones", "Según el artículo 88.1 del texto refundido del Estatuto Básico del Empleado Público, serán declarados en servicio en otras Administraciones Públicas los funcionarios de carrera que obtengan destino en una Administración distinta:",
  ["En virtud de los procesos de transferencias o por los procedimientos de provisión de puestos de trabajo.", "Solo en virtud de los procesos de transferencias.", "Solo mediante comisión de servicios.", "Por haber superado un proceso selectivo de esa otra Administración."], "Art. 88.1 TREBEP.", "en virtud de los procesos de transferencias o por los procedimientos de provisión de puestos de trabajo"),
 ("TREBEP", "a88", "Otras Administraciones", "Según el artículo 88.3 del texto refundido del Estatuto Básico del Empleado Público, el tiempo de servicio en la Administración Pública en la que estén destinados los funcionarios en servicio en otras Administraciones Públicas:",
  ["Se les computará como de servicio activo en su cuerpo o escala de origen.", "No se les computará a ningún efecto en su Administración de origen.", "Se les computará solo a efectos de trienios.", "Se les computará solo si reingresan en un plazo de dos años."], "Art. 88.3 TREBEP.", "se les computará como de servicio activo en su cuerpo o escala de origen"),
 ("RD365", "a11", "Otras Administraciones", "Según el artículo 11.2 del Real Decreto 365/1995, la sanción de separación del servicio de un funcionario de la Administración del Estado destinado en una comunidad autónoma se acordará por:",
  ["El Ministro del Departamento al que esté adscrito el Cuerpo o Escala al que pertenezca el funcionario.", "El órgano competente de la comunidad autónoma de destino, sin intervención del Estado.", "El Consejo de Ministros, en todo caso.", "El Delegado del Gobierno en la comunidad autónoma."], "Art. 11.2 RD 365/1995, previa incoación del expediente por la comunidad autónoma.", "se acordará por el Ministro del Departamento al que esté adscrito el Cuerpo o Escala al que pertenezca el funcionario"),
 ("TREBEP", "a89", "Excedencias", "Según el artículo 89.1 del texto refundido del Estatuto Básico del Empleado Público, ¿cuál de las siguientes es una modalidad de excedencia de los funcionarios de carrera?",
  ["Excedencia por razón de violencia terrorista.", "Excedencia por razón de matrimonio.", "Excedencia por estudios en el extranjero.", "Excedencia por cargo sindical."], "Art. 89.1 e) TREBEP.", "e) Excedencia por razón de violencia terrorista."),
 ("TREBEP", "a89", "Excedencias", "Según el artículo 89.2 del texto refundido del Estatuto Básico del Empleado Público, los funcionarios de carrera podrán obtener la excedencia voluntaria por interés particular cuando hayan prestado servicios efectivos en cualquiera de las Administraciones Públicas durante un periodo mínimo de:",
  ["Cinco años inmediatamente anteriores.", "Tres años inmediatamente anteriores.", "Dos años inmediatamente anteriores.", "Diez años inmediatamente anteriores."], "Art. 89.2 TREBEP.", "durante un periodo mínimo de cinco años inmediatamente anteriores"),
 ("TREBEP", "a89", "Excedencias", "Según el artículo 89.2 del texto refundido del Estatuto Básico del Empleado Público, la excedencia voluntaria por interés particular no podrá declararse cuando:",
  ["Al funcionario público se le instruya expediente disciplinario.", "El funcionario tenga menos de diez años de servicios.", "El funcionario haya disfrutado antes de una excedencia por cuidado de familiares.", "El funcionario ocupe un puesto de libre designación."], "Art. 89.2 TREBEP.", "No podrá declararse cuando al funcionario público se le instruya expediente disciplinario"),
 ("TREBEP", "a89", "Excedencias", "Según el artículo 89.2 del texto refundido del Estatuto Básico del Empleado Público, quienes se encuentren en situación de excedencia por interés particular:",
  ["No devengarán retribuciones, ni les será computable el tiempo a efectos de ascensos, trienios y derechos en el régimen de Seguridad Social.", "Devengarán las retribuciones básicas.", "No devengarán retribuciones, pero el tiempo les computará a efectos de trienios.", "Tendrán reserva del puesto de trabajo durante dos años."], "Art. 89.2 TREBEP.", "no devengarán retribuciones, ni les será computable el tiempo que permanezcan en tal situación a efectos de ascensos, trienios y derechos en el régimen de Seguridad Social"),
 ("TREBEP", "a89", "Excedencias", "Según el artículo 89.3 del texto refundido del Estatuto Básico del Empleado Público, la excedencia voluntaria por agrupación familiar podrá concederse a los funcionarios:",
  ["Cuyo cónyuge resida en otra localidad por haber obtenido y estar desempeñando un puesto de trabajo de carácter definitivo en el sector público.", "Que acrediten cinco años de servicios efectivos y cuyo cónyuge trabaje en cualquier empresa.", "Cuyo cónyuge resida en la misma localidad y trabaje en el sector público.", "Que tengan hijos menores de doce años a su cargo."], "Art. 89.3 TREBEP: sin requisito de servicios previos.", "cuyo cónyuge resida en otra localidad por haber obtenido y estar desempeñando un puesto de trabajo de carácter definitivo"),
 ("TREBEP", "a89", "Excedencias", "Según el artículo 89.4 del texto refundido del Estatuto Básico del Empleado Público, la excedencia para atender al cuidado de cada hijo tendrá una duración:",
  ["No superior a tres años.", "No superior a dos años.", "No superior a cinco años.", "No inferior a dos años ni superior a quince."], "Art. 89.4 TREBEP.", "derecho a un período de excedencia de duración no superior a tres años para atender al cuidado de cada hijo"),
 ("TREBEP", "a89", "Excedencias", "Según el artículo 89.4 del texto refundido del Estatuto Básico del Empleado Público, durante la excedencia por cuidado de familiares el puesto de trabajo desempeñado se reservará, al menos, durante:",
  ["Dos años.", "Un año.", "Seis meses.", "Tres años."], "Art. 89.4 TREBEP; después, a un puesto en la misma localidad y de igual retribución.", "El puesto de trabajo desempeñado se reservará, al menos, durante dos años"),
 ("TREBEP", "a89", "Excedencias", "Según el artículo 89.4 del texto refundido del Estatuto Básico del Empleado Público, la excedencia para atender al cuidado de un familiar a cargo alcanza a los familiares:",
  ["Hasta el segundo grado inclusive de consanguinidad o afinidad.", "Hasta el primer grado de consanguinidad, exclusivamente.", "Hasta el cuarto grado de consanguinidad.", "Hasta el tercer grado de consanguinidad o afinidad."], "Art. 89.4 TREBEP.", "hasta el segundo grado inclusive de consanguinidad o afinidad"),
 ("TREBEP", "a89", "Excedencias", "Según el artículo 89.5 del texto refundido del Estatuto Básico del Empleado Público, las funcionarias víctimas de violencia de género o de violencia sexual en situación de excedencia tendrán derecho a la reserva del puesto de trabajo durante:",
  ["Los seis primeros meses.", "Los dos primeros meses.", "El primer año.", "Los tres primeros meses."], "Art. 89.5 TREBEP; prorrogable por tres meses, con un máximo de dieciocho.", "Durante los seis primeros meses tendrán derecho a la reserva del puesto de trabajo"),
 ("TREBEP", "a89", "Excedencias", "Según el artículo 89.5 del texto refundido del Estatuto Básico del Empleado Público, durante la excedencia por razón de violencia de género o de violencia sexual, la funcionaria tendrá derecho a percibir las retribuciones íntegras durante:",
  ["Los dos primeros meses.", "Los seis primeros meses.", "Toda la excedencia.", "El primer mes."], "Art. 89.5 TREBEP.", "Durante los dos primeros meses de esta excedencia la funcionaria tendrá derecho a percibir las retribuciones íntegras"),
 ("RD365", "a12", "Situaciones de la AGE", "Según el artículo 12.2 del Real Decreto 365/1995, los funcionarios permanecerán en la situación de expectativa de destino un período máximo de:",
  ["Un año, transcurrido el cual pasarán a la situación de excedencia forzosa.", "Seis meses, transcurridos los cuales pasarán a excedencia voluntaria por interés particular.", "Dos años, transcurridos los cuales pasarán a la situación de excedencia forzosa.", "Un año, transcurrido el cual perderán la condición de funcionario."], "Art. 12.2 RD 365/1995.", "un período máximo de un año, transcurrido el cual pasarán a la situación de excedencia forzosa"),
 ("RD365", "a18", "Situaciones de la AGE", "Según el artículo 18.4 del Real Decreto 365/1995, la excedencia voluntaria incentivada tendrá una duración de:",
  ["Cinco años.", "Dos años.", "Tres años.", "Diez años."], "Art. 18.4 RD 365/1995.", "La excedencia voluntaria incentivada tendrá una duración de cinco años"),
 ("RD365", "a18", "Situaciones de la AGE", "Según el artículo 18.5 del Real Decreto 365/1995, quienes pasen a la excedencia voluntaria incentivada tendrán derecho a una mensualidad de las retribuciones de carácter periódico por cada año completo de servicios efectivos, con un máximo de:",
  ["Doce mensualidades.", "Seis mensualidades.", "Veinticuatro mensualidades.", "Quince mensualidades."], "Art. 18.5 RD 365/1995.", "con un máximo de doce mensualidades"),
 ("TREBEP", "a90", "Suspensión", "Según el artículo 90.1 del texto refundido del Estatuto Básico del Empleado Público, la suspensión de funciones determinará la pérdida del puesto de trabajo cuando exceda de:",
  ["Seis meses.", "Tres meses.", "Un año.", "Seis años."], "Art. 90.1 TREBEP.", "La suspensión determinará la pérdida del puesto de trabajo cuando exceda de seis meses"),
 ("TREBEP", "a90", "Suspensión", "Según el artículo 90.2 del texto refundido del Estatuto Básico del Empleado Público, la suspensión firme por sanción disciplinaria no podrá exceder de:",
  ["Seis años.", "Tres años.", "Seis meses.", "Diez años."], "Art. 90.2 TREBEP.", "La suspensión firme por sanción disciplinaria no podrá exceder de seis años"),
 ("RD365", "a21", "Suspensión", "Según el artículo 21.4 del Real Decreto 365/1995, el funcionario en suspensión provisional tendrá derecho a percibir:",
  ["El 75 por 100 de su sueldo, trienios y pagas extraordinarias.", "El 50 por 100 de su sueldo, trienios y pagas extraordinarias.", "La totalidad de sus retribuciones básicas y complementarias.", "Ninguna retribución."], "Art. 21.4 RD 365/1995.", "El suspenso provisional tendrá derecho a percibir el 75 por 100 de su sueldo, trienios y pagas extraordinarias"),
 ("TREBEP", "a91", "Reingreso", "Según el artículo 91 del texto refundido del Estatuto Básico del Empleado Público, los plazos, procedimientos y condiciones para solicitar el reingreso al servicio activo de los funcionarios de carrera:",
  ["Se regularán reglamentariamente, según las situaciones administrativas de procedencia.", "Los fija el propio Estatuto en un mes para todas las situaciones.", "Se regularán en los convenios colectivos.", "Los fija cada órgano de selección."], "Art. 91 TREBEP.", "Reglamentariamente se regularán los plazos, procedimientos y condiciones, según las situaciones administrativas de procedencia"),
 ("L53", "aprimero", "Incompatibilidades", "Según el artículo 1.3 de la Ley 53/1984, de Incompatibilidades, el desempeño de un puesto de trabajo será incompatible con el ejercicio de cualquier cargo, profesión o actividad, público o privado, que pueda impedir o menoscabar el estricto cumplimiento de sus deberes o:",
  ["Comprometer su imparcialidad o independencia.", "Reducir su rendimiento en más de un 10 por 100.", "Suponer una retribución superior a la del puesto principal.", "Exceder de setenta y cinco horas al año."], "Art. 1.3 Ley 53/1984.", "comprometer su imparcialidad o independencia"),
 ("L53", "atercero", "Incompatibilidades", "Según el artículo 3.2 de la Ley 53/1984, el desempeño de un puesto de trabajo en el sector público es incompatible con la percepción de pensión de jubilación o retiro, de modo que la pensión:",
  ["Quedará en suspenso por el tiempo que dure el desempeño del puesto, sin que ello afecte a sus actualizaciones.", "Se extinguirá definitivamente.", "Se reducirá al 50 por 100.", "Se percibirá íntegra junto con la retribución del puesto."], "Art. 3.2 Ley 53/1984.", "La percepción de las pensiones indicadas quedará en suspenso por el tiempo que dure el desempeño de dicho puesto, sin que ello afecte a sus actualizaciones"),
 ("L53", "aquinto", "Incompatibilidades", "Según el artículo 5.1 a) de la Ley 53/1984, el personal incluido en su ámbito podrá compatibilizar sus actividades con el cargo de miembro de las Asambleas Legislativas de las Comunidades Autónomas:",
  ["Salvo que perciba retribuciones periódicas por el desempeño de la función o que por las mismas se establezca la incompatibilidad.", "En todo caso, percibiendo ambas retribuciones.", "Solo si renuncia a la retribución del puesto público.", "Nunca: es siempre incompatible."], "Art. 5.1 a) Ley 53/1984.", "salvo que perciban retribuciones periódicas por el desempeño de la función o que por las mismas se establezca la incompatibilidad"),
 ("L53", "aseptimo", "Incompatibilidades", "Según el artículo 7.1 de la Ley 53/1984, para autorizar la compatibilidad de actividades públicas, la cantidad total percibida por ambos puestos no podrá superar la correspondiente al principal incrementada, para los funcionarios del grupo C o personal de nivel equivalente, en:",
  ["Un 40 por 100.", "Un 30 por 100.", "Un 35 por 100.", "Un 50 por 100."], "Art. 7.1 Ley 53/1984: A 30, B 35, C 40, D 45, E 50 por 100.", "Un 40 por 100, para los funcionarios del grupo C o personal de nivel equivalente"),
 ("L53", "aseptimo", "Incompatibilidades", "Según el artículo 7.1 de la Ley 53/1984, la cantidad total percibida por ambos puestos o actividades públicas no podrá superar la remuneración prevista en los Presupuestos Generales del Estado para el cargo de:",
  ["Director General.", "Secretario de Estado.", "Subsecretario.", "Ministro."], "Art. 7.1 Ley 53/1984.", "la remuneración prevista en los Presupuestos Generales del Estado para el cargo de Director General"),
 ("L53", "aoctavo", "Incompatibilidades", "Según el artículo 8 de la Ley 53/1984, el personal que en representación del sector público pertenezca a Consejos de Administración no podrá pertenecer, salvo autorización excepcional, a más de:",
  ["Dos Consejos de Administración u órganos de gobierno.", "Tres Consejos de Administración u órganos de gobierno.", "Un Consejo de Administración u órgano de gobierno.", "Cinco Consejos de Administración u órganos de gobierno."], "Art. 8 Ley 53/1984.", "No se podrá pertenecer a más de dos Consejos de Administración u órganos de gobierno"),
 ("L53", "adiez", "Incompatibilidades", "Según el artículo 10 de la Ley 53/1984, quienes accedan a un nuevo puesto del sector público incompatible con el que vinieran desempeñando y no ejerzan la opción en el plazo señalado:",
  ["Se entenderá que optan por el nuevo puesto, pasando a la situación de excedencia voluntaria en los que vinieran desempeñando.", "Se entenderá que optan por el puesto que vinieran desempeñando.", "Perderán los dos puestos.", "Serán declarados en servicios especiales en el nuevo puesto."], "Art. 10 Ley 53/1984: la opción se hace dentro del plazo de toma de posesión.", "A falta de opción en el plazo señalado se entenderá que optan por el nuevo puesto, pasando a la situación de excedencia voluntaria en los que vinieran desempeñando"),
 ("L53", "adoce", "Incompatibilidades", "Según el artículo 12.1 d) de la Ley 53/1984, el personal incluido en su ámbito no podrá tener, en las empresas concesionarias o contratistas del sector público, una participación en el capital:",
  ["Superior al 10 por 100.", "Superior al 5 por 100.", "Superior al 25 por 100.", "Superior al 50 por 100."], "Art. 12.1 d) Ley 53/1984.", "La participación superior al 10 por 100 en el capital"),
 ("L53", "adoce", "Incompatibilidades", "Según el artículo 12.1 a) de la Ley 53/1984, el personal incluido en su ámbito no podrá desempeñar actividades privadas en los asuntos en que esté interviniendo, tenga que intervenir por razón del puesto público o haya intervenido en:",
  ["Los dos últimos años.", "El último año.", "Los cinco últimos años.", "Los seis últimos meses."], "Art. 12.1 a) Ley 53/1984.", "haya intervenido en los dos últimos años"),
 ("L53", "acatorce", "Incompatibilidades", "Según el artículo 14 de la Ley 53/1984, la resolución motivada que reconozca la compatibilidad para actividades privadas o declare la incompatibilidad se dictará en el plazo de:",
  ["Dos meses.", "Tres meses.", "Un mes.", "Seis meses."], "Art. 14 Ley 53/1984.", "que se dictará en el plazo de dos meses"),
 ("L53", "adieciseis", "Incompatibilidades", "Según el artículo 16.4 de la Ley 53/1984, podrá reconocerse compatibilidad para actividades privadas al personal que perciba complementos específicos, o concepto equiparable, cuya cuantía no supere:",
  ["El 30 por 100 de su retribución básica, excluidos los conceptos que tengan su origen en la antigüedad.", "El 50 por 100 de su retribución básica, incluidos los trienios.", "El 30 por 100 de sus retribuciones totales.", "El 10 por 100 de su retribución básica."], "Art. 16.4 Ley 53/1984.", "cuya cuantía no supere el 30 por 100 de su retribución básica, excluidos los conceptos que tengan su origen en la antigüedad"),
 ("L53", "adiecinueve", "Incompatibilidades", "Según el artículo 19 b) de la Ley 53/1984, queda exceptuada del régimen de incompatibilidades la impartición de cursos o conferencias en centros oficiales destinados a la formación de funcionarios, cuando no tenga carácter permanente o habitual ni suponga más de:",
  ["Setenta y cinco horas al año.", "Cien horas al año.", "Cincuenta horas al año.", "Treinta horas al mes."], "Art. 19 b) Ley 53/1984.", "ni supongan más de setenta y cinco horas al año"),
 ("RD598", "art5", "Incompatibilidades", "Según el artículo 5 del Real Decreto 598/1985, las solicitudes de autorización de compatibilidad de un segundo puesto en el sector público serán resueltas en el plazo de:",
  ["Tres meses a contar desde la fecha de presentación de la solicitud.", "Dos meses a contar desde la fecha de presentación de la solicitud.", "Un mes a contar desde la fecha de presentación de la solicitud.", "Seis meses a contar desde la fecha de presentación de la solicitud."], "Art. 5 RD 598/1985; prorrogable por un mes como máximo.", "en el plazo de tres meses a contar desde la fecha de presentación de la solicitud"),
 ("RD598", "art14", "Incompatibilidades", "Según el artículo 14 del Real Decreto 598/1985, se entiende por puesto de trabajo con jornada de tiempo parcial aquel que no supere:",
  ["Las treinta horas semanales.", "Las veinte horas semanales.", "Las treinta y siete horas y media semanales.", "La mitad de la jornada ordinaria."], "Art. 14 RD 598/1985.", "aquella que no supere las treinta horas semanales"),
 ("L53", "adieciocho", "Incompatibilidades", "Según el artículo 18 de la Ley 53/1984, todas las resoluciones de compatibilidad:",
  ["Se inscribirán en los Registros de Personal correspondientes.", "Se publicarán en el Boletín Oficial del Estado.", "Se comunicarán al Tribunal de Cuentas.", "Se notificarán a las organizaciones sindicales."], "Art. 18 Ley 53/1984.", "se inscribirán en los Registros de Personal correspondientes"),
]
for k, art, cat, enun, ops, expl, frag in Q: T.q(k, art, cat, enun, ops, expl, frag)
T.real("L", 69, "Situaciones"); T.real("X", 77, "Situaciones"); T.real("L", 70, "Incompatibilidades"); T.real("X", 78, "Incompatibilidades")

# Flashcards
for q_, a_, cat in [
  ("Situaciones de los funcionarios de carrera (TREBEP, art. 85.1)", "Servicio activo; servicios especiales; servicio en otras Administraciones Públicas; excedencia; suspensión de funciones.", "Situaciones"),
  ("¿Es la comisión de servicios una situación administrativa?", "No: es una forma de provisión; el funcionario sigue en servicio activo (RD 365/1995, art. 3 c).", "Situaciones"),
  ("Situaciones del personal laboral (art. 92)", "Estatuto de los Trabajadores y convenios colectivos; el capítulo del TREBEP solo si el convenio lo dice y en lo compatible.", "Situaciones"),
  ("Situaciones propias del RD 365/1995 (AGE)", "Expectativa de destino, excedencia forzosa, excedencia voluntaria por servicios en el sector público y excedencia voluntaria incentivada.", "Situaciones de la AGE"),
  ("Servicios especiales: misión internacional (art. 87.1 b)", "Por periodo determinado superior a seis meses.", "Servicios especiales"),
  ("Servicios especiales: retribuciones y cómputo (art. 87.2)", "Las del cargo, no las de funcionario, más los trienios; el tiempo computa para ascensos, trienios, promoción interna y Seguridad Social.", "Servicios especiales"),
  ("Servicios especiales: reingreso (art. 87.3; RD 365/1995, art. 9)", "Derecho, al menos, a la misma localidad; pedirlo en un mes al perder el cargo o excedencia voluntaria por interés particular.", "Servicios especiales"),
  ("Servicio en otras AA. PP. (art. 88)", "Destino en otra Administración por transferencias o provisión; legislación de destino; el tiempo computa como servicio activo en el cuerpo de origen.", "Otras Administraciones"),
  ("Modalidades de excedencia (art. 89.1)", "Voluntaria por interés particular; voluntaria por agrupación familiar; cuidado de familiares; violencia de género o sexual; violencia terrorista.", "Excedencias"),
  ("Excedencia por interés particular (art. 89.2)", "Cinco años de servicios; subordinada a necesidades del servicio; no con expediente disciplinario; sin retribuciones ni cómputo.", "Excedencias"),
  ("Excedencia por agrupación familiar (art. 89.3)", "Sin servicios previos; cónyuge en otra localidad con puesto definitivo en el sector público; sin retribuciones ni cómputo.", "Excedencias"),
  ("Excedencia por cuidado de familiares (art. 89.4)", "Hasta tres años por sujeto causante (hijos o familiares hasta 2.º grado); computa; reserva del puesto dos años.", "Excedencias"),
  ("Excedencia por violencia de género o sexual (art. 89.5)", "Sin tiempo mínimo; reserva 6 meses, prorrogable por 3 hasta 18; retribuciones íntegras 2 meses.", "Excedencias"),
  ("Expectativa de destino (RD 365/1995, art. 12)", "Máximo un año; luego excedencia forzosa; básicas, destino y 50 % del específico.", "Situaciones de la AGE"),
  ("Excedencia voluntaria incentivada (RD 365/1995, art. 18)", "Cinco años sin trabajar en el sector público; una mensualidad por año de servicio, máximo doce.", "Situaciones de la AGE"),
  ("Suspensión de funciones (art. 90)", "Pérdida del puesto si excede de seis meses; firme disciplinaria, máximo seis años; provisional durante procedimiento.", "Suspensión"),
  ("Suspensión provisional (RD 365/1995, art. 21)", "En expediente disciplinario, máximo seis meses; cobra el 75 % del sueldo, trienios y pagas extraordinarias.", "Suspensión"),
  ("Principios de la Ley 53/1984 (art. 1)", "Un solo puesto en el sector público; una sola remuneración; nada que comprometa la imparcialidad o independencia.", "Incompatibilidades"),
  ("Cargos electivos compatibles (art. 5)", "Asambleas autonómicas sin retribuciones periódicas; Corporaciones locales sin cargo retribuido en dedicación exclusiva.", "Incompatibilidades"),
  ("Límites retributivos del segundo puesto público (art. 7)", "Retribución de Director General y principal + 30 % (A), 35 % (B), 40 % (C), 45 % (D), 50 % (E).", "Incompatibilidades"),
  ("Opción por incompatibilidad (art. 10)", "En el plazo de toma de posesión; sin opción, el nuevo puesto y excedencia voluntaria en el anterior.", "Incompatibilidades"),
  ("Actividades privadas prohibidas en todo caso (art. 12)", "Asuntos en que intervenga o haya intervenido en los dos últimos años; consejos de empresas relacionadas; cargos en contratistas; participación superior al 10 %.", "Incompatibilidades"),
  ("Plazos de las compatibilidades", "Actividades privadas: dos meses (Ley 53/1984, art. 14). Segundo puesto público: tres meses, prorrogables un mes (RD 598/1985, art. 5).", "Incompatibilidades"),
  ("Complemento específico y actividades privadas (art. 16.4)", "Cabe reconocer compatibilidad si no supera el 30 % de la retribución básica (sin antigüedad).", "Incompatibilidades"),
  ("Actividades exceptuadas (art. 19)", "Patrimonio personal; cursos hasta 75 horas al año; tribunales calificadores; creación literaria, artística, científica y técnica; participación ocasional en medios y congresos.", "Incompatibilidades"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Situación administrativa", "Posición del funcionario de carrera en su relación de servicio; el TREBEP enumera cinco (art. 85.1) y permite que las leyes de función pública regulen otras (art. 85.2).", "s1", "Situaciones")
T.glos("Servicio activo", "Situación de quien presta servicios como funcionario y no le corresponde otra; goza de todos los derechos y deberes (TREBEP, art. 86).", "s4", "Servicio activo")
T.glos("Servicios especiales", "Situación del funcionario que pasa a ciertos cargos (Gobierno, parlamentos, altos cargos, organismos internacionales…); cobra el cargo, conserva los trienios y computa el tiempo (TREBEP, art. 87).", "s5", "Servicios especiales")
T.glos("Servicio en otras Administraciones Públicas", "Situación de quien obtiene destino en otra Administración por transferencias o provisión de puestos (TREBEP, art. 88).", "s6", "Otras Administraciones")
T.glos("Excedencia voluntaria por interés particular", "Excedencia a petición, con cinco años de servicios previos y subordinada a las necesidades del servicio; sin retribuciones ni cómputo (TREBEP, art. 89.2).", "s7", "Excedencias")
T.glos("Excedencia por cuidado de familiares", "Derecho a una excedencia de hasta tres años por cada hijo o familiar a cargo hasta el segundo grado; computa y reserva el puesto dos años (TREBEP, art. 89.4).", "s9", "Excedencias")
T.glos("Expectativa de destino", "Situación de la AGE de quien no obtiene puesto en las dos primeras fases de reasignación de efectivos; máximo un año (RD 365/1995, art. 12).", "s11", "Situaciones de la AGE")
T.glos("Excedencia forzosa", "Situación de la AGE tras agotar la expectativa de destino o por no obtener reingreso en seis meses tras una suspensión firme; cobra las retribuciones básicas (RD 365/1995, art. 13).", "s11", "Situaciones de la AGE")
T.glos("Suspensión de funciones", "Privación temporal del ejercicio de funciones y de los derechos de la condición de funcionario, firme o provisional (TREBEP, art. 90).", "s12", "Suspensión")
T.glos("Reingreso", "Vuelta al servicio activo desde otra situación; plazos, procedimientos y condiciones por reglamento (TREBEP, art. 91).", "s13", "Reingreso")
T.glos("Autorización de compatibilidad", "Acto previo y expreso que permite desempeñar un segundo puesto o actividad en el sector público (Ley 53/1984, art. 3).", "s16", "Incompatibilidades")
T.glos("Reconocimiento de compatibilidad", "Acto previo que permite ejercer actividades privadas; se resuelve en dos meses (Ley 53/1984, art. 14).", "s17", "Incompatibilidades")
T.glos("Actividades exceptuadas", "Actividades que no están sujetas al régimen de incompatibilidades si cumplen sus requisitos (Ley 53/1984, art. 19).", "s18", "Incompatibilidades")

# Cronología (fechas de los metadatos del BOE)
T.hito("1984", "Ley 30/1984, de 2 de agosto, de medidas para la reforma de la Función Pública (BOE de 3-8-1984)", "Su art. 29 (situaciones) quedó derogado por el TREBEP, salvo el último párrafo de sus apartados 5, 6 y 7", "normativo", "s3")
T.hito("1985", "Ley 53/1984, de 26 de diciembre, de Incompatibilidades del personal al servicio de las Administraciones Públicas (BOE de 4-1-1985)", "Régimen básico de incompatibilidades", "normativo", "s15")
T.hito("1985", "Real Decreto 598/1985, de 30 de abril, sobre incompatibilidades (BOE de 4-5-1985)", "Desarrollo para la Administración del Estado, la Seguridad Social y sus entes", "normativo", "s16")
T.hito("1995", "Real Decreto 365/1995, de 10 de marzo, Reglamento de Situaciones Administrativas de los Funcionarios Civiles de la AGE (BOE de 10-4-1995)", "Situaciones de la AGE: expectativa de destino, excedencia forzosa e incentivada", "normativo", "s3")
T.hito("2015", "Real Decreto Legislativo 5/2015, de 30 de octubre, texto refundido del Estatuto Básico del Empleado Público (BOE de 31-10-2015)", "Arts. 85 a 92: situaciones administrativas", "normativo", "s1")

T.publicar()
