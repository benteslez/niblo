# -*- coding: utf-8 -*-
"""Tema II.5 (B2T05): El presupuesto comunitario. Los fondos europeos. La cohesión
económica y social.
Método del I.2: mapa → bloques (I a VI) con guía; cada artículo, texto literal (EUR-Lex,
etiqueta DOUE) + ficha de casillas fijas; cierre 1 (preguntas oficiales) y cierre 2 (repaso).
Normas: TUE (art. 3.3) y TFUE (arts. 3, 4, 162 a 164, 174 a 178 y 310 a 325), versión
consolidada de 2016; y, en su versión consolidada de EUR-Lex: Reglamento (UE, Euratom)
2020/2093 (MFP, a 24.4.2026), Decisión (UE, Euratom) 2020/2053 (recursos propios),
Reglamentos (UE) 2021/1060 (disposiciones comunes), 2021/1058 (FEDER y FC), 2021/1057
(FSE+), 2021/2116 (financiación de la PAC), 2021/241 (MRR) y 2021/695 (Horizonte
Europa); Reglamento (UE) 2021/1139 (FEMPA, texto del DO)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO.update({
  "MFPC": "Reglamento (UE, Euratom) 2020/2093, del MFP",
  "DRP": "Decisión (UE, Euratom) 2020/2053, de recursos propios",
  "RDC": "Reglamento (UE) 2021/1060, de disposiciones comunes",
  "FEDERFC": "Reglamento (UE) 2021/1058, del FEDER y del Fondo de Cohesión",
  "FSEP": "Reglamento (UE) 2021/1057, del FSE+",
  "PAC2116": "Reglamento (UE) 2021/2116, de financiación de la PAC",
  "HEUR": "Reglamento (UE) 2021/695, Horizonte Europa",
  "MRR": "Reglamento (UE) 2021/241, del Mecanismo de Recuperación y Resiliencia",
  "FEMPA": "Reglamento (UE) 2021/1139, del FEMPA"})

T = Tema("B2T05",
  "Seis preguntas: I. Qué es el presupuesto de la Unión y qué reglas lo rigen (TFUE, arts. 310, 313, 316 y 320) · II. Con qué se financia: los recursos propios (art. 311 y Decisión 2020/2053) · III. Qué es el marco financiero plurianual (art. 312 y Reglamento 2020/2093) · IV. Cómo se aprueba, ejecuta y controla (arts. 314, 315, 317 a 319, 322, 324 y 325) · V. Qué son los fondos europeos (FSE+, FEDER, Fondo de Cohesión, FEAGA, Feader, FEMPA, MRR y Horizonte Europa) · VI. Qué es la cohesión económica, social y territorial (TUE, art. 3.3; TFUE, arts. 4.2 c) y 174 a 178; Reglamento 2021/1060). Cada artículo: texto literal (EUR-Lex) y ficha.",
  ["Presupuesto de la UE", "Arts. 310-325 TFUE", "Recursos propios", "Decisión 2020/2053", "Marco financiero plurianual", "MFP 2021-2027", "Procedimiento presupuestario", "Comité de Conciliación", "Aprobación de la gestión", "Fondos europeos", "FEDER", "Fondo de Cohesión", "FSE+", "Feader", "FEMPA", "MRR", "Cohesión", "Arts. 174-178 TFUE"])

# =============================================================================
T.ap("s0", "Mapa del tema: seis preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque II, tema 5):
> El presupuesto comunitario. Los fondos europeos. La cohesión económica y social.

### El hilo conductor

El epígrafe se lee como **seis preguntas encadenadas** (cuatro sobre el presupuesto, una sobre los fondos y una sobre la cohesión). Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Tratados | Otras normas (EUR-Lex) |
|---|---|---|---|
| **I** | ¿Qué es el presupuesto de la Unión y qué reglas lo rigen? | TFUE, arts. 310, 313, 316 y 320 | — |
| **II** | ¿Con qué se financia? Los recursos propios | TFUE, art. 311 | Decisión (UE, Euratom) 2020/2053, arts. 2 a 5, 7 y 9 |
| **III** | ¿Qué es el marco financiero plurianual? | TFUE, art. 312 | Reglamento (UE, Euratom) 2020/2093, arts. 1, 2, 13 y 21 |
| **IV** | ¿Cómo se aprueba, se ejecuta y se controla? | TFUE, arts. 314, 315, 317 a 319, 322, 324 y 325 | — |
| **V** | ¿Qué son los fondos europeos? | TFUE, arts. 162 a 164 | Reglamentos (UE) 2021/1060, 2021/1058, 2021/1057, 2021/2116, 2021/1139, 2021/241 y 2021/695 |
| **VI** | ¿Qué es la cohesión económica, social y territorial? | TUE, art. 3.3; TFUE, arts. 4.2 c) y 174 a 178 | Reglamento (UE) 2021/1060, arts. 5.2 y 108 |

!> **La idea que une los seis bloques:** la Unión tiene un **presupuesto anual** (I) que se financia **íntegramente con recursos propios** (II) y que debe respetar un **marco financiero plurianual** (III). El Parlamento Europeo y el Consejo lo **aprueban**, la Comisión lo **ejecuta** y el Parlamento **aprueba su gestión** (IV). Buena parte del gasto se canaliza mediante **fondos** (V), y los fondos con finalidad estructural sirven a la **cohesión económica, social y territorial** (VI).

### Cómo está escrito

- Cada artículo: primero el **texto literal** de EUR-Lex (etiqueta **DOUE**) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Tratados: versión consolidada de 2016 del TUE y del TFUE. Reglamentos y Decisión: **texto consolidado** de EUR-Lex (MFP, a 24.4.2026; Decisión de recursos propios, a 15.12.2020; disposiciones comunes, a 1.7.2026; FEDER y FSE+, a 20.9.2025; PAC, a 18.8.2026; Horizonte Europa, a 24.12.2025; MRR, a 1.3.2024). El FEMPA, según el texto publicado en el Diario Oficial.
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué es el presupuesto de la Unión y qué reglas lo rigen? (TFUE, arts. 310, 313, 316 y 320)", donde(
  "Primera pregunta del tema. Antes de ver de dónde salen los ingresos o cómo se aprueba, hay que saber **qué es** el presupuesto de la Unión y qué **reglas básicas** cumple: el art. 310 TFUE las reúne casi todas.",
  ["1 Unidad, equilibrio, anualidad y legalidad del gasto (arts. 310 y 313)", "2 Créditos por capítulos, partidas separadas y euro (arts. 316 y 320)"]))

T.ap("s1", "I.1 Unidad, equilibrio, anualidad y legalidad del gasto (TFUE, arts. 310 y 313)", f"""
{unidad("1.1 Las reglas del presupuesto (art. 310)",
  lit("TFUE", "Artículo 310", ["Todos los ingresos y gastos de la Unión", "establecerán el presupuesto anual de la Unión con arreglo al artículo 314", "deberá estar equilibrado en cuanto a ingresos y gastos", "para todo el ejercicio presupuestario anual", "la adopción previa de un acto jurídicamente vinculante de la Unión", "dentro del límite de los recursos propios de la Unión y dentro del marco financiero plurianual", "principio de buena gestión financiera", "combatirán el fraude"]),
  fichab("Reglas básicas del presupuesto de la Unión",
         f"{c('TFUE', 'Artículo 310', 'El Parlamento Europeo y el Consejo establecerán el presupuesto anual de la Unión')} (→ IV.1); la Unión y los Estados miembros cooperan en la buena gestión y en la lucha contra el fraude",
         ["Todos los ingresos y gastos, en el presupuesto de cada ejercicio (310.1)", "Presupuesto **equilibrado** en ingresos y gastos (310.1)", "Gastos autorizados para **todo el ejercicio anual** (310.2)", "Ejecutar un gasto exige **antes** un acto jurídicamente vinculante que le dé fundamento (310.3)", "**Disciplina**: no adoptar actos con incidencia considerable sin garantizar su financiación dentro de los recursos propios y del MFP (310.4)", "**Buena gestión financiera** (310.5) y lucha contra el **fraude** (310.6 → IV.3)"],
         "Anual (→ 1.2)",
         "Los gastos se autorizan **para todo el ejercicio presupuestario anual**, no por semestres ni por trimestres (pregunta oficial L 26, → Cierre 1). El presupuesto debe estar **equilibrado**."))}

{unidad("1.2 El ejercicio presupuestario (art. 313)",
  lit("TFUE", "Artículo 313", ["el 1 de enero", "el 31 de diciembre"]),
  fichab("Duración del ejercicio presupuestario", "—", "Coincide con el año natural",
         f"Del {c('TFUE', 'Artículo 313', '1 de enero')} al {c('TFUE', 'Artículo 313', '31 de diciembre')}",
         "Año natural: **1 de enero a 31 de diciembre**."))}
""", 2)

T.ap("s2", "I.2 Créditos por capítulos, partidas separadas y euro (TFUE, arts. 316 y 320)", f"""
{unidad("2.1 Prórroga de créditos, capítulos y partidas separadas (art. 316)",
  lit("TFUE", "Artículo 316", ["que no correspondan a gastos de personal", "sólo podrán ser prorrogados hasta el ejercicio siguiente", "se especificarán por capítulos", "figurarán en partidas separadas del presupuesto"]),
  fichab("Cómo se ordenan los créditos y qué pasa con los no utilizados",
         "—",
         ["Créditos sin utilizar (salvo los de **personal**): solo prorrogables **hasta el ejercicio siguiente**", "Créditos especificados **por capítulos**, según la naturaleza o el destino del gasto", "Gastos del Parlamento Europeo, del Consejo Europeo y del Consejo, de la Comisión y del Tribunal de Justicia: en **partidas separadas**"],
         "Prórroga: solo al ejercicio **siguiente**",
         "Los créditos de **gastos de personal** quedan fuera de la prórroga. La prórroga es **solo** al ejercicio siguiente."))}

{unidad("2.2 El euro (art. 320)",
  lit("TFUE", "Artículo 320", ["se establecerán en euros"]),
  fichab("Moneda del MFP y del presupuesto", "—",
         f"{c('TFUE', 'Artículo 320', 'El marco financiero plurianual y el presupuesto anual se establecerán en euros')}", "—",
         "Sin excepciones para ningún Estado miembro: el distractor «salvo para Hungría y Dinamarca» es falso (pregunta oficial L 26, → Cierre 1)."))}

{resumen([
  "**Todos** los ingresos y gastos, en el presupuesto; presupuesto **equilibrado**; gastos autorizados para **todo el ejercicio anual** (310).",
  "Ejecutar un gasto exige **antes** un **acto jurídicamente vinculante**; **disciplina** dentro de los recursos propios y del MFP; **buena gestión financiera** (310).",
  "Ejercicio: **1 de enero a 31 de diciembre** (313); créditos por **capítulos**; prórroga solo al ejercicio **siguiente** y nunca de los de **personal** (316); todo en **euros** (320)."],
  "Siguiente: II. ¿Con qué se financia? Los recursos propios")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Con qué se financia el presupuesto? Los recursos propios (TFUE, art. 311; Decisión 2020/2053)", donde(
  "Segunda pregunta. El presupuesto debe estar equilibrado (→ I.1); ahora, **de dónde salen los ingresos**: el Tratado dice que de los **recursos propios**, y una **Decisión del Consejo** fija cuáles son y sus límites.",
  ["1 El principio: financiación con recursos propios (art. 311)", "2 La Decisión sobre recursos propios: categorías, límites, empréstitos y recaudación (Decisión 2020/2053)"]))

T.ap("s3", "II.1 El principio: financiación íntegra con recursos propios (TFUE, art. 311)", f"""
{unidad("1.1 Recursos propios y Decisión del Consejo (art. 311)",
  lit("TFUE", "Artículo 311", ["el presupuesto será financiado íntegramente con cargo a los recursos propios", "por unanimidad y previa consulta al Parlamento Europeo", "aprobada por los Estados miembros, de conformidad con sus respectivas normas constitucionales", "previa aprobación del Parlamento Europeo"]),
  fichab("El sistema de recursos propios de la Unión",
         ["Decisión: el **Consejo**, por **unanimidad**, previa **consulta** al Parlamento Europeo; después, **aprobación por los Estados miembros**", "Medidas de ejecución: el **Consejo**, por reglamentos, previa **aprobación** del Parlamento Europeo"],
         ["Presupuesto financiado **íntegramente** con recursos propios, sin perjuicio de otros ingresos", "La Decisión puede crear **nuevas categorías** de recursos propios o **suprimir** una existente"],
         "Decisión: procedimiento legislativo **especial**, **unanimidad** del Consejo y **consulta** al Parlamento; entra en vigor cuando la aprueban **todos** los Estados miembros según sus normas constitucionales",
         "Decisión de recursos propios: Parlamento **consultado**. Reglamentos de ejecución: Parlamento que **aprueba**. No confundir."))}
""", 2)

T.ap("s4", "II.2 La Decisión sobre recursos propios (Decisión (UE, Euratom) 2020/2053)", f"""
La Decisión vigente es la **2020/2053**, adoptada conforme al art. 311 TFUE (→ II.1).

{unidad("2.1 Categorías de recursos propios (art. 2.1)",
  lit("DRP", "Artículo 2", ["los recursos propios tradicionales", "del 0,30 %", "residuos de envases de plástico generados en cada Estado miembro que no se reciclen", "0,80 EUR por kilogramo", "a la suma de la RNB de todos los Estados miembros"], solo=[1, 2, 3, 4, 5], titulo="Artículo 2.1 (Decisión (UE, Euratom) 2020/2053) · Categorías de recursos propios"),
  fichab("Los cuatro ingresos que constituyen recursos propios",
         "Los recaudan los Estados miembros (los tradicionales, → 2.4) y los ponen a disposición de la Comisión",
         ["a) **Tradicionales**: derechos de aduana y exacciones en los intercambios con terceros países, cotizaciones del azúcar", "b) **IVA**: tipo uniforme del **0,30 %** sobre la base armonizada (base limitada al **50 % de la RNB**)", "c) **Plástico**: **0,80 EUR por kilogramo** de residuos de envases de plástico no reciclados", "d) **RNB**: tipo uniforme sobre la suma de la RNB, fijado en el procedimiento presupuestario"],
         "—",
         "Cuatro categorías. Los tipos que se preguntan: **0,30 %** (IVA) y **0,80 EUR/kg** (plástico). El recurso RNB es el que **cierra** el presupuesto: su tipo se fija teniendo en cuenta **todos los demás ingresos**."))}

{unidad("2.2 Límites máximos (art. 3.1 y 2)",
  lit("DRP", "Artículo 3", ["no rebasará el 1,40 %", "no rebasará el 1,46 %"], solo=[1, 2], titulo="Artículo 3.1 y 2 (Decisión (UE, Euratom) 2020/2053) · Límites máximos de los recursos propios"),
  fichab("Techo de los recursos propios", "—",
         ["Recursos para **créditos de pago** anuales: máximo **1,40 %** de la suma de la RNB", "**Créditos de compromiso** anuales: máximo **1,46 %** de la suma de la RNB"],
         "—",
         "**1,40 %** para pagos; **1,46 %** para compromisos. El MFP debe respetar este techo (→ III.2)."))}

{unidad("2.3 Empréstitos: regla y excepción por la COVID-19 (arts. 4 y 5.1)",
  lit("DRP", "Artículo 4", ["no utilizará empréstitos contraídos en mercados de capitales para financiar gastos operativos"], titulo="Artículo 4 (Decisión (UE, Euratom) 2020/2053) · Utilización de los empréstitos contraídos en mercados de capitales"),
  lit("DRP", "Artículo 5", ["por un máximo de hasta 750 000 millones EUR a precios de 2018", "un máximo de 360 000 millones EUR", "un máximo de 390 000 millones EUR", "después de 2026"], solo=[1, 2, 3, 5], titulo="Artículo 5.1 (Decisión (UE, Euratom) 2020/2053) · Medios complementarios extraordinarios y temporales para la crisis de la COVID-19"),
  fichab("Prohibición de endeudarse para gastos operativos y su excepción temporal",
         f"{c('DRP', 'Artículo 5', 'la Comisión estará facultada para contraer empréstitos en mercados de capitales en nombre de la Unión')}",
         ["Regla: **no** se financian **gastos operativos** con empréstitos (art. 4)", f"Excepción, {c('DRP', 'Artículo 5', 'Con el único propósito de hacer frente a las consecuencias de la crisis ocasionada por la COVID-19')}: empréstitos para préstamos y para gastos"],
         ["Hasta **750 000 millones EUR** (precios de 2018)", "Para préstamos: hasta **360 000 millones**", "Para gastos: hasta **390 000 millones**", "Sin endeudamiento neto nuevo **después de 2026**"],
         f"Los pasivos deben reembolsarse {c('DRP', 'Artículo 5', 'a más tardar el 31 de diciembre de 2058')}. La excepción es **única y temporal** y está ligada a la COVID-19 (financia, entre otros, el MRR → V.5)."))}

{unidad("2.4 Universalidad y gastos de recaudación (art. 7 y art. 9.1 y 2)",
  lit("DRP", "Artículo 7", ["se utilizarán indistintamente"], titulo="Artículo 7 (Decisión (UE, Euratom) 2020/2053) · Principio de universalidad"),
  lit("DRP", "Artículo 9", ["serán recaudados por los Estados miembros", "el 25 %"], solo=[1, 3], titulo="Artículo 9.1 y 2 (Decisión (UE, Euratom) 2020/2053) · Recaudación de los recursos propios"),
  fichab("Destino de los ingresos y quién los recauda",
         "Los **Estados miembros** recaudan los recursos propios tradicionales con sus propias normas",
         ["**Universalidad**: los ingresos financian **indistintamente** todos los gastos del presupuesto (art. 7)", "Los Estados retienen un porcentaje de los tradicionales como gastos de recaudación (art. 9.2)"],
         "Gastos de recaudación: **25 %** de los recursos propios tradicionales",
         "Los Estados **retienen el 25 %** de los recursos propios **tradicionales** (no de todos los recursos)."))}

{resumen([
  "El presupuesto se financia **íntegramente** con **recursos propios** (311); la Decisión la adopta el **Consejo por unanimidad**, previa **consulta** al Parlamento, y la **aprueban los Estados miembros**.",
  "Cuatro recursos (Decisión 2020/2053): **tradicionales**, **IVA (0,30 %)**, **plástico no reciclado (0,80 EUR/kg)** y **RNB**.",
  "Techo: **1,40 %** de la RNB (pagos) y **1,46 %** (compromisos); sin empréstitos para gastos operativos, salvo la excepción **COVID-19** (hasta **750 000 millones**).",
  "**Universalidad** (art. 7); los Estados retienen el **25 %** de los tradicionales (art. 9.2)."],
  "Siguiente: III. ¿Qué es el marco financiero plurianual?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Qué es el marco financiero plurianual? (TFUE, art. 312; Reglamento 2020/2093)", donde(
  "Tercera pregunta. El presupuesto es **anual**, pero se encaja en un marco **plurianual** que fija los **límites máximos** de gasto por categorías durante varios años.",
  ["1 El MFP en el Tratado (art. 312)", "2 El MFP 2021-2027 (Reglamento (UE, Euratom) 2020/2093)"]))

T.ap("s5", "III.1 El marco financiero plurianual en el Tratado (TFUE, art. 312)", f"""
{unidad("1.1 Objeto, duración, adopción y prórroga (art. 312)",
  lit("TFUE", "Artículo 312", ["garantizar la evolución ordenada de los gastos de la Unión dentro del límite de sus recursos propios", "Se establecerá para un período mínimo de cinco años", "El Consejo se pronunciará por unanimidad, previa aprobación del Parlamento Europeo, que se pronunciará por mayoría de los miembros que lo componen", "pronunciarse por mayoría cualificada", "límites máximos anuales de créditos para compromisos, por categoría de gastos, y del límite máximo anual de créditos para pagos", "se prorrogarán los límites máximos y las demás disposiciones correspondientes al último año de aquél"]),
  fichab("Marco de gasto plurianual al que se somete el presupuesto anual",
         ["Lo adopta el **Consejo** mediante **reglamento**, por procedimiento legislativo **especial**", "Previa **aprobación** del **Parlamento Europeo**", "El **Consejo Europeo** puede permitir, por unanimidad, la mayoría cualificada en el Consejo"],
         ["Objeto: evolución ordenada de los gastos **dentro del límite de los recursos propios**", "Fija los **límites máximos anuales** de créditos para **compromisos por categoría** de gastos y el de créditos para **pagos**", "El presupuesto anual **respeta** el MFP"],
         ["Duración: **mínimo cinco años**", "Consejo: **unanimidad** (o mayoría cualificada si lo permite el Consejo Europeo)", "Parlamento: **mayoría de los miembros que lo componen**", "Si no hay nuevo MFP al vencer el anterior: **prórroga** de los límites del **último año**"],
         "Período mínimo de **cinco** años (no cuatro: pregunta oficial X 35, → Cierre 1). El Parlamento **aprueba** (no solo es consultado)."))}
""", 2)

T.ap("s6", "III.2 El MFP 2021-2027 (Reglamento (UE, Euratom) 2020/2093)", f"""
{unidad("2.1 Período y respeto de los límites (arts. 1 y 2.1)",
  lit("MFPC", "Artículo 1", ["para los ejercicios 2021 a 2027"], titulo="Artículo 1 (Reglamento (UE, Euratom) 2020/2093) · Marco financiero plurianual"),
  lit("MFPC", "Artículo 2", ["respetarán", "los límites máximos anuales de gasto establecidos en el anexo I"], solo=[1], titulo="Artículo 2.1 (Reglamento (UE, Euratom) 2020/2093) · Cumplimiento de los límites máximos del MFP"),
  fichab("El MFP vigente",
         "El Parlamento Europeo, el Consejo y la Comisión («instituciones»)",
         "Respetan los límites máximos anuales de gasto del **anexo I** durante cada procedimiento presupuestario y durante la ejecución",
         "Ejercicios **2021 a 2027** (siete años)",
         "El MFP vigente abarca **2021-2027** (pregunta oficial X 35, → Cierre 1). Siete años: por encima del mínimo de cinco del art. 312 TFUE."))}

{unidad("2.2 Revisión del MFP y transición (arts. 13.1 y 21)",
  lit("MFPC", "Artículo 13", ["en caso de imprevistos", "respetando el límite máximo de los recursos propios"], solo=[1], titulo="Artículo 13.1 (Reglamento (UE, Euratom) 2020/2093) · Revisión del MFP"),
  lit("MFPC", "Artículo 21", ["Antes del 1 de julio de 2025"], titulo="Artículo 21 (Reglamento (UE, Euratom) 2020/2093) · Transición al próximo MFP"),
  fichab("Cambios del MFP y propuesta del siguiente",
         "La Comisión (propuesta del nuevo MFP)",
         ["Revisión **en caso de imprevistos**, respetando el techo de recursos propios (13.1)", "Otras revisiones: por ejecución (14), revisión de los Tratados (15), ampliación (16) y reunificación de Chipre (17)"],
         f"Propuesta de nuevo MFP: {c('MFPC', 'Artículo 21', 'Antes del 1 de julio de 2025')}",
         "Toda revisión respeta el **límite máximo de los recursos propios** (→ II.2.2)."))}

{resumen([
  "MFP: evolución ordenada del gasto **dentro de los recursos propios**; **mínimo cinco años**; el presupuesto anual lo **respeta** (312).",
  "Lo adopta el **Consejo por unanimidad** mediante reglamento, previa **aprobación** del Parlamento (**mayoría de sus miembros**); si no se adopta a tiempo, se **prorrogan** los límites del último año.",
  "MFP vigente: **2021 a 2027** (Reglamento 2020/2093); límites del **anexo I**; revisable en caso de **imprevistos**."],
  "Siguiente: IV. ¿Cómo se aprueba, se ejecuta y se controla el presupuesto?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Cómo se aprueba, se ejecuta y se controla el presupuesto? (TFUE, arts. 314, 315, 317 a 319, 322, 324 y 325)", donde(
  "Cuarta pregunta. Ya sabemos qué es el presupuesto, cómo se financia y qué marco respeta. Ahora, el **ciclo**: quién lo **aprueba** y con qué plazos, quién lo **ejecuta** y quién **controla** esa ejecución.",
  ["1 Aprobación: el procedimiento presupuestario y las doceavas partes (arts. 314 y 315)", "2 Ejecución, cuentas y aprobación de la gestión (arts. 317 a 319)", "3 Normas financieras, concertación y lucha contra el fraude (arts. 322, 324 y 325)"]))

T.ap("s7", "IV.1 Aprobación: el procedimiento presupuestario (TFUE, arts. 314 y 315)", f"""
{unidad("1.1 El procedimiento presupuestario anual (art. 314)",
  lit("TFUE", "Artículo 314", ["con arreglo a un procedimiento legislativo especial", "excepto el Banco Central Europeo", "antes del 1 de julio", "a más tardar el 1 de septiembre", "a más tardar el 1 de octubre", "en un plazo de cuarenta y dos días", "convocará sin demora al Comité de Conciliación", "en un plazo de veintiún días", "de catorce días", "tres quintas partes de los votos emitidos", "el Presidente del Parlamento Europeo declarará que el presupuesto ha quedado definitivamente adoptado"], solo=[1, 2, 3, 4, 5, 9, 10, 11, 16, 17, 18]),
  fichab("Procedimiento para aprobar el presupuesto anual",
         ["Lo establecen el **Parlamento Europeo** y el **Consejo**", "Cada institución (salvo el **BCE**) hace su estado de previsiones; la **Comisión** presenta el proyecto", "Comité de Conciliación: miembros del Consejo y **igual número** de representantes del Parlamento; la Comisión participa", "Declara la adopción definitiva el **Presidente del Parlamento Europeo**"],
         ["Previsiones → proyecto de la Comisión → posición del Consejo → lectura del Parlamento", "Parlamento: **aprueba** la posición del Consejo o **no se pronuncia** → presupuesto adoptado; **enmienda** → Comité de Conciliación (salvo que el Consejo acepte todas las enmiendas en **10 días**)", "Sin acuerdo en conciliación, o texto rechazado: **nuevo proyecto** de la Comisión"],
         ["Previsiones de gastos: **antes del 1 de julio**", "Proyecto de la Comisión: **a más tardar el 1 de septiembre** del año anterior", "Posición del Consejo: **a más tardar el 1 de octubre**", "Parlamento: **42 días**; enmiendas por **mayoría de los miembros que lo componen**", "Comité de Conciliación: **21 días**; mayoría cualificada (Consejo) y mayoría (representantes del Parlamento)", "Aprobación del texto conjunto: **14 días**", "Confirmación de enmiendas si el Consejo rechaza: **mayoría de los miembros y tres quintas partes de los votos emitidos**"],
         "Procedimiento legislativo **especial** (no ordinario). Las previsiones las hace **cada institución excepto el BCE** (pregunta oficial X 35, → Cierre 1). Plazos: **1 julio · 1 septiembre · 1 octubre · 42 · 21 · 14** días."))}

{unidad("1.2 Si no hay presupuesto al empezar el año: las doceavas partes (art. 315)",
  lit("TFUE", "Artículo 315", ["mensualmente por capítulos", "dentro del límite de la doceava parte de los créditos consignados en el capítulo correspondiente del presupuesto del ejercicio precedente", "a los treinta días de su adopción", "por mayoría de los miembros que lo componen, reducir los gastos"]),
  fichab("Régimen provisional de gasto sin presupuesto adoptado",
         "El **Consejo**, a propuesta de la Comisión, puede autorizar más de la doceava parte; el **Parlamento Europeo** puede reducir los gastos",
         ["Gastos **mensuales por capítulos**, hasta **1/12** de los créditos del ejercicio **precedente** (sin superar 1/12 de los del proyecto)", "El Consejo puede autorizar más de la doceava parte y lo comunica inmediatamente al Parlamento"],
         ["La decisión del Consejo entra en vigor a los **30 días**", "El Parlamento puede reducir los gastos por **mayoría de los miembros que lo componen**"],
         "Límite: **doceava parte** del ejercicio **precedente**, por **capítulos** y **mensualmente**."))}
""", 2)

T.ap("s8", "IV.2 Ejecución, cuentas y aprobación de la gestión (TFUE, arts. 317 a 319)", f"""
{unidad("2.1 La Comisión ejecuta el presupuesto (art. 317)",
  lit("TFUE", "Artículo 317", ["La Comisión, bajo su propia responsabilidad y dentro del límite de los créditos autorizados, ejecutará el presupuesto en cooperación con los Estados miembros", "la Comisión podrá transferir créditos de capítulo a capítulo o de subdivisión a subdivisión"]),
  fichab("Ejecución del presupuesto",
         f"{c('TFUE', 'Artículo 317', 'La Comisión, bajo su propia responsabilidad')}, en cooperación con los Estados miembros",
         ["Dentro del **límite de los créditos autorizados** y con arreglo al principio de **buena gestión financiera**", "Transferencias de créditos **de capítulo a capítulo** o **de subdivisión a subdivisión**, según el reglamento financiero (art. 322)"],
         "—",
         "Las transferencias de créditos las hace **la Comisión**, no el Parlamento (pregunta oficial L 26, → Cierre 1)."))}

{unidad("2.2 Cuentas e informe de evaluación (art. 318)",
  lit("TFUE", "Artículo 318", ["las cuentas del ejercicio cerrado", "un balance financiero del activo y pasivo de la Unión", "un informe de evaluación de las finanzas de la Unión"]),
  fichab("Rendición de cuentas de la Comisión", "La **Comisión**, ante el Parlamento Europeo y el Consejo",
         ["Cuentas del ejercicio cerrado", "Balance financiero del activo y pasivo", "Informe de evaluación de las finanzas basado en los resultados"],
         "Cada año", "Son los documentos que examina después el Parlamento para aprobar la gestión (→ 2.3)."))}

{unidad("2.3 La aprobación de la gestión de la Comisión (art. 319)",
  lit("TFUE", "Artículo 319", ["El Parlamento Europeo, por recomendación del Consejo, aprobará la gestión de la Comisión en la ejecución del presupuesto", "después del Consejo", "el informe anual del Tribunal de Cuentas", "podrá solicitar explicaciones a la Comisión"]),
  fichab("Control político de la ejecución del presupuesto",
         ["Aprueba la gestión: el **Parlamento Europeo**", "Recomienda: el **Consejo**", "Rinde cuentas: la **Comisión**"],
         ["El Parlamento examina, **después del Consejo**, las cuentas, el balance y el informe del art. 318, el **informe anual del Tribunal de Cuentas** con las respuestas, la declaración de fiabilidad y los informes especiales", "Puede pedir explicaciones a la Comisión; la Comisión da efecto a sus observaciones"],
         "—",
         "**Parlamento** aprueba, **por recomendación del Consejo** (no al revés). Es la respuesta de la pregunta oficial L 26 (→ Cierre 1)."))}
""", 2)

T.ap("s9", "IV.3 Normas financieras, concertación y lucha contra el fraude (TFUE, arts. 322, 324 y 325)", f"""
{unidad("3.1 Normas financieras (art. 322)",
  lit("TFUE", "Artículo 322", ["con arreglo al procedimiento legislativo ordinario y tras consultar al Tribunal de Cuentas", "las normas financieras", "previa consulta al Parlamento Europeo y al Tribunal de Cuentas"]),
  fichab("Reglas financieras de desarrollo",
         ["Normas financieras y control de los agentes financieros: **Parlamento Europeo y Consejo**, por reglamentos", "Puesta a disposición de los recursos propios: el **Consejo**, a propuesta de la Comisión"],
         ["Establecimiento y ejecución del presupuesto, rendición y censura de cuentas (322.1 a)", "Responsabilidad de ordenadores de pagos y contables (322.1 b)", "Modalidades para poner los recursos propios a disposición de la Comisión y necesidades de tesorería (322.2)"],
         ["322.1: procedimiento legislativo **ordinario**, tras consultar al **Tribunal de Cuentas**", "322.2: consulta al Parlamento y al Tribunal de Cuentas"],
         "El reglamento financiero se aprueba por procedimiento legislativo **ordinario** (a diferencia del presupuesto, del MFP y de los recursos propios, que siguen procedimientos **especiales**)."))}

{unidad("3.2 Concertación entre Presidentes (art. 324)",
  lit("TFUE", "Artículo 324", ["Por iniciativa de la Comisión", "reuniones periódicas de los Presidentes del Parlamento Europeo, del Consejo y de la Comisión"]),
  fichab("Diálogo entre instituciones en los procedimientos presupuestarios",
         "Presidentes del **Parlamento Europeo**, del **Consejo** y de la **Comisión**; convoca a iniciativa de la **Comisión**",
         "Reuniones periódicas para propiciar la concertación y el acercamiento de posiciones", "Periódicas",
         "La iniciativa es de la **Comisión**. El Reglamento del MFP desarrolla esta cooperación (art. 19: reuniones tripartitas)."))}

{unidad("3.3 Lucha contra el fraude (art. 325)",
  lit("TFUE", "Artículo 325", ["efecto disuasorio", "las mismas medidas que para combatir el fraude que afecte a sus propios intereses financieros", "con arreglo al procedimiento legislativo ordinario y previa consulta al Tribunal de Cuentas", "presentará anualmente"]),
  fichab("Protección de los intereses financieros de la Unión",
         "La **Unión** y los **Estados miembros**; medidas del **Parlamento Europeo y del Consejo**; informe anual de la **Comisión**",
         ["Medidas disuasorias y eficaces", "**Asimilación**: los Estados combaten el fraude contra la Unión con **las mismas medidas** que el que afecta a sus propios intereses", "Coordinación entre Estados y colaboración con la Comisión"],
         "Procedimiento legislativo **ordinario**, previa consulta al **Tribunal de Cuentas**; informe **anual**",
         "Principio de **asimilación** (325.2). Remite a él el art. 310.6 (→ I.1.1)."))}

{resumen([
  "Aprobación (314): procedimiento legislativo **especial**; previsiones **antes del 1 de julio** (todas las instituciones **salvo el BCE**); proyecto **1 de septiembre**; posición del Consejo **1 de octubre**; Parlamento **42 días**; conciliación **21 días**; texto conjunto **14 días**.",
  "Sin presupuesto el 1 de enero: **doceavas partes** mensuales por capítulos (315).",
  "Ejecuta la **Comisión** (317), que también **transfiere créditos**; rinde cuentas (318); el **Parlamento**, por **recomendación del Consejo**, **aprueba la gestión** (319).",
  "Reglamento financiero y medidas contra el fraude: procedimiento **ordinario**, previa consulta al **Tribunal de Cuentas** (322 y 325)."],
  "Siguiente: V. ¿Qué son los fondos europeos?")}
""", 2)

# =============================================================================
T.ap("bV", "V. ¿Qué son los fondos europeos? (TFUE, arts. 162 a 164; Reglamentos de los fondos 2021-2027)", donde(
  "Quinta pregunta. Buena parte del presupuesto se gasta a través de **fondos**. Los Tratados crean algunos (Fondo Social Europeo, FEDER, Fondo de Cohesión) y los **reglamentos** de 2021 fijan sus objetivos para el período 2021-2027.",
  ["1 El Fondo Social Europeo y el FSE+ (TFUE, arts. 162 a 164; Reglamento 2021/1057)", "2 Las disposiciones comunes de los fondos (Reglamento 2021/1060)", "3 El FEDER y el Fondo de Cohesión (Reglamento 2021/1058)", "4 Fondos agrícolas y de pesca: FEAGA, Feader y FEMPA (Reglamentos 2021/2116 y 2021/1139)", "5 El Mecanismo de Recuperación y Resiliencia y Horizonte Europa (Reglamentos 2021/241 y 2021/695)", "6 Cuadro de los fondos"]))

T.ap("s10", "V.1 El Fondo Social Europeo y el FSE+ (TFUE, arts. 162 a 164; Reglamento (UE) 2021/1057)", f"""
{unidad("1.1 Creación y fines del Fondo Social Europeo (art. 162)",
  lit("TFUE", "Artículo 162", ["Para mejorar las posibilidades de empleo de los trabajadores en el mercado interior", "facilitar su adaptación a las transformaciones industriales"]),
  fichab("Fondo creado por el Tratado para el empleo y la movilidad de los trabajadores", "La Unión",
         ["Mejorar las posibilidades de **empleo** de los trabajadores en el mercado interior", "Fomentar las oportunidades de empleo y la **movilidad geográfica y profesional**", "Facilitar la adaptación a las **transformaciones industriales** y a los cambios de los sistemas de producción, especialmente mediante formación y reconversión profesionales"],
         "—",
         "Mejorar el empleo y adaptarse a las transformaciones industriales son fines del **FSE**, no del Fondo de Cohesión (distractores de la pregunta oficial P 17, → Cierre 1)."))}

{unidad("1.2 Administración y reglamentos de aplicación (arts. 163 y 164)",
  lit("TFUE", "Artículo 163", ["La administración del Fondo corresponderá a la Comisión", "presidido por un miembro de la Comisión"]),
  lit("TFUE", "Artículo 164", ["con arreglo al procedimiento legislativo ordinario"]),
  fichab("Quién administra el FSE y cómo se regula",
         ["Administra: la **Comisión**", "La asiste un **Comité** presidido por un miembro de la Comisión, con representantes de los **Gobiernos**, de los **sindicatos** y de las **asociaciones empresariales**", "Reglamentos de aplicación: **Parlamento Europeo y Consejo**"],
         "—",
         "Reglamentos: procedimiento legislativo **ordinario**, previa consulta al **Comité Económico y Social** y al **Comité de las Regiones**",
         "Comité **tripartito** (Gobiernos, sindicatos, empresarios) presidido por un **miembro de la Comisión**."))}

{unidad("1.3 El Fondo Social Europeo Plus (Reglamento (UE) 2021/1057, arts. 1 y 3.1)",
  lit("FSEP", "Artículo 1", ["Fondo Social Europeo Plus (FSE+)", "dos capítulos"], solo=[1], titulo="Artículo 1 (Reglamento (UE) 2021/1057) · Objeto"),
  lit("FSEP", "Artículo 3", ["elevados niveles de empleo, una protección social justa y una mano de obra capacitada y resiliente", "pilar europeo de derechos sociales"], solo=[1], titulo="Artículo 3.1 (Reglamento (UE) 2021/1057) · Objetivos generales del FSE+"),
  fichab("El FSE en el período 2021-2027", "Estados miembros y regiones (destinatarios del apoyo)",
         ["Dos capítulos: **gestión compartida** y **empleo e innovación social (EaSI)**", "Objetivo: altos niveles de **empleo**, **protección social** justa, mano de obra **capacitada y resiliente**, sociedades inclusivas, erradicar la **pobreza**, principios del **pilar europeo de derechos sociales**"],
         "Período **2021-2027**",
         "El FSE+ tiene **dos** capítulos: el de **gestión compartida** y el **EaSI** (empleo e innovación social)."))}
""", 2)

T.ap("s11", "V.2 Las disposiciones comunes de los fondos (Reglamento (UE) 2021/1060)", f"""
{unidad("2.1 Qué fondos regula (art. 1.1)",
  lit("RDC", "Artículo 1", ["el Fondo Europeo de Desarrollo Regional (FEDER), el Fondo Social Europeo Plus (FSE+), el Fondo de Cohesión, el Fondo de Transición Justa (FTJ), el Fondo Europeo Marítimo, de Pesca y de Acuicultura (FEMPA)", "las disposiciones comunes aplicables al FEDER, al FSE+, al Fondo de Cohesión, al FTJ y al FEMPA"], solo=[1, 2, 3], titulo="Artículo 1.1 (Reglamento (UE) 2021/1060) · Objeto y ámbito de aplicación"),
  fichab("Reglamento de disposiciones comunes (RDC)", "—",
         ["**Normas financieras** para **ocho** fondos: FEDER, FSE+, Fondo de Cohesión, FTJ, FEMPA, FAMI, FSI e IGFV («Fondos»)", "**Disposiciones comunes** para **cinco**: FEDER, FSE+, Fondo de Cohesión, FTJ y FEMPA"],
         "—",
         "El RDC **no** regula el **Feader** ni el **FEAGA** (su financiación está en el Reglamento 2021/2116, → V.4)."))}

{unidad("2.2 Los cinco objetivos políticos (art. 5.1)",
  lit("RDC", "Artículo 5", ["una Europa más competitiva e inteligente", "una Europa más verde", "una Europa más conectada", "una Europa más social e inclusiva", "una Europa más próxima a sus ciudadanos"], solo=[1, 2, 3, 4, 5, 6, 7], titulo="Artículo 5.1 (Reglamento (UE) 2021/1060) · Objetivos políticos"),
  fichab("A qué se destinan el FEDER, el FSE+, el Fondo de Cohesión y el FEMPA", "FEDER, FSE+, Fondo de Cohesión y FEMPA; el FTJ, a su objetivo específico",
         ["a) Europa más **competitiva e inteligente**", "b) Europa más **verde**, baja en carbono", "c) Europa más **conectada**", "d) Europa más **social e inclusiva**", "e) Europa más **próxima a sus ciudadanos**"],
         "—",
         "Son **cinco** objetivos políticos. El **FTJ** tiene un objetivo **específico** propio: afrontar las repercusiones de la transición hacia una economía climáticamente neutra."))}
""", 2)

T.ap("s12", "V.3 El FEDER y el Fondo de Cohesión (Reglamento (UE) 2021/1058)", f"""
Los dos fondos nacen del Tratado (arts. 176 y 177 TFUE, → VI.2) y el Reglamento 2021/1058 concreta sus cometidos.

{unidad("3.1 Cometidos del FEDER y del Fondo de Cohesión (art. 2)",
  lit("FEDERFC", "Artículo 2", ["fortalecer la cohesión económica, social y territorial de la Unión", "reducir las disparidades entre los niveles de desarrollo de las distintas regiones", "proyectos en los sectores del medio ambiente y de las redes transeuropeas en materia de infraestructuras de transporte"], titulo="Artículo 2 (Reglamento (UE) 2021/1058) · Cometidos del FEDER y del Fondo de Cohesión"),
  fichab("Para qué sirven el FEDER y el Fondo de Cohesión", "FEDER y Fondo de Cohesión",
         ["Ambos: fortalecer la **cohesión económica, social y territorial**", "**FEDER**: reducir las **disparidades regionales** y el retraso de las regiones menos favorecidas; ajuste estructural y **reconversión** de regiones industriales en declive", "**Fondo de Cohesión**: proyectos de **medio ambiente** y de **redes transeuropeas** de transporte (RTE-T)"],
         "—",
         "**FEDER = regiones** (desequilibrios regionales). **Fondo de Cohesión = medio ambiente y redes transeuropeas de transporte** (pregunta oficial P 17, → Cierre 1)."))}
""", 2)

T.ap("s13", "V.4 Fondos agrícolas y de pesca: FEAGA, Feader y FEMPA (Reglamentos (UE) 2021/2116 y 2021/1139)", f"""
{unidad("4.1 Los dos fondos agrícolas (Reglamento (UE) 2021/2116, arts. 4, 5.1 y 6)",
  lit("PAC2116", "Artículo 4", ["Fondo Europeo Agrícola de Garantía (FEAGA)", "Fondo Europeo Agrícola de Desarrollo Rural (Feader)"], titulo="Artículo 4 (Reglamento (UE) 2021/2116) · Fondos que financian el gasto agrícola"),
  lit("PAC2116", "Artículo 5", ["bien en régimen de gestión compartida", "bien en régimen de gestión directa"], solo=[1], titulo="Artículo 5.1 (Reglamento (UE) 2021/2116) · Gastos del FEAGA"),
  lit("PAC2116", "Artículo 6", ["en régimen de gestión compartida entre los Estados miembros y la Unión", "intervenciones para el desarrollo rural"], titulo="Artículo 6 (Reglamento (UE) 2021/2116) · Gastos del Feader"),
  fichab("Financiación de la política agrícola común", "FEAGA y Feader, con cargo al presupuesto de la Unión",
         ["**FEAGA** (garantía): gestión **compartida** o **directa**; financia, entre otros, los **pagos directos** y las medidas de mercado (art. 5.2)", "**Feader** (desarrollo rural): solo gestión **compartida**; financia las **intervenciones para el desarrollo rural** de los planes estratégicos de la PAC"],
         "—",
         "**Dos** fondos agrícolas: **FEAGA** (garantía) y **Feader** (desarrollo rural). El Feader se ejecuta **solo** en gestión compartida."))}

{unidad("4.2 El FEMPA (Reglamento (UE) 2021/1139, arts. 1 y 25.1)",
  lit("FEMPA", "Artículo 1", ["entre el 1 de enero de 2021 y el 31 de diciembre de 2027"], titulo="Artículo 1 (Reglamento (UE) 2021/1139) · Objeto"),
  lit("FEMPA", "Artículo 25", ["incluso en las aguas interiores"], solo=[1, 2], titulo="Artículo 25.1 (Reglamento (UE) 2021/1139) · Protección y recuperación de la biodiversidad y los ecosistemas acuáticos"),
  fichab("Fondo Europeo Marítimo, de Pesca y de Acuicultura", "La Unión, con cargo al FEMPA",
         ["Duración ajustada a la del **MFP 2021-2027**", "Puede apoyar la protección y recuperación de la biodiversidad y los ecosistemas acuáticos, **incluso en las aguas interiores** (25.1)"],
         "Del **1 de enero de 2021** al **31 de diciembre de 2027**",
         "«**incluso** en las aguas **interiores**» (no «salvo», ni «aguas fluviales»): pregunta oficial L 102, de reserva (→ Cierre 1)."))}
""", 2)

T.ap("s14", "V.5 El Mecanismo de Recuperación y Resiliencia y Horizonte Europa (Reglamentos (UE) 2021/241 y 2021/695)", f"""
{unidad("5.1 El Mecanismo de Recuperación y Resiliencia (Reglamento (UE) 2021/241, arts. 1, 3 y 4)",
  lit("MRR", "Artículo 1", ["Mecanismo de Recuperación y Resiliencia"], solo=[1], titulo="Artículo 1 (Reglamento (UE) 2021/241) · Objeto"),
  lit("MRR", "Artículo 3", ["seis pilares", "transición ecológica", "transformación digital", "cohesión social y territorial"], titulo="Artículo 3 (Reglamento (UE) 2021/241) · Ámbito de aplicación"),
  lit("MRR", "Artículo 4", ["el objetivo general del Mecanismo será fomentar la cohesión económica, social y territorial de la Unión", "planes de recuperación y resiliencia"], titulo="Artículo 4 (Reglamento (UE) 2021/241) · Objetivo general y objetivos específicos"),
  fichab("Instrumento de ayuda financiera a las reformas e inversiones de los Estados miembros", "Los Estados miembros, según sus **planes de recuperación y resiliencia**",
         ["**Seis pilares**: transición ecológica; transformación digital; crecimiento inteligente, sostenible e integrador; cohesión social y territorial; salud y resiliencia; políticas para la próxima generación", "Objetivo general: fomentar la **cohesión económica, social y territorial**, en el contexto de la crisis de la **COVID-19**", "Objetivo específico: ayuda financiera para alcanzar los **hitos y objetivos** de reformas e inversiones"],
         "—",
         f"**Seis** pilares. Su dinero viene del Instrumento de Recuperación de la UE: {c('MRR', 'Artículo 6', 'Las medidas contempladas en el artículo 1 del Reglamento (UE) 2020/2094 se aplicarán en el marco del Mecanismo')} (art. 6.1), y ese Instrumento se financia con los empréstitos excepcionales de la Decisión de recursos propios, {c('DRP', 'Artículo 5', 'mediante el Reglamento del Consejo por el que se establece un Instrumento de Recuperación de la Unión Europea')} (art. 5.1, → II.2.3)."))}

{unidad("5.2 Horizonte Europa (Reglamento (UE) 2021/695, art. 1.1)",
  lit("HEUR", "Artículo 1", ["Programa Marco de Investigación e Innovación «Horizonte Europa»", "marco financiero plurianual 2021-2027"], solo=[1, 2], titulo="Artículo 1.1 (Reglamento (UE) 2021/695) · Objeto"),
  fichab("Programa marco de investigación e innovación de la Unión", "La Unión",
         "Establece el programa, sus objetivos, su presupuesto y las normas de participación y difusión",
         "Vigencia del **MFP 2021-2027**",
         "El programa marco de I+i 2021-2027 es **Horizonte Europa** (pregunta oficial L 27, → Cierre 1)."))}
""", 2)

T.ap("s15", "V.6 Cuadro de los fondos (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Fondo | Base | Para qué (según la norma citada) | Gestión |
|---|---|---|---|
| **FSE / FSE+** | TFUE, 162-164; Reglamento 2021/1057 | Empleo, movilidad, adaptación a las transformaciones industriales; protección social, inclusión | Compartida (y capítulo EaSI) |
| **FEDER** | TFUE, 176 y 178; Reglamento 2021/1058 | Corregir los **desequilibrios regionales** | — |
| **Fondo de Cohesión** | TFUE, 177; Reglamento 2021/1058 | Proyectos de **medio ambiente** y **redes transeuropeas** de transporte | — |
| **FTJ** | Reglamento 2021/1060, art. 5.1 | Repercusiones de la transición hacia una economía climáticamente neutra | — |
| **FEAGA** | Reglamento 2021/2116 | Pagos directos y medidas de mercado de la PAC | Compartida o directa |
| **Feader** | Reglamento 2021/2116 | Desarrollo rural | **Solo compartida** |
| **FEMPA** | Reglamento 2021/1139 | Pesca, acuicultura y medio marino | — |
| **MRR** | Reglamento 2021/241 | Reformas e inversiones de los planes de recuperación y resiliencia | — |

{resumen([
  "**FSE**: lo crea el art. 162 para el **empleo** y la **adaptación a las transformaciones industriales**; lo administra la **Comisión** con un Comité tripartito (163). Hoy, **FSE+** (2021/1057).",
  "El **RDC** (2021/1060) da normas financieras a **ocho** fondos y disposiciones comunes a **cinco** (FEDER, FSE+, FC, FTJ, FEMPA), con **cinco objetivos políticos**.",
  "**FEDER**: disparidades **regionales**; **Fondo de Cohesión**: **medio ambiente** y **RTE-T**.",
  "PAC: **FEAGA** y **Feader** (este, solo en gestión compartida); pesca: **FEMPA** (2021-2027).",
  "**MRR**: **seis pilares** y planes de recuperación; **Horizonte Europa**: programa marco de I+i 2021-2027."],
  "Siguiente: VI. ¿Qué es la cohesión económica, social y territorial?")}
""", 2)

# =============================================================================
T.ap("bVI", "VI. ¿Qué es la cohesión económica, social y territorial? (TUE, art. 3.3; TFUE, arts. 4.2 c) y 174 a 178; Reglamento 2021/1060)", donde(
  "Sexta y última pregunta. La cohesión es un **objetivo** de la Unión y una **competencia compartida**. El Título XVIII del TFUE (arts. 174 a 178) dice qué persigue y con qué instrumentos (los fondos del bloque V).",
  ["1 La cohesión como objetivo y como competencia (TUE, art. 3.3; TFUE, arts. 4.2 c) y 174)", "2 Los instrumentos: fondos estructurales, FEDER y Fondo de Cohesión (TFUE, arts. 175 a 178)", "3 Las categorías de regiones (Reglamento (UE) 2021/1060, arts. 5.2 y 108)"]))

T.ap("s16", "VI.1 La cohesión como objetivo y como competencia (TUE, art. 3.3; TFUE, arts. 4.2 c) y 174)", f"""
{unidad("1.1 Objetivo de la Unión (TUE, art. 3.3)",
  lit("TUE", "Artículo 3", ["fomentará la cohesión económica, social y territorial y la solidaridad entre los Estados miembros"], solo=[5], titulo="Artículo 3.3, párrafo tercero (TUE)"),
  fichab("La cohesión entre los objetivos de la Unión", "La Unión",
         "Fomentar la cohesión **económica, social y territorial** y la **solidaridad entre los Estados miembros**", "—",
         "Son **tres** dimensiones: económica, social **y territorial**."))}

{unidad("1.2 Competencia compartida (TFUE, art. 4.2 c)",
  lit("TFUE", "Artículo 4", ["la cohesión económica, social y territorial"], solo=[2, 5], titulo="Artículo 4.2 c) (TFUE)"),
  fichab("Tipo de competencia", "La Unión y los Estados miembros",
         "Competencia **compartida** (no exclusiva)", "—",
         "La cohesión es competencia **compartida** (art. 4.2 c); la política comercial común es **exclusiva** (art. 3.1 e). Pregunta oficial P 8 (→ Cierre 1)."))}

{unidad("1.3 Qué persigue la política de cohesión (TFUE, art. 174)",
  lit("TFUE", "Artículo 174", ["desarrollo armonioso del conjunto de la Unión", "reducir las diferencias entre los niveles de desarrollo de las diversas regiones y el retraso de las regiones menos favorecidas", "las zonas rurales", "las regiones más septentrionales con una escasa densidad de población y las regiones insulares, transfronterizas y de montaña"]),
  fichab("Objetivo de la acción de cohesión", "La Unión",
         ["Fin: **desarrollo armonioso** del conjunto de la Unión", "Reducir las **diferencias de desarrollo** entre regiones y el **retraso de las menos favorecidas**", "Atención especial: **zonas rurales**, zonas en **transición industrial**, regiones con **desventajas naturales o demográficas graves y permanentes** (más septentrionales con escasa densidad, **insulares, transfronterizas y de montaña**)"],
         "—",
         "La lista de regiones de atención especial es un ejemplo («como, por ejemplo»): **septentrionales** poco pobladas, **insulares**, **transfronterizas** y **de montaña**."))}
""", 2)

T.ap("s17", "VI.2 Los instrumentos: fondos estructurales, FEDER y Fondo de Cohesión (TFUE, arts. 175 a 178)", f"""
{unidad("2.1 Coordinación, fondos con finalidad estructural e informe trienal (art. 175)",
  lit("TFUE", "Artículo 175", ["fondos con finalidad estructural", "Cada tres años", "con arreglo al procedimiento legislativo ordinario y previa consulta al Comité Económico y Social y al Comité de las Regiones"]),
  fichab("Cómo se persigue la cohesión",
         ["Los **Estados miembros** conducen y coordinan su política económica también con este fin", "La **Unión**, con los fondos estructurales, el **BEI** y otros instrumentos", "Informe: la **Comisión**, al Parlamento, al Consejo, al CESE y al Comité de las Regiones"],
         ["Fondos con finalidad estructural: **FEOGA-Orientación**, **FSE** y **FEDER**", "Acciones específicas al margen de los fondos: Parlamento Europeo y Consejo"],
         ["Informe de la Comisión: **cada tres años**", "Acciones específicas: procedimiento legislativo **ordinario**, previa consulta al **CESE** y al **Comité de las Regiones**"],
         "El informe sobre la cohesión es **trienal**. El art. 175 cita **tres** fondos con finalidad estructural; el **Fondo de Cohesión** está en el art. 177."))}

{unidad("2.2 El FEDER (art. 176)",
  lit("TFUE", "Artículo 176", ["contribuir a la corrección de los principales desequilibrios regionales dentro de la Unión", "regiones menos desarrolladas", "reconversión de las regiones industriales en declive"]),
  fichab("Fondo para los desequilibrios regionales", "Fondo Europeo de Desarrollo Regional",
         ["Corregir los **principales desequilibrios regionales**", "Desarrollo y ajuste estructural de las **regiones menos desarrolladas**", "**Reconversión** de las **regiones industriales en declive**"],
         "—",
         f"{c('TFUE', 'Artículo 176', 'corrección de los principales desequilibrios regionales')} es el **FEDER**, no el Fondo de Cohesión (pregunta oficial P 17, → Cierre 1)."))}

{unidad("2.3 Fondos estructurales y Fondo de Cohesión (art. 177)",
  lit("TFUE", "Artículo 177", ["mediante reglamentos adoptados con arreglo al procedimiento legislativo ordinario", "Un Fondo de Cohesión", "proyectos en los sectores del medio ambiente y de las redes transeuropeas en materia de infraestructuras del transporte"]),
  fichab("Organización de los fondos y creación del Fondo de Cohesión",
         "**Parlamento Europeo y Consejo**, mediante reglamentos",
         ["Determinan las **funciones**, los **objetivos prioritarios** y la **organización** de los fondos con finalidad estructural (pueden **agruparlos**)", "Fijan las **normas generales** de los fondos y su coordinación", f"{c('TFUE', 'Artículo 177', 'Un Fondo de Cohesión')}: contribución financiera a proyectos de **medio ambiente** y de **redes transeuropeas** de infraestructuras del transporte"],
         "Procedimiento legislativo **ordinario**, tras consultar al **CESE** y al **Comité de las Regiones**",
         "Objetivo del **Fondo de Cohesión**: proyectos de **medio ambiente** y **redes transeuropeas de transporte** (pregunta oficial P 17, → Cierre 1)."))}

{unidad("2.4 Reglamentos de aplicación del FEDER (art. 178)",
  lit("TFUE", "Artículo 178", ["Los reglamentos de aplicación relativos al Fondo Europeo de Desarrollo Regional", "los artículos 43 y 164"]),
  fichab("Quién dicta los reglamentos de aplicación",
         "FEDER: **Parlamento Europeo y Consejo**",
         ["FEDER: procedimiento legislativo ordinario", "FEOGA-Orientación: art. 43 (agricultura); FSE: art. 164 (→ V.1.2)"],
         "Procedimiento legislativo **ordinario**, previa consulta al **CESE** y al **Comité de las Regiones**",
         "Cada fondo tiene su base: FEDER (178), FSE (164), FEOGA-Orientación (43)."))}
""", 2)

T.ap("s18", "VI.3 Las categorías de regiones (Reglamento (UE) 2021/1060, arts. 5.2 y 108)", f"""
{unidad("3.1 Los dos objetivos de la cohesión (art. 5.2)",
  lit("RDC", "Artículo 5", ["el objetivo de inversión en empleo y crecimiento", "el objetivo de cooperación territorial europea (Interreg), con el apoyo del FEDER"], solo=[9, 10, 11], titulo="Artículo 5.2 (Reglamento (UE) 2021/1060) · Objetivos políticos"),
  fichab("Objetivos de los fondos de cohesión en 2021-2027", "FEDER, FSE+, Fondo de Cohesión y FTJ",
         ["a) **Inversión en empleo y crecimiento**: FEDER, FSE+, Fondo de Cohesión y FTJ", "b) **Cooperación territorial europea (Interreg)**: solo el **FEDER**"],
         "—",
         "**Interreg** se apoya **solo** en el **FEDER**."))}

{unidad("3.2 Regiones y Estados beneficiarios (art. 108)",
  lit("RDC", "Artículo 108", ["regiones de nivel NUTS 2", "inferior al 75 %", "entre el 75 % y el 100 %", "superior al 100 %", "sea inferior al 90 % de la RNB media per cápita de la UE-27", "del 1 de enero de 2021 al 31 de diciembre de 2027"], titulo="Artículo 108 (Reglamento (UE) 2021/1060) · Ámbito geográfico de la ayuda destinada al objetivo de inversión en empleo y crecimiento"),
  fichab("Quién recibe la ayuda del objetivo de inversión en empleo y crecimiento",
         ["FEDER y FSE+: **regiones NUTS 2**, en tres categorías", "Fondo de Cohesión: **Estados miembros**", "Lista: la **Comisión**, mediante acto de ejecución"],
         ["**Menos desarrolladas**: PIB per cápita **< 75 %** de la media UE-27", "**En transición**: **entre el 75 % y el 100 %**", "**Más desarrolladas**: **> 100 %**", "Fondo de Cohesión: Estados con **RNB per cápita < 90 %** de la media"],
         ["Referencia: cifras de **2015-2017**", "Lista válida del **1.1.2021 al 31.12.2027**"],
         "Para las **regiones** se usa el **PIB** per cápita (75 % / 100 %); para el **Fondo de Cohesión**, la **RNB** per cápita del **Estado** (90 %)."))}

{resumen([
  "Cohesión **económica, social y territorial**: objetivo de la Unión (TUE 3.3) y competencia **compartida** (TFUE 4.2 c).",
  "Fin: **desarrollo armonioso**; reducir diferencias entre regiones y el **retraso de las menos favorecidas**; atención a zonas **rurales**, en **transición industrial** e islas, montaña, zonas transfronterizas y septentrionales poco pobladas (174).",
  "Instrumentos: fondos estructurales (**FEOGA-Orientación, FSE, FEDER**), **BEI**; informe de la Comisión **cada tres años** (175). **FEDER**: desequilibrios regionales (176); **Fondo de Cohesión**: medio ambiente y redes transeuropeas de transporte (177).",
  "Regiones (RDC 108): **< 75 %**, **75-100 %**, **> 100 %** del PIB per cápita; Fondo de Cohesión: Estados con RNB **< 90 %**."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

T.ap("s19", "Pendiente (temario)", """
Lo que sigue lo pide el epígrafe o lo suelen tratar los temarios, pero **no está en las normas citadas** ni se ha encontrado una fuente oficial descargable en español. Se completará con el temario del usuario:

- **Cuantías del MFP 2021-2027** por rúbricas (anexo I del Reglamento 2020/2093: tablas de importes, no extraídas aquí) y del instrumento de recuperación.
- **Antecedentes y evolución** del presupuesto comunitario, de los fondos y de la política de cohesión (perspectivas financieras anteriores, reformas de los fondos).
- **Asignaciones a España** y **gestión de los fondos europeos en España** (Plan de Recuperación, Transformación y Resiliencia y su normativa interna).
""")

# =============================================================================
EX_L26 = examen("L", 26, {
  "a": f"El art. 320 no prevé excepciones: {c('TFUE', 'Artículo 320', 'El marco financiero plurianual y el presupuesto anual se establecerán en euros')}.",
  "b": f"Cambia el órgano: según el art. 317, {c('TFUE', 'Artículo 317', 'la Comisión podrá transferir créditos de capítulo a capítulo o de subdivisión a subdivisión')}; no el Parlamento.",
  "c": f"Literal del art. 319.1: {c('TFUE', 'Artículo 319', 'El Parlamento Europeo, por recomendación del Consejo, aprobará la gestión de la Comisión en la ejecución del presupuesto')}.",
  "d": f"Cambia el período: según el art. 310.2, los gastos {c('TFUE', 'Artículo 310', 'serán autorizados para todo el ejercicio presupuestario anual')}, no con carácter semestral."},
  [("por recomendación del Consejo, aprobará la gestión de la Comisión", "TFUE", "Artículo 319", "El Parlamento Europeo, por recomendación del Consejo, aprobará la gestión de la Comisión en la ejecución del presupuesto")])
EX_X35 = examen("X", 35, {
  "a": f"Cambia el plazo: el MFP {c('TFUE', 'Artículo 312', 'Se establecerá para un período mínimo de cinco años')} (art. 312.1), no de cuatro.",
  "b": f"Cambia el procedimiento: el presupuesto anual se establece {c('TFUE', 'Artículo 314', 'con arreglo a un procedimiento legislativo especial')} (art. 314), no ordinario.",
  "c": f"No son todas: {c('TFUE', 'Artículo 314', 'Cada institución, excepto el Banco Central Europeo, elaborará, antes del 1 de julio, un estado de previsiones de sus gastos')} (art. 314.1).",
  "d": f"Correcta: el Reglamento (UE, Euratom) 2020/2093 {c('MFPC', 'Artículo 1', 'establece el marco financiero plurianual para los ejercicios 2021 a 2027')} (art. 1)."},
  [("2021-2027", "MFPC", "Artículo 1", "El presente Reglamento establece el marco financiero plurianual para los ejercicios 2021 a 2027")])
EX_P17 = examen("P", 17, {
  "a": f"Es el fin del **FEDER** (art. 176): {c('TFUE', 'Artículo 176', 'contribuir a la corrección de los principales desequilibrios regionales dentro de la Unión')}.",
  "b": f"Literal del art. 177: {c('TFUE', 'Artículo 177', 'Un Fondo de Cohesión, creado con arreglo al mismo procedimiento, proporcionará una contribución financiera a proyectos en los sectores del medio ambiente')} y de las redes transeuropeas de transporte.",
  "c": f"Es el fin del **Fondo Social Europeo** (art. 162): {c('TFUE', 'Artículo 162', 'Para mejorar las posibilidades de empleo de los trabajadores en el mercado interior')}.",
  "d": f"También es del **Fondo Social Europeo** (art. 162): {c('TFUE', 'Artículo 162', 'facilitar su adaptación a las transformaciones industriales')}."},
  [("proyectos en los sectores de medio ambiente", "TFUE", "Artículo 177", "proporcionará una contribución financiera a proyectos en los sectores del medio ambiente")])
EX_P8 = examen("P", 8, {
  "a": f"Es competencia **compartida**: art. 4.2 c), {c('TFUE', 'Artículo 4', 'la cohesión económica, social y territorial')}.",
  "b": f"Es competencia **compartida**: art. 4.2 f), {c('TFUE', 'Artículo 4', 'la protección de los consumidores')}.",
  "c": f"Es competencia **compartida**: art. 4.2 h), {c('TFUE', 'Artículo 4', 'las redes transeuropeas')}.",
  "d": f"Literal del art. 3.1 e): competencia exclusiva en {c('TFUE', 'Artículo 3', 'la política comercial común')}."},
  [("política comercial común", "TFUE", "Artículo 3", "la política comercial común")])
EX_L27 = examen("L", 27, {
  "a": f"No es el nombre del programa marco: el Reglamento (UE) 2021/695 {c('HEUR', 'Artículo 1', 'establece el Programa Marco de Investigación e Innovación «Horizonte Europa»')}.",
  "b": "No es el programa marco de investigación e innovación que establece el Reglamento (UE) 2021/695 (art. 1.1).",
  "c": "No es el programa marco de investigación e innovación que establece el Reglamento (UE) 2021/695 (art. 1.1).",
  "d": f"Literal del art. 1.1 del Reglamento (UE) 2021/695: {c('HEUR', 'Artículo 1', 'el Programa Marco de Investigación e Innovación «Horizonte Europa»')}, {c('HEUR', 'Artículo 1', 'por el período de vigencia del marco financiero plurianual 2021-2027')}."},
  [("Horizonte Europa", "HEUR", "Artículo 1", "el Programa Marco de Investigación e Innovación «Horizonte Europa» (en lo sucesivo, «Programa») por el período de vigencia del marco financiero plurianual 2021-2027")])
EX_L102 = examen("L", 102, {
  "a": f"Literal del art. 25.1: {c('FEMPA', 'Artículo 25', 'El FEMPA podrá apoyar acciones que contribuyan a la protección y la recuperación de la biodiversidad y los ecosistemas acuáticos, incluso en las aguas interiores')}.",
  "b": f"Cambia una palabra: el texto dice {c('FEMPA', 'Artículo 25', 'incluso en las aguas interiores')}, no «salvo».",
  "c": f"Cambia una palabra: el texto dice aguas {c('FEMPA', 'Artículo 25', 'interiores')}, no «fluviales».",
  "d": f"Cambia dos palabras: el texto dice {c('FEMPA', 'Artículo 25', 'incluso en las aguas interiores')}."},
  [("incluso en las aguas interiores", "FEMPA", "Artículo 25", "incluso en las aguas interiores")])

T.ap("s20", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **tres** preguntas de este tema (presupuesto: L 26 y X 35; cohesión: P 17) y **tres** relacionadas (P 8, competencias; L 27, Horizonte Europa; L 102, FEMPA, de reserva). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-L 2025, pregunta 26 · Aprobación de la gestión (→ IV.2.3)", EX_L26,
  "### GACE-L 2025 extraordinario, pregunta 35 · MFP y procedimiento presupuestario (→ III.2.1)", EX_X35,
  "### GACE-P 2025, pregunta 17 · Fondo de Cohesión (→ VI.2.3)", EX_P17,
  "### GACE-P 2025, pregunta 8 · Competencias de la Unión (relacionada; → VI.1.2)", EX_P8,
  "### GACE-L 2025, pregunta 27 · Horizonte Europa (relacionada; → V.5.2)", EX_L27,
  "### GACE-L 2025, pregunta 102 (reserva) · FEMPA (relacionada; → V.4.2)", EX_L102,
  "### Cómo se pregunta",
  "!> Las preguntas del presupuesto mezclan **artículos vecinos** (310, 312, 314, 317, 319, 320) cambiando **un órgano** (Comisión/Parlamento), **un plazo** (cinco años, anual) o **un procedimiento** (especial/ordinario). Las de fondos cambian **el fondo** al que corresponde cada finalidad (FEDER, Fondo de Cohesión, FSE).",
]))

T.ap("s21", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Reglas del presupuesto | Todos los ingresos y gastos; equilibrio; acto previo; disciplina; buena gestión (310); año natural (313); capítulos (316); euros (320) | Gastos autorizados para **todo el ejercicio anual**; **euros** sin excepciones |
| II. Recursos propios | Financiación **íntegra** con recursos propios; Decisión del **Consejo por unanimidad**, aprobada por los Estados (311); Decisión 2020/2053 | Cuatro recursos: tradicionales, IVA **0,30 %**, plástico **0,80 EUR/kg**, RNB; techo **1,40 % / 1,46 %** |
| III. MFP | Reglamento del **Consejo** por unanimidad, previa **aprobación** del Parlamento (312) | **Mínimo cinco años**; MFP vigente **2021-2027** |
| IV. Aprobación, ejecución y control | Procedimiento **especial** (314); doceavas partes (315); ejecuta la **Comisión** (317); aprueba la gestión el **Parlamento**, por recomendación del **Consejo** (319) | **1 julio · 1 septiembre · 1 octubre · 42 · 21 · 14**; previsiones de todas **salvo el BCE** |
| V. Fondos | FSE (162-164) y FSE+; RDC (8 fondos, 5 objetivos políticos); FEDER y FC; FEAGA, Feader, FEMPA; MRR; Horizonte Europa | **FC**: medio ambiente y redes transeuropeas; Feader solo gestión compartida |
| VI. Cohesión | Objetivo (TUE 3.3) y competencia **compartida** (TFUE 4.2 c); arts. 174 a 178; categorías de regiones (RDC 108) | **FEDER**: desequilibrios regionales; regiones **< 75 % / 75-100 % / > 100 %**; FC: RNB **< 90 %** |

?> **Trampas frecuentes:** «el **Parlamento** transfiere créditos» (los transfiere la **Comisión**, 317); «el **Consejo**, por recomendación del Parlamento, aprueba la gestión» (es al revés, 319); «MFP de **cuatro** años» (mínimo **cinco**, 312); «presupuesto por procedimiento legislativo **ordinario**» (es **especial**, 314); «**todas** las instituciones elaboran previsiones» (todas **excepto el BCE**); «el Fondo de Cohesión corrige los **desequilibrios regionales**» (eso es el **FEDER**, 176); «la cohesión es competencia **exclusiva**» (es **compartida**, 4.2 c).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
Q = T.q
Q("TFUE", "Artículo 310", "Principios presupuestarios", "Según el artículo 310.1 del TFUE, el presupuesto de la Unión deberá estar:",
  ["Equilibrado en cuanto a ingresos y gastos.", "Equilibrado a lo largo del período del marco financiero plurianual.", "Financiado en un 50 % con contribuciones nacionales.", "Aprobado antes del 1 de octubre del año anterior."],
  "Art. 310.1 TFUE: «El presupuesto deberá estar equilibrado en cuanto a ingresos y gastos».", "El presupuesto deberá estar equilibrado en cuanto a ingresos y gastos")
Q("TFUE", "Artículo 310", "Principios presupuestarios", "Según el artículo 310.2 del TFUE, los gastos consignados en el presupuesto serán autorizados:",
  ["Para todo el ejercicio presupuestario anual.", "Con carácter semestral.", "Para todo el período del marco financiero plurianual.", "Con carácter trimestral, previa autorización del Consejo."],
  "Art. 310.2 TFUE.", "serán autorizados para todo el ejercicio presupuestario anual")
Q("TFUE", "Artículo 310", "Principios presupuestarios", "Según el artículo 310.3 del TFUE, la ejecución de gastos consignados en el presupuesto requerirá:",
  ["La adopción previa de un acto jurídicamente vinculante de la Unión que otorgue un fundamento jurídico a su acción.", "La aprobación previa del Tribunal de Cuentas.", "El dictamen previo del Comité de las Regiones.", "La autorización previa de los Parlamentos nacionales."],
  "Art. 310.3 TFUE.", "requerirá la adopción previa de un acto jurídicamente vinculante de la Unión que otorgue un fundamento jurídico a su acción")
Q("TFUE", "Artículo 310", "Principios presupuestarios", "Según el artículo 310.5 del TFUE, el presupuesto se ejecutará con arreglo al principio de:",
  ["Buena gestión financiera.", "Unidad de caja.", "Anualidad estricta.", "Solidaridad entre los Estados miembros."],
  "Art. 310.5 TFUE.", "El presupuesto se ejecutará con arreglo al principio de buena gestión financiera")
Q("TFUE", "Artículo 313", "Principios presupuestarios", "Según el artículo 313 del TFUE, el ejercicio presupuestario de la Unión:",
  ["Comenzará el 1 de enero y finalizará el 31 de diciembre.", "Comenzará el 1 de julio y finalizará el 30 de junio.", "Coincidirá con el período del marco financiero plurianual.", "Comenzará el 1 de octubre y finalizará el 30 de septiembre."],
  "Art. 313 TFUE.", "El ejercicio presupuestario comenzará el 1 de enero y finalizará el 31 de diciembre")
Q("TFUE", "Artículo 316", "Principios presupuestarios", "Según el artículo 316 del TFUE, los créditos que no correspondan a gastos de personal y que queden sin utilizar al final del ejercicio:",
  ["Sólo podrán ser prorrogados hasta el ejercicio siguiente.", "Podrán prorrogarse hasta el final del marco financiero plurianual.", "Se devolverán en todo caso a los Estados miembros.", "Se transferirán automáticamente al Fondo de Cohesión."],
  "Art. 316 TFUE.", "sólo podrán ser prorrogados hasta el ejercicio siguiente")
Q("TFUE", "Artículo 320", "Principios presupuestarios", "Según el artículo 320 del TFUE, el marco financiero plurianual y el presupuesto anual se establecerán:",
  ["En euros.", "En euros, salvo para los Estados miembros que no lo hayan adoptado.", "En la moneda de cada Estado miembro.", "En derechos especiales de giro."],
  "Art. 320 TFUE.", "El marco financiero plurianual y el presupuesto anual se establecerán en euros")
Q("TFUE", "Artículo 311", "Recursos propios", "Según el artículo 311 del TFUE, sin perjuicio del concurso de otros ingresos, el presupuesto será financiado:",
  ["Íntegramente con cargo a los recursos propios.", "Mayoritariamente con contribuciones de los Estados miembros.", "Con cargo a los empréstitos contraídos por la Comisión.", "A partes iguales con recursos propios y contribuciones nacionales."],
  "Art. 311 TFUE.", "el presupuesto será financiado íntegramente con cargo a los recursos propios")
Q("TFUE", "Artículo 311", "Recursos propios", "Según el artículo 311 del TFUE, la decisión que establece las disposiciones aplicables al sistema de recursos propios la adopta el Consejo:",
  ["Por unanimidad y previa consulta al Parlamento Europeo.", "Por mayoría cualificada y previa aprobación del Parlamento Europeo.", "Por unanimidad, conjuntamente con el Parlamento Europeo por el procedimiento legislativo ordinario.", "Por mayoría simple, previa consulta al Tribunal de Cuentas."],
  "Art. 311, párrafo tercero, TFUE; después debe ser aprobada por los Estados miembros.", "por unanimidad y previa consulta al Parlamento Europeo")
Q("TFUE", "Artículo 311", "Recursos propios", "Según el artículo 311 del TFUE, la decisión sobre el sistema de recursos propios sólo entrará en vigor:",
  ["Una vez que haya sido aprobada por los Estados miembros, de conformidad con sus respectivas normas constitucionales.", "A los veinte días de su publicación en el Diario Oficial.", "Cuando la apruebe el Parlamento Europeo por mayoría de sus miembros.", "Cuando la ratifique el Consejo Europeo por consenso."],
  "Art. 311 TFUE.", "Dicha decisión sólo entrará en vigor una vez que haya sido aprobada por los Estados miembros, de conformidad con sus respectivas normas constitucionales")
Q("DRP", "Artículo 2", "Recursos propios", "Según el artículo 2.1 b) de la Decisión (UE, Euratom) 2020/2053, el recurso propio basado en el IVA se obtiene aplicando un tipo uniforme de referencia del:",
  ["0,30 %.", "0,80 %.", "1,40 %.", "0,50 %."],
  "Art. 2.1 b) Decisión 2020/2053.", "un tipo uniforme de referencia del 0,30 %")
Q("DRP", "Artículo 2", "Recursos propios", "Según el artículo 2.1 c) de la Decisión (UE, Euratom) 2020/2053, el tipo uniforme de referencia aplicable al peso de los residuos de envases de plástico no reciclados será de:",
  ["0,80 EUR por kilogramo.", "0,30 EUR por kilogramo.", "1 EUR por kilogramo.", "0,80 EUR por tonelada."],
  "Art. 2.1 c) Decisión 2020/2053.", "El tipo uniforme de referencia será de 0,80 EUR por kilogramo")
Q("DRP", "Artículo 3", "Recursos propios", "Según el artículo 3.1 de la Decisión (UE, Euratom) 2020/2053, el importe total de los recursos propios asignados a la Unión para financiar los créditos de pago anuales no rebasará:",
  ["El 1,40 % de la suma de la RNB de todos los Estados miembros.", "El 1,46 % de la suma de la RNB de todos los Estados miembros.", "El 1,00 % de la suma del PIB de todos los Estados miembros.", "El 0,30 % de la suma de la RNB de todos los Estados miembros."],
  "Art. 3.1 Decisión 2020/2053 (el 1,46 % es el límite de los créditos de compromiso, art. 3.2).", "no rebasará el 1,40 % de la suma de la RNB de todos los Estados miembros")
Q("DRP", "Artículo 4", "Recursos propios", "Según el artículo 4 de la Decisión (UE, Euratom) 2020/2053, la Unión no utilizará empréstitos contraídos en mercados de capitales para financiar:",
  ["Gastos operativos.", "Préstamos a los Estados miembros.", "Gastos de personal de las instituciones.", "Ninguna clase de gasto ni de préstamo, sin excepciones."],
  "Art. 4 Decisión 2020/2053 (con la excepción temporal del art. 5).", "La Unión no utilizará empréstitos contraídos en mercados de capitales para financiar gastos operativos")
Q("DRP", "Artículo 9", "Recursos propios", "Según el artículo 9.2 de la Decisión (UE, Euratom) 2020/2053, los Estados miembros retendrán, en concepto de gastos de recaudación, el siguiente porcentaje de los recursos propios tradicionales:",
  ["El 25 %.", "El 20 %.", "El 10 %.", "El 50 %."],
  "Art. 9.2 Decisión 2020/2053.", "Los Estados miembros retendrán, en concepto de gastos de recaudación, el 25 %")
Q("TFUE", "Artículo 312", "Marco financiero plurianual", "Según el artículo 312.1 del TFUE, el marco financiero plurianual se establecerá para un período mínimo de:",
  ["Cinco años.", "Cuatro años.", "Siete años.", "Diez años."],
  "Art. 312.1 TFUE.", "Se establecerá para un período mínimo de cinco años")
Q("TFUE", "Artículo 312", "Marco financiero plurianual", "Según el artículo 312.2 del TFUE, el reglamento que fija el marco financiero plurianual lo adopta:",
  ["El Consejo, por unanimidad, previa aprobación del Parlamento Europeo.", "El Parlamento Europeo y el Consejo, por el procedimiento legislativo ordinario.", "El Consejo Europeo, por consenso, a propuesta de la Comisión.", "El Consejo, por mayoría cualificada, previa consulta al Parlamento Europeo."],
  "Art. 312.2 TFUE.", "El Consejo se pronunciará por unanimidad, previa aprobación del Parlamento Europeo")
Q("TFUE", "Artículo 312", "Marco financiero plurianual", "Según el artículo 312.4 del TFUE, si al vencimiento del marco financiero anterior no se ha adoptado el nuevo:",
  ["Se prorrogarán los límites máximos y las demás disposiciones correspondientes al último año de aquél hasta que se adopte dicho acto.", "La Comisión aprobará un marco provisional por un año.", "Se aplicará la doceava parte de los créditos del último ejercicio.", "El presupuesto anual quedará sin límites máximos hasta que se adopte."],
  "Art. 312.4 TFUE.", "se prorrogarán los límites máximos y las demás disposiciones correspondientes al último año de aquél hasta que se adopte dicho acto")
Q("MFPC", "Artículo 1", "Marco financiero plurianual", "Según el artículo 1 del Reglamento (UE, Euratom) 2020/2093, el marco financiero plurianual vigente se establece para los ejercicios:",
  ["2021 a 2027.", "2020 a 2026.", "2021 a 2025.", "2014 a 2020."],
  "Art. 1 Reglamento 2020/2093.", "el marco financiero plurianual para los ejercicios 2021 a 2027")
Q("TFUE", "Artículo 314", "Procedimiento presupuestario", "Según el artículo 314 del TFUE, el Parlamento Europeo y el Consejo establecerán el presupuesto anual de la Unión con arreglo a:",
  ["Un procedimiento legislativo especial.", "El procedimiento legislativo ordinario.", "El procedimiento de cooperación reforzada.", "Un acuerdo interinstitucional aprobado por el Consejo Europeo."],
  "Art. 314 TFUE.", "con arreglo a un procedimiento legislativo especial")
Q("TFUE", "Artículo 314", "Procedimiento presupuestario", "Según el artículo 314.1 del TFUE, cada institución, excepto el Banco Central Europeo, elaborará un estado de previsiones de sus gastos para el ejercicio siguiente:",
  ["Antes del 1 de julio.", "Antes del 1 de septiembre.", "Antes del 1 de octubre.", "Antes del 1 de mayo."],
  "Art. 314.1 TFUE.", "elaborará, antes del 1 de julio, un estado de previsiones de sus gastos")
Q("TFUE", "Artículo 314", "Procedimiento presupuestario", "Según el artículo 314.2 del TFUE, la Comisión presentará la propuesta que contenga el proyecto de presupuesto a más tardar:",
  ["El 1 de septiembre del año que precede al de su ejecución.", "El 1 de julio del año que precede al de su ejecución.", "El 1 de octubre del año que precede al de su ejecución.", "El 31 de diciembre del año que precede al de su ejecución."],
  "Art. 314.2 TFUE.", "a más tardar el 1 de septiembre del año que precede al de su ejecución")
Q("TFUE", "Artículo 314", "Procedimiento presupuestario", "Según el artículo 314.4 del TFUE, si en el plazo de cuarenta y dos días desde la transmisión de la posición del Consejo el Parlamento Europeo no se pronuncia:",
  ["El presupuesto se considerará adoptado.", "La Comisión presentará un nuevo proyecto de presupuesto.", "Se convocará el Comité de Conciliación.", "Se prorrogará el presupuesto del ejercicio anterior."],
  "Art. 314.4 b) TFUE.", "no se pronuncia, el presupuesto se considerará adoptado")
Q("TFUE", "Artículo 314", "Procedimiento presupuestario", "Según el artículo 314.5 del TFUE, el Comité de Conciliación tendrá por misión alcanzar un acuerdo sobre un texto conjunto en un plazo de:",
  ["Veintiún días a partir de su convocatoria.", "Catorce días a partir de su convocatoria.", "Cuarenta y dos días a partir de su convocatoria.", "Diez días a partir de su convocatoria."],
  "Art. 314.5 TFUE.", "en un plazo de veintiún días a partir de su convocatoria")
Q("TFUE", "Artículo 314", "Procedimiento presupuestario", "Según el artículo 314.9 del TFUE, cuando haya concluido el procedimiento presupuestario, declarará que el presupuesto ha quedado definitivamente adoptado:",
  ["El Presidente del Parlamento Europeo.", "El Presidente del Consejo.", "El Presidente de la Comisión.", "El Presidente del Consejo Europeo."],
  "Art. 314.9 TFUE.", "el Presidente del Parlamento Europeo declarará que el presupuesto ha quedado definitivamente adoptado")
Q("TFUE", "Artículo 315", "Procedimiento presupuestario", "Según el artículo 315 del TFUE, si al iniciarse un ejercicio aún no se ha adoptado definitivamente el presupuesto, los gastos podrán efectuarse mensualmente por capítulos dentro del límite de:",
  ["La doceava parte de los créditos consignados en el capítulo correspondiente del presupuesto del ejercicio precedente.", "La sexta parte de los créditos consignados en el presupuesto del ejercicio precedente.", "La doceava parte de los créditos del marco financiero plurianual.", "La mitad de los créditos previstos en el proyecto de presupuesto."],
  "Art. 315 TFUE.", "dentro del límite de la doceava parte de los créditos consignados en el capítulo correspondiente del presupuesto del ejercicio precedente")
Q("TFUE", "Artículo 317", "Ejecución y control", "Según el artículo 317 del TFUE, el presupuesto lo ejecutará, bajo su propia responsabilidad y en cooperación con los Estados miembros:",
  ["La Comisión.", "El Consejo.", "El Parlamento Europeo.", "El Tribunal de Cuentas."],
  "Art. 317 TFUE.", "La Comisión, bajo su propia responsabilidad y dentro del límite de los créditos autorizados, ejecutará el presupuesto en cooperación con los Estados miembros")
Q("TFUE", "Artículo 319", "Ejecución y control", "Según el artículo 319.1 del TFUE, la gestión de la Comisión en la ejecución del presupuesto la aprueba:",
  ["El Parlamento Europeo, por recomendación del Consejo.", "El Consejo, por recomendación del Parlamento Europeo.", "El Tribunal de Cuentas, previo informe del Consejo.", "El Consejo Europeo, a propuesta del Parlamento Europeo."],
  "Art. 319.1 TFUE.", "El Parlamento Europeo, por recomendación del Consejo, aprobará la gestión de la Comisión en la ejecución del presupuesto")
Q("TFUE", "Artículo 322", "Ejecución y control", "Según el artículo 322.1 del TFUE, las normas financieras sobre el establecimiento y la ejecución del presupuesto se adoptan mediante reglamentos:",
  ["Con arreglo al procedimiento legislativo ordinario y tras consultar al Tribunal de Cuentas.", "Del Consejo, por unanimidad, previa consulta al Parlamento Europeo.", "De la Comisión, previa aprobación del Consejo.", "Con arreglo a un procedimiento legislativo especial, previa aprobación del Tribunal de Cuentas."],
  "Art. 322.1 TFUE.", "con arreglo al procedimiento legislativo ordinario y tras consultar al Tribunal de Cuentas")
Q("TFUE", "Artículo 325", "Ejecución y control", "Según el artículo 325.2 del TFUE, para combatir el fraude que afecte a los intereses financieros de la Unión, los Estados miembros adoptarán:",
  ["Las mismas medidas que para combatir el fraude que afecte a sus propios intereses financieros.", "Las medidas que les indique en cada caso la Comisión.", "Medidas penales armonizadas aprobadas por el Consejo por unanimidad.", "Medidas más severas que las que aplican a sus propios intereses financieros."],
  "Art. 325.2 TFUE (asimilación).", "las mismas medidas que para combatir el fraude que afecte a sus propios intereses financieros")
Q("TFUE", "Artículo 324", "Ejecución y control", "Según el artículo 324 del TFUE, las reuniones periódicas de los Presidentes del Parlamento Europeo, del Consejo y de la Comisión en el marco de los procedimientos presupuestarios se convocan:",
  ["Por iniciativa de la Comisión.", "Por iniciativa del Parlamento Europeo.", "Por iniciativa del Consejo Europeo.", "Por iniciativa del Tribunal de Cuentas."],
  "Art. 324 TFUE.", "Por iniciativa de la Comisión, se convocarán reuniones periódicas de los Presidentes")
Q("TFUE", "Artículo 162", "Fondos europeos", "Según el artículo 162 del TFUE, el Fondo Social Europeo se crea para:",
  ["Mejorar las posibilidades de empleo de los trabajadores en el mercado interior y contribuir así a la elevación del nivel de vida.", "Contribuir financieramente a proyectos en los sectores del medio ambiente.", "Corregir los principales desequilibrios regionales dentro de la Unión.", "Financiar los pagos directos a los agricultores."],
  "Art. 162 TFUE.", "Para mejorar las posibilidades de empleo de los trabajadores en el mercado interior y contribuir así a la elevación del nivel de vida")
Q("TFUE", "Artículo 163", "Fondos europeos", "Según el artículo 163 del TFUE, la administración del Fondo Social Europeo corresponderá a:",
  ["La Comisión.", "El Consejo.", "Los Estados miembros.", "El Banco Europeo de Inversiones."],
  "Art. 163 TFUE.", "La administración del Fondo corresponderá a la Comisión")
Q("RDC", "Artículo 5", "Fondos europeos", "Según el artículo 5.2 del Reglamento (UE) 2021/1060, el objetivo de cooperación territorial europea (Interreg) cuenta con el apoyo de:",
  ["El FEDER.", "El Fondo de Cohesión.", "El FSE+.", "El FEMPA."],
  "Art. 5.2 b) Reglamento 2021/1060.", "el objetivo de cooperación territorial europea (Interreg), con el apoyo del FEDER")
Q("PAC2116", "Artículo 6", "Fondos europeos", "Según el artículo 6 del Reglamento (UE) 2021/2116, el Feader se ejecutará:",
  ["En régimen de gestión compartida entre los Estados miembros y la Unión.", "En régimen de gestión directa por la Comisión.", "En régimen de gestión indirecta a través del Banco Europeo de Inversiones.", "Indistintamente en gestión compartida o directa."],
  "Art. 6 Reglamento 2021/2116 (el FEAGA puede ser compartida o directa, art. 5.1).", "El Feader se ejecutará en régimen de gestión compartida entre los Estados miembros y la Unión")
Q("MRR", "Artículo 3", "Fondos europeos", "Según el artículo 3 del Reglamento (UE) 2021/241, el ámbito de aplicación del Mecanismo de Recuperación y Resiliencia se estructura en:",
  ["Seis pilares.", "Cuatro pilares.", "Cinco objetivos políticos.", "Tres ejes."],
  "Art. 3 Reglamento 2021/241.", "estructurados en seis pilares")
Q("TUE", "Artículo 3", "Cohesión", "Según el artículo 3.3 del TUE, la Unión fomentará la cohesión económica, social y territorial y:",
  ["La solidaridad entre los Estados miembros.", "La convergencia fiscal entre los Estados miembros.", "La uniformidad de las regiones.", "La competencia entre los Estados miembros."],
  "Art. 3.3 TUE.", "fomentará la cohesión económica, social y territorial y la solidaridad entre los Estados miembros")
Q("TFUE", "Artículo 174", "Cohesión", "Según el artículo 174 del TFUE, la Unión se propondrá, en particular, reducir las diferencias entre los niveles de desarrollo de las diversas regiones y:",
  ["El retraso de las regiones menos favorecidas.", "El retraso de los Estados miembros con menor renta.", "La población de las zonas urbanas.", "Las diferencias de los tipos impositivos."],
  "Art. 174 TFUE.", "reducir las diferencias entre los niveles de desarrollo de las diversas regiones y el retraso de las regiones menos favorecidas")
Q("TFUE", "Artículo 175", "Cohesión", "Según el artículo 175 del TFUE, la Comisión presentará un informe sobre los avances realizados en la consecución de la cohesión económica, social y territorial:",
  ["Cada tres años.", "Cada año.", "Cada cinco años.", "Cada siete años, al final del marco financiero plurianual."],
  "Art. 175 TFUE.", "Cada tres años, la Comisión presentará un informe")
Q("TFUE", "Artículo 176", "Cohesión", "Según el artículo 176 del TFUE, el fondo destinado a contribuir a la corrección de los principales desequilibrios regionales dentro de la Unión es:",
  ["El Fondo Europeo de Desarrollo Regional.", "El Fondo de Cohesión.", "El Fondo Social Europeo.", "El Fondo Europeo Agrícola de Desarrollo Rural."],
  "Art. 176 TFUE.", "El Fondo Europeo de Desarrollo Regional estará destinado a contribuir a la corrección de los principales desequilibrios regionales dentro de la Unión")
Q("TFUE", "Artículo 177", "Cohesión", "Según el artículo 177 del TFUE, el Fondo de Cohesión proporcionará una contribución financiera a proyectos en los sectores:",
  ["Del medio ambiente y de las redes transeuropeas en materia de infraestructuras del transporte.", "De la investigación y de la innovación.", "Del empleo y de la formación profesional.", "De la agricultura y del desarrollo rural."],
  "Art. 177 TFUE.", "proyectos en los sectores del medio ambiente y de las redes transeuropeas en materia de infraestructuras del transporte")
Q("RDC", "Artículo 108", "Cohesión", "Según el artículo 108.2 del Reglamento (UE) 2021/1060, son regiones menos desarrolladas aquellas cuyo PIB per cápita sea:",
  ["Inferior al 75 % del PIB medio per cápita de la UE-27.", "Inferior al 90 % del PIB medio per cápita de la UE-27.", "Inferior al 100 % del PIB medio per cápita de la UE-27.", "Inferior al 50 % del PIB medio per cápita de la UE-27."],
  "Art. 108.2 a) Reglamento 2021/1060.", "regiones menos desarrolladas, cuyo PIB per cápita sea inferior al 75 % del PIB medio per cápita de la UE-27")
Q("RDC", "Artículo 108", "Cohesión", "Según el artículo 108.3 del Reglamento (UE) 2021/1060, el Fondo de Cohesión prestará ayuda a los Estados miembros cuya RNB per cápita sea inferior al:",
  ["90 % de la RNB media per cápita de la UE-27.", "75 % de la RNB media per cápita de la UE-27.", "100 % de la RNB media per cápita de la UE-27.", "85 % de la RNB media per cápita de la UE-27."],
  "Art. 108.3 Reglamento 2021/1060.", "sea inferior al 90 % de la RNB media per cápita de la UE-27")
T.real("L", 26, "Ejecución y control"); T.real("X", 35, "Marco financiero plurianual"); T.real("P", 17, "Cohesión")
T.real("P", 8, "Cohesión"); T.real("L", 27, "Fondos europeos")

# Flashcards
for q_, a_, cat in [
  ("Reglas del art. 310 TFUE", "Todos los ingresos y gastos en el presupuesto; equilibrio; gastos autorizados para todo el ejercicio anual; acto jurídicamente vinculante previo; disciplina presupuestaria; buena gestión financiera; lucha contra el fraude.", "Principios presupuestarios"),
  ("Ejercicio presupuestario (art. 313)", "Del 1 de enero al 31 de diciembre.", "Principios presupuestarios"),
  ("¿Qué créditos no utilizados pueden prorrogarse? (art. 316)", "Los que no correspondan a gastos de personal, y solo hasta el ejercicio siguiente.", "Principios presupuestarios"),
  ("Financiación del presupuesto (art. 311)", "Íntegramente con recursos propios, sin perjuicio de otros ingresos.", "Recursos propios"),
  ("Decisión de recursos propios: quién y cómo (art. 311)", "Consejo, procedimiento legislativo especial, unanimidad, previa consulta al Parlamento; entra en vigor tras su aprobación por los Estados miembros.", "Recursos propios"),
  ("Categorías de recursos propios (Decisión 2020/2053, art. 2)", "Tradicionales; IVA (0,30 %); plástico no reciclado (0,80 EUR/kg); RNB.", "Recursos propios"),
  ("Límites máximos de recursos propios (Decisión 2020/2053, art. 3)", "1,40 % de la RNB (créditos de pago) y 1,46 % (créditos de compromiso).", "Recursos propios"),
  ("Gastos de recaudación que retienen los Estados (art. 9.2)", "El 25 % de los recursos propios tradicionales.", "Recursos propios"),
  ("Empréstitos COVID-19 (Decisión 2020/2053, art. 5)", "Hasta 750 000 millones EUR (precios de 2018): 360 000 para préstamos y 390 000 para gastos; reembolso a más tardar el 31.12.2058.", "Recursos propios"),
  ("MFP en el Tratado (art. 312)", "Mínimo cinco años; reglamento del Consejo por unanimidad, previa aprobación del Parlamento (mayoría de sus miembros); prórroga de los límites del último año si no se adopta.", "Marco financiero plurianual"),
  ("MFP vigente (Reglamento 2020/2093, art. 1)", "Ejercicios 2021 a 2027.", "Marco financiero plurianual"),
  ("Plazos del procedimiento presupuestario (art. 314)", "Previsiones antes del 1 de julio; proyecto el 1 de septiembre; posición del Consejo el 1 de octubre; Parlamento 42 días; conciliación 21 días; texto conjunto 14 días.", "Procedimiento presupuestario"),
  ("¿Qué institución no elabora estado de previsiones? (art. 314.1)", "El Banco Central Europeo.", "Procedimiento presupuestario"),
  ("Sin presupuesto el 1 de enero (art. 315)", "Gastos mensuales por capítulos hasta la doceava parte de los créditos del ejercicio precedente.", "Procedimiento presupuestario"),
  ("¿Quién ejecuta el presupuesto y transfiere créditos? (art. 317)", "La Comisión.", "Ejecución y control"),
  ("Aprobación de la gestión (art. 319)", "El Parlamento Europeo, por recomendación del Consejo.", "Ejecución y control"),
  ("Fines del FSE (art. 162)", "Empleo de los trabajadores, movilidad geográfica y profesional, adaptación a las transformaciones industriales.", "Fondos europeos"),
  ("Fondos con disposiciones comunes (Reglamento 2021/1060, art. 1)", "FEDER, FSE+, Fondo de Cohesión, FTJ y FEMPA (normas financieras también para FAMI, FSI e IGFV).", "Fondos europeos"),
  ("Los dos fondos agrícolas (Reglamento 2021/2116, art. 4)", "FEAGA y Feader.", "Fondos europeos"),
  ("Pilares del MRR (Reglamento 2021/241, art. 3)", "Seis: transición ecológica, transformación digital, crecimiento inteligente, cohesión social y territorial, salud y resiliencia, próxima generación.", "Fondos europeos"),
  ("FEDER (art. 176) y Fondo de Cohesión (art. 177)", "FEDER: desequilibrios regionales. FC: proyectos de medio ambiente y redes transeuropeas de transporte.", "Cohesión"),
  ("Categorías de regiones (Reglamento 2021/1060, art. 108)", "Menos desarrolladas < 75 %; en transición 75-100 %; más desarrolladas > 100 % del PIB per cápita; FC: Estados con RNB < 90 %.", "Cohesión"),
  ("Informe sobre la cohesión (art. 175)", "Cada tres años, de la Comisión.", "Cohesión"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Recursos propios", "Ingresos que financian íntegramente el presupuesto de la Unión (art. 311 TFUE); categorías fijadas por la Decisión 2020/2053.", "s3", "Recursos propios")
T.glos("Recursos propios tradicionales", "Exacciones y derechos de aduana en los intercambios comerciales con terceros países, y cotizaciones y otros derechos de la organización común de mercados del azúcar (Decisión 2020/2053, art. 2.1 a); los Estados retienen el 25 % como gastos de recaudación.", "s4", "Recursos propios")
T.glos("Principio de universalidad", "Los ingresos se utilizan indistintamente para financiar todos los gastos del presupuesto (Decisión 2020/2053, art. 7).", "s4", "Recursos propios")
T.glos("Marco financiero plurianual (MFP)", "Reglamento del Consejo que fija, para un mínimo de cinco años, los límites máximos anuales de créditos para compromisos y para pagos (art. 312 TFUE). Vigente: 2021-2027.", "s5", "Marco financiero plurianual")
T.glos("Créditos de compromiso y de pago", "Límites del MFP por categoría de gastos (compromisos) y global (pagos) (art. 312.3 TFUE).", "s5", "Marco financiero plurianual")
T.glos("Comité de Conciliación", "Órgano del procedimiento presupuestario formado por miembros del Consejo y un número igual de representantes del Parlamento; 21 días para acordar un texto conjunto (art. 314.5 TFUE).", "s7", "Procedimiento presupuestario")
T.glos("Doceavas partes", "Régimen de gasto mensual por capítulos cuando el presupuesto no se ha adoptado al iniciarse el ejercicio (art. 315 TFUE).", "s7", "Procedimiento presupuestario")
T.glos("Aprobación de la gestión", "Decisión del Parlamento Europeo, por recomendación del Consejo, sobre la ejecución del presupuesto por la Comisión (art. 319 TFUE).", "s8", "Ejecución y control")
T.glos("Fondo Social Europeo (FSE+)", "Fondo creado por el art. 162 TFUE para el empleo y la adaptación de los trabajadores; en 2021-2027, FSE+ (Reglamento 2021/1057).", "s10", "Fondos europeos")
T.glos("Reglamento de disposiciones comunes (RDC)", "Reglamento (UE) 2021/1060: normas financieras de ocho fondos y disposiciones comunes del FEDER, FSE+, Fondo de Cohesión, FTJ y FEMPA.", "s11", "Fondos europeos")
T.glos("Feader", "Fondo Europeo Agrícola de Desarrollo Rural; financia las intervenciones de desarrollo rural, en gestión compartida (Reglamento 2021/2116, art. 6).", "s13", "Fondos europeos")
T.glos("Mecanismo de Recuperación y Resiliencia (MRR)", "Instrumento del Reglamento (UE) 2021/241 que da ayuda financiera a las reformas e inversiones de los planes de recuperación y resiliencia; seis pilares.", "s14", "Fondos europeos")
T.glos("FEDER", "Fondo Europeo de Desarrollo Regional: corrección de los principales desequilibrios regionales (art. 176 TFUE).", "s17", "Cohesión")
T.glos("Fondo de Cohesión", "Fondo que financia proyectos de medio ambiente y de redes transeuropeas de transporte (art. 177 TFUE); para Estados con RNB per cápita inferior al 90 % de la media (RDC, art. 108.3).", "s17", "Cohesión")
T.glos("Regiones en transición", "Regiones NUTS 2 con PIB per cápita entre el 75 % y el 100 % de la media de la UE-27 (RDC, art. 108.2 b).", "s18", "Cohesión")

# Cronología (fechas de los títulos y del Diario Oficial que da EUR-Lex)
T.hito("2020", "Decisión (UE, Euratom) 2020/2053 del Consejo, de 14 de diciembre de 2020, sobre el sistema de recursos propios (DO L 424 de 15.12.2020)", "Recursos propios del período 2021-2027 y empréstitos por la COVID-19", "normativo", "s4")
T.hito("2020", "Reglamento (UE, Euratom) 2020/2093 del Consejo, de 17 de diciembre de 2020 (DO L 433I de 22.12.2020)", "Marco financiero plurianual 2021-2027", "normativo", "s6")
T.hito("2021", "Reglamento (UE) 2021/241, de 12 de febrero de 2021 (DO L 057 de 18.2.2021)", "Mecanismo de Recuperación y Resiliencia", "normativo", "s14")
T.hito("2021", "Reglamento (UE) 2021/695, de 28 de abril de 2021 (DO L 170 de 12.5.2021)", "Programa Marco Horizonte Europa 2021-2027", "normativo", "s14")
T.hito("2021", "Reglamentos (UE) 2021/1057, 2021/1058 y 2021/1060, de 24 de junio de 2021 (DO L 231 de 30.6.2021)", "FSE+, FEDER y Fondo de Cohesión, y disposiciones comunes de los fondos", "normativo", "s11")
T.hito("2021", "Reglamento (UE) 2021/2116, de 2 de diciembre de 2021 (DO L 435 de 6.12.2021)", "Financiación de la PAC: FEAGA y Feader", "normativo", "s13")

T.publicar()
