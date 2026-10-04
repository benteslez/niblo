# -*- coding: utf-8 -*-
"""Tema VI.2 (B6T02): Las leyes anuales de presupuestos. Su contenido. El presupuesto del
Estado. Principios de programación y de gestión. Contenido, elaboración y estructura.
Desglose de aplicaciones presupuestarias.
Método del I.2. Normas (textos consolidados del BOE): CE, arts. 66.2, 75.3, 79.2 y 134;
Ley 47/2003, General Presupuestaria (arts. 26 a 44); LO 2/2012 (art. 30); Reglamento del
Congreso (arts. 79.1 y 133 a 135); Reglamento del Senado (arts. 148 a 150); Orden
HAC/557/2026 (normas de elaboración de los PGE para 2027); Resolución de 20 de enero de
2014 de la Dirección General de Presupuestos (clasificación económica); Orden de 1 de
febrero de 1996 (documentos contables) y Orden de 1 de febrero de 1996 (Instrucción de
operatoria contable, reglas 9 y 10)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO.update({"RES2014": "Resolución de 20-1-2014", "OPGE27": "Orden HAC/557/2026", "RCD": "Reglamento del Congreso",
              "RS": "Reglamento del Senado", "ODOC": "Orden de 1-2-1996, documentos contables",
              "OIOC": "Orden de 1-2-1996, Instrucción de operatoria contable"})

A2 = "Anexo II (Resolución de 20 de enero de 2014, de la Dirección General de Presupuestos): clasificación económica del gasto"
OA1 = "Anexo I (Orden HAC/557/2026): clasificación por programas de gasto"
DOC = "Anexo I (Orden de 1 de febrero de 1996, documentos contables): normas de cumplimentación"

T = Tema("B6T02",
  "Cinco preguntas: I. Qué es la Ley de Presupuestos y qué contiene (arts. 66.2, 75.3 y 134 CE; LGP, arts. 32 a 34 y 38) · II. Con qué principios se programa y se gestiona (LGP, arts. 26 a 29 y 31) · III. Cómo se elabora y se aprueba (CE, arts. 79.2 y 134.3, 5 y 6; LGP, arts. 36 y 37; LO 2/2012, art. 30; Orden HAC/557/2026; Reglamentos del Congreso y del Senado) · IV. Cómo se estructura (LGP, arts. 35 y 39 a 44; Orden HAC/557/2026, art. 6) · V. Cómo se lee y se desglosa una aplicación presupuestaria (documentos contables, Instrucción de operatoria contable, Orden HAC/557/2026, anexo I, y Resolución de 20-1-2014). Cada artículo: texto literal del BOE y ficha.",
  ["Art. 134 CE", "Ley de Presupuestos", "Prórroga", "Beneficios fiscales", "Programación plurianual", "Escenarios presupuestarios", "Límite de gasto no financiero", "1 de octubre", "Comisión de Políticas de Gasto", "Clasificación orgánica", "Clasificación por programas", "Clasificación económica", "Programas finalistas", "Especificación", "Aplicación presupuestaria", "Desglose", "Reasignación"])

# =============================================================================
T.ap("s0", "Mapa del tema: cinco preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque VI, tema 2):
> Las leyes anuales de presupuestos. Su contenido. El presupuesto del Estado. Principios de programación y de gestión. Contenido, elaboración y estructura. Desglose de aplicaciones presupuestarias.

### El hilo conductor

El epígrafe se lee como **cinco preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Constitución | Otras normas |
|---|---|---|---|
| **I** | ¿Qué es la Ley de Presupuestos y qué contiene? | Arts. 66.2, 75.3 y 134 | LGP, arts. 32, 33, 34 y 38 |
| **II** | ¿Con qué principios se programa y se gestiona el presupuesto? | — | LGP, arts. 26 a 29 y 31 |
| **III** | ¿Cómo se elabora y se aprueba? | Arts. 79.2 y 134.3, 5 y 6 | LGP, arts. 36 y 37; LO 2/2012, art. 30; Orden HAC/557/2026, arts. 4 y 5; Reglamento del Congreso, arts. 79.1 y 133 a 135; Reglamento del Senado, arts. 148 a 150 |
| **IV** | ¿Cómo se estructura? (clasificaciones y especificación) | — | LGP, arts. 35 y 39 a 44; Orden HAC/557/2026, art. 6 y anexo I |
| **V** | ¿Cómo se lee y se desglosa una aplicación presupuestaria? | — | Orden de 1-2-1996 de documentos contables (anexo I y apartado sexto); Orden de 1-2-1996 de operatoria contable (reglas 9 y 10); Orden HAC/557/2026, anexo I, y Resolución de 20-1-2014, anexo II (extractos) |

!> **La idea que une los cinco bloques:** la Constitución reserva a una **ley anual** —que elabora el **Gobierno** y aprueban las **Cortes**— la totalidad de los gastos e ingresos del sector público estatal (I). Esa ley se **programa** en escenarios plurianuales y se **gestiona** con créditos de finalidad específica (II); se **elabora** por un procedimiento que fija la LGP y desarrolla cada año una orden del Ministro de Hacienda (III); se **estructura** en tres clasificaciones —orgánica, por programas y económica— (IV), y la combinación de las tres da la **aplicación presupuestaria**, que los gestores pueden **desglosar** al ejecutar (V).

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- La orden de elaboración que se cita es la **vigente**: Orden HAC/557/2026 (presupuestos para 2027), que derogó la de 2026. Sus fechas concretas valen para ese ejercicio.
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- El régimen de las modificaciones de crédito es del tema VI.3; la ejecución del gasto y los documentos contables, del tema VI.5; los capítulos 2, 4, 6 y 7 en detalle, del tema VI.6.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué es la Ley de Presupuestos y qué contiene? (arts. 66.2, 75.3 y 134 CE; LGP, arts. 32 a 34 y 38)", donde(
  "Primera pregunta del tema. La Constitución dedica un artículo entero, el **134**, a los Presupuestos Generales del Estado: quién los hace, qué deben contener, qué no pueden hacer y qué pasa si no se aprueban a tiempo. La LGP lo completa.",
  ["1 Quién los elabora y quién los aprueba (arts. 66.2, 75.3 y 134.1)", "2 Contenido constitucional: anualidad, totalidad, beneficios fiscales y tributos (art. 134.2 y 7)", "3 El presupuesto en la LGP: definición, contenido y ejercicio (arts. 32 a 34)", "4 La prórroga (art. 134.4 CE; LGP, art. 38)"]))

T.ap("s1", "I.1 Quién elabora y quién aprueba los Presupuestos (arts. 66.2, 75.3 y 134.1)", f"""
La Ley de Presupuestos reparte el trabajo entre dos poderes: el **Gobierno** la elabora y las **Cortes** la examinan, enmiendan y aprueban.

{unidad("1.1 Las Cortes aprueban los Presupuestos (art. 66.2)",
  lit("CE", "Artículo 66", ["aprueban sus Presupuestos"], solo=[2]),
  fichab("Competencia de las Cortes sobre los Presupuestos del Estado",
         c("CE", "Artículo 66", "Las Cortes Generales"),
         "Junto a la potestad legislativa y el control del Gobierno, la aprobación de los Presupuestos es función propia de las Cortes",
         "—",
         "La aprobación es de las **Cortes Generales** (Congreso y Senado), no del Gobierno ni solo del Congreso."))}

{unidad("1.2 No cabe delegarlos en Comisión (art. 75.3)",
  lit("CE", "Artículo 75", ["los Presupuestos Generales del Estado"], solo=[3]),
  fichab("Excepción a la delegación en las Comisiones Legislativas Permanentes",
         "Las Cámaras (en Pleno)",
         f"La aprobación de los Presupuestos no puede delegarse en las Comisiones (art. 75.2), como {c('CE', 'Artículo 75', 'la reforma constitucional, las cuestiones internacionales, las leyes orgánicas y de bases')}",
         "—",
         "Los Presupuestos **siempre** pasan por el **Pleno**. Es otra pregunta clásica junto a leyes orgánicas y de bases (tema IV.2)."))}

{unidad("1.3 Reparto de papeles: Gobierno y Cortes (art. 134.1)",
  lit("CE", "Artículo 134", ["Corresponde al Gobierno la elaboración", "a las Cortes Generales, su examen, enmienda y aprobación"], solo=[1]),
  fichab("Distribución constitucional de funciones sobre los Presupuestos",
         ["Gobierno: **elaboración**", "Cortes Generales: **examen, enmienda y aprobación**"],
         "El Gobierno presenta el proyecto (→ III.3); las Cortes lo tramitan como ley (→ III.4)",
         "—",
         "La **enmienda** es de las **Cortes**, no del Consejo de Ministros. Cayó en 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s2", "I.2 Contenido constitucional: anualidad, totalidad, beneficios fiscales y tributos (art. 134.2 y 7)", f"""
Dos apartados del art. 134 dicen **qué tiene que estar** en la Ley de Presupuestos y **qué no puede hacer**.

{unidad("2.1 Anuales, completos y con los beneficios fiscales (art. 134.2)",
  lit("CE", "Artículo 134", ["carácter anual", "la totalidad de los gastos e ingresos del sector público estatal", "el importe de los beneficios fiscales que afecten a los tributos del Estado"], solo=[2]),
  fichab("Contenido mínimo de los Presupuestos Generales del Estado",
         "—",
         ["Carácter **anual**", "**Todos** los gastos e ingresos del **sector público estatal**", "El importe de los **beneficios fiscales** que afecten a los tributos del Estado"],
         "Un año (el ejercicio coincide con el año natural: LGP, art. 34 → I.3.3)",
         "Tres rasgos en una frase: anual, **totalidad** (gastos **e** ingresos) y **beneficios fiscales** de los tributos **del Estado**."))}

{unidad("2.2 No pueden crear tributos (art. 134.7)",
  lit("CE", "Artículo 134", ["no puede crear tributos", "cuando una ley tributaria sustantiva así lo prevea"], solo=[7]),
  fichab("Límite material de la Ley de Presupuestos en materia tributaria",
         "Las Cortes, al aprobar la Ley de Presupuestos",
         ["**Crear** tributos: nunca", "**Modificarlos**: solo si una **ley tributaria sustantiva** lo prevé"],
         "—",
         "Crear: **no**. Modificar: **sí, con habilitación** de una ley tributaria sustantiva. Cayó en 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s3", "I.3 El presupuesto en la LGP: definición, contenido y ejercicio (arts. 32 a 34)", f"""
La LGP desarrolla el art. 134 CE: define los Presupuestos, dice quién se integra en ellos y qué determinan, y fija el ejercicio.

{unidad("3.1 Definición (LGP, art. 32)",
  lit("LGP", "Artículo 32", ["expresión cifrada, conjunta y sistemática de los derechos y obligaciones a liquidar durante el ejercicio"]),
  fichab("Qué son los Presupuestos Generales del Estado",
         f"{c('LGP', 'Artículo 32', 'cada uno de los órganos y entidades que forman parte del sector público estatal')}",
         "Expresan en cifras los **derechos y obligaciones** a liquidar durante el ejercicio",
         "—",
         "Tres adjetivos: **cifrada, conjunta y sistemática**. Se habla de derechos y obligaciones **a liquidar** en el ejercicio."))}

{unidad("3.2 Quién se integra y qué determinan (LGP, art. 33)",
  lit("LGP", "Artículo 33", ["Los presupuestos estimativos", "como máximo", "Los objetivos a alcanzar en el ejercicio", "La estimación de los beneficios fiscales"]),
  fichab("Alcance subjetivo y contenido de los Presupuestos Generales del Estado",
         ["::Integran los PGE (33.1):", "a) Presupuestos **limitativos**: órganos del art. 2.3 y entidades con régimen de especificaciones y modificaciones de la LGP o con presupuesto limitativo por su norma", "b) Presupuestos **estimativos**: sectores empresarial y fundacional, consorcios, universidades no transferidas, fondos sin personalidad jurídica y resto del sector público administrativo"],
         ["::Determinan (33.2):", "Las obligaciones que **como máximo** pueden reconocer los sujetos con presupuesto limitativo", "Los derechos a reconocer", "Las operaciones no financieras y financieras de las entidades con presupuesto estimativo", "Los **objetivos** de cada gestor de programas", "La estimación de los **beneficios fiscales**"],
         "—",
         "Limitativo = las obligaciones son un **máximo** (art. 46: los créditos son limitativos). Las entidades empresariales y fundacionales tienen presupuesto **estimativo**."))}

{unidad("3.3 El ejercicio presupuestario (LGP, art. 34.1)",
  lit("LGP", "Artículo 34", ["coincidirá con el año natural", "cualquiera que sea el período del que deriven", "hasta el fin del mes de diciembre"], solo=[1, 2, 3]),
  fichab("Ámbito temporal del presupuesto",
         "—",
         ["Ejercicio = **año natural**", "Derechos: los **liquidados** en el ejercicio, cualquiera que sea su origen temporal", "Obligaciones: las **reconocidas hasta fin de diciembre** por gastos realizados en el ejercicio"],
         "Año natural; obligaciones reconocidas hasta el **31 de diciembre**",
         "Derechos: criterio de **liquidación**, sin importar el período del que deriven. Obligaciones: **reconocidas** hasta fin de diciembre **y** por gastos del propio ejercicio. Las excepciones (atrasos de personal, sentencias, obligaciones de ejercicios anteriores) están en el resto del art. 34."))}
""", 2)

T.ap("s4", "I.4 La prórroga de los Presupuestos (art. 134.4 CE; LGP, art. 38)", f"""
{unidad("4.1 Prórroga automática (art. 134.4)",
  lit("CE", "Artículo 134", ["antes del primer día del ejercicio económico correspondiente", "automáticamente prorrogados"], solo=[4]),
  fichab("Qué ocurre si la Ley de Presupuestos no está aprobada a 1 de enero",
         "—",
         "Se prorrogan **automáticamente** los Presupuestos del ejercicio anterior, sin necesidad de acuerdo",
         "Hasta la aprobación de los nuevos",
         "El hito es el **primer día del ejercicio**, no «tres meses antes» (ese es el plazo de **presentación** del art. 134.3 → III.3.1). Cayó en 2025 (→ Cierre 1)."))}

{unidad("4.2 Alcance de la prórroga (LGP, art. 38)",
  lit("LGP", "Artículo 38", ["presupuestos iniciales del ejercicio anterior", "La prórroga no afectará", "sin alteración de la cuantía total"]),
  fichab("Reglas de la prórroga presupuestaria",
         f"Criterios de aplicación: {c('LGP', 'Artículo 38', 'El Consejo de Ministros, a propuesta del Ministerio de Hacienda')}",
         ["Se prorrogan los presupuestos **iniciales** del ejercicio anterior", "No se prorrogan los créditos de programas o actuaciones que **terminen** en el ejercicio ni los de obligaciones que se extingan en él", "La estructura **orgánica** se adapta a la organización vigente, **sin alterar la cuantía total**"],
         f"{c('LGP', 'Artículo 38', 'hasta la aprobación y publicación de los nuevos')}",
         "La LGP precisa lo que la CE no dice: se prorrogan los **iniciales** (no los modificados durante el año) y hasta la aprobación **y publicación** de los nuevos."))}

{resumen([
  "El **Gobierno** elabora; las **Cortes** examinan, enmiendan y aprueban (134.1 y 66.2); nunca en Comisión (75.3).",
  "Contenido: **anual**, **totalidad** de gastos e ingresos del sector público estatal y **beneficios fiscales** (134.2); no pueden **crear** tributos, solo modificarlos si lo prevé una ley tributaria sustantiva (134.7).",
  "LGP: expresión **cifrada, conjunta y sistemática** (32); presupuestos **limitativos** y **estimativos** (33); ejercicio = **año natural** (34).",
  "Sin ley el **1 de enero**: prórroga **automática** de los presupuestos **iniciales** (134.4 CE y 38 LGP)."],
  "Siguiente: II. ¿Con qué principios se programa y se gestiona el presupuesto?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Con qué principios se programa y se gestiona el presupuesto? (LGP, arts. 26 a 29 y 31)", donde(
  "Segunda pregunta. El epígrafe pide los «Principios de programación y de gestión». La LGP los recoge en el capítulo I de su título II (arts. 26 y 27); el capítulo II (arts. 28 a 31) regula los instrumentos de la programación plurianual.",
  ["1 Principios de programación y de gestión (arts. 26 y 27)", "2 Escenarios y programas plurianuales; asignación y objetivos (arts. 28, 29 y 31)"]))

T.ap("s5", "II.1 Principios y reglas de programación y de gestión (LGP, arts. 26 y 27)", f"""
{unidad("1.1 Principios de programación (art. 26)",
  lit("LGP", "Artículo 26", ["estabilidad presupuestaria, sostenibilidad financiera, plurianualidad, transparencia, eficiencia en la asignación y utilización de los recursos públicos, responsabilidad y lealtad institucional", "supeditarse de forma estricta a las disponibilidades presupuestarias"]),
  fichab("Principios que rigen la programación presupuestaria",
         "Todos los sujetos del sector público estatal (normas en elaboración, actos, contratos, convenios…)",
         ["::Principios (26.1), conforme a la LO 2/2012:", "Estabilidad presupuestaria", "Sostenibilidad financiera", "Plurianualidad", "Transparencia", "Eficiencia en la asignación y utilización de los recursos públicos", "Responsabilidad y lealtad institucional", "::Regla (26.2): valorar repercusiones y efectos y supeditarse a las disponibilidades y a los escenarios plurianuales"],
         "—",
         "Son **siete** principios y remiten a la **LO 2/2012** (tema VI.1). La regla del 26.2 alcanza también a las **disposiciones en fase de elaboración**."))}

{unidad("1.2 Principios de gestión (art. 27)",
  lit("LGP", "Artículo 27", ["régimen de presupuesto anual aprobado por las Cortes Generales y enmarcado en los límites de un escenario plurianual", "exclusivamente a la finalidad específica", "El carácter limitativo y vinculante de dichos créditos será el correspondiente al nivel de especificación", "salvo que por ley se establezca su afectación a fines determinados", "por su importe íntegro"], solo=[1, 2, 3, 4, 5, 9]),
  fichab("Reglas de la gestión presupuestaria",
         "Administración General del Estado, organismos autónomos y entidades con presupuesto limitativo",
         ["Presupuesto **anual** aprobado por las Cortes, dentro de un escenario **plurianual** (27.1)", "Créditos para su **finalidad específica**; limitativos y vinculantes al **nivel de especificación** (27.2 → IV.3)", "Los recursos financian el **conjunto** de las obligaciones, salvo **afectación por ley** (27.3)", "Derechos y obligaciones por su **importe íntegro**, sin minorar derechos para atender obligaciones salvo autorización expresa de la ley (27.4)", "Información suficiente para verificar principios y objetivos (27.5)"],
         "—",
         f"La regla del 27.2 es la que el art. 42 rotula {c('LGP', 'Artículo 42', 'Especialidad de los créditos')} (→ IV.3.1). La **afectación** de recursos a fines determinados exige **ley** (27.3)."))}
""", 2)

T.ap("s6", "II.2 Escenarios y programas plurianuales; asignación y objetivos (LGP, arts. 28, 29 y 31)", f"""
{unidad("2.1 Escenarios presupuestarios plurianuales (art. 28)",
  lit("LGP", "Artículo 28", ["referidos a los tres ejercicios siguientes", "serán confeccionados por el Ministerio de Hacienda", "un escenario de ingresos y un escenario de gastos"], solo=[1, 3, 4]),
  fichab("Programación plurianual del sector público estatal con presupuesto limitativo",
         f"{c('LGP', 'Artículo 28', 'serán confeccionados por el Ministerio de Hacienda')}, que da cuenta al **Consejo de Ministros** antes de aprobar el proyecto de Ley de Presupuestos",
         ["Definen los equilibrios básicos, la evolución de ingresos y los recursos de las políticas de gasto", "Se ajustan al objetivo de estabilidad (LO 2/2012, art. 15)", "Dos escenarios: **ingresos** y **gastos**"],
         "Límites referidos a los **tres ejercicios siguientes**",
         "**Tres** ejercicios. Los confecciona **Hacienda**; el Consejo de Ministros recibe cuenta, no los aprueba."))}

{unidad("2.2 Programas plurianuales ministeriales (art. 29)",
  lit("LGP", "Artículo 29", ["referidos a los tres ejercicios siguientes", "se aprobará por el Ministro", "Los indicadores de ejecución"], solo=[1, 3, 6, 7, 8, 9, 10, 11]),
  fichab("Desarrollo de los escenarios por ministerios y centros gestores",
         ["Cada **ministerio**: programa plurianual que **aprueba el Ministro**", "Seguridad Social: programa propio (art. 29.3)", "Centros gestores: sus programas se integran en el del ministerio (art. 30)"],
         ["::Contenido (29.6):", "Objetivos plurianuales claros y mensurables", "Actividad a realizar", "Medios económicos, materiales y personales", "Inversiones reales y financieras", "Indicadores de ejecución (eficacia, eficiencia, economía y calidad)"],
         "Tres ejercicios siguientes; se remiten **anualmente** a Hacienda (29.2)",
         "Los programas plurianuales los aprueba el **Ministro** del departamento; los escenarios los confecciona **Hacienda**."))}

{unidad("2.3 Asignación presupuestaria y objetivos (art. 31)",
  lit("LGP", "Artículo 31", ["se adecuarán a los escenarios presupuestarios plurianuales", "el nivel de cumplimiento de los objetivos en ejercicios anteriores", "Los objetivos de carácter instrumental"]),
  fichab("Cómo se asignan los créditos a los gestores",
         "Gobierno (restricciones de política económica); centros gestores (destinatarios)",
         ["Los PGE se adecuan a los **escenarios** y atienden a los objetivos de los programas plurianuales", "Para asignar se tiene en cuenta el **cumplimiento de objetivos** de ejercicios anteriores", "Los objetivos **instrumentales** se ponen en relación con los **finales**"],
         "—",
         "Presupuestar por **objetivos**: el cumplimiento pasado cuenta para la asignación futura."))}

{resumen([
  "Programación (26): estabilidad, sostenibilidad, **plurianualidad**, transparencia, eficiencia, responsabilidad y lealtad institucional.",
  "Gestión (27): presupuesto **anual** en escenario **plurianual**; créditos a su **finalidad específica**, vinculantes al **nivel de especificación**; recursos sin afectación salvo **ley**; importes **íntegros**.",
  "Escenarios plurianuales de **tres** ejercicios, confeccionados por **Hacienda** (28); programas plurianuales aprobados por cada **Ministro** (29 y 30); asignación según objetivos (31)."],
  "Siguiente: III. ¿Cómo se elabora y se aprueba?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Cómo se elabora y se aprueba? (CE, arts. 79.2 y 134.3, 5 y 6; LGP, arts. 36 y 37; LO 2/2012, art. 30; Orden HAC/557/2026; Reglamentos de las Cámaras)", donde(
  "Tercera pregunta. Del techo de gasto al Boletín Oficial: la fase **gubernamental** (límite de gasto, directrices, propuestas, anteproyecto) y la fase **parlamentaria** (remisión antes del 1 de octubre, tramitación en Congreso y Senado).",
  ["1 El límite de gasto no financiero (LGP, art. 36.1; LO 2/2012, art. 30)", "2 El procedimiento de elaboración (LGP, art. 36.2 a 5; Orden HAC/557/2026, arts. 4 y 5)", "3 Presentación y documentación (art. 134.3 CE; LGP, art. 37)", "4 Tramitación parlamentaria y mayoría (arts. 79.2 y 134.5 y 6 CE; Reglamentos del Congreso y del Senado)"]))

T.ap("s7", "III.1 El límite de gasto no financiero (LGP, art. 36.1; LO 2/2012, art. 30)", f"""
{unidad("1.1 El techo de gasto (LGP, art. 36.1; LO 2/2012, art. 30.1 y 2)",
  lit("LGP", "Artículo 36", ["límite de gasto no financiero"], solo=[1]),
  lit("LOEP", "a30", ["un límite máximo de gasto no financiero", "techo de asignación de recursos", "Antes del 1 de agosto de cada año"], solo=[1, 2, 3]),
  fichab("Primer paso de la elaboración: el límite de gasto no financiero del Estado",
         f"El Estado (y también las CC. AA. y las Corporaciones Locales en sus ámbitos); el Ministerio de Hacienda informa al {c('LOEP', 'a30', 'Consejo de Política Fiscal y Financiera')}",
         ["Coherente con el **objetivo de estabilidad** y la **regla de gasto**", "Marca el **techo** de asignación de recursos", "Excluye las transferencias de los sistemas de financiación autonómica y local"],
         f"{c('LOEP', 'a30', 'Antes del 1 de agosto de cada año')}",
         "El límite es de gasto **no financiero**. Información al CPFF **antes del 1 de agosto**. La LGP no lo regula: remite a la **LO 2/2012**."))}
""", 2)

T.ap("s8", "III.2 El procedimiento de elaboración (LGP, art. 36.2 a 5; Orden HAC/557/2026, arts. 4 y 5)", f"""
{unidad("2.1 Las normas de la LGP (art. 36.2 a 5)",
  lit("LGP", "Artículo 36", ["por orden del Ministro de Hacienda", "Comisión de Políticas de Gasto", "remitirán al Ministerio de Hacienda sus correspondientes propuestas de presupuesto", "memoria de objetivos anuales", "Corresponderá al Ministro de Hacienda elevar al acuerdo del Gobierno"], solo=[2, 3, 4, 5, 6, 7, 13, 14, 15, 16, 17]),
  fichab("Fase gubernamental: de las directrices al anteproyecto",
         ["**Ministro de Hacienda**: dicta la orden de elaboración, fija las directrices y eleva el anteproyecto al Gobierno", "**Comisión de Políticas de Gasto**: criterios y prioridades", "**Ministerios** y órganos con dotación diferenciada: remiten sus propuestas (y las de sus organismos y entidades)", "**Gobierno**: acuerda el anteproyecto"],
         ["Primera: directrices de distribución del gasto (Ministro de Hacienda; Comisión de Políticas de Gasto)", "Segunda: propuestas de los ministerios, ajustadas a los límites", "Tercera: cada programa, con su **memoria de objetivos anuales**", "Cuarta: especificaciones de la Seguridad Social por orden de su Ministro", "El presupuesto de **ingresos** lo elabora el **Ministerio de Hacienda** (36.3)"],
         "Los plazos los fija la orden de elaboración (36.4)",
         "El procedimiento se regula por **orden del Ministro de Hacienda** (no por real decreto). El apartado 2 conserva denominaciones ministeriales antiguas: la orden vigente nombra los actuales."))}

{unidad("2.2 Las comisiones del proceso (Orden HAC/557/2026, art. 4)",
  lit("OPGE27", "a4", ["presidida por la persona titular del Ministerio de Hacienda", "reuniones bilaterales entre el Ministerio de Hacienda y los distintos departamentos ministeriales", "Actuará como presidente de las Comisiones de Análisis de Programas la persona titular de la Secretaría de Estado de Presupuestos y Gastos"], solo=[1, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13]),
  fichab("Órganos colegiados que intervienen en la elaboración",
         ["**Comisión de Políticas de Gasto**: preside el titular del **Ministerio de Hacienda** (en su ausencia, el de la Secretaría de Estado de Presupuestos y Gastos); la integran los titulares de los ministerios (o de sus subsecretarías); secretario: Subdirección General de Política Presupuestaria", "**Comisiones de Análisis de Programas**: una por ministerio; preside el titular de la **Secretaría de Estado de Presupuestos y Gastos** (en su ausencia, el de la Dirección General de Presupuestos)"],
         "Las de Análisis de Programas son **reuniones bilaterales** Hacienda-ministerio sobre la adecuación de los programas a sus objetivos y sus necesidades financieras",
         "—",
         "Ojo a las presidencias: Políticas de Gasto → **Ministro/a de Hacienda**; Análisis de Programas → **Secretaría de Estado de Presupuestos y Gastos**."))}

{unidad("2.3 Del anteproyecto al Gobierno (Orden HAC/557/2026, art. 5)",
  lit("OPGE27", "a5", ["La Dirección General de Presupuestos elaborará los estados de gastos", "se elevarán a la persona titular del Ministerio de Hacienda, quien someterá al acuerdo del Gobierno"], solo=[1, 2, 3]),
  fichab("Elaboración y tramitación del anteproyecto",
         ["**Dirección General de Presupuestos**: elabora los estados de gastos (y los de ingresos con las previsiones que coordina la Secretaría de Estado de Presupuestos y Gastos)", "**Ministro/a de Hacienda**: lo somete al Gobierno"],
         "Teniendo en cuenta el límite de gasto no financiero, las prioridades de la Comisión de Políticas de Gasto, las conclusiones de las Comisiones de Análisis de Programas y las propuestas de los centros gestores",
         f"Para 2027, las propuestas de los centros gestores se remitían {c('OPGE27', 'a7', 'antes del 29 de junio de 2026')} (art. 7.1)",
         "Quien **elabora** los estados es la **Dirección General de Presupuestos**; quien los **eleva** al Gobierno, el **Ministro de Hacienda** (LGP, art. 36.5)."))}
""", 2)

T.ap("s9", "III.3 Presentación a las Cortes y documentación (art. 134.3 CE; LGP, art. 37)", f"""
{unidad("3.1 Plazo constitucional (art. 134.3)",
  lit("CE", "Artículo 134", ["ante el Congreso de los Diputados", "al menos tres meses antes de la expiración de los del año anterior"], solo=[3]),
  fichab("Presentación del proyecto de Presupuestos",
         f"{c('CE', 'Artículo 134', 'El Gobierno deberá presentar ante el Congreso de los Diputados')}",
         "Como proyecto de ley, ante el **Congreso** (la Cámara donde empieza su tramitación)",
         "**Al menos tres meses** antes de que expiren los del año anterior",
         "El de «tres meses antes» es el plazo de **presentación**, no el de aprobación (si no se aprueban **antes del 1 de enero**, prórroga → I.4.1)."))}

{unidad("3.2 Remisión y documentación complementaria (LGP, art. 37)",
  lit("LGP", "Artículo 37", ["antes del día 1 de octubre del año anterior", "El informe de impacto de género", "Una memoria de los beneficios fiscales"]),
  fichab("Qué se remite a las Cortes y cuándo",
         "El Gobierno remite; las **Cortes Generales** reciben",
         ["Proyecto: **articulado con sus anexos** y **estados de ingresos y de gastos**, con la especificación de los arts. 40 y 41", "::Documentación complementaria (37.2), entre otras:", "Memorias de los programas y sus objetivos", "Informes de impacto de **género**, en la **infancia, la adolescencia y la familia** y de alineamiento con los **ODS**", "Anexo plurianual de proyectos de **inversión** con clasificación territorial", "Liquidación del año anterior y avance del corriente", "Estados consolidados, informe económico y financiero y memoria de **beneficios fiscales**"],
         "Antes del **1 de octubre** del año anterior",
         "La LGP concreta el plazo: **1 de octubre** (coherente con los «tres meses» del 134.3 CE). La documentación **acompaña**: no forma parte del proyecto que se vota."))}
""", 2)

T.ap("s10", "III.4 Tramitación parlamentaria y mayoría (arts. 79.2 y 134.5 y 6 CE; Reglamentos del Congreso y del Senado)", f"""
{unidad("4.1 Mayoría: la regla general (art. 79.2 CE; Reglamento del Congreso, art. 79.1)",
  lit("CE", "Artículo 79", ["la mayoría de los miembros presentes"], solo=[2]),
  lit("RCD", "art79", ["la mayoría simple de los miembros presentes"], solo=[1]),
  fichab("Mayoría para aprobar la Ley de Presupuestos",
         "El Pleno del Congreso",
         "Ninguna norma exige para los Presupuestos una mayoría especial: rige la regla general",
         f"{c('RCD', 'art79', 'mayoría simple de los miembros presentes')}",
         "**Mayoría simple**. La Ley de Presupuestos no es ley orgánica (la mayoría absoluta del Congreso es del art. 81.2). Cayó en 2025 (→ Cierre 1)."))}

{unidad("4.2 Leyes de gasto e iniciativas que alteran el presupuesto (art. 134.5 y 6)",
  lit("CE", "Artículo 134", ["el Gobierno podrá presentar proyectos de ley que impliquen aumento del gasto público o disminución de los ingresos", "aumento de los créditos o disminución de los ingresos presupuestarios requerirá la conformidad del Gobierno"], solo=[5, 6]),
  fichab("Protección del presupuesto aprobado frente a iniciativas que lo desequilibren",
         ["**Gobierno**: puede presentar proyectos que aumenten el gasto o disminuyan los ingresos (134.5)", "Proposiciones y enmiendas: necesitan la **conformidad del Gobierno** si aumentan créditos o disminuyen ingresos (134.6)"],
         "Veto presupuestario del Gobierno a la **tramitación**",
         "En el Senado, la comunicación del Gobierno sobre proposiciones de ley: diez días (RS, art. 151.3)",
         "La conformidad se exige para el **aumento** de créditos o la **disminución** de ingresos (no para «disminución de créditos»). Cayó en 2025 (→ Cierre 1)."))}

{unidad("4.3 Especialidades en el Congreso (Reglamento del Congreso, arts. 133 a 135)",
  lit("RCD", "art133", ["procedimiento legislativo común", "gozará de preferencia en la tramitación", "proponen una baja de igual cuantía en la misma Sección", "requerirán la conformidad del Gobierno"]),
  lit("RCD", "art134", ["tendrá lugar en el Pleno de la Cámara", "quedarán fijadas las cuantías globales de los estados de los Presupuestos", "diferenciando el conjunto del articulado de la ley y cada una de sus Secciones"]),
  lit("RCD", "art135", ["Entes Públicos"]),
  fichab("Procedimiento legislativo común con especialidades",
         "Pleno del Congreso (debate de totalidad y debate final) y **Comisión de Presupuestos**",
         ["**Preferencia** sobre los demás trabajos de la Cámara", "Enmiendas que **aumenten** créditos: solo con **baja de igual cuantía en la misma Sección**", "Enmiendas que **minoren ingresos**: conformidad del Gobierno", "Debate de **totalidad** en Pleno: fija las **cuantías globales** de los estados", "Debate final: articulado y **cada Sección** por separado"],
         "—",
         "La baja compensatoria debe ser en la **misma Sección**. Las cuantías globales quedan fijadas en el debate de **totalidad**."))}

{unidad("4.4 Especialidades en el Senado (Reglamento del Senado, arts. 148 a 150)",
  lit("RS", "Artículo 148", ["gozará de preferencia en la tramitación"]),
  lit("RS", "Artículo 149", ["mediante una propuesta de veto", "una baja de igual cuantía en la misma sección"]),
  lit("RS", "Artículo 150", ["se dará por concluida la tramitación"]),
  fichab("Tramitación en el Senado",
         "Mesa (oída la Junta de Portavoces, calendario), Pleno y Comisión competente",
         ["Preferencia y procedimiento ordinario con especialidades", "La impugnación de una **sección** se formula como **propuesta de veto**", "Enmiendas que aumentan crédito: baja de igual cuantía en la misma sección", "Si se aprueba un veto, concluye la tramitación del proyecto en el Senado"],
         "—",
         "En el Senado, la impugnación de una sección es un **veto**, no una enmienda."))}

{resumen([
  "Primero, el **límite de gasto no financiero** (LO 2/2012, art. 30); el CPFF es informado **antes del 1 de agosto**.",
  "Procedimiento por **orden del Ministro de Hacienda**; directrices y **Comisión de Políticas de Gasto**; propuestas de los ministerios; la **DG de Presupuestos** elabora y el **Ministro de Hacienda** eleva el anteproyecto al Gobierno (LGP 36; Orden HAC/557/2026).",
  "Presentación ante el **Congreso** al menos **tres meses** antes (134.3 CE): **antes del 1 de octubre** (LGP 37).",
  "Aprobación por **mayoría simple**; enmiendas que aumentan créditos, con **baja en la misma Sección**; las que minoran ingresos o las proposiciones que aumentan créditos, con **conformidad del Gobierno**."],
  "Siguiente: IV. ¿Cómo se estructura el presupuesto?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Cómo se estructura el presupuesto? (LGP, arts. 35 y 39 a 44; Orden HAC/557/2026, art. 6)", donde(
  "Cuarta pregunta. Los créditos se ordenan con **tres clasificaciones** del gasto —orgánica (quién gasta), por programas (para qué) y económica (en qué)— y dos del ingreso. Además, la LGP fija a qué **nivel** se especifican y vinculan los créditos.",
  ["1 Créditos y programas presupuestarios (LGP, art. 35)", "2 Las clasificaciones del gasto y del ingreso (LGP, arts. 39 a 41; Orden HAC/557/2026, art. 6)", "3 Especialidad y especificación de los créditos (LGP, arts. 42 a 44)"]))

T.ap("s11", "IV.1 Créditos y programas presupuestarios (LGP, art. 35)", f"""
{unidad("1.1 Qué es un crédito y qué es un programa (art. 35)",
  lit("LGP", "Artículo 35", ["asignaciones individualizadas de gasto", "de acuerdo con la agrupación orgánica, por programas y económica", "programas de apoyo", "Constituye un programa de gasto del presupuesto anual"]),
  fichab("Las dos piezas básicas del estado de gastos",
         "Centros gestores (créditos a su disposición; responsables de los programas)",
         ["**Crédito**: asignación **individualizada** de gasto, especificada por las agrupaciones **orgánica, por programas y económica**", "**Programa plurianual**: conjunto de gastos para objetivos preestablecidos (producir bienes y servicios, cumplir obligaciones específicas u otras actividades)", "**Programas de apoyo**: actividades horizontales e instrumentales", "**Programa de gasto anual**: concreción anual del plurianual"],
         "Cumplimiento: por **resultados** si son mensurables; si no, por **indicadores** de medición indirecta",
         "El crédito se especifica combinando las **tres** agrupaciones: es la base de la **aplicación presupuestaria** (→ V.1)."))}
""", 2)

T.ap("s12", "IV.2 Las clasificaciones del gasto y del ingreso (LGP, arts. 39 a 41; Orden HAC/557/2026, art. 6)", f"""
{unidad("2.1 Quién determina la estructura (LGP, art. 39)",
  lit("LGP", "Artículo 39", ["por el Ministerio de Hacienda"]),
  fichab("Competencia para fijar la estructura presupuestaria",
         c("LGP", "Artículo 39", "el Ministerio de Hacienda"),
         "Atendiendo a tres criterios: la **organización** del sector público estatal, la **naturaleza económica** de ingresos y gastos y las **finalidades y objetivos**",
         "—",
         "Los tres criterios del art. 39 son las tres clasificaciones del art. 40: **orgánica**, **económica** y **por programas**."))}

{unidad("2.2 Las tres clasificaciones del gasto (LGP, art. 40)",
  lit("LGP", "Artículo 40", ["por secciones y servicios", "La clasificación por programas", "que agrupará los créditos por capítulos separando las operaciones corrientes, las de capital, las financieras y el Fondo de Contingencia de ejecución presupuestaria", "Los capítulos se desglosarán en artículos y estos, a su vez, en conceptos que podrán dividirse en subconceptos", "clasificación funcional"]),
  fichab("Estructura de los estados de gastos de los presupuestos limitativos",
         "—",
         ["**Orgánica**: por **secciones y servicios**, según los centros gestores", "**Por programas**: créditos agrupados por objetivos, adecuados a las **políticas de gasto** de la programación plurianual", "**Económica**: por **capítulos** (operaciones corrientes, de capital, financieras y Fondo de Contingencia) → artículos → conceptos → subconceptos", "Además, identificación **funcional** según la finalidad (40.2)"],
         "—",
         "Cada clasificación «agrupa» de forma distinta: la **orgánica**, por secciones y servicios; la **económica**, por capítulos; la **por programas**, por objetivos y políticas de gasto. Cayó en 2025 (→ Cierre 1)."))}

{unidad("2.3 Estructura de programas: finalistas e instrumentales (Orden HAC/557/2026, art. 6.1.1)",
  lit("OPGE27", "a6", ["programas de gasto de carácter finalista de los programas instrumentales y de gestión", "Los programas finalistas son aquellos a los que se puede asignar objetivos cuantificables e indicadores de ejecución mensurables", "o el apoyo a un programa finalista", "grupos de programas, políticas de gasto y áreas de gasto"], solo=[3, 4, 5, 6, 7]),
  lit("OPGE27", "ai", ["las letras «A» a »L» identifican a los programas finalistas"], solo=[3], titulo=OA1),
  fichab("Cómo se clasifican los programas de gasto",
         "Dirección General de Presupuestos (puede modificar código, denominación y contenido de los programas)",
         ["**Finalistas**: objetivos **cuantificables** e indicadores **mensurables** (cuarto carácter del código: **A a L**)", "**Instrumentales y de gestión** (cuarto carácter: **M a Z**): administrar recursos de ordenación, regulación y planificación; actividades que se perfeccionan por su propia realización; o **apoyo** a un programa finalista", "Agrupación: **programa → grupo de programas → política de gasto → área de gasto** (anexo I)"],
         "—",
         "Las tres finalidades de los programas **instrumentales** son los distractores típicos de la definición de programa **finalista**. Cayó en 2025 (→ Cierre 1)."))}

{unidad("2.4 Estructura orgánica y económica en la orden (Orden HAC/557/2026, art. 6.1.2 y 1.3)",
  lit("OPGE27", "a6", ["que se dividirá en secciones y éstas a su vez en servicios", "clasificación por capítulos, artículos, conceptos y subconceptos"], solo=[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]),
  fichab("Subsectores de la clasificación orgánica y naturaleza económica de los créditos",
         "Centros gestores: unidades orgánicas con diferenciación presupuestaria y responsabilidad en la gestión",
         ["::Clasificación orgánica por subsectores:", "a) El **Estado**: secciones → servicios", "b) Organismos autónomos", "c) Seguridad Social", "d) Agencias estatales y resto del sector público administrativo con presupuesto limitativo", "::Económica: capítulos, artículos, conceptos y subconceptos (anexo II de la orden; códigos en la Resolución de 20-1-2014 → V.1.2)"],
         "—",
         "Solo el subsector **Estado** se divide en **secciones y servicios**; los organismos se agrupan por el ministerio de adscripción."))}

{unidad("2.5 Las clasificaciones del ingreso (LGP, art. 41)",
  lit("LGP", "Artículo 41", ["siguiendo las clasificaciones orgánica y económica", "impuestos directos y cotizaciones sociales"]),
  fichab("Estructura de los estados de ingresos",
         "—",
         ["Solo **dos** clasificaciones: **orgánica** y **económica** (no por programas)", "Corrientes: impuestos directos y cotizaciones sociales, impuestos indirectos, tasas, precios públicos y otros ingresos, transferencias corrientes e ingresos patrimoniales", "De capital: enajenación de inversiones reales y transferencias de capital", "Financieras: activos y pasivos financieros"],
         "—",
         "Los ingresos **no** tienen clasificación **por programas**: los programas son del gasto."))}
""", 2)

T.ap("s13", "IV.3 Especialidad y especificación de los créditos (LGP, arts. 42 a 44)", f"""
{unidad("3.1 Especialidad (LGP, art. 42)",
  lit("LGP", "Artículo 42", ["exclusivamente a la finalidad específica"]),
  fichab("Principio de especialidad de los créditos",
         "Todos los gestores de créditos para gastos",
         "El crédito solo puede usarse para la finalidad autorizada por la Ley de Presupuestos o por sus modificaciones conforme a la LGP",
         "—",
         "Repite la regla del art. 27.2 (→ II.1.2). Cambiar la finalidad exige una **modificación** de crédito (tema VI.3)."))}

{unidad("3.2 Nivel de especificación en el presupuesto del Estado (LGP, art. 43)",
  lit("LGP", "Artículo 43", ["a nivel de concepto", "que se especificarán a nivel de artículo", "las inversiones reales a nivel de capítulo", "Los créditos extraordinarios que se concedan durante el ejercicio"]),
  fichab("A qué nivel aparecen (y vinculan) los créditos del Estado",
         "—",
         ["Regla general: **concepto**", "Gastos de **personal** y **bienes y servicios**: **artículo**", "**Inversiones reales**: **capítulo**", "::Al nivel de su concreta clasificación económica (43.2):", "Atenciones protocolarias y representativas y gastos reservados", "Arrendamientos de edificios y otras construcciones", "Créditos ampliables", "Créditos con perceptor o beneficiario identificado (salvo transferencias al exterior)", "Los que fije la Ley de Presupuestos", "Créditos extraordinarios"],
         "—",
         "Personal y capítulo 2 → **artículo**; inversiones → **capítulo**; lo demás → **concepto**. Cayó dos veces en 2025 (P 87 y L 96, → Cierre 1)."))}

{unidad("3.3 Organismos autónomos y Seguridad Social (LGP, art. 44)",
  lit("LGP", "Artículo 44", ["que se especificarán a nivel de capítulo", "a nivel de grupo de programas"], solo=[1, 2, 3, 4, 5, 6, 7, 8, 9]),
  fichab("Especificación en organismos autónomos, Seguridad Social y entidades del art. 3.1",
         "—",
         ["Regla general: **concepto**", "Personal, bienes y servicios e inversiones reales: **capítulo** (en el Estado, personal y bienes y servicios van a nivel de artículo)", "Mismas excepciones que el art. 43.2 (sin gastos reservados)", "Seguridad Social: **grupo de programas**; acción protectora no contributiva y universal: **programa**"],
         "—",
         "La diferencia con el Estado está en **personal** y **bienes y servicios**: artículo en el Estado, **capítulo** en los organismos autónomos."))}

{resumen([
  "Crédito = asignación individualizada de gasto especificada por las clasificaciones orgánica, por programas y económica (35).",
  "Gasto: **orgánica** (secciones y servicios), **por programas** (objetivos; finalistas A-L e instrumentales M-Z) y **económica** (capítulos → artículos → conceptos → subconceptos). Ingreso: solo orgánica y económica (40 y 41).",
  "Especificación en el Estado: **concepto**; personal y bienes y servicios, **artículo**; inversiones, **capítulo** (43). En organismos autónomos, las tres, **capítulo** (44)."],
  "Siguiente: V. ¿Cómo se lee y se desglosa una aplicación presupuestaria?")}
""", 2)

# =============================================================================
T.ap("bV", "V. ¿Cómo se lee y se desglosa una aplicación presupuestaria? (Orden de 1-2-1996 de documentos contables; Instrucción de operatoria contable, reglas 9 y 10; Orden HAC/557/2026, anexo I; Resolución de 20-1-2014)", donde(
  "Quinta pregunta. La combinación de las tres clasificaciones identifica cada crédito: es la **aplicación presupuestaria** que figura en los documentos contables. El gestor puede **crear** aplicaciones y **desglosarlas** a más nivel que el aprobado, sin alterar la vinculación.",
  ["1 Cómo se lee una aplicación presupuestaria (documentos contables, anexo I; Orden HAC/557/2026, anexo I; Resolución de 20-1-2014)", "2 Creación y desglose de aplicaciones; reasignación (Instrucción de operatoria contable, reglas 9 y 10; documentos contables, apartado sexto)", "3 Cuadro para leer una aplicación (esquema)"]))

T.ap("s14", "V.1 Cómo se lee una aplicación presupuestaria", f"""
La LGP no define la «aplicación presupuestaria». Los campos que la componen están en las normas de cumplimentación de los documentos contables del presupuesto de gastos.

{unidad("1.1 Los campos del documento contable (Orden de 1-2-1996, anexo I, notas 12 a 15)",
  lit("ODOC", "ani", ["Sección", "código del servicio en los dos primeros dígitos", "clasificación por programas", "clasificación económica"], solo=[96, 97, 98, 100], titulo=DOC),
  fichab("Elementos que identifican el crédito en cada operación",
         "El servicio gestor que expide el documento; la oficina de contabilidad que lo registra",
         ["**Sección** (clasificación orgánica): código numérico y literal", "**Orgánica**: el **servicio** en los dos primeros dígitos (y, si hay desglose, las unidades dependientes)", "**Programa**: clasificación por programas", "**Económica**: clasificación económica (en el documento de desglose, el concepto o subconcepto que se desglosa)"],
         "—",
         "En el orden de los campos del documento: **sección**, **servicio**, **programa** y **económica**. Así se leen las aplicaciones de las preguntas de examen (→ V.3)."))}

{unidad("1.2 Programas y códigos económicos que se preguntan (Orden HAC/557/2026, anexo I; Resolución de 20-1-2014, anexo II)",
  lit("OPGE27", "ai", ["112 A Tribunales de Justicia y Ministerio Fiscal", "231 B Acciones en favor de los emigrantes"], solo=[5, 14, 15, 80, 82], titulo=OA1 + " (extracto)"),
  lit("RES2014", "ai-2", ["12. Funcionarios", "120. Retribuciones básicas", "240. Gastos de edición y distribución", "48. A familias e instituciones sin fines de lucro"], solo=[14, 26, 27, 98, 169, 174, 175, 210, 219], titulo=A2 + " (extracto)"),
  fichab("Cómo se leen los códigos de programa y de la clasificación económica",
         "—",
         ["Programa: **tres cifras** (política y grupo de programas) + **letra** (programa): 112A, 231B…", "Económica: **una** cifra = capítulo; **dos** = artículo; **tres** = concepto; las dos de un **subconcepto** se añaden al concepto (120.05)"],
         "—",
         "**120** es un **concepto** (retribuciones básicas de **funcionarios**, artículo 12, capítulo 1); **240**, también concepto (artículo 24). El **48** es el artículo de transferencias corrientes a familias e instituciones sin fines de lucro."))}
""", 2)

T.ap("s15", "V.2 Creación y desglose de aplicaciones; reasignación (Instrucción de operatoria contable, reglas 9 y 10; documentos contables, apartado sexto)", f"""
{unidad("2.1 Crear una aplicación sin dotación (regla 9)",
  lit("OIOC", "regla9", ["dentro del mismo nivel de vinculación", "sin necesidad de efectuar una operación de transferencia de crédito"], solo=[1]),
  fichab("Imputar gastos a una aplicación que no figura en contabilidad",
         "El **servicio gestor** la solicita a la **oficina de contabilidad** (y da cuenta a la oficina presupuestaria)",
         "Cabe cuando existe dotación en el mismo **nivel de vinculación**; la solicitud puede sustituirse por una diligencia en el primer documento contable",
         "—",
         "No hace falta **transferencia de crédito**: el crédito ya vincula a ese nivel (→ IV.3.2)."))}

{unidad("2.2 Desglose y reasignación (regla 10)",
  lit("OIOC", "regla10", ["que puede afectar a cualesquiera de las clasificaciones orgánica, funcional o económica", "a un mayor nivel de desagregación que el que figuraba en el presupuesto aprobado, sin perjuicio del nivel de vinculación jurídica", "documento de «Desglose»", "reasignar crédito entre aplicaciones desglosadas, dentro del mismo nivel de desglose"]),
  fichab("Ejecutar los créditos con más detalle que el aprobado",
         "**Servicios gestores** (expiden el documento); oficina de contabilidad (registra); oficina presupuestaria del Departamento (recibe comunicación)",
         ["**Desglose**: más desagregación en cualquiera de las clasificaciones orgánica, funcional o económica", "**Reasignación**: reponer crédito a la aplicación origen o moverlo entre aplicaciones desglosadas del **mismo nivel de desglose**"],
         "—",
         "El desglose **no** cambia la **vinculación jurídica** del crédito ni es una modificación presupuestaria."))}

{unidad("2.3 El documento contable de desglose (Orden de 1-2-1996, apartado sexto.1 b)",
  lit("ODOC", "sexto", ["Documento de desglose: Se utilizará en las operaciones de desglose de las aplicaciones presupuestarias"], solo=[3]),
  fichab("Soporte contable del desglose",
         "Servicios gestores",
         ["Operaciones de **desglose** de aplicaciones", "Seguimiento de créditos distribuidos a **servicios periféricos** (delegaciones y desconcentraciones)"],
         "—",
         "Se llama literalmente **«Documento de desglose»**; la reasignación tiene su propio documento **«Reasignación»** (apartado sexto.1 m). Cayó en 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s16", "V.3 Cuadro para leer una aplicación presupuestaria (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal. Los ejemplos son las aplicaciones de las preguntas oficiales de 2025.*

| Campo (documento contable) | Clasificación | Ejemplo 13.91.112A.240 | Ejemplo 15.01.231B.120 |
|---|---|---|---|
| Sección | Orgánica (LGP, art. 40.1 a) | **13** | **15** |
| Servicio | Orgánica | 91 | 01 |
| Programa | Por programas (LGP, art. 40.1 b) | 112A (letra A: finalista) | 231B (letra B: finalista) |
| Económica | Económica (LGP, art. 40.1 c) | 240 (concepto) | 120 (concepto: retribuciones básicas de funcionarios) |

!> Leer de izquierda a derecha: **quién** gasta (sección y servicio) → **para qué** (programa) → **en qué** (económica).

{resumen([
  "La aplicación presupuestaria combina **sección, servicio, programa y económica** (documentos contables, notas 12 a 15).",
  "Letra del programa: **A-L finalista**, **M-Z instrumental y de gestión**; económica: 1 cifra capítulo, 2 artículo, 3 concepto, + 2 subconcepto.",
  "Se pueden **crear** aplicaciones en el mismo nivel de vinculación sin transferencia (regla 9) y **desglosar** a más nivel sin cambiar la vinculación, con el **documento de desglose** (regla 10; apartado sexto.1 b)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_P85 = examen("P", 85, {
  "a": f"Literal del art. 134.7: la Ley de Presupuestos {c('CE', 'Artículo 134', 'Podrá modificarlos cuando una ley tributaria sustantiva así lo prevea')}.",
  "b": f"Cambia el órgano: la enmienda es de las Cortes. {c('CE', 'Artículo 134', 'Corresponde al Gobierno la elaboración de los Presupuestos Generales del Estado y a las Cortes Generales, su examen, enmienda y aprobación')}.",
  "c": f"Mezcla dos plazos. El de «tres meses antes» es el de presentación (134.3); la prórroga se produce {c('CE', 'Artículo 134', 'Si la Ley de Presupuestos no se aprobara antes del primer día del ejercicio económico correspondiente')} (134.4).",
  "d": f"Cambia «aumento» por «disminución»: requiere conformidad {c('CE', 'Artículo 134', 'Toda proposición o enmienda que suponga aumento de los créditos o disminución de los ingresos presupuestarios')} (134.6)."},
  [("cuando una ley tributaria sustantiva así lo prevea", "CE", "Artículo 134", "Podrá modificarlos cuando una ley tributaria sustantiva así lo prevea")])
EX_X89 = examen("X", 89, {
  "a": f"Ninguna norma exige mayoría especial para los Presupuestos; rige la general: {c('RCD', 'art79', 'deberán ser aprobados por la mayoría simple de los miembros presentes')} (Reglamento del Congreso, art. 79.1; CE, art. 79.2).",
  "b": f"La mayoría absoluta del Congreso es la de las leyes orgánicas: {c('CE', 'Artículo 81', 'exigirá mayoría absoluta del Congreso, en una votación final sobre el conjunto del proyecto')} (art. 81.2 CE); la Ley de Presupuestos no está entre ellas.",
  "c": f"Ninguna norma exige dos tercios para los Presupuestos: {c('RCD', 'art133', 'se aplicará el procedimiento legislativo común, salvo lo dispuesto en la presente Sección')} (RCD, art. 133.1), y esa Sección no fija mayorías especiales.",
  "d": f"Los tres quintos son, por ejemplo, la mayoría de la reforma constitucional: {c('CE', 'Artículo 167', 'una mayoría de tres quintos de cada una de las Cámaras')} (art. 167.1); no la de los Presupuestos."},
  [("Mayoría simple", "RCD", "art79", "deberán ser aprobados por la mayoría simple de los miembros presentes")])
EX_L85 = examen("L", 85, {
  "a": f"Es la clasificación orgánica: {c('LGP', 'Artículo 40', 'La clasificación orgánica que agrupará por secciones y servicios los créditos asignados a los distintos centros gestores de gasto')} (art. 40.1 a).",
  "b": "También describe una agrupación por órganos, no por naturaleza económica; la LGP habla de «secciones y servicios» (art. 40.1 a).",
  "c": f"Literal del art. 40.1 c): {c('LGP', 'Artículo 40', 'La clasificación económica, que agrupará los créditos por capítulos separando las operaciones corrientes, las de capital, las financieras y el Fondo de Contingencia de ejecución presupuestaria')}.",
  "d": f"Es la clasificación por programas: {c('LGP', 'Artículo 40', 'La estructura de programas se adecuará a los contenidos de las políticas de gasto contenidas en la programación plurianual')} (art. 40.1 b)."},
  [("Agrupa los créditos por capítulos separando las operaciones corrientes, las de capital, las financieras y el Fondo de Contingencia de ejecución presupuestaria", "LGP", "Artículo 40", "que agrupará los créditos por capítulos separando las operaciones corrientes, las de capital, las financieras y el Fondo de Contingencia de ejecución presupuestaria")])
EX_X91 = examen("X", 91, {
  "a": f"Es una finalidad de los programas instrumentales y de gestión: {c('OPGE27', 'a6', 'la ejecución de una actividad que se perfecciona por su propia realización, sin que sea posible proceder a una cuantificación material de sus objetivos')}.",
  "b": f"Literal de la orden de elaboración (art. 6.1.1): {c('OPGE27', 'a6', 'Los programas finalistas son aquellos a los que se puede asignar objetivos cuantificables e indicadores de ejecución mensurables')}.",
  "c": f"Otra finalidad de los instrumentales: {c('OPGE27', 'a6', 'la administración de los recursos necesarios para la ejecución de actividades generales de ordenación, regulación y planificación')}.",
  "d": f"La tercera finalidad de los instrumentales: {c('OPGE27', 'a6', 'el apoyo a un programa finalista')}; no puede definir al propio finalista."},
  [("objetivos cuantificables e indicadores de ejecución mensurables", "OPGE27", "a6", "Los programas finalistas son aquellos a los que se puede asignar objetivos cuantificables e indicadores de ejecución mensurables")])
EX_P87 = examen("P", 87, {
  "a": "El subconcepto no es nivel de especificación en el art. 43.1; es un desglose posible de los conceptos (art. 40.1 c).",
  "b": f"El concepto es la regla general ({c('LGP', 'Artículo 43', 'los créditos se especificarán a nivel de concepto')}), pero el capítulo 2 es una de sus salvedades.",
  "c": f"Literal del art. 43.1: {c('LGP', 'Artículo 43', 'los gastos corrientes en bienes y servicios, que se especificarán a nivel de artículo')}.",
  "d": f"A nivel de capítulo se especifican solo {c('LGP', 'Artículo 43', 'las inversiones reales a nivel de capítulo')}."},
  [("Artículo", "LGP", "Artículo 43", "los gastos corrientes en bienes y servicios, que se especificarán a nivel de artículo")])
EX_L96 = examen("L", 96, {
  "a": f"Literal del art. 43.1: {c('LGP', 'Artículo 43', 'las inversiones reales a nivel de capítulo')}.",
  "b": f"A nivel de artículo se especifican {c('LGP', 'Artículo 43', 'los créditos destinados a gastos de personal y los gastos corrientes en bienes y servicios')}, no las inversiones reales.",
  "c": f"El concepto es la regla general: {c('LGP', 'Artículo 43', 'los créditos se especificarán a nivel de concepto')}, salvo personal, bienes y servicios e inversiones reales.",
  "d": "El subconcepto no es nivel de especificación en el art. 43.1; es un desglose posible de los conceptos (art. 40.1 c)."},
  [("Capítulo", "LGP", "Artículo 43", "las inversiones reales a nivel de capítulo")])
EX_L84 = examen("L", 84, {
  "a": f"El servicio es el segundo grupo (91): en el documento contable, tras la sección, el campo orgánico lleva {c('ODOC', 'ani', 'el código del servicio en los dos primeros dígitos')}.",
  "b": f"112A es un programa (tres cifras y una letra): {c('OPGE27', 'ai', '112 A Tribunales de Justicia y Ministerio Fiscal')} (anexo I de la orden de elaboración); la sección es el primer grupo.",
  "c": f"El primer grupo de la aplicación es la sección de la clasificación orgánica: {c('ODOC', 'ani', '12. Sección: Se indicará el código numérico y el literal de la Sección que corresponda según la clasificación orgánica del Presupuesto de Gastos')}. Es la lectura del orden de los campos del documento contable (sección, servicio, programa, económica).",
  "d": f"240 tiene tres cifras: es un concepto ({c('RES2014', 'ai-2', '240. Gastos de edición y distribución')}); el subconcepto añade dos cifras al concepto."},
  [("El 13 hace referencia a la Sección", "ODOC", "ani", "12. Sección: Se indicará el código numérico y el literal de la Sección que corresponda según la clasificación orgánica del Presupuesto de Gastos")])
EX_P86 = examen("P", 86, {
  "a": f"231B es finalista: en el código de programas {c('OPGE27', 'ai', 'las letras «A» a »L» identifican a los programas finalistas')}; los instrumentales y de gestión van de la M a la Z.",
  "b": f"El último grupo es la clasificación económica: concepto {c('RES2014', 'ai-2', '120. Retribuciones básicas')}, dentro del artículo {c('RES2014', 'ai-2', '12. Funcionarios')}; el programa es el 231B.",
  "c": f"Los grupos de la aplicación son sección (15) y servicio (01) del Estado, que {c('OPGE27', 'a6', 'se dividirá en secciones y éstas a su vez en servicios')}; los organismos autónomos son otro subsector de la clasificación orgánica y nada en el código remite a uno.",
  "d": f"Las transferencias corrientes a familias son capítulo 4: {c('RES2014', 'ai-2', '48. A familias e instituciones sin fines de lucro')}; 120 es del capítulo 1 (gastos de personal)."},
  [("retribuciones básicas", "RES2014", "ai-2", "120. Retribuciones básicas"), ("funcionario", "RES2014", "ai-2", "12. Funcionarios")])
EX_L94 = examen("L", 94, {
  "a": f"El artículo 21 es otro artículo del capítulo 2: {c('RES2014', 'ai-2', '21. Reparaciones, mantenimiento y conservación')}.",
  "b": f"El artículo 12 es de gastos de personal (capítulo 1): {c('RES2014', 'ai-2', '12. Funcionarios')}.",
  "c": f"Literal del anexo II: {c('RES2014', 'ai-2', '23. Indemnizaciones por razón del servicio')}.",
  "d": f"El artículo 14 es {c('RES2014', 'ai-2', '14. Otro personal')} (capítulo 1)."},
  [("Artículo 23", "RES2014", "ai-2", "23. Indemnizaciones por razón del servicio")])
EX_P96 = examen("P", 96, {
  "a": f"El 12 es {c('RES2014', 'ai-2', '12. Funcionarios')} (capítulo 1, gastos de personal).",
  "b": f"Literal del anexo II: {c('RES2014', 'ai-2', '23. Indemnizaciones por razón del servicio')}.",
  "c": f"El 42 es una transferencia corriente: {c('RES2014', 'ai-2', '42. A la Seguridad Social')}.",
  "d": f"El 60 es una inversión real: {c('RES2014', 'ai-2', '60. Inversión nueva en infraestructura y bienes destinados al uso general')}."},
  [("23", "RES2014", "ai-2", "23. Indemnizaciones por razón del servicio")])
EX_X95 = examen("X", 95, {
  "a": f"Literal del apartado sexto.1 b): {c('ODOC', 'sexto', 'Documento de desglose: Se utilizará en las operaciones de desglose de las aplicaciones presupuestarias')}.",
  "b": "Esa denominación no existe en la orden: el documento del desglose se llama «Documento de desglose».",
  "c": f"Sí se utiliza documento: la Instrucción de operatoria contable manda que {c('OIOC', 'regla10', 'los Servicios gestores expedirán el oportuno documento de «Desglose»')} (regla 10.2).",
  "d": "Tiene denominación específica: «Documento de desglose» (apartado sexto.1 b)."},
  [("Documento de desglose", "ODOC", "sexto", "Documento de desglose: Se utilizará en las operaciones de desglose de las aplicaciones presupuestarias")])

T.ap("s17", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **siete** preguntas de este tema (art. 134 CE, mayoría de aprobación, clasificaciones, programas finalistas, nivel de especificación y lectura de aplicaciones presupuestarias) y **cuatro** relacionadas (nivel de especificación de las inversiones, artículo 23 de la clasificación económica y documento de desglose). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-P 2025, pregunta 85 · Artículo 134 CE (→ I.2.2)", EX_P85,
  "### GACE-L 2025 extraordinario, pregunta 89 · Mayoría de aprobación (→ III.4.1)", EX_X89,
  "### GACE-L 2025, pregunta 85 · Clasificación económica (→ IV.2.2)", EX_L85,
  "### GACE-L 2025 extraordinario, pregunta 91 · Programas finalistas (→ IV.2.3)", EX_X91,
  "### GACE-P 2025, pregunta 87 · Bienes y servicios: nivel de artículo (→ IV.3.2)", EX_P87,
  "### GACE-L 2025, pregunta 96 · Inversiones reales: nivel de capítulo (relacionada; → IV.3.2)", EX_L96,
  "### GACE-L 2025, pregunta 84 · Lectura de una aplicación: la sección (→ V.1.1)", EX_L84,
  "### GACE-P 2025, pregunta 86 · Lectura de una aplicación: programa y económica (→ V.1.2)", EX_P86,
  "### GACE-L 2025, pregunta 94 · Indemnizaciones por razón del servicio: artículo 23 (relacionada; → V.1.2)", EX_L94,
  "### GACE-P 2025, pregunta 96 · Indemnizaciones por razón del servicio: artículo 23 (relacionada; → V.1.2)", EX_P96,
  "### GACE-L 2025 extraordinario, pregunta 95 · Documento de desglose (relacionada; → V.2.3)", EX_X95,
  "### Cómo se pregunta",
  "!> Las preguntas de este tema son de **letra**: el art. 134 CE con un dato cambiado (órgano, plazo, «aumento/disminución»), las tres clasificaciones del art. 40 LGP con sus verbos («por secciones y servicios», «por capítulos», «políticas de gasto») y el **nivel de especificación** del art. 43. Las de aplicaciones presupuestarias se resuelven leyendo **sección · servicio · programa · económica** (→ V.3).",
]))

T.ap("s18", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Ley de Presupuestos | Gobierno elabora, Cortes aprueban (134.1); anual, totalidad y beneficios fiscales (134.2); prórroga (134.4; LGP 38) | No **crea** tributos; los **modifica** si lo prevé una ley tributaria sustantiva (134.7) |
| II. Principios | Programación (26): siete principios; gestión (27): especialidad, no afectación salvo ley, importe íntegro; escenarios y programas plurianuales (28 a 31) | Escenarios de **tres** ejercicios, confeccionados por **Hacienda** |
| III. Elaboración y aprobación | Límite de gasto no financiero; orden del Ministro de Hacienda; Comisión de Políticas de Gasto; remisión a las Cortes | **1 de octubre** (LGP 37); **mayoría simple**; baja en la **misma Sección** |
| IV. Estructura | Orgánica, por programas y económica (40); ingresos: orgánica y económica (41); especificación (43 y 44) | Bienes y servicios → **artículo**; inversiones → **capítulo** |
| V. Aplicación presupuestaria | Sección · servicio · programa · económica; creación y desglose (reglas 9 y 10) | **Documento de desglose**; finalistas **A-L** |

?> **Trampas frecuentes:** «el **Consejo de Ministros** enmienda los Presupuestos» (las **Cortes**); prórroga si no se aprueban «**tres meses antes**» (es **antes del primer día del ejercicio**); conformidad del Gobierno para la «**disminución** de créditos» (es para el **aumento** de créditos o la disminución de **ingresos**); «la clasificación económica agrupa por **secciones y servicios**» (esa es la **orgánica**); «inversiones reales a nivel de **concepto**» (es **capítulo**); «programa **finalista**: apoyo a otro programa» (eso es **instrumental**); «los ingresos se clasifican **por programas**» (solo orgánica y económica).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
Q = T.q
Q("CE", "Artículo 134", "Ley de Presupuestos", "Según el artículo 134.1 de la Constitución, el examen, enmienda y aprobación de los Presupuestos Generales del Estado corresponde:",
  ["A las Cortes Generales.", "Al Gobierno.", "Al Congreso de los Diputados.", "Al Ministerio de Hacienda."], "Art. 134.1 CE: al Gobierno, la elaboración; a las Cortes, su examen, enmienda y aprobación.", "a las Cortes Generales, su examen, enmienda y aprobación")
Q("CE", "Artículo 134", "Ley de Presupuestos", "Según el artículo 134.2 de la Constitución, los Presupuestos Generales del Estado incluirán:",
  ["La totalidad de los gastos e ingresos del sector público estatal.", "Los gastos del sector público estatal y los ingresos tributarios del Estado.", "La totalidad de los gastos e ingresos de todas las Administraciones Públicas.", "Los gastos de la Administración General del Estado y de sus organismos autónomos."], "Art. 134.2 CE.", "incluirán la totalidad de los gastos e ingresos del sector público estatal")
Q("CE", "Artículo 134", "Ley de Presupuestos", "Según el artículo 134.2 de la Constitución, en los Presupuestos Generales del Estado se consignará el importe de:",
  ["Los beneficios fiscales que afecten a los tributos del Estado.", "Los beneficios fiscales de todas las Administraciones Públicas.", "La deuda pública del Estado a largo plazo.", "Los ingresos tributarios de las Comunidades Autónomas."], "Art. 134.2 CE.", "el importe de los beneficios fiscales que afecten a los tributos del Estado")
Q("CE", "Artículo 134", "Ley de Presupuestos", "Según el artículo 134.7 de la Constitución, la Ley de Presupuestos:",
  ["No puede crear tributos, pero podrá modificarlos cuando una ley tributaria sustantiva así lo prevea.", "Puede crear tributos cuando una ley tributaria sustantiva así lo prevea.", "No puede crear ni modificar tributos en ningún caso.", "Puede crear y modificar tributos libremente."], "Art. 134.7 CE.", ["La Ley de Presupuestos no puede crear tributos", "Podrá modificarlos cuando una ley tributaria sustantiva así lo prevea"])
Q("CE", "Artículo 134", "Prórroga", "Según el artículo 134.4 de la Constitución, si la Ley de Presupuestos no se aprobara antes del primer día del ejercicio económico correspondiente:",
  ["Se considerarán automáticamente prorrogados los Presupuestos del ejercicio anterior hasta la aprobación de los nuevos.", "El Gobierno deberá aprobar un real decreto-ley de prórroga.", "Se prorrogarán por un máximo de seis meses.", "Se aplicarán los créditos del proyecto presentado por el Gobierno."], "Art. 134.4 CE: la prórroga es automática.", "se considerarán automáticamente prorrogados los Presupuestos del ejercicio anterior hasta la aprobación de los nuevos")
Q("CE", "Artículo 134", "Elaboración", "Según el artículo 134.3 de la Constitución, el Gobierno deberá presentar ante el Congreso de los Diputados los Presupuestos Generales del Estado:",
  ["Al menos tres meses antes de la expiración de los del año anterior.", "Al menos dos meses antes de la expiración de los del año anterior.", "Antes del 1 de septiembre.", "Al menos seis meses antes de la expiración de los del año anterior."], "Art. 134.3 CE.", "al menos tres meses antes de la expiración de los del año anterior")
Q("CE", "Artículo 134", "Tramitación", "Según el artículo 134.6 de la Constitución, requerirá la conformidad del Gobierno para su tramitación toda proposición o enmienda que suponga:",
  ["Aumento de los créditos o disminución de los ingresos presupuestarios.", "Disminución de los créditos o aumento de los ingresos presupuestarios.", "Cualquier modificación de los créditos presupuestarios.", "Aumento de los ingresos presupuestarios."], "Art. 134.6 CE.", "aumento de los créditos o disminución de los ingresos presupuestarios requerirá la conformidad del Gobierno")
Q("CE", "Artículo 75", "Tramitación", "Según el artículo 75.3 de la Constitución, la aprobación de los Presupuestos Generales del Estado:",
  ["No puede delegarse en las Comisiones Legislativas Permanentes.", "Puede delegarse en la Comisión de Presupuestos.", "Corresponde a la Diputación Permanente si las Cámaras están disueltas.", "Puede delegarse en las Comisiones si lo acuerda el Pleno por mayoría absoluta."], "Art. 75.3 CE: los Presupuestos están exceptuados de la delegación del 75.2.", "Quedan exceptuados de lo dispuesto en el apartado anterior la reforma constitucional, las cuestiones internacionales, las leyes orgánicas y de bases y los Presupuestos Generales del Estado")
Q("LGP", "Artículo 32", "Ley de Presupuestos", "Según el artículo 32 de la Ley General Presupuestaria, los Presupuestos Generales del Estado constituyen la expresión:",
  ["Cifrada, conjunta y sistemática de los derechos y obligaciones a liquidar durante el ejercicio.", "Contable, anual y limitativa de los gastos e ingresos del Estado.", "Cifrada y plurianual de los objetivos de la política económica.", "Conjunta y estimativa de los ingresos a recaudar durante el ejercicio."], "Art. 32 LGP.", "expresión cifrada, conjunta y sistemática de los derechos y obligaciones a liquidar durante el ejercicio")
Q("LGP", "Artículo 33", "Ley de Presupuestos", "Según el artículo 33.1 b) de la Ley General Presupuestaria, los presupuestos de las entidades de los sectores empresarial y fundacional que integran los Presupuestos Generales del Estado tienen carácter:",
  ["Estimativo.", "Limitativo.", "Vinculante.", "Plurianual."], "Art. 33.1 b) LGP.", "Los presupuestos estimativos de las entidades de los sectores empresarial y fundacional")
Q("LGP", "Artículo 34", "Ley de Presupuestos", "Según el artículo 34.1 de la Ley General Presupuestaria, al ejercicio presupuestario se imputarán las obligaciones económicas reconocidas:",
  ["Hasta el fin del mes de diciembre, siempre que correspondan a gastos realizados dentro del ejercicio.", "Hasta el 31 de marzo del año siguiente.", "Durante el ejercicio, cualquiera que sea el período del que deriven.", "Hasta el fin del mes de enero del año siguiente."], "Art. 34.1 b) LGP. El criterio «cualquiera que sea el período del que deriven» es el de los derechos (34.1 a).", "Las obligaciones económicas reconocidas hasta el fin del mes de diciembre")
Q("LGP", "Artículo 38", "Prórroga", "Según el artículo 38 de la Ley General Presupuestaria, si la Ley de Presupuestos no se aprobara antes del primer día del ejercicio, se prorrogan:",
  ["Los presupuestos iniciales del ejercicio anterior.", "Los presupuestos definitivos del ejercicio anterior, con sus modificaciones.", "Los créditos de los programas que terminen en el ejercicio prorrogado.", "Únicamente los créditos de personal."], "Art. 38.1 LGP; los créditos de programas que terminen no se prorrogan (38.2).", "se considerarán automáticamente prorrogados los presupuestos iniciales del ejercicio anterior")
Q("LGP", "Artículo 38", "Prórroga", "Según el artículo 38.4 de la Ley General Presupuestaria, los criterios para instrumentar la prórroga de los Presupuestos los acuerda:",
  ["El Consejo de Ministros, a propuesta del Ministerio de Hacienda.", "El Ministro de Hacienda, oída la Comisión de Políticas de Gasto.", "El Congreso de los Diputados.", "La Dirección General de Presupuestos."], "Art. 38.4 LGP.", "El Consejo de Ministros, a propuesta del Ministerio de Hacienda, acordará los criterios")
Q("LGP", "Artículo 26", "Principios", "Según el artículo 26.1 de la Ley General Presupuestaria, ¿cuál de los siguientes es un principio de la programación presupuestaria?",
  ["Plurianualidad.", "Unidad de caja.", "Anualidad de la gestión.", "Especialidad cuantitativa."], "Art. 26.1 LGP: estabilidad, sostenibilidad financiera, plurianualidad, transparencia, eficiencia, responsabilidad y lealtad institucional.", "sostenibilidad financiera, plurianualidad, transparencia")
Q("LGP", "Artículo 27", "Principios", "Según el artículo 27.3 de la Ley General Presupuestaria, los recursos del Estado se destinarán a satisfacer el conjunto de sus obligaciones, salvo que:",
  ["Por ley se establezca su afectación a fines determinados.", "El Ministro de Hacienda acuerde su afectación.", "Lo autorice el Consejo de Ministros.", "Procedan de transferencias de la Unión Europea."], "Art. 27.3 LGP: la afectación exige ley.", "salvo que por ley se establezca su afectación a fines determinados")
Q("LGP", "Artículo 27", "Principios", "Según el artículo 27.2 de la Ley General Presupuestaria, el carácter limitativo y vinculante de los créditos será el correspondiente:",
  ["Al nivel de especificación con que aparezcan en los presupuestos.", "Al nivel de capítulo en todo caso.", "Al nivel de subconcepto.", "Al que fije cada año el Ministro de Hacienda."], "Art. 27.2 LGP.", "será el correspondiente al nivel de especificación con que aparezcan en aquéllos")
Q("LGP", "Artículo 28", "Programación plurianual", "Según el artículo 28.1 de la Ley General Presupuestaria, los escenarios presupuestarios plurianuales determinarán los límites referidos a:",
  ["Los tres ejercicios siguientes.", "Los dos ejercicios siguientes.", "Los cuatro ejercicios siguientes.", "La legislatura en curso."], "Art. 28.1 LGP.", "referidos a los tres ejercicios siguientes")
Q("LGP", "Artículo 28", "Programación plurianual", "Según el artículo 28.3 de la Ley General Presupuestaria, los escenarios presupuestarios plurianuales serán confeccionados por:",
  ["El Ministerio de Hacienda.", "El Consejo de Ministros.", "La Comisión de Políticas de Gasto.", "Cada departamento ministerial."], "Art. 28.3 LGP; de ellos se da cuenta al Consejo de Ministros.", "serán confeccionados por el Ministerio de Hacienda")
Q("LGP", "Artículo 29", "Programación plurianual", "Según el artículo 29.3 de la Ley General Presupuestaria, el programa plurianual de cada ministerio se aprobará por:",
  ["El Ministro.", "El Consejo de Ministros.", "El Ministro de Hacienda.", "El Subsecretario del departamento."], "Art. 29.3 LGP.", "se aprobará por el Ministro")
Q("LGP", "Artículo 36", "Elaboración", "Según el artículo 36.2 de la Ley General Presupuestaria, el procedimiento de elaboración de los Presupuestos Generales del Estado se establecerá por:",
  ["Orden del Ministro de Hacienda.", "Real decreto del Consejo de Ministros.", "Resolución de la Dirección General de Presupuestos.", "La propia Ley de Presupuestos del ejercicio anterior."], "Art. 36.2 LGP.", "se establecerá por orden del Ministro de Hacienda")
Q("LGP", "Artículo 36", "Elaboración", "Según el artículo 36.5 de la Ley General Presupuestaria, elevar al acuerdo del Gobierno el anteproyecto de la Ley de Presupuestos Generales del Estado corresponde:",
  ["Al Ministro de Hacienda.", "Al Presidente del Gobierno.", "A la Comisión de Políticas de Gasto.", "A la Dirección General de Presupuestos."], "Art. 36.5 LGP.", "Corresponderá al Ministro de Hacienda elevar al acuerdo del Gobierno el anteproyecto")
Q("LGP", "Artículo 36", "Elaboración", "Según el artículo 36.3 de la Ley General Presupuestaria, el presupuesto de ingresos de la Administración General del Estado será elaborado por:",
  ["El Ministerio de Hacienda.", "Cada departamento ministerial.", "La Agencia Estatal de Administración Tributaria.", "La Comisión de Políticas de Gasto."], "Art. 36.3 LGP.", "El presupuesto de ingresos de la Administración General del Estado será elaborado por el Ministerio de Hacienda")
Q("LOEP", "a30", "Elaboración", "Según el artículo 30.2 de la Ley Orgánica 2/2012, el Ministerio de Hacienda informará al Consejo de Política Fiscal y Financiera sobre el límite de gasto no financiero del Presupuesto del Estado:",
  ["Antes del 1 de agosto de cada año.", "Antes del 1 de octubre de cada año.", "Antes del 15 de julio de cada año.", "Antes del 30 de junio de cada año."], "Art. 30.2 LO 2/2012.", "Antes del 1 de agosto de cada año el Ministerio de Hacienda y Administraciones Públicas informará al Consejo de Política Fiscal y Financiera")
Q("OPGE27", "a4", "Elaboración", "Según la Orden HAC/557/2026, de normas para la elaboración de los Presupuestos Generales del Estado para 2027, la Comisión de Políticas de Gasto está presidida por:",
  ["La persona titular del Ministerio de Hacienda.", "La persona titular de la Presidencia del Gobierno.", "La persona titular de la Dirección General de Presupuestos.", "La persona titular de la Subdirección General de Política Presupuestaria."], "Art. 4.1 de la orden; la Subdirección General de Política Presupuestaria actúa como secretaría.", "estará presidida por la persona titular del Ministerio de Hacienda")
Q("OPGE27", "a4", "Elaboración", "Según la Orden HAC/557/2026, las Comisiones de Análisis de Programas son:",
  ["Reuniones bilaterales entre el Ministerio de Hacienda y los distintos departamentos ministeriales.", "Reuniones plenarias de todos los departamentos ministeriales presididas por el Ministro de Hacienda.", "Comisiones parlamentarias del Congreso para el estudio de los programas de gasto.", "Órganos de la Autoridad Independiente de Responsabilidad Fiscal."], "Art. 4.2 de la orden.", "Las Comisiones de Análisis de Programas son reuniones bilaterales entre el Ministerio de Hacienda y los distintos departamentos ministeriales")
Q("LGP", "Artículo 37", "Elaboración", "Según el artículo 37.1 de la Ley General Presupuestaria, el proyecto de Ley de Presupuestos Generales del Estado será remitido a las Cortes Generales:",
  ["Antes del día 1 de octubre del año anterior al que se refiera.", "Antes del día 1 de septiembre del año anterior al que se refiera.", "Antes del día 30 de septiembre del año al que se refiera.", "Antes del día 1 de noviembre del año anterior al que se refiera."], "Art. 37.1 LGP.", "antes del día 1 de octubre del año anterior al que se refiera")
Q("LGP", "Artículo 37", "Elaboración", "Según el artículo 37.2 de la Ley General Presupuestaria, ¿cuál de los siguientes documentos acompaña al proyecto de Ley de Presupuestos Generales del Estado?",
  ["El informe de impacto de género.", "El dictamen del Consejo de Estado.", "El informe del Tribunal de Cuentas sobre el proyecto.", "La memoria del análisis de impacto normativo de cada sección."], "Art. 37.2 b) LGP.", "El informe de impacto de género")
Q("RCD", "art133", "Tramitación", "Según el artículo 133.3 del Reglamento del Congreso, las enmiendas al proyecto de Ley de Presupuestos que supongan aumento de créditos en algún concepto únicamente podrán ser admitidas a trámite si proponen:",
  ["Una baja de igual cuantía en la misma Sección.", "Una baja de igual cuantía en cualquier Sección.", "Un aumento de ingresos de igual cuantía.", "Una baja de igual cuantía en el mismo capítulo de cualquier Sección."], "Art. 133.3 RCD.", "proponen una baja de igual cuantía en la misma Sección")
Q("RCD", "art134", "Tramitación", "Según el artículo 134.1 del Reglamento del Congreso, las cuantías globales de los estados de los Presupuestos quedan fijadas:",
  ["En el debate de totalidad en el Pleno de la Cámara.", "En el dictamen de la Comisión de Presupuestos.", "En el debate final en el Pleno.", "En el acuerdo del Consejo de Ministros que aprueba el proyecto."], "Art. 134.1 RCD.", "En dicho debate quedarán fijadas las cuantías globales de los estados de los Presupuestos")
Q("RCD", "art79", "Tramitación", "Según el artículo 79.1 del Reglamento del Congreso, salvo mayorías especiales, los acuerdos para ser válidos deberán ser aprobados por:",
  ["La mayoría simple de los miembros presentes del órgano correspondiente.", "La mayoría absoluta de los miembros del órgano correspondiente.", "La mayoría de tres quintos de los miembros presentes.", "La mayoría simple de los miembros de derecho del órgano."], "Art. 79.1 RCD: es la mayoría que rige la aprobación de los Presupuestos.", "aprobados por la mayoría simple de los miembros presentes del órgano correspondiente")
Q("RS", "Artículo 149", "Tramitación", "Según el artículo 149.1 del Reglamento del Senado, la impugnación de una sección del proyecto de Ley de Presupuestos deberá formularse mediante:",
  ["Una propuesta de veto.", "Una enmienda a la totalidad de devolución.", "Una moción.", "Una enmienda de supresión."], "Art. 149.1 RS.", "La impugnación de una sección deberá formularse mediante una propuesta de veto")
Q("LGP", "Artículo 35", "Estructura", "Según el artículo 35.1 de la Ley General Presupuestaria, son créditos presupuestarios:",
  ["Cada una de las asignaciones individualizadas de gasto puestas a disposición de los centros gestores.", "Los derechos económicos reconocidos durante el ejercicio.", "Las previsiones de ingresos de cada centro gestor.", "Los compromisos de gasto adquiridos por los centros gestores."], "Art. 35.1 LGP.", "Son créditos presupuestarios cada una de las asignaciones individualizadas de gasto")
Q("LGP", "Artículo 40", "Estructura", "Según el artículo 40.1 a) de la Ley General Presupuestaria, la clasificación orgánica agrupará los créditos:",
  ["Por secciones y servicios.", "Por capítulos, artículos y conceptos.", "Por áreas y políticas de gasto.", "Por programas y subprogramas."], "Art. 40.1 a) LGP.", "La clasificación orgánica que agrupará por secciones y servicios")
Q("LGP", "Artículo 40", "Estructura", "Según el artículo 40.1 c) de la Ley General Presupuestaria, en los créditos para operaciones de capital se distinguirán:",
  ["Las inversiones reales y las transferencias de capital.", "Los activos financieros y los pasivos financieros.", "Los gastos financieros y las transferencias corrientes.", "Las inversiones reales y los activos financieros."], "Art. 40.1 c) LGP.", "En los créditos para operaciones de capital se distinguirán las inversiones reales y las transferencias de capital")
Q("LGP", "Artículo 40", "Estructura", "Según el artículo 40.1 de la Ley General Presupuestaria, en la clasificación económica los conceptos:",
  ["Podrán dividirse en subconceptos.", "Deberán dividirse en subconceptos.", "Se agrupan en programas.", "Se dividen en artículos."], "Art. 40.1 LGP: capítulos → artículos → conceptos, que «podrán» dividirse en subconceptos.", "en conceptos que podrán dividirse en subconceptos")
Q("LGP", "Artículo 41", "Estructura", "Según el artículo 41 de la Ley General Presupuestaria, los estados de ingresos se estructurarán siguiendo las clasificaciones:",
  ["Orgánica y económica.", "Orgánica, por programas y económica.", "Económica y funcional.", "Por programas y económica."], "Art. 41 LGP: los programas son solo del gasto.", "se estructurarán siguiendo las clasificaciones orgánica y económica")
Q("OPGE27", "a6", "Estructura", "Según la Orden HAC/557/2026, los programas a los que se puede asignar objetivos cuantificables e indicadores de ejecución mensurables son los programas:",
  ["Finalistas.", "Instrumentales.", "De gestión.", "De apoyo."], "Art. 6.1.1 de la orden.", "Los programas finalistas son aquellos a los que se puede asignar objetivos cuantificables e indicadores de ejecución mensurables")
Q("OPGE27", "ai", "Estructura", "Según el anexo I de la Orden HAC/557/2026, el cuarto carácter del código de programas identifica a los programas finalistas con las letras:",
  ["De la «A» a la «L».", "De la «M» a la «Z».", "De la «A» a la «M».", "De la «L» a la «Z»."], "Anexo I de la orden: A a L finalistas; M a Z instrumentales y de gestión.", "las letras «A» a »L» identifican a los programas finalistas")
Q("OPGE27", "a6", "Estructura", "Según el artículo 6.1.2 de la Orden HAC/557/2026, en la clasificación orgánica el Estado se dividirá en:",
  ["Secciones y éstas a su vez en servicios.", "Servicios y éstos a su vez en secciones.", "Áreas de gasto y políticas de gasto.", "Capítulos y artículos."], "Art. 6.1.2 a) de la orden.", "El Estado, que se dividirá en secciones y éstas a su vez en servicios")
Q("LGP", "Artículo 43", "Especificación", "Según el artículo 43.1 de la Ley General Presupuestaria, en el presupuesto del Estado los créditos destinados a gastos de personal se especificarán a nivel de:",
  ["Artículo.", "Concepto.", "Capítulo.", "Subconcepto."], "Art. 43.1 LGP.", "los créditos destinados a gastos de personal y los gastos corrientes en bienes y servicios, que se especificarán a nivel de artículo")
Q("LGP", "Artículo 43", "Especificación", "Según el artículo 43.2 de la Ley General Presupuestaria, se especificarán al nivel que corresponda conforme a su concreta clasificación económica:",
  ["Los créditos extraordinarios que se concedan durante el ejercicio.", "Todos los créditos de inversiones reales.", "Todos los créditos de gastos de personal.", "Los créditos destinados a transferencias corrientes al exterior."], "Art. 43.2 f) LGP; las transferencias al exterior están expresamente exceptuadas de la letra d).", "Los créditos extraordinarios que se concedan durante el ejercicio")
Q("LGP", "Artículo 44", "Especificación", "Según el artículo 44.1 de la Ley General Presupuestaria, en el presupuesto de los organismos autónomos los créditos destinados a gastos corrientes en bienes y servicios se especificarán a nivel de:",
  ["Capítulo.", "Artículo.", "Concepto.", "Subconcepto."], "Art. 44.1 LGP (en el Estado, artículo: art. 43.1).", "gastos corrientes en bienes y servicios y las inversiones reales, que se especificarán a nivel de capítulo")
Q("LGP", "Artículo 44", "Especificación", "Según el artículo 44.3 de la Ley General Presupuestaria, los créditos del Presupuesto de la Seguridad Social se especificarán, con carácter general, a nivel de:",
  ["Grupo de programas.", "Programa.", "Capítulo.", "Concepto."], "Art. 44.3 LGP; la acción protectora no contributiva y universal, a nivel de programa.", "se especificarán a nivel de grupo de programas")
Q("OIOC", "regla10", "Aplicación presupuestaria", "Según la regla 10 de la Instrucción de operatoria contable a seguir en la ejecución del gasto del Estado, la operación de desglose de aplicaciones presupuestarias:",
  ["Permite ejecutar los créditos a un mayor nivel de desagregación, sin perjuicio del nivel de vinculación jurídica de dichos créditos.", "Modifica el nivel de vinculación jurídica de los créditos.", "Es una modificación presupuestaria que aprueba el Ministro de Hacienda.", "Solo puede afectar a la clasificación económica."], "Regla 10.1: puede afectar a cualquiera de las clasificaciones orgánica, funcional o económica.", "a un mayor nivel de desagregación que el que figuraba en el presupuesto aprobado, sin perjuicio del nivel de vinculación jurídica de dichos créditos")
Q("OIOC", "regla9", "Aplicación presupuestaria", "Según la regla 9 de la Instrucción de operatoria contable, cuando se pretenda imputar gastos a una aplicación dentro del mismo nivel de vinculación que no cuente con dotación, el servicio gestor solicitará su creación:",
  ["A la oficina de contabilidad, sin necesidad de efectuar una operación de transferencia de crédito.", "A la Dirección General de Presupuestos, mediante una transferencia de crédito.", "Al Ministro de Hacienda, mediante una generación de crédito.", "A la Intervención Delegada, mediante un crédito extraordinario."], "Regla 9.", "el Servicio gestor solicitará a la oficina de contabilidad la creación de la correspondiente aplicación presupuestaria, sin necesidad de efectuar una operación de transferencia de crédito")
Q("ODOC", "ani", "Aplicación presupuestaria", "Según las normas de cumplimentación de los documentos contables (Orden de 1 de febrero de 1996), en el campo «Orgánica» se indicará en los dos primeros dígitos el código:",
  ["Del servicio.", "De la sección.", "Del programa.", "Del capítulo."], "Anexo I, nota 13; la sección tiene su propio campo (nota 12).", "13. Orgánica: Se indicará el código del servicio en los dos primeros dígitos")
T.real("P", 85, "Ley de Presupuestos"); T.real("X", 89, "Tramitación"); T.real("L", 85, "Estructura"); T.real("X", 91, "Estructura")
T.real("P", 87, "Especificación"); T.real("L", 84, "Aplicación presupuestaria"); T.real("P", 86, "Aplicación presupuestaria")

# Flashcards
for q_, a_, cat in [
  ("¿Quién elabora y quién aprueba los Presupuestos? (art. 134.1 CE)", "El Gobierno los elabora; las Cortes Generales los examinan, enmiendan y aprueban.", "Ley de Presupuestos"),
  ("Contenido constitucional de los PGE (art. 134.2)", "Carácter anual; totalidad de gastos e ingresos del sector público estatal; importe de los beneficios fiscales de los tributos del Estado.", "Ley de Presupuestos"),
  ("¿Puede la Ley de Presupuestos crear tributos? (art. 134.7)", "No. Puede modificarlos cuando una ley tributaria sustantiva así lo prevea.", "Ley de Presupuestos"),
  ("¿Qué pasa si no hay Ley de Presupuestos el 1 de enero?", "Prórroga automática de los presupuestos (iniciales, LGP 38) del ejercicio anterior hasta la aprobación (y publicación) de los nuevos (134.4 CE).", "Prórroga"),
  ("Definición de los PGE (LGP, art. 32)", "Expresión cifrada, conjunta y sistemática de los derechos y obligaciones a liquidar durante el ejercicio por los órganos y entidades del sector público estatal.", "Ley de Presupuestos"),
  ("Principios de programación (LGP, art. 26.1)", "Estabilidad presupuestaria, sostenibilidad financiera, plurianualidad, transparencia, eficiencia, responsabilidad y lealtad institucional.", "Principios"),
  ("Escenarios presupuestarios plurianuales (LGP, art. 28)", "Límites para los tres ejercicios siguientes; los confecciona el Ministerio de Hacienda; escenario de ingresos y de gastos.", "Programación plurianual"),
  ("¿Qué norma regula el procedimiento de elaboración de los PGE? (LGP, art. 36.2)", "Una orden del Ministro de Hacienda (la vigente: Orden HAC/557/2026, para 2027).", "Elaboración"),
  ("Presidencias en la elaboración (Orden HAC/557/2026, art. 4)", "Comisión de Políticas de Gasto: titular del Ministerio de Hacienda. Comisiones de Análisis de Programas: titular de la Secretaría de Estado de Presupuestos y Gastos.", "Elaboración"),
  ("Plazos de presentación del proyecto", "CE 134.3: al menos tres meses antes de la expiración de los del año anterior; LGP 37.1: antes del 1 de octubre.", "Elaboración"),
  ("¿Con qué mayoría se aprueban los PGE en el Congreso?", "Mayoría simple de los miembros presentes (RCD 79.1; CE 79.2).", "Tramitación"),
  ("Enmiendas que aumentan créditos (RCD 133.3)", "Solo si proponen una baja de igual cuantía en la misma Sección.", "Tramitación"),
  ("Las tres clasificaciones del gasto (LGP, art. 40)", "Orgánica (secciones y servicios), por programas (objetivos; políticas de gasto) y económica (capítulos, artículos, conceptos, subconceptos).", "Estructura"),
  ("Clasificaciones del ingreso (LGP, art. 41)", "Orgánica y económica.", "Estructura"),
  ("Programas finalistas e instrumentales", "Finalistas: objetivos cuantificables e indicadores mensurables (letras A-L). Instrumentales y de gestión: ordenación, regulación y planificación; actividad que se perfecciona por su realización; apoyo a un finalista (M-Z).", "Estructura"),
  ("Nivel de especificación en el Estado (LGP, art. 43.1)", "Concepto; personal y bienes y servicios, artículo; inversiones reales, capítulo.", "Especificación"),
  ("Nivel de especificación en organismos autónomos (LGP, art. 44.1)", "Concepto; personal, bienes y servicios e inversiones reales, capítulo.", "Especificación"),
  ("¿Cómo se lee una aplicación presupuestaria?", "Sección · servicio · programa · económica (campos 12 a 15 de los documentos contables).", "Aplicación presupuestaria"),
  ("Desglose de aplicaciones (regla 10)", "Ejecutar los créditos a mayor desagregación (orgánica, funcional o económica) sin cambiar la vinculación jurídica; documento «Desglose».", "Aplicación presupuestaria"),
  ("Reasignación de créditos (regla 10.3)", "Reponer crédito a la aplicación origen del desglose o reasignarlo entre aplicaciones desglosadas del mismo nivel; documento «Reasignación».", "Aplicación presupuestaria"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Ley de Presupuestos Generales del Estado", "Ley anual que elabora el Gobierno y examinan, enmiendan y aprueban las Cortes; incluye la totalidad de los gastos e ingresos del sector público estatal (art. 134 CE).", "s1", "Ley de Presupuestos")
T.glos("Beneficios fiscales", "Su importe, en cuanto afecte a los tributos del Estado, se consigna en los Presupuestos (art. 134.2 CE; LGP, art. 33.2 e).", "s2", "Ley de Presupuestos")
T.glos("Prórroga presupuestaria", "Vigencia automática de los presupuestos iniciales del ejercicio anterior si la nueva ley no se aprueba antes del primer día del ejercicio (art. 134.4 CE; LGP, art. 38).", "s4", "Ley de Presupuestos")
T.glos("Presupuesto limitativo", "Aquel cuyos créditos fijan las obligaciones que, como máximo, pueden reconocerse (LGP, art. 33).", "s3", "Ley de Presupuestos")
T.glos("Escenario presupuestario plurianual", "Programación del sector público estatal con presupuesto limitativo que fija límites para los tres ejercicios siguientes (LGP, art. 28).", "s6", "Principios")
T.glos("Límite de gasto no financiero", "Techo de asignación de recursos del presupuesto, coherente con el objetivo de estabilidad y la regla de gasto (LO 2/2012, art. 30; LGP, art. 36.1).", "s7", "Elaboración")
T.glos("Comisión de Políticas de Gasto", "Órgano presidido por el titular del Ministerio de Hacienda que interviene en las directrices de distribución del gasto (LGP, art. 36.2; Orden HAC/557/2026, art. 4).", "s8", "Elaboración")
T.glos("Crédito presupuestario", "Asignación individualizada de gasto puesta a disposición de los centros gestores (LGP, art. 35.1).", "s11", "Estructura")
T.glos("Programa finalista", "Programa al que se pueden asignar objetivos cuantificables e indicadores de ejecución mensurables (Orden HAC/557/2026, art. 6.1.1); letras A a L.", "s12", "Estructura")
T.glos("Clasificación orgánica", "Agrupa los créditos por secciones y servicios según los centros gestores (LGP, art. 40.1 a).", "s12", "Estructura")
T.glos("Clasificación económica", "Agrupa los créditos por capítulos (operaciones corrientes, de capital, financieras y Fondo de Contingencia), desglosados en artículos, conceptos y subconceptos (LGP, art. 40.1 c).", "s12", "Estructura")
T.glos("Nivel de especificación", "Nivel de la clasificación económica al que aparecen los créditos y al que son limitativos y vinculantes (LGP, arts. 27.2 y 43).", "s13", "Especificación")
T.glos("Aplicación presupuestaria", "Identificación del crédito por sección, servicio, programa y clasificación económica en los documentos contables (Orden de 1-2-1996, anexo I).", "s14", "Aplicación presupuestaria")
T.glos("Desglose de aplicaciones", "Operación que permite ejecutar los créditos a un mayor nivel de desagregación que el aprobado, sin alterar su vinculación jurídica (regla 10 de la Instrucción de operatoria contable).", "s15", "Aplicación presupuestaria")

# Cronología (fechas de los metadatos del BOE)
T.hito("1978", "Constitución Española (27-12-1978; BOE de 29-12-1978)", "Art. 134: Presupuestos Generales del Estado", "normativo", "s1")
T.hito("1982", "Reglamento del Congreso de los Diputados (publicado por Resolución de 24-2-1982; BOE de 5-3-1982)", "Arts. 133 a 135: especialidades de la tramitación de los Presupuestos", "normativo", "s10")
T.hito("1994", "Texto refundido del Reglamento del Senado (3-5-1994; BOE de 13-5-1994)", "Arts. 148 a 151: tramitación de los Presupuestos en el Senado", "normativo", "s10")
T.hito("1996", "Orden de 1 de febrero de 1996, documentos contables de la Administración General del Estado (BOE de 9-2-1996)", "Campos de la aplicación presupuestaria y documento de desglose", "normativo", "s14")
T.hito("2003", "Ley 47/2003, de 26 de noviembre, General Presupuestaria (BOE de 27-11-2003; en vigor el 1-1-2005)", "Arts. 26 a 44: principios, contenido, elaboración y estructura", "normativo", "s3")
T.hito("2012", "Ley Orgánica 2/2012, de 27 de abril, de Estabilidad Presupuestaria y Sostenibilidad Financiera (BOE de 30-4-2012)", "Art. 30: límite de gasto no financiero", "normativo", "s7")
T.hito("2014", "Resolución de 20 de enero de 2014, de la Dirección General de Presupuestos (BOE de 29-1-2014)", "Códigos de la clasificación económica de gastos e ingresos", "normativo", "s14")
T.hito("2026", "Orden HAC/557/2026, de 3 de junio, normas para la elaboración de los PGE para 2027 (BOE de 5-6-2026)", "Comisiones, proceso de elaboración y estructura de los Presupuestos", "normativo", "s8")

T.publicar()
