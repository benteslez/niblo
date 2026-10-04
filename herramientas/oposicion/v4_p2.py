# -*- coding: utf-8 -*-
# Tema I.2 (v4) · Parte 2: bloque I, Sección 1.ª (arts. 15 a 29).
from v4_util import *

SUSP_EXC_SITIO = "Suspendible: **sí**, en los estados de excepción y de sitio (art. 55.1 → III.2)"

ap("s3-1", "I.4 Sección 1.ª (I): la esfera personal (arts. 15 a 19)", f"""
La Sección 1.ª, «De los derechos fundamentales y de las libertades públicas», reúne los derechos con **protección máxima**. Todos comparten las mismas garantías (→ II.1); por eso, en sus fichas la casilla «Protección» destaca sobre todo **si el derecho puede suspenderse**.

Se estudia en cuatro grupos: esfera personal (15-19), comunicación y participación (20-23), garantías procesales y penales (24-26) y educación, sindicación, huelga y petición (27-29).

{unidad("4.1 Vida e integridad (art. 15)",
  lit("CE", 15, ["Todos tienen derecho a la vida y a la integridad física y moral", "salvo lo que puedan disponer las leyes penales militares para tiempos de guerra"]),
  ficha(f"{c('CE', 15, 'Todos')} (no solo los españoles)",
        ["Vida", "Integridad **física y moral**", f"Prohibición absoluta, {c('CE', 15, 'en ningún caso')}, de la tortura y de las penas o tratos inhumanos o degradantes", "Abolición de la pena de muerte"],
        "La única salvedad es la pena de muerte en las leyes penales militares para tiempos de guerra. *Dato, no texto legal: la LO 11/1995, de 27 de noviembre, de abolición de la pena de muerte en tiempo de guerra (BOE-A-1995-25714) [[BOE]], la abolió también en tiempo de guerra; la salvedad sigue en la Constitución*",
        [f"::{P_S1}", NO_SUSP],
        "«para **tiempos de guerra**», no «estado de sitio». Integridad «física **y moral**»."))}

{unidad("4.2 Libertad ideológica, religiosa y de culto (art. 16)",
  lit("CE", 16, ["sin más limitación, en sus manifestaciones, que la necesaria para el mantenimiento del orden público protegido por la ley", "Nadie podrá ser obligado a declarar sobre su ideología, religión o creencias", "Ninguna confesión tendrá carácter estatal"]),
  ficha(f"{c('CE', 16, 'los individuos y las comunidades')}",
        ["16.1, libertad ideológica, religiosa y de culto", "16.2, nadie puede ser obligado a declarar sobre su ideología, religión o creencias", f"16.3, aconfesionalidad del Estado y cooperación {c('CE', 16, 'con la Iglesia Católica y las demás confesiones')}"],
        "Uno solo, y solo en sus **manifestaciones**: el orden público protegido por la ley",
        [f"::{P_S1}", NO_SUSP],
        "Límite **único**: orden público. Aconfesional no es lo mismo que sin relación: hay **cooperación**."))}

{unidad("4.3 Libertad y seguridad personal (art. 17)",
  lit("CE", 17, ["en el plazo máximo de setenta y dos horas", "de forma inmediata, y de modo que le sea comprensible", "no pudiendo ser obligada a declarar", "habeas corpus", "plazo máximo de duración de la prisión provisional"]),
  ficha(f"{c('CE', 17, 'Toda persona')}",
        ["17.1, regla: libertad; privación solo en los casos y en la forma de la ley",
         "17.2, detención preventiva: lo estrictamente necesario y, como máximo, **72 horas**; después, libertad o disposición judicial",
         "17.3, derechos del detenido: información inmediata y comprensible de derechos y razones; no declarar; abogado",
         "17.4, *habeas corpus* (→ II.4) y plazo máximo de la prisión provisional, fijado por ley"],
        f"Solo {c('CE', 17, 'en los casos y en la forma previstos en la ley')}",
        [f"::{P_S1}; además, *habeas corpus*", f"{SUSP_EXC_SITIO}; el **17.3 solo en el de sitio**", "17.2: también suspensión **individual** por terrorismo (55.2 → III.9)"],
        f"72 horas es el **máximo**: la regla es {c('CE', 17, 'el tiempo estrictamente necesario')}. Información {c('CE', 17, 'de forma inmediata')}, no «en 24 horas»."))}

{unidad("4.4 Honor, intimidad, domicilio, comunicaciones e informática (art. 18)",
  lit("CE", 18, ["El domicilio es inviolable", "salvo en caso de flagrante delito", "salvo resolución judicial", "La ley limitará el uso de la informática"]),
  ficha(f"No se nombra titular: {c('CE', 18, 'Se garantiza el derecho')}…",
        ["18.1, honor, intimidad personal y familiar y propia imagen", "18.2, inviolabilidad del domicilio", "18.3, secreto de las comunicaciones, en especial postales, telegráficas y telefónicas", "18.4, la ley limitará el uso de la **informática** (base de la protección de datos)"],
        ["Domicilio, **tres** títulos: consentimiento del titular, resolución judicial o flagrante delito", "Comunicaciones, **uno**: resolución judicial"],
        [f"::{P_S1}", f"{SUSP_EXC_SITIO}: solo **18.2 y 18.3**; el 18.1, nunca", "18.2 y 18.3: también suspensión **individual** por terrorismo (55.2 → III.9)"],
        "En las comunicaciones **no** hay excepción por flagrante delito."))}

{unidad("4.5 Residencia y circulación (art. 19)",
  lit("CE", 19, ["Los españoles tienen derecho a elegir libremente su residencia", "no podrá ser limitado por motivos políticos o ideológicos"]),
  ficha(f"{c('CE', 19, 'Los españoles')} (los extranjeros, según el art. 13.1)",
        ["Elegir libremente la residencia", "Circular por el territorio nacional", "Entrar y salir libremente de España"],
        "Los términos de la ley; el derecho a entrar y salir no puede limitarse por motivos políticos o ideológicos",
        [f"::{P_S1}", SUSP_EXC_SITIO, "En la alarma solo puede **limitarse** (STC 148/2021 [[TC|https://hj.tribunalconstitucional.es/es-ES/Resolucion/Show/26778]] → III.8)"],
        "«motivos políticos **o ideológicos**». Titulares: los **españoles**."))}

!> **Idea clave del grupo.** Se pueden suspender **17, 18.2, 18.3 y 19**. Nunca: vida (15), libertad ideológica (16), honor e intimidad (18.1).
""", 2)

# ---------------------------------------------------------------------------
ap("s3-2", "I.5 Sección 1.ª (II): comunicación y participación (arts. 20 a 23)", f"""
Segundo grupo de la Sección 1.ª: las libertades para **comunicarse** y **participar** en la vida colectiva y política.

{unidad("5.1 Expresión e información (art. 20)",
  lit("CE", 20, ["libertad de cátedra", "información veraz", "cláusula de conciencia y al secreto profesional", "ningún tipo de censura previa", "protección de la juventud y de la infancia", "en virtud de resolución judicial"]),
  ficha(f"No se nombra titular: {c('CE', 20, 'Se reconocen y protegen los derechos')}",
        ["20.1 a), expresión de pensamientos, ideas y opiniones", "20.1 b), producción y creación literaria, artística, científica y técnica", "20.1 c), libertad de cátedra", "20.1 d), información **veraz**; la ley regula la cláusula de conciencia y el secreto profesional", "20.2, sin censura previa", "20.3, medios públicos: control parlamentario, acceso de los grupos significativos, pluralismo y lenguas de España"],
        ["20.4, el respeto a los demás derechos del Título I y a las leyes que lo desarrollen; en especial, honor, intimidad, propia imagen y protección de la juventud y de la infancia", "20.5, secuestro de publicaciones, grabaciones y otros medios **solo por resolución judicial**"],
        [f"::{P_S1}", f"{SUSP_EXC_SITIO}: solo **20.1 a) y d)** y **20.5**"],
        "Información «**veraz**». Secuestro: **solo** el juez, nunca la autoridad gubernativa."))}

{unidad("5.2 Reunión (art. 21)",
  lit("CE", 21, ["pacífica y sin armas", "no necesitará autorización previa", "comunicación previa", "con peligro para personas o bienes"]),
  ficha(f"No se nombra titular: {c('CE', 21, 'Se reconoce el derecho de reunión')}…",
        ["21.1, reunión pacífica y sin armas, sin autorización previa", "21.2, en lugares de tránsito público y manifestaciones: **comunicación previa** a la autoridad"],
        f"La autoridad solo puede prohibir {c('CE', 21, 'cuando existan razones fundadas de alteración del orden público, con peligro para personas o bienes')}",
        [f"::{P_S1}; recurso urgente contra la prohibición (art. 122 LJCA → II.3)", SUSP_EXC_SITIO],
        "«Comunicación previa», **no** «autorización previa». Prohibición: orden público **con peligro para personas o bienes**."))}

{unidad("5.3 Asociación (art. 22)",
  lit("CE", 22, ["a los solos efectos de publicidad", "en virtud de resolución judicial motivada", "secretas y las de carácter paramilitar"]),
  ficha(f"No se nombra titular: {c('CE', 22, 'Se reconoce el derecho de asociación')}",
        ["22.1, derecho de asociación", "22.3, inscripción en un registro **a los solos efectos de publicidad**"],
        ["22.2, ilegales: fines o medios tipificados como **delito**", "22.4, disolución o suspensión solo por **resolución judicial motivada**", "22.5, prohibidas las **secretas** y las **paramilitares**"],
        [f"::{P_S1}", NO_SUSP],
        "La inscripción **no** es constitutiva. El art. 34.2 aplica a las **fundaciones** los apartados **2 y 4** de este artículo (→ I.8.5)."))}

{unidad("5.4 Participación política y acceso a cargos públicos (art. 23)",
  lit("CE", 23, ["directamente o por medio de representantes", "sufragio universal", "en condiciones de igualdad a las funciones y cargos públicos, con los requisitos que señalen las leyes"]),
  ficha(f"{c('CE', 23, 'Los ciudadanos')}: solo los españoles, salvo el sufragio municipal (13.2 → I.2.3)",
        ["23.1, participar en los asuntos públicos directamente o por representantes elegidos en elecciones periódicas por sufragio universal", "23.2, acceder en condiciones de igualdad a las funciones y cargos públicos: base constitucional del acceso al empleo público"],
        "Los requisitos que señalen las leyes",
        [f"::{P_S1}", NO_SUSP],
        "El 23.2 **no** dice «mérito y capacidad»: eso está en el **art. 103.3**."))}

!> **Idea clave del grupo.** Se pueden suspender **20.1 a) y d), 20.5 y 21**. Nunca: asociación (22) ni participación (23).
""", 2)

# ---------------------------------------------------------------------------
ap("s3-3", "I.6 Sección 1.ª (III): garantías procesales y penales (arts. 24 a 26)", f"""
Tercer grupo: la protección de la persona **ante los tribunales** y **ante el poder sancionador** del Estado.

{unidad("6.1 Tutela judicial efectiva y garantías del proceso (art. 24)",
  lit("CE", 24, ["Todas las personas", "sin que, en ningún caso, pueda producirse indefensión", "Juez ordinario predeterminado por la ley", "presunción de inocencia", "por razón de parentesco o de secreto profesional"]),
  ficha([f"::24.1, {c('CE', 24, 'Todas las personas')}; 24.2, {c('CE', 24, 'Asimismo, todos tienen derecho')}…"],
        ["::24.1, tutela efectiva de jueces y tribunales, sin indefensión", "24.2: Juez ordinario predeterminado por la ley", "defensa y asistencia de letrado", "ser informados de la acusación", "proceso público sin dilaciones indebidas y con todas las garantías", "medios de prueba pertinentes", "no declarar contra sí mismos y no confesarse culpables", "presunción de inocencia"],
        "La ley regula cuándo no hay obligación de declarar por parentesco o secreto profesional",
        [f"::{P_S1}", NO_SUSP],
        f"{c('CE', 24, 'sin que, en ningún caso, pueda producirse indefensión')}. Dispensa de declarar: **parentesco o secreto profesional**."))}

{unidad("6.2 Legalidad penal y sancionadora; fines de la pena (art. 25)",
  lit("CE", 25, ["delito, falta o infracción administrativa", "reeducación y reinserción social", "no podrán consistir en trabajos forzados", "directa o subsidiariamente"]),
  ficha([f"::25.1, {c('CE', 25, 'Nadie puede ser condenado o sancionado')}…; 25.2, {c('CE', 25, 'El condenado a pena de prisión')}"],
        ["25.1, legalidad: nadie condenado o sancionado por hechos que no fueran delito, falta o **infracción administrativa** cuando se cometieron", "25.2, penas y medidas de seguridad orientadas a la reeducación y reinserción social; sin trabajos forzados; el condenado conserva sus derechos fundamentales y tiene derecho a trabajo remunerado, Seguridad Social, cultura y desarrollo de su personalidad", "25.3, la Administración civil no puede imponer sanciones privativas de libertad"],
        "Los derechos del condenado ceden ante el fallo, el sentido de la pena y la ley penitenciaria",
        [f"::{P_S1}", NO_SUSP],
        f"La legalidad alcanza a las **sanciones administrativas**. Sin privación de libertad {c('CE', 25, 'directa o subsidiariamente')}: la Administración **civil** (no la militar)."))}

{unidad("6.3 Prohibición de los Tribunales de Honor (art. 26)",
  lit("CE", 26, ["Administración civil y de las organizaciones profesionales"]),
  ficha("—",
        "Prohibición de los Tribunales de Honor",
        "—",
        [f"::{P_S1}", NO_SUSP],
        "En el ámbito de la Administración **civil** y de las **organizaciones profesionales**."))}
""", 2)

# ---------------------------------------------------------------------------
ap("s3-4", "I.7 Sección 1.ª (IV): educación, sindicación, huelga y petición (arts. 27 a 29)", f"""
Último grupo de la Sección 1.ª: un derecho de **prestación** (educación) y derechos de **acción colectiva** (sindicación, huelga y petición).

{unidad("7.1 Educación y libertad de enseñanza (art. 27)",
  lit("CE", 27, ["Todos tienen el derecho a la educación", "obligatoria y gratuita", "en su caso, los alumnos", "autonomía de las Universidades"]),
  ficha(f"{c('CE', 27, 'Todos')}; los padres, para la formación religiosa y moral de sus hijos (27.3)",
        ["27.1, derecho a la educación y libertad de enseñanza", "27.2, objeto: el pleno desarrollo de la personalidad humana", "27.3, formación religiosa y moral según las convicciones de los padres", "27.4, enseñanza básica obligatoria y gratuita", "27.5, programación general de la enseñanza y creación de centros", "27.6, libertad de creación de centros docentes", "27.7, profesores, padres y, en su caso, alumnos intervienen en los centros sostenidos con fondos públicos", "27.8, inspección y homologación", "27.9, ayudas a los centros", "27.10, autonomía de las Universidades"],
        ["27.2, el respeto a los principios democráticos de convivencia y a los derechos y libertades fundamentales", "27.6, creación de centros dentro del respeto a los principios constitucionales"],
        [f"::{P_S1}", NO_SUSP],
        f"Alumnos: {c('CE', 27, 'en su caso')}. Autonomía universitaria {c('CE', 27, 'en los términos que la ley establezca')}."))}

{unidad("7.2 Libertad sindical y huelga (art. 28)",
  lit("CE", 28, ["limitar o exceptuar", "regulará las peculiaridades de su ejercicio para los funcionarios públicos", "Nadie podrá ser obligado a afiliarse a un sindicato", "mantenimiento de los servicios esenciales de la comunidad"]),
  ficha([f"::28.1, {c('CE', 28, 'Todos tienen derecho a sindicarse libremente')}; 28.2, {c('CE', 28, 'los trabajadores')}"],
        ["28.1, libertad sindical: fundar sindicatos y afiliarse; los sindicatos pueden formar confederaciones y organizaciones internacionales; nadie obligado a afiliarse", "28.2, huelga de los trabajadores para la defensa de sus intereses"],
        ["Fuerzas o Institutos armados y Cuerpos con disciplina militar: la ley puede **limitar o exceptuar** la libertad sindical", "Funcionarios públicos: la ley regula sus **peculiaridades**", "Huelga: garantías para mantener los **servicios esenciales** de la comunidad"],
        [f"::{P_S1}", f"{SUSP_EXC_SITIO}: solo la **huelga (28.2)**; la libertad sindical (28.1), no"],
        "Los **jueces** no están aquí: su prohibición de sindicarse está en el **art. 127**."))}

{unidad("7.3 Petición (art. 29)",
  lit("CE", 29, ["individual y colectiva, por escrito", "sólo individualmente"]),
  ficha(f"{c('CE', 29, 'Todos los españoles')}",
        "Petición individual y colectiva, **por escrito**, en la forma y con los efectos que determine la ley",
        f"Miembros de las Fuerzas o Institutos armados y Cuerpos con disciplina militar: {c('CE', 29, 'sólo individualmente')} y según su legislación específica",
        [f"::{P_S1}", NO_SUSP],
        "Siempre **por escrito**. Militares: **solo individual**."))}

!> **Idea clave del grupo.** Solo se suspende la **huelga (28.2)**.
""", 2)
