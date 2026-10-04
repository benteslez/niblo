# -*- coding: utf-8 -*-
"""Tema IV.1 (B4T01): Las fuentes del derecho administrativo: concepto y clases. La
jerarquía de las fuentes.
Método del I.2: mapa → bloques (I a III) con guía; cada artículo, texto literal del
BOE + ficha de casillas fijas; cierre 1 (preguntas oficiales) y cierre 2 (repaso).
Normas (textos consolidados del BOE): Código Civil, art. 1 (y 2.1); CE, arts. 1.1, 9,
10.2, 93, 96.1, 97, 103.1, 106.1, 149.1.8.ª y 149.3; Ley 39/2015, arts. 37, 47.2 y 127
a 133; Ley 40/2015, art. 3.1; Ley 50/1997, arts. 22, 24 y 25; LRBRL, art. 4.1 a); LJCA,
art. 26. Doctrina: STC 55/2018, de 24 de mayo (publicada en el BOE, BOE-A-2018-8574):
fallo y FJ 7, sobre el alcance de los arts. 129 a 133 de la Ley 39/2015."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO["LRBRL"] = "Ley 7/1985, LRBRL"
STC = "STC55_2018"   # Sentencia del TC 55/2018, BOE-A-2018-8574 (texto del BOE)
TIT_STC = "Sentencia del Tribunal Constitucional 55/2018, de 24 de mayo (BOE núm. 151, de 22 de junio de 2018) · {} · doctrina del TC publicada en el BOE; no es texto legal"

T = Tema("B4T01",
  "Tres preguntas: I. Qué son las fuentes y qué clases hay (Código Civil, art. 1; CE, arts. 1.1, 9.1, 10.2, 96, 97 y 103.1; Ley 39/2015, arts. 127 y 128.1) · II. Cómo se ordenan: la jerarquía (CE, art. 9.3; CC, art. 1.2; Ley 39/2015, arts. 37, 47.2 y 128; Ley 50/1997, art. 24; CE, arts. 106.1 y 149.3) · III. Cómo se hacen las normas: buena regulación, planificación y participación (Ley 39/2015, arts. 129 a 133, y STC 55/2018). Cada artículo: texto literal del BOE y ficha.",
  ["Fuentes del Derecho", "CC art. 1", "Costumbre", "Principios generales", "Jurisprudencia", "Jerarquía normativa", "Art. 9.3 CE", "Potestad reglamentaria", "Art. 97 CE", "Ley 50/1997 art. 24", "Orden Ministerial", "Inderogabilidad singular", "Buena regulación", "Consulta pública", "STC 55/2018"])

# =============================================================================
T.ap("s0", "Mapa del tema: tres preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque IV, tema 1):
> Las fuentes del derecho administrativo: concepto y clases. La jerarquía de las fuentes.

### El hilo conductor

El epígrafe se lee como **tres preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Constitución | Otras normas |
|---|---|---|---|
| **I** | ¿Qué son las fuentes y qué clases hay? (concepto y clases) | Arts. 1.1, 9.1, 10.2, 93, 96.1, 97, 103.1 y 149.1.8.ª | Código Civil, art. 1; Ley 40/2015, art. 3.1; Ley 39/2015, arts. 127 y 128.1; LRBRL, art. 4.1 a) |
| **II** | ¿Cómo se ordenan? (la jerarquía) | Arts. 9.3, 106.1 y 149.3 | Código Civil, art. 1.2; Ley 39/2015, arts. 128.2 y 3, 37 y 47.2; Ley 50/1997, art. 24; LJCA, art. 26 |
| **III** | ¿Cómo se hacen las normas administrativas? (buena regulación, planificación y participación) | — | Ley 39/2015, arts. 129 a 133; Ley 50/1997, arts. 22 y 25; Código Civil, art. 2.1; STC 55/2018 |

!> **La idea que une los tres bloques:** la ley no define qué es una «fuente»: el **Código Civil** enumera cuáles son (ley, costumbre y principios generales del derecho) y la **Constitución** atribuye al Estado la «determinación de las fuentes del Derecho» (I). Esas normas no valen todas lo mismo: la Constitución garantiza la **jerarquía normativa** y la norma que contradice otra de rango superior **carece de validez** (II). Y las normas que dicta la Administración (los reglamentos) se elaboran con unos **principios** y una **participación** ciudadana que fija la Ley 39/2015 (III).

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- La **ley** y los decretos legislativos y decretos-leyes se estudian en el tema IV.2; el **reglamento** (concepto, clases y límites), los **principios generales** y los **tratados**, en el tema IV.3. Aquí se ven como **clases de fuentes** y en su **jerarquía**.
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados. La STC 55/2018 se cita literal del BOE y se marca como **doctrina del TC**.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué son las fuentes y qué clases hay? (concepto y clases)", donde(
  "Primera pregunta del tema. Antes de ordenar las normas hay que saber **cuáles son**: qué fuentes enumera el Código Civil, qué papel tiene la Constitución y quién puede dictar normas con rango de ley y reglamentos.",
  ["1 Las fuentes del ordenamiento según el Código Civil (art. 1)", "2 La Constitución, norma suprema y fuente del Derecho administrativo", "3 Las normas con rango de ley (Ley 39/2015, art. 127)", "4 El reglamento: quién tiene la potestad reglamentaria", "5 Cuadro de las clases de fuentes"]))

T.ap("s1", "I.1 Las fuentes del ordenamiento según el Código Civil (art. 1)", f"""
El art. 1 del Código Civil (redacción del título preliminar de 1974) es la regla general sobre fuentes de todo el ordenamiento español, también del administrativo. La Constitución reserva al Estado su determinación.

{unidad("1.1 Cuáles son las fuentes (CC, art. 1.1; CE, art. 149.1.8.ª)",
  lit("CC", "a1", ["la ley, la costumbre y los principios generales del derecho"], solo=[1]),
  lit("CE", "Artículo 149", ["determinación de las fuentes del Derecho"], solo=[1, 9]),
  fichab("Enumeración de las fuentes del ordenamiento jurídico español",
         f"Las fija el **Estado**: {c('CE', 'Artículo 149', 'determinación de las fuentes del Derecho, con respeto, en este último caso, a las normas de derecho foral o especial')} (149.1.8.ª)",
         ["::Tres fuentes, por este orden (CC 1.1):", "La **ley**", "La **costumbre**", "Los **principios generales del derecho**"],
         "—",
         "Son **tres**. Ni la **jurisprudencia** ni los **reglamentos** ni los **tratados** figuran en la lista del 1.1 (los tratados se integran por publicación, → I.1.4; la jurisprudencia «complementará», → I.1.5). Cayó en 2025 (→ Cierre 1)."))}

{unidad("1.2 La costumbre (CC, art. 1.3)",
  lit("CC", "a1", ["sólo regirá en defecto de ley aplicable", "que resulte probada"], solo=[3, 4]),
  fichab("Fuente subsidiaria de la ley",
         "—",
         ["::Requisitos (1.3):", "En **defecto de ley** aplicable", "No contraria a la **moral** o al **orden público**", "Que resulte **probada**"],
         "—",
         f"Los usos jurídicos tienen la consideración de costumbre si no son {c('CC', 'a1', 'meramente interpretativos de una declaración de voluntad')}. La costumbre se **prueba**; la ley no."))}

{unidad("1.3 Los principios generales del derecho (CC, art. 1.4)",
  lit("CC", "a1", ["en defecto de ley o costumbre", "carácter informador del ordenamiento jurídico"], solo=[5]),
  fichab("Tercera fuente, con doble función",
         "—",
         ["Se aplican **en defecto de ley o costumbre**", "Y además **informan** todo el ordenamiento"],
         "—",
         "Doble papel: fuente **subsidiaria** (tras ley y costumbre) y carácter **informador**. Se desarrollan en el tema IV.3."))}

{unidad("1.4 Los tratados internacionales (CC, art. 1.5; CE, arts. 96.1 y 93)",
  lit("CC", "a1", ["mediante su publicación íntegra en el «Boletín Oficial del Estado»"], solo=[6]),
  lit("CE", "Artículo 96", ["una vez publicados oficialmente en España, formarán parte del ordenamiento interno"], solo=[1]),
  lit("CE", "Artículo 93", ["Mediante ley orgánica"]),
  fichab("Integración de los tratados en el ordenamiento interno",
         "—",
         ["Los tratados **válidamente celebrados**, una vez **publicados oficialmente** en España, forman parte del ordenamiento interno (CE 96.1)", "Sin publicación íntegra en el BOE, sus normas **no** son de aplicación directa (CC 1.5)", "Sus disposiciones solo se derogan, modifican o suspenden según el propio tratado o el Derecho internacional general (CE 96.1)"],
         "Tratados que atribuyan a una organización o institución internacional el ejercicio de competencias derivadas de la Constitución (art. 93): autorización **mediante ley orgánica**",
         "La clave es la **publicación** (íntegra, en el BOE), no la firma ni la autorización de las Cortes. Se desarrollan en el tema IV.3; el Derecho de la Unión Europea, en el bloque II del programa."))}

{unidad("1.5 La jurisprudencia y el deber de resolver (CC, arts. 1.6 y 1.7)",
  lit("CC", "a1", ["complementará el ordenamiento jurídico", "de modo reiterado", "el Tribunal Supremo", "el deber inexcusable de resolver en todo caso", "ateniéndose al sistema de fuentes establecido"], solo=[7, 8]),
  fichab("Papel de la jurisprudencia y obligación de los jueces",
         f"{c('CC', 'a1', 'el Tribunal Supremo')} (jurisprudencia); {c('CC', 'a1', 'Los Jueces y Tribunales')} (deber de resolver)",
         ["La jurisprudencia **complementa** el ordenamiento: doctrina del **Tribunal Supremo**, **reiterada**, al interpretar y aplicar ley, costumbre y principios", "Los jueces deben resolver **en todo caso**, conforme al sistema de fuentes"],
         "Doctrina establecida **de modo reiterado**",
         "La jurisprudencia **no** está en la lista del 1.1: «complementará». Es la del **Tribunal Supremo** (no la de cualquier tribunal) y exige reiteración."))}
""", 2)

T.ap("s2", "I.2 La Constitución, norma suprema y fuente del Derecho administrativo", f"""
La Constitución es la primera norma del ordenamiento: obliga a todos, fija sus valores superiores y somete la Administración a la ley y al Derecho.

{unidad("2.1 Sujeción a la Constitución y al ordenamiento (CE, art. 9.1)",
  lit("CE", "Artículo 9", ["están sujetos a la Constitución y al resto del ordenamiento jurídico"], solo=[1]),
  fichab("La Constitución vincula a todos",
         f"{c('CE', 'Artículo 9', 'Los ciudadanos y los poderes públicos')}",
         "Sujeción a la Constitución **y** al resto del ordenamiento",
         "—",
         "Vincula a **ciudadanos y poderes públicos** (no solo a los poderes públicos)."))}

{unidad("2.2 Los valores superiores del ordenamiento (CE, art. 1.1)",
  lit("CE", "Artículo 1", ["la libertad, la justicia, la igualdad y el pluralismo político"], solo=[1]),
  fichab("Valores que propugna el Estado social y democrático de Derecho",
         "El Estado (España)",
         ["Libertad", "Justicia", "Igualdad", "Pluralismo político"],
         "—",
         "Son **cuatro** valores superiores. La seguridad jurídica no es uno de ellos: es una garantía del art. 9.3 (→ II.1.1)."))}

{unidad("2.3 Interpretación de las normas sobre derechos (CE, art. 10.2)",
  lit("CE", "Artículo 10", ["la Declaración Universal de Derechos Humanos y los tratados y acuerdos internacionales sobre las mismas materias ratificados por España"], solo=[2]),
  fichab("Criterio de interpretación de las normas sobre derechos fundamentales y libertades",
         "Quien interpreta y aplica esas normas",
         "De conformidad con la **Declaración Universal de Derechos Humanos** y los tratados y acuerdos internacionales sobre las mismas materias **ratificados por España**",
         "—",
         "Es una regla de **interpretación**, no una enumeración de fuentes."))}

{unidad("2.4 La Administración, sometida a la ley y al Derecho (CE, art. 103.1; Ley 40/2015, art. 3.1)",
  lit("CE", "Artículo 103", ["con sometimiento pleno a la ley y al Derecho"], solo=[1]),
  lit("L40", "Artículo 3", ["con sometimiento pleno a la Constitución, a la Ley y al Derecho"], solo=[1]),
  fichab("Sometimiento de la Administración a todo el ordenamiento",
         f"{c('CE', 'Artículo 103', 'La Administración Pública')}; {c('L40', 'Artículo 3', 'Las Administraciones Públicas')}",
         "Sirven con objetividad los intereses generales con **sometimiento pleno** a la ley y al Derecho",
         "—",
         "La CE dice «a la **ley** y al **Derecho**»; la Ley 40/2015 añade «a la **Constitución**». Principios de actuación (103.1): **eficacia, jerarquía, descentralización, desconcentración y coordinación**."))}
""", 2)

T.ap("s3", "I.3 Las normas con rango de ley (Ley 39/2015, art. 127)", f"""
Además de las leyes, el Gobierno de la Nación y los órganos de gobierno autonómicos pueden dictar normas con rango de ley en los términos de la Constitución y los Estatutos (art. 127). Su estudio completo es el del tema IV.2; aquí basta su lugar entre las fuentes.

{unidad("3.1 Iniciativa legislativa y normas con rango de ley del Gobierno (Ley 39/2015, art. 127)",
  lit("L39", "Artículo 127", ["la ulterior remisión de los proyectos de ley a las Cortes Generales", "reales decretos-leyes y reales decretos legislativos", "normas equivalentes a aquéllas en su ámbito territorial"]),
  fichab("Participación del Gobierno en la producción de normas con rango de ley",
         f"{c('L39', 'Artículo 127', 'El Gobierno de la Nación')}; los órganos de gobierno de las Comunidades Autónomas",
         ["Iniciativa legislativa: elaboración y aprobación de **anteproyectos** y remisión de **proyectos** de ley a las Cortes", "Normas propias con rango de ley: **reales decretos-leyes** y **reales decretos legislativos**, en los términos de la Constitución (tema IV.2)", "Comunidades Autónomas: normas **equivalentes** en su ámbito, según la Constitución y su Estatuto"],
         "—",
         "El Gobierno **no** aprueba leyes: elabora **anteproyectos** y remite **proyectos**. Con rango de ley solo dicta **decretos-leyes** y **decretos legislativos**."))}
""", 2)

T.ap("s4", "I.4 El reglamento: quién tiene la potestad reglamentaria (CE, art. 97; Ley 39/2015, art. 128.1; LRBRL, art. 4.1 a)", f"""
El reglamento es la fuente propia de la Administración. Concepto, clases y límites: tema IV.3. Aquí, **quién** puede dictarlos.

{unidad("4.1 El Gobierno ejerce la potestad reglamentaria (CE, art. 97)",
  lit("CE", "Artículo 97", ["la potestad reglamentaria de acuerdo con la Constitución y las leyes"]),
  fichab("Fundamento constitucional de la potestad reglamentaria del Gobierno",
         c("CE", "Artículo 97", "El Gobierno"),
         "La ejerce **de acuerdo con la Constitución y las leyes**",
         "—",
         "La potestad reglamentaria se ejerce **de acuerdo con la Constitución y las leyes**; el art. 97 la atribuye al **Gobierno**. Las Órdenes Ministeriales son el segundo escalón de los reglamentos estatales (→ II.2.2)."))}

{unidad("4.2 Titulares de la potestad reglamentaria (Ley 39/2015, art. 128.1)",
  lit("L39", "Artículo 128", ["al Gobierno de la Nación, a los órganos de Gobierno de las Comunidades Autónomas", "a los órganos de gobierno locales"], solo=[1]),
  fichab("Quién puede dictar reglamentos",
         ["::Tres niveles (128.1):", "El **Gobierno de la Nación**", "Los **órganos de Gobierno de las Comunidades Autónomas**, según sus Estatutos", "Los **órganos de gobierno locales**, según la Constitución, los Estatutos y la Ley 7/1985"],
         "—",
         "—",
         "La potestad reglamentaria es de los **órganos de gobierno** de cada Administración territorial."))}

{unidad("4.3 Las entidades locales (LRBRL, art. 4.1 a)",
  lit("LRBRL", "Artículo 4", ["Las potestades reglamentaria y de autoorganización"], solo=[1, 2]),
  fichab("Potestad reglamentaria de las entidades locales territoriales",
         f"{c('LRBRL', 'Artículo 4', 'los municipios, las provincias y las islas')}",
         f"{c('LRBRL', 'Artículo 4', 'dentro de la esfera de sus competencias')}",
         "—",
         f"Corresponde a municipios, provincias e islas {c('LRBRL', 'Artículo 4', 'en todo caso')}, junto con la de **autoorganización**."))}
""", 2)

T.ap("s5", "I.5 Cuadro de las clases de fuentes (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Clase | Qué es | Quién la dicta | Artículos |
|---|---|---|---|
| Constitución | Norma a la que están sujetos ciudadanos y poderes públicos | — | CE 9.1 |
| Ley y normas con rango de ley | Leyes; decretos-leyes y decretos legislativos | Cortes Generales y Asambleas autonómicas; el Gobierno y los Consejos de Gobierno, en los términos de la Constitución y los Estatutos | CE 66.2, 82 y 86 (tema IV.2); Ley 39/2015, art. 127 |
| Reglamento | Disposición administrativa | Gobierno de la Nación, órganos de Gobierno autonómicos y órganos de gobierno locales | CE 97; Ley 39/2015, art. 128.1; LRBRL 4.1 a) |
| Tratados internacionales | Forman parte del ordenamiento interno una vez publicados oficialmente | — | CE 96.1; CC 1.5 (tema IV.3) |
| Costumbre | Fuente en defecto de ley aplicable, si se prueba | — | CC 1.3 |
| Principios generales del derecho | En defecto de ley o costumbre; informan el ordenamiento | — | CC 1.4 (tema IV.3) |
| Jurisprudencia | **Complementa** el ordenamiento (no es fuente del 1.1) | Tribunal Supremo, de modo reiterado | CC 1.6 |

{resumen([
  "Fuentes (CC 1.1): **ley**, **costumbre** y **principios generales del derecho**; su determinación es competencia del **Estado** (CE 149.1.8.ª).",
  "Costumbre: en **defecto de ley**, no contraria a la moral o al orden público y **probada** (1.3). Principios: en defecto de ley o costumbre, e **informadores** (1.4).",
  "Tratados: parte del ordenamiento una vez **publicados oficialmente** (CE 96.1); sin publicación íntegra en el BOE no se aplican directamente (CC 1.5). Jurisprudencia del **TS**, reiterada, **complementa** (1.6).",
  "La Administración actúa con **sometimiento pleno a la ley y al Derecho** (CE 103.1). Reglamentos: **Gobierno**, órganos de Gobierno **autonómicos** y órganos de gobierno **locales** (CE 97; Ley 39/2015, 128.1)."],
  "Siguiente: II. ¿Cómo se ordenan las fuentes? La jerarquía")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Cómo se ordenan las fuentes? La jerarquía", donde(
  "Segunda pregunta. Ya sabemos cuáles son las fuentes; ahora, **qué vale más**. La Constitución garantiza la jerarquía normativa y el Código Civil y la Ley 39/2015 dicen qué pasa con la norma que contradice otra superior.",
  ["1 El principio de jerarquía normativa (CE, art. 9.3; CC, art. 1.2; Ley 39/2015, art. 128.3)", "2 La jerarquía de los reglamentos del Estado (Ley 50/1997, art. 24)", "3 Ley y reglamento: límites y consecuencias (Ley 39/2015, arts. 128.2, 47.2 y 37)", "4 Quién controla la jerarquía (CE, art. 106.1; LJCA, art. 26)", "5 Jerarquía y competencia: Estado y Comunidades Autónomas (CE, art. 149.3)"]))

T.ap("s6", "II.1 El principio de jerarquía normativa (CE, art. 9.3; CC, art. 1.2; Ley 39/2015, art. 128.3)", f"""
{unidad("1.1 La Constitución garantiza la jerarquía normativa (CE, art. 9.3)",
  lit("CE", "Artículo 9", ["la jerarquía normativa", "la publicidad de las normas", "la interdicción de la arbitrariedad de los poderes públicos"], solo=[3]),
  fichab("Garantías constitucionales del ordenamiento",
         "La Constitución las garantiza",
         ["::Siete garantías (9.3):", "Principio de **legalidad**", "**Jerarquía normativa**", "**Publicidad** de las normas", "**Irretroactividad** de las disposiciones sancionadoras no favorables o restrictivas de derechos individuales", "**Seguridad jurídica**", "**Responsabilidad**", "**Interdicción de la arbitrariedad** de los poderes públicos"],
         "—",
         "Es **irretroactividad** (no «retroactividad») de las disposiciones sancionadoras **no favorables** o restrictivas de derechos individuales. Cayó en 2025 (→ Cierre 1)."))}

{unidad("1.2 Consecuencia: la norma contraria a otra superior carece de validez (CC, art. 1.2)",
  lit("CC", "a1", ["Carecerán de validez"], solo=[2]),
  fichab("Efecto de la jerarquía",
         "—",
         "La disposición que **contradiga otra de rango superior** carece de validez",
         "—",
         "El criterio es el **rango** de la disposición. Va en el art. 1.2, junto a la enumeración de fuentes."))}

{unidad("1.3 Jerarquía entre disposiciones administrativas (Ley 39/2015, art. 128.3)",
  lit("L39", "Artículo 128", ["al orden de jerarquía que establezcan las leyes", "Ninguna disposición administrativa podrá vulnerar los preceptos de otra de rango superior"], solo=[3]),
  fichab("Jerarquía dentro de los reglamentos",
         "—",
         "Las disposiciones administrativas se ordenan según la jerarquía que **establezcan las leyes** (en el Estado, la Ley 50/1997, art. 24 → II.2)",
         "—",
         "La Ley 39/2015 **no** fija el orden: remite a las **leyes**."))}
""", 2)

T.ap("s7", "II.2 La jerarquía de los reglamentos del Estado (Ley 50/1997, art. 24)", f"""
{unidad("2.1 Formas de las decisiones del Gobierno y de sus miembros (art. 24.1)",
  lit("LGOB", "a24", ["Reales Decretos del Presidente del Gobierno", "Reales Decretos acordados en Consejo de Ministros, las decisiones que aprueben normas reglamentarias", "Órdenes Ministeriales", "Orden del Ministro de la Presidencia"], solo=[1, 2, 3, 4, 5, 6, 7]),
  fichab("Forma de cada decisión",
         "El Gobierno de la Nación y sus miembros",
         ["a) **Reales Decretos Legislativos** y **Reales Decretos-leyes** (arts. 82 y 86 CE)", "b) **Reales Decretos del Presidente** del Gobierno", "c) **Reales Decretos acordados en Consejo de Ministros**: normas reglamentarias de su competencia", "d) **Acuerdos del Consejo de Ministros**: lo que no deba ser Real Decreto", "e) Acuerdos de **Comisiones Delegadas**: revisten forma de Orden", "f) **Órdenes Ministeriales**: disposiciones y resoluciones de los Ministros"],
         "—",
         "Si la Orden afecta a **varios Departamentos**: **Orden del Ministro de la Presidencia**, a propuesta de los Ministros interesados (24.1 f)."))}

{unidad("2.2 Jerarquía de los reglamentos (art. 24.2)",
  lit("LGOB", "a24", ["Los reglamentos se ordenarán según la siguiente jerarquía", "Disposiciones aprobadas por Real Decreto del Presidente del Gobierno o acordado en el Consejo de Ministros", "Disposiciones aprobadas por Orden Ministerial"], solo=[8, 9, 10]),
  fichab("Orden de los reglamentos estatales",
         "—",
         ["1.º Real Decreto del **Presidente** del Gobierno o **acordado en Consejo de Ministros**", "2.º **Orden Ministerial**"],
         "—",
         "Solo **dos** escalones. El Real Decreto del Presidente y el acordado en Consejo de Ministros están en el **mismo** nivel; las Órdenes Ministeriales, debajo."))}
""", 2)

T.ap("s8", "II.3 Ley y reglamento: límites y consecuencias (Ley 39/2015, arts. 128.2, 47.2 y 37)", f"""
{unidad("3.1 Lo que el reglamento no puede hacer (Ley 39/2015, art. 128.2)",
  lit("L39", "Artículo 128", ["no podrán vulnerar la Constitución o las leyes", "no podrán tipificar delitos, faltas o infracciones administrativas, establecer penas o sanciones, así como tributos"], solo=[2]),
  fichab("Límites de los reglamentos frente a la ley",
         "Los reglamentos y disposiciones administrativas",
         ["No pueden **vulnerar** la Constitución o las leyes", "No pueden regular materias de la competencia de las **Cortes** o de las **Asambleas Legislativas** autonómicas", "Sin perjuicio de su función de **desarrollo o colaboración** con la ley, no pueden tipificar delitos, faltas o infracciones, establecer penas o sanciones, tributos, exacciones parafiscales u otras cargas o prestaciones personales o patrimoniales de carácter público"],
         "—",
         "La lista de lo vedado incluye **infracciones administrativas** y **sanciones**, no solo delitos y penas. Límites del reglamento: tema IV.3."))}

{unidad("3.2 La sanción: nulidad de pleno derecho (Ley 39/2015, art. 47.2)",
  lit("L39", "Artículo 47", ["las disposiciones administrativas que vulneren la Constitución, las leyes u otras disposiciones administrativas de rango superior"], solo=[9]),
  fichab("Disposiciones administrativas nulas de pleno derecho",
         "—",
         ["::Son nulas (47.2) las que:", "Vulneren la **Constitución**, las **leyes** u otras disposiciones administrativas de **rango superior**", "Regulen **materias reservadas a la Ley**", "Establezcan la **retroactividad** de disposiciones sancionadoras no favorables o restrictivas de derechos individuales"],
         "—",
         "En los supuestos del 47.2 la disposición es **nula de pleno derecho**, no anulable. Incluye regular **materias reservadas a la Ley**."))}

{unidad("3.3 La inderogabilidad singular de los reglamentos (Ley 39/2015, art. 37)",
  lit("L39", "Artículo 37", ["aunque aquéllas procedan de un órgano de igual o superior jerarquía", "Son nulas las resoluciones administrativas que vulneren lo establecido en una disposición reglamentaria"]),
  fichab("La resolución particular no puede saltarse el reglamento",
         "Cualquier órgano, **aunque sea de igual o superior jerarquía** al que dictó la disposición general",
         "Las resoluciones de **carácter particular** no pueden vulnerar una disposición de **carácter general**",
         "—",
         "Rige **aunque** la resolución venga de un órgano de **igual o superior** jerarquía. Efecto: **nulidad** de la resolución (37.2)."))}
""", 2)

T.ap("s9", "II.4 Quién controla la jerarquía (CE, art. 106.1; LJCA, art. 26)", f"""
{unidad("4.1 Los Tribunales controlan la potestad reglamentaria (CE, art. 106.1)",
  lit("CE", "Artículo 106", ["Los Tribunales controlan la potestad reglamentaria"], solo=[1]),
  fichab("Control judicial de los reglamentos y de la actuación administrativa",
         c("CE", "Artículo 106", "Los Tribunales"),
         "Controlan la **potestad reglamentaria**, la **legalidad** de la actuación administrativa y su sometimiento a los **fines** que la justifican",
         "—",
         "El control de los reglamentos es de los **Tribunales** (jurisdicción contencioso-administrativa: tema IV.13)."))}

{unidad("4.2 Recurso directo e indirecto contra reglamentos (LJCA, art. 26)",
  lit("LJCA", "Artículo 26", ["también es admisible la de los actos que se produzcan en aplicación de las mismas", "no impiden la impugnación de los actos de aplicación"]),
  fichab("Dos vías para atacar un reglamento ilegal",
         "Quien esté legitimado (LJCA: tema IV.13)",
         ["Impugnación **directa** de la disposición general", "Impugnación de los **actos de aplicación**, fundada en que la disposición no es conforme a Derecho (26.1)"],
         "—",
         "No haber impugnado el reglamento, o haber perdido el recurso directo, **no impide** atacar sus actos de aplicación (26.2)."))}
""", 2)

T.ap("s10", "II.5 Jerarquía y competencia: Estado y Comunidades Autónomas (CE, art. 149.3)", f"""
Entre normas del Estado y de las Comunidades Autónomas no decide solo el rango: la Constitución fija reglas de **competencia**, **prevalencia** y **supletoriedad**.

{unidad("5.1 Cláusulas de cierre del reparto de competencias (CE, art. 149.3)",
  lit("CE", "Artículo 149", ["podrán corresponder a las Comunidades Autónomas, en virtud de sus respectivos Estatutos", "cuyas normas prevalecerán, en caso de conflicto", "El derecho estatal será, en todo caso, supletorio del derecho de las Comunidades Autónomas"], solo=[35]),
  fichab("Relación entre el Derecho estatal y el autonómico",
         "El Estado y las Comunidades Autónomas",
         ["Materias no atribuidas expresamente al Estado: **pueden** corresponder a las CC. AA. según sus **Estatutos**", "Materias no asumidas por los Estatutos: corresponden al **Estado**", "**Prevalencia**: en caso de conflicto, la norma estatal prevalece en todo lo no atribuido a la **exclusiva** competencia autonómica", "**Supletoriedad**: el derecho estatal es, en todo caso, supletorio"],
         "—",
         "Las normas del Estado **no** prevalecen sobre lo que es de **exclusiva** competencia autonómica. Supletoriedad: «**en todo caso**»."))}

### Cuadro: la escala de las normas (esquema)

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Escalón | Norma | Artículos |
|---|---|---|
| 1 | Constitución | CE 9.1; Ley 39/2015, arts. 128.2 y 47.2 |
| 2 | Leyes y normas con rango de ley | CE 97; Ley 39/2015, arts. 128.2 y 47.2; tema IV.2 |
| 3 | Reglamentos del Estado: Real Decreto del Presidente o acordado en Consejo de Ministros | Ley 50/1997, art. 24.2.1.º |
| 4 | Reglamentos del Estado: Orden Ministerial | Ley 50/1997, art. 24.2.2.º |
| — | Resoluciones de carácter particular: no pueden vulnerar una disposición general | Ley 39/2015, art. 37.1 |

{resumen([
  "La CE garantiza la **jerarquía normativa** (9.3); la norma que contradice otra de **rango superior** carece de validez (CC 1.2) y ninguna disposición administrativa puede vulnerar otra superior (Ley 39/2015, 128.3).",
  "Reglamentos del Estado (Ley 50/1997, 24.2): **1.º** Real Decreto del Presidente o acordado en Consejo de Ministros; **2.º** Orden Ministerial.",
  "Disposiciones contrarias a la CE, a las leyes o a otras superiores: **nulas de pleno derecho** (47.2). Resolución particular contra reglamento: **nula**, aunque venga de órgano igual o superior (37).",
  "Controlan los **Tribunales** (CE 106.1), por recurso directo o indirecto (LJCA 26). Estado y CC. AA.: **prevalencia** fuera de lo exclusivo autonómico y **supletoriedad** (CE 149.3)."],
  "Siguiente: III. ¿Cómo se hacen las normas administrativas?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Cómo se hacen las normas administrativas? Buena regulación, planificación y participación (Ley 39/2015, arts. 129 a 133)", donde(
  "Tercera pregunta. El Título VI de la Ley 39/2015 fija los **principios** con que las Administraciones ejercen la iniciativa legislativa y la potestad reglamentaria, la **evaluación**, la **publicidad**, la **planificación** y la **participación** ciudadana. La STC 55/2018 limitó su alcance para las Comunidades Autónomas.",
  ["1 Principios de buena regulación (art. 129; Ley 50/1997, art. 22)", "2 Evaluación, publicidad y planificación normativa (arts. 130 a 132; Ley 50/1997, art. 25; CC, art. 2.1)", "3 Participación de los ciudadanos (art. 133)", "4 El alcance de los arts. 129 a 133 tras la STC 55/2018"]))

T.ap("s11", "III.1 Principios de buena regulación (Ley 39/2015, art. 129; Ley 50/1997, art. 22)", f"""
{unidad("1.1 El Gobierno se rige por el Título VI de la Ley 39/2015 (Ley 50/1997, art. 22)",
  lit("LGOB", "a22", ["de conformidad con los principios y reglas establecidos en el Título VI de la Ley 39/2015"]),
  fichab("Remisión de la Ley del Gobierno a la Ley 39/2015",
         c("LGOB", "a22", "El Gobierno"),
         "Ejerce la iniciativa y la potestad reglamentaria según el **Título VI de la Ley 39/2015** y el Título V de la propia Ley 50/1997",
         "—",
         "Por esta remisión los arts. 127 a 133 de la Ley 39/2015 rigen para el **Gobierno de la Nación** (→ III.4)."))}

{unidad("1.2 Los seis principios, necesidad y eficacia, proporcionalidad (art. 129.1 a 3)",
  lit("L39", "Artículo 129", ["necesidad, eficacia, proporcionalidad, seguridad jurídica, transparencia, y eficiencia", "En la exposición de motivos o en el preámbulo", "una razón de interés general", "la regulación imprescindible"], solo=[1, 2, 3]),
  fichab("Principios que deben respetar las iniciativas normativas",
         f"{c('L39', 'Artículo 129', 'las Administraciones Públicas')}, en la iniciativa legislativa y la potestad reglamentaria",
         ["::Seis principios (129.1):", "Necesidad", "Eficacia", "Proporcionalidad", "Seguridad jurídica", "Transparencia", "Eficiencia"],
         "Justificación en la **exposición de motivos** (anteproyectos de ley) o en el **preámbulo** (proyectos de reglamento)",
         "**Necesidad y eficacia**: razón de **interés general**, fines claros, instrumento **más adecuado** (129.2). **Proporcionalidad**: la regulación **imprescindible**, tras constatar que no hay medidas **menos restrictivas** (129.3)."))}

{unidad("1.3 Seguridad jurídica y habilitaciones reglamentarias (art. 129.4)",
  lit("L39", "Artículo 129", ["de manera coherente con el resto del ordenamiento jurídico, nacional y de la Unión Europea", "deberán ser justificados atendiendo a la singularidad de la materia", "Autoridades Independientes"], solo=[4, 5, 7]),
  fichab("Coherencia del ordenamiento y a quién se habilita para desarrollar la ley",
         ["Habilitación para el desarrollo reglamentario: " + c('L39', 'Artículo 129', 'con carácter general, al Gobierno'), "Directamente a los titulares de los departamentos ministeriales u órganos dependientes o subordinados: " + c('L39', 'Artículo 129', 'tendrá carácter excepcional y deberá justificarse en la ley habilitante'), "Las leyes pueden habilitar directamente a **Autoridades Independientes** u otros organismos, cuando la naturaleza de la materia lo exija"],
         ["Seguridad jurídica: marco normativo **estable, predecible, integrado, claro y de certidumbre**", "Trámites de procedimiento **adicionales o distintos** a los de la Ley 39/2015: justificados por la **singularidad** de la materia o los fines"],
         "—",
         "La habilitación **general** es al **Gobierno**; a un **Ministro**, solo de forma **excepcional** y justificada en la ley habilitante."))}

?> **Aviso de vigencia (párrafo tercero del art. 129.4).** Ese párrafo no se reproduce entero arriba porque la STC 55/2018 declaró inconstitucionales y nulos dos incisos suyos referidos a las Comunidades Autónomas: {c(STC, 'preambulo', 'los incisos «o Consejo de Gobierno respectivo» y «o de las consejerías de Gobierno» del párrafo tercero del artículo 129.4')} (fallo, 1.º → III.4). Lo que sigue vigente se cita en la ficha: {c('L39', 'Artículo 129', 'Las habilitaciones para el desarrollo reglamentario de una ley serán conferidas, con carácter general, al Gobierno')}.

{unidad("1.4 Transparencia, eficiencia y gasto público (art. 129.5 a 7)",
  lit("L39", "Artículo 129", ["acceso sencillo, universal y actualizado a la normativa en vigor", "participación activa en la elaboración de las normas", "evitar cargas administrativas innecesarias o accesorias", "estabilidad presupuestaria y sostenibilidad financiera"], solo=[8, 9, 10]),
  fichab("Últimos principios y la regla del gasto",
         "Las Administraciones Públicas",
         ["**Transparencia**: acceso sencillo, universal y actualizado a la normativa y a los documentos de su elaboración (art. 7 de la Ley 19/2013); objetivos y justificación en el preámbulo o exposición de motivos; **participación activa** de los destinatarios", "**Eficiencia**: evitar **cargas administrativas innecesarias o accesorias** y racionalizar la gestión de los recursos públicos", "Si afecta a gastos o ingresos públicos: **cuantificar y valorar** sus repercusiones"],
         "Supeditación a la **estabilidad presupuestaria** y **sostenibilidad financiera** (129.7)",
         f"Evitar {c('L39', 'Artículo 129', 'cargas administrativas **innecesarias o accesorias**')} es **eficiencia** (129.6), no proporcionalidad."))}
""", 2)

T.ap("s12", "III.2 Evaluación, publicidad y planificación normativa (Ley 39/2015, arts. 130 a 132; Ley 50/1997, art. 25; CC, art. 2.1)", f"""
{unidad("2.1 Evaluación normativa (Ley 39/2015, art. 130)",
  lit("L39", "Artículo 130", ["revisarán periódicamente su normativa vigente", "un informe que se hará público"]),
  fichab("Revisión periódica de la normativa vigente",
         "Las Administraciones Públicas",
         ["Revisar la normativa para adaptarla a los **principios de buena regulación**", "Comprobar si las normas han conseguido sus **objetivos** y si estaban justificados el **coste** y las **cargas**", "Promover el **análisis económico** y evitar restricciones injustificadas o desproporcionadas a la actividad económica (130.2)"],
         "Resultado: **informe público**, con el detalle, periodicidad y órgano que fije la normativa de cada Administración",
         "La evaluación es **periódica** y termina en un informe **público**."))}

{unidad("2.2 Publicidad de las normas (Ley 39/2015, art. 131; CC, art. 2.1)",
  lit("L39", "Artículo 131", ["habrán de publicarse en el diario oficial correspondiente para que entren en vigor y produzcan efectos jurídicos", "de manera facultativa", "tendrá carácter oficial y auténtico"]),
  lit("CC", "art2", ["a los veinte días de su completa publicación"], solo=[1]),
  fichab("Publicación como requisito de vigencia y eficacia",
         "Cada Administración, en su **diario oficial**",
         ["Normas con rango de ley, reglamentos y disposiciones: **publicación en el diario oficial** correspondiente para que **entren en vigor** y produzcan efectos", "Otros medios de publicidad: **complementarios** y **facultativos**", "Diarios en sede electrónica: los **mismos efectos** que la edición impresa; el BOE en sede electrónica es **oficial y auténtico**"],
         f"Entrada en vigor de las leyes: {c('CC', 'art2', 'a los veinte días de su completa publicación')} en el BOE, si en ellas no se dispone otra cosa (CC 2.1)",
         "Sin publicación no hay entrada en vigor (es la **publicidad** del art. 9.3 CE → II.1.1). Plazo supletorio de entrada en vigor de las leyes: **20 días** desde la **completa** publicación."))}

{unidad("2.3 Planificación normativa (Ley 39/2015, art. 132; Ley 50/1997, art. 25)",
  lit("L39", "Artículo 132", ["Anualmente", "en el Portal de la Transparencia"]),
  lit("LGOB", "a25", ["El Gobierno aprobará anualmente un Plan Normativo", "antes del 30 de abril"], solo=[1, 3, 4]),
  fichab("El Plan Anual Normativo",
         "Cada Administración Pública lo hace público; en el Estado, lo aprueba el **Consejo de Ministros**: lo coordina el **Ministerio de la Presidencia** y lo eleva el **Ministro de la Presidencia** (LGOB 25.4)",
         ["Contiene las iniciativas legales o reglamentarias que se elevarán para su aprobación **el año siguiente**", "Se publica en el **Portal de la Transparencia** (132.2)", "Propuesta normativa no incluida en el Plan: hay que **justificarlo** en la Memoria del Análisis de Impacto Normativo (LGOB 25.3)"],
         "**Anual**; en el Estado, el Ministro de la Presidencia lo eleva al Consejo de Ministros **antes del 30 de abril** (LGOB 25.4)",
         "El Plan recoge las iniciativas del **año siguiente**. El art. 132 no rige para las Comunidades Autónomas (STC 55/2018 → III.4)."))}
""", 2)

T.ap("s13", "III.3 Participación de los ciudadanos (Ley 39/2015, art. 133)", f"""
{unidad("3.1 Consulta pública previa y audiencia e información públicas (art. 133.1 a 3)",
  lit("L39", "Artículo 133", ["Con carácter previo a la elaboración del proyecto o anteproyecto de ley o de reglamento, se sustanciará una consulta pública", "Los problemas que se pretenden solucionar con la iniciativa", "Las posibles soluciones alternativas regulatorias y no regulatorias", "dar audiencia a los ciudadanos afectados", "claros, concisos"], solo=[1, 2, 3, 4, 5, 6, 7]),
  fichab("Dos momentos de participación",
         ["Consulta previa: sujetos y **organizaciones más representativas** potencialmente afectados", "Audiencia: **ciudadanos afectados** en sus derechos e intereses legítimos; puede recabarse la opinión de organizaciones o asociaciones reconocidas por ley"],
         ["::Consulta pública **previa** (133.1), por el portal web, sobre:", "a) Los **problemas** que se pretenden solucionar", "b) La **necesidad y oportunidad** de su aprobación", "c) Los **objetivos** de la norma", "d) Las posibles **soluciones alternativas** regulatorias y no regulatorias", "Después, **audiencia e información públicas** sobre el **texto** ya redactado, si afecta a derechos e intereses legítimos (133.2)"],
         "—",
         "La consulta es **previa a la elaboración** del texto; la audiencia es **sobre el texto**. Los documentos deben ser **claros, concisos** y con toda la información precisa (133.3)."))}

{unidad("3.2 Cuándo puede prescindirse de la participación (art. 133.4)",
  lit("L39", "Artículo 133", ["normas presupuestarias u organizativas", "razones graves de interés público que lo justifiquen", "no tenga un impacto significativo en la actividad económica"], solo=[8, 9]),
  fichab("Excepciones a la consulta, audiencia e información públicas",
         "La Administración que elabora la norma",
         ["::Puede prescindirse de **todos** los trámites (133.4, párr. 1.º):", "Normas **presupuestarias u organizativas** de la AGE, la autonómica, la local o sus organizaciones dependientes o vinculadas", "Cuando concurran **razones graves de interés público** que lo justifiquen", "Solo de la **consulta previa** (párr. 2.º): sin impacto significativo en la actividad económica, sin obligaciones relevantes para los destinatarios o regulación de aspectos parciales; y en la tramitación urgente, según su normativa"],
         "—",
         "Las normas excluidas son las presupuestarias u **organizativas** (no las «no organizativas»). Cayó en 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s14", "III.4 El alcance de los arts. 129 a 133 tras la STC 55/2018", f"""
La STC 55/2018, que resolvió un recurso de inconstitucionalidad contra la Ley 39/2015, anuló dos incisos del art. 129.4 y declaró que varios artículos del Título VI son **contrarios al orden constitucional de competencias**, sin anularlos. Fallo literal:

{lit(STC, "preambulo", ["Declarar la inconstitucionalidad y nulidad", "son contrarios al orden constitucional de competencias"], solo=[196, 197, 198, 199], titulo=TIT_STC.format("fallo"))}

Qué significa «contrarios al orden constitucional de competencias» lo explica la propia sentencia (FJ 7):

{lit(STC, "preambulo", ["no son aplicables a las iniciativas legislativas de las Comunidades Autónomas", "resultando por ello inaplicables a las Comunidades Autónomas", "los preceptos se aplican en el ámbito estatal"], solo=[109, 120], titulo=TIT_STC.format("fundamento jurídico 7, extractos"))}

### Cuadro: qué rige para quién (esquema)

*Esquema de elaboración propia: resume el fallo y el FJ 7 citados; no es texto legal.*

| Precepto de la Ley 39/2015 | Estado | Comunidades Autónomas |
|---|---|---|
| Art. 129.4, párr. 3.º, incisos «o Consejo de Gobierno respectivo» y «o de las consejerías…» | **Nulos** (fallo 1.º) | **Nulos** (fallo 1.º) |
| Arts. 129 (salvo 129.4, párrs. 2.º y 3.º) y 130 | Se aplican | No se aplican a sus **iniciativas legislativas** (fallo 2.º; FJ 7 b) |
| Art. 132 (Plan Anual Normativo) | Se aplica | No se aplica (fallo 2.º y 3.º) |
| Art. 133 (participación) | Se aplica | Solo el **inciso inicial del 133.1** (se sustanciará una consulta pública previa) y el **primer párrafo del 133.4**, y no en sus iniciativas legislativas (fallo 2.º y 3.º) |

!> **Por qué importa para el examen:** el examen pregunta la **letra** de los arts. 129 a 133, que siguen en el BOE y rigen en el **Estado** (Ley 50/1997, art. 22 → III.1.1). La pregunta oficial de 2025 sobre el art. 133.4 (→ Cierre 1) se refiere precisamente al **primer párrafo** del 133.4, que el TC salvó.

{resumen([
  "**Seis** principios de buena regulación (129.1): necesidad, eficacia, proporcionalidad, seguridad jurídica, transparencia y eficiencia; justificación en la **exposición de motivos** o el **preámbulo**.",
  "Habilitación para desarrollar una ley: **con carácter general, al Gobierno**; a un Ministro, **excepcional** y justificada (129.4).",
  "Evaluación **periódica** con informe **público** (130); publicación en el **diario oficial** para entrar en vigor (131); **Plan Anual Normativo** con las iniciativas del **año siguiente**, en el Portal de la Transparencia (132).",
  "Consulta pública **previa** + audiencia sobre el **texto** (133); se prescinde en normas **presupuestarias u organizativas** o por **razones graves de interés público** (133.4).",
  "STC 55/2018: **nulos** dos incisos del 129.4; arts. 129, 130, 132 y 133 **inaplicables** en parte a las Comunidades Autónomas, pero **vigentes** en el ámbito estatal."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_L46 = examen("L", 46, {
  "a": f"Ni los tratados ni la jurisprudencia están en el art. 1.1: los tratados se integran {c('CC', 'a1', 'mediante su publicación íntegra')} en el BOE (1.5) y la jurisprudencia {c('CC', 'a1', 'complementará el ordenamiento jurídico')} (1.6).",
  "b": f"Los reglamentos no figuran en la enumeración del 1.1, y la doctrina del Tribunal Supremo es la jurisprudencia, que {c('CC', 'a1', 'complementará el ordenamiento jurídico')} (1.6): no es fuente del 1.1.",
  "c": f"Cambia dos de las tres fuentes: el art. 1.1 no cita los reglamentos, y la jurisprudencia {c('CC', 'a1', 'complementará el ordenamiento jurídico')} (1.6).",
  "d": f"Literal del art. 1.1: {c('CC', 'a1', 'Las fuentes del ordenamiento jurídico español son la ley, la costumbre y los principios generales del derecho')}."},
  [("la costumbre y los principios generales del derecho", "CC", "a1", "Las fuentes del ordenamiento jurídico español son la ley, la costumbre y los principios generales del derecho")])
EX_L48 = examen("L", 48, {
  "a": f"El art. 133.4 dice lo contrario: se puede prescindir en el caso de {c('L39', 'Artículo 133', 'normas presupuestarias u organizativas')}, no de las «no organizativas».",
  "b": f"Cambia la palabra clave: son las normas {c('L39', 'Artículo 133', 'presupuestarias u organizativas')}, no las «no presupuestarias».",
  "c": f"Literal del art. 133.4: {c('L39', 'Artículo 133', 'o cuando concurran razones graves de interés público que lo justifiquen')}.",
  "d": f"Igual que la a): la excepción es para las normas {c('L39', 'Artículo 133', 'presupuestarias u organizativas de la Administración General del Estado')}, no para las «no organizativas»."},
  [("razones graves de interés público que lo justifiquen", "L39", "Artículo 133", "o cuando concurran razones graves de interés público que lo justifiquen")])
EX_P51 = examen("P", 51, {
  "a": f"Es al revés: se garantiza {c('CE', 'Artículo 9', 'la irretroactividad de las disposiciones sancionadoras no favorables o restrictivas de derechos individuales')}; el art. 9.3 no prevé ninguna salvedad por interés general.",
  "b": f"Literal del art. 9.3: {c('CE', 'Artículo 9', 'la interdicción de la arbitrariedad de los poderes públicos')}.",
  "c": f"No está en el art. 9.3: es un principio de actuación de las Administraciones de la Ley 40/2015 ({c('L40', 'Artículo 3', 'Servicio efectivo a los ciudadanos')}, art. 3.1 a).",
  "d": f"El art. 9.3 garantiza {c('CE', 'Artículo 9', 'el principio de legalidad, la jerarquía normativa')}, no una reserva de ley orgánica; las materias de ley orgánica las fija el art. 81.1 (tema IV.2)."},
  [("interdicción de la arbitrariedad de los poderes públicos", "CE", "Artículo 9", "la interdicción de la arbitrariedad de los poderes públicos")])

T.ap("s15", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayó **una** pregunta de este tema (las fuentes del art. 1.1 del Código Civil) y **dos** relacionadas (consulta pública del art. 133 de la Ley 39/2015 y garantías del art. 9.3 CE). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-L 2025, pregunta 46 · Fuentes del ordenamiento (→ I.1.1)", EX_L46,
  "### GACE-L 2025, pregunta 48 · Consulta pública (relacionada; → III.3.2)", EX_L48,
  "### GACE-P 2025, pregunta 51 · Art. 9.3 (relacionada; → II.1.1)", EX_P51,
  "### Cómo se pregunta",
  "!> Las fuentes se preguntan **mezclando** las del art. 1.1 con figuras que **no** están en él (reglamentos, tratados, jurisprudencia). Los arts. 9.3 CE y 133.4 de la Ley 39/2015, con **una palabra cambiada** («retroactividad», «no organizativas», «no presupuestarias»). Saber el texto literal resuelve la pregunta.",
]))

T.ap("s16", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Concepto y clases | CC 1: ley, costumbre, principios generales; tratados publicados; jurisprudencia del TS que complementa. CE 9.1, 1.1, 103.1. Reglamentos: Gobierno, CC. AA., entes locales (CE 97; Ley 39/2015, 128.1) | **Tres** fuentes del 1.1; la jurisprudencia **complementa**; costumbre **probada** y en **defecto de ley** |
| II. Jerarquía | CE 9.3; CC 1.2; Ley 39/2015, 128.2 y 3, 47.2 y 37; Ley 50/1997, 24; CE 106.1 y 149.3 | Reglamentos estatales: **1.º** RD del Presidente o acordado en Consejo de Ministros; **2.º** Orden Ministerial. Disposición contraria a otra superior: **nula de pleno derecho** |
| III. Elaboración | Ley 39/2015, 129 a 133; Ley 50/1997, 22 y 25; STC 55/2018 | **Seis** principios; Plan Anual Normativo del **año siguiente**; consulta previa salvo normas **presupuestarias u organizativas** o **razones graves de interés público** |

?> **Trampas frecuentes:** «la **jurisprudencia** es fuente del art. 1.1» (la **complementa**, 1.6); «los **reglamentos** son fuente del 1.1» (el 1.1 dice ley, costumbre y principios generales); «la costumbre rige **aunque haya ley**» (solo **en defecto de ley aplicable**); «el art. 9.3 garantiza la **retroactividad**…» (es la **irretroactividad**); «la Orden Ministerial y el Real Decreto tienen el **mismo** rango» (la Orden va en el **2.º** escalón); «una resolución del **superior** puede dispensar del reglamento» (no: inderogabilidad singular, art. 37.1); «se prescinde de la consulta en normas **no organizativas**» (son las **organizativas** y **presupuestarias**); «la STC 55/2018 **anuló** los arts. 132 y 133» (los declaró **contrarios al orden de competencias**, sin nulidad).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
T.q("CC", "a1", "Fuentes", "Según el artículo 1.1 del Código Civil, las fuentes del ordenamiento jurídico español son:",
    ["La ley, la costumbre y los principios generales del derecho.", "La ley, el reglamento y la costumbre.", "La ley, la costumbre y la jurisprudencia.", "La Constitución, la ley y los tratados internacionales."],
    "Art. 1.1 CC: «la ley, la costumbre y los principios generales del derecho».", "Las fuentes del ordenamiento jurídico español son la ley, la costumbre y los principios generales del derecho")
T.q("CC", "a1", "Jerarquía", "Según el artículo 1.2 del Código Civil, las disposiciones que contradigan otra de rango superior:",
    ["Carecerán de validez.", "Serán anulables en el plazo de cuatro años.", "Se aplicarán con carácter supletorio.", "Serán válidas hasta su derogación expresa."],
    "Art. 1.2 CC: «Carecerán de validez las disposiciones que contradigan otra de rango superior».", "Carecerán de validez las disposiciones que contradigan otra de rango superior")
T.q("CC", "a1", "Fuentes", "Según el artículo 1.3 del Código Civil, la costumbre sólo regirá:",
    ["En defecto de ley aplicable, siempre que no sea contraria a la moral o al orden público, y que resulte probada.", "En concurrencia con la ley, cuando sea más favorable.", "En defecto de principios generales del derecho.", "Cuando lo declare el Tribunal Supremo de modo reiterado."],
    "Art. 1.3 CC.", "La costumbre sólo regirá en defecto de ley aplicable, siempre que no sea contraria a la moral o al orden público, y que resulte probada")
T.q("CC", "a1", "Fuentes", "Según el artículo 1.3 del Código Civil, tendrán la consideración de costumbre:",
    ["Los usos jurídicos que no sean meramente interpretativos de una declaración de voluntad.", "Los usos sociales reiterados durante más de diez años.", "Los usos meramente interpretativos de una declaración de voluntad.", "Las prácticas administrativas reiteradas."],
    "Art. 1.3 CC, párrafo segundo.", "Los usos jurídicos que no sean meramente interpretativos de una declaración de voluntad, tendrán la consideración de costumbre")
T.q("CC", "a1", "Fuentes", "Según el artículo 1.4 del Código Civil, los principios generales del derecho se aplicarán:",
    ["En defecto de ley o costumbre, sin perjuicio de su carácter informador del ordenamiento jurídico.", "Con preferencia a la costumbre.", "Solo cuando lo autorice expresamente una ley.", "En defecto de jurisprudencia del Tribunal Supremo."],
    "Art. 1.4 CC.", "Los principios generales del derecho se aplicarán en defecto de ley o costumbre, sin perjuicio de su carácter informador del ordenamiento jurídico")
T.q("CC", "a1", "Fuentes", "Según el artículo 1.5 del Código Civil, las normas jurídicas contenidas en los tratados internacionales serán de aplicación directa en España cuando hayan pasado a formar parte del ordenamiento interno mediante:",
    ["Su publicación íntegra en el «Boletín Oficial del Estado».", "Su ratificación por el Congreso de los Diputados.", "Su firma por el Gobierno.", "Su publicación en el Boletín Oficial de las Cortes Generales."],
    "Art. 1.5 CC.", "mediante su publicación íntegra en el «Boletín Oficial del Estado»")
T.q("CC", "a1", "Fuentes", "Según el artículo 1.6 del Código Civil, la jurisprudencia:",
    ["Complementará el ordenamiento jurídico con la doctrina que, de modo reiterado, establezca el Tribunal Supremo.", "Es fuente del ordenamiento jurídico junto con la ley y la costumbre.", "Complementará el ordenamiento con la doctrina de cualquier Tribunal Superior de Justicia.", "Prevalece sobre la costumbre."],
    "Art. 1.6 CC: «complementará»; doctrina reiterada del Tribunal Supremo.", "La jurisprudencia complementará el ordenamiento jurídico con la doctrina que, de modo reiterado, establezca el Tribunal Supremo")
T.q("CC", "a1", "Fuentes", "Según el artículo 1.7 del Código Civil, los Jueces y Tribunales tienen el deber inexcusable de:",
    ["Resolver en todo caso los asuntos de que conozcan, ateniéndose al sistema de fuentes establecido.", "Plantear cuestión de inconstitucionalidad cuando no haya ley aplicable.", "Abstenerse de resolver cuando no exista ley aplicable.", "Resolver conforme a la equidad en defecto de ley."],
    "Art. 1.7 CC.", "Los Jueces y Tribunales tienen el deber inexcusable de resolver en todo caso los asuntos de que conozcan, ateniéndose al sistema de fuentes establecido")
T.q("CE", "Artículo 149", "Fuentes", "Según el artículo 149.1.8.ª de la Constitución, la determinación de las fuentes del Derecho es competencia exclusiva:",
    ["Del Estado, con respeto a las normas de derecho foral o especial.", "De las Comunidades Autónomas con derecho civil propio.", "Compartida entre el Estado y las Comunidades Autónomas.", "Del Estado, sin excepción alguna."],
    "Art. 149.1.8.ª CE.", "determinación de las fuentes del Derecho, con respeto, en este último caso, a las normas de derecho foral o especial")
T.q("CE", "Artículo 96", "Fuentes", "Según el artículo 96.1 de la Constitución, los tratados internacionales válidamente celebrados formarán parte del ordenamiento interno:",
    ["Una vez publicados oficialmente en España.", "Desde su firma por el Jefe del Estado.", "Desde la autorización de las Cortes Generales.", "Una vez ratificados por el Congreso de los Diputados."],
    "Art. 96.1 CE.", "una vez publicados oficialmente en España, formarán parte del ordenamiento interno")
T.q("CE", "Artículo 9", "Constitución", "Según el artículo 9.1 de la Constitución, están sujetos a la Constitución y al resto del ordenamiento jurídico:",
    ["Los ciudadanos y los poderes públicos.", "Solo los poderes públicos.", "Los poderes públicos y las Administraciones Públicas.", "Los españoles y los extranjeros residentes."],
    "Art. 9.1 CE.", "Los ciudadanos y los poderes públicos están sujetos a la Constitución y al resto del ordenamiento jurídico")
T.q("CE", "Artículo 1", "Constitución", "Según el artículo 1.1 de la Constitución, son valores superiores del ordenamiento jurídico:",
    ["La libertad, la justicia, la igualdad y el pluralismo político.", "La libertad, la justicia, la igualdad y la seguridad jurídica.", "La dignidad, la libertad, la igualdad y la solidaridad.", "La libertad, la igualdad, la legalidad y el pluralismo político."],
    "Art. 1.1 CE.", "la libertad, la justicia, la igualdad y el pluralismo político")
T.q("CE", "Artículo 10", "Constitución", "Según el artículo 10.2 de la Constitución, las normas relativas a los derechos fundamentales y a las libertades que la Constitución reconoce se interpretarán de conformidad con:",
    ["La Declaración Universal de Derechos Humanos y los tratados y acuerdos internacionales sobre las mismas materias ratificados por España.", "La jurisprudencia del Tribunal Supremo.", "Los principios generales del derecho.", "Los tratados internacionales firmados por España, aunque no estén ratificados."],
    "Art. 10.2 CE.", "se interpretarán de conformidad con la Declaración Universal de Derechos Humanos y los tratados y acuerdos internacionales sobre las mismas materias ratificados por España")
T.q("CE", "Artículo 103", "Constitución", "Según el artículo 103.1 de la Constitución, la Administración Pública actúa con sometimiento pleno:",
    ["A la ley y al Derecho.", "A la ley y a las instrucciones del Gobierno.", "A la Constitución y a los reglamentos.", "A la ley y a la jurisprudencia."],
    "Art. 103.1 CE.", "con sometimiento pleno a la ley y al Derecho")
T.q("L39", "Artículo 127", "Normas con rango de ley", "Según el artículo 127 de la Ley 39/2015, el Gobierno de la Nación ejercerá la iniciativa legislativa mediante:",
    ["La elaboración y aprobación de los anteproyectos de Ley y la ulterior remisión de los proyectos de ley a las Cortes Generales.", "La aprobación de proposiciones de ley.", "La aprobación de reales decretos legislativos.", "La remisión de anteproyectos de ley al Senado."],
    "Art. 127 Ley 39/2015.", "mediante la elaboración y aprobación de los anteproyectos de Ley y la ulterior remisión de los proyectos de ley a las Cortes Generales")
T.q("CE", "Artículo 97", "Potestad reglamentaria", "Según el artículo 97 de la Constitución, el Gobierno ejerce la potestad reglamentaria:",
    ["De acuerdo con la Constitución y las leyes.", "De acuerdo con las instrucciones de las Cortes Generales.", "Por delegación del Rey.", "Solo en las materias no reservadas a ley orgánica."],
    "Art. 97 CE.", "Ejerce la función ejecutiva y la potestad reglamentaria de acuerdo con la Constitución y las leyes")
T.q("L39", "Artículo 128", "Potestad reglamentaria", "Según el artículo 128.1 de la Ley 39/2015, el ejercicio de la potestad reglamentaria corresponde:",
    ["Al Gobierno de la Nación, a los órganos de Gobierno de las Comunidades Autónomas y a los órganos de gobierno locales.", "Solo al Gobierno de la Nación y a los Ministros.", "Al Gobierno de la Nación y a las Asambleas Legislativas de las Comunidades Autónomas.", "A todos los órganos administrativos en el ámbito de sus competencias."],
    "Art. 128.1 Ley 39/2015.", ["al Gobierno de la Nación, a los órganos de Gobierno de las Comunidades Autónomas", "a los órganos de gobierno locales"])
T.q("LRBRL", "Artículo 4", "Potestad reglamentaria", "Según el artículo 4.1 de la Ley 7/1985, reguladora de las Bases del Régimen Local, corresponden en todo caso a los municipios, las provincias y las islas, dentro de la esfera de sus competencias:",
    ["Las potestades reglamentaria y de autoorganización.", "La potestad legislativa en materia de régimen local.", "La potestad de dictar decretos-leyes en caso de urgencia.", "La potestad reglamentaria, solo por delegación de la Comunidad Autónoma."],
    "Art. 4.1 a) LRBRL.", "Las potestades reglamentaria y de autoorganización")
T.q("CE", "Artículo 9", "Jerarquía", "¿Cuál de los siguientes principios garantiza expresamente el artículo 9.3 de la Constitución?",
    ["La jerarquía normativa.", "La primacía del Derecho de la Unión Europea.", "La reserva de ley orgánica.", "La autonomía de las Comunidades Autónomas."],
    "Art. 9.3 CE: legalidad, jerarquía normativa, publicidad de las normas, irretroactividad…, seguridad jurídica, responsabilidad e interdicción de la arbitrariedad.", "la jerarquía normativa")
T.q("CE", "Artículo 9", "Jerarquía", "Según el artículo 9.3 de la Constitución, se garantiza la irretroactividad de:",
    ["Las disposiciones sancionadoras no favorables o restrictivas de derechos individuales.", "Todas las disposiciones de carácter general.", "Las disposiciones sancionadoras, sean o no favorables.", "Las leyes tributarias."],
    "Art. 9.3 CE.", "la irretroactividad de las disposiciones sancionadoras no favorables o restrictivas de derechos individuales")
T.q("L39", "Artículo 128", "Jerarquía", "Según el artículo 128.3 de la Ley 39/2015, las disposiciones administrativas se ajustarán al orden de jerarquía que establezcan:",
    ["Las leyes.", "Los propios reglamentos.", "Los Estatutos de Autonomía.", "Las Órdenes del Ministro de la Presidencia."],
    "Art. 128.3 Ley 39/2015.", "Las disposiciones administrativas se ajustarán al orden de jerarquía que establezcan las leyes")
T.q("LGOB", "a24", "Jerarquía", "Según el artículo 24.2 de la Ley 50/1997, del Gobierno, los reglamentos se ordenarán según la siguiente jerarquía:",
    ["1.º Disposiciones aprobadas por Real Decreto del Presidente del Gobierno o acordado en el Consejo de Ministros; 2.º Disposiciones aprobadas por Orden Ministerial.", "1.º Real Decreto acordado en Consejo de Ministros; 2.º Real Decreto del Presidente del Gobierno; 3.º Orden Ministerial.", "1.º Orden del Ministro de la Presidencia; 2.º Órdenes Ministeriales; 3.º Reales Decretos.", "1.º Acuerdos del Consejo de Ministros; 2.º Reales Decretos; 3.º Órdenes Ministeriales."],
    "Art. 24.2 Ley 50/1997: dos escalones.", ["Disposiciones aprobadas por Real Decreto del Presidente del Gobierno o acordado en el Consejo de Ministros", "Disposiciones aprobadas por Orden Ministerial"])
T.q("LGOB", "a24", "Jerarquía", "Según el artículo 24.1 de la Ley 50/1997, del Gobierno, ¿qué forma revisten las disposiciones y resoluciones de los Ministros?",
    ["Órdenes Ministeriales.", "Reales Decretos.", "Acuerdos del Consejo de Ministros.", "Resoluciones ministeriales."],
    "Art. 24.1 f) Ley 50/1997.", "Órdenes Ministeriales, las disposiciones y resoluciones de los Ministros")
T.q("LGOB", "a24", "Jerarquía", "Según el artículo 24.1 f) de la Ley 50/1997, cuando la disposición o resolución afecte a varios Departamentos revestirá la forma de:",
    ["Orden del Ministro de la Presidencia, dictada a propuesta de los Ministros interesados.", "Real Decreto acordado en Consejo de Ministros.", "Orden conjunta firmada por todos los Ministros interesados.", "Acuerdo de la Comisión General de Secretarios de Estado y Subsecretarios."],
    "Art. 24.1 f) Ley 50/1997.", "revestirá la forma de Orden del Ministro de la Presidencia, dictada a propuesta de los Ministros interesados")
T.q("LGOB", "a24", "Jerarquía", "Según el artículo 24.1 c) de la Ley 50/1997, las decisiones que aprueben normas reglamentarias de la competencia del Consejo de Ministros revisten la forma de:",
    ["Reales Decretos acordados en Consejo de Ministros.", "Acuerdos del Consejo de Ministros.", "Reales Decretos del Presidente del Gobierno.", "Órdenes Ministeriales."],
    "Art. 24.1 c) Ley 50/1997.", "Reales Decretos acordados en Consejo de Ministros, las decisiones que aprueben normas reglamentarias de la competencia de éste")
T.q("L39", "Artículo 128", "Ley y reglamento", "Según el artículo 128.2 de la Ley 39/2015, los reglamentos y disposiciones administrativas, sin perjuicio de su función de desarrollo o colaboración con respecto a la ley, no podrán:",
    ["Tipificar delitos, faltas o infracciones administrativas, ni establecer penas o sanciones.", "Desarrollar los preceptos de una ley.", "Regular la organización interna de la Administración.", "Fijar los modelos de solicitud de los procedimientos."],
    "Art. 128.2 Ley 39/2015.", "no podrán tipificar delitos, faltas o infracciones administrativas, establecer penas o sanciones")
T.q("L39", "Artículo 47", "Ley y reglamento", "Según el artículo 47.2 de la Ley 39/2015, las disposiciones administrativas que regulen materias reservadas a la Ley son:",
    ["Nulas de pleno derecho.", "Anulables.", "Válidas hasta que se apruebe la ley.", "Irregulares no invalidantes."],
    "Art. 47.2 Ley 39/2015.", "También serán nulas de pleno derecho las disposiciones administrativas que vulneren la Constitución, las leyes u otras disposiciones administrativas de rango superior, las que regulen materias reservadas a la Ley")
T.q("L39", "Artículo 37", "Ley y reglamento", "Según el artículo 37.1 de la Ley 39/2015, las resoluciones administrativas de carácter particular no podrán vulnerar lo establecido en una disposición de carácter general:",
    ["Aunque procedan de un órgano de igual o superior jerarquía al que dictó la disposición general.", "Salvo que procedan de un órgano superior al que dictó la disposición general.", "Salvo que lo autorice expresamente el Consejo de Ministros.", "Salvo que la resolución sea favorable al interesado."],
    "Art. 37.1 Ley 39/2015 (inderogabilidad singular).", "aunque aquéllas procedan de un órgano de igual o superior jerarquía al que dictó la disposición general")
T.q("CE", "Artículo 106", "Control", "Según el artículo 106.1 de la Constitución, controlan la potestad reglamentaria y la legalidad de la actuación administrativa:",
    ["Los Tribunales.", "Las Cortes Generales.", "El Consejo de Estado.", "El Defensor del Pueblo."],
    "Art. 106.1 CE.", "Los Tribunales controlan la potestad reglamentaria")
T.q("CE", "Artículo 149", "Competencia", "Según el artículo 149.3 de la Constitución, el derecho estatal será, respecto del derecho de las Comunidades Autónomas:",
    ["En todo caso, supletorio.", "Siempre prevalente.", "Supletorio solo en las materias de competencia compartida.", "Aplicable solo si la Comunidad Autónoma lo acepta."],
    "Art. 149.3 CE.", "El derecho estatal será, en todo caso, supletorio del derecho de las Comunidades Autónomas")
T.q("CE", "Artículo 149", "Competencia", "Según el artículo 149.3 de la Constitución, las normas del Estado prevalecerán, en caso de conflicto, sobre las de las Comunidades Autónomas:",
    ["En todo lo que no esté atribuido a la exclusiva competencia de éstas.", "En todo caso.", "Solo en las materias del artículo 149.1.", "Cuando sean leyes orgánicas."],
    "Art. 149.3 CE.", "cuyas normas prevalecerán, en caso de conflicto, sobre las de las Comunidades Autónomas en todo lo que no esté atribuido a la exclusiva competencia de éstas")
T.q("L39", "Artículo 129", "Buena regulación", "Según el artículo 129.1 de la Ley 39/2015, en el ejercicio de la iniciativa legislativa y la potestad reglamentaria, las Administraciones Públicas actuarán de acuerdo con los principios de:",
    ["Necesidad, eficacia, proporcionalidad, seguridad jurídica, transparencia y eficiencia.", "Legalidad, jerarquía, publicidad, irretroactividad, seguridad jurídica y responsabilidad.", "Eficacia, jerarquía, descentralización, desconcentración y coordinación.", "Necesidad, oportunidad, legalidad, transparencia y participación."],
    "Art. 129.1 Ley 39/2015.", "necesidad, eficacia, proporcionalidad, seguridad jurídica, transparencia, y eficiencia")
T.q("L39", "Artículo 129", "Buena regulación", "Según el artículo 129.3 de la Ley 39/2015, en virtud del principio de proporcionalidad, la iniciativa que se proponga deberá contener:",
    ["La regulación imprescindible para atender la necesidad a cubrir con la norma.", "La regulación más completa posible de la materia.", "Una cuantificación de sus repercusiones en los gastos públicos.", "Un listado de las normas que quedan derogadas."],
    "Art. 129.3 Ley 39/2015.", "la iniciativa que se proponga deberá contener la regulación imprescindible para atender la necesidad a cubrir con la norma")
T.q("L39", "Artículo 129", "Buena regulación", "Según el artículo 129.6 de la Ley 39/2015, en aplicación del principio de eficiencia, la iniciativa normativa debe:",
    ["Evitar cargas administrativas innecesarias o accesorias y racionalizar, en su aplicación, la gestión de los recursos públicos.", "Contener la regulación imprescindible para atender la necesidad a cubrir.", "Ejercerse de manera coherente con el resto del ordenamiento jurídico.", "Estar justificada por una razón de interés general."],
    "Art. 129.6 Ley 39/2015. Las demás opciones son proporcionalidad (129.3), seguridad jurídica (129.4) y necesidad y eficacia (129.2).", "la iniciativa normativa debe evitar cargas administrativas innecesarias o accesorias y racionalizar, en su aplicación, la gestión de los recursos públicos")
T.q("L39", "Artículo 129", "Buena regulación", "Según el artículo 129.4 de la Ley 39/2015, las habilitaciones para el desarrollo reglamentario de una ley serán conferidas, con carácter general:",
    ["Al Gobierno.", "A los titulares de los departamentos ministeriales.", "A las Autoridades Independientes.", "A la Comisión General de Secretarios de Estado y Subsecretarios."],
    "Art. 129.4 Ley 39/2015: con carácter general, al Gobierno; la atribución directa a los Ministros es excepcional.", "Las habilitaciones para el desarrollo reglamentario de una ley serán conferidas, con carácter general, al Gobierno")
T.q("L39", "Artículo 131", "Publicidad", "Según el artículo 131 de la Ley 39/2015, para que entren en vigor y produzcan efectos jurídicos, las normas con rango de ley, los reglamentos y disposiciones administrativas habrán de publicarse:",
    ["En el diario oficial correspondiente.", "En el tablón de anuncios del órgano que las dicte.", "En el Portal de la Transparencia.", "En la sede electrónica del Ministerio proponente."],
    "Art. 131 Ley 39/2015.", "habrán de publicarse en el diario oficial correspondiente para que entren en vigor y produzcan efectos jurídicos")
T.q("CC", "art2", "Publicidad", "Según el artículo 2.1 del Código Civil, las leyes entrarán en vigor, si en ellas no se dispone otra cosa:",
    ["A los veinte días de su completa publicación en el «Boletín Oficial del Estado».", "Al día siguiente de su publicación en el «Boletín Oficial del Estado».", "A los quince días de su sanción.", "A los veinte días de su aprobación por las Cortes Generales."],
    "Art. 2.1 CC.", "Las leyes entrarán en vigor a los veinte días de su completa publicación en el «Boletín Oficial del Estado», si en ellas no se dispone otra cosa")
T.q("L39", "Artículo 132", "Planificación", "Según el artículo 132 de la Ley 39/2015, el Plan Anual Normativo contendrá las iniciativas legales o reglamentarias que vayan a ser elevadas para su aprobación:",
    ["En el año siguiente.", "En el año en curso.", "Durante la legislatura.", "En los dos años siguientes."],
    "Art. 132.1 Ley 39/2015.", "que vayan a ser elevadas para su aprobación en el año siguiente")
T.q("L39", "Artículo 132", "Planificación", "Según el artículo 132.2 de la Ley 39/2015, una vez aprobado, el Plan Anual Normativo se publicará:",
    ["En el Portal de la Transparencia de la Administración Pública correspondiente.", "En el «Boletín Oficial del Estado».", "En el Boletín Oficial de las Cortes Generales.", "En la sede electrónica del Ministerio de la Presidencia."],
    "Art. 132.2 Ley 39/2015.", "el Plan Anual Normativo se publicará en el Portal de la Transparencia de la Administración Pública correspondiente")
T.q("LGOB", "a25", "Planificación", "Según el artículo 25.4 de la Ley 50/1997, el Ministro de la Presidencia elevará el Plan Anual Normativo al Consejo de Ministros para su aprobación:",
    ["Antes del 30 de abril.", "Antes del 31 de diciembre.", "Antes del 30 de junio.", "Antes del 1 de marzo."],
    "Art. 25.4 Ley 50/1997.", "El Ministro de la Presidencia elevará el Plan al Consejo de Ministros para su aprobación antes del 30 de abril")
T.q("L39", "Artículo 133", "Participación", "Según el artículo 133.1 de la Ley 39/2015, la consulta pública previa a la elaboración del proyecto o anteproyecto de ley o de reglamento se sustanciará:",
    ["A través del portal web de la Administración competente.", "Mediante anuncio en el «Boletín Oficial del Estado».", "Ante el Consejo de Estado.", "Mediante audiencia a las Cortes Generales."],
    "Art. 133.1 Ley 39/2015.", "se sustanciará una consulta pública, a través del portal web de la Administración competente")
T.q("L39", "Artículo 133", "Participación", "¿Cuál de los siguientes aspectos NO figura entre aquellos sobre los que se recaba opinión en la consulta pública del artículo 133.1 de la Ley 39/2015?",
    ["El coste de personal de la futura norma.", "Los problemas que se pretenden solucionar con la iniciativa.", "La necesidad y oportunidad de su aprobación.", "Las posibles soluciones alternativas regulatorias y no regulatorias."],
    "Art. 133.1 Ley 39/2015: problemas, necesidad y oportunidad, objetivos y soluciones alternativas.", ["Los problemas que se pretenden solucionar con la iniciativa", "La necesidad y oportunidad de su aprobación", "Las posibles soluciones alternativas regulatorias y no regulatorias"])
T.q("L39", "Artículo 133", "Participación", "Según el artículo 133.4 de la Ley 39/2015, podrá omitirse solo la consulta pública del apartado primero cuando la propuesta normativa:",
    ["No tenga un impacto significativo en la actividad económica.", "Afecte a los derechos e intereses legítimos de las personas.", "Imponga obligaciones relevantes a los destinatarios.", "Regule de forma completa una materia."],
    "Art. 133.4, párrafo segundo, Ley 39/2015.", "Cuando la propuesta normativa no tenga un impacto significativo en la actividad económica")
T.q(STC, "preambulo", "STC 55/2018", "Según el fallo de la STC 55/2018, los artículos 132 y 133 de la Ley 39/2015 (con las salvedades del 133):",
    ["Son contrarios al orden constitucional de competencias.", "Son inconstitucionales y nulos.", "No son inconstitucionales interpretados conforme a la sentencia.", "Fueron declarados conformes a la Constitución en su integridad."],
    "Fallo de la STC 55/2018 (2.º y 3.º): contrarios al orden constitucional de competencias, sin nulidad.", "Declarar que el artículo 132 y el artículo 133, salvo el inciso de su apartado primero")
T.real("L", 46, "Fuentes"); T.real("L", 48, "Participación")

# Flashcards
for q_, a_, cat in [
  ("Fuentes del ordenamiento jurídico español (CC 1.1)", "La ley, la costumbre y los principios generales del derecho.", "Fuentes"),
  ("¿A quién corresponde la determinación de las fuentes del Derecho? (CE 149.1.8.ª)", "Al Estado (competencia exclusiva), con respeto a las normas de derecho foral o especial.", "Fuentes"),
  ("Requisitos de la costumbre (CC 1.3)", "En defecto de ley aplicable, no contraria a la moral o al orden público y probada.", "Fuentes"),
  ("Papel de los principios generales del derecho (CC 1.4)", "Se aplican en defecto de ley o costumbre, sin perjuicio de su carácter informador del ordenamiento.", "Fuentes"),
  ("¿Cuándo se aplican directamente las normas de los tratados? (CC 1.5)", "Cuando hayan pasado a formar parte del ordenamiento interno mediante su publicación íntegra en el BOE.", "Fuentes"),
  ("Jurisprudencia (CC 1.6)", "Complementa el ordenamiento con la doctrina que, de modo reiterado, establezca el Tribunal Supremo al interpretar y aplicar la ley, la costumbre y los principios generales.", "Fuentes"),
  ("Valores superiores del ordenamiento (CE 1.1)", "La libertad, la justicia, la igualdad y el pluralismo político.", "Constitución"),
  ("Garantías del art. 9.3 CE", "Legalidad, jerarquía normativa, publicidad de las normas, irretroactividad de las disposiciones sancionadoras no favorables o restrictivas de derechos individuales, seguridad jurídica, responsabilidad e interdicción de la arbitrariedad.", "Jerarquía"),
  ("Disposición que contradice otra de rango superior (CC 1.2)", "Carece de validez.", "Jerarquía"),
  ("Titulares de la potestad reglamentaria (Ley 39/2015, 128.1)", "Gobierno de la Nación, órganos de Gobierno de las CC. AA. y órganos de gobierno locales.", "Potestad reglamentaria"),
  ("Jerarquía de los reglamentos del Estado (Ley 50/1997, 24.2)", "1.º Real Decreto del Presidente del Gobierno o acordado en Consejo de Ministros; 2.º Orden Ministerial.", "Jerarquía"),
  ("Forma de las disposiciones que afectan a varios Departamentos (Ley 50/1997, 24.1 f)", "Orden del Ministro de la Presidencia, a propuesta de los Ministros interesados.", "Jerarquía"),
  ("Disposiciones administrativas nulas de pleno derecho (Ley 39/2015, 47.2)", "Las que vulneren la CE, las leyes u otras disposiciones de rango superior, regulen materias reservadas a la Ley o establezcan la retroactividad de disposiciones sancionadoras no favorables o restrictivas de derechos individuales.", "Jerarquía"),
  ("Inderogabilidad singular (Ley 39/2015, 37)", "Las resoluciones particulares no pueden vulnerar una disposición general, aunque procedan de órgano de igual o superior jerarquía; si lo hacen, son nulas.", "Jerarquía"),
  ("Art. 149.3 CE: prevalencia y supletoriedad", "Las normas del Estado prevalecen en lo no atribuido a la exclusiva competencia autonómica; el derecho estatal es, en todo caso, supletorio.", "Competencia"),
  ("Principios de buena regulación (Ley 39/2015, 129.1)", "Necesidad, eficacia, proporcionalidad, seguridad jurídica, transparencia y eficiencia.", "Buena regulación"),
  ("¿A quién se confieren con carácter general las habilitaciones para el desarrollo reglamentario? (129.4)", "Al Gobierno; la atribución directa a un Ministro es excepcional y se justifica en la ley habilitante.", "Buena regulación"),
  ("Requisito para que una norma entre en vigor (Ley 39/2015, 131)", "Su publicación en el diario oficial correspondiente.", "Publicidad"),
  ("Plan Anual Normativo (Ley 39/2015, 132; Ley 50/1997, 25)", "Iniciativas del año siguiente; se publica en el Portal de la Transparencia; en el Estado se eleva al Consejo de Ministros antes del 30 de abril.", "Planificación"),
  ("¿Cuándo puede prescindirse de consulta, audiencia e información públicas? (133.4)", "Normas presupuestarias u organizativas de las Administraciones o sus organizaciones dependientes o vinculadas, o razones graves de interés público.", "Participación"),
  ("STC 55/2018: efecto sobre los arts. 129, 130, 132 y 133 Ley 39/2015", "Contrarios al orden constitucional de competencias (inaplicables en parte a las CC. AA.), sin nulidad; nulos dos incisos del 129.4.", "STC 55/2018"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Fuentes del ordenamiento", "Según el art. 1.1 del Código Civil: la ley, la costumbre y los principios generales del derecho.", "s1", "Fuentes")
T.glos("Costumbre", "Fuente que rige en defecto de ley aplicable, si no es contraria a la moral o al orden público y resulta probada (CC 1.3).", "s1", "Fuentes")
T.glos("Jurisprudencia", "Doctrina que, de modo reiterado, establece el Tribunal Supremo al interpretar y aplicar ley, costumbre y principios generales; complementa el ordenamiento (CC 1.6).", "s1", "Fuentes")
T.glos("Valores superiores", "Libertad, justicia, igualdad y pluralismo político, que propugna el Estado social y democrático de Derecho (CE 1.1).", "s2", "Constitución")
T.glos("Potestad reglamentaria", "Facultad de dictar reglamentos; la ejercen el Gobierno de la Nación, los órganos de Gobierno autonómicos y los órganos de gobierno locales (CE 97; Ley 39/2015, 128.1).", "s4", "Potestad reglamentaria")
T.glos("Jerarquía normativa", "Garantía constitucional (CE 9.3) por la que la norma que contradice otra de rango superior carece de validez (CC 1.2).", "s6", "Jerarquía")
T.glos("Orden Ministerial", "Forma de las disposiciones y resoluciones de los Ministros; segundo escalón de la jerarquía de los reglamentos estatales (Ley 50/1997, 24.1 f y 24.2).", "s7", "Jerarquía")
T.glos("Inderogabilidad singular", "Regla por la que una resolución particular no puede vulnerar una disposición general, aunque proceda de órgano de igual o superior jerarquía (Ley 39/2015, 37). Expresión de la rúbrica del artículo.", "s8", "Jerarquía")
T.glos("Supletoriedad del derecho estatal", "El derecho estatal será, en todo caso, supletorio del derecho de las Comunidades Autónomas (CE 149.3).", "s10", "Competencia")
T.glos("Principios de buena regulación", "Necesidad, eficacia, proporcionalidad, seguridad jurídica, transparencia y eficiencia (Ley 39/2015, 129.1).", "s11", "Buena regulación")
T.glos("Plan Anual Normativo", "Plan que recoge las iniciativas legales o reglamentarias que se elevarán para su aprobación el año siguiente (Ley 39/2015, 132; Ley 50/1997, 25).", "s12", "Planificación")
T.glos("Consulta pública", "Trámite previo a la elaboración del proyecto o anteproyecto de ley o de reglamento, a través del portal web, sobre problemas, necesidad y oportunidad, objetivos y alternativas (Ley 39/2015, 133.1).", "s13", "Participación")

# Cronología (fechas de los metadatos del BOE)
T.hito("1889", "Real Decreto de 24 de julio de 1889 por el que se publica el Código Civil (Gaceta de Madrid de 25-7-1889)", "Código Civil: art. 1 sobre las fuentes", "normativo", "s1")
T.hito("1974", "Decreto 1836/1974, de 31 de mayo, texto articulado del título preliminar del Código Civil (BOE de 9-7-1974)", "Redacción vigente del art. 1 del Código Civil", "normativo", "s1")
T.hito("1978", "Constitución Española (27-12-1978; BOE de 29-12-1978)", "Arts. 9.3 (jerarquía normativa), 97 (potestad reglamentaria) y 149.1.8.ª (fuentes del Derecho)", "normativo", "s6")
T.hito("1985", "Ley 7/1985, de 2 de abril, reguladora de las Bases del Régimen Local (BOE de 3-4-1985)", "Art. 4.1 a): potestad reglamentaria de los entes locales", "normativo", "s4")
T.hito("1997", "Ley 50/1997, de 27 de noviembre, del Gobierno (BOE de 28-11-1997)", "Art. 24: forma y jerarquía de las disposiciones del Gobierno", "normativo", "s7")
T.hito("2015", "Leyes 39/2015 y 40/2015, de 1 de octubre (BOE de 2-10-2015)", "Ley 39/2015, Título VI (arts. 127 a 133): iniciativa legislativa y potestad reglamentaria", "normativo", "s11")
T.hito("2018", "Sentencia del Tribunal Constitucional 55/2018, de 24 de mayo (BOE de 22-6-2018)", "Alcance de los arts. 129 a 133 de la Ley 39/2015", "jurisprudencia", "s14")

T.publicar()
