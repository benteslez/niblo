
# =============================================================================
# IV. NIVELES DE PROTECCIÓN · V. GARANTÍAS
def lx(k, idb, num, resaltar=(), solo=None, extra=""):
    return lit(k, idb, resaltar, solo=solo, titulo=f"Artículo {num}{extra} ({CORTO[k]})")
SI, NO = "✔", "✘"
T.ap("bIV", "IV. Derechos y deberes fundamentales: los niveles de protección", donde(
  "Primera pregunta. El Título I no protege igual todos sus artículos: hay **niveles de protección**. Saber a qué artículo corresponde cada garantía es la clave del tema: **las preguntas se resuelven con el cuadro** del apartado IV.2.",
  ["1 Qué contiene el Título I", "2 Cuadro de contenido y garantías", "3 Los deberes"]))

T.ap("s16", "IV.1 Qué contiene el Título I", f"""
{tag("I", "Título I")} se llama **«De los derechos y deberes fundamentales»** (arts. **10 a 55**) y reúne tres cosas: **los derechos y deberes** (arts. 10 a 52), **sus garantías** (cap. IV, arts. 53 y 54) y **su suspensión** (cap. V, art. 55).

Lo primero que hay que entender es que **no todo lo que está en el Título I es un «derecho fundamental»**. El nombre se reserva a los de la {tag("I.2.1", "sección 1.ª")} del capítulo II: «**De los derechos fundamentales y de las libertades públicas**» (arts. 15 a 29). Los demás son derechos y principios con **menos garantías**:

{tabla(["Nivel", "Dónde está", "Qué son", "Garantías"], [
  ["**1.º · Máximo**", f"{tag('I.2.1', 'Sección 1.ª')} · arts. **15 a 29**", "**Derechos fundamentales y libertades públicas**", "**Todas**: ley orgánica, ley, tutela preferente y sumaria, amparo, inconstitucionalidad, vinculación"],
  ["**2.º · Igualdad**", f"{tag('I.2', 'Art. 14')}", "Igualdad ante la ley", "Todas **menos la ley orgánica**: tutela preferente y sumaria, amparo, inconstitucionalidad, vinculación"],
  ["**3.º · Derechos y deberes de los ciudadanos**", f"{tag('I.2.2', 'Sección 2.ª')} · arts. **30 a 38**", "Derechos y deberes", "Vinculación, ley e inconstitucionalidad. **Amparo solo para el art. 30.2**"],
  ["**4.º · Principios rectores**", f"{tag('I.3', 'Capítulo III')} · arts. **39 a 52**", "**Principios**, no derechos fundamentales", "Solo **informan** la legislación, la práctica judicial y la actuación de los poderes públicos; se alegan **según las leyes**"],
  ["Fuera de estos niveles", f"{tag('I', 'Art. 10')} y {tag('I.1', 'capítulo I')} (arts. 11 a 13)", "Fundamento del orden político; nacionalidad y extranjeros", "No están en las garantías del art. 53; los protege el **Defensor del Pueblo** como todo el Título I"]])}

{IMP} **Ojo con lo que intentan colar:** el **derecho al trabajo** (35), la **propiedad privada** (33), la **salud** (43), la **vivienda** (47) o la redistribución equitativa de la renta (40) **no son derechos fundamentales** (los dos primeros son de la sección 2.ª; los demás, del capítulo III).
""", 2)

T.ap("s17", "IV.2 Cuadro de contenido y garantías", f"""
El cuadro cruza **cada unidad del Título I** con **cada garantía**. {IMP} Es **lo más preguntable**: «¿qué derechos pueden ser objeto de recurso de amparo?», «¿cuáles se regulan por ley orgánica?»…

{tabla(["Unidad", "Ley orgánica (art. 81.1)", "Solo por ley (53.1)", "Tutela ordinaria preferente y sumaria (53.2)", "Amparo (53.2)", "Inconstitucionalidad (53.1)", "Vinculan a los poderes públicos (53.1)", "Defensor del Pueblo (54)"], [
  [f"{tag('I', 'Art. 10')} y {tag('I.1', 'cap. I')} (10-13)", NO, NO, NO, NO, NO, NO, SI],
  [f"{tag('I.2', 'Art. 14')}", NO, SI, SI, SI, SI, SI, SI],
  [f"{tag('I.2.1', 'Sección 1.ª')} (15-29)", SI, SI, SI, SI, SI, SI, SI],
  [f"{tag('I.2.2', 'Art. 30.2')} (objeción de conciencia)", NO, SI, NO, SI, SI, SI, SI],
  [f"{tag('I.2.2', 'Sección 2.ª')} (resto: 30-38)", NO, SI, NO, NO, SI, SI, SI],
  [f"{tag('I.3', 'Capítulo III')} (39-52)", NO, NO, NO, NO, NO, "Informan (53.3)", SI]])}

**Cómo leer el cuadro (basado en los arts. 53, 54 y 81):**

- **Por ley orgánica:** solo la **sección 1.ª** (arts. 15 a 29). *Ojo con el art. 81.1: «y las demás previstas en la Constitución»*: hay leyes orgánicas por otras razones (→ V.1).
- **Tutela ante los tribunales ordinarios (preferente y sumaria):** el **art. 14 + la sección 1.ª**.
- **Recurso de amparo:** el **art. 14 + la sección 1.ª + el art. 30.2**.
- **Defensor del Pueblo:** **todo el Título I**.
- **Recurso de inconstitucionalidad y vinculación a los poderes públicos:** todo el **capítulo II** (arts. **14 a 38**).

!> {IMP} **Mnemotecnia de las tres garantías «fuertes»:** la **sección 1.ª (15-29)** las tiene **todas**. El **art. 14** las tiene todas **menos la ley orgánica**. Y el **30.2** solo tiene **amparo** de entre las especiales. Todo lo demás del capítulo II solo vincula, exige ley y puede llegar al **TC por inconstitucionalidad**.

{ir("#/ce/organigrama", "🗺 Ver el organigrama")}
""", 2)

T.ap("s18", "IV.3 Los deberes del Título I", f"""
El título habla de **derechos y deberes**. Los deberes expresamente declarados son pocos y se reconocen por la palabra «**deber**» en el texto (además, el **39.3** impone a los padres el deber de asistencia a los hijos y el **30.4** prevé deberes en casos de grave riesgo, catástrofe o calamidad pública):

{tabla(["Artículo", "Deber", "Texto literal"], [
  [tag("I.2.2", "Art. 30"), "**Defender a España** (y obligaciones militares, objeción de conciencia, servicio civil, grave riesgo o catástrofe)", c("CE", "a30", "Los españoles tienen el derecho y el deber de defender a España")],
  [tag("I.2.2", "Art. 31"), "**Contribuir** al sostenimiento de los gastos públicos", c("CE", "a31", "Todos contribuirán al sostenimiento de los gastos públicos de acuerdo con su capacidad económica")],
  [tag("I.2.2", "Art. 35"), "**Trabajar** (junto al derecho al trabajo)", c("CE", "a35", "Todos los españoles tienen el deber de trabajar y el derecho al trabajo")],
  [tag("I.3", "Art. 45"), "**Conservar el medio ambiente**", c("CE", "a45", "el deber de conservarlo")]])}

Fuera del Título I, el **art. 3.1** impone a todos los españoles el **deber de conocer el castellano**.
""", 2)

# ----------------------------------------------------------------------------- V
T.ap("bV", "V. ¿Cómo se garantizan los derechos? Los mecanismos (arts. 53, 54 y 81)", donde(
  "Quinta pregunta. La Constitución no se limita a reconocer los derechos: dispone **mecanismos para protegerlos**. Se estudian **en este orden**, y después se relaciona cada mecanismo con los artículos que protege (cuadro IV.2).",
  ["1 Reserva de ley (orgánica y ordinaria)", "2 Tutela ante los tribunales ordinarios", "3 Recurso de amparo", "4 Defensor del Pueblo", "5 Recurso de inconstitucionalidad", "6 Vinculación de los poderes públicos", "7 La paradoja del capítulo III", "8 Cuadro resumen"]))

T.ap("s19", "V.1 Reserva de ley: orgánica y ordinaria", f"""
Los derechos son cosas importantes que **no puede regular un reglamento**: solo una **ley**. Hay dos niveles de reserva:

{unidad("1.1 Reserva de ley en todo el capítulo II (art. 53.1)",
  lit("CE", "a53", ["vinculan a todos los poderes públicos", "Sólo por ley", "deberá respetar su contenido esencial", "artículo 161, 1, a)"], solo=[1]),
  fichab("Regulación del ejercicio de los derechos y libertades del capítulo II",
         "**Cualquier derecho del capítulo II** (arts. 14 a 38)",
         ["**Solo por ley**, nunca por reglamento", "Respetando siempre su **contenido esencial**"],
         "—",
         "La reserva de ley (ordinaria) es para **todo el capítulo II**; la de **ley orgánica**, solo para la sección 1.ª."))}

{unidad("1.2 Reserva de ley orgánica (art. 81)",
  lit("CE", "a81", ["desarrollo de los derechos fundamentales y de las libertades públicas", "y las demás previstas en la Constitución", "mayoría absoluta del Congreso"], solo=[1, 2]),
  fichab("Leyes orgánicas",
         "Las Cortes Generales; el Congreso, por mayoría absoluta",
         ["Desarrollo de los **derechos fundamentales y libertades públicas** = **sección 1.ª (arts. 15 a 29)**", "Estatutos de Autonomía y régimen electoral general", "**Y las demás previstas en la Constitución**"],
         "**Mayoría absoluta del Congreso** en una votación final sobre el conjunto del proyecto",
         f"{IMP} El **desarrollo de los derechos fundamentales y de las libertades públicas** (sección 1.ª, arts. 15 a 29) exige ley orgánica (art. 81.1); el resto de los derechos, **ley ordinaria**. Pero ojo: otros artículos del Título I prevén también ley orgánica (el **54**, Defensor del Pueblo, y el **55.2**, suspensión individual) y el 81.1 termina con «**y las demás previstas en la Constitución**»: hay otras leyes orgánicas que no son de derechos."))}

**Otras leyes orgánicas previstas en la propia Constitución**, que no están en el art. 81 (y por eso se pregunta):

{tabla(["Artículo", "Ley orgánica de…", "Literal"], [
  [tag("P", "Art. 8.2"), "Bases de la organización militar (Fuerzas Armadas)", c("CE", "a8", "Una ley orgánica regulará las bases de la organización militar")],
  [tag("I.4", "Art. 54"), "El Defensor del Pueblo", c("CE", "a54", "Una ley orgánica regulará la institución del Defensor del Pueblo")],
  [tag("IV", "Art. 116.1"), "Estados de alarma, de excepción y de sitio", c("CE", "a116", "Una ley orgánica regulará los estados de alarma, de excepción y de sitio")],
  [tag("IX", "Art. 165"), "El Tribunal Constitucional", c("CE", "a165", "Una ley orgánica regulará el funcionamiento del Tribunal Constitucional")]])}

!> {IMP} **Atención a la «ley de igualdad».** El vídeo del módulo dice que la ley de igualdad entre mujeres y hombres va por ley orgánica aunque el art. 14 quede fuera de la sección 1.ª. Es cierto que se llama **Ley Orgánica 3/2007**, pero **no toda ella** tiene ese carácter, según su propia disposición final:
{lit("LO3_2007", "dfsegunda", ["disposiciones adicionales primera, segunda y tercera", "El resto de los preceptos contenidos en esta Ley no tienen tal carácter"], solo=[0, 1], titulo="Disposición final segunda (LO 3/2007)")}
""", 2)

T.ap("s20", "V.2 Tutela ante los tribunales ordinarios (procedimiento preferente y sumario)", f"""
{unidad("2.1 Qué dice el art. 53.2",
  lit("CE", "a53", ["Cualquier ciudadano podrá recabar la tutela", "artículo 14 y la Sección primera del Capítulo segundo", "preferencia y sumariedad"], solo=[2]),
  fichab("Tutela ordinaria de los derechos",
         "**Cualquier ciudadano**",
         ["Ante los **tribunales ordinarios**", "Por un procedimiento **preferente y sumario** (rápido y prioritario)"],
         "—",
         f"{IMP} Cubre el **art. 14 y la sección 1.ª** (arts. 15 a 29); **no** el resto del capítulo II. Después, y «en su caso», cabe el **amparo** ante el Tribunal Constitucional (→ V.3)."))}

{unidad("2.2 El procedimiento en la jurisdicción contencioso-administrativa",
  lit("LJCA", "a114", ["procedimiento de amparo judicial", "artículo 53.2 de la Constitución"], solo=[1], titulo="Artículo 114.1 (LJCA)"),
  lit("LJCA", "a115", ["diez días"], solo=[1], titulo="Artículo 115.1 (LJCA)"),
  "En el orden contencioso-administrativo, este procedimiento es el «**Procedimiento para la protección de los derechos fundamentales de la persona**» (LJCA, Título V, capítulo I) y tiene un **plazo de diez días** para recurrir.")}
""", 2)

T.ap("s21", "V.3 El recurso de amparo", f"""
Es **el último remedio**: normalmente se acude al Tribunal Constitucional **cuando ya se ha agotado la vía judicial** (el procedimiento preferente y sumario y los recursos que quepan). La excepción son los actos sin valor de ley de las Cortes o de las Asambleas autonómicas (art. 42 LOTC), que no tienen vía judicial previa.

{unidad("3.1 Qué derechos protege (arts. 53.2 y 161.1.b CE; art. 41 LOTC)",
  lit("CE", "a53", ["recurso de amparo ante el Tribunal Constitucional", "objeción de conciencia reconocida en el artículo 30"], solo=[2], titulo="Artículo 53.2 (amparo)"),
  lx("LOTC", "acuarentayuno", 41, ["artículos catorce a veintinueve de la Constitución", "objeción de conciencia reconocida en el artículo treinta"], solo=[1, 2]),
  fichab("Recurso de amparo constitucional",
         "Persona natural o jurídica con interés legítimo, **Defensor del Pueblo** y **Ministerio Fiscal** (art. 162.1.b CE; art. 46 LOTC)",
         ["Frente a violaciones de los derechos de los **arts. 14 a 29** y de la **objeción de conciencia (art. 30.2)**", "Por disposiciones, actos, omisiones o vía de hecho de los poderes públicos"],
         ["Plazos según el origen de la violación (→ 3.2)", "Se admite solo si tiene **especial trascendencia constitucional** (art. 50.1.b LOTC)"],
         f"{IMP} Amparo: **14 + 15 a 29 + 30.2**. Los derechos de la sección 2.ª (salvo el 30.2) y los principios del capítulo III **no** tienen amparo."))}

{unidad("3.2 Los plazos (arts. 42, 43 y 44 LOTC)",
  lx("LOTC", "acuarentaydos", 42, ["tres meses"]),
  lx("LOTC", "acuarentaytres", 43, ["agotado la vía judicial procedente", "veinte días"], solo=[1, 2]),
  lx("LOTC", "acuarentaycuatro", 44, ["Que se hayan agotado todos los medios de impugnación", "30 días"], solo=[1, 2, 3, 4, 5]),
  tabla(["Origen de la violación", "Plazo", "Desde cuándo", "Art. LOTC"], [
    ["Decisiones o actos **sin valor de ley** de las **Cortes** o de las **Asambleas legislativas de las CCAA** (o sus órganos)", "**3 meses**", "Desde que sean **firmes** según las normas internas de la Cámara o Asamblea", "**42**"],
    ["Actos u omisiones del **Gobierno** o de sus autoridades o funcionarios, o de los **órganos ejecutivos colegiados de las CCAA** (o sus autoridades o funcionarios)", "**20 días**", "Desde la notificación de la resolución del **previo proceso judicial** (tras agotar la vía judicial)", "**43**"],
    ["Acto u omisión de un **órgano judicial**", "**30 días**", "Desde la notificación de la resolución del proceso judicial (tras agotar los medios de impugnación)", "**44**"]]),
  f"!> {IMP} **Tres plazos, tres orígenes:** **3 meses** (Cortes y Asambleas), **20 días** (Gobierno y CCAA, tras la vía judicial) y **30 días** (órgano judicial, ¡con la vía judicial agotada!). Lo más preguntable es el de **30 días** y el de **20 días**.")}

{unidad("3.3 Quién lo interpone y cómo se admite (art. 46 y 50 LOTC)",
  lx("LOTC", "acuarentayseis", 46, ["la persona directamente afectada, el Defensor del Pueblo y el Ministerio Fiscal", "quienes hayan sido parte en el proceso judicial correspondiente, el Defensor del Pueblo y el Ministerio Fiscal"], solo=[1, 2, 3]),
  lx("LOTC", "acincuenta", 50, ["especial trascendencia constitucional"], solo=[1, 2, 3, 4, 5, 6], extra=".1"),
  "?> **Ojo:** el art. 46.1.a) remite a los arts. 42 y **45**, pero el art. 45 LOTC está **derogado** (el 46.1.a) lo sigue citando).")}
""", 2)
