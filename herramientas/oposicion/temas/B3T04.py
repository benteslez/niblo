# -*- coding: utf-8 -*-
"""Tema III.4 (B3T04): La Seguridad Social: estructura y financiación. Problemas actuales y
líneas de actuación. El régimen general y los regímenes especiales. La acción protectora de
la Seguridad Social. Tipos y características de las prestaciones.
Método del I.2. Normas (textos consolidados del BOE): CE, arts. 41, 50, 129.1 y 149.1.17.ª;
texto refundido de la Ley General de la Seguridad Social (RDLeg 8/2015, LGSS). «Problemas
actuales y líneas de actuación»: exposición de motivos de la Ley 21/2021 y del RDL 2/2023
(texto oficial del BOE, no parte dispositiva) y los artículos de la LGSS que las aplican."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO["LGSS"] = "LGSS"
CORTO["L21_2021"] = "Ley 21/2021"
CORTO["RDL2_2023"] = "RDL 2/2023"
NOLEGAL = "*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*"
EM21 = "Ley 21/2021, de 28 de diciembre · preámbulo, apartado {} (exposición de motivos publicada en el BOE; explica la ley, no es parte dispositiva)"
EM23 = "Real Decreto-ley 2/2023, de 16 de marzo · preámbulo, apartado I (exposición de motivos publicada en el BOE; explica la norma, no es parte dispositiva)"

T = Tema("B3T04",
  "Seis preguntas: I. Cómo se organiza la Seguridad Social (CE, arts. 41, 50, 129 y 149.1.17.ª; LGSS, arts. 1 a 4 y 66 a 80) · II. Cómo se financia (LGSS, arts. 18, 109, 110, 117 a 127 bis) · III. Qué problemas tiene y qué líneas de actuación sigue (Ley 21/2021 y RDL 2/2023; LGSS, art. 58) · IV. Qué regímenes la forman (LGSS, arts. 7 a 11, 136, 137 y 305) · V. Qué protege (LGSS, arts. 42, 43, 63, 64 y 155 a 158) · VI. Qué prestaciones da y cómo son (LGSS, arts. 44, 53, 165 y siguientes). Cada artículo: texto literal del BOE y ficha.",
  ["Seguridad Social", "Art. 41 CE", "Art. 149.1.17.ª", "LGSS", "Entidades gestoras", "INSS", "Tesorería General", "Mutuas colaboradoras", "Reparto", "Fondo de Reserva", "MEI", "Pacto de Toledo", "Revalorización", "Régimen General", "Regímenes especiales", "RETA", "Acción protectora", "Accidente de trabajo", "Prestaciones no contributivas", "Jubilación"])

# =============================================================================
T.ap("s0", "Mapa del tema: seis preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque III, tema 4):
> La Seguridad Social: estructura y financiación. Problemas actuales y líneas de actuación. El régimen general y los regímenes especiales. La acción protectora de la Seguridad Social. Tipos y características de las prestaciones.

### El hilo conductor

El epígrafe se lee como **seis preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Constitución | LGSS (RDLeg 8/2015) y otras normas |
|---|---|---|---|
| **I** | ¿Cómo se organiza? (estructura: gestión y colaboración) | Arts. 41, 50, 129.1 y 149.1.17.ª | Arts. 1, 2, 4, 66, 68, 73, 74, 74 bis, 79 y 80; disp. adic. 9.ª |
| **II** | ¿Cómo se financia? | — | Arts. 18, 109, 110, 117, 118, 121, 125 y 127 bis |
| **III** | ¿Qué problemas tiene y qué líneas de actuación sigue? | — | Preámbulos de la Ley 21/2021 y del RDL 2/2023; art. 58 |
| **IV** | ¿Qué regímenes la forman? (Régimen General y especiales) | — | Arts. 7, 9, 10, 11, 136, 137 y 305 |
| **V** | ¿Qué protege? (acción protectora) | — | Arts. 42, 43, 63, 64, 155 a 158 y 314 |
| **VI** | ¿Qué prestaciones da y cómo son? (tipos y características) | — | Arts. 44, 53, 165, 169, 172, 177, 193, 194, 204, 205, 216, 351, 363 y 369 |

!> **La idea que une los seis bloques:** la Constitución manda mantener un **régimen público** de Seguridad Social (art. 41) y reserva al Estado su **legislación básica y régimen económico** (art. 149.1.17.ª). La LGSS lo organiza en **entidades gestoras, servicios comunes y entidades colaboradoras** (I), lo financia con **cuotas y aportaciones del Estado** en un sistema de **reparto** (II), lo reforma para hacer frente al **reto demográfico** (III), lo divide en **Régimen General y regímenes especiales** (IV) y define una **acción protectora** común (V) que se concreta en **prestaciones contributivas y no contributivas** (VI).

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen; o, para un derecho o una prestación, Titulares · Contenido · Límites · Protección · ⚠ Ojo en el examen).
- La LGSS se cita en su **texto consolidado vigente**; donde dice «Ministerio de Empleo y Seguridad Social» se copia tal cual, porque así figura en el BOE.
- El bloque III cita **exposiciones de motivos** publicadas en el BOE: son texto oficial, pero **no** son parte dispositiva de la norma.
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- El desempleo es el tema III.5 y el mutualismo administrativo (MUFACE) y las clases pasivas, el tema V.9: aquí solo se mencionan.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Cómo se organiza la Seguridad Social? Estructura (CE; LGSS, arts. 1 a 4 y 66 a 80)", donde(
  "Primera pregunta del tema. Antes de ver cuánto cuesta y qué protege, hay que saber **de dónde nace** la Seguridad Social (la Constitución), **qué principios** la rigen y **quién la gestiona**.",
  ["1 Fundamento constitucional (arts. 41, 50, 129.1 y 149.1.17.ª CE)", "2 Derecho, principios y reparto de funciones (LGSS, arts. 1, 2 y 4)", "3 Entidades gestoras (arts. 66 y 68; disp. adic. 9.ª)", "4 Servicios comunes (arts. 73, 74 y 74 bis)", "5 Colaboración en la gestión: mutuas y empresas (arts. 79 y 80)"]))

T.ap("s1", "I.1 Fundamento constitucional (arts. 41, 50, 129.1 y 149.1.17.ª CE)", f"""
{unidad("1.1 Un régimen público de Seguridad Social (art. 41)",
  lit("CE", "Artículo 41", ["régimen público de Seguridad Social para todos los ciudadanos", "especialmente en caso de desempleo", "La asistencia y prestaciones complementarias serán libres"]),
  ficha(c("CE", "Artículo 41", "todos los ciudadanos"),
        f"Un régimen **público** que {c('CE', 'Artículo 41', 'garantice la asistencia y prestaciones sociales suficientes ante situaciones de necesidad')}",
        "Principio rector (Capítulo III del Título I): obliga a los poderes públicos a mantener el régimen",
        "—",
        "Régimen **público**; prestaciones **suficientes**; ante situaciones de **necesidad**; menciona **expresamente el desempleo**. Lo **complementario** es **libre** (no obligatorio)."))}

{unidad("1.2 Pensiones adecuadas y periódicamente actualizadas (art. 50)",
  lit("CE", "Artículo 50", ["pensiones adecuadas y periódicamente actualizadas", "durante la tercera edad"]),
  ficha("Los ciudadanos durante la tercera edad",
        f"{c('CE', 'Artículo 50', 'la suficiencia económica')} mediante pensiones adecuadas y actualizadas; y un sistema de servicios sociales",
        "—", "—",
        "Es la base de la **revalorización** de las pensiones (→ III.2.1): «adecuadas **y periódicamente actualizadas**»."))}

{unidad("1.3 Participación de los interesados (art. 129.1)",
  lit("CE", "Artículo 129", ["formas de participación de los interesados en la Seguridad Social"], solo=[1]),
  fichab("Participación de los interesados en la Seguridad Social", "Los interesados; la regula la ley",
         "En las formas que establezca la ley (la LGSS prevé la colaboración de trabajadores y empresarios: → I.2.3)", "—",
         "Es una **remisión a la ley**: «La ley establecerá»."))}

{unidad("1.4 Competencia del Estado (art. 149.1.17.ª)",
  lit("CE", "Artículo 149", ["Legislación básica y régimen económico de la Seguridad Social", "sin perjuicio de la ejecución de sus servicios por las Comunidades Autónomas"], solo=[1, 18]),
  fichab("Reparto de competencias sobre Seguridad Social",
         "**Estado**: legislación básica y régimen económico; **Comunidades Autónomas**: ejecución de sus servicios",
         "Competencia exclusiva del Estado sobre lo básico y lo económico",
         "—",
         "Exclusiva del Estado: **legislación básica y régimen económico** (no «toda la gestión»). Las CC. AA. pueden **ejecutar sus servicios**. Cayó en 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s2", "I.2 Derecho, principios y reparto de funciones (LGSS, arts. 1, 2 y 4)", f"""
{unidad("2.1 El derecho a la Seguridad Social se ajusta a la LGSS (art. 1)",
  lit("LGSS", "a1", ["establecido en el artículo 41 de la Constitución"]),
  ficha(c("LGSS", "a1", "los españoles"), "El derecho del art. 41 CE, con el contenido que fija la LGSS", "Lo que dispone la ley", "—",
        "La LGSS **desarrolla** el art. 41 CE."))}

{unidad("2.2 Principios y fines (art. 2)",
  lit("LGSS", "a2", ["modalidades contributiva y no contributiva", "universalidad, unidad, solidaridad e igualdad", "la protección adecuada"]),
  fichab("Principios del sistema y fin de protección",
         f"{c('LGSS', 'a2', 'El Estado, por medio de la Seguridad Social')}",
         ["::Cuatro principios:", "Universalidad", "Unidad", "Solidaridad", "Igualdad"],
         "—",
         "Son **cuatro**: universalidad, unidad, solidaridad e **igualdad** (no «suficiencia» ni «contributividad»). El sistema tiene **dos modalidades**: contributiva y no contributiva."))}

{unidad("2.3 Delimitación de funciones (art. 4)",
  lit("LGSS", "a4", ["la ordenación, jurisdicción e inspección", "colaborarán en la gestión", "operaciones de lucro mercantil"]),
  fichab("Qué corresponde al Estado y quién colabora",
         "**Estado**: ordenación, jurisdicción e inspección; **trabajadores y empresarios**: colaboran en la gestión",
         "Colaboración en los términos de la LGSS, de acuerdo con el art. 129.1 CE (→ I.1.3)",
         "—",
         "Tres funciones del Estado: **ordenación, jurisdicción e inspección**. La ordenación **nunca** puede fundar **operaciones de lucro mercantil**."))}
""", 2)

T.ap("s3", "I.3 Entidades gestoras (LGSS, arts. 66 y 68; disposición adicional novena)", f"""
{unidad("3.1 Enumeración: INSS, INGESA e IMSERSO (art. 66)",
  lit("LGSS", "a66", ["simplificación, racionalización, economía de costes, solidaridad financiera y unidad de caja, eficacia social y descentralización", "El Instituto Nacional de la Seguridad Social", "El Instituto Nacional de Gestión Sanitaria", "El Instituto de Mayores y Servicios Sociales"], solo=[1, 2, 3, 4]),
  fichab("Entidades que gestionan y administran la Seguridad Social",
         "Bajo la dirección y tutela de los departamentos ministeriales",
         ["::Tres entidades gestoras:", "**INSS**: prestaciones económicas (salvo las del IMSERSO)", "**INGESA**: servicios sanitarios", "**IMSERSO**: pensiones no contributivas de invalidez y jubilación y servicios complementarios"],
         "—",
         "Las **pensiones no contributivas** las gestiona el **IMSERSO**, no el INSS. La lista de principios incluye la **unidad de caja** y la **descentralización**."))}

{unidad("3.2 Naturaleza jurídica (art. 68)",
  lit("LGSS", "a68", ["entidades de derecho público"], solo=[1]),
  fichab("Naturaleza de las entidades gestoras", "INSS, INGESA, IMSERSO", "Entidades de derecho público con capacidad jurídica para sus fines", "—",
         "Son **entidades de derecho público** (no sociedades mercantiles ni fundaciones)."))}

{unidad("3.3 Instituto Social de la Marina (disposición adicional novena)",
  lit("LGSS", "danovena", ["Régimen Especial de la Seguridad Social de los Trabajadores del Mar", "se adscriben a la Tesorería General de la Seguridad Social"]),
  fichab("Gestión del régimen especial del mar", "El **Instituto Social de la Marina**",
         "Continúa con sus funciones; sus recursos y patrimonio se adscriben a la Tesorería General", "—",
         "El ISM gestiona el **Régimen Especial de los Trabajadores del Mar** (→ IV.2.2). Las prestaciones por **desempleo** las gestiona el **Servicio Público de Empleo Estatal** (art. 294; tema III.5)."))}
""", 2)

T.ap("s4", "I.4 Servicios comunes (LGSS, arts. 73, 74 y 74 bis)", f"""
{unidad("4.1 Creación (art. 73)",
  lit("LGSS", "a73", ["Corresponde al Gobierno"]),
  fichab("Establecimiento de servicios comunes", f"{c('LGSS', 'a73', 'al Gobierno, a propuesta del Ministerio de Empleo y Seguridad Social')}",
         "Establece los servicios comunes y reglamenta su estructura y competencias", "—", "Los crea el **Gobierno** (no una ley ni el Ministro solo)."))}

{unidad("4.2 Tesorería General de la Seguridad Social (art. 74)",
  lit("LGSS", "a74", ["servicio común con personalidad jurídica propia", "solidaridad financiera y caja única", "custodia de los fondos, valores y créditos"], solo=[1]),
  fichab("Caja única del sistema", "La **Tesorería General de la Seguridad Social** (servicio común con personalidad jurídica propia)",
         ["Unifica todos los recursos financieros, presupuestarios y extrapresupuestarios", "Custodia fondos, valores y créditos", "Recauda derechos y paga obligaciones"],
         "—",
         "Principios: **solidaridad financiera y caja única**. En ella se constituyen el **fondo de estabilización** (→ II.2.1) y el **Fondo de Reserva** (→ II.3.1)."))}

{unidad("4.3 Gerencia de Informática de la Seguridad Social (art. 74 bis)",
  lit("LGSS", "a7-2", ["servicio común para la gestión y administración de las tecnologías de la información y las comunicaciones", "con rango de Subdirección General"], solo=[1]),
  fichab("Servicio común de tecnologías de la información", "La **Gerencia de Informática de la Seguridad Social**",
         "Con personalidad jurídica propia; adscrita a la Secretaría de Estado de la Seguridad Social", "—",
         "Es el **segundo** servicio común que nombra la ley; tiene rango de **Subdirección General**."))}
""", 2)

T.ap("s5", "I.5 Colaboración en la gestión: mutuas y empresas (LGSS, arts. 79 y 80)", f"""
{unidad("5.1 Quién colabora (art. 79)",
  lit("LGSS", "a79", ["por mutuas colaboradoras con la Seguridad Social y por empresas", "previa su inscripción en un registro público"]),
  fichab("Entidades colaboradoras", "**Mutuas** colaboradoras y **empresas**; también asociaciones, fundaciones y entidades públicas y privadas inscritas",
         "Según el capítulo VI del título I", "—", "Las colaboradoras «clásicas» son **mutuas y empresas**; las demás necesitan **inscripción en un registro público**."))}

{unidad("5.2 Mutuas colaboradoras con la Seguridad Social (art. 80)",
  lit("LGSS", "a80", ["asociaciones privadas de empresarios", "sin ánimo de lucro", "responsabilidad mancomunada", "contingencias de accidentes de trabajo y enfermedades profesionales", "incapacidad temporal derivada de contingencias comunes", "sector público estatal de carácter administrativo"], solo=[1, 3, 4, 5, 6, 7, 8, 9, 11]),
  fichab("Asociaciones privadas de empresarios que colaboran en la gestión",
         f"Constituidas {c('LGSS', 'a80', 'mediante autorización del Ministerio de Empleo y Seguridad Social e inscripción en el registro especial dependiente de este')}",
         ["::Gestionan:", "Prestaciones y asistencia sanitaria de accidentes de trabajo y enfermedades profesionales", "Incapacidad temporal por contingencias comunes", "Riesgo durante el embarazo y la lactancia natural", "Cese de actividad de los autónomos", "Cuidado de menores con cáncer u otra enfermedad grave"],
         "—",
         "Son **privadas**, **sin ánimo de lucro**, con **responsabilidad mancomunada** de sus asociados, pero forman parte del **sector público estatal de carácter administrativo**."))}

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Quién | Qué es | Artículo |
|---|---|---|
| INSS | Entidad gestora: prestaciones económicas | 66.1 a) |
| INGESA | Entidad gestora: servicios sanitarios | 66.1 b) |
| IMSERSO | Entidad gestora: pensiones no contributivas de invalidez y jubilación y servicios complementarios | 66.1 c) |
| Instituto Social de la Marina | Gestión del régimen especial del mar | Disp. adic. 9.ª |
| Tesorería General | Servicio común: caja única | 74 |
| Gerencia de Informática | Servicio común: tecnologías de la información | 74 bis |
| Mutuas colaboradoras | Asociaciones privadas de empresarios que colaboran | 80 |

{resumen([
  "La CE manda un **régimen público** de Seguridad Social (41) y reserva al Estado la **legislación básica y el régimen económico** (149.1.17.ª).",
  "Principios: **universalidad, unidad, solidaridad e igualdad** (LGSS, 2); al Estado, **ordenación, jurisdicción e inspección** (4).",
  "Entidades gestoras: **INSS, INGESA e IMSERSO** (66); servicios comunes: **Tesorería General** y **Gerencia de Informática** (74 y 74 bis).",
  "Colaboran **mutuas** (asociaciones privadas de empresarios, sin ánimo de lucro) y **empresas** (79 y 80)."],
  "Siguiente: II. ¿Cómo se financia?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Cómo se financia? (LGSS, arts. 18, 109, 110 y 117 a 127 bis)", donde(
  "Segunda pregunta. Ya sabemos quién gestiona; ahora, **con qué dinero**: cuotas, aportaciones del Estado y otros recursos, en un sistema de **reparto** con dos colchones: el fondo de estabilización y el **Fondo de Reserva**.",
  ["1 Cotización obligatoria y recursos (arts. 18 y 109)", "2 Sistema financiero de reparto (art. 110)", "3 Fondo de Reserva (arts. 117, 118, 121 y 125)", "4 Mecanismo de Equidad Intergeneracional (art. 127 bis)"]))

T.ap("s6", "II.1 Cotización obligatoria y recursos (LGSS, arts. 18 y 109)", f"""
{unidad("1.1 La cotización es obligatoria (art. 18.1 y 2)",
  lit("LGSS", "a18", ["es obligatoria en todos los regímenes del sistema", "desde el momento de iniciación de la actividad correspondiente"], solo=[1, 3]),
  fichab("Obligación de cotizar", "Las personas que determinen las normas de cada régimen",
         "Obligatoria en **todos** los regímenes", "Nace desde la **iniciación de la actividad**",
         "La cotización es obligatoria en **todos** los regímenes; la obligación nace con el **inicio de la actividad** (no con el alta)."))}

{unidad("1.2 Recursos generales (art. 109.1)",
  lit("LGSS", "a109", ["Las aportaciones progresivas del Estado", "con carácter permanente en sus Presupuestos Generales", "Las cuotas de las personas obligadas", "recargos, sanciones u otras de naturaleza análoga"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Recursos con que se financia la Seguridad Social", "Estado, personas obligadas a cotizar y otros",
         ["a) Aportaciones progresivas del Estado", "b) Cuotas de las personas obligadas", "c) Recargos, sanciones y análogos", "d) Frutos, rentas o intereses del patrimonio", "e) Cualesquiera otros ingresos"],
         "—",
         "Las aportaciones del Estado son **progresivas** y se consignan **con carácter permanente** en los Presupuestos Generales. La ley **no** las califica de «finalistas» (→ Cierre 1)."))}

{unidad("1.3 Qué se paga con cada recurso (art. 109.2)",
  lit("LGSS", "a109", ["en su modalidad no contributiva y universal, se financiará mediante aportaciones del Estado", "serán financiadas básicamente con los recursos a que se refieren las letras b), c), d) y e)"], solo=[7, 8]),
  fichab("Separación de fuentes de financiación",
         "Estado (no contributivo); cotizaciones y demás recursos (contributivo)",
         ["**No contributivo y universal** → aportaciones del Estado (salvo sanidad y servicios sociales transferidos a las CC. AA.: financiación autonómica)", "**Contributivo** y gastos de gestión → básicamente cuotas y demás recursos (letras b a e)"],
         "—",
         "Regla de examen: **no contributivas → Estado**; **contributivas → cotizaciones**."))}

{unidad("1.4 Naturaleza de cada prestación (art. 109.3)",
  lit("LGSS", "a109", ["Tienen naturaleza contributiva", "Tienen naturaleza no contributiva", "Los complementos por mínimos de las pensiones de la Seguridad Social", "El ingreso mínimo vital"], solo=[9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]),
  fichab("Qué prestaciones son contributivas y cuáles no", "—",
         ["::Contributivas:", "Las prestaciones económicas (salvo las no contributivas de la lista)", "Todas las de accidentes de trabajo y enfermedades profesionales", "::No contributivas:", "Asistencia sanitaria y servicios sociales (salvo AT y EP)", "Pensiones no contributivas de invalidez y jubilación", "Subsidio por maternidad de los arts. 181 y 182", "Complementos por mínimos", "Prestaciones familiares del capítulo I del título VI", "Ingreso mínimo vital"],
         "—",
         "Los **complementos por mínimos** y la **asistencia sanitaria** son **no contributivos** (los paga el Estado), aunque complementen o atiendan a pensionistas contributivos. **Todo** lo de AT y EP es contributivo."))}
""", 2)

T.ap("s7", "II.2 Sistema financiero de reparto (LGSS, art. 110)", f"""
{unidad("2.1 Reparto, fondo de estabilización y capitalización de AT y EP (art. 110)",
  lit("LGSS", "a110", ["será el de reparto", "fondo de estabilización único", "se procederá a la capitalización del importe de dichas pensiones"], solo=[1, 2, 3]),
  fichab("Sistema financiero del sistema",
         "Todos los regímenes; el fondo de estabilización, en la **Tesorería General**; los capitales coste, a cargo de mutuas o empresas responsables",
         ["**Reparto** para todas las contingencias", "**Fondo de estabilización único**: desviaciones entre ingresos y gastos", "**Capitalización** de pensiones de IP o muerte por AT o EP a cargo de mutuas o empresas (capitales coste)"],
         "—",
         "La regla es el **reparto**; la excepción, la **capitalización** de las pensiones de incapacidad permanente o muerte por **AT o EP** a cargo de mutuas o empresas."))}
""", 2)

T.ap("s8", "II.3 El Fondo de Reserva de la Seguridad Social (LGSS, arts. 117, 118, 121 y 125)", f"""
{unidad("3.1 Constitución (art. 117)",
  lit("LGSS", "a117", ["En la Tesorería General de la Seguridad Social", "prestaciones contributivas"]),
  fichab("Fondo de Reserva", "Se constituye en la **Tesorería General**", "Para atender necesidades financieras de las **prestaciones contributivas**", "—",
         "Es para prestaciones **contributivas**; el fondo de **estabilización** (110.2) es otro fondo distinto."))}

{unidad("3.2 Dotación (art. 118)",
  lit("LGSS", "a118", ["Los excedentes de ingresos", "siempre que las posibilidades económicas y la situación financiera del sistema de Seguridad Social lo permitan", "cotización finalista fijada en el artículo 127 bis"]),
  fichab("Con qué se nutre el Fondo",
         "Sistema (excedentes) y mutuas colaboradoras (excedentes de su gestión)",
         ["Excedentes de ingresos de lo contributivo, si la situación financiera lo permite", "Excedente tras dotar la Reserva de Estabilización de Contingencias Comunes de las mutuas", "Porcentaje del excedente de contingencias profesionales de las mutuas", "Cotización finalista del **MEI** (→ II.4.1)"],
         "—",
         "Desde el MEI, el Fondo recibe también la **cotización finalista** del art. 127 bis."))}

{unidad("3.3 Para qué se usa (art. 121.1)",
  lit("LGSS", "a121", ["con carácter exclusivo a la financiación de las pensiones de carácter contributivo"], solo=[1]),
  fichab("Destino de los activos del Fondo", "—",
         f"Solo para pensiones contributivas, {c('LGSS', 'a121', 'para reforzar el equilibrio y sostenibilidad del sistema de Seguridad Social')}",
         f"Desembolsos anuales que fija la Ley de Presupuestos {c('LGSS', 'a121', 'desde 2033')} (121.2)",
         "Destino **exclusivo**: pensiones **contributivas** (ni no contributivas ni el MEI, que es un **ingreso** del Fondo). Cayó en 2025 (→ Cierre 1)."))}

{unidad("3.4 Comisión de Seguimiento del Fondo (art. 125)",
  lit("LGSS", "a125", ["presidida por el Secretario de Estado de la Seguridad Social", "Cuatro representantes de las distintas organizaciones sindicales de mayor implantación", "Cuatro representantes de las organizaciones empresariales de mayor implantación", "sin voz ni voto", "conocerá semestralmente"]),
  fichab("Órgano que conoce la evolución del Fondo",
         "Preside el **Secretario de Estado de la Seguridad Social**; 3 del Ministerio de Empleo y Seguridad Social, 1 de Economía, 1 de Hacienda, **4 sindicales**, **4 empresariales**; secretario sin voz ni voto",
         "Recibe información del Comité de Gestión, la Comisión Asesora de Inversiones y la Tesorería General antes de sus reuniones",
         "Conoce **semestralmente** de la evolución y composición del Fondo",
         "**Semestralmente** (no anual ni trimestral). Cayó dos veces en 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s9", "II.4 El Mecanismo de Equidad Intergeneracional (LGSS, art. 127 bis)", f"""
{unidad("4.1 Una cotización finalista que nutre el Fondo de Reserva (art. 127 bis)",
  lit("LGSS", "a1-5", ["cotización finalista", "que no será computable a efectos de prestaciones", "La cotización será de 1,2 puntos porcentuales", "un punto porcentual corresponderá a la empresa y 0,2 puntos porcentuales al trabajador", "no podrá ser objeto de bonificación, reducción, exención o deducción alguna"], solo=[1, 2, 3]),
  fichab("Mecanismo de Equidad Intergeneracional (MEI)",
         "Todos los regímenes, en todos los supuestos en que se cotice por **jubilación**; en cuenta ajena, empresa y trabajador",
         ["Cotización **finalista**: nutre el **Fondo de Reserva**", "**No** computa a efectos de prestaciones", "Sin bonificaciones, reducciones, exenciones ni deducciones"],
         "**1,2** puntos: **1** la empresa y **0,2** el trabajador",
         "1,2 = 1 + 0,2. El MEI **no** genera derecho a prestaciones: va al **Fondo de Reserva**."))}

{resumen([
  "Cotizar es **obligatorio en todos los regímenes**, desde el inicio de la actividad (18).",
  "Recursos: aportaciones **progresivas** del Estado, **cuotas**, recargos y sanciones, rentas del patrimonio y otros (109.1). **No contributivo → Estado; contributivo → cotizaciones** (109.2).",
  "Sistema de **reparto**, con **fondo de estabilización** en la Tesorería y capitalización de pensiones por AT y EP a cargo de mutuas o empresas (110).",
  "**Fondo de Reserva**: solo para pensiones **contributivas** (121); su Comisión de Seguimiento lo conoce **semestralmente** (125); lo nutre el **MEI**: **1,2 puntos** (1 empresa + 0,2 trabajador) (127 bis)."],
  "Siguiente: III. ¿Qué problemas tiene y qué líneas de actuación sigue?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. Problemas actuales y líneas de actuación (Ley 21/2021 y RDL 2/2023)", donde(
  "Tercera pregunta. El epígrafe pide los **problemas actuales** y las **líneas de actuación**. No son materia de un artículo: se toman de lo que el propio legislador dice en las **exposiciones de motivos** de las dos últimas reformas de pensiones (BOE) y de los artículos de la LGSS que las aplican.",
  ["1 El diagnóstico: Pacto de Toledo y reto demográfico (Ley 21/2021, preámbulo)", "2 Las líneas de actuación ya en vigor (LGSS, art. 58; RDL 2/2023, preámbulo)", "3 Pendiente (temario): datos y documentos que no son del BOE"]))

T.ap("s10", "III.1 El diagnóstico del legislador (Ley 21/2021, preámbulo, apartados I y II)", f"""
*Las exposiciones de motivos son texto oficial publicado en el BOE, pero no son parte dispositiva de la ley: explican por qué se aprueba.*

{unidad("1.1 El Pacto de Toledo marca las líneas de actuación (preámbulo, I)",
  lit("L21_2021", "pr", ["19 de noviembre de 2020", "por tercera vez desde su aprobación inicial en 1995", "marca las líneas de actuación"], solo=[6], titulo=EM21.format("I")),
  fichab("Origen de la reforma: el Informe de evaluación y reforma del Pacto de Toledo",
         "El **Pleno del Congreso** (aprobación del Informe); después, diálogo social entre Gobierno, sindicatos y empresarios",
         "Recomendaciones que reivindican la centralidad del sistema público de pensiones",
         "Aprobado el **19-11-2020**; tercera revisión desde **1995**",
         "Lo aprueba el **Congreso**; es la **tercera** vez desde **1995**."))}

{unidad("1.2 El problema: sostenibilidad y jubilación del «baby boom» (preámbulo, II)",
  lit("L21_2021", "pr", ["problemas de sostenibilidad", "la del baby boom"], solo=[12, 13], titulo=EM21.format("II")),
  fichab("Diagnóstico", "—",
         ["Advertencia de **problemas de sostenibilidad** desde hace décadas", "El sistema se ha adaptado con **reformas paramétricas periódicas**", "Singularidad actual: llega a la jubilación la generación del **baby boom**"],
         "—",
         "El reto que nombra la ley es **demográfico**: la jubilación de la generación del **baby boom**."))}

{unidad("1.3 Los dos objetivos de la respuesta (preámbulo, II)",
  lit("L21_2021", "pr", ["revalorización vinculado a la evolución de la inflación", "la asunción por el Estado de los gastos de naturaleza no contributiva", "favorecen la demora en el acceso a la pensión de jubilación"], solo=[14, 15], titulo=EM21.format("II")),
  fichab("Objetivos de la reforma de 2021", "Los poderes públicos (Estado)",
         ["1.º **Certidumbre**: garantizar el poder adquisitivo con una revalorización ligada a la **inflación** (→ III.2.1)", "2.º **Equilibrio**: el Estado asume los **gastos no contributivos** (→ II.1.3) e incentivos a **demorar la jubilación**"],
         "—",
         "Dos objetivos: **certidumbre** (revalorización con la inflación) y **equilibrio** (separación de fuentes y jubilación demorada)."))}
""", 2)

T.ap("s11", "III.2 Las líneas de actuación ya en vigor (LGSS, art. 58; RDL 2/2023, preámbulo)", f"""
{unidad("2.1 Revalorización con el IPC (LGSS, art. 58)",
  lit("LGSS", "a58", ["mantendrán su poder adquisitivo", "al comienzo de cada año", "valor medio de las tasas de variación interanual", "Índice de Precios al Consumo de los doce meses previos a diciembre del año anterior", "el importe de las pensiones no variará"], solo=[1, 2, 3, 4]),
  fichab("Garantía del poder adquisitivo de las pensiones contributivas",
         "Todas las pensiones contributivas, **incluido el complemento de brecha de género**; la Ley de Presupuestos actualiza también la pensión máxima y la mínima",
         "Porcentaje = **valor medio** de las tasas interanuales del **IPC** de los **doce meses previos a diciembre** del año anterior",
         "Al **comienzo de cada año**; si el valor medio es **negativo**, las pensiones **no varían**",
         "Media de **doce meses** (no el IPC de diciembre). Con inflación negativa, **no bajan**. Es la línea de la recomendación 2 del Pacto de Toledo, según el preámbulo (apartado III) de la Ley 21/2021 (→ III.1.3)."))}

{unidad("2.2 Tres actuaciones para la sostenibilidad financiera (RDL 2/2023, preámbulo, I)",
  lit("RDL2_2023", "pr", ["la jubilación de la macrogeneración del baby boom", "en los próximos treinta años", "el incremento gradual de la base máxima", "una novedosa cotización de solidaridad", "Mecanismo de Equidad Intergeneracional", "el factor de sostenibilidad"], solo=[4, 5, 6, 7], titulo=EM23),
  fichab("Líneas de actuación de la reforma de 2023",
         "El Gobierno (real decreto-ley), tras el diálogo social",
         ["1.ª Subida **gradual** de la **base máxima** de cotización", "2.ª **Cotización de solidaridad** sobre los salarios que superan la base máxima (LGSS, art. 19 bis)", "3.ª **MEI**: cotización adicional que recupera el **Fondo de Reserva** (→ II.4.1)", "Se sustituye el **factor de sostenibilidad** (LGSS, art. 211: hoy «(Derogado)»)"],
         "Objetivo: sostenibilidad **en los próximos treinta años**",
         "Tres actuaciones: **base máxima**, **cotización de solidaridad** y **MEI**. El MEI **sustituye** al factor de sostenibilidad, que recortaba la pensión inicial."))}
""", 2)

T.ap("s12", "III.3 Pendiente (temario): datos y documentos que no son del BOE", f"""
?> **Pendiente (temario).** El epígrafe pide también los **problemas actuales** en cifras (número de afiliados y de pensionistas, relación entre ellos, gasto en pensiones, saldo del sistema, evolución del Fondo de Reserva) y el contenido de las **recomendaciones del Pacto de Toledo** (Informe de 2020, publicado por el Congreso). No se han copiado aquí porque no se ha descargado una fuente oficial con esos datos: se completará con el temario del usuario o con la fuente oficial (Seguridad Social, Congreso) que aporte.

{resumen([
  "El **Pacto de Toledo** (informe aprobado por el **Pleno del Congreso** el **19-11-2020**, tercera revisión desde **1995**) **marca las líneas de actuación**.",
  "Problema central según el legislador: la **sostenibilidad** ante la jubilación de la generación del **baby boom**.",
  "Líneas en vigor: **revalorización** con la media del **IPC** (art. 58), el **Estado** asume lo **no contributivo**, incentivos a la **jubilación demorada**, subida de la **base máxima**, **cotización de solidaridad** y **MEI** en lugar del **factor de sostenibilidad**."],
  "Siguiente: IV. ¿Qué regímenes la forman? Régimen General y regímenes especiales")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Qué regímenes forman el sistema? Régimen General y regímenes especiales (LGSS, arts. 7 a 11, 136, 137 y 305)", donde(
  "Cuarta pregunta. ¿A **quién** protege el sistema y **en qué régimen** se encuadra cada uno? El sistema se divide en el **Régimen General** y los **regímenes especiales**, con **sistemas especiales** dentro de ellos.",
  ["1 Campo de aplicación del sistema (art. 7)", "2 Estructura: regímenes y sistemas especiales (arts. 9, 10 y 11)", "3 El Régimen General (arts. 136 y 137)", "4 El Régimen Especial de Trabajadores Autónomos (art. 305)"]))

T.ap("s13", "IV.1 Campo de aplicación del sistema (LGSS, art. 7)", f"""
{unidad("1.1 Quién está comprendido (art. 7.1 y 2)",
  lit("LGSS", "a7", ["a efectos de las prestaciones contributivas", "los españoles que residan en España y los extranjeros que residan o se encuentren legalmente en España", "mayores de dieciocho años", "Funcionarios públicos, civiles y militares", "a efectos de las prestaciones no contributivas, todos los españoles residentes en territorio español"], solo=[1, 2, 3, 4, 5, 6, 7, 8]),
  fichab("Personas incluidas en el sistema",
         ["::Nivel contributivo (ejercen su actividad en territorio nacional):", "a) Trabajadores por cuenta ajena", "b) Autónomos mayores de dieciocho años", "c) Socios trabajadores de cooperativas de trabajo asociado", "d) Estudiantes", "e) Funcionarios públicos, civiles y militares", "::Nivel no contributivo:", "Españoles residentes y extranjeros residentes legalmente"],
         "—", "—",
         "Contributivo: españoles **residentes** y extranjeros que **residan o se encuentren legalmente**, con actividad **en territorio nacional**. No contributivo: **residentes**. Autónomos: **mayores de dieciocho años**."))}

{unidad("1.2 Exclusión por trabajo marginal (art. 7.5)",
  lit("LGSS", "a7", ["pueda considerarse marginal y no constitutivo de medio fundamental de vida"], solo=[11]),
  fichab("Exclusión del campo de aplicación", "El **Gobierno**, a propuesta del Ministerio y oídos sindicatos más representativos o el colegio oficial",
         "A **instancia de los interesados**, por razón de jornada o retribución", "—",
         "La exclusión la decide el **Gobierno** y requiere **instancia de los interesados**."))}
""", 2)

T.ap("s14", "IV.2 Estructura del sistema: regímenes y sistemas especiales (LGSS, arts. 9, 10 y 11)", f"""
{unidad("2.1 Régimen General y regímenes especiales (art. 9)",
  lit("LGSS", "a9", ["El Régimen General, que se regula en el título II de la presente ley", "Los regímenes especiales a que se refiere el artículo siguiente", "totalización de los períodos de permanencia"]),
  fichab("Composición del sistema", "—",
         ["**Régimen General** (título II)", "**Regímenes especiales** (art. 10)", "Paso de un régimen a otro: **totalización** de periodos que no se superpongan"],
         "—", "Solo hay **dos** piezas: Régimen General y regímenes especiales."))}

{unidad("2.2 Cuándo y cuáles son regímenes especiales (art. 10)",
  lit("LGSS", "a10", ["por su naturaleza, sus peculiares condiciones de tiempo y lugar o por la índole de sus procesos productivos", "Trabajadores por cuenta propia o autónomos", "Trabajadores del mar", "Funcionarios públicos, civiles y militares", "Estudiantes", "se regirán por las leyes específicas", "máxima homogeneidad con el Régimen General", "tendencia a la unidad"]),
  fichab("Regímenes especiales",
         "Los crea la ley o el Ministerio (letra e); el **Gobierno** puede integrarlos en el Régimen General",
         ["::Grupos (10.2):", "a) Autónomos", "b) Trabajadores del mar", "c) Funcionarios públicos, civiles y militares", "d) Estudiantes", "e) Los que determine el Ministerio", "::Regulación:", "Mar y funcionarios: **leyes específicas** (10.3)", "Los demás: normas reglamentarias, con máxima homogeneidad con el Régimen General (10.4)"],
         "—",
         "**Mar** y **funcionarios** se rigen por **leyes específicas** y **no** pueden integrarse en el Régimen General por el art. 10.5. La integración responde a la **tendencia a la unidad**. Funcionarios: tema V.9."))}

{unidad("2.3 Sistemas especiales (art. 11)",
  lit("LGSS", "a11", ["encuadramiento, afiliación, forma de cotización o recaudación"]),
  fichab("Sistemas especiales dentro de un régimen", "—",
         f"Solo en materia de {c('LGSS', 'a11', 'encuadramiento, afiliación, forma de cotización o recaudación')}",
         "—",
         "Un **sistema** especial no es un **régimen**: solo modula **encuadramiento, afiliación, cotización o recaudación**, no la acción protectora. Ejemplos: empleados de hogar y agrarios (→ IV.3.1)."))}
""", 2)

T.ap("s15", "IV.3 El Régimen General (LGSS, arts. 136 y 137)", f"""
{unidad("3.1 Quién está incluido (art. 136)",
  lit("LGSS", "a136", ["los trabajadores por cuenta ajena y los asimilados", "Sistema Especial para Empleados de Hogar y en el Sistema Especial para Trabajadores por Cuenta Ajena Agrarios", "El personal civil no funcionario de las administraciones públicas", "salvo que estén incluidos en el Régimen de Clases Pasivas del Estado", "Los altos cargos de las administraciones públicas"], solo=[1, 2, 3, 15, 16, 19]),
  fichab("Campo de aplicación del Régimen General",
         ["**Trabajadores por cuenta ajena** y asimilados (art. 7.1 a)", "Incluidos los sistemas especiales de **empleados de hogar** y **agrarios por cuenta ajena**", "Personal civil no funcionario de las Administraciones", "Funcionarios, salvo Clases Pasivas u otro régimen por ley especial", "Altos cargos que no sean funcionarios", "(y los demás asimilados de las letras b a q)"],
         "Inclusión **obligatoria**, salvo que por su actividad deban ir a un régimen especial", "—",
         "Los **funcionarios de nuevo ingreso** que no estén en Clases Pasivas cotizan al **Régimen General** (letra l). Empleados de hogar y agrarios por cuenta ajena son **sistemas especiales del Régimen General**, no regímenes especiales."))}

{unidad("3.2 Quién queda fuera (art. 137)",
  lit("LGSS", "a137", ["servicios amistosos, benévolos o de buena vecindad"], solo=[1, 2, 3]),
  fichab("Exclusiones del Régimen General", "—",
         ["Trabajos ocasionales amistosos, benévolos o de buena vecindad", "Los que den lugar a inclusión en un régimen especial", "Profesores universitarios eméritos y personal licenciado sanitario emérito"], "—",
         "La **buena vecindad** ocasional no da lugar a alta."))}
""", 2)

T.ap("s16", "IV.4 El Régimen Especial de Trabajadores Autónomos (LGSS, art. 305)", f"""
{unidad("4.1 Quién está incluido (art. 305.1 y 2)",
  lit("LGSS", "a305", ["mayores de dieciocho años", "de forma habitual, personal, directa, por cuenta propia y fuera del ámbito de dirección y organización de otra persona", "Sistema Especial para Trabajadores por Cuenta Propia Agrarios", "al menos, la mitad del capital social", "Los trabajadores autónomos económicamente dependientes"], solo=[1, 2, 3, 4, 13]),
  fichab("Campo de aplicación del RETA",
         "Personas físicas **mayores de dieciocho años** que trabajan por cuenta propia; entre otros, agrarios por cuenta propia (sistema especial), consejeros con **control efectivo**, TRADE",
         "Actividad **habitual, personal, directa**, por cuenta propia y fuera de la dirección de otro, **a título lucrativo**", "Control efectivo: en todo caso, con **al menos la mitad** del capital social",
         "Los consejeros o administradores **con control** de la sociedad van al **RETA**; **sin control**, al Régimen General como asimilados (→ IV.3.1)."))}

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Pieza | Qué es | Ejemplos | Artículos |
|---|---|---|---|
| Régimen General | Cuenta ajena y asimilados | Personal laboral; funcionarios fuera de Clases Pasivas; altos cargos no funcionarios | 136 |
| Sistema especial (dentro de un régimen) | Solo encuadramiento, afiliación, cotización o recaudación | Empleados de hogar y agrarios por cuenta ajena (RG); agrarios por cuenta propia (RETA) | 11, 136.2 a), 305.2 a) |
| Régimen especial por norma reglamentaria | Máxima homogeneidad con el RG | Autónomos (hoy en el título IV de la LGSS); estudiantes | 10.2 a) y d), 10.4 |
| Régimen especial por ley específica | No integrable en el RG por el art. 10.5 | Trabajadores del mar; funcionarios civiles y militares (tema V.9) | 10.2 b) y c), 10.3 |

{resumen([
  "Sistema = **Régimen General** + **regímenes especiales** (9); dentro de ellos, **sistemas especiales** solo para encuadramiento, afiliación, cotización o recaudación (11).",
  "Regímenes especiales: **autónomos, mar, funcionarios, estudiantes** y los que determine el Ministerio (10.2); **mar y funcionarios**, por **ley específica** (10.3).",
  "Régimen General: **cuenta ajena** y asimilados, con los sistemas especiales de **empleados de hogar** y **agrarios** (136).",
  "RETA: **mayores de 18 años**, actividad **habitual, personal y directa** por cuenta propia (305)."],
  "Siguiente: V. ¿Qué protege? La acción protectora")}
""", 2)

# =============================================================================
T.ap("bV", "V. ¿Qué protege? La acción protectora (LGSS, arts. 42, 43, 63, 64 y 155 a 158)", donde(
  "Quinta pregunta. La **acción protectora** es la lista de **lo que cubre** el sistema. La fija el art. 42 para todo el sistema; cada régimen la recorta, y las **contingencias** (accidente de trabajo, enfermedad profesional, accidente no laboral, enfermedad común) deciden qué reglas se aplican.",
  ["1 Contenido de la acción protectora (arts. 42 y 43)", "2 Servicios sociales y asistencia social (arts. 63 y 64)", "3 Alcance en el Régimen General y en el RETA (arts. 155 y 314)", "4 Las contingencias (arts. 156, 157 y 158)"]))

T.ap("s17", "V.1 Contenido de la acción protectora (LGSS, arts. 42 y 43)", f"""
{unidad("1.1 Qué comprende (art. 42)",
  lit("LGSS", "a42", ["La asistencia sanitaria", "La recuperación profesional", "Las prestaciones económicas en las situaciones de incapacidad temporal", "ingreso mínimo vital", "Las prestaciones familiares de la Seguridad Social", "Las prestaciones de servicios sociales", "los beneficios de la asistencia social", "establece y limita el ámbito de extensión posible"]),
  fichab("Acción protectora del sistema", "Todo el sistema (cada régimen, dentro de este límite)",
         ["a) Asistencia sanitaria", "b) Recuperación profesional", "c) Prestaciones económicas (IT, nacimiento y cuidado de menor, riesgo en el embarazo y la lactancia, IP, jubilación, desempleo, cese de actividad, muerte y supervivencia, ingreso mínimo vital…)", "d) Prestaciones familiares", "e) Servicios sociales", "Como complemento: asistencia social (42.2)"],
         "—",
         "El art. 42 **establece y limita** lo que pueden cubrir los regímenes. Toda prestación pública que complemente las contributivas **forma parte del sistema** (42.4)."))}

{unidad("1.2 Mejoras voluntarias y prohibición de contratación colectiva (art. 43)",
  lit("LGSS", "a43", ["podrá ser mejorada voluntariamente", "no podrá ser objeto de contratación colectiva"]),
  fichab("Mejoras de la acción protectora", "Las personas del art. 7.1 (nivel contributivo)",
         "Mejora voluntaria en la forma que fijen las normas de cada régimen", "—",
         "Solo se mejora la modalidad **contributiva**. Fuera de las mejoras voluntarias, la Seguridad Social **no** puede ser objeto de **contratación colectiva**."))}
""", 2)

T.ap("s18", "V.2 Servicios sociales y asistencia social (LGSS, arts. 63 y 64)", f"""
{unidad("2.1 Servicios sociales (art. 63)",
  lit("LGSS", "a63", ["Como complemento de las prestaciones"]),
  fichab("Servicios sociales de la Seguridad Social", "La Seguridad Social, en conexión con el departamento ministerial que corresponda",
         "Prestaciones de servicios sociales establecidas legal o reglamentariamente (art. 42.1 e)", "—", "Son **complemento** de las prestaciones."))}

{unidad("2.2 Asistencia social (art. 64)",
  lit("LGSS", "a64", ["previa demostración, salvo en casos de urgencia, de que el interesado carece de los recursos indispensables", "con el límite de los recursos consignados a este fin", "sin que los servicios o auxilios económicos otorgados puedan comprometer recursos del ejercicio económico siguiente"], solo=[1, 4]),
  fichab("Servicios y auxilios por estados de necesidad",
         "Las personas incluidas en el campo de aplicación y sus familiares o asimilados; la conceden las **entidades gestoras**",
         "Previa prueba de **carencia de recursos** (salvo urgencia)",
         "Con el límite del crédito presupuestario; sin comprometer el ejercicio **siguiente**",
         "La asistencia social es **potestativa** («podrá») y **limitada** por el presupuesto."))}
""", 2)

T.ap("s19", "V.3 Alcance de la acción protectora en el Régimen General y en el RETA (LGSS, arts. 155 y 314)", f"""
{unidad("3.1 Régimen General (art. 155.1)",
  lit("LGSS", "a155", ["con excepción de la protección por cese de actividad y las prestaciones no contributivas"], solo=[1, 2]),
  fichab("Lo que cubre el Régimen General", "Los incluidos en el Régimen General",
         "La del art. 42, **menos** cese de actividad y prestaciones no contributivas", "—",
         "El Régimen General **sí** cubre el **desempleo**; **no** el cese de actividad (propio de autónomos)."))}

{unidad("3.2 Régimen Especial de Autónomos (art. 314)",
  lit("LGSS", "a314", ["con excepción de la protección por desempleo y las prestaciones no contributivas", "estar al corriente en el pago de las cotizaciones"]),
  fichab("Lo que cubre el RETA", "Los incluidos en el RETA",
         "La del art. 42, **menos** desempleo y prestaciones no contributivas", "—",
         "Simetría de examen: el **RG** excluye el **cese de actividad**; el **RETA** excluye el **desempleo**. En el RETA, además, hay que estar **al corriente** en las cotizaciones."))}
""", 2)

T.ap("s20", "V.4 Las contingencias (LGSS, arts. 156, 157 y 158)", f"""
{unidad("4.1 Accidente de trabajo (art. 156)",
  lit("LGSS", "a156", ["toda lesión corporal que el trabajador sufra con ocasión o por consecuencia del trabajo que ejecute por cuenta ajena", "al ir o al volver del lugar de trabajo", "Se presumirá, salvo prueba en contrario", "fuerza mayor extraña al trabajo", "dolo o a imprudencia temeraria del trabajador accidentado", "La imprudencia profesional"], solo=[1, 2, 3, 10, 11, 12, 13, 14, 15, 16]),
  fichab("Contingencia profesional: accidente de trabajo",
         "El trabajador **por cuenta ajena**",
         ["Lesión corporal con ocasión o por consecuencia del trabajo", "Incluye el accidente **in itinere** (ir o volver del trabajo) y los demás supuestos del 156.2", "**Presunción**: lesiones en tiempo y lugar de trabajo"],
         "—",
         "**No** es AT: fuerza mayor **extraña** al trabajo, **dolo** o **imprudencia temeraria**. **Sí** lo es pese a la **imprudencia profesional**. Insolación y rayo **no** son fuerza mayor extraña."))}

{unidad("4.2 Enfermedad profesional (art. 157)",
  lit("LGSS", "a157", ["en las actividades que se especifiquen en el cuadro", "el informe del Ministerio de Sanidad, Servicios Sociales e Igualdad"]),
  fichab("Contingencia profesional: enfermedad profesional", "Trabajador por cuenta ajena",
         "Contraída por el trabajo en actividades **del cuadro**, provocada por los elementos o sustancias que el cuadro indique", "—",
         "Sistema de **lista** (cuadro). Una enfermedad causada por el trabajo que **no** esté en el cuadro puede ser **accidente de trabajo** (156.2 e)."))}

{unidad("4.3 Accidente no laboral y enfermedad común (art. 158)",
  lit("LGSS", "a158", ["no tenga el carácter de accidente de trabajo", "las alteraciones de la salud que no tengan la condición de accidentes de trabajo ni de enfermedades profesionales"]),
  fichab("Contingencias comunes", "—", "Se definen **por exclusión** de las profesionales", "—",
         "Accidente no laboral y enfermedad común se definen **en negativo**."))}

{resumen([
  "Acción protectora (42): asistencia **sanitaria**, **recuperación** profesional, prestaciones **económicas**, **familiares** y **servicios sociales**; y, como complemento, **asistencia social**. **Establece y limita** lo que cubre cada régimen.",
  "Mejoras **voluntarias** solo en lo **contributivo**; fuera de ellas, **nada de contratación colectiva** (43).",
  "RG: todo menos **cese de actividad** y no contributivas (155); RETA: todo menos **desempleo** y no contributivas (314).",
  "**AT**: lesión con ocasión o por consecuencia del trabajo por cuenta ajena, incluido **in itinere**; **EP**: la del **cuadro**; comunes, **por exclusión** (156 a 158)."],
  "Siguiente: VI. ¿Qué prestaciones da y cómo son?")}
""", 2)

# =============================================================================
T.ap("bVI", "VI. Tipos y características de las prestaciones (LGSS, arts. 44, 53, 165 y siguientes)", donde(
  "Sexta y última pregunta. Las **características** comunes de todas las prestaciones, las **condiciones** generales para tener derecho y los **tipos**: las principales contributivas del Régimen General y las no contributivas.",
  ["1 Caracteres y prescripción (arts. 44 y 53)", "2 Condiciones generales del derecho (art. 165)", "3 Incapacidad temporal y nacimiento y cuidado de menor (arts. 169, 172 y 177)", "4 Incapacidad permanente y jubilación (arts. 193, 194, 204 y 205)", "5 Muerte y supervivencia (art. 216)", "6 Prestaciones no contributivas (arts. 351, 363 y 369)", "7 Cuadro de las prestaciones"]))

T.ap("s21", "VI.1 Caracteres de las prestaciones y prescripción (LGSS, arts. 44 y 53)", f"""
{unidad("1.1 Caracteres (art. 44)",
  lit("LGSS", "a44", ["no podrán ser objeto de retención", "cesión total o parcial, compensación o descuento", "obligaciones alimenticias a favor del cónyuge e hijos", "obligaciones contraídas por el beneficiario dentro de la Seguridad Social", "estarán sujetas a tributación", "No podrá ser exigida ninguna tasa fiscal"]),
  ficha("Los beneficiarios de prestaciones, servicios sociales y asistencia social",
        ["Prestaciones no retenibles, no cedibles, no compensables ni descontables", "Embargo: según la Ley de Enjuiciamiento Civil", "Información y certificaciones gratuitas (sin tasas)"],
        ["::Excepciones a la intangibilidad:", "Obligaciones alimenticias a favor del cónyuge e hijos", "Obligaciones contraídas dentro de la Seguridad Social"],
        "—",
        "**Dos** excepciones: **alimentos** a cónyuge e hijos y deudas **con la propia Seguridad Social**. Las prestaciones **sí tributan** (44.2)."))}

{unidad("1.2 Prescripción del derecho (art. 53.1)",
  lit("LGSS", "a53", ["prescribirá a los cinco años", "a partir de los tres meses anteriores a la fecha en que se presente la correspondiente solicitud"], solo=[1]),
  fichab("Plazo para pedir el reconocimiento de una prestación", "El beneficiario",
         "Desde el día siguiente al hecho causante", "**Cinco años**; efectos económicos con retroactividad máxima de **tres meses** desde la solicitud",
         "**5 años** para pedirla, pero solo se cobran **3 meses** hacia atrás. Excepción conocida: la **jubilación** es **imprescriptible** (art. 212)."))}
""", 2)

T.ap("s22", "VI.2 Condiciones generales del derecho a las prestaciones (LGSS, art. 165)", f"""
{unidad("2.1 Afiliación y alta, y periodos de cotización (art. 165)",
  lit("LGSS", "a165", ["estar afiliadas y en alta en dicho Régimen o en situación asimilada a la de alta", "las cotizaciones efectivamente realizadas o las expresamente asimiladas", "No se exigirán períodos previos de cotización para el derecho a las prestaciones derivadas de accidente, sea o no de trabajo, o de enfermedad profesional"], solo=[1, 2, 4]),
  fichab("Requisitos comunes en el Régimen General",
         "Personas incluidas en el Régimen General",
         ["Requisito general: **afiliación y alta** (o situación **asimilada al alta**) al sobrevenir la contingencia", "Periodos de cotización: solo las **efectivamente realizadas** o asimiladas"],
         "Sin periodo previo para **accidente** (sea o no de trabajo) y **enfermedad profesional**",
         "El accidente **no laboral** tampoco exige carencia: «sea **o no** de trabajo». La **enfermedad común** sí."))}
""", 2)

T.ap("s23", "VI.3 Incapacidad temporal y nacimiento y cuidado de menor (LGSS, arts. 169, 172 y 177)", f"""
{unidad("3.1 Incapacidad temporal: concepto y duración (art. 169.1 a)",
  lit("LGSS", "a169", ["con una duración máxima de trescientos sesenta y cinco días, prorrogables por otros ciento ochenta días", "gestación de la mujer trabajadora desde el día primero de la semana trigésima novena"], solo=[1, 2, 3, 4]),
  ficha("Trabajadores impedidos para el trabajo que reciben asistencia sanitaria",
        ["Enfermedad común o profesional y accidente, sea o no de trabajo", "Situaciones especiales por contingencias comunes: menstruación incapacitante secundaria, interrupción del embarazo, gestación desde la semana 39 (y donación de órganos)"],
        "Máximo **365 días**, prorrogables **180** si se presume el alta por curación",
        "Subsidio económico (art. 171)",
        "**365 + 180** días. La gestación es IT especial desde el **primer día de la semana 39**."))}

{unidad("3.2 Incapacidad temporal: carencia (art. 172)",
  lit("LGSS", "a172", ["ciento ochenta días dentro de los cinco años inmediatamente anteriores al hecho causante", "no se exigirá ningún período previo de cotización"], solo=[1, 2, 4]),
  ficha("Beneficiarios del subsidio por IT", "Subsidio si se reúnen alta y carencia",
        ["Enfermedad común: **180 días** cotizados en los **5 años** anteriores", "Accidente (sea o no de trabajo) y EP: **sin** carencia"], "—",
        "**180 días en 5 años**, solo para **enfermedad común**."))}

{unidad("3.3 Nacimiento y cuidado de menor: situaciones protegidas (art. 177)",
  lit("LGSS", "a177", ["el nacimiento, la adopción, la guarda con fines de adopción y el acogimiento familiar"]),
  ficha("Los progenitores, adoptantes, guardadores o acogedores durante los descansos legales",
        "Prestación económica durante los periodos de descanso del ET (art. 48.4 a 6) y del TREBEP (art. 49 a, b y c)",
        "—", "—",
        "Cuatro situaciones: **nacimiento, adopción, guarda con fines de adopción y acogimiento familiar**."))}
""", 2)

T.ap("s24", "VI.4 Incapacidad permanente y jubilación (LGSS, arts. 193, 194, 204 y 205)", f"""
{unidad("4.1 Incapacidad permanente: concepto (art. 193.1)",
  lit("LGSS", "a193", ["reducciones anatómicas o funcionales graves, susceptibles de determinación objetiva y previsiblemente definitivas"], solo=[1]),
  ficha("La persona trabajadora que, tras el tratamiento prescrito, tiene reducciones graves y previsiblemente definitivas",
        "Prestaciones económicas según el grado (art. 196)",
        "No impide la calificación que la recuperación sea **incierta o a largo plazo**", "—",
        "Reducciones **graves**, **objetivables** y **previsiblemente definitivas** que disminuyan o anulen la capacidad laboral."))}

{unidad("4.2 Grados (art. 194.1)",
  lit("LGSS", "a194", ["Incapacidad permanente parcial", "Incapacidad permanente total", "Incapacidad permanente absoluta", "Gran incapacidad"], solo=[1, 2, 3, 4, 5]),
  fichab("Clasificación de la incapacidad permanente", "—",
         "En función del **porcentaje de reducción** de la capacidad de trabajo, según la lista de enfermedades reglamentaria",
         "—", "**Cuatro** grados: parcial, total, absoluta y **gran incapacidad**."))}

{unidad("4.3 Jubilación: concepto (art. 204)",
  lit("LGSS", "a204", ["será única para cada beneficiario y consistirá en una pensión vitalicia"]),
  ficha("Quien, alcanzada la edad, cesa o ha cesado en el trabajo por cuenta ajena",
        "Pensión **única** y **vitalicia** (modalidad contributiva)", "—", "Imprescriptible (art. 212)",
        "**Única** para cada beneficiario y **vitalicia**."))}

{unidad("4.4 Jubilación: edad y carencia (art. 205.1)",
  lit("LGSS", "a205", ["sesenta y siete años de edad, o sesenta y cinco años cuando se acrediten treinta y ocho años y seis meses de cotización", "un período mínimo de cotización de quince años, de los cuales al menos dos deberán estar comprendidos dentro de los quince años inmediatamente anteriores"], solo=[1, 2, 4]),
  ficha("Personas del Régimen General con alta o asimilada (o sin alta, art. 205.3)",
        "Pensión de jubilación contributiva",
        ["Edad: **67** años, o **65** con **38 años y 6 meses** cotizados", "Carencia: **15 años**, de ellos **2** en los **15** anteriores"],
        "—",
        "No cuentan las **pagas extraordinarias** para la edad ni para la carencia. La edad de 67 se aplica de forma paulatina (disp. trans. 7.ª)."))}
""", 2)

T.ap("s25", "VI.5 Muerte y supervivencia (LGSS, art. 216)", f"""
{unidad("5.1 Prestaciones por muerte (art. 216)",
  lit("LGSS", "a216", ["Un auxilio por defunción", "Una pensión vitalicia de viudedad", "Una prestación temporal de viudedad", "Una pensión de orfandad", "Una pensión vitalicia o, en su caso, subsidio temporal en favor de familiares", "una indemnización a tanto alzado"], solo=[1, 2, 3, 4, 5, 6, 7]),
  ficha("Supervivientes del causante, cualquiera que sea la causa de la muerte",
        ["a) Auxilio por defunción", "b) Pensión vitalicia de viudedad", "c) Prestación temporal de viudedad", "d) Pensión de orfandad", "e) Pensión vitalicia o subsidio temporal en favor de familiares"],
        "—",
        "Si la muerte es por **AT o EP**: además, **indemnización a tanto alzado**",
        "La **indemnización a tanto alzado** solo procede por **AT o EP**."))}
""", 2)

T.ap("s26", "VI.6 Prestaciones no contributivas (LGSS, arts. 351, 363 y 369)", f"""
{unidad("6.1 Prestaciones familiares no contributivas (art. 351)",
  lit("LGSS", "a351", ["afectado por una discapacidad en un grado igual o superior al 33 por ciento", "familias numerosas, monoparentales y en los casos de madres o padres con discapacidad", "por parto o adopción múltiples"], solo=[1, 2, 5, 6]),
  ficha("Familias con hijos o menores a cargo en los supuestos legales",
        ["a) Asignación por hijo o menor a cargo con discapacidad (≥ 33 % si es menor de 18; ≥ 65 % si es mayor)", "b) Pago único por nacimiento o adopción en familias numerosas, monoparentales o con progenitores con discapacidad", "c) Pago único por parto o adopción múltiples"],
        "—", "—",
        "Umbrales: **33 %** (menores de 18) y **65 %** (mayores de 18)."))}

{unidad("6.2 Pensión de invalidez no contributiva (art. 363.1)",
  lit("LGSS", "a363", ["Ser mayor de dieciocho y menor de sesenta y cinco años de edad", "durante cinco años, de los cuales dos deberán ser inmediatamente anteriores", "en un grado igual o superior al 65 por ciento", "Carecer de rentas o ingresos suficientes"], solo=[1, 2, 3, 4, 5]),
  ficha("Personas de **18 a 64 años** con discapacidad o enfermedad crónica ≥ **65 %**",
        "Pensión no contributiva (la gestiona el IMSERSO o el órgano autonómico: → I.3.1)",
        ["Residencia legal: **5 años**, **2** inmediatamente anteriores a la solicitud", "Carencia de rentas"],
        "—",
        "**65 %** de discapacidad; residencia **5 años** (2 inmediatos)."))}

{unidad("6.3 Pensión de jubilación no contributiva (art. 369.1)",
  lit("LGSS", "a369", ["habiendo cumplido sesenta y cinco años de edad", "durante diez años entre la edad de dieciséis años y la edad de devengo de la pensión"], solo=[1]),
  ficha("Personas de **65 o más años** sin rentas suficientes",
        "Pensión no contributiva de jubilación",
        ["Residencia legal: **10 años** entre los **16** y la edad de devengo, **2** consecutivos e inmediatamente anteriores", "Rentas por debajo de los límites del art. 363"],
        "—",
        "No contributiva: **65** años y **10** de residencia; contributiva: **67** (o 65 con 38 años y 6 meses) y **15** de cotización."))}
""", 2)

T.ap("s27", "VI.7 Cuadro de las prestaciones (esquema)", f"""
{NOLEGAL}

| Prestación | Modalidad | Requisito clave | Artículo |
|---|---|---|---|
| Incapacidad temporal | Contributiva | Enfermedad común: 180 días en 5 años; accidente y EP: sin carencia; 365 + 180 días | 169, 172 |
| Nacimiento y cuidado de menor | Contributiva | Nacimiento, adopción, guarda con fines de adopción, acogimiento | 177 |
| Incapacidad permanente | Contributiva | Reducciones graves y previsiblemente definitivas; cuatro grados | 193, 194 |
| Jubilación | Contributiva | 67 años (65 con 38 años y 6 meses); 15 años cotizados | 204, 205 |
| Muerte y supervivencia | Contributiva | Auxilio, viudedad, orfandad, favor de familiares; AT/EP: indemnización | 216 |
| Invalidez no contributiva | No contributiva | 18 a 64 años; ≥ 65 %; 5 años de residencia | 363 |
| Jubilación no contributiva | No contributiva | 65 años; 10 años de residencia | 369 |
| Prestaciones familiares | No contributiva | Hijo con discapacidad; pagos únicos | 351 |
| Desempleo | Contributivo y asistencial | Tema III.5 | 262 y ss. |

{resumen([
  "Las prestaciones **no se retienen, ceden, compensan ni descuentan**, salvo **alimentos** y deudas **con la Seguridad Social**; **tributan** (44).",
  "El derecho a pedirlas **prescribe a los 5 años**; los efectos, como máximo **3 meses** antes de la solicitud (53).",
  "Requisito general: **afiliación y alta** o asimilada; sin carencia por **accidente** (sea o no de trabajo) y **EP** (165).",
  "IT **365 + 180** días; jubilación a los **67** (o **65** con **38 años y 6 meses**) con **15** años cotizados; no contributivas: invalidez **18-64** y **65 %**, jubilación **65** y **10** años de residencia."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_P28 = examen("P", 28, {
  "a": f"El Estado no tiene «toda la gestión»: el art. 149.1.17.ª reserva al Estado la legislación básica y el régimen económico {c('CE', 'Artículo 149', 'sin perjuicio de la ejecución de sus servicios por las Comunidades Autónomas')}.",
  "b": f"Literal del art. 149.1.17.ª: {c('CE', 'Artículo 149', 'Legislación básica y régimen económico de la Seguridad Social')}.",
  "c": "Las prestaciones asistenciales autonómicas no figuran en el art. 149.1.17.ª, que se refiere a la Seguridad Social; la ley además salva las ayudas que puedan establecer las comunidades autónomas (LGSS, art. 42.4).",
  "d": f"Las políticas de empleo no son el contenido del art. 149.1.17.ª; en materia laboral, el art. 149.1.7.ª atribuye al Estado la {c('CE', 'Artículo 149', 'Legislación laboral; sin perjuicio de su ejecución por los órganos de las Comunidades Autónomas')}."},
  [("Legislación básica y régimen económico de la Seguridad Social", "CE", "Artículo 149", "17.ª Legislación básica y régimen económico de la Seguridad Social, sin perjuicio de la ejecución de sus servicios por las Comunidades Autónomas")])
EX_P29 = examen("P", 29, {
  "a": f"Cambia «contributivo» por «no contributivo». Las no contributivas las financia el Estado (art. 109.2); el Fondo es para las {c('LGSS', 'a121', 'pensiones de carácter contributivo')}.",
  "b": f"Literal del art. 121.1: {c('LGSS', 'a121', 'se destinará con carácter exclusivo a la financiación de las pensiones de carácter contributivo')}.",
  "c": f"Añade el MEI, que no es un destino del Fondo sino un ingreso: {c('LGSS', 'a118', 'Los ingresos obtenidos de la cotización finalista fijada en el artículo 127 bis. 1 se ingresarán en el Fondo de Reserva')} (art. 118.4). El destino es «con carácter exclusivo» las pensiones contributivas.",
  "d": "Cambia el tipo de pensión (no contributivas) y añade el MEI: falla por los dos lados (arts. 121.1 y 118.4)."},
  [("pensiones de carácter contributivo.", "LGSS", "a121", "se destinará con carácter exclusivo a la financiación de las pensiones de carácter contributivo")])
POR125 = {
  "a": f"Literal del art. 125.3: {c('LGSS', 'a125', 'La Comisión de Seguimiento conocerá semestralmente de la evolución y composición del Fondo de Reserva')}.",
  "b": f"Cambia el plazo. Anual es el **informe** del art. 127, no el conocimiento de la Comisión de Seguimiento, que es {c('LGSS', 'a125', 'semestralmente')}.",
  "c": f"Cambia el plazo: la ley dice {c('LGSS', 'a125', 'semestralmente')}, no cada tres meses.",
  "d": f"Cambia el plazo: la ley dice {c('LGSS', 'a125', 'semestralmente')}, no cada dos meses."}
AP125 = [("Semestralmente", "LGSS", "a125", "La Comisión de Seguimiento conocerá semestralmente de la evolución y composición del Fondo de Reserva de la Seguridad Social")]
EX_L35 = examen("L", 35, POR125, AP125)
EX_P30 = examen("P", 30, POR125, AP125)

T.ap("s28", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **cinco** preguntas de este tema. Aquí están **cuatro**, **literales** (la del Fondo de Reserva se repitió en el turno libre y en promoción interna). Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-P 2025, pregunta 28 · Competencia del Estado (→ I.1.4)", EX_P28,
  "### GACE-P 2025, pregunta 29 · Destino del Fondo de Reserva (→ II.3.3)", EX_P29,
  "### GACE-L 2025, pregunta 35 · Comisión de Seguimiento del Fondo de Reserva (→ II.3.4)", EX_L35,
  "### GACE-P 2025, pregunta 30 · Comisión de Seguimiento del Fondo de Reserva (→ II.3.4)", EX_P30,
  f"?> **GACE-X 2025, pregunta 44** («¿Cuáles son las características de las aportaciones del Estado como fuente de financiación de la Seguridad Social?»). La plantilla da como correcta la d) «Intervienen en la función redistribuidora de los tributos y tienen carácter finalista». Esa caracterización **no está en la ley**: el art. 109 LGSS solo dice que son {c('LGSS', 'a109', 'Las aportaciones progresivas del Estado, que se consignarán con carácter permanente en sus Presupuestos Generales')} y que financian la modalidad {c('LGSS', 'a109', 'no contributiva y universal')} (→ II.1.2 y → II.1.3). Como no se puede comprobar contra el texto legal, no se publica aquí ni en el test.",
  "### Cómo se pregunta",
  "!> Las preguntas del Fondo de Reserva cambian **un plazo** (semestral / anual / trimestral) o **añaden algo** al destino (el MEI, que es un **ingreso** del Fondo). La del art. 149.1.17.ª contrapone «legislación básica y régimen económico» a «toda la gestión».",
]))

T.ap("s29", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Estructura | Art. 41 CE; 149.1.17.ª; principios (LGSS 2); INSS, INGESA, IMSERSO; Tesorería; mutuas | Estado: **legislación básica y régimen económico** |
| II. Financiación | Cotización obligatoria; recursos (109); reparto (110); Fondo de Reserva; MEI | Comisión de Seguimiento: **semestralmente**; Fondo: solo **pensiones contributivas** |
| III. Problemas y líneas | Pacto de Toledo 2020; baby boom; revalorización IPC; base máxima, solidaridad, MEI | Revalorización: media del IPC de **12 meses** previos a diciembre |
| IV. Regímenes | Régimen General y especiales; sistemas especiales; RG (136); RETA (305) | Mar y funcionarios: **leyes específicas** |
| V. Acción protectora | Art. 42; mejoras voluntarias; RG y RETA; AT, EP, comunes | RG sin **cese de actividad**; RETA sin **desempleo** |
| VI. Prestaciones | Caracteres (44); prescripción (53); alta y carencia (165); IT, IP, jubilación, muerte; no contributivas | Prescripción **5 años**; IT **365 + 180** días |

?> **Trampas frecuentes:** «el Estado tiene competencia exclusiva sobre **toda la gestión**» (solo **legislación básica y régimen económico**); «el Fondo de Reserva financia el **MEI**» (el MEI **nutre** el Fondo); «la Comisión de Seguimiento conoce **anualmente**» (es **semestralmente**); «las pensiones no contributivas las gestiona el **INSS**» (las gestiona el **IMSERSO**); «el accidente **no laboral** exige periodo de cotización» (no: «sea **o no** de trabajo»); «los principios son universalidad, unidad, solidaridad y **suficiencia**» (es **igualdad**).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
Q = T.q
Q("CE", "Artículo 41", "Fundamento constitucional", "Según el artículo 41 de la Constitución, los poderes públicos mantendrán un régimen público de Seguridad Social para todos los ciudadanos que garantice la asistencia y prestaciones sociales suficientes ante situaciones de necesidad, especialmente en caso de:",
  ["Desempleo.", "Jubilación.", "Enfermedad.", "Incapacidad permanente."], "Art. 41 CE: «especialmente en caso de desempleo».", "especialmente en caso de desempleo")
Q("CE", "Artículo 41", "Fundamento constitucional", "Según el artículo 41 de la Constitución, la asistencia y prestaciones complementarias:",
  ["Serán libres.", "Serán obligatorias.", "Se financiarán por el Estado.", "Corresponderán a las Comunidades Autónomas."], "Art. 41 CE.", "La asistencia y prestaciones complementarias serán libres")
Q("CE", "Artículo 149", "Fundamento constitucional", "Según el artículo 149.1.17.ª de la Constitución, la ejecución de los servicios de la Seguridad Social:",
  ["Puede corresponder a las Comunidades Autónomas.", "Corresponde en exclusiva al Estado.", "Corresponde a las Corporaciones locales.", "Corresponde a las mutuas colaboradoras."], "Art. 149.1.17.ª CE: «sin perjuicio de la ejecución de sus servicios por las Comunidades Autónomas».", "sin perjuicio de la ejecución de sus servicios por las Comunidades Autónomas")
Q("LGSS", "a2", "Estructura", "Según el artículo 2.1 de la LGSS, el sistema de la Seguridad Social se fundamenta en los principios de:",
  ["Universalidad, unidad, solidaridad e igualdad.", "Universalidad, unidad, solidaridad y suficiencia.", "Contributividad, solidaridad y equidad.", "Unidad, descentralización y eficacia social."], "Art. 2.1 LGSS.", "universalidad, unidad, solidaridad e igualdad")
Q("LGSS", "a4", "Estructura", "Según el artículo 4.1 de la LGSS, corresponde al Estado:",
  ["La ordenación, jurisdicción e inspección de la Seguridad Social.", "La gestión de todas las prestaciones de la Seguridad Social.", "La ordenación y la gestión de la Seguridad Social.", "La inspección de la Seguridad Social, en exclusiva."], "Art. 4.1 LGSS.", "Corresponde al Estado la ordenación, jurisdicción e inspección de la Seguridad Social")
Q("LGSS", "a66", "Estructura", "Según el artículo 66 de la LGSS, la gestión de las pensiones no contributivas de invalidez y de jubilación corresponde a:",
  ["El Instituto de Mayores y Servicios Sociales.", "El Instituto Nacional de la Seguridad Social.", "La Tesorería General de la Seguridad Social.", "El Instituto Nacional de Gestión Sanitaria."], "Art. 66.1 c) LGSS.", "El Instituto de Mayores y Servicios Sociales, para la gestión de las pensiones no contributivas de invalidez y de jubilación")
Q("LGSS", "a66", "Estructura", "Según el artículo 66 de la LGSS, la administración y gestión de servicios sanitarios corresponde a:",
  ["El Instituto Nacional de Gestión Sanitaria.", "El Instituto Nacional de la Seguridad Social.", "El Instituto de Mayores y Servicios Sociales.", "La Gerencia de Informática de la Seguridad Social."], "Art. 66.1 b) LGSS.", "El Instituto Nacional de Gestión Sanitaria, para la administración y gestión de servicios sanitarios")
Q("LGSS", "a68", "Estructura", "Según el artículo 68 de la LGSS, las entidades gestoras tienen la naturaleza de:",
  ["Entidades de derecho público.", "Sociedades mercantiles estatales.", "Fundaciones del sector público.", "Asociaciones privadas de interés público."], "Art. 68.1 LGSS.", "Las entidades gestoras tienen la naturaleza de entidades de derecho público")
Q("LGSS", "a74", "Estructura", "Según el artículo 74 de la LGSS, la Tesorería General de la Seguridad Social es:",
  ["Un servicio común con personalidad jurídica propia.", "Una entidad gestora sin personalidad jurídica.", "Un órgano directivo del Ministerio de Hacienda.", "Una entidad colaboradora."], "Art. 74.1 LGSS.", "es un servicio común con personalidad jurídica propia")
Q("LGSS", "a74", "Estructura", "Según el artículo 74 de la LGSS, en la Tesorería General de la Seguridad Social se unifican todos los recursos financieros por aplicación de los principios de:",
  ["Solidaridad financiera y caja única.", "Eficacia y eficiencia.", "Descentralización y desconcentración.", "Universalidad y presupuesto único."], "Art. 74.1 LGSS.", "por aplicación de los principios de solidaridad financiera y caja única")
Q("LGSS", "a80", "Estructura", "Según el artículo 80 de la LGSS, las mutuas colaboradoras con la Seguridad Social son:",
  ["Asociaciones privadas de empresarios, sin ánimo de lucro.", "Entidades de derecho público adscritas a la Tesorería General.", "Sociedades mercantiles de seguros.", "Asociaciones de trabajadores con ánimo de lucro."], "Art. 80.1 LGSS.", ["asociaciones privadas de empresarios", "sin ánimo de lucro"])
Q("LGSS", "a80", "Estructura", "Según el artículo 80.4 de la LGSS, las mutuas colaboradoras con la Seguridad Social forman parte:",
  ["Del sector público estatal de carácter administrativo.", "Del sector público estatal de carácter empresarial.", "Del sector privado, sin vinculación con el sector público.", "Del sector público autonómico."], "Art. 80.4 LGSS.", "forman parte del sector público estatal de carácter administrativo")
Q("LGSS", "a18", "Financiación", "Según el artículo 18 de la LGSS, la cotización a la Seguridad Social:",
  ["Es obligatoria en todos los regímenes del sistema.", "Es obligatoria solo en el Régimen General.", "Es voluntaria para los trabajadores autónomos.", "Es obligatoria solo para las contingencias profesionales."], "Art. 18.1 LGSS.", "La cotización a la Seguridad Social es obligatoria en todos los regímenes del sistema")
Q("LGSS", "a109", "Financiación", "Según el artículo 109.1 a) de la LGSS, las aportaciones del Estado a la financiación de la Seguridad Social son:",
  ["Progresivas y se consignan con carácter permanente en sus Presupuestos Generales.", "Decrecientes y se consignan con carácter temporal.", "Extraordinarias y solo para atenciones especiales.", "Finalistas y se consignan en el presupuesto de la Tesorería General."], "Art. 109.1 a) LGSS.", "Las aportaciones progresivas del Estado, que se consignarán con carácter permanente en sus Presupuestos Generales")
Q("LGSS", "a109", "Financiación", "Según el artículo 109.2 de la LGSS, la acción protectora de la Seguridad Social en su modalidad no contributiva y universal se financiará mediante:",
  ["Aportaciones del Estado al Presupuesto de la Seguridad Social.", "Cuotas de empresarios y trabajadores.", "El Fondo de Reserva de la Seguridad Social.", "Los excedentes de las mutuas colaboradoras."], "Art. 109.2 LGSS.", "se financiará mediante aportaciones del Estado al Presupuesto de la Seguridad Social")
Q("LGSS", "a109", "Financiación", "Según el artículo 109.3 de la LGSS, tienen naturaleza no contributiva:",
  ["Los complementos por mínimos de las pensiones de la Seguridad Social.", "Las prestaciones derivadas de accidentes de trabajo.", "Las pensiones de jubilación contributivas.", "Las prestaciones por incapacidad temporal."], "Art. 109.3 b) 4.ª LGSS.", "Los complementos por mínimos de las pensiones de la Seguridad Social")
Q("LGSS", "a109", "Financiación", "Según el artículo 109.3 de la LGSS, las prestaciones derivadas de las contingencias de accidentes de trabajo y enfermedades profesionales tienen naturaleza:",
  ["Contributiva, en su totalidad.", "No contributiva, en su totalidad.", "Contributiva, salvo la asistencia sanitaria.", "Mixta."], "Art. 109.3 a) 2.ª LGSS: «La totalidad de las prestaciones derivadas de las contingencias de accidentes de trabajo y enfermedades profesionales».", "La totalidad de las prestaciones derivadas de las contingencias de accidentes de trabajo y enfermedades profesionales")
Q("LGSS", "a110", "Financiación", "Según el artículo 110 de la LGSS, el sistema financiero de todos los regímenes del sistema de la Seguridad Social será el de:",
  ["Reparto.", "Capitalización individual.", "Capitalización colectiva.", "Reparto de capitales de cobertura."], "Art. 110.1 LGSS.", "será el de reparto")
Q("LGSS", "a110", "Financiación", "Según el artículo 110.2 de la LGSS, el fondo de estabilización único para todo el sistema se constituirá en:",
  ["La Tesorería General de la Seguridad Social.", "El Instituto Nacional de la Seguridad Social.", "El Banco de España.", "El Ministerio de Hacienda."], "Art. 110.2 LGSS.", "En la Tesorería General de la Seguridad Social se constituirá un fondo de estabilización único")
Q("LGSS", "a117", "Financiación", "Según el artículo 117 de la LGSS, el Fondo de Reserva de la Seguridad Social tiene la finalidad de atender las necesidades financieras en materia de:",
  ["Prestaciones contributivas.", "Prestaciones no contributivas.", "Asistencia sanitaria.", "Servicios sociales."], "Art. 117 LGSS.", "atender las necesidades financieras en materia de prestaciones contributivas")
Q("LGSS", "a1-5", "Financiación", "Según el artículo 127 bis de la LGSS, la cotización del Mecanismo de Equidad Intergeneracional será de:",
  ["1,2 puntos porcentuales.", "0,6 puntos porcentuales.", "2 puntos porcentuales.", "1 punto porcentual."], "Art. 127 bis.1 LGSS.", "La cotización será de 1,2 puntos porcentuales")
Q("LGSS", "a1-5", "Financiación", "Según el artículo 127 bis de la LGSS, en el caso de trabajadores por cuenta ajena, la cotización del Mecanismo de Equidad Intergeneracional se distribuye así:",
  ["Un punto porcentual la empresa y 0,2 puntos porcentuales el trabajador.", "0,6 puntos porcentuales cada uno.", "0,2 puntos porcentuales la empresa y un punto porcentual el trabajador.", "La totalidad corresponde a la empresa."], "Art. 127 bis.1 LGSS.", "un punto porcentual corresponderá a la empresa y 0,2 puntos porcentuales al trabajador")
Q("LGSS", "a1-5", "Financiación", "Según el artículo 127 bis de la LGSS, la cotización finalista del Mecanismo de Equidad Intergeneracional:",
  ["No será computable a efectos de prestaciones.", "Será computable a efectos de la pensión de jubilación.", "Podrá ser objeto de bonificación.", "Nutrirá el fondo de estabilización."], "Art. 127 bis.1 LGSS.", "que no será computable a efectos de prestaciones")
Q("LGSS", "a58", "Problemas y líneas de actuación", "Según el artículo 58.2 de la LGSS, las pensiones contributivas se revalorizarán al comienzo de cada año en el porcentaje equivalente:",
  ["Al valor medio de las tasas de variación interanual del IPC de los doce meses previos a diciembre del año anterior.", "A la tasa de variación interanual del IPC del mes de diciembre del año anterior.", "Al índice de revalorización que fije la Ley de Presupuestos.", "Al crecimiento del PIB del año anterior."], "Art. 58.2 LGSS.", "valor medio de las tasas de variación interanual expresadas en tanto por ciento del Índice de Precios al Consumo de los doce meses previos a diciembre del año anterior")
Q("LGSS", "a58", "Problemas y líneas de actuación", "Según el artículo 58.3 de la LGSS, si el valor medio del IPC que sirve para revalorizar las pensiones fuera negativo:",
  ["El importe de las pensiones no variará al comienzo del año.", "Las pensiones se reducirán en ese porcentaje.", "Las pensiones se reducirán en la mitad de ese porcentaje.", "Lo decidirá la Ley de Presupuestos."], "Art. 58.3 LGSS.", "el importe de las pensiones no variará al comienzo del año")
Q("L21_2021", "pr", "Problemas y líneas de actuación", "Según el preámbulo de la Ley 21/2021, el Informe de evaluación y reforma del Pacto de Toledo fue aprobado por:",
  ["El pleno del Congreso de los Diputados.", "El Consejo de Ministros.", "El Pleno del Senado.", "La Comisión del Pacto de Toledo del Senado."], "Preámbulo, I, Ley 21/2021.", "el pleno del Congreso de los Diputados aprobó el Informe de evaluación y reforma del Pacto de Toledo")
Q("LGSS", "a10", "Regímenes", "Según el artículo 10.3 de la LGSS, ¿qué regímenes especiales se regirán por las leyes específicas que se dicten al efecto?",
  ["Los de los trabajadores del mar y de los funcionarios públicos, civiles y militares.", "Los de los trabajadores autónomos y de los estudiantes.", "Los de los trabajadores del mar y de los autónomos.", "Los de los estudiantes y de los funcionarios públicos."], "Art. 10.3 LGSS, en relación con las letras b) y c) del 10.2.", ["Los regímenes especiales correspondientes a los grupos incluidos en las letras b) y c) del apartado anterior se regirán por las leyes específicas", "Trabajadores del mar", "Funcionarios públicos, civiles y militares"])
Q("LGSS", "a11", "Regímenes", "Según el artículo 11 de la LGSS, los sistemas especiales podrán establecerse exclusivamente en materia de:",
  ["Encuadramiento, afiliación, forma de cotización o recaudación.", "Acción protectora y cuantía de las prestaciones.", "Edad de jubilación y periodos de carencia.", "Gestión y colaboración en la gestión."], "Art. 11 LGSS.", "encuadramiento, afiliación, forma de cotización o recaudación")
Q("LGSS", "a136", "Regímenes", "Según el artículo 136.2 a) de la LGSS, los trabajadores incluidos en el Sistema Especial para Empleados de Hogar están comprendidos en:",
  ["El Régimen General de la Seguridad Social.", "El Régimen Especial de Trabajadores Autónomos.", "Un régimen especial propio.", "Ningún régimen: quedan excluidos."], "Art. 136.2 a) LGSS.", "Sistema Especial para Empleados de Hogar")
Q("LGSS", "a305", "Regímenes", "Según el artículo 305.1 de la LGSS, están obligatoriamente incluidas en el RETA las personas físicas que realicen la actividad por cuenta propia siendo mayores de:",
  ["Dieciocho años.", "Dieciséis años.", "Veintiún años.", "Catorce años."], "Art. 305.1 LGSS.", "las personas físicas mayores de dieciocho años")
Q("LGSS", "a42", "Acción protectora", "Según el artículo 42.3 de la LGSS, la acción protectora del sistema:",
  ["Establece y limita el ámbito de extensión posible del Régimen General y de los especiales.", "Solo se aplica al Régimen General.", "Puede ser ampliada libremente por cada régimen especial.", "Puede ser objeto de contratación colectiva."], "Art. 42.3 LGSS.", "establece y limita el ámbito de extensión posible del Régimen General y de los especiales")
Q("LGSS", "a43", "Acción protectora", "Según el artículo 43.2 de la LGSS, sin otra excepción que el establecimiento de mejoras voluntarias, la Seguridad Social:",
  ["No podrá ser objeto de contratación colectiva.", "Podrá ser objeto de contratación colectiva.", "Solo podrá mejorarse por ley.", "Podrá mejorarse por convenio en las prestaciones no contributivas."], "Art. 43.2 LGSS.", "la Seguridad Social no podrá ser objeto de contratación colectiva")
Q("LGSS", "a155", "Acción protectora", "Según el artículo 155.1 de la LGSS, la acción protectora del Régimen General será la del artículo 42, con excepción de:",
  ["La protección por cese de actividad y las prestaciones no contributivas.", "La protección por desempleo y las prestaciones no contributivas.", "La asistencia sanitaria y la recuperación profesional.", "Las prestaciones familiares."], "Art. 155.1 LGSS.", "con excepción de la protección por cese de actividad y las prestaciones no contributivas")
Q("LGSS", "a314", "Acción protectora", "Según el artículo 314 de la LGSS, la acción protectora del Régimen Especial de Trabajadores Autónomos será la del artículo 42, con excepción de:",
  ["La protección por desempleo y las prestaciones no contributivas.", "La protección por cese de actividad y las prestaciones no contributivas.", "La incapacidad temporal.", "La jubilación."], "Art. 314 LGSS.", "con excepción de la protección por desempleo y las prestaciones no contributivas")
Q("LGSS", "a156", "Acción protectora", "Según el artículo 156.4 de la LGSS, NO tendrán la consideración de accidente de trabajo los debidos a:",
  ["Dolo o imprudencia temeraria del trabajador accidentado.", "La imprudencia profesional derivada de la confianza que inspira el trabajo habitual.", "La insolación sufrida en el trabajo.", "La culpabilidad civil de un compañero de trabajo."], "Art. 156.4 b) LGSS; la imprudencia profesional, la insolación y la culpa de un compañero no impiden la calificación (156.4 a y 5).", "dolo o a imprudencia temeraria del trabajador accidentado")
Q("LGSS", "a156", "Acción protectora", "Según el artículo 156.2 a) de la LGSS, tendrán la consideración de accidentes de trabajo:",
  ["Los que sufra el trabajador al ir o al volver del lugar de trabajo.", "Solo los ocurridos dentro del centro de trabajo.", "Los debidos a fuerza mayor extraña al trabajo.", "Los ocurridos durante las vacaciones."], "Art. 156.2 a) LGSS (accidente in itinere).", "Los que sufra el trabajador al ir o al volver del lugar de trabajo")
Q("LGSS", "a44", "Prestaciones", "Según el artículo 44.1 de la LGSS, las prestaciones de la Seguridad Social podrán ser objeto de retención, cesión, compensación o descuento:",
  ["En orden al cumplimiento de las obligaciones alimenticias a favor del cónyuge e hijos.", "Para el pago de deudas tributarias de cualquier clase.", "Para el pago de deudas con entidades financieras.", "En ningún caso."], "Art. 44.1 a) LGSS; la otra excepción son las obligaciones contraídas dentro de la Seguridad Social.", "En orden al cumplimiento de las obligaciones alimenticias a favor del cónyuge e hijos")
Q("LGSS", "a53", "Prestaciones", "Según el artículo 53.1 de la LGSS, el derecho al reconocimiento de las prestaciones prescribirá:",
  ["A los cinco años.", "A los cuatro años.", "Al año.", "A los diez años."], "Art. 53.1 LGSS.", "prescribirá a los cinco años")
Q("LGSS", "a165", "Prestaciones", "Según el artículo 165.4 de la LGSS, no se exigirán períodos previos de cotización para el derecho a las prestaciones derivadas de:",
  ["Accidente, sea o no de trabajo, o de enfermedad profesional.", "Enfermedad común.", "Accidente de trabajo únicamente.", "Cualquier contingencia común."], "Art. 165.4 LGSS.", "derivadas de accidente, sea o no de trabajo, o de enfermedad profesional")
Q("LGSS", "a169", "Prestaciones", "Según el artículo 169.1 a) de la LGSS, la incapacidad temporal tendrá una duración máxima de:",
  ["Trescientos sesenta y cinco días, prorrogables por otros ciento ochenta días.", "Doce meses, prorrogables por otros seis meses.", "Quinientos cuarenta y cinco días, improrrogables.", "Trescientos sesenta y cinco días, prorrogables por otros trescientos sesenta y cinco."], "Art. 169.1 a) LGSS.", "con una duración máxima de trescientos sesenta y cinco días, prorrogables por otros ciento ochenta días")
Q("LGSS", "a172", "Prestaciones", "Según el artículo 172 de la LGSS, en caso de enfermedad común, para ser beneficiario del subsidio por incapacidad temporal se exige haber cotizado:",
  ["Ciento ochenta días dentro de los cinco años inmediatamente anteriores al hecho causante.", "Trescientos sesenta días dentro de los siete años anteriores.", "Noventa días dentro del año anterior.", "Ningún período previo."], "Art. 172 a) LGSS.", "ciento ochenta días dentro de los cinco años inmediatamente anteriores al hecho causante")
Q("LGSS", "a194", "Prestaciones", "Según el artículo 194 de la LGSS, ¿cuál de los siguientes NO es un grado de incapacidad permanente?",
  ["Incapacidad permanente temporal.", "Incapacidad permanente parcial.", "Incapacidad permanente absoluta.", "Gran incapacidad."], "Art. 194.1 LGSS: parcial, total, absoluta y gran incapacidad.", ["Incapacidad permanente parcial", "Incapacidad permanente absoluta", "Gran incapacidad"])
Q("LGSS", "a205", "Prestaciones", "Según el artículo 205.1 b) de la LGSS, para la pensión de jubilación contributiva se exige un período mínimo de cotización de:",
  ["Quince años, de los cuales al menos dos dentro de los quince años inmediatamente anteriores.", "Quince años, de los cuales al menos cinco dentro de los diez años anteriores.", "Diez años, de los cuales al menos dos dentro de los quince años anteriores.", "Veinte años, sin otro requisito."], "Art. 205.1 b) LGSS.", "un período mínimo de cotización de quince años, de los cuales al menos dos deberán estar comprendidos dentro de los quince años inmediatamente anteriores")
Q("LGSS", "a205", "Prestaciones", "Según el artículo 205.1 a) de la LGSS, se puede acceder a la pensión de jubilación a los sesenta y cinco años cuando se acrediten:",
  ["Treinta y ocho años y seis meses de cotización.", "Treinta y cinco años de cotización.", "Cuarenta años de cotización.", "Treinta y siete años de cotización."], "Art. 205.1 a) LGSS.", "sesenta y cinco años cuando se acrediten treinta y ocho años y seis meses de cotización")
Q("LGSS", "a216", "Prestaciones", "Según el artículo 216.2 de la LGSS, en caso de muerte causada por accidente de trabajo o enfermedad profesional se reconocerá, además:",
  ["Una indemnización a tanto alzado.", "Un auxilio por defunción doble.", "Una pensión de viudedad incrementada en un 50 por ciento.", "Un subsidio de orfandad vitalicio."], "Art. 216.2 LGSS.", "se reconocerá, además, una indemnización a tanto alzado")
Q("LGSS", "a363", "Prestaciones", "Según el artículo 363.1 de la LGSS, para tener derecho a la pensión de incapacidad no contributiva se exige estar afectado por una discapacidad o enfermedad crónica en un grado igual o superior al:",
  ["65 por ciento.", "33 por ciento.", "50 por ciento.", "75 por ciento."], "Art. 363.1 c) LGSS.", "en un grado igual o superior al 65 por ciento")
Q("LGSS", "a369", "Prestaciones", "Según el artículo 369.1 de la LGSS, para la pensión de jubilación no contributiva se exige haber residido legalmente en territorio español durante:",
  ["Diez años entre la edad de dieciséis años y la edad de devengo de la pensión.", "Cinco años, dos de ellos inmediatamente anteriores a la solicitud.", "Quince años entre los dieciocho y los sesenta y cinco.", "Veinte años en cualquier momento."], "Art. 369.1 LGSS.", "durante diez años entre la edad de dieciséis años y la edad de devengo de la pensión")
T.real("P", 28, "Fundamento constitucional"); T.real("P", 29, "Financiación"); T.real("L", 35, "Financiación"); T.real("P", 30, "Financiación")

# Flashcards
for q_, a_, cat in [
  ("¿Qué garantiza el art. 41 CE?", "Un régimen público de Seguridad Social para todos los ciudadanos, con asistencia y prestaciones suficientes ante situaciones de necesidad, especialmente en caso de desempleo; lo complementario es libre.", "Fundamento constitucional"),
  ("Competencia exclusiva del Estado (art. 149.1.17.ª CE)", "Legislación básica y régimen económico de la Seguridad Social, sin perjuicio de la ejecución de sus servicios por las CC. AA.", "Fundamento constitucional"),
  ("Principios del sistema (LGSS, art. 2.1)", "Universalidad, unidad, solidaridad e igualdad.", "Estructura"),
  ("Entidades gestoras (LGSS, art. 66)", "INSS (prestaciones económicas), INGESA (servicios sanitarios) e IMSERSO (pensiones no contributivas de invalidez y jubilación y servicios complementarios).", "Estructura"),
  ("Servicios comunes con personalidad jurídica propia (LGSS, arts. 74 y 74 bis)", "Tesorería General de la Seguridad Social (caja única) y Gerencia de Informática de la Seguridad Social.", "Estructura"),
  ("¿Qué son las mutuas colaboradoras? (LGSS, art. 80)", "Asociaciones privadas de empresarios, sin ánimo de lucro, con responsabilidad mancomunada de sus asociados; forman parte del sector público estatal de carácter administrativo.", "Estructura"),
  ("Recursos de la Seguridad Social (LGSS, art. 109.1)", "Aportaciones progresivas del Estado; cuotas; recargos y sanciones; frutos y rentas del patrimonio; otros ingresos.", "Financiación"),
  ("¿Quién financia lo no contributivo y quién lo contributivo? (art. 109.2)", "No contributivo y universal: aportaciones del Estado. Contributivo: básicamente cuotas y demás recursos.", "Financiación"),
  ("Sistema financiero (LGSS, art. 110)", "Reparto, con fondo de estabilización en la Tesorería; capitalización de pensiones de IP o muerte por AT/EP a cargo de mutuas o empresas.", "Financiación"),
  ("Destino del Fondo de Reserva (art. 121.1)", "Con carácter exclusivo, la financiación de las pensiones de carácter contributivo.", "Financiación"),
  ("¿Cada cuánto conoce la Comisión de Seguimiento la evolución del Fondo de Reserva? (art. 125.3)", "Semestralmente.", "Financiación"),
  ("MEI (art. 127 bis)", "Cotización finalista de 1,2 puntos (1 empresa, 0,2 trabajador) que no computa para prestaciones y nutre el Fondo de Reserva.", "Financiación"),
  ("Revalorización de las pensiones contributivas (art. 58)", "Al comienzo de cada año, con el valor medio del IPC interanual de los doce meses previos a diciembre; si es negativo, no varían.", "Problemas y líneas de actuación"),
  ("Tres actuaciones de sostenibilidad del RDL 2/2023 (preámbulo)", "Subida gradual de la base máxima, cotización de solidaridad y MEI (que sustituye al factor de sostenibilidad).", "Problemas y líneas de actuación"),
  ("Regímenes especiales (LGSS, art. 10.2)", "Autónomos, trabajadores del mar, funcionarios públicos civiles y militares, estudiantes y los que determine el Ministerio.", "Regímenes"),
  ("Sistemas especiales (LGSS, art. 11)", "Solo en encuadramiento, afiliación, forma de cotización o recaudación (p. ej., empleados de hogar y agrarios en el RG).", "Regímenes"),
  ("Acción protectora del RG y del RETA (arts. 155 y 314)", "RG: la del art. 42 salvo cese de actividad y no contributivas. RETA: salvo desempleo y no contributivas.", "Acción protectora"),
  ("¿Qué no es accidente de trabajo? (art. 156.4)", "El debido a fuerza mayor extraña al trabajo y el debido a dolo o imprudencia temeraria del trabajador.", "Acción protectora"),
  ("Excepciones a la intangibilidad de las prestaciones (art. 44.1)", "Obligaciones alimenticias a favor del cónyuge e hijos y obligaciones contraídas dentro de la Seguridad Social.", "Prestaciones"),
  ("Prescripción del derecho a las prestaciones (art. 53.1)", "Cinco años desde el día siguiente al hecho causante; efectos desde tres meses antes de la solicitud.", "Prestaciones"),
  ("Edad y carencia de la jubilación contributiva (art. 205.1)", "67 años (65 con 38 años y 6 meses cotizados); 15 años cotizados, 2 en los últimos 15.", "Prestaciones"),
  ("Pensiones no contributivas (arts. 363 y 369)", "Invalidez: 18 a 64 años, ≥ 65 %, 5 años de residencia. Jubilación: 65 años, 10 años de residencia entre los 16 y el devengo.", "Prestaciones"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Entidad gestora", "Entidad de derecho público que gestiona y administra la Seguridad Social: INSS, INGESA e IMSERSO (LGSS, arts. 66 y 68).", "s3", "Estructura")
T.glos("Servicio común", "Servicio con personalidad jurídica propia que atiende a todo el sistema: Tesorería General y Gerencia de Informática (LGSS, arts. 73 a 74 bis).", "s4", "Estructura")
T.glos("Mutua colaboradora con la Seguridad Social", "Asociación privada de empresarios, sin ánimo de lucro, que colabora en la gestión bajo la dirección y tutela del Ministerio (LGSS, art. 80).", "s5", "Estructura")
T.glos("Caja única", "Principio por el que la Tesorería General unifica todos los recursos financieros del sistema (LGSS, art. 74).", "s4", "Estructura")
T.glos("Reparto", "Sistema financiero de todos los regímenes de la Seguridad Social (LGSS, art. 110.1).", "s7", "Financiación")
T.glos("Fondo de Reserva de la Seguridad Social", "Fondo constituido en la Tesorería General para las necesidades financieras de las prestaciones contributivas; sus activos se destinan en exclusiva a las pensiones contributivas (LGSS, arts. 117 y 121).", "s8", "Financiación")
T.glos("Mecanismo de Equidad Intergeneracional", "Cotización finalista de 1,2 puntos, no computable para prestaciones, que nutre el Fondo de Reserva (LGSS, art. 127 bis).", "s9", "Financiación")
T.glos("Revalorización", "Actualización anual de las pensiones contributivas con el valor medio del IPC de los doce meses previos a diciembre del año anterior (LGSS, art. 58).", "s11", "Problemas y líneas de actuación")
T.glos("Régimen especial", "Régimen para actividades cuyas peculiaridades lo exigen: autónomos, mar, funcionarios, estudiantes y los que determine el Ministerio (LGSS, art. 10).", "s14", "Regímenes")
T.glos("Sistema especial", "Especialidad dentro de un régimen limitada a encuadramiento, afiliación, forma de cotización o recaudación (LGSS, art. 11).", "s14", "Regímenes")
T.glos("Acción protectora", "Conjunto de prestaciones y servicios que el sistema dispensa; el art. 42 LGSS establece y limita la de cada régimen.", "s17", "Acción protectora")
T.glos("Accidente de trabajo", "Toda lesión corporal que el trabajador sufra con ocasión o por consecuencia del trabajo que ejecute por cuenta ajena (LGSS, art. 156.1).", "s20", "Acción protectora")
T.glos("Enfermedad profesional", "La contraída a consecuencia del trabajo por cuenta ajena en las actividades y por los elementos del cuadro reglamentario (LGSS, art. 157).", "s20", "Acción protectora")
T.glos("Situación asimilada a la de alta", "Situación que, sin alta efectiva, permite cumplir el requisito general de alta para causar prestaciones (LGSS, art. 165.1).", "s22", "Prestaciones")

# Cronología (fechas de los metadatos del BOE)
T.hito("1978", "Constitución Española (27-12-1978; BOE de 29-12-1978)", "Arts. 41, 50, 129.1 y 149.1.17.ª: régimen público de Seguridad Social y competencia del Estado", "normativo", "s1")
T.hito("2015", "Real Decreto Legislativo 8/2015, de 30 de octubre, texto refundido de la Ley General de la Seguridad Social (BOE de 31-10-2015; vigencia desde 2-1-2016)", "Norma básica del tema: estructura, financiación, regímenes y prestaciones", "normativo", "s2")
T.hito("2021", "Ley 21/2021, de 28 de diciembre, de garantía del poder adquisitivo de las pensiones (BOE de 29-12-2021)", "Revalorización con el IPC (art. 58) y derogación del factor de sostenibilidad", "normativo", "s10")
T.hito("2023", "Real Decreto-ley 2/2023, de 16 de marzo, nuevo marco de sostenibilidad del sistema público de pensiones (BOE de 17-3-2023)", "Base máxima, cotización de solidaridad y nuevo MEI (art. 127 bis)", "normativo", "s11")

T.publicar()
