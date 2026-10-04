# -*- coding: utf-8 -*-
# Tema I.2 (v4) · Parte 5: bloque III, la suspensión.
from v4_util import *
from v4_examen import EX10, EX10_NOTA, EX_X4

ap("bIII", "III. ¿Cuándo pueden suspenderse? (arts. 55 y 116, su desarrollo y art. 3.2 LOPJ)", f"""
{donde("Los derechos están reconocidos (I) y protegidos (II). Pero la Constitución admite que, en situaciones extraordinarias, **algunos** queden temporalmente sin efecto. Este bloque responde a **cuáles**, **cuándo**, **quién lo decide** y **con qué controles**.",
       ["1 El art. 55: dos clases de suspensión", "2 Qué derechos se suspenden", "3 El art. 116 y las reglas comunes (LO 4/1981)", "4 Alarma", "5 Excepción", "6 Sitio", "7 Cuadro comparativo", "8 Práctica y jurisprudencia", "9 Suspensión individual: art. 55.2 y LECrim"])}

**Orden de estudio.** El art. 55 primero (es el Capítulo quinto del Título I); después la suspensión **general**, con el art. 116 y la LO 4/1981 en el orden de sus artículos; al final, la suspensión **individual** del art. 55.2 y su desarrollo en la LECrim.

!> **Distinción que lo ordena todo:** **limitar** un derecho (posible en el estado de alarma) no es lo mismo que **suspenderlo** (solo en los estados de excepción y de sitio, art. 55.1).
""")

# ---------------------------------------------------------------------------
ap("s6", "III.1 El art. 55: suspensión general y suspensión individual", f"""
Suspender un derecho es **dejarlo temporalmente sin efecto**, no solo limitarlo. El Capítulo quinto, «De la suspensión de los derechos y libertades», tiene un único artículo.

{unidad("1.1 La suspensión de los derechos y libertades (art. 55)",
  lit("CE", 55, ["17, 18, apartados 2 y 3, artículos 19, 20, apartados 1, a) y d), y 5, artículos 21, 28, apartado 2, y artículo 37, apartado 2", "estado de excepción o de sitio", "el apartado 3 del artículo 17 para el supuesto de declaración de estado de excepción", "de forma individual", "necesaria intervención judicial y el adecuado control parlamentario", "bandas armadas o elementos terroristas", "responsabilidad penal"]),
  fichab("Dos clases de suspensión: **general** (55.1) e **individual** (55.2)",
         ["55.1: todos los que estén en el territorio afectado por el estado de **excepción** o de **sitio**", f"55.2: {c('CE', 55, 'personas determinadas')}, investigadas por actuaciones de **bandas armadas o elementos terroristas**"],
         ["55.1: al declararse el estado (art. 116 y LO 4/1981 → III.3 a III.6)", "55.2: por **ley orgánica**, con intervención **judicial** y control **parlamentario** (LECrim → III.9)"],
         "—",
         ["55.1 solo nombra **excepción y sitio**: la **alarma no suspende**", "El **17.3** no se suspende en la excepción (solo en el sitio)", "55.2 solo alcanza a **17.2, 18.2 y 18.3**", "El abuso de las facultades del 55.2 genera responsabilidad **penal**"]))}

| | Suspensión **general** (55.1) | Suspensión **individual** (55.2) |
|---|---|---|
| Cuándo | Estado de **excepción** o de **sitio** | Investigaciones sobre **bandas armadas o elementos terroristas** |
| A quién | A todos en el territorio afectado | A personas determinadas |
| Derechos | 17; 18.2 y 18.3; 19; 20.1 a) y d) y 20.5; 21; 28.2; 37.2 | Solo 17.2, 18.2 y 18.3 |
| Regulación | Art. 116 CE y LO 4/1981 | Una ley orgánica (preceptos de la LECrim) |
| Control | El Congreso autoriza o declara | Intervención judicial y control parlamentario |
""", 2)

# ---------------------------------------------------------------------------
ap("s6-1", "III.2 Qué derechos pueden suspenderse (art. 55.1)", f"""
Es la consecuencia de la casilla «Protección» de las fichas del bloque I. Solo los que enumera el art. 55.1:

| Art. | Derecho | Matiz |
|---|---|---|
| 17 | Libertad y seguridad personal | El **17.3** (derechos del detenido) **no** se suspende en el estado de excepción; solo en el de **sitio** |
| 18.2 | Inviolabilidad del domicilio | — |
| 18.3 | Secreto de las comunicaciones | — |
| 19 | Residencia y circulación | — |
| 20.1 a) | Libertad de expresión | — |
| 20.1 d) | Libertad de información | — |
| 20.5 | Secuestro de publicaciones solo por resolución judicial | — |
| 21 | Reunión y manifestación | — |
| 28.2 | Huelga | — |
| 37.2 | Medidas de conflicto colectivo | Único de la Sección 2.ª |

**La excepción del 17.3.** {c("CE", 55, "Se exceptúa de lo establecido anteriormente el apartado 3 del artículo 17 para el supuesto de declaración de estado de excepción")}. Las garantías del detenido (información inmediata, no declarar, abogado) se mantienen en la excepción y **solo** se suspenden en el **sitio**, como confirma el art. 32.3 LO 4/1981 (→ III.6).

**Lo que nunca se suspende** (los distractores habituales): igualdad (14), vida (15), libertad ideológica (16), honor e intimidad (18.1), creación (20.1 b), cátedra (20.1 c), **asociación (22)**, participación (23), tutela judicial (24), legalidad penal (25), educación (27), **libertad sindical (28.1)** y petición (29).

Cayó en el extraordinario de 2025: pregunta real justo debajo.

{EX_X4}
""", 2)

# ---------------------------------------------------------------------------
ap("s6-3", "III.3 El art. 116 CE y las reglas comunes de la LO 4/1981 (arts. 1 a 3)", f"""
El art. 116 fija **quién** declara cada estado y **cuánto** dura; la **Ley Orgánica 4/1981, de 1 de junio, de los estados de alarma, excepción y sitio** (BOE-A-1981-12774; BOE de 5 de junio de 1981; **no modificada** desde su aprobación) fija **cuándo** procede y **qué medidas** permite.

{unidad("3.1 Los estados de alarma, excepción y sitio (art. 116 CE)",
  lit("CE", 116, ["Una ley orgánica regulará", "plazo máximo de quince días", "reunido inmediatamente al efecto", "previa autorización del Congreso de los Diputados", "no podrá exceder de treinta días, prorrogables por otro plazo igual", "mayoría absoluta del Congreso de los Diputados, a propuesta exclusiva del Gobierno", "No podrá procederse a la disolución del Congreso", "Diputación Permanente", "principio de responsabilidad del Gobierno"]),
  fichab("Los tres estados excepcionales y sus garantías institucionales",
         ["Alarma (116.2): el **Gobierno**, por decreto en Consejo de Ministros, dando cuenta al Congreso", "Excepción (116.3): el **Gobierno**, por decreto en Consejo de Ministros, **previa autorización** del Congreso", "Sitio (116.4): el **Congreso**, por **mayoría absoluta**, a **propuesta exclusiva** del Gobierno"],
         ["116.5: no se puede **disolver** el Congreso; las Cámaras quedan **automáticamente convocadas** si no están en sesiones; no se interrumpe el funcionamiento de las Cámaras ni de los demás poderes; si el Congreso está disuelto o expirado, asume sus competencias la **Diputación Permanente**", "116.6: no se modifica el principio de **responsabilidad** del Gobierno y sus agentes"],
         ["Alarma: máximo **15 días**; prórroga solo con autorización del Congreso", "Excepción: máximo **30 días**, prorrogables por **otro plazo igual**", "Sitio: lo que fije el Congreso (ámbito, duración y condiciones)", "Sitio: **mayoría absoluta** del Congreso"],
         [f"Alarma: Congreso {c('CE', 116, 'reunido inmediatamente al efecto')}", "Sitio: la propuesta del Gobierno es **exclusiva**", "En la excepción el Congreso **autoriza**; en el sitio **declara**"]))}

{unidad("3.2 Disposiciones comunes de la LO 4/1981 (arts. 1 a 3)",
  lit("LO4", "primero", ["circunstancias extraordinarias", "estrictamente indispensables", "de forma proporcionada a las circunstancias", "salvo las que consistiesen en sanciones firmes"]),
  lit("LO4", "segundo", ["desde el instante mismo de su publicación"]),
  lit("LO4", "tercero", ["impugnables en vía jurisdiccional", "tendrán derecho a ser indemnizados"]),
  fichab("Reglas que valen para los tres estados",
         "El Gobierno y las Autoridades competentes",
         ["Presupuesto (1.1): **circunstancias extraordinarias** que hagan imposible la normalidad con los poderes ordinarios", "Proporcionalidad (1.2): medidas y duración **estrictamente indispensables**, aplicadas de forma proporcionada", "Fin del estado (1.3): decaen las competencias y medidas, **salvo las sanciones firmes**", "Continuidad (1.4): no se interrumpe el funcionamiento de los poderes constitucionales", "Publicación (2): de inmediato en el BOE y difusión obligatoria por los medios públicos y por los privados que se determinen", "Control (3): actos **impugnables** en vía jurisdiccional e **indemnización** de los daños no imputables al perjudicado"],
         "Vigencia de la **declaración**: desde el instante mismo de su publicación en el BOE",
         "La **declaración** rige «desde el instante mismo de su publicación»; la **propia LO 4/1981** entró en vigor «el día siguiente al de su publicación» (disposición final)."))}
""", 2)

# ---------------------------------------------------------------------------
ap("s6-4", "III.4 El estado de alarma (LO 4/1981, arts. 4 a 12)", f"""
El estado de las **catástrofes y emergencias**. No suspende derechos: solo permite **limitarlos**.

{unidad("4.1 Supuestos (art. 4)",
  lit("LO4", "cuarto", ["Crisis sanitarias", "concurra alguna de las demás circunstancia o situaciones", "desabastecimiento"]),
  fichab("Cuándo puede declararse la alarma, en todo o parte del territorio",
         "El Gobierno",
         ["a) **catástrofes**, calamidades o desgracias públicas (terremotos, inundaciones, incendios urbanos y forestales, accidentes de gran magnitud)", "b) **crisis sanitarias** (epidemias, contaminación grave)", "c) **paralización de servicios públicos esenciales**, si no se garantizan los arts. 28.2 y 37.2 CE **y** concurre otra circunstancia del artículo", "d) **desabastecimiento** de productos de primera necesidad"],
         "—",
         ["Una huelga sola **no** basta: el supuesto c) exige que concurra otro de los supuestos", "*Así en el BOE:* «circunstancia» en singular"]))}

{unidad("4.2 Declaración, duración, autoridad y control (arts. 5 a 8)",
  lit("LO4", "quinto", ["podrá solicitar del Gobierno"]),
  lit("LO4", "sexto", ["que no podrá exceder de quince días", "autorización expresa del Congreso de los Diputados"]),
  lit("LO4", "séptimo", ["por delegación de éste, el Presidente de la Comunidad Autónoma"]),
  lit("LO4", "octavo", []),
  fichab("Cómo se declara, cuánto dura y quién manda",
         ["**Declara** siempre el Gobierno (6)", "Si afecta solo a una CA, su **Presidente puede solicitarlo** (5)", "Autoridad competente (7): el Gobierno o, **por delegación**, el Presidente de la CA si solo afecta a su territorio"],
         ["Decreto en Consejo de Ministros: ámbito, duración y efectos (6.1)", "El Gobierno **da cuenta** al Congreso de la declaración y de los decretos que dicte (8)"],
         ["Máximo **15 días** (6.2)", "Prórroga: solo con **autorización expresa del Congreso**, que puede fijar su alcance y condiciones (6.2)"],
         "El Presidente autonómico **solicita** y puede ser **autoridad delegada**, pero **nunca declara**."))}

{unidad("4.3 Poderes sobre el personal e incumplimientos (arts. 9 y 10)",
  lit("LO4", "noveno", ["bajo las órdenes directas de la Autoridad competente"]),
  lit("LO4", "diez", []),
  fichab("Mando único sobre las Administraciones del territorio",
         "Autoridades civiles, policías autonómicas y locales y personal de las Administraciones del territorio afectado",
         ["Quedan **bajo las órdenes directas** de la Autoridad competente, que puede imponerles servicios extraordinarios (9)", "Incumplimientos: sanción según las leyes; los funcionarios pueden ser **suspendidos** de inmediato y, si son Autoridades, la Autoridad competente puede asumir sus facultades (10)"],
         "—",
         "Incluye a las **policías autonómicas y locales**."))}

{unidad("4.4 Medidas (arts. 11 y 12)",
  lit("LO4", "once", ["Limitar la circulación o permanencia de personas o vehículos", "con excepción de domicilios privados"]),
  lit("LO4", "doce", ["movilización de su personal"]),
  fichab("Qué puede acordar el decreto: **limitaciones**, no suspensiones",
         "La Autoridad competente",
         ["11 a) limitar la circulación o permanencia de personas o vehículos en horas y lugares determinados", "11 b) requisas temporales y **prestaciones personales obligatorias**", "11 c) intervenir y ocupar transitoriamente industrias, fábricas, talleres, explotaciones o locales, **salvo domicilios privados**", "11 d) limitar o racionar servicios y artículos de primera necesidad", "11 e) órdenes para el abastecimiento de los mercados", "12.1, catástrofes y crisis sanitarias: medidas de las normas sobre enfermedades infecciosas, medio ambiente, aguas e incendios forestales", "12.2, paralización de servicios y desabastecimiento: **intervención de empresas** y **movilización de su personal**"],
         "—",
         "Las ocupaciones excluyen los **domicilios privados**. Limitar la circulación no es suspenderla (STC 148/2021 [[TC|https://hj.tribunalconstitucional.es/es-ES/Resolucion/Show/26778]] → III.8)."))}
""", 2)

# ---------------------------------------------------------------------------
ap("s6-5", "III.5 El estado de excepción (LO 4/1981, arts. 13 a 31)", f"""
El estado de las **crisis de orden público**. Aquí sí se suspenden derechos, los del 55.1 **salvo el 17.3**.

{unidad("5.1 Supuesto y solicitud (art. 13)",
  lit("LO4", "trece", ["gravemente alterados", "que no podrán ser otros que los enumerados en el apartado uno del artículo cincuenta y cinco", "que no podrá exceder de treinta días", "La cuantía máxima de las sanciones pecuniarias", "introducir modificaciones"]),
  fichab("Cuándo procede y qué pide el Gobierno al Congreso",
         "El Gobierno solicita; el **Congreso** autoriza",
         ["Supuesto (13.1): el libre ejercicio de los derechos, el funcionamiento de las instituciones democráticas, el de los servicios públicos esenciales u otro aspecto del orden público, **tan gravemente alterados** que las potestades ordinarias no bastan", "La solicitud (13.2) contiene **cuatro** extremos: a) efectos y **derechos cuya suspensión se pide** (solo los del 55.1); b) medidas; c) ámbito territorial y duración; d) **cuantía máxima de las sanciones pecuniarias**", f"El Congreso (13.3) puede {c('LO4', 'trece', 'aprobarla en sus propios términos o introducir modificaciones en la misma')}"],
         "Duración solicitada: máximo **30 días**",
         "Cuatro extremos; el último, la **cuantía máxima de las sanciones**."))}

{unidad("5.2 Declaración, cambios y prórroga (arts. 14 y 15)",
  lit("LO4", "catorce", []),
  lit("LO4", "quince", ["no podrá exceder de treinta días"]),
  fichab("Del permiso del Congreso al decreto del Gobierno",
         "El Gobierno declara; el Congreso autoriza",
         [f"Decreto en Consejo de Ministros {c('LO4', 'catorce', 'con el contenido autorizado por el Congreso de los Diputados')} (14)", "Cambiar las medidas exige **nueva autorización** (15.1)", "**Fin anticipado** por decreto del Gobierno, dando cuenta inmediata al Congreso (15.2)", "**Prórroga**: se solicita al Congreso (15.3)"],
         "Prórroga: máximo **30 días**",
         "El Gobierno puede **terminarlo antes** sin pedir permiso; para **cambiarlo** o **prorrogarlo**, necesita al Congreso."))}

{unidad("5.3 Medidas según el derecho suspendido (arts. 16 a 23)",
  lit("LO4", "dieciséis", ["no podrá exceder de diez días", "en el plazo de veinticuatro horas"]),
  lit("LO4", "diecisiete", ["dos vecinos"]),
  lit("LO4", "dieciocho", []),
  lit("LO4", "diecinueve", []),
  lit("LO4", "veinte", ["con una antelación de dos días"]),
  lit("LO4", "veintiuno", ["ningún tipo de censura previa"]),
  lit("LO4", "veintidós", ["no podrán ser prohibidas, disueltas ni sometidas a autorización previa"]),
  lit("LO4", "veintitrés", []),
  fichab("Cada medida exige que la autorización del Congreso incluya la suspensión del derecho correspondiente",
         "La Autoridad gubernativa; el juez, informado",
         ["17 → **detención** por la Autoridad gubernativa; el detenido conserva los derechos del **17.3** (16)", "18.2 → **inspecciones y registros** domiciliarios, con el titular o familiares y **dos vecinos**; acta y comunicación al juez (17)", "18.3 → **intervención de comunicaciones**, comunicada de inmediato al juez por escrito motivado (18)", "Control de **transportes** y su carga (19)", "19 → prohibir la circulación, zonas de seguridad, control de desplazamientos y fijación de residencia (20)", "20.1 a) y d) y 20.5 → suspender publicaciones, emisiones y espectáculos y secuestrar publicaciones, **sin censura previa** (21)", "21 → autorización previa, prohibición o disolución de reuniones (22)", "28.2 y 37.2 → prohibir **huelgas** y medidas de **conflicto colectivo** (23)"],
         ["Detención: máximo **10 días**; comunicada al juez en **24 horas** (16)", "Desplazamientos: aviso con **2 días** de antelación (20)"],
         ["Detención: **10 días** y juez en **24 horas**, no las 72 horas del art. 17.2 CE", "Las reuniones **orgánicas** de partidos, sindicatos y asociaciones empresariales **no** pueden prohibirse, disolverse ni someterse a autorización (22)"]))}

{unidad("5.4 Otras medidas y Comunidades Autónomas (arts. 24 a 31)",
  lit("LO4", "veinticuatro", ["podrán ser expulsados de España"]),
  lit("LO4", "veinticinco", []),
  lit("LO4", "veintiséis", []),
  lit("LO4", "veintisiete", []),
  lit("LO4", "veintiocho", []),
  lit("LO4", "veintinueve", []),
  lit("LO4", "treinta", []),
  lit("LO4", "treinta y uno", []),
  fichab("Medidas complementarias del estado de excepción",
         ["La Autoridad gubernativa; el **juez**, para la prisión provisional (30)", f"Si afecta solo a una CA, la Autoridad gubernativa {c('LO4', 'treinta y uno', 'podrá coordinar el ejercicio de sus competencias con el Gobierno de dicha Comunidad')} (31)"],
         ["**Extranjeros** (24): comparecencias, control de permisos y posible **expulsión**, con justificación sumaria previa", "Incautación de **armas** y explosivos (25)", "Intervención o cierre de industrias, comercios y locales (26)", "Vigilancia de instalaciones con puestos armados (27)", "Si coincide con circunstancias del art. 4, se suman las medidas de la **alarma** (28)", "Suspensión de **funcionarios** que favorezcan a los perturbadores (29)", "**Prisión provisional** acordada por el juez durante el estado (30)"],
         "—",
         "La Autoridad del estado de excepción es **gubernativa** (civil); la **militar** es propia del sitio."))}
""", 2)

# ---------------------------------------------------------------------------
ap("s6-6", "III.6 El estado de sitio (LO 4/1981, arts. 32 a 36; art. 3.2 LOPJ)", f"""
El estado de las **crisis que amenazan la existencia del Estado**. Suspende los derechos del 55.1, **incluido el 17.3**.

{unidad("6.1 Supuesto, declaración y medidas (art. 32)",
  lit("LO4", "treinta y dos", ["insurrección o acto de fuerza", "apartado tres del artículo diecisiete"]),
  fichab("Cuándo procede y qué añade a los otros dos estados",
         "Propone el Gobierno; **declara el Congreso** por mayoría absoluta (116.4 CE)",
         [f"Supuesto (32.1): {c('LO4', 'treinta y dos', 'insurrección o acto de fuerza contra la soberanía o independencia de España, su integridad territorial o el ordenamiento constitucional, que no pueda resolverse por otros medios')}", f"La declaración {c('LO4', 'treinta y dos', 'determinará el ámbito territorial, duración y condiciones del estado de sitio')} (32.2)", "Medidas (32.3): las de la alarma y la excepción **y además** la suspensión de las garantías del detenido del **art. 17.3** CE"],
         "Mayoría absoluta del Congreso; duración la que fije",
         "Lo único que **solo** permite el sitio: suspender el **17.3**."))}

{unidad("6.2 La Autoridad militar (arts. 33 a 36; art. 3.2 LOPJ)",
  lit("LO4", "treinta y tres", ["designará la Autoridad militar"]),
  lit("LO4", "treinta y cuatro", ["bandos"]),
  lit("LO4", "treinta y cinco", ["Jurisdicción Militar"]),
  lit("LO4", "treinta y seis", []),
  EX10_NOTA,
  fichab("Quién ejecuta las medidas del estado de sitio",
         ["El **Gobierno** dirige (33.1; art. 97 CE)", "Una **Autoridad militar** designada por el Gobierno ejecuta, bajo su dirección (33.2)", "Las **autoridades civiles** conservan las facultades no conferidas a la militar (36)"],
         ["La Autoridad militar publica **bandos** con las medidas y prevenciones (34)", "El Congreso puede someter determinados delitos a la **Jurisdicción Militar** durante el estado (35)",
          f"La jurisdicción militar administra Justicia {c('LOPJ', 3, 'en el ámbito estrictamente castrense y, en su caso, en las materias que establezca la declaración del estado de sitio')} (art. 3.2 LOPJ; la LOPJ se estudia en el tema I.7)"],
         "—",
         "La Jurisdicción Militar en el sitio la fija **el Congreso** en la declaración, no el Gobierno ni la Autoridad militar. Cayó en 2025, vía art. 3.2 LOPJ: pregunta real justo debajo."))}

{EX10}
""", 2)

# ---------------------------------------------------------------------------
ap("s6-7", "III.7 Cuadro comparativo de los tres estados", f"""
| | Alarma | Excepción | Sitio |
|---|---|---|---|
| Naturaleza de la crisis | Catástrofes y emergencias | Orden público | Amenaza a la soberanía, la integridad o el orden constitucional |
| Presupuesto (LO 4/1981) | Catástrofes; crisis sanitarias; paralización de servicios esenciales (con otra circunstancia); desabastecimiento (art. 4) | Grave alteración del libre ejercicio de los derechos, de las instituciones democráticas, de los servicios esenciales o de otro aspecto del orden público (art. 13) | Insurrección o acto de fuerza contra la soberanía, independencia, integridad territorial u ordenamiento constitucional (art. 32) |
| Quién lo declara | **Gobierno**, decreto en Consejo de Ministros (116.2) | **Gobierno**, decreto en Consejo de Ministros, **previa autorización** del Congreso (116.3) | **Congreso** por **mayoría absoluta**, a **propuesta exclusiva** del Gobierno (116.4) |
| Papel del Congreso | Se le da cuenta, «reunido inmediatamente al efecto»; autoriza la prórroga | Autoriza; puede introducir modificaciones | Declara y fija ámbito, duración y condiciones |
| Duración | Máximo **quince días** | Máximo **treinta días** | La que fije el Congreso |
| Prórroga | Con autorización expresa del Congreso; la CE no fija límite | **Otro plazo igual** (máximo treinta días), con los mismos requisitos | La que fije el Congreso |
| Suspensión de derechos | **No**: solo limitaciones (art. 11) | Sí: los del 55.1, **salvo el 17.3** | Sí: los del 55.1, **incluido el 17.3** (art. 32.3) |
| Autoridad | Gobierno o, por delegación, Presidente autonómico (art. 7) | Autoridad gubernativa | Autoridad militar designada por el Gobierno (art. 33) |
| Comunidad Autónoma | Su Presidente puede solicitarlo (art. 5) | Coordinación con su Gobierno (art. 31) | — |

**Reglas comunes a los tres estados:**
- no se disuelve el Congreso y no se interrumpen los poderes del Estado (116.5 CE; art. 1.4 LO 4/1981);
- se mantiene la responsabilidad del Gobierno (116.6);
- no puede iniciarse la reforma constitucional (art. 169 → II.2.4);
- los actos son impugnables y los daños, indemnizables (art. 3 LO 4/1981).

**En excepción y sitio**, además, la ley dice expresamente que no se interrumpe la actividad del Defensor del Pueblo (art. 11.3 LO 3/1981 → IV.4.3) ni la de los defensores autonómicos (art. 1.4 Ley 36/1985 → IV.7).
""", 2)

# ---------------------------------------------------------------------------
ap("s6-8", "III.8 Aplicación práctica y jurisprudencia", f"""
*Este apartado no es texto legal: recoge hechos y sentencias, con su referencia (reales decretos: [[BOE]]; sentencias: [[TC]]).*

- **Estados de excepción y de sitio:** **nunca se han declarado**.
- **Estado de alarma de 2010:** **RD 1673/2010**, de 4 de diciembre (BOE-A-2010-18683) [[BOE]], para normalizar el servicio público esencial del **transporte aéreo** (cierre del espacio aéreo por los controladores). Fue el primero.
- **Estado de alarma de 2020:** **RD 463/2020**, de 14 de marzo (BOE-A-2020-3692) [[BOE]], por la **COVID-19**, con varias prórrogas hasta junio de 2020.
- **Estado de alarma de 2020-2021:** **RD 926/2020**, de 25 de octubre (BOE-A-2020-12898) [[BOE]], con delegación en los Presidentes autonómicos como autoridades competentes; el Congreso autorizó una **prórroga de seis meses** (RD 956/2020, de 3 de noviembre).

| Sentencia | Qué declaró |
|---|---|
| **STC 83/2016, de 28 de abril** [[TC]] | El decreto que declara la alarma tiene **rango o valor de ley**; su control corresponde al **Tribunal Constitucional** |
| **STC 148/2021, de 14 de julio** [[TC]] | Inconstitucionales los **apartados 1, 3 y 5 del art. 7 del RD 463/2020**, porque **suspendían** (no limitaban) la libertad de circulación del **art. 19 CE**, algo que la alarma no permite. También anuló el inciso «modificar, ampliar o» de su art. 10.6 |
| **STC 183/2021, de 27 de octubre** [[TC]] | Inconstitucionales la **duración de seis meses** de la prórroga (acuerdo del Congreso de 29 de octubre de 2020 y art. 2 del RD 956/2020) y el régimen de **delegación** en los Presidentes autonómicos («autoridades competentes delegadas») del RD 926/2020 |

Texto de las sentencias: STC 83/2016 [[TC|https://hj.tribunalconstitucional.es/es-ES/Resolucion/Show/24935]] · STC 148/2021 [[TC|https://hj.tribunalconstitucional.es/es-ES/Resolucion/Show/26778]] · STC 183/2021 [[TC|https://hj.tribunalconstitucional.es/es-ES/Resolucion/Show/26843]].

!> **Idea clave.** La STC 148/2021 aplica directamente la distinción del bloque: **limitar** (posible en la alarma) frente a **suspender** (solo en excepción y sitio, art. 55.1).
""", 2)

# ---------------------------------------------------------------------------
ap("s6-2", "III.9 La suspensión individual (art. 55.2 CE y LECrim)", f"""
La segunda clase de suspensión: frente al **terrorismo**, sobre **personas determinadas** y **sin** declarar ningún estado.

{unidad("9.1 El art. 55.2 CE",
  lit("CE", 55, ["de forma individual", "necesaria intervención judicial y el adecuado control parlamentario", "17, apartado 2, y 18, apartados 2 y 3", "bandas armadas o elementos terroristas", "responsabilidad penal"], solo=[1, 2], titulo="Artículo 55.2"),
  fichab("Suspensión **individual** de tres derechos en investigaciones de terrorismo",
         [f"Persona: {c('CE', 55, 'personas determinadas')}", "Regula: **una ley orgánica**", "Controlan: el **juez** y el **Parlamento**"],
         [f"Presupuesto: {c('CE', 55, 'en relación con las investigaciones correspondientes a la actuación de bandas armadas o elementos terroristas')}", "Derechos: **17.2** (duración de la detención), **18.2** (domicilio) y **18.3** (comunicaciones)", "Garantías: necesaria intervención judicial y adecuado control parlamentario", "Abuso: utilización injustificada o abusiva → **responsabilidad penal**"],
         "—",
         "Solo **17.2, 18.2 y 18.3**: ni todo el art. 17 ni el 19."))}

### 9.2 Su desarrollo en la Ley de Enjuiciamiento Criminal

Las reglas están en la **Ley de Enjuiciamiento Criminal** (BOE-A-1882-6036; texto consolidado con última modificación de 9 de abril de 2026). Los preceptos siguientes se refieren a los delitos de **bandas armadas o elementos terroristas**, los mismos del art. 55.2. Que sean su desarrollo es **interpretación**: la LECrim no lo dice expresamente. Se reproducen en el orden de sus artículos.

{lit("LEC", "384 bis", ["quedará automáticamente suspendido"])}

{lit("LEC", 509, ["no podrá extenderse más allá de cinco días", "por otro plazo no superior a cinco días", "los menores de dieciséis años"])}

{lit("LEC", 520, ["en el plazo máximo de setenta y dos horas"], solo=[1], titulo="Artículo 520.1, párrafo segundo (LECrim)")}

{lit("LEC", "520 bis", ["dentro de las setenta y dos horas siguientes a la detención", "hasta un límite máximo de otras cuarenta y ocho horas", "dentro de las primeras cuarenta y ocho horas", "en las veinticuatro horas siguientes", "en el plazo de veinticuatro horas"])}

{lit("LEC", 527, ["dos reconocimientos cada veinticuatro horas"])}

{lit("LEC", 553, ["en casos de excepcional o urgente necesidad", "se dará cuenta inmediata al Juez competente"])}

{lit("LEC", 579, ["podrá ordenarla el Ministro del Interior o, en su defecto, el Secretario de Estado de Seguridad", "dentro del plazo máximo de veinticuatro horas", "en un plazo máximo de setenta y dos horas"], solo=[0, 1, 2, 3, 4, 5], titulo="Artículo 579.1 a 3 (LECrim). De la correspondencia escrita o telegráfica.")}

{lit("LEC", "588 ter d", ["podrá ordenarla el Ministro del Interior"], solo=[9], titulo="Artículo 588 ter d.3 (LECrim)")}

{fichab("Cómo se concreta la suspensión de cada derecho del 55.2",
        ["El **Juez** autoriza o confirma", "En urgencia, el **Ministro del Interior** o, en su defecto, el **Secretario de Estado de Seguridad** (579.3 y 588 ter d.3)", "Los **Agentes**, para entrar en domicilios en urgencia (553)"],
        ["**17.2**, detención: prórroga de la detención más allá de 72 horas (520 bis.1); incomunicación (509, 520 bis.2 y 527)", f"**18.2**, domicilio: entrada y detención de propia autoridad {c('LEC', 553, 'en casos de excepcional o urgente necesidad')}, con **cuenta inmediata al Juez** (553)", "**18.3**, comunicaciones: correspondencia (579.3) y comunicaciones telefónicas y telemáticas (588 ter d.3) ordenadas en urgencia por Interior", "Cargo público con auto de procesamiento **firme** y en **prisión provisional**: suspensión **automática** mientras dure la prisión (384 bis)"],
        ["Detención: **72 horas** + prórroga de **otras 48**; se pide motivadamente **en las primeras 48** y el Juez decide **en las 24 siguientes** (520 bis.1)", "Incomunicación: el Juez se pronuncia en **24 horas**; mientras, el detenido queda incomunicado (520 bis.2)", "Incomunicación: máximo **5 días**; en causas del 384 bis, prórroga de **otros 5** como máximo; nunca a **menores de 16 años** (509)", "Incomunicado: al menos **dos reconocimientos médicos cada 24 horas** (527)", "Comunicaciones en urgencia: juez avisado en **24 horas**; revoca o confirma en **72 horas** (579.3)"],
        ["**72 + 48** horas (no 72 + 72)", "Urgencia: Ministro del **Interior** (no de Justicia)", f"Plazo general de referencia (520.1): {c('LEC', 520, 'en todo caso, en el plazo máximo de setenta y dos horas')}", "Enlace: si la detención se basa en esta ley orgánica, el *habeas corpus* lo conoce el **Juez Central de Instrucción** (→ II.4.2)", "*Así en el BOE:* el art. 579.1 dice «la comprobación del algún hecho»"])}

{resumen(["**Suspender** no es **limitar**: la alarma solo limita; excepción y sitio suspenden los derechos del 55.1.",
          "Quién decide: alarma y excepción, el **Gobierno** (en la excepción, con autorización previa del Congreso); sitio, el **Congreso** por mayoría absoluta.",
          "Duración: alarma **15** días; excepción **30 + 30**; sitio, lo que fije el Congreso.",
          "El **17.3** solo se suspende en el **sitio**.",
          "Suspensión **individual** (55.2): terrorismo, solo 17.2, 18.2 y 18.3, con juez y control parlamentario (LECrim)."],
         "Siguiente: bloque IV. Falta la institución que vela por los derechos en todo momento, también durante los estados de excepción y sitio: el Defensor del Pueblo.")}
""", 2)
