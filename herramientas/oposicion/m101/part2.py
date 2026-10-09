
# =============================================================================
# MAPA
T.ap("s0", "Mapa del tema", f"""
**Epígrafes oficiales** (BOE-A-2025-26262, anexo VII, Bloque I). Este tema **reúne los tres primeros temas del bloque**, igual que la plantilla del plan de estudio y el módulo M101:
> I.1 La Constitución Española de 1978: estructura y contenido. La reforma de la Constitución.
> I.2 Derechos y deberes fundamentales. Su garantía y suspensión. El Defensor del Pueblo.
> I.3 El Tribunal Constitucional. Organización, composición y atribuciones.

### El hilo del tema

| Bloque | Pregunta | Constitución | Otras normas |
|---|---|---|---|
| **I** | ¿Cuándo nace y cuándo se ha reformado? | Fórmula final, disp. final | Cuatro reformas (1992, 2011, 2024, 2026) |
| **II** | ¿Cómo está hecha? | Partes, títulos, capítulos, secciones, disposiciones | — |
| **III** | ¿De qué trata cada artículo? | Arts. 1 a 55 (literales) | — |
| **IV** | ¿Qué niveles de protección tienen los derechos? | Título I, arts. 10 a 52 | — |
| **V** | ¿Cómo se garantizan? | Arts. 53, 81, 161 y 162 | LOTC arts. 32, 33, 41 a 46 |
| **VI** | ¿Cómo se suspenden? | Arts. 55 y 116 | LO 4/1981 |
| **VII** | El Tribunal Constitucional | Título IX, arts. 159 a 165 | LOTC |
| **VIII** | El Defensor del Pueblo | Art. 54 | LO 3/1981 |
| **IX** | ¿Cómo se reforma? | Título X, arts. 166 a 169; art. 87 | Reglamentos del Congreso y del Senado; LO 2/1980 |
| **X** | Preguntas y repaso | — | — |
| **XI** | Cronología e hitos | — | — |

### Cómo estudiar este tema (módulo M101)

- **Mira siempre el epígrafe.** Estudiar «por leyes» está bien al principio, pero el programa dice qué se puede preguntar: aquí se ha quitado lo que no entra.
- La Constitución es la **única** norma en la que hay que aprender la **estructura y el contenido artículo por artículo**: en las demás leyes no se pregunta así.
- **Lectura profunda de los artículos 1 a 55**, cada vez que repases el tema. Gran parte de las preguntas intentan confundirte con **palabras clave** de esos artículos. **No hace falta saberlos literalmente**, pero sí conocer su «música» para que no te cuelen una palabra cambiada.
- **Usa siempre el mismo material.** La memoria visual ayuda a ubicar la información: por eso cada título y capítulo tiene **el mismo color** en los apuntes, en el texto de la Constitución, en el organigrama y en el test.
- Primera vuelta: sabe **de qué trata cada artículo** y **dónde está** en la estructura (¿en qué capítulo? ¿en qué sección?). Después, ve profundizando.
- Se preguntan, sobre todo, la **estructura**, las **garantías** y la **suspensión** de derechos. Según el módulo, el 90 % de las preguntas de este tema son de lo que aquí se desarrolla.

{ir("#/ce/texto", "📜 Constitución completa")} {ir("#/ce/organigrama", "🗺 Organigrama")} {ir("#/ce/test", "🧭 Test Constitución")}

### Las etiquetas de los apuntes

- {IMP} → lo que el módulo marca como «importante» o «atención»: se pregunta mucho o se presta a trampas.
- {PRE} → lo que el módulo dice que **no es necesario** estudiar a fondo. Lleva una nota que explica por qué.
- Los colores de los títulos y capítulos son los de la Constitución completa: {tag("P", "Título preliminar")} {tag("I", "Título I")} {tag("I.2.1", "Sección 1.ª")} {tag("III", "Título III")} {tag("IX", "Título IX")}…

### Avisos: lo que dice la norma prevalece sobre la guía

- **Reforma del art. 69.3.** La guía M101 la sitúa el «20 de mayo de 2026». La reforma es **de 19 de mayo de 2026** (fecha de la sanción del Rey) y se publicó y entró en vigor el **20 de mayo de 2026** (→ I.2).
- **Reformas.** En el vídeo solo se citan las de los arts. 13.2 y 135; la guía añade la del 49 (2024) y la del 69.3 (2026). En total hay **cuatro**.
- **Ley de igualdad.** El vídeo dice que va «por ley orgánica». La LO 3/2007 lo es por su nombre, pero solo tienen carácter orgánico algunos preceptos (→ V.1).
- **Organigrama.** El de la guía rotula el capítulo II del título I con «Art. 14». Aquí se sigue el texto de la CE: el capítulo II comprende los **arts. 14 a 38** (→ II.3).
""")

# =============================================================================
T.ap("bI", "I. ¿Cuándo nace la Constitución y cuándo se ha reformado?", donde(
  "Primera pregunta. Conviene conocer las **fechas** y, sobre todo, **quién hace qué** en cada una: aprobar, ratificar, sancionar, promulgar, publicar y entrar en vigor son cosas distintas.",
  ["1 Las fechas de 1978", "2 Las cuatro reformas"]))

T.ap("s1", "I.1 Las fechas de 1978", f"""
Para recordarlas, ponte en situación: **las Cortes aprueban** el texto en sesiones plenarias del Congreso y del Senado; más de un mes después, **el pueblo lo ratifica** en referéndum (preparar el referéndum es lo que más tarda); y todo lo demás ocurre en diciembre del 78: **el Rey sanciona y promulga**, y dos días después **se publica en el BOE y entra en vigor**.

{tabla(["Hecho", "Fecha", "Quién", "Fuente"], [
  ["**Aprobación**", "31 de octubre de 1978", "Las **Cortes Generales**, en sesiones plenarias del Congreso de los Diputados y del Senado", "[[M101]]"],
  ["**Ratificación**", "6 de diciembre de 1978", "El **pueblo español**, en referéndum", "[[M101]]"],
  ["**Sanción y promulgación**", "27 de diciembre de 1978", "El **Rey**, ante las Cortes", "CE (fórmula final)"],
  ["**Publicación en el BOE y entrada en vigor**", "29 de diciembre de 1978", "BOE n.º 311; entra en vigor el **mismo día** de la publicación", "BOE · CE (disp. final)"]])}

{unidad("1.1 La sanción y promulgación: 27 de diciembre",
  lit("CE", "firma", ["GUARDEN Y HAGAN GUARDAR ESTA CONSTITUCIÓN COMO NORMA FUNDAMENTAL DEL ESTADO", "A VEINTISIETE DE DICIEMBRE DE MIL NOVECIENTOS SETENTA Y OCHO"], solo=[0, 1, 2], titulo="Fórmula final de la Constitución"))}

{unidad("1.2 La entrada en vigor: el día de la publicación en el BOE",
  lit("CE", "df", ["entrará en vigor el mismo día de la publicación de su texto oficial"]))}

!> {IMP} **Atención a los verbos.** Las preguntas juegan con quién hace cada cosa: las **Cortes aprueban**, el **pueblo ratifica**, el **Rey sanciona y promulga**, el **BOE publica** y la Constitución **entra en vigor**. Y se agrupan **de dos en dos**: sanción y promulgación (27); publicación y entrada en vigor (29, dos días después). Sepáralos siempre.

?> **Publicar no es entrar en vigor.** Que una norma se publique en el BOE no significa que esté ya en vigor: a veces se pospone. En la Constitución coinciden porque lo dice su disposición final.

**Truco para recordar:** todo empieza el **27** (sanción y promulgación) y **dos días después**, el **29**, pasan otras dos cosas (publicación y entrada en vigor). El 27 se repite en las reformas de 1992 (27 de agosto) y de 2011 (27 de septiembre).
""", 2)

T.ap("s2", "I.2 Las cuatro reformas de la Constitución", f"""
La Constitución se ha reformado **cuatro veces**, siempre por el procedimiento del **art. 167** (→ IX.2). Las fechas son las de la **sanción** del Rey, que figuran al pie de cada reforma; el BOE las publica y entran en vigor, como la propia Constitución, el mismo día de la publicación.

{tabla(["Reforma", "Artículo", "Sanción", "Publicación y entrada en vigor", "Qué cambia"], [
  ["**1992**", "**13.2**", "27 de agosto de 1992", "28 de agosto de 1992", "Los extranjeros pueden tener **sufragio pasivo** (y no solo activo) en las elecciones **municipales**, por reciprocidad. Se añadió «y pasivo»."],
  ["**2011**", "**135**", "27 de septiembre de 2011", "27 de septiembre de 2011", "**Estabilidad presupuestaria**: el artículo se reescribió entero. Los límites de déficit estructural del art. 135.2 «entrarán en vigor a partir de 2020» (disposición adicional única, ap. 3)."],
  ["**2024**", "**49**", "15 de febrero de 2024", "17 de febrero de 2024", "Protección de las **personas con discapacidad**: actualiza su lenguaje y su contenido."],
  ["**2026**", "**69.3**", "19 de mayo de 2026", "20 de mayo de 2026", "Circunscripciones del **Senado** en las islas: **Ibiza y Formentera** pasan a elegir cada una su senador; la eficacia de estas circunscripciones «quedará pospuesta hasta la convocatoria de las primeras elecciones al Senado» posteriores a la reforma (disposición transitoria única)."]])}

{unidad("2.1 Reforma del art. 13.2 (1992)",
  lit("CE", "a13", ["sufragio activo y pasivo"], solo=[2]),
  lit("REF1992", "preambulo", ["27 de agosto de 1992"], solo=[ix("REF1992", "preambulo", "Artículo único") + j for j in (0, 1, 2)] + [ix("REF1992", "preambulo", "Madrid,")], titulo="Reforma de la Constitución de 1992 (artículo único)"))}

^> **Antes de 1992.** El apartado ya permitía, por reciprocidad, una excepción a que solo los españoles sean titulares de los derechos del art. 23, pero **solo para el derecho de voto (sufragio activo)** en las elecciones municipales: un extranjero podía votar, no ser elegido. La reforma añadió el **sufragio pasivo** (poder ser elegido).

{unidad("2.2 Reforma del art. 135 (2011)",
  lit("CE", "a135", ["principio de estabilidad presupuestaria", "mayoría absoluta de los miembros del Congreso de los Diputados"], solo=[1, 2, 3, 4, 5, 6, 7], titulo="Artículo 135 (apartados 1 a 4; el 5 y el 6 no se reproducen)"),
  lit("REF2011", "preambulo", ["garantizar el principio de estabilidad presupuestaria"], solo=[9], titulo="Exposición de motivos de la Reforma de 2011 (extracto)"))}

^> **Antes de 2011.** El art. 135 era mucho más corto y trataba solo de la **deuda pública**: el Gobierno necesitaba autorización por ley para emitirla o contraer crédito, y los créditos para pagar los intereses y el capital de la deuda del Estado se consideraban siempre incluidos en los presupuestos de gastos y quedaban protegidos frente a enmiendas mientras cumplieran la ley de emisión. **No decía nada de estabilidad presupuestaria ni de déficit estructural**: la reforma reescribió el artículo entero.

{unidad("2.3 Reforma del art. 49 (2024)",
  lit("CE", "a49", ["Las personas con discapacidad ejercen los derechos previstos en este Título en condiciones de libertad e igualdad reales y efectivas"], solo=[1, 2]),
  lit("REF2024", "preambulo", ["precisa de una actualización en cuanto a su lenguaje y contenido"], solo=[10], titulo="Preámbulo de la Reforma de 2024 (extracto)"))}

^> **Antes de 2024.** El art. 49 era un solo párrafo, con enfoque **asistencial**: ordenaba a los poderes públicos una política de previsión, tratamiento, rehabilitación e integración de los **«disminuidos»** físicos, sensoriales y psíquicos, con atención especializada y amparo para disfrutar de los derechos del Título I. La reforma cambió el término por **«personas con discapacidad»** y el enfoque por el de derechos en **libertad e igualdad reales y efectivas**, con autonomía personal, inclusión social y participación de sus organizaciones.

{unidad("2.4 Reforma del art. 69.3 (2026)",
  lit("CE", "a69", ["Ibiza, Formentera"], solo=[3]),
  lit("REF2026", "preambulo", ["19 de mayo de 2026"], solo=[ix("REF2026", "preambulo", "Artículo único") + j for j in (0, 1)] + [ix("REF2026", "preambulo", "Madrid,")], titulo="Reforma de la Constitución de 2026 (artículo único y fecha)"))}

^> **Antes de 2026.** El apartado tenía ya una circunscripción por **isla o agrupación de islas** con Cabildo o Consejo Insular, con tres senadores para las islas mayores y uno para cada una de las demás, pero **Ibiza y Formentera figuraban unidas como una agrupación** que elegía **un solo senador**. La reforma las separó: cada una elige el suyo y desaparece la referencia a las «agrupaciones». Ojo también a los nombres: la redacción de 1978 decía «Gomera, Hierro»; la vigente, «La Gomera, El Hierro».

### 2.5 Por qué se reformó cada artículo

Las cuatro reformas tienen una **causa externa o social** que explica su contenido, y la propia reforma la cuenta en su **exposición de motivos** o preámbulo (citas literales, en **color violeta** como todos los textos de las reformas, para distinguirlos del artículo definitivo, que va en el color normal de los textos legales):

{tabla(["Reforma", "Por qué se hizo", "Lo dice así la reforma"], [
  ["**1992** · art. 13.2", "Para poder **ratificar el Tratado de la Unión Europea (Maastricht)**: reconocía a los ciudadanos de la Unión el derecho a ser **elegibles** en las elecciones municipales del Estado en que residan, y el Tribunal Constitucional declaró que **chocaba con el art. 13.2** (que solo permitía el sufragio activo).", f"{c('REF1992', 'preambulo', 'es contraria al artículo 13.2 de la Constitución')} … {c('REF1992', 'preambulo', 'exige, pues, la reforma previa del citado precepto constitucional')}"],
  ["**2011** · art. 135", "La **crisis económica** y la pertenencia a la **Unión Económica y Monetaria**: se quiso llevar a la Constitución la **estabilidad presupuestaria** para reforzar la confianza en la economía española y el compromiso con la UE.", f"{c('REF2011', 'preambulo', 'no ha hecho sino reforzar la conveniencia de llevar el principio de referencia a nuestra Constitución')}"],
  ["**2024** · art. 49", "Adaptar el artículo a la **Convención sobre los derechos de las personas con discapacidad** (Nueva York, 2006) y a la petición de las organizaciones del sector: **actualizar su lenguaje y su contenido**.", f"{c('REF2024', 'preambulo', 'precisa de una actualización en cuanto a su lenguaje y contenido')}"],
  ["**2026** · art. 69.3", "Atender la **reivindicación histórica de Formentera**: que, al tener su propio Consejo Insular, **elija un senador propio** y no comparta el de la agrupación Ibiza-Formentera.", f"{c('REF2026', 'preambulo', 'ha ido ligada históricamente a la posibilidad de elección de un senador propio')}"]])}

{IMP} **El texto que figura en cada reforma (2.1 a 2.4) es el redactado definitivo**: el artículo tal como **quedó** tras la reforma y como está **hoy en vigor** en el texto consolidado del BOE. Cada reforma sustituye el texto anterior; no se acumulan. Dos matices de eficacia: en el art. 135, los límites de déficit estructural del apartado 2 «entrarán en vigor a partir de 2020», y en el 69.3, las nuevas circunscripciones del Senado se aplican desde las **primeras elecciones al Senado posteriores** a la reforma.

!> {IMP} **Para el examen:** artículos reformados **13.2, 135, 49 y 69.3**, y año de cada reforma (**1992, 2011, 2024, 2026**). La del 135 es la más «radical»: se reescribió entero (como el 49 en 2024), en plena crisis económica y financiera.

?> La **guía M101** da el art. 69.3 el «20 de mayo de 2026»: es la fecha de **publicación y entrada en vigor**. La reforma es de **19 de mayo de 2026** (sanción).
""", 2)
