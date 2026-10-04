# -*- coding: utf-8 -*-
"""Tema III.5 (B3T05): La evolución del empleo en España. Los servicios públicos de
empleo: régimen de prestaciones y políticas de empleo.
Método del I.2. Normas (textos consolidados del BOE): CE, arts. 35, 40, 41 y 149.1.7.ª;
Ley 3/2023, de 28 de febrero, de Empleo; texto refundido de la Ley General de la Seguridad
Social (título III: protección por desempleo); Real Decreto 633/2025, de 15 de julio
(Estrategia Española de Apoyo Activo al Empleo 2025-2028: su diagnóstico del mercado de
trabajo, capítulo II, es la fuente de la «evolución del empleo»)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO["L3_2023"] = "Ley 3/2023, de Empleo"
CORTO["LGSS"] = "LGSS"
CORTO["RD633"] = "RD 633/2025"
L3, SS, RD = "L3_2023", "LGSS", "RD633"
DIAG, OBJ = "CAPÍTULO II", "CAPÍTULO III"   # capítulos de la Estrategia (anexo del RD 633/2025)
NOLEGAL = "*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*"

T = Tema("B3T05",
  "Cuatro preguntas: I. Cómo ha evolucionado el empleo en España (diagnóstico de la Estrategia 2025-2028, RD 633/2025) · II. Qué es la política de empleo y quién la gestiona: el Sistema Nacional de Empleo y los servicios públicos de empleo (CE, arts. 35, 40, 41 y 149.1.7.ª; Ley 3/2023) · III. Qué prestaciones protegen frente al desempleo (LGSS, arts. 262 a 303) · IV. Qué son las políticas activas de empleo y cómo se planifican (Ley 3/2023; RD 633/2025). Cada artículo: texto literal del BOE y ficha.",
  ["Ley 3/2023 de Empleo", "Sistema Nacional de Empleo", "Agencia Española de Empleo", "SEPE", "Conferencia Sectorial", "Estrategia 2025-2028", "Plan Anual (PAFED)", "Ejes", "Prestación contributiva", "Subsidio por desempleo", "Situación legal de desempleo", "Acuerdo de actividad", "Colocación adecuada", "Agencias de colocación", "Colectivos prioritarios", "Servicios garantizados"])

# =============================================================================
T.ap("s0", "Mapa del tema: cuatro preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque III, tema 5):
> La evolución del empleo en España. Los servicios públicos de empleo: régimen de prestaciones y políticas de empleo.

### El hilo conductor

| Bloque | Pregunta | Normas |
|---|---|---|
| **I** | ¿Cómo ha evolucionado el empleo en España? | RD 633/2025 (Estrategia Española de Apoyo Activo al Empleo 2025-2028), capítulos II y III |
| **II** | ¿Qué es la política de empleo y quién la gestiona? (los servicios públicos de empleo) | CE, arts. 35, 40, 41 y 149.1.7.ª; Ley 3/2023, arts. 1, 2, 6 a 10, 18 a 24, disposiciones adicional primera y transitoria segunda; LGSS, art. 294 |
| **III** | ¿Qué prestaciones protegen frente al desempleo? (régimen de prestaciones) | LGSS, arts. 262 a 280, 282, 299 a 301 y 303; Ley 3/2023, art. 3 |
| **IV** | ¿Qué son las políticas activas de empleo y cómo se planifican? (políticas de empleo) | Ley 3/2023, arts. 11 a 13, 31, 41 a 43, 47, 50, 56, 58 y 61; RD 633/2025 |

!> **La idea que une los cuatro bloques:** la **política de empleo** tiene dos patas (Ley 3/2023, art. 2): las **políticas activas** (orientar, formar, intermediar, fomentar la contratación) y la **protección frente al desempleo** (prestaciones y subsidios). Las gestionan los **servicios públicos de empleo** (la Agencia Española de Empleo —hasta su puesta en funcionamiento, el SEPE— y los de las Comunidades Autónomas) dentro del **Sistema Nacional de Empleo**. El diagnóstico de cómo ha evolucionado el empleo (I) es el punto de partida de la planificación (IV).

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen; o, para las prestaciones, Titulares · Contenido · Límites · Protección · ⚠ Ojo en el examen).
- El **bloque I** cita literalmente el **diagnóstico** de la Estrategia 2025-2028, publicado en el BOE como anexo del RD 633/2025: es un texto oficial, pero **no es un precepto legal**; las cifras son las que da la propia Estrategia (que cita como fuente la EPA del INE y Eurostat).
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
- Lo que el tema III.4 explica de la Seguridad Social en general (estructura, financiación, otras prestaciones) no se repite aquí (tema III.4).
""")

# =============================================================================
T.ap("bI", "I. ¿Cómo ha evolucionado el empleo en España? (RD 633/2025, Estrategia 2025-2028)", donde(
  "Primera pregunta del tema. El epígrafe empieza por la **evolución del empleo**. La fuente oficial es el diagnóstico que el Gobierno aprobó, como parte de la Estrategia Española de Apoyo Activo al Empleo 2025-2028, por el RD 633/2025 (BOE de 16-7-2025). La Ley 3/2023 exige que la Estrategia incluya ese diagnóstico (→ IV.2.1).",
  ["1 Evolución 2015-2024: paro, brecha de género, sectores y temporalidad", "2 Situación actual, retos y metas a 2028"]))

T.ap("s1", "I.1 Evolución 2015-2024: paro, brecha de género, sectores y temporalidad (Estrategia, cap. II.5)", f"""
?> **Qué es este texto.** Es el capítulo II («Escenario y tendencias del Mercado de Trabajo») de la Estrategia aprobada por el RD 633/2025: **texto oficial publicado en el BOE**, pero **no es una norma que establezca derechos u obligaciones**; es un diagnóstico, y sus cifras proceden, según la propia Estrategia, de la **EPA (INE)** al cuarto trimestre de cada año.

{unidad("1.1 La tasa de paro: descenso desde 2015, salvo 2020 (cap. II.5)",
  lit(RD, DIAG, ["significativo descenso desde el año 2015 de la tasa de paro", "pasando de una tasa del 46,24 % en el cuarto trimestre del 2015 al 24,90 % en el mismo trimestre de 2024"], solo=[41, 42, 43, 44, 45, 46], titulo="Estrategia 2025-2028, capítulo II, 5. Evolución de la situación del Mercado de Trabajo (RD 633/2025) · diagnóstico oficial, no es texto legal"),
  fichab("Tendencia del paro según el diagnóstico oficial",
         "Datos de la EPA (INE) citados por la Estrategia",
         ["Descenso de la tasa de paro desde **2015**, con la excepción de **2020** (pandemia)", "Reducción para todos los grupos de edad, más acentuada en los **menores de 25 años**"],
         f"Menores de 25: {c(RD, DIAG, 'del 46,24 % en el cuarto trimestre del 2015 al 24,90 % en el mismo trimestre de 2024')}",
         "Aun así, la de los **menores de 25** es la tasa de paro **más elevada** por grupos de edad."))}

{unidad("1.2 La brecha de género en el paro (cap. II.5)",
  lit(RD, DIAG, ["pasando de 3,03 puntos de diferencia entre sexos en 2015 a 4,16 en 2020", "hasta llegar en 2024 a una diferencia de 2,30", "129.700 mujeres paradas más que hombres"], solo=[50, 53], titulo="Estrategia 2025-2028, capítulo II, 5 (RD 633/2025) · diagnóstico oficial, no es texto legal"),
  fichab("Diferencia entre la tasa de paro de mujeres y hombres",
         "Datos de la EPA (INE) citados por la Estrategia",
         ["La brecha **aumenta hasta 2020** (3,03 → 4,16 puntos)", "Desde **2021** cambia la tendencia (3,22) hasta **2,30 puntos** en 2024"],
         f"Cuarto trimestre de 2024: {c(RD, DIAG, '129.700 mujeres paradas más que hombres')}",
         "La brecha **se acorta pero no se cierra**: la Estrategia la sitúa como uno de los principales retos del mercado laboral."))}

{unidad("1.3 Paro y ocupación por sectores (cap. II.5)",
  lit(RD, DIAG, ["pasando de un 58,53 % a finales de 2015 a un 47,3 % al cuarto trimestre de 2024", "que pasa de un 28,8 % a finales de 2015 a un 39,2 % en el cuarto trimestre de 2024", "más de tres cuartas partes de la población ocupada", "pasando de 14.588,3 miles de ocupados en 2020 a 16.721,3 mil en 2024"], solo=[57, 58, 63], titulo="Estrategia 2025-2028, capítulo II, 5 (RD 633/2025) · diagnóstico oficial, no es texto legal"),
  fichab("Distribución del paro y del empleo por sectores",
         "Datos de la EPA (INE) citados por la Estrategia",
         ["Baja el peso de quienes buscan **primer empleo** o están en **paro de larga duración** (58,53 % → 47,3 %)", "Sube el porcentaje de parados del **sector servicios** (28,8 % → 39,2 %)", "Servicios concentra **más de tres cuartas partes** de la población ocupada"],
         "Ocupados en servicios: 14.588,3 miles (2020) → 16.721,3 miles (2024)",
         "No confundir: el **58,53 % → 47,3 %** es el porcentaje de parados que buscan su **primer empleo** o están en **paro de larga duración**, no la tasa de paro."))}

{unidad("1.4 Indefinidos y temporales: el efecto de la reforma laboral (cap. II.5)",
  lit(RD, DIAG, ["un descenso del 27 % interanual de la contratación temporal y un aumento de casi el 13 % de la indefinida", "aumentan un 3,9 %", "una disminución interanual del 4,5 %"], solo=[69, 70, 71], titulo="Estrategia 2025-2028, capítulo II, 5 (RD 633/2025) · diagnóstico oficial, no es texto legal"),
  fichab("Evolución de la estabilidad del empleo asalariado",
         "Datos de la EPA (INE) citados por la Estrategia",
         ["**2022**: con la reforma laboral de finales de 2021, temporales −27 % y indefinidos casi +13 %", "**2023**: indefinidos +5,6 %, temporales −5,3 %", "**2024** (4.º trimestre): ocupados +2,5 %, indefinidos +3,9 %, temporales −4,5 %"],
         "Variaciones interanuales al cuarto trimestre",
         "La Estrategia lo lee como **mejoría de la estabilidad** del empleo frente a la temporalidad (→ I.2.1: la temporalidad sigue siendo alta en el sector público y entre los jóvenes)."))}
""", 2)

T.ap("s2", "I.2 Situación actual, retos y metas a 2028 (Estrategia, caps. II y III)", f"""
{unidad("2.1 Perspectivas y retos del mercado laboral (cap. II.2)",
  lit(RD, DIAG, ["el número de ocupados se incrementó en unas 486.100 personas", "cerca del 87,3 % correspondió a ocupados extranjeros o con doble nacionalidad", "alcanza sus mayores números en la serie histórica", "sigue siendo alta en el sector público y entre las personas más jóvenes", "alto nivel de desempleo de larga duración"], solo=[9, 10, 13, 14], titulo="Estrategia 2025-2028, capítulo II, 2. Perspectivas del mercado laboral (RD 633/2025) · diagnóstico oficial, no es texto legal"),
  fichab("Situación en 2024 y problemas que persisten",
         "Datos de la EPA y de afiliación citados por la Estrategia",
         ["2024: **+486.100 ocupados** (EPA), cerca del **87,3 %** extranjeros o con doble nacionalidad", "Afiliación: **+468.084** (diciembre 2024 sobre diciembre 2023), máximo de la serie", "Retos: **temporalidad** (sector público y jóvenes) y **paro de larga duración**"],
         "—",
         "La reforma laboral de 2021 redujo la temporalidad, **pero** sigue alta en el **sector público** y entre los **jóvenes**; el paro sigue alto respecto de los países del entorno por el **desempleo de larga duración**."))}

{unidad("2.2 Vacantes y transiciones (cap. II.2 y 4)",
  lit(RD, DIAG, ["la tasa de puestos de trabajo vacantes en España era del 0,9 %, frente al 2,3 % de en el ámbito de la UE (27) o el 2,5 % de la eurozona", "La falta de relevo generacional"], solo=[17, 40], titulo="Estrategia 2025-2028, capítulo II, 2 y 4 (RD 633/2025) · diagnóstico oficial, no es texto legal"),
  fichab("Desajustes del mercado de trabajo",
         "Datos de Eurostat citados por la Estrategia",
         ["Una de las **menores tasas de vacantes** de Europa, pero dificultades para cubrir ciertos puestos", "Retos: transformación **digital**, transición **ecológica**, **envejecimiento** y falta de **relevo generacional**"],
         "Vacantes (4.º trimestre de 2024): España 0,9 %; UE-27 2,3 %; eurozona 2,5 %",
         f"Los «tres grandes retos» que nombra la Estrategia (cap. II): {c(RD, DIAG, 'la transformación digital, la transición ecológica y energética y el reto demográfico')}."))}

{unidad("2.3 Meta a 2028: tasa de paro del 8,5 % (cap. III.3)",
  lit(RD, OBJ, ["para situarse en el 8,5 % a su finalización", "la intermediación debería alcanzar el 42 % en jóvenes"], solo=[56, 57, 61], titulo="Estrategia 2025-2028, capítulo III, 3. Metas a 2028 (RD 633/2025) · texto oficial, no es texto legal"),
  fichab("Objetivo cuantitativo de la Estrategia",
         "El Sistema Nacional de Empleo, mediante los objetivos y medidas de la Estrategia",
         ["Seguir reduciendo la tasa de paro hasta el **8,5 %** al final de la Estrategia", "Intermediación necesaria: **42 %** jóvenes, **36 %** de 30 a 45 años, **23 %** mayores de 45"],
         "Horizonte: **2028**",
         "La situación es desigual: hay provincias con paro cercano o inferior al **5 %** y otras por encima del **15 %**."))}

{resumen([
  "Desde **2015** baja la tasa de paro (salvo **2020**); menores de 25: **46,24 % → 24,90 %** (2015-2024), aún la más alta por edades.",
  "La **brecha de género** en el paro sube hasta 2020 (**4,16**) y baja a **2,30** puntos en 2024.",
  "Tras la reforma laboral de 2021, **más indefinidos y menos temporales**; persisten la temporalidad en el **sector público** y en los **jóvenes** y el **paro de larga duración**.",
  "Meta de la Estrategia: tasa de paro del **8,5 %** en **2028**."],
  "Siguiente: II. ¿Qué es la política de empleo y quién la gestiona?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Qué es la política de empleo y quién la gestiona? Los servicios públicos de empleo (CE; Ley 3/2023)", donde(
  "Segunda pregunta. La Constitución manda una política orientada al **pleno empleo** y protección frente al **desempleo**; la Ley 3/2023 la organiza en el **Sistema Nacional de Empleo**, formado por la **Agencia Española de Empleo** y los **servicios públicos de empleo autonómicos**.",
  ["1 Fundamento constitucional y concepto de política de empleo (CE; Ley 3/2023, arts. 1 y 2)", "2 Reparto de competencias (Ley 3/2023, arts. 6 y 7)", "3 El Sistema Nacional de Empleo y sus órganos de gobernanza (arts. 8 a 10)", "4 La Agencia Española de Empleo y el SEPE (arts. 18 a 22; disposiciones adicional primera y transitoria segunda; LGSS, art. 294)", "5 Los servicios públicos de empleo de las Comunidades Autónomas (arts. 23 y 24)"]))

T.ap("s3", "II.1 Fundamento constitucional y concepto de política de empleo (CE, arts. 35, 40, 41 y 149.1.7.ª; Ley 3/2023, arts. 1 y 2)", f"""
{unidad("1.1 Derecho al trabajo, pleno empleo y protección del desempleo (CE, arts. 35.1, 40.1 y 41)",
  lit("CE", "Artículo 35", ["el derecho al trabajo"], solo=[1]),
  lit("CE", "Artículo 40", ["De manera especial realizarán una política orientada al pleno empleo"], solo=[1]),
  lit("CE", "Artículo 41", ["especialmente en caso de desempleo"]),
  ficha("Todos los españoles (art. 35.1); todos los ciudadanos (art. 41)",
        ["Deber de trabajar y **derecho al trabajo** (35.1)", "Mandato de **política orientada al pleno empleo** (40.1)", "**Régimen público de Seguridad Social** con prestaciones suficientes, **especialmente en caso de desempleo** (41)"],
        "—",
        "—",
        "El **pleno empleo** está en el art. **40.1**; el **desempleo** se nombra expresamente en el art. **41**. La Ley 3/2023 cita los arts. 35 y 40 para las políticas activas y el 41 para la protección (→ II.1.3)."))}

{unidad("1.2 Competencia del Estado: legislación laboral (CE, art. 149.1.7.ª)",
  lit("CE", "Artículo 149", ["Legislación laboral; sin perjuicio de su ejecución por los órganos de las Comunidades Autónomas"], solo=[1, 8], titulo="Artículo 149.1.7.ª"),
  fichab("Reparto constitucional en materia laboral",
         "**Estado**: legislación; **Comunidades Autónomas**: ejecución",
         "A las CC. AA. corresponde, entre otras cosas, la ejecución de la legislación laboral (Ley 3/2023, art. 7.2 → II.2.2)",
         "—",
         "Legislación laboral **exclusiva del Estado**, con **ejecución** autonómica. La gestión de las **prestaciones por desempleo** es estatal (→ II.2.1)."))}

{unidad("1.3 Objeto de la Ley 3/2023 y definición de la política de empleo (arts. 1 y 2)",
  lit(L3, "Artículo 1", ["Sistema Nacional de Empleo"], solo=[1]),
  lit(L3, "Artículo 2", ["las políticas activas de empleo y las políticas de protección frente al desempleo", "artículos 35 y 40 de la Constitución", "conjunto de prestaciones y subsidios", "artículo 41 de la Constitución"], solo=[1, 2, 4]),
  fichab("La política de empleo y sus dos componentes",
         "Administraciones públicas con competencias, con participación de los **interlocutores sociales**",
         ["**Políticas activas**: decisiones, medidas, servicios y programas para la empleabilidad, la reducción del desempleo y el pleno empleo (arts. 35 y 40 CE)", "**Protección frente al desempleo**: prestaciones y subsidios (art. 41 CE)"],
         "—",
         "Integran la política de empleo **las dos**: activas **y** de protección frente al desempleo. Las activas se enmarcan en la **estrategia coordinada para el empleo de la Unión Europea**."))}
""", 2)

T.ap("s4", "II.2 Reparto de competencias (Ley 3/2023, arts. 6 y 7)", f"""
{unidad("2.1 Planificación estatal (art. 6)",
  lit(L3, "Artículo 6", ["corresponde al Gobierno, a través del Ministerio de Trabajo y Economía Social", "la gestión y control de las prestaciones por desempleo"]),
  fichab("Competencias de la Administración General del Estado",
         "El **Gobierno**, a través del **Ministerio de Trabajo y Economía Social**",
         ["**Planificación** de la política de empleo, en el marco de los acuerdos de la Conferencia Sectorial (6.2)", "Proyectos de ley y reglamentos sobre intermediación, fomento del empleo, protección por desempleo y formación en el trabajo (6.2)", "**Gestión y control de las prestaciones por desempleo** (6.2, último párrafo)"],
         "—",
         "La gestión de las **prestaciones por desempleo** es **estatal** «en cualquier caso», no autonómica."))}

{unidad("2.2 Dimensión autonómica y local (art. 7)",
  lit(L3, "Artículo 7", ["corresponde a las Comunidades Autónomas", "Corresponde a las Corporaciones Locales"], solo=[2, 3, 5]),
  fichab("Competencias de las Comunidades Autónomas y de las Corporaciones Locales",
         ["**Comunidades Autónomas**: desarrollo de la política de empleo, fomento del empleo y ejecución de la legislación laboral y de los programas transferidos", "**Corporaciones Locales**: colaboración y cooperación con las demás Administraciones"],
         "Las entidades locales actúan mediante el principio de **cooperación** y **convenios**",
         "—",
         "A las **Corporaciones Locales** les corresponde **colaborar y cooperar**, no ejecutar la legislación laboral."))}
""", 2)

T.ap("s5", "II.3 El Sistema Nacional de Empleo y sus órganos de gobernanza (arts. 8 a 10)", f"""
{unidad("3.1 Composición y funciones del Sistema Nacional de Empleo (art. 8)",
  lit(L3, "Artículo 8", ["Está conformado por la Agencia Española de Empleo y por los servicios públicos de empleo de las Comunidades Autónomas", "tendrán la consideración de servicios públicos de empleo", "La Conferencia Sectorial de Empleo y Asuntos Laborales", "El Consejo General del Sistema Nacional de Empleo"], solo=[1, 3, 4, 5, 6, 7, 8, 9, 14]),
  fichab("Conjunto de estructuras, recursos, estrategias, planes, programas e información para las políticas de empleo",
         ["Lo forman la **Agencia Española de Empleo** y los **servicios públicos de empleo autonómicos**", "Colaboran las Corporaciones Locales y otras entidades públicas o privadas"],
         ["Órganos de gobernanza: **Conferencia Sectorial de Empleo y Asuntos Laborales** y **Consejo General del Sistema Nacional de Empleo** (8.3)", "Funciones (8.4), entre otras: concretar la Estrategia a través del **Plan Anual** y mantener una **Cartera Común de Servicios**"],
         "—",
         "La prestación de servicios de empleo es **servicio público** con independencia de quién la realice (8.2). Solo **dos** órganos de gobernanza."))}

{unidad("3.2 Conferencia Sectorial de Empleo y Asuntos Laborales (art. 9)",
  lit(L3, "Artículo 9", ["es el órgano de colaboración entre la Administración General del Estado y las Comunidades Autónomas", "presidida por la persona titular del Ministerio de Trabajo y Economía Social", "con voz, pero sin voto", "Acordar los criterios de distribución de los créditos presupuestarios destinados a Comunidades Autónomas", "Identificar los colectivos prioritarios"], solo=[1, 2, 4, 8, 10]),
  fichab("Órgano de **colaboración** entre la AGE y las Comunidades Autónomas",
         ["Preside: el **Ministro/a de Trabajo y Economía Social**", "Miembros: los de los Consejos de Gobierno de las CC. AA. y de **Ceuta y Melilla** con competencias en empleo", "Con voz pero **sin voto**: otras Administraciones y la asociación más representativa de las entidades locales"],
         ["Acuerdos de coordinación; informe de los instrumentos de planificación", "**Distribución de créditos** a las CC. AA.", "**Colectivos prioritarios** de ámbito estatal", "Informe Conjunto sobre el empleo (con el Consejo General)"],
         "—",
         "Preside el **Ministro**, no el director de la Agencia (ese preside el **Consejo General**, → II.3.3). Las entidades locales: **voz sin voto**."))}

{unidad("3.3 Consejo General del Sistema Nacional de Empleo (art. 10)",
  lit(L3, "Artículo 10", ["es el órgano consultivo y de participación institucional en materia de Empleo", "presidido por la persona titular de la Dirección de la Agencia Española de Empleo", "manteniendo así el carácter tripartito del Consejo"], solo=[1, 2, 3, 4]),
  fichab("Órgano **consultivo** y de **participación institucional**, **tripartito**",
         ["Preside: el **titular de la Dirección de la Agencia Española de Empleo**", "Un representante de cada **Comunidad Autónoma** e igual número de la **AGE**, de las organizaciones **empresariales** y de las **sindicales** más representativas"],
         ["Informa las propuestas normativas y los instrumentos de planificación", "Analiza la eficacia de la política de empleo; colabora en el Informe Conjunto", "Funciones en formación en el trabajo (Comisión Estatal de Formación en el trabajo)"],
         "Voto **ponderado**: empresarios y sindicatos pesan, cada uno, lo mismo que el conjunto de las dos Administraciones",
         "**Conferencia Sectorial** = colaboración AGE-CC. AA. (preside el Ministro). **Consejo General** = consultivo y **tripartito** (preside el director de la Agencia)."))}
""", 2)

T.ap("s6", "II.4 La Agencia Española de Empleo y el SEPE (Ley 3/2023, arts. 18 a 22, disposiciones adicional primera y transitoria segunda; LGSS, art. 294)", f"""
{unidad("4.1 Creación, concepto y naturaleza (arts. 18 a 20)",
  lit(L3, "Artículo 18", ["Se autoriza la creación de la Agencia Española de Empleo"]),
  lit(L3, "Artículo 19", ["entidad de derecho público de la Administración General del Estado"]),
  lit(L3, "Artículo 20", ["sección IV del capítulo III del título II de la Ley 40/2015", "a través de la Secretaría de Estado de Empleo y Economía Social", "El control externo corresponderá al Tribunal de Cuentas"], solo=[1, 2, 4]),
  fichab("Organismo público estatal que sustituirá al Servicio Público de Empleo Estatal",
         "Adscrita al **Ministerio de Trabajo y Economía Social**, a través de la **Secretaría de Estado de Empleo y Economía Social**",
         ["La ley **autoriza** su creación; un **Real Decreto** regula la transformación del SEPE en la Agencia (18.2)", "Ordena, desarrolla y sigue las políticas **activas** y de **protección por desempleo** (19)", "Agencia estatal (sección IV del cap. III del título II de la Ley 40/2015): personalidad jurídica, patrimonio y tesorería propios"],
         "Control de eficacia: Secretaría de Estado; control interno: **IGAE**; control externo: **Tribunal de Cuentas** (20.3)",
         "La ley **autoriza** la creación; la transformación del SEPE se hace por **Real Decreto** (→ II.4.3)."))}

{unidad("4.2 Competencias (art. 22, selección)",
  lit(L3, "Artículo 22", ["Elaborar el proyecto de la Estrategia Española de Apoyo Activo al Empleo", "La gestión y el control de las prestaciones por desempleo", "ostentar la representación del Estado español en la red EURES"], solo=[1, 5, 19, 21]),
  fichab("Qué hace la Agencia (entre otras competencias del art. 22)",
         "La Agencia Española de Empleo",
         ["Elabora el proyecto de la **Estrategia**, del **Plan Anual** y de las Recomendaciones Específicas, con las CC. AA. (d)", "**Gestión y control de las prestaciones por desempleo** (j)", "Representación del Estado en la red **EURES** (k)", "Gestiona el Observatorio de las Ocupaciones y las estadísticas estatales (f y g)"],
         "—",
         "**Elabora el proyecto** de la Estrategia, pero la **aprueba el Gobierno** por real decreto (→ IV.2.1). La Agencia gestiona las **prestaciones**; las CC. AA., las **políticas activas** en su territorio."))}

{unidad("4.3 Transformación del SEPE y régimen transitorio (disposiciones adicional primera y transitoria segunda)",
  lit(L3, "Disposición adicional primera", ["mediante Real Decreto se regularán las condiciones de la transformación del Servicio Público de Empleo Estatal, O.A., en la Agencia Española de Empleo", "por real decreto acordado en Consejo de Ministros"], solo=[1, 2, 5, 7]),
  lit(L3, "Disposición transitoria segunda", ["Hasta la entrada en funcionamiento efectivo de la Agencia Española de Empleo, el actual Servicio Público de Empleo Estatal, O.A., asumirá el ejercicio de las funciones"], solo=[1]),
  fichab("Paso del SEPE a la Agencia Española de Empleo",
         "El Gobierno (Real Decreto de transformación y Estatuto); el director o directora de la Agencia se nombra y separa por **real decreto acordado en Consejo de Ministros**, a propuesta del Ministro/a de Trabajo",
         ["Cesión e integración **global**, en unidad de acto, del activo y el pasivo del SEPE; sucesión **universal**", "Las referencias al **INEM** o al **SEPE** se entienden hechas a la Agencia", "Mientras la Agencia no funcione de forma efectiva, el **SEPE** ejerce sus funciones"],
         "—",
         "Hasta su **funcionamiento efectivo**, quien actúa es el **SEPE** (O.A.). Por eso la LGSS sigue nombrando al SEPE como entidad gestora (→ II.4.4)."))}

{unidad("4.4 Entidad gestora de las prestaciones por desempleo (LGSS, art. 294)",
  lit(SS, "Artículo 294", ["Corresponde al Servicio Público de Empleo Estatal gestionar las funciones y servicios derivados de las prestaciones de protección por desempleo", "pago delegado"]),
  fichab("Gestión de las prestaciones por desempleo",
         ["**Servicio Público de Empleo Estatal** (hoy referido a la Agencia Española de Empleo: → II.4.3)", "Las **empresas** colaboran con el **pago delegado** en los casos reglamentarios"],
         "Declara el **reconocimiento, suspensión, extinción y reanudación** de las prestaciones",
         "—",
         "Las **sanciones** son de los órganos de la **Administración laboral**, no de la entidad gestora."))}
""", 2)

T.ap("s7", "II.5 Los servicios públicos de empleo de las Comunidades Autónomas (Ley 3/2023, arts. 23 y 24)", f"""
{unidad("5.1 Definición y competencias (art. 23)",
  lit(L3, "Artículo 23", ["corresponde la gestión y desarrollo de las políticas activas de empleo", "podrán recurrir"], solo=[1, 2]),
  fichab("Servicios públicos de empleo autonómicos",
         "Los órganos o entidades de cada Comunidad Autónoma",
         ["Gestionan y desarrollan las **políticas activas de empleo**", "Garantizan los servicios de empleo comunes y complementarios", "Pueden recurrir a **Corporaciones Locales** u otras entidades colaboradoras"],
         "—",
         "A los autonómicos les corresponden las **políticas activas**; la gestión de las **prestaciones** es estatal (→ II.2.1 y → II.4.4)."))}

{unidad("5.2 Estructura organizativa (art. 24)",
  lit(L3, "Artículo 24", ["órganos de carácter tripartito y paritario"], solo=[2]),
  fichab("Participación social en los servicios autonómicos",
         "Organizaciones sindicales y empresariales **más representativas**",
         "Órganos **tripartitos y paritarios** en la estructura de cada servicio",
         "—",
         "También la **Agencia** tiene participación **tripartita y paritaria** de los interlocutores sociales en sus órganos (art. 21)."))}

{resumen([
  "CE: derecho al trabajo (**35.1**), política orientada al **pleno empleo** (**40.1**), prestaciones **especialmente en caso de desempleo** (**41**); legislación laboral del **Estado** con ejecución autonómica (**149.1.7.ª**).",
  "Política de empleo = políticas **activas** + **protección frente al desempleo** (Ley 3/2023, art. 2).",
  "Sistema Nacional de Empleo: **Agencia Española de Empleo** + **servicios autonómicos**; gobernanza: **Conferencia Sectorial** (preside el Ministro) y **Consejo General** (tripartito; preside el director de la Agencia).",
  "Prestaciones: **gestión estatal** (SEPE, hasta el funcionamiento efectivo de la Agencia); políticas activas: **Comunidades Autónomas**."],
  "Siguiente: III. ¿Qué prestaciones protegen frente al desempleo?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Qué prestaciones protegen frente al desempleo? (LGSS, título III)", donde(
  "Tercera pregunta: el **régimen de prestaciones**. La protección por desempleo tiene un **nivel contributivo** (la prestación) y un **nivel asistencial** (el subsidio). Ambos exigen inscribirse como demandante y suscribir el **acuerdo de actividad** de la Ley 3/2023.",
  ["1 Objeto, niveles, personas protegidas y acción protectora (arts. 262 a 265)", "2 Requisitos, situación legal de desempleo y solicitud (arts. 266 a 268)", "3 Duración y cuantía de la prestación (arts. 269 y 270)", "4 Suspensión y extinción (arts. 271 y 272)", "5 El subsidio por desempleo (arts. 274 a 280)", "6 Incompatibilidades, obligaciones e impugnación (arts. 282, 299 a 301 y 303; Ley 3/2023, art. 3)"]))

T.ap("s8", "III.1 Objeto, niveles, personas protegidas y acción protectora (LGSS, arts. 262 a 265)", f"""
{unidad("1.1 Objeto: desempleo total y parcial (art. 262)",
  lit(SS, "Artículo 262", ["pudiendo y queriendo trabajar", "entre un mínimo de un 10 y un máximo de un 70 por ciento"], solo=[1, 2, 4]),
  ficha("Quienes, **pudiendo y queriendo trabajar**, pierden su empleo o ven suspendido su contrato o reducida su jornada",
        ["**Desempleo total**: cese en la actividad y privación del salario", "**Desempleo parcial**: reducción temporal de la jornada diaria ordinaria, con análoga reducción del salario"],
        "Parcial: reducción **entre el 10 y el 70 %**; no las reducciones definitivas (262.3)",
        "—",
        "Horquilla del parcial: **10 %–70 %**. La reducción debe ser **temporal**."))}

{unidad("1.2 Niveles de protección (art. 263)",
  lit(SS, "Artículo 263", ["un nivel contributivo y en un nivel asistencial, ambos de carácter público y obligatorio", "complementario del anterior"]),
  ficha("Trabajadores desempleados",
        ["**Contributivo**: prestaciones **sustitutivas de las rentas salariales** dejadas de percibir", "**Asistencial**: **complementario** del anterior, para los supuestos del art. 274"],
        "—",
        "Ambos niveles son **públicos y obligatorios**",
        "Dos niveles, **ambos públicos y obligatorios**. El asistencial es **complementario** del contributivo."))}

{unidad("1.3 Personas protegidas (art. 264.1)",
  lit(SS, "Artículo 264", ["siempre que tengan previsto cotizar por esta contingencia", "Los funcionarios interinos, el personal eventual"], solo=[1, 2, 3, 4, 5, 6, 7]),
  ficha(["::Siempre que tengan previsto **cotizar** por desempleo:", "Trabajadores por cuenta ajena del **Régimen General** y de los regímenes especiales que lo protegen", "Emigrantes retornados y liberados de prisión", "**Funcionarios interinos**, personal eventual y contratado en régimen administrativo", "Miembros de corporaciones locales y cargos sindicales retribuidos con dedicación", "Altos cargos retribuidos que no sean funcionarios"],
        "Protección por desempleo",
        "Altos cargos: no si tienen derecho a compensación por el cese",
        "El Gobierno puede **ampliar** la cobertura a otros colectivos (264.3)",
        "Los **funcionarios interinos** sí están protegidos (letra d)."))}

{unidad("1.4 Acción protectora (art. 265.1)",
  lit(SS, "Artículo 265", ["Prestación por desempleo total o parcial", "Subsidio por desempleo"], solo=[1, 2, 3, 4, 5, 6, 7, 8]),
  ficha("Personas protegidas (art. 264)",
        ["::Contributivo:", "Prestación por desempleo **total o parcial**", "Abono de la **aportación de la empresa** a la Seguridad Social", "**Asistencial:**", "**Subsidio** por desempleo", "Cotización por **jubilación** (supuestos del art. 280)", "Asistencia sanitaria y, en su caso, prestaciones familiares"],
        "—",
        "Además: acciones de formación, orientación, reconversión e inserción (265.2)",
        "Contributivo = **prestación**; asistencial = **subsidio**."))}
""", 2)

T.ap("s9", "III.2 Requisitos, situación legal de desempleo y solicitud (LGSS, arts. 266 a 268)", f"""
{unidad("2.1 Requisitos (art. 266)",
  lit(SS, "Artículo 266", ["Estar afiliadas a la Seguridad Social y en situación de alta o asimilada al alta", "dentro de los seis años anteriores a la situación legal de desempleo", "acuerdo de actividad", "No haber cumplido la edad ordinaria", "Estar inscrito como demandante de empleo"], solo=[1, 2, 3, 5, 6, 7]),
  ficha("Personas comprendidas en el art. 264",
        ["**Afiliación** y **alta** o asimilada", "Periodo mínimo de cotización (art. 269.1) en los **seis años** anteriores", "**Situación legal de desempleo** y disponibilidad acreditada por el **acuerdo de actividad**", "No haber cumplido la **edad ordinaria de jubilación** (salvo excepciones)", "**Inscripción** como demandante de empleo"],
        "—", "—",
        "La carencia se busca en los **seis años** anteriores. La disponibilidad se acredita con el **acuerdo de actividad** (Ley 3/2023, art. 3)."))}

{unidad("2.2 Situación legal de desempleo (art. 267, apartados 1 y 2, selección)",
  lit(SS, "Artículo 267", ["En virtud de despido colectivo", "Por extinción del contrato por causas objetivas", "Por resolución de la relación laboral durante el período de prueba a instancia del empresario", "Durante los períodos de inactividad productiva de los trabajadores fijos-discontinuos", "Cuando cesen voluntariamente en el trabajo"], solo=[1, 2, 3, 4, 5, 7, 8, 9, 11, 13, 14, 16, 17, 20, 21, 22]),
  ficha("Trabajadores en alguno de los supuestos legales",
        ["**Extinción**: despido colectivo, muerte/jubilación/incapacidad del empresario individual, despido, causas objetivas, resolución voluntaria en los casos de los arts. 40, 41.3, 49.1.m) y 50 ET, fin de contrato formativo o temporal, no superación del periodo de prueba a instancia del empresario", "**Suspensión** del contrato (ERTE del art. 47 ET; víctimas de violencia de género o sexual)", "**Reducción temporal de jornada** (art. 47 ET)", "**Fijos-discontinuos**, en la inactividad productiva"],
        ["No hay situación legal si se **cesa voluntariamente** (salvo los supuestos del 1.a) 5.º)", "Ni si no se acredita la disponibilidad mediante el **acuerdo de actividad**"],
        "—",
        "Baja voluntaria = **no** hay situación legal de desempleo, salvo las resoluciones voluntarias de los arts. 40, 41.3, 49.1.m) y 50 del Estatuto de los Trabajadores (267.1.a) 5.º)."))}

{unidad("2.3 Solicitud y nacimiento del derecho (art. 268.1 y 2)",
  lit(SS, "Artículo 268", ["dentro del plazo de los quince días siguientes", "perdiendo tantos días de prestación"], solo=[1, 2, 3]),
  ficha("Quien cumpla los requisitos del art. 266",
        ["Solicitud a la entidad gestora; nace desde la **situación legal de desempleo**", "Requiere **inscripción** como demandante y suscribir el **acuerdo de actividad** en la fecha de solicitud"],
        "La inscripción debe **mantenerse** durante toda la prestación",
        "Fuera de plazo: derecho desde la **solicitud**, perdiendo los días de retraso",
        "Plazo: **quince días** siguientes. Fuera de plazo **no se pierde** el derecho entero: se pierden los **días** de retraso."))}
""", 2)

# Escala del art. 269.1 (cotización → prestación), comprobada contra el BOE
_ESC = [("360", "539", "120"), ("540", "719", "180"), ("720", "899", "240"), ("900", "1.079", "300"), ("1.080", "1.259", "360"), ("1.260", "1.439", "420"),
        ("1.440", "1.619", "480"), ("1.620", "1.799", "540"), ("1.800", "1.979", "600"), ("1.980", "2.159", "660")]
_p269 = parrafos(SS, "Artículo 269")
for de, a, d in _ESC:
    i = _p269.index(f"Desde {de} hasta {a}"); assert _p269[i + 1] == d, (de, a, d)
assert _p269[_p269.index("Desde 2.160") + 1] == "720"
ESCALA = "\n".join(["| Cotización (días, en los 6 años anteriores) | Prestación (días) |", "|---|---|"]
                   + [f"| Desde {de} hasta {a} | {d} |" for de, a, d in _ESC] + ["| Desde 2.160 | 720 |"])
ESCALA = "Escala del art. 269.1 (cifras literales del BOE, en forma de cuadro):\n\n" + ESCALA

T.ap("s10", "III.3 Duración y cuantía de la prestación (LGSS, arts. 269 y 270)", f"""
{unidad("3.1 Duración (art. 269)",
  lit(SS, "Artículo 269", ["en los seis años anteriores a la situación legal de desempleo", "previo informe al Consejo General del Servicio Público de Empleo Estatal"], solo=[1, 28]),
  ESCALA,
  ficha("Beneficiarios de la prestación contributiva",
        "Duración según los días **cotizados** en los **seis años** anteriores",
        ["Mínimo: **360** días cotizados → **120** días de prestación", "Máximo: **2.160** o más → **720** días"],
        "El **Gobierno** puede modificar la escala, previo informe al Consejo General",
        "Cada **180** días cotizados más, **60** días más de prestación. Tope: **720** días (dos años)."))}

{unidad("3.2 Cuantía (art. 270, apartados 1 a 3)",
  lit(SS, "Artículo 270", ["durante los últimos ciento ochenta días", "el 70 por ciento durante los ciento ochenta primeros días y el 60 por ciento a partir del día ciento ochenta y uno", "175 por ciento", "107 por ciento o del 80 por ciento"], solo=[1, 2, 4, 5, 6]),
  ficha("Beneficiarios de la prestación contributiva",
        ["Base reguladora: promedio de la base de cotización por desempleo de los **últimos 180 días** (sin horas extraordinarias)", "**70 %** los primeros **180 días**; **60 %** desde el día **181**"],
        ["Máximo: **175 %** del IPREM (200 % o 225 % con uno o más hijos a cargo)", "Mínimo: **107 %** (con hijos) u **80 %** (sin hijos) del IPREM"],
        "—",
        "**70 → 60 %** y el corte es en el día **180**. Topes sobre el **IPREM**, no sobre el salario mínimo."))}
""", 2)

T.ap("s11", "III.4 Suspensión y extinción (LGSS, arts. 271 y 272)", f"""
{unidad("4.1 Suspensión (art. 271, selección)",
  lit(SS, "Artículo 271", ["de duración inferior a doce meses", "de hasta noventa días naturales como máximo durante cada año natural", "no afectará al período de su percepción"], solo=[1, 2, 6, 8, 9, 10, 16]),
  ficha("Beneficiarios de la prestación",
        ["Se suspende, entre otros casos, por **sanción** leve o grave, **trabajo por cuenta ajena** de **menos de 12 meses**, trabajo por cuenta propia de menos de **60 meses**, traslado al extranjero de menos de 12 meses o estancia de hasta **90 días** al año (comunicados y autorizados)"],
        "La suspensión interrumpe el abono pero **no** reduce el periodo de percepción, salvo la **sanción**",
        "Reanudación: de oficio (sanción) o a solicitud en los **quince días** siguientes",
        "Salida al extranjero de **hasta 30 días** una vez al año: ni estancia ni traslado. Trabajo ajeno **< 12 meses** suspende; **≥ 12 meses** extingue (→ III.4.2)."))}

{unidad("4.2 Extinción (art. 272)",
  lit(SS, "Artículo 272", ["Agotamiento del plazo de duración de la prestación", "de duración igual o superior a doce meses", "Renuncia voluntaria al derecho", "Transcurso del plazo de seis años desde la fecha de baja de la prestación sin haber reanudado el derecho"]),
  ficha("Beneficiarios de la prestación",
        ["Agotamiento", "Sanción (en los términos de la LISOS)", "Trabajo por cuenta ajena **≥ 12 meses** o por cuenta propia **≥ 60 meses**", "Edad ordinaria de jubilación; pasar a pensionista de jubilación o de incapacidad permanente total, absoluta o gran incapacidad (con opción)", "Traslado o estancia en el extranjero (salvo suspensión)", "**Renuncia** voluntaria", "**Seis años** desde la baja sin reanudar"],
        "—", "—",
        "**Doce meses** de trabajo por cuenta ajena separan la suspensión de la extinción; con derecho de **opción** (art. 269.3)."))}
""", 2)

T.ap("s12", "III.5 El subsidio por desempleo (LGSS, arts. 274 a 280)", f"""
{unidad("5.1 Beneficiarios (art. 274)",
  lit(SS, "Artículo 274", ["Haber agotado la prestación por desempleo", "trescientos sesenta días", "siempre que hayan cotizado al menos noventa días", "carecer de rentas propias, o bien, alternativamente, acreditar responsabilidades familiares"], solo=[1, 2, 3, 6, 7, 8]),
  ficha("Desempleados que reúnan los requisitos",
        ["Haber **agotado** la prestación (menores de 45 sin responsabilidades familiares: prestación agotada de **360 días** o más)", "Estar en situación legal de desempleo **sin** el periodo mínimo para la contributiva, con al menos **90 días** cotizados", "Mayores de **52** años (art. 280)"],
        "No tener derecho a la contributiva, no estar en incompatibilidad y **carecer de rentas** o acreditar **responsabilidades familiares**",
        "Exige **inscripción** y **acuerdo de actividad** (274.4)",
        "Cotización insuficiente: basta con **90 días** cotizados."))}

{unidad("5.2 Carencia de rentas y responsabilidades familiares (art. 275, apartados 1 a 3)",
  lit(SS, "Artículo 275", ["no superen el 75 por ciento del salario mínimo interprofesional, excluida la parte proporcional de dos pagas extraordinarias", "dividida entre el número de miembros que la componen", "hijos e hijas menores de veintiséis años"], solo=[1, 2, 3]),
  ficha("Solicitantes del subsidio",
        ["**Carencia de rentas**: rentas propias del mes anterior **≤ 75 % del SMI** (sin pagas extras)", "**Responsabilidades familiares**: rentas de la unidad familiar divididas por sus miembros **≤ 75 % del SMI**"],
        "Unidad familiar: solicitante, cónyuge o pareja de hecho, hijos **menores de 26** (o mayores con discapacidad) y menores acogidos o en guarda",
        "Requisitos que deben darse en la solicitud y en cada **prórroga** o **reanudación**",
        "El umbral es el **75 % del SMI** (no del IPREM), **sin** la parte proporcional de **dos pagas extraordinarias**."))}

{unidad("5.3 Solicitud y duración (arts. 276 y 277.3)",
  lit(SS, "Artículo 276", ["en los quince días hábiles siguientes a la fecha del mismo", "cada vez que se hayan devengado tres meses de su percepción"], solo=[1, 5]),
  lit(SS, "Artículo 277", ["por periodos trimestrales"], solo=[6]),
  ficha("Solicitantes del subsidio",
        ["Nace al día siguiente del hecho causante si se solicita en **15 días hábiles**; fuera de plazo pero en **seis meses**, desde la solicitud", "Se reconoce por **periodos trimestrales** prorrogables"],
        "Más de seis meses desde el hecho causante: **denegación** (salvo trabajo, IT o nacimiento en el último día)",
        "Prórroga: solicitud en los **15 días hábiles** siguientes a cada trimestre",
        "Plazos en días **hábiles** (15). Periodos **trimestrales**. (Las tablas de duración máxima del art. 277.1 y 2 no se reproducen aquí.)"))}

{unidad("5.4 Cuantía (art. 278)",
  lit(SS, "Artículo 278", ["el 95 por ciento durante los ciento ochenta primeros días, el 90 por ciento desde el día ciento ochenta y uno al día trescientos sesenta, y el 80 por ciento a partir del día trescientos sesenta y uno"]),
  ficha("Beneficiarios del subsidio",
        ["**95 %** del IPREM (días 1-180)", "**90 %** (días 181-360)", "**80 %** (desde el día 361)"],
        "—", "—",
        "Escalonado **95 / 90 / 80 %** del **IPREM** mensual; el de **mayores de 52** es siempre el **80 %** (→ III.5.5)."))}

{unidad("5.5 Subsidio para mayores de cincuenta y dos años (art. 280, apartados 1, 2, 4 y 9)",
  lit(SS, "Artículo 280", ["acrediten todos los requisitos, salvo la edad, para acceder a cualquier tipo de pensión contributiva de jubilación", "durante al menos seis años", "igual al 80 por ciento", "La entidad gestora cotizará por la contingencia de jubilación", "125 por cien de la base mínima de cotización"], solo=[1, 6, 9, 23, 25]),
  ficha("Mayores de **52 años**",
        ["Requisitos, salvo la edad, para **cualquier pensión contributiva de jubilación**", "Haber cotizado por desempleo al menos **seis años** en la vida laboral", "**Carencia de rentas propias** (art. 275.1)"],
        "Cuantía: **80 %** del IPREM",
        "La entidad gestora **cotiza por jubilación** sobre el **125 %** de la base mínima del Régimen General",
        "Cotización por **jubilación** (no por todas las contingencias). Exige **carencia de rentas propias**, no responsabilidades familiares."))}
""", 2)

T.ap("s13", "III.6 Incompatibilidades, obligaciones e impugnación (LGSS, arts. 282, 299 a 301 y 303; Ley 3/2023, art. 3)", f"""
{unidad("6.1 Incompatibilidades (art. 282, apartados 1, 2 y 4)",
  lit(SS, "Artículo 282", ["incompatibles con el trabajo por cuenta propia", "excepto cuando éste se realice a tiempo parcial", "compatibles con la percepción de cualquier tipo de rentas mínimas"], solo=[1, 3, 18]),
  ficha("Beneficiarios de prestación o subsidio",
        ["**Incompatibles** con el trabajo por **cuenta propia** y, en general, con prestaciones contributivas de la Seguridad Social", "Prestación **compatible** con trabajo **a tiempo parcial** (deduciendo la parte proporcional)", "**Compatibles** con rentas mínimas y prestaciones no contributivas (salvo la de jubilación)"],
        "El subsidio se compatibiliza con el empleo como **complemento de apoyo al empleo** (282.3)",
        "—",
        "Tiempo **parcial**: compatible con deducción; cuenta **propia**: incompatible (salvo programas de fomento, 282.7)."))}

{unidad("6.2 Obligaciones de los beneficiarios (art. 299.1, selección)",
  lit(SS, "Artículo 299", ["Inscribirse como persona demandante de empleo", "Buscar activamente empleo", "en el plazo de cinco días"], solo=[1, 5, 7, 9, 10]),
  ficha("Trabajadores, solicitantes y beneficiarios",
        ["Inscribirse, mantener la inscripción y cumplir el **acuerdo de actividad**", "**Buscar activamente empleo** y acreditarlo cuando se requiera", "Participar en programas de empleo y formación y **aceptar la colocación adecuada**", "Devolver el justificante de comparecencia a una oferta en **cinco días**"],
        "—",
        "La falta de acreditación de la búsqueda activa = **incumplimiento** del acuerdo de actividad",
        "Justificante de comparecencia: **cinco días**."))}

{unidad("6.3 Acuerdo de actividad y colocación adecuada (LGSS, arts. 300 y 301; Ley 3/2023, art. 3 f y g)",
  lit(SS, "Artículo 300", ["artículo 3 de la Ley 3/2023"]),
  lit(L3, "Artículo 3", ["Acuerdo documentado", "deberá ser indefinida y con un salario, en ningún caso, inferior al salario mínimo interprofesional"], solo=[10, 11, 12, 13], titulo="Artículo 3 f) y g) (Ley 3/2023, de Empleo)"),
  ficha("Demandante de servicios de empleo y servicio público de empleo",
        ["**Acuerdo de actividad**: acuerdo documentado de derechos y obligaciones para incrementar la empleabilidad", "**Colocación adecuada**: la de la profesión demandada o la habitual, o cualquier otra ajustada a las aptitudes físicas y formativas"],
        "La colocación ofrecida debe ser **indefinida** y con salario **no inferior al SMI**",
        "Fuera de la localidad de residencia o temporal: solo como colocación adecuada dentro del **acuerdo de actividad** e itinerario (art. 3 g)",
        "La LGSS **remite** a la Ley 3/2023 para definir el acuerdo de actividad y la colocación adecuada."))}

{unidad("6.4 Impugnación (art. 303)",
  lit(SS, "Artículo 303", ["serán recurribles ante los órganos jurisdiccionales del orden social", "reclamación previa ante la entidad gestora"], solo=[1, 6]),
  ficha("Solicitantes y beneficiarios",
        "Recurso contra el reconocimiento, denegación, suspensión o extinción de las prestaciones",
        "Antes de la demanda: **reclamación previa** ante la entidad gestora",
        "Orden jurisdiccional **social**",
        "Orden **social**, no contencioso-administrativo. Requisito: **reclamación previa**."))}

{resumen([
  "Dos niveles **públicos y obligatorios**: **contributivo** (prestación) y **asistencial** (subsidio) (art. 263).",
  "Requisitos: afiliación y alta, **360 días** cotizados en **6 años**, situación legal de desempleo, **acuerdo de actividad**, no edad de jubilación, **inscripción**; solicitud en **15 días** (arts. 266 y 268).",
  "Duración: **120 a 720 días**; cuantía **70 % / 60 %** de la base reguladora (corte en el día **180**), entre **80/107 %** y **175/200/225 %** del IPREM (arts. 269 y 270).",
  "Subsidio: carencia de rentas (**75 % del SMI**), **95/90/80 %** del IPREM; mayores de **52**: **80 %** y cotización por jubilación (arts. 274 a 280).",
  "Impugnación ante el orden **social**, con **reclamación previa** (art. 303)."],
  "Siguiente: IV. ¿Qué son las políticas activas de empleo y cómo se planifican?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Qué son las políticas activas de empleo y cómo se planifican? (Ley 3/2023; RD 633/2025)", donde(
  "Cuarta pregunta: las **políticas de empleo** en sentido estricto, las **activas**. La Ley 3/2023 las define, fija sus **instrumentos de planificación** (Estrategia, Plan Anual y Sistema Público Integrado de Información), regula la **intermediación** y los **servicios garantizados** a personas y empresas.",
  ["1 Concepto de políticas activas e instrumentos de planificación (arts. 11 y 31)", "2 La Estrategia Española de Apoyo Activo al Empleo (art. 12; RD 633/2025)", "3 El Plan Anual para el Fomento del Empleo Digno (art. 13)", "4 Intermediación y agencias de colocación (arts. 41 a 43)", "5 Coordinación con las prestaciones y colectivos prioritarios (arts. 47 y 50)", "6 Servicios garantizados, compromisos y cartera común (arts. 56, 58 y 61)"]))

T.ap("s14", "IV.1 Concepto de políticas activas e instrumentos de planificación (Ley 3/2023, arts. 11 y 31)", f"""
{unidad("1.1 Instrumentos de planificación y coordinación (art. 11)",
  lit(L3, "Artículo 11", ["Informe Conjunto sobre el empleo", "La Estrategia Española de Apoyo Activo al Empleo", "El Plan Anual para el Fomento del Empleo Digno", "El Sistema Público Integrado de Información de los Servicios de Empleo"], solo=[2, 4, 5, 6, 7]),
  fichab("Cómo se planifica y coordina la política de empleo",
         "Seguimiento y evaluación en la **Conferencia Sectorial** y el **Consejo General** (Informe Conjunto sobre el empleo)",
         ["Tres instrumentos: **Estrategia** (→ IV.2), **Plan Anual** (→ IV.3) y **Sistema Público Integrado de Información de los Servicios de Empleo**"],
         "—",
         "Son **tres** instrumentos. El **Informe Conjunto** es el resultado del seguimiento, no un instrumento del art. 11.4."))}

{unidad("1.2 Concepto de políticas activas de empleo (art. 31)",
  lit(L3, "Artículo 31", ["el conjunto de servicios y programas de orientación, intermediación, empleo, formación en el trabajo y asesoramiento para el autoempleo y el emprendimiento", "serán objetivos prioritarios de las políticas activas"]),
  fichab("Políticas activas de empleo",
         "Agencia Española de Empleo y servicios autonómicos, en sus competencias (art. 32.2)",
         ["Servicios y programas de **orientación, intermediación, empleo, formación en el trabajo y asesoramiento para el autoempleo y el emprendimiento**", "Objetivos prioritarios: elevar la **empleabilidad**, reducir las **brechas de género** y ajustar **oferta y demanda**"],
         "—",
         "Garantía de servicios especializados para los **colectivos prioritarios** (→ IV.5.2)."))}
""", 2)

T.ap("s15", "IV.2 La Estrategia Española de Apoyo Activo al Empleo (Ley 3/2023, art. 12; RD 633/2025)", f"""
{unidad("2.1 Aprobación, contenido, duración y ejes (art. 12)",
  lit(L3, "Artículo 12", ["aprobará mediante real decreto", "se someterá a informe del Consejo General del Sistema Nacional de Empleo y de la Conferencia Sectorial de Empleo y Asuntos Laborales", "El diagnóstico de la situación y tendencias del mercado de trabajo", "La Estrategia tendrá carácter cuatrienal", "Eje 7. Mejora del marco institucional"], solo=[1, 2, 3, 4, 10, 11, 12, 13, 14, 15, 16, 17, 18]),
  fichab("Instrumento plurianual de planificación de las políticas activas",
         ["Aprueba: el **Gobierno**, por **real decreto**, a propuesta del Ministerio de Trabajo", "Elabora la propuesta: con la Agencia, los servicios autonómicos y los interlocutores sociales", "Informan antes: **Consejo General** y **Conferencia Sectorial**"],
         ["Contenido: diagnóstico del mercado de trabajo (→ I.1), plan integral de políticas activas, evaluación, buenas prácticas y modelo financiero", "**Siete ejes**: orientación; formación; oportunidades de empleo; oportunidades para personas con discapacidad; igualdad de oportunidades; emprendimiento; mejora del marco institucional (transversal)"],
         "Carácter **cuatrienal**; evaluación **intermedia a los dos años** y evaluación **ex post**",
         "La Estrategia tiene **7** ejes; el Plan Anual, **6** (→ IV.3.1). El eje 7 (marco institucional) es **transversal**."))}

{unidad("2.2 La Estrategia 2025-2028: objetivos estratégicos (RD 633/2025, cap. III.4)",
  lit(RD, "Artículo único", ["Estrategia Española de Apoyo Activo al Empleo 2025-2028"], titulo="Artículo único (RD 633/2025)"),
  lit(RD, OBJ, ["Objetivo estratégico 1. Promover la plena implementación de los servicios garantizados a las personas."], solo=list(range(97, 111)), titulo="Estrategia 2025-2028, capítulo III, 4. Objetivos estratégicos (RD 633/2025)"),
  fichab("Primer nivel de objetivos de la Estrategia vigente",
         "Gobierno (RD 633/2025, de 15 de julio)",
         ["**Ocho** objetivos estratégicos: dos para personas demandantes (1 y 2), dos para empresas (3 y 4), dos para los servicios públicos de empleo y entidades colaboradoras (5 y 6) y dos transversales (7 igualdad y 8 evaluación)"],
         "Vigencia: **2025-2028**",
         "«Promover el acompañamiento integral a las empresas» o «la plena implementación de los servicios garantizados» son objetivos **estratégicos**, no operativos (pregunta oficial L 37, → Cierre 1)."))}

{unidad("2.3 Objetivos operativos: el ejemplo del objetivo estratégico 5 (RD 633/2025, cap. III.5)",
  lit(RD, OBJ, ["Objetivo operativo 5.2 Promover la digitalización del Sistema Nacional de Empleo y el desarrollo de herramientas digitales de apoyo a la labor de los servicios públicos de empleo."], solo=[111, 112, 191, 192, 198], titulo="Estrategia 2025-2028, capítulo III, 5. Objetivos operativos (fragmento) (RD 633/2025)"),
  fichab("Segundo nivel: los objetivos operativos, que se concretan en medidas",
         "—",
         ["Cada objetivo estratégico se divide en objetivos **operativos** (numerados 1.1, 1.2…) y estos en **medidas** (1.1.1…)", "Objetivo estratégico 5 (capacidades de los SPE): operativos **5.1** (medios y profesionalización) y **5.2** (digitalización)"],
         "—",
         "Se reconoce el objetivo **operativo** por su numeración **con punto** (5.2); los estratégicos van del 1 al 8."))}
""", 2)

T.ap("s16", "IV.3 El Plan Anual para el Fomento del Empleo Digno (Ley 3/2023, art. 13)", f"""
{unidad("3.1 Contenido, elaboración y ejes (art. 13)",
  lit(L3, "Artículo 13", ["concretará, con carácter anual", "se elaborará por el Ministerio de Trabajo y Economía Social", "se aprobará por el Consejo de Ministros", "f) Eje 6. Mejora del marco institucional"], solo=[1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13]),
  fichab("Concreción anual de la Estrategia",
         ["Elabora: el **Ministerio de Trabajo y Economía Social**, con las previsiones de las CC. AA. y de la Agencia", "Informan: **Consejo General** y **Conferencia Sectorial**", "Aprueba: el **Consejo de Ministros**"],
         ["Directrices anuales, indicadores y servicios y programas de las CC. AA. y de la Agencia", "**Seis ejes**: orientación; formación; oportunidades de empleo; igualdad de oportunidades en el acceso al empleo; emprendimiento; mejora del marco institucional"],
         "**Anual**; la Agencia puede modificar excepcionalmente servicios y programas a petición justificada de una Comunidad Autónoma",
         "Plan Anual: **seis** ejes (pregunta oficial X 45, → Cierre 1). En el Plan la discapacidad va dentro del eje 4 (igualdad de oportunidades); en la Estrategia tiene eje propio."))}
""", 2)

T.ap("s17", "IV.4 Intermediación y agencias de colocación (Ley 3/2023, arts. 41 a 43)", f"""
{unidad("4.1 Agentes de la intermediación (art. 41.1)",
  lit(L3, "Artículo 41", ["se realizará únicamente a través de", "Los servicios públicos de empleo", "Las agencias de colocación"], solo=[1, 2, 3, 4]),
  fichab("Quién puede intermediar en el mercado de trabajo",
         ["Los **servicios públicos de empleo**", "Las **agencias de colocación** (incluidas las de recolocación y selección)", "Los servicios que se determinen para trabajadores en el exterior"],
         "Las entidades promotoras de programas de políticas activas pueden intermediar de forma complementaria sin ser agencia (41.2)",
         "—",
         "La intermediación se hace «**únicamente**» a través de estos agentes."))}

{unidad("4.2 Servicio público y gratuidad (art. 42, apartados 1, 4 y 6)",
  lit(L3, "Artículo 42", ["tiene la consideración de servicio de carácter público, con independencia del agente que la realice", "Se garantizará, en todo caso, a las personas trabajadoras la gratuidad", "al menos un 60 por ciento de su actividad con fondos propios"], solo=[1, 7, 9]),
  fichab("Régimen de la intermediación",
         "Servicios públicos de empleo y agencias de colocación",
         ["Servicio de carácter **público** sea quien sea el agente", "**Gratuidad** para las personas trabajadoras"],
         "Agencias **con ánimo de lucro**: al menos el **60 %** de su actividad con **fondos propios**",
         "**60 %** con fondos propios, solo para las agencias **con ánimo de lucro**."))}

{unidad("4.3 Agencias de colocación (art. 43, apartados 1, 2 y 4)",
  lit(L3, "Artículo 43", ["con o sin ánimo de lucro", "declaración responsable", "en todo el territorio del Estado y sin límite de duración", "durante los dos años siguientes a la fecha de baja"], solo=[1, 2, 3, 4, 13]),
  fichab("Agencias de colocación",
         "Entidades **públicas o privadas**, **con o sin** ánimo de lucro",
         "**Declaración responsable** ante el servicio público de empleo de la Comunidad donde tengan su **establecimiento principal**",
         ["Validez en **todo el Estado** y **sin límite de duración**; actividad desde el día de la declaración", "Baja por falsear la declaración o incumplir obligaciones: **dos años** sin poder volver a serlo"],
         "No hay autorización: basta **declaración responsable**, con validez **estatal** e **indefinida**."))}
""", 2)

T.ap("s18", "IV.5 Coordinación con las prestaciones y colectivos prioritarios (Ley 3/2023, arts. 47 y 50)", f"""
{unidad("5.1 Perceptores de prestaciones y subsidios (art. 47.1)",
  lit(L3, "Artículo 47", ["deberán adquirir la condición de personas demandantes de servicios de empleo"], solo=[1]),
  fichab("Enlace entre políticas activas y protección por desempleo",
         "Quienes soliciten o perciban prestaciones o subsidios de desempleo o prestaciones por cese de actividad",
         "Adquieren la condición de **demandantes de servicios de empleo**: titulares de los **servicios garantizados** y del **acuerdo de actividad**",
         "—",
         "Es la pieza que une los bloques III y IV: sin **inscripción** ni **acuerdo de actividad** no hay prestación (→ III.2.1)."))}

{unidad("5.2 Colectivos de atención prioritaria (art. 50.1)",
  lit(L3, "Artículo 50", ["personas en desempleo de larga duración", "personas mayores de cuarenta y cinco años", "igual o superior al 33 por ciento", "igual o superior al 65 por ciento"], solo=[1, 2, 3]),
  fichab("Colectivos vulnerables de atención prioritaria",
         "El **Gobierno** y las **Comunidades Autónomas** adoptan programas específicos; las CC. AA. pueden identificar colectivos propios (50.3)",
         ["Entre otros: jóvenes (especialmente con baja cualificación), parados de **larga duración**, personas con discapacidad, **mayores de 45 años**, migrantes, víctimas de violencia de género, de trata o de terrorismo, personas LGTBI, personas gitanas…", "Discapacidad con mayores dificultades: parálisis cerebral, salud mental, discapacidad intelectual o autismo con grado **≥ 33 %**; física o sensorial con grado **≥ 65 %**"],
         "Itinerarios individuales y personalizados; objetivos cuantitativos y cualitativos con perspectiva de género",
         "Mayores de **45** (no de 52 ni de 55). Persona joven: menor de **30** años o beneficiaria de la Garantía Juvenil (art. 3 e)."))}
""", 2)

T.ap("s19", "IV.6 Servicios garantizados, compromisos y cartera común (Ley 3/2023, arts. 56, 58 y 61)", f"""
{unidad("6.1 Servicios garantizados a las personas demandantes (art. 56.1, selección)",
  lit(L3, "Artículo 56", ["Elaboración de un perfil individualizado de usuario", "Tutorización individual", "Un itinerario o plan personalizado adecuado a su perfil que exigirá la formalización de un acuerdo de actividad", "en el plazo máximo de un mes, a contar desde la elaboración de su perfil de usuario", "Un expediente laboral personalizado único"], solo=[1, 2, 5, 8, 15, 17, 18, 19, 20, 22, 25, 26]),
  ficha("Personas demandantes de servicios de empleo",
        ["Perfil individualizado (a)", "Tutorización individual (b)", "Itinerario o plan personalizado con **acuerdo de actividad** (c)", "Formación en el trabajo (d)", "Asesoramiento para el autoempleo (e)", "Intermediación eficiente (f)", "Canal presencial o digital (g)", "Acceso a trabajos en todo el Estado (h)", "Búsqueda de protección social (i)", "**Expediente laboral personalizado único** (j)"],
        "Se implementan a través de la **Cartera Común de Servicios** del Sistema Nacional de Empleo (56.2; → IV.6.3)",
        "Itinerario: en el plazo máximo de **un mes** desde el perfil",
        "**Un mes** desde la elaboración del **perfil** para disponer del **itinerario**."))}

{unidad("6.2 Compromisos de las personas demandantes (art. 58, selección)",
  lit(L3, "Artículo 58", ["Aceptar ofertas de empleo adecuadas"], solo=[1, 2, 3, 7]),
  fichab("Contrapartida de los servicios garantizados",
         "Personas demandantes de servicios de empleo",
         ["Colaborar en el perfil y el itinerario", "Desarrollar, **salvo causa justificada**, las actividades del itinerario", "Aceptar **ofertas de empleo adecuadas** (los desempleados)", "Si perciben prestaciones: buscar activamente empleo y aceptar la colocación adecuada"],
         "—",
         "Los compromisos se cumplen «**salvo causa justificada**»; la colocación adecuada se define en el art. 3 (→ III.6.3)."))}

{unidad("6.3 Cartera Común de Servicios del Sistema Nacional de Empleo (art. 61.1 y 2)",
  lit(L3, "Artículo 61", ["Servicios de orientación para el empleo personalizada, integral e inclusiva", "Servicios de intermediación, colocación y asesoramiento a empresas", "Servicios de formación en el trabajo", "Servicios de asesoramiento para el autoempleo"], solo=[1, 2, 3, 4, 5, 6, 7]),
  fichab("Servicios que deben prestarse en todo el Estado",
         "Todos los servicios públicos de empleo, directamente o mediante entidades colaboradoras",
         ["**Cuatro** grupos: orientación; intermediación, colocación y asesoramiento a empresas; formación en el trabajo; asesoramiento para el autoempleo y el emprendimiento", "Cada servicio público puede aprobar su **cartera propia**, que incluye siempre la común y puede añadir servicios complementarios"],
         "Se regula **reglamentariamente**",
         "Cartera **común** (todo el Estado) + carteras **propias** (complementarias)."))}

{resumen([
  "Políticas activas: orientación, intermediación, empleo, formación en el trabajo y asesoramiento para el autoempleo (art. 31).",
  "Tres instrumentos de planificación: **Estrategia**, **Plan Anual** y **Sistema Público Integrado de Información** (art. 11).",
  "Estrategia: **real decreto**, **cuatrienal**, **7 ejes** (art. 12); la vigente es la **2025-2028** (RD 633/2025), con **8 objetivos estratégicos**. Plan Anual: lo aprueba el **Consejo de Ministros**, **6 ejes** (art. 13).",
  "Intermediación solo por servicios públicos y **agencias de colocación** (declaración responsable; gratuita para el trabajador).",
  "Servicios garantizados con **acuerdo de actividad**; itinerario en **un mes** desde el perfil; cartera común de **cuatro** grupos de servicios."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX = [
 ("X", 45, "Ejes del Plan Anual (→ IV.3.1)", {
   "a": "Ninguno de los dos instrumentos tiene diez ejes: la Estrategia tiene siete (art. 12.4) y el Plan Anual, seis (art. 13.3).",
   "b": "Ocho no es el número de ejes de ninguno de los dos instrumentos (ocho son los **objetivos estratégicos** de la Estrategia 2025-2028, no ejes).",
   "c": f"El art. 13.3 enumera los ejes de la a) a la f) y el último es {c(L3, 'Artículo 13', 'f) Eje 6. Mejora del marco institucional')}: **seis**.",
   "d": f"Cinco se queda corto: el quinto es {c(L3, 'Artículo 13', 'e) Eje 5. Emprendimiento')} y aún falta el eje 6, de mejora del marco institucional."},
   [("Seis", L3, "Artículo 13", "f) Eje 6. Mejora del marco institucional")]),
 ("L", 37, "Objetivos de la Estrategia 2025-2028 (→ IV.2.3)", {
   "a": f"Es el {c(RD, OBJ, 'Objetivo operativo 5.2 Promover la digitalización del Sistema Nacional de Empleo y el desarrollo de herramientas digitales de apoyo a la labor de los servicios públicos de empleo')}.",
   "b": f"Es un objetivo **estratégico**, no operativo: {c(RD, OBJ, 'Objetivo estratégico 6. Promover la participación de las entidades colaboradoras de los servicios públicos de empleo')}.",
   "c": f"Es un objetivo **estratégico**: {c(RD, OBJ, 'Objetivo estratégico 4. Promover el acompañamiento integral a las empresas')}.",
   "d": f"Es un objetivo **estratégico**: {c(RD, OBJ, 'Objetivo estratégico 1. Promover la plena implementación de los servicios garantizados a las personas')}."},
   [("digitalización del Sistema Nacional de Empleo", RD, OBJ, "Objetivo operativo 5.2 Promover la digitalización del Sistema Nacional de Empleo")]),
]
bloques = []
for cod, n, tit, por, ap_ in EX:
    bloques += [f"### {('GACE-L' if cod == 'L' else 'GACE-P' if cod == 'P' else 'GACE-L extraordinario')} 2025, pregunta {n} · {tit}", examen(cod, n, por, ap_)]
T.ap("s20", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join(
  ["En los primeros ejercicios de **2025** cayeron **dos** preguntas de este tema: la **L 37** (Estrategia 2025-2028) y la **X 45** (ejes del Plan Anual). Son literales. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto del BOE."]
  + bloques + ["### Cómo se pregunta", "!> Las dos preguntas juegan con la **estructura** de los instrumentos de planificación: cuántos **ejes** (Estrategia 7, Plan Anual 6) y qué es objetivo **estratégico** u **operativo**. Aprende los números y los niveles."]))

T.ap("s21", "Cierre 2. Repaso en 10 minutos (por bloques)", """
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Evolución del empleo | Paro en descenso desde 2015 (salvo 2020); más indefinidos tras la reforma de 2021 | Menores de 25: **46,24 % → 24,90 %**; meta 2028: **8,5 %** |
| II. Servicios públicos de empleo | Sistema Nacional de Empleo: Agencia Española de Empleo (SEPE hasta su funcionamiento efectivo) + servicios autonómicos | Conferencia Sectorial (preside el **Ministro**); Consejo General (**tripartito**, preside el **director de la Agencia**) |
| III. Prestaciones | Contributivo y asistencial; requisitos; duración y cuantía; subsidio | **360** días → **120**; tope **720**; **70/60 %**; subsidio **75 % SMI**, **95/90/80 %** IPREM |
| IV. Políticas activas | Estrategia, Plan Anual, Sistema Público Integrado de Información; intermediación; servicios garantizados | Estrategia **7 ejes**, Plan Anual **6 ejes**; agencias por **declaración responsable** |

?> **Trampas frecuentes:** «la Estrategia la aprueba el Consejo de Ministros por acuerdo» (por **real decreto** del Gobierno; el que aprueba el Consejo de Ministros es el **Plan Anual**); «el Plan Anual tiene siete ejes» (tiene **seis**; siete la Estrategia); «la Conferencia Sectorial es tripartita» (es el **Consejo General**); «las CC. AA. gestionan las prestaciones por desempleo» (gestión **estatal**); «la prestación es el 70 % durante un año» (el 70 % son los **180 primeros días**); «el subsidio exige rentas inferiores al 75 % del IPREM» (es del **SMI**); «las agencias de colocación necesitan autorización» (basta **declaración responsable**).
""")

# =============================================================================
Q = [
 (L3, "Artículo 2", "Política de empleo", "Según el artículo 2.1 de la Ley 3/2023, de Empleo, integran la política de empleo:",
  ["Las políticas activas de empleo y las políticas de protección frente al desempleo.", "Únicamente las políticas activas de empleo.", "Las políticas activas de empleo y las políticas de Seguridad Social.", "Las políticas de protección frente al desempleo y las de formación profesional del sistema educativo."], "Art. 2.1 Ley 3/2023.", "Integran la política de empleo las políticas activas de empleo y las políticas de protección frente al desempleo"),
 (L3, "Artículo 2", "Política de empleo", "Según el artículo 2.3 de la Ley 3/2023, las políticas de protección frente al desempleo se configuran de conformidad con lo previsto en el artículo de la Constitución:",
  ["41.", "35.", "40.", "149.1.7.ª"], "Art. 2.3 Ley 3/2023: «de conformidad con lo previsto por el artículo 41 de la Constitución». Las activas, con los arts. 35 y 40.", "de conformidad con lo previsto por el artículo 41 de la Constitución"),
 ("CE", "Artículo 40", "Política de empleo", "Según el artículo 40.1 de la Constitución, los poderes públicos realizarán de manera especial una política orientada:",
  ["Al pleno empleo.", "A la estabilidad en el empleo.", "A la protección por desempleo.", "Al empleo público."], "Art. 40.1 CE.", "De manera especial realizarán una política orientada al pleno empleo"),
 (L3, "Artículo 6", "Política de empleo", "Según el artículo 6.2 de la Ley 3/2023, la gestión y control de las prestaciones por desempleo corresponde:",
  ["Al Gobierno, a través del Ministerio de Trabajo y Economía Social.", "A los servicios públicos de empleo de las Comunidades Autónomas.", "A la Tesorería General de la Seguridad Social.", "A las Corporaciones Locales."], "Art. 6.2, último párrafo, Ley 3/2023.", "corresponde al Gobierno, a través del Ministerio de Trabajo y Economía Social, la gestión y control de las prestaciones por desempleo"),
 (L3, "Artículo 8", "Servicios públicos de empleo", "Según el artículo 8.1 de la Ley 3/2023, el Sistema Nacional de Empleo está conformado por:",
  ["La Agencia Española de Empleo y los servicios públicos de empleo de las Comunidades Autónomas.", "La Agencia Española de Empleo y las agencias de colocación.", "El Ministerio de Trabajo y Economía Social y las Corporaciones Locales.", "Los servicios públicos de empleo de las Comunidades Autónomas y las entidades colaboradoras."], "Art. 8.1 Ley 3/2023.", "Está conformado por la Agencia Española de Empleo y por los servicios públicos de empleo de las Comunidades Autónomas"),
 (L3, "Artículo 8", "Servicios públicos de empleo", "Según el artículo 8.3 de la Ley 3/2023, son órganos de gobernanza del Sistema Nacional de Empleo:",
  ["La Conferencia Sectorial de Empleo y Asuntos Laborales y el Consejo General del Sistema Nacional de Empleo.", "El Consejo Rector y la Comisión Permanente de la Agencia Española de Empleo.", "La Conferencia Sectorial de Empleo y Asuntos Laborales y la Oficina de Análisis del Empleo.", "El Consejo General del Sistema Nacional de Empleo y el Observatorio de las Ocupaciones."], "Art. 8.3 Ley 3/2023.", "La Conferencia Sectorial de Empleo y Asuntos Laborales"),
 (L3, "Artículo 9", "Servicios públicos de empleo", "Según el artículo 9.1 de la Ley 3/2023, la Conferencia Sectorial de Empleo y Asuntos Laborales estará presidida por:",
  ["La persona titular del Ministerio de Trabajo y Economía Social.", "La persona titular de la Dirección de la Agencia Española de Empleo.", "La persona titular de la Secretaría de Estado de Empleo y Economía Social.", "Rotatoriamente, por las Comunidades Autónomas."], "Art. 9.1 Ley 3/2023.", "Estará presidida por la persona titular del Ministerio de Trabajo y Economía Social"),
 (L3, "Artículo 10", "Servicios públicos de empleo", "Según el artículo 10.1 de la Ley 3/2023, el Consejo General del Sistema Nacional de Empleo es:",
  ["El órgano consultivo y de participación institucional en materia de Empleo, de carácter tripartito.", "El órgano de colaboración entre la Administración General del Estado y las Comunidades Autónomas.", "El órgano de dirección de la Agencia Española de Empleo.", "Un órgano consultivo integrado solo por representantes de las Administraciones públicas."], "Art. 10.1 Ley 3/2023.", "es el órgano consultivo y de participación institucional en materia de Empleo"),
 (L3, "Artículo 10", "Servicios públicos de empleo", "Según el artículo 10.1 de la Ley 3/2023, el Consejo General del Sistema Nacional de Empleo estará presidido por:",
  ["La persona titular de la Dirección de la Agencia Española de Empleo.", "La persona titular del Ministerio de Trabajo y Economía Social.", "Un representante de las organizaciones sindicales más representativas.", "La persona titular de la Presidencia del Gobierno."], "Art. 10.1 Ley 3/2023.", "presidido por la persona titular de la Dirección de la Agencia Española de Empleo"),
 (L3, "Artículo 20", "Servicios públicos de empleo", "Según el artículo 20.1 de la Ley 3/2023, la Agencia Española de Empleo estará adscrita al Ministerio de Trabajo y Economía Social a través de:",
  ["La Secretaría de Estado de Empleo y Economía Social.", "La Subsecretaría de Trabajo y Economía Social.", "La Dirección General del Servicio Público de Empleo Estatal.", "La Conferencia Sectorial de Empleo y Asuntos Laborales."], "Art. 20.1 Ley 3/2023.", "a través de la Secretaría de Estado de Empleo y Economía Social"),
 (L3, "Disposición transitoria segunda", "Servicios públicos de empleo", "Según la disposición transitoria segunda de la Ley 3/2023, hasta la entrada en funcionamiento efectivo de la Agencia Española de Empleo, sus funciones las asumirá:",
  ["El Servicio Público de Empleo Estatal, O.A.", "El Ministerio de Trabajo y Economía Social directamente.", "La Conferencia Sectorial de Empleo y Asuntos Laborales.", "Los servicios públicos de empleo de las Comunidades Autónomas."], "DT 2.ª Ley 3/2023.", "el actual Servicio Público de Empleo Estatal, O.A., asumirá el ejercicio de las funciones"),
 (L3, "Disposición adicional primera", "Servicios públicos de empleo", "Según la disposición adicional primera de la Ley 3/2023, la persona titular de la dirección de la Agencia Española de Empleo será nombrada y separada de su cargo:",
  ["Por real decreto acordado en Consejo de Ministros, a propuesta de la persona titular del Ministerio de Trabajo y Economía Social.", "Por orden de la persona titular del Ministerio de Trabajo y Economía Social.", "Por acuerdo de la Conferencia Sectorial de Empleo y Asuntos Laborales.", "Por el Consejo General del Sistema Nacional de Empleo, por mayoría absoluta."], "DA 1.ª.7 Ley 3/2023.", "será nombrada y separada de su cargo por real decreto acordado en Consejo de Ministros, a propuesta de la persona titular del Ministerio de Trabajo y Economía Social"),
 (L3, "Artículo 23", "Servicios públicos de empleo", "Según el artículo 23.1 de la Ley 3/2023, a los servicios públicos de empleo de las Comunidades Autónomas corresponde, en sus respectivos ámbitos:",
  ["La gestión y desarrollo de las políticas activas de empleo.", "La gestión y control de las prestaciones por desempleo.", "La aprobación de la Estrategia Española de Apoyo Activo al Empleo.", "La representación del Estado en la red EURES."], "Art. 23.1 Ley 3/2023; las prestaciones, la Estrategia y EURES son estatales (arts. 6.2, 12.1 y 22 k).", "corresponde la gestión y desarrollo de las políticas activas de empleo"),
 (SS, "Artículo 263", "Prestaciones", "Según el artículo 263.1 de la LGSS, la protección por desempleo se estructura en:",
  ["Un nivel contributivo y un nivel asistencial, ambos de carácter público y obligatorio.", "Un nivel contributivo, público y obligatorio, y un nivel complementario, libre.", "Un nivel asistencial público y un nivel contributivo voluntario.", "Tres niveles: contributivo, asistencial y complementario."], "Art. 263.1 LGSS.", "un nivel contributivo y en un nivel asistencial, ambos de carácter público y obligatorio"),
 (SS, "Artículo 262", "Prestaciones", "Según el artículo 262.3 de la LGSS, el desempleo será parcial cuando el trabajador vea reducida temporalmente su jornada diaria ordinaria de trabajo:",
  ["Entre un mínimo de un 10 y un máximo de un 70 por ciento.", "Entre un mínimo de un 20 y un máximo de un 80 por ciento.", "Entre un mínimo de un 10 y un máximo de un 50 por ciento.", "En cualquier porcentaje, siempre que sea definitiva."], "Art. 262.3 LGSS.", "entre un mínimo de un 10 y un máximo de un 70 por ciento"),
 (SS, "Artículo 264", "Prestaciones", "Según el artículo 264.1 de la LGSS, ¿cuál de los siguientes colectivos está comprendido en la protección por desempleo, siempre que tenga previsto cotizar por esta contingencia?",
  ["Los funcionarios interinos.", "Los funcionarios de carrera.", "Los trabajadores por cuenta propia sin asalariados.", "Los pensionistas de jubilación."], "Art. 264.1 d) LGSS.", "Los funcionarios interinos, el personal eventual"),
 (SS, "Artículo 266", "Prestaciones", "Según el artículo 266 b) de la LGSS, el período mínimo de cotización para tener derecho a la prestación debe estar cubierto dentro de:",
  ["Los seis años anteriores a la situación legal de desempleo o al momento en que cesó la obligación de cotizar.", "Los cuatro años anteriores a la situación legal de desempleo.", "Los dos años anteriores a la solicitud.", "Toda la vida laboral del trabajador."], "Art. 266 b) LGSS.", "dentro de los seis años anteriores a la situación legal de desempleo o al momento en que cesó la obligación de cotizar"),
 (SS, "Artículo 267", "Prestaciones", "Según el artículo 267.2 a) de la LGSS, no se considerará en situación legal de desempleo a los trabajadores que:",
  ["Cesen voluntariamente en el trabajo, salvo en los supuestos de resolución voluntaria previstos en el apartado 1.a) 5.º.", "Sean despedidos por causas objetivas.", "Vean extinguido su contrato temporal por expiración del tiempo convenido.", "Vean extinguida su relación durante el periodo de prueba a instancia del empresario."], "Art. 267.2 a) LGSS; las demás son situaciones legales del 267.1 a).", "Cuando cesen voluntariamente en el trabajo, salvo lo previsto en el apartado 1.a) 5.º"),
 (SS, "Artículo 268", "Prestaciones", "Según el artículo 268.1 de la LGSS, el derecho a las prestaciones nacerá a partir de que se produzca la situación legal de desempleo, siempre que se solicite dentro del plazo de:",
  ["Los quince días siguientes.", "El mes siguiente.", "Los diez días hábiles siguientes.", "Los tres meses siguientes."], "Art. 268.1 LGSS.", "siempre que se solicite dentro del plazo de los quince días siguientes"),
 (SS, "Artículo 268", "Prestaciones", "Según el artículo 268.2 de la LGSS, quien presente la solicitud de la prestación por desempleo transcurrido el plazo de quince días:",
  ["Tendrá derecho a la prestación desde la fecha de la solicitud, perdiendo tantos días de prestación como medien desde la fecha en que habría nacido el derecho.", "Perderá el derecho a la prestación.", "Tendrá derecho a la prestación desde la situación legal de desempleo, sin pérdida alguna.", "Solo podrá acceder al subsidio por desempleo."], "Art. 268.2 LGSS.", "perdiendo tantos días de prestación como medien"),
 (SS, "Artículo 269", "Prestaciones", "Según la escala del artículo 269.1 de la LGSS, con un periodo de cotización desde 360 hasta 539 días, corresponde un periodo de prestación de:",
  ["120 días.", "180 días.", "90 días.", "360 días."], "Art. 269.1 LGSS (escala).", ["Desde 360 hasta 539", "120"]),
 (SS, "Artículo 269", "Prestaciones", "Según la escala del artículo 269.1 de la LGSS, la duración máxima de la prestación por desempleo, con 2.160 o más días cotizados, es de:",
  ["720 días.", "660 días.", "900 días.", "1.080 días."], "Art. 269.1 LGSS: «Desde 2.160» → 720.", ["Desde 2.160", "720"]),
 (SS, "Artículo 270", "Prestaciones", "Según el artículo 270.2 de la LGSS, la cuantía de la prestación por desempleo se determina aplicando a la base reguladora:",
  ["El 70 por ciento durante los ciento ochenta primeros días y el 60 por ciento a partir del día ciento ochenta y uno.", "El 80 por ciento durante los ciento ochenta primeros días y el 70 por ciento a partir del día ciento ochenta y uno.", "El 70 por ciento durante el primer año y el 50 por ciento a partir de entonces.", "El 60 por ciento durante toda la duración de la prestación."], "Art. 270.2 LGSS.", "el 70 por ciento durante los ciento ochenta primeros días y el 60 por ciento a partir del día ciento ochenta y uno"),
 (SS, "Artículo 270", "Prestaciones", "Según el artículo 270.1 de la LGSS, la base reguladora de la prestación por desempleo será el promedio de la base por la que se haya cotizado por dicha contingencia durante:",
  ["Los últimos ciento ochenta días del período del artículo 269.1.", "Los últimos trescientos sesenta días cotizados.", "Los últimos doce meses del período del artículo 269.1.", "Los últimos noventa días cotizados."], "Art. 270.1 LGSS.", "durante los últimos ciento ochenta días del período"),
 (SS, "Artículo 270", "Prestaciones", "Según el artículo 270.3 de la LGSS, la cuantía máxima de la prestación por desempleo, cuando el trabajador no tenga hijos a su cargo, será del:",
  ["175 por ciento del indicador público de rentas de efectos múltiples.", "175 por ciento del salario mínimo interprofesional.", "200 por ciento del indicador público de rentas de efectos múltiples.", "225 por ciento del indicador público de rentas de efectos múltiples."], "Art. 270.3 LGSS: 175 % del IPREM; 200 % o 225 % con uno o más hijos a cargo.", "La cuantía máxima de la prestación por desempleo será del 175 por ciento del indicador público de rentas de efectos múltiples"),
 (SS, "Artículo 271", "Prestaciones", "Según el artículo 271.1 d) de la LGSS, el derecho a la prestación por desempleo se suspende mientras el titular realice un trabajo por cuenta ajena de duración:",
  ["Inferior a doce meses.", "Inferior a seis meses.", "Igual o superior a doce meses.", "Inferior a veinticuatro meses."], "Art. 271.1 d) LGSS; igual o superior a doce meses, se extingue (art. 272 c).", "de duración inferior a doce meses"),
 (SS, "Artículo 272", "Prestaciones", "Según el artículo 272 h) de la LGSS, el derecho a la prestación por desempleo se extingue por el transcurso, sin haberlo reanudado, del plazo de:",
  ["Seis años desde la fecha de baja de la prestación.", "Cuatro años desde la fecha de baja de la prestación.", "Un año desde la fecha de baja de la prestación.", "Seis meses desde la fecha de baja de la prestación."], "Art. 272 h) LGSS.", "Transcurso del plazo de seis años desde la fecha de baja de la prestación sin haber reanudado el derecho"),
 (SS, "Artículo 274", "Prestaciones", "Según el artículo 274.1 b) de la LGSS, puede acceder al subsidio quien se encuentre en situación legal de desempleo sin tener cubierto el periodo mínimo de cotización para la prestación contributiva, siempre que haya cotizado al menos:",
  ["Noventa días.", "Ciento ochenta días.", "Trescientos sesenta días.", "Treinta días."], "Art. 274.1 b) LGSS.", "siempre que hayan cotizado al menos noventa días"),
 (SS, "Artículo 275", "Prestaciones", "Según el artículo 275.1 de la LGSS, se entiende cumplido el requisito de carencia de rentas propias cuando las rentas del mes natural anterior no superen:",
  ["El 75 por ciento del salario mínimo interprofesional, excluida la parte proporcional de dos pagas extraordinarias.", "El 75 por ciento del indicador público de rentas de efectos múltiples.", "El 100 por ciento del salario mínimo interprofesional, incluidas las pagas extraordinarias.", "El 80 por ciento del salario mínimo interprofesional."], "Art. 275.1 LGSS.", "no superen el 75 por ciento del salario mínimo interprofesional, excluida la parte proporcional de dos pagas extraordinarias"),
 (SS, "Artículo 278", "Prestaciones", "Según el artículo 278 de la LGSS, durante los ciento ochenta primeros días la cuantía del subsidio por desempleo será igual al:",
  ["95 por ciento del indicador público de rentas de efectos múltiples mensual.", "80 por ciento del indicador público de rentas de efectos múltiples mensual.", "70 por ciento de la base reguladora.", "75 por ciento del salario mínimo interprofesional."], "Art. 278 LGSS: 95 %, 90 % y 80 % del IPREM.", "el 95 por ciento durante los ciento ochenta primeros días"),
 (SS, "Artículo 280", "Prestaciones", "Según el artículo 280.9 de la LGSS, durante la percepción del subsidio para mayores de cincuenta y dos años, la entidad gestora cotizará por la contingencia de:",
  ["Jubilación.", "Incapacidad temporal.", "Todas las contingencias.", "Desempleo."], "Art. 280.9 LGSS.", "La entidad gestora cotizará por la contingencia de jubilación"),
 (SS, "Artículo 303", "Prestaciones", "Según el artículo 303.1 de la LGSS, las decisiones de la entidad gestora sobre reconocimiento, denegación, suspensión o extinción de las prestaciones por desempleo son recurribles ante:",
  ["Los órganos jurisdiccionales del orden social.", "Los órganos jurisdiccionales del orden contencioso-administrativo.", "El Ministerio de Trabajo y Economía Social, en alzada.", "La Conferencia Sectorial de Empleo y Asuntos Laborales."], "Art. 303.1 LGSS; con reclamación previa (303.3).", "serán recurribles ante los órganos jurisdiccionales del orden social"),
 (L3, "Artículo 11", "Políticas activas", "Según el artículo 11.4 de la Ley 3/2023, ¿cuál de los siguientes NO es un instrumento de planificación y coordinación de la política de empleo?",
  ["El Informe Conjunto sobre el empleo.", "La Estrategia Española de Apoyo Activo al Empleo.", "El Plan Anual para el Fomento del Empleo Digno.", "El Sistema Público Integrado de Información de los Servicios de Empleo."], "Art. 11.4 Ley 3/2023: Estrategia, Plan Anual y Sistema Público Integrado de Información. El Informe Conjunto recoge el seguimiento (11.2).", "El Plan Anual para el Fomento del Empleo Digno"),
 (L3, "Artículo 12", "Políticas activas", "Según el artículo 12.1 de la Ley 3/2023, la Estrategia Española de Apoyo Activo al Empleo se aprueba:",
  ["Por el Gobierno, mediante real decreto, a propuesta del Ministerio de Trabajo y Economía Social.", "Por el Consejo de Ministros, mediante acuerdo.", "Por la Conferencia Sectorial de Empleo y Asuntos Laborales.", "Por las Cortes Generales, mediante ley."], "Art. 12.1 Ley 3/2023 (el Plan Anual es el que aprueba el Consejo de Ministros, art. 13.2).", "El Gobierno, a propuesta del Ministerio de Trabajo y Economía Social, aprobará mediante real decreto la Estrategia Española de Apoyo Activo al Empleo"),
 (L3, "Artículo 12", "Políticas activas", "Según el artículo 12.3 de la Ley 3/2023, la Estrategia Española de Apoyo Activo al Empleo tendrá carácter:",
  ["Cuatrienal.", "Anual.", "Bienal.", "Quinquenal."], "Art. 12.3 Ley 3/2023; con evaluación intermedia a los dos años.", "La Estrategia tendrá carácter cuatrienal"),
 (L3, "Artículo 12", "Políticas activas", "Según el artículo 12.4 de la Ley 3/2023, ¿qué eje de la Estrategia Española de Apoyo Activo al Empleo tiene carácter transversal, por lo que afecta a todos los restantes?",
  ["Mejora del marco institucional.", "Orientación.", "Emprendimiento.", "Igualdad de oportunidades en el acceso al empleo."], "Art. 12.4 g) Ley 3/2023 (eje 7).", "Eje 7. Mejora del marco institucional. Este Eje tiene carácter transversal"),
 (L3, "Artículo 13", "Políticas activas", "Según el artículo 13.2 de la Ley 3/2023, el Plan Anual para el Fomento del Empleo Digno se aprobará por:",
  ["El Consejo de Ministros.", "Real decreto del Gobierno, previo dictamen del Consejo de Estado.", "La Conferencia Sectorial de Empleo y Asuntos Laborales.", "La persona titular de la Dirección de la Agencia Española de Empleo."], "Art. 13.2 Ley 3/2023.", "se aprobará por el Consejo de Ministros"),
 (L3, "Artículo 41", "Políticas activas", "Según el artículo 41.1 de la Ley 3/2023, a efectos del Sistema Nacional de Empleo, la intermediación en el mercado de trabajo se realizará únicamente a través de:",
  ["Los servicios públicos de empleo, las agencias de colocación y los servicios que reglamentariamente se determinen para o con las personas trabajadoras en el exterior.", "Los servicios públicos de empleo, exclusivamente.", "Las empresas de trabajo temporal y los servicios públicos de empleo.", "Cualquier persona física o jurídica, sin requisito alguno."], "Art. 41.1 Ley 3/2023.", "se realizará únicamente a través de"),
 (L3, "Artículo 42", "Políticas activas", "Según el artículo 42.6 de la Ley 3/2023, las agencias de colocación que actúen con ánimo de lucro deberán, al margen de la actividad concertada públicamente, desarrollar con fondos propios al menos:",
  ["Un 60 por ciento de su actividad.", "Un 40 por ciento de su actividad.", "Un 50 por ciento de su actividad.", "Un 75 por ciento de su actividad."], "Art. 42.6 Ley 3/2023.", "desarrollar al menos un 60 por ciento de su actividad con fondos propios"),
 (L3, "Artículo 43", "Políticas activas", "Según el artículo 43.2 de la Ley 3/2023, quienes deseen actuar como agencias de colocación deberán:",
  ["Presentar declaración responsable ante el servicio público de empleo competente de la Comunidad o ciudad autónoma en la que tengan su establecimiento principal.", "Obtener autorización previa de la Agencia Española de Empleo, con validez de cinco años.", "Inscribirse en el Registro Mercantil y obtener autorización del Ministerio de Trabajo.", "Obtener autorización de cada Comunidad Autónoma en la que vayan a actuar."], "Art. 43.2 Ley 3/2023; validez en todo el Estado y sin límite de duración.", "deberán presentar declaración responsable ante el servicio público de empleo competente de la Comunidad o ciudad autónoma en la que tengan su establecimiento principal"),
 (L3, "Artículo 50", "Políticas activas", "Según el artículo 50.1 de la Ley 3/2023, se consideran colectivos vulnerables de atención prioritaria, entre otros, las personas mayores de:",
  ["Cuarenta y cinco años.", "Cincuenta y dos años.", "Cincuenta y cinco años.", "Sesenta años."], "Art. 50.1 Ley 3/2023.", "personas mayores de cuarenta y cinco años"),
 (L3, "Artículo 56", "Políticas activas", "Según el artículo 56.1 c) de la Ley 3/2023, las personas demandantes de los servicios de empleo tienen derecho a disponer de su itinerario o plan de actuación individualizado en el plazo máximo de:",
  ["Un mes, a contar desde la elaboración de su perfil de usuario.", "Quince días, a contar desde su inscripción.", "Tres meses, a contar desde la elaboración de su perfil de usuario.", "Seis meses, a contar desde su inscripción."], "Art. 56.1 c) Ley 3/2023.", "en el plazo máximo de un mes, a contar desde la elaboración de su perfil de usuario"),
 (L3, "Artículo 3", "Prestaciones", "Según el artículo 3 g) de la Ley 3/2023, con carácter general la colocación adecuada que se ofrezca deberá ser:",
  ["Indefinida y con un salario, en ningún caso, inferior al salario mínimo interprofesional.", "De duración mínima de seis meses y con salario no inferior al IPREM.", "A jornada completa y en la localidad de residencia, con cualquier salario.", "Indefinida y con un salario no inferior al de la última ocupación."], "Art. 3 g) Ley 3/2023.", "La colocación que se ofrezca deberá ser indefinida y con un salario, en ningún caso, inferior al salario mínimo interprofesional"),
 (RD, OBJ, "Evolución del empleo", "Según la Estrategia Española de Apoyo Activo al Empleo 2025-2028 (RD 633/2025), el conjunto de sus objetivos y medidas deberá contribuir a que la tasa de paro se sitúe a su finalización en el:",
  ["8,5 %.", "5 %.", "10 %.", "12,5 %."], "Estrategia 2025-2028, cap. III.3 (Metas a 2028).", "para situarse en el 8,5 % a su finalización"),
 (RD, DIAG, "Evolución del empleo", "Según el diagnóstico de la Estrategia 2025-2028 (RD 633/2025), la tasa de paro de los menores de 25 años pasó del 46,24 % en el cuarto trimestre de 2015 al:",
  ["24,90 % en el mismo trimestre de 2024.", "14,90 % en el mismo trimestre de 2024.", "34,90 % en el mismo trimestre de 2024.", "8,5 % en el mismo trimestre de 2024."], "Estrategia 2025-2028, cap. II.5.", "pasando de una tasa del 46,24 % en el cuarto trimestre del 2015 al 24,90 % en el mismo trimestre de 2024"),
]
for k, art, cat, enun, ops, expl, frag in Q: T.q(k, art, cat, enun, ops, expl, frag)
T.real("L", 37, "Políticas activas"); T.real("X", 45, "Políticas activas")

# Flashcards
for q_, a_, cat in [
  ("¿Qué integra la política de empleo? (Ley 3/2023, art. 2)", "Las políticas activas de empleo y las políticas de protección frente al desempleo.", "Política de empleo"),
  ("¿Qué artículos de la CE fundamentan las políticas activas y la protección por desempleo?", "Activas: arts. 35 y 40; protección frente al desempleo: art. 41 (Ley 3/2023, art. 2).", "Política de empleo"),
  ("Composición del Sistema Nacional de Empleo (art. 8.1)", "La Agencia Española de Empleo y los servicios públicos de empleo de las Comunidades Autónomas.", "Servicios públicos de empleo"),
  ("Órganos de gobernanza del Sistema Nacional de Empleo (art. 8.3)", "La Conferencia Sectorial de Empleo y Asuntos Laborales y el Consejo General del Sistema Nacional de Empleo.", "Servicios públicos de empleo"),
  ("¿Quién preside la Conferencia Sectorial y quién el Consejo General?", "Conferencia Sectorial: la persona titular del Ministerio de Trabajo y Economía Social (art. 9.1). Consejo General: la persona titular de la Dirección de la Agencia Española de Empleo (art. 10.1).", "Servicios públicos de empleo"),
  ("¿Quién ejerce las funciones de la Agencia Española de Empleo hasta su funcionamiento efectivo?", "El Servicio Público de Empleo Estatal, O.A. (disposición transitoria segunda).", "Servicios públicos de empleo"),
  ("Niveles de la protección por desempleo (LGSS, art. 263)", "Contributivo y asistencial, ambos públicos y obligatorios; el asistencial es complementario.", "Prestaciones"),
  ("Requisitos de la prestación contributiva (LGSS, art. 266)", "Afiliación y alta o asimilada; periodo mínimo cotizado en los seis años anteriores; situación legal de desempleo y acuerdo de actividad; no tener la edad ordinaria de jubilación; inscripción como demandante.", "Prestaciones"),
  ("Plazo de solicitud de la prestación (art. 268.1)", "Quince días siguientes a la situación legal de desempleo; fuera de plazo se pierden los días de retraso (268.2).", "Prestaciones"),
  ("Duración mínima y máxima de la prestación (art. 269.1)", "De 360 a 539 días cotizados: 120 días; desde 2.160: 720 días.", "Prestaciones"),
  ("Cuantía de la prestación (art. 270.2)", "70 % de la base reguladora los primeros 180 días; 60 % desde el día 181.", "Prestaciones"),
  ("Topes de la prestación (art. 270.3)", "Máximo 175 % del IPREM (200 % o 225 % con hijos a cargo); mínimo 107 % (con hijos) u 80 % (sin hijos).", "Prestaciones"),
  ("Carencia de rentas para el subsidio (art. 275.1)", "Rentas del mes anterior no superiores al 75 % del SMI, excluida la parte proporcional de dos pagas extraordinarias.", "Prestaciones"),
  ("Cuantía del subsidio (art. 278)", "95 % del IPREM los 180 primeros días, 90 % del día 181 al 360 y 80 % desde el 361.", "Prestaciones"),
  ("Subsidio para mayores de 52 años (art. 280)", "80 % del IPREM; requisitos (salvo edad) para la jubilación contributiva, seis años cotizados por desempleo, carencia de rentas; la entidad gestora cotiza por jubilación.", "Prestaciones"),
  ("¿Ante qué orden jurisdiccional se impugnan las prestaciones por desempleo? (art. 303)", "Ante el orden social, con reclamación previa ante la entidad gestora.", "Prestaciones"),
  ("Instrumentos de planificación de la política de empleo (art. 11.4)", "Estrategia Española de Apoyo Activo al Empleo, Plan Anual para el Fomento del Empleo Digno y Sistema Público Integrado de Información de los Servicios de Empleo.", "Políticas activas"),
  ("Estrategia Española de Apoyo Activo al Empleo (art. 12)", "La aprueba el Gobierno por real decreto; cuatrienal; siete ejes; informan el Consejo General y la Conferencia Sectorial. Vigente: 2025-2028 (RD 633/2025).", "Políticas activas"),
  ("Plan Anual para el Fomento del Empleo Digno (art. 13)", "Lo elabora el Ministerio de Trabajo, lo informan el Consejo General y la Conferencia Sectorial y lo aprueba el Consejo de Ministros; seis ejes.", "Políticas activas"),
  ("Agencias de colocación (art. 43)", "Entidades públicas o privadas, con o sin ánimo de lucro; declaración responsable; validez en todo el Estado y sin límite de duración.", "Políticas activas"),
  ("Grupos de la Cartera Común de Servicios (art. 61.1)", "Orientación; intermediación, colocación y asesoramiento a empresas; formación en el trabajo; asesoramiento para el autoempleo y el emprendimiento.", "Políticas activas"),
  ("Meta de tasa de paro de la Estrategia 2025-2028", "8,5 % al finalizar la Estrategia (cap. III.3).", "Evolución del empleo"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Política de empleo", "Conjunto de las políticas activas de empleo y de las políticas de protección frente al desempleo (Ley 3/2023, art. 2).", "s3", "Política de empleo")
T.glos("Sistema Nacional de Empleo", "Estructuras, recursos, estrategias, planes, programas e información para las políticas de empleo; lo forman la Agencia Española de Empleo y los servicios públicos de empleo autonómicos (Ley 3/2023, art. 8).", "s5", "Servicios públicos de empleo")
T.glos("Conferencia Sectorial de Empleo y Asuntos Laborales", "Órgano de colaboración entre la AGE y las Comunidades Autónomas en política de empleo, presidido por el Ministro/a de Trabajo (Ley 3/2023, art. 9).", "s5", "Servicios públicos de empleo")
T.glos("Consejo General del Sistema Nacional de Empleo", "Órgano consultivo y de participación institucional, tripartito, presidido por el director/a de la Agencia Española de Empleo (Ley 3/2023, art. 10).", "s5", "Servicios públicos de empleo")
T.glos("Agencia Española de Empleo", "Organismo público estatal adscrito al Ministerio de Trabajo a través de la Secretaría de Estado de Empleo y Economía Social, que sucede al SEPE (Ley 3/2023, arts. 18 a 22 y disposición adicional primera).", "s6", "Servicios públicos de empleo")
T.glos("Situación legal de desempleo", "Supuestos de extinción, suspensión o reducción de jornada que dan acceso a la protección por desempleo (LGSS, art. 267).", "s9", "Prestaciones")
T.glos("Acuerdo de actividad", "Acuerdo documentado de derechos y obligaciones entre la persona demandante y el servicio público de empleo para incrementar su empleabilidad (Ley 3/2023, art. 3 f; LGSS, art. 300).", "s13", "Prestaciones")
T.glos("Colocación adecuada", "La de la profesión demandada o habitual, o ajustada a las aptitudes; con carácter general, indefinida y con salario no inferior al SMI (Ley 3/2023, art. 3 g; LGSS, art. 301).", "s13", "Prestaciones")
T.glos("Subsidio por desempleo", "Prestación del nivel asistencial para desempleados que agotaron la prestación o no alcanzan la cotización mínima y carecen de rentas o tienen responsabilidades familiares (LGSS, arts. 274 y 275).", "s12", "Prestaciones")
T.glos("Políticas activas de empleo", "Servicios y programas de orientación, intermediación, empleo, formación en el trabajo y asesoramiento para el autoempleo y el emprendimiento (Ley 3/2023, art. 31).", "s14", "Políticas activas")
T.glos("Estrategia Española de Apoyo Activo al Empleo", "Instrumento cuatrienal de planificación aprobado por real decreto, articulado en siete ejes (Ley 3/2023, art. 12); la vigente, 2025-2028 (RD 633/2025).", "s15", "Políticas activas")
T.glos("Plan Anual para el Fomento del Empleo Digno", "Concreción anual de la Estrategia, aprobada por el Consejo de Ministros, articulada en seis ejes (Ley 3/2023, art. 13).", "s16", "Políticas activas")
T.glos("Agencia de colocación", "Entidad pública o privada, con o sin ánimo de lucro, que intermedia en coordinación o colaboración con los servicios públicos de empleo, previa declaración responsable (Ley 3/2023, art. 43).", "s17", "Políticas activas")
T.glos("Colectivos de atención prioritaria", "Personas con especiales dificultades de acceso y mantenimiento del empleo enumeradas en el art. 50 de la Ley 3/2023 (jóvenes, parados de larga duración, mayores de 45, personas con discapacidad, entre otros).", "s18", "Políticas activas")

# Cronología (fechas de los metadatos del BOE)
T.hito("1978", "Constitución Española (BOE de 29-12-1978)", "Arts. 35, 40 y 41: derecho al trabajo, pleno empleo y protección del desempleo", "normativo", "s3")
T.hito("2015", "Real Decreto Legislativo 8/2015, de 30 de octubre, texto refundido de la Ley General de la Seguridad Social (BOE de 31-10-2015)", "Título III: protección por desempleo", "normativo", "s8")
T.hito("2023", "Ley 3/2023, de 28 de febrero, de Empleo (BOE de 1-3-2023; vigor el 2-3-2023)", "Sistema Nacional de Empleo, Agencia Española de Empleo y servicios garantizados", "normativo", "s5")
T.hito("2024", "Real Decreto-ley 2/2024, de 21 de mayo (BOE de 22-5-2024)", "Reforma del nivel asistencial de la protección por desempleo (subsidio)", "normativo", "s12")
T.hito("2025", "Real Decreto 633/2025, de 15 de julio (BOE de 16-7-2025; vigor el 17-7-2025)", "Estrategia Española de Apoyo Activo al Empleo 2025-2028", "normativo", "s15")

T.publicar()
