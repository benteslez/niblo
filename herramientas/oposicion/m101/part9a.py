
# =============================================================================
# VIII. DEFENSOR DEL PUEBLO
T.ap("bVIII", "VIII. El Defensor del Pueblo (art. 54)", donde(
  "Octava pregunta. El Defensor del Pueblo es la **garantía institucional** de los derechos del Título I. Se estudia el art. 54 y la **LO 3/1981**: cómo se elige, cuánto dura su mandato, qué puede investigar y qué recursos puede interponer.",
  ["1 Qué es", "2 Requisitos y elección", "3 Mandato, adjuntos y estatuto", "4 Funciones y actuación"]))

T.ap("s39", "VIII.1 Qué es el Defensor del Pueblo", f"""
Según el módulo, tiene **cierta inspiración nórdica** (el *ombudsman*). Sus **aspectos constitucionales** son cuatro:

{unidad("1.1 El art. 54 CE y el art. 1 de su ley orgánica",
  lit("CE", "a54", ["alto comisionado de las Cortes Generales", "los derechos comprendidos en este Título", "supervisar la actividad de la Administración, dando cuenta a las Cortes Generales"]),
  lx("LODP", "aprimero", 1, ["alto comisionado de las Cortes Generales", "defensa de los derechos comprendidos en el Título I de la Constitución", "supervisar la actividad de la Administración, dando cuenta a las Cortes Generales"]),
  fichab("Defensor del Pueblo",
         "**Alto comisionado de las Cortes Generales**, **designado por éstas**",
         ["**Defiende todos los derechos del Título I** de la Constitución", "**Supervisa la actividad de la Administración**, dando cuenta a las Cortes Generales", "Regulado por **ley orgánica** (LO 3/1981)"],
         "—",
         f"{IMP} Es un comisionado de las **Cortes Generales** (no del Gobierno) y defiende **todo el Título I**, no solo la sección 1.ª."))}
""", 2)

T.ap("s40", "VIII.2 Requisitos y elección", f"""
{unidad("2.1 Requisitos (art. 3 LO 3/1981)",
  lx("LODP", "atercero", 3, ["cualquier español mayor de edad", "pleno disfrute de sus derechos civiles y políticos"]),
  tabla(["Requisito", "Contenido"], [["**Nacionalidad**", "**Español**"], ["**Edad**", "**Mayor de edad**"], ["**Capacidad**", "**Pleno disfrute de sus derechos civiles y políticos**"]]))}

{unidad("2.2 La elección (art. 2 LO 3/1981)",
  lx("LODP", "asegundo", 2, ["Comisión Mixta Congreso-Senado", "tres quintas partes de los miembros del Congreso", "veinte días", "mayoría absoluta del Senado", "cinco años"], solo=[1, 2, 3, 4, 5, 6]),
  tabla(["Paso", "Qué ocurre", "Mayoría"], [
    ["**1.º**", "La **Comisión Mixta Congreso-Senado** se reúne y **propone** al candidato o candidatos a los Plenos", "**Mayoría simple** (acuerdos de la Comisión)"],
    ["**2.º · Votación A**", "El **Pleno del Congreso** elige; después, el **Senado ratifica** en un plazo máximo de **20 días**", "**3/5 del Congreso** y **3/5 del Senado**"],
    ["**2.º · Votación B** (si no se alcanzan esas mayorías)", "Nueva sesión de la Comisión, que formula sucesivas propuestas **en el plazo máximo de un mes**", "**3/5 del Congreso** y **mayoría absoluta del Senado**"],
    ["**3.º**", "Los **Presidentes del Congreso y del Senado acreditan conjuntamente con sus firmas** el nombramiento, que se publica en el **BOE**; toma posesión ante las **Mesas de ambas Cámaras** reunidas", "—"]]),
  f"!> {IMP} En el Congreso siempre **3/5**; en el Senado, **3/5** la primera vez y **mayoría absoluta** si hay que repetir. El **Presidente del Congreso y el del Senado** firman **conjuntamente** el nombramiento.")}

{unidad("2.3 El nombramiento y la toma de posesión (art. 4 LO 3/1981)",
  lx("LODP", "acuao", 4, ["acreditarán conjuntamente con sus firmas el nombramiento", "Mesas de ambas Cámaras reunidas conjuntamente"]))}

{unidad("2.4 La excepción del Defensor: el cargo que no nombra el Rey",
  "Si repasas los cargos que has visto en este bloque, descubrirás una regla muy útil: **casi todos los nombramientos constitucionales los firma el Rey**, aunque la propuesta venga de otro órgano. Los **doce Magistrados del Tribunal Constitucional**, por ejemplo, son «nombrados por el Rey» a propuesta del Congreso, del Senado, del Gobierno y del Consejo General del Poder Judicial (art. 159.1 CE), y su Presidente también (art. 160 CE). El **Defensor del Pueblo es la excepción**: lo **eligen las Cortes Generales** y su nombramiento lo **acreditan conjuntamente con sus firmas los Presidentes del Congreso y del Senado** (art. 4 LO 3/1981), con publicación en el BOE. Sin Rey. Por eso, ante una pregunta que mencione al Defensor, piensa: *«la regla es el Rey; el Defensor es la excepción»*. [[M101]]",
  f"!> {IMP} **Trampa típica:** que el Defensor del Pueblo lo «nombra el Rey a propuesta de las Cortes». Es **falso**: lo nombran, **conjuntamente, los Presidentes del Congreso y del Senado**.",
  "Y no te líes con la elección: aunque se parezca al «plan B» de la reforma constitucional, **no es lo mismo** (→ tema I.1 · IV.6). Aquí, si no se alcanza el 3/5 en el Senado, basta con su **mayoría absoluta** (art. 2.5), **una vez lograda la mayoría de 3/5 en el Congreso**.")}
""", 2)

T.ap("s41", "VIII.3 Mandato, adjuntos y estatuto", f"""
{unidad("3.1 Mandato y cese (arts. 2.1 y 5 LO 3/1981)",
  lx("LODP", "aquinto", 5, ["Por renuncia", "Por expiración del plazo de su nombramiento", "Por muerte o por incapacidad sobrevenida", "Por actuar con notoria negligencia", "condenado, mediante sentencia firme, por delito doloso"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Mandato del Defensor del Pueblo",
         "Las **Cortes Generales**",
         "Cesa por **renuncia**, **expiración del plazo**, **muerte o incapacidad**, **notoria negligencia** o **condena firme por delito doloso**",
         ["**5 años**", "La vacante por muerte, renuncia y expiración la declara el **Presidente del Congreso**; en los demás casos, **3/5 de cada Cámara**"],
         "El módulo anota que el mandato es reelegible; la ley orgánica **no regula** la reelección."))}

{unidad("3.2 Los adjuntos (art. 8 LO 3/1981)",
  lx("LODP", "aoctavo", 8, ["Adjunto Primero y un Adjunto Segundo", "El Defensor del Pueblo nombrará y separará a sus Adjuntos previa conformidad de las Cámaras"], solo=[1, 2]),
  "**Dos adjuntos** (**primero** y **segundo**), **nombrados por él** con la **conformidad previa** de las Cámaras (la Comisión Mixta, art. 2.6). Lo sustituyen **por su orden**.")}

{unidad("3.3 Independencia e inviolabilidad (art. 6 LO 3/1981)",
  lx("LODP", "asexto", 6, ["no estará sujeto a mandato imperativo alguno", "No recibirá instrucciones de ninguna Autoridad", "gozará de inviolabilidad"], solo=[1, 2]))}

{unidad("3.4 Incompatibilidades (art. 7 LO 3/1981)",
  lx("LODP", "aseptimo", 7, ["incompatible con todo mandato representativo", "con la afiliación a un partido político"], solo=[1]))}
""", 2)

T.ap("s42", "VIII.4 Funciones y actuación", f"""
{tabla(["Aspecto", "Qué dice", "Norma"], [
  ["**Qué supervisa**", "La actividad de la **Administración** (del Estado y también de las **Comunidades Autónomas**, aunque estas pueden tener sus propios defensores)", "Art. 54 CE; arts. 9 y 12 LO 3/1981"],
  ["**Quién puede dirigirse a él**", "**Toda persona natural o jurídica** con interés legítimo, sin restricción de nacionalidad, residencia, sexo, minoría de edad… · **Diputados y Senadores** individualmente · **comisiones de investigación** · la **Comisión Mixta Congreso-Senado**", "Art. 10"],
  ["**Quién no**", "**Ninguna autoridad administrativa** en asuntos de su competencia", "Art. 10.3"],
  ["**Cómo actúa**", "De **oficio** o a **petición de parte**; **investigación sumaria e informal**; la Administración informa en **15 días**", "Arts. 9.1 y 18.1"],
  ["**Plazo para la queja**", "**Un año** desde que se conocen los hechos; es **gratuita** y no necesita abogado ni procurador", "Art. 15"],
  ["**Recursos**", "Está legitimado para interponer **recurso de inconstitucionalidad** y **recurso de amparo**", "Art. 29; CE 162.1"],
  ["**Resultado**", "Puede formular **advertencias, recomendaciones, recordatorios y sugerencias**; **no puede modificar ni anular** los actos de la Administración", "Arts. 28 y 30"],
  ["**Informes**", "Da cuenta **anualmente** a las Cortes Generales", "Art. 32"]])}

{unidad("4.1 Investigación y límites",
  lx("LODP", "adiez", 10, ["toda persona natural o jurídica que invoque un interés legítimo", "Los Diputados y Senadores individualmente", "las comisiones de investigación", "la Comisión Mixta Congreso-Senado de relaciones con el Defensor del Pueblo", "No podrá presentar quejas ante el Defensor del Pueblo ninguna autoridad administrativa"], solo=[1, 2, 3]),
  lx("LODP", "adieciocho", 18, ["investigación sumaria e informal", "quince días"], solo=[1]),
  lx("LODP", "aveintinueve", 29, ["recursos de inconstitucionalidad y de amparo"]),
  lx("LODP", "aquince", 15, ["en el plazo máximo de un año"], solo=[1]))}

{unidad("4.2 Admisión y rechazo de las quejas (art. 17 LO 3/1981)",
  "Una vez registrada la queja, el Defensor decide si **la tramita o la rechaza**. Si la rechaza, debe hacerlo **en escrito motivado** y puede orientar al interesado sobre las vías que considere más oportunas. Lo que más se pregunta es **qué quejas rechaza**: las **anónimas** las rechaza **siempre** («rechazará»); las demás, si lo estima oportuno («podrá rechazar»), cuando advierta **mala fe**, **carencia de fundamento**, **inexistencia de pretensión** o cuando su tramitación **perjudique el legítimo derecho de un tercero**. Y una regla de cierre que no conviene olvidar: **sus decisiones no son recurribles**. [[M106]]",
  lx("LODP", "adiecisiete", 17, ["registrará y acusará recibo de las quejas", "en escrito motivado", "rechazará las quejas anónimas", "mala fe, carencia de fundamento, inexistencia de pretensión", "tercera persona", "Sus decisiones no serán susceptibles de recurso"], solo=[1, 3]),
  tabla(["Queja", "Qué hace el Defensor", "Cómo se recuerda"], [
    ["**Anónima**", "**La rechaza** (obligatorio)", "«Rechazará»"],
    ["Mala fe · sin fundamento · sin pretensión · perjuicio a un tercero", "**Puede rechazarla**", "«Podrá rechazar»: cuatro supuestos"],
    ["Pendiente de resolución judicial", "No entra en el examen individual y lo **suspende** si luego se acude a los tribunales (sí puede investigar los problemas generales)", "Art. 17.2"],
    ["Cualquier decisión de admisión o rechazo", "**No cabe recurso**", "Art. 17.3"]]),
  f"?> **Trampa típica:** «el Defensor **podrá** rechazar las quejas anónimas» (falso: las **rechaza siempre**) o «sus decisiones son recurribles ante…» (falso: **no son susceptibles de recurso**).")}

!> {IMP} **Para el examen:** el Defensor puede interponer **a la vez** amparo e inconstitucionalidad; su investigación es **sumaria e informal**; supervisa también a las **CCAA**; los **estados de excepción o sitio no interrumpen** su actividad (art. 11.3, sin perjuicio del art. 55 CE).
""", 2)

T.ap("s43", "VIII.5 Resumen del Defensor del Pueblo", resumen([
  "**Alto comisionado** de las Cortes Generales; defiende los derechos del **Título I** y supervisa la **Administración** (estatal y autonómica); ley orgánica.",
  "**Requisitos:** español, mayor de edad, pleno disfrute de derechos civiles y políticos.",
  "**Elección:** Comisión Mixta propone → **3/5 Congreso** y ratificación **3/5 Senado** (20 días) → si no, **3/5 Congreso + mayoría absoluta Senado** → firma conjunta de los Presidentes y **BOE**.",
  "**5 años**; **dos adjuntos** nombrados por él; **investigación sumaria e informal**; puede interponer **amparo e inconstitucionalidad**.",
  "**Quejas:** plazo de **1 año**; **rechaza siempre las anónimas** y puede rechazar las de mala fe, sin fundamento, sin pretensión o que perjudiquen a un tercero; **sus decisiones no son recurribles**."], "Siguiente: IX. La reforma de la Constitución (Título X)"), 2)
