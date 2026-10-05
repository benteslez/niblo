
# =============================================================================
# III. CONTENIDO: ARTÍCULOS 1 A 55
KEYU = {}   # artículo → clave de color de su unidad (la más específica)
def _clave(x, k):
    for a in x.get("arts", []): KEYU[a["n"]] = k
    for i, cp in enumerate(x.get("caps", []), 1):
        _clave(cp, f"{k}.{i}")
    for j, s in enumerate(x.get("secs", []), 1): _clave(s, f"{k}.{j}")
for _t in CEJ["titulos"]: _clave(_t, _t["id"])
assert KEYU[10] == "I" and KEYU[14] == "I.2" and KEYU[15] == "I.2.1" and KEYU[30] == "I.2.2" and KEYU[40] == "I.3" and KEYU[55] == "I.5"

def fila_art(n): return [tag(KEYU[n], f"Art. {n}"), rubrica(n) if n <= 52 else "", ""]
def tabla_arts(nums, ojo=None):
    return tabla(["Art.", "De qué trata (título de la guía M101)"], [[tag(KEYU[n], f"Art. {n}"), rubrica(n)] for n in nums])

NOTAS = {
 1: (["Estado social y democrático de Derecho", "la libertad, la justicia, la igualdad y el pluralismo político", "La soberanía nacional reside en el pueblo español", "Monarquía parlamentaria"],
     "Tres ideas, un apartado cada una: **valores superiores** (cuatro: libertad, justicia, igualdad y pluralismo político), **soberanía nacional** del pueblo español y **forma política** (Monarquía parlamentaria)."),
 2: (["indisoluble unidad de la Nación española", "derecho a la autonomía de las nacionalidades y regiones", "solidaridad entre todas ellas"], "Tres ideas: **unidad**, **autonomía** y **solidaridad**."),
 3: (["El castellano es la lengua española oficial del Estado", "Las demás lenguas españolas serán también oficiales en las respectivas Comunidades Autónomas de acuerdo con sus Estatutos"],
     "Del castellano hay **deber de conocerla** y **derecho a usarla**; las demás lenguas son oficiales en su Comunidad **según sus Estatutos**."),
 4: (["tres franjas horizontales, roja, amarilla y roja", "la amarilla de doble anchura"], "Rojo-amarillo-rojo: la franja **amarilla** es la de **doble anchura**."),
 5: (["villa de Madrid"], "La capital es la **villa** de Madrid."),
 6: (["Su estructura interna y funcionamiento deberán ser democráticos"], f"{IMP} **Estructura interna y funcionamiento democráticos**: lo exige la Constitución a los **partidos** (art. 6), a los **sindicatos y asociaciones empresariales** (art. 7), a los **Colegios Profesionales** (art. 36) y a las **organizaciones profesionales** (art. 52)."),
 7: (["libres dentro del respeto a la Constitución y a la ley"], "Mismo esquema que el art. 6: creación y actividad **libres** dentro del respeto a la Constitución y a la ley."),
 8: (["Ejército de Tierra, la Armada y el Ejército del Aire", "Una ley orgánica regulará las bases de la organización militar"], "Tres ejércitos (**Tierra, Armada y Aire**) y **ley orgánica** para las bases de la organización militar."),
 9: (["Los ciudadanos y los poderes públicos están sujetos a la Constitución", "reales y efectivas", "principio de legalidad, la jerarquía normativa, la publicidad de las normas, la irretroactividad de las disposiciones sancionadoras no favorables o restrictivas de derechos individuales, la seguridad jurídica, la responsabilidad y la interdicción de la arbitrariedad de los poderes públicos"],
     f"{IMP} **El art. 9.3 garantiza siete principios:** legalidad · jerarquía normativa · publicidad de las normas · irretroactividad de las sancionadoras no favorables o restrictivas de derechos individuales · seguridad jurídica · responsabilidad · interdicción de la arbitrariedad de los poderes públicos."),
 10: (["La dignidad de la persona", "derechos inviolables", "libre desarrollo de la personalidad", "Declaración Universal de Derechos Humanos"],
      f"El art. 10 queda **fuera de los capítulos**: es el **fundamento** del orden político. Su apartado 2 manda interpretar los derechos **conforme a la Declaración Universal de Derechos Humanos** y a los tratados ratificados por España."),
 11: (["se adquiere, se conserva y se pierde de acuerdo con lo establecido por la ley", "Ningún español de origen podrá ser privado de su nacionalidad"], "La nacionalidad se regula **por ley**; ningún español **de origen** puede ser privado de ella."),
 12: (["dieciocho años"], "Mayoría de edad: **dieciocho años**."),
 13: (["Solamente los españoles serán titulares de los derechos reconocidos en el artículo 23", "La extradición sólo se concederá en cumplimiento de un tratado o de la ley"], "Extranjeros: libertades **según tratados y ley**; sufragio (art. 23) solo para españoles, salvo reciprocidad **en elecciones municipales** (reforma de 1992); extradición y asilo."),
 14: (["Los españoles son iguales ante la ley", "nacimiento, raza, sexo, religión, opinión"], f"{IMP} El art. 14 está **dentro del capítulo II pero fuera de las secciones**. Tiene **tutela preferente y sumaria y amparo**, pero **no** reserva de ley orgánica (→ IV)."),
 15: (["derecho a la vida y a la integridad física y moral", "Queda abolida la pena de muerte"], "Vida e integridad física y moral; sin tortura ni tratos inhumanos o degradantes; **pena de muerte abolida** (salvo leyes penales militares en tiempos de guerra)."),
 16: (["Ninguna confesión tendrá carácter estatal", "Nadie podrá ser obligado a declarar sobre su ideología, religión o creencias"], "Libertad ideológica, religiosa y de culto; **ninguna confesión estatal**; nadie obligado a declarar sobre sus creencias."),
 17: (["setenta y dos horas", "Se garantiza la asistencia de abogado al detenido"], f"{IMP} **Detención preventiva: máximo 72 horas.** El **art. 17.3** (derechos del detenido) es el que **no se puede suspender en el estado de excepción** (→ VI)."),
 18: (["El domicilio es inviolable", "consentimiento del titular o resolución judicial, salvo en caso de flagrante delito", "secreto de las comunicaciones"], "Honor, intimidad e imagen · **domicilio inviolable** (18.2) · **secreto de las comunicaciones** (18.3). Los apartados 2 y 3 son **suspendibles** (→ VI)."),
 19: (["elegir libremente su residencia", "entrar y salir libremente de España"], "Residencia y circulación; entrar y salir de España **sin limitación por motivos políticos o ideológicos**."),
 20: (["Sólo podrá acordarse el secuestro de publicaciones, grabaciones y otros medios de información en virtud de resolución judicial", "no puede restringirse mediante ningún tipo de censura previa"], "Cuatro libertades en el apartado 1; **sin censura previa**; el **secuestro** de publicaciones, solo por **resolución judicial**. Suspendibles: 20.1 a) y d) y 20.5."),
 21: (["no necesitará autorización previa", "comunicación previa a la autoridad"], "Reunión **sin autorización previa**; en lugares de tránsito público y manifestaciones, **comunicación previa**."),
 22: (["resolución judicial motivada", "Se prohíben las asociaciones secretas y las de carácter paramilitar"], "Las asociaciones solo se disuelven o suspenden por **resolución judicial motivada**; se inscriben en un registro **a solo efectos de publicidad**."),
 23: (["participar en los asuntos públicos", "acceder en condiciones de igualdad a las funciones y cargos públicos"], "**23.1** participación política (directa o por representantes); **23.2** acceso a **funciones y cargos públicos** en condiciones de igualdad: el derecho de los opositores."),
 24: (["tutela efectiva de los jueces y tribunales", "Juez ordinario predeterminado por la ley", "presunción de inocencia"], "**Tutela judicial efectiva** sin indefensión (24.1) y las garantías del proceso (24.2): juez predeterminado, defensa, letrado, proceso público sin dilaciones, pruebas, no declarar contra sí mismo, presunción de inocencia."),
 25: (["no constituyan delito, falta o infracción administrativa", "reeducación y reinserción social", "no podrán consistir en trabajos forzados", "La Administración civil no podrá imponer sanciones que, directa o subsidiariamente, impliquen privación de libertad"], "**Legalidad penal** (25.1) · penas orientadas a la **reinserción** (25.2) · la Administración civil **no puede imponer privación de libertad** (25.3)."),
 26: (["Se prohíben los Tribunales de Honor"], "**Tribunales de Honor prohibidos** en la Administración civil y las organizaciones profesionales."),
 27: (["La enseñanza básica es obligatoria y gratuita", "autonomía de las Universidades"], "Derecho a la educación y libertad de enseñanza; enseñanza básica **obligatoria y gratuita**; **autonomía universitaria**."),
 28: (["Todos tienen derecho a sindicarse libremente", "derecho a la huelga de los trabajadores"], "Libertad sindical (28.1) y **huelga** (28.2); la ley asegura los **servicios esenciales**. El 28.2 es **suspendible** (→ VI)."),
 29: (["derecho de petición individual y colectiva, por escrito"], "Petición **individual y colectiva, por escrito**. Los militares, solo **individualmente**. Es el **último** artículo de la sección 1.ª."),
 30: (["objeción de conciencia", "servicio militar obligatorio"], f"**Derecho y deber** de defender a España (30.1). El **30.2** (objeción de conciencia) es el **único** de la sección 2.ª que tiene **amparo** (→ IV)."),
 31: (["capacidad económica", "igualdad y progresividad", "alcance confiscatorio"], "Deber de contribuir a los gastos públicos según la **capacidad económica**, con un sistema tributario **justo, igual y progresivo**, nunca confiscatorio."),
 32: (["plena igualdad jurídica"], "Matrimonio entre el hombre y la mujer con **plena igualdad jurídica**."),
 33: (["derecho a la propiedad privada y a la herencia", "La función social", "utilidad pública o interés social, mediante la correspondiente indemnización"], f"{IMP} La propiedad privada **no es un derecho fundamental** (sección 2.ª): sin amparo ni ley orgánica. Su contenido lo delimita la **función social**; solo se priva de bienes por **utilidad pública o interés social** con **indemnización**."),
 34: (["derecho de fundación para fines de interés general"], "Derecho de fundación para **fines de interés general**."),
 35: (["deber de trabajar y el derecho al trabajo"], "**Deber** de trabajar y **derecho** al trabajo, a la libre elección de profesión, a la promoción y a una remuneración suficiente, **sin discriminación por sexo**."),
 36: (["La estructura interna y el funcionamiento de los Colegios deberán ser democráticos"], "Colegios Profesionales: ley propia y **estructura democrática**."),
 37: (["negociación colectiva laboral", "medidas de conflicto colectivo"], "**Negociación colectiva** (37.1) y **conflicto colectivo** (37.2, suspendible en excepción y sitio)."),
 38: (["libertad de empresa en el marco de la economía de mercado"], "Es el **último** artículo del capítulo II (sección 2.ª). Libertad de empresa en la **economía de mercado**."),
 39: (["protección social, económica y jurídica de la familia"], "**Familia, hijos y madres**. Primer artículo del capítulo tercero: **principios rectores**, no derechos fundamentales."),
 40: (["pleno empleo"], "Progreso social y económico, distribución de la renta, **pleno empleo**, formación, seguridad e higiene, descanso."),
 41: (["régimen público de Seguridad Social para todos los ciudadanos"], "**Régimen público de Seguridad Social**; las prestaciones complementarias son **libres**."),
 42: (["trabajadores españoles en el extranjero"], "La guía M101 lo titula «inmigrantes españoles en el extranjero»; la CE dice **trabajadores españoles en el extranjero** y su **retorno**."),
 43: (["derecho a la protección de la salud"], f"{IMP} La **salud** es un derecho **del capítulo III**: sin amparo ni recurso de inconstitucionalidad por sí mismo; solo se alega ante la jurisdicción ordinaria **según las leyes que lo desarrollen**."),
 44: (["acceso a la cultura"], "**Cultura** y **ciencia e investigación**."),
 45: (["medio ambiente adecuado"], "**Medio ambiente** adecuado: derecho **y deber** de conservarlo."),
 46: (["patrimonio histórico, cultural y artístico"], "Conservación y enriquecimiento del **patrimonio histórico, cultural y artístico**."),
 47: (["derecho a disfrutar de una vivienda digna y adecuada"], f"{IMP} La **vivienda** (como la salud) es del **capítulo III**: se queda fuera de la protección del amparo y de la reserva de ley orgánica (→ V.7)."),
 48: (["juventud"], "**Participación de la juventud**."),
 49: (["personas con discapacidad"], "**Discapacidad**: artículo reformado en **2024** (→ I.2)."),
 50: (["tercera edad"], "**Pensiones** adecuadas y actualizadas y servicios sociales para la **tercera edad**."),
 51: (["consumidores y usuarios"], "**Consumidores y usuarios**."),
 52: (["organizaciones profesionales"], "**Organizaciones profesionales** con estructura interna **democrática**. Es el **último** artículo del capítulo III."),
}
PROXIMO = {}
def arts_lit(ap, nums):
    out = []
    for k, n in enumerate(nums, 1):
        res, nota = NOTAS[n]
        out.append(unidad(f"{ap}.{k} Art. {n} · {rubrica(n)}", lit("CE", f"a{n}", res), nota))
    return "\n\n".join(out)

T.ap("bIII", "III. ¿De qué trata cada artículo? Los artículos 1 a 55", donde(
  "Tercera pregunta. La Constitución no pone título a sus artículos: los títulos que se usan para estudiar son una ayuda. Aquí tienes **de qué trata cada uno** y, debajo, su **texto literal** para la **lectura profunda** que pide el módulo.",
  ["1 Cómo estudiar los artículos", "2 Cuadro: de qué trata cada artículo", "3 a 7 Lectura profunda del texto literal, por unidades"]))

T.ap("s9", "III.1 Cómo estudiar los artículos 1 a 55", f"""
{IMP} **Primera meta:** saber **de qué trata cada artículo** y **dónde está** en la estructura. Preguntan directamente cosas como «¿qué regula el artículo 20?» (la libertad de expresión). La Constitución es la única norma por la que se pregunta así.

- **Del 1 al 38 y del 53 al 55: hay que saber de qué trata cada uno.** Las preguntas se resuelven con eso.
- **Del 39 al 52** (principios rectores): también conviene saber de qué tratan, sobre todo para **distinguirlos de los derechos** de los capítulos anteriores. Los examinadores intentan **meter como derechos fundamentales** cosas que no lo son: la salud, la vivienda, la redistribución de la renta, la **propiedad privada**… (→ V.7).
- A la vez, **ubícalos**: cuando leas el art. 12 pregúntate «¿dónde estaba?» (capítulo I del título I). Ponerte a prueba así es la forma de aprender la estructura.
- Segunda meta, en vueltas posteriores: la **lectura profunda** de los 55 artículos hasta captar la «música», de modo que una palabra cambiada te haga saltar la alarma. **No hace falta saberlos literalmente.**
- Para entrenarlo, usa el {ir("#/ce/test", "🧭 Test Constitución")}: te sale el número y tienes que decir de qué trata.

{ir("#/ce/texto", "📜 Constitución completa")} {ir("#/ce/organigrama", "🗺 Organigrama")}
""", 2)

T.ap("s10", "III.2 Cuadro: de qué trata cada artículo (1 a 55)", f"""
Cada artículo lleva el **color** de su título, capítulo o sección. Los títulos son los de la guía M101 (no son texto de la Constitución).

### {tag("P", "Título preliminar")} · arts. 1 a 9

{tabla_arts(range(1, 10))}

### {tag("I", "Título I")} · art. 10 y {tag("I.1", "capítulo primero")} (arts. 11 a 13)

{tabla_arts(range(10, 14))}

### {tag("I.2", "Capítulo segundo")} · art. 14 y {tag("I.2.1", "sección 1.ª")} (arts. 15 a 29) {IMP}

{tabla_arts(range(14, 30))}

### {tag("I.2.2", "Sección 2.ª")} · arts. 30 a 38

{tabla_arts(range(30, 39))}

### {tag("I.3", "Capítulo tercero")} · arts. 39 a 52

{tabla_arts(range(39, 53))}

### {tag("I.4", "Capítulo cuarto")} y {tag("I.5", "quinto")} · arts. 53 a 55

| Art. | De qué trata |
|---|---|
| {tag("I.4", "Art. 53")} | Vinculación de los poderes públicos, reserva de ley y tutela de los derechos (→ V) |
| {tag("I.4", "Art. 54")} | El Defensor del Pueblo (→ VIII) |
| {tag("I.5", "Art. 55")} | Suspensión de derechos y libertades (→ VI) |

*Los arts. 53 a 55 no figuran en la tabla de la guía: el rótulo es nuestro.*
""", 2)

T.ap("s11", "III.3 Lectura profunda: Título preliminar (arts. 1 a 9)", f"""
Es el {tag("P", "Título preliminar")}: no tiene nombre. Sienta los **principios del Estado**: forma, valores, soberanía, unidad y autonomía, lenguas, símbolos, capital, partidos, sindicatos, Fuerzas Armadas y sujeción a la Constitución.

{arts_lit("3", range(1, 10))}
""", 2)

T.ap("s12", "III.4 Lectura profunda: art. 10 y capítulo primero (arts. 10 a 13)", f"""
{tag("I", "Título I")}: «De los derechos y deberes fundamentales». El **art. 10** va fuera de los capítulos; el {tag("I.1", "capítulo primero")} trata «de los españoles y los extranjeros».

{arts_lit("4", range(10, 14))}
""", 2)

T.ap("s13", "III.5 Lectura profunda: art. 14 y sección 1.ª (arts. 14 a 29)", f"""
{IMP} Los derechos de la {tag("I.2.1", "sección 1.ª")} (arts. **15 a 29**) son los **derechos fundamentales y libertades públicas**: los que tienen **más garantías** (→ IV). El art. 14 va aparte.

{arts_lit("5", range(14, 30))}
""", 2)

T.ap("s14", "III.6 Lectura profunda: sección 2.ª (arts. 30 a 38)", f"""
La {tag("I.2.2", "sección 2.ª")}, «De los derechos y deberes de los ciudadanos», reúne **derechos y deberes** con menos garantías que la sección 1.ª: vinculan a los poderes públicos y se protegen con el recurso de inconstitucionalidad, pero **no** tienen reserva de ley orgánica, ni tutela preferente y sumaria, ni amparo (salvo el art. **30.2**).

{arts_lit("6", range(30, 39))}
""", 2)

T.ap("s15", "III.7 Lectura profunda: capítulo tercero (arts. 39 a 52)", f"""
El {tag("I.3", "capítulo tercero")}, «De los principios rectores de la política social y económica», contiene **principios**, no derechos fundamentales: orientan a los poderes públicos, pero solo se pueden alegar ante la jurisdicción ordinaria **según lo que digan las leyes que los desarrollen** (art. 53.3, → V.7).

{arts_lit("7", range(39, 53))}
""", 2)
