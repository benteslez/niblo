# -*- coding: utf-8 -*-
"""Tema II.6 (B2T06): Políticas de la Unión Europea: mercado interior. Política económica y
monetaria. Política exterior y de seguridad común. El espacio de seguridad, libertad y
justicia. Defensa de la competencia. Política agrícola y pesquera.
Método del I.2. Normas: TFUE y TUE (versiones consolidadas, EUR-Lex); Protocolos n.º 12,
13 y 16 anejos a los Tratados (EUR-Lex); Reglamento (UE) 2021/1139, del FEMPA (EUR-Lex);
Tratado de Estabilidad, Coordinación y Gobernanza (BOE-A-2013-1118).
Fuera de las normas: la lista de países de la zona del euro, citada literal de la página
oficial de la Unión Europea (european-union.europa.eu), marcada como no legal."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO["TFUE"] = "TFUE"
CORTO["TUE"] = "TUE"
CORTO["PROT12"] = "Protocolo n.º 12"
CORTO["PROT13"] = "Protocolo n.º 13"
CORTO["PROT16"] = "Protocolo n.º 16"
CORTO["FEMPA"] = "Reglamento (UE) 2021/1139, FEMPA"
CORTO["TECG"] = "TECG"
EURO_URL = "https://european-union.europa.eu/institutions-law-budget/euro/countries-using-euro_es"
TF = "TFUE"
def tf(n): return f"Artículo {n}"

T = Tema("B2T06",
  "Seis preguntas: I. Qué es el mercado interior y sus cuatro libertades (TFUE, arts. 26 a 66) · II. Cómo se coordina la política económica y quién hace la monetaria (TFUE, arts. 119 a 140; Protocolos n.º 12, 13 y 16; TECG) · III. Cómo funciona la PESC (TUE, arts. 21 a 46) · IV. Qué es el espacio de libertad, seguridad y justicia (TFUE, arts. 67 a 89) · V. Qué prohíben las normas de competencia (TFUE, arts. 101 a 108) · VI. Qué persiguen la política agrícola y la pesquera (TFUE, arts. 38 a 43; FEMPA). Cada artículo: texto literal (EUR-Lex o BOE) y ficha.",
  ["Mercado interior", "Art. 26 TFUE", "Cuatro libertades", "Unión aduanera", "Art. 45.4", "UEM", "Euro", "BCE y SEBC", "Déficit excesivo", "Criterios de convergencia", "TECG", "PESC", "Alto Representante", "Abstención con declaración formal", "Art. 42.7 TUE", "ELSJ", "Reconocimiento mutuo", "Eurojust y Fiscalía Europea", "Arts. 101 y 102", "Ayudas de Estado", "PAC", "Pesca", "FEMPA"])

# =============================================================================
T.ap("s0", "Mapa del tema: seis preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque II, tema 6):
> Políticas de la Unión Europea: mercado interior. Política económica y monetaria. Política exterior y de seguridad común. El espacio de seguridad, libertad y justicia. Defensa de la competencia. Política agrícola y pesquera.

### El hilo conductor

El epígrafe enumera **seis políticas**. Cada una es un bloque de los apuntes, en el orden del epígrafe; dentro de cada bloque, los artículos van en su orden.

| Bloque | Pregunta | Tratados | Otras normas |
|---|---|---|---|
| **I** | ¿Qué es el mercado interior y cómo se garantizan las cuatro libertades? | TFUE, arts. 3.1 a), 4.2 a), 26, 28, 30, 34 a 36, 45, 49, 51, 56, 57, 59, 63, 65 y 66 | — |
| **II** | ¿Cómo se coordina la política económica y quién decide la monetaria? | TFUE, arts. 3.1 c), 119, 121, 123 a 128, 130, 136, 139 y 140 | Protocolos n.º 12, 13 y 16; Tratado de Estabilidad, Coordinación y Gobernanza (BOE) |
| **III** | ¿Cómo funciona la política exterior y de seguridad común? | TUE, arts. 21, 24, 26, 27, 31, 42 y 46 | — |
| **IV** | ¿Qué es el espacio de libertad, seguridad y justicia? | TFUE, arts. 4.2 j), 67, 68, 76 a 79, 81 a 83 y 85 a 88 | — |
| **V** | ¿Qué prohíben las normas de competencia y quién las aplica? | TFUE, arts. 3.1 b), 101, 102 y 105 a 108 | — |
| **VI** | ¿Qué persiguen la política agrícola común y la pesquera? | TFUE, arts. 3.1 d), 4.2 d), 38 a 40, 42 y 43 | Reglamento (UE) 2021/1139 (FEMPA) |

!> **La idea que une los seis bloques:** el **mercado interior** (I) es la base: un espacio sin fronteras interiores con cuatro libertades. Sobre él se construyen la **unión económica y monetaria** (II), las **normas de competencia** (V), que impiden que empresas o Estados lo falseen, y la **política agrícola y pesquera** (VI), porque el mercado interior abarca la agricultura y la pesca. La **PESC** (III) y el **espacio de libertad, seguridad y justicia** (IV) llevan la integración fuera de lo económico, con reglas propias (unanimidad en la PESC; reconocimiento mutuo en la justicia).

### Cómo está escrito

- Cada artículo: primero el **texto literal** (EUR-Lex, con la etiqueta DOUE; el Tratado de Estabilidad, del BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen; en las libertades, Titulares · Contenido · Límites · Protección · ⚠ Ojo).
- Los esquemas **no son texto legal**: resumen los artículos citados. La lista de países del euro sale de la página oficial de la Unión Europea y está marcada como tal.
- No se repite lo de otros temas: instituciones (temas II.2 y II.3), fuentes (tema II.4), presupuesto y fondos (tema II.5).
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
# BLOQUE I. MERCADO INTERIOR
T.ap("bI", "I. ¿Qué es el mercado interior y cómo se garantizan las cuatro libertades? (TFUE, arts. 26 a 66)", donde(
  "Primera política del epígrafe y base de las demás. El TFUE define el mercado interior como un **espacio sin fronteras interiores** y lo construye con **cuatro libertades**: mercancías, personas, servicios y capitales.",
  ["1 Competencia y concepto (arts. 3, 4 y 26)", "2 Mercancías: unión aduanera y restricciones cuantitativas (arts. 28 a 36)", "3 Personas: trabajadores y establecimiento (arts. 45, 49 y 51)", "4 Servicios (arts. 56, 57 y 59)", "5 Capitales y pagos (arts. 63, 65 y 66)"]))

T.ap("s1", "I.1 Competencia de la Unión y concepto de mercado interior (TFUE, arts. 3, 4 y 26)", f"""
{unidad("1.1 Unión aduanera, exclusiva; mercado interior, compartida (arts. 3.1 a y 4.2 a)",
  lit(TF, tf(3), ["a) la unión aduanera;"], solo=[1, 2]),
  lit(TF, tf(4), ["a) el mercado interior;"], solo=[2, 3]),
  fichab("Qué tipo de competencia tiene la Unión en este ámbito",
         "La Unión (y, en lo compartido, también los Estados miembros)",
         ["**Unión aduanera**: competencia **exclusiva** (art. 3.1 a)", "**Mercado interior**: competencia **compartida** (art. 4.2 a)"],
         "—",
         "No confundir: la unión aduanera es **exclusiva**; el mercado interior, **compartido**. Las normas de competencia «necesarias para el funcionamiento del mercado interior» son exclusivas (art. 3.1 b → V.1.1)."))}

{unidad("1.2 Qué implica el mercado interior (art. 26)",
  lit(TF, tf(26), ["un espacio sin fronteras interiores", "la libre circulación de mercancías, personas, servicios y capitales"]),
  fichab("El mercado interior: espacio sin fronteras interiores con cuatro libertades",
         f"{c(TF, tf(26), 'La Unión')} adopta las medidas; {c(TF, tf(26), 'El Consejo, a propuesta de la Comisión')} define las orientaciones y condiciones",
         ["Libre circulación de **mercancías**", "Libre circulación de **personas**", "Libre circulación de **servicios**", "Libre circulación de **capitales**"],
         "—",
         "Cayó en 2025 (→ Cierre 1): el mercado interior implica **un espacio sin fronteras interiores**; no armonización fiscal plena ni unificación presupuestaria."))}
""", 2)

T.ap("s2", "I.2 Libre circulación de mercancías (TFUE, arts. 28 a 36)", f"""
{unidad("2.1 La unión aduanera (art. 28)",
  lit(TF, tf(28), ["la totalidad de los intercambios de mercancías", "la prohibición, entre los Estados miembros, de los derechos de aduana de importación y exportación y de cualesquiera exacciones de efecto equivalente", "un arancel aduanero común"]),
  fichab("Unión aduanera: libre comercio interior + arancel común frente a terceros",
         "La Unión (competencia exclusiva, → I.1.1)",
         ["Hacia dentro: prohibición de derechos de aduana y **exacciones de efecto equivalente**", "Hacia fuera: **arancel aduanero común**", "Se aplica a productos originarios de los Estados miembros y a los de terceros países **en libre práctica** (28.2 y 29)"],
         "—",
         "Abarca **la totalidad** de los intercambios de mercancías. Arancel común solo **con terceros países**."))}

{unidad("2.2 Prohibición de derechos de aduana (art. 30)",
  lit(TF, tf(30), ["derechos de aduana de carácter fiscal"]),
  fichab("Prohibición de derechos de aduana entre Estados miembros", "Los Estados miembros (destinatarios de la prohibición)",
         "Prohibidos los de **importación y exportación** y las **exacciones de efecto equivalente**", "—",
         "La prohibición alcanza también a los derechos de aduana **de carácter fiscal**."))}

{unidad("2.3 Prohibición de restricciones cuantitativas (arts. 34 y 35)",
  lit(TF, tf(34), ["restricciones cuantitativas a la importación"]),
  lit(TF, tf(35), ["restricciones cuantitativas a la exportación"]),
  fichab("Prohibición de cupos y de medidas de efecto equivalente", "Los Estados miembros",
         ["Art. 34: a la **importación**", "Art. 35: a la **exportación**", "En los dos, también **todas las medidas de efecto equivalente**"], "—",
         "Distinguir: arts. 28 y 30 = **derechos de aduana** (cargas pecuniarias); arts. 34 y 35 = **restricciones cuantitativas** y medidas de efecto equivalente."))}

{unidad("2.4 Excepciones justificadas (art. 36)",
  lit(TF, tf(36), ["orden público, moralidad y seguridad públicas", "protección del patrimonio artístico, histórico o arqueológico nacional", "un medio de discriminación arbitraria ni una restricción encubierta del comercio entre los Estados miembros"]),
  fichab("Cuándo un Estado puede restringir la circulación de mercancías", "Los Estados miembros",
         ["::Razones tasadas:", "Orden público, moralidad y seguridad públicas", "Protección de la salud y vida de las personas y animales; preservación de los vegetales", "Protección del patrimonio artístico, histórico o arqueológico nacional", "Protección de la propiedad industrial y comercial"],
         "—",
         "Límite: nunca **discriminación arbitraria** ni **restricción encubierta** del comercio. Las excepciones se refieren a **importación, exportación o tránsito**."))}
""", 2)

T.ap("s3", "I.3 Libre circulación de personas: trabajadores y establecimiento (TFUE, arts. 45, 49 y 51)", f"""
{unidad("3.1 Libre circulación de trabajadores (art. 45)",
  lit(TF, tf(45), ["la abolición de toda discriminación por razón de la nacionalidad", "Sin perjuicio de las limitaciones justificadas por razones de orden público, seguridad y salud públicas", "no serán aplicables a los empleos en la administración pública"]),
  ficha("Los **trabajadores** de los Estados miembros",
        ["Igualdad de trato: sin discriminación por **nacionalidad** en empleo, retribución y condiciones de trabajo (45.2)", "::Derechos (45.3):", "Responder a ofertas efectivas de trabajo", "Desplazarse libremente para ello", "Residir para ejercer un empleo", "Permanecer tras haber ejercido un empleo"],
        ["Razones de **orden público, seguridad y salud públicas** (45.3)", "No se aplica a los **empleos en la administración pública** (45.4)"],
        f"El Parlamento Europeo y el Consejo adoptan las medidas {c(TF, tf(46), 'mediante directivas o reglamentos')} (art. 46)",
        "Para una oposición, el dato clave es el **45.4**: el artículo **no se aplica** a los empleos en la administración pública."))}

{unidad("3.2 Libertad de establecimiento (art. 49)",
  lit(TF, tf(49), ["la apertura de agencias, sucursales o filiales", "el acceso a las actividades no asalariadas y su ejercicio"]),
  ficha("Los **nacionales** de un Estado miembro (y las sociedades del art. 54)",
        ["Acceso a las actividades **no asalariadas** y su ejercicio", "Constitución y gestión de empresas y sociedades", "Apertura de agencias, sucursales o filiales"],
        f"{c(TF, tf(49), 'en las condiciones fijadas por la legislación del país de establecimiento para sus propios nacionales')}",
        "Prohibición de restricciones (49, párrafo primero)",
        "Trabajadores = actividad **asalariada** (45); establecimiento = actividad **no asalariada** (49)."))}

{unidad("3.3 Excepción del poder público (art. 51)",
  lit(TF, tf(51), ["aunque sólo sea de manera ocasional, con el ejercicio del poder público"]),
  fichab("Actividades excluidas de la libertad de establecimiento", "El Estado miembro interesado; el Parlamento Europeo y el Consejo pueden excluir otras",
         "Quedan fuera las actividades relacionadas con el **ejercicio del poder público**", "Exclusión de otras actividades: procedimiento legislativo **ordinario**",
         "Basta que la relación con el poder público sea **ocasional**. Es el equivalente, en el establecimiento, del art. 45.4 para los trabajadores."))}
""", 2)

T.ap("s4", "I.4 Libre prestación de servicios (TFUE, arts. 56, 57 y 59)", f"""
{unidad("4.1 Prohibición de restricciones (art. 56)",
  lit(TF, tf(56), ["establecidos en un Estado miembro que no sea el del destinatario de la prestación", "nacionales de un tercer Estado y se hallen establecidos dentro de la Unión"]),
  ficha("Nacionales de los Estados miembros **establecidos** en un Estado distinto del del destinatario",
        "Prestar servicios sin restricciones dentro de la Unión",
        "—",
        "Prohibición de restricciones; extensión posible a nacionales de terceros Estados establecidos en la Unión (procedimiento legislativo ordinario)",
        "El elemento transfronterizo: el prestador está establecido en un Estado **que no sea el del destinatario**."))}

{unidad("4.2 Qué es un servicio (art. 57)",
  lit(TF, tf(57), ["normalmente a cambio de una remuneración", "en la medida en que no se rijan por las disposiciones relativas a la libre circulación de mercancías, capitales y personas", "ejercer temporalmente su actividad"]),
  fichab("Concepto de servicio a efectos de los Tratados", "—",
         ["Prestación **normalmente remunerada**", "Carácter **residual**: si no la rigen las normas de mercancías, capitales y personas", "Incluye actividades industriales, mercantiles, artesanales y de profesiones liberales", "El prestador ejerce **temporalmente** en el Estado de la prestación, en las mismas condiciones que sus nacionales"],
         "—",
         "La nota de **temporalidad** distingue el servicio del **establecimiento** (que es estable)."))}

{unidad("4.3 Liberalización mediante directivas (art. 59)",
  lit(TF, tf(59), ["con arreglo al procedimiento legislativo ordinario y previa consulta al Comité Económico y Social, decidirán mediante directivas"], solo=[1]),
  fichab("Liberalización de un servicio determinado", f"{c(TF, tf(59), 'el Parlamento Europeo y el Consejo')}",
         "Mediante **directivas**", "Procedimiento legislativo **ordinario** y previa consulta al **Comité Económico y Social**",
         "Cayó en 2025 (→ Cierre 1): **directivas** (no reglamentos, recomendaciones ni decisiones), **ordinario** (no especial)."))}
""", 2)

T.ap("s5", "I.5 Libre circulación de capitales y pagos (TFUE, arts. 63, 65 y 66)", f"""
{unidad("5.1 Prohibición de restricciones (art. 63)",
  lit(TF, tf(63), ["entre Estados miembros y entre Estados miembros y terceros países"]),
  fichab("Libertad de movimientos de capitales y de pagos", "Estados miembros (destinatarios de la prohibición)",
         ["Prohibidas las restricciones a los **movimientos de capitales** (63.1)", "Prohibidas las restricciones a los **pagos** (63.2)"], "—",
         "Alcanza también a **terceros países**: entre Estados miembros **y** entre estos y terceros países."))}

{unidad("5.2 Lo que pueden seguir haciendo los Estados (art. 65)",
  lit(TF, tf(65), ["Derecho fiscal", "supervisión prudencial de entidades financieras", "razones de orden público o de seguridad pública", "ni un medio de discriminación arbitraria ni una restricción encubierta"], solo=[1, 2, 3, 5]),
  fichab("Excepciones a la libertad de capitales", "Los Estados miembros",
         ["Distinguir fiscalmente por residencia o lugar de inversión", "Impedir infracciones, en particular fiscales y de supervisión prudencial", "Declaraciones administrativas o estadísticas", "Medidas por **orden público** o **seguridad pública**"], "—",
         "Como en el art. 36: nunca **discriminación arbitraria** ni **restricción encubierta**."))}

{unidad("5.3 Medidas de salvaguardia frente a terceros países (art. 66)",
  lit(TF, tf(66), ["por un plazo que no sea superior a seis meses"]),
  fichab("Salvaguardia por dificultades graves para la unión económica y monetaria",
         f"{c(TF, tf(66), 'el Consejo, a propuesta de la Comisión y previa consulta al Banco Central Europeo')}",
         "Medidas estrictamente necesarias, solo **respecto a terceros países** y en **circunstancias excepcionales**",
         "Máximo **seis meses**",
         "Seis meses; consulta al **BCE**; solo frente a **terceros países**."))}

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Libertad | Regla | Excepciones | Dato que se pregunta |
|---|---|---|---|
| Mercancías | Unión aduanera (28 y 30) y prohibición de restricciones cuantitativas (34 y 35) | Art. 36 | Arancel común **solo frente a terceros** |
| Trabajadores | Sin discriminación por nacionalidad (45) | Orden público, seguridad y salud públicas; **administración pública** (45.4) | 45.4 |
| Establecimiento | Actividades **no asalariadas** (49) | **Poder público** (51) | Agencias, sucursales o filiales |
| Servicios | Prestador establecido en otro Estado (56); remunerado y **temporal** (57) | — | Liberalización por **directivas** (59) |
| Capitales y pagos | Sin restricciones, también con **terceros países** (63) | Art. 65; salvaguardia de **6 meses** (66) | Terceros países |

{resumen([
  "Mercado interior: **espacio sin fronteras interiores** con libre circulación de **mercancías, personas, servicios y capitales** (26.2); competencia **compartida** (4.2 a); unión aduanera, **exclusiva** (3.1 a).",
  "Mercancías: sin derechos de aduana ni exacciones de efecto equivalente (28 y 30), sin restricciones cuantitativas (34 y 35), salvo el art. 36.",
  "Trabajadores: no se aplica a los **empleos en la administración pública** (45.4); establecimiento: excepción del **poder público** (51).",
  "Servicios: remunerados y temporales (57); liberalización por **directivas**, procedimiento **ordinario** y consulta al **CES** (59). Capitales: también con **terceros países** (63)."],
  "Siguiente: II. ¿Cómo se coordina la política económica y quién decide la monetaria?")}
""", 2)

# =============================================================================
# BLOQUE II. POLÍTICA ECONÓMICA Y MONETARIA
T.ap("bII", "II. ¿Cómo se coordina la política económica y quién decide la monetaria? (TFUE, arts. 119 a 140; Protocolos n.º 12, 13 y 16; TECG)", donde(
  "Segunda política del epígrafe. La unión económica y monetaria tiene dos piezas **asimétricas**: la política **económica** sigue en manos de los Estados, que la **coordinan** en el Consejo; la política **monetaria** de los Estados del euro es **exclusiva** de la Unión y la conduce el **SEBC**.",
  ["1 Principios (arts. 3.1 c y 119)", "2 Coordinación de las políticas económicas (art. 121)", "3 Prohibiciones de financiación y de rescate (arts. 123 a 125)", "4 Déficit excesivo (art. 126 y Protocolo n.º 12)", "5 La política monetaria: SEBC, BCE y euro (arts. 127, 128 y 130)", "6 Estados del euro y Estados acogidos a una excepción (arts. 136, 139 y 140; Protocolos n.º 13 y 16)", "7 El Tratado de Estabilidad, Coordinación y Gobernanza"]))

T.ap("s6", "II.1 Principios de la unión económica y monetaria (TFUE, arts. 3.1 c y 119)", f"""
{unidad("1.1 La política monetaria del euro, competencia exclusiva (art. 3.1 c)",
  lit(TF, tf(3), ["c) la política monetaria de los Estados miembros cuya moneda es el euro;"], solo=[1, 4]),
  fichab("Reparto de la competencia en la UEM", "La **Unión**, en exclusiva, para los Estados cuya moneda es el euro",
         ["Política **monetaria** del euro: exclusiva (3.1 c)", f"Política **económica**: los Estados la coordinan en la Unión ({c(TF, tf(121), 'Los Estados miembros considerarán sus políticas económicas como una cuestión de interés común')}, art. 121.1 → II.2.1)"],
         "—",
         "La política monetaria es exclusiva **solo** para los Estados **cuya moneda es el euro**. Cayó en 2025 como pregunta relacionada (→ Cierre 1)."))}

{unidad("1.2 Política económica, moneda única y principios rectores (art. 119)",
  lit(TF, tf(119), ["la estrecha coordinación de las políticas económicas de los Estados miembros", "una moneda única, el euro", "mantener la estabilidad de precios", "precios estables, finanzas públicas y condiciones monetarias sólidas y balanza de pagos estable"]),
  fichab("Las dos piezas de la UEM y sus principios", "Los Estados miembros y la Unión",
         ["Política **económica**: estrecha coordinación, mercado interior y objetivos comunes (119.1)", "Política **monetaria y de tipos de cambio única**, con el euro; objetivo **primordial**: la **estabilidad de precios** (119.2)", "Siempre con una **economía de mercado abierta y de libre competencia**"],
         "—",
         "Cuatro principios rectores (119.3): **precios estables**, **finanzas públicas y condiciones monetarias sólidas** y **balanza de pagos estable**."))}
""", 2)

T.ap("s7", "II.2 La coordinación de las políticas económicas (TFUE, art. 121)", f"""
{unidad("2.1 Las orientaciones generales de política económica (art. 121.1 y 2)",
  lit(TF, tf(121), ["una cuestión de interés común", "sobre la base de una recomendación de la Comisión", "el Consejo Europeo debatirá unas conclusiones", "adoptará una recomendación"], solo=[1, 2, 3, 4]),
  fichab("Orientaciones generales para las políticas económicas de los Estados y de la Unión",
         "Comisión (recomendación) → Consejo (proyecto) → Consejo Europeo (conclusiones) → Consejo (recomendación); se informa al Parlamento Europeo",
         "Coordinación en el seno del **Consejo**",
         "—",
         "Las orientaciones generales se adoptan por **recomendación** del Consejo (no por reglamento ni decisión). El Consejo Europeo solo **debate conclusiones**."))}

{unidad("2.2 Supervisión multilateral y advertencias (art. 121.3 y 4)",
  lit(TF, tf(121), ["supervisará la evolución económica de cada uno de los Estados miembros", "la Comisión podrá dirigir una advertencia", "sin tomar en consideración el voto del miembro del Consejo que represente al Estado miembro de que se trate"], solo=[5, 6, 7, 8]),
  fichab("Vigilancia de la coherencia de las políticas nacionales con las orientaciones", "**Consejo** (supervisa, recomienda) y **Comisión** (informes, advertencia)",
         ["Los Estados informan a la Comisión de sus medidas importantes", "Si un Estado se aparta: **advertencia** de la Comisión y **recomendaciones** del Consejo, que pueden hacerse públicas"],
         "El Consejo decide **sin el voto** del Estado afectado (mayoría cualificada de los demás)",
         "La **advertencia** la dirige la **Comisión**; las **recomendaciones**, el **Consejo**."))}
""", 2)

T.ap("s8", "II.3 Prohibiciones de financiación privilegiada y de rescate (TFUE, arts. 123 a 125)", f"""
{unidad("3.1 Prohibición de financiación monetaria (art. 123)",
  lit(TF, tf(123), ["Queda prohibida la autorización de descubiertos o la concesión de cualquier otro tipo de créditos", "la adquisición directa a los mismos de instrumentos de deuda"], solo=[1]),
  fichab("El BCE y los bancos centrales no pueden financiar a los poderes públicos", "Destinatarios: **BCE** y **bancos centrales nacionales**",
         ["Prohibidos descubiertos y créditos a instituciones de la Unión, Gobiernos, autoridades regionales o locales, organismos de Derecho público o empresas públicas", "Prohibida la **adquisición directa** de sus instrumentos de deuda"], "—",
         "Lo prohibido es la adquisición **directa** de deuda. Las entidades de crédito públicas reciben el mismo trato que las privadas (123.2)."))}

{unidad("3.2 Prohibición de acceso privilegiado (art. 124)",
  lit(TF, tf(124), ["que no se base en consideraciones prudenciales"]),
  fichab("Sin acceso privilegiado de los poderes públicos a las entidades financieras", "Todos los poderes públicos de la Unión y de los Estados",
         "Prohibida cualquier medida que establezca un acceso privilegiado", "—",
         "Salvedad: medidas basadas en **consideraciones prudenciales**."))}

{unidad("3.3 Ni la Unión ni los Estados asumen los compromisos de otro (art. 125)",
  lit(TF, tf(125), ["no asumirá ni responderá de los compromisos", "sin perjuicio de las garantías financieras mutuas para la realización conjunta de proyectos específicos"], solo=[1]),
  fichab("Ni la Unión ni los Estados responden de las deudas de otro Estado", "La Unión y los Estados miembros",
         "No asumen ni responden de los compromisos de los poderes públicos de los Estados (la Unión) o de otro Estado (los Estados)", "—",
         "Única salvedad: las **garantías financieras mutuas** para proyectos específicos conjuntos."))}
""", 2)

T.ap("s9", "II.4 El procedimiento de déficit excesivo (TFUE, art. 126 y Protocolo n.º 12)", f"""
{unidad("4.1 Obligación y criterios (art. 126.1 y 2)",
  lit(TF, tf(126), ["Los Estados miembros evitarán déficits públicos excesivos", "La Comisión supervisará", "la proporción entre la deuda pública y el producto interior bruto"], solo=[1, 2, 3, 6, 7]),
  fichab("Disciplina presupuestaria: déficit y deuda", "Los **Estados** evitan déficits excesivos; la **Comisión** supervisa",
         ["Criterio del **déficit** público en relación con el PIB (126.2 a)", "Criterio de la **deuda** pública en relación con el PIB (126.2 b)"],
         "Los valores de referencia, en el Protocolo sobre déficit excesivo (→ II.4.2)",
         "Cada criterio tiene sus matices: se tolera si la proporción **desciende** y se **aproxima** al valor de referencia."))}

{unidad("4.2 Los valores de referencia: 3 % y 60 % (Protocolo n.º 12, art. 1)",
  lit("PROT12", "Artículo 1", ["3 %", "60 %"], titulo="Artículo 1 (Protocolo n.º 12 sobre el procedimiento aplicable en caso de déficit excesivo)"),
  fichab("Cifras del procedimiento de déficit excesivo", "—",
         ["Déficit público: **3 %** del PIB a precios de mercado", "Deuda pública: **60 %** del PIB a precios de mercado"], "—",
         "Son valores del **Protocolo n.º 12**, no del art. 126. **3 %** = déficit; **60 %** = deuda."))}

{unidad("4.3 Del dictamen a las multas (art. 126.3 a 11)",
  lit(TF, tf(126), ["El Comité Económico y Financiero emitirá un dictamen", "decidirá si existe un déficit excesivo", "no se harán públicas", "no podrá ejercerse el derecho de recurso previsto en los artículos 258 y 259", "imponer multas de una magnitud apropiada"], solo=[8, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22]),
  fichab("Procedimiento de déficit excesivo",
         "**Comisión** (informe y dictamen) · **Comité Económico y Financiero** (dictamen sobre el informe) · **Consejo** (decide y sanciona)",
         ["Informe de la Comisión → dictamen del CEF → dictamen de la Comisión al Estado", "El Consejo decide si **existe** déficit excesivo y dirige **recomendaciones** (no públicas salvo incumplimiento)", "Si persiste: **advertencia**; si incumple: información adicional, revisión de préstamos del BEI, **depósito sin intereses**, **multas**"],
         "El Consejo decide **sin el voto** del Estado afectado (126.13)",
         "En los apartados 1 a 9 **no cabe** el recurso por incumplimiento de los arts. **258 y 259** (126.10)."))}
""", 2)

T.ap("s10", "II.5 La política monetaria: SEBC, BCE y euro (TFUE, arts. 127, 128 y 130)", f"""
{unidad("5.1 Objetivo y funciones del SEBC (art. 127.1 y 2)",
  lit(TF, tf(127), ["será mantener la estabilidad de precios", "definir y ejecutar la política monetaria de la Unión"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Qué hace el Sistema Europeo de Bancos Centrales", f"El **SEBC**; lo dirigen {c(TF, tf(129), 'los órganos rectores del Banco Central Europeo, que serán el Consejo de Gobierno y el Comité Ejecutivo')} (art. 129.1)",
         ["Definir y ejecutar la **política monetaria**", "Operaciones de **divisas**", "Poseer y gestionar las **reservas oficiales de divisas**", "Promover el buen funcionamiento de los **sistemas de pago**"],
         "—",
         "Objetivo **principal**: la **estabilidad de precios**; el apoyo a las políticas económicas generales va **sin perjuicio** de ese objetivo. Instituciones del BCE: tema II.3."))}

{unidad("5.2 Billetes y monedas en euros (art. 128)",
  lit(TF, tf(128), ["el derecho exclusivo de autorizar la emisión de billetes de banco en euros", "la aprobación del Banco Central Europeo en cuanto al volumen de emisión"]),
  fichab("Quién emite el euro", "**BCE** (autoriza los billetes); BCE y bancos centrales nacionales (emiten billetes); **Estados** (emiten monedas)",
         ["Billetes: autorización **exclusiva** del BCE; son los únicos de **curso legal**", "Monedas metálicas: las emiten los **Estados**, con aprobación del BCE del **volumen**"], "—",
         "Billetes → **BCE** autoriza; monedas → **Estados** emiten, el BCE aprueba solo el **volumen**."))}

{unidad("5.3 Independencia (art. 130)",
  lit(TF, tf(130), ["podrán solicitar o aceptar instrucciones", "a no tratar de influir"]),
  fichab("Independencia del BCE y de los bancos centrales nacionales", "BCE, bancos centrales nacionales y miembros de sus órganos rectores",
         "No piden ni aceptan instrucciones de instituciones de la Unión, Gobiernos ni ningún otro órgano; estos se comprometen a no influir", "—",
         "La independencia alcanza también a los **bancos centrales nacionales**. Los Estados adaptan su legislación (art. 131)."))}
""", 2)

EURO_BLK = f"""> [[COMISION|{EURO_URL}]]
> **Países que utilizan el euro · página oficial de la Unión Europea (european-union.europa.eu, actualizada el 12 de enero de 2026) · fuente oficial, no es texto legal**
> Hoy en día, el euro (€) es la moneda oficial de 21 de los 27 países de la UE, que juntos constituyen la eurozona, denominada oficialmente zona del euro.
> **Países de la zona del euro:** Austria · Bélgica · Bulgaria · Croacia · Chipre · Estonia · Finlandia · Francia · Alemania · Grecia · Irlanda · Italia · Letonia · Lituania · Luxemburgo · Malta · Países Bajos · Portugal · Eslovaquia · Eslovenia · España
> **Países no pertenecientes a la zona del euro:** Los siguientes países aún no han adoptado el euro, pero se espera que lo hagan una vez que cumplan las condiciones necesarias. Chequia · Hungría · Polonia · Rumanía · Suecia
> En algunos casos, los países de la UE pueden negociar una cláusula de exclusión voluntaria de la legislación o los tratados de la Unión Europea y decidir no participar en determinados ámbitos políticos. Dinamarca se ha acogido a esta cláusula para la moneda única y ha mantenido su propia moneda tras su adhesión a la UE.
> Estas condiciones económicas y jurídicas de obligado cumplimiento se acordaron en 1992 a través del Tratado de Maastricht."""

T.ap("s11", "II.6 Estados del euro y Estados acogidos a una excepción (TFUE, arts. 136, 139 y 140; Protocolos n.º 13 y 16)", f"""
{unidad("6.1 Medidas propias de la zona del euro y mecanismo de estabilidad (art. 136)",
  lit(TF, tf(136), ["Únicamente participarán en las votaciones", "podrán establecer un mecanismo de estabilidad", "se supeditará a condiciones estrictas"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Gobernanza específica de los Estados cuya moneda es el euro", "El **Consejo**, votando solo los miembros de los Estados del euro; los Estados del euro (mecanismo de estabilidad)",
         ["Reforzar la coordinación y supervisión de su disciplina presupuestaria", "Orientaciones de política económica propias", "**Mecanismo de estabilidad** si es **indispensable** para la zona del euro"],
         "Mayoría cualificada de los miembros del euro (art. 238.3 a)",
         f"La ayuda del mecanismo, a **condiciones estrictas**. Las reuniones de ministros del euro, en el {c(TF, tf(137), 'Protocolo sobre el Eurogrupo')} (art. 137)."))}

{unidad("6.2 Qué es un Estado acogido a una excepción (art. 139.1)",
  lit(TF, tf(139), ["Estados miembros acogidos a una excepción"], solo=[1]),
  EURO_BLK,
  fichab("Estados de la UE que aún no han adoptado el euro", "Lo determina el **Consejo** (si no ha decidido que cumplen las condiciones)",
         "No se les aplican, entre otras, las normas sobre objetivos del SEBC, emisión del euro y actos del BCE (139.2); sus votos se suspenden en esas materias (139.4)", "—",
         "Definición **negativa**: los Estados sobre los que el Consejo **no** ha decidido que cumplen las condiciones."))}

{unidad("6.3 Los cuatro criterios de convergencia y la decisión (art. 140.1 y 2)",
  lit(TF, tf(140), ["Una vez cada dos años como mínimo", "como máximo, los tres Estados miembros más eficaces", "sin un déficit público excesivo", "durante dos años como mínimo, sin que se haya producido devaluación frente al euro", "tipos de interés a largo plazo", "suprimirá las excepciones"], solo=[1, 2, 3, 4, 5, 7]),
  fichab("Examen de la convergencia y paso al euro",
         "**Comisión y BCE** (informes) · Parlamento Europeo (consulta) · Consejo Europeo (debate) · **Consejo** (decide, a propuesta de la Comisión)",
         ["::Cuatro criterios:", "**Estabilidad de precios** (inflación)", "**Finanzas públicas** sin déficit excesivo", "**Tipo de cambio**: dos años en el mecanismo de cambios sin devaluar", "**Tipos de interés** a largo plazo"],
         "Informes **cada dos años como mínimo** o a petición del Estado; recomendación previa de la mayoría cualificada de los miembros del euro, en **seis meses** (140.2)",
         "Los criterios se **explicitan** en un Protocolo anejo (→ II.6.4)."))}

{unidad("6.4 Cómo se miden los criterios (Protocolo n.º 13, arts. 1 a 4)",
  lit("PROT13", "Artículo 1", ["1½ punto porcentual"], titulo="Artículo 1 (Protocolo n.º 13 sobre los criterios de convergencia): estabilidad de precios"),
  lit("PROT13", "Artículo 2", ["no sea objeto de una decisión del Consejo con arreglo al apartado 6 del artículo 126"], titulo="Artículo 2 (Protocolo n.º 13): situación del presupuesto público"),
  lit("PROT13", "Artículo 3", ["durante por lo menos los dos años anteriores al examen"], titulo="Artículo 3 (Protocolo n.º 13): tipo de cambio"),
  lit("PROT13", "Artículo 4", ["2 puntos porcentuales"], titulo="Artículo 4 (Protocolo n.º 13): tipos de interés"),
  fichab("Las cifras de los criterios de convergencia", "La Comisión suministra los datos estadísticos (art. 5)",
         ["Inflación: no más de **1½ punto** sobre los tres Estados con mejor comportamiento", "Presupuesto: no tener una **decisión de déficit excesivo** (126.6)", "Tipo de cambio: **dos años** sin tensiones graves y sin devaluar", "Interés a largo plazo: no más de **2 puntos** sobre los tres mejores en estabilidad de precios"],
         "Observación de **un año** antes del examen (inflación e interés)",
         "Cayó en 2025 (→ Cierre 1): el interés es **2 puntos**, no 3; la inflación, **1½**."))}

{unidad("6.5 Dinamarca: la excepción por protocolo (Protocolo n.º 16)",
  lit("PROT16", "Disposiciones", ["Dinamarca disfrutará de una excepción", "sólo se iniciará a petición de Dinamarca"], solo=[1, 2], titulo="Protocolo (n.º 16) sobre determinadas disposiciones relativas a Dinamarca, puntos 1 y 2"),
  fichab("Situación de Dinamarca respecto del euro", "**Dinamarca** (notificación al Consejo de 3 de noviembre de 1993)",
         "Se le aplican las normas de los Tratados y de los Estatutos del SEBC referentes a una **excepción**", "—",
         f"El procedimiento del art. 140 para derogar su excepción **solo** se inicia **a petición de Dinamarca**. Su preámbulo recuerda que notificó {c('PROT16', 'Preámbulo', 'su intención de no participar en la tercera fase de la unión económica y monetaria')}. Cayó en 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s12", "II.7 El Tratado de Estabilidad, Coordinación y Gobernanza (BOE-A-2013-1118)", f"""
Tratado internacional entre Estados miembros, **fuera** de los Tratados de la Unión, publicado en el BOE con el instrumento de ratificación de España.

{unidad("7.1 Quién lo firmó (acta de la firma)",
  lit("TECG", "preambulo", ["han firmado hoy"], solo=[111, 113], titulo="Acta de la firma del Tratado de Estabilidad, Coordinación y Gobernanza en la Unión Económica y Monetaria (BOE-A-2013-1118)"),
  fichab("Los firmantes", "**25** Estados miembros (los que enumera el acta)",
         f"Firma en Bruselas; España lo ratificó tras la autorización de la {c('TECG', 'preambulo', 'Ley Orgánica 3/2012, de 25 de julio')} (art. 93 CE)", "—",
         f"No figuran en la lista de firmantes la **República Checa** ni el **Reino Unido**. El Tratado {c('TECG', 'preambulo', 'estará abierto a la adhesión de los Estados Miembros de la Unión Europea que no sean Partes Contratantes')} (art. 15). Cayó en 2025 (→ Cierre 1)."))}

{unidad("7.2 Objeto y regla de equilibrio presupuestario (arts. 1 y 3.1 a y b)",
  lit("TECG", "preambulo", ["reforzar el pilar económico de la unión económica y monetaria", "será de equilibrio o de superávit", "0,5 % del producto interior bruto"], solo=[42, 43, 52, 53, 54], titulo="Artículos 1 y 3.1 a) y b) (Tratado de Estabilidad, Coordinación y Gobernanza)"),
  fichab("El «pacto presupuestario»", "Las Partes Contratantes; se aplica **íntegramente** a las del euro",
         ["Situación presupuestaria de **equilibrio o superávit**", "Límite inferior de déficit estructural del **0,5 %** del PIB"], "—",
         "Se aplica **íntegramente** a los Estados **cuya moneda es el euro**; a los demás, en la medida del art. 14."))}

{unidad("7.3 La Cumbre del Euro (art. 12.1 y 2)",
  lit("TECG", "preambulo", ["celebrarán de manera informal reuniones de la Cumbre del Euro", "por mayoría simple", "como mínimo dos veces al año"], solo=[87, 88, 89], titulo="Artículo 12.1 y 2 (Tratado de Estabilidad, Coordinación y Gobernanza)"),
  fichab("Reuniones de los Jefes de Estado o de Gobierno del euro", "Jefes de Estado o de Gobierno de las Partes del euro y el Presidente de la Comisión; se invita al Presidente del BCE",
         "Reuniones **informales**; el Eurogrupo las prepara (12.4)",
         "Presidente designado por **mayoría simple**, a la vez que el Consejo Europeo elige al suyo y por un mandato de igual duración; reuniones **como mínimo dos veces al año**",
         "Mayoría **simple** para designar al Presidente; **dos** reuniones al año como mínimo."))}

{resumen([
  "UEM asimétrica: política **monetaria** del euro, **exclusiva** de la Unión (3.1 c); política **económica**, **coordinada** en el Consejo (121).",
  "Objetivo **primordial**: **estabilidad de precios** (119.2 y 127.1); el BCE autoriza los billetes y aprueba el volumen de monedas (128); independencia (130).",
  "Prohibidas la financiación monetaria (123), el acceso privilegiado (124) y el rescate (125). Déficit excesivo: **3 %** y **60 %** (Protocolo n.º 12).",
  "Criterios de convergencia (140 y Protocolo n.º 13): inflación **1½**, sin déficit excesivo, **dos años** en el mecanismo de cambios, interés **2 puntos**. **Dinamarca**: excepción por protocolo.",
  "TECG: firmado por **25** Estados (sin la República Checa ni el Reino Unido); equilibrio o superávit y Cumbre del Euro."],
  "Siguiente: III. ¿Cómo funciona la política exterior y de seguridad común?")}
""", 2)

# =============================================================================
# BLOQUE III. PESC
T.ap("bIII", "III. ¿Cómo funciona la política exterior y de seguridad común? (TUE, arts. 21 a 46)", donde(
  "Tercera política del epígrafe. La PESC está en el **TUE**, no en el TFUE, y se rige por **reglas propias**: unanimidad como regla, sin actos legislativos y con un control muy limitado del Tribunal de Justicia.",
  ["1 Principios y objetivos de la acción exterior (art. 21)", "2 Competencia y reglas específicas (arts. 24 y 26)", "3 El Alto Representante y el Servicio Europeo de Acción Exterior (art. 27)", "4 Cómo se decide (art. 31)", "5 La política común de seguridad y defensa (arts. 42 y 46)"]))

T.ap("s13", "III.1 Principios y objetivos de la acción exterior (TUE, art. 21)", f"""
{unidad("1.1 Principios y objetivos (art. 21.1 y 2)",
  lit("TUE", tf(21), ["la democracia, el Estado de Derecho, la universalidad e indivisibilidad de los derechos humanos", "mantener la paz, prevenir los conflictos y fortalecer la seguridad internacional"], solo=[1, 3, 4, 5, 6, 7, 8, 9, 10, 11]),
  fichab("Lo que inspira toda la acción exterior de la Unión", "La Unión",
         ["::Principios (21.1): los que han inspirado su creación, desarrollo y ampliación:", "Democracia y Estado de Derecho", "Universalidad e indivisibilidad de los derechos humanos", "Dignidad humana, igualdad y solidaridad", "Carta de las Naciones Unidas y Derecho internacional"],
         "—",
         "Preferencia por las **soluciones multilaterales**, en particular en el marco de las **Naciones Unidas** (21.1, párrafo segundo)."))}
""", 2)

T.ap("s14", "III.2 Competencia y reglas específicas de la PESC (TUE, arts. 24 y 26)", f"""
{unidad("2.1 Alcance y reglas propias (art. 24.1)",
  lit("TUE", tf(24), ["todos los ámbitos de la política exterior y todas las cuestiones relativas a la seguridad de la Unión", "por unanimidad salvo cuando los Tratados dispongan otra cosa", "Queda excluida la adopción de actos legislativos", "no tendrá competencia respecto de estas disposiciones"], solo=[1, 2]),
  fichab("La PESC: competencia de la Unión con reglas y procedimientos específicos",
         f"La definen y aplican el **Consejo Europeo** y el **Consejo**; la ejecutan {c('TUE', tf(24), 'el Alto Representante de la Unión para Asuntos Exteriores y Política de Seguridad y por los Estados miembros')}",
         ["Abarca todos los ámbitos de la política exterior y de la seguridad", "Incluye la definición progresiva de una **política común de defensa** que podrá conducir a una **defensa común**"],
         "**Unanimidad**, salvo disposición en contrario; **sin actos legislativos**",
         "El **TJUE no es competente**, salvo para controlar el respeto del **art. 40 TUE** y la legalidad de ciertas decisiones (art. 275 TFUE)."))}

{unidad("2.2 Quién define y quién elabora (art. 26)",
  lit("TUE", tf(26), ["determinará los intereses estratégicos de la Unión", "convocará una reunión extraordinaria del Consejo Europeo", "el Consejo elaborará la política exterior y de seguridad común"]),
  fichab("Reparto de papeles en la PESC",
         ["**Consejo Europeo**: intereses estratégicos, objetivos y orientaciones generales", "**Consejo**: elabora la PESC y adopta las decisiones", "**Alto Representante y Estados**: la ejecutan"],
         "Si un acontecimiento internacional lo exige, el **Presidente del Consejo Europeo** convoca una reunión **extraordinaria**",
         "—",
         "**Consejo Europeo** = orientaciones; **Consejo** = elabora y decide; **Alto Representante** = ejecuta."))}
""", 2)

T.ap("s15", "III.3 El Alto Representante y el Servicio Europeo de Acción Exterior (TUE, art. 27)", f"""
{unidad("3.1 Funciones del Alto Representante y el SEAE (art. 27)",
  lit("TUE", tf(27), ["presidirá el Consejo de Asuntos Exteriores", "representará a la Unión en las materias concernientes a la política exterior y de seguridad común", "servicio europeo de acción exterior", "previa consulta al Parlamento Europeo y previa aprobación de la Comisión"]),
  fichab("El Alto Representante de la Unión para Asuntos Exteriores y Política de Seguridad",
         "El Alto Representante, apoyado por el **Servicio Europeo de Acción Exterior** (SEAE)",
         ["**Preside el Consejo de Asuntos Exteriores**", "Propone y **ejecuta** las decisiones del Consejo Europeo y del Consejo", "**Representa** a la Unión en la PESC y dirige el diálogo político"],
         "Organización del SEAE: **decisión del Consejo**, a propuesta del Alto Representante, previa **consulta** al Parlamento Europeo y previa **aprobación** de la Comisión",
         "SEAE: funcionarios de la Secretaría General del Consejo y de la Comisión y personal de los servicios diplomáticos nacionales. Su nombramiento y su doble función en la Comisión: tema II.2."))}
""", 2)

T.ap("s16", "III.4 Cómo se decide en la PESC (TUE, art. 31)", f"""
{unidad("4.1 Unanimidad y abstención con declaración formal (art. 31.1)",
  lit("TUE", tf(31), ["adoptarán por unanimidad", "no estará obligado a aplicar la decisión, pero admitirá que ésta sea vinculante para la Unión", "al menos un tercio de los Estados miembros que reúnen como mínimo un tercio de la población de la Unión"], solo=[1, 2]),
  fichab("Regla general de decisión y abstención con declaración formal", "Consejo Europeo y Consejo",
         ["Regla: **unanimidad**; sin actos legislativos", "**Abstención con declaración formal**: el Estado que se abstiene con **declaración formal** no aplica la decisión, pero la acepta como vinculante para la Unión"],
         "Si los que se abstienen así representan **al menos un tercio de los Estados** con **un tercio de la población**, no se adopta la decisión",
         "La abstención con declaración **no impide** la decisión (salvo el doble tercio)."))}

{unidad("4.2 Mayoría cualificada y sus límites (art. 31.2 a 5)",
  lit("TUE", tf(31), ["el Consejo adoptará por mayoría cualificada", "por motivos vitales y explícitos de política nacional", "no se aplicarán a las decisiones que tengan repercusiones en el ámbito militar o de la defensa", "por mayoría de los miembros que lo componen"], solo=[3, 4, 5, 6, 7, 8, 9, 10, 11]),
  fichab("Cuándo el Consejo decide por mayoría cualificada en la PESC", "Consejo; Alto Representante (busca una solución); Consejo Europeo (decide por unanimidad si se le remite)",
         ["::Mayoría cualificada (31.2):", "Acción o posición a partir de una decisión del Consejo Europeo sobre intereses estratégicos", "Acción o posición a partir de una propuesta del Alto Representante pedida por el Consejo Europeo", "Aplicación de una decisión que establezca una acción o posición", "Designación de un **representante especial**"],
         ["Freno: **motivos vitales y explícitos de política nacional** → no se vota", "Pasarela: el Consejo Europeo, **por unanimidad**, puede ampliar la mayoría cualificada (31.3)", "Cuestiones de **procedimiento**: **mayoría de los miembros** (31.5)"],
         "**Nunca** mayoría cualificada en decisiones con repercusiones **militares o de defensa** (31.4)."))}
""", 2)

T.ap("s17", "III.5 La política común de seguridad y defensa (TUE, arts. 42 y 46)", f"""
{unidad("5.1 Qué es la PCSD (art. 42.1 y 2)",
  lit("TUE", tf(42), ["forma parte integrante de la política exterior y de seguridad común", "en misiones fuera de la Unión", "una vez que el Consejo Europeo lo haya decidido por unanimidad", "Organización del Tratado del Atlántico Norte (OTAN)"], solo=[1, 2, 3]),
  fichab("Política común de seguridad y defensa", "La Unión, con capacidades **civiles y militares** de los Estados",
         ["Misiones **fuera** de la Unión: mantenimiento de la paz, prevención de conflictos, seguridad internacional", "Definición progresiva de una política común de defensa"],
         "La **defensa común** exige decisión del **Consejo Europeo por unanimidad** y que los Estados la adopten según sus normas constitucionales",
         "Respeta el carácter específico de la política de defensa de algunos Estados y las obligaciones de la **OTAN**."))}

{unidad("5.2 Ayuda y asistencia ante una agresión armada (art. 42.7)",
  lit("TUE", tf(42), ["objeto de una agresión armada en su territorio", "con todos los medios a su alcance", "artículo 51 de la Carta de las Naciones Unidas"], solo=[9, 10]),
  fichab("Obligación de ayuda si un Estado es agredido", "Los **demás Estados miembros**",
         "Ayuda y asistencia **con todos los medios a su alcance**", "—",
         "Supuesto: **agresión armada en su territorio**; base: **art. 51 de la Carta de las Naciones Unidas**; la OTAN sigue siendo el fundamento de la defensa colectiva de sus miembros."))}

{unidad("5.3 La cooperación estructurada permanente (arts. 42.6 y 46)",
  lit("TUE", tf(42), ["establecerán una cooperación estructurada permanente"], solo=[8]),
  lit("TUE", tf(46), ["En un plazo de tres meses", "se pronunciará por mayoría cualificada"], solo=[1, 2]),
  fichab("Cooperación más estrecha en defensa entre los Estados con mayores capacidades militares", "Estados que cumplen **criterios más elevados** de capacidades militares; el **Consejo** la establece",
         "Notificación al Consejo y al Alto Representante; decisión del Consejo con la lista de participantes",
         "Decisión en **tres meses** desde la notificación, por **mayoría cualificada**, tras consultar al Alto Representante",
         "Es una excepción a la unanimidad: se **crea** por **mayoría cualificada** (las demás decisiones en su seno, por unanimidad de los participantes, 46.6)."))}

{resumen([
  "La PESC está en el **TUE**; la definen **Consejo Europeo** y **Consejo** por **unanimidad**, **sin actos legislativos**; el **TJUE no es competente** salvo el art. 40 TUE y el art. 275 TFUE (24.1).",
  "El **Alto Representante** preside el **Consejo de Asuntos Exteriores**, representa a la Unión y se apoya en el **SEAE** (27).",
  "**Abstención con declaración formal** (31.1); mayoría cualificada solo en los casos del 31.2 y **nunca** en defensa (31.4); procedimiento: mayoría de los miembros (31.5).",
  "PCSD: misiones fuera de la Unión; **ayuda y asistencia** ante una agresión armada (42.7); **cooperación estructurada permanente** creada por mayoría cualificada en **tres meses** (46)."],
  "Siguiente: IV. ¿Qué es el espacio de libertad, seguridad y justicia?")}
""", 2)

# =============================================================================
# BLOQUE IV. ELSJ
T.ap("bIV", "IV. ¿Qué es el espacio de libertad, seguridad y justicia? (TFUE, arts. 67 a 89)", donde(
  "Cuarta política del epígrafe (el programa la llama «espacio de seguridad, libertad y justicia»; el TFUE, **espacio de libertad, seguridad y justicia**). Es una competencia **compartida** (art. 4.2 j) con cuatro piezas: fronteras, asilo e inmigración; cooperación judicial civil; cooperación judicial penal; y cooperación policial.",
  ["1 Objetivos, orientaciones e iniciativa (arts. 67, 68 y 76)", "2 Fronteras, asilo e inmigración (arts. 77 a 79)", "3 Cooperación judicial civil y penal (arts. 81 a 83)", "4 Eurojust, Fiscalía Europea, cooperación policial y Europol (arts. 85 a 88)"]))

T.ap("s18", "IV.1 Objetivos, orientaciones e iniciativa (TFUE, arts. 67, 68 y 76)", f"""
{unidad("1.1 Qué garantiza el espacio (art. 67)",
  lit(TF, tf(67), ["dentro del respeto de los derechos fundamentales y de los distintos sistemas y tradiciones jurídicos", "la ausencia de controles de las personas en las fronteras interiores", "los apátridas se asimilarán a los nacionales de terceros países", "reconocimiento mutuo"]),
  fichab("El espacio de libertad, seguridad y justicia", f"La Unión (competencia compartida: {c(TF, tf(4), 'el espacio de libertad, seguridad y justicia')}, art. 4.2 j)",
         ["Sin controles en las **fronteras interiores**; política común de **asilo, inmigración y fronteras exteriores**", "**Seguridad**: prevención de la delincuencia, el racismo y la xenofobia; cooperación policial y judicial", "**Justicia**: tutela judicial y **reconocimiento mutuo** de resoluciones"],
         "—",
         "Los **apátridas** se asimilan a los nacionales de terceros países. Principio transversal: el **reconocimiento mutuo**."))}

{unidad("1.2 Orientaciones estratégicas del Consejo Europeo (art. 68)",
  lit(TF, tf(68), ["El Consejo Europeo definirá las orientaciones estratégicas"]),
  fichab("Programación del espacio", "El **Consejo Europeo**", "Define las orientaciones estratégicas de la programación **legislativa y operativa**", "—",
         f"Es el **Consejo Europeo** (no el Consejo ni la Comisión). Y el título se entiende {c(TF, tf(72), 'sin perjuicio del ejercicio de las responsabilidades que incumben a los Estados miembros en cuanto al mantenimiento del orden público y la salvaguardia de la seguridad interior')} (art. 72)."))}

{unidad("1.3 Iniciativa compartida en cooperación penal y policial (art. 76)",
  lit(TF, tf(76), ["por iniciativa de la cuarta parte de los Estados miembros"]),
  fichab("Quién propone los actos de cooperación judicial penal y policial (capítulos 4 y 5)", "La **Comisión** o **la cuarta parte de los Estados miembros**",
         "Propuesta o iniciativa", "Una **cuarta parte** de los Estados",
         "Excepción al monopolio de iniciativa de la Comisión: solo en los capítulos **4** (penal) y **5** (policial)."))}
""", 2)

T.ap("s19", "IV.2 Fronteras, asilo e inmigración (TFUE, arts. 77 a 79)", f"""
{unidad("2.1 Fronteras (art. 77.1 y 2)",
  lit(TF, tf(77), ["la ausencia total de controles de las personas, sea cual sea su nacionalidad", "un sistema integrado de gestión de las fronteras exteriores", "la política común de visados"], solo=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
  fichab("Política de fronteras", "El Parlamento Europeo y el Consejo (procedimiento legislativo **ordinario**)",
         ["Interiores: **ausencia total** de controles, sea cual sea la nacionalidad", "Exteriores: controles y **vigilancia eficaz**; sistema integrado de gestión", "Visados y permisos de residencia de **corta** duración"], "Procedimiento legislativo ordinario",
         "La delimitación geográfica de las fronteras sigue siendo de los **Estados** (77.4)."))}

{unidad("2.2 Asilo (art. 78.1)",
  lit(TF, tf(78), ["asilo, protección subsidiaria y protección temporal", "principio de no devolución", "Convención de Ginebra de 28 de julio de 1951"], solo=[1]),
  fichab("Política común de asilo", "La Unión; medidas del Parlamento Europeo y el Consejo por procedimiento **ordinario** (78.2)",
         ["Asilo, protección **subsidiaria** y protección **temporal**", "Respeto del principio de **no devolución**", "Sistema europeo común de asilo"], "—",
         "Se ajusta a la **Convención de Ginebra de 1951** y al **Protocolo de 1967**. Ante una afluencia repentina, el Consejo puede adoptar **medidas provisionales** (78.3)."))}

{unidad("2.3 Inmigración (art. 79.1 y 5)",
  lit(TF, tf(79), ["una gestión eficaz de los flujos migratorios", "trata de seres humanos", "volúmenes de admisión"], solo=[1, 9]),
  fichab("Política común de inmigración", "La Unión; los **Estados** conservan los volúmenes de admisión",
         ["Gestión eficaz de los **flujos migratorios**", "Trato equitativo de los residentes legales", "Prevención y lucha contra la **inmigración ilegal** y la **trata**"], "—",
         "Los Estados fijan los **volúmenes de admisión** de nacionales de terceros países que buscan trabajo (79.5); la integración se apoya **sin armonización** (79.4)."))}
""", 2)

T.ap("s20", "IV.3 Cooperación judicial civil y penal (TFUE, arts. 81 a 83)", f"""
{unidad("3.1 Cooperación judicial civil (art. 81.1 y 3)",
  lit(TF, tf(81), ["con repercusión transfronteriza, basada en el principio de reconocimiento mutuo de las resoluciones judiciales y extrajudiciales", "las medidas relativas al Derecho de familia con repercusión transfronteriza se establecerán por el Consejo"], solo=[1, 11]),
  fichab("Cooperación judicial en asuntos civiles", "Parlamento Europeo y Consejo (ordinario); **Derecho de familia**: el **Consejo**",
         "Basada en el **reconocimiento mutuo** de resoluciones judiciales **y extrajudiciales**",
         "Derecho de familia: procedimiento legislativo **especial**, **unanimidad** del Consejo, previa **consulta** al Parlamento Europeo",
         "En lo civil se reconocen también las resoluciones **extrajudiciales**; el Derecho de familia exige **unanimidad**."))}

{unidad("3.2 Cooperación judicial penal (art. 82.1 y 2)",
  lit(TF, tf(82), ["se basará en el principio de reconocimiento mutuo de las sentencias y resoluciones judiciales", "normas mínimas mediante directivas"], solo=[1, 2, 3, 4, 5, 6, 7]),
  fichab("Cooperación judicial en materia penal", "Parlamento Europeo y Consejo (procedimiento legislativo **ordinario**)",
         ["Principio: **reconocimiento mutuo** de sentencias y resoluciones judiciales", "Incluye la **aproximación** de legislaciones", "**Normas mínimas** por **directivas** (pruebas, derechos de las personas y de las víctimas)"],
         "Si un Estado considera que una directiva afecta a aspectos fundamentales de su sistema penal, puede remitir el asunto al Consejo Europeo; sin acuerdo en **cuatro meses**, cooperación reforzada con **al menos nueve** Estados (82.3)",
         "Cayó en 2025 (→ Cierre 1): **reconocimiento mutuo**, no atribución, proporcionalidad ni subsidiariedad."))}

{unidad("3.3 Infracciones penales de especial gravedad (art. 83.1)",
  lit(TF, tf(83), ["de especial gravedad y tengan una dimensión transfronteriza", "el terrorismo, la trata de seres humanos"], solo=[1, 2, 3]),
  fichab("Normas mínimas sobre infracciones y sanciones penales", "Parlamento Europeo y Consejo, mediante **directivas** (ordinario)",
         "Ámbitos delictivos de **especial gravedad** con **dimensión transfronteriza**",
         "Ampliar la lista: decisión del Consejo por **unanimidad**, previa **aprobación** del Parlamento Europeo",
         "Ámbitos: terrorismo, trata de seres humanos y explotación sexual de mujeres y niños, tráfico ilícito de drogas y de armas, blanqueo de capitales, corrupción, falsificación de medios de pago, delincuencia informática y delincuencia organizada."))}
""", 2)

T.ap("s21", "IV.4 Eurojust, Fiscalía Europea, cooperación policial y Europol (TFUE, arts. 85 a 88)", f"""
{unidad("4.1 Eurojust (art. 85.1)",
  lit(TF, tf(85), ["apoyar y reforzar la coordinación y la cooperación entre las autoridades nacionales encargadas de investigar y perseguir la delincuencia grave"], solo=[1, 2]),
  fichab("Eurojust: coordinación judicial penal", "Eurojust; su estructura y competencias, por **reglamentos** (ordinario)",
         "Apoya la coordinación de las autoridades nacionales frente a la delincuencia grave que afecte a **dos o más** Estados", "—",
         "Los actos procesales formales los realizan los **funcionarios nacionales** (85.2)."))}

{unidad("4.2 La Fiscalía Europea (art. 86.1 y 2)",
  lit(TF, tf(86), ["una Fiscalía Europea a partir de Eurojust", "El Consejo se pronunciará por unanimidad, previa aprobación del Parlamento Europeo", "un grupo de al menos nueve Estados miembros", "Ejercerá ante los órganos jurisdiccionales competentes de los Estados miembros la acción penal"], solo=[1, 2, 3, 4]),
  fichab("Fiscalía Europea", "La crea el **Consejo** «a partir de **Eurojust**»",
         "Descubre, persigue y lleva a juicio a los autores de infracciones contra los **intereses financieros de la Unión**; ejerce la acción penal ante los tribunales **nacionales**",
         "Reglamentos por procedimiento **especial**: **unanimidad** del Consejo y **aprobación** del Parlamento Europeo; sin unanimidad, al menos **nueve** Estados pueden ir a una cooperación reforzada",
         "Competencia: **intereses financieros de la Unión**; ampliable por el Consejo Europeo por unanimidad (86.4)."))}

{unidad("4.3 Cooperación policial (art. 87.1)",
  lit(TF, tf(87), ["incluidos los servicios de policía, los servicios de aduanas"], solo=[1]),
  fichab("Cooperación policial", "Todas las autoridades competentes de los Estados (policía, aduanas y otros servicios coercitivos)",
         "Información, formación, técnicas comunes de investigación (87.2, ordinario)",
         "Cooperación **operativa**: procedimiento **especial**, unanimidad del Consejo previa consulta al Parlamento (87.3)",
         "Incluye a los servicios de **aduanas**."))}

{unidad("4.4 Europol (art. 88.1 y 3)",
  lit(TF, tf(88), ["La función de Europol es apoyar y reforzar la actuación de las autoridades policiales", "La aplicación de medidas coercitivas corresponderá exclusivamente a las autoridades nacionales competentes"], solo=[1, 6]),
  fichab("Europol: apoyo a las policías nacionales", "Europol; estructura y competencias por **reglamentos** (ordinario), con control del Parlamento Europeo y de los Parlamentos nacionales",
         "Apoya frente a la delincuencia grave de **dos o más** Estados, el **terrorismo** y las formas de delincuencia que lesionen un interés común",
         "—",
         "Europol **no** aplica medidas coercitivas: corresponden **exclusivamente** a las autoridades **nacionales**."))}

{resumen([
  "Espacio de libertad, seguridad y justicia: competencia **compartida** (4.2 j); sin controles en fronteras interiores; los **apátridas** se asimilan a nacionales de terceros países (67).",
  "El **Consejo Europeo** fija las orientaciones estratégicas (68); en lo penal y policial, iniciativa también de **la cuarta parte de los Estados** (76).",
  "Civil: reconocimiento mutuo de resoluciones judiciales **y extrajudiciales**; Derecho de familia por **unanimidad** (81). Penal: **reconocimiento mutuo** de sentencias y resoluciones (82.1).",
  "**Fiscalía Europea**, creada **a partir de Eurojust** por **unanimidad** y con **aprobación** del Parlamento (86); **Europol** no aplica medidas coercitivas (88.3)."],
  "Siguiente: V. ¿Qué prohíben las normas de competencia y quién las aplica?")}
""", 2)

# =============================================================================
# BLOQUE V. COMPETENCIA
T.ap("bV", "V. ¿Qué prohíben las normas de competencia y quién las aplica? (TFUE, arts. 101 a 108)", donde(
  "Quinta política del epígrafe: la **defensa de la competencia**. El TFUE prohíbe a las **empresas** los acuerdos colusorios y el abuso de posición dominante, y a los **Estados** las ayudas que falseen la competencia. La **Comisión** vela por su aplicación.",
  ["1 Normas aplicables a las empresas (arts. 3.1 b, 101 y 102)", "2 Aplicación por la Comisión y empresas públicas (arts. 105 y 106)", "3 Ayudas otorgadas por los Estados (arts. 107 y 108)"]))

T.ap("s22", "V.1 Normas aplicables a las empresas (TFUE, arts. 3.1 b, 101 y 102)", f"""
{unidad("1.1 Competencia exclusiva (art. 3.1 b)",
  lit(TF, tf(3), ["b) el establecimiento de las normas sobre competencia necesarias para el funcionamiento del mercado interior;"], solo=[1, 3]),
  fichab("Quién fija las normas de competencia", "La **Unión**, en exclusiva", "Las normas **necesarias para el funcionamiento del mercado interior**", "—",
         "Exclusiva **solo** en lo necesario para el funcionamiento del mercado interior."))}

{unidad("1.2 Acuerdos entre empresas prohibidos (art. 101.1 y 2)",
  lit(TF, tf(101), ["Serán incompatibles con el mercado interior y quedarán prohibidos", "que puedan afectar al comercio entre los Estados miembros", "serán nulos de pleno derecho"], solo=[1, 2, 3, 4, 5, 6, 7]),
  fichab("Prohibición de acuerdos, decisiones y prácticas concertadas restrictivos", "**Empresas** y **asociaciones de empresas**",
         ["Acuerdos, decisiones de asociaciones y **prácticas concertadas**", "Que puedan **afectar al comercio entre los Estados miembros**", "Con **objeto o efecto** de impedir, restringir o falsear la competencia (p. ej., fijar precios, repartirse mercados)"],
         "—",
         "Consecuencia: **nulos de pleno derecho** (101.2). Basta el **objeto** o el **efecto**."))}

{unidad("1.3 Exención (art. 101.3)",
  lit(TF, tf(101), ["podrán ser declaradas inaplicables", "reserven al mismo tiempo a los usuarios una participación equitativa en el beneficio resultante"], solo=[8, 9, 10, 11, 12, 13, 14]),
  fichab("Cuándo un acuerdo restrictivo puede quedar exento", "Acuerdos o categorías de acuerdos, decisiones y prácticas concertadas",
         ["::Requisitos acumulativos:", "Mejorar la producción o distribución, o fomentar el progreso técnico o económico", "Participación equitativa de los **usuarios** en el beneficio", "Restricciones **indispensables**", "Sin posibilidad de **eliminar la competencia** en una parte sustancial de los productos"],
         "—",
         "Son **cuatro** condiciones, dos positivas y dos negativas."))}

{unidad("1.4 Abuso de posición dominante (art. 102)",
  lit(TF, tf(102), ["la explotación abusiva, por parte de una o más empresas, de una posición dominante", "en una parte sustancial del mismo"]),
  fichab("Prohibición del abuso de posición dominante", "**Una o más** empresas con posición dominante",
         ["Lo prohibido es la **explotación abusiva**, no la posición dominante en sí", "Ejemplos: precios no equitativos, limitar la producción, condiciones desiguales, prestaciones suplementarias"],
         "—",
         "Posición dominante en el mercado interior **o en una parte sustancial** de él; puede ser de **una o más** empresas."))}
""", 2)

T.ap("s23", "V.2 Aplicación por la Comisión y empresas públicas (TFUE, arts. 105 y 106)", f"""
{unidad("2.1 La Comisión vela por los arts. 101 y 102 (art. 105.1 y 2)",
  lit(TF, tf(105), ["la Comisión velará por la aplicación de los principios enunciados en los artículos 101 y 102", "A instancia de un Estado miembro o de oficio", "mediante una decisión motivada"], solo=[1, 2]),
  fichab("Control de la competencia", "La **Comisión**, con la asistencia de las autoridades nacionales",
         ["Investiga **a instancia de un Estado o de oficio**", "Propone medidas para poner término a la infracción", "Si no cesa: **decisión motivada**, que puede publicar"],
         f"Las normas de aplicación de los arts. 101 y 102, por {c(TF, tf(103), 'El Consejo, a propuesta de la Comisión y previa consulta al Parlamento Europeo')} (art. 103.1)",
         "La guardiana de la competencia es la **Comisión**; la multa la prevén los reglamentos del art. 103."))}

{unidad("2.2 Empresas públicas y servicios de interés económico general (art. 106.1 y 2)",
  lit(TF, tf(106), ["empresas públicas y aquellas empresas a las que concedan derechos especiales o exclusivos", "servicios de interés económico general", "el cumplimiento de la misión específica a ellas confiada"], solo=[1, 2]),
  fichab("Las normas de competencia y el sector público", "Estados miembros y empresas públicas o con derechos especiales o exclusivos; la **Comisión** vela (106.3)",
         ["Los Estados no adoptan medidas contrarias a los Tratados respecto de sus empresas públicas", "Las empresas de **servicios de interés económico general** y los **monopolios fiscales** quedan sometidos a la competencia…", "…en la medida en que no impida el cumplimiento de su **misión específica**"],
         "—", "La excepción del 106.2 protege la **misión específica** confiada, no a la empresa."))}
""", 2)

T.ap("s24", "V.3 Ayudas otorgadas por los Estados (TFUE, arts. 107 y 108)", f"""
{unidad("3.1 Regla general: incompatibilidad (art. 107.1)",
  lit(TF, tf(107), ["las ayudas otorgadas por los Estados o mediante fondos estatales, bajo cualquier forma", "favoreciendo a determinadas empresas o producciones"], solo=[1]),
  fichab("Ayudas de Estado incompatibles", "**Estados** (ayudas otorgadas por ellos o mediante fondos estatales)",
         ["Ayuda pública **bajo cualquier forma**", "Que **favorezca a determinadas** empresas o producciones", "Que falsee o amenace falsear la competencia", "Que afecte a los intercambios entre Estados miembros"], "—",
         "«Salvo que los Tratados dispongan otra cosa»: la regla es la **incompatibilidad**."))}

{unidad("3.2 Ayudas compatibles de pleno derecho (art. 107.2)",
  lit(TF, tf(107), ["Serán compatibles con el mercado interior", "las ayudas de carácter social concedidas a los consumidores individuales", "desastres naturales"], solo=[2, 3, 4, 5]),
  fichab("Ayudas que son compatibles", "—",
         ["Ayudas **sociales** a consumidores individuales, sin discriminar por el origen de los productos", "Ayudas para reparar **desastres naturales** o acontecimientos excepcionales", "Ayudas a regiones alemanas afectadas por la división"], "—",
         f"{c(TF, tf(107), '**Serán** compatibles')} (107.2) frente a {c(TF, tf(107), '**Podrán** considerarse compatibles')} (107.3)."))}

{unidad("3.3 Ayudas que pueden ser compatibles (art. 107.3)",
  lit(TF, tf(107), ["Podrán considerarse compatibles con el mercado interior", "nivel de vida sea anormalmente bajo", "proyecto importante de interés común europeo", "promover la cultura y la conservación del patrimonio"], solo=[6, 7, 8, 9, 10, 11]),
  fichab("Ayudas que pueden declararse compatibles", "La Comisión las valora; el **Consejo** puede añadir categorías, a propuesta de la Comisión (107.3 e)",
         ["Desarrollo de regiones con nivel de vida **anormalmente bajo** o grave subempleo, y regiones del art. 349", "**Proyecto importante de interés común europeo** o grave perturbación de la economía de un Estado", "Desarrollo de actividades o regiones", "**Cultura** y conservación del patrimonio"], "—",
         f"Aquí la compatibilidad **no es automática**: {c(TF, tf(107), 'Podrán considerarse')}."))}

{unidad("3.4 Control de la Comisión y papel del Consejo (art. 108.2 y 3)",
  lit(TF, tf(108), ["decidirá que el Estado interesado la suprima o modifique", "podrá recurrir directamente al Tribunal de Justicia de la Unión Europea", "por unanimidad", "dentro de los tres meses siguientes a la petición", "no podrá ejecutar las medidas proyectadas"], solo=[2, 3, 4, 5, 6]),
  fichab("Procedimiento de control de las ayudas", "**Comisión** (examina y decide); **Consejo** (excepcionalmente, a petición de un Estado)",
         ["Proyectos de ayuda: se **notifican** a la Comisión con antelación", "Si es incompatible: la Comisión decide que el Estado la **suprima o modifique**", "Incumplimiento: recurso **directo** al Tribunal de Justicia"],
         "Consejo: **unanimidad**; si no se pronuncia en **tres meses**, decide la Comisión",
         "El Estado no puede ejecutar la ayuda proyectada hasta la decisión definitiva (108.3)."))}

{resumen([
  "Competencia: **exclusiva** de la Unión en lo necesario para el mercado interior (3.1 b).",
  "Empresas: prohibidos los acuerdos colusorios, **nulos de pleno derecho** (101.1 y 2), salvo exención con **cuatro** condiciones (101.3); y el **abuso** de posición dominante (102).",
  "La **Comisión** vela por su aplicación, **de oficio** o a instancia de un Estado (105).",
  "Ayudas de Estado: incompatibles como regla (107.1); «**Serán**» compatibles las del 107.2 y «**Podrán**» serlo las del 107.3; la Comisión controla y el Estado **no ejecuta** la ayuda antes de la decisión (108.3)."],
  "Siguiente: VI. ¿Qué persiguen la política agrícola común y la pesquera?")}
""", 2)

# =============================================================================
# BLOQUE VI. AGRICULTURA Y PESCA
T.ap("bVI", "VI. ¿Qué persiguen la política agrícola común y la pesquera? (TFUE, arts. 38 a 43; Reglamento FEMPA)", donde(
  "Sexta y última política del epígrafe. El TFUE trata **juntas** la agricultura y la pesca: el mercado interior abarca los productos agrícolas y de la pesca, y la Unión define una **política común de agricultura y pesca**. Su financiación general es del tema II.5; aquí, solo el FEMPA por la pregunta de 2025.",
  ["1 Competencia y ámbito (arts. 3.1 d, 4.2 d y 38)", "2 Objetivos de la PAC (art. 39)", "3 Organización común de mercados y procedimiento (arts. 40, 42 y 43)", "4 El Fondo Europeo Marítimo, de Pesca y de Acuicultura (Reglamento (UE) 2021/1139)"]))

T.ap("s25", "VI.1 Competencia y ámbito (TFUE, arts. 3.1 d, 4.2 d y 38)", f"""
{unidad("1.1 Conservación de recursos marinos, exclusiva; agricultura y pesca, compartidas (arts. 3.1 d y 4.2 d)",
  lit(TF, tf(3), ["d) la conservación de los recursos biológicos marinos dentro de la política pesquera común;"], solo=[1, 5]),
  lit(TF, tf(4), ["con exclusión de la conservación de los recursos biológicos marinos"], solo=[2, 6]),
  fichab("Tipo de competencia en agricultura y pesca", "La Unión (y los Estados en lo compartido)",
         ["**Conservación de los recursos biológicos marinos** en la política pesquera común: **exclusiva** (3.1 d)", "**Agricultura y pesca** en lo demás: **compartida** (4.2 d)"], "—",
         "Lo exclusivo es solo la **conservación** de los recursos biológicos **marinos**."))}

{unidad("1.2 Política común de agricultura y pesca (art. 38.1)",
  lit(TF, tf(38), ["una política común de agricultura y pesca", "los productos de la tierra, de la ganadería y de la pesca", "abarcan también la pesca"], solo=[1, 2]),
  fichab("Ámbito de la PAC", "La Unión la define y aplica",
         ["El mercado interior abarca la **agricultura, la pesca y el comercio** de productos agrícolas", "Productos agrícolas: de la **tierra**, de la **ganadería** y de la **pesca**, y los de **primera transformación**", "Las referencias a la PAC **abarcan también la pesca**"], "—",
         "Los productos sujetos a los arts. 39 a 44 son los del **anexo I** (38.3)."))}
""", 2)

T.ap("s26", "VI.2 Objetivos de la política agrícola común (TFUE, art. 39)", f"""
{unidad("2.1 Los cinco objetivos (art. 39.1)",
  lit(TF, tf(39), ["incrementar la productividad agrícola", "un nivel de vida equitativo a la población agrícola", "estabilizar los mercados", "garantizar la seguridad de los abastecimientos", "precios razonables"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Para qué sirve la PAC", "—",
         ["Incrementar la **productividad** agrícola", "**Nivel de vida equitativo** de la población agrícola", "**Estabilizar** los mercados", "**Seguridad** de los abastecimientos", "**Precios razonables** para el consumidor"], "—",
         "Son **cinco** objetivos; el del consumidor habla de **precios razonables** (no «bajos» ni «mínimos»)."))}

{unidad("2.2 Qué se tiene en cuenta al elaborarla (art. 39.2)",
  lit(TF, tf(39), ["las características especiales de la actividad agrícola", "efectuar gradualmente las oportunas adaptaciones", "estrechamente vinculado al conjunto de la economía"], solo=[7, 8, 9, 10]),
  fichab("Criterios de elaboración de la PAC", "—",
         ["Características especiales de la actividad agrícola y desigualdades entre regiones", "Adaptaciones **graduales**", "La agricultura, vinculada al conjunto de la economía"], "—", "—"))}
""", 2)

T.ap("s27", "VI.3 Organización común de mercados y procedimiento (TFUE, arts. 40, 42 y 43)", f"""
{unidad("3.1 La organización común de los mercados agrícolas (art. 40.1 y 2)",
  lit(TF, tf(40), ["normas comunes sobre la competencia", "una coordinación obligatoria de las diversas organizaciones nacionales de mercado", "una organización europea del mercado", "deberá excluir toda discriminación entre productores o consumidores de la Unión"], solo=[1, 2, 3, 4, 5, 6, 7]),
  fichab("Instrumento de la PAC", "La Unión (se crea por el propio art. 40)",
         ["::Tres formas, según los productos:", "Normas comunes sobre la competencia", "Coordinación obligatoria de las organizaciones nacionales", "Organización europea del mercado"],
         "—",
         f"Puede incluir regulación de precios, subvenciones, almacenamiento y estabilización; prohibida toda **discriminación** entre productores o consumidores. Se podrán crear {c(TF, tf(40), 'uno o más fondos de orientación y de garantía agrícolas')} (40.3)."))}

{unidad("3.2 Competencia y ayudas en la agricultura (art. 42)",
  lit(TF, tf(42), ["sólo en la medida determinada por el Parlamento Europeo y el Consejo", "explotaciones desfavorecidas"]),
  fichab("Aplicación limitada de las normas de competencia a la agricultura", "Parlamento Europeo y Consejo (alcance); **Consejo**, a propuesta de la Comisión (ayudas)",
         ["Las normas de competencia se aplican **solo en la medida** que decidan el Parlamento y el Consejo", "Ayudas autorizables: explotaciones **desfavorecidas** y programas de desarrollo económico"], "—",
         "Excepción al régimen general del bloque V (→ V.1.2)."))}

{unidad("3.3 Quién decide en la PAC y en la pesca (art. 43.1 a 3)",
  lit(TF, tf(43), ["La Comisión presentará propuestas", "con arreglo al procedimiento legislativo ordinario y previa consulta al Comité Económico y Social", "la fijación y el reparto de las posibilidades de pesca"], solo=[1, 3, 4]),
  fichab("Procedimiento de la política común de agricultura y pesca",
         ["**Comisión**: propuestas", "**Parlamento Europeo y Consejo**: organización común de mercados y demás disposiciones (43.2)", "**Consejo**, a propuesta de la Comisión: precios, exacciones, ayudas, limitaciones cuantitativas y **posibilidades de pesca** (43.3)"],
         "—",
         "43.2: procedimiento legislativo **ordinario** y consulta al **Comité Económico y Social**",
         "Las **posibilidades de pesca** las fija y reparte **el Consejo** solo (43.3), no el Parlamento y el Consejo."))}
""", 2)

T.ap("s28", "VI.4 El Fondo Europeo Marítimo, de Pesca y de Acuicultura (Reglamento (UE) 2021/1139)", f"""
{unidad("4.1 Objeto y período (art. 1)",
  lit("FEMPA", tf(1), ["entre el 1 de enero de 2021 y el 31 de diciembre de 2027", "marco financiero plurianual 2021-2027"]),
  fichab("El FEMPA", "Fondo de la Unión para la política marítima, pesquera y de acuicultura",
         "Establece sus prioridades, presupuesto y normas específicas de financiación, que complementan el **Reglamento (UE) 2021/1060**",
         "**1-1-2021 a 31-12-2027**, como el marco financiero plurianual",
         "Su duración se ajusta al **MFP 2021-2027** (tema II.5)."))}

{unidad("4.2 Biodiversidad y ecosistemas acuáticos (art. 25.1)",
  lit("FEMPA", tf(25), ["incluso en las aguas interiores"], solo=[1, 2]),
  fichab("Apoyo a la protección y recuperación de la biodiversidad acuática", "El **FEMPA**",
         "Acciones de protección y recuperación de la biodiversidad y los ecosistemas acuáticos", "—",
         "«**incluso** en las aguas **interiores**»: no «salvo», ni «aguas fluviales». Fue pregunta de reserva en 2025 (→ Cierre 1)."))}

{resumen([
  "**Conservación de los recursos biológicos marinos**: competencia **exclusiva** (3.1 d); el resto de agricultura y pesca, **compartida** (4.2 d).",
  "Política **común** de agricultura y pesca; productos de la **tierra**, la **ganadería** y la **pesca** (38.1).",
  "**Cinco objetivos** de la PAC (39.1); organización común de mercados en **tres formas** (40.1).",
  "Ordinario + CES para la organización de mercados (43.2); el **Consejo** fija precios y **posibilidades de pesca** (43.3). FEMPA: 2021-2027; biodiversidad **incluso en las aguas interiores** (art. 25.1)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

T.ap("s29", "Pendiente (temario): lo que el epígrafe pide y no está en una norma", """
Estos apuntes se han limitado a lo que está en los Tratados, sus protocolos, el Reglamento del FEMPA y el Tratado de Estabilidad (BOE). Quedan **pendientes** de completar con el temario del usuario (sin fuente oficial descargada, no se incluyen):

- **Evolución histórica** de cada política: del mercado común al mercado interior; las fases de la unión económica y monetaria; el origen de la PESC y de la cooperación en justicia e interior; las sucesivas reformas de la PAC y de la política pesquera común.
- **Derecho derivado** de cada política: reglamentos de aplicación de los arts. 101 y 102, control de concentraciones, Reglamento de la política pesquera común, reglamentos de la PAC 2023-2027, normas del sistema Schengen y del sistema europeo común de asilo.
- **Instrumentos fuera de los Tratados** distintos del Tratado de Estabilidad (por ejemplo, el Mecanismo Europeo de Estabilidad) y la unión bancaria.
""")

# =============================================================================
# CIERRE 1. Preguntas oficiales
EX_P18 = examen("P", 18, {
  "a": "El art. 26 no habla de armonización fiscal. Cambia el contenido del mercado interior por una medida que el artículo no prevé.",
  "b": "El mercado interior no suprime las competencias nacionales: es una competencia **compartida** (art. 4.2 a).",
  "c": "No hay unificación presupuestaria en el art. 26; el mercado interior se define por la libre circulación, no por el presupuesto.",
  "d": f"Literal del art. 26.2: {c(TF, tf(26), 'El mercado interior implicará un espacio sin fronteras interiores')}, con la libre circulación de mercancías, personas, servicios y capitales."},
  [("espacio sin fronteras interiores", TF, tf(26), "un espacio sin fronteras interiores")])
EX_P15 = examen("P", 15, {
  "a": f"Literal del art. 59.1: {c(TF, tf(59), 'con arreglo al procedimiento legislativo ordinario y previa consulta al Comité Económico y Social, decidirán mediante directivas')}.",
  "b": "Cambia el instrumento: **reglamentos** en lugar de **directivas**.",
  "c": "Cambia el instrumento (recomendaciones, que no son vinculantes) y el procedimiento (especial en lugar de **ordinario**).",
  "d": "Cambia el instrumento (decisiones) y el procedimiento (especial en lugar de **ordinario**)."},
  [("Directivas", TF, tf(59), "decidirán mediante directivas"), ("procedimiento legislativo ordinario", TF, tf(59), "con arreglo al procedimiento legislativo ordinario")])
EX_L17 = examen("L", 17, {
  "a": f"Dinamarca no forma parte: {c('PROT16', 'Disposiciones', 'Dinamarca disfrutará de una excepción')} (Protocolo n.º 16, punto 1). La página oficial de la Unión lo confirma: Dinamarca ha mantenido su propia moneda.",
  "b": f"Letonia está en la lista oficial de los 21 países de la zona del euro (página oficial de la Unión; no es texto legal). En 2012 el Tratado de Estabilidad la citaba entre las Partes {c('TECG', 'preambulo', 'acogidas, en la fecha de la firma del presente Tratado, a una excepción a la participación en la moneda única')} (preámbulo).",
  "c": f"Eslovenia usa el euro: el Tratado de Estabilidad ya la incluía entre las {c('TECG', 'preambulo', 'Partes Contratantes cuya moneda es el euro')} (preámbulo) y está en la lista oficial.",
  "d": "Malta usa el euro: figura en la misma lista del preámbulo del Tratado de Estabilidad y en la lista oficial de la Unión."},
  [("Dinamarca", "PROT16", "Disposiciones", "Dinamarca disfrutará de una excepción")])
EX_L30 = examen("L", 30, {
  "a": "Chipre lo firmó: en el acta de la firma aparece «la República de Chipre».",
  "b": "Malta lo firmó: aparece en el acta de la firma.",
  "c": "Estonia lo firmó: en el acta aparece «la República de Estonia».",
  "d": "La **República Checa** no está en el acta de la firma (BOE-A-2013-1118): los firmantes son los **25** Estados que esta enumera. El Tratado queda abierto a la adhesión de los demás (art. 15)."},
  [("República Checa", "TECG", "preambulo", "Los plenipotenciarios del Reino de Bélgica, la República de Bulgaria, el Reino de Dinamarca, la República Federal de Alemania, la República de Estonia, Irlanda, la República Helénica, el Reino de España, la República Francesa, la República Italiana, la República de Chipre, la República de Letonia, la República de Lituania, el Gran Ducado de Luxemburgo, Hungría, Malta, el Reino de los Países Bajos, la República de Austria, la República de Polonia, la República Portuguesa, Rumania, la República de Eslovenia, la República Eslovaca, la República de Finlandia y el Reino de Suecia han firmado hoy")])
EX_X37 = examen("X", 37, {
  "a": f"Es un criterio (estabilidad de precios): inflación que no exceda {c('PROT13', 'Artículo 1', 'en más de 1½ punto porcentual')} la de, como máximo, los tres Estados con mejor comportamiento (Protocolo n.º 13, art. 1).",
  "b": f"Es un criterio (presupuesto): que el Estado {c('PROT13', 'Artículo 2', 'no sea objeto de una decisión del Consejo con arreglo al apartado 6 del artículo 126')}, relativa a un déficit excesivo (art. 2).",
  "c": f"**No** es el criterio: el tipo de interés a largo plazo no puede exceder {c('PROT13', 'Artículo 4', 'en más de 2 puntos porcentuales')} (art. 4). La opción cambia **2** por **tres** puntos.",
  "d": f"Es un criterio (tipo de cambio): {c('PROT13', 'Artículo 3', 'durante por lo menos los dos años anteriores al examen')}, sin tensiones graves y sin devaluar respecto del euro (art. 3)."},
  [("tres puntos porcentuales", "PROT13", "Artículo 4", "no exceda en más de 2 puntos porcentuales")])
EX_L29 = examen("L", 29, {
  "a": f"Literal del art. 82.1: {c(TF, tf(82), 'se basará en el principio de reconocimiento mutuo de las sentencias y resoluciones judiciales')}.",
  "b": f"La atribución es el principio que rige la **delimitación** de las competencias de la Unión: {c('TUE', tf(5), 'La delimitación de las competencias de la Unión se rige por el principio de atribución')} (TUE, art. 5.1).",
  "c": f"La proporcionalidad rige el **ejercicio** de las competencias (TUE, art. 5.1: {c('TUE', tf(5), 'se rige por los principios de subsidiariedad y proporcionalidad')}), no la base de la cooperación penal.",
  "d": f"La subsidiariedad también rige el **ejercicio** de las competencias (TUE, art. 5.1 y 3); en la cooperación penal y policial (capítulos 4 y 5 de este título) la vigilan los Parlamentos nacionales: {c(TF, tf(69), 'En relación con las propuestas e iniciativas legislativas presentadas en el marco de los capítulos 4 y 5, los Parlamentos nacionales velarán por que se respete el principio de subsidiariedad')} (TFUE, art. 69); pero no es la base de la cooperación penal."},
  [("Reconocimiento mutuo de las sentencias y resoluciones judiciales", TF, tf(82), "se basará en el principio de reconocimiento mutuo de las sentencias y resoluciones judiciales")])
EX_L102 = examen("L", 102, {
  "a": f"Literal del art. 25.1: {c('FEMPA', tf(25), 'El FEMPA podrá apoyar acciones que contribuyan a la protección y la recuperación de la biodiversidad y los ecosistemas acuáticos, incluso en las aguas interiores')}.",
  "b": "Cambia «**incluso**» por «**salvo**»: invierte el sentido.",
  "c": "Cambia «aguas **interiores**» por «aguas **fluviales**».",
  "d": "Cambia las dos cosas: «**salvo**» y «aguas **fluviales**»."},
  [("incluso en las aguas interiores", "FEMPA", tf(25), "incluso en las aguas interiores")])
EX_P19 = examen("P", 19, {
  "a": f"No es compartida: en el art. 4.2 (competencias compartidas) no está la política monetaria; sí {c(TF, tf(4), 'el mercado interior')}.",
  "b": "No es de apoyo y coordinación (art. 6 TFUE): el art. 3.1 c) la incluye entre las **exclusivas**.",
  "c": f"Literal del art. 3.1: {c(TF, tf(3), 'La Unión dispondrá de competencia exclusiva')} en {c(TF, tf(3), 'la política monetaria de los Estados miembros cuya moneda es el euro')}.",
  "d": "Los Tratados no hablan de competencias «residuales» de los Estados para la política monetaria del euro: es **exclusiva** de la Unión."},
  [("Exclusiva", TF, tf(3), "La Unión dispondrá de competencia exclusiva"), ("Exclusiva", TF, tf(3), "la política monetaria de los Estados miembros cuya moneda es el euro")])

T.ap("s30", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **siete** preguntas de este tema (una de ellas, de **reserva**) y **una** relacionada. Aquí están **literales**, en el orden de los bloques. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-P 2025, pregunta 18 · Mercado interior (→ I.1.2)", EX_P18,
  "### GACE-P 2025, pregunta 15 · Liberalización de servicios (→ I.4.3)", EX_P15,
  "### GACE-P 2025, pregunta 19 · Política monetaria, competencia exclusiva (relacionada; → II.1.1)", EX_P19,
  "### GACE-L 2025, pregunta 17 · La zona del euro (→ II.6.2 y II.6.5)", EX_L17,
  "### GACE-X 2025, pregunta 37 · Criterios de convergencia (→ II.6.4)", EX_X37,
  "### GACE-L 2025, pregunta 30 · Tratado de Estabilidad, Coordinación y Gobernanza (→ II.7.1)", EX_L30,
  "### GACE-L 2025, pregunta 29 · Cooperación judicial penal (→ IV.3.2)", EX_L29,
  "### GACE-L 2025, pregunta 102 (reserva) · FEMPA (→ VI.4.2)", EX_L102,
  "### Cómo se pregunta",
  "!> Dos estilos: **letra del Tratado** (art. 26, 59, 82, 3.1; Protocolo n.º 13; FEMPA), con distractores que cambian el instrumento, el procedimiento o una palabra; y **datos** (qué países usan el euro, quién firmó el Tratado de Estabilidad), que se resuelven con el protocolo de Dinamarca, el acta de la firma del TECG y la lista oficial de la zona del euro.",
]))

T.ap("s31", "Cierre 2. Repaso en 10 minutos (por bloques)", """
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Mercado interior | Espacio sin fronteras interiores y cuatro libertades (26); unión aduanera (28); arts. 34 a 36; trabajadores (45), establecimiento (49), servicios (56 y 57), capitales (63) | **Espacio sin fronteras interiores**; liberalización por **directivas**, ordinario y CES (59); 45.4 |
| II. UEM | Monetaria exclusiva (3.1 c); estabilidad de precios (119 y 127); arts. 123 a 126; criterios (140 y Protocolo n.º 13) | **3 %** y **60 %**; interés **2 puntos**; **Dinamarca** fuera del euro; TECG sin la **República Checa** |
| III. PESC | Unanimidad, sin actos legislativos, TJUE sin competencia (24); Alto Representante (27); art. 31; PCSD (42 y 46) | **Abstención con declaración formal**; nada de mayoría cualificada en **defensa** |
| IV. ELSJ | Compartida (4.2 j); fronteras, asilo e inmigración (77 a 79); cooperación civil y penal (81 a 83); Eurojust, Fiscalía Europea, Europol (85 a 88) | **Reconocimiento mutuo** (82.1); iniciativa de **un cuarto** de los Estados (76) |
| V. Competencia | Acuerdos (101), abuso (102), Comisión (105), ayudas (107 y 108) | **Nulos de pleno derecho**; «Serán» / «Podrán» compatibles |
| VI. Agricultura y pesca | Conservación de recursos marinos exclusiva (3.1 d); cinco objetivos (39); art. 43; FEMPA | **Posibilidades de pesca**: el Consejo (43.3); «incluso en las aguas interiores» |

?> **Trampas frecuentes:** «el mercado interior es competencia **exclusiva**» (es **compartida**; exclusiva es la **unión aduanera**); «servicios liberalizados por **reglamentos**» (por **directivas**); «interés a largo plazo, **tres** puntos» (son **dos**); «la PESC se adopta por **mayoría cualificada**» (regla: **unanimidad**); «el Tribunal de Justicia controla la PESC» (no, salvo art. 40 TUE y art. 275 TFUE); «la cooperación penal se basa en la **subsidiariedad**» (en el **reconocimiento mutuo**); «Europol detiene» (las medidas coercitivas son **nacionales**); «el FEMPA, **salvo** en aguas interiores» (es **incluso**).
""")

# =============================================================================
# Test
def Q(k, art, cat, enun, ops, expl, frags): T.q(k, art, cat, enun, ops, expl, frags)

Q(TF, tf(26), "Mercado interior", "Según el artículo 26.2 del TFUE, el mercado interior implicará:",
  ["Un espacio sin fronteras interiores, en el que la libre circulación de mercancías, personas, servicios y capitales estará garantizada.", "Un espacio sin fronteras exteriores, en el que la libre circulación de mercancías y capitales estará garantizada.", "Una unión aduanera con armonización fiscal plena entre los Estados miembros.", "Un espacio sin fronteras interiores limitado a la libre circulación de mercancías y servicios."],
  "Art. 26.2 TFUE.", "El mercado interior implicará un espacio sin fronteras interiores")
Q(TF, tf(4), "Mercado interior", "Según el artículo 4.2 del TFUE, el mercado interior es un ámbito de competencia:",
  ["Compartida entre la Unión y los Estados miembros.", "Exclusiva de la Unión.", "De apoyo, coordinación o complemento.", "Exclusiva de los Estados miembros."],
  "Art. 4.2 a) TFUE. La exclusiva es la unión aduanera (art. 3.1 a).", ["Las competencias compartidas entre la Unión y los Estados miembros", "a) el mercado interior;"])
Q(TF, tf(28), "Mercado interior", "Según el artículo 28.1 del TFUE, la unión aduanera implicará la adopción de un arancel aduanero común:",
  ["En sus relaciones con terceros países.", "En las relaciones entre los Estados miembros.", "Solo para los productos agrícolas.", "Para los productos en libre práctica en los Estados miembros."],
  "Art. 28.1 TFUE.", "la adopción de un arancel aduanero común en sus relaciones con terceros países")
Q(TF, tf(36), "Mercado interior", "Según el artículo 36 del TFUE, las prohibiciones o restricciones a la importación justificadas por razones de orden público no deberán constituir:",
  ["Un medio de discriminación arbitraria ni una restricción encubierta del comercio entre los Estados miembros.", "Una medida de efecto equivalente a un derecho de aduana.", "Una medida no notificada previamente a la Comisión.", "Una restricción superior a seis meses."],
  "Art. 36 TFUE, segunda frase.", "no deberán constituir un medio de discriminación arbitraria ni una restricción encubierta del comercio entre los Estados miembros")
Q(TF, tf(45), "Mercado interior", "Según el artículo 45.4 del TFUE, las disposiciones sobre libre circulación de trabajadores:",
  ["No serán aplicables a los empleos en la administración pública.", "Se aplicarán a todos los empleos, incluidos los de la administración pública.", "Solo se aplicarán a los empleos en la administración pública de la Unión.", "No serán aplicables a las profesiones liberales."],
  "Art. 45.4 TFUE.", "no serán aplicables a los empleos en la administración pública")
Q(TF, tf(51), "Mercado interior", "Según el artículo 51 del TFUE, las disposiciones sobre el derecho de establecimiento no se aplicarán a las actividades relacionadas, aunque sólo sea de manera ocasional, con:",
  ["El ejercicio del poder público.", "Las profesiones liberales.", "Las actividades industriales.", "La constitución de sociedades mercantiles."],
  "Art. 51 TFUE.", "aunque sólo sea de manera ocasional, con el ejercicio del poder público")
Q(TF, tf(57), "Mercado interior", "Según el artículo 57 del TFUE, se considerarán como servicios las prestaciones realizadas:",
  ["Normalmente a cambio de una remuneración.", "Siempre de forma gratuita.", "Exclusivamente por personas jurídicas.", "De forma permanente en otro Estado miembro."],
  "Art. 57 TFUE.", "las prestaciones realizadas normalmente a cambio de una remuneración")
Q(TF, tf(63), "Mercado interior", "Según el artículo 63.1 del TFUE, quedan prohibidas todas las restricciones a los movimientos de capitales:",
  ["Entre Estados miembros y entre Estados miembros y terceros países.", "Solo entre Estados miembros.", "Solo entre los Estados miembros cuya moneda es el euro.", "Entre Estados miembros, salvo las inversiones directas."],
  "Art. 63.1 TFUE.", "entre Estados miembros y entre Estados miembros y terceros países")
Q(TF, tf(66), "Mercado interior", "Según el artículo 66 del TFUE, las medidas de salvaguardia respecto a terceros países en materia de capitales podrán adoptarse por un plazo que no sea superior a:",
  ["Seis meses.", "Tres meses.", "Un año.", "Dos años."],
  "Art. 66 TFUE.", "por un plazo que no sea superior a seis meses")
Q(TF, tf(119), "UEM", "Según el artículo 119.2 del TFUE, el objetivo primordial de la política monetaria y de tipos de cambio única será:",
  ["Mantener la estabilidad de precios.", "Alcanzar el pleno empleo.", "Garantizar el crecimiento económico.", "Mantener la balanza de pagos equilibrada."],
  "Art. 119.2 TFUE.", "cuyo objetivo primordial sea mantener la estabilidad de precios")
Q(TF, tf(121), "UEM", "Según el artículo 121.2 del TFUE, las orientaciones generales de las políticas económicas de los Estados miembros y de la Unión las establece el Consejo mediante:",
  ["Una recomendación.", "Un reglamento.", "Una decisión.", "Una directiva."],
  "Art. 121.2 TFUE, párrafo tercero.", "el Consejo, adoptará una recomendación en la que establecerá dichas orientaciones generales")
Q(TF, tf(123), "UEM", "Según el artículo 123.1 del TFUE, queda prohibida la adquisición de instrumentos de deuda de los Gobiernos de los Estados miembros por el Banco Central Europeo cuando sea:",
  ["Directa.", "En el mercado secundario.", "Superior al 3 % del PIB.", "Sin autorización del Consejo."],
  "Art. 123.1 TFUE: lo prohibido es la adquisición directa.", "así como la adquisición directa a los mismos de instrumentos de deuda")
Q(TF, tf(126), "UEM", "Según el artículo 126.4 del TFUE, ¿quién emite un dictamen sobre el informe de la Comisión en el procedimiento de déficit excesivo?",
  ["El Comité Económico y Financiero.", "El Banco Central Europeo.", "El Parlamento Europeo.", "El Tribunal de Cuentas."],
  "Art. 126.4 TFUE.", "El Comité Económico y Financiero emitirá un dictamen sobre el informe de la Comisión")
Q(TF, tf(126), "UEM", "Según el artículo 126.10 del TFUE, en el marco de los apartados 1 a 9 del procedimiento de déficit excesivo:",
  ["No podrá ejercerse el derecho de recurso previsto en los artículos 258 y 259.", "Solo la Comisión podrá interponer el recurso del artículo 258.", "Cualquier Estado miembro podrá interponer el recurso del artículo 259.", "El Estado afectado podrá recurrir ante el Tribunal General."],
  "Art. 126.10 TFUE.", "no podrá ejercerse el derecho de recurso previsto en los artículos 258 y 259")
Q("PROT12", "Artículo 1", "UEM", "Según el artículo 1 del Protocolo n.º 12, el valor de referencia de la proporción entre la deuda pública y el producto interior bruto a precios de mercado es:",
  ["El 60 %.", "El 3 %.", "El 50 %.", "El 90 %."],
  "Protocolo n.º 12, art. 1: 3 % (déficit) y 60 % (deuda).", "60 % en lo referente a la proporción entre la deuda pública y el producto interior bruto")
Q(TF, tf(127), "UEM", "Según el artículo 127.1 del TFUE, el objetivo principal del Sistema Europeo de Bancos Centrales será:",
  ["Mantener la estabilidad de precios.", "Apoyar las políticas económicas generales de la Unión.", "Supervisar las entidades de crédito.", "Gestionar la deuda pública de los Estados miembros."],
  "Art. 127.1 TFUE: el apoyo a las políticas económicas va «sin perjuicio» del objetivo principal.", "El objetivo principal del Sistema Europeo de Bancos Centrales, denominado en lo sucesivo «SEBC», será mantener la estabilidad de precios")
Q(TF, tf(128), "UEM", "Según el artículo 128 del TFUE, la emisión de moneda metálica en euros corresponde a:",
  ["Los Estados miembros, con aprobación del Banco Central Europeo en cuanto al volumen de emisión.", "El Banco Central Europeo en exclusiva.", "La Comisión, previa consulta al Banco Central Europeo.", "Los bancos centrales nacionales, sin necesidad de aprobación."],
  "Art. 128.2 TFUE.", "Los Estados miembros podrán realizar emisiones de moneda metálica en euros, para las cuales será necesaria la aprobación del Banco Central Europeo en cuanto al volumen de emisión")
Q(TF, tf(140), "UEM", "Según el artículo 140.1 del TFUE, la Comisión y el Banco Central Europeo presentarán informes al Consejo sobre los Estados miembros acogidos a una excepción:",
  ["Una vez cada dos años como mínimo, o a petición de cualquier Estado miembro acogido a una excepción.", "Una vez al año, en todo caso.", "Cada cinco años.", "Solo a petición del Parlamento Europeo."],
  "Art. 140.1 TFUE.", "Una vez cada dos años como mínimo, o a petición de cualquier Estado miembro acogido a una excepción")
Q("PROT13", "Artículo 1", "UEM", "Según el artículo 1 del Protocolo n.º 13, la tasa promedio de inflación no debe exceder la de, como máximo, los tres Estados miembros con mejor comportamiento en materia de estabilidad de precios en más de:",
  ["1½ punto porcentual.", "2 puntos porcentuales.", "3 puntos porcentuales.", "½ punto porcentual."],
  "Protocolo n.º 13, art. 1 (el de 2 puntos es el del tipo de interés, art. 4).", "que no exceda en más de 1½ punto porcentual")
Q("PROT16", "Disposiciones", "UEM", "Según el Protocolo n.º 16, el procedimiento del artículo 140 del TFUE para la derogación de la excepción de Dinamarca:",
  ["Sólo se iniciará a petición de Dinamarca.", "Se iniciará de oficio cada dos años.", "Se iniciará a propuesta del Banco Central Europeo.", "No podrá iniciarse en ningún caso."],
  "Protocolo n.º 16, punto 2.", "sólo se iniciará a petición de Dinamarca")
Q("TECG", "preambulo", "UEM", "Según el artículo 12.1 del Tratado de Estabilidad, Coordinación y Gobernanza, el Presidente de la Cumbre del Euro será designado por los Jefes de Estado o de Gobierno de las Partes Contratantes cuya moneda es el euro:",
  ["Por mayoría simple.", "Por unanimidad.", "Por mayoría cualificada.", "Por mayoría de dos tercios."],
  "TECG, art. 12.1.", "será designado por mayoría simple")
Q("TECG", "preambulo", "UEM", "Según el artículo 3.1 a) del Tratado de Estabilidad, Coordinación y Gobernanza, la situación presupuestaria de las administraciones públicas de cada Parte Contratante será:",
  ["De equilibrio o de superávit.", "De déficit inferior al 3 %.", "De deuda inferior al 60 %.", "De equilibrio a lo largo del ciclo, con déficit máximo del 1 %."],
  "TECG, art. 3.1 a).", "la situación presupuestaria de las administraciones públicas de cada Parte Contratante será de equilibrio o de superávit")
Q("TUE", tf(24), "PESC", "Según el artículo 24.1 del TUE, la política exterior y de seguridad común la definirán y aplicarán el Consejo Europeo y el Consejo, que deberán pronunciarse:",
  ["Por unanimidad salvo cuando los Tratados dispongan otra cosa.", "Por mayoría cualificada salvo cuando los Tratados dispongan otra cosa.", "Por mayoría simple.", "Por consenso, previa aprobación del Parlamento Europeo."],
  "Art. 24.1 TUE.", "que deberán pronunciarse por unanimidad salvo cuando los Tratados dispongan otra cosa")
Q("TUE", tf(24), "PESC", "Según el artículo 24.1 del TUE, en la política exterior y de seguridad común:",
  ["Queda excluida la adopción de actos legislativos.", "Los actos se adoptan por el procedimiento legislativo ordinario.", "Los actos se adoptan por un procedimiento legislativo especial.", "El Tribunal de Justicia tiene plena competencia."],
  "Art. 24.1 TUE.", "Queda excluida la adopción de actos legislativos")
Q("TUE", tf(27), "PESC", "Según el artículo 27.1 del TUE, el Alto Representante de la Unión para Asuntos Exteriores y Política de Seguridad presidirá:",
  ["El Consejo de Asuntos Exteriores.", "El Consejo Europeo.", "El Comité Político y de Seguridad.", "El Consejo de Asuntos Generales."],
  "Art. 27.1 TUE.", "que presidirá el Consejo de Asuntos Exteriores")
Q("TUE", tf(27), "PESC", "Según el artículo 27.3 del TUE, la organización y el funcionamiento del servicio europeo de acción exterior se establecerán mediante decisión del Consejo, a propuesta del Alto Representante:",
  ["Previa consulta al Parlamento Europeo y previa aprobación de la Comisión.", "Previa aprobación del Parlamento Europeo y previa consulta a la Comisión.", "Previa consulta al Consejo Europeo.", "Previa aprobación de los Parlamentos nacionales."],
  "Art. 27.3 TUE.", "previa consulta al Parlamento Europeo y previa aprobación de la Comisión")
Q("TUE", tf(31), "PESC", "Según el artículo 31.1 del TUE, no se adoptará la decisión cuando los miembros del Consejo que acompañen su abstención de una declaración formal representen:",
  ["Al menos un tercio de los Estados miembros que reúnen como mínimo un tercio de la población de la Unión.", "Al menos la mitad de los Estados miembros.", "Al menos un cuarto de los Estados miembros que reúnen el 35 % de la población.", "Al menos dos tercios de los Estados miembros."],
  "Art. 31.1 TUE, párrafo segundo.", "al menos un tercio de los Estados miembros que reúnen como mínimo un tercio de la población de la Unión")
Q("TUE", tf(31), "PESC", "Según el artículo 31.4 del TUE, la adopción de decisiones por mayoría cualificada no se aplicará a las decisiones que tengan repercusiones en el ámbito:",
  ["Militar o de la defensa.", "Comercial.", "De la cooperación al desarrollo.", "De la ayuda humanitaria."],
  "Art. 31.4 TUE.", "no se aplicarán a las decisiones que tengan repercusiones en el ámbito militar o de la defensa")
Q("TUE", tf(46), "PESC", "Según el artículo 46.2 del TUE, el Consejo adoptará la decisión por la que se establezca la cooperación estructurada permanente en un plazo de:",
  ["Tres meses a partir de la notificación.", "Seis meses a partir de la notificación.", "Un mes a partir de la notificación.", "Un año a partir de la notificación."],
  "Art. 46.2 TUE.", "En un plazo de tres meses a partir de la notificación mencionada en el apartado 1")
Q(TF, tf(67), "ELSJ", "Según el artículo 67.2 del TFUE, a efectos del título del espacio de libertad, seguridad y justicia, los apátridas:",
  ["Se asimilarán a los nacionales de terceros países.", "Se asimilarán a los ciudadanos de la Unión.", "Quedan excluidos de su ámbito de aplicación.", "Se asimilarán a los refugiados."],
  "Art. 67.2 TFUE.", "los apátridas se asimilarán a los nacionales de terceros países")
Q(TF, tf(68), "ELSJ", "Según el artículo 68 del TFUE, las orientaciones estratégicas de la programación legislativa y operativa en el espacio de libertad, seguridad y justicia las definirá:",
  ["El Consejo Europeo.", "El Consejo.", "La Comisión.", "El Parlamento Europeo."],
  "Art. 68 TFUE.", "El Consejo Europeo definirá las orientaciones estratégicas de la programación legislativa y operativa")
Q(TF, tf(76), "ELSJ", "Según el artículo 76 del TFUE, los actos sobre cooperación judicial en materia penal y cooperación policial se adoptarán a propuesta de la Comisión o por iniciativa de:",
  ["La cuarta parte de los Estados miembros.", "La tercera parte de los Estados miembros.", "Nueve Estados miembros.", "La mayoría de los Estados miembros."],
  "Art. 76 TFUE.", "por iniciativa de la cuarta parte de los Estados miembros")
Q(TF, tf(81), "ELSJ", "Según el artículo 81.3 del TFUE, las medidas relativas al Derecho de familia con repercusión transfronteriza las establecerá el Consejo, con arreglo a un procedimiento legislativo especial:",
  ["Por unanimidad, previa consulta al Parlamento Europeo.", "Por mayoría cualificada, previa aprobación del Parlamento Europeo.", "Por unanimidad, previa aprobación del Parlamento Europeo.", "Por mayoría cualificada, previa consulta al Parlamento Europeo."],
  "Art. 81.3 TFUE.", "El Consejo se pronunciará por unanimidad, previa consulta al Parlamento Europeo")
Q(TF, tf(86), "ELSJ", "Según el artículo 86.1 del TFUE, el Consejo podrá crear una Fiscalía Europea:",
  ["A partir de Eurojust.", "A partir de Europol.", "A partir de la Oficina Europea de Lucha contra el Fraude.", "A partir de la Red Judicial Europea."],
  "Art. 86.1 TFUE.", "una Fiscalía Europea a partir de Eurojust")
Q(TF, tf(86), "ELSJ", "Según el artículo 86.1 del TFUE, para crear la Fiscalía Europea el Consejo se pronunciará:",
  ["Por unanimidad, previa aprobación del Parlamento Europeo.", "Por mayoría cualificada, previa consulta al Parlamento Europeo.", "Por unanimidad, previa consulta al Parlamento Europeo.", "Por mayoría cualificada, con arreglo al procedimiento legislativo ordinario."],
  "Art. 86.1 TFUE.", "El Consejo se pronunciará por unanimidad, previa aprobación del Parlamento Europeo")
Q(TF, tf(88), "ELSJ", "Según el artículo 88.3 del TFUE, la aplicación de medidas coercitivas corresponderá:",
  ["Exclusivamente a las autoridades nacionales competentes.", "A Europol, en colaboración con las autoridades nacionales.", "A Europol y a Eurojust conjuntamente.", "A la Fiscalía Europea."],
  "Art. 88.3 TFUE.", "La aplicación de medidas coercitivas corresponderá exclusivamente a las autoridades nacionales competentes")
Q(TF, tf(101), "Competencia", "Según el artículo 101.2 del TFUE, los acuerdos o decisiones prohibidos por ese artículo serán:",
  ["Nulos de pleno derecho.", "Anulables a instancia de la Comisión.", "Válidos hasta que los declare nulos el Tribunal de Justicia.", "Sancionables, pero válidos."],
  "Art. 101.2 TFUE.", "serán nulos de pleno derecho")
Q(TF, tf(102), "Competencia", "Según el artículo 102 del TFUE, queda prohibida, en la medida en que pueda afectar al comercio entre los Estados miembros:",
  ["La explotación abusiva, por parte de una o más empresas, de una posición dominante.", "La existencia de una posición dominante de una empresa en el mercado interior.", "Cualquier concentración de empresas.", "La fijación de precios por una sola empresa."],
  "Art. 102 TFUE: lo prohibido es el abuso, no la posición dominante.", "la explotación abusiva, por parte de una o más empresas, de una posición dominante")
Q(TF, tf(105), "Competencia", "Según el artículo 105.1 del TFUE, la Comisión investigará los casos de supuesta infracción de los artículos 101 y 102:",
  ["A instancia de un Estado miembro o de oficio.", "Solo a instancia de un Estado miembro.", "Solo a instancia del Consejo.", "Solo a instancia de las empresas perjudicadas."],
  "Art. 105.1 TFUE.", "A instancia de un Estado miembro o de oficio")
Q(TF, tf(107), "Competencia", "Según el artículo 107.2 del TFUE, serán compatibles con el mercado interior:",
  ["Las ayudas destinadas a reparar los perjuicios causados por desastres naturales.", "Las ayudas destinadas a promover la cultura y la conservación del patrimonio.", "Las ayudas para fomentar un proyecto importante de interés común europeo.", "Las ayudas al desarrollo de regiones con un nivel de vida anormalmente bajo."],
  "Art. 107.2 b) TFUE. Las otras tres son del 107.3 («Podrán considerarse compatibles»).", "las ayudas destinadas a reparar los perjuicios causados por desastres naturales")
Q(TF, tf(108), "Competencia", "Según el artículo 108.2 del TFUE, si el Consejo no se pronuncia sobre la petición de un Estado miembro relativa a una ayuda dentro de cierto plazo, decidirá la Comisión. Ese plazo es de:",
  ["Tres meses siguientes a la petición.", "Seis meses siguientes a la petición.", "Un mes siguiente a la petición.", "Dos meses siguientes a la petición."],
  "Art. 108.2 TFUE, párrafo cuarto.", "dentro de los tres meses siguientes a la petición")
Q(TF, tf(3), "Agricultura y pesca", "Según el artículo 3.1 del TFUE, la Unión dispondrá de competencia exclusiva en:",
  ["La conservación de los recursos biológicos marinos dentro de la política pesquera común.", "La agricultura y la pesca.", "La política agrícola común en su conjunto.", "La acuicultura y la pesca continental."],
  "Art. 3.1 d) TFUE; la agricultura y la pesca, en lo demás, son compartidas (art. 4.2 d).", "la conservación de los recursos biológicos marinos dentro de la política pesquera común")
Q(TF, tf(39), "Agricultura y pesca", "Según el artículo 39.1 del TFUE, es objetivo de la política agrícola común:",
  ["Asegurar al consumidor suministros a precios razonables.", "Asegurar al consumidor suministros a precios mínimos.", "Garantizar la autosuficiencia alimentaria de cada Estado miembro.", "Reducir el número de explotaciones agrícolas."],
  "Art. 39.1 e) TFUE.", "asegurar al consumidor suministros a precios razonables")
Q(TF, tf(43), "Agricultura y pesca", "Según el artículo 43.3 del TFUE, las medidas relativas a la fijación y el reparto de las posibilidades de pesca las adoptará:",
  ["El Consejo, a propuesta de la Comisión.", "El Parlamento Europeo y el Consejo, con arreglo al procedimiento legislativo ordinario.", "La Comisión, previa consulta al Comité Económico y Social.", "Cada Estado miembro en sus aguas territoriales."],
  "Art. 43.3 TFUE.", "El Consejo, a propuesta de la Comisión, adoptará las medidas relativas a la fijación de los precios")
Q("FEMPA", tf(1), "Agricultura y pesca", "Según el artículo 1 del Reglamento (UE) 2021/1139, el FEMPA se establece para el período comprendido entre:",
  ["El 1 de enero de 2021 y el 31 de diciembre de 2027.", "El 1 de enero de 2020 y el 31 de diciembre de 2026.", "El 1 de julio de 2021 y el 30 de junio de 2028.", "El 1 de enero de 2014 y el 31 de diciembre de 2020."],
  "Art. 1 del Reglamento FEMPA.", "entre el 1 de enero de 2021 y el 31 de diciembre de 2027")

T.real("P", 18, "Mercado interior"); T.real("P", 15, "Mercado interior"); T.real("P", 19, "UEM"); T.real("L", 17, "UEM")
T.real("X", 37, "UEM"); T.real("L", 30, "UEM"); T.real("L", 29, "ELSJ"); T.real("L", 102, "Agricultura y pesca")

# Flashcards
for q_, a_, cat in [
  ("¿Qué implica el mercado interior? (art. 26.2 TFUE)", "Un espacio sin fronteras interiores con libre circulación de mercancías, personas, servicios y capitales.", "Mercado interior"),
  ("Unión aduanera y mercado interior: ¿qué tipo de competencia?", "Unión aduanera: exclusiva (3.1 a). Mercado interior: compartida (4.2 a).", "Mercado interior"),
  ("Razones del art. 36 TFUE", "Orden público, moralidad y seguridad públicas; salud y vida de personas y animales; vegetales; patrimonio artístico, histórico o arqueológico; propiedad industrial y comercial. Sin discriminación arbitraria ni restricción encubierta.", "Mercado interior"),
  ("Libre circulación de trabajadores y administración pública (art. 45.4)", "Las disposiciones del art. 45 no se aplican a los empleos en la administración pública.", "Mercado interior"),
  ("Liberalización de un servicio (art. 59.1)", "Directivas del Parlamento Europeo y del Consejo; procedimiento legislativo ordinario; consulta previa al Comité Económico y Social.", "Mercado interior"),
  ("Objetivo primordial de la política monetaria (arts. 119.2 y 127.1)", "Mantener la estabilidad de precios.", "UEM"),
  ("Principios rectores de la UEM (art. 119.3)", "Precios estables, finanzas públicas y condiciones monetarias sólidas y balanza de pagos estable.", "UEM"),
  ("Valores de referencia del déficit excesivo (Protocolo n.º 12)", "Déficit: 3 % del PIB. Deuda: 60 % del PIB.", "UEM"),
  ("Criterios de convergencia (art. 140 y Protocolo n.º 13)", "Inflación: no más de 1½ punto sobre los tres mejores. Sin decisión de déficit excesivo. Dos años en el mecanismo de cambios sin devaluar. Interés a largo plazo: no más de 2 puntos.", "UEM"),
  ("Billetes y monedas en euros (art. 128)", "Billetes: autorización exclusiva del BCE. Monedas: las emiten los Estados con aprobación del BCE del volumen.", "UEM"),
  ("¿Qué Estado tiene excepción al euro por protocolo?", "Dinamarca (Protocolo n.º 16): la derogación solo se inicia a petición suya.", "UEM"),
  ("¿Quién no firmó el Tratado de Estabilidad (2012)?", "No están en el acta de la firma la República Checa ni el Reino Unido (firmaron 25 Estados).", "UEM"),
  ("Reglas básicas de la PESC (art. 24.1 TUE)", "Unanimidad salvo disposición en contrario; sin actos legislativos; TJUE sin competencia salvo art. 40 TUE y art. 275 TFUE.", "PESC"),
  ("Abstención con declaración formal (art. 31.1 TUE)", "Quien se abstiene con declaración formal no aplica la decisión, pero la acepta como vinculante. Bloquea si suman un tercio de Estados con un tercio de la población.", "PESC"),
  ("Ayuda y asistencia ante una agresión armada (art. 42.7 TUE)", "Agresión armada en el territorio de un Estado: los demás le deben ayuda y asistencia con todos los medios a su alcance (art. 51 de la Carta de la ONU).", "PESC"),
  ("Base de la cooperación judicial penal (art. 82.1 TFUE)", "El principio de reconocimiento mutuo de las sentencias y resoluciones judiciales.", "ELSJ"),
  ("Fiscalía Europea (art. 86 TFUE)", "La crea el Consejo a partir de Eurojust, por unanimidad y con aprobación del Parlamento Europeo; persigue infracciones contra los intereses financieros de la Unión.", "ELSJ"),
  ("Arts. 101 y 102 TFUE", "101: acuerdos, decisiones y prácticas concertadas restrictivos, nulos de pleno derecho. 102: explotación abusiva de una posición dominante.", "Competencia"),
  ("Ayudas de Estado: 107.2 y 107.3", "107.2: «Serán» compatibles (sociales a consumidores, desastres naturales, división de Alemania). 107.3: «Podrán considerarse» compatibles.", "Competencia"),
  ("Objetivos de la PAC (art. 39.1)", "Productividad; nivel de vida equitativo de la población agrícola; estabilizar mercados; seguridad de abastecimientos; precios razonables al consumidor.", "Agricultura y pesca"),
  ("¿Quién fija y reparte las posibilidades de pesca? (art. 43.3)", "El Consejo, a propuesta de la Comisión.", "Agricultura y pesca"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Mercado interior", "Espacio sin fronteras interiores en el que está garantizada la libre circulación de mercancías, personas, servicios y capitales (art. 26.2 TFUE).", "s1", "Mercado interior")
T.glos("Unión aduanera", "Prohibición de derechos de aduana y exacciones de efecto equivalente entre Estados miembros y arancel aduanero común frente a terceros países (art. 28 TFUE).", "s2", "Mercado interior")
T.glos("Medida de efecto equivalente", "Medida que, sin ser una restricción cuantitativa, está prohibida como ella entre los Estados miembros (arts. 34 y 35 TFUE).", "s2", "Mercado interior")
T.glos("Estado miembro acogido a una excepción", "Estado sobre el que el Consejo no ha decidido que cumple las condiciones para adoptar el euro (art. 139.1 TFUE).", "s11", "UEM")
T.glos("Criterios de convergencia", "Condiciones para adoptar el euro: estabilidad de precios, finanzas públicas sin déficit excesivo, tipo de cambio y tipos de interés a largo plazo (art. 140.1 TFUE y Protocolo n.º 13).", "s11", "UEM")
T.glos("Déficit excesivo", "Situación declarada por el Consejo cuando un Estado incumple los criterios de déficit (3 % del PIB) o deuda (60 %) (art. 126 TFUE y Protocolo n.º 12).", "s9", "UEM")
T.glos("Cumbre del Euro", "Reunión informal de los Jefes de Estado o de Gobierno de las Partes del euro con el Presidente de la Comisión, al menos dos veces al año (TECG, art. 12).", "s12", "UEM")
T.glos("Abstención con declaración formal", "Abstención en la PESC: el Estado no aplica la decisión, pero admite que vincula a la Unión (art. 31.1 TUE).", "s16", "PESC")
T.glos("Cooperación estructurada permanente", "Cooperación en defensa de los Estados con criterios más elevados de capacidades militares; la establece el Consejo por mayoría cualificada (arts. 42.6 y 46 TUE).", "s17", "PESC")
T.glos("Reconocimiento mutuo", "Principio en que se basa la cooperación judicial civil (resoluciones judiciales y extrajudiciales) y penal (sentencias y resoluciones judiciales) (arts. 81.1 y 82.1 TFUE).", "s20", "ELSJ")
T.glos("Fiscalía Europea", "Órgano creado por el Consejo a partir de Eurojust para perseguir las infracciones que perjudiquen a los intereses financieros de la Unión (art. 86 TFUE).", "s21", "ELSJ")
T.glos("Posición dominante", "Situación de una o más empresas en el mercado interior o en una parte sustancial de él; se prohíbe su explotación abusiva (art. 102 TFUE).", "s22", "Competencia")
T.glos("Ayuda de Estado", "Ayuda otorgada por un Estado o mediante fondos estatales que falsea o amenaza falsear la competencia favoreciendo a determinadas empresas o producciones (art. 107.1 TFUE).", "s24", "Competencia")
T.glos("Organización común de mercados", "Instrumento de la PAC: normas comunes de competencia, coordinación obligatoria de organizaciones nacionales u organización europea del mercado (art. 40 TFUE).", "s27", "Agricultura y pesca")

# Cronología (fechas de los textos y de los metadatos del BOE)
T.hito("1993", "Dinamarca notifica al Consejo, el 3-11-1993, que no participará en la tercera fase de la UEM (Protocolo n.º 16)", "Base de su excepción al euro", "normativo", "s11")
T.hito("2012", "Firma del Tratado de Estabilidad, Coordinación y Gobernanza en Bruselas (2-3-2012)", "25 Estados firmantes; pacto presupuestario y Cumbre del Euro", "normativo", "s12")
T.hito("2013", "Publicación en el BOE del instrumento de ratificación de España del TECG (BOE de 2-2-2013, BOE-A-2013-1118)", "Autorizado por la LO 3/2012, de 25 de julio (art. 93 CE)", "normativo", "s12")
T.hito("2016", "Versiones consolidadas del TUE y del TFUE (DOUE C 202 de 7-6-2016)", "Texto de los Tratados citado en estos apuntes", "normativo", "s0")
T.hito("2021", "Reglamento (UE) 2021/1139, de 7 de julio de 2021, del FEMPA", "Fondo para el período 2021-2027", "normativo", "s28")

T.publicar()
