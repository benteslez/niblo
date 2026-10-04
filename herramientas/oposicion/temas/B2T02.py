# -*- coding: utf-8 -*-
"""Tema II.2 (B2T02): La organización de la Unión Europea (I): el Consejo Europeo, el
Consejo y la Comisión Europea. Composición y funciones. El procedimiento decisorio. La
participación de los Estados miembros en las diferentes fases del proceso.
Método del I.2. Normas: TUE, arts. 10 a 18 (selección); TFUE, arts. 235 a 250, 289, 291 y
293 a 297; Protocolos n.º 1 y n.º 2; Decisión 2013/272/UE del Consejo Europeo (EUR-Lex,
DOUE); Ley 8/1994 (Comisión Mixta para la Unión Europea), Ley 2/1997 (Conferencia para
Asuntos Relacionados con las Comunidades Europeas) y Acuerdos de la Conferencia de 9 de
diciembre de 2004 (BOE). Lista de formaciones del Consejo: Decisiones 2009/878/UE y
2010/594/UE (EUR-Lex), citadas literalmente en bloques con su URL."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO.update({"TUE": "TUE", "TFUE": "TFUE", "PROT1": "Protocolo n.º 1", "PROT2": "Protocolo n.º 2",
              "DCE2013": "Decisión 2013/272/UE del Consejo Europeo", "L8_1994": "Ley 8/1994",
              "L2_1997": "Ley 2/1997", "CARUE2004": "Acuerdo de la CARUE de 9-12-2004"})
D2009 = "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32009D0878"
D2010 = "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32010D0594"


def U(n, resaltar=(), solo=None, titulo=None): return lit("TUE", f"Artículo {n}", resaltar, solo, titulo)
def F(n, resaltar=(), solo=None, titulo=None): return lit("TFUE", f"Artículo {n}", resaltar, solo, titulo)
def cU(n, frag): return c("TUE", f"Artículo {n}", frag)
def cF(n, frag): return c("TFUE", f"Artículo {n}", frag)
def frag(t): return t + " (fragmento)"


T = Tema("B2T02",
  "Cinco preguntas: I. Qué es el Consejo Europeo y qué hace (TUE, arts. 13 y 15; TFUE, arts. 235 y 236) · II. Qué es el Consejo y cómo decide (TUE, art. 16; TFUE, arts. 237 a 243) · III. Qué es la Comisión y cómo funciona (TUE, art. 17; TFUE, arts. 244 a 250) · IV. Cómo se decide: el procedimiento legislativo (TFUE, arts. 289 y 293 a 297) · V. Cómo participan los Estados miembros en cada fase (TUE, art. 12; Protocolos n.º 1 y 2; Ley 8/1994; Ley 2/1997). Cada artículo: texto literal (DOUE o BOE) y ficha.",
  ["Consejo Europeo", "Presidente del Consejo Europeo", "Consejo", "Mayoría cualificada", "COREPER", "Formaciones del Consejo", "Comisión Europea", "Iniciativa legislativa", "Moción de censura", "Procedimiento legislativo ordinario", "Comité de Conciliación", "Art. 294 TFUE", "Parlamentos nacionales", "Subsidiariedad", "Comisión Mixta para la UE", "CARUE"])

# =============================================================================
T.ap("s0", "Mapa del tema: cinco preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque II, tema 2):
> La organización de la Unión Europea (I): el Consejo Europeo, el Consejo y la Comisión Europea. Composición y funciones. El procedimiento decisorio. La participación de los Estados miembros en las diferentes fases del proceso.

### El hilo conductor

El epígrafe se lee como **cinco preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Tratados (EUR-Lex) | Otras normas |
|---|---|---|---|
| **I** | ¿Qué es el **Consejo Europeo** y qué hace? (composición y funciones) | TUE, arts. 13, 10.2 y 15; TFUE, arts. 235 y 236 | — |
| **II** | ¿Qué es el **Consejo** y cómo decide? (composición y funciones) | TUE, art. 16; TFUE, arts. 237 a 243 | Decisiones 2009/878/UE y 2010/594/UE (formaciones) |
| **III** | ¿Qué es la **Comisión** y cómo funciona? (composición y funciones) | TUE, arts. 17 y 18; TFUE, arts. 244 a 250 | Decisión 2013/272/UE del Consejo Europeo |
| **IV** | ¿Cómo se decide? (el **procedimiento decisorio**) | TFUE, arts. 289 y 293 a 297; TUE, art. 11.4 | — |
| **V** | ¿Cómo participan los **Estados miembros** en cada fase? | TUE, art. 12; TFUE, art. 291; Protocolos n.º 1 y 2 | Ley 8/1994 (Comisión Mixta); Ley 2/1997 (CARUE); Acuerdos de la CARUE de 2004 |

!> **La idea que une los cinco bloques:** el **Consejo Europeo** (Jefes de Estado o de Gobierno) da los **impulsos** y las **orientaciones**, pero **no legisla** (I). Legislan el **Parlamento Europeo y el Consejo** (ministros de los Estados) (II), casi siempre **a propuesta de la Comisión**, que defiende el **interés general** de la Unión con independencia (III). El **procedimiento legislativo ordinario** del art. 294 TFUE encadena propuesta, lecturas y conciliación (IV). Los **Estados** están dentro del proceso en cada fase: en el Consejo Europeo y en el Consejo, con sus **Parlamentos nacionales** vigilando la **subsidiariedad** y, en España, con las **Cortes** (Comisión Mixta) y las **Comunidades Autónomas** (CARUE) (V).

### Cómo está escrito

- Cada artículo: primero el **texto literal** y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen). Los Tratados, los Protocolos y las decisiones de la Unión se citan de **EUR-Lex** (etiqueta **DOUE**); las leyes españolas, del **BOE**.
- El Parlamento Europeo, el Tribunal de Justicia, el Tribunal de Cuentas y el BCE son del **tema II.3**; los actos jurídicos de la Unión (reglamento, directiva, decisión: art. 288 TFUE), del **tema II.4**; el presupuesto y el marco financiero, del **tema II.5**.
- Los esquemas y cuadros **no son texto legal**: resumen los artículos citados.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué es el Consejo Europeo y qué hace? (TUE, arts. 13, 10.2 y 15; TFUE, arts. 235 y 236)", donde(
  "Primera pregunta del tema. Antes de ver cada institución hay que situarla en el **marco institucional** de la Unión. Después, el **Consejo Europeo**: quién lo compone, qué hace (y qué **no** hace), cómo decide y quién lo preside.",
  ["1 El marco institucional (TUE, arts. 13 y 10.2)", "2 Funciones, composición y forma de decidir (TUE, art. 15.1 a 4)", "3 El Presidente del Consejo Europeo (TUE, art. 15.5 y 6)", "4 Funcionamiento: votaciones y decisiones sobre el Consejo (TFUE, arts. 235 y 236)"]))

T.ap("s1", "I.1 El marco institucional de la Unión (TUE, arts. 13 y 10.2)", f"""
{unidad("1.1 Las siete instituciones (TUE, art. 13)",
  U(13, ["El Consejo Europeo", "El Consejo,", "La Comisión Europea", "Las instituciones mantendrán entre sí una cooperación leal", "un Comité Económico y Social y por un Comité de las Regiones que ejercerán funciones consultivas"]),
  fichab("Marco institucional de la Unión",
         ["::Siete instituciones (13.1):", "Parlamento Europeo", "**Consejo Europeo**", "**Consejo**", "**Comisión Europea**", "Tribunal de Justicia de la Unión Europea", "Banco Central Europeo", "Tribunal de Cuentas"],
         ["Cada institución actúa **dentro de los límites de sus atribuciones** (13.2)", "Las instituciones mantienen entre sí una **cooperación leal** (13.2)", "Las disposiciones detalladas figuran en el **TFUE** (13.3)"],
         "—",
         "Son **siete**. El **Comité Económico y Social** y el **Comité de las Regiones** **no** son instituciones: asisten al Parlamento, al Consejo y a la Comisión con **funciones consultivas** (13.4)."))}

{unidad("1.2 Cómo están representados los Estados miembros (TUE, art. 10.2)",
  U(10, ["en el Consejo Europeo por su Jefe de Estado o de Gobierno y en el Consejo por sus Gobiernos"], solo=[2, 3], titulo=frag("Artículo 10 (TUE)")),
  fichab("Doble vía de representación en la Unión",
         ["**Ciudadanos**: directamente, a través del **Parlamento Europeo**", "**Estados miembros**: en el **Consejo Europeo** (Jefe de Estado o de Gobierno) y en el **Consejo** (Gobiernos)"],
         f"Los Gobiernos son {cU(10, 'democráticamente responsables, bien ante sus Parlamentos nacionales, bien ante sus ciudadanos')}",
         "—",
         "Los **Estados** están en el **Consejo Europeo** y en el **Consejo**; la **Comisión** no representa a los Estados (→ III.2.1). Es la base del bloque V."))}
""", 2)

T.ap("s2", "I.2 El Consejo Europeo: funciones, composición y forma de decidir (TUE, art. 15.1 a 4)", f"""
{unidad("2.1 Funciones y composición (art. 15.1 y 2)",
  U(15, ["dará a la Unión los impulsos necesarios para su desarrollo y definirá sus orientaciones y prioridades políticas generales", "No ejercerá función legislativa alguna", "los Jefes de Estado o de Gobierno de los Estados miembros, así como por su Presidente y por el Presidente de la Comisión", "Participará en sus trabajos el Alto Representante"], solo=[1, 2], titulo=frag("Artículo 15 (TUE)")),
  fichab("Institución que impulsa y orienta la Unión",
         ["::Miembros (15.2):", "Los **Jefes de Estado o de Gobierno** de los Estados miembros", "Su **Presidente**", "El **Presidente de la Comisión**", "Participa en sus trabajos, sin ser miembro: el **Alto Representante** para Asuntos Exteriores y Política de Seguridad"],
         ["Da los **impulsos** necesarios para el desarrollo de la Unión", "Define sus **orientaciones y prioridades políticas generales**", "**No** ejerce función legislativa alguna"],
         "—",
         "El Consejo Europeo **no legisla** (15.1). El Alto Representante **participa**, pero no figura entre sus miembros."))}

{unidad("2.2 Reuniones y forma de decidir (art. 15.3 y 4)",
  U(15, ["dos veces por semestre por convocatoria de su Presidente", "reunión extraordinaria", "El Consejo Europeo se pronunciará por consenso, excepto cuando los Tratados dispongan otra cosa"], solo=[3, 4], titulo=frag("Artículo 15 (TUE)")),
  fichab("Reuniones y regla de decisión",
         ["Convoca su **Presidente**", "Cada miembro puede contar con la asistencia de un **ministro**; el Presidente de la Comisión, con la de un **miembro de la Comisión**"],
         ["Reunión ordinaria: **dos veces por semestre**", "Reunión **extraordinaria** cuando la situación lo exija"],
         "Regla general: **consenso**, salvo que los Tratados dispongan otra cosa",
         "**Dos veces por semestre** (no «por trimestre» ni «al año»). Regla general: **consenso** (no mayoría cualificada ni unanimidad). Cayó en 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s3", "I.3 El Presidente del Consejo Europeo (TUE, art. 15.5 y 6)", f"""
{unidad("3.1 Elección y mandato (art. 15.5)",
  U(15, ["por mayoría cualificada para un mandato de dos años y medio, que podrá renovarse una sola vez", "En caso de impedimento o falta grave"], solo=[5], titulo=frag("Artículo 15 (TUE)")),
  fichab("Elección del Presidente del Consejo Europeo",
         "Lo elige el **propio Consejo Europeo**",
         "Elección y, en caso de impedimento o falta grave, fin del mandato **por el mismo procedimiento**",
         ["Mayoría **cualificada**", "Mandato de **dos años y medio**, renovable **una sola vez**"],
         "**Dos años y medio**, renovable **una vez** (no cinco años, ni dos). Pregunta oficial L 19 (→ Cierre 1)."))}

{unidad("3.2 Funciones e incompatibilidad (art. 15.6)",
  U(15, ["presidirá e impulsará los trabajos del Consejo Europeo", "al término de cada reunión del Consejo Europeo, presentará un informe al Parlamento Europeo", "la representación exterior de la Unión en los asuntos de política exterior y de seguridad común", "no podrá ejercer mandato nacional alguno"], solo=list(range(6, 13)), titulo=frag("Artículo 15 (TUE)")),
  fichab("Qué hace el Presidente del Consejo Europeo",
         "El Presidente del Consejo Europeo",
         ["**Preside e impulsa** los trabajos del Consejo Europeo (a)", "Vela por su **preparación y continuidad**, con el Presidente de la Comisión y sobre los trabajos del Consejo de **Asuntos Generales** (b)", "Facilita la **cohesión y el consenso** (c)", "Presenta un **informe al Parlamento Europeo** tras cada reunión (d)", "**Representación exterior** en la PESC, en su rango y condición, sin perjuicio del Alto Representante"],
         "Informe al Parlamento Europeo: **al término de cada reunión**",
         "**No puede ejercer mandato nacional alguno** (incompatibilidad absoluta). El informe es al **Parlamento Europeo**."))}
""", 2)

T.ap("s4", "I.4 Funcionamiento: votaciones y decisiones sobre el Consejo (TFUE, arts. 235 y 236)", f"""
{unidad("4.1 Votaciones, mayorías y asistencia (TFUE, art. 235)",
  F(235, ["podrá actuar en representación de uno solo de los demás miembros", "no participarán en las votaciones del Consejo Europeo", "La abstención de los miembros presentes o representados no obstará", "invitar al Presidente del Parlamento Europeo a comparecer ante él", "por mayoría simple en las cuestiones de procedimiento y para la aprobación de su reglamento interno", "asistido por la Secretaría General del Consejo"]),
  fichab("Cómo vota el Consejo Europeo",
         ["Votan los **Jefes de Estado o de Gobierno**", "**No votan** el Presidente del Consejo Europeo ni el Presidente de la Comisión"],
         ["Cada miembro puede representar a **uno solo** de los demás (235.1)", "Mayoría cualificada: la del **art. 16.4 TUE** y el **art. 238.2 TFUE** (→ II.3.2)", "La **abstención** no impide la **unanimidad**", "Puede invitar al **Presidente del Parlamento Europeo** (235.2)", "Lo asiste la **Secretaría General del Consejo** (235.4)"],
         "**Mayoría simple**: cuestiones de procedimiento y reglamento interno (235.3)",
         "Delegación de voto: en **uno solo** de los demás miembros. La abstención **no** bloquea la unanimidad. Su secretaría es la **del Consejo**."))}

{unidad("4.2 Decisiones del Consejo Europeo sobre el Consejo (TFUE, art. 236)",
  F(236, ["adoptará por mayoría cualificada", "la lista de las formaciones del Consejo", "presidencia de las formaciones del Consejo"]),
  fichab("Dos decisiones organizativas sobre el Consejo",
         "El **Consejo Europeo**",
         ["a) **Lista de formaciones** del Consejo, distintas de Asuntos Generales y Asuntos Exteriores (→ II.2.1)", "b) **Presidencia** de las formaciones, salvo Asuntos Exteriores (→ II.2.2)"],
         "**Mayoría cualificada**",
         "Las formaciones de **Asuntos Generales** y **Asuntos Exteriores** las crea el propio **TUE** (16.6), no esta decisión."))}

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Consejo Europeo | Regla | Artículo |
|---|---|---|
| Regla general de decisión | **Consenso**, salvo que los Tratados dispongan otra cosa | TUE 15.4 |
| Elección de su Presidente | **Mayoría cualificada**; 2 años y medio, renovable una vez | TUE 15.5 |
| Procedimiento y reglamento interno | **Mayoría simple** | TFUE 235.3 |
| Formaciones del Consejo y su presidencia | **Mayoría cualificada** | TFUE 236 |
| Reuniones | Dos veces por semestre; extraordinarias si la situación lo exige | TUE 15.3 |

{resumen([
  "**Siete** instituciones (TUE 13); el CESE y el Comité de las Regiones son **consultivos**.",
  "Consejo Europeo: **Jefes de Estado o de Gobierno** + su **Presidente** + Presidente de la **Comisión**; da **impulsos** y **orientaciones**; **no legisla** (TUE 15.1 y 2).",
  "Se reúne **dos veces por semestre** y decide por **consenso** (TUE 15.3 y 4).",
  "Presidente: **mayoría cualificada**, **dos años y medio**, renovable **una vez**; **sin mandato nacional** (TUE 15.5 y 6).",
  "Mayoría **simple** para procedimiento y reglamento interno; sus Presidentes y el de la Comisión **no votan** (TFUE 235)."],
  "Siguiente: II. ¿Qué es el Consejo y cómo decide?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Qué es el Consejo y cómo decide? (TUE, art. 16; TFUE, arts. 237 a 243)", donde(
  "Segunda pregunta. El **Consejo** (los ministros de los Estados) es, con el Parlamento Europeo, **colegislador** y autoridad **presupuestaria**. Hay que saber cómo se compone, en qué **formaciones** se reúne, quién prepara sus trabajos (**COREPER**) y, sobre todo, con qué **mayorías** decide.",
  ["1 Funciones, composición y mayoría cualificada (TUE, art. 16.1 a 5)", "2 Formaciones, COREPER, sesiones públicas y presidencia (TUE, art. 16.6 a 9)", "3 Funcionamiento y mayorías (TFUE, arts. 237 a 243)"]))

T.ap("s5", "II.1 Funciones, composición y mayoría cualificada (TUE, art. 16.1 a 5)", f"""
{unidad("1.1 Funciones y composición (art. 16.1 y 2)",
  U(16, ["conjuntamente con el Parlamento Europeo la función legislativa y la función presupuestaria", "funciones de definición de políticas y de coordinación", "un representante de cada Estado miembro, de rango ministerial, facultado para comprometer al Gobierno del Estado miembro al que represente y para ejercer el derecho de voto"], solo=[1, 2], titulo=frag("Artículo 16 (TUE)")),
  fichab("Institución de los Gobiernos de los Estados miembros",
         f"{cU(16, 'un representante de cada Estado miembro, de rango ministerial')}, facultado para **comprometer a su Gobierno** y **votar**",
         ["Función **legislativa** y **presupuestaria**, **conjuntamente con el Parlamento Europeo**", "Funciones de **definición de políticas** y de **coordinación**"],
         "—",
         "Legisla **con** el Parlamento Europeo (no solo). Sus miembros son de **rango ministerial** y pueden **comprometer a su Gobierno**."))}

{unidad("1.2 La mayoría cualificada (art. 16.3 a 5)",
  U(16, ["El Consejo se pronunciará por mayoría cualificada, excepto cuando los Tratados dispongan otra cosa", "un mínimo del 55 % de los miembros del Consejo que incluya al menos a quince de ellos y represente a Estados miembros que reúnan como mínimo el 65 % de la población de la Unión", "al menos cuatro miembros del Consejo"], solo=[3, 4, 5, 6, 7], titulo=frag("Artículo 16 (TUE)")),
  fichab("Regla general de decisión del Consejo",
         "El Consejo",
         ["Regla general: **mayoría cualificada** (16.3)", "Las demás modalidades, en el **art. 238.2 TFUE** (→ II.3.2)"],
         ["::Desde el **1 de noviembre de 2014** (doble mayoría):", "**55 %** de los miembros del Consejo, con **al menos quince**", "Que representen al menos el **65 %** de la población de la Unión", "Minoría de bloqueo: **al menos cuatro** miembros; si no, la mayoría se considera alcanzada"],
         "**55 % de Estados** (mínimo **quince**) + **65 % de población**. Minoría de bloqueo: **cuatro** miembros como mínimo. Regla general del **Consejo** = mayoría **cualificada**; del **Consejo Europeo** = **consenso** (→ I.2.2)."))}
""", 2)

T.ap("s6", "II.2 Formaciones, COREPER, sesiones públicas y presidencia (TUE, art. 16.6 a 9)", f"""
{unidad("2.1 Formaciones del Consejo (art. 16.6)",
  U(16, ["El Consejo se reunirá en diferentes formaciones", "El Consejo de Asuntos Generales velará por la coherencia de los trabajos de las diferentes formaciones del Consejo", "Preparará las reuniones del Consejo Europeo", "El Consejo de Asuntos Exteriores elaborará la acción exterior de la Unión"], solo=[8, 9, 10], titulo=frag("Artículo 16 (TUE)")),
  fichab("El Consejo se reúne por materias",
         "Los ministros competentes en cada materia; la lista de formaciones la adopta el **Consejo Europeo** (TFUE 236 a, → I.4.2)",
         ["**Asuntos Generales**: coherencia entre formaciones; **prepara** las reuniones del Consejo Europeo y garantiza su actuación subsiguiente", "**Asuntos Exteriores**: elabora la **acción exterior** según las líneas del Consejo Europeo"],
         "—",
         "Quien **prepara** las reuniones del **Consejo Europeo** es el Consejo de **Asuntos Generales** (no el COREPER)."))}

> [[DOUE|{D2009}]]
> **Decisión 2009/878/UE del Consejo (Asuntos Generales), de 1 de diciembre de 2009, por la que se establece la lista de formaciones del Consejo (DOUE L 315 de 2.12.2009) · anexo (texto de EUR-Lex, sin las notas al pie)**
> ANEXO LISTA DE FORMACIONES DEL CONSEJO
> 1. Asuntos Generales
> 2. Asuntos Exteriores
> 3. Asuntos Económicos y Financieros
> 4. Justicia y Asuntos de Interior
> 5. Empleo, Política Social, Sanidad y Consumidores
> 6. Competitividad (Mercado Interior, Industria e Investigación)
> 7. Transporte, Telecomunicaciones y Energía
> 8. Agricultura y Pesca
> 9. Medio Ambiente
> 10. Educación, Juventud y Cultura

> [[DOUE|{D2010}]]
> **Decisión 2010/594/UE del Consejo Europeo, de 16 de septiembre de 2010, por la que se modifica la lista de formaciones del Consejo (DOUE L 263 de 6.10.2010) · artículo 1 (texto de EUR-Lex)**
> 1) El punto 6 «Competitividad (Mercado Interior, Industria e Investigación)» se sustituye por el texto siguiente: «6. Competitividad (Mercado Interior, Industria, Investigación y Espacio)».
> 2) El punto 10 «Educación, Juventud y Cultura» se sustituye por el texto siguiente: «10. Educación, Juventud, Cultura y Deporte».

?> **Diez formaciones.** Leídas las dos decisiones juntas, la lista tiene **diez** formaciones; la 6 es «Competitividad (Mercado Interior, Industria, Investigación y Espacio)» y la 10, «Educación, Juventud, Cultura y Deporte». La ficha de EUR-Lex de la Decisión 2009/878/UE no recoge más modificaciones que la de 2010.

{unidad("2.2 COREPER, sesiones públicas y presidencia (art. 16.7 a 9)",
  U(16, ["Un Comité de Representantes Permanentes de los Gobiernos de los Estados miembros se encargará de preparar los trabajos del Consejo", "El Consejo se reunirá en público cuando delibere y vote sobre un proyecto de acto legislativo", "con excepción de la de Asuntos Exteriores", "sistema de rotación igual"], solo=[11, 12, 13], titulo=frag("Artículo 16 (TUE)")),
  fichab("Preparación, publicidad y presidencia del Consejo",
         ["**COREPER** (Comité de Representantes Permanentes): prepara los trabajos", "Presidencia: los **representantes de los Estados** por **rotación igual**; la de **Asuntos Exteriores**, no (la preside el Alto Representante: TUE 18.3)"],
         ["Sesión **pública** cuando delibera y vota un **proyecto de acto legislativo**", "Cada sesión, en **dos partes**: actos legislativos y actividades no legislativas"],
         "—",
         "**Comité de Representantes Permanentes** (no «Especiales», «Expertos» ni «Profesionales»): pregunta oficial L 20 (→ Cierre 1). Publicidad: solo al deliberar y votar **actos legislativos**."))}
""", 2)

T.ap("s7", "II.3 Funcionamiento y mayorías del Consejo (TFUE, arts. 237 a 243)", f"""
{unidad("3.1 Convocatoria (art. 237)",
  F(237, ["por convocatoria de su Presidente, a iniciativa de éste, de uno de sus miembros o de la Comisión"]),
  fichab("Quién pone en marcha una reunión del Consejo", "Convoca el **Presidente**", ["A iniciativa del **Presidente**", "De **uno de sus miembros**", "O de la **Comisión**"], "—",
         "La **Comisión** puede pedir que se reúna el Consejo; el **Parlamento Europeo**, no (no está en la lista)."))}

{unidad("3.2 Mayoría simple, mayoría cualificada reforzada y abstención (art. 238)",
  F(238, ["el Consejo se pronunciará por mayoría de los miembros que lo componen", "cuando el Consejo no actúe a propuesta de la Comisión o del Alto Representante", "un mínimo del 72 % de los miembros del Consejo", "más del 35 % de la población de los Estados miembros participantes, más un miembro", "Las abstenciones de los miembros presentes o representados no impedirán la adopción de los acuerdos del Consejo que requieran unanimidad"]),
  fichab("Las mayorías del Consejo",
         "El Consejo (y el Consejo Europeo cuando vota por mayoría cualificada: TFUE 235.1)",
         ["Si no todos los miembros votan, los porcentajes se calculan sobre los **Estados participantes** (238.3)", "Las **abstenciones** no impiden la **unanimidad** (238.4)"],
         ["**Mayoría simple** = mayoría de los **miembros que lo componen** (238.1)", "Mayoría cualificada sin propuesta de la Comisión o del Alto Representante: **72 %** de los miembros + **65 %** de la población (238.2)", "Con participación parcial: **55 %** + **65 %**; bloqueo: miembros que representen **más del 35 %** de la población **más un miembro** (238.3 a)"],
         "Cuando **no** hay propuesta de la Comisión o del Alto Representante, el porcentaje de Estados sube al **72 %** (la población sigue en el **65 %**)."))}

{unidad("3.3 Delegación de voto (art. 239)",
  F(239, ["podrá actuar en representación de uno solo de los demás miembros"]),
  fichab("Representación en las votaciones", "Cada miembro del Consejo", "Puede votar en nombre de otro miembro", "Como máximo, de **uno solo** de los demás", "Igual que en el Consejo Europeo (TFUE 235.1)."))}

{unidad("3.4 COREPER y Secretaría General (art. 240)",
  F(240, ["preparar los trabajos del Consejo y de realizar las tareas que éste le confíe", "podrá adoptar decisiones de procedimiento", "Secretario General nombrado por el Consejo", "por mayoría simple en las cuestiones de procedimiento y para la aprobación de su reglamento interno"]),
  fichab("Órganos de apoyo del Consejo",
         ["**COREPER**: Representantes Permanentes de los Gobiernos", "**Secretaría General**, bajo un **Secretario General** nombrado por el Consejo"],
         ["COREPER: prepara los trabajos, realiza las tareas que se le confíen y puede adoptar **decisiones de procedimiento** en los casos del reglamento interno", "La Secretaría General asiste al Consejo (y al Consejo Europeo: TFUE 235.4)"],
         ["Organización de la Secretaría General: **mayoría simple** (240.2)", "Procedimiento y reglamento interno del Consejo: **mayoría simple** (240.3)"],
         "El COREPER **prepara**; no adopta actos legislativos. Solo **decisiones de procedimiento** previstas en el reglamento interno."))}

{unidad("3.5 Petición de propuestas, Comités y retribuciones (arts. 241 a 243)",
  F(241, ["por mayoría simple, podrá pedir a la Comisión", "Si la Comisión no presenta propuesta alguna, comunicará las razones al Consejo"]),
  F(242, ["previa consulta a la Comisión"]),
  F(243, ["fijará los sueldos, dietas y pensiones"]),
  fichab("Otras atribuciones del Consejo",
         "El Consejo",
         ["Pedir a la Comisión **estudios** y **propuestas** (241)", "Establecer los **estatutos de los Comités** previstos en los Tratados, previa consulta a la Comisión (242)", "Fijar **sueldos, dietas y pensiones** del Presidente del Consejo Europeo, del Presidente y los miembros de la Comisión, del Alto Representante, del TJUE y del Secretario General del Consejo (243)"],
         "**Mayoría simple** (241 y 242)",
         "El Consejo **pide** propuestas, pero no puede obligar a la Comisión a presentarlas: si no la presenta, la Comisión **comunica las razones**."))}

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Mayoría | Cómo se calcula | Cuándo | Artículo |
|---|---|---|---|
| Simple | Mayoría de los **miembros que lo componen** | Procedimiento, reglamento interno, Secretaría General, petición de propuestas, estatutos de Comités | TFUE 238.1, 240, 241 y 242 |
| Cualificada | **55 %** de los miembros (mínimo **15**) + **65 %** de la población; bloqueo: **4** miembros | Regla general | TUE 16.3 y 4 |
| Cualificada reforzada | **72 %** de los miembros + **65 %** de la población | Cuando el Consejo **no** actúa a propuesta de la Comisión o del Alto Representante | TFUE 238.2 |
| Unanimidad | Las **abstenciones no la impiden** | Cuando los Tratados la exigen | TFUE 238.4 |

{resumen([
  "Consejo: un representante de **rango ministerial** por Estado; **colegislador** y autoridad **presupuestaria** con el Parlamento Europeo (TUE 16.1 y 2).",
  "Regla general: **mayoría cualificada** = **55 %** de los miembros (mín. **15**) + **65 %** de la población; bloqueo con **4** (TUE 16.4). Sin propuesta de la Comisión: **72 %** (TFUE 238.2).",
  "**Asuntos Generales** prepara el Consejo Europeo; **Asuntos Exteriores**, la acción exterior; **COREPER** prepara los trabajos del Consejo (TUE 16.6 y 7).",
  "Sesión **pública** al deliberar y votar actos **legislativos**; presidencia por **rotación igual**, salvo Asuntos Exteriores (TUE 16.8 y 9)."],
  "Siguiente: III. ¿Qué es la Comisión y cómo funciona?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Qué es la Comisión y cómo funciona? (TUE, arts. 17 y 18; TFUE, arts. 244 a 250)", donde(
  "Tercera pregunta. La **Comisión** promueve el **interés general** de la Unión, tiene casi en exclusiva la **iniciativa legislativa** y actúa con **plena independencia** de los Gobiernos. Responde ante el **Parlamento Europeo**.",
  ["1 Funciones e iniciativa legislativa (TUE, art. 17.1 y 2)", "2 Mandato, composición e independencia (TUE, art. 17.3 a 5; Decisión 2013/272/UE; TFUE, arts. 244 y 245)", "3 Presidente, nombramiento y responsabilidad (TUE, arts. 17.6 a 8 y 18; TFUE, art. 248)", "4 Fin del mandato, cese y funcionamiento (TFUE, arts. 246, 247, 249 y 250)"]))

T.ap("s8", "III.1 Funciones e iniciativa legislativa (TUE, art. 17.1 y 2)", f"""
{unidad("1.1 Funciones de la Comisión (art. 17.1)",
  U(17, ["La Comisión promoverá el interés general de la Unión", "Velará por que se apliquen los Tratados", "bajo el control del Tribunal de Justicia de la Unión Europea", "Ejecutará el presupuesto y gestionará los programas", "asumirá la representación exterior de la Unión"], solo=[1], titulo=frag("Artículo 17 (TUE)")),
  fichab("La institución del interés general",
         "La **Comisión**",
         ["Promueve el **interés general** de la Unión y toma las **iniciativas** adecuadas", "**Vela** por la aplicación de los Tratados y de las medidas de las instituciones", "**Supervisa** la aplicación del Derecho de la Unión, bajo el control del TJUE", "**Ejecuta el presupuesto** y gestiona los programas", "Coordinación, ejecución y gestión", "**Representación exterior**, salvo la PESC y otros casos previstos", "Iniciativas de la **programación anual y plurianual**"],
         "—",
         "Pregunta oficial P 13 (→ Cierre 1): la Comisión **promueve el interés general** y **vela por la aplicación de los Tratados**. No representa a los Estados, no juzga y no aprueba el marco financiero."))}

{unidad("1.2 El monopolio de la iniciativa legislativa (art. 17.2)",
  U(17, ["Los actos legislativos de la Unión sólo podrán adoptarse a propuesta de la Comisión, excepto cuando los Tratados dispongan otra cosa"], solo=[2], titulo=frag("Artículo 17 (TUE)")),
  fichab("Iniciativa legislativa",
         "La **Comisión** (regla general)",
         ["Actos **legislativos**: **solo a propuesta de la Comisión**, salvo que los Tratados dispongan otra cosa", "Demás actos: a propuesta de la Comisión **cuando así lo establezcan** los Tratados"],
         "—",
         "Excepciones: los casos del art. 289.4 TFUE (grupo de Estados, Parlamento Europeo, BCE, Tribunal de Justicia, BEI: → IV.1.1)."))}
""", 2)

T.ap("s9", "III.2 Mandato, composición e independencia (TUE, art. 17.3 a 5; Decisión 2013/272/UE; TFUE, arts. 244 y 245)", f"""
{unidad("2.1 Mandato, requisitos e independencia (art. 17.3)",
  U(17, ["El mandato de la Comisión será de cinco años", "competencia general y de su compromiso europeo", "con plena independencia", "no solicitarán ni aceptarán instrucciones de ningún gobierno"], solo=[3, 4, 5], titulo=frag("Artículo 17 (TUE)")),
  fichab("Una institución independiente de los Gobiernos",
         ["Personalidades elegidas por su **competencia general** y su **compromiso europeo**", "Con **plenas garantías de independencia**"],
         ["Ejerce sus responsabilidades con **plena independencia**", "Sus miembros **no solicitan ni aceptan instrucciones** de ningún gobierno, institución, órgano u organismo"],
         "Mandato: **cinco años**",
         "La Comisión **no representa a los Estados**: sus miembros no reciben **instrucciones** de los Gobiernos. Mandato de **cinco** años (el del Presidente del Consejo Europeo es de dos años y medio)."))}

{unidad("2.2 Número de miembros (art. 17.4 y 5; Decisión 2013/272/UE)",
  U(17, ["dos tercios del número de Estados miembros", "a menos que el Consejo Europeo decida por unanimidad modificar dicho número", "un sistema de rotación estrictamente igual"], solo=[6, 7, 8], titulo=frag("Artículo 17 (TUE)")),
  lit("DCE2013", "Artículo 1", ["un número de miembros igual al número de Estados miembros"], titulo="Artículo 1 (Decisión 2013/272/UE del Consejo Europeo, de 22 de mayo de 2013, relativa al número de miembros de la Comisión Europea)"),
  lit("DCE2013", "Artículo 2", ["trigésimo Estado miembro"], titulo="Artículo 2 (Decisión 2013/272/UE)"),
  lit("DCE2013", "Artículo 3", ["Será aplicable a partir del 1 de noviembre de 2014"], solo=[1, 2], titulo="Artículo 3 (Decisión 2013/272/UE)"),
  fichab("Cuántos comisarios hay",
         "El **Consejo Europeo**, **por unanimidad**, puede modificar el número (17.5)",
         ["Regla del Tratado desde el 1-11-2014: **dos tercios** del número de Estados, con rotación **estrictamente igual** (17.5)", "Decisión 2013/272/UE: un número **igual al número de Estados miembros**, incluidos el Presidente y el Alto Representante"],
         "Unanimidad del Consejo Europeo; revisión antes de la primera Comisión tras la adhesión del **trigésimo** Estado (art. 2 de la Decisión)",
         "El Tratado dice «**dos tercios**», pero el Consejo Europeo lo ha **modificado por unanimidad**: hoy, **un miembro por Estado** (Decisión 2013/272/UE, aplicable desde el **1-11-2014**)."))}

{unidad("2.3 El sistema de rotación (TFUE, art. 244)",
  F(244, ["establecido por unanimidad por el Consejo Europeo", "rigurosa igualdad", "nunca podrá ser superior a uno", "diversidad demográfica y geográfica"]),
  fichab("Cómo se reparten los puestos si hay menos comisarios que Estados",
         "Lo establece el **Consejo Europeo**, por **unanimidad**",
         ["**Rigurosa igualdad** entre Estados en orden de turno y permanencia", "Reflejar la **diversidad demográfica y geográfica**"],
         "Diferencia máxima de mandatos entre nacionales de dos Estados: **uno**",
         "Solo se aplicaría con una Comisión de **dos tercios** (17.5 TUE); hoy hay un comisario por Estado (→ III.2.2)."))}

{unidad("2.4 Deberes de los miembros (TFUE, art. 245)",
  F(245, ["Los Estados miembros respetarán su independencia y no intentarán influir en ellos", "no podrán, mientras dure su mandato, ejercer ninguna otra actividad profesional, retribuida o no", "honestidad y discreción", "a instancia del Consejo, por mayoría simple, o de la Comisión"]),
  fichab("Incompatibilidades y deberes de los comisarios",
         "Los miembros de la Comisión; el **Tribunal de Justicia** declara el incumplimiento",
         ["Abstenerse de todo acto **incompatible** con sus funciones", "Ninguna otra **actividad profesional**, **retribuida o no**, durante el mandato", "Compromiso solemne de **honestidad y discreción**, también **después** del mandato"],
         "Sanción: **cese** (art. 247) o **privación de la pensión**, a instancia del Consejo (**mayoría simple**) o de la Comisión",
         "La incompatibilidad alcanza a actividades **no retribuidas**. Los deberes siguen **después** del mandato."))}
""", 2)

T.ap("s10", "III.3 Presidente, nombramiento y responsabilidad (TUE, arts. 17.6 a 8 y 18; TFUE, art. 248)", f"""
{unidad("3.1 El Presidente de la Comisión (TUE, art. 17.6; TFUE, art. 248)",
  U(17, ["definirá las orientaciones con arreglo a las cuales la Comisión desempeñará sus funciones", "coherencia, eficacia y colegialidad", "nombrará Vicepresidentes", "Un miembro de la Comisión presentará su dimisión si se lo pide el Presidente"], solo=[9, 10, 11, 12, 13], titulo=frag("Artículo 17 (TUE)")),
  F(248, ["serán estructuradas y repartidas entre sus miembros por el Presidente", "bajo la autoridad de éste"]),
  fichab("Dirección política de la Comisión",
         "El **Presidente** de la Comisión",
         ["Define las **orientaciones** (a)", "Determina la **organización interna**: coherencia, eficacia y **colegialidad** (b)", "Nombra **Vicepresidentes** de entre los comisarios, distintos del Alto Representante (c)", "**Reparte** las responsabilidades entre los miembros y puede **reorganizarlas** (TFUE 248)"],
         "—",
         "Un comisario **dimite si se lo pide el Presidente**. El Alto Representante es Vicepresidente **por el Tratado** (TUE 18.4), no por nombramiento del Presidente."))}

{unidad("3.2 Nombramiento de la Comisión (TUE, art. 17.7)",
  U(17, ["Teniendo en cuenta el resultado de las elecciones al Parlamento Europeo", "por mayoría cualificada, un candidato al cargo de Presidente de la Comisión", "El Parlamento Europeo elegirá al candidato por mayoría de los miembros que lo componen", "en el plazo de un mes", "de común acuerdo con el Presidente electo", "se someterán colegiadamente al voto de aprobación del Parlamento Europeo", "la Comisión será nombrada por el Consejo Europeo, por mayoría cualificada"], solo=[14, 15, 16], titulo=frag("Artículo 17 (TUE)")),
  fichab("Cómo se nombra la Comisión (procedimiento en tres pasos)",
         ["**Consejo Europeo**: propone al candidato a Presidente y nombra la Comisión", "**Parlamento Europeo**: elige al Presidente y aprueba el colegio", "**Consejo**: adopta la lista de las demás personalidades"],
         ["1.º Propuesta del candidato, **teniendo en cuenta las elecciones europeas** y tras consultas", "2.º Elección por el **Parlamento Europeo**", "3.º Lista de comisarios, **de común acuerdo con el Presidente electo**, a partir de las propuestas de los **Estados**", "4.º **Voto de aprobación colegiado** del Parlamento Europeo", "5.º **Nombramiento** por el Consejo Europeo"],
         ["Propuesta y nombramiento: **mayoría cualificada** del Consejo Europeo", "Elección del Presidente: **mayoría de los miembros** del Parlamento Europeo", "Si no la obtiene: nuevo candidato **en un mes**"],
         "Propone el **Consejo Europeo**; **elige** el **Parlamento**; la lista la adopta el **Consejo** (no el Consejo Europeo); **nombra** el **Consejo Europeo**."))}

{unidad("3.3 Responsabilidad ante el Parlamento Europeo (TUE, art. 17.8)",
  U(17, ["responsabilidad colegiada ante el Parlamento Europeo", "moción de censura", "dimitir colectivamente de sus cargos"], solo=[17], titulo=frag("Artículo 17 (TUE)")),
  fichab("Control político de la Comisión",
         "El **Parlamento Europeo**, frente a la Comisión como **colegio**",
         ["Responsabilidad **colegiada**", "**Moción de censura** según el art. 234 TFUE (tema II.3)", "Si se aprueba: **dimisión colectiva**; el Alto Representante dimite **del cargo que ejerce en la Comisión**"],
         "La mayoría de la moción está en el art. 234 TFUE (tema II.3)",
         "La responsabilidad es ante el **Parlamento Europeo** (no ante el Consejo) y **colegiada**."))}

{unidad("3.4 El Alto Representante dentro de la Comisión (TUE, art. 18.1 y 4)",
  U(18, ["con la aprobación del Presidente de la Comisión", "será uno de los Vicepresidentes de la Comisión"], solo=[1, 4], titulo=frag("Artículo 18 (TUE)")),
  fichab("Doble posición del Alto Representante",
         "Nombra el **Consejo Europeo**, con la **aprobación del Presidente de la Comisión**",
         ["Es uno de los **Vicepresidentes** de la Comisión", "Vela por la **coherencia de la acción exterior**", "Preside el Consejo de **Asuntos Exteriores** (18.3, → II.2.2)"],
         "Nombramiento y cese: **mayoría cualificada** del Consejo Europeo",
         "Es **miembro de la Comisión** y **participa** en el Consejo Europeo (15.2) sin ser miembro de este."))}
""", 2)

T.ap("s11", "III.4 Fin del mandato, cese y funcionamiento (TFUE, arts. 246, 247, 249 y 250)", f"""
{unidad("4.1 Fin del mandato y sustitución (art. 246)",
  F(246, ["por dimisión voluntaria o cese", "un nuevo miembro de la misma nacionalidad, nombrado por el Consejo, de común acuerdo con el Presidente de la Comisión, previa consulta al Parlamento Europeo", "por unanimidad y a propuesta del Presidente de la Comisión", "continuarán despachando los asuntos de administración ordinaria"]),
  fichab("Cuándo termina el mandato de un comisario y cómo se le sustituye",
         ["Sustituto: **misma nacionalidad**, nombrado por el **Consejo** con el **Presidente de la Comisión**, previa consulta al **Parlamento**", "Presidente: procedimiento del art. 17.7 TUE", "Alto Representante: art. 18.1 TUE"],
         ["Fin individual: **dimisión voluntaria** o **cese** (además de renovación periódica y fallecimiento)", "Dimisión de **todos**: siguen en funciones (**administración ordinaria**) hasta su sustitución"],
         "No sustituir: **unanimidad** del Consejo a propuesta del **Presidente de la Comisión**",
         "El sustituto es de la **misma nacionalidad** y solo **por el resto del mandato**."))}

{unidad("4.2 Cese por el Tribunal de Justicia (art. 247)",
  F(247, ["deje de reunir las condiciones necesarias para el ejercicio de sus funciones o haya cometido una falta grave", "podrá ser cesado por el Tribunal de Justicia, a instancia del Consejo, por mayoría simple, o de la Comisión"]),
  fichab("Cese forzoso de un comisario",
         ["Cesa: el **Tribunal de Justicia**", "Pide el cese: el **Consejo** (mayoría simple) o la **Comisión**"],
         ["::Dos causas:", "Dejar de reunir las **condiciones necesarias** para el ejercicio de sus funciones", "Haber cometido una **falta grave**"],
         "Consejo: **mayoría simple**",
         "Falta **grave** (no «leve»). Cesa el **Tribunal de Justicia**, no el Parlamento ni el Presidente. Pregunta oficial P 11 (→ Cierre 1)."))}

{unidad("4.3 Reglamento interno, informe general y acuerdos (arts. 249 y 250)",
  F(249, ["La Comisión publicará dicho reglamento", "al menos un mes antes de la apertura del período de sesiones del Parlamento Europeo, un informe general sobre las actividades de la Unión"]),
  F(250, ["Los acuerdos de la Comisión se adoptarán por mayoría de sus miembros", "Su reglamento interno fijará el quórum"]),
  fichab("Cómo funciona la Comisión",
         "La Comisión, como **colegio**",
         ["Establece y **publica** su **reglamento interno** (249.1)", "Publica cada año un **informe general** sobre las actividades de la Unión (249.2)"],
         ["Informe general: **al menos un mes antes** de la apertura del período de sesiones del Parlamento Europeo", "Acuerdos: **mayoría de sus miembros**; el **quórum**, en su reglamento interno (250)"],
         "**Un mes** (no tres, cuatro ni seis): pregunta oficial L 21 (→ Cierre 1). Mayoría **de sus miembros** (no de los presentes)."))}

{resumen([
  "La Comisión **promueve el interés general**, **vela** por la aplicación de los Tratados, **ejecuta** el presupuesto y tiene la **iniciativa legislativa** salvo excepción (TUE 17.1 y 2).",
  "Mandato de **cinco años**; **plena independencia**; un comisario **por Estado** (Decisión 2013/272/UE, que modifica los **dos tercios** del TUE 17.5).",
  "Nombramiento: propone el **Consejo Europeo** (mayoría cualificada) → **elige** el **Parlamento** (mayoría de sus miembros) → lista del **Consejo** → aprobación **colegiada** del Parlamento → **nombra** el **Consejo Europeo** (TUE 17.7).",
  "Responsabilidad **colegiada** ante el Parlamento (moción de censura) (TUE 17.8); cese individual por el **Tribunal de Justicia** (falta **grave** o pérdida de condiciones) (TFUE 247).",
  "Informe general **un mes antes** del período de sesiones del Parlamento; acuerdos por **mayoría de sus miembros** (TFUE 249 y 250)."],
  "Siguiente: IV. ¿Cómo se decide? El procedimiento decisorio")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Cómo se decide? El procedimiento decisorio (TFUE, arts. 289 y 293 a 297; TUE, art. 11.4)", donde(
  "Cuarta pregunta. Ya conocemos a los protagonistas; ahora, **cómo** adoptan las normas. Los Tratados distinguen el procedimiento legislativo **ordinario** (Parlamento y Consejo, a propuesta de la Comisión) y los **especiales**. El ordinario se regula paso a paso en el **art. 294 TFUE**.",
  ["1 Procedimientos y actos legislativos; iniciativa (TFUE, art. 289; TUE, art. 11.4)", "2 La propuesta de la Comisión (TFUE, art. 293)", "3 El procedimiento legislativo ordinario (TFUE, art. 294)", "4 Cooperación, motivación, firma y publicación (TFUE, arts. 295 a 297)"]))

T.ap("s12", "IV.1 Procedimientos y actos legislativos; iniciativa (TFUE, art. 289; TUE, art. 11.4)", f"""
{unidad("1.1 Procedimiento ordinario, procedimientos especiales y actos legislativos (TFUE, art. 289)",
  F(289, ["la adopción conjunta por el Parlamento Europeo y el Consejo, a propuesta de la Comisión", "bien por el Parlamento Europeo con la participación del Consejo, bien por el Consejo con la participación del Parlamento Europeo", "constituirán actos legislativos", "por iniciativa de un grupo de Estados miembros o del Parlamento Europeo, por recomendación del Banco Central Europeo o a petición del Tribunal de Justicia o del Banco Europeo de Inversiones"]),
  fichab("Dos clases de procedimiento legislativo",
         ["**Ordinario**: **Parlamento Europeo y Consejo** conjuntamente, a propuesta de la **Comisión**", "**Especial**: el **Parlamento** con participación del **Consejo**, o el **Consejo** con participación del **Parlamento**"],
         ["Producen **reglamentos, directivas o decisiones** (tipos de actos: tema II.4)", "Lo adoptado por procedimiento legislativo = **acto legislativo** (289.3)", "Iniciativas distintas de la Comisión solo en los **casos específicos** previstos (289.4)"],
         "El ordinario se define en el **art. 294** (→ IV.3)",
         "Especial = **uno** de los dos adopta y el otro **participa**. Excepciones a la iniciativa de la Comisión: **grupo de Estados**, **Parlamento**, **BCE**, **Tribunal de Justicia**, **BEI**."))}

{unidad("1.2 La iniciativa ciudadana (TUE, art. 11.4)",
  U(11, ["al menos un millón de ciudadanos de la Unión", "un número significativo de Estados miembros", "invitar a la Comisión Europea"], solo=[4, 5], titulo=frag("Artículo 11 (TUE)")),
  fichab("Los ciudadanos pueden invitar a la Comisión a proponer",
         f"{cU(11, 'Un grupo de al menos un millón de ciudadanos de la Unión')}, nacionales de un **número significativo** de Estados miembros",
         "**Invitan** a la Comisión, en el marco de sus atribuciones, a presentar una propuesta; procedimiento y condiciones según el art. 24 TFUE",
         "**Un millón** de ciudadanos",
         "Los ciudadanos **invitan**: no presentan ellos la propuesta. La iniciativa sigue siendo de la **Comisión**."))}
""", 2)

T.ap("s13", "IV.2 La propuesta de la Comisión (TFUE, art. 293)", f"""
{unidad("2.1 Quién puede cambiar la propuesta (art. 293)",
  F(293, ["únicamente podrá modificar la propuesta por unanimidad", "la Comisión podrá modificar su propuesta mientras duren los procedimientos"]),
  fichab("Protección de la propuesta de la Comisión",
         ["**Consejo**: solo la modifica **por unanimidad** (293.1)", "**Comisión**: puede modificarla mientras el Consejo no se haya pronunciado (293.2)"],
         "Excepciones a la unanimidad: **294.10 y 13** (conciliación y tercera lectura), arts. **310, 312, 314** y **315** párrafo segundo (presupuestarios)",
         "Para modificar: **unanimidad** del Consejo",
         "Es una garantía del **monopolio de iniciativa**: el Consejo solo puede apartarse de la propuesta **por unanimidad**, salvo en conciliación."))}
""", 2)

T.ap("s14", "IV.3 El procedimiento legislativo ordinario (TFUE, art. 294)", f"""
{unidad("3.1 Propuesta y primera lectura (art. 294.1 a 6)",
  F(294, ["La Comisión presentará una propuesta al Parlamento Europeo y al Consejo", "El Parlamento Europeo aprobará su posición en primera lectura y la transmitirá al Consejo", "Si el Consejo aprueba la posición del Parlamento Europeo, se adoptará el acto", "adoptará su posición en primera lectura y la transmitirá al Parlamento Europeo"], solo=[1, 2, 3, 4, 5, 6], titulo=frag("Artículo 294 (TFUE)")),
  fichab("Primera lectura: primero el Parlamento, después el Consejo",
         ["**Comisión**: propuesta al Parlamento y al Consejo", "**Parlamento Europeo**: posición en primera lectura", "**Consejo**: aprueba esa posición o adopta la suya"],
         ["Si el Consejo **aprueba** la posición del Parlamento → acto **adoptado** (294.4)", "Si **no** la aprueba → **posición del Consejo** en primera lectura, motivada, al Parlamento (294.5 y 6)"],
         "La primera lectura **no tiene plazo** en el art. 294",
         "En primera lectura el **primero** en pronunciarse es el **Parlamento**. El Consejo **informa** de sus razones; la Comisión, de su posición."))}

{unidad("3.2 Segunda lectura (art. 294.7 a 9)",
  F(294, ["Si, en un plazo de tres meses a partir de dicha transmisión", "o no toma decisión alguna", "rechaza, por mayoría de los miembros que lo componen", "propone, por mayoría de los miembros que lo componen, enmiendas", "el Consejo, por mayoría cualificada", "convocará al Comité de Conciliación en un plazo de seis semanas", "El Consejo se pronunciará por unanimidad sobre las enmiendas que hayan sido objeto de un dictamen negativo de la Comisión"], solo=list(range(7, 15)), titulo=frag("Artículo 294 (TFUE)")),
  fichab("Segunda lectura: el Parlamento sobre la posición del Consejo; el Consejo sobre las enmiendas",
         ["**Parlamento Europeo** (3 meses)", "**Consejo** (3 meses desde la recepción de las enmiendas)", "**Comisión**: dictamina sobre las enmiendas"],
         ["Parlamento **aprueba** o **no decide** → acto adoptado con la posición del Consejo (7 a)", "Parlamento **rechaza** → acto **no adoptado** (7 b)", "Parlamento **enmienda** → al Consejo y a la Comisión (7 c)", "Consejo aprueba **todas** las enmiendas → adoptado (8 a); si no → **Comité de Conciliación** en **6 semanas** (8 b)"],
         ["Plazos: **tres meses** (Parlamento) y **tres meses** (Consejo)", "Rechazo o enmiendas del Parlamento: **mayoría de los miembros que lo componen**", "Consejo: **mayoría cualificada**; **unanimidad** para enmiendas con **dictamen negativo** de la Comisión (294.9)"],
         "El **silencio** del Parlamento en segunda lectura **adopta** el acto (posición del Consejo). Convoca la conciliación el **Presidente del Consejo**, de acuerdo con el del Parlamento."))}

{unidad("3.3 Conciliación y tercera lectura (art. 294.10 a 14)",
  F(294, ["los miembros del Consejo o sus representantes y por un número igual de miembros que representen al Parlamento Europeo", "en el plazo de seis semanas a partir de su convocatoria", "el acto propuesto se considerará no adoptado", "pronunciándose el Parlamento Europeo por mayoría de los votos emitidos y el Consejo por mayoría cualificada", "como máximo, en un mes y dos semanas respectivamente"], solo=list(range(15, 20)), titulo=frag("Artículo 294 (TFUE)")),
  fichab("Comité de Conciliación y tercera lectura",
         ["**Comité de Conciliación**: miembros del **Consejo** (o representantes) y un **número igual** de representantes del **Parlamento**", "La **Comisión** participa y facilita el acercamiento"],
         ["Objetivo: **texto conjunto** sobre las posiciones en segunda lectura", "Sin texto conjunto en el plazo → **no adoptado**", "Con texto conjunto → **tercera lectura**: Parlamento y Consejo adoptan el acto"],
         ["Conciliación: **seis semanas**; acuerdo por **mayoría cualificada** (Consejo) y **mayoría** de los representantes del Parlamento", "Tercera lectura: **seis semanas**; Parlamento por **mayoría de los votos emitidos**, Consejo por **mayoría cualificada**", "Ampliación: los **tres meses**, hasta **un mes**; las **seis semanas**, hasta **dos semanas** (294.14)"],
         "En **tercera lectura** el Parlamento decide por mayoría de los **votos emitidos** (en segunda, por mayoría de sus **miembros**)."))}

{unidad("3.4 Cuando la iniciativa no es de la Comisión (art. 294.15)",
  F(294, ["no se aplicarán el apartado 2, la segunda frase del apartado 6 ni el apartado 9", "podrá pedir el dictamen de la Comisión"], solo=[20, 21], titulo=frag("Artículo 294 (TFUE)")),
  fichab("Procedimiento ordinario iniciado por otros",
         "Iniciativa de un **grupo de Estados**, recomendación del **BCE** o instancia del **Tribunal de Justicia**",
         ["No se aplican: la propuesta de la Comisión (294.2), su información en primera lectura (294.6, 2.ª frase) ni la **unanimidad** del 294.9", "El Parlamento y el Consejo transmiten el proyecto y sus posiciones a la Comisión, que puede **dictaminar**"],
         "—",
         "Sin propuesta de la Comisión **no hay** unanimidad del Consejo por dictamen negativo de esta (294.9 no se aplica)."))}

*Esquema de elaboración propia: resume el art. 294 TFUE; no es texto legal.*

| Fase | Quién | Plazo | Mayoría | Resultado |
|---|---|---|---|---|
| Propuesta | Comisión | — | — | Al Parlamento y al Consejo |
| 1.ª lectura | Parlamento, después Consejo | Sin plazo | — | Consejo aprueba la posición del PE → adoptado; si no, posición del Consejo |
| 2.ª lectura (PE) | Parlamento | 3 meses (+1) | Mayoría de **miembros** para rechazar o enmendar | Aprueba o calla → adoptado; rechaza → no adoptado; enmienda → Consejo |
| 2.ª lectura (Consejo) | Consejo | 3 meses (+1) | Cualificada; **unanimidad** si dictamen negativo de la Comisión | Aprueba todas → adoptado; si no → conciliación |
| Conciliación | Comité (Consejo + igual número del PE) | Convocatoria en 6 semanas; 6 semanas (+2) para acordar | Cualificada (Consejo) y mayoría (PE) | Sin texto conjunto → no adoptado |
| 3.ª lectura | Parlamento y Consejo | 6 semanas (+2) | PE: **votos emitidos**; Consejo: cualificada | Adoptado o no adoptado |
""", 2)

T.ap("s15", "IV.4 Cooperación, motivación, firma y publicación (TFUE, arts. 295 a 297)", f"""
{unidad("4.1 Acuerdos interinstitucionales (art. 295)",
  F(295, ["llevarán a cabo consultas recíprocas", "podrán celebrar acuerdos interinstitucionales que podrán tener carácter vinculante"]),
  fichab("Cooperación entre los tres", "**Parlamento Europeo, Consejo y Comisión**", "Consultas recíprocas y organización de común acuerdo de su cooperación", "—",
         "Los acuerdos interinstitucionales **pueden** ser **vinculantes**."))}

{unidad("4.2 Elección del tipo de acto y motivación (art. 296)",
  F(296, ["conforme a los procedimientos aplicables y al principio de proporcionalidad", "Los actos jurídicos deberán estar motivados", "se abstendrán de adoptar actos no previstos por el procedimiento legislativo aplicable"]),
  fichab("Reglas comunes a los actos", "Las instituciones",
         ["Si el Tratado no fija el tipo de acto: se elige caso por caso según la **proporcionalidad**", "Todos los actos: **motivados** y con referencia a las propuestas, iniciativas o dictámenes previstos", "Ante un proyecto legislativo, Parlamento y Consejo no adoptan **actos no previstos** en el procedimiento"], "—",
         "La **motivación** es obligatoria para **todos** los actos jurídicos."))}

{unidad("4.3 Firma, publicación y entrada en vigor (art. 297)",
  F(297, ["serán firmados por el Presidente del Parlamento Europeo y por el Presidente del Consejo", "serán firmados por el Presidente de la institución que los haya adoptado", "Entrarán en vigor en la fecha que ellos mismos fijen o, a falta de ella, a los veinte días de su publicación", "se notificarán a sus destinatarios y surtirán efecto en virtud de dicha notificación"]),
  fichab("Último paso: firma y publicación",
         ["Procedimiento **ordinario**: firman el **Presidente del Parlamento Europeo** y el **Presidente del Consejo**", "Procedimiento **especial** y actos no legislativos: el **Presidente de la institución** que lo adoptó"],
         ["Actos legislativos, reglamentos, directivas dirigidas a todos los Estados y decisiones sin destinatario: **DOUE**", "Demás directivas y decisiones con destinatario: **notificación**"],
         "Entrada en vigor: la fecha que fijen o, en su defecto, a los **veinte días** de su publicación",
         "Firma del ordinario: Presidentes del **Parlamento** y del **Consejo** (no de la Comisión): pregunta oficial P 14 (→ Cierre 1). **Veinte** días de *vacatio*."))}

{resumen([
  "Procedimiento **ordinario**: Parlamento **y** Consejo a propuesta de la Comisión; **especial**: uno adopta y el otro participa; lo que sale de ellos son **actos legislativos** (TFUE 289).",
  "El Consejo solo modifica la propuesta de la Comisión **por unanimidad**, salvo conciliación y tercera lectura (TFUE 293).",
  "Art. 294: 1.ª lectura sin plazo; 2.ª lectura **3 + 3 meses**; conciliación **6 semanas**; 3.ª lectura **6 semanas**; ampliables **1 mes** y **2 semanas**.",
  "Firman los Presidentes del **Parlamento** y del **Consejo**; entrada en vigor a los **veinte días** de su publicación si no fijan fecha (TFUE 297)."],
  "Siguiente: V. ¿Cómo participan los Estados miembros en cada fase?")}
""", 2)

# =============================================================================
T.ap("bV", "V. ¿Cómo participan los Estados miembros en cada fase? (TUE, art. 12; TFUE, art. 291; Protocolos n.º 1 y 2; Ley 8/1994; Ley 2/1997)", donde(
  "Quinta pregunta. Los Estados no están fuera del proceso: deciden en el **Consejo Europeo** y en el **Consejo**; sus **Parlamentos nacionales** reciben los proyectos y controlan la **subsidiariedad**; y, al final, los Estados **ejecutan** el Derecho de la Unión. En España, esa participación se articula en las **Cortes** (Comisión Mixta para la Unión Europea) y con las **Comunidades Autónomas** (CARUE).",
  ["1 Las fases del proceso y la ejecución por los Estados (esquema; TFUE, art. 291)", "2 Los Parlamentos nacionales (TUE, art. 12; Protocolos n.º 1 y 2)", "3 España: las Cortes Generales y la Comisión Mixta para la Unión Europea (Ley 8/1994)", "4 España: las Comunidades Autónomas (Ley 2/1997; Acuerdos de la CARUE de 2004)"]))

T.ap("s16", "V.1 Las fases del proceso y la ejecución por los Estados (esquema; TFUE, art. 291)", f"""
*Esquema de elaboración propia: resume los artículos citados en este tema; no es texto legal.*

| Fase | Cómo intervienen los Estados | Dónde |
|---|---|---|
| Orientación política | Jefes de Estado o de Gobierno en el **Consejo Europeo** | TUE 10.2 y 15 (→ I.2) |
| Propuesta | Proponen comisarios (la Comisión es independiente); un **grupo de Estados** puede tener la iniciativa en casos tasados | TUE 17.7; TFUE 289.4 (→ III.3.2 y → IV.1.1) |
| Control de la propuesta | Los **Parlamentos nacionales** reciben los proyectos y emiten **dictámenes motivados** de subsidiariedad | TUE 12; Protocolos n.º 1 y 2 (→ V.2) |
| Decisión | Ministros en el **Consejo**, preparado por el **COREPER** | TUE 16; TFUE 240 (→ II.1 y → II.2) |
| Ejecución | Los Estados adoptan las medidas de **Derecho interno**; controlan las competencias de ejecución de la Comisión | TFUE 291 (→ V.1.1) |
| Control judicial | Recurso por violación de la **subsidiariedad** ante el TJUE | Protocolo n.º 2, art. 8 (→ V.2.4) |

{unidad("1.1 La ejecución, tarea de los Estados (TFUE, art. 291)",
  F(291, ["Los Estados miembros adoptarán todas las medidas de Derecho interno necesarias para la ejecución de los actos jurídicamente vinculantes de la Unión", "conferirán competencias de ejecución a la Comisión", "las modalidades de control, por parte de los Estados miembros", "la expresión «de ejecución»"]),
  fichab("Quién ejecuta el Derecho de la Unión",
         ["Regla: los **Estados miembros**", "Si hacen falta **condiciones uniformes**: la **Comisión** (o el **Consejo** en casos justificados y en la PESC)"],
         ["Los actos vinculantes confieren las competencias de ejecución", "Parlamento y Consejo fijan **por reglamento (procedimiento ordinario)** cómo **controlan los Estados** a la Comisión", "Los actos llevan en el título «**de ejecución**»"],
         "—",
         "La ejecución es, **por regla general**, de los **Estados**; la Comisión solo cuando se requieren **condiciones uniformes**. Los actos **delegados** (art. 290) y los actos jurídicos se estudian en el tema II.4."))}
""", 2)

T.ap("s17", "V.2 Los Parlamentos nacionales (TUE, art. 12; Protocolos n.º 1 y 2)", f"""
{unidad("2.1 Qué hacen los Parlamentos nacionales (TUE, art. 12)",
  U(12, ["contribuirán activamente al buen funcionamiento de la Unión", "recibirán notificación de los proyectos de actos legislativos", "velarán por que se respete el principio de subsidiariedad", "participarán en los procedimientos de revisión de los Tratados", "serán informados de las solicitudes de adhesión"]),
  fichab("Los Parlamentos nacionales en la Unión",
         "Los **Parlamentos nacionales**",
         ["Reciben **información** y los **proyectos de actos legislativos** (Protocolo n.º 1) (a)", "Velan por la **subsidiariedad** (Protocolo n.º 2) (b)", "Evaluación en el espacio de libertad, seguridad y justicia; control de **Europol** y **Eurojust** (c)", "**Revisión** de los Tratados (d) y **adhesiones** (e)", "Cooperación **interparlamentaria** (f)"],
         "—",
         "Su función principal en el proceso legislativo es vigilar la **subsidiariedad** (no la proporcionalidad: el control del Protocolo n.º 2 es de subsidiariedad)."))}

{unidad("2.2 Información y plazo de ocho semanas (Protocolo n.º 1, arts. 2, 4 y 8)",
  lit("PROT1", "Artículo 2", ["se transmitirán a los Parlamentos nacionales"], solo=[1, 2]),
  lit("PROT1", "Artículo 4", ["deberá transcurrir un plazo de ocho semanas", "deberá transcurrir un plazo de diez días"]),
  lit("PROT1", "Artículo 8", ["se aplicarán a las cámaras que lo compongan"]),
  fichab("Los proyectos llegan antes a los Parlamentos nacionales",
         "Transmiten: la **Comisión**, el **Parlamento Europeo** o el **Consejo**, según el origen del proyecto",
         ["Se transmiten **todos** los proyectos de actos legislativos", "En sistemas **bicamerales**, cada **cámara** recibe y actúa (art. 8)"],
         ["**Ocho semanas** entre la transmisión y la inclusión en el orden del día del Consejo (salvo urgencia motivada)", "**Diez días** entre la inclusión en el orden del día y la adopción de la posición del Consejo"],
         "**Ocho semanas** para los Parlamentos; **diez días** en el orden del día del Consejo. En España: Congreso **y** Senado."))}

{unidad("2.3 El dictamen motivado de subsidiariedad (Protocolo n.º 2, art. 6)",
  lit("PROT2", "Artículo 6", ["en un plazo de ocho semanas a partir de la fecha de transmisión", "un dictamen motivado que exponga las razones por las que considera que el proyecto no se ajusta al principio de subsidiariedad", "consultar, cuando proceda, a los Parlamentos regionales que posean competencias legislativas"], solo=[1]),
  fichab("Alerta temprana de subsidiariedad",
         "Cada **Parlamento nacional** o cada **cámara**; consultan, cuando proceda, a los **Parlamentos regionales** con competencias legislativas",
         "**Dictamen motivado** dirigido a los Presidentes del **Parlamento Europeo**, del **Consejo** y de la **Comisión**",
         "**Ocho semanas** desde la transmisión del proyecto en las lenguas oficiales",
         "Lo que se controla es la **subsidiariedad**. En España, los Parlamentos autonómicos tienen **cuatro semanas** para enviar su dictamen a las Cortes (Ley 8/1994, art. 6: → V.3.4)."))}

{unidad("2.4 Efectos de los dictámenes y recurso ante el Tribunal de Justicia (Protocolo n.º 2, arts. 7 y 8)",
  lit("PROT2", "Artículo 7", ["Cada Parlamento nacional dispondrá de dos votos", "al menos un tercio del total de votos", "se reducirá a un cuarto", "podrá decidir mantener el proyecto, modificarlo o retirarlo", "al menos la mayoría simple de los votos atribuidos a los Parlamentos nacionales", "por mayoría del 55 % de los miembros del Consejo o por mayoría de los votos emitidos en el Parlamento Europeo"]),
  lit("PROT2", "Artículo 8", ["con arreglo a los procedimientos establecidos en el artículo 263", "el Comité de las Regiones también podrá interponer recursos"]),
  fichab("Qué pasa si los Parlamentos nacionales se oponen",
         ["Cada Parlamento nacional: **dos votos** (en sistema bicameral, **uno por cámara**)", "Recurso ante el **TJUE**: lo interpone el **Estado miembro**, también en nombre de su Parlamento o de una cámara; también el **Comité de las Regiones**"],
         ["**Un tercio** de los votos → el proyecto se **vuelve a estudiar**; el autor lo **mantiene, modifica o retira**, motivadamente (7.2)", "Espacio de libertad, seguridad y justicia (art. 76 TFUE): basta **un cuarto** (7.2)", "Procedimiento **ordinario**: **mayoría simple** de los votos → nuevo estudio; si la Comisión la mantiene, el legislador decide antes de concluir la **primera lectura** (7.3)"],
         ["Desestimación (7.3 b): **55 %** de los miembros del **Consejo** o **mayoría de los votos emitidos** en el **Parlamento Europeo**", "Recurso: el del art. **263 TFUE** (anulación)"],
         "Umbrales: **1/3** (general), **1/4** (art. 76 TFUE) y **mayoría simple** (procedimiento ordinario). Los dictámenes **no vetan**: obligan a **reestudiar**."))}
""", 2)

T.ap("s18", "V.3 España: las Cortes Generales y la Comisión Mixta para la Unión Europea (Ley 8/1994)", f"""
{unidad("3.1 Creación y composición (arts. 1 y 2)",
  lit("L8_1994", "a1", ["Comisión Mixta del Congreso de los Diputados y del Senado", "participación adecuada en las propuestas legislativas elaboradas por la Comisión Europea"]),
  lit("L8_1994", "a2", ["garantizando, en todo caso, la presencia de todos los Grupos Parlamentarios", "dentro de los quince días siguientes a la constitución de las Cámaras", "al Presidente del Congreso de los Diputados o al diputado o senador en quien éste delegue con carácter permanente", "mayoría simple de los miembros presentes"]),
  fichab("El órgano de las Cortes para los asuntos europeos",
         ["Comisión **Mixta** de **Congreso y Senado**", "Número de miembros: lo fijan las **Mesas** de las Cámaras en **sesión conjunta**", "Miembros designados por los **Grupos**, en proporción a su importancia", "Preside el **Presidente del Congreso** (o el diputado o senador en quien delegue permanentemente)"],
         "Fin: participación de las Cortes en las **propuestas legislativas** de la Comisión Europea y la **más amplia información** sobre la Unión",
         ["Nombres de los miembros: en **15 días** desde la constitución de las Cámaras", "Acuerdos: **mayoría simple de los presentes**"],
         "Es **mixta** (Congreso + Senado) y la preside el **Presidente del Congreso**. Están **todos** los Grupos Parlamentarios."))}

{unidad("3.2 Competencias (art. 3, selección)",
  lit("L8_1994", "a3", ["un sucinto informe sobre el contenido sustancial de aquellas propuestas legislativas que tengan repercusión en España", "con anterioridad a cada Consejo Europeo ordinario", "dictamen motivado sobre la vulneración del principio de subsidiariedad", "en el plazo máximo de dos semanas", "Solicitar del Gobierno la interposición del recurso de anulación"], solo=[1, 2, 3, 4, 10, 11, 17, 18, 20, 21], titulo=frag("Artículo 3 (Ley 8/1994)")),
  fichab("Qué hace la Comisión Mixta",
         "La **Comisión Mixta**; el **Gobierno** le informa",
         ["Conoce los **decretos legislativos** de aplicación del Derecho derivado (a)", "Recibe las **propuestas legislativas**; el Gobierno envía un **sucinto informe** de las que tengan repercusión en España (b)", "Es informada de la política del Gobierno en la Unión y de los acuerdos del **Consejo** (e)", "Emite, **en nombre de las Cortes**, el **dictamen motivado** de subsidiariedad (j)", "Pide al Gobierno el **recurso de anulación** por subsidiariedad (k)", "Participa en la **revisión simplificada** del art. 48.7 TUE (l)"],
         ["Informe escrito del Gobierno **antes de cada Consejo Europeo ordinario** (e)", "Informe del Gobierno sobre subsidiariedad: **dos semanas** como máximo (j)"],
         "El dictamen de subsidiariedad lo emite la **Comisión Mixta en nombre de las Cortes** (no el Gobierno)."))}

{unidad("3.3 Comparecencias del Gobierno (art. 4 y artículos 8 y 9 «nuevos»)",
  lit("L8_1994", "a4", ["ante el Pleno del Congreso de los Diputados, con posterioridad a cada Consejo Europeo, ordinario o extraordinario"]),
  lit("L8_1994", "a8-2", ["antes de la celebración de la reunión del Consejo"], titulo="Artículo 8 (nuevo) del capítulo tercero (Ley 8/1994)"),
  lit("L8_1994", "a9-2", ["Al final de cada presidencia semestral del Consejo de la Unión Europea"], titulo="Artículo 9 (nuevo) del capítulo tercero (Ley 8/1994)"),
  fichab("El Gobierno da cuenta antes y después",
         ["**Gobierno**, ante el **Pleno del Congreso**: después de cada **Consejo Europeo**", "**Ministros o altos cargos** que decida la **Mesa** de la Comisión Mixta: antes de cada reunión del **Consejo**", "**Ministro de Asuntos Exteriores** o **Secretario de Estado para la UE**: al final de cada **presidencia semestral**"],
         "Informar de lo decidido y debatir; manifestar la **posición del Gobierno** sobre el orden del día del Consejo; dar cuenta de los **progresos** de la presidencia",
         ["Consejo Europeo: comparecencia **posterior** (ordinario o extraordinario), ante el **Pleno del Congreso**", "Consejo: comparecencia **previa**, ante la **Comisión Mixta**"],
         "Consejo **Europeo** → **Pleno del Congreso**, **después**. Consejo (de ministros de la UE) → **Comisión Mixta**, **antes**. La ley tiene **dos** arts. 8 y 9: los añadidos en el capítulo tercero llevan «(nuevo)» en el BOE."))}

{unidad("3.4 El control de la subsidiariedad (arts. 5 y 6)",
  lit("L8_1994", "a5", ["corresponderá con carácter general a la Comisión Mixta para la Unión Europea", "podrán avocar el debate y la votación", "en el plazo máximo de ocho semanas"]),
  lit("L8_1994", "a6", ["sin prejuzgar la existencia de competencias autonómicas afectadas", "en el plazo de cuatro semanas"]),
  fichab("Cómo emiten las Cortes el dictamen motivado",
         ["Regla: la **Comisión Mixta** (5.1)", "Los **Plenos** del Congreso y del Senado pueden **avocar** (5.2)", "Los **Parlamentos autonómicos** pueden enviar su dictamen (6)"],
         ["Congreso y Senado remiten las iniciativas a los **Parlamentos autonómicos** en cuanto las reciben", "Los dictámenes se remiten a los Presidentes del **Parlamento Europeo**, del **Consejo** y de la **Comisión**, por conducto de los Presidentes de las Cámaras, y se trasladan al Gobierno"],
         ["Dictamen de las Cortes: **ocho semanas** desde la transmisión (5.3)", "Dictamen autonómico: recibido en **cuatro semanas** desde la remisión (6.2)"],
         "**Ocho** semanas (Cortes, como el Protocolo n.º 2) y **cuatro** semanas (Parlamentos autonómicos). Si un Pleno avoca, la propuesta va a los Plenos de **ambas** Cámaras."))}

{unidad("3.5 Recurso de anulación y oposición a la «pasarela» (arts. 7 y 8)",
  lit("L8_1994", "a7", ["En el plazo máximo de seis semanas desde la publicación oficial de un acto legislativo europeo", "podrá descartar, de forma motivada"]),
  lit("L8_1994", "a8", ["corresponderá a los Plenos del Congreso de los Diputados y del Senado, a propuesta de la Comisión Mixta para la Unión Europea"]),
  fichab("Últimas fases: recurso y revisión simplificada",
         ["La **Comisión Mixta** pide el recurso; lo **interpone o descarta** el **Gobierno**", "Oposición del art. 48.7 TUE: **Plenos** del Congreso y del Senado, a propuesta de la Comisión Mixta"],
         ["Recurso de **anulación** ante el TJUE por infracción de la **subsidiariedad** (art. 8 del Protocolo n.º 2: → V.2.4)", f"Oposición a que el Consejo pase de unanimidad a **mayoría cualificada** o de procedimiento especial a **ordinario** (art. 48.7 TUE: {cU(48, 'En caso de oposición de un Parlamento nacional notificada en un plazo de seis meses')}, no se adopta la decisión)"],
         "Solicitud del recurso: **seis semanas** desde la publicación oficial del acto",
         "El Gobierno puede **descartar** el recurso **motivadamente** y lo justifica compareciendo ante la Comisión Mixta si esta lo pide."))}
""", 2)

T.ap("s19", "V.4 España: las Comunidades Autónomas (Ley 2/1997; Acuerdos de la CARUE de 2004)", f"""
{unidad("4.1 La Conferencia para Asuntos Relacionados con las Comunidades Europeas (Ley 2/1997, arts. 1 a 3)",
  lit("L2_1997", "a1", ["órgano de cooperación entre el Estado y las Comunidades Autónomas", "en la fase de formación de la voluntad del Estado ante las instituciones comunitarias y en la ejecución del Derecho comunitario", "Comisión de Coordinadores de Asuntos Comunitarios Europeos"]),
  lit("L2_1997", "a2", ["que la presidirá"]),
  lit("L2_1997", "a3", ["La articulación de mecanismos para hacer efectiva la participación de las Comunidades Autónomas en la formación de la voluntad del Estado"], solo=[1, 2, 3, 10], titulo=frag("Artículo 3. Funciones (Ley 2/1997)")),
  fichab("Órgano de cooperación Estado–Comunidades Autónomas para los asuntos europeos",
         ["Preside el **Ministro de Administraciones Públicas** (así lo dice la ley; hoy, el ministro que tenga atribuida esa competencia)", "Un **Consejero** por Comunidad Autónoma", "Por el Estado, también los Secretarios de Estado de Política Exterior y para la UE y para las Administraciones Territoriales", "Órgano de apoyo: **Comisión de Coordinadores de Asuntos Comunitarios Europeos**"],
         ["Garantiza la participación autonómica en **dos fases**: **formación de la voluntad del Estado** y **ejecución** del Derecho de la Unión", "Información y debate sobre la construcción europea; mecanismos de participación; impulso de la participación a través de las **Conferencias Sectoriales**"],
         "—",
         "Es un órgano de **cooperación** (no de decisión); las fases son la **ascendente** (formación de la voluntad) y la **descendente** (ejecución). Ceuta y Melilla también participan (disposición adicional segunda)."))}

?> **Denominación de la ley.** La Ley 2/1997 sigue diciendo «Ministro de Administraciones Públicas» y «Comunidades Europeas»: se cita literal, como está en el BOE.

{unidad("4.2 Representación autonómica en el Consejo de la Unión Europea (Acuerdo de la CARUE de 9-12-2004)",
  lit("CARUE2004", "A1", ["con rango de Consejero o miembro de un Consejo de Gobierno autonómico"], solo=[1, 2], titulo="Acuerdo sobre el sistema de representación autonómica en las formaciones del Consejo de la Unión Europea, apartado 1.1 (CARUE, 9-12-2004; BOE de 16-3-2005)"),
  lit("CARUE2004", "A2", [], solo=[1, 2, 3, 4, 5, 6], titulo="Mismo Acuerdo, apartado 2.1 (formaciones en las que se aplica)"),
  lit("CARUE2004", "A5", ["miembro de pleno derecho de la delegación española", "Representará al conjunto de las Comunidades Autónomas", "La responsabilidad última de las negociaciones y de su conclusión corresponderá en todo momento al jefe de delegación"], titulo="Mismo Acuerdo, apartado 5 (aplicación de la representación autonómica directa)"),
  fichab("Un consejero autonómico en la delegación española",
         ["Un miembro **con rango de Consejero** (o de un Consejo de Gobierno autonómico) que **representa al conjunto** de las Comunidades Autónomas", "Lo designa el **Pleno** de la **Conferencia Sectorial** correspondiente (apartado 3.1)"],
         ["Se integra en la **delegación española** como miembro de pleno derecho", "Asesora al **jefe de delegación** sobre la **posición común** autonómica", "Puede pedir la palabra si hay posición común; el jefe de delegación se la cede si lo estima oportuno"],
         "—",
         "La **responsabilidad última** de la negociación es siempre del **jefe de delegación** (Estado). Texto publicado en el BOE (resolución de 28-2-2005, no consolidado); el propio Acuerdo previó su revisión tras aplicarse en 2005 (apartado 7.2)."))}

{resumen([
  "Los Estados están en todas las fases: **Consejo Europeo** y **Consejo** (decisión), **Parlamentos nacionales** (control de la propuesta) y **ejecución** (TFUE 291).",
  "Parlamentos nacionales: **ocho semanas** para el **dictamen motivado** de subsidiariedad; **dos votos** cada uno; umbrales **1/3**, **1/4** y **mayoría simple** (Protocolos n.º 1 y 2).",
  "España: **Comisión Mixta para la UE** (Congreso + Senado), que emite el dictamen **en nombre de las Cortes**; Parlamentos autonómicos, **cuatro semanas**; recurso de anulación pedido en **seis semanas** (Ley 8/1994).",
  "Gobierno: comparece ante el **Pleno del Congreso después** de cada **Consejo Europeo** y ante la Comisión Mixta **antes** de cada **Consejo** (Ley 8/1994, arts. 4 y 8 «nuevo»).",
  "Comunidades Autónomas: **CARUE** (Ley 2/1997), en la **formación de la voluntad** del Estado y en la **ejecución**; representante autonómico en ciertas formaciones del **Consejo** (Acuerdo de 2004)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_L19 = examen("L", 19, {
  "a": f"Cinco años es el mandato de la **Comisión** ({cU(17, 'El mandato de la Comisión será de cinco años')}), no el del Presidente del Consejo Europeo.",
  "b": f"Cambia la duración y la renovación: el art. 15.5 dice {cU(15, 'dos años y medio, que podrá renovarse una sola vez')}.",
  "c": f"Literal del art. 15.5 TUE: {cU(15, 'para un mandato de dos años y medio, que podrá renovarse una sola vez')}.",
  "d": f"Cuatro años no aparece en el art. 15.5: el mandato es {cU(15, 'de dos años y medio')}."},
  [("dos años y medio", "TUE", "Artículo 15", "para un mandato de dos años y medio, que podrá renovarse una sola vez")])
EX_L20 = examen("L", 20, {
  "a": f"Literal del art. 16.7 TUE: {cU(16, 'Un Comité de Representantes Permanentes de los Gobiernos de los Estados miembros se encargará de preparar los trabajos del Consejo')}.",
  "b": f"Cambia una palabra: los representantes son {cU(16, 'Permanentes')}, no «Especiales».",
  "c": f"Cambia una palabra: {cU(16, 'Comité de Representantes Permanentes')}, no «Expertos».",
  "d": f"Cambia una palabra: {cU(16, 'Comité de Representantes Permanentes')}, no «Profesionales»."},
  [("Representantes Permanentes", "TUE", "Artículo 16", "Un Comité de Representantes Permanentes de los Gobiernos de los Estados miembros se encargará de preparar los trabajos del Consejo")])
EX_L21 = examen("L", 21, {
  "a": f"Cambia el plazo: el art. 249.2 dice {cF(249, 'al menos un mes antes de la apertura del período de sesiones')}.",
  "b": f"Cambia el plazo: {cF(249, 'al menos un mes antes')}, no seis meses.",
  "c": f"Literal del art. 249.2 TFUE: {cF(249, 'La Comisión publicará todos los años, al menos un mes antes de la apertura del período de sesiones del Parlamento Europeo, un informe general sobre las actividades de la Unión')}.",
  "d": f"Cambia el plazo: {cF(249, 'al menos un mes antes')}, no cuatro meses."},
  [("un mes", "TFUE", "Artículo 249", "al menos un mes antes de la apertura del período de sesiones del Parlamento Europeo")])
EX_P11 = examen("P", 11, {
  "a": f"Cambia una palabra: la falta tiene que ser {cF(247, 'grave')}, no leve.",
  "b": f"Literal del art. 247 TFUE: {cF(247, 'Todo miembro de la Comisión que deje de reunir las condiciones necesarias para el ejercicio de sus funciones o haya cometido una falta grave podrá ser cesado por el Tribunal de Justicia')}.",
  "c": f"No es causa del art. 247, que solo prevé {cF(247, 'deje de reunir las condiciones necesarias para el ejercicio de sus funciones o haya cometido una falta grave')}.",
  "d": f"No es causa de cese; además, la Comisión actúa con {cU(17, 'plena independencia')} y adopta sus acuerdos {cF(250, 'por mayoría de sus miembros')}."},
  [("las condiciones necesarias para el ejercicio de sus funciones", "TFUE", "Artículo 247", "Todo miembro de la Comisión que deje de reunir las condiciones necesarias para el ejercicio de sus funciones")])
EX_P13 = examen("P", 13, {
  "a": f"Los Estados están representados {cU(10, 'en el Consejo Europeo por su Jefe de Estado o de Gobierno y en el Consejo por sus Gobiernos')} (art. 10.2 TUE); los comisarios {cU(17, 'no solicitarán ni aceptarán instrucciones de ningún gobierno')}.",
  "b": f"Literal del art. 17.1 TUE: {cU(17, 'La Comisión promoverá el interés general de la Unión')} y {cU(17, 'Velará por que se apliquen los Tratados')}.",
  "c": f"La función jurisdiccional es del Tribunal de Justicia de la Unión Europea (tema II.3); la Comisión supervisa la aplicación del Derecho {cU(17, 'bajo el control del Tribunal de Justicia de la Unión Europea')}.",
  "d": f"El marco financiero plurianual lo adopta el Consejo: {cF(312, 'El Consejo adoptará con arreglo a un procedimiento legislativo especial un reglamento que fije el marco financiero plurianual')} (art. 312.2 TFUE; tema II.5)."},
  [("interés general de la Unión", "TUE", "Artículo 17", "La Comisión promoverá el interés general de la Unión"), ("vela por la aplicación de los Tratados", "TUE", "Artículo 17", "Velará por que se apliquen los Tratados")])
EX_P14 = examen("P", 14, {
  "a": f"Ninguno de los dos firma: según el art. 297.1, los actos del procedimiento ordinario {cF(297, 'serán firmados por el Presidente del Parlamento Europeo y por el Presidente del Consejo')}.",
  "b": f"Literal del art. 297.1 TFUE: {cF(297, 'serán firmados por el Presidente del Parlamento Europeo y por el Presidente del Consejo')}.",
  "c": f"Cambia un órgano: firma el Presidente del Consejo, no el de la Comisión ({cF(297, 'por el Presidente del Parlamento Europeo y por el Presidente del Consejo')}).",
  "d": f"Cambia un órgano: firma el Presidente del Parlamento Europeo, no el de la Comisión ({cF(297, 'por el Presidente del Parlamento Europeo y por el Presidente del Consejo')})."},
  [("Presidente del Parlamento Europeo y al Presidente del Consejo", "TFUE", "Artículo 297", "serán firmados por el Presidente del Parlamento Europeo y por el Presidente del Consejo")])
EX_X32 = examen("X", 32, {
  "a": f"Cambia el plazo: el art. 15.3 dice {cU(15, 'se reunirá dos veces por semestre por convocatoria de su Presidente')}, no por trimestre.",
  "b": f"Literal del art. 15.4 TUE: {cU(15, 'El Consejo Europeo se pronunciará por consenso, excepto cuando los Tratados dispongan otra cosa')}.",
  "c": f"Es lo contrario del art. 15.6: {cU(15, 'El Presidente del Consejo Europeo no podrá ejercer mandato nacional alguno')}.",
  "d": f"El art. 235.1 TFUE sí admite la delegación: {cF(235, 'cada miembro del Consejo Europeo podrá actuar en representación de uno solo de los demás miembros')}."},
  [("por consenso", "TUE", "Artículo 15", "El Consejo Europeo se pronunciará por consenso, excepto cuando los Tratados dispongan otra cosa")])

T.ap("s20", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **siete** preguntas de este tema: **tres** en el turno libre (L 19, 20 y 21), **tres** en promoción interna (P 11, 13 y 14) y **una** en el extraordinario (X 32). Todas citan el artículo y se resuelven con su **letra**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-L 2025, pregunta 19 · Mandato del Presidente del Consejo Europeo (→ I.3.1)", EX_L19,
  "### GACE-X 2025 (extraordinario), pregunta 32 · Consenso en el Consejo Europeo (→ I.2.2)", EX_X32,
  "### GACE-L 2025, pregunta 20 · COREPER (→ II.2.2)", EX_L20,
  "### GACE-P 2025, pregunta 13 · Funciones de la Comisión (→ III.1.1)", EX_P13,
  "### GACE-P 2025, pregunta 11 · Cese de un comisario (→ III.4.2)", EX_P11,
  "### GACE-L 2025, pregunta 21 · Informe general de la Comisión (→ III.4.3)", EX_L21,
  "### GACE-P 2025, pregunta 14 · Firma de los actos legislativos (→ IV.4.3)", EX_P14,
  "### Cómo se pregunta",
  "!> Las siete preguntas **nombran el artículo** (TUE 15, 16 y 17; TFUE 247, 249 y 297) y cambian **un dato**: un **plazo** (dos años y medio, un mes, dos veces por semestre), una **palabra** («Permanentes», «grave») o un **órgano** (quién firma). Memorizar esos datos literales resuelve el bloque.",
]))

T.ap("s21", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Consejo Europeo | Jefes de Estado o de Gobierno + Presidente + Presidente de la Comisión; impulsos y orientaciones; no legisla (TUE 15) | Presidente: **2 años y medio**, renovable **una vez**; **consenso**; **dos veces por semestre** |
| II. Consejo | Ministros; colegislador y presupuestario; formaciones; COREPER (TUE 16; TFUE 237-243) | Mayoría cualificada **55 % (15) + 65 %**; **72 %** sin propuesta de la Comisión; **COREPER** prepara |
| III. Comisión | Interés general, iniciativa, independencia; nombramiento y moción de censura (TUE 17; TFUE 244-250) | **Cinco años**; un comisario **por Estado** (Decisión 2013/272/UE); cese por el **TJ**; informe **un mes** antes |
| IV. Procedimiento | Ordinario y especiales (289); propuesta (293); art. 294; firma y publicación (297) | **3 + 3 meses**, **6 + 6 semanas**; firma de los Presidentes del **PE** y del **Consejo**; **veinte días** |
| V. Estados miembros | Parlamentos nacionales; Comisión Mixta; CARUE (Protocolos 1 y 2; Leyes 8/1994 y 2/1997) | **Ocho semanas** (dictamen); **cuatro semanas** (Parlamentos autonómicos); umbrales **1/3**, **1/4**, mayoría simple |

?> **Trampas frecuentes:** «el Consejo Europeo ejerce la función legislativa» (**no** la ejerce: TUE 15.1); «el Presidente del Consejo Europeo, cinco años» (son **dos años y medio**); «el Consejo Europeo se reúne dos veces al **trimestre**» (por **semestre**); «Comité de Representantes **Especiales**» (son **Permanentes**); «la Comisión **representa a los Estados**» (promueve el **interés general**); «cese por falta **leve**» (falta **grave**); «firman los Presidentes de la **Comisión** y del Parlamento» (del **Parlamento** y del **Consejo**); «la Comisión tiene **dos tercios** de los Estados» (el Consejo Europeo lo cambió: **uno por Estado**).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
q = T.q
q("TUE", "Artículo 13", "Marco institucional", "Según el artículo 13.1 del Tratado de la Unión Europea, ¿cuál de los siguientes NO figura entre las instituciones de la Unión?",
  ["El Comité de las Regiones.", "El Consejo Europeo.", "El Banco Central Europeo.", "El Tribunal de Cuentas."],
  "Art. 13 TUE: el Comité Económico y Social y el Comité de las Regiones asisten con funciones consultivas (13.4); no son instituciones.", ["— El Consejo Europeo,", "— El Banco Central Europeo,", "— El Tribunal de Cuentas.", "un Comité de las Regiones que ejercerán funciones consultivas"])
q("TUE", "Artículo 15", "Consejo Europeo", "Según el artículo 15.1 del Tratado de la Unión Europea, el Consejo Europeo:",
  ["No ejercerá función legislativa alguna.", "Ejercerá la función legislativa conjuntamente con el Parlamento Europeo.", "Ejercerá la función legislativa conjuntamente con el Consejo.", "Ejercerá la función legislativa en los casos de urgencia."],
  "Art. 15.1 TUE: da impulsos y define orientaciones; «No ejercerá función legislativa alguna».", "No ejercerá función legislativa alguna")
q("TUE", "Artículo 15", "Consejo Europeo", "Según el artículo 15.2 del Tratado de la Unión Europea, el Consejo Europeo estará compuesto por los Jefes de Estado o de Gobierno de los Estados miembros, así como:",
  ["Por su Presidente y por el Presidente de la Comisión.", "Por su Presidente y por el Alto Representante de la Unión para Asuntos Exteriores y Política de Seguridad.", "Por el Presidente del Parlamento Europeo y por el Presidente de la Comisión.", "Por los Ministros de Asuntos Exteriores."],
  "Art. 15.2 TUE. El Alto Representante «Participará en sus trabajos», pero no es miembro.", "así como por su Presidente y por el Presidente de la Comisión")
q("TUE", "Artículo 15", "Consejo Europeo", "Según el artículo 15.3 del Tratado de la Unión Europea, el Consejo Europeo se reunirá:",
  ["Dos veces por semestre por convocatoria de su Presidente.", "Dos veces al año por convocatoria de su Presidente.", "Una vez al mes por convocatoria del Presidente de la Comisión.", "Cuatro veces por semestre por convocatoria del Consejo de Asuntos Generales."],
  "Art. 15.3 TUE.", "se reunirá dos veces por semestre por convocatoria de su Presidente")
q("TUE", "Artículo 15", "Presidente del Consejo Europeo", "Según el artículo 15.5 del Tratado de la Unión Europea, el Consejo Europeo elegirá a su Presidente:",
  ["Por mayoría cualificada.", "Por unanimidad.", "Por mayoría simple.", "Por consenso."],
  "Art. 15.5 TUE: «por mayoría cualificada para un mandato de dos años y medio».", "El Consejo Europeo elegirá a su Presidente por mayoría cualificada")
q("TUE", "Artículo 15", "Presidente del Consejo Europeo", "Según el artículo 15.6 del Tratado de la Unión Europea, al término de cada reunión del Consejo Europeo, su Presidente presentará un informe:",
  ["Al Parlamento Europeo.", "Al Consejo.", "A la Comisión.", "A los Parlamentos nacionales."],
  "Art. 15.6 d) TUE.", "al término de cada reunión del Consejo Europeo, presentará un informe al Parlamento Europeo")
q("TFUE", "Artículo 235", "Consejo Europeo", "Según el artículo 235.3 del Tratado de Funcionamiento de la Unión Europea, el Consejo Europeo se pronunciará en las cuestiones de procedimiento y para la aprobación de su reglamento interno:",
  ["Por mayoría simple.", "Por mayoría cualificada.", "Por unanimidad.", "Por consenso."],
  "Art. 235.3 TFUE.", "El Consejo Europeo se pronunciará por mayoría simple en las cuestiones de procedimiento y para la aprobación de su reglamento interno")
q("TFUE", "Artículo 235", "Consejo Europeo", "Según el artículo 235.1 del Tratado de Funcionamiento de la Unión Europea, cuando el Consejo Europeo se pronuncie por votación:",
  ["El Presidente del Consejo Europeo y el Presidente de la Comisión no participarán en las votaciones.", "Solo votará el Presidente del Consejo Europeo en caso de empate.", "El Presidente de la Comisión votará en nombre de la Comisión.", "El Alto Representante votará en asuntos de política exterior."],
  "Art. 235.1 TFUE.", "El Presidente del Consejo Europeo y el Presidente de la Comisión no participarán en las votaciones del Consejo Europeo cuando éste se pronuncie por votación")
q("TUE", "Artículo 16", "Consejo", "Según el artículo 16.2 del Tratado de la Unión Europea, el Consejo estará compuesto por:",
  ["Un representante de cada Estado miembro, de rango ministerial.", "Los Jefes de Estado o de Gobierno de los Estados miembros.", "Un representante de cada Estado miembro elegido por su Parlamento nacional.", "Los Representantes Permanentes de los Estados miembros."],
  "Art. 16.2 TUE.", "un representante de cada Estado miembro, de rango ministerial")
q("TUE", "Artículo 16", "Mayoría cualificada", "Según el artículo 16.4 del Tratado de la Unión Europea, a partir del 1 de noviembre de 2014 la mayoría cualificada se definirá como un mínimo del:",
  ["55 % de los miembros del Consejo que incluya al menos a quince de ellos y represente a Estados miembros que reúnan como mínimo el 65 % de la población de la Unión.", "65 % de los miembros del Consejo que incluya al menos a quince de ellos y represente a Estados miembros que reúnan como mínimo el 55 % de la población de la Unión.", "55 % de los miembros del Consejo que incluya al menos a doce de ellos y represente a Estados miembros que reúnan como mínimo el 60 % de la población de la Unión.", "72 % de los miembros del Consejo que represente a Estados miembros que reúnan como mínimo el 55 % de la población de la Unión."],
  "Art. 16.4 TUE: 55 % de los miembros (al menos quince) y 65 % de la población.", "un mínimo del 55 % de los miembros del Consejo que incluya al menos a quince de ellos y represente a Estados miembros que reúnan como mínimo el 65 % de la población de la Unión")
q("TUE", "Artículo 16", "Mayoría cualificada", "Según el artículo 16.4 del Tratado de la Unión Europea, una minoría de bloqueo estará compuesta por al menos:",
  ["Cuatro miembros del Consejo.", "Tres miembros del Consejo.", "Cinco miembros del Consejo.", "Seis miembros del Consejo."],
  "Art. 16.4 TUE.", "Una minoría de bloqueo estará compuesta por al menos cuatro miembros del Consejo")
q("TUE", "Artículo 16", "Formaciones del Consejo", "Según el artículo 16.6 del Tratado de la Unión Europea, ¿qué formación del Consejo preparará las reuniones del Consejo Europeo?",
  ["El Consejo de Asuntos Generales.", "El Consejo de Asuntos Exteriores.", "El Consejo de Asuntos Económicos y Financieros.", "El Comité de Representantes Permanentes."],
  "Art. 16.6 TUE: el Consejo de Asuntos Generales «Preparará las reuniones del Consejo Europeo».", "Preparará las reuniones del Consejo Europeo")
q("TUE", "Artículo 16", "Consejo", "Según el artículo 16.8 del Tratado de la Unión Europea, el Consejo se reunirá en público:",
  ["Cuando delibere y vote sobre un proyecto de acto legislativo.", "En todas sus sesiones.", "Cuando lo solicite el Parlamento Europeo.", "Solo cuando adopte actos no legislativos."],
  "Art. 16.8 TUE.", "El Consejo se reunirá en público cuando delibere y vote sobre un proyecto de acto legislativo")
q("TUE", "Artículo 16", "Formaciones del Consejo", "Según el artículo 16.9 del Tratado de la Unión Europea, la presidencia de las formaciones del Consejo será desempeñada por los representantes de los Estados miembros mediante un sistema de rotación igual, con excepción de la de:",
  ["Asuntos Exteriores.", "Asuntos Generales.", "Asuntos Económicos y Financieros.", "Justicia y Asuntos de Interior."],
  "Art. 16.9 TUE.", "con excepción de la de Asuntos Exteriores")
q("TFUE", "Artículo 237", "Consejo", "Según el artículo 237 del Tratado de Funcionamiento de la Unión Europea, el Consejo se reunirá por convocatoria de su Presidente, a iniciativa de éste, de uno de sus miembros o:",
  ["De la Comisión.", "Del Parlamento Europeo.", "Del Presidente del Consejo Europeo.", "Del Comité de Representantes Permanentes."],
  "Art. 237 TFUE.", "a iniciativa de éste, de uno de sus miembros o de la Comisión")
q("TFUE", "Artículo 238", "Mayoría cualificada", "Según el artículo 238.2 del Tratado de Funcionamiento de la Unión Europea, cuando el Consejo no actúe a propuesta de la Comisión o del Alto Representante, la mayoría cualificada se definirá como un mínimo del:",
  ["72 % de los miembros del Consejo que represente a Estados miembros que reúnan como mínimo el 65 % de la población de la Unión.", "55 % de los miembros del Consejo que represente a Estados miembros que reúnan como mínimo el 65 % de la población de la Unión.", "72 % de los miembros del Consejo que represente a Estados miembros que reúnan como mínimo el 72 % de la población de la Unión.", "65 % de los miembros del Consejo que represente a Estados miembros que reúnan como mínimo el 72 % de la población de la Unión."],
  "Art. 238.2 TFUE.", "un mínimo del 72 % de los miembros del Consejo que represente a Estados miembros que reúnan como mínimo el 65 % de la población de la Unión")
q("TFUE", "Artículo 238", "Consejo", "Según el artículo 238.1 del Tratado de Funcionamiento de la Unión Europea, cuando deba adoptar un acuerdo por mayoría simple, el Consejo se pronunciará por:",
  ["Mayoría de los miembros que lo componen.", "Mayoría de los miembros presentes.", "Mayoría de los votos emitidos.", "Mayoría de los Estados que representen el 50 % de la población."],
  "Art. 238.1 TFUE.", "el Consejo se pronunciará por mayoría de los miembros que lo componen")
q("TFUE", "Artículo 238", "Consejo", "Según el artículo 238.4 del Tratado de Funcionamiento de la Unión Europea, las abstenciones de los miembros presentes o representados:",
  ["No impedirán la adopción de los acuerdos del Consejo que requieran unanimidad.", "Impedirán la adopción de los acuerdos del Consejo que requieran unanimidad.", "Se computarán como votos negativos.", "Se computarán como votos favorables en la mayoría cualificada."],
  "Art. 238.4 TFUE.", "Las abstenciones de los miembros presentes o representados no impedirán la adopción de los acuerdos del Consejo que requieran unanimidad")
q("TUE", "Artículo 17", "Comisión", "Según el artículo 17.2 del Tratado de la Unión Europea, los actos legislativos de la Unión sólo podrán adoptarse, excepto cuando los Tratados dispongan otra cosa:",
  ["A propuesta de la Comisión.", "A propuesta del Consejo Europeo.", "A propuesta del Parlamento Europeo.", "A propuesta de un tercio de los Estados miembros."],
  "Art. 17.2 TUE.", "Los actos legislativos de la Unión sólo podrán adoptarse a propuesta de la Comisión")
q("TUE", "Artículo 17", "Comisión", "Según el artículo 17.3 del Tratado de la Unión Europea, el mandato de la Comisión será de:",
  ["Cinco años.", "Cuatro años.", "Dos años y medio.", "Seis años."],
  "Art. 17.3 TUE.", "El mandato de la Comisión será de cinco años")
q("DCE2013", "Artículo 1", "Comisión", "Según el artículo 1 de la Decisión 2013/272/UE del Consejo Europeo, la Comisión estará compuesta por un número de miembros:",
  ["Igual al número de Estados miembros, que incluirá a su Presidente y al Alto Representante.", "Correspondiente a los dos tercios del número de Estados miembros.", "Igual al número de Estados miembros, más su Presidente.", "Igual a la mitad del número de Estados miembros, más su Presidente."],
  "Art. 1 de la Decisión 2013/272/UE, que ejerce la facultad del art. 17.5 TUE de modificar el número de dos tercios.", "un número de miembros igual al número de Estados miembros, que incluirá a su Presidente y al Alto Representante")
q("TUE", "Artículo 17", "Nombramiento de la Comisión", "Según el artículo 17.7 del Tratado de la Unión Europea, el Parlamento Europeo elegirá al candidato a Presidente de la Comisión propuesto por el Consejo Europeo:",
  ["Por mayoría de los miembros que lo componen.", "Por mayoría de los votos emitidos.", "Por mayoría de dos tercios.", "Por mayoría cualificada."],
  "Art. 17.7 TUE.", "El Parlamento Europeo elegirá al candidato por mayoría de los miembros que lo componen")
q("TUE", "Artículo 17", "Nombramiento de la Comisión", "Según el artículo 17.7 del Tratado de la Unión Europea, tras el voto de aprobación del Parlamento Europeo, la Comisión será nombrada:",
  ["Por el Consejo Europeo, por mayoría cualificada.", "Por el Consejo, por unanimidad.", "Por el Parlamento Europeo, por mayoría absoluta.", "Por el Consejo Europeo, por unanimidad."],
  "Art. 17.7 TUE.", "la Comisión será nombrada por el Consejo Europeo, por mayoría cualificada")
q("TUE", "Artículo 17", "Comisión", "Según el artículo 17.8 del Tratado de la Unión Europea, la Comisión tendrá una responsabilidad colegiada ante:",
  ["El Parlamento Europeo.", "El Consejo.", "El Consejo Europeo.", "El Tribunal de Justicia de la Unión Europea."],
  "Art. 17.8 TUE.", "La Comisión tendrá una responsabilidad colegiada ante el Parlamento Europeo")
q("TFUE", "Artículo 246", "Comisión", "Según el artículo 246 del Tratado de Funcionamiento de la Unión Europea, el miembro de la Comisión dimisionario, cesado o fallecido será sustituido por el resto de su mandato por un nuevo miembro:",
  ["De la misma nacionalidad, nombrado por el Consejo de común acuerdo con el Presidente de la Comisión.", "De cualquier nacionalidad, nombrado por el Presidente de la Comisión.", "De la misma nacionalidad, elegido por el Parlamento Europeo.", "Propuesto por su Estado y nombrado por el Consejo Europeo por unanimidad."],
  "Art. 246 TFUE: misma nacionalidad, nombrado por el Consejo, de común acuerdo con el Presidente de la Comisión y previa consulta al Parlamento Europeo.", "nuevo miembro de la misma nacionalidad, nombrado por el Consejo, de común acuerdo con el Presidente de la Comisión")
q("TFUE", "Artículo 250", "Comisión", "Según el artículo 250 del Tratado de Funcionamiento de la Unión Europea, los acuerdos de la Comisión se adoptarán:",
  ["Por mayoría de sus miembros.", "Por mayoría de los miembros presentes.", "Por unanimidad.", "Por mayoría de dos tercios de sus miembros."],
  "Art. 250 TFUE; el quórum lo fija su reglamento interno.", "Los acuerdos de la Comisión se adoptarán por mayoría de sus miembros")
q("TFUE", "Artículo 289", "Procedimiento legislativo", "Según el artículo 289.1 del Tratado de Funcionamiento de la Unión Europea, el procedimiento legislativo ordinario consiste en la adopción conjunta de un reglamento, una directiva o una decisión:",
  ["Por el Parlamento Europeo y el Consejo, a propuesta de la Comisión.", "Por el Consejo y la Comisión, a propuesta del Parlamento Europeo.", "Por el Consejo Europeo y el Consejo, a propuesta de la Comisión.", "Por el Parlamento Europeo y la Comisión, a propuesta del Consejo."],
  "Art. 289.1 TFUE.", "la adopción conjunta por el Parlamento Europeo y el Consejo, a propuesta de la Comisión")
q("TFUE", "Artículo 293", "Procedimiento legislativo", "Según el artículo 293.1 del Tratado de Funcionamiento de la Unión Europea, cuando el Consejo se pronuncie a propuesta de la Comisión, únicamente podrá modificar la propuesta:",
  ["Por unanimidad.", "Por mayoría cualificada.", "Por mayoría simple.", "Con el acuerdo del Parlamento Europeo."],
  "Art. 293.1 TFUE (salvo los casos que cita: 294.10 y 13, 310, 312, 314 y 315).", "únicamente podrá modificar la propuesta por unanimidad")
q("TFUE", "Artículo 294", "Procedimiento legislativo ordinario", "Según el artículo 294.7 del Tratado de Funcionamiento de la Unión Europea, si en el plazo de tres meses el Parlamento Europeo no toma decisión alguna sobre la posición del Consejo en primera lectura:",
  ["El acto se considerará adoptado en la formulación correspondiente a la posición del Consejo.", "El acto propuesto se considerará no adoptado.", "Se convocará al Comité de Conciliación.", "La Comisión deberá presentar una nueva propuesta."],
  "Art. 294.7 a) TFUE.", "aprueba la posición del Consejo en primera lectura o no toma decisión alguna, el acto de que se trate se considerará adoptado en la formulación correspondiente a la posición del Consejo")
q("TFUE", "Artículo 294", "Procedimiento legislativo ordinario", "Según el artículo 294.7 del Tratado de Funcionamiento de la Unión Europea, en segunda lectura el Parlamento Europeo podrá rechazar la posición del Consejo en primera lectura:",
  ["Por mayoría de los miembros que lo componen.", "Por mayoría de los votos emitidos.", "Por mayoría de dos tercios de los votos emitidos.", "Por mayoría cualificada."],
  "Art. 294.7 b) TFUE.", "rechaza, por mayoría de los miembros que lo componen, la posición del Consejo en primera lectura")
q("TFUE", "Artículo 294", "Procedimiento legislativo ordinario", "Según el artículo 294.9 del Tratado de Funcionamiento de la Unión Europea, el Consejo se pronunciará por unanimidad sobre las enmiendas del Parlamento Europeo:",
  ["Que hayan sido objeto de un dictamen negativo de la Comisión.", "Que hayan sido aprobadas por mayoría de los votos emitidos.", "Que afecten a la base jurídica del acto.", "Que hayan sido objeto de un dictamen negativo del Comité de las Regiones."],
  "Art. 294.9 TFUE.", "El Consejo se pronunciará por unanimidad sobre las enmiendas que hayan sido objeto de un dictamen negativo de la Comisión")
q("TFUE", "Artículo 294", "Procedimiento legislativo ordinario", "Según el artículo 294.10 del Tratado de Funcionamiento de la Unión Europea, el Comité de Conciliación tendrá por misión alcanzar un acuerdo sobre un texto conjunto en el plazo de:",
  ["Seis semanas a partir de su convocatoria.", "Tres meses a partir de su convocatoria.", "Ocho semanas a partir de su convocatoria.", "Un mes a partir de su convocatoria."],
  "Art. 294.10 TFUE.", "en el plazo de seis semanas a partir de su convocatoria")
q("TFUE", "Artículo 294", "Procedimiento legislativo ordinario", "Según el artículo 294.13 del Tratado de Funcionamiento de la Unión Europea, en tercera lectura el Parlamento Europeo se pronunciará sobre el texto conjunto:",
  ["Por mayoría de los votos emitidos.", "Por mayoría de los miembros que lo componen.", "Por mayoría de dos tercios.", "Por unanimidad."],
  "Art. 294.13 TFUE: el Parlamento, por mayoría de los votos emitidos; el Consejo, por mayoría cualificada.", "pronunciándose el Parlamento Europeo por mayoría de los votos emitidos y el Consejo por mayoría cualificada")
q("TFUE", "Artículo 294", "Procedimiento legislativo ordinario", "Según el artículo 294.14 del Tratado de Funcionamiento de la Unión Europea, los períodos de tres meses y de seis semanas podrán ampliarse, como máximo, en:",
  ["Un mes y dos semanas respectivamente.", "Dos meses y un mes respectivamente.", "Un mes y una semana respectivamente.", "Tres meses y seis semanas respectivamente."],
  "Art. 294.14 TFUE.", "podrán ampliarse, como máximo, en un mes y dos semanas respectivamente")
q("TFUE", "Artículo 297", "Procedimiento legislativo", "Según el artículo 297.1 del Tratado de Funcionamiento de la Unión Europea, a falta de fecha fijada en ellos mismos, los actos legislativos entrarán en vigor:",
  ["A los veinte días de su publicación.", "Al día siguiente de su publicación.", "A los quince días de su publicación.", "A los tres meses de su publicación."],
  "Art. 297.1 TFUE.", "a falta de ella, a los veinte días de su publicación")
q("TUE", "Artículo 11", "Procedimiento legislativo", "Según el artículo 11.4 del Tratado de la Unión Europea, podrá tomar la iniciativa de invitar a la Comisión Europea a que presente una propuesta un grupo de al menos:",
  ["Un millón de ciudadanos de la Unión, nacionales de un número significativo de Estados miembros.", "Quinientos mil ciudadanos de la Unión, nacionales de al menos siete Estados miembros.", "Un millón de ciudadanos de la Unión, nacionales de un mismo Estado miembro.", "Dos millones de ciudadanos de la Unión, nacionales de la mayoría de los Estados miembros."],
  "Art. 11.4 TUE.", "Un grupo de al menos un millón de ciudadanos de la Unión, que sean nacionales de un número significativo de Estados miembros")
q("PROT2", "Artículo 6", "Parlamentos nacionales", "Según el artículo 6 del Protocolo n.º 2 sobre la aplicación de los principios de subsidiariedad y proporcionalidad, todo Parlamento nacional podrá dirigir un dictamen motivado sobre la no conformidad de un proyecto con el principio de subsidiariedad en un plazo de:",
  ["Ocho semanas a partir de la fecha de transmisión del proyecto.", "Seis semanas a partir de la fecha de transmisión del proyecto.", "Tres meses a partir de la fecha de transmisión del proyecto.", "Cuatro semanas a partir de la fecha de transmisión del proyecto."],
  "Art. 6 del Protocolo n.º 2.", "en un plazo de ocho semanas a partir de la fecha de transmisión de un proyecto de acto legislativo")
q("PROT2", "Artículo 7", "Parlamentos nacionales", "Según el artículo 7.2 del Protocolo n.º 2, el proyecto de acto legislativo deberá volverse a estudiar cuando los dictámenes motivados sobre el incumplimiento del principio de subsidiariedad representen, con carácter general, al menos:",
  ["Un tercio del total de votos atribuidos a los Parlamentos nacionales.", "Un cuarto del total de votos atribuidos a los Parlamentos nacionales.", "La mitad del total de votos atribuidos a los Parlamentos nacionales.", "Dos tercios del total de votos atribuidos a los Parlamentos nacionales."],
  "Art. 7.2 del Protocolo n.º 2 (un cuarto solo para el art. 76 TFUE; mayoría simple en el procedimiento ordinario, 7.3).", "representen al menos un tercio del total de votos atribuidos a los Parlamentos nacionales")
q("PROT2", "Artículo 7", "Parlamentos nacionales", "Según el artículo 7.1 del Protocolo n.º 2, en un sistema parlamentario nacional bicameral:",
  ["Cada una de las dos cámaras dispondrá de un voto.", "La cámara baja dispondrá de dos votos.", "Cada una de las dos cámaras dispondrá de dos votos.", "Las dos cámaras deberán votar conjuntamente."],
  "Art. 7.1 del Protocolo n.º 2: cada Parlamento nacional dispone de dos votos.", "En un sistema parlamentario nacional bicameral, cada una de las dos cámaras dispondrá de un voto")
q("PROT1", "Artículo 4", "Parlamentos nacionales", "Según el artículo 4 del Protocolo n.º 1, entre la inclusión de un proyecto de acto legislativo en el orden del día provisional del Consejo y la adopción de una posición deberá transcurrir, salvo en casos urgentes debidamente motivados, un plazo de:",
  ["Diez días.", "Ocho semanas.", "Quince días.", "Seis semanas."],
  "Art. 4 del Protocolo n.º 1 (las ocho semanas son entre la transmisión a los Parlamentos y la inclusión en el orden del día).", "Entre la inclusión de un proyecto de acto legislativo en el orden del día provisional del Consejo y la adopción de una posición deberá transcurrir un plazo de diez días")
q("L8_1994", "a2", "Comisión Mixta para la UE", "Según el artículo 2 de la Ley 8/1994, la Presidencia de la Comisión Mixta para la Unión Europea corresponderá:",
  ["Al Presidente del Congreso de los Diputados o al diputado o senador en quien éste delegue con carácter permanente.", "Al Presidente del Senado o al senador en quien éste delegue.", "Alternativamente, por legislaturas, a los Presidentes del Congreso y del Senado.", "Al Ministro de Asuntos Exteriores."],
  "Art. 2 de la Ley 8/1994.", "La Presidencia de la Comisión corresponderá al Presidente del Congreso de los Diputados o al diputado o senador en quien éste delegue con carácter permanente")
q("L8_1994", "a4", "Comisión Mixta para la UE", "Según el artículo 4 de la Ley 8/1994, el Gobierno comparecerá con posterioridad a cada Consejo Europeo, ordinario o extraordinario, para informar sobre lo allí decidido:",
  ["Ante el Pleno del Congreso de los Diputados.", "Ante la Comisión Mixta para la Unión Europea.", "Ante el Pleno del Senado.", "Ante la Comisión de Asuntos Exteriores del Congreso."],
  "Art. 4 de la Ley 8/1994.", "El Gobierno comparecerá ante el Pleno del Congreso de los Diputados, con posterioridad a cada Consejo Europeo, ordinario o extraordinario")
q("L8_1994", "a6", "Comisión Mixta para la UE", "Según el artículo 6.2 de la Ley 8/1994, el dictamen motivado del Parlamento de una Comunidad Autónoma, para ser tenido en consideración, deberá haberse recibido en el Congreso o en el Senado en el plazo de:",
  ["Cuatro semanas desde la remisión de la iniciativa legislativa europea por las Cortes Generales.", "Ocho semanas desde la remisión de la iniciativa legislativa europea por las Cortes Generales.", "Dos semanas desde la remisión de la iniciativa legislativa europea por las Cortes Generales.", "Seis semanas desde la publicación oficial del acto legislativo europeo."],
  "Art. 6.2 de la Ley 8/1994.", "en el plazo de cuatro semanas desde la remisión de la iniciativa legislativa europea por las Cortes Generales")
q("L8_1994", "a7", "Comisión Mixta para la UE", "Según el artículo 7.2 de la Ley 8/1994, la Comisión Mixta para la Unión Europea podrá solicitar del Gobierno la interposición de un recurso de anulación por infracción del principio de subsidiariedad en el plazo máximo de:",
  ["Seis semanas desde la publicación oficial del acto legislativo europeo.", "Ocho semanas desde la publicación oficial del acto legislativo europeo.", "Dos meses desde la publicación oficial del acto legislativo europeo.", "Cuatro semanas desde la publicación oficial del acto legislativo europeo."],
  "Art. 7.2 de la Ley 8/1994.", "En el plazo máximo de seis semanas desde la publicación oficial de un acto legislativo europeo")
q("L2_1997", "a1", "CARUE", "Según el artículo 1.2 de la Ley 2/1997, la Conferencia para Asuntos Relacionados con las Comunidades Europeas debe garantizar la participación efectiva de las Comunidades Autónomas:",
  ["En la fase de formación de la voluntad del Estado ante las instituciones comunitarias y en la ejecución del Derecho comunitario.", "En las votaciones del Consejo de la Unión Europea.", "En la elección de los miembros españoles de la Comisión Europea.", "En el control de la subsidiariedad en lugar de las Cortes Generales."],
  "Art. 1.2 de la Ley 2/1997.", "en la fase de formación de la voluntad del Estado ante las instituciones comunitarias y en la ejecución del Derecho comunitario")

for cod, n, cat in [("L", 19, "Presidente del Consejo Europeo"), ("X", 32, "Consejo Europeo"), ("L", 20, "Consejo"), ("P", 13, "Comisión"), ("P", 11, "Comisión"), ("L", 21, "Comisión"), ("P", 14, "Procedimiento legislativo")]:
    T.real(cod, n, cat)

# Flashcards
for q_, a_, cat in [
  ("¿Cuáles son las siete instituciones de la Unión? (TUE 13)", "Parlamento Europeo, Consejo Europeo, Consejo, Comisión, TJUE, BCE y Tribunal de Cuentas.", "Marco institucional"),
  ("¿Quién compone el Consejo Europeo? (TUE 15.2)", "Jefes de Estado o de Gobierno, su Presidente y el Presidente de la Comisión; participa el Alto Representante.", "Consejo Europeo"),
  ("¿Legisla el Consejo Europeo? (TUE 15.1)", "No: da impulsos y define orientaciones; «No ejercerá función legislativa alguna».", "Consejo Europeo"),
  ("¿Cada cuánto se reúne el Consejo Europeo y cómo decide? (TUE 15.3 y 4)", "Dos veces por semestre; por consenso, salvo que los Tratados dispongan otra cosa.", "Consejo Europeo"),
  ("Presidente del Consejo Europeo: elección y mandato (TUE 15.5)", "Mayoría cualificada; dos años y medio, renovable una sola vez; sin mandato nacional (15.6).", "Presidente del Consejo Europeo"),
  ("Composición del Consejo (TUE 16.2)", "Un representante de cada Estado, de rango ministerial, facultado para comprometer a su Gobierno y votar.", "Consejo"),
  ("Mayoría cualificada (TUE 16.4)", "55 % de los miembros (al menos 15) que representen al menos el 65 % de la población; minoría de bloqueo: al menos 4.", "Mayoría cualificada"),
  ("Mayoría cualificada sin propuesta de la Comisión (TFUE 238.2)", "72 % de los miembros + 65 % de la población.", "Mayoría cualificada"),
  ("¿Quién prepara los trabajos del Consejo? ¿Y las reuniones del Consejo Europeo?", "COREPER (TUE 16.7; TFUE 240) / Consejo de Asuntos Generales (TUE 16.6).", "Formaciones del Consejo"),
  ("¿Cuándo es pública la sesión del Consejo? (TUE 16.8)", "Cuando delibera y vota sobre un proyecto de acto legislativo.", "Consejo"),
  ("Funciones de la Comisión (TUE 17.1)", "Interés general, velar por la aplicación de los Tratados, ejecutar el presupuesto, coordinación y gestión, representación exterior (salvo PESC).", "Comisión"),
  ("Mandato y número de miembros de la Comisión", "Cinco años (TUE 17.3); uno por Estado miembro (Decisión 2013/272/UE).", "Comisión"),
  ("Nombramiento de la Comisión (TUE 17.7)", "Consejo Europeo propone (MC) → PE elige al Presidente (mayoría de miembros) → Consejo adopta la lista → aprobación colegiada del PE → nombra el Consejo Europeo (MC).", "Nombramiento de la Comisión"),
  ("Cese de un comisario (TFUE 247)", "Por el Tribunal de Justicia, a instancia del Consejo (mayoría simple) o de la Comisión: falta grave o pérdida de condiciones.", "Comisión"),
  ("Informe general de la Comisión (TFUE 249.2)", "Cada año, al menos un mes antes de la apertura del período de sesiones del Parlamento Europeo.", "Comisión"),
  ("¿Cómo puede el Consejo modificar la propuesta de la Comisión? (TFUE 293.1)", "Solo por unanimidad, salvo en conciliación y tercera lectura y en los casos presupuestarios citados.", "Procedimiento legislativo"),
  ("Plazos del procedimiento legislativo ordinario (TFUE 294)", "2.ª lectura: 3 meses (PE) y 3 meses (Consejo); conciliación: 6 semanas; 3.ª lectura: 6 semanas; ampliables 1 mes y 2 semanas.", "Procedimiento legislativo ordinario"),
  ("¿Quién firma los actos del procedimiento ordinario? (TFUE 297.1)", "El Presidente del Parlamento Europeo y el Presidente del Consejo.", "Procedimiento legislativo"),
  ("Dictamen motivado de subsidiariedad (Protocolo n.º 2, art. 6)", "Cada Parlamento nacional o cámara, en ocho semanas desde la transmisión del proyecto.", "Parlamentos nacionales"),
  ("Umbrales del Protocolo n.º 2 (art. 7)", "1/3 de los votos (general); 1/4 (art. 76 TFUE); mayoría simple en el procedimiento ordinario.", "Parlamentos nacionales"),
  ("Comisión Mixta para la UE: quién la preside (Ley 8/1994, art. 2)", "El Presidente del Congreso o el diputado o senador en quien delegue con carácter permanente.", "Comisión Mixta para la UE"),
  ("Plazos de la Ley 8/1994", "Dictamen de las Cortes: 8 semanas; Parlamentos autonómicos: 4 semanas; solicitud de recurso de anulación: 6 semanas; informe del Gobierno sobre subsidiariedad: 2 semanas.", "Comisión Mixta para la UE"),
  ("CARUE (Ley 2/1997)", "Órgano de cooperación Estado–CC. AA. para la formación de la voluntad del Estado y la ejecución del Derecho de la Unión.", "CARUE"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Consejo Europeo", "Institución formada por los Jefes de Estado o de Gobierno, su Presidente y el Presidente de la Comisión; da los impulsos y define las orientaciones políticas de la Unión, sin función legislativa (TUE 15).", "s2", "Instituciones")
T.glos("Consejo", "Institución formada por un representante de rango ministerial de cada Estado; ejerce con el Parlamento Europeo la función legislativa y presupuestaria (TUE 16).", "s5", "Instituciones")
T.glos("Comisión Europea", "Institución que promueve el interés general de la Unión, vela por la aplicación de los Tratados y tiene, por regla general, la iniciativa legislativa (TUE 17).", "s8", "Instituciones")
T.glos("Mayoría cualificada", "Desde el 1-11-2014: 55 % de los miembros del Consejo (al menos 15) que representen al menos el 65 % de la población; 72 % de los miembros si no hay propuesta de la Comisión o del Alto Representante (TUE 16.4; TFUE 238.2).", "s5", "Consejo")
T.glos("Minoría de bloqueo", "Al menos cuatro miembros del Consejo; sin ella, la mayoría cualificada se considera alcanzada (TUE 16.4).", "s5", "Consejo")
T.glos("COREPER", "Comité de Representantes Permanentes de los Gobiernos de los Estados miembros: prepara los trabajos del Consejo (TUE 16.7; TFUE 240).", "s6", "Consejo")
T.glos("Formaciones del Consejo", "Configuraciones del Consejo por materias; Asuntos Generales y Asuntos Exteriores están en el TUE (16.6) y la lista de las demás la adopta el Consejo Europeo (TFUE 236).", "s6", "Consejo")
T.glos("Moción de censura", "Votación del Parlamento Europeo contra la Comisión; si se aprueba, sus miembros dimiten colectivamente (TUE 17.8; TFUE 234).", "s10", "Comisión")
T.glos("Procedimiento legislativo ordinario", "Adopción conjunta por el Parlamento Europeo y el Consejo, a propuesta de la Comisión, de un reglamento, directiva o decisión; se regula en el art. 294 TFUE (TFUE 289.1).", "s12", "Procedimiento")
T.glos("Procedimiento legislativo especial", "Adopción de un acto por el Parlamento Europeo con participación del Consejo, o por el Consejo con participación del Parlamento, en los casos previstos (TFUE 289.2).", "s12", "Procedimiento")
T.glos("Comité de Conciliación", "Órgano de miembros del Consejo y un número igual de representantes del Parlamento Europeo que busca un texto conjunto en seis semanas (TFUE 294.10).", "s14", "Procedimiento")
T.glos("Dictamen motivado", "Escrito de un Parlamento nacional o de una cámara que expone por qué un proyecto no se ajusta al principio de subsidiariedad; plazo de ocho semanas (Protocolo n.º 2, art. 6).", "s17", "Estados miembros")
T.glos("Comisión Mixta para la Unión Europea", "Comisión del Congreso y del Senado que canaliza la participación de las Cortes en los asuntos de la Unión y emite el dictamen de subsidiariedad en su nombre (Ley 8/1994).", "s18", "Estados miembros")
T.glos("CARUE", "Conferencia para Asuntos Relacionados con las Comunidades Europeas (hoy, con la Unión Europea): órgano de cooperación entre el Estado y las Comunidades Autónomas para los asuntos europeos (Ley 2/1997).", "s19", "Estados miembros")

# Cronología (fechas de los metadatos del BOE y de EUR-Lex)
T.hito("1994", "Ley 8/1994, de 19 de mayo, por la que se regula la Comisión Mixta para la Unión Europea (BOE de 20-5-1994)", "Comisión Mixta de Congreso y Senado para los asuntos de la Unión", "normativo", "s18")
T.hito("1997", "Ley 2/1997, de 13 de marzo, por la que se regula la Conferencia para Asuntos Relacionados con las Comunidades Europeas (BOE de 15-3-1997)", "Participación de las Comunidades Autónomas en los asuntos europeos", "normativo", "s19")
T.hito("2005", "Acuerdos de la CARUE de 9 de diciembre de 2004 (BOE de 16-3-2005)", "Representación autonómica en formaciones del Consejo y en sus grupos de trabajo", "normativo", "s19")
T.hito("2009", "Ley 24/2009, de 22 de diciembre, de modificación de la Ley 8/1994 para su adaptación al Tratado de Lisboa de 13 de diciembre de 2007 (BOE de 23-12-2009)", "Control de la subsidiariedad por las Cortes y recurso de anulación", "normativo", "s18")
T.hito("2010", "Ley 38/2010, de 20 de diciembre, de modificación de la Ley 8/1994 (BOE de 21-12-2010)", "Comparecencias del Gobierno ante la Comisión Mixta y de los Gobiernos autonómicos", "normativo", "s18")
T.hito("2013", "Decisión 2013/272/UE del Consejo Europeo, de 22 de mayo de 2013 (DOUE L 165 de 18-6-2013)", "La Comisión, con un miembro por Estado miembro (aplicable desde el 1-11-2014)", "normativo", "s9")
T.hito("2014", "1 de noviembre de 2014: nueva definición de la mayoría cualificada (TUE, art. 16.4)", "Doble mayoría: 55 % de los miembros del Consejo y 65 % de la población", "normativo", "s5")

T.publicar()
