# -*- coding: utf-8 -*-
# Tema I.2 (v4) · Parte 6: bloque IV, el Defensor del Pueblo.
from v4_util import *
from v4_examen import EX2

ap("bIV", "IV. ¿Quién vela por ellos? El Defensor del Pueblo (art. 54, LO 3/1981 y Ley 36/1985)", f"""
{donde("Los bloques II y III han mostrado las garantías **normativas** y **jurisdiccionales** y su suspensión. Falta la garantía **institucional**: una institución que supervisa a la Administración y no se interrumpe ni siquiera en los estados de excepción y sitio.",
       ["1 Art. 54 y naturaleza", "2 Elección", "3 Estatuto", "4 Ámbito y quejas", "5 Investigación", "6 Resoluciones e informes", "7 Defensores autonómicos (Ley 36/1985)", "8 La institución hoy"])}

**Orden de estudio.** El art. 54 CE y, después, la **Ley Orgánica 3/1981, de 6 de abril, del Defensor del Pueblo** (BOE-A-1981-10325; última modificación: 4 de noviembre de 2009) en el orden de sus artículos. Al final, la Ley 36/1985 sobre los defensores autonómicos.
""")

# ---------------------------------------------------------------------------
ap("s7", "IV.1 El art. 54 y la naturaleza del Defensor del Pueblo", f"""
La garantía **institucional** de los derechos: una institución que recibe quejas y **supervisa a la Administración**, primero en la Constitución (art. 54) y después en su ley orgánica (art. 1 LO 3/1981).

{unidad("1.1 El Defensor del Pueblo en la Constitución (art. 54)",
  lit("CE", 54, ["Una ley orgánica", "alto comisionado de las Cortes Generales", "los derechos comprendidos en este Título", "supervisar la actividad de la Administración", "dando cuenta a las Cortes Generales"]),
  fichab("La garantía **institucional** de los derechos del Título I",
         "**Alto comisionado de las Cortes Generales**, designado por ellas",
         ["Defiende los derechos del **Título I**", "Para ello, puede **supervisar la actividad de la Administración**", "Da cuenta a las **Cortes Generales**"],
         "Regulación por **ley orgánica**",
         ["De las **Cortes Generales**, no solo del Congreso", "Está en el **Capítulo cuarto** (garantías), no en un título propio"]))}

{unidad("1.2 Carácter y finalidad (art. 1 LO 3/1981)",
  lit("LO3", "primero", ["alto comisionado de las Cortes Generales", "Título I de la Constitución"]),
  fichab("Comisionado parlamentario para la defensa de los derechos del Título I",
         "El Defensor del Pueblo, designado por las Cortes Generales",
         ["Supervisa la actividad de la **Administración**, dando cuenta a las Cortes", "Actúa con **independencia** (art. 6.1 → IV.3.2)", "Sus resoluciones **no son vinculantes**: no anula actos (art. 28.1 → IV.6.1)"],
         "—",
         "No supervisa a los **jueces** (art. 13 → IV.4.4) ni al **legislador**."))}
""", 2)

# ---------------------------------------------------------------------------
ap("s7-1", "IV.2 Elección y nombramiento (arts. 2 a 4 LO 3/1981)", f"""
{unidad("2.1 Elección (art. 2)",
  lit("LO3", "segundo", ["cinco años", "mayoría simple", "no inferior a diez días", "tres quintas partes", "plazo máximo de veinte días", "en el plazo máximo de un mes", "mayoría absoluta del Senado", "conformidad previa"]),
  fichab("Cómo eligen las Cortes al Defensor del Pueblo",
         ["Una **Comisión Mixta** Congreso-Senado propone; el **Pleno del Congreso** vota; el **Senado** ratifica", "La Comisión se reúne cuando lo acuerdan los Presidentes de ambas Cámaras y, en todo caso, para proponer candidatos; decide por **mayoría simple**", "Se relaciona con las Cortes a través de los **Presidentes del Congreso y del Senado**"],
         ["1 Propuesta de la Comisión Mixta", "2 Votación en el Pleno del Congreso", "3 Ratificación en el Senado", "Si fracasa: nueva sesión de la Comisión y **sucesivas propuestas**", "Designado el Defensor, la Comisión da su **conformidad previa** a los Adjuntos que proponga"],
         ["Mandato: **5 años**", "Pleno del Congreso convocado en término **no inferior a 10 días**; **tres quintos**", "Senado: en un plazo máximo de **20 días**; la **misma mayoría**", "Si no se alcanzan: Comisión en **un mes** máximo; después basta **tres quintos en el Congreso** y **mayoría absoluta en el Senado**"],
         ["Si fracasa: Comisión (no «Pleno conjunto»), **un mes** (no quince días) y **mayoría absoluta del Senado** (no simple)", "Cayó en 2025: pregunta real justo debajo"]))}

{EX2}

{unidad("2.2 Requisitos, nombramiento y toma de posesión (arts. 3 y 4)",
  lit("LO3", "tercero", ["español mayor de edad"]),
  lit("LO3", "cuarto", ["conjuntamente con sus firmas", "Mesas de ambas Cámaras reunidas conjuntamente"]),
  fichab("Quién puede serlo y cómo se formaliza",
         f"{c('LO3', 'tercero', 'cualquier español mayor de edad que se encuentre en el pleno disfrute de sus derechos civiles y políticos')}",
         ["Nombramiento: los **Presidentes del Congreso y del Senado** lo acreditan conjuntamente con sus firmas; se publica en el **BOE** (4.1)", "Toma de posesión ante las **Mesas de ambas Cámaras reunidas conjuntamente**, con juramento o promesa (4.2)"],
         "—",
         "Firman los **dos Presidentes**; toma posesión ante las **Mesas** (no ante los Plenos)."))}
""", 2)

# ---------------------------------------------------------------------------
ap("s7-2", "IV.3 Estatuto: cese, prerrogativas, incompatibilidades y Adjuntos (arts. 5 a 8)", f"""
{unidad("3.1 Cese y vacante (art. 5)",
  lit("LO3", "quinto", ["notoria negligencia", "delito doloso", "Presidente del Congreso", "tres quintas partes de los componentes de cada Cámara", "en plazo no superior a un mes", "en su propio orden"]),
  fichab("Por qué cesa y quién declara la vacante",
         ["**Presidente del Congreso**: vacante por muerte, renuncia o expiración del mandato", "**Cada Cámara**, en los demás casos", "**Adjuntos**: ejercen interinamente, en su propio orden, hasta el nuevo nombramiento"],
         ["::Cinco causas (5.1):", "renuncia", "expiración del plazo", "muerte o incapacidad sobrevenida", "**notoria negligencia** en el cumplimiento de sus obligaciones y deberes", "condena por **delito doloso** en sentencia firme"],
         ["Negligencia o condena: **tres quintos** de los componentes de cada Cámara, con debate y audiencia del interesado (5.2)", "Nuevo nombramiento: iniciar en plazo **no superior a un mes** (5.3)"],
         "La pérdida de confianza de las Cortes **no** es causa de cese."))}

{unidad("3.2 Independencia y prerrogativas (art. 6)",
  lit("LO3", "sexto", ["no estará sujeto a mandato imperativo alguno", "gozará de inviolabilidad", "flagrante delito", "Sala de lo Penal del Tribunal Supremo"]),
  fichab("Las garantías personales del Defensor",
         "El Defensor y, por extensión (6.4), los **Adjuntos**",
         ["**Independencia** (6.1): sin mandato imperativo ni instrucciones; actúa con autonomía y según su criterio", "**Inviolabilidad** (6.2): no puede ser detenido, expedientado, multado, perseguido o juzgado por sus opiniones o actos en el ejercicio del cargo", f"**Inmunidad** (6.3): en los demás casos, solo detenido o retenido {c('LO3', 'sexto', 'en caso de flagrante delito')}", "**Fuero** (6.3): inculpación, prisión, procesamiento y juicio, exclusivamente la **Sala de lo Penal del Tribunal Supremo**"],
         "—",
         "Fuero: **Sala de lo Penal del Tribunal Supremo** (no el TC ni la Audiencia Nacional). Los defensores autonómicos, el **TSJ** (→ IV.7)."))}

{unidad("3.3 Incompatibilidades (art. 7)",
  lit("LO3", "séptimo", ["dentro de los diez días siguientes a su nombramiento y antes de tomar posesión"]),
  fichab("Qué no puede compatibilizar",
         "El Defensor y los Adjuntos (8.4)",
         ["::Incompatible con (7.1):", "todo mandato representativo", "todo cargo político o actividad de propaganda política", "el servicio activo en cualquier Administración", "la afiliación a un partido o funciones directivas en un partido, sindicato, asociación o fundación, o el empleo al servicio de los mismos", "las carreras **judicial y fiscal**", "cualquier actividad profesional, liberal, mercantil o laboral"],
         ["Cesar en la causa de incompatibilidad **en 10 días** desde el nombramiento y antes de tomar posesión; si no, **no acepta** el nombramiento (7.2)", "Incompatibilidad sobrevenida: se entiende que **renuncia** en la fecha en que se produjo (7.3)"],
         "Antes: «no acepta». Después: «renuncia»."))}

{unidad("3.4 Los Adjuntos (art. 8)",
  lit("LO3", "octavo", ["Adjunto Primero y un Adjunto Segundo", "previa conformidad de las Cámaras"]),
  fichab("Los colaboradores directos del Defensor",
         "Un **Adjunto Primero** y un **Adjunto Segundo**",
         ["Le auxilian; puede **delegarles** funciones; le **sustituyen por su orden** en caso de imposibilidad temporal o cese (8.1)", "El Defensor los nombra y separa **previa conformidad de las Cámaras** (8.2)", "Se les aplican los arts. 3, 6 y 7: requisitos, prerrogativas e incompatibilidades (8.4)"],
         "—",
         "Los nombra **el Defensor**, con conformidad previa de las Cámaras (en la práctica, de la Comisión Mixta, art. 2.6)."))}
""", 2)

# ---------------------------------------------------------------------------
ap("s7-3", "IV.4 Ámbito de actuación y quejas (arts. 9 a 17)", f"""
{unidad("4.1 Objeto de la supervisión (art. 9)",
  lit("LO3", "noveno", ["de oficio o a petición de parte", "artículo ciento tres, uno"]),
  fichab("Qué investiga",
         "Ministros, autoridades administrativas, funcionarios y cualquier persona al servicio de las Administraciones (9.2)",
         ["Investigaciones **de oficio o a petición de parte** sobre actos y resoluciones de la **Administración pública** y sus agentes", "Criterios: el **art. 103.1 CE** y el respeto a los derechos del Título I"],
         "—",
         "Mide a la Administración con el **art. 103.1** CE (objetividad, eficacia, sometimiento a la ley)."))}

{unidad("4.2 Quién puede presentar quejas (art. 10)",
  lit("LO3", "diez", ["toda persona natural o jurídica que invoque un interés legítimo", "ninguna autoridad administrativa en asuntos de su competencia"]),
  fichab("Legitimación para acudir al Defensor",
         [f"{c('LO3', 'diez', 'toda persona natural o jurídica que invoque un interés legítimo, sin restricción alguna')}", "Diputados y Senadores individualmente, comisiones de investigación o de derechos y, principalmente, la **Comisión Mixta**, por escrito motivado (10.2)"],
         "No impiden la queja la nacionalidad, la residencia, el sexo, la minoría de edad, la incapacidad legal, el internamiento penitenciario ni ninguna relación especial de sujeción",
         "—",
         "Exclusión (10.3): **ninguna autoridad administrativa en asuntos de su competencia**."))}

{unidad("4.3 Continuidad de su actividad (art. 11)",
  lit("LO3", "once", ["Diputaciones Permanentes", "excepción o de sitio"]),
  fichab("La institución no se detiene",
         "El Defensor; se dirige a las **Diputaciones Permanentes** si las Cámaras no están reunidas, se han disuelto o ha expirado su mandato",
         [f"{c('LO3', 'once', 'La declaración de los estados de excepción o de sitio no interrumpirán la actividad del Defensor del Pueblo, ni el derecho de los ciudadanos de acceder al mismo')} (11.3)"],
         "—",
         "Enlace con el bloque III: sigue actuando en **excepción y sitio** (→ III.7)."))}

{unidad("4.4 Comunidades Autónomas, Administración de Justicia y Administración Militar (arts. 12 a 14)",
  lit("LO3", "doce", []),
  lit("LO3", "trece", ["Ministerio Fiscal", "Consejo General del Poder Judicial"]),
  lit("LO3", "catorce", []),
  fichab("Hasta dónde llega su supervisión",
         ["CC. AA. (12): puede supervisarlas **por sí mismo**; los órganos autonómicos similares coordinan sus funciones con él (→ IV.7)", "Justicia (13): **no** la supervisa; remite las quejas al **Ministerio Fiscal** o al **CGPJ**", "Militar (14): vela por los derechos en ella, sin interferir en el **mando** de la Defensa Nacional"],
         "—",
         "—",
         "Quejas sobre la **Justicia**: al Ministerio Fiscal o al Consejo General del Poder Judicial, según el tipo de reclamación."))}

{unidad("4.5 La queja y su correspondencia (arts. 15 y 16)",
  lit("LO3", "quince", ["en el plazo máximo de un año", "gratuitas"]),
  lit("LO3", "dieciséis", []),
  fichab("Cómo se presenta una queja",
         "El interesado",
         ["Firmada, con nombre, apellidos y domicilio, en escrito razonado en papel común (15.1)", "Actuaciones **gratuitas**, sin Letrado ni Procurador (15.2)", f"Correspondencia desde centros de detención, internamiento o custodia: {c('LO3', 'dieciséis', 'no podrá ser objeto de censura de ningún tipo')}; las conversaciones no pueden ser escuchadas (16)"],
         "**Un año** desde que se conocieron los hechos (15.1)",
         "Plazo: **un año**. Sin abogado ni procurador."))}

{unidad("4.6 Admisión y rechazo (art. 17)",
  lit("LO3", "diecisiete", ["pendiente resolución judicial", "rechazará las quejas anónimas", "Sus decisiones no serán susceptibles de recurso"]),
  fichab("Qué quejas se tramitan",
         "El Defensor",
         ["Registro y acuse; tramitación o rechazo por **escrito motivado** (17.1)", "No examina individualmente las quejas **pendientes de resolución judicial** y suspende el examen si se interpone demanda o recurso; puede investigar los problemas generales (17.2)", "Rechaza **siempre** las **anónimas**; **puede** rechazar las de mala fe, sin fundamento o sin pretensión, y las que perjudiquen a terceros (17.3)"],
         "—",
         "Anónimas: **rechaza** (obligatorio). Mala fe: **podrá** rechazar. Sus decisiones **no son recurribles**."))}
""", 2)

# ---------------------------------------------------------------------------
ap("s7-7", "IV.5 La investigación y el deber de colaboración (arts. 18 a 27)", f"""
{unidad("5.1 Desarrollo de la investigación (arts. 18 a 21)",
  lit("LO3", "dieciocho", ["en el plazo máximo de quince días", "hostil y entorpecedora"]),
  lit("LO3", "diecinueve", ["con carácter preferente y urgente"]),
  lit("LO3", "veinte", ["que en ningún caso será inferior a diez días", "por la mitad del concedido"]),
  lit("LO3", "veintiuno", []),
  fichab("Cómo investiga una queja admitida",
         ["El organismo afectado, que debe informar", f"{c('LO3', 'diecinueve', 'Todos los poderes públicos están obligados a auxiliar, con carácter preferente y urgente, al Defensor del Pueblo')}", "El funcionario investigado y su superior"],
         [f"Investigación {c('LO3', 'dieciocho', 'sumaria e informal')} con petición de informe escrito (18.1)", "No enviar el informe puede considerarse **hostil y entorpecedor** y hacerse público (18.2)", "Puede personarse en cualquier centro de la Administración (19.2) y no se le puede negar el acceso a ningún expediente, salvo lo previsto para los secretos (19.3)", "Lo que aporte un funcionario con su testimonio es **reservado** (20.4)", "Si el superior prohíbe colaborar, debe hacerlo por escrito motivado; el Defensor se dirige entonces a él (21)"],
         ["Informe del organismo: **15 días**, ampliable (18.1)", "Respuesta del funcionario: **no menos de 10 días**, prorrogable **por la mitad** (20.2)"],
         "**15** días el organismo; **no menos de 10** el funcionario."))}

{unidad("5.2 Documentos y reserva (art. 22)",
  lit("LO3", "veintidós", ["deberá ser acordada por el Consejo de Ministros", "la más absoluta reserva"]),
  fichab("Acceso a documentos, incluidos los secretos",
         "El Defensor pide; el **Consejo de Ministros** puede denegar los secretos",
         ["Puede pedir todos los documentos necesarios, también los **secretos** (22.1)", "La no remisión la acuerda el **Consejo de Ministros**, con certificación del acuerdo (22.1)", "Investigaciones con la **más absoluta reserva** (22.2)", "Si un secreto no remitido puede afectar decisivamente a la investigación, lo comunica a la **Comisión Mixta** (22.3)"],
         "—",
         "Documentos secretos: decide el **Consejo de Ministros** (no un ministro)."))}

{unidad("5.3 Consecuencias de la investigación (arts. 23 a 27)",
  lit("LO3", "veintitrés", []),
  lit("LO3", "veinticuatro", ["informe especial"]),
  lit("LO3", "veinticinco", ["Fiscal General del Estado"]),
  lit("LO3", "veintiséis", ["de oficio"]),
  lit("LO3", "veintisiete", []),
  fichab("Qué hace si encuentra irregularidades",
         "El Defensor; el **Fiscal General del Estado**, ante delitos",
         ["Abuso, arbitrariedad, discriminación, error, negligencia u omisión de un funcionario: se dirige a él y traslada su criterio al superior (23)", "Actitud hostil persistente: **informe especial** y mención en el informe anual (24.1; el 24.2 está derogado)", "Hechos delictivos: al **Fiscal General del Estado**, que le informa periódicamente (25)", f"Acción de **responsabilidad** de oficio contra autoridades, funcionarios y agentes civiles, {c('LO3', 'veintiséis', 'sin que sea necesaria en ningún caso la previa reclamación por escrito')} (26)", "Resarce a los particulares llamados a informar que no promovieron la queja (27)"],
         "—",
         "Delitos: al **Fiscal General del Estado** (no al juez)."))}
""", 2)

# ---------------------------------------------------------------------------
ap("s7-4", "IV.6 Resoluciones, informes y medios (arts. 28 a 37, DT y DF única)", f"""
{unidad("6.1 Las resoluciones (arts. 28 a 31)",
  lit("LO3", "veintiocho", ["aun no siendo competente para modificar o anular"]),
  lit("LO3", "veintinueve", ["recursos de inconstitucionalidad y de amparo"]),
  lit("LO3", "treinta", ["advertencias, recomendaciones, recordatorios de sus deberes legales y sugerencias", "en término no superior al de un mes"]),
  lit("LO3", "treinta y uno", []),
  fichab("Qué puede hacer con el resultado: persuadir, no anular",
         ["Autoridades y funcionarios, que deben responder", "El interesado, el parlamentario o comisión que lo pidió y la autoridad afectada reciben el resultado (31)"],
         ["**No** modifica ni anula actos; puede sugerir cambiar los criterios (28.1)", "Si una norma provoca situaciones injustas, sugiere su **modificación** (28.2)", "Servicios prestados por particulares: insta a las autoridades a inspeccionar y sancionar (28.3)", "Legitimado para los recursos de **inconstitucionalidad y amparo** (29 → II.2.3)", "Formula **advertencias, recomendaciones, recordatorios de sus deberes legales y sugerencias** (30.1)", "Sin respuesta: acude al **Ministro** o máxima autoridad y, si sigue sin justificación, lo incluye en su informe **con nombres** (30.2)"],
         "Respuesta a sus resoluciones: **un mes** como máximo (30.1)",
         "Cuatro tipos de resolución: advertencias, recomendaciones, recordatorios y sugerencias. **Ninguna vinculante**."))}

{unidad("6.2 Los informes a las Cortes (arts. 32 y 33)",
  lit("LO3", "treinta y dos", ["cuando se hallen reunidas en periodo ordinario de sesiones", "Diputaciones Permanentes"]),
  lit("LO3", "treinta y tres", ["Un resumen del informe será expuesto oralmente"]),
  fichab("Cómo da cuenta a las Cortes",
         "Las **Cortes Generales**; si no están reunidas, las **Diputaciones Permanentes** (informe extraordinario)",
         ["**Anual**, en periodo ordinario de sesiones (32.1)", "**Extraordinario**, por gravedad o urgencia (32.2)", "Los informes se **publican** (32.3)", "Contenido del anual (33): quejas presentadas, rechazadas y sus causas, investigadas y su resultado; **sin datos personales**; anexo con la **liquidación del presupuesto**", f"{c('LO3', 'treinta y tres', 'Un resumen del informe será expuesto oralmente por el Defensor del Pueblo ante los Plenos de ambas Cámaras')}, con intervención de los grupos (33.4)"],
         "—",
         "Exposición **oral** de un **resumen** ante los **Plenos** de ambas Cámaras."))}

{unidad("6.3 Medios personales y económicos (arts. 34 a 37)",
  lit("LO3", "treinta y cuatro", []),
  lit("LO3", "treinta y cinco", ["persona al servicio de las Cortes"]),
  lit("LO3", "treinta y seis", ["cesarán automáticamente"]),
  lit("LO3", "treinta y siete", ["Presupuestos de las Cortes Generales"]),
  fichab("Personal y presupuesto",
         ["Asesores: los designa **libremente** (34)", "Su personal es **personal al servicio de las Cortes**; los funcionarios conservan plaza y destino (35)"],
         [f"{c('LO3', 'treinta y seis', 'Los adjuntos y asesores cesarán automáticamente en el momento de la toma de posesión de un nuevo Defensor del Pueblo')} (36)", "Presupuesto: una **partida** de los Presupuestos de las **Cortes Generales** (37)"],
         "—",
         ["Presupuesto: dentro de los de las **Cortes Generales**, no sección propia de los PGE", "*Así en el BOE:* el art. 36 dice «destinado por las Cortes»; el art. 31.3 termina en coma"]))}

{unidad("6.4 Disposición transitoria y Mecanismo Nacional de Prevención de la Tortura (DF única)",
  lit("LO3", "Disposición transitoria", []),
  lit("LO3", "Disposición final única", ["Mecanismo Nacional de Prevención de la Tortura", "Consejo Asesor"]),
  fichab("El Defensor como **Mecanismo Nacional de Prevención de la Tortura** (MNPT)",
         [f"El Defensor del Pueblo {c('LO3', 'Disposición final única', 'ejercerá las funciones del Mecanismo Nacional de Prevención de la Tortura')}", f"Un **Consejo Asesor**, {c('LO3', 'Disposición final única', 'que será presidido por el Adjunto en el que el Defensor del Pueblo delegue las funciones previstas en esta disposición')}"],
         "Conforme al Protocolo facultativo de la Convención contra la tortura",
         "—",
         "La introdujo la reforma de **2009**, la última de la ley. El Consejo Asesor lo preside el **Adjunto en quien delegue**, no el Defensor."))}
""", 2)

# ---------------------------------------------------------------------------
ap("s7-6", "IV.7 Los defensores autonómicos (Ley 36/1985)", f"""
Muchos Estatutos de Autonomía crean figuras similares al Defensor del Pueblo. Sus relaciones con él las regula la **Ley 36/1985, de 6 de noviembre** (BOE-A-1985-23210), ley **ordinaria** **no modificada**, que desarrolla la coordinación del art. 12.2 LO 3/1981 (→ IV.4.4).

{unidad("7.1 Estatuto de los comisionados autonómicos (art. 1)",
  lit("L36", "primero", ["Comisionados territoriales de las respectivas Asambleas Legislativas", "Sala correspondiente de los Tribunales Superiores de Justicia", "no interrumpirán la actividad de los Comisionados"]),
  fichab("Las garantías de los defensores autonómicos",
         [f"{c('L36', 'primero', 'Comisionados territoriales de las respectivas Asambleas Legislativas')}", "Sus **Adjuntos**, con las mismas prerrogativas (1.3)"],
         ["Inviolabilidad e inmunidad: las de los miembros de su **Asamblea** autonómica", f"Aforamiento: {c('L36', 'primero', 'la Sala correspondiente de los Tribunales Superiores de Justicia en cada ámbito territorial')}", "Se les aplican los arts. **16, 19, 24 y 26** LO 3/1981 y el **25.2** (este, con el **Fiscal** de su ámbito territorial) (1.2 a y b)", "Irregularidades de Administraciones **no autonómicas**: las notifican al Defensor del Pueblo (1.2 c)", "No se interrumpe su actividad en los estados de **excepción o de sitio** (1.4)"],
         "—",
         ["Fuero autonómico: **TSJ**. Fuero del Defensor del Pueblo: **Tribunal Supremo**", "*Así en el BOE:* el art. 1.4 dice «el derecho de las personas afectadas de acceder ellos»"]))}

{unidad("7.2 Cooperación con el Defensor del Pueblo (art. 2 y disposición adicional)",
  lit("L36", "segundo", ["competencias delegadas", "se concertarán entre ellos acuerdos", "podrá recabar la colaboración del respectivo Comisionado parlamentario"]),
  lit("L36", "Disposición adicional", ["servicios especiales"]),
  fichab("Cómo se coordinan las dos instituciones",
         "El Defensor del Pueblo y cada comisionado autonómico",
         [f"Cooperan en la supervisión de la Administración **autonómica** y de los **Entes Locales** cuando actúen por {c('L36', 'segundo', 'competencias delegadas')} de la Comunidad (2.1)", "Conciertan **acuerdos** sobre ámbitos de actuación, facultades, comunicación y duración (2.2)", "Administración del Estado en la Comunidad: el Defensor del Pueblo puede **recabar la colaboración** del comisionado autonómico y recibe de él las quejas (2.3)", "Funcionarios en activo nombrados comisionados: **servicios especiales** (DA)"],
         "—",
         "Sobre la Administración **del Estado**, la competencia sigue siendo del **Defensor del Pueblo**; el autonómico colabora."))}
""", 2)
