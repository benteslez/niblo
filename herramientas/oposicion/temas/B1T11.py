# -*- coding: utf-8 -*-
"""Tema I.11 (B1T11): Organización territorial (II): la Administración local: entidades que
la integran. La autonomía local. El municipio: organización y competencias. La provincia:
organización y competencias.
Método del I.2. Normas (textos consolidados del BOE): CE, arts. 137 y 140 a 142; Ley 7/1985,
Reguladora de las Bases del Régimen Local (LRBRL), arts. 1 a 44 y 121; Carta Europea de
Autonomía Local (BOE-A-1989-4370), arts. 3 y 4; LOTC, arts. 75 bis y 75 ter."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO["LRBRL"] = "Ley 7/1985"
CORTO["CEAL"] = "Carta Europea de Autonomía Local"
L = "LRBRL"

T = Tema("B1T11",
  "Cuatro preguntas: I. Qué entidades forman la Administración local (arts. 137 y 141 CE; Ley 7/1985, arts. 3 y 42 a 44) · II. Qué es la autonomía local y cómo se protege (art. 142 CE; Carta Europea de Autonomía Local; Ley 7/1985, arts. 1, 2, 4, 7 y 10; LOTC) · III. Cómo se organiza el municipio y qué competencias tiene (art. 140 CE; Ley 7/1985, arts. 11 a 13, 15, 19 a 27, 29 y 121) · IV. Cómo se organiza la provincia y qué competencias tiene (art. 141 CE; Ley 7/1985, arts. 31 a 41). Cada artículo: texto literal del BOE y ficha.",
  ["Administración local", "Ley 7/1985", "Entidades locales", "Autonomía local", "Carta Europea de Autonomía Local", "Municipio", "Alcalde", "Pleno", "Junta de Gobierno Local", "Concejo abierto", "Competencias propias", "Servicios mínimos", "Provincia", "Diputación", "Cabildos y Consejos insulares", "Áreas metropolitanas", "Mancomunidades"])

# =============================================================================
T.ap("s0", "Mapa del tema: cuatro preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque I, tema 11):
> Organización territorial (II): la Administración local: entidades que la integran. La autonomía local. El municipio: organización y competencias. La provincia: organización y competencias.

### El hilo conductor

El epígrafe se lee como **cuatro preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Constitución | Otras normas |
|---|---|---|---|
| **I** | ¿Qué entidades integran la Administración local? | Arts. 137 y 141.3 y 4 | Ley 7/1985, arts. 3, 42, 43 y 44 |
| **II** | ¿Qué es la autonomía local y cómo se garantiza? | Arts. 137 y 142 | Carta Europea de Autonomía Local, arts. 3 y 4; Ley 7/1985, arts. 1, 2, 4, 7 y 10; LOTC, arts. 75 bis y 75 ter |
| **III** | ¿Cómo se organiza el municipio y qué competencias tiene? | Art. 140 | Ley 7/1985, arts. 11 a 13, 15, 19 a 27, 29 y 121 |
| **IV** | ¿Cómo se organiza la provincia y qué competencias tiene? | Art. 141.1 y 2 | Ley 7/1985, arts. 31 a 41 |

!> **La idea que une los cuatro bloques:** la Constitución organiza el Estado en **municipios, provincias y Comunidades Autónomas** y les reconoce **autonomía** para gestionar sus intereses (art. 137). La Ley 7/1985 dice **qué entidades** son locales (I), **en qué consiste** su autonomía y cuáles son sus **competencias** (II), y regula los dos niveles básicos: el **municipio** (III), gobernado por el **Ayuntamiento** (Alcalde y Concejales), y la **provincia** (IV), gobernada por la **Diputación** u otras Corporaciones representativas.

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- La Comunidad Autónoma y sus instituciones son el tema I.10; el conflicto en defensa de la autonomía local ante el Tribunal Constitucional se estudia en el tema I.3 (aquí, solo lo esencial).
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué entidades integran la Administración local? (arts. 137 y 141 CE; Ley 7/1985, arts. 3 y 42 a 44)", donde(
  "Primera pregunta del tema. Antes de estudiar el municipio y la provincia hay que saber **qué entidades** forman la Administración local: las que nombra la Constitución y las que añade la Ley 7/1985.",
  ["1 Las entidades locales en la Constitución (arts. 137 y 141.3 y 4)", "2 Entidades locales territoriales y no territoriales (Ley 7/1985, art. 3)", "3 Comarcas, áreas metropolitanas y mancomunidades (Ley 7/1985, arts. 42 a 44)"]))

T.ap("s1", "I.1 Las entidades locales en la Constitución (arts. 137 y 141.3 y 4)", f"""
La Constitución nombra **dos** entidades locales en el art. 137 (municipios y provincias), permite otras **agrupaciones de municipios** y da a las **islas** de los archipiélagos administración propia.

{unidad("1.1 La organización territorial del Estado (art. 137)",
  lit("CE", "Artículo 137", ["en municipios, en provincias y en las Comunidades Autónomas que se constituyan", "autonomía para la gestión de sus respectivos intereses"]),
  fichab("Los tres niveles en que se organiza territorialmente el Estado",
         f"{c('CE', 'Artículo 137', 'municipios')}, {c('CE', 'Artículo 137', 'provincias')} y {c('CE', 'Artículo 137', 'Comunidades Autónomas que se constituyan')}",
         f"Todas {c('CE', 'Artículo 137', 'gozan de autonomía para la gestión de sus respectivos intereses')} (→ II.1)",
         "—",
         "El art. 137 nombra **municipios, provincias y Comunidades Autónomas**: ni islas, ni comarcas, ni áreas metropolitanas. La autonomía es «para la gestión de sus **respectivos intereses**»."))}

{unidad("1.2 Agrupaciones de municipios e islas (art. 141.3 y 4)",
  lit("CE", "Artículo 141", ["agrupaciones de municipios diferentes de la provincia", "en forma de Cabildos o Consejos"], solo=[3, 4]),
  fichab("Otras entidades locales previstas en la Constitución",
         ["Agrupaciones de municipios distintas de la provincia (141.3)", "Islas de los archipiélagos (141.4)"],
         f"Las islas tienen {c('CE', 'Artículo 141', 'su administración propia en forma de Cabildos o Consejos')}",
         "—",
         "Archipiélagos: **Cabildos o Consejos** (no Diputaciones insulares, ni mancomunidades, ni Delegaciones del Gobierno). Cayó en 2025 (→ Cierre 1). La Ley 7/1985 los regula en el art. 41 (→ IV.5.3)."))}
""", 2)

T.ap("s2", "I.2 Entidades locales territoriales y no territoriales (Ley 7/1985, art. 3)", f"""
La Ley 7/1985 distingue las entidades locales **territoriales** (las que tienen un territorio propio y potestades plenas) de las que **gozan asimismo** de la condición de entidad local.

{unidad("2.1 Lista legal de entidades locales (art. 3)",
  lit(L, "Artículo 3", ["Son Entidades Locales territoriales", "La Isla en los archipiélagos balear y canario", "Gozan, asimismo, de la condición de Entidades Locales"]),
  fichab("Catálogo de las entidades locales",
         ["::Territoriales (3.1):", "El Municipio", "La Provincia", "La Isla en los archipiélagos balear y canario", "::También entidades locales (3.2):", "Comarcas u otras entidades que agrupen varios Municipios, instituidas por las Comunidades Autónomas", "Áreas Metropolitanas", "Mancomunidades de Municipios"],
         f"Las comarcas, {c(L, 'Artículo 3', 'instituidas por las Comunidades Autónomas de conformidad con esta Ley y los correspondientes Estatutos de Autonomía')}",
         "—",
         "Solo **tres** son territoriales: **Municipio, Provincia e Isla**. Comarcas, áreas metropolitanas y mancomunidades son entidades locales, pero **no territoriales**. Los entes de ámbito inferior al municipio **no** están en la lista (→ III.6.3)."))}
""", 2)

T.ap("s3", "I.3 Comarcas, áreas metropolitanas y mancomunidades (Ley 7/1985, arts. 42 a 44)", f"""
Las tres entidades del art. 3.2 se regulan en el título IV de la Ley 7/1985 («Otras Entidades locales»).

{unidad("3.1 Comarcas (art. 42)",
  lit(L, "Artículo 42", ["podrán crear en su territorio comarcas", "las dos quintas partes de los Municipios", "al menos la mitad del censo electoral", "informe favorable de las Diputaciones Provinciales"]),
  fichab("Agrupación de municipios con intereses comunes, creada por la Comunidad Autónoma",
         f"{c(L, 'Artículo 42', 'Las Comunidades Autónomas, de acuerdo con lo dispuesto en sus respectivos Estatutos')}; la iniciativa {c(L, 'Artículo 42', 'podrá partir de los propios Municipios interesados')}",
         ["Las leyes autonómicas fijan territorio, órganos (representativos de los Ayuntamientos), competencias y recursos (42.3)", "No priva a los municipios de los servicios del art. 26 ni de toda intervención en las materias del 25.2 (42.4)"],
         f"Veto: {c(L, 'Artículo 42', 'las dos quintas partes de los Municipios')} que representen {c(L, 'Artículo 42', 'al menos la mitad del censo electoral')}; si abarca más de una provincia, informe **favorable** de las Diputaciones",
         "**Dos quintas** partes de los municipios + **mitad del censo**: las dos condiciones a la vez."))}

{unidad("3.2 Áreas metropolitanas (art. 43)",
  lit(L, "Artículo 43", ["mediante Ley", "Municipios de grandes aglomeraciones urbanas", "planificación conjunta y la coordinación de determinados servicios y obras"]),
  fichab("Entidad local de los municipios de grandes aglomeraciones urbanas",
         f"Las crean, modifican y suprimen {c(L, 'Artículo 43', 'Las Comunidades Autónomas')} {c(L, 'Artículo 43', 'mediante Ley')}",
         f"{c(L, 'Artículo 43', 'previa audiencia de la Administración del Estado y de los Ayuntamientos y Diputaciones afectados')}; en sus órganos están representados **todos** los municipios del área",
         "—",
         "La definición del 43.2 (grandes aglomeraciones urbanas + vinculaciones económicas y sociales + planificación conjunta) es la del **área metropolitana**, no la de la mancomunidad ni la de la comarca. Cayó en 2025 (→ Cierre 1)."))}

{unidad("3.3 Mancomunidades (art. 44)",
  lit(L, "Artículo 44", ["derecho a asociarse con otros en mancomunidades", "obras y servicios determinados de su competencia", "Los Plenos de todos los ayuntamientos aprueban los estatutos", "distintas comunidades autónomas"]),
  fichab("Asociación voluntaria de municipios para obras y servicios comunes",
         c(L, 'Artículo 44', 'los municipios'),
         ["Personalidad y capacidad jurídicas para sus fines específicos; se rigen por sus Estatutos (44.2)", "Estatutos: los elaboran los concejales de los municipios promotores en asamblea; informe de la Diputación; los aprueban los Plenos de todos los ayuntamientos (44.3)"],
         "—",
         "La mancomunidad nace de un **derecho de los municipios** (asociarse); la comarca y el área metropolitana las crea la **Comunidad Autónoma**. Puede reunir municipios de **distintas Comunidades Autónomas** si lo permiten sus normativas."))}

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Entidad | Quién la crea | Para qué | Artículo |
|---|---|---|---|
| Comarca | Comunidad Autónoma (iniciativa posible de los municipios) | Intereses comunes que precisan gestión propia o servicios de ese ámbito | 42 |
| Área metropolitana | Comunidad Autónoma, mediante ley | Planificación conjunta y coordinación de servicios y obras en grandes aglomeraciones urbanas | 43 |
| Mancomunidad | Los municipios (derecho a asociarse) | Ejecución en común de obras y servicios determinados de su competencia | 44 |

{resumen([
  "Constitución: **municipios, provincias y Comunidades Autónomas** (137); agrupaciones de municipios (141.3); islas con **Cabildos o Consejos** (141.4).",
  "Entidades locales **territoriales**: Municipio, Provincia e Isla (art. 3.1 Ley 7/1985).",
  "También entidades locales: **comarcas** (las crea la CA), **áreas metropolitanas** (la CA, por ley) y **mancomunidades** (asociación de municipios)."],
  "Siguiente: II. ¿Qué es la autonomía local y cómo se garantiza?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Qué es la autonomía local y cómo se garantiza? (art. 142 CE; Carta Europea; Ley 7/1985; LOTC)", donde(
  "Segunda pregunta. Ya sabemos **qué** entidades son locales; ahora, **qué significa** que gocen de autonomía, con qué **potestades** y **competencias** la ejercen y cómo se **defiende**.",
  ["1 La garantía constitucional: autonomía y suficiencia financiera (arts. 137 y 142)", "2 El concepto: la Carta Europea de Autonomía Local (arts. 3 y 4)", "3 La autonomía en la Ley 7/1985: entidades y potestades (arts. 1, 2 y 4)", "4 Competencias propias, delegadas y distintas; coordinación (arts. 7 y 10)", "5 La defensa de la autonomía local ante el Tribunal Constitucional (LOTC, arts. 75 bis y 75 ter)"]))

T.ap("s4", "II.1 La garantía constitucional: autonomía y suficiencia financiera (arts. 137 y 142)", f"""
El art. 137 reconoce a municipios y provincias autonomía {c('CE', 'Artículo 137', 'para la gestión de sus respectivos intereses')} (→ I.1.1). El art. 140 la **garantiza** para los municipios (→ III.1.1). El art. 142 asegura el soporte económico de esa autonomía.

{unidad("1.1 Las Haciendas locales (art. 142)",
  lit("CE", "Artículo 142", ["medios suficientes", "tributos propios y de participación en los del Estado y de las Comunidades Autónomas"]),
  fichab("Principio de suficiencia de las Haciendas locales",
         c('CE', 'Artículo 142', 'Las Haciendas locales'),
         f"Se nutren {c('CE', 'Artículo 142', 'fundamentalmente de tributos propios y de participación en los del Estado y de las Comunidades Autónomas')}",
         "—",
         f"Dos fuentes **fundamentales**: **tributos propios** y **participación** en los del Estado **y** de las Comunidades Autónomas. Las Corporaciones locales establecen y exigen tributos {c('CE', 'Artículo 133', 'de acuerdo con la Constitución y las leyes')} (art. 133.2, tema IV.2)."))}
""", 2)

T.ap("s5", "II.2 El concepto: la Carta Europea de Autonomía Local (arts. 3 y 4)", f"""
La Carta Europea de Autonomía Local (Estrasburgo, 15 de octubre de 1985) está ratificada por España y publicada en el BOE. Da la **definición** de autonomía local que la Constitución no contiene.

{unidad("2.1 Concepto de autonomía local (art. 3)",
  lit("CEAL", "a3", ["el derecho y la capacidad efectiva", "una parte importante de los asuntos públicos", "bajo su propia responsabilidad"]),
  fichab("Qué es la autonomía local",
         c('CEAL', 'a3', 'las Entidades locales'),
         f"{c('CEAL', 'a3', 'ordenar y gestionar una parte importante de los asuntos públicos, en el marco de la Ley, bajo su propia responsabilidad y en beneficio de sus habitantes')}",
         f"Se ejerce por {c('CEAL', 'a3', 'Asambleas o Consejos integrados por miembros elegidos por sufragio libre, secreto, igual, directo y universal')}",
         "Es un **derecho** y una **capacidad efectiva**; sobre **una parte importante** de los asuntos públicos (no todos), **en el marco de la Ley**."))}

{unidad("2.2 Alcance de la autonomía local (art. 4)",
  lit("CEAL", "a4", ["vienen fijadas por la Constitución o por la Ley", "a las autoridades más cercanas a los ciudadanos", "normalmente plenas y completas"], solo=[1, 3, 4]),
  fichab("Cómo se fijan y ejercen las competencias locales",
         "Las Entidades locales",
         ["Competencias básicas fijadas por la Constitución o por la Ley (4.1)", "Preferencia por las autoridades más cercanas a los ciudadanos (4.3)", "Competencias normalmente plenas y completas (4.4)"],
         "—",
         "El criterio de **proximidad** («autoridades más cercanas a los ciudadanos») reaparece en el art. 2.1 de la Ley 7/1985: «máxima proximidad de la gestión administrativa a los ciudadanos» (→ II.3.2)."))}
""", 2)

T.ap("s6", "II.3 La autonomía en la Ley 7/1985: entidades y potestades (arts. 1, 2 y 4)", f"""
{unidad("3.1 Municipio, provincia e isla: entidades con autonomía (art. 1)",
  lit(L, "Artículo 1", ["entidades básicas de la organización territorial del Estado", "cauces inmediatos de participación ciudadana", "idéntica autonomía"]),
  fichab("Posición del municipio, la provincia y la isla",
         ["Municipios: entidades básicas de la organización territorial del Estado (1.1)", "Provincia y, en su caso, Isla: idéntica autonomía (1.2)"],
         f"Los municipios {c(L, 'Artículo 1', 'institucionalizan y gestionan con autonomía los intereses propios de las correspondientes colectividades')}",
         "—",
         "Municipio = **entidad básica** y **cauce inmediato de participación ciudadana**. La provincia y la isla tienen **idéntica** autonomía (no una autonomía menor)."))}

{unidad("3.2 La garantía legal: derecho a intervenir en sus asuntos (art. 2)",
  lit(L, "Artículo 2", ["su derecho a intervenir en cuantos asuntos afecten directamente al círculo de sus intereses", "descentralización y de máxima proximidad de la gestión administrativa a los ciudadanos"]),
  fichab("Mandato al legislador estatal y autonómico para hacer efectiva la autonomía local",
         f"{c(L, 'Artículo 2', 'la legislación del Estado y la de las Comunidades Autónomas')}, según la distribución constitucional de competencias",
         f"Atribuyendo competencias {c(L, 'Artículo 2', 'en atención a las características de la actividad pública de que se trate y a la capacidad de gestión de la entidad local')}",
         "—",
         "Principios del 2.1: **descentralización** y **máxima proximidad** de la gestión a los ciudadanos. Las leyes básicas del Estado determinan las competencias locales en las materias que regulan (2.2)."))}

{unidad("3.3 Potestades de las entidades locales territoriales (art. 4)",
  lit(L, "Artículo 4", ["corresponden en todo caso a los municipios, las provincias y las islas", "reglamentaria y de autoorganización", "expropiatoria", "la inembargabilidad de sus bienes y derechos"], solo=[1, 2, 3, 4, 5, 6, 7, 8, 9]),
  fichab("Potestades y prerrogativas de las Administraciones locales territoriales",
         c(L, 'Artículo 4', 'los municipios, las provincias y las islas'),
         ["Reglamentaria y de autoorganización", "Tributaria y financiera", "Programación o planificación", "Expropiatoria; investigación, deslinde y recuperación de oficio de bienes", "Presunción de legitimidad y ejecutividad de sus actos", "Ejecución forzosa y sancionadora", "Revisión de oficio", "Prelaciones y prerrogativas de la Hacienda Pública; inembargabilidad"],
         "Dentro de la esfera de sus competencias",
         "Son potestades **administrativas**: no hay potestad **legislativa** local. Las demás entidades (comarcas, áreas metropolitanas) tienen las que concreten las leyes autonómicas; las mancomunidades, las de sus Estatutos (4.2 y 3)."))}
""", 2)

T.ap("s7", "II.4 Competencias propias, delegadas y distintas; coordinación (arts. 7 y 10)", f"""
{unidad("4.1 Clases de competencias (art. 7)",
  lit(L, "Artículo 7", ["propias o atribuidas por delegación", "solo podrán ser determinadas por Ley", "en régimen de autonomía y bajo la propia responsabilidad", "no se ponga en riesgo la sostenibilidad financiera", "necesarios y vinculantes"]),
  fichab("Competencias de las entidades locales",
         "Entidades locales; delegan el Estado y las Comunidades Autónomas",
         ["Propias: solo por Ley; se ejercen en régimen de autonomía y bajo la propia responsabilidad (7.2)", "Delegadas: en los términos de la delegación, con las reglas del art. 27 (7.3; → III.9.1)", "Distintas de las propias y delegadas: solo sin riesgo para la sostenibilidad financiera y sin ejecución simultánea del mismo servicio (7.4)"],
         "Competencias distintas: informes previos **necesarios y vinculantes** de la Administración competente por razón de materia y de la que tenga la tutela financiera",
         "Las competencias **propias** se determinan **solo por Ley**. Las distintas exigen dos informes **necesarios y vinculantes**."))}

{unidad("4.2 Relaciones y coordinación (art. 10)",
  lit(L, "Artículo 10", ["información mutua, colaboración, coordinación y respeto a los ámbitos competenciales respectivos", "compatibles con la autonomía"], solo=[1, 4]),
  fichab("Deberes recíprocos entre la Administración local y las demás",
         "La Administración Local y las demás Administraciones públicas",
         ["Información mutua", "Colaboración", "Coordinación", "Respeto a los ámbitos competenciales respectivos"],
         "—",
         f"La coordinación es **compatible** con la autonomía: {c(L, 'Artículo 10', 'Las funciones de coordinación serán compatibles con la autonomía de las Entidades Locales')}."))}
""", 2)

T.ap("s8", "II.5 La defensa de la autonomía local ante el Tribunal Constitucional (LOTC, arts. 75 bis y 75 ter)", f"""
El **conflicto en defensa de la autonomía local** se estudia con el Tribunal Constitucional (tema I.3). Aquí, lo esencial: contra qué leyes y quién puede plantearlo.

{unidad("5.1 Objeto del conflicto (art. 75 bis LOTC)",
  lit("LOTC", "asetentaycincobis", ["normas del Estado con rango de ley o las disposiciones con rango de ley de las Comunidades Autónomas"], solo=[1]),
  fichab("Vía para que los entes locales impugnen leyes que lesionen su autonomía",
         "Municipios y provincias legitimados (→ II.5.2)",
         f"Contra {c('LOTC', 'asetentaycincobis', 'las normas del Estado con rango de ley o las disposiciones con rango de ley de las Comunidades Autónomas')}",
         "—",
         "Se impugnan normas con **rango de ley** (estatales o autonómicas), no reglamentos ni actos."))}

{unidad("5.2 Legitimación y acuerdo del Pleno (art. 75 ter LOTC)",
  lit("LOTC", "asetentaycincoter", ["destinatario único de la ley", "al menos un séptimo", "como mínimo un sexto", "al menos la mitad de las existentes", "mayoría absoluta del número legal de miembros", "preceptivo pero no vinculante"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Quién puede plantear el conflicto y qué trámites previos exige",
         ["Municipio o provincia destinatario único de la ley", "Municipios: al menos un séptimo de los existentes y un sexto de la población", "Provincias: al menos la mitad de las existentes y la mitad de la población"],
         "Acuerdo del Pleno y, antes de formalizar el conflicto, dictamen del Consejo de Estado u órgano consultivo autonómico",
         f"{c('LOTC', 'asetentaycincoter', 'mayoría absoluta del número legal de miembros')}; dictamen {c('LOTC', 'asetentaycincoter', 'con carácter preceptivo pero no vinculante')}; solicitud del dictamen {c('LOTC', 'asetentaycincoquater', 'dentro de los tres meses siguientes al día de la publicación de la ley')} (art. 75 quater.1)",
         "**Un séptimo** de los municipios y **un sexto** de la población; provincias, **la mitad** y **la mitad**. Dictamen **preceptivo pero no vinculante**."))}

{resumen([
  "Autonomía **para la gestión de sus respectivos intereses** (137 CE); Haciendas locales con **medios suficientes**: tributos propios y participación en los del Estado y de las CC. AA. (142).",
  "Carta Europea: derecho y **capacidad efectiva** de ordenar y gestionar **una parte importante** de los asuntos públicos (art. 3).",
  "Ley 7/1985: municipios, **entidades básicas** (1); **descentralización y máxima proximidad** (2); potestades del art. 4; competencias **propias (solo por Ley)** o **delegadas** (7).",
  "Defensa: conflicto en defensa de la autonomía local contra **normas con rango de ley** (LOTC, 75 bis)."],
  "Siguiente: III. ¿Cómo se organiza el municipio y qué competencias tiene?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Cómo se organiza el municipio y qué competencias tiene? (art. 140 CE; Ley 7/1985, arts. 11 a 13, 15, 19 a 27, 29 y 121)", donde(
  "Tercera pregunta, la más preguntada. El municipio es la **entidad local básica**: primero, qué es y cuáles son sus elementos; después, sus **órganos** (Alcalde, Pleno, Junta de Gobierno Local) y sus **competencias** (propias, servicios mínimos y delegadas).",
  ["1 El municipio en la Constitución (art. 140)", "2 Concepto y elementos: territorio y población (arts. 11 a 13 y 15)", "3 Organización: el Ayuntamiento y los órganos necesarios (arts. 19 y 20)", "4 El Alcalde (art. 21)", "5 El Pleno (art. 22)", "6 Junta de Gobierno Local, Tenientes de Alcalde y gestión desconcentrada (arts. 23, 24 y 24 bis)", "7 Competencias propias (art. 25)", "8 Servicios mínimos obligatorios (art. 26)", "9 Competencias delegadas (art. 27)", "10 Regímenes especiales: concejo abierto y municipios de gran población (arts. 29 y 121)"]))

T.ap("s9", "III.1 El municipio en la Constitución (art. 140)", f"""
{unidad("1.1 Autonomía, gobierno y elección (art. 140)",
  lit("CE", "Artículo 140", ["La Constitución garantiza la autonomía de los municipios", "personalidad jurídica plena", "integrados por los Alcaldes y los Concejales", "sufragio universal, igual, libre, directo y secreto", "Los Alcaldes serán elegidos por los Concejales o por los vecinos", "concejo abierto"]),
  fichab("Garantía constitucional del municipio y de su gobierno",
         f"Gobierno y administración: {c('CE', 'Artículo 140', 'sus respectivos Ayuntamientos, integrados por los Alcaldes y los Concejales')}",
         ["Concejales: elegidos por los vecinos por sufragio universal, igual, libre, directo y secreto", "Alcaldes: elegidos por los Concejales o por los vecinos", "Concejo abierto: en las condiciones que regule la ley"],
         "—",
         "Personalidad jurídica **plena**. El Alcalde lo eligen **los Concejales o los vecinos**; los Concejales, **los vecinos**. El concejo abierto lo regula **la ley** (→ III.10.1)."))}
""", 2)

T.ap("s10", "III.2 Concepto y elementos: territorio y población (arts. 11 a 13 y 15)", f"""
{unidad("2.1 Concepto y elementos (art. 11)",
  lit(L, "Artículo 11", ["la entidad local básica de la organización territorial del Estado", "el territorio, la población y la organización"]),
  fichab("El municipio y sus tres elementos",
         "El Municipio",
         f"Tiene {c(L, 'Artículo 11', 'personalidad jurídica y plena capacidad para el cumplimiento de sus fines')}",
         "—",
         "Tres elementos: **territorio, población y organización** (no «competencias» ni «hacienda»)."))}

{unidad("2.2 El término municipal (art. 12)",
  lit(L, "Artículo 12", ["el territorio en que el ayuntamiento ejerce sus competencias", "a una sola provincia"]),
  fichab("Territorio del municipio", "El Ayuntamiento ejerce en él sus competencias", "—", "—",
         "Cada municipio pertenece a **una sola** provincia; por eso la alteración de términos municipales **no** puede modificar límites provinciales (art. 13.1)."))}

{unidad("2.3 Creación, supresión y alteración de municipios (art. 13.1 y 2)",
  lit(L, "Artículo 13", ["legislación de las Comunidades Autónomas sobre régimen local", "en ningún caso, modificación de los límites provinciales", "dictamen del Consejo de Estado o del órgano consultivo superior", "de al menos 4.000 habitantes"], solo=[1, 2]),
  fichab("Cambios en el mapa municipal",
         f"Los regula {c(L, 'Artículo 13', 'la legislación de las Comunidades Autónomas sobre régimen local')}",
         ["Audiencia de los municipios interesados", "Dictamen del Consejo de Estado o del órgano consultivo autonómico superior", "Informe de la Administración que ejerza la tutela financiera", "Conocimiento simultáneo a la Administración General del Estado"],
         "Nuevos municipios: núcleos territorialmente diferenciados de **al menos 4.000 habitantes**, financieramente sostenibles",
         "La competencia es **autonómica**; la alteración de términos municipales **nunca** modifica límites provinciales (eso exige ley orgánica: → IV.1.1)."))}

{unidad("2.4 La población: padrón y vecinos (art. 15)",
  lit(L, "Artículo 15", ["está obligada a inscribirse en el Padrón del municipio en el que resida habitualmente", "durante más tiempo al año", "Los inscritos en el Padrón municipal son los vecinos del municipio", "en el mismo momento de su inscripción en el Padrón"]),
  fichab("Empadronamiento y condición de vecino",
         c(L, 'Artículo 15', 'Toda persona que viva en España'),
         "Inscripción en el Padrón del municipio de residencia habitual; si vive en varios, en el que habite **más tiempo al año**",
         "La condición de vecino se adquiere **en el mismo momento** de la inscripción",
         f"Los inscritos son **los vecinos**; el conjunto de inscritos {c(L, 'Artículo 15', 'constituye la población del municipio')}."))}
""", 2)

T.ap("s11", "III.3 Organización: el Ayuntamiento y los órganos necesarios (arts. 19 y 20)", f"""
{unidad("3.1 El Ayuntamiento (art. 19)",
  lit(L, "Artículo 19", ["corresponde al ayuntamiento, integrado por el Alcalde y los Concejales", "el Alcalde es elegido por los Concejales o por los vecinos", "título X"]),
  fichab("Órgano de gobierno y administración del municipio",
         f"El Ayuntamiento, {c(L, 'Artículo 19', 'integrado por el Alcalde y los Concejales')} (salvo concejo abierto)",
         "Elección según la legislación electoral general",
         "—",
         "Los municipios de **gran población** (título X) tienen su propio régimen de organización; en lo no previsto, el común (19.3; → III.10.2)."))}

{unidad("3.2 Órganos de existencia obligatoria (art. 20.1)",
  lit(L, "Artículo 20", ["existen en todos los ayuntamientos", "población superior a 5.000 habitantes", "existe en todos los municipios"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Qué órganos hay en cada municipio",
         ["::En todos:", "Alcalde, Tenientes de Alcalde y Pleno (20.1 a)", "Comisión Especial de Cuentas (20.1 e)", "::Más de 5.000 habitantes (o si lo dispone el reglamento orgánico o lo acuerda el Pleno):", "Junta de Gobierno Local (20.1 b)", "Órganos de estudio, informe o consulta y seguimiento de la gestión (20.1 c)", "::Gran población (título X) o acuerdo del Pleno:", "Comisión Especial de Sugerencias y Reclamaciones (20.1 d)"],
         "Las leyes autonómicas y los reglamentos orgánicos pueden añadir órganos complementarios (20.2 y 3)",
         "Comisión Especial de Sugerencias y Reclamaciones por acuerdo del Pleno: **mayoría absoluta del número legal** de miembros",
         "La **Junta de Gobierno Local no existe en todos** los ayuntamientos: es obligatoria con **más de 5.000** habitantes. Cayó en 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s12", "III.4 El Alcalde (art. 21)", f"""
{unidad("4.1 Atribuciones y delegación (art. 21)",
  lit(L, "Artículo 21", ["El Alcalde es el Presidente de la Corporación", "Dirigir el gobierno y la administración municipal", "decidir los empates con voto de calidad", "Dictar bandos", "Ejercer la jefatura de la Policía Municipal", "El otorgamiento de las licencias", "el nombramiento de los Tenientes de Alcalde", "El Alcalde puede delegar el ejercicio de sus atribuciones, salvo"]),
  fichab("Presidente de la Corporación y órgano ejecutivo del municipio",
         c(L, 'Artículo 21', 'El Alcalde'),
         ["Dirige el gobierno y la administración municipal y representa al ayuntamiento", "Convoca y preside el Pleno y la Junta de Gobierno Local; voto de calidad", "Dicta bandos; jefatura del personal y de la Policía Municipal", "Licencias (salvo que las leyes sectoriales las atribuyan al Pleno o a la Junta de Gobierno Local)", "En catástrofe o grave riesgo, medidas personales dando cuenta inmediata al Pleno", "Competencia residual: las que las leyes asignen al municipio sin atribuirlas a otro órgano (21.1 s)"],
         "Indelegables: convocar y presidir el Pleno y la Junta, voto de calidad, operaciones de crédito, jefatura superior del personal, separación de funcionarios y despido de laborales, y las letras a), e), j), k), l) y m)",
         "**Dictar bandos** es del Alcalde e **indelegable**; el **control y la fiscalización** de los órganos de gobierno es del **Pleno** (no del Alcalde). Para la lesividad, el Alcalde solo tiene la **iniciativa** (21.1 l)."))}
""", 2)

T.ap("s13", "III.5 El Pleno (art. 22)", f"""
{unidad("5.1 Composición, atribuciones y delegación (art. 22)",
  lit(L, "Artículo 22", ["integrado por todos los Concejales, es presidido por el Alcalde", "al Pleno municipal en los Ayuntamientos, y a la Asamblea vecinal en el régimen de Concejo Abierto", "El control y la fiscalización de los órganos de gobierno", "La aprobación del reglamento orgánico y de las ordenanzas", "La declaración de lesividad de los actos del Ayuntamiento", "mediante llamamiento nominal en todo caso", "El Pleno puede delegar el ejercicio de sus atribuciones en el Alcalde y en la Junta de Gobierno Local"]),
  fichab("Órgano de máxima deliberación del municipio",
         f"{c(L, 'Artículo 22', 'todos los Concejales')}; lo preside el Alcalde. En concejo abierto, la **Asamblea vecinal**",
         ["Control y fiscalización de los órganos de gobierno", "Reglamento orgánico y ordenanzas; presupuestos y cuentas; recursos tributarios", "Alteración del término, creación o supresión de municipios, bandera, enseña o escudo", "Plantilla y relación de puestos de trabajo", "Declaración de lesividad de los actos del Ayuntamiento", "Moción de censura y cuestión de confianza (22.3)"],
         "Votación de la moción de censura y de la cuestión de confianza: **pública** y por **llamamiento nominal**; delegable en el Alcalde y la Junta de Gobierno Local salvo las letras a) a i), l) y p) del 22.2 y el 22.3",
         "La **lesividad** es del **Pleno** (22.2 k) y **sí es delegable** (no está en la lista del 22.4). En concejo abierto, las atribuciones del Pleno son de la **Asamblea vecinal**."))}
""", 2)

T.ap("s14", "III.6 Junta de Gobierno Local, Tenientes de Alcalde y gestión desconcentrada (arts. 23, 24 y 24 bis)", f"""
{unidad("6.1 Junta de Gobierno Local y Tenientes de Alcalde (art. 23)",
  lit(L, "Artículo 23", ["no superior al tercio del número legal de los mismos", "La asistencia al Alcalde en el ejercicio de sus atribuciones", "por el orden de su nombramiento", "libremente designados y removidos por éste de entre los miembros de la Junta de Gobierno Local"]),
  fichab("Órgano colegiado de asistencia al Alcalde y sus sustitutos",
         ["Junta: el Alcalde y Concejales nombrados y separados libremente por él, dando cuenta al Pleno", "Tenientes de Alcalde: designados y removidos por el Alcalde entre los miembros de la Junta (o entre los Concejales si no hay Junta)"],
         ["Junta: asiste al Alcalde y ejerce las atribuciones delegadas o atribuidas por ley", "Tenientes: sustituyen al Alcalde por el orden de su nombramiento en vacante, ausencia o enfermedad"],
         "Número de Concejales en la Junta: **no superior al tercio** del número legal",
         "Los Tenientes de Alcalde los designa **el Alcalde** (no el Pleno). Cayó en 2025 (→ Cierre 1)."))}

{unidad("6.2 Órganos territoriales de gestión desconcentrada (art. 24.1)",
  lit(L, "Artículo 24", ["órganos territoriales de gestión desconcentrada", "sin perjuicio de la unidad de gobierno y gestión del municipio"], solo=[1]),
  fichab("Desconcentración territorial dentro del municipio", "Los municipios (potestativo)", "Con la organización, funciones y competencias que cada ayuntamiento les confiera", "—",
         "Su finalidad: facilitar la **participación ciudadana** y mejorar la gestión; respetan la **unidad** de gobierno y gestión del municipio."))}

{unidad("6.3 Entes de ámbito territorial inferior al municipio (art. 24 bis)",
  lit(L, "Artículo 24 bis", ["carecerán de personalidad jurídica", "forma de organización desconcentrada", "pedanías"]),
  fichab("Organización desconcentrada de núcleos de población separados",
         f"Los regulan {c(L, 'Artículo 24 bis', 'Las leyes de las Comunidades Autónomas sobre régimen local')}; iniciativa de la población interesada o del Ayuntamiento (que debe ser oído siempre)",
         "Solo si son una opción más eficiente según los principios de la Ley Orgánica 2/2012",
         "—",
         "**Sin personalidad jurídica**: no son entidades locales del art. 3 (→ I.2.1). Denominaciones tradicionales: caseríos, parroquias, aldeas, barrios, anteiglesias, concejos, pedanías, lugares anejos."))}
""", 2)

T.ap("s15", "III.7 Competencias propias (art. 25)", f"""
{unidad("7.1 Las materias de competencia propia (art. 25.1 a 5)",
  lit(L, "Artículo 25", ["ejercerá en todo caso como competencias propias", "Policía local, protección civil, prevención y extinción de incendios", "Información y promoción de la actividad turística de interés y ámbito local", "Protección de la salubridad pública", "Actuaciones en la promoción de la igualdad entre hombres y mujeres así como contra la violencia de género", "se determinarán por Ley"], solo=list(range(1, 24))),
  fichab("Materias en que el municipio tiene siempre competencias propias",
         c(L, 'Artículo 25', 'El Municipio'),
         ["Las ejerce «en los términos de la legislación del Estado y de las Comunidades Autónomas» (25.2)", "La ley que las determine evalúa la conveniencia conforme a descentralización, eficiencia, estabilidad y sostenibilidad financiera (25.3)", "Memoria económica y garantía de que no hay atribución simultánea a otra Administración (25.4 y 5)"],
         "—",
         "Se pregunta con distractores que **no están** en la lista: «Turismo» en general (solo información y promoción turística de interés y ámbito local), «Sanidad» (solo protección de la salubridad pública), «Pesca». La **igualdad entre hombres y mujeres y contra la violencia de género** sí está (letra o). Cayó en 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s16", "III.8 Servicios mínimos obligatorios (art. 26)", f"""
{unidad("8.1 Servicios por tramos de población (art. 26.1)",
  lit(L, "Artículo 26", ["En todos los Municipios", "superior a 5.000 habitantes", "superior a 20.000 habitantes", "superior a 50.000 habitantes"], solo=[1, 2, 3, 4, 5]),
  fichab("Servicios que los municipios deben prestar en todo caso",
         "Los Municipios, según su población",
         ["Todos: alumbrado público, cementerio, recogida de residuos, limpieza viaria, agua potable, alcantarillado, acceso a núcleos y pavimentación", "Más de 5.000: además, parque público, biblioteca pública y tratamiento de residuos", "Más de 20.000: además, protección civil, servicios sociales de atención inmediata, prevención y extinción de incendios e instalaciones deportivas", "Más de 50.000: además, transporte colectivo urbano de viajeros y medio ambiente urbano"],
         "Umbrales: **5.000 · 20.000 · 50.000** habitantes",
         "Los tramos son **acumulativos** («además»). **Biblioteca**: más de 5.000; **incendios**: más de 20.000; **transporte urbano**: más de 50.000."))}

{unidad("8.2 Coordinación por la Diputación en municipios de menos de 20.000 habitantes (art. 26.2 y 3)",
  lit(L, "Artículo 26", ["con población inferior a 20.000 habitantes", "la Diputación provincial o entidad equivalente la que coordinará"], solo=[6, 7, 8, 9, 10, 11, 12, 14, 15, 16]),
  fichab("Papel de la Diputación en los servicios mínimos de los municipios pequeños",
         "La Diputación provincial o entidad equivalente",
         ["Coordina: recogida y tratamiento de residuos, agua y aguas residuales, limpieza viaria, acceso a núcleos, pavimentación y alumbrado", "El municipio puede asumirlos si acredita ante la Diputación un coste efectivo menor", "Si la Diputación asume la prestación, repercute a los municipios el coste efectivo del servicio en función de su uso (y, si se financia con tasas, la tasa va a la Diputación)", "Su asistencia del art. 36 se dirige preferentemente a los servicios mínimos (26.3)"],
         "Municipios de **menos de 20.000** habitantes",
         "Es **coordinación** de la Diputación (la competencia sigue siendo municipal)."))}

?> **Aviso de vigencia (nota del BOE al texto consolidado).** [[BOE]] En el art. 26.2, el BOE señala como «inconstitucionales y nulos» los incisos destacados del párrafo sobre la propuesta de la Diputación al Ministerio (Sentencia del TC 111/2016, de 9 de junio). Por eso ese párrafo no se reproduce arriba.
""", 2)

T.ap("s17", "III.9 Competencias delegadas (art. 27)", f"""
{unidad("9.1 La delegación de competencias en los municipios (art. 27)",
  lit(L, "Artículo 27", ["El Estado y las Comunidades Autónomas", "no podrá ser inferior a cinco años", "requerirá su aceptación por el Municipio interesado", "siendo nula sin dicha dotación", "El acuerdo de renuncia se adoptará por el Pleno"], solo=[1, 2, 3, 4] + list(range(7, 26)) + [27, 28]),
  fichab("Ejercicio por el municipio de competencias del Estado o de la Comunidad Autónoma",
         f"Delegan {c(L, 'Artículo 27', 'El Estado y las Comunidades Autónomas')}; acepta el municipio",
         ["Debe mejorar la eficiencia, eliminar duplicidades y ajustarse a la estabilidad presupuestaria", "Fija alcance, contenido, condiciones, duración, control de eficiencia y medios; memoria económica", "La delegante dirige y controla: instrucciones, información, comisionados, requerimientos; puede revocar o ejecutar por sí misma (27.4)", "Lista orientativa de competencias delegables en el 27.3 (p. ej., promoción y gestión turística)"],
         "Duración **no inferior a cinco años**; **aceptación** del municipio; **financiación** obligatoria (nula sin dotación); la renuncia la acuerda el **Pleno**",
         "**Cinco años** como mínimo (no máximo). Sin dotación presupuestaria, la delegación es **nula**. Los actos del municipio se recurren ante la Administración **delegante**."))}
""", 2)

T.ap("s18", "III.10 Regímenes especiales: concejo abierto y municipios de gran población (arts. 29 y 121)", f"""
{unidad("10.1 Concejo abierto (art. 29)",
  lit(L, "Artículo 29", ["tradicional y voluntariamente", "petición de la mayoría de los vecinos, decisión favorable por mayoría de dos tercios de los miembros del Ayuntamiento y aprobación por la Comunidad Autónoma", "un Alcalde y una asamblea vecinal de la que forman parte todos los electores", "menos de 100 residentes"]),
  fichab("Régimen de gobierno municipal por asamblea de vecinos",
         "Gobierno: un Alcalde y la asamblea vecinal (todos los electores)",
         ["Municipios que tradicional y voluntariamente lo tengan (29.1 a)", "Otros, por localización geográfica, mejor gestión u otras circunstancias (29.1 b)", "Alcaldes de municipios de menos de 100 residentes: pueden convocar a los vecinos a concejo abierto para decisiones de especial trascendencia (29.4)"],
         "Supuesto b): petición de la **mayoría de los vecinos** + **dos tercios** de los miembros del Ayuntamiento + aprobación de la **Comunidad Autónoma**",
         "Funciona según **usos, costumbres y tradiciones locales** y, en su defecto, la Ley 7/1985 y las leyes autonómicas. Las atribuciones del Pleno las ejerce la **Asamblea vecinal** (22.2 → III.5.1)."))}

{unidad("10.2 Municipios de gran población: ámbito (art. 121)",
  lit(L, "Artículo 121", ["supere los 250.000 habitantes", "superior a los 175.000 habitantes", "capitales de provincia, capitales autonómicas o sedes de las instituciones autonómicas", "supere los 75.000 habitantes", "Asambleas Legislativas correspondientes a iniciativa de los respectivos ayuntamientos"], solo=[1, 2, 3, 4, 5, 6, 9]),
  fichab("Municipios a los que se aplica el título X de la Ley 7/1985",
         ["Más de 250.000 habitantes", "Capitales de provincia de más de 175.000", "Capitales de provincia, capitales autonómicas o sedes de instituciones autonómicas (si lo decide la Asamblea Legislativa)", "Más de 75.000 con circunstancias especiales (si lo decide la Asamblea Legislativa)"],
         "En los supuestos c) y d), decisión de la **Asamblea Legislativa** autonómica a iniciativa del ayuntamiento",
         "Una vez incluidos, siguen en el régimen aunque su población baje del límite (121.3)",
         "**250.000** en general; **175.000** si es capital de provincia; **75.000** con circunstancias especiales. En c) y d) decide el **Parlamento autonómico**, no el Gobierno."))}

{resumen([
  "Art. 140 CE: autonomía **garantizada**; Ayuntamiento = **Alcalde + Concejales**; el Alcalde lo eligen los **Concejales o los vecinos**.",
  "Elementos: **territorio, población y organización** (11); nuevos municipios, **al menos 4.000 habitantes** (13.2); vecino desde la **inscripción en el Padrón** (15).",
  "Órganos en todos: **Alcalde, Tenientes de Alcalde y Pleno**; Junta de Gobierno Local con **más de 5.000** habitantes (20).",
  "Alcalde: preside, dirige, **dicta bandos**; Pleno: **control y fiscalización**, ordenanzas, **lesividad**; Junta: hasta **un tercio** de los Concejales (21 a 23).",
  "Competencias propias (25), servicios mínimos por tramos **5.000 / 20.000 / 50.000** (26) y delegadas **por al menos cinco años** (27).",
  "Concejo abierto (29) y gran población: **250.000 / 175.000 / 75.000** (121)."],
  "Siguiente: IV. ¿Cómo se organiza la provincia y qué competencias tiene?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Cómo se organiza la provincia y qué competencias tiene? (art. 141 CE; Ley 7/1985, arts. 31 a 41)", donde(
  "Cuarta pregunta. La provincia es la otra entidad local que nombra la Constitución. Su órgano es la **Diputación**, con una organización paralela a la municipal y unas competencias centradas en **ayudar y coordinar a los municipios**.",
  ["1 La provincia en la Constitución y en la Ley 7/1985 (art. 141.1 y 2 CE; art. 31)", "2 Organización: órganos necesarios y Pleno (arts. 32 y 33)", "3 Presidente, Junta de Gobierno y Vicepresidentes (arts. 34 y 35)", "4 Competencias de la Diputación (arts. 36 y 37)", "5 Regímenes especiales: territorios forales, comunidades uniprovinciales e islas (arts. 38 a 41)", "6 Cuadro comparativo: municipio y provincia"]))

T.ap("s19", "IV.1 La provincia en la Constitución y en la Ley 7/1985 (art. 141.1 y 2 CE; art. 31)", f"""
{unidad("1.1 La provincia en la Constitución (art. 141.1 y 2)",
  lit("CE", "Artículo 141", ["entidad local con personalidad jurídica propia", "agrupación de municipios y división territorial para el cumplimiento de las actividades del Estado", "por las Cortes Generales mediante ley orgánica", "Diputaciones u otras Corporaciones de carácter representativo"], solo=[1, 2]),
  fichab("Doble naturaleza de la provincia y garantía de sus límites",
         f"Gobierno y administración autónoma: {c('CE', 'Artículo 141', 'Diputaciones u otras Corporaciones de carácter representativo')}",
         ["Entidad local con personalidad jurídica propia", "Agrupación de municipios", "División territorial para el cumplimiento de las actividades del Estado"],
         "Alteración de los límites provinciales: **Cortes Generales mediante ley orgánica**",
         "Ni el Gobierno, ni las Diputaciones, ni los Ayuntamientos: los límites provinciales los altera **una ley orgánica de las Cortes**. Cayó en 2025 (→ Cierre 1)."))}

{unidad("1.2 Concepto y fines de la provincia (art. 31)",
  lit(L, "Artículo 31", ["determinada por la agrupación de Municipios", "solidaridad y equilibrio intermunicipales", "prestación integral y adecuada en la totalidad del territorio provincial"]),
  fichab("Para qué existe la provincia",
         "La Provincia; su gobierno corresponde a la Diputación u otras Corporaciones representativas (31.3)",
         ["Garantizar la solidaridad y el equilibrio intermunicipales", "Asegurar la prestación integral y adecuada de los servicios municipales en todo el territorio provincial", "Participar en la coordinación de la Administración local con la autonómica y la estatal"],
         "—",
         "El fin propio es la **solidaridad y el equilibrio intermunicipales**: la provincia está al servicio de los **municipios**."))}
""", 2)

T.ap("s20", "IV.2 Organización: órganos necesarios y Pleno (arts. 32 y 33)", f"""
{unidad("2.1 Órganos necesarios de la Diputación (art. 32)",
  lit(L, "Artículo 32", ["El Presidente, los Vicepresidentes, la Junta de Gobierno y el Pleno existen en todas las Diputaciones"], solo=[1, 2, 3, 4, 5]),
  fichab("Organización provincial",
         ["En todas las Diputaciones: Presidente, Vicepresidentes, Junta de Gobierno y Pleno", "Órganos de estudio, informe o consulta y seguimiento de la gestión (salvo otra forma prevista por la ley autonómica)"],
         "Los órganos complementarios los regulan las Diputaciones; las leyes autonómicas pueden añadir organización complementaria",
         "Grupos políticos representados en proporción a sus Diputados",
         "A diferencia del municipio, en la Diputación la **Junta de Gobierno existe siempre**."))}

{unidad("2.2 El Pleno de la Diputación (art. 33)",
  lit(L, "Artículo 33", ["constituido por el Presidente y los Diputados", "La aprobación de los planes de carácter provincial", "El control y la fiscalización de los órganos de gobierno", "La declaración de lesividad de los actos de la Diputación"], solo=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19, 20]),
  fichab("Órgano de máxima deliberación de la provincia",
         c(L, 'Artículo 33', 'el Presidente y los Diputados'),
         ["Organización de la Diputación; ordenanzas; presupuestos", "Planes de carácter provincial", "Control y fiscalización de los órganos de gobierno", "Plantilla y relación de puestos de trabajo", "Declaración de lesividad de los actos de la Diputación", "Moción de censura al Presidente y cuestión de confianza (33.3)"],
         "Delegable en el Presidente y en la Comisión de Gobierno, salvo las letras a), b), c), d), e), f), h) y ñ) del 33.2 y el 33.3",
         "Atribución **propia del Pleno provincial**: aprobar los **planes de carácter provincial**."))}
""", 2)

T.ap("s21", "IV.3 Presidente, Junta de Gobierno y Vicepresidentes (arts. 34 y 35)", f"""
{unidad("3.1 El Presidente de la Diputación (art. 34)",
  lit(L, "Artículo 34", ["Dirigir el gobierno y la administración de la provincia", "Asegurar la gestión de los servicios propios de la Comunidad Autónoma", "El Presidente puede delegar el ejercicio de sus atribuciones, salvo", "el nombramiento de los Vicepresidentes"], solo=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18, 19]),
  fichab("Órgano ejecutivo de la provincia",
         c(L, 'Artículo 34', 'Presidente de la Diputación'),
         ["Dirige el gobierno y la administración de la provincia y representa a la Diputación", "Convoca y preside Pleno y Junta de Gobierno; voto de calidad", "Asegura la gestión de los servicios de la Comunidad Autónoma encomendados a la Diputación", "Jefatura superior del personal", "Nombra a los Vicepresidentes (34.3)"],
         "Indelegables: convocar y presidir Pleno y Junta, voto de calidad, operaciones de crédito, jefatura superior del personal, separación y despido, y las letras a), i) y j)",
         "Paralelo al Alcalde, con una atribución propia: **asegurar la gestión de los servicios de la Comunidad Autónoma** encomendados a la Diputación."))}

{unidad("3.2 Junta de Gobierno y Vicepresidentes (art. 35)",
  lit(L, "Artículo 35", ["no superior al tercio del número legal de los mismos", "por el orden de su nombramiento", "libremente designados por éste entre los miembros de la Junta de Gobierno"]),
  fichab("Asistencia y sustitución del Presidente",
         ["Junta: el Presidente y Diputados nombrados y separados libremente por él, dando cuenta al Pleno", "Vicepresidentes: designados por el Presidente entre los miembros de la Junta"],
         ["Junta: asiste al Presidente y ejerce las atribuciones delegadas o legales", "Vicepresidentes: sustituyen al Presidente por el orden de nombramiento en vacante, ausencia o enfermedad"],
         "Diputados en la Junta: **no superior al tercio** del número legal",
         "Mismo esquema que en el municipio: **un tercio**; los Vicepresidentes salen de la **Junta de Gobierno**."))}
""", 2)

T.ap("s22", "IV.4 Competencias de la Diputación (arts. 36 y 37)", f"""
{unidad("4.1 Competencias propias (art. 36.1)",
  lit(L, "Artículo 36", ["La coordinación de los servicios municipales entre sí", "La asistencia y cooperación jurídica, económica y técnica a los Municipios", "en los municipios de menos de 1.000 habitantes la prestación de los servicios de secretaría e intervención", "tratamiento de residuos en los municipios de menos de 5.000 habitantes", "prevención y extinción de incendios en los de menos de 20.000 habitantes"], solo=list(range(1, 11))),
  fichab("Lo que la Diputación hace en todo caso",
         c(L, 'Artículo 36', 'la Diputación o entidad equivalente'),
         ["Coordinación de los servicios municipales entre sí", "Asistencia y cooperación jurídica, económica y técnica a los municipios", "Servicios supramunicipales y, en su caso, supracomarcales", "Cooperación en el fomento del desarrollo económico y social", "Recaudación, apoyo financiero, administración electrónica y contratación centralizada en municipios de menos de 20.000 habitantes", "Seguimiento de los costes efectivos de los servicios municipales"],
         "Secretaría e intervención: municipios de **menos de 1.000**; residuos (si el municipio no presta el servicio): **menos de 5.000**; incendios: **menos de 20.000**",
         "Además de las competencias que le atribuyan las leyes estatales y autonómicas, las del 36.1 las tiene **en todo caso**."))}

{unidad("4.2 El plan provincial de cooperación (art. 36.2 a)",
  lit(L, "Artículo 36", ["Aprueba anualmente un plan provincial de cooperación a las obras y servicios de competencia municipal"], solo=[11, 12]),
  fichab("Instrumento principal de la cooperación provincial",
         "La Diputación lo aprueba; participan los municipios de la provincia",
         "Con memoria justificativa y criterios de distribución objetivos y equitativos (entre ellos, los costes efectivos de los servicios)",
         "**Anual**",
         "Se financia con medios propios de la Diputación, aportaciones municipales y subvenciones de la Comunidad Autónoma y del Estado; la Comunidad Autónoma coordina los planes provinciales."))}

{unidad("4.3 Competencias delegadas y encomiendas (art. 37)",
  lit(L, "Artículo 37", ["sujeción plena a las instrucciones generales y particulares de las Comunidades", "previa consulta e informe de la Comunidad Autónoma interesada", "competencias de mera ejecución"]),
  fichab("La Diputación como gestora de competencias ajenas",
         ["Comunidades Autónomas: delegan competencias o encomiendan la gestión ordinaria de servicios propios", "Estado: delega competencias de mera ejecución"],
         "La delegación se ajusta al art. 27 (→ III.9.1)",
         "Estado: **previa consulta e informe** de la Comunidad Autónoma interesada",
         "El Estado solo delega competencias **de mera ejecución** y cuando el ámbito provincial sea el más idóneo."))}
""", 2)

T.ap("s23", "IV.5 Regímenes especiales: territorios forales, comunidades uniprovinciales e islas (arts. 38 a 41)", f"""
{unidad("5.1 Otras Corporaciones representativas y territorios forales (arts. 38 y 39)",
  lit(L, "Artículo 38", ["aquellas otras Corporaciones de carácter representativo"]),
  lit(L, "Artículo 39", ["Álava, Guipúzcoa y Vizcaya", "con carácter supletorio"]),
  fichab("Provincias con órganos distintos de la Diputación ordinaria",
         ["Otras Corporaciones representativas a las que corresponda el gobierno de la provincia (38)", "Órganos forales de Álava, Guipúzcoa y Vizcaya (39)"],
         "Los órganos forales conservan su régimen peculiar en el marco del Estatuto de Autonomía del País Vasco",
         "—",
         "Para los territorios forales vascos, la Ley 7/1985 es **supletoria**."))}

{unidad("5.2 Comunidades Autónomas uniprovinciales y Navarra (art. 40)",
  lit(L, "Artículo 40", ["Las Comunidades Autónomas uniprovinciales y la Foral de Navarra", "Islas Baleares"]),
  fichab("Comunidades que asumen las funciones de las Diputaciones",
         "Las Comunidades Autónomas uniprovinciales y la Comunidad Foral de Navarra",
         "Asumen las competencias, medios y recursos de las Diputaciones Provinciales del régimen ordinario",
         "—",
         "Excepción expresa: **Islas Baleares**, según su Estatuto."))}

{unidad("5.3 Cabildos y Consejos insulares (art. 41)",
  lit(L, "Artículo 41", ["Los Cabildos Insulares Canarios", "supletoriamente por las normas que regulan la organización y funcionamiento de las Diputaciones provinciales", "mancomunidades provinciales interinsulares", "Los Consejos Insulares de las Islas Baleares"]),
  fichab("Gobierno de las islas (art. 141.4 CE → I.1.2)",
         ["Canarias: Cabildos Insulares, órganos de gobierno, administración y representación de cada isla", "Baleares: Consejos Insulares"],
         ["Cabildos: disposición adicional decimocuarta de la Ley 7/1985 y, supletoriamente, las normas de las Diputaciones; asumen sus competencias", "Mancomunidades provinciales interinsulares canarias: solo órganos de representación y expresión de los intereses provinciales"],
         "—",
         "**Cabildos** = Canarias; **Consejos** = Baleares. Las mancomunidades interinsulares canarias **no** gobiernan las islas: solo **representan** los intereses provinciales."))}
""", 2)

T.ap("s24", "IV.6 Cuadro comparativo: municipio y provincia (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| | Municipio | Provincia |
|---|---|---|
| Constitución | Art. 140 | Art. 141.1 y 2 |
| Órgano de gobierno | Ayuntamiento: Alcalde y Concejales (19) | Diputación u otras Corporaciones representativas (31.3) |
| Órganos en todos | Alcalde, Tenientes de Alcalde y Pleno (20.1 a) | Presidente, Vicepresidentes, Junta de Gobierno y Pleno (32.1) |
| Junta de Gobierno | Más de 5.000 habitantes o si lo acuerdan (20.1 b); hasta un tercio de los Concejales (23.1) | Siempre (32.1); hasta un tercio de los Diputados (35.1) |
| Sustitutos | Tenientes de Alcalde (23.3) | Vicepresidentes (35.4) |
| Competencias | Propias (25), servicios mínimos (26), delegadas (27) | Propias (36), delegadas y encomiendas (37) |
| Lesividad | Pleno (22.2 k) | Pleno (33.2 j) |

{resumen([
  "Provincia: entidad local con **personalidad jurídica propia**, agrupación de municipios y división territorial del Estado; límites, solo por **ley orgánica** de las Cortes (141.1).",
  "Fin propio: **solidaridad y equilibrio intermunicipales** (31.2).",
  "Órganos: **Presidente, Vicepresidentes, Junta de Gobierno y Pleno** en todas las Diputaciones (32); el Pleno aprueba los **planes provinciales** (33).",
  "Competencias: coordinación y **asistencia a los municipios**; secretaría e intervención en los de **menos de 1.000** habitantes; **plan provincial anual** (36).",
  "Regímenes especiales: territorios forales (39), CC. AA. uniprovinciales y Navarra (40), **Cabildos** canarios y **Consejos** baleares (41)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX = [
 ("L", 15, "Administración de las islas (→ I.1.2)", {
   "a": "Cambia el órgano: el art. 141.4 no habla de Diputaciones sino de **Cabildos o Consejos** como administración propia de las islas.",
   "b": f"Cambia el órgano: la mancomunidad es la asociación de municipios {c(L, 'Artículo 44', 'para la ejecución en común de obras y servicios determinados de su competencia')} (Ley 7/1985, art. 44), no la administración de la isla.",
   "c": f"Literal del art. 141.4: {c('CE', 'Artículo 141', 'En los archipiélagos, las islas tendrán además su administración propia en forma de Cabildos o Consejos')}.",
   "d": "Cambia el órgano: el art. 141.4 atribuye la administración propia de las islas a **Cabildos o Consejos**, no a Delegaciones del Gobierno (que se estudian en el tema I.8)."},
   [("Cabildos o Consejos", "CE", "Artículo 141", "en forma de Cabildos o Consejos")]),
 ("L", 16, "Órganos del municipio (→ III.3.2, → III.5.1 y → III.6.1)", {
   "a": f"La Junta de Gobierno Local no existe en todos: {c(L, 'Artículo 20', 'La Junta de Gobierno Local existe en todos los municipios con población superior a 5.000 habitantes')} (art. 20.1 b); en todos solo existen {c(L, 'Artículo 20', 'El Alcalde, los Tenientes de Alcalde y el Pleno')}.",
   "b": f"Cambia quién los designa: los Tenientes de Alcalde son {c(L, 'Artículo 23', 'libremente designados y removidos por éste de entre los miembros de la Junta de Gobierno Local')} (por el Alcalde; art. 23.3), no por los miembros del Pleno.",
   "c": f"El Alcalde sí es el Presidente de la Corporación (art. 21.1), pero el control y la fiscalización corresponden al Pleno: {c(L, 'Artículo 22', 'El control y la fiscalización de los órganos de gobierno')} (art. 22.2 a).",
   "d": f"Literal del art. 22.2 k): corresponden {c(L, 'Artículo 22', 'al Pleno municipal en los Ayuntamientos, y a la Asamblea vecinal en el régimen de Concejo Abierto')} … {c(L, 'Artículo 22', 'La declaración de lesividad de los actos del Ayuntamiento')}."},
   [("declaración de lesividad de los actos del Ayuntamiento", L, "Artículo 22", "La declaración de lesividad de los actos del Ayuntamiento"),
    ("Asamblea vecinal en el régimen de Concejo Abierto", L, "Artículo 22", "al Pleno municipal en los Ayuntamientos, y a la Asamblea vecinal en el régimen de Concejo Abierto")]),
 ("X", 25, "Áreas metropolitanas (→ I.3.2)", {
   "a": f"Cambia la entidad: la mancomunidad nace del derecho de los municipios {c(L, 'Artículo 44', 'a asociarse con otros en mancomunidades para la ejecución en común de obras y servicios determinados de su competencia')} (art. 44.1).",
   "b": f"Literal del art. 43.2: {c(L, 'Artículo 43', 'Las áreas metropolitanas son entidades locales integradas por los Municipios de grandes aglomeraciones urbanas')} entre cuyos núcleos existan vinculaciones que hagan necesaria la planificación conjunta.",
   "c": f"Cambia la entidad: la comarca agrupa municipios {c(L, 'Artículo 42', 'cuyas características determinen intereses comunes precisados de una gestión propia o demanden la prestación de servicios de dicho ámbito')} (art. 42.1); no se define por las grandes aglomeraciones urbanas.",
   "d": f"La pedanía es una denominación tradicional de los entes de ámbito inferior al municipio, que {c(L, 'Artículo 24 bis', 'carecerán de personalidad jurídica')} (art. 24 bis); no agrupa municipios."},
   [("área metropolitana", L, "Artículo 43", "Las áreas metropolitanas son entidades locales integradas por los Municipios de grandes aglomeraciones urbanas")]),
 ("X", 26, "Límites provinciales (→ IV.1.1)", {
   "a": "Cambia el órgano y la norma: no basta un Real Decreto del Gobierno; el art. 141.1 exige ley orgánica de las Cortes Generales.",
   "b": "Cambia el órgano: las Diputaciones gobiernan la provincia (art. 141.2), pero no aprueban la alteración de sus límites.",
   "c": f"Literal del art. 141.1: {c('CE', 'Artículo 141', 'Cualquier alteración de los límites provinciales habrá de ser aprobada por las Cortes Generales mediante ley orgánica')}.",
   "d": f"Cambia el órgano: los Ayuntamientos no pueden; incluso la alteración de términos municipales no puede suponer {c(L, 'Artículo 13', 'en ningún caso, modificación de los límites provinciales')} (Ley 7/1985, art. 13.1)."},
   [("Cortes Generales mediante ley orgánica", "CE", "Artículo 141", "habrá de ser aprobada por las Cortes Generales mediante ley orgánica")]),
 ("X", 27, "Competencias propias del municipio (→ III.7.1)", {
   "a": f"«Turismo» en general no está en el art. 25.2; solo {c(L, 'Artículo 25', 'Información y promoción de la actividad turística de interés y ámbito local')} (letra h). La {c(L, 'Artículo 27', 'Promoción y gestión turística')} es competencia que el Estado y las Comunidades Autónomas pueden delegar (art. 27.3 j).",
   "b": "La pesca en aguas interiores no figura entre las materias del art. 25.2.",
   "c": f"Literal del art. 25.2 o): {c(L, 'Artículo 25', 'Actuaciones en la promoción de la igualdad entre hombres y mujeres así como contra la violencia de género')}.",
   "d": f"«Sanidad» en general no está en el art. 25.2; solo {c(L, 'Artículo 25', 'Protección de la salubridad pública')} (letra j)."},
   [("promoción de la igualdad entre hombres y mujeres así como contra la violencia de género", L, "Artículo 25", "Actuaciones en la promoción de la igualdad entre hombres y mujeres así como contra la violencia de género")]),
]
NOMBRE = {"L": "GACE-L", "P": "GACE-P", "X": "GACE-L extraordinario"}
bloques = []
for cod, n, tit, por, ap_ in EX:
    bloques += [f"### {NOMBRE[cod]} 2025, pregunta {n} · {tit}", examen(cod, n, por, ap_)]

T.ap("s25", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **cinco** preguntas de este tema: dos en el turno libre (islas y órganos del municipio) y tres en el extraordinario (áreas metropolitanas, límites provinciales y competencias propias). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal."] + bloques + [
  "### Cómo se pregunta",
  "!> Dos técnicas: **cambiar el órgano** (Tenientes de Alcalde designados por el Pleno, control y fiscalización por el Alcalde, límites provinciales por el Gobierno) y **colar una materia que no está en la lista** (turismo o sanidad en general, en lugar de la letra literal del art. 25.2). Memoriza **quién hace qué** y la **letra** de las listas.",
]))

T.ap("s26", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Entidades | Municipios, provincias y CC. AA. (137); islas (141.4); territoriales: Municipio, Provincia, Isla (art. 3); comarcas, áreas metropolitanas, mancomunidades (42 a 44) | Islas: **Cabildos o Consejos**; área metropolitana = **grandes aglomeraciones urbanas** |
| II. Autonomía | Gestión de sus intereses (137); suficiencia financiera (142); Carta Europea (3 y 4); potestades (art. 4); competencias propias por Ley o delegadas (7); conflicto en defensa de la autonomía local | Competencias propias **solo por Ley**; conflicto: **un séptimo** de municipios y **un sexto** de población |
| III. Municipio | Alcalde y Concejales (140); elementos (11); órganos (20 a 23); competencias (25 a 27); concejo abierto (29); gran población (121) | JGL con **más de 5.000** habitantes; lesividad del **Pleno**; Tenientes los designa el **Alcalde**; igualdad y violencia de género, competencia **propia** |
| IV. Provincia | Personalidad propia y límites por ley orgánica (141); fines (31); órganos (32 a 35); competencias (36 y 37); regímenes especiales (39 a 41) | Límites: **Cortes, ley orgánica**; secretaría e intervención en municipios de **menos de 1.000** |

?> **Trampas frecuentes:** «la Junta de Gobierno Local existe en **todos** los ayuntamientos» (solo con más de 5.000 habitantes o si se acuerda); «los Tenientes de Alcalde los designa el **Pleno**» (los designa el **Alcalde**); «el **Alcalde** ejerce el control y la fiscalización» (es el **Pleno**); «límites provinciales por **Real Decreto**» (por **ley orgánica** de las Cortes); «delegación por un **máximo** de cinco años» (es un **mínimo**); «la comarca la crean los **municipios**» (la crea la **Comunidad Autónoma**; los municipios forman **mancomunidades**).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
T.q("CE", "Artículo 137", "Entidades locales", "Según el artículo 137 de la Constitución, el Estado se organiza territorialmente en:",
    ["Municipios, provincias y las Comunidades Autónomas que se constituyan.", "Municipios, comarcas y Comunidades Autónomas.", "Provincias y Comunidades Autónomas.", "Municipios, provincias, áreas metropolitanas y Comunidades Autónomas."],
    "Art. 137 CE: «en municipios, en provincias y en las Comunidades Autónomas que se constituyan».", "El Estado se organiza territorialmente en municipios, en provincias y en las Comunidades Autónomas que se constituyan")
T.q("CE", "Artículo 141", "Entidades locales", "Según el artículo 141.3 de la Constitución, se podrán crear:",
    ["Agrupaciones de municipios diferentes de la provincia.", "Nuevas provincias por ley ordinaria.", "Comunidades Autónomas interinsulares.", "Agrupaciones de provincias distintas de las Comunidades Autónomas."],
    "Art. 141.3 CE.", "Se podrán crear agrupaciones de municipios diferentes de la provincia")
T.q(L, "Artículo 3", "Entidades locales", "Según el artículo 3.1 de la Ley 7/1985, son Entidades Locales territoriales:",
    ["El Municipio, la Provincia y la Isla en los archipiélagos balear y canario.", "El Municipio, la Provincia y la Comarca.", "El Municipio, la Provincia y el Área Metropolitana.", "El Municipio, la Provincia y la Mancomunidad de Municipios."],
    "Art. 3.1 Ley 7/1985: Municipio, Provincia e Isla. Comarcas, áreas metropolitanas y mancomunidades son entidades locales del 3.2, no territoriales.", ["a) El Municipio.", "b) La Provincia.", "c) La Isla en los archipiélagos balear y canario."])
T.q(L, "Artículo 3", "Entidades locales", "Según el artículo 3.2 de la Ley 7/1985, gozan asimismo de la condición de Entidades Locales:",
    ["Las Mancomunidades de Municipios.", "Los consorcios.", "Las fundaciones del sector público local.", "Las Delegaciones del Gobierno."],
    "Art. 3.2 Ley 7/1985: comarcas u otras entidades que agrupen varios municipios, áreas metropolitanas y mancomunidades de municipios.", "c) Las Mancomunidades de Municipios.")
T.q(L, "Artículo 42", "Entidades locales", "Según el artículo 42.2 de la Ley 7/1985, no podrá crearse una comarca si a ello se oponen expresamente:",
    ["Las dos quintas partes de los Municipios que debieran agruparse en ella, siempre que representen al menos la mitad del censo electoral del territorio.", "La mitad de los Municipios que debieran agruparse en ella, siempre que representen al menos dos tercios del censo electoral.", "Un tercio de los Municipios que debieran agruparse en ella, cualquiera que sea su población.", "La Diputación Provincial, en todo caso."],
    "Art. 42.2 Ley 7/1985.", "no podrá crearse la comarca si a ello se oponen expresamente las dos quintas partes de los Municipios que debieran agruparse en ella, siempre que, en este caso, tales Municipios representen al menos la mitad del censo electoral del territorio correspondiente")
T.q(L, "Artículo 43", "Entidades locales", "Según el artículo 43.1 de la Ley 7/1985, las áreas metropolitanas se crean, modifican y suprimen:",
    ["Por las Comunidades Autónomas, mediante Ley, previa audiencia de la Administración del Estado y de los Ayuntamientos y Diputaciones afectados.", "Por el Gobierno de la Nación, mediante Real Decreto.", "Por acuerdo de los Ayuntamientos afectados, mediante convenio.", "Por las Diputaciones Provinciales, previa audiencia de la Comunidad Autónoma."],
    "Art. 43.1 Ley 7/1985.", "Las Comunidades Autónomas, previa audiencia de la Administración del Estado y de los Ayuntamientos y Diputaciones afectados, podrán crear, modificar y suprimir, mediante Ley, áreas metropolitanas")
T.q(L, "Artículo 44", "Entidades locales", "Según el artículo 44.3 de la Ley 7/1985, los estatutos de las mancomunidades los aprueban:",
    ["Los Plenos de todos los ayuntamientos.", "La Diputación o Diputaciones provinciales interesadas.", "El Consejo de Gobierno de la Comunidad Autónoma.", "Los Alcaldes de los municipios promotores."],
    "Art. 44.3 c) Ley 7/1985; la Diputación solo emite informe (44.3 b).", "c) Los Plenos de todos los ayuntamientos aprueban los estatutos.")
T.q("CE", "Artículo 142", "Autonomía local", "Según el artículo 142 de la Constitución, las Haciendas locales se nutrirán fundamentalmente de:",
    ["Tributos propios y de participación en los del Estado y de las Comunidades Autónomas.", "Transferencias del Estado y de las Comunidades Autónomas.", "Tasas y precios públicos por la prestación de servicios.", "Tributos propios y de participación en los de la Unión Europea."],
    "Art. 142 CE.", "se nutrirán fundamentalmente de tributos propios y de participación en los del Estado y de las Comunidades Autónomas")
T.q("CEAL", "a3", "Autonomía local", "Según el artículo 3.1 de la Carta Europea de Autonomía Local, por autonomía local se entiende el derecho y la capacidad efectiva de las Entidades locales de ordenar y gestionar:",
    ["Una parte importante de los asuntos públicos, en el marco de la Ley, bajo su propia responsabilidad y en beneficio de sus habitantes.", "La totalidad de los asuntos públicos de su territorio, sin sujeción a la Ley.", "Los asuntos que les delegue el Estado, bajo la responsabilidad de este.", "Una parte importante de los asuntos públicos, bajo la tutela de la autoridad central o regional."],
    "Art. 3.1 de la Carta Europea de Autonomía Local.", "ordenar y gestionar una parte importante de los asuntos públicos, en el marco de la Ley, bajo su propia responsabilidad y en beneficio de sus habitantes")
T.q("CEAL", "a4", "Autonomía local", "Según el artículo 4.3 de la Carta Europea de Autonomía Local, el ejercicio de las competencias públicas debe, de modo general, incumbir preferentemente a:",
    ["Las autoridades más cercanas a los ciudadanos.", "Las autoridades centrales.", "Las autoridades regionales.", "Las autoridades con mayor capacidad financiera."],
    "Art. 4.3 de la Carta.", "incumbir preferentemente a las autoridades más cercanas a los ciudadanos")
T.q(L, "Artículo 1", "Autonomía local", "Según el artículo 1.1 de la Ley 7/1985, los Municipios son:",
    ["Entidades básicas de la organización territorial del Estado y cauces inmediatos de participación ciudadana en los asuntos públicos.", "Divisiones territoriales para el cumplimiento de las actividades del Estado.", "Órganos desconcentrados de las Comunidades Autónomas.", "Entidades instrumentales de las provincias."],
    "Art. 1.1 Ley 7/1985. La «división territorial para el cumplimiento de las actividades del Estado» es la provincia (art. 141.1 CE).", "Los Municipios son entidades básicas de la organización territorial del Estado y cauces inmediatos de participación ciudadana en los asuntos públicos")
T.q(L, "Artículo 2", "Autonomía local", "Según el artículo 2.1 de la Ley 7/1985, la legislación estatal y autonómica atribuirá competencias a los entes locales de conformidad con los principios de:",
    ["Descentralización y de máxima proximidad de la gestión administrativa a los ciudadanos.", "Jerarquía y desconcentración.", "Solidaridad y equilibrio intermunicipales.", "Eficacia, jerarquía y coordinación."],
    "Art. 2.1 Ley 7/1985. «solidaridad y equilibrio intermunicipales» son los fines de la provincia (art. 31.2).", "de conformidad con los principios de descentralización y de máxima proximidad de la gestión administrativa a los ciudadanos")
T.q(L, "Artículo 4", "Autonomía local", "Según el artículo 4.1 de la Ley 7/1985, ¿cuál de las siguientes potestades corresponde en todo caso a los municipios, las provincias y las islas?",
    ["La potestad expropiatoria.", "La potestad legislativa.", "La potestad jurisdiccional.", "La potestad de indulto."],
    "Art. 4.1 d) Ley 7/1985.", "d) Las potestades expropiatoria y de investigación, deslinde y recuperación de oficio de sus bienes.")
T.q(L, "Artículo 7", "Autonomía local", "Según el artículo 7.2 de la Ley 7/1985, las competencias propias de los Municipios, las Provincias, las Islas y demás Entidades Locales territoriales:",
    ["Solo podrán ser determinadas por Ley.", "Podrán ser determinadas por Ley o por reglamento.", "Se determinan en los reglamentos orgánicos de cada entidad.", "Se determinan por acuerdo de la Conferencia Sectorial."],
    "Art. 7.2 Ley 7/1985.", "solo podrán ser determinadas por Ley")
T.q("LOTC", "asetentaycincobis", "Autonomía local", "Según el artículo 75 bis de la Ley Orgánica del Tribunal Constitucional, pueden dar lugar al planteamiento de los conflictos en defensa de la autonomía local:",
    ["Las normas del Estado con rango de ley o las disposiciones con rango de ley de las Comunidades Autónomas.", "Los reglamentos del Estado y de las Comunidades Autónomas.", "Los actos administrativos de las Diputaciones Provinciales.", "Las ordenanzas municipales de otros municipios."],
    "Art. 75 bis.1 LOTC.", "las normas del Estado con rango de ley o las disposiciones con rango de ley de las Comunidades Autónomas que lesionen la autonomía local constitucionalmente garantizada")
T.q("LOTC", "asetentaycincoter", "Autonomía local", "Según el artículo 75 ter.1 b) de la LOTC, están legitimados para plantear un conflicto en defensa de la autonomía local un número de municipios que supongan al menos:",
    ["Un séptimo de los existentes en el ámbito territorial de aplicación y representen como mínimo un sexto de la población oficial.", "Un quinto de los existentes y representen como mínimo un cuarto de la población oficial.", "La mitad de los existentes y representen como mínimo la mitad de la población oficial.", "Un tercio de los existentes, cualquiera que sea su población."],
    "Art. 75 ter.1 b) LOTC. «La mitad» y «la mitad» es el requisito de las provincias (letra c).", "al menos un séptimo de los existentes en el ámbito territorial de aplicación de la disposición con rango de ley, y representen como mínimo un sexto de la población oficial")
T.q("LOTC", "asetentaycincoter", "Autonomía local", "Según el artículo 75 ter.2 de la LOTC, para iniciar la tramitación de un conflicto en defensa de la autonomía local se necesita el acuerdo del órgano plenario de las Corporaciones locales con el voto favorable de:",
    ["La mayoría absoluta del número legal de miembros.", "La mayoría simple de los miembros presentes.", "Dos tercios del número legal de miembros.", "Tres quintos del número legal de miembros."],
    "Art. 75 ter.2 LOTC.", "con el voto favorable de la mayoría absoluta del número legal de miembros de las mismas")
T.q("CE", "Artículo 140", "Municipio", "Según el artículo 140 de la Constitución, los Alcaldes serán elegidos:",
    ["Por los Concejales o por los vecinos.", "Por el Pleno de la Diputación Provincial.", "Únicamente por los vecinos, mediante sufragio directo.", "Por el Gobierno de la Comunidad Autónoma, a propuesta de los Concejales."],
    "Art. 140 CE.", "Los Alcaldes serán elegidos por los Concejales o por los vecinos")
T.q(L, "Artículo 11", "Municipio", "Según el artículo 11.2 de la Ley 7/1985, son elementos del Municipio:",
    ["El territorio, la población y la organización.", "El territorio, la población y la hacienda.", "La población, la organización y las competencias.", "El territorio, el Ayuntamiento y el padrón."],
    "Art. 11.2 Ley 7/1985.", "Son elementos del Municipio el territorio, la población y la organización")
T.q(L, "Artículo 13", "Municipio", "Según el artículo 13.2 de la Ley 7/1985, la creación de nuevos municipios solo podrá realizarse sobre la base de núcleos de población territorialmente diferenciados de al menos:",
    ["4.000 habitantes.", "5.000 habitantes.", "2.000 habitantes.", "10.000 habitantes."],
    "Art. 13.2 Ley 7/1985.", "de al menos 4.000 habitantes")
T.q(L, "Artículo 15", "Municipio", "Según el artículo 15 de la Ley 7/1985, la condición de vecino se adquiere:",
    ["En el mismo momento de la inscripción en el Padrón.", "Al año de residencia habitual en el municipio.", "Con la inscripción en el censo electoral.", "Tras la aprobación de la inscripción por el Pleno."],
    "Art. 15 Ley 7/1985.", "La condición de vecino se adquiere en el mismo momento de su inscripción en el Padrón")
T.q(L, "Artículo 20", "Municipio", "Según el artículo 20.1 b) de la Ley 7/1985, la Junta de Gobierno Local existe en todos los municipios con población superior a:",
    ["5.000 habitantes.", "20.000 habitantes.", "1.000 habitantes.", "50.000 habitantes."],
    "Art. 20.1 b) Ley 7/1985; en los de menos, si lo dispone el reglamento orgánico o lo acuerda el Pleno.", "La Junta de Gobierno Local existe en todos los municipios con población superior a 5.000 habitantes")
T.q(L, "Artículo 20", "Municipio", "Según el artículo 20.1 e) de la Ley 7/1985, la Comisión Especial de Cuentas existe:",
    ["En todos los municipios.", "Solo en los municipios de gran población.", "En los municipios de más de 5.000 habitantes.", "Solo si lo acuerda el Pleno por mayoría absoluta."],
    "Art. 20.1 e) Ley 7/1985.", "La Comisión Especial de Cuentas existe en todos los municipios")
T.q(L, "Artículo 21", "Municipio", "Según el artículo 21.1 de la Ley 7/1985, ¿cuál de las siguientes es una atribución del Alcalde?",
    ["Dictar bandos.", "La aprobación del reglamento orgánico y de las ordenanzas.", "El control y la fiscalización de los órganos de gobierno.", "La aprobación de la plantilla de personal."],
    "Art. 21.1 e) Ley 7/1985. Las demás son atribuciones del Pleno (art. 22.2 a, d e i).", "e) Dictar bandos.")
T.q(L, "Artículo 21", "Municipio", "Según el artículo 21.3 de la Ley 7/1985, ¿cuál de las siguientes atribuciones NO puede delegar el Alcalde?",
    ["Decidir los empates con el voto de calidad.", "El otorgamiento de las licencias.", "Dirigir, inspeccionar e impulsar los servicios y obras municipales.", "Sancionar las faltas por infracción de las ordenanzas municipales."],
    "Art. 21.3 Ley 7/1985: el voto de calidad está entre las indelegables; las otras tres (letras q, d y n) no.", "decidir los empates con el voto de calidad")
T.q(L, "Artículo 22", "Municipio", "Según el artículo 22.2 de la Ley 7/1985, corresponde al Pleno municipal:",
    ["La declaración de lesividad de los actos del Ayuntamiento.", "Dictar bandos.", "El nombramiento de los Tenientes de Alcalde.", "Ejercer la jefatura de la Policía Municipal."],
    "Art. 22.2 k) Ley 7/1985. Las demás son del Alcalde (art. 21.1 e e i, y 21.2).", "k) La declaración de lesividad de los actos del Ayuntamiento.")
T.q(L, "Artículo 22", "Municipio", "Según el artículo 22.3 de la Ley 7/1985, las votaciones del Pleno sobre la moción de censura al Alcalde y sobre la cuestión de confianza:",
    ["Serán públicas y se realizarán mediante llamamiento nominal en todo caso.", "Serán secretas, mediante papeleta.", "Serán públicas, por asentimiento.", "Serán secretas salvo que lo pida un tercio de los Concejales."],
    "Art. 22.3 Ley 7/1985.", "que serán públicas y se realizarán mediante llamamiento nominal en todo caso")
T.q(L, "Artículo 23", "Municipio", "Según el artículo 23.1 de la Ley 7/1985, la Junta de Gobierno Local se integra por el Alcalde y un número de Concejales no superior:",
    ["Al tercio del número legal de los mismos.", "A la mitad del número legal de los mismos.", "Al cuarto del número legal de los mismos.", "A dos tercios del número legal de los mismos."],
    "Art. 23.1 Ley 7/1985.", "un número de Concejales no superior al tercio del número legal de los mismos")
T.q(L, "Artículo 23", "Municipio", "Según el artículo 23.3 de la Ley 7/1985, los Tenientes de Alcalde son libremente designados y removidos:",
    ["Por el Alcalde, de entre los miembros de la Junta de Gobierno Local.", "Por el Pleno, de entre los Concejales.", "Por la Junta de Gobierno Local, de entre sus miembros.", "Por el Alcalde, previa aprobación del Pleno."],
    "Art. 23.3 Ley 7/1985.", "libremente designados y removidos por éste de entre los miembros de la Junta de Gobierno Local")
T.q(L, "Artículo 24 bis", "Municipio", "Según el artículo 24 bis de la Ley 7/1985, los entes de ámbito territorial inferior al Municipio:",
    ["Carecerán de personalidad jurídica.", "Tendrán personalidad jurídica propia y plena capacidad.", "Son Entidades Locales territoriales.", "Los regula el Estado mediante ley orgánica."],
    "Art. 24 bis.1 Ley 7/1985.", "que carecerán de personalidad jurídica")
T.q(L, "Artículo 25", "Municipio", "Según el artículo 25.2 de la Ley 7/1985, ¿cuál de las siguientes materias es competencia propia del Municipio?",
    ["Cementerios y actividades funerarias.", "Administración de Justicia.", "Pesca en aguas interiores.", "Defensa nacional."],
    "Art. 25.2 k) Ley 7/1985.", "k) Cementerios y actividades funerarias.")
T.q(L, "Artículo 26", "Municipio", "Según el artículo 26.1 b) de la Ley 7/1985, en los Municipios con población superior a 5.000 habitantes deberán prestarse, además de los servicios comunes a todos:",
    ["Parque público, biblioteca pública y tratamiento de residuos.", "Transporte colectivo urbano de viajeros y medio ambiente urbano.", "Protección civil y prevención y extinción de incendios.", "Instalaciones deportivas de uso público."],
    "Art. 26.1 b) Ley 7/1985. Las demás corresponden a los tramos de más de 20.000 (c) o más de 50.000 habitantes (d).", "En los Municipios con población superior a 5.000 habitantes, además: parque público, biblioteca pública y tratamiento de residuos")
T.q(L, "Artículo 26", "Municipio", "Según el artículo 26.1 d) de la Ley 7/1985, el transporte colectivo urbano de viajeros es servicio obligatorio en los Municipios con población superior a:",
    ["50.000 habitantes.", "20.000 habitantes.", "5.000 habitantes.", "100.000 habitantes."],
    "Art. 26.1 d) Ley 7/1985.", "En los Municipios con población superior a 50.000 habitantes, además: transporte colectivo urbano de viajeros y medio ambiente urbano")
T.q(L, "Artículo 27", "Municipio", "Según el artículo 27.1 de la Ley 7/1985, la duración de la delegación de competencias en los Municipios:",
    ["No podrá ser inferior a cinco años.", "No podrá ser superior a cinco años.", "No podrá ser inferior a diez años.", "Será indefinida."],
    "Art. 27.1 Ley 7/1985.", "que no podrá ser inferior a cinco años")
T.q(L, "Artículo 27", "Municipio", "Según el artículo 27.5 de la Ley 7/1985, la efectividad de la delegación de competencias en un Municipio requerirá:",
    ["Su aceptación por el Municipio interesado.", "Su aprobación por las Cortes Generales.", "El informe favorable de la Diputación Provincial.", "Su publicación en el Boletín Oficial del Estado."],
    "Art. 27.5 Ley 7/1985.", "La efectividad de la delegación requerirá su aceptación por el Municipio interesado")
T.q(L, "Artículo 29", "Municipio", "Según el artículo 29.2 de la Ley 7/1985, la constitución en concejo abierto de los municipios en que lo hagan aconsejable su localización geográfica u otras circunstancias requiere decisión favorable del Ayuntamiento por mayoría de:",
    ["Dos tercios de sus miembros.", "La mitad más uno de sus miembros.", "Tres quintos de sus miembros.", "Unanimidad de sus miembros."],
    "Art. 29.2 Ley 7/1985: petición de la mayoría de los vecinos, dos tercios del Ayuntamiento y aprobación de la Comunidad Autónoma.", "decisión favorable por mayoría de dos tercios de los miembros del Ayuntamiento")
T.q(L, "Artículo 121", "Municipio", "Según el artículo 121.1 a) de la Ley 7/1985, el régimen de los municipios de gran población se aplica a los municipios cuya población supere:",
    ["Los 250.000 habitantes.", "Los 175.000 habitantes.", "Los 100.000 habitantes.", "Los 500.000 habitantes."],
    "Art. 121.1 a) Ley 7/1985. 175.000 es el umbral para las capitales de provincia (letra b).", "A los municipios cuya población supere los 250.000 habitantes")
T.q("CE", "Artículo 141", "Provincia", "Según el artículo 141.2 de la Constitución, el gobierno y la administración autónoma de las provincias estarán encomendados a:",
    ["Diputaciones u otras Corporaciones de carácter representativo.", "Las Delegaciones del Gobierno.", "Los Consejos de Gobierno de las Comunidades Autónomas.", "Las Subdelegaciones del Gobierno."],
    "Art. 141.2 CE.", "estarán encomendados a Diputaciones u otras Corporaciones de carácter representativo")
T.q(L, "Artículo 31", "Provincia", "Según el artículo 31.2 de la Ley 7/1985, son fines propios y específicos de la Provincia garantizar los principios de:",
    ["Solidaridad y equilibrio intermunicipales.", "Descentralización y máxima proximidad.", "Eficacia y jerarquía.", "Autonomía y suficiencia financiera."],
    "Art. 31.2 Ley 7/1985.", "garantizar los principios de solidaridad y equilibrio intermunicipales")
T.q(L, "Artículo 32", "Provincia", "Según el artículo 32 de la Ley 7/1985, existen en todas las Diputaciones:",
    ["El Presidente, los Vicepresidentes, la Junta de Gobierno y el Pleno.", "El Presidente, el Pleno y la Comisión Especial de Cuentas.", "El Presidente y el Pleno; la Junta de Gobierno, solo en provincias de más de 500.000 habitantes.", "El Presidente, los Vicepresidentes y el Pleno."],
    "Art. 32.1 Ley 7/1985: la Junta de Gobierno existe en **todas** las Diputaciones.", "El Presidente, los Vicepresidentes, la Junta de Gobierno y el Pleno existen en todas las Diputaciones")
T.q(L, "Artículo 33", "Provincia", "Según el artículo 33.2 de la Ley 7/1985, corresponde en todo caso al Pleno de la Diputación:",
    ["La aprobación de los planes de carácter provincial.", "Dirigir el gobierno y la administración de la provincia.", "El nombramiento de los Vicepresidentes.", "Representar a la Diputación."],
    "Art. 33.2 d) Ley 7/1985. Las demás son del Presidente (art. 34.1 a y b, y 34.3).", "d) La aprobación de los planes de carácter provincial.")
T.q(L, "Artículo 35", "Provincia", "Según el artículo 35.4 de la Ley 7/1985, los Vicepresidentes de la Diputación son libremente designados:",
    ["Por el Presidente, entre los miembros de la Junta de Gobierno.", "Por el Pleno, entre los Diputados.", "Por la Junta de Gobierno, entre sus miembros.", "Por la Comunidad Autónoma, a propuesta del Presidente."],
    "Art. 35.4 Ley 7/1985.", "siendo libremente designados por éste entre los miembros de la Junta de Gobierno")
T.q(L, "Artículo 36", "Provincia", "Según el artículo 36.1 b) de la Ley 7/1985, la Diputación garantizará la prestación de los servicios de secretaría e intervención en los municipios de menos de:",
    ["1.000 habitantes.", "5.000 habitantes.", "20.000 habitantes.", "2.000 habitantes."],
    "Art. 36.1 b) Ley 7/1985.", "En todo caso garantizará en los municipios de menos de 1.000 habitantes la prestación de los servicios de secretaría e intervención")
T.q(L, "Artículo 37", "Provincia", "Según el artículo 37.2 de la Ley 7/1985, el Estado podrá delegar en las Diputaciones:",
    ["Competencias de mera ejecución, previa consulta e informe de la Comunidad Autónoma interesada.", "Cualquier competencia, sin necesidad de informe autonómico.", "Competencias legislativas en materias de interés provincial.", "Competencias de mera ejecución, previa autorización de las Cortes Generales."],
    "Art. 37.2 Ley 7/1985.", "previa consulta e informe de la Comunidad Autónoma interesada, delegar en las Diputaciones competencias de mera ejecución")
T.q(L, "Artículo 41", "Provincia", "Según el artículo 41.1 de la Ley 7/1985, los Cabildos Insulares Canarios se rigen supletoriamente por:",
    ["Las normas que regulan la organización y funcionamiento de las Diputaciones provinciales.", "Las normas de los municipios de gran población.", "Las normas de las mancomunidades de municipios.", "Las normas de las áreas metropolitanas."],
    "Art. 41.1 Ley 7/1985.", "supletoriamente por las normas que regulan la organización y funcionamiento de las Diputaciones provinciales")
T.real("L", 15, "Entidades locales"); T.real("L", 16, "Municipio"); T.real("X", 25, "Entidades locales"); T.real("X", 26, "Provincia"); T.real("X", 27, "Municipio")

# Flashcards
for q_, a_, cat in [
  ("¿En qué se organiza territorialmente el Estado? (art. 137 CE)", "En municipios, en provincias y en las Comunidades Autónomas que se constituyan; todas con autonomía para la gestión de sus respectivos intereses.", "Entidades locales"),
  ("¿Cómo se administran las islas de los archipiélagos? (art. 141.4 CE)", "Con administración propia en forma de Cabildos o Consejos.", "Entidades locales"),
  ("Entidades Locales territoriales (art. 3.1 Ley 7/1985)", "El Municipio, la Provincia y la Isla en los archipiélagos balear y canario.", "Entidades locales"),
  ("Otras entidades locales (art. 3.2 Ley 7/1985)", "Comarcas u otras entidades que agrupen varios municipios; áreas metropolitanas; mancomunidades de municipios.", "Entidades locales"),
  ("¿Qué es un área metropolitana? (art. 43.2)", "Entidad local integrada por los municipios de grandes aglomeraciones urbanas con vinculaciones económicas y sociales que exigen planificación conjunta y coordinación de servicios y obras.", "Entidades locales"),
  ("¿De qué se nutren las Haciendas locales? (art. 142 CE)", "Fundamentalmente de tributos propios y de participación en los del Estado y de las Comunidades Autónomas.", "Autonomía local"),
  ("Concepto de autonomía local (Carta Europea, art. 3.1)", "Derecho y capacidad efectiva de las Entidades locales de ordenar y gestionar una parte importante de los asuntos públicos, en el marco de la Ley, bajo su propia responsabilidad y en beneficio de sus habitantes.", "Autonomía local"),
  ("Clases de competencias locales (art. 7)", "Propias (solo determinadas por Ley) o atribuidas por delegación; las distintas, con informes necesarios y vinculantes.", "Autonomía local"),
  ("Conflicto en defensa de la autonomía local: ¿contra qué? (LOTC 75 bis)", "Normas del Estado con rango de ley o disposiciones con rango de ley de las Comunidades Autónomas.", "Autonomía local"),
  ("Elementos del Municipio (art. 11.2)", "El territorio, la población y la organización.", "Municipio"),
  ("¿Cuándo se adquiere la condición de vecino? (art. 15)", "En el mismo momento de la inscripción en el Padrón.", "Municipio"),
  ("Órganos que existen en todos los ayuntamientos (art. 20.1 a)", "El Alcalde, los Tenientes de Alcalde y el Pleno (y la Comisión Especial de Cuentas, 20.1 e).", "Municipio"),
  ("¿Cuándo es obligatoria la Junta de Gobierno Local? (art. 20.1 b)", "En los municipios de más de 5.000 habitantes; en los de menos, si lo dispone el reglamento orgánico o lo acuerda el Pleno.", "Municipio"),
  ("¿Quién declara la lesividad de los actos del Ayuntamiento? (art. 22.2 k)", "El Pleno (en concejo abierto, la Asamblea vecinal); el Alcalde solo tiene la iniciativa en materias de su competencia.", "Municipio"),
  ("Composición de la Junta de Gobierno Local (art. 23.1)", "El Alcalde y Concejales en número no superior al tercio del número legal, nombrados y separados libremente por él.", "Municipio"),
  ("Servicios mínimos: umbrales de población (art. 26.1)", "Todos; más de 5.000; más de 20.000; más de 50.000 habitantes.", "Municipio"),
  ("Delegación de competencias en el municipio: duración y requisito de eficacia (art. 27)", "No inferior a cinco años; requiere la aceptación del municipio y financiación (nula sin dotación).", "Municipio"),
  ("Municipios de gran población (art. 121.1)", "Más de 250.000 habitantes; capitales de provincia de más de 175.000; capitales de provincia, capitales autonómicas o sedes de instituciones autonómicas, y más de 75.000 con circunstancias especiales (estos dos, si lo decide la Asamblea Legislativa).", "Municipio"),
  ("¿Quién aprueba la alteración de los límites provinciales? (art. 141.1 CE)", "Las Cortes Generales mediante ley orgánica.", "Provincia"),
  ("Fines propios de la Provincia (art. 31.2)", "Garantizar los principios de solidaridad y equilibrio intermunicipales.", "Provincia"),
  ("Órganos de todas las Diputaciones (art. 32.1)", "Presidente, Vicepresidentes, Junta de Gobierno y Pleno.", "Provincia"),
  ("¿En qué municipios garantiza la Diputación secretaría e intervención? (art. 36.1 b)", "En los de menos de 1.000 habitantes.", "Provincia"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Entidad local territorial", "Municipio, Provincia e Isla en los archipiélagos balear y canario (art. 3.1 Ley 7/1985); tienen las potestades del art. 4.", "s2", "Entidades locales")
T.glos("Comarca", "Entidad local que agrupa varios municipios con intereses comunes, creada por la Comunidad Autónoma de acuerdo con su Estatuto (arts. 3.2 y 42 Ley 7/1985).", "s3", "Entidades locales")
T.glos("Área metropolitana", "Entidad local de los municipios de grandes aglomeraciones urbanas que necesitan planificación conjunta; la crea la Comunidad Autónoma mediante ley (art. 43 Ley 7/1985).", "s3", "Entidades locales")
T.glos("Mancomunidad", "Asociación de municipios para la ejecución en común de obras y servicios determinados de su competencia, con personalidad jurídica y Estatutos propios (art. 44 Ley 7/1985).", "s3", "Entidades locales")
T.glos("Autonomía local", "Derecho y capacidad efectiva de las Entidades locales de ordenar y gestionar una parte importante de los asuntos públicos, en el marco de la Ley y bajo su propia responsabilidad (Carta Europea, art. 3.1).", "s5", "Autonomía local")
T.glos("Competencia propia", "Competencia local determinada solo por Ley y ejercida en régimen de autonomía y bajo la propia responsabilidad (art. 7.2 Ley 7/1985).", "s7", "Autonomía local")
T.glos("Vecino", "Persona inscrita en el Padrón municipal; la condición se adquiere en el mismo momento de la inscripción (art. 15 Ley 7/1985).", "s10", "Municipio")
T.glos("Ayuntamiento", "Órgano de gobierno y administración del municipio, integrado por el Alcalde y los Concejales (art. 140 CE; art. 19 Ley 7/1985).", "s11", "Municipio")
T.glos("Junta de Gobierno Local", "Órgano integrado por el Alcalde y Concejales (no más de un tercio del número legal) que asiste al Alcalde; obligatorio en municipios de más de 5.000 habitantes (arts. 20 y 23 Ley 7/1985).", "s14", "Municipio")
T.glos("Bando", "Disposición que dicta el Alcalde (art. 21.1 e Ley 7/1985); atribución indelegable (art. 21.3).", "s12", "Municipio")
T.glos("Servicios mínimos", "Servicios que los municipios deben prestar en todo caso según su población (art. 26.1 Ley 7/1985).", "s16", "Municipio")
T.glos("Concejo abierto", "Régimen en que el gobierno y la administración municipales corresponden a un Alcalde y a una asamblea vecinal de la que forman parte todos los electores (art. 29 Ley 7/1985).", "s18", "Municipio")
T.glos("Diputación provincial", "Corporación a la que corresponde el gobierno y la administración autónoma de la provincia (art. 141.2 CE; art. 31.3 Ley 7/1985).", "s19", "Provincia")
T.glos("Plan provincial de cooperación", "Plan anual de la Diputación de cooperación a las obras y servicios de competencia municipal, con participación de los municipios (art. 36.2 a Ley 7/1985).", "s22", "Provincia")
T.glos("Cabildo insular", "Órgano de gobierno, administración y representación de cada isla canaria (art. 141.4 CE; art. 41.1 Ley 7/1985).", "s23", "Provincia")

# Cronología (fechas de los metadatos del BOE)
T.hito("1978", "Constitución Española (27-12-1978; BOE de 29-12-1978)", "Arts. 137 y 140 a 142: municipios, provincias, islas y Haciendas locales", "normativo", "s1")
T.hito("1985", "Ley 7/1985, de 2 de abril, Reguladora de las Bases del Régimen Local (BOE de 3-4-1985)", "Régimen común del municipio, la provincia y las demás entidades locales", "normativo", "s2")
T.hito("1989", "Carta Europea de Autonomía Local, hecha en Estrasburgo el 15-10-1985 (instrumento de ratificación publicado en el BOE de 24-2-1989)", "Art. 3: concepto de autonomía local", "normativo", "s5")
T.hito("1999", "Ley Orgánica 7/1999, de 21 de abril (BOE de 22-4-1999)", "Arts. 75 bis y siguientes LOTC: conflicto en defensa de la autonomía local", "normativo", "s8")
T.hito("2003", "Ley 57/2003, de 16 de diciembre, de medidas para la modernización del gobierno local (BOE de 17-12-2003)", "Añade el título X (municipios de gran población; art. 121)", "normativo", "s18")
T.hito("2013", "Ley 27/2013, de 27 de diciembre, de racionalización y sostenibilidad de la Administración Local (BOE de 30-12-2013)", "Nueva redacción de los arts. 7, 25, 26 y 27 y nuevo art. 24 bis", "normativo", "s7")
T.hito("2018", "Real Decreto-ley 9/2018, de 3 de agosto (BOE de 4-8-2018)", "Añade la letra o) del art. 25.2: igualdad entre hombres y mujeres y violencia de género", "normativo", "s15")
T.hito("2026", "Real Decreto-ley 7/2026, de 20 de marzo (BOE de 21-3-2026)", "Añade la letra p) del art. 25.2: comunidades ciudadanas de energía y transición energética", "normativo", "s15")

T.publicar()
