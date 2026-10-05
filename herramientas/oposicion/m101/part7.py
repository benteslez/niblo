
T.ap("s29", "VI.3 Qué derechos se pueden suspender en cada estado", f"""
El art. 55.1 enumera los derechos **suspendibles** y el art. 116 dice que solo en **excepción y sitio**. Combinando ambos:

{tabla(["Derecho (art.)", "Alarma", "Excepción", "Sitio"], [
  ["**17** · Libertad y seguridad (detención…)", NO, SI, SI],
  ["**17.3** · Derechos del detenido (información, no declarar, abogado)", NO, f"**{NO}**", f"**{SI}**"],
  ["**18.2** · Inviolabilidad del domicilio", NO, SI, SI],
  ["**18.3** · Secreto de las comunicaciones", NO, SI, SI],
  ["**19** · Libertad de residencia y de circulación", NO, SI, SI],
  ["**20.1.a)** y **d)** · Libertad de expresión e información", NO, SI, SI],
  ["**20.5** · Secuestro de publicaciones solo por resolución judicial", NO, SI, SI],
  ["**21** · Derecho de reunión y manifestación", NO, SI, SI],
  ["**28.2** · Huelga", NO, SI, SI],
  ["**37.2** · Conflicto colectivo", NO, SI, SI]])}

{IMP} **El matiz del 17.3.** El art. 55.1 exceptúa el **apartado 3 del art. 17** «para el supuesto de declaración de estado de excepción». Es decir: en **excepción** el detenido **conserva** sus garantías (información inmediata, no ser obligado a declarar, abogado); en **sitio** pueden **suspenderse**.

{unidad("3.1 Por qué importa el 17.3: lo que dice el art. 17.3",
  lit("CE", "a17", ["Toda persona detenida debe ser informada de forma inmediata", "no pudiendo ser obligada a declarar", "asistencia de abogado"], solo=[3]),
  lx("LOEAS", "adieciseis", 16, ["La detención no podrá exceder de diez días", "los derechos que les reconoce el artículo diecisiete, tres, de la Constitución"], solo=[1]))}

Dos ideas para ayudarte a recordar la lista: **tiene sentido** que se puedan restringir justo estas libertades (circulación, reunión, huelga, comunicaciones, domicilio…) cuando el problema es de **orden público**; no se limitan «a tochomocho».

*Alarma no suspende derechos:* el decreto de alarma solo permite **limitaciones**, como limitar la circulación, requisar bienes o racionar servicios (→ VI.2, art. 11 LO 4/1981).
""", 2)

T.ap("s30", "VI.4 Puntos en común de los tres estados", f"""
{tabla(["Regla", "Qué dice", "Norma"], [
  ["**Ámbito territorial**", "No está preestablecido: lo **determina cada declaración** (decreto o autorización/declaración del Congreso)", "CE 116.2, 116.3 y 116.4"],
  ["**Congreso**", "**No puede disolverse** mientras dure el estado; si no estaba reunido, las Cámaras **quedan convocadas automáticamente**", "CE 116.5"],
  ["**Congreso disuelto o mandato expirado**", "Sus competencias las asume la **Diputación Permanente**", "CE 116.5"],
  ["**Funcionamiento**", "El de las Cámaras y el de los demás poderes constitucionales **no se interrumpe**", "CE 116.5; LO 4/1981, art. 1.4"],
  ["**Responsabilidad**", "No se modifica el principio de **responsabilidad del Gobierno y de sus agentes**", "CE 116.6"],
  ["**Publicación**", "Se publica **de inmediato en el BOE** y se difunde obligatoriamente por medios públicos y los privados que se determinen; **entra en vigor desde el instante de su publicación**", "LO 4/1981, art. 2"],
  ["**Reforma constitucional**", "**No puede iniciarse** durante ninguno de los tres estados (ni en tiempo de guerra)", "CE 169"],
  ["**Regulación**", "Por **ley orgánica**", "CE 116.1"]])}

{lit("CE", "a116", ["No podrá procederse a la disolución del Congreso", "quedando automáticamente convocadas las Cámaras", "no podrán interrumpirse", "las competencias del Congreso serán asumidas por su Diputación Permanente"], solo=[5, 6], titulo="Artículo 116.5")}

{lit("CE", "a116", ["no modificarán el principio de responsabilidad del Gobierno y de sus agentes"], solo=[7], titulo="Artículo 116.6")}

{lx("LOEAS", "asegundo", 2, ["publicada de inmediato en el «Boletín Oficial del Estado»", "difundida obligatoriamente por todos los medios de comunicación públicos y por los privados que se determinen", "entrará en vigor desde el instante mismo de su publicación"])}

{lit("CE", "a169", ["No podrá iniciarse la reforma constitucional en tiempo de guerra o de vigencia de alguno de los estados previstos en el artículo 116"])}

!> {IMP} **Para el examen:** no se puede **disolver el Congreso**, no se **interrumpe** el funcionamiento de las Cámaras ni de los poderes del Estado, no se modifica la **responsabilidad** de los poderes públicos, **no se puede reformar la Constitución** (ni siquiera en alarma) y todo se regula por **ley orgánica**.
""", 2)

T.ap("s31", "VI.5 La suspensión individual (art. 55.2)", f"""
Además de la suspensión general, el art. 55.2 permite una suspensión **individual** de algunos derechos, **para personas determinadas** y en relación con las investigaciones de la actuación de **bandas armadas o elementos terroristas**.

{tabla(["Derecho", "Qué se puede suspender", "Garantía"], [
  [tag("I.2.1", "Art. 17.2"), "La **duración máxima de la detención preventiva** (72 horas)", "**Intervención judicial** y **control parlamentario**"],
  [tag("I.2.1", "Art. 18.2"), "La **inviolabilidad del domicilio**", "Ley **orgánica**"],
  [tag("I.2.1", "Art. 18.3"), "El **secreto de las comunicaciones**", "Responsabilidad **penal** por uso injustificado o abusivo"]])}

{lit("CE", "a55", ["Una ley orgánica podrá determinar la forma y los casos en los que, de forma individual y con la necesaria intervención judicial y el adecuado control parlamentario", "La utilización injustificada o abusiva de las facultades reconocidas en dicha ley orgánica producirá responsabilidad penal"], solo=[2, 3], titulo="Artículo 55.2")}

!> {IMP} La suspensión individual afecta **solo** a tres derechos (**17.2, 18.2 y 18.3**), a diferencia de la general, que afecta a diez. Y siempre **con intervención judicial y control parlamentario**.
""", 2)

T.ap("s32", "VI.6 Cuadro resumen de la suspensión", f"""
{tabla(["Clase", "Supuesto", "Declaración", "Duración", "Derechos que se pueden suspender"], [
  ["**Suspensión general**", f"{tag('I.5', 'Excepción')}", "**Gobierno**, con **autorización del Congreso**", "**30 días**; prórroga por otro plazo igual", "**17** (salvo 17.3) · **18.2** · **18.3** · **19** · **20.1.a)** y **d)** y **20.5** · **21** · **28.2** · **37.2**"],
  ["**Suspensión general**", f"{tag('X', 'Sitio')}", "**Congreso**, mayoría absoluta, a propuesta exclusiva del Gobierno", "La determinada por el **Congreso**", "Los mismos **más el 17.3**"],
  ["**Limitación**", f"{tag('IV', 'Alarma')}", "**Gobierno**, dando cuenta al Congreso", "**15 días**; prórroga con autorización del Congreso", "**Ninguno** (solo se pueden decretar algunas limitaciones)"],
  ["**Suspensión individual**", "Bandas armadas y elementos terroristas (art. 55.2)", "Ley orgánica", "—", "**17.2** (duración máxima de la detención preventiva) · **18.2** · **18.3**"]])}

{resumen([
  "**Art. 55** (capítulo V): suspensión **general** (excepción y sitio: diez derechos, salvo el 17.3 en excepción) e **individual** (bandas armadas y terroristas: 17.2, 18.2, 18.3).",
  "**Quién declara:** alarma → Gobierno (da cuenta); excepción → Gobierno con autorización del Congreso; sitio → Congreso por mayoría absoluta a propuesta del Gobierno.",
  "**Duración:** alarma 15 días; excepción 30 (+30); sitio, la que fije el Congreso.",
  "**En común:** no se disuelve el Congreso, no se interrumpe el funcionamiento de las Cámaras, no se modifica la responsabilidad, no se reforma la Constitución; ley orgánica."], "Siguiente: VII. El Tribunal Constitucional (Título IX)")}
""", 2)

# =============================================================================
# VII. TRIBUNAL CONSTITUCIONAL
T.ap("bVII", "VII. El Tribunal Constitucional (Título IX, arts. 159 a 165)", donde(
  "Séptima pregunta. Tras ver cómo se garantizan los derechos, el **Tribunal Constitucional** es el órgano que garantiza la Constitución: quién lo compone, qué procesos conoce y qué valor tienen sus sentencias. La guía manda **leer detenidamente los arts. 159 a 165**.",
  ["1 Qué es el Tribunal Constitucional", "2 Composición y mandato", "3 Competencias y procedimientos", "4 Las sentencias", "5 Amparo frente a inconstitucionalidad"]))

T.ap("s33", "VII.1 Qué es el Tribunal Constitucional", f"""
{tag("IX", "Título IX")} se llama «**Del Tribunal Constitucional**» (arts. **159 a 165**).

{unidad("1.1 Naturaleza (art. 1 LOTC) y regulación (art. 165 CE)",
  lx("LOTC", "aprimero", 1, ["intérprete supremo de la Constitución", "es independiente de los demás órganos constitucionales", "sometido sólo a la Constitución y a la presente Ley Orgánica", "único en su orden"]),
  lit("CE", "a165", ["Una ley orgánica regulará el funcionamiento del Tribunal Constitucional"]),
  fichab("Tribunal Constitucional",
         "**Intérprete supremo** de la Constitución; **único en su orden**",
         ["**Independiente** de los demás órganos constitucionales", "Sometido **solo** a la Constitución y a su ley orgánica", "Jurisdicción en **todo el territorio**"],
         "—",
         f"{IMP} Está regulado por **ley orgánica** (la **LO 2/1979, del Tribunal Constitucional**, LOTC)."))}
""", 2)

T.ap("s34", "VII.2 Composición y mandato", f"""
{tabla(["Quién propone", "Cuántos", "Cómo", "Norma"], [
  ["**Congreso**", "**4**", "Mayoría de **tres quintos** de sus miembros", "CE 159.1"],
  ["**Senado**", "**4**", "Idéntica mayoría (3/5), **entre las candidaturas presentadas por las Asambleas Legislativas de las CCAA**", "CE 159.1; LOTC 16.1"],
  ["**Gobierno**", "**2**", "—", "CE 159.1"],
  ["**Consejo General del Poder Judicial**", "**2**", "—", "CE 159.1"],
  ["**Total**", "**12 miembros** nombrados **por el Rey**", "", "CE 159.1; LOTC 5"]])}

{unidad("2.1 Los 12 miembros (art. 159 CE)",
  lit("CE", "a159", ["12 miembros nombrados por el Rey", "cuatro a propuesta del Congreso por mayoría de tres quintos", "dos a propuesta del Gobierno, y dos a propuesta del Consejo General del Poder Judicial", "más de quince años de ejercicio profesional", "nueve años", "terceras partes cada tres", "independientes e inamovibles"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Composición y estatuto de los miembros",
         "**12 miembros**, nombrados por el **Rey**: 4 Congreso, 4 Senado, 2 Gobierno, 2 CGPJ",
         ["**Requisitos:** Magistrados y Fiscales, Profesores de Universidad, funcionarios públicos y Abogados, **juristas de reconocida competencia con más de 15 años** de ejercicio profesional", "Presencia **equilibrada** de mujeres y hombres: **al menos un 40 %** de cada sexo en las propuestas (art. 16.1 LOTC)"],
         ["**Mandato: 9 años**", "Renovación **por terceras partes cada 3 años**", "Sin nuevo mandato inmediato salvo que el cargo se hubiera ocupado **3 años o menos** (art. 16.4 LOTC)"],
         f"{IMP} **9 años** de mandato y renovación por **terceras partes cada 3**. Los miembros son **independientes e inamovibles**."))}

{unidad("2.2 Incompatibilidades (art. 159.4 CE; art. 19 LOTC)",
  lit("CE", "a159", ["incompatible: con todo mandato representativo", "con los cargos políticos o administrativos", "con el ejercicio de las carreras judicial y fiscal"], solo=[4, 5]),
  lx("LOTC", "adiecinueve", 19, ["incompatible", "Defensor del Pueblo", "Diputado y Senador", "carrera judicial o fiscal"], solo=[1]),
  "Incompatibilidades principales: **mandato representativo**, **cargo político o administrativo**, **funciones directivas en un partido político o sindicato** (y asociaciones, fundaciones y colegios profesionales según la LOTC), **carreras judicial y fiscal** y cualquier **actividad profesional o mercantil**.")}

{unidad("2.3 El Presidente y el Vicepresidente (art. 160 CE; art. 9 LOTC)",
  lit("CE", "a160", ["nombrado entre sus miembros por el Rey", "a propuesta del mismo Tribunal en pleno", "tres años"]),
  lx("LOTC", "anoveno", 9, ["elige de entre sus miembros por votación secreta a su Presidente", "tres años", "reelegido por una sola vez"], solo=[1, 3, 4]),
  fichab("Presidente del Tribunal Constitucional",
         "Lo elige el **Pleno** de entre sus miembros; lo nombra el **Rey**",
         "**Votación secreta** del Pleno; propuesta al Rey",
         "**3 años**; **reelegible por una sola vez**",
         "El Presidente lo nombra el Rey **a propuesta del propio Tribunal en pleno** (art. 160). El **Vicepresidente** lo elige el Pleno por el mismo procedimiento y periodo (art. 9.4 LOTC)."))}
""", 2)
