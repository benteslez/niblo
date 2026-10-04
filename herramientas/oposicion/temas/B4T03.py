# -*- coding: utf-8 -*-
"""Tema IV.3 (B4T03): El reglamento: concepto, clases y límites. Los principios generales
del Derecho. Los tratados internacionales.
Método del I.2: mapa → bloques (I a V) con guía; cada artículo, texto literal del BOE +
ficha de casillas fijas; cierre 1 (preguntas oficiales) y cierre 2 (repaso).
Normas (textos consolidados del BOE): CE (arts. 9.3, 63.2, 74.2, 93 a 97, 106.1, 153);
Ley 50/1997, del Gobierno (arts. 4, 5, 22 a 26); Ley 39/2015 (arts. 37, 47.2, 128 a 133,
con la nota del BOE sobre la STC 55/2018); LO 3/1980, del Consejo de Estado (art. 22);
Ley 7/1985 (art. 4.1 a); LJCA (arts. 1.1, 26 y 27); Código Civil (art. 1); LOTC (arts. 27.2
y 78); Ley 25/2014, de Tratados y otros Acuerdos Internacionales."""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *
from plantilla import _norm, AQUI

CORTO["L25_2014"] = "Ley 25/2014, de Tratados"
CORTO["LRBRL"] = "Ley 7/1985 (LRBRL)"


def nota(k, bloque, frag):
    """Nota del BOE al texto consolidado (no es texto legal): se comprueba literal en el XML."""
    s = open(os.path.join(AQUI, "boe", k + ".xml"), encoding="utf-8").read()
    i = s.find(f'<bloque id="{bloque}"'); j = s.find("</bloque>", i)
    notas = [" ".join(re.sub(r"<[^>]+>", "", m).split()) for m in re.findall(r'<p class="nota_pie"[^>]*>(.*?)</p>', s[i:j], re.S)]
    assert any(_norm(frag) in _norm(x) for x in notas), ("NOTA DEL BOE NO LITERAL", k, bloque, frag)
    return frag


T = Tema("B4T03",
  "Cinco preguntas: I. Qué es el reglamento y quién lo dicta (art. 97 CE; Ley 39/2015, art. 128.1; Ley 50/1997) · II. Qué clases hay: forma, jerarquía y relación con la ley (Ley 50/1997, art. 24; LO 3/1980, art. 22) · III. Qué límites tiene y cómo se controla (Ley 39/2015, arts. 37, 47.2 y 128 a 133; Ley 50/1997, arts. 23, 25 y 26; art. 106.1 CE; LJCA) · IV. Qué son los principios generales del Derecho (Código Civil, art. 1; art. 9.3 CE) · V. Cómo se celebra un tratado y cómo entra en el ordenamiento (arts. 93 a 96 CE; Código Civil, art. 1.5; Ley 25/2014). Cada artículo: texto literal del BOE y ficha.",
  ["Potestad reglamentaria", "Art. 97 CE", "Art. 128 LPAC", "Real Decreto", "Orden Ministerial", "Jerarquía", "Reglamento ejecutivo", "Inderogabilidad singular", "Nulidad de disposiciones", "Buena regulación", "Recurso indirecto", "Principios generales del Derecho", "Art. 1 CC", "Tratados", "Arts. 93-96 CE", "Ley 25/2014", "Control previo"])

# =============================================================================
T.ap("s0", "Mapa del tema: cinco preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque IV, tema 3):
> El reglamento: concepto, clases y límites. Los principios generales del Derecho. Los tratados internacionales.

### El hilo conductor

El epígrafe se lee como **cinco preguntas encadenadas**: tres sobre el reglamento (concepto, clases y límites), una sobre los principios generales del Derecho y una sobre los tratados. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Constitución | Otras normas |
|---|---|---|---|
| **I** | ¿Qué es el reglamento y quién lo dicta? (concepto) | Art. 97 | Ley 50/1997, arts. 4.1 b), 5.1 h) y 22; Ley 39/2015, art. 128.1; Ley 7/1985, art. 4.1 a) |
| **II** | ¿Qué clases de reglamentos hay? (clases) | — | Ley 50/1997, art. 24; Ley 39/2015, art. 128.3; LO 3/1980, art. 22; Ley 39/2015, art. 129.4 |
| **III** | ¿Qué límites tiene y cómo se controla? (límites) | Arts. 106.1 y 153 c) | Ley 39/2015, arts. 37, 47.2, 128.2, 129 a 133; Código Civil, art. 1.2; Ley 50/1997, arts. 23, 25 y 26; LJCA, arts. 1.1, 26 y 27 |
| **IV** | ¿Qué son los principios generales del Derecho? | Art. 9.3 | Código Civil, art. 1 (apartados 1, 3, 4, 6 y 7) |
| **V** | ¿Cómo se celebra un tratado y cómo entra en el ordenamiento? | Arts. 63.2, 74.2, 93 a 96 | Ley 25/2014, de Tratados; Código Civil, art. 1.5; LOTC, arts. 27.2 c) y 78 |

!> **La idea que une los cinco bloques:** el **reglamento** es la norma que dicta la **Administración** (el Gobierno, las Comunidades Autónomas y los entes locales) con **rango inferior a la ley** (I); según quién lo apruebe adopta una forma y ocupa un lugar en la **jerarquía** (II); por eso **no puede** contradecir la ley ni entrar en lo reservado a ella, y los **Tribunales** lo controlan (III). Las otras dos fuentes del epígrafe se sitúan respecto de la ley: los **principios generales del Derecho** se aplican **en defecto de ley o costumbre** (IV), y los **tratados** forman parte del ordenamiento interno **una vez publicados** y prevalecen sobre las normas internas salvo las constitucionales (V).

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- Lo que el BOE añade en **notas** al texto consolidado (por ejemplo, el efecto de la STC 55/2018 sobre la Ley 39/2015) va aparte, señalado como nota del BOE.
- La ley, el decreto-ley y el decreto legislativo son el tema IV.2; las fuentes y la jerarquía en general, el tema IV.1; el Derecho de la Unión Europea, el bloque II.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué es el reglamento y quién lo dicta? (art. 97 CE; Ley 39/2015, art. 128.1)", donde(
  "Primera pregunta del tema. La Constitución no define el reglamento: atribuye al Gobierno la **potestad reglamentaria** «de acuerdo con la Constitución y las leyes». La Ley 39/2015 dice **quién más** la tiene.",
  ["1 La potestad reglamentaria del Gobierno (art. 97 CE; Ley 50/1997, art. 22)", "2 Los titulares de la potestad reglamentaria (Ley 39/2015, art. 128.1; Ley 50/1997, arts. 4 y 5; Ley 7/1985, art. 4)"]))

T.ap("s1", "I.1 La potestad reglamentaria del Gobierno (art. 97 CE; Ley 50/1997, art. 22)", f"""
El reglamento es una norma **escrita** que dicta la **Administración** en ejercicio de la potestad reglamentaria. Su rango es **inferior a la ley**: lo demuestra que la jurisdicción contencioso-administrativa conoce de las {c('LJCA', 'Artículo 1', 'disposiciones generales de rango inferior a la Ley')} (→ III.4.3).

{unidad("1.1 El Gobierno ejerce la potestad reglamentaria (art. 97)",
  lit("CE", "Artículo 97", ["Ejerce la función ejecutiva y la potestad reglamentaria de acuerdo con la Constitución y las leyes"]),
  fichab("Atribución constitucional de la potestad reglamentaria",
         c("CE", "Artículo 97", "El Gobierno"),
         f"{c('CE', 'Artículo 97', 'de acuerdo con la Constitución y las leyes')}",
         "—",
         "La potestad reglamentaria se ejerce **de acuerdo con la Constitución y las leyes**: por debajo de ambas. El art. 97 la atribuye al **Gobierno** (no al Rey ni a las Cortes)."))}

{unidad("1.2 Remisión a la Ley 39/2015 (Ley 50/1997, art. 22)",
  lit("LGOB", "a22", ["de conformidad con los principios y reglas establecidos en el Título VI de la Ley 39/2015"]),
  fichab("Reglas a las que se sujeta la potestad reglamentaria del Gobierno",
         c("LGOB", "a22", "El Gobierno"),
         "Con los principios y reglas del **Título VI de la Ley 39/2015** (arts. 127 a 133, → III.2) y del Título V de la Ley 50/1997 (arts. 22 a 28, → III.3)",
         "—",
         "El Título de la Ley 39/2015 al que se remite es el **VI** (iniciativa legislativa y potestad reglamentaria)."))}
""", 2)

T.ap("s2", "I.2 Los titulares de la potestad reglamentaria (Ley 39/2015, art. 128.1; Ley 50/1997, arts. 4 y 5; Ley 7/1985, art. 4)", f"""
{unidad("2.1 Gobierno, Comunidades Autónomas y entes locales (Ley 39/2015, art. 128.1)",
  lit("L39", "Artículo 128", ["al Gobierno de la Nación", "a los órganos de Gobierno de las Comunidades Autónomas", "a los órganos de gobierno locales"], solo=[1]),
  fichab("Quién dicta reglamentos",
         ["Gobierno de la Nación", "Órganos de Gobierno de las Comunidades Autónomas, según sus Estatutos", "Órganos de gobierno locales, según la Constitución, los Estatutos y la Ley 7/1985"],
         "—",
         "—",
         "Son **tres** niveles: Estado, Comunidades Autónomas y entes locales. Para las Comunidades, «de conformidad con lo establecido en sus respectivos **Estatutos**»."))}

{unidad("2.2 Consejo de Ministros y Ministros (Ley 50/1997, arts. 5.1 h) y 4.1 b)",
  lit("LGOB", "a5", ["Aprobar los reglamentos para el desarrollo y la ejecución de las leyes, previo dictamen del Consejo de Estado"], solo=[1, 9], titulo="Artículo 5.1 h) (Ley 50/1997, del Gobierno)"),
  lit("LGOB", "a4", ["Ejercer la potestad reglamentaria en las materias propias de su Departamento"], solo=[1, 3], titulo="Artículo 4.1 b) (Ley 50/1997, del Gobierno)"),
  fichab("Reparto de la potestad reglamentaria dentro del Gobierno",
         ["**Consejo de Ministros**: reglamentos de desarrollo y ejecución de las leyes y demás disposiciones reglamentarias que procedan", "**Ministros**: en las materias propias de su Departamento"],
         "Los reglamentos de desarrollo y ejecución de las leyes, **previo dictamen del Consejo de Estado** (→ II.2.1)",
         "—",
         "El **dictamen del Consejo de Estado** se exige para los reglamentos **para el desarrollo y la ejecución de las leyes**. El Ministro solo en las materias **de su Departamento**."))}

{unidad("2.3 Municipios, provincias e islas (Ley 7/1985, art. 4.1 a)",
  lit("LRBRL", "Artículo 4", ["Las potestades reglamentaria y de autoorganización"], solo=[1, 2], titulo="Artículo 4.1 a) (Ley 7/1985, reguladora de las Bases del Régimen Local)"),
  fichab("Potestad reglamentaria de las entidades locales territoriales",
         f"{c('LRBRL', 'Artículo 4', 'los municipios, las provincias y las islas')}",
         f"{c('LRBRL', 'Artículo 4', 'dentro de la esfera de sus competencias')}; corresponde {c('LRBRL', 'Artículo 4', 'en todo caso')}",
         "Las ordenanzas locales se aprueban por el Pleno, con información pública de **treinta días** como mínimo (Ley 7/1985, art. 49)",
         f"La tienen municipios, provincias e **islas**: {c('LRBRL', 'Artículo 4', 'En su calidad de Administraciones públicas de carácter **territorial**')}."))}

{resumen([
  "La potestad reglamentaria es del **Gobierno** «de acuerdo con la Constitución y las leyes» (97 CE), con las reglas del Título VI de la Ley 39/2015 (Ley 50/1997, art. 22).",
  "Titulares (Ley 39/2015, art. 128.1): **Gobierno de la Nación**, **órganos de Gobierno de las CC. AA.** y **órganos de gobierno locales**.",
  "Consejo de Ministros: reglamentos de desarrollo y ejecución de las leyes, **previo dictamen del Consejo de Estado** (5.1 h); Ministros: materias **de su Departamento** (4.1 b)."],
  "Siguiente: II. ¿Qué clases de reglamentos hay?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Qué clases de reglamentos hay? Forma, jerarquía y relación con la ley", donde(
  "Segunda pregunta. Las normas clasifican los reglamentos por **quién** los aprueba (y la **forma** que toman), por su lugar en la **jerarquía** y por su **relación con la ley** (los que se dictan «en ejecución de las Leyes»).",
  ["1 Forma y jerarquía de los reglamentos del Gobierno (Ley 50/1997, art. 24; Ley 39/2015, art. 128.3)", "2 Reglamentos ejecutivos y habilitaciones (LO 3/1980, art. 22; Ley 39/2015, art. 129.4)", "3 Cuadro de las clases de reglamentos"]))

T.ap("s3", "II.1 Forma y jerarquía de los reglamentos del Gobierno (Ley 50/1997, art. 24; Ley 39/2015, art. 128.3)", f"""
{unidad("1.1 Formas de las decisiones del Gobierno y de sus miembros (Ley 50/1997, art. 24.1)",
  lit("LGOB", "a24", ["Reales Decretos acordados en Consejo de Ministros, las decisiones que aprueben normas reglamentarias", "Órdenes Ministeriales, las disposiciones y resoluciones de los Ministros"], solo=[1, 2, 3, 4, 5, 6, 7]),
  fichab("Forma jurídica de cada decisión del Gobierno",
         "Presidente del Gobierno, Consejo de Ministros, Comisiones Delegadas y Ministros",
         ["Normas con rango de ley (arts. 82 y 86 CE): **Reales Decretos Legislativos** y **Reales Decretos-leyes** (tema IV.2)", "Del Presidente: **Reales Decretos del Presidente del Gobierno**", "Reglamentos del Consejo de Ministros: **Reales Decretos acordados en Consejo de Ministros**", "Lo demás del Consejo de Ministros: **Acuerdos del Consejo de Ministros**", "Comisiones Delegadas: acuerdos con forma de **Orden** del Ministro competente o del de la Presidencia", "Ministros: **Órdenes Ministeriales**; si afecta a varios Departamentos, Orden del Ministro de la Presidencia"],
         "—",
         "Las decisiones del Consejo de Ministros que **no** deban ser Real Decreto son **Acuerdos del Consejo de Ministros** (pregunta oficial P 49, → Cierre 1)."))}

{unidad("1.2 Jerarquía de los reglamentos (Ley 50/1997, art. 24.2)",
  lit("LGOB", "a24", ["Los reglamentos se ordenarán según la siguiente jerarquía"], solo=[8, 9, 10]),
  fichab("Orden jerárquico de los reglamentos del Gobierno",
         "—",
         ["1.º Real Decreto del Presidente del Gobierno o acordado en el Consejo de Ministros", "2.º Orden Ministerial"],
         "—",
         "Solo **dos** escalones. El Real Decreto del **Presidente** y el **acordado en Consejo de Ministros** están en el **mismo** (1.º)."))}

{unidad("1.3 El orden de jerarquía lo fijan las leyes (Ley 39/2015, art. 128.3)",
  lit("L39", "Artículo 128", ["Ninguna disposición administrativa podrá vulnerar los preceptos de otra de rango superior"], solo=[3]),
  fichab("Jerarquía entre disposiciones administrativas",
         "—",
         f"{c('L39', 'Artículo 128', 'Las disposiciones administrativas se ajustarán al orden de jerarquía que establezcan las leyes')}",
         "—",
         "El orden de jerarquía lo establecen **las leyes** (para el Estado, el art. 24.2 de la Ley 50/1997). La disposición que vulnera otra de rango superior es **nula** (→ III.1.2)."))}
""", 2)

P3_129 = f"""El párrafo tercero del art. 129.4 se cita aquí **sin los incisos anulados** (nota del BOE, abajo): {c('L39', 'Artículo 129', 'Las habilitaciones para el desarrollo reglamentario de una ley serán conferidas, con carácter general, al Gobierno')} … {c('L39', 'Artículo 129', 'La atribución directa a los titulares de los departamentos ministeriales')} … {c('L39', 'Artículo 129', 'o a otros órganos dependientes o subordinados de ellos, tendrá carácter excepcional y deberá justificarse en la ley habilitante')}."""

NOTA_129 = f"""> [[BOE|https://www.boe.es/buscar/act.php?id=BOE-A-2015-10565]]
> **Nota del BOE al artículo 129 de la Ley 39/2015 (texto consolidado) · fuente oficial, no es texto legal**
> {nota('L39', 'a129', 'Se declara contrario al orden constitucional de competencias en los términos del f.j. 7 b), salvo los párrafos segundo y tercero del apartado 4, y la inconstitucionalidad y nulidad de los incisos destacados en negrita del párrafo tercero del apartado 4, por Sentencia del TC 55/2018, de 24 de mayo.')}

*Los incisos destacados en el texto consolidado del BOE son «o Consejo de Gobierno respectivo» y «o de las consejerías del Gobierno»: por eso no se reproducen.*"""

T.ap("s4", "II.2 Reglamentos ejecutivos y habilitaciones (LO 3/1980, art. 22; Ley 39/2015, art. 129.4)", f"""
{unidad("2.1 Reglamentos que se dictan en ejecución de las leyes o de tratados: dictamen del Consejo de Estado (LO 3/1980, art. 22)",
  lit("LO3_1980", "aveintidos", ["Disposiciones reglamentarias que se dicten en ejecución, cumplimiento o desarrollo de tratados", "Reglamentos o disposiciones de carácter general que se dicten en ejecución de las Leyes, así como sus modificaciones"], solo=[1, 3, 4], titulo="Artículo veintidós, apartados Dos y Tres (LO 3/1980, del Consejo de Estado)"),
  fichab("Consulta preceptiva al Consejo de Estado sobre ciertos reglamentos",
         "La **Comisión Permanente** del Consejo de Estado",
         ["Disposiciones reglamentarias en ejecución, cumplimiento o desarrollo de **tratados**, convenios o acuerdos internacionales y del **derecho comunitario europeo** (Dos)", "Reglamentos o disposiciones de carácter general que se dicten **en ejecución de las Leyes**, y sus modificaciones (Tres)"],
         "—",
         "Es la **Comisión Permanente** (no el Pleno). Cubre también las **modificaciones** de los reglamentos ejecutivos. Concuerda con la Ley 50/1997, art. 5.1 h) (→ I.2.2)."))}

{unidad("2.2 A quién habilita la ley para desarrollarla (Ley 39/2015, art. 129.4, párrafos tercero y cuarto)",
  lit("L39", "Artículo 129", ["cuando la naturaleza de la materia así lo exija"], solo=[7], titulo="Artículo 129.4, párrafo cuarto (Ley 39/2015)"),
  P3_129,
  NOTA_129,
  fichab("Habilitación legal para dictar reglamentos de desarrollo",
         ["Regla: el **Gobierno**", "Excepción: los **titulares de los departamentos ministeriales** u otros órganos dependientes o subordinados, si lo justifica la ley habilitante", "Autoridades Independientes u otros organismos con esta potestad, cuando la naturaleza de la materia lo exija"],
         "La habilitación la confiere **la ley** que se desarrolla",
         "—",
         "La atribución directa a los **Ministros** es **excepcional** y debe justificarse **en la ley habilitante**."))}
""", 2)

T.ap("s5", "II.3 Cuadro de las clases de reglamentos (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Criterio | Clases | Dónde está |
|---|---|---|
| Administración que lo dicta | Del Estado (Gobierno), de las Comunidades Autónomas y de los entes locales | Ley 39/2015, art. 128.1 (→ I.2.1) |
| Órgano y forma (Estado) | Real Decreto del Presidente del Gobierno · Real Decreto acordado en Consejo de Ministros · Orden Ministerial (y Orden del Ministro de la Presidencia si afecta a varios Departamentos) | Ley 50/1997, art. 24.1 (→ II.1.1) |
| Jerarquía (Estado) | 1.º Reales Decretos · 2.º Órdenes Ministeriales | Ley 50/1997, art. 24.2 (→ II.1.2) |
| Relación con la ley | «Reglamentos … que se dicten en ejecución de las Leyes» (dictamen del Consejo de Estado) y «demás disposiciones reglamentarias que procedan» | LO 3/1980, art. 22.Tres; Ley 50/1997, art. 5.1 h) (→ II.2.1) |
| Ejecución de tratados y Derecho de la UE | Disposiciones reglamentarias en ejecución de tratados y del derecho comunitario europeo | LO 3/1980, art. 22.Dos (→ II.2.1) |
| Normas organizativas | Las «normas presupuestarias u organizativas» pueden prescindir de la consulta pública | Ley 39/2015, art. 133.4; Ley 50/1997, art. 26.2 a) (→ III.2.3 y III.3.3) |

{resumen([
  "Formas (Ley 50/1997, art. 24.1): **Real Decreto** (del Presidente o acordado en Consejo de Ministros), **Acuerdo** del Consejo de Ministros, **Orden Ministerial**.",
  "Jerarquía (art. 24.2): **1.º Reales Decretos**, **2.º Órdenes Ministeriales**; ninguna disposición puede vulnerar otra de **rango superior** (Ley 39/2015, art. 128.3).",
  "Reglamentos **en ejecución de las Leyes** y en ejecución de **tratados** o del Derecho de la UE: dictamen de la **Comisión Permanente** del Consejo de Estado (LO 3/1980, art. 22).",
  "La ley habilita, **con carácter general, al Gobierno**; a los **Ministros**, solo de forma **excepcional** y justificada (Ley 39/2015, art. 129.4)."],
  "Siguiente: III. ¿Qué límites tiene el reglamento y cómo se controla?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Qué límites tiene el reglamento y cómo se controla?", donde(
  "Tercera pregunta. El reglamento está **por debajo de la ley**: no puede contradecirla ni regular lo reservado a ella (límites **materiales**); se elabora por un **procedimiento** y se **publica** (límites **formales**); si los incumple es **nulo**, y lo controlan los **Tribunales**.",
  ["1 Límites materiales y nulidad (Ley 39/2015, arts. 128.2, 47.2 y 37; Código Civil, art. 1.2)", "2 Principios de buena regulación, publicidad y participación (Ley 39/2015, arts. 129 a 133)", "3 Elaboración de los reglamentos del Gobierno (Ley 50/1997, arts. 23, 25 y 26)", "4 El control de los reglamentos (arts. 106.1 y 153 c) CE; LJCA, arts. 1.1, 26 y 27)"]))

T.ap("s6", "III.1 Límites materiales y nulidad (Ley 39/2015, arts. 128.2, 47.2 y 37; Código Civil, art. 1.2)", f"""
{unidad("1.1 Lo que un reglamento no puede hacer (Ley 39/2015, art. 128.2)",
  lit("L39", "Artículo 128", ["no podrán vulnerar la Constitución o las leyes", "no podrán tipificar delitos, faltas o infracciones administrativas, establecer penas o sanciones, así como tributos, exacciones parafiscales u otras cargas o prestaciones personales o patrimoniales de carácter público"], solo=[2]),
  fichab("Límites materiales de los reglamentos",
         "Todos los titulares de la potestad reglamentaria (→ I.2.1)",
         ["No vulnerar la **Constitución** ni las **leyes**", "No regular materias de la competencia de las **Cortes Generales** o de las **Asambleas Legislativas** de las CC. AA.", "No **tipificar** delitos, faltas o infracciones administrativas ni establecer **penas o sanciones**", "No establecer **tributos**, exacciones parafiscales u otras cargas o **prestaciones personales o patrimoniales** de carácter público"],
         "—",
         f"Todo ello {c('L39', 'Artículo 128', 'Sin perjuicio de su función de desarrollo o colaboración con respecto a la ley')}: el reglamento puede **desarrollar** o **colaborar**, pero no **tipificar** ni **crear** tributos."))}

{unidad("1.2 Disposiciones nulas de pleno derecho (Ley 39/2015, art. 47.2)",
  lit("L39", "Artículo 47", ["las que regulen materias reservadas a la Ley", "las que establezcan la retroactividad de disposiciones sancionadoras no favorables o restrictivas de derechos individuales"], solo=[9]),
  fichab("Consecuencia de vulnerar los límites: nulidad de pleno derecho",
         "—",
         ["Vulnerar la Constitución, las leyes u otras disposiciones administrativas de **rango superior**", "Regular **materias reservadas a la Ley**", "Establecer la **retroactividad** de disposiciones **sancionadoras no favorables** o **restrictivas de derechos individuales**"],
         "—",
         "Para las disposiciones generales la sanción es la **nulidad de pleno derecho** (art. 47.2), no la anulabilidad. Concuerda con el Código Civil: «Carecerán de validez las disposiciones que contradigan otra de rango superior» (→ III.1.4)."))}

{unidad("1.3 Inderogabilidad singular (Ley 39/2015, art. 37)",
  lit("L39", "Artículo 37", ["aunque aquéllas procedan de un órgano de igual o superior jerarquía al que dictó la disposición general"]),
  fichab("El reglamento vincula también a quien lo dictó al resolver casos concretos",
         "Cualquier órgano, aunque sea **de igual o superior jerarquía** al que dictó la disposición",
         f"Las {c('L39', 'Artículo 37', 'resoluciones administrativas de carácter particular no podrán vulnerar lo establecido en una disposición de carácter general')}",
         "—",
         f"La sanción es la nulidad: {c('L39', 'Artículo 37', 'Son nulas las resoluciones administrativas que vulneren lo establecido en una disposición reglamentaria')}. Ni el órgano **superior** puede saltarse el reglamento en un caso concreto."))}

{unidad("1.4 Jerarquía normativa en el Código Civil (art. 1.2)",
  lit("CC", "a1", ["Carecerán de validez las disposiciones que contradigan otra de rango superior"], solo=[2], titulo="Artículo 1.2 (Código Civil)"),
  fichab("Invalidez de la norma que contradice otra superior",
         "—",
         "La disposición que contradice otra de **rango superior** carece de validez",
         "—",
         "Es la misma regla que el art. 128.3 de la Ley 39/2015 (→ II.1.3) y el principio de **jerarquía normativa** que garantiza el art. 9.3 CE (→ IV.2.1)."))}
""", 2)

T.ap("s7", "III.2 Principios de buena regulación, publicidad y participación (Ley 39/2015, arts. 129 a 133)", f"""
> [[BOE|https://www.boe.es/buscar/act.php?id=BOE-A-2015-10565]]
> **Notas del BOE a los artículos 130, 132 y 133 de la Ley 39/2015 (texto consolidado) · fuente oficial, no es texto legal**
> Art. 130: «{nota('L39', 'a130', 'Se declara contrario al orden constitucional de competencias en los términos del f.j. 7 b) por Sentencia del TC 55/2018, de 24 de mayo.')}»
> Art. 132: «{nota('L39', 'a132', 'Se declara contrario al orden constitucional de competencias en los términos del f.j. 7 b) y 7 c) por Sentencia del TC 55/2018, de 24 de mayo.')}»
> Art. 133: «{nota('L39', 'a133', 'Se declara contrario al orden constitucional de competencias en los términos del f.j. 7 b) y, salvo el inciso de su apartado primero «Con carácter previo a la elaboración del proyecto o anteproyecto de ley o de reglamento, se sustanciará una consulta pública» y el primer párrafo de su apartado 4, en los términos del f.j. 7 c), por Sentencia del TC 55/2018, de 24 de mayo.')}»

*Estos artículos siguen en el texto consolidado (no se han anulado); las notas del BOE indican que la STC 55/2018 los declaró contrarios al orden constitucional de competencias en los términos que en ellas se citan. El art. 129 lleva la nota que se reproduce en → II.2.2.*

{unidad("2.1 Principios de buena regulación (Ley 39/2015, art. 129.1 a 3)",
  lit("L39", "Artículo 129", ["necesidad, eficacia, proporcionalidad, seguridad jurídica, transparencia, y eficiencia", "En la exposición de motivos o en el preámbulo"], solo=[1, 2, 3]),
  fichab("Principios a los que se ajusta toda iniciativa normativa",
         c("L39", "Artículo 129", "las Administraciones Públicas"),
         ["**Necesidad y eficacia**: razón de interés general, fines claros, instrumento más adecuado", "**Proporcionalidad**: la regulación **imprescindible**, tras constatar que no hay medidas menos restrictivas", "**Seguridad jurídica**, **transparencia** y **eficiencia** (129.4 a 6)"],
         "La adecuación se justifica en la **exposición de motivos** (anteproyectos de ley) o en el **preámbulo** (proyectos de reglamento)",
         "Son **seis** principios: necesidad, eficacia, proporcionalidad, seguridad jurídica, transparencia y eficiencia. Los reglamentos los justifican en el **preámbulo**."))}

{unidad("2.2 Publicidad: sin publicación no hay entrada en vigor (Ley 39/2015, art. 131)",
  lit("L39", "Artículo 131", ["habrán de publicarse en el diario oficial correspondiente para que entren en vigor y produzcan efectos jurídicos"], solo=[1]),
  fichab("Publicación de las normas",
         "Cada Administración, en su **diario oficial**",
         "Publicación obligatoria; otros medios de publicidad complementarios, **facultativos**",
         "—",
         "La publicación es requisito para que la norma **entre en vigor y produzca efectos**. Es el principio de **publicidad de las normas** del art. 9.3 CE (→ IV.2.1)."))}

{unidad("2.3 Plan Anual Normativo y participación de los ciudadanos (Ley 39/2015, arts. 132 y 133)",
  lit("L39", "Artículo 132", ["que vayan a ser elevadas para su aprobación en el año siguiente"]),
  lit("L39", "Artículo 133", ["se sustanciará una consulta pública", "normas presupuestarias u organizativas"], solo=[1, 6, 8]),
  fichab("Planificación y participación en la elaboración de las normas",
         "Las Administraciones Públicas; el **centro directivo competente** publica el texto para audiencia",
         ["**Plan Anual Normativo**: iniciativas del año siguiente; se publica en el **Portal de la Transparencia** (132)", "**Consulta pública previa**, a través del portal web, antes de elaborar el texto (133.1)", "**Audiencia e información pública** del texto cuando afecte a derechos e intereses legítimos (133.2)"],
         "—",
         "Se puede prescindir de consulta, audiencia e información públicas en normas **presupuestarias u organizativas** o por **razones graves de interés público** (133.4)."))}
""", 2)

T.ap("s8", "III.3 Elaboración de los reglamentos del Gobierno (Ley 50/1997, arts. 23, 25 y 26)", f"""
{unidad("3.1 Entrada en vigor el 2 de enero o el 1 de julio (Ley 50/1997, art. 23)",
  lit("LGOB", "a23", ["el 2 de enero o el 1 de julio siguientes a su aprobación", "no será de aplicación a los reales decretos-leyes"]),
  fichab("Fechas fijas de entrada en vigor",
         "Leyes o reglamentos cuya aprobación o propuesta corresponda al **Gobierno** o a sus miembros",
         "Cuando impongan **nuevas obligaciones** a quienes desempeñen una **actividad económica o profesional**, preverán su vigencia el **2 de enero** o el **1 de julio** siguientes a su aprobación",
         "—",
         "No se aplica a los **reales decretos-leyes**, ni cuando lo aconsejen la transposición de directivas u otras razones justificadas (acreditadas en la Memoria)."))}

{unidad("3.2 Plan Anual Normativo del Gobierno (Ley 50/1997, art. 25.1 y 4)",
  lit("LGOB", "a25", ["El Gobierno aprobará anualmente un Plan Normativo", "antes del 30 de abril"], solo=[1, 4]),
  fichab("Programación anual de las iniciativas normativas del Gobierno",
         "El **Gobierno** lo aprueba; lo coordina el **Ministerio de la Presidencia**, cuyo titular lo eleva al Consejo de Ministros",
         "Contiene las iniciativas legislativas o reglamentarias que se elevarán en el **año siguiente**",
         "Elevación al Consejo de Ministros **antes del 30 de abril**",
         "Si se tramita una norma **no incluida** en el Plan, hay que justificarlo en la **Memoria del Análisis de Impacto Normativo** (art. 25.3)."))}

{unidad("3.3 Procedimiento de elaboración (Ley 50/1997, art. 26, extracto)",
  lit("LGOB", "a26", ["que en ningún caso será inferior a quince días naturales", "deberán ser informados por la Secretaría General Técnica", "El plazo mínimo de esta audiencia e información públicas será de 15 días hábiles", "Se recabará el dictamen del Consejo de Estado u órgano consultivo equivalente cuando fuera preceptivo o se considere conveniente"], solo=[1, 3, 4, 5, 6, 7, 8, 9, 16, 17, 29, 30, 32, 35, 36, 38, 39]),
  fichab("Pasos para aprobar un reglamento del Gobierno",
         ["El **centro directivo competente** (Memoria, informes, audiencia)", "**Secretaría General Técnica** del Ministerio proponente (informe preceptivo)", "**Consejo de Estado** (cuando sea preceptivo o conveniente)", "**Comisión General de Secretarios de Estado y Subsecretarios** y **Consejo de Ministros**"],
         ["Consulta pública previa en el portal web (26.2)", "**Memoria del Análisis de Impacto Normativo**, preceptiva (26.3)", "Informes y dictámenes (26.5)", "Audiencia e información públicas (26.6)", "Dictamen del Consejo de Estado (26.7)", "Comisión General y Consejo de Ministros (26.8)"],
         ["Consulta pública: **no inferior a quince días naturales**", "Informes preceptivos: **diez días**, o **un mes** si se piden a otra Administración o a un órgano con especial independencia", "Audiencia: mínimo **15 días hábiles**, reducible a **siete días hábiles** si está motivado o hay tramitación urgente"],
         "Consulta pública: días **naturales**; audiencia: días **hábiles**. La consulta pública puede omitirse, entre otros casos, en normas **presupuestarias u organizativas** de la AGE (26.2 a)."))}
""", 2)

T.ap("s9", "III.4 El control de los reglamentos (arts. 106.1 y 153 c) CE; LJCA, arts. 1.1, 26 y 27)", f"""
{unidad("4.1 Los Tribunales controlan la potestad reglamentaria (art. 106.1)",
  lit("CE", "Artículo 106", ["Los Tribunales controlan la potestad reglamentaria"], solo=[1]),
  fichab("Control judicial de los reglamentos",
         c("CE", "Artículo 106", "Los Tribunales"),
         f"Controlan {c('CE', 'Artículo 106', 'la potestad reglamentaria y la legalidad de la actuación administrativa')}",
         "—",
         "El art. 106.1 nombra **expresamente** la potestad reglamentaria. La jurisdicción competente es la contencioso-administrativa (→ III.4.3)."))}

{unidad("4.2 Normas reglamentarias de las Comunidades Autónomas (art. 153 c)",
  lit("CE", "Artículo 153", ["Por la jurisdicción contencioso-administrativa, el de la administración autónoma y sus normas reglamentarias"], solo=[1, 4]),
  fichab("Control de los reglamentos autonómicos",
         "La **jurisdicción contencioso-administrativa**",
         "Controla la administración autónoma **y sus normas reglamentarias**",
         "—",
         "El **Tribunal Constitucional** controla las disposiciones autonómicas **con fuerza de ley** (153 a); los **reglamentos**, la jurisdicción **contencioso-administrativa** (pregunta oficial X 65, → Cierre 1)."))}

{unidad("4.3 Recurso directo e indirecto (LJCA, arts. 1.1 y 26)",
  lit("LJCA", "Artículo 1", ["con las disposiciones generales de rango inferior a la Ley"], solo=[1]),
  lit("LJCA", "Artículo 26", ["también es admisible la de los actos que se produzcan en aplicación de las mismas", "no impiden la impugnación de los actos de aplicación"]),
  fichab("Cómo se impugna un reglamento",
         "Juzgados y Tribunales del orden **contencioso-administrativo**",
         ["**Recurso directo** contra la disposición general", "**Recurso indirecto**: contra los actos de aplicación, alegando que la disposición no es conforme a Derecho"],
         "—",
         "El recurso indirecto cabe **aunque** no se impugnara directamente la disposición o se **desestimara** el recurso directo (26.2)."))}

{unidad("4.4 La cuestión de ilegalidad (LJCA, art. 27)",
  lit("LJCA", "Artículo 27", ["deberá plantear la cuestión de ilegalidad ante el Tribunal competente para conocer del recurso directo contra la disposición", "el Tribunal Supremo anulará cualquier disposición general"]),
  fichab("Depuración del reglamento ilegal tras un recurso indirecto",
         ["Juez o Tribunal que dictó la **sentencia firme estimatoria**", "Tribunal competente para el **recurso directo**", "**Tribunal Supremo**"],
         ["Regla: el juez **plantea la cuestión de ilegalidad** al Tribunal del recurso directo (27.1)", "Si es competente para ambos, la sentencia declara la validez o nulidad de la disposición (27.2)", "El Tribunal Supremo la **anula** sin plantear la cuestión (27.3)"],
         "Tras **sentencia firme estimatoria**",
         "La cuestión de ilegalidad la plantea el **juez**, no las partes, y solo tras sentencia **firme** **estimatoria**."))}

{resumen([
  "Límites materiales (Ley 39/2015, art. 128.2): ni vulnerar la CE o las leyes, ni materias de las **Cortes** o de las **Asambleas**; ni **tipificar** infracciones ni **sanciones**; ni **tributos** ni prestaciones personales o patrimoniales.",
  "Sanción: **nulidad de pleno derecho** (art. 47.2), incluida la **retroactividad** de disposiciones sancionadoras no favorables; e **inderogabilidad singular** (art. 37).",
  "Forma: buena regulación (art. 129), **publicación** en el diario oficial para entrar en vigor (art. 131); en el Estado, **consulta pública** (≥ 15 días naturales), **audiencia** (≥ 15 días hábiles, reducible a 7), SGT y Consejo de Estado (Ley 50/1997, art. 26).",
  "Control: los **Tribunales** (106.1 CE); contencioso-administrativo, **directo** o **indirecto** (LJCA, arts. 1.1 y 26), y **cuestión de ilegalidad** (art. 27)."],
  "Siguiente: IV. ¿Qué son los principios generales del Derecho?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Qué son los principios generales del Derecho? (Código Civil, art. 1; art. 9.3 CE)", donde(
  "Cuarta pregunta. El Código Civil enumera las fuentes del ordenamiento y coloca a los **principios generales del Derecho** en tercer lugar: se aplican **en defecto de ley o costumbre**, pero además **informan** todo el ordenamiento. La Constitución, por su parte, **garantiza** una serie de principios en su art. 9.3.",
  ["1 Las fuentes y el lugar de los principios generales (Código Civil, art. 1.1, 1.3 y 1.4)", "2 Principios que garantiza la Constitución (art. 9.3) y la jurisprudencia (Código Civil, art. 1.6 y 1.7)"]))

T.ap("s10", "IV.1 Las fuentes y el lugar de los principios generales (Código Civil, art. 1.1, 1.3 y 1.4)", f"""
{unidad("1.1 Las tres fuentes del ordenamiento (art. 1.1)",
  lit("CC", "a1", ["la ley, la costumbre y los principios generales del derecho"], solo=[1], titulo="Artículo 1.1 (Código Civil)"),
  fichab("Enumeración de las fuentes del ordenamiento jurídico español",
         "—",
         ["La **ley**", "La **costumbre**", "Los **principios generales del derecho**"],
         "—",
         "Son **tres**, en ese orden. **No** figuran ni la **jurisprudencia** (la «complementa», 1.6), ni los **tratados** (rigen al publicarse, 1.5 → V.4), ni los reglamentos como fuente separada (pregunta oficial L 46, → Cierre 1)."))}

{unidad("1.2 La costumbre, solo en defecto de ley (art. 1.3)",
  lit("CC", "a1", ["sólo regirá en defecto de ley aplicable"], solo=[3, 4], titulo="Artículo 1.3 (Código Civil)"),
  fichab("Requisitos de la costumbre como fuente",
         "—",
         ["En defecto de **ley aplicable**", "No contraria a la **moral** ni al **orden público**", "**Probada**"],
         "—",
         "Los **usos jurídicos** no meramente interpretativos de una declaración de voluntad tienen consideración de **costumbre**."))}

{unidad("1.3 Los principios generales del derecho (art. 1.4)",
  lit("CC", "a1", ["se aplicarán en defecto de ley o costumbre", "sin perjuicio de su carácter informador del ordenamiento jurídico"], solo=[5], titulo="Artículo 1.4 (Código Civil)"),
  fichab("Doble función de los principios generales",
         "—",
         ["**Fuente supletoria**: se aplican **en defecto de ley o costumbre**", "**Función informadora** del ordenamiento jurídico"],
         "—",
         "Se aplican en defecto de ley **o** costumbre (en tercer lugar), **sin perjuicio** de su carácter **informador**. No se dice que sean «fuente principal» ni que necesiten prueba (eso es la costumbre, 1.3)."))}
""", 2)

T.ap("s11", "IV.2 Principios que garantiza la Constitución (art. 9.3) y la jurisprudencia (Código Civil, art. 1.6 y 1.7)", f"""
{unidad("2.1 Principios que garantiza la Constitución (art. 9.3)",
  lit("CE", "Artículo 9", ["La Constitución garantiza el principio de legalidad, la jerarquía normativa, la publicidad de las normas"], solo=[3]),
  fichab("Principios garantizados expresamente por la Constitución",
         "—",
         ["Legalidad", "Jerarquía normativa", "Publicidad de las normas", "Irretroactividad de las disposiciones sancionadoras no favorables o restrictivas de derechos individuales", "Seguridad jurídica", "Responsabilidad", "Interdicción de la arbitrariedad de los poderes públicos"],
         "—",
         "Son **siete** y la Constitución los **garantiza**. Varios se proyectan sobre el reglamento: jerarquía (→ II.1.2), publicidad (→ III.2.2) e irretroactividad (→ III.1.2)."))}

*Nota de elaboración propia: el art. 9.3 CE no usa la expresión «principios generales del derecho»; se estudia aquí porque enuncia principios con rango constitucional que limitan al reglamento. No es texto legal.*

{unidad("2.2 La jurisprudencia y el deber de resolver (Código Civil, art. 1.6 y 1.7)",
  lit("CC", "a1", ["complementará el ordenamiento jurídico", "ateniéndose al sistema de fuentes establecido"], solo=[7, 8], titulo="Artículo 1.6 y 1.7 (Código Civil)"),
  fichab("Papel de la jurisprudencia y deber de los jueces",
         ["La **jurisprudencia**: doctrina reiterada del **Tribunal Supremo**", "**Jueces y Tribunales**"],
         ["La jurisprudencia **complementa** el ordenamiento al interpretar y aplicar la ley, la costumbre y los principios generales del derecho", "Los jueces deben resolver **en todo caso**, ateniéndose al sistema de fuentes"],
         "—",
         "La jurisprudencia **no** es fuente del art. 1.1: **complementa** el ordenamiento. Exige doctrina **reiterada** del **Tribunal Supremo**. El deber de resolver es **inexcusable**."))}

{resumen([
  "Fuentes (CC 1.1): **ley, costumbre y principios generales del derecho**, por ese orden.",
  "Los principios generales se aplican **en defecto de ley o costumbre**, sin perjuicio de su carácter **informador** del ordenamiento (CC 1.4).",
  "La jurisprudencia del **Tribunal Supremo**, reiterada, **complementa** el ordenamiento (CC 1.6); los jueces deben resolver **en todo caso** (CC 1.7).",
  "El art. 9.3 CE **garantiza** legalidad, jerarquía, publicidad, irretroactividad, seguridad jurídica, responsabilidad e interdicción de la arbitrariedad."],
  "Siguiente: V. ¿Cómo se celebra un tratado y cómo entra en el ordenamiento?")}
""", 2)

# =============================================================================
T.ap("bV", "V. ¿Cómo se celebra un tratado y cómo entra en el ordenamiento? (arts. 93 a 96 CE; Ley 25/2014)", donde(
  "Quinta pregunta. La Constitución regula **qué tratados necesitan autorización de las Cortes** (arts. 93 y 94), su **control previo** (art. 95) y su **eficacia interna** (art. 96). La Ley 25/2014 desarrolla la celebración, la publicación y la aplicación.",
  ["1 Qué es un tratado y qué otros acuerdos hay (Ley 25/2014, arts. 2 y 43)", "2 Quién se obliga y cuándo hace falta autorización de las Cortes (arts. 63.2, 74.2, 93 y 94 CE; Ley 25/2014, arts. 15 y 17)", "3 Control de constitucionalidad del tratado (art. 95 CE; LOTC, arts. 27.2 y 78; Ley 25/2014, arts. 19 y 32)", "4 Publicación, eficacia y prevalencia (art. 96.1 CE; Código Civil, art. 1.5; Ley 25/2014, arts. 23, 30 y 31)", "5 Denuncia (art. 96.2 CE; Ley 25/2014, art. 37)"]))

T.ap("s12", "V.1 Qué es un tratado y qué otros acuerdos hay (Ley 25/2014, arts. 2 y 43)", f"""
{unidad("1.1 Tratado, acuerdo internacional administrativo y acuerdo no normativo (Ley 25/2014, art. 2 a) a c)",
  lit("L25_2014", "a2", ["acuerdo celebrado por escrito entre España y otro u otros sujetos de Derecho Internacional, y regido por el Derecho Internacional", "cuya celebración está prevista en el tratado que ejecuta o concreta", "no constituye fuente de obligaciones internacionales ni se rige por el Derecho Internacional"], solo=[1, 2, 3, 4], titulo="Artículo 2 a) a c) (Ley 25/2014, de Tratados)"),
  fichab("Las tres clases de acuerdos que regula la Ley 25/2014",
         "España y otros **sujetos de Derecho Internacional** (Estado, organización internacional u otro ente con capacidad para celebrar tratados, art. 2 d)",
         ["**Tratado internacional**: por **escrito**, regido por el **Derecho Internacional**, cualquiera que sea su **denominación**", "**Acuerdo internacional administrativo**: **no** es tratado; lo celebran órganos competentes en ejecución o concreción de un **tratado** que lo prevé; contenido habitualmente **técnico**", "**Acuerdo internacional no normativo**: declaraciones de intenciones o compromisos de actuación; **no** es fuente de obligaciones internacionales ni se rige por el Derecho Internacional"],
         "—",
         "El tratado lo es «**cualquiera que sea su denominación**» (convenio, protocolo…). El acuerdo administrativo necesita un **tratado que lo prevea**."))}

{unidad("1.2 Naturaleza del acuerdo no normativo (Ley 25/2014, art. 43)",
  lit("L25_2014", "a43", ["no constituyen fuente de obligaciones internacionales"]),
  fichab("Acuerdos sin efectos jurídicos internacionales",
         "Gobierno, departamentos, Comunidades Autónomas, Ciudades de Ceuta y Melilla, Entidades Locales, Universidades públicas y otros sujetos de derecho público con competencia (art. 44)",
         "—", "—",
         "**No** son fuente de obligaciones internacionales y **no** necesitan la tramitación del título II (art. 46.1)."))}
""", 2)

T.ap("s13", "V.2 Quién se obliga y cuándo hace falta autorización de las Cortes (arts. 63.2, 74.2, 93 y 94 CE; Ley 25/2014, arts. 15 y 17)", f"""
{unidad("2.1 El Rey manifiesta el consentimiento del Estado (art. 63.2)",
  lit("CE", "Artículo 63", ["manifestar el consentimiento del Estado para obligarse internacionalmente por medio de tratados"], solo=[2]),
  fichab("Manifestación del consentimiento",
         c("CE", "Artículo 63", "Al Rey"),
         f"{c('CE', 'Artículo 63', 'de conformidad con la Constitución y las leyes')}; lo acuerda el **Consejo de Ministros** (Ley 25/2014, art. 16.1) y el Rey firma los instrumentos de ratificación y adhesión con el **refrendo del Ministro de Asuntos Exteriores y de Cooperación** (art. 22)",
         "—",
         "**Acuerda** el Consejo de Ministros; **manifiesta** el Rey."))}

{unidad("2.2 Tratados que atribuyen competencias a una organización internacional (art. 93)",
  lit("CE", "Artículo 93", ["Mediante ley orgánica", "el ejercicio de competencias derivadas de la Constitución"]),
  fichab("Cesión del ejercicio de competencias a organizaciones internacionales",
         ["Autorizan las **Cortes**, por **ley orgánica**", "Garantizan el cumplimiento **las Cortes Generales o el Gobierno**, según los casos"],
         "Tratados por los que se atribuye a una organización o institución internacional el **ejercicio** de competencias derivadas de la Constitución",
         "**Ley orgánica** (mayoría absoluta del Congreso en votación final: tema IV.2)",
         "Se cede el **ejercicio** de competencias, no la titularidad. Estos tratados **no** admiten **aplicación provisional** (Ley 25/2014, art. 15.2, → V.2.4)."))}

{unidad("2.3 Tratados que necesitan autorización previa de las Cortes (arts. 94 y 74.2)",
  lit("CE", "Artículo 94", ["requerirá la previa autorización de las Cortes Generales", "serán inmediatamente informados"]),
  lit("CE", "Artículo 74", ["se adoptarán por mayoría de cada una de las Cámaras", "En el primer caso, el procedimiento se iniciará por el Congreso"], solo=[2]),
  fichab("Autorización parlamentaria para obligarse por un tratado",
         ["Autorizan las **Cortes Generales** (art. 94.1)", "Para los demás tratados, el Congreso y el Senado son **informados** (art. 94.2)"],
         ["::Casos del art. 94.1:", "a) Tratados de carácter **político**", "b) De carácter **militar**", "c) Que afecten a la **integridad territorial** o a los **derechos y deberes fundamentales** del Título I", "d) Que impliquen **obligaciones financieras** para la Hacienda Pública", "e) Que supongan **modificación o derogación de alguna ley** o exijan **medidas legislativas** para su ejecución"],
         ["Mayoría **de cada una de las Cámaras**; el procedimiento empieza en el **Congreso** (74.2)", "Sin acuerdo: **Comisión Mixta**; si su texto no se aprueba, decide el **Congreso por mayoría absoluta**"],
         "El 94.1 es **previo** («previa autorización»); el 94.2 solo exige **información inmediata**. En el art. 74.2 el procedimiento del 94.1 empieza en el **Congreso** (los del 145.2 y 158.2, en el Senado)."))}

{unidad("2.4 Trámites internos: Consejo de Estado y aplicación provisional (Ley 25/2014, arts. 15 y 17)",
  lit("L25_2014", "a15", ["autorizará la aplicación provisional, total o parcial", "no podrá autorizarse respecto de los tratados internacionales a que se refiere el artículo 93"], solo=[1, 2]),
  lit("L25_2014", "a17", ["elevará al Consejo de Estado", "la consulta acerca de la necesidad de autorización de las Cortes Generales"], solo=[1, 2]),
  fichab("Pasos internos antes de obligarse",
         ["**Consejo de Ministros** (autoriza la aplicación provisional; remite el tratado a las Cortes)", "**Ministerio de Asuntos Exteriores y de Cooperación** (eleva la consulta al Consejo de Estado)", "**Consejo de Estado** (dictamen sobre la necesidad de autorización)"],
         ["Aplicación provisional, total o parcial, antes de la entrada en vigor; el Ministerio de la Presidencia la comunica a las Cortes (15.1)", "Consulta al **Consejo de Estado** sobre si hace falta autorización de las Cortes (17.2)"],
         "—",
         "**No** cabe aplicación provisional de los tratados del **art. 93**. La consulta sobre la necesidad de autorización va a la **Comisión Permanente** del Consejo de Estado (LO 3/1980, art. 22.Uno)."))}
""", 2)

T.ap("s14", "V.3 Control de constitucionalidad del tratado (art. 95 CE; LOTC, arts. 27.2 y 78; Ley 25/2014, arts. 19 y 32)", f"""
{unidad("3.1 Tratado contrario a la Constitución: revisión previa (art. 95)",
  lit("CE", "Artículo 95", ["exigirá la previa revisión constitucional", "El Gobierno o cualquiera de las Cámaras"]),
  fichab("Control previo de constitucionalidad",
         ["Pueden requerir al TC: **el Gobierno o cualquiera de las Cámaras**", "Declara: el **Tribunal Constitucional**"],
         "Si el tratado contiene estipulaciones contrarias a la Constitución, hay que **revisar antes la Constitución**",
         "—",
         "No legitima a 50 Diputados ni al Defensor del Pueblo: solo **Gobierno** o **cualquiera de las Cámaras**."))}

{unidad("3.2 El requerimiento al Tribunal Constitucional (LOTC, art. 78; Ley 25/2014, art. 19)",
  lit("LOTC", "asetentayocho", ["cuyo texto estuviera ya definitivamente fijado, pero al que no se hubiere prestado aún el consentimiento del Estado", "tendrá carácter vinculante"], solo=[1, 2]),
  lit("L25_2014", "a19", ["artículo 78 de la Ley Orgánica 2/1979"]),
  fichab("Procedimiento del control previo",
         "Gobierno o cualquiera de ambas Cámaras; el **Tribunal Constitucional**",
         "Requerimiento sobre un tratado con texto **definitivamente fijado** y **sin** consentimiento prestado",
         ["Opiniones de los órganos legitimados: **un mes**", "Declaración del TC: **dentro del mes siguiente**", "Ampliación por aclaraciones: hasta **treinta días**"],
         "La declaración del TC es **vinculante**. El control es **previo** al consentimiento."))}

{unidad("3.3 Control posterior: el tratado como objeto de declaración de inconstitucionalidad (LOTC, art. 27.2 c; Ley 25/2014, art. 32)",
  lit("LOTC", "aveintisiete", ["Los Tratados Internacionales"], solo=[2, 5], titulo="Artículo veintisiete, apartado Dos c) (LOTC)"),
  lit("L25_2014", "a32", ["título II de la Ley Orgánica 2/1979"]),
  fichab("Control de constitucionalidad del tratado ya celebrado",
         "El **Tribunal Constitucional**",
         "Por el procedimiento de declaración de inconstitucionalidad del título II de la LOTC",
         "—",
         "Los tratados son **susceptibles de declaración de inconstitucionalidad**; una ordenanza local, no (pregunta oficial X 9, → Cierre 1)."))}
""", 2)

T.ap("s15", "V.4 Publicación, eficacia y prevalencia (art. 96.1 CE; Código Civil, art. 1.5; Ley 25/2014, arts. 23, 30 y 31)", f"""
{unidad("4.1 Forman parte del ordenamiento una vez publicados (art. 96.1)",
  lit("CE", "Artículo 96", ["una vez publicados oficialmente en España, formarán parte del ordenamiento interno", "en la forma prevista en los propios tratados o de acuerdo con las normas generales del Derecho internacional"], solo=[1]),
  fichab("Recepción de los tratados en el Derecho interno",
         "—",
         ["Requisitos: **válidamente celebrados** y **publicados oficialmente** en España", "Solo se derogan, modifican o suspenden según el **propio tratado** o las **normas generales del Derecho internacional**"],
         "—",
         "Una **ley** interna **no** puede derogar ni modificar un tratado. Lo repite la Ley 25/2014, art. 28.1."))}

{unidad("4.2 Publicación íntegra en el BOE (Código Civil, art. 1.5)",
  lit("CC", "a1", ["mediante su publicación íntegra en el «Boletín Oficial del Estado»"], solo=[6], titulo="Artículo 1.5 (Código Civil)"),
  fichab("Aplicación directa de los tratados",
         "—",
         "No son de aplicación directa en España hasta que se publiquen **íntegramente** en el **«Boletín Oficial del Estado»**",
         "—",
         "Es el **BOE**, no el Boletín Oficial de las Cortes Generales; y la publicación, no la ratificación ni la adopción (pregunta oficial P 50, → Cierre 1)."))}

{unidad("4.3 Publicación y entrada en vigor (Ley 25/2014, art. 23)",
  lit("L25_2014", "a23", ["se publicarán íntegramente en el «Boletín Oficial del Estado»", "formarán parte del ordenamiento jurídico interno una vez publicados"]),
  fichab("Momento de la publicación",
         "—",
         ["Publicación **íntegra** en el BOE, al tiempo de la entrada en vigor para España o **antes**", "Con aplicación provisional: publicación **inmediata**"],
         "—",
         f"Tres normas dicen lo mismo con palabras distintas: art. 96.1 CE («publicados oficialmente en España»), CC 1.5 ({c('CC', 'a1', 'publicación íntegra en el «Boletín Oficial del Estado»')}) y Ley 25/2014, art. 23.3."))}

{unidad("4.4 Aplicación directa, ejecución y prevalencia (Ley 25/2014, arts. 30 y 31)",
  lit("L25_2014", "a30", ["serán de aplicación directa, a menos que de su texto se desprenda"]),
  lit("L25_2014", "a31", ["prevalecerán sobre cualquier otra norma del ordenamiento interno en caso de conflicto con ellas, salvo las normas de rango constitucional"]),
  fichab("Eficacia interna del tratado",
         ["El **Gobierno** remite a las Cortes los proyectos de ley necesarios", "Gobierno, Comunidades Autónomas y Ciudades de Ceuta y Melilla, en sus competencias, adoptan las medidas de ejecución"],
         ["**Aplicación directa**, salvo que el texto la condicione a leyes o reglamentos", "**Prevalencia** sobre cualquier norma interna en caso de conflicto, **salvo** las de **rango constitucional**"],
         "—",
         "Prevalecen sobre las **leyes**, pero **no** sobre la **Constitución**: un tratado contrario a ella exige la **previa revisión constitucional** (art. 95 → V.3.1)."))}
""", 2)

T.ap("s16", "V.5 Denuncia (art. 96.2 CE; Ley 25/2014, art. 37)", f"""
{unidad("5.1 Mismo procedimiento que para su aprobación (art. 96.2)",
  lit("CE", "Artículo 96", ["el mismo procedimiento previsto para su aprobación en el artículo 94"], solo=[2]),
  fichab("Denuncia de los tratados",
         "—",
         "Por el **mismo procedimiento** que para su aprobación (art. 94)",
         "—",
         "Si el tratado necesitó autorización de las Cortes, la **denuncia** también."))}

{unidad("5.2 Denuncia y suspensión en la Ley 25/2014 (art. 37)",
  lit("L25_2014", "a37", ["podrá acordar la denuncia o la suspensión", "solo podrán ser denunciados previa autorización de las Cortes Generales", "informará inmediatamente a las Cortes Generales"], solo=[1, 3, 4]),
  fichab("Quién denuncia o suspende un tratado",
         ["El **Consejo de Ministros**, a propuesta del Ministro de Asuntos Exteriores y de Cooperación", "Las **Cortes Generales** autorizan la denuncia de los tratados de los arts. 93 y 94.1"],
         "Conforme a las normas del propio tratado o a las normas generales de Derecho Internacional",
         "—",
         "Los tratados de los arts. **93 y 94.1** solo se denuncian **previa autorización** de las Cortes. Del resto, el Gobierno **informa inmediatamente**."))}

{resumen([
  "Tratado: acuerdo **escrito**, regido por el **Derecho Internacional**, **cualquiera que sea su denominación** (Ley 25/2014, art. 2 a); los acuerdos **no normativos** no son fuente de obligaciones internacionales (art. 43).",
  "Consiente el **Rey** (63.2); **ley orgánica** para ceder el ejercicio de competencias (93); **autorización previa** de las Cortes en los cinco casos del 94.1, por **mayoría de cada Cámara** empezando por el **Congreso** (74.2).",
  "Tratado contrario a la CE: **revisión constitucional previa**; requieren al TC el **Gobierno** o **cualquiera de las Cámaras**; declaración **vinculante** (95 CE; LOTC 78).",
  "Forman parte del ordenamiento **una vez publicados** (96.1 CE; publicación **íntegra en el BOE**, CC 1.5); **prevalecen** sobre las normas internas **salvo** las constitucionales (Ley 25/2014, art. 31); denuncia por el procedimiento del **art. 94** (96.2)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_P50 = examen("P", 50, {
  "a": f"La adopción solo expresa el acuerdo sobre el **texto** (Ley 25/2014, art. 2 h: {c('L25_2014', 'a2', 'acto por el que España expresa su acuerdo sobre el texto de un tratado internacional')}); no lo incorpora al ordenamiento.",
  "b": f"Literal del art. 1.5 CC: no son de aplicación directa {c('CC', 'a1', 'en tanto no hayan pasado a formar parte del ordenamiento interno mediante su publicación íntegra en el «Boletín Oficial del Estado»')}.",
  "c": f"Cambia el acto y el órgano: el Congreso no ratifica; las Cortes **autorizan** en los casos del art. 94.1 CE ({c('CE', 'Artículo 94', 'requerirá la previa autorización de las Cortes Generales')}), y lo que integra el tratado es su **publicación**.",
  "d": f"Cambia el diario: es el {c('CC', 'a1', 'Boletín Oficial del Estado')}, no el Boletín Oficial de las Cortes Generales."},
  [("Oficial del Estado", "CC", "a1", "mediante su publicación íntegra en el «Boletín Oficial del Estado»"),
   ("publicado", "L25_2014", "a23", "Los tratados internacionales formarán parte del ordenamiento jurídico interno una vez publicados en el «Boletín Oficial del Estado»")])
EX_L46 = examen("L", 46, {
  "a": f"Ni los tratados ni la jurisprudencia están en el art. 1.1: los tratados se aplican al publicarse (art. 1.5) y la jurisprudencia {c('CC', 'a1', 'complementará el ordenamiento jurídico')} (art. 1.6).",
  "b": "Ni los reglamentos aparecen como fuente separada ni la doctrina del Tribunal Supremo es fuente: la jurisprudencia complementa el ordenamiento (art. 1.6).",
  "c": f"Cambia dos de las tres: faltan la costumbre y los principios generales; la jurisprudencia {c('CC', 'a1', 'complementará el ordenamiento jurídico')}.",
  "d": f"Literal del art. 1.1 CC: {c('CC', 'a1', 'Las fuentes del ordenamiento jurídico español son la ley, la costumbre y los principios generales del derecho')}."},
  [("la costumbre y los principios generales del derecho", "CC", "a1", "Las fuentes del ordenamiento jurídico español son la ley, la costumbre y los principios generales del derecho")])
EX_P49 = examen("P", 49, {
  "a": f"Las «Órdenes» son la forma de las disposiciones de los Ministros ({c('LGOB', 'a24', 'Órdenes Ministeriales, las disposiciones y resoluciones de los Ministros')}), no del Consejo de Ministros.",
  "b": "La Ley 50/1997 no prevé «Resoluciones del Consejo de Ministros» como forma de sus decisiones (art. 24.1).",
  "c": f"No existen «Reglamentos del Consejo de Ministros» como forma: sus normas reglamentarias se aprueban por {c('LGOB', 'a24', 'Reales Decretos acordados en Consejo de Ministros')} (art. 24.1 c).",
  "d": f"Literal del art. 24.1 d): {c('LGOB', 'a24', 'Acuerdos del Consejo de Ministros, las decisiones de dicho órgano colegiado que no deban adoptar la forma de Real Decreto')}."},
  [("Acuerdos del Consejo de Ministros", "LGOB", "a24", "Acuerdos del Consejo de Ministros, las decisiones de dicho órgano colegiado que no deban adoptar la forma de Real Decreto")])
EX_X65 = examen("X", 65, {
  "a": f"El Tribunal Constitucional controla solo {c('CE', 'Artículo 153', 'la constitucionalidad de sus disposiciones normativas con fuerza de ley')} (art. 153 a), no los reglamentos.",
  "b": f"El Gobierno controla, previo dictamen del Consejo de Estado, {c('CE', 'Artículo 153', 'el del ejercicio de funciones delegadas')} (art. 153 b).",
  "c": "Ningún Ministerio aparece en el art. 153 como órgano de control.",
  "d": f"Literal del art. 153 c): {c('CE', 'Artículo 153', 'Por la jurisdicción contencioso-administrativa, el de la administración autónoma y sus normas reglamentarias')}."},
  [("jurisdicción contencioso-administrativa", "CE", "Artículo 153", "Por la jurisdicción contencioso-administrativa, el de la administración autónoma y sus normas reglamentarias")])
EX_X9 = examen("X", 9, {
  "a": f"Sí es susceptible: art. 27.2 d) LOTC, {c('LOTC', 'aveintisiete', 'Los Reglamentos de las Cámaras y de las Cortes Generales')}.",
  "b": f"Sí es susceptible: art. 27.2 c) LOTC, {c('LOTC', 'aveintisiete', 'Los Tratados Internacionales')}.",
  "c": f"Sí es susceptible: art. 27.2 a) LOTC, {c('LOTC', 'aveintisiete', 'Los Estatutos de Autonomía y las demás Leyes orgánicas')}.",
  "d": f"No está en el art. 27.2 LOTC: la ordenanza fiscal es una norma **reglamentaria** local ({c('LRBRL', 'a106', 'La potestad reglamentaria de las entidades locales en materia tributaria se ejercerá a través de Ordenanzas fiscales reguladoras de sus tributos propios')}: Ley 7/1985, art. 106.2), y la jurisdicción contencioso-administrativa conoce {c('LJCA', 'Artículo 1', 'con las disposiciones generales de rango inferior a la Ley')} (LJCA, art. 1.1)."},
  [("Ordenanza fiscal", "LRBRL", "a106", "La potestad reglamentaria de las entidades locales en materia tributaria se ejercerá a través de Ordenanzas fiscales")])

T.ap("s17", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayó **una** pregunta asignada a este tema (tratados: art. 1.5 del Código Civil) y **cuatro** relacionadas con él (fuentes del art. 1.1 CC, forma de las decisiones del Consejo de Ministros, control de los reglamentos autonómicos y tratados como objeto de control de constitucionalidad). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-P 2025, pregunta 50 · Publicación de los tratados (→ V.4.2)", EX_P50,
  "### GACE-L 2025, pregunta 46 · Fuentes del ordenamiento (relacionada; → IV.1.1)", EX_L46,
  "### GACE-P 2025, pregunta 49 · Forma de las decisiones del Consejo de Ministros (relacionada; → II.1.1)", EX_P49,
  "### GACE-L 2025 extraordinario, pregunta 65 · Control de los reglamentos autonómicos (relacionada; → III.4.2)", EX_X65,
  "### GACE-L 2025 extraordinario, pregunta 9 · El tratado, objeto de declaración de inconstitucionalidad (relacionada; → V.3.3)", EX_X9,
  "### Cómo se pregunta",
  "!> Las preguntas citan el **artículo** (1.1 y 1.5 CC, 24 Ley 50/1997, 153 CE, 27 LOTC) y cambian **un órgano o un diario** (Congreso por Cortes, BOCG por BOE), **una fuente** (jurisprudencia o tratados por costumbre y principios) o meten en la lista una norma **sin rango de ley** (una ordenanza).",
]))

T.ap("s18", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Concepto | Potestad reglamentaria del Gobierno «de acuerdo con la Constitución y las leyes» (97 CE); titulares (LPAC 128.1) | **Gobierno**, **CC. AA.** y **entes locales**; reglamentos ejecutivos, **previo dictamen del Consejo de Estado** |
| II. Clases | Real Decreto (Presidente o Consejo de Ministros), Acuerdo, Orden Ministerial (Ley 50/1997, art. 24) | Jerarquía: **1.º Reales Decretos, 2.º Órdenes**; decisiones sin forma de Real Decreto: **Acuerdos** |
| III. Límites y control | No vulnerar CE ni leyes; no tipificar ni crear tributos (128.2); nulidad (47.2); inderogabilidad singular (37); buena regulación y publicación (129 y 131) | Consulta pública **≥ 15 días naturales**; audiencia **≥ 15 días hábiles** (7 si urgente); control **contencioso** directo e indirecto |
| IV. Principios generales | Ley, costumbre y principios generales (CC 1.1); en defecto de ley o costumbre, y carácter informador (CC 1.4) | La **jurisprudencia** no es fuente: **complementa** (CC 1.6) |
| V. Tratados | Ley orgánica (93); autorización previa (94.1); revisión constitucional previa (95); publicación (96.1, CC 1.5) | **Publicación íntegra en el BOE**; prevalecen salvo sobre la **Constitución** |

?> **Trampas frecuentes:** «el reglamento puede **tipificar** infracciones si lo autoriza un Ministro» (no puede tipificar, art. 128.2); «la jerarquía es Real Decreto del Presidente > Real Decreto del Consejo de Ministros» (están en el **mismo** escalón); «la jurisprudencia es fuente del ordenamiento» (la **complementa**); «el tratado se integra al **ratificarlo el Congreso**» (al **publicarse en el BOE**); «el control previo lo piden **50 Diputados**» (el **Gobierno** o **cualquiera de las Cámaras**); «los tratados prevalecen también sobre la Constitución» (**salvo** las normas de rango constitucional).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
Q = T.q
Q("CE", "Artículo 97", "Concepto", "Según el artículo 97 de la Constitución, el Gobierno ejerce la potestad reglamentaria:",
  ["De acuerdo con la Constitución y las leyes.", "De acuerdo con las leyes orgánicas y los Estatutos de Autonomía.", "Por delegación de las Cortes Generales.", "Bajo la dirección del Consejo de Estado."],
  "Art. 97 CE: «Ejerce la función ejecutiva y la potestad reglamentaria de acuerdo con la Constitución y las leyes».", "Ejerce la función ejecutiva y la potestad reglamentaria de acuerdo con la Constitución y las leyes")
Q("L39", "Artículo 128", "Concepto", "Según el artículo 128.1 de la Ley 39/2015, el ejercicio de la potestad reglamentaria corresponde:",
  ["Al Gobierno de la Nación, a los órganos de Gobierno de las Comunidades Autónomas y a los órganos de gobierno locales.", "Exclusivamente al Gobierno de la Nación.", "Al Gobierno de la Nación y a las Asambleas Legislativas de las Comunidades Autónomas.", "Al Gobierno de la Nación y a los Delegados del Gobierno en las Comunidades Autónomas."],
  "Art. 128.1 Ley 39/2015.", "El ejercicio de la potestad reglamentaria corresponde al Gobierno de la Nación, a los órganos de Gobierno de las Comunidades Autónomas")
Q("LGOB", "a5", "Concepto", "Según el artículo 5.1 h) de la Ley 50/1997, del Gobierno, el Consejo de Ministros aprueba los reglamentos para el desarrollo y la ejecución de las leyes:",
  ["Previo dictamen del Consejo de Estado.", "Previa autorización de las Cortes Generales.", "Previo informe del Tribunal Supremo.", "Previa convalidación del Congreso de los Diputados."],
  "Art. 5.1 h) Ley 50/1997.", "Aprobar los reglamentos para el desarrollo y la ejecución de las leyes, previo dictamen del Consejo de Estado")
Q("LGOB", "a4", "Concepto", "Según el artículo 4.1 b) de la Ley 50/1997, los Ministros ejercen la potestad reglamentaria:",
  ["En las materias propias de su Departamento.", "En cualquier materia, por delegación del Presidente del Gobierno.", "Solo cuando lo autorice el Consejo de Estado.", "En ningún caso: corresponde en exclusiva al Consejo de Ministros."],
  "Art. 4.1 b) Ley 50/1997.", "Ejercer la potestad reglamentaria en las materias propias de su Departamento")
Q("LRBRL", "Artículo 4", "Concepto", "Según el artículo 4.1 a) de la Ley 7/1985, reguladora de las Bases del Régimen Local, a los municipios, las provincias y las islas les corresponden en todo caso, dentro de la esfera de sus competencias:",
  ["Las potestades reglamentaria y de autoorganización.", "Las potestades legislativa y reglamentaria.", "La potestad reglamentaria, solo si la delega la Comunidad Autónoma.", "La potestad de dictar decretos-leyes en su ámbito territorial."],
  "Art. 4.1 a) Ley 7/1985.", "Las potestades reglamentaria y de autoorganización")
Q("LGOB", "a24", "Clases", "Según el artículo 24.1 c) de la Ley 50/1997, las decisiones que aprueben normas reglamentarias de la competencia del Consejo de Ministros revisten la forma de:",
  ["Reales Decretos acordados en Consejo de Ministros.", "Órdenes Ministeriales.", "Acuerdos del Consejo de Ministros.", "Reales Decretos del Presidente del Gobierno."],
  "Art. 24.1 c) Ley 50/1997.", "Reales Decretos acordados en Consejo de Ministros, las decisiones que aprueben normas reglamentarias de la competencia de éste")
Q("LGOB", "a24", "Clases", "Según el artículo 24.1 f) de la Ley 50/1997, cuando una disposición de los Ministros afecte a varios Departamentos revestirá la forma de:",
  ["Orden del Ministro de la Presidencia, dictada a propuesta de los Ministros interesados.", "Real Decreto acordado en Consejo de Ministros.", "Orden conjunta de todos los Ministros interesados, sin intervención de otro Ministro.", "Acuerdo de la Comisión General de Secretarios de Estado y Subsecretarios."],
  "Art. 24.1 f) Ley 50/1997.", "revestirá la forma de Orden del Ministro de la Presidencia, dictada a propuesta de los Ministros interesados")
Q("LGOB", "a24", "Clases", "Según el artículo 24.2 de la Ley 50/1997, en la jerarquía de los reglamentos, las disposiciones aprobadas por Real Decreto del Presidente del Gobierno:",
  ["Ocupan el mismo lugar que las aprobadas por Real Decreto acordado en Consejo de Ministros.", "Son superiores a las aprobadas por Real Decreto acordado en Consejo de Ministros.", "Son inferiores a las aprobadas por Orden Ministerial.", "Ocupan el mismo lugar que las aprobadas por Orden Ministerial."],
  "Art. 24.2 Ley 50/1997: 1.º Real Decreto del Presidente del Gobierno o acordado en el Consejo de Ministros; 2.º Orden Ministerial.", "Disposiciones aprobadas por Real Decreto del Presidente del Gobierno o acordado en el Consejo de Ministros")
Q("L39", "Artículo 128", "Clases", "Según el artículo 128.3 de la Ley 39/2015, las disposiciones administrativas se ajustarán al orden de jerarquía que establezcan:",
  ["Las leyes.", "Los Estatutos de Autonomía.", "Los propios reglamentos.", "El Consejo de Estado."],
  "Art. 128.3 Ley 39/2015.", "Las disposiciones administrativas se ajustarán al orden de jerarquía que establezcan las leyes")
Q("LO3_1980", "aveintidos", "Clases", "Según el artículo 22 de la Ley Orgánica 3/1980, del Consejo de Estado, sobre los reglamentos o disposiciones de carácter general que se dicten en ejecución de las Leyes, así como sus modificaciones, deberá ser consultado:",
  ["La Comisión Permanente del Consejo de Estado.", "El Pleno del Consejo de Estado.", "La Comisión de Estudios del Consejo de Estado.", "El Consejo de Estado solo cuando lo pida el Congreso."],
  "Art. 22.Tres LO 3/1980 (Comisión Permanente).", "Reglamentos o disposiciones de carácter general que se dicten en ejecución de las Leyes, así como sus modificaciones")
Q("L39", "Artículo 129", "Clases", "Según el artículo 129.4 de la Ley 39/2015, las habilitaciones para el desarrollo reglamentario de una ley serán conferidas, con carácter general:",
  ["Al Gobierno.", "A los titulares de los departamentos ministeriales.", "A las Autoridades Independientes.", "A la Secretaría General Técnica del Ministerio competente."],
  "Art. 129.4, párrafo tercero, Ley 39/2015 (la atribución directa a los Ministros es excepcional).", "Las habilitaciones para el desarrollo reglamentario de una ley serán conferidas, con carácter general, al Gobierno")
Q("L39", "Artículo 128", "Límites", "Según el artículo 128.2 de la Ley 39/2015, los reglamentos, sin perjuicio de su función de desarrollo o colaboración con respecto a la ley:",
  ["No podrán tipificar delitos, faltas o infracciones administrativas.", "Podrán tipificar infracciones administrativas leves.", "Podrán establecer tributos si lo autoriza el Consejo de Ministros.", "Podrán establecer sanciones cuando lo prevea una Orden Ministerial."],
  "Art. 128.2 Ley 39/2015.", "no podrán tipificar delitos, faltas o infracciones administrativas")
Q("L39", "Artículo 128", "Límites", "Según el artículo 128.2 de la Ley 39/2015, los reglamentos no podrán regular aquellas materias que la Constitución o los Estatutos de Autonomía reconocen de la competencia de:",
  ["Las Cortes Generales o de las Asambleas Legislativas de las Comunidades Autónomas.", "El Consejo de Estado o de los órganos consultivos autonómicos.", "Los Tribunales de Justicia.", "Los órganos de gobierno locales."],
  "Art. 128.2 Ley 39/2015.", "de la competencia de las Cortes Generales o de las Asambleas Legislativas de las Comunidades Autónomas")
Q("L39", "Artículo 47", "Límites", "Según el artículo 47.2 de la Ley 39/2015, las disposiciones administrativas que regulen materias reservadas a la Ley son:",
  ["Nulas de pleno derecho.", "Anulables.", "Válidas, pero ineficaces hasta su convalidación.", "Irregulares no invalidantes."],
  "Art. 47.2 Ley 39/2015.", "También serán nulas de pleno derecho las disposiciones administrativas que vulneren la Constitución, las leyes u otras disposiciones administrativas de rango superior, las que regulen materias reservadas a la Ley")
Q("L39", "Artículo 47", "Límites", "Según el artículo 47.2 de la Ley 39/2015, son nulas de pleno derecho las disposiciones administrativas que establezcan la retroactividad de:",
  ["Disposiciones sancionadoras no favorables o restrictivas de derechos individuales.", "Cualquier disposición, sea o no favorable.", "Disposiciones favorables a los interesados.", "Disposiciones organizativas."],
  "Art. 47.2 Ley 39/2015.", "las que establezcan la retroactividad de disposiciones sancionadoras no favorables o restrictivas de derechos individuales")
Q("L39", "Artículo 37", "Límites", "Según el artículo 37.1 de la Ley 39/2015, las resoluciones administrativas de carácter particular no podrán vulnerar lo establecido en una disposición de carácter general:",
  ["Aunque procedan de un órgano de igual o superior jerarquía al que dictó la disposición general.", "Salvo que procedan de un órgano de superior jerarquía al que dictó la disposición general.", "Salvo que procedan del mismo órgano que dictó la disposición general.", "Salvo que las dicte el Consejo de Ministros."],
  "Art. 37.1 Ley 39/2015 (inderogabilidad singular).", "aunque aquéllas procedan de un órgano de igual o superior jerarquía al que dictó la disposición general")
Q("L39", "Artículo 129", "Límites", "Según el artículo 129.1 de la Ley 39/2015, en el ejercicio de la potestad reglamentaria la adecuación a los principios de buena regulación quedará suficientemente justificada, en los proyectos de reglamento:",
  ["En el preámbulo.", "En la exposición de motivos.", "En el dictamen del Consejo de Estado.", "En una disposición adicional."],
  "Art. 129.1 Ley 39/2015: exposición de motivos (anteproyectos de ley) o preámbulo (proyectos de reglamento).", "En la exposición de motivos o en el preámbulo, según se trate, respectivamente, de anteproyectos de ley o de proyectos de reglamento")
Q("L39", "Artículo 129", "Límites", "¿Cuál de los siguientes NO figura entre los principios de buena regulación del artículo 129.1 de la Ley 39/2015?",
  ["Jerarquía.", "Proporcionalidad.", "Seguridad jurídica.", "Eficiencia."],
  "Art. 129.1: necesidad, eficacia, proporcionalidad, seguridad jurídica, transparencia y eficiencia.", "necesidad, eficacia, proporcionalidad, seguridad jurídica, transparencia, y eficiencia")
Q("L39", "Artículo 131", "Límites", "Según el artículo 131 de la Ley 39/2015, los reglamentos y disposiciones administrativas habrán de publicarse para que entren en vigor y produzcan efectos jurídicos:",
  ["En el diario oficial correspondiente.", "En el tablón de anuncios del órgano que los dicte.", "En la sede electrónica del Ministerio, en todo caso, sin diario oficial.", "En el Boletín Oficial de las Cortes Generales."],
  "Art. 131 Ley 39/2015.", "habrán de publicarse en el diario oficial correspondiente para que entren en vigor y produzcan efectos jurídicos")
Q("L39", "Artículo 132", "Límites", "Según el artículo 132.2 de la Ley 39/2015, una vez aprobado, el Plan Anual Normativo se publicará:",
  ["En el Portal de la Transparencia de la Administración Pública correspondiente.", "En el Boletín Oficial de las Cortes Generales.", "En la sede del Consejo de Estado.", "En el tablón edictal único."],
  "Art. 132.2 Ley 39/2015.", "el Plan Anual Normativo se publicará en el Portal de la Transparencia de la Administración Pública correspondiente")
Q("L39", "Artículo 133", "Límites", "Según el artículo 133.4 de la Ley 39/2015, podrá prescindirse de los trámites de consulta, audiencia e información públicas en el caso de normas:",
  ["Presupuestarias u organizativas.", "Sancionadoras.", "Tributarias.", "Que afecten a derechos e intereses legítimos de las personas."],
  "Art. 133.4 Ley 39/2015.", "en el caso de normas presupuestarias u organizativas")
Q("LGOB", "a23", "Límites", "Según el artículo 23 de la Ley 50/1997, los reglamentos del Gobierno que impongan nuevas obligaciones a quienes desempeñen una actividad económica o profesional preverán el comienzo de su vigencia:",
  ["El 2 de enero o el 1 de julio siguientes a su aprobación.", "El 1 de enero o el 1 de julio siguientes a su aprobación.", "A los veinte días de su publicación, en todo caso.", "El 1 de enero del año siguiente a su aprobación."],
  "Art. 23 Ley 50/1997.", "preverán el comienzo de su vigencia el 2 de enero o el 1 de julio siguientes a su aprobación")
Q("LGOB", "a25", "Límites", "Según el artículo 25.4 de la Ley 50/1997, el Ministro de la Presidencia elevará el Plan Anual Normativo al Consejo de Ministros para su aprobación:",
  ["Antes del 30 de abril.", "Antes del 31 de enero.", "Antes del 30 de junio.", "Antes del 30 de septiembre."],
  "Art. 25.4 Ley 50/1997.", "El Ministro de la Presidencia elevará el Plan al Consejo de Ministros para su aprobación antes del 30 de abril")
Q("LGOB", "a26", "Límites", "Según el artículo 26.2 de la Ley 50/1997, el tiempo para emitir opinión en la consulta pública previa en ningún caso será inferior a:",
  ["Quince días naturales.", "Quince días hábiles.", "Diez días naturales.", "Un mes."],
  "Art. 26.2 Ley 50/1997.", "que en ningún caso será inferior a quince días naturales")
Q("LGOB", "a26", "Límites", "Según el artículo 26.6 de la Ley 50/1997, el plazo mínimo del trámite de audiencia e información públicas será de:",
  ["15 días hábiles, que podrá reducirse hasta un mínimo de siete días hábiles cuando razones debidamente motivadas lo justifiquen.", "15 días naturales, que podrá reducirse hasta un mínimo de diez días naturales.", "Un mes, que podrá reducirse a quince días hábiles.", "20 días hábiles, sin posibilidad de reducción."],
  "Art. 26.6 Ley 50/1997.", "El plazo mínimo de esta audiencia e información públicas será de 15 días hábiles, y podrá ser reducido hasta un mínimo de siete días hábiles")
Q("LGOB", "a26", "Límites", "Según el artículo 26.5 de la Ley 50/1997, los proyectos de disposiciones reglamentarias deberán ser informados en todo caso por:",
  ["La Secretaría General Técnica del Ministerio o Ministerios proponentes.", "El Consejo de Estado en Pleno.", "La Abogacía General del Estado.", "El Tribunal de Cuentas."],
  "Art. 26.5 Ley 50/1997.", "deberán ser informados por la Secretaría General Técnica del Ministerio o Ministerios proponentes")
Q("CE", "Artículo 106", "Control", "Según el artículo 106.1 de la Constitución, la potestad reglamentaria la controlan:",
  ["Los Tribunales.", "Las Cortes Generales.", "El Consejo de Estado.", "El Defensor del Pueblo."],
  "Art. 106.1 CE.", "Los Tribunales controlan la potestad reglamentaria")
Q("LJCA", "Artículo 26", "Control", "Según el artículo 26.2 de la Ley 29/1998, la falta de impugnación directa de una disposición general o la desestimación del recurso que frente a ella se hubiera interpuesto:",
  ["No impiden la impugnación de los actos de aplicación fundada en que la disposición no es conforme a Derecho.", "Impiden impugnar los actos de aplicación por ese motivo.", "Solo permiten impugnar los actos de aplicación ante el Tribunal Constitucional.", "Obligan a plantear la cuestión de inconstitucionalidad."],
  "Art. 26.2 LJCA (recurso indirecto).", "no impiden la impugnación de los actos de aplicación con fundamento en lo dispuesto en el apartado anterior")
Q("LJCA", "Artículo 27", "Control", "Según el artículo 27.3 de la Ley 29/1998, sin necesidad de plantear cuestión de ilegalidad, anulará cualquier disposición general cuando, en cualquier grado, conozca de un recurso contra un acto fundado en la ilegalidad de aquella norma:",
  ["El Tribunal Supremo.", "La Audiencia Nacional.", "El Tribunal Constitucional.", "Cualquier Juzgado de lo Contencioso-administrativo."],
  "Art. 27.3 LJCA.", "Sin necesidad de plantear cuestión de ilegalidad, el Tribunal Supremo anulará cualquier disposición general")
Q("CC", "a1", "Principios generales", "Según el artículo 1.4 del Código Civil, los principios generales del derecho se aplicarán:",
  ["En defecto de ley o costumbre, sin perjuicio de su carácter informador del ordenamiento jurídico.", "Con preferencia a la costumbre.", "Solo cuando hayan sido probados por quien los alega.", "En defecto de ley, antes que la costumbre."],
  "Art. 1.4 CC.", "Los principios generales del derecho se aplicarán en defecto de ley o costumbre, sin perjuicio de su carácter informador del ordenamiento jurídico")
Q("CC", "a1", "Principios generales", "Según el artículo 1.3 del Código Civil, la costumbre sólo regirá en defecto de ley aplicable, siempre que no sea contraria a la moral o al orden público, y que:",
  ["Resulte probada.", "Esté recogida en una ordenanza.", "Haya sido reconocida por el Tribunal Supremo.", "Tenga una antigüedad mínima de diez años."],
  "Art. 1.3 CC.", "y que resulte probada")
Q("CC", "a1", "Principios generales", "Según el artículo 1.6 del Código Civil, la jurisprudencia:",
  ["Complementará el ordenamiento jurídico con la doctrina que, de modo reiterado, establezca el Tribunal Supremo.", "Es fuente del ordenamiento jurídico con el mismo rango que la ley.", "Se aplicará en defecto de ley, costumbre y principios generales del derecho.", "Complementará el ordenamiento con la doctrina de cualquier Tribunal Superior de Justicia."],
  "Art. 1.6 CC.", "La jurisprudencia complementará el ordenamiento jurídico con la doctrina que, de modo reiterado, establezca el Tribunal Supremo")
Q("CE", "Artículo 9", "Principios generales", "¿Cuál de los siguientes NO figura entre los principios que garantiza el artículo 9.3 de la Constitución?",
  ["La autonomía de los municipios.", "La publicidad de las normas.", "La seguridad jurídica.", "La interdicción de la arbitrariedad de los poderes públicos."],
  "Art. 9.3 CE: legalidad, jerarquía normativa, publicidad de las normas, irretroactividad…, seguridad jurídica, responsabilidad e interdicción de la arbitrariedad.", "La Constitución garantiza el principio de legalidad, la jerarquía normativa, la publicidad de las normas")
Q("L25_2014", "a2", "Tratados", "Según el artículo 2 a) de la Ley 25/2014, de Tratados y otros Acuerdos Internacionales, el tratado internacional es un acuerdo celebrado por escrito entre España y otro u otros sujetos de Derecho Internacional, y regido por el Derecho Internacional:",
  ["Cualquiera que sea su denominación.", "Siempre que se denomine «tratado».", "Siempre que conste en un instrumento único.", "Siempre que lo haya autorizado el Consejo de Estado."],
  "Art. 2 a) Ley 25/2014.", "ya conste en un instrumento único o en dos o más instrumentos conexos y cualquiera que sea su denominación")
Q("L25_2014", "a43", "Tratados", "Según el artículo 43 de la Ley 25/2014, los acuerdos internacionales no normativos:",
  ["No constituyen fuente de obligaciones internacionales.", "Constituyen fuente de obligaciones internacionales una vez publicados en el BOE.", "Requieren la autorización previa de las Cortes Generales.", "Solo pueden celebrarlos el Gobierno y los departamentos ministeriales."],
  "Art. 43 Ley 25/2014.", "Los acuerdos internacionales no normativos no constituyen fuente de obligaciones internacionales")
Q("CE", "Artículo 63", "Tratados", "Según el artículo 63.2 de la Constitución, manifestar el consentimiento del Estado para obligarse internacionalmente por medio de tratados corresponde:",
  ["Al Rey.", "Al Presidente del Gobierno.", "A las Cortes Generales.", "Al Ministro de Asuntos Exteriores."],
  "Art. 63.2 CE.", "Al Rey corresponde manifestar el consentimiento del Estado para obligarse internacionalmente por medio de tratados")
Q("CE", "Artículo 93", "Tratados", "Según el artículo 93 de la Constitución, la celebración de tratados por los que se atribuya a una organización o institución internacional el ejercicio de competencias derivadas de la Constitución se podrá autorizar mediante:",
  ["Ley orgánica.", "Ley ordinaria.", "Acuerdo del Consejo de Ministros.", "Real Decreto-ley."],
  "Art. 93 CE.", "Mediante ley orgánica se podrá autorizar la celebración de tratados")
Q("CE", "Artículo 94", "Tratados", "Según el artículo 94.1 de la Constitución, requerirá la previa autorización de las Cortes Generales la prestación del consentimiento del Estado para obligarse por tratados o convenios:",
  ["Que impliquen obligaciones financieras para la Hacienda Pública.", "De carácter cultural.", "De cooperación técnica entre administraciones.", "Que no exijan medidas legislativas para su ejecución."],
  "Art. 94.1 d) CE.", "Tratados o convenios que impliquen obligaciones financieras para la Hacienda Pública")
Q("CE", "Artículo 74", "Tratados", "Según el artículo 74.2 de la Constitución, las decisiones de las Cortes Generales previstas en el artículo 94.1 se adoptarán:",
  ["Por mayoría de cada una de las Cámaras, iniciándose el procedimiento en el Congreso.", "Por mayoría de cada una de las Cámaras, iniciándose el procedimiento en el Senado.", "Por mayoría absoluta del Congreso en una votación final sobre el conjunto.", "En sesión conjunta de ambas Cámaras."],
  "Art. 74.2 CE.", "se adoptarán por mayoría de cada una de las Cámaras. En el primer caso, el procedimiento se iniciará por el Congreso")
Q("CE", "Artículo 95", "Tratados", "Según el artículo 95.2 de la Constitución, pueden requerir al Tribunal Constitucional para que declare si existe contradicción entre un tratado y la Constitución:",
  ["El Gobierno o cualquiera de las Cámaras.", "Cincuenta Diputados o cincuenta Senadores.", "El Defensor del Pueblo.", "El Consejo de Estado."],
  "Art. 95.2 CE.", "El Gobierno o cualquiera de las Cámaras puede requerir al Tribunal Constitucional")
Q("LOTC", "asetentayocho", "Tratados", "Según el artículo 78.2 de la Ley Orgánica 2/1979, del Tribunal Constitucional, la declaración que emita el Tribunal sobre la contradicción entre la Constitución y un tratado:",
  ["Tendrá carácter vinculante.", "Tendrá carácter consultivo.", "Solo será vinculante si la aprueba el Pleno del Congreso.", "Deberá ser ratificada por el Consejo de Estado."],
  "Art. 78.2 LOTC.", "tendrá carácter vinculante")
Q("L25_2014", "a15", "Tratados", "Según el artículo 15.2 de la Ley 25/2014, la aplicación provisional no podrá autorizarse respecto de los tratados internacionales a que se refiere:",
  ["El artículo 93 de la Constitución.", "El artículo 94.2 de la Constitución.", "El artículo 96.2 de la Constitución.", "El artículo 63.2 de la Constitución."],
  "Art. 15.2 Ley 25/2014.", "La aplicación provisional no podrá autorizarse respecto de los tratados internacionales a que se refiere el artículo 93 de la Constitución Española")
Q("CE", "Artículo 96", "Tratados", "Según el artículo 96.1 de la Constitución, las disposiciones de los tratados internacionales válidamente celebrados y publicados sólo podrán ser derogadas, modificadas o suspendidas:",
  ["En la forma prevista en los propios tratados o de acuerdo con las normas generales del Derecho internacional.", "Por ley orgánica.", "Por ley ordinaria posterior.", "Por acuerdo del Consejo de Ministros, en todo caso."],
  "Art. 96.1 CE.", "Sus disposiciones sólo podrán ser derogadas, modificadas o suspendidas en la forma prevista en los propios tratados o de acuerdo con las normas generales del Derecho internacional")
Q("L25_2014", "a31", "Tratados", "Según el artículo 31 de la Ley 25/2014, las normas jurídicas contenidas en los tratados internacionales válidamente celebrados y publicados oficialmente prevalecerán sobre cualquier otra norma del ordenamiento interno en caso de conflicto con ellas:",
  ["Salvo las normas de rango constitucional.", "Salvo las leyes orgánicas.", "Sin excepción alguna.", "Salvo las leyes posteriores al tratado."],
  "Art. 31 Ley 25/2014.", "prevalecerán sobre cualquier otra norma del ordenamiento interno en caso de conflicto con ellas, salvo las normas de rango constitucional")
Q("CE", "Artículo 96", "Tratados", "Según el artículo 96.2 de la Constitución, para la denuncia de los tratados y convenios internacionales se utilizará:",
  ["El mismo procedimiento previsto para su aprobación en el artículo 94.", "Un acuerdo del Consejo de Ministros, en todo caso.", "Una ley orgánica.", "El procedimiento de reforma constitucional."],
  "Art. 96.2 CE.", "se utilizará el mismo procedimiento previsto para su aprobación en el artículo 94")
T.real("P", 50, "Tratados")

# Flashcards
for q_, a_, cat in [
  ("¿Quién ejerce la potestad reglamentaria según el art. 97 CE y cómo?", "El Gobierno, de acuerdo con la Constitución y las leyes.", "Concepto"),
  ("Titulares de la potestad reglamentaria (Ley 39/2015, art. 128.1)", "Gobierno de la Nación; órganos de Gobierno de las CC. AA. (según sus Estatutos); órganos de gobierno locales.", "Concepto"),
  ("¿Qué reglamentos aprueba el Consejo de Ministros previo dictamen del Consejo de Estado? (Ley 50/1997, art. 5.1 h)", "Los reglamentos para el desarrollo y la ejecución de las leyes.", "Concepto"),
  ("Potestad reglamentaria de los Ministros (Ley 50/1997, art. 4.1 b)", "En las materias propias de su Departamento.", "Concepto"),
  ("Forma de los reglamentos del Consejo de Ministros (Ley 50/1997, art. 24.1 c)", "Reales Decretos acordados en Consejo de Ministros.", "Clases"),
  ("Forma de las disposiciones de los Ministros (art. 24.1 f)", "Órdenes Ministeriales; si afectan a varios Departamentos, Orden del Ministro de la Presidencia a propuesta de los interesados.", "Clases"),
  ("Jerarquía de los reglamentos (Ley 50/1997, art. 24.2)", "1.º Real Decreto del Presidente o acordado en Consejo de Ministros; 2.º Orden Ministerial.", "Clases"),
  ("¿Qué órgano del Consejo de Estado dictamina los reglamentos ejecutivos? (LO 3/1980, art. 22)", "La Comisión Permanente (también los que ejecutan tratados o Derecho de la UE).", "Clases"),
  ("Límites del art. 128.2 de la Ley 39/2015", "No vulnerar la CE ni las leyes; no regular materias de las Cortes o Asambleas; no tipificar delitos, faltas o infracciones ni establecer penas o sanciones; no establecer tributos ni prestaciones personales o patrimoniales.", "Límites"),
  ("Disposiciones nulas de pleno derecho (Ley 39/2015, art. 47.2)", "Las que vulneren la CE, las leyes u otras de rango superior; las que regulen materias reservadas a la Ley; las que establezcan la retroactividad de disposiciones sancionadoras no favorables o restrictivas de derechos individuales.", "Límites"),
  ("Inderogabilidad singular (Ley 39/2015, art. 37)", "Las resoluciones particulares no pueden vulnerar una disposición general, aunque procedan de un órgano de igual o superior jerarquía.", "Límites"),
  ("Principios de buena regulación (Ley 39/2015, art. 129.1)", "Necesidad, eficacia, proporcionalidad, seguridad jurídica, transparencia y eficiencia.", "Límites"),
  ("Plazos de la consulta pública y de la audiencia (Ley 50/1997, art. 26)", "Consulta: no inferior a 15 días naturales. Audiencia: mínimo 15 días hábiles, reducible a 7 días hábiles.", "Límites"),
  ("Entrada en vigor de normas que imponen nuevas obligaciones a actividades económicas (Ley 50/1997, art. 23)", "El 2 de enero o el 1 de julio siguientes a su aprobación.", "Límites"),
  ("Recurso indirecto contra reglamentos (LJCA, art. 26)", "Impugnación de los actos de aplicación fundada en que la disposición no es conforme a Derecho, aunque no se recurriera directamente.", "Control"),
  ("Fuentes del ordenamiento (CC, art. 1.1)", "La ley, la costumbre y los principios generales del derecho.", "Principios generales"),
  ("¿Cuándo se aplican los principios generales del derecho? (CC, art. 1.4)", "En defecto de ley o costumbre, sin perjuicio de su carácter informador del ordenamiento jurídico.", "Principios generales"),
  ("Papel de la jurisprudencia (CC, art. 1.6)", "Complementa el ordenamiento con la doctrina reiterada del Tribunal Supremo.", "Principios generales"),
  ("Tratados que exigen ley orgánica (art. 93 CE)", "Los que atribuyen a una organización o institución internacional el ejercicio de competencias derivadas de la Constitución.", "Tratados"),
  ("Casos de autorización previa de las Cortes (art. 94.1 CE)", "Tratados políticos; militares; que afecten a la integridad territorial o a los derechos y deberes del Título I; con obligaciones financieras para la Hacienda Pública; que modifiquen o deroguen leyes o exijan medidas legislativas.", "Tratados"),
  ("¿Cuándo forma parte del ordenamiento un tratado? (art. 96.1 CE; CC 1.5)", "Una vez publicado oficialmente en España: publicación íntegra en el BOE.", "Tratados"),
  ("Prevalencia de los tratados (Ley 25/2014, art. 31)", "Sobre cualquier norma interna en caso de conflicto, salvo las de rango constitucional.", "Tratados"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Potestad reglamentaria", "Poder de dictar reglamentos, que la Constitución atribuye al Gobierno «de acuerdo con la Constitución y las leyes» (art. 97) y la Ley 39/2015 también a las CC. AA. y a los entes locales (art. 128.1).", "s1", "Reglamento")
T.glos("Real Decreto acordado en Consejo de Ministros", "Forma de las decisiones que aprueban normas reglamentarias de la competencia del Consejo de Ministros (Ley 50/1997, art. 24.1 c).", "s3", "Reglamento")
T.glos("Orden Ministerial", "Forma de las disposiciones y resoluciones de los Ministros; segundo escalón de la jerarquía reglamentaria (Ley 50/1997, art. 24.1 f y 24.2).", "s3", "Reglamento")
T.glos("Reglamento ejecutivo", "Reglamento o disposición de carácter general que se dicta en ejecución de las Leyes; requiere dictamen de la Comisión Permanente del Consejo de Estado (LO 3/1980, art. 22.Tres; Ley 50/1997, art. 5.1 h).", "s4", "Reglamento")
T.glos("Inderogabilidad singular", "Regla por la que una resolución particular no puede vulnerar una disposición general, aunque proceda de un órgano de igual o superior jerarquía (Ley 39/2015, art. 37).", "s6", "Reglamento")
T.glos("Principios de buena regulación", "Necesidad, eficacia, proporcionalidad, seguridad jurídica, transparencia y eficiencia, que deben justificarse en el preámbulo del reglamento (Ley 39/2015, art. 129.1).", "s7", "Reglamento")
T.glos("Memoria del Análisis de Impacto Normativo", "Documento preceptivo que elabora el centro directivo competente en la elaboración de normas del Gobierno (Ley 50/1997, art. 26.3).", "s8", "Reglamento")
T.glos("Recurso indirecto", "Impugnación de los actos de aplicación de una disposición general fundada en que esta no es conforme a Derecho (LJCA, art. 26).", "s9", "Reglamento")
T.glos("Cuestión de ilegalidad", "La que debe plantear el juez que dictó sentencia firme estimatoria por ilegalidad de la disposición general aplicada, ante el Tribunal competente para el recurso directo (LJCA, art. 27.1).", "s9", "Reglamento")
T.glos("Principios generales del derecho", "Tercera fuente del ordenamiento (CC 1.1); se aplican en defecto de ley o costumbre, sin perjuicio de su carácter informador del ordenamiento (CC 1.4).", "s10", "Principios generales")
T.glos("Tratado internacional", "Acuerdo celebrado por escrito entre España y otro u otros sujetos de Derecho Internacional, regido por el Derecho Internacional, cualquiera que sea su denominación (Ley 25/2014, art. 2 a).", "s12", "Tratados")
T.glos("Acuerdo internacional no normativo", "Acuerdo que contiene declaraciones de intenciones o compromisos de actuación y no constituye fuente de obligaciones internacionales (Ley 25/2014, arts. 2 c y 43).", "s12", "Tratados")
T.glos("Aplicación provisional", "Aplicación, total o parcial, de un tratado antes de su entrada en vigor, autorizada por el Consejo de Ministros; no cabe para los tratados del art. 93 CE (Ley 25/2014, art. 15).", "s13", "Tratados")
T.glos("Control previo de los tratados", "Requerimiento al Tribunal Constitucional del Gobierno o de cualquiera de las Cámaras para que declare si un tratado contradice la Constitución; la declaración es vinculante (art. 95 CE; LOTC, art. 78).", "s14", "Tratados")

# Cronología (fechas de los metadatos del BOE)
T.hito("1889", "Real Decreto de 24 de julio de 1889 por el que se publica el Código Civil (Gaceta de Madrid de 25-7-1889)", "Art. 1: fuentes del ordenamiento, principios generales del derecho y publicación de los tratados", "normativo", "s10")
T.hito("1978", "Constitución Española (27-12-1978; BOE de 29-12-1978)", "Arts. 93 a 97: tratados y potestad reglamentaria del Gobierno; art. 106.1: control judicial", "normativo", "s1")
T.hito("1979", "Ley Orgánica 2/1979, de 3 de octubre, del Tribunal Constitucional (BOE de 5-10-1979)", "Art. 78: control previo de los tratados", "normativo", "s14")
T.hito("1997", "Ley 50/1997, de 27 de noviembre, del Gobierno (BOE de 28-11-1997)", "Art. 24: forma y jerarquía de los reglamentos del Gobierno", "normativo", "s3")
T.hito("1998", "Ley 29/1998, de 13 de julio, reguladora de la Jurisdicción Contencioso-administrativa (BOE de 14-7-1998)", "Arts. 26 y 27: recurso indirecto y cuestión de ilegalidad", "normativo", "s9")
T.hito("2014", "Ley 25/2014, de 27 de noviembre, de Tratados y otros Acuerdos Internacionales (BOE de 28-11-2014)", "Celebración, publicación y aplicación de los tratados", "normativo", "s12")
T.hito("2015", "Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común (BOE de 2-10-2015)", "Título VI (arts. 127 a 133): potestad reglamentaria y buena regulación", "normativo", "s6")
T.hito("2018", "STC 55/2018, de 24 de mayo (según las notas del BOE al texto consolidado de la Ley 39/2015)", "Declara contrarios al orden constitucional de competencias, en los términos que citan las notas, los arts. 129, 130, 132 y 133, y nulos dos incisos del art. 129.4", "jurisprudencia", "s7")

T.publicar()
