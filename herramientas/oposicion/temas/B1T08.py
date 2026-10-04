# -*- coding: utf-8 -*-
"""Tema I.8 (B1T08): La Administración General del Estado. Principios de organización y
funcionamiento. Órganos centrales. Órganos superiores y órganos directivos: creación,
nombramiento, cese y funciones. Los servicios comunes de los ministerios. Órganos
territoriales. La Administración del Estado en el Exterior.
Método del I.2: mapa → bloques (I a VI) con guía; cada artículo, texto literal del
BOE + ficha de casillas fijas; cierre 1 (preguntas oficiales) y cierre 2 (repaso).
Normas (textos consolidados del BOE): Ley 40/2015, arts. 3 y 54 a 80; Ley 50/1997, del
Gobierno, art. 15.1; Ley 2/2014, de la Acción y del Servicio Exterior del Estado
(arts. 1, 6, 41, 42, 44, 45, 47 y 48)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO["L2_2014"] = "Ley 2/2014"

T = Tema("B1T08",
  "Seis preguntas: I. Qué es la AGE y con qué principios se organiza (Ley 40/2015, arts. 3, 54 a 56) · II. Cómo se organizan los órganos centrales: los Ministerios (arts. 57 a 60) · III. Quiénes son los órganos superiores y directivos y cómo se crean, nombran, cesan y qué hacen (arts. 55, 55 bis y 61 a 67; Ley 50/1997, art. 15) · IV. Qué son los servicios comunes (art. 68) · V. Cómo se organiza la AGE en el territorio: Delegados y Subdelegados del Gobierno (arts. 69 a 79) · VI. Cómo actúa en el exterior (art. 80; Ley 2/2014). Cada artículo: texto literal del BOE y ficha.",
  ["Administración General del Estado", "Ley 40/2015", "Arts. 54-80", "Órganos superiores", "Órganos directivos", "Art. 55 bis", "Ministros", "Secretarios de Estado", "Subsecretarios", "Directores generales", "Servicios comunes", "Delegados del Gobierno", "Subdelegados del Gobierno", "Servicio Exterior", "Ley 2/2014", "Embajadores", "Oficinas Consulares"])

# =============================================================================
T.ap("s0", "Mapa del tema: seis preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque I, tema 8):
> 8. La Administración General del Estado. Principios de organización y funcionamiento. Órganos centrales. Órganos superiores y órganos directivos: creación, nombramiento, cese y funciones. Los servicios comunes de los ministerios. Órganos territoriales. La Administración del Estado en el Exterior.

### El hilo conductor

El epígrafe se lee como **seis preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Ley 40/2015 | Otras normas |
|---|---|---|---|
| **I** | ¿Qué es la AGE y con qué principios se organiza y funciona? | Arts. 3.1, 54, 55.1 y 2 y 56 | — |
| **II** | ¿Cómo se organizan los órganos centrales? (los Ministerios) | Arts. 57 a 60 | — |
| **III** | ¿Quiénes son los órganos superiores y directivos? Creación, nombramiento, cese y funciones | Arts. 55.3, 6, 9, 10 y 11, 55 bis y 61 a 67 | Ley 50/1997, art. 15.1 |
| **IV** | ¿Qué son los servicios comunes de los Ministerios? | Art. 68 (y 58.2, 63 y 65) | — |
| **V** | ¿Cómo se organiza la AGE en el territorio? (órganos territoriales) | Arts. 55.4 y 69 a 79 | — |
| **VI** | ¿Cómo se organiza la AGE en el exterior? | Arts. 55.5 y 80 | Ley 2/2014, arts. 1, 6, 41, 42, 44, 45, 47 y 48 |

!> **La idea que une los seis bloques:** la AGE se organiza según unos **principios** (I) en tres piezas: una **organización central** de Ministerios (II), dirigida por **órganos superiores** que planifican y **órganos directivos** que ejecutan (III), con unos **servicios comunes** que dan apoyo a todo el Ministerio (IV); una **organización territorial** integrada en las Delegaciones del Gobierno (V); y una **Administración en el exterior**, el Servicio Exterior del Estado (VI).

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- Fronteras con otros temas: el Gobierno, el Presidente, los Ministros como miembros del Gobierno y la Ley 50/1997 (tema I.6); el sector público institucional: organismos públicos, entidades y sociedades (tema I.9); la competencia, la delegación y la avocación de los órganos administrativos no se desarrollan aquí.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).

?> **Aviso sobre los nombres de los Ministerios.** La Ley 40/2015 y la Ley 2/2014 se citan **literalmente**, como están en el BOE, con los nombres de Ministerios de cuando se aprobaron («Ministerio de Hacienda y Administraciones Públicas», «Ministerio de Asuntos Exteriores y de Cooperación»). El número y la denominación de los Ministerios los fija un Real Decreto del Presidente del Gobierno (art. 57.3 → II.1.1), así que pueden no coincidir con los actuales.
""")

# =============================================================================
T.ap("bI", "I. ¿Qué es la AGE y con qué principios se organiza y funciona? (Ley 40/2015, arts. 3, 54 a 56)", donde(
  "Primera pregunta del tema. Antes de ver sus órganos, hay que saber **con qué principios** actúa y se organiza la Administración General del Estado (AGE) y **qué piezas** la forman.",
  ["1 Principios de organización y funcionamiento (arts. 3.1 y 54)", "2 Estructura de la AGE y elementos organizativos básicos (arts. 55.1 y 2 y 56)"]))

T.ap("s1", "I.1 Principios de organización y funcionamiento (arts. 3.1 y 54)", f"""
La Ley 40/2015 fija unos principios **comunes a todas las Administraciones** (art. 3) y añade **los propios de la AGE** (art. 54).

{unidad("1.1 Principios generales de todas las Administraciones Públicas (art. 3.1)",
  lit("L40", "Artículo 3", ["eficacia, jerarquía, descentralización, desconcentración y coordinación", "con sometimiento pleno a la Constitución, a la Ley y al Derecho"], solo=list(range(1, 14))),
  fichab("Principios con los que actúan todas las Administraciones Públicas, también la AGE",
         c("L40", "Artículo 3", "Las Administraciones Públicas"),
         [f"::{c('L40', 'Artículo 3', 'sirven con objetividad los intereses generales')} y actúan con:", "Eficacia, jerarquía, descentralización, desconcentración y coordinación", "Sometimiento pleno a la Constitución, a la Ley y al Derecho", "Y respetan en su actuación y relaciones los once principios de las letras a) a k)"],
         "—",
         "Los cinco principios de actuación del primer párrafo (eficacia, jerarquía, descentralización, desconcentración, coordinación) no son los mismos que los once de las letras a) a k) (servicio efectivo, simplicidad, participación, racionalización, buena fe, responsabilidad, planificación, eficacia en los objetivos, economía, eficiencia, cooperación)."))}

{unidad("1.2 Principios y competencias propios de la AGE (art. 54)",
  lit("L40", "Artículo 54", ["descentralización funcional y desconcentración funcional y territorial", "presencia equilibrada de mujeres y hombres", "corresponderán al Ministerio de Hacienda y Administraciones Públicas"]),
  fichab("Principios de organización de la AGE y Ministerio competente en organización administrativa",
         "La Administración General del Estado",
         ["Los principios del art. 3 (→ I.1.1)", "Además: descentralización funcional y desconcentración funcional y territorial", "Presencia equilibrada de mujeres y hombres en los nombramientos de órganos superiores y directivos y del personal de alta dirección del sector público institucional estatal (arts. 55 bis y 84 bis)", "Competencias residuales en organización, personal, procedimientos e inspección de servicios: al Ministerio de Hacienda y Administraciones Públicas"],
         "—",
         f"La descentralización que añade el art. 54 es la **funcional**; la desconcentración, **funcional y territorial**. La competencia residual en organización es del Ministerio de Hacienda y Administraciones Públicas solo si no está atribuida {c('L40', 'Artículo 54', 'a ningún otro órgano de la Administración General del Estado, ni al Gobierno')}."))}
""", 2)

T.ap("s2", "I.2 Estructura de la AGE y elementos organizativos básicos (arts. 55.1 y 2 y 56)", f"""
{unidad("2.1 Cómo se estructura la AGE (art. 55.1 y 2)",
  lit("L40", "Artículo 55", ["división funcional en Departamentos ministeriales", "gestión territorial integrada en Delegaciones del Gobierno en las Comunidades Autónomas", "La Organización Central, que integra los Ministerios y los servicios comunes"], solo=[1, 2, 3, 4, 5]),
  fichab("Las tres piezas de la AGE",
         "—",
         ["::Principios: división funcional en Departamentos ministeriales y gestión territorial integrada en Delegaciones del Gobierno. Comprende:", "Organización Central: Ministerios y servicios comunes (→ II y → IV.1)", "Organización Territorial (→ V.1)", "AGE en el exterior (→ VI.1)"],
         "—",
         "La Organización Central integra **los Ministerios y los servicios comunes**. La gestión territorial se integra en las **Delegaciones del Gobierno en las Comunidades Autónomas** (no en las provincias)."))}

{unidad("2.2 Las unidades administrativas (art. 56)",
  lit("L40", "Artículo 56", ["elementos organizativos básicos de las estructuras orgánicas", "mediante las relaciones de puestos de trabajo"]),
  fichab("Elemento organizativo básico: la unidad administrativa",
         "Los jefes de las unidades responden de su funcionamiento y de la ejecución de sus tareas",
         ["Comprenden puestos de trabajo o dotaciones de plantilla vinculados funcionalmente por sus cometidos y orgánicamente por una jefatura común", "Pueden existir unidades complejas que agrupen dos o más unidades menores", "Se integran en un determinado órgano"],
         "Se establecen mediante las **relaciones de puestos de trabajo**",
         "Las unidades administrativas **no** se crean por Real Decreto ni por Orden: se establecen por las **relaciones de puestos de trabajo** (lo mismo dice el art. 59.3 → II.2.1)."))}

{resumen([
  "Todas las AAPP: **eficacia, jerarquía, descentralización, desconcentración y coordinación** (3.1); la AGE añade **descentralización funcional** y **desconcentración funcional y territorial** (54.1).",
  "Presencia **equilibrada** de mujeres y hombres en los nombramientos (54.1, con los arts. 55 bis y 84 bis).",
  "La AGE comprende **Organización Central** (Ministerios y servicios comunes), **Organización Territorial** y **AGE en el exterior** (55.2).",
  "La **unidad administrativa** es el elemento organizativo básico y se establece por **RPT** (56)."],
  "Siguiente: II. ¿Cómo se organizan los órganos centrales? Los Ministerios")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Cómo se organizan los órganos centrales? Los Ministerios (Ley 40/2015, arts. 57 a 60)", donde(
  "Segunda pregunta. La Organización Central se articula en **Presidencia del Gobierno y Ministerios**. Aquí: cómo se determinan los Ministerios, qué órganos tienen dentro, cómo se crean esos órganos y cómo se ordenan jerárquicamente.",
  ["1 Los Ministerios y su organización interna (arts. 57 y 58)", "2 Creación, modificación y supresión de órganos y unidades (art. 59)", "3 Ordenación jerárquica de los órganos ministeriales (art. 60)"]))

T.ap("s3", "II.1 Los Ministerios y su organización interna (arts. 57 y 58)", f"""
{unidad("1.1 Los Ministerios (art. 57)",
  lit("L40", "Artículo 57", ["en Presidencia del Gobierno y en Ministerios", "con carácter excepcional se adscriban directamente al Ministro", "mediante Real Decreto del Presidente del Gobierno"]),
  fichab("Organización de la AGE en Ministerios (Departamentos ministeriales)",
         f"Número, denominación y competencias de los Ministerios y de las Secretarías de Estado: {c('L40', 'Artículo 57', 'Real Decreto del Presidente del Gobierno')}",
         ["Cada Ministerio comprende uno o varios sectores funcionalmente homogéneos de actividad administrativa", "Con carácter excepcional, órganos superiores o directivos u Organismos públicos pueden adscribirse directamente al Ministro"],
         "—",
         "El Real Decreto es **del Presidente del Gobierno** (no del Consejo de Ministros) y fija también las **Secretarías de Estado**. Compáralo con el art. 59.1 (→ II.2.1): Subsecretarías, Direcciones Generales, etc., se crean por Real Decreto **del Consejo de Ministros**."))}

{unidad("1.2 Organización interna de los Ministerios (art. 58)",
  lit("L40", "Artículo 58", ["pueden existir Secretarías de Estado, y Secretarías Generales", "contarán, en todo caso, con una Subsecretaría, y dependiendo de ella una Secretaría General Técnica", "órganos de gestión de una o varias áreas funcionalmente homogéneas", "se organizan en Subdirecciones Generales"]),
  fichab("Órganos que existen dentro de cada Ministerio",
         "—",
         ["Potestativos: Secretarías de Estado y Secretarías Generales, para la gestión de un sector de actividad", "Obligatorios: una Subsecretaría y, dependiendo de ella, una Secretaría General Técnica, para los servicios comunes", "Direcciones Generales: gestión de una o varias áreas funcionalmente homogéneas", "Subdirecciones Generales: en que se organizan las Direcciones Generales (o adscritas directamente a órganos de mayor nivel)"],
         "—",
         "Lo único que existe **en todo caso** es la **Subsecretaría** con su **Secretaría General Técnica**. Las Secretarías de Estado y las Secretarías Generales «pueden existir»."))}
""", 2)

T.ap("s4", "II.2 Creación, modificación y supresión de órganos y unidades (art. 59)", f"""
{unidad("2.1 Qué norma crea cada órgano (art. 59)",
  lit("L40", "Artículo 59", ["por Real Decreto del Consejo de Ministros, a iniciativa del Ministro interesado y a propuesta del Ministro de Hacienda y Administraciones Públicas", "por orden del Ministro respectivo, previa autorización del Ministro de Hacienda y Administraciones Públicas", "a través de las relaciones de puestos de trabajo"]),
  fichab("Instrumento para crear, modificar y suprimir órganos y unidades",
         "Consejo de Ministros; Ministro respectivo; o relaciones de puestos de trabajo, según el nivel",
         ["Subsecretarías, Secretarías Generales, Secretarías Generales Técnicas, Direcciones Generales, Subdirecciones Generales y similares: Real Decreto del Consejo de Ministros (iniciativa del Ministro interesado; propuesta del Ministro de Hacienda y Administraciones Públicas)", "Órganos de nivel inferior a Subdirección General: orden del Ministro respectivo, previa autorización del Ministro de Hacienda y Administraciones Públicas", "Unidades que no son órganos: relaciones de puestos de trabajo"],
         "—",
         "En el Real Decreto del art. 59.1, la **iniciativa** es del Ministro interesado y la **propuesta**, del Ministro de Hacienda y Administraciones Públicas (no al revés). La **Subdirección General** se crea por **Real Decreto**; lo inferior, por **orden**."))}
""", 2)

T.ap("s5", "II.3 Ordenación jerárquica de los órganos ministeriales (art. 60)", f"""
{unidad("3.1 Quién depende de quién (art. 60)",
  lit("L40", "Artículo 60", ["jefes superiores del Departamento y superiores jerárquicos directos de los Secretarios de Estado y Subsecretarios", "Subsecretario, Director general y Subdirector general", "Los Secretarios generales tienen categoría de Subsecretario y los Secretarios Generales Técnicos tienen categoría de Director general"]),
  fichab("Orden jerárquico dentro del Ministerio",
         "Ministro → Secretarios de Estado y Subsecretarios → Directores generales → Subdirectores generales",
         ["Los Ministros son superiores jerárquicos directos de Secretarios de Estado y Subsecretarios", "Los órganos directivos se ordenan: Subsecretario, Director general y Subdirector general", "Categorías asimiladas: Secretario general = Subsecretario; Secretario General Técnico = Director general"],
         "—",
         "**Secretario general** tiene categoría de **Subsecretario**; **Secretario General Técnico**, de **Director general**. Es la equivalencia que más se confunde."))}

*Esquema de elaboración propia: resume los arts. 55.3, 57.3, 58, 59 y 60 de la Ley 40/2015; no es texto legal.*

| Órgano | Clase (55.3) | Categoría (60) | ¿Existe siempre? (58) | Se crea por (57.3 y 59) |
|---|---|---|---|---|
| Ministro | Superior | Jefe superior del Departamento | Sí | Real Decreto del Presidente del Gobierno (Ministerios) |
| Secretario de Estado | Superior | Depende del Ministro | No («pueden existir») | Real Decreto del Presidente del Gobierno |
| Subsecretario | Directivo | Subsecretario | **Sí** | Real Decreto del Consejo de Ministros |
| Secretario general | Directivo | Categoría de Subsecretario | No («pueden existir») | Real Decreto del Consejo de Ministros |
| Secretario general técnico | Directivo | Categoría de Director general | **Sí** (depende de la Subsecretaría) | Real Decreto del Consejo de Ministros |
| Director general | Directivo | Director general | — | Real Decreto del Consejo de Ministros |
| Subdirector general | Directivo | Subdirector general | — | Real Decreto del Consejo de Ministros |
| Órganos inferiores | — | — | — | Orden del Ministro |

{resumen([
  "La AGE se organiza en **Presidencia del Gobierno y Ministerios**; su número, denominación y competencias (y las de las Secretarías de Estado), por **Real Decreto del Presidente del Gobierno** (57).",
  "En todo Ministerio: **Subsecretaría** y **Secretaría General Técnica**; potestativas: Secretarías de Estado y Secretarías Generales (58).",
  "Órganos hasta Subdirección General: **Real Decreto del Consejo de Ministros**; inferiores: **orden del Ministro**; unidades: **RPT** (59).",
  "Secretario general = categoría de **Subsecretario**; Secretario General Técnico = categoría de **Director general** (60)."],
  "Siguiente: III. ¿Quiénes son los órganos superiores y directivos? Creación, nombramiento, cese y funciones")}
""", 2)

# =============================================================================
T.ap("bIII", "III. Órganos superiores y directivos: creación, nombramiento, cese y funciones (Ley 40/2015, arts. 55, 55 bis y 61 a 67)", donde(
  "Tercera pregunta, el centro del epígrafe. Los **órganos superiores** planifican; los **órganos directivos** desarrollan y ejecutan. Para cada uno: quién lo nombra y separa, entre quiénes y qué funciones tiene.",
  ["1 Clases, alto cargo y régimen común (art. 55.3, 6, 7, 9, 10 y 11; art. 55 bis)", "2 Los Ministros (art. 61)", "3 Los Secretarios de Estado (art. 62; Ley 50/1997, art. 15.1)", "4 Subsecretarios y Secretarios generales (arts. 63 y 64)", "5 Secretarios generales técnicos, Directores generales y Subdirectores generales (arts. 65 a 67)", "6 Cuadro: nombramiento, cese y requisitos"]))

T.ap("s6", "III.1 Clases de órganos, alto cargo y régimen común (art. 55.3, 6, 7, 9, 10 y 11; art. 55 bis)", f"""
{unidad("1.1 Órganos superiores y órganos directivos de la organización central (art. 55.3)",
  lit("L40", "Artículo 55", ["Órganos superiores", "Órganos directivos"], solo=list(range(6, 14))),
  fichab("Clasificación de los órganos de la organización central",
         "—",
         ["Superiores: Ministros y Secretarios de Estado", "Directivos: Subsecretarios y Secretarios generales; Secretarios generales técnicos y Directores generales; Subdirectores generales"],
         "—",
         "Solo **dos** órganos superiores: **Ministros y Secretarios de Estado**. El Subsecretario y el Secretario general son ya órganos **directivos**. Cayó en 2025 (→ Cierre 1)."))}

{unidad("1.2 Alto cargo, dependencia y funciones de unos y otros (art. 55.6, 7 y 9)",
  lit("L40", "Artículo 55", ["excepto los Subdirectores generales y asimilados", "establecer los planes de actuación", "su desarrollo y ejecución"], solo=[16, 17, 19]),
  fichab("Condición de alto cargo y reparto de funciones",
         "Órganos superiores y directivos",
         ["Son altos cargos, salvo Subdirectores generales y asimilados (Ley 3/2015)", "Todos los demás órganos dependen de un órgano superior o directivo", "Superiores: establecen los planes de actuación", "Directivos: su desarrollo y ejecución"],
         "—",
         "Los **Subdirectores generales** son órganos directivos pero **no** altos cargos. Superiores **planifican**; directivos **desarrollan y ejecutan**."))}

{unidad("1.3 Nombramiento y régimen del desempeño (art. 55.10 y 11)",
  lit("L40", "Artículo 55", ["Ley 50/1997, de 27 de noviembre, del Gobierno", "atendiendo a criterios de competencia profesional y experiencia", "La responsabilidad profesional, personal y directa por la gestión desarrollada"], solo=[20, 21, 22, 23]),
  fichab("Reglas comunes de nombramiento y de desempeño",
         "Ministros y Secretarios de Estado: según la Ley 50/1997 y la Ley 3/2015; demás titulares: en la forma de la Ley 40/2015",
         ["Criterios: competencia profesional y experiencia", "Responsabilidad profesional, personal y directa por la gestión", "Sujeción al control y evaluación de la gestión por el órgano superior o directivo competente (sin perjuicio del control de la Ley General Presupuestaria)"],
         "—",
         "El nombramiento de Ministros (tema I.6) y Secretarios de Estado (→ III.3.2) se rige por la **Ley 50/1997** y la **Ley 3/2015**, no por la Ley 40/2015."))}

{unidad("1.4 Presencia equilibrada de mujeres y hombres (art. 55 bis)",
  lit("L40", "Artículo 55 bis", ["no superen el sesenta por ciento ni sean menos del cuarenta por ciento en el ámbito de cada departamento ministerial"]),
  fichab("Regla de representación equilibrada en los nombramientos",
         "Titulares de las **Secretarías de Estado** y de los **órganos directivos** de la AGE",
         "Cada sexo: no más del sesenta por ciento ni menos del cuarenta por ciento",
         f"60 % / 40 %, {c('L40', 'Artículo 55 bis', 'en el ámbito de cada departamento ministerial')}",
         "El porcentaje se mide **en cada departamento ministerial** (no en el conjunto de la AGE) y es **60/40** (no 70/30). Se aplica igual a Secretarías de Estado y a órganos directivos. Cayó en 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s7", "III.2 Los Ministros (art. 61)", f"""
Los Ministros son miembros del Gobierno: su nombramiento y cese por el Rey, a propuesta del Presidente, se estudian en el tema I.6 (Ley 50/1997, art. 12.2). Aquí, sus funciones como **jefes de su Departamento**.

{unidad("2.1 Funciones de los Ministros (art. 61)",
  lit("L40", "Artículo 61", ["dirigen los sectores de actividad administrativa integrados en su Ministerio", "Ejercer la potestad reglamentaria en las materias propias de su Departamento", "Nombrar y separar a los titulares de los órganos directivos del Ministerio", "Mantener las relaciones con las Comunidades Autónomas y convocar las Conferencias sectoriales", "Imponer la sanción de separación del servicio por faltas muy graves"]),
  fichab("Funciones del Ministro como titular del Departamento",
         "El Ministro",
         ["::Entre otras:", "Potestad reglamentaria en las materias de su Departamento (a)", "Fijar objetivos, aprobar planes y asignar recursos (b)", "Determinar y, en su caso, proponer la organización interna del Ministerio (d)", "Nombrar y separar a los titulares de órganos directivos, salvo que corresponda al Consejo de Ministros, a otro órgano o al organismo (f)", "Relaciones con las CC. AA. y convocar las Conferencias sectoriales (h)", "Revisar de oficio, resolver conflictos de atribuciones (j); resolver recursos y declarar la lesividad cuando les corresponda (ñ)", "Imponer la separación del servicio por faltas muy graves (s)"],
         "—",
         "La **separación del servicio** la impone el **Ministro**; el Subsecretario ejerce la potestad disciplinaria por faltas graves o muy graves **salvo** la separación (→ III.4.1). Las **Conferencias sectoriales** las convoca el **Ministro**."))}
""", 2)

T.ap("s8", "III.3 Los Secretarios de Estado (art. 62; Ley 50/1997, art. 15.1)", f"""
{unidad("3.1 Funciones de los Secretarios de Estado (art. 62)",
  lit("L40", "Artículo 62", ["directamente responsables de la ejecución de la acción del Gobierno en un sector de actividad específica", "por delegación expresa de sus respectivos Ministros", "Nombrar y separar a los Subdirectores Generales de la Secretaría de Estado"]),
  fichab("Órgano superior responsable de un sector de actividad",
         "El Secretario de Estado; responde ante el Ministro",
         ["Ejecuta la acción del Gobierno en un sector de actividad específica", "Por delegación expresa del Ministro, puede representarlo en materias de su competencia, incluso con proyección internacional", "Dirige y coordina las Secretarías y Direcciones Generales bajo su dependencia", "Nombra y separa a los Subdirectores Generales de la Secretaría de Estado (c)", "Resuelve los recursos contra resoluciones de órganos directivos que dependan directamente de él y no agoten la vía administrativa (i)"],
         "—",
         "Representa al Ministro solo **por delegación expresa**. Nombra a los **Subdirectores Generales** de su Secretaría de Estado (no a los Directores generales)."))}

{unidad("3.2 Nombramiento y separación (Ley 50/1997, art. 15.1)",
  lit("LGOB", "a15", ["por Real Decreto del Consejo de Ministros, aprobado a propuesta del Presidente del Gobierno o del miembro del Gobierno a cuyo Departamento pertenezcan"], solo=[1]),
  fichab("Nombramiento y cese de los Secretarios de Estado",
         "El Consejo de Ministros, a propuesta del Presidente del Gobierno o del miembro del Gobierno del Departamento",
         "Real Decreto del Consejo de Ministros",
         "—",
         "Es órgano superior, pero **no** lo nombra el Rey (como a los Ministros) sino el **Consejo de Ministros** por Real Decreto. Ver también la regla 60/40 del art. 55 bis (→ III.1.4)."))}
""", 2)

T.ap("s9", "III.4 Subsecretarios y Secretarios generales (arts. 63 y 64)", f"""
{unidad("4.1 Los Subsecretarios (art. 63)",
  lit("L40", "Artículo 63", ["ostentan la representación ordinaria del Ministerio, dirigen los servicios comunes", "Desempeñar la jefatura superior de todo el personal del Departamento", "Convocar y resolver pruebas selectivas de personal funcionario y laboral", "salvo la separación del servicio", "serán nombrados y separados por Real Decreto del Consejo de Ministros a propuesta del titular del Ministerio", "pertenecientes al Subgrupo A1"]),
  fichab("Órgano directivo que dirige los servicios comunes del Ministerio",
         "El Subsecretario; nombramiento y separación: Real Decreto del Consejo de Ministros a propuesta del titular del Ministerio",
         ["Representación ordinaria del Ministerio y dirección de los servicios comunes", "Jefatura superior de todo el personal del Departamento (f)", "Asesoramiento jurídico al Ministro (g)", "Dirección, impulso y supervisión de la Secretaría General Técnica (h)", "Nombrar y cesar a los Subdirectores y asimilados de la Subsecretaría, al personal de libre designación y al eventual (l)", "Convocar y resolver pruebas selectivas y concursos (m y n)", "Potestad disciplinaria por faltas graves o muy graves, salvo la separación del servicio (ñ)"],
         "Nombramiento: entre funcionarios de carrera del Estado, de las CC. AA. o de las Entidades locales del Subgrupo A1 (o jubilados que hubieran tenido esa condición) y con los requisitos de idoneidad de la Ley 3/2015",
         "Representación **ordinaria** (no «superior») del Ministerio; jefatura **superior** de todo el personal. Tiene que ser **funcionario A1** (a diferencia del Secretario general)."))}

{unidad("4.2 Los Secretarios generales (art. 64)",
  lit("L40", "Artículo 64", ["deberán determinar las competencias que le correspondan sobre un sector de actividad administrativa determinado", "con categoría de Subsecretario", "a propuesta del titular del Ministerio o del Presidente del Gobierno", "entre personas con cualificación y experiencia en el desempeño de puestos de responsabilidad en la gestión pública o privada"]),
  fichab("Órgano directivo, potestativo, para un sector de actividad",
         "El Secretario general (categoría de Subsecretario); nombramiento y separación: Real Decreto del Consejo de Ministros a propuesta del titular del Ministerio o del Presidente del Gobierno",
         ["Su existencia la prevén las normas de estructura del Ministerio, que deben fijar sus competencias", "Ejerce las competencias de dirección del art. 62.2 b) y las que le asigne el Real Decreto de estructura"],
         "Nombramiento: entre personas con cualificación y experiencia en puestos de responsabilidad en la gestión pública **o privada**; requisitos de idoneidad de la Ley 3/2015",
         "Al Secretario general **no** se le exige ser funcionario. Lo propone el titular del Ministerio **o el Presidente del Gobierno**."))}
""", 2)

T.ap("s10", "III.5 Secretarios generales técnicos, Directores generales y Subdirectores generales (arts. 65 a 67)", f"""
{unidad("5.1 Los Secretarios generales técnicos (art. 65)",
  lit("L40", "Artículo 65", ["bajo la inmediata dependencia del Subsecretario", "producción normativa, asistencia jurídica y publicaciones", "la categoría de Director General", "a propuesta del titular del Ministerio"]),
  fichab("Órgano directivo de servicios comunes, dependiente del Subsecretario",
         "El Secretario general técnico (categoría de Director General); nombramiento y separación: Real Decreto del Consejo de Ministros a propuesta del titular del Ministerio",
         ["Competencias sobre servicios comunes que le atribuya el Real Decreto de estructura", "En todo caso: producción normativa, asistencia jurídica y publicaciones"],
         "Nombramiento: entre funcionarios de carrera del Estado, de las CC. AA. o de las Entidades locales del Subgrupo A1; requisitos de idoneidad de la Ley 3/2015",
         "En todo caso: **producción normativa, asistencia jurídica y publicaciones**. Depende **inmediatamente del Subsecretario**."))}

{unidad("5.2 Los Directores generales (art. 66)",
  lit("L40", "Artículo 66", ["gestión de una o varias áreas funcionalmente homogéneas del Ministerio", "a propuesta del titular del Departamento o del Presidente del Gobierno", "salvo que el Real Decreto de estructura permita", "memoria razonada"]),
  fichab("Órgano directivo de gestión de una o varias áreas funcionalmente homogéneas",
         "El Director general; nombramiento y separación: Real Decreto del Consejo de Ministros a propuesta del titular del Departamento o del Presidente del Gobierno",
         ["Propone los proyectos de la Dirección general, dirige su ejecución y controla su cumplimiento", "Ejerce las competencias atribuidas, desconcentradas o delegadas", "Impulsa y supervisa la gestión ordinaria y vela por el buen funcionamiento de órganos, unidades y personal"],
         "Nombramiento: entre funcionarios de carrera A1 (o jubilados que hubieran tenido esa condición), salvo que el Real Decreto de estructura lo permita por las características de las funciones, motivándolo en memoria razonada; requisitos de idoneidad de la Ley 3/2015",
         "Regla: **funcionario A1**. Excepción: que el **Real Decreto de estructura** lo permita, con **memoria razonada**."))}

{unidad("5.3 Los Subdirectores generales (art. 67)",
  lit("L40", "Artículo 67", ["respetando los principios de igualdad, mérito y capacidad", "por el Ministro, Secretario de Estado o Subsecretario del que dependan"]),
  fichab("Responsables inmediatos de la ejecución de proyectos, objetivos o actividades",
         "El Subdirector general; nombramiento y cese: el Ministro, Secretario de Estado o Subsecretario del que dependan",
         "Bajo la supervisión del Director general o del titular del órgano del que dependan; también gestión ordinaria de la Subdirección General",
         "Nombramiento respetando igualdad, mérito y capacidad, entre funcionarios de carrera del Estado (o de otras Administraciones si lo prevén las normas) del Subgrupo A1",
         "No los nombra el Consejo de Ministros sino el **Ministro, Secretario de Estado o Subsecretario** del que dependan. Son los únicos de esta lista con **igualdad, mérito y capacidad** y **no son altos cargos** (→ III.1.2)."))}
""", 2)

T.ap("s11", "III.6 Cuadro: nombramiento, cese y requisitos (esquema)", f"""
*Esquema de elaboración propia: resume los arts. 55.10, 63 a 67 de la Ley 40/2015 y 15.1 de la Ley 50/1997; no es texto legal.*

| Órgano | Nombra y separa | A propuesta de | Requisito de acceso |
|---|---|---|---|
| Secretario de Estado | Consejo de Ministros (Real Decreto) | Presidente del Gobierno o miembro del Gobierno del Departamento | — (Ley 3/2015) |
| Subsecretario | Consejo de Ministros (Real Decreto) | Titular del Ministerio | Funcionario de carrera A1 (o jubilado) |
| Secretario general | Consejo de Ministros (Real Decreto) | Titular del Ministerio **o** Presidente del Gobierno | Cualificación y experiencia en gestión pública **o privada** |
| Secretario general técnico | Consejo de Ministros (Real Decreto) | Titular del Ministerio | Funcionario de carrera A1 |
| Director general | Consejo de Ministros (Real Decreto) | Titular del Departamento **o** Presidente del Gobierno | Funcionario de carrera A1 (o jubilado), salvo excepción motivada |
| Subdirector general | Ministro, Secretario de Estado o Subsecretario del que dependa | — | Funcionario de carrera A1; igualdad, mérito y capacidad |

{resumen([
  "Órganos **superiores**: Ministros y Secretarios de Estado; **directivos**: Subsecretarios, Secretarios generales, Secretarios generales técnicos, Directores generales y Subdirectores generales (55.3).",
  "Todos son **altos cargos** salvo los **Subdirectores generales** y asimilados (55.6).",
  "Secretarías de Estado y órganos directivos: cada sexo entre el **40 y el 60 %** en **cada departamento ministerial** (55 bis).",
  "Subsecretario, Secretario general técnico y Director general: **funcionarios A1**; Secretario general: gestión pública **o privada** (63 a 66)."],
  "Siguiente: IV. ¿Qué son los servicios comunes de los Ministerios?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Qué son los servicios comunes de los Ministerios? (Ley 40/2015, art. 68)", donde(
  "Cuarta pregunta. Junto a los órganos que gestionan cada sector de actividad, todo Ministerio tiene **servicios comunes** que dan apoyo a todo el Departamento. Los dirige el **Subsecretario** (→ III.4.1) con la **Secretaría General Técnica** (→ III.5.1).",
  ["1 Los servicios comunes: funciones, dependencia y gestión compartida (art. 68)"]))

T.ap("s12", "IV.1 Los servicios comunes de los Ministerios (art. 68)", f"""
{unidad("1.1 Reglas generales de los servicios comunes (art. 68)",
  lit("L40", "Artículo 68", ["prestan a los órganos superiores y directivos del resto del Ministerio la asistencia precisa", "el asesoramiento, el apoyo técnico y, en su caso, la gestión directa", "de acuerdo con las disposiciones y directrices adoptadas por los Ministerios con competencia sobre dichas funciones comunes", "Mediante Real Decreto podrá preverse la gestión compartida"]),
  fichab("Asistencia a los órganos del Ministerio en las funciones comunes",
         "Los órganos directivos encargados de los servicios comunes: la Subsecretaría, que los dirige (art. 63.1), y la Secretaría General Técnica que depende de ella (arts. 58.2 y 65.1)",
         ["::Asesoramiento, apoyo técnico y, en su caso, gestión directa en:", "Planificación, programación y presupuestación; cooperación internacional; acción en el exterior", "Organización y recursos humanos; sistemas de información y comunicación", "Producción normativa; asistencia jurídica; gestión financiera", "Gestión de medios materiales y servicios auxiliares; seguimiento, control e inspección de servicios", "Estadística para fines estatales; publicaciones"],
         "Gestión compartida, por Real Decreto: coordinada por el Ministerio de Hacienda y Administraciones Públicas (o un organismo autónomo suyo) para varios Ministerios, o por la Subsecretaría de cada Ministerio (o un organismo autónomo suyo) para todo el Ministerio",
         "Los servicios comunes funcionan según las directrices de los **Ministerios con competencia sobre esas funciones comunes**. La gestión compartida se prevé **mediante Real Decreto** y puede ser **interministerial** (Hacienda) o **intraministerial** (Subsecretaría)."))}

!> **Cómo encaja con lo anterior:** cada Ministerio tiene **en todo caso** una **Subsecretaría** y, dependiendo de ella, una **Secretaría General Técnica**, «para la gestión de los servicios comunes» (art. 58.2 → II.1.2). El Subsecretario **dirige** los servicios comunes (art. 63.1); el Secretario general técnico tiene las competencias sobre servicios comunes que le atribuya el Real Decreto de estructura y, en todo caso, **producción normativa, asistencia jurídica y publicaciones** (art. 65.1). Las Delegaciones del Gobierno tienen su propio órgano de servicios comunes: la **Secretaría General** (art. 76.1 → V.4.1).

{resumen([
  "Servicios comunes: **asesoramiento, apoyo técnico y, en su caso, gestión directa** de funciones transversales del Ministerio (68.1).",
  "Los dirige el **Subsecretario**; la **Secretaría General Técnica** depende de él (58.2, 63.1 y 65.1).",
  "Gestión compartida **por Real Decreto**: por el Ministerio de Hacienda y Administraciones Públicas o por la Subsecretaría de cada Ministerio (68.3)."],
  "Siguiente: V. ¿Cómo se organiza la AGE en el territorio? Los órganos territoriales")}
""", 2)

# =============================================================================
T.ap("bV", "V. ¿Cómo se organiza la AGE en el territorio? Órganos territoriales (Ley 40/2015, arts. 55.4 y 69 a 79)", donde(
  "Quinta pregunta. La AGE se organiza en el territorio según el principio de **gestión territorial integrada en Delegaciones del Gobierno** (art. 55.1 → I.2.1). Aquí: Delegaciones y Subdelegaciones, Directores Insulares, servicios territoriales, competencias de Delegados y Subdelegados y órganos de apoyo.",
  ["1 Delegaciones, Subdelegaciones, Directores Insulares y servicios territoriales (arts. 55.4 y 69 a 71)", "2 Los Delegados del Gobierno (arts. 72 y 73)", "3 Los Subdelegados del Gobierno (arts. 74 y 75)", "4 Estructura, asistencia jurídica, control y órganos colegiados (arts. 76 a 79)", "5 Cuadro de los órganos territoriales"]))

T.ap("s13", "V.1 Delegaciones, Subdelegaciones, Directores Insulares y servicios territoriales (arts. 55.4 y 69 a 71)", f"""
{unidad("1.1 Rango de Delegados y Subdelegados (art. 55.4)",
  lit("L40", "Artículo 55", ["que tendrán rango de Subsecretario", "los cuales tendrán nivel de Subdirector general"], solo=[14]),
  fichab("Órganos directivos de la organización territorial",
         "Delegados del Gobierno en las CC. AA. y Subdelegados del Gobierno en las provincias",
         "Son órganos **directivos**",
         "—",
         "Delegado: **rango de Subsecretario**; Subdelegado: **nivel de Subdirector general**. Ninguno es órgano superior. Cayó en 2025 (→ Cierre 1)."))}

{unidad("1.2 Las Delegaciones y las Subdelegaciones del Gobierno (art. 69)",
  lit("L40", "Artículo 69", ["en cada una de las Comunidades Autónomas", "donde radique el Consejo de Gobierno de la Comunidad Autónoma", "adscritas orgánicamente al Ministerio de Hacienda y Administraciones Públicas", "Comunidades Autónomas pluriprovinciales", "Comunidades Autónomas uniprovinciales"]),
  fichab("Delegaciones (por Comunidad Autónoma) y Subdelegaciones (por provincia)",
         "Una Delegación del Gobierno en cada Comunidad Autónoma; un Subdelegado en cada provincia de las CC. AA. pluriprovinciales",
         ["Sede de la Delegación: donde radique el Consejo de Gobierno de la Comunidad Autónoma, salvo acuerdo del Consejo de Ministros y sin perjuicio del Estatuto de Autonomía", "Las Delegaciones están adscritas orgánicamente al Ministerio de Hacienda y Administraciones Públicas", "En las CC. AA. uniprovinciales pueden crearse Subdelegaciones por Real Decreto (población, volumen de gestión, singularidades)"],
         "—",
         "Sede: donde esté el **Consejo de Gobierno** autonómico (no el Parlamento). En las uniprovinciales la Subdelegación es **potestativa** («Podrán crearse por Real Decreto»)."))}

{unidad("1.3 Los Directores Insulares (art. 70)",
  lit("L40", "Artículo 70", ["Reglamentariamente se determinarán las islas", "nombrados por el Delegado del Gobierno mediante el procedimiento de libre designación"]),
  fichab("Órgano de la AGE en determinadas islas",
         "El Director Insular; lo nombra el Delegado del Gobierno",
         ["Islas: las que se determinen reglamentariamente; nivel: el de la relación de puestos de trabajo", "Dependen jerárquicamente del Delegado del Gobierno o, si existe, del Subdelegado", "Ejercen en su isla las competencias de los Subdelegados del Gobierno"],
         "Libre designación entre funcionarios de carrera del Estado, de las CC. AA. o de las Entidades Locales del Subgrupo A1",
         "Lo nombra el **Delegado** del Gobierno, por **libre designación**. Ejerce las competencias de un **Subdelegado** en su ámbito."))}

{unidad("1.4 Los servicios territoriales (art. 71)",
  lit("L40", "Artículo 71", ["servicios integrados y no integrados", "dependerán del órgano central competente sobre el sector de actividad", "dependerán del Delegado del Gobierno, o en su caso Subdelegado del Gobierno, a través de la Secretaría General"]),
  fichab("Servicios de la AGE en la Comunidad Autónoma",
         "—",
         ["No integrados: dependen del órgano central competente del sector, que fija objetivos y controla su ejecución; se organizan por Real Decreto a propuesta conjunta (unidades de nivel de Subdirección General o equivalentes) o por Orden conjunta (órganos inferiores)", "Integrados: dependen del Delegado (o Subdelegado) a través de la Secretaría General, con las instrucciones técnicas del Ministerio competente"],
         "—",
         "**Integrados** → Delegado, **a través de la Secretaría General**; **no integrados** → órgano **central** competente."))}
""", 2)

T.ap("s14", "V.2 Los Delegados del Gobierno en las Comunidades Autónomas (arts. 72 y 73)", f"""
{unidad("2.1 Naturaleza, dependencia, nombramiento y suplencia (art. 72)",
  lit("L40", "Artículo 72", ["representan al Gobierno de la Nación en el territorio de la respectiva Comunidad Autónoma", "sin perjuicio de la representación ordinaria del Estado en las mismas a través de sus respectivos Presidentes", "órganos directivos con rango de Subsecretario que dependen orgánicamente del Presidente del Gobierno y funcionalmente del Ministerio competente por razón de la materia", "nombrados y separados por Real Decreto del Consejo de Ministros, a propuesta del Presidente del Gobierno", "será suplido por el Subdelegado del Gobierno que el Delegado designe"]),
  fichab("Representante del Gobierno de la Nación en la Comunidad Autónoma",
         "El Delegado del Gobierno; nombramiento y separación: Real Decreto del Consejo de Ministros a propuesta del Presidente del Gobierno",
         ["Representa al Gobierno de la Nación en la Comunidad Autónoma (la representación ordinaria del Estado es del Presidente autonómico)", "Dirige y supervisa la AGE en el territorio y la coordina con la administración autonómica y la local", "Órgano directivo con rango de Subsecretario; dependencia orgánica del Presidente del Gobierno y funcional del Ministerio competente por razón de la materia"],
         "Nombramiento según competencia profesional y experiencia, con los requisitos de idoneidad de la Ley 3/2015. Suplencia: el Subdelegado que designe el Delegado; en su defecto, el de la provincia de la sede; en uniprovinciales sin Subdelegado, el Secretario General",
         "Representa al **Gobierno**; la representación **ordinaria del Estado** en la Comunidad es de su **Presidente**. Ojo: la **Delegación** está adscrita orgánicamente al **Ministerio de Hacienda y Administraciones Públicas** (69.3), pero el **Delegado** depende orgánicamente del **Presidente del Gobierno** (72.3). Cayó en 2025 (→ Cierre 1)."))}

{unidad("2.2 Competencias de los Delegados del Gobierno (art. 73)",
  lit("L40", "Artículo 73", ["Nombrar a los Subdelegados del Gobierno en las provincias de su ámbito de actuación", "Informar, con carácter preceptivo", "con carácter anual", "Resolver los recursos en vía administrativa interpuestos contra las resoluciones y actos dictados por los órganos de la Delegación", "potestad sancionadora, expropiatoria", "cuya jefatura corresponderá al Delegado del Gobierno"]),
  fichab("Las cinco áreas de competencia del Delegado del Gobierno",
         "El Delegado del Gobierno, titular de la Delegación",
         ["a) Dirección y coordinación de la AGE y sus Organismos públicos: nombra a los Subdelegados y, en su caso, a los Directores Insulares; informa preceptivamente los nombramientos de titulares de órganos territoriales", "b) Información de la acción del Gobierno y a los ciudadanos: informe anual al Gobierno sobre los servicios públicos estatales", "c) Coordinación y colaboración con otras AAPP: convenios; Comisiones mixtas de transferencias y bilaterales de cooperación", "d) Control de legalidad: resuelve recursos contra actos de los órganos de la Delegación (previo informe del Ministerio competente); suspende o propone suspender; conflictos y recursos", "e) Políticas públicas: propuestas sobre objetivos, duplicidades, recursos humanos y edificios", "Además: potestad sancionadora, expropiatoria y las desconcentradas o delegadas (73.2); seguridad ciudadana, con la jefatura de las Fuerzas y Cuerpos de Seguridad del Estado, bajo la dependencia funcional del Ministerio del Interior (73.3)"],
         "Informe sobre el funcionamiento de los servicios públicos estatales: **anual**, al Gobierno, a través del titular del Ministerio de Hacienda y Administraciones Públicas",
         "Las impugnaciones de actos **del propio Delegado** que no agoten la vía administrativa las resuelve el **Ministerio competente**; la **responsabilidad patrimonial** la resuelve el **titular del Departamento** competente, no el Delegado."))}
""", 2)

T.ap("s15", "V.3 Los Subdelegados del Gobierno en las provincias (arts. 74 y 75)", f"""
{unidad("3.1 Subdelegado del Gobierno: nivel y nombramiento (art. 74)",
  lit("L40", "Artículo 74", ["bajo la inmediata dependencia del Delegado del Gobierno", "con nivel de Subdirector General", "mediante el procedimiento de libre designación", "el Delegado del Gobierno asumirá las competencias"]),
  fichab("Órgano de la AGE en cada provincia",
         "El Subdelegado del Gobierno; lo nombra el Delegado del Gobierno",
         "Bajo la inmediata dependencia del Delegado; en las CC. AA. uniprovinciales sin Subdelegado, el Delegado asume sus competencias",
         "Libre designación entre funcionarios de carrera del Estado, de las CC. AA. o de las Entidades Locales del Subgrupo A1",
         "Lo nombra el **Delegado** (no el Consejo de Ministros), por **libre designación**, entre **funcionarios A1**. Nivel de **Subdirector General**."))}

{unidad("3.2 Competencias de los Subdelegados (art. 75)",
  lit("L40", "Artículo 75", ["dirigirá las Fuerzas y Cuerpos de Seguridad del Estado en la provincia", "Dirigir y coordinar la protección civil en el ámbito de la provincia", "e impulsar, supervisar e inspeccionar los servicios no integrados"]),
  fichab("Funciones del Subdelegado en la provincia",
         "El Subdelegado del Gobierno",
         ["Comunicación, colaboración y cooperación con la Comunidad Autónoma y las Entidades Locales", "Protección del libre ejercicio de derechos y libertades y seguridad ciudadana: dirige las Fuerzas y Cuerpos de Seguridad del Estado en la provincia", "Dirige y coordina la protección civil en la provincia", "Dirige los servicios integrados e impulsa, supervisa e inspecciona los no integrados", "Coordina la utilización de los medios materiales y edificios", "Potestad sancionadora y las desconcentradas o delegadas"],
         "—",
         "La **protección civil** en la provincia la dirige y coordina el **Subdelegado**. En seguridad ciudadana, el Delegado tiene la **jefatura** de las Fuerzas y Cuerpos (73.3) y el Subdelegado las **dirige en la provincia** (75 b)."))}
""", 2)

T.ap("s16", "V.4 Estructura, asistencia jurídica, control y órganos colegiados (arts. 76 a 79)", f"""
{unidad("4.1 Estructura de Delegaciones y Subdelegaciones (art. 76)",
  lit("L40", "Artículo 76", ["por Real Decreto del Consejo de Ministros a propuesta del Ministerio de Hacienda y Administraciones Públicas", "una Secretaría General", "como órgano de gestión de los servicios comunes"]),
  fichab("Estructura de las Delegaciones y Subdelegaciones; integración de servicios",
         "Consejo de Ministros, a propuesta del Ministerio de Hacienda y Administraciones Públicas (y, para integrar o desintegrar servicios, también del Ministerio competente del área)",
         ["Real Decreto de estructura", "En todo caso, una Secretaría General, órgano de gestión de los servicios comunes, de la que dependen los servicios integrados"],
         "—",
         "La **Secretaría General** existe **en todo caso** y gestiona los **servicios comunes** de la Delegación o Subdelegación."))}

{unidad("4.2 Asistencia jurídica y control económico-financiero (art. 77)",
  lit("L40", "Artículo 77", ["Abogacía del Estado", "Intervención General de la Administración del Estado"]),
  fichab("Quién asesora y quién controla a las Delegaciones y Subdelegaciones",
         "Abogacía del Estado (asistencia jurídica); Intervención General de la Administración del Estado (intervención y control económico-financiero)",
         "De acuerdo con su normativa específica",
         "—",
         "Asistencia jurídica → **Abogacía del Estado**; control → **IGAE**."))}

{unidad("4.3 Comisión interministerial de coordinación de la Administración periférica del Estado (art. 78)",
  lit("L40", "Artículo 78", ["es un órgano colegiado, adscrito al Ministerio de Hacienda y Administraciones Públicas", "coordinar la actuación de la Administración periférica del Estado con los distintos Departamentos ministeriales"]),
  fichab("Órgano colegiado de coordinación de la Administración periférica",
         "Adscrita al Ministerio de Hacienda y Administraciones Públicas",
         "Coordina la Administración periférica con los Departamentos ministeriales; atribuciones, composición y funcionamiento por Real Decreto",
         "—",
         "Es órgano **colegiado** y **adscrito** al Ministerio de Hacienda y Administraciones Públicas; su régimen se regula **mediante Real Decreto**."))}

{unidad("4.4 Órganos colegiados de asistencia al Delegado y al Subdelegado (art. 79)",
  lit("L40", "Artículo 79", ["Comisión territorial de asistencia al Delegado del Gobierno", "Comisión de asistencia al Delegado del Gobierno", "Comisión de asistencia al Subdelegado del Gobierno"]),
  fichab("Comisiones de asistencia",
         ["Pluriprovinciales: Comisión territorial de asistencia al Delegado (preside el Delegado; la integran los Subdelegados)", "Uniprovinciales: Comisión de asistencia al Delegado (preside el Delegado; Secretario General y titulares de servicios que el Delegado considere)", "Cada Subdelegación: Comisión de asistencia al Subdelegado (preside el Subdelegado; Secretario General y titulares de servicios que el Subdelegado considere)"],
         "Coordinar actuaciones homogéneas, homogeneizar políticas públicas, asesorar en simplificación y racionalización y las demás que el Delegado considere adecuadas",
         "—",
         "La Comisión **territorial** existe en las CC. AA. **pluriprovinciales** y la integran los **Subdelegados**; en las **uniprovinciales**, la Comisión de asistencia la integran el **Secretario General** y los titulares de servicios."))}
""", 2)

T.ap("s17", "V.5 Cuadro de los órganos territoriales (esquema)", f"""
*Esquema de elaboración propia: resume los arts. 55.4, 69, 70, 72 y 74 de la Ley 40/2015; no es texto legal.*

| | Delegado del Gobierno | Subdelegado del Gobierno | Director Insular |
|---|---|---|---|
| Ámbito | Comunidad Autónoma | Provincia (CC. AA. pluriprovinciales; potestativo en uniprovinciales) | Islas que se determinen reglamentariamente |
| Clase y rango | Órgano directivo, **rango de Subsecretario** | Órgano directivo, **nivel de Subdirector general** | Nivel que fije la RPT |
| Nombramiento | **Consejo de Ministros** (Real Decreto), a propuesta del **Presidente del Gobierno** | El **Delegado**, por libre designación | El **Delegado**, por libre designación |
| Requisito | Competencia profesional y experiencia; idoneidad (Ley 3/2015) | Funcionario de carrera A1 | Funcionario de carrera A1 |
| Dependencia | Orgánica: Presidente del Gobierno; funcional: Ministerio competente | Inmediata del Delegado | Jerárquica del Delegado o del Subdelegado |

{resumen([
  "Una **Delegación** en cada Comunidad Autónoma, con sede donde radique su **Consejo de Gobierno**; adscrita orgánicamente al Ministerio de Hacienda y Administraciones Públicas (69).",
  "Delegado: **rango de Subsecretario**; Real Decreto del **Consejo de Ministros** a propuesta del **Presidente del Gobierno**; depende orgánicamente del **Presidente** (72).",
  "Subdelegado: **nivel de Subdirector General**; lo nombra el **Delegado** por libre designación entre funcionarios **A1** (74); dirige la **protección civil** (75).",
  "Servicios integrados → Delegado a través de la **Secretaría General**; no integrados → órgano central (71 y 76)."],
  "Siguiente: VI. ¿Cómo se organiza la AGE en el exterior?")}
""", 2)

# =============================================================================
T.ap("bVI", "VI. ¿Cómo se organiza la AGE en el exterior? (Ley 40/2015, arts. 55.5 y 80; Ley 2/2014)", donde(
  "Sexta y última pregunta. La tercera pieza de la AGE es la **Administración General del Estado en el exterior** (art. 55.2 c → I.2.1). La Ley 40/2015 la remite a la **Ley 2/2014, de la Acción y del Servicio Exterior del Estado**.",
  ["1 La AGE en el exterior y el Servicio Exterior del Estado (Ley 40/2015, arts. 55.5 y 80; Ley 2/2014, arts. 1.2 c y 41)", "2 Quién dirige la Política Exterior: Gobierno, Presidente y Ministros (Ley 2/2014, art. 6)", "3 Misiones Diplomáticas y Representaciones Permanentes (Ley 2/2014, arts. 42, 44 y 45)", "4 Oficinas Consulares (Ley 2/2014, arts. 47 y 48)"]))

T.ap("s18", "VI.1 La AGE en el exterior y el Servicio Exterior del Estado (Ley 40/2015, arts. 55.5 y 80; Ley 2/2014, arts. 1.2 c y 41)", f"""
{unidad("1.1 Órganos directivos en el exterior y régimen aplicable (Ley 40/2015, arts. 55.5 y 80)",
  lit("L40", "Artículo 55", ["los embajadores y representantes permanentes ante Organizaciones internacionales"], solo=[15]),
  lit("L40", "Artículo 80", ["Ley 2/2014, de 25 de marzo, de la Acción y del Servicio Exterior del Estado", "supletoriamente"]),
  fichab("Régimen de la AGE en el exterior",
         "Órganos directivos: embajadores y representantes permanentes ante Organizaciones internacionales",
         "El Servicio Exterior se rige por la Ley 2/2014 y su normativa de desarrollo; la Ley 40/2015 se aplica **supletoriamente**",
         "—",
         "Los **embajadores** son órganos **directivos** (no superiores). La Ley 40/2015 es **supletoria** para el Servicio Exterior."))}

{unidad("1.2 Concepto y funciones del Servicio Exterior del Estado (Ley 2/2014, arts. 1.2 c y 41)",
  lit("L2_2014", "Artículo 1", ["Servicio Exterior del Estado"], solo=[5]),
  lit("L2_2014", "Artículo 41", ["bajo la dependencia jerárquica del Embajador y orgánica y funcional de los respectivos Departamentos ministeriales", "prestar asistencia y protección"], solo=[1, 2, 3]),
  fichab("Medios de la AGE que ejecutan la Política Exterior y la Acción Exterior",
         "Órganos, unidades administrativas, instituciones y medios humanos y materiales de la AGE que actúan en el exterior",
         ["Dependencia jerárquica del Embajador; orgánica y funcional de los respectivos Departamentos ministeriales", "Aporta análisis y valoración para que el Gobierno formule y ejecute su Política Exterior; promueve y defiende los intereses de España", "Asistencia y protección a los españoles en el exterior y asistencia a las empresas españolas"],
         "—",
         "**Doble dependencia**: **jerárquica** del **Embajador** y **orgánica y funcional** del **Ministerio** del que depende cada unidad."))}
""", 2)

T.ap("s19", "VI.2 Quién dirige la Política Exterior: Gobierno, Presidente y Ministros (Ley 2/2014, art. 6)", f"""
{unidad("2.1 Gobierno, Presidente, Ministros y Ministro de Asuntos Exteriores (Ley 2/2014, art. 6)",
  lit("L2_2014", "Artículo 6", ["El Gobierno dirige la Política Exterior", "determinar las directrices de Política Exterior y velar por su cumplimiento", "dirigen y desarrollan la Acción Exterior del Estado en su ámbito competencial", "planifica y ejecuta la Política Exterior del Estado"]),
  fichab("Reparto de papeles en la Política y la Acción Exterior",
         ["Gobierno: dirige la Política Exterior y aprueba la Estrategia de Acción Exterior y demás instrumentos de planificación", "Presidente del Gobierno: determina las directrices de Política Exterior y vela por su cumplimiento", "Ministros: dirigen y desarrollan la Acción Exterior en su ámbito competencial", "Ministro de Asuntos Exteriores y de Cooperación: planifica y ejecuta la Política Exterior y coordina la Acción Exterior y el Servicio Exterior"],
         "Los Ministros disponen del Servicio Exterior, sin perjuicio de la dirección y coordinación del Jefe de la Misión Diplomática o Representación Permanente",
         "—",
         "**Dirige** la Política Exterior el **Gobierno**; **planifica y ejecuta** el **Ministro de Asuntos Exteriores** (art. 6.5); el **Presidente** determina las **directrices**. Cayó en 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s20", "VI.3 Misiones Diplomáticas y Representaciones Permanentes (Ley 2/2014, arts. 42, 44 y 45)", f"""
{unidad("3.1 Misiones Diplomáticas Permanentes y Representaciones Permanentes (Ley 2/2014, art. 42)",
  lit("L2_2014", "Artículo 42", ["ante uno o varios Estados", "ante la Unión Europea o una Organización Internacional", "Representaciones de Observación", "mediante real decreto del Consejo de Ministros, a iniciativa del Ministerio de Asuntos Exteriores y de Cooperación, y a propuesta del Ministerio de Hacienda y Administraciones Públicas, previo informe del Consejo Ejecutivo de Política Exterior"], solo=[1, 2, 4, 5, 6, 7, 8, 9, 10, 11]),
  fichab("Representación permanente de España ante Estados u organizaciones",
         "Misiones Diplomáticas Permanentes (ante Estados); Representaciones Permanentes (ante la UE o una Organización Internacional)",
         ["Funciones de las Misiones: representar, proteger intereses y nacionales, negociar, informarse, fomentar relaciones y cooperar con la representación exterior de la UE", "Creación y supresión: real decreto del Consejo de Ministros (iniciativa del Ministerio de Asuntos Exteriores y de Cooperación; propuesta del de Hacienda y Administraciones Públicas; previo informe del Consejo Ejecutivo de Política Exterior)"],
         "—",
         "Si España **no es parte** de la organización, la Representación es **de Observación**. Una Misión puede representar a España ante **varios Estados** (acreditación múltiple, con residencia en uno)."))}

{unidad("3.2 La Jefatura de la Misión: Embajadores (Ley 2/2014, art. 44)",
  lit("L2_2014", "Artículo 44", ["Embajador Extraordinario y Plenipotenciario", "El Rey acreditará", "representa al conjunto de la Administración del Estado", "designados y cesarán por real decreto acordado en Consejo de Ministros a propuesta del Ministro de Asuntos Exteriores y de Cooperación", "personas no pertenecientes a la Carrera Diplomática", "Segunda Jefatura"], solo=[1, 2, 3, 6, 10]),
  fichab("Jefe de Misión Diplomática o de Representación Permanente",
         "Embajador Extraordinario y Plenipotenciario (Misión); Embajador Representante Permanente (Representación); también un Encargado de Negocios con cartas de gabinete",
         ["Ostenta la representación y máxima autoridad de España ante el Estado receptor; representa al conjunto de la Administración del Estado y ejerce la jefatura superior del personal de la Misión", "Depende orgánica y funcionalmente del Ministerio de Asuntos Exteriores y de Cooperación", "Acreditación: el Rey, con cartas credenciales; los Encargados de Negocios, con cartas de gabinete del Ministro de Asuntos Exteriores y de Cooperación"],
         "Designación y cese: real decreto acordado en Consejo de Ministros a propuesta del Ministro de Asuntos Exteriores y de Cooperación; entre funcionarios de la Carrera Diplomática, aunque el Gobierno puede designar a personas ajenas a ella. Suplencia: Segunda Jefatura",
         "El Gobierno **puede** nombrar Embajador a quien **no** sea diplomático de carrera. Las **cartas credenciales** las da el **Rey**; las **cartas de gabinete**, el **Ministro**."))}

{unidad("3.3 Organización de la Misión (Ley 2/2014, art. 45.1 y 3)",
  lit("L2_2014", "Artículo 45", ["La Cancillería Diplomática", "órganos técnicos especializados"], solo=[1, 2, 3, 4, 5, 9]),
  fichab("Partes de la Misión Diplomática o Representación Permanente",
         "—",
         ["Jefatura", "Cancillería Diplomática", "Consejerías, Agregadurías, Oficinas sectoriales, Oficinas Económicas y Comerciales, Oficinas Técnicas de Cooperación, Centros Culturales, Centros de Formación de la Cooperación Española e Instituto Cervantes", "En su caso, la Sección de Servicios Comunes"],
         "—",
         "Los órganos técnicos especializados dependen **jerárquicamente del Embajador** y **orgánica y funcionalmente** de sus **Departamentos**, que se encargan de su organización interna y dotación presupuestaria."))}
""", 2)

T.ap("s21", "VI.4 Oficinas Consulares (Ley 2/2014, arts. 47 y 48)", f"""
{unidad("4.1 Las Oficinas Consulares: concepto y creación (Ley 2/2014, art. 47)",
  lit("L2_2014", "Artículo 47", ["prestar asistencia y protección a los españoles en el exterior", "del que dependen orgánica y funcionalmente"], solo=[1, 2]),
  fichab("Órganos de la AGE para las funciones consulares",
         "Oficinas Consulares de Carrera y agencias consulares; dependen orgánica y funcionalmente del Ministerio de Asuntos Exteriores y de Cooperación",
         "Funciones consulares y especialmente asistencia y protección a los españoles en el exterior",
         "Creación y supresión (de carrera y agencias): real decreto del Consejo de Ministros (iniciativa del Ministerio de Asuntos Exteriores y de Cooperación; propuesta del de Hacienda y Administraciones Públicas; previo informe del Consejo Ejecutivo de Política Exterior)",
         "La función que la ley destaca («especialmente») es la **asistencia y protección a los españoles en el exterior**."))}

{unidad("4.2 Clases de Oficinas Consulares y su Jefe (Ley 2/2014, art. 48.1 y 2)",
  lit("L2_2014", "Artículo 48", ["podrán ser de carrera y honorarias", "se crearán por Orden del Ministro de Asuntos Exteriores y de Cooperación", "será designado por Orden del Ministro de Asuntos Exteriores y de Cooperación entre funcionarios de la Carrera Diplomática"], solo=[1, 2]),
  fichab("Oficinas de carrera y honorarias",
         ["De carrera: Consulado General o Consulado, dirigidas por funcionarios de la Carrera Diplomática", "Honorarias: Consulados Honorarios o Viceconsulados Honorarios, a cargo de cónsules honorarios"],
         "El Jefe de la Oficina Consular de carrera: Orden del Ministro de Asuntos Exteriores y de Cooperación, entre funcionarios de la Carrera Diplomática; carta patente otorgada por el Rey con el refrendo del Ministro",
         "Oficinas honorarias: se crean por Orden del Ministro de Asuntos Exteriores y de Cooperación",
         "Oficinas **de carrera** → **real decreto** del Consejo de Ministros (47.2); **honorarias** → **Orden** del Ministro (48.1). Al Embajador lo designa el Consejo de Ministros; al Jefe de Oficina Consular, el **Ministro** por Orden."))}

{resumen([
  "En el exterior son órganos **directivos** los **embajadores** y **representantes permanentes** (55.5); el Servicio Exterior se rige por la **Ley 2/2014** y supletoriamente por la Ley 40/2015 (80).",
  "Servicio Exterior: dependencia **jerárquica del Embajador** y **orgánica y funcional** de cada Ministerio (Ley 2/2014, 41.1).",
  "El **Gobierno dirige** la Política Exterior; el **Ministro de Asuntos Exteriores** la **planifica y ejecuta** (6.1 y 6.5).",
  "Embajadores: **real decreto** del Consejo de Ministros a propuesta del Ministro de Asuntos Exteriores; acreditados por el **Rey** (44). Oficinas consulares de carrera: real decreto; honorarias: **Orden** (47 y 48)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_P3 = examen("P", 3, {
  "a": f"Subsecretarios y Secretarios generales técnicos son **órganos directivos**: {c('L40', 'Artículo 55', 'Órganos directivos: 1.º Los Subsecretarios y Secretarios generales. 2.º Los Secretarios generales técnicos y Directores generales')} (art. 55.3 b).",
  "b": f"Literal del art. 55.3 a): {c('L40', 'Artículo 55', 'Órganos superiores: 1.º Los Ministros. 2.º Los Secretarios de Estado')}.",
  "c": "Quita a los **Secretarios de Estado**, que el art. 55.3 a) 2.º también incluye entre los órganos superiores.",
  "d": f"Secretarios generales y Directores generales son **órganos directivos** (art. 55.3 b): {c('L40', 'Artículo 55', '1.º Los Subsecretarios y Secretarios generales')}; {c('L40', 'Artículo 55', '2.º Los Secretarios generales técnicos y Directores generales')}."},
  [("Ministros", "L40", "Artículo 55", "1.º Los Ministros."), ("Secretarios de Estado", "L40", "Artículo 55", "2.º Los Secretarios de Estado.")])
EX_L11 = examen("L", 11, {
  "a": f"Literal del art. 55 bis: {c('L40', 'Artículo 55 bis', 'no superen el sesenta por ciento ni sean menos del cuarenta por ciento en el ámbito de cada departamento ministerial')}.",
  "b": "Cambia **dos** datos: el ámbito («el conjunto de la AGE» en lugar de «cada departamento ministerial») y los porcentajes (70/30 en lugar de 60/40).",
  "c": f"Los porcentajes son los de la ley, pero cambia el ámbito: la ley dice {c('L40', 'Artículo 55 bis', 'en el ámbito de cada departamento ministerial')}, no en el conjunto de la AGE.",
  "d": f"La ley no distingue: aplica el mismo principio {c('L40', 'Artículo 55 bis', 'de representación equilibrada entre mujeres y hombres')} a {c('L40', 'Artículo 55 bis', 'Las personas titulares de las Secretarías de Estado y de los órganos directivos')}; la «paridad» no aparece."},
  [("cada departamento ministerial", "L40", "Artículo 55 bis", "en el ámbito de cada departamento ministerial"), ("no superen el 60%", "L40", "Artículo 55 bis", "no superen el sesenta por ciento ni sean menos del cuarenta por ciento")])
EX_P2 = examen("P", 2, {
  "a": f"No son órganos superiores (solo lo son {c('L40', 'Artículo 55', 'Los Ministros')} y {c('L40', 'Artículo 55', 'Los Secretarios de Estado')}), y el rango de Subdirector general es el de los **Subdelegados**: {c('L40', 'Artículo 55', 'los cuales tendrán nivel de Subdirector general')}.",
  "b": f"Literal del art. 55.4: {c('L40', 'Artículo 55', 'son órganos directivos tanto los Delegados del Gobierno en las Comunidades Autónomas, que tendrán rango de Subsecretario')}.",
  "c": "Cambia los dos datos: no son órganos superiores y su rango no es el de Director General, sino el de **Subsecretario** (art. 55.4).",
  "d": f"Son órganos directivos, pero el rango es otro: {c('L40', 'Artículo 55', 'que tendrán rango de Subsecretario')}."},
  [("órganos directivos", "L40", "Artículo 55", "son órganos directivos tanto los Delegados del Gobierno en las Comunidades Autónomas"), ("rango de Subsecretario", "L40", "Artículo 55", "que tendrán rango de Subsecretario")])
EX_P1 = examen("P", 1, {
  "a": f"Literal del art. 6.5: {c('L2_2014', 'Artículo 6', 'El Ministro de Asuntos Exteriores y de Cooperación, en el marco de la superior dirección del Gobierno y de su Presidente, planifica y ejecuta la Política Exterior del Estado')}.",
  "b": f"Al Presidente le corresponde {c('L2_2014', 'Artículo 6', 'determinar las directrices de Política Exterior y velar por su cumplimiento')} (art. 6.3); planificar y ejecutar es del Ministro, sin que la ley prevea una «propuesta».",
  "c": "La Ley 2/2014 no atribuye esa función a las Fuerzas y Cuerpos de Seguridad del Estado: el art. 6.5 la atribuye al Ministro de Asuntos Exteriores y de Cooperación.",
  "d": "Tampoco a las Fuerzas Armadas: el art. 6.5 la atribuye al Ministro de Asuntos Exteriores y de Cooperación, en el marco de la dirección del Gobierno y de su Presidente."},
  [("Al Ministro de Asuntos Exteriores y de Cooperación", "L2_2014", "Artículo 6", "El Ministro de Asuntos Exteriores y de Cooperación, en el marco de la superior dirección del Gobierno y de su Presidente, planifica y ejecuta la Política Exterior del Estado")])

T.ap("s22", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **tres** preguntas de este tema y **una** relacionada (la del art. 6.5 de la Ley 2/2014, asignada al tema III.10 y que también corresponde a «La Administración del Estado en el Exterior»). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-P 2025, pregunta 3 · Órganos superiores de los Ministerios (→ III.1.1)", EX_P3,
  "### GACE-L 2025, pregunta 11 · Presencia equilibrada en los nombramientos (→ III.1.4)", EX_L11,
  "### GACE-P 2025, pregunta 2 · Delegados del Gobierno: clase y rango (→ V.1.1)", EX_P2,
  "### GACE-P 2025, pregunta 1 · Quién planifica y ejecuta la Política Exterior (relacionada; → VI.2.1)", EX_P1,
  "### Cómo se pregunta",
  "!> El examen pregunta la **clasificación** (superior o directivo), el **rango** (Subsecretario, Director general, Subdirector general) y los **porcentajes** o el **ámbito** de una regla. Los distractores intercambian superior/directivo, cambian el rango por el del órgano vecino (Delegado ↔ Subdelegado) o amplían el ámbito («el conjunto de la AGE»).",
]))

T.ap("s23", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Principios y estructura | Art. 3.1 (eficacia, jerarquía, descentralización, desconcentración, coordinación); art. 54 (descentralización funcional, desconcentración funcional y territorial); art. 55.2 (central, territorial, exterior); unidades (56) | La Organización Central integra **Ministerios y servicios comunes** |
| II. Ministerios | Real Decreto del **Presidente** (57.3); Subsecretaría y SGT en todo caso (58.2); creación de órganos (59); jerarquía (60) | Hasta Subdirección General: **Real Decreto del Consejo de Ministros**; inferiores: **orden** |
| III. Superiores y directivos | 55.3; alto cargo (55.6); 55 bis; funciones y nombramiento (61 a 67) | Superiores: **Ministros y Secretarios de Estado**; 60/40 **en cada departamento** |
| IV. Servicios comunes | Asesoramiento, apoyo técnico y gestión directa (68.1); gestión compartida por Real Decreto (68.3) | Los dirige el **Subsecretario** |
| V. Órganos territoriales | Delegaciones (69); Delegados (72-73); Subdelegados (74-75); Secretaría General (76) | Delegado: **rango de Subsecretario**; Subdelegado: **nivel de Subdirector General** |
| VI. Exterior | Art. 55.5 y 80; Ley 2/2014: Servicio Exterior (41), art. 6, Misiones (42, 44, 45), Consulados (47, 48) | El **Ministro de Asuntos Exteriores planifica y ejecuta** la Política Exterior |

?> **Trampas frecuentes:** «los Subsecretarios son órganos **superiores**» (son **directivos**); «el Secretario general técnico tiene categoría de **Subsecretario**» (la tiene de **Director general**; la de Subsecretario es del Secretario **general**); «el 60/40 se calcula en el **conjunto de la AGE**» (es **en cada departamento ministerial**); «el Delegado del Gobierno tiene rango de **Director general**» (de **Subsecretario**); «el Subdelegado lo nombra el **Consejo de Ministros**» (lo nombra el **Delegado**); «los Subdirectores generales son **altos cargos**» (**no** lo son); «el Delegado depende orgánicamente del **Ministerio de Hacienda**» (depende del **Presidente del Gobierno**; la **Delegación** está adscrita a Hacienda).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
T.q("L40", "Artículo 3", "Principios", "Según el artículo 3.1 de la Ley 40/2015, las Administraciones Públicas actúan de acuerdo con los principios de:",
    ["Eficacia, jerarquía, descentralización, desconcentración y coordinación.", "Eficacia, jerarquía, centralización, concentración y cooperación.", "Legalidad, jerarquía, autonomía, desconcentración y colaboración.", "Eficiencia, competencia, descentralización, delegación y coordinación."],
    "Art. 3.1 Ley 40/2015.", "actúan de acuerdo con los principios de eficacia, jerarquía, descentralización, desconcentración y coordinación")
T.q("L40", "Artículo 54", "Principios", "Según el artículo 54.1 de la Ley 40/2015, además de los principios del artículo 3, la Administración General del Estado actúa y se organiza de acuerdo con los de:",
    ["Descentralización funcional y desconcentración funcional y territorial.", "Descentralización territorial y desconcentración funcional.", "Centralización funcional y desconcentración territorial.", "Autonomía funcional y descentralización territorial."],
    "Art. 54.1 Ley 40/2015.", "así como los de descentralización funcional y desconcentración funcional y territorial")
T.q("L40", "Artículo 55", "Estructura", "Según el artículo 55.1 de la Ley 40/2015, la organización de la Administración General del Estado responde a los principios de:",
    ["División funcional en Departamentos ministeriales y gestión territorial integrada en Delegaciones del Gobierno en las Comunidades Autónomas.", "División territorial en Departamentos ministeriales y gestión funcional integrada en Subdelegaciones del Gobierno en las provincias.", "Unidad de acción en Ministerios y gestión territorial integrada en las Diputaciones provinciales.", "División funcional en Secretarías de Estado y gestión territorial descentralizada en las Comunidades Autónomas."],
    "Art. 55.1 Ley 40/2015.", "división funcional en Departamentos ministeriales y de gestión territorial integrada en Delegaciones del Gobierno en las Comunidades Autónomas")
T.q("L40", "Artículo 55", "Estructura", "Según el artículo 55.2 de la Ley 40/2015, la Organización Central de la Administración General del Estado integra:",
    ["Los Ministerios y los servicios comunes.", "Los Ministerios y las Delegaciones del Gobierno.", "Los órganos superiores y los Organismos públicos.", "La Presidencia del Gobierno y los órganos constitucionales."],
    "Art. 55.2 a) Ley 40/2015.", "La Organización Central, que integra los Ministerios y los servicios comunes")
T.q("L40", "Artículo 56", "Estructura", "Según el artículo 56.3 de la Ley 40/2015, las unidades administrativas se establecen:",
    ["Mediante las relaciones de puestos de trabajo.", "Por Real Decreto del Consejo de Ministros.", "Por orden del Ministro respectivo.", "Por resolución del Subsecretario del Departamento."],
    "Art. 56.3 Ley 40/2015.", "Las unidades administrativas se establecen mediante las relaciones de puestos de trabajo")
T.q("L40", "Artículo 57", "Ministerios", "Según el artículo 57.3 de la Ley 40/2015, la determinación del número, la denominación y el ámbito de competencia de los Ministerios y las Secretarías de Estado se establece mediante:",
    ["Real Decreto del Presidente del Gobierno.", "Real Decreto del Consejo de Ministros.", "Ley de las Cortes Generales.", "Orden del Ministro de Hacienda."],
    "Art. 57.3 Ley 40/2015.", "se establecen mediante Real Decreto del Presidente del Gobierno")
T.q("L40", "Artículo 58", "Ministerios", "Según el artículo 58.2 de la Ley 40/2015, los Ministerios contarán, en todo caso, con:",
    ["Una Subsecretaría y, dependiendo de ella, una Secretaría General Técnica.", "Una Secretaría de Estado y, dependiendo de ella, una Subsecretaría.", "Una Secretaría General y, dependiendo de ella, una Dirección General de servicios comunes.", "Una Subsecretaría y, dependiendo de ella, una Secretaría General."],
    "Art. 58.2 Ley 40/2015.", "contarán, en todo caso, con una Subsecretaría, y dependiendo de ella una Secretaría General Técnica")
T.q("L40", "Artículo 59", "Ministerios", "Según el artículo 59.1 de la Ley 40/2015, las Direcciones Generales se crean, modifican y suprimen:",
    ["Por Real Decreto del Consejo de Ministros, a iniciativa del Ministro interesado y a propuesta del Ministro de Hacienda y Administraciones Públicas.", "Por Real Decreto del Presidente del Gobierno, a propuesta del Ministro interesado.", "Por orden del Ministro respectivo, previa autorización del Ministro de Hacienda y Administraciones Públicas.", "Por Real Decreto del Consejo de Ministros, a iniciativa del Ministro de Hacienda y Administraciones Públicas y a propuesta del Ministro interesado."],
    "Art. 59.1 Ley 40/2015.", "por Real Decreto del Consejo de Ministros, a iniciativa del Ministro interesado y a propuesta del Ministro de Hacienda y Administraciones Públicas")
T.q("L40", "Artículo 59", "Ministerios", "Según el artículo 59.2 de la Ley 40/2015, los órganos de nivel inferior a Subdirección General se crean, modifican y suprimen:",
    ["Por orden del Ministro respectivo, previa autorización del Ministro de Hacienda y Administraciones Públicas.", "Por Real Decreto del Consejo de Ministros.", "A través de las relaciones de puestos de trabajo, exclusivamente.", "Por resolución del Subsecretario, previo informe de la Secretaría General Técnica."],
    "Art. 59.2 Ley 40/2015.", "Los órganos de nivel inferior a Subdirección General se crean, modifican y suprimen por orden del Ministro respectivo, previa autorización del Ministro de Hacienda y Administraciones Públicas")
T.q("L40", "Artículo 60", "Ministerios", "Según el artículo 60.2 de la Ley 40/2015, los Secretarios Generales Técnicos tienen categoría de:",
    ["Director general.", "Subsecretario.", "Secretario de Estado.", "Subdirector general."],
    "Art. 60.2 Ley 40/2015: los Secretarios generales tienen categoría de Subsecretario y los Secretarios Generales Técnicos, de Director general.", "los Secretarios Generales Técnicos tienen categoría de Director general")
T.q("L40", "Artículo 60", "Ministerios", "Según el artículo 60.2 de la Ley 40/2015, los Secretarios generales tienen categoría de:",
    ["Subsecretario.", "Director general.", "Secretario de Estado.", "Ministro."],
    "Art. 60.2 Ley 40/2015.", "Los Secretarios generales tienen categoría de Subsecretario")
T.q("L40", "Artículo 55", "Superiores y directivos", "Según el artículo 55.3 de la Ley 40/2015, en la organización central son órganos directivos:",
    ["Los Subsecretarios y Secretarios generales.", "Los Ministros.", "Los Secretarios de Estado.", "Los Delegados del Gobierno."],
    "Art. 55.3 b) Ley 40/2015. Los Delegados del Gobierno son órganos directivos, pero de la organización territorial (55.4).", "1.º Los Subsecretarios y Secretarios generales")
T.q("L40", "Artículo 55", "Superiores y directivos", "Según el artículo 55.6 de la Ley 40/2015, los órganos superiores y directivos tienen además la condición de alto cargo, excepto:",
    ["Los Subdirectores generales y asimilados.", "Los Directores generales y asimilados.", "Los Secretarios generales técnicos.", "Los Subsecretarios."],
    "Art. 55.6 Ley 40/2015.", "excepto los Subdirectores generales y asimilados")
T.q("L40", "Artículo 55", "Superiores y directivos", "Según el artículo 55.9 de la Ley 40/2015, corresponde a los órganos superiores:",
    ["Establecer los planes de actuación de la organización situada bajo su responsabilidad.", "El desarrollo y ejecución de los planes de actuación.", "La gestión ordinaria de los asuntos de su competencia.", "La inspección de los servicios del Ministerio."],
    "Art. 55.9 Ley 40/2015: a los directivos les corresponde su desarrollo y ejecución.", "Corresponde a los órganos superiores establecer los planes de actuación de la organización situada bajo su responsabilidad")
T.q("L40", "Artículo 55 bis", "Superiores y directivos", "Según el artículo 55 bis de la Ley 40/2015, el principio de representación equilibrada entre mujeres y hombres en el nombramiento de los titulares de las Secretarías de Estado y de los órganos directivos se aplica:",
    ["En el ámbito de cada departamento ministerial.", "En el conjunto de la Administración General del Estado.", "En el conjunto de los órganos superiores del Gobierno.", "En el ámbito de cada Secretaría de Estado."],
    "Art. 55 bis Ley 40/2015.", "en el ámbito de cada departamento ministerial")
T.q("L40", "Artículo 61", "Ministros", "Según el artículo 61 de la Ley 40/2015, corresponde a los Ministros:",
    ["Imponer la sanción de separación del servicio por faltas muy graves.", "Nombrar y separar a los Secretarios de Estado de su Departamento.", "Desempeñar la jefatura superior de todo el personal del Departamento.", "Convocar y resolver los concursos de personal funcionario."],
    "Art. 61 s) Ley 40/2015. La jefatura superior del personal y los concursos son del Subsecretario (art. 63.1 f y n); los Secretarios de Estado los nombra el Consejo de Ministros (Ley 50/1997, art. 15.1).", "Imponer la sanción de separación del servicio por faltas muy graves")
T.q("L40", "Artículo 61", "Ministros", "Según el artículo 61 h) de la Ley 40/2015, convocar las Conferencias sectoriales en el ámbito de las competencias de su Departamento corresponde:",
    ["A los Ministros.", "A los Secretarios de Estado.", "A los Subsecretarios.", "A los Delegados del Gobierno."],
    "Art. 61 h) Ley 40/2015.", "Mantener las relaciones con las Comunidades Autónomas y convocar las Conferencias sectoriales")
T.q("L40", "Artículo 62", "Secretarios de Estado", "Según el artículo 62.1 de la Ley 40/2015, los Secretarios de Estado son directamente responsables de:",
    ["La ejecución de la acción del Gobierno en un sector de actividad específica.", "La representación ordinaria del Ministerio.", "La dirección de los servicios comunes del Ministerio.", "La gestión de una o varias áreas funcionalmente homogéneas del Ministerio."],
    "Art. 62.1 Ley 40/2015. La representación ordinaria y los servicios comunes son del Subsecretario (63.1); las áreas funcionalmente homogéneas, de los Directores generales (66.1).", "Los Secretarios de Estado son directamente responsables de la ejecución de la acción del Gobierno en un sector de actividad específica")
T.q("L40", "Artículo 62", "Secretarios de Estado", "Según el artículo 62.2 de la Ley 40/2015, corresponde a los Secretarios de Estado nombrar y separar:",
    ["A los Subdirectores Generales de la Secretaría de Estado.", "A los Directores Generales de la Secretaría de Estado.", "A los Subsecretarios del Departamento.", "A los Delegados del Gobierno."],
    "Art. 62.2 c) Ley 40/2015.", "Nombrar y separar a los Subdirectores Generales de la Secretaría de Estado")
T.q("LGOB", "a15", "Secretarios de Estado", "Según el artículo 15.1 de la Ley 50/1997, del Gobierno, los Secretarios de Estado son nombrados y separados:",
    ["Por Real Decreto del Consejo de Ministros, a propuesta del Presidente del Gobierno o del miembro del Gobierno a cuyo Departamento pertenezcan.", "Por el Rey, a propuesta del Presidente del Gobierno.", "Por Orden del Ministro del Departamento.", "Por Real Decreto del Presidente del Gobierno, a propuesta del Consejo de Ministros."],
    "Art. 15.1 Ley 50/1997.", "Los Secretarios de Estado son nombrados y separados por Real Decreto del Consejo de Ministros, aprobado a propuesta del Presidente del Gobierno o del miembro del Gobierno a cuyo Departamento pertenezcan")
T.q("L40", "Artículo 63", "Subsecretarios", "Según el artículo 63.1 de la Ley 40/2015, los Subsecretarios:",
    ["Ostentan la representación ordinaria del Ministerio y dirigen los servicios comunes.", "Ostentan la representación superior del Ministerio y dirigen la política del Departamento.", "Son órganos superiores responsables de un sector de actividad específica.", "Dirigen las Direcciones Generales de su Secretaría de Estado."],
    "Art. 63.1 Ley 40/2015.", "Los Subsecretarios ostentan la representación ordinaria del Ministerio, dirigen los servicios comunes")
T.q("L40", "Artículo 63", "Subsecretarios", "Según el artículo 63.1 ñ) de la Ley 40/2015, el Subsecretario ejerce la potestad disciplinaria del personal del Departamento:",
    ["Por faltas graves o muy graves, salvo la separación del servicio.", "Por faltas leves exclusivamente.", "Por faltas muy graves, incluida la separación del servicio.", "Por cualquier falta, sin excepción."],
    "Art. 63.1 ñ) Ley 40/2015; la separación del servicio la impone el Ministro (art. 61 s).", "Ejercer la potestad disciplinaria del personal del Departamento por faltas graves o muy graves, salvo la separación del servicio")
T.q("L40", "Artículo 63", "Subsecretarios", "Según el artículo 63.3 de la Ley 40/2015, los Subsecretarios serán nombrados y separados:",
    ["Por Real Decreto del Consejo de Ministros a propuesta del titular del Ministerio.", "Por orden del Ministro, entre funcionarios de carrera.", "Por Real Decreto del Presidente del Gobierno.", "Por el Rey, a propuesta del Ministro del Departamento."],
    "Art. 63.3 Ley 40/2015.", "Los Subsecretarios serán nombrados y separados por Real Decreto del Consejo de Ministros a propuesta del titular del Ministerio")
T.q("L40", "Artículo 64", "Secretarios generales", "Según el artículo 64.3 de la Ley 40/2015, los nombramientos de Secretarios generales habrán de efectuarse entre:",
    ["Personas con cualificación y experiencia en el desempeño de puestos de responsabilidad en la gestión pública o privada.", "Funcionarios de carrera del Estado pertenecientes al Subgrupo A1, exclusivamente.", "Funcionarios de carrera de cualquier Administración pertenecientes al Subgrupo A2.", "Miembros de la Carrera Diplomática o del Cuerpo de Abogados del Estado."],
    "Art. 64.3 Ley 40/2015: a diferencia de Subsecretarios, Secretarios generales técnicos y Directores generales, no se exige ser funcionario.", "entre personas con cualificación y experiencia en el desempeño de puestos de responsabilidad en la gestión pública o privada")
T.q("L40", "Artículo 65", "Secretarios generales técnicos", "Según el artículo 65.1 de la Ley 40/2015, los Secretarios generales técnicos tendrán, en todo caso, las competencias relativas a:",
    ["Producción normativa, asistencia jurídica y publicaciones.", "Organización, recursos humanos e inspección de servicios.", "Gestión financiera, presupuestación y contratación.", "Relaciones con las Comunidades Autónomas y Conferencias sectoriales."],
    "Art. 65.1 Ley 40/2015.", "en todo caso, las relativas a producción normativa, asistencia jurídica y publicaciones")
T.q("L40", "Artículo 66", "Directores generales", "Según el artículo 66.2 de la Ley 40/2015, los Directores generales serán nombrados y separados por Real Decreto del Consejo de Ministros:",
    ["A propuesta del titular del Departamento o del Presidente del Gobierno.", "A propuesta del Subsecretario del Departamento.", "A propuesta del Secretario de Estado del que dependan, exclusivamente.", "A propuesta del Ministro de Hacienda y Administraciones Públicas."],
    "Art. 66.2 Ley 40/2015.", "a propuesta del titular del Departamento o del Presidente del Gobierno")
T.q("L40", "Artículo 67", "Subdirectores generales", "Según el artículo 67.2 de la Ley 40/2015, los Subdirectores generales serán nombrados y cesados:",
    ["Por el Ministro, Secretario de Estado o Subsecretario del que dependan.", "Por Real Decreto del Consejo de Ministros.", "Por el Director general del que dependan.", "Por el Ministro de Hacienda y Administraciones Públicas."],
    "Art. 67.2 Ley 40/2015.", "cesados por el Ministro, Secretario de Estado o Subsecretario del que dependan")
T.q("L40", "Artículo 68", "Servicios comunes", "Según el artículo 68.3 de la Ley 40/2015, la gestión compartida de algunos de los servicios comunes podrá preverse:",
    ["Mediante Real Decreto.", "Mediante Orden del Ministro de Hacienda y Administraciones Públicas.", "Mediante acuerdo de la Comisión General de Secretarios de Estado y Subsecretarios.", "Mediante ley."],
    "Art. 68.3 Ley 40/2015.", "Mediante Real Decreto podrá preverse la gestión compartida de algunos de los servicios comunes")
T.q("L40", "Artículo 69", "Órganos territoriales", "Según el artículo 69.2 de la Ley 40/2015, las Delegaciones del Gobierno tendrán su sede, salvo que el Consejo de Ministros acuerde otra distinta y sin perjuicio del Estatuto de Autonomía:",
    ["En la localidad donde radique el Consejo de Gobierno de la Comunidad Autónoma.", "En la localidad donde radique el Parlamento de la Comunidad Autónoma.", "En la capital de la provincia más poblada de la Comunidad Autónoma.", "En la localidad donde radique el Tribunal Superior de Justicia."],
    "Art. 69.2 Ley 40/2015.", "tendrán su sede en la localidad donde radique el Consejo de Gobierno de la Comunidad Autónoma")
T.q("L40", "Artículo 69", "Órganos territoriales", "Según el artículo 69.3 de la Ley 40/2015, las Delegaciones del Gobierno están adscritas orgánicamente:",
    ["Al Ministerio de Hacienda y Administraciones Públicas.", "Al Ministerio del Interior.", "A la Presidencia del Gobierno.", "Al Ministerio de la Presidencia."],
    "Art. 69.3 Ley 40/2015 (cuidado: el Delegado depende orgánicamente del Presidente del Gobierno, art. 72.3).", "Las Delegaciones del Gobierno están adscritas orgánicamente al Ministerio de Hacienda y Administraciones Públicas")
T.q("L40", "Artículo 72", "Delegados del Gobierno", "Según el artículo 72.3 de la Ley 40/2015, los Delegados del Gobierno dependen:",
    ["Orgánicamente del Presidente del Gobierno y funcionalmente del Ministerio competente por razón de la materia.", "Orgánicamente del Ministerio de Hacienda y funcionalmente del Presidente del Gobierno.", "Orgánica y funcionalmente del Ministerio del Interior.", "Orgánicamente del Ministerio competente por razón de la materia y funcionalmente del Presidente del Gobierno."],
    "Art. 72.3 Ley 40/2015.", "dependen orgánicamente del Presidente del Gobierno y funcionalmente del Ministerio competente por razón de la materia")
T.q("L40", "Artículo 72", "Delegados del Gobierno", "Según el artículo 72.4 de la Ley 40/2015, los Delegados del Gobierno serán nombrados y separados:",
    ["Por Real Decreto del Consejo de Ministros, a propuesta del Presidente del Gobierno.", "Por Real Decreto del Consejo de Ministros, a propuesta del Ministro del Interior.", "Por el Presidente del Gobierno, oído el Presidente de la Comunidad Autónoma.", "Por el Rey, a propuesta del Consejo de Ministros."],
    "Art. 72.4 Ley 40/2015.", "serán nombrados y separados por Real Decreto del Consejo de Ministros, a propuesta del Presidente del Gobierno")
T.q("L40", "Artículo 72", "Delegados del Gobierno", "Según el artículo 72.5 de la Ley 40/2015, en caso de ausencia, vacante o enfermedad del Delegado del Gobierno en una Comunidad Autónoma pluriprovincial, será suplido:",
    ["Por el Subdelegado del Gobierno que el Delegado designe y, en su defecto, por el de la provincia en que tenga su sede.", "Por el Secretario General de la Delegación.", "Por el Subdelegado del Gobierno de mayor antigüedad.", "Por quien designe el Ministro de Hacienda y Administraciones Públicas."],
    "Art. 72.5 Ley 40/2015; el Secretario General suple solo en las uniprovinciales sin Subdelegado.", "será suplido por el Subdelegado del Gobierno que el Delegado designe y, en su defecto, al de la provincia en que tenga su sede")
T.q("L40", "Artículo 73", "Delegados del Gobierno", "Según el artículo 73.1 a) de la Ley 40/2015, corresponde a los Delegados del Gobierno nombrar:",
    ["A los Subdelegados del Gobierno en las provincias de su ámbito de actuación y, en su caso, a los Directores Insulares.", "A los Secretarios Generales de las Delegaciones del Gobierno de otras Comunidades Autónomas.", "A los titulares de los servicios no integrados, sin informe del Ministerio.", "A los Jefes de las Fuerzas y Cuerpos de Seguridad del Estado en la provincia."],
    "Art. 73.1 a) 2.º Ley 40/2015.", "Nombrar a los Subdelegados del Gobierno en las provincias de su ámbito de actuación y, en su caso, a los Directores Insulares")
T.q("L40", "Artículo 73", "Delegados del Gobierno", "Según el artículo 73.1 b) de la Ley 40/2015, el Delegado del Gobierno elevará al Gobierno un informe sobre el funcionamiento de los servicios públicos estatales en el ámbito autonómico:",
    ["Con carácter anual.", "Con carácter semestral.", "Cada dos años.", "Solo cuando lo solicite el Consejo de Ministros."],
    "Art. 73.1 b) 4.º Ley 40/2015.", "Elevar al Gobierno, con carácter anual")
T.q("L40", "Artículo 74", "Subdelegados del Gobierno", "Según el artículo 74 de la Ley 40/2015, el Subdelegado del Gobierno en cada provincia tendrá nivel de:",
    ["Subdirector General, y será nombrado por el Delegado del Gobierno mediante libre designación.", "Director General, y será nombrado por el Consejo de Ministros.", "Subsecretario, y será nombrado por el Delegado del Gobierno mediante concurso.", "Subdirector General, y será nombrado por el Ministro de Hacienda y Administraciones Públicas."],
    "Art. 74 Ley 40/2015.", "con nivel de Subdirector General, que será nombrado por aquél mediante el procedimiento de libre designación")
T.q("L40", "Artículo 75", "Subdelegados del Gobierno", "Según el artículo 75 de la Ley 40/2015, dirigir y coordinar la protección civil en el ámbito de la provincia corresponde:",
    ["Al Subdelegado del Gobierno.", "Al Delegado del Gobierno.", "Al Director Insular.", "Al Secretario General de la Subdelegación."],
    "Art. 75 c) Ley 40/2015.", "Dirigir y coordinar la protección civil en el ámbito de la provincia")
T.q("L40", "Artículo 76", "Órganos territoriales", "Según el artículo 76.1 de la Ley 40/2015, las Delegaciones y Subdelegaciones del Gobierno contarán, en todo caso, como órgano de gestión de los servicios comunes, con:",
    ["Una Secretaría General.", "Una Secretaría General Técnica.", "Una Subsecretaría.", "Una Comisión territorial de asistencia."],
    "Art. 76.1 Ley 40/2015.", "contarán, en todo caso, con una Secretaría General")
T.q("L40", "Artículo 77", "Órganos territoriales", "Según el artículo 77 de la Ley 40/2015, la asistencia jurídica en relación con las Delegaciones y Subdelegaciones del Gobierno se ejercerá por:",
    ["La Abogacía del Estado.", "La Intervención General de la Administración del Estado.", "La Secretaría General Técnica del Ministerio de Hacienda.", "El Consejo de Estado."],
    "Art. 77 Ley 40/2015: la intervención y el control económico-financiero, por la IGAE.", "se ejercerán por la Abogacía del Estado y la Intervención General de la Administración del Estado respectivamente")
T.q("L40", "Artículo 79", "Órganos territoriales", "Según el artículo 79.1 de la Ley 40/2015, en cada Comunidad Autónoma pluriprovincial existirá una Comisión territorial de asistencia al Delegado del Gobierno, integrada por:",
    ["Los Subdelegados del Gobierno en las provincias comprendidas en su territorio.", "Los Consejeros del Gobierno de la Comunidad Autónoma.", "Los Presidentes de las Diputaciones provinciales.", "Los Directores generales de los Ministerios con servicios en la Comunidad."],
    "Art. 79.1 a) Ley 40/2015.", "integrada por los Subdelegados del Gobierno en las provincias comprendidas en el territorio de ésta")
T.q("L40", "Artículo 55", "Exterior", "Según el artículo 55.5 de la Ley 40/2015, en la Administración General del Estado en el exterior son órganos directivos:",
    ["Los embajadores y representantes permanentes ante Organizaciones internacionales.", "Los cónsules honorarios.", "Los Secretarios de Estado de Asuntos Exteriores.", "Los agregados sectoriales de las Misiones Diplomáticas."],
    "Art. 55.5 Ley 40/2015.", "son órganos directivos los embajadores y representantes permanentes ante Organizaciones internacionales")
T.q("L40", "Artículo 80", "Exterior", "Según el artículo 80 de la Ley 40/2015, el Servicio Exterior del Estado se rige por la Ley 2/2014, de la Acción y del Servicio Exterior del Estado, y su normativa de desarrollo y:",
    ["Supletoriamente, por lo dispuesto en la Ley 40/2015.", "Preferentemente, por lo dispuesto en la Ley 40/2015.", "Exclusivamente, por los tratados internacionales.", "Supletoriamente, por la Ley 50/1997, del Gobierno."],
    "Art. 80 Ley 40/2015.", "supletoriamente, por lo dispuesto en esta Ley")
T.q("L2_2014", "Artículo 41", "Exterior", "Según el artículo 41.1 de la Ley 2/2014, el Servicio Exterior del Estado actúa en el exterior:",
    ["Bajo la dependencia jerárquica del Embajador y orgánica y funcional de los respectivos Departamentos ministeriales.", "Bajo la dependencia jerárquica, orgánica y funcional del Ministerio de Asuntos Exteriores.", "Bajo la dependencia orgánica del Embajador y jerárquica de los respectivos Departamentos ministeriales.", "Bajo la dependencia jerárquica del Presidente del Gobierno."],
    "Art. 41.1 Ley 2/2014.", "bajo la dependencia jerárquica del Embajador y orgánica y funcional de los respectivos Departamentos ministeriales")
T.q("L2_2014", "Artículo 44", "Exterior", "Según el artículo 44.4 de la Ley 2/2014, los Embajadores serán designados y cesarán:",
    ["Por real decreto acordado en Consejo de Ministros a propuesta del Ministro de Asuntos Exteriores y de Cooperación.", "Por Orden del Ministro de Asuntos Exteriores y de Cooperación.", "Por el Rey, a propuesta del Presidente del Gobierno.", "Por real decreto del Presidente del Gobierno, previa comparecencia ante el Congreso."],
    "Art. 44.4 Ley 2/2014. Por Orden del Ministro se designa a los Encargados de Negocios con cartas de gabinete y a los Jefes de Oficina Consular de carrera (art. 48.2).", "Los Embajadores serán designados y cesarán por real decreto acordado en Consejo de Ministros a propuesta del Ministro de Asuntos Exteriores y de Cooperación")
T.q("L2_2014", "Artículo 48", "Exterior", "Según el artículo 48.1 de la Ley 2/2014, las Oficinas Consulares honorarias se crearán:",
    ["Por Orden del Ministro de Asuntos Exteriores y de Cooperación.", "Por real decreto del Consejo de Ministros.", "Por acuerdo del Jefe de la Misión Diplomática Permanente.", "Por resolución del Consejo Ejecutivo de Política Exterior."],
    "Art. 48.1 Ley 2/2014. Las Oficinas Consulares de carrera, por real decreto del Consejo de Ministros (art. 47.2).", "Las Oficinas Consulares honorarias se crearán por Orden del Ministro de Asuntos Exteriores y de Cooperación")
T.real("P", 3, "Superiores y directivos"); T.real("L", 11, "Superiores y directivos"); T.real("P", 2, "Órganos territoriales")

# Flashcards
for q_, a_, cat in [
  ("Principios de actuación de las AAPP (art. 3.1 Ley 40/2015)", "Eficacia, jerarquía, descentralización, desconcentración y coordinación, con sometimiento pleno a la Constitución, a la Ley y al Derecho.", "Principios"),
  ("Principios que añade el art. 54.1 para la AGE", "Descentralización funcional y desconcentración funcional y territorial.", "Principios"),
  ("¿Qué comprende la AGE? (art. 55.2)", "La Organización Central (Ministerios y servicios comunes), la Organización Territorial y la AGE en el exterior.", "Estructura"),
  ("¿Cómo se determinan el número, denominación y competencias de Ministerios y Secretarías de Estado? (art. 57.3)", "Por Real Decreto del Presidente del Gobierno.", "Ministerios"),
  ("¿Qué órganos tiene en todo caso un Ministerio? (art. 58.2)", "Una Subsecretaría y, dependiendo de ella, una Secretaría General Técnica.", "Ministerios"),
  ("Creación de Direcciones y Subdirecciones Generales (art. 59.1)", "Real Decreto del Consejo de Ministros, a iniciativa del Ministro interesado y a propuesta del Ministro de Hacienda y Administraciones Públicas.", "Ministerios"),
  ("Órganos superiores (art. 55.3 a)", "Los Ministros y los Secretarios de Estado.", "Superiores y directivos"),
  ("Órganos directivos de la organización central (art. 55.3 b)", "Subsecretarios y Secretarios generales; Secretarios generales técnicos y Directores generales; Subdirectores generales.", "Superiores y directivos"),
  ("¿Quiénes no son altos cargos? (art. 55.6)", "Los Subdirectores generales y asimilados.", "Superiores y directivos"),
  ("Regla del art. 55 bis", "Secretarías de Estado y órganos directivos: cada sexo ni más del 60 % ni menos del 40 % en el ámbito de cada departamento ministerial.", "Superiores y directivos"),
  ("Categorías asimiladas (art. 60.2)", "Secretario general = Subsecretario; Secretario General Técnico = Director general.", "Ministerios"),
  ("Nombramiento de los Secretarios de Estado (Ley 50/1997, art. 15.1)", "Real Decreto del Consejo de Ministros, a propuesta del Presidente del Gobierno o del miembro del Gobierno del Departamento.", "Secretarios de Estado"),
  ("Funciones características del Subsecretario (art. 63.1)", "Representación ordinaria del Ministerio, dirección de los servicios comunes y jefatura superior de todo el personal del Departamento.", "Subsecretarios"),
  ("Competencias del Secretario general técnico en todo caso (art. 65.1)", "Producción normativa, asistencia jurídica y publicaciones.", "Secretarios generales técnicos"),
  ("¿Quién nombra a los Subdirectores generales? (art. 67.2)", "El Ministro, Secretario de Estado o Subsecretario del que dependan, respetando igualdad, mérito y capacidad.", "Subdirectores generales"),
  ("Servicios comunes (art. 68.1)", "Asesoramiento, apoyo técnico y, en su caso, gestión directa en funciones comunes del Ministerio (planificación, recursos humanos, producción normativa, asistencia jurídica, gestión financiera, etc.).", "Servicios comunes"),
  ("Delegado del Gobierno: rango, nombramiento y dependencia (arts. 55.4 y 72)", "Órgano directivo con rango de Subsecretario; Real Decreto del Consejo de Ministros a propuesta del Presidente del Gobierno; dependencia orgánica del Presidente y funcional del Ministerio competente.", "Delegados del Gobierno"),
  ("Subdelegado del Gobierno: nivel y nombramiento (art. 74)", "Nivel de Subdirector General; lo nombra el Delegado por libre designación entre funcionarios A1.", "Subdelegados del Gobierno"),
  ("¿Qué órgano gestiona los servicios comunes de Delegaciones y Subdelegaciones? (art. 76.1)", "La Secretaría General.", "Órganos territoriales"),
  ("¿Quién planifica y ejecuta la Política Exterior? (Ley 2/2014, art. 6.5)", "El Ministro de Asuntos Exteriores (en la ley, «y de Cooperación»), en el marco de la superior dirección del Gobierno y de su Presidente.", "Exterior"),
  ("Designación de los Embajadores (Ley 2/2014, art. 44.4)", "Real decreto acordado en Consejo de Ministros a propuesta del Ministro de Asuntos Exteriores; normalmente entre diplomáticos de carrera, aunque el Gobierno puede designar a personas ajenas.", "Exterior"),
  ("Oficinas Consulares de carrera y honorarias: ¿cómo se crean? (Ley 2/2014, arts. 47.2 y 48.1)", "De carrera: real decreto del Consejo de Ministros. Honorarias: Orden del Ministro de Asuntos Exteriores.", "Exterior"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Administración General del Estado", "Administración del Estado organizada en Organización Central (Ministerios y servicios comunes), Organización Territorial y Administración en el exterior (Ley 40/2015, art. 55.2).", "s2", "Estructura")
T.glos("Unidad administrativa", "Elemento organizativo básico de las estructuras orgánicas; agrupa puestos de trabajo vinculados por sus cometidos y una jefatura común; se establece por RPT (art. 56).", "s2", "Estructura")
T.glos("Órganos superiores", "Ministros y Secretarios de Estado; establecen los planes de actuación (art. 55.3 a y 9).", "s6", "Superiores y directivos")
T.glos("Órganos directivos", "Subsecretarios, Secretarios generales, Secretarios generales técnicos, Directores generales y Subdirectores generales en la organización central; Delegados y Subdelegados en la territorial; embajadores y representantes permanentes en el exterior (art. 55.3 a 5).", "s6", "Superiores y directivos")
T.glos("Alto cargo", "Condición de los órganos superiores y directivos, salvo Subdirectores generales y asimilados (art. 55.6; Ley 3/2015).", "s6", "Superiores y directivos")
T.glos("Presencia equilibrada", "Regla por la que en los nombramientos de Secretarías de Estado y órganos directivos cada sexo no supera el 60 % ni baja del 40 % en cada departamento ministerial (art. 55 bis).", "s6", "Superiores y directivos")
T.glos("Subsecretaría", "Órgano directivo que existe en todo Ministerio; ostenta la representación ordinaria y dirige los servicios comunes (arts. 58.2 y 63).", "s9", "Subsecretarios")
T.glos("Secretaría General Técnica", "Órgano directivo dependiente de la Subsecretaría, con categoría de Dirección General; en todo caso, producción normativa, asistencia jurídica y publicaciones (arts. 58.2 y 65).", "s10", "Secretarios generales técnicos")
T.glos("Servicios comunes", "Funciones transversales de apoyo a todo el Ministerio (planificación, recursos humanos, asistencia jurídica, gestión financiera…), dirigidas por el Subsecretario (art. 68).", "s12", "Servicios comunes")
T.glos("Delegado del Gobierno", "Representante del Gobierno de la Nación en una Comunidad Autónoma; órgano directivo con rango de Subsecretario (arts. 72 y 73).", "s14", "Órganos territoriales")
T.glos("Subdelegado del Gobierno", "Órgano directivo de la AGE en cada provincia, con nivel de Subdirector General, nombrado por el Delegado (arts. 74 y 75).", "s15", "Órganos territoriales")
T.glos("Servicios integrados y no integrados", "Servicios territoriales de la AGE que dependen del Delegado a través de la Secretaría General (integrados) o del órgano central competente (no integrados) (art. 71).", "s13", "Órganos territoriales")
T.glos("Servicio Exterior del Estado", "Órganos, unidades, instituciones y medios de la AGE que actúan en el exterior, bajo la dependencia jerárquica del Embajador y orgánica y funcional de cada Ministerio (Ley 2/2014, arts. 1.2 c y 41).", "s18", "Exterior")
T.glos("Oficina Consular", "Órgano de la AGE para las funciones consulares, especialmente la asistencia y protección a los españoles en el exterior; de carrera u honoraria (Ley 2/2014, arts. 47 y 48).", "s21", "Exterior")

# Cronología (fechas de los metadatos del BOE)
T.hito("1997", "Ley 50/1997, de 27 de noviembre, del Gobierno (BOE de 28-11-1997)", "Art. 15.1: nombramiento y separación de los Secretarios de Estado", "normativo", "s8")
T.hito("2014", "Ley 2/2014, de 25 de marzo, de la Acción y del Servicio Exterior del Estado (BOE de 26-3-2014; vigor el 27-3-2014)", "Servicio Exterior, Misiones Diplomáticas, Embajadores y Oficinas Consulares", "normativo", "s18")
T.hito("2015", "Ley 40/2015, de 1 de octubre, de Régimen Jurídico del Sector Público (BOE de 2-10-2015)", "Título I: organización y funcionamiento de la Administración General del Estado (arts. 54 a 80)", "normativo", "s1")
T.hito("2016", "Entrada en vigor de la Ley 40/2015 (2-10-2016)", "Fecha de vigencia que dan los metadatos del BOE", "normativo", "s2")
T.hito("2024", "Ley Orgánica 2/2024, de 1 de agosto, de representación paritaria y presencia equilibrada de mujeres y hombres (BOE de 2-8-2024; vigor el 22-8-2024)", "Añade el art. 55 bis de la Ley 40/2015 (60/40 en cada departamento ministerial)", "normativo", "s6")

T.publicar()
