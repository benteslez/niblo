# -*- coding: utf-8 -*-
"""Tema IV.8 (B4T08): La expropiación forzosa: concepto, naturaleza y elementos.
Procedimientos de expropiación. Garantías jurisdiccionales.
Método del I.2. Norma: Ley de 16 de diciembre de 1954 sobre expropiación forzosa
(texto consolidado del BOE) y art. 33.3 CE. La LEF es preconstitucional: su texto
conserva menciones al «Fuero de los Españoles» y al «Gobernador civil»; se citan
literalmente y se advierte de ello."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

T = Tema("B4T08",
  "Cuatro preguntas: I. Qué es la expropiación y quiénes intervienen (art. 33.3 CE; LEF, arts. 1 a 5, 7 y 8) · II. Cómo se expropia: el procedimiento general (LEF, arts. 9 a 13, 15, 17 a 26, 29, 30, 32 a 36, 43 y 47 a 58) · III. Otros procedimientos y la ocupación temporal (arts. 59, 108 y 109) · IV. Cómo se defiende el expropiado: garantías jurisdiccionales (arts. 35.2, 125 y 126). Cada artículo: texto literal del BOE y ficha.",
  ["Art. 33.3 CE", "LEF", "Beneficiario", "Utilidad pública", "Necesidad de ocupación", "Justo precio", "Jurado de expropiación", "Premio de afección", "Urgente ocupación", "Reversión", "Retasación", "Interdictos", "Recurso contencioso"])

T.ap("s0", "Mapa del tema: cuatro preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque IV, tema 8):
> La expropiación forzosa: concepto, naturaleza y elementos. Procedimientos de expropiación. Garantías jurisdiccionales.

### El hilo conductor

| Bloque | Pregunta | Normas |
|---|---|---|
| **I** | ¿Qué es la expropiación y quiénes intervienen? (concepto y elementos) | CE, art. 33.3; LEF, arts. 1 a 5, 7 y 8 |
| **II** | ¿Cómo se expropia? (procedimiento general) | LEF, arts. 9 a 13, 15, 17 a 26, 29, 30, 32 a 36, 43 y 47 a 58 |
| **III** | ¿Hay otros procedimientos? (especiales y ocupación temporal) | LEF, arts. 59, 108 y 109 |
| **IV** | ¿Cómo se defiende el expropiado? (garantías jurisdiccionales) | LEF, arts. 22.3, 35, 125 y 126 |

!> **La idea que une los cuatro bloques:** la Constitución solo permite privar a alguien de sus bienes con **tres garantías**: **causa** (utilidad pública o interés social), **indemnización** y **procedimiento legal** (art. 33.3). El procedimiento de la LEF desarrolla cada una: declaración de la causa, necesidad de ocupación, **justo precio** y pago; y, si la Administración se las salta, el expropiado tiene **garantías ante los jueces**.

?> **Aviso sobre la norma.** La LEF es de **1954**: su texto vigente conserva expresiones anteriores a la Constitución, como el «Fuero de los Españoles» o el «**Gobernador civil**». Se citan **literalmente**, como dice el BOE; donde el examen ha preguntado por el órgano actual, se explica con su fuente (→ II.2).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué es la expropiación y quiénes intervienen? (art. 33.3 CE; LEF, arts. 1 a 5, 7 y 8)", donde(
  "Primera pregunta del tema: **qué es** la expropiación forzosa, **quién** puede acordarla y **con quién** se tramita.",
  ["1 Garantía constitucional y concepto (art. 33.3 CE; LEF, art. 1)", "2 Sujetos: expropiante, beneficiario, expropiado e interesados (arts. 2 a 5)", "3 Transmisiones y cargas (arts. 7 y 8)"]))

T.ap("s1", "I.1 Garantía constitucional y concepto (art. 33.3 CE; LEF, art. 1)", f"""
{unidad("1.1 Las tres garantías de la Constitución (art. 33.3)",
  lit("CE", "Artículo 33", ["por causa justificada de utilidad pública o interés social", "mediante la correspondiente indemnización", "de conformidad con lo dispuesto por las leyes"], solo=[3]),
  ficha(c("CE", "Artículo 33", "Nadie"),
        ["::Nadie puede ser privado de sus bienes y derechos salvo con:", "Causa justificada de **utilidad pública o interés social**", "La correspondiente **indemnización**", "Conformidad con lo dispuesto por las **leyes** (procedimiento)"],
        "La propiedad y la herencia tienen una función social que delimita su contenido (33.2)",
        "Es un derecho de la Sección 2.ª del Capítulo segundo (→ tema I.2): vincula a los poderes públicos y solo la ley puede regularlo",
        "Tres garantías: **causa**, **indemnización** y **ley**. «utilidad pública **o** interés social»."))}

{unidad("1.2 Concepto legal de expropiación (LEF, art. 1)",
  lit("LEF", "aprimero", ["cualquier forma de privación singular de la propiedad privada o de derechos o intereses patrimoniales legítimos", "acordada imperativamente", "ya implique venta, permuta, censo, arrendamiento, ocupación temporal o mera cesación de su ejercicio", "Quedan fuera del ámbito de esta Ley las ventas forzosas"]),
  fichab("Toda privación **singular** e **imperativa** de la propiedad o de derechos o intereses patrimoniales legítimos",
         c("LEF", "aprimero", "cualesquiera que fueren las personas o Entidades a que pertenezcan"),
         f"{c('LEF', 'aprimero', 'acordada imperativamente')}, por causa de utilidad pública o interés social",
         "—",
         "Comprende no solo la venta: también **permuta, censo, arrendamiento, ocupación temporal o mera cesación** del ejercicio. Excluidas las **ventas forzosas** de abastecimientos, comercio exterior y divisas."))}
""", 2)

T.ap("s2", "I.2 Sujetos: expropiante, beneficiario, expropiado e interesados (arts. 2 a 5)", f"""
{unidad("2.1 Quién expropia y quién se beneficia (art. 2)",
  lit("LEF", "asegundo", ["sólo podrá ser acordada por el Estado, la Provincia o el Municipio", "las entidades y concesionarios a los que se reconozca legalmente esta condición", "cualquier persona natural o jurídica"]),
  fichab("Titulares de la potestad expropiatoria y beneficiarios",
         ["::Expropiante (acuerda la expropiación):", "El Estado", "La Provincia", "El Municipio"],
         ["Beneficiario por **utilidad pública**: entidades y concesionarios a los que la ley reconozca esa condición", "Beneficiario por **interés social**: además, cualquier persona natural o jurídica que reúna los requisitos de la ley especial"],
         "—",
         "Solo **tres** pueden **acordar** la expropiación: Estado, Provincia y Municipio (pregunta oficial P 67, → Cierre 1). Expropiante ≠ beneficiario."))}

{unidad("2.2 Con quién se entiende el expediente (arts. 3 a 5)",
  lit("LEF", "atercero", ["en primer lugar, con el propietario de la cosa o titular del derecho objeto de la expropiación", "que sólo puede ser destruida judicialmente"]),
  lit("LEF", "aquinto", ["con el Ministerio Fiscal"], solo=[1]),
  fichab("Interesados en el expediente",
         ["El propietario o titular del derecho, **en primer lugar** (art. 3.1)", "Titulares de derechos reales e intereses económicos directos y arrendatarios, si lo solicitan (art. 4)", "El **Ministerio Fiscal**, si no comparecen o están incapacitados sin representante o la propiedad es litigiosa (art. 5.1)", "Quienes presenten títulos contradictorios (art. 5.2)"],
         "Se presume propietario quien conste en registros públicos que produzcan presunción de titularidad; en su defecto, en registros fiscales",
         "—",
         "El expediente se entiende «en primer lugar, con el **propietario**» (pregunta oficial X 58, → Cierre 1), no con el poseedor ni con el Ayuntamiento."))}
""", 2)

T.ap("s3", "I.3 Transmisiones y cargas (arts. 7 y 8)", f"""
{unidad("3.1 Las transmisiones no paran el expediente (art. 7)",
  lit("LEF", "aseptimo", ["no impedirán la continuación de los expedientes de expropiación forzosa", "Se considerará subrogado el nuevo titular"]),
  fichab("Efecto de las transmisiones durante el expediente", "El nuevo titular", "Se subroga en las obligaciones y derechos del anterior", "—",
         "Ni suspensión, ni retroacción, ni caducidad: el expediente **continúa** (pregunta oficial P 68, → Cierre 1)."))}

{unidad("3.2 Adquisición libre de cargas (art. 8)",
  lit("LEF", "aoctavo", ["se adquirirá libre de cargas", "si resultase compatible con el nuevos destino"]),
  fichab("Situación jurídica del bien expropiado", "Expropiante y titular del derecho real", "Libre de cargas, salvo derecho real compatible con el nuevo destino y acuerdo entre las partes", "—",
         "Regla: **libre de cargas**; excepción con **dos** requisitos (compatibilidad y acuerdo)."))}

{resumen([
  "Art. 33.3 CE: **causa** (utilidad pública o interés social), **indemnización** y **conformidad con las leyes**.",
  "Expropiación: cualquier privación **singular** e **imperativa** de la propiedad o de derechos patrimoniales legítimos (LEF, art. 1).",
  "Acuerdan la expropiación **Estado, Provincia y Municipio**; beneficiarios, los que diga la ley (art. 2).",
  "El expediente se entiende, en primer lugar, con el **propietario** (art. 3); las transmisiones no lo paran (art. 7); el bien se adquiere **libre de cargas** (art. 8)."],
  "Siguiente: II. ¿Cómo se expropia? El procedimiento general")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Cómo se expropia? El procedimiento general (LEF, arts. 9 a 13, 15, 17 a 26, 29, 30, 32 a 36, 43 y 47 a 58)", donde(
  "Segunda pregunta. El procedimiento general sigue el orden de las garantías del art. 33.3: primero la **causa**, después **qué bienes** hacen falta, luego **cuánto** se paga y, por último, el **pago** y la **ocupación**.",
  ["1 Causa: declaración de utilidad pública o interés social (arts. 9 a 13)", "2 Necesidad de ocupación (arts. 15 y 17 a 23)", "3 Justo precio: acuerdo, hojas de aprecio y Jurado (arts. 24 a 26, 29, 30, 32 a 36, 43 y 47)", "4 Pago y ocupación; ocupación urgente (arts. 48 a 53)", "5 Reversión, demora y retasación (arts. 54 a 58)"]))

T.ap("s4", "II.1 La causa: declaración de utilidad pública o interés social (arts. 9 a 13)", f"""
{unidad("1.1 Requisito previo (art. 9)",
  lit("LEF", "anoveno", ["será indispensable la previa declaración de utilidad pública o interés social"]),
  fichab("Primer requisito del procedimiento: declarar la causa", "—", "Declaración **previa** de utilidad pública o interés social del fin", "—", "Sin declaración previa, la ocupación es una vía de hecho (→ IV.1)."))}

{unidad("1.2 Cómo se declara la utilidad pública o el interés social (arts. 10 a 13)",
  lit("LEF", "adiez", ["se entiende implícita", "por acuerdo del Consejo de Ministros"]),
  lit("LEF", "aonce", ["mediante Ley aprobada en Cortes"]),
  lit("LEF", "adoce", ["expresa y singularmente mediante Ley en cada caso", "bastará el acuerdo del Consejo de Ministros"]),
  lit("LEF", "atrece", ["al mismo procedimiento previsto en el artículo anterior"]),
  fichab("Formas de declarar la utilidad pública o el interés social",
         "Las Cortes (por ley) o el Consejo de Ministros, según el caso",
         ["Inmuebles: **implícita** en los planes de obras y servicios del Estado, Provincia y Municipio (art. 10)", "Utilidad pública declarada genéricamente por ley: reconocimiento en cada caso por **Consejo de Ministros** (art. 10)", "Resto de inmuebles: **ley** aprobada en Cortes (art. 11)", "Muebles: **ley** expresa y singular en cada caso, o Consejo de Ministros si una ley autorizó la categoría (art. 12)", f"Interés social (art. 13): {c('LEF', 'atrece', 'se sujetará, en cuanto a su declaración, al mismo procedimiento previsto en el artículo anterior')}, es decir, el del art. 12"],
         "—",
         "Para **inmuebles** de planes de obras y servicios, la utilidad pública es **implícita**; para **muebles**, por **ley** en cada caso (salvo categoría autorizada)."))}
""", 2)

T.ap("s5", "II.2 La necesidad de ocupación (arts. 15 y 17 a 23)", f"""
{unidad("2.1 Qué es y quién la promueve (arts. 15 y 17)",
  lit("LEF", "aquince", ["que sean estrictamente indispensables para el fin de la expropiación", "previsibles ampliaciones"]),
  lit("LEF", "adiecisiete", ["relación concreta e individualizada", "se entenderá implícita en la aprobación del proyecto"]),
  fichab("Determinar qué bienes concretos hacen falta", "La Administración resuelve; el **beneficiario** formula la relación de bienes",
         ["Solo los **estrictamente indispensables** (art. 15)", "Previsibles ampliaciones: por acuerdo del **Consejo de Ministros** (art. 15)", "Si el proyecto describe los bienes, la necesidad es **implícita** en su aprobación (art. 17.2)"],
         "—", "La relación concreta e individualizada la formula el **beneficiario**."))}

{unidad("2.2 Información pública y resolución (arts. 18 a 21)",
  lit("LEF", "adieciocho", ["el Gobernador civil abrirá información pública durante un plazo de quince días"], solo=[1]),
  lit("LEF", "aveinte", ["el Gobernador civil", "resolverá, en el plazo máximo de veinte días, sobre la necesidad de la ocupación"]),
  lit("LEF", "aveintiuno", ["inicia el expediente expropiatorio"]),
  lit("LOFAGE", "dacuarta", ["el Delegado del Gobierno desempeñará las demás competencias que la legislación vigente atribuye a los Gobernadores Civiles"], solo=[3], titulo="Disposición adicional cuarta (Ley 6/1997, LOFAGE, hoy DEROGADA por la Ley 40/2015)"),
  fichab("Información pública y acuerdo de necesidad de ocupación",
         f"El texto de la LEF dice {c('LEF', 'aveinte', 'el Gobernador civil')}; la Ley 6/1997 (LOFAGE) atribuyó al **Delegado del Gobierno** las demás competencias de los Gobernadores civiles (disposición adicional cuarta), hoy derogada por la Ley 40/2015",
         ["Información pública: **15 días** (art. 18.1); cualquier persona puede alegar (art. 19)", "Resolución sobre la necesidad: máximo **20 días** (art. 20)", "El acuerdo **inicia el expediente** y se publica y notifica (art. 21)"],
         "Información pública 15 días; resolución 20 días",
         "El examen (P 66) dio por buena la respuesta «**Delegado del Gobierno**» (→ Cierre 1). El acuerdo de necesidad de ocupación **inicia** el expediente expropiatorio."))}

{unidad("2.3 Recurso contra la necesidad de ocupación (art. 22) y expropiación total (art. 23)",
  lit("LEF", "aveintidos", ["recurso de alzada ante el Ministerio correspondiente", "será de diez días", "en el plazo de veinte días", "surtirá efectos suspensivos", "no cabrá reclamar en la vía contencioso-administrativa"]),
  lit("LEF", "aveintitres", ["resulte antieconómica para el propietario la conservación de la parte de finca no expropiada", "en el plazo de diez días"]),
  fichab("Impugnación del acuerdo de necesidad de ocupación",
         "Interesados y quienes comparecieron en la información pública; resuelve el **Ministerio correspondiente**",
         ["Recurso de **alzada** con efectos **suspensivos** (art. 22)", "Expropiación total si la parte no expropiada resulta antieconómica (art. 23)"],
         "Interposición: **10 días**; resolución: **20 días**; expropiación total: decisión en **10 días**",
         "Alzada ante el **Ministerio** (pregunta oficial L 54, → Cierre 1). El art. 22.3 excluye literalmente la vía contencioso-administrativa contra la orden ministerial; el art. 126.1 lo repite como excepción (→ IV.2)."))}
""", 2)

T.ap("s6", "II.3 El justo precio: acuerdo, hojas de aprecio y Jurado (arts. 24 a 26, 29, 30, 32 a 36, 43 y 47)", f"""
{unidad("3.1 Mutuo acuerdo (art. 24) y pieza separada (arts. 25 y 26)",
  lit("LEF", "aveinticuatro", ["libremente y por mutuo acuerdo", "en el plazo de quince días"]),
  lit("LEF", "aveinticinco", ["Una vez firme el acuerdo por el que se declara la necesidad de ocupación"]),
  fichab("Adquisición amistosa y apertura del justiprecio", "Administración y particular",
         ["Mutuo acuerdo en cualquier momento; si no lo hay en **15 días**, sigue el procedimiento (art. 24)", "Firme la necesidad de ocupación, se fija el justo precio (art. 25) en **pieza separada** (art. 26)"],
         "15 días para el mutuo acuerdo", "El mutuo acuerdo cabe **también después**, en cualquier estado de la tramitación."))}

{unidad("3.2 Hojas de aprecio (arts. 29 y 30)",
  lit("LEF", "aveintinueve", ["en el plazo de veinte días", "presenten hoja de aprecio", "habrá de ser forzosamente motivada"]),
  lit("LEF", "atreinta", ["en igual plazo de veinte días", "dentro de los diez días siguientes"]),
  fichab("Intercambio de valoraciones", "Propietario y Administración expropiante",
         ["Propietario: hoja de aprecio motivada (art. 29)", "Administración: la acepta (justo precio fijado) o extiende hoja de aprecio fundada (art. 30)", "Propietario: la acepta o la rechaza con alegaciones (art. 30.2)"],
         "Propietario **20 días**; Administración **20 días**; respuesta del propietario **10 días**",
         "Plazos 20 / 20 / 10. Si la Administración **acepta** la hoja del propietario, el justo precio queda **fijado definitivamente**."))}

{unidad("3.3 El Jurado provincial de expropiación (arts. 32 a 35)",
  lit("LEF", "atreintaydos", ["el Magistrado que designe el Presidente de la audiencia correspondiente", "cuatro vocales"], solo=[1, 2, 3, 4, 5, 6]),
  lit("LEF", "atreintaycuatro", ["decidirá ejecutoriamente sobre el justo precio"]),
  lit("LEF", "atreintaycinco", ["necesariamente motivada", "ultimará la vía gubernativa", "tan sólo el recurso contencioso-administrativo"], solo=[1, 2]),
  fichab("Órgano que fija el justo precio si no hay acuerdo",
         ["::Jurado provincial (art. 32):", "Presidente: un **Magistrado** designado por el Presidente de la Audiencia", "Vocales: Abogado del Estado; dos funcionarios técnicos; representante de la Cámara o colegio según el bien; Notario; Interventor territorial"],
         "Decide **ejecutoriamente** a la vista de las dos hojas de aprecio (art. 34); resolución **motivada** (art. 35.1)",
         "Por mayoría de votos (art. 33.2)",
         "Su resolución **ultima la vía gubernativa**: contra ella solo cabe el **recurso contencioso-administrativo** (art. 35.2 → IV.2)."))}

{unidad("3.4 Criterios de valoración y premio de afección (arts. 36, 43 y 47)",
  lit("LEF", "atreintayseis", ["al tiempo de iniciarse el expediente de justiprecio", "sin tenerse en cuenta las plusvalías"], solo=[1]),
  lit("LEF", "acuarentaytres", ["No será en ningún caso de aplicación a las expropiaciones de bienes inmuebles", "ley que regule la valoración del suelo"], solo=[2, 3]),
  lit("LEF", "acuarentasiete", ["un cinco por ciento como premio de afección"]),
  fichab("Cómo se calcula y qué se añade",
         "—",
         ["Valor al tiempo de **iniciarse el expediente de justiprecio**, sin plusvalías del proyecto ni futuras (art. 36.1)", "Inmuebles: **solo** el sistema de la ley de valoración del suelo; el régimen estimativo del art. 43 no se aplica (art. 43.2 a)", "**Premio de afección**: un **5 %** además del justo precio, en todos los casos (art. 47)"],
         "—",
         "Premio de afección: **cinco por ciento**, «En todos los casos de expropiación»."))}
""", 2)

T.ap("s7", "II.4 Pago y ocupación; la ocupación urgente (arts. 48 a 53)", f"""
{unidad("4.1 Pago, consignación y ocupación (arts. 48 a 51 y 53)",
  lit("LEF", "acuarentayocho", ["en el plazo máximo de seis meses"], solo=[1]),
  lit("LEF", "acincuenta", ["se consignará el justiprecio", "Caja General de Depósitos"], solo=[1]),
  lit("LEF", "acincuentayuno", ["Hecho efectivo el justo precio, o consignado", "podrá ocuparse la finca por vía administrativa"], solo=[1]),
  fichab("Del justo precio a la toma de posesión", "La Administración expropiante (o el beneficiario)",
         ["Pago en el plazo máximo de **seis meses** (art. 48.1); exento de gastos e impuestos (art. 49)", "Si el propietario rehúsa o hay litigio: **consignación** en la Caja General de Depósitos (art. 50)", "Pagado o consignado, **ocupación** por vía administrativa (art. 51); el acta de ocupación es título para el Registro (art. 53)"],
         "Pago: máximo **6 meses**",
         "Regla general: **primero pagar** (o consignar), **después ocupar**. La excepción es la ocupación urgente (→ II.4.2)."))}

{unidad("4.2 La ocupación urgente (art. 52)",
  lit("LEF", "acincuentaydos", ["Excepcionalmente y mediante acuerdo del Consejo de Ministros", "retención de crédito", "dará derecho a su ocupación inmediata", "con una antelación mínima de ocho días"], solo=[1, 2, 3]),
  fichab("Procedimiento excepcional: ocupar antes de fijar y pagar el justo precio",
         "El **Consejo de Ministros** la declara",
         ["Se entiende cumplida la necesidad de ocupación y da derecho a ocupar de inmediato", "Acta previa a la ocupación, notificada con **8 días** de antelación mínima", "Depósito previo e indemnización por rapidez de la ocupación (52.4 y 52.5); después, justiprecio y pago por la vía general (52.7)"],
         "Notificación del acta previa: al menos **8 días** antes",
         "Es **excepcional** y la acuerda el **Consejo de Ministros**, con **retención de crédito** en el expediente."))}
""", 2)

T.ap("s8", "II.5 Reversión, demora y retasación (arts. 54 a 58)", f"""
{unidad("5.1 La reversión (arts. 54 y 55)",
  lit("LEF", "acincuentaycuatro", ["no ejecutarse la obra o no establecerse el servicio", "podrán recobrar la totalidad o la parte sobrante", "se prolongue durante diez años", "el de tres meses", "no hubieran transcurrido veinte años", "transcurrido cinco años", "suspendidas más de dos años"], solo=[1, 2, 3, 4, 5, 6, 7, 8, 9]),
  lit("LEF", "acincuentaycinco", ["la restitución de la indemnización expropiatoria percibida por el expropiado, actualizada"], solo=[1]),
  fichab("Derecho del expropiado a recuperar el bien si no se usa para su fin",
         "El primitivo dueño o sus causahabientes",
         ["Supuestos: obra o servicio no ejecutado, parte sobrante o desaparición de la afectación (art. 54.1)", "Excluida si hay nueva afectación de utilidad pública o interés social, o si la afectación duró **10 años** (art. 54.2)", "Presupuesto: restituir la indemnización **actualizada** (art. 55.1)"],
         "Solicitud: **3 meses** desde la notificación; sin notificación: exceso o desafectación (20 años), obra no iniciada (5 años), suspensión imputable (más de 2 años)",
         "Cifras que se cruzan: **10** años de afectación excluyen la reversión; **3 meses** para pedirla si hubo notificación; **5** años sin iniciar la obra; **20** años como máximo para excesos o desafectación."))}

{unidad("5.2 Intereses de demora y retasación (arts. 56 a 58)",
  lit("LEF", "acincuentayseis", ["Cuando hayan transcurrido seis meses desde la iniciación legal del expediente expropiatorio", "el interés legal del justo precio"]),
  lit("LEF", "acincuentaysiete", ["devengará el interés legal"]),
  lit("LEF", "acincuentayocho", ["Si transcurrieran cuatro años", "evaluar de nuevo", "no procederá el derecho a la retasación"]),
  fichab("Consecuencias del retraso",
         "La Administración culpable de la demora",
         ["Demora en **fijar** el justo precio: interés legal si pasan **6 meses** desde la iniciación del expediente (art. 56)", "Demora en **pagar**: interés legal desde los 6 meses del art. 48 (art. 57)", "**Retasación**: si pasan **4 años** sin pagar ni consignar (art. 58)"],
         "6 meses (intereses) · 4 años (retasación)",
         "Retasación a los **cuatro años**; si ya se pagó o consignó, **no** hay retasación aunque pasen los cuatro años."))}

{resumen([
  "Causa: declaración **previa** de utilidad pública o interés social (art. 9); implícita en los planes de obras y servicios para inmuebles (art. 10).",
  "Necesidad de ocupación: información pública **15 días**; resolución **20 días**; **inicia** el expediente; alzada ante el **Ministerio** en **10 días**, con efectos suspensivos (arts. 18 a 22).",
  "Justo precio: mutuo acuerdo; hojas de aprecio **20/20/10 días**; **Jurado provincial** presidido por un Magistrado; **premio de afección del 5 %**.",
  "Pago en **6 meses**; ocupación tras pagar o consignar; **ocupación urgente** por el **Consejo de Ministros**; **reversión**, intereses y retasación a los **4 años**."],
  "Siguiente: III. ¿Hay otros procedimientos? Especiales y ocupación temporal")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Hay otros procedimientos? Especiales y ocupación temporal (arts. 59, 108 y 109)", donde(
  "Tercera pregunta. Además del procedimiento general, la LEF regula **procedimientos especiales** (Título III) y la **ocupación temporal** de terrenos (Título IV).",
  ["1 Los procedimientos especiales: el ejemplo de la expropiación por zonas (art. 59)", "2 La ocupación temporal (arts. 108 y 109)"]))

T.ap("s9", "III.1 Los procedimientos especiales: el ejemplo de la expropiación por zonas (art. 59)", f"""
*Esquema de elaboración propia (rúbricas del Título III de la LEF, texto consolidado del BOE): expropiación por zonas o grupos de bienes; por incumplimiento de la función social de la propiedad; de bienes de valor artístico, histórico y arqueológico; por Entidades locales o por razón de urbanismo; con traslado de poblaciones; por causa de colonización o de obras públicas; en materia de propiedad industrial; y por razones de defensa nacional y seguridad del Estado.*

{unidad("1.1 Expropiación por zonas o grupos de bienes (art. 59)",
  lit("LEF", "acincuentaynueve", ["grandes zonas territoriales o series de bienes susceptibles de una consideración de conjunto", "el Consejo de Ministros podrá acordar, mediante Decreto"]),
  fichab("Procedimiento especial para expropiaciones de conjunto", "El **Consejo de Ministros**, mediante **Decreto**", "Aplica el procedimiento especial del capítulo", "—", "Lo decide el **Consejo de Ministros por Decreto**."))}
""", 2)

T.ap("s9b", "III.2 La ocupación temporal (arts. 108 y 109)", f"""
{unidad("2.1 Ocupación temporal (arts. 108 y 109)",
  lit("LEF", "acientoocho", ["podrán ocupar temporalmente los terrenos propiedad del particular"], solo=[1, 2, 3, 4, 5]),
  lit("LEF", "acientonueve", ["Las viviendas quedan exceptuadas de la ocupación temporal e imposición de servidumbres", "permiso expreso de su morador"]),
  fichab("Ocupación temporal de terrenos de particulares", "La Administración y quienes se hayan subrogado en sus derechos",
         ["Estudios u operaciones facultativas de corta duración", "Estaciones, caminos provisionales, talleres, almacenes y depósitos para obras de utilidad pública", "Extracción de materiales para esas obras", "Trabajos por causa de interés social"],
         "—", "**Viviendas** excluidas: solo con **permiso expreso del morador** (art. 109)."))}

{resumen([
  "Título III: ocho procedimientos especiales; por zonas o grupos de bienes, lo acuerda el **Consejo de Ministros por Decreto** (art. 59).",
  "Ocupación temporal en cuatro supuestos (art. 108); las **viviendas** quedan exceptuadas salvo permiso del morador (art. 109)."],
  "Siguiente: IV. ¿Cómo se defiende el expropiado? Garantías jurisdiccionales")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Cómo se defiende el expropiado? Garantías jurisdiccionales (arts. 35.2, 125 y 126)", donde(
  "Cuarta pregunta. Si la Administración ocupa **sin respetar** las garantías, o si el expropiado no está de acuerdo con el resultado, la LEF le abre la vía judicial (Título V, «Garantías jurisdiccionales»).",
  ["1 Frente a la vía de hecho: los interdictos (art. 125)", "2 El recurso contencioso-administrativo (arts. 35.2 y 126)"]))

T.ap("s10", "IV.1 Frente a la vía de hecho: los interdictos (art. 125)", f"""
{unidad("1.1 Ocupación sin los requisitos sustanciales (art. 125)",
  lit("LEF", "acientoveinticinco", ["declaración de utilidad pública o interés social, necesidad de ocupación y previo pago o depósito", "los interdictos de retener y recobrar"]),
  fichab("Defensa posesoria frente a la ocupación ilegal", "El interesado, ante los **Jueces**",
         ["::Cuando la Administración ocupa o intenta ocupar sin:", "Declaración de utilidad pública o interés social", "Necesidad de ocupación", "Previo pago o depósito"],
         "—", "Son **interdictos de retener y recobrar** (protección de la posesión), «aparte de los demás medios legales procedentes»."))}
""", 2)

T.ap("s11", "IV.2 El recurso contencioso-administrativo (arts. 35.2 y 126)", f"""
{unidad("2.1 La resolución del Jurado agota la vía administrativa (art. 35.2)",
  lit("LEF", "atreintaycinco", ["ultimará la vía gubernativa y contra la misma procederá tan sólo el recurso contencioso-administrativo"], solo=[2]),
  fichab("Impugnación del justiprecio del Jurado", "Administración y propietario", "Directamente recurso contencioso-administrativo", "—", "Contra el Jurado **no** hay recurso administrativo: «tan sólo» el contencioso."))}

{unidad("2.2 Contra la resolución final y el justo precio (art. 126)",
  lit("LEF", "acientoveintiseis", ["con excepción del caso previsto en el número tercero del artículo veintidós", "en más de una sexta parte", "vicio sustancial de forma", "de turno preferente"]),
  fichab("Recurso contencioso-administrativo en materia expropiatoria",
         "Ambas partes (expropiado y Administración o beneficiario)",
         ["Contra la resolución que pone fin al expediente o a cualquier pieza separada, salvo el art. 22.3", "Contra el justo precio: fundado en **lesión** si la diferencia supera **una sexta parte**", "Siempre: vicio sustancial de forma o infracción de la LEF", "Recursos de **turno preferente**"],
         "Lesión: diferencia de **más de una sexta parte**",
         "La **sexta parte** es el umbral de la lesión. La única excepción a la vía contenciosa es la del **art. 22.3** (necesidad de ocupación tras la alzada)."))}


*Cuadro de plazos de la LEF (esquema de elaboración propia sobre los artículos citados; no es texto legal).*

| Trámite | Plazo | Artículo |
|---|---|---|
| Información pública de la relación de bienes | 15 días | 18.1 |
| Resolución sobre la necesidad de ocupación | 20 días | 20 |
| Alzada contra la necesidad de ocupación: interposición / resolución | 10 / 20 días | 22.2 y 3 |
| Mutuo acuerdo sobre el precio | 15 días | 24 |
| Hoja de aprecio del propietario / respuesta de la Administración / del propietario | 20 / 20 / 10 días | 29 y 30 |
| Pago del justo precio | 6 meses | 48.1 |
| Intereses por demora en fijar el precio | desde los 6 meses | 56 |
| Retasación | 4 años sin pagar ni consignar | 58 |
| Acta previa en la ocupación urgente | 8 días de antelación | 52.2 |
| Reversión: solicitud tras notificación | 3 meses | 54.3 |

{resumen([
  "Ocupación sin causa, sin necesidad de ocupación o sin previo pago o depósito: **interdictos de retener y recobrar** ante los Jueces (art. 125).",
  "Contencioso contra la resolución final o las piezas separadas, **salvo el art. 22.3**; contra el justo precio, por **lesión** de más de **una sexta parte** (art. 126).",
  "Contra la resolución del Jurado, **solo** el contencioso (art. 35.2)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}""", 2)

# =============================================================================
EX = [
 ("L", 54, "Recurso contra la necesidad de ocupación (→ II.2.3)", {
   "a": "La LEF no prevé recurso de súplica; el recurso es de **alzada** ante el **Ministerio**.",
   "b": f"No es reposición ante el Subdelegado: {c('LEF', 'aveintidos', 'se dará recurso de alzada ante el Ministerio correspondiente')}.",
   "c": "El recurso de revisión no es el previsto: el art. 22 regula la **alzada** ante el **Ministerio**.",
   "d": f"Literal del art. 22.1: {c('LEF', 'aveintidos', 'se dará recurso de alzada ante el Ministerio correspondiente')}."},
   [("Recurso de alzada ante el Ministerio correspondiente", "LEF", "aveintidos", "se dará recurso de alzada ante el Ministerio correspondiente")]),
 ("P", 66, "Órgano que resuelve la necesidad de ocupación (→ II.2.2)", {
   "a": "El Ministerio resuelve la **alzada** contra el acuerdo (art. 22), no el acuerdo de necesidad de ocupación.",
   "b": "El Consejo de Ministros interviene para incluir previsibles ampliaciones (art. 15) o declarar la ocupación urgente (art. 52), no para resolver la necesidad de ocupación ordinaria.",
   "c": f"El art. 20 LEF dice {c('LEF', 'aveinte', 'el Gobernador civil')}; la LOFAGE (Ley 6/1997, disposición adicional cuarta, hoy derogada) dispuso que {c('LOFAGE', 'dacuarta', 'el Delegado del Gobierno desempeñará las demás competencias que la legislación vigente atribuye a los Gobernadores Civiles')}. Es la respuesta de la plantilla.",
   "d": "El Secretario de Estado no aparece en la LEF como órgano de este trámite."},
   [("Delegado del Gobierno", "LOFAGE", "dacuarta", "el Delegado del Gobierno desempeñará las demás competencias que la legislación vigente atribuye a los Gobernadores Civiles")]),
 ("P", 67, "Titulares de la potestad expropiatoria (→ I.2.1)", {
   "a": f"Falta la **Provincia** y sobran los organismos públicos: {c('LEF', 'asegundo', 'sólo podrá ser acordada por el Estado, la Provincia o el Municipio')}.",
   "b": "Los organismos públicos no figuran en el art. 2.1; podrán ser, en su caso, **beneficiarios** (art. 2.2).",
   "c": "Falta el **Municipio** y sobran los organismos públicos.",
   "d": f"Literal del art. 2.1: {c('LEF', 'asegundo', 'sólo podrá ser acordada por el Estado, la Provincia o el Municipio')}."},
   [("El Estado, la Provincia y el Municipio", "LEF", "asegundo", "La expropiación forzosa sólo podrá ser acordada por el Estado, la Provincia o el Municipio.")]),
 ("P", 68, "Transmisiones durante el expediente (→ I.3.1)", {
   "a": f"No impiden la continuación: {c('LEF', 'aseptimo', 'no impedirán la continuación de los expedientes de expropiación forzosa')}.",
   "b": "La LEF no obliga a suspender ni a retrotraer: el nuevo titular se **subroga**.",
   "c": "No hay caducidad: el expediente **continúa** y el adquirente se subroga.",
   "d": f"Literal del art. 7: {c('LEF', 'aseptimo', 'no impedirán la continuación de los expedientes de expropiación forzosa')} y {c('LEF', 'aseptimo', 'Se considerará subrogado el nuevo titular en las obligaciones y derechos del anterior')}."},
   [("No impiden la continuación del expediente", "LEF", "aseptimo", "no impedirán la continuación de los expedientes de expropiación forzosa"), ("subrogada", "LEF", "aseptimo", "Se considerará subrogado el nuevo titular")]),
 ("X", 58, "Con quién se entienden las actuaciones (→ I.2.2)", {
   "a": f"No con cualquier poseedor: {c('LEF', 'atercero', 'en primer lugar, con el propietario de la cosa o titular del derecho objeto de la expropiación')}.",
   "b": f"Literal del art. 3.1: {c('LEF', 'atercero', 'en primer lugar, con el propietario de la cosa o titular del derecho objeto de la expropiación')}.",
   "c": "El Ayuntamiento no es el interesado: recibe comunicación de la relación de bienes (art. 18.2), pero las actuaciones se entienden con el propietario.",
   "d": "Los arrendatarios intervienen si lo solicitan (art. 4.1), no «en primer lugar»."},
   [("Con el propietario de la cosa o titular del derecho objeto de la expropiación", "LEF", "atercero", "en primer lugar, con el propietario de la cosa o titular del derecho objeto de la expropiación")]),
]
bloques = []
for cod, n, tit, por, ap_ in EX:
    bloques += [f"### {('GACE-L' if cod == 'L' else 'GACE-P' if cod == 'P' else 'GACE-L extraordinario')} 2025, pregunta {n} · {tit}", examen(cod, n, por, ap_)]
T.ap("s12", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join(
  ["En los primeros ejercicios de **2025** cayeron **cinco** preguntas de este tema, todas literales de la LEF. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal."]
  + bloques + ["### Cómo se pregunta", "!> Casi todas citan el **número del artículo** de la LEF y cambian **un órgano** (Ministerio, Delegado, Consejo de Ministros), **un sujeto** (propietario, poseedor, arrendatario) o **un efecto** (continuar, suspender, caducar). Aprende quién hace cada trámite."]))

T.ap("s13", "Cierre 2. Repaso en 10 minutos (por bloques)", """
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Concepto y sujetos | Causa, indemnización y ley (33.3 CE); privación singular e imperativa (art. 1); Estado, Provincia y Municipio (art. 2) | Expediente, **en primer lugar**, con el **propietario** (art. 3); las transmisiones **no** lo paran (art. 7) |
| II. Procedimiento general | Causa → necesidad de ocupación → justo precio → pago y ocupación | Alzada ante el **Ministerio** (art. 22); **premio de afección 5 %** (art. 47); pago en **6 meses** |
| III. Otros procedimientos | Ocho especiales; ocupación temporal | Viviendas exceptuadas de la ocupación temporal |
| IV. Garantías | Interdictos (art. 125); contencioso (art. 126) | Lesión: **más de una sexta parte** |

?> **Trampas frecuentes:** «la expropiación la acuerdan los organismos públicos» (solo Estado, Provincia y Municipio; los demás pueden ser **beneficiarios**); «reposición ante el Subdelegado» (es **alzada ante el Ministerio**); «retasación a los dos años» (son **cuatro**); «premio de afección del 10 %» (es el **5 %**).
""")

# =============================================================================
Q = [
 ("CE", "Artículo 33", "Concepto", "Según el artículo 33.3 de la Constitución, nadie podrá ser privado de sus bienes y derechos sino por causa justificada de:",
  ["Utilidad pública o interés social.", "Interés general o necesidad urgente.", "Utilidad pública exclusivamente.", "Seguridad nacional o interés social."], "Art. 33.3 CE.", "por causa justificada de utilidad pública o interés social"),
 ("LEF", "aprimero", "Concepto", "Según el artículo 1 de la Ley de Expropiación Forzosa, quedan fuera del ámbito de dicha Ley:",
  ["Las ventas forzosas reguladas por la legislación especial sobre abastecimientos, comercio exterior y divisas.", "Las ocupaciones temporales.", "Los arrendamientos acordados imperativamente.", "La mera cesación del ejercicio de derechos patrimoniales acordada imperativamente."], "Art. 1.2 LEF; las demás figuras están incluidas en el art. 1.1.", "Quedan fuera del ámbito de esta Ley las ventas forzosas reguladas por la legislación especial sobre abastecimientos, comercio exterior y divisas"),
 ("LEF", "asegundo", "Sujetos", "Según el artículo 2 de la Ley de Expropiación Forzosa, por causa de interés social podrá ser beneficiario de la expropiación:",
  ["Cualquier persona natural o jurídica en la que concurran los requisitos señalados por la Ley especial.", "Únicamente el Estado, la Provincia y el Municipio.", "Solo los concesionarios de servicios públicos.", "Solo las entidades públicas empresariales."], "Art. 2.3 LEF.", "cualquier persona natural o jurídica en la que concurran los requisitos señalados por la Ley especial"),
 ("LEF", "aquinto", "Sujetos", "Según el artículo 5 de la Ley de Expropiación Forzosa, se entenderán las diligencias con el Ministerio Fiscal cuando, entre otros supuestos:",
  ["La propiedad fuere litigiosa.", "El propietario hubiera aceptado la hoja de aprecio.", "El beneficiario sea una entidad pública.", "Se trate de bienes muebles."], "Art. 5.1 LEF.", "o fuere la propiedad litigiosa"),
 ("LEF", "aoctavo", "Sujetos", "Según el artículo 8 de la Ley de Expropiación Forzosa, la cosa expropiada se adquirirá:",
  ["Libre de cargas.", "Con todas sus cargas.", "Con las cargas inscritas en el Registro de la Propiedad.", "Libre de cargas solo si el beneficiario es el Estado."], "Art. 8 LEF (salvo derecho real compatible con el nuevo destino y acuerdo).", "La cosa expropiada se adquirirá libre de cargas"),
 ("LEF", "anoveno", "Causa", "Según el artículo 9 de la Ley de Expropiación Forzosa, para proceder a la expropiación forzosa será indispensable:",
  ["La previa declaración de utilidad pública o interés social del fin a que haya de afectarse el objeto expropiado.", "El previo pago del justo precio.", "El previo acuerdo del Jurado de expropiación.", "La conformidad del propietario."], "Art. 9 LEF.", "será indispensable la previa declaración de utilidad pública o interés social"),
 ("LEF", "adiez", "Causa", "Según el artículo 10 de la Ley de Expropiación Forzosa, en relación con la expropiación de inmuebles, la utilidad pública se entiende implícita:",
  ["En todos los planes de obras y servicios del Estado, Provincia y Municipio.", "En todos los contratos de obras del sector público.", "En las declaraciones de interés social de las Comunidades Autónomas.", "En toda obra financiada con fondos europeos."], "Art. 10 LEF.", "en todos los planes de obras y servicios del Estado, Provincia y Municipio"),
 ("LEF", "adoce", "Causa", "Según el artículo 12 de la Ley de Expropiación Forzosa, respecto a los bienes muebles, la utilidad pública habrá de ser declarada, como regla:",
  ["Expresa y singularmente mediante Ley en cada caso.", "Por acuerdo del Consejo de Ministros en todo caso.", "Por orden del Ministro competente.", "Implícitamente en los planes de obras."], "Art. 12 LEF (salvo categoría especial autorizada por ley: Consejo de Ministros).", "expresa y singularmente mediante Ley en cada caso"),
 ("LEF", "aquince", "Necesidad de ocupación", "Según el artículo 15 de la Ley de Expropiación Forzosa, ¿mediante qué acuerdo podrán incluirse entre los bienes de necesaria ocupación los indispensables para previsibles ampliaciones de la obra?",
  ["Acuerdo del Consejo de Ministros.", "Acuerdo del Jurado provincial de expropiación.", "Orden del Ministro competente.", "Resolución del Delegado del Gobierno."], "Art. 15 LEF.", "Mediante acuerdo del Consejo de Ministros podrán incluirse también entre los bienes de necesaria ocupación"),
 ("LEF", "adiecisiete", "Necesidad de ocupación", "Según el artículo 17 de la Ley de Expropiación Forzosa, ¿quién está obligado a formular la relación concreta e individualizada de los bienes o derechos de necesaria expropiación?",
  ["El beneficiario de la expropiación.", "El Jurado provincial de expropiación.", "El Ministerio Fiscal.", "El propietario afectado."], "Art. 17.1 LEF.", "el beneficiario de la expropiación estará obligado a formular una relación concreta e individualizada"),
 ("LEF", "adieciocho", "Necesidad de ocupación", "Según el artículo 18 de la Ley de Expropiación Forzosa, recibida la relación de bienes se abrirá información pública durante un plazo de:",
  ["Quince días.", "Diez días.", "Veinte días.", "Un mes."], "Art. 18.1 LEF.", "durante un plazo de quince días"),
 ("LEF", "aveinte", "Necesidad de ocupación", "Según el artículo 20 de la Ley de Expropiación Forzosa, el plazo máximo para resolver sobre la necesidad de la ocupación es de:",
  ["Veinte días.", "Quince días.", "Diez días.", "Tres meses."], "Art. 20 LEF.", "resolverá, en el plazo máximo de veinte días, sobre la necesidad de la ocupación"),
 ("LEF", "aveintiuno", "Necesidad de ocupación", "Según el artículo 21 de la Ley de Expropiación Forzosa, el acuerdo de necesidad de ocupación:",
  ["Inicia el expediente expropiatorio.", "Pone fin al expediente expropiatorio.", "Fija el justo precio.", "Autoriza la ocupación inmediata de los bienes."], "Art. 21.1 LEF.", "El acuerdo de necesidad de ocupación inicia el expediente expropiatorio"),
 ("LEF", "aveintidos", "Necesidad de ocupación", "Según el artículo 22 de la Ley de Expropiación Forzosa, el plazo para interponer el recurso de alzada contra el acuerdo de necesidad de ocupación será de:",
  ["Diez días.", "Un mes.", "Veinte días.", "Quince días."], "Art. 22.2 LEF.", "El plazo para la interposición del recurso será de diez días"),
 ("LEF", "aveintidos", "Necesidad de ocupación", "Según el artículo 22.3 de la Ley de Expropiación Forzosa, la interposición del recurso de alzada contra el acuerdo de necesidad de ocupación:",
  ["Surtirá efectos suspensivos hasta tanto se dicte la resolución expresa.", "No suspenderá en ningún caso la ejecución del acuerdo.", "Suspenderá el acuerdo solo si lo solicita el interesado.", "Suspenderá el acuerdo durante un máximo de diez días."], "Art. 22.3 LEF.", "surtirá efectos suspensivos hasta tanto se dicte la resolución expresa"),
 ("LEF", "aveinticuatro", "Justo precio", "Según el artículo 24 de la Ley de Expropiación Forzosa, si no se llega a un mutuo acuerdo sobre la adquisición en el plazo de quince días:",
  ["Se seguirá el procedimiento de los artículos siguientes, sin perjuicio de que las partes puedan llegar después a dicho mutuo acuerdo.", "Se archivará el expediente.", "El Jurado de expropiación fijará el precio sin hojas de aprecio.", "Se declarará la urgente ocupación."], "Art. 24 LEF.", "sin perjuicio de que en cualquier estado posterior de su tramitación puedan ambas parte llegar a dicho mutuo acuerdo"),
 ("LEF", "aveintinueve", "Justo precio", "Según el artículo 29 de la Ley de Expropiación Forzosa, la Administración requerirá a los propietarios para que presenten hoja de aprecio en el plazo de:",
  ["Veinte días.", "Diez días.", "Quince días.", "Un mes."], "Art. 29.1 LEF.", "en el plazo de veinte días, a contar desde el siguiente al de la notificación, presenten hoja de aprecio"),
 ("LEF", "atreinta", "Justo precio", "Según el artículo 30 de la Ley de Expropiación Forzosa, notificada la hoja de aprecio fundada de la Administración, el propietario podrá aceptarla o rechazarla dentro de:",
  ["Los diez días siguientes.", "Los veinte días siguientes.", "Los quince días siguientes.", "El mes siguiente."], "Art. 30.2 LEF.", "dentro de los diez días siguientes"),
 ("LEF", "atreintaydos", "Justo precio", "Según el artículo 32 de la Ley de Expropiación Forzosa, el Jurado provincial de expropiación estará presidido por:",
  ["El Magistrado que designe el Presidente de la audiencia correspondiente.", "El Delegado de Economía y Hacienda de la provincia.", "El Abogado del Estado de la Delegación de Hacienda.", "El Notario de libre designación por el Decano del Colegio Notarial."], "Art. 32.1 LEF.", "el Magistrado que designe el Presidente de la audiencia correspondiente"),
 ("LEF", "atreintaycinco", "Justo precio", "Según el artículo 35 de la Ley de Expropiación Forzosa, contra la resolución del Jurado de expropiación procederá:",
  ["Tan sólo el recurso contencioso-administrativo.", "Recurso de alzada ante el Ministerio de Hacienda.", "Recurso potestativo de reposición y después contencioso.", "Recurso extraordinario de revisión."], "Art. 35.2 LEF.", "procederá tan sólo el recurso contencioso-administrativo"),
 ("LEF", "atreintayseis", "Justo precio", "Según el artículo 36 de la Ley de Expropiación Forzosa, las tasaciones se efectuarán con arreglo al valor que tengan los bienes o derechos expropiables:",
  ["Al tiempo de iniciarse el expediente de justiprecio.", "Al tiempo de la declaración de utilidad pública.", "Al tiempo del pago.", "Al tiempo de la ocupación."], "Art. 36.1 LEF.", "al tiempo de iniciarse el expediente de justiprecio"),
 ("LEF", "acuarentasiete", "Justo precio", "Según el artículo 47 de la Ley de Expropiación Forzosa, en todos los casos de expropiación se abonará al expropiado, además del justo precio, un premio de afección del:",
  ["Cinco por ciento.", "Diez por ciento.", "Tres por ciento.", "Quince por ciento."], "Art. 47 LEF.", "un cinco por ciento como premio de afección"),
 ("LEF", "acuarentayocho", "Pago y ocupación", "Según el artículo 48 de la Ley de Expropiación Forzosa, una vez determinado el justo precio, se procederá al pago en el plazo máximo de:",
  ["Seis meses.", "Tres meses.", "Un año.", "Dos meses."], "Art. 48.1 LEF.", "en el plazo máximo de seis meses"),
 ("LEF", "acincuenta", "Pago y ocupación", "Según el artículo 50 de la Ley de Expropiación Forzosa, cuando el propietario rehusare recibir el precio, se consignará el justiprecio en:",
  ["La Caja General de Depósitos.", "El Banco de España.", "La cuenta del Juzgado de Primera Instancia.", "La Delegación de Economía y Hacienda."], "Art. 50.1 LEF.", "Caja General de Depósitos"),
 ("LEF", "acincuentaydos", "Pago y ocupación", "Según el artículo 52 de la Ley de Expropiación Forzosa, la urgente ocupación de los bienes podrá declararse excepcionalmente mediante:",
  ["Acuerdo del Consejo de Ministros.", "Orden del Ministro de Hacienda.", "Resolución del Jurado provincial de expropiación.", "Ley aprobada en Cortes en todo caso."], "Art. 52 LEF.", "Excepcionalmente y mediante acuerdo del Consejo de Ministros"),
 ("LEF", "acincuentaydos", "Pago y ocupación", "Según el artículo 52 de la Ley de Expropiación Forzosa, en la urgente ocupación, el día y hora del levantamiento del acta previa a la ocupación se notificará con una antelación mínima de:",
  ["Ocho días.", "Quince días.", "Tres días.", "Un mes."], "Art. 52.2 LEF.", "con una antelación mínima de ocho días"),
 ("LEF", "acincuentayseis", "Demora y reversión", "Según el artículo 56 de la Ley de Expropiación Forzosa, la Administración culpable de la demora abonará intereses cuando hayan transcurrido, sin determinarse el justo precio, desde la iniciación legal del expediente:",
  ["Seis meses.", "Tres meses.", "Un año.", "Cuatro años."], "Art. 56 LEF.", "Cuando hayan transcurrido seis meses desde la iniciación legal del expediente expropiatorio"),
 ("LEF", "acincuentayocho", "Demora y reversión", "Según el artículo 58 de la Ley de Expropiación Forzosa, procederá evaluar de nuevo las cosas o derechos expropiados si transcurren sin pago ni consignación del justo precio:",
  ["Cuatro años.", "Dos años.", "Seis meses.", "Diez años."], "Art. 58 LEF (retasación).", "Si transcurrieran cuatro años sin que el pago de la cantidad fijada como justo precio se haga efectivo o se consigne"),
 ("LEF", "acincuentaycuatro", "Demora y reversión", "Según el artículo 54 de la Ley de Expropiación Forzosa, no habrá derecho de reversión cuando la afectación al fin que justificó la expropiación se prolongue desde la terminación de la obra o el establecimiento del servicio durante:",
  ["Diez años.", "Cinco años.", "Veinte años.", "Cuatro años."], "Art. 54.2 b) LEF.", "se prolongue durante diez años desde la terminación de la obra o el establecimiento del servicio"),
 ("LEF", "acincuentaycuatro", "Demora y reversión", "Según el artículo 54.3 de la Ley de Expropiación Forzosa, notificada por la Administración la desafectación, el plazo para solicitar la reversión será de:",
  ["Tres meses.", "Un mes.", "Seis meses.", "Un año."], "Art. 54.3 LEF.", "el plazo para que el dueño primitivo o sus causahabientes puedan solicitarla será el de tres meses"),
 ("LEF", "acientonueve", "Otros procedimientos", "Según el artículo 109 de la Ley de Expropiación Forzosa, quedan exceptuadas de la ocupación temporal e imposición de servidumbres:",
  ["Las viviendas.", "Las fincas rústicas.", "Los locales de negocio.", "Los bienes de las Corporaciones locales."], "Art. 109 LEF (salvo permiso expreso del morador).", "Las viviendas quedan exceptuadas de la ocupación temporal e imposición de servidumbres"),
 ("LEF", "acincuentaynueve", "Otros procedimientos", "Según el artículo 59 de la Ley de Expropiación Forzosa, la aplicación del procedimiento especial para expropiar grandes zonas territoriales podrá acordarla:",
  ["El Consejo de Ministros, mediante Decreto.", "El Ministro de Hacienda, mediante Orden.", "Las Cortes Generales, mediante Ley.", "El Delegado del Gobierno."], "Art. 59 LEF.", "el Consejo de Ministros podrá acordar, mediante Decreto"),
 ("LEF", "acientoveinticinco", "Garantías", "Según el artículo 125 de la Ley de Expropiación Forzosa, si la Administración ocupare la cosa sin cumplir los requisitos sustanciales, el interesado podrá utilizar:",
  ["Los interdictos de retener y recobrar.", "Únicamente el recurso de alzada.", "La reclamación ante el Jurado de expropiación.", "El recurso de amparo directamente."], "Art. 125 LEF.", "los interdictos de retener y recobrar"),
 ("LEF", "acientoveintiseis", "Garantías", "Según el artículo 126 de la Ley de Expropiación Forzosa, el recurso contencioso-administrativo contra el justo precio deberá fundarse en lesión cuando la cantidad fijada sea inferior o superior a la alegada en más de:",
  ["Una sexta parte.", "Una quinta parte.", "Un diez por ciento.", "Una tercera parte."], "Art. 126.2 LEF.", "en más de una sexta parte"),
 ("LEF", "acientoveintiseis", "Garantías", "Según el artículo 126 de la Ley de Expropiación Forzosa, los recursos contencioso-administrativos en materia de expropiación:",
  ["Se considerarán de turno preferente.", "Se tramitarán por el procedimiento abreviado.", "Requieren previa reclamación ante el Jurado.", "Solo pueden interponerlos los expropiados."], "Art. 126.4 LEF.", "Se considerarán de turno preferente los recursos comprendidos en este artículo"),
]
for k, art, cat, enun, ops, expl, frag in Q: T.q(k, art, cat, enun, ops, expl, frag)
for cod, n, *_ in EX: T.real(cod, n, "Preguntas oficiales")

for q_, a_, cat in [
  ("Tres garantías del art. 33.3 CE", "Causa justificada de utilidad pública o interés social; indemnización; conformidad con las leyes.", "Concepto"),
  ("¿Quién puede acordar la expropiación? (LEF, art. 2.1)", "Solo el Estado, la Provincia o el Municipio.", "Sujetos"),
  ("Beneficiario por interés social (art. 2.3)", "Además de los del 2.2, cualquier persona natural o jurídica que reúna los requisitos de la ley especial.", "Sujetos"),
  ("¿Con quién se entiende el expediente en primer lugar? (art. 3.1)", "Con el propietario de la cosa o titular del derecho.", "Sujetos"),
  ("Efecto de las transmisiones durante el expediente (art. 7)", "No impiden su continuación; el nuevo titular se subroga.", "Sujetos"),
  ("Requisito previo a toda expropiación (art. 9)", "Declaración previa de utilidad pública o interés social.", "Causa"),
  ("Utilidad pública implícita (art. 10)", "Para inmuebles, en todos los planes de obras y servicios del Estado, Provincia y Municipio.", "Causa"),
  ("Plazos de la necesidad de ocupación", "Información pública 15 días (art. 18); resolución 20 días (art. 20).", "Necesidad de ocupación"),
  ("Recurso contra la necesidad de ocupación (art. 22)", "Alzada ante el Ministerio correspondiente; 10 días para interponer, 20 para resolver; efectos suspensivos.", "Necesidad de ocupación"),
  ("Plazos de las hojas de aprecio (arts. 29 y 30)", "Propietario 20 días; Administración 20 días; respuesta del propietario 10 días.", "Justo precio"),
  ("Presidente del Jurado provincial de expropiación (art. 32)", "El Magistrado que designe el Presidente de la Audiencia.", "Justo precio"),
  ("Recurso contra la resolución del Jurado (art. 35.2)", "Tan sólo el contencioso-administrativo: ultima la vía gubernativa.", "Justo precio"),
  ("Premio de afección (art. 47)", "Cinco por ciento, en todos los casos de expropiación.", "Justo precio"),
  ("Plazo de pago del justo precio (art. 48)", "Máximo seis meses.", "Pago y ocupación"),
  ("Ocupación urgente (art. 52)", "Excepcional; por acuerdo del Consejo de Ministros; acta previa con 8 días de antelación.", "Pago y ocupación"),
  ("Retasación (art. 58)", "Si pasan cuatro años sin pagar ni consignar el justo precio.", "Demora y reversión"),
  ("Reversión: plazos clave (art. 54)", "10 años de afectación la excluyen; 3 meses para pedirla tras la notificación.", "Demora y reversión"),
  ("Defensa frente a la vía de hecho (art. 125)", "Interdictos de retener y recobrar.", "Garantías"),
  ("Lesión en el recurso contra el justo precio (art. 126.2)", "Diferencia de más de una sexta parte.", "Garantías"),
]: T.fc(q_, a_, cat)

T.glos("Expropiación forzosa", "Cualquier forma de privación singular de la propiedad privada o de derechos o intereses patrimoniales legítimos, acordada imperativamente (LEF, art. 1).", "s1", "Concepto")
T.glos("Beneficiario", "Sujeto que adquiere el bien o derecho expropiado sin ser el expropiante: entidades y concesionarios por utilidad pública; cualquier persona por interés social (art. 2).", "s2", "Sujetos")
T.glos("Declaración de utilidad pública o interés social", "Requisito previo e indispensable de la expropiación (art. 9).", "s4", "Causa")
T.glos("Necesidad de ocupación", "Acuerdo que determina los bienes estrictamente indispensables para el fin de la expropiación; inicia el expediente (arts. 15 y 21).", "s5", "Procedimiento")
T.glos("Hoja de aprecio", "Valoración motivada que presentan el propietario y, si la rechaza, la Administración (arts. 29 y 30).", "s6", "Justo precio")
T.glos("Jurado provincial de expropiación", "Órgano presidido por un Magistrado que decide ejecutoriamente el justo precio si no hay acuerdo (arts. 32 a 35).", "s6", "Justo precio")
T.glos("Premio de afección", "Cinco por ciento que se abona además del justo precio en todos los casos (art. 47).", "s6", "Justo precio")
T.glos("Ocupación urgente", "Procedimiento excepcional acordado por el Consejo de Ministros que permite ocupar antes de fijar y pagar el justo precio (art. 52).", "s7", "Procedimiento")
T.glos("Retasación", "Nueva valoración cuando pasan cuatro años sin pagar ni consignar el justo precio (art. 58).", "s8", "Demora")
T.glos("Reversión", "Derecho del primitivo dueño a recobrar lo expropiado si no se ejecuta la obra, hay sobrante o desaparece la afectación (art. 54).", "s8", "Reversión")
T.glos("Interdictos de retener y recobrar", "Defensa posesoria ante los jueces frente a la ocupación sin los requisitos sustanciales (art. 125).", "s10", "Garantías")

T.hito("1954", "Ley de 16 de diciembre de 1954 sobre expropiación forzosa", "Norma vigente del procedimiento expropiatorio (texto consolidado en el BOE)", "normativo", "s1")
T.hito("1978", "Constitución Española (27-12-1978; BOE de 29-12-1978)", "Art. 33.3: causa, indemnización y conformidad con las leyes", "normativo", "s1")
T.hito("1997", "Ley 6/1997 (LOFAGE), disposición adicional cuarta", "Atribuye al Delegado del Gobierno las demás competencias de los Gobernadores civiles; ley hoy derogada por la Ley 40/2015", "normativo", "s5")

T.publicar()
