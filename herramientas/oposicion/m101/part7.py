
T.ap("s29", "VI.3 Qué derechos se pueden suspender en cada estado", f"""
El art. 55.1 enumera los derechos **suspendibles** y dice que solo pueden suspenderse en **excepción y sitio**. Combinando ambos:

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

### 3.2 Reglas de memoria de los arts. 17, 18, 19, 20, 21, 28 y 37 [[M107]]

Es un trabajo de **memoria**, y el vídeo avisa de que hay que cuidar sobre todo la redacción de los arts. **17, 18 y 20**:

- **17.3, la excepción dentro de la excepción.** Es lo único del art. 17 que **no** se suspende en el estado de excepción: solo en el **sitio**. Tiene sentido si se lee el apartado: {c("CE", "a17", "no pudiendo ser obligada a declarar")} y debe ser informada «de forma inmediata». Suspenderlo supondría poder **obligar a declarar a alguien sin informarle de sus derechos**: la mayor gravedad del artículo, por eso solo cabe en el sitio.
- **18.2 y 18.3.** La **inviolabilidad del domicilio** y el **secreto de las comunicaciones** sí pueden suspenderse en excepción y sitio (y, para personas determinadas, por la ley orgánica del art. 55.2).
- **19 y 21: circulación y reunión.** Son los derechos que más se tocaron en la pandemia y los que dieron problema al decreto de alarma (→ VI.2).
- **El «laberinto» del art. 20.** De todo el art. 20 solo se suspenden **tres cosas**: el **20.1.a)** ({c("CE", "a20", "A expresar y difundir libremente los pensamientos, ideas y opiniones")}), el **20.1.d)** ({c("CE", "a20", "A comunicar o recibir libremente información veraz por cualquier medio de difusión")}) y el **20.5** (el secuestro de publicaciones, grabaciones y otros medios de información, solo por **resolución judicial**). **No** se suspenden la creación literaria, artística, científica y técnica (20.1.b), la libertad de cátedra (20.1.c) ni los apartados 2, 3 y 4.
- **28.2 y 37.2: huelga y conflicto colectivo.** Los dos pueden suspenderse, pero **no están en el mismo nivel**: la **huelga** (28.2) está en la **sección 1.ª** (máxima protección) y el **conflicto colectivo** (37.2), en la **sección 2.ª**, sin esa protección reforzada. Tiene lógica que vayan juntos: la huelga es la **máxima expresión** del conflicto colectivo.
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

!> {IMP} **Para el examen:** no se puede **disolver el Congreso**, no se **interrumpe** el funcionamiento de las Cámaras ni de los poderes del Estado, no se modifica la **responsabilidad del Gobierno y de sus agentes**, **no se puede reformar la Constitución** (ni siquiera en alarma) y todo se regula por **ley orgánica**.
""", 2)

T.ap("s31", "VI.5 La suspensión individual (art. 55.2)", f"""
Además de la suspensión general, el art. 55.2 permite una suspensión **individual** de algunos derechos, **para personas determinadas** y en relación con las investigaciones de la actuación de **bandas armadas o elementos terroristas**.

{tabla(["Derecho", "Qué se puede suspender"], [
  [tag("I.2.1", "Art. 17.2"), "La **duración máxima de la detención preventiva** (72 horas)"],
  [tag("I.2.1", "Art. 18.2"), "La **inviolabilidad del domicilio**"],
  [tag("I.2.1", "Art. 18.3"), "El **secreto de las comunicaciones**"]])}

**Garantías comunes a los tres derechos:** forma y casos fijados por **ley orgánica**, **intervención judicial** y **control parlamentario**; y el uso injustificado o abusivo de esas facultades produce **responsabilidad penal**.

{lit("CE", "a55", ["Una ley orgánica podrá determinar la forma y los casos en los que, de forma individual y con la necesaria intervención judicial y el adecuado control parlamentario", "La utilización injustificada o abusiva de las facultades reconocidas en dicha ley orgánica producirá responsabilidad penal"], solo=[2, 3], titulo="Artículo 55.2")}

!> {IMP} La suspensión individual afecta **solo** a tres derechos (**17.2, 18.2 y 18.3**), a diferencia de la general, que afecta a diez. Y siempre **con intervención judicial y control parlamentario**.
""", 2)

T.ap("s32", "VI.6 Cuadro resumen de la suspensión", f"""
{tabla(["Clase", "Supuesto", "Declaración", "Duración", "Derechos que se pueden suspender"], [
  ["**Suspensión general**", f"{tag('I.5', 'Excepción')}", "**Gobierno**, con **autorización del Congreso**", "**30 días**; prórroga por otro plazo igual", "**17** (salvo 17.3) · **18.2** · **18.3** · **19** · **20.1.a)** y **d)** y **20.5** · **21** · **28.2** · **37.2**"],
  ["**Suspensión general**", f"{tag('X', 'Sitio')}", "**Congreso**, mayoría absoluta, a propuesta exclusiva del Gobierno", "La determinada por el **Congreso**", "Los mismos **más el 17.3**"],
  ["**Limitación**", f"{tag('IV', 'Alarma')}", "**Gobierno**, dando cuenta al Congreso", "**15 días**; prórroga con autorización del Congreso", "**Ninguno** (solo se pueden decretar algunas limitaciones)"],
  ["**Suspensión individual**", "Bandas armadas y elementos terroristas (art. 55.2)", "Sin declaración de estado: **ley orgánica** que fija la forma y los casos", "—", "**17.2** (duración máxima de la detención preventiva) · **18.2** · **18.3**"]])}

{resumen([
  "**Art. 55** (capítulo V): suspensión **general** (excepción y sitio: diez derechos, salvo el 17.3 en excepción) e **individual** (bandas armadas y terroristas: 17.2, 18.2, 18.3).",
  "**Quién declara:** alarma → Gobierno (da cuenta); excepción → Gobierno con autorización del Congreso; sitio → Congreso por mayoría absoluta a propuesta del Gobierno.",
  "**Duración:** alarma 15 días; excepción 30 (+30); sitio, la que fije el Congreso.",
  "**En común:** no se disuelve el Congreso, no se interrumpe el funcionamiento de las Cámaras, no se modifica la responsabilidad del Gobierno y de sus agentes, no se reforma la Constitución; ley orgánica."], "Siguiente: VII. El Tribunal Constitucional (Título IX)")}
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
  lx("LOTC", "anoveno", 9, ["elige de entre sus miembros por votación secreta a su Presidente", "mayoría absoluta", "tres años", "reelegido por una sola vez"], solo=[1, 2, 3, 4]),
  fichab("Presidente del Tribunal Constitucional",
         "Lo elige el **Pleno** de entre sus miembros; lo nombra el **Rey**",
         "**Votación secreta** del Pleno: **mayoría absoluta** en primera votación y, si no se alcanza, segunda votación (resulta elegido quien obtenga más votos; art. 9.2 LOTC); propuesta al Rey",
         "**3 años**; **reelegible por una sola vez**",
         "El Presidente lo nombra el Rey **a propuesta del propio Tribunal en pleno** (art. 160). El **Vicepresidente** lo elige el Pleno por el mismo procedimiento y periodo (art. 9.4 LOTC)."))}
""", 2)

T.ap("s34c", "VII.2c Organización del Tribunal: Pleno, Salas, Secciones, quórum y cese", f"""
El epígrafe oficial habla de «**organización, composición y atribuciones**»: tras la composición (arts. 159 y 160 CE) toca ver **cómo se organiza** el Tribunal por dentro (arts. 6 a 15 LOTC) y **cuándo cesan** sus Magistrados (art. 23 LOTC). *Apartado añadido a la guía M101 a partir de la LOTC vigente (ampliación): el módulo no lo desarrolla, pero el test oficial lo pregunta.*

{unidad("4.1 Pleno, Salas y Secciones (arts. 6 a 8 LOTC)",
  lx("LOTC", "asexto", 6, ["actúa en Pleno, en Sala o en Sección", "integrado por todos los Magistrados del Tribunal"], solo=[1, 2]),
  lx("LOTC", "aseptimo", 7, ["consta de dos Salas", "seis Magistrados nombrados por el Tribunal en Pleno"], solo=[1, 2, 3]),
  lx("LOTC", "aoctavo", 8, ["Secciones compuestas por el respectivo Presidente o quien le sustituya y dos Magistrados"], solo=[1]),
  tabla(["Órgano", "Composición", "Preside"], [
    ["**Pleno**", "**Todos** los Magistrados (12)", "El **Presidente**; en su defecto, el Vicepresidente y, a falta de ambos, el Magistrado más antiguo (y, si hay igual antigüedad, el de mayor edad)"],
    ["**Salas** (dos)", "**6 Magistrados** cada una, nombrados por el Pleno", "**Sala Primera**: el Presidente del Tribunal · **Sala Segunda**: el Vicepresidente"],
    ["**Secciones**", "El **Presidente** (del Pleno o de la Sala) o quien le sustituya y **2 Magistrados** (3 miembros)", "El Presidente respectivo"]]))}

{unidad("4.2 Qué conoce cada órgano (arts. 10 a 13 LOTC)",
  lx("LOTC", "adiez", 10, ["tratados internacionales", "excepto los de mera aplicación de doctrina", "conflictos constitucionales de competencia", "conflictos entre los órganos constitucionales del Estado"], solo=[1, 2, 3, 4, 5, 6, 7, 8, 9]),
  lx("LOTC", "aonce", 11, ["no sean de la competencia del Pleno"], solo=[1]),
  lx("LOTC", "adoce", 12, ["turno establecido por el Pleno"]),
  lx("LOTC", "atrece", 13, ["se someterá a la decisión del Pleno"]),
  fichab("Reparto de asuntos",
         ["El **Pleno**: tratados, recursos de inconstitucionalidad, conflictos de competencia, impugnaciones del art. 161.2 CE, conflictos en defensa de la autonomía local y entre órganos constitucionales…", "Las **Salas**: todo lo que **no** es del Pleno (art. 11), en especial el **amparo**"],
         "Las **Salas** se reparten los asuntos por un **turno** que fija el Pleno a propuesta de su Presidente (art. 12)",
         "—",
         f"{IMP} Si una **Sala** quiere **apartarse de la doctrina constitucional** anterior, la cuestión pasa al **Pleno** (art. 13)."))}

{unidad("4.3 Quórum (art. 14 LOTC) y funciones del Presidente (art. 15 LOTC)",
  lx("LOTC", "acatorce", 14, ["dos tercios de los miembros", "presencia de dos miembros"]),
  lx("LOTC", "aquince", 15, ["ejerce la representación del Tribunal", "convoca y preside el Tribunal en Pleno"], solo=[1]),
  fichab("Adopción de acuerdos",
         "El **Pleno**, las **Salas** y las **Secciones**",
         "Con la **presencia** de un número mínimo de miembros",
         ["**Pleno** y **Salas**: al menos **dos tercios** de los miembros que en cada momento los compongan", "**Secciones**: **dos** miembros, salvo que haya discrepancia (entonces, los **tres**)"],
         f"{IMP} **Dos tercios** de presencia (quórum), **no** de votos. El voto del Presidente dirime los empates (art. 90 LOTC; véase «Claves para memorizar la composición»)."))}

{unidad("4.4 Cese de los Magistrados (art. 23 LOTC)",
  lx("LOTC", "aveintitres", 23, ["por renuncia aceptada por el Presidente del Tribunal", "por expiración del plazo de su nombramiento", "mayoría simple en los casos tercero y cuarto", "mayoría de las tres cuartas partes de sus miembros en los demás casos"], solo=[1, 2]),
  tabla(["Causa de cese (art. 23.1)", "Quién lo decreta o decide (art. 23.2)"], [
    ["**1.º** Renuncia aceptada por el Presidente · **2.º** Expiración del plazo del nombramiento · **Fallecimiento**", "El **Presidente** del Tribunal"],
    ["**3.º** Incapacidad (las de los miembros del Poder Judicial) · **4.º** Incompatibilidad sobrevenida", "El **Pleno**, por **mayoría simple**"],
    ["**5.º** No atender con diligencia los deberes del cargo · **6.º** Violar la reserva propia de su función · **7.º** Responsabilidad civil por dolo, o condena por delito doloso o por culpa grave", "El **Pleno**, por **mayoría de las tres cuartas partes** de sus miembros"]]),
  f"{IMP} **Regla:** las dos causas «normales» (renuncia y expiración) y la muerte las decreta el **Presidente**; el resto lo decide el **Pleno**: **mayoría simple** para las dos primeras causas «sobrevenidas» (3.ª y 4.ª) y **tres cuartas partes** para las demás.")}
""", 2)

T.ap("s34b", "VII.2b Claves para memorizar la composición", f"""
La composición del Tribunal Constitucional es un puro trabajo de memoria, pero se puede **anclar** con unas cuantas ideas. [[M101]]

{unidad("3.1 Todo va «en packs de tres»",
  "Son **12** magistrados y se renuevan **por terceras partes cada tres años** (art. 159.3 CE): cada renovación afecta, por tanto, a **4** magistrados. Y **4** es justo el número que propone cada una de las dos Cámaras. Los **doce** se reparten así: **4 + 4** (Congreso y Senado) **+ 2 + 2** (Gobierno y Consejo General del Poder Judicial). En la práctica, las renovaciones se organizan **por bloques de quienes proponen** (los cuatro del Congreso, los cuatro del Senado y los cuatro del Gobierno y del CGPJ), aunque la Constitución solo exige el ritmo de **terceras partes cada tres años**.",
  tabla(["Bloque", "Magistrados", "Quién propone", "Mayoría"], [
    ["**1.º**", "**4**", "**Congreso**", "**3/5**"],
    ["**2.º**", "**4**", "**Senado** (entre candidaturas de las Asambleas autonómicas)", "**3/5**"],
    ["**3.º**", "**2 + 2**", "**Gobierno** (2) y **CGPJ** (2)", "—"]]))}

{unidad("3.2 Los nueve años: uno de los mandatos más largos",
  "El mandato de **9 años** es de los más largos entre los órganos constitucionales: sirve como referencia cuando «te bailen las cifras» (el Presidente del Tribunal, **3 años**; el Defensor del Pueblo, **5**). Ojo con la exactitud: el módulo lo presenta como el más largo de todos, pero la ley le pone un **empate**, porque los Consejeros de Cuentas del **Tribunal de Cuentas** también se designan «por un período de **nueve años**» y por **3/5** de cada Cámara (art. 30 LO 2/1982). Aprende «9 años = TC (y Tribunal de Cuentas)».",
  lx("LOTCu", "atreinta", 30, ["por un período de nueve años"], solo=[1]))}

{unidad("3.3 El Presidente es «uno más» y su voto dirime los empates",
  "El Presidente **ya forma parte del Tribunal** (no llega «desde fuera»): el **Pleno** elige a su Presidente **de entre sus miembros** por votación secreta y lo propone al Rey, que lo nombra. Como los miembros son **12** (un número par), los empates son posibles, y para eso la ley atribuye al Presidente el voto que decide: *«En caso de empate, decidirá el voto del Presidente»* (art. 90.1 LOTC), lo que la academia llama el **voto de calidad**.",
  lx("LOTC", "anoventa", 90, ["En caso de empate, decidirá el voto del Presidente"], solo=[1]))}

{unidad("3.4 Los quince años, siempre quince",
  "El requisito profesional es el mismo en todos los casos: **juristas de reconocida competencia con más de quince años de ejercicio** (art. 159.2 CE; art. 18 LOTC). Te servirá de patrón para otros órganos, como el Consejo General del Poder Judicial. La excepción que conviene conocer es la **Presidencia del Tribunal Supremo y del CGPJ**, donde el jurista debe acreditar **más de veinticinco años** de ejercicio (art. 586.1 LOPJ).",
  lx("LOPJ", "aquinientosochentayseis", 586, ["más de veinticinco años de antigüedad en el ejercicio de su profesión"], solo=[1]))}
""", 2)
