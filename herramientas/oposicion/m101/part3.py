
# =============================================================================
# II. ESTRUCTURA
_P = TIT["P"]; _I = TIT["I"]
assert rng(arts(_P)) == "1–9" and rng(arts(_I)) == "10–55"
FILAS_TIT = []
for _t in CEJ["titulos"]:
    _a = arts(_t); assert _a == list(range(_a[0], _a[-1] + 1))
    FILAS_TIT.append([tag(_t["id"], "Título preliminar" if _t["id"] == "P" else "Título " + _t["id"]), _t["nombre"] or "—", f"**{rng(_a)}**", len(_a)])
assert sum(f[3] for f in FILAS_TIT) == 169 and len(FILAS_TIT) == 11

T.ap("bII", "II. ¿Cómo está hecha? Estructura de la Constitución", donde(
  "Segunda pregunta. La Constitución es la **única norma** en la que hay que saber de memoria **cómo se reparten los artículos**: títulos, capítulos y secciones. Sirve de armazón para colgar después el contenido de cada artículo.",
  ["1 Las dos partes: dogmática y orgánica", "2 Los títulos y sus artículos", "3 El Título I por dentro (lo más preguntable)", "4 Los capítulos de los Títulos III y VIII", "5 Las disposiciones: 4-9-1-1"]))

T.ap("s3", "II.1 Las dos partes y la lógica de «las muñecas rusas»", f"""
La Constitución se abre con un **preámbulo** y su articulado se reparte en **dos partes**:

{tabla(["Parte", "Títulos", "Artículos", "De qué trata"], [
  [f"**Parte dogmática**", f"{tag('P', 'Título preliminar')} y {tag('I', 'Título I')}", "**1 a 55**", "Los principios y los **derechos y deberes**: qué es el Estado y qué se reconoce a las personas"],
  [f"**Parte orgánica**", f"{tag('II', 'Título II')} a {tag('X', 'Título X')}", "**56 a 169**", "Cómo se **organiza** el Estado y sus instituciones: Corona, Cortes, Gobierno, Poder Judicial, territorio, Tribunal Constitucional y reforma"]])}

### La lógica de «las muñecas rusas»

Como muchas leyes, la Constitución va **de lo general a lo concreto**: lo primero que aparece es lo más **ideal e inespecífico**, y lo que viene después lo **concreta**. Si tienes esto en la cabeza, la estructura se asimila mejor:

- El **preámbulo** dice a qué aspira el Estado; la Constitución desarrolla esas aspiraciones. Según el módulo M101, no tiene valor jurídico propio («papel mojado»), pero a la vez es lo más importante porque da el sentido a todo lo demás.
- El **Título preliminar** y el **Título I** son la parte dogmática: sientan las ideas que luego desarrolla la parte orgánica.
- Dentro del Título I ocurre lo mismo: el **art. 10** (la dignidad de la persona, los derechos inviolables…) queda **fuera de los capítulos** y nutre «espiritualmente» todo lo demás; y el **art. 14** (la igualdad ante la ley) queda **fuera de las dos secciones** y se concreta en los derechos que vienen después.

!> {IMP} No es una regla que se cumpla a rajatabla, pero **sirve para ubicar**: lo primero es lo más importante y a la vez lo más genérico; lo que viene después es lo que concreta. Por eso los artículos 10 y 14 quedan «sueltos».

{ir("#/ce/organigrama", "🗺 Ver el organigrama")}
""", 2)

T.ap("s4", "II.2 Los títulos y sus artículos", f"""
{IMP} Hay que saberse **los nombres de los títulos** y **cómo se reparten los artículos** entre ellos. Se pregunta con frecuencia (p. ej., «¿en qué título está el art. 56?», «¿qué artículos comprende el Título VIII?»).

{tabla(["Título", "Nombre (rúbrica del BOE)", "Artículos", "N.º"], FILAS_TIT + [["**Total**", "", "**1–169**", "**169**"]])}

**Números finales de cada título** (para fijar los límites): **9 · 55 · 65 · 96 · 107 · 116 · 127 · 136 · 158 · 165 · 169**.

Los títulos tienen **rúbrica propia** salvo el **Título preliminar**, que no tiene nombre. En total: **11 títulos** (el preliminar y diez numerados), **169 artículos** y **15 disposiciones** (→ II.5).

### 2.1 Cómo memorizar los límites de los títulos [[M107]]

**1.º El orden de los títulos II a X.** Se aprende de lo más «alto» a lo más práctico: la **Corona** (Título II, la más solemne), después los poderes del Estado —**Cortes**, **Gobierno y Administración**, las **relaciones** entre ambos y el **Poder Judicial**—, luego **Economía y Hacienda**, la **organización territorial** (el gran asunto político, que ya asoma en los primeros artículos: lenguas, banderas, autonomía) y, al final, los dos «constitucionales»: el **Tribunal Constitucional** y la **reforma**. Saber qué es lo último ayuda: la reforma cierra la Constitución, como es lógico.

**2.º Los dos «cincos».** El Título I acaba en el **55** (su único artículo final es el de la suspensión de los derechos) y el Título II en el **65**: **55, 65**.

**3.º Desde el Título III, no memorices el final: suma.** Cada título termina en «su primer artículo + N»:

| Título | Primer artículo | + N | Último artículo |
|---|---|---|---|
| {{{{c:III~III · Cortes Generales}}}} | 66 | **+30** | 96 |
| {{{{c:IV~IV · Gobierno y Administración}}}} | 97 | **+10** | 107 |
| {{{{c:V~V · Relaciones Gobierno–Cortes}}}} | 108 | **+8** | 116 |
| {{{{c:VI~VI · Poder Judicial}}}} | 117 | **+10** | 127 |
| {{{{c:VII~VII · Economía y Hacienda}}}} | 128 | **+8** | 136 |
| {{{{c:VIII~VIII · Organización territorial}}}} | 137 | **+21** | 158 |
| {{{{c:IX~IX · Tribunal Constitucional}}}} | 159 | **+6** | 165 |
| {{{{c:X~X · Reforma constitucional}}}} | 166 | **+3** | 169 |

Los números se retienen mejor con una idea: **30, 10 y 8** son los «sumandos» de los primeros bloques (las Cortes se llevan el 30; el Gobierno y el Poder Judicial, un 10 cada uno; las relaciones y Economía, el «8 comodín»), y lo que queda desde el art. 137 hasta el 169 —**21 + 6 + 3**— suma otro **30**. Recuerda que «+ N» significa que el título tiene **N + 1** artículos (el Título III tiene 31).

{ir("#/ce/texto", "📜 Ver el texto completo, con un color por título")}
""", 2)

_c2 = _I["caps"][1]
assert [rng(arts(x)) for x in _I["caps"]] == ["11–13", "14–38", "39–52", "53–54", "55"] and rng(arts(_c2["secs"][0])) == "15–29" and rng(arts(_c2["secs"][1])) == "30–38"
assert _I["arts"][0]["n"] == 10 and _c2["arts"][0]["n"] == 14
T.ap("s5", "II.3 El Título I por dentro (lo más preguntable)", f"""
{IMP} Es **lo más preguntable de la estructura**, sobre todo la división del **capítulo segundo** en secciones. Hay que saberlo «como el padrenuestro».

{tabla(["Unidad", "Nombre (BOE)", "Artículos", "Ojo"], [
  [tag("I", "Título I"), c("CE", "ti", "De los derechos y deberes fundamentales"), "**10 a 55**", "Contiene los derechos, deberes y sus garantías"],
  [tag("I", "Art. 10"), "(dignidad de la persona…)", "**10**", "**Fuera de los capítulos**: va antes del capítulo primero"],
  [tag("I.1", "Capítulo primero"), c("CE", "cprimero", "De los españoles y los extranjeros"), "**11 a 13**", "Nacionalidad, mayoría de edad y extranjeros"],
  [tag("I.2", "Capítulo segundo"), c("CE", "csegundo", "Derechos y libertades"), "**14 a 38**", "El art. **14** queda **fuera de las dos secciones**"],
  [tag("I.2.1", "Sección 1.ª"), c("CE", "s1", "De los derechos fundamentales y de las libertades públicas"), "**15 a 29**", "**Los derechos fundamentales**: la máxima protección"],
  [tag("I.2.2", "Sección 2.ª"), c("CE", "s2", "De los derechos y deberes de los ciudadanos"), "**30 a 38**", "Derechos y deberes de los ciudadanos"],
  [tag("I.3", "Capítulo tercero"), c("CE", "ctercero", "De los principios rectores de la política social y económica"), "**39 a 52**", "Son principios, no derechos fundamentales"],
  [tag("I.4", "Capítulo cuarto"), c("CE", "ccuarto", "De las garantías de las libertades y derechos fundamentales"), "**53 y 54**", "Garantías: arts. 53 y 54 (→ V)"],
  [tag("I.5", "Capítulo quinto"), c("CE", "cquinto", "De la suspensión de los derechos y libertades"), "**55**", "Suspensión (→ VI)"]])}

!> {IMP} **Los dos «sueltos» del título I:** el **art. 10** queda fuera de los capítulos y el **art. 14** queda dentro del capítulo segundo pero **fuera de las secciones primera y segunda**. Si preguntan «¿qué artículos comprende la sección primera?», la respuesta es **15 a 29** (no el 14).

!> {IMP} **La división de los 55 artículos de la parte dogmática, en una línea:** 1-9 · 10 · 11-13 · 14 · **15-29** · 30-38 · 39-52 · 53-54 · 55.

### 3.1 Reglas para no perderse en el Título I [[M107]]

- **Los dos artículos «colgantes».** En el Título I —el más importante— aparecen dos artículos que quedan fuera de la subdivisión siguiente: el **10**, fuera de los capítulos, y el **14**, dentro del capítulo II pero fuera de las secciones. Los dos son «de principios» (la dignidad de la persona; la igualdad y la no discriminación): lo más general abre cada nivel y lo más concreto viene después.
- **Cómo saber dónde acaba.** El título I termina en el **55**: recuerda la rima del cinco. El capítulo V solo tiene ese artículo (la suspensión de los derechos, «el destructor»).
- **El capítulo I, de «calentamiento».** Son tres artículos poco importantes pero muy tramposos: la **nacionalidad** (11), la **mayoría de edad** (12) y los **extranjeros** (13). No te olvides de que existe antes de llegar al capítulo II.
- **«Los dos protectores».** El capítulo IV (arts. **53** y **54**) protege lo anterior: el 53, con la tutela y el amparo; el 54, con el Defensor del Pueblo.
- **El capítulo III, por descarte.** Si ya sabes que la sección 2.ª acaba en el **38** y que los protectores empiezan en el **53**, el capítulo III es lo que queda: del **39 al 52**.
- **Círculos concéntricos.** Cuanto más te alejas del centro, menos garantías y menos preguntas: **sección 1.ª** (máxima protección), **sección 2.ª** (vinculan a los poderes públicos, pero sin amparo salvo el 30.2) y **capítulo III** (solo informan). Si preguntan por el amparo, ubica el artículo: ¿está en 14, 15-29 o 30.2?

**Truco:** de **15 a 29** es la sección primera del capítulo segundo del título I. Parece un trabalenguas, pero es la clave de muchas preguntas: los derechos de la sección primera son los que tienen **todas** las garantías, incluidas la reserva de ley orgánica (art. 81) y la reforma agravada (art. 168); el art. 14 y el 30.2 comparten solo algunas, como el amparo (→ IV).
""", 2)

T.ap("s6", "II.4 Los capítulos de los Títulos III y VIII", f"""
{PRE} **No pierdas tiempo memorizando la división en capítulos de los Títulos III y VIII.** El módulo la considera prescindible: se pregunta mucho menos que la del Título I. Basta con saber que existen y los límites de los títulos. Aquí está por si quieres consultarla:

{tabla(["Título", "Capítulo", "Nombre (BOE)", "Artículos"], [
  [tag(t["id"], "Título " + t["id"]), tag(f'{t["id"]}.{i + 1}', cp["num"].capitalize().replace("Ítulo", "ítulo")), cp["nombre"], rng(arts(cp))] for t in (TIT["III"], TIT["VIII"]) for i, cp in enumerate(t["caps"])])}

*Nota: en el Título I (11 a 13, 14 a 38, 39 a 52, 53 y 54, 55) la división sí es muy preguntable; en el III y el VIII, no.*
""", 2)

assert sum(1 for d in CEJ["disposiciones"] if "adicional" in d["t"]) == 4 and sum(1 for d in CEJ["disposiciones"] if "transitoria" in d["t"]) == 9
T.ap("s7", "II.5 Las disposiciones: 4-9-1-1", f"""
Tras el artículo 169 vienen **quince disposiciones**, que se agrupan así:

{tabla(["Clase", "Cuántas", "Cuáles"], [
  ["**Adicionales**", "**4**", "Primera a cuarta"],
  ["**Transitorias**", "**9**", "Primera a novena"],
  ["**Derogatoria**", "**1**", "Única"],
  ["**Final**", "**1**", "Única"]])}

{IMP} **Regla mnemotécnica: «4-9-1-1».** Cuatro adicionales, **nueve** transitorias (la Constitución nace en plena **transición**: por eso son las más numerosas), **una** derogatoria y **una** final. Y siempre **en este orden**: adicionales, transitorias, derogatoria y final.

{lit("CE", "dd", ["Queda derogada la Ley 1/1977, de 4 de enero, para la Reforma Política"], solo=[0, 1])}

{lit("CE", "df", ["entrará en vigor el mismo día de la publicación de su texto oficial"])}

!> La **disposición derogatoria** deroga la Ley para la Reforma Política y las Leyes Fundamentales del régimen anterior; la **final** fija la **entrada en vigor** (→ I.1).
""", 2)

T.ap("s8", "II.6 Resumen de la estructura", resumen([
  "**Preámbulo** + **Parte dogmática** (arts. **1-55**: Título preliminar y Título I) + **Parte orgánica** (arts. **56-169**: Títulos II a X) + **15 disposiciones** (4-9-1-1).",
  "**11 títulos**, **169 artículos**. Finales de título: 9 · 55 · 65 · 96 · 107 · 116 · 127 · 136 · 158 · 165 · 169.",
  "**Título I:** art. 10 (suelto) · cap. I (11-13) · cap. II (14-38: art. 14 suelto, **sección 1.ª 15-29**, sección 2.ª 30-38) · cap. III (39-52) · cap. IV (53-54) · cap. V (55).",
  "La división en capítulos de los Títulos III y VIII es " + PRE + "."], "Siguiente: III. ¿De qué trata cada artículo? (arts. 1 a 55)"), 2)
