
T.ap("s22", "V.4 El Defensor del Pueblo (art. 54)", f"""
{unidad("4.1 El art. 54",
  lit("CE", "a54", ["alto comisionado de las Cortes Generales", "los derechos comprendidos en este Título", "supervisar la actividad de la Administración"]),
  fichab("Garantía institucional de los derechos",
         "El **Defensor del Pueblo**, alto comisionado de las Cortes Generales",
         ["Defiende **los derechos comprendidos en el Título I** (arts. 10 a 52: todos los que haya en el título)", "Supervisa la actividad de la **Administración**, dando cuenta a las Cortes Generales"],
         "—",
         f"{IMP} Defiende **todo el Título I**, no solo la sección 1.ª. Su regulación va por **ley orgánica** (→ VIII)."))}

El Defensor del Pueblo tiene su propio apartado completo más adelante (→ VIII).
""", 2)

T.ap("s23", "V.5 El recurso de inconstitucionalidad", f"""
{unidad("5.1 Qué es y quién lo interpone (arts. 53.1, 161.1.a y 162.1.a CE; art. 32 LOTC)",
  lit("CE", "a161", ["recurso de inconstitucionalidad contra leyes y disposiciones normativas con fuerza de ley"], solo=[1, 2]),
  lit("CE", "a162", ["el Presidente del Gobierno, el Defensor del Pueblo, 50 Diputados, 50 Senadores, los órganos colegiados ejecutivos de las Comunidades Autónomas y, en su caso, las Asambleas de las mismas"], solo=[1, 2]),
  lx("LOTC", "atreintaydos", 32, ["El Presidente del Gobierno", "El Defensor del Pueblo", "Cincuenta Diputados", "Cincuenta Senadores", "previo acuerdo adoptado al efecto"]),
  fichab("Recurso de inconstitucionalidad ante el Tribunal Constitucional",
         ["**Presidente del Gobierno**", "**Defensor del Pueblo**", "**50 Diputados** y **50 Senadores**", "**Órganos ejecutivos** y **Asambleas** de las CCAA, solo contra leyes del Estado que afecten a su ámbito de autonomía"],
         "Contra **leyes y disposiciones normativas con fuerza de ley** (Estatutos, leyes orgánicas y ordinarias, decretos-leyes, decretos legislativos, tratados, reglamentos de las Cámaras)",
         ["**3 meses** desde la publicación de la norma (art. 33.1 LOTC)", "**9 meses** (Presidente del Gobierno y ejecutivos autonómicos) si hay Comisión Bilateral, acuerdo de negociaciones y este se comunica al Tribunal en los 3 primeros meses y se publica en el BOE y en el diario oficial de la Comunidad (art. 33.2 LOTC)"],
         "Protege **todo el capítulo II (arts. 14 a 38)** según el art. 53.1; pero el TC puede apoyar su fallo en **cualquier** precepto constitucional (art. 39.2 LOTC)."))}

{unidad("5.2 El plazo (art. 33 LOTC)",
  lx("LOTC", "atreintaytres", 33, ["tres meses", "nueve meses", "Comisión Bilateral de Cooperación"], solo=[1, 2, 3, 4, 5]),
  f"!> {IMP} **Plazo: 3 meses**, y **9 meses** si el Presidente del Gobierno o el ejecutivo autonómico han activado la **Comisión Bilateral** para negociar, y el acuerdo se comunica al Tribunal **dentro de los 3 meses siguientes a la publicación** y se publica en el BOE y en el diario oficial de la Comunidad (art. 33.2 LOTC). Se cuenta desde la **publicación** de la norma.")}
""", 2)

T.ap("s24", "V.6 Vinculación de los poderes públicos", f"""
{unidad("6.1 Todos los poderes públicos están vinculados",
  lit("CE", "a9", ["Los ciudadanos y los poderes públicos están sujetos a la Constitución"], solo=[1]),
  lit("CE", "a53", ["vinculan a todos los poderes públicos"], solo=[1]),
  fichab("Eficacia directa de los derechos del capítulo II",
         "**Todos los poderes públicos** (legislativo, ejecutivo, judicial y administraciones)",
         "Los derechos del **capítulo II** tienen **eficacia inmediata**: no necesitan una ley que los desarrolle para poder invocarse",
         "—",
         f"{IMP} **Vinculan** los derechos del **capítulo II (14 a 38)**. Los del **capítulo III** no vinculan igual: **informan** (→ V.7.2)."))}
""", 2)

T.ap("s25", "V.7 La paradoja del capítulo III: principios rectores", f"""
El {tag("I.3", "capítulo III")} se llama «**De los principios rectores de la política social y económica**» y contiene cosas tan importantes como la **salud**, la **vivienda**, la **seguridad social** o el **medio ambiente**. Pero tiene una paradoja: **son principios que parecen derechos, pero con poca garantía**.

{unidad("7.1 El art. 53.3",
  lit("CE", "a53", ["informarán la legislación positiva, la práctica judicial y la actuación de los poderes públicos", "Sólo podrán ser alegados ante la Jurisdicción ordinaria de acuerdo con lo que dispongan las leyes que los desarrollen"], solo=[3]),
  fichab("Principios rectores del capítulo III",
         "Los **poderes públicos**",
         ["**Informan** la legislación positiva, la práctica judicial y la actuación de los poderes públicos", "Solo se **alegan ante la jurisdicción ordinaria** según las leyes que los desarrollen"],
         "Sin amparo ni tutela preferente y sumaria; solo se alegan ante la jurisdicción ordinaria según las leyes que los desarrollen (53.3); entre las garantías específicas del Título I, solo les alcanza el **Defensor del Pueblo** (art. 54)",
         f"{IMP} **A diferencia** de los derechos del capítulo II, **no pueden exigirse sin una ley que los desarrolle**. Si no hay ley, aunque lo diga la Constitución, no hay acción."))}

{IMP} **Trampa típica:** te presentan como «derechos fundamentales» la **salud** (43), la **vivienda** (47), la **distribución de la renta regional y personal más equitativa** (40) o la **propiedad privada** (33). **No lo son**: los tres primeros son principios del capítulo III; la propiedad privada es un derecho de la sección 2.ª (sin amparo). El **derecho al trabajo** (35), también de la sección 2.ª, tampoco es fundamental.
""", 2)

T.ap("s26", "V.8 Cuadro resumen de las garantías", f"""
{tabla(["Mecanismo", "Qué protege", "Norma", "Quién / ante quién"], [
  ["**Reserva de ley orgánica**", f"{tag('I.2.1', 'Sección 1.ª')} (15-29)", "Art. 81.1", "Cortes Generales; mayoría absoluta del Congreso"],
  ["**Reserva de ley**", f"{tag('I.2', 'Capítulo II')} (14-38), respetando el contenido esencial", "Art. 53.1", "Ley (nunca reglamento)"],
  ["**Tutela ante los tribunales ordinarios** (preferente y sumaria)", f"{tag('I.2', 'Art. 14')} + {tag('I.2.1', 'sección 1.ª')} (14-29)", "Art. 53.2", "Cualquier ciudadano · tribunales ordinarios"],
  ["**Recurso de amparo**", f"{tag('I.2', 'Art. 14')} + {tag('I.2.1', 'sección 1.ª')} + {tag('I.2.2', 'art. 30.2')} (14-29 y 30.2)", "Arts. 53.2 y 161.1.b", "Persona con interés legítimo, Defensor del Pueblo, Ministerio Fiscal · TC"],
  ["**Defensor del Pueblo**", f"{tag('I', 'Título I')} (10-52)", "Art. 54", "Alto comisionado de las Cortes Generales"],
  ["**Recurso de inconstitucionalidad**", f"{tag('I.2', 'Capítulo II')} (14-38)", "Arts. 53.1 y 161.1.a", "Presidente del Gobierno, Defensor del Pueblo, 50 Diputados, 50 Senadores, ejecutivos y asambleas autonómicas · TC"],
  ["**Vinculación de los poderes públicos**", f"{tag('I.2', 'Capítulo II')} (14-38)", "Art. 53.1", "Todos los poderes públicos"]])}

{IMP} **Entre las garantías de este cuadro, al capítulo III (39-52) solo le alcanza el Defensor del Pueblo** (art. 54): sus principios **informan** la actuación de los poderes públicos y se alegan ante la jurisdicción ordinaria según las leyes que los desarrollen (art. 53.3). No hay amparo ni tutela preferente y sumaria; y, aunque no tienen un recurso propio, una ley contraria a ellos sí puede impugnarse por inconstitucionalidad, porque el Tribunal puede fundar su fallo en cualquier precepto constitucional (art. 39.2 LOTC).
""", 2)

# =============================================================================
# VI. SUSPENSIÓN
T.ap("bVI", "VI. ¿Cómo se suspenden los derechos? Estados de alarma, excepción y sitio (arts. 55 y 116)", donde(
  "Cuarta pregunta. La Constitución protege los derechos, pero **se reserva la carta de poder suspenderlos** en situaciones graves. Es el art. 55 (capítulo V, el último del Título I). " + IMP + " **Es muy preguntable: se pregunta por palabras clave y hay que dominarlo bien.**",
  ["1 El art. 55, ordenado", "2 Los tres estados: quién declara y cuánto dura", "3 Qué derechos se pueden suspender", "4 Puntos en común", "5 La suspensión individual (art. 55.2)", "6 Cuadro resumen"]))

T.ap("s27", "VI.1 El art. 55, ordenado", f"""
El art. 55 es un artículo «lioso»: dice «los derechos reconocidos en los artículos 17, 18, apartados 2 y 3, artículos 19…». Leído así no se entiende. Por eso conviene **ordenarlo**: lo que dice, en dos bloques.

{lit("CE", "a55", ["podrán ser suspendidos cuando se acuerde la declaración del estado de excepción o de sitio", "Se exceptúa de lo establecido anteriormente el apartado 3 del artículo 17 para el supuesto de declaración de estado de excepción", "Una ley orgánica podrá determinar", "bandas armadas o elementos terroristas"], solo=[1, 2, 3])}

{tabla(["", "Suspensión **general** (art. 55.1)", "Suspensión **individual** (art. 55.2)"], [
  ["**Cuándo**", "Al **declararse** el estado de **excepción o de sitio**", "**Ley orgánica**, para **personas determinadas**"],
  ["**Alcance**", "**General** (la guía M101 la llama «suspensión general»): se aplica en el ámbito de la declaración", "**Individual**: solo en relación con la actuación de **bandas armadas o elementos terroristas**"],
  ["**Derechos**", "**17**, **18.2**, **18.3**, **19**, **20.1.a)**, **20.1.d)**, **20.5**, **21**, **28.2** y **37.2** (salvo el **17.3** en excepción)", "**17.2**, **18.2** y **18.3**"],
  ["**Garantías**", "Declaración del estado en los términos de la Constitución (art. 116)", "**Intervención judicial** necesaria y **control parlamentario** adecuado"]])}

!> {IMP} **Es el artículo 55 de la Constitución y el capítulo es el quinto**: el art. **55** está en el capítulo **V**, el último del Título I. Las dos cifras son un cinco (5-5).
""", 2)

T.ap("s28", "VI.2 Los tres estados: quién declara y cuánto dura (art. 116)", f"""
Hay **tres estados**, de menor a mayor gravedad: **alarma < excepción < sitio**. La Constitución solo regula lo esencial (art. 116) y **una ley orgánica** lo desarrolla: la **LO 4/1981**.

{lit("CE", "a116", ["Una ley orgánica regulará los estados de alarma, de excepción y de sitio"], solo=[1], titulo="Artículo 116.1")}

{tabla(["", f"{tag('IV', 'ALARMA')}", f"{tag('I.5', 'EXCEPCIÓN')}", f"{tag('X', 'SITIO')}"], [
  ["**Quién declara**", "El **Gobierno**, por **decreto** del Consejo de Ministros", "El **Gobierno**, por **decreto** del Consejo de Ministros, **previa autorización del Congreso**", "El **Congreso**, por **mayoría absoluta**, **a propuesta exclusiva del Gobierno**"],
  ["**Papel del Congreso**", "Se le **da cuenta** (reunido inmediatamente)", "**Autoriza** antes", "**Declara**"],
  ["**Duración**", "**No más de 15 días**", "**No más de 30 días**", "**La que determine el Congreso**"],
  ["**Prórroga**", "Solo con **autorización** del Congreso", "**Otro plazo igual** (30 días), con los **mismos requisitos**", "La que fije el Congreso"],
  ["**Derechos**", "**No se suspende ninguno** (solo limitaciones)", "Se **suspenden** los del art. 55.1, **salvo el 17.3**", "Se **suspenden** los del art. 55.1, **incluido el 17.3**"],
  ["**Artículos**", "CE 116.2; LO 4/1981, arts. 4 a 12", "CE 116.3; LO 4/1981, arts. 13 a 31", "CE 116.4; LO 4/1981, arts. 32 a 36"]])}

{unidad("2.1 Estado de alarma (art. 116.2 CE; art. 6 LO 4/1981)",
  lit("CE", "a116", ["declarado por el Gobierno mediante decreto acordado en Consejo de Ministros por un plazo máximo de quince días", "dando cuenta al Congreso de los Diputados", "sin cuya autorización no podrá ser prorrogado dicho plazo"], solo=[2], titulo="Artículo 116.2"),
  lx("LOEAS", "asexto", 6, ["decreto acordado en Consejo de Ministros", "no podrá exceder de quince días", "Sólo se podrá prorrogar con autorización expresa del Congreso de los Diputados"], solo=[1, 2]),
  lx("LOEAS", "acuao", 4, ["Catástrofes, calamidades o desgracias públicas", "Crisis sanitarias", "Paralización de servicios públicos esenciales", "desabastecimiento de productos de primera necesidad"], solo=[1, 2, 3, 4, 5]),
  lx("LOEAS", "aonce", 11, ["Limitar la circulación o permanencia de personas o vehículos", "requisas temporales", "prestaciones personales obligatorias"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Estado de alarma",
         ["**Gobierno** (decreto del Consejo de Ministros)", "El Presidente de la CA puede **solicitarlo** si solo afecta a su territorio (art. 5 LO 4/1981)"],
         ["Se declara ante **catástrofes, crisis sanitarias, paralización de servicios esenciales o desabastecimiento** (art. 4 LO 4/1981)", "El decreto determina **ámbito territorial, duración y efectos**", "Admite **limitaciones** (circulación, requisas, prestaciones, intervención de industrias, racionamiento…), **no suspensión de derechos**"],
         ["**15 días**", "Prórroga **solo con autorización expresa del Congreso**, que puede fijar el alcance y las condiciones"],
         f"{IMP} En el alarma el Gobierno **da cuenta** al Congreso, pero **la prórroga necesita su autorización**. **Ningún derecho se suspende**: solo se **limitan** algunos."))}

{unidad("2.2 Estado de excepción (art. 116.3 CE; art. 13 LO 4/1981)",
  lit("CE", "a116", ["previa autorización del Congreso de los Diputados", "que no podrá exceder de treinta días, prorrogables por otro plazo igual, con los mismos requisitos"], solo=[3], titulo="Artículo 116.3"),
  lx("LOEAS", "atrece", 13, ["solicitar del Congreso de los Diputados autorización para declarar el estado de excepción", "que no podrá exceder de treinta días"], solo=[1, 2, 3, 4, 5, 6, 7]),
  fichab("Estado de excepción",
         ["**Gobierno** (decreto en Consejo de Ministros) **con autorización previa del Congreso**", "El Congreso puede aprobar la solicitud **o modificarla**"],
         ["Se declara cuando el ejercicio de los **derechos y libertades**, las **instituciones democráticas**, los **servicios públicos esenciales** u otro aspecto del **orden público** estén tan alterados que las potestades ordinarias no basten", "La solicitud al Congreso incluye los **derechos cuya suspensión se pide** (solo los del art. 55.1), las medidas, el ámbito y la duración"],
         ["**30 días**", "Prorrogable por **otro plazo igual**, con los **mismos requisitos**"],
         f"{IMP} Declara el **Gobierno**, pero **con autorización previa del Congreso** (en alarma, el Congreso solo recibe cuenta). La autorización y la proclamación deben **determinar los efectos, el ámbito territorial y la duración**."))}

{unidad("2.3 Estado de sitio (art. 116.4 CE; art. 32 LO 4/1981)",
  lit("CE", "a116", ["declarado por la mayoría absoluta del Congreso de los Diputados, a propuesta exclusiva del Gobierno", "El Congreso determinará su ámbito territorial, duración y condiciones"], solo=[4], titulo="Artículo 116.4"),
  lx("LOEAS", "atreintaydos", 32, ["podrá proponer al Congreso de los Diputados la declaración de estado de sitio", "determinará el ámbito territorial, duración y condiciones", "suspensión temporal de las garantías jurídicas del detenido"], solo=[1, 2, 3]),
  fichab("Estado de sitio",
         "**El Congreso**, por **mayoría absoluta**, y solo **a propuesta del Gobierno**",
         ["Se declara ante una **insurrección o acto de fuerza** contra la soberanía o independencia de España, su integridad territorial o el ordenamiento constitucional, que no pueda resolverse por otros medios", "Puede suspender, además, las **garantías jurídicas del detenido** (art. 17.3)"],
         ["**La que determine el Congreso**", "El Congreso fija también el ámbito territorial y las condiciones"],
         f"{IMP} En el sitio **declara el Congreso** (en los otros dos, el Gobierno). Es el **único** en que se pueden suspender las garantías del detenido (**17.3**)."))}

!> {IMP} **Fíjate bien en «quién declara» y «cómo»:** **alarma** → Gobierno, *dando cuenta* al Congreso; **excepción** → Gobierno, *con autorización previa* del Congreso; **sitio** → Congreso, *mayoría absoluta*, *a propuesta exclusiva* del Gobierno. Todo se mueve **entre Gobierno y Congreso**.

**Regla mnemotécnica: 15 – 30 – lo decide el Congreso.** Alarma, 15 días; excepción, 30 días (+30); sitio, el tiempo que decida el Congreso.

### La gradación: el peso pasa del Gobierno al Congreso [[M107]]

La clave para ordenar los tres estados es verlos como una **escala de gravedad** (alarma < excepción < sitio) en la que **el poder de decidir se desplaza** del Gobierno al Congreso. Y siempre es un **diálogo entre Gobierno y Congreso**: ni el **Senado** ni las **Cortes Generales** en su conjunto intervienen en la declaración (los apartados 2 a 4 del art. 116 solo nombran al Gobierno y al Congreso).

{tabla(["", "Alarma", "Excepción", "Sitio"], [
  ["**Quién decide**", "**Gobierno**; el Congreso solo recibe **cuenta**", "**Gobierno**, con **autorización previa** del Congreso", "**Congreso** (mayoría absoluta), a propuesta exclusiva del Gobierno"],
  ["**Duración**", "**15 días**; dentro del tope, la fija el Gobierno", "**30 días**: el **doble**, porque el problema es más grave", "La que **determine el Congreso**"],
  ["**Prórroga**", "Con **autorización del Congreso**; la Constitución no fija el plazo de la prórroga", "**Otro plazo igual** (30 días) y con los **mismos requisitos**: es más rígida", "La del propio Congreso"],
  ["**Dependencia del Gobierno**", "Mínima: solo necesita al Congreso para **prorrogar**", "Mayor: necesita al Congreso **desde el principio** y cada 30 días", "Total: **decide el Congreso**"]])}

?> **Comentario del vídeo (no es texto legal).** Como la prórroga del estado de alarma solo exige la autorización del Congreso y no un plazo máximo propio, el vídeo recuerda que la **pandemia** se gestionó con la alarma y no con la excepción, aunque esta fuera «más apropiada» para limitar ciertos derechos: así el Gobierno no dependía del Congreso **cada 30 días**. El propio vídeo advierte de que es una **especulación**: lo que hay que retener es el cuadro.

{IMP} **Alarma = limitar, no suspender.** El vídeo recuerda que el decreto del estado de alarma de la pandemia fue **recurrido ante el Tribunal Constitucional** y que se declararon **inconstitucionales** algunas de sus medidas, sobre todo las que afectaban a la **libertad de circulación** y al **derecho de reunión**, porque en la práctica equivalían a una **suspensión** de esos derechos, que la alarma no permite (solo caben **limitaciones**). [[M107]] *(Comentario del vídeo, sin cita de sentencia: la referencia exacta de las resoluciones del Tribunal queda pendiente de la fuente oficial.)*
""", 2)
