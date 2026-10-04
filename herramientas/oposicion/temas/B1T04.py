# -*- coding: utf-8 -*-
"""Tema I.4 (B1T04): La Corona. Funciones constitucionales del Rey. Sucesión y regencia.
El refrendo.
Método del I.2: mapa → bloques (I a IV) con guía; cada artículo, texto literal del
BOE + ficha de casillas fijas; cierre 1 (preguntas oficiales) y cierre 2 (repaso).
Normas (textos consolidados del BOE): CE, Título II (arts. 56 a 65) y arts. 1.3, 91,
92.2, 99, 115.1 y 168.1; Ley 50/1997, del Gobierno (arts. 2.2 h y 4.1 d); LO 3/2014
(abdicación de Don Juan Carlos I de Borbón)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO["LO3_2014"] = "LO 3/2014"

T = Tema("B1T04",
  "Cuatro preguntas: I. Qué es la Corona y qué posición tiene el Rey (arts. 1.3, 56, 65 y 168 CE) · II. Qué funciones tiene el Rey (arts. 62 y 63, y otros de la Constitución) · III. Quién sucede al Rey y quién lo suple: sucesión, regencia y tutela (arts. 57 a 61 y LO 3/2014) · IV. Quién responde de los actos del Rey: el refrendo (arts. 56.3, 64 y 65.2; Ley 50/1997). Cada artículo: texto literal del BOE y ficha.",
  ["Título II CE", "Monarquía parlamentaria", "Art. 56", "Inviolabilidad", "Art. 62", "Art. 63", "Funciones del Rey", "Art. 57: sucesión", "Príncipe de Asturias", "LO 3/2014", "Regencia", "Tutela del Rey menor", "Juramento", "Refrendo", "Art. 64", "Casa del Rey"])

# =============================================================================
T.ap("s0", "Mapa del tema: cuatro preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque I, tema 4):
> La Corona. Funciones constitucionales del Rey. Sucesión y regencia. El refrendo.

### El hilo conductor

El epígrafe se lee como **cuatro preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Constitución | Otras normas |
|---|---|---|---|
| **I** | ¿Qué es la Corona y qué posición tiene el Rey? | Arts. 1.3, 56, 65 y 168.1 | — |
| **II** | ¿Qué funciones tiene el Rey? | Arts. 62 y 63; 91, 92.2, 99, 115.1 y otros | — |
| **III** | ¿Quién sucede al Rey y quién lo suple? (sucesión, regencia y tutela) | Arts. 57 a 61 | LO 3/2014 (abdicación) |
| **IV** | ¿Quién responde de los actos del Rey? (el refrendo) | Arts. 56.3, 64, 65.2 y 99.5 | Ley 50/1997, del Gobierno, arts. 2.2 h) y 4.1 d) |

!> **La idea que une los cuatro bloques:** España es una **Monarquía parlamentaria** (I): el Rey es el **Jefe del Estado**, pero es **inviolable** y **no está sujeto a responsabilidad**. Por eso sus funciones (II) son las que le atribuyen **expresamente** la Constitución y las leyes; la Corona se transmite por un **orden de sucesión** fijado en la Constitución y, cuando el Rey no puede ejercer, actúa la **Regencia** (III); y sus actos tienen que ir **refrendados**: responde quien refrenda (IV).

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Los esquemas y cuadros **no son texto legal**: resumen los artículos citados.
- Lo que es de otros temas solo se sitúa: Cortes Generales (tema I.5), Gobierno (tema I.6), Poder Judicial (tema I.7), Tribunal Constitucional (tema I.3) y reforma constitucional (tema I.1).
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué es la Corona y qué posición tiene el Rey? (arts. 1.3, 56, 65 y 168.1)", donde(
  "Primera pregunta del tema. Antes de ver qué hace el Rey, hay que saber **qué es la Corona** en la Constitución: la forma política del Estado, la posición del Rey como Jefe del Estado, su estatuto personal y su Casa.",
  ["1 Monarquía parlamentaria y Jefatura del Estado (arts. 1.3 y 56.1 y 2)", "2 Inviolabilidad e irresponsabilidad (art. 56.3)", "3 La Casa del Rey (art. 65)", "4 La protección del Título II: reforma agravada (art. 168.1)"]))

T.ap("s1", "I.1 Monarquía parlamentaria y Jefatura del Estado (arts. 1.3 y 56.1 y 2)", f"""
La Corona es la institución del **Título II** de la Constitución («De la Corona», arts. 56 a 65). Su titular es el Rey.

{unidad("1.1 La forma política del Estado (art. 1.3)",
  lit("CE", "Artículo 1", ["Monarquía parlamentaria"], solo=[3]),
  fichab("Forma política del Estado español",
         "El Estado español; la Jefatura del Estado corresponde al Rey (art. 56.1 → I.1.2)",
         f"Monarquía **parlamentaria**; {c('CE', 'Artículo 1', 'La soberanía nacional reside en el pueblo español')} (art. 1.2)",
         "—",
         f"Es el art. **1.3** (Título preliminar), no el 56. La fórmula exacta es {c('CE', 'Artículo 1', 'Monarquía parlamentaria')}, no «Monarquía constitucional»."))}

{unidad("1.2 El Rey, Jefe del Estado (art. 56.1)",
  lit("CE", "Artículo 56", ["Jefe del Estado", "símbolo de su unidad y permanencia", "arbitra y modera el funcionamiento regular de las instituciones", "la más alta representación del Estado español en las relaciones internacionales", "especialmente con las naciones de su comunidad histórica", "las funciones que le atribuyen expresamente la Constitución y las leyes"], solo=[1]),
  fichab("Posición constitucional del Rey",
         c("CE", "Artículo 56", "El Rey"),
         ["::Cinco rasgos del art. 56.1:", "Jefe del Estado", "Símbolo de su unidad y permanencia", "Arbitra y modera el funcionamiento regular de las instituciones", "Más alta representación del Estado en las relaciones internacionales, especialmente con las naciones de su comunidad histórica", "Ejerce las funciones que le atribuyen **expresamente** la Constitución y las leyes (→ II.1)"],
         "—",
         "Cada verbo tiene su objeto: es **símbolo** de la **unidad y permanencia** del Estado; **arbitra y modera** el **funcionamiento regular de las instituciones** (cayó en 2025, → Cierre 1); **representa** al Estado en las **relaciones internacionales**. Las funciones son solo las atribuidas **expresamente**."))}

{unidad("1.3 El título de Rey de España (art. 56.2)",
  lit("CE", "Artículo 56", ["Rey de España"], solo=[2]),
  fichab("Título del Jefe del Estado",
         "El Rey",
         f"Título: {c('CE', 'Artículo 56', 'Rey de España')}; {c('CE', 'Artículo 56', 'podrá utilizar los demás que correspondan a la Corona')}",
         "—",
         "El título constitucional es **Rey de España**; los demás títulos de la Corona son **potestativos** («podrá utilizar»)."))}
""", 2)

T.ap("s2", "I.2 Inviolabilidad e irresponsabilidad (art. 56.3)", f"""
{unidad("2.1 La persona del Rey (art. 56.3)",
  lit("CE", "Artículo 56", ["inviolable y no está sujeta a responsabilidad", "careciendo de validez sin dicho refrendo", "salvo lo dispuesto en el artículo 65, 2"], solo=[3]),
  fichab("Estatuto personal del Rey",
         c("CE", "Artículo 56", "La persona del Rey"),
         ["Es **inviolable**", "**No está sujeta a responsabilidad**", "Sus actos estarán **siempre refrendados** (art. 64 → IV.1)", "Sin refrendo, **carecen de validez**", "Excepción: art. 65.2 (nombramiento y relevo de los miembros de su Casa → I.3.2)"],
         "—",
         "Inviolabilidad e irresponsabilidad van unidas al **refrendo**: como el Rey no responde, sus actos los refrenda otro, que es quien responde (art. 64.2 → IV.1.2). La única excepción que cita el art. 56.3 es el **65.2**."))}
""", 2)

T.ap("s3", "I.3 La Casa del Rey (art. 65)", f"""
{unidad("3.1 La dotación de la Familia y Casa del Rey (art. 65.1)",
  lit("CE", "Artículo 65", ["de los Presupuestos del Estado una cantidad global", "distribuye libremente"], solo=[1]),
  fichab("Sostenimiento económico de la Familia y Casa del Rey",
         "El Rey (recibe y distribuye); la cantidad figura en los **Presupuestos del Estado**",
         f"{c('CE', 'Artículo 65', 'una cantidad global para el sostenimiento de su Familia y Casa')}",
         "—",
         "Cantidad **global** (no partidas detalladas) y el Rey la **distribuye libremente**."))}

{unidad("3.2 Los miembros de su Casa (art. 65.2)",
  lit("CE", "Artículo 65", ["nombra y releva libremente"], solo=[2]),
  fichab("Nombramiento y relevo del personal de la Casa del Rey",
         c("CE", "Artículo 65", "El Rey"),
         f"{c('CE', 'Artículo 65', 'nombra y releva libremente a los miembros civiles y militares de su Casa')}",
         "—",
         "Es el acto que el art. 56.3 exceptúa del refrendo (→ IV.3). Alcanza a los miembros **civiles y militares** de su Casa."))}
""", 2)

T.ap("s4", "I.4 La protección del Título II: reforma agravada (art. 168.1)", f"""
{unidad("4.1 La reforma que afecte al Título II (art. 168.1)",
  lit("CE", "Artículo 168", ["o al Título II", "mayoría de dos tercios de cada Cámara", "disolución inmediata de las Cortes"], solo=[1]),
  fichab("Procedimiento agravado de reforma para el Título II",
         "Las Cortes Generales (cada Cámara)",
         "Aprobación del principio, disolución inmediata de las Cortes, ratificación por las nuevas Cámaras y referéndum (art. 168.2 y 3; tema I.1)",
         f"{c('CE', 'Artículo 168', 'mayoría de dos tercios de cada Cámara')}",
         "El Título II («De la Corona») está protegido como el Título preliminar y la Sección 1.ª del Capítulo segundo del Título I: su reforma va por el **art. 168**, no por el 167."))}

{resumen([
  "La forma política del Estado es la **Monarquía parlamentaria** (art. **1.3**).",
  "El Rey es **Jefe del Estado**, **símbolo** de su unidad y permanencia, **arbitra y modera** el funcionamiento regular de las instituciones y ejerce las funciones que le atribuyen **expresamente** la Constitución y las leyes (56.1).",
  "Su persona es **inviolable** y **no está sujeta a responsabilidad**; sus actos, siempre **refrendados**, salvo el **65.2** (56.3).",
  "Recibe una **cantidad global** de los Presupuestos y **nombra y releva libremente** a los miembros de su Casa (65).",
  "Reformar el Título II exige el procedimiento del **art. 168** (dos tercios de cada Cámara, disolución y referéndum)."],
  "Siguiente: II. ¿Qué funciones tiene el Rey?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Qué funciones tiene el Rey? (arts. 62 y 63, y otros de la Constitución)", donde(
  "Segunda pregunta. El art. 56.1 dice que el Rey ejerce las funciones que le atribuyen **expresamente** la Constitución y las leyes. La lista básica está en los arts. **62** (funciones internas) y **63** (relaciones internacionales); otras están repartidas por la Constitución.",
  ["1 Las funciones del art. 62", "2 Las funciones internacionales (art. 63)", "3 Otras funciones en la Constitución (arts. 91, 92.2, 99 y 115.1)", "4 Cuadro de las funciones del Rey y nombramientos de otros órganos"]))

T.ap("s5", "II.1 Las funciones del art. 62", f"""
El art. 62 enumera diez funciones, de la a) a la j). Para memorizarlas, se agrupan aquí por su destinatario (la agrupación **no es** del texto legal).

{unidad("1.1 Cortes, leyes, elecciones y referéndum (art. 62 a, b y c)",
  lit("CE", "Artículo 62", ["Sancionar y promulgar las leyes", "Convocar y disolver las Cortes Generales y convocar elecciones", "Convocar a referéndum"], solo=[1, 2, 3, 4]),
  fichab("Funciones del Rey respecto de las Cortes Generales y del cuerpo electoral",
         c("CE", "Artículo 62", "Corresponde al Rey"),
         ["a) Sancionar y promulgar las leyes (plazo: art. 91 → II.3.1)", "b) Convocar y disolver las Cortes y convocar elecciones, en los términos previstos en la Constitución", "c) Convocar a referéndum en los casos previstos en la Constitución (art. 92.2 → II.3.2)"],
         "—",
         "Las tres funciones se ejercen **en los términos** o **en los casos previstos en la Constitución**: el Rey no decide cuándo disolver ni cuándo convocar referéndum (→ II.3)."))}

{unidad("1.2 El Gobierno (art. 62 d, e, f y g)",
  lit("CE", "Artículo 62", ["Proponer el candidato a Presidente del Gobierno", "a propuesta de su Presidente", "Expedir los decretos acordados en el Consejo de Ministros", "Ser informado de los asuntos de Estado y presidir, a estos efectos, las sesiones del Consejo de Ministros, cuando lo estime oportuno, a petición del Presidente del Gobierno"], solo=[1, 5, 6, 7, 8]),
  fichab("Funciones del Rey respecto del Gobierno",
         "El Rey; en las letras e) y g) interviene el **Presidente del Gobierno** (propuesta o petición)",
         ["d) Proponer el candidato a Presidente del Gobierno, nombrarlo y poner fin a sus funciones, en los términos de la Constitución (art. 99 → II.3.3)", "e) Nombrar y separar a los miembros del Gobierno, **a propuesta de su Presidente**", "f) Expedir los decretos del Consejo de Ministros, conferir los empleos civiles y militares y conceder honores y distinciones con arreglo a las leyes", "g) Ser informado de los asuntos de Estado y presidir el Consejo de Ministros a estos efectos"],
         "—",
         "En la letra g), el Rey preside **el Consejo de Ministros** (no las Cortes), solo **a estos efectos** (ser informado), **cuando lo estime oportuno** y **a petición del Presidente del Gobierno**. Cayó en 2025 como distractor (→ Cierre 1)."))}

{unidad("1.3 Fuerzas Armadas, derecho de gracia y Reales Academias (art. 62 h, i y j)",
  lit("CE", "Artículo 62", ["El mando supremo de las Fuerzas Armadas", "que no podrá autorizar indultos generales", "El Alto Patronazgo de las Reales Academias"], solo=[1, 9, 10, 11]),
  fichab("Otras funciones del art. 62",
         c("CE", "Artículo 62", "Corresponde al Rey"),
         ["h) El **mando supremo** de las Fuerzas Armadas", "i) El derecho de gracia **con arreglo a la ley**, que **no podrá autorizar indultos generales**", "j) El **Alto Patronazgo** de las **Reales Academias**"],
         "—",
         "Cruces típicos de distractores: «Alto Patronazgo de las **Fuerzas Armadas**» (es el **mando supremo**); «**autorizar** indultos generales» (la ley **no podrá** autorizarlos). Cayó en 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s6", "II.2 Las funciones internacionales (art. 63)", f"""
Desarrollan la «más alta representación del Estado español en las relaciones internacionales» del art. 56.1 (→ I.1.2).

{unidad("2.1 Los representantes diplomáticos (art. 63.1)",
  lit("CE", "Artículo 63", ["acredita a los embajadores y otros representantes diplomáticos", "están acreditados ante él"], solo=[1]),
  fichab("Acreditación de los representantes diplomáticos",
         c("CE", "Artículo 63", "El Rey"),
         ["Acredita a los embajadores y otros representantes diplomáticos de España", "Los representantes extranjeros en España están acreditados **ante él**"],
         "—",
         "Doble dirección: el Rey **acredita** a los españoles y los extranjeros se **acreditan ante él**."))}

{unidad("2.2 Los tratados (art. 63.2)",
  lit("CE", "Artículo 63", ["manifestar el consentimiento del Estado para obligarse internacionalmente por medio de tratados"], solo=[2]),
  fichab("Manifestación del consentimiento del Estado en los tratados",
         "El Rey",
         f"{c('CE', 'Artículo 63', 'de conformidad con la Constitución y las leyes')} (la autorización de las Cortes en ciertos tratados es del tema I.5)",
         "—",
         "El Rey **manifiesta** el consentimiento; no negocia ni autoriza los tratados."))}

{unidad("2.3 Guerra y paz (art. 63.3)",
  lit("CE", "Artículo 63", ["previa autorización de las Cortes Generales, declarar la guerra y hacer la paz"], solo=[3]),
  fichab("Declaración de guerra y conclusión de la paz",
         "El Rey, con **autorización previa de las Cortes Generales**",
         "Declara la guerra y hace la paz",
         c("CE", "Artículo 63", "previa autorización de las Cortes Generales"),
         "La autorización es **previa** y de las **Cortes Generales** (no del Gobierno ni solo del Congreso)."))}
""", 2)

T.ap("s7", "II.3 Otras funciones en la Constitución (arts. 91, 92.2, 99 y 115.1)", f"""
Las letras a) a d) del art. 62 remiten a otros artículos («en los términos previstos en la Constitución»). Aquí solo se ve **qué hace el Rey**; el procedimiento completo es de los temas I.5 y I.6.

{unidad("3.1 Sanción y promulgación de las leyes (art. 91)",
  lit("CE", "Artículo 91", ["en el plazo de quince días"]),
  fichab("Sanción, promulgación y orden de publicación de las leyes",
         c("CE", "Artículo 91", "El Rey"),
         f"{c('CE', 'Artículo 91', 'sancionará')}, {c('CE', 'Artículo 91', 'promulgará')} y {c('CE', 'Artículo 91', 'ordenará su inmediata publicación')}",
         f"Sanción: {c('CE', 'Artículo 91', 'en el plazo de quince días')}",
         "**Quince** días para sancionar; publicación **inmediata**. Desarrolla el art. 62 a)."))}

{unidad("3.2 Convocatoria del referéndum consultivo (art. 92.2)",
  lit("CE", "Artículo 92", ["convocado por el Rey, mediante propuesta del Presidente del Gobierno, previamente autorizada por el Congreso de los Diputados"], solo=[2]),
  fichab("Convocatoria del referéndum consultivo",
         "El Rey convoca; propone el **Presidente del Gobierno**; autoriza el **Congreso de los Diputados**",
         "Propuesta del Presidente del Gobierno → autorización previa del Congreso → convocatoria del Rey",
         "—",
         "Autoriza el **Congreso** (no las Cortes Generales ni el Senado) y propone el **Presidente del Gobierno** (no el Consejo de Ministros)."))}

{unidad("3.3 Propuesta, nombramiento del Presidente del Gobierno y disolución del art. 99 (art. 99.1, 3 y 5)",
  lit("CE", "Artículo 99", ["previa consulta con los representantes designados por los Grupos políticos con representación parlamentaria", "a través del Presidente del Congreso", "el Rey le nombrará Presidente", "el Rey disolverá ambas Cámaras y convocará nuevas elecciones con el refrendo del Presidente del Congreso"], solo=[1, 3, 5]),
  fichab("Intervención del Rey en la investidura del Presidente del Gobierno",
         "El Rey; a través del **Presidente del Congreso**",
         ["Propone candidato **previa consulta** con los representantes designados por los Grupos políticos con representación parlamentaria (99.1)", "Nombra Presidente al candidato que obtiene la confianza del Congreso (99.3)", "Si en **dos meses** desde la primera votación nadie obtiene la confianza, disuelve ambas Cámaras y convoca elecciones (99.5)"],
         f"Disolución del 99.5: {c('CE', 'Artículo 99', 'transcurrido el plazo de dos meses, a partir de la primera votación de investidura')}",
         "Consulta a los **representantes designados por los Grupos políticos con representación parlamentaria** (cayó en 2025, → Cierre 1). La disolución del 99.5 la refrenda el **Presidente del Congreso** (→ IV.1.1). La investidura es del tema I.6."))}

{unidad("3.4 La disolución a propuesta del Presidente del Gobierno (art. 115.1)",
  lit("CE", "Artículo 115", ["que será decretada por el Rey"], solo=[1]),
  fichab("Disolución anticipada de las Cámaras",
         "Propone el **Presidente del Gobierno** (previa deliberación del Consejo de Ministros y bajo su exclusiva responsabilidad); decreta el **Rey**",
         f"{c('CE', 'Artículo 115', 'El decreto de disolución fijará la fecha de las elecciones')}",
         "—",
         "El Rey **decreta** la disolución, pero la **propone** el Presidente del Gobierno, que asume la responsabilidad. Es el contenido del art. 62 b)."))}
""", 2)

T.ap("s8", "II.4 Cuadro de las funciones del Rey y nombramientos de otros órganos (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Ámbito | Función | Artículo | Quién propone o autoriza |
|---|---|---|---|
| Cortes y leyes | Sancionar y promulgar las leyes (15 días) | 62 a); 91 | — |
| Cortes y elecciones | Convocar y disolver las Cortes; convocar elecciones | 62 b); 99.5; 115.1 | Presidente del Gobierno (115.1) |
| Referéndum | Convocar a referéndum | 62 c); 92.2 | Presidente del Gobierno, con autorización previa del Congreso |
| Gobierno | Proponer candidato y nombrar Presidente | 62 d); 99 | Consulta a los representantes de los Grupos políticos con representación parlamentaria |
| Gobierno | Nombrar y separar a los miembros del Gobierno | 62 e); 100 | Presidente del Gobierno |
| Gobierno | Expedir decretos del Consejo de Ministros; empleos civiles y militares; honores | 62 f) | — |
| Gobierno | Ser informado; presidir el Consejo de Ministros a estos efectos | 62 g) | A petición del Presidente del Gobierno |
| Defensa | Mando supremo de las Fuerzas Armadas | 62 h) | — |
| Justicia | Derecho de gracia con arreglo a la ley (sin indultos generales) | 62 i) | — |
| Cultura | Alto Patronazgo de las Reales Academias | 62 j) | — |
| Exterior | Acreditar diplomáticos; manifestar el consentimiento en los tratados | 63.1 y 2 | — |
| Exterior | Declarar la guerra y hacer la paz | 63.3 | Autorización previa de las Cortes Generales |

**Nombramientos de otros órganos que la Constitución atribuye al Rey** (los procedimientos son de otros temas):

| Órgano | Cita literal | Tema |
|---|---|---|
| Miembros del Gobierno | {c("CE", "Artículo 100", "serán nombrados y separados por el Rey, a propuesta de su Presidente")} (art. 100) | I.6 |
| Vocales del CGPJ | {c("CE", "Artículo 122", "veinte miembros nombrados por el Rey por un período de cinco años")} (art. 122.3) | I.7 |
| Presidente del Tribunal Supremo | {c("CE", "Artículo 123", "será nombrado por el Rey, a propuesta del Consejo General del Poder Judicial")} (art. 123.2) | I.7 |
| Fiscal General del Estado | {c("CE", "Artículo 124", "será nombrado por el Rey, a propuesta del Gobierno, oído el Consejo General del Poder Judicial")} (art. 124.4) | I.7 |
| Presidente de Comunidad Autónoma (art. 152.1) | {c("CE", "Artículo 152", "elegido por la Asamblea, de entre sus miembros, y nombrado por el Rey")} | I.10 |
| Magistrados del Tribunal Constitucional | {c("CE", "Artículo 159", "12 miembros nombrados por el Rey")} (art. 159.1) | I.3 |
| Presidente del Tribunal Constitucional | {c("CE", "Artículo 160", "será nombrado entre sus miembros por el Rey, a propuesta del mismo Tribunal en pleno")} (art. 160) | I.3 |

Además, la justicia {c("CE", "Artículo 117", "se administra en nombre del Rey")} (art. 117.1).

{resumen([
  "El Rey ejerce las funciones que le atribuyen **expresamente** la Constitución y las leyes (56.1): las del **art. 62** (a-j) y del **63**.",
  "62 g): preside el **Consejo de Ministros** solo **a efectos de ser informado**, cuando lo estime oportuno, **a petición del Presidente del Gobierno**.",
  "62 h) **mando supremo** de las FF. AA.; 62 i) derecho de gracia **sin indultos generales**; 62 j) **Alto Patronazgo de las Reales Academias**.",
  "63: acredita diplomáticos, manifiesta el consentimiento en los tratados y declara la guerra y hace la paz **previa autorización de las Cortes**.",
  "Sanciona en **15 días** (91); convoca el referéndum a propuesta del **Presidente del Gobierno** autorizada por el **Congreso** (92.2); propone candidato **previa consulta** a los representantes de los Grupos políticos (99.1)."],
  "Siguiente: III. ¿Quién sucede al Rey y quién lo suple? Sucesión y regencia")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Quién sucede al Rey y quién lo suple? Sucesión, regencia y tutela (arts. 57 a 61; LO 3/2014)", donde(
  "Tercera pregunta. La Corona es **hereditaria**: la Constitución fija el **orden de sucesión** y qué pasa si se agotan las líneas, si hay abdicación o dudas. Si el Rey es **menor de edad** o queda **inhabilitado**, ejerce sus funciones la **Regencia**; el Rey menor tiene además un **tutor**. Todos juran ante las Cortes.",
  ["1 La sucesión en la Corona (art. 57 y LO 3/2014)", "2 El consorte (art. 58)", "3 La Regencia (art. 59)", "4 La tutela del Rey menor (art. 60)", "5 El juramento (art. 61)", "6 Cuadro: Regencia y tutela"]))

T.ap("s9", "III.1 La sucesión en la Corona (art. 57 y LO 3/2014)", f"""
{unidad("1.1 El orden de sucesión (art. 57.1)",
  lit("CE", "Artículo 57", ["hereditaria en los sucesores de S. M. Don Juan Carlos I de Borbón", "primogenitura y representación", "la línea anterior a las posteriores", "el grado más próximo al más remoto", "el varón a la mujer", "la persona de más edad a la de menos"], solo=[1]),
  fichab("Transmisión hereditaria de la Corona",
         f"{c('CE', 'Artículo 57', 'los sucesores de S. M. Don Juan Carlos I de Borbón, legítimo heredero de la dinastía histórica')}",
         ["::Orden regular de **primogenitura y representación**:", "1.º Línea: la **anterior** a las posteriores", "2.º En la misma línea: el **grado más próximo** al más remoto", "3.º En el mismo grado: el **varón** a la mujer", "4.º En el mismo sexo: la persona de **más edad** a la de menos"],
         "—",
         "Cuatro criterios en cascada y **cada uno con su ámbito**: línea → grado → sexo → edad. El distractor típico cambia el ámbito («en el mismo **grado**, la persona de más edad»). Cayó en 2025 (→ Cierre 1)."))}

{unidad("1.2 El Príncipe heredero (art. 57.2)",
  lit("CE", "Artículo 57", ["desde su nacimiento o desde que se produzca el hecho que origine el llamamiento", "Príncipe de Asturias"], solo=[2]),
  fichab("Dignidad y títulos del sucesor",
         c("CE", "Artículo 57", "El Príncipe heredero"),
         f"Tendrá {c('CE', 'Artículo 57', 'la dignidad de Príncipe de Asturias y los demás títulos vinculados tradicionalmente al sucesor de la Corona de España')}",
         "Desde su **nacimiento** o desde el **hecho que origine el llamamiento**",
         "La dignidad es la de **Príncipe de Asturias**; se adquiere desde el nacimiento **o** desde el llamamiento (no desde la mayoría de edad, que es el momento del **juramento**, → III.5.1)."))}

{unidad("1.3 Extinción de las líneas y matrimonio prohibido (art. 57.3 y 4)",
  lit("CE", "Artículo 57", ["las Cortes Generales proveerán a la sucesión en la Corona", "contra la expresa prohibición del Rey y de las Cortes Generales", "por sí y sus descendientes"], solo=[3, 4]),
  fichab("Supuestos excepcionales de la sucesión",
         "Las **Cortes Generales** (proveen la sucesión; prohíben el matrimonio junto con el Rey)",
         ["Extinguidas todas las líneas llamadas en Derecho: las Cortes proveen a la sucesión en la forma que más convenga a los intereses de España (57.3)", "Matrimonio contra la expresa prohibición del Rey **y** de las Cortes: exclusión de la sucesión **por sí y sus descendientes** (57.4)"],
         "—",
         "La prohibición tiene que ser **expresa** y **del Rey y de las Cortes Generales** (los dos). La exclusión alcanza también a los **descendientes**."))}

{unidad("1.4 Abdicaciones, renuncias y dudas: ley orgánica (art. 57.5)",
  lit("CE", "Artículo 57", ["se resolverán por una ley orgánica"], solo=[5]),
  fichab("Instrumento para resolver abdicaciones, renuncias y dudas sucesorias",
         "Las Cortes Generales, mediante **ley orgánica**",
         ["Abdicaciones y renuncias", "Cualquier duda de **hecho o de derecho** en el orden de sucesión"],
         "Ley orgánica: mayoría absoluta del Congreso en una votación final sobre el conjunto del proyecto (art. 81.2; tema I.5)",
         "Ley **orgánica** (no ordinaria, ni real decreto, ni acuerdo de las Cortes). Aplicación: la LO 3/2014 (→ III.1.5)."))}

{unidad("1.5 La abdicación de Don Juan Carlos I (LO 3/2014, artículo único)",
  lit("LO3_2014", "aunico", ["abdica la Corona de España", "en el momento de entrada en vigor de la presente ley orgánica"], titulo="Artículo único. Abdicación de Su Majestad el Rey Don Juan Carlos I de Borbón (LO 3/2014, de 18 de junio)"),
  lit("LO3_2014", "dfunica", ["en el momento de su publicación"], titulo="Disposición final única. Entrada en vigor (LO 3/2014)"),
  fichab("Ley orgánica que hace efectiva una abdicación (aplicación del art. 57.5)",
         "Las Cortes Generales, por **ley orgánica**",
         "La abdicación se hace efectiva con la entrada en vigor de la ley, que se produce con su publicación en el BOE",
         "Ley Orgánica 3/2014, de 18 de junio (BOE de 19-6-2014)",
         f"La abdicación es efectiva {c('LO3_2014', 'aunico', 'en el momento de entrada en vigor de la presente ley orgánica')}, y la ley entra en vigor {c('LO3_2014', 'dfunica', 'en el momento de su publicación')}: no hay *vacatio legis*."))}
""", 2)

T.ap("s10", "III.2 El consorte (art. 58)", f"""
{unidad("2.1 La Reina consorte o el consorte de la Reina (art. 58)",
  lit("CE", "Artículo 58", ["no podrán asumir funciones constitucionales", "salvo lo dispuesto para la Regencia"]),
  fichab("Posición constitucional del consorte",
         c("CE", "Artículo 58", "La Reina consorte o el consorte de la Reina"),
         "No puede asumir funciones constitucionales",
         "—",
         "La única excepción es la **Regencia**: el padre o la madre del Rey menor la ejercen (art. 59.1 → III.3.1)."))}
""", 2)

T.ap("s11", "III.3 La Regencia (art. 59)", f"""
La Regencia ejerce las funciones del Rey cuando este no puede hacerlo. La Constitución prevé dos supuestos (minoría de edad e inhabilitación) y una Regencia electiva subsidiaria.

{unidad("3.1 Regencia por minoría de edad del Rey (art. 59.1)",
  lit("CE", "Artículo 59", ["el padre o la madre del Rey", "el pariente mayor de edad más próximo a suceder en la Corona", "inmediatamente", "durante el tiempo de la minoría de edad del Rey"], solo=[1]),
  fichab("Regencia legítima por minoría de edad",
         ["1.º El padre o la madre del Rey", "2.º En su defecto, el pariente mayor de edad más próximo a suceder en la Corona, según el orden de la Constitución"],
         f"{c('CE', 'Artículo 59', 'entrará a ejercer inmediatamente la Regencia')}",
         f"Durante {c('CE', 'Artículo 59', 'el tiempo de la minoría de edad del Rey')}",
         "Es **inmediata** (no la nombran las Cortes). Llama primero al **padre o la madre**; después, al **pariente** mayor de edad **más próximo a suceder**."))}

{unidad("3.2 Regencia por inhabilitación del Rey (art. 59.2)",
  lit("CE", "Artículo 59", ["la imposibilidad fuere reconocida por las Cortes Generales", "el Príncipe heredero de la Corona, si fuere mayor de edad", "hasta que el Príncipe heredero alcance la mayoría de edad"], solo=[2]),
  fichab("Regencia por inhabilitación",
         ["1.º El **Príncipe heredero**, si es mayor de edad", "2.º Si no lo es: como en la minoría de edad (59.1), hasta que el Príncipe alcance la mayoría de edad"],
         f"Requisito: {c('CE', 'Artículo 59', 'la imposibilidad fuere reconocida por las Cortes Generales')}; después, la Regencia es inmediata",
         "—",
         "La inhabilitación la **reconocen las Cortes Generales**. Aquí el primer llamado es el **Príncipe heredero** (no el padre o la madre del Rey)."))}

{unidad("3.3 Regencia electiva (art. 59.3)",
  lit("CE", "Artículo 59", ["será nombrada por las Cortes Generales", "una, tres o cinco personas"], solo=[3]),
  fichab("Regencia nombrada por las Cortes",
         "Las **Cortes Generales** la nombran",
         f"Solo {c('CE', 'Artículo 59', 'Si no hubiere ninguna persona a quien corresponda la Regencia')}",
         f"Composición: {c('CE', 'Artículo 59', 'una, tres o cinco personas')}",
         "**Una, tres o cinco** personas (número impar; nunca dos ni cuatro). Solo cuando no hay regente por los apartados 1 y 2."))}

{unidad("3.4 Requisitos y naturaleza de la Regencia (art. 59.4 y 5)",
  lit("CE", "Artículo 59", ["ser español y mayor de edad", "por mandato constitucional y siempre en nombre del Rey"], solo=[4, 5]),
  fichab("Condiciones para ser Regente y título por el que se ejerce",
         "El Regente o los Regentes",
         [f"Requisitos: {c('CE', 'Artículo 59', 'ser español y mayor de edad')}", f"Se ejerce {c('CE', 'Artículo 59', 'por mandato constitucional y siempre en nombre del Rey')}"],
         "—",
         "Para la Regencia basta ser **español** y **mayor de edad**; para el **tutor** testamentario se exige ser **español de nacimiento** (→ III.4.1). La Regencia actúa **en nombre del Rey**."))}
""", 2)

T.ap("s12", "III.4 La tutela del Rey menor (art. 60)", f"""
{unidad("4.1 Quién es tutor y compatibilidades (art. 60)",
  lit("CE", "Artículo 60", ["la persona que en su testamento hubiese nombrado el Rey difunto", "mayor de edad y español de nacimiento", "el padre o la madre mientras permanezcan viudos", "lo nombrarán las Cortes Generales", "sino en el padre, madre o ascendientes directos del Rey", "incompatible con el de todo cargo o representación política"]),
  fichab("Tutela del Rey menor de edad",
         ["1.º La persona nombrada en su **testamento** por el Rey difunto (mayor de edad y **español de nacimiento**)", "2.º Si no la nombró: el **padre o la madre** mientras permanezcan **viudos**", "3.º En su defecto: la nombran las **Cortes Generales**"],
         ["Regente y tutor solo pueden acumularse en el **padre, madre o ascendientes directos** del Rey", "La tutela es **incompatible** con todo cargo o representación política (60.2)"],
         "—",
         "El tutor testamentario tiene que ser español **de nacimiento** (más que el Regente). El padre o la madre solo **mientras permanezcan viudos**. El tutor **no presta** el juramento del art. 61 (cayó en 2025, → Cierre 1)."))}
""", 2)

T.ap("s13", "III.5 El juramento (art. 61)", f"""
{unidad("5.1 Quién jura y qué jura (art. 61)",
  lit("CE", "Artículo 61", ["al ser proclamado ante las Cortes Generales", "desempeñar fielmente sus funciones, guardar y hacer guardar la Constitución y las leyes y respetar los derechos de los ciudadanos y de las Comunidades Autónomas", "al alcanzar la mayoría de edad", "al hacerse cargo de sus funciones", "así como el de fidelidad al Rey"]),
  fichab("Juramento constitucional",
         ["El **Rey**, al ser proclamado ante las Cortes Generales (61.1)", "El **Príncipe heredero**, al alcanzar la mayoría de edad (61.2)", "El **Regente o Regentes**, al hacerse cargo de sus funciones (61.2)"],
         ["Contenido: desempeñar fielmente sus funciones, guardar y hacer guardar la Constitución y las leyes y respetar los derechos de los ciudadanos y de las Comunidades Autónomas", "Príncipe heredero y Regentes: además, el de **fidelidad al Rey**"],
         "—",
         "Juran **tres**: Rey, Príncipe heredero y Regente o Regentes. **No** jura el tutor. El juramento de **fidelidad al Rey** es solo del Príncipe y de los Regentes."))}
""", 2)

T.ap("s14", "III.6 Cuadro: Regencia y tutela (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| | Regencia (art. 59) | Tutela del Rey menor (art. 60) |
|---|---|---|
| Qué hace | Ejerce las funciones del Rey, **en su nombre** | Cuida del Rey menor |
| Cuándo | Minoría de edad o inhabilitación reconocida por las Cortes | Minoría de edad |
| Primer llamado | Minoría: padre o madre del Rey. Inhabilitación: Príncipe heredero mayor de edad | La persona nombrada en el testamento del Rey difunto |
| Después | Pariente mayor de edad más próximo a suceder | Padre o madre mientras permanezcan viudos |
| Subsidiario | Las Cortes nombran una Regencia de una, tres o cinco personas | Las Cortes nombran tutor |
| Requisitos | Español y mayor de edad | Testamentario: mayor de edad y español **de nacimiento** |
| Incompatibilidad | — | Todo cargo o representación política |
| Juramento (art. 61) | Sí, también de fidelidad al Rey | No |

!> **Acumulación:** Regente y tutor solo pueden ser la misma persona si es el **padre, madre o ascendiente directo** del Rey (art. 60.1).

{resumen([
  "Sucesión: primogenitura y representación; **línea** anterior → **grado** más próximo → **varón** → **más edad**, cada uno dentro del anterior (57.1).",
  "El heredero es **Príncipe de Asturias** desde su nacimiento o el llamamiento (57.2); extinguidas las líneas, proveen las **Cortes** (57.3); el matrimonio prohibido por el Rey **y** las Cortes excluye por sí y sus descendientes (57.4).",
  "Abdicaciones, renuncias y dudas: **ley orgánica** (57.5); aplicada en la **LO 3/2014**.",
  "El consorte no asume funciones constitucionales, salvo la **Regencia** (58).",
  "Regencia: minoría (padre o madre → pariente más próximo) o inhabilitación reconocida por las Cortes (Príncipe heredero mayor de edad); si no hay nadie, las Cortes nombran **una, tres o cinco** personas; español y mayor de edad; **en nombre del Rey** (59).",
  "Tutor: testamentario (español **de nacimiento**) → padre o madre viudos → Cortes; incompatible con cargo político (60). Juran el Rey, el Príncipe y los Regentes, no el tutor (61)."],
  "Siguiente: IV. ¿Quién responde de los actos del Rey? El refrendo")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Quién responde de los actos del Rey? El refrendo (arts. 56.3, 64 y 65.2; Ley 50/1997)", donde(
  "Cuarta pregunta. El Rey es inviolable y no está sujeto a responsabilidad (→ I.2). Para que sus actos sean válidos tienen que ir **refrendados**, y **responde quien refrenda**. Hay que saber **quién** refrenda cada acto y **qué** actos no necesitan refrendo.",
  ["1 Quién refrenda y quién responde (art. 64)", "2 Los refrendantes en la Ley del Gobierno (Ley 50/1997, arts. 2.2 h y 4.1 d)", "3 Cuadro: quién refrenda qué y actos sin refrendo"]))

T.ap("s15", "IV.1 Quién refrenda y quién responde (art. 64)", f"""
{unidad("1.1 Los refrendantes (art. 64.1)",
  lit("CE", "Artículo 64", ["por el Presidente del Gobierno y, en su caso, por los Ministros competentes", "serán refrendados por el Presidente del Congreso"], solo=[1]),
  fichab("Refrendo de los actos del Rey",
         ["Regla general: el **Presidente del Gobierno** y, en su caso, los **Ministros competentes**", "Excepción: el **Presidente del Congreso**, para la propuesta y el nombramiento del Presidente del Gobierno y la disolución del art. 99"],
         f"Exigencia general: los actos del Rey {c('CE', 'Artículo 56', 'estarán siempre refrendados en la forma establecida en el artículo 64')} (art. 56.3 → I.2.1)",
         "—",
         "Los tres actos que refrenda el **Presidente del Congreso**: **propuesta** del candidato, **nombramiento** del Presidente del Gobierno y **disolución del art. 99** (99.5). La disolución anticipada del art. 115 no está entre ellos."))}

{unidad("1.2 La responsabilidad del refrendante (art. 64.2)",
  lit("CE", "Artículo 64", ["serán responsables las personas que los refrenden"], solo=[2]),
  fichab("Efecto del refrendo: traslado de la responsabilidad",
         "Las personas que refrendan",
         "Responden de los actos del Rey que refrendan",
         "—",
         "Es la otra cara del art. 56.3: el Rey **no está sujeto a responsabilidad**; responde **quien refrenda**."))}
""", 2)

T.ap("s16", "IV.2 Los refrendantes en la Ley 50/1997, del Gobierno (arts. 2.2 h y 4.1 d)", f"""
{unidad("2.1 El Presidente del Gobierno (Ley 50/1997, art. 2.2 h)",
  lit("LGOB", "a2", ["Refrendar, en su caso, los actos del Rey"], solo=[2, 10]),
  fichab("Atribución de refrendo al Presidente del Gobierno",
         "El **Presidente del Gobierno**",
         f"{c('LGOB', 'a2', 'Refrendar, en su caso, los actos del Rey y someterle, para su sanción, las leyes y demás normas con rango de ley')}",
         "—",
         "La Ley del Gobierno remite a los **arts. 64 y 91** de la Constitución: refrendo y sometimiento de las leyes a la sanción del Rey."))}

{unidad("2.2 Los Ministros (Ley 50/1997, art. 4.1 d)",
  lit("LGOB", "a4", ["en materia de su competencia"], solo=[1, 5]),
  fichab("Atribución de refrendo a los Ministros",
         "Los **Ministros**",
         f"{c('LGOB', 'a4', 'Refrendar, en su caso, los actos del Rey en materia de su competencia')}",
         "—",
         "Refrendan solo **en materia de su competencia** (en la Constitución: «los Ministros **competentes**», art. 64.1)."))}
""", 2)

T.ap("s17", "IV.3 Cuadro: quién refrenda qué y actos sin refrendo (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Acto del Rey | Quién refrenda | Base |
|---|---|---|
| Regla general | Presidente del Gobierno y, en su caso, Ministros competentes | CE 64.1; Ley 50/1997, arts. 2.2 h) y 4.1 d) |
| Propuesta de candidato a Presidente del Gobierno | Presidente del Congreso | CE 64.1 y 99.1 |
| Nombramiento del Presidente del Gobierno | Presidente del Congreso | CE 64.1 y 99.3 |
| Disolución de ambas Cámaras del art. 99.5 | Presidente del Congreso | CE 64.1 y 99.5 |
| Nombramiento y relevo de los miembros civiles y militares de su Casa | **Sin refrendo** | CE 56.3 y 65.2 |

!> **Sin refrendo, sin validez:** los actos del Rey {c("CE", "Artículo 56", "careciendo de validez sin dicho refrendo")}, y la única excepción que nombra el art. 56.3 es el art. 65.2.

{resumen([
  "Los actos del Rey van **siempre refrendados**; sin refrendo **carecen de validez** (56.3).",
  "Refrendan el **Presidente del Gobierno** y, en su caso, los **Ministros competentes** (64.1; Ley 50/1997, arts. 2.2 h y 4.1 d).",
  "El **Presidente del Congreso** refrenda la **propuesta** y el **nombramiento** del Presidente del Gobierno y la **disolución del art. 99** (64.1).",
  "De los actos del Rey **responden quienes los refrendan** (64.2).",
  "Excepción expresa: el nombramiento y relevo **libre** de los miembros de su **Casa** (65.2)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_L5 = examen("L", 5, {
  "a": f"Lo contrario de la letra i): el derecho de gracia se ejerce con arreglo a la ley, {c('CE', 'Artículo 62', 'que no podrá autorizar indultos generales')}.",
  "b": f"Mezcla la letra g): el Rey preside {c('CE', 'Artículo 62', 'las sesiones del Consejo de Ministros')} (no las de las Cortes Generales), y solo a efectos de ser informado.",
  "c": f"Cambia el objeto: el Alto Patronazgo es {c('CE', 'Artículo 62', 'de las Reales Academias')} (letra j); de las Fuerzas Armadas tiene {c('CE', 'Artículo 62', 'El mando supremo')} (letra h).",
  "d": f"Literal de la letra i): {c('CE', 'Artículo 62', 'Ejercer el derecho de gracia con arreglo a la ley, que no podrá autorizar indultos generales')}."},
  [("Ejercer el derecho de gracia con arreglo a la ley", "CE", "Artículo 62", "Ejercer el derecho de gracia con arreglo a la ley, que no podrá autorizar indultos generales")])
EX_L6 = examen("L", 6, {
  "a": f"Las relaciones internacionales aparecen en el art. 56.1, pero el Rey {c('CE', 'Artículo 56', 'asume la más alta representación del Estado español en las relaciones internacionales')}: las representa, no las arbitra.",
  "b": f"Literal del art. 56.1: {c('CE', 'Artículo 56', 'arbitra y modera el funcionamiento regular de las instituciones')}.",
  "c": f"De la unidad y permanencia del Estado el Rey es {c('CE', 'Artículo 56', 'símbolo de su unidad y permanencia')}; no las arbitra ni modera.",
  "d": f"Las naciones de su comunidad histórica se citan en la representación internacional: {c('CE', 'Artículo 56', 'especialmente con las naciones de su comunidad histórica')}."},
  [("funcionamiento regular de las instituciones", "CE", "Artículo 56", "arbitra y modera el funcionamiento regular de las instituciones")])
EX_X10 = examen("X", 10, {
  "a": f"Cambia «línea» por «grado»: lo que se prefiere siempre es {c('CE', 'Artículo 57', 'la línea anterior a las posteriores')}; en la misma línea, {c('CE', 'Artículo 57', 'el grado más próximo al más remoto')}.",
  "b": f"Cambia el ámbito: el varón se prefiere a la mujer {c('CE', 'Artículo 57', 'en el mismo grado, el varón a la mujer')}; en la misma línea se prefiere el grado más próximo.",
  "c": f"Literal del art. 57.1: {c('CE', 'Artículo 57', 'en el mismo sexo, la persona de más edad a la de menos')}.",
  "d": f"Cambia el ámbito: en el mismo grado se prefiere {c('CE', 'Artículo 57', 'el varón a la mujer')}; la edad decide solo {c('CE', 'Artículo 57', 'en el mismo sexo')}."},
  [("En el mismo sexo, la persona de más edad a la de menos", "CE", "Artículo 57", "en el mismo sexo, la persona de más edad a la de menos")])
EX_X11 = examen("X", 11, {
  "a": f"Correcta según el art. 61.2 (por eso no es la que se pide): {c('CE', 'Artículo 61', 'el Regente o Regentes al hacerse cargo de sus funciones, prestarán el mismo juramento, así como el de fidelidad al Rey')}.",
  "b": f"Correcta según el art. 61.1 (no es la que se pide): {c('CE', 'Artículo 61', 'El Rey, al ser proclamado ante las Cortes Generales, prestará juramento')}.",
  "c": f"Correcta según el art. 61.2 (no es la que se pide): {c('CE', 'Artículo 61', 'El Príncipe heredero, al alcanzar la mayoría de edad')} presta el mismo juramento y el de fidelidad al Rey.",
  "d": f"Es la INCORRECTA: la persona nombrada en el testamento del Rey difunto es el **tutor** del Rey menor ({c('CE', 'Artículo 60', 'Será tutor del Rey menor la persona que en su testamento hubiese nombrado el Rey difunto')}, art. 60.1), y el art. 61 no le exige juramento."},
  [("en su testamento hubiese nombrado", "CE", "Artículo 60", "la persona que en su testamento hubiese nombrado el Rey difunto")])
EX_L4 = examen("L", 4, {
  "a": f"El art. 99.1 exige consulta: {c('CE', 'Artículo 99', 'previa consulta con los representantes designados por los Grupos políticos con representación parlamentaria')}.",
  "b": "Cambia a quién se consulta: no son los Grupos Parlamentarios del Congreso y el Senado, sino los representantes designados por los Grupos **políticos** con representación parlamentaria.",
  "c": f"Literal del art. 99.1: {c('CE', 'Artículo 99', 'previa consulta con los representantes designados por los Grupos políticos con representación parlamentaria')}.",
  "d": f"El Presidente del Congreso no propone: el Rey propone {c('CE', 'Artículo 99', 'a través del Presidente del Congreso')}, que además refrenda la propuesta (art. 64.1)."},
  [("representantes designados por los grupos políticos con representación parlamentaria", "CE", "Artículo 99", "representantes designados por los Grupos políticos con representación parlamentaria")])

T.ap("s18", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **cuatro** preguntas de este tema (dos en el turno libre y dos en el extraordinario) y **una** relacionada (la propuesta del candidato a Presidente del Gobierno, art. 99, del tema I.6). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-L 2025, pregunta 6 · El Rey arbitra y modera (→ I.1.2)", EX_L6,
  "### GACE-X 2025, pregunta 10 · Orden de sucesión (→ III.1.1)", EX_X10,
  "### GACE-X 2025, pregunta 11 · Quién presta juramento (→ III.5.1)", EX_X11,
  "### GACE-L 2025, pregunta 5 · Funciones del art. 62 (→ II.1.3)", EX_L5,
  "### GACE-L 2025, pregunta 4 · Propuesta del candidato a Presidente del Gobierno (relacionada; → II.3.3)", EX_L4,
  "### Cómo se pregunta",
  "!> Las preguntas de la Corona copian **un artículo literal** y cambian una pieza: el **objeto** de un verbo (arbitra y modera **el funcionamiento regular de las instituciones**), el **ámbito** de un criterio sucesorio (**en el mismo sexo**, la edad), el **órgano** (Consejo de Ministros, no Cortes; Reales Academias, no Fuerzas Armadas) o mezclan figuras próximas (**tutor** y Regente).",
]))

T.ap("s19", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. La Corona y el Rey | Monarquía parlamentaria (1.3); Jefe del Estado (56.1); inviolable y no responsable (56.3); Casa del Rey (65); reforma por el 168 | **Arbitra y modera el funcionamiento regular de las instituciones** |
| II. Funciones | Art. 62 a) a j); art. 63; 91, 92.2, 99, 115.1 | **Derecho de gracia sin indultos generales**; Alto Patronazgo de las **Reales Academias**; mando supremo de las FF. AA. |
| III. Sucesión y regencia | Orden del 57.1; Príncipe de Asturias; ley orgánica para abdicaciones (LO 3/2014); Regencia (59); tutela (60); juramento (61) | Línea → grado → **varón** (mismo grado) → **edad** (mismo sexo); juran Rey, Príncipe y Regentes, **no el tutor** |
| IV. Refrendo | Presidente del Gobierno y Ministros competentes; Presidente del Congreso en el art. 99; responden los refrendantes | Sin refrendo **no hay validez**; excepción: **65.2** |

?> **Trampas frecuentes:** «el Rey preside las sesiones de **las Cortes**» (preside el **Consejo de Ministros**, a efectos de ser informado); «Alto Patronazgo de las **Fuerzas Armadas**» (de las **Reales Academias**); «**en el mismo grado**, la persona de más edad» (en el mismo grado, el **varón**; la edad, **en el mismo sexo**); «el **tutor** presta juramento» (no lo presta); «la Regencia electiva tiene **dos o cuatro** miembros» (**una, tres o cinco**); «el tutor testamentario basta con que sea **español**» (español **de nacimiento**); «abdicación por **ley ordinaria**» (**ley orgánica**, 57.5); «la disolución del **art. 115** la refrenda el Presidente del Congreso» (solo la del **art. 99**).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
T.q("CE", "Artículo 1", "La Corona", "Según el artículo 1.3 de la Constitución, la forma política del Estado español es:",
    ["La Monarquía parlamentaria.", "La Monarquía constitucional.", "La Monarquía hereditaria y constitucional.", "El Estado social y democrático de Derecho."],
    "Art. 1.3 CE: «La forma política del Estado español es la Monarquía parlamentaria». El Estado social y democrático de Derecho es el art. 1.1.", "La forma política del Estado español es la Monarquía parlamentaria")
T.q("CE", "Artículo 56", "La Corona", "Según el artículo 56.1 de la Constitución, el Rey es el Jefe del Estado y símbolo de:",
    ["Su unidad y permanencia.", "Su soberanía e independencia.", "Su integridad territorial y su ordenamiento constitucional.", "La unidad de la Nación y la autonomía de sus nacionalidades."],
    "Art. 56.1 CE: «símbolo de su unidad y permanencia».", "símbolo de su unidad y permanencia")
T.q("CE", "Artículo 56", "La Corona", "Según el artículo 56.1 de la Constitución, el Rey asume la más alta representación del Estado español en las relaciones internacionales, especialmente con:",
    ["Las naciones de su comunidad histórica.", "Los Estados miembros de la Unión Europea.", "Los países de habla hispana.", "Las organizaciones internacionales de las que España es parte."],
    "Art. 56.1 CE.", "especialmente con las naciones de su comunidad histórica")
T.q("CE", "Artículo 56", "La Corona", "Según el artículo 56.1 de la Constitución, el Rey ejerce las funciones que le atribuyen:",
    ["Expresamente la Constitución y las leyes.", "La Constitución, las leyes y la costumbre.", "Las Cortes Generales mediante ley orgánica.", "El Gobierno mediante real decreto."],
    "Art. 56.1 CE: «las funciones que le atribuyen expresamente la Constitución y las leyes».", "ejerce las funciones que le atribuyen expresamente la Constitución y las leyes")
T.q("CE", "Artículo 56", "La Corona", "Según el artículo 56.2 de la Constitución, el título del Rey es el de:",
    ["Rey de España, y podrá utilizar los demás que correspondan a la Corona.", "Rey de los españoles, sin otros títulos.", "Rey de España, sin que pueda utilizar otros títulos.", "Jefe del Estado y Rey de España, y deberá utilizar todos los que correspondan a la Corona."],
    "Art. 56.2 CE: los demás títulos son potestativos («podrá utilizar»).", "Su título es el de Rey de España y podrá utilizar los demás que correspondan a la Corona")
T.q("CE", "Artículo 56", "Refrendo", "Según el artículo 56.3 de la Constitución, los actos del Rey no refrendados:",
    ["Carecen de validez, salvo lo dispuesto en el artículo 65.2.", "Son válidos, pero el Rey responde de ellos.", "Son anulables a instancia del Gobierno.", "Carecen de validez en todo caso, sin excepción."],
    "Art. 56.3 CE: «careciendo de validez sin dicho refrendo, salvo lo dispuesto en el artículo 65, 2».", "careciendo de validez sin dicho refrendo, salvo lo dispuesto en el artículo 65, 2")
T.q("CE", "Artículo 56", "La Corona", "Según el artículo 56.3 de la Constitución, la persona del Rey:",
    ["Es inviolable y no está sujeta a responsabilidad.", "Es inviolable, pero responde ante las Cortes Generales.", "Está sujeta a responsabilidad penal ante el Tribunal Supremo.", "Es irresponsable solo durante el ejercicio de sus funciones."],
    "Art. 56.3 CE.", "La persona del Rey es inviolable y no está sujeta a responsabilidad")
T.q("CE", "Artículo 65", "La Corona", "Según el artículo 65.1 de la Constitución, el Rey recibe de los Presupuestos del Estado para el sostenimiento de su Familia y Casa:",
    ["Una cantidad global, que distribuye libremente.", "Una cantidad global, cuya distribución aprueban las Cortes.", "Partidas específicas fijadas por el Gobierno.", "Una asignación anual que distribuye el Ministerio de Hacienda."],
    "Art. 65.1 CE.", "una cantidad global para el sostenimiento de su Familia y Casa, y distribuye libremente la misma")
T.q("CE", "Artículo 65", "La Corona", "Según el artículo 65.2 de la Constitución, los miembros civiles y militares de la Casa del Rey:",
    ["Los nombra y releva libremente el Rey.", "Los nombra el Rey a propuesta del Gobierno.", "Los nombra el Presidente del Gobierno, con el refrendo del Rey.", "Los nombra el Rey, con el refrendo del Ministro de la Presidencia."],
    "Art. 65.2 CE; es la excepción al refrendo del art. 56.3.", "El Rey nombra y releva libremente a los miembros civiles y militares de su Casa")
T.q("CE", "Artículo 168", "La Corona", "Según el artículo 168.1 de la Constitución, una reforma parcial que afecte al Título II (De la Corona) exige la aprobación del principio por:",
    ["Mayoría de dos tercios de cada Cámara, y la disolución inmediata de las Cortes.", "Mayoría de tres quintos de cada Cámara.", "Mayoría absoluta del Congreso y del Senado.", "Mayoría de dos tercios del Congreso, sin disolución de las Cortes."],
    "Art. 168.1 CE.", "se procederá a la aprobación del principio por mayoría de dos tercios de cada Cámara, y a la disolución inmediata de las Cortes")
T.q("CE", "Artículo 62", "Funciones del Rey", "Según el artículo 62 de la Constitución, corresponde al Rey:",
    ["El mando supremo de las Fuerzas Armadas.", "El Alto Patronazgo de las Fuerzas Armadas.", "La dirección de la defensa del Estado.", "La jefatura del Estado Mayor de la Defensa."],
    "Art. 62 h) CE. La defensa del Estado la dirige el Gobierno: «El Gobierno dirige la política interior y exterior, la Administración civil y militar y la defensa del Estado» (art. 97, tema I.6).", "El mando supremo de las Fuerzas Armadas")
T.q("CE", "Artículo 62", "Funciones del Rey", "Según el artículo 62 j) de la Constitución, corresponde al Rey el Alto Patronazgo de:",
    ["Las Reales Academias.", "Las Fuerzas Armadas.", "Las Universidades públicas.", "El Patrimonio Nacional."],
    "Art. 62 j) CE.", "El Alto Patronazgo de las Reales Academias")
T.q("CE", "Artículo 62", "Funciones del Rey", "Según el artículo 62 i) de la Constitución, el Rey ejerce el derecho de gracia:",
    ["Con arreglo a la ley, que no podrá autorizar indultos generales.", "Con arreglo a la ley, que podrá autorizar indultos generales.", "Libremente, sin necesidad de refrendo.", "A propuesta del Consejo General del Poder Judicial."],
    "Art. 62 i) CE.", "Ejercer el derecho de gracia con arreglo a la ley, que no podrá autorizar indultos generales")
T.q("CE", "Artículo 62", "Funciones del Rey", "Según el artículo 62 g) de la Constitución, el Rey preside, a efectos de ser informado de los asuntos de Estado, las sesiones del Consejo de Ministros:",
    ["Cuando lo estime oportuno, a petición del Presidente del Gobierno.", "Siempre que lo estime oportuno, sin necesidad de petición.", "Una vez al mes, a petición del Consejo de Ministros.", "Cuando lo acuerden las Cortes Generales."],
    "Art. 62 g) CE.", "presidir, a estos efectos, las sesiones del Consejo de Ministros, cuando lo estime oportuno, a petición del Presidente del Gobierno")
T.q("CE", "Artículo 62", "Funciones del Rey", "Según el artículo 62 e) de la Constitución, el Rey nombra y separa a los miembros del Gobierno:",
    ["A propuesta de su Presidente.", "A propuesta del Congreso de los Diputados.", "Libremente, oído el Presidente del Gobierno.", "A propuesta del Consejo de Ministros."],
    "Art. 62 e) CE (y art. 100).", "Nombrar y separar a los miembros del Gobierno, a propuesta de su Presidente")
T.q("CE", "Artículo 62", "Funciones del Rey", "Según el artículo 62 f) de la Constitución, corresponde al Rey:",
    ["Expedir los decretos acordados en el Consejo de Ministros.", "Aprobar los reglamentos de las Cámaras.", "Dictar decretos-leyes en caso de urgencia.", "Aprobar los Presupuestos Generales del Estado."],
    "Art. 62 f) CE.", "Expedir los decretos acordados en el Consejo de Ministros")
T.q("CE", "Artículo 63", "Funciones del Rey", "Según el artículo 63.3 de la Constitución, al Rey corresponde declarar la guerra y hacer la paz:",
    ["Previa autorización de las Cortes Generales.", "Previa autorización del Congreso de los Diputados.", "A propuesta del Consejo de Defensa Nacional.", "Previo dictamen del Consejo de Estado."],
    "Art. 63.3 CE.", "Al Rey corresponde, previa autorización de las Cortes Generales, declarar la guerra y hacer la paz")
T.q("CE", "Artículo 63", "Funciones del Rey", "Según el artículo 63.2 de la Constitución, al Rey corresponde:",
    ["Manifestar el consentimiento del Estado para obligarse internacionalmente por medio de tratados.", "Negociar y firmar los tratados internacionales en nombre del Gobierno.", "Autorizar la celebración de los tratados internacionales.", "Denunciar los tratados por decisión propia."],
    "Art. 63.2 CE: de conformidad con la Constitución y las leyes.", "Al Rey corresponde manifestar el consentimiento del Estado para obligarse internacionalmente por medio de tratados")
T.q("CE", "Artículo 63", "Funciones del Rey", "Según el artículo 63.1 de la Constitución, los representantes extranjeros en España están acreditados:",
    ["Ante el Rey.", "Ante el Ministro de Asuntos Exteriores.", "Ante el Presidente del Gobierno.", "Ante las Cortes Generales."],
    "Art. 63.1 CE.", "Los representantes extranjeros en España están acreditados ante él")
T.q("CE", "Artículo 91", "Funciones del Rey", "Según el artículo 91 de la Constitución, el Rey sancionará las leyes aprobadas por las Cortes Generales en el plazo de:",
    ["Quince días.", "Diez días.", "Un mes.", "Treinta días."], "Art. 91 CE.", "El Rey sancionará en el plazo de quince días")
T.q("CE", "Artículo 92", "Funciones del Rey", "Según el artículo 92.2 de la Constitución, el referéndum consultivo será convocado por el Rey:",
    ["Mediante propuesta del Presidente del Gobierno, previamente autorizada por el Congreso de los Diputados.", "Mediante propuesta del Consejo de Ministros, previamente autorizada por las Cortes Generales.", "A propuesta del Congreso de los Diputados, por mayoría absoluta.", "Mediante propuesta del Presidente del Gobierno, previamente autorizada por el Senado."],
    "Art. 92.2 CE.", "será convocado por el Rey, mediante propuesta del Presidente del Gobierno, previamente autorizada por el Congreso de los Diputados")
T.q("CE", "Artículo 115", "Funciones del Rey", "Según el artículo 115.1 de la Constitución, la disolución del Congreso, del Senado o de las Cortes Generales la propone el Presidente del Gobierno y:",
    ["Será decretada por el Rey.", "Será acordada por el Consejo de Ministros.", "Será autorizada por el Congreso de los Diputados.", "Será refrendada por el Presidente del Congreso."],
    "Art. 115.1 CE.", "que será decretada por el Rey")
T.q("CE", "Artículo 57", "Sucesión", "Según el artículo 57.1 de la Constitución, en la sucesión en el trono, en la misma línea se prefiere:",
    ["El grado más próximo al más remoto.", "El varón a la mujer.", "La persona de más edad a la de menos.", "La línea anterior a las posteriores."],
    "Art. 57.1 CE: línea anterior → en la misma línea, grado más próximo → en el mismo grado, varón → en el mismo sexo, más edad.", "en la misma línea, el grado más próximo al más remoto")
T.q("CE", "Artículo 57", "Sucesión", "Según el artículo 57.1 de la Constitución, en la sucesión en el trono, en el mismo grado se prefiere:",
    ["El varón a la mujer.", "La persona de más edad a la de menos.", "El grado más próximo al más remoto.", "La persona que designe el Rey."],
    "Art. 57.1 CE.", "en el mismo grado, el varón a la mujer")
T.q("CE", "Artículo 57", "Sucesión", "Según el artículo 57.2 de la Constitución, el Príncipe heredero tendrá la dignidad de Príncipe de Asturias:",
    ["Desde su nacimiento o desde que se produzca el hecho que origine el llamamiento.", "Desde que alcance la mayoría de edad.", "Desde que preste juramento ante las Cortes Generales.", "Desde que lo proclamen las Cortes Generales."],
    "Art. 57.2 CE.", "desde su nacimiento o desde que se produzca el hecho que origine el llamamiento")
T.q("CE", "Artículo 57", "Sucesión", "Según el artículo 57.3 de la Constitución, extinguidas todas las líneas llamadas en Derecho, proveerán a la sucesión en la Corona:",
    ["Las Cortes Generales.", "El Gobierno.", "El Congreso de los Diputados.", "El pueblo español mediante referéndum."],
    "Art. 57.3 CE.", "Extinguidas todas las líneas llamadas en Derecho, las Cortes Generales proveerán a la sucesión en la Corona")
T.q("CE", "Artículo 57", "Sucesión", "Según el artículo 57.4 de la Constitución, quedarán excluidas en la sucesión a la Corona, por sí y sus descendientes, las personas con derecho a la sucesión que contrajeren matrimonio:",
    ["Contra la expresa prohibición del Rey y de las Cortes Generales.", "Contra la expresa prohibición del Rey o del Gobierno.", "Sin autorización previa del Consejo de Ministros.", "Contra la expresa prohibición de las Cortes Generales, aunque el Rey lo consienta."],
    "Art. 57.4 CE: la prohibición es del Rey y de las Cortes Generales.", "contrajeren matrimonio contra la expresa prohibición del Rey y de las Cortes Generales")
T.q("CE", "Artículo 57", "Sucesión", "Según el artículo 57.5 de la Constitución, las abdicaciones y renuncias y cualquier duda de hecho o de derecho en el orden de sucesión a la Corona se resolverán por:",
    ["Una ley orgánica.", "Una ley ordinaria.", "Un real decreto acordado en Consejo de Ministros.", "Acuerdo de las Cortes Generales en sesión conjunta."],
    "Art. 57.5 CE (aplicado en la LO 3/2014).", "se resolverán por una ley orgánica")
T.q("LO3_2014", "aunico", "Sucesión", "Según el artículo único de la Ley Orgánica 3/2014, de 18 de junio, la abdicación de Su Majestad el Rey Don Juan Carlos I de Borbón será efectiva:",
    ["En el momento de entrada en vigor de la ley orgánica.", "A los veinte días de la publicación de la ley orgánica.", "En el momento de la proclamación del nuevo Rey ante las Cortes Generales.", "En el momento en que el Rey comunique su voluntad al Presidente del Gobierno."],
    "Art. único.2 LO 3/2014; según su disposición final única, entró en vigor en el momento de su publicación en el BOE.", "La abdicación será efectiva en el momento de entrada en vigor de la presente ley orgánica")
T.q("CE", "Artículo 58", "Regencia", "Según el artículo 58 de la Constitución, la Reina consorte o el consorte de la Reina:",
    ["No podrán asumir funciones constitucionales, salvo lo dispuesto para la Regencia.", "Podrán asumir funciones constitucionales por delegación del Rey.", "No podrán asumir funciones constitucionales en ningún caso.", "Ejercerán la tutela del Rey menor en todo caso."],
    "Art. 58 CE.", "no podrán asumir funciones constitucionales, salvo lo dispuesto para la Regencia")
T.q("CE", "Artículo 59", "Regencia", "Según el artículo 59.1 de la Constitución, cuando el Rey fuere menor de edad, entrará a ejercer inmediatamente la Regencia:",
    ["El padre o la madre del Rey y, en su defecto, el pariente mayor de edad más próximo a suceder en la Corona.", "La persona que hubiese nombrado el Rey difunto en su testamento.", "El Príncipe heredero, si fuere mayor de edad.", "La persona que nombren las Cortes Generales."],
    "Art. 59.1 CE. El Príncipe heredero es el primer llamado en la inhabilitación (59.2).", "el padre o la madre del Rey y, en su defecto, el pariente mayor de edad más próximo a suceder en la Corona")
T.q("CE", "Artículo 59", "Regencia", "Según el artículo 59.2 de la Constitución, si el Rey se inhabilitare para el ejercicio de su autoridad, la imposibilidad debe ser reconocida por:",
    ["Las Cortes Generales.", "El Tribunal Constitucional.", "El Gobierno, previo dictamen del Consejo de Estado.", "El Congreso de los Diputados por mayoría absoluta."],
    "Art. 59.2 CE.", "la imposibilidad fuere reconocida por las Cortes Generales")
T.q("CE", "Artículo 59", "Regencia", "Según el artículo 59.3 de la Constitución, si no hubiere ninguna persona a quien corresponda la Regencia, ésta será nombrada por las Cortes Generales y se compondrá de:",
    ["Una, tres o cinco personas.", "Dos o cuatro personas.", "Tres personas.", "Entre una y siete personas."],
    "Art. 59.3 CE.", "se compondrá de una, tres o cinco personas")
T.q("CE", "Artículo 59", "Regencia", "Según el artículo 59.4 de la Constitución, para ejercer la Regencia es preciso:",
    ["Ser español y mayor de edad.", "Ser español de nacimiento y mayor de edad.", "Ser miembro de la Familia Real.", "Ser mayor de cuarenta años."],
    "Art. 59.4 CE. Al tutor testamentario se le exige ser «español de nacimiento» (art. 60.1).", "Para ejercer la Regencia es preciso ser español y mayor de edad")
T.q("CE", "Artículo 59", "Regencia", "Según el artículo 59.5 de la Constitución, la Regencia se ejercerá:",
    ["Por mandato constitucional y siempre en nombre del Rey.", "Por delegación de las Cortes Generales y en nombre propio.", "Por mandato del Rey y en su nombre.", "Por mandato constitucional y en nombre de las Cortes Generales."],
    "Art. 59.5 CE.", "La Regencia se ejercerá por mandato constitucional y siempre en nombre del Rey")
T.q("CE", "Artículo 60", "Tutela", "Según el artículo 60.1 de la Constitución, el tutor del Rey menor nombrado en su testamento por el Rey difunto debe ser:",
    ["Mayor de edad y español de nacimiento.", "Mayor de edad y español.", "Pariente del Rey en línea directa.", "Miembro de las Cortes Generales."],
    "Art. 60.1 CE.", "siempre que sea mayor de edad y español de nacimiento")
T.q("CE", "Artículo 60", "Tutela", "Según el artículo 60.1 de la Constitución, si el Rey difunto no hubiese nombrado tutor en su testamento, será tutor:",
    ["El padre o la madre mientras permanezcan viudos.", "El Regente, en todo caso.", "El pariente mayor de edad más próximo a suceder en la Corona.", "El Presidente del Gobierno."],
    "Art. 60.1 CE; en su defecto, lo nombran las Cortes Generales.", "si no lo hubiese nombrado, será tutor el padre o la madre mientras permanezcan viudos")
T.q("CE", "Artículo 60", "Tutela", "Según el artículo 60.1 de la Constitución, los cargos de Regente y de tutor solo podrán acumularse en:",
    ["El padre, madre o ascendientes directos del Rey.", "El Príncipe heredero.", "Cualquier pariente mayor de edad del Rey.", "La persona nombrada por las Cortes Generales."],
    "Art. 60.1 CE.", "no podrán acumularse los cargos de Regente y de tutor sino en el padre, madre o ascendientes directos del Rey")
T.q("CE", "Artículo 60", "Tutela", "Según el artículo 60.2 de la Constitución, el ejercicio de la tutela del Rey menor es incompatible con:",
    ["Todo cargo o representación política.", "El ejercicio de la Regencia en todo caso.", "Cualquier actividad profesional o mercantil.", "La condición de miembro de la Familia Real."],
    "Art. 60.2 CE. La Regencia sí puede acumularse en el padre, madre o ascendientes directos (60.1).", "El ejercicio de la tutela es también incompatible con el de todo cargo o representación política")
T.q("CE", "Artículo 61", "Sucesión", "Según el artículo 61.2 de la Constitución, el Príncipe heredero presta juramento:",
    ["Al alcanzar la mayoría de edad.", "Al ser proclamado ante las Cortes Generales.", "Al nacer o producirse el llamamiento.", "Al hacerse cargo de la Regencia, en todo caso."],
    "Art. 61.2 CE; el Rey jura al ser proclamado ante las Cortes Generales (61.1).", "El Príncipe heredero, al alcanzar la mayoría de edad")
T.q("CE", "Artículo 61", "Sucesión", "Según el artículo 61 de la Constitución, además del juramento común, prestan el de fidelidad al Rey:",
    ["El Príncipe heredero y el Regente o Regentes.", "El Príncipe heredero y el tutor del Rey menor.", "El Presidente del Gobierno y los Ministros.", "Solo el Regente o Regentes."],
    "Art. 61.2 CE.", "prestarán el mismo juramento, así como el de fidelidad al Rey")
T.q("CE", "Artículo 64", "Refrendo", "Según el artículo 64.1 de la Constitución, los actos del Rey serán refrendados, como regla general, por:",
    ["El Presidente del Gobierno y, en su caso, por los Ministros competentes.", "El Presidente del Congreso.", "El Consejo de Ministros en pleno.", "El Ministro de Justicia, en todo caso."],
    "Art. 64.1 CE.", "Los actos del Rey serán refrendados por el Presidente del Gobierno y, en su caso, por los Ministros competentes")
T.q("CE", "Artículo 64", "Refrendo", "Según el artículo 64.1 de la Constitución, la propuesta y el nombramiento del Presidente del Gobierno, y la disolución prevista en el artículo 99, serán refrendados por:",
    ["El Presidente del Congreso.", "El Presidente del Gobierno saliente.", "El Presidente del Senado.", "El Ministro de la Presidencia."],
    "Art. 64.1 CE.", "La propuesta y el nombramiento del Presidente del Gobierno, y la disolución prevista en el artículo 99, serán refrendados por el Presidente del Congreso")
T.q("CE", "Artículo 64", "Refrendo", "Según el artículo 64.2 de la Constitución, de los actos del Rey serán responsables:",
    ["Las personas que los refrenden.", "El Rey y las personas que los refrenden, solidariamente.", "El Gobierno en su conjunto, ante el Senado.", "Las Cortes Generales."],
    "Art. 64.2 CE.", "De los actos del Rey serán responsables las personas que los refrenden")
T.q("LGOB", "a4", "Refrendo", "Según el artículo 4.1 d) de la Ley 50/1997, del Gobierno, corresponde a los Ministros:",
    ["Refrendar, en su caso, los actos del Rey en materia de su competencia.", "Refrendar todos los actos del Rey.", "Proponer al Rey la disolución de las Cortes Generales.", "Someter al Rey, para su sanción, las leyes aprobadas por las Cortes."],
    "Art. 4.1 d) Ley 50/1997. Someter las leyes a la sanción y proponer la disolución corresponden al Presidente del Gobierno (art. 2.2 c y h).", "Refrendar, en su caso, los actos del Rey en materia de su competencia")
T.real("L", 6, "La Corona"); T.real("L", 5, "Funciones del Rey"); T.real("X", 10, "Sucesión"); T.real("X", 11, "Sucesión")

# Flashcards
for q_, a_, cat in [
  ("Forma política del Estado español (art. 1.3)", "La Monarquía parlamentaria.", "La Corona"),
  ("Cinco rasgos del Rey en el art. 56.1", "Jefe del Estado; símbolo de su unidad y permanencia; arbitra y modera el funcionamiento regular de las instituciones; más alta representación en las relaciones internacionales (especialmente con las naciones de su comunidad histórica); ejerce las funciones que le atribuyen expresamente la Constitución y las leyes.", "La Corona"),
  ("Estatuto personal del Rey (art. 56.3)", "Inviolable y no sujeto a responsabilidad; sus actos, siempre refrendados (sin refrendo carecen de validez), salvo el art. 65.2.", "La Corona"),
  ("Casa del Rey (art. 65)", "Cantidad global de los Presupuestos del Estado que distribuye libremente; nombra y releva libremente a los miembros civiles y militares de su Casa.", "La Corona"),
  ("¿Por qué procedimiento se reforma el Título II?", "Art. 168: aprobación del principio por dos tercios de cada Cámara, disolución inmediata, ratificación y referéndum.", "La Corona"),
  ("Art. 62 g): presidencia del Consejo de Ministros", "Para ser informado de los asuntos de Estado, cuando lo estime oportuno, a petición del Presidente del Gobierno.", "Funciones del Rey"),
  ("Art. 62 h), i) y j)", "Mando supremo de las Fuerzas Armadas; derecho de gracia con arreglo a la ley, que no podrá autorizar indultos generales; Alto Patronazgo de las Reales Academias.", "Funciones del Rey"),
  ("Funciones internacionales del Rey (art. 63)", "Acredita a los diplomáticos (y los extranjeros se acreditan ante él); manifiesta el consentimiento del Estado en los tratados; declara la guerra y hace la paz, previa autorización de las Cortes Generales.", "Funciones del Rey"),
  ("Referéndum consultivo (art. 92.2)", "Lo convoca el Rey, mediante propuesta del Presidente del Gobierno, previamente autorizada por el Congreso de los Diputados.", "Funciones del Rey"),
  ("¿A quién consulta el Rey antes de proponer candidato a Presidente del Gobierno? (art. 99.1)", "A los representantes designados por los Grupos políticos con representación parlamentaria; propone a través del Presidente del Congreso.", "Funciones del Rey"),
  ("Orden de sucesión (art. 57.1)", "Primogenitura y representación: línea anterior; en la misma línea, grado más próximo; en el mismo grado, varón; en el mismo sexo, más edad.", "Sucesión"),
  ("¿Desde cuándo es Príncipe de Asturias el heredero? (art. 57.2)", "Desde su nacimiento o desde que se produzca el hecho que origine el llamamiento.", "Sucesión"),
  ("Matrimonio prohibido (art. 57.4)", "Contra la expresa prohibición del Rey y de las Cortes Generales: exclusión de la sucesión por sí y sus descendientes.", "Sucesión"),
  ("Abdicaciones, renuncias y dudas sucesorias (art. 57.5)", "Se resuelven por ley orgánica (p. ej., LO 3/2014, abdicación de Don Juan Carlos I).", "Sucesión"),
  ("Regencia por minoría de edad (art. 59.1)", "Padre o madre del Rey; en su defecto, el pariente mayor de edad más próximo a suceder. Inmediata, durante la minoría.", "Regencia"),
  ("Regencia por inhabilitación (art. 59.2)", "Reconocida la imposibilidad por las Cortes Generales: el Príncipe heredero si es mayor de edad; si no, como en la minoría, hasta su mayoría de edad.", "Regencia"),
  ("Regencia nombrada por las Cortes (art. 59.3)", "Si no hay nadie a quien corresponda; una, tres o cinco personas.", "Regencia"),
  ("Requisitos y naturaleza de la Regencia (art. 59.4 y 5)", "Español y mayor de edad; por mandato constitucional y siempre en nombre del Rey.", "Regencia"),
  ("Tutor del Rey menor (art. 60)", "El nombrado en el testamento del Rey difunto (mayor de edad y español de nacimiento); si no, el padre o la madre mientras permanezcan viudos; en su defecto, lo nombran las Cortes. Incompatible con cargo o representación política.", "Tutela"),
  ("¿Quiénes prestan juramento? (art. 61)", "El Rey al ser proclamado ante las Cortes; el Príncipe heredero al alcanzar la mayoría de edad y el Regente o Regentes al hacerse cargo (estos dos, además, el de fidelidad al Rey). No el tutor.", "Sucesión"),
  ("¿Quién refrenda los actos del Rey? (art. 64.1)", "El Presidente del Gobierno y, en su caso, los Ministros competentes; la propuesta y nombramiento del Presidente del Gobierno y la disolución del art. 99, el Presidente del Congreso.", "Refrendo"),
  ("¿Quién responde de los actos del Rey? (art. 64.2)", "Las personas que los refrenden.", "Refrendo"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Monarquía parlamentaria", "Forma política del Estado español según el art. 1.3 de la Constitución.", "s1", "La Corona")
T.glos("Jefe del Estado", "Condición del Rey según el art. 56.1, que añade que es símbolo de la unidad y permanencia del Estado y arbitra y modera el funcionamiento regular de las instituciones.", "s1", "La Corona")
T.glos("Inviolabilidad", "Cualidad de la persona del Rey, que además no está sujeta a responsabilidad (art. 56.3).", "s2", "La Corona")
T.glos("Casa del Rey", "Conjunto de miembros civiles y militares que el Rey nombra y releva libremente (art. 65.2); se sostiene con la cantidad global de los Presupuestos del Estado (art. 65.1).", "s3", "La Corona")
T.glos("Derecho de gracia", "Función del Rey que se ejerce con arreglo a la ley, que no podrá autorizar indultos generales (art. 62 i).", "s5", "Funciones del Rey")
T.glos("Primogenitura y representación", "Orden regular de la sucesión en el trono: línea anterior, grado más próximo, varón en el mismo grado y más edad en el mismo sexo (art. 57.1).", "s9", "Sucesión")
T.glos("Príncipe de Asturias", "Dignidad del Príncipe heredero desde su nacimiento o desde el hecho que origine el llamamiento (art. 57.2).", "s9", "Sucesión")
T.glos("Abdicación", "Las abdicaciones y renuncias se resuelven por ley orgánica (art. 57.5); la de Don Juan Carlos I de Borbón se hizo efectiva por la LO 3/2014.", "s9", "Sucesión")
T.glos("Regencia", "Ejercicio de las funciones del Rey, por mandato constitucional y siempre en su nombre, durante su minoría de edad o inhabilitación (art. 59).", "s11", "Regencia")
T.glos("Tutor del Rey menor", "Persona que ejerce la tutela del Rey menor de edad: la nombrada en el testamento del Rey difunto, el padre o la madre viudos o la que nombren las Cortes (art. 60).", "s12", "Tutela")
T.glos("Juramento", "Compromiso de desempeñar fielmente las funciones, guardar y hacer guardar la Constitución y las leyes y respetar los derechos de los ciudadanos y de las Comunidades Autónomas; lo prestan el Rey, el Príncipe heredero y los Regentes (art. 61).", "s13", "Sucesión")
T.glos("Refrendo", "Requisito de validez de los actos del Rey (art. 56.3): los refrendan el Presidente del Gobierno y, en su caso, los Ministros competentes o, en los casos del art. 64.1, el Presidente del Congreso, que son los responsables de esos actos (art. 64.2).", "s15", "Refrendo")

# Cronología (fechas de los metadatos del BOE)
T.hito("1978", "Constitución Española (27-12-1978; BOE de 29-12-1978)", "Título II, «De la Corona» (arts. 56 a 65)", "normativo", "s1")
T.hito("1997", "Ley 50/1997, de 27 de noviembre, del Gobierno (BOE de 28-11-1997)", "Arts. 2.2 h) y 4.1 d): refrendo del Presidente del Gobierno y de los Ministros", "normativo", "s16")
T.hito("2014", "Ley Orgánica 3/2014, de 18 de junio (BOE de 19-6-2014), por la que se hace efectiva la abdicación de Su Majestad el Rey Don Juan Carlos I de Borbón", "Aplicación del art. 57.5: la abdicación es efectiva con la entrada en vigor de la ley, en el momento de su publicación", "normativo", "s9")

T.publicar()
