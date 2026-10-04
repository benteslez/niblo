# -*- coding: utf-8 -*-
"""Tema I.6 (B1T06): El poder ejecutivo. El Presidente del Gobierno y el Consejo de
Ministros. Relaciones entre el Gobierno y las Cortes Generales. Designación, causas de
cese y responsabilidad del Gobierno. El Consejo de Estado.
Método del I.2: mapa → bloques (I a IV) con guía; cada artículo, texto literal del
BOE + ficha de casillas fijas; cierre 1 (preguntas oficiales) y cierre 2 (repaso).
Normas (textos consolidados del BOE): CE, Títulos IV (arts. 97 a 102 y 107) y V
(arts. 108 a 116); Ley 50/1997, del Gobierno; Reglamento del Congreso (arts. 170 a
188); LO 3/1980, del Consejo de Estado."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

T = Tema("B1T06",
  "Cuatro preguntas: I. Qué es el Gobierno y cómo se organiza (arts. 97 y 98 CE; Ley 50/1997) · II. Cómo se designa, cuándo cesa y de qué responde penalmente (arts. 99 a 102; Reglamento del Congreso) · III. Cómo se relaciona con las Cortes: control y responsabilidad política (arts. 108 a 116) · IV. Qué es el Consejo de Estado (art. 107; LO 3/1980). Cada artículo: texto literal del BOE y ficha.",
  ["Gobierno", "Art. 97", "Art. 98", "Ley 50/1997", "Presidente del Gobierno", "Consejo de Ministros", "Comisiones Delegadas", "Investidura", "Art. 99", "Gobierno en funciones", "Art. 102", "Cuestión de confianza", "Moción de censura", "Art. 115", "Consejo de Estado", "LO 3/1980"])

# =============================================================================
T.ap("s0", "Mapa del tema: cuatro preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque I, tema 6):
> 6. El poder ejecutivo. El Presidente del Gobierno y el Consejo de Ministros. Relaciones entre el Gobierno y las Cortes Generales. Designación, causas de cese y responsabilidad del Gobierno. El Consejo de Estado.

### El hilo conductor

El epígrafe se lee como **cuatro preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Constitución | Leyes de desarrollo |
|---|---|---|---|
| **I** | ¿Qué es el Gobierno y cómo se organiza? (poder ejecutivo, Presidente y Consejo de Ministros) | Arts. 97 y 98.1 y 2 | Ley 50/1997, arts. 1 a 10, 17, 18, 20 y 24 |
| **II** | ¿Cómo se designa, cuándo cesa y de qué responde penalmente? | Arts. 99 a 102 (y 98.3 y 4) | Ley 50/1997, arts. 11 a 14 y 21; Reglamento del Congreso, arts. 170 a 172 |
| **III** | ¿Cómo se relacionan el Gobierno y las Cortes? (control y responsabilidad política) | Arts. 108 a 116 | Ley 50/1997, art. 29; Reglamento del Congreso, arts. 173 a 188 |
| **IV** | ¿Qué es el Consejo de Estado? | Art. 107 | LO 3/1980, del Consejo de Estado |

!> **La idea que une los cuatro bloques:** el Gobierno **dirige la política** y ejerce la función ejecutiva (I). Nace de la **confianza del Congreso** (investidura) y cesa cuando la pierde, con las elecciones o con la dimisión o muerte de su Presidente (II). Mientras gobierna, **responde políticamente ante el Congreso**, que puede retirarle la confianza (III). Y para decidir en Derecho cuenta con un **supremo órgano consultivo**: el Consejo de Estado (IV).

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- Fronteras con otros temas: la Corona y el refrendo (tema I.4); las Cortes, su composición y el procedimiento legislativo (tema I.5); los estados de alarma, excepción y sitio en detalle (tema I.2); los órganos superiores y directivos de los Ministerios (tema I.8); el decreto-ley y el decreto legislativo (tema IV.2). Los arts. 103 a 106 CE (Administración) no se desarrollan aquí.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué es el Gobierno y cómo se organiza? (arts. 97 y 98; Ley 50/1997)", donde(
  "Primera pregunta del tema. El epígrafe empieza por «el poder ejecutivo»: la Constitución lo regula en su Título IV, " + c("CE", "tiv", "Del Gobierno y de la Administración") + ". Antes de ver cómo se nombra o se controla al Gobierno, hay que saber **qué hace**, **quién lo forma** y **cómo funciona**.",
  ["1 Las funciones del Gobierno (art. 97)", "2 Composición (art. 98.1; Ley 50/1997, arts. 1, 3 y 4)", "3 El Presidente del Gobierno (art. 98.2; Ley 50/1997, art. 2)", "4 Consejo de Ministros y Comisiones Delegadas (Ley 50/1997, arts. 5 y 6)", "5 Órganos de colaboración y apoyo (Ley 50/1997, arts. 7 a 10)", "6 Funcionamiento, delegación y forma de las decisiones (Ley 50/1997, arts. 17, 18, 20 y 24)"]))

T.ap("s1", "I.1 Las funciones del Gobierno (art. 97; Ley 50/1997, art. 1.1)", f"""
{unidad("1.1 Qué hace el Gobierno (art. 97)",
  lit("CE", "Artículo 97", ["dirige la política interior y exterior", "la función ejecutiva y la potestad reglamentaria"]),
  fichab("Las funciones constitucionales del Gobierno",
         c("CE", "Artículo 97", "El Gobierno"),
         ["::Dirige y ejerce:", "Dirige la política interior y exterior", "Dirige la Administración civil y militar", "Dirige la defensa del Estado", "Ejerce la función ejecutiva", "Ejerce la potestad reglamentaria"],
         f"Todo ello {c('CE', 'Artículo 97', 'de acuerdo con la Constitución y las leyes')}",
         f"La Ley 50/1997 lo repite **literalmente** (art. 1.1: {c('LGOB', 'a1', 'El Gobierno dirige la política interior y exterior')}). El Gobierno tiene la potestad **reglamentaria**; la **legislativa** es de las Cortes ({c('CE', 'Artículo 66', 'Las Cortes Generales ejercen la potestad legislativa del Estado')}, tema I.5)."))}
""", 2)

T.ap("s2", "I.2 Composición del Gobierno (art. 98.1; Ley 50/1997, arts. 1.2 y 3, 3 y 4)", f"""
{unidad("2.1 Quién forma el Gobierno (art. 98.1; Ley 50/1997, art. 1.2 y 3)",
  lit("CE", "Artículo 98", ["de los Vicepresidentes, en su caso", "de los demás miembros que establezca la ley"], solo=[1]),
  lit("LGOB", "a1", ["del Vicepresidente o Vicepresidentes, en su caso, y de los Ministros", "en Consejo de Ministros y en Comisiones Delegadas del Gobierno"], solo=[2, 3]),
  fichab("Composición del Gobierno",
         ["Presidente", "Vicepresidente o Vicepresidentes, **en su caso**", "Ministros", "Los demás miembros que establezca la ley (la Ley 50/1997 no añade ninguno)"],
         "Los miembros del Gobierno se reúnen en **Consejo de Ministros** y en **Comisiones Delegadas** (→ I.4)",
         "—",
         "Los Vicepresidentes son **eventuales** («en su caso»). La Ley 50/1997 enumera solo Presidente, Vicepresidentes y Ministros: los **Secretarios de Estado no son miembros del Gobierno**; la ley los regula entre los órganos de colaboración y apoyo (→ I.5.1)."))}

{unidad("2.2 Los Vicepresidentes (Ley 50/1997, art. 3)",
  lit("LGOB", "a3", ["las funciones que les encomiende el Presidente", "ostentará, además, la condición de Ministro"]),
  fichab("Vicepresidente o Vicepresidentes del Gobierno",
         c("LGOB", "a3", "cuando existan"),
         f"Ejercen {c('LGOB', 'a3', 'las funciones que les encomiende el Presidente')}",
         "—",
         "Si asume un Departamento ministerial, es **también Ministro** (3.2). Su separación extingue el órgano, salvo que se designe otro en sustitución (art. 12.3 → II.2.3)."))}

{unidad("2.3 Los Ministros (Ley 50/1997, art. 4)",
  lit("LGOB", "a4", ["Ejercer la potestad reglamentaria en las materias propias de su Departamento", "Refrendar, en su caso, los actos del Rey en materia de su competencia", "Ministros sin cartera", "por Real Decreto se determinará el ámbito de sus competencias"]),
  fichab("Ministros: titulares de los Departamentos y Ministros sin cartera",
         ["Ministros titulares de un Departamento", "Ministros **sin cartera**, con la responsabilidad de determinadas funciones gubernamentales"],
         ["Desarrollan la acción del Gobierno en su Departamento", "Potestad reglamentaria en las materias propias de su Departamento", "Las demás competencias que les atribuyan las normas", "Refrendan, en su caso, los actos del Rey en materia de su competencia"],
         "—",
         f"Los Ministros tienen potestad reglamentaria **propia** en su materia. Los Ministros sin cartera: su ámbito, estructura y medios se fijan {c('LGOB', 'a4', 'por Real Decreto')} (no por ley ni por Orden)."))}
""", 2)

T.ap("s3", "I.3 El Presidente del Gobierno (art. 98.2; Ley 50/1997, art. 2)", f"""
{unidad("3.1 Dirige y coordina (art. 98.2; Ley 50/1997, art. 2.1)",
  lit("CE", "Artículo 98", ["dirige la acción del Gobierno y coordina las funciones de los demás miembros"], solo=[2]),
  lit("LGOB", "a2", ["responsabilidad directa de los Ministros en su gestión"], solo=[1]),
  fichab("Posición del Presidente dentro del Gobierno",
         c("CE", "Artículo 98", "El Presidente"),
         ["Dirige la acción del Gobierno", "Coordina las funciones de los demás miembros"],
         "—",
         f"Dirección y coordinación {c('CE', 'Artículo 98', 'sin perjuicio de la competencia y responsabilidad directa de éstos en su gestión')}: cada miembro responde directamente de su gestión."))}

{unidad("3.2 Las atribuciones del Presidente (Ley 50/1997, art. 2.2)",
  lit("LGOB", "a2", ["previa deliberación del Consejo de Ministros, la disolución", "previa autorización del Congreso de los Diputados", "Interponer el recurso de inconstitucionalidad", "Crear, modificar y suprimir, por Real Decreto, los Departamentos Ministeriales", "Proponer al Rey el nombramiento y separación de los Vicepresidentes y de los Ministros"], solo=list(range(2, 17))),
  fichab("Lo que corresponde «en todo caso» al Presidente del Gobierno",
         c("LGOB", "a2", "En todo caso, corresponde al Presidente del Gobierno"),
         ["::Las que más se preguntan:", "Representar al Gobierno y establecer su programa político", "Proponer al Rey la disolución de las Cámaras o de las Cortes (previa deliberación del Consejo de Ministros)", "Plantear la cuestión de confianza (previa deliberación del Consejo de Ministros)", "Proponer al Rey el referéndum consultivo (previa autorización del Congreso)", "Convocar, presidir y fijar el orden del día del Consejo de Ministros", "Interponer el recurso de inconstitucionalidad", "Crear, modificar y suprimir por Real Decreto los Ministerios y las Secretarías de Estado", "Proponer al Rey el nombramiento y separación de Vicepresidentes y Ministros", "Resolver los conflictos de atribuciones entre Ministerios"],
         "Disolución y cuestión de confianza: previa **deliberación** del Consejo de Ministros. Referéndum consultivo: previa **autorización del Congreso**",
         "Crear Ministerios es del **Presidente**, por **Real Decreto** (no ley, no Consejo de Ministros). En el referéndum, la autorización es del **Congreso** (no de las Cortes ni del Senado)."))}
""", 2)

T.ap("s4", "I.4 El Consejo de Ministros y las Comisiones Delegadas (Ley 50/1997, arts. 5 y 6)", f"""
{unidad("4.1 Funciones del Consejo de Ministros (Ley 50/1997, art. 5.1)",
  lit("LGOB", "a5", ["como órgano colegiado del Gobierno", "Aprobar el Proyecto de Ley de Presupuestos Generales del Estado", "Aprobar los Reales Decretos-leyes y los Reales Decretos Legislativos", "Declarar los estados de alarma y de excepción y proponer al Congreso de los Diputados la declaración del estado de sitio", "previo dictamen del Consejo de Estado", "Crear, modificar y suprimir los órganos directivos"], solo=list(range(1, 13))),
  fichab("El Consejo de Ministros, órgano colegiado del Gobierno",
         "Los miembros del Gobierno reunidos en Consejo de Ministros (art. 1.3 → I.2.1)",
         ["::Entre otras funciones:", "Aprobar los proyectos de ley y el Proyecto de Ley de Presupuestos", "Aprobar Reales Decretos-leyes y Reales Decretos Legislativos", "Acordar la negociación y firma de Tratados y remitirlos a las Cortes", "Declarar los estados de alarma y de excepción; **proponer** al Congreso el de sitio", "Aprobar los reglamentos de desarrollo y ejecución de las leyes, previo dictamen del Consejo de Estado", "Crear, modificar y suprimir los **órganos directivos** de los Ministerios"],
         "—",
         "Alarma y excepción: los **declara** el Consejo de Ministros; el estado de sitio solo lo **propone** al Congreso (art. 116.4 → III.7.1). Ministerios: el **Presidente** (→ I.3.2); órganos **directivos**: el **Consejo de Ministros**."))}

{unidad("4.2 Quién asiste y secreto de las deliberaciones (Ley 50/1997, art. 5.2 y 3)",
  lit("LGOB", "a5", ["podrán asistir los Secretarios de Estado y excepcionalmente otros altos cargos", "serán secretas"], solo=[13, 14]),
  fichab("Asistencia y deliberaciones del Consejo de Ministros",
         "Pueden asistir los **Secretarios de Estado** y, excepcionalmente, otros altos cargos convocados",
         "—", "—",
         "Las deliberaciones del Consejo de Ministros son **secretas**; las de la Comisión General de Secretarios de Estado y Subsecretarios, **reservadas** (→ I.5.2)."))}

{unidad("4.3 Las Comisiones Delegadas del Gobierno (Ley 50/1997, art. 6)",
  lit("LGOB", "a6", ["mediante Real Decreto, a propuesta del Presidente del Gobierno", "en su caso, Secretarios de Estado", "El régimen interno de funcionamiento y en particular el de convocatorias y suplencias", "Resolver los asuntos que, afectando a más de un Ministerio, no requieran ser elevados al Consejo de Ministros"]),
  fichab("Órganos colegiados del Gobierno para asuntos que afectan a varios Ministerios",
         f"Las crea, modifica y suprime {c('LGOB', 'a6', 'el Consejo de Ministros mediante Real Decreto, a propuesta del Presidente del Gobierno')}; las integran miembros del Gobierno y, en su caso, Secretarios de Estado",
         ["::El Real Decreto de creación especifica en todo caso:", "El miembro del Gobierno que la preside", "Los miembros del Gobierno y, en su caso, Secretarios de Estado que la integran", "Sus funciones", "El miembro al que corresponde la Secretaría", "El régimen interno de funcionamiento (convocatorias y suplencias)"],
         "—",
         "Los Secretarios de Estado, «**en su caso**» (no «en todo caso»). Deliberaciones **secretas** (6.5). Cayó en 2025 como pregunta de reserva (→ Cierre 1)."))}
""", 2)

T.ap("s5", "I.5 Órganos de colaboración y apoyo del Gobierno (Ley 50/1997, arts. 7 a 10)", f"""
{unidad("5.1 Los Secretarios de Estado (Ley 50/1997, art. 7.1 y 2)",
  lit("LGOB", "a7", ["órganos superiores de la Administración General del Estado"], solo=[1, 2]),
  fichab("Órganos de colaboración del Gobierno; no son miembros de él",
         "Secretarios de Estado (de un Departamento o de la Presidencia del Gobierno)",
         "Ejecutan la acción del Gobierno en un sector de actividad, bajo la dirección del Ministro o, si están adscritos a la Presidencia, del Presidente",
         "—",
         "Son **órganos superiores de la Administración General del Estado**, no miembros del Gobierno. Su nombramiento y sus competencias se estudian en el tema I.8."))}

{unidad("5.2 La Comisión General de Secretarios de Estado y Subsecretarios (Ley 50/1997, art. 8)",
  lit("LGOB", "a8", ["corresponde a un Vicepresidente del Gobierno o, en su defecto, al Ministro de la Presidencia", "será ejercida por el Subsecretario de la Presidencia", "serán reservadas", "En ningún caso la Comisión podrá adoptar decisiones o acuerdos por delegación del Gobierno", "El examen de todos los asuntos que vayan a someterse a aprobación del Consejo de Ministros"], solo=list(range(1, 9))),
  fichab("Órgano que prepara las reuniones del Consejo de Ministros",
         ["Titulares de las Secretarías de Estado y Subsecretarios; asiste el Abogado General del Estado", "Preside: un Vicepresidente o, en su defecto, el Ministro de la Presidencia", "Secretaría: el Subsecretario de la Presidencia"],
         "Examina todos los asuntos que van al Consejo de Ministros, salvo nombramientos, ceses, ascensos a oficiales generales y los urgentes",
         "—",
         "Deliberaciones **reservadas** (las del Consejo de Ministros son **secretas**). **Nunca** decide por delegación del Gobierno."))}

{unidad("5.3 El Secretariado del Gobierno (Ley 50/1997, art. 9.1)",
  lit("LGOB", "a9", ["como órgano de apoyo del Consejo de Ministros"], solo=list(range(1, 8))),
  fichab("Órgano de apoyo de los órganos colegiados del Gobierno",
         "Secretariado del Gobierno (integrado en el Ministerio de la Presidencia, art. 9.3)",
         ["Asiste al Ministro-Secretario del Consejo de Ministros", "Remite convocatorias; archiva convocatorias, órdenes del día y actas", "Vela por la calidad técnica de las disposiciones y por su correcta publicación en el BOE"],
         "—",
         "Apoya al Consejo de Ministros, a las Comisiones Delegadas **y** a la Comisión General de Secretarios de Estado y Subsecretarios."))}

{unidad("5.4 Los Gabinetes (Ley 50/1997, art. 10.1)",
  lit("LGOB", "a10", ["sin que en ningún caso puedan adoptar actos o resoluciones que correspondan legalmente a los órganos de la Administración General del Estado"], solo=[1]),
  fichab("Órganos de apoyo político y técnico",
         "Gabinetes del Presidente, de los Vicepresidentes, de los Ministros y de los Secretarios de Estado",
         "Tareas de confianza y asesoramiento especial",
         "—",
         "No pueden dictar actos que correspondan a los órganos de la Administración; sus directores sí, los propios de la jefatura de la unidad que dirigen."))}
""", 2)

T.ap("s6", "I.6 Funcionamiento, delegación y forma de las decisiones (Ley 50/1997, arts. 17, 18, 20 y 24)", f"""
{unidad("6.1 Normas por las que se rige el Gobierno (Ley 50/1997, art. 17)",
  lit("LGOB", "a17", ["Los Reales Decretos del Presidente del Gobierno sobre la composición y organización del Gobierno"]),
  fichab("Fuentes de la organización y funcionamiento del Gobierno", "—",
         ["La Ley 50/1997", "Reales Decretos del Presidente sobre composición y organización del Gobierno y sus órganos de colaboración y apoyo", "Disposiciones organizativas internas del Presidente o del Consejo de Ministros"],
         "—", "La composición y organización del Gobierno la fija el **Presidente** por **Real Decreto**."))}

{unidad("6.2 Las reuniones del Consejo de Ministros (Ley 50/1997, art. 18)",
  lit("LGOB", "a18", ["actuando como Secretario el Ministro de la Presidencia", "carácter decisorio o deliberante", "exclusivamente"]),
  fichab("Funcionamiento del Consejo de Ministros",
         "Convoca y preside el **Presidente del Gobierno**; Secretario: el **Ministro de la Presidencia**",
         ["Reuniones decisorias o deliberantes", "Orden del día fijado por el Presidente", "Acta solo con tiempo y lugar, asistentes, acuerdos e informes presentados"],
         "—",
         "El Secretario del Consejo de Ministros es el **Ministro** de la Presidencia (en la Comisión General es el **Subsecretario** de la Presidencia, → I.5.2). El acta **no** recoge las deliberaciones."))}

{unidad("6.3 Delegación y avocación (Ley 50/1997, art. 20)",
  lit("LGOB", "a20", ["Las atribuidas directamente por la Constitución", "Las relativas al nombramiento y separación de los altos cargos atribuidas al Consejo de Ministros", "mediante acuerdo motivado"]),
  fichab("Delegación y avocación de competencias dentro del Gobierno",
         ["El Presidente delega en Vicepresidentes y Ministros", "Los Ministros, en Secretarios de Estado, Subsecretarios, Delegados del Gobierno y órganos directivos", "Funciones administrativas del Consejo de Ministros → Comisiones Delegadas, a propuesta del Presidente"],
         ["::No delegables en ningún caso:", "Las atribuidas directamente por la Constitución", "Nombramiento y separación de altos cargos atribuidos al Consejo de Ministros", "Las de los órganos colegiados del Gobierno (salvo el 20.2)", "Las de una ley que prohíba expresamente la delegación"],
         "Avocación: acuerdo motivado del Consejo de Ministros, a propuesta del Presidente",
         "Contra el acuerdo de avocación **no cabe recurso** (podrá impugnarse con el que se interponga contra la decisión final)."))}

{unidad("6.4 La forma y la jerarquía de las decisiones del Gobierno (Ley 50/1997, art. 24)",
  lit("LGOB", "a24", ["Reales Decretos del Presidente del Gobierno", "Acuerdos del Consejo de Ministros, las decisiones de dicho órgano colegiado que no deban adoptar la forma de Real Decreto", "Órdenes Ministeriales", "Disposiciones aprobadas por Orden Ministerial"]),
  fichab("Forma que revisten las decisiones del Gobierno y de sus miembros",
         "Gobierno, Presidente, Consejo de Ministros, Comisiones Delegadas y Ministros",
         ["Reales Decretos Legislativos y Reales Decretos-leyes (arts. 82 y 86 CE)", "Reales Decretos del Presidente", "Reales Decretos acordados en Consejo de Ministros", "**Acuerdos** del Consejo de Ministros (lo que no deba ser Real Decreto)", "Acuerdos de Comisiones Delegadas, con forma de Orden", "Órdenes Ministeriales"],
         "Jerarquía de los reglamentos: 1.º Real Decreto (del Presidente o acordado en Consejo de Ministros); 2.º Orden Ministerial",
         "Lo que el Consejo de Ministros decide sin Real Decreto es un **Acuerdo** (no «Orden» ni «Resolución»). Cayó en 2025 (→ Cierre 1). Los decretos-leyes y legislativos: tema IV.2."))}

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Órgano | Quién lo forma | Lo que más se pregunta |
|---|---|---|
| Gobierno (art. 98.1; Ley 50/1997, art. 1.2) | Presidente, Vicepresidentes (en su caso) y Ministros | Los Secretarios de Estado no son miembros |
| Consejo de Ministros (arts. 5 y 18) | Los miembros del Gobierno; secretario, el Ministro de la Presidencia | Deliberaciones **secretas**; formas: Real Decreto o **Acuerdo** |
| Comisiones Delegadas (art. 6) | Miembros del Gobierno y, en su caso, Secretarios de Estado | Creadas por Real Decreto del Consejo de Ministros, a propuesta del Presidente |
| Comisión General de Secretarios de Estado y Subsecretarios (art. 8) | Secretarios de Estado y Subsecretarios | Deliberaciones **reservadas**; nunca decide por delegación |

{resumen([
  "El Gobierno **dirige** la política interior y exterior, la Administración civil y militar y la defensa del Estado, y ejerce la función **ejecutiva** y la potestad **reglamentaria** (art. 97).",
  "Lo forman el **Presidente**, los **Vicepresidentes en su caso** y los **Ministros** (art. 98.1; Ley 50/1997, art. 1.2); se reúnen en Consejo de Ministros y en Comisiones Delegadas.",
  "El Presidente **dirige y coordina** (art. 98.2) y crea los Ministerios **por Real Decreto** (Ley 50/1997, art. 2.2 j).",
  "Consejo de Ministros: deliberaciones **secretas**; lo que no es Real Decreto se adopta como **Acuerdo** (art. 24.1 d)."],
  "Siguiente: II. ¿Cómo se designa al Gobierno, cuándo cesa y de qué responde penalmente?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Cómo se designa al Gobierno, cuándo cesa y de qué responde penalmente? (arts. 99 a 102)", donde(
  "Segunda pregunta. Ya sabemos qué es el Gobierno; ahora, **cómo nace** (investidura del Presidente y nombramiento de los demás miembros), **cuándo cesa** (y qué puede hacer en funciones) y **cómo responde penalmente**. La responsabilidad **política** se ve en el bloque III.",
  ["1 La investidura del Presidente (art. 99; Reglamento del Congreso, arts. 170 a 172)", "2 Los demás miembros: nombramiento, requisitos, suplencia e incompatibilidades (art. 100 y 98.3 y 4; Ley 50/1997, arts. 11 a 14)", "3 El cese y el Gobierno en funciones (art. 101; Ley 50/1997, art. 21)", "4 La responsabilidad criminal (art. 102)"]))

T.ap("s7", "II.1 La investidura del Presidente del Gobierno (art. 99; Reglamento del Congreso, arts. 170 a 172)", f"""
{unidad("1.1 La propuesta de candidato (art. 99.1; Reglamento del Congreso, art. 170)",
  lit("CE", "Artículo 99", ["previa consulta con los representantes designados por los Grupos políticos con representación parlamentaria", "a través del Presidente del Congreso"], solo=[1]),
  lit("RCD", "art170", ["la Presidencia de la Cámara convocará el Pleno"]),
  fichab("Propuesta de candidato a la Presidencia del Gobierno",
         f"{c('CE', 'Artículo 99', 'el Rey')}, {c('CE', 'Artículo 99', 'a través del Presidente del Congreso')}",
         f"{c('CE', 'Artículo 99', 'previa consulta con los representantes designados por los Grupos políticos con representación parlamentaria')}; recibida la propuesta, la Presidencia del Congreso convoca el Pleno",
         f"{c('CE', 'Artículo 99', 'Después de cada renovación del Congreso de los Diputados')} y en los demás supuestos constitucionales (por ejemplo, tras negarse la confianza: art. 114.1 → III.5.1)",
         "Consulta a los **representantes designados por los Grupos políticos con representación parlamentaria** (no a los Grupos Parlamentarios de las dos Cámaras); propone **a través del** Presidente del Congreso (no a propuesta de este). Cayó en 2025 (→ Cierre 1)."))}

{unidad("1.2 Programa y votaciones (art. 99.2 y 3; Reglamento del Congreso, art. 171)",
  lit("CE", "Artículo 99", ["el programa político del Gobierno", "por el voto de la mayoría absoluta de sus miembros", "cuarenta y ocho horas después de la anterior", "mayoría simple"], solo=[2, 3]),
  lit("RCD", "art171", ["sin limitación de tiempo", "la Presidencia del Congreso lo comunicará al Rey o a la Reina"], solo=[2, 5, 6]),
  fichab("Debate y votación de investidura",
         "El **Congreso de los Diputados** (el Senado no interviene); el Rey nombra al investido",
         "El candidato expone el programa político del Gobierno que pretende formar (sin limitación de tiempo) y solicita la confianza",
         ["1.ª votación: **mayoría absoluta** de los miembros del Congreso", "2.ª votación, **48 horas** después: **mayoría simple**"],
         "Las 48 horas se cuentan **desde la votación anterior**. La investidura es solo del **Congreso**."))}

{unidad("1.3 Sucesivas propuestas y disolución a los dos meses (art. 99.4 y 5; Reglamento del Congreso, art. 172)",
  lit("CE", "Artículo 99", ["se tramitarán sucesivas propuestas", "el plazo de dos meses, a partir de la primera votación de investidura", "con el refrendo del Presidente del Congreso"], solo=[4, 5]),
  lit("RCD", "art172", ["someterá a la firma del Rey o de la Reina el Decreto de disolución de las Cortes Generales y de convocatoria de elecciones"], solo=[2]),
  fichab("Qué pasa si ningún candidato obtiene la confianza",
         "El Rey disuelve **ambas Cámaras**; refrenda el **Presidente del Congreso**",
         "Sucesivas propuestas por el mismo procedimiento; si nadie la obtiene en el plazo, disolución y nuevas elecciones",
         "**Dos meses** desde la **primera votación** de investidura",
         "El plazo corre desde la **primera votación**, no desde las elecciones ni desde la constitución de las Cámaras. Refrenda el **Presidente del Congreso**, no el del Gobierno. Esta disolución es la excepción al plazo de un año del art. 115.3 (→ III.6.1)."))}
""", 2)

T.ap("s8", "II.2 Los demás miembros: nombramiento, requisitos, suplencia e incompatibilidades (art. 100; Ley 50/1997, arts. 11 a 14)", f"""
{unidad("2.1 Nombramiento y separación (art. 100)",
  lit("CE", "Artículo 100", ["a propuesta de su Presidente"]),
  fichab("Nombramiento de Vicepresidentes y Ministros",
         f"{c('CE', 'Artículo 100', 'el Rey')}, {c('CE', 'Artículo 100', 'a propuesta de su Presidente')}",
         "Nombramiento y separación",
         "—",
         "El Congreso solo inviste al **Presidente**: los demás miembros los nombra y separa el **Rey a propuesta del Presidente**, sin votación parlamentaria."))}

{unidad("2.2 Requisitos para ser miembro del Gobierno (Ley 50/1997, art. 11)",
  lit("LGOB", "a11", ["ser español, mayor de edad, disfrutar de los derechos de sufragio activo y pasivo", "no estar inhabilitado para ejercer empleo o cargo público por sentencia judicial firme"]),
  fichab("Requisitos de acceso al cargo",
         "Cualquier miembro del Gobierno",
         ["Ser español", "Mayor de edad", "Disfrutar de los derechos de sufragio activo y pasivo", "No estar inhabilitado por sentencia judicial firme", "Requisitos de idoneidad de la Ley 3/2015"],
         "—",
         "No se exige ser Diputado ni Senador."))}

{unidad("2.3 Nombramiento y cese en la Ley 50/1997 (art. 12)",
  lit("LGOB", "a12", ["en los términos previstos en la Constitución", "nombrados y separados por el Rey, a propuesta del Presidente del Gobierno", "como mínimo el cuarenta por ciento", "llevará aparejada la extinción de dichos órganos, salvo"]),
  fichab("Nombramiento, cese y presencia equilibrada",
         ["Presidente: según la Constitución (art. 99 → II.1)", "Vicepresidentes y Ministros: el Rey, a propuesta del Presidente"],
         ["Presencia equilibrada en Vicepresidencias y Ministerios", "La separación de un Vicepresidente o de un Ministro sin cartera extingue el órgano"],
         "Cada sexo, como mínimo el **40 %** en su conjunto (12.2 bis)",
         "La separación del Vicepresidente extingue el órgano **salvo** que se designe otro en sustitución. El estatuto del ex Presidente: **Real Decreto** (12.4)."))}

{unidad("2.4 La suplencia (Ley 50/1997, art. 13)",
  lit("LGOB", "a13", ["por los Vicepresidentes, de acuerdo con el correspondiente orden de prelación", "según el orden de precedencia de los Departamentos", "debiendo recaer, en todo caso, en otro miembro del Gobierno"], solo=[1, 2]),
  fichab("Quién sustituye al Presidente y a los Ministros",
         ["Presidente: los Vicepresidentes por su orden de prelación; en su defecto, los Ministros por el orden de precedencia de los Departamentos", "Ministros: otro miembro del Gobierno"],
         "Suplencia de los Ministros: **Real Decreto del Presidente**, que expresa la causa y el carácter de la suplencia",
         "—",
         "Supuestos: **vacante, ausencia o enfermedad**. El suplente de un Ministro es siempre **otro miembro del Gobierno** (no un Secretario de Estado)."))}

{unidad("2.5 Incompatibilidades (art. 98.3 y 4; Ley 50/1997, art. 14)",
  lit("CE", "Artículo 98", ["que las propias del mandato parlamentario", "actividad profesional o mercantil alguna"], solo=[3, 4]),
  lit("LGOB", "a14", ["el régimen de incompatibilidades de los altos cargos"]),
  fichab("Estatuto e incompatibilidades de los miembros del Gobierno",
         "Todos los miembros del Gobierno",
         ["No pueden ejercer otras funciones representativas, salvo las del mandato parlamentario", "Ni otra función pública que no derive de su cargo", "Ni actividad profesional o mercantil alguna", "Además: régimen de incompatibilidades de los altos cargos (Ley 50/1997, art. 14.2)"],
         "—",
         f"El cargo de miembro del Gobierno **es compatible con el escaño**: la Constitución exceptúa a los miembros del Gobierno de las incompatibilidades parlamentarias de los altos cargos ({c('CE', 'Artículo 70', 'con la excepción de los miembros del Gobierno')}, tema I.5). Pregunta relacionada de 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s9", "II.3 El cese del Gobierno y el Gobierno en funciones (art. 101; Ley 50/1997, art. 21)", f"""
{unidad("3.1 Causas de cese (art. 101.1)",
  lit("CE", "Artículo 101", ["tras la celebración de elecciones generales", "pérdida de la confianza parlamentaria", "por dimisión o fallecimiento de su Presidente"], solo=[1]),
  fichab("Cuándo cesa el Gobierno",
         "El Gobierno en su conjunto",
         ["Celebración de elecciones generales", "Pérdida de la confianza parlamentaria en los casos previstos en la Constitución (cuestión de confianza negada o moción de censura aprobada: art. 114 → III.5.1)", "Dimisión del Presidente", "Fallecimiento del Presidente"],
         "—",
         "Las causas personales son las **del Presidente**: su dimisión o fallecimiento hace cesar **a todo el Gobierno**. La dimisión de un Ministro no."))}

{unidad("3.2 El Gobierno en funciones (art. 101.2; Ley 50/1997, art. 21)",
  lit("CE", "Artículo 101", ["continuará en funciones hasta la toma de posesión del nuevo Gobierno"], solo=[2]),
  lit("LGOB", "a21", ["limitará su gestión al despacho ordinario de los asuntos públicos", "Proponer al Rey la disolución de alguna de las Cámaras", "Plantear la cuestión de confianza", "Proponer al Rey la convocatoria de un referéndum consultivo", "Aprobar el Proyecto de Ley de Presupuestos Generales del Estado", "Presentar proyectos de ley", "quedarán en suspenso"], solo=list(range(3, 12))),
  fichab("Límites del Gobierno cesante",
         "El Gobierno cesante, hasta la **toma de posesión** del nuevo",
         ["Facilita la formación del nuevo Gobierno y el traspaso de poderes", "Limita su gestión al **despacho ordinario**, salvo urgencia o interés general acreditados", "El Presidente en funciones no puede: proponer la disolución, plantear la cuestión de confianza ni proponer un referéndum consultivo", "El Gobierno en funciones no puede: aprobar el Proyecto de Presupuestos ni presentar proyectos de ley"],
         "Las delegaciones legislativas quedan **en suspenso** mientras está en funciones por la celebración de elecciones generales",
         "Son **tres** prohibiciones para el Presidente y **dos** para el Gobierno. Cuidado: la suspensión de las delegaciones legislativas es solo cuando está en funciones **por elecciones generales**."))}
""", 2)

T.ap("s10", "II.4 La responsabilidad criminal del Gobierno (art. 102)", f"""
{unidad("4.1 Fuero, acusación por traición y exclusión del indulto (art. 102)",
  lit("CE", "Artículo 102", ["Sala de lo Penal del Tribunal Supremo", "por iniciativa de la cuarta parte de los miembros del Congreso, y con la aprobación de la mayoría absoluta del mismo", "no será aplicable"]),
  fichab("Responsabilidad criminal del Presidente y de los demás miembros del Gobierno",
         f"Se exige ante {c('CE', 'Artículo 102', 'la Sala de lo Penal del Tribunal Supremo')}",
         f"Acusación por {c('CE', 'Artículo 102', 'traición o por cualquier delito contra la seguridad del Estado en el ejercicio de sus funciones')}: solo a iniciativa del Congreso",
         "Iniciativa: **cuarta parte** de los miembros del Congreso; aprobación: **mayoría absoluta** del Congreso",
         "Para la traición o los delitos contra la seguridad del Estado: **1/4 inicia** y **mayoría absoluta aprueba**, todo en el **Congreso**. El **indulto** (prerrogativa real de gracia) no se aplica a ningún supuesto del artículo."))}

{resumen([
  "El Rey propone candidato **previa consulta con los representantes de los Grupos políticos** con representación parlamentaria y **a través del Presidente del Congreso** (art. 99.1).",
  "Investidura: **mayoría absoluta** en la primera votación; **mayoría simple** 48 horas después; si en **dos meses** desde la primera votación nadie obtiene la confianza, disolución con refrendo del **Presidente del Congreso** (art. 99).",
  "Los demás miembros: los nombra y separa **el Rey a propuesta del Presidente** (art. 100).",
  "El Gobierno cesa por **elecciones**, **pérdida de confianza** o **dimisión o fallecimiento del Presidente**, y sigue **en funciones** hasta la toma de posesión del nuevo (art. 101; Ley 50/1997, art. 21).",
  "Responsabilidad criminal: **Sala de lo Penal del Tribunal Supremo**; traición o delitos contra la seguridad del Estado: iniciativa de **1/4** y aprobación por **mayoría absoluta** del Congreso; **sin indulto** (art. 102)."],
  "Siguiente: III. ¿Cómo se relacionan el Gobierno y las Cortes?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Cómo se relacionan el Gobierno y las Cortes? Control y responsabilidad política (arts. 108 a 116)", donde(
  "Tercera pregunta. El Título V de la Constitución, " + c("CE", "tv", "De las relaciones entre el Gobierno y las Cortes Generales") + ", regula cómo las Cámaras **controlan** al Gobierno y cómo el Congreso puede **exigirle la responsabilidad política** o **renovarle la confianza**; y, a la inversa, cómo el Presidente puede **disolver** las Cámaras.",
  ["1 Responsabilidad política solidaria y control (art. 108; Ley 50/1997, art. 29)", "2 Información, presencia, interpelaciones y preguntas (arts. 109 a 111; Reglamento del Congreso)", "3 La cuestión de confianza (art. 112)", "4 La moción de censura (art. 113)", "5 Efectos de la pérdida de confianza (art. 114)", "6 La disolución anticipada (art. 115)", "7 Los estados de alarma, excepción y sitio: el papel del Congreso (art. 116)", "8 Cuadro: investidura, cuestión de confianza y moción de censura"]))

T.ap("s11", "III.1 Responsabilidad política solidaria y control del Gobierno (art. 108; Ley 50/1997, art. 29)", f"""
{unidad("1.1 El Gobierno responde ante el Congreso (art. 108)",
  lit("CE", "Artículo 108", ["responde solidariamente en su gestión política ante el Congreso de los Diputados"]),
  fichab("Responsabilidad política del Gobierno",
         "El Gobierno (responde) ante el **Congreso de los Diputados**",
         "**Solidariamente**: responde el Gobierno como conjunto de su gestión política",
         "—",
         "Ante el **Congreso** (no ante las Cortes Generales ni ante el Senado). Los instrumentos para exigirla son la cuestión de confianza y la moción de censura (→ III.3 y → III.4)."))}

{unidad("1.2 El control de los actos del Gobierno (Ley 50/1997, art. 29)",
  lit("LGOB", "a29", ["al control político de las Cortes Generales", "son impugnables ante la jurisdicción contencioso-administrativa", "impugnable ante el Tribunal Constitucional"]),
  fichab("Tres controles sobre el Gobierno",
         ["Cortes Generales: control político", "Jurisdicción contencioso-administrativa: actos, inactividad y vía de hecho", "Tribunal Constitucional: en los términos de su Ley Orgánica"],
         f"El Gobierno {c('LGOB', 'a29', 'está sujeto a la Constitución y al resto del ordenamiento jurídico en toda su actuación')}",
         "—",
         "El control político alcanza a **todos los actos y omisiones** del Gobierno y es de las **Cortes Generales** (art. 29.2); la responsabilidad política solidaria, en cambio, es ante el **Congreso** (art. 108 CE)."))}
""", 2)

T.ap("s12", "III.2 Información, presencia, interpelaciones y preguntas (arts. 109 a 111; Reglamento del Congreso, arts. 180 a 187)", f"""
{unidad("2.1 Petición de información (art. 109)",
  lit("CE", "Artículo 109", ["a través de los Presidentes de aquéllas"]),
  fichab("Derecho de las Cámaras a recabar información y ayuda",
         "Las Cámaras y sus Comisiones, **a través de sus Presidentes**",
         f"Recaban información y ayuda {c('CE', 'Artículo 109', 'del Gobierno y de sus Departamentos y de cualesquiera autoridades del Estado y de las Comunidades Autónomas')}",
         "—", "Alcanza también a autoridades de las **Comunidades Autónomas**."))}

{unidad("2.2 Presencia de los miembros del Gobierno (art. 110)",
  lit("CE", "Artículo 110", ["pueden reclamar la presencia de los miembros del Gobierno", "la facultad de hacerse oír en ellas"]),
  fichab("Comparecencias y acceso a las Cámaras",
         ["Las Cámaras y sus Comisiones: reclaman la presencia", "Los miembros del Gobierno: tienen acceso y voz"],
         "Los miembros del Gobierno pueden pedir que informen **funcionarios de sus Departamentos**",
         "—", "Es un derecho en las dos direcciones: las Cámaras **reclaman** la presencia y los miembros del Gobierno **tienen acceso** y pueden **hacerse oír**."))}

{unidad("2.3 Interpelaciones y mociones (art. 111; Reglamento del Congreso, arts. 180, 181.1 y 184)",
  lit("CE", "Artículo 111", ["un tiempo mínimo semanal", "Toda interpelación podrá dar lugar a una moción"]),
  lit("RCD", "art180", ["Los diputados y diputadas y los grupos parlamentarios"]),
  lit("RCD", "art181", ["cuestiones de política general"], solo=[1]),
  lit("RCD", "art184", ["en el día siguiente al de la sustanciación"], solo=[1, 2]),
  fichab("Interpelación: control sobre la política general del Gobierno",
         "En el Congreso: los **diputados y diputadas** y los **grupos parlamentarios**; se dirige al Gobierno y a cada uno de sus miembros",
         ["Por escrito ante la Mesa, sobre los motivos o propósitos de la conducta del Ejecutivo en **política general**", "Puede dar lugar a una **moción** en que la Cámara manifieste su posición"],
         "Tiempo mínimo **semanal** (lo fijan los Reglamentos); moción: el día siguiente al de la sustanciación ante el Pleno",
         "La interpelación puede acabar en **moción** (art. 111.2); la pregunta no. Si el escrito no es propio de una interpelación, la Mesa lo convierte en pregunta (RCD 181.2)."))}

{unidad("2.4 Preguntas (Reglamento del Congreso, arts. 185 a 187)",
  lit("RCD", "art185", ["Las diputadas y los diputados"]),
  lit("RCD", "art186", ["ni la que suponga consulta de índole estrictamente jurídica"], solo=[1, 2]),
  lit("RCD", "art187", ["se entenderá que quien formula la pregunta solicita respuesta por escrito"]),
  fichab("Pregunta: control sobre un hecho, situación o información",
         "Las diputadas y los diputados (no los grupos), al Gobierno y a sus miembros",
         ["Por escrito ante la Mesa", "No se admite la de exclusivo interés personal ni la consulta de índole estrictamente jurídica"],
         "—",
         "Sin indicación, la respuesta es **por escrito**; si se pide oral sin especificar, es **en Comisión**. Las interpelaciones las pueden formular también los **grupos**; las preguntas, solo los **diputados**."))}
""", 2)

T.ap("s13", "III.3 La cuestión de confianza (art. 112; Reglamento del Congreso, arts. 173 y 174)", f"""
{unidad("3.1 Planteamiento y votación (art. 112; Reglamento del Congreso, art. 174)",
  lit("CE", "Artículo 112", ["previa deliberación del Consejo de Ministros", "sobre su programa o sobre una declaración de política general", "la mayoría simple de los Diputados"]),
  lit("RCD", "art174", ["escrito motivado", "veinticuatro horas desde su presentación", "la mayoría simple de los miembros de la Cámara"], solo=[1, 4, 5]),
  fichab("El Presidente pide al Congreso que renueve su confianza",
         "La plantea el **Presidente del Gobierno**, previa **deliberación** del Consejo de Ministros, ante el **Congreso**",
         ["Sobre su **programa** o sobre una **declaración de política general**", "Escrito motivado ante la Mesa, con certificación del Consejo de Ministros", "Debate con las normas del de investidura (RCD 174.3)"],
         ["Se otorga con **mayoría simple**", "No se vota hasta pasadas **24 horas** desde su presentación"],
         "Iniciativa **del Presidente** (no del Congreso); el Consejo de Ministros **delibera**, no autoriza. Mayoría **simple** (la censura exige **absoluta**). Si se niega: → III.5.1."))}
""", 2)

T.ap("s14", "III.4 La moción de censura (art. 113; Reglamento del Congreso, arts. 175 a 179)", f"""
{unidad("4.1 Requisitos, plazos y mayoría (art. 113)",
  lit("CE", "Artículo 113", ["por mayoría absoluta", "al menos por la décima parte de los Diputados", "un candidato a la Presidencia del Gobierno", "cinco días desde su presentación", "En los dos primeros días", "durante el mismo período de sesiones"]),
  fichab("El Congreso exige la responsabilidad política del Gobierno",
         "La proponen al menos **1/10 de los Diputados**; decide el **Congreso**",
         "Debe incluir un **candidato a la Presidencia del Gobierno**; caben mociones alternativas",
         ["Aprobación: **mayoría absoluta**", "No se vota hasta pasados **cinco días** desde su presentación", "Mociones alternativas: en los **dos primeros días**"],
         "Si no se aprueba, sus **signatarios** no pueden presentar otra **en el mismo período de sesiones**. Mayoría **absoluta** (no simple). Cayó en 2025 (→ Cierre 1)."))}

{unidad("4.2 Tramitación en el Congreso (Reglamento del Congreso, arts. 175.2, 177.4 y 5 y 179)",
  lit("RCD", "art175", ["que haya aceptado la candidatura"], solo=[2]),
  lit("RCD", "art177", ["no podrá ser anterior al transcurso de cinco días desde la presentación de la primera", "el voto favorable de la mayoría absoluta de los miembros del Congreso"], solo=[4, 5]),
  lit("RCD", "art179", ["se imputará al siguiente período de sesiones"]),
  fichab("Cómo se tramita la moción de censura",
         "Al menos la décima parte de la Cámara; el candidato tiene que haber **aceptado** la candidatura",
         "Escrito motivado dirigido a la Mesa; si hay varias mociones, pueden debatirse juntas pero se votan **por separado**, por orden de presentación",
         "Votación: no antes de **cinco días** desde la presentación de la **primera**; aprobación: **mayoría absoluta de los miembros** del Congreso",
         "La presentada **entre períodos de sesiones** se imputa al **siguiente** período (a efectos de la prohibición de firmar otra)."))}
""", 2)

T.ap("s15", "III.5 Efectos de la pérdida de confianza (art. 114; Reglamento del Congreso, art. 178)", f"""
{unidad("5.1 Dimisión del Gobierno y nuevo Presidente (art. 114)",
  lit("CE", "Artículo 114", ["presentará su dimisión al Rey", "según lo dispuesto en el artículo 99", "se entenderá investido de la confianza de la Cámara"]),
  lit("RCD", "art178", ["se considerará que ha recibido la confianza de la Cámara"]),
  fichab("Qué pasa cuando el Gobierno pierde la confianza del Congreso",
         "El Gobierno dimite ante el **Rey**; el Rey nombra al nuevo Presidente",
         ["Confianza **negada**: dimisión y nueva designación por el procedimiento del art. 99 (→ II.1)", "Censura **aprobada**: dimisión y el **candidato de la moción** se entiende investido; el Rey lo nombra"],
         "—",
         "Con la moción de censura **no hay nueva investidura**: el candidato incluido en ella queda investido. Con la cuestión de confianza negada, se abre el procedimiento del art. 99."))}
""", 2)

T.ap("s16", "III.6 La disolución anticipada de las Cortes (art. 115)", f"""
{unidad("6.1 Propuesta del Presidente y límites (art. 115)",
  lit("CE", "Artículo 115", ["bajo su exclusiva responsabilidad", "El decreto de disolución fijará la fecha de las elecciones", "cuando esté en trámite una moción de censura", "antes de que transcurra un año desde la anterior"]),
  fichab("Disolución del Congreso, del Senado o de las Cortes Generales",
         "La **propone** el Presidente del Gobierno, previa deliberación del Consejo de Ministros y bajo su exclusiva responsabilidad; la **decreta** el Rey",
         "El decreto de disolución fija la fecha de las elecciones",
         ["No cabe mientras esté **en trámite una moción de censura**", "No cabe nueva disolución antes de **un año** desde la anterior, salvo la del art. 99.5 (→ II.1.3)"],
         "Puede disolverse **una sola Cámara** o las dos. Tampoco cabe disolver el **Congreso** durante los estados de alarma, excepción o sitio (art. 116.5 → III.7.1); ni puede proponerla el Presidente **en funciones** (→ II.3.2)."))}
""", 2)

T.ap("s17", "III.7 Los estados de alarma, de excepción y de sitio: el papel del Congreso (art. 116)", f"""
El régimen completo de los tres estados (LO 4/1981 y derechos que pueden suspenderse) se estudia en el tema I.2. Aquí interesa la **relación entre el Gobierno y el Congreso** que dibuja el art. 116.

{unidad("7.1 Quién declara cada estado y qué hace el Congreso (art. 116.2 a 5)",
  lit("CE", "Artículo 116", ["por un plazo máximo de quince días", "previa autorización del Congreso de los Diputados", "por la mayoría absoluta del Congreso de los Diputados, a propuesta exclusiva del Gobierno", "No podrá procederse a la disolución del Congreso"], solo=[2, 3, 4, 5, 6]),
  fichab("Intervención del Gobierno y del Congreso en los estados excepcionales",
         ["Alarma: la declara el **Gobierno** y da cuenta al Congreso", "Excepción: la declara el **Gobierno**, previa **autorización** del Congreso", "Sitio: la declara el **Congreso** por mayoría absoluta, a propuesta exclusiva del Gobierno"],
         "Por decreto acordado en Consejo de Ministros (alarma y excepción)",
         ["Alarma: máximo **15 días**; la prórroga exige autorización del Congreso", "Excepción: máximo **30 días**, prorrogables por otros 30", "Sitio: mayoría **absoluta** del Congreso"],
         "Mientras dure cualquiera de los tres **no puede disolverse el Congreso**; si está disuelto o expirado su mandato, sus competencias las asume la **Diputación Permanente**."))}
""", 2)

T.ap("s18", "III.8 Cuadro: investidura, cuestión de confianza y moción de censura (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| | Investidura (art. 99) | Cuestión de confianza (art. 112) | Moción de censura (art. 113) |
|---|---|---|---|
| Quién la inicia | El Rey propone candidato | El **Presidente**, previa deliberación del Consejo de Ministros | **1/10** de los Diputados, con candidato |
| Ante quién | Congreso | Congreso | Congreso |
| Mayoría | Absoluta en la 1.ª votación; simple 48 horas después | **Simple** | **Absoluta** |
| Plazo antes de votar | — | 24 horas desde la presentación (RCD 174.4) | **5 días** desde la presentación (alternativas: 2 primeros días) |
| Si sale mal | Nuevas propuestas; a los **2 meses**, disolución (99.5) | El Gobierno dimite; nuevo Presidente por el art. 99 (114.1) | Rechazada: sus firmantes no pueden presentar otra en el mismo período de sesiones (113.4) |
| Si sale bien | El Rey nombra Presidente | Sigue el Gobierno | El Gobierno dimite y el candidato queda investido (114.2) |

{resumen([
  "El Gobierno responde **solidariamente** de su gestión política ante el **Congreso** (art. 108).",
  "Control ordinario: información (109), presencia (110), **interpelaciones** (pueden acabar en moción) y **preguntas**, con un tiempo mínimo **semanal** (111).",
  "Cuestión de confianza: la plantea el **Presidente** previa deliberación del Consejo de Ministros; se otorga por **mayoría simple** (112).",
  "Moción de censura: **1/10** de los Diputados, con **candidato**, **5 días** de espera y **mayoría absoluta** (113); si prospera, el candidato queda **investido** (114.2).",
  "Disolución: la propone el Presidente y la decreta el Rey; no con una moción de censura **en trámite** ni antes de **un año** desde la anterior, salvo la del art. 99.5 (115)."],
  "Siguiente: IV. ¿Qué es el Consejo de Estado?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Qué es el Consejo de Estado? (art. 107; LO 3/1980)", donde(
  "Cuarta pregunta. El Gobierno no decide solo: para muchos asuntos debe oír antes al **supremo órgano consultivo**. La Constitución lo crea en una línea (art. 107) y remite a una **ley orgánica** su composición y competencia: la LO 3/1980.",
  ["1 Naturaleza y función consultiva (art. 107; LO 3/1980, arts. 1 y 2)", "2 Órganos y miembros (arts. 3 a 10)", "3 Estatuto de los Consejeros, Secciones y funcionamiento (arts. 11 a 13, 16 y 19)", "4 Competencias: Pleno y Comisión Permanente (arts. 21, 22, 24 y 25)", "5 Cuadro de la composición del Consejo de Estado"]))

T.ap("s19", "IV.1 Naturaleza y función consultiva (art. 107; LO 3/1980, arts. 1 y 2)", f"""
{unidad("1.1 Supremo órgano consultivo del Gobierno (art. 107; LO 3/1980, art. 1)",
  lit("CE", "Artículo 107", ["el supremo órgano consultivo del Gobierno", "Una ley orgánica regulará su composición y competencia"]),
  lit("LO3_1980", "aprimero", ["con autonomía orgánica y funcional"], solo=[1, 2]),
  fichab("El Consejo de Estado",
         "Órgano consultivo **del Gobierno**",
         f"Ejerce la función consultiva {c('LO3_1980', 'aprimero', 'con autonomía orgánica y funcional para garantizar su objetividad e independencia')}",
         "Composición y competencia: por **ley orgánica** (LO 3/1980)",
         "Es **supremo** órgano consultivo **del Gobierno** (no de las Cortes). Tiene sede en el Palacio de los Consejos de Madrid (art. 1.3)."))}

{unidad("1.2 Los dictámenes: preceptivos o facultativos, y no vinculantes (LO 3/1980, art. 2)",
  lit("LO3_1980", "asegundo", ["Valorará los aspectos de oportunidad y conveniencia", "preceptiva cuando en esta o en otras leyes así se establezca, y facultativa en los demás casos", "no serán vinculantes, salvo que la ley disponga lo contrario", "Corresponderá en todo caso al Consejo de Ministros resolver", "de acuerdo con el Consejo de Estado", "oído el Consejo de Estado"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Cómo dictamina el Consejo de Estado",
         "Dictamina sobre lo que le sometan **el Gobierno o sus miembros**",
         ["Vela por la Constitución y el ordenamiento; valora oportunidad y conveniencia si lo exige el asunto o lo pide el consultante", "Consulta **preceptiva** si una ley lo establece; **facultativa** en los demás casos", "Dictamen **no vinculante**, salvo que la ley disponga lo contrario"],
         "Si el Ministro disiente en una consulta preceptiva, resuelve el **Consejo de Ministros**",
         "Fórmulas: «**de acuerdo con** el Consejo de Estado» (conforme) y «**oído** el Consejo de Estado» (se aparta). Tras dictamen del **Pleno**, ningún otro órgano informa; tras el de la Comisión Permanente, solo el Pleno."))}
""", 2)

T.ap("s20", "IV.2 Órganos y miembros del Consejo de Estado (LO 3/1980, arts. 3 a 10)", f"""
{unidad("2.1 Cómo actúa y quién forma el Pleno (LO 3/1980, arts. 3 y 4)",
  lit("LO3_1980", "atercero", ["en Pleno, en Comisión Permanente o en Comisión de Estudios"]),
  lit("LO3_1980", "acuarto", ["El Presidente y los demás Miembros del Gobierno podrán asistir"]),
  fichab("Órganos del Consejo de Estado y composición del Pleno",
         ["Pleno: Presidente, Consejeros permanentes, natos y electivos y Secretario general"],
         "Actúa en **Pleno**, **Comisión Permanente** o **Comisión de Estudios**; también en secciones",
         "—",
         "En el Pleno **no hay vicepresidente**. El Presidente y los miembros del Gobierno pueden **asistir** al Pleno e informar en él. Cayó en 2025 (→ Cierre 1)."))}

{unidad("2.2 Comisión Permanente y Comisión de Estudios (LO 3/1980, art. 5)",
  lit("LO3_1980", "aquinto", ["el Presidente, los Consejeros permanentes y el Secretario general", "dos Consejeros permanentes, dos natos y dos electivos"], solo=[1, 2]),
  fichab("Las dos comisiones del Consejo de Estado",
         ["Comisión Permanente: Presidente, Consejeros **permanentes** y Secretario general", "Comisión de Estudios: Presidente, **2 permanentes, 2 natos y 2 electivos** (designados por el Pleno) y el Secretario General"],
         "—", "—",
         "En la Comisión Permanente solo hay Consejeros **permanentes**; en la de Estudios, de las **tres** clases."))}

{unidad("2.3 El Presidente (LO 3/1980, art. 6)",
  lit("LO3_1980", "asexto", ["nombrado libremente por Real Decreto acordado en Consejo de Ministros y refrendado por su Presidente", "entre juristas de reconocido prestigio y experiencia en asuntos de Estado"]),
  fichab("Presidente del Consejo de Estado",
         "Nombrado **libremente** por Real Decreto acordado en Consejo de Ministros, refrendado por el Presidente del Gobierno",
         "Entre **juristas de reconocido prestigio y experiencia en asuntos de Estado**",
         "—",
         "Le sustituye el Consejero **permanente** que corresponda por el orden de las Secciones."))}

{unidad("2.4 Los Consejeros permanentes (LO 3/1980, art. 7)",
  lit("LO3_1980", "aseptimo", ["en numero igual al de las Secciones del Consejo, son nombrados, sin límite de tiempo, por Real Decreto", "Ex Gobernadores del Banco de España"]),
  fichab("Consejeros permanentes",
         "Tantos como **Secciones** (mínimo ocho: → IV.3.3)",
         "Nombrados por Real Decreto entre quienes estén o hayan estado en alguna de las **diez** categorías del artículo (Ministro, Consejero de Estado, Letrado Mayor, catedrático con 15 años, funcionarios con 15 años en cuerpos de titulado universitario, ex Gobernadores del Banco de España…)",
         "**Sin límite de tiempo**; presencia equilibrada: cada sexo, mínimo el **40 %**",
         "Los **ex** Gobernadores del Banco de España son categoría de Consejero **permanente**; el Gobernador **en ejercicio** es Consejero **nato** (→ IV.2.5)."))}

{unidad("2.5 Los Consejeros natos (LO 3/1980, art. 8)",
  lit("LO3_1980", "aoctavo", ["con carácter vitalicio", "El Fiscal General del Estado", "El Gobernador del Banco de España"]),
  fichab("Consejeros natos",
         ["Los ex Presidentes del Gobierno, con carácter **vitalicio**, si manifiestan su voluntad de incorporarse", "Por su cargo: Director de la RAE y Presidentes de las Reales Academias de Ciencias Morales y Políticas y de Jurisprudencia y Legislación; Presidente del CES; **Fiscal General del Estado**; JEMAD; Presidente del Consejo General de la Abogacía; Presidente de la Comisión General de Codificación; Abogado General del Estado; Director del CEPC; **Gobernador del Banco de España**"],
         "Lo son por razón del cargo (o por haber sido Presidente del Gobierno)",
         "Mientras ostenten el cargo (art. 11.2); los ex Presidentes, vitalicios",
         "Cayó en 2025: el **Fiscal General del Estado** es nato; el Defensor del Pueblo, el Presidente del Tribunal de Cuentas y los del CGPJ son cargos para nombrar Consejeros **electivos** (→ IV.2.6; → Cierre 1)."))}

{unidad("2.6 Los Consejeros electivos (LO 3/1980, art. 9)",
  lit("LO3_1980", "anoveno", ["en número de diez", "por un período de cuatro años", "Defensor del Pueblo", "Presidente del Tribunal de Cuentas", "Su mandato será de ocho años"]),
  fichab("Consejeros electivos",
         "**Diez**, nombrados por Real Decreto entre quienes hayan desempeñado alguno de los cargos del art. 9.1 (Diputado o Senador, Magistrado del TC, Defensor del Pueblo, Presidente o Vocal del CGPJ, Ministro o Secretario de Estado, Presidente del Tribunal de Cuentas, Rector…)",
         "Dos de los diez: ex Presidentes de Consejo Ejecutivo autonómico durante al menos ocho años",
         ["Mandato: **cuatro años**", "Los dos ex Presidentes autonómicos: **ocho años**", "Presencia equilibrada: cada sexo, mínimo el 40 %"],
         "**Diez** (no doce) y **cuatro** años. Se exige **haber desempeñado** el cargo."))}

{unidad("2.7 El Secretario general (LO 3/1980, art. 10)",
  lit("LO3_1980", "adiez", ["entre los Letrados Mayores", "con voz pero sin voto"]),
  fichab("Secretario general del Consejo de Estado",
         "Nombrado por Real Decreto **entre los Letrados Mayores**, a propuesta de la Comisión Permanente aprobada por el Pleno",
         "Asiste a las sesiones del Pleno, de la Comisión Permanente y de la Comisión de Estudios",
         "—", "Tiene **voz pero no voto**."))}
""", 2)

T.ap("s21", "IV.3 Estatuto de los Consejeros, Secciones y funcionamiento (LO 3/1980, arts. 11 a 13, 16 y 19)", f"""
{unidad("3.1 Inamovilidad y cese (LO 3/1980, art. 11)",
  lit("LO3_1980", "aonce", ["inamovibles", "informe favorable del Consejo de Estado en Pleno"], solo=[1, 2, 3]),
  fichab("Estatuto de los Consejeros",
         ["Permanentes: **inamovibles**", "Natos: mientras ostenten el cargo", "Electivos: durante su mandato"],
         "Cese de permanentes y electivos solo por renuncia, delito, incapacidad permanente o incumplimiento de su función",
         "Real Decreto acordado en Consejo de Ministros, previa audiencia del interesado e **informe favorable del Pleno**",
         "La separación de Consejeros permanentes es asunto del **Pleno** (art. 21.9 → IV.4.1)."))}

{unidad("3.2 Incompatibilidades (LO 3/1980, art. 12.1 y 2)",
  lit("LO3_1980", "adoce", ["incompatibles con los mandatos de Diputado, Senador o miembro de una Asamblea de Comunidad Autónoma"], solo=[1, 2]),
  fichab("Incompatibilidades del Presidente y de los Consejeros permanentes", "Presidente y Consejeros permanentes",
         ["Las de los altos cargos de la Administración del Estado", "Incompatibles con el mandato de Diputado, Senador o miembro de Asamblea autonómica"],
         "—", "La incompatibilidad con el escaño afecta al **Presidente** y a los **permanentes** (no a natos ni electivos)."))}

{unidad("3.3 Las Secciones (LO 3/1980, art. 13.1 a 3)",
  lit("LO3_1980", "atrece", ["ocho como mínimo", "un Consejero permanente que la preside"], solo=[1, 2, 3]),
  fichab("Secciones del Consejo de Estado",
         "Cada Sección: un **Consejero permanente** que la preside, un Letrado Mayor y los Letrados necesarios",
         "Ampliables reglamentariamente a propuesta de la Comisión Permanente, si el volumen de consultas lo exige",
         "**Ocho** como mínimo",
         "Mínimo **ocho**, presididas por un Consejero **permanente**. Cayó en 2025 (→ Cierre 1)."))}

{unidad("3.4 Quórum y acuerdos (LO 3/1980, art. 16)",
  lit("LO3_1980", "adieciseis", ["la de la mitad, al menos, de los Consejeros que lo formen", "por mayoría absoluta de votos de los asistentes", "voto de calidad"], solo=[1, 3, 4]),
  fichab("Cómo delibera y acuerda", "Pleno y Comisión Permanente",
         ["Quórum: Presidente (o quien haga sus veces), la **mitad** al menos de los Consejeros y el Secretario general", "Voto particular por escrito de los discrepantes"],
         "Acuerdos por **mayoría absoluta de votos de los asistentes**; empate: voto de calidad de quien presida",
         "La mayoría absoluta se cuenta sobre los **asistentes**, no sobre los miembros."))}

{unidad("3.5 Dictámenes urgentes (LO 3/1980, art. 19)",
  lit("LO3_1980", "adiecinueve", ["el plazo máximo para su despacho será de quince días", "inferior a diez días"]),
  fichab("Plazo de los dictámenes urgentes", "El Gobierno o su Presidente pueden fijar un plazo inferior",
         "Si el plazo es inferior a diez días, despacha la **Comisión Permanente** aunque el asunto sea del Pleno",
         ["Urgencia: máximo **15 días**", "Plazo inferior a **10 días**: Comisión Permanente"],
         "El Gobierno puede pedir después el dictamen del **Pleno**."))}
""", 2)

T.ap("s22", "IV.4 Competencias: Pleno y Comisión Permanente (LO 3/1980, arts. 21, 22, 24 y 25)", f"""
{unidad("4.1 Consultas al Pleno (LO 3/1980, art. 21)",
  lit("LO3_1980", "aveintiuno", ["Anteproyectos de reforma constitucional", "Proyectos de Decretos legislativos", "Separación de Consejeros permanentes", "Asuntos de Estado a los que el Gobierno reconozca especial trascendencia o repercusión"]),
  fichab("Asuntos en que debe consultarse al Pleno", "El Consejo de Estado en **Pleno**",
         ["Anteproyectos de reforma constitucional (si la propuesta no es del propio Consejo)", "Anteproyectos de ley en ejecución de tratados y del Derecho de la UE", "**Proyectos de Decretos legislativos**", "Dudas sobre tratados y problemas jurídicos de actos de organizaciones internacionales", "Protección diplomática", "Transacciones y arbitrajes sobre derechos de la Hacienda Pública", "Separación de Consejeros permanentes", "Asuntos de Estado de especial trascendencia"],
         "—",
         "Al **Pleno**: **anteproyectos de ley** y **proyectos de decretos legislativos**. A la **Comisión Permanente**: **reglamentos** y disposiciones reglamentarias (→ IV.4.2)."))}

{unidad("4.2 Consultas a la Comisión Permanente (LO 3/1980, art. 22; art. 153 b CE)",
  lit("LO3_1980", "aveintidos", ["Reglamentos o disposiciones de carácter general que se dicten en ejecución de las Leyes", "Anteproyectos de Ley Orgánica de transferencias", "Control del ejercicio de funciones delegadas por el Estado a las Comunidades Autónomas", "Recursos administrativos de revisión", "Concesión de créditos extraordinarios o suplementos de crédito", "no se diga expresamente que debe ser al Consejo en Pleno"]),
  lit("CE", "Artículo 153", ["Por el Gobierno, previo dictamen del Consejo de Estado"], solo=[1, 3]),
  fichab("Asuntos en que debe consultarse a la Comisión Permanente", "La **Comisión Permanente**",
         ["Necesidad de autorización de las Cortes para los tratados", "Reglamentos de ejecución de las leyes y de tratados y Derecho de la UE", "Anteproyectos de LO de transferencia o delegación a las CC. AA. y control de las funciones delegadas", "Impugnación ante el TC de disposiciones autonómicas", "Conflictos de atribuciones entre Ministerios", "Recursos de revisión; revisión de oficio; contratos y concesiones con oposición; responsabilidad patrimonial", "Créditos extraordinarios y suplementos de crédito"],
         "—",
         f"Es la **cláusula residual**: va a la Comisión Permanente todo asunto en que una ley exija consultar al Consejo de Estado sin decir que sea al Pleno. El control de funciones delegadas a las CC. AA. lo ejerce el Gobierno {c('CE', 'Artículo 153', 'previo dictamen del Consejo de Estado')} (pregunta relacionada de 2025, → Cierre 1)."))}

{unidad("4.3 Comunidades Autónomas y consulta facultativa (LO 3/1980, arts. 24 y 25)",
  lit("LO3_1980", "aveinticuatro", ["por conducto de sus Presidentes", "que carezcan de órgano consultivo propio"]),
  lit("LO3_1980", "aveinticinco", ["sin ser obligatoria la consulta"]),
  fichab("Otros consultantes y consultas no obligatorias",
         ["Comunidades Autónomas, por conducto de sus **Presidentes**", "Presidente del Gobierno o cualquier Ministro (consulta facultativa)"],
         ["Dictamen preceptivo para las CC. AA. **sin órgano consultivo propio**, en los mismos casos que para el Estado", "El Pleno dictamina asuntos de la Comisión Permanente si lo pide el Presidente del Gobierno o lo acuerda el Presidente del Consejo"],
         "—",
         "Las CC. AA. piden el dictamen por medio de **sus Presidentes**."))}
""", 2)

T.ap("s23", "IV.5 Cuadro de la composición del Consejo de Estado (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Miembro | Cuántos | Cómo y entre quiénes | Duración |
|---|---|---|---|
| Presidente (art. 6) | 1 | Libremente, Real Decreto acordado en Consejo de Ministros; juristas de reconocido prestigio | — |
| Consejeros permanentes (art. 7) | Igual al de Secciones (mínimo 8) | Real Decreto; 10 categorías (ex Ministros, Letrados Mayores, ex Gobernadores del Banco de España…) | **Sin límite de tiempo**; inamovibles |
| Consejeros natos (art. 8) | Por cargo | Ex Presidentes del Gobierno; Fiscal General, Gobernador del Banco de España, JEMAD, Director de la RAE… | Mientras ostenten el cargo (ex Presidentes: vitalicio) |
| Consejeros electivos (art. 9) | **10** | Real Decreto; haber sido Diputado, Senador, Defensor del Pueblo, Presidente del Tribunal de Cuentas… | **4 años** (2 de ellos, 8 años) |
| Secretario general (art. 10) | 1 | Real Decreto, entre Letrados Mayores | Voz sin voto |

{resumen([
  "El Consejo de Estado es el **supremo órgano consultivo del Gobierno**; una **ley orgánica** regula su composición y competencia (art. 107; LO 3/1980).",
  "Dictámenes: consulta **preceptiva** si una ley lo establece y **facultativa** en los demás casos; **no vinculantes** salvo que la ley disponga otra cosa.",
  "Pleno: Presidente, Consejeros **permanentes** (sin límite de tiempo), **natos** (por cargo) y **electivos** (**diez**, **cuatro años**) y Secretario general; Secciones: **ocho como mínimo**, presididas por un Consejero permanente.",
  "Pleno: anteproyectos de reforma constitucional y **proyectos de decretos legislativos**; Comisión Permanente: **reglamentos** ejecutivos y cláusula residual."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_L4 = examen("L", 4, {
  "a": f"No es libre: el art. 99.1 exige que el Rey proponga {c('CE', 'Artículo 99', 'previa consulta con los representantes designados por los Grupos políticos con representación parlamentaria')}.",
  "b": "Cambia a quién se consulta: no a los «Grupos Parlamentarios del Congreso y el Senado», sino a los **representantes designados por los Grupos políticos con representación parlamentaria**; el art. 99.1 no menciona al Senado.",
  "c": f"Literal del art. 99.1: {c('CE', 'Artículo 99', 'previa consulta con los representantes designados por los Grupos políticos con representación parlamentaria')}.",
  "d": f"El Presidente del Congreso no propone: el Rey propone {c('CE', 'Artículo 99', 'a través del Presidente del Congreso')}."},
  [("representantes designados por los grupos políticos con representación parlamentaria", "CE", "Artículo 99", "previa consulta con los representantes designados por los Grupos políticos con representación parlamentaria")])
EX_X15 = examen("X", 15, {
  "a": f"La moción no la presenta el Presidente del Gobierno: {c('CE', 'Artículo 113', 'deberá ser propuesta al menos por la décima parte de los Diputados')} (art. 113.2). El Presidente plantea, en cambio, la cuestión de confianza (art. 112).",
  "b": f"Literal del art. 113.1: {c('CE', 'Artículo 113', 'El Congreso de los Diputados puede exigir la responsabilidad política del Gobierno mediante la adopción por mayoría absoluta de la moción de censura')}; el Reglamento del Congreso precisa {c('RCD', 'art177', 'el voto favorable de la mayoría absoluta de los miembros del Congreso')}.",
  "c": f"El Senado no interviene: es {c('CE', 'Artículo 113', 'El Congreso de los Diputados')} quien adopta la moción de censura (art. 113.1), igual que el Gobierno responde solo ante el Congreso (art. 108).",
  "d": f"La mayoría simple es la de la cuestión de confianza ({c('CE', 'Artículo 112', 'la mayoría simple de los Diputados')}, art. 112), no la de la moción de censura."},
  [("mayoría absoluta", "CE", "Artículo 113", "mediante la adopción por mayoría absoluta de la moción de censura"),
   ("Congreso de los Diputados", "CE", "Artículo 113", "El Congreso de los Diputados puede exigir la responsabilidad política del Gobierno")])
EX_P49 = examen("P", 49, {
  "a": f"Las «Órdenes» son la forma de las decisiones de los Ministros y de los acuerdos de las Comisiones Delegadas ({c('LGOB', 'a24', 'Tales acuerdos revestirán la forma de Orden del Ministro competente')}), no del Consejo de Ministros.",
  "b": "La Ley 50/1997 no prevé «Resoluciones del Consejo de Ministros» como forma de sus decisiones (art. 24.1).",
  "c": "No existen «Reglamentos del Consejo de Ministros» como forma: los reglamentos del Consejo se aprueban por Real Decreto acordado en Consejo de Ministros (art. 24.1 c).",
  "d": f"Literal del art. 24.1 d): {c('LGOB', 'a24', 'Acuerdos del Consejo de Ministros, las decisiones de dicho órgano colegiado que no deban adoptar la forma de Real Decreto')}."},
  [("Acuerdos del Consejo de Ministros", "LGOB", "a24", "Acuerdos del Consejo de Ministros, las decisiones de dicho órgano colegiado que no deban adoptar la forma de Real Decreto")])
EX_P101 = examen("P", 101, {
  "a": "Las competencias en materia de régimen de personal no figuran entre los contenidos obligatorios del Real Decreto de creación (art. 6.2 a) a e).",
  "b": f"Cambia dos datos: no son «Subsecretarios de Estado» ni «en todo caso», sino {c('LGOB', 'a6', 'Los miembros del Gobierno y, en su caso, Secretarios de Estado que la integran')}.",
  "c": f"Literal del art. 6.2 e): {c('LGOB', 'a6', 'El régimen interno de funcionamiento y en particular el de convocatorias y suplencias')}.",
  "d": f"Cambia «en su caso» por «en todo caso»: la ley dice {c('LGOB', 'a6', 'Los miembros del Gobierno y, en su caso, Secretarios de Estado que la integran')}."},
  [("régimen interno de funcionamiento", "LGOB", "a6", "El régimen interno de funcionamiento y en particular el de convocatorias y suplencias")])
EX_L8 = examen("L", 8, {
  "a": f"La LO 3/1980 no prevé vicepresidente: integran el Pleno {c('LO3_1980', 'acuarto', 'El Presidente')}, los Consejeros permanentes, natos y electivos y el Secretario general (art. 4.1).",
  "b": f"Cambia el número y la procedencia: los electivos son {c('LO3_1980', 'anoveno', 'en número de diez')}, y el de Fiscal General del Estado no está entre los cargos del art. 9.1 (el Fiscal General es Consejero **nato**: art. 8.2 c).",
  "c": f"Es Consejero nato {c('LO3_1980', 'aoctavo', 'El Gobernador del Banco de España')}; los {c('LO3_1980', 'aseptimo', 'Ex Gobernadores del Banco de España')} son una de las categorías para nombrar Consejeros **permanentes** (art. 7).",
  "d": f"Literal del art. 7: los Consejeros Permanentes, {c('LO3_1980', 'aseptimo', 'en numero igual al de las Secciones del Consejo, son nombrados, sin límite de tiempo, por Real Decreto')}; y forman parte del Pleno (art. 4.1 b)."},
  [("igual al de las Secciones del Consejo", "LO3_1980", "aseptimo", "en numero igual al de las Secciones del Consejo"),
   ("sin límite de tiempo", "LO3_1980", "aseptimo", "son nombrados, sin límite de tiempo, por Real Decreto")])
EX_X16 = examen("X", 16, {
  "a": f"Cambia el número y el Consejero: {c('LO3_1980', 'atrece', 'Las Secciones del Consejo serán ocho como mínimo')} y cada una tiene {c('LO3_1980', 'atrece', 'un Consejero permanente que la preside')} (no un electivo).",
  "b": f"Literal del art. 13.1 y 2: {c('LO3_1980', 'atrece', 'ocho como mínimo')} … {c('LO3_1980', 'atrece', 'un Consejero permanente que la preside')}.",
  "c": "Cambia el número: el mínimo del art. 13.1 es **ocho**, no diez (el número puede ampliarse reglamentariamente, pero el mínimo legal es ocho).",
  "d": "Cambia el número: el mínimo del art. 13.1 es **ocho**, no once."},
  [("Ocho", "LO3_1980", "atrece", "Las Secciones del Consejo serán ocho como mínimo"),
   ("Consejero permanente", "LO3_1980", "atrece", "un Consejero permanente que la preside")])
EX_X17 = examen("X", 17, {
  "a": f"Haber sido {c('LO3_1980', 'anoveno', 'Defensor del Pueblo')} es uno de los cargos para nombrar Consejeros **electivos** (art. 9.1 c), no un Consejero nato.",
  "b": f"Literal del art. 8.2 c): {c('LO3_1980', 'aoctavo', 'Serán Consejeros natos de Estado')} … {c('LO3_1980', 'aoctavo', 'El Fiscal General del Estado')}.",
  "c": f"Haber sido {c('LO3_1980', 'anoveno', 'Presidente del Tribunal de Cuentas')} es un cargo para nombrar Consejeros **electivos** (art. 9.1 f).",
  "d": f"Haber sido {c('LO3_1980', 'anoveno', 'Presidente o Vocal del Consejo General del Poder Judicial')} es un cargo para nombrar Consejeros **electivos** (art. 9.1 d)."},
  [("Fiscal General del Estado", "LO3_1980", "aoctavo", "El Fiscal General del Estado")])
EX_X12 = examen("X", 12, {
  "a": f"Sí es causa: {c('CE', 'Artículo 70', 'A los componentes del Tribunal Constitucional')} (art. 70.1 a).",
  "b": f"Sí es causa: {c('CE', 'Artículo 70', 'A los Magistrados, Jueces y Fiscales en activo')} (art. 70.1 d).",
  "c": f"Sí es causa: {c('CE', 'Artículo 70', 'A los miembros de las Juntas Electorales')} (art. 70.1 f).",
  "d": f"No es causa: el art. 70.1 b) incluye a los altos cargos {c('CE', 'Artículo 70', 'con la excepción de los miembros del Gobierno')}; y el art. 98.3 les permite {c('CE', 'Artículo 98', 'las propias del mandato parlamentario')}."},
  [("miembro del Gobierno", "CE", "Artículo 70", "con la excepción de los miembros del Gobierno")])
EX_X24 = examen("X", 24, {
  "a": f"Al Tribunal de Cuentas le corresponde otro control: {c('CE', 'Artículo 153', 'Por el Tribunal de Cuentas, el económico y presupuestario')} (art. 153 d).",
  "b": f"Al Tribunal Constitucional, {c('CE', 'Artículo 153', 'el relativo a la constitucionalidad de sus disposiciones normativas con fuerza de ley')} (art. 153 a).",
  "c": f"Literal del art. 153 b): {c('CE', 'Artículo 153', 'Por el Gobierno, previo dictamen del Consejo de Estado, el del ejercicio de funciones delegadas')}; y la LO 3/1980 lo atribuye a la Comisión Permanente ({c('LO3_1980', 'aveintidos', 'Control del ejercicio de funciones delegadas por el Estado a las Comunidades Autónomas')}, art. 22.5).",
  "d": "El Senado no figura entre los órganos de control del art. 153."},
  [("previo dictamen del Consejo de Estado", "CE", "Artículo 153", "Por el Gobierno, previo dictamen del Consejo de Estado, el del ejercicio de funciones delegadas")])

T.ap("s24", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **siete** preguntas de este tema (una de ellas, de reserva) y **dos** relacionadas. Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-L 2025, pregunta 4 · Propuesta de candidato a la Presidencia (→ II.1.1)", EX_L4,
  "### GACE-L 2025 extraordinario, pregunta 15 · Moción de censura (→ III.4.1)", EX_X15,
  "### GACE-P 2025, pregunta 49 · Forma de las decisiones del Consejo de Ministros (→ I.6.4)", EX_P49,
  "### GACE-P 2025, pregunta 101 (reserva) · Comisiones Delegadas (→ I.4.3)", EX_P101,
  "### GACE-L 2025, pregunta 8 · Pleno del Consejo de Estado (→ IV.2.4)", EX_L8,
  "### GACE-L 2025 extraordinario, pregunta 16 · Secciones del Consejo de Estado (→ IV.3.3)", EX_X16,
  "### GACE-L 2025 extraordinario, pregunta 17 · Consejeros natos (→ IV.2.5)", EX_X17,
  "### GACE-L 2025 extraordinario, pregunta 12 · Miembros del Gobierno y escaño (relacionada; → II.2.5)", EX_X12,
  "### GACE-L 2025 extraordinario, pregunta 24 · Control de funciones delegadas, previo dictamen del Consejo de Estado (relacionada; → IV.4.2)", EX_X24,
  "### Cómo se pregunta",
  "!> Dos patrones: **quién** hace cada cosa (el Rey propone **a través del** Presidente del Congreso; el Consejo de Ministros adopta **Acuerdos**; el Fiscal General es Consejero **nato**) y **cuánto** (mayoría **absoluta** en la censura; **ocho** Secciones; **diez** electivos). Los distractores cambian el órgano o el número.",
]))

T.ap("s25", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Gobierno | Funciones (97); composición (98.1); Presidente (98.2; Ley 50/1997, art. 2); Consejo de Ministros y Comisiones Delegadas (arts. 5 y 6); forma de las decisiones (art. 24) | Lo que el Consejo de Ministros decide sin Real Decreto: **Acuerdos**; deliberaciones **secretas** |
| II. Designación, cese y responsabilidad penal | Investidura (99); nombramiento de los demás (100); cese y Gobierno en funciones (101; art. 21); responsabilidad criminal (102) | El Rey propone **previa consulta con los representantes de los Grupos políticos** y **a través del Presidente del Congreso**; **2 meses** desde la 1.ª votación |
| III. Relaciones con las Cortes | Responsabilidad solidaria (108); control (109-111); confianza (112); censura (113); efectos (114); disolución (115); estados (116) | Censura: **1/10**, candidato, **5 días**, **mayoría absoluta**; confianza: **mayoría simple** |
| IV. Consejo de Estado | Art. 107; LO 3/1980: dictámenes, Pleno, Comisión Permanente, Consejeros | **8** Secciones mínimo; **10** electivos por **4** años; Fiscal General = **nato** |

?> **Trampas frecuentes:** «el Rey consulta a los **Grupos Parlamentarios** del Congreso y del Senado» (consulta a los **representantes designados por los Grupos políticos** con representación parlamentaria); «la moción de censura se aprueba por mayoría **simple**» (es **absoluta**; la simple es la de la **confianza**); «la cuestión de confianza requiere **acuerdo** del Consejo de Ministros» (basta su **deliberación**); «el Gobierno responde ante **las Cortes Generales**» (ante el **Congreso**); «los Consejeros electivos son **doce**» (son **diez**); «las deliberaciones del Consejo de Ministros son **reservadas**» (son **secretas**; reservadas las de la Comisión General).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
T.q("CE", "Artículo 97", "El Gobierno", "Según el artículo 97 de la Constitución, el Gobierno ejerce:",
    ["La función ejecutiva y la potestad reglamentaria de acuerdo con la Constitución y las leyes.", "La función ejecutiva y la potestad legislativa de acuerdo con la Constitución y las leyes.", "La potestad reglamentaria y la función jurisdiccional en materia administrativa.", "La función ejecutiva, bajo la dirección de las Cortes Generales."],
    "Art. 97 CE: «Ejerce la función ejecutiva y la potestad reglamentaria de acuerdo con la Constitución y las leyes».", "Ejerce la función ejecutiva y la potestad reglamentaria de acuerdo con la Constitución y las leyes")
T.q("CE", "Artículo 98", "El Gobierno", "Según el artículo 98.1 de la Constitución, el Gobierno se compone:",
    ["Del Presidente, de los Vicepresidentes, en su caso, de los Ministros y de los demás miembros que establezca la ley.", "Del Presidente, de los Vicepresidentes, de los Ministros y de los Secretarios de Estado.", "Del Presidente y de los Ministros, exclusivamente.", "Del Presidente, de los Ministros y de los Subsecretarios."],
    "Art. 98.1 CE. Los Vicepresidentes son eventuales («en su caso»); los Secretarios de Estado no son miembros del Gobierno (Ley 50/1997, art. 1.2).", "El Gobierno se compone del Presidente, de los Vicepresidentes, en su caso, de los Ministros y de los demás miembros que establezca la ley")
T.q("CE", "Artículo 98", "Presidente del Gobierno", "Según el artículo 98.2 de la Constitución, el Presidente del Gobierno:",
    ["Dirige la acción del Gobierno y coordina las funciones de los demás miembros del mismo.", "Dirige la acción del Gobierno y responde en exclusiva de la gestión de cada Ministro.", "Coordina la acción del Gobierno, cuya dirección corresponde al Consejo de Ministros.", "Dirige la Administración civil y militar sin intervención de los Ministros."],
    "Art. 98.2 CE: dirige y coordina, «sin perjuicio de la competencia y responsabilidad directa de éstos en su gestión».", "El Presidente dirige la acción del Gobierno y coordina las funciones de los demás miembros del mismo")
T.q("LGOB", "a2", "Presidente del Gobierno", "Según el artículo 2.2 de la Ley 50/1997, del Gobierno, corresponde al Presidente del Gobierno proponer al Rey la convocatoria de un referéndum consultivo:",
    ["Previa autorización del Congreso de los Diputados.", "Previa autorización del Senado.", "Previa autorización de las Cortes Generales por mayoría absoluta de cada Cámara.", "Previo dictamen favorable del Consejo de Estado."],
    "Art. 2.2 e) Ley 50/1997.", "Proponer al Rey la convocatoria de un referéndum consultivo, previa autorización del Congreso de los Diputados")
T.q("LGOB", "a2", "Presidente del Gobierno", "Según el artículo 2.2 j) de la Ley 50/1997, del Gobierno, la creación, modificación y supresión de los Departamentos Ministeriales corresponde:",
    ["Al Presidente del Gobierno, por Real Decreto.", "A las Cortes Generales, por ley.", "Al Consejo de Ministros, mediante Acuerdo.", "Al Ministro de la Presidencia, por Orden Ministerial."],
    "Art. 2.2 j) Ley 50/1997.", "Crear, modificar y suprimir, por Real Decreto, los Departamentos Ministeriales")
T.q("LGOB", "a2", "Presidente del Gobierno", "Según el artículo 2.2 de la Ley 50/1997, el Presidente del Gobierno plantea ante el Congreso de los Diputados la cuestión de confianza:",
    ["Previa deliberación del Consejo de Ministros.", "Previa autorización del Consejo de Ministros por mayoría absoluta.", "Previo dictamen del Consejo de Estado.", "Previa audiencia de la Junta de Portavoces del Congreso."],
    "Art. 2.2 d) Ley 50/1997 y art. 112 CE.", "Plantear ante el Congreso de los Diputados, previa deliberación del Consejo de Ministros, la cuestión de confianza")
T.q("LGOB", "a3", "Composición", "Según el artículo 3.2 de la Ley 50/1997, el Vicepresidente que asuma la titularidad de un Departamento Ministerial:",
    ["Ostentará, además, la condición de Ministro.", "Perderá la condición de Vicepresidente.", "Tendrá rango de Secretario de Estado en ese Departamento.", "Deberá ser autorizado por el Congreso de los Diputados."],
    "Art. 3.2 Ley 50/1997.", "ostentará, además, la condición de Ministro")
T.q("LGOB", "a4", "Composición", "Según el artículo 4.2 de la Ley 50/1997, en caso de que existan Ministros sin cartera, el ámbito de sus competencias se determinará:",
    ["Por Real Decreto.", "Por ley.", "Por Orden del Ministro de la Presidencia.", "Por acuerdo de la Comisión General de Secretarios de Estado y Subsecretarios."],
    "Art. 4.2 Ley 50/1997.", "por Real Decreto se determinará el ámbito de sus competencias")
T.q("LGOB", "a5", "Consejo de Ministros", "Según el artículo 5.1 de la Ley 50/1997, en relación con los estados excepcionales, corresponde al Consejo de Ministros:",
    ["Declarar los estados de alarma y de excepción y proponer al Congreso de los Diputados la declaración del estado de sitio.", "Declarar los estados de alarma, de excepción y de sitio.", "Proponer al Congreso de los Diputados la declaración de los estados de alarma y de excepción.", "Declarar el estado de alarma y proponer al Senado la declaración de los estados de excepción y de sitio."],
    "Art. 5.1 f) Ley 50/1997 (y art. 116 CE).", "Declarar los estados de alarma y de excepción y proponer al Congreso de los Diputados la declaración del estado de sitio")
T.q("LGOB", "a5", "Consejo de Ministros", "Según el artículo 5.1 h) de la Ley 50/1997, el Consejo de Ministros aprueba los reglamentos para el desarrollo y la ejecución de las leyes:",
    ["Previo dictamen del Consejo de Estado.", "Previa autorización de las Cortes Generales.", "Previo informe vinculante de la Comisión General de Secretarios de Estado y Subsecretarios.", "Previa convalidación del Congreso de los Diputados."],
    "Art. 5.1 h) Ley 50/1997.", "Aprobar los reglamentos para el desarrollo y la ejecución de las leyes, previo dictamen del Consejo de Estado")
T.q("LGOB", "a5", "Consejo de Ministros", "Según el artículo 5.3 de la Ley 50/1997, las deliberaciones del Consejo de Ministros serán:",
    ["Secretas.", "Reservadas.", "Públicas, salvo acuerdo en contrario.", "Públicas en lo que se refiera a la aprobación de proyectos de ley."],
    "Art. 5.3 Ley 50/1997. «Reservadas» son las de la Comisión General de Secretarios de Estado y Subsecretarios (art. 8.4).", "Las deliberaciones del Consejo de Ministros serán secretas")
T.q("LGOB", "a6", "Comisiones Delegadas", "Según el artículo 6.1 de la Ley 50/1997, la creación de las Comisiones Delegadas del Gobierno será acordada:",
    ["Por el Consejo de Ministros mediante Real Decreto, a propuesta del Presidente del Gobierno.", "Por el Presidente del Gobierno mediante Real Decreto, sin intervención del Consejo de Ministros.", "Por las Cortes Generales mediante ley.", "Por el Consejo de Ministros mediante Acuerdo, a propuesta del Ministro de la Presidencia."],
    "Art. 6.1 Ley 50/1997.", "será acordada por el Consejo de Ministros mediante Real Decreto, a propuesta del Presidente del Gobierno")
T.q("LGOB", "a8", "Órganos de colaboración", "Según el artículo 8.2 de la Ley 50/1997, la Presidencia de la Comisión General de Secretarios de Estado y Subsecretarios corresponde:",
    ["A un Vicepresidente del Gobierno o, en su defecto, al Ministro de la Presidencia.", "Al Subsecretario de la Presidencia.", "Al Presidente del Gobierno.", "Al Secretario de Estado de más antigüedad."],
    "Art. 8.2 Ley 50/1997. La Secretaría de la Comisión la ejerce el Subsecretario de la Presidencia (8.3).", "corresponde a un Vicepresidente del Gobierno o, en su defecto, al Ministro de la Presidencia")
T.q("LGOB", "a8", "Órganos de colaboración", "Según el artículo 8.4 de la Ley 50/1997, la Comisión General de Secretarios de Estado y Subsecretarios:",
    ["En ningún caso podrá adoptar decisiones o acuerdos por delegación del Gobierno.", "Podrá adoptar acuerdos por delegación del Consejo de Ministros.", "Tiene deliberaciones públicas.", "Resuelve los asuntos que afecten a más de un Ministerio sin necesidad de elevarlos al Consejo de Ministros."],
    "Art. 8.4 Ley 50/1997. Resolver asuntos que afectan a varios Ministerios es propio de las Comisiones Delegadas (art. 6.4 c).", "En ningún caso la Comisión podrá adoptar decisiones o acuerdos por delegación del Gobierno")
T.q("LGOB", "a18", "Consejo de Ministros", "Según el artículo 18.1 de la Ley 50/1997, en las reuniones del Consejo de Ministros actúa como Secretario:",
    ["El Ministro de la Presidencia.", "El Subsecretario de la Presidencia.", "El Director del Secretariado del Gobierno.", "El Vicepresidente primero del Gobierno."],
    "Art. 18.1 Ley 50/1997.", "actuando como Secretario el Ministro de la Presidencia")
T.q("LGOB", "a20", "Funcionamiento", "Según el artículo 20.3 de la Ley 50/1997, NO son en ningún caso delegables:",
    ["Las competencias atribuidas directamente por la Constitución.", "Las competencias propias del Presidente del Gobierno en favor de los Vicepresidentes.", "Las competencias de los Ministros en favor de los Secretarios de Estado.", "Las funciones administrativas del Consejo de Ministros en las Comisiones Delegadas."],
    "Art. 20.3 a) Ley 50/1997. Las otras tres son delegaciones permitidas por el art. 20.1 y 2.", "Las atribuidas directamente por la Constitución")
T.q("LGOB", "a24", "Funcionamiento", "Según el artículo 24.2 de la Ley 50/1997, en la jerarquía de los reglamentos, las disposiciones aprobadas por Orden Ministerial se sitúan:",
    ["Por debajo de las aprobadas por Real Decreto del Presidente del Gobierno o acordado en el Consejo de Ministros.", "Al mismo nivel que las aprobadas por Real Decreto acordado en Consejo de Ministros.", "Por encima de las aprobadas por Real Decreto del Presidente del Gobierno.", "Al mismo nivel que los Reales Decretos-leyes."],
    "Art. 24.2 Ley 50/1997: 1.º Real Decreto del Presidente o acordado en Consejo de Ministros; 2.º Orden Ministerial.", "2.º Disposiciones aprobadas por Orden Ministerial")
T.q("CE", "Artículo 99", "Investidura", "Según el artículo 99.3 de la Constitución, si en la primera votación de investidura el candidato no obtiene la mayoría absoluta, se someterá la misma propuesta a nueva votación:",
    ["Cuarenta y ocho horas después de la anterior, y la confianza se entenderá otorgada si obtuviere la mayoría simple.", "Veinticuatro horas después de la anterior, y la confianza se entenderá otorgada si obtuviere la mayoría simple.", "Cuarenta y ocho horas después de la anterior, y la confianza se entenderá otorgada si obtuviere la mayoría absoluta.", "Quince días después de la anterior, con mayoría de tres quintos."],
    "Art. 99.3 CE.", "se someterá la misma propuesta a nueva votación cuarenta y ocho horas después de la anterior, y la confianza se entenderá otorgada si obtuviere la mayoría simple")
T.q("CE", "Artículo 99", "Investidura", "Según el artículo 99.5 de la Constitución, si ningún candidato hubiere obtenido la confianza del Congreso, el Rey disolverá ambas Cámaras transcurrido el plazo de:",
    ["Dos meses, a partir de la primera votación de investidura.", "Dos meses, a partir de la celebración de las elecciones.", "Tres meses, a partir de la primera votación de investidura.", "Un mes, a partir de la constitución del Congreso."],
    "Art. 99.5 CE.", "Si transcurrido el plazo de dos meses, a partir de la primera votación de investidura")
T.q("CE", "Artículo 99", "Investidura", "Según el artículo 99.5 de la Constitución, la disolución de ambas Cámaras por no haberse otorgado la confianza a ningún candidato se hace con el refrendo:",
    ["Del Presidente del Congreso.", "Del Presidente del Gobierno en funciones.", "Del Presidente del Senado.", "Del Ministro de la Presidencia."],
    "Art. 99.5 CE.", "con el refrendo del Presidente del Congreso")
T.q("CE", "Artículo 100", "Nombramiento", "Según el artículo 100 de la Constitución, los demás miembros del Gobierno serán nombrados y separados:",
    ["Por el Rey, a propuesta de su Presidente.", "Por el Presidente del Gobierno, previa comunicación al Rey.", "Por el Rey, previa votación de confianza del Congreso.", "Por el Rey, a propuesta del Presidente del Congreso."],
    "Art. 100 CE.", "Los demás miembros del Gobierno serán nombrados y separados por el Rey, a propuesta de su Presidente")
T.q("LGOB", "a12", "Nombramiento", "Según el artículo 12.2 bis de la Ley 50/1997, en el nombramiento de las personas titulares de las Vicepresidencias y los Ministerios, cada uno de los sexos debe suponer en su conjunto como mínimo:",
    ["El cuarenta por ciento.", "El cincuenta por ciento.", "El treinta por ciento.", "El treinta y tres por ciento."],
    "Art. 12.2 bis Ley 50/1997.", "como mínimo el cuarenta por ciento en su conjunto")
T.q("LGOB", "a13", "Nombramiento", "Según el artículo 13.1 de la Ley 50/1997, en los casos de vacante, ausencia o enfermedad, las funciones del Presidente del Gobierno serán asumidas:",
    ["Por los Vicepresidentes, de acuerdo con el correspondiente orden de prelación, y, en defecto de ellos, por los Ministros, según el orden de precedencia de los Departamentos.", "Por el Ministro de la Presidencia en todo caso.", "Por el Presidente del Congreso de los Diputados.", "Por el Ministro de mayor edad."],
    "Art. 13.1 Ley 50/1997.", "las funciones del Presidente del Gobierno serán asumidas por los Vicepresidentes, de acuerdo con el correspondiente orden de prelación, y, en defecto de ellos, por los Ministros, según el orden de precedencia de los Departamentos")
T.q("CE", "Artículo 101", "Cese", "Según el artículo 101.1 de la Constitución, el Gobierno cesa, entre otros supuestos:",
    ["Por dimisión o fallecimiento de su Presidente.", "Por la dimisión de la mitad de sus Ministros.", "Por la disolución del Senado.", "Por la reprobación de uno de sus Ministros por el Congreso."],
    "Art. 101.1 CE: elecciones generales, pérdida de la confianza parlamentaria y dimisión o fallecimiento del Presidente.", "o por dimisión o fallecimiento de su Presidente")
T.q("LGOB", "a21", "Cese", "Según el artículo 21.4 de la Ley 50/1997, el Presidente del Gobierno en funciones NO podrá:",
    ["Plantear la cuestión de confianza.", "Representar al Gobierno.", "Convocar y presidir las reuniones del Consejo de Ministros.", "Impartir instrucciones a los demás miembros del Gobierno."],
    "Art. 21.4 Ley 50/1997: tampoco puede proponer la disolución ni la convocatoria de un referéndum consultivo.", "Plantear la cuestión de confianza")
T.q("LGOB", "a21", "Cese", "Según el artículo 21.5 de la Ley 50/1997, el Gobierno en funciones NO podrá:",
    ["Aprobar el Proyecto de Ley de Presupuestos Generales del Estado.", "Despachar los asuntos públicos ordinarios.", "Adoptar medidas por razones de urgencia debidamente acreditadas.", "Facilitar el traspaso de poderes al nuevo Gobierno."],
    "Art. 21.5 a) Ley 50/1997 (tampoco presentar proyectos de ley).", "Aprobar el Proyecto de Ley de Presupuestos Generales del Estado")
T.q("CE", "Artículo 102", "Responsabilidad", "Según el artículo 102.1 de la Constitución, la responsabilidad criminal del Presidente y los demás miembros del Gobierno será exigible ante:",
    ["La Sala de lo Penal del Tribunal Supremo.", "El Tribunal Constitucional.", "La Sala de lo Penal de la Audiencia Nacional.", "El Senado, constituido en tribunal."],
    "Art. 102.1 CE.", "será exigible, en su caso, ante la Sala de lo Penal del Tribunal Supremo")
T.q("CE", "Artículo 102", "Responsabilidad", "Según el artículo 102.2 de la Constitución, la acusación contra miembros del Gobierno por traición o por delito contra la seguridad del Estado en el ejercicio de sus funciones solo podrá ser planteada:",
    ["Por iniciativa de la cuarta parte de los miembros del Congreso, y con la aprobación de la mayoría absoluta del mismo.", "Por iniciativa de la décima parte de los miembros del Congreso, y con la aprobación de la mayoría absoluta del mismo.", "Por iniciativa de la cuarta parte de los miembros del Senado, y con la aprobación de la mayoría absoluta del mismo.", "Por iniciativa del Fiscal General del Estado, con autorización del Congreso por mayoría simple."],
    "Art. 102.2 CE. Además, la prerrogativa real de gracia no se aplica (102.3).", "sólo podrá ser planteada por iniciativa de la cuarta parte de los miembros del Congreso, y con la aprobación de la mayoría absoluta del mismo")
T.q("CE", "Artículo 108", "Relaciones con las Cortes", "Según el artículo 108 de la Constitución, el Gobierno responde solidariamente en su gestión política ante:",
    ["El Congreso de los Diputados.", "Las Cortes Generales.", "El Senado.", "El Rey."],
    "Art. 108 CE.", "El Gobierno responde solidariamente en su gestión política ante el Congreso de los Diputados")
T.q("CE", "Artículo 111", "Relaciones con las Cortes", "Según el artículo 111.1 de la Constitución, para el debate de las interpelaciones y preguntas los Reglamentos establecerán:",
    ["Un tiempo mínimo semanal.", "Un tiempo máximo semanal.", "Un tiempo mínimo mensual.", "Una sesión plenaria quincenal."],
    "Art. 111.1 CE.", "Para esta clase de debate los Reglamentos establecerán un tiempo mínimo semanal")
T.q("RCD", "art187", "Relaciones con las Cortes", "Según el artículo 187 del Reglamento del Congreso, en defecto de indicación, se entenderá que quien formula una pregunta solicita:",
    ["Respuesta por escrito.", "Respuesta oral ante el Pleno.", "Respuesta oral ante la Comisión correspondiente.", "Respuesta oral ante la Diputación Permanente."],
    "Art. 187 RCD: si se pide oral sin especificar, en la Comisión correspondiente.", "En defecto de indicación se entenderá que quien formula la pregunta solicita respuesta por escrito")
T.q("CE", "Artículo 112", "Cuestión de confianza", "Según el artículo 112 de la Constitución, la confianza se entenderá otorgada cuando vote a favor de la misma:",
    ["La mayoría simple de los Diputados.", "La mayoría absoluta de los Diputados.", "La mayoría de tres quintos de los Diputados.", "La mayoría simple de los miembros de ambas Cámaras."],
    "Art. 112 CE.", "La confianza se entenderá otorgada cuando vote a favor de la misma la mayoría simple de los Diputados")
T.q("RCD", "art174", "Cuestión de confianza", "Según el artículo 174.4 del Reglamento del Congreso, la cuestión de confianza no podrá ser votada hasta que transcurran:",
    ["Veinticuatro horas desde su presentación.", "Cinco días desde su presentación.", "Cuarenta y ocho horas desde su presentación.", "Dos días desde su admisión a trámite por la Mesa."],
    "Art. 174.4 RCD. Los cinco días son de la moción de censura (art. 113.3 CE).", "La cuestión de confianza no podrá ser votada hasta que transcurran veinticuatro horas desde su presentación")
T.q("CE", "Artículo 113", "Moción de censura", "Según el artículo 113.2 de la Constitución, la moción de censura deberá ser propuesta al menos por:",
    ["La décima parte de los Diputados, y habrá de incluir un candidato a la Presidencia del Gobierno.", "La quinta parte de los Diputados, y habrá de incluir un candidato a la Presidencia del Gobierno.", "La décima parte de los Diputados, sin necesidad de incluir candidato.", "Dos Grupos Parlamentarios, con un programa de gobierno alternativo."],
    "Art. 113.2 CE.", "La moción de censura deberá ser propuesta al menos por la décima parte de los Diputados, y habrá de incluir un candidato a la Presidencia del Gobierno")
T.q("CE", "Artículo 113", "Moción de censura", "Según el artículo 113.3 de la Constitución, la moción de censura no podrá ser votada hasta que transcurran:",
    ["Cinco días desde su presentación.", "Dos días desde su presentación.", "Veinticuatro horas desde su presentación.", "Diez días desde su presentación."],
    "Art. 113.3 CE: en los dos primeros días pueden presentarse mociones alternativas.", "no podrá ser votada hasta que transcurran cinco días desde su presentación")
T.q("CE", "Artículo 113", "Moción de censura", "Según el artículo 113.4 de la Constitución, si la moción de censura no fuere aprobada por el Congreso, sus signatarios:",
    ["No podrán presentar otra durante el mismo período de sesiones.", "No podrán presentar otra durante el plazo de un año.", "No podrán presentar otra durante la misma legislatura.", "Podrán presentar otra transcurridos cinco días."],
    "Art. 113.4 CE.", "sus signatarios no podrán presentar otra durante el mismo período de sesiones")
T.q("CE", "Artículo 114", "Moción de censura", "Según el artículo 114.2 de la Constitución, si el Congreso adopta una moción de censura:",
    ["El Gobierno presentará su dimisión al Rey y el candidato incluido en aquélla se entenderá investido de la confianza de la Cámara.", "El Rey propondrá un nuevo candidato tras consultar a los grupos políticos.", "Se disolverán automáticamente las Cortes Generales.", "El candidato incluido en la moción deberá someterse a una votación de investidura en el plazo de cuarenta y ocho horas."],
    "Art. 114.2 CE: el Rey le nombrará Presidente del Gobierno.", "el candidato incluido en aquélla se entenderá investido de la confianza de la Cámara")
T.q("CE", "Artículo 115", "Disolución", "Según el artículo 115 de la Constitución, la propuesta de disolución de las Cortes:",
    ["No podrá presentarse cuando esté en trámite una moción de censura.", "Requiere la autorización previa del Congreso de los Diputados.", "Corresponde al Consejo de Ministros, bajo la responsabilidad solidaria del Gobierno.", "Puede presentarse en cualquier momento, aunque no haya transcurrido un año desde la anterior disolución."],
    "Art. 115 CE: la propone el Presidente, previa deliberación del Consejo de Ministros y bajo su exclusiva responsabilidad; no antes de un año desde la anterior, salvo el art. 99.5.", "La propuesta de disolución no podrá presentarse cuando esté en trámite una moción de censura")
T.q("CE", "Artículo 116", "Estados excepcionales", "Según el artículo 116.2 de la Constitución, el estado de alarma será declarado por el Gobierno por un plazo máximo de:",
    ["Quince días, dando cuenta al Congreso de los Diputados.", "Treinta días, previa autorización del Congreso de los Diputados.", "Quince días, previa autorización del Congreso de los Diputados.", "Un mes, dando cuenta al Senado."],
    "Art. 116.2 CE: la prórroga requiere autorización del Congreso.", "por un plazo máximo de quince días, dando cuenta al Congreso de los Diputados")
T.q("CE", "Artículo 107", "Consejo de Estado", "Según el artículo 107 de la Constitución, el Consejo de Estado es:",
    ["El supremo órgano consultivo del Gobierno.", "El supremo órgano consultivo de las Cortes Generales.", "El órgano de gobierno de la Administración consultiva.", "El supremo órgano de control externo del Gobierno."],
    "Art. 107 CE: una ley orgánica regulará su composición y competencia.", "El Consejo de Estado es el supremo órgano consultivo del Gobierno")
T.q("LO3_1980", "asegundo", "Consejo de Estado", "Según el artículo 2.2 de la Ley Orgánica 3/1980, del Consejo de Estado, los dictámenes del Consejo:",
    ["No serán vinculantes, salvo que la ley disponga lo contrario.", "Serán vinculantes en todo caso cuando la consulta sea preceptiva.", "Serán vinculantes cuando los emita el Pleno.", "No serán vinculantes en ningún caso."],
    "Art. 2.2 LO 3/1980.", "Los dictámenes del Consejo no serán vinculantes, salvo que la ley disponga lo contrario")
T.q("LO3_1980", "asegundo", "Consejo de Estado", "Según el artículo 2.2 de la Ley Orgánica 3/1980, cuando una disposición sobre un asunto informado por el Consejo de Estado se aparte de su dictamen, se usará la fórmula:",
    ["«Oído el Consejo de Estado».", "«De acuerdo con el Consejo de Estado».", "«Visto el dictamen del Consejo de Estado».", "«Con el informe desfavorable del Consejo de Estado»."],
    "Art. 2.2 LO 3/1980: si se acuerda conforme, «de acuerdo con el Consejo de Estado».", "en el segundo, la de ''oído el Consejo de Estado")
T.q("LO3_1980", "asexto", "Consejo de Estado", "Según el artículo 6 de la Ley Orgánica 3/1980, el Presidente del Consejo de Estado será nombrado:",
    ["Libremente por Real Decreto acordado en Consejo de Ministros y refrendado por su Presidente, entre juristas de reconocido prestigio y experiencia en asuntos de Estado.", "Por el Rey, a propuesta del Congreso de los Diputados por mayoría de tres quintos.", "Por el Pleno del Consejo de Estado, entre sus Consejeros permanentes.", "Por Real Decreto del Presidente del Gobierno, entre los Letrados Mayores del Consejo."],
    "Art. 6 LO 3/1980.", "será nombrado libremente por Real Decreto acordado en Consejo de Ministros y refrendado por su Presidente entre juristas de reconocido prestigio y experiencia en asuntos de Estado")
T.q("LO3_1980", "aoctavo", "Consejo de Estado", "Según el artículo 8.1 de la Ley Orgánica 3/1980, quienes hayan desempeñado el cargo de Presidente del Gobierno adquirirán la condición de:",
    ["Consejeros natos de Estado con carácter vitalicio.", "Consejeros permanentes de Estado sin límite de tiempo.", "Consejeros electivos por un período de ocho años.", "Consejeros natos de Estado durante cuatro años."],
    "Art. 8.1 LO 3/1980: pueden manifestar en cualquier momento su voluntad de incorporarse.", "adquirirán la condición de Consejeros natos de Estado con carácter vitalicio")
T.q("LO3_1980", "anoveno", "Consejo de Estado", "Según el artículo 9.1 de la Ley Orgánica 3/1980, los Consejeros electivos de Estado son:",
    ["Diez, nombrados por Real Decreto por un período de cuatro años.", "Doce, nombrados por Real Decreto por un período de cuatro años.", "Diez, nombrados por Real Decreto sin límite de tiempo.", "Diez, elegidos por las Cortes Generales por un período de cinco años."],
    "Art. 9.1 LO 3/1980 (dos de ellos, ex Presidentes autonómicos, con mandato de ocho años: art. 9.2).", "Los Consejeros electivos de Estado, en número de diez, serán nombrados por Real Decreto, por un período de cuatro años")
T.q("LO3_1980", "aveintiuno", "Consejo de Estado", "Según el artículo 21 de la Ley Orgánica 3/1980, deberá ser consultado el Consejo de Estado en Pleno en el caso de:",
    ["Proyectos de Decretos legislativos.", "Reglamentos que se dicten en ejecución de las leyes.", "Recursos administrativos de revisión.", "Concesión de créditos extraordinarios o suplementos de crédito."],
    "Art. 21.3 LO 3/1980. Las otras tres son competencia de la Comisión Permanente (art. 22).", "Proyectos de Decretos legislativos")
T.q("LO3_1980", "adiecinueve", "Consejo de Estado", "Según el artículo 19 de la Ley Orgánica 3/1980, cuando en la orden de remisión se haga constar la urgencia del dictamen, el plazo máximo para su despacho será de:",
    ["Quince días, salvo que el Gobierno o su Presidente fijen otro inferior.", "Diez días, salvo que el Gobierno fije otro superior.", "Un mes, en todo caso.", "Cinco días, si debe dictaminar la Comisión Permanente."],
    "Art. 19.1 LO 3/1980; si el plazo es inferior a diez días, despacha la Comisión Permanente (19.2).", "el plazo máximo para su despacho será de quince días, salvo que el Gobierno o su Presidente fijen otro inferior")

T.real("L", 4, "Investidura"); T.real("X", 15, "Moción de censura"); T.real("P", 49, "Funcionamiento"); T.real("P", 101, "Comisiones Delegadas")
T.real("L", 8, "Consejo de Estado"); T.real("X", 16, "Consejo de Estado"); T.real("X", 17, "Consejo de Estado")

# Flashcards
for q_, a_, cat in [
  ("¿Qué dirige y qué ejerce el Gobierno? (art. 97)", "Dirige la política interior y exterior, la Administración civil y militar y la defensa del Estado; ejerce la función ejecutiva y la potestad reglamentaria.", "El Gobierno"),
  ("Composición del Gobierno (art. 98.1; Ley 50/1997, art. 1.2)", "Presidente, Vicepresidente o Vicepresidentes (en su caso) y Ministros (la CE añade «los demás miembros que establezca la ley»).", "Composición"),
  ("¿Quién crea, modifica y suprime los Ministerios?", "El Presidente del Gobierno, por Real Decreto (Ley 50/1997, art. 2.2 j).", "Presidente del Gobierno"),
  ("¿Quién crea las Comisiones Delegadas del Gobierno?", "El Consejo de Ministros, mediante Real Decreto, a propuesta del Presidente (Ley 50/1997, art. 6.1).", "Comisiones Delegadas"),
  ("Forma de las decisiones del Consejo de Ministros que no deban ser Real Decreto", "Acuerdos del Consejo de Ministros (Ley 50/1997, art. 24.1 d).", "Funcionamiento"),
  ("Secretario del Consejo de Ministros", "El Ministro de la Presidencia (Ley 50/1997, art. 18.1).", "Consejo de Ministros"),
  ("¿Secretas o reservadas?", "Secretas: Consejo de Ministros y Comisiones Delegadas. Reservadas: Comisión General de Secretarios de Estado y Subsecretarios.", "Consejo de Ministros"),
  ("¿A quién consulta el Rey antes de proponer candidato a la Presidencia? (art. 99.1)", "A los representantes designados por los Grupos políticos con representación parlamentaria; propone a través del Presidente del Congreso.", "Investidura"),
  ("Mayorías de la investidura (art. 99.3)", "Mayoría absoluta en la primera votación; mayoría simple en la segunda, 48 horas después.", "Investidura"),
  ("¿Cuándo se disuelven las Cámaras si nadie obtiene la investidura? (art. 99.5)", "Transcurridos dos meses desde la primera votación de investidura; refrenda el Presidente del Congreso.", "Investidura"),
  ("Causas de cese del Gobierno (art. 101.1)", "Elecciones generales, pérdida de la confianza parlamentaria y dimisión o fallecimiento de su Presidente.", "Cese"),
  ("¿Qué no puede hacer el Presidente en funciones? (Ley 50/1997, art. 21.4)", "Proponer la disolución, plantear la cuestión de confianza ni proponer un referéndum consultivo.", "Cese"),
  ("Responsabilidad criminal del Gobierno (art. 102)", "Ante la Sala de lo Penal del Tribunal Supremo; traición o delitos contra la seguridad del Estado: iniciativa de 1/4 del Congreso y mayoría absoluta; sin indulto.", "Responsabilidad"),
  ("¿Ante quién responde políticamente el Gobierno? (art. 108)", "Ante el Congreso de los Diputados, solidariamente.", "Relaciones con las Cortes"),
  ("Cuestión de confianza (art. 112)", "La plantea el Presidente, previa deliberación del Consejo de Ministros, sobre su programa o una declaración de política general; mayoría simple.", "Cuestión de confianza"),
  ("Moción de censura (art. 113)", "1/10 de los Diputados, con candidato; no se vota antes de 5 días (alternativas en los 2 primeros); mayoría absoluta.", "Moción de censura"),
  ("Límites a la disolución (art. 115)", "No con una moción de censura en trámite; no antes de un año desde la anterior, salvo el art. 99.5.", "Disolución"),
  ("Naturaleza del Consejo de Estado (art. 107)", "Supremo órgano consultivo del Gobierno; composición y competencia por ley orgánica (LO 3/1980).", "Consejo de Estado"),
  ("Clases de Consejeros de Estado", "Permanentes (sin límite de tiempo), natos (por cargo; ex Presidentes del Gobierno, vitalicios) y electivos (diez, cuatro años).", "Consejo de Estado"),
  ("Secciones del Consejo de Estado (LO 3/1980, art. 13)", "Ocho como mínimo, cada una presidida por un Consejero permanente.", "Consejo de Estado"),
  ("¿Pleno o Comisión Permanente? (LO 3/1980, arts. 21 y 22)", "Pleno: anteproyectos de reforma constitucional y proyectos de decretos legislativos. Comisión Permanente: reglamentos ejecutivos y cláusula residual.", "Consejo de Estado"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Gobierno", "Órgano que dirige la política interior y exterior, la Administración civil y militar y la defensa del Estado, y ejerce la función ejecutiva y la potestad reglamentaria (art. 97 CE).", "s1", "El Gobierno")
T.glos("Ministro sin cartera", "Ministro no titular de un Departamento, con la responsabilidad de determinadas funciones gubernamentales; su ámbito se fija por Real Decreto (Ley 50/1997, art. 4.2).", "s2", "Composición")
T.glos("Consejo de Ministros", "Órgano colegiado del Gobierno en que se reúnen sus miembros; sus deliberaciones son secretas (Ley 50/1997, arts. 1.3 y 5).", "s4", "Consejo de Ministros")
T.glos("Comisión Delegada del Gobierno", "Órgano colegiado del Gobierno, creado por Real Decreto del Consejo de Ministros a propuesta del Presidente, para asuntos que afectan a varios Ministerios (Ley 50/1997, art. 6).", "s4", "Comisiones Delegadas")
T.glos("Comisión General de Secretarios de Estado y Subsecretarios", "Órgano de colaboración que examina los asuntos que van al Consejo de Ministros; deliberaciones reservadas; nunca decide por delegación del Gobierno (Ley 50/1997, art. 8).", "s5", "Órganos de colaboración")
T.glos("Investidura", "Otorgamiento por el Congreso de su confianza al candidato propuesto por el Rey: mayoría absoluta o, 48 horas después, simple (art. 99 CE).", "s7", "Investidura")
T.glos("Gobierno en funciones", "Gobierno cesante que continúa hasta la toma de posesión del nuevo, limitado al despacho ordinario de los asuntos públicos (art. 101.2 CE; Ley 50/1997, art. 21).", "s9", "Cese")
T.glos("Responsabilidad política solidaria", "Responsabilidad del Gobierno en su gestión política ante el Congreso de los Diputados (art. 108 CE).", "s11", "Relaciones con las Cortes")
T.glos("Interpelación", "Instrumento de control sobre los motivos o propósitos de la conducta del Ejecutivo en cuestiones de política general; puede dar lugar a una moción (art. 111 CE; RCD, arts. 180 a 184).", "s12", "Relaciones con las Cortes")
T.glos("Cuestión de confianza", "Petición del Presidente al Congreso, previa deliberación del Consejo de Ministros, de confianza sobre su programa o una declaración de política general; se otorga por mayoría simple (art. 112 CE).", "s13", "Cuestión de confianza")
T.glos("Moción de censura", "Instrumento por el que el Congreso exige la responsabilidad política del Gobierno; propuesta por 1/10 de los Diputados con candidato y aprobada por mayoría absoluta (art. 113 CE).", "s14", "Moción de censura")
T.glos("Consejo de Estado", "Supremo órgano consultivo del Gobierno, regulado por la LO 3/1980 (art. 107 CE).", "s19", "Consejo de Estado")
T.glos("Dictamen preceptivo", "Dictamen del Consejo de Estado que debe pedirse porque una ley lo establece; salvo disposición en contrario, no es vinculante (LO 3/1980, art. 2.2).", "s19", "Consejo de Estado")
T.glos("Consejero nato", "Consejero de Estado por razón de su cargo (p. ej., el Fiscal General del Estado) o, con carácter vitalicio, por haber sido Presidente del Gobierno (LO 3/1980, art. 8).", "s20", "Consejo de Estado")

# Cronología (fechas de los metadatos del BOE)
T.hito("1978", "Constitución Española (27-12-1978; BOE de 29-12-1978)", "Títulos IV y V: el Gobierno, sus relaciones con las Cortes y el Consejo de Estado (art. 107)", "normativo", "s1")
T.hito("1980", "Ley Orgánica 3/1980, de 22 de abril, del Consejo de Estado (BOE de 25-4-1980)", "Desarrolla el art. 107 CE: composición y competencia del Consejo de Estado", "normativo", "s19")
T.hito("1982", "Reglamento del Congreso de los Diputados (publicado por Resolución de 24-2-1982; BOE de 5-3-1982)", "Arts. 170 a 188: investidura, cuestión de confianza, moción de censura, interpelaciones y preguntas", "normativo", "s7")
T.hito("1997", "Ley 50/1997, de 27 de noviembre, del Gobierno (BOE de 28-11-1997)", "Composición, organización, estatuto y funcionamiento del Gobierno", "normativo", "s2")
T.hito("2004", "Ley Orgánica 3/2004, de 28 de diciembre, que modifica la LO 3/1980 (BOE de 29-12-2004)", "Nueva redacción, entre otros, de los arts. 2, 5, 7, 8, 9 y 13 de la LO 3/1980", "normativo", "s20")
T.hito("2024", "Ley Orgánica 2/2024, de 1 de agosto, de representación paritaria y presencia equilibrada de mujeres y hombres (BOE de 2-8-2024)", "Modifica, entre otros, el art. 12 de la Ley 50/1997 y los arts. 7 y 9 de la LO 3/1980", "normativo", "s8")

T.publicar()
