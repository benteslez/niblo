# -*- coding: utf-8 -*-
"""Tema I.10 (B1T10): Organización territorial (I): las Comunidades Autónomas. Los
Estatutos de Autonomía. Organización política y administrativa. La delimitación de
competencias entre el Estado y las Comunidades Autónomas en la Constitución y en los
Estatutos de Autonomía.
Método del I.2. Normas (textos consolidados del BOE): CE, arts. 2, 3.2, 4.2, 81.1, 137 a
139, 143 a 158, disposición adicional primera y transitorias primera, segunda, cuarta y
quinta; LO 3/1980, del Consejo de Estado, art. 22; Ley 22/2009 (preámbulo, solo para la
pregunta oficial sobre el Fondo de Suficiencia Global)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO["L22_2009"] = "Ley 22/2009"

T = Tema("B1T10",
  "Cinco preguntas: I. Qué son las Comunidades Autónomas y cómo se constituyen (arts. 2, 137 a 139, 143 a 145 y 151.1 CE) · II. Qué son los Estatutos de Autonomía y cómo se aprueban y reforman (arts. 81.1, 146, 147, 151.2 y 152.2) · III. Cómo se organizan y con qué medios (arts. 152, 154 y 156 a 158) · IV. Quién hace qué: la delimitación de competencias (arts. 148 a 150) · V. Quién controla a las Comunidades Autónomas (arts. 153 y 155). Cada artículo: texto literal del BOE y ficha.",
  ["Art. 2 CE", "Art. 137", "Solidaridad", "Art. 139", "Art. 143", "Art. 151", "Federación", "Estatutos de Autonomía", "Art. 147", "Art. 152", "Delegado del Gobierno", "Autonomía financiera", "Art. 148", "Art. 149.1", "Cláusula residual", "Art. 150", "Art. 153", "Art. 155"])

# =============================================================================
T.ap("s0", "Mapa del tema: cinco preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque I, tema 10):
> Organización territorial (I): las Comunidades Autónomas. Los Estatutos de Autonomía. Organización política y administrativa. La delimitación de competencias entre el Estado y las Comunidades Autónomas en la Constitución y en los Estatutos de Autonomía.

### El hilo conductor

El epígrafe se lee como **cinco preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Constitución | Otras normas |
|---|---|---|---|
| **I** | ¿Qué son las Comunidades Autónomas y cómo se constituyen? | Arts. 2, 137, 138, 139, 143, 144, 145 y 151.1; disposiciones transitorias primera, segunda, cuarta y quinta | — |
| **II** | ¿Qué son los Estatutos de Autonomía y cómo se aprueban y reforman? | Arts. 81.1, 146, 147, 151.2 y 3 y 152.2; arts. 3.2 y 4.2; disposición adicional primera | — |
| **III** | ¿Cómo se organizan y con qué medios? (organización política y administrativa) | Arts. 152.1 y 3, 154, 156, 157 y 158 | Ley 22/2009 (preámbulo) |
| **IV** | ¿Quién hace qué? (delimitación de competencias en la Constitución y en los Estatutos) | Arts. 148, 149 y 150 | — |
| **V** | ¿Quién controla a las Comunidades Autónomas? | Arts. 153 y 155 | LO 3/1980, del Consejo de Estado, art. 22 |

!> **La idea que une los cinco bloques:** la Constitución parte de la **unidad** de la Nación y reconoce el **derecho a la autonomía** de nacionalidades y regiones (I). Ese derecho se concreta en un **Estatuto**, norma institucional básica aprobada por **ley orgánica** (II), que crea unas **instituciones propias** con medios financieros (III) y asume **competencias** dentro del marco de los arts. 148 y 149 (IV). El ejercicio de la autonomía está sujeto a **controles** tasados y, en último extremo, a la **coerción estatal** del art. 155 (V).

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen; o, para un derecho, Titulares · Contenido · Límites · Protección · ⚠ Ojo en el examen).
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- Los Estatutos de Autonomía no se desarrollan uno a uno: el tema estudia lo que la Constitución dice **de todos** ellos.
- Fronteras con otros temas: los Senadores de designación autonómica (art. 69.5) se estudian en el tema I.5; el Delegado del Gobierno en la Ley 40/2015, en el tema I.8; los conflictos de competencia y la impugnación del art. 161.2 ante el Tribunal Constitucional, en el tema I.3; las leyes del art. 150 como tipos de ley, en el tema IV.2.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué son las Comunidades Autónomas y cómo se constituyen? (arts. 2, 137 a 139, 143 a 145 y 151.1)", donde(
  "Primera pregunta del tema. Antes de los Estatutos, las instituciones o las competencias, hay que saber **en qué principios** se apoya el Estado autonómico y **por qué vías** se accede a la autonomía.",
  ["1 Unidad, autonomía y organización territorial (arts. 2 y 137)", "2 Solidaridad e igualdad (arts. 138 y 139)", "3 La vía general de acceso y la intervención de las Cortes (arts. 143 y 144)", "4 Ni federación: convenios y acuerdos de cooperación (art. 145)", "5 La vía del art. 151.1 y las disposiciones transitorias"]))

T.ap("s1", "I.1 Unidad, autonomía y organización territorial (arts. 2 y 137)", f"""
La Constitución combina tres ideas en un solo artículo: **unidad** de la Nación, **derecho a la autonomía** y **solidaridad**. El art. 137 traduce la autonomía en una organización territorial.

{unidad("1.1 Unidad, autonomía y solidaridad (art. 2)",
  lit("CE", "Artículo 2", ["indisoluble unidad de la Nación española", "el derecho a la autonomía de las nacionalidades y regiones que la integran", "la solidaridad entre todas ellas"]),
  fichab("Fundamento constitucional del Estado autonómico",
         f"{c('CE', 'Artículo 2', 'las nacionalidades y regiones que la integran')} (titulares del derecho a la autonomía)",
         f"La Constitución {c('CE', 'Artículo 2', 'reconoce y garantiza el derecho a la autonomía')} sobre la base de la {c('CE', 'Artículo 2', 'indisoluble unidad de la Nación española')}",
         "—",
         "Tres principios en un solo artículo: **unidad**, **autonomía** y **solidaridad**. Los titulares del derecho son las **nacionalidades y regiones**, no las provincias ni los municipios."))}

{unidad("1.2 Municipios, provincias y Comunidades Autónomas (art. 137)",
  lit("CE", "Artículo 137", ["en municipios, en provincias y en las Comunidades Autónomas que se constituyan", "autonomía para la gestión de sus respectivos intereses"]),
  fichab("La organización territorial del Estado",
         f"Tres entidades: {c('CE', 'Artículo 137', 'municipios')}, {c('CE', 'Artículo 137', 'provincias')} y {c('CE', 'Artículo 137', 'Comunidades Autónomas que se constituyan')}",
         f"Todas {c('CE', 'Artículo 137', 'gozan de autonomía para la gestión de sus respectivos intereses')}",
         "—",
         "Las Comunidades Autónomas son las «**que se constituyan**»: la Constitución no las enumera. La autonomía es «para la gestión de sus **respectivos intereses**» (no soberanía). Municipio y provincia: tema I.11."))}
""", 2)

T.ap("s2", "I.2 Solidaridad e igualdad (arts. 138 y 139)", f"""
{unidad("2.1 El Estado garantiza la solidaridad; los Estatutos no crean privilegios (art. 138)",
  lit("CE", "Artículo 138", ["equilibrio económico, adecuado y justo", "circunstancias del hecho insular", "privilegios económicos o sociales"]),
  fichab("Principio de solidaridad interterritorial",
         c("CE", "Artículo 138", "El Estado"),
         [f"Velando por {c('CE', 'Artículo 138', 'un equilibrio económico, adecuado y justo entre las diversas partes del territorio español')}", f"Atendiendo {c('CE', 'Artículo 138', 'en particular a las circunstancias del hecho insular')}", "Las diferencias entre Estatutos no pueden implicar privilegios económicos o sociales (138.2)"],
         "—",
         "La garantía de la solidaridad es del **Estado**. La circunstancia que se cita expresamente es el **hecho insular**. Lo prohibido son los **privilegios económicos o sociales**, no las diferencias entre Estatutos."))}

{unidad("2.2 Mismos derechos y libre circulación en todo el territorio (art. 139)",
  lit("CE", "Artículo 139", ["los mismos derechos y obligaciones en cualquier parte del territorio del Estado", "libertad de circulación y establecimiento de las personas y la libre circulación de bienes"]),
  ficha(c("CE", "Artículo 139", "Todos los españoles"),
        "Los mismos derechos y obligaciones en cualquier parte del territorio del Estado (139.1)",
        "—",
        f"{c('CE', 'Artículo 139', 'Ninguna autoridad podrá adoptar medidas que directa o indirectamente obstaculicen')} la libre circulación de personas y bienes (139.2)",
        "Cayó en 2025 (→ Cierre 1): el art. 139 habla de igualdad de derechos y obligaciones de **los españoles**, no de igualdad de las **Comunidades Autónomas**. La prohibición del 139.2 alcanza a medidas que obstaculicen **directa o indirectamente**."))}
""", 2)

T.ap("s3", "I.3 La vía general de acceso y la intervención de las Cortes (arts. 143 y 144)", f"""
{unidad("3.1 Quién puede acceder al autogobierno y quién tiene la iniciativa (art. 143)",
  lit("CE", "Artículo 143", ["provincias limítrofes con características históricas, culturales y económicas comunes, los territorios insulares y las provincias con entidad regional histórica", "todas las Diputaciones interesadas o al órgano interinsular correspondiente y a las dos terceras partes de los municipios", "en el plazo de seis meses", "pasados cinco años"]),
  fichab("Acceso a la autonomía por la vía general",
         ["::Pueden constituirse en Comunidad Autónoma:", "Provincias limítrofes con características históricas, culturales y económicas comunes", "Territorios insulares", "Provincias con entidad regional histórica"],
         [f"::Iniciativa (143.2): {c('CE', 'Artículo 143', 'todas las Diputaciones interesadas o al órgano interinsular correspondiente')}", f"y {c('CE', 'Artículo 143', 'las dos terceras partes de los municipios cuya población represente, al menos, la mayoría del censo electoral de cada provincia o isla')}"],
         ["**Seis meses** desde el primer acuerdo de alguna Corporación local interesada para cumplir los requisitos", "Si no prospera: solo puede reiterarse **pasados cinco años** (143.3)"],
         "Vía general: **todas** las Diputaciones + **dos tercios** de los municipios que sean **mayoría del censo** de cada provincia o isla. Comparar con la vía del 151.1: **tres cuartas partes** de los municipios y referéndum (→ I.5.1)."))}

{unidad("3.2 Las Cortes, por ley orgánica y por interés nacional (art. 144)",
  lit("CE", "Artículo 144", ["mediante ley orgánica", "por motivos de interés nacional"]),
  fichab("Intervención extraordinaria de las Cortes en el acceso a la autonomía",
         c("CE", "Artículo 144", "Las Cortes Generales"),
         ["Autorizar una comunidad autónoma de ámbito no superior a una provincia sin las condiciones del 143.1 (letra a)", "Autorizar o acordar un Estatuto para territorios no integrados en la organización provincial (letra b)", "Sustituir la iniciativa de las Corporaciones locales del 143.2 (letra c)"],
         f"{c('CE', 'Artículo 144', 'mediante ley orgánica')}",
         "Dos requisitos juntos: **ley orgánica** y **motivos de interés nacional**. A este artículo remite la disposición transitoria quinta para Ceuta y Melilla (→ I.5.2)."))}
""", 2)

T.ap("s4", "I.4 Ni federación: convenios y acuerdos de cooperación (art. 145)", f"""
{unidad("4.1 Prohibición de federación y cooperación entre Comunidades (art. 145)",
  lit("CE", "Artículo 145", ["En ningún caso se admitirá la federación de Comunidades Autónomas", "comunicación a las Cortes Generales", "necesitarán la autorización de las Cortes Generales"]),
  fichab("Límites a las relaciones entre Comunidades Autónomas",
         "Las Comunidades Autónomas; las Cortes Generales (comunicación o autorización)",
         ["Federación: prohibida en todo caso (145.1)", "Convenios para la gestión y prestación de servicios propios: en los supuestos, requisitos y términos que prevean los Estatutos, con comunicación a las Cortes Generales (145.2)", "Demás acuerdos de cooperación: autorización de las Cortes Generales (145.2)"],
         "—",
         "Cayó en 2025 (→ Cierre 1): la federación está **prohibida** («**En ningún caso**»), ni por ley orgánica ni por acuerdo de las Asambleas. Convenio de servicios propios = **comunicación**; otros acuerdos de cooperación = **autorización** de las Cortes."))}
""", 2)

T.ap("s5", "I.5 La vía del art. 151.1 y las disposiciones transitorias", f"""
{unidad("5.1 Iniciativa reforzada y referéndum (art. 151.1)",
  lit("CE", "Artículo 151", ["No será preciso dejar transcurrir el plazo de cinco años", "las tres cuartas partes de los municipios de cada una de las provincias afectadas", "por el voto afirmativo de la mayoría absoluta de los electores de cada provincia"], solo=[1]),
  fichab("Acceso a la autonomía sin esperar los cinco años del art. 148.2",
         f"Las Diputaciones u órganos interinsulares y {c('CE', 'Artículo 151', 'las tres cuartas partes de los municipios de cada una de las provincias afectadas que representen, al menos, la mayoría del censo electoral de cada una de ellas')}",
         "Iniciativa acordada dentro del plazo del 143.2 y ratificada mediante referéndum, en los términos de una ley orgánica",
         ["Iniciativa en el plazo del art. 143.2 (seis meses)", f"Referéndum: {c('CE', 'Artículo 151', 'voto afirmativo de la mayoría absoluta de los electores de cada provincia')}"],
         "**Tres cuartas partes** de los municipios (no dos tercios) y referéndum con mayoría absoluta de los **electores** (no de los votos emitidos) de **cada provincia**. Ventaja: no hay que esperar **cinco años** para ampliar competencias (→ IV.1.2)."))}

{unidad("5.2 Las disposiciones transitorias del acceso (primera, segunda, cuarta y quinta)",
  lit("CE", "primera-2", ["mediante acuerdo adoptado por la mayoría absoluta de sus miembros"]),
  lit("CE", "segunda-2", ["hubiesen plebiscitado afirmativamente proyectos de Estatuto de autonomía"]),
  lit("CE", "cuarta-2", ["En el caso de Navarra", "ratificada por referéndum"], solo=[1]),
  lit("CE", "quinta", ["Las ciudades de Ceuta y Melilla podrán constituirse en Comunidades Autónomas", "mediante una ley orgánica, en los términos previstos en el artículo 144"]),
  fichab("Reglas especiales de acceso previstas en 1978",
         ["Territorios con régimen provisional de autonomía (primera y segunda)", "Navarra (cuarta)", "Ceuta y Melilla (quinta)"],
         ["Primera: los órganos colegiados superiores preautonómicos pueden sustituir la iniciativa de las Diputaciones", "Segunda: territorios que plebiscitaron Estatuto en el pasado y con régimen provisional: acceso directo, con Estatuto elaborado según el art. 151.2", "Cuarta: Navarra, para incorporarse al régimen autonómico vasco: iniciativa del Órgano Foral, ratificada por referéndum", "Quinta: Ceuta y Melilla, por acuerdo de sus Ayuntamientos y autorización de las Cortes por ley orgánica (art. 144)"],
         ["Primera, segunda y quinta: **mayoría absoluta**", "Cuarta: mayoría de los miembros del Órgano Foral; referéndum por mayoría de los votos válidos"],
         "Ceuta y Melilla: **Ayuntamientos** por **mayoría absoluta** + **ley orgánica** de las Cortes «en los términos previstos en el artículo **144**»."))}

{resumen([
  "Art. 2: **unidad** de la Nación, **derecho a la autonomía** de nacionalidades y regiones y **solidaridad**; art. 137: municipios, provincias y Comunidades Autónomas «que se constituyan», con autonomía para la gestión de sus **respectivos intereses**.",
  "Art. 138: el **Estado** garantiza la solidaridad (atendiendo al **hecho insular**) y las diferencias entre Estatutos no pueden suponer **privilegios económicos o sociales**; art. 139: **mismos derechos y obligaciones** de todos los españoles en todo el territorio.",
  "Vía general (143): **todas** las Diputaciones + **2/3** de los municipios (mayoría del censo); **6 meses**; si fracasa, **5 años**. Las Cortes pueden intervenir por **ley orgánica** y **interés nacional** (144).",
  "**Prohibida la federación** (145.1). Vía del 151.1: **3/4** de los municipios y referéndum por **mayoría absoluta de los electores** de cada provincia."],
  "Siguiente: II. ¿Qué son los Estatutos de Autonomía y cómo se aprueban y reforman?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Qué son los Estatutos de Autonomía y cómo se aprueban y reforman? (arts. 81.1, 146, 147, 151.2 y 152.2)", donde(
  "Segunda pregunta. El derecho a la autonomía se concreta en un **Estatuto**. Hay que saber qué es, qué contiene, quién lo elabora y cómo se reforma, porque el procedimiento cambia según la vía de acceso.",
  ["1 Norma institucional básica aprobada por ley orgánica (arts. 81.1 y 147.1 y 2)", "2 Elaboración: vía general y vía del art. 151 (arts. 146 y 151.2 y 3)", "3 Reforma de los Estatutos (arts. 147.3 y 152.2)", "4 Otras materias que la Constitución remite a los Estatutos (arts. 3.2 y 4.2; disposición adicional primera)"]))

T.ap("s6", "II.1 Norma institucional básica aprobada por ley orgánica (arts. 81.1 y 147.1 y 2)", f"""
{unidad("1.1 Los Estatutos se aprueban por ley orgánica (art. 81.1)",
  lit("CE", "Artículo 81", ["las que aprueben los Estatutos de Autonomía"], solo=[1]),
  fichab("Forma de aprobación del Estatuto",
         "Las Cortes Generales",
         f"Por ley orgánica: {c('CE', 'Artículo 81', 'las que aprueben los Estatutos de Autonomía')}",
         "Ley orgánica: mayoría absoluta del Congreso en una votación final sobre el conjunto del proyecto (art. 81.2; tema IV.2)",
         "El Estatuto es una **ley orgánica del Estado**, aprobada por las Cortes, no por la Comunidad Autónoma."))}

{unidad("1.2 Naturaleza y contenido obligatorio (art. 147.1 y 2)",
  lit("CE", "Artículo 147", ["la norma institucional básica de cada Comunidad Autónoma", "parte integrante de su ordenamiento jurídico", "La denominación de la Comunidad que mejor corresponda a su identidad histórica", "La delimitación de su territorio", "La denominación, organización y sede de las instituciones autónomas propias", "Las competencias asumidas dentro del marco establecido en la Constitución"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("El Estatuto de Autonomía",
         f"Cada Comunidad Autónoma; {c('CE', 'Artículo 147', 'el Estado los reconocerá y amparará como parte integrante de su ordenamiento jurídico')}",
         ["::Contenido obligatorio (147.2):", "Denominación (identidad histórica)", "Delimitación del territorio", "Denominación, organización y sede de las instituciones propias", "Competencias asumidas y bases para el traspaso de servicios"],
         "—",
         f"{c('CE', 'Artículo 147', 'Dentro de los términos de la presente Constitución')}: el Estatuto está sometido a la Constitución. Son **cuatro** contenidos obligatorios; las competencias se asumen «dentro del marco establecido en la Constitución» (→ IV.2.1)."))}
""", 2)

T.ap("s7", "II.2 Elaboración: vía general y vía del art. 151 (arts. 146 y 151.2 y 3)", f"""
{unidad("2.1 Vía general: asamblea de la Diputación y parlamentarios (art. 146)",
  lit("CE", "Artículo 146", ["los miembros de la Diputación u órgano interinsular de las provincias afectadas y por los Diputados y Senadores elegidos en ellas", "para su tramitación como ley"]),
  fichab("Elaboración del proyecto de Estatuto por la vía general",
         f"Una asamblea de {c('CE', 'Artículo 146', 'los miembros de la Diputación u órgano interinsular de las provincias afectadas')} y {c('CE', 'Artículo 146', 'los Diputados y Senadores elegidos en ellas')}",
         f"El proyecto {c('CE', 'Artículo 146', 'será elevado a las Cortes Generales para su tramitación como ley')}",
         "—",
         "En la vía general la asamblea mezcla **diputados provinciales** y **parlamentarios**; en la del art. 151 solo hay **Diputados y Senadores** (→ II.2.2)."))}

{unidad("2.2 Vía del art. 151: Asamblea de Parlamentarios, Comisión Constitucional y referéndum (art. 151.2 y 3)",
  lit("CE", "Artículo 151", ["El Gobierno convocará a todos los Diputados y Senadores", "mediante el acuerdo de la mayoría absoluta de sus miembros", "Comisión Constitucional del Congreso, la cual, dentro del plazo de dos meses", "mediante un voto de ratificación", "será tramitado como proyecto de ley ante las Cortes Generales"], solo=[2, 3, 4, 5, 6, 7, 8]),
  fichab("Elaboración del Estatuto por la vía del art. 151",
         ["El **Gobierno** convoca a los Diputados y Senadores del territorio (Asamblea de Parlamentarios)", "Comisión Constitucional del **Congreso** con una delegación de la Asamblea", "Cuerpo electoral de las provincias (referéndum)", "Plenos de ambas Cámaras (ratificación)", "El Rey sanciona y promulga"],
         ["1.º Proyecto aprobado por la Asamblea de Parlamentarios", "2.º Examen de común acuerdo con la Comisión Constitucional", "3.º Si hay acuerdo: referéndum en las provincias", "4.º Aprobado en cada provincia: voto de ratificación de los plenos de ambas Cámaras", "5.º Sin acuerdo: se tramita como proyecto de ley y el texto aprobado se somete a referéndum"],
         ["Proyecto: **mayoría absoluta** de los miembros de la Asamblea", "Comisión Constitucional: **dos meses**", "Referéndum: **mayoría de los votos válidamente emitidos** en cada provincia"],
         "Aquí el referéndum se gana por **mayoría de los votos válidos** en cada provincia (en el 151.1, por mayoría absoluta de los **electores**). Si una provincia dice no, las demás pueden constituir la Comunidad (151.3)."))}
""", 2)

T.ap("s8", "II.3 Reforma de los Estatutos (arts. 147.3 y 152.2)", f"""
{unidad("3.1 Regla general: procedimiento del Estatuto y ley orgánica (art. 147.3)",
  lit("CE", "Artículo 147", ["al procedimiento establecido en los mismos", "mediante ley orgánica"], solo=[7]),
  fichab("Reforma de los Estatutos",
         "La Comunidad Autónoma (según su Estatuto) y las Cortes Generales",
         c("CE", "Artículo 147", "La reforma de los Estatutos se ajustará al procedimiento establecido en los mismos"),
         f"{c('CE', 'Artículo 147', 'requerirá, en todo caso, la aprobación por las Cortes Generales, mediante ley orgánica')}",
         "**En todo caso**, aprobación de las Cortes por **ley orgánica**: no basta la aprobación del Parlamento autonómico."))}

{unidad("3.2 Estatutos de la vía del art. 151: además, referéndum (art. 152.2)",
  lit("CE", "Artículo 152", ["con referéndum entre los electores inscritos en los censos correspondientes"], solo=[4]),
  fichab("Reforma de los Estatutos aprobados por el art. 151",
         "La Comunidad Autónoma, las Cortes y los electores de la Comunidad",
         c("CE", "Artículo 152", "solamente podrán ser modificados mediante los procedimientos en ellos establecidos"),
         "Referéndum entre los electores inscritos en los censos correspondientes",
         "El **referéndum** de reforma es obligatorio en los Estatutos **del art. 151**, no en todos."))}
""", 2)

T.ap("s9", "II.4 Otras materias que la Constitución remite a los Estatutos (arts. 3.2 y 4.2; disposición adicional primera)", f"""
Además del contenido obligatorio del art. 147.2, la Constitución deja a los Estatutos otras decisiones. Estas son las que se preguntan con más frecuencia.

{unidad("4.1 Lenguas cooficiales (art. 3.2)",
  lit("CE", "Artículo 3", ["de acuerdo con sus Estatutos"], solo=[2]),
  fichab("Oficialidad de las demás lenguas españolas", "Las Comunidades Autónomas, a través de sus Estatutos",
         f"{c('CE', 'Artículo 3', 'serán también oficiales en las respectivas Comunidades Autónomas')}", "—",
         "La oficialidad de las demás lenguas es **territorial** («en las respectivas Comunidades») y la fija el **Estatuto**."))}

{unidad("4.2 Banderas y enseñas propias (art. 4.2)",
  lit("CE", "Artículo 4", ["junto a la bandera de España"], solo=[2]),
  fichab("Símbolos de las Comunidades Autónomas", "Los Estatutos",
         f"{c('CE', 'Artículo 4', 'Los Estatutos podrán reconocer banderas y enseñas propias')}", "—",
         "Es potestativo («**podrán**»), y las banderas propias se usan **junto a** la de España en edificios públicos y actos oficiales."))}

{unidad("4.3 Derechos históricos de los territorios forales (disposición adicional primera)",
  lit("CE", "primera", ["ampara y respeta los derechos históricos de los territorios forales", "en el marco de la Constitución y de los Estatutos de Autonomía"]),
  fichab("Garantía de los regímenes forales", "Los territorios forales",
         "La Constitución ampara y respeta sus derechos históricos; la actualización general del régimen foral se hace en el marco de la Constitución y de los Estatutos", "—",
         "La actualización es «**en su caso**» y siempre **en el marco de la Constitución y de los Estatutos**."))}

{resumen([
  "El Estatuto es la **norma institucional básica** de cada Comunidad, aprobada por **ley orgánica** (81.1 y 147.1) y con **cuatro** contenidos obligatorios (147.2).",
  "Vía general: lo elabora una asamblea de **diputados provinciales y parlamentarios** y se tramita **como ley** (146). Vía del 151: **Asamblea de Parlamentarios**, Comisión Constitucional del Congreso (**dos meses**), **referéndum** y **ratificación** de ambas Cámaras.",
  "Reforma: procedimiento del Estatuto + **ley orgánica** de las Cortes (147.3); en los del 151, además, **referéndum** (152.2).",
  "Los Estatutos también deciden la **cooficialidad** de las lenguas (3.2) y las **banderas** propias (4.2)."],
  "Siguiente: III. ¿Cómo se organizan y con qué medios?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Cómo se organizan y con qué medios? Organización política y administrativa (arts. 152, 154 y 156 a 158)", donde(
  "Tercera pregunta. La Constitución dibuja las **instituciones** de las Comunidades del art. 151 (Asamblea, Consejo de Gobierno, Presidente y Tribunal Superior de Justicia), sitúa en su territorio a un **Delegado del Gobierno** y les da **autonomía financiera**.",
  ["1 Asamblea Legislativa, Consejo de Gobierno y Presidente (art. 152.1)", "2 Tribunal Superior de Justicia y circunscripciones territoriales (art. 152.1 y 3)", "3 El Delegado del Gobierno (art. 154)", "4 Autonomía financiera y recursos (arts. 156 a 158)"]))

T.ap("s10", "III.1 Asamblea Legislativa, Consejo de Gobierno y Presidente (art. 152.1)", f"""
{unidad("1.1 La organización institucional autonómica (art. 152.1, párrafo primero)",
  lit("CE", "Artículo 152", ["una Asamblea Legislativa, elegida por sufragio universal", "representación de las diversas zonas del territorio", "un Consejo de Gobierno con funciones ejecutivas y administrativas", "elegido por la Asamblea, de entre sus miembros, y nombrado por el Rey", "la suprema representación de la respectiva Comunidad y la ordinaria del Estado en aquélla", "políticamente responsables ante la Asamblea"], solo=[1]),
  fichab("Instituciones de autogobierno de los Estatutos aprobados por el art. 151",
         ["**Asamblea Legislativa**", "**Consejo de Gobierno**", "**Presidente**"],
         [f"Asamblea: {c('CE', 'Artículo 152', 'elegida por sufragio universal, con arreglo a un sistema de representación proporcional')}", "Consejo de Gobierno: funciones ejecutivas y administrativas", f"Presidente: {c('CE', 'Artículo 152', 'elegido por la Asamblea, de entre sus miembros, y nombrado por el Rey')}; dirige el Consejo de Gobierno y tiene la suprema representación de la Comunidad y la ordinaria del Estado en ella"],
         "—",
         f"El Presidente lo **elige la Asamblea** de entre sus miembros y lo **nombra el Rey**. Ostenta la representación **ordinaria del Estado** en la Comunidad. {c('CE', 'Artículo 152', 'El Presidente y los miembros del Consejo de Gobierno serán políticamente responsables ante la Asamblea')}."))}
""", 2)

T.ap("s11", "III.2 Tribunal Superior de Justicia y circunscripciones territoriales (art. 152.1 y 3)", f"""
{unidad("2.1 El Tribunal Superior de Justicia (art. 152.1, párrafos segundo y tercero)",
  lit("CE", "Artículo 152", ["Un Tribunal Superior de Justicia, sin perjuicio de la jurisdicción que corresponde al Tribunal Supremo", "dentro de la unidad e independencia de éste", "se agotarán ante órganos judiciales radicados en el mismo territorio"], solo=[2, 3]),
  fichab("Culminación de la organización judicial en la Comunidad Autónoma",
         "El Tribunal Superior de Justicia; los Estatutos (participación en las demarcaciones judiciales)",
         ["Culmina la organización judicial en el territorio de la Comunidad, sin perjuicio del Tribunal Supremo", "Las sucesivas instancias se agotan ante órganos del mismo territorio, sin perjuicio del art. 123"],
         "—",
         "El poder judicial sigue siendo **único**: todo se hace «de conformidad con lo previsto en la **ley orgánica del poder judicial** y dentro de la **unidad e independencia** de éste» (tema I.7)."))}

{unidad("2.2 Circunscripciones territoriales propias (art. 152.3)",
  lit("CE", "Artículo 152", ["agrupación de municipios limítrofes", "plena personalidad jurídica"], solo=[5]),
  fichab("Entidades territoriales que pueden crear los Estatutos", "Los Estatutos",
         c("CE", "Artículo 152", "Mediante la agrupación de municipios limítrofes, los Estatutos podrán establecer circunscripciones territoriales propias"),
         "—", "Agrupación de municipios **limítrofes**, con **plena personalidad jurídica**."))}
""", 2)

T.ap("s12", "III.3 El Delegado del Gobierno (art. 154)", f"""
{unidad("3.1 La Administración del Estado en la Comunidad Autónoma (art. 154)",
  lit("CE", "Artículo 154", ["Un Delegado nombrado por el Gobierno", "dirigirá la Administración del Estado", "cuando proceda"]),
  fichab("Órgano que dirige la Administración del Estado en el territorio de cada Comunidad",
         c("CE", "Artículo 154", "Un Delegado nombrado por el Gobierno"),
         f"{c('CE', 'Artículo 154', 'dirigirá la Administración del Estado en el territorio de la Comunidad Autónoma')} y la coordinará, cuando proceda, con la administración de la Comunidad",
         "—",
         "Lo nombra el **Gobierno** (no el Rey ni el Presidente autonómico). La coordinación con la administración autonómica es «**cuando proceda**». Su régimen en la Ley 40/2015: tema I.8."))}
""", 2)

T.ap("s13", "III.4 Autonomía financiera y recursos (arts. 156 a 158)", f"""
{unidad("4.1 Autonomía financiera y colaboración tributaria (art. 156)",
  lit("CE", "Artículo 156", ["autonomía financiera para el desarrollo y ejecución de sus competencias", "coordinación con la Hacienda estatal y de solidaridad entre todos los españoles", "como delegados o colaboradores del Estado"]),
  fichab("Autonomía financiera de las Comunidades Autónomas", "Las Comunidades Autónomas",
         ["Para el desarrollo y ejecución de sus competencias", "Pueden recaudar, gestionar y liquidar recursos tributarios del Estado como delegados o colaboradores, de acuerdo con las leyes y los Estatutos (156.2)"],
         "—",
         "Dos principios: **coordinación con la Hacienda estatal** y **solidaridad entre todos los españoles**."))}

{unidad("4.2 Los recursos de las Comunidades Autónomas (art. 157)",
  lit("CE", "Artículo 157", ["Impuestos cedidos total o parcialmente por el Estado", "Sus propios impuestos, tasas y contribuciones especiales", "Fondo de Compensación interterritorial", "El producto de las operaciones de crédito", "sobre bienes situados fuera de su territorio", "Mediante ley orgánica"]),
  fichab("Recursos financieros autonómicos y sus límites", "Las Comunidades Autónomas; el Estado regula por ley orgánica",
         ["::Recursos (157.1):", "Impuestos cedidos, recargos y participaciones en ingresos del Estado", "Impuestos, tasas y contribuciones especiales propios", "Transferencias del Fondo de Compensación interterritorial y asignaciones de los Presupuestos Generales del Estado", "Rendimientos del patrimonio e ingresos de derecho privado", "Operaciones de crédito"],
         "Ley orgánica para regular el ejercicio de estas competencias financieras (157.3)",
         "Límites del 157.2: nada de medidas tributarias sobre bienes **fuera de su territorio** ni que obstaculicen la **libre circulación** de mercancías o servicios."))}

{unidad("4.3 Asignaciones del Estado y Fondo de Compensación (art. 158)",
  lit("CE", "Artículo 158", ["un nivel mínimo en la prestación de los servicios públicos fundamentales", "un Fondo de Compensación con destino a gastos de inversión", "distribuidos por las Cortes Generales"]),
  fichab("Instrumentos de nivelación y solidaridad", "El Estado (Presupuestos Generales); las Cortes Generales (distribución del Fondo)",
         ["Asignación en los Presupuestos en función de los servicios asumidos y de la garantía de un nivel mínimo de los servicios públicos fundamentales (158.1)", "Fondo de Compensación para corregir desequilibrios interterritoriales y hacer efectivo el principio de solidaridad (158.2)"],
         "—",
         "El Fondo de Compensación va a **gastos de inversión** y lo distribuyen **las Cortes Generales** entre Comunidades Autónomas y provincias, en su caso."))}

{unidad("4.4 El Fondo de Suficiencia Global en la Ley 22/2009 (preámbulo)",
  "*El preámbulo de una ley explica su contenido; no es parte de su articulado. Se copia porque en él figura literalmente la expresión que preguntó el examen de 2025.*",
  lit("L22_2009", "preambulo", ["Fondo de Suficiencia Global opera como recurso de cierre del sistema"], solo=[24], titulo="Preámbulo de la Ley 22/2009, de 18 de diciembre (sistema de financiación de las Comunidades Autónomas de régimen común)"),
  fichab("Recurso de cierre del sistema de financiación de las Comunidades Autónomas de régimen común",
         "Las Comunidades Autónomas de régimen común y Ciudades con Estatuto de Autonomía",
         "Asegura que las necesidades globales de financiación de cada Comunidad en el año base se cubren con su capacidad tributaria, la transferencia del Fondo de Garantía y el propio Fondo de Suficiencia",
         "—",
         "Cayó en 2025 (→ Cierre 1): el recurso de cierre es el **Fondo de Suficiencia Global**, no el Fondo de Garantía de Servicios Públicos Fundamentales."))}

{resumen([
  "Comunidades del 151: **Asamblea Legislativa** (sufragio universal, representación proporcional), **Consejo de Gobierno** y **Presidente** elegido por la Asamblea de entre sus miembros y **nombrado por el Rey**; responsabilidad política **ante la Asamblea** (152.1).",
  "El **Tribunal Superior de Justicia** culmina la organización judicial en la Comunidad, sin perjuicio del Tribunal Supremo; los Estatutos pueden crear **circunscripciones** con municipios limítrofes (152.1 y 3).",
  "Un **Delegado nombrado por el Gobierno** dirige la Administración del Estado en la Comunidad (154).",
  "**Autonomía financiera** con coordinación y solidaridad (156); recursos del 157.1; **Fondo de Compensación** para **gastos de inversión**, distribuido por las **Cortes** (158.2)."],
  "Siguiente: IV. ¿Quién hace qué? La delimitación de competencias")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Quién hace qué? La delimitación de competencias (arts. 148, 149 y 150)", donde(
  "Cuarta pregunta. La Constitución no reparte las competencias directamente: el art. 148 dice qué materias **pueden asumir** las Comunidades, el art. 149 cuáles son **exclusivas del Estado**, los **Estatutos** concretan las asumidas por cada Comunidad y el art. 150 permite **modificar** el reparto por ley estatal.",
  ["1 Lo que las Comunidades pueden asumir (art. 148)", "2 Las competencias exclusivas del Estado (art. 149.1)", "3 Cultura y cláusulas de cierre: residual, prevalencia y supletoriedad (art. 149.2 y 3)", "4 Las leyes del art. 150: marco, transferencia o delegación y armonización", "5 Cuadro de las materias que se confunden"]))

T.ap("s14", "IV.1 Lo que las Comunidades pueden asumir (art. 148)", f"""
{unidad("1.1 La lista del art. 148.1",
  lit("CE", "Artículo 148", ["podrán asumir competencias", "Ordenación del territorio, urbanismo y vivienda", "La pesca en aguas interiores, el marisqueo y la acuicultura, la caza y la pesca fluvial", "Los puertos de refugio, los puertos y aeropuertos deportivos", "Asistencia social", "Sanidad e higiene"], solo=list(range(1, 24))),
  fichab("Materias en las que las Comunidades Autónomas pueden asumir competencias",
         "Las Comunidades Autónomas, a través de sus Estatutos (art. 147.2 d)",
         "Veintidós materias. Las que más se preguntan: organización de sus instituciones; ordenación del territorio, urbanismo y vivienda; puertos y aeropuertos deportivos y sin actividades comerciales; pesca en aguas interiores, marisqueo, acuicultura, caza y pesca fluvial; asistencia social; sanidad e higiene",
         "—",
         "Cayó en 2025 (→ Cierre 1): ordenación del territorio, asistencia social y pesca fluvial son del **148** (pueden asumirlas las Comunidades). El verbo es «**podrán asumir**»: la asunción la hace el Estatuto."))}

{unidad("1.2 Ampliación pasados cinco años (art. 148.2)",
  lit("CE", "Artículo 148", ["Transcurridos cinco años", "mediante la reforma de sus Estatutos", "dentro del marco establecido en el artículo 149"], solo=[24]),
  fichab("Ampliación de competencias de las Comunidades Autónomas",
         "Las Comunidades Autónomas",
         c("CE", "Artículo 148", "mediante la reforma de sus Estatutos"),
         "**Cinco años**",
         "Dos requisitos: **cinco años** y **reforma del Estatuto**; límite: el **art. 149**. Las Comunidades que accedieron por el **151.1** no necesitaron esperar ese plazo (→ I.5.1)."))}
""", 2)

T.ap("s15", "IV.2 Las competencias exclusivas del Estado (art. 149.1)", f"""
{unidad("2.1 La lista del art. 149.1",
  lit("CE", "Artículo 149", ["El Estado tiene competencia exclusiva", "Relaciones internacionales", "Legislación laboral; sin perjuicio de su ejecución por los órganos de las Comunidades Autónomas", "Hacienda general y Deuda del Estado", "Pesca marítima", "Marina mercante y abanderamiento de buques", "Obras públicas de interés general", "Autorización para la convocatoria de consultas populares por vía de referéndum"], solo=list(range(1, 34))),
  fichab("Materias reservadas al Estado",
         c("CE", "Artículo 149", "El Estado"),
         ["::Treinta y dos materias, con tres formas de reserva:", "Materia entera (p. ej., relaciones internacionales; defensa y Fuerzas Armadas; Hacienda general y Deuda del Estado; marina mercante)", "Solo la legislación, con ejecución autonómica (p. ej., legislación laboral; legislación básica de Seguridad Social)", "Solo las bases o la legislación básica (p. ej., bases del régimen jurídico de las Administraciones públicas; legislación básica de medio ambiente)"],
         "—",
         "Pares que se confunden: **pesca marítima** (149.1.19.ª) frente a **pesca fluvial** y en aguas interiores (148.1.11.ª); puertos y aeropuertos **de interés general** (149.1.20.ª) frente a **deportivos** (148.1.6.ª); obras públicas **de interés general** (149.1.24.ª) frente a las **de interés de la Comunidad** (148.1.4.ª)."))}
""", 2)

T.ap("s16", "IV.3 Cultura y cláusulas de cierre: residual, prevalencia y supletoriedad (art. 149.2 y 3)", f"""
{unidad("3.1 La cultura, deber y atribución esencial del Estado (art. 149.2)",
  lit("CE", "Artículo 149", ["el servicio de la cultura como deber y atribución esencial"], solo=[34]),
  fichab("El servicio de la cultura, deber y atribución esencial del Estado", "El Estado, sin perjuicio de las competencias de las Comunidades",
         "Considera la cultura deber y atribución esencial y facilita la comunicación cultural entre Comunidades, de acuerdo con ellas", "—",
         "La comunicación cultural entre Comunidades la facilita el Estado «**de acuerdo con ellas**»."))}

{unidad("3.2 Cláusula residual, prevalencia y supletoriedad (art. 149.3)",
  lit("CE", "Artículo 149", ["podrán corresponder a las Comunidades Autónomas, en virtud de sus respectivos Estatutos", "corresponderá al Estado", "prevalecerán, en caso de conflicto", "supletorio"], solo=[35]),
  fichab("Reglas de cierre del reparto de competencias",
         "El Estado y las Comunidades Autónomas (según sus Estatutos)",
         ["Materias no atribuidas expresamente al Estado: **pueden** corresponder a las Comunidades si las asumen sus Estatutos", "Materias no asumidas por los Estatutos: corresponden al **Estado**", "En caso de conflicto, prevalecen las normas del Estado en todo lo no atribuido a la exclusiva competencia de las Comunidades", "El derecho estatal es, en todo caso, **supletorio** del autonómico"],
         "—",
         "Es aquí donde los **Estatutos** delimitan las competencias: lo no asumido por el Estatuto **vuelve al Estado**. Prevalencia del derecho estatal **salvo** en lo exclusivo de las Comunidades; supletoriedad «**en todo caso**»."))}
""", 2)

T.ap("s17", "IV.4 Las leyes del art. 150: marco, transferencia o delegación y armonización", f"""
El art. 150 permite a las Cortes **ampliar** (apartados 1 y 2) o **armonizar** (apartado 3) las competencias autonómicas sin reformar los Estatutos. Como tipos de ley se estudian también en el tema IV.2.

{unidad("4.1 Leyes marco (art. 150.1)",
  lit("CE", "Artículo 150", ["la facultad de dictar, para sí mismas, normas legislativas", "la modalidad del control de las Cortes Generales"], solo=[1]),
  fichab("Atribución de facultades legislativas en materias estatales",
         f"{c('CE', 'Artículo 150', 'Las Cortes Generales')} → todas o alguna de las Comunidades Autónomas",
         f"Dentro de {c('CE', 'Artículo 150', 'los principios, bases y directrices fijados por una ley estatal')}",
         "—",
         "Se atribuye la facultad de dictar **normas legislativas**; cada ley marco fija el **control de las Cortes**, sin perjuicio del de los Tribunales."))}

{unidad("4.2 Leyes de transferencia o delegación (art. 150.2)",
  lit("CE", "Artículo 150", ["mediante ley orgánica", "susceptibles de transferencia o delegación", "las formas de control que se reserve el Estado"], solo=[2]),
  fichab("Transferencia o delegación de facultades estatales",
         f"{c('CE', 'Artículo 150', 'El Estado')} → Comunidades Autónomas",
         "Solo facultades que por su propia naturaleza sean susceptibles de transferencia o delegación; con medios financieros y formas de control",
         "**Ley orgánica**",
         "El control de las funciones **delegadas** lo ejerce el **Gobierno, previo dictamen del Consejo de Estado** (153 b → V.1.1)."))}

{unidad("4.3 Leyes de armonización (art. 150.3)",
  lit("CE", "Artículo 150", ["aun en el caso de materias atribuidas a la competencia de éstas", "por mayoría absoluta de cada Cámara"], solo=[3]),
  fichab("Armonización de las disposiciones autonómicas", f"{c('CE', 'Artículo 150', 'El Estado')}; aprecian la necesidad las Cortes Generales",
         f"Cuando {c('CE', 'Artículo 150', 'así lo exija el interés general')}, incluso en materias de competencia autonómica",
         "Mayoría absoluta **de cada Cámara**",
         "Es la única ley del 150 que entra en materias **de las Comunidades**."))}
""", 2)

T.ap("s18", "IV.5 Cuadro de las materias que se confunden (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Materia | Art. 148.1 (pueden asumir las Comunidades) | Art. 149.1 (exclusiva del Estado) |
|---|---|---|
| Pesca | Pesca en aguas interiores, marisqueo, acuicultura, caza y pesca fluvial (11.ª) | Pesca marítima, sin perjuicio de la ordenación del sector (19.ª) |
| Puertos y aeropuertos | De refugio, deportivos y sin actividades comerciales (6.ª) | De interés general (20.ª) |
| Obras públicas | De interés de la Comunidad en su territorio (4.ª) | De interés general o que afecten a más de una Comunidad (24.ª) |
| Ferrocarriles y transportes | Itinerario íntegro en la Comunidad (5.ª) | Por el territorio de más de una Comunidad (21.ª) |
| Aguas | Aprovechamientos hidráulicos de interés de la Comunidad (10.ª) | Aguas que discurran por más de una Comunidad (22.ª) |
| Medio ambiente | Gestión en materia de protección (9.ª) | Legislación básica (23.ª) |
| Sanidad | Sanidad e higiene (21.ª) | Sanidad exterior; bases y coordinación general; productos farmacéuticos (16.ª) |
| Montes | Montes y aprovechamientos forestales (8.ª) | Legislación básica sobre montes, aprovechamientos forestales y vías pecuarias (23.ª) |
| Museos y bibliotecas | De interés para la Comunidad (15.ª) | De titularidad estatal, sin perjuicio de su gestión autonómica (28.ª) |
| Policía | Vigilancia de sus edificios; coordinación de policías locales (22.ª) | Seguridad pública, sin perjuicio de policías autonómicas (29.ª) |

{resumen([
  "Art. 148.1: lo que las Comunidades **pueden asumir**; pasados **cinco años**, y **reformando el Estatuto**, pueden ampliar dentro del marco del **149** (148.2).",
  "Art. 149.1: **32** materias exclusivas del Estado (materia entera, solo legislación o solo bases).",
  "Art. 149.3: lo no atribuido al Estado puede ser autonómico **si lo asume el Estatuto**; lo no asumido es del **Estado**; prevalencia estatal salvo en lo exclusivo autonómico; derecho estatal **supletorio en todo caso**.",
  "Art. 150: ley **marco**, ley **orgánica** de transferencia o delegación y ley de **armonización** (mayoría absoluta de **cada Cámara**)."],
  "Siguiente: V. ¿Quién controla a las Comunidades Autónomas?")}
""", 2)

# =============================================================================
T.ap("bV", "V. ¿Quién controla a las Comunidades Autónomas? (arts. 153 y 155)", donde(
  "Quinta pregunta. La autonomía no es soberanía: la Constitución reparte el **control** de la actividad autonómica entre cuatro órganos según **qué** se controla, y prevé una medida extraordinaria de **coerción** del Gobierno con el Senado.",
  ["1 Los cuatro controles del art. 153", "2 La coerción estatal (art. 155)"]))

T.ap("s19", "V.1 Los cuatro controles del art. 153", f"""
{unidad("1.1 Quién controla qué (art. 153)",
  lit("CE", "Artículo 153", ["Por el Tribunal Constitucional", "Por el Gobierno, previo dictamen del Consejo de Estado", "Por la jurisdicción contencioso-administrativa", "Por el Tribunal de Cuentas"]),
  fichab("Control de la actividad de los órganos de las Comunidades Autónomas",
         ["Tribunal Constitucional", "Gobierno (con dictamen del Consejo de Estado)", "Jurisdicción contencioso-administrativa", "Tribunal de Cuentas"],
         ["a) TC: constitucionalidad de sus **disposiciones normativas con fuerza de ley**", "b) Gobierno, previo dictamen del Consejo de Estado: ejercicio de **funciones delegadas** del art. 150.2", "c) Contencioso-administrativo: la **administración autónoma** y sus **normas reglamentarias**", "d) Tribunal de Cuentas: el **económico y presupuestario**"],
         "—",
         "Cayó dos veces en 2025 (→ Cierre 1): funciones delegadas del 150.2 → **Gobierno, previo dictamen del Consejo de Estado**; administración autonómica y reglamentos → **contencioso-administrativo**. La impugnación del art. 161.2 ante el TC se estudia en el tema I.3."))}

{unidad("1.2 El dictamen del Consejo de Estado (LO 3/1980, art. 22)",
  lit("LO3_1980", "aveintidos", ["La Comisión Permanente del Consejo de Estado deberá ser consultada", "Control del ejercicio de funciones delegadas por el Estado a las Comunidades Autónomas", "con carácter previo a la interposición del recurso"], solo=[1, 5, 6, 7]),
  fichab("Consultas preceptivas a la Comisión Permanente sobre las Comunidades Autónomas",
         "La **Comisión Permanente** del Consejo de Estado",
         ["Anteproyectos de ley orgánica de transferencias o delegación (art. 150.2 CE)", "Control del ejercicio de funciones delegadas (art. 153 b CE)", "Impugnación ante el TC de disposiciones y resoluciones autonómicas, antes del recurso"],
         "—",
         "El dictamen del art. 153 b) lo emite la **Comisión Permanente** (no el Pleno). Consejo de Estado: tema I.6."))}
""", 2)

T.ap("s20", "V.2 La coerción estatal (art. 155)", f"""
{unidad("2.1 Medidas para el cumplimiento forzoso (art. 155)",
  lit("CE", "Artículo 155", ["no cumpliere las obligaciones que la Constitución u otras leyes le impongan", "atente gravemente al interés general de España", "previo requerimiento al Presidente de la Comunidad Autónoma", "con la aprobación por mayoría absoluta del Senado", "dar instrucciones a todas las autoridades de las Comunidades Autónomas"]),
  fichab("Coerción estatal sobre una Comunidad Autónoma",
         [f"{c('CE', 'Artículo 155', 'el Gobierno')} adopta las medidas", "El **Presidente de la Comunidad** recibe el requerimiento", "El **Senado** las aprueba"],
         ["::Supuestos:", "Incumplimiento de las obligaciones que la Constitución u otras leyes le impongan", "Actuación que atente gravemente al interés general de España", "Pasos: requerimiento al Presidente de la Comunidad → si no es atendido, aprobación del Senado → medidas necesarias; para ejecutarlas, instrucciones a todas las autoridades autonómicas (155.2)"],
         "**Mayoría absoluta del Senado**",
         "Interviene el **Senado** (no el Congreso) por **mayoría absoluta**; el requerimiento previo va al **Presidente de la Comunidad Autónoma**, y solo si no es atendido."))}

{resumen([
  "Art. 153: **TC** (normas con fuerza de ley), **Gobierno previo dictamen del Consejo de Estado** (funciones delegadas del 150.2), **contencioso-administrativo** (administración autonómica y reglamentos) y **Tribunal de Cuentas** (económico y presupuestario).",
  "El dictamen sobre funciones delegadas lo emite la **Comisión Permanente** del Consejo de Estado (LO 3/1980, art. 22).",
  "Art. 155: incumplimiento o atentado grave al interés general → **requerimiento al Presidente** autonómico → **mayoría absoluta del Senado** → medidas del **Gobierno** e instrucciones a todas las autoridades autonómicas."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_L13 = examen("L", 13, {
  "a": f"Es materia del art. 148.1.3.ª, que pueden asumir las Comunidades: {c('CE', 'Artículo 148', 'Ordenación del territorio, urbanismo y vivienda')}.",
  "b": f"Es materia del art. 148.1.20.ª: {c('CE', 'Artículo 148', 'Asistencia social')}.",
  "c": f"Literal del art. 149.1.20.ª: {c('CE', 'Artículo 149', 'Marina mercante y abanderamiento de buques')}.",
  "d": f"Es materia del art. 148.1.11.ª: {c('CE', 'Artículo 148', 'la caza y la pesca fluvial')}. Lo exclusivo del Estado es la **pesca marítima** (149.1.19.ª)."},
  [("Marina mercante", "CE", "Artículo 149", "Marina mercante y abanderamiento de buques")])
EX_L14 = examen("L", 14, {
  "a": f"Literal del art. 145.1: {c('CE', 'Artículo 145', 'En ningún caso se admitirá la federación de Comunidades Autónomas')}.",
  "b": f"La prohibición es absoluta ({c('CE', 'Artículo 145', 'En ningún caso')}): no la levanta una ley orgánica.",
  "c": "Ningún acuerdo de las Asambleas Legislativas puede permitirla; lo que admite el art. 145.2 son **convenios** y **acuerdos de cooperación**, no la federación.",
  "d": f"La Constitución sí la regula, y para prohibirla (art. 145.1); a los Estatutos solo les remite los **convenios** entre Comunidades: {c('CE', 'Artículo 145', 'Los Estatutos podrán prever los supuestos, requisitos y términos en que las Comunidades Autónomas podrán celebrar convenios entre sí')}."},
  [("prohíbe", "CE", "Artículo 145", "En ningún caso se admitirá la federación de Comunidades Autónomas")])
EX_X23 = examen("X", 23, {
  "a": f"El art. 139 no habla de las Comunidades, sino de los españoles. Lo que la Constitución dice de los Estatutos es que sus diferencias {c('CE', 'Artículo 138', 'no podrán implicar, en ningún caso, privilegios económicos o sociales')} (art. 138.2).",
  "b": f"Literal del art. 139.1: {c('CE', 'Artículo 139', 'Todos los españoles tienen los mismos derechos y obligaciones en cualquier parte del territorio del Estado')}.",
  "c": f"La autonomía es {c('CE', 'Artículo 137', 'para la gestión de sus respectivos intereses')} (art. 137) y se basa en la {c('CE', 'Artículo 2', 'indisoluble unidad de la Nación española')} (art. 2); no hay separación ni autonomía «total».",
  "d": f"La Constitución se fundamenta en la {c('CE', 'Artículo 2', 'indisoluble unidad de la Nación española, patria común e indivisible de todos los españoles')}: no prevé secesión alguna."},
  [("derechos y obligaciones", "CE", "Artículo 139", "Todos los españoles tienen los mismos derechos y obligaciones"),
   ("en cualquier parte del territorio", "CE", "Artículo 139", "en cualquier parte del territorio del Estado")])
EX_X24 = examen("X", 24, {
  "a": f"El Tribunal de Cuentas ejerce el control {c('CE', 'Artículo 153', 'el económico y presupuestario')} (art. 153 d).",
  "b": f"El Tribunal Constitucional controla {c('CE', 'Artículo 153', 'la constitucionalidad de sus disposiciones normativas con fuerza de ley')} (art. 153 a).",
  "c": f"Literal del art. 153 b): {c('CE', 'Artículo 153', 'Por el Gobierno, previo dictamen del Consejo de Estado, el del ejercicio de funciones delegadas a que se refiere el apartado 2 del artículo 150')}.",
  "d": "El Senado no aparece en el art. 153; interviene en la coerción del art. 155 (aprobación por mayoría absoluta)."},
  [("previo dictamen del Consejo de Estado", "CE", "Artículo 153", "Por el Gobierno, previo dictamen del Consejo de Estado, el del ejercicio de funciones delegadas")])
EX_X65 = examen("X", 65, {
  "a": f"El Tribunal Constitucional controla solo {c('CE', 'Artículo 153', 'sus disposiciones normativas con fuerza de ley')} (art. 153 a), no los reglamentos ni la administración.",
  "b": f"El Gobierno controla, previo dictamen del Consejo de Estado, {c('CE', 'Artículo 153', 'el del ejercicio de funciones delegadas')} (art. 153 b).",
  "c": "Ningún Ministerio aparece en el art. 153 como órgano de control.",
  "d": f"Literal del art. 153 c): {c('CE', 'Artículo 153', 'Por la jurisdicción contencioso-administrativa, el de la administración autónoma y sus normas reglamentarias')}."},
  [("jurisdicción contencioso-administrativa", "CE", "Artículo 153", "Por la jurisdicción contencioso-administrativa, el de la administración autónoma y sus normas reglamentarias")])
POR_FSG = {
  "a": "El Fondo de Cohesión Sanitaria no es el fondo que el preámbulo de la Ley 22/2009 califica de recurso de cierre.",
  "b": "El «Fondo de Garantía Asistencial» no es el fondo que el preámbulo de la Ley 22/2009 califica de recurso de cierre.",
  "c": f"Literal del preámbulo de la Ley 22/2009: {c('L22_2009', 'preambulo', 'El Fondo de Suficiencia Global opera como recurso de cierre del sistema')}.",
  "d": f"El Fondo de Garantía es uno de los recursos que el de Suficiencia completa: las necesidades se cubren {c('L22_2009', 'preambulo', 'con su capacidad tributaria, la transferencia del Fondo de Garantía y el propio Fondo de Suficiencia')}."}
APOYO_FSG = [("Fondo de Suficiencia Global", "L22_2009", "preambulo", "El Fondo de Suficiencia Global opera como recurso de cierre del sistema")]
EX_L36 = examen("L", 36, POR_FSG, APOYO_FSG)
EX_P31 = examen("P", 31, POR_FSG, APOYO_FSG)

T.ap("s21", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **cuatro** preguntas de este tema (competencias exclusivas del Estado, federación y dos sobre el art. 153) y **tres** relacionadas (art. 139 y, dos veces, el Fondo de Suficiencia Global). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-L 2025, pregunta 13 · Competencias exclusivas del Estado (→ IV.2.1)", EX_L13,
  "### GACE-L 2025, pregunta 14 · Federación de Comunidades Autónomas (→ I.4.1)", EX_L14,
  "### GACE-L 2025 extraordinario, pregunta 24 · Control de las funciones delegadas (→ V.1.1)", EX_X24,
  "### GACE-L 2025 extraordinario, pregunta 65 · Control de la administración autonómica (→ V.1.1)", EX_X65,
  "### GACE-L 2025 extraordinario, pregunta 23 · Art. 139 (relacionada; → I.2.2)", EX_X23,
  "### GACE-L 2025, pregunta 36 · Fondo de Suficiencia Global (relacionada; → III.4.4)", EX_L36,
  "### GACE-P 2025, pregunta 31 · Fondo de Suficiencia Global (relacionada; → III.4.4)", EX_P31,
  "### Cómo se pregunta",
  "!> Las preguntas de competencias se construyen **mezclando las listas** de los arts. 148 y 149: la correcta sale de una y los distractores de la otra. Las del art. 153 cambian **el órgano** de control. Saber **quién controla qué** y **qué lista es cuál** resuelve casi todas.",
]))

T.ap("s22", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Comunidades Autónomas | Unidad, autonomía y solidaridad (2); municipios, provincias y Comunidades (137); solidaridad e igualdad (138 y 139); acceso (143, 144, 151.1) | **Federación prohibida** (145.1); art. 139: **mismos derechos y obligaciones** de los españoles |
| II. Estatutos | Norma institucional básica por **ley orgánica** (81.1 y 147); elaboración (146 y 151.2); reforma (147.3 y 152.2) | Reforma: **ley orgánica** en todo caso; referéndum en los del 151 |
| III. Organización | Asamblea, Consejo de Gobierno y Presidente; TSJ (152); Delegado del Gobierno (154); financiación (156 a 158) | Presidente **elegido por la Asamblea** y **nombrado por el Rey** |
| IV. Competencias | 148 (pueden asumir); 149.1 (exclusivas del Estado); 149.3 (cláusulas de cierre); 150 | **Marina mercante** y **pesca marítima**, del Estado; **pesca fluvial**, autonómica |
| V. Control | 153 (cuatro órganos); 155 (coerción) | Funciones delegadas → **Gobierno, previo dictamen del Consejo de Estado**; 155 → **mayoría absoluta del Senado** |

?> **Trampas frecuentes:** «la federación se permite por **ley orgánica**» (está **prohibida en todo caso**); «**dos tercios** de los municipios» en la vía del 151.1 (son **tres cuartas partes**; los dos tercios son del 143.2); «el Presidente autonómico lo **nombra el Presidente del Gobierno**» (lo nombra **el Rey**); «el 155 lo aprueba el **Congreso**» (es el **Senado**, por **mayoría absoluta**); «los reglamentos autonómicos los controla el **TC**» (es la **jurisdicción contencioso-administrativa**); «el derecho estatal es supletorio **solo** en materias concurrentes» (lo es «**en todo caso**»).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
Q = [
 ("CE", "Artículo 2", "Principios", "Según el artículo 2 de la Constitución, esta reconoce y garantiza el derecho a la autonomía de:",
  ["Las nacionalidades y regiones que la integran.", "Las provincias y los municipios que la integran.", "Los territorios forales y los insulares.", "Las Comunidades Autónomas que tengan Estatuto aprobado por ley orgánica."],
  "Art. 2 CE.", "reconoce y garantiza el derecho a la autonomía de las nacionalidades y regiones que la integran"),
 ("CE", "Artículo 137", "Principios", "Según el artículo 137 de la Constitución, el Estado se organiza territorialmente en:",
  ["Municipios, provincias y las Comunidades Autónomas que se constituyan.", "Municipios, comarcas y Comunidades Autónomas.", "Provincias y Comunidades Autónomas.", "Municipios, provincias, islas y Comunidades Autónomas."],
  "Art. 137 CE.", "en municipios, en provincias y en las Comunidades Autónomas que se constituyan"),
 ("CE", "Artículo 137", "Principios", "Según el artículo 137 de la Constitución, los municipios, las provincias y las Comunidades Autónomas gozan de autonomía:",
  ["Para la gestión de sus respectivos intereses.", "Para el ejercicio de la soberanía en su territorio.", "Para la gestión de los intereses generales del Estado.", "Para dictar leyes en todas las materias."],
  "Art. 137 CE.", "gozan de autonomía para la gestión de sus respectivos intereses"),
 ("CE", "Artículo 138", "Principios", "Según el artículo 138.1 de la Constitución, el Estado garantiza la realización efectiva del principio de solidaridad atendiendo en particular a:",
  ["Las circunstancias del hecho insular.", "Las circunstancias de los territorios forales.", "La población de cada Comunidad Autónoma.", "Las lenguas cooficiales."],
  "Art. 138.1 CE.", "atendiendo en particular a las circunstancias del hecho insular"),
 ("CE", "Artículo 138", "Principios", "Según el artículo 138.2 de la Constitución, las diferencias entre los Estatutos de las distintas Comunidades Autónomas no podrán implicar, en ningún caso:",
  ["Privilegios económicos o sociales.", "Diferencias en las competencias asumidas.", "Diferencias en la organización de sus instituciones.", "Diferencias en la denominación de sus instituciones."],
  "Art. 138.2 CE.", "no podrán implicar, en ningún caso, privilegios económicos o sociales"),
 ("CE", "Artículo 139", "Principios", "Según el artículo 139.2 de la Constitución, ninguna autoridad podrá adoptar medidas que directa o indirectamente obstaculicen:",
  ["La libertad de circulación y establecimiento de las personas y la libre circulación de bienes en todo el territorio español.", "La libre circulación de capitales entre Comunidades Autónomas.", "El ejercicio de las competencias del Estado.", "La libertad de empresa en el marco de la economía de mercado."],
  "Art. 139.2 CE.", "obstaculicen la libertad de circulación y establecimiento de las personas y la libre circulación de bienes en todo el territorio español"),
 ("CE", "Artículo 143", "Acceso a la autonomía", "Según el artículo 143.2 de la Constitución, la iniciativa del proceso autonómico corresponde a todas las Diputaciones interesadas o al órgano interinsular correspondiente y a:",
  ["Las dos terceras partes de los municipios cuya población represente, al menos, la mayoría del censo electoral de cada provincia o isla.", "Las tres cuartas partes de los municipios cuya población represente, al menos, la mayoría del censo electoral de cada provincia o isla.", "La mitad de los municipios cuya población represente, al menos, dos tercios del censo electoral de cada provincia o isla.", "La mayoría absoluta de los municipios de cada provincia o isla."],
  "Art. 143.2 CE. Las tres cuartas partes son de la vía del art. 151.1.", "a las dos terceras partes de los municipios cuya población represente, al menos, la mayoría del censo electoral de cada provincia o isla"),
 ("CE", "Artículo 143", "Acceso a la autonomía", "Según el artículo 143.2 de la Constitución, los requisitos de la iniciativa autonómica deberán ser cumplidos en el plazo de:",
  ["Seis meses desde el primer acuerdo adoptado al respecto por alguna de las Corporaciones locales interesadas.", "Tres meses desde el primer acuerdo adoptado al respecto por alguna de las Corporaciones locales interesadas.", "Un año desde la convocatoria del referéndum.", "Dos meses desde la remisión a la Comisión Constitucional del Congreso."],
  "Art. 143.2 CE.", "en el plazo de seis meses desde el primer acuerdo adoptado al respecto por alguna de las Corporaciones locales interesadas"),
 ("CE", "Artículo 143", "Acceso a la autonomía", "Según el artículo 143.3 de la Constitución, la iniciativa del proceso autonómico, en caso de no prosperar, solamente podrá reiterarse pasados:",
  ["Cinco años.", "Tres años.", "Dos años.", "Cuatro años."],
  "Art. 143.3 CE.", "solamente podrá reiterarse pasados cinco años"),
 ("CE", "Artículo 144", "Acceso a la autonomía", "Según el artículo 144 de la Constitución, las Cortes Generales podrán sustituir la iniciativa de las Corporaciones locales a que se refiere el artículo 143.2:",
  ["Mediante ley orgánica, por motivos de interés nacional.", "Mediante ley ordinaria, por motivos de urgencia.", "Mediante ley de armonización, por mayoría absoluta de cada Cámara.", "Mediante acuerdo del Senado, por mayoría absoluta."],
  "Art. 144 c) CE.", "Las Cortes Generales, mediante ley orgánica, podrán, por motivos de interés nacional"),
 ("CE", "Artículo 145", "Acceso a la autonomía", "Según el artículo 145.2 de la Constitución, los acuerdos de cooperación entre las Comunidades Autónomas distintos de los convenios para la gestión y prestación de servicios propios necesitarán:",
  ["La autorización de las Cortes Generales.", "La comunicación al Gobierno de la Nación.", "La aprobación por ley orgánica.", "El dictamen previo del Consejo de Estado."],
  "Art. 145.2 CE.", "En los demás supuestos, los acuerdos de cooperación entre las Comunidades Autónomas necesitarán la autorización de las Cortes Generales"),
 ("CE", "Artículo 151", "Acceso a la autonomía", "Según el artículo 151.1 de la Constitución, la iniciativa del proceso autonómico por esta vía debe ser ratificada mediante referéndum:",
  ["Por el voto afirmativo de la mayoría absoluta de los electores de cada provincia.", "Por la mayoría de los votos válidamente emitidos en el conjunto del territorio.", "Por el voto afirmativo de las dos terceras partes de los electores de cada provincia.", "Por la mayoría de los votos válidamente emitidos en la mayoría de las provincias."],
  "Art. 151.1 CE.", "ratificada mediante referéndum por el voto afirmativo de la mayoría absoluta de los electores de cada provincia"),
 ("CE", "quinta", "Acceso a la autonomía", "Según la disposición transitoria quinta de la Constitución, las ciudades de Ceuta y Melilla podrán constituirse en Comunidades Autónomas si así lo deciden sus Ayuntamientos por mayoría absoluta y así lo autorizan las Cortes Generales mediante:",
  ["Una ley orgánica, en los términos previstos en el artículo 144.", "Una ley ordinaria, en los términos previstos en el artículo 143.", "Una ley marco, en los términos previstos en el artículo 150.1.", "Un referéndum de ratificación, en los términos previstos en el artículo 151."],
  "Disposición transitoria quinta CE.", "mediante una ley orgánica, en los términos previstos en el artículo 144"),
 ("CE", "Artículo 147", "Estatutos", "Según el artículo 147.1 de la Constitución, dentro de los términos de la Constitución, los Estatutos serán:",
  ["La norma institucional básica de cada Comunidad Autónoma.", "La norma suprema de cada Comunidad Autónoma.", "Leyes ordinarias de cada Comunidad Autónoma.", "Reglamentos orgánicos de cada Comunidad Autónoma."],
  "Art. 147.1 CE.", "los Estatutos serán la norma institucional básica de cada Comunidad Autónoma"),
 ("CE", "Artículo 147", "Estatutos", "Según el artículo 147.2 de la Constitución, los Estatutos de autonomía deberán contener:",
  ["La delimitación de su territorio.", "El sistema de financiación de la Comunidad.", "La regulación de sus Corporaciones locales.", "El régimen de sus funcionarios."],
  "Art. 147.2 b) CE.", "La delimitación de su territorio"),
 ("CE", "Artículo 147", "Estatutos", "Según el artículo 147.3 de la Constitución, la reforma de los Estatutos requerirá, en todo caso, la aprobación por las Cortes Generales mediante:",
  ["Ley orgánica.", "Ley ordinaria.", "Ley de bases.", "Ley de armonización."],
  "Art. 147.3 CE.", "requerirá, en todo caso, la aprobación por las Cortes Generales, mediante ley orgánica"),
 ("CE", "Artículo 146", "Estatutos", "Según el artículo 146 de la Constitución, el proyecto de Estatuto será elaborado por una asamblea compuesta por:",
  ["Los miembros de la Diputación u órgano interinsular de las provincias afectadas y los Diputados y Senadores elegidos en ellas.", "Los Diputados y Senadores elegidos en las provincias afectadas, convocados por el Gobierno.", "Los Alcaldes de los municipios de las provincias afectadas.", "Los miembros de la Comisión Constitucional del Congreso y una delegación de las provincias afectadas."],
  "Art. 146 CE. La Asamblea solo de Diputados y Senadores es la del art. 151.2.", "por los miembros de la Diputación u órgano interinsular de las provincias afectadas y por los Diputados y Senadores elegidos en ellas"),
 ("CE", "Artículo 151", "Estatutos", "Según el artículo 151.2 de la Constitución, aprobado el proyecto de Estatuto por la Asamblea de Parlamentarios, se remitirá a la Comisión Constitucional del Congreso, que lo examinará dentro del plazo de:",
  ["Dos meses.", "Un mes.", "Tres meses.", "Seis meses."],
  "Art. 151.2.2.º CE.", "la cual, dentro del plazo de dos meses, lo examinará"),
 ("CE", "Artículo 152", "Estatutos", "Según el artículo 152.2 de la Constitución, los Estatutos aprobados por el procedimiento del artículo 151, una vez sancionados y promulgados, solamente podrán ser modificados mediante los procedimientos en ellos establecidos y:",
  ["Con referéndum entre los electores inscritos en los censos correspondientes.", "Con la aprobación del Senado por mayoría absoluta.", "Con el dictamen previo del Consejo de Estado.", "Con la aprobación de tres quintos de la Asamblea Legislativa."],
  "Art. 152.2 CE.", "con referéndum entre los electores inscritos en los censos correspondientes"),
 ("CE", "Artículo 4", "Estatutos", "Según el artículo 4.2 de la Constitución, las banderas y enseñas propias de las Comunidades Autónomas reconocidas en sus Estatutos se utilizarán:",
  ["Junto a la bandera de España en sus edificios públicos y en sus actos oficiales.", "En lugar de la bandera de España en sus edificios públicos.", "Solo en los actos oficiales de la Comunidad Autónoma.", "Previa autorización del Delegado del Gobierno."],
  "Art. 4.2 CE.", "Estas se utilizarán junto a la bandera de España en sus edificios públicos y en sus actos oficiales"),
 ("CE", "primera", "Estatutos", "Según la disposición adicional primera de la Constitución, la Constitución ampara y respeta:",
  ["Los derechos históricos de los territorios forales.", "Los privilegios económicos de los territorios insulares.", "Los regímenes provisionales de autonomía.", "Los derechos históricos de las provincias con entidad regional histórica."],
  "Disposición adicional primera CE.", "La Constitución ampara y respeta los derechos históricos de los territorios forales"),
 ("CE", "Artículo 152", "Organización", "Según el artículo 152.1 de la Constitución, el Presidente de la Comunidad Autónoma es:",
  ["Elegido por la Asamblea, de entre sus miembros, y nombrado por el Rey.", "Elegido por la Asamblea, de entre sus miembros, y nombrado por el Presidente del Gobierno.", "Elegido por sufragio universal directo y nombrado por el Rey.", "Elegido por el Consejo de Gobierno y nombrado por la Asamblea."],
  "Art. 152.1 CE.", "elegido por la Asamblea, de entre sus miembros, y nombrado por el Rey"),
 ("CE", "Artículo 152", "Organización", "Según el artículo 152.1 de la Constitución, al Presidente de la Comunidad Autónoma le corresponde:",
  ["La dirección del Consejo de Gobierno, la suprema representación de la respectiva Comunidad y la ordinaria del Estado en aquélla.", "La dirección del Consejo de Gobierno y la suprema representación del Estado en la Comunidad.", "La dirección de la Administración del Estado en la Comunidad.", "La presidencia de la Asamblea Legislativa y del Tribunal Superior de Justicia."],
  "Art. 152.1 CE. La dirección de la Administración del Estado en la Comunidad es del Delegado del Gobierno (art. 154).", "al que corresponde la dirección del Consejo de Gobierno, la suprema representación de la respectiva Comunidad y la ordinaria del Estado en aquélla"),
 ("CE", "Artículo 152", "Organización", "Según el artículo 152.1 de la Constitución, la organización judicial en el ámbito territorial de la Comunidad Autónoma culminará en:",
  ["Un Tribunal Superior de Justicia, sin perjuicio de la jurisdicción que corresponde al Tribunal Supremo.", "La Audiencia Nacional, sin perjuicio de la jurisdicción que corresponde al Tribunal Supremo.", "La Audiencia Provincial de la capital de la Comunidad.", "Un Consejo de Justicia de la Comunidad Autónoma."],
  "Art. 152.1 CE.", "Un Tribunal Superior de Justicia, sin perjuicio de la jurisdicción que corresponde al Tribunal Supremo, culminará la organización judicial"),
 ("CE", "Artículo 152", "Organización", "Según el artículo 152.3 de la Constitución, mediante la agrupación de municipios limítrofes, los Estatutos podrán establecer:",
  ["Circunscripciones territoriales propias, que gozarán de plena personalidad jurídica.", "Provincias propias, que gozarán de autonomía para la gestión de sus intereses.", "Mancomunidades, sin personalidad jurídica propia.", "Áreas metropolitanas, que dependerán del Consejo de Gobierno."],
  "Art. 152.3 CE.", "los Estatutos podrán establecer circunscripciones territoriales propias, que gozarán de plena personalidad jurídica"),
 ("CE", "Artículo 154", "Organización", "Según el artículo 154 de la Constitución, la Administración del Estado en el territorio de la Comunidad Autónoma la dirigirá:",
  ["Un Delegado nombrado por el Gobierno.", "Un Delegado nombrado por el Rey a propuesta del Presidente de la Comunidad.", "El Presidente de la Comunidad Autónoma, como representante ordinario del Estado.", "Un Subdelegado nombrado por el Ministro de Hacienda."],
  "Art. 154 CE.", "Un Delegado nombrado por el Gobierno dirigirá la Administración del Estado en el territorio de la Comunidad Autónoma"),
 ("CE", "Artículo 156", "Financiación", "Según el artículo 156.1 de la Constitución, las Comunidades Autónomas gozarán de autonomía financiera con arreglo a los principios de:",
  ["Coordinación con la Hacienda estatal y de solidaridad entre todos los españoles.", "Suficiencia y de equilibrio presupuestario.", "Estabilidad presupuestaria y de sostenibilidad financiera.", "Igualdad y de progresividad."],
  "Art. 156.1 CE.", "con arreglo a los principios de coordinación con la Hacienda estatal y de solidaridad entre todos los españoles"),
 ("CE", "Artículo 157", "Financiación", "Según el artículo 157.1 de la Constitución, los recursos de las Comunidades Autónomas estarán constituidos, entre otros, por:",
  ["El producto de las operaciones de crédito.", "Los aranceles aduaneros.", "Las cotizaciones a la Seguridad Social.", "Los impuestos sobre bienes situados fuera de su territorio."],
  "Art. 157.1 e) CE. Los tributos sobre bienes fuera de su territorio están prohibidos (157.2).", "El producto de las operaciones de crédito"),
 ("CE", "Artículo 158", "Financiación", "Según el artículo 158.2 de la Constitución, el Fondo de Compensación tendrá destino a gastos de inversión y sus recursos serán distribuidos por:",
  ["Las Cortes Generales.", "El Gobierno, previo dictamen del Consejo de Estado.", "El Consejo de Política Fiscal y Financiera.", "El Ministerio de Hacienda."],
  "Art. 158.2 CE.", "cuyos recursos serán distribuidos por las Cortes Generales"),
 ("CE", "Artículo 148", "Competencias", "¿En cuál de las siguientes materias pueden asumir competencias las Comunidades Autónomas según el artículo 148.1 de la Constitución?",
  ["Asistencia social.", "Marina mercante.", "Relaciones internacionales.", "Hacienda general y Deuda del Estado."],
  "Art. 148.1.20.ª CE. Las demás son exclusivas del Estado (149.1.20.ª, 3.ª y 14.ª).", "Asistencia social"),
 ("CE", "Artículo 148", "Competencias", "Según el artículo 148.2 de la Constitución, las Comunidades Autónomas podrán ampliar sucesivamente sus competencias dentro del marco establecido en el artículo 149:",
  ["Transcurridos cinco años, y mediante la reforma de sus Estatutos.", "Transcurridos tres años, y mediante ley de sus Asambleas.", "En cualquier momento, mediante ley orgánica de transferencia.", "Transcurridos cinco años, y mediante acuerdo de su Consejo de Gobierno."],
  "Art. 148.2 CE.", "Transcurridos cinco años, y mediante la reforma de sus Estatutos"),
 ("CE", "Artículo 149", "Competencias", "Según el artículo 149.1 de la Constitución, es competencia exclusiva del Estado:",
  ["La pesca marítima, sin perjuicio de las competencias que en la ordenación del sector se atribuyan a las Comunidades Autónomas.", "La pesca en aguas interiores.", "El marisqueo y la acuicultura.", "La pesca fluvial."],
  "Art. 149.1.19.ª CE. Las otras tres son del art. 148.1.11.ª.", "Pesca marítima, sin perjuicio de las competencias que en la ordenación del sector se atribuyan a las Comunidades Autónomas"),
 ("CE", "Artículo 149", "Competencias", "Según el artículo 149.1 de la Constitución, el Estado tiene competencia exclusiva sobre:",
  ["La autorización para la convocatoria de consultas populares por vía de referéndum.", "La promoción del deporte y de la adecuada utilización del ocio.", "Las ferias interiores.", "La artesanía."],
  "Art. 149.1.32.ª CE. Las otras tres son del art. 148.1.", "Autorización para la convocatoria de consultas populares por vía de referéndum"),
 ("CE", "Artículo 149", "Competencias", "Según el artículo 149.1.7.ª de la Constitución, la legislación laboral es competencia exclusiva del Estado:",
  ["Sin perjuicio de su ejecución por los órganos de las Comunidades Autónomas.", "Sin perjuicio de su desarrollo legislativo por las Comunidades Autónomas.", "Salvo en las Comunidades Autónomas que la hayan asumido en sus Estatutos.", "Incluida su ejecución, en todo caso."],
  "Art. 149.1.7.ª CE.", "Legislación laboral; sin perjuicio de su ejecución por los órganos de las Comunidades Autónomas"),
 ("CE", "Artículo 149", "Competencias", "Según el artículo 149.3 de la Constitución, la competencia sobre las materias que no se hayan asumido por los Estatutos de Autonomía corresponderá:",
  ["Al Estado.", "A las Comunidades Autónomas.", "A las Corporaciones locales.", "A quien determine el Tribunal Constitucional."],
  "Art. 149.3 CE.", "La competencia sobre las materias que no se hayan asumido por los Estatutos de Autonomía corresponderá al Estado"),
 ("CE", "Artículo 149", "Competencias", "Según el artículo 149.3 de la Constitución, el derecho estatal será, en todo caso:",
  ["Supletorio del derecho de las Comunidades Autónomas.", "Inaplicable en las materias asumidas por las Comunidades Autónomas.", "Derogatorio del derecho de las Comunidades Autónomas.", "De rango inferior al de los Estatutos de Autonomía."],
  "Art. 149.3 CE.", "El derecho estatal será, en todo caso, supletorio del derecho de las Comunidades Autónomas"),
 ("CE", "Artículo 150", "Competencias", "Según el artículo 150.1 de la Constitución, en cada ley marco se establecerá, sin perjuicio de la competencia de los Tribunales:",
  ["La modalidad del control de las Cortes Generales sobre estas normas legislativas de las Comunidades Autónomas.", "La modalidad del control del Gobierno, previo dictamen del Consejo de Estado.", "La transferencia de medios financieros.", "El plazo de vigencia de la atribución."],
  "Art. 150.1 CE.", "en cada ley marco se establecerá la modalidad del control de las Cortes Generales"),
 ("CE", "Artículo 150", "Competencias", "Según el artículo 150.3 de la Constitución, la apreciación de la necesidad de dictar leyes de armonización corresponde:",
  ["A las Cortes Generales, por mayoría absoluta de cada Cámara.", "Al Congreso de los Diputados, por mayoría absoluta.", "Al Senado, por mayoría de tres quintos.", "Al Gobierno, previo dictamen del Consejo de Estado."],
  "Art. 150.3 CE.", "Corresponde a las Cortes Generales, por mayoría absoluta de cada Cámara, la apreciación de esta necesidad"),
 ("CE", "Artículo 153", "Control", "Según el artículo 153 a) de la Constitución, el control de la constitucionalidad de las disposiciones normativas con fuerza de ley de las Comunidades Autónomas se ejercerá por:",
  ["El Tribunal Constitucional.", "La jurisdicción contencioso-administrativa.", "El Gobierno, previo dictamen del Consejo de Estado.", "El Tribunal Supremo."],
  "Art. 153 a) CE.", "Por el Tribunal Constitucional, el relativo a la constitucionalidad de sus disposiciones normativas con fuerza de ley"),
 ("CE", "Artículo 153", "Control", "Según el artículo 153 d) de la Constitución, el control económico y presupuestario de la actividad de los órganos de las Comunidades Autónomas se ejercerá por:",
  ["El Tribunal de Cuentas.", "La Intervención General de la Administración del Estado.", "El Gobierno, previo dictamen del Consejo de Estado.", "Las Cortes Generales."],
  "Art. 153 d) CE.", "Por el Tribunal de Cuentas, el económico y presupuestario"),
 ("LO3_1980", "aveintidos", "Control", "Según el artículo 22 de la Ley Orgánica 3/1980, del Consejo de Estado, el control del ejercicio de funciones delegadas por el Estado a las Comunidades Autónomas exige la consulta:",
  ["A la Comisión Permanente del Consejo de Estado.", "Al Pleno del Consejo de Estado.", "A la Comisión de Estudios del Consejo de Estado.", "Al órgano consultivo de la Comunidad Autónoma."],
  "Art. 22.Cinco LO 3/1980.", "Control del ejercicio de funciones delegadas por el Estado a las Comunidades Autónomas"),
 ("CE", "Artículo 155", "Control", "Según el artículo 155.1 de la Constitución, para adoptar las medidas necesarias para obligar a una Comunidad Autónoma al cumplimiento forzoso de sus obligaciones, el Gobierno necesita, si el requerimiento previo no es atendido:",
  ["La aprobación por mayoría absoluta del Senado.", "La aprobación por mayoría absoluta del Congreso de los Diputados.", "La autorización de las Cortes Generales en sesión conjunta.", "El dictamen previo del Tribunal Constitucional."],
  "Art. 155.1 CE.", "con la aprobación por mayoría absoluta del Senado"),
 ("CE", "Artículo 155", "Control", "Según el artículo 155.1 de la Constitución, antes de adoptar las medidas de cumplimiento forzoso, el Gobierno debe formular un requerimiento:",
  ["Al Presidente de la Comunidad Autónoma.", "A la Asamblea Legislativa de la Comunidad Autónoma.", "Al Delegado del Gobierno en la Comunidad Autónoma.", "Al Tribunal Superior de Justicia de la Comunidad Autónoma."],
  "Art. 155.1 CE.", "previo requerimiento al Presidente de la Comunidad Autónoma"),
 ("CE", "Artículo 155", "Control", "Según el artículo 155.2 de la Constitución, para la ejecución de las medidas previstas en su apartado 1, el Gobierno podrá dar instrucciones:",
  ["A todas las autoridades de las Comunidades Autónomas.", "Solo al Presidente de la Comunidad Autónoma.", "Solo a los Delegados del Gobierno.", "A las autoridades de la Comunidad, previa autorización del Congreso."],
  "Art. 155.2 CE.", "el Gobierno podrá dar instrucciones a todas las autoridades de las Comunidades Autónomas"),
]
for k, art, cat, q_, ops, e_, fr in Q: T.q(k, art, cat, q_, ops, e_, fr)
T.real("L", 13, "Competencias"); T.real("L", 14, "Acceso a la autonomía"); T.real("X", 24, "Control"); T.real("X", 65, "Control")
T.real("X", 23, "Principios"); T.real("L", 36, "Financiación"); T.real("P", 31, "Financiación")

# Flashcards
for q_, a_, cat in [
  ("Los tres principios del art. 2 CE", "Indisoluble unidad de la Nación española; derecho a la autonomía de las nacionalidades y regiones; solidaridad entre todas ellas.", "Principios"),
  ("¿Cómo se organiza territorialmente el Estado? (art. 137)", "En municipios, provincias y las Comunidades Autónomas que se constituyan; todas con autonomía para la gestión de sus respectivos intereses.", "Principios"),
  ("¿Qué no pueden implicar las diferencias entre Estatutos? (art. 138.2)", "En ningún caso, privilegios económicos o sociales.", "Principios"),
  ("Art. 139.1", "Todos los españoles tienen los mismos derechos y obligaciones en cualquier parte del territorio del Estado.", "Principios"),
  ("Iniciativa autonómica por la vía general (art. 143.2)", "Todas las Diputaciones interesadas (u órgano interinsular) y dos tercios de los municipios que sean mayoría del censo de cada provincia o isla; en seis meses. Si fracasa, cinco años (143.3).", "Acceso a la autonomía"),
  ("Iniciativa por la vía del art. 151.1", "Diputaciones y tres cuartas partes de los municipios de cada provincia (mayoría del censo), ratificada en referéndum por la mayoría absoluta de los electores de cada provincia.", "Acceso a la autonomía"),
  ("Art. 144: ¿cómo y por qué intervienen las Cortes?", "Mediante ley orgánica y por motivos de interés nacional.", "Acceso a la autonomía"),
  ("¿Cabe la federación de Comunidades Autónomas? (art. 145.1)", "No: «En ningún caso se admitirá».", "Acceso a la autonomía"),
  ("Convenios y acuerdos de cooperación entre Comunidades (art. 145.2)", "Convenios de servicios propios: según los Estatutos, con comunicación a las Cortes; demás acuerdos: autorización de las Cortes Generales.", "Acceso a la autonomía"),
  ("Ceuta y Melilla (disposición transitoria quinta)", "Acuerdo de sus Ayuntamientos por mayoría absoluta y autorización de las Cortes por ley orgánica, en los términos del art. 144.", "Acceso a la autonomía"),
  ("Contenido obligatorio del Estatuto (art. 147.2)", "Denominación; delimitación del territorio; denominación, organización y sede de las instituciones; competencias asumidas y bases para el traspaso de servicios.", "Estatutos"),
  ("Reforma de los Estatutos (arts. 147.3 y 152.2)", "Procedimiento del propio Estatuto y, en todo caso, aprobación de las Cortes por ley orgánica; en los del art. 151, además, referéndum.", "Estatutos"),
  ("Plazo de la Comisión Constitucional del Congreso en la vía del art. 151", "Dos meses.", "Estatutos"),
  ("Instituciones del art. 152.1", "Asamblea Legislativa (sufragio universal, representación proporcional); Consejo de Gobierno; Presidente elegido por la Asamblea de entre sus miembros y nombrado por el Rey.", "Organización"),
  ("¿Ante quién responden políticamente el Presidente y el Consejo de Gobierno?", "Ante la Asamblea (art. 152.1).", "Organización"),
  ("¿Quién dirige la Administración del Estado en la Comunidad? (art. 154)", "Un Delegado nombrado por el Gobierno.", "Organización"),
  ("Fondo de Compensación (art. 158.2)", "Para gastos de inversión; sus recursos los distribuyen las Cortes Generales.", "Financiación"),
  ("Ampliación de competencias (art. 148.2)", "Transcurridos cinco años y mediante la reforma de sus Estatutos, dentro del marco del art. 149.", "Competencias"),
  ("Cláusulas del art. 149.3", "Lo no atribuido al Estado puede ser autonómico vía Estatuto; lo no asumido es del Estado; prevalencia estatal salvo en lo exclusivo autonómico; derecho estatal supletorio en todo caso.", "Competencias"),
  ("Pesca: ¿Estado o Comunidades?", "Pesca marítima: Estado (149.1.19.ª). Aguas interiores, marisqueo, acuicultura y pesca fluvial: Comunidades (148.1.11.ª).", "Competencias"),
  ("Los cuatro controles del art. 153", "TC: normas con fuerza de ley; Gobierno, previo dictamen del Consejo de Estado: funciones delegadas del 150.2; contencioso-administrativo: administración y reglamentos; Tribunal de Cuentas: económico y presupuestario.", "Control"),
  ("Art. 155: pasos", "Requerimiento al Presidente de la Comunidad; si no es atendido, aprobación por mayoría absoluta del Senado; medidas del Gobierno e instrucciones a todas las autoridades autonómicas.", "Control"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Derecho a la autonomía", "Derecho que la Constitución reconoce y garantiza a las nacionalidades y regiones que integran la Nación española (art. 2).", "s1", "Principios")
T.glos("Principio de solidaridad", "Principio del art. 2 cuya realización efectiva garantiza el Estado, velando por un equilibrio económico adecuado y justo entre las partes del territorio (art. 138.1).", "s2", "Principios")
T.glos("Iniciativa autonómica", "Acuerdo de Diputaciones (u órganos interinsulares) y municipios que pone en marcha el acceso a la autonomía (arts. 143.2 y 151.1).", "s3", "Acceso a la autonomía")
T.glos("Federación de Comunidades Autónomas", "Unión de Comunidades Autónomas que la Constitución prohíbe en todo caso (art. 145.1).", "s4", "Acceso a la autonomía")
T.glos("Estatuto de Autonomía", "Norma institucional básica de cada Comunidad Autónoma, aprobada por ley orgánica y reconocida por el Estado como parte de su ordenamiento (arts. 81.1 y 147.1).", "s6", "Estatutos")
T.glos("Asamblea de Parlamentarios", "Asamblea de los Diputados y Senadores de las circunscripciones afectadas, convocada por el Gobierno para elaborar el proyecto de Estatuto por la vía del art. 151 (art. 151.2).", "s7", "Estatutos")
T.glos("Territorios forales", "Territorios cuyos derechos históricos ampara y respeta la Constitución (disposición adicional primera).", "s9", "Estatutos")
T.glos("Consejo de Gobierno", "Órgano colegiado autonómico con funciones ejecutivas y administrativas, dirigido por el Presidente de la Comunidad (art. 152.1).", "s10", "Organización")
T.glos("Tribunal Superior de Justicia", "Órgano que culmina la organización judicial en el territorio de la Comunidad Autónoma, sin perjuicio de la jurisdicción del Tribunal Supremo (art. 152.1).", "s11", "Organización")
T.glos("Delegado del Gobierno", "Órgano nombrado por el Gobierno que dirige la Administración del Estado en el territorio de la Comunidad Autónoma (art. 154).", "s12", "Organización")
T.glos("Fondo de Compensación", "Fondo con destino a gastos de inversión para corregir desequilibrios interterritoriales, distribuido por las Cortes Generales (art. 158.2).", "s13", "Financiación")
T.glos("Cláusula residual", "Regla del art. 149.3: la competencia sobre las materias no asumidas por los Estatutos corresponde al Estado.", "s16", "Competencias")
T.glos("Supletoriedad del derecho estatal", "El derecho estatal es, en todo caso, supletorio del derecho de las Comunidades Autónomas (art. 149.3).", "s16", "Competencias")
T.glos("Coerción estatal", "Medidas que puede adoptar el Gobierno, con aprobación por mayoría absoluta del Senado, para obligar a una Comunidad Autónoma al cumplimiento forzoso de sus obligaciones (art. 155).", "s20", "Control")

# Cronología (fechas de los metadatos del BOE)
T.hito("1978", "Constitución Española (27-12-1978; BOE de 29-12-1978)", "Título VIII, capítulo tercero (arts. 143 a 158): las Comunidades Autónomas", "normativo", "s1")
T.hito("1980", "Ley Orgánica 3/1980, de 22 de abril, del Consejo de Estado (BOE de 25-4-1980)", "Art. 22: consulta a la Comisión Permanente sobre el control de funciones delegadas", "normativo", "s19")
T.hito("2009", "Ley 22/2009, de 18 de diciembre, del sistema de financiación de las Comunidades Autónomas de régimen común (BOE de 19-12-2009)", "Fondo de Suficiencia Global como recurso de cierre del sistema", "normativo", "s13")

T.publicar()
