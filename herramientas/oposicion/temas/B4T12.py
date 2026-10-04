# -*- coding: utf-8 -*-
"""Tema IV.12 (B4T12): Los derechos de los ciudadanos en el procedimiento administrativo.
Las garantías en el desarrollo del procedimiento. La revisión de los actos en vía
administrativa: revisión de oficio y recursos administrativos.
Método del I.2: mapa → bloques (I a V) con guía; cada artículo, texto literal del
BOE + ficha de casillas fijas; cierre 1 (preguntas oficiales) y cierre 2 (repaso)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

T = Tema("B4T12",
  "Cinco preguntas: I. Quién actúa ante la Administración: capacidad, interesados y representación (arts. 3, 4, 5, 7, 8 y 11 Ley 39/2015) · II. Qué derechos tienen los ciudadanos (arts. 13, 14 y 53.1) · III. Qué garantías rodean el procedimiento: el presunto responsable (art. 53.2) y la imparcialidad (abstención y recusación, arts. 23 y 24 Ley 40/2015) · IV. Cómo revisa la Administración sus actos: revisión de oficio (arts. 106 a 111 y Ley 7/1985, art. 22.2 k) · V. Cómo recurre el interesado: alzada, reposición y revisión (arts. 112 a 126). Cada artículo: texto literal del BOE y ficha.",
  ["Interesado", "Art. 4", "Representación", "Derechos de las personas", "Art. 13", "Art. 14", "Derechos del interesado", "Art. 53", "Abstención", "Recusación", "Arts. 23-24 Ley 40/2015", "Revisión de oficio", "Art. 106", "Lesividad", "Art. 107", "Revocación", "Rectificación de errores", "Recursos administrativos", "Art. 112", "Fin de la vía administrativa", "Art. 114", "Recurso de alzada", "Recurso de reposición", "Recurso extraordinario de revisión"])

ESQ = "*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*"

# =============================================================================
T.ap("s0", "Mapa del tema: cinco preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque IV, tema 12):
> Los derechos de los ciudadanos en el procedimiento administrativo. Las garantías en el desarrollo del procedimiento. La revisión de los actos en vía administrativa: revisión de oficio y recursos administrativos.

### El hilo conductor

El epígrafe se lee como **cinco preguntas encadenadas**. Casi todo está en la **Ley 39/2015**: su Título I («De los interesados en el procedimiento»), el art. 13, el capítulo «Garantías del procedimiento» del Título IV (art. 53) y el Título V («De la revisión de los actos en vía administrativa», arts. 106 a 126). Cada pregunta es un bloque de los apuntes:

| Bloque | Pregunta | Ley 39/2015 | Otras normas |
|---|---|---|---|
| **I** | ¿Quién actúa ante la Administración? (capacidad, interesados, representación) | Arts. 3, 4, 5, 7, 8 y 11 | — |
| **II** | ¿Qué derechos tienen los ciudadanos? | Arts. 13, 14 y 53.1 | — |
| **III** | ¿Qué garantías rodean el desarrollo del procedimiento? | Art. 53.2 | Ley 40/2015, arts. 23 y 24 (abstención y recusación) |
| **IV** | ¿Cómo revisa la Administración sus propios actos? (revisión de oficio) | Arts. 106 a 111 | Ley 7/1985, art. 22.2 k) |
| **V** | ¿Cómo recurre el interesado en vía administrativa? (recursos) | Arts. 112 a 126 | — |

!> **La idea que une los cinco bloques:** la ley dice primero **quién** puede actuar y quién es **interesado** (I). A todas las personas les reconoce unos **derechos** en sus relaciones con la Administración y, a los interesados, otros más dentro del procedimiento (II). El procedimiento se rodea de **garantías**: las del presunto responsable en el sancionador y la **imparcialidad** de quien tramita y resuelve (III). Si el acto ya dictado es inválido, la propia Administración puede **revisarlo de oficio** (IV), y el interesado puede **recurrirlo** en vía administrativa (V).

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (derechos: Titulares · Contenido · Límites · Protección · ⚠ Ojo en el examen; instituciones y procedimientos: Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- Fronteras: los vicios de nulidad y anulabilidad (arts. 47 y 48) son del tema IV.4; el procedimiento común, el silencio y los plazos, del tema IV.11; la responsabilidad patrimonial, del tema IV.10; el recurso contencioso-administrativo, del tema IV.13.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Quién actúa ante la Administración? Capacidad, interesados y representación (arts. 3, 4, 5, 7, 8 y 11)", donde(
  "Primera pregunta del tema. Antes de hablar de derechos y garantías hay que saber **quién** tiene capacidad para actuar ante la Administración, **quién es interesado** en un procedimiento y **cómo** se actúa por medio de otro.",
  ["1 Capacidad de obrar y concepto de interesado (arts. 3 y 4)", "2 Representación, pluralidad, nuevos interesados y firma (arts. 5, 7, 8 y 11)"]))

T.ap("s1", "I.1 Capacidad de obrar y concepto de interesado (arts. 3 y 4)", f"""
{unidad("1.1 Capacidad de obrar (art. 3)",
  lit("L39", "Artículo 3", ["con arreglo a las normas civiles", "Los menores de edad", "Cuando la Ley así lo declare expresamente"]),
  fichab("Quién puede actuar por sí mismo ante las Administraciones Públicas",
         ["::Tienen capacidad de obrar:", "Personas físicas o jurídicas con capacidad de obrar según las normas civiles", "Menores de edad, para los derechos e intereses cuya actuación permita el ordenamiento sin asistencia de quien ejerza la patria potestad, tutela o curatela", "Grupos de afectados, uniones y entidades sin personalidad jurídica y patrimonios independientes o autónomos, cuando la Ley así lo declare expresamente"],
         "—",
         "—",
         f"Los entes sin personalidad solo tienen capacidad {c('L39', 'Artículo 3', 'Cuando la Ley así lo declare expresamente')}. El art. 13 reconoce sus derechos a quienes tienen capacidad de obrar según este artículo (→ II.1.1)."))}

{unidad("1.2 Concepto de interesado (art. 4)",
  lit("L39", "Artículo 4", ["Quienes lo promuevan", "tengan derechos que puedan resultar afectados", "se personen en el procedimiento en tanto no haya recaído resolución definitiva", "intereses legítimos colectivos", "el derecho-habiente sucederá en tal condición cualquiera que sea el estado del procedimiento"]),
  fichab("Quién tiene la condición de interesado en un procedimiento",
         ["::Tres grupos (4.1):", "a) Quienes **promueven** el procedimiento como titulares de derechos o intereses legítimos individuales o colectivos", "b) Quienes, sin haberlo iniciado, tienen **derechos** que pueden resultar afectados por la decisión", "c) Quienes tienen **intereses legítimos** que pueden resultar afectados y se **personan** mientras no haya resolución definitiva"],
         ["Asociaciones y organizaciones representativas de intereses económicos y sociales: titulares de intereses legítimos colectivos en los términos que la Ley reconozca (4.2)", "Relación jurídica transmisible: el derecho-habiente sucede en la condición de interesado (4.3)"],
         f"Personación del grupo c): {c('L39', 'Artículo 4', 'en tanto no haya recaído resolución definitiva')}",
         "Quien tiene **derechos** afectados es interesado aunque no se persone (b); quien solo tiene **intereses legítimos** necesita **personarse** (c). La sucesión opera **cualquiera que sea el estado** del procedimiento."))}
""", 2)

T.ap("s2", "I.2 Representación, pluralidad, nuevos interesados y firma (arts. 5, 7, 8 y 11)", f"""
{unidad("2.1 Representación (art. 5)",
  lit("L39", "Artículo 5", ["salvo manifestación expresa en contra del interesado", "siempre que ello esté previsto en sus Estatutos", "deberá acreditarse la representación", "Para los actos y gestiones de mero trámite se presumirá aquella representación", "apoderamiento apud acta", "dentro del plazo de diez días", "siempre podrá comparecer el interesado por sí mismo en el procedimiento"], solo=[1, 2, 3, 4, 5, 7, 8]),
  fichab("Actuación del interesado por medio de otra persona",
         ["Interesados con capacidad de obrar (representados)", "Representantes: personas físicas con capacidad de obrar y personas jurídicas, si lo prevén sus Estatutos (5.2)"],
         ["::Hay que **acreditar** la representación para:", "Formular solicitudes", "Presentar declaraciones responsables o comunicaciones", "Interponer recursos", "Desistir de acciones y renunciar a derechos", "Actos de **mero trámite**: la representación se **presume** (5.3)", "Acreditación: cualquier medio válido en Derecho; entre otros, apoderamiento apud acta o inscripción en el registro electrónico de apoderamientos (5.4)"],
         f"Subsanación: {c('L39', 'Artículo 5', 'dentro del plazo de diez días que deberá conceder al efecto el órgano administrativo')}, o superior si las circunstancias lo requieren (5.6)",
         "La falta de acreditación **no impide** tener por realizado el acto si se subsana en **diez días**. Para **interponer recursos** hay que acreditar la representación; para el mero trámite, se presume."))}

{unidad("2.2 Pluralidad de interesados y nuevos interesados (arts. 7 y 8)",
  lit("L39", "Artículo 7", ["en su defecto, con el que figure en primer término"]),
  lit("L39", "Artículo 8", ["que no haya tenido publicidad", "se comunicará a dichas personas la tramitación del procedimiento"]),
  fichab("Con quién se entienden las actuaciones y qué se hace con los afectados no personados",
         "La Administración que tramita",
         ["Varios interesados en un escrito: con el representante o interesado señalado expresamente; en su defecto, con el que figure **en primer término** (art. 7)", "Procedimiento **sin publicidad**: si del expediente resultan titulares de derechos o intereses legítimos y directos que puedan resultar afectados, **se les comunica** la tramitación (art. 8)"],
         "—",
         "El art. 8 opera en procedimientos que **no** hayan tenido publicidad y durante la **instrucción**."))}

{unidad("2.3 Cuándo se exige firma (art. 11)",
  lit("L39", "Artículo 11", ["será suficiente con que los interesados acrediten previamente su identidad", "sólo requerirán a los interesados el uso obligatorio de firma", "Interponer recursos"]),
  fichab("Identificación como regla general; firma solo en los casos tasados",
         "Los interesados",
         ["::Regla: basta **acreditar la identidad** (11.1). Firma obligatoria solo para (11.2):", "Formular solicitudes", "Presentar declaraciones responsables o comunicaciones", "Interponer recursos", "Desistir de acciones", "Renunciar a derechos"],
         "—",
         "La lista de la firma obligatoria coincide con los actos para los que hay que **acreditar la representación** (5.3 → I.2.1)."))}

{resumen([
  "Capacidad de obrar: personas con capacidad según las **normas civiles**, **menores** en lo que el ordenamiento les permita y entes sin personalidad **si la Ley lo declara** (3).",
  "Interesados: quienes **promueven**, quienes tienen **derechos** afectados y quienes tienen **intereses legítimos** afectados y se **personan** antes de la resolución definitiva (4).",
  "Representación: se **acredita** para solicitudes, declaraciones, **recursos**, desistimiento y renuncia; se **presume** en el mero trámite; subsanación en **10 días** (5).",
  "Firma obligatoria solo en esos mismos supuestos; para lo demás basta identificarse (11)."],
  "Siguiente: II. ¿Qué derechos tienen los ciudadanos?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Qué derechos tienen los ciudadanos? (arts. 13, 14 y 53.1)", donde(
  "Segunda pregunta. La Ley 39/2015 distingue dos listas: los derechos de **todas las personas** en sus relaciones con las Administraciones (art. 13) y los derechos de los **interesados** dentro de un procedimiento concreto (art. 53.1).",
  ["1 Derechos de las personas (art. 13)", "2 Derecho y obligación de relacionarse electrónicamente (art. 14)", "3 Derechos del interesado en el procedimiento (art. 53.1)", "4 Cuadro: art. 13 frente a art. 53.1"]))

T.ap("s3", "II.1 Derechos de las personas en sus relaciones con las Administraciones Públicas (art. 13)", f"""
{unidad("1.1 La lista del art. 13",
  lit("L39", "Artículo 13", ["Quienes de conformidad con el artículo 3, tienen capacidad de obrar", "Punto de Acceso General electrónico", "A ser asistidos en el uso de medios electrónicos", "A utilizar las lenguas oficiales en el territorio de su Comunidad Autónoma", "Al acceso a la información pública, archivos y registros", "A ser tratados con respeto y deferencia", "A exigir las responsabilidades", "A la protección de datos de carácter personal", "sin perjuicio de los reconocidos en el artículo 53"]),
  ficha(f"{c('L39', 'Artículo 13', 'Quienes de conformidad con el artículo 3, tienen capacidad de obrar ante las Administraciones Públicas')} (→ I.1.1), sean o no interesados en un procedimiento",
        ["a) Comunicarse a través de un **Punto de Acceso General electrónico**", "b) Ser **asistidos** en el uso de medios electrónicos", "c) Utilizar las **lenguas oficiales** en el territorio de su Comunidad Autónoma", "d) **Acceso a la información pública**, archivos y registros (Ley 19/2013)", "e) Ser tratados con **respeto y deferencia**", "f) **Exigir las responsabilidades** de las Administraciones y autoridades", "g) Obtener y utilizar los **medios de identificación y firma** electrónica", "h) **Protección de datos** personales", "i) Cualesquiera otros que reconozcan la Constitución y las leyes"],
        "Lenguas: de acuerdo con la Ley 39/2015 y el resto del ordenamiento; acceso a la información: de acuerdo con la Ley 19/2013; responsabilidades: cuando así corresponda legalmente",
        "—",
        "El art. 13 es de las **personas** (relaciones con la Administración en general); el art. 53 es del **interesado** en un procedimiento. Son compatibles: «sin perjuicio» de los del art. 53 (→ II.3.1)."))}
""", 2)

T.ap("s4", "II.2 Derecho y obligación de relacionarse electrónicamente (art. 14)", f"""
{unidad("2.1 Quién elige y quién está obligado (art. 14)",
  lit("L39", "Artículo 14", ["podrán elegir en todo momento", "podrá ser modificado por aquella en cualquier momento", "Las personas jurídicas", "Las entidades sin personalidad jurídica", "colegiación obligatoria", "Quienes representen a un interesado", "Los empleados de las Administraciones Públicas", "Reglamentariamente"]),
  ficha(["Personas **físicas**: derecho a elegir (14.1)", "Obligados (14.2): los sujetos de la lista"],
        ["Las personas físicas eligen **en todo momento** el medio, y pueden cambiarlo en cualquier momento, salvo que estén obligadas", "::Obligados, al menos (14.2):", "a) Personas jurídicas", "b) Entidades sin personalidad jurídica", "c) Profesionales de colegiación obligatoria, en el ejercicio de esa actividad (incluidos notarios y registradores)", "d) Representantes de un interesado obligado", "e) Empleados públicos, por razón de su condición de empleado público"],
        f"Reglamentariamente puede imponerse a {c('L39', 'Artículo 14', 'ciertos colectivos de personas físicas')} con acceso y disponibilidad acreditados de medios electrónicos (14.3)",
        "Los no obligados pueden pedir **asistencia** en el uso de medios electrónicos (art. 12.2; derecho del art. 13 b → II.1.1)",
        "La **persona física** elige; la **persona jurídica** está obligada siempre. La obligación de ciertos colectivos de personas físicas se impone **reglamentariamente** (no hace falta ley)."))}
""", 2)

T.ap("s5", "II.3 Derechos del interesado en el procedimiento (art. 53.1)", f"""
La Ley 39/2015 abre su Título IV con un capítulo titulado «Garantías del procedimiento», que contiene solo el art. 53: su apartado 1 recoge los **derechos del interesado** y su apartado 2, los del **presunto responsable** en el procedimiento sancionador (→ III.1.1).

{unidad("3.1 La lista del art. 53.1",
  lit("L39", "Artículo 53", ["A conocer, en cualquier momento, el estado de la tramitación", "acceder y a obtener copia de los documentos", "A identificar a las autoridades y al personal", "A no presentar documentos originales", "A no presentar datos y documentos no exigidos", "en cualquier fase del procedimiento anterior al trámite de audiencia", "A obtener información y orientación", "A actuar asistidos de asesor", "A cumplir las obligaciones de pago"], solo=list(range(1, 12))),
  ficha("Los **interesados** en un procedimiento administrativo (→ I.1.2), además del resto de derechos de la ley",
        ["a) **Conocer en cualquier momento** el estado de la tramitación, el sentido del silencio, el órgano competente y los actos de trámite; **acceder y obtener copia** de los documentos", "b) **Identificar** a las autoridades y al personal bajo cuya responsabilidad se tramitan", "c) **No presentar documentos originales**, salvo excepción normativa (y entonces, copia autenticada)", "d) **No presentar datos y documentos** no exigidos o que ya tenga la Administración", "e) **Formular alegaciones**, usar los medios de defensa y **aportar documentos** en cualquier fase **anterior al trámite de audiencia**", "f) **Información y orientación** sobre los requisitos de proyectos, actuaciones o solicitudes", "g) Actuar **asistidos de asesor**", "h) Cumplir las obligaciones de pago por **medios electrónicos** (art. 98.2)", "i) Cualesquiera otros que reconozcan la Constitución y las leyes"],
        "Original solo si la normativa lo establece «de manera excepcional»; documentos y alegaciones, antes del trámite de audiencia",
        f"Lo alegado y aportado {c('L39', 'Artículo 53', 'deberán ser tenidos en cuenta por el órgano competente al redactar la propuesta de resolución')}; con medios electrónicos, la consulta se hace en el Punto de Acceso General electrónico",
        "Cayó dos veces en 2025 (→ Cierre 1): **conocer en cualquier momento** el estado de la tramitación (a) e **identificar** a autoridades y personal (b). Los distractores: «Aportar documentos **una vez finalizado** el trámite de audiencia» (es **antes**) o «Exigir que la Administración aporte los documentos **originales**» (el derecho es a **no presentarlos**)."))}
""", 2)

T.ap("s6", "II.4 Cuadro: derechos de las personas (art. 13) y derechos del interesado (art. 53.1) (esquema)", f"""
{ESQ}

| | Art. 13 | Art. 53.1 |
|---|---|---|
| Titulares | Quienes tienen **capacidad de obrar** (art. 3) | Los **interesados** en un procedimiento (art. 4) |
| Ámbito | Relaciones con las Administraciones en general | Un **procedimiento** concreto |
| Derechos característicos | Punto de Acceso General; asistencia electrónica; lenguas oficiales; acceso a la información pública; respeto y deferencia; exigir responsabilidades; identificación y firma electrónica; protección de datos | Conocer el estado de la tramitación; identificar al personal; no presentar originales ni documentos ya en poder de la Administración; alegar y aportar antes de la audiencia; información y orientación; asesor; pago electrónico |
| Cláusula final | «Cualesquiera otros que les reconozcan la Constitución y las leyes» | La misma |

{resumen([
  "Art. 13: derechos de **quienes tienen capacidad de obrar** en sus relaciones con las Administraciones (Punto de Acceso General, lenguas oficiales, información pública, respeto y deferencia, responsabilidades, protección de datos…).",
  "Art. 14: la persona **física elige** el medio; las **jurídicas** y los demás sujetos del 14.2 están **obligados** a relacionarse electrónicamente.",
  "Art. 53.1: derechos del **interesado**: **conocer en cualquier momento** el estado de la tramitación, **identificar** al personal, **no presentar originales**, alegar y aportar **antes del trámite de audiencia**, asesor."],
  "Siguiente: III. ¿Qué garantías rodean el desarrollo del procedimiento?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Qué garantías rodean el desarrollo del procedimiento? (art. 53.2; Ley 40/2015, arts. 23 y 24)", donde(
  "Tercera pregunta. Además de los derechos del interesado (→ II.3), el procedimiento tiene garantías propias: las del **presunto responsable** en el procedimiento sancionador y la **imparcialidad** de las autoridades y el personal que intervienen (abstención y recusación).",
  ["1 Garantías del presunto responsable en el procedimiento sancionador (art. 53.2)", "2 Imparcialidad: abstención y recusación (Ley 40/2015, arts. 23 y 24)"]))

T.ap("s7", "III.1 Garantías del presunto responsable en el procedimiento sancionador (art. 53.2)", f"""
{unidad("1.1 Los derechos del art. 53.2",
  lit("L39", "Artículo 53", ["procedimientos administrativos de naturaleza sancionadora", "A ser notificado de los hechos que se le imputen", "la identidad del instructor", "A la presunción de no existencia de responsabilidad administrativa"], solo=[12, 13, 14]),
  ficha(f"{c('L39', 'Artículo 53', 'los presuntos responsables')} en procedimientos de naturaleza sancionadora",
        ["::Además de los del 53.1:", "a) Ser **notificado** de los hechos imputados, las infracciones que pueden constituir, las sanciones que pueden imponerse, la **identidad del instructor**, la autoridad competente para sancionar y la norma que le atribuye la competencia", "b) **Presunción de no existencia de responsabilidad administrativa** mientras no se demuestre lo contrario"],
        "—",
        "—",
        "Se suman a los del art. 53.1 («Además de los derechos previstos en el apartado anterior»). Hay que notificar también la identidad del **instructor** y la **norma** que atribuye la competencia."))}
""", 2)

T.ap("s8", "III.2 Imparcialidad: abstención y recusación (Ley 40/2015, arts. 23 y 24)", f"""
{unidad("2.1 Abstención (Ley 40/2015, art. 23)",
  lit("L40", "Artículo 23", ["lo comunicarán a su superior inmediato", "Tener interés personal en el asunto", "consanguinidad dentro del cuarto grado o de afinidad dentro del segundo", "amistad íntima o enemistad manifiesta", "como perito o como testigo", "en los dos últimos años", "podrán ordenarle que se abstengan", "no implicará, necesariamente, y en todo caso, la invalidez", "dará lugar a la responsabilidad que proceda"]),
  fichab("Deber de no intervenir en el procedimiento cuando concurre un motivo legal",
         "Las autoridades y el personal al servicio de las Administraciones; resuelve el **superior inmediato**; los superiores jerárquicos pueden **ordenar** la abstención",
         ["::Motivos (23.2):", "a) **Interés personal** en el asunto; administrador de sociedad interesada; cuestión litigiosa pendiente con un interesado", "b) **Matrimonio** o situación de hecho asimilable; parentesco de **consanguinidad hasta el cuarto grado** o de **afinidad hasta el segundo** con interesados, administradores, asesores, representantes o mandatarios; compartir despacho o estar asociado", "c) **Amistad íntima o enemistad manifiesta**", "d) Haber intervenido como **perito o testigo** en el procedimiento", "e) **Relación de servicio** con el interesado directo o haberle prestado servicios profesionales en los **dos últimos años**"],
         "Parentesco: consanguinidad, **cuarto** grado; afinidad, **segundo**. Servicios profesionales: **dos** últimos años",
         "Actuar con motivo de abstención **no implica necesariamente** la invalidez del acto (23.4), pero **no abstenerse** da lugar a **responsabilidad** (23.5)."))}

{unidad("2.2 Recusación (Ley 40/2015, art. 24)",
  lit("L40", "Artículo 24", ["por los interesados en cualquier momento de la tramitación del procedimiento", "por escrito", "En el día siguiente", "acordará su sustitución acto seguido", "en el plazo de tres días", "no cabrá recurso"]),
  fichab("Petición del interesado para apartar a quien incurre en un motivo de abstención",
         "La promueven los **interesados**; el recusado manifiesta si concurre la causa; resuelve su **inmediato superior**",
         ["Por **escrito**, expresando la causa o causas (24.2)", "Si el recusado **admite** la causa y el superior la aprecia: sustitución **acto seguido** (24.3)", "Si la **niega**: el superior resuelve, previos los informes y comprobaciones oportunos (24.4)"],
         f"Cuándo: {c('L40', 'Artículo 24', 'en cualquier momento de la tramitación del procedimiento')}; el recusado responde {c('L40', 'Artículo 24', 'En el día siguiente')}; el superior resuelve {c('L40', 'Artículo 24', 'en el plazo de tres días')}",
         "Las causas de recusación son **las mismas** que las de abstención («En los casos previstos en el artículo anterior»). Contra lo resuelto **no cabe recurso**, pero puede alegarse la recusación al recurrir el acto que ponga fin al procedimiento."))}

{ESQ}

| | Abstención (art. 23) | Recusación (art. 24) |
|---|---|---|
| Quién la inicia | La propia autoridad o empleado (o se la ordena su superior jerárquico) | Los **interesados** |
| Motivos | Los del art. 23.2 | Los mismos |
| Quién decide | El **superior inmediato** | El **inmediato superior** del recusado |
| Plazos | — | Recusado: **día siguiente**; superior, si se niega la causa: **tres días** |
| Consecuencia | Su omisión: **responsabilidad**; no necesariamente invalidez | Sustitución del recusado; **sin recurso** autónomo |

{resumen([
  "Presunto responsable (53.2): derecho a ser **notificado** de hechos, infracciones, sanciones, **instructor**, autoridad y norma; **presunción de no existencia de responsabilidad**.",
  "Abstención (Ley 40/2015, art. 23): cinco motivos; parentesco de consanguinidad hasta el **cuarto** grado y de afinidad hasta el **segundo**; servicios en los **dos** últimos años; no abstenerse genera **responsabilidad**, no necesariamente invalidez.",
  "Recusación (art. 24): la promueven los **interesados** en **cualquier momento**, por **escrito**; el recusado responde al **día siguiente**; el superior resuelve en **tres días**; **sin recurso**."],
  "Siguiente: IV. ¿Cómo revisa la Administración sus propios actos? La revisión de oficio")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Cómo revisa la Administración sus propios actos? La revisión de oficio (arts. 106 a 111; Ley 7/1985, art. 22.2 k)", donde(
  "Cuarta pregunta. El Título V de la Ley 39/2015 trata «De la revisión de los actos en vía administrativa». Su capítulo I, «Revisión de oficio», permite a la Administración **declarar la nulidad** de actos y disposiciones, **impugnar** sus actos favorables anulables previa **declaración de lesividad**, **revocar** actos desfavorables y **rectificar errores**. Los vicios de nulidad y anulabilidad (arts. 47 y 48) son del tema IV.4.",
  ["1 Revisión de actos y disposiciones nulos (art. 106)", "2 Declaración de lesividad de actos anulables (art. 107; Ley 7/1985, art. 22.2 k)", "3 Suspensión, revocación, rectificación de errores y límites (arts. 108 a 110)", "4 Competencia en el ámbito estatal (art. 111) y cuadro"]))

T.ap("s9", "IV.1 Revisión de actos y disposiciones nulos (art. 106)", f"""
{unidad("1.1 Revisión de oficio de actos y disposiciones nulos (art. 106)",
  lit("L39", "Artículo 106", ["en cualquier momento, por iniciativa propia o a solicitud de interesado", "previo dictamen favorable del Consejo de Estado u órgano consultivo equivalente de la Comunidad Autónoma", "que hayan puesto fin a la vía administrativa o que no hayan sido recurridos en plazo", "podrán declarar la nulidad de las disposiciones administrativas", "inadmisión a trámite", "las indemnizaciones que proceda reconocer", "subsistan los actos firmes", "el transcurso del plazo de seis meses desde su inicio sin dictarse resolución producirá la caducidad", "se podrá entender la misma desestimada por silencio administrativo"]),
  fichab("Declaración de nulidad por la propia Administración de actos (art. 47.1) y disposiciones (art. 47.2)",
         ["Las Administraciones Públicas, por **iniciativa propia o a solicitud de interesado** (actos); solo **de oficio** (disposiciones)", "Dictamen **favorable** del Consejo de Estado u órgano consultivo autonómico equivalente"],
         ["Actos: los que hayan **puesto fin a la vía administrativa** o **no hayan sido recurridos en plazo**, en los supuestos del art. 47.1", "Disposiciones: en los supuestos del art. 47.2", "Inadmisión motivada sin dictamen: solicitud que no se base en causa del 47.1, que carezca manifiestamente de fundamento o igual a otras ya desestimadas en cuanto al fondo (106.3)", "Puede fijar en la misma resolución las **indemnizaciones** (106.4); si es una disposición, subsisten los actos firmes dictados en su aplicación"],
         f"Cuándo: {c('L39', 'Artículo 106', 'en cualquier momento')}. Plazo para resolver: **seis meses**; iniciado de oficio → **caducidad**; a solicitud de interesado → **desestimación** por silencio (106.5)",
         "El dictamen del Consejo de Estado debe ser **favorable** (no basta pedirlo). La solicitud del interesado solo cabe para **actos**; las **disposiciones** se revisan **de oficio**. Para inadmitir **no** hace falta dictamen."))}
""", 2)

T.ap("s10", "IV.2 Declaración de lesividad de actos anulables (art. 107; Ley 7/1985, art. 22.2 k)", f"""
{unidad("2.1 Lesividad: la Administración impugna su propio acto ante el juez (art. 107)",
  lit("L39", "Artículo 107", ["los actos favorables para los interesados que sean anulables", "previa su declaración de lesividad para el interés público", "cuatro años desde que se dictó el acto administrativo", "previa audiencia de cuantos aparezcan como interesados", "no será susceptible de recurso", "seis meses desde la iniciación del procedimiento", "por el órgano de cada Administración competente en la materia", "por el Pleno de la Corporación"]),
  fichab("Declaración de que un acto favorable anulable es lesivo para el interés público, paso previo a impugnarlo ante el orden contencioso-administrativo",
         ["Estado y Comunidades Autónomas: el **órgano competente en la materia** (107.4)", "Entidades locales: el **Pleno** de la Corporación o, en su defecto, el órgano colegiado superior (107.5)"],
         ["La Administración **no anula** por sí misma: declara la lesividad e **impugna** ante el orden jurisdiccional contencioso-administrativo (107.1)", "Previa **audiencia** de los interesados (art. 82)", "La declaración **no es recurrible**; puede notificarse a efectos informativos"],
         f"Límite: {c('L39', 'Artículo 107', 'no podrá adoptarse una vez transcurridos cuatro años desde que se dictó el acto administrativo')}. **Seis meses** desde la iniciación sin declararla → **caducidad** (107.3)",
         "Actos **favorables** y **anulables** (art. 48). **Cuatro años** desde que **se dictó** el acto (no desde la notificación). En los entes locales, el **Pleno**."))}

{unidad("2.2 En el municipio, el Pleno (Ley 7/1985, art. 22.2 k)",
  lit("LRBRL", "Artículo 22", ["al Pleno municipal en los Ayuntamientos, y a la Asamblea vecinal en el régimen de Concejo Abierto", "La declaración de lesividad de los actos del Ayuntamiento"], solo=list(range(2, 21)), titulo="Artículo 22.2 (Ley 7/1985, Reguladora de las Bases del Régimen Local)"),
  fichab("Órgano municipal competente para declarar la lesividad",
         "El **Pleno** municipal; en régimen de Concejo Abierto, la **Asamblea vecinal**",
         "Es atribución que les corresponde «en todo caso» (art. 22.2)",
         "—",
         "Coincide con el art. 107.5 de la Ley 39/2015 (→ IV.2.1). Cayó en 2025 como pregunta de régimen local (→ Cierre 1)."))}
""", 2)

T.ap("s11", "IV.3 Suspensión, revocación, rectificación de errores y límites (arts. 108 a 110)", f"""
{unidad("3.1 Suspensión del acto durante la revisión (art. 108)",
  lit("L39", "Artículo 108", ["podrá suspender la ejecución del acto", "perjuicios de imposible o difícil reparación"]),
  fichab("Medida para que el acto no se ejecute mientras se revisa",
         "El órgano competente para declarar la nulidad o la lesividad",
         "Una vez **iniciado** el procedimiento de los arts. 106 o 107",
         "—",
         "Es **potestativa** («podrá») y exige que la ejecución pueda causar perjuicios de **imposible o difícil reparación**."))}

{unidad("3.2 Revocación de actos desfavorables y rectificación de errores (art. 109)",
  lit("L39", "Artículo 109", ["mientras no haya transcurrido el plazo de prescripción", "actos de gravamen o desfavorables", "dispensa o exención no permitida por las leyes", "rectificar en cualquier momento, de oficio o a instancia de los interesados, los errores materiales, de hecho o aritméticos"]),
  fichab("Dos facultades distintas: dejar sin efecto actos desfavorables (revocación) y corregir errores (rectificación)",
         "Las Administraciones Públicas; la rectificación, **de oficio o a instancia** de los interesados",
         ["Revocación (109.1): solo actos **de gravamen o desfavorables**; no puede constituir dispensa o exención no permitida, ni ser contraria a la igualdad, al interés público o al ordenamiento", "Rectificación (109.2): errores **materiales, de hecho o aritméticos**"],
         f"Revocación: {c('L39', 'Artículo 109', 'mientras no haya transcurrido el plazo de prescripción')}. Rectificación: **en cualquier momento**",
         "Se **revocan** actos **desfavorables** (los favorables anulables van por lesividad → IV.2.1). La rectificación es de errores **materiales, de hecho o aritméticos**, no de errores de derecho."))}

{unidad("3.3 Límites de la revisión (art. 110)",
  lit("L39", "Artículo 110", ["por prescripción de acciones, por el tiempo transcurrido o por otras circunstancias", "contrario a la equidad, a la buena fe, al derecho de los particulares o a las leyes"]),
  fichab("Límite común a todas las facultades de revisión del capítulo",
         "Afecta a la Administración que revisa",
         "No pueden ejercerse cuando, por prescripción de acciones, por el tiempo transcurrido o por otras circunstancias, su ejercicio resulte contrario a la **equidad**, a la **buena fe**, al **derecho de los particulares** o a las **leyes**",
         "—",
         "Aunque la nulidad puede declararse «en cualquier momento» (→ IV.1.1), este artículo la limita."))}
""", 2)

T.ap("s12", "IV.4 Competencia en el ámbito estatal (art. 111) y cuadro de la revisión de oficio", f"""
{unidad("4.1 Quién revisa en la Administración General del Estado (art. 111)",
  lit("L39", "Artículo 111", ["El Consejo de Ministros, respecto de sus propios actos y disposiciones y de los actos y disposiciones dictados por los Ministros", "Los Ministros, respecto de los actos y disposiciones de los Secretarios de Estado", "Los Secretarios de Estado, respecto de los actos y disposiciones dictados por los órganos directivos de ellos dependientes", "Los máximos órganos rectores"]),
  fichab("Órgano competente para la revisión de oficio de disposiciones y actos nulos y anulables en el ámbito estatal",
         ["a) **Consejo de Ministros**: sus actos y disposiciones y los de los **Ministros**", "b) 1.º **Ministros**: los de los **Secretarios de Estado** y de los órganos directivos no dependientes de una Secretaría de Estado", "b) 2.º **Secretarios de Estado**: los de sus órganos directivos dependientes", "c) Organismos públicos: el órgano de adscripción revisa los del máximo órgano rector; el máximo órgano rector, los de sus órganos dependientes"],
         "La regla: revisa el órgano **superior** o, en el caso del Consejo de Ministros, el propio órgano",
         "—",
         "Los actos de los **Ministros** los revisa el **Consejo de Ministros**; los de los **Secretarios de Estado**, el **Ministro**."))}

{ESQ}

| Figura | Artículo | Actos | Quién la inicia | Requisito clave | Plazo |
|---|---|---|---|---|---|
| Revisión de actos nulos | 106.1 | Nulos (47.1) que pusieron fin a la vía o no se recurrieron en plazo | De oficio o a solicitud de interesado | Dictamen **favorable** del Consejo de Estado o equivalente | En cualquier momento; resolver en 6 meses |
| Revisión de disposiciones nulas | 106.2 | Disposiciones nulas (47.2) | De oficio | Dictamen **favorable** | En cualquier momento |
| Lesividad | 107 | **Favorables** anulables (48) | La Administración | Audiencia; después, impugnación ante el contencioso | 4 años desde que se dictó; caducidad a los 6 meses |
| Revocación | 109.1 | **De gravamen o desfavorables** | La Administración | Sin dispensa no permitida ni contraria a igualdad, interés público u ordenamiento | Mientras no prescriba |
| Rectificación | 109.2 | Errores materiales, de hecho o aritméticos | De oficio o a instancia | — | En cualquier momento |

{resumen([
  "Nulidad (106): actos nulos firmes en vía administrativa o no recurridos, **en cualquier momento**, de oficio o a solicitud, con dictamen **favorable** del Consejo de Estado; disposiciones, solo de oficio; **6 meses** (caducidad o desestimación).",
  "Lesividad (107): actos **favorables anulables**; **4 años** desde que se dictó; audiencia; no recurrible; **6 meses** o caducidad; después, **impugnación ante el contencioso**; en los entes locales, el **Pleno**.",
  "Revocación de actos **desfavorables** mientras no prescriba; rectificación de errores **materiales, de hecho o aritméticos** en cualquier momento (109); límites de **equidad, buena fe**, derecho de los particulares y leyes (110).",
  "Estado (111): Consejo de Ministros (sus actos y los de los Ministros), Ministros (Secretarios de Estado), Secretarios de Estado (sus órganos directivos)."],
  "Siguiente: V. ¿Cómo recurre el interesado en vía administrativa? Los recursos administrativos")}
""", 2)

# =============================================================================
T.ap("bV", "V. ¿Cómo recurre el interesado en vía administrativa? Los recursos administrativos (arts. 112 a 126)", donde(
  "Quinta pregunta. El capítulo II del Título V regula los **recursos administrativos**: unos principios generales comunes (sección 1.ª) y tres recursos: **alzada** (sección 2.ª), **potestativo de reposición** (sección 3.ª) y **extraordinario de revisión** (sección 4.ª).",
  ["1 Objeto, clases y fin de la vía administrativa (arts. 112 a 114)", "2 Interposición, inadmisión, suspensión, audiencia y resolución (arts. 115 a 120)", "3 Recurso de alzada (arts. 121 y 122)", "4 Recurso potestativo de reposición (arts. 123 y 124)", "5 Recurso extraordinario de revisión (arts. 125 y 126)", "6 Cuadro comparativo de los tres recursos"]))

T.ap("s13", "V.1 Objeto, clases y fin de la vía administrativa (arts. 112 a 114)", f"""
{unidad("1.1 Qué se recurre, con qué recursos y por qué motivos (art. 112)",
  lit("L39", "Artículo 112", ["Contra las resoluciones y los actos de trámite", "los recursos de alzada y potestativo de reposición", "cualquiera de los motivos de nulidad o anulabilidad previstos en los artículos 47 y 48", "La oposición a los restantes actos de trámite", "Las leyes podrán sustituir el recurso de alzada", "respetando su carácter potestativo para el interesado", "Contra las disposiciones administrativas de carácter general no cabrá recurso en vía administrativa", "legislación específica"]),
  fichab("Objeto de los recursos ordinarios y posibilidad de sustituirlos",
         "Los **interesados**",
         ["::Se recurren (112.1):", "Las **resoluciones**", "Los actos de trámite **cualificados**: deciden directa o indirectamente el fondo, impiden continuar el procedimiento o producen indefensión o perjuicio irreparable", "Los demás actos de trámite: la oposición se alega para la **resolución** que ponga fin al procedimiento", "Motivos: los de nulidad o anulabilidad de los arts. **47 y 48**", "Las **leyes** pueden sustituir la alzada (y la reposición, respetando su carácter potestativo) por otros procedimientos ante órganos colegiados o comisiones no sometidas a instrucciones jerárquicas (112.2)", "**Disposiciones generales**: no cabe recurso en vía administrativa (112.3)"],
         "—",
         "Contra los **reglamentos** no hay recurso administrativo; un recurso contra un acto fundado **solo** en la nulidad de una disposición general puede interponerse **directamente ante el órgano que la dictó**. La sustitución de la alzada la hacen las **leyes**, no los reglamentos."))}

{unidad("1.2 El recurso extraordinario de revisión, solo contra actos firmes (art. 113)",
  lit("L39", "Artículo 113", ["Contra los actos firmes en vía administrativa", "sólo procederá"]),
  fichab("Recurso extraordinario: objeto y causas tasadas",
         "Los interesados",
         "Contra actos **firmes en vía administrativa**, solo en las circunstancias del art. 125.1 (→ V.5.1)",
         "—",
         "Es el único recurso contra actos **firmes**; las causas son tasadas («sólo procederá»)."))}

{unidad("1.3 Actos que ponen fin a la vía administrativa (art. 114)",
  lit("L39", "Artículo 114", ["Las resoluciones de los recursos de alzada", "carezcan de superior jerárquico, salvo que una Ley establezca lo contrario", "Los acuerdos, pactos, convenios o contratos", "responsabilidad patrimonial", "Los actos administrativos de los miembros y órganos del Gobierno", "Los emanados de los Ministros y los Secretarios de Estado", "en materia de personal"]),
  fichab("Actos contra los que ya no cabe alzada: solo reposición potestativa o recurso contencioso-administrativo",
         "Según el órgano que dicta el acto o el procedimiento que resuelve",
         ["::En general (114.1):", "a) Resoluciones de los recursos de **alzada**", "b) Resoluciones de los procedimientos sustitutivos del art. 112.2", "c) Resoluciones de órganos **sin superior jerárquico**, salvo que una Ley establezca lo contrario", "d) Acuerdos, pactos, convenios o contratos finalizadores", "e) Resolución de la **responsabilidad patrimonial**", "f) Procedimientos complementarios en materia sancionadora (art. 90.4)", "g) Las demás cuando una disposición legal o reglamentaria lo establezca", "::En el ámbito estatal, además (114.2):", "a) Miembros y órganos del **Gobierno**", "b) **Ministros y Secretarios de Estado**, en sus competencias", "c) Órganos directivos con nivel de **Director general o superior**, en materia de **personal**", "d) Máximos órganos de dirección de los organismos públicos estatales, según sus estatutos, salvo ley"],
         "—",
         "Cayó en 2025 (→ Cierre 1): el Director general pone fin a la vía **solo en materia de personal**, no en todas las competencias de su Dirección General."))}
""", 2)

T.ap("s14", "V.2 Interposición, inadmisión, suspensión, audiencia y resolución (arts. 115 a 120)", f"""
{unidad("2.1 Interposición del recurso (art. 115)",
  lit("L39", "Artículo 115", ["El nombre y apellidos del recurrente", "El acto que se recurre y la razón de su impugnación", "El error o la ausencia de la calificación del recurso", "no podrán ser alegados por quienes los hubieren causado"]),
  fichab("Contenido del escrito de recurso",
         "El recurrente",
         ["::El escrito expresa (115.1):", "a) Nombre, apellidos e identificación del recurrente", "b) Acto recurrido y razón de la impugnación", "c) Lugar, fecha, firma, medio y, en su caso, lugar para notificaciones", "d) Órgano, centro o unidad al que se dirige y su código de identificación", "e) Las demás particularidades de las disposiciones específicas"],
         "—",
         "El **error** o la **falta de calificación** del recurso no impiden tramitarlo si se deduce su verdadero carácter (115.2). Quien **causó** un vicio de anulabilidad no puede alegarlo (115.3)."))}

{unidad("2.2 Causas de inadmisión (art. 116)",
  lit("L39", "Artículo 116", ["cuando el competente perteneciera a otra Administración Pública", "Carecer de legitimación el recurrente", "Tratarse de un acto no susceptible de recurso", "Haber transcurrido el plazo", "Carecer el recurso manifiestamente de fundamento"]),
  fichab("Supuestos en que el recurso no se examina en cuanto al fondo",
         "El órgano que resuelve el recurso",
         ["a) Órgano **incompetente**, si el competente es de **otra Administración** (se remite al competente)", "b) Falta de **legitimación**", "c) Acto **no susceptible** de recurso", "d) Recurso **fuera de plazo**", "e) Recurso **manifiestamente** infundado"],
         "—",
         "La incompetencia es causa de inadmisión solo si el competente pertenece a **otra Administración**, y aun entonces el recurso **se remite** al órgano competente."))}

{unidad("2.3 Suspensión de la ejecución (art. 117)",
  lit("L39", "Artículo 117", ["no suspenderá la ejecución del acto impugnado", "previa ponderación, suficientemente razonada", "perjuicios de imposible o difícil reparación", "causas de nulidad de pleno derecho previstas en el artículo 47.1", "transcurrido un mes desde que la solicitud de suspensión haya tenido entrada", "caución o garantía suficiente", "publicada en el periódico oficial"]),
  fichab("Excepción a la regla de que el recurso no paraliza el acto",
         "El órgano a quien competa **resolver el recurso**, de oficio o a solicitud del recurrente",
         ["Regla (117.1): el recurso **no suspende** la ejecución, salvo disposición en contrario", "Puede suspender, previa **ponderación** razonada, si la ejecución causaría perjuicios de **imposible o difícil reparación** o la impugnación se funda en **nulidad de pleno derecho** (117.2)", "Puede adoptar medidas cautelares y exigir **caución** si la suspensión puede causar perjuicios (117.4)", "Acto que afecte a una pluralidad indeterminada de personas: la suspensión se **publica** en el periódico oficial (117.5)"],
         f"Silencio positivo sobre la suspensión: se entiende suspendida si {c('L39', 'Artículo 117', 'transcurrido un mes desde que la solicitud de suspensión haya tenido entrada en el registro electrónico')} sin resolución expresa notificada (117.3)",
         "**Un mes** sin resolver la solicitud = se entiende **suspendida**. Basta **una** de las dos circunstancias del 117.2."))}

{unidad("2.4 Audiencia de los interesados (art. 118)",
  lit("L39", "Artículo 118", ["en un plazo no inferior a diez días ni superior a quince", "habiendo podido aportarlos en el trámite de alegaciones no lo haya hecho", "se les dará, en todo caso, traslado del recurso", "no tienen el carácter de documentos nuevos"]),
  fichab("Trámite de audiencia en la resolución del recurso",
         "Los interesados (recurrente y demás interesados)",
         ["Solo si hay **nuevos hechos o documentos** no recogidos en el expediente originario (118.1)", "A los **otros interesados** se les da **siempre** traslado del recurso (118.2)", "No son documentos nuevos: el recurso, los informes, las propuestas ni lo aportado antes de la resolución impugnada (118.3)"],
         f"{c('L39', 'Artículo 118', 'en un plazo no inferior a diez días ni superior a quince')}",
         "Lo que el recurrente **pudo aportar** en alegaciones y no aportó **no se tiene en cuenta** al resolver el recurso."))}

{unidad("2.5 Resolución del recurso (art. 119)",
  lit("L39", "Artículo 119", ["estimará en todo o en parte o desestimará", "se ordenará la retroacción del procedimiento al momento en el que el vicio fue cometido", "hayan sido o no alegadas por los interesados", "sin que en ningún caso pueda agravarse su situación inicial"]),
  fichab("Contenido de la resolución del recurso",
         "El órgano competente para resolver",
         ["Estima total o parcialmente, desestima o **inadmite** (119.1)", "Vicio de forma sin resolver el fondo: **retroacción** al momento del vicio, sin perjuicio de la convalidación (art. 52) (119.2)", "Decide todas las cuestiones de forma y fondo, alegadas o no (oyendo antes a los interesados si no lo fueron) (119.3)"],
         "—",
         "La resolución es **congruente** con lo pedido y **nunca** puede agravar la situación inicial del recurrente: «sin que en ningún caso pueda agravarse su situación inicial» (119.3)."))}

{unidad("2.6 Pluralidad de recursos (art. 120)",
  lit("L39", "Artículo 120", ["traigan causa de un mismo acto administrativo", "podrá acordar la suspensión del plazo para resolver hasta que recaiga pronunciamiento judicial", "quienes podrán recurrirlo"]),
  fichab("Suspensión del plazo para resolver muchos recursos sobre un mismo acto mientras se decide uno en vía judicial",
         "El órgano administrativo que debe resolver",
         ["Supuesto: pluralidad de recursos contra un **mismo acto** y un recurso **judicial** ya interpuesto", "El acuerdo de suspensión se **notifica** y es **recurrible** (120.2)", "Tras el pronunciamiento judicial se resuelve sin más trámite, salvo audiencia cuando proceda (120.3)"],
         "Suspensión del plazo hasta que recaiga el pronunciamiento judicial",
         "La suspensión es **potestativa** («podrá») y el acuerdo **sí** es recurrible."))}
""", 2)

T.ap("s15", "V.3 Recurso de alzada (arts. 121 y 122)", f"""
{unidad("3.1 Objeto y órgano (art. 121)",
  lit("L39", "Artículo 121", ["cuando no pongan fin a la vía administrativa", "ante el órgano superior jerárquico del que los dictó", "Tribunales y órganos de selección", "ante el órgano que dictó el acto que se impugna o ante el competente para resolverlo", "deberá remitirlo al competente en el plazo de diez días", "responsable directo"]),
  fichab("Recurso ordinario ante el superior jerárquico contra actos que no ponen fin a la vía administrativa",
         ["Lo resuelve el **órgano superior jerárquico** del que dictó el acto", "Tribunales y órganos de selección y órganos con autonomía funcional: dependen del órgano al que estén adscritos o, en su defecto, del que nombró a su presidente"],
         ["Objeto: resoluciones y actos de trámite cualificados del art. 112.1 que **no pongan fin** a la vía administrativa", "Se interpone ante el órgano que dictó el acto **o** ante el competente para resolverlo"],
         f"Si se presenta ante el autor del acto, este {c('L39', 'Artículo 121', 'deberá remitirlo al competente en el plazo de diez días, con su informe y con una copia completa y ordenada del expediente')}",
         "Cayó en 2025 (→ Cierre 1): **deberá** (no «podrá») **remitirlo** (no «resolverlo») en **diez** días (no quince), con **informe** y **copia completa y ordenada** del expediente. El titular del órgano es **responsable directo**."))}

{unidad("3.2 Plazos (art. 122)",
  lit("L39", "Artículo 122", ["será de un mes, si el acto fuera expreso", "la resolución será firme a todos los efectos", "en cualquier momento a partir del día siguiente", "será de tres meses", "salvo en el supuesto previsto en el artículo 24.1, tercer párrafo", "no cabrá ningún otro recurso administrativo, salvo el recurso extraordinario de revisión"]),
  fichab("Plazos de interposición y de resolución de la alzada",
         "El interesado (interpone); el superior jerárquico (resuelve)",
         ["Pasado el mes sin recurrir un acto expreso, la resolución es **firme a todos los efectos**", "Contra la resolución de la alzada: **ningún otro recurso administrativo**, salvo el **extraordinario de revisión** (122.3)"],
         ["Interposición: **un mes** (acto expreso); acto no expreso: **en cualquier momento** desde el día siguiente a que se produzcan los efectos del silencio", "Resolución: **tres meses**; si no, se puede entender **desestimado**", f"Excepción (art. 24.1, tercer párrafo): alzada contra la desestimación por silencio de una solicitud → {c('L39', 'Artículo 24', 'se entenderá estimado el mismo si, llegado el plazo de resolución, el órgano administrativo competente no dictase y notificase resolución expresa')}"],
         "Alzada: **1 mes** para interponer y **3 meses** para resolver. El silencio en la alzada es **desestimatorio**, salvo la alzada contra una desestimación **por silencio** de una solicitud, que se entiende **estimada** (fuera de las materias del art. 24.1, segundo párrafo)."))}
""", 2)

T.ap("s16", "V.4 Recurso potestativo de reposición (arts. 123 y 124)", f"""
{unidad("4.1 Objeto y naturaleza (art. 123)",
  lit("L39", "Artículo 123", ["Los actos administrativos que pongan fin a la vía administrativa", "potestativamente en reposición ante el mismo órgano que los hubiera dictado", "impugnados directamente ante el orden jurisdiccional contencioso-administrativo", "No se podrá interponer recurso contencioso-administrativo hasta que sea resuelto expresamente"]),
  fichab("Recurso potestativo ante el mismo órgano contra actos que ponen fin a la vía administrativa",
         "Se interpone y se resuelve ante **el mismo órgano** que dictó el acto",
         ["Objeto: actos que **ponen fin** a la vía administrativa (→ V.1.3)", "Es **potestativo**: el interesado puede ir **directamente** al contencioso-administrativo", "Si se interpone, no cabe contencioso hasta su resolución **expresa** o su **desestimación presunta** (123.2)"],
         "—",
         "Alzada: actos que **no** ponen fin a la vía, ante el **superior**. Reposición: actos que **sí** la ponen, ante el **mismo** órgano, y es **potestativo**."))}

{unidad("4.2 Plazos (art. 124)",
  lit("L39", "Artículo 124", ["será de un mes, si el acto fuera expreso", "únicamente podrá interponerse recurso contencioso-administrativo", "se produzca el acto presunto", "El plazo máximo para dictar y notificar la resolución del recurso será de un mes", "no podrá interponerse de nuevo dicho recurso"]),
  fichab("Plazos de interposición y de resolución de la reposición",
         "El interesado (interpone); el mismo órgano (resuelve)",
         ["Pasado el mes sin recurrir un acto expreso: solo cabe el **contencioso-administrativo** (y, en su caso, el extraordinario de revisión)", "Contra la resolución de la reposición **no** cabe una nueva reposición (124.3)"],
         ["Interposición: **un mes** (acto expreso); acto no expreso: **en cualquier momento** desde el día siguiente a que se produzca el acto presunto", f"Resolución: {c('L39', 'Artículo 124', 'El plazo máximo para dictar y notificar la resolución del recurso será de un mes')}"],
         "Reposición: **1 mes** para interponer y **1 mes** para resolver (la alzada: 1 y **3**)."))}
""", 2)

T.ap("s17", "V.5 Recurso extraordinario de revisión (arts. 125 y 126)", f"""
{unidad("5.1 Objeto, causas y plazos (art. 125)",
  lit("L39", "Artículo 125", ["Contra los actos firmes en vía administrativa", "ante el órgano administrativo que los dictó, que también será el competente para su resolución", "error de hecho, que resulte de los propios documentos incorporados al expediente", "documentos de valor esencial", "declarados falsos por sentencia judicial firme", "prevaricación, cohecho, violencia, maquinación fraudulenta u otra conducta punible", "dentro del plazo de cuatro años siguientes a la fecha de la notificación de la resolución impugnada", "el plazo será de tres meses", "no perjudica el derecho de los interesados"]),
  fichab("Recurso extraordinario contra actos firmes, por causas tasadas",
         "Ante el **órgano que dictó** el acto, que también lo **resuelve**",
         ["::Causas (125.1):", "a) **Error de hecho** que resulte de los propios documentos del expediente", "b) Aparición de **documentos de valor esencial**, aunque sean posteriores, que evidencien el error", "c) Documentos o testimonios **declarados falsos** por sentencia judicial firme", "d) Prevaricación, cohecho, violencia, maquinación fraudulenta u otra conducta punible **declarada por sentencia judicial firme**", "No perjudica la solicitud de revisión de oficio (art. 106) ni la de rectificación de errores (art. 109.2) (125.3)"],
         ["Causa a): **cuatro años** desde la **notificación** de la resolución impugnada", "Causas b), c) y d): **tres meses** desde el conocimiento de los documentos o desde que la sentencia quedó firme"],
         "Solo la causa a) (error de hecho) tiene **cuatro años**; las demás, **tres meses**. Lo resuelve el **mismo órgano** que dictó el acto (no el superior)."))}

{unidad("5.2 Resolución (art. 126)",
  lit("L39", "Artículo 126", ["inadmisión a trámite, sin necesidad de recabar dictamen del Consejo de Estado", "no sólo sobre la procedencia del recurso, sino también, en su caso, sobre el fondo", "Transcurrido el plazo de tres meses desde la interposición"]),
  fichab("Cómo y en qué plazo se resuelve el recurso extraordinario de revisión",
         "El órgano competente para resolverlo",
         ["Inadmisión motivada **sin dictamen** del Consejo de Estado si no se funda en causas del 125.1 o hay otros recursos sustancialmente iguales desestimados en cuanto al fondo (126.1)", "Se pronuncia sobre la **procedencia** del recurso y, en su caso, sobre el **fondo** (126.2)"],
         f"{c('L39', 'Artículo 126', 'Transcurrido el plazo de tres meses desde la interposición del recurso extraordinario de revisión sin haberse dictado y notificado la resolución, se entenderá desestimado')}",
         "**Tres meses** desde la interposición sin resolución = **desestimado**, y queda expedita la vía contencioso-administrativa."))}
""", 2)

T.ap("s18", "V.6 Cuadro comparativo de los tres recursos (esquema)", f"""
{ESQ}

| | Alzada | Potestativo de reposición | Extraordinario de revisión |
|---|---|---|---|
| Artículos | 121 y 122 | 123 y 124 | 113, 125 y 126 |
| Contra qué | Actos del 112.1 que **no** ponen fin a la vía administrativa | Actos que **ponen fin** a la vía administrativa | Actos **firmes** en vía administrativa |
| Ante quién se interpone | El órgano que dictó el acto o el competente para resolver | El **mismo** órgano | El órgano que **dictó** el acto |
| Quién resuelve | El **superior jerárquico** | El **mismo** órgano | El **mismo** órgano |
| Plazo para interponer | **1 mes** (expreso); acto no expreso, en cualquier momento | **1 mes** (expreso); acto no expreso, en cualquier momento | **4 años** (error de hecho); **3 meses** (demás causas) |
| Plazo para resolver | **3 meses** | **1 mes** | **3 meses** |
| Silencio | Desestimatorio (salvo art. 24.1, tercer párrafo) | Desestimación presunta (123.2) | Desestimatorio (126.3) |
| Después | Ningún otro recurso administrativo, salvo el extraordinario de revisión (122.3); vía contencioso-administrativa | No cabe nueva reposición (124.3) | Vía contencioso-administrativa |

{resumen([
  "Se recurren las **resoluciones** y los actos de trámite **cualificados**; motivos: los de los arts. **47 y 48**; contra **disposiciones generales**, no hay recurso administrativo (112).",
  "Ponen fin a la vía, entre otros: resoluciones de **alzada**, órganos **sin superior jerárquico**, **responsabilidad patrimonial**; en el Estado, **Ministros y Secretarios de Estado** y **Director general** solo en **personal** (114).",
  "El recurso **no suspende** el acto; suspensión por perjuicios de imposible o difícil reparación o nulidad de pleno derecho; **un mes** sin resolver la solicitud = suspendido (117). Nunca puede **agravarse** la situación del recurrente (119.3).",
  "Alzada: ante el **superior**; **1 mes** / **3 meses**; si se presenta ante el autor del acto, lo **remite en 10 días** (121 y 122). Reposición: **mismo órgano**, potestativa, **1 mes** / **1 mes** (123 y 124). Revisión: actos **firmes**, causas tasadas, **4 años** o **3 meses**; **3 meses** para resolver (125 y 126)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX = [
 ("P", 75, "Derechos del interesado: conocer el estado de la tramitación (→ II.3.1)", {
   "a": f"Invierte el derecho: el interesado tiene derecho {c('L39', 'Artículo 53', 'A no presentar documentos originales salvo que, de manera excepcional, la normativa reguladora aplicable establezca lo contrario')} (art. 53.1 c); no hay un derecho a exigir que la Administración aporte originales.",
   "b": f"Literal del art. 53.1 a): {c('L39', 'Artículo 53', 'A conocer, en cualquier momento, el estado de la tramitación de los procedimientos en los que tengan la condición de interesados')}.",
   "c": f"Cambia el momento: se aportan documentos {c('L39', 'Artículo 53', 'en cualquier fase del procedimiento anterior al trámite de audiencia')} (art. 53.1 e), no una vez finalizado.",
   "d": f"Cambia el objeto: el derecho de identificación se refiere {c('L39', 'Artículo 53', 'a las autoridades y al personal al servicio de las Administraciones Públicas')} (art. 53.1 b), no al resto de interesados."},
   [("Conocer, en cualquier momento, el estado de la tramitación", "L39", "Artículo 53", "A conocer, en cualquier momento, el estado de la tramitación de los procedimientos")]),
 ("X", 64, "Derechos del interesado: identificar a autoridades y personal (→ II.3.1)", {
   "a": "El art. 53.1 no reconoce un derecho al «cambio» de las autoridades o del personal. Apartarlos solo cabe por recusación, en los casos de abstención (Ley 40/2015, art. 24 → III.2.2).",
   "b": f"Literal del art. 53.1 b): {c('L39', 'Artículo 53', 'A identificar a las autoridades y al personal al servicio de las Administraciones Públicas bajo cuya responsabilidad se tramiten los procedimientos')}.",
   "c": "El art. 53.1 no recoge un derecho a la «comunicación directa» con las autoridades y el personal.",
   "d": f"El art. 53.1 a) da derecho {c('L39', 'Artículo 53', 'A conocer, en cualquier momento, el estado de la tramitación')}, no a recibir un «informe escrito» de las autoridades o del personal."},
   [("identificación", "L39", "Artículo 53", "A identificar a las autoridades y al personal")]),
 ("P", 74, "Fin de la vía administrativa: el Director general, solo en materia de personal (→ V.1.3)", {
   "a": f"Cambia el ámbito: los órganos con nivel de Director general o superior ponen fin a la vía {c('L39', 'Artículo 114', 'en relación con las competencias que tengan atribuidas en materia de personal')} (art. 114.2 c), no en todo el ámbito de su Dirección General. Por eso **no** pone fin a la vía y es la respuesta.",
   "b": f"Sí pone fin: {c('L39', 'Artículo 114', 'Los acuerdos, pactos, convenios o contratos que tengan la consideración de finalizadores del procedimiento')} (art. 114.1 d).",
   "c": f"Sí pone fin: {c('L39', 'Artículo 114', 'Los emanados de los Ministros y los Secretarios de Estado en el ejercicio de las competencias que tienen atribuidas los órganos de los que son titulares')} (art. 114.2 b).",
   "d": f"Sí pone fin: {c('L39', 'Artículo 114', 'Las resoluciones de los órganos administrativos que carezcan de superior jerárquico, salvo que una Ley establezca lo contrario')} (art. 114.1 c)."},
   [("Director General", "L39", "Artículo 114", "Los emanados de los órganos directivos con nivel de Director general o superior, en relación con las competencias que tengan atribuidas en materia de personal")]),
 ("L", 59, "Alzada presentada ante el autor del acto: remisión en diez días (→ V.3.1)", {
   "a": f"Cambia el órgano y la actuación: el autor del acto no resuelve la alzada, que resuelve {c('L39', 'Artículo 121', 'el órgano superior jerárquico del que los dictó')} (art. 121.1); solo debe remitirla.",
   "b": "Cambia el verbo y el plazo: «**deberá**» (no «podrá») y en **diez** días (no quince).",
   "c": f"Literal del art. 121.2, párrafo segundo: {c('L39', 'Artículo 121', 'éste deberá remitirlo al competente en el plazo de diez días, con su informe y con una copia completa y ordenada del expediente')}.",
   "d": "Cambia el órgano, la actuación y el plazo: ni resuelve el autor del acto ni hay un plazo de quince días; el plazo para resolver la alzada es de tres meses (art. 122.2)."},
   [("deberá remitirlo al competente en el plazo de diez días", "L39", "Artículo 121", "deberá remitirlo al competente en el plazo de diez días")]),
 ("L", 16, "Lesividad en el municipio: el Pleno (relacionada; → IV.2.2)", {
   "a": f"La Junta de Gobierno Local no existe en todos: {c('LRBRL', 'Artículo 20', 'La Junta de Gobierno Local existe en todos los municipios con población superior a 5.000 habitantes y en los de menos, cuando así lo disponga su reglamento orgánico o así lo acuerde el Pleno de su ayuntamiento')} (Ley 7/1985, art. 20.1 b).",
   "b": f"Cambia quién los designa: los Tenientes de Alcalde son {c('LRBRL', 'Artículo 23', 'libremente designados y removidos por éste de entre los miembros de la Junta de Gobierno Local')} (por el Alcalde; art. 23.3), no por los miembros del Pleno.",
   "c": f"El control y la fiscalización de los órganos de gobierno corresponden al Pleno: {c('LRBRL', 'Artículo 22', 'El control y la fiscalización de los órganos de gobierno')} (art. 22.2 a), no al Alcalde.",
   "d": f"Literal del art. 22.2 k) de la Ley 7/1985, entre las atribuciones del Pleno y de la Asamblea vecinal: {c('LRBRL', 'Artículo 22', 'La declaración de lesividad de los actos del Ayuntamiento')}. Concuerda con el art. 107.5 de la Ley 39/2015."},
   [("declaración de lesividad de los actos del Ayuntamiento", "LRBRL", "Artículo 22", "La declaración de lesividad de los actos del Ayuntamiento"),
    ("Asamblea vecinal en el régimen de Concejo Abierto", "LRBRL", "Artículo 22", "al Pleno municipal en los Ayuntamientos, y a la Asamblea vecinal en el régimen de Concejo Abierto")]),
]
NOMBRE = {"L": "GACE-L", "P": "GACE-P", "X": "GACE-L extraordinario"}
bloques = []
for cod, n, tit, por, ap_ in EX:
    bloques += [f"### {NOMBRE[cod]} 2025, pregunta {n} · {tit}", examen(cod, n, por, ap_)]
T.ap("s19", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join(
  ["En los primeros ejercicios de **2025** cayeron **cuatro** preguntas de este tema (dos sobre los derechos del interesado del art. 53, una sobre el fin de la vía administrativa y una sobre el recurso de alzada) y **una** relacionada, de régimen local, sobre la declaración de lesividad. Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal."]
  + bloques + ["### Cómo se pregunta", "!> Las preguntas citan el **artículo** y cambian **un plazo** (diez o quince días), **un verbo** («deberá» o «podrá»; «remitir» o «resolver»), **un ámbito** («en materia de personal») o **invierten un derecho** (no presentar originales frente a exigir que se aporten). La letra de los arts. 53, 114 y 121 resuelve las cuatro."]))

T.ap("s20", "Cierre 2. Repaso en 10 minutos (por bloques)", """
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Quién actúa | Capacidad de obrar (3); interesados (4); representación (5); firma (11) | Representación **acreditada** para recursos; **10 días** para subsanar |
| II. Derechos | Art. 13 (personas); art. 14 (relación electrónica); art. 53.1 (interesados) | **Conocer en cualquier momento** el estado de la tramitación; **identificar** al personal |
| III. Garantías | Presunto responsable (53.2); abstención y recusación (Ley 40/2015, arts. 23 y 24) | Recusación: **día siguiente** y **tres días**; sin recurso |
| IV. Revisión de oficio | Nulidad (106), lesividad (107), revocación y rectificación (109), límites (110), competencia (111) | Dictamen **favorable**; lesividad en **4 años**; **6 meses** o caducidad |
| V. Recursos | Principios (112 a 120); alzada (121-122); reposición (123-124); revisión (125-126) | Alzada: remitir en **10 días**; **1 mes / 3 meses**; Director general: solo **personal** |

?> **Trampas frecuentes:** «aportar documentos **después** del trámite de audiencia» (es **antes**); «el autor del acto **podrá** remitir la alzada en **quince** días» (es **deberá** y **diez**); «el Director general pone fin a la vía en **todas** sus competencias» (solo en **personal**); «lesividad en **cuatro años desde la notificación**» (es desde que **se dictó**); «revisión de nulidad con dictamen **preceptivo**» (tiene que ser **favorable**); «la reposición se resuelve en **tres meses**» (es **un mes**); «la interposición del recurso **suspende** el acto» (regla: **no** lo suspende).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
L = "Según el artículo"
Q = [
 ("L39", "Artículo 3", "Interesados", f"{L} 3 de la Ley 39/2015, los grupos de afectados, las uniones y entidades sin personalidad jurídica y los patrimonios independientes o autónomos tienen capacidad de obrar ante las Administraciones Públicas:",
  ["Cuando la Ley así lo declare expresamente.", "En todo caso.", "Cuando lo autorice el órgano competente para resolver.", "Solo si actúan mediante representante acreditado."], "Art. 3 c) Ley 39/2015.", "Cuando la Ley así lo declare expresamente, los grupos de afectados"),
 ("L39", "Artículo 4", "Interesados", f"{L} 4.1 c) de la Ley 39/2015, son interesados aquellos cuyos intereses legítimos puedan resultar afectados por la resolución y se personen en el procedimiento:",
  ["En tanto no haya recaído resolución definitiva.", "Antes del trámite de audiencia.", "Dentro de los diez días siguientes a su iniciación.", "En cualquier momento, incluso después de la resolución."], "Art. 4.1 c) Ley 39/2015.", "se personen en el procedimiento en tanto no haya recaído resolución definitiva"),
 ("L39", "Artículo 4", "Interesados", f"{L} 4.3 de la Ley 39/2015, cuando la condición de interesado derivase de alguna relación jurídica transmisible, el derecho-habiente sucederá en tal condición:",
  ["Cualquiera que sea el estado del procedimiento.", "Solo antes del trámite de audiencia.", "Solo si lo autoriza el órgano instructor.", "Solo si no ha recaído propuesta de resolución."], "Art. 4.3 Ley 39/2015.", "el derecho-habiente sucederá en tal condición cualquiera que sea el estado del procedimiento"),
 ("L39", "Artículo 5", "Interesados", f"{L} 5.3 de la Ley 39/2015, ¿para cuál de las siguientes actuaciones en nombre de otra persona deberá acreditarse la representación?",
  ["Interponer recursos.", "Solicitar una copia de un documento del expediente como acto de mero trámite.", "Cualquier gestión de mero trámite.", "Consultar el estado de la tramitación como gestión de mero trámite."], "Art. 5.3 Ley 39/2015: hay que acreditarla para solicitudes, declaraciones responsables o comunicaciones, recursos, desistimiento y renuncia; para el mero trámite se presume.", "interponer recursos, desistir de acciones y renunciar a derechos en nombre de otra persona, deberá acreditarse la representación"),
 ("L39", "Artículo 5", "Interesados", f"{L} 5.6 de la Ley 39/2015, la falta o insuficiente acreditación de la representación no impedirá que se tenga por realizado el acto, siempre que se subsane el defecto dentro del plazo que deberá conceder el órgano administrativo de:",
  ["Diez días, o un plazo superior cuando las circunstancias del caso así lo requieran.", "Cinco días, improrrogables.", "Quince días, o un plazo superior cuando las circunstancias del caso así lo requieran.", "Un mes."], "Art. 5.6 Ley 39/2015.", "dentro del plazo de diez días que deberá conceder al efecto el órgano administrativo"),
 ("L39", "Artículo 7", "Interesados", f"{L} 7 de la Ley 39/2015, cuando en una solicitud figuren varios interesados y no hayan señalado expresamente representante o interesado, las actuaciones se efectuarán:",
  ["Con el que figure en primer término.", "Con todos ellos por separado.", "Con el de mayor edad.", "Con el que designe el órgano instructor."], "Art. 7 Ley 39/2015.", "en su defecto, con el que figure en primer término"),
 ("L39", "Artículo 11", "Interesados", f"{L} 11.2 de la Ley 39/2015, las Administraciones Públicas solo requerirán a los interesados el uso obligatorio de firma para, entre otros:",
  ["Interponer recursos.", "Consultar el estado de la tramitación.", "Aportar documentos durante la instrucción.", "Identificarse ante la Administración."], "Art. 11.2 Ley 39/2015: solicitudes, declaraciones responsables o comunicaciones, recursos, desistimiento y renuncia.", "Interponer recursos"),
 ("L39", "Artículo 13", "Derechos", f"{L} 13 de la Ley 39/2015, son titulares de los derechos de las personas en sus relaciones con las Administraciones Públicas:",
  ["Quienes, de conformidad con el artículo 3, tienen capacidad de obrar ante las Administraciones Públicas.", "Solo los interesados en un procedimiento administrativo.", "Solo los ciudadanos españoles mayores de edad.", "Solo las personas físicas."], "Art. 13 Ley 39/2015.", "Quienes de conformidad con el artículo 3, tienen capacidad de obrar ante las Administraciones Públicas, son titulares"),
 ("L39", "Artículo 13", "Derechos", f"{L} 13 de la Ley 39/2015, ¿cuál de los siguientes es un derecho de las personas en sus relaciones con las Administraciones Públicas?",
  ["A ser tratados con respeto y deferencia por las autoridades y empleados públicos.", "A elegir el órgano que debe resolver su solicitud.", "A que no se les exija nunca el uso de medios electrónicos.", "A la suspensión automática de los actos que recurran."], "Art. 13 e) Ley 39/2015.", "A ser tratados con respeto y deferencia por las autoridades y empleados públicos"),
 ("L39", "Artículo 13", "Derechos", f"{L} 13 c) de la Ley 39/2015, las personas tienen derecho a utilizar las lenguas oficiales:",
  ["En el territorio de su Comunidad Autónoma, de acuerdo con lo previsto en esta Ley y en el resto del ordenamiento jurídico.", "En todo el territorio nacional, ante cualquier Administración.", "Solo ante la Administración General del Estado.", "Solo en los procedimientos iniciados a solicitud del interesado."], "Art. 13 c) Ley 39/2015.", "A utilizar las lenguas oficiales en el territorio de su Comunidad Autónoma"),
 ("L39", "Artículo 14", "Derechos", f"{L} 14.2 de la Ley 39/2015, ¿cuál de los siguientes sujetos está obligado a relacionarse a través de medios electrónicos con las Administraciones Públicas?",
  ["Las entidades sin personalidad jurídica.", "Las personas físicas mayores de edad.", "Los menores de edad con capacidad de obrar.", "Los pensionistas."], "Art. 14.2 b) Ley 39/2015.", "Las entidades sin personalidad jurídica"),
 ("L39", "Artículo 14", "Derechos", f"{L} 14.1 de la Ley 39/2015, las personas físicas no obligadas podrán elegir si se comunican con las Administraciones Públicas a través de medios electrónicos o no:",
  ["En todo momento, y podrán modificar el medio elegido en cualquier momento.", "Solo al iniciar el procedimiento, sin posibilidad de cambio.", "Solo una vez al año.", "Solo con autorización del órgano instructor."], "Art. 14.1 Ley 39/2015.", "podrán elegir en todo momento si se comunican"),
 ("L39", "Artículo 53", "Derechos", f"{L} 53.1 e) de la Ley 39/2015, los interesados tienen derecho a formular alegaciones y aportar documentos:",
  ["En cualquier fase del procedimiento anterior al trámite de audiencia.", "En cualquier fase del procedimiento, incluso después del trámite de audiencia.", "Solo en el plazo de diez días desde la iniciación.", "Solo en el trámite de audiencia."], "Art. 53.1 e) Ley 39/2015.", "en cualquier fase del procedimiento anterior al trámite de audiencia"),
 ("L39", "Artículo 53", "Derechos", f"{L} 53.1 c) de la Ley 39/2015, los interesados tienen derecho:",
  ["A no presentar documentos originales salvo que, de manera excepcional, la normativa reguladora aplicable establezca lo contrario.", "A presentar siempre documentos originales en lugar de copias.", "A exigir que la Administración les devuelva los documentos originales en el plazo de diez días.", "A no presentar documentos de ningún tipo en el procedimiento."], "Art. 53.1 c) Ley 39/2015.", "A no presentar documentos originales salvo que, de manera excepcional"),
 ("L39", "Artículo 53", "Derechos", f"{L} 53.1 g) de la Ley 39/2015, los interesados tienen derecho a actuar asistidos de asesor:",
  ["Cuando lo consideren conveniente en defensa de sus intereses.", "Solo en los procedimientos sancionadores.", "Solo si lo autoriza el órgano instructor.", "Solo en la fase de recurso."], "Art. 53.1 g) Ley 39/2015.", "A actuar asistidos de asesor cuando lo consideren conveniente en defensa de sus intereses"),
 ("L39", "Artículo 53", "Garantías", f"{L} 53.2 b) de la Ley 39/2015, en los procedimientos de naturaleza sancionadora los presuntos responsables tienen derecho:",
  ["A la presunción de no existencia de responsabilidad administrativa mientras no se demuestre lo contrario.", "A la suspensión automática del procedimiento si recusan al instructor.", "A que la sanción no se ejecute hasta que sea firme en vía judicial.", "A no ser notificados de la identidad del instructor."], "Art. 53.2 b) Ley 39/2015.", "A la presunción de no existencia de responsabilidad administrativa mientras no se demuestre lo contrario"),
 ("L40", "Artículo 23", "Garantías", f"{L} 23.2 b) de la Ley 40/2015, es motivo de abstención el parentesco con cualquiera de los interesados:",
  ["De consanguinidad dentro del cuarto grado o de afinidad dentro del segundo.", "De consanguinidad dentro del segundo grado o de afinidad dentro del cuarto.", "De consanguinidad o afinidad dentro del tercer grado.", "De consanguinidad dentro del cuarto grado, sin incluir la afinidad."], "Art. 23.2 b) Ley 40/2015.", "consanguinidad dentro del cuarto grado o de afinidad dentro del segundo"),
 ("L40", "Artículo 23", "Garantías", f"{L} 23.2 e) de la Ley 40/2015, es motivo de abstención haber prestado servicios profesionales a la persona interesada directamente en el asunto:",
  ["En los dos últimos años.", "En los cinco últimos años.", "En el último año.", "En cualquier momento anterior."], "Art. 23.2 e) Ley 40/2015.", "haberle prestado en los dos últimos años servicios profesionales"),
 ("L40", "Artículo 23", "Garantías", f"{L} 23.4 de la Ley 40/2015, la actuación de autoridades y personal en los que concurran motivos de abstención:",
  ["No implicará, necesariamente, y en todo caso, la invalidez de los actos en que hayan intervenido.", "Determinará en todo caso la nulidad de pleno derecho de los actos.", "Determinará en todo caso la anulabilidad de los actos.", "Obligará a retrotraer siempre el procedimiento a su inicio."], "Art. 23.4 Ley 40/2015.", "no implicará, necesariamente, y en todo caso, la invalidez de los actos"),
 ("L40", "Artículo 24", "Garantías", f"{L} 24.4 de la Ley 40/2015, si el recusado niega la causa de recusación, el superior resolverá en el plazo de:",
  ["Tres días.", "Diez días.", "Un día.", "Quince días."], "Art. 24.4 Ley 40/2015.", "el superior resolverá en el plazo de tres días"),
 ("L40", "Artículo 24", "Garantías", f"{L} 24.5 de la Ley 40/2015, contra las resoluciones adoptadas en materia de recusación:",
  ["No cabrá recurso, sin perjuicio de alegar la recusación al interponer el recurso que proceda contra el acto que ponga fin al procedimiento.", "Cabe recurso de alzada en el plazo de un mes.", "Cabe recurso potestativo de reposición.", "Cabe recurso extraordinario de revisión."], "Art. 24.5 Ley 40/2015.", "Contra las resoluciones adoptadas en esta materia no cabrá recurso"),
 ("L39", "Artículo 106", "Revisión de oficio", f"{L} 106.1 de la Ley 39/2015, la declaración de oficio de la nulidad de los actos administrativos requiere:",
  ["Dictamen favorable del Consejo de Estado u órgano consultivo equivalente de la Comunidad Autónoma, si lo hubiere.", "Informe preceptivo, aunque no vinculante, del Consejo de Estado.", "Autorización previa del Consejo de Ministros.", "Sentencia firme del orden contencioso-administrativo."], "Art. 106.1 Ley 39/2015: dictamen **favorable**.", "previo dictamen favorable del Consejo de Estado u órgano consultivo equivalente de la Comunidad Autónoma"),
 ("L39", "Artículo 106", "Revisión de oficio", f"{L} 106.5 de la Ley 39/2015, si el procedimiento de revisión de oficio se hubiera iniciado de oficio, el transcurso sin dictarse resolución del plazo de:",
  ["Seis meses desde su inicio producirá la caducidad del mismo.", "Tres meses desde su inicio producirá la caducidad del mismo.", "Seis meses desde su inicio permitirá entenderlo estimado.", "Un año desde su inicio producirá la caducidad del mismo."], "Art. 106.5 Ley 39/2015.", "el transcurso del plazo de seis meses desde su inicio sin dictarse resolución producirá la caducidad del mismo"),
 ("L39", "Artículo 106", "Revisión de oficio", f"{L} 106.2 de la Ley 39/2015, la declaración de nulidad de las disposiciones administrativas puede acordarse:",
  ["De oficio, en cualquier momento, previo dictamen favorable del Consejo de Estado u órgano consultivo equivalente.", "Solo a solicitud de interesado, en el plazo de cuatro años.", "De oficio, en el plazo de un año desde su publicación.", "A solicitud de interesado, sin necesidad de dictamen."], "Art. 106.2 Ley 39/2015.", "en cualquier momento, las Administraciones Públicas de oficio"),
 ("L39", "Artículo 107", "Revisión de oficio", f"{L} 107.2 de la Ley 39/2015, la declaración de lesividad no podrá adoptarse una vez transcurridos:",
  ["Cuatro años desde que se dictó el acto administrativo.", "Cuatro años desde la notificación del acto administrativo.", "Seis meses desde que se dictó el acto administrativo.", "Dos años desde que se dictó el acto administrativo."], "Art. 107.2 Ley 39/2015.", "no podrá adoptarse una vez transcurridos cuatro años desde que se dictó el acto administrativo"),
 ("L39", "Artículo 107", "Revisión de oficio", f"{L} 107.5 de la Ley 39/2015, si el acto proviniera de las entidades que integran la Administración Local, la declaración de lesividad se adoptará por:",
  ["El Pleno de la Corporación o, en defecto de éste, por el órgano colegiado superior de la entidad.", "El Alcalde o Presidente de la entidad.", "La Junta de Gobierno Local.", "El Delegado del Gobierno en la Comunidad Autónoma."], "Art. 107.5 Ley 39/2015.", "se adoptará por el Pleno de la Corporación"),
 ("L39", "Artículo 107", "Revisión de oficio", f"{L} 107.1 de la Ley 39/2015, la declaración de lesividad permite a las Administraciones Públicas:",
  ["Impugnar ante el orden jurisdiccional contencioso-administrativo los actos favorables para los interesados que sean anulables.", "Anular por sí mismas los actos favorables para los interesados que sean anulables.", "Revocar los actos de gravamen o desfavorables.", "Declarar de oficio la nulidad de las disposiciones administrativas."], "Art. 107.1 Ley 39/2015.", "podrán impugnar ante el orden jurisdiccional contencioso-administrativo los actos favorables para los interesados que sean anulables"),
 ("L39", "Artículo 109", "Revisión de oficio", f"{L} 109.1 de la Ley 39/2015, las Administraciones Públicas podrán revocar, mientras no haya transcurrido el plazo de prescripción:",
  ["Sus actos de gravamen o desfavorables.", "Sus actos favorables para los interesados.", "Sus disposiciones de carácter general.", "Cualquier acto, sin limitación alguna."], "Art. 109.1 Ley 39/2015.", "sus actos de gravamen o desfavorables"),
 ("L39", "Artículo 109", "Revisión de oficio", f"{L} 109.2 de la Ley 39/2015, las Administraciones Públicas podrán rectificar los errores materiales, de hecho o aritméticos existentes en sus actos:",
  ["En cualquier momento, de oficio o a instancia de los interesados.", "En el plazo de cuatro años, solo de oficio.", "En el plazo de un mes desde la notificación.", "Solo a instancia de los interesados, en el plazo de tres meses."], "Art. 109.2 Ley 39/2015.", "rectificar en cualquier momento, de oficio o a instancia de los interesados"),
 ("L39", "Artículo 111", "Revisión de oficio", f"{L} 111 de la Ley 39/2015, en el ámbito estatal, es competente para la revisión de oficio de los actos dictados por los Ministros:",
  ["El Consejo de Ministros.", "El propio Ministro.", "El Secretario de Estado correspondiente.", "El Consejo de Estado."], "Art. 111 a) Ley 39/2015.", "El Consejo de Ministros, respecto de sus propios actos y disposiciones y de los actos y disposiciones dictados por los Ministros"),
 ("L39", "Artículo 112", "Recursos", f"{L} 112.3 de la Ley 39/2015, contra las disposiciones administrativas de carácter general:",
  ["No cabrá recurso en vía administrativa.", "Cabe recurso de alzada ante el superior jerárquico.", "Cabe recurso potestativo de reposición en el plazo de un mes.", "Cabe recurso extraordinario de revisión en el plazo de cuatro años."], "Art. 112.3 Ley 39/2015.", "Contra las disposiciones administrativas de carácter general no cabrá recurso en vía administrativa"),
 ("L39", "Artículo 114", "Recursos", f"{L} 114.1 de la Ley 39/2015, ponen fin a la vía administrativa:",
  ["Las resoluciones de los recursos de alzada.", "Las resoluciones de los órganos que tengan superior jerárquico.", "Los actos de trámite que no decidan el fondo del asunto.", "Las propuestas de resolución."], "Art. 114.1 a) Ley 39/2015.", "Las resoluciones de los recursos de alzada"),
 ("L39", "Artículo 117", "Recursos", f"{L} 117.1 de la Ley 39/2015, la interposición de cualquier recurso, excepto en los casos en que una disposición establezca lo contrario:",
  ["No suspenderá la ejecución del acto impugnado.", "Suspenderá automáticamente la ejecución del acto impugnado.", "Suspenderá la ejecución si el recurrente presta caución.", "Suspenderá la ejecución durante un mes."], "Art. 117.1 Ley 39/2015.", "no suspenderá la ejecución del acto impugnado"),
 ("L39", "Artículo 117", "Recursos", f"{L} 117.3 de la Ley 39/2015, la ejecución del acto impugnado se entenderá suspendida si, desde que la solicitud de suspensión haya tenido entrada en el registro electrónico del órgano competente, no se ha dictado y notificado resolución expresa al respecto en el plazo de:",
  ["Un mes.", "Quince días.", "Tres meses.", "Diez días."], "Art. 117.3 Ley 39/2015.", "transcurrido un mes desde que la solicitud de suspensión haya tenido entrada"),
 ("L39", "Artículo 118", "Recursos", f"{L} 118.1 de la Ley 39/2015, cuando hayan de tenerse en cuenta nuevos hechos o documentos no recogidos en el expediente originario, se pondrán de manifiesto a los interesados para que formulen alegaciones en un plazo:",
  ["No inferior a diez días ni superior a quince.", "No inferior a cinco días ni superior a diez.", "De un mes.", "No inferior a quince días ni superior a veinte."], "Art. 118.1 Ley 39/2015.", "en un plazo no inferior a diez días ni superior a quince"),
 ("L39", "Artículo 119", "Recursos", f"{L} 119.3 de la Ley 39/2015, la resolución del recurso será congruente con las peticiones formuladas por el recurrente:",
  ["Sin que en ningún caso pueda agravarse su situación inicial.", "Pudiendo agravarse su situación inicial si así lo exige el interés público.", "Pudiendo agravarse su situación inicial previa audiencia del recurrente.", "Sin que pueda pronunciarse sobre cuestiones no alegadas por los interesados."], "Art. 119.3 Ley 39/2015: el órgano decide también las cuestiones no alegadas (oyendo antes a los interesados), pero nunca puede agravar la situación del recurrente.", "sin que en ningún caso pueda agravarse su situación inicial"),
 ("L39", "Artículo 121", "Recursos", f"{L} 121.1 de la Ley 39/2015, las resoluciones y actos que no pongan fin a la vía administrativa podrán ser recurridos en alzada ante:",
  ["El órgano superior jerárquico del que los dictó.", "El mismo órgano que los dictó.", "El Consejo de Estado.", "El Defensor del Pueblo."], "Art. 121.1 Ley 39/2015.", "podrán ser recurridos en alzada ante el órgano superior jerárquico del que los dictó"),
 ("L39", "Artículo 122", "Recursos", f"{L} 122 de la Ley 39/2015, el plazo para interponer el recurso de alzada contra un acto expreso y el plazo máximo para dictar y notificar su resolución son, respectivamente:",
  ["Un mes y tres meses.", "Un mes y un mes.", "Tres meses y un mes.", "Dos meses y seis meses."], "Art. 122.1 y 2 Ley 39/2015.", ["será de un mes, si el acto fuera expreso", "El plazo máximo para dictar y notificar la resolución será de tres meses"]),
 ("L39", "Artículo 122", "Recursos", f"{L} 122.3 de la Ley 39/2015, contra la resolución de un recurso de alzada:",
  ["No cabrá ningún otro recurso administrativo, salvo el recurso extraordinario de revisión en los casos del artículo 125.1.", "Cabe recurso potestativo de reposición en el plazo de un mes.", "Cabe un nuevo recurso de alzada ante el Ministro.", "No cabe ningún recurso, ni administrativo ni judicial."], "Art. 122.3 Ley 39/2015.", "Contra la resolución de un recurso de alzada no cabrá ningún otro recurso administrativo, salvo el recurso extraordinario de revisión"),
 ("L39", "Artículo 123", "Recursos", f"{L} 123.1 de la Ley 39/2015, los actos administrativos que pongan fin a la vía administrativa podrán ser recurridos potestativamente en reposición ante:",
  ["El mismo órgano que los hubiera dictado.", "El órgano superior jerárquico del que los dictó.", "El Consejo de Ministros.", "El órgano consultivo de la Comunidad Autónoma."], "Art. 123.1 Ley 39/2015.", "potestativamente en reposición ante el mismo órgano que los hubiera dictado"),
 ("L39", "Artículo 124", "Recursos", f"{L} 124.2 de la Ley 39/2015, el plazo máximo para dictar y notificar la resolución del recurso de reposición será de:",
  ["Un mes.", "Tres meses.", "Quince días.", "Seis meses."], "Art. 124.2 Ley 39/2015.", "El plazo máximo para dictar y notificar la resolución del recurso será de un mes"),
 ("L39", "Artículo 125", "Recursos", f"{L} 125.2 de la Ley 39/2015, cuando el recurso extraordinario de revisión se funde en un error de hecho que resulte de los propios documentos incorporados al expediente, se interpondrá dentro del plazo de:",
  ["Cuatro años siguientes a la fecha de la notificación de la resolución impugnada.", "Tres meses desde la notificación de la resolución impugnada.", "Un mes desde la notificación de la resolución impugnada.", "Cuatro años desde que se dictó la resolución impugnada."], "Art. 125.2 Ley 39/2015.", "dentro del plazo de cuatro años siguientes a la fecha de la notificación de la resolución impugnada"),
 ("L39", "Artículo 125", "Recursos", f"{L} 125.1 de la Ley 39/2015, el recurso extraordinario de revisión se interpone:",
  ["Ante el órgano administrativo que dictó los actos, que también será el competente para su resolución.", "Ante el órgano superior jerárquico del que dictó los actos.", "Ante el Consejo de Estado.", "Ante el orden jurisdiccional contencioso-administrativo."], "Art. 125.1 Ley 39/2015.", "ante el órgano administrativo que los dictó, que también será el competente para su resolución"),
 ("L39", "Artículo 126", "Recursos", f"{L} 126.3 de la Ley 39/2015, transcurrido el plazo de tres meses desde la interposición del recurso extraordinario de revisión sin haberse dictado y notificado la resolución:",
  ["Se entenderá desestimado, quedando expedita la vía jurisdiccional contencioso-administrativa.", "Se entenderá estimado.", "Se producirá la caducidad del procedimiento.", "Se entenderá estimado si así lo informa el Consejo de Estado."], "Art. 126.3 Ley 39/2015.", "se entenderá desestimado, quedando expedita la vía jurisdiccional contencioso-administrativa"),
]
for k, art, cat, q_, ops, e, fr in Q: T.q(k, art, cat, q_, ops, e, fr)
T.real("P", 75, "Derechos"); T.real("X", 64, "Derechos"); T.real("P", 74, "Recursos"); T.real("L", 59, "Recursos")

# Flashcards
for q_, a_, cat in [
  ("¿Quién es interesado según el art. 4.1 de la Ley 39/2015?", "Quienes promueven el procedimiento; quienes, sin iniciarlo, tienen derechos que pueden resultar afectados; y quienes tienen intereses legítimos afectados y se personan mientras no haya resolución definitiva.", "Interesados"),
  ("¿Para qué actos hay que acreditar la representación? (art. 5.3)", "Formular solicitudes, presentar declaraciones responsables o comunicaciones, interponer recursos, desistir de acciones y renunciar a derechos. Para el mero trámite se presume.", "Interesados"),
  ("Plazo para subsanar la falta de acreditación de la representación (art. 5.6)", "Diez días (o superior si las circunstancias lo requieren).", "Interesados"),
  ("Varios interesados sin designación expresa: ¿con quién se entienden las actuaciones? (art. 7)", "Con el que figure en primer término.", "Interesados"),
  ("Titulares de los derechos del art. 13", "Quienes tienen capacidad de obrar ante las Administraciones Públicas según el art. 3.", "Derechos"),
  ("¿Quién está obligado a relacionarse electrónicamente? (art. 14.2)", "Personas jurídicas; entidades sin personalidad; profesionales de colegiación obligatoria en esa actividad; representantes de obligados; empleados públicos por razón de su condición.", "Derechos"),
  ("Art. 53.1 a): ¿qué puede conocer el interesado?", "En cualquier momento, el estado de la tramitación, el sentido del silencio, el órgano competente para instruir y resolver y los actos de trámite; y acceder y obtener copia de los documentos.", "Derechos"),
  ("¿Hasta cuándo se pueden aportar documentos? (art. 53.1 e)", "En cualquier fase del procedimiento anterior al trámite de audiencia.", "Derechos"),
  ("Derechos del presunto responsable (art. 53.2)", "Ser notificado de hechos, infracciones, sanciones, identidad del instructor, autoridad competente y norma atributiva; presunción de no existencia de responsabilidad.", "Garantías"),
  ("Parentesco que obliga a abstenerse (Ley 40/2015, art. 23.2 b)", "Consanguinidad dentro del cuarto grado o afinidad dentro del segundo (y vínculo matrimonial o situación de hecho asimilable).", "Garantías"),
  ("Plazos de la recusación (Ley 40/2015, art. 24)", "El recusado manifiesta al día siguiente si concurre la causa; si la niega, el superior resuelve en tres días. Sin recurso autónomo.", "Garantías"),
  ("Revisión de oficio de actos nulos (art. 106.1): requisitos", "En cualquier momento, de oficio o a solicitud de interesado, dictamen favorable del Consejo de Estado u órgano equivalente; actos que pusieron fin a la vía o no recurridos en plazo.", "Revisión de oficio"),
  ("Plazo para resolver la revisión de oficio (art. 106.5)", "Seis meses: si se inició de oficio, caducidad; si a solicitud de interesado, desestimación por silencio.", "Revisión de oficio"),
  ("Declaración de lesividad (art. 107)", "Actos favorables anulables; plazo de cuatro años desde que se dictó; audiencia; no recurrible; caducidad a los seis meses; después, impugnación ante el contencioso.", "Revisión de oficio"),
  ("¿Qué se revoca y qué se rectifica? (art. 109)", "Se revocan actos de gravamen o desfavorables mientras no prescriban; se rectifican en cualquier momento errores materiales, de hecho o aritméticos.", "Revisión de oficio"),
  ("¿Quién revisa de oficio los actos de los Ministros? (art. 111)", "El Consejo de Ministros.", "Revisión de oficio"),
  ("¿Cabe recurso administrativo contra un reglamento? (art. 112.3)", "No.", "Recursos"),
  ("¿Pone fin a la vía administrativa el Director general? (art. 114.2 c)", "Solo en relación con sus competencias en materia de personal.", "Recursos"),
  ("¿Suspende el recurso la ejecución del acto? (art. 117)", "No, salvo disposición en contrario; cabe suspensión por perjuicios de imposible o difícil reparación o nulidad de pleno derecho; un mes sin resolver la solicitud = suspendido.", "Recursos"),
  ("Alzada presentada ante el autor del acto (art. 121.2)", "Debe remitirla al competente en diez días, con su informe y copia completa y ordenada del expediente.", "Recursos"),
  ("Alzada: plazos (art. 122)", "Un mes para interponer (acto expreso); tres meses para resolver; después, ningún otro recurso administrativo salvo el extraordinario de revisión (122.3).", "Recursos"),
  ("Reposición: plazos (art. 124)", "Un mes para interponer (acto expreso) y un mes para resolver; no cabe nueva reposición.", "Recursos"),
  ("Extraordinario de revisión: plazos (arts. 125 y 126)", "Error de hecho: cuatro años desde la notificación; demás causas: tres meses; tres meses para resolver o desestimado.", "Recursos"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Interesado", "Quien promueve el procedimiento, quien tiene derechos que pueden resultar afectados o quien, con intereses legítimos afectados, se persona antes de la resolución definitiva (art. 4 Ley 39/2015).", "s1", "Interesados")
T.glos("Apoderamiento apud acta", "Forma de acreditar la representación por comparecencia personal o electrónica en la sede electrónica (art. 5.4 Ley 39/2015).", "s2", "Interesados")
T.glos("Punto de Acceso General electrónico", "Portal a través del cual las personas pueden comunicarse con la Administración (art. 13 a) y consultar el estado de sus procedimientos (art. 53.1 a).", "s3", "Derechos")
T.glos("Abstención", "Deber de autoridades y personal de no intervenir en el procedimiento cuando concurre alguno de los motivos del art. 23.2 de la Ley 40/2015, comunicándolo al superior inmediato.", "s8", "Garantías")
T.glos("Recusación", "Facultad de los interesados de pedir, en cualquier momento de la tramitación y por escrito, que se aparte a quien incurre en un motivo de abstención (art. 24 Ley 40/2015).", "s8", "Garantías")
T.glos("Revisión de oficio", "Declaración por la propia Administración de la nulidad de actos (art. 47.1) y disposiciones (art. 47.2), con dictamen favorable del Consejo de Estado u órgano equivalente (art. 106 Ley 39/2015).", "s9", "Revisión de oficio")
T.glos("Declaración de lesividad", "Declaración de que un acto favorable anulable es lesivo para el interés público, previa a su impugnación ante el orden contencioso-administrativo (art. 107 Ley 39/2015).", "s10", "Revisión de oficio")
T.glos("Revocación", "Supresión por la Administración de sus actos de gravamen o desfavorables mientras no haya prescrito, con los límites del art. 109.1 de la Ley 39/2015.", "s11", "Revisión de oficio")
T.glos("Rectificación de errores", "Corrección, en cualquier momento, de los errores materiales, de hecho o aritméticos de los actos (art. 109.2 Ley 39/2015).", "s11", "Revisión de oficio")
T.glos("Fin de la vía administrativa", "Situación del acto contra el que ya no cabe alzada: solo reposición potestativa o recurso contencioso-administrativo (arts. 114 y 123 Ley 39/2015).", "s13", "Recursos")
T.glos("Recurso de alzada", "Recurso ante el superior jerárquico contra actos que no ponen fin a la vía administrativa; un mes para interponer y tres para resolver (arts. 121 y 122 Ley 39/2015).", "s15", "Recursos")
T.glos("Recurso potestativo de reposición", "Recurso ante el mismo órgano contra actos que ponen fin a la vía administrativa; un mes para interponer y uno para resolver (arts. 123 y 124 Ley 39/2015).", "s16", "Recursos")
T.glos("Recurso extraordinario de revisión", "Recurso contra actos firmes en vía administrativa por las causas tasadas del art. 125.1 de la Ley 39/2015, ante el órgano que los dictó.", "s17", "Recursos")

# Cronología (fechas de los metadatos del BOE)
T.hito("1985", "Ley 7/1985, de 2 de abril, Reguladora de las Bases del Régimen Local (BOE de 3-4-1985)", "Art. 22.2 k): el Pleno declara la lesividad de los actos del Ayuntamiento", "normativo", "s10")
T.hito("2015", "Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas (BOE de 2-10-2015)", "Derechos de las personas e interesados (arts. 3 a 14 y 53); revisión de oficio y recursos (Título V, arts. 106 a 126)", "normativo", "s3")
T.hito("2015", "Ley 40/2015, de 1 de octubre, de Régimen Jurídico del Sector Público (BOE de 2-10-2015)", "Arts. 23 y 24: abstención y recusación", "normativo", "s8")
T.hito("2016", "Entrada en vigor de la Ley 39/2015 (2-10-2016)", f"Disposición final séptima: {c('L39', 'Disposición final séptima', 'al año de su publicación en el “Boletín Oficial del Estado”')}", "normativo", "s13")
T.hito("2021", "Efectos de las previsiones sobre registro electrónico de apoderamientos y Punto de Acceso General electrónico de la Ley 39/2015 (2-4-2021)", "Disposición final séptima: afecta a la acreditación de la representación (art. 5.4) y al derecho del art. 13 a)", "normativo", "s2")

T.publicar()
