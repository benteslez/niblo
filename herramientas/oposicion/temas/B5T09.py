# -*- coding: utf-8 -*-
"""Tema V.9 (B5T09): El régimen especial de la Seguridad Social de los funcionarios civiles
del Estado. MUFACE y las clases pasivas: acción protectora. Concepto y clases de prestaciones.
Derechos pasivos.
Método del I.2. Normas (textos consolidados del BOE): RDLeg 4/2000 (texto refundido de la
Ley sobre Seguridad Social de los Funcionarios Civiles del Estado); RD 375/2003 (Reglamento
General del Mutualismo Administrativo); RD 577/1997 (Estatuto de MUFACE, en la redacción del
RD 466/2026); RD 466/2026 (art. tercero); RDLeg 670/1987 (texto refundido de Ley de Clases
Pasivas del Estado); RDLeg 8/2015 (LGSS), disposición adicional tercera; RDL 13/2010, art. 20
(derogado: solo se cita su estado)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO.update({"MUF": "RDLeg 4/2000", "RD375": "RD 375/2003", "RDL670": "RDLeg 670/1987", "LGSS": "LGSS",
              "RD577": "RD 577/1997", "RD466_2026": "RD 466/2026", "RDL13_2010": "RDL 13/2010"})

T = Tema("B5T09",
  "Cuatro preguntas: I. Qué es el régimen especial de los funcionarios civiles del Estado y a quién protege (RDLeg 4/2000, arts. 1 a 3, 7 y 8; LGSS, disp. adic. 3.ª; RD 375/2003, art. 13) · II. Qué es MUFACE y cómo se financia (RDLeg 4/2000, arts. 4, 5, 10, 34, 37 y disp. adic. 6.ª; Estatuto de MUFACE, RD 577/1997; RD 466/2026) · III. Qué protege el mutualismo: concepto y clases de prestaciones (RDLeg 4/2000, arts. 11 a 19, 21 a 26 y 28 a 31; RD 375/2003) · IV. Qué protegen las Clases Pasivas: derechos pasivos y pensiones (RDLeg 670/1987). Cada artículo: texto literal del BOE y ficha.",
  ["MUFACE", "RDLeg 4/2000", "RD 375/2003", "Mutualismo administrativo", "Clases Pasivas", "RDLeg 670/1987", "Régimen General desde 2011", "Asistencia sanitaria", "Incapacidad temporal", "Gran invalidez", "Fondo especial", "Derechos pasivos", "Pensiones extraordinarias", "INSS"])

# =============================================================================
T.ap("s0", "Mapa del tema: cuatro preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque V, tema 9):
> El régimen especial de la Seguridad Social de los funcionarios civiles del Estado. MUFACE y las clases pasivas: acción protectora. Concepto y clases de prestaciones. Derechos pasivos.

### El hilo conductor

El epígrafe se lee como **cuatro preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Normas |
|---|---|---|
| **I** | ¿Qué es el régimen especial y a quién protege? | RDLeg 4/2000, arts. 1 a 3, 7 y 8; LGSS, disposición adicional tercera; RD 375/2003, art. 13 |
| **II** | ¿Qué es MUFACE y cómo se financia? | RDLeg 4/2000, arts. 4, 5, 10, 34, 37 y disposición adicional sexta; RD 577/1997 (Estatuto de MUFACE), arts. 1, 4 y 6; RD 466/2026, art. tercero |
| **III** | ¿Qué protege el mutualismo administrativo? (acción protectora, concepto y clases de prestaciones) | RDLeg 4/2000, arts. 11 a 19, 21 a 26 y 28 a 31; RD 375/2003, arts. 50, 53, 54, 66, 129 y 137 |
| **IV** | ¿Qué protegen las Clases Pasivas? (acción protectora y derechos pasivos) | RDLeg 670/1987, arts. 1, 2, 5 a 7, 11, 12, 14, 18, 19, 23, 28 a 31, 34, 35, 38, 39, 41, 44, 47 a 49 |

!> **La idea que une los cuatro bloques:** el régimen especial de los funcionarios civiles del Estado tiene **dos mecanismos de cobertura** (I): las **Clases Pasivas** (pensiones: jubilación y muerte y supervivencia) y el **mutualismo administrativo** que gestiona **MUFACE** (II). El mutualismo da asistencia sanitaria, subsidios y otras prestaciones (III); las Clases Pasivas, los **derechos pasivos** (IV). Desde el **1 de enero de 2011**, el personal de nuevo ingreso queda en el **Régimen General** a efectos de pensiones, no en Clases Pasivas (→ I.1).

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha**: de **institución o procedimiento** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen) o de **derecho/prestación** (Titulares · Contenido · Límites · Protección · ⚠ Ojo en el examen).
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- Algunas normas usan denominaciones de ministerios ya desaparecidos (p. ej., «Ministerio de Administraciones Públicas»): se copian **literales**, tal como están en el texto consolidado.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
- Relacionados: situaciones administrativas (tema V.5); retribuciones (tema V.6); jubilación como pérdida de la condición de funcionario (tema V.1).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué es el régimen especial y a quién protege? (RDLeg 4/2000, arts. 1 a 3, 7 y 8; LGSS, disp. adic. 3.ª; RD 375/2003, art. 13)", donde(
  "Primera pregunta del tema. Antes de ver las prestaciones hay que saber **qué es** el régimen especial, **con qué mecanismos** protege, **a quién** incluye y **desde cuándo** el nuevo personal pasa al Régimen General.",
  ["1 Régimen especial y mecanismos de cobertura; el Régimen General desde 2011", "2 Campo de aplicación: incluidos y excluidos", "3 Afiliación, alta, baja y mantenimiento como mutualista"]))

T.ap("s1", "I.1 Régimen especial y mecanismos de cobertura; el Régimen General desde 2011 (RDLeg 4/2000, arts. 1 y 2; LGSS, disp. adic. 3.ª)", f"""
{unidad("1.1 Normas del régimen especial (art. 1)",
  lit("MUF", "a1", ["así como por la legislación de Clases Pasivas del Estado"]),
  fichab("El Régimen especial de la Seguridad Social de los Funcionarios Civiles del Estado",
         "—",
         f"Se rige por {c('MUF', 'a1', 'lo dispuesto en la presente Ley y en sus normas de aplicación y desarrollo')} y por la legislación de Clases Pasivas",
         "—",
         "Son **dos** bloques normativos: la ley del mutualismo (RDLeg 4/2000, desarrollada por el RD 375/2003) y la **legislación de Clases Pasivas** (RDLeg 670/1987)."))}

{unidad("1.2 Dos mecanismos de cobertura y el Régimen General desde 2011 (art. 2)",
  lit("MUF", "a2", ["El Régimen de Clases Pasivas del Estado", "El Régimen del Mutualismo Administrativo", "hayan ingresado a partir del 1 de enero de 2011", "a los exclusivos efectos de pensiones"]),
  fichab("Composición del Régimen especial",
         "Funcionarios de carrera de la Administración Civil del Estado (→ I.2)",
         [f"::{c('MUF', 'a2', 'Este Régimen especial queda integrado por los siguientes mecanismos de cobertura')}:", "Clases Pasivas del Estado, con sus normas específicas (→ IV.1)", "Mutualismo Administrativo, regulado en el RDLeg 4/2000 (→ III.1)"],
         f"Ingreso {c('MUF', 'a2', 'a partir del 1 de enero de 2011')} → Régimen General {c('MUF', 'a2', 'a los exclusivos efectos de pensiones')}",
         "Desde 2011 el nuevo funcionario **no** entra en Clases Pasivas: pensiones en el **Régimen General**; el mutualismo (MUFACE) lo sigue teniendo. El art. 2.2 remite al art. 20.1 del RDL 13/2010, hoy derogado (→ I.1.3)."))}

{unidad("1.3 La regla vigente: LGSS, disposición adicional tercera",
  lit("LGSS", "datercera", ["Con efectos de 1 de enero de 2011", "excepción hecha del comprendido en la letra i)", "en el Régimen General de la Seguridad Social siempre que el acceso a la condición de que se trate se produzca a partir de aquella fecha", "continuará incluido en dicho régimen"], solo=[1, 2, 5, 6]),
  fichab("Inclusión en el Régimen General de los funcionarios públicos y otro personal de nuevo ingreso",
         f"El personal del art. 2.1 del texto refundido de Clases Pasivas (→ IV.1.2), {c('LGSS', 'datercera', 'excepción hecha del comprendido en la letra i)')} (ex Presidentes, Vicepresidentes y Ministros y otros cargos del art. 51)",
         ["Inclusión obligatoria en el Régimen General a los efectos de lo dispuesto en el texto de Clases Pasivas", "Se respetan la edad de jubilación forzosa y los tribunales médicos de cada colectivo (apartado 2)", "Quien estaba en Clases Pasivas a 31-12-2010 y, sin solución de continuidad, ingresa o reingresa en otro Cuerpo que hubiera motivado ese encuadramiento, sigue en Clases Pasivas (apartado 3)"],
         f"Efectos: {c('LGSS', 'datercera', 'Con efectos de 1 de enero de 2011')}; para accesos {c('LGSS', 'datercera', 'a partir de aquella fecha')}",
         f"El art. 20 del RDL 13/2010, que introdujo la regla, figura hoy en el texto consolidado como {c('RDL13_2010', 'a20', '(Derogado)')}: la norma vigente es la **disposición adicional tercera de la LGSS**. Cayó en 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s2", "I.2 Campo de aplicación: incluidos y excluidos (RDLeg 4/2000, art. 3; RD 375/2003, art. 13)", f"""
{unidad("2.1 Quién está incluido y quién excluido (art. 3)",
  lit("MUF", "a3", ["Los funcionarios de carrera de la Administración Civil del Estado.", "Los funcionarios en prácticas que aspiren a incorporarse a Cuerpos de la Administración Civil del Estado", "Quedan excluidos de este Régimen especial"]),
  fichab("Ámbito personal del Régimen especial",
         ["::Incluidos obligatoriamente (3.1):", "Funcionarios de carrera de la Administración Civil del Estado", "Funcionarios en prácticas que aspiren a incorporarse a esos Cuerpos"],
         ["::Excluidos, con sus normas específicas (3.2):", "Administración Local; organismos autónomos; Administración Militar; Administración de Justicia; Administración de la Seguridad Social", "Funcionarios de nuevo ingreso y en prácticas de las CC. AA.", "Funcionarios del Estado transferidos que ingresen en Cuerpos o Escalas propios de la CA", "PAS propio de las universidades"],
         "—",
         "Los **funcionarios en prácticas** están **incluidos**; los de **organismos autónomos**, **Justicia** y **Local**, **excluidos**. Cayó en 2025 (→ Cierre 1). Hay supuestos especiales de afiliación en la disposición adicional primera (p. ej., interinos del Decreto-ley 10/1965)."))}

{unidad("2.2 Funcionarios en prácticas (RD 375/2003, art. 13)",
  lit("RD375", "Artículo 13", ["en las mismas condiciones que los funcionarios de carrera hasta la fecha de su toma de posesión como tales", "con efectos del día de inicio del período de prácticas"]),
  fichab("Inclusión de los funcionarios en prácticas en el mutualismo",
         "Funcionarios en prácticas que aspiren a ingresar en Cuerpos de la Administración Civil del Estado",
         "Afiliación a MUFACE en las mismas condiciones que los de carrera; si no llegan a ser de carrera, causan baja",
         f"Efectos: {c('RD375', 'Artículo 13', 'con efectos del día de inicio del período de prácticas')}",
         "Se afilian desde el **inicio de las prácticas**, no desde la toma de posesión como funcionarios de carrera."))}
""", 2)

T.ap("s3", "I.3 Afiliación, alta, baja y mantenimiento como mutualista (RDLeg 4/2000, arts. 7 y 8)", f"""
{unidad("3.1 Incorporación obligatoria y situaciones en que se conserva (art. 7)",
  lit("MUF", "a7", ["en el momento de la toma de posesión de su cargo", "Expectativa de destino.", "Excedencia por el cuidado de familiares.", "por una sola vez, en el plazo de quince días desde la toma de posesión en el nuevo Cuerpo o Escala", "no comportará, en ningún caso, su inclusión en el Régimen de Clases Pasivas del Estado"]),
  fichab("Incorporación a MUFACE como mutualista",
         "Funcionarios de carrera de la Administración Civil del Estado",
         ["::Se incorporan obligatoriamente al tomar posesión, al adquirir la condición, al ser rehabilitados o al reingresar al servicio activo. Conservan la condición, con los mismos derechos y obligaciones, en:", "Servicios especiales (salvo art. 8.1 c y 8.3)", "Servicios en Comunidades Autónomas", "Expectativa de destino", "Excedencia forzosa", "Excedencia por el cuidado de familiares", "Suspensión provisional o firme de funciones", "Y también al ser jubilados (7.2)"],
         f"Opción por seguir siendo mutualista tras promoción interna a Escalas de organismos autónomos o de la CA de destino (7.3): {c('MUF', 'a7', 'por una sola vez, en el plazo de quince días desde la toma de posesión en el nuevo Cuerpo o Escala')}",
         "La excedencia **por cuidado de familiares** conserva la condición; la excedencia **voluntaria** causa baja (→ I.3.2). Quien mantiene el mutualismo por la opción del 7.3 **no** entra en Clases Pasivas."))}

{unidad("3.2 Baja, mantenimiento facultativo y suspensión del alta (art. 8)",
  lit("MUF", "a8", ["excedencia voluntaria, en cualquiera de sus modalidades", "Los funcionarios que pierdan tal condición, cualquiera que sea la causa.", "siempre que abonen exclusivamente a su cargo las cuotas correspondientes al funcionario y al Estado", "Podrán optar por suspender el alta"]),
  fichab("Fin del alta obligatoria, mutualistas voluntarios y suspensión del alta",
         "Funcionarios en excedencia voluntaria, quienes pierden la condición de funcionario y los demás supuestos del 8.1",
         ["::Causan baja como mutualistas obligatorios (8.1):", "Excedencia voluntaria, en cualquiera de sus modalidades (salvo la opción del art. 7.3)", "Pérdida de la condición de funcionario, cualquiera que sea la causa", "Ejercicio del derecho de transferencia del Estatuto de los Funcionarios de las Comunidades Europeas", "Afiliación obligatoria al Régimen especial de la Seguridad Social de las Fuerzas Armadas (disp. trans. 14.ª de la Ley 17/1999)"],
         "Supuestos de las letras a), b) y c) del 8.1: pueden seguir como **mutualistas voluntarios** pagando las dos cuotas (la del funcionario y la del Estado) (8.2). Suspensión del alta (8.3): opcional en servicios especiales en la Unión Europea u otra organización internacional, si están acogidos obligatoriamente a su régimen de previsión",
         "El mutualista voluntario paga **las dos** cuotas, «exclusivamente a su cargo»."))}

{resumen([
  "El régimen especial se rige por el RDLeg 4/2000 y por la legislación de **Clases Pasivas** (art. 1); tiene **dos** mecanismos: **Clases Pasivas** y **mutualismo administrativo** (art. 2.1).",
  "Ingreso **desde el 1-1-2011** → **Régimen General** a los exclusivos efectos de **pensiones** (art. 2.2; LGSS, disp. adic. 3.ª).",
  "Incluidos: funcionarios **de carrera** de la Administración Civil del Estado y **en prácticas**; excluidos: Local, **organismos autónomos**, Militar, **Justicia**, Seguridad Social, CC. AA. (nuevo ingreso), universidades (PAS) (art. 3).",
  "Alta al **tomar posesión**; se conserva en servicios especiales, servicios en CC. AA., expectativa de destino, excedencia forzosa y por cuidado de familiares y suspensión; la **excedencia voluntaria** causa baja (arts. 7 y 8)."],
  "Siguiente: II. ¿Qué es MUFACE y cómo se financia?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Qué es MUFACE y cómo se financia? (RDLeg 4/2000, arts. 4, 5, 10, 34, 37 y disp. adic. 6.ª; Estatuto de MUFACE; RD 466/2026)", donde(
  "Segunda pregunta. El mutualismo administrativo lo **gestiona MUFACE**. Hay que saber qué tipo de organismo es, qué órganos tiene, de qué recursos vive (cotizaciones, aportación del Estado, Fondo especial) y cómo se recurren sus actos.",
  ["1 Naturaleza, adscripción y órganos de MUFACE", "2 Cotización, recursos económicos y Fondo especial", "3 Recursos contra los actos de MUFACE"]))

T.ap("s4", "II.1 Naturaleza, adscripción y órganos de MUFACE (RDLeg 4/2000, arts. 4 y 5; RD 577/1997, arts. 1, 4 y 6; RD 466/2026)", f"""
{unidad("1.1 Gestión del mutualismo por MUFACE (art. 4)",
  lit("MUF", "a4", ["Mutualidad General de Funcionarios Civiles del Estado (MUFACE)", "de forma unitaria"]),
  fichab("Gestión del mutualismo administrativo",
         c("MUF", "a4", "Mutualidad General de Funcionarios Civiles del Estado (MUFACE)"),
         f"Gestión {c('MUF', 'a4', 'de forma unitaria')}, sin perjuicio de las obligaciones de las CC. AA. respecto de los funcionarios transferidos",
         "—",
         "Una sola entidad gestora del mutualismo: **MUFACE**. La adscripción que cita la ley («Ministerio de Administraciones Públicas») está actualizada en el Estatuto (→ II.1.2)."))}

{unidad("1.2 Naturaleza jurídica y adscripción (art. 5 RDLeg 4/2000 y art. 1 del Estatuto)",
  lit("MUF", "a5", ["organismo público con personalidad jurídica pública diferenciada, patrimonio y tesorería propios y autonomía de gestión"], solo=[1]),
  lit("RD577", "a1", ["organismo autónomo de los previstos en el artículo 98.1 de la Ley 40/2015", "adscrito a través de la Secretaría de Estado de Función Pública", "Mutualidad General de Funcionarias y Funcionarios Civiles del Estado, O.A. (MUFACE)"], solo=[1, 2]),
  fichab("MUFACE como organismo autónomo",
         f"{c('RD577', 'a1', 'adscrito a través de la Secretaría de Estado de Función Pública al Ministerio del que ésta dependa')}",
         "Personalidad jurídica diferenciada, tesorería y patrimonio propios y autonomía en su gestión",
         "—",
         f"Es un **organismo autónomo** (art. 98.1 Ley 40/2015). Desde el RD 466/2026 su denominación es {c('RD577', 'a1', 'Mutualidad General de Funcionarias y Funcionarios Civiles del Estado, O.A. (MUFACE)')} y las referencias a la antigua denominación {c('RD577', 'da', 'se entenderán hechas a la Mutualidad General de Funcionarias y Funcionarios Civiles del Estado')}."))}

{unidad("1.3 Órganos de gobierno y órgano ejecutivo (Estatuto, arts. 4 y 6)",
  lit("RD577", "a4", ["La Presidencia.", "El Consejo Rector, que recibe la denominación de Consejo General.", "El órgano ejecutivo del organismo autónomo es la Dirección."], solo=[1, 2, 3, 4]),
  lit("RD577", "a6-2", ["corresponde a la persona titular de la Secretaría de Estado de Función Pública", "agotan la vía administrativa"], solo=[1, 6], titulo="Artículo 6 [sic]. Presidencia (RD 577/1997)"),
  fichab("Gobierno y dirección de MUFACE",
         ["::Órganos de gobierno: la **Presidencia** y el **Consejo General** (Consejo Rector)", "Órgano ejecutivo: la **Dirección**", "Presidencia: la persona titular de la **Secretaría de Estado de Función Pública**"],
         "Consejo General con representantes de la Administración y nueve de los funcionarios designados por los sindicatos de la Mesa General de Negociación de la AGE (art. 5.1)",
         "—",
         "La norma que regula estos órganos es el **RD 577/1997**: hoy titulado Estatuto de MUFACE (→ II.1.4). Los actos de la **Presidencia** agotan la vía administrativa (art. 6 [sic].3)."))}

{unidad("1.4 El RD 577/1997 y su nuevo título (RD 466/2026, art. tercero)",
  lit("RD466_2026", "at", ["por el que se establece la estructura de los órganos de gobierno, administración y representación de la Mutualidad General de Funcionarios Civiles del Estado", "por el que se aprueba el Estatuto de la Mutualidad General de Funcionarias y Funcionarios Civiles del Estado, O.A."], solo=[1, 2, 3], titulo="Artículo tercero. Modificación del Real Decreto 577/1997, de 18 de abril, por el que se establece la estructura de los órganos de gobierno, administración y representación de la Mutualidad General de Funcionarios Civiles del Estado (MUFACE) (RD 466/2026)"),
  fichab("La norma de organización de MUFACE",
         "El Gobierno (real decreto)",
         "El RD 577/1997 nació como norma que establece la estructura de los órganos de gobierno, administración y representación de MUFACE; el RD 466/2026 cambia su título y lo convierte en el Estatuto del organismo",
         "—",
         "Pregunta de 2025 (X 85): la norma por la que «se establece la estructura de los órganos de gobierno, administración y representación de la Mutualidad General de Funcionarios Civiles del Estado (MUFACE)» es el **RD 577/1997** (→ Cierre 1)."))}
""", 2)

T.ap("s5", "II.2 Cotización, recursos económicos y Fondo especial (RDLeg 4/2000, arts. 10, 34 y disp. adic. 6.ª)", f"""
{unidad("2.1 Régimen de cotización de los mutualistas (art. 10)",
  lit("MUF", "a10", ["con excepción de los mutualistas jubilados y de quienes se encuentren en la situación de excedencia voluntaria para atender al cuidado de hijos o familiares", "haber regulador en la Ley de Presupuestos Generales del Estado", "dividiendo por catorce", "se abonará doblemente en los meses de junio y diciembre", "prescribirá a los cuatro años"], solo=[1, 2, 3, 4, 8]),
  fichab("Cotización obligatoria a MUFACE",
         f"Todos los mutualistas, {c('MUF', 'a10', 'con excepción de los mutualistas jubilados y de quienes se encuentren en la situación de excedencia voluntaria para atender al cuidado de hijos o familiares')}",
         ["Base: el **haber regulador** de la Ley de Presupuestos", "Tipo: fijado en la Ley de Presupuestos de cada ejercicio", "Cuota mensual: la anual dividida por **catorce**, doble en **junio y diciembre**"],
         f"Prescripción de la obligación de pago: {c('MUF', 'a10', 'a los cuatro años')}",
         "No cotizan los **jubilados** ni los excedentes **para cuidado de hijos o familiares**. Prescripción y devolución de cuotas: **cuatro** años."))}

{unidad("2.2 Recursos económicos de MUFACE (art. 34)",
  lit("MUF", "a34", ["Las aportaciones económicas del Estado", "Las cuotas de los mutualistas.", "Los bienes, derechos y acciones de las Mutualidades y Montepíos integrados en el Fondo especial"]),
  fichab("Financiación de MUFACE",
         "MUFACE (recursos); el Estado (aportaciones y subvenciones)",
         ["Aportaciones económicas del Estado (art. 35: porcentaje sobre los haberes reguladores fijado en la Ley de Presupuestos)", "Cuotas de los mutualistas", "Subvenciones estatales y otros recursos públicos", "Bienes, derechos y acciones del Fondo especial", "Frutos y rentas de su patrimonio; otros recursos privados"],
         "—",
         f"El sistema financiero del régimen es {c('MUF', 'a33', 'de reparto y su cuota revisable periódicamente')} (art. 33.1)."))}

{unidad("2.3 El Fondo especial (disposición adicional sexta)",
  lit("MUF", "dasexta", ["constituye un Fondo especial", "No podrán incorporarse nuevos socios"], solo=[4, 5, 6]),
  fichab("Fondo especial de MUFACE",
         "Socios y beneficiarios de las Mutualidades, Asociaciones y Montepíos integrados en MUFACE",
         f"Lo forman {c('MUF', 'dasexta', 'La totalidad de los bienes, derechos y acciones de las Mutualidades, Asociaciones y Montepíos aportados con su integración a la Mutualidad General de Funcionarios Civiles del Estado')}, más las cuotas de los mutualistas afectados y los recursos públicos que les correspondan",
         "Su déficit lo cubre una **subvención del Estado** (apartado 3)",
         "Cayó en 2025 como pregunta de reserva (→ Cierre 1). Es un fondo **cerrado**: no admite nuevos socios; la baja voluntaria se puede pedir en cualquier momento, sin devolución de cuotas."))}
""", 2)

T.ap("s6", "II.3 Recursos contra los actos de MUFACE (RDLeg 4/2000, art. 37)", f"""
{unidad("3.1 Alzada y vía contencioso-administrativa (art. 37)",
  lit("MUF", "a37", ["no ponen fin a la vía administrativa, pudiéndose recurrir en alzada", "las dictadas en materia de personal por el Director general de la Mutualidad", "serán resueltas por el Director general"]),
  fichab("Revisión de los actos del Director general de MUFACE",
         "El Director general (dicta); el Ministro (resuelve la alzada)",
         ["Regla: **no** ponen fin a la vía administrativa → **alzada**", "Excepción (37.2): las resoluciones del art. 109 a) y b) de la Ley 30/1992 y las de **personal** → ponen fin a la vía: reposición potestativa y contencioso", "Reclamaciones previas civiles y laborales: las resuelve el Director general"],
         "—",
         "La regla de MUFACE es la **alzada**, al revés que en Clases Pasivas, donde los acuerdos del INSS **ponen fin** a la vía administrativa (→ IV.3.2)."))}

{resumen([
  "MUFACE gestiona el mutualismo **de forma unitaria** (art. 4); es un **organismo autónomo** adscrito a través de la **Secretaría de Estado de Función Pública** (Estatuto, art. 1).",
  "Órganos de gobierno: **Presidencia** (titular de la Secretaría de Estado de Función Pública) y **Consejo General**; órgano ejecutivo: la **Dirección** (Estatuto, arts. 4 y 6). La norma: **RD 577/1997**, retitulado por el RD 466/2026.",
  "Cotizan todos los mutualistas salvo **jubilados** y excedentes **por cuidado de hijos o familiares**; cuota anual ÷ **14**, doble en junio y diciembre; prescripción a los **cuatro años** (art. 10).",
  "**Fondo especial**: bienes de las Mutualidades, Asociaciones y Montepíos integrados; sin nuevos socios (disp. adic. 6.ª).",
  "Actos del Director general: **alzada** ante el Ministro, salvo los del art. 37.2 (art. 37)."],
  "Siguiente: III. ¿Qué protege el mutualismo administrativo?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Qué protege el mutualismo administrativo? Concepto y clases de prestaciones (RDLeg 4/2000, arts. 11 a 19, 21 a 26 y 28 a 31; RD 375/2003)", donde(
  "Tercera pregunta: la **acción protectora** de MUFACE. La ley enumera primero las **contingencias** (situaciones protegidas) y después las **prestaciones** con que las cubre. Cada prestación se estudia en su artículo.",
  ["1 Contingencias y prestaciones: la lista legal", "2 Asistencia sanitaria", "3 Incapacidad temporal y riesgo durante el embarazo o la lactancia", "4 Incapacidad permanente y lesiones permanentes no invalidantes", "5 Protección a la familia, servicios sociales y asistencia social", "6 Reglas comunes de las prestaciones y cuadro"]))

T.ap("s7", "III.1 Contingencias y prestaciones: la lista legal (RDLeg 4/2000, arts. 11 y 12)", f"""
{unidad("1.1 Contingencias protegidas (art. 11)",
  lit("MUF", "a11", ["Necesidad de asistencia sanitaria.", "Incapacidad temporal", "Incapacidad permanente", "Cargas familiares.", "donación de órganos o tejidos"]),
  fichab("Situaciones de necesidad que cubre el mutualismo",
         "Los mutualistas y, en su caso, los familiares o asimilados a su cargo",
         ["Necesidad de asistencia sanitaria", "Incapacidad temporal (enfermedad común o profesional; accidente común o en acto de servicio)", "Incapacidad permanente", "Cargas familiares", "IT especial por donación de órganos o tejidos (art. 18)"],
         "—",
         "La **jubilación** y la **muerte y supervivencia** no están en el art. 11: son de **Clases Pasivas** (→ IV.1)."))}

{unidad("1.2 Prestaciones (art. 12)",
  lit("MUF", "a12", ["Asistencia sanitaria.", "Subsidios por incapacidad temporal", "Prestaciones recuperadoras", "Servicios sociales.", "Asistencia social.", "Ayudas económicas en los casos de parto múltiple."], solo=list(range(1, 12))),
  ficha("Los mutualistas o sus beneficiarios, en los supuestos de hecho legalmente establecidos",
        ["Asistencia sanitaria", "Subsidios por IT (incluidas la IT por donación, el riesgo durante el embarazo y durante la lactancia natural)", "Prestaciones recuperadoras por incapacidad permanente total, absoluta y gran invalidez", "Remuneración de la persona que asiste al gran inválido", "Indemnizaciones por lesiones, mutilaciones o deformidades (enfermedad profesional o acto de servicio)", "Servicios sociales", "Asistencia social", "Prestaciones familiares por hijo a cargo minusválido", "Ayudas económicas por parto múltiple"],
        "Las prestaciones de pago económico se abonan únicamente en la cuenta corriente o libreta abierta a nombre del titular (12.2)",
        "—",
        "Son **nueve** prestaciones (letras a a i). La pensión de **jubilación no** es prestación de MUFACE."))}
""", 2)

T.ap("s8", "III.2 Asistencia sanitaria (RDLeg 4/2000, arts. 13 a 17; RD 375/2003, art. 66)", f"""
{unidad("2.1 Objeto y contingencias cubiertas (arts. 13 y 14)",
  lit("MUF", "a13", ["servicios médicos, quirúrgicos y farmacéuticos"], solo=[1]),
  lit("MUF", "a14", ["así como el embarazo, el parto y el puerperio"]),
  lit("RD375", "Artículo 66", ["así como el embarazo, el parto y el puerperio"]),
  ficha("Mutualistas, jubilados mutualistas y beneficiarios de ambos (art. 15.1)",
        f"{c('MUF', 'a13', 'la prestación de los servicios médicos, quirúrgicos y farmacéuticos conducentes a conservar o restablecer la salud de los beneficiarios de este Régimen especial, así como su aptitud para el trabajo')}",
        "Cubre enfermedad común o profesional, accidente común o en acto de servicio, IT por donación, **embarazo, parto y puerperio**",
        "—",
        "El **embarazo** es contingencia cubierta por la **asistencia sanitaria** (ley, art. 14; reglamento, art. 66). Cayó en 2025 (→ Cierre 1)."))}

{unidad("2.2 Beneficiarios y el recién nacido (art. 15)",
  lit("MUF", "a15", ["a todos los mutualistas incluidos en el ámbito de aplicación de este Régimen especial y jubilados mutualistas", "durante los primeros quince días desde el momento del parto"], solo=[1, 4]),
  ficha("Mutualistas, jubilados mutualistas y sus beneficiarios",
        "Asistencia sanitaria",
        "MUFACE no da asistencia a familiares no reconocidos como beneficiarios, salvo el recién nacido y los adoptados o acogidos, los **primeros quince días**",
        "La condición de beneficiario a cargo en MUFACE es incompatible con la de asegurado o beneficiario del Sistema Nacional de Salud reconocida por otro organismo (15.2)",
        "Recién nacido: **quince días** desde el parto (si la madre es mutualista o beneficiaria)."))}

{unidad("2.3 Contenido y forma de la prestación (arts. 16 y 17)",
  lit("MUF", "a16", ["con un contenido análogo al establecido para los beneficiarios del Sistema Nacional de Salud", "mediante el pago de una cantidad porcentual por receta"], solo=[1, 2, 3]),
  lit("MUF", "a17", ["bien directamente o por concierto con otras entidades o establecimientos públicos o privados", "preferentemente con instituciones de la Seguridad Social"], solo=[1]),
  fichab("Cómo presta MUFACE la asistencia sanitaria",
         c("MUF", "a17", "La asistencia sanitaria se facilitará por la Mutualidad General de Funcionarios Civiles del Estado"),
         ["Atención primaria y especializada con contenido **análogo al del Sistema Nacional de Salud**", "Prestación farmacéutica con participación del beneficiario por receta o medicamento", "Prestaciones complementarias"],
         "—",
         "**Directamente o por concierto**; los conciertos, **preferentemente** con instituciones de la **Seguridad Social**."))}
""", 2)

T.ap("s9", "III.3 Incapacidad temporal y riesgo durante el embarazo o la lactancia (RDLeg 4/2000, arts. 18, 19, 21 y 22)", f"""
{unidad("3.1 Qué es incapacidad temporal y qué no (art. 18)",
  lit("MUF", "a18", ["los de enfermedad, accidente y los denominados períodos de observación en caso de enfermedad profesional", "no tendrán la consideración de incapacidad temporal"], solo=[1, 2, 3]),
  ficha("Funcionarios incluidos en el Régimen especial",
        "Estados determinantes de IT: **enfermedad**, **accidente** y **períodos de observación** por enfermedad profesional; además, la IT especial por donación de órganos o tejidos",
        f"{c('MUF', 'a18', 'Los permisos o licencias por parto, adopción o acogimiento')} y los de paternidad **no** son IT",
        "Si al terminar el permiso por parto continúa la imposibilidad de incorporarse, se inician las licencias de IT",
        "Los **permisos por parto, adopción o acogimiento y paternidad no** son IT. Cayó en 2025 (→ Cierre 1)."))}

{unidad("3.2 Situación de IT y licencias (art. 19)",
  lit("MUF", "a19", ["hayan obtenido licencia por enfermedad", "corresponderá a los órganos administrativos con competencia en materias de gestión de personal", "Unidades Médicas de Seguimiento"], solo=[1, 4, 6]),
  fichab("Reconocimiento y control de la incapacidad temporal",
         ["Licencias: los **órganos de personal**", "Control y seguimiento: también MUFACE, con sus Unidades Médicas de Seguimiento"],
         "Requisitos: proceso patológico que impida temporalmente el desempeño + asistencia sanitaria de MUFACE + **licencia por enfermedad**",
         "Duración y extinción: las del Régimen General, con las particularidades del art. 20",
         "La licencia la **conceden los órganos de personal**, no MUFACE. Los reconocimientos de las Unidades Médicas de Seguimiento son potestativos pero **vinculan** (19.5)."))}

{unidad("3.3 Prestación económica de la IT (art. 21)",
  lit("MUF", "a21", ["Desde el cuarto mes", "El 80 por ciento de las retribuciones básicas", "El 75 por ciento de las retribuciones complementarias devengadas en el tercer mes de licencia", "Durante los tres primeros meses"], solo=[1, 3, 4, 5, 7]),
  ficha("Mutualista en IT",
        ["Tres primeros meses: la totalidad de las retribuciones, a cargo de los órganos de personal", "Desde el **cuarto mes**: retribuciones básicas, prestación por hijo a cargo y **subsidio de MUFACE**, la mayor de: **80 %** de las básicas (incrementadas en la sexta parte de una paga extraordinaria) o **75 %** de las complementarias del tercer mes"],
        "La suma de lo pagado por el órgano y el subsidio no puede exceder de las percepciones del tercer mes (21.3)",
        "El subsidio se extingue por el transcurso del plazo máximo de duración del Régimen General (21.5)",
        "El subsidio de MUFACE empieza en el **cuarto** mes. **80 % básicas** o **75 % complementarias**: la mayor de las dos. La letra a) del art. 21.1 está **derogada**."))}

{unidad("3.4 Riesgo durante el embarazo y durante la lactancia natural (art. 22)",
  lit("MUF", "a22", ["hijos menores de 9 meses", "la misma consideración que la situación de incapacidad temporal derivada de enfermedad profesional", "100 por ciento de las retribuciones complementarias devengadas en el tercer mes de licencia"], solo=[1, 2, 4]),
  ficha("Funcionarias en situación de riesgo durante el embarazo o la lactancia natural de hijos menores de 9 meses",
        "Se tratan como IT derivada de **enfermedad profesional**: sin periodo de carencia",
        "Licencias: órganos de personal",
        f"Subsidio de MUFACE: {c('MUF', 'a22', 'en cuantía igual al 100 por ciento de las retribuciones complementarias devengadas en el tercer mes de licencia')}",
        "Lactancia natural: hijos **menores de 9 meses**. Subsidio: **100 %** de las complementarias (no el 75 % de la IT)."))}
""", 2)

T.ap("s10", "III.4 Incapacidad permanente y lesiones permanentes no invalidantes (RDLeg 4/2000, arts. 23 a 26 y 28)", f"""
{unidad("4.1 Concepto y grados (art. 23)",
  lit("MUF", "a23", ["Incapacidad permanente parcial para la función habitual", "La incapacidad permanente total para la función habitual", "Incapacidad permanente absoluta para todo trabajo", "Gran invalidez"], solo=[1, 2, 3, 4, 5, 6]),
  ficha("Funcionario que, tras el tratamiento y el alta médica, presenta reducciones anatómicas o funcionales graves",
        ["Parcial: limitación para las funciones de su Cuerpo, Escala o plaza", "Total: inhabilita para todas o las fundamentales funciones de su Cuerpo, Escala o plaza", "Absoluta: inhabilita por completo para toda profesión u oficio", "Gran invalidez: absoluta + necesita la asistencia de otra persona para los actos más elementales"],
        "Ha de derivarse, cualquiera que sea su causa, de la situación de incapacidad temporal",
        "—",
        "Cuatro grados. La **gran invalidez** parte de la **absoluta** y añade la necesidad de **otra persona**."))}

{unidad("4.2 Efectos de cada grado (arts. 24 a 26)",
  lit("MUF", "a24", ["la totalidad de los haberes"]),
  lit("MUF", "a25", ["darán lugar a la jubilación del funcionario", "prestaciones recuperadoras"]),
  lit("MUF", "a26", ["50 por 100 de la pensión de jubilación"]),
  ficha("Funcionario declarado en incapacidad permanente",
        ["Parcial: cobra la totalidad de los haberes de su puesto (art. 24)", "Total y absoluta: **jubilación**; si hay posibilidad razonable de recuperación, prestaciones recuperadoras de MUFACE (art. 25)", "Gran invalidez: jubilación + cantidad mensual del **50 %** de la pensión de jubilación de Clases Pasivas para remunerar a quien le asiste (art. 26)"],
        "La calificación y revisión de la incapacidad siguen las normas de derechos pasivos (art. 27.1)",
        "—",
        "La pensión de jubilación por incapacidad es de **Clases Pasivas** (→ IV.5; o del Régimen General para el nuevo ingreso: → I.1); MUFACE paga las prestaciones **recuperadoras** y la del **gran inválido** (50 %)."))}

{unidad("4.3 Lesiones permanentes no invalidantes (art. 28)",
  lit("MUF", "a28", ["darán derecho a la percepción por una sola vez de las cantidades que se establezcan reglamentariamente"]),
  ficha("Funcionario con lesiones, mutilaciones o deformaciones definitivas por enfermedad profesional o en acto de servicio",
        "Cantidad a tanto alzado, fijada reglamentariamente",
        "Solo si **no** llegan a incapacidad permanente total, absoluta o gran invalidez, y solo si derivan de enfermedad profesional o acto de servicio",
        "—",
        "Se cobran **por una sola vez** (no es pensión)."))}
""", 2)

T.ap("s11", "III.5 Protección a la familia, servicios sociales y asistencia social (RDLeg 4/2000, arts. 29 a 31)", f"""
{unidad("5.1 Prestaciones económicas de protección a la familia (art. 29)",
  lit("MUF", "a29", ["serán de pago periódico y de pago único", "son incompatibles con cualesquiera otras análogas"], solo=[1, 2, 4]),
  ficha("Mutualistas con cargas familiares",
        ["Pago periódico: prestaciones familiares por hijo a cargo", "Pago único: ayudas económicas por parto múltiple y por nacimiento de hijo", "Hijo a cargo minusválido: lo gestiona MUFACE, con las reglas de la LGSS"],
        "Incompatibles con prestaciones análogas de los restantes regímenes de la Seguridad Social",
        "—",
        "MUFACE gestiona la de **hijo a cargo minusválido**; la de hijo menor de dieciocho años no minusválido la gestionan las unidades administrativas que tenían la antigua ayuda familiar (29.3)."))}

{unidad("5.2 Servicios sociales (art. 30; RD 375/2003, art. 129)",
  lit("MUF", "a30", ["siempre que las contingencias que atiendan no estén cubiertas por otras prestaciones"]),
  lit("RD375", "Artículo 129", ["situaciones ordinarias de necesidad no cubiertas por otras prestaciones"], solo=[1, 2, 3, 4, 5, 6]),
  ficha("Mutualistas y beneficiarios",
        ["Acción formativa", "Asistencia al pensionista", "Prestaciones por fallecimiento", "Programas sociosanitarios"],
        "Solo para contingencias **no cubiertas** por otras prestaciones; su incorporación, por orden ministerial (art. 30.2)",
        "—",
        "Servicios sociales = situaciones **ordinarias** de necesidad; asistencia social = estados y situaciones **de necesidad** con límite presupuestario (→ III.5.3)."))}

{unidad("5.3 Asistencia social (art. 31; RD 375/2003, art. 137)",
  lit("MUF", "a31", ["los servicios y auxilios económicos que, en atención a estados y situaciones de necesidad, se consideren precisos", "no podrá comprometer recursos del ejercicio siguiente"], solo=[1, 2]),
  lit("RD375", "Artículo 137", ["carece de recursos suficientes"], solo=[2, 3, 4, 5, 6]),
  ficha("Mutualistas y beneficiarios (art. 32; RD 375/2003, art. 138)",
        "Servicios y auxilios económicos para estados y situaciones de necesidad: ayudas asistenciales (tratamientos especiales, inexistencia o insuficiencia de prestaciones, gastos urgentes…)",
        "Límite: los créditos del presupuesto de MUFACE; no compromete recursos del ejercicio siguiente. Hay que acreditar que se **carece de recursos suficientes**",
        "—",
        "La definición «servicios y auxilios económicos… estados y situaciones de necesidad» es la de la **asistencia social** (art. 31), no la de la asistencia sanitaria ni la del Fondo especial."))}
""", 2)

T.ap("s12", "III.6 Reglas comunes de las prestaciones y cuadro (RD 375/2003, arts. 50, 53 y 54)", f"""
{unidad("6.1 Reconocimiento, prescripción y caducidad (RD 375/2003, arts. 50, 53 y 54)",
  lit("RD375", "Artículo 50", ["por el Director General de MUFACE"], solo=[1]),
  lit("RD375", "Artículo 53", ["prescribirá a los cinco años"], solo=[1]),
  lit("RD375", "Artículo 54", ["caducará al año"], solo=[1]),
  fichab("Cómo se reconocen y cuándo se pierden las prestaciones",
         c("RD375", "Artículo 50", "por el Director General de MUFACE"),
         "A instancia del interesado (o de oficio, excepcionalmente o por convocatoria)",
         ["Derecho al **reconocimiento**: prescribe a los **cinco años** desde el día siguiente al hecho causante", "Derecho al **percibo** de lo reconocido: caduca **al año** desde la notificación"],
         "**Cinco** años para pedir; **un** año para cobrar lo reconocido."))}

### 6.2 Cuadro de la acción protectora del mutualismo (esquema)

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Contingencia (art. 11) | Prestación (art. 12) | Dato clave |
|---|---|---|
| Asistencia sanitaria | Asistencia sanitaria (arts. 13-17) | Incluye embarazo, parto y puerperio; conciertos preferentemente con la Seguridad Social |
| Incapacidad temporal | Subsidio desde el **cuarto mes** (art. 21) | Mayor de 80 % básicas o 75 % complementarias |
| Riesgo embarazo / lactancia | Subsidio (art. 22) | 100 % complementarias; lactancia: hijos menores de 9 meses |
| Incapacidad permanente | Recuperadoras; gran inválido (arts. 25-26) | Gran invalidez: 50 % de la pensión de jubilación |
| Lesiones no invalidantes | Indemnización (art. 28) | Por una sola vez |
| Cargas familiares | Hijo a cargo minusválido; parto múltiple (art. 29) | Incompatibles con otras análogas |
| — | Servicios sociales y asistencia social (arts. 30-31) | Asistencia social: límite de créditos |

{resumen([
  "Contingencias (art. 11): asistencia sanitaria, **IT**, **incapacidad permanente**, **cargas familiares** e IT por donación; la jubilación y la muerte son de **Clases Pasivas**.",
  "Asistencia sanitaria: servicios médicos, quirúrgicos y farmacéuticos; cubre **embarazo, parto y puerperio**; directa o por **concierto** (arts. 13-17).",
  "IT: enfermedad, accidente y observación por enfermedad profesional; los **permisos por parto** no son IT; subsidio de MUFACE desde el **cuarto mes** (arts. 18-21).",
  "Incapacidad permanente: cuatro grados; total y absoluta → **jubilación**; gran invalidez → + **50 %** (arts. 23-26).",
  "Reconocimiento por el **Director General**; prescripción **5 años**; caducidad del percibo **1 año** (RD 375/2003)."],
  "Siguiente: IV. ¿Qué protegen las Clases Pasivas? Derechos pasivos y pensiones")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Qué protegen las Clases Pasivas? Derechos pasivos y pensiones (RDLeg 670/1987)", donde(
  "Cuarta pregunta. El otro mecanismo de cobertura es el **Régimen de Clases Pasivas**: protege frente a la **vejez, la incapacidad y la muerte y supervivencia** mediante **pensiones**. Los derechos que genera se llaman **derechos pasivos**.",
  ["1 Acción protectora y ámbito personal", "2 Derechos pasivos: legalidad, naturaleza y ejercicio", "3 Gestión: INSS y Tesorería General de la Seguridad Social", "4 Clases de prestaciones y cuota de derechos pasivos", "5 Pensión ordinaria de jubilación", "6 Pensiones en favor de familiares", "7 Pensiones extraordinarias y cuadro"]))

T.ap("s13", "IV.1 Acción protectora y ámbito personal (RDLeg 670/1987, arts. 1 y 2)", f"""
{unidad("1.1 Qué garantiza el Régimen de Clases Pasivas (art. 1)",
  lit("RDL670", "a1", ["la protección frente a los riesgos de vejez, incapacidad y muerte y supervivencia", "uno de los mecanismos de cobertura"]),
  fichab("El Régimen de Clases Pasivas del Estado",
         c("RDL670", "a1", "el Estado garantiza al personal referido en el siguiente artículo"),
         f"Protección {c('RDL670', 'a1', 'frente a los riesgos de vejez, incapacidad y muerte y supervivencia')}",
         "—",
         "Tres riesgos: **vejez, incapacidad y muerte y supervivencia**. Para los funcionarios civiles es **uno** de los mecanismos del régimen especial (→ I.1.2)."))}

{unidad("1.2 Ámbito personal de cobertura (art. 2)",
  lit("RDL670", "a2", ["Los funcionarios de carrera de carácter civil de la Administración del Estado.", "Los funcionarios de carrera de la Administración de Justicia.", "sólo podrá ser ampliado o restringido por Ley"], solo=list(range(1, 14))),
  fichab("Quién está cubierto por Clases Pasivas",
         ["Funcionarios de carrera civiles del Estado, de la Administración de Justicia, de las Cortes Generales y de otros órganos constitucionales si su legislación lo prevé", "Personal militar (letras b, j y k)", "Interinos del Decreto-ley 10/1965; personal transferido a las CC. AA.; funcionarios en prácticas", "Ex Presidentes, Vicepresidentes y Ministros y otros cargos del art. 51"],
         "—",
         f"El ámbito {c('RDL670', 'a2', 'sólo podrá ser ampliado o restringido por Ley')}",
         "Desde el 1-1-2011, quien accede a estas condiciones va al **Régimen General** (LGSS, disp. adic. 3.ª → I.1.3), salvo los cargos de la **letra i)**, que siguen en Clases Pasivas."))}
""", 2)

T.ap("s14", "IV.2 Derechos pasivos: legalidad, naturaleza y ejercicio (RDLeg 670/1987, arts. 5 a 7)", f"""
{unidad("2.1 Solo por ley (art. 5)",
  lit("RDL670", "a5", ["Solamente por Ley"]),
  ficha("Personal del ámbito de Clases Pasivas y sus familiares",
        "Los derechos pasivos recogidos en el texto refundido",
        f"{c('RDL670', 'a5', 'Solamente por Ley')} pueden establecerse otros o ampliarse, mejorarse, reducirse o alterarse",
        "Reserva de ley",
        "Ni un reglamento ni un acuerdo pueden crear o cambiar derechos pasivos: **solo la ley**."))}

{unidad("2.2 Naturaleza de los derechos pasivos (art. 6)",
  lit("RDL670", "a6", ["inembargables, irrenunciables o inalienables", "imprescriptibles"]),
  ficha("Titulares de derechos pasivos",
        "Derechos que se originan, transmiten y extinguen solo por las causas del texto refundido",
        ["**Inembargables**, **irrenunciables** e **inalienables**: no pueden ser objeto de cesiones, convenios o contratos", "**Imprescriptibles** (con la caducidad de efectos del art. 7)"],
        "—",
        "El **derecho** es imprescriptible; lo que caduca son sus **efectos económicos** (→ IV.2.3). Las **pensiones** sí pueden embargarse en los casos de las leyes civiles (art. 21)."))}

{unidad("2.3 Ejercicio y retroactividad (art. 7)",
  lit("RDL670", "a7", ["por los propios interesados o por sus representantes legales", "desde el día siguiente a aquel en que tenga lugar el hecho causante", "la retroactividad máxima de los efectos económicos de tal reconocimiento sea de tres meses"]),
  fichab("Solicitud de reconocimiento de derechos pasivos",
         "Los interesados o sus representantes legales (o de oficio cuando lo diga el reglamento)",
         "Solicitud desde el día siguiente al hecho causante",
         f"Efectos económicos: {c('RDL670', 'a7', 'retroactividad máxima de los efectos económicos de tal reconocimiento sea de tres meses')}, desde el día primero del mes siguiente a la solicitud",
         "**Tres meses** de retroactividad máxima. No caben declaraciones **preventivas** antes del hecho causante (art. 17)."))}
""", 2)

T.ap("s15", "IV.3 Gestión: INSS y Tesorería General de la Seguridad Social (RDLeg 670/1987, arts. 11, 12 y 14)", f"""
{unidad("3.1 Reconocimiento y pago (arts. 11 y 12)",
  lit("RDL670", "a11", ["corresponde al Instituto Nacional de la Seguridad Social", "se entenderá desestimada la petición por silencio administrativo"], solo=[1, 2]),
  lit("RDL670", "a12", ["El Instituto Nacional de la Seguridad Social es la entidad gestora competente", "corresponde a la Tesorería General de la Seguridad Social"], solo=[1, 3]),
  fichab("Gestión de las Clases Pasivas",
         ["Reconocimiento de derechos pasivos y concesión de prestaciones: **Instituto Nacional de la Seguridad Social**", "Ordenación del pago y pago material: **Tesorería General de la Seguridad Social**"],
         "Procedimiento con plazo máximo para resolver; silencio **desestimatorio**",
         "—",
         "Hoy es el **INSS**, no el Ministerio de Hacienda ni MUFACE. Cayó en 2025 (→ Cierre 1). La **jubilación** la declara el órgano de personal (art. 28.3); la **pensión**, el INSS."))}

{unidad("3.2 Recursos (art. 14)",
  lit("RDL670", "a14", ["pondrán fin a la vía administrativa", "recurso potestativo de reposición"], solo=[1]),
  fichab("Revisión de los acuerdos del INSS en Clases Pasivas",
         "El INSS",
         "Ponen fin a la vía administrativa → contencioso-administrativo; antes, reposición **potestativa**",
         "—",
         "Diferencia con MUFACE: allí **alzada** (→ II.3.1); aquí los acuerdos del INSS **agotan** la vía administrativa."))}
""", 2)

T.ap("s16", "IV.4 Clases de prestaciones y cuota de derechos pasivos (RDLeg 670/1987, arts. 18, 19 y 23)", f"""
{unidad("4.1 Prestaciones: solo pensiones (art. 18)",
  lit("RDL670", "a18", ["exclusivamente de carácter económico y pago periódico", "pensiones de jubilación o retiro, de viudedad, de orfandad y en favor de los padres"]),
  ficha("El personal del art. 3.1 (en su favor) y sus familiares",
        ["Pensión de jubilación o retiro", "Pensión de viudedad", "Pensión de orfandad", "Pensión en favor de los padres"],
        "Se causan al ser jubilado o retirado, o al fallecer o ser declarado fallecido",
        "—",
        "Las prestaciones de Clases Pasivas son **exclusivamente económicas y de pago periódico**: **pensiones**. Ni asistencia sanitaria ni subsidios (eso es MUFACE)."))}

{unidad("4.2 Pensiones ordinarias, extraordinarias y excepcionales (art. 19)",
  lit("RDL670", "a19", ["ordinarias o extraordinarias", "lesión, muerte o desaparición producida en acto de servicio o como consecuencia del mismo", "pensiones excepcionales"]),
  ficha("Pensionistas de Clases Pasivas",
        ["**Ordinarias**: hecho causante en circunstancias ordinarias", "**Extraordinarias**: lesión, muerte o desaparición en **acto de servicio** o como consecuencia del mismo (→ IV.7)", "**Excepcionales**: reconocidas por ley a favor de persona determinada"],
        "Las excepcionales se rigen primero por su ley de concesión",
        "—",
        "Ordinaria / **extraordinaria** (acto de servicio) / **excepcional** (por ley, persona determinada)."))}

{unidad("4.3 Cuota de derechos pasivos (art. 23)",
  lit("RDL670", "a23", ["del tipo porcentual del 3,86 por 100", "dividiendo por catorce"], solo=[1, 2, 4, 5, 9]),
  fichab("Cotización a Clases Pasivas",
         "El personal del art. 3.1 (los funcionarios en prácticas también)",
         "Tipo sobre el haber regulador de la pensión de jubilación, retenido en nómina",
         f"Tipo general: {c('RDL670', 'a23', 'del tipo porcentual del 3,86 por 100')}; cuota mensual: la anual entre catorce, doble en junio y diciembre",
         "**3,86 %** del haber regulador. Los tipos los establece en lo sucesivo el **Gobierno** (23.4)."))}
""", 2)

_t31 = parrafos("RDL670", "a31"); _P31 = dict(zip(_t31[5:77:2], _t31[6:78:2]))
TABLA31 = "*Valores del art. 31.1 (copiados de la tabla del BOE; selección):*\n\n| Años de servicio | Porcentaje del regulador |\n|---|---|\n" + "\n".join(f"| {a} | {_P31[a]} |" for a in ["15", "20", "25", "30", "35 y más"])

T.ap("s17", "IV.5 Pensión ordinaria de jubilación (RDLeg 670/1987, arts. 28 a 31)", f"""
{unidad("5.1 Hecho causante y clases de jubilación (art. 28)",
  lit("RDL670", "a28", ["De carácter forzoso", "De carácter voluntario", "sesenta años de edad y reconocidos treinta años de servicios efectivos al Estado", "Por incapacidad permanente para el servicio o inutilidad", "dictamen preceptivo y vinculante"], solo=[1, 2, 3, 4, 5, 6]),
  ficha("El personal del art. 3.1 (entre otros, los funcionarios de carrera civiles del Estado)",
        ["**Forzosa**: automática al cumplir la edad legal", "**Voluntaria**: a instancia, con **60 años** de edad y **30** de servicios efectivos (o anticipada si una ley lo dispone)", "**Por incapacidad permanente para el servicio**: de oficio o a instancia, con dictamen preceptivo y vinculante del órgano médico"],
        "Prórroga para completar la carencia: quien llega a la edad forzosa con 12 años de servicios y sin los 15 puede pedirla (28.2 a)",
        "La declara el órgano de personal del art. 28.3 (p. ej., el Subsecretario del Departamento)",
        "Voluntaria: **60 + 30**. La jubilación es el **hecho causante** de la pensión."))}

{unidad("5.2 Período de carencia (art. 29)",
  lit("RDL670", "a29", ["quince años de servicios efectivos al Estado"]),
  ficha("Funcionario jubilado",
        "Pensión ordinaria de jubilación o retiro",
        f"Requisito: {c('RDL670', 'a29', 'haber completado quince años de servicios efectivos al Estado')}",
        "—",
        "Carencia: **15 años** (ordinaria). Las **extraordinarias** y las de **familiares** no exigen carencia (→ IV.6.1 y → IV.7)."))}

{unidad("5.3 Cálculo de la pensión (arts. 30 y 31)",
  lit("RDL670", "a30", ["se establecerán en la Ley de Presupuestos Generales del Estado para cada ejercicio económico"], solo=[1]),
  lit("RDL670", "a31", ["el porcentaje de cálculo que, atendidos los años completos de servicios efectivos al Estado"], solo=[1]),
  TABLA31,
  ficha("Funcionario jubilado",
        "Pensión anual = haber regulador (Ley de Presupuestos) × porcentaje según los años completos de servicios; si hubo varios Cuerpos, fórmula del art. 31.2",
        "La cuantía mensual es la anual entre catorce (31.5)",
        "Revalorización anual según el IPC medio (art. 27.2)",
        "Con **35 años o más**, el **100 %** del haber regulador."))}
""", 2)

T.ap("s18", "IV.6 Pensiones en favor de familiares (RDLeg 670/1987, arts. 34, 35, 38, 39, 41 y 44)", f"""
{unidad("6.1 Hecho causante y sin carencia (arts. 34 y 35)",
  lit("RDL670", "a34", ["se causará con el fallecimiento del personal correspondiente"], solo=[1]),
  lit("RDL670", "a35", ["no será preciso que el causante de los mismos haya completado ningún periodo mínimo"]),
  ficha("Familiares del funcionario fallecido",
        "Pensiones de viudedad, orfandad y en favor de los padres",
        "La ausencia legal no basta: hace falta la **declaración de fallecimiento** (34.2), salvo la pensión provisional del 34.2",
        "—",
        "Hecho causante: el **fallecimiento**. **Sin** periodo mínimo de servicios."))}

{unidad("6.2 Viudedad (arts. 38 y 39)",
  lit("RDL670", "a38", ["cónyuge supérstite", "con un año de antelación como mínimo a la fecha del fallecimiento", "con una duración de dos años"], solo=[1, 2, 3]),
  lit("RDL670", "a39", ["porcentaje fijo del 50 por 100"], solo=[6]),
  ficha("El cónyuge supérstite (y, con requisitos, el ex cónyuge y la pareja de hecho)",
        f"Pensión = base reguladora (pensión de jubilación del causante) × {c('RDL670', 'a39', 'porcentaje fijo del 50 por 100')}",
        "Si la muerte deriva de **enfermedad común** no sobrevenida tras el vínculo: matrimonio con **un año** de antelación (salvo hijos comunes o convivencia previa que sume más de dos años); si no, **prestación temporal de dos años**",
        "Se extingue por nuevo matrimonio o pareja de hecho (38.6)",
        "**50 %** (25 % si el causante tenía pensión extraordinaria por inutilidad en acto de servicio)."))}

{unidad("6.3 Orfandad (art. 41)",
  lit("RDL670", "a41", ["menores de veintiún años", "incapacitados para todo trabajo"], solo=[1]),
  ficha("Hijos del causante",
        "Pensión de orfandad, con independencia de que exista o no cónyuge supérstite",
        "Menores de **veintiún** años o incapacitados para todo trabajo; hasta **veinticinco** años si no trabajan o sus ingresos son inferiores al SMI (41.2)",
        "—",
        "Edad general: **21** años (en las extraordinarias por terrorismo, **23**: art. 48.3)."))}

{unidad("6.4 En favor de los padres (art. 44)",
  lit("RDL670", "a44", ["siempre que aquéllos dependieran económicamente de éste al momento de su fallecimiento y que no existan cónyuge supérstite o hijos del fallecido con derecho a pensión"], solo=[1]),
  ficha("El padre y la madre del causante",
        "Pensión en favor de los padres (15 % de la base reguladora cada una: art. 45.2)",
        "Dependencia económica del causante y **ausencia** de cónyuge o hijos con derecho a pensión",
        "—",
        "Es **subsidiaria**: solo si no hay viudo ni huérfanos con derecho (o desde que se extingue su derecho)."))}
""", 2)

T.ap("s19", "IV.7 Pensiones extraordinarias y cuadro (RDLeg 670/1987, arts. 47 a 49)", f"""
{unidad("7.1 Hecho causante y presunción de acto de servicio (art. 47)",
  lit("RDL670", "a47", ["en acto de servicio o como consecuencia del mismo", "competencia exclusiva del Instituto Nacional de la Seguridad Social", "en el lugar y tiempo de trabajo"], solo=[1, 2, 4, 7]),
  ficha("Funcionario incapacitado o fallecido en acto de servicio, y sus familiares",
        "Pensiones extraordinarias de jubilación o retiro y de viudedad, orfandad o en favor de los padres",
        "La incapacidad o la muerte deben producirse en acto de servicio o como consecuencia del mismo",
        f"Se presume el acto de servicio, salvo prueba en contrario, si ocurre {c('RDL670', 'a47', 'en el lugar y tiempo de trabajo')}",
        "La jubilación la declara el órgano de personal; **conceder** la pensión extraordinaria es competencia **exclusiva del INSS**."))}

{unidad("7.2 Sin carencia y cuantía (arts. 48 y 49)",
  lit("RDL670", "a48", ["cualquiera que sea el tiempo de servicios prestados al Estado"], solo=[1]),
  lit("RDL670", "a49", ["se tomarán al 200 por 100"], solo=[1]),
  ficha("Funcionario inutilizado en acto de servicio",
        "Pensión calculada con los años que faltaban hasta la edad de jubilación forzosa y con el haber regulador **al 200 %**",
        "Incompatibles con las ordinarias por los mismos hechos (art. 50.1)",
        "—",
        "Sin carencia («cualquiera que sea el tiempo de servicios»); regulador **al 200 %**."))}

### 7.3 Cuadro: mutualismo y Clases Pasivas (esquema)

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| | Mutualismo administrativo | Clases Pasivas |
|---|---|---|
| Norma | RDLeg 4/2000; RD 375/2003 | RDLeg 670/1987 |
| Gestión | **MUFACE** (organismo autónomo) | **INSS** (reconocimiento) y **TGSS** (pago) |
| Riesgos | Asistencia sanitaria, IT, incapacidad permanente, cargas familiares | Vejez, incapacidad y muerte y supervivencia |
| Prestaciones | Sanitarias, subsidios, recuperadoras, familiares, sociales | **Solo pensiones** (jubilación, viudedad, orfandad, padres) |
| Cotización | Cuota a MUFACE (tipo en la Ley de Presupuestos) | Cuota de derechos pasivos (**3,86 %**) |
| Recursos | **Alzada** contra el Director general | Acuerdos del INSS: **ponen fin** a la vía |
| Nuevo ingreso desde 2011 | Sigue en MUFACE | **Régimen General** a efectos de pensiones |

{resumen([
  "Clases Pasivas protege frente a **vejez, incapacidad y muerte y supervivencia** (art. 1); su ámbito solo cambia **por ley** (art. 2.2).",
  "Derechos pasivos: **solo por ley** (art. 5); **inembargables, irrenunciables, inalienables e imprescriptibles** (art. 6); efectos con **tres meses** de retroactividad máxima (art. 7).",
  "Reconoce y concede el **INSS**; paga la **TGSS**; sus acuerdos **ponen fin** a la vía administrativa (arts. 11, 12 y 14).",
  "Solo **pensiones**: jubilación, viudedad (50 %), orfandad (menores de 21) y en favor de los padres; ordinarias, **extraordinarias** (acto de servicio) y excepcionales (arts. 18 y 19).",
  "Jubilación voluntaria: **60 años + 30 de servicios**; carencia **15 años**; extraordinarias sin carencia y con regulador **al 200 %**."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_L77 = examen("L", 77, {
  "a": f"Excluidos: {c('MUF', 'a3', 'a) Los funcionarios de la Administración Local.')} (art. 3.2 a).",
  "b": f"Excluidos: {c('MUF', 'a3', 'b) Los funcionarios de organismos autónomos.')} (art. 3.2 b).",
  "c": f"Literal del art. 3.1 b): quedan obligatoriamente incluidos {c('MUF', 'a3', 'Los funcionarios en prácticas que aspiren a incorporarse a Cuerpos de la Administración Civil del Estado')}.",
  "d": f"Excluidos: {c('MUF', 'a3', 'd) Los funcionarios de la Administración de Justicia.')} (art. 3.2 d)."},
  [("Los funcionarios en prácticas que aspiren a incorporarse a Cuerpos de la Administración Civil del Estado", "MUF", "a3", "Los funcionarios en prácticas que aspiren a incorporarse a Cuerpos de la Administración Civil del Estado")])
EX_L78 = examen("L", 78, {
  "a": f"Falso: el art. 66 enumera el embarazo entre las contingencias cubiertas: {c('RD375', 'Artículo 66', 'así como el embarazo, el parto y el puerperio')}.",
  "b": "Que el embarazo no sea una enfermedad no importa: el art. 66 lo cubre expresamente junto a la enfermedad y el accidente.",
  "c": f"La cobertura es de la **asistencia sanitaria**: {c('RD375', 'Artículo 66', 'Las contingencias cubiertas por la prestación de la asistencia sanitaria son')}… el embarazo; no de la asistencia social.",
  "d": f"Literal del art. 66 del Reglamento: {c('RD375', 'Artículo 66', 'así como el embarazo, el parto y el puerperio, en la extensión y términos que se establecen en este reglamento')}."},
  [("Sí, así lo establece", "RD375", "Artículo 66", "así como el embarazo, el parto y el puerperio")])
EX_L79 = examen("L", 79, {
  "a": f"Clases Pasivas es para quienes ya estaban en él: con ingreso desde 2011 el personal del art. 2.1 del texto de Clases Pasivas está incluido {c('LGSS', 'datercera', 'en el Régimen General de la Seguridad Social siempre que el acceso a la condición de que se trate se produzca a partir de aquella fecha')}.",
  "b": f"Literal de la LGSS, disposición adicional tercera.1: {c('LGSS', 'datercera', 'Con efectos de 1 de enero de 2011')}… {c('LGSS', 'datercera', 'estará obligatoriamente incluido')}… en el Régimen General. Una funcionaria de la OEP 2021 accede después de esa fecha.",
  "c": f"No hay opción: la inclusión es **obligatoria** ({c('LGSS', 'datercera', 'estará obligatoriamente incluido')}).",
  "d": f"El mutualismo administrativo no da pensiones de jubilación: los nuevos funcionarios quedan en el Régimen General {c('MUF', 'a2', 'a los exclusivos efectos de pensiones')} (RDLeg 4/2000, art. 2.2)."},
  [("En el Régimen General de la Seguridad Social", "LGSS", "datercera", "en el Régimen General de la Seguridad Social siempre que el acceso a la condición de que se trate se produzca a partir de aquella fecha")])
EX_L105 = examen("L", 105, {
  "a": f"Es el objeto de la **asistencia sanitaria** (art. 13.1): {c('MUF', 'a13', 'la prestación de los servicios médicos, quirúrgicos y farmacéuticos conducentes a conservar o restablecer la salud de los beneficiarios de este Régimen especial')}.",
  "b": f"Literal de la disposición adicional sexta.2: {c('MUF', 'dasexta', 'La totalidad de los bienes, derechos y acciones de las Mutualidades, Asociaciones y Montepíos aportados con su integración a la Mutualidad General de Funcionarios Civiles del Estado constituye un Fondo especial')}.",
  "c": f"Mezcla la regla de **cotización** del art. 10.1 ({c('MUF', 'a10', 'con excepción de los mutualistas jubilados y de quienes se encuentren en la situación de excedencia voluntaria para atender al cuidado de hijos o familiares')}); al Fondo especial solo se incorporan las cuotas de los mutualistas **afectados**.",
  "d": f"Es la **asistencia social** (art. 31.1): {c('MUF', 'a31', 'los servicios y auxilios económicos que, en atención a estados y situaciones de necesidad, se consideren precisos')}."},
  [("La totalidad de los bienes, derechos y acciones de las Mutualidades, Asociaciones y Montepíos aportados con su integración a la Mutualidad General de Funcionarios Civiles del Estado", "MUF", "dasexta", "La totalidad de los bienes, derechos y acciones de las Mutualidades, Asociaciones y Montepíos aportados con su integración a la Mutualidad General de Funcionarios Civiles del Estado constituye un Fondo especial")])
EX_X85 = examen("X", 85, {
  "a": "El Real Decreto 35/1982 no es la norma que el art. tercero del RD 466/2026 identifica como la que establece la estructura de los órganos de MUFACE: esa es el Real Decreto 577/1997.",
  "b": "El Real Decreto 624/2014 no es la norma que el art. tercero del RD 466/2026 identifica como la que establece la estructura de los órganos de MUFACE: esa es el Real Decreto 577/1997.",
  "c": "El Real Decreto 462/2021 no es la norma que el art. tercero del RD 466/2026 identifica como la que establece la estructura de los órganos de MUFACE: esa es el Real Decreto 577/1997.",
  "d": f"El art. tercero del RD 466/2026 cita literalmente el título original: {c('RD466_2026', 'at', 'Real Decreto 577/1997, de 18 de abril, por el que se establece la estructura de los órganos de gobierno, administración y representación de la Mutualidad General de Funcionarios Civiles del Estado')}. Desde 2026 se titula {c('RD466_2026', 'at', 'por el que se aprueba el Estatuto de la Mutualidad General de Funcionarias y Funcionarios Civiles del Estado, O.A.')}."},
  [("Real Decreto 577/1997", "RD466_2026", "at", "Modificación del Real Decreto 577/1997, de 18 de abril, por el que se establece la estructura de los órganos de gobierno, administración y representación de la Mutualidad General de Funcionarios Civiles del Estado")])
EX_X86 = examen("X", 86, {
  "a": f"Literal del art. 18.2: {c('MUF', 'a18', 'Los permisos o licencias por parto, adopción o acogimiento, tanto preadoptivo como permanente o simple, y de paternidad por el nacimiento, acogimiento o adopción de un hijo')}… {c('MUF', 'a18', 'no tendrán la consideración de incapacidad temporal')}.",
  "b": f"Sí lo es: {c('MUF', 'a18', 'los de enfermedad, accidente y los denominados períodos de observación en caso de enfermedad profesional')} (art. 18.1).",
  "c": f"Sí lo es: el accidente está en el art. 18.1 ({c('MUF', 'a18', 'los de enfermedad, accidente')}).",
  "d": f"Sí lo es: {c('MUF', 'a18', 'los denominados períodos de observación en caso de enfermedad profesional')} (art. 18.1)."},
  [("Permiso o licencia por parto, adopción o acogimiento, tanto preadoptivo como permanente o simple", "MUF", "a18", "Los permisos o licencias por parto, adopción o acogimiento, tanto preadoptivo como permanente o simple, y de paternidad por el nacimiento, acogimiento o adopción de un hijo")])
EX_X87 = examen("X", 87, {
  "a": f"MUFACE gestiona el **mutualismo**, no las Clases Pasivas: el art. 11.1 atribuye el reconocimiento de derechos pasivos {c('RDL670', 'a11', 'al Instituto Nacional de la Seguridad Social')}.",
  "b": f"Hacienda no aparece en el art. 11.1 vigente: la competencia {c('RDL670', 'a11', 'corresponde al Instituto Nacional de la Seguridad Social')}.",
  "c": f"La IGAE no aparece en el art. 11.1; el art. 11.2 solo deja a salvo las funciones de las {c('RDL670', 'a11', 'Intervenciones Delegadas correspondientes')}, sin atribuirles el reconocimiento.",
  "d": f"Literal del art. 11.1: el reconocimiento de derechos pasivos y la concesión de las prestaciones {c('RDL670', 'a11', 'corresponde al Instituto Nacional de la Seguridad Social')}."},
  [("Instituto Nacional de la Seguridad Social", "RDL670", "a11", "corresponde al Instituto Nacional de la Seguridad Social")])

T.ap("s20", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **siete** preguntas de este tema: tres en el turno libre (más una de **reserva**, la 105) y tres en el extraordinario. Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-L 2025, pregunta 77 · Campo de aplicación (→ I.2.1)", EX_L77,
  "### GACE-L 2025, pregunta 78 · El embarazo en la asistencia sanitaria (→ III.2.1)", EX_L78,
  "### GACE-L 2025, pregunta 79 · Régimen General desde 2011 (→ I.1.3)", EX_L79,
  "### GACE-L 2025, pregunta 105 (reserva) · Fondo especial (→ II.2.3)", EX_L105,
  "### GACE-X 2025, pregunta 85 · La norma de los órganos de MUFACE (→ II.1.4)", EX_X85,
  "### GACE-X 2025, pregunta 86 · Qué no es incapacidad temporal (→ III.3.1)", EX_X86,
  "### GACE-X 2025, pregunta 87 · Quién reconoce los derechos pasivos (→ IV.3.1)", EX_X87,
  "### Cómo se pregunta",
  "!> Las preguntas citan el **artículo exacto** y ponen como distractores **otras piezas del mismo régimen**: excluidos del art. 3 frente a incluidos, la asistencia social o la sanitaria frente al Fondo especial, MUFACE frente al INSS. Saber **qué artículo regula cada cosa** resuelve la mayoría.",
]))

T.ap("s21", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Régimen especial | Dos mecanismos: Clases Pasivas y mutualismo (art. 2); incluidos y excluidos (art. 3); alta y baja (arts. 7 y 8) | **En prácticas: incluidos**; organismos autónomos y Justicia: excluidos; nuevo ingreso desde **1-1-2011** → **Régimen General** |
| II. MUFACE | Organismo autónomo; Presidencia, Consejo General y Dirección; cotización; Fondo especial; alzada | **RD 577/1997** (órganos); Fondo especial = bienes de Mutualidades y Montepíos integrados |
| III. Mutualismo | Contingencias (art. 11) y nueve prestaciones (art. 12); sanitaria; IT; incapacidad permanente; familia; social | **Embarazo** cubierto por la asistencia sanitaria; permisos por parto **no** son IT; subsidio desde el **cuarto mes** |
| IV. Clases Pasivas | Vejez, incapacidad y muerte; derechos pasivos; INSS; solo pensiones | **INSS** reconoce; jubilación voluntaria **60 + 30**; carencia **15**; viudedad **50 %** |

?> **Trampas frecuentes:** «los funcionarios de **organismos autónomos** están incluidos» (están **excluidos**); «el embarazo lo cubre la **asistencia social**» (lo cubre la **sanitaria**); «la nueva funcionaria **puede optar** por Clases Pasivas» (inclusión **obligatoria** en el Régimen General); «reconoce los derechos pasivos **MUFACE** o **Hacienda**» (es el **INSS**); «los permisos por parto son **IT**» (**no** lo son); «el subsidio de IT empieza el **primer** día» (desde el **cuarto mes**).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
q = T.q
q("MUF", "a2", "Régimen especial", "Según el artículo 2.1 del texto refundido aprobado por Real Decreto Legislativo 4/2000, el Régimen especial de la Seguridad Social de los Funcionarios Civiles del Estado queda integrado por los siguientes mecanismos de cobertura:",
  ["El Régimen de Clases Pasivas del Estado y el Régimen del Mutualismo Administrativo.", "El Régimen General de la Seguridad Social y el Régimen del Mutualismo Administrativo.", "El Régimen de Clases Pasivas del Estado y el Régimen Especial de las Fuerzas Armadas.", "Únicamente el Régimen del Mutualismo Administrativo."],
  "Art. 2.1 RDLeg 4/2000: a) Clases Pasivas; b) Mutualismo Administrativo.", ["a) El Régimen de Clases Pasivas del Estado, de acuerdo con sus normas específicas.", "b) El Régimen del Mutualismo Administrativo que se regula en la presente Ley."])
q("MUF", "a2", "Régimen especial", "Según el artículo 2.2 del Real Decreto Legislativo 4/2000, los funcionarios de carrera de la Administración Civil del Estado que hayan ingresado a partir del 1 de enero de 2011 quedarán integrados en el Régimen General de la Seguridad Social:",
  ["A los exclusivos efectos de pensiones.", "A los exclusivos efectos de asistencia sanitaria.", "A todos los efectos, con baja en MUFACE.", "A los exclusivos efectos de incapacidad temporal."],
  "Art. 2.2 RDLeg 4/2000: «a los exclusivos efectos de pensiones».", "quedarán integrados en el Régimen General de la Seguridad Social a los exclusivos efectos de pensiones")
q("LGSS", "datercera", "Régimen especial", "Según la disposición adicional tercera de la Ley General de la Seguridad Social, el personal del artículo 2.1 del texto refundido de Clases Pasivas (salvo la letra i) está obligatoriamente incluido en el Régimen General si accede a su condición a partir de:",
  ["El 1 de enero de 2011.", "El 1 de enero de 2010.", "El 1 de enero de 2012.", "El 3 de diciembre de 2010."],
  "LGSS, disp. adic. 3.ª.1: «Con efectos de 1 de enero de 2011».", "Con efectos de 1 de enero de 2011")
q("MUF", "a3", "Campo de aplicación", "Según el artículo 3.2 del Real Decreto Legislativo 4/2000, ¿cuál de los siguientes colectivos queda excluido del Régimen especial de la Seguridad Social de los Funcionarios Civiles del Estado?",
  ["Los funcionarios de la Administración de la Seguridad Social.", "Los funcionarios de carrera de la Administración Civil del Estado.", "Los funcionarios en prácticas que aspiren a incorporarse a Cuerpos de la Administración Civil del Estado.", "Los funcionarios interinos a que se refiere el artículo 1 del Decreto-ley 10/1965."],
  "Art. 3.2 e) RDLeg 4/2000. Los de carrera y en prácticas están incluidos (3.1) y los interinos del Decreto-ley 10/1965, también (disp. adic. 1.ª.1 a).", "e) Los funcionarios de la Administración de la Seguridad Social.")
q("MUF", "a7", "Afiliación", "Según el artículo 7.1 del Real Decreto Legislativo 4/2000, los funcionarios de carrera de la Administración Civil del Estado se incorporarán obligatoriamente a MUFACE:",
  ["En el momento de la toma de posesión de su cargo.", "En el momento de superar el proceso selectivo.", "Al mes siguiente de la toma de posesión.", "Con la publicación de su nombramiento en el BOE."],
  "Art. 7.1 RDLeg 4/2000.", "en el momento de la toma de posesión de su cargo")
q("MUF", "a7", "Afiliación", "Según el artículo 7.1 del Real Decreto Legislativo 4/2000, ¿en cuál de las siguientes situaciones conserva el funcionario la condición de mutualista con los mismos derechos y obligaciones que en servicio activo?",
  ["Expectativa de destino.", "Excedencia voluntaria por interés particular.", "Excedencia voluntaria por agrupación familiar.", "Pérdida de la condición de funcionario."],
  "Art. 7.1 c) RDLeg 4/2000. La excedencia voluntaria, en cualquiera de sus modalidades, y la pérdida de la condición causan baja (art. 8.1).", "c) Expectativa de destino.")
q("MUF", "a7", "Afiliación", "Según el artículo 7.3 del Real Decreto Legislativo 4/2000, los funcionarios que accedan por promoción interna a Escalas de Organismos Autónomos y deseen mantener su condición de mutualistas deberán ejercitar esta opción, por una sola vez, en el plazo de:",
  ["Quince días desde la toma de posesión en el nuevo Cuerpo o Escala.", "Un mes desde la toma de posesión en el nuevo Cuerpo o Escala.", "Diez días desde el nombramiento.", "Tres meses desde la publicación del nombramiento."],
  "Art. 7.3 RDLeg 4/2000.", "en el plazo de quince días desde la toma de posesión en el nuevo Cuerpo o Escala")
q("MUF", "a10", "Cotización", "Según el artículo 10.1 del Real Decreto Legislativo 4/2000, la cotización a MUFACE será obligatoria para todos los mutualistas, con excepción de:",
  ["Los mutualistas jubilados.", "Los mutualistas en situación de servicios especiales.", "Los funcionarios en prácticas.", "Los mutualistas voluntarios."],
  "Art. 10.1: excepción de los jubilados y de los excedentes para cuidado de hijos o familiares. Los voluntarios pagan las dos cuotas (art. 8.2).", "con excepción de los mutualistas jubilados")
q("MUF", "a10", "Cotización", "Según el artículo 10.4 del Real Decreto Legislativo 4/2000, la cuota mensual de cotización a MUFACE se obtendrá dividiendo la cantidad anual resultante por:",
  ["Catorce, y se abonará doblemente en los meses de junio y diciembre.", "Doce, y se abonará en cada mensualidad ordinaria.", "Catorce, y se abonará doblemente en los meses de julio y diciembre.", "Doce, y se abonará doblemente en el mes de diciembre."],
  "Art. 10.4 RDLeg 4/2000.", ["dividiendo por catorce", "se abonará doblemente en los meses de junio y diciembre"])
q("MUF", "a10", "Cotización", "Según el artículo 10.6 del Real Decreto Legislativo 4/2000, la obligación de pago de las cotizaciones a la Mutualidad prescribirá:",
  ["A los cuatro años a contar desde la fecha en que preceptivamente debieron ser ingresadas.", "A los cinco años a contar desde la fecha en que preceptivamente debieron ser ingresadas.", "Al año de su devengo.", "A los tres años desde la notificación de la liquidación."],
  "Art. 10.6 RDLeg 4/2000.", "prescribirá a los cuatro años a contar desde la fecha en que preceptivamente debieron ser ingresadas")
q("RD577", "a1", "MUFACE", "Según el artículo 1 del Estatuto de MUFACE (Real Decreto 577/1997), la Mutualidad General de Funcionarias y Funcionarios Civiles del Estado es:",
  ["Un organismo autónomo de los previstos en el artículo 98.1 de la Ley 40/2015.", "Una entidad pública empresarial.", "Una agencia estatal.", "Una entidad gestora de la Seguridad Social dependiente del Ministerio competente en materia de Seguridad Social."],
  "Art. 1.1 del Estatuto (redacción del RD 466/2026).", "es un organismo autónomo de los previstos en el artículo 98.1 de la Ley 40/2015")
q("RD577", "a4", "MUFACE", "Según el artículo 4 del Estatuto de MUFACE (Real Decreto 577/1997), el órgano ejecutivo del organismo autónomo es:",
  ["La Dirección.", "El Consejo General.", "La Presidencia.", "La Comisión Permanente."],
  "Art. 4.2: «El órgano ejecutivo del organismo autónomo es la Dirección». La Presidencia y el Consejo General son órganos de gobierno (4.1).", "El órgano ejecutivo del organismo autónomo es la Dirección")
q("RD577", "a6-2", "MUFACE", "Según el Estatuto de MUFACE (Real Decreto 577/1997), la Presidencia del organismo autónomo corresponde a:",
  ["La persona titular de la Secretaría de Estado de Función Pública.", "La persona titular del Ministerio de Hacienda.", "La persona titular de la Dirección General de MUFACE.", "La persona titular de la Subsecretaría del Ministerio de adscripción."],
  "Art. 6 [sic].1 del Estatuto.", "La Presidencia del organismo autónomo MUFACE corresponde a la persona titular de la Secretaría de Estado de Función Pública")
q("MUF", "a37", "MUFACE", "Según el artículo 37.1 del Real Decreto Legislativo 4/2000, los actos y resoluciones del Director general de MUFACE, como regla general:",
  ["No ponen fin a la vía administrativa y pueden recurrirse en alzada.", "Ponen fin a la vía administrativa y solo cabe recurso contencioso-administrativo.", "Son recurribles en reposición obligatoria ante el propio Director general.", "Son recurribles ante el Consejo General de MUFACE."],
  "Art. 37.1 RDLeg 4/2000 (con las excepciones del 37.2).", "no ponen fin a la vía administrativa, pudiéndose recurrir en alzada")
q("MUF", "a11", "Acción protectora", "Según el artículo 11 del Real Decreto Legislativo 4/2000, ¿cuál de las siguientes es una contingencia protegida por el mutualismo administrativo?",
  ["Cargas familiares.", "Desempleo.", "Jubilación.", "Viudedad."],
  "Art. 11: asistencia sanitaria, IT, incapacidad permanente, cargas familiares e IT por donación. Jubilación y viudedad son de Clases Pasivas.", "d) Cargas familiares.")
q("MUF", "a13", "Asistencia sanitaria", "Según el artículo 13.1 del Real Decreto Legislativo 4/2000, la asistencia sanitaria tiene por objeto la prestación de los servicios:",
  ["Médicos, quirúrgicos y farmacéuticos conducentes a conservar o restablecer la salud de los beneficiarios.", "Médicos y quirúrgicos, excluidos los farmacéuticos.", "Sociales y asistenciales precisos en situaciones de necesidad.", "Médicos de atención primaria, con exclusión de la especializada."],
  "Art. 13.1 RDLeg 4/2000.", "la prestación de los servicios médicos, quirúrgicos y farmacéuticos conducentes a conservar o restablecer la salud de los beneficiarios")
q("MUF", "a15", "Asistencia sanitaria", "Según el artículo 15.3 del Real Decreto Legislativo 4/2000, MUFACE facilitará asistencia sanitaria al recién nacido, cuando la madre sea mutualista o beneficiaria, aunque no tenga reconocida la condición de beneficiario, durante:",
  ["Los primeros quince días desde el momento del parto.", "Los primeros treinta días desde el momento del parto.", "Los tres primeros meses de vida.", "El primer año de vida."],
  "Art. 15.3 RDLeg 4/2000.", "durante los primeros quince días desde el momento del parto")
q("MUF", "a17", "Asistencia sanitaria", "Según el artículo 17.1 del Real Decreto Legislativo 4/2000, los conciertos para facilitar la asistencia sanitaria se establecerán:",
  ["Preferentemente con instituciones de la Seguridad Social.", "Exclusivamente con entidades de seguro privadas.", "Preferentemente con entidades de seguro privadas.", "Únicamente con los servicios de salud de las Comunidades Autónomas."],
  "Art. 17.1 RDLeg 4/2000.", "Estos conciertos se establecerán preferentemente con instituciones de la Seguridad Social")
q("MUF", "a18", "Incapacidad temporal", "Según el artículo 18.2 del Real Decreto Legislativo 4/2000, si al término del permiso por parto continuase la imposibilidad de incorporarse al trabajo:",
  ["Se iniciarán las licencias que dan lugar a la incapacidad temporal.", "Se prorrogará automáticamente el permiso por parto.", "Se iniciará de oficio el procedimiento de jubilación por incapacidad permanente.", "La funcionaria pasará a excedencia por cuidado de familiares."],
  "Art. 18.2 RDLeg 4/2000.", "Si al término del permiso por parto continuase la imposibilidad de incorporarse al trabajo, se iniciarán las licencias que dan lugar a la incapacidad temporal")
q("MUF", "a19", "Incapacidad temporal", "Según el artículo 19.3 del Real Decreto Legislativo 4/2000, la concesión de las licencias por incapacidad temporal y sus posibles prórrogas corresponderá a:",
  ["Los órganos administrativos con competencia en materias de gestión de personal.", "La Mutualidad General de Funcionarios Civiles del Estado.", "Las Unidades Médicas de Seguimiento.", "El Instituto Nacional de la Seguridad Social."],
  "Art. 19.3 RDLeg 4/2000; MUFACE puede ejercer el control y seguimiento (19.4).", "corresponderá a los órganos administrativos con competencia en materias de gestión de personal")
q("MUF", "a21", "Incapacidad temporal", "Según el artículo 21.1 del Real Decreto Legislativo 4/2000, el mutualista en incapacidad temporal percibe un subsidio a cargo de MUFACE:",
  ["Desde el cuarto mes.", "Desde el primer día de la licencia.", "Desde el segundo mes.", "Desde el séptimo mes."],
  "Art. 21.1 b): «Desde el cuarto mes»; los tres primeros meses, la totalidad de las retribuciones a cargo de los órganos de personal.", "Desde el cuarto mes")
q("MUF", "a21", "Incapacidad temporal", "Según el artículo 21.1 b) del Real Decreto Legislativo 4/2000, el subsidio por incapacidad temporal será la mayor de dos cantidades: el 75 por ciento de las retribuciones complementarias devengadas en el tercer mes de licencia o:",
  ["El 80 por ciento de las retribuciones básicas, incrementadas en la sexta parte de una paga extraordinaria, correspondientes al tercer mes de licencia.", "El 75 por ciento de las retribuciones básicas correspondientes al primer mes de licencia.", "El 100 por ciento de las retribuciones básicas correspondientes al tercer mes de licencia.", "El 60 por ciento de la base de cotización del mes anterior."],
  "Art. 21.1 b) 1.ª RDLeg 4/2000.", "El 80 por ciento de las retribuciones básicas (sueldo, trienios y grado, en su caso), incrementadas en la sexta parte de una paga extraordinaria, correspondientes al tercer mes de licencia")
q("MUF", "a22", "Incapacidad temporal", "Según el artículo 22.1 del Real Decreto Legislativo 4/2000, la situación de riesgo durante la lactancia natural está protegida respecto de hijos menores de:",
  ["9 meses.", "12 meses.", "6 meses.", "18 meses."],
  "Art. 22.1 RDLeg 4/2000.", "lactancia natural de hijos menores de 9 meses")
q("MUF", "a23", "Incapacidad permanente", "Según el artículo 23.2 del Real Decreto Legislativo 4/2000, la situación del funcionario afecto de incapacidad permanente absoluta que, como consecuencia de pérdidas anatómicas o funcionales, necesita de la asistencia de otra persona para realizar los actos más elementales de la vida se denomina:",
  ["Gran invalidez.", "Incapacidad permanente total para la función habitual.", "Incapacidad permanente absoluta para todo trabajo.", "Incapacidad permanente parcial para la función habitual."],
  "Art. 23.2 d) RDLeg 4/2000.", "d) Gran invalidez: es la situación del funcionario afecto de incapacidad permanente absoluta")
q("MUF", "a26", "Incapacidad permanente", "Según el artículo 26 del Real Decreto Legislativo 4/2000, la gran invalidez da derecho a una cantidad mensual, destinada a remunerar a la persona encargada de la asistencia del funcionario, equivalente al:",
  ["50 por 100 de la pensión de jubilación que le corresponda con arreglo al Régimen de Clases Pasivas.", "25 por 100 de la pensión de jubilación que le corresponda con arreglo al Régimen de Clases Pasivas.", "100 por 100 de la pensión de jubilación que le corresponda con arreglo al Régimen de Clases Pasivas.", "50 por 100 del salario mínimo interprofesional."],
  "Art. 26 RDLeg 4/2000.", "una cantidad mensual equivalente al 50 por 100 de la pensión de jubilación que le corresponda con arreglo al Régimen de Clases Pasivas")
q("MUF", "a28", "Incapacidad permanente", "Según el artículo 28 del Real Decreto Legislativo 4/2000, las lesiones permanentes no invalidantes causadas por enfermedad profesional o en acto de servicio dan derecho a:",
  ["La percepción por una sola vez de las cantidades que se establezcan reglamentariamente.", "Una pensión vitalicia de Clases Pasivas.", "Un subsidio mensual mientras dure la lesión.", "La jubilación por incapacidad permanente para el servicio."],
  "Art. 28 RDLeg 4/2000.", "darán derecho a la percepción por una sola vez de las cantidades que se establezcan reglamentariamente")
q("MUF", "a31", "Asistencia social", "Según el artículo 31.2 del Real Decreto Legislativo 4/2000, los servicios y auxilios económicos de asistencia social tendrán como límite los créditos consignados en el presupuesto de gastos de MUFACE y su concesión:",
  ["No podrá comprometer recursos del ejercicio siguiente a aquel en que la misma tenga lugar.", "Podrá comprometer recursos de los dos ejercicios siguientes.", "Requerirá autorización previa del Consejo de Ministros.", "Se financiará con cargo al Fondo especial."],
  "Art. 31.2 RDLeg 4/2000.", "su concesión no podrá comprometer recursos del ejercicio siguiente a aquel en que la misma tenga lugar")
q("RD375", "Artículo 53", "Reglas comunes", "Según el artículo 53.1 del Reglamento General del Mutualismo Administrativo (Real Decreto 375/2003), el derecho al reconocimiento de las prestaciones prescribirá:",
  ["A los cinco años, contados a partir del día siguiente a aquél en que tenga lugar el hecho causante.", "A los cuatro años, contados desde la fecha del hecho causante.", "Al año, contado desde el día siguiente al hecho causante.", "A los tres meses desde el hecho causante."],
  "Art. 53.1 RD 375/2003. (Al año caduca el derecho al percibo de lo ya reconocido: art. 54.1.)", "El derecho al reconocimiento de las prestaciones prescribirá a los cinco años, contados a partir del día siguiente a aquél en que tenga lugar el hecho causante")
q("RDL670", "a1", "Clases Pasivas", "Según el artículo 1.1 del texto refundido de Ley de Clases Pasivas del Estado, a través del Régimen de Clases Pasivas el Estado garantiza la protección frente a los riesgos de:",
  ["Vejez, incapacidad y muerte y supervivencia.", "Enfermedad, maternidad y desempleo.", "Vejez, desempleo y cargas familiares.", "Incapacidad temporal, asistencia sanitaria y vejez."],
  "Art. 1.1 RDLeg 670/1987.", "la protección frente a los riesgos de vejez, incapacidad y muerte y supervivencia")
q("RDL670", "a5", "Derechos pasivos", "Según el artículo 5 del texto refundido de Ley de Clases Pasivas del Estado, podrán establecerse derechos pasivos distintos de los recogidos en él, o ampliarse, mejorarse, reducirse o alterarse:",
  ["Solamente por Ley.", "Por real decreto acordado en Consejo de Ministros.", "Por orden del Ministerio competente en materia de Seguridad Social.", "Por acuerdo de la Mesa General de Negociación."],
  "Art. 5 RDLeg 670/1987.", "Solamente por Ley podrán establecerse derechos pasivos distintos de los recogidos en este texto")
q("RDL670", "a6", "Derechos pasivos", "Según el artículo 6 del texto refundido de Ley de Clases Pasivas del Estado, los derechos pasivos son:",
  ["Inembargables, irrenunciables, inalienables e imprescriptibles.", "Embargables, renunciables y prescriptibles a los cinco años.", "Inembargables, pero renunciables y transmisibles por contrato.", "Imprescriptibles, pero embargables en todo caso."],
  "Art. 6.1: «inembargables, irrenunciables o inalienables»; art. 6.2: «imprescriptibles».", ["Las derechos pasivos son inembargables, irrenunciables o inalienables", "Los derechos pasivos son imprescriptibles"])
q("RDL670", "a7", "Derechos pasivos", "Según el artículo 7.2 del texto refundido de Ley de Clases Pasivas del Estado, la retroactividad máxima de los efectos económicos del reconocimiento de las prestaciones será de:",
  ["Tres meses a contar desde el día primero del mes siguiente a la presentación de la solicitud.", "Seis meses a contar desde la presentación de la solicitud.", "Un año a contar desde el hecho causante.", "Cinco años a contar desde el hecho causante."],
  "Art. 7.2 RDLeg 670/1987.", "la retroactividad máxima de los efectos económicos de tal reconocimiento sea de tres meses a contar desde el día primero del mes siguiente a la presentación de la correspondiente solicitud")
q("RDL670", "a12", "Gestión", "Según el artículo 12.3 del texto refundido de Ley de Clases Pasivas del Estado, la ordenación del pago de las prestaciones de Clases Pasivas y el pago material de las mismas corresponde a:",
  ["La Tesorería General de la Seguridad Social.", "El Instituto Nacional de la Seguridad Social.", "La Mutualidad General de Funcionarios Civiles del Estado.", "La Secretaría General del Tesoro y Financiación Internacional."],
  "Art. 12.3 RDLeg 670/1987. Al INSS le corresponde el reconocimiento de las obligaciones y la propuesta de pagos (12.1).", "La ordenación del pago de las prestaciones de Clases Pasivas y el pago material de las mismas corresponde a la Tesorería General de la Seguridad Social")
q("RDL670", "a14", "Gestión", "Según el artículo 14.1 del texto refundido de Ley de Clases Pasivas del Estado, los acuerdos del Instituto Nacional de la Seguridad Social en materia de Clases Pasivas:",
  ["Pondrán fin a la vía administrativa; con carácter previo al contencioso podrá interponerse recurso potestativo de reposición.", "No pondrán fin a la vía administrativa y serán recurribles en alzada ante el Ministro.", "Serán recurribles ante el Tribunal Económico-Administrativo Central.", "Exigen reclamación previa obligatoria ante la Tesorería General de la Seguridad Social."],
  "Art. 14.1 RDLeg 670/1987.", ["pondrán fin a la vía administrativa", "podrá interponerse recurso potestativo de reposición"])
q("RDL670", "a18", "Prestaciones de Clases Pasivas", "Según el artículo 18.2 del texto refundido de Ley de Clases Pasivas del Estado, ¿cuál de las siguientes es una prestación del Régimen de Clases Pasivas?",
  ["La pensión en favor de los padres.", "El subsidio por incapacidad temporal.", "La asistencia sanitaria.", "La prestación por hijo a cargo minusválido."],
  "Art. 18.2: pensiones de jubilación o retiro, viudedad, orfandad y en favor de los padres. Las demás son prestaciones de MUFACE (art. 12 RDLeg 4/2000).", "pensiones de jubilación o retiro, de viudedad, de orfandad y en favor de los padres")
q("RDL670", "a19", "Prestaciones de Clases Pasivas", "Según el artículo 19.1 del texto refundido de Ley de Clases Pasivas del Estado, son pensiones extraordinarias aquellas cuyo hecho causante se produce:",
  ["Por razón de lesión, muerte o desaparición producida en acto de servicio o como consecuencia del mismo.", "Por reconocimiento en virtud de Ley a favor de persona determinada.", "Por jubilación voluntaria anticipada.", "En circunstancias ordinarias."],
  "Art. 19.1 RDLeg 670/1987. Las reconocidas por ley a persona determinada son pensiones excepcionales (19.2).", "por razón de lesión, muerte o desaparición producida en acto de servicio o como consecuencia del mismo")
q("RDL670", "a23", "Prestaciones de Clases Pasivas", "Según el artículo 23.1 del texto refundido de Ley de Clases Pasivas del Estado, el tipo porcentual de la cuota de derechos pasivos aplicable al haber regulador de los funcionarios civiles es del:",
  ["3,86 por 100.", "4,70 por 100.", "2,50 por 100.", "6,35 por 100."],
  "Art. 23.1 RDLeg 670/1987.", "del tipo porcentual del 3,86 por 100")
q("RDL670", "a28", "Jubilación", "Según el artículo 28.2 b) del texto refundido de Ley de Clases Pasivas del Estado, la jubilación de carácter voluntario se declarará a instancia de parte siempre que el interesado tenga cumplidos:",
  ["Sesenta años de edad y reconocidos treinta años de servicios efectivos al Estado.", "Sesenta y cinco años de edad y reconocidos quince años de servicios efectivos al Estado.", "Sesenta años de edad y reconocidos treinta y cinco años de servicios efectivos al Estado.", "Sesenta y un años de edad y reconocidos treinta años de servicios efectivos al Estado."],
  "Art. 28.2 b) RDLeg 670/1987.", "siempre que el interesado tenga cumplidos los sesenta años de edad y reconocidos treinta años de servicios efectivos al Estado")
q("RDL670", "a29", "Jubilación", "Según el artículo 29 del texto refundido de Ley de Clases Pasivas del Estado, para causar derecho a la pensión ordinaria de jubilación el funcionario deberá haber completado:",
  ["Quince años de servicios efectivos al Estado.", "Diez años de servicios efectivos al Estado.", "Veinte años de servicios efectivos al Estado.", "Treinta y cinco años de servicios efectivos al Estado."],
  "Art. 29 RDLeg 670/1987.", "deberá haber completado quince años de servicios efectivos al Estado")
q("RDL670", "a39", "Pensiones de familiares", "Según el artículo 39.3 del texto refundido de Ley de Clases Pasivas del Estado, para obtener el importe de la pensión ordinaria de viudedad se aplicará a la base reguladora el porcentaje fijo del:",
  ["50 por 100.", "25 por 100.", "60 por 100.", "45 por 100."],
  "Art. 39.3 RDLeg 670/1987 (25 por 100 si el causante tenía pensión extraordinaria por inutilidad en acto de servicio).", "se aplicará el porcentaje fijo del 50 por 100 para obtener el importe de la pensión de viudedad")
q("RDL670", "a38", "Pensiones de familiares", "Según el artículo 38.1 del texto refundido de Ley de Clases Pasivas del Estado, cuando el cónyuge no pueda acceder a la pensión de viudedad por no cumplir el requisito de duración del matrimonio, tendrá derecho a una prestación temporal de igual cuantía con una duración de:",
  ["Dos años.", "Un año.", "Seis meses.", "Cinco años."],
  "Art. 38.1, párrafo tercero, RDLeg 670/1987.", "tendrá derecho a una prestación temporal de igual cuantía que la pensión de viudedad que le hubiera correspondido y con una duración de dos años")
q("RDL670", "a41", "Pensiones de familiares", "Según el artículo 41.1 del texto refundido de Ley de Clases Pasivas del Estado, con carácter general tendrán derecho a pensión de orfandad los hijos del causante que fueran menores de:",
  ["Veintiún años.", "Dieciocho años.", "Veintitrés años.", "Veinticinco años, en todo caso."],
  "Art. 41.1 RDLeg 670/1987 (hasta veinticinco años solo con los requisitos de ingresos del 41.2).", "los hijos del causante de los derechos pasivos que fueran menores de veintiún años")
q("RDL670", "a44", "Pensiones de familiares", "Según el artículo 44.1 del texto refundido de Ley de Clases Pasivas del Estado, el padre y la madre del causante tendrán derecho a pensión siempre que dependieran económicamente de éste al momento de su fallecimiento y:",
  ["Que no existan cónyuge supérstite o hijos del fallecido con derecho a pensión.", "Que sean mayores de sesenta y cinco años.", "Que hubieran convivido con el causante durante al menos cinco años.", "Aunque existan cónyuge supérstite o hijos con derecho a pensión."],
  "Art. 44.1 RDLeg 670/1987.", "que no existan cónyuge supérstite o hijos del fallecido con derecho a pensión")
q("RDL670", "a47", "Pensiones extraordinarias", "Según el artículo 47.4 del texto refundido de Ley de Clases Pasivas del Estado, se presumirá el acto de servicio, salvo prueba en contrario, cuando la incapacidad permanente o el fallecimiento del funcionario hayan acaecido:",
  ["En el lugar y tiempo de trabajo.", "En el trayecto de ida o vuelta al domicilio, en todo caso.", "Durante el periodo de vacaciones.", "En cualquier lugar, si el funcionario estaba en servicio activo."],
  "Art. 47.4 RDLeg 670/1987.", "cuando la incapacidad permanente o el fallecimiento del funcionario hayan acaecido en el lugar y tiempo de trabajo")
q("RDL670", "a49", "Pensiones extraordinarias", "Según el artículo 49.1 del texto refundido de Ley de Clases Pasivas del Estado, para el cálculo de la pensión extraordinaria de jubilación el haber regulador o los haberes reguladores que correspondan se tomarán al:",
  ["200 por 100.", "100 por 100.", "150 por 100.", "50 por 100."],
  "Art. 49.1 RDLeg 670/1987.", "se tomarán al 200 por 100")
T.real("L", 77, "Campo de aplicación"); T.real("L", 78, "Asistencia sanitaria"); T.real("L", 79, "Régimen especial")
T.real("L", 105, "MUFACE"); T.real("X", 85, "MUFACE"); T.real("X", 86, "Incapacidad temporal"); T.real("X", 87, "Gestión")

# Flashcards
for q_, a_, cat in [
  ("Mecanismos de cobertura del Régimen especial (RDLeg 4/2000, art. 2.1)", "El Régimen de Clases Pasivas del Estado y el Régimen del Mutualismo Administrativo.", "Régimen especial"),
  ("Funcionarios ingresados desde el 1-1-2011: ¿en qué régimen?", "En el Régimen General de la Seguridad Social, a los exclusivos efectos de pensiones (art. 2.2; LGSS, disp. adic. 3.ª); siguen en MUFACE.", "Régimen especial"),
  ("Incluidos obligatoriamente (art. 3.1)", "Funcionarios de carrera de la Administración Civil del Estado y funcionarios en prácticas que aspiren a incorporarse a sus Cuerpos.", "Campo de aplicación"),
  ("Excluidos (art. 3.2)", "Administración Local, organismos autónomos, Administración Militar, Administración de Justicia, Administración de la Seguridad Social, nuevo ingreso y prácticas de CC. AA., transferidos integrados en Cuerpos de la CA, PAS de universidades.", "Campo de aplicación"),
  ("¿Cuándo se incorpora el funcionario a MUFACE? (art. 7.1)", "En el momento de la toma de posesión de su cargo (los de prácticas, desde el inicio de las prácticas: RD 375/2003, art. 13).", "Afiliación"),
  ("¿Qué excedencia causa baja como mutualista obligatorio? (art. 8.1)", "La excedencia voluntaria, en cualquiera de sus modalidades (la de cuidado de familiares conserva la condición: art. 7.1).", "Afiliación"),
  ("Naturaleza de MUFACE (Estatuto, art. 1)", "Organismo autónomo (art. 98.1 Ley 40/2015), adscrito a través de la Secretaría de Estado de Función Pública.", "MUFACE"),
  ("Órganos de MUFACE (Estatuto, art. 4)", "De gobierno: la Presidencia y el Consejo General (Consejo Rector); ejecutivo: la Dirección.", "MUFACE"),
  ("¿Quién no cotiza a MUFACE? (art. 10.1)", "Los mutualistas jubilados y los excedentes voluntarios para atender al cuidado de hijos o familiares.", "Cotización"),
  ("Fondo especial (disp. adic. 6.ª)", "Bienes, derechos y acciones de las Mutualidades, Asociaciones y Montepíos integrados en MUFACE; no admite nuevos socios; déficit cubierto por el Estado.", "MUFACE"),
  ("Contingencias del mutualismo (art. 11)", "Asistencia sanitaria; incapacidad temporal; incapacidad permanente; cargas familiares; IT especial por donación de órganos.", "Acción protectora"),
  ("¿Cubre la asistencia sanitaria el embarazo? (art. 14; RD 375/2003, art. 66)", "Sí: el embarazo, el parto y el puerperio.", "Asistencia sanitaria"),
  ("Estados determinantes de IT (art. 18.1)", "Enfermedad, accidente y períodos de observación por enfermedad profesional. Los permisos por parto, adopción, acogimiento y paternidad no son IT (18.2).", "Incapacidad temporal"),
  ("Subsidio de IT de MUFACE (art. 21)", "Desde el cuarto mes: la mayor de 80 % de las retribuciones básicas (+1/6 de paga extra) o 75 % de las complementarias del tercer mes.", "Incapacidad temporal"),
  ("Grados de incapacidad permanente (art. 23)", "Parcial, total para la función habitual, absoluta para todo trabajo y gran invalidez.", "Incapacidad permanente"),
  ("Gran invalidez: prestación de MUFACE (art. 26)", "50 % de la pensión de jubilación de Clases Pasivas, para remunerar a quien le asiste.", "Incapacidad permanente"),
  ("Riesgos protegidos por Clases Pasivas (RDLeg 670/1987, art. 1)", "Vejez, incapacidad y muerte y supervivencia.", "Clases Pasivas"),
  ("Naturaleza de los derechos pasivos (art. 6)", "Inembargables, irrenunciables, inalienables e imprescriptibles.", "Derechos pasivos"),
  ("¿Quién reconoce derechos pasivos y concede prestaciones de Clases Pasivas? (art. 11)", "El Instituto Nacional de la Seguridad Social; el pago lo ordena y realiza la Tesorería General de la Seguridad Social (art. 12).", "Gestión"),
  ("Prestaciones de Clases Pasivas (art. 18.2)", "Exclusivamente económicas y periódicas: pensiones de jubilación o retiro, viudedad, orfandad y en favor de los padres.", "Prestaciones de Clases Pasivas"),
  ("Jubilación voluntaria y carencia (arts. 28.2 b y 29)", "60 años de edad y 30 de servicios efectivos; carencia de la pensión ordinaria: 15 años.", "Jubilación"),
  ("Pensión extraordinaria (arts. 47 a 49)", "Incapacidad o muerte en acto de servicio; sin carencia; haber regulador al 200 %; la concede en exclusiva el INSS.", "Pensiones extraordinarias"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Mutualismo administrativo", "Mecanismo de cobertura del Régimen especial regulado en el RDLeg 4/2000 y gestionado por MUFACE (art. 2.1 b).", "s1", "Régimen especial")
T.glos("Clases Pasivas", "Régimen por el que el Estado garantiza la protección frente a los riesgos de vejez, incapacidad y muerte y supervivencia (RDLeg 670/1987, art. 1).", "s13", "Clases Pasivas")
T.glos("Mutualista", "Funcionario incorporado a MUFACE: obligatoriamente al tomar posesión; voluntario si mantiene el alta pagando las dos cuotas (arts. 7 y 8).", "s3", "Régimen especial")
T.glos("MUFACE", "Mutualidad General de Funcionarias y Funcionarios Civiles del Estado, O.A.: organismo autónomo que gestiona el mutualismo administrativo (RDLeg 4/2000, art. 4; Estatuto, art. 1).", "s4", "MUFACE")
T.glos("Fondo especial", "Fondo formado por los bienes, derechos y acciones de las Mutualidades, Asociaciones y Montepíos integrados en MUFACE (disp. adic. 6.ª RDLeg 4/2000).", "s5", "MUFACE")
T.glos("Contingencia", "Situación de necesidad protegida: asistencia sanitaria, incapacidad temporal, incapacidad permanente, cargas familiares (art. 11 RDLeg 4/2000).", "s7", "Acción protectora")
T.glos("Incapacidad temporal", "Situación del funcionario que, por enfermedad o accidente, está impedido temporalmente para sus funciones, recibe asistencia sanitaria de MUFACE y tiene licencia (art. 19).", "s9", "Mutualismo")
T.glos("Gran invalidez", "Incapacidad permanente absoluta con necesidad de asistencia de otra persona para los actos más elementales de la vida (art. 23.2 d).", "s10", "Mutualismo")
T.glos("Asistencia social", "Servicios y auxilios económicos que MUFACE dispensa en estados y situaciones de necesidad, con el límite de sus créditos (art. 31).", "s11", "Mutualismo")
T.glos("Derechos pasivos", "Derechos a las prestaciones de Clases Pasivas: solo por ley; inembargables, irrenunciables, inalienables e imprescriptibles (RDLeg 670/1987, arts. 5 y 6).", "s14", "Clases Pasivas")
T.glos("Cuota de derechos pasivos", "Cotización a Clases Pasivas: 3,86 % del haber regulador de la pensión de jubilación (art. 23.1).", "s16", "Clases Pasivas")
T.glos("Pensión extraordinaria", "Pensión de Clases Pasivas causada por incapacidad, muerte o desaparición en acto de servicio o como consecuencia del mismo (arts. 19.1 y 47).", "s19", "Clases Pasivas")
T.glos("Período de carencia", "Tiempo mínimo de servicios para causar la pensión ordinaria de jubilación: quince años (art. 29).", "s17", "Clases Pasivas")

# Cronología (fechas de los metadatos del BOE)
T.hito("1987", "Real Decreto Legislativo 670/1987, de 30 de abril, texto refundido de Ley de Clases Pasivas del Estado (BOE de 27-5-1987)", "Derechos pasivos y pensiones de Clases Pasivas", "normativo", "s13")
T.hito("1997", "Real Decreto 577/1997, de 18 de abril (BOE de 7-5-1997)", "Estructura de los órganos de gobierno, administración y representación de MUFACE", "normativo", "s4")
T.hito("2000", "Real Decreto Legislativo 4/2000, de 23 de junio, texto refundido de la Ley sobre Seguridad Social de los Funcionarios Civiles del Estado (BOE de 28-6-2000)", "Régimen especial: mecanismos de cobertura, MUFACE y prestaciones del mutualismo", "normativo", "s1")
T.hito("2003", "Real Decreto 375/2003, de 28 de marzo, Reglamento General del Mutualismo Administrativo (BOE de 11-4-2003)", "Desarrollo del RDLeg 4/2000", "normativo", "s8")
T.hito("2010", "Real Decreto-ley 13/2010, de 3 de diciembre (BOE de 3-12-2010)", "Art. 20 (hoy derogado): inclusión en el Régimen General del personal de nuevo ingreso con efectos de 1-1-2011", "normativo", "s1")
T.hito("2015", "Real Decreto Legislativo 8/2015, de 30 de octubre, texto refundido de la LGSS (BOE de 31-10-2015)", "Disposición adicional tercera: Régimen General para el nuevo ingreso desde 1-1-2011", "normativo", "s1")
T.hito("2026", "Real Decreto 466/2026, de 10 de junio (BOE de 12-6-2026)", "El RD 577/1997 pasa a ser el Estatuto de la Mutualidad General de Funcionarias y Funcionarios Civiles del Estado, O.A.", "normativo", "s4")

T.publicar()
