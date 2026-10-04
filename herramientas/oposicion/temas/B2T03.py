# -*- coding: utf-8 -*-
"""Tema II.3 (B2T03): La organización de la Unión Europea (II): el Parlamento Europeo.
El Tribunal de Justicia de la Unión Europea. El Tribunal de Cuentas. El Banco Central Europeo.
Método del I.2: mapa → bloques (I a IV) con guía; cada artículo, texto literal + ficha;
cierre 1 (preguntas oficiales) y cierre 2 (repaso).
Normas (EUR-Lex, etiqueta DOUE): TUE (versión consolidada, DO C 202 de 7-6-2016), arts. 14 y 19;
TFUE, arts. 223 a 287; Protocolo n.º 3 sobre el Estatuto del TJUE (ESTJUE, texto de 2016:
solo artículos que no han modificado los Reglamentos 2016/1192, 2019/629 y 2024/2019);
Decisión 2013/336/UE del Consejo (número de abogados generales; bloque DOUE con su URL);
Reglamento (UE, Euratom) 2024/2019 (art. 50 ter del Estatuto; REG2024_2019.json extraído del
HTML de EUR-Lex agrupando cada artículo citado con sus párrafos).
Otras fuentes oficiales (no BOE): Reglamento interno del Parlamento Europeo, arts. 15 y 16
(boe/RIPE.json, copiado literal de europarl.europa.eu, versión de mayo de 2026) y portal del
Parlamento Europeo (dato de actualidad de la pregunta X 33)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *
import boe

CORTO["ESTJUE"] = "Estatuto del TJUE"
CORTO["REG2024_2019"] = "Reglamento (UE, Euratom) 2024/2019"

# Fuentes oficiales que no son del BOE ni de EUR-Lex (etiqueta PE). Textos copiados literales de
# las páginas descargadas (comprobado con un script contra la copia guardada).
URL_RIPE15 = "https://www.europarl.europa.eu/doceo/document/lastrules/RULE-015_ES.html"
URL_RIPE16 = "https://www.europarl.europa.eu/doceo/document/lastrules/RULE-016_ES.html"
URL_PE = "https://www.europarl.europa.eu/portal/es"
boe.IDS.setdefault("RIPE", "PE:Reglamento interno")
boe.IDS.setdefault("PEWEB", "PE:portal")
boe._cache["PEWEB"] = {"portal": ("portal", [("parrafo", "Presidenta Roberta Metsola"),
    ("parrafo", "La Presidenta es elegida por un periodo renovable de dos años y medio, equivalente a la mitad de la legislatura.")])}

PE_BLOQUE = "\n".join([f"> [[PE|{URL_PE}]]", "> **Portal del Parlamento Europeo (consultado en octubre de 2026) · fuente oficial, no es texto legal**",
    "> Presidenta Roberta Metsola", "> La Presidenta es elegida por un periodo renovable de dos años y medio, equivalente a la mitad de la legislatura."])

URL_AG = "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32013D0336"
AG_2013 = "\n".join([f"> [[DOUE|{URL_AG}]]",
    "> **Decisión 2013/336/UE del Consejo, de 25 de junio de 2013, por la que se aumenta el número de abogados generales del Tribunal de Justicia de la Unión Europea (DOUE L 179 de 29.6.2013) · artículo 1 (texto de EUR-Lex)**",
    "> Artículo 1",
    "> Se aumenta el número de abogados generales del Tribunal de Justicia de la Unión Europea a:",
    "> — nueve, con efectos a partir del 1 de julio de 2013;",
    "> — once, con efectos a partir del 7 de octubre de 2015."])

def lit_pe(url, art, resaltar, rubrica):
    return f"> [[PE|{url}]]\n" + lit("RIPE", art, resaltar, titulo=f"{art} del Reglamento interno del Parlamento Europeo. {rubrica} · texto oficial publicado por el Parlamento Europeo (10.ª legislatura, versión de mayo de 2026); norma interna de la Cámara, no publicada en el BOE")

T = Tema("B2T03",
  "Cuatro preguntas: I. Qué es y cómo funciona el Parlamento Europeo (TUE, art. 14; TFUE, arts. 223 a 234) · II. Cómo está organizado y qué juzga el Tribunal de Justicia de la Unión Europea (TUE, art. 19; TFUE, arts. 251 a 281; Estatuto del TJUE) · III. Quién controla las cuentas de la Unión: el Tribunal de Cuentas (TFUE, arts. 285 a 287) · IV. Quién dirige la política monetaria: el Banco Central Europeo (TFUE, arts. 282 a 284). Cada artículo: texto literal de EUR-Lex y ficha.",
  ["Parlamento Europeo", "TUE art. 14", "Moción de censura", "Defensor del Pueblo Europeo", "Derecho de petición", "TJUE", "TUE art. 19", "Abogados generales", "Tribunal General", "Comité del art. 255", "Recurso por incumplimiento", "Recurso de anulación", "Cuestión prejudicial", "Tribunal de Cuentas", "BCE", "Eurosistema"])

# =============================================================================
T.ap("s0", "Mapa del tema: cuatro preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque II, tema 3):
> La organización de la Unión Europea (II): el Parlamento Europeo. El Tribunal de Justicia de la Unión Europea. El Tribunal de Cuentas. El Banco Central Europeo.

### El hilo conductor

El epígrafe nombra **cuatro instituciones** de la Unión. Cada una es un bloque de los apuntes, que se lee como una pregunta:

| Bloque | Pregunta | Tratado de la Unión Europea (TUE) | Tratado de Funcionamiento (TFUE) y otras normas |
|---|---|---|---|
| **I** | ¿Qué es y cómo funciona el Parlamento Europeo? | Art. 14 | Arts. 223 a 234; Reglamento interno del Parlamento Europeo, arts. 15 y 16 |
| **II** | ¿Cómo está organizado y qué juzga el Tribunal de Justicia de la Unión Europea? | Art. 19 | Arts. 251 a 281; Estatuto del TJUE (Protocolo n.º 3); Reglamento (UE, Euratom) 2024/2019; Decisión 2013/336/UE (abogados generales) |
| **III** | ¿Quién controla las cuentas de la Unión? El Tribunal de Cuentas | — | Arts. 285 a 287 |
| **IV** | ¿Quién dirige la política monetaria? El Banco Central Europeo | — | Arts. 282 a 284 |

!> **La idea que une los cuatro bloques:** el Parlamento Europeo **representa a los ciudadanos** y comparte con el Consejo la función legislativa y la presupuestaria (I); el TJUE **garantiza el respeto del Derecho** en la interpretación y aplicación de los Tratados (II); el Tribunal de Cuentas **fiscaliza** los ingresos y gastos de la Unión (III), y el BCE, **independiente**, dirige con los bancos centrales del euro la política monetaria (IV). La lista de instituciones del art. 13 TUE, el Consejo Europeo, el Consejo y la Comisión son del tema II.2; las fuentes del Derecho de la Unión y el valor de la jurisprudencia, del tema II.4.

### Cómo está escrito

- Cada artículo: primero el **texto literal** de los Tratados tal como lo publica EUR-Lex (etiqueta **DOUE**), y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen; para el derecho de petición, ficha de derecho).
- El Reglamento interno del Parlamento Europeo se cita de la web oficial del Parlamento (etiqueta **PE**): es la norma interna de la Cámara y no está en el BOE.
- Los esquemas y cuadros **no son texto legal**: resumen los artículos citados.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué es y cómo funciona el Parlamento Europeo? (TUE, art. 14; TFUE, arts. 223 a 234)", donde(
  "Primera pregunta del tema. El Parlamento Europeo es la institución de **los ciudadanos de la Unión**: sus diputados se eligen por sufragio universal directo. Hay que saber qué funciones tiene, cómo se compone, qué poderes de impulso y control ejerce y cómo decide.",
  ["1 Funciones, composición, elección y Presidente (TUE, art. 14; TFUE, art. 223; Reglamento interno, arts. 15 y 16)", "2 Poderes de impulso y de control: partidos, iniciativa, investigación, peticiones y Defensor del Pueblo (TFUE, arts. 224 a 228)", "3 Funcionamiento y moción de censura (TFUE, arts. 229 a 234)"]))

T.ap("s1", "I.1 Funciones, composición, elección y Presidente (TUE, art. 14; TFUE, art. 223; Reglamento interno, arts. 15 y 16)", f"""
{unidad("1.1 Funciones (TUE, art. 14.1)",
  lit("TUE", "Artículo 14", ["conjuntamente con el Consejo la función legislativa y la función presupuestaria", "funciones de control político y consultivas", "Elegirá al Presidente de la Comisión"], solo=[1]),
  fichab("Las cuatro funciones del Parlamento Europeo",
         c("TUE", "Artículo 14", "El Parlamento Europeo"),
         ["Función **legislativa** y función **presupuestaria**: " + c("TUE", "Artículo 14", "conjuntamente con el Consejo"), "Funciones de **control político** y **consultivas**, en las condiciones de los Tratados", c("TUE", "Artículo 14", "Elegirá al Presidente de la Comisión")],
         "—",
         "Legisla y aprueba el presupuesto **con el Consejo**, no en exclusiva (cayó en 2025, → Cierre 1). **Elige** al Presidente de la Comisión."))}

{unidad("1.2 Composición (TUE, art. 14.2)",
  lit("TUE", "Artículo 14", ["representantes de los ciudadanos de la Unión", "no excederá de setecientos cincuenta, más el Presidente", "decrecientemente proporcional", "mínimo de seis diputados por Estado miembro", "más de noventa y seis escaños", "por unanimidad, a iniciativa del Parlamento Europeo y con su aprobación"], solo=[2, 3]),
  fichab("Cuántos diputados y cómo se reparten",
         f"Diputados: {c('TUE', 'Artículo 14', 'representantes de los ciudadanos de la Unión')}; fija la composición {c('TUE', 'Artículo 14', 'El Consejo Europeo')}",
         ["Representación **decrecientemente proporcional**", "Decisión del Consejo Europeo sobre la composición, a iniciativa del Parlamento y con su aprobación"],
         ["::Cifras del Tratado:", "Máximo: **750 más el Presidente**", "Mínimo por Estado: **6** diputados", "Máximo por Estado: **96** escaños", "Decisión de composición: Consejo Europeo **por unanimidad**"],
         "Representan a los **ciudadanos de la Unión** (no a los Estados). 6 de mínimo y 96 de máximo por Estado; el Presidente va **aparte** del límite de 750."))}

{unidad("1.3 Elección y mandato de los diputados (TUE, art. 14.3; TFUE, art. 223)",
  lit("TUE", "Artículo 14", ["sufragio universal directo, libre y secreto", "mandato de cinco años"], solo=[4]),
  lit("TFUE", "Artículo 223", ["procedimiento uniforme en todos los Estados miembros o de acuerdo con principios comunes", "por unanimidad con arreglo a un procedimiento legislativo especial", "por mayoría de los miembros que lo componen", "con la aprobación del Consejo", "se decidirán en el Consejo por unanimidad"]),
  fichab("Cómo se elige a los diputados y quién fija su estatuto",
         ["::Procedimiento electoral (223.1):", "Proyecto: el **Parlamento Europeo**", "Disposiciones: el **Consejo**, por unanimidad", "Aprobación posterior de los Estados miembros según sus normas constitucionales", "::Estatuto de los diputados (223.2):", "El **Parlamento**, por propia iniciativa, previo dictamen de la Comisión y con aprobación del Consejo"],
         f"Sufragio universal directo, libre y secreto; {c('TFUE', 'Artículo 223', 'procedimiento uniforme en todos los Estados miembros o de acuerdo con principios comunes a todos los Estados miembros')}",
         ["Mandato: **cinco años** (TUE 14.3)", "Procedimiento electoral: Consejo **por unanimidad** + aprobación del Parlamento **por mayoría de los miembros que lo componen** (223.1)", "Régimen fiscal de los diputados: Consejo **por unanimidad** (223.2)"],
         "Mandato de **cinco** años. El proyecto de procedimiento electoral lo elabora el **Parlamento**, pero lo establece el **Consejo** y necesita aprobación de los **Estados**. El estatuto de los diputados lo fija el **Parlamento** con aprobación del Consejo."))}

{unidad("1.4 Presidente y Mesa (TUE, art. 14.4; Reglamento interno, arts. 15 y 16)",
  lit("TUE", "Artículo 14", ["elegirá a su Presidente y a la Mesa de entre sus diputados"], solo=[5]),
  lit_pe(URL_RIPE15, "Artículo 15", ["en votación secreta", "por aclamación", "representación equitativa de las fuerzas políticas, así como por un equilibrio geográfico y de género"], "Candidaturas y disposiciones generales"),
  lit_pe(URL_RIPE16, "Artículo 16", ["Si después de tres votaciones ningún candidato hubiera obtenido la mayoría absoluta de los votos emitidos", "en la cuarta votación las candidaturas de los dos diputados", "el candidato de más edad"], "Elección del presidente - Discurso de apertura"),
  PE_BLOQUE,
  fichab("Elección del Presidente y de la Mesa del Parlamento Europeo",
         f"El propio Parlamento, {c('TUE', 'Artículo 14', 'de entre sus diputados')}",
         ["**Votación secreta** (Reglamento interno, art. 15.1); por **aclamación** si las candidaturas no superan los cargos, salvo que se pida votación secreta", "Representación equitativa de las fuerzas políticas y equilibrio geográfico y de género (art. 15.2)"],
         ["Tres votaciones: **mayoría absoluta de los votos emitidos**", "Cuarta votación: solo los **dos** más votados en la tercera", "Empate: el candidato **de más edad**"],
         "El Presidente lo elige el **Parlamento entre sus diputados** (no el Consejo ni los Estados). Empate en la cuarta votación: gana el **de más edad**."),
  "?> **Dato de actualidad (cayó en 2025, → Cierre 1):** la Presidenta del Parlamento Europeo es **Roberta Metsola** (portal del Parlamento Europeo, comprobado el 4-10-2026). Es un dato que **caduca**: según el mismo portal, la Presidencia dura **dos años y medio**, renovables, así que hay que volver a comprobarlo antes del examen. No confundir con la Presidencia de la **Comisión** (tema II.2).")}
""", 2)

T.ap("s2", "I.2 Poderes de impulso y de control (TFUE, arts. 224 a 228)", f"""
{unidad("2.1 Partidos políticos a escala europea (art. 224)",
  lit("TFUE", "Artículo 224", ["con arreglo al procedimiento legislativo ordinario", "estatuto de los partidos políticos a escala europea", "normas relativas a su financiación"]),
  fichab("Estatuto y financiación de los partidos políticos europeos",
         c("TFUE", "Artículo 224", "El Parlamento Europeo y el Consejo"),
         c("TFUE", "Artículo 224", "mediante reglamentos"),
         "Procedimiento legislativo **ordinario**",
         "Es de los pocos casos del bloque con procedimiento legislativo **ordinario** (Parlamento **y** Consejo)."))}

{unidad("2.2 Iniciativa: pedir propuestas a la Comisión (art. 225)",
  lit("TFUE", "Artículo 225", ["Por decisión de la mayoría de los miembros que lo componen", "solicitar a la Comisión que presente las propuestas oportunas", "comunicará las razones al Parlamento Europeo"]),
  fichab("Derecho del Parlamento a pedir a la Comisión que proponga un acto",
         "El Parlamento Europeo pide; la **Comisión** decide si propone",
         ["Solicitud sobre cualquier asunto que requiera un acto de la Unión para aplicar los Tratados", "Si la Comisión no propone, **comunica las razones**"],
         "Mayoría **de los miembros que lo componen**",
         "Por esta vía el Parlamento **pide** a la Comisión que proponga; si no lo hace, la Comisión debe **comunicar las razones**. Mayoría: de los **miembros que lo componen**."))}

{unidad("2.3 Comisiones temporales de investigación (art. 226)",
  lit("TFUE", "Artículo 226", ["a petición de la cuarta parte de los miembros que lo componen", "comisión temporal de investigación", "alegaciones de infracción o de mala administración", "salvo que de los hechos alegados esté conociendo un órgano jurisdiccional", "terminará con la presentación de su informe"]),
  fichab("Investigación parlamentaria de infracciones o mala administración en la aplicación del Derecho de la Unión",
         c("TFUE", "Artículo 226", "el Parlamento Europeo podrá constituir una comisión temporal de investigación"),
         ["Examina alegaciones de **infracción** o **mala administración**", "No si los hechos están ante un **órgano jurisdiccional**, hasta que concluya", "Modalidades: reglamento del Parlamento con aprobación del Consejo y de la Comisión"],
         ["Petición de **la cuarta parte** de los miembros", "Termina con la **presentación de su informe**"],
         "**Una cuarta parte** de los miembros. Es **temporal**: se extingue con el **informe**. Cede ante el proceso judicial en curso."))}

{unidad("2.4 Derecho de petición (art. 227)",
  lit("TFUE", "Artículo 227", ["Cualquier ciudadano de la Unión", "que resida o tenga su domicilio social en un Estado miembro", "individualmente o asociado con otros ciudadanos o personas", "que le afecte directamente"]),
  ficha(["Cualquier **ciudadano de la Unión**", "Cualquier persona física o jurídica que **resida o tenga su domicilio social** en un Estado miembro"],
        f"Presentar al Parlamento Europeo una petición, {c('TFUE', 'Artículo 227', 'individualmente o asociado con otros ciudadanos o personas')}",
        f"Sobre {c('TFUE', 'Artículo 227', 'un asunto propio de los ámbitos de actuación de la Unión que le afecte directamente')}",
        "—",
        "Se dirige al **Parlamento Europeo** (no a la Comisión ni al Defensor del Pueblo). El asunto tiene que **afectar directamente** al peticionario."))}

{unidad("2.5 El Defensor del Pueblo Europeo (art. 228)",
  lit("TFUE", "Artículo 228", ["elegirá a un Defensor del Pueblo Europeo", "casos de mala administración", "con exclusión del Tribunal de Justicia de la Unión Europea en el ejercicio de sus funciones jurisdiccionales", "plazo de tres meses", "después de cada elección del Parlamento Europeo para toda la legislatura", "Su mandato será renovable", "el Tribunal de Justicia podrá destituir al Defensor del Pueblo", "con total independencia"]),
  fichab("Órgano que recibe reclamaciones por mala administración de las instituciones de la Unión",
         ["Lo **elige** el Parlamento Europeo", "Lo puede **destituir** el **Tribunal de Justicia**, a petición del Parlamento"],
         ["Reclamaciones de ciudadanos de la Unión y de personas que residan o tengan domicilio social en un Estado miembro", "Investiga de oficio o por reclamación (directa o a través de un diputado)", "No si los hechos son o han sido objeto de un procedimiento jurisdiccional", "Informe anual al Parlamento"],
         ["Elegido **después de cada elección** del Parlamento, **para toda la legislatura**; mandato **renovable**", "La institución afectada tiene **tres meses** para exponer su posición"],
         "Excluido el **TJUE** en sus funciones **jurisdiccionales**. Lo elige el **Parlamento** y lo destituye el **Tribunal de Justicia** (en Pleno: Estatuto, art. 16, → II.1.3). Plazo de **tres meses** para la institución."))}
""", 2)

T.ap("s3", "I.3 Funcionamiento y moción de censura (TFUE, arts. 229 a 234)", f"""
{unidad("3.1 Período de sesiones (art. 229)",
  lit("TFUE", "Artículo 229", ["cada año un período de sesiones", "el segundo martes de marzo", "a petición de la mayoría de los miembros que lo componen, del Consejo o de la Comisión"]),
  fichab("Cuándo se reúne el Parlamento Europeo",
         ["Sesión anual: sin convocatoria", "Período parcial extraordinario: a petición de la **mayoría de sus miembros**, del **Consejo** o de la **Comisión**"],
         c("TFUE", "Artículo 229", "Se reunirá sin necesidad de previa convocatoria el segundo martes de marzo"),
         "Un período de sesiones **cada año**; arranca el **segundo martes de marzo**",
         "**Segundo martes de marzo**, sin convocatoria. El extraordinario lo pueden pedir **tres**: la mayoría de los diputados, el Consejo o la Comisión (no el Consejo Europeo)."))}

{unidad("3.2 Relación con la Comisión, el Consejo Europeo y el Consejo (art. 230)",
  lit("TFUE", "Artículo 230", ["podrá asistir a todas las sesiones", "contestará oralmente o por escrito", "en las condiciones fijadas por el reglamento interno del Consejo Europeo y por el del Consejo"]),
  fichab("Presencia de las demás instituciones ante el Parlamento",
         "Comisión; Consejo Europeo y Consejo",
         ["La Comisión puede asistir a todas las sesiones y comparece si el Parlamento lo pide", "La Comisión contesta **oralmente o por escrito** las preguntas del Parlamento o de sus miembros", "Consejo Europeo y Consejo: comparecen según **sus propios reglamentos internos**"],
         "—",
         "Las preguntas parlamentarias obligan a la **Comisión** a contestar; el Consejo Europeo y el Consejo comparecen en las condiciones de **su** reglamento interno."))}

{unidad("3.3 Mayorías, quórum y reglamento interno (arts. 231 y 232)",
  lit("TFUE", "Artículo 231", ["por mayoría de los votos emitidos", "El reglamento interno fijará el quórum"]),
  lit("TFUE", "Artículo 232", ["por mayoría de los miembros que lo componen"]),
  fichab("Cómo decide el Parlamento y quién fija sus normas internas",
         "El Parlamento Europeo",
         "Regla general de votación y aprobación de su propio reglamento interno",
         ["Regla general: **mayoría de los votos emitidos**, salvo disposición en contrario de los Tratados (231)", "Quórum: lo fija el **reglamento interno** (231)", "Reglamento interno: **mayoría de los miembros que lo componen** (232)"],
         "Distinguir **votos emitidos** (regla general) de **miembros que lo componen** (reglamento interno, art. 225, art. 229, procedimiento electoral)."))}

{unidad("3.4 El informe general anual de la Comisión (art. 233)",
  lit("TFUE", "Artículo 233", ["en sesión pública", "informe general anual"]),
  fichab("Debate del informe general anual",
         "La Comisión lo presenta; el Parlamento lo discute",
         c("TFUE", "Artículo 233", "en sesión pública"),
         "Anual",
         "El informe es de la **Comisión** y se discute en sesión **pública**. Cuándo lo publica la Comisión es del art. 249 (tema II.2)."))}

{unidad("3.5 La moción de censura contra la Comisión (art. 234)",
  lit("TFUE", "Artículo 234", ["transcurridos tres días como mínimo desde la fecha de su presentación y en votación pública", "por mayoría de dos tercios de los votos emitidos que representen, a su vez, la mayoría de los diputados que componen el Parlamento Europeo", "deberán dimitir colectivamente", "deberá dimitir del cargo que ejerce en la Comisión", "continuarán despachando los asuntos de administración ordinaria"]),
  fichab("Exigencia de responsabilidad política colectiva de la Comisión",
         "El Parlamento Europeo frente a la **Comisión** (y al Alto Representante en lo que ejerce en ella)",
         ["Votación **pública**", "Si se aprueba: dimisión **colectiva** de los miembros de la Comisión; el Alto Representante dimite del cargo que ejerce **en la Comisión**", "Siguen en funciones (asuntos de administración ordinaria) hasta su sustitución", "Los sustitutos terminan el mandato de los cesados"],
         ["Votación: **tres días como mínimo** desde la presentación", "Aprobación: **dos tercios de los votos emitidos** que sean, a su vez, **mayoría de los diputados**"],
         "Doble mayoría: **2/3 de los votos emitidos** + **mayoría de los diputados**. Esperar **3 días**. Votación **pública** (no secreta). Dimisión **colectiva**."))}

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Decisión del Parlamento Europeo | Mayoría | Artículo |
|---|---|---|
| Regla general | Mayoría de los **votos emitidos** | TFUE 231 |
| Pedir a la Comisión una propuesta | Mayoría de los **miembros que lo componen** | TFUE 225 |
| Constituir una comisión de investigación (petición) | **Cuarta parte** de los miembros | TFUE 226 |
| Pedir período parcial extraordinario | Mayoría de los **miembros que lo componen** (o Consejo, o Comisión) | TFUE 229 |
| Aprobar el procedimiento electoral | Mayoría de los **miembros que lo componen** | TFUE 223.1 |
| Aprobar su reglamento interno | Mayoría de los **miembros que lo componen** | TFUE 232 |
| Moción de censura | **2/3 de los votos emitidos** + **mayoría de los diputados** | TFUE 234 |
| Elegir a su Presidente (tres primeras votaciones) | Mayoría **absoluta de los votos emitidos** | Reglamento interno, art. 16.1 |

{resumen([
  "Funciones (TUE 14.1): **legislativa y presupuestaria con el Consejo**, control político y consultivas; **elige** al Presidente de la Comisión.",
  "Composición (TUE 14.2): máximo **750 + el Presidente**; mínimo **6** y máximo **96** por Estado; **decrecientemente proporcional**.",
  "Diputados: sufragio universal directo, libre y secreto, mandato de **cinco años** (TUE 14.3).",
  "Impulso y control: pedir propuestas a la Comisión (225), comisiones de investigación a petición de **1/4** (226), peticiones (227) y **Defensor del Pueblo** (228).",
  "Sesión anual el **segundo martes de marzo** (229); regla general: **mayoría de los votos emitidos** (231); moción de censura: **2/3 de los emitidos + mayoría de los diputados**, tras **3 días** (234)."],
  "Siguiente: II. ¿Cómo está organizado y qué juzga el Tribunal de Justicia de la Unión Europea?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Cómo está organizado y qué juzga el Tribunal de Justicia de la Unión Europea? (TUE, art. 19; TFUE, arts. 251 a 281)", donde(
  "Segunda pregunta. El TJUE es la institución **jurisdiccional** de la Unión. Primero, **quiénes lo forman** (Tribunal de Justicia, Tribunal General y tribunales especializados); después, **qué recursos** conoce y **con qué límites**.",
  ["1 Estructura y composición (TUE, art. 19; TFUE, arts. 251 a 255; Estatuto)", "2 Tribunal General y tribunales especializados (TFUE, arts. 256 y 257; Estatuto)", "3 Recurso por incumplimiento (arts. 258 a 260)", "4 Control de legalidad: anulación, omisión y excepción de ilegalidad (arts. 263 a 266 y 277)", "5 Cuestión prejudicial (art. 267)", "6 Otras competencias y límites (arts. 261, 262, 268 a 276)", "7 Disposiciones comunes y Estatuto (arts. 278 a 281; Estatuto, art. 20)"]))

T.ap("s4", "II.1 Estructura y composición (TUE, art. 19; TFUE, arts. 251 a 255; Estatuto)", f"""
{unidad("1.1 Qué comprende y para qué sirve (TUE, art. 19.1)",
  lit("TUE", "Artículo 19", ["comprenderá el Tribunal de Justicia, el Tribunal General y los tribunales especializados", "Garantizará el respeto del Derecho en la interpretación y aplicación de los Tratados", "tutela judicial efectiva"], solo=[1, 2]),
  fichab("La institución jurisdiccional de la Unión",
         ["El **Tribunal de Justicia de la Unión Europea** (institución) comprende tres órganos: Tribunal de Justicia, Tribunal General y tribunales especializados", "Los **Estados miembros** establecen las vías de recurso nacionales"],
         c("TUE", "Artículo 19", "Garantizará el respeto del Derecho en la interpretación y aplicación de los Tratados"),
         "—",
         "«TJUE» es la **institución**; «Tribunal de Justicia» es **uno** de sus órganos. La tutela judicial efectiva en el Derecho de la Unión también corresponde a los **Estados** (vías de recurso nacionales)."))}

{unidad("1.2 Composición y nombramiento (TUE, art. 19.2)",
  lit("TUE", "Artículo 19", ["un juez por Estado miembro", "abogados generales", "al menos de un juez por Estado miembro", "de común acuerdo por los Gobiernos de los Estados miembros para un período de seis años", "podrán ser nombrados de nuevo"], solo=[3, 4, 5]),
  fichab("Quién forma el Tribunal de Justicia y el Tribunal General",
         ["Tribunal de Justicia: **un juez por Estado miembro**, asistido por **abogados generales**", "Tribunal General: **al menos un juez por Estado miembro**", "Nombran: los **Gobiernos** de los Estados miembros, **de común acuerdo**"],
         "Entre personalidades con plenas garantías de independencia y que reúnan las condiciones de los arts. 253 y 254 TFUE",
         ["Mandato: **seis años**", "Reelegibles"],
         "Tribunal de Justicia: **uno** por Estado; Tribunal General: **al menos uno** (el Estatuto fija dos, → II.1.6). Los nombran los **Gobiernos** de común acuerdo (no el Consejo ni el Parlamento)."))}

{unidad("1.3 Salas, Gran Sala y Pleno (TFUE, art. 251; Estatuto, arts. 16 y 17)",
  lit("TFUE", "Artículo 251", ["en Salas o en Gran Sala", "también podrá actuar en Pleno"]),
  lit("ESTJUE", "Artículo 16", ["Salas compuestas por tres y cinco Jueces", "La Gran Sala estará compuesta por quince Jueces", "cuando lo solicite un Estado miembro o una institución de la Unión que sea parte en el proceso", "del apartado 2 del artículo 228, del apartado 2 del artículo 245, del artículo 247 o del apartado 6 del artículo 286", "reviste una importancia excepcional"]),
  lit("ESTJUE", "Artículo 17", ["en número impar", "si están presentes tres Jueces", "si están presentes once Jueces", "si están presentes diecisiete Jueces"], solo=[1, 2, 3, 4]),
  fichab("Formaciones del Tribunal de Justicia",
         ["**Salas** de 3 y de 5 jueces", "**Gran Sala**: 15 jueces, presidida por el Presidente del Tribunal", "**Pleno**"],
         ["Gran Sala: cuando lo pida un **Estado miembro** o una **institución** que sea parte", "Pleno obligatorio: asuntos de los arts. 228.2 (destitución del Defensor del Pueblo), 245.2 y 247 (miembros de la Comisión) y 286.6 (miembros del Tribunal de Cuentas)", "Pleno potestativo: asunto de **importancia excepcional**, oído el Abogado General"],
         ["Quórum: número **impar** siempre", "Salas de 3 o 5: **3** jueces presentes", "Gran Sala: **11**", "Pleno: **17**"],
         "Gran Sala **15** jueces, quórum **11**; Pleno, quórum **17**. El Pleno es obligatorio en los asuntos de los arts. **228.2, 245.2, 247 y 286.6** TFUE (Defensor del Pueblo, miembros de la Comisión y del Tribunal de Cuentas)."))}

{unidad("1.4 Los abogados generales (TFUE, art. 252)",
  lit("TFUE", "Artículo 252", ["ocho abogados generales", "el Consejo, por unanimidad, podrá aumentar el número de abogados generales", "conclusiones motivadas"]),
  AG_2013,
  fichab("Miembros del Tribunal de Justicia que presentan conclusiones",
         ["**Ocho** abogados generales según el Tratado", "Puede aumentarlos el **Consejo, por unanimidad**, si lo solicita el Tribunal de Justicia", "Hoy son **once**: Decisión 2013/336/UE del Consejo (nueve desde el 1-7-2013; once desde el **7-10-2015**)"],
         f"{c('TFUE', 'Artículo 252', 'presentar públicamente, con toda imparcialidad e independencia, conclusiones motivadas')} en los asuntos que, según el Estatuto, requieran su intervención",
         "Aumento del número: **unanimidad** del Consejo, a petición del Tribunal",
         "El Tratado dice **ocho**, pero el Consejo los aumentó a **once** (Decisión 2013/336/UE). El abogado general **no juzga**: presenta **conclusiones motivadas**. Si el asunto no plantea cuestiones de derecho nuevas, puede juzgarse **sin conclusiones** (Estatuto, art. 20, → II.7.4)."))}

{unidad("1.5 Jueces y abogados generales del Tribunal de Justicia (TFUE, art. 253; Estatuto, art. 9)",
  lit("TFUE", "Artículo 253", ["absolutas garantías de independencia", "las más altas funciones jurisdiccionales o que sean jurisconsultos de reconocida competencia", "de común acuerdo por los Gobiernos de los Estados miembros por un período de seis años, tras consultar al comité a que se refiere el artículo 255", "Cada tres años tendrá lugar una renovación parcial", "por un período de tres años. Su mandato será renovable", "requerirá la aprobación del Consejo"]),
  lit("ESTJUE", "Artículo 9", ["cada tres años, afectará a la mitad de los Jueces"]),
  fichab("Requisitos, nombramiento y mandato en el Tribunal de Justicia",
         ["Nombran: los **Gobiernos**, de común acuerdo, **tras consultar al comité del art. 255**", "Presidente: lo eligen **los jueces** de entre ellos", "Secretario: lo nombra el Tribunal"],
         ["Independencia absoluta y condiciones para las **más altas funciones jurisdiccionales** de su país, o **jurisconsultos de reconocida competencia**", "Reglamento de Procedimiento: lo establece el Tribunal con **aprobación del Consejo**"],
         ["Mandato: **seis años**, reelegibles", "Renovación parcial **cada tres años** (de la **mitad** de los jueces: Estatuto, art. 9)", "Presidente: **tres años**, renovable"],
         "Seis años de mandato; renovación parcial cada **tres**; Presidente por **tres**, renovable. Antes de nombrar hay que **consultar al comité del art. 255** (→ II.1.7)."))}

{unidad("1.6 El Tribunal General (TFUE, art. 254; Estatuto, art. 48)",
  lit("TFUE", "Artículo 254", ["será fijado por el Estatuto", "podrá disponer que el Tribunal General esté asistido por abogados generales", "la capacidad necesaria para el ejercicio de altas funciones jurisdiccionales", "por un período de seis años", "Cada tres años tendrá lugar una renovación parcial", "de acuerdo con el Tribunal de Justicia"]),
  lit("ESTJUE", "Artículo 48", ["dos Jueces por Estado miembro a partir del 1 de septiembre de 2019"]),
  fichab("Composición y nombramiento del Tribunal General",
         ["Número de jueces: lo fija el **Estatuto** (hoy, **dos por Estado miembro**)", "Nombran: los **Gobiernos**, de común acuerdo, tras consultar al comité del art. 255", "Presidente: lo eligen los jueces"],
         ["Independencia absoluta y capacidad para **altas** funciones jurisdiccionales", "Reglamento de Procedimiento: **de acuerdo con el Tribunal de Justicia** y con aprobación del Consejo", "Salvo disposición del Estatuto, se le aplican las normas de los Tratados sobre el Tribunal de Justicia"],
         ["Mandato: **seis años**, reelegibles", "Renovación parcial **cada tres años**", "Presidente: **tres años**, renovable"],
         "TFUE: el número lo fija el **Estatuto**; Estatuto: **dos jueces por Estado miembro** desde el 1-9-2019. Al Tribunal de Justicia se le piden las «**más altas**» funciones jurisdiccionales; al General, «**altas**»."))}

{unidad("1.7 El comité de idoneidad de candidatos (TFUE, art. 255)",
  lit("TFUE", "Artículo 255", ["antes de que los Gobiernos de los Estados miembros procedan a los nombramientos", "siete personalidades", "uno de los cuales será propuesto por el Parlamento Europeo", "El Consejo adoptará una decisión por la que se establezcan las normas de funcionamiento del comité", "por iniciativa del Presidente del Tribunal de Justicia"]),
  fichab("Comité que se pronuncia sobre la idoneidad de los candidatos a juez y abogado general",
         ["**Siete** personalidades: antiguos miembros del Tribunal de Justicia y del Tribunal General, miembros de órganos jurisdiccionales nacionales superiores y juristas de reconocida competencia", "**Uno** propuesto por el **Parlamento Europeo**", "El **Consejo** adopta sus normas de funcionamiento y designa a sus miembros, por iniciativa del **Presidente del Tribunal de Justicia**"],
         "Informa sobre los candidatos a juez y abogado general del Tribunal de Justicia y del Tribunal General",
         "Interviene **antes** de los nombramientos",
         "**Siete** miembros (no nueve); actúa **antes** de que los Gobiernos nombren; el Tratado **no** exige años de ejercicio profesional. Cayó en 2025 (→ Cierre 1)."))}

{unidad("1.8 Juramento e incompatibilidades de los jueces (Estatuto, arts. 2 y 4)",
  lit("ESTJUE", "Artículo 2", ["antes de entrar en funciones, deberá prestar juramento ante el Tribunal de Justicia, en sesión pública"]),
  lit("ESTJUE", "Artículo 4", ["ninguna función política o administrativa", "salvo autorización concedida con carácter excepcional por el Consejo, por mayoría simple"], solo=[1, 2]),
  fichab("Estatuto personal de los jueces",
         f"Los jueces. Estatuto, art. 8: {c('ESTJUE', 'Artículo 8', 'Las disposiciones de los artículos 2 a 7 serán aplicables a los Abogados Generales')}",
         ["Juramento ante el Tribunal, en sesión **pública**, antes de entrar en funciones", "Prohibida toda función **política o administrativa**", "Prohibida toda actividad profesional, retribuida o no, salvo autorización excepcional"],
         "Autorización excepcional de actividad profesional: **Consejo, por mayoría simple**",
         "La autorización la da el **Consejo** por **mayoría simple**, y solo con carácter **excepcional**; nunca para funciones **políticas o administrativas**."))}
""", 2)

T.ap("s5", "II.2 Tribunal General y tribunales especializados (TFUE, arts. 256 y 257; Estatuto, arts. 50 ter y 56)", f"""
{unidad("2.1 Competencias del Tribunal General (art. 256)",
  lit("TFUE", "Artículo 256", ["en primera instancia de los recursos contemplados en los artículos 263, 265, 268, 270 y 272", "limitado a las cuestiones de Derecho", "contra las resoluciones de los tribunales especializados", "en materias específicas determinadas por el Estatuto", "podrá remitir el asunto ante el Tribunal de Justicia"]),
  fichab("Qué juzga el Tribunal General y qué recurso cabe",
         "El Tribunal General; revisa el Tribunal de Justicia",
         ["**Primera instancia**: recursos de los arts. 263 (anulación), 265 (omisión), 268 (responsabilidad), 270 (personal) y 272 (cláusula compromisoria), salvo los de un tribunal especializado y los que el Estatuto reserve al Tribunal de Justicia", "Recursos contra las resoluciones de los **tribunales especializados**", "**Cuestiones prejudiciales** en materias específicas del Estatuto (→ II.2.2)"],
         ["Contra lo resuelto en primera instancia: **casación** ante el Tribunal de Justicia, solo **cuestiones de Derecho**", "Reexamen excepcional por el Tribunal de Justicia si hay riesgo grave para la **unidad o coherencia** del Derecho de la Unión"],
         "El recurso por **incumplimiento** (258-259) **no** está en la lista del 256.1. La casación se limita a **cuestiones de Derecho**."))}

{unidad("2.2 Cuestiones prejudiciales que conoce el Tribunal General desde 2024 (Estatuto, art. 50 ter)",
  lit("REG2024_2019", "Artículo 50 ter", ["exclusivamente en una o varias de las siguientes materias específicas", "el sistema común del impuesto sobre el valor añadido", "los impuestos especiales", "el código aduanero", "seguirá siendo competente", "se presentará ante el Tribunal de Justicia", "transferirá dicha petición al Tribunal General"], titulo="Artículo 50 ter del Estatuto del TJUE (añadido por el art. 1, punto 4, del Reglamento (UE, Euratom) 2024/2019, de 11 de abril de 2024)"),
  lit("REG2024_2019", "Artículo 4", ["el primer día del mes siguiente al de su publicación"], solo=[1], titulo="Artículo 4 del Reglamento (UE, Euratom) 2024/2019. Entrada en vigor"),
  fichab("Traspaso de cuestiones prejudiciales al Tribunal General en seis materias",
         ["Se presentan **siempre ante el Tribunal de Justicia**, que comprueba la materia y **transfiere** la petición al Tribunal General", "El Tribunal de Justicia se queda las que planteen cuestiones independientes de Derecho primario, Derecho internacional público, principios generales o la Carta"],
         ["::Seis materias:", "IVA (sistema común)", "Impuestos especiales", "Código aduanero", "Clasificación arancelaria (nomenclatura combinada)", "Compensación y asistencia a pasajeros", "Comercio de derechos de emisión de gases de efecto invernadero"],
         "Entrada en vigor: el **primer día del mes siguiente** a su publicación (DO L de 12-8-2024)",
         "Es el desarrollo del art. 256.3 TFUE. La petición **no** se presenta directamente en el Tribunal General: se presenta en el **Tribunal de Justicia**, que la transfiere."))}

{unidad("2.3 La casación ante el Tribunal de Justicia (Estatuto, art. 56)",
  lit("ESTJUE", "Artículo 56", ["en un plazo de dos meses a partir de la notificación de la resolución impugnada", "cuyas pretensiones hayan sido total o parcialmente desestimadas", "Salvo en los litigios entre la Unión y sus agentes"]),
  fichab("Recurso contra las resoluciones del Tribunal General",
         "Las partes cuyas pretensiones se hayan desestimado total o parcialmente (y, salvo litigios de personal, Estados e instituciones aunque no intervinieran)",
         "Contra resoluciones que pongan fin al proceso, resuelvan parcialmente el fondo o pongan fin a un incidente de incompetencia o inadmisibilidad",
         "**Dos meses** desde la notificación",
         "Plazo de **dos meses** desde la **notificación** (el mismo número que el del recurso de anulación, pero contado desde la notificación de la resolución)."))}

{unidad("2.4 Tribunales especializados (art. 257)",
  lit("TFUE", "Artículo 257", ["con arreglo al procedimiento legislativo ordinario, podrán crear tribunales especializados adjuntos al Tribunal General", "recurso de casación limitado a las cuestiones de Derecho", "recurso de apelación referente también a las cuestiones de hecho", "Serán designados por el Consejo por unanimidad"]),
  fichab("Tribunales de primera instancia en materias específicas",
         ["Los crean el **Parlamento Europeo y el Consejo**, por reglamentos", "A propuesta de la Comisión (previa consulta al Tribunal de Justicia) o a instancia del Tribunal de Justicia (previa consulta a la Comisión)", "Miembros: los designa el **Consejo por unanimidad**"],
         ["Adjuntos al **Tribunal General**", "Contra sus resoluciones: **casación** (derecho) ante el Tribunal General o, si el reglamento lo prevé, **apelación** (también hechos)"],
         "Creación: procedimiento legislativo **ordinario**; miembros: **unanimidad** del Consejo",
         "Están **adjuntos al Tribunal General** (no al Tribunal de Justicia), y es el Tribunal General el que conoce de los recursos contra sus resoluciones."))}

""", 2)

T.ap("s6", "II.3 El recurso por incumplimiento (TFUE, arts. 258 a 260)", f"""
{unidad("3.1 A iniciativa de la Comisión (art. 258)",
  lit("TFUE", "Artículo 258", ["emitirá un dictamen motivado", "después de haber ofrecido a dicho Estado la posibilidad de presentar sus observaciones", "en el plazo determinado por la Comisión"]),
  fichab("Recurso contra un Estado miembro que incumple los Tratados",
         "La **Comisión** contra un **Estado miembro**",
         ["1.º Observaciones del Estado", "2.º **Dictamen motivado** de la Comisión", "3.º Si el Estado no se atiene a él: recurso ante el TJUE"],
         "El plazo para atenerse al dictamen lo fija **la Comisión**",
         "Fase previa obligatoria: observaciones + **dictamen motivado**. El plazo no lo fija el Tratado sino la **Comisión**."))}

{unidad("3.2 A iniciativa de otro Estado miembro (art. 259)",
  lit("TFUE", "Artículo 259", ["deberá someter el asunto a la Comisión", "por escrito y oralmente en procedimiento contradictorio", "en el plazo de tres meses"]),
  fichab("Recurso de un Estado contra otro por incumplimiento",
         "Un **Estado miembro** contra otro",
         ["Antes, el asunto se somete a la **Comisión**", "La Comisión emite **dictamen motivado** tras oír a los Estados por escrito y oralmente"],
         "Si la Comisión no emite dictamen en **tres meses**, se puede recurrir igualmente",
         "**Tres meses**: pasado ese plazo sin dictamen de la Comisión, la falta de dictamen **no impide** recurrir."))}

{unidad("3.3 Ejecución de la sentencia y sanciones económicas (art. 260)",
  lit("TFUE", "Artículo 260", ["estará obligado a adoptar las medidas necesarias para la ejecución de la sentencia", "suma a tanto alzado o de la multa coercitiva", "obligación de informar sobre las medidas de transposición de una directiva", "dentro del límite del importe indicado por la Comisión"]),
  fichab("Consecuencias de la sentencia de incumplimiento",
         ["El Estado condenado ejecuta la sentencia", "La **Comisión** puede volver al TJUE e indicar el importe", "El **TJUE** impone la sanción"],
         ["260.2: si el Estado no ejecuta la sentencia → nuevo recurso → **suma a tanto alzado o multa coercitiva**", "260.3: si no informa de las medidas de **transposición de una directiva** → la sanción se puede pedir ya en el primer recurso del 258"],
         "260.3: la sanción, **dentro del límite** del importe indicado por la Comisión; surte efecto en la fecha que fije la sentencia",
         "Las sanciones son **suma a tanto alzado** o **multa coercitiva**. Solo en el caso de no comunicar la **transposición** de directivas puede pedirse sanción en el **primer** recurso, y con el **tope** que indique la Comisión."))}
""", 2)

T.ap("s7", "II.4 Control de legalidad: anulación, omisión y excepción de ilegalidad (TFUE, arts. 263 a 266 y 277)", f"""
{unidad("4.1 El recurso de anulación (art. 263)",
  lit("TFUE", "Artículo 263", ["que no sean recomendaciones o dictámenes", "destinados a producir efectos jurídicos frente a terceros", "incompetencia, vicios sustanciales de forma, violación de los Tratados o de cualquier norma jurídica relativa a su ejecución, o desviación de poder", "por un Estado miembro, el Parlamento Europeo, el Consejo o la Comisión", "por el Tribunal de Cuentas, por el Banco Central Europeo y por el Comité de las Regiones con el fin de salvaguardar prerrogativas de éstos", "que la afecten directa e individualmente", "en el plazo de dos meses"]),
  fichab("Control de la legalidad de los actos de la Unión",
         ["::Legitimados:", "**Privilegiados**: Estado miembro, Parlamento Europeo, Consejo, Comisión", "**Semiprivilegiados** (para salvaguardar sus prerrogativas): **Tribunal de Cuentas, BCE y Comité de las Regiones**", "**Particulares**: actos de los que sean destinatarios, que les afecten directa e individualmente, o actos reglamentarios que les afecten directamente sin medidas de ejecución"],
         ["Actos impugnables: legislativos; del Consejo, Comisión y BCE (no recomendaciones ni dictámenes); del Parlamento y del Consejo Europeo y de órganos y organismos, si producen efectos frente a terceros", "Motivos: **incompetencia**, **vicios sustanciales de forma**, **violación de los Tratados** o de normas de ejecución, **desviación de poder**"],
         "Plazo: **dos meses** desde la publicación, la notificación o el conocimiento del acto",
         "El **Comité Económico y Social no** está entre los legitimados del párrafo tercero (cayó en 2025, → Cierre 1). Las **recomendaciones y dictámenes** no se impugnan."))}

{unidad("4.2 Efectos de la sentencia de anulación (arts. 264 y 266)",
  lit("TFUE", "Artículo 264", ["nulo y sin valor ni efecto alguno", "que deban ser considerados como definitivos"]),
  lit("TFUE", "Artículo 266", ["estarán obligados a adoptar las medidas necesarias para la ejecución de la sentencia"], solo=[1]),
  fichab("Qué pasa si el recurso prospera",
         ["El TJUE declara nulo el acto y puede mantener efectos", "La institución, órgano u organismo autor ejecuta la sentencia"],
         ["Nulidad: «nulo y sin valor ni efecto alguno»", "El Tribunal puede indicar qué efectos del acto anulado son **definitivos**"],
         "—",
         "La nulidad es la regla, pero el Tribunal **puede mantener** efectos como definitivos. La obligación de ejecutar alcanza también a la **abstención** declarada contraria a los Tratados (266)."))}

{unidad("4.3 El recurso por omisión (art. 265)",
  lit("TFUE", "Artículo 265", ["se abstuvieren de pronunciarse", "requeridos previamente para que actúen", "dentro de un nuevo plazo de dos meses", "recurrir en queja"]),
  fichab("Recurso contra la inactividad de las instituciones",
         ["Contra: Parlamento Europeo, Consejo Europeo, Consejo, Comisión, BCE, y órganos y organismos", "Recurren: Estados miembros y demás instituciones; los particulares, «en queja», si no se les ha dirigido un acto"],
         "Requerimiento previo a la institución para que actúe; si no define su posición, recurso",
         ["**Dos meses** para que la institución responda al requerimiento", "**Otros dos meses** para recurrir"],
         "Sin **requerimiento previo** no se admite. Los plazos son **2 + 2 meses**. El particular recurre por no haberle dirigido un acto distinto de **recomendación o dictamen**."))}

{unidad("4.4 La excepción de ilegalidad (art. 277)",
  lit("TFUE", "Artículo 277", ["Aunque haya expirado el plazo previsto en el párrafo sexto del artículo 263", "acto de alcance general", "alegando la inaplicabilidad de dicho acto"]),
  fichab("Impugnación indirecta de actos de alcance general",
         "Cualquiera de las partes de un litigio",
         "Alegar la **inaplicabilidad** de un acto de alcance general por los motivos del art. 263",
         "Cabe **aunque** haya expirado el plazo de **dos meses** del recurso de anulación",
         "No anula el acto: pide que se declare **inaplicable** en el litigio. Sirve **después** de vencido el plazo del 263."))}
""", 2)

T.ap("s8", "II.5 La cuestión prejudicial (TFUE, art. 267)", f"""
{unidad("5.1 Interpretación y validez del Derecho de la Unión (art. 267)",
  lit("TFUE", "Artículo 267", ["sobre la interpretación de los Tratados", "sobre la validez e interpretación de los actos adoptados por las instituciones, órganos u organismos de la Unión", "dicho órgano podrá pedir al Tribunal", "cuyas decisiones no sean susceptibles de ulterior recurso judicial de Derecho interno, dicho órgano estará obligado", "con la mayor brevedad"]),
  fichab("Diálogo entre los jueces nacionales y el TJUE",
         ["Plantea: un **órgano jurisdiccional** de un Estado miembro", "Resuelve: el TJUE (en seis materias, el Tribunal General: → II.2.2)"],
         ["Objeto: **interpretación** de los Tratados; **validez e interpretación** de los actos de instituciones, órganos u organismos", "Facultativa: si el juez estima necesaria la decisión para su fallo", "**Obligatoria**: si sus decisiones **no son susceptibles de ulterior recurso** de Derecho interno"],
         "Persona **privada de libertad**: el TJUE se pronuncia **con la mayor brevedad**",
         "De los **Tratados** solo se pide **interpretación**; de los **actos** se pide **validez e interpretación**. Obligada a plantearla: la última instancia."))}
""", 2)

T.ap("s9", "II.6 Otras competencias y límites (TFUE, arts. 261, 262 y 268 a 276)", f"""
{unidad("6.1 Sanciones y títulos de propiedad intelectual (arts. 261 y 262)",
  lit("TFUE", "Artículo 261", ["competencia jurisdiccional plena respecto de las sanciones"]),
  lit("TFUE", "Artículo 262", ["por unanimidad, con arreglo a un procedimiento legislativo especial y previa consulta al Parlamento Europeo", "títulos europeos de propiedad intelectual o industrial", "cuando hayan sido aprobadas por los Estados miembros"]),
  fichab("Competencias que pueden atribuirse al TJUE",
         ["Reglamentos del Parlamento y del Consejo, o del Consejo (261)", "El **Consejo** (262)"],
         ["Competencia jurisdiccional **plena** sobre las sanciones de esos reglamentos (261)", "Litigios sobre **títulos europeos de propiedad intelectual o industrial** (262)"],
         "262: Consejo **por unanimidad**, procedimiento legislativo **especial**, consulta al Parlamento y aprobación de los **Estados**",
         "La atribución del 262 necesita, además, la **aprobación de los Estados miembros** según sus normas constitucionales."))}

{unidad("6.2 Responsabilidad, personal, BEI y BCN, cláusula compromisoria y compromiso (arts. 268 a 273)",
  lit("TFUE", "Artículo 268", ["indemnización por daños"]),
  lit("TFUE", "Artículo 269", ["en virtud del artículo 7 del Tratado de la Unión Europea", "únicamente en lo que se refiere al respeto de las disposiciones de procedimiento", "en el plazo de un mes"]),
  lit("TFUE", "Artículo 270", ["cualquier litigio entre la Unión y sus agentes"]),
  lit("TFUE", "Artículo 271", ["Estatutos del Banco Europeo de Inversiones", "bancos centrales nacionales"], solo=[1, 2, 5]),
  lit("TFUE", "Artículo 272", ["cláusula compromisoria"]),
  lit("TFUE", "Artículo 273", ["en virtud de un compromiso"]),
  fichab("Otras competencias del TJUE",
         "El TJUE (en primera instancia, el Tribunal General para 268, 270 y 272: → II.2.1)",
         ["**268**: indemnización por daños (responsabilidad extracontractual, art. 340)", "**269**: actos del art. 7 TUE, solo a petición del Estado afectado y **solo por el procedimiento**", "**270**: litigios con sus **agentes**", "**271**: obligaciones derivadas de los Estatutos del **BEI** y de los del SEBC y del BCE por los **bancos centrales nacionales**", "**272**: **cláusula compromisoria** en contratos de la Unión", "**273**: controversias entre Estados si se le someten **por compromiso**"],
         "Art. 269: petición en **un mes** desde la constatación; el Tribunal resuelve en **un mes**",
         "Art. 7 TUE: el control es **solo procedimental** y **solo a petición del Estado** afectado; plazos de **un mes**. En el 271 d), el Consejo de Gobierno del BCE tiene frente a los bancos centrales nacionales los poderes de la Comisión del art. 258."))}

{unidad("6.3 Límites: jurisdicciones nacionales, PESC y orden público (arts. 274 a 276)",
  lit("TFUE", "Artículo 274", ["no podrán ser, por tal motivo, sustraídos a la competencia de las jurisdicciones nacionales"]),
  lit("TFUE", "Artículo 275", ["no será competente para pronunciarse sobre las disposiciones relativas a la política exterior y de seguridad común", "controlar el respeto del artículo 40 del Tratado de la Unión Europea", "medidas restrictivas frente a personas físicas o jurídicas"]),
  lit("TFUE", "Artículo 276", ["operaciones efectuadas por la policía u otros servicios con funciones coercitivas", "mantenimiento del orden público y de la salvaguardia de la seguridad interior"]),
  fichab("Lo que el TJUE no juzga",
         "—",
         ["Que la Unión sea parte no saca el litigio de los **jueces nacionales** (274)", "**PESC**: no es competente, salvo el control del **art. 40 TUE** y las **medidas restrictivas** contra personas físicas o jurídicas (275)", "Espacio de libertad, seguridad y justicia: no controla operaciones **policiales** ni el **orden público** y la **seguridad interior** (276)"],
         "—",
         "PESC: regla de **incompetencia** con **dos** excepciones (art. 40 TUE y medidas restrictivas contra particulares)."))}
""", 2)

T.ap("s10", "II.7 Disposiciones comunes y Estatuto (TFUE, arts. 278 a 281; Estatuto, art. 20)", f"""
{unidad("7.1 Sin efecto suspensivo; suspensión y medidas provisionales (arts. 278 y 279)",
  lit("TFUE", "Artículo 278", ["no tendrán efecto suspensivo", "ordenar la suspensión de la ejecución del acto impugnado"]),
  lit("TFUE", "Artículo 279", ["medidas provisionales necesarias"]),
  fichab("Tutela cautelar", "El TJUE", ["Regla: los recursos **no suspenden**", "El Tribunal puede ordenar la **suspensión** si las circunstancias lo exigen", "Puede ordenar **medidas provisionales**"], "—",
         "La regla es la **no suspensión**; la suspensión es una decisión del Tribunal, no automática."))}

{unidad("7.2 Fuerza ejecutiva de las sentencias (art. 280)",
  lit("TFUE", "Artículo 280", ["tendrán fuerza ejecutiva en las condiciones que establece el artículo 299"]),
  fichab("Ejecución forzosa de las sentencias", "—", "Según el art. 299 TFUE", "—", "Remite al **art. 299** (tema II.2)."))}

{unidad("7.3 El Estatuto del TJUE (art. 281)",
  lit("TFUE", "Artículo 281", ["en un protocolo independiente", "a excepción de su título I y su artículo 64"]),
  fichab("Norma que regula el TJUE",
         ["Modifican el Estatuto: el **Parlamento Europeo y el Consejo**", "A petición del Tribunal de Justicia (consulta a la Comisión) o a propuesta de la Comisión (consulta al Tribunal)"],
         "El Estatuto está en un **protocolo** anejo (Protocolo n.º 3)",
         "Procedimiento legislativo **ordinario**, salvo el **título I** y el **art. 64** (régimen lingüístico)",
         "El Estatuto se modifica por procedimiento legislativo **ordinario** (así se hizo con el Reglamento 2024/2019, → II.2.2), pero **no** su título I ni su art. 64."))}

{unidad("7.4 El procedimiento: fase escrita y fase oral (Estatuto, art. 20)",
  lit("ESTJUE", "Artículo 20", ["dos fases: una escrita y otra oral", "las conclusiones del Abogado General", "no plantea ninguna cuestión de derecho nueva"], solo=[1, 4, 5]),
  fichab("Cómo se tramita un asunto ante el Tribunal de Justicia",
         "Partes, agentes, asesores y abogados; el Abogado General",
         ["Fase **escrita**", "Fase **oral**: audiencia, conclusiones del Abogado General y, en su caso, testigos y peritos"],
         "—",
         "Sin cuestión de derecho nueva, el Tribunal puede juzgar **sin conclusiones** del Abogado General, **oído** el Abogado General."))}

?> **Vigencia de los artículos del Estatuto citados.** El Estatuto se cita en el texto de la versión consolidada de los Tratados de 2016 (DO C 202 de 7-6-2016). Según la ficha de EUR-Lex del Protocolo n.º 3 (relaciones entre documentos) [[DOUE|https://eur-lex.europa.eu/legal-content/ES/ALL/?uri=CELEX:12016E/PRO/03]], después lo han modificado tres reglamentos (2016/1192, 2019/629 y 2024/2019) en otros artículos (23, 49 bis, 50, 50 bis, 50 ter, 51, 54, 58 bis, 62 quater y 62 quinquies, y el anexo I). Por eso aquí solo se citan artículos **no modificados** (2, 4, 9, 16, 17, 20, 48 y 56) y el art. 50 ter en el texto del Reglamento 2024/2019.

{resumen([
  "Organización: el TJUE comprende **Tribunal de Justicia** (un juez por Estado; **ocho** abogados generales en el Tratado, **once** desde el 7-10-2015 por la Decisión 2013/336/UE), **Tribunal General** (**dos jueces por Estado**: Estatuto, art. 48) y **tribunales especializados** (TUE 19.1; TFUE 252).",
  "Nombran los **Gobiernos de común acuerdo**, por **seis años**, tras consultar al **comité de siete** del art. 255; renovación parcial cada **tres** años. Gran Sala de **15** (quórum 11) y **Pleno** (quórum 17).",
  "Tribunal General: primera instancia (263, 265, 268, 270, 272) con **casación** en dos meses; desde 2024, cuestiones prejudiciales en **seis materias** (Estatuto, art. 50 ter).",
  "Incumplimiento: la **Comisión** (dictamen motivado) o **otro Estado** (previo paso por la Comisión, tres meses); sanciones de **suma a tanto alzado o multa coercitiva** (258 a 260).",
  "Anulación: plazo de **dos meses**; legitimados privilegiados (Estados, Parlamento, Consejo, Comisión) y, por sus prerrogativas, **Tribunal de Cuentas, BCE y Comité de las Regiones** (263).",
  "Omisión: **requerimiento previo** y plazos de **2 + 2 meses** (265); excepción de ilegalidad aunque haya vencido el plazo (277).",
  "Cuestión prejudicial: **obligatoria** para el órgano cuyas decisiones no admiten recurso (267).",
  "Límites: **PESC** (salvo art. 40 TUE y medidas restrictivas), operaciones policiales y orden público (275 y 276); los recursos **no suspenden** (278)."],
  "Siguiente: III. ¿Quién controla las cuentas de la Unión? El Tribunal de Cuentas")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Quién controla las cuentas de la Unión? El Tribunal de Cuentas (TFUE, arts. 285 a 287)", donde(
  "Tercera pregunta. El Tribunal de Cuentas no es un órgano judicial: es la institución que **fiscaliza** las cuentas de la Unión. Hay que saber cómo se compone y qué controla.",
  ["1 Composición y estatuto de sus miembros (arts. 285 y 286)", "2 Funciones: qué controla, cómo y qué informes emite (art. 287)"]))

T.ap("s11", "III.1 Composición y estatuto de sus miembros (TFUE, arts. 285 y 286)", f"""
{unidad("1.1 Función y composición (art. 285)",
  lit("TFUE", "Artículo 285", ["La fiscalización, o control de cuentas de la Unión", "un nacional de cada Estado miembro", "con plena independencia, en interés general de la Unión"]),
  fichab("La institución de control externo de la Unión",
         c("TFUE", "Artículo 285", "un nacional de cada Estado miembro"),
         c("TFUE", "Artículo 285", "con plena independencia, en interés general de la Unión"),
         "—",
         "**Uno por Estado miembro**. Actúan en interés **general de la Unión**, no de su Estado."))}

{unidad("1.2 Nombramiento, mandato y cese (art. 286)",
  lit("TFUE", "Artículo 286", ["instituciones de control externo", "para un período de seis años", "El Consejo, previa consulta al Parlamento Europeo, adoptará la lista de miembros", "El mandato de los miembros del Tribunal de Cuentas será renovable", "por un período de tres años. Su mandato será renovable", "ninguna otra actividad profesional", "si el Tribunal de Justicia, a instancia del Tribunal de Cuentas, declarare"], solo=[1, 2, 3, 4, 5, 6, 9]),
  fichab("Quién nombra a los miembros y cómo terminan",
         ["Propuestas: **cada Estado miembro**", "Lista de miembros: la adopta el **Consejo**, **previa consulta al Parlamento Europeo**", "Presidente: lo eligen **los miembros** de entre ellos", "Cese: lo declara el **Tribunal de Justicia**, a instancia del **Tribunal de Cuentas**"],
         ["Requisito: pertenecer o haber pertenecido a **instituciones de control externo** o estar especialmente calificados; absolutas garantías de independencia", "Sin instrucciones de ningún Gobierno ni organismo; incompatibles con cualquier otra actividad profesional", "Fin del mandato: renovación periódica, fallecimiento, **dimisión voluntaria** o **cese**"],
         ["Mandato: **seis años**, **renovable**", "Presidente: **tres años**, renovable"],
         "Los nombra el **Consejo** tras **consultar** al Parlamento (no lo «aprueba» el Parlamento). El cese lo declara el **Tribunal de Justicia** (en **Pleno**: Estatuto, art. 16, → II.1.3)."))}
""", 2)

T.ap("s12", "III.2 Funciones (TFUE, art. 287)", f"""
{unidad("2.1 Qué examina y qué declaración emite (art. 287.1 y 2)",
  lit("TFUE", "Artículo 287", ["la totalidad de los ingresos y gastos de la Unión", "en la medida en que el acto constitutivo de dicho órgano u organismo no excluya dicho examen", "declaración sobre la fiabilidad de las cuentas y la regularidad y legalidad de las operaciones correspondientes", "garantizará una buena gestión financiera", "sobre la base de las liquidaciones y de las cantidades entregadas a la Unión", "sobre la base de los compromisos asumidos y los pagos realizados", "antes del cierre de las cuentas"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Objeto del control",
         "El Tribunal de Cuentas; destinatarios de la declaración: **Parlamento Europeo y Consejo**",
         ["Cuentas de **todos** los ingresos y gastos de la Unión y de sus órganos u organismos (salvo exclusión en su acto constitutivo)", "Control de **legalidad y regularidad** y de **buena gestión financiera**", "Declaración de **fiabilidad** de las cuentas, publicada en el DOUE"],
         ["Ingresos: sobre **liquidaciones** y cantidades entregadas", "Gastos: sobre **compromisos** y **pagos**", "Pueden hacerse **antes del cierre** del ejercicio"],
         "La declaración de fiabilidad va al **Parlamento y al Consejo**. Gastos: **compromisos y pagos**; ingresos: **liquidaciones y cantidades entregadas**."))}

{unidad("2.2 Dónde controla: documentos, dependencias y Estados miembros (art. 287.3)",
  lit("TFUE", "Artículo 287", ["sobre la documentación contable y, en caso necesario, en las dependencias", "en colaboración con las instituciones nacionales de control", "con espíritu de confianza y manteniendo su independencia"], solo=[7, 8]),
  fichab("Lugares y forma del control",
         "Tribunal de Cuentas, con las **instituciones nacionales de control** (o, si no tienen competencia, los servicios nacionales)",
         ["Sobre la documentación contable y, si es necesario, **sobre el terreno**: instituciones, órganos, Estados miembros y perceptores de fondos", "Todos deben facilitarle documentos e información a su instancia"],
         "—",
         "En los Estados, el control se hace **en colaboración** con las instituciones nacionales de control, «con espíritu de confianza y manteniendo su independencia»."))}

{unidad("2.3 Informes y dictámenes (art. 287.4)",
  lit("TFUE", "Artículo 287", ["después del cierre de cada ejercicio, un informe anual", "acompañado de las respuestas de estas instituciones", "informes especiales", "por mayoría de los miembros que lo componen", "salas", "requerirá la aprobación del Consejo"], solo=[10, 11, 12, 13, 14]),
  fichab("Qué documentos emite y cómo los aprueba",
         "El Tribunal de Cuentas (en Pleno o en salas, según su reglamento interno)",
         ["**Informe anual** tras el cierre de cada ejercicio, publicado en el DOUE con las **respuestas** de las instituciones", "**Informes especiales** y observaciones en cualquier momento", "**Dictámenes** a instancia de otra institución", "Asiste al Parlamento y al Consejo en el control de la ejecución del presupuesto"],
         ["Aprobación: **mayoría de los miembros que lo componen**", "Reglamento interno: con **aprobación del Consejo**"],
         "El informe anual se publica **con las respuestas** de las instituciones. Mayoría de **los miembros que lo componen** (no de los presentes)."))}

{resumen([
  "Composición: **un nacional por Estado miembro**, con plena independencia (285).",
  "Nombramiento: el **Consejo**, **previa consulta al Parlamento**, sobre propuestas de cada Estado; **seis años**, renovable; Presidente **tres años** (286).",
  "Cese: lo declara el **Tribunal de Justicia**, a instancia del Tribunal de Cuentas (286.6).",
  "Funciones: examina **todos** los ingresos y gastos; **declaración de fiabilidad** al Parlamento y al Consejo; **informe anual** con las respuestas de las instituciones (287)."],
  "Siguiente: IV. ¿Quién dirige la política monetaria? El Banco Central Europeo")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Quién dirige la política monetaria? El Banco Central Europeo (TFUE, arts. 282 a 284)", donde(
  "Cuarta pregunta. El BCE es la institución **independiente** que, con los bancos centrales nacionales del euro, dirige la **política monetaria** de la Unión. La política económica y monetaria en sí es del tema II.6.",
  ["1 SEBC, Eurosistema y estatuto del BCE (art. 282)", "2 Órganos rectores y relaciones con las demás instituciones (arts. 283 y 284)", "3 Cuadro comparativo de las cuatro instituciones"]))

T.ap("s13", "IV.1 SEBC, Eurosistema y estatuto del BCE (TFUE, art. 282)", f"""
{unidad("1.1 SEBC y Eurosistema; objetivo; independencia (art. 282)",
  lit("TFUE", "Artículo 282", ["constituirán el Sistema Europeo de Bancos Centrales (SEBC)", "que constituyen el Eurosistema", "mantener la estabilidad de precios", "Le corresponderá en exclusiva autorizar la emisión del euro", "Será independiente en el ejercicio de sus competencias y en la gestión de sus finanzas", "mantendrán sus competencias en el ámbito monetario", "el Banco podrá emitir dictámenes"]),
  fichab("El banco central de la Unión",
         ["**SEBC**: el BCE + **todos** los bancos centrales nacionales", "**Eurosistema**: el BCE + los bancos centrales de los Estados **cuya moneda es el euro**; dirigen la política monetaria"],
         ["Objetivo principal del SEBC: **estabilidad de precios**; sin perjuicio de él, apoya las políticas económicas generales", "El BCE tiene **personalidad jurídica** y autoriza **en exclusiva** la emisión del euro", "Se le consulta sobre proyectos de actos de la Unión y de normas nacionales en su ámbito; puede emitir dictámenes"],
         "—",
         "**SEBC ≠ Eurosistema**: el Eurosistema solo incluye los bancos centrales **del euro**. Independiente en sus competencias **y en la gestión de sus finanzas**. Los Estados sin euro **conservan** sus competencias monetarias."))}
""", 2)

T.ap("s14", "IV.2 Órganos rectores y relaciones con las demás instituciones (TFUE, arts. 283 y 284)", f"""
{unidad("2.1 Consejo de Gobierno y Comité Ejecutivo (art. 283)",
  lit("TFUE", "Artículo 283", ["los miembros del Comité Ejecutivo del Banco Central Europeo y los gobernadores de los bancos centrales nacionales de los Estados miembros cuya moneda sea el euro", "el presidente, el vicepresidente y otros cuatro miembros", "por el Consejo Europeo, por mayoría cualificada", "sobre la base de una recomendación del Consejo y previa consulta al Parlamento Europeo y al Consejo de Gobierno", "ocho años y no será renovable", "Sólo podrán ser miembros del Comité Ejecutivo los nacionales de los Estados miembros"]),
  fichab("Órganos rectores del BCE",
         ["**Consejo de Gobierno**: Comité Ejecutivo + gobernadores de los bancos centrales **del euro**", "**Comité Ejecutivo**: presidente, vicepresidente y **otros cuatro** miembros (**seis**)", "Nombra al Comité Ejecutivo: el **Consejo Europeo**"],
         ["Recomendación del **Consejo**", "Consulta al **Parlamento Europeo** y al **Consejo de Gobierno** del BCE", "Entre personas de reconocido prestigio en asuntos monetarios o bancarios, **nacionales** de los Estados miembros"],
         ["Nombramiento: **mayoría cualificada** del Consejo Europeo", "Mandato: **ocho años**, **no renovable**"],
         "**Ocho** años **no renovables** (frente a los seis renovables del TJUE y del Tribunal de Cuentas). Nombra el **Consejo Europeo** (no el Consejo), por **mayoría cualificada**."))}

{unidad("2.2 Relaciones con el Consejo, la Comisión y el Parlamento (art. 284)",
  lit("TFUE", "Artículo 284", ["podrán participar, sin derecho de voto", "podrá someter una moción a la deliberación", "Se invitará al Presidente del Banco Central Europeo", "un informe anual sobre las actividades del SEBC y sobre la política monetaria del año precedente y del año en curso", "podrán ser oídos por las comisiones competentes del Parlamento Europeo"]),
  fichab("Cooperación y rendición de cuentas del BCE",
         ["Presidente del **Consejo** y un miembro de la **Comisión**: en el Consejo de Gobierno, **sin voto**", "Presidente del BCE: invitado al Consejo cuando se trate de objetivos y funciones del SEBC"],
         ["El Presidente del Consejo puede someter una **moción** al Consejo de Gobierno", "**Informe anual** del BCE al Parlamento, Consejo, Comisión y Consejo Europeo; lo presenta su Presidente al Consejo y al Parlamento", "El Presidente y los miembros del Comité Ejecutivo pueden ser oídos por las comisiones del Parlamento"],
         "Informe **anual** (actividades del SEBC y política monetaria del año precedente y del año en curso)",
         "El Presidente del Consejo y el comisario asisten **sin voto**. El informe anual lo **presenta** el Presidente del BCE al **Consejo y al Parlamento**."))}
""", 2)

T.ap("s15", "IV.3 Cuadro comparativo de las cuatro instituciones (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| | Parlamento Europeo | Tribunal de Justicia | Tribunal de Cuentas | BCE (Comité Ejecutivo) |
|---|---|---|---|---|
| Composición | Máx. 750 + Presidente; 6 a 96 por Estado (TUE 14.2) | Un juez por Estado + abogados generales: 8 en el Tratado, 11 desde 2015 (TUE 19.2; TFUE 252; Decisión 2013/336/UE) | Un nacional por Estado (285) | Presidente, vicepresidente y 4 miembros (283.2) |
| Quién elige o nombra | Los ciudadanos, por sufragio universal directo (TUE 14.3) | Los Gobiernos de común acuerdo, tras el comité del 255 (253) | El Consejo, previa consulta al Parlamento (286.2) | El Consejo Europeo, por mayoría cualificada (283.2) |
| Mandato | 5 años (TUE 14.3) | 6 años, renovable; renovación parcial cada 3 (253) | 6 años, renovable (286.2) | 8 años, no renovable (283.2) |
| Presidente | Elegido por el Parlamento entre sus diputados (TUE 14.4) | Elegido por los jueces, 3 años renovables (253) | Elegido por los miembros, 3 años renovables (286.2) | Nombrado por el Consejo Europeo (283.2) |

{resumen([
  "**SEBC** = BCE + todos los bancos centrales nacionales; **Eurosistema** = BCE + bancos centrales del euro, que dirigen la política monetaria (282.1).",
  "Objetivo principal: **estabilidad de precios**; el BCE es **independiente** y autoriza **en exclusiva** la emisión del euro (282).",
  "Comité Ejecutivo: **seis** miembros nombrados por el **Consejo Europeo** por **mayoría cualificada**, **ocho años no renovables** (283).",
  "Presidente del Consejo y un comisario: en el Consejo de Gobierno **sin voto**; **informe anual** del BCE (284)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_L22 = examen("L", 22, {
  "a": f"Literal del art. 14.4 TUE: {c('TUE', 'Artículo 14', 'El Parlamento Europeo elegirá a su Presidente y a la Mesa de entre sus diputados')}.",
  "b": f"Cambia «conjuntamente» por «en exclusiva»: el Parlamento {c('TUE', 'Artículo 14', 'ejercerá conjuntamente con el Consejo la función legislativa y la función presupuestaria')} (art. 14.1).",
  "c": f"Cambia la formación del Consejo y el artículo (es el 16.6 TUE, tema II.2): {c('TUE', 'Artículo 16', 'El Consejo de Asuntos Generales velará por la coherencia de los trabajos de las diferentes formaciones del Consejo')}.",
  "d": f"Cambia el plazo y el artículo (es el 17.3 TUE, tema II.2): {c('TUE', 'Artículo 17', 'El mandato de la Comisión será de cinco años')}."},
  [("elegirá a su Presidente y a la Mesa de entre sus diputados", "TUE", "Artículo 14", "El Parlamento Europeo elegirá a su Presidente y a la Mesa de entre sus diputados")])
EX_L23 = examen("L", 23, {
  "a": f"Sí está legitimado: el TJUE es competente para los recursos {c('TFUE', 'Artículo 263', 'interpuestos por el Tribunal de Cuentas, por el Banco Central Europeo y por el Comité de las Regiones')} (art. 263, párr. 3).",
  "b": f"Sí está legitimado: el Banco Central Europeo figura en el mismo párrafo tercero, {c('TFUE', 'Artículo 263', 'con el fin de salvaguardar prerrogativas de éstos')}.",
  "c": "Sí está legitimado: el Tribunal de Cuentas es el primero de la lista del párrafo tercero del art. 263.",
  "d": f"Es la respuesta: el **Comité Económico y Social** no aparece entre los legitimados del art. 263, que en su párrafo tercero solo cita {c('TFUE', 'Artículo 263', 'el Tribunal de Cuentas, por el Banco Central Europeo y por el Comité de las Regiones')}."},
  [("Comité Económico y Social", "TFUE", "Artículo 263", "el Tribunal de Cuentas, por el Banco Central Europeo y por el Comité de las Regiones")])
EX_P12 = examen("P", 12, {
  "a": f"Cambia el momento: el comité se pronuncia {c('TFUE', 'Artículo 255', 'antes de que los Gobiernos de los Estados miembros procedan a los nombramientos')}.",
  "b": f"Cambia el número: {c('TFUE', 'Artículo 255', 'El comité estará compuesto por siete personalidades')}.",
  "c": f"Inventa un requisito: el art. 255 no exige años de ejercicio; sus miembros se eligen {c('TFUE', 'Artículo 255', 'de entre antiguos miembros del Tribunal de Justicia y del Tribunal General, miembros de los órganos jurisdiccionales nacionales superiores y juristas de reconocida competencia')}.",
  "d": f"Literal del art. 255: {c('TFUE', 'Artículo 255', 'El Consejo adoptará una decisión por la que se establezcan las normas de funcionamiento del comité')}."},
  [("normas de funcionamiento", "TFUE", "Artículo 255", "El Consejo adoptará una decisión por la que se establezcan las normas de funcionamiento del comité")])
EX_X33 = examen("X", 33, {
  "a": f"Es correcta (no es la que se pide): Reglamento interno del Parlamento Europeo, art. 16.1: {c('RIPE', 'Artículo 16', 'solamente se mantendrán en la cuarta votación las candidaturas de los dos diputados que hubieran obtenido en la tercera el mayor número de votos. En caso de empate, será proclamado electo el candidato de más edad')}.",
  "b": f"Es correcta (no es la que se pide): art. 15.2 del Reglamento interno: {c('RIPE', 'Artículo 15', 'debe velarse, en general, por una representación equitativa de las fuerzas políticas, así como por un equilibrio geográfico y de género')}.",
  "c": f"Es correcta (no es la que se pide): art. 15.1 del Reglamento interno: {c('RIPE', 'Artículo 15', 'El presidente y, a continuación, los vicepresidentes y los cuestores serán elegidos en votación secreta')}.",
  "d": f"Es la INCORRECTA: según el portal oficial del Parlamento Europeo, {c('PEWEB', 'portal', 'Presidenta Roberta Metsola')}. Ursula von der Leyen preside la **Comisión** ([[COMISION|https://commission.europa.eu/about/organisation/college-commissioners_es]]: «La Presidenta Ursula von der Leyen»; tema II.2), no el Parlamento."},
  [("presidenta del Parlamento Europeo", "PEWEB", "portal", "Presidenta Roberta Metsola")])

T.ap("s16", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **cuatro** preguntas de este tema: dos en el turno libre (art. 14 TUE y art. 263 TFUE), una en promoción interna (comité del art. 255) y una en el extraordinario (elección del Presidente del Parlamento). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal (y, en la del extraordinario, contra el Reglamento interno y el portal oficial del Parlamento Europeo).",
  "### GACE-L 2025, pregunta 22 · Presidente y Mesa del Parlamento Europeo (→ I.1.4)", EX_L22,
  "### GACE-L 2025, pregunta 23 · Legitimados en el recurso de anulación (→ II.4.1)", EX_L23,
  "### GACE-P 2025, pregunta 12 · Comité del art. 255 (→ II.1.7)", EX_P12,
  "### GACE-L 2025 extraordinario, pregunta 33 · Elección del Presidente del Parlamento Europeo (→ I.1.4)", EX_X33,
  "### Cómo se pregunta",
  "!> Las preguntas de este tema citan el **artículo** del Tratado y cambian **una palabra**: «conjuntamente» por «en exclusiva», «siete» por «nueve», «antes» por «después», o añaden un órgano que **no** está en la lista (el Comité Económico y Social en el art. 263). Las de actualidad (quién preside) se resuelven con la **fuente oficial** de la institución.",
]))

T.ap("s17", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Parlamento Europeo | Funciones con el Consejo; 750 + Presidente; 5 años; Presidente y Mesa entre sus diputados; peticiones, Defensor del Pueblo, comisiones de investigación; moción de censura | Presidente y Mesa **de entre sus diputados** (TUE 14.4); censura por **2/3 de los emitidos + mayoría de diputados** |
| II. TJUE | Tribunal de Justicia, Tribunal General y tribunales especializados; nombramiento por los Gobiernos; comité del 255; recursos (258 a 277) y cuestión prejudicial (267) | Comité de **siete**; legitimados del 263 (Tribunal de Cuentas, BCE, Comité de las Regiones) |
| III. Tribunal de Cuentas | Un nacional por Estado; nombra el Consejo tras consultar al Parlamento; 6 años; declaración de fiabilidad e informe anual | Nombramiento por el **Consejo**, **previa consulta** al Parlamento |
| IV. BCE | SEBC y Eurosistema; estabilidad de precios; independencia; Comité Ejecutivo de seis | **Ocho años no renovables**, nombra el **Consejo Europeo** |

?> **Trampas frecuentes:** «el Parlamento ejerce **en exclusiva** la función presupuestaria» (es **con el Consejo**); «el comité del art. 255 tiene **nueve** miembros» (son **siete**) o «actúa **después** de los nombramientos» (es **antes**); «el **Comité Económico y Social** puede interponer recurso de anulación para salvaguardar sus prerrogativas» (solo **Tribunal de Cuentas, BCE y Comité de las Regiones**); «el mandato del Comité Ejecutivo del BCE es **renovable**» (**no** lo es); «la moción de censura se vota en secreto» (votación **pública**); «el Defensor del Pueblo lo destituye el Parlamento» (lo destituye el **Tribunal de Justicia**, a petición del Parlamento).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
Q = [
 ("TUE", "Artículo 14", "Parlamento Europeo", "Según el artículo 14.1 del Tratado de la Unión Europea, el Parlamento Europeo ejercerá la función legislativa y la función presupuestaria:",
  ["Conjuntamente con el Consejo.", "En exclusiva.", "Conjuntamente con la Comisión.", "Conjuntamente con el Consejo Europeo."], "Art. 14.1 TUE.", "ejercerá conjuntamente con el Consejo la función legislativa y la función presupuestaria"),
 ("TUE", "Artículo 14", "Parlamento Europeo", "Según el artículo 14.2 del Tratado de la Unión Europea, el número de miembros del Parlamento Europeo no excederá de:",
  ["Setecientos cincuenta, más el Presidente.", "Setecientos cincuenta, incluido el Presidente.", "Setecientos, más el Presidente.", "Setecientos cincuenta y uno, más el Presidente."], "Art. 14.2 TUE.", "Su número no excederá de setecientos cincuenta, más el Presidente"),
 ("TUE", "Artículo 14", "Parlamento Europeo", "Según el artículo 14.2 del Tratado de la Unión Europea, la representación de los ciudadanos en el Parlamento Europeo será decrecientemente proporcional, con un mínimo por Estado miembro de:",
  ["Seis diputados.", "Cuatro diputados.", "Cinco diputados.", "Ocho diputados."], "Art. 14.2 TUE: «con un mínimo de seis diputados por Estado miembro».", "con un mínimo de seis diputados por Estado miembro"),
 ("TUE", "Artículo 14", "Parlamento Europeo", "Según el artículo 14.2 del Tratado de la Unión Europea, no se asignará a ningún Estado miembro más de:",
  ["Noventa y seis escaños.", "Noventa y nueve escaños.", "Cien escaños.", "Ochenta escaños."], "Art. 14.2 TUE.", "No se asignará a ningún Estado miembro más de noventa y seis escaños"),
 ("TUE", "Artículo 14", "Parlamento Europeo", "Según el artículo 14.2 del Tratado de la Unión Europea, la decisión por la que se fije la composición del Parlamento Europeo la adoptará:",
  ["El Consejo Europeo, por unanimidad, a iniciativa del Parlamento Europeo y con su aprobación.", "El Consejo, por mayoría cualificada, a propuesta de la Comisión.", "El Parlamento Europeo, por mayoría de los miembros que lo componen.", "El Consejo Europeo, por mayoría cualificada, previa consulta al Parlamento Europeo."], "Art. 14.2 TUE, párrafo segundo.", "El Consejo Europeo adoptará por unanimidad, a iniciativa del Parlamento Europeo y con su aprobación"),
 ("TUE", "Artículo 14", "Parlamento Europeo", "Según el artículo 14.3 del Tratado de la Unión Europea, los diputados al Parlamento Europeo serán elegidos para un mandato de:",
  ["Cinco años.", "Cuatro años.", "Seis años.", "Dos años y medio."], "Art. 14.3 TUE.", "por sufragio universal directo, libre y secreto, para un mandato de cinco años"),
 ("TFUE", "Artículo 223", "Parlamento Europeo", "Según el artículo 223.1 del TFUE, las disposiciones necesarias para la elección de los miembros del Parlamento Europeo por sufragio universal directo las establecerá:",
  ["El Consejo, por unanimidad, con arreglo a un procedimiento legislativo especial, previa aprobación del Parlamento Europeo.", "El Parlamento Europeo y el Consejo, con arreglo al procedimiento legislativo ordinario.", "El Parlamento Europeo, por mayoría de los votos emitidos.", "La Comisión, previa consulta al Parlamento Europeo."], "Art. 223.1 TFUE.", "El Consejo establecerá las disposiciones necesarias por unanimidad con arreglo a un procedimiento legislativo especial, previa aprobación del Parlamento Europeo"),
 ("TFUE", "Artículo 225", "Parlamento Europeo", "Según el artículo 225 del TFUE, el Parlamento Europeo podrá solicitar a la Comisión que presente las propuestas oportunas por decisión de:",
  ["La mayoría de los miembros que lo componen.", "La mayoría de los votos emitidos.", "La cuarta parte de sus miembros.", "Dos tercios de los votos emitidos."], "Art. 225 TFUE.", "Por decisión de la mayoría de los miembros que lo componen, el Parlamento Europeo podrá solicitar a la Comisión"),
 ("TFUE", "Artículo 226", "Parlamento Europeo", "Según el artículo 226 del TFUE, el Parlamento Europeo podrá constituir una comisión temporal de investigación a petición de:",
  ["La cuarta parte de los miembros que lo componen.", "La tercera parte de los miembros que lo componen.", "La mayoría de los miembros que lo componen.", "La Comisión o el Consejo."], "Art. 226 TFUE.", "a petición de la cuarta parte de los miembros que lo componen"),
 ("TFUE", "Artículo 227", "Parlamento Europeo", "Según el artículo 227 del TFUE, el derecho a presentar una petición al Parlamento Europeo sobre un asunto propio de los ámbitos de actuación de la Unión exige que el asunto:",
  ["Le afecte directamente.", "Le afecte directa e individualmente.", "Haya sido previamente planteado ante la Comisión.", "Haya sido objeto de una reclamación ante el Defensor del Pueblo."], "Art. 227 TFUE.", "un asunto propio de los ámbitos de actuación de la Unión que le afecte directamente"),
 ("TFUE", "Artículo 228", "Parlamento Europeo", "Según el artículo 228 del TFUE, el Defensor del Pueblo Europeo será elegido:",
  ["Por el Parlamento Europeo, después de cada elección del Parlamento Europeo, para toda la legislatura.", "Por el Consejo, por un período de cinco años no renovable.", "Por el Parlamento Europeo, por un período de seis años.", "Por la Comisión, previa consulta al Parlamento Europeo."], "Art. 228.1 y 2 TFUE.", "El Defensor del Pueblo será elegido después de cada elección del Parlamento Europeo para toda la legislatura"),
 ("TFUE", "Artículo 228", "Parlamento Europeo", "Según el artículo 228 del TFUE, a petición del Parlamento Europeo, podrá destituir al Defensor del Pueblo:",
  ["El Tribunal de Justicia.", "El Consejo, por unanimidad.", "El propio Parlamento Europeo, por mayoría de dos tercios.", "El Consejo Europeo."], "Art. 228.2 TFUE.", "A petición del Parlamento Europeo, el Tribunal de Justicia podrá destituir al Defensor del Pueblo"),
 ("TFUE", "Artículo 228", "Parlamento Europeo", "Según el artículo 228 del TFUE, cuando el Defensor del Pueblo haya comprobado un caso de mala administración, la institución interesada dispondrá para exponer su posición de un plazo de:",
  ["Tres meses.", "Un mes.", "Dos meses.", "Seis meses."], "Art. 228.1 TFUE.", "que dispondrá de un plazo de tres meses para exponer su posición al Defensor del Pueblo"),
 ("TFUE", "Artículo 229", "Parlamento Europeo", "Según el artículo 229 del TFUE, el Parlamento Europeo se reunirá sin necesidad de previa convocatoria:",
  ["El segundo martes de marzo.", "El primer martes de marzo.", "El segundo martes de septiembre.", "El primer lunes de enero."], "Art. 229 TFUE.", "Se reunirá sin necesidad de previa convocatoria el segundo martes de marzo"),
 ("TFUE", "Artículo 231", "Parlamento Europeo", "Según el artículo 231 del TFUE, salvo disposición en contrario de los Tratados, el Parlamento Europeo decidirá por:",
  ["Mayoría de los votos emitidos.", "Mayoría de los miembros que lo componen.", "Mayoría de dos tercios.", "Mayoría cualificada."], "Art. 231 TFUE.", "el Parlamento Europeo decidirá por mayoría de los votos emitidos"),
 ("TFUE", "Artículo 234", "Parlamento Europeo", "Según el artículo 234 del TFUE, el Parlamento Europeo solo podrá pronunciarse sobre una moción de censura sobre la gestión de la Comisión:",
  ["Transcurridos tres días como mínimo desde la fecha de su presentación y en votación pública.", "Transcurridos cinco días como mínimo desde su presentación y en votación secreta.", "Transcurridas cuarenta y ocho horas desde su presentación y en votación pública.", "Transcurridos tres días como mínimo desde su presentación y en votación secreta."], "Art. 234 TFUE.", "transcurridos tres días como mínimo desde la fecha de su presentación y en votación pública"),
 ("TFUE", "Artículo 234", "Parlamento Europeo", "Según el artículo 234 del TFUE, la moción de censura contra la Comisión se aprueba por:",
  ["Mayoría de dos tercios de los votos emitidos que representen, a su vez, la mayoría de los diputados que componen el Parlamento Europeo.", "Mayoría absoluta de los diputados que componen el Parlamento Europeo.", "Mayoría de tres quintos de los votos emitidos.", "Mayoría de dos tercios de los diputados que componen el Parlamento Europeo."], "Art. 234 TFUE.", "por mayoría de dos tercios de los votos emitidos que representen, a su vez, la mayoría de los diputados que componen el Parlamento Europeo"),
 ("TUE", "Artículo 19", "TJUE", "Según el artículo 19.1 del Tratado de la Unión Europea, el Tribunal de Justicia de la Unión Europea comprenderá:",
  ["El Tribunal de Justicia, el Tribunal General y los tribunales especializados.", "El Tribunal de Justicia, el Tribunal General y el Tribunal de Cuentas.", "El Tribunal de Justicia y el Tribunal de la Función Pública.", "El Tribunal de Justicia, el Tribunal General y el Defensor del Pueblo Europeo."], "Art. 19.1 TUE.", "comprenderá el Tribunal de Justicia, el Tribunal General y los tribunales especializados"),
 ("TUE", "Artículo 19", "TJUE", "Según el artículo 19.2 del Tratado de la Unión Europea, los jueces y abogados generales del Tribunal de Justicia serán nombrados:",
  ["De común acuerdo por los Gobiernos de los Estados miembros para un período de seis años.", "Por el Consejo, por mayoría cualificada, para un período de seis años.", "Por el Parlamento Europeo, a propuesta de los Estados, para un período de cinco años.", "De común acuerdo por los Gobiernos de los Estados miembros para un período de nueve años."], "Art. 19.2 TUE.", "Serán nombrados de común acuerdo por los Gobiernos de los Estados miembros para un período de seis años"),
 ("TFUE", "Artículo 252", "TJUE", "Según el artículo 252 del TFUE, el Tribunal de Justicia estará asistido por:",
  ["Ocho abogados generales.", "Seis abogados generales.", "Un abogado general por Estado miembro.", "Dos abogados generales por Estado miembro."], "Art. 252 TFUE (el Consejo, por unanimidad, puede aumentar su número: la Decisión 2013/336/UE los elevó a once desde el 7-10-2015).", "El Tribunal de Justicia estará asistido por ocho abogados generales"),
 ("TFUE", "Artículo 253", "TJUE", "Según el artículo 253 del TFUE, el Presidente del Tribunal de Justicia será elegido:",
  ["Por los jueces, de entre ellos, por un período de tres años renovable.", "Por los Gobiernos de los Estados miembros, por un período de seis años.", "Por el Consejo, por un período de tres años no renovable.", "Por los jueces y abogados generales, por un período de seis años."], "Art. 253 TFUE.", "Los jueces elegirán de entre ellos al Presidente del Tribunal de Justicia por un período de tres años. Su mandato será renovable"),
 ("TFUE", "Artículo 255", "TJUE", "Según el artículo 255 del TFUE, el comité que se pronuncia sobre la idoneidad de los candidatos a juez y abogado general estará compuesto por:",
  ["Siete personalidades, una de las cuales será propuesta por el Parlamento Europeo.", "Nueve personalidades, una de las cuales será propuesta por el Parlamento Europeo.", "Siete personalidades, todas propuestas por el Consejo.", "Un representante de cada Estado miembro."], "Art. 255 TFUE.", "El comité estará compuesto por siete personalidades"),
 ("ESTJUE", "Artículo 16", "TJUE", "Según el artículo 16 del Estatuto del Tribunal de Justicia de la Unión Europea, la Gran Sala estará compuesta por:",
  ["Quince jueces.", "Trece jueces.", "Once jueces.", "Diecisiete jueces."], "Estatuto, art. 16 (quórum de la Gran Sala: once, art. 17).", "La Gran Sala estará compuesta por quince Jueces"),
 ("ESTJUE", "Artículo 16", "TJUE", "Según el artículo 16 del Estatuto del Tribunal de Justicia de la Unión Europea, el Tribunal actuará en Gran Sala cuando lo solicite:",
  ["Un Estado miembro o una institución de la Unión que sea parte en el proceso.", "Cualquiera de las partes en el proceso.", "El Abogado General.", "El órgano jurisdiccional nacional que plantee la cuestión prejudicial."], "Estatuto, art. 16.", "cuando lo solicite un Estado miembro o una institución de la Unión que sea parte en el proceso"),
 ("ESTJUE", "Artículo 17", "TJUE", "Según el artículo 17 del Estatuto del Tribunal de Justicia de la Unión Europea, las deliberaciones del Tribunal reunido en Pleno solo serán válidas si están presentes:",
  ["Diecisiete jueces.", "Quince jueces.", "Once jueces.", "La mitad más uno de los jueces."], "Estatuto, art. 17.", "sólo serán válidas si están presentes diecisiete Jueces"),
 ("ESTJUE", "Artículo 48", "TJUE", "Según el artículo 48 del Estatuto del Tribunal de Justicia de la Unión Europea, a partir del 1 de septiembre de 2019 el Tribunal General estará compuesto por:",
  ["Dos jueces por Estado miembro.", "Un juez por Estado miembro.", "Cuarenta y siete jueces.", "Tres jueces por Estado miembro."], "Estatuto, art. 48 c).", "dos Jueces por Estado miembro a partir del 1 de septiembre de 2019"),
 ("TFUE", "Artículo 256", "TJUE", "Según el artículo 256 del TFUE, contra las resoluciones dictadas en primera instancia por el Tribunal General podrá interponerse ante el Tribunal de Justicia:",
  ["Recurso de casación limitado a las cuestiones de Derecho.", "Recurso de apelación sobre cuestiones de hecho y de Derecho.", "Recurso de anulación.", "Cuestión prejudicial."], "Art. 256.1 TFUE.", "recurso de casación ante el Tribunal de Justicia limitado a las cuestiones de Derecho"),
 ("TFUE", "Artículo 257", "TJUE", "Según el artículo 257 del TFUE, los tribunales especializados estarán adjuntos:",
  ["Al Tribunal General.", "Al Tribunal de Justicia.", "A la Comisión.", "Al Tribunal de Cuentas."], "Art. 257 TFUE.", "podrán crear tribunales especializados adjuntos al Tribunal General"),
 ("TFUE", "Artículo 259", "TJUE", "Según el artículo 259 del TFUE, si la Comisión no hubiere emitido el dictamen motivado solicitado por un Estado miembro antes de recurrir contra otro Estado, la falta de dictamen no será obstáculo para recurrir al Tribunal transcurrido un plazo de:",
  ["Tres meses desde la fecha de la solicitud.", "Dos meses desde la fecha de la solicitud.", "Seis meses desde la fecha de la solicitud.", "Un mes desde la fecha de la solicitud."], "Art. 259 TFUE.", "Si la Comisión no hubiere emitido el dictamen en el plazo de tres meses desde la fecha de la solicitud"),
 ("TFUE", "Artículo 260", "TJUE", "Según el artículo 260.2 del TFUE, si el Tribunal declarare que el Estado miembro afectado ha incumplido su sentencia, podrá imponerle:",
  ["El pago de una suma a tanto alzado o de una multa coercitiva.", "La suspensión de su derecho de voto en el Consejo.", "La pérdida de los fondos de cohesión.", "La anulación de la norma nacional contraria al Derecho de la Unión."], "Art. 260.2 TFUE.", "podrá imponerle el pago de una suma a tanto alzado o de una multa coercitiva"),
 ("TFUE", "Artículo 263", "TJUE", "Según el artículo 263 del TFUE, los recursos de anulación deberán interponerse en el plazo de:",
  ["Dos meses.", "Un mes.", "Tres meses.", "Seis meses."], "Art. 263, párrafo sexto, TFUE.", "deberán interponerse en el plazo de dos meses"),
 ("TFUE", "Artículo 263", "TJUE", "Según el artículo 263 del TFUE, el Tribunal de Justicia de la Unión Europea NO controla la legalidad de los actos del Consejo, de la Comisión y del Banco Central Europeo que sean:",
  ["Recomendaciones o dictámenes.", "Reglamentos.", "Decisiones.", "Directivas."], "Art. 263, párrafo primero, TFUE.", "que no sean recomendaciones o dictámenes"),
 ("TFUE", "Artículo 265", "TJUE", "Según el artículo 265 del TFUE, el recurso por omisión solamente será admisible si la institución, órgano u organismo de que se trate:",
  ["Hubiere sido requerido previamente para que actúe.", "Hubiere sido objeto de un dictamen motivado de la Comisión.", "Hubiere dejado transcurrir seis meses sin pronunciarse.", "Hubiere sido advertido por el Parlamento Europeo."], "Art. 265 TFUE.", "si la institución, órgano u organismo de que se trate hubieren sido requeridos previamente para que actúen"),
 ("TFUE", "Artículo 267", "TJUE", "Según el artículo 267 del TFUE, está obligado a someter la cuestión prejudicial al Tribunal el órgano jurisdiccional nacional:",
  ["Cuyas decisiones no sean susceptibles de ulterior recurso judicial de Derecho interno.", "Que conozca en primera instancia.", "Que tenga dudas sobre la constitucionalidad de una ley nacional.", "Que haya sido requerido por la Comisión."], "Art. 267 TFUE, párrafo tercero.", "cuyas decisiones no sean susceptibles de ulterior recurso judicial de Derecho interno, dicho órgano estará obligado"),
 ("TFUE", "Artículo 269", "TJUE", "Según el artículo 269 del TFUE, la petición del Estado miembro para que el Tribunal de Justicia se pronuncie sobre un acto adoptado en virtud del artículo 7 del TUE deberá presentarse en el plazo de:",
  ["Un mes a partir de la constatación.", "Dos meses a partir de la constatación.", "Tres meses a partir de la constatación.", "Quince días a partir de la constatación."], "Art. 269 TFUE.", "Esta petición deberá presentarse en el plazo de un mes a partir de la constatación"),
 ("TFUE", "Artículo 278", "TJUE", "Según el artículo 278 del TFUE, los recursos interpuestos ante el Tribunal de Justicia de la Unión Europea:",
  ["No tendrán efecto suspensivo, aunque el Tribunal podrá ordenar la suspensión si las circunstancias lo exigen.", "Tendrán siempre efecto suspensivo.", "Tendrán efecto suspensivo solo si los interpone un Estado miembro.", "Tendrán efecto suspensivo salvo que el Tribunal disponga lo contrario."], "Art. 278 TFUE.", "no tendrán efecto suspensivo. Sin embargo, el Tribunal podrá, si estima que las circunstancias así lo exigen, ordenar la suspensión"),
 ("TFUE", "Artículo 285", "Tribunal de Cuentas", "Según el artículo 285 del TFUE, el Tribunal de Cuentas estará compuesto por:",
  ["Un nacional de cada Estado miembro.", "Dos nacionales de cada Estado miembro.", "Quince miembros nombrados por el Consejo.", "Un número de miembros fijado por el Parlamento Europeo."], "Art. 285 TFUE.", "El Tribunal de Cuentas estará compuesto por un nacional de cada Estado miembro"),
 ("TFUE", "Artículo 286", "Tribunal de Cuentas", "Según el artículo 286.2 del TFUE, la lista de miembros del Tribunal de Cuentas la adoptará:",
  ["El Consejo, previa consulta al Parlamento Europeo.", "El Parlamento Europeo, previa consulta al Consejo.", "El Consejo Europeo, por mayoría cualificada.", "La Comisión, a propuesta de los Estados miembros."], "Art. 286.2 TFUE.", "El Consejo, previa consulta al Parlamento Europeo, adoptará la lista de miembros"),
 ("TFUE", "Artículo 286", "Tribunal de Cuentas", "Según el artículo 286 del TFUE, los miembros del Tribunal de Cuentas serán nombrados para un período de:",
  ["Seis años, renovable.", "Seis años, no renovable.", "Cinco años, renovable.", "Ocho años, no renovable."], "Art. 286.2 TFUE.", "serán nombrados para un período de seis años"),
 ("TFUE", "Artículo 287", "Tribunal de Cuentas", "Según el artículo 287 del TFUE, el Tribunal de Cuentas aprobará sus informes anuales, informes especiales o dictámenes por:",
  ["Mayoría de los miembros que lo componen.", "Unanimidad.", "Mayoría de dos tercios.", "Mayoría de los miembros presentes."], "Art. 287.4 TFUE.", "por mayoría de los miembros que lo componen"),
 ("TFUE", "Artículo 287", "Tribunal de Cuentas", "Según el artículo 287 del TFUE, la declaración sobre la fiabilidad de las cuentas y la regularidad y legalidad de las operaciones correspondientes la presentará el Tribunal de Cuentas:",
  ["Al Parlamento Europeo y al Consejo.", "Al Consejo Europeo.", "A la Comisión y al Tribunal de Justicia.", "A los Parlamentos nacionales."], "Art. 287.1 TFUE.", "El Tribunal de Cuentas presentará al Parlamento Europeo y al Consejo una declaración sobre la fiabilidad de las cuentas"),
 ("TFUE", "Artículo 282", "BCE", "Según el artículo 282 del TFUE, el Eurosistema lo constituyen:",
  ["El Banco Central Europeo y los bancos centrales nacionales de los Estados miembros cuya moneda es el euro.", "El Banco Central Europeo y los bancos centrales nacionales de todos los Estados miembros.", "Los bancos centrales nacionales de los Estados miembros cuya moneda es el euro, sin el Banco Central Europeo.", "El Banco Central Europeo y el Banco Europeo de Inversiones."], "Art. 282.1 TFUE (el SEBC lo forman el BCE y todos los bancos centrales nacionales).", "El Banco Central Europeo y los bancos centrales nacionales de los Estados miembros cuya moneda es el euro, que constituyen el Eurosistema"),
 ("TFUE", "Artículo 282", "BCE", "Según el artículo 282.2 del TFUE, el objetivo principal del SEBC será:",
  ["Mantener la estabilidad de precios.", "Alcanzar el pleno empleo.", "Garantizar el crecimiento económico.", "Mantener el tipo de cambio del euro."], "Art. 282.2 TFUE.", "El objetivo principal del SEBC será mantener la estabilidad de precios"),
 ("TFUE", "Artículo 283", "BCE", "Según el artículo 283 del TFUE, el mandato de los miembros del Comité Ejecutivo del Banco Central Europeo tendrá una duración de:",
  ["Ocho años y no será renovable.", "Ocho años, renovable una vez.", "Seis años, renovable.", "Cinco años y no será renovable."], "Art. 283.2 TFUE.", "Su mandato tendrá una duración de ocho años y no será renovable"),
 ("TFUE", "Artículo 283", "BCE", "Según el artículo 283 del TFUE, el presidente, el vicepresidente y los demás miembros del Comité Ejecutivo del BCE serán nombrados por:",
  ["El Consejo Europeo, por mayoría cualificada.", "El Consejo, por unanimidad.", "El Parlamento Europeo, a propuesta del Consejo.", "El Consejo de Gobierno del Banco Central Europeo."], "Art. 283.2 TFUE.", "serán nombrados por el Consejo Europeo, por mayoría cualificada"),
]
for k, art, cat, q_, ops, e, fr in Q: T.q(k, art, cat, q_, ops, e, fr)
T.real("L", 22, "Parlamento Europeo"); T.real("L", 23, "TJUE"); T.real("P", 12, "TJUE"); T.real("X", 33, "Parlamento Europeo")

# Flashcards
for q_, a_, cat in [
  ("Funciones del Parlamento Europeo (TUE 14.1)", "Legislativa y presupuestaria, conjuntamente con el Consejo; control político y consultivas; elige al Presidente de la Comisión.", "Parlamento Europeo"),
  ("Composición del Parlamento Europeo (TUE 14.2)", "Máximo 750 más el Presidente; representación decrecientemente proporcional; mínimo 6 y máximo 96 por Estado miembro.", "Parlamento Europeo"),
  ("Mandato de los diputados europeos (TUE 14.3)", "Cinco años; sufragio universal directo, libre y secreto.", "Parlamento Europeo"),
  ("¿Quién elige al Presidente y a la Mesa del Parlamento Europeo?", "El Parlamento Europeo, de entre sus diputados (TUE 14.4); en votación secreta (Reglamento interno, art. 15.1).", "Parlamento Europeo"),
  ("Comisión temporal de investigación (TFUE 226)", "A petición de la cuarta parte de los miembros; termina con la presentación de su informe.", "Parlamento Europeo"),
  ("Defensor del Pueblo Europeo (TFUE 228)", "Lo elige el Parlamento tras cada elección, para toda la legislatura (renovable); lo destituye el Tribunal de Justicia a petición del Parlamento.", "Parlamento Europeo"),
  ("Período de sesiones del Parlamento Europeo (TFUE 229)", "Uno cada año; se reúne sin convocatoria el segundo martes de marzo.", "Parlamento Europeo"),
  ("Moción de censura (TFUE 234)", "Votación pública tras tres días como mínimo; 2/3 de los votos emitidos que sean mayoría de los diputados; dimisión colectiva de la Comisión.", "Parlamento Europeo"),
  ("¿Qué comprende el TJUE? (TUE 19.1)", "El Tribunal de Justicia, el Tribunal General y los tribunales especializados.", "TJUE"),
  ("Nombramiento de jueces y abogados generales (TUE 19.2; TFUE 253)", "De común acuerdo por los Gobiernos de los Estados miembros, por seis años, tras consultar al comité del art. 255; renovación parcial cada tres años.", "TJUE"),
  ("Abogados generales (TFUE 252)", "Ocho en el Tratado; el Consejo, por unanimidad y a petición del Tribunal, puede aumentar su número, y lo elevó a once desde el 7-10-2015 (Decisión 2013/336/UE). Presentan conclusiones motivadas.", "TJUE"),
  ("Comité del art. 255 TFUE", "Siete personalidades (una propuesta por el Parlamento); se pronuncia antes de los nombramientos; normas de funcionamiento y miembros: decisiones del Consejo.", "TJUE"),
  ("Gran Sala y Pleno del Tribunal de Justicia (Estatuto, arts. 16 y 17)", "Gran Sala: 15 jueces (quórum 11), si lo pide un Estado o institución parte. Pleno: quórum 17.", "TJUE"),
  ("Composición del Tribunal General (Estatuto, art. 48)", "Dos jueces por Estado miembro desde el 1 de septiembre de 2019.", "TJUE"),
  ("Legitimados del art. 263, párrafo tercero, TFUE", "Tribunal de Cuentas, Banco Central Europeo y Comité de las Regiones, para salvaguardar sus prerrogativas.", "TJUE"),
  ("Plazos de los recursos de anulación y por omisión", "Anulación: dos meses (263). Omisión: requerimiento previo; dos meses para que la institución actúe y otros dos para recurrir (265).", "TJUE"),
  ("¿Cuándo es obligatoria la cuestión prejudicial? (TFUE 267)", "Cuando el órgano jurisdiccional nacional resuelve sin ulterior recurso judicial de Derecho interno.", "TJUE"),
  ("¿Qué cuestiones prejudiciales conoce el Tribunal General? (Estatuto, art. 50 ter)", "Las comprendidas exclusivamente en: IVA, impuestos especiales, código aduanero, clasificación arancelaria, compensación a pasajeros y comercio de derechos de emisión.", "TJUE"),
  ("Tribunal de Cuentas: composición y nombramiento (TFUE 285 y 286)", "Un nacional por Estado; lista adoptada por el Consejo previa consulta al Parlamento; seis años renovables; Presidente tres años.", "Tribunal de Cuentas"),
  ("Funciones del Tribunal de Cuentas (TFUE 287)", "Examina todos los ingresos y gastos; declaración de fiabilidad al Parlamento y al Consejo; informe anual con las respuestas de las instituciones; informes especiales y dictámenes.", "Tribunal de Cuentas"),
  ("SEBC y Eurosistema (TFUE 282)", "SEBC: BCE + todos los bancos centrales nacionales. Eurosistema: BCE + bancos centrales del euro; dirigen la política monetaria.", "BCE"),
  ("Comité Ejecutivo del BCE (TFUE 283)", "Presidente, vicepresidente y otros cuatro miembros; nombrados por el Consejo Europeo por mayoría cualificada; ocho años no renovables.", "BCE"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Decrecientemente proporcional", "Criterio de reparto de escaños del Parlamento Europeo entre Estados, con un mínimo de seis y un máximo de noventa y seis por Estado (TUE 14.2).", "s1", "Parlamento Europeo")
T.glos("Comisión temporal de investigación", "Comisión del Parlamento Europeo, creada a petición de la cuarta parte de sus miembros, para examinar alegaciones de infracción o mala administración en la aplicación del Derecho de la Unión (TFUE 226).", "s2", "Parlamento Europeo")
T.glos("Defensor del Pueblo Europeo", "Órgano elegido por el Parlamento Europeo que recibe reclamaciones por mala administración de las instituciones, órganos u organismos de la Unión (TFUE 228).", "s2", "Parlamento Europeo")
T.glos("Moción de censura", "Votación del Parlamento Europeo sobre la gestión de la Comisión; aprobada, obliga a sus miembros a dimitir colectivamente (TFUE 234).", "s3", "Parlamento Europeo")
T.glos("Abogado general", "Miembro del Tribunal de Justicia que presenta públicamente, con imparcialidad e independencia, conclusiones motivadas en los asuntos que lo requieran (TFUE 252).", "s4", "TJUE")
T.glos("Gran Sala", "Formación del Tribunal de Justicia de quince jueces, presidida por su Presidente; actúa si lo pide un Estado miembro o una institución parte (Estatuto, art. 16).", "s4", "TJUE")
T.glos("Tribunal General", "Órgano del TJUE que conoce en primera instancia de los recursos de los arts. 263, 265, 268, 270 y 272 TFUE, con casación ante el Tribunal de Justicia (TFUE 256).", "s5", "TJUE")
T.glos("Tribunal especializado", "Tribunal adjunto al Tribunal General, creado por reglamento del Parlamento y del Consejo, para conocer en primera instancia de categorías de recursos en materias específicas (TFUE 257).", "s5", "TJUE")
T.glos("Recurso por incumplimiento", "Recurso de la Comisión o de un Estado miembro contra un Estado que ha incumplido las obligaciones de los Tratados (TFUE 258 y 259).", "s6", "TJUE")
T.glos("Recurso de anulación", "Recurso para controlar la legalidad de los actos de la Unión, en el plazo de dos meses (TFUE 263).", "s7", "TJUE")
T.glos("Recurso por omisión", "Recurso contra la abstención de pronunciarse de una institución, órgano u organismo, previo requerimiento (TFUE 265).", "s7", "TJUE")
T.glos("Cuestión prejudicial", "Petición de un órgano jurisdiccional nacional al TJUE sobre la interpretación de los Tratados o la validez e interpretación de los actos de la Unión (TFUE 267).", "s8", "TJUE")
T.glos("Declaración de fiabilidad", "Declaración del Tribunal de Cuentas al Parlamento Europeo y al Consejo sobre la fiabilidad de las cuentas y la regularidad y legalidad de las operaciones (TFUE 287.1).", "s12", "Tribunal de Cuentas")
T.glos("Eurosistema", "El BCE y los bancos centrales nacionales de los Estados miembros cuya moneda es el euro, que dirigen la política monetaria de la Unión (TFUE 282.1).", "s13", "BCE")
T.glos("Comité Ejecutivo del BCE", "Órgano rector del BCE formado por el presidente, el vicepresidente y otros cuatro miembros, nombrados por el Consejo Europeo por ocho años no renovables (TFUE 283.2).", "s14", "BCE")

# Cronología (fechas de los metadatos del BOE y de EUR-Lex)
T.hito("2007", "Tratado de Lisboa, firmado el 13-12-2007 (título de la LO 1/2008)", "Redacción vigente del TUE (arts. 14 y 19) y del TFUE (arts. 223 a 287)", "normativo", "s1")
T.hito("2008", "Ley Orgánica 1/2008, de 30 de julio, por la que se autoriza la ratificación por España del Tratado de Lisboa (BOE de 31-7-2008)", "Autorización de la ratificación española", "normativo", "s1")
T.hito("2016", "Versiones consolidadas del TUE y del TFUE y Protocolo n.º 3 sobre el Estatuto del TJUE (DO C 202 de 7-6-2016)", "Texto que se cita en estos apuntes", "normativo", "s4")
T.hito("2019", "Reglamento (UE) 2019/629, de 17 de abril de 2019 (DO L 111 de 25-4-2019)", "Sustituye el art. 51 y añade el art. 58 bis del Estatuto del TJUE", "normativo", "s10")
T.hito("2024", "Reglamento (UE, Euratom) 2024/2019, de 11 de abril de 2024 (DO L de 12-8-2024; en vigor el 1-9-2024)", "Cuestiones prejudiciales al Tribunal General en seis materias (art. 50 ter del Estatuto)", "normativo", "s5")
T.hito("2026", "Reglamento interno del Parlamento Europeo, 10.ª legislatura (versión de mayo de 2026)", "Arts. 15 y 16: elección del Presidente", "normativo", "s1")

T.publicar()
