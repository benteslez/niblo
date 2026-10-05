# -*- coding: utf-8 -*-
"""Reparte el contenido del módulo M101 en los TRES temas del bloque I:
   B1T01 (I.1) La Constitución: estructura, contenido y reforma
   B1T02 (I.2) Derechos y deberes fundamentales: garantía, suspensión y Defensor del Pueblo
   B1T03 (I.3) El Tribunal Constitucional

El contenido (con todo su texto literal) se escribe una sola vez en m101/part*.py y se comprueba al
ejecutarlo (lit, c, T.q). Aquí solo se reparte: qué apartado va a qué tema, su numeración y títulos,
los mapas de cada tema, las remisiones «→» entre apartados (entre temas se escriben «→ tema I.2 · III.1»)
y las preguntas, flashcards, glosario e hitos de cada uno.

    cd herramientas/oposicion && python3 temas/B1T01.py   (y B1T02.py, B1T03.py)
"""
import os, re, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
PARTES = ["part1", "part2", "part3", "part4", "part5", "part6", "part7", "part8", "part9a", "part9b", "part10", "part11"]

def _cargar():
    ns = {}
    for f in PARTES:
        p = os.path.join(AQUI, f + ".py"); ns["__file__"] = p
        exec(compile(open(p, encoding="utf-8").read(), p, "exec"), ns)
    return ns

# --------------------------------------------------------------------------- reparto de apartados
# id antiguo → (tema, código nuevo). Los apartados fusionados llevan el id del primero.
TEMA_DE = {1: "B1T01", 2: "B1T02", 3: "B1T03"}
COD_TEMA = {1: "I.1", 2: "I.2", 3: "I.3"}
# código antiguo → (tema, código nuevo): para reescribir las remisiones «→ V.1»
CODIGOS = {
 "I": (1, "I"), "II": (1, "II"), "III": (1, "III"), "IV": (2, "I"), "V": (2, "III"), "VI": (2, "IV"), "VII": (3, "I"), "VIII": (2, "V"), "IX": (1, "IV"),
 "I.1": (1, "I.1"), "I.2": (1, "I.2"), "II.1": (1, "II.1"), "II.2": (1, "II.2"), "II.3": (1, "II.3"), "II.4": (1, "II.4"), "II.5": (1, "II.4"), "II.6": (1, "II.5"),
 "III.1": (1, "III.1"), "III.2": (1, "III.2"), "III.3": (1, "III.3"), "III.4": (2, "II.1"), "III.5": (2, "II.2"), "III.6": (2, "II.3"), "III.7": (2, "II.4"),
 "IV.1": (2, "I.1"), "IV.2": (2, "I.2"), "IV.3": (2, "I.3"),
 "V.1": (2, "III.1"), "V.2": (2, "III.2"), "V.3": (2, "III.3"), "V.4": (2, "V.1"), "V.5": (2, "III.4"), "V.6": (2, "III.5"), "V.7": (2, "III.5"), "V.8": (2, "III.6"),
 "VI.1": (2, "IV.1"), "VI.2": (2, "IV.2"), "VI.3": (2, "IV.3"), "VI.4": (2, "IV.4"), "VI.5": (2, "IV.3"), "VI.6": (2, "IV.5"),
 "VII.1": (3, "I.1"), "VII.2": (3, "I.2"), "VII.3": (3, "II.1"), "VII.4": (3, "III.1"), "VII.5": (3, "II.2"), "VII.6": (3, "IV.1"),
 "VIII.1": (2, "V.1"), "VIII.2": (2, "V.1"), "VIII.3": (2, "V.2"), "VIII.4": (2, "V.2"), "VIII.5": (2, "V.3"),
 "IX.1": (1, "IV.1"), "IX.2": (1, "IV.2"), "IX.3": (1, "IV.3"), "IX.4": (1, "IV.4"), "IX.5": (1, "IV.5"),
}
ROM = r"(?:XI|X|IX|VIII|VII|VI|IV|V|I{1,3})"
RE_REM = re.compile(r"→ (" + ROM + r"(?:\.\d+)*)(?![\w.])")
def _remisiones(body, tema):
    def f(m):
        cod = m.group(1); partes = cod.split(".")
        base = ".".join(partes[:2]) if len(partes) >= 2 else cod
        suf = "." + ".".join(partes[2:]) if len(partes) > 2 else ""
        if base not in CODIGOS: return m.group(0)
        t, nuevo = CODIGOS[base]
        return "→ " + nuevo + suf if t == tema else "→ tema " + COD_TEMA[t] + " · " + nuevo + suf
    return RE_REM.sub(f, body)

def _renum(body, n):
    """Renumera los «### a.b » de un apartado a «### n.i » en orden."""
    k = [0]
    def f(m): k[0] += 1; return f"### {n}.{k[0]} "
    return re.sub(r"^### \d+\.\d+ ", f, body, flags=re.M)

def _limpia(body, titulo):
    """Sin duplicados: el mapa no repite lo que ya dice su tabla, «Qué vas a ver» repite el índice lateral y un
    apartado «Cuadro…» ya es su propio resumen."""
    body = re.sub(r"^@> \*\*▸ Qué vas a ver\.\*\*.*\n?", "", body, flags=re.M)
    if titulo == "Mapa del tema":
        body = re.sub(r"^### Qué vas a aprender\n[\s\S]*?(?=^### )", "", body, flags=re.M)
        body = re.sub(r"^\| \*\*[IVX]+\*\* \| (?:Repaso|Preguntas y repaso) \|[^\n]*\n?", "", body, flags=re.M)
    if re.match(r"^[IVX]+\.\d+ Cuadro", titulo):
        body = re.sub(r"^@> \*\*▸ En resumen\.\*\*\n(?:@> • .*\n?)*", "", body, flags=re.M)
    return body.rstrip("\n")

def generar(tema_n):
    ns = _cargar()
    Tema, donde, resumen, IMP, PRE, tag, tabla, ir, T = (ns[k] for k in ("Tema", "donde", "resumen", "IMP", "PRE", "tag", "tabla", "ir", "T"))
    S = {s["id"]: s for s in T.S}
    def cuerpo(*ids): return "\n\n".join(S[i]["body"] for i in ids)

    ap = []   # (id, título, cuerpo, nivel)
    def A(i, tit, body, nivel=2): ap.append((i, tit, body, nivel))

    if tema_n == 1:
        A("s0", "Mapa del tema", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque I, tema 1):
> La Constitución Española de 1978: estructura y contenido. La reforma de la Constitución.

Este es el **primer tema del bloque I**. El módulo M101 lo estudia junto a los otros dos (I.2: derechos, garantías, suspensión y Defensor del Pueblo; I.3: Tribunal Constitucional), pero cada uno se desarrolla por separado.

### Qué vas a aprender

- **Cuándo nace** la Constitución, **quién hace qué** en cada fecha y **cuántas veces se ha reformado**.
- **Cómo está hecha**: partes, títulos, capítulos, secciones y disposiciones. Es lo más preguntable del tema y se memoriza.
- **De qué trata cada artículo** del 1 al 55 y qué dice el Título preliminar.
- **Cómo se reforma**: los procedimientos de los arts. 167 y 168.

### El hilo del tema

| Bloque | Pregunta | Constitución | Otras normas |
|---|---|---|---|
| **I** | ¿Cuándo nace y cuándo se ha reformado? | Fórmula final, disp. final | Cuatro reformas (1992, 2011, 2024, 2026) |
| **II** | ¿Cómo está hecha? | Partes, títulos, capítulos, secciones, disposiciones | — |
| **III** | ¿De qué trata cada artículo? | Arts. 1 a 55; Título preliminar (1 a 9) | — |
| **IV** | ¿Cómo se reforma? | Título X (166 a 169); arts. 75.3, 87 y 116 | Reglamentos del Congreso y del Senado; LO 2/1980 |
| **V** | Preguntas y repaso | — | — |

### Cómo estudiarlo (módulo M101)

- **Mira siempre el epígrafe.** Estudiar «por leyes» está bien al principio, pero el programa dice qué se puede preguntar: aquí se ha quitado lo que no entra.
- La Constitución es la **única norma** en la que hay que aprender la **estructura y el contenido artículo por artículo**.
- **Lectura profunda de los artículos 1 a 55** cada vez que repases (no hace falta saberlos literalmente, sí su «música»). Se hace con el texto del botón **Constitución Española**.
- **Usa siempre el mismo material**: por eso cada título y capítulo tiene **el mismo color** en los apuntes, en la Constitución, en el organigrama y en el test.
- Primera vuelta: sabe **de qué trata cada artículo** y **dónde está**. Después, profundiza.

{ir("#/ce/texto", "📜 Constitución completa")} {ir("#/ce/organigrama", "🗺 Organigrama")} {ir("#/ce/test", "🧭 Test Constitución")}

### Las etiquetas de los apuntes

- {IMP} → lo que el módulo marca como «importante» o «atención».
- {PRE} → lo que **no hace falta** estudiar a fondo, con una nota que explica por qué.
- Los colores de los títulos y capítulos son los de la Constitución completa: {tag("P", "Título preliminar")} {tag("I", "Título I")} {tag("I.2.1", "Sección 1.ª")} {tag("III", "Título III")}…

### Avisos: lo que dice la norma prevalece sobre la guía

- **Reforma del art. 69.3.** La guía M101 la sitúa el «20 de mayo de 2026». La reforma es **de 19 de mayo de 2026** (sanción del Rey) y se publicó y entró en vigor el **20 de mayo de 2026**.
- **Reformas.** En el vídeo solo se citan las de los arts. 13.2 y 135; la guía añade la del 49 (2024) y la del 69.3 (2026): en total, **cuatro**.
- **Organigrama.** El de la guía rotula el capítulo II del Título I con «Art. 14». Aquí se sigue el texto de la CE: el capítulo II comprende los **arts. 14 a 38**.
- **Art. 42.** La guía lo titula «inmigrantes españoles en el extranjero»; el art. 42 habla de los **trabajadores españoles en el extranjero** (emigrantes): se usa el término de la norma.
""", 1)
        A("bI", "I. ¿Cuándo nace la Constitución y cuándo se ha reformado?", S["bI"]["body"], 1)
        A("s1", S["s1"]["title"], S["s1"]["body"]); A("s2", S["s2"]["title"], S["s2"]["body"])
        A("bII", "II. ¿Cómo está hecha? Estructura de la Constitución", donde(
          "Segunda pregunta. La Constitución es la **única norma** en la que hay que saber de memoria **cómo se reparten los artículos**: títulos, capítulos y secciones. Sirve de armazón para colgar después el contenido de cada artículo.",
          ["1 Las dos partes: dogmática y orgánica", "2 Los títulos y sus artículos", "3 El Título I por dentro (lo más preguntable)", "4 Capítulos de los Títulos III y VIII y disposiciones (4-9-1-1)"]), 1)
        A("s3", S["s3"]["title"], S["s3"]["body"]); A("s4", S["s4"]["title"], _remisiones(S["s4"]["body"], 1)); A("s5", S["s5"]["title"], S["s5"]["body"])
        A("s6", "II.4 Los capítulos de los Títulos III y VIII y las disposiciones (4-9-1-1)",
          "### 4.1 Los capítulos de los Títulos III y VIII\n\n" + S["s6"]["body"] + "\n\n### 4.2 Las disposiciones: 4-9-1-1\n\n" + S["s7"]["body"])
        A("s8", "II.5 Resumen de la estructura", S["s8"]["body"])
        A("bIII", "III. ¿De qué trata cada artículo? Los artículos 1 a 55", donde(
          "Tercera pregunta. La Constitución no pone título a sus artículos: los títulos que se usan para estudiar son una ayuda. Aquí tienes **de qué trata cada uno** (arts. 1 a 55) y la **lectura del Título preliminar**; los artículos 10 a 52 se leen a fondo en el tema I.2.",
          ["1 Cómo estudiar los artículos", "2 Cuadro: de qué trata cada artículo", "3 Lectura profunda del Título preliminar (arts. 1 a 9)"]), 1)
        A("s9", S["s9"]["title"], S["s9"]["body"]); A("s10", S["s10"]["title"], S["s10"]["body"]); A("s11", S["s11"]["title"], S["s11"]["body"])
        A("bIX", "IV. ¿Cómo se reforma la Constitución? Título X (arts. 166 a 169)", donde(
          "Cuarta pregunta. El **Título X** recoge **dos procedimientos**: el **ordinario o «light»** (art. 167) y el **agravado o «heavy»** (art. 168), para la revisión total o la de las partes más protegidas (la «rigidez» de la Constitución). Los Reglamentos de las Cámaras y la LO 2/1980 completan el procedimiento.",
          ["1 La iniciativa (arts. 87 y 166)", "2 El procedimiento del art. 167", "3 El procedimiento del art. 168", "4 Límites y reglas comunes", "5 Cuadro comparativo"]), 1)
        for i, n in (("s44", 1), ("s45", 2), ("s46", 3), ("s47", 4), ("s48", 5)):
            A(i, f"IV.{n}" + S[i]["title"][4:], S[i]["body"])
        A("s48b", "IV.6 Cómo no confundir las mayorías", S["s48b"]["body"])
    elif tema_n == 2:
        A("s0", "Mapa del tema", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque I, tema 2):
> Derechos y deberes fundamentales. Su garantía y suspensión. El Defensor del Pueblo.

Es el **segundo tema del bloque I** (el primero estudia la estructura de la Constitución y el tercero el Tribunal Constitucional). Se apoya en el **Título I** y en el art. 116.

### Qué vas a aprender

- Qué **niveles de protección** tienen los artículos 10 a 52: es el **cuadro** que resuelve la mayoría de las preguntas.
- Los **mecanismos de garantía**: reserva de ley, tutela ordinaria, amparo, inconstitucionalidad, Defensor del Pueblo y vinculación de los poderes públicos.
- La **suspensión** de derechos: art. 55 y estados de alarma, excepción y sitio.
- El **Defensor del Pueblo**: elección, mandato y funciones.

### El hilo del tema

| Bloque | Pregunta | Constitución | Otras normas |
|---|---|---|---|
| **I** | ¿Qué niveles de protección tienen los derechos? | Título I, arts. 10 a 52 | — |
| **II** | Lectura profunda de los arts. 10 a 52 | Arts. 10 a 52 (literales) | — |
| **III** | ¿Cómo se garantizan? | Arts. 53, 54, 81, 161 y 162 | LOTC, LJCA |
| **IV** | ¿Cómo se suspenden? | Arts. 55 y 116 | LO 4/1981 |
| **V** | El Defensor del Pueblo | Art. 54 | LO 3/1981 |
| **VI** | Repaso | — | — |

### Cómo estudiarlo (módulo M101)

- Primero **los mecanismos** (qué son), después **qué derechos cubre cada uno**: si tienes clara la estructura (tema I.1), el cuadro se deduce.
- **De qué trata cada artículo del 1 al 38 y del 53 al 55**; del 39 al 52 basta distinguirlos de los derechos.
- **El art. 55 («suspensión») es muy preguntable**: se pregunta por palabras clave y hay que dominarlo. Estudia el esquema y repásalo varias veces.
- La **lectura profunda** de los arts. 10 a 52 se hace en vueltas posteriores; no hace falta saberlos literalmente.
- {ir("#/ce/texto", "📜 Constitución completa")} {ir("#/ce/test", "🧭 Test Constitución")}

### Las etiquetas de los apuntes

- {IMP} → lo que el módulo marca como «importante» o «atención».
- {PRE} → lo que no hace falta estudiar a fondo.
- Colores: {tag("I.2.1", "Sección 1.ª")} {tag("I.2.2", "Sección 2.ª")} {tag("I.3", "Capítulo III")} {tag("I.4", "Capítulo IV")} {tag("I.5", "Capítulo V")}, los mismos de la Constitución completa.

### Avisos: lo que dice la norma prevalece sobre la guía

- **Ley de igualdad.** El vídeo dice que va «por ley orgánica». La LO 3/2007 lo es por su nombre, pero solo tienen carácter orgánico algunos preceptos (→ III.1).
- **Defensor del Pueblo (elección).** El vídeo dice que, si no se alcanzan los 3/5 en el Senado, bastaría la **mayoría simple**; la LO 3/1981 (art. 2.5) exige la **mayoría absoluta del Senado** (con 3/5 en el Congreso): prevalece la ley (→ V.1).
- **Defensor del Pueblo.** La guía anota «5 años. Reelegible»; la ley orgánica fija 5 años y **no regula** la reelección (→ V.2).
- **Capítulo II.** Comprende los arts. **14 a 38**: el art. 14 queda fuera de las dos secciones.
""", 1)
        A("bIV", "I. Derechos y deberes fundamentales: los niveles de protección", S["bIV"]["body"].replace("apartado IV.2", "apartado I.2"), 1)
        for i, n in (("s16", 1), ("s17", 2), ("s18", 3)): A(i, f"I.{n}" + S[i]["title"][4:], S[i]["body"])
        A("bLP", "II. Lectura profunda de los artículos 10 a 52", donde(
          "Segunda pregunta. Para **dominar la «música»** de cada artículo, léelos con calma, uno a uno, cada vez que repases. Tienes el **texto literal** con las palabras clave en negrita y una nota por artículo. El resto del tema te dice **qué garantiza cada nivel** y **cómo se suspenden** los derechos.",
          ["1 Art. 10 y capítulo primero (10 a 13)", "2 Art. 14 y sección 1.ª (14 a 29)", "3 Sección 2.ª (30 a 38)", "4 Capítulo tercero (39 a 52)"]), 1)
        for i, n, M in (("s12", 1, 4), ("s13", 2, 5), ("s14", 3, 6), ("s15", 4, 7)):
            A(i, f"II.{n}" + S[i]["title"][len(f"III.{M}"):], _renum(S[i]["body"], n))
        A("bV", "III. ¿Cómo se garantizan los derechos? Los mecanismos (arts. 53, 81, 161 y 162)", donde(
          "Tercera pregunta. La Constitución no se limita a reconocer los derechos: dispone **mecanismos para protegerlos**. Se estudian **en este orden**, y después se relaciona cada mecanismo con los artículos que protege (cuadro I.2).",
          ["1 Reserva de ley (orgánica y ordinaria)", "2 Tutela ante los tribunales ordinarios", "3 Recurso de amparo", "4 Recurso de inconstitucionalidad", "5 Vinculación de los poderes públicos y paradoja del capítulo III", "6 Cuadro resumen"]), 1)
        A("s19", "III.1" + S["s19"]["title"][3:], S["s19"]["body"]); A("s20", "III.2" + S["s20"]["title"][3:], S["s20"]["body"]); A("s21", "III.3" + S["s21"]["title"][3:], S["s21"]["body"])
        A("s23", "III.4" + S["s23"]["title"][3:], _renum(S["s23"]["body"], 4))
        A("s24", "III.5 Vinculación de los poderes públicos y paradoja del capítulo III", _renum(S["s24"]["body"] + "\n\n" + S["s25"]["body"], 5))
        A("s26", "III.6" + S["s26"]["title"][3:], S["s26"]["body"])
        A("bVI", "IV. ¿Cómo se suspenden los derechos? Estados de alarma, excepción y sitio (arts. 55 y 116)", S["bVI"]["body"], 1)
        A("s27", "IV.1" + S["s27"]["title"][4:], S["s27"]["body"]); A("s28", "IV.2" + S["s28"]["title"][4:], S["s28"]["body"])
        A("s29", "IV.3 Qué derechos se pueden suspender: suspensión general e individual",
          S["s29"]["body"] + "\n\n### 3.2 La suspensión individual (art. 55.2)\n\n" + S["s31"]["body"])
        A("s30", "IV.4" + S["s30"]["title"][4:], S["s30"]["body"]); A("s32", "IV.5" + S["s32"]["title"][4:], re.sub(r"Siguiente: [^*\n]+", "Siguiente: V. El Defensor del Pueblo", S["s32"]["body"]))
        A("bVIII", "V. El Defensor del Pueblo (art. 54)", donde(
          "Quinta pregunta. El Defensor del Pueblo es la **garantía institucional** de los derechos del Título I. Se estudia el art. 54 y la **LO 3/1981**: cómo se elige, cuánto dura su mandato, qué puede investigar y qué recursos puede interponer.",
          ["1 Qué es, requisitos y elección", "2 Mandato, adjuntos, estatuto y funciones", "3 Resumen"]), 1)
        A("s39", "V.1 Qué es el Defensor del Pueblo, requisitos y elección", _renum(S["s39"]["body"] + "\n\n" + S["s40"]["body"], 1))
        A("s41", "V.2 Mandato, adjuntos, estatuto y funciones", _renum(S["s41"]["body"] + "\n\n### 2.5 Funciones y actuación\n\n" + S["s42"]["body"], 2))
        A("s43", "V.3 Resumen del Defensor del Pueblo", re.sub(r"→ Siguiente: [^*\n]+", "→ Fin del tema I.2: sigue el tema I.3 (Tribunal Constitucional)", S["s43"]["body"]))
    else:
        A("s0", "Mapa del tema", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque I, tema 3):
> El Tribunal Constitucional. Organización, composición y atribuciones.

Es el **tercer tema del bloque I**. Se apoya en el **Título IX de la Constitución** (arts. 159 a 165) y en la **LO 2/1979, del Tribunal Constitucional** (LOTC). El módulo manda **leer detenidamente los arts. 159 a 165**.

### Qué vas a aprender

- **Qué es** el Tribunal Constitucional y **cómo se compone** (quién propone, mandato, requisitos, incompatibilidades).
- **Qué procesos conoce**: inconstitucionalidad, cuestión de inconstitucionalidad, amparo y conflictos.
- **Qué valor tienen sus sentencias**.

### El hilo del tema

| Bloque | Pregunta | Constitución | Otras normas |
|---|---|---|---|
| **I** | ¿Qué es y cómo se compone? | Arts. 159 y 160, 165 | LOTC arts. 1, 5, 9, 16, 18, 19 |
| **II** | ¿Qué conoce? | Arts. 161 a 163 | LOTC arts. 32, 33, 35, 41 a 46, 59 a 63, 73 a 77 |
| **III** | ¿Qué valor tienen las sentencias? | Art. 164 | LOTC arts. 38 y 39 |
| **IV** | Resumen | — | — |

### Cómo estudiarlo

- Las preguntas se centran en la **composición** (12 miembros, 4+4+2+2, 9 años), los **legitimados** de cada procedimiento, los **plazos** y los **efectos de las sentencias**.
- El **amparo** y la **inconstitucionalidad** se explican con más detalle en el tema I.2, como garantías de los derechos; aquí se estudian como competencias del Tribunal.
- {IMP} → lo que el módulo marca como importante; {PRE} → lo que no hace falta estudiar a fondo.

### Aviso

- **9 años de mandato.** El módulo los presenta como el mandato más largo de los órganos constitucionales; la LO 2/1982 (art. 30) fija también **9 años** para los Consejeros de Cuentas: es un **empate**, no un récord (→ I.3).
- La **jurisprudencia** del Tribunal Constitucional no se incluye todavía: se añadirá cuando se aporte la fuente oficial.
""", 1)
        A("bVII", "I. El Tribunal Constitucional: naturaleza y composición", donde(
          "Primera pregunta. Antes de ver qué hace el Tribunal Constitucional hay que saber **qué es** y **cómo se compone**: quién propone a sus 12 miembros, cuánto dura el mandato y quién puede serlo.",
          ["1 Qué es el Tribunal Constitucional", "2 Composición y mandato"]), 1)
        A("s33", "I.1" + S["s33"]["title"][5:], S["s33"]["body"]); A("s34", "I.2" + S["s34"]["title"][5:], S["s34"]["body"])
        A("s34b", "I.3 Claves para memorizar la composición", S["s34b"]["body"])
        A("bII", "II. ¿Qué procesos conoce el Tribunal Constitucional?", donde(
          "Segunda pregunta. El Tribunal conoce de **inconstitucionalidad**, **cuestión de inconstitucionalidad**, **amparo**, **conflictos de competencia** (de tres clases) y la **impugnación del art. 161.2** del Gobierno. Aprende **quién** los interpone, **frente a qué** y en **qué plazo**.",
          ["1 Competencias y procedimientos", "2 Recapitulación: amparo frente a inconstitucionalidad"]), 1)
        A("s35", "II.1 Competencias y procedimientos", _renum(_remisiones(S["s35"]["body"], 3), 1)); A("s37", "II.2" + S["s37"]["title"][5:], S["s37"]["body"])
        A("bIII", "III. ¿Qué valor tienen las sentencias?", donde("Tercera pregunta. Las sentencias del Tribunal Constitucional tienen un valor especial: se publican en el BOE, no tienen recurso y, en ciertos casos, tienen efectos frente a todos.", ["1 Las sentencias y sus efectos"]), 1)
        A("s36", "III.1" + S["s36"]["title"][5:], _renum(S["s36"]["body"], 1))
        A("bIV", "IV. Resumen del tema", donde("Cuarta y última parte: el resumen del Tribunal Constitucional.", ["1 Resumen"]), 1)
        A("s38", "IV.1" + S["s38"]["title"][5:], re.sub(r"\*\*→ Siguiente: [^*\n]+\*\*", "**→ Fin del tema I.3 y del bloque de Constitución (I.1 a I.3)**", S["s38"]["body"]))

    # ----------------------------------------------------------------- preguntas, flashcards, glosario, hitos
    def tema_de_q(q):
        c = q["cat"]; t = q["q"]
        if c in ("Estructura", "Reforma", "Fechas"): return 1
        if c == "Contenido": return 1 if re.search(r"valores superiores|lengua española oficial", t) else 2
        if c in ("Garantías", "Suspensión", "Defensor del Pueblo"): return 2
        return 3
    def tema_de_fc(f):
        c = f["cat"]; q = f["q"]
        if c in ("Fechas", "Estructura", "Reforma"): return 1
        if c == "Contenido": return 1 if re.search(r"estructura interna|valores superiores|art. 9\.3|9\.3 de la", q) else 2
        if c in ("Garantías", "Suspensión", "Defensor del Pueblo"): return 2
        return 3
    def tema_de_g(g): return 1 if g["cat"] in ("Estructura", "Fechas", "Reforma") else 3 if g["cat"] == "Tribunal Constitucional" else 2
    REMAP_G = {"s5": "s16", "s25": "s24", "s40": "s39", "s31": "s29", "s7": "s6"}
    ids_tema = {a[0] for a in ap}
    Q = [q for q in T.Q if tema_de_q(q) == tema_n]
    FC = [f for f in T.FC if tema_de_fc(f) == tema_n]
    G = [dict(g, section=REMAP_G.get(g["section"], g["section"])) for g in T.G if tema_de_g(g) == tema_n]
    H = []
    # hitos por tema
    if tema_n == 1:
        H = [h for h in T.H if h["target"] in ("s1", "s2", "s45")]
    elif tema_n == 2:
        H = [dict(y="1978", txt="27-12-1978: la Constitución, en vigor desde el 29-12-1978, reconoce en el Título I (arts. 10 a 55) los derechos y deberes fundamentales y sus garantías", cons="Niveles de protección, garantías (arts. 53 y 54) y suspensión (art. 55)", cat="normativo", target="s16")] + [h for h in T.H if h["target"] in ("s39", "s28")]
    else:
        H = [dict(y="1978", txt="27-12-1978: sanción de la Constitución, que crea el Tribunal Constitucional (Título IX, arts. 159 a 165); BOE y entrada en vigor el 29-12-1978", cons="Composición, competencias y valor de las sentencias", cat="normativo", target="s33")] + [h for h in T.H if h["target"] == "s33"]
    if tema_n == 3:
        FC += [dict(q="¿Qué es el Tribunal Constitucional según su ley orgánica?", a="**Intérprete supremo** de la Constitución, **independiente** de los demás órganos constitucionales, sometido **solo** a la Constitución y a su ley orgánica y **único en su orden** (art. 1 LOTC).", cat="Tribunal Constitucional"),
               dict(q="¿Quién legitima cada proceso ante el Tribunal Constitucional?", a="**Inconstitucionalidad**: Presidente del Gobierno, Defensor del Pueblo, 50 Diputados, 50 Senadores y ejecutivos y Asambleas de las CCAA. **Amparo**: persona con interés legítimo, Defensor del Pueblo y Ministerio Fiscal. **Cuestión**: el órgano judicial (arts. 162 y 163 CE).", cat="Tribunal Constitucional")]
    # ----------------------------------------------------------------- montaje
    cod = COD_TEMA[tema_n]
    sub = {1: "Cuándo y cómo nace la Constitución, cómo está estructurada, de qué trata cada artículo del 1 al 55 y cómo se reforma. Primer tema del bloque I, estudiado junto a I.2 e I.3 según el módulo M101.",
           2: "Los niveles de protección del Título I, los mecanismos de garantía, la suspensión de derechos (estados de alarma, excepción y sitio) y el Defensor del Pueblo. Segundo tema del bloque I (módulo M101).",
           3: "Qué es el Tribunal Constitucional, cómo se compone, qué procesos conoce y qué valor tienen sus sentencias. Tercer tema del bloque I (módulo M101)."}[tema_n]
    et = {1: ["Constitución Española", "Estructura de la CE", "Arts. 1 a 55", "Reforma constitucional", "Módulo M101"],
          2: ["Derechos fundamentales", "Garantías", "Suspensión de derechos", "Defensor del Pueblo", "Módulo M101"],
          3: ["Tribunal Constitucional", "LOTC", "Amparo", "Inconstitucionalidad", "Módulo M101"]}[tema_n]
    X = Tema(TEMA_DE[tema_n], sub, et)
    X.meta["title"] = {1: "La Constitución de 1978: estructura, contenido y reforma", 2: "Derechos y deberes fundamentales: garantía, suspensión y Defensor del Pueblo", 3: "El Tribunal Constitucional"}[tema_n]
    for i, tit, body, nivel in ap:
        body = _limpia(body, tit)
        if i == "s48" and tema_n == 1:
            body = re.sub(r"→ Siguiente: [^*\n]+", "→ Siguiente: IV.6 Cómo no confundir las mayorías", body)
        if i == ap[-1][0] and tema_n == 1:   # último apartado de I.1: enlace al tema siguiente
            body = re.sub(r"→ Siguiente: [^*\n]+", "→ Fin del tema I.1: sigue el tema I.2 (derechos y deberes fundamentales)", body)
        X.ap(i, tit, body if i == "s0" else _remisiones(body, tema_n), nivel)
    X.Q, X.FC, X.G, X.H = Q, FC, G, H
    return X
