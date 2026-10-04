# -*- coding: utf-8 -*-
"""Tema III.6 (B3T06): Política de inmigración. Régimen de los extranjeros en España.
Derecho de asilo y condición de refugiado.
Método del I.2. Normas (textos consolidados del BOE): CE, arts. 13 y 149.1.2.ª; LO 4/2000
(LOEX); Reglamento de la LO 4/2000 aprobado por RD 1155/2024 (REX, en vigor desde el
20-5-2025; deroga el del RD 557/2011); RD 345/2001 (Observatorio Permanente de la
Inmigración: texto publicado, sin versión consolidada); Ley 12/2009 (ASILO); Convención de
Ginebra de 1951 (REFUG, solo para la pregunta X46).
Lo que no está en una norma (balance del Sistema de Acogida, datos y evolución de la
inmigración) queda como «Pendiente (temario)»: la web del Ministerio de Inclusión
(inclusion.gob.es) devuelve 403 desde este entorno."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO["LOEX"] = "LO 4/2000"
CORTO["ASILO"] = "Ley 12/2009"
CORTO["REX"] = "Reglamento de extranjería, RD 1155/2024"
CORTO["RD345"] = "RD 345/2001"
CORTO["REFUG"] = "Convención de Ginebra de 1951"

T = Tema("B3T06",
  "Tres preguntas: I. Quién dirige la política de inmigración y con qué principios (arts. 13 y 149.1.2.ª CE; LOEX, arts. 1, 2 bis, 2 ter y 67 a 72; RD 345/2001) · II. Qué régimen jurídico tienen los extranjeros en España: derechos, entrada, situaciones, menores, trabajo, infracciones y expulsión (LOEX y Reglamento de 2024) · III. Qué son el derecho de asilo y la condición de refugiado, y cómo se piden (art. 13.4 CE; Ley 12/2009). Cada artículo: texto literal del BOE y ficha.",
  ["LO 4/2000", "Art. 13 CE", "Art. 149.1.2.ª", "Política inmigratoria", "Conferencia Sectorial de Inmigración", "Observatorio Permanente", "Estancia y residencia", "Arraigo", "Menores no acompañados", "Expulsión", "Devolución", "Ley 12/2009", "Refugiado", "Protección subsidiaria", "OAR y CIAR"])

# =============================================================================
T.ap("s0", "Mapa del tema: tres preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque III, tema 6):
> Política de inmigración. Régimen de los extranjeros en España. Derecho de asilo y condición de refugiado.

### El hilo conductor

El epígrafe se lee como **tres preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Constitución | Otras normas |
|---|---|---|---|
| **I** | ¿Quién dirige la política de inmigración y con qué principios? | Arts. 13.1 y 2 y 149.1.2.ª | LO 4/2000, arts. 1, 2 bis, 2 ter y 67 a 72; RD 345/2001, arts. 1, 2 y 4 |
| **II** | ¿Qué régimen jurídico tienen los extranjeros en España? | Art. 13.1 | LO 4/2000, arts. 3 a 62 (selección); Reglamento aprobado por RD 1155/2024 (arraigo y Oficinas de Extranjería) |
| **III** | ¿Qué son el derecho de asilo y la condición de refugiado, y cómo se obtienen? | Art. 13.4 | Ley 12/2009, arts. 1 a 48 (selección) |

!> **La idea que une los tres bloques:** la Constitución reconoce a los extranjeros las libertades del Título I **en los términos de los tratados y la ley** (art. 13) y reserva al **Estado**, en exclusiva, la inmigración, la extranjería y el asilo (art. 149.1.2.ª). La **LO 4/2000** fija la política inmigratoria (I) y el estatuto de los extranjeros (II); la **Ley 12/2009** regula la protección internacional: **asilo** para quien es **refugiado** y **protección subsidiaria** para quien, sin serlo, corre riesgo de **daños graves** (III).

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (de derecho: Titulares · Contenido · Límites · Protección · ⚠ Ojo; de institución o procedimiento: Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo).
- El **Reglamento de extranjería vigente** es el aprobado por el **Real Decreto 1155/2024**: {c('REX', 'dd', 'Quedan derogados el Reglamento de la Ley Orgánica 4/2000, de 11 de enero')} … {c('REX', 'dd', 'aprobado por el Real Decreto 557/2011')} (→ II.7).
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Quién dirige la política de inmigración y con qué principios?", donde(
  "Primera pregunta del tema. Antes del estatuto de los extranjeros hay que saber **qué dice la Constitución**, **quién es competente** y **qué principios** guían la política inmigratoria, y con qué **órganos** se coordina.",
  ["1 La Constitución: los extranjeros (art. 13.1 y 2) y la competencia del Estado (art. 149.1.2.ª)", "2 La política inmigratoria en la LO 4/2000 (arts. 1, 2 bis y 2 ter)", "3 Órganos de coordinación, consulta y estudio (arts. 67 a 72; RD 345/2001)", "4 Datos y evolución de la inmigración (pendiente)"]))

T.ap("s1", "I.1 La Constitución: los extranjeros (art. 13.1 y 2) y la competencia exclusiva del Estado (art. 149.1.2.ª)", f"""
{unidad("1.1 Libertades de los extranjeros y sufragio (art. 13.1 y 2)",
  lit("CE", "Artículo 13", ["en los términos que establezcan los tratados y la ley", "Solamente los españoles serán titulares de los derechos reconocidos en el artículo 23", "en las elecciones municipales"], solo=[1, 2]),
  ficha(f"{c('CE', 'Artículo 13', 'Los extranjeros')}",
        f"Las libertades públicas del Título I, {c('CE', 'Artículo 13', 'en los términos que establezcan los tratados y la ley')}",
        ["Los derechos del art. 23 (participación política y acceso a cargos y funciones públicas) son solo de los españoles", f"Excepción: {c('CE', 'Artículo 13', 'atendiendo a criterios de reciprocidad')}, por tratado o ley, el sufragio activo y pasivo en las **elecciones municipales**"],
        "La de los derechos del Título I (→ desarrollo legal en la LO 4/2000, → II.1)",
        "La única excepción al art. 23 es el sufragio **activo y pasivo** en las **municipales**, por **reciprocidad** y por tratado o ley. Nunca en generales, autonómicas ni europeas por esta vía."))}

{unidad("1.2 Competencia exclusiva del Estado (art. 149.1.2.ª)",
  lit("CE", "Artículo 149", ["El Estado tiene competencia exclusiva sobre las siguientes materias", "Nacionalidad, inmigración, emigración, extranjería y derecho de asilo"], solo=[1, 3]),
  fichab("Título competencial de la inmigración, la extranjería y el asilo",
         c("CE", "Artículo 149", "El Estado"),
         f"{c('CE', 'Artículo 149', 'competencia exclusiva')} sobre cinco materias en una sola regla",
         "—",
         "Las cinco materias de la regla 2.ª: **nacionalidad, inmigración, emigración, extranjería y derecho de asilo**. Es competencia **exclusiva** del Estado, no compartida (cayó en 2025, → Cierre 1). Las CC. AA. intervienen en integración, menores o autorizaciones iniciales de trabajo (→ I.2 y → I.3)."))}
""", 2)

T.ap("s2", "I.2 La política inmigratoria en la LO 4/2000 (arts. 1, 2 bis y 2 ter)", f"""
{unidad("2.1 Quién es extranjero y a quién se aplica la ley (art. 1)",
  lit("LOEX", "a1", ["a los que carezcan de la nacionalidad española", "en aquellos aspectos que pudieran ser más favorables"]),
  fichab("Ámbito subjetivo de la LO 4/2000",
         f"Extranjeros: {c('LOEX', 'a1', 'los que carezcan de la nacionalidad española')}",
         ["Sin perjuicio de las leyes especiales y de los tratados (1.2)", "Los ciudadanos de la UE y quienes tengan el régimen comunitario se rigen por sus normas; la LOEX solo en lo más favorable (1.3)"],
         "—",
         "Extranjero = **quien carece de la nacionalidad española**. A los nacionales de la UE la LOEX solo se les aplica en lo que les sea **más favorable**. Quedan **excluidos** los diplomáticos, cónsules y miembros de misiones y organismos internacionales (art. 2)."))}

{unidad("2.2 Quién define la política de inmigración y con qué principios (art. 2 bis)",
  lit("LOEX", "a2.bis", ["Corresponde al Gobierno", "la definición, planificación, regulación y desarrollo de la política de inmigración", "la coordinación con las políticas definidas por la Unión Europea", "la ordenación de los flujos migratorios laborales, de acuerdo con las necesidades de la situación nacional del empleo", "la lucha contra la inmigración irregular y la persecución del tráfico ilícito de personas", "principio de solidaridad"]),
  fichab("La política inmigratoria y sus principios",
         f"{c('LOEX', 'a2.bis', 'Corresponde al Gobierno')}, {c('LOEX', 'a2.bis', 'sin perjuicio de las competencias que puedan ser asumidas por las Comunidades Autónomas y por las Entidades Locales')}",
         ["::Diez principios para **todas las Administraciones** (2 bis.2):", "a) Coordinación con las políticas de la UE", "b) Ordenación de los flujos laborales según la situación nacional del empleo", "c) Integración social con políticas transversales", "d) Igualdad efectiva entre mujeres y hombres", "e) No discriminación e iguales derechos para quienes vivan o trabajen legalmente", "f) Garantía de los derechos reconocidos a todas las personas", "g) Lucha contra la inmigración irregular y el tráfico ilícito", "h) Persecución de la trata de seres humanos", "i) Igualdad de trato en condiciones laborales y de Seguridad Social", "j) Diálogo y colaboración con países de origen y tránsito"],
         "—",
         "La política la define el **Gobierno** (no las Cortes ni las CC. AA.), «de conformidad con» el art. 149.1.2.ª. El **Estado** garantiza la **solidaridad** con los territorios donde los flujos tienen especial incidencia (2 bis.3)."))}

{unidad("2.3 Integración de los inmigrantes (art. 2 ter)",
  lit("LOEX", "a2.ter", ["sin más límite que el respeto a la Constitución y la ley", "con carácter transversal a todas las políticas y servicios públicos", "plan estratégico plurianual", "programas de acción bienales", "fondo estatal para la integración de los inmigrantes"]),
  fichab("Objetivo transversal de integración",
         "Los poderes públicos y todas las Administraciones; cooperan la AGE, las CC. AA., Ceuta y Melilla y los Ayuntamientos",
         ["Acciones formativas sobre valores constitucionales, estatutarios y de la UE, derechos humanos, democracia, tolerancia e igualdad", "Escolarización obligatoria, lenguas oficiales y acceso al empleo", "Plan estratégico plurianual (incluye la integración de los menores no acompañados)", "Programas de acción bienales acordados en la Conferencia Sectorial de Inmigración, financiados con un fondo estatal"],
         f"Programas de acción {c('LOEX', 'a2.ter', 'bienales')}; fondo estatal {c('LOEX', 'a2.ter', 'que se dotará anualmente')}",
         "Programas **bienales**, fondo **anual**, plan **plurianual**. Los programas se acuerdan en la **Conferencia Sectorial de Inmigración** (→ I.3.2)."))}
""", 2)

EX_X101 = examen("X", 101, {
  "a": f"La Comisión Laboral Tripartita es el órgano colegiado {c('LOEX', 'a72', 'de la que forman parte las organizaciones sindicales y empresariales más representativas')} (art. 72): se informa y consulta, no coordina a las Administraciones.",
  "b": f"El Foro es {c('LOEX', 'a70', 'el órgano de consulta, información y asesoramiento en materia de integración de los inmigrantes')} (art. 70).",
  "c": "No existe en la LO 4/2000 ninguna «Comisión bilateral de Cooperación en materia de Inmigración».",
  "d": f"Literal del art. 68.1: {c('LOEX', 'a68', 'La Conferencia Sectorial de Inmigración es el órgano a través del cual se asegurará la adecuada coordinación de las actuaciones que desarrollen las Administraciones Públicas en materia de inmigración')}."},
  [("Conferencia Sectorial de Inmigración", "LOEX", "a68", "La Conferencia Sectorial de Inmigración es el órgano a través del cual se asegurará la adecuada coordinación")])

EX_L101 = examen("L", 101, {
  "a": "Quince es uno menos: la suma de las letras a) a g) del art. 4.1 da 4 + 1 + 1 + 2 + 4 + 2 + 2 = 16.",
  "b": f"Literal del art. 4.1: {c('RD345', 'a4', 'formarán parte del mismo dieciséis vocales')}.",
  "c": f"Dieciocho no aparece: el número es {c('RD345', 'a4', 'dieciséis vocales')}; el Presidente y el Secretario (que tiene {c('RD345', 'a4', 'voz pero no voto')}) no son vocales.",
  "d": "Diecisiete sería sumar al Presidente; el art. 4.1 cuenta solo los vocales: dieciséis."},
  [("Dieciséis", "RD345", "a4", "formarán parte del mismo dieciséis vocales")])
EX_P34 = examen("P", 34, {
  "a": "Quince es uno menos: la suma de las letras a) a g) del art. 4.1 da 4 + 1 + 1 + 2 + 4 + 2 + 2 = 16.",
  "b": f"Literal del art. 4.1: {c('RD345', 'a4', 'formarán parte del mismo dieciséis vocales')}.",
  "c": f"Dieciocho no aparece: el número es {c('RD345', 'a4', 'dieciséis vocales')}; el Presidente y el Secretario no son vocales.",
  "d": "Diecisiete sería sumar al Presidente; el art. 4.1 cuenta solo los vocales: dieciséis."},
  [("Dieciséis", "RD345", "a4", "formarán parte del mismo dieciséis vocales")])

T.ap("s3", "I.3 Órganos de coordinación, consulta y estudio (LO 4/2000, arts. 67 a 72; RD 345/2001)", f"""
{unidad("3.1 Observación permanente y Oficinas provinciales (art. 67)",
  lit("LOEX", "a67", ["observación permanente de las magnitudes y características más significativas del fenómeno inmigratorio", "Oficinas provinciales"], solo=[1, 2]),
  fichab("Coordinación dentro de la Administración del Estado",
         c("LOEX", "a67", "El Gobierno"),
         ["Observa el fenómeno inmigratorio para dar información objetiva y evitar corrientes xenófobas o racistas", "Unifica en **Oficinas provinciales** los servicios estatales con competencia en inmigración"],
         "—",
         f"Su desarrollo en el Reglamento de 2024 son las **Oficinas de Extranjería**: {c('REX', 'Artículo 258', 'integran los diferentes servicios de la Administración General del Estado competentes en materia de extranjería e inmigración en el ámbito provincial')} (art. 258; → II.7.3)."))}

{unidad("3.2 La Conferencia Sectorial de Inmigración (art. 68)",
  lit("LOEX", "a68", ["La Conferencia Sectorial de Inmigración es el órgano a través del cual se asegurará la adecuada coordinación", "Con carácter previo a la concesión de autorizaciones por arraigo"], solo=[1, 2, 3]),
  fichab("Órgano de coordinación entre Administraciones en materia de inmigración",
         "Conferencia Sectorial de Inmigración (Estado y CC. AA.)",
         ["Coordina las actuaciones de todas las Administraciones (68.1)", "Las CC. AA. con competencias ejecutivas en la autorización inicial de trabajo las ejercen en coordinación con el Estado (68.2)", "Antes de conceder el arraigo, las CC. AA. o los Ayuntamientos emiten un informe sobre la integración social (68.3)"],
         "—",
         "Pregunta de 2025 (→ Cierre 1): la **coordinación** es de la **Conferencia Sectorial**; el **Foro** asesora (70); la **Comisión Laboral Tripartita** es consultada (72)."),
  EX_X101)}

{unidad("3.3 Movimiento asociativo y Foro para la Integración Social de los Inmigrantes (arts. 69 y 70)",
  lit("LOEX", "a70", ["constituido de forma tripartita y equilibrada", "constituye el órgano de consulta, información y asesoramiento en materia de integración de los inmigrantes"]),
  fichab("Órgano de consulta, información y asesoramiento en integración",
         "Representantes de las Administraciones, de las asociaciones de inmigrantes y de otras organizaciones (incluidas las sindicales y empresariales más representativas)",
         f"Composición {c('LOEX', 'a70', 'tripartita y equilibrada')}; composición, competencias y adscripción, por reglamento",
         "—",
         f"Es **consultivo**, no coordinador. Además, los poderes públicos {c('LOEX', 'a69', 'impulsarán el fortalecimiento del movimiento asociativo entre los inmigrantes')} (art. 69)."))}

{unidad("3.4 Observatorio Español del Racismo y la Xenofobia (art. 71)",
  lit("LOEX", "a71", ["con funciones de estudio y análisis"]),
  fichab("Observatorio contra el racismo y la xenofobia",
         "Observatorio Español del Racismo y la Xenofobia",
         f"{c('LOEX', 'a71', 'funciones de estudio y análisis')} y {c('LOEX', 'a71', 'capacidad para elevar propuestas de actuación')}",
         "—",
         "No confundir con el **Observatorio Permanente de la Inmigración** (RD 345/2001, → I.3.6)."))}

{unidad("3.5 Comisión Laboral Tripartita de Inmigración (art. 72)",
  lit("LOEX", "a72", ["adscrito al Ministerio competente en materia de inmigración", "las organizaciones sindicales y empresariales más representativas", "Catálogo de ocupaciones de difícil cobertura", "Mediante Orden Ministerial"]),
  fichab("Órgano colegiado de diálogo social en inmigración",
         "Administración (Ministerio competente en inmigración) y organizaciones sindicales y empresariales más representativas",
         ["Es informada de la evolución de los movimientos migratorios", "Es consultada sobre el Catálogo de ocupaciones de difícil cobertura, la gestión colectiva del art. 39 y la contratación de temporada"],
         f"Composición y funcionamiento: {c('LOEX', 'a72', 'Mediante Orden Ministerial')}",
         "Su régimen se fija por **Orden Ministerial** (el del Foro, «reglamentariamente»)."))}

{unidad("3.6 Observatorio Permanente de la Inmigración: objeto y naturaleza (RD 345/2001, arts. 1 y 2)",
  "*Texto publicado en el BOE en 2001: esta norma no tiene versión consolidada; los nombres de los órganos son los de su publicación.*",
  lit("RD345", "a1", ["órgano colegiado con funciones de recogida de datos, análisis y estudio"], titulo="Artículo 1. Objeto (RD 345/2001)"),
  lit("RD345", "a2", ["se adscribe al Ministerio del Interior"], titulo="Artículo 2. Naturaleza jurídica (RD 345/2001)"),
  fichab("Órgano colegiado de datos y estudio de la realidad inmigratoria",
         "Observatorio Permanente de la Inmigración",
         ["Recoge datos, analiza y estudia la realidad inmigratoria y difunde la información", "Prepara propuestas para canalizar los flujos migratorios y la integración de los residentes extranjeros", f"Elabora {c('RD345', 'a3', 'un informe anual e informes periódicos sobre la realidad inmigratoria')} (art. 3 i)"],
         "—",
         "Según su texto publicado, se adscribe al Ministerio del Interior a través de la Delegación del Gobierno para la Extranjería y la Inmigración."))}

{unidad("3.7 Composición del Observatorio (RD 345/2001, art. 4)",
  lit("RD345", "a4", ["dieciséis vocales", "Cuatro vocales en representación de los Ministerios", "Cuatro vocales en representación de las Comunidades Autónomas", "voz pero no voto"], solo=[1, 2, 3, 4, 5, 6, 7, 8, 9], titulo="Artículo 4. Composición (RD 345/2001)"),
  fichab("Pleno del Observatorio",
         f"Presidente: {c('RD345', 'a4', 'el Delegado del Gobierno para la Extranjería y la Inmigración')}; 16 vocales; un Secretario con voz pero sin voto",
         ["::Vocales (16):", "4 de los Ministerios de la Comisión Interministerial de Extranjería", "1 del INE", "1 del CIS", "2 expertos a propuesta de la Policía (1) y de la Guardia Civil (1)", "4 de las CC. AA. y de Ceuta y Melilla", "2 de las Entidades locales", "2 expertos universitarios"],
         "—",
         "**Dieciséis** vocales (cayó dos veces en 2025, → Cierre 1). El Secretario tiene **voz pero no voto**."),
  EX_L101)}

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Órgano | Norma | Naturaleza | Dato que se pregunta |
|---|---|---|---|
| Conferencia Sectorial de Inmigración | LOEX, art. 68 | **Coordinación** entre Administraciones | Acuerda los programas bienales de integración (2 ter.4) |
| Foro para la Integración Social de los Inmigrantes | LOEX, art. 70 | **Consulta**, información y asesoramiento | Tripartito y equilibrado |
| Observatorio Español del Racismo y la Xenofobia | LOEX, art. 71 | Estudio y análisis; propuestas | Racismo y xenofobia |
| Comisión Laboral Tripartita de Inmigración | LOEX, art. 72 | Diálogo con sindicatos y empresarios | Consultada sobre el Catálogo de ocupaciones de difícil cobertura |
| Observatorio Permanente de la Inmigración | RD 345/2001 | Datos, análisis y estudio | **16 vocales** |
""", 2)

T.ap("s4", "I.4 Datos y evolución de la inmigración (pendiente)", f"""
?> **Pendiente (temario).** El epígrafe «Política de inmigración» suele estudiarse también con **datos**: evolución de la población extranjera, llegadas, balances del Sistema de Acogida… Esos datos **no están en ninguna norma** y no se han podido descargar de una fuente oficial (la web del Ministerio de Inclusión, Seguridad Social y Migraciones no es accesible desde este entorno). Se completará con el **temario** o con la fuente oficial que aporte el usuario. En 2025 cayó una pregunta de este tipo (GACE-X 2025, n.º 39, sobre el balance del Sistema de Acogida Estatal de 2025) que, por eso, **no** se resuelve aquí.

{resumen([
  "Los extranjeros gozan de las libertades del Título I **en los términos de los tratados y la ley**; el art. 23 es solo de españoles, salvo el sufragio **municipal** por **reciprocidad** (art. 13 CE).",
  "Nacionalidad, inmigración, emigración, extranjería y asilo: competencia **exclusiva del Estado** (149.1.2.ª).",
  "La política inmigratoria la define el **Gobierno**, con diez principios para todas las Administraciones (2 bis); la integración es **transversal** (2 ter).",
  "Coordina la **Conferencia Sectorial de Inmigración** (68); asesora el **Foro** (70); el Observatorio Permanente tiene **16 vocales** (RD 345/2001)."],
  "Siguiente: II. ¿Qué régimen jurídico tienen los extranjeros en España?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Qué régimen jurídico tienen los extranjeros en España? (LO 4/2000 y su Reglamento)", donde(
  "Segunda pregunta. Ya sabemos quién dirige la política inmigratoria; ahora, **qué derechos** tienen los extranjeros, **cómo entran**, en qué **situaciones** pueden estar, qué pasa con los **menores no acompañados**, cómo **trabajan** y qué ocurre si **infringen** la ley.",
  ["1 Derechos y libertades (arts. 3 a 22)", "2 Entrada y salida (arts. 25, 25 bis y 28)", "3 Situaciones: estancia y residencia; el arraigo (arts. 29 a 32; Reglamento, arts. 125 y 126)", "4 Menores extranjeros no acompañados (arts. 35, 35 bis y 35 ter)", "5 Autorización de residencia y trabajo (art. 36)", "6 Infracciones, sanciones, expulsión, devolución e internamiento (arts. 51 a 62)", "7 El Reglamento de 2024 y las Oficinas de Extranjería"]))

T.ap("s5", "II.1 Derechos y libertades de los extranjeros (LO 4/2000, arts. 3 a 22)", f"""
La LO 4/2000 distingue derechos de **todos** los extranjeros, de los que **se hallen** en España y de los **residentes**. Esa distinción es lo que se pregunta.

{unidad("1.1 Criterio general: igualdad con los españoles (art. 3)",
  lit("LOEX", "a3", ["en condiciones de igualdad con los españoles", "Declaración Universal de Derechos Humanos"]),
  ficha("Los extranjeros",
        f"Los derechos y libertades del Título I CE {c('LOEX', 'a3', 'en los términos establecidos en los Tratados internacionales, en esta Ley y en las que regulen el ejercicio de cada uno de ellos')}",
        "No puede alegarse la profesión de creencias religiosas o convicciones ideológicas o culturales para justificar actos contrarios a los derechos fundamentales",
        "Interpretación conforme a la Declaración Universal de Derechos Humanos y los tratados vigentes en España",
        "Criterio interpretativo **general**: igualdad con los españoles. Interpretación conforme a la **Declaración Universal**."))}

{unidad("1.2 Documentación (art. 4)",
  lit("LOEX", "a4", ["el derecho y el deber de conservar la documentación", "por un período superior a seis meses", "en el plazo de un mes"], solo=[1, 2, 4]),
  ficha("Los extranjeros que se encuentren en territorio español",
        ["Derecho **y deber** de conservar la documentación de identidad y de su situación en España", "Tarjeta de identidad de extranjero si tienen visado o autorización por más de seis meses"],
        "Exceptuados de la tarjeta: los titulares de un visado de residencia y trabajo de temporada",
        "No pueden ser privados de su documentación salvo en los supuestos de la LOEX y de la Ley de seguridad ciudadana",
        "Tarjeta: estancia **superior a seis meses**; se solicita **personalmente** en el plazo de **un mes**. Incumplirlo es infracción **grave** (art. 53.1 h)."))}

{unidad("1.3 Participación pública (art. 6)",
  lit("LOEX", "a6", ["en las elecciones municipales", "Los Ayuntamientos incorporarán al padrón"], solo=[1, 2, 3]),
  ficha("Los extranjeros **residentes** (sufragio); los empadronados (derechos vecinales)",
        ["Sufragio en las elecciones municipales en los términos de la CE, los tratados y la ley", "Los empadronados tienen los derechos de la legislación de régimen local y pueden ser oídos"],
        "Solo elecciones **municipales** (art. 13.2 CE, → I.1.1)",
        "—",
        "El padrón incorpora a los extranjeros con **domicilio habitual** en el municipio."))}

{unidad("1.4 Educación (art. 9.1)",
  lit("LOEX", "a9", ["menores de dieciséis años", "básica, gratuita y obligatoria", "menores de dieciocho años también tienen derecho a la enseñanza posobligatoria"], solo=[1, 2, 3]),
  ficha("Los extranjeros menores de dieciséis años (básica) y de dieciocho (posobligatoria)",
        ["Enseñanza básica, gratuita y obligatoria", "Titulación y becas en las mismas condiciones que los españoles"],
        "—",
        "Si cumplen dieciocho durante el curso, conservan el derecho hasta su final",
        "Menores de **16**: derecho **y deber** a la educación básica; menores de **18**: también la posobligatoria. No depende de ser residente."))}

{unidad("1.5 Seguridad Social y servicios sociales (art. 14)",
  lit("LOEX", "a14", ["Los extranjeros residentes tienen derecho a acceder a las prestaciones y servicios de la Seguridad Social", "cualquiera que sea su situación administrativa"], solo=[1, 3]),
  ficha("Residentes (Seguridad Social y servicios sociales); todos (servicios sociales básicos)",
        ["Residentes: prestaciones y servicios de la Seguridad Social en las mismas condiciones que los españoles", "Cualquiera que sea su situación administrativa: servicios y prestaciones sociales **básicas**"],
        "—", "—",
        "La Seguridad Social es para **residentes**; los servicios sociales **básicos**, para todos, **cualquiera que sea su situación administrativa**."))}

{unidad("1.6 Familiares reagrupables (art. 17.1)",
  lit("LOEX", "a17", ["En ningún caso podrá reagruparse a más de un cónyuge", "menores de dieciocho años", "mayores de sesenta y cinco años"], solo=[1, 2, 3, 5]),
  ficha("El extranjero **residente** (reagrupante)",
        ["Cónyuge no separado y sin fraude de ley", "Hijos del residente y del cónyuge (incluidos adoptados) menores de 18 o con discapacidad", "Representados legales menores de 18", "Ascendientes en primer grado a cargo, mayores de 65 años y con razones que lo justifiquen"],
        "Nunca más de un cónyuge, aunque la ley personal admita la poligamia",
        f"Requisitos: vivienda adecuada y medios económicos (art. 18.2); se ejerce {c('LOEX', 'a18', 'cuando hayan obtenido la renovación de su autorización de residencia inicial')}",
        "Ascendientes: **mayores de 65** y a cargo; solo desde que el reagrupante tiene la **residencia de larga duración** (18.1). La pareja de hecho acreditada se equipara al cónyuge (17.4)."))}

{unidad("1.7 Asistencia jurídica gratuita (art. 22.1)",
  lit("LOEX", "a22", ["cualquiera que sea la jurisdicción en la que se sigan, en las mismas condiciones que los ciudadanos españoles"], solo=[1]),
  ficha("Los extranjeros que **se hallen** en España",
        "Asistencia jurídica gratuita en todos los procesos en los que sean parte",
        "—",
        f"Asistencia letrada e intérprete en los procedimientos de {c('LOEX', 'a22', 'denegación de entrada, devolución, o expulsión')} y de protección internacional (22.2)",
        "Basta con **hallarse** en España: no hace falta ser residente. Vale en **cualquier jurisdicción**."))}
""", 2)

T.ap("s6", "II.2 Entrada y salida (LO 4/2000, arts. 25, 25 bis y 28)", f"""
{unidad("2.1 Requisitos para la entrada (art. 25)",
  lit("LOEX", "a25", ["por los puestos habilitados al efecto", "será preciso, además, un visado", "a los extranjeros que soliciten acogerse al derecho de asilo en el momento de su entrada en España", "razones excepcionales de índole humanitaria, interés público o cum plimiento de compromisos adquiridos por España"], solo=[1, 2, 3, 4, 5]),
  fichab("Condiciones de entrada en España",
         "El extranjero que pretende entrar; control en los puestos fronterizos",
         ["Puesto habilitado", "Pasaporte o documento de viaje válido", "No estar sujeto a prohibiciones expresas", "Documentos sobre el objeto y condiciones de la estancia y medios de vida suficientes", "Visado, salvo convenios o normativa de la UE (no si tiene tarjeta de identidad de extranjero o autorización de regreso)"],
         "—",
         "No se aplican a quien pide **asilo** en el momento de la entrada (25.3). Puede autorizarse la entrada sin requisitos por razones **humanitarias, de interés público o compromisos de España** (25.4)."))}

{unidad("2.2 Clases de visado (art. 25 bis)",
  lit("LOEX", "a25bis", ["no exceda de tres meses por semestre", "por un período máximo de tres meses", "hasta nueve meses en un período de doce meses consecutivos"], solo=[2, 3, 4, 5, 6, 7, 8, 9]),
  fichab("Siete clases de visado",
         "Misiones Diplomáticas y Oficinas Consulares (art. 27.1)",
         ["Tránsito", "Estancia: hasta tres meses por semestre", "Residencia (sin actividad laboral)", "Residencia y trabajo: entrada y estancia hasta tres meses para empezar la actividad; el alta en la Seguridad Social da eficacia a la autorización", "Residencia y trabajo de temporada: hasta nueve meses en doce", "Estudios", "Investigación"],
         "Estancia: **3 meses por semestre**; temporada: **9 meses en 12**",
         "El visado de residencia y trabajo cobra eficacia con el **alta en la Seguridad Social** dentro de los tres meses."))}

{unidad("2.3 La salida y la salida obligatoria (art. 28)",
  lit("LOEX", "a28", ["podrán realizarse libremente", "el Ministro del Interior podrá prohibir la salida", "La salida será obligatoria"], solo=[1, 2, 3, 4, 5, 6, 7]),
  fichab("Régimen de la salida de España",
         f"El extranjero; excepcionalmente, {c('LOEX', 'a28', 'el Ministro del Interior')} prohíbe la salida",
         ["Libre, salvo en los casos del Código Penal y de la LOEX", "Prohibición excepcional por seguridad nacional o salud pública, siempre individual", "Obligatoria: expulsión judicial o administrativa, devolución, denegación de la permanencia o falta de autorización, fin del plazo de un programa de retorno voluntario"],
         "—",
         "La prohibición de salida es del **Ministro del Interior**, por **seguridad nacional o salud pública**, y con expediente **individual**."))}
""", 2)

T.ap("s7", "II.3 Situaciones: estancia y residencia; el arraigo (LO 4/2000, arts. 29 a 32; Reglamento, arts. 125 y 126)", f"""
{unidad("3.1 Estancia (arts. 29 y 30)",
  lit("LOEX", "a29", ["estancia o residencia"], solo=[1]),
  lit("LOEX", "a30", ["no superior a 90 días", "prórroga de estancia o una autorización de residencia"], solo=[1, 2]),
  fichab("Permanencia de corta duración",
         "El extranjero que entra sin autorización de residencia",
         "Si se quiere permanecer más: prórroga de estancia o autorización de residencia",
         f"Hasta **90 días**; la prórroga con visado {c('LOEX', 'a30', 'en ningún caso podrá ser superior a tres meses, en un período de seis meses')}",
         "Solo hay **dos** situaciones: **estancia** (≤ 90 días) y **residencia** (temporal o de larga duración)."))}

{unidad("3.2 Residencia temporal (arts. 30 bis y 31)",
  lit("LOEX", "a30bis", ["residencia temporal o de residencia de larga duración"], solo=[2]),
  lit("LOEX", "a31", ["por un período superior a 90 días e inferior a cinco años", "situación de arraigo", "En estos supuestos no será exigible el visado", "carezca de antecedentes penales"], solo=[1, 3, 4, 6]),
  fichab("Autorización para permanecer más de 90 días y menos de cinco años",
         "La Administración (Oficinas de Extranjería, → II.7.3)",
         ["Renovable a petición del interesado", "Por arraigo, razones humanitarias, colaboración con la Justicia u otras circunstancias excepcionales: **sin visado** (31.3)", "Requisito: sin antecedentes penales y no figurar como rechazable"],
         "**Más de 90 días y menos de cinco años**",
         "El **arraigo** es una residencia temporal por **circunstancias excepcionales** y **no exige visado** (→ II.3.4)."))}

{unidad("3.3 Residencia de larga duración (art. 32)",
  lit("LOEX", "a32", ["residir y trabajar en España indefinidamente, en las mismas condiciones que los españoles", "durante cinco años de forma continuada", "durante 12 meses consecutivos"], solo=[1, 2, 7, 8, 9, 10, 11]),
  fichab("Residencia indefinida",
         "Quien haya tenido residencia temporal cinco años continuados",
         "Reside y trabaja **indefinidamente** en las mismas condiciones que los españoles",
         ["Requisito: **cinco años** de residencia temporal continuada", "Extinción, entre otras, por ausencia de la UE durante **12 meses consecutivos**"],
         "Cinco años **continuados**; se pierde por **12 meses** fuera **de la UE** (no de España), por fraude, por expulsión o por adquirirla en otro Estado miembro."))}

{unidad("3.4 Tipos de arraigo (Reglamento, art. 125)",
  lit("REX", "Artículo 125", ["arraigo de segunda oportunidad", "arraigo sociolaboral", "arraigo social", "arraigo socioformativo", "arraigo familiar", "La duración de estas autorizaciones es de un año, salvo por razón de arraigo familiar, cuya duración será de cinco años"], titulo="Artículo 125. Tipos de autorización de residencia temporal por razones de arraigo (Reglamento, RD 1155/2024)"),
  fichab("Residencia temporal por vínculos con el lugar de residencia",
         "Extranjeros que se encuentren en España con vínculos económicos, sociales, familiares, laborales o formativos",
         ["Segunda oportunidad", "Sociolaboral", "Social", "Socioformativo", "Familiar"],
         "**Un año**; el familiar, **cinco años**",
         "Son **cinco** tipos en el Reglamento de 2024 (incluido el de **segunda oportunidad**). Duración de **un año**, salvo el **familiar** (**cinco**)."))}

{unidad("3.5 Requisitos generales del arraigo (Reglamento, art. 126)",
  lit("REX", "Artículo 126", ["no tener la condición de solicitante de protección internacional", "durante, al menos, los dos años anteriores", "El arraigo familiar no requerirá ninguna permanencia mínima"], solo=[1, 2, 3, 4, 5, 6], titulo="Artículo 126. Requisitos generales (Reglamento, RD 1155/2024)"),
  fichab("Requisitos comunes a todos los arraigos",
         "La persona extranjera solicitante",
         ["No ser solicitante de protección internacional (al pedirlo ni durante la tramitación)", "Permanencia continuada de dos años (no cuenta el tiempo como solicitante de protección internacional)", "No ser amenaza para el orden público, la seguridad o la salud pública", "Sin antecedentes penales en España ni en los países de residencia de los cinco años anteriores a la entrada", "Además: no rechazable, sin compromiso de no retorno vigente, tasa abonada, sin otra autorización ni procedimiento en curso"],
         "Permanencia mínima de **dos años**; el **familiar**, ninguna",
         "Los requisitos son **acumulativos**. El tiempo como **solicitante de protección internacional** no computa para los dos años."))}
""", 2)

EX_L38 = examen("L", 38, {
  "a": f"Sí lo contiene: art. 35 ter.1 a), {c('LOEX', 'Artículo 35 ter', 'El conjunto de criterios objetivos para la determinación, por el órgano competente de la Administración General del Estado')}.",
  "b": f"Sí lo contiene: art. 35 ter.1 b), {c('LOEX', 'Artículo 35 ter', 'La regulación del mecanismo de derivación')}.",
  "c": f"Sí lo contiene: art. 35 ter.1 c), {c('LOEX', 'Artículo 35 ter', 'Los criterios para la determinación del número de plazas por comunidad autónoma o ciudad autónoma')}.",
  "d": "Es la respuesta: el art. 35 ter.1 enumera solo tres contenidos (criterios de ubicación, mecanismo de derivación y número de plazas); el **análisis de la situación de las familias** no figura."},
  [("análisis de la situación de las familias", "LOEX", "Artículo 35 ter", "El Modelo de gestión de contingencias migratorias extraordinarias para la infancia y la adolescencia migrante no acompañada contendrá")])

T.ap("s8", "II.4 Menores extranjeros no acompañados (LO 4/2000, arts. 35, 35 bis y 35 ter)", f"""
{unidad("4.1 Determinación de la edad, protección y residencia (art. 35.3, 4 y 7)",
  lit("LOEX", "a35", ["poniéndose el hecho en conocimiento inmediato del Ministerio Fiscal, que dispondrá la determinación de su edad", "el Ministerio Fiscal lo pondrá a disposición de los servicios competentes de protección de menores de la Comunidad Autónoma", "Se considerará regular, a todos los efectos, la residencia de los menores que sean tutelados en España"], solo=[3, 4, 8]),
  fichab("Régimen de los menores extranjeros no acompañados",
         "Cuerpos y Fuerzas de Seguridad del Estado (localizan), **Ministerio Fiscal** (edad y puesta a disposición), servicios de protección de menores de la **Comunidad Autónoma** (tutela)",
         ["Atención inmediata por los servicios de protección de menores", "El Fiscal dispone la determinación de la edad, con pruebas prioritarias de las instituciones sanitarias", "Si es menor, se pone a disposición de la protección de menores de la Comunidad Autónoma donde se halle", "Residencia regular de los tutelados; autorización con efectos retroactivos al momento de la puesta a disposición"],
         "—",
         "La edad la determina el **Ministerio Fiscal**. La residencia del menor tutelado es **regular a todos los efectos**. La repatriación la resuelve la **Administración del Estado** (35.5)."))}

{unidad("4.2 Contingencia migratoria extraordinaria (art. 35 bis)",
  lit("LOEX", "Artículo 35 bis", ["La Conferencia Sectorial de Infancia y Adolescencia podrá adoptar mediante Acuerdo por unanimidad", "exceda en ocupación tres veces su capacidad ordinaria", "en un plazo máximo de cinco días naturales"], solo=[1, 3, 4, 5]),
  fichab("Declaración de contingencia y traslado entre comunidades",
         "Conferencia Sectorial de Infancia y Adolescencia (requisitos, Plan y criterios, por unanimidad; si no, los de la ley); el órgano competente de la AGE decide el destino",
         "Se declara cuando el sistema de protección de una comunidad o ciudad autónoma supera en ocupación **tres veces** su capacidad ordinaria",
         f"Declaración {c('LOEX', 'Artículo 35 bis', 'en un plazo máximo de cinco días naturales')} desde la comunicación de la comunidad afectada",
         "**Tres veces** la capacidad ordinaria; **cinco días naturales**; acuerdo por **unanimidad** en la Conferencia Sectorial de **Infancia y Adolescencia** (no la de Inmigración)."))}

{unidad("4.3 Modelo de gestión de contingencias (art. 35 ter.1)",
  lit("LOEX", "Artículo 35 ter", ["contendrá", "El conjunto de criterios objetivos", "La regulación del mecanismo de derivación", "Los criterios para la determinación del número de plazas"], solo=[1, 2, 3, 4]),
  fichab("Contenido del Modelo de gestión",
         "El órgano competente de la Administración General del Estado aplica los criterios",
         ["a) Criterios objetivos de ubicación de los menores en las comunidades o ciudades autónomas", "b) Mecanismo de derivación", "c) Criterios para el número de plazas por comunidad o ciudad autónoma"],
         "A falta de acuerdo unánime, criterios legales de reparto (35 ter.2): 50 % población, 13 % renta, 15 % paro (inversa), 6 % esfuerzo, 10 % dimensionamiento (inversa) y 2 % por cada uno de estos tres: ciudad fronteriza, insularidad y dispersión de la población (total, 100 %)",
         "Son **tres** contenidos. Cayó en 2025 en negativo: el «análisis de la situación de las familias» **no** está (→ Cierre 1)."),
  EX_L38)}
""", 2)

T.ap("s9", "II.5 Autorización de residencia y trabajo (LO 4/2000, art. 36)", f"""
{unidad("5.1 Autorización administrativa previa para residir y trabajar (art. 36)",
  lit("LOEX", "a36", ["Los extranjeros mayores de dieciséis años precisarán", "se condicionará al alta del trabajador en la Seguridad Social", "no invalidará el contrato de trabajo", "no podrá obtener prestaciones por desempleo"], solo=[1, 2, 4, 5]),
  fichab("Autorización para ejercer cualquier actividad lucrativa, laboral o profesional",
         "Extranjeros **mayores de dieciséis años**; para contratar, la solicita **el empleador** con el contrato de trabajo",
         ["La autorización de trabajo se concede **conjuntamente** con la de residencia (salvo penados y supuestos excepcionales)", "La autorización inicial es eficaz con el **alta en la Seguridad Social**", "Su falta no invalida el contrato respecto de los derechos del trabajador, pero no da derecho a prestaciones por desempleo"],
         "—",
         "Mayores de **16**. Contratar sin autorización es infracción **muy grave** del empresario (art. 54.1 d), → II.6.2)."))}
""", 2)

T.ap("s10", "II.6 Infracciones, sanciones, expulsión, devolución e internamiento (LO 4/2000, arts. 51 a 62)", f"""
{unidad("6.1 Infracciones leves y graves (arts. 51 a 53)",
  lit("LOEX", "a51", ["leves, graves y muy graves"], solo=[2]),
  lit("LOEX", "a52", ["El retraso, hasta tres meses, en la solicitud de renovación"], solo=[1, 3]),
  lit("LOEX", "a53", ["Encontrarse irregularmente en territorio español", "Encontrarse trabajando en España sin haber obtenido autorización de trabajo"], solo=[1, 2, 3]),
  fichab("Clasificación y ejemplos de infracciones",
         "Autores y partícipes (51.1)",
         ["Leve: retraso de hasta tres meses en renovar (52 b)", "Grave: estancia irregular (sin prórroga, sin autorización o con ella caducada más de tres meses sin pedir la renovación) (53.1 a)", "Grave: trabajar sin autorización de trabajo y sin residencia válida (53.1 b)"],
         "Retraso en renovar: hasta **3 meses** = leve; caducada **más de 3 meses** sin renovar = grave (estancia irregular)",
         "La **estancia irregular** es infracción **grave** (no muy grave). Su sanción es multa o, en su caso, **expulsión** (57.1)."))}

{unidad("6.2 Infracciones muy graves (art. 54.1)",
  lit("LOEX", "a54", ["Participar en actividades contrarias a la seguridad nacional", "la inmigración clandestina de personas", "La contratación de trabajadores extranjeros sin haber obtenido con carácter previo la correspondiente autorización de residencia y trabajo"], solo=[1, 2, 3, 5]),
  fichab("Las conductas más graves",
         "Extranjeros, empresarios y cualquier persona que promueva la inmigración clandestina",
         ["Actividades contra la seguridad nacional o las relaciones exteriores", "Favorecer con ánimo de lucro la inmigración clandestina (si no es delito)", "Contratar extranjeros sin autorización previa: una infracción por trabajador"],
         "—",
         "En la contratación sin autorización hay **una infracción por cada trabajador**. No es infracción transportar a quien pide protección internacional sin demora y es admitida a trámite (54.3)."))}

{unidad("6.3 Sanciones y órgano competente (art. 55.1 y 2)",
  lit("LOEX", "a55", ["multa de hasta 500 euros", "multa de 501 hasta 10.000 euros", "multa desde 10.001 hasta 100.000 euros", "corresponderá al Subdelegado del Gobierno o al Delegado del Gobierno en las Comunidades Autónomas uniprovinciales"], solo=[1, 2, 3, 4, 5]),
  fichab("Multas y competencia sancionadora",
         f"{c('LOEX', 'a55', 'al Subdelegado del Gobierno o al Delegado del Gobierno en las Comunidades Autónomas uniprovinciales')}",
         ["Leves: hasta 500 €", "Graves: de 501 a 10.000 €", "Muy graves: de 10.001 a 100.000 €"],
         "Graduación por proporcionalidad y capacidad económica del infractor (55.3 y 4)",
         "Sanciona el **Subdelegado** (o el **Delegado** en las uniprovinciales). Las muy graves de seguridad nacional (54.1 a), el **Secretario de Estado de Seguridad**."))}

{unidad("6.4 La expulsión (art. 57)",
  lit("LOEX", "a57", ["en lugar de la sanción de multa", "pena privativa de libertad superior a un año", "En ningún caso podrán imponerse conjuntamente las sanciones de expulsión y multa", "Los residentes de larga duración"], solo=[1, 2, 3, 6, 7, 8, 9, 10]),
  fichab("Sanción de expulsión del territorio",
         "Extranjeros que cometan infracciones muy graves o ciertas graves del 53.1 (a, b, c, d y f), o condenados por delito doloso con pena de más de un año",
         ["En lugar de la multa, por proporcionalidad, con expediente y resolución motivada", "Nunca expulsión y multa a la vez", "Extingue cualquier autorización para permanecer en España"],
         "Delito doloso con pena privativa de libertad **superior a un año** (salvo antecedentes cancelados)",
         "Protegidos (salvo seguridad nacional o reincidencia): nacidos en España con cinco años de residencia legal, **residentes de larga duración**, antiguos españoles de origen y perceptores de ciertas prestaciones (57.5)."))}

{unidad("6.5 Prohibición de entrada y devolución (art. 58)",
  lit("LOEX", "a58", ["su vigencia no excederá de cinco años", "hasta diez años", "Los que habiendo sido expulsados contravengan la prohibición de entrada en España", "Los que pretendan entrar ilegalmente en el país", "en el plazo de 72 horas", "por un plazo máximo de tres años"], solo=[1, 2, 4, 5, 6, 7, 8, 9, 10, 11]),
  fichab("Efectos de la expulsión y devolución sin expediente",
         "La autoridad gubernativa competente para la expulsión acuerda la devolución",
         ["Expulsión → prohibición de entrada (máximo cinco años; hasta diez por amenaza grave)", "Devolución sin expediente de expulsión: expulsados que vuelven y quienes pretenden entrar ilegalmente", "Pedir protección internacional suspende la devolución hasta la inadmisión"],
         "Prohibición: **5 años** (excepcionalmente **10**); devolución: si no se ejecuta en **72 horas**, se pide internamiento al juez; quien pretende entrar ilegalmente: prohibición de hasta **3 años**",
         "La **devolución** no necesita expediente de expulsión. No se devuelve a **embarazadas** si hay riesgo para la gestación o la salud de la madre."))}

{unidad("6.6 Internamiento (art. 62.1, 2 y 4)",
  lit("LOEX", "a62", ["Juez de Instrucción competente", "siendo su duración máxima de 60 días", "No podrá acordarse el ingreso de menores en los centros de internamiento"], solo=[1, 3, 5]),
  fichab("Ingreso en un centro de internamiento durante el expediente de expulsión",
         "Lo solicita el **instructor**; lo acuerda el **Juez de Instrucción** (previa audiencia del interesado y del Fiscal), por auto motivado",
         "Por el tiempo imprescindible para los fines del expediente; no cabe un nuevo internamiento por las mismas causas en el mismo expediente",
         "Máximo **60 días**",
         "**60 días**, decide un **juez** (no la Administración). **Nunca** se interna a **menores** no acompañados."))}
""", 2)

T.ap("s11", "II.7 El Reglamento de 2024 y las Oficinas de Extranjería (RD 1155/2024)", f"""
{unidad("7.1 Aprobación y ámbito (artículo único)",
  lit("REX", "au", ["Se aprueba el Reglamento de la Ley Orgánica 4/2000", "con carácter supletorio"], titulo="Artículo único. Aprobación y ámbito de aplicación del reglamento (RD 1155/2024)"),
  fichab("Aprobación del Reglamento de la LO 4/2000",
         "El Gobierno, por Real Decreto 1155/2024",
         "Aplicación supletoria (o en lo más favorable) a los ciudadanos de la UE y supletoria a los beneficiarios de la Ley 12/2009",
         "—",
         "Supletorio para los ciudadanos de la UE, igual que la ley (art. 1.3 LOEX, → I.2.1)."))}

{unidad("7.2 Entrada en vigor y derogación (disposiciones final cuarta y derogatoria única)",
  lit("REX", "df-4", ["a los 6 meses de su publicación"], titulo="Disposición final cuarta. Entrada en vigor (RD 1155/2024)"),
  lit("REX", "dd", ["aprobado por el Real Decreto 557/2011"], titulo="Disposición derogatoria única. Derogación normativa (RD 1155/2024)"),
  fichab("Sustitución del Reglamento de 2011",
         "—",
         "Deroga el Reglamento aprobado por el RD 557/2011 y lo que se oponga",
         "Vigor: a los **seis meses** de su publicación en el BOE",
         "El Reglamento de 2011 está **derogado**: no citarlo como vigente."))}

{unidad("7.3 Oficinas de Extranjería (Reglamento, arts. 258 y 259)",
  lit("REX", "Artículo 258", ["en el ámbito provincial", "en la capital de las provincias"], solo=[1, 3], titulo="Artículo 258. Creación (Reglamento, RD 1155/2024)"),
  lit("REX", "Artículo 259", ["dependerán orgánicamente de la correspondiente Delegación o Subdelegación del Gobierno", "dependerán funcionalmente del Ministerio de Inclusión, Seguridad Social y Migraciones"], solo=[1], titulo="Artículo 259. Dependencia (Reglamento, RD 1155/2024)"),
  fichab("Unidades provinciales de extranjería",
         "Integran los servicios de la AGE competentes en extranjería e inmigración en cada provincia",
         ["Ubicación: capital de la provincia (excepcionalmente, otra población)", "Funciones (art. 260): tramitación de prórrogas, tarjetas y autorizaciones; procedimientos sancionadores; recursos; NIE; solicitudes de protección internacional y de apatridia; estadística"],
         "—",
         "Dependencia **orgánica**: Delegación o Subdelegación del Gobierno. Dependencia **funcional**: Ministerio de Inclusión (Secretaría de Estado de Migraciones) **y** Ministerio del Interior."))}

{resumen([
  "Derechos: igualdad con los españoles como criterio interpretativo (3); educación hasta **16** básica y **18** posobligatoria (9); Seguridad Social para **residentes**, servicios sociales básicos para **todos** (14); justicia gratuita para quien **se halle** en España (22).",
  "Situaciones: **estancia** (≤ 90 días) y **residencia** temporal (> 90 días y < 5 años) o de **larga duración** (tras **5 años**; se pierde por **12 meses** fuera de la UE).",
  "Arraigo (Reglamento de 2024): **cinco** tipos; **dos años** de permanencia (el familiar, ninguna); dura **un año** (el familiar, **cinco**).",
  "Menores no acompañados: edad → **Fiscal**; contingencia si la ocupación supera **tres veces** la capacidad; el Modelo contiene **tres** cosas (35 ter).",
  "Multas: leves ≤ 500 €; graves 501-10.000 €; muy graves 10.001-100.000 €; sanciona el **Subdelegado**; expulsión **o** multa, nunca las dos; prohibición de entrada ≤ **5 años**; internamiento ≤ **60 días**."],
  "Siguiente: III. ¿Qué son el derecho de asilo y la condición de refugiado?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Qué son el derecho de asilo y la condición de refugiado, y cómo se obtienen? (art. 13.4 CE; Ley 12/2009)", donde(
  "Tercera pregunta. Dentro de los extranjeros hay un grupo con un régimen propio: quienes huyen de persecución o de daños graves. La Constitución remite a la ley (art. 13.4) y la **Ley 12/2009** regula la **protección internacional**: el **asilo** (para el refugiado) y la **protección subsidiaria**.",
  ["1 Fundamento: art. 13.4 CE y Ley 12/2009 (arts. 1 y 2)", "2 Quién es refugiado y quién tiene protección subsidiaria (arts. 3, 4, 5 y 10)", "3 Exclusión y denegación (arts. 8, 9, 11 y 12)", "4 El procedimiento (arts. 16 a 29)", "5 Contenido de la protección, familia, cese y revocación (arts. 36, 40, 42 y 44)", "6 Cuadro comparativo: asilo y protección subsidiaria"]))

EX_X46 = examen("X", 46, {
  "a": f"Ley 12/2009, art. 2: la Convención sobre el Estatuto de los Refugiados fue {c('ASILO', 'a2', 'hecha en Ginebra el 28 de julio de 1951')}.",
  "b": "Cambia el año: es **1951**, no 1961. El Protocolo que la completa es de Nueva York, de 1967.",
  "c": f"Cambia la ciudad: {c('ASILO', 'a2', 'hecha en Ginebra')}, no en Bruselas.",
  "d": "Cambian la ciudad y el año: ni Bruselas ni 1961."},
  [("Ginebra", "ASILO", "a2", "hecha en Ginebra el 28 de julio de 1951"), ("1951", "ASILO", "a2", "hecha en Ginebra el 28 de julio de 1951")])

T.ap("s12", "III.1 Fundamento: art. 13.4 CE y Ley 12/2009 (arts. 1 y 2)", f"""
{unidad("1.1 Reserva de ley del asilo (art. 13.4 CE)",
  lit("CE", "Artículo 13", ["La ley establecerá los términos"], solo=[4]),
  ficha(f"{c('CE', 'Artículo 13', 'los ciudadanos de otros países y los apátridas')}",
        "El derecho de asilo en España",
        "Los términos que establezca la ley (hoy, la Ley 12/2009)",
        "—",
        "El asilo es un derecho **de configuración legal**: la CE remite a **la ley**. Incluye a los **apátridas**."))}

{unidad("1.2 Objeto de la Ley 12/2009 (art. 1)",
  lit("ASILO", "a1", ["nacionales de países no comunitarios y las apátridas", "el derecho de asilo y la protección subsidiaria"]),
  fichab("Ley de protección internacional",
         f"{c('ASILO', 'a1', 'las personas nacionales de países no comunitarios y las apátridas')}",
         "La protección internacional tiene **dos** formas: derecho de **asilo** y **protección subsidiaria**",
         "—",
         "Los nacionales de la UE no están en el ámbito de la ley (y su solicitud se inadmite, art. 20.1 f)."))}

{unidad("1.3 El derecho de asilo (art. 2)",
  lit("ASILO", "a2", ["a quienes se reconozca la condición de refugiado", "hecha en Ginebra el 28 de julio de 1951", "suscrito en Nueva York el 31 de enero de 1967"]),
  fichab("Protección dispensada al refugiado",
         "Nacionales no comunitarios o apátridas reconocidos como refugiados",
         "Según el art. 3 de la ley, la Convención de Ginebra y su Protocolo",
         "Convención: Ginebra, **28-7-1951**; Protocolo: Nueva York, **31-1-1967**",
         "Asilo = protección **del refugiado**. **Ginebra 1951** (cayó en 2025, → Cierre 1) y **Nueva York 1967**."),
  EX_X46)}
""", 2)

T.ap("s13", "III.2 Quién es refugiado y quién tiene protección subsidiaria (Ley 12/2009, arts. 3, 4, 5 y 10)", f"""
{unidad("2.1 La condición de refugiado (art. 3)",
  lit("ASILO", "a3", ["fundados temores de ser perseguida", "raza, religión, nacionalidad, opiniones políticas, pertenencia a determinado grupo social, de género, orientación sexual o de identidad sexual", "se encuentra fuera del país de su nacionalidad"]),
  ficha("Toda persona (o apátrida) con fundados temores de persecución que esté fuera de su país",
        ["::Motivos de persecución:", "Raza", "Religión", "Nacionalidad", "Opiniones políticas", "Pertenencia a determinado grupo social", "Género, orientación sexual o identidad sexual"],
        "No estar incurso en las causas de exclusión (art. 8) ni de denegación o revocación (art. 9) (→ III.3)",
        "Se le reconoce el derecho de asilo (art. 2)",
        "Tres elementos: **temor fundado** de persecución + **motivo** de la lista + estar **fuera** de su país. Los actos de persecución deben ser **graves** o una **acumulación** grave de medidas (art. 6)."))}

{unidad("2.2 La protección subsidiaria (art. 4)",
  lit("ASILO", "a4", ["sin reunir los requisitos para obtener el asilo o ser reconocidas como refugiadas", "riesgo real de sufrir alguno de los daños graves previstos en el artículo 10"]),
  ficha("Personas de otros países y apátridas que no son refugiados",
        "Protección frente al **riesgo real** de sufrir **daños graves** si regresan",
        "No incurrir en las causas de exclusión (art. 11) ni de denegación (art. 12)",
        "Los mismos derechos del art. 36 (→ III.5.1)",
        "Es **subsidiaria**: solo para quien **no** reúne los requisitos del asilo. No exige persecución por un motivo, sino **riesgo real de daño grave**."))}

{unidad("2.3 Qué protege: no devolución (art. 5)",
  lit("ASILO", "a5", ["la no devolución ni expulsión de las personas a quienes se les haya reconocido"]),
  ficha("Refugiados y beneficiarios de protección subsidiaria",
        "No devolución ni expulsión, y las medidas del art. 36",
        "—",
        "Normativa española, de la Unión Europea y convenios internacionales",
        "El núcleo de las dos protecciones es el mismo: **no devolución ni expulsión**."))}

{unidad("2.4 Los daños graves (art. 10)",
  lit("ASILO", "a10", ["la condena a pena de muerte o el riesgo de su ejecución material", "la tortura y los tratos inhumanos o degradantes", "violencia indiscriminada en situaciones de conflicto internacional o interno"]),
  ficha("Solicitantes de protección subsidiaria",
        ["Pena de muerte (condena o riesgo de ejecución)", "Tortura y tratos inhumanos o degradantes en el país de origen", "Amenazas graves contra la vida o integridad de civiles por violencia indiscriminada en conflicto internacional o interno"],
        "—", "—",
        "Son **tres** daños graves. La violencia indiscriminada se refiere a **civiles** y a conflictos **internacionales o internos**."))}
""", 2)

T.ap("s14", "III.3 Exclusión y denegación (Ley 12/2009, arts. 8, 9, 11 y 12)", f"""
{unidad("3.1 Exclusión de la condición de refugiado (art. 8.2)",
  lit("ASILO", "a8", ["un delito contra la paz, un delito de guerra o un delito contra la humanidad", "actos contrarios a las finalidades y a los principios de las Naciones Unidas"], solo=[4, 5, 6, 7]),
  fichab("Personas que no pueden ser refugiadas",
         "Quienes tengan motivos fundados en su contra (y quienes inciten o participen, 8.3)",
         ["Delitos contra la paz, de guerra o contra la humanidad", "Delito grave fuera del país de refugio antes de ser admitidas como refugiadas", "Actos contrarios a los fines y principios de las Naciones Unidas"],
         "—",
         "También se excluye (8.1) a quien ya recibe protección de otro organismo de la ONU distinto del **ACNUR** y a quien tiene derechos equivalentes a la nacionalidad del país donde reside."))}

{unidad("3.2 Denegación del asilo y de la protección subsidiaria (arts. 9, 11.1 d y 12)",
  lit("ASILO", "a9", ["un peligro para la seguridad de España", "condena firme por delito grave constituyan una amenaza para la comunidad"]),
  lit("ASILO", "a11", ["constituyen un peligro para la seguridad interior o exterior de España o para el orden público"], solo=[1, 5]),
  lit("ASILO", "a12", ["la protección subsidiaria se denegará"]),
  fichab("Causas por las que se deniega «en todo caso»",
         "Ministro del Interior, en la resolución (→ III.4.4)",
         ["Peligro, por razones fundadas, para la seguridad de España", "Condena firme por delito grave y amenaza para la comunidad"],
         "—",
         "Las dos causas de denegación son **idénticas** para el asilo (9) y la protección subsidiaria (12). La subsidiaria añade como **exclusión** el peligro para la seguridad interior o exterior **o para el orden público** (11.1 d)."))}
""", 2)

T.ap("s15", "III.4 El procedimiento de protección internacional (Ley 12/2009, arts. 16 a 29)", f"""
{unidad("4.1 Derecho a solicitar y presentación de la solicitud (arts. 16 y 17)",
  lit("ASILO", "a16", ["presentes en territorio español tienen derecho a solicitar protección internacional", "asistencia jurídica gratuita", "tendrá carácter confidencial"], solo=[1, 2, 5]),
  lit("ASILO", "a17", ["mediante comparecencia personal", "en el plazo máximo de un mes desde la entrada en el territorio español", "la entrada ilegal en territorio español no podrá ser sancionada"], solo=[1, 2]),
  fichab("Inicio del procedimiento",
         "Nacionales no comunitarios y apátridas presentes en España; comparecen personalmente (o por representante si hay imposibilidad)",
         ["Asistencia sanitaria, jurídica gratuita e intérprete", "Confidencialidad de toda la información, incluso de la presentación", "Se formaliza en **entrevista personal individual** (17.4)"],
         f"Comparecencia {c('ASILO', 'a17', 'sin demora y en todo caso en el plazo máximo de un mes')} desde la entrada o desde los hechos que justifican el temor",
         "**Un mes**; presentarla fuera de plazo sin motivo es causa de **tramitación de urgencia** (25.1 e). La entrada ilegal **no se sanciona** si la persona reúne los requisitos de protección."))}

{unidad("4.2 Efectos de la solicitud (art. 19.1 y 2)",
  lit("ASILO", "a19", ["no podrá ser objeto de retorno, devolución o expulsión hasta que se resuelva sobre su solicitud o ésta no sea admitida", "suspenderá, hasta la decisión definitiva, la ejecución del fallo de cualquier proceso de extradición"], solo=[1, 2]),
  fichab("Protección provisional del solicitante",
         "El solicitante (derechos del art. 18: documentación, justicia gratuita, comunicación al ACNUR, suspensión de devoluciones…)",
         ["Ni retorno, ni devolución, ni expulsión hasta la resolución o la inadmisión", "Se suspende la ejecución de la extradición"],
         "—",
         "Excepciones: medidas cautelares por **salud o seguridad públicas** y la **orden europea de detención y entrega** (19.3)."))}

{unidad("4.3 No admisión a trámite y solicitudes en frontera (arts. 20.2 y 21)",
  lit("ASILO", "a20", ["en el plazo máximo de un mes contado a partir de la presentación de la solicitud", "determinará la admisión a trámite"], solo=[10]),
  lit("ASILO", "a21", ["en el plazo máximo de cuatro días desde su presentación", "hasta un máximo de diez días", "en el plazo de dos días contados desde su notificación"], solo=[1, 5, 6]),
  fichab("Filtro previo de las solicitudes",
         f"Resuelve {c('ASILO', 'a20', 'El Ministro del Interior, a propuesta de la Oficina de Asilo y Refugio')}",
         ["En territorio: inadmisión por falta de competencia (otro Estado responsable) o de requisitos (art. 20.1)", "En frontera: inadmisión o denegación por resolución motivada; cabe **petición de reexamen**, que suspende sus efectos"],
         ["En territorio: notificar la inadmisión en **un mes** (si no, queda admitida)", "En frontera: **cuatro días** (hasta **diez** si lo pide el ACNUR); reexamen: pedirlo en **dos días** y resolverlo en **dos días**"],
         "1 mes (territorio) / 4 días (frontera) / 10 días (si lo pide el ACNUR) / 2 + 2 días (reexamen). El silencio **favorece** al solicitante: admisión a trámite."))}

{unidad("4.4 Órganos y procedimiento ordinario (arts. 23 y 24)",
  lit("ASILO", "a23", ["La Oficina de Asilo y Refugio, dependiente del Ministerio del Interior", "La Comisión Interministerial de Asilo y Refugio es un órgano colegiado adscrito al Ministerio del Interior"], solo=[1, 2]),
  lit("ASILO", "a24", ["que formulará propuesta al Ministro del Interior", "Transcurridos seis meses desde la presentación de la solicitud sin que se haya notificado la correspondiente resolución, la misma podrá entenderse desestimada"], solo=[2, 3]),
  fichab("Instrucción, propuesta y resolución",
         ["**Oficina de Asilo y Refugio** (OAR, Ministerio del Interior): tramita", "**Comisión Interministerial de Asilo y Refugio** (CIAR): estudia y propone", "**Ministro del Interior**: resuelve"],
         "La CIAR tiene un representante de cada departamento con competencia en política exterior e interior, justicia, inmigración, acogida e igualdad",
         "**Seis meses**: silencio **desestimatorio**",
         "OAR **tramita**, CIAR **propone**, el **Ministro del Interior** **resuelve**. En el procedimiento ordinario el silencio de seis meses es **negativo** (a diferencia de la inadmisión, → III.4.3)."))}

{unidad("4.5 Tramitación de urgencia (art. 25.1 y 4)",
  lit("ASILO", "a25", ["que parezcan manifiestamente fundadas", "especialmente, por menores no acompañados", "salvo en materia de plazos que se verán reducidos a la mitad"], solo=[1, 2, 3, 6, 10]),
  fichab("Procedimiento acelerado",
         "El Ministerio del Interior, de oficio o a petición del interesado; se informa a la CIAR",
         ["Solicitudes manifiestamente fundadas", "Solicitantes con necesidades específicas, especialmente menores no acompañados", "Solicitudes fuera del plazo de un mes sin motivo", "Otros: cuestiones ajenas a la protección, país de origen seguro, causas de exclusión o denegación"],
         "Plazos del procedimiento ordinario **reducidos a la mitad**",
         "La urgencia sirve tanto para lo **manifiestamente fundado** como para lo dudoso; plazos a la **mitad**."))}

{unidad("4.6 Recursos (art. 29.1)",
  lit("ASILO", "a29", ["pondrán fin a la vía administrativa", "recurso de reposición con carácter potestativo"], solo=[1]),
  fichab("Impugnación de las resoluciones",
         "El solicitante",
         "Reposición **potestativa** y recurso contencioso-administrativo",
         "—",
         "Las resoluciones **agotan la vía administrativa**; la reposición es **potestativa**."))}
""", 2)

T.ap("s16", "III.5 Contenido de la protección, familia, cese y revocación (Ley 12/2009, arts. 36, 40, 42 y 44)", f"""
{unidad("5.1 Efectos de la concesión (art. 36.1)",
  lit("ASILO", "a36", ["la protección contra la devolución", "la autorización de residencia y trabajo permanente", "en las mismas condiciones que los españoles"], solo=[1, 2, 4, 5, 6, 7, 9]),
  ficha("Refugiados y beneficiarios de protección subsidiaria",
        ["No devolución", "Autorización de residencia y trabajo **permanente**", "Documentos de identidad y viaje (para el refugiado; para la subsidiaria, cuando sea necesario)", "Servicios públicos de empleo; educación, sanidad, vivienda, asistencia social y Seguridad Social en las mismas condiciones que los españoles", "Libertad de circulación, integración, retorno voluntario y unidad familiar"],
        "—",
        "Derechos de la Convención de Ginebra, de la normativa de extranjería y de la UE",
        "La autorización de residencia y trabajo es **permanente**. Los **documentos de viaje** son para el **refugiado**; al subsidiario, solo «cuando sea necesario»."))}

{unidad("5.2 Extensión familiar (art. 40.1 y 2)",
  lit("ASILO", "a40", ["Los ascendientes en primer grado que acreditasen la dependencia y sus descendientes en primer grado que fueran menores de edad", "El cónyuge o persona ligada por análoga relación de afectividad y convivencia"], solo=[1, 2, 4, 5, 7]),
  fichab("Asilo o protección subsidiaria por extensión familiar",
         "Tramita la OAR; estudia la CIAR; resuelve el Ministro del Interior",
         ["Ascendientes en primer grado dependientes y descendientes en primer grado menores", "Cónyuge o pareja de hecho con convivencia", "Otro adulto responsable si el beneficiario es un menor no casado", "Otros familiares con dependencia y convivencia previa en el país de origen"],
         "—",
         "Exclusiones: **distinta nacionalidad**, divorcio o separación, y la pareja que es la **persecutora** en el asilo por violencia de género."))}

{unidad("5.3 Cese del estatuto de refugiado (art. 42)",
  lit("ASILO", "a42", ["expresamente así lo soliciten", "hayan abandonado el territorio español y fijado su residencia en otro país", "no impedirá la continuación de la residencia en España"], solo=[1, 2, 3, 7, 10]),
  fichab("Fin de la condición de refugiado",
         "Inicia la OAR; si procede, propone la CIAR y resuelve el Ministro del Interior (art. 45)",
         ["Petición expresa", "Volver a acogerse a la protección de su país, recobrar la nacionalidad o adquirir otra con protección", "Establecerse de nuevo en su país", "Fijar la residencia en otro país", "Desaparición de las circunstancias que motivaron el reconocimiento"],
         "Plazo para notificar la resolución de cese o revocación: **seis meses** (art. 45.7)",
         "El cese **no impide seguir residiendo** en España según la normativa de extranjería."))}

{unidad("5.4 Revocación (art. 44.1 y 4)",
  lit("ASILO", "a44", ["concurra alguno de los supuestos de exclusión", "haya tergiversado u omitido hechos, incluido el uso de documentos falsos", "ninguna revocación ni eventual expulsión posterior podrá determinar el envío"], solo=[1, 2, 3, 4, 7]),
  fichab("Retirada del estatuto por causas imputables al beneficiario",
         "Mismo procedimiento que el cese (art. 45)",
         ["Supuestos de exclusión de los arts. 8, 9, 11 y 12", "Tergiversación u omisión de hechos decisivos, incluidos documentos falsos", "Peligro para la seguridad de España o condena firme por delito grave con amenaza para la comunidad"],
         "—",
         "Cese ≠ revocación: el **cese** es porque **ya no hace falta** la protección; la **revocación**, por **causas del beneficiario**. Aun revocada, **nunca** se le envía a un país donde corra peligro."))}
""", 2)

T.ap("s17", "III.6 Cuadro comparativo: asilo y protección subsidiaria (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| | Derecho de asilo | Protección subsidiaria |
|---|---|---|
| Para quién | Refugiado (art. 3) | Quien no es refugiado (art. 4) |
| Qué lo justifica | **Fundados temores de persecución** por raza, religión, nacionalidad, opiniones políticas, grupo social, género, orientación o identidad sexual | **Riesgo real de daños graves**: pena de muerte, tortura o tratos inhumanos, violencia indiscriminada en conflicto (art. 10) |
| Exclusión | Art. 8 | Art. 11 (añade el peligro para el orden público) |
| Denegación | Art. 9 | Art. 12 (mismas causas) |
| Contenido | No devolución + art. 36 | No devolución + art. 36 |
| Documento de viaje | Sí | Cuando sea necesario |
| Fin | Cese (42) o revocación (44) | Cese (43) o revocación (44) |

| Trámite | Plazo (Ley 12/2009) |
|---|---|
| Presentar la solicitud | Un mes desde la entrada (17.2) |
| Inadmisión en territorio | Un mes; si no, admitida (20.2) |
| Inadmisión o denegación en frontera | Cuatro días; hasta diez si lo pide el ACNUR (21.1 a 3) |
| Reexamen en frontera | Pedirlo en dos días; resolverlo en dos días (21.4) |
| Resolución en el procedimiento ordinario | Seis meses; silencio desestimatorio (24.3) |
| Urgencia | Plazos a la mitad (25.4) |

{resumen([
  "Asilo: derecho de **configuración legal** (13.4 CE) para nacionales no comunitarios y **apátridas**; la Convención es de **Ginebra, 1951**, y el Protocolo de **Nueva York, 1967** (Ley 12/2009, art. 2).",
  "Refugiado = **temor fundado de persecución** por un motivo tasado; protección **subsidiaria** = **riesgo real de daño grave** (tres daños del art. 10).",
  "Procedimiento: comparecencia en **un mes**; **OAR** tramita, **CIAR** propone, **Ministro del Interior** resuelve; **seis meses** con silencio negativo; urgencia, plazos a la **mitad**; frontera, **cuatro días**.",
  "Concesión: no devolución y **residencia y trabajo permanente** (36); cese ≠ revocación."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_P33 = examen("P", 33, {
  "a": f"Las Comunidades Autónomas no tienen esta competencia: el art. 149.1 empieza {c('CE', 'Artículo 149', 'El Estado tiene competencia exclusiva sobre las siguientes materias')}.",
  "b": "Los Municipios no tienen competencia sobre nacionalidad, inmigración ni extranjería: es materia del art. 149.1.2.ª.",
  "c": f"Literal del art. 149.1: {c('CE', 'Artículo 149', 'El Estado tiene competencia exclusiva')} sobre {c('CE', 'Artículo 149', 'Nacionalidad, inmigración, emigración, extranjería y derecho de asilo')} (regla 2.ª).",
  "d": "No es compartida: el art. 149.1.2.ª la atribuye al Estado **con carácter exclusivo** (otra cosa es que las CC. AA. asuman algunas competencias, como admite el art. 2 bis.1 LOEX)."},
  [("Estado", "CE", "Artículo 149", "El Estado tiene competencia exclusiva sobre las siguientes materias"), ("exclusivo", "CE", "Artículo 149", "Nacionalidad, inmigración, emigración, extranjería y derecho de asilo")])

T.ap("s18", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **siete** preguntas de este tema. Aquí están **seis**, **literales**: la séptima (GACE-X 2025, n.º 39, balance del Sistema de Acogida Estatal de 2025) pide un dato que **no está en ninguna norma** y queda pendiente (→ I.4). Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-P 2025, pregunta 33 · Competencia exclusiva del Estado (→ I.1.2)", EX_P33,
  "### GACE-X 2025, pregunta 101 · Conferencia Sectorial de Inmigración (→ I.3.2)", EX_X101,
  "### GACE-L 2025, pregunta 101 · Vocales del Observatorio Permanente de la Inmigración (→ I.3.7)", EX_L101,
  "### GACE-P 2025, pregunta 34 · Vocales del Observatorio Permanente de la Inmigración (→ I.3.7)", EX_P34,
  "### GACE-L 2025, pregunta 38 · Modelo de gestión de contingencias migratorias (→ II.4.3)", EX_L38,
  "### GACE-X 2025, pregunta 46 · Convención de Ginebra (→ III.1.3)", EX_X46,
  "### Cómo se pregunta",
  "!> Este tema se pregunta por **órganos** (quién coordina, quién asesora, cuántos vocales), por **normas recientes** (contingencia migratoria de los menores no acompañados, reformada en 2025) y por **datos de identificación** (dónde y cuándo se firmó la Convención). Los distractores cambian el **órgano**, el **número** o la **fecha**.",
]))

T.ap("s19", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Política de inmigración | Art. 13 CE; competencia **exclusiva** del Estado (149.1.2.ª); la define el **Gobierno** con diez principios (2 bis); integración transversal (2 ter); órganos (67 a 72) | **Conferencia Sectorial de Inmigración** coordina (68); Observatorio Permanente: **16 vocales** |
| II. Régimen de los extranjeros | Derechos (3 a 22); entrada y visados (25, 25 bis); estancia y residencia (29 a 32); arraigo (Reglamento 2024); menores (35 a 35 ter); trabajo (36); infracciones y expulsión (51 a 62) | Estancia **≤ 90 días**; larga duración tras **5 años**; internamiento **≤ 60 días**; prohibición de entrada **≤ 5 años** |
| III. Asilo y refugio | Art. 13.4 CE; Ley 12/2009: refugiado (3), subsidiaria (4), daños graves (10), procedimiento (16 a 29), efectos (36) | **Ginebra 1951**; solicitud en **un mes**; OAR tramita, CIAR propone, **Ministro del Interior** resuelve; **seis meses** |

?> **Trampas frecuentes:** «competencia **compartida**» en extranjería (es **exclusiva** del Estado); «el **Foro** coordina» (coordina la **Conferencia Sectorial**; el Foro asesora); «la estancia irregular es **muy grave**» (es **grave**); «expulsión **y** multa» (nunca las dos); «residencia de larga duración tras **tres** años» (son **cinco**); «la Convención de **Bruselas**» o «**1961**» (Ginebra, **1951**); «el silencio en el procedimiento ordinario de asilo es **positivo**» (es **desestimatorio**; el positivo es el de la **admisión a trámite**).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
T.q("CE", "Artículo 149", "Marco constitucional", "Según el artículo 149.1.2.ª de la Constitución, la nacionalidad, inmigración, emigración, extranjería y derecho de asilo son competencia:",
    ["Exclusiva del Estado.", "Compartida entre el Estado y las Comunidades Autónomas.", "De las Comunidades Autónomas, en el marco de la legislación básica estatal.", "Del Estado en la legislación y de las Comunidades Autónomas en la ejecución."],
    "Art. 149.1.2.ª CE.", ["El Estado tiene competencia exclusiva sobre las siguientes materias", "Nacionalidad, inmigración, emigración, extranjería y derecho de asilo"])
T.q("CE", "Artículo 13", "Marco constitucional", "Según el artículo 13.2 de la Constitución, por tratado o ley, atendiendo a criterios de reciprocidad, puede establecerse para los extranjeros el derecho de sufragio activo y pasivo en las elecciones:",
    ["Municipales.", "Generales.", "Autonómicas.", "Municipales, pero solo el sufragio activo."], "Art. 13.2 CE.", "para el derecho de sufragio activo y pasivo en las elecciones municipales")
T.q("CE", "Artículo 13", "Marco constitucional", "Según el artículo 13.4 de la Constitución, los términos en que los ciudadanos de otros países y los apátridas podrán gozar del derecho de asilo en España los establecerá:",
    ["La ley.", "Un tratado internacional.", "El Gobierno, por real decreto.", "La Convención de Ginebra."], "Art. 13.4 CE.", "La ley establecerá los términos en que los ciudadanos de otros países y los apátridas podrán gozar del derecho de asilo en España")
T.q("LOEX", "a1", "Política inmigratoria", "Según el artículo 1.1 de la Ley Orgánica 4/2000, se consideran extranjeros a los efectos de su aplicación:",
    ["Los que carezcan de la nacionalidad española.", "Los que no residan legalmente en España.", "Los nacionales de Estados no miembros de la Unión Europea.", "Los que carezcan de autorización de residencia."], "Art. 1.1 LOEX.", "Se consideran extranjeros, a los efectos de la aplicación de la presente Ley, a los que carezcan de la nacionalidad española")
T.q("LOEX", "a2.bis", "Política inmigratoria", "Según el artículo 2 bis.1 de la Ley Orgánica 4/2000, la definición, planificación, regulación y desarrollo de la política de inmigración corresponde:",
    ["Al Gobierno.", "A las Cortes Generales.", "A la Conferencia Sectorial de Inmigración.", "A las Comunidades Autónomas."], "Art. 2 bis.1 LOEX.", "Corresponde al Gobierno, de conformidad con lo previsto en el artículo 149.1.2.ª de la Constitución, la definición, planificación, regulación y desarrollo de la política de inmigración")
T.q("LOEX", "a2.bis", "Política inmigratoria", "Según el artículo 2 bis.2 de la Ley Orgánica 4/2000, la ordenación de los flujos migratorios laborales se hará de acuerdo con:",
    ["Las necesidades de la situación nacional del empleo.", "Las propuestas de las Comunidades Autónomas.", "Los acuerdos de la Comisión Laboral Tripartita.", "El número de solicitudes presentadas en el año anterior."], "Art. 2 bis.2 b) LOEX.", "la ordenación de los flujos migratorios laborales, de acuerdo con las necesidades de la situación nacional del empleo")
T.q("LOEX", "a2.ter", "Política inmigratoria", "Según el artículo 2 ter.4 de la Ley Orgánica 4/2000, los programas de acción para reforzar la integración social de los inmigrantes que acuerdan el Gobierno y las Comunidades Autónomas en la Conferencia Sectorial de Inmigración son:",
    ["Bienales.", "Anuales.", "Cuatrienales.", "Quinquenales."], "Art. 2 ter.4 LOEX.", "programas de acción bienales para reforzar la integración social de los inmigrantes")
T.q("LOEX", "a70", "Órganos", "Según el artículo 70 de la Ley Orgánica 4/2000, el órgano de consulta, información y asesoramiento en materia de integración de los inmigrantes es:",
    ["El Foro para la Integración Social de los Inmigrantes.", "La Conferencia Sectorial de Inmigración.", "El Observatorio Español del Racismo y la Xenofobia.", "La Comisión Laboral Tripartita de Inmigración."], "Art. 70.1 LOEX.", "constituye el órgano de consulta, información y asesoramiento en materia de integración de los inmigrantes")
T.q("LOEX", "a72", "Órganos", "Según el artículo 72 de la Ley Orgánica 4/2000, la composición y el régimen de funcionamiento de la Comisión Laboral Tripartita de Inmigración se determinarán:",
    ["Mediante Orden Ministerial.", "Mediante Real Decreto.", "Por acuerdo de la Conferencia Sectorial de Inmigración.", "Por ley."], "Art. 72.3 LOEX.", "Mediante Orden Ministerial se determinará su composición")
T.q("RD345", "a4", "Órganos", "Según el artículo 4 del Real Decreto 345/2001, el Observatorio Permanente de la Inmigración está presidido por:",
    ["El Delegado del Gobierno para la Extranjería y la Inmigración.", "El Ministro del Interior.", "El Presidente del Instituto Nacional de Estadística.", "El Secretario de Estado de Seguridad."], "Art. 4.1 RD 345/2001.", "estará presidido por el Delegado del Gobierno para la Extranjería y la Inmigración")
T.q("LOEX", "a4", "Derechos", "Según el artículo 4.2 de la Ley Orgánica 4/2000, la tarjeta de identidad de extranjero se solicitará personalmente en el plazo de:",
    ["Un mes desde la entrada en España o desde que se conceda la autorización.", "Tres meses desde la entrada en España.", "Quince días desde la concesión de la autorización.", "Seis meses desde la entrada en España."], "Art. 4.2 LOEX.", "en el plazo de un mes desde su entrada en España o desde que se conceda la autorización")
T.q("LOEX", "a9", "Derechos", "Según el artículo 9.1 de la Ley Orgánica 4/2000, tienen el derecho y el deber a la educación, que incluye el acceso a una enseñanza básica, gratuita y obligatoria, los extranjeros menores de:",
    ["Dieciséis años.", "Dieciocho años.", "Catorce años.", "Doce años."], "Art. 9.1 LOEX.", "Los extranjeros menores de dieciséis años tienen el derecho y el deber a la educación")
T.q("LOEX", "a14", "Derechos", "Según el artículo 14.3 de la Ley Orgánica 4/2000, los extranjeros, cualquiera que sea su situación administrativa, tienen derecho:",
    ["A los servicios y prestaciones sociales básicas.", "A las prestaciones de la Seguridad Social en las mismas condiciones que los españoles.", "A las ayudas públicas en materia de vivienda.", "A las prestaciones por desempleo."], "Art. 14.3 LOEX.", "Los extranjeros, cualquiera que sea su situación administrativa, tienen derecho a los servicios y prestaciones sociales básicas")
T.q("LOEX", "a17", "Derechos", "Según el artículo 17.1 d) de la Ley Orgánica 4/2000, los ascendientes en primer grado del reagrupante y de su cónyuge pueden ser reagrupados cuando estén a su cargo y sean mayores de:",
    ["Sesenta y cinco años.", "Sesenta años.", "Setenta años.", "Sesenta y siete años."], "Art. 17.1 d) LOEX.", "sean mayores de sesenta y cinco años")
T.q("LOEX", "a22", "Derechos", "Según el artículo 22.1 de la Ley Orgánica 4/2000, tienen derecho a la asistencia jurídica gratuita en los procesos en que sean parte, en las mismas condiciones que los españoles:",
    ["Los extranjeros que se hallen en España, cualquiera que sea la jurisdicción.", "Solo los extranjeros residentes, en la jurisdicción contencioso-administrativa.", "Solo los residentes de larga duración.", "Los extranjeros que se hallen en España, solo en el orden penal."], "Art. 22.1 LOEX.", "Los extranjeros que se hallen en España tienen derecho a la asistencia jurídica gratuita en los procesos en los que sean parte, cualquiera que sea la jurisdicción")
T.q("LOEX", "a25bis", "Entrada", "Según el artículo 25 bis.2 e) de la Ley Orgánica 4/2000, el visado de residencia y trabajo de temporada habilita para trabajar por cuenta ajena hasta:",
    ["Nueve meses en un período de doce meses consecutivos.", "Seis meses en un período de doce meses consecutivos.", "Tres meses por semestre.", "Doce meses en un período de dieciocho meses."], "Art. 25 bis.2 e) LOEX.", "hasta nueve meses en un período de doce meses consecutivos")
T.q("LOEX", "a28", "Entrada", "Según el artículo 28.2 de la Ley Orgánica 4/2000, ¿quién puede prohibir excepcionalmente la salida del territorio español por razones de seguridad nacional o de salud pública?",
    ["El Ministro del Interior.", "El Juez de Instrucción.", "El Delegado del Gobierno.", "El Consejo de Ministros."], "Art. 28.2 LOEX.", "Excepcionalmente, el Ministro del Interior podrá prohibir la salida del territorio español por razones de seguridad nacional o de salud pública")
T.q("LOEX", "a30", "Situaciones", "Según el artículo 30.1 de la Ley Orgánica 4/2000, la estancia es la permanencia en territorio español por un período de tiempo no superior a:",
    ["90 días.", "Seis meses.", "30 días.", "Un año."], "Art. 30.1 LOEX.", "Estancia es la permanencia en territorio español por un período de tiempo no superior a 90 días")
T.q("LOEX", "a31", "Situaciones", "Según el artículo 31.1 de la Ley Orgánica 4/2000, la residencia temporal es la situación que autoriza a permanecer en España por un período:",
    ["Superior a 90 días e inferior a cinco años.", "Superior a seis meses e inferior a tres años.", "Superior a 90 días e inferior a diez años.", "Superior a un año e inferior a cinco años."], "Art. 31.1 LOEX.", "La residencia temporal es la situación que autoriza a permanecer en España por un período superior a 90 días e inferior a cinco años")
T.q("LOEX", "a32", "Situaciones", "Según el artículo 32.2 de la Ley Orgánica 4/2000, tendrán derecho a residencia de larga duración los que hayan tenido residencia temporal en España de forma continuada durante:",
    ["Cinco años.", "Tres años.", "Diez años.", "Dos años."], "Art. 32.2 LOEX.", "los que hayan tenido residencia temporal en España durante cinco años de forma continuada")
T.q("LOEX", "a32", "Situaciones", "Según el artículo 32.5 c) de la Ley Orgánica 4/2000, la residencia de larga duración se extingue cuando se produzca la ausencia del territorio de la Unión Europea durante:",
    ["12 meses consecutivos.", "6 meses consecutivos.", "24 meses consecutivos.", "12 meses en un período de dos años."], "Art. 32.5 c) LOEX.", "Cuando se produzca la ausencia del territorio de la Unión Europea durante 12 meses consecutivos")
T.q("REX", "Artículo 125", "Situaciones", "Según el artículo 125.2 del Reglamento de la Ley Orgánica 4/2000 aprobado por el Real Decreto 1155/2024, la autorización de residencia temporal por arraigo familiar tiene una duración de:",
    ["Cinco años.", "Un año.", "Dos años.", "Tres años."], "Art. 125.2 del Reglamento: un año, salvo el arraigo familiar, de cinco años.", "salvo por razón de arraigo familiar, cuya duración será de cinco años")
T.q("REX", "Artículo 126", "Situaciones", "Según el artículo 126 b) del Reglamento de la Ley Orgánica 4/2000 aprobado por el Real Decreto 1155/2024, para el arraigo es requisito general haber permanecido en territorio nacional de forma continuada, al menos, durante:",
    ["Los dos años anteriores a la presentación de la solicitud.", "Los tres años anteriores a la presentación de la solicitud.", "El año anterior a la presentación de la solicitud.", "Los cinco años anteriores a la presentación de la solicitud."], "Art. 126 b) del Reglamento (el arraigo familiar no exige permanencia mínima).", "durante, al menos, los dos años anteriores a la presentación de dicha solicitud")
T.q("LOEX", "Artículo 35 bis", "Menores no acompañados", "Según el artículo 35 bis.2 de la Ley Orgánica 4/2000, se declarará la situación de contingencia migratoria extraordinaria en las comunidades o ciudades autónomas cuyo sistema de protección de personas menores extranjeras no acompañadas exceda en ocupación:",
    ["Tres veces su capacidad ordinaria.", "Dos veces su capacidad ordinaria.", "El 150 por ciento de su capacidad ordinaria.", "Cuatro veces su capacidad ordinaria."], "Art. 35 bis.2 LOEX.", "exceda en ocupación tres veces su capacidad ordinaria")
T.q("LOEX", "a35", "Menores no acompañados", "Según el artículo 35.3 de la Ley Orgánica 4/2000, cuando no pueda establecerse con seguridad la minoría de edad de un extranjero indocumentado, dispondrá la determinación de su edad:",
    ["El Ministerio Fiscal.", "El Juez de Menores.", "La Delegación del Gobierno.", "La entidad pública de protección de menores."], "Art. 35.3 LOEX.", "poniéndose el hecho en conocimiento inmediato del Ministerio Fiscal, que dispondrá la determinación de su edad")
T.q("LOEX", "a36", "Trabajo", "Según el artículo 36.1 de la Ley Orgánica 4/2000, precisan autorización administrativa previa para residir y trabajar, para ejercer cualquier actividad lucrativa, laboral o profesional, los extranjeros mayores de:",
    ["Dieciséis años.", "Dieciocho años.", "Catorce años.", "Veintiún años."], "Art. 36.1 LOEX.", "Los extranjeros mayores de dieciséis años precisarán, para ejercer cualquier actividad lucrativa, laboral o profesional")
T.q("LOEX", "a53", "Infracciones", "Según la Ley Orgánica 4/2000, encontrarse irregularmente en territorio español por carecer de autorización de residencia es una infracción:",
    ["Grave.", "Leve.", "Muy grave.", "No es infracción administrativa."], "Art. 53.1 a) LOEX.", "Encontrarse irregularmente en territorio español, por no haber obtenido la prórroga de estancia, carecer de autorización de residencia")
T.q("LOEX", "a55", "Infracciones", "Según el artículo 55.1 de la Ley Orgánica 4/2000, las infracciones graves se sancionan con multa:",
    ["De 501 hasta 10.000 euros.", "De hasta 500 euros.", "Desde 10.001 hasta 100.000 euros.", "De 1.001 hasta 50.000 euros."], "Art. 55.1 b) LOEX.", "Las infracciones graves con multa de 501 hasta 10.000 euros")
T.q("LOEX", "a55", "Infracciones", "Según el artículo 55.2 de la Ley Orgánica 4/2000, con carácter general, la imposición de las sanciones por las infracciones administrativas de esa ley corresponde:",
    ["Al Subdelegado del Gobierno o al Delegado del Gobierno en las Comunidades Autónomas uniprovinciales.", "Al Ministro del Interior.", "Al Secretario de Estado de Migraciones.", "A la Inspección de Trabajo y Seguridad Social."], "Art. 55.2 LOEX.", "corresponderá al Subdelegado del Gobierno o al Delegado del Gobierno en las Comunidades Autónomas uniprovinciales")
T.q("LOEX", "a57", "Expulsión", "Según el artículo 57.3 de la Ley Orgánica 4/2000, las sanciones de expulsión y multa:",
    ["En ningún caso podrán imponerse conjuntamente.", "Se impondrán siempre conjuntamente en las infracciones muy graves.", "Podrán imponerse conjuntamente si hay reincidencia.", "Podrán imponerse conjuntamente a los residentes de larga duración."], "Art. 57.3 LOEX.", "En ningún caso podrán imponerse conjuntamente las sanciones de expulsión y multa")
T.q("LOEX", "a58", "Expulsión", "Según el artículo 58.1 de la Ley Orgánica 4/2000, con carácter general, la vigencia de la prohibición de entrada que lleva consigo la expulsión no excederá de:",
    ["Cinco años.", "Tres años.", "Diez años.", "Dos años."], "Art. 58.1 LOEX (hasta diez años, excepcionalmente, por amenaza grave: 58.2).", "su vigencia no excederá de cinco años")
T.q("LOEX", "a62", "Expulsión", "Según el artículo 62.2 de la Ley Orgánica 4/2000, la duración máxima del internamiento en un centro de internamiento de extranjeros es de:",
    ["60 días.", "40 días.", "72 horas.", "90 días."], "Art. 62.2 LOEX.", "siendo su duración máxima de 60 días")
T.q("REX", "Artículo 259", "Reglamento", "Según el artículo 259 del Reglamento de la Ley Orgánica 4/2000 aprobado por el Real Decreto 1155/2024, las Oficinas de Extranjería dependen orgánicamente:",
    ["De la correspondiente Delegación o Subdelegación del Gobierno.", "Del Ministerio del Interior.", "De la Secretaría de Estado de Migraciones.", "De la Comunidad Autónoma."], "Art. 259.1 del Reglamento.", "dependerán orgánicamente de la correspondiente Delegación o Subdelegación del Gobierno")
T.q("ASILO", "a2", "Asilo", "Según el artículo 2 de la Ley 12/2009, el Protocolo de la Convención sobre el Estatuto de los Refugiados fue suscrito en:",
    ["Nueva York el 31 de enero de 1967.", "Ginebra el 28 de julio de 1951.", "Nueva York el 28 de julio de 1951.", "Ginebra el 31 de enero de 1967."], "Art. 2 Ley 12/2009.", "y su Protocolo, suscrito en Nueva York el 31 de enero de 1967")
T.q("ASILO", "a10", "Protección subsidiaria", "Según el artículo 10 de la Ley 12/2009, ¿cuál de los siguientes es uno de los daños graves que dan lugar a la protección subsidiaria?",
    ["La condena a pena de muerte o el riesgo de su ejecución material.", "La falta de empleo en el país de origen.", "La persecución por motivos de opiniones políticas.", "La carencia de vivienda en el país de origen."], "Art. 10 a) Ley 12/2009. La persecución por opiniones políticas es motivo de la condición de refugiado (art. 3), no un daño grave.", "la condena a pena de muerte o el riesgo de su ejecución material")
T.q("ASILO", "a9", "Asilo", "Según el artículo 9 de la Ley 12/2009, el derecho de asilo se denegará en todo caso a las personas que:",
    ["Constituyan, por razones fundadas, un peligro para la seguridad de España.", "Hayan entrado ilegalmente en territorio español.", "Presenten su solicitud fuera de plazo.", "Procedan de un país de origen seguro."], "Art. 9 a) Ley 12/2009. La entrada ilegal no se sanciona (17.2) y el plazo y el país seguro son causas de urgencia (25.1).", "las personas que constituyan, por razones fundadas, un peligro para la seguridad de España")
T.q("ASILO", "a17", "Procedimiento de asilo", "Según el artículo 17.2 de la Ley 12/2009, la comparecencia para solicitar protección internacional deberá realizarse sin demora y en todo caso en el plazo máximo de:",
    ["Un mes desde la entrada en el territorio español.", "Quince días desde la entrada en el territorio español.", "Tres meses desde la entrada en el territorio español.", "Seis meses desde la entrada en el territorio español."], "Art. 17.2 Ley 12/2009.", "en el plazo máximo de un mes desde la entrada en el territorio español")
T.q("ASILO", "a21", "Procedimiento de asilo", "Según el artículo 21.1 de la Ley 12/2009, la resolución de no admisión a trámite de una solicitud de protección internacional presentada en un puesto fronterizo deberá notificarse en el plazo máximo de:",
    ["Cuatro días desde su presentación.", "Dos días desde su presentación.", "Un mes desde su presentación.", "Diez días desde su presentación."], "Art. 21.1 Ley 12/2009 (ampliable hasta diez días si lo solicita el ACNUR, 21.3).", "deberá ser notificada a la persona interesada en el plazo máximo de cuatro días desde su presentación")
T.q("ASILO", "a23", "Procedimiento de asilo", "Según el artículo 23.1 de la Ley 12/2009, el órgano competente para la tramitación de las solicitudes de protección internacional es:",
    ["La Oficina de Asilo y Refugio, dependiente del Ministerio del Interior.", "La Comisión Interministerial de Asilo y Refugio.", "La Secretaría de Estado de Migraciones.", "El Alto Comisionado de las Naciones Unidas para los Refugiados."], "Art. 23.1 Ley 12/2009.", "La Oficina de Asilo y Refugio, dependiente del Ministerio del Interior, es el órgano competente para la tramitación")
T.q("ASILO", "a24", "Procedimiento de asilo", "Según el artículo 24 de la Ley 12/2009, ¿quién es competente para dictar la resolución que concede o deniega el derecho de asilo o la protección subsidiaria?",
    ["El Ministro del Interior, a propuesta de la Comisión Interministerial de Asilo y Refugio.", "La Comisión Interministerial de Asilo y Refugio.", "La Oficina de Asilo y Refugio.", "El Consejo de Ministros, a propuesta del Ministro de Asuntos Exteriores."], "Art. 24.2 Ley 12/2009.", "que formulará propuesta al Ministro del Interior, quien será el competente para dictar la correspondiente resolución")
T.q("ASILO", "a24", "Procedimiento de asilo", "Según el artículo 24.3 de la Ley 12/2009, transcurridos seis meses desde la presentación de la solicitud sin que se haya notificado la resolución, la solicitud:",
    ["Podrá entenderse desestimada.", "Se entenderá estimada.", "Se tendrá por desistida.", "Se tramitará por el procedimiento de urgencia."], "Art. 24.3 Ley 12/2009: silencio desestimatorio.", "la misma podrá entenderse desestimada")
T.q("ASILO", "a25", "Procedimiento de asilo", "Según el artículo 25.4 de la Ley 12/2009, en la tramitación de urgencia los plazos del procedimiento ordinario:",
    ["Se reducen a la mitad.", "Se reducen a la tercera parte.", "Se mantienen, pero el expediente tiene preferencia.", "Se reducen a quince días."], "Art. 25.4 Ley 12/2009.", "salvo en materia de plazos que se verán reducidos a la mitad")
T.q("ASILO", "a36", "Efectos de la protección", "Según el artículo 36.1 c) de la Ley 12/2009, la concesión del derecho de asilo o de la protección subsidiaria implica:",
    ["La autorización de residencia y trabajo permanente.", "Una autorización de residencia temporal de cinco años.", "La adquisición de la nacionalidad española por residencia.", "Una autorización de estancia renovable cada año."], "Art. 36.1 c) Ley 12/2009.", "la autorización de residencia y trabajo permanente")
T.real("P", 33, "Marco constitucional"); T.real("X", 101, "Órganos"); T.real("L", 101, "Órganos"); T.real("P", 34, "Órganos")
T.real("L", 38, "Menores no acompañados"); T.real("X", 46, "Asilo")

# Flashcards
for q_, a_, cat in [
  ("¿De qué libertades gozan los extranjeros según el art. 13.1 CE?", "De las libertades públicas del Título I, en los términos que establezcan los tratados y la ley.", "Marco constitucional"),
  ("Excepción al art. 23 CE para los extranjeros (art. 13.2)", "Sufragio activo y pasivo en las elecciones municipales, por reciprocidad, por tratado o ley.", "Marco constitucional"),
  ("¿Qué materias reúne el art. 149.1.2.ª CE?", "Nacionalidad, inmigración, emigración, extranjería y derecho de asilo: competencia exclusiva del Estado.", "Marco constitucional"),
  ("¿Quién define la política de inmigración? (LOEX 2 bis.1)", "El Gobierno, sin perjuicio de las competencias que asuman CC. AA. y Entidades Locales.", "Política inmigratoria"),
  ("Órgano de coordinación de las Administraciones en inmigración (LOEX 68)", "La Conferencia Sectorial de Inmigración.", "Órganos"),
  ("Foro para la Integración Social de los Inmigrantes (LOEX 70)", "Órgano tripartito de consulta, información y asesoramiento en integración.", "Órganos"),
  ("Vocales del Observatorio Permanente de la Inmigración (RD 345/2001, art. 4)", "Dieciséis; lo preside el Delegado del Gobierno para la Extranjería y la Inmigración.", "Órganos"),
  ("Estancia (LOEX 30)", "Permanencia no superior a 90 días.", "Situaciones"),
  ("Residencia temporal (LOEX 31)", "Más de 90 días y menos de cinco años; por arraigo y otras circunstancias excepcionales no se exige visado.", "Situaciones"),
  ("Residencia de larga duración (LOEX 32)", "Residir y trabajar indefinidamente como los españoles, tras cinco años continuados de residencia temporal; se extingue por 12 meses consecutivos fuera de la UE.", "Situaciones"),
  ("Tipos de arraigo del Reglamento de 2024 (art. 125)", "Segunda oportunidad, sociolaboral, social, socioformativo y familiar; un año (el familiar, cinco).", "Situaciones"),
  ("Contingencia migratoria de menores no acompañados (LOEX 35 bis)", "Cuando la ocupación del sistema de protección supera tres veces la capacidad ordinaria; declaración en cinco días naturales.", "Menores no acompañados"),
  ("Multas de la LOEX (art. 55.1)", "Leves hasta 500 €; graves de 501 a 10.000 €; muy graves de 10.001 a 100.000 €.", "Infracciones"),
  ("¿Expulsión y multa a la vez? (LOEX 57.3)", "En ningún caso.", "Expulsión"),
  ("Prohibición de entrada por expulsión (LOEX 58)", "Hasta cinco años; excepcionalmente hasta diez por amenaza grave.", "Expulsión"),
  ("Duración máxima del internamiento (LOEX 62.2)", "60 días; lo acuerda el Juez de Instrucción; nunca menores.", "Expulsión"),
  ("Convención sobre el Estatuto de los Refugiados", "Hecha en Ginebra el 28 de julio de 1951; Protocolo de Nueva York de 31 de enero de 1967 (Ley 12/2009, art. 2).", "Asilo"),
  ("Motivos de persecución del refugiado (Ley 12/2009, art. 3)", "Raza, religión, nacionalidad, opiniones políticas, pertenencia a determinado grupo social, de género, orientación sexual o identidad sexual.", "Asilo"),
  ("Daños graves de la protección subsidiaria (Ley 12/2009, art. 10)", "Pena de muerte; tortura y tratos inhumanos o degradantes; amenazas graves contra civiles por violencia indiscriminada en conflicto.", "Protección subsidiaria"),
  ("Plazo para solicitar protección internacional (Ley 12/2009, art. 17.2)", "Sin demora y como máximo un mes desde la entrada o desde los hechos.", "Procedimiento de asilo"),
  ("OAR, CIAR y Ministro del Interior (Ley 12/2009, arts. 23 y 24)", "La OAR tramita, la CIAR propone y el Ministro del Interior resuelve; seis meses, silencio desestimatorio.", "Procedimiento de asilo"),
  ("Solicitudes en frontera (Ley 12/2009, art. 21)", "Inadmisión o denegación en cuatro días (hasta diez si lo pide el ACNUR); reexamen en dos días.", "Procedimiento de asilo"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Extranjero", "Quien carece de la nacionalidad española (LO 4/2000, art. 1.1).", "s2", "Política inmigratoria")
T.glos("Conferencia Sectorial de Inmigración", "Órgano a través del cual se asegura la coordinación de las actuaciones de las Administraciones Públicas en materia de inmigración (LO 4/2000, art. 68.1).", "s3", "Órganos")
T.glos("Observatorio Permanente de la Inmigración", "Órgano colegiado de recogida de datos, análisis y estudio de la realidad inmigratoria; 16 vocales (RD 345/2001).", "s3", "Órganos")
T.glos("Estancia", "Permanencia en España por un período no superior a 90 días (LO 4/2000, art. 30.1).", "s7", "Situaciones")
T.glos("Residencia temporal", "Situación que autoriza a permanecer en España más de 90 días y menos de cinco años (LO 4/2000, art. 31.1).", "s7", "Situaciones")
T.glos("Residencia de larga duración", "Situación que autoriza a residir y trabajar en España indefinidamente en las mismas condiciones que los españoles (LO 4/2000, art. 32.1).", "s7", "Situaciones")
T.glos("Arraigo", "Autorización de residencia temporal por vínculos económicos, sociales, familiares, laborales o formativos con el lugar de residencia (Reglamento de 2024, art. 125).", "s7", "Situaciones")
T.glos("Contingencia migratoria extraordinaria", "Situación declarada cuando el sistema de protección de menores extranjeros no acompañados de una comunidad o ciudad autónoma supera en ocupación tres veces su capacidad ordinaria (LO 4/2000, art. 35 bis).", "s8", "Menores no acompañados")
T.glos("Devolución", "Salida forzosa sin expediente de expulsión de quien vuelve contraviniendo una prohibición de entrada o pretende entrar ilegalmente (LO 4/2000, art. 58.3).", "s10", "Expulsión")
T.glos("Oficina de Extranjería", "Unidad provincial que integra los servicios de la AGE competentes en extranjería e inmigración (Reglamento de 2024, art. 258).", "s11", "Reglamento")
T.glos("Derecho de asilo", "Protección dispensada a nacionales no comunitarios o apátridas a quienes se reconozca la condición de refugiado (Ley 12/2009, art. 2).", "s12", "Asilo")
T.glos("Refugiado", "Persona que, por fundados temores de persecución por los motivos del art. 3 de la Ley 12/2009, está fuera de su país y no puede o no quiere acogerse a su protección.", "s13", "Asilo")
T.glos("Protección subsidiaria", "Protección de quien, sin ser refugiado, corre un riesgo real de sufrir daños graves si regresa a su país (Ley 12/2009, art. 4).", "s13", "Protección subsidiaria")
T.glos("Oficina de Asilo y Refugio (OAR)", "Órgano del Ministerio del Interior competente para tramitar las solicitudes de protección internacional (Ley 12/2009, art. 23.1).", "s15", "Procedimiento de asilo")
T.glos("Comisión Interministerial de Asilo y Refugio (CIAR)", "Órgano colegiado adscrito al Ministerio del Interior que estudia los expedientes y formula propuesta al Ministro (Ley 12/2009, arts. 23.2 y 24.2).", "s15", "Procedimiento de asilo")

# Cronología (fechas de los metadatos del BOE)
T.hito("1951", "Convención sobre el Estatuto de los Refugiados, hecha en Ginebra el 28-7-1951 (Instrumento de Adhesión de España: BOE de 21-10-1978)", "Definición internacional de refugiado", "normativo", "s12")
T.hito("1978", "Constitución Española (27-12-1978; BOE de 29-12-1978)", "Arts. 13 y 149.1.2.ª: extranjeros, asilo y competencia exclusiva del Estado", "normativo", "s1")
T.hito("2000", "Ley Orgánica 4/2000, de 11 de enero, sobre derechos y libertades de los extranjeros en España y su integración social (BOE de 12-1-2000; vigente desde el 1-2-2000)", "Régimen general de la extranjería", "normativo", "s2")
T.hito("2001", "Real Decreto 345/2001, de 4 de abril, por el que se regula el Observatorio Permanente de la Inmigración (BOE de 6-4-2001)", "Observatorio: 16 vocales", "normativo", "s3")
T.hito("2009", "Ley 12/2009, de 30 de octubre, reguladora del derecho de asilo y de la protección subsidiaria (BOE de 31-10-2009; vigente desde el 20-11-2009)", "Asilo y protección subsidiaria", "normativo", "s12")
T.hito("2024", "Real Decreto 1155/2024, de 19 de noviembre, Reglamento de la LO 4/2000 (BOE de 20-11-2024; vigente desde el 20-5-2025)", "Deroga el Reglamento de 2011; arraigos y Oficinas de Extranjería", "normativo", "s11")

T.publicar()
