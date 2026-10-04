# -*- coding: utf-8 -*-
"""Tema II.4 (B2T04): Las fuentes del derecho de la Unión Europea. Derecho originario.
Derecho derivado: Reglamentos, directivas y decisiones. Otras fuentes. Las relaciones
entre el Derecho de la Unión Europea y el ordenamiento jurídico de los Estados miembros.
Método del I.2. Normas: TUE (arts. 6 y 51) y TFUE (arts. 216, 267 y 288 a 292), versión
consolidada de EUR-Lex (DO C 202 de 7-6-2016); Carta de los Derechos Fundamentales de la
UE (arts. 51 a 53); Declaración n.º 17 aneja al Acta Final de Lisboa; CE, arts. 93 a 96;
LOPJ, art. 4 bis (BOE). Fuentes oficiales que no son texto legal (se citan literales, con
su etiqueta): sentencias del TJUE en EUR-Lex (Van Gend & Loos, Costa/ENEL, Van Duyn,
Simmenthal, Francovich), síntesis y glosario de EUR-Lex, y la Declaración del Tribunal
Constitucional 1/2004 (buscador oficial del TC). Todas se cargan con boe/eurdoc.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *
from plantilla import _norm

CORTO["CDFUE"] = "Carta de los Derechos Fundamentales de la UE"
CORTO["LOPJ"] = "LOPJ"

# --- Fuentes oficiales que no son texto legal -----------------------------------
EURLEX = "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:"
URL = {
  "SINT_FUENTES": "https://eur-lex.europa.eu/ES/legal-content/summary/sources-of-european-union-law.html",
  "SINT_PRIMARIO": "https://eur-lex.europa.eu/ES/legal-content/summary/the-european-union-s-primary-law.html",
  "SINT_DERIVADO": "https://eur-lex.europa.eu/ES/legal-content/summary/the-european-union-s-secondary-law.html",
  "SINT_ATIPICOS": "https://eur-lex.europa.eu/ES/legal-content/summary/atypical-acts.html",
  "SINT_EFECTO": "https://eur-lex.europa.eu/ES/legal-content/summary/the-direct-effect-of-european-union-law.html",
  "GLOS_PRIMACIA": "https://eur-lex.europa.eu/ES/legal-content/glossary/primacy-of-eu-law-precedence-supremacy.html",
  "GLOS_JERARQUIA": "https://eur-lex.europa.eu/ES/legal-content/glossary/eu-hierarchy-of-norms.html",
  "STJ_VANGEND": EURLEX + "61962CJ0026", "STJ_COSTA": EURLEX + "61964CJ0006", "STJ_VANDUYN": EURLEX + "61974CJ0041",
  "STJ_SIMMENTHAL": EURLEX + "61977CJ0106", "STJ_FRANCOVICH": EURLEX + "61990CJ0006",
  "DTC1_2004": "https://hj.tribunalconstitucional.es/es-ES/Resolucion/Show/6945",
}
COD = {"STJ_VANGEND": "TJUE", "STJ_COSTA": "TJUE", "STJ_VANDUYN": "TJUE", "STJ_SIMMENTHAL": "TJUE", "STJ_FRANCOVICH": "TJUE", "DTC1_2004": "TC"}
T_ = "Texto"   # bloque único de los textos cargados con eurdoc.py


def doc(k, cab, frases, resaltar=()):
    """Bloque literal de una fuente oficial que no es texto legal: primera línea
    [[COD|url]], cabecera en negrita que lo dice y frases comprobadas una a una."""
    t = texto(k, T_)
    out = []
    for f in frases:
        assert _norm(f) in _norm(t), ("FUENTE NO LITERAL", k, f)
        for r in resaltar:
            if r in f: f = f.replace(r, "**" + r + "**", 1)
        out.append(f)
    for r in resaltar: assert any(r in f for f in frases), ("NEGRITA NO LITERAL", k, r)
    return "\n".join([f"> [[{COD.get(k, 'DOUE')}|{URL[k]}]]", "> **" + cab + "**"] + ["> " + x for x in out])


def cs(k, frag): return c(k, T_, frag)


NOLEGAL = "*Esquema de elaboración propia: resume los artículos y documentos citados; no es texto legal.*"

T = Tema("B2T04",
  "Cuatro preguntas: I. Qué son las fuentes y qué es el Derecho originario (TUE, arts. 6 y 51; Carta, arts. 51 a 53) · II. Qué es el Derecho derivado: reglamentos, directivas y decisiones (TFUE, arts. 288 a 292) · III. Qué otras fuentes hay (TUE, art. 6.3; TFUE, art. 216) · IV. Cómo se relaciona el Derecho de la Unión con el de los Estados miembros: primacía, efecto directo, cuestión prejudicial (TFUE, art. 267; LOPJ, art. 4 bis) y CE, arts. 93 a 96. Cada artículo: texto literal (EUR-Lex o BOE) y ficha.",
  ["Fuentes del Derecho de la UE", "Derecho originario", "Carta de los Derechos Fundamentales", "Art. 288 TFUE", "Reglamento", "Directiva", "Decisión", "Actos delegados", "Actos de ejecución", "Principios generales", "Acuerdos internacionales", "Primacía", "Efecto directo", "Cuestión prejudicial", "Arts. 93-96 CE"])

# =============================================================================
T.ap("s0", "Mapa del tema: cuatro preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque II, tema 4):
> Las fuentes del derecho de la Unión Europea. Derecho originario. Derecho derivado: Reglamentos, directivas y decisiones. Otras fuentes. Las relaciones entre el Derecho de la Unión Europea y el ordenamiento jurídico de los Estados miembros.

### El hilo conductor

El epígrafe se lee como **cuatro preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Tratados y Carta (EUR-Lex) | Otras fuentes |
|---|---|---|---|
| **I** | ¿Qué fuentes tiene el Derecho de la Unión y qué es el Derecho originario? | TUE, arts. 6.1, 6.2 y 51; Carta, arts. 51 a 53 | Síntesis y glosario de EUR-Lex |
| **II** | ¿Qué es el Derecho derivado? Reglamentos, directivas y decisiones | TFUE, arts. 288 a 292 | Síntesis de EUR-Lex |
| **III** | ¿Qué otras fuentes hay? | TUE, art. 6.3; TFUE, art. 216 | Síntesis de EUR-Lex (jurisprudencia, actos atípicos) |
| **IV** | ¿Cómo se relaciona el Derecho de la Unión con el de los Estados miembros? | Declaración n.º 17; TFUE, art. 267 | Sentencias del TJUE; CE, arts. 93 a 96; LOPJ, art. 4 bis; Declaración del TC 1/2004 |

!> **La idea que une los cuatro bloques:** en la cúspide están los **Tratados** y la **Carta**, con el mismo valor jurídico (I). Con base en ellos, las instituciones adoptan **reglamentos, directivas y decisiones** (II). Completan el sistema los **principios generales** y los **acuerdos internacionales** (III). Y ese Derecho **prima** sobre el de los Estados y puede tener **efecto directo**, con el **juez nacional** como aplicador ordinario y el **TJUE** como intérprete (IV); en España, la puerta es el **art. 93 CE**.

### Cómo está escrito

- Cada artículo: primero el **texto literal** (EUR-Lex, etiqueta DOUE; o BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- La primacía y el efecto directo **no están escritos en los Tratados**: se citan **literalmente** la Declaración n.º 17 y las sentencias del TJUE (etiqueta TJUE), y como orientación las síntesis oficiales de EUR-Lex. Todo lo que no es texto legal lo dice en su cabecera.
- Fronteras con otros temas: Tratados originarios y modificativos, arts. 1 a 8 TUE y competencias (tema II.1); instituciones y procedimiento legislativo, arts. 293 a 297 TFUE (tema II.2); Tribunal de Justicia y recursos (tema II.3).
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué fuentes tiene el Derecho de la Unión y qué es el Derecho originario?", donde(
  "Primera pregunta. Antes de estudiar cada acto, hay que tener el **mapa de las fuentes** y saber qué está en la cúspide: los **Tratados** y, con su mismo valor, la **Carta de los Derechos Fundamentales**.",
  ["1 El mapa de las fuentes (síntesis de EUR-Lex)", "2 Los Tratados y sus protocolos (art. 51 TUE)", "3 La Carta de los Derechos Fundamentales (art. 6.1 TUE; arts. 51 a 53 de la Carta)", "4 La adhesión al Convenio Europeo de Derechos Humanos (art. 6.2 TUE)"]))

T.ap("s1", "I.1 El mapa de las fuentes (síntesis y glosario de EUR-Lex)", f"""
Los Tratados no tienen un artículo que enumere «las fuentes». La clasificación que se pregunta es la de la doctrina y la que usa la propia **EUR-Lex** en sus síntesis oficiales:

{doc("SINT_FUENTES", "Síntesis de EUR-Lex «Las fuentes del Derecho de la Unión Europea» (última actualización 21.4.2022) · fuente oficial, no es texto legal", [
  "Hay tres fuentes de derecho de la UE: el Derecho primario, los principios generales del Derecho de la UE y el Derecho derivado (véase en detalle en la jerarquía de las normas).",
  "Las principales fuentes de Derecho primario son los tratados que establecen la UE: el TUE, el TFUE y el Tratado de la Comunidad Europea de la Energía Atómica (Euratom).",
  "El Derecho derivado comprende los actos unilaterales, que pueden clasificarse en dos categorías:",
  "los actos enumerados en el artículo 288 del TFUE: reglamentos, directivas, decisiones, dictámenes y recomendaciones;",
  "los que no figuran en el artículo 288 del TFUE, es decir, actos atípicos, como los reglamentos internos de las instituciones y los acuerdos interinstitucionales.",
  "Los acuerdos internacionales con países no pertenecientes a la UE o con organizaciones internacionales son también una parte integral del Derecho de la UE. Son independientes del Derecho primario y del Derecho derivado.",
  "Otras fuentes del Derecho de la UE",
  "la jurisprudencia del TJUE;",
  "el Derecho internacional: a menudo una fuente de inspiración para el TJUE en la elaboración de su jurisprudencia."],
  ["Derecho primario", "principios generales del Derecho de la UE", "Derecho derivado", "actos atípicos", "acuerdos internacionales"])}

{doc("GLOS_JERARQUIA", "Glosario de EUR-Lex «Jerarquía de las normas de la Unión Europea» · fuente oficial, no es texto legal", [
  "En la cumbre de la jerarquía de las normas de la Unión Europea (UE) es el Derecho primario, que consiste en:",
  "los tratados constitutivos de la UE [el Tratado de la Unión Europea y el Tratado de Funcionamiento de la Unión Europea (TFUE)] y sus protocolos;",
  "la Carta de los Derechos Fundamentales [artículo 6 del Tratado de la Unión Europea (TUE)]; y",
  "los principios generales establecidos por el Tribunal de Justicia de la Unión Europea.",
  "Le siguen, en orden de jerarquía, los acuerdos internacionales con países no pertenecientes a la UE o con organizaciones internacionales.",
  "La siguiente categoría es el Derecho secundario, que comprende todos los actos legislativos y no legislativos adoptados por las instituciones de la Unión que permiten que la UE ejerza sus competencias."],
  ["En la cumbre", "Le siguen", "La siguiente categoría"])}

{NOLEGAL}

| Escalón (según el glosario de EUR-Lex) | Qué incluye | Dónde se estudia |
|---|---|---|
| 1. Derecho primario u originario | Tratados (TUE, TFUE) y sus protocolos; Carta; principios generales | → I.2, → I.3 y → III.1 |
| 2. Acuerdos internacionales de la Unión | Acuerdos con terceros países u organizaciones internacionales | → III.2 |
| 3. Derecho derivado o secundario | Reglamentos, directivas, decisiones (vinculantes); recomendaciones y dictámenes (no vinculantes); actos atípicos | → II.1 a → II.3 y → III.3 |

?> Las dos síntesis no agrupan igual los **principios generales**: la de las fuentes los presenta como una fuente propia y el glosario de la jerarquía los sitúa en la cumbre, junto al Derecho primario. En el examen basta con saber que son fuente del Derecho de la Unión (art. 6.3 TUE → III.1).
""", 2)

T.ap("s2", "I.2 Los Tratados y sus protocolos: el Derecho originario (art. 51 TUE)", f"""
El Derecho originario (o primario) son los **Tratados**. El art. 1 TUE (tema II.1) dice que la Unión se fundamenta en el TUE y en el TFUE y que {c('TUE', 'Artículo 1', 'Ambos Tratados tienen el mismo valor jurídico')}. El art. 51 TUE incluye en ellos sus protocolos y anexos.

{doc("SINT_PRIMARIO", "Síntesis de EUR-Lex «El Derecho primario de la Unión Europea» (última actualización 12.10.2022) · fuente oficial, no es texto legal", [
  "Es la fuente suprema del Derecho de la Unión Europea (UE). Proviene principalmente de los tratados constitutivos, en particular, el Tratado de Roma (que se convirtió en el Tratado de Funcionamiento de la Unión Europea) y el Tratado de Maastricht (también denominado Tratado de la Unión Europea).",
  "El Derecho primario, también conocido como fuentes primarias, se deriva de los siguientes textos de la UE:",
  "tratados constitutivos;", "tratados de modificación;", "tratados de adhesión;", "protocolos anexos a los mencionados tratados;",
  "acuerdos complementarios que modifican secciones concretas de los tratados constitutivos;",
  "la Carta de los Derechos Fundamentales (desde el Tratado de Lisboa).",
  "Los tratados constitutivos son: el Tratado de París constitutivo de la Comunidad Europea del Carbón y del Acero (1951); el Tratado de Roma constitutivo de la Comunidad Económica Europea (1957); el Tratado Euratom (1957); el Tratado de Maastricht (1992).",
  "Los tratados modificativos son: el Acta Única Europea (1986); el Tratado de Ámsterdam (1997); el Tratado de Niza (2001); el Tratado de Lisboa (2007)."],
  ["fuente suprema", "Tratado de Maastricht (también denominado Tratado de la Unión Europea)"])}

{unidad("2.1 Protocolos y anexos (art. 51 TUE)",
  lit("TUE", "Artículo 51", ["forman parte integrante de los mismos"]),
  fichab("Valor de los protocolos y anexos de los Tratados",
         "—",
         "Se integran en los Tratados: tienen su mismo rango (Derecho originario)",
         "—",
         "Los **Protocolos** (por ejemplo, el del Estatuto del TJUE o el de los criterios de convergencia) **son Tratado**: no son Derecho derivado."))}

!> El **TUE** es **Derecho primario**: cayó en 2025 (→ Cierre 1). La historia de cada Tratado se estudia en el tema II.1.
""", 2)

T.ap("s3", "I.3 La Carta de los Derechos Fundamentales (art. 6.1 TUE; arts. 51 a 53 de la Carta)", f"""
{unidad("3.1 La Carta tiene el mismo valor jurídico que los Tratados (art. 6.1 TUE)",
  lit("TUE", "Artículo 6", ["tendrá el mismo valor jurídico que los Tratados", "no ampliarán en modo alguno las competencias de la Unión"], solo=[1, 2, 3]),
  fichab("Rango de la Carta de los Derechos Fundamentales de la Unión Europea",
         c("TUE", "Artículo 6", "La Unión reconoce los derechos, libertades y principios enunciados en la Carta"),
         ["Mismo valor jurídico que los Tratados: es Derecho originario", "Se interpreta con las disposiciones generales del **título VII** de la Carta y teniendo en cuenta las **explicaciones**"],
         "Fechas de la Carta: 7 de diciembre de 2000, adaptada el 12 de diciembre de 2007 en Estrasburgo",
         f"{c('TUE', 'Artículo 6', 'el **mismo** valor jurídico que los Tratados')} (no inferior ni superior). La Carta **no amplía** las competencias de la Unión."))}

{unidad("3.2 A quién obliga la Carta (art. 51 de la Carta)",
  lit("CDFUE", "Artículo 51", ["únicamente cuando apliquen el Derecho de la Unión", "ni crea ninguna competencia o misión nuevas para la Unión"]),
  fichab("Ámbito de aplicación de la Carta",
         ["Las **instituciones, órganos y organismos** de la Unión", "Los **Estados miembros**, **únicamente** cuando apliquen el Derecho de la Unión"],
         "Respetan los derechos, observan los principios y promueven su aplicación, dentro de sus competencias",
         "—",
         "A los Estados solo les vincula **cuando aplican Derecho de la Unión**. La Carta no amplía el ámbito del Derecho de la Unión ni crea competencias."))}

{unidad("3.3 Límites a los derechos y relación con el Convenio Europeo (art. 52.1 y 3 de la Carta)",
  lit("CDFUE", "Artículo 52", ["deberá ser establecida por la ley y respetar el contenido esencial", "su sentido y alcance serán iguales a los que les confiere dicho Convenio"], solo=[1, 3]),
  fichab("Cómo se pueden limitar los derechos de la Carta",
         "El legislador (por ley)",
         ["Limitación **establecida por la ley**", "Respeta el **contenido esencial**", "Respeta la **proporcionalidad**: necesaria y para objetivos de interés general o para proteger derechos de los demás"],
         "—",
         "Derechos que corresponden a los del Convenio Europeo: **igual** sentido y alcance, pero el Derecho de la Unión **puede** dar una protección más extensa."))}

{unidad("3.4 Nivel de protección (art. 53 de la Carta)",
  lit("CDFUE", "Artículo 53", ["como limitativa o lesiva"]),
  fichab("Cláusula de nivel de protección",
         "—",
         "La Carta no puede interpretarse como limitativa o lesiva de los derechos reconocidos por el Derecho de la Unión, el Derecho internacional, los convenios (en particular el Convenio Europeo) y las constituciones de los Estados miembros",
         "—",
         "La Carta **suma** protección: no rebaja la de las **constituciones** nacionales ni la del Convenio Europeo."))}
""", 2)

T.ap("s4", "I.4 La adhesión al Convenio Europeo de Derechos Humanos (art. 6.2 TUE)", f"""
{unidad("4.1 La Unión se adherirá al Convenio (art. 6.2 TUE)",
  lit("TUE", "Artículo 6", ["La Unión se adherirá", "no modificará las competencias de la Unión"], solo=[4]),
  fichab("Mandato de adhesión de la Unión al Convenio Europeo para la Protección de los Derechos Humanos",
         "La Unión",
         "Mediante un acuerdo de adhesión (su celebración: art. 218 TFUE)",
         f"En el Consejo, {c('TFUE', 'Artículo 218', 'El Consejo se pronunciará también por unanimidad sobre el acuerdo de adhesión de la Unión al Convenio Europeo')} (art. 218.8 TFUE); además, {c('TFUE', 'Artículo 218', 'previa aprobación del Parlamento Europeo')} (art. 218.6 a)",
         "«Se **adherirá**» (futuro: es un mandato). La adhesión **no modifica** las competencias de la Unión."))}

{resumen([
  "Fuentes según EUR-Lex: **Derecho primario**, **principios generales** y **Derecho derivado**; aparte, los **acuerdos internacionales**; otras: jurisprudencia del TJUE y Derecho internacional.",
  "Derecho originario: **TUE y TFUE** (mismo valor jurídico, art. 1 TUE), con sus **protocolos y anexos** (art. 51 TUE).",
  "La **Carta** tiene **el mismo valor jurídico que los Tratados** (6.1 TUE) y obliga a los Estados **solo cuando aplican Derecho de la Unión** (51 Carta).",
  "La Unión **se adherirá** al Convenio Europeo, sin modificar sus competencias (6.2 TUE)."],
  "Siguiente: II. ¿Qué es el Derecho derivado? Reglamentos, directivas y decisiones")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Qué es el Derecho derivado? Reglamentos, directivas y decisiones (arts. 288 a 292 TFUE)", donde(
  "Segunda pregunta. Con base en los Tratados, las instituciones adoptan actos jurídicos: es el **Derecho derivado**. El art. 288 TFUE enumera **cinco** actos y define la eficacia de cada uno; los arts. 289 a 291 los clasifican en legislativos, delegados y de ejecución.",
  ["1 Los cinco actos del art. 288 TFUE", "2 Actos legislativos, delegados y de ejecución (arts. 289 a 291)", "3 Las recomendaciones (art. 292) y cuadro de los actos"]))

T.ap("s5", "II.1 Los cinco actos del art. 288 TFUE", f"""
{doc("SINT_DERIVADO", "Síntesis de EUR-Lex «El Derecho derivado de la Unión Europea» (última actualización 2.12.2021) · fuente oficial, no es texto legal", [
  "El Derecho derivado de la Unión Europea (UE) es el corpus jurídico que se basa en los Tratados de la UE.",
  "Los reglamentos, las directivas y las decisiones son actos jurídicos vinculantes.",
  "Una decisión puede dirigirse a uno o varios destinatarios concretos (Estados miembros de la UE, personas físicas o jurídicas). Al mismo tiempo, existen decisiones sin destinatario específico, en particular en el ámbito de la política exterior y de seguridad común.",
  "Las recomendaciones y los dictámenes son actos jurídicos no legislativos no vinculantes."],
  ["se basa en los Tratados", "actos jurídicos vinculantes", "no vinculantes"])}

{unidad("1.1 La lista (art. 288, párrafo primero)",
  lit("TFUE", "Artículo 288", ["reglamentos, directivas, decisiones, recomendaciones y dictámenes"], solo=[1]),
  fichab("Los actos jurídicos de la Unión",
         c("TFUE", "Artículo 288", "las instituciones"),
         "Cinco tipos: reglamentos, directivas, decisiones, recomendaciones y dictámenes",
         "—",
         "Son **cinco**, y los adoptan **para ejercer las competencias de la Unión** (que son solo las atribuidas: tema II.1)."))}

{unidad("1.2 El reglamento (art. 288, párrafo segundo)",
  lit("TFUE", "Artículo 288", ["alcance general", "obligatorio en todos sus elementos", "directamente aplicable en cada Estado miembro"], solo=[2]),
  fichab("Acto de alcance general, obligatorio en todo y directamente aplicable",
         "Destinatarios: todos (alcance general)",
         ["**Alcance general**", "**Obligatorio en todos sus elementos**", "**Directamente aplicable** en cada Estado miembro"],
         "—",
         "Tres notas: alcance **general** + obligatorio en **todos sus elementos** + **directamente aplicable**. Si la opción dice «obliga en cuanto al resultado», es la directiva."))}

{unidad("1.3 La directiva (art. 288, párrafo tercero)",
  lit("TFUE", "Artículo 288", ["obligará al Estado miembro destinatario en cuanto al resultado que deba conseguirse", "la elección de la forma y de los medios"], solo=[3]),
  fichab("Acto que obliga en cuanto al resultado",
         c("TFUE", "Artículo 288", "al Estado miembro destinatario"),
         "El Estado elige **la forma y los medios** (transposición al Derecho nacional)",
         "—",
         "Obliga **en cuanto al resultado**; la **forma y los medios** quedan a las **autoridades nacionales**. Obliga al Estado **destinatario** (no «a todos los particulares»)."))}

{unidad("1.4 La decisión (art. 288, párrafo cuarto)",
  lit("TFUE", "Artículo 288", ["obligatoria en todos sus elementos", "sólo será obligatoria para éstos"], solo=[4]),
  fichab("Acto obligatorio en todos sus elementos, con o sin destinatarios",
         "Si designa destinatarios, solo ellos; si no, es obligatoria en general",
         "Obligatoria en todos sus elementos",
         "—",
         "Pregunta oficial de 2025 (→ Cierre 1): «Cuando designe destinatarios, **sólo** será obligatoria para éstos». El art. 288 no le atribuye «alcance general» ni la declara «directamente aplicable»: eso lo dice del reglamento."))}

{unidad("1.5 Recomendaciones y dictámenes (art. 288, párrafo quinto)",
  lit("TFUE", "Artículo 288", ["no serán vinculantes"], solo=[5]),
  fichab("Actos no vinculantes",
         "—",
         "Recomendaciones y dictámenes: **no vinculantes**",
         "—",
         "Los dos son actos del art. 288, pero **no vinculan**. «No será vinculante» es un distractor típico para la decisión."))}
""", 2)

T.ap("s6", "II.2 Actos legislativos, delegados y de ejecución (arts. 289 a 291 TFUE)", f"""
{unidad("2.1 Actos legislativos (art. 289)",
  lit("TFUE", "Artículo 289", ["adopción conjunta por el Parlamento Europeo y el Consejo, a propuesta de la Comisión", "constituirá un procedimiento legislativo especial", "constituirán actos legislativos"]),
  fichab("Qué hace «legislativo» a un reglamento, directiva o decisión",
         ["Procedimiento **ordinario**: Parlamento Europeo **y** Consejo, a propuesta de la Comisión", "Procedimiento **especial**: el Parlamento con participación del Consejo, o el Consejo con participación del Parlamento", "En casos previstos: iniciativa de un grupo de Estados o del Parlamento, recomendación del BCE o petición del Tribunal de Justicia o del BEI"],
         "Es acto legislativo el adoptado **mediante procedimiento legislativo** (289.3); el procedimiento ordinario se define en el art. 294 (tema II.2)",
         "—",
         "Lo legislativo depende del **procedimiento**, no del tipo de acto: un reglamento, una directiva o una decisión pueden ser legislativos o no."))}

{unidad("2.2 Actos delegados (art. 290)",
  lit("TFUE", "Artículo 290", ["delegar en la Comisión", "actos no legislativos de alcance general", "elementos no esenciales", "no podrá ser objeto de una delegación de poderes", "revocar la delegación", "por mayoría de los miembros que lo componen y el Consejo lo hará por mayoría cualificada", "«delegado» o «delegada»"]),
  fichab("Delegación de poderes en la Comisión para completar o modificar un acto legislativo",
         "Delega el **acto legislativo**; adopta el acto delegado la **Comisión**; controlan el **Parlamento Europeo** y el **Consejo**",
         ["Actos **no legislativos** de **alcance general** que completen o modifiquen elementos **no esenciales**", "El acto legislativo fija **objetivos, contenido, alcance y duración** de la delegación", "Condiciones posibles: **revocación** y **objeción** dentro del plazo fijado"],
         "Revocar u objetar: Parlamento por **mayoría de los miembros que lo componen**; Consejo por **mayoría cualificada**",
         "Los **elementos esenciales** nunca se delegan. Delegación **solo en la Comisión**. En el título: «**delegado**» o «**delegada**»."))}

{unidad("2.3 Actos de ejecución (art. 291)",
  lit("TFUE", "Artículo 291", ["Los Estados miembros adoptarán todas las medidas de Derecho interno necesarias", "conferirán competencias de ejecución a la Comisión", "al Consejo", "«de ejecución»"]),
  fichab("Ejecución de los actos jurídicamente vinculantes de la Unión",
         ["Regla: los **Estados miembros** (291.1)", "Si se requieren **condiciones uniformes**: la **Comisión**; en casos específicos debidamente justificados y en los de los arts. 24 y 26 TUE, el **Consejo** (291.2)"],
         "El Parlamento Europeo y el Consejo fijan previamente, por **reglamentos** del procedimiento legislativo ordinario, las modalidades de **control por los Estados** de las competencias de ejecución de la Comisión (291.3)",
         "—",
         "La ejecución corresponde **primero a los Estados**. En el título: «**de ejecución**». No confundir con el delegado (art. 290): **completa o modifica**; el de ejecución **ejecuta** en condiciones uniformes."))}
""", 2)

T.ap("s7", "II.3 Las recomendaciones (art. 292 TFUE) y cuadro de los actos", f"""
{unidad("3.1 Quién adopta recomendaciones (art. 292)",
  lit("TFUE", "Artículo 292", ["El Consejo adoptará recomendaciones", "Se pronunciará por unanimidad en los ámbitos en los que se requiere la unanimidad", "La Comisión, así como el Banco Central Europeo"]),
  fichab("Adopción de recomendaciones",
         ["El **Consejo**", "La **Comisión**", "El **Banco Central Europeo**, en los casos específicos previstos por los Tratados"],
         "El Consejo, a propuesta de la Comisión cuando los Tratados prevean que adopte actos a propuesta de esta",
         "Consejo: **unanimidad** en los ámbitos en que se requiera para adoptar un acto de la Unión",
         "Recomiendan el **Consejo**, la **Comisión** y el **BCE** (este, en casos previstos). La recomendación **no vincula** (288)."))}

{NOLEGAL}

| Acto (art. 288 TFUE) | ¿Vinculante? | Alcance | Rasgo que se pregunta |
|---|---|---|---|
| Reglamento | Sí, en todos sus elementos | General | **Directamente aplicable** en cada Estado miembro |
| Directiva | Sí, en cuanto al **resultado** | Estado(s) destinatario(s) | Forma y medios: **autoridades nacionales** |
| Decisión | Sí, en todos sus elementos | Con destinatarios: **solo** para ellos | Puede no designar destinatarios |
| Recomendación | **No** | — | La adoptan Consejo, Comisión y BCE (292) |
| Dictamen | **No** | — | — |

| Clase (arts. 289 a 291) | Quién lo adopta | Título del acto |
|---|---|---|
| Legislativo | Parlamento y Consejo (ordinario) o uno con participación del otro (especial) | — |
| Delegado | Comisión, por delegación de un acto legislativo | «delegado» o «delegada» |
| De ejecución | Estados miembros; en condiciones uniformes, Comisión (o Consejo) | «de ejecución» |

{resumen([
  "Art. 288: **reglamentos, directivas, decisiones, recomendaciones y dictámenes**.",
  "Reglamento: **alcance general**, obligatorio en **todos sus elementos** y **directamente aplicable**. Directiva: obliga en cuanto al **resultado**; **forma y medios**, nacionales. Decisión: obligatoria en todos sus elementos; con destinatarios, **solo para estos**. Recomendaciones y dictámenes: **no vinculantes**.",
  "Legislativo = adoptado por **procedimiento legislativo** (289). Delegado: la **Comisión**, sobre elementos **no esenciales** (290). Ejecución: los **Estados**; en condiciones uniformes, la **Comisión** o el **Consejo** (291)."],
  "Siguiente: III. ¿Qué otras fuentes hay?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Qué otras fuentes hay? Principios generales, acuerdos internacionales, jurisprudencia y actos atípicos", donde(
  "Tercera pregunta. Además de los Tratados y de los actos del art. 288, el epígrafe pide «otras fuentes»: los **principios generales** (art. 6.3 TUE), los **acuerdos internacionales** de la Unión (art. 216 TFUE) y, según EUR-Lex, la **jurisprudencia** del TJUE y los **actos atípicos**.",
  ["1 Los principios generales y los derechos fundamentales (art. 6.3 TUE)", "2 Los acuerdos internacionales (art. 216 TFUE)", "3 Jurisprudencia del TJUE y actos atípicos (síntesis de EUR-Lex)"]))

T.ap("s8", "III.1 Los principios generales y los derechos fundamentales (art. 6.3 TUE)", f"""
{unidad("1.1 Derechos fundamentales como principios generales (art. 6.3 TUE)",
  lit("TUE", "Artículo 6", ["tradiciones constitucionales comunes a los Estados miembros", "como principios generales"], solo=[5]),
  doc("SINT_FUENTES", "Síntesis de EUR-Lex «Las fuentes del Derecho de la Unión Europea» · fuente oficial, no es texto legal", [
  "Estos pueden corresponder con fuentes de Derecho no escritas desarrolladas por la jurisprudencia del Tribunal de Justicia de la Unión Europea (TJUE).",
  "Los principios generales del Derecho de la UE también pueden ser el resultado de las tradiciones constitucionales comunes a los Estados miembros."],
  ["fuentes de Derecho no escritas"]),
  fichab("Los derechos fundamentales forman parte del Derecho de la Unión como principios generales",
         "—",
         ["Los derechos que garantiza el **Convenio Europeo** (CEDH)", "Los que son fruto de las **tradiciones constitucionales comunes** a los Estados miembros"],
         "—",
         "Dos orígenes: **Convenio Europeo** y **tradiciones constitucionales comunes**. Entran «**como principios generales**», no como Derecho derivado."))}
""", 2)

T.ap("s9", "III.2 Los acuerdos internacionales de la Unión (art. 216 TFUE)", f"""
{unidad("2.1 Cuándo celebra acuerdos la Unión y a quién vinculan (art. 216)",
  lit("TFUE", "Artículo 216", ["cuando así lo prevean los Tratados", "vincularán a las instituciones de la Unión y a los Estados miembros"]),
  doc("SINT_PRIMARIO", "Síntesis de EUR-Lex «El Derecho primario de la Unión Europea» · fuente oficial, no es texto legal", [
  "Los acuerdos internacionales con países no pertenecientes a la UE o con organizaciones internacionales son también una parte integral del Derecho de la UE. Estos acuerdos son independientes del Derecho primario y del Derecho derivado, además de conformar una categoría sui generis (es decir, una categoría propia y única).",
  "De acuerdo con la sentencia del TJUE en el asunto Demirel contra Stadt Schwäbisch Gmünd, los acuerdos internacionales pueden tener efecto directo y su fuerza jurídica es superior a la del Derecho derivado, que, por lo tanto, debe cumplirlas."],
  ["sui generis", "superior a la del Derecho derivado"]),
  fichab("Acuerdos de la Unión con terceros países u organizaciones internacionales",
         "La Unión (procedimiento de negociación y celebración: art. 218 TFUE)",
         ["Cuando lo prevean los Tratados", "Cuando sea necesario para alcanzar, en el contexto de las políticas de la Unión, un objetivo de los Tratados", "Cuando esté previsto en un acto jurídicamente vinculante de la Unión", "Cuando pueda afectar a normas comunes o alterar su alcance"],
         "—",
         "Vinculan **a las instituciones de la Unión y a los Estados miembros** (216.2)."))}

?> Un acuerdo internacional que la Unión quiera celebrar puede someterse al **dictamen del Tribunal de Justicia**: {c('TFUE', 'Artículo 218', 'En caso de dictamen negativo del Tribunal de Justicia, el acuerdo previsto no podrá entrar en vigor, salvo modificación de éste o revisión de los Tratados')} (art. 218.11 TFUE). Por eso los acuerdos están **por debajo de los Tratados**; y, según la síntesis de EUR-Lex citada arriba, su fuerza jurídica es **superior a la del Derecho derivado**.
""", 2)

T.ap("s10", "III.3 Jurisprudencia del TJUE y actos atípicos (síntesis de EUR-Lex)", f"""
La **jurisprudencia** del TJUE es la vía por la que se han formulado los principios de **primacía** y **efecto directo** (→ IV.1 y → IV.2). El TJUE {c('TUE', 'Artículo 19', 'Garantizará el respeto del Derecho en la interpretación y aplicación de los Tratados')} (art. 19.1 TUE; su organización, tema II.3).

{doc("SINT_PRIMARIO", "Síntesis de EUR-Lex «El Derecho primario de la Unión Europea» · fuente oficial, no es texto legal", [
  "Además del Derecho primario, el Derecho de la UE se basa en fuentes secundarias y complementarias.",
  "Las fuentes complementarias incluyen la jurisprudencia del Tribunal de Justicia de la UE (TJUE) y los principios jurídicos generales."],
  ["fuentes complementarias"])}

{doc("SINT_ATIPICOS", "Síntesis de EUR-Lex «Actos atípicos» (última actualización 17.5.2024) · fuente oficial, no es texto legal", [
  "Los actos atípicos constituyen una categoría de actos adoptados por las instituciones de la Unión Europea (UE) y están relacionados con la organización interna de la UE. Estos actos se denominan atípicos porque no forman parte de la nomenclatura de actos jurídicos prevista en el artículo 288 del Tratado de Funcionamiento de la Unión Europea (TFUE).",
  "Los Reglamentos internos de las instituciones de la UE constituyen actos atípicos.",
  "Solo son vinculantes para la institución u organismo en cuestión.",
  "Las instituciones pueden ir más lejos y organizar su cooperación a través de acuerdos interinstitucionales (artículo 295 del TFUE). Los acuerdos de este tipo también son actos atípicos. Pueden tener un efecto vinculante pero solamente para las instituciones signatarias del acuerdo.",
  "Las instituciones de la UE utilizan toda una serie de instrumentos resultantes de la práctica. Se trata, en particular, de las declaraciones, deliberaciones, recomendaciones, resoluciones, comunicaciones, códigos de conducta, acuerdos interinstitucionales, calendarios, conclusiones y libros blancos y verdes."],
  ["no forman parte de la nomenclatura de actos jurídicos prevista en el artículo 288", "Reglamentos internos", "acuerdos interinstitucionales (artículo 295 del TFUE)"])}

{resumen([
  "Los derechos del **Convenio Europeo** y de las **tradiciones constitucionales comunes** forman parte del Derecho de la Unión **como principios generales** (6.3 TUE).",
  "Los **acuerdos internacionales** de la Unión **vinculan a las instituciones y a los Estados miembros** (216.2 TFUE); según EUR-Lex, están por encima del Derecho derivado.",
  "Fuentes complementarias (EUR-Lex): **jurisprudencia del TJUE** y **principios generales**. **Actos atípicos**: fuera de la lista del art. 288 (reglamentos internos, acuerdos interinstitucionales, comunicaciones…)."],
  "Siguiente: IV. ¿Cómo se relaciona el Derecho de la Unión con el de los Estados miembros?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Cómo se relaciona el Derecho de la Unión con el de los Estados miembros?", donde(
  "Cuarta pregunta. El Derecho de la Unión **prima** sobre el nacional y puede **aplicarse directamente** por los jueces nacionales. Ninguno de los dos principios está en el articulado de los Tratados: los formuló el **Tribunal de Justicia**, y la **Declaración n.º 17** de Lisboa lo recuerda. En España, la base es el **art. 93 CE**.",
  ["1 La primacía (Declaración n.º 17; Costa/ENEL; Simmenthal)", "2 El efecto directo y la responsabilidad del Estado (Van Gend & Loos; Van Duyn; Francovich)", "3 El juez nacional y la cuestión prejudicial (art. 267 TFUE; LOPJ, art. 4 bis)", "4 España: arts. 93 a 96 CE y la Declaración del TC 1/2004"]))

T.ap("s11", "IV.1 La primacía (Declaración n.º 17; Costa/ENEL; Simmenthal)", f"""
{unidad("1.1 La Declaración n.º 17, relativa a la primacía (Acta Final del Tratado de Lisboa)",
  lit("DECL17", T_, ["priman sobre el Derecho de los Estados miembros", "Costa/ENEL, 15 de julio de 1964, asunto 6/64", "el Tratado no contenía mención alguna a la primacía, y todavía hoy sigue sin contenerla"], solo=[2, 3, 4, 5, 6],
      titulo="Declaración n.º 17, relativa a la primacía (aneja al Acta Final de la Conferencia intergubernamental que adoptó el Tratado de Lisboa; DO C 202 de 7-6-2016, p. 344)"),
  doc("STJ_COSTA", "Sentencia del Tribunal de Justicia de 15 de julio de 1964, Costa/ENEL, asunto 6/64 (EUR-Lex; fundamentos de Derecho) · jurisprudencia, no es texto legal", [
  "Considerando que, a diferencia de los Tratados internacionales ordinarios, el Tratado de la CEE creó un ordenamiento jurídico propio, integrado en el sistema jurídico de los Estados miembros desde la entrada en vigor del Tratado, y que vincula a sus órganos jurisdiccionales;",
  "Considerando que la primacía del Derecho comunitario está confirmada por el artículo 189, a cuyo tenor los Reglamentos tienen fuerza «obligatoria» y son «directamente aplicables en cada Estado miembro»;",
  "Considerando que del conjunto de estos elementos se desprende que al Derecho creado por el Tratado, nacido de una fuente autónoma, no se puede oponer, en razón de su específica naturaleza original una norma interna, cualquiera que sea ésta, ante los órganos jurisdiccionales, sin que al mismo tiempo aquél pierda su carácter comunitario y se ponga en tela de juicio la base jurídica misma de la Comunidad;"],
  ["ordenamiento jurídico propio", "la primacía del Derecho comunitario", "no se puede oponer"]),
  doc("STJ_SIMMENTHAL", "Sentencia del Tribunal de Justicia de 9 de marzo de 1978, Simmenthal, asunto 106/77 (EUR-Lex; fallo) · jurisprudencia, no es texto legal", [
  "Los Jueces nacionales encargados de aplicar, en el marco de su competencia, las disposiciones del Derecho comunitario, están obligados a garantizar la plena eficacia de dichas normas dejando, si procede, inaplicadas, por su propia iniciativa, cualesquiera disposiciones contrarias de la legislación nacional, aunque sean posteriores, sin que estén obligados a solicitar o a esperar la derogación previa de éstas por vía legislativa o mediante otro procedimiento constitucional."],
  ["inaplicadas, por su propia iniciativa", "aunque sean posteriores"]),
  doc("GLOS_PRIMACIA", "Glosario de EUR-Lex «Primacía del Derecho de la Unión (prevalencia o supremacía)» · fuente oficial, no es texto legal", [
  "El principio de primacía del Derecho de la Unión se ha desarrollado con el paso del tiempo a partir de la jurisprudencia del Tribunal de Justicia de la Unión Europea. No está consagrado en los Tratados de la UE, aunque hay una breve declaración anexa al Tratado de Lisboa al respecto.",
  "Cuando el Derecho de la Unión prevalece sobre el Derecho interno en conflicto, las disposiciones nacionales no se anulan o invalidan automáticamente. Sin embargo, las autoridades y los órganos jurisdiccionales nacionales deben negarse a aplicar dichas disposiciones mientras esté en vigor el Derecho de la UE primordial."],
  ["No está consagrado en los Tratados", "no se anulan o invalidan automáticamente"]),
  fichab("Reconocimiento por los Estados de la primacía, sin incluirla en el articulado",
         "La **Conferencia** de los representantes de los Gobiernos de los Estados miembros; incorpora el dictamen del **Servicio Jurídico del Consejo** de 22 de junio de 2007",
         ["Los Tratados y el Derecho adoptado sobre su base **priman** sobre el Derecho de los Estados miembros", "En las **condiciones establecidas por la jurisprudencia** del TJUE"],
         "—",
         "La primacía es de **construcción jurisprudencial**: la primera sentencia es **Costa/ENEL (15-7-1964, asunto 6/64)**. Es una **declaración**, no un artículo de los Tratados."))}

?> **Primacía ≠ anulación.** La norma nacional contraria **se inaplica** (Simmenthal: «dejando, si procede, inaplicadas»); no se anula ni hay que esperar a que se derogue. Por eso es falsa la fórmula «debe inaplicarse la norma nacional **y eliminarla del ordenamiento**».
""", 2)

T.ap("s12", "IV.2 El efecto directo y la responsabilidad del Estado (Van Gend & Loos; Van Duyn; Francovich)", f"""
{doc("STJ_VANGEND", "Sentencia del Tribunal de Justicia de 5 de febrero de 1963, NV Algemene Transport- en Expeditie Onderneming van Gend & Loos, asunto 26/62 (EUR-Lex) · jurisprudencia, no es texto legal", [
  "Considerando que la Tariefcommissie plantea en primer lugar la cuestión de si el artículo 12 del Tratado tiene un efecto directo en Derecho interno, en el sentido de que los nacionales de los Estados miembros puedan invocar, basándose en este artículo, derechos que el Juez nacional deba proteger.",
  "que, por esas razones, ha de llegarse a la conclusión de que la Comunidad constituye un nuevo ordenamiento jurídico de Derecho internacional, a favor del cual los Estados miembros han limitado su soberanía, si bien en un ámbito restringido, y cuyos sujetos son, no sólo los Estados miembros, sino también sus nacionales;",
  "1) El artículo 12 del Tratado constitutivo de la Comunidad Económica Europea produce efectos directos y genera en favor de los justiciables derechos individuales que los órganos jurisdiccionales nacionales deben proteger."],
  ["nuevo ordenamiento jurídico", "produce efectos directos y genera en favor de los justiciables derechos individuales"])}

{doc("SINT_EFECTO", "Síntesis de EUR-Lex «El efecto directo del Derecho de la Unión Europea» (última actualización 25.11.2022) · fuente oficial, no es texto legal", [
  "Por lo que respecta al Derecho primario, el Tribunal estableció el principio del efecto directo en la sentencia Van Gend en Loos. No obstante, indicó como condición que las obligaciones deben ser precisas, claras, incondicionales y no deben requerir medidas complementarias, tanto de carácter nacional como europeo.",
  "El efecto directo vertical interviene en las relaciones entre los particulares y el país, lo que significa que los particulares pueden acogerse a una disposición del Derecho de la UE en relación con el Estado.",
  "El efecto directo horizontal interviene en las relaciones entre particulares, lo que significa que los particulares pueden acogerse a una disposición del Derecho de la UE en relación con otro particular.",
  "Los reglamentos son directamente aplicables en los Estados miembros, tal como se especifica en el artículo 288 del Tratado de Funcionamiento de la Unión Europea y, por tanto, tienen un efecto directo.",
  "En consecuencia, el Tribunal estableció en su sentencia Van Duyn contra Home Office que una directiva tendrá un efecto directo si sus disposiciones son incondicionales y suficientemente claras y precisas y cuando el Estado miembro no haya transpuesto la directiva antes del plazo correspondiente. Sin embargo, el efecto directo solo puede ser de carácter vertical: los Estados miembros están obligados a aplicar las directivas, pero las directivas no pueden ser invocadas por un Estado miembro contra un particular (véase la sentencia Ratti).",
  "Los dictámenes y las recomendaciones no tienen una fuerza jurídica vinculante. En consecuencia, no tienen efecto directo.",
  "Junto con la primacía del Derecho de la UE (también denominada «prioridad»), el efecto directo es un principio básico del Derecho de la UE."],
  ["estableció el principio del efecto directo en la sentencia Van Gend en Loos", "precisas, claras, incondicionales", "Van Duyn contra Home Office", "solo puede ser de carácter vertical"])}

{doc("STJ_VANDUYN", "Sentencia del Tribunal de Justicia de 4 de diciembre de 1974, Van Duyn, asunto 41/74 (EUR-Lex; fallo) · jurisprudencia, no es texto legal", [
  "1) El artículo 48 del Tratado CEE tiene efecto directo sobre el ordenamiento jurídico de los Estados miembros y otorga a los particulares derechos que los Tribunales nacionales deben tutelar."],
  ["tiene efecto directo"])}

{doc("STJ_FRANCOVICH", "Sentencia del Tribunal de Justicia de 19 de noviembre de 1991, Francovich y otros, asuntos C-6/90 y C-9/90 (EUR-Lex; fallo) · jurisprudencia, no es texto legal", [
  "2) Un Estado miembro está obligado a reparar los daños que resultan para los particulares de la no adaptación del Derecho nacional a la Directiva 80/987/CEE."],
  ["está obligado a reparar los daños"])}

{NOLEGAL}

| Sentencia (fecha) | Qué se cita de ella | Principio |
|---|---|---|
| **Van Gend & Loos** (5-2-1963, 26/62) | El art. 12 del Tratado CEE «produce efectos directos» | **Efecto directo** (lo «estableció», según la síntesis de EUR-Lex) |
| **Costa/ENEL** (15-7-1964, 6/64) | «la primacía del Derecho comunitario» | **Primacía** (primera sentencia, según la Declaración n.º 17) |
| **Van Duyn** (4-12-1974, 41/74) | Efecto directo del art. 48 CEE y de una directiva | Efecto directo de las **directivas** |
| **Simmenthal** (9-3-1978, 106/77) | El juez nacional deja **inaplicada** la norma nacional contraria | Primacía: **inaplicación** |
| **Francovich** (19-11-1991, C-6/90 y C-9/90) | El Estado está obligado a **reparar los daños** por no adaptar su Derecho a una directiva | **Responsabilidad** del Estado |
""", 2)

T.ap("s13", "IV.3 El juez nacional y la cuestión prejudicial (art. 267 TFUE; LOPJ, art. 4 bis)", f"""
{unidad("3.1 La cuestión prejudicial (art. 267 TFUE)",
  lit("TFUE", "Artículo 267", ["con carácter prejudicial", "sobre la interpretación de los Tratados", "sobre la validez e interpretación de los actos", "podrá pedir", "estará obligado a someter la cuestión al Tribunal", "con la mayor brevedad"]),
  fichab("Diálogo entre el juez nacional y el Tribunal de Justicia",
         ["Plantea: un **órgano jurisdiccional** de un Estado miembro", "Resuelve: el **Tribunal de Justicia de la Unión Europea**"],
         ["Objeto: **interpretación** de los Tratados; **validez e interpretación** de los actos de instituciones, órganos u organismos", "**Facultativa** («podrá») si estima necesaria la decisión para su fallo", "**Obligatoria** («estará obligado») si sus decisiones **no son susceptibles de ulterior recurso** judicial de Derecho interno"],
         "Persona **privada de libertad**: el TJUE se pronuncia **con la mayor brevedad**",
         "De los **Tratados** solo se pregunta la **interpretación**; de los **actos**, **validez e interpretación**. Obligan a plantearla los órganos de **última instancia**."))}

{unidad("3.2 Los jueces españoles y el Derecho de la Unión (LOPJ, art. 4 bis)",
  lit("LOPJ", "acuaobis", ["de conformidad con la jurisprudencia del Tribunal de Justicia de la Unión Europea", "mediante auto, previa audiencia de las partes"], titulo="Artículo 4 bis (LOPJ, añadido por la LO 7/2015)"),
  fichab("Aplicación del Derecho de la Unión por los Jueces y Tribunales españoles",
         "Los **Jueces y Tribunales**",
         ["Aplican el Derecho de la Unión **de conformidad con la jurisprudencia del TJUE**", "La cuestión prejudicial europea se plantea **mediante auto**, **previa audiencia de las partes**"],
         "—",
         "Forma: **auto** (no providencia ni sentencia) y **previa audiencia de las partes**."))}
""", 2)

T.ap("s14", "IV.4 España: arts. 93 a 96 CE y la Declaración del Tribunal Constitucional 1/2004", f"""
{unidad("4.1 Atribución del ejercicio de competencias (art. 93 CE)",
  lit("CE", "Artículo 93", ["Mediante ley orgánica", "el ejercicio de competencias derivadas de la Constitución", "Corresponde a las Cortes Generales o al Gobierno, según los casos, la garantía del cumplimiento"]),
  doc("DTC1_2004", "Declaración del Tribunal Constitucional 1/2004, de 13 de diciembre (BOE núm. 3, de 4 de enero de 2005), sobre el Tratado por el que se establece una Constitución para Europa (buscador oficial del TC) · doctrina, no es texto legal", [
  "Primacía y supremacía son categorías que se desenvuelven en órdenes diferenciados. Aquélla, en el de la aplicación de normas válidas; ésta, en el de los procedimientos de normación.",
  "La supremacía de la Constitución es, pues, compatible con regímenes de aplicación que otorguen preferencia aplicativa a normas de otro Ordenamiento diferente del nacional siempre que la propia Constitución lo haya así dispuesto, que es lo que ocurre exactamente con la previsión contenida en su art. 93",
  "En suma, la Constitución ha aceptado, ella misma, en virtud de su art. 93, la primacía del Derecho de la Unión en el ámbito que a ese Derecho le es propio",
  "3º Que el art. 93 de la Constitución española es suficiente para la prestación del consentimiento del Estado al Tratado referido."],
  ["Primacía y supremacía son categorías que se desenvuelven en órdenes diferenciados", "la primacía del Derecho de la Unión en el ámbito que a ese Derecho le es propio"]),
  fichab("Cauce constitucional de la integración en la Unión Europea",
         ["Autorizan: las **Cortes Generales**, por **ley orgánica**", "Garantizan el cumplimiento: las **Cortes Generales o el Gobierno**, según los casos"],
         "Tratados que atribuyen a una organización o institución internacional **el ejercicio** de competencias derivadas de la Constitución",
         "**Ley orgánica**: mayoría absoluta del Congreso en una votación final sobre el conjunto (art. 81.2 CE)",
         "Se atribuye **el ejercicio** de competencias, no su titularidad. La garantía alcanza también las **resoluciones** de los organismos titulares de la cesión."))}

{unidad("4.2 Autorización de las Cortes para otros tratados (art. 94 CE)",
  lit("CE", "Artículo 94", ["previa autorización de las Cortes Generales", "inmediatamente informados"]),
  fichab("Tratados que exigen autorización previa de las Cortes",
         "Las **Cortes Generales** (autorizan); el **Congreso y el Senado** (son informados de los demás)",
         ["Políticos", "Militares", "Integridad territorial o derechos y deberes fundamentales del Título I", "Obligaciones financieras para la Hacienda Pública", "Modificación o derogación de una ley o medidas legislativas para su ejecución"],
         "Autorización **previa**; de los restantes, información **inmediata**",
         "Son **cinco** supuestos. Los tratados de atribución de competencias del art. 93 van por **ley orgánica**, no por esta autorización."))}

{unidad("4.3 Tratados contrarios a la Constitución (art. 95 CE)",
  lit("CE", "Artículo 95", ["exigirá la previa revisión constitucional", "El Gobierno o cualquiera de las Cámaras"]),
  fichab("Control previo de constitucionalidad de los tratados",
         "Pueden requerir al **Tribunal Constitucional**: el **Gobierno** o **cualquiera de las Cámaras**",
         "Si el tratado contiene estipulaciones contrarias a la Constitución: **previa revisión constitucional**",
         "—",
         "Por esta vía el Gobierno requirió al TC en 2004 (Declaración 1/2004, → IV.4.1). El TC declara si existe **o no** contradicción."))}

{unidad("4.4 Los tratados forman parte del ordenamiento interno (art. 96 CE)",
  lit("CE", "Artículo 96", ["una vez publicados oficialmente en España, formarán parte del ordenamiento interno", "en la forma prevista en los propios tratados o de acuerdo con las normas generales del Derecho internacional"]),
  fichab("Eficacia interna de los tratados",
         "—",
         ["Válidamente celebrados + **publicados oficialmente en España** = parte del ordenamiento interno", "Solo se derogan, modifican o suspenden según **los propios tratados** o las **normas generales del Derecho internacional**"],
         "Denuncia: el **mismo procedimiento** que para su aprobación (art. 94)",
         "Requisito de la eficacia interna: la **publicación oficial en España**. Una ley posterior no puede derogar un tratado."))}

?> El Tratado examinado en la Declaración 1/2004 no llegó a ratificarse: el glosario de EUR-Lex se refiere a él como {cs('GLOS_JERARQUIA', 'el Tratado constitucional no ratificado')}. La distinción **primacía (aplicación) / supremacía (validez)** es la que se pregunta.

{resumen([
  "**Primacía**: el Derecho de la Unión prima sobre el nacional (Declaración n.º 17); primera sentencia, **Costa/ENEL (1964)**; la norma nacional contraria se **inaplica**, aunque sea posterior (**Simmenthal**). No está en el articulado de los Tratados.",
  "**Efecto directo**: **Van Gend & Loos (1963)**; directivas, **Van Duyn**; vertical (frente al Estado) y horizontal (entre particulares). **Responsabilidad del Estado**: **Francovich (1991)**.",
  "**Cuestión prejudicial** (267 TFUE): facultativa, salvo para los órganos **sin ulterior recurso**; en España, **mediante auto, previa audiencia de las partes** (LOPJ, 4 bis).",
  "España: **ley orgánica** para atribuir el ejercicio de competencias (**93 CE**); tratado contrario a la CE, **previa revisión** (95); tratados publicados, parte del **ordenamiento interno** (96). TC 1/2004: **primacía ≠ supremacía**."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_L24 = examen("L", 24, {
  "a": f"Es el **reglamento**: {c('TFUE', 'Artículo 288', 'El reglamento tendrá un alcance general')} y será {c('TFUE', 'Artículo 288', 'directamente aplicable en cada Estado miembro')}.",
  "b": f"Literal del art. 288, párrafo cuarto: {c('TFUE', 'Artículo 288', 'La decisión será obligatoria en todos sus elementos. Cuando designe destinatarios, sólo será obligatoria para éstos')}.",
  "c": f"Es la **directiva**: {c('TFUE', 'Artículo 288', 'La directiva obligará al Estado miembro destinatario en cuanto al resultado que deba conseguirse')}.",
  "d": f"Son las **recomendaciones y los dictámenes**: {c('TFUE', 'Artículo 288', 'Las recomendaciones y los dictámenes no serán vinculantes')}."},
  [("Cuando designe destinatarios, sólo será obligatoria para éstos", "TFUE", "Artículo 288", "La decisión será obligatoria en todos sus elementos. Cuando designe destinatarios, sólo será obligatoria para éstos.")])

EX_L25 = examen("L", 25, {
  "a": f"Simmenthal (1978) es posterior y trata de la **inaplicación** de la norma nacional contraria: los jueces deben garantizar la plena eficacia del Derecho comunitario {cs('STJ_SIMMENTHAL', 'dejando, si procede, inaplicadas, por su propia iniciativa, cualesquiera disposiciones contrarias de la legislación nacional')}.",
  "b": f"Van Duyn (1974) es posterior: según EUR-Lex, en ella {cs('SINT_EFECTO', 'el Tribunal estableció en su sentencia Van Duyn contra Home Office que una directiva tendrá un efecto directo')} si se cumplen ciertos requisitos; es el efecto directo **de las directivas**, no el principio.",
  "c": f"Según la síntesis oficial de EUR-Lex, {cs('SINT_EFECTO', 'el Tribunal estableció el principio del efecto directo en la sentencia Van Gend en Loos')}; su fallo (1963): el art. 12 del Tratado CEE {cs('STJ_VANGEND', 'produce efectos directos y genera en favor de los justiciables derechos individuales que los órganos jurisdiccionales nacionales deben proteger')}.",
  "d": f"Francovich (1991) es la de la **responsabilidad del Estado**: {cs('STJ_FRANCOVICH', 'Un Estado miembro está obligado a reparar los daños que resultan para los particulares de la no adaptación del Derecho nacional a la Directiva 80/987/CEE')}."},
  [("Van Gend", "SINT_EFECTO", T_, "el Tribunal estableció el principio del efecto directo en la sentencia Van Gend en Loos"),
   ("Van Gend", "STJ_VANGEND", T_, "NV (Sociedad Anónima) Algemene Transport- en Expeditie Onderneming van Gend & Loos"),
   ("Van Gend", "STJ_VANGEND", T_, "produce efectos directos y genera en favor de los justiciables derechos individuales que los órganos jurisdiccionales nacionales deben proteger")])

EX_P10 = examen("P", 10, {
  "a": f"El Derecho derivado es el {cs('SINT_DERIVADO', 'corpus jurídico que se basa en los Tratados de la UE')}: son los actos del art. 288 TFUE, no el Tratado.",
  "b": f"El TUE lo celebran Estados soberanos: {c('TUE', 'Artículo 1', 'las ALTAS PARTES CONTRATANTES constituyen entre sí una UNIÓN EUROPEA')}. No es una norma dictada por un Estado (aunque, publicado, forme parte del ordenamiento español: art. 96.1 CE).",
  "c": f"Según la síntesis oficial de EUR-Lex, {cs('SINT_FUENTES', 'Las principales fuentes de Derecho primario son los tratados que establecen la UE: el TUE, el TFUE')} y el Tratado Euratom.",
  "d": "No es un acuerdo entre Administraciones: es un tratado entre Estados que constituye la Unión (art. 1 TUE) y, con el TFUE, la fundamenta."},
  [("Derecho primario", "SINT_FUENTES", T_, "Las principales fuentes de Derecho primario son los tratados que establecen la UE: el TUE, el TFUE y el Tratado de la Comunidad Europea de la Energía Atómica (Euratom)"),
   ("Derecho primario", "SINT_PRIMARIO", T_, "el Tratado de Maastricht (también denominado Tratado de la Unión Europea)")])

EX_P16 = examen("P", 16, {
  "a": f"El efecto directo se estableció antes, en Van Gend & Loos (1963): {cs('SINT_EFECTO', 'el Tribunal estableció el principio del efecto directo en la sentencia Van Gend en Loos')}.",
  "b": f"La Declaración n.º 17 (Lisboa) recoge que la primacía es jurisprudencial y que {c('DECL17', T_, 'En el momento de la primera sentencia de esta jurisprudencia constante (Costa/ENEL, 15 de julio de 1964, asunto 6/64')}; y la sentencia: {cs('STJ_COSTA', 'la primacía del Derecho comunitario está confirmada por el artículo 189')}.",
  "c": f"La responsabilidad del Estado es de Francovich (1991): {cs('STJ_FRANCOVICH', 'Un Estado miembro está obligado a reparar los daños')}.",
  "d": f"La atribución no es creación jurisprudencial: está en los Tratados, {c('TUE', 'Artículo 5', 'La delimitación de las competencias de la Unión se rige por el principio de atribución')} (art. 5.1 TUE, tema II.1)."},
  [("Primacía", "DECL17", T_, "En el momento de la primera sentencia de esta jurisprudencia constante (Costa/ENEL, 15 de julio de 1964, asunto 6/64"),
   ("Primacía", "DECL17", T_, "la primacía del Derecho comunitario es un principio fundamental del Derecho comunitario"),
   ("Primacía", "STJ_COSTA", T_, "Considerando que la primacía del Derecho comunitario está confirmada por el artículo 189")])

T.ap("s15", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **cuatro** preguntas de este tema: una del art. 288 TFUE, dos sobre la jurisprudencia del TJUE (efecto directo y primacía) y una sobre el Derecho primario. Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto del art. 288 TFUE y, en las otras tres (que no dependen de un artículo, porque la primacía y el efecto directo no están en el articulado de los Tratados), contra la Declaración n.º 17, las sentencias del TJUE y las síntesis oficiales de EUR-Lex.",
  "### GACE-L 2025, pregunta 24 · La decisión (art. 288 TFUE) (→ II.1.4)", EX_L24,
  "### GACE-L 2025, pregunta 25 · Efecto directo: Van Gend & Loos (→ IV.2)", EX_L25,
  "### GACE-P 2025, pregunta 10 · El TUE es Derecho primario (→ I.2)", EX_P10,
  "### GACE-P 2025, pregunta 16 · Primacía: Costa/ENEL (→ IV.1)", EX_P16,
  "### Cómo se pregunta",
  "!> Dos estilos: **literal del art. 288** (los distractores son las definiciones de los **otros** actos: reglamento, directiva, recomendaciones y dictámenes) y **«qué sentencia / qué principio»** (los distractores son las **otras sentencias** del cuadro de → IV.2). Saber **a qué acto** corresponde cada frase y **qué dijo cada sentencia** resuelve las cuatro.",
]))

T.ap("s16", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Fuentes y Derecho originario | Tratados (mismo valor), protocolos y anexos (51 TUE); Carta con el mismo valor que los Tratados (6.1 TUE); adhesión al Convenio (6.2) | El **TUE es Derecho primario**; la Carta obliga a los Estados **solo cuando aplican** Derecho de la Unión |
| II. Derecho derivado | Cinco actos (288); legislativos (289), delegados (290), de ejecución (291); recomendaciones (292) | Reglamento **directamente aplicable**; directiva: **resultado**; decisión: **solo para sus destinatarios** |
| III. Otras fuentes | Principios generales (6.3 TUE); acuerdos internacionales (216 TFUE); jurisprudencia; actos atípicos | Los acuerdos **vinculan a instituciones y Estados** |
| IV. Relaciones con los Estados | Primacía (Decl. 17, Costa/ENEL, Simmenthal); efecto directo (Van Gend & Loos); cuestión prejudicial (267); arts. 93 a 96 CE | **Costa/ENEL → primacía**; **Van Gend & Loos → efecto directo**; **Francovich → responsabilidad** |

?> **Trampas frecuentes:** «la decisión tiene **alcance general** y es **directamente aplicable**» (eso es el **reglamento**); «la directiva obliga **en todos sus elementos**» (obliga **en cuanto al resultado**); «la Carta tiene valor **inferior** a los Tratados» (tiene el **mismo** valor); «la primacía está en un **artículo** del TFUE» (es **jurisprudencial**; la recuerda la **Declaración n.º 17**); «la norma nacional contraria **se anula**» (se **inaplica**); «el juez de última instancia **podrá** plantear la cuestión prejudicial» (**estará obligado**); «el art. 93 CE exige ley **ordinaria**» (exige **ley orgánica**).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
Q = T.q
Q("TFUE", "Artículo 288", "Derecho derivado", "Según el artículo 288 del TFUE, para ejercer las competencias de la Unión, las instituciones adoptarán:",
  ["Reglamentos, directivas, decisiones, recomendaciones y dictámenes.", "Reglamentos, directivas, decisiones marco y posiciones comunes.", "Reglamentos, directivas y decisiones, únicamente.", "Tratados, reglamentos, directivas y decisiones."],
  "Art. 288, párrafo primero, TFUE: cinco actos.", "las instituciones adoptarán reglamentos, directivas, decisiones, recomendaciones y dictámenes")
Q("TFUE", "Artículo 288", "Derecho derivado", "Según el artículo 288 del TFUE, el reglamento:",
  ["Tendrá un alcance general, será obligatorio en todos sus elementos y directamente aplicable en cada Estado miembro.", "Obligará al Estado miembro destinatario en cuanto al resultado que deba conseguirse.", "Será obligatorio solo para sus destinatarios.", "No será vinculante."],
  "Art. 288, párrafo segundo, TFUE.", "El reglamento tendrá un alcance general. Será obligatorio en todos sus elementos y directamente aplicable en cada Estado miembro.")
Q("TFUE", "Artículo 288", "Derecho derivado", "Según el artículo 288 del TFUE, la directiva obligará al Estado miembro destinatario:",
  ["En cuanto al resultado que deba conseguirse, dejando a las autoridades nacionales la elección de la forma y de los medios.", "En todos sus elementos, y será directamente aplicable.", "En cuanto a la forma y los medios, dejando a las autoridades nacionales la elección del resultado.", "Solo si el Estado la ha ratificado por ley orgánica."],
  "Art. 288, párrafo tercero, TFUE.", "La directiva obligará al Estado miembro destinatario en cuanto al resultado que deba conseguirse, dejando, sin embargo, a las autoridades nacionales la elección de la forma y de los medios.")
Q("TFUE", "Artículo 288", "Derecho derivado", "Según el artículo 288 del TFUE, ¿qué actos no serán vinculantes?",
  ["Las recomendaciones y los dictámenes.", "Las decisiones sin destinatario.", "Las directivas no transpuestas.", "Los reglamentos de ejecución."],
  "Art. 288, párrafo quinto, TFUE.", "Las recomendaciones y los dictámenes no serán vinculantes.")
Q("TFUE", "Artículo 288", "Derecho derivado", "Según el artículo 288 del TFUE, cuando una decisión designe destinatarios:",
  ["Sólo será obligatoria para éstos.", "Será obligatoria para todos los Estados miembros.", "No será vinculante para los destinatarios.", "Solo obligará en cuanto al resultado."],
  "Art. 288, párrafo cuarto, TFUE.", "Cuando designe destinatarios, sólo será obligatoria para éstos.")
Q("TFUE", "Artículo 289", "Derecho derivado", "Según el artículo 289 del TFUE, el procedimiento legislativo ordinario consiste en la adopción de un reglamento, una directiva o una decisión:",
  ["Conjuntamente por el Parlamento Europeo y el Consejo, a propuesta de la Comisión.", "Por el Consejo, previa consulta al Parlamento Europeo.", "Por la Comisión, a propuesta del Consejo.", "Por el Consejo Europeo, a propuesta de la Comisión."],
  "Art. 289.1 TFUE.", "adopción conjunta por el Parlamento Europeo y el Consejo, a propuesta de la Comisión")
Q("TFUE", "Artículo 289", "Derecho derivado", "Según el artículo 289.3 del TFUE, constituirán actos legislativos:",
  ["Los actos jurídicos que se adopten mediante procedimiento legislativo.", "Todos los reglamentos, cualquiera que sea su procedimiento de adopción.", "Los actos que adopte la Comisión por delegación.", "Las recomendaciones del Consejo."],
  "Art. 289.3 TFUE.", "Los actos jurídicos que se adopten mediante procedimiento legislativo constituirán actos legislativos.")
Q("TFUE", "Artículo 290", "Actos delegados", "Según el artículo 290 del TFUE, un acto legislativo podrá delegar los poderes para adoptar actos no legislativos de alcance general que completen o modifiquen determinados elementos no esenciales del acto legislativo en:",
  ["La Comisión.", "El Consejo.", "Los Estados miembros.", "El Parlamento Europeo."],
  "Art. 290.1 TFUE.", "Un acto legislativo podrá delegar en la Comisión los poderes para adoptar actos no legislativos de alcance general")
Q("TFUE", "Artículo 290", "Actos delegados", "Según el artículo 290 del TFUE, la regulación de los elementos esenciales de un ámbito:",
  ["Estará reservada al acto legislativo y no podrá ser objeto de una delegación de poderes.", "Podrá delegarse en la Comisión por un plazo máximo de cinco años.", "Podrá delegarse en el Consejo por unanimidad.", "Corresponderá a los actos de ejecución."],
  "Art. 290.1, párrafo segundo, TFUE.", "La regulación de los elementos esenciales de un ámbito estará reservada al acto legislativo y, por lo tanto, no podrá ser objeto de una delegación de poderes.")
Q("TFUE", "Artículo 290", "Actos delegados", "Según el artículo 290.2 del TFUE, a efectos de revocar la delegación o de formular objeciones, el Parlamento Europeo se pronunciará:",
  ["Por mayoría de los miembros que lo componen, y el Consejo por mayoría cualificada.", "Por mayoría de los votos emitidos, y el Consejo por unanimidad.", "Por mayoría de dos tercios, y el Consejo por mayoría simple.", "Por mayoría de los miembros que lo componen, y el Consejo por unanimidad."],
  "Art. 290.2 TFUE.", "el Parlamento Europeo se pronunciará por mayoría de los miembros que lo componen y el Consejo lo hará por mayoría cualificada")
Q("TFUE", "Artículo 290", "Actos delegados", "Según el artículo 290.3 del TFUE, en el título de los actos delegados figurará:",
  ["El adjetivo «delegado» o «delegada».", "La expresión «de ejecución».", "La expresión «legislativo».", "El nombre de la institución delegante."],
  "Art. 290.3 TFUE.", "En el título de los actos delegados figurará el adjetivo «delegado» o «delegada».")
Q("TFUE", "Artículo 291", "Actos de ejecución", "Según el artículo 291.1 del TFUE, ¿quién adoptará todas las medidas de Derecho interno necesarias para la ejecución de los actos jurídicamente vinculantes de la Unión?",
  ["Los Estados miembros.", "La Comisión.", "El Consejo.", "El Parlamento Europeo y el Consejo."],
  "Art. 291.1 TFUE.", "Los Estados miembros adoptarán todas las medidas de Derecho interno necesarias para la ejecución de los actos jurídicamente vinculantes de la Unión.")
Q("TFUE", "Artículo 291", "Actos de ejecución", "Según el artículo 291.2 del TFUE, cuando se requieran condiciones uniformes de ejecución, los actos jurídicamente vinculantes de la Unión conferirán competencias de ejecución, como regla, a:",
  ["La Comisión.", "El Parlamento Europeo.", "El Tribunal de Justicia.", "El Consejo Europeo."],
  "Art. 291.2 TFUE: a la Comisión o, en casos específicos debidamente justificados y en los previstos en los arts. 24 y 26 TUE, al Consejo.", "éstos conferirán competencias de ejecución a la Comisión")
Q("TFUE", "Artículo 291", "Actos de ejecución", "Según el artículo 291.4 del TFUE, en el título de los actos de ejecución figurará:",
  ["La expresión «de ejecución».", "El adjetivo «delegado» o «delegada».", "La expresión «de aplicación».", "La expresión «reglamentario»."],
  "Art. 291.4 TFUE.", "En el título de los actos de ejecución figurará la expresión «de ejecución».")
Q("TFUE", "Artículo 292", "Derecho derivado", "Según el artículo 292 del TFUE, el Consejo se pronunciará por unanimidad al adoptar recomendaciones:",
  ["En los ámbitos en los que se requiere la unanimidad para la adopción de un acto de la Unión.", "En todos los casos.", "Solo cuando la recomendación vaya dirigida a un Estado miembro.", "Nunca: siempre decide por mayoría cualificada."],
  "Art. 292 TFUE.", "Se pronunciará por unanimidad en los ámbitos en los que se requiere la unanimidad para la adopción de un acto de la Unión.")
Q("TFUE", "Artículo 292", "Derecho derivado", "Según el artículo 292 del TFUE, además del Consejo y de la Comisión, adoptará recomendaciones en los casos específicos previstos por los Tratados:",
  ["El Banco Central Europeo.", "El Tribunal de Cuentas.", "El Comité de las Regiones.", "El Defensor del Pueblo Europeo."],
  "Art. 292 TFUE.", "La Comisión, así como el Banco Central Europeo en los casos específicos previstos por los Tratados, adoptarán recomendaciones.")
Q("TUE", "Artículo 6", "Derecho originario", "Según el artículo 6.1 del TUE, la Carta de los Derechos Fundamentales de la Unión Europea tendrá:",
  ["El mismo valor jurídico que los Tratados.", "Un valor jurídico inferior a los Tratados y superior a los reglamentos.", "Valor de recomendación.", "El valor de un reglamento."],
  "Art. 6.1 TUE.", "la cual tendrá el mismo valor jurídico que los Tratados")
Q("TUE", "Artículo 6", "Derecho originario", "Según el artículo 6.1 del TUE, las disposiciones de la Carta:",
  ["No ampliarán en modo alguno las competencias de la Unión tal como se definen en los Tratados.", "Ampliarán las competencias de la Unión en materia de derechos fundamentales.", "Prevalecerán sobre los Tratados.", "Solo vincularán a los Estados que las ratifiquen."],
  "Art. 6.1, párrafo segundo, TUE.", "Las disposiciones de la Carta no ampliarán en modo alguno las competencias de la Unión tal como se definen en los Tratados.")
Q("TUE", "Artículo 6", "Derecho originario", "Según el artículo 6.2 del TUE, la adhesión de la Unión al Convenio Europeo para la Protección de los Derechos Humanos y de las Libertades Fundamentales:",
  ["No modificará las competencias de la Unión que se definen en los Tratados.", "Ampliará las competencias de la Unión.", "Requerirá la reforma previa de las constituciones nacionales.", "Sustituirá a la Carta de los Derechos Fundamentales."],
  "Art. 6.2 TUE.", "Esta adhesión no modificará las competencias de la Unión que se definen en los Tratados.")
Q("TUE", "Artículo 6", "Otras fuentes", "Según el artículo 6.3 del TUE, los derechos fundamentales que garantiza el Convenio Europeo y los que son fruto de las tradiciones constitucionales comunes a los Estados miembros formarán parte del Derecho de la Unión como:",
  ["Principios generales.", "Derecho derivado.", "Actos atípicos.", "Recomendaciones."],
  "Art. 6.3 TUE.", "formarán parte del Derecho de la Unión como principios generales")
Q("TUE", "Artículo 51", "Derecho originario", "Según el artículo 51 del TUE, los Protocolos y Anexos de los Tratados:",
  ["Forman parte integrante de los mismos.", "Son Derecho derivado.", "Tienen valor de declaración política.", "Prevalecen sobre los Tratados."],
  "Art. 51 TUE.", "Los Protocolos y Anexos de los Tratados forman parte integrante de los mismos.")
Q("CDFUE", "Artículo 51", "Derecho originario", "Según el artículo 51.1 de la Carta de los Derechos Fundamentales de la Unión Europea, sus disposiciones están dirigidas a los Estados miembros:",
  ["Únicamente cuando apliquen el Derecho de la Unión.", "En todo caso.", "Únicamente cuando lo autorice su Tribunal Constitucional.", "Solo en materia de política exterior."],
  "Art. 51.1 de la Carta.", "así como a los Estados miembros únicamente cuando apliquen el Derecho de la Unión")
Q("CDFUE", "Artículo 52", "Derecho originario", "Según el artículo 52.1 de la Carta, cualquier limitación del ejercicio de los derechos y libertades reconocidos por ella deberá:",
  ["Ser establecida por la ley y respetar el contenido esencial de dichos derechos y libertades.", "Ser aprobada por unanimidad del Consejo.", "Ser autorizada por el Tribunal de Justicia.", "Establecerse mediante recomendación de la Comisión."],
  "Art. 52.1 de la Carta.", "deberá ser establecida por la ley y respetar el contenido esencial de dichos derechos y libertades")
Q("TFUE", "Artículo 216", "Otras fuentes", "Según el artículo 216.2 del TFUE, los acuerdos celebrados por la Unión vincularán:",
  ["A las instituciones de la Unión y a los Estados miembros.", "Solo a las instituciones de la Unión.", "Solo a los Estados miembros que los ratifiquen.", "Solo a la Comisión, que los negocia."],
  "Art. 216.2 TFUE.", "Los acuerdos celebrados por la Unión vincularán a las instituciones de la Unión y a los Estados miembros.")
Q("TFUE", "Artículo 267", "Cuestión prejudicial", "Según el artículo 267 del TFUE, el Tribunal de Justicia será competente para pronunciarse, con carácter prejudicial, sobre los Tratados en cuanto a su:",
  ["Interpretación.", "Validez.", "Validez e interpretación.", "Aplicación a un asunto concreto."],
  "Art. 267 a) TFUE: interpretación de los Tratados; la validez solo de los actos de las instituciones (letra b).", "a) sobre la interpretación de los Tratados;")
Q("TFUE", "Artículo 267", "Cuestión prejudicial", "Según el artículo 267 del TFUE, cuando se plantee una cuestión prejudicial en un asunto pendiente ante un órgano jurisdiccional nacional cuyas decisiones no sean susceptibles de ulterior recurso judicial de Derecho interno, dicho órgano:",
  ["Estará obligado a someter la cuestión al Tribunal.", "Podrá pedir al Tribunal que se pronuncie, si lo estima necesario.", "Deberá resolver la cuestión por sí mismo.", "Deberá remitirla al Tribunal Constitucional."],
  "Art. 267, párrafo tercero, TFUE.", "dicho órgano estará obligado a someter la cuestión al Tribunal")
Q("TFUE", "Artículo 267", "Cuestión prejudicial", "Según el artículo 267 del TFUE, cuando la cuestión prejudicial se plantee en un asunto pendiente en relación con una persona privada de libertad, el Tribunal de Justicia se pronunciará:",
  ["Con la mayor brevedad.", "En el plazo de dos meses.", "En el plazo de quince días.", "Por el procedimiento ordinario, sin especialidad."],
  "Art. 267, último párrafo, TFUE.", "el Tribunal de Justicia de la Unión Europea se pronunciará con la mayor brevedad")
Q("LOPJ", "acuaobis", "Cuestión prejudicial", "Según el artículo 4 bis de la Ley Orgánica del Poder Judicial, cuando los Tribunales decidan plantear una cuestión prejudicial europea lo harán:",
  ["Mediante auto, previa audiencia de las partes.", "Mediante providencia, sin audiencia de las partes.", "Mediante sentencia, previa audiencia del Ministerio Fiscal.", "Mediante auto, sin audiencia de las partes."],
  "Art. 4 bis.2 LOPJ.", "en todo caso, mediante auto, previa audiencia de las partes")
Q("LOPJ", "acuaobis", "Relaciones con los Estados", "Según el artículo 4 bis.1 de la Ley Orgánica del Poder Judicial, los Jueces y Tribunales aplicarán el Derecho de la Unión Europea de conformidad con:",
  ["La jurisprudencia del Tribunal de Justicia de la Unión Europea.", "La jurisprudencia del Tribunal Supremo.", "La doctrina del Consejo de Estado.", "Las instrucciones de la Comisión Europea."],
  "Art. 4 bis.1 LOPJ.", "Los Jueces y Tribunales aplicarán el Derecho de la Unión Europea de conformidad con la jurisprudencia del Tribunal de Justicia de la Unión Europea.")
Q("CE", "Artículo 93", "Relaciones con los Estados", "Según el artículo 93 de la Constitución, la celebración de tratados por los que se atribuya a una organización o institución internacional el ejercicio de competencias derivadas de la Constitución se podrá autorizar mediante:",
  ["Ley orgánica.", "Ley ordinaria.", "Real decreto acordado en Consejo de Ministros.", "Acuerdo de las Cortes por mayoría de tres quintos."],
  "Art. 93 CE.", "Mediante ley orgánica se podrá autorizar la celebración de tratados")
Q("CE", "Artículo 93", "Relaciones con los Estados", "Según el artículo 93 de la Constitución, la garantía del cumplimiento de los tratados de atribución de competencias y de las resoluciones emanadas de los organismos titulares de la cesión corresponde:",
  ["A las Cortes Generales o al Gobierno, según los casos.", "Exclusivamente al Tribunal Constitucional.", "Al Consejo de Estado.", "A las Comunidades Autónomas."],
  "Art. 93 CE.", "Corresponde a las Cortes Generales o al Gobierno, según los casos, la garantía del cumplimiento de estos tratados")
Q("CE", "Artículo 94", "Relaciones con los Estados", "Según el artículo 94.1 de la Constitución, requiere la previa autorización de las Cortes Generales la prestación del consentimiento para obligarse por tratados:",
  ["Que impliquen obligaciones financieras para la Hacienda Pública.", "De carácter técnico sin repercusión legislativa.", "De cooperación cultural.", "Que solo requieran medidas reglamentarias para su ejecución."],
  "Art. 94.1 d) CE.", "d) Tratados o convenios que impliquen obligaciones financieras para la Hacienda Pública.")
Q("CE", "Artículo 95", "Relaciones con los Estados", "Según el artículo 95 de la Constitución, la celebración de un tratado internacional que contenga estipulaciones contrarias a la Constitución exigirá:",
  ["La previa revisión constitucional.", "Su aprobación por ley orgánica.", "La autorización del Senado por mayoría absoluta.", "Un referéndum consultivo."],
  "Art. 95.1 CE.", "exigirá la previa revisión constitucional")
Q("CE", "Artículo 95", "Relaciones con los Estados", "Según el artículo 95.2 de la Constitución, pueden requerir al Tribunal Constitucional para que declare si existe o no contradicción entre un tratado y la Constitución:",
  ["El Gobierno o cualquiera de las Cámaras.", "Cincuenta Diputados o cincuenta Senadores.", "El Defensor del Pueblo.", "Cualquier órgano jurisdiccional."],
  "Art. 95.2 CE.", "El Gobierno o cualquiera de las Cámaras puede requerir al Tribunal Constitucional")
Q("CE", "Artículo 96", "Relaciones con los Estados", "Según el artículo 96.1 de la Constitución, los tratados internacionales válidamente celebrados formarán parte del ordenamiento interno:",
  ["Una vez publicados oficialmente en España.", "Desde su firma.", "Desde su ratificación por el Rey.", "Una vez aprobados por ley orgánica."],
  "Art. 96.1 CE.", "una vez publicados oficialmente en España, formarán parte del ordenamiento interno")
Q("CE", "Artículo 96", "Relaciones con los Estados", "Según el artículo 96.2 de la Constitución, para la denuncia de los tratados y convenios internacionales se utilizará:",
  ["El mismo procedimiento previsto para su aprobación en el artículo 94.", "Una ley orgánica en todo caso.", "Un acuerdo del Consejo de Ministros, sin intervención de las Cortes.", "El procedimiento de reforma constitucional."],
  "Art. 96.2 CE.", "se utilizará el mismo procedimiento previsto para su aprobación en el artículo 94")
Q("DECL17", T_, "Relaciones con los Estados", "Según la Declaración n.º 17 aneja al Acta Final del Tratado de Lisboa, la primera sentencia de la jurisprudencia constante sobre la primacía es:",
  ["Costa/ENEL, de 15 de julio de 1964 (asunto 6/64).", "Van Gend & Loos, de 5 de febrero de 1963 (asunto 26/62).", "Simmenthal, de 9 de marzo de 1978 (asunto 106/77).", "Francovich, de 19 de noviembre de 1991."],
  "Declaración n.º 17 (dictamen del Servicio Jurídico del Consejo de 22-6-2007).", "En el momento de la primera sentencia de esta jurisprudencia constante (Costa/ENEL, 15 de julio de 1964, asunto 6/64")
Q("DECL17", T_, "Relaciones con los Estados", "Según la Declaración n.º 17 aneja al Acta Final del Tratado de Lisboa, los Tratados y el Derecho adoptado por la Unión sobre la base de los mismos priman sobre el Derecho de los Estados miembros:",
  ["En las condiciones establecidas por la jurisprudencia del Tribunal de Justicia.", "En las condiciones establecidas por cada constitución nacional.", "Solo en materia de competencia exclusiva de la Unión.", "Solo si así lo declara el Consejo Europeo."],
  "Declaración n.º 17.", "priman sobre el Derecho de los Estados miembros, en las condiciones establecidas por la citada jurisprudencia")
Q("STJ_SIMMENTHAL", T_, "Relaciones con los Estados", "Según el fallo de la sentencia Simmenthal (1978), el juez nacional que aplique el Derecho comunitario, ante disposiciones contrarias de la legislación nacional, aunque sean posteriores:",
  ["Las dejará inaplicadas por su propia iniciativa, sin esperar su derogación previa.", "Deberá esperar a que el legislador las derogue.", "Deberá plantear en todo caso cuestión de inconstitucionalidad.", "Las declarará nulas con efectos generales."],
  "Fallo de la sentencia Simmenthal (EUR-Lex).", "dejando, si procede, inaplicadas, por su propia iniciativa, cualesquiera disposiciones contrarias de la legislación nacional, aunque sean posteriores")
Q("STJ_VANGEND", T_, "Relaciones con los Estados", "Según el fallo de la sentencia Van Gend & Loos (1963), el artículo 12 del Tratado constitutivo de la Comunidad Económica Europea:",
  ["Produce efectos directos y genera en favor de los justiciables derechos individuales que los órganos jurisdiccionales nacionales deben proteger.", "Solo genera obligaciones para los Estados, sin derechos para los particulares.", "Solo puede invocarse mediante el recurso por incumplimiento de la Comisión.", "Necesita una ley nacional para producir efectos."],
  "Fallo 1) de Van Gend & Loos (EUR-Lex).", "produce efectos directos y genera en favor de los justiciables derechos individuales que los órganos jurisdiccionales nacionales deben proteger")
Q("STJ_FRANCOVICH", T_, "Relaciones con los Estados", "Según el fallo de la sentencia Francovich (1991), un Estado miembro está obligado a reparar los daños que resultan para los particulares de:",
  ["La no adaptación del Derecho nacional a la Directiva 80/987/CEE.", "La aplicación de un reglamento comunitario.", "Las sentencias del Tribunal de Justicia.", "Los actos de la Comisión."],
  "Fallo 2) de Francovich (EUR-Lex).", "Un Estado miembro está obligado a reparar los daños que resultan para los particulares de la no adaptación del Derecho nacional a la Directiva 80/987/CEE.")

T.real("L", 24, "Derecho derivado"); T.real("L", 25, "Relaciones con los Estados"); T.real("P", 10, "Derecho originario"); T.real("P", 16, "Relaciones con los Estados")

# Flashcards
for q_, a_, cat in [
  ("Fuentes del Derecho de la UE (síntesis de EUR-Lex)", "Derecho primario, principios generales y Derecho derivado; aparte, los acuerdos internacionales; otras: jurisprudencia del TJUE y Derecho internacional.", "Derecho originario"),
  ("¿Qué valor tienen el TUE y el TFUE entre sí?", "El mismo valor jurídico (art. 1 TUE).", "Derecho originario"),
  ("Protocolos y anexos de los Tratados (art. 51 TUE)", "Forman parte integrante de los Tratados.", "Derecho originario"),
  ("Valor jurídico de la Carta de los Derechos Fundamentales (art. 6.1 TUE)", "El mismo que los Tratados; no amplía las competencias de la Unión.", "Derecho originario"),
  ("¿A quién se dirige la Carta? (art. 51.1)", "A las instituciones, órganos y organismos de la Unión y a los Estados miembros únicamente cuando apliquen el Derecho de la Unión.", "Derecho originario"),
  ("Los cinco actos del art. 288 TFUE", "Reglamentos, directivas, decisiones, recomendaciones y dictámenes.", "Derecho derivado"),
  ("Reglamento (art. 288)", "Alcance general; obligatorio en todos sus elementos; directamente aplicable en cada Estado miembro.", "Derecho derivado"),
  ("Directiva (art. 288)", "Obliga al Estado destinatario en cuanto al resultado; forma y medios, a elección de las autoridades nacionales.", "Derecho derivado"),
  ("Decisión (art. 288)", "Obligatoria en todos sus elementos; si designa destinatarios, solo para ellos.", "Derecho derivado"),
  ("Actos delegados (art. 290)", "Los adopta la Comisión por delegación de un acto legislativo; alcance general; completan o modifican elementos no esenciales; título «delegado/a».", "Actos delegados"),
  ("Revocación u objeción de un acto delegado: mayorías (art. 290.2)", "Parlamento: mayoría de los miembros que lo componen; Consejo: mayoría cualificada.", "Actos delegados"),
  ("Actos de ejecución (art. 291)", "Ejecutan los Estados; si hacen falta condiciones uniformes, la Comisión (o el Consejo en casos justificados y arts. 24 y 26 TUE); título «de ejecución».", "Actos de ejecución"),
  ("¿Quién adopta recomendaciones? (art. 292)", "El Consejo, la Comisión y el BCE (este, en los casos previstos).", "Derecho derivado"),
  ("Principios generales del Derecho de la Unión (art. 6.3 TUE)", "Los derechos del Convenio Europeo y los fruto de las tradiciones constitucionales comunes.", "Otras fuentes"),
  ("¿A quién vinculan los acuerdos de la Unión? (art. 216.2)", "A las instituciones de la Unión y a los Estados miembros.", "Otras fuentes"),
  ("Primacía: ¿dónde está y cuál fue la primera sentencia?", "Es jurisprudencial (no está en el articulado; la recuerda la Declaración n.º 17); primera sentencia: Costa/ENEL, 15-7-1964, asunto 6/64.", "Relaciones con los Estados"),
  ("Efecto directo: sentencia que lo estableció", "Van Gend & Loos (5-2-1963, asunto 26/62).", "Relaciones con los Estados"),
  ("Simmenthal (1978)", "El juez nacional deja inaplicadas, por su propia iniciativa, las normas nacionales contrarias, aunque sean posteriores.", "Relaciones con los Estados"),
  ("Francovich (1991)", "El Estado está obligado a reparar los daños causados a los particulares por no adaptar su Derecho a una directiva.", "Relaciones con los Estados"),
  ("Cuestión prejudicial obligatoria (art. 267)", "Para el órgano jurisdiccional cuyas decisiones no sean susceptibles de ulterior recurso judicial de Derecho interno.", "Cuestión prejudicial"),
  ("Forma de plantear la cuestión prejudicial en España (LOPJ, art. 4 bis)", "Mediante auto, previa audiencia de las partes.", "Cuestión prejudicial"),
  ("Art. 93 CE", "Ley orgánica para autorizar tratados que atribuyan el ejercicio de competencias derivadas de la Constitución; garantía de cumplimiento: Cortes o Gobierno.", "Relaciones con los Estados"),
  ("Primacía y supremacía (DTC 1/2004)", "Primacía: aplicación de normas válidas; supremacía: procedimientos de normación (validez). La CE acepta la primacía en virtud del art. 93.", "Relaciones con los Estados"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Derecho primario u originario", "Los Tratados (TUE y TFUE, con el mismo valor jurídico), sus protocolos y anexos (art. 51 TUE) y la Carta, con el mismo valor que los Tratados (art. 6.1 TUE).", "s2", "Derecho originario")
T.glos("Carta de los Derechos Fundamentales", "Carta de 7-12-2000, adaptada el 12-12-2007 en Estrasburgo; mismo valor jurídico que los Tratados; obliga a los Estados solo cuando aplican el Derecho de la Unión.", "s3", "Derecho originario")
T.glos("Derecho derivado", "Actos que adoptan las instituciones para ejercer las competencias de la Unión (art. 288 TFUE); según EUR-Lex, el corpus jurídico que se basa en los Tratados.", "s5", "Derecho derivado")
T.glos("Reglamento", "Acto de alcance general, obligatorio en todos sus elementos y directamente aplicable en cada Estado miembro (art. 288 TFUE).", "s5", "Derecho derivado")
T.glos("Directiva", "Acto que obliga al Estado destinatario en cuanto al resultado, dejando a las autoridades nacionales la forma y los medios (art. 288 TFUE).", "s5", "Derecho derivado")
T.glos("Decisión", "Acto obligatorio en todos sus elementos; si designa destinatarios, solo es obligatorio para ellos (art. 288 TFUE).", "s5", "Derecho derivado")
T.glos("Acto legislativo", "Acto jurídico adoptado mediante procedimiento legislativo, ordinario o especial (art. 289 TFUE).", "s6", "Derecho derivado")
T.glos("Acto delegado", "Acto no legislativo de alcance general de la Comisión que completa o modifica elementos no esenciales de un acto legislativo (art. 290 TFUE).", "s6", "Derecho derivado")
T.glos("Acto de ejecución", "Acto que establece condiciones uniformes de ejecución de los actos vinculantes de la Unión; lo adopta la Comisión o, en casos previstos, el Consejo (art. 291 TFUE).", "s6", "Derecho derivado")
T.glos("Principios generales", "Fuente del Derecho de la Unión; incluyen los derechos del Convenio Europeo y los de las tradiciones constitucionales comunes (art. 6.3 TUE).", "s8", "Otras fuentes")
T.glos("Actos atípicos", "Según EUR-Lex, actos de las instituciones que no forman parte de la nomenclatura del art. 288 TFUE (reglamentos internos, acuerdos interinstitucionales, comunicaciones…).", "s10", "Otras fuentes")
T.glos("Primacía", "Principio jurisprudencial (Costa/ENEL, 1964) por el que el Derecho de la Unión prima sobre el de los Estados miembros; recordado en la Declaración n.º 17 de Lisboa.", "s11", "Relaciones con los Estados")
T.glos("Efecto directo", "Principio establecido en Van Gend & Loos (1963): normas de la Unión que generan derechos que los particulares pueden invocar ante los jueces nacionales.", "s12", "Relaciones con los Estados")
T.glos("Cuestión prejudicial", "Consulta de un órgano jurisdiccional nacional al TJUE sobre la interpretación de los Tratados o la validez e interpretación de los actos de la Unión (art. 267 TFUE).", "s13", "Cuestión prejudicial")

# Cronología (fechas de las propias sentencias en EUR-Lex y de los metadatos del BOE y del DOUE)
T.hito("1963", "Sentencia Van Gend & Loos, de 5 de febrero de 1963 (asunto 26/62)", "Efecto directo: el art. 12 del Tratado CEE «produce efectos directos»", "jurisprudencial", "s12")
T.hito("1964", "Sentencia Costa/ENEL, de 15 de julio de 1964 (asunto 6/64)", "Primera sentencia sobre la primacía, según la Declaración n.º 17", "jurisprudencial", "s11")
T.hito("1978", "Sentencia Simmenthal, de 9 de marzo de 1978 (asunto 106/77)", "Inaplicación de la norma nacional contraria, aunque sea posterior", "jurisprudencial", "s11")
T.hito("1978", "Constitución Española (27-12-1978; BOE de 29-12-1978)", "Arts. 93 a 96: tratados internacionales y atribución del ejercicio de competencias", "normativo", "s14")
T.hito("1991", "Sentencia Francovich, de 19 de noviembre de 1991 (asuntos C-6/90 y C-9/90)", "Obligación del Estado de reparar los daños por no adaptar su Derecho a una directiva", "jurisprudencial", "s12")
T.hito("2004", "Declaración del Tribunal Constitucional 1/2004, de 13 de diciembre (BOE de 4-1-2005)", "Primacía y supremacía; suficiencia del art. 93 CE", "jurisprudencial", "s14")
T.hito("2008", "Ley Orgánica 1/2008, de 30 de julio (BOE de 31-7-2008), que autoriza la ratificación del Tratado de Lisboa (firmado el 13-12-2007)", "Art. 93 CE: autorización por ley orgánica", "normativo", "s14")
T.hito("2015", "Ley Orgánica 7/2015, de 21 de julio (BOE de 22-7-2015), que modifica la LOPJ", "Añade el art. 4 bis: aplicación del Derecho de la Unión y cuestión prejudicial mediante auto", "normativo", "s13")

T.publicar()
