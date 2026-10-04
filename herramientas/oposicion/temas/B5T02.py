# -*- coding: utf-8 -*-
"""Tema V.2 (B5T02): Derechos y deberes del personal al servicio de las Administraciones
Públicas. Régimen disciplinario.
Método del I.2: mapa → bloques (I a IV) con guía; cada artículo, texto literal del
BOE + ficha de casillas fijas; cierre 1 (preguntas oficiales) y cierre 2 (repaso).
Normas (textos consolidados del BOE): TREBEP (RDLeg 5/2015), arts. 14 a 20, 47 a 54 y
93 a 98, disposición derogatoria única y disposición final cuarta; Real Decreto 33/1986,
Reglamento de Régimen Disciplinario de los Funcionarios de la Administración del Estado."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO["RD33"] = "RD 33/1986"
TB = "TREBEP"

T = Tema("B5T02",
  "Cuatro preguntas: I. Qué derechos tiene el personal (TREBEP, arts. 14 a 20) · II. Cuánto trabaja y qué permisos y vacaciones tiene (arts. 47 a 51) · III. Qué deberes tiene: el Código de Conducta (arts. 52 a 54) · IV. Qué pasa si los incumple: el régimen disciplinario (arts. 93 a 98 y Real Decreto 33/1986 en la AGE). Cada artículo: texto literal del BOE y ficha.",
  ["TREBEP", "Derechos individuales", "Art. 15", "Evaluación del desempeño", "Jornada", "Teletrabajo", "Permisos", "Art. 48", "Art. 49", "Vacaciones", "Código de Conducta", "Principios éticos", "Régimen disciplinario", "Faltas", "Sanciones", "Prescripción", "Suspensión provisional", "RD 33/1986"])

# =============================================================================
T.ap("s0", "Mapa del tema: cuatro preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque V, tema 2):
> Derechos y deberes del personal al servicio de las Administraciones Públicas. Régimen disciplinario.

### El hilo conductor

El epígrafe se lee como **cuatro preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | TREBEP (RDLeg 5/2015) | Otras normas |
|---|---|---|---|
| **I** | ¿Qué derechos tiene el personal? | Arts. 14, 15, 16.1, 19.1 y 20 | — |
| **II** | ¿Cuánto trabaja y qué permisos y vacaciones tiene? | Arts. 47, 47 bis, 48, 49, 50 y 51 | — |
| **III** | ¿Qué deberes tiene? (Código de Conducta) | Arts. 52, 53 y 54 | — |
| **IV** | ¿Qué pasa si los incumple? (régimen disciplinario) | Arts. 93 a 98; disposición derogatoria única y disposición final cuarta | Real Decreto 33/1986 (Reglamento de Régimen Disciplinario de los funcionarios de la AGE), arts. 1 a 3, 7, 8, 14 a 19, 27 a 31, 34 a 37, 41 a 45, 47, 49 y 51 |

!> **La idea que une los cuatro bloques:** el TREBEP reconoce al personal unos **derechos** (I), entre ellos el de las vacaciones, descansos, permisos y licencias, que se concretan en la **jornada, los permisos y las vacaciones** (II). A cambio le impone unos **deberes**: el **Código de Conducta** (III), cuyos principios, dice la propia ley, informan el **régimen disciplinario** (IV): qué conductas son falta, qué sanción cabe, cuándo prescriben y con qué procedimiento se imponen.

### Fronteras con otros temas

- Clases de personal y adquisición o pérdida de la condición de funcionario: tema V.1. Selección: tema V.3. Carrera, promoción interna y provisión de puestos: tema V.4. Situaciones e incompatibilidades: tema V.5. Retribuciones: tema V.6. Personal laboral: tema V.7. Negociación colectiva, reunión y huelga: tema V.8. Seguridad Social y MUFACE: tema V.9.
- Aquí solo se citan esos derechos (art. 14 y 15) y se remite al tema que los desarrolla.

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (derechos: Titulares · Contenido · Límites · Protección · ⚠ Ojo en el examen; instituciones y procedimientos: Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Los esquemas y cuadros **no son texto legal**: resumen los artículos citados.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué derechos tiene el personal? (TREBEP, arts. 14 a 20)", donde(
  "Primera pregunta del tema. El título III del TREBEP abre con los **derechos** de los empleados públicos. Distingue los derechos **individuales** (art. 14) de los derechos **individuales que se ejercen de forma colectiva** (art. 15), y dedica un capítulo a la carrera y a la evaluación del desempeño.",
  ["1 Derechos individuales (art. 14)", "2 Derechos individuales ejercidos colectivamente (art. 15)", "3 Promoción profesional y evaluación del desempeño (arts. 16.1, 19.1 y 20)"]))

T.ap("s1", "I.1 Derechos individuales (art. 14)", f"""
El art. 14 enumera, de la a) a la q), los derechos **de carácter individual** de **todos** los empleados públicos (funcionarios y laborales). Para estudiarlo se parte en tres grupos; la lista es una sola.

{unidad("1.1 Derechos ligados a la relación de servicio (art. 14 a a g)",
  lit(TB, "Artículo 14", ["en correspondencia con la naturaleza jurídica de su relación de servicio", "A la inamovilidad en la condición de funcionario de carrera", "igualdad, mérito y capacidad", "A la defensa jurídica y protección de la Administración Pública", "preferentemente en horario laboral"], solo=[1, 2, 3, 4, 5, 6, 7, 8], titulo="Artículo 14. Derechos individuales (TREBEP), letras a) a g)"),
  ficha(f"{c(TB, 'Artículo 14', 'Los empleados públicos')}; la inamovilidad, solo el **funcionario de carrera**",
        ["Inamovilidad en la condición de funcionario de carrera (a)", "Desempeño efectivo de funciones o tareas (b)", "Progresión en la carrera y promoción interna (c; tema V.4)", "Retribuciones e indemnizaciones por razón del servicio (d; tema V.6)", "Participar en los objetivos de la unidad y ser informado de las tareas (e)", "Defensa jurídica y protección de la Administración (f)", "Formación continua y actualización (g)"],
        f"Defensa jurídica: solo por el {c(TB, 'Artículo 14', 'ejercicio legítimo de sus funciones o cargos públicos')}",
        "—",
        "La **inamovilidad** es de la condición de **funcionario de carrera** (no del puesto). La formación es **preferentemente** en horario laboral. La defensa jurídica alcanza a **cualquier orden jurisdiccional**."))}

{unidad("1.2 Derechos de la persona en el trabajo (art. 14 h a k)",
  lit(TB, "Artículo 14", ["especialmente frente al acoso sexual y por razón de sexo", "A la no discriminación", "A la adopción de medidas que favorezcan la conciliación de la vida personal, familiar y laboral", "desconexión digital", "dentro de los límites del ordenamiento jurídico"], solo=[9, 10, 11, 12, 13], titulo="Artículo 14. Derechos individuales (TREBEP), letras h) a k)"),
  ficha("Los empleados públicos",
        ["Intimidad, propia imagen y dignidad en el trabajo, frente al acoso (h)", "No discriminación (i)", "Medidas de conciliación (j)", "Intimidad ante dispositivos digitales, videovigilancia y geolocalización, y desconexión digital (j bis)", "Libertad de expresión (k)"],
        f"Libertad de expresión: {c(TB, 'Artículo 14', 'dentro de los límites del ordenamiento jurídico')}; desconexión digital: {c(TB, 'Artículo 14', 'en los términos establecidos en la legislación vigente en materia de protección de datos personales y garantía de los derechos digitales')}",
        "El acoso y la discriminación son también **faltas muy graves** (art. 95.2 b y o → IV.2.1)",
        "La letra **j bis)** (intimidad digital y desconexión) remite a la legislación de **protección de datos**. El acoso protegido es el sexual, por razón de sexo, de orientación e identidad sexual, expresión de género o características sexuales, **moral y laboral**."))}

{unidad("1.3 Salud, descansos, jubilación, Seguridad Social y asociación (art. 14 l a q)",
  lit(TB, "Artículo 14", ["A las vacaciones, descansos, permisos y licencias", "A la libre asociación profesional"], solo=[14, 15, 16, 17, 18, 19], titulo="Artículo 14. Derechos individuales (TREBEP), letras l) a q)"),
  ficha("Los empleados públicos",
        ["Protección eficaz en seguridad y salud en el trabajo (l)", "Vacaciones, descansos, permisos y licencias (m → II)", "Jubilación (n; tema V.5)", "Prestaciones de la Seguridad Social del régimen aplicable (o; tema V.9)", "Libre asociación profesional (p)", "Los demás reconocidos por el ordenamiento jurídico (q)"],
        f"Jubilación {c(TB, 'Artículo 14', 'según los términos y condiciones establecidas en las normas aplicables')}",
        "—",
        "La **libre asociación profesional** es un derecho **individual** (art. 14 p); la **libertad sindical** es individual **ejercido colectivamente** (art. 15 a → I.2.1). Cayó en 2025 (→ Cierre 1). La lista no es cerrada: letra **q)**."))}
""", 2)

T.ap("s2", "I.2 Derechos individuales ejercidos colectivamente (art. 15)", f"""
{unidad("2.1 Cinco derechos de ejercicio colectivo (art. 15)",
  lit(TB, "Artículo 15", ["que se ejercen de forma colectiva", "A la libertad sindical", "con la garantía del mantenimiento de los servicios esenciales de la comunidad", "en los términos establecidos en el artículo 46 de este Estatuto"]),
  ficha(c(TB, 'Artículo 15', 'Los empleados públicos'),
        ["Libertad sindical (a)", "Negociación colectiva y participación en la determinación de las condiciones de trabajo (b; tema V.8)", "Huelga (c; tema V.8)", "Planteamiento de conflictos colectivos (d)", "Reunión, en los términos del art. 46 (e; tema V.8)"],
        f"Huelga: {c(TB, 'Artículo 15', 'con la garantía del mantenimiento de los servicios esenciales de la comunidad')}",
        "No atender los servicios esenciales en caso de huelga es **falta muy grave** (art. 95.2 m → IV.2.1)",
        "Son **cinco**: libertad sindical, negociación colectiva, huelga, conflictos colectivos y reunión. La **libre asociación profesional** NO está aquí (es del art. 14 p → I.1.3)."))}
""", 2)

T.ap("s3", "I.3 Promoción profesional y evaluación del desempeño (arts. 16.1, 19.1 y 20)", f"""
El capítulo II del título III reconoce el derecho a la carrera y a la promoción interna. Las **modalidades de carrera** y la **promoción interna** (arts. 16.2 a 18) se estudian en el tema V.4; aquí, el derecho y la evaluación del desempeño.

{unidad("3.1 Derecho a la promoción profesional (arts. 16.1 y 19.1)",
  lit(TB, "Artículo 16", ["tendrán derecho a la promoción profesional"], solo=[1], titulo="Artículo 16. Concepto, principios y modalidades de la carrera profesional de los funcionarios de carrera (TREBEP), apartado 1"),
  lit(TB, "Artículo 19", ["El personal laboral tendrá derecho a la promoción profesional", "Estatuto de los Trabajadores o en los convenios colectivos"]),
  ficha("Funcionarios de carrera (art. 16.1) y personal laboral (art. 19.1)",
        "Derecho a la promoción profesional",
        f"Personal laboral: {c(TB, 'Artículo 19', 'a través de los procedimientos previstos en el Estatuto de los Trabajadores o en los convenios colectivos')}",
        "—",
        "Las modalidades (carrera horizontal y vertical, promoción interna vertical y horizontal) son materia del tema V.4."))}

{unidad("3.2 La evaluación del desempeño (art. 20)",
  lit(TB, "Artículo 20", ["se mide y valora la conducta profesional y el rendimiento o el logro de resultados", "transparencia, objetividad, imparcialidad y no discriminación", "dándose audiencia al interesado", "requerirán la aprobación previa"]),
  fichab("Procedimiento que mide y valora la conducta profesional y el rendimiento o el logro de resultados",
         c(TB, 'Artículo 20', 'Las Administraciones Públicas establecerán sistemas'),
         ["::Criterios (20.2): transparencia, objetividad, imparcialidad y no discriminación. Efectos que fija cada Administración (20.3):", "Carrera profesional horizontal", "Formación", "Provisión de puestos de trabajo", "Retribuciones complementarias del art. 24"],
         f"Continuidad en el puesto obtenido por concurso: vinculada a la evaluación, {c(TB, 'Artículo 20', 'dándose audiencia al interesado, y por la correspondiente resolución motivada')}",
         "Para aplicar la carrera horizontal, las retribuciones complementarias del art. 24 c) y el **cese** en un puesto obtenido por **concurso** hace falta la **aprobación previa** de sistemas objetivos de evaluación (20.5)."))}

{resumen([
  "Art. 14: derechos **individuales** (a-q), entre ellos inamovilidad del funcionario de carrera, defensa jurídica, formación, intimidad y desconexión digital, vacaciones y permisos y **libre asociación profesional**.",
  "Art. 15: derechos individuales **ejercidos colectivamente**: libertad sindical, negociación colectiva, huelga, conflictos colectivos y reunión.",
  "Derecho a la **promoción profesional** de funcionarios (16.1) y laborales (19.1); la **evaluación del desempeño** mide conducta profesional y rendimiento (20)."],
  "Siguiente: II. ¿Cuánto trabaja y qué permisos y vacaciones tiene?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Cuánto trabaja y qué permisos y vacaciones tiene? (TREBEP, arts. 47 a 51)", donde(
  "Segunda pregunta. El derecho del art. 14 m) «a las vacaciones, descansos, permisos y licencias» se concreta en el capítulo V del título III: **jornada** y **teletrabajo**, **permisos** (art. 48), permisos **por conciliación y por violencia de género, violencia sexual o terrorismo** (art. 49) y **vacaciones** (art. 50).",
  ["1 Jornada y teletrabajo (arts. 47 y 47 bis)", "2 Permisos de los funcionarios (art. 48)", "3 Permisos por conciliación, violencia de género o sexual y terrorismo (art. 49)", "4 Vacaciones y personal laboral (arts. 50 y 51) y cuadro de permisos"]))

T.ap("s4", "II.1 Jornada y teletrabajo (arts. 47 y 47 bis)", f"""
{unidad("1.1 Jornada de trabajo (art. 47)",
  lit(TB, "Artículo 47", ["establecerán la jornada general y las especiales", "a tiempo completo o a tiempo parcial", "hijos e hijas menores de doce años"]),
  fichab("Jornada general y especiales de los funcionarios y flexibilización horaria",
         c(TB, 'Artículo 47', 'Las Administraciones Públicas'),
         ["Jornada a tiempo completo o a tiempo parcial", "Medidas de flexibilización horaria para la conciliación"],
         "Flexibilización: hijos e hijas **menores de doce años**; también necesidades de cuidado de hijos mayores de doce años, cónyuge o pareja de hecho, familiares hasta el **segundo grado** de consanguinidad y convivientes que no puedan valerse por sí mismos",
         "El TREBEP **no fija** el número de horas: lo establece cada Administración. La edad de referencia es **doce** años."))}

{unidad("1.2 Teletrabajo (art. 47 bis)",
  lit(TB, "Artículo 47 bis", ["fuera de las dependencias de la Administración", "expresamente autorizada", "voluntario y reversible", "los mismos deberes y derechos", "proporcionará y mantendrá"]),
  fichab("Modalidad de prestación de servicios a distancia mediante tecnologías de la información y comunicación",
         "El personal autorizado; la Administración proporciona y mantiene los medios tecnológicos; el personal laboral se rige por el TREBEP y sus normas de desarrollo (47 bis.5)",
         ["Expresamente autorizada y compatible con la modalidad presencial", "Voluntaria y reversible, salvo supuestos excepcionales debidamente justificados", "Normas de desarrollo objeto de negociación colectiva, con criterios objetivos de acceso"],
         "—",
         f"Siempre {c(TB, 'Artículo 47 bis', 'que las necesidades del servicio lo permitan')}. El personal en teletrabajo tiene **los mismos** deberes y derechos que el presencial, salvo los inherentes a la presencia."))}
""", 2)

T.ap("s5", "II.2 Permisos de los funcionarios (art. 48)", f"""
El art. 48 enumera, de la a) a la m), los permisos de los funcionarios públicos. Se agrupan para estudiarlos; el cuadro final (→ II.4) reúne los días.

{unidad("2.1 Enfermedad grave o fallecimiento de familiares (art. 48 a)",
  lit(TB, "Artículo 48", ["cinco días hábiles", "el permiso será de cuatro días hábiles", "tres días hábiles cuando el suceso se produzca en la misma localidad, y cinco días hábiles, cuando sea en distinta localidad", "dos días hábiles cuando se produzca en la misma localidad y de cuatro días hábiles cuando sea en distinta localidad"], solo=[1, 2, 3, 4], titulo="Artículo 48. Permisos de los funcionarios públicos (TREBEP), letra a)"),
  ficha("Los funcionarios públicos",
        ["::Accidente o enfermedad graves, hospitalización o intervención quirúrgica sin hospitalización con reposo domiciliario:", "Cónyuge, pareja de hecho, parientes hasta el **primer grado** o conviviente que requiera cuidado efectivo: **cinco** días hábiles", "Familiar dentro del **segundo grado**: **cuatro** días hábiles", "::Fallecimiento:", "Cónyuge, pareja de hecho o familiar de **primer grado**: **tres** días hábiles (misma localidad) o **cinco** (distinta localidad)", "Familiar de **segundo grado**: **dos** días hábiles (misma localidad) o **cuatro** (distinta localidad)"],
        "Los días son **hábiles**",
        "—",
        "Enfermedad grave: **5** (1.er grado y convivientes) / **4** (2.º grado), sin distinguir localidad. Fallecimiento: **3/5** (1.er grado) y **2/4** (2.º grado), según sea la misma o distinta localidad."))}

{unidad("2.2 Traslado, funciones sindicales, exámenes y exámenes prenatales (art. 48 b a e)",
  lit(TB, "Artículo 48", ["un día", "durante los días de su celebración", "por las funcionarias embarazadas", "incluye también a las personas funcionarias trans gestantes"], solo=[5, 6, 7, 8, 9], titulo="Artículo 48. Permisos de los funcionarios públicos (TREBEP), letras b) a e)"),
  ficha("Los funcionarios públicos; el de exámenes prenatales, las **funcionarias embarazadas** (incluidas las personas funcionarias trans gestantes)",
        ["Traslado de domicilio sin cambio de residencia: **un día** (b)", "Funciones sindicales o de representación del personal (c)", "Exámenes finales y demás pruebas definitivas de aptitud: **durante los días de su celebración** (d)", "Exámenes prenatales y técnicas de preparación al parto; en adopción, acogimiento o guarda, sesiones de información y preparación e informes previos a la idoneidad: **tiempo indispensable** (e)"],
        f"El permiso de la letra e), para trámites {c(TB, 'Artículo 48', 'que deban realizarse dentro de la jornada de trabajo')}",
        "—",
        "Exámenes prenatales: solo **funcionarias embarazadas** y **personas funcionarias trans gestantes** (cayó en 2025 → Cierre 1). Traslado: **sin** cambio de residencia, **un** día."))}

{unidad("2.3 Lactancia y nacimiento de hijos prematuros u hospitalizados (art. 48 f y g)",
  lit(TB, "Artículo 48", ["menor de doce meses tendrán derecho a una hora de ausencia del trabajo que podrá dividir en dos fracciones", "sin que pueda transferirse su ejercicio al otro progenitor", "acumule en jornadas completas", "un máximo de dos horas diarias percibiendo las retribuciones íntegras", "con la disminución proporcional de sus retribuciones"], solo=[10, 11, 12, 13, 14, 15], titulo="Artículo 48. Permisos de los funcionarios públicos (TREBEP), letras f) y g)"),
  ficha("Los funcionarios (derecho **individual**, intransferible, el de lactancia)",
        ["Lactancia de hijo **menor de doce meses**: **una hora** de ausencia, divisible en dos fracciones; o reducción de media hora al inicio y al final, o de una hora al inicio o al final", "Puede acumularse en **jornadas completas** (permiso retribuido), a partir del fin del permiso por nacimiento, adopción, guarda, acogimiento o del progenitor diferente", "Prematuros u hospitalizados tras el parto: ausencia de hasta **dos horas diarias** con retribuciones íntegras, y reducción de jornada de hasta **dos horas** con disminución proporcional"],
        "Se incrementa proporcionalmente en caso de parto, adopción, guarda o acogimiento **múltiple**",
        "—",
        "Lactancia: **doce meses**, **una hora**, **intransferible**. Prematuros: ausentarse **dos horas** cobrando íntegro; **reducir** hasta dos horas cobrando menos."))}

{unidad("2.4 Reducciones de jornada por guarda legal y por cuidado de familiar (art. 48 h e i)",
  lit(TB, "Artículo 48", ["algún menor de doce años", "con la disminución de sus retribuciones que corresponda", "hasta el segundo grado de consanguinidad o afinidad", "una reducción de hasta el cincuenta por ciento de la jornada laboral, con carácter retribuido, por razones de enfermedad muy grave y por el plazo máximo de un mes"], solo=[16, 17, 18, 19], titulo="Artículo 48. Permisos de los funcionarios públicos (TREBEP), letras h) e i)"),
  ficha("El funcionario con el cuidado directo de la persona",
        ["Guarda legal (h): menor de **doce años**, persona mayor que requiera especial dedicación o persona con discapacidad sin actividad retribuida → reducción de jornada **con disminución** de retribuciones", "Mismo derecho para cuidar a un familiar hasta el **segundo grado** que no pueda valerse por sí mismo y sin actividad retribuida", "Familiar de **primer grado** con **enfermedad muy grave** (i) → reducción de hasta el **50 %**, **retribuida**, máximo **un mes**"],
        "En la letra i), si hay varios titulares por el mismo hecho causante, se prorratea respetando el máximo de un mes",
        "—",
        "Guarda legal: **sin** sueldo íntegro. Enfermedad muy grave de familiar de **1.er grado**: **retribuida**, hasta el **50 %** y **un mes**."))}

{unidad("2.5 Deberes inexcusables, asuntos particulares, matrimonio y donación (art. 48 j a m)",
  lit(TB, "Artículo 48", ["deber inexcusable de carácter público o personal", "seis días al año", "quince días", "donación de órganos o tejidos"], solo=[20, 21, 22, 23], titulo="Artículo 48. Permisos de los funcionarios públicos (TREBEP), letras j) a m)"),
  ficha("Los funcionarios públicos",
        ["Deber inexcusable público o personal y deberes de conciliación: tiempo indispensable (j)", "Asuntos particulares: **seis días al año** (k)", "Matrimonio o registro o constitución formalizada por documento público de pareja de hecho: **quince días** (l)", "Actos preparatorios de la donación de órganos o tejidos: tiempo indispensable, si deben tener lugar dentro de la jornada (m)"],
        "—",
        "—",
        "Asuntos particulares: **seis** días. Matrimonio **o pareja de hecho** formalizada: **quince** días (el texto no dice «hábiles»)."))}
""", 2)

T.ap("s6", "II.3 Permisos por conciliación, violencia de género o sexual y terrorismo (art. 49)", f"""
El art. 49 fija **condiciones mínimas** ({c(TB, 'Artículo 49', 'En todo caso se concederán los siguientes permisos con las correspondientes condiciones mínimas')}). Es el artículo que más se reforma: se cita en su redacción vigente.

{unidad("3.1 Permiso por nacimiento para la madre biológica (art. 49 a)",
  lit(TB, "Artículo 49", ["tendrá una duración de diecinueve semanas", "treinta y dos semanas", "con un máximo de trece semanas adicionales", "Seis semanas ininterrumpidas inmediatamente posteriores al parto, serán obligatorias", "Once semanas, veintidós en el caso de monoparentalidad", "Dos semanas, cuatro en el caso de monoparentalidad", "hasta que el hijo o la hija cumpla los ocho años", "sin que pueda transferirse su ejercicio", "un preaviso de al menos quince días"], solo=[1, 2, 3, 4, 6, 8, 9, 10, 11, 12, 14, 17], titulo="Artículo 49. Permisos por motivos de conciliación… (TREBEP), letra a) (fragmento)"),
  ficha("La **madre biológica** (incluye a las personas trans gestantes)",
        ["**Diecinueve semanas**; **treinta y dos** en monoparentalidad", "Seis semanas **obligatorias**, ininterrumpidas y a jornada completa, tras el parto", "Once semanas (veintidós si monoparentalidad) a disfrutar hasta que el hijo cumpla **doce meses**", "Dos semanas (cuatro si monoparentalidad) hasta que cumpla **ocho años**"],
        "Parto prematuro u hospitalización del neonato: se amplía en los días de hospitalización, con un máximo de **trece semanas** adicionales; discapacidad del hijo o parto múltiple: **dos semanas más** / una por cada hijo a partir del segundo",
        "Se computa como **servicio efectivo** a todos los efectos, con plenitud de derechos económicos (párrafo final de la letra c)",
        "**19** semanas (no 16 ni 17); **32** si monoparental. Derecho **individual** e **intransferible**. Disfrute interrumpido: preaviso de **quince días** y por **semanas completas**. Cayó en 2025 (→ Cierre 1)."))}

{unidad("3.2 Permiso por adopción, guarda con fines de adopción o acogimiento (art. 49 b)",
  lit(TB, "Artículo 49", ["tendrá una duración de diecinueve semanas para cada adoptante, guardador o acogedor", "un permiso de hasta dos meses de duración, percibiendo durante este periodo exclusivamente las retribuciones básicas", "no inferior a un año"], solo=[18, 19, 22, 26, 30, 33], titulo="Artículo 49. Permisos por motivos de conciliación… (TREBEP), letra b) (fragmento)"),
  ficha("Cada adoptante, guardador o acogedor",
        ["**Diecinueve semanas** para cada uno; **treinta y dos** en monoparentalidad", "Seis semanas obligatorias tras la resolución judicial o la decisión administrativa", "Adopción o acogimiento **internacional**: además, hasta **dos meses** con solo las retribuciones **básicas**"],
        "Acogimiento temporal: duración **no inferior a un año**",
        "—",
        "Derecho **individual** e intransferible. El permiso adicional por desplazamiento al país de origen es de **dos meses** con retribuciones **básicas**."))}

{unidad("3.3 Permiso del progenitor diferente de la madre biológica y efectos comunes (art. 49 c)",
  lit(TB, "Artículo 49", ["Permiso del progenitor diferente de la madre biológica", "tendrá una duración de diecinueve semanas", "se computará como de servicio efectivo a todos los efectos", "a reintegrarse a su puesto de trabajo"], solo=[34, 35, 44, 50, 51], titulo="Artículo 49. Permisos por motivos de conciliación… (TREBEP), letra c) (fragmento)"),
  ficha("El progenitor diferente de la madre biológica (nacimiento, guarda con fines de adopción, acogimiento o adopción)",
        ["**Diecinueve semanas**; **treinta y dos** en monoparentalidad", "Derecho individual, sin que pueda transferirse su ejercicio"],
        "—",
        ["::En las letras a), b) y c):", "Servicio efectivo a todos los efectos y plenitud de derechos económicos", "Reintegro al puesto en condiciones no menos favorables y derecho a las mejoras producidas durante la ausencia"],
        "Madre biológica, adoptante y progenitor diferente: **los tres, 19 semanas**. Cayó en 2025 con la fórmula «19 semanas por progenitor» (→ Cierre 1)."))}

{unidad("3.4 Violencia de género o violencia sexual (art. 49 d)",
  lit(TB, "Artículo 49", ["tendrán la consideración de justificadas", "mantendrá sus retribuciones íntegras cuando reduzca su jornada en un tercio o menos"], solo=[52, 53, 54], titulo="Artículo 49. Permisos por motivos de conciliación… (TREBEP), letra d)"),
  ficha("La **funcionaria** víctima de violencia de género o de violencia sexual",
        ["Faltas de asistencia totales o parciales **justificadas**, en los términos que determinen los servicios sociales de atención o de salud", "Reducción de jornada con disminución proporcional, o reordenación del tiempo de trabajo (adaptación del horario, horario flexible…)"],
        "En los términos del plan de igualdad aplicable o, en su defecto, de la Administración competente",
        "—",
        "Retribuciones **íntegras** si reduce la jornada en **un tercio o menos**."))}

{unidad("3.5 Cuidado de hijo menor afectado por cáncer u otra enfermedad grave (art. 49 e)",
  lit(TB, "Artículo 49", ["de al menos la mitad de la duración de aquélla, percibiendo las retribuciones íntegras", "cumpla los 23 años", "hasta que la persona a su cargo cumpla 26 años"], solo=[55, 57], titulo="Artículo 49. Permisos por motivos de conciliación… (TREBEP), letra e) (fragmento)"),
  ficha(f"El funcionario, {c(TB, 'Artículo 49', 'siempre que ambas personas progenitoras, adoptantes, guardadoras con fines de adopción o acogedoras de carácter permanente trabajen')}",
        "Reducción de jornada de **al menos la mitad**, con retribuciones **íntegras**, durante la hospitalización y tratamiento continuado",
        "Como máximo hasta que el hijo cumpla **23 años**; hasta **26** si antes de los 23 acredita una discapacidad igual o superior al **65 %**",
        "Acreditación por informe del servicio público de salud u órgano sanitario de la comunidad autónoma (o entidad concertada)",
        "Reducción **mínima** del **50 %** con sueldo **íntegro**. Edades: **23** y, con discapacidad ≥ 65 %, **26**."))}

{unidad("3.6 Víctimas del terrorismo y sus familiares (art. 49 f)",
  lit(TB, "Artículo 49", ["como consecuencia de la actividad terrorista", "previo reconocimiento del Ministerio del Interior o de sentencia judicial firme"], solo=[62], titulo="Artículo 49. Permisos por motivos de conciliación… (TREBEP), letra f) (fragmento)"),
  ficha("Funcionarios víctimas del terrorismo, su cónyuge o persona con análoga relación de afectividad y los hijos de heridos y fallecidos (si son funcionarios y víctimas), y funcionarios amenazados",
        "Reducción de jornada con disminución proporcional de la retribución, o reordenación del tiempo de trabajo",
        f"{c(TB, 'Artículo 49', 'previo reconocimiento del Ministerio del Interior o de sentencia judicial firme')}",
        "Las medidas se mantienen mientras resulten necesarias",
        "Reconoce el **Ministerio del Interior** o una **sentencia judicial firme**."))}

{unidad("3.7 Permiso parental (art. 49 g)",
  lit(TB, "Artículo 49", ["hasta el momento en que el menor cumpla ocho años", "no tendrá carácter retribuido y tendrá una duración no superior a ocho semanas", "con una antelación de quince días"], solo=[64, 65, 66], titulo="Artículo 49. Permisos por motivos de conciliación… (TREBEP), letra g) (fragmento)"),
  ficha("Las personas progenitoras, adoptantes o acogedoras (derecho individual e intransferible)",
        "Cuidado de hijo, hija o menor acogido por tiempo superior a un año, hasta que cumpla **ocho años**",
        "**No retribuido**; **no superior a ocho semanas**, continuas o discontinuas, a tiempo completo o parcial si las necesidades del servicio lo permiten",
        "Comunicación con **quince días** de antelación y por semanas completas",
        "Parental: **ocho** semanas, **sin** retribución, hasta los **ocho** años del menor."))}
""", 2)

T.ap("s7", "II.4 Vacaciones y personal laboral (arts. 50 y 51) y cuadro de permisos", f"""
{unidad("4.1 Vacaciones de los funcionarios (art. 50)",
  lit(TB, "Artículo 50", ["vacaciones retribuidas de veintidós días hábiles", "no se considerarán como días hábiles los sábados", "dieciocho meses a partir del final del año en que se hayan originado", "no puede ser sustituido por una cuantía económica", "por causas ajenas a la voluntad de estos"]),
  ficha("Los funcionarios públicos",
        ["**Veintidós días hábiles** por año natural (o la parte proporcional si el servicio fue menor)", "Los **sábados** no son días hábiles a estos efectos (salvo adaptaciones de horarios especiales)"],
        "No se sustituyen por dinero; excepción: conclusión de la relación de servicios por causas **ajenas a la voluntad** del funcionario (compensación por las devengadas y no disfrutadas)",
        "Si el permiso de maternidad, la incapacidad temporal o el riesgo durante la lactancia o el embarazo impiden disfrutarlas en el año: pueden disfrutarse después, siempre que no hayan pasado más de **dieciocho meses** desde el final del año en que se originaron",
        "**22 días hábiles**, sábados **no** hábiles; límite de **18 meses**. En la renuncia voluntaria debe garantizarse el disfrute de las vacaciones devengadas."))}

{unidad("4.2 Personal laboral (art. 51)",
  lit(TB, "Artículo 51", ["en este capítulo y en la legislación laboral correspondiente"]),
  fichab("Régimen de jornada, permisos y vacaciones del personal laboral",
         "El personal laboral de las Administraciones Públicas (tema V.7)",
         f"Se rige por {c(TB, 'Artículo 51', 'lo establecido en este capítulo y en la legislación laboral correspondiente')}",
         "—",
         "Al personal laboral **también** se le aplica el capítulo V del TREBEP, no solo la legislación laboral."))}

### Cuadro de permisos y vacaciones (esquema)

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Supuesto | Artículo | Duración |
|---|---|---|
| Enfermedad grave, hospitalización… de cónyuge, pareja, 1.er grado o conviviente | 48 a) | 5 días hábiles |
| Ídem, familiar de 2.º grado | 48 a) | 4 días hábiles |
| Fallecimiento de cónyuge, pareja o 1.er grado | 48 a) | 3 días hábiles (misma localidad) / 5 (distinta) |
| Fallecimiento de familiar de 2.º grado | 48 a) | 2 días hábiles (misma localidad) / 4 (distinta) |
| Traslado de domicilio sin cambio de residencia | 48 b) | 1 día |
| Lactancia de hijo menor de 12 meses | 48 f) | 1 hora diaria (acumulable en jornadas completas) |
| Hijos prematuros u hospitalizados tras el parto | 48 g) | Hasta 2 horas diarias retribuidas |
| Enfermedad muy grave de familiar de 1.er grado | 48 i) | Reducción de hasta el 50 %, retribuida, máximo 1 mes |
| Asuntos particulares | 48 k) | 6 días al año |
| Matrimonio o pareja de hecho formalizada | 48 l) | 15 días |
| Nacimiento (madre biológica), adopción, guarda o acogimiento, progenitor diferente | 49 a), b) y c) | 19 semanas (32 en monoparentalidad) |
| Permiso parental | 49 g) | Hasta 8 semanas, no retribuido, hasta los 8 años del menor |
| Vacaciones | 50 | 22 días hábiles por año natural |

{resumen([
  "Jornada: la fijan **las Administraciones** (general y especiales; completa o parcial); flexibilización para hijos **menores de doce años** y otros cuidados (47). Teletrabajo **autorizado, voluntario y reversible** (47 bis).",
  "Art. 48: enfermedad grave **5/4** días hábiles; fallecimiento **3/5** y **2/4**; asuntos particulares **6**; matrimonio **15**; lactancia **una hora** hasta los **doce meses**.",
  "Art. 49: nacimiento, adopción y progenitor diferente, **19 semanas** (32 en monoparentalidad), con **6** obligatorias; permiso parental de **8 semanas** no retribuido.",
  "Vacaciones: **22 días hábiles**, sábados no hábiles, sin compensación económica salvo cese por causas ajenas a la voluntad (50). Laborales: este capítulo + legislación laboral (51)."],
  "Siguiente: III. ¿Qué deberes tiene? El Código de Conducta")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Qué deberes tiene? El Código de Conducta (TREBEP, arts. 52 a 54)", donde(
  "Tercera pregunta. Frente a los derechos, el capítulo VI del título III fija los **deberes** de los empleados públicos y los organiza como un **Código de Conducta**: un artículo de deberes y principios generales (52), los **principios éticos** (53) y los **principios de conducta** (54).",
  ["1 Deberes y Código de Conducta (art. 52)", "2 Principios éticos (art. 53)", "3 Principios de conducta (art. 54)"]))

T.ap("s8", "III.1 Deberes de los empleados públicos y Código de Conducta (art. 52)", f"""
{unidad("1.1 Deberes y principios del Código de Conducta (art. 52)",
  lit(TB, "Artículo 52", ["desempeñar con diligencia las tareas que tengan asignadas y velar por los intereses generales", "objetividad, integridad, neutralidad, responsabilidad, imparcialidad, confidencialidad, dedicación al servicio público, transparencia, ejemplaridad, austeridad, accesibilidad, eficacia, honradez, promoción del entorno cultural y medioambiental, y respeto a la igualdad entre mujeres y hombres", "informarán la interpretación y aplicación del régimen disciplinario"]),
  fichab("Deber general de diligencia y de servicio a los intereses generales; principios que inspiran el Código de Conducta",
         c(TB, 'Artículo 52', 'Los empleados públicos'),
         f"Con {c(TB, 'Artículo 52', 'sujeción y observancia de la Constitución y del resto del ordenamiento jurídico')}, conforme a quince principios",
         "—",
         "El Código de Conducta está formado por los **principios éticos** (53) y los **principios de conducta** (54). Estos principios **informan** la interpretación y aplicación del **régimen disciplinario** (→ IV.1)."))}
""", 2)

T.ap("s9", "III.2 Principios éticos (art. 53)", f"""
{unidad("2.1 Constitución, interés general, lealtad, no discriminación y conflictos de intereses (art. 53.1 a 6)",
  lit(TB, "Artículo 53", ["respetarán la Constitución", "satisfacción de los intereses generales de los ciudadanos", "lealtad y buena fe", "evitando toda actuación que pueda producir discriminación alguna", "Se abstendrán en aquellos asuntos en los que tengan un interés personal", "No contraerán obligaciones económicas"], solo=[1, 2, 3, 4, 5, 6], titulo="Artículo 53. Principios éticos (TREBEP), apartados 1 a 6"),
  fichab("Principios éticos del Código de Conducta (I)",
         "Los empleados públicos",
         ["Respeto a la Constitución y al ordenamiento (1)", "Intereses generales, objetividad e imparcialidad (2)", "Lealtad y buena fe con la Administración, superiores, compañeros, subordinados y ciudadanos (3)", "Respeto de los derechos fundamentales y no discriminación (4)", "Abstención en asuntos con interés personal y ante riesgos de conflicto de intereses (5)", "No contraer obligaciones económicas ni intervenir en operaciones con conflicto de intereses (6)"],
         "—",
         "La **abstención** (53.5) alcanza a asuntos con **interés personal** y a toda actividad privada que pueda plantear **conflictos de intereses**."))}

{unidad("2.2 Trato de favor, eficacia, neutralidad, plazos y secreto (art. 53.7 a 12)",
  lit(TB, "Artículo 53", ["No aceptarán ningún trato de favor", "eficacia, economía y eficiencia", "No influirán en la agilización o resolución de trámite", "resolverán dentro de plazo", "dedicación al servicio público", "Guardarán secreto de las materias clasificadas"], solo=[7, 8, 9, 10, 11, 12], titulo="Artículo 53. Principios éticos (TREBEP), apartados 7 a 12"),
  fichab("Principios éticos del Código de Conducta (II)",
         "Los empleados públicos",
         ["Rechazo de trato de favor o ventaja injustificada de particulares (7)", "Eficacia, economía y eficiencia (8)", "No influir en la agilización o resolución de trámites sin justa causa (9)", "Diligencia y resolución en plazo (10)", "Dedicación al servicio público y neutralidad (11)", "Secreto de materias clasificadas y discreción (12)"],
         "—",
         "**Secreto** para las materias clasificadas o de difusión prohibida; **discreción** para lo conocido por razón del cargo. Su vulneración puede ser falta muy grave (95.2 e y f → IV.2.1)."))}
""", 2)

T.ap("s10", "III.3 Principios de conducta (art. 54)", f"""
{unidad("3.1 Trato, diligencia, obediencia, información, recursos públicos y regalos (art. 54.1 a 6)",
  lit(TB, "Artículo 54", ["cumpliendo la jornada y el horario establecidos", "salvo que constituyan una infracción manifiesta del ordenamiento jurídico", "órganos de inspección procedentes", "con austeridad", "más allá de los usos habituales, sociales y de cortesía"], solo=[1, 2, 3, 4, 5, 6], titulo="Artículo 54. Principios de conducta (TREBEP), apartados 1 a 6"),
  fichab("Principios de conducta (I)",
         "Los empleados públicos",
         ["Atención y respeto a ciudadanos, superiores y compañeros (1)", "Diligencia y cumplimiento de jornada y horario (2)", "Obediencia a instrucciones y órdenes profesionales, salvo infracción manifiesta (3)", "Informar a los ciudadanos y facilitar sus derechos (4)", "Austeridad en recursos y bienes públicos (5)", "Rechazo de regalos más allá de los usos habituales, sociales y de cortesía (6)"],
         "—",
         "Si la orden es una **infracción manifiesta** del ordenamiento, no se obedece y se pone **inmediatamente** en conocimiento de los **órganos de inspección**. La desobediencia **abierta** es falta muy grave (95.2 i → IV.2.1)."))}

{unidad("3.2 Documentos, formación, seguridad, propuestas de mejora y lengua (art. 54.7 a 11)",
  lit(TB, "Artículo 54", ["constancia y permanencia de los documentos", "Mantendrán actualizada su formación", "en la lengua que lo solicite siempre que sea oficial en el territorio"], solo=[7, 8, 9, 10, 11], titulo="Artículo 54. Principios de conducta (TREBEP), apartados 7 a 11"),
  fichab("Principios de conducta (II)",
         "Los empleados públicos",
         ["Constancia y permanencia de los documentos (7)", "Formación y cualificación actualizadas (8)", "Normas de seguridad y salud laboral (9)", "Propuestas de mejora a superiores u órganos competentes (10)", "Atención al ciudadano en la lengua oficial que solicite (11)"],
         "—",
         f"Lengua: {c(TB, 'Artículo 54', 'siempre que sea oficial en el territorio')}."))}

{resumen([
  "Art. 52: deber de **diligencia** y de servicio a los **intereses generales**, con **quince** principios que inspiran el Código de Conducta; informan el **régimen disciplinario**.",
  "Art. 53 (principios **éticos**): Constitución, interés general, lealtad y buena fe, no discriminación, **abstención**, conflictos de intereses, trato de favor, plazos, **secreto** y discreción.",
  "Art. 54 (principios de **conducta**): respeto, jornada y horario, **obediencia salvo infracción manifiesta**, información, austeridad, **regalos** solo de cortesía, documentos, formación, lengua oficial."],
  "Siguiente: IV. ¿Qué pasa si los incumple? El régimen disciplinario")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Qué pasa si los incumple? El régimen disciplinario (TREBEP, arts. 93 a 98; RD 33/1986)", donde(
  "Cuarta pregunta. El incumplimiento de los deberes puede ser **falta disciplinaria**. El título VII del TREBEP fija las bases (responsabilidad, principios, faltas muy graves, sanciones, prescripción y procedimiento). En la Administración General del Estado se aplica además el **Real Decreto 33/1986**, en lo que no se oponga al TREBEP.",
  ["1 Responsabilidad, potestad disciplinaria y normas aplicables (arts. 93 y 94; RD 33/1986, arts. 1 a 3)", "2 Faltas (art. 95; RD 33/1986, arts. 7 y 8)", "3 Sanciones (art. 96; RD 33/1986, arts. 14 a 18)", "4 Prescripción y extinción (art. 97; RD 33/1986, art. 19)", "5 Procedimiento y medidas provisionales (art. 98)", "6 El procedimiento en la AGE (RD 33/1986)", "7 Cuadro del régimen disciplinario"]))

T.ap("s11", "IV.1 Responsabilidad, potestad disciplinaria y normas aplicables (arts. 93 y 94; RD 33/1986, arts. 1 a 3)", f"""
{unidad("1.1 Responsabilidad disciplinaria (art. 93)",
  lit(TB, "Artículo 93", ["Los funcionarios públicos y el personal laboral quedan sujetos al régimen disciplinario", "incurrirán en la misma responsabilidad que éstos", "encubrieren las faltas consumadas muy graves o graves", "por la legislación laboral"]),
  fichab("Sujeción al régimen disciplinario",
         "**Funcionarios** y **personal laboral**; también quien **induce** y quien **encubre**",
         ["Régimen del título VII del TREBEP y de las leyes de Función Pública de desarrollo", "Inductores: la misma responsabilidad que los autores", "Encubridores de faltas consumadas muy graves o graves, si se deriva daño grave para la Administración o los ciudadanos"],
         "—",
         "El encubrimiento solo es responsable si la falta es **muy grave o grave**, está **consumada** y causa **daño grave**. Personal laboral: en lo no previsto, **legislación laboral**."))}

{unidad("1.2 Ejercicio de la potestad disciplinaria y principios (art. 94)",
  lit(TB, "Artículo 94", ["sin perjuicio de la responsabilidad patrimonial o penal", "Principio de legalidad y tipicidad", "Principio de irretroactividad de las disposiciones sancionadoras no favorables", "Principio de proporcionalidad", "Principio de culpabilidad", "Principio de presunción de inocencia", "se suspenderá su tramitación poniéndolo en conocimiento del Ministerio Fiscal", "vinculan a la Administración"]),
  fichab("Potestad de las Administraciones para corregir las infracciones de su personal",
         c(TB, 'Artículo 94', 'Las Administraciones Públicas'),
         ["::Principios (94.2):", "Legalidad y tipicidad (predeterminación normativa o, para laborales, convenios colectivos)", "Irretroactividad de lo desfavorable y retroactividad de lo favorable", "Proporcionalidad", "Culpabilidad", "Presunción de inocencia"],
         "—",
         "Con **indicios fundados de criminalidad**, el procedimiento **se suspende** y se comunica al **Ministerio Fiscal**. Los hechos probados por resoluciones judiciales **firmes** vinculan a la Administración."))}

{unidad("1.3 El Reglamento de Régimen Disciplinario de la AGE y su encaje con el TREBEP (RD 33/1986, arts. 1 a 3; TREBEP, disposición derogatoria única y disposición final cuarta)",
  lit("RD33", "a1", ["Ley 30/1984"]),
  lit("RD33", "a2", ["funcionarios en prácticas"]),
  lit("RD33", "a3", ["carácter supletorio"]),
  lit(TB, "ddunica-2", ["Todas las normas de igual o inferior rango que contradigan o se opongan a lo dispuesto en este Estatuto"], solo=[1, 7], titulo="Disposición derogatoria única (TREBEP) (fragmento)"),
  lit(TB, "dfcuaa", ["se mantendrán en vigor en cada Administración Pública las normas vigentes"], solo=[3], titulo="Disposición final cuarta. Entrada en vigor (TREBEP), apartado 2"),
  fichab("Desarrollo reglamentario del régimen disciplinario de los funcionarios de la Administración del Estado",
         "Funcionarios del art. 1.1 de la Ley 30/1984; funcionarios en prácticas, en lo que les sea aplicable; supletorio para los demás",
         "El TREBEP deroga las normas de igual o inferior rango que se le opongan y mantiene las vigentes en cada Administración **en tanto no se opongan** a él",
         "—",
         "Por eso el RD 33/1986 se estudia **después** del TREBEP y **solo en lo que no se le opone**: donde difiere (faltas muy graves, prescripción), manda el TREBEP (→ IV.2.1 y → IV.4.1). Los nombres de órganos del RD 33/1986 son los de su texto de 1986, tal como lo publica el BOE consolidado."))}
""", 2)

T.ap("s12", "IV.2 Faltas disciplinarias (art. 95; RD 33/1986, arts. 7 y 8)", f"""
{unidad("2.1 Clases de faltas y faltas muy graves (art. 95.1 y 2)",
  lit(TB, "Artículo 95", ["pueden ser muy graves, graves y leves", "en el ejercicio de la función pública", "el acoso moral y sexual", "El abandono del servicio", "La publicación o utilización indebida de la documentación o información", "El notorio incumplimiento de las funciones esenciales", "La desobediencia abierta", "La prevalencia de la condición de empleado público", "El incumplimiento de la obligación de atender los servicios esenciales en caso de huelga", "cuando ello dé lugar a una situación de incompatibilidad", "La incomparecencia injustificada en las Comisiones de Investigación", "El acoso laboral", "en ley de las Cortes Generales o de la asamblea legislativa"], solo=list(range(1, 20)), titulo="Artículo 95. Faltas disciplinarias (TREBEP), apartados 1 y 2"),
  fichab("Catálogo de faltas muy graves del TREBEP",
         "Funcionarios y personal laboral",
         "Las letras a) a o) del art. 95.2 y las que tipifique una **ley** de las Cortes o de la asamblea legislativa autonómica (o los **convenios colectivos**, para el personal laboral)",
         "Prescriben a los **tres años** (→ IV.4.1)",
         f"Ojo con los matices: abandono del servicio **y** no hacerse cargo voluntariamente de las tareas (c); **notorio** incumplimiento de funciones **esenciales** (g); desobediencia **abierta** (i); incompatibilidades solo si dan lugar a una **situación de incompatibilidad** (n). El art. 6 del RD 33/1986 recoge otra lista (por ejemplo, {c('RD33', 'a6', 'La notoria falta de rendimiento')}): en lo que se oponga, rige el TREBEP (→ IV.1.3)."))}

{unidad("2.2 Faltas graves y leves (art. 95.3 y 4)",
  lit(TB, "Artículo 95", ["serán establecidas por ley de las Cortes Generales o de la asamblea legislativa", "El grado en que se haya vulnerado la legalidad", "El descrédito para la imagen pública de la Administración", "determinarán el régimen aplicable a las faltas leves"], solo=[20, 21, 22, 23, 24], titulo="Artículo 95. Faltas disciplinarias (TREBEP), apartados 3 y 4"),
  fichab("Remisión de las faltas graves y leves a la legislación de desarrollo",
         "Graves: ley de las Cortes o de la asamblea legislativa autonómica (convenios colectivos, laborales). Leves: leyes de Función Pública de desarrollo",
         ["::Circunstancias que se atienden:", "Grado de vulneración de la legalidad", "Gravedad de los daños al interés público, patrimonio o bienes de la Administración o de los ciudadanos", "Descrédito para la imagen pública de la Administración"],
         "—",
         "El TREBEP **no enumera** las faltas graves ni las leves: da los **criterios**. En la AGE, la lista está en el RD 33/1986 (→ IV.2.3 y → IV.2.4)."))}

{unidad("2.3 Faltas graves en la AGE (RD 33/1986, art. 7)",
  lit("RD33", "a7", ["La falta de obediencia debida a los superiores y autoridades", "La tolerancia de los superiores", "Intervenir en un procedimiento administrativo cuando se dé alguna de las causas de abstención", "un mínimo de diez horas al mes", "La tercera falta injustificada de asistencia en un período de tres meses", "evadir los sistemas de control de horarios", "desde el día primero al último de cada uno de los doce que componen el año"]),
  fichab("Catálogo de faltas graves de los funcionarios de la Administración del Estado",
         "Funcionarios del ámbito del RD 33/1986",
         "Letras a) a p) del art. 7.1",
         ["Incumplimiento injustificado de jornada: **mínimo de diez horas al mes** acumuladas (l)", "**Tercera** falta injustificada de asistencia en **tres meses**, si las dos anteriores se sancionaron como leves (m)", "Mes = del día primero al último de cada mes natural (7.2)"],
         "Falta de **obediencia debida** = grave; desobediencia **abierta** = muy grave (TREBEP 95.2 i). Intervenir en un procedimiento con causa de **abstención** = grave (g)."))}

{unidad("2.4 Faltas leves en la AGE (RD 33/1986, art. 8)",
  lit("RD33", "a8", ["cuando no suponga falta grave", "La falta de asistencia injustificada de un día", "El descuido o negligencia en el ejercicio de sus funciones"]),
  fichab("Catálogo de faltas leves de los funcionarios de la Administración del Estado",
         "Funcionarios del ámbito del RD 33/1986",
         ["Incumplimiento injustificado del horario que no sea falta grave (a)", "Falta de asistencia injustificada de **un día** (b)", "Incorrección con el público, superiores, compañeros o subordinados (c)", "Descuido o negligencia (d)", "Incumplimiento de deberes que no sea falta muy grave ni grave (e)"],
         "—",
         "**Un día** de falta injustificada = leve; la **tercera** en tres meses (con dos sancionadas) = grave. Incorrección = leve; **grave** desconsideración = grave (art. 7.1 e)."))}
""", 2)

T.ap("s13", "IV.3 Sanciones (art. 96; RD 33/1986, arts. 14 a 18)", f"""
{unidad("3.1 Sanciones del TREBEP (art. 96)",
  lit(TB, "Artículo 96", ["revocación de su nombramiento", "sólo podrá sancionar la comisión de faltas muy graves", "inhabilitación para ser titular de un nuevo contrato de trabajo", "con una duración máxima de 6 años", "con o sin cambio de localidad de residencia", "penalización a efectos de carrera, promoción o movilidad voluntaria", "Apercibimiento", "Procederá la readmisión del personal laboral fijo", "el grado de intencionalidad, descuido o negligencia"]),
  fichab("Sanciones disciplinarias",
         "Funcionarios (de carrera e interinos) y personal laboral",
         ["Separación del servicio (interinos: revocación del nombramiento): solo faltas **muy graves** (a)", "Despido disciplinario del laboral: solo faltas muy graves, con inhabilitación para un nuevo contrato con funciones similares (b)", "Suspensión firme de funciones (laborales: de empleo y sueldo): máximo **6 años** (c)", "Traslado forzoso, con o sin cambio de localidad (d)", "**Demérito**: penalización a efectos de carrera, promoción o movilidad voluntaria (e)", "Apercibimiento (f)", "Cualquier otra que establezca la ley (g)"],
         "Despido improcedente de un laboral **fijo** por falta muy grave → **readmisión** (96.2)",
         "Graduación (96.3): intencionalidad, descuido o negligencia, daño al interés público, reiteración o reincidencia y grado de participación. **Demérito** cayó en 2025 (→ Cierre 1)."))}

{unidad("3.2 Sanciones en la AGE y su correspondencia con las faltas (RD 33/1986, arts. 14 a 18)",
  lit("RD33", "a14", ["(Derogada)"]),
  lit("RD33", "a15", ["únicamente podrá imponerse por faltas muy graves"]),
  lit("RD33", "a16", ["no podrá ser superior a seis años ni inferior a tres", "no excederá de tres años", "durante tres años", "durante uno"]),
  lit("RD33", "a17", ["apartados d) o e) del artículo 14"]),
  lit("RD33", "a18", ["en virtud de expediente instruido al efecto", "salvo el trámite de audiencia al inculpado que deberá evacuarse en todo caso"]),
  fichab("Qué sanción corresponde a cada clase de falta en la AGE",
         "El órgano competente (→ IV.6.4)",
         ["Separación del servicio: solo faltas **muy graves** (15)", "Suspensión de funciones y traslado con cambio de residencia: faltas **graves o muy graves** (16)", "Faltas leves: solo las sanciones de las letras d) o e) del art. 14; la d) figura como **derogada**, de modo que queda el **apercibimiento** (17)"],
         ["Suspensión por falta muy grave: entre **tres y seis años**; por falta grave: **hasta tres años** (16)", "Trasladado con cambio de residencia: sin nuevo destino en la localidad de origen **tres años** (falta muy grave) o **uno** (grave) (16)", "Graves y muy graves: **expediente**; leves: sin expediente, pero **siempre con audiencia** (18)"],
         "El TREBEP añade el **demérito** y el traslado **sin** cambio de localidad (art. 96 → IV.3.1); el art. 14 del RD 33/1986 no los recoge."))}
""", 2)

T.ap("s14", "IV.4 Prescripción y extinción de la responsabilidad (art. 97; RD 33/1986, art. 19)", f"""
{unidad("4.1 Prescripción de faltas y sanciones (art. 97)",
  lit(TB, "Artículo 97", ["Las infracciones muy graves prescribirán a los tres años, las graves a los dos años y las leves a los seis meses", "las impuestas por faltas leves al año", "desde el cese de su comisión cuando se trate de faltas continuadas", "desde la firmeza de la resolución sancionadora"]),
  fichab("Plazos de prescripción de faltas y sanciones",
         "—",
         ["Faltas: desde que se cometieron; si son **continuadas**, desde el **cese** de su comisión", "Sanciones: desde la **firmeza** de la resolución sancionadora"],
         ["Faltas: muy graves **3 años**; graves **2 años**; leves **6 meses**", "Sanciones: por muy graves **3 años**; por graves **2 años**; por leves **1 año**"],
         f"La asimetría que más cae: falta leve **6 meses**, sanción por falta leve **1 año**. El RD 33/1986 fija otros plazos ({c('RD33', 'a20', 'Las faltas muy graves prescribirán a los seis años')}; leves, al mes): en lo que se opone al TREBEP, rige el art. 97 (→ IV.1.3)."))}

{unidad("4.2 Extinción de la responsabilidad disciplinaria (RD 33/1986, art. 19)",
  lit("RD33", "a19", ["cumplimiento de la sanción, muerte, prescripción de la falta o de la sanción, indulto y amnistía", "se declarará extinguido el procedimiento sancionador", "salvo que por parte interesada se inste la continuación del expediente"]),
  fichab("Causas de extinción de la responsabilidad disciplinaria",
         "—",
         ["Cumplimiento de la sanción", "Muerte", "Prescripción de la falta o de la sanción", "Indulto", "Amnistía"],
         "—",
         "Si durante el procedimiento se **pierde la condición de funcionario**, se declara extinguido el procedimiento y se archiva, **salvo** que la parte interesada inste su continuación; quedan sin efecto las medidas provisionales y subsiste la responsabilidad civil o penal."))}
""", 2)

T.ap("s15", "IV.5 Procedimiento disciplinario y medidas provisionales (art. 98)", f"""
{unidad("5.1 Procedimiento y separación de fases (art. 98.1 y 2)",
  lit(TB, "Artículo 98", ["sino mediante el procedimiento previamente establecido", "procedimiento sumario con audiencia al interesado", "eficacia, celeridad y economía procesal", "encomendándose a órganos distintos"], solo=[1, 2, 3, 4], titulo="Artículo 98. Procedimiento disciplinario y medidas provisionales (TREBEP), apartados 1 y 2"),
  fichab("Garantías del procedimiento disciplinario",
         "La Administración; la instrucción y la sanción, en **órganos distintos**",
         ["Faltas muy graves o graves: procedimiento previamente establecido", "Faltas leves: procedimiento **sumario** con **audiencia** al interesado", "Principios: eficacia, celeridad y economía procesal, con pleno respeto a los derechos de defensa"],
         "—",
         "Separación entre fase **instructora** y **sancionadora**, encomendadas a **órganos distintos**. Para faltas leves no hay expediente completo, pero **sí audiencia**."))}

{unidad("5.2 Medidas provisionales y suspensión provisional (art. 98.3 y 4)",
  lit(TB, "Artículo 98", ["mediante resolución motivada", "no podrá exceder de 6 meses, salvo en caso de paralización del procedimiento imputable al interesado", "las retribuciones básicas y, en su caso, las prestaciones familiares por hijo a cargo", "deberá devolver lo percibido", "será de abono para el cumplimiento de la suspensión firme", "se computará como de servicio activo"], solo=[5, 6, 7, 8, 9, 10], titulo="Artículo 98. Procedimiento disciplinario y medidas provisionales (TREBEP), apartados 3 y 4"),
  fichab("Medidas cautelares durante el expediente o un procedimiento judicial",
         "El órgano competente, por **resolución motivada**, cuando lo prevean las normas del procedimiento",
         ["Durante la suspensión provisional: retribuciones **básicas** y, en su caso, prestaciones familiares por hijo a cargo", "Si se eleva a definitiva: se devuelve lo percibido; el tiempo de suspensión provisional es **de abono** para la firme", "Si no se declara firme: cuenta como **servicio activo**, reincorporación inmediata y restitución de derechos"],
         ["Suspensión provisional en el expediente: máximo **6 meses** (salvo paralización imputable al interesado)", "En un procedimiento judicial: mientras duren la prisión provisional u otras medidas que impidan desempeñar el puesto; si excede de seis meses, no supone pérdida del puesto"],
         "**Seis meses** como máximo; se cobran solo las **básicas**. No confundir con la suspensión **firme** (sanción, hasta **6 años** → IV.3.1)."))}
""", 2)

T.ap("s16", "IV.6 El procedimiento en la AGE (RD 33/1986, título II)", f"""
El título II del RD 33/1986 desarrolla el procedimiento para las faltas graves y muy graves. Se recogen los artículos que fijan **órganos, actos y plazos**.

{unidad("6.1 Iniciación: de oficio, información reservada, órgano e instructor (arts. 27 a 31)",
  lit("RD33", "a27", ["se iniciará siempre de oficio", "orden superior, moción razonada de los subordinados o denuncia"]),
  lit("RD33", "a28", ["información reservada"]),
  lit("RD33", "a29", ["el Subsecretario del Departamento en que esté destinado el funcionario, en todo caso"]),
  lit("RD33", "a30", ["de igual o superior grupo al del inculpado", "nombramiento de Secretario"]),
  lit("RD33", "a31", ["se notificará al funcionario sujeto a expediente"]),
  fichab("Inicio del expediente disciplinario",
         "Incoa: el **Subsecretario** del Departamento (en todo caso), los Directores generales (su personal) y los Delegados del Gobierno o Gobernadores Civiles (su ámbito territorial). Instruye: un funcionario de **igual o superior grupo** que el inculpado; Secretario, si la complejidad lo exige",
         ["**Siempre de oficio**: por propia iniciativa, orden superior, moción razonada de los subordinados o denuncia", "Puede ir precedido de una **información reservada**", "La incoación y el nombramiento de Instructor y Secretario se notifican al funcionario y a los designados"],
         "—",
         "Aunque haya denuncia, el procedimiento se inicia **de oficio** (y se comunica al denunciante). El Instructor, de **igual o superior** grupo."))}

{unidad("6.2 Instrucción: pliego de cargos, contestación y prueba (arts. 34 a 37)",
  lit("RD33", "a34", ["recibir declaración al presunto inculpado"]),
  lit("RD33", "a35", ["en un plazo no superior a un mes, contados a partir de la incoación del procedimiento", "pliego de cargos"]),
  lit("RD33", "a36", ["un plazo de diez días"]),
  lit("RD33", "a37", ["Para la práctica de las pruebas se dispondrá del plazo de un mes", "sin que contra esta resolución queda recurso del inculpado"]),
  fichab("Fase de instrucción",
         "El **Instructor**",
         ["Primeras actuaciones: declaración del presunto inculpado y diligencias derivadas de la denuncia o comunicación (34)", "**Pliego de cargos**: hechos imputados, falta presunta y sanciones aplicables, en párrafos separados y numerados (35)", "Contestación del inculpado, con alegaciones, documentos y proposición de prueba (36)", "Prueba; la denegación debe motivarse y no cabe recurso del inculpado contra ella (37)"],
         ["Pliego de cargos: **no más de un mes** desde la incoación (ampliable por causas justificadas)", "Contestación al pliego: **diez días**", "Práctica de pruebas: **un mes**"],
         "Al formular el pliego, el Instructor propone mantener o levantar la **suspensión provisional** (35.2)."))}

{unidad("6.3 Vista del expediente, propuesta de resolución y resolución (arts. 41 a 45)",
  lit("RD33", "a41", ["en el plazo de diez días", "Se facilitará copia completa del expediente"]),
  lit("RD33", "a42", ["dentro de los diez días siguientes la propuesta de resolución"]),
  lit("RD33", "a43", ["en el plazo de diez días"]),
  lit("RD33", "a44", ["se remitirá con carácter inmediato el expediente completo"]),
  lit("RD33", "a45", ["en el plazo de diez días, salvo en caso de separación del servicio", "no se podrán aceptar hechos distintos de los que sirvieron de base al pliego de cargos"]),
  fichab("Fase final del procedimiento",
         "Instructor (vista y propuesta); órgano que acordó la incoación (remisión); órgano competente (resolución)",
         ["Vista del expediente al inculpado, con copia completa si la pide (41)", "Propuesta de resolución: hechos, valoración jurídica, falta, responsabilidad y sanción (42)", "Notificación de la propuesta y alegaciones (43)", "Remisión del expediente al órgano competente (44)", "Resolución **motivada**, sin hechos distintos de los del pliego y la propuesta (45)"],
         ["Vista: **diez días** para alegar", "Propuesta: dentro de los **diez días** siguientes", "Alegaciones a la propuesta: **diez días**", "Resolución: **diez días**, salvo separación del servicio"],
         "La resolución no puede aceptar **hechos distintos** de los del pliego y la propuesta, aunque sí una **distinta valoración jurídica**."))}

{unidad("6.4 Órganos competentes para sancionar, ejecución y anotación (arts. 47, 49 y 51)",
  lit("RD33", "a47", ["El Consejo de Ministros", "para imponer la separación del servicio", "Los Ministros y Secretarios de Estado", "para la imposición de las sanciones de los apartados d) y e) del artículo 14"]),
  lit("RD33", "a49", ["en el plazo máximo de un mes"]),
  lit("RD33", "a51", ["Registro Central de Personal", "En ningún caso se computarán a efectos de reincidencia las sanciones canceladas"]),
  fichab("Quién sanciona en la AGE y qué ocurre después",
         ["Separación del servicio: **Consejo de Ministros**, a propuesta del Ministro de la Presidencia, oída la Comisión Superior de Personal", "Suspensión y traslado (art. 14 b y c): **Ministros y Secretarios de Estado** del Departamento, o Subsecretarios por delegación", "Sanciones de las letras d) y e) del art. 14: **Subsecretario** (en todo caso), Directores generales y Delegados del Gobierno o Gobernadores civiles"],
         ["Ejecución en los términos de la resolución (49)", "Anotación en el **Registro Central de Personal**, con indicación de las faltas (51)"],
         "Ejecución: máximo **un mes**, salvo que la resolución fije otro plazo por causas justificadas",
         "La **separación** la impone el **Consejo de Ministros**. Las sanciones **canceladas** (o que hubieran podido serlo) no cuentan para la **reincidencia**. Las denominaciones de órganos son las del texto de 1986."))}
""", 2)

T.ap("s17", "IV.7 Cuadro del régimen disciplinario (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Falta | Dónde se tipifica | Sanciones posibles (funcionarios AGE) | Prescribe la falta | Prescribe la sanción |
|---|---|---|---|---|
| Muy grave | TREBEP, art. 95.2 (y leyes) | Separación del servicio; suspensión firme de 3 a 6 años; traslado con cambio de residencia | 3 años | 3 años |
| Grave | Ley (art. 95.3); en la AGE, RD 33/1986, art. 7 | Suspensión hasta 3 años; traslado con cambio de residencia | 2 años | 2 años |
| Leve | Leyes de Función Pública (art. 95.4); en la AGE, RD 33/1986, art. 8 | Apercibimiento | 6 meses | 1 año |

| Trámite (RD 33/1986) | Plazo |
|---|---|
| Pliego de cargos desde la incoación | No más de 1 mes |
| Contestación al pliego | 10 días |
| Práctica de pruebas | 1 mes |
| Vista del expediente | 10 días |
| Propuesta de resolución | 10 días siguientes |
| Alegaciones a la propuesta | 10 días |
| Resolución | 10 días (salvo separación) |
| Ejecución de la sanción | Máximo 1 mes |
| Suspensión provisional (TREBEP, art. 98.3) | Máximo 6 meses |

{resumen([
  "Responden funcionarios y laborales, y también quien **induce** y quien **encubre** faltas muy graves o graves con daño grave (93). Principios: legalidad y tipicidad, irretroactividad, proporcionalidad, culpabilidad y presunción de inocencia (94).",
  "Faltas **muy graves**: lista del art. 95.2; **graves**: por ley (en la AGE, art. 7 RD 33/1986); **leves**: leyes de Función Pública (en la AGE, art. 8).",
  "Sanciones: separación (solo muy graves), despido, suspensión firme (máx. **6 años**), traslado forzoso, **demérito**, apercibimiento (96).",
  "Prescripción: faltas **3 años / 2 años / 6 meses**; sanciones **3 / 2 / 1 año** (97). Suspensión provisional: máximo **6 meses**, cobrando las básicas (98)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_L64 = examen("L", 64, {
  "a": f"La revocación del nombramiento es el efecto de la **separación del servicio** para los interinos: {c(TB, 'Artículo 96', 'que en el caso de los funcionarios interinos comportará la revocación de su nombramiento')} (art. 96.1 a).",
  "b": f"La inhabilitación acompaña al **despido disciplinario** del personal laboral: {c(TB, 'Artículo 96', 'comportará la inhabilitación para ser titular de un nuevo contrato de trabajo con funciones similares')} (art. 96.1 b).",
  "c": f"El art. 96.1 c) habla de {c(TB, 'Artículo 96', 'Suspensión firme de funciones, o de empleo y sueldo en el caso del personal laboral')}: es otra sanción, no el demérito.",
  "d": f"Literal del art. 96.1 e): {c(TB, 'Artículo 96', 'Demérito, que consistirá en la penalización a efectos de carrera, promoción o movilidad voluntaria')}."},
  [("movilidad voluntaria", TB, "Artículo 96", "Demérito, que consistirá en la penalización a efectos de carrera, promoción o movilidad voluntaria")])
EX_X68 = examen("X", 68, {
  "a": f"Es un derecho **individual** del art. 14: {c(TB, 'Artículo 14', 'p) A la libre asociación profesional')}.",
  "b": f"Literal del art. 15: {c(TB, 'Artículo 15', 'derechos individuales que se ejercen de forma colectiva')}: {c(TB, 'Artículo 15', 'a) A la libertad sindical')}.",
  "c": f"Es el derecho individual del art. 14 e): {c(TB, 'Artículo 14', 'A participar en la consecución de los objetivos atribuidos a la unidad donde preste sus servicios')}.",
  "d": f"Es el derecho individual del art. 14 f): {c(TB, 'Artículo 14', 'A la defensa jurídica y protección de la Administración Pública')}."},
  [("libertad sindical", TB, "Artículo 15", "A la libertad sindical")])
EX_P24 = examen("P", 24, {
  "a": f"Art. 49 a) y c): madre biológica, {c(TB, 'Artículo 49', 'tendrá una duración de diecinueve semanas')}; progenitor diferente de la madre biológica, también diecinueve semanas.",
  "b": f"Veinticuatro semanas no aparece en el art. 49; en monoparentalidad son {c(TB, 'Artículo 49', 'treinta y dos semanas')}.",
  "c": "Dieciséis semanas no es la duración que fija el art. 49 vigente: son diecinueve.",
  "d": "Diecisiete semanas no es la duración que fija el art. 49 vigente: son diecinueve."},
  [("19 semanas", TB, "Artículo 49", "Permiso por nacimiento para la madre biológica: tendrá una duración de diecinueve semanas")])
EX_X69 = examen("X", 69, {
  "a": f"No es para todos: el art. 48 e) lo reconoce {c(TB, 'Artículo 48', 'por las funcionarias embarazadas')}.",
  "b": f"No es para todas las funcionarias, sino para las **embarazadas** ({c(TB, 'Artículo 48', 'por las funcionarias embarazadas')}).",
  "c": f"Mezcla la fórmula del permiso de **lactancia**, que es justo lo contrario: {c(TB, 'Artículo 48', 'sin que pueda transferirse su ejercicio al otro progenitor, adoptante, guardador o acogedor')} (art. 48 f).",
  "d": f"Literal del art. 48 e): {c(TB, 'Artículo 48', 'por las funcionarias embarazadas')}, y {c(TB, 'Artículo 48', 'el término de funcionarias embarazadas incluye también a las personas funcionarias trans gestantes')}."},
  [("funcionarias embarazadas", TB, "Artículo 48", "por las funcionarias embarazadas"), ("trans gestantes", TB, "Artículo 48", "incluye también a las personas funcionarias trans gestantes")])

T.ap("s18", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **dos** preguntas asignadas a este tema (sanción de demérito y derechos ejercidos colectivamente) y **dos** relacionadas sin tema asignado (duración del permiso por nacimiento y permiso para exámenes prenatales). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-L 2025, pregunta 64 · Sanción de demérito (→ IV.3.1)", EX_L64,
  "### GACE-L 2025 extraordinario, pregunta 68 · Derechos individuales ejercidos colectivamente (→ I.2.1)", EX_X68,
  "### GACE-P 2025, pregunta 24 · Permiso por nacimiento (relacionada; → II.3.1)", EX_P24,
  "### GACE-L 2025 extraordinario, pregunta 69 · Permiso para exámenes prenatales (relacionada; → II.2.2)", EX_X69,
  "### Cómo se pregunta",
  "!> Las preguntas de este tema usan como distractores **otros apartados del mismo artículo**: las demás sanciones del art. 96, los derechos del art. 14 frente a los del art. 15, la fórmula de otro permiso del art. 48. Saber **qué dice cada letra** resuelve la pregunta.",
]))

T.ap("s19", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Derechos | Individuales (14, a-q); individuales ejercidos colectivamente (15); promoción profesional (16.1, 19.1); evaluación del desempeño (20) | **Libertad sindical** = art. 15; **libre asociación profesional** = art. 14 p) |
| II. Jornada, permisos y vacaciones | Jornada que fija cada Administración (47); teletrabajo (47 bis); permisos (48 y 49); vacaciones (50) | **19 semanas** (32 monoparental); asuntos particulares **6**; matrimonio **15**; vacaciones **22 días hábiles** |
| III. Deberes | Art. 52 (diligencia y 15 principios); principios éticos (53); principios de conducta (54) | Obediencia **salvo infracción manifiesta**; regalos solo de **cortesía** |
| IV. Régimen disciplinario | Responsabilidad (93), principios (94), faltas (95), sanciones (96), prescripción (97), procedimiento (98); RD 33/1986 en la AGE | **Demérito** = carrera, promoción o movilidad voluntaria; prescripción **3/2/6 meses** y **3/2/1 año** |

?> **Trampas frecuentes:** «la libre asociación profesional es un derecho ejercido colectivamente» (es **individual**, art. 14 p); «el permiso por nacimiento es de 16 semanas» (son **19**); «los sábados son hábiles para las vacaciones» (**no** lo son); «la falta leve prescribe al año» (prescribe a los **seis meses**; es la **sanción** por falta leve la que prescribe al año); «la suspensión provisional puede durar un año» (máximo **seis meses**, salvo paralización imputable al interesado); «la separación del servicio cabe por faltas graves» (solo **muy graves**).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
Q = T.q
Q(TB, "Artículo 15", "Derechos", "Según el artículo 15 del TREBEP, ¿cuál de los siguientes es un derecho individual que se ejerce de forma colectiva?",
  ["Al planteamiento de conflictos colectivos de trabajo.", "A la libre asociación profesional.", "A la formación continua.", "A la libertad de expresión."],
  "Art. 15 d) TREBEP. La libre asociación profesional (p), la formación (g) y la libertad de expresión (k) son derechos individuales del art. 14.", "Al planteamiento de conflictos colectivos de trabajo")
Q(TB, "Artículo 15", "Derechos", "Según el artículo 15 c) del TREBEP, el derecho al ejercicio de la huelga se reconoce:",
  ["Con la garantía del mantenimiento de los servicios esenciales de la comunidad.", "Sin límite alguno.", "Solo al personal laboral.", "Previa autorización de la Administración."],
  "Art. 15 c) TREBEP.", "Al ejercicio de la huelga, con la garantía del mantenimiento de los servicios esenciales de la comunidad")
Q(TB, "Artículo 14", "Derechos", "Según el artículo 14 a) del TREBEP, la inamovilidad es un derecho individual que se predica:",
  ["De la condición de funcionario de carrera.", "Del puesto de trabajo obtenido por concurso.", "De la localidad de destino.", "De todo el personal laboral fijo."],
  "Art. 14 a) TREBEP: «A la inamovilidad en la condición de funcionario de carrera».", "A la inamovilidad en la condición de funcionario de carrera")
Q(TB, "Artículo 14", "Derechos", "Según el artículo 14 g) del TREBEP, la formación continua y la actualización permanente de conocimientos se realizará:",
  ["Preferentemente en horario laboral.", "Exclusivamente fuera del horario laboral.", "Solo a petición del superior jerárquico.", "Únicamente en los centros de formación del Estado."],
  "Art. 14 g) TREBEP.", "preferentemente en horario laboral")
Q(TB, "Artículo 14", "Derechos", "Según el artículo 14 f) del TREBEP, los empleados públicos tienen derecho a la defensa jurídica y protección de la Administración en los procedimientos que se sigan:",
  ["Ante cualquier orden jurisdiccional como consecuencia del ejercicio legítimo de sus funciones o cargos públicos.", "Solo ante el orden penal.", "Solo ante el orden contencioso-administrativo.", "En cualquier procedimiento judicial, aunque no traiga causa de sus funciones."],
  "Art. 14 f) TREBEP.", "ante cualquier orden jurisdiccional como consecuencia del ejercicio legítimo de sus funciones o cargos públicos")
Q(TB, "Artículo 20", "Derechos", "Según el artículo 20 del TREBEP, la evaluación del desempeño es el procedimiento mediante el cual se mide y valora:",
  ["La conducta profesional y el rendimiento o el logro de resultados.", "Exclusivamente la antigüedad del empleado.", "Los méritos académicos del empleado.", "La adecuación del puesto a la relación de puestos de trabajo."],
  "Art. 20.1 TREBEP.", "se mide y valora la conducta profesional y el rendimiento o el logro de resultados")
Q(TB, "Artículo 20", "Derechos", "Según el artículo 20.2 del TREBEP, los sistemas de evaluación del desempeño se adecuarán, en todo caso, a criterios de:",
  ["Transparencia, objetividad, imparcialidad y no discriminación.", "Jerarquía, antigüedad y confianza.", "Publicidad, concurrencia y libre designación.", "Eficacia, eficiencia y economía."],
  "Art. 20.2 TREBEP.", "transparencia, objetividad, imparcialidad y no discriminación")
Q(TB, "Artículo 47", "Jornada y permisos", "Según el artículo 47.2 del TREBEP, las Administraciones adoptarán medidas de flexibilización horaria para los empleados públicos que tengan a su cargo hijos e hijas menores de:",
  ["Doce años.", "Ocho años.", "Seis años.", "Catorce años."], "Art. 47.2 TREBEP.", "hijos e hijas menores de doce años")
Q(TB, "Artículo 47 bis", "Jornada y permisos", "Según el artículo 47 bis del TREBEP, la prestación del servicio mediante teletrabajo:",
  ["Habrá de ser expresamente autorizada y tendrá carácter voluntario y reversible, salvo supuestos excepcionales debidamente justificados.", "Será obligatoria cuando lo decida el superior jerárquico.", "Se entenderá autorizada por silencio administrativo.", "Excluye la modalidad presencial durante el año natural."],
  "Art. 47 bis.2 TREBEP.", "habrá de ser expresamente autorizada y será compatible con la modalidad presencial")
Q(TB, "Artículo 48", "Jornada y permisos", "Según el artículo 48 a) del TREBEP, por fallecimiento del cónyuge cuando el suceso se produzca en distinta localidad, el permiso será de:",
  ["Cinco días hábiles.", "Tres días hábiles.", "Cuatro días naturales.", "Dos días hábiles."],
  "Art. 48 a) TREBEP: tres días hábiles en la misma localidad y cinco en distinta localidad.", "tres días hábiles cuando el suceso se produzca en la misma localidad, y cinco días hábiles, cuando sea en distinta localidad")
Q(TB, "Artículo 48", "Jornada y permisos", "Según el artículo 48 a) del TREBEP, por enfermedad grave de un familiar dentro del segundo grado de consanguinidad o afinidad, el permiso será de:",
  ["Cuatro días hábiles.", "Cinco días hábiles.", "Dos días hábiles.", "Tres días naturales."],
  "Art. 48 a) TREBEP, párrafo segundo.", "de un familiar dentro del segundo grado de consanguinidad o afinidad, el permiso será de cuatro días hábiles")
Q(TB, "Artículo 48", "Jornada y permisos", "Según el artículo 48 k) del TREBEP, por asuntos particulares los funcionarios tendrán:",
  ["Seis días al año.", "Tres días al año.", "Ocho días al año.", "Diez días al año."], "Art. 48 k) TREBEP.", "Por asuntos particulares, seis días al año")
Q(TB, "Artículo 48", "Jornada y permisos", "Según el artículo 48 l) del TREBEP, por matrimonio o registro o constitución formalizada por documento público de pareja de hecho, el permiso será de:",
  ["Quince días.", "Diez días.", "Veinte días.", "Siete días."], "Art. 48 l) TREBEP.", "pareja de hecho, quince días")
Q(TB, "Artículo 48", "Jornada y permisos", "Según el artículo 48 f) del TREBEP, por lactancia de un hijo menor de doce meses se tendrá derecho a:",
  ["Una hora de ausencia del trabajo, que podrá dividirse en dos fracciones.", "Dos horas diarias de ausencia retribuida.", "Media hora de ausencia, no divisible.", "Una reducción de jornada del cincuenta por ciento."],
  "Art. 48 f) TREBEP.", "una hora de ausencia del trabajo que podrá dividir en dos fracciones")
Q(TB, "Artículo 48", "Jornada y permisos", "Según el artículo 48 f) del TREBEP, el permiso por lactancia:",
  ["Constituye un derecho individual de los funcionarios, sin que pueda transferirse su ejercicio al otro progenitor.", "Puede cederse libremente al otro progenitor.", "Solo corresponde a la madre biológica.", "Se extingue cuando el hijo cumple seis meses."],
  "Art. 48 f) TREBEP, párrafo segundo.", "constituye un derecho individual de los funcionarios, sin que pueda transferirse su ejercicio al otro progenitor")
Q(TB, "Artículo 48", "Jornada y permisos", "Según el artículo 48 i) del TREBEP, para atender el cuidado de un familiar de primer grado por enfermedad muy grave, el funcionario podrá solicitar una reducción de jornada:",
  ["De hasta el cincuenta por ciento, con carácter retribuido, por el plazo máximo de un mes.", "De hasta el cincuenta por ciento, sin retribución, por el plazo máximo de tres meses.", "De hasta un tercio, con carácter retribuido, sin límite temporal.", "Del cien por cien, con carácter retribuido, por el plazo máximo de quince días."],
  "Art. 48 i) TREBEP.", "una reducción de hasta el cincuenta por ciento de la jornada laboral, con carácter retribuido, por razones de enfermedad muy grave y por el plazo máximo de un mes")
Q(TB, "Artículo 48", "Jornada y permisos", "Según el artículo 48 g) del TREBEP, por nacimiento de hijos prematuros que deban permanecer hospitalizados a continuación del parto, el funcionario tendrá derecho a ausentarse del trabajo:",
  ["Durante un máximo de dos horas diarias percibiendo las retribuciones íntegras.", "Durante un máximo de una hora diaria sin retribución.", "Durante toda la jornada mientras dure la hospitalización.", "Durante un máximo de cuatro horas diarias con disminución proporcional de retribuciones."],
  "Art. 48 g) TREBEP.", "durante un máximo de dos horas diarias percibiendo las retribuciones íntegras")
Q(TB, "Artículo 49", "Jornada y permisos", "Según el artículo 49 a) del TREBEP, en el supuesto de monoparentalidad, el permiso por nacimiento para la madre biológica será de:",
  ["Treinta y dos semanas.", "Diecinueve semanas.", "Veinticuatro semanas.", "Treinta y ocho semanas."], "Art. 49 a) TREBEP.", "En el supuesto de monoparentalidad, por existir una única persona progenitora, el permiso será de treinta y dos semanas")
Q(TB, "Artículo 49", "Jornada y permisos", "Según el artículo 49 a) del TREBEP, del permiso por nacimiento para la madre biológica serán obligatorias y habrán de disfrutarse a jornada completa:",
  ["Seis semanas ininterrumpidas inmediatamente posteriores al parto.", "Cuatro semanas ininterrumpidas anteriores al parto.", "Diez semanas ininterrumpidas posteriores al parto.", "Dos semanas ininterrumpidas posteriores al parto."],
  "Art. 49 a) 1.º TREBEP.", "Seis semanas ininterrumpidas inmediatamente posteriores al parto, serán obligatorias y habrán de disfrutarse a jornada completa")
Q(TB, "Artículo 49", "Jornada y permisos", "Según el artículo 49 b) del TREBEP, si en la adopción internacional fuera necesario el desplazamiento previo de los progenitores al país de origen del adoptado, se tendrá derecho además a un permiso:",
  ["De hasta dos meses, percibiendo exclusivamente las retribuciones básicas.", "De hasta dos meses, con retribuciones íntegras.", "De hasta seis meses, sin retribución.", "De hasta un mes, percibiendo exclusivamente las retribuciones complementarias."],
  "Art. 49 b) TREBEP.", "un permiso de hasta dos meses de duración, percibiendo durante este periodo exclusivamente las retribuciones básicas")
Q(TB, "Artículo 49", "Jornada y permisos", "Según el artículo 49 d) del TREBEP, la funcionaria víctima de violencia sobre la mujer o de violencia sexual mantendrá sus retribuciones íntegras cuando reduzca su jornada en:",
  ["Un tercio o menos.", "La mitad o menos.", "Un cuarto o menos.", "Dos tercios o menos."], "Art. 49 d) TREBEP.", "mantendrá sus retribuciones íntegras cuando reduzca su jornada en un tercio o menos")
Q(TB, "Artículo 49", "Jornada y permisos", "Según el artículo 49 g) del TREBEP, el permiso parental para el cuidado de hijo, hija o menor acogido hasta que cumpla ocho años:",
  ["No tendrá carácter retribuido y tendrá una duración no superior a ocho semanas.", "Será retribuido y tendrá una duración de ocho semanas.", "No será retribuido y durará hasta doce semanas.", "Será retribuido al cincuenta por ciento y durará cuatro semanas."],
  "Art. 49 g) TREBEP.", "no tendrá carácter retribuido y tendrá una duración no superior a ocho semanas")
Q(TB, "Artículo 49", "Jornada y permisos", "Según el artículo 49 e) del TREBEP, el permiso por cuidado de hijo menor afectado por cáncer u otra enfermedad grave da derecho a una reducción de la jornada:",
  ["De al menos la mitad de su duración, percibiendo las retribuciones íntegras.", "De hasta un tercio, con disminución proporcional de retribuciones.", "De al menos la mitad, sin retribución.", "Del cien por cien, con las retribuciones básicas."],
  "Art. 49 e) TREBEP.", "una reducción de la jornada de trabajo de al menos la mitad de la duración de aquélla, percibiendo las retribuciones íntegras")
Q(TB, "Artículo 50", "Jornada y permisos", "Según el artículo 50 del TREBEP, los funcionarios públicos tendrán derecho a disfrutar, durante cada año natural, de unas vacaciones retribuidas de:",
  ["Veintidós días hábiles.", "Treinta días hábiles.", "Veintidós días naturales.", "Un mes natural."], "Art. 50.1 TREBEP.", "vacaciones retribuidas de veintidós días hábiles")
Q(TB, "Artículo 50", "Jornada y permisos", "Según el artículo 50 del TREBEP, a efectos de vacaciones:",
  ["No se considerarán como días hábiles los sábados, sin perjuicio de las adaptaciones para los horarios especiales.", "Los sábados se consideran días hábiles en todo caso.", "Los domingos se consideran días hábiles.", "Solo son hábiles los días de lunes a jueves."],
  "Art. 50.1 TREBEP, párrafo segundo.", "no se considerarán como días hábiles los sábados")
Q(TB, "Artículo 50", "Jornada y permisos", "Según el artículo 50.2 del TREBEP, si una incapacidad temporal impide iniciar las vacaciones dentro del año natural, podrán disfrutarse siempre que no hayan transcurrido más de:",
  ["Dieciocho meses a partir del final del año en que se hayan originado.", "Doce meses a partir del final del año en que se hayan originado.", "Seis meses a partir del alta médica.", "Veinticuatro meses desde el inicio de la incapacidad."],
  "Art. 50.2 TREBEP.", "no hayan transcurrido más de dieciocho meses a partir del final del año en que se hayan originado")
Q(TB, "Artículo 52", "Deberes", "Según el artículo 52 del TREBEP, los principios y reglas del Código de Conducta:",
  ["Informarán la interpretación y aplicación del régimen disciplinario de los empleados públicos.", "Carecen de relevancia en el régimen disciplinario.", "Solo se aplican al personal directivo.", "Sustituyen a las faltas tipificadas en la ley."],
  "Art. 52, párrafo segundo, TREBEP.", "informarán la interpretación y aplicación del régimen disciplinario de los empleados públicos")
Q(TB, "Artículo 54", "Deberes", "Según el artículo 54.3 del TREBEP, los empleados públicos obedecerán las instrucciones y órdenes profesionales de los superiores, salvo que constituyan:",
  ["Una infracción manifiesta del ordenamiento jurídico.", "Una orden verbal.", "Una instrucción no publicada en el BOE.", "Una orden que el empleado considere inoportuna."],
  "Art. 54.3 TREBEP: en ese caso, la pondrán inmediatamente en conocimiento de los órganos de inspección procedentes.", "salvo que constituyan una infracción manifiesta del ordenamiento jurídico")
Q(TB, "Artículo 54", "Deberes", "Según el artículo 54.6 del TREBEP, se rechazará cualquier regalo, favor o servicio en condiciones ventajosas que vaya más allá de:",
  ["Los usos habituales, sociales y de cortesía.", "Un valor de cien euros.", "Lo autorizado por el superior jerárquico.", "Lo declarado en el registro de intereses."],
  "Art. 54.6 TREBEP.", "que vaya más allá de los usos habituales, sociales y de cortesía")
Q(TB, "Artículo 53", "Deberes", "Según el artículo 53.12 del TREBEP, sobre los asuntos que conozcan por razón de su cargo, los empleados públicos mantendrán:",
  ["La debida discreción.", "Secreto absoluto en todo caso.", "Plena publicidad.", "Reserva solo durante su servicio activo."],
  "Art. 53.12 TREBEP: secreto de las materias clasificadas o de difusión prohibida; discreción sobre lo conocido por razón del cargo.", "mantendrán la debida discreción sobre aquellos asuntos que conozcan por razón de su cargo")
Q(TB, "Artículo 93", "Régimen disciplinario", "Según el artículo 93.3 del TREBEP, incurrirán en responsabilidad los que encubrieren las faltas consumadas muy graves o graves:",
  ["Cuando de dichos actos se derive daño grave para la Administración o los ciudadanos.", "En todo caso.", "Solo si son superiores jerárquicos del autor.", "Solo cuando la falta sea leve."],
  "Art. 93.3 TREBEP.", "cuando de dichos actos se derive daño grave para la Administración o los ciudadanos")
Q(TB, "Artículo 94", "Régimen disciplinario", "Según el artículo 94.3 del TREBEP, cuando de la instrucción de un procedimiento disciplinario resulte la existencia de indicios fundados de criminalidad:",
  ["Se suspenderá su tramitación poniéndolo en conocimiento del Ministerio Fiscal.", "Se continuará su tramitación hasta la resolución.", "Se archivará definitivamente el expediente.", "Se remitirá al Tribunal de Cuentas."],
  "Art. 94.3 TREBEP.", "se suspenderá su tramitación poniéndolo en conocimiento del Ministerio Fiscal")
Q(TB, "Artículo 95", "Régimen disciplinario", "Según el artículo 95.2 del TREBEP, es falta muy grave:",
  ["La desobediencia abierta a las órdenes o instrucciones de un superior, salvo que constituyan infracción manifiesta del Ordenamiento jurídico.", "La falta de asistencia injustificada de un día.", "La incorrección con el público.", "El descuido o negligencia en el ejercicio de sus funciones."],
  "Art. 95.2 i) TREBEP. Las demás son faltas leves en la AGE (art. 8 RD 33/1986).", "La desobediencia abierta a las órdenes o instrucciones de un superior")
Q(TB, "Artículo 95", "Régimen disciplinario", "Según el artículo 95.3 del TREBEP, las faltas graves serán establecidas:",
  ["Por ley de las Cortes Generales o de la asamblea legislativa de la correspondiente comunidad autónoma o por los convenios colectivos en el caso de personal laboral.", "Por orden ministerial.", "Por el propio TREBEP en una lista cerrada.", "Por acuerdo de la Mesa General de Negociación."],
  "Art. 95.3 TREBEP.", "Las faltas graves serán establecidas por ley de las Cortes Generales o de la asamblea legislativa")
Q(TB, "Artículo 96", "Régimen disciplinario", "Según el artículo 96.1 c) del TREBEP, la suspensión firme de funciones tendrá una duración máxima de:",
  ["6 años.", "3 años.", "6 meses.", "2 años."], "Art. 96.1 c) TREBEP.", "con una duración máxima de 6 años")
Q(TB, "Artículo 96", "Régimen disciplinario", "Según el artículo 96.1 a) del TREBEP, la separación del servicio de los funcionarios:",
  ["Sólo podrá sancionar la comisión de faltas muy graves.", "Podrá sancionar faltas graves y muy graves.", "Podrá imponerse por la reiteración de faltas leves.", "Solo se aplica a los funcionarios interinos."],
  "Art. 96.1 a) TREBEP.", "que sólo podrá sancionar la comisión de faltas muy graves")
Q(TB, "Artículo 97", "Régimen disciplinario", "Según el artículo 97 del TREBEP, las faltas leves prescribirán a:",
  ["Los seis meses.", "Al año.", "Al mes.", "Los dos años."], "Art. 97.1 TREBEP. Al año prescriben las sanciones impuestas por faltas leves.", "las leves a los seis meses")
Q(TB, "Artículo 97", "Régimen disciplinario", "Según el artículo 97 del TREBEP, las sanciones impuestas por faltas leves prescribirán:",
  ["Al año.", "A los seis meses.", "Al mes.", "A los tres años."], "Art. 97.1 TREBEP.", "las impuestas por faltas leves al año")
Q(TB, "Artículo 97", "Régimen disciplinario", "Según el artículo 97.2 del TREBEP, en las faltas continuadas el plazo de prescripción comenzará a contarse:",
  ["Desde el cese de su comisión.", "Desde que se cometió el primer acto.", "Desde la incoación del expediente.", "Desde que la Administración tuvo conocimiento de la falta."],
  "Art. 97.2 TREBEP.", "desde el cese de su comisión cuando se trate de faltas continuadas")
Q(TB, "Artículo 98", "Régimen disciplinario", "Según el artículo 98.3 del TREBEP, la suspensión provisional como medida cautelar en la tramitación de un expediente disciplinario no podrá exceder de:",
  ["6 meses, salvo en caso de paralización del procedimiento imputable al interesado.", "1 año, en todo caso.", "3 meses, prorrogables por otros tres.", "6 años."], "Art. 98.3 TREBEP.", "no podrá exceder de 6 meses, salvo en caso de paralización del procedimiento imputable al interesado")
Q(TB, "Artículo 98", "Régimen disciplinario", "Según el artículo 98.3 del TREBEP, el funcionario suspenso provisional tendrá derecho a percibir durante la suspensión:",
  ["Las retribuciones básicas y, en su caso, las prestaciones familiares por hijo a cargo.", "Las retribuciones íntegras.", "Solo las retribuciones complementarias.", "Ninguna retribución."], "Art. 98.3 TREBEP.", "las retribuciones básicas y, en su caso, las prestaciones familiares por hijo a cargo")
Q(TB, "Artículo 98", "Régimen disciplinario", "Según el artículo 98.2 del TREBEP, en el procedimiento disciplinario la fase instructora y la sancionadora:",
  ["Se encomendarán a órganos distintos.", "Se encomendarán al mismo órgano.", "Se encomendarán al superior jerárquico directo.", "Se tramitarán ante la jurisdicción contencioso-administrativa."],
  "Art. 98.2 TREBEP.", "la debida separación entre la fase instructora y la sancionadora, encomendándose a órganos distintos")
Q("RD33", "a7", "Régimen disciplinario", "Según el artículo 7 del Real Decreto 33/1986, es falta grave el incumplimiento injustificado de la jornada de trabajo que acumulado suponga un mínimo de:",
  ["Diez horas al mes.", "Cinco horas al mes.", "Veinte horas al trimestre.", "Diez horas a la semana."], "Art. 7.1 l) RD 33/1986.", "un mínimo de diez horas al mes")
Q("RD33", "a35", "Régimen disciplinario", "Según el artículo 35 del Real Decreto 33/1986, el Instructor formulará el pliego de cargos en un plazo no superior a:",
  ["Un mes, contado a partir de la incoación del procedimiento.", "Diez días desde la incoación.", "Tres meses desde la denuncia.", "Quince días desde la declaración del inculpado."],
  "Art. 35.1 RD 33/1986.", "en un plazo no superior a un mes, contados a partir de la incoación del procedimiento")
Q("RD33", "a47", "Régimen disciplinario", "Según el artículo 47 del Real Decreto 33/1986, el órgano competente para imponer la sanción de separación del servicio es:",
  ["El Consejo de Ministros.", "El Subsecretario del Departamento.", "El Director general del que dependa el funcionario.", "El Secretario de Estado de Función Pública."],
  "Art. 47.1 RD 33/1986.", "El Consejo de Ministros, a propuesta del Ministro de la Presidencia")
T.real("L", 64, "Régimen disciplinario"); T.real("X", 68, "Derechos"); T.real("P", 24, "Jornada y permisos"); T.real("X", 69, "Jornada y permisos")

# Flashcards
for q_, a_, cat in [
  ("¿Qué distingue los arts. 14 y 15 del TREBEP?", "El 14 recoge derechos individuales; el 15, derechos individuales que se ejercen de forma colectiva.", "Derechos"),
  ("Derechos individuales ejercidos colectivamente (art. 15)", "Libertad sindical; negociación colectiva y participación; huelga con servicios esenciales; conflictos colectivos; reunión (art. 46).", "Derechos"),
  ("¿La libre asociación profesional es del art. 14 o del 15?", "Del art. 14 p): derecho individual.", "Derechos"),
  ("Evaluación del desempeño (art. 20)", "Procedimiento que mide y valora la conducta profesional y el rendimiento o el logro de resultados; criterios de transparencia, objetividad, imparcialidad y no discriminación.", "Derechos"),
  ("Teletrabajo (art. 47 bis)", "Expresamente autorizado, compatible con la modalidad presencial, voluntario y reversible salvo supuestos excepcionales justificados.", "Jornada y permisos"),
  ("Permiso por enfermedad grave de familiar (art. 48 a)", "Primer grado, cónyuge, pareja o conviviente: 5 días hábiles; segundo grado: 4 días hábiles.", "Jornada y permisos"),
  ("Permiso por fallecimiento (art. 48 a)", "Cónyuge, pareja o primer grado: 3 días hábiles (misma localidad) o 5 (distinta); segundo grado: 2 o 4.", "Jornada y permisos"),
  ("Asuntos particulares y matrimonio (art. 48 k y l)", "Seis días al año; quince días por matrimonio o pareja de hecho formalizada.", "Jornada y permisos"),
  ("Lactancia (art. 48 f)", "Hijo menor de doce meses: una hora de ausencia, divisible en dos fracciones; acumulable en jornadas completas; derecho individual intransferible.", "Jornada y permisos"),
  ("Permiso por nacimiento, adopción o del progenitor diferente (art. 49 a, b y c)", "Diecinueve semanas; treinta y dos en monoparentalidad; seis semanas obligatorias.", "Jornada y permisos"),
  ("Permiso parental (art. 49 g)", "Hasta ocho semanas, no retribuido, hasta que el menor cumpla ocho años; preaviso de quince días.", "Jornada y permisos"),
  ("Vacaciones (art. 50)", "Veintidós días hábiles por año natural; sábados no hábiles; no sustituibles por dinero salvo cese por causas ajenas a la voluntad; límite de 18 meses si IT, riesgo o maternidad impiden disfrutarlas.", "Jornada y permisos"),
  ("¿Qué forman los arts. 53 y 54 del TREBEP?", "El Código de Conducta: principios éticos (53) y principios de conducta (54).", "Deberes"),
  ("Obediencia (art. 54.3)", "Se obedecen las órdenes profesionales salvo infracción manifiesta del ordenamiento; entonces se comunica inmediatamente a los órganos de inspección.", "Deberes"),
  ("Principios de la potestad disciplinaria (art. 94.2)", "Legalidad y tipicidad; irretroactividad de lo desfavorable y retroactividad de lo favorable; proporcionalidad; culpabilidad; presunción de inocencia.", "Régimen disciplinario"),
  ("Sanciones del art. 96 TREBEP", "Separación del servicio; despido disciplinario; suspensión firme (máx. 6 años); traslado forzoso; demérito; apercibimiento; otras por ley.", "Régimen disciplinario"),
  ("Demérito (art. 96.1 e)", "Penalización a efectos de carrera, promoción o movilidad voluntaria.", "Régimen disciplinario"),
  ("Prescripción (art. 97)", "Faltas: muy graves 3 años, graves 2, leves 6 meses. Sanciones: 3 años, 2 años y 1 año.", "Régimen disciplinario"),
  ("Suspensión provisional (art. 98.3)", "Máximo 6 meses en el expediente (salvo paralización imputable al interesado); se perciben las retribuciones básicas y prestaciones familiares por hijo a cargo.", "Régimen disciplinario"),
  ("Faltas leves y sanción en la AGE (RD 33/1986, arts. 8, 17 y 18)", "Sin expediente, pero siempre con audiencia; sanción: apercibimiento (la letra d del art. 14 figura derogada).", "Régimen disciplinario"),
  ("¿Quién impone la separación del servicio en la AGE? (RD 33/1986, art. 47)", "El Consejo de Ministros.", "Régimen disciplinario"),
  ("Plazos del expediente (RD 33/1986)", "Pliego de cargos: ≤ 1 mes desde la incoación; contestación: 10 días; pruebas: 1 mes; vista: 10 días; propuesta: 10 días; resolución: 10 días.", "Régimen disciplinario"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Derechos individuales ejercidos colectivamente", "Los del art. 15 TREBEP: libertad sindical, negociación colectiva, huelga, conflictos colectivos y reunión.", "s2", "Derechos")
T.glos("Evaluación del desempeño", "Procedimiento mediante el cual se mide y valora la conducta profesional y el rendimiento o el logro de resultados (art. 20.1 TREBEP).", "s3", "Derechos")
T.glos("Teletrabajo", "Modalidad de prestación de servicios a distancia, fuera de las dependencias de la Administración, mediante tecnologías de la información y comunicación (art. 47 bis.1 TREBEP).", "s4", "Jornada y permisos")
T.glos("Asuntos particulares", "Permiso de seis días al año del art. 48 k) TREBEP.", "s5", "Jornada y permisos")
T.glos("Permiso parental", "Permiso no retribuido, de hasta ocho semanas, para el cuidado del menor hasta que cumpla ocho años (art. 49 g TREBEP).", "s6", "Jornada y permisos")
T.glos("Código de Conducta", "Conjunto de principios éticos (art. 53) y de conducta (art. 54) de los empleados públicos; informa el régimen disciplinario (art. 52 TREBEP).", "s8", "Deberes")
T.glos("Falta muy grave", "Infracción disciplinaria de las letras a) a o) del art. 95.2 TREBEP o tipificada como tal por ley (o convenio, para laborales); prescribe a los tres años.", "s12", "Régimen disciplinario")
T.glos("Demérito", "Sanción consistente en la penalización a efectos de carrera, promoción o movilidad voluntaria (art. 96.1 e TREBEP).", "s13", "Régimen disciplinario")
T.glos("Separación del servicio", "Sanción solo para faltas muy graves; en los interinos comporta la revocación del nombramiento (art. 96.1 a TREBEP).", "s13", "Régimen disciplinario")
T.glos("Prescripción", "Extinción por el transcurso del tiempo: faltas 3 años, 2 años y 6 meses; sanciones 3 años, 2 años y 1 año (art. 97 TREBEP).", "s14", "Régimen disciplinario")
T.glos("Suspensión provisional", "Medida cautelar durante el expediente, de hasta seis meses salvo paralización imputable al interesado, con derecho a las retribuciones básicas (art. 98.3 TREBEP).", "s15", "Régimen disciplinario")
T.glos("Información reservada", "Actuación previa que puede acordar el órgano competente antes de incoar el procedimiento disciplinario (art. 28 RD 33/1986).", "s16", "Régimen disciplinario")
T.glos("Pliego de cargos", "Acto del Instructor con los hechos imputados, la falta presunta y las sanciones aplicables, en el plazo de un mes desde la incoación (art. 35 RD 33/1986).", "s16", "Régimen disciplinario")

# Cronología (fechas de los metadatos del BOE)
T.hito("1986", "Real Decreto 33/1986, de 10 de enero, Reglamento de Régimen Disciplinario de los Funcionarios de la Administración del Estado (BOE de 17-1-1986)", "Faltas graves y leves, sanciones y procedimiento en la AGE", "normativo", "s11")
T.hito("2007", "Ley 7/2007, de 12 de abril, del Estatuto Básico del Empleado Público (BOE de 13-4-2007)", "Primer Estatuto Básico; derogada por el texto refundido de 2015", "normativo", "s1")
T.hito("2015", "Real Decreto Legislativo 5/2015, de 30 de octubre, texto refundido de la Ley del Estatuto Básico del Empleado Público (BOE de 31-10-2015)", "Derechos (14-20), jornada y permisos (47-51), deberes (52-54) y régimen disciplinario (93-98)", "normativo", "s1")
T.hito("2020", "Real Decreto-ley 29/2020, de 29 de septiembre, de medidas urgentes en materia de teletrabajo en las Administraciones Públicas (BOE de 30-9-2020)", "Introduce el art. 47 bis (teletrabajo)", "normativo", "s4")
T.hito("2023", "Ley 4/2023, de 28 de febrero, para la igualdad real y efectiva de las personas trans y para la garantía de los derechos de las personas LGTBI (BOE de 1-3-2023)", "Modifica, entre otros, los arts. 14, 48, 49 y 95 del TREBEP", "normativo", "s5")
T.hito("2024", "Ley 6/2024, de 20 de diciembre, para la mejora de la protección de las personas donantes en vivo de órganos o tejidos (BOE de 21-12-2024)", "Modifica el art. 48 del TREBEP (redacción vigente desde el 3-3-2025)", "normativo", "s5")
T.hito("2025", "Real Decreto-ley 9/2025, de 29 de julio, por el que se amplía el permiso de nacimiento y cuidado (BOE de 30-7-2025)", "Redacción vigente del art. 49 del TREBEP (diecinueve semanas) desde el 31-7-2025", "normativo", "s6")

T.publicar()
