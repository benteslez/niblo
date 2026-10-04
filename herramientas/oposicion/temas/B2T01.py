# -*- coding: utf-8 -*-
"""Tema II.1 (B2T01): La Unión Europea: Antecedentes. Objetivos y naturaleza jurídica. Los
Tratados originarios y modificativos. El Tratado de la Unión Europea y el Tratado de
Funcionamiento de la Unión Europea. El proceso de ampliación. Las cooperaciones reforzadas.
Método del I.2. Normas: TUE (preámbulo y arts. 1 a 8, 20, 47 a 51 y 53) y TFUE (arts. 1 y
326 a 334), versión consolidada de EUR-Lex (DOUE C 202 de 7-6-2016); Ley Orgánica 1/2008
(BOE). Lo que no es norma (antecedentes, tratados históricos, ampliaciones) sale literal de
fuentes oficiales: fichas temáticas del Parlamento Europeo (PE) y portal de la Unión Europea
(Comisión Europea), marcadas como «fuente oficial, no es texto legal».
Si se define WEB_B2T01 (carpeta con las páginas descargadas en .txt), se comprueba además que
cada frase de esas fuentes es literal."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *
import plantilla as P

CORTO["TUEPRE"] = "TUE"
CORTO["LO1_2008"] = "LO 1/2008"
ESQ = "*Esquema de elaboración propia: resume los artículos y las fuentes citados; no es texto legal.*"


# --- Textos legales -------------------------------------------------------------
def LT(n, resaltar=(), solo=None):
    a = f"Artículo {n}"
    return lit("TUE", a, resaltar, solo, titulo=f"{a} TUE" + (" (fragmento)" if solo else ""))
def LF(n, resaltar=(), solo=None):
    a = f"Artículo {n}"
    return lit("TFUE", a, resaltar, solo, titulo=f"{a} TFUE" + (" (fragmento)" if solo else ""))
def cT(n, frag): return c("TUE", f"Artículo {n}", frag)
def cF(n, frag): return c("TFUE", f"Artículo {n}", frag)


# --- Fuentes oficiales que no son norma (literal; se comprueban si hay WEB_B2T01) ---
PE1 = "https://www.europarl.europa.eu/factsheets/es/sheet/1/los-primeros-tratados"
PE2 = "https://www.europarl.europa.eu/factsheets/es/sheet/2/la-evolucion-hacia-el-acta-unica-europea"
PE3 = "https://www.europarl.europa.eu/factsheets/es/sheet/3/los-tratados-de-maastricht-y-amsterdam"
PE4 = "https://www.europarl.europa.eu/factsheets/es/sheet/4/el-tratado-de-niza-y-la-convencion-sobre-el-futuro-de-europa"
PE5 = "https://www.europarl.europa.eu/factsheets/es/sheet/5/el-tratado-de-lisboa"
PE167 = "https://www.europarl.europa.eu/factsheets/es/sheet/167/la-ampliacion-de-la-union"
DIA = "https://european-union.europa.eu/principles-countries-history/europe-day_es"
TUEX = "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:12016M/TXT"
TFUEX = "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:12016E/TXT"
ARCH = {PE1: "pe1", PE2: "pe2", PE3: "pe3", PE4: "pe4", PE5: "pe5", PE167: "s167", DIA: "dia", TUEX: "tue2", TFUEX: "tfue"}
NOMBRE = {PE1: "Parlamento Europeo, ficha temática 1.1.1 «Los primeros Tratados»",
          PE2: "Parlamento Europeo, ficha temática 1.1.2 «La evolución hacia el Acta Única Europea»",
          PE3: "Parlamento Europeo, ficha temática 1.1.3 «Los Tratados de Maastricht y Ámsterdam»",
          PE4: "Parlamento Europeo, ficha temática 1.1.4 «El Tratado de Niza y la Convención sobre el futuro de Europa»",
          PE5: "Parlamento Europeo, ficha temática 1.1.5 «El Tratado de Lisboa»",
          PE167: "Parlamento Europeo, ficha temática 5.5.1 «La ampliación de la Unión»",
          DIA: "Portal de la Unión Europea, «Día de Europa: 9 de mayo»"}
_WEB = os.environ.get("WEB_B2T01")
_TXT = {}
def _wchk(url, frag):
    if not _WEB: return
    if url not in _TXT: _TXT[url] = P._norm(open(os.path.join(_WEB, ARCH[url] + ".txt"), encoding="utf-8").read())
    for parte in frag.split("…"):
        p = P._norm(parte.replace("**", ""))
        if p: assert p in _TXT[url], ("FUENTE NO LITERAL", url, p)
def web(cod, url, *ps, que=None):
    """Bloque literal de una fuente oficial que no es norma: etiqueta, línea en negrita y párrafos."""
    for p in ps: _wchk(url, p)
    return "\n".join([f"> [[{cod}|{url}]]", f"> **{que or NOMBRE[url]} · fuente oficial, no es texto legal**"] + ["> " + p for p in ps])
def cw(url, frag):
    _wchk(url, frag); return "«" + frag + "»"


def examen_web(cod, n, porque, apoyo):
    """Como examen(), pero la pregunta no es de texto legal: la respuesta de la plantilla se
    contrasta con una fuente oficial (apoyo: [(dato en la opción correcta, url, fragmento)])."""
    q = P._qs(cod)[n]; assert not q["anulada"], (cod, n)
    ok = "abcd"[q["c"]]; P.PORQUE[(cod, n)] = dict(porque)
    assert sorted(porque) == list("abcd") and apoyo, (cod, n)
    for dato, url, frag in apoyo:
        _wchk(url, frag)
        assert P._norm(dato) in P._norm(frag), ("DATO FUERA DEL FRAGMENTO", cod, n, dato)
        assert P._norm(dato) in P._norm(q["o"][ok]), ("LA PLANTILLA NO CASA CON LA FUENTE", cod, n, ok, dato)
    for x in "abcd":
        if x != ok: assert not all(P._norm(d) in P._norm(q["o"][x]) for d, *_ in apoyo), ("DISTRACTOR IGUAL DE APOYADO", cod, n, x)
    lin = [f"**📋 Pregunta real · {P.EXAMENES[cod][1]} · n.º {n}**", "«" + q["q"] + "»"]
    lin += [f"[{'x' if x == ok else ' '}] {x}) {q['o'][x]} || {porque[x]}" for x in "abcd"]
    lin.append(f"= **Respuesta correcta: {ok})**, según la plantilla definitiva, y coherente con la fuente oficial citada (no es texto legal).")
    return "\n".join("%> " + l for l in lin)


# Cuadros (fuera de los f-strings)
TAB1 = "| Rasgo | Dónde se dice |\n|---|---|\n| Se crea **por Tratado** entre Estados (" + cT(1, "constituyen entre sí una UNIÓN EUROPEA") + ") | TUE, art. 1 |\n| Tiene **competencias atribuidas** por los Estados; lo no atribuido es de los Estados | TUE, arts. 1, 4.1 y 5.2 |\n| Se fundamenta en **dos Tratados con el mismo valor jurídico** | TUE, art. 1; TFUE, art. 1.2 |\n| **Sustituye y sucede** a la Comunidad Europea | TUE, art. 1 |\n| Tiene **personalidad jurídica** | TUE, art. 47 |\n| Se basa en **valores** comunes a los Estados miembros | TUE, art. 2 |"
TAB2 = "| Tratado | Firma | Entrada en vigor | Lo esencial |\n|---|---|---|---|\n| París (CECA) | 18-4-1951 | 23-7-1952 | Carbón y acero; 50 años (expiró el 23-7-2002) |\n| Roma (CEE y Euratom) | 25-3-1957 | 1-1-1958 | Mercado común y energía atómica; duración indefinida |\n| Fusión | 8-4-1965 | 1967 | Consejo único y Comisión única |\n| Acta Única Europea | 17 y 28-2-1986 | 1-7-1987 | Mercado interior (1-1-1993); primera modificación sustancial |\n| Maastricht (TUE) | 7-2-1992 | 1-11-1993 | Nace la Unión Europea; tres pilares |\n| Ámsterdam | 2-10-1997 | 1-5-1999 | Cooperación reforzada; renumeración |\n| Niza | 26-2-2001 | 1-2-2003 | Reforma institucional ante la ampliación; Carta proclamada |\n| Constitución para Europa | — | No entró en vigor | Rechazada en Francia y Países Bajos (2005) |\n| Lisboa | 13-12-2007 | 1-12-2009 | TUE y TFUE actuales |\n\nFuente de las fechas: fichas temáticas 1.1.1 a 1.1.5 del Parlamento Europeo (citadas arriba)."
TAB3 = "| Año | Estados | Particularidad (ficha 5.5.1 del Parlamento Europeo) |\n|---|---|---|\n| 1958 | Bélgica, Francia, Alemania, Italia, Luxemburgo, Países Bajos | Signatarios originales del Tratado de Roma de 1957 |\n| 1973 | Dinamarca, Irlanda, Reino Unido | Groenlandia, como parte de Dinamarca, se adhirió en 1973 y se retiró en 1985 |\n| 1981 | Grecia | Consolidó la democracia en el país |\n| 1986 | Portugal, España | Consolidó la democracia en España y Portugal |\n| 1995 | Austria, Finlandia, Suecia | Antes, miembros de la AELC; Noruega rechazó la adhesión en referéndum |\n| 2004 | Chipre, Chequia, Estonia, Hungría, Letonia, Lituania, Malta, Polonia, Eslovaquia, Eslovenia | Reunificar el continente tras la caída del muro de Berlín |\n| 2007 | Bulgaria, Rumanía | Mecanismo de cooperación y verificación |\n| 2013 | Croacia | Condiciones más estrictas del «consenso renovado sobre la ampliación» (2006) |"
TAB4 = "| | Régimen general (329.1 y 331.1) | PESC (329.2 y 331.2) |\n|---|---|---|\n| Solicitud | A la **Comisión** | Al **Consejo** |\n| Propuesta o dictámenes | Propuesta de la **Comisión** | Dictámenes del **Alto Representante** y de la **Comisión** |\n| Parlamento Europeo | **Aprobación** | Solo **información** |\n| Autoriza | **Consejo** | **Consejo**, por **unanimidad** |\n| Incorporación posterior | Confirma la **Comisión** (4 meses) | Confirma el **Consejo** (unanimidad) |\n| Mínimo de Estados (art. 20.2 TUE) | **Nueve** | **Nueve** |"

T = Tema("B2T01",
  "Seis preguntas: I. De dónde viene la Unión: antecedentes (fuentes oficiales del Parlamento Europeo y de la Unión) · II. Qué es la Unión y qué persigue: naturaleza jurídica, valores y objetivos (TUE, preámbulo y arts. 1 a 8 y 47) · III. Con qué Tratados: originarios, modificativos y su revisión (fichas del Parlamento Europeo; LO 1/2008; TUE, art. 48) · IV. Qué son el TUE y el TFUE (TUE, arts. 1, 51 y 53; TFUE, art. 1) · V. Cómo se entra y cómo se sale: ampliación y retirada (TUE, arts. 49 y 50) · VI. Cómo avanzan solo algunos: cooperaciones reforzadas (TUE, art. 20; TFUE, arts. 326 a 334). Cada artículo: texto literal (DOUE o BOE) y ficha.",
  ["Declaración Schuman", "9 de mayo", "CECA", "Tratados de Roma", "Tratado de Fusión", "Acta Única", "Maastricht", "Ámsterdam", "Niza", "Lisboa", "Valores (art. 2)", "Objetivos (art. 3)", "Atribución", "Subsidiariedad", "Proporcionalidad", "Cooperación leal", "Art. 7 TUE", "Personalidad jurídica", "Revisión de los Tratados", "TUE y TFUE", "Adhesión (art. 49)", "Criterios de Copenhague", "Retirada (art. 50)", "Cooperaciones reforzadas", "Nueve Estados"])

# =============================================================================
T.ap("s0", "Mapa del tema: seis preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque II, tema 1):
> La Unión Europea: Antecedentes. Objetivos y naturaleza jurídica. Los Tratados originarios y modificativos. El Tratado de la Unión Europea y el Tratado de Funcionamiento de la Unión Europea. El proceso de ampliación. Las cooperaciones reforzadas.

### El hilo conductor

El epígrafe se lee como **seis preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Tratados (EUR-Lex) | Otras fuentes |
|---|---|---|---|
| **I** | ¿De dónde viene la Unión? (antecedentes) | — | Fichas del Parlamento Europeo 1.1.1; portal de la Unión (Día de Europa) |
| **II** | ¿Qué es la Unión y qué persigue? (naturaleza jurídica y objetivos) | TUE: preámbulo y arts. 1 a 8 y 47 | — |
| **III** | ¿Con qué Tratados? (originarios y modificativos) | TUE, art. 48 | Fichas del Parlamento Europeo 1.1.1 a 1.1.5; LO 1/2008, art. 1 |
| **IV** | ¿Qué son el TUE y el TFUE? | TUE, arts. 1, 51 y 53; TFUE, art. 1 | Índices de las versiones consolidadas (DOUE) |
| **V** | ¿Cómo se entra y cómo se sale? (ampliación y retirada) | TUE, arts. 49 y 50 | Ficha del Parlamento Europeo 5.5.1 |
| **VI** | ¿Cómo avanzan solo algunos Estados? (cooperaciones reforzadas) | TUE, art. 20; TFUE, arts. 326 a 334 | Fichas del Parlamento Europeo 1.1.3 y 1.1.4 |

!> **La idea que une los seis bloques:** tras la guerra, seis Estados ponen en común el carbón y el acero (I). De ahí nacen unas Comunidades que los **Tratados** van ampliando y reformando (III) hasta una **Unión** fundada en el TUE y el TFUE, con **valores**, **objetivos** y **competencias atribuidas** por los Estados (II y IV). La Unión puede **crecer** (adhesión) o **perder** miembros (retirada) (V), y dentro de ella unos Estados pueden **ir más deprisa** mediante cooperaciones reforzadas (VI).

### Cómo está escrito

- Cada artículo: primero el **texto literal** del Tratado (versión consolidada de EUR-Lex, etiqueta **DOUE**) o de la ley española (etiqueta **BOE**) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Lo que **no es norma** (historia, fechas de los Tratados, ampliaciones) se copia **literal** de fuentes oficiales —fichas temáticas del **Parlamento Europeo** y portal de la **Unión Europea**— con su etiqueta y la advertencia «fuente oficial, no es texto legal».
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos y las fuentes citados.
- Lo que el epígrafe comparte con otros temas se remite allí: instituciones (tema II.2 y tema II.3), Carta de Derechos Fundamentales y fuentes del Derecho (tema II.4), políticas (tema II.6).
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿De dónde viene la Unión? Antecedentes", donde(
  "Primera pregunta del tema. Antes de leer los Tratados vigentes, hay que saber **por qué** y **cómo** empezó la integración europea: la reconciliación franco-alemana y la puesta en común del carbón y del acero. Este bloque no es texto legal: todo sale literal de fuentes oficiales de la Unión.",
  ["1 El punto de partida: la Declaración Schuman y el Día de Europa", "2 Del fracaso de la CED a la Conferencia de Mesina"]))

T.ap("s1", "I.1 El punto de partida: la Declaración Schuman (9 de mayo de 1950)", f"""
{unidad("1.1 La Declaración Schuman y el contexto de posguerra",
  web("PE", PE1,
      "Los efectos desastrosos de la Segunda Guerra Mundial y la amenaza constante del enfrentamiento Este-Oeste hicieron de la reconciliación franco-alemana una prioridad fundamental. La decisión de poner en común la industria del carbón y del acero entre seis países europeos (Bélgica, Francia, Alemania, Italia, Luxemburgo y Países Bajos) llevada a la práctica mediante el Tratado de París en 1951, representó el primer paso hacia la integración europea.",
      "El llamamiento que lanzó el **9 de mayo de 1950** el ministro francés de Asuntos Exteriores, **Robert Schuman**, puede considerarse el punto de partida de la Europa comunitaria. La elección del carbón y del acero era, en esa época, altamente simbólica. En efecto, a principios de los años 1950, el carbón y la siderurgia eran industrias fundamentales, base de la potencia de un país. Además del evidente interés económico, la puesta en común de los recursos franceses y alemanes complementarios debía señalar el final del antagonismo entre estos dos países."),
  fichab("Llamamiento que inicia la Europa comunitaria",
         f"{cw(PE1, 'el ministro francés de Asuntos Exteriores, Robert Schuman')}; seis países: Bélgica, Francia, Alemania, Italia, Luxemburgo y Países Bajos",
         f"Puesta en común del **carbón y del acero**, llevada a la práctica por el **Tratado de París** (→ III.1.1)",
         f"{cw(PE1, 'el 9 de mayo de 1950')}; Tratado de París en 1951",
         "El punto de partida es la **Declaración Schuman** (1950), no los Tratados de Roma (1957). La clave política: la **reconciliación franco-alemana**."))}

{unidad("1.2 El Día de Europa (9 de mayo)",
  web("COMISION", DIA,
      "El 9 de mayo de 1950, el ministro francés de Asuntos Exteriores, Robert Schuman, pronunció un discurso histórico y expuso un plan para una mayor cooperación en Europa. Conocida como la **Declaración Schuman**, allanó el camino para una nueva era de paz, integración y cooperación en todo el continente, y sentó las bases de la Unión Europea tal como la conocemos hoy."),
  fichab("Día de Europa: 9 de mayo",
         "La Unión Europea (lo celebran las instituciones y los Estados miembros)",
         f"Recuerda el discurso de Schuman, {cw(DIA, 'Conocida como la Declaración Schuman')}",
         "9 de mayo (de 1950, fecha de la Declaración)",
         "Cayó en 2025 (→ Cierre 1): el 9 de mayo **no** es la firma del Tratado de Roma (25 de marzo de 1957, → III.1.2) ni la primera ampliación (1973, → V.2.1)."))}
""", 2)

T.ap("s2", "I.2 Del fracaso de la CED a la Conferencia de Mesina", f"""
Tras la CECA (→ III.1.1) se intentó ir más allá en defensa y en política; el fracaso llevó a relanzar la integración por la vía **económica**.

{unidad("2.1 La Comunidad Europea de Defensa y la Conferencia de Mesina",
  web("PE", PE1,
      "Después de la firma del Tratado de París, y a pesar de que Francia se oponía a la reconstitución de una fuerza militar alemana, René Pleven propuso la formación de un ejército europeo. Esto dio lugar a la negociación de 1952 de la Comunidad Europea de Defensa (CED), que debía ir acompañada de una Comunidad Política Europea. Sin embargo, ambos proyectos fueron abandonados como consecuencia de la negativa de la **Asamblea Nacional francesa** a autorizar la ratificación del Tratado el **30 de agosto de 1954**.",
      "Los esfuerzos de reactivación de la construcción europea tras el fracaso de la CED se materializaron con las propuestas específicas en la **Conferencia de Mesina (junio de 1955)** de la unión aduanera y de la energía atómica. Las propuestas condujeron a la firma del Tratado CEE y del Tratado CEEA."),
  fichab("Intento fallido de integración militar y política, y relanzamiento económico",
         "René Pleven (propuesta de ejército europeo); la Asamblea Nacional francesa (rechazo)",
         ["CED (negociada en 1952), acompañada de una Comunidad Política Europea: **abandonadas**", "Mesina (junio de 1955): propuestas de **unión aduanera** y de **energía atómica** → Tratados CEE y CEEA (→ III.1.2)"],
         "Rechazo francés: 30 de agosto de 1954",
         "La CED **no llegó a nacer**: la Asamblea Nacional francesa no autorizó su ratificación. Mesina conduce a los **Tratados de Roma**."))}

{resumen([
  "Punto de partida: **Declaración Schuman**, **9 de mayo de 1950** (por eso el 9 de mayo es el **Día de Europa**).",
  "Idea: poner en común el **carbón y el acero** para la **reconciliación franco-alemana**; seis países.",
  "La **CED** fracasó (Asamblea Nacional francesa, 1954); la **Conferencia de Mesina** (1955) llevó a los Tratados **CEE** y **CEEA**."],
  "Siguiente: II. ¿Qué es la Unión y qué persigue? Naturaleza jurídica y objetivos")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Qué es la Unión y qué persigue? Naturaleza jurídica y objetivos (TUE, preámbulo y arts. 1 a 8 y 47)", donde(
  "Segunda pregunta. Ya sabemos de dónde viene; ahora, **qué es jurídicamente** la Unión (una organización creada por Tratado entre Estados, con personalidad jurídica y competencias atribuidas) y **para qué** existe (valores y objetivos).",
  ["1 La creación de la Unión: preámbulo, art. 1 y personalidad jurídica (art. 47)", "2 Valores y objetivos (arts. 2 y 3)", "3 Unión y Estados: atribución, subsidiariedad, proporcionalidad y cooperación leal (arts. 4 y 5)", "4 Derechos fundamentales, defensa de los valores y vecindad (arts. 6 a 8)"]))

T.ap("s3", "II.1 La creación de la Unión: preámbulo, art. 1 y personalidad jurídica (TUE, art. 47)", f"""
{unidad("1.1 El preámbulo del TUE (fragmento)",
  lit("TUEPRE", "Preámbulo", ["RESUELTOS a salvar una nueva etapa en el proceso de integración europea", "una unión cada vez más estrecha entre los pueblos de Europa", "de acuerdo con el principio de subsidiariedad", "HAN DECIDIDO crear una Unión Europea"], solo=[2, 3, 4, 14, 16], titulo="Preámbulo del TUE (fragmento)"),
  fichab("Declaración de intenciones de las Altas Partes Contratantes al crear la Unión",
         "Los Jefes de Estado de los Estados firmantes (Altas Partes Contratantes)",
         ["Continúa el proceso de integración " + c("TUEPRE", "Preámbulo", "emprendido con la constitución de las Comunidades Europeas"), "Se inspira en la herencia cultural, religiosa y humanista de Europa", "Persigue una unión cada vez más estrecha, con decisiones lo más próximas posible a los ciudadanos (subsidiariedad)"],
         "—",
         f"El preámbulo cierra con {c('TUEPRE', 'Preámbulo', 'HAN DECIDIDO crear una Unión Europea')}. La Unión **no** sustituye a los Estados: se crea **entre** ellos."))}

{unidad("1.2 Constitución de la Unión y fundamento en los dos Tratados (art. 1)",
  LT(1, ["constituyen entre sí una UNIÓN EUROPEA", "a la que los Estados miembros atribuyen competencias", "Ambos Tratados tienen el mismo valor jurídico", "La Unión sustituirá y sucederá a la Comunidad Europea"]),
  fichab("Acto de creación de la Unión y sus bases jurídicas",
         f"{cT(1, 'las ALTAS PARTES CONTRATANTES')}; los Estados miembros atribuyen las competencias",
         ["Por Tratado: los Estados constituyen entre sí la Unión", "La Unión se fundamenta en el **TUE** y el **TFUE** («los Tratados»)", "Sustituye y sucede a la **Comunidad Europea**"],
         f"{cT(1, 'Ambos Tratados tienen el mismo valor jurídico')}",
         "Naturaleza jurídica en tres datos del art. 1: creada **por Tratado** entre Estados, con competencias **atribuidas** por ellos, y **sucesora** de la Comunidad Europea. TUE y TFUE: **mismo valor jurídico** (no hay jerarquía)."))}

{unidad("1.3 Personalidad jurídica (art. 47)",
  LT(47, ["La Unión tiene personalidad jurídica"]),
  fichab("La Unión como sujeto de Derecho", "La Unión", "—", "—",
         "Lo dice el **TUE** (art. 47), en sus disposiciones finales. La personalidad jurídica es **de la Unión**, que sucedió a la Comunidad Europea (art. 1)."))}

{unidad("1.4 La naturaleza jurídica de la Unión (esquema)",
  ESQ,
  TAB1)}
""", 2)

T.ap("s4", "II.2 Valores y objetivos de la Unión (TUE, arts. 2 y 3)", f"""
{unidad("2.1 Los valores de la Unión (art. 2)",
  LT(2, ["respeto de la dignidad humana, libertad, democracia, igualdad, Estado de Derecho y respeto de los derechos humanos", "Estos valores son comunes a los Estados miembros"]),
  fichab("Valores en que se fundamenta la Unión",
         "La Unión y los Estados miembros (los valores son comunes)",
         ["::Valores:", "Dignidad humana", "Libertad", "Democracia", "Igualdad", "Estado de Derecho", "Respeto de los derechos humanos, incluidos los de las personas pertenecientes a minorías"],
         "—",
         "Son **seis** valores. Pluralismo, no discriminación, tolerancia, justicia, solidaridad e igualdad entre mujeres y hombres **caracterizan la sociedad**, no son la lista de valores. Su respeto es requisito de **adhesión** (art. 49, → V.1.1) y su violación activa el **art. 7** (→ II.4.2)."))}

{unidad("2.2 Los objetivos de la Unión (art. 3)",
  LT(3, ["promover la paz, sus valores y el bienestar de sus pueblos", "un espacio de libertad, seguridad y justicia sin fronteras interiores", "La Unión establecerá un mercado interior", "economía social de mercado altamente competitiva", "una unión económica y monetaria cuya moneda es el euro", "de acuerdo con las competencias que se le atribuyen en los Tratados"]),
  fichab("Finalidad y objetivos de la Unión",
         "La Unión",
         ["::Finalidad general (3.1): paz, valores y bienestar de sus pueblos. Objetivos:", "Espacio de libertad, seguridad y justicia sin fronteras interiores (3.2)", "Mercado interior y desarrollo sostenible; economía social de mercado; cohesión económica, social y territorial; diversidad cultural y lingüística (3.3)", "Unión económica y monetaria cuya moneda es el euro (3.4)", "Relaciones con el resto del mundo: valores, paz, comercio libre y justo, Derecho internacional (3.5)"],
         "—",
         f"Los objetivos **no amplían competencias**: {cT(3, 'La Unión perseguirá sus objetivos por los medios apropiados, de acuerdo con las competencias que se le atribuyen en los Tratados')} (3.6). Ojo al orden: el 3.2 (espacio de libertad, seguridad y justicia) va **antes** que el mercado interior (3.3)."))}
""", 2)

T.ap("s5", "II.3 Unión y Estados miembros: atribución, subsidiariedad, proporcionalidad y cooperación leal (TUE, arts. 4 y 5)", f"""
{unidad("3.1 Competencias de los Estados, identidad nacional y cooperación leal (art. 4)",
  LT(4, ["toda competencia no atribuida a la Unión en los Tratados corresponde a los Estados miembros", "su identidad nacional", "la seguridad nacional seguirá siendo responsabilidad exclusiva de cada Estado miembro", "principio de cooperación leal"]),
  fichab("Relaciones entre la Unión y los Estados miembros",
         "La Unión y los Estados miembros",
         ["Lo no atribuido es de los **Estados** (4.1)", "La Unión respeta la **igualdad** de los Estados, su **identidad nacional** (también autonomía local y regional) y sus funciones esenciales (4.2)", "**Cooperación leal**: respeto y asistencia mutuos; los Estados aseguran el cumplimiento y se abstienen de poner en peligro los objetivos (4.3)"],
         "—",
         "La **seguridad nacional** es **responsabilidad exclusiva de cada Estado miembro** (4.2). La cooperación leal obliga **en los dos sentidos** (Unión ↔ Estados)."))}

{unidad("3.2 Atribución, subsidiariedad y proporcionalidad (art. 5)",
  LT(5, ["principio de atribución", "principios de subsidiariedad y proporcionalidad", "la Unión actúa dentro de los límites de las competencias que le atribuyen los Estados miembros en los Tratados", "en los ámbitos que no sean de su competencia exclusiva", "Los Parlamentos nacionales velarán por el respeto del principio de subsidiariedad", "no excederán de lo necesario para alcanzar los objetivos de los Tratados"]),
  fichab("Los tres principios de las competencias de la Unión",
         "Las instituciones de la Unión los aplican; los **Parlamentos nacionales** velan por la subsidiariedad",
         ["**Atribución** (delimitación): la Unión solo actúa dentro de las competencias atribuidas; el resto, a los Estados (5.2)", "**Subsidiariedad** (ejercicio): solo fuera de la competencia exclusiva, si los Estados no pueden alcanzar los objetivos de manera suficiente y la Unión puede hacerlo mejor (5.3)", "**Proporcionalidad** (ejercicio): contenido y forma no exceden de lo necesario (5.4)"],
         "Se aplican conforme al Protocolo sobre la aplicación de los principios de subsidiariedad y proporcionalidad",
         f"La **delimitación** se rige por la **atribución**; el **ejercicio**, por **subsidiariedad y proporcionalidad** (5.1). La subsidiariedad **no** se aplica a las competencias **exclusivas**. Dos preguntas oficiales de 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s6", "II.4 Derechos fundamentales, defensa de los valores y vecindad (TUE, arts. 6 a 8)", f"""
{unidad("4.1 Carta de Derechos Fundamentales y Convenio Europeo (art. 6)",
  LT(6, ["la cual tendrá el mismo valor jurídico que los Tratados", "no ampliarán en modo alguno las competencias de la Unión", "La Unión se adherirá al Convenio Europeo", "como principios generales"]),
  fichab("Protección de los derechos fundamentales en la Unión (se desarrolla en el tema II.4)",
         "La Unión",
         ["Reconoce la **Carta** (7-12-2000, adaptada el 12-12-2007 en Estrasburgo), con el **mismo valor jurídico que los Tratados** (6.1)", "Se **adherirá** al Convenio Europeo para la Protección de los Derechos Humanos (6.2)", "Los derechos del Convenio y de las tradiciones constitucionales comunes son **principios generales** del Derecho de la Unión (6.3)"],
         "—",
         "La Carta **no amplía** las competencias de la Unión, y la adhesión al Convenio **tampoco** las modifica."))}

{unidad("4.2 Riesgo y violación grave de los valores del art. 2 (art. 7)",
  LT(7, ["un tercio de los Estados miembros, del Parlamento Europeo o de la Comisión", "por mayoría de cuatro quintos de sus miembros", "un riesgo claro de violación grave", "El Consejo Europeo, por unanimidad", "violación grave y persistente", "por mayoría cualificada", "incluidos los derechos de voto del representante del Gobierno de dicho Estado miembro en el Consejo"]),
  fichab("Mecanismo de defensa de los valores de la Unión frente a un Estado miembro",
         ["::Proponen y deciden:", "**Riesgo claro** (7.1): proponen un tercio de los Estados, el Parlamento Europeo o la Comisión; constata el **Consejo**", "**Violación grave y persistente** (7.2): proponen un tercio de los Estados o la Comisión; constata el **Consejo Europeo**", "**Sanción** (7.3): decide el **Consejo**"],
         ["Antes de constatar el riesgo, el Consejo **oye** al Estado y puede dirigirle recomendaciones (7.1)", "Constatada la violación, el Consejo puede **suspender derechos**, incluido el **voto** en el Consejo (7.3); las **obligaciones** del Estado siguen vinculándole"],
         ["Riesgo: **cuatro quintos** de los miembros del Consejo + aprobación del Parlamento Europeo", "Violación: **unanimidad** del Consejo Europeo + aprobación del Parlamento Europeo", "Suspensión, modificación o revocación: **mayoría cualificada** del Consejo"],
         "Tres escalones con **tres mayorías**: 4/5 (riesgo, Consejo), unanimidad (violación, Consejo Europeo), mayoría cualificada (sanción, Consejo). En el 7.2 **no** propone el Parlamento Europeo."))}

{unidad("4.3 Relaciones con los países vecinos (art. 8)",
  LT(8, ["relaciones preferentes", "un espacio de prosperidad y de buena vecindad", "acuerdos específicos"]),
  fichab("Política de vecindad", "La Unión, con los países vecinos",
         "Relaciones preferentes y **acuerdos específicos** con derechos y obligaciones recíprocos y acciones en común", "Aplicación: concertación periódica",
         "El objetivo es un **espacio de prosperidad y de buena vecindad** basado en los valores de la Unión; no es una adhesión."))}

{resumen([
  "La Unión se crea **por Tratado** entre Estados que le **atribuyen competencias**; se fundamenta en el **TUE** y el **TFUE**, con el **mismo valor jurídico**, y sucede a la Comunidad Europea (art. 1); tiene **personalidad jurídica** (art. 47).",
  "**Valores** (art. 2): dignidad humana, libertad, democracia, igualdad, Estado de Derecho y derechos humanos. **Finalidad** (art. 3.1): paz, valores y bienestar de sus pueblos.",
  "**Atribución** delimita; **subsidiariedad** y **proporcionalidad** rigen el ejercicio (art. 5); lo no atribuido es de los Estados y la seguridad nacional es exclusiva de cada Estado (art. 4).",
  "Art. 7: riesgo (Consejo, **4/5**), violación grave y persistente (Consejo Europeo, **unanimidad**), suspensión de derechos (Consejo, **mayoría cualificada**)."],
  "Siguiente: III. ¿Con qué Tratados? Los Tratados originarios y modificativos")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Con qué Tratados? Los Tratados originarios y modificativos", donde(
  "Tercera pregunta. La Unión de hoy es el resultado de **tres Tratados originarios** (CECA, CEE y Euratom) y de una cadena de **Tratados modificativos** que culmina en Lisboa. Las fechas y contenidos históricos salen literales de las fichas del Parlamento Europeo (no son texto legal); el procedimiento vigente para reformar los Tratados es el art. 48 TUE.",
  ["1 Los Tratados originarios: París (1951) y Roma (1957)", "2 Los Tratados modificativos hasta Niza", "3 Del Tratado constitucional al Tratado de Lisboa", "4 Cómo se modifican hoy los Tratados (art. 48 TUE)"]))

T.ap("s7", "III.1 Los Tratados originarios: París (1951) y Roma (1957)", f"""
{unidad("1.1 El Tratado de París: la CECA",
  web("PE", PE1,
      "El Tratado constitutivo de la Comunidad Europea del Carbón y del Acero (CECA – Tratado de París): firmado el **18 de abril de 1951** y que entró en vigor el **23 de julio de 1952**, creó la Comunidad Europea del Carbón y del Acero (CECA) y creó instituciones comunes, entre ellas la Alta Autoridad, la Asamblea Parlamentaria, el Consejo de Ministros, el Tribunal de Justicia y un Comité Consultivo. El artículo 97 preveía la expiración del Tratado al cabo de **50 años**, el 23 de julio de 2002;"),
  fichab("Primer Tratado originario: Comunidad Europea del Carbón y del Acero",
         cw(PE1, "Francia, Italia, Alemania y los países del Benelux (Bélgica, los Países Bajos y Luxemburgo) firmaron el Tratado de París"),
         f"Mercado común del carbón y del acero, con instituciones propias: {cw(PE1, 'la Alta Autoridad, la Asamblea Parlamentaria, el Consejo de Ministros, el Tribunal de Justicia y un Comité Consultivo')}",
         ["Firma: 18-4-1951 (París)", "Entrada en vigor: 23-7-1952", "Duración: **50 años** (expiró el 23-7-2002)"],
         "Es el **único** Tratado originario **de duración limitada** (50 años); los de Roma se celebraron **por tiempo indefinido** (→ III.1.2). El ejecutivo de la CECA era la **Alta Autoridad**."))}

{unidad("1.2 Los Tratados de Roma: CEE y Euratom",
  web("PE", PE1,
      "Los Tratados de Roma, que crean la Comunidad Económica Europea (CEE) y la Comunidad Europea de la Energía Atómica (Euratom), o los Tratados de Roma: firmados el **25 de marzo de 1957** y que entraron en vigor el **1 de enero de 1958**, crearon la Comunidad Económica Europea (CEE) y la Comunidad Europea de la Energía Atómica (Euratom). El artículo 240 del Tratado CEE y el artículo 208 del Tratado CEEA establecían expresamente que ambos pactos se celebraban **por tiempo indefinido**.",
      "El objetivo de la CEE era establecer un mercado común basado en las cuatro libertades de circulación (mercancías, de personas, de capitales y servicios).",
      "El objetivo de Euratom era coordinar el suministro de materiales fisionables y los programas de investigación ya iniciados por los distintos Estados o que estos se disponían a lanzar con miras a la utilización pacífica de la energía nuclear.",
      "En el Convenio sobre determinadas instituciones comunes a las Comunidades Europeas, que se firmó y entró en vigor al mismo tiempo que los Tratados de Roma, se estableció que la **Asamblea Parlamentaria y el Tribunal de Justicia** serían instituciones comunes."),
  fichab("Segundo y tercer Tratados originarios: Comunidad Económica Europea y Euratom",
         "Los mismos seis Estados fundadores",
         ["CEE: **mercado común** basado en las cuatro libertades de circulación", "Euratom: suministro de materiales fisionables e investigación para el **uso pacífico de la energía nuclear**", "Convenio de instituciones comunes: Asamblea Parlamentaria y Tribunal de Justicia **comunes**"],
         ["Firma: **25-3-1957**", "Entrada en vigor: **1-1-1958**", "Duración: **indefinida** (art. 240 CEE y 208 CEEA)"],
         "Son **dos** Tratados de Roma (CEE y CEEA/Euratom). Con el Convenio de 1957 ya eran comunes la Asamblea y el Tribunal; Consejo y Comisión se unificaron después (Tratado de Fusión, → III.2.1)."))}
""", 2)

T.ap("s8", "III.2 Los Tratados modificativos hasta Niza", f"""
{unidad("2.1 El Tratado de Fusión (1965) y los Tratados presupuestarios (1970 y 1975)",
  web("PE", PE1,
      "El proceso de unificación institucional se completó con el Tratado por el que se constituye un **Consejo único y una Comisión única** de las Comunidades Europeas, de **8 de abril de 1965**, conocido como **Tratado de Fusión**."),
  web("PE", PE2,
      "La primera modificación institucional fue la realizada por el Tratado de Fusión, de 8 de abril de 1965, que fusionó los órganos ejecutivos de las tres comunidades. Entró en vigor en **1967**, estableciendo un único Consejo y una única Comisión de las Comunidades Europeas (la Comunidad Europea del Carbón y del Acero, la CEE y la Comunidad Europea de la Energía Atómica) e introduciendo el principio de unidad presupuestaria.",
      "El Tratado de Luxemburgo, de 22 de abril de 1970, concedió al Parlamento Europeo determinadas competencias presupuestarias (1.3.1).",
      "El Tratado por el que se modifican determinadas disposiciones financieras de los Tratados constitutivos de las Comunidades Económicas Europeas y del Tratado por el que se constituye un Consejo único de las Comunidades Europeas (Tratado de Bruselas), de 22 de julio de 1975, otorgó al Parlamento el derecho a rechazar el presupuesto y a conceder a la Comisión la aprobación de la gestión en la ejecución del presupuesto. Este Tratado creó, asimismo, el **Tribunal de Cuentas**, organismo de control contable y de gestión financiera de la Comunidad (1.3.12)."),
  fichab("Primeras modificaciones: unificación de los ejecutivos y poderes presupuestarios",
         "Los Estados miembros de las tres Comunidades",
         ["Fusión: **un único Consejo y una única Comisión** para CECA, CEE y Euratom; principio de unidad presupuestaria", "Luxemburgo (1970): competencias presupuestarias del Parlamento Europeo", "Bruselas (1975): rechazo del presupuesto, aprobación de la gestión y creación del **Tribunal de Cuentas**"],
         ["Fusión: firmado el **8-4-1965**; en vigor en **1967**", "Luxemburgo: 22-4-1970", "Bruselas: 22-7-1975"],
         "Las tres Comunidades **siguen existiendo**: lo que se fusiona son sus **ejecutivos** (Consejo y Comisión). La fecha del Tratado de Fusión es el **8 de abril de 1965** (pregunta oficial X 31, → Cierre 1)."))}

{unidad("2.2 El Acta Única Europea (1986)",
  web("PE", PE2,
      "El 17 de febrero de 1986, procedieron a la firma del AUE nueve Estados miembros, a los que siguieron, el 28 de febrero de 1986, Dinamarca (tras celebrar un referéndum), Italia y Grecia. Ratificada por los respectivos Parlamentos de los Estados miembros a lo largo de 1986, el AUE entró en vigor el **1 de julio de 1987**, con seis meses de retraso debido a un recurso interpuesto ante los tribunales irlandeses por un particular. El Acta constituye la **primera modificación sustancial del Tratado de Roma**.",
      "La culminación de un mercado único plenamente operativo fue prevista para el **1 de enero de 1993**, lo que suponía la reactivación y ampliación del objetivo del mercado común ya introducido en 1958 (2.1.1).",
      "Mediante el reconocimiento de nuevas competencias en los ámbitos siguientes:",
      "política monetaria;",
      "política social;",
      "cohesión económica y social;",
      "investigación y desarrollo tecnológico;",
      "medio ambiente;",
      "cooperación en materia de política exterior.",
      "La votación por mayoría cualificada sustituyó a la unanimidad en cuatro competencias comunitarias…",
      "Las competencias del Parlamento se vieron reforzadas:…",
      "al introducir un procedimiento de cooperación con el Consejo (1.2.3), que dio al Parlamento auténticas, aunque limitadas, competencias legislativas."),
  fichab("Primera modificación sustancial del Tratado de Roma",
         "Doce Estados miembros (nueve firmaron el 17-2-1986; Dinamarca, Italia y Grecia, el 28-2-1986)",
         ["**Mercado interior** (gran mercado único) para el 1-1-1993", "Nuevas competencias (política monetaria, social, cohesión, investigación, medio ambiente, cooperación en política exterior)", "Más **mayoría cualificada** en el Consejo", "Procedimiento de **cooperación** del Parlamento con el Consejo"],
         ["Firma: 17 y 28-2-1986", "Entrada en vigor: **1-7-1987**"],
         "El AUE es la **primera modificación sustancial** del Tratado de Roma y fija el mercado único para el **1-1-1993**. Entró en vigor con seis meses de retraso."))}

{unidad("2.3 El Tratado de Maastricht (1992): nace la Unión Europea",
  web("PE", PE3,
      "El Tratado de la Unión Europea, firmado en Maastricht el **7 de febrero de 1992**, entró en vigor el **1 de noviembre de 1993**.",
      "Al instaurar una Unión Europea, el Tratado de Maastricht supuso una nueva etapa en el proceso de creación de «una unión cada vez más estrecha entre los pueblos de Europa». La Unión Europea se fundó sobre la base de las Comunidades Europeas, completadas con las políticas y formas de cooperación establecidas por el Tratado de la Unión Europea (TUE).",
      "El Tratado de Maastricht confirió ciertas competencias a la Unión creada por el mismo, las cuales se clasifican en tres grandes grupos conocidos comúnmente como «pilares»:",
      "el primer pilar estaba formado por las Comunidades Europeas…",
      "el segundo pilar estaba formado por la política exterior y de seguridad común prevista en el título V del Tratado;",
      "el tercer pilar estaba constituido por la cooperación en los ámbitos de la justicia y los asuntos de interior prevista en el título VI del Tratado."),
  fichab("Tratado de la Unión Europea: crea la Unión sobre tres pilares",
         "Los doce Estados miembros",
         ["1.er pilar: **Comunidades Europeas**", "2.º pilar: **PESC**", "3.er pilar: **justicia y asuntos de interior** (JAI)", "Se crean el Sistema Europeo de Bancos Centrales y el Banco Central Europeo"],
         ["Firma: **7-2-1992** (Maastricht)", "Entrada en vigor: **1-11-1993**"],
         f"La Unión nace en **Maastricht** sobre **tres pilares**; el 2.º y el 3.º eran de cooperación **intergubernamental**. Ojo: el art. 54.2 del TUE vigente conserva la fecha prevista inicialmente, {cT(54, 'El presente Tratado entrará en vigor el 1 de enero de 1993')}, pero según la ficha del Parlamento Europeo entró en vigor el **1 de noviembre de 1993**."))}

{unidad("2.4 El Tratado de Ámsterdam (1997)",
  web("PE", PE3,
      "El Tratado de Ámsterdam, por el que se modifican el Tratado de la Unión Europea, los Tratados constitutivos de las Comunidades Europeas y determinados actos conexos…firmado en Ámsterdam el **2 de octubre de 1997**, entró en vigor el **1 de mayo de 1999**.",
      "Por primera vez, los Tratados contenían disposiciones generales que permitían a un determinado número de Estados miembros recurrir, en ciertas condiciones, a las instituciones comunes para organizar una **cooperación reforzada** entre ellos.",
      "Asimismo, preveía una nueva numeración de los artículos de los Tratados."),
  fichab("Reforma para una Unión más eficaz y democrática ante la ampliación",
         "Los quince Estados miembros",
         ["Comunitariza ámbitos del tercer pilar (asilo, inmigración, fronteras exteriores, cooperación judicial civil) e integra el acervo de Schengen", "Amplía la **codecisión**", "Introduce disposiciones generales sobre **cooperación reforzada** (→ VI.1.2)", "Simplifica y **renumera** los artículos de los Tratados"],
         ["Firma: **2-10-1997**", "Entrada en vigor: **1-5-1999**"],
         "La cooperación reforzada con disposiciones generales aparece **por primera vez** en **Ámsterdam**, no en Niza ni en Lisboa."))}

{unidad("2.5 El Tratado de Niza (2001)",
  web("PE", PE4,
      "El Tratado de Niza, que modificaba el Tratado de la Unión Europea (TUE) y los Tratados constitutivos de las Comunidades Europeas y algunos actos conexos, se firmó el **26 de febrero de 2001** y entró en vigor el **1 de febrero de 2003**.",
      "El Tratado de Niza tenía, por consiguiente, el objetivo de hacer que las instituciones de la Unión fueran más eficaces y legítimas y de preparar a la Unión para su siguiente gran ampliación.",
      "Se proclamó una Carta de los Derechos Fundamentales de la Unión Europea, no vinculante."),
  fichab("Reforma institucional para preparar la gran ampliación",
         "Los quince Estados miembros",
         ["Nueva ponderación de votos en el Consejo y composición de la Comisión", "Reforma del sistema judicial", "Cooperación reforzada más flexible, extendida a los **tres pilares** (→ VI.1.2)", "Proclamación de la **Carta**, entonces **no vinculante**"],
         ["Firma: **26-2-2001**", "Entrada en vigor: **1-2-2003**"],
         "En Niza la Carta se **proclamó sin valor vinculante**; hoy tiene **el mismo valor jurídico que los Tratados** (art. 6.1 TUE, → II.4.1)."))}
""", 2)

T.ap("s9", "III.3 Del Tratado constitucional al Tratado de Lisboa", f"""
{unidad("3.1 El Tratado por el que se establece una Constitución para Europa (fracasado)",
  web("PE", PE4,
      "El 18 de junio de 2004, el Consejo Europeo aprobó el Proyecto de Tratado por el que se instituye una Constitución para Europa con un considerable número de enmiendas, si bien se mantuvo la estructura esencial del proyecto de Convención. El Tratado propuesto fue aprobado por el Parlamento Europeo en enero de 2005, pero meses después fue rechazado por **Francia (29 de mayo de 2005)** y por los **Países Bajos (1 de junio de 2005)** en sendos referendos nacionales. A consecuencia del resultado negativo en estos referendos celebrados en dos Estados miembros, no se pudo concluir el procedimiento de ratificación del Tratado por el que se establece una Constitución para Europa."),
  fichab("Intento de sustituir los Tratados por una Constitución",
         "Preparado por la Convención sobre el futuro de Europa; aprobado por el Consejo Europeo",
         "Texto único que debía sustituir a los Tratados existentes",
         ["Aprobación del Consejo Europeo: 18-6-2004", "Rechazo: Francia (29-5-2005) y Países Bajos (1-6-2005), en referéndum"],
         "La Constitución **nunca entró en vigor**: la rechazaron **Francia y los Países Bajos** en referéndum."))}

{unidad("3.2 El Tratado de Lisboa (2007)",
  web("PE", PE5,
      "Tras un «período de reflexión» de dos años, la Conferencia Intergubernamental de 2007 reactivó los objetivos y logros del Tratado Constitucional, y los elevó al rango de tratado modificando los Tratados existentes:",
      "El contenido es en su mayoría el mismo que el del Tratado Constitucional, aunque la mención de los símbolos de la Unión (lema, himno, euro, bandera, Día de Europa) y la primacía del Derecho de la UE se trasladaron a declaraciones específicas anejas a los Tratados. El texto consta de unas 325 páginas que incluyen nuevas disposiciones, disposiciones modificativas, 37 protocolos y 65 declaraciones. Se aprobó el **13 de diciembre de 2007** durante el Consejo Europeo de Lisboa y ha sido ratificado por todos los Estados miembros (esto es, los países que forman parte de la Unión). Entró en vigor el **1 de diciembre de 2009**."),
  lit("LO1_2008", "a1", ["firmado en la capital de la República de Portugal el 13 de diciembre de 2007"], titulo="Artículo 1 (LO 1/2008). Autorización de la ratificación del Tratado de Lisboa"),
  fichab("Último Tratado modificativo: TUE y TFUE actuales",
         "Los Estados miembros; España autorizó su ratificación por la **Ley Orgánica 1/2008**",
         ["Modifica el TUE y el Tratado constitutivo de la Comunidad Europea (que pasa a ser el **TFUE**, → IV.1)", "Recoge la mayor parte del contenido del Tratado constitucional", "Símbolos y primacía, en **declaraciones** anejas"],
         ["Firma: **13-12-2007** (Lisboa)", "Entrada en vigor: **1-12-2009**"],
         f"En España la autorización es por **ley orgánica** ({c('LO1_2008', 'a1', 'Se autoriza la ratificación por España del Tratado de Lisboa')}). Lisboa **modifica** los Tratados; no los sustituye por un texto único."))}
""", 2)

T.ap("s10", "III.4 Cómo se modifican hoy los Tratados (TUE, art. 48)", f"""
{unidad("4.1 El procedimiento de revisión ordinario (art. 48.1 a 5)",
  LT(48, ["procedimiento de revisión ordinario", "El Gobierno de cualquier Estado miembro, el Parlamento Europeo o la Comisión podrán presentar al Consejo proyectos de revisión", "aumentar o reducir las competencias", "adopta por mayoría simple una decisión favorable", "convocará una Convención", "adoptará por consenso una recomendación", "no convocar una Convención", "aprueben de común acuerdo", "ratificadas por todos los Estados miembros", "transcurrido un plazo de dos años", "las cuatro quintas partes de los Estados miembros"], solo=[1, 2, 3, 4, 5, 6, 7]),
  fichab("Reforma de los Tratados por Convención y Conferencia intergubernamental",
         ["**Iniciativa**: Gobierno de cualquier Estado miembro, Parlamento Europeo o Comisión → al **Consejo**, que remite al Consejo Europeo y notifica a los Parlamentos nacionales", "**Convención**: representantes de Parlamentos nacionales, Jefes de Estado o de Gobierno, Parlamento Europeo y Comisión", "**Conferencia** de representantes de los Gobiernos: aprueba las modificaciones"],
         ["Consejo Europeo decide examinar (consulta al PE y a la Comisión; al BCE si hay cambios institucionales monetarios)", "Convención → recomendación por **consenso** (o sin Convención, con mandato del Consejo Europeo)", "Conferencia: **común acuerdo**", "Entrada en vigor: tras la **ratificación de todos** los Estados"],
         ["Decisión de examinar: **mayoría simple** del Consejo Europeo", "No convocar Convención: mayoría simple del Consejo Europeo + **aprobación** del Parlamento Europeo", "Si a los **2 años** de la firma han ratificado **4/5** y hay dificultades: lo examina el Consejo Europeo"],
         "La iniciativa es del **Gobierno de cualquier Estado miembro, el Parlamento Europeo o la Comisión** (no el Consejo Europeo ni el BCE): pregunta oficial X 30 (→ Cierre 1). Puede servir para **aumentar o reducir** competencias."))}

{unidad("4.2 Los procedimientos de revisión simplificados (art. 48.6 y 7)",
  LT(48, ["tercera parte del Tratado de Funcionamiento de la Unión Europea", "El Consejo Europeo se pronunciará por unanimidad", "no podrá aumentar las competencias atribuidas a la Unión", "a pronunciarse por mayoría cualificada", "con arreglo al procedimiento legislativo ordinario", "en un plazo de seis meses"], solo=[8, 9, 10, 11, 12, 13, 14]),
  fichab("Reformas sin Conferencia intergubernamental: tercera parte del TFUE y «pasarelas»",
         "Iniciativa: Gobierno de cualquier Estado miembro, Parlamento Europeo o Comisión (48.6); decide el **Consejo Europeo**",
         ["48.6: decisión que modifica la **tercera parte del TFUE** (políticas y acciones internas); entra en vigor tras la aprobación de los Estados", "48.7: autorizar al Consejo a pasar de **unanimidad a mayoría cualificada**, o de procedimiento legislativo **especial a ordinario**"],
         ["48.6: **unanimidad** del Consejo Europeo, consultando al PE y a la Comisión", "48.7: **unanimidad** del Consejo Europeo + aprobación del PE (mayoría de sus miembros); veto de **cualquier Parlamento nacional** en **6 meses**"],
         "El 48.6 **no puede aumentar** las competencias de la Unión. La pasarela del 48.7 no vale para decisiones con repercusiones **militares o de defensa**."))}

{unidad("4.3 Cuadro de los Tratados originarios y modificativos (esquema)",
  ESQ,
  TAB2)}

{resumen([
  "Originarios: **París** (CECA, 1951; 50 años) y **Roma** (CEE y Euratom, 25-3-1957; indefinidos).",
  "Modificativos: **Fusión** (1965), **Acta Única** (1986), **Maastricht** (1992; nace la Unión), **Ámsterdam** (1997), **Niza** (2001) y **Lisboa** (2007, en vigor el 1-12-2009). La Constitución para Europa fracasó (2005).",
  "Revisión (art. 48): **ordinaria** (iniciativa de un Gobierno, el PE o la Comisión; Convención; Conferencia; ratificación de todos) y **simplificadas** (unanimidad del Consejo Europeo)."],
  "Siguiente: IV. ¿Qué son el TUE y el TFUE?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Qué son el TUE y el TFUE? (TUE, arts. 1, 51 y 53; TFUE, art. 1)", donde(
  "Cuarta pregunta. Desde Lisboa, la Unión se apoya en **dos Tratados** con el mismo valor jurídico: el **TUE** (principios, instituciones, acción exterior) y el **TFUE** (funcionamiento y competencias). Aquí se ve qué hace cada uno y cómo están organizados.",
  ["1 Dos Tratados con el mismo valor jurídico (art. 1 TFUE)", "2 Cómo están organizados y disposiciones finales (arts. 51 y 53 TUE)"]))

T.ap("s11", "IV.1 Dos Tratados con el mismo valor jurídico (TFUE, art. 1)", f"""
{unidad("1.1 Qué organiza el TFUE (art. 1 TFUE)",
  LF(1, ["organiza el funcionamiento de la Unión", "los ámbitos, la delimitación y las condiciones de ejercicio de sus competencias", "que tienen el mismo valor jurídico"]),
  fichab("Objeto del TFUE y relación con el TUE",
         "—",
         ["El TFUE **organiza el funcionamiento** de la Unión y determina sus **competencias** (ámbitos, delimitación, condiciones de ejercicio)", "TUE + TFUE = «los Tratados» (también art. 1 TUE, → II.1.2)"],
         f"{cF(1, 'Estos dos Tratados, que tienen el mismo valor jurídico')}",
         "No hay jerarquía entre TUE y TFUE: **mismo valor jurídico**, lo dicen **los dos** (art. 1 TUE y art. 1.2 TFUE)."))}

{unidad("1.2 El TUE y el TFUE tras Lisboa",
  web("PE", PE5,
      "El Tratado de Lisboa modificó los Tratados existentes, lo que dio lugar a los dos Tratados fundamentales siguientes:",
      "el Tratado de la Unión Europea (TUE), que establece los objetivos, los principios, las instituciones y los procesos principales de toma de decisiones de la Unión;",
      "el Tratado de Funcionamiento de la Unión Europea (TFUE), que sustituye al Tratado constitutivo de la Comunidad Europea (TCE) y define las políticas de la Unión."),
  fichab("Reparto de contenidos entre los dos Tratados",
         "—",
         ["**TUE**: objetivos, principios, instituciones y procesos principales de decisión", "**TFUE**: sustituye al TCE y define las **políticas** de la Unión"],
         "—",
         "El TFUE es el antiguo **Tratado constitutivo de la Comunidad Europea** renombrado y modificado por Lisboa."))}
""", 2)

T.ap("s12", "IV.2 Cómo están organizados y disposiciones finales (TUE, arts. 51 y 53)", f"""
{unidad("2.1 Estructura del TUE (títulos)",
  web("DOUE", TUEX,
      "TÍTULO I DISPOSICIONES COMUNES",
      "TÍTULO II DISPOSICIONES SOBRE LOS PRINCIPIOS DEMOCRÁTICOS",
      "TÍTULO III DISPOSICIONES SOBRE LAS INSTITUCIONES",
      "TÍTULO IV DISPOSICIONES SOBRE LAS COOPERACIONES REFORZADAS",
      "TÍTULO V DISPOSICIONES GENERALES RELATIVAS A LA ACCIÓN EXTERIOR DE LA UNIÓN Y DISPOSICIONES ESPECÍFICAS RELATIVAS A LA POLÍTICA EXTERIOR Y DE SEGURIDAD COMÚN",
      "TÍTULO VI DISPOSICIONES FINALES",
      que="Versión consolidada del Tratado de la Unión Europea (DOUE C 202 de 7-6-2016), índice · rúbricas de los títulos"),
  fichab("Seis títulos (arts. 1 a 55)", "—",
         ["I: disposiciones comunes (arts. 1 a 8, → II)", "II: principios democráticos", "III: instituciones (tema II.2 y tema II.3)", "IV: cooperaciones reforzadas (art. 20, → VI.1)", "V: acción exterior y PESC (tema II.6)", "VI: disposiciones finales (arts. 47 a 55)"],
         "—",
         "Las **cooperaciones reforzadas** tienen un título propio en el TUE (**título IV**, solo el art. 20) y otro en el TFUE (título III de la sexta parte, arts. 326 a 334)."))}

{unidad("2.2 Estructura del TFUE (partes)",
  web("DOUE", TFUEX,
      "PRIMERA PARTE PRINCIPIOS",
      "SEGUNDA PARTE NO DISCRIMINACIÓN Y CIUDADANÍA DE LA UNIÓN",
      "TERCERA PARTE POLÍTICAS Y ACCIONES INTERNAS DE LA UNIÓN",
      "CUARTA PARTE ASOCIACIÓN DE LOS PAÍSES Y TERRITORIOS DE ULTRAMAR",
      "QUINTA PARTE ACCIÓN EXTERIOR DE LA UNIÓN",
      "SEXTA PARTE DISPOSICIONES INSTITUCIONALES Y FINANCIERAS",
      "SÉPTIMA PARTE DISPOSICIONES GENERALES Y FINALES",
      que="Versión consolidada del Tratado de Funcionamiento de la Unión Europea (DOUE C 202 de 7-6-2016), índice · rúbricas de las partes"),
  fichab("Siete partes", "—",
         ["1.ª: principios (categorías y ámbitos de competencias)", "3.ª: políticas y acciones internas (es la que puede revisarse por el procedimiento simplificado del art. 48.6 TUE, → III.4.2)", "6.ª: disposiciones institucionales y financieras (incluye las cooperaciones reforzadas, → VI.2)"],
         "—",
         "El TUE se divide en **títulos**; el TFUE, en **partes** (siete)."))}

{unidad("2.3 Protocolos y anexos; duración (arts. 51 y 53)",
  LT(51, ["forman parte integrante de los mismos"]),
  LT(53, ["por un período de tiempo ilimitado"]),
  fichab("Valor de protocolos y anexos y vigencia del TUE", "—",
         ["Los **Protocolos y Anexos** forman parte integrante de los Tratados (51)", "El TUE se concluye por tiempo **ilimitado** (53)"],
         "Duración: **ilimitada**",
         "Los protocolos tienen el **mismo valor** que los Tratados (son parte integrante). Ilimitado, como los Tratados de Roma (indefinidos), a diferencia de la CECA (50 años)."))}

{resumen([
  "La Unión se fundamenta en el **TUE** y el **TFUE**, con el **mismo valor jurídico** (art. 1 TUE; art. 1.2 TFUE).",
  "TUE: objetivos, principios, instituciones; **seis títulos**. TFUE: funcionamiento y competencias; **siete partes**; sustituye al TCE.",
  "**Protocolos y Anexos** son parte integrante (art. 51); el TUE es de duración **ilimitada** (art. 53); la Unión tiene **personalidad jurídica** (art. 47)."],
  "Siguiente: V. ¿Cómo se entra y cómo se sale? Ampliación y retirada")}
""", 2)

# =============================================================================
T.ap("bV", "V. ¿Cómo se entra y cómo se sale? Ampliación y retirada (TUE, arts. 49 y 50)", donde(
  "Quinta pregunta. La Unión ha pasado de seis a veintisiete Estados mediante sucesivas **ampliaciones** (art. 49) y ha conocido una **retirada** (art. 50). Los requisitos y el procedimiento están en el TUE; los criterios de Copenhague y la historia de las ampliaciones, en la ficha del Parlamento Europeo.",
  ["1 La adhesión de nuevos Estados (art. 49) y los criterios de Copenhague", "2 Las sucesivas ampliaciones", "3 La retirada de un Estado miembro (art. 50)"]))

T.ap("s13", "V.1 La adhesión de nuevos Estados (TUE, art. 49) y los criterios de Copenhague", f"""
{unidad("1.1 Quién puede solicitar el ingreso y cómo se decide (art. 49)",
  LT(49, ["Cualquier Estado europeo que respete los valores mencionados en el artículo 2 y se comprometa a promoverlos", "al Parlamento Europeo y a los Parlamentos nacionales", "dirigirá su solicitud al Consejo, que se pronunciará por unanimidad", "después de haber consultado a la Comisión", "por mayoría de los miembros que lo componen", "criterios de elegibilidad acordados por el Consejo Europeo", "un acuerdo entre los Estados miembros y el Estado solicitante", "la ratificación de todos los Estados contratantes"]),
  fichab("Procedimiento de adhesión a la Unión",
         ["**Solicita**: cualquier Estado **europeo** que respete los valores del art. 2 y se comprometa a promoverlos", "**Decide**: el **Consejo**", "Interviene la **Comisión** (consulta) y el **Parlamento Europeo** (aprobación); se informa a los Parlamentos nacionales"],
         ["Solicitud al **Consejo**", "Consulta a la Comisión y **aprobación** del Parlamento Europeo", "**Acuerdo** entre los Estados miembros y el solicitante sobre condiciones y adaptaciones de los Tratados", "**Ratificación** por todos los Estados contratantes"],
         ["Consejo: **unanimidad**", "Parlamento Europeo: **mayoría de los miembros que lo componen**"],
         "La solicitud va **al Consejo**, que decide por **unanimidad** (no a la Comisión ni al Parlamento): pregunta oficial P 9 (→ Cierre 1). La Comisión solo es **consultada**."))}

{unidad("1.2 Los criterios de Copenhague (1993)",
  web("PE", PE167,
      "Cualquier Estado europeo podrá solicitar el ingreso como miembro en la Unión si respeta sus valores comunes y se compromete a promoverlos (artículo 49 del TUE). Los **criterios de Copenhague**, establecidos por el Consejo Europeo celebrado en Copenhague en **1993**, resultan de crucial importancia en el proceso de integración en la Unión de todo país candidato o candidato potencial. Estos criterios incluyen:",
      "la presencia de instituciones estables que garanticen la democracia, el Estado de Derecho, los derechos humanos, y el respeto a las minorías, así como su protección;",
      "la existencia de una economía de mercado viable, así como la capacidad de hacer frente a la presión competitiva y las fuerzas del mercado dentro de la Unión;",
      "la capacidad de asumir las obligaciones que se derivan de la adhesión, en particular de suscribir los objetivos de la unión política, económica y monetaria y adoptar las normas y políticas comunes que constituyen la legislación de la Unión, es decir, el acervo comunitario."),
  fichab("Criterios de elegibilidad para la adhesión",
         "Fijados por el **Consejo Europeo** de Copenhague (1993); el art. 49 manda tener en cuenta los criterios de elegibilidad del Consejo Europeo",
         ["**Político**: instituciones estables (democracia, Estado de Derecho, derechos humanos, minorías)", "**Económico**: economía de mercado viable y capacidad de competir", "**Acervo**: capacidad de asumir las obligaciones de la adhesión"],
         "—",
         "Son **tres** criterios y los fijó el **Consejo Europeo** (1993), no el Tratado. El art. 49 solo remite a ellos («criterios de elegibilidad acordados por el Consejo Europeo»)."))}

{unidad("1.3 El proceso de adhesión en la práctica",
  web("PE", PE167,
      "Todo país que desee ingresar en la Unión debe dirigir su solicitud al Consejo de la Unión Europea, que pedirá a la Comisión que presente un dictamen al respecto. Se informa de esta solicitud al Parlamento. Si la Comisión emite un dictamen favorable, los jefes de Estado o de Gobierno de la Unión pueden decidir, por unanimidad en el Consejo Europeo, conferir el estatuto de candidato al país. Una vez que la Comisión ha formulado su recomendación, el Consejo Europeo decide, de nuevo por unanimidad, si se ha de proceder a la apertura de negociaciones. El conjunto de la legislación de la Unión (el acervo comunitario) se divide en más de treinta capítulos.",
      "Una vez concluidas las negociaciones sobre todos los capítulos o grupos de capítulos, las condiciones acordadas —incluidas las posibles cláusulas de salvaguardia y disposiciones transitorias— se plasman en un tratado de adhesión entre los Estados miembros de la Unión y el país adherente. La firma de dicho tratado únicamente puede tener lugar una vez que se disponga del beneplácito del Parlamento, así como de la aprobación por unanimidad del Consejo de la Unión Europea. Es entonces cuando el tratado de adhesión se somete a la ratificación de todos los Estados contratantes, incluido el país adherente, de conformidad con sus normas constitucionales correspondientes (es decir, ratificación parlamentaria o mediante referéndum)."),
  fichab("Fases: solicitud, candidatura, negociación, tratado de adhesión y ratificación",
         "Consejo de la UE, Comisión (dictamen y recomendaciones), Consejo Europeo (estatuto de candidato y apertura de negociaciones), Parlamento Europeo (beneplácito)",
         ["Solicitud al Consejo → dictamen de la Comisión", "Estatuto de **candidato** y apertura de negociaciones: Consejo Europeo", "Negociación por **capítulos** del acervo (más de treinta)", "**Tratado de adhesión** → ratificación de todos los Estados contratantes, incluido el adherente"],
         "**Unanimidad** en cada decisión del Consejo Europeo y del Consejo",
         "La ficha describe la práctica; el texto que se pregunta literal es el **art. 49** (→ V.1.1)."))}
""", 2)

T.ap("s14", "V.2 Las sucesivas ampliaciones", f"""
{unidad("2.1 De seis a veintiocho Estados (1958-2013)",
  web("PE", PE2,
      "El **1 de enero de 1973** tuvo lugar la adhesión del Reino Unido, así como de Dinamarca e Irlanda, mientras que el pueblo noruego rechazó la adhesión por referéndum. Grecia pasó a ser miembro en 1981, y **Portugal y España se adhirieron en 1986**."),
  web("PE", PE167,
      "La adhesión de Croacia a la Unión el **1 de julio de 2013** constituye un importante incentivo para otros países de la región."),
  ESQ,
  TAB3,
  fichab("Ampliaciones de la Unión", "Los Estados adherentes en cada ronda", "Por tratado de adhesión (art. 49, → V.1.1)",
         "1973 · 1981 · 1986 · 1995 · 2004 · 2007 · 2013",
         "**España y Portugal: 1986.** La primera ampliación es la de **1973** (Reino Unido, Dinamarca e Irlanda). La mayor, la de **2004** (diez Estados). La última, **Croacia** (1-7-2013)."))}

{unidad("2.2 Los candidatos actuales",
  web("PE", PE167,
      "Se han entablado negociaciones y abierto capítulos de adhesión con Albania, Montenegro, Serbia y Turquía. Macedonia del Norte abrió negociaciones de adhesión en 2022, y Bosnia y Herzegovina lo hizo en 2024. Kosovo presentó su solicitud de adhesión a la Unión en 2022. En 2023, la Unión decidió iniciar las negociaciones de adhesión con Moldavia y Ucrania y conceder a Georgia el estatuto de país candidato"),
  fichab("Estado de la ampliación según la ficha del Parlamento Europeo", "Balcanes Occidentales, Turquía, Moldavia, Ucrania y Georgia", "Negociaciones por capítulos", "—",
         f"Dato **cambiante**: comprobar la ficha actualizada antes del examen. Según la misma ficha, {cw(PE167, 'Turquía solicitó su ingreso en la Unión en 1987')}."))}
""", 2)

T.ap("s15", "V.3 La retirada de un Estado miembro (TUE, art. 50)", f"""
{unidad("3.1 Procedimiento de retirada (art. 50)",
  LT(50, ["de conformidad con sus normas constitucionales, retirarse de la Unión", "notificará su intención al Consejo Europeo", "El Consejo lo celebrará en nombre de la Unión por mayoría cualificada, previa aprobación del Parlamento Europeo", "a los dos años de la notificación", "decide por unanimidad prorrogar dicho plazo", "no participará ni en las deliberaciones ni en las decisiones", "se someterá al procedimiento establecido en el artículo 49"]),
  fichab("Salida voluntaria de la Unión",
         ["**Decide**: el Estado, según sus normas constitucionales", "**Notificación**: al **Consejo Europeo** (que da orientaciones)", "**Celebra el acuerdo**: el **Consejo**, en nombre de la Unión, con aprobación del Parlamento Europeo"],
         ["Notificación → negociación del **acuerdo de retirada** (art. 218.3 TFUE) → celebración", "Los Tratados dejan de aplicarse desde la entrada en vigor del acuerdo o, en su defecto, **a los dos años** de la notificación", "El Estado que se retira **no participa** en las deliberaciones ni decisiones que le afecten", "Si quiere volver: procedimiento del **art. 49** (→ V.1.1)"],
         ["Acuerdo: **mayoría cualificada** del Consejo + aprobación del PE", "Prórroga del plazo de dos años: **unanimidad** del Consejo Europeo, de acuerdo con el Estado"],
         "Se notifica al **Consejo Europeo**, pero el acuerdo lo celebra el **Consejo** por **mayoría cualificada** (no por unanimidad). Plazo: **dos años**, prorrogable por unanimidad."))}

{unidad("3.2 La retirada del Reino Unido",
  web("PE", PE167, "El Reino Unido abandonó la Unión el **31 de enero de 2020**."),
  fichab("Salida del Reino Unido de la Unión", "Reino Unido", "—", "Salida: 31-1-2020",
         "La versión consolidada de 2016 del TUE aún enumera al Reino Unido en el art. 52.1: por eso ese artículo no se reproduce aquí."))}

{resumen([
  "Adhesión (art. 49): **cualquier Estado europeo** que respete y promueva los valores del art. 2; solicitud al **Consejo** (unanimidad), consulta a la Comisión, aprobación del PE (**mayoría de sus miembros**); acuerdo y **ratificación de todos**.",
  "Criterios de **Copenhague** (Consejo Europeo, 1993): político, económico y asunción del acervo.",
  "Ampliaciones: 1973, 1981, **1986 (España y Portugal)**, 1995, 2004, 2007 y 2013 (Croacia).",
  "Retirada (art. 50): notificación al **Consejo Europeo**; acuerdo del **Consejo** por **mayoría cualificada** con aprobación del PE; **dos años** prorrogables por unanimidad; Reino Unido, 31-1-2020."],
  "Siguiente: VI. ¿Cómo avanzan solo algunos Estados? Las cooperaciones reforzadas")}
""", 2)

# =============================================================================
T.ap("bVI", "VI. ¿Cómo avanzan solo algunos Estados? Las cooperaciones reforzadas (TUE, art. 20; TFUE, arts. 326 a 334)", donde(
  "Sexta pregunta. Cuando la Unión en su conjunto no puede avanzar, un grupo de Estados puede **cooperar más estrechamente** usando las instituciones de la Unión. El marco general está en el art. 20 TUE y el detalle, en los arts. 326 a 334 TFUE. Es el bloque con más preguntas oficiales de este tema.",
  ["1 Concepto, finalidad y requisitos (art. 20 TUE) y su origen", "2 Límites y apertura (arts. 326 a 328 TFUE)", "3 Autorización, votación y participación posterior (arts. 329 a 331 TFUE)", "4 Gastos, pasarelas y coherencia (arts. 332 a 334 TFUE)"]))

T.ap("s16", "VI.1 Concepto, finalidad y requisitos (TUE, art. 20) y su origen", f"""
{unidad("1.1 El marco general (art. 20 TUE)",
  LT(20, ["en el marco de las competencias no exclusivas de la Unión", "impulsar los objetivos de la Unión, proteger sus intereses y reforzar su proceso de integración", "abiertas permanentemente a todos los Estados miembros", "como último recurso", "en un plazo razonable", "al menos nueve Estados miembros", "únicamente participarán en la votación", "vincularán únicamente a los Estados miembros participantes", "no se considerarán acervo"]),
  fichab("Cooperación reforzada: concepto y requisitos",
         ["Los **Estados miembros** que lo deseen (mínimo **nueve**)", "Autoriza el **Consejo** (procedimiento del art. 329 TFUE, → VI.3.1)"],
         ["Solo en **competencias no exclusivas** de la Unión", "Usan las **instituciones** de la Unión y los Tratados", "Finalidad: impulsar objetivos, proteger intereses y reforzar la integración", "Abiertas **permanentemente** a todos los Estados (art. 328 TFUE)"],
         ["**Último recurso**: objetivos inalcanzables **en un plazo razonable** por la Unión en su conjunto", "Participación mínima: **nueve** Estados", "Deliberan todos los miembros del Consejo; **votan solo** los participantes (art. 330 TFUE)"],
         "**Nueve** Estados como mínimo (pregunta oficial X 29, → Cierre 1). Los actos vinculan **solo a los participantes** y **no** son acervo que deban aceptar los candidatos a la adhesión."))}

{unidad("1.2 Su origen: Ámsterdam (1997) y Niza (2001)",
  web("PE", PE3,
      "Por primera vez, los Tratados contenían disposiciones generales que permitían a un determinado número de Estados miembros recurrir, en ciertas condiciones, a las instituciones comunes para organizar una cooperación reforzada entre ellos. Esta facultad se añadió a los casos de cooperación reforzada regulada por disposiciones específicas, como la unión económica y monetaria, la creación de un espacio de libertad, seguridad y justicia, y la integración del acervo de Schengen."),
  web("PE", PE4,
      "Mientras que el Tratado de Ámsterdam preveía la cooperación reforzada en el ámbito del primer y el tercer pilar, el de Niza la extendió a los tres pilares."),
  fichab("Evolución histórica de la cooperación reforzada", "—",
         ["**Ámsterdam**: primeras disposiciones **generales** (primer y tercer pilar)", "**Niza**: extendida a los **tres** pilares", "**Lisboa**: régimen actual (art. 20 TUE y arts. 326 a 334 TFUE)"],
         "—",
         "Nace con disposiciones generales en **Ámsterdam** (→ III.2.4)."))}
""", 2)

T.ap("s17", "VI.2 Límites y apertura (TFUE, arts. 326 a 328)", f"""
{unidad("2.1 Respeto de los Tratados y del mercado interior (art. 326)",
  LF(326, ["respetarán los Tratados y el Derecho de la Unión", "no perjudicarán al mercado interior ni a la cohesión económica, social y territorial"]),
  fichab("Límites materiales de toda cooperación reforzada", "Los Estados participantes",
         ["Respetan los Tratados y el Derecho de la Unión", "No perjudican al **mercado interior** ni a la **cohesión** económica, social y territorial", "No obstaculizan ni discriminan los intercambios ni distorsionan la competencia"],
         "—", "Cuatro prohibiciones: obstáculo, discriminación, distorsión de la competencia y perjuicio al mercado interior o a la cohesión."))}

{unidad("2.2 Respeto a los Estados no participantes (art. 327)",
  LF(327, ["respetarán las competencias, los derechos y las obligaciones de los Estados miembros que no participen en ellas", "no impedirán que las apliquen"]),
  fichab("Relación entre participantes y no participantes", "Participantes y no participantes",
         "Respeto **recíproco**: los participantes respetan a los demás; los no participantes **no impiden** su aplicación", "—",
         "Obligación en **los dos sentidos**."))}

{unidad("2.3 Apertura e información (art. 328)",
  LF(328, ["estarán abiertas a todos los Estados miembros en el momento en que se establezcan", "en cualquier otro momento", "procurarán fomentar la participación del mayor número posible de Estados miembros", "La Comisión y, en su caso, el Alto Representante de la Unión para Asuntos Exteriores y Política de Seguridad informarán periódicamente al Parlamento Europeo y al Consejo"]),
  fichab("Carácter abierto y deber de información",
         ["Abiertas a **todos** los Estados, al establecerse y en cualquier otro momento", "Informan: la **Comisión** y, en su caso, el **Alto Representante** → al **Parlamento Europeo** y al **Consejo**"],
         ["Respetando las condiciones de participación de la decisión de autorización (y, después, los actos ya adoptados)", "La Comisión y los participantes fomentan la participación del mayor número posible"],
         "Información **periódica**",
         "Informan **la Comisión y el Alto Representante** a **el Parlamento Europeo y el Consejo** (no al Consejo Europeo): pregunta oficial X 28 (→ Cierre 1)."))}
""", 2)

T.ap("s18", "VI.3 Autorización, votación y participación posterior (TFUE, arts. 329 a 331)", f"""
{unidad("3.1 Autorización (art. 329)",
  LF(329, ["con excepción de los ámbitos de competencia exclusiva y de la política exterior y de seguridad común", "dirigirán a la Comisión una solicitud", "la Comisión comunicará los motivos", "será concedida por el Consejo a propuesta de la Comisión y previa aprobación del Parlamento Europeo", "en el marco de la política exterior y de seguridad común se dirigirá al Consejo", "a título informativo", "que se pronunciará por unanimidad"]),
  fichab("Cómo se autoriza una cooperación reforzada",
         ["**Régimen general**: solicitud a la **Comisión** → propuesta de la Comisión → autoriza el **Consejo** con **aprobación del PE**", "**PESC**: solicitud al **Consejo** → dictámenes del Alto Representante y de la Comisión; el PE, solo **informado** → autoriza el **Consejo**"],
         ["La solicitud precisa ámbito de aplicación y objetivos", "Si la Comisión no presenta propuesta, comunica los motivos a los Estados interesados"],
         ["Régimen general: autoriza el Consejo, previa **aprobación** del PE", "PESC: **unanimidad** del Consejo"],
         "Fuera de PESC, la solicitud va a la **Comisión**; en PESC, al **Consejo**. Excluidas las competencias **exclusivas** (en PESC hay régimen propio)."))}

{unidad("3.2 Votación en el Consejo (art. 330)",
  LF(330, ["únicamente participarán en la votación los miembros del Consejo que representen a los Estados miembros que participan", "únicamente por los votos de los representantes de los Estados miembros participantes", "apartado 3 del artículo 238"]),
  fichab("Quién vota en el marco de una cooperación reforzada", "Deliberan **todos** los miembros del Consejo; votan **solo** los participantes",
         "—",
         ["Unanimidad: solo los votos de los participantes", "Mayoría cualificada: art. 238.3 TFUE"],
         "Todos **deliberan**, solo los participantes **votan**."))}

{unidad("3.3 Incorporación posterior de un Estado (art. 331)",
  LF(331, ["lo notificará al Consejo y a la Comisión", "en un plazo de cuatro meses", "podrá someter la cuestión al Consejo", "lo notificará al Consejo, al Alto Representante de la Unión para Asuntos Exteriores y Política de Seguridad y a la Comisión", "El Consejo confirmará la participación", "el Consejo se pronunciará por unanimidad"]),
  fichab("Cómo se une un Estado a una cooperación reforzada ya existente",
         ["Régimen general: confirma la **Comisión**; si se deniega dos veces, el Estado puede acudir al **Consejo**", "PESC: confirma el **Consejo**, previa consulta al Alto Representante"],
         ["Notificación (régimen general: al Consejo y a la Comisión; PESC: además al Alto Representante)", "Medidas transitorias para aplicar los actos ya adoptados"],
         ["Comisión: **cuatro meses** desde la notificación", "PESC: **unanimidad** del Consejo (art. 330)"],
         "En el régimen general confirma la **Comisión** en **4 meses**; en PESC, el **Consejo** por **unanimidad**."))}
""", 2)

T.ap("s19", "VI.4 Gastos, pasarelas y coherencia (TFUE, arts. 332 a 334)", f"""
{unidad("4.1 Gastos (art. 332)",
  LF(332, ["serán sufragados por los Estados miembros participantes", "por unanimidad de todos sus miembros y previa consulta al Parlamento Europeo"]),
  fichab("Financiación de la cooperación reforzada", "Los Estados participantes (salvo decisión del Consejo)",
         "Los gastos que no sean administrativos de las instituciones los pagan los **participantes**",
         "Excepción: **unanimidad de todos** los miembros del Consejo, previa consulta al PE",
         "Para cambiar quién paga, unanimidad de **todos** los miembros del Consejo (no solo de los participantes)."))}

{unidad("4.2 Cláusulas pasarela propias (art. 333)",
  LF(333, ["éste podrá adoptar por unanimidad", "que se pronunciará por mayoría cualificada", "con arreglo al procedimiento legislativo ordinario", "no se aplicarán a las decisiones que tengan repercusiones militares o en el ámbito de la defensa"]),
  fichab("Cambio de regla de votación o de procedimiento dentro de la cooperación reforzada",
         "El Consejo (votan los participantes, art. 330)",
         ["De **unanimidad** a **mayoría cualificada** (333.1)", "De procedimiento legislativo **especial** a **ordinario**, previa consulta al PE (333.2)"],
         "**Unanimidad** (de los participantes) para adoptar la decisión de cambio",
         "No vale para decisiones con repercusiones **militares o de defensa** (333.3), igual que la pasarela general del art. 48.7 TUE (→ III.4.2)."))}

{unidad("4.3 Coherencia (art. 334)",
  LF(334, ["El Consejo y la Comisión velarán por la coherencia"]),
  fichab("Coherencia de la cooperación reforzada con las políticas de la Unión", "El **Consejo** y la **Comisión**", "Velan por la coherencia y cooperan a tal efecto", "—",
         "Velan **Consejo y Comisión** (no el Parlamento ni el Alto Representante)."))}

{unidad("4.4 Cuadro: régimen general y PESC (esquema)",
  ESQ,
  TAB4)}

{resumen([
  "Cooperación reforzada (art. 20 TUE): solo en **competencias no exclusivas**, como **último recurso**, con **al menos nueve** Estados; abierta permanentemente; sus actos vinculan **solo a los participantes**.",
  "Límites (326-327): respetar Tratados, mercado interior y cohesión, y a los no participantes. Informan **Comisión y Alto Representante** al **PE y al Consejo** (328.2).",
  "Autorización (329): régimen general, solicitud a la **Comisión** y aprobación del **PE**; PESC, solicitud al **Consejo** y **unanimidad**. Votan solo los participantes (330).",
  "Gastos para los participantes salvo unanimidad de todos (332); pasarelas propias sin efectos militares (333); coherencia: Consejo y Comisión (334)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_L18 = examen_web("L", 18, {
  "a": f"El Tratado de Roma se firmó el **25 de marzo de 1957**: {cw(PE1, 'firmados el 25 de marzo de 1957')}. No es el 9 de mayo.",
  "b": f"El 9 de mayo recuerda el discurso de Schuman de 1950: {cw(DIA, 'Conocida como la Declaración Schuman')}.",
  "c": f"La primera ampliación fue el **1 de enero de 1973**: {cw(PE2, 'El 1 de enero de 1973 tuvo lugar la adhesión del Reino Unido, así como de Dinamarca e Irlanda')}.",
  "d": f"El Día de Europa no conmemora Schengen: recuerda que {cw(DIA, 'El 9 de mayo de 1950, el ministro francés de Asuntos Exteriores, Robert Schuman, pronunció un discurso histórico')}."},
  [("Declaración Schuman", DIA, "Conocida como la Declaración Schuman")])
EX_P9 = examen("P", 9, {
  "a": f"La Comisión solo es **consultada**; quien decide es el Consejo: {cT(49, 'después de haber consultado a la Comisión')}.",
  "b": f"Literal del art. 49: {cT(49, 'dirigirá su solicitud al Consejo, que se pronunciará por unanimidad')}.",
  "c": f"El Parlamento Europeo da su **aprobación** {cT(49, 'por mayoría de los miembros que lo componen')}, pero la solicitud no se le dirige: solo {cT(49, 'Se informará de esta solicitud al Parlamento Europeo')}.",
  "d": "El Banco Central Europeo no interviene en el procedimiento de adhesión del art. 49."},
  [("Al Consejo, que se pronunciará por unanimidad", "TUE", "Artículo 49", "dirigirá su solicitud al Consejo, que se pronunciará por unanimidad")])
EX_X28 = examen("X", 28, {
  "a": f"Cambia quién informa y a quién: informan {cF(328, 'La Comisión y, en su caso, el Alto Representante')}, no el Parlamento Europeo.",
  "b": "Cambia quién informa: no es el Consejo, que es destinatario de la información junto con el Parlamento Europeo.",
  "c": f"Literal del art. 328.2: {cF(328, 'La Comisión y, en su caso, el Alto Representante de la Unión para Asuntos Exteriores y Política de Seguridad informarán periódicamente al Parlamento Europeo y al Consejo')}.",
  "d": "Cambia el segundo informante (el Consejo en vez del Alto Representante) y los destinatarios (Consejo Europeo en vez de Consejo)."},
  [("La Comisión y, en su caso, el Alto Representante de la Unión para Asuntos Exteriores y Política de Seguridad informarán periódicamente al Parlamento Europeo y al Consejo", "TFUE", "Artículo 328", "La Comisión y, en su caso, el Alto Representante de la Unión para Asuntos Exteriores y Política de Seguridad informarán periódicamente al Parlamento Europeo y al Consejo")])
EX_X29 = examen("X", 29, {
  "a": f"No en cualquier ámbito: el art. 329.1 TFUE exceptúa {cF(329, 'los ámbitos de competencia exclusiva')} (y el art. 20.1 TUE habla de {cT(20, 'competencias no exclusivas')}).",
  "b": f"La solicitud no va al Consejo Europeo: en el régimen general {cF(329, 'dirigirán a la Comisión una solicitud')}.",
  "c": f"Es al revés: en PESC la solicitud {cF(329, 'se dirigirá al Consejo')}.",
  "d": f"Literal del art. 20.2 TUE: {cT(20, 'a condición de que participen en ella al menos nueve Estados miembros')}."},
  [("al menos nueve Estados miembros", "TUE", "Artículo 20", "a condición de que participen en ella al menos nueve Estados miembros")])
EX_X30 = examen("X", 30, {
  "a": f"Literal del art. 48.2 TUE: {cT(48, 'El Gobierno de cualquier Estado miembro, el Parlamento Europeo o la Comisión podrán presentar al Consejo proyectos de revisión de los Tratados')}.",
  "b": f"El Consejo Europeo no presenta los proyectos: los recibe del Consejo ({cT(48, 'El Consejo remitirá dichos proyectos al Consejo Europeo')}).",
  "c": "El Consejo tampoco es titular de la iniciativa: es quien recibe los proyectos (art. 48.2). Y falta el Gobierno de cualquier Estado miembro.",
  "d": f"El Banco Central Europeo solo es **consultado** {cT(48, 'Cuando se trate de modificaciones institucionales en el ámbito monetario')} (48.3); no presenta proyectos."},
  [("El Gobierno de cualquier Estado miembro, el Parlamento Europeo o la Comisión", "TUE", "Artículo 48", "El Gobierno de cualquier Estado miembro, el Parlamento Europeo o la Comisión podrán presentar al Consejo proyectos de revisión de los Tratados")])
EX_X34 = examen("X", 34, {
  "a": "El art. 5.2 no limita la acción de la Unión a «acuerdos» de los Estados, sino a las competencias que le atribuyen **en los Tratados**.",
  "b": f"Literal del art. 5.2: {cT(5, 'la Unión actúa dentro de los límites de las competencias que le atribuyen los Estados miembros en los Tratados')} y {cT(5, 'Toda competencia no atribuida a la Unión en los Tratados corresponde a los Estados miembros')}.",
  "c": "Describe un conflicto entre normas (primacía), que no es lo que regula el principio de atribución del art. 5.2 (la primacía se estudia en el tema II.4).",
  "d": f"Es el principio de **subsidiariedad** (art. 5.3: {cT(5, 'En virtud del principio de subsidiariedad, en los ámbitos que no sean de su competencia exclusiva')}), no el de atribución."},
  [("las competencias que le atribuyen los Estados miembros en los Tratados", "TUE", "Artículo 5", "la Unión actúa dentro de los límites de las competencias que le atribuyen los Estados miembros en los Tratados")])
EX_X36 = examen("X", 36, {
  "a": "Ni la cooperación ni la equidad en la distribución de recursos son principios del art. 5 TUE.",
  "b": "El desarrollo sostenible es un objetivo (art. 3.3) y la cooperación leal está en el art. 4.3, no en el art. 5.",
  "c": "La igualdad y la solidaridad aparecen entre los valores y rasgos de la sociedad del art. 2, no como principios del ejercicio de las competencias.",
  "d": f"Literal del art. 5.1: {cT(5, 'El ejercicio de las competencias de la Unión se rige por los principios de subsidiariedad y proporcionalidad')}."},
  [("Subsidiariedad y proporcionalidad", "TUE", "Artículo 5", "se rige por los principios de subsidiariedad y proporcionalidad")])

T.ap("s20", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **cinco** preguntas de este tema con respuesta coherente con la fuente (cuatro de cooperaciones reforzadas, revisión y ampliación; una del Día de Europa) y **dos** relacionadas (principios del art. 5 TUE). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto del Tratado o, en la del Día de Europa, contra la fuente oficial citada.",
  "### GACE-L 2025, pregunta 18 · Día de Europa (→ I.1.2)", EX_L18,
  "### GACE-P 2025, pregunta 9 · Solicitud de adhesión (→ V.1.1)", EX_P9,
  "### GACE-L 2025 extraordinario, pregunta 28 · Información sobre las cooperaciones reforzadas (→ VI.2.3)", EX_X28,
  "### GACE-L 2025 extraordinario, pregunta 29 · Requisitos de la cooperación reforzada (→ VI.1.1)", EX_X29,
  "### GACE-L 2025 extraordinario, pregunta 30 · Revisión ordinaria de los Tratados (→ III.4.1)", EX_X30,
  "### GACE-L 2025 extraordinario, pregunta 34 · Principio de atribución (relacionada; → II.3.2)", EX_X34,
  "### GACE-L 2025 extraordinario, pregunta 36 · Principios del ejercicio de las competencias (relacionada; → II.3.2)", EX_X36,
  "### Pregunta oficial no incluida",
  f"?> **GACE-L 2025 extraordinario, pregunta 31** («Las Comunidades Europeas pasaron a tener una única Comisión en virtud del:»). La plantilla da como correcta la a) «Tratado de Fusión del 1 de julio de 1967», pero la fuente oficial consultada fecha el Tratado de Fusión el **8 de abril de 1965** ({cw(PE2, 'el Tratado de Fusión, de 8 de abril de 1965, que fusionó los órganos ejecutivos de las tres comunidades. Entró en vigor en 1967')}), que es lo que dice la opción d). No se incluye en estos apuntes; en el test real se mantiene la respuesta de la plantilla con la marca **Discrepancia** (→ III.2.1).",
  "### Cómo se pregunta",
  "!> En cooperaciones reforzadas se cambian **órganos** (Comisión ↔ Consejo ↔ Consejo Europeo; Parlamento ↔ Alto Representante) y **números** (nueve Estados, cuatro meses). En adhesión y revisión, **quién inicia** y **quién decide** (Consejo por unanimidad; Gobierno, Parlamento o Comisión).",
]))

T.ap("s21", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Antecedentes | Declaración Schuman; carbón y acero; CED fallida; Mesina | **9 de mayo de 1950** (Día de Europa) |
| II. Naturaleza y objetivos | Tratado entre Estados; competencias atribuidas; personalidad jurídica (47); valores (2); objetivos (3); principios (5); art. 7 | **Atribución** delimita; **subsidiariedad y proporcionalidad** rigen el ejercicio |
| III. Tratados | París 1951; Roma 1957; Fusión 1965; AUE 1986; Maastricht 1992; Ámsterdam 1997; Niza 2001; Lisboa 2007 | Revisión ordinaria: iniciativa del **Gobierno de un Estado, el PE o la Comisión** |
| IV. TUE y TFUE | Mismo valor jurídico; TUE en títulos, TFUE en partes; protocolos, parte integrante | **Mismo valor jurídico** (art. 1 TUE y 1.2 TFUE) |
| V. Ampliación y retirada | Art. 49 y criterios de Copenhague; ampliaciones; art. 50 | Solicitud al **Consejo**, **unanimidad**; retirada: **2 años** |
| VI. Cooperaciones reforzadas | Art. 20 TUE; arts. 326 a 334 TFUE | **Nueve** Estados; informan **Comisión y Alto Representante** al **PE y Consejo** |

?> **Trampas frecuentes:** «la solicitud de adhesión se dirige a la **Comisión**» (va al **Consejo**, que decide por **unanimidad**); «cooperación reforzada en **cualquier** ámbito» (no en competencias **exclusivas**); «solicitud de cooperación reforzada al **Consejo Europeo**» (a la **Comisión**; en PESC, al **Consejo**); «el TUE prevalece sobre el TFUE» (tienen el **mismo valor jurídico**); «el Día de Europa conmemora el Tratado de **Roma**» (conmemora la **Declaración Schuman**); «el acuerdo de retirada lo celebra el Consejo por **unanimidad**» (por **mayoría cualificada**).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
Q = T.q
Q("TUE", "Artículo 1", "Naturaleza jurídica", "Según el artículo 1 del Tratado de la Unión Europea, el Tratado de la Unión Europea y el Tratado de Funcionamiento de la Unión Europea:",
  ["Tienen el mismo valor jurídico.", "El Tratado de la Unión Europea prevalece sobre el Tratado de Funcionamiento.", "El Tratado de Funcionamiento prevalece sobre el Tratado de la Unión Europea.", "Tienen el valor jurídico que determine el Consejo Europeo."],
  "Art. 1 TUE: «Ambos Tratados tienen el mismo valor jurídico».", "Ambos Tratados tienen el mismo valor jurídico")
Q("TUE", "Artículo 1", "Naturaleza jurídica", "Según el artículo 1 del Tratado de la Unión Europea, la Unión sustituirá y sucederá a:",
  ["La Comunidad Europea.", "La Comunidad Europea del Carbón y del Acero.", "El Consejo de Europa.", "La Comunidad Europea de la Energía Atómica."],
  "Art. 1 TUE.", "La Unión sustituirá y sucederá a la Comunidad Europea")
Q("TUE", "Artículo 1", "Naturaleza jurídica", "Según el artículo 1 del Tratado de la Unión Europea, las Altas Partes Contratantes constituyen entre sí una Unión Europea a la que:",
  ["Los Estados miembros atribuyen competencias para alcanzar sus objetivos comunes.", "Los Estados miembros ceden su soberanía para alcanzar sus objetivos comunes.", "Los ciudadanos atribuyen competencias para alcanzar objetivos comunes.", "Los Estados miembros delegan la totalidad de sus competencias legislativas."],
  "Art. 1 TUE.", "a la que los Estados miembros atribuyen competencias para alcanzar sus objetivos comunes")
Q("TUE", "Artículo 47", "Naturaleza jurídica", "Según el artículo 47 del Tratado de la Unión Europea:",
  ["La Unión tiene personalidad jurídica.", "La Unión carece de personalidad jurídica propia.", "Solo la Comunidad Europea de la Energía Atómica tiene personalidad jurídica.", "La personalidad jurídica corresponde al Consejo Europeo."],
  "Art. 47 TUE.", "La Unión tiene personalidad jurídica")
Q("TUE", "Artículo 2", "Valores y objetivos", "¿Cuál de los siguientes figura entre los valores en que se fundamenta la Unión según el artículo 2 del Tratado de la Unión Europea?",
  ["El Estado de Derecho.", "La economía social de mercado.", "La estabilidad de los precios.", "El pleno empleo."],
  "Art. 2 TUE: dignidad humana, libertad, democracia, igualdad, Estado de Derecho y respeto de los derechos humanos. Las demás opciones aparecen en el art. 3.3 como objetivos.", "democracia, igualdad, Estado de Derecho")
Q("TUE", "Artículo 3", "Valores y objetivos", "Según el artículo 3.1 del Tratado de la Unión Europea, la Unión tiene como finalidad promover:",
  ["La paz, sus valores y el bienestar de sus pueblos.", "El mercado interior, la competencia y el empleo.", "La seguridad, la defensa y la libertad de sus ciudadanos.", "La unión económica y monetaria y la estabilidad de los precios."],
  "Art. 3.1 TUE.", "La Unión tiene como finalidad promover la paz, sus valores y el bienestar de sus pueblos")
Q("TUE", "Artículo 3", "Valores y objetivos", "Según el artículo 3.4 del Tratado de la Unión Europea, la Unión establecerá:",
  ["Una unión económica y monetaria cuya moneda es el euro.", "Una unión aduanera con moneda única para todos los Estados miembros.", "Un sistema monetario europeo basado en el ecu.", "Una unión bancaria con un Tesoro común."],
  "Art. 3.4 TUE.", "La Unión establecerá una unión económica y monetaria cuya moneda es el euro")
Q("TUE", "Artículo 3", "Valores y objetivos", "Según el artículo 3.6 del Tratado de la Unión Europea, la Unión perseguirá sus objetivos por los medios apropiados:",
  ["De acuerdo con las competencias que se le atribuyen en los Tratados.", "Con independencia de las competencias atribuidas, si así lo exigen los objetivos.", "De acuerdo con lo que decida el Consejo Europeo por mayoría simple.", "De acuerdo con las competencias que le delegue cada Estado miembro por ley."],
  "Art. 3.6 TUE.", "de acuerdo con las competencias que se le atribuyen en los Tratados")
Q("TUE", "Artículo 4", "Principios", "Según el artículo 4.2 del Tratado de la Unión Europea, la seguridad nacional:",
  ["Seguirá siendo responsabilidad exclusiva de cada Estado miembro.", "Es una competencia compartida entre la Unión y los Estados miembros.", "Es una competencia exclusiva de la Unión.", "Corresponde al Alto Representante de la Unión."],
  "Art. 4.2 TUE.", "la seguridad nacional seguirá siendo responsabilidad exclusiva de cada Estado miembro")
Q("TUE", "Artículo 4", "Principios", "Según el artículo 4.3 del Tratado de la Unión Europea, la Unión y los Estados miembros se respetarán y asistirán mutuamente en el cumplimiento de las misiones derivadas de los Tratados conforme al principio de:",
  ["Cooperación leal.", "Subsidiariedad.", "Proporcionalidad.", "Atribución."],
  "Art. 4.3 TUE.", "Conforme al principio de cooperación leal, la Unión y los Estados miembros se respetarán y asistirán mutuamente")
Q("TUE", "Artículo 5", "Principios", "Según el artículo 5.1 del Tratado de la Unión Europea, la delimitación de las competencias de la Unión se rige por el principio de:",
  ["Atribución.", "Subsidiariedad.", "Proporcionalidad.", "Cooperación leal."],
  "Art. 5.1 TUE: la delimitación, por atribución; el ejercicio, por subsidiariedad y proporcionalidad.", "La delimitación de las competencias de la Unión se rige por el principio de atribución")
Q("TUE", "Artículo 5", "Principios", "Según el artículo 5.3 del Tratado de la Unión Europea, el principio de subsidiariedad se aplica:",
  ["En los ámbitos que no sean de competencia exclusiva de la Unión.", "En todos los ámbitos de competencia de la Unión.", "Solo en los ámbitos de competencia exclusiva de la Unión.", "Solo en la política exterior y de seguridad común."],
  "Art. 5.3 TUE.", "en los ámbitos que no sean de su competencia exclusiva")
Q("TUE", "Artículo 5", "Principios", "Según el artículo 5.3 del Tratado de la Unión Europea, ¿quiénes velarán por el respeto del principio de subsidiariedad con arreglo al procedimiento establecido en el Protocolo correspondiente?",
  ["Los Parlamentos nacionales.", "El Tribunal de Cuentas.", "Los Gobiernos regionales.", "El Comité Económico y Social."],
  "Art. 5.3 TUE, párrafo segundo.", "Los Parlamentos nacionales velarán por el respeto del principio de subsidiariedad")
Q("TUE", "Artículo 5", "Principios", "Según el artículo 5.4 del Tratado de la Unión Europea, en virtud del principio de proporcionalidad:",
  ["El contenido y la forma de la acción de la Unión no excederán de lo necesario para alcanzar los objetivos de los Tratados.", "La Unión solo actuará en los ámbitos de su competencia exclusiva.", "Toda competencia no atribuida a la Unión corresponde a los Estados miembros.", "La Unión intervendrá solo si los Estados miembros no pueden alcanzar los objetivos de manera suficiente."],
  "Art. 5.4 TUE. La c) es la atribución (5.2) y la d), la subsidiariedad (5.3).", "el contenido y la forma de la acción de la Unión no excederán de lo necesario para alcanzar los objetivos de los Tratados")
Q("TUE", "Artículo 6", "Derechos fundamentales", "Según el artículo 6.1 del Tratado de la Unión Europea, la Carta de los Derechos Fundamentales de la Unión Europea tendrá:",
  ["El mismo valor jurídico que los Tratados.", "Un valor meramente declarativo.", "Un valor inferior a los Tratados y superior al Derecho derivado.", "El valor que le atribuya cada Estado miembro."],
  "Art. 6.1 TUE.", "la cual tendrá el mismo valor jurídico que los Tratados")
Q("TUE", "Artículo 7", "Defensa de los valores", "Según el artículo 7.1 del Tratado de la Unión Europea, el Consejo podrá constatar la existencia de un riesgo claro de violación grave por un Estado miembro de los valores del artículo 2 por mayoría de:",
  ["Cuatro quintos de sus miembros, previa aprobación del Parlamento Europeo.", "Dos tercios de sus miembros, previa consulta al Parlamento Europeo.", "Unanimidad, previa aprobación de la Comisión.", "Mayoría cualificada, previo dictamen del Tribunal de Justicia."],
  "Art. 7.1 TUE.", "por mayoría de cuatro quintos de sus miembros y previa aprobación del Parlamento Europeo")
Q("TUE", "Artículo 7", "Defensa de los valores", "Según el artículo 7.2 del Tratado de la Unión Europea, la existencia de una violación grave y persistente de los valores del artículo 2 la constata:",
  ["El Consejo Europeo, por unanimidad.", "El Consejo, por mayoría cualificada.", "El Parlamento Europeo, por mayoría de dos tercios.", "La Comisión, previa audiencia del Estado."],
  "Art. 7.2 TUE.", "El Consejo Europeo, por unanimidad")
Q("TUE", "Artículo 7", "Defensa de los valores", "Según el artículo 7.3 del Tratado de la Unión Europea, constatada una violación grave y persistente, el Consejo podrá suspender determinados derechos del Estado miembro, incluidos los derechos de voto, decidiendo por:",
  ["Mayoría cualificada.", "Unanimidad.", "Mayoría de cuatro quintos.", "Mayoría simple."],
  "Art. 7.3 TUE.", "el Consejo podrá decidir, por mayoría cualificada, que se suspendan determinados derechos")
Q("TUE", "Artículo 48", "Revisión de los Tratados", "Según el artículo 48.3 del Tratado de la Unión Europea, la Convención examinará los proyectos de revisión y adoptará una recomendación:",
  ["Por consenso.", "Por mayoría simple.", "Por mayoría cualificada.", "Por mayoría de dos tercios."],
  "Art. 48.3 TUE.", "adoptará por consenso una recomendación")
Q("TUE", "Artículo 48", "Revisión de los Tratados", "Según el artículo 48.3 del Tratado de la Unión Europea, la decisión del Consejo Europeo favorable al examen de las modificaciones propuestas se adopta:",
  ["Por mayoría simple, previa consulta al Parlamento Europeo y a la Comisión.", "Por unanimidad, previa aprobación del Parlamento Europeo.", "Por mayoría cualificada, a propuesta de la Comisión.", "Por mayoría de cuatro quintos, previa consulta al Banco Central Europeo."],
  "Art. 48.3 TUE.", "previa consulta al Parlamento Europeo y a la Comisión, adopta por mayoría simple una decisión favorable")
Q("TUE", "Artículo 48", "Revisión de los Tratados", "Según el artículo 48.4 del Tratado de la Unión Europea, las modificaciones de los Tratados entrarán en vigor:",
  ["Después de haber sido ratificadas por todos los Estados miembros de conformidad con sus respectivas normas constitucionales.", "Tras su aprobación por el Parlamento Europeo por mayoría absoluta.", "Cuando las ratifiquen las cuatro quintas partes de los Estados miembros.", "A los veinte días de su publicación en el Diario Oficial de la Unión Europea."],
  "Art. 48.4 TUE. Las cuatro quintas partes solo cuentan, a los dos años, para que el Consejo Europeo examine la cuestión (48.5).", "Las modificaciones entrarán en vigor después de haber sido ratificadas por todos los Estados miembros de conformidad con sus respectivas normas constitucionales")
Q("TUE", "Artículo 48", "Revisión de los Tratados", "Según el artículo 48.6 del Tratado de la Unión Europea, el procedimiento de revisión simplificado permite modificar la totalidad o parte de las disposiciones de:",
  ["La tercera parte del Tratado de Funcionamiento de la Unión Europea.", "El título III del Tratado de la Unión Europea, sobre las instituciones.", "La primera parte del Tratado de Funcionamiento de la Unión Europea.", "El título V del Tratado de la Unión Europea, sobre la acción exterior."],
  "Art. 48.6 TUE: tercera parte del TFUE (políticas y acciones internas).", "proyectos de revisión de la totalidad o parte de las disposiciones de la tercera parte del Tratado de Funcionamiento de la Unión Europea")
Q("TUE", "Artículo 48", "Revisión de los Tratados", "Según el artículo 48.7 del Tratado de la Unión Europea, en caso de oposición de un Parlamento nacional a una iniciativa de «pasarela» del Consejo Europeo, notificada en el plazo de:",
  ["Seis meses, no se adoptará la decisión.", "Dos meses, no se adoptará la decisión.", "Seis meses, la decisión se adoptará por mayoría cualificada.", "Tres meses, decidirá el Parlamento Europeo."],
  "Art. 48.7 TUE.", "En caso de oposición de un Parlamento nacional notificada en un plazo de seis meses a partir de esta transmisión, no se adoptará la decisión")
Q("TUE", "Artículo 49", "Ampliación", "Según el artículo 49 del Tratado de la Unión Europea, el Parlamento Europeo, antes de que el Consejo se pronuncie sobre una solicitud de adhesión, se pronunciará:",
  ["Por mayoría de los miembros que lo componen.", "Por mayoría simple de los votos emitidos.", "Por mayoría de dos tercios de los votos emitidos.", "Por unanimidad."],
  "Art. 49 TUE.", "el cual se pronunciará por mayoría de los miembros que lo componen")
Q("TUE", "Artículo 49", "Ampliación", "Según el artículo 49 del Tratado de la Unión Europea, puede solicitar el ingreso como miembro en la Unión:",
  ["Cualquier Estado europeo que respete los valores mencionados en el artículo 2 y se comprometa a promoverlos.", "Cualquier Estado que haya firmado el Convenio Europeo de Derechos Humanos.", "Cualquier Estado miembro del Consejo de Europa con economía de mercado.", "Cualquier Estado europeo invitado por el Consejo Europeo."],
  "Art. 49 TUE.", "Cualquier Estado europeo que respete los valores mencionados en el artículo 2 y se comprometa a promoverlos podrá solicitar el ingreso")
Q("TUE", "Artículo 49", "Ampliación", "Según el artículo 49 del Tratado de la Unión Europea, las condiciones de admisión y las adaptaciones de los Tratados serán objeto de:",
  ["Un acuerdo entre los Estados miembros y el Estado solicitante, sometido a la ratificación de todos los Estados contratantes.", "Una decisión del Consejo por mayoría cualificada.", "Un reglamento del Parlamento Europeo y del Consejo.", "Un acuerdo entre la Comisión y el Estado solicitante, aprobado por el Parlamento Europeo."],
  "Art. 49, párrafo segundo, TUE.", "serán objeto de un acuerdo entre los Estados miembros y el Estado solicitante")
Q("TUE", "Artículo 50", "Retirada", "Según el artículo 50.2 del Tratado de la Unión Europea, el Estado miembro que decida retirarse de la Unión notificará su intención:",
  ["Al Consejo Europeo.", "A la Comisión.", "Al Parlamento Europeo.", "Al Tribunal de Justicia de la Unión Europea."],
  "Art. 50.2 TUE.", "notificará su intención al Consejo Europeo")
Q("TUE", "Artículo 50", "Retirada", "Según el artículo 50.2 del Tratado de la Unión Europea, el acuerdo de retirada lo celebrará en nombre de la Unión:",
  ["El Consejo, por mayoría cualificada, previa aprobación del Parlamento Europeo.", "El Consejo Europeo, por unanimidad, previa consulta al Parlamento Europeo.", "La Comisión, previa aprobación del Consejo.", "El Parlamento Europeo, por mayoría absoluta."],
  "Art. 50.2 TUE.", "El Consejo lo celebrará en nombre de la Unión por mayoría cualificada, previa aprobación del Parlamento Europeo")
Q("TUE", "Artículo 50", "Retirada", "Según el artículo 50.3 del Tratado de la Unión Europea, a falta de acuerdo de retirada, los Tratados dejarán de aplicarse al Estado de que se trate:",
  ["A los dos años de la notificación, salvo prórroga decidida por unanimidad por el Consejo Europeo de acuerdo con dicho Estado.", "Al año de la notificación, salvo prórroga decidida por mayoría cualificada.", "A los dos años de la notificación, sin posibilidad de prórroga.", "A los seis meses de la notificación."],
  "Art. 50.3 TUE.", "a los dos años de la notificación a que se refiere el apartado 2, salvo si el Consejo Europeo, de acuerdo con dicho Estado, decide por unanimidad prorrogar dicho plazo")
Q("TUE", "Artículo 51", "TUE y TFUE", "Según el artículo 51 del Tratado de la Unión Europea, los Protocolos y Anexos de los Tratados:",
  ["Forman parte integrante de los mismos.", "Tienen un valor meramente interpretativo.", "Tienen rango de Derecho derivado.", "Solo vinculan a los Estados que los ratifiquen expresamente."],
  "Art. 51 TUE.", "Los Protocolos y Anexos de los Tratados forman parte integrante de los mismos")
Q("TUE", "Artículo 53", "TUE y TFUE", "Según el artículo 53 del Tratado de la Unión Europea, el Tratado se concluye:",
  ["Por un período de tiempo ilimitado.", "Por un período de cincuenta años.", "Por un período de diez años prorrogable.", "Hasta la entrada en vigor de una Constitución europea."],
  "Art. 53 TUE. Los cincuenta años eran del Tratado CECA.", "El presente Tratado se concluye por un período de tiempo ilimitado")
Q("TFUE", "Artículo 1", "TUE y TFUE", "Según el artículo 1.1 del Tratado de Funcionamiento de la Unión Europea, este Tratado:",
  ["Organiza el funcionamiento de la Unión y determina los ámbitos, la delimitación y las condiciones de ejercicio de sus competencias.", "Establece los valores y objetivos de la Unión.", "Regula la adhesión y la retirada de los Estados miembros.", "Crea la Unión Europea y le atribuye personalidad jurídica."],
  "Art. 1.1 TFUE. Las demás son contenido del TUE (arts. 2, 3, 47, 49 y 50).", "El presente Tratado organiza el funcionamiento de la Unión y determina los ámbitos, la delimitación y las condiciones de ejercicio de sus competencias")
Q("LO1_2008", "a1", "Tratados", "Según el artículo 1 de la Ley Orgánica 1/2008, el Tratado de Lisboa se firmó en la capital de la República de Portugal el:",
  ["13 de diciembre de 2007.", "1 de diciembre de 2009.", "18 de junio de 2004.", "7 de febrero de 1992."],
  "Art. 1 LO 1/2008. El 1-12-2009 es su entrada en vigor; el 18-6-2004, la aprobación de la Constitución europea; el 7-2-1992, la firma de Maastricht.", "firmado en la capital de la República de Portugal el 13 de diciembre de 2007")
Q("TUE", "Artículo 20", "Cooperaciones reforzadas", "Según el artículo 20.1 del Tratado de la Unión Europea, los Estados miembros pueden instaurar entre sí una cooperación reforzada:",
  ["En el marco de las competencias no exclusivas de la Unión.", "En el marco de las competencias exclusivas de la Unión.", "En cualquier ámbito, incluidas las competencias exclusivas.", "Solo en el ámbito de la política exterior y de seguridad común."],
  "Art. 20.1 TUE.", "en el marco de las competencias no exclusivas de la Unión")
Q("TUE", "Artículo 20", "Cooperaciones reforzadas", "Según el artículo 20.2 del Tratado de la Unión Europea, la decisión de autorizar una cooperación reforzada será adoptada por el Consejo:",
  ["Como último recurso, cuando los objetivos no puedan ser alcanzados en un plazo razonable por la Unión en su conjunto.", "Como primera opción, siempre que lo soliciten al menos nueve Estados.", "Cuando lo pida el Parlamento Europeo por mayoría absoluta.", "Cuando la Comisión considere que el mercado interior lo exige."],
  "Art. 20.2 TUE.", "como último recurso, cuando haya llegado a la conclusión de que los objetivos perseguidos por dicha cooperación no pueden ser alcanzados en un plazo razonable por la Unión en su conjunto")
Q("TUE", "Artículo 20", "Cooperaciones reforzadas", "Según el artículo 20.4 del Tratado de la Unión Europea, los actos adoptados en el marco de una cooperación reforzada:",
  ["Vincularán únicamente a los Estados miembros participantes.", "Vincularán a todos los Estados miembros.", "Formarán parte del acervo que deben aceptar los Estados candidatos.", "Solo serán vinculantes si los ratifica el Parlamento Europeo."],
  "Art. 20.4 TUE.", "Los actos adoptados en el marco de una cooperación reforzada vincularán únicamente a los Estados miembros participantes")
Q("TFUE", "Artículo 329", "Cooperaciones reforzadas", "Según el artículo 329.1 del Tratado de Funcionamiento de la Unión Europea, fuera de la política exterior y de seguridad común, la autorización para llevar a cabo una cooperación reforzada será concedida por:",
  ["El Consejo, a propuesta de la Comisión y previa aprobación del Parlamento Europeo.", "El Consejo Europeo, por unanimidad.", "La Comisión, previa consulta al Consejo.", "El Parlamento Europeo, a propuesta del Consejo."],
  "Art. 329.1 TFUE.", "será concedida por el Consejo a propuesta de la Comisión y previa aprobación del Parlamento Europeo")
Q("TFUE", "Artículo 329", "Cooperaciones reforzadas", "Según el artículo 329.2 del Tratado de Funcionamiento de la Unión Europea, la autorización de una cooperación reforzada en el marco de la política exterior y de seguridad común se concederá mediante decisión del Consejo, que se pronunciará:",
  ["Por unanimidad.", "Por mayoría cualificada.", "Por mayoría de cuatro quintos.", "Por mayoría simple."],
  "Art. 329.2 TFUE.", "se concederá mediante decisión del Consejo, que se pronunciará por unanimidad")
Q("TFUE", "Artículo 329", "Cooperaciones reforzadas", "Según el artículo 329.2 del Tratado de Funcionamiento de la Unión Europea, la solicitud de una cooperación reforzada en el marco de la política exterior y de seguridad común se transmitirá al Parlamento Europeo:",
  ["A título informativo.", "Para su aprobación por mayoría de sus miembros.", "Para que emita dictamen vinculante.", "Para que la autorice en lugar del Consejo."],
  "Art. 329.2 TFUE.", "Se transmitirá asimismo al Parlamento Europeo a título informativo")
Q("TFUE", "Artículo 330", "Cooperaciones reforzadas", "Según el artículo 330 del Tratado de Funcionamiento de la Unión Europea, en el marco de una cooperación reforzada la unanimidad estará constituida:",
  ["Únicamente por los votos de los representantes de los Estados miembros participantes.", "Por los votos de todos los miembros del Consejo.", "Por los votos de los Estados participantes y de la Comisión.", "Por los votos de todos los miembros del Consejo Europeo."],
  "Art. 330 TFUE.", "La unanimidad estará constituida únicamente por los votos de los representantes de los Estados miembros participantes")
Q("TFUE", "Artículo 331", "Cooperaciones reforzadas", "Según el artículo 331.1 del Tratado de Funcionamiento de la Unión Europea, la Comisión confirmará la participación de un Estado miembro en una cooperación reforzada ya existente en un plazo de:",
  ["Cuatro meses a partir de la recepción de la notificación.", "Dos meses a partir de la recepción de la notificación.", "Seis meses a partir de la recepción de la notificación.", "Un mes a partir de la recepción de la notificación."],
  "Art. 331.1 TFUE.", "en un plazo de cuatro meses a partir de la recepción de dicha notificación")
Q("TFUE", "Artículo 332", "Cooperaciones reforzadas", "Según el artículo 332 del Tratado de Funcionamiento de la Unión Europea, los gastos resultantes de la aplicación de una cooperación reforzada que no sean gastos administrativos de las instituciones serán sufragados:",
  ["Por los Estados miembros participantes, salvo que el Consejo decida otra cosa por unanimidad de todos sus miembros, previa consulta al Parlamento Europeo.", "Por el presupuesto de la Unión en todo caso.", "Por todos los Estados miembros en proporción a su renta nacional bruta.", "Por los Estados miembros participantes, salvo que la Comisión decida otra cosa."],
  "Art. 332 TFUE.", "serán sufragados por los Estados miembros participantes, a menos que el Consejo, por unanimidad de todos sus miembros y previa consulta al Parlamento Europeo, decida otra cosa")
Q("TFUE", "Artículo 333", "Cooperaciones reforzadas", "Según el artículo 333.3 del Tratado de Funcionamiento de la Unión Europea, las «pasarelas» de los apartados 1 y 2 de ese artículo no se aplicarán a las decisiones:",
  ["Que tengan repercusiones militares o en el ámbito de la defensa.", "Que afecten al mercado interior.", "Que se refieran a la cohesión económica, social y territorial.", "Que tengan repercusiones presupuestarias."],
  "Art. 333.3 TFUE.", "no se aplicarán a las decisiones que tengan repercusiones militares o en el ámbito de la defensa")
Q("TFUE", "Artículo 334", "Cooperaciones reforzadas", "Según el artículo 334 del Tratado de Funcionamiento de la Unión Europea, ¿quiénes velarán por la coherencia de las acciones emprendidas en el marco de una cooperación reforzada?",
  ["El Consejo y la Comisión.", "El Parlamento Europeo y el Consejo.", "El Consejo Europeo y el Alto Representante.", "La Comisión y el Tribunal de Justicia."],
  "Art. 334 TFUE.", "El Consejo y la Comisión velarán por la coherencia")
Q("TFUE", "Artículo 326", "Cooperaciones reforzadas", "Según el artículo 326 del Tratado de Funcionamiento de la Unión Europea, las cooperaciones reforzadas no perjudicarán:",
  ["Al mercado interior ni a la cohesión económica, social y territorial.", "A la política exterior y de seguridad común ni a la defensa.", "A las competencias de las regiones ni de los entes locales.", "Al presupuesto de la Unión ni a sus recursos propios."],
  "Art. 326 TFUE.", "no perjudicarán al mercado interior ni a la cohesión económica, social y territorial")

T.real("L", 18, "Antecedentes"); T.real("P", 9, "Ampliación"); T.real("X", 28, "Cooperaciones reforzadas"); T.real("X", 29, "Cooperaciones reforzadas")
T.real("X", 30, "Revisión de los Tratados"); T.real("X", 34, "Principios"); T.real("X", 36, "Principios")

# Flashcards
for q_, a_, cat in [
  ("¿Qué conmemora el Día de Europa (9 de mayo)?", "La Declaración Schuman, de 9 de mayo de 1950 (portal de la Unión Europea).", "Antecedentes"),
  ("¿Qué se puso en común con el Tratado de París y entre cuántos países?", "El carbón y el acero, entre seis países: Bélgica, Francia, Alemania, Italia, Luxemburgo y Países Bajos (ficha 1.1.1 del PE).", "Antecedentes"),
  ("¿Por qué fracasó la Comunidad Europea de Defensa?", "Porque la Asamblea Nacional francesa no autorizó su ratificación (30-8-1954) (ficha 1.1.1 del PE).", "Antecedentes"),
  ("Tratado CECA: firma, entrada en vigor y duración", "18-4-1951; 23-7-1952; 50 años (expiró el 23-7-2002) (ficha 1.1.1 del PE).", "Tratados"),
  ("Tratados de Roma: qué crean y cuándo", "CEE y Euratom; firmados el 25-3-1957, en vigor el 1-1-1958, por tiempo indefinido (ficha 1.1.1 del PE).", "Tratados"),
  ("¿Qué hizo el Tratado de Fusión y cuándo se firmó?", "Un único Consejo y una única Comisión para las tres Comunidades; 8-4-1965, en vigor en 1967 (fichas 1.1.1 y 1.1.2 del PE).", "Tratados"),
  ("Acta Única Europea: entrada en vigor y objetivo principal", "1-7-1987; mercado interior plenamente operativo el 1-1-1993 (ficha 1.1.2 del PE).", "Tratados"),
  ("Tratado de Maastricht: firma, entrada en vigor y estructura", "7-2-1992; 1-11-1993; tres pilares: Comunidades Europeas, PESC y justicia y asuntos de interior (ficha 1.1.3 del PE).", "Tratados"),
  ("Tratado de Lisboa: firma y entrada en vigor", "13-12-2007 (LO 1/2008, art. 1); en vigor el 1-12-2009 (ficha 1.1.5 del PE).", "Tratados"),
  ("¿Qué valor jurídico tienen el TUE y el TFUE?", "El mismo (art. 1 TUE y art. 1.2 TFUE).", "TUE y TFUE"),
  ("Valores de la Unión (art. 2 TUE)", "Dignidad humana, libertad, democracia, igualdad, Estado de Derecho y respeto de los derechos humanos (incluidas las minorías).", "Valores y objetivos"),
  ("Atribución, subsidiariedad y proporcionalidad (art. 5 TUE)", "La atribución rige la delimitación de competencias; la subsidiariedad y la proporcionalidad, su ejercicio.", "Principios"),
  ("Art. 7 TUE: mayorías", "Riesgo claro: Consejo, 4/5 + aprobación del PE. Violación grave y persistente: Consejo Europeo, unanimidad + aprobación del PE. Suspensión de derechos: Consejo, mayoría cualificada.", "Defensa de los valores"),
  ("Revisión ordinaria (art. 48 TUE): ¿quién puede presentar proyectos?", "El Gobierno de cualquier Estado miembro, el Parlamento Europeo o la Comisión, al Consejo.", "Revisión de los Tratados"),
  ("Adhesión (art. 49 TUE): ¿a quién se dirige la solicitud y cómo decide?", "Al Consejo, que decide por unanimidad, tras consultar a la Comisión y con aprobación del PE (mayoría de sus miembros).", "Ampliación"),
  ("Criterios de Copenhague", "Consejo Europeo de 1993: instituciones estables (democracia, Estado de Derecho, derechos humanos, minorías); economía de mercado viable; capacidad de asumir el acervo (ficha 5.5.1 del PE).", "Ampliación"),
  ("¿Cuándo se adhirieron España y Portugal?", "En 1986 (fichas 1.1.2 y 5.5.1 del PE).", "Ampliación"),
  ("Retirada (art. 50 TUE): notificación, acuerdo y plazo", "Notificación al Consejo Europeo; acuerdo celebrado por el Consejo por mayoría cualificada con aprobación del PE; dos años, prorrogables por unanimidad del Consejo Europeo.", "Retirada"),
  ("Cooperación reforzada: requisitos del art. 20 TUE", "Competencias no exclusivas; último recurso; al menos nueve Estados; abierta a todos; actos vinculan solo a los participantes.", "Cooperaciones reforzadas"),
  ("Cooperación reforzada: ¿a quién se dirige la solicitud?", "Régimen general: a la Comisión (autoriza el Consejo con aprobación del PE). PESC: al Consejo, que decide por unanimidad (art. 329 TFUE).", "Cooperaciones reforzadas"),
  ("Art. 328.2 TFUE: ¿quién informa sobre las cooperaciones reforzadas y a quién?", "La Comisión y, en su caso, el Alto Representante, al Parlamento Europeo y al Consejo.", "Cooperaciones reforzadas"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Declaración Schuman", "Llamamiento del ministro francés de Asuntos Exteriores Robert Schuman, el 9 de mayo de 1950, considerado el punto de partida de la Europa comunitaria (ficha 1.1.1 del PE).", "s1", "Antecedentes")
T.glos("Tratados originarios", "Los que crearon las Comunidades: Tratado de París (CECA, 1951) y Tratados de Roma (CEE y Euratom, 1957) (ficha 1.1.1 del PE).", "s7", "Tratados")
T.glos("Tratado de Fusión", "Tratado de 8 de abril de 1965 que estableció un Consejo único y una Comisión única de las Comunidades Europeas (fichas 1.1.1 y 1.1.2 del PE).", "s8", "Tratados")
T.glos("Pilares de Maastricht", "Los tres grupos de competencias de la Unión creada en Maastricht: Comunidades Europeas, PESC y cooperación en justicia y asuntos de interior (ficha 1.1.3 del PE).", "s8", "Tratados")
T.glos("Principio de atribución", "La Unión actúa dentro de los límites de las competencias que le atribuyen los Estados miembros en los Tratados; lo no atribuido corresponde a los Estados (art. 5.2 TUE).", "s5", "Principios")
T.glos("Principio de subsidiariedad", "Fuera de sus competencias exclusivas, la Unión interviene solo si los Estados no pueden alcanzar los objetivos de manera suficiente y la Unión puede hacerlo mejor (art. 5.3 TUE).", "s5", "Principios")
T.glos("Principio de proporcionalidad", "El contenido y la forma de la acción de la Unión no exceden de lo necesario para alcanzar los objetivos de los Tratados (art. 5.4 TUE).", "s5", "Principios")
T.glos("Cooperación leal", "Respeto y asistencia mutuos entre la Unión y los Estados miembros en el cumplimiento de las misiones de los Tratados (art. 4.3 TUE).", "s5", "Principios")
T.glos("Procedimiento de revisión ordinario", "Reforma de los Tratados con iniciativa de un Gobierno, del PE o de la Comisión, Convención (o mandato del Consejo Europeo), Conferencia de representantes de los Gobiernos y ratificación de todos los Estados (art. 48.2 a 5 TUE).", "s10", "Revisión de los Tratados")
T.glos("Criterios de Copenhague", "Criterios de adhesión fijados por el Consejo Europeo de Copenhague de 1993: políticos, económicos y de asunción del acervo (ficha 5.5.1 del PE).", "s13", "Ampliación")
T.glos("Acervo comunitario", "Conjunto de la legislación de la Unión que el Estado candidato debe asumir; se negocia por capítulos (ficha 5.5.1 del PE).", "s13", "Ampliación")
T.glos("Acuerdo de retirada", "Acuerdo que establece la forma de la retirada de un Estado; lo celebra el Consejo por mayoría cualificada, previa aprobación del PE (art. 50.2 TUE).", "s15", "Retirada")
T.glos("Cooperación reforzada", "Cooperación entre al menos nueve Estados en competencias no exclusivas, usando las instituciones de la Unión, autorizada como último recurso (art. 20 TUE; arts. 326 a 334 TFUE).", "s16", "Cooperaciones reforzadas")

# Cronología (fechas: fichas del Parlamento Europeo y metadatos del BOE)
T.hito("1950", "Declaración Schuman (9 de mayo de 1950)", "Punto de partida de la Europa comunitaria; hoy, Día de Europa (ficha 1.1.1 del PE; portal de la UE)", "normativo", "s1")
T.hito("1951", "Tratado de París (CECA), firmado el 18-4-1951", "En vigor el 23-7-1952; 50 años de duración (ficha 1.1.1 del PE)", "normativo", "s7")
T.hito("1957", "Tratados de Roma (CEE y Euratom), firmados el 25-3-1957", "En vigor el 1-1-1958, por tiempo indefinido (ficha 1.1.1 del PE)", "normativo", "s7")
T.hito("1986", "Adhesión de España y Portugal", "Tercera ampliación (fichas 1.1.2 y 5.5.1 del PE)", "normativo", "s14")
T.hito("1992", "Tratado de la Unión Europea, firmado en Maastricht el 7-2-1992", "Nace la Unión Europea; en vigor el 1-11-1993 (ficha 1.1.3 del PE)", "normativo", "s8")
T.hito("2007", "Tratado de Lisboa, firmado el 13-12-2007", "Ratificación autorizada por la Ley Orgánica 1/2008, de 30 de julio (BOE de 31-7-2008); en vigor el 1-12-2009 (ficha 1.1.5 del PE)", "normativo", "s9")
T.hito("2020", "Retirada del Reino Unido (31-1-2020)", "Dato de la ficha 5.5.1 del PE; la retirada se regula en el art. 50 TUE", "normativo", "s15")

T.publicar()
