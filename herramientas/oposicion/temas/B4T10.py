# -*- coding: utf-8 -*-
"""Tema IV.10 (B4T10): La responsabilidad patrimonial de las Administraciones públicas.
Procedimiento de responsabilidad patrimonial.
Método del I.2. Normas (textos consolidados del BOE): CE, arts. 106.2 y 121; Ley 40/2015
(LRJSP), arts. 32 a 37; Ley 39/2015 (LPAC), especialidades del procedimiento; LO 3/1980,
del Consejo de Estado, art. 22; LJCA, art. 2 e)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

T = Tema("B4T10",
  "Tres preguntas: I. Cuándo responde la Administración (arts. 106.2 y 121 CE; LRJSP, arts. 32 y 34.1) · II. Cuánto se indemniza y quién responde (LRJSP, arts. 33 a 37) · III. Cómo se reclama: el procedimiento (LPAC, LO 3/1980 y LJCA). Cada artículo: texto literal del BOE y ficha.",
  ["Art. 106.2 CE", "LRJSP", "LPAC", "Lesión", "Fuerza mayor", "Relación de causalidad", "Estado legislador", "Responsabilidad concurrente", "Acción de regreso", "Prescripción: un año", "Consejo de Estado", "Silencio desestimatorio", "Procedimiento simplificado"])

T.ap("s0", "Mapa del tema: tres preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque IV, tema 10):
> La responsabilidad patrimonial de las Administraciones públicas. Procedimiento de responsabilidad patrimonial.

### El hilo conductor

| Bloque | Pregunta | Normas |
|---|---|---|
| **I** | ¿Cuándo responde la Administración? (fundamento y requisitos) | CE, arts. 106.2 y 121; LRJSP, arts. 32 y 34.1 |
| **II** | ¿Cuánto se indemniza y quién responde? | LRJSP, arts. 33, 34.2 a 34.4, 35, 36 y 37 |
| **III** | ¿Cómo se reclama? (el procedimiento) | LPAC, arts. 24, 35, 61, 65, 67, 81, 82, 86, 91, 92, 96 y 114; LO 3/1980, art. 22; LJCA, art. 2 |

!> **La idea que une los tres bloques:** la responsabilidad patrimonial es **objetiva**: no hace falta culpa. Basta una **lesión** (daño efectivo, evaluable e individualizado que el particular **no tiene el deber jurídico de soportar**) causada por el **funcionamiento normal o anormal** de los servicios públicos, **salvo fuerza mayor**. La regla sustantiva está en la **Ley 40/2015** (arts. 32 a 37); el **procedimiento** no es especial: es el **común** de la **Ley 39/2015** con unas especialidades repartidas por sus artículos.

?> **Dónde está cada cosa.** La Ley 39/2015 no tiene un capítulo propio para la responsabilidad patrimonial: sus especialidades aparecen **dentro** de cada fase (iniciación, instrucción, terminación, tramitación simplificada). Por eso el bloque III sigue el orden de sus artículos.
""")

# =============================================================================
T.ap("bI", "I. ¿Cuándo responde la Administración? (arts. 106.2 y 121 CE; LRJSP, arts. 32 y 34.1)", donde(
  "Primera pregunta del tema: **en qué casos** nace el derecho a ser indemnizado. La Constitución lo garantiza y la Ley 40/2015 fija sus requisitos.",
  ["1 Fundamento constitucional (arts. 106.2 y 121 CE; LRJSP, art. 32.7)", "2 Principios y requisitos de la responsabilidad (LRJSP, art. 32)", "3 El daño indemnizable (LRJSP, art. 34.1)"]))

T.ap("s1", "I.1 Fundamento constitucional (arts. 106.2 y 121 CE; LRJSP, art. 32.7)", f"""
{unidad("1.1 El derecho a ser indemnizado (art. 106.2)",
  lit("CE", "Artículo 106", ["toda lesión que sufran en cualquiera de sus bienes y derechos", "salvo en los casos de fuerza mayor", "consecuencia del funcionamiento de los servicios públicos"], solo=[2]),
  ficha(c("CE", "Artículo 106", "Los particulares"),
        ["::Derecho a ser indemnizados por toda lesión en sus bienes y derechos:", "Que sea **consecuencia del funcionamiento de los servicios públicos**", f"{c('CE', 'Artículo 106', 'en los **términos establecidos por la ley**')} (hoy, Leyes 40/2015 y 39/2015)"],
        "**Fuerza mayor**: excluye la indemnización",
        "Control de los Tribunales sobre la actuación administrativa (106.1); reclamación ante la Administración y, después, contencioso (→ III.6)",
        "El art. 106.2 está en el **Título IV** (Gobierno y Administración), **no** en el Título I: no es un derecho fundamental susceptible de amparo. Única exclusión constitucional: la **fuerza mayor**."))}

{unidad("1.2 La responsabilidad por la Administración de Justicia (art. 121 CE; LRJSP, art. 32.7)",
  lit("CE", "Artículo 121", ["error judicial", "funcionamiento anormal de la Administración de Justicia", "a cargo del Estado"]),
  lit("L40", "Artículo 32", ["se regirá por la Ley Orgánica 6/1985, de 1 de julio, del Poder Judicial"], solo=[14]),
  fichab("Indemnización por error judicial o funcionamiento anormal de la Administración de Justicia",
         "El **Estado** paga la indemnización",
         "Se rige por la **LOPJ**, no por la Ley 40/2015 (art. 32.7 LRJSP)",
         "—",
         "Dos supuestos: **error judicial** y funcionamiento **anormal** de la Justicia (no el normal). Es otro régimen: la LRJSP **remite** a la LOPJ."))}
""", 2)

T.ap("s2", "I.2 Principios y requisitos de la responsabilidad (LRJSP, art. 32)", f"""
{unidad("2.1 La regla general (art. 32.1 y 2)",
  lit("L40", "Artículo 32", ["toda lesión que sufran en cualquiera de sus bienes y derechos", "funcionamiento normal o anormal de los servicios públicos", "salvo en los casos de fuerza mayor o de daños que el particular tenga el deber jurídico de soportar de acuerdo con la Ley", "no presupone, por sí misma, derecho a la indemnización", "efectivo, evaluable económicamente e individualizado"], solo=[1, 2, 3]),
  ficha("Los **particulares** (frente a las Administraciones Públicas correspondientes)",
        ["::Indemnización por toda lesión en sus bienes y derechos si:", "Es consecuencia del funcionamiento **normal o anormal** de los servicios públicos (responsabilidad **objetiva**)", "El daño es **efectivo**, **evaluable económicamente** e **individualizado** con relación a una persona o grupo de personas (32.2)"],
        ["::No se indemniza:", "**Fuerza mayor**", "Daños que el particular tenga el **deber jurídico de soportar** de acuerdo con la Ley", "La **anulación** de un acto o disposición **no presupone, por sí misma**, el derecho a indemnización (32.1, párrafo 2.º)"],
        "Reclamación en el procedimiento de la Ley 39/2015 (→ III) y, después, el contencioso-administrativo",
        f"{c('L40', 'Artículo 32', 'funcionamiento **normal o anormal**')}: también responde por el funcionamiento **normal**. La anulación **no** da derecho automático a indemnización (pregunta oficial X 61, → Cierre 1). Tres notas del daño: **efectivo, evaluable, individualizado**."))}

{unidad("2.2 La responsabilidad del Estado legislador (art. 32.3 a 6)",
  lit("L40", "Artículo 32", ["actos legislativos de naturaleza no expropiatoria", "cuando así se establezca en los propios actos legislativos", "norma con rango de ley declarada inconstitucional", "norma contraria al Derecho de la Unión Europea", "sentencia firme desestimatoria", "suficientemente caracterizado", "relación de causalidad directa", "desde la fecha de su publicación"], solo=list(range(4, 14))),
  fichab("Indemnización por daños derivados de **leyes**",
         "Particulares que no tengan el deber jurídico de soportar el daño",
         ["**Actos legislativos no expropiatorios**: cuando lo establezca el propio acto legislativo y en sus términos (32.3)", "**Ley inconstitucional**: si el particular obtuvo **sentencia firme desestimatoria** de un recurso contra la actuación que causó el daño y **alegó la inconstitucionalidad** (32.4)", "**Norma contraria al Derecho de la UE**: los mismos requisitos y, además, que la norma confiera derechos a los particulares, un incumplimiento **suficientemente caracterizado** y una relación de causalidad **directa** (32.5)"],
         "La sentencia surte efectos desde su publicación en el **BOE** o en el **DOUE**, salvo que disponga otra cosa (32.6). Daños indemnizables: los de los **cinco años** anteriores a esa publicación (→ I.3)",
         "Para la UE se exigen **tres** requisitos más (a, b y c). En ambos casos hace falta **sentencia firme desestimatoria** y haber **alegado** el vicio después declarado."))}

{unidad("2.3 Remisiones del art. 32: Justicia, Tribunal Constitucional y contratos (art. 32.7 a 9)",
  lit("L40", "Artículo 32", ["El Consejo de Ministros fijará el importe de las indemnizaciones", "funcionamiento anormal en la tramitación de los recursos de amparo o de las cuestiones de inconstitucionalidad", "se tramitará por el Ministerio de Justicia, con audiencia al Consejo de Estado", "durante la ejecución de contratos", "consecuencia de una orden inmediata y directa de la Administración o de los vicios del proyecto elaborado por ella misma"], solo=[15, 16, 17]),
  fichab("Supuestos con regla propia",
         ["**Consejo de Ministros**: fija la indemnización por funcionamiento anormal del TC en amparos y cuestiones de inconstitucionalidad (32.8)", "**Ministerio de Justicia**: tramita, con audiencia al **Consejo de Estado** (32.8)"],
         ["Administración de Justicia: **LOPJ** (32.7, → I.1.2)", "Daños a terceros en la ejecución de **contratos**: responde la Administración si derivan de una **orden inmediata y directa** suya o de **vicios del proyecto** elaborado por ella; procedimiento de la Ley 39/2015 (32.9)"],
         "—",
         "En los contratos, la Administración responde **solo** por orden inmediata y directa o por vicios de **su** proyecto. Nota: el art. 32.9 cita todavía el **Real Decreto Legislativo 3/2011** (texto refundido de contratos), hoy sustituido por la Ley 9/2017; se transcribe tal como está en el BOE."))}
""", 2)

T.ap("s3", "I.3 El daño indemnizable (LRJSP, art. 34.1)", f"""
{unidad("3.1 Deber jurídico de soportar y riesgos del progreso (art. 34.1)",
  lit("L40", "Artículo 34", ["que éste no tenga el deber jurídico de soportar de acuerdo con la Ley", "según el estado de los conocimientos de la ciencia o de la técnica existentes en el momento de producción", "en el plazo de los cinco años anteriores a la fecha de la publicación de la sentencia"], solo=[1, 2]),
  ficha("El particular lesionado",
        "Solo son indemnizables las lesiones por daños que el particular **no tenga el deber jurídico de soportar**",
        ["::No son indemnizables:", "Los daños por hechos o circunstancias que **no se hubiesen podido prever o evitar** según el estado de la ciencia o de la técnica en ese momento (riesgos del progreso), sin perjuicio de prestaciones asistenciales o económicas", "Estado legislador (32.4 y 5): solo los daños de los **cinco años** anteriores a la publicación de la sentencia, salvo que esta disponga otra cosa"],
        "—",
        "El **estado de la ciencia o de la técnica** se mide **en el momento de producirse** el daño, no en el de la reclamación. Estado legislador: **cinco años** hacia atrás."))}

{resumen([
  "Art. 106.2 CE: indemnización por toda lesión consecuencia del funcionamiento de los servicios públicos, **salvo fuerza mayor**; Justicia: art. 121 CE y **LOPJ**.",
  "LRJSP, art. 32: funcionamiento **normal o anormal**; daño **efectivo, evaluable económicamente e individualizado**; la anulación **no presupone por sí misma** indemnización.",
  "Estado legislador: actos legislativos (si lo prevén), ley **inconstitucional** y norma **contraria al Derecho de la UE**, con sentencia firme desestimatoria previa.",
  "Art. 34.1: no se indemniza lo que hay **deber jurídico de soportar** ni los **riesgos del progreso**."],
  "Siguiente: II. ¿Cuánto se indemniza y quién responde?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Cuánto se indemniza y quién responde? (LRJSP, arts. 33 a 37)", donde(
  "Segunda pregunta. Una vez que hay lesión indemnizable, hay que saber **qué Administración** responde cuando son varias, **cómo se calcula** la indemnización y qué pasa con el **personal** que causó el daño.",
  ["1 Responsabilidad concurrente de varias Administraciones (art. 33)", "2 Cálculo y forma de la indemnización (art. 34.2 a 4)", "3 Derecho privado, personal y responsabilidad penal (arts. 35 a 37)"]))

T.ap("s4", "II.1 Responsabilidad concurrente de varias Administraciones (art. 33)", f"""
{unidad("1.1 Fórmulas conjuntas y otros supuestos de concurrencia (art. 33)",
  lit("L40", "Artículo 33", ["responderán frente al particular, en todo caso, de forma solidaria", "criterios de competencia, interés público tutelado e intensidad de la intervención", "La responsabilidad será solidaria cuando no sea posible dicha determinación", "con mayor participación en la financiación del servicio", "en el plazo de quince días"]),
  fichab("Daño causado por varias Administraciones",
         ["::Competente para tramitar en las fórmulas conjuntas:", "La fijada en los **Estatutos** o reglas de la organización colegiada", "En su defecto, la de **mayor participación en la financiación** del servicio"],
         ["**Fórmulas conjuntas de actuación**: responden frente al particular **en todo caso de forma solidaria**; el instrumento regulador puede repartir la responsabilidad entre ellas (33.1)", "**Otros supuestos de concurrencia**: responsabilidad de cada una según **competencia, interés público tutelado e intensidad de la intervención**; **solidaria** si no es posible determinarla (33.2)"],
         "Consulta a las demás Administraciones implicadas: **15 días** (33.4)",
         "Fórmulas conjuntas → **solidaria siempre**. Otros casos → reparto por **tres** criterios y solidaria solo si no se puede repartir."))}
""", 2)

T.ap("s5", "II.2 Cálculo y forma de la indemnización (art. 34.2 a 4)", f"""
{unidad("2.1 Criterios, fecha de cálculo y forma de pago (art. 34.2, 3 y 4)",
  lit("L40", "Artículo 34", ["legislación fiscal, de expropiación forzosa y demás normas aplicables", "valoraciones predominantes en el mercado", "baremos de la normativa vigente en materia de Seguros obligatorios y de la Seguridad Social", "con referencia al día en que la lesión efectivamente se produjo", "Índice de Garantía de la Competitividad", "compensación en especie o ser abonada mediante pagos periódicos", "siempre que exista acuerdo con el interesado"], solo=[3, 4, 5]),
  fichab("Cuánto y cómo se indemniza",
         "La Administración responsable; el **INE** fija el índice de actualización",
         ["**Criterios** de valoración: legislación **fiscal**, de **expropiación forzosa** y demás normas, ponderando las valoraciones del **mercado** (34.2)", "Muerte o lesiones corporales: puede tomarse como referencia el **baremo** de seguros obligatorios y de Seguridad Social (34.2)", "**Fecha**: el día en que la lesión **efectivamente se produjo**, actualizada al fin del procedimiento con el **Índice de Garantía de la Competitividad** (34.3)", "**Forma**: dinero; o, con **acuerdo** del interesado, compensación **en especie** o **pagos periódicos** (34.4)"],
         "Intereses de demora en el pago: Ley 47/2003, General Presupuestaria, o normas presupuestarias autonómicas (34.3)",
         "Actualización con el **Índice de Garantía de la Competitividad** (no el IPC). Especie o pagos periódicos: **solo con acuerdo** del interesado."))}
""", 2)

T.ap("s6", "II.3 Derecho privado, personal y responsabilidad penal (arts. 35 a 37)", f"""
{unidad("3.1 Responsabilidad en relaciones de Derecho privado (art. 35)",
  lit("L40", "Artículo 35", ["de conformidad con lo previsto en los artículos 32 y siguientes", "incluso cuando concurra con sujetos de derecho privado"]),
  fichab("Unidad de régimen", "Administraciones que actúen directamente o a través de una entidad de derecho privado",
         "Se aplican **también** los arts. 32 y siguientes, aunque concurran sujetos privados o se reclame a la entidad privada o a la aseguradora",
         "—", "Aunque la relación sea **privada**, el régimen es el **de la LRJSP** (y la jurisdicción, la contencioso-administrativa: → III.6)."))}

{unidad("3.2 Acción directa contra la Administración y acción de regreso (art. 36)",
  lit("L40", "Artículo 36", ["exigirán directamente a la Administración Pública correspondiente", "exigirá de oficio en vía administrativa", "por dolo, o culpa o negligencia graves", "Alegaciones durante un plazo de quince días", "Audiencia durante un plazo de diez días", "pondrá fin a la vía administrativa"]),
  fichab("Exigencia de responsabilidad al personal (acción de **regreso**)",
         ["El particular reclama **directamente a la Administración**, no a la autoridad o al empleado (36.1)", "La Administración, tras indemnizar, lo exige **de oficio** a su personal (36.2)"],
         ["Solo si hubo **dolo, o culpa o negligencia graves** (36.2 y 3)", "Criterios: resultado dañoso, grado de culpabilidad, responsabilidad profesional y relación con el resultado (36.2)", "También por daños a los **bienes o derechos de la propia Administración** (36.3)"],
         "Alegaciones **15 días** · prueba **15 días** · audiencia **10 días** · propuesta **5 días** · resolución **5 días** (36.4)",
         "La acción de regreso es **obligatoria** («exigirá **de oficio**») y solo por **dolo o culpa/negligencia graves**. La resolución **pone fin a la vía administrativa** (36.5)."))}

{unidad("3.3 Responsabilidad penal (art. 37)",
  lit("L40", "Artículo 37", ["no suspenderá los procedimientos de reconocimiento de responsabilidad patrimonial", "salvo que la determinación de los hechos en el orden jurisdiccional penal sea necesaria"]),
  fichab("Relación entre el proceso penal y la responsabilidad patrimonial", "Personal al servicio de las Administraciones",
         "La responsabilidad penal y la civil derivada del delito, según su legislación (37.1)",
         "—", "Regla: el proceso penal **no suspende** el procedimiento de responsabilidad patrimonial; excepción: que los hechos deban fijarse en el orden **penal**."))}

{resumen([
  "Fórmulas conjuntas: **solidaria en todo caso**; otros supuestos: reparto por competencia, interés tutelado e intensidad (solidaria si no se puede).",
  "Indemnización: criterios fiscales, expropiatorios y de mercado; referida al **día de la lesión** y actualizada con el **Índice de Garantía de la Competitividad**; en especie o periódica **con acuerdo**.",
  "El particular reclama **a la Administración**; esta repite **de oficio** contra su personal por **dolo o culpa o negligencia graves**.",
  "El proceso penal **no suspende**, salvo que la fijación de los hechos lo requiera."],
  "Siguiente: III. ¿Cómo se reclama? El procedimiento")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Cómo se reclama? El procedimiento (LPAC; LO 3/1980; LJCA)", donde(
  "Tercera pregunta. El procedimiento es el **común** de la Ley 39/2015 con especialidades en cada fase. Se ven por el orden de sus artículos: reglas generales, iniciación, instrucción, terminación, tramitación simplificada y, al final, el fin de la vía administrativa y el control judicial.",
  ["1 Reglas generales: silencio y motivación (arts. 24 y 35)", "2 Iniciación (arts. 61, 65 y 67)", "3 Instrucción: informes, dictamen y audiencia (arts. 81 y 82)", "4 Terminación (arts. 86, 91 y 92)", "5 Tramitación simplificada (art. 96)", "6 Fin de la vía administrativa y control judicial (art. 114; LO 3/1980, art. 22; LJCA, art. 2)"]))

T.ap("s7", "III.1 Reglas generales: silencio y motivación (LPAC, arts. 24 y 35)", f"""
{unidad("1.1 Silencio desestimatorio (art. 24.1)",
  lit("L39", "Artículo 24", ["en los procedimientos de responsabilidad patrimonial de las Administraciones Públicas"], solo=[2]),
  fichab("Efecto de la falta de resolución en plazo", "El reclamante", "El silencio es **desestimatorio** (excepción a la regla del silencio positivo)", "Plazo de resolución: **seis meses** (→ III.4.2)",
         "En responsabilidad patrimonial el silencio es **negativo**, igual que en el derecho de petición y en las facultades sobre dominio o servicio público."))}

{unidad("1.2 Motivación (art. 35.1 h)",
  lit("L39", "Artículo 35", ["o de responsabilidad patrimonial"], solo=list(range(1, 11))),
  fichab("Actos que deben motivarse", "El órgano que resuelve", "Se motivan, con sucinta referencia de hechos y fundamentos de derecho, los actos que resuelvan procedimientos de responsabilidad patrimonial", "—",
         "Motivación **obligatoria** de la resolución de responsabilidad patrimonial (letra **h**)."))}
""", 2)

T.ap("s8", "III.2 Iniciación (LPAC, arts. 61, 65 y 67)", f"""
{unidad("2.1 Iniciación de oficio por petición razonada (art. 61.4)",
  lit("L39", "Artículo 61", ["individualizar la lesión producida en una persona o grupo de personas"], solo=[4]),
  fichab("Contenido de la petición razonada de otro órgano", "Un órgano sin competencia para iniciar que conoce los hechos",
         ["Individualizar la **lesión** en una persona o grupo", "Su **relación de causalidad** con el funcionamiento del servicio", "Su **evaluación económica**, si fuera posible", "El **momento** en que se produjo"],
         "—", "Mismo contenido que la solicitud del interesado (→ III.2.3)."))}

{unidad("2.2 Especialidades del inicio de oficio (art. 65)",
  lit("L39", "Artículo 65", ["será necesario que no haya prescrito el derecho a la reclamación del interesado", "un plazo de diez días", "aunque los particulares presuntamente lesionados no se personen"]),
  fichab("La Administración inicia de oficio", "Órgano competente; se notifica a los presuntos lesionados",
         ["Requisito: que **no haya prescrito** el derecho a reclamar del interesado (art. 67)", "Se instruye **aunque los lesionados no se personen**"],
         "Alegaciones, documentos y prueba de los lesionados: **10 días**",
         "Ni siquiera de oficio puede iniciarse si el derecho a reclamar **ha prescrito**."))}

{unidad("2.3 Solicitud del interesado y prescripción (art. 67)",
  lit("L39", "Artículo 67", ["prescribirá al año de producido el hecho o el acto que motive la indemnización o se manifieste su efecto lesivo", "desde la curación o la determinación del alcance de las secuelas", "al año de haberse notificado la resolución administrativa o la sentencia definitiva", "al año de la publicación", "la evaluación económica de la responsabilidad patrimonial, si fuera posible"]),
  fichab("Reclamación del particular",
         "El interesado, mientras **no haya prescrito** su derecho",
         ["Contenido (además del art. 66): **lesiones**, presunta **relación de causalidad**, **evaluación económica** si es posible y **momento** de la lesión; con alegaciones, documentos y **proposición de prueba** (67.2)"],
         ["::Prescripción: **un año**, contado desde:", "El hecho o acto que motive la indemnización o la manifestación de su efecto lesivo (regla general)", "Daños **físicos o psíquicos**: la **curación** o la determinación del alcance de las **secuelas**", "Anulación de un acto o disposición: la **notificación** de la resolución o de la **sentencia definitiva**", "Estado legislador (32.4 y 5 LRJSP): la **publicación** de la sentencia en el BOE o el DOUE"],
         "Plazo de **un año**, no seis meses ni dos años (pregunta oficial P 71, → Cierre 1). Daños personales: el plazo empieza con la **curación** o la fijación de las **secuelas**."))}
""", 2)

T.ap("s9", "III.3 Instrucción: informes, dictamen y audiencia (LPAC, arts. 81 y 82)", f"""
{unidad("3.1 Informe del servicio y dictamen del Consejo de Estado (art. 81)",
  lit("L39", "Artículo 81", ["será preceptivo solicitar informe al servicio cuyo funcionamiento haya ocasionado la presunta lesión indemnizable", "no pudiendo exceder de diez días", "de cuantía igual o superior a 50.000 euros", "en el plazo de diez días a contar desde la finalización del trámite de audiencia", "El dictamen se emitirá en el plazo de dos meses", "será preceptivo el informe del Consejo General del Poder Judicial"]),
  fichab("Informes y dictámenes preceptivos",
         ["**Servicio** causante de la lesión: informe preceptivo", "**Consejo de Estado** u órgano consultivo autonómico: dictamen", "**CGPJ**: informe en la responsabilidad por funcionamiento anormal de la Justicia"],
         ["Dictamen preceptivo si la cuantía reclamada es **igual o superior a 50.000 euros** (o la fijada por la legislación autonómica) o lo dispone la LO 3/1980", "El instructor remite **propuesta de resolución** (o de acuerdo convencional) **10 días** después de la audiencia", "El dictamen se pronuncia sobre la **relación de causalidad** y, en su caso, la **valoración**, cuantía y modo de la indemnización"],
         "Informe del servicio: máximo **10 días** · remisión de la propuesta: **10 días** · dictamen: **2 meses** · informe del CGPJ: máximo **2 meses** (suspende el plazo para resolver)",
         "Umbral: **50.000 euros**, «igual **o superior**». El informe del **servicio** es siempre preceptivo; el dictamen, por cuantía."))}

{unidad("3.2 Audiencia al contratista (art. 82.5)",
  lit("L39", "Artículo 82", ["será necesario en todo caso dar audiencia al contratista"], solo=[6]),
  fichab("Daños causados en la ejecución de contratos (32.9 LRJSP)", "El **contratista**", "Audiencia **en todo caso**, con notificación de todas las actuaciones para que se persone, alegue y proponga prueba", "—",
         "Si el daño se produjo en la ejecución de un contrato, el contratista es parte **necesaria** (→ I.2.3)."))}
""", 2)

T.ap("s10", "III.4 Terminación (LPAC, arts. 86, 91 y 92)", f"""
{unidad("4.1 Terminación convencional (art. 86.5)",
  lit("L39", "Artículo 86", ["el acuerdo alcanzado entre las partes deberá fijar la cuantía y modo de indemnización"], solo=[5]),
  fichab("Acuerdo indemnizatorio", "La Administración y el reclamante", "El acuerdo fija **cuantía y modo** de la indemnización según el **art. 34 LRJSP**", "—",
         "Cabe terminar por **acuerdo**; los criterios de cálculo siguen siendo los del art. 34 LRJSP (→ II.2)."))}

{unidad("4.2 Contenido de la resolución y silencio (art. 91)",
  lit("L39", "Artículo 91", ["una vez finalizado el trámite de audiencia", "sobre la existencia o no de la relación de causalidad", "Transcurridos seis meses desde que se inició el procedimiento", "podrá entenderse que la resolución es contraria a la indemnización del particular"]),
  fichab("La resolución del procedimiento",
         "El órgano competente (→ III.4.3); si hay propuesta de acuerdo, la formalizan el interesado y el órgano competente",
         ["Se resuelve tras el **dictamen** (si es preceptivo) o tras la **audiencia** (si no lo es)", "Contenido: además del art. 88, la **relación de causalidad** y, en su caso, la **valoración** del daño, la **cuantía** y el **modo** de la indemnización (art. 34 LRJSP)"],
         "**Seis meses** desde el inicio sin resolución expresa notificada ni acuerdo: puede entenderse **contraria** a la indemnización",
         "**Seis meses** desde que **se inició** el procedimiento (pregunta oficial L 56, → Cierre 1). Silencio **desestimatorio**."))}

{unidad("4.3 Órgano competente para resolver (art. 92)",
  lit("L39", "Artículo 92", ["por el Ministro respectivo o por el Consejo de Ministros en los casos del artículo 32.3", "por los órganos correspondientes de las Comunidades Autónomas o de las Entidades que integran la Administración Local"]),
  fichab("Quién resuelve",
         ["AGE: el **Ministro respectivo**", "AGE: el **Consejo de Ministros** en los casos del **art. 32.3 LRJSP** (actos legislativos) o cuando una ley lo disponga", "CCAA y entidades locales: sus órganos correspondientes", "Entidades de Derecho Público: las que digan sus normas; en su defecto, este artículo"],
         "—", "—",
         "Regla en la AGE: el **Ministro**. Consejo de Ministros: **responsabilidad por actos legislativos** (32.3) o si lo dice una ley."))}
""", 2)

T.ap("s11", "III.5 Tramitación simplificada (LPAC, art. 96)", f"""
{unidad("5.1 El procedimiento simplificado de responsabilidad patrimonial (art. 96.4 y 6)",
  lit("L39", "Artículo 96", ["considera inequívoca la relación de causalidad", "podrá acordar de oficio la suspensión del procedimiento general y la iniciación de un procedimiento simplificado"], solo=[5]),
  lit("L39", "Artículo 96", ["deberán ser resueltos en treinta días", "durante el plazo de cinco días", "suspensión automática del plazo para resolver", "en el plazo de quince días", "Cuando el Dictamen sea contrario al fondo de la propuesta de resolución"], solo=list(range(7, 18))),
  fichab("Vía rápida cuando todo está claro",
         "El órgano competente para la tramitación, **de oficio**",
         ["Requisito: relación de causalidad, valoración del daño y cálculo de la cuantía **inequívocos**", "Se **suspende** el procedimiento general y se inicia el simplificado", "Trámites tasados (96.6): inicio, subsanación, alegaciones, audiencia solo si la resolución es desfavorable, informes y dictamen preceptivos, resolución"],
         "Resolución en **30 días** · alegaciones **5 días** · dictamen en **15 días** si se pide · el plazo se **suspende** mientras se emite el dictamen",
         "En responsabilidad patrimonial lo acuerda el órgano **de oficio** (96.4). Si el dictamen es **contrario** al fondo de la propuesta, se pasa a la tramitación **ordinaria**."))}
""", 2)

T.ap("s12", "III.6 Fin de la vía administrativa y control judicial (LPAC, art. 114; LO 3/1980, art. 22; LJCA, art. 2)", f"""
{unidad("6.1 La resolución pone fin a la vía administrativa (art. 114.1 e)",
  lit("L39", "Artículo 114", ["cualquiera que fuese el tipo de relación, pública o privada, de que derive"], solo=list(range(1, 9))),
  fichab("Recursos contra la resolución", "El reclamante", "La resolución **pone fin a la vía administrativa**: cabe reposición potestativa (→ tema IV.12) o, directamente, el contencioso", "—",
         "**Toda** resolución de responsabilidad patrimonial agota la vía, sea **pública o privada** la relación de la que derive."))}

{unidad("6.2 Dictamen del Consejo de Estado (LO 3/1980, art. 22.13)",
  lit("LO3_1980", "aveintidos", ["Comisión Permanente", "en concepto de indemnización por daños y perjuicios"], solo=[1, 14]),
  fichab("Competencia de la Comisión Permanente del Consejo de Estado", "La **Comisión Permanente** del Consejo de Estado",
         "Dictamen en las reclamaciones de indemnización a la **AGE** en los supuestos que fijen las leyes (hoy, la cuantía del art. 81.2 LPAC)", "—",
         "Es la remisión del art. 81.2 LPAC: el dictamen es preceptivo desde **50.000 euros**."))}

{unidad("6.3 Jurisdicción competente (LJCA, art. 2 e)",
  lit("LJCA", "Artículo 2", ["cualquiera que sea la naturaleza de la actividad o el tipo de relación de que derive", "no pudiendo ser demandadas aquellas por este motivo ante los órdenes jurisdiccionales civil o social", "cuenten con un seguro de responsabilidad"], solo=list(range(1, 8))),
  fichab("Unidad jurisdiccional", "Orden **contencioso-administrativo**",
         "Conoce de la responsabilidad patrimonial de las AAPP **cualquiera que sea** la actividad o la relación; las AAPP **no** pueden ser demandadas por ello en los órdenes civil o social",
         "—", "Aunque concurran **particulares** en el daño o haya un **seguro** de responsabilidad: siempre el **contencioso** (→ II.3.1)."))}

{resumen([
  "Silencio **desestimatorio** (art. 24.1) y resolución **motivada** (art. 35.1 h).",
  "Reclamación: **un año** desde el hecho o la manifestación del efecto lesivo; daños personales, desde la **curación** o la fijación de las **secuelas** (art. 67).",
  "Informe del **servicio** (10 días) y dictamen del **Consejo de Estado** desde **50.000 euros** (2 meses) (art. 81).",
  "Resolución sobre la **relación de causalidad** y la indemnización; a los **seis meses** sin resolver, se entiende **desestimada** (art. 91); resuelve el **Ministro** (o el Consejo de Ministros en el art. 32.3) (art. 92).",
  "Simplificado: de oficio, si todo es **inequívoco**; **30 días** (art. 96). Pone **fin a la vía administrativa** (art. 114.1 e) y va al **contencioso** (LJCA, art. 2 e)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX = [
 ("L", 56, "Desestimación por silencio a los seis meses (→ III.4.2)", {
   "a": "Cambia el plazo: el art. 91.3 dice **seis** meses, no cinco.",
   "b": "Cambia el plazo (tres meses) y omite el acuerdo formalizado.",
   "c": f"Literal del art. 91.3: {c('L39', 'Artículo 91', 'Transcurridos seis meses desde que se inició el procedimiento sin que haya recaído y se notifique resolución expresa o, en su caso, se haya formalizado el acuerdo, podrá entenderse que la resolución es contraria a la indemnización del particular')}.",
   "d": "Cambia el plazo (dos meses) y omite el acuerdo formalizado."},
   [("seis meses", "L39", "Artículo 91", "Transcurridos seis meses desde que se inició el procedimiento")]),
 ("P", 71, "Prescripción del derecho a reclamar (→ III.2.3)", {
   "a": "Cambia el plazo: tres meses no aparece en el art. 67.1.",
   "b": "Cambia el plazo: seis meses es el plazo del **silencio** (art. 91.3), no el de prescripción.",
   "c": f"Literal del art. 67.1: {c('L39', 'Artículo 67', 'El derecho a reclamar prescribirá al año de producido el hecho o el acto que motive la indemnización o se manifieste su efecto lesivo')}.",
   "d": "Cambia el plazo: dos años no es el de la Ley 39/2015."},
   [("Al año de producido el hecho", "L39", "Artículo 67", "prescribirá al año de producido el hecho")]),
 ("X", 61, "La anulación no presupone indemnización (→ I.2.1)", {
   "a": "Contradice el art. 32.1: la anulación **no** otorga «siempre» derecho a indemnización.",
   "b": "Contradice el art. 32.1: la anulación **no presupone** el derecho a ser indemnizado.",
   "c": "El art. 32.1 no condiciona la indemnización solo a que el daño sea evaluable: exige todos los requisitos de la responsabilidad (lesión antijurídica, daño efectivo, evaluable e individualizado, relación con el servicio).",
   "d": f"Literal del art. 32.1, párrafo segundo: {c('L40', 'Artículo 32', 'La anulación en vía administrativa o por el orden jurisdiccional contencioso administrativo de los actos o disposiciones administrativas no presupone, por sí misma, derecho a la indemnización')}."},
   [("no presupone, por sí misma, derecho a la indemnización", "L40", "Artículo 32", "no presupone, por sí misma, derecho a la indemnización")]),
]
bloques = []
for cod, n, tit, por, ap_ in EX:
    bloques += [f"### {('GACE-L' if cod == 'L' else 'GACE-P' if cod == 'P' else 'GACE-L extraordinario')} 2025, pregunta {n} · {tit}", examen(cod, n, por, ap_)]
T.ap("s13", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join(
  ["En los primeros ejercicios de **2025** cayeron **tres** preguntas de este tema, una en cada examen, todas literales. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal."]
  + bloques + ["### Cómo se pregunta", "!> Las tres citan el **artículo** y cambian **un plazo** (tres, seis meses, un año, dos años) o **invierten la regla** («siempre», «automáticamente»). Memoriza los plazos del procedimiento y las negaciones literales del art. 32."]))

T.ap("s14", "Cierre 2. Repaso en 10 minutos (por bloques)", """
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Cuándo se responde | Art. 106.2 CE; responsabilidad **objetiva** por funcionamiento **normal o anormal**, salvo **fuerza mayor** (art. 32 LRJSP) | La **anulación** no presupone indemnización; daño **efectivo, evaluable e individualizado** |
| II. Cuánto y quién | Concurrencia (art. 33), cálculo (art. 34), acción de regreso (art. 36) | Fórmulas conjuntas: **solidaria**; regreso por **dolo o culpa o negligencia graves** |
| III. Procedimiento | Ley 39/2015 con especialidades; contencioso (LJCA, art. 2 e) | Prescripción **1 año**; dictamen desde **50.000 €**; silencio negativo a los **6 meses**; simplificado **30 días** |

?> **Trampas frecuentes:** «solo por funcionamiento anormal» (también el **normal**); «la anulación da siempre derecho a indemnización» (**no por sí misma**); «prescribe a los seis meses» (**un año**; los seis meses son del **silencio**); «dictamen desde 30.000 €» (**50.000**); «resuelve el Consejo de Ministros» (en la AGE, el **Ministro**, salvo el art. 32.3); «se demanda ante el orden civil si la relación es privada» (**siempre contencioso**).
""")

# =============================================================================
Q = [
 ("CE", "Artículo 106", "Fundamento", "Según el artículo 106.2 de la Constitución, los particulares tendrán derecho a ser indemnizados por toda lesión que sufran en cualquiera de sus bienes y derechos, siempre que la lesión sea consecuencia del funcionamiento de los servicios públicos, salvo en los casos de:",
  ["Fuerza mayor.", "Caso fortuito.", "Culpa leve del funcionario.", "Funcionamiento normal del servicio."], "Art. 106.2 CE.", "salvo en los casos de fuerza mayor"),
 ("CE", "Artículo 121", "Fundamento", "Según el artículo 121 de la Constitución, los daños causados por error judicial darán derecho a una indemnización a cargo:",
  ["Del Estado.", "Del Consejo General del Poder Judicial.", "Del Juez o Magistrado causante.", "De la Comunidad Autónoma donde radique el órgano judicial."], "Art. 121 CE.", "darán derecho a una indemnización a cargo del Estado"),
 ("L40", "Artículo 32", "Requisitos", "Según el artículo 32.1 de la Ley 40/2015, los particulares tendrán derecho a ser indemnizados de toda lesión que sea consecuencia del funcionamiento:",
  ["Normal o anormal de los servicios públicos.", "Anormal de los servicios públicos exclusivamente.", "Culposo de los servicios públicos.", "Ilegal de los servicios públicos."], "Art. 32.1 LRJSP: responsabilidad objetiva.", "funcionamiento normal o anormal de los servicios públicos"),
 ("L40", "Artículo 32", "Requisitos", "Según el artículo 32.2 de la Ley 40/2015, el daño alegado habrá de ser:",
  ["Efectivo, evaluable económicamente e individualizado con relación a una persona o grupo de personas.", "Efectivo, cierto y referido a una colectividad indeterminada.", "Evaluable económicamente, aunque sea futuro o hipotético.", "Grave, permanente e individualizado."], "Art. 32.2 LRJSP.", "efectivo, evaluable económicamente e individualizado con relación a una persona o grupo de personas"),
 ("L40", "Artículo 32", "Estado legislador", "Según el artículo 32.4 de la Ley 40/2015, si la lesión es consecuencia de una norma con rango de ley declarada inconstitucional, procederá su indemnización cuando el particular haya obtenido, en cualquier instancia:",
  ["Sentencia firme desestimatoria de un recurso contra la actuación administrativa que ocasionó el daño, siempre que se hubiera alegado la inconstitucionalidad posteriormente declarada.", "Sentencia firme estimatoria de un recurso contra la actuación administrativa que ocasionó el daño.", "Sentencia del Tribunal Constitucional en un recurso de amparo.", "Resolución administrativa firme, sin necesidad de haber alegado la inconstitucionalidad."], "Art. 32.4 LRJSP.", "sentencia firme desestimatoria de un recurso contra la actuación administrativa que ocasionó el daño, siempre que se hubiera alegado la inconstitucionalidad posteriormente declarada"),
 ("L40", "Artículo 32", "Estado legislador", "Según el artículo 32.5 de la Ley 40/2015, en la responsabilidad por aplicación de una norma contraria al Derecho de la Unión Europea, el incumplimiento ha de estar:",
  ["Suficientemente caracterizado.", "Declarado por la Comisión Europea.", "Reconocido por el Consejo de Estado.", "Sancionado por el Tribunal de Cuentas Europeo."], "Art. 32.5 b) LRJSP.", "El incumplimiento ha de estar suficientemente caracterizado"),
 ("L40", "Artículo 32", "Estado legislador", "Según el artículo 32.6 de la Ley 40/2015, la sentencia que declare la inconstitucionalidad de la norma con rango de ley producirá efectos, salvo que en ella se establezca otra cosa:",
  ["Desde la fecha de su publicación en el «Boletín Oficial del Estado».", "Desde la fecha de entrada en vigor de la norma declarada inconstitucional.", "Desde que se notifique a las partes del proceso.", "Desde los veinte días siguientes a su publicación."], "Art. 32.6 LRJSP.", "producirá efectos desde la fecha de su publicación en el «Boletín Oficial del Estado»"),
 ("L40", "Artículo 32", "Requisitos", "Según el artículo 32.7 de la Ley 40/2015, la responsabilidad patrimonial del Estado por el funcionamiento de la Administración de Justicia se regirá por:",
  ["La Ley Orgánica 6/1985, de 1 de julio, del Poder Judicial.", "La propia Ley 40/2015.", "La Ley 39/2015, del Procedimiento Administrativo Común.", "La Ley 29/1998, reguladora de la Jurisdicción Contencioso-administrativa."], "Art. 32.7 LRJSP.", "se regirá por la Ley Orgánica 6/1985, de 1 de julio, del Poder Judicial"),
 ("L40", "Artículo 32", "Requisitos", "Según el artículo 32.8 de la Ley 40/2015, ¿quién fija el importe de las indemnizaciones cuando el Tribunal Constitucional haya declarado un funcionamiento anormal en la tramitación de los recursos de amparo o de las cuestiones de inconstitucionalidad?",
  ["El Consejo de Ministros.", "El Tribunal Constitucional.", "El Ministro de Justicia.", "El Consejo de Estado."], "Art. 32.8 LRJSP (tramita el Ministerio de Justicia, con audiencia al Consejo de Estado).", "El Consejo de Ministros fijará el importe de las indemnizaciones"),
 ("L40", "Artículo 33", "Concurrencia", "Según el artículo 33.1 de la Ley 40/2015, cuando de la gestión dimanante de fórmulas conjuntas de actuación entre varias Administraciones se derive responsabilidad, estas responderán frente al particular:",
  ["En todo caso, de forma solidaria.", "De forma mancomunada, según su participación.", "Solo la Administración con mayor participación en la financiación.", "De forma subsidiaria, por orden de competencia."], "Art. 33.1 LRJSP.", "responderán frente al particular, en todo caso, de forma solidaria"),
 ("L40", "Artículo 33", "Concurrencia", "Según el artículo 33.3 de la Ley 40/2015, en defecto de previsión en los Estatutos o reglas de la organización colegiada, la competencia para tramitar los procedimientos de responsabilidad concurrente corresponde a la Administración:",
  ["Con mayor participación en la financiación del servicio.", "Que primero tuvo conocimiento del daño.", "Del lugar donde se produjo la lesión.", "General del Estado en todo caso."], "Art. 33.3 LRJSP.", "la Administración Pública con mayor participación en la financiación del servicio"),
 ("L40", "Artículo 33", "Concurrencia", "Según el artículo 33.4 de la Ley 40/2015, la Administración competente deberá consultar a las restantes Administraciones implicadas para que puedan exponer cuanto consideren procedente en el plazo de:",
  ["Quince días.", "Diez días.", "Un mes.", "Veinte días."], "Art. 33.4 LRJSP.", "en el plazo de quince días"),
 ("L40", "Artículo 34", "Indemnización", "Según el artículo 34.1 de la Ley 40/2015, no serán indemnizables los daños que se deriven de hechos o circunstancias que no se hubiesen podido prever o evitar según el estado de los conocimientos de la ciencia o de la técnica existentes:",
  ["En el momento de producción de aquéllos.", "En el momento de presentar la reclamación.", "En el momento de dictarse la resolución.", "En el momento de la sentencia firme."], "Art. 34.1 LRJSP.", "existentes en el momento de producción de aquéllos"),
 ("L40", "Artículo 34", "Estado legislador", "Según el artículo 34.1 de la Ley 40/2015, en la responsabilidad por leyes declaradas inconstitucionales o contrarias al Derecho de la Unión Europea, serán indemnizables los daños producidos en el plazo de los:",
  ["Cinco años anteriores a la fecha de la publicación de la sentencia.", "Cuatro años anteriores a la fecha de la publicación de la sentencia.", "Diez años anteriores a la fecha de la sentencia.", "Dos años anteriores a la interposición del recurso."], "Art. 34.1, párrafo segundo, LRJSP.", "en el plazo de los cinco años anteriores a la fecha de la publicación de la sentencia"),
 ("L40", "Artículo 34", "Indemnización", "Según el artículo 34.3 de la Ley 40/2015, la cuantía de la indemnización se calculará con referencia:",
  ["Al día en que la lesión efectivamente se produjo.", "Al día en que se presentó la reclamación.", "Al día en que se dicte la resolución.", "Al día en que se emita el dictamen del Consejo de Estado."], "Art. 34.3 LRJSP (con actualización a la fecha de fin del procedimiento).", "con referencia al día en que la lesión efectivamente se produjo"),
 ("L40", "Artículo 34", "Indemnización", "Según el artículo 34.3 de la Ley 40/2015, la cuantía de la indemnización se actualizará a la fecha en que se ponga fin al procedimiento con arreglo:",
  ["Al Índice de Garantía de la Competitividad.", "Al Índice de Precios de Consumo.", "Al interés legal del dinero.", "Al Euríbor a un año."], "Art. 34.3 LRJSP.", "con arreglo al Índice de Garantía de la Competitividad"),
 ("L40", "Artículo 34", "Indemnización", "Según el artículo 34.4 de la Ley 40/2015, la indemnización podrá sustituirse por una compensación en especie o abonarse mediante pagos periódicos:",
  ["Cuando resulte más adecuado para lograr la reparación debida y convenga al interés público, siempre que exista acuerdo con el interesado.", "Siempre que lo decida unilateralmente la Administración.", "Solo en los casos de muerte o lesiones corporales.", "Solo si lo acuerda el Consejo de Ministros."], "Art. 34.4 LRJSP.", "siempre que exista acuerdo con el interesado"),
 ("L40", "Artículo 36", "Personal", "Según el artículo 36.1 de la Ley 40/2015, para hacer efectiva la responsabilidad patrimonial, los particulares exigirán las indemnizaciones por los daños causados por las autoridades y personal al servicio de la Administración:",
  ["Directamente a la Administración Pública correspondiente.", "Directamente a la autoridad o empleado causante del daño.", "Solidariamente a la Administración y al empleado causante.", "Al empleado y, subsidiariamente, a la Administración."], "Art. 36.1 LRJSP.", "exigirán directamente a la Administración Pública correspondiente"),
 ("L40", "Artículo 36", "Personal", "Según el artículo 36.2 de la Ley 40/2015, la Administración que hubiere indemnizado a los lesionados exigirá de oficio a sus autoridades y personal la responsabilidad en que hubieran incurrido por:",
  ["Dolo, o culpa o negligencia graves.", "Cualquier grado de culpa o negligencia.", "Dolo exclusivamente.", "Culpa leve reiterada."], "Art. 36.2 LRJSP.", "por dolo, o culpa o negligencia graves"),
 ("L40", "Artículo 36", "Personal", "Según el artículo 36.4 de la Ley 40/2015, en el procedimiento para exigir responsabilidad a las autoridades y personal, el trámite de audiencia durará:",
  ["Diez días.", "Quince días.", "Cinco días.", "Veinte días."], "Art. 36.4 c) LRJSP.", "Audiencia durante un plazo de diez días"),
 ("L40", "Artículo 37", "Personal", "Según el artículo 37.2 de la Ley 40/2015, la exigencia de responsabilidad penal del personal al servicio de las Administraciones Públicas:",
  ["No suspenderá los procedimientos de reconocimiento de responsabilidad patrimonial, salvo que la determinación de los hechos en el orden penal sea necesaria para fijarla.", "Suspenderá siempre los procedimientos de responsabilidad patrimonial.", "Impedirá iniciar el procedimiento de responsabilidad patrimonial hasta la sentencia penal.", "Extinguirá la responsabilidad patrimonial de la Administración."], "Art. 37.2 LRJSP.", "no suspenderá los procedimientos de reconocimiento de responsabilidad patrimonial que se instruyan, salvo que la determinación de los hechos en el orden jurisdiccional penal sea necesaria"),
 ("L39", "Artículo 24", "Procedimiento", "Según el artículo 24.1 de la Ley 39/2015, en los procedimientos de responsabilidad patrimonial de las Administraciones Públicas iniciados a solicitud del interesado, el silencio tendrá efecto:",
  ["Desestimatorio.", "Estimatorio.", "Estimatorio, salvo que una norma con rango de ley disponga lo contrario.", "Estimatorio si la cuantía no supera 50.000 euros."], "Art. 24.1 LPAC.", "El silencio tendrá efecto desestimatorio"),
 ("L39", "Artículo 65", "Procedimiento", "Según el artículo 65.2 de la Ley 39/2015, el acuerdo de iniciación de oficio de un procedimiento de responsabilidad patrimonial se notificará a los presuntos lesionados, concediéndoles para aportar alegaciones, documentos o información un plazo de:",
  ["Diez días.", "Quince días.", "Cinco días.", "Un mes."], "Art. 65.2 LPAC.", "concediéndoles un plazo de diez días"),
 ("L39", "Artículo 67", "Procedimiento", "Según el artículo 67.1 de la Ley 39/2015, en caso de daños de carácter físico o psíquico a las personas, el plazo para reclamar empezará a computarse:",
  ["Desde la curación o la determinación del alcance de las secuelas.", "Desde el día en que se produjo el daño, en todo caso.", "Desde el alta hospitalaria.", "Desde la declaración de incapacidad por la Seguridad Social."], "Art. 67.1 LPAC.", "el plazo empezará a computarse desde la curación o la determinación del alcance de las secuelas"),
 ("L39", "Artículo 67", "Procedimiento", "Según el artículo 67.1 de la Ley 39/2015, cuando proceda reconocer derecho a indemnización por anulación de un acto en vía administrativa o contencioso-administrativa, el derecho a reclamar prescribirá:",
  ["Al año de haberse notificado la resolución administrativa o la sentencia definitiva.", "A los seis meses de haberse notificado la resolución administrativa o la sentencia definitiva.", "Al año de haberse dictado el acto anulado.", "A los cuatro años de haberse notificado la sentencia definitiva."], "Art. 67.1, párrafo segundo, LPAC.", "prescribirá al año de haberse notificado la resolución administrativa o la sentencia definitiva"),
 ("L39", "Artículo 81", "Procedimiento", "Según el artículo 81.1 de la Ley 39/2015, el informe preceptivo del servicio cuyo funcionamiento haya ocasionado la presunta lesión no podrá exceder en su emisión de:",
  ["Diez días.", "Quince días.", "Un mes.", "Dos meses."], "Art. 81.1 LPAC.", "no pudiendo exceder de diez días el plazo de su emisión"),
 ("L39", "Artículo 81", "Procedimiento", "Según el artículo 81.2 de la Ley 39/2015, será preceptivo solicitar dictamen del Consejo de Estado o, en su caso, del órgano consultivo autonómico, cuando las indemnizaciones reclamadas sean de cuantía:",
  ["Igual o superior a 50.000 euros o a la que se establezca en la correspondiente legislación autonómica.", "Superior a 30.000 euros.", "Igual o superior a 6.000 euros.", "Superior a 100.000 euros, en todo caso."], "Art. 81.2 LPAC.", "de cuantía igual o superior a 50.000 euros o a la que se establezca en la correspondiente legislación autonómica"),
 ("L39", "Artículo 81", "Procedimiento", "Según el artículo 81.2 de la Ley 39/2015, el dictamen del Consejo de Estado en los procedimientos de responsabilidad patrimonial se emitirá en el plazo de:",
  ["Dos meses.", "Un mes.", "Diez días.", "Tres meses."], "Art. 81.2 LPAC.", "El dictamen se emitirá en el plazo de dos meses"),
 ("L39", "Artículo 81", "Procedimiento", "Según el artículo 81.3 de la Ley 39/2015, en las reclamaciones por el funcionamiento anormal de la Administración de Justicia será preceptivo el informe de:",
  ["El Consejo General del Poder Judicial.", "El Ministerio Fiscal.", "El Tribunal Supremo.", "La Abogacía General del Estado."], "Art. 81.3 LPAC (plazo máximo de dos meses).", "será preceptivo el informe del Consejo General del Poder Judicial"),
 ("L39", "Artículo 82", "Procedimiento", "Según el artículo 82.5 de la Ley 39/2015, en los procedimientos de responsabilidad patrimonial del artículo 32.9 de la Ley 40/2015 (daños durante la ejecución de contratos), será necesario en todo caso dar audiencia:",
  ["Al contratista.", "Al Consejo de Estado.", "A la Intervención General.", "Al órgano de contratación."], "Art. 82.5 LPAC.", "será necesario en todo caso dar audiencia al contratista"),
 ("L39", "Artículo 91", "Procedimiento", "Según el artículo 91.2 de la Ley 39/2015, la resolución de los procedimientos de responsabilidad patrimonial deberá pronunciarse necesariamente sobre:",
  ["La existencia o no de la relación de causalidad entre el funcionamiento del servicio público y la lesión producida.", "La responsabilidad disciplinaria del empleado causante del daño.", "La procedencia de pasar el tanto de culpa a la jurisdicción penal.", "La conveniencia de modificar el servicio público afectado."], "Art. 91.2 LPAC.", "sobre la existencia o no de la relación de causalidad entre el funcionamiento del servicio público y la lesión producida"),
 ("L39", "Artículo 92", "Procedimiento", "Según el artículo 92 de la Ley 39/2015, en el ámbito de la Administración General del Estado, los procedimientos de responsabilidad patrimonial se resolverán, como regla general, por:",
  ["El Ministro respectivo.", "El Consejo de Ministros.", "El Subsecretario del Departamento.", "El Delegado del Gobierno."], "Art. 92 LPAC (Consejo de Ministros: casos del art. 32.3 LRJSP o si una ley lo dispone).", "se resolverán por el Ministro respectivo"),
 ("L39", "Artículo 96", "Procedimiento", "Según el artículo 96.4 de la Ley 39/2015, en los procedimientos de responsabilidad patrimonial, si el órgano competente para su tramitación considera inequívoca la relación de causalidad, la valoración del daño y el cálculo de la cuantía, podrá:",
  ["Acordar de oficio la suspensión del procedimiento general y la iniciación de un procedimiento simplificado.", "Resolver sin dictamen del Consejo de Estado en todo caso.", "Prescindir del trámite de audiencia y del informe del servicio.", "Dictar resolución estimatoria sin más trámites."], "Art. 96.4 LPAC.", "podrá acordar de oficio la suspensión del procedimiento general y la iniciación de un procedimiento simplificado"),
 ("L39", "Artículo 96", "Procedimiento", "Según el artículo 96.6 de la Ley 39/2015, salvo que reste menos para su tramitación ordinaria, los procedimientos tramitados de manera simplificada deberán ser resueltos en:",
  ["Treinta días.", "Quince días.", "Dos meses.", "Tres meses."], "Art. 96.6 LPAC.", "deberán ser resueltos en treinta días"),
 ("L39", "Artículo 114", "Procedimiento", "Según el artículo 114.1 e) de la Ley 39/2015, pone fin a la vía administrativa la resolución de los procedimientos de responsabilidad patrimonial:",
  ["Cualquiera que fuese el tipo de relación, pública o privada, de que derive.", "Solo cuando derive de una relación de Derecho público.", "Solo cuando la dicte el Consejo de Ministros.", "Solo cuando haya mediado dictamen del Consejo de Estado."], "Art. 114.1 e) LPAC.", "cualquiera que fuese el tipo de relación, pública o privada, de que derive"),
 ("LJCA", "Artículo 2", "Procedimiento", "Según el artículo 2 e) de la Ley 29/1998, reguladora de la Jurisdicción Contencioso-administrativa, las Administraciones públicas no podrán ser demandadas por responsabilidad patrimonial ante los órdenes jurisdiccionales civil o social:",
  ["Aun cuando en la producción del daño concurran con particulares o cuenten con un seguro de responsabilidad.", "Salvo que en la producción del daño concurran con particulares.", "Salvo que cuenten con un seguro de responsabilidad.", "Salvo que la relación de la que derive el daño sea de Derecho privado."], "Art. 2 e) LJCA.", "aun cuando en la producción del daño concurran con particulares o cuenten con un seguro de responsabilidad"),
]
for k, art, cat, enun, ops, expl, frag in Q: T.q(k, art, cat, enun, ops, expl, frag)
for cod, n, *_ in EX: T.real(cod, n, "Preguntas oficiales")

for q_, a_, cat in [
  ("Única exclusión del art. 106.2 CE", "La fuerza mayor.", "Fundamento"),
  ("Responsabilidad por la Administración de Justicia", "Art. 121 CE: error judicial y funcionamiento anormal, a cargo del Estado; se rige por la LOPJ (art. 32.7 LRJSP).", "Fundamento"),
  ("¿Funcionamiento normal o anormal? (art. 32.1 LRJSP)", "Ambos: responsabilidad objetiva, salvo fuerza mayor o deber jurídico de soportar.", "Requisitos"),
  ("Caracteres del daño (art. 32.2)", "Efectivo, evaluable económicamente e individualizado con relación a una persona o grupo.", "Requisitos"),
  ("¿La anulación de un acto da derecho a indemnización? (art. 32.1)", "No presupone, por sí misma, derecho a la indemnización.", "Requisitos"),
  ("Estado legislador: requisitos comunes (art. 32.4 y 5)", "Sentencia firme desestimatoria previa y haber alegado la inconstitucionalidad o la infracción del Derecho de la UE.", "Estado legislador"),
  ("Requisitos adicionales del Derecho de la UE (art. 32.5)", "Norma que confiera derechos; incumplimiento suficientemente caracterizado; causalidad directa.", "Estado legislador"),
  ("Riesgos del progreso (art. 34.1)", "No indemnizables los daños imprevisibles o inevitables según la ciencia o la técnica del momento en que se producen.", "Indemnización"),
  ("Fórmulas conjuntas de actuación (art. 33.1)", "Responsabilidad solidaria en todo caso frente al particular.", "Concurrencia"),
  ("Fecha y actualización de la indemnización (art. 34.3)", "Día en que se produjo la lesión; actualización con el Índice de Garantía de la Competitividad.", "Indemnización"),
  ("Acción de regreso (art. 36.2)", "De oficio, contra autoridades y personal, por dolo, o culpa o negligencia graves.", "Personal"),
  ("Prescripción del derecho a reclamar (art. 67.1 LPAC)", "Un año desde el hecho o la manifestación del efecto lesivo; daños personales, desde la curación o la fijación de las secuelas.", "Procedimiento"),
  ("Dictamen del Consejo de Estado (art. 81.2 LPAC)", "Preceptivo desde 50.000 euros; se emite en dos meses.", "Procedimiento"),
  ("Silencio en responsabilidad patrimonial (arts. 24.1 y 91.3 LPAC)", "Desestimatorio; seis meses desde el inicio del procedimiento.", "Procedimiento"),
  ("¿Quién resuelve en la AGE? (art. 92 LPAC)", "El Ministro respectivo; el Consejo de Ministros en los casos del art. 32.3 LRJSP o si lo dice una ley.", "Procedimiento"),
  ("Procedimiento simplificado (art. 96.4 y 6 LPAC)", "De oficio, si causalidad, valoración y cuantía son inequívocas; resolución en 30 días.", "Procedimiento"),
  ("Jurisdicción (art. 2 e) LJCA)", "Siempre la contencioso-administrativa, aunque concurran particulares o haya seguro.", "Procedimiento"),
]: T.fc(q_, a_, cat)

T.glos("Lesión indemnizable", "Daño efectivo, evaluable económicamente e individualizado, que el particular no tiene el deber jurídico de soportar (LRJSP, arts. 32.2 y 34.1).", "s2", "Requisitos")
T.glos("Fuerza mayor", "Causa que excluye la responsabilidad patrimonial (art. 106.2 CE; LRJSP, art. 32.1).", "s1", "Requisitos")
T.glos("Responsabilidad objetiva", "La Administración responde por el funcionamiento normal o anormal de los servicios públicos, sin necesidad de culpa (LRJSP, art. 32.1). Expresión doctrinal, no literal de la ley.", "s2", "Requisitos")
T.glos("Responsabilidad del Estado legislador", "Indemnización por daños derivados de actos legislativos, de leyes inconstitucionales o de normas contrarias al Derecho de la UE (LRJSP, art. 32.3 a 6).", "s2", "Estado legislador")
T.glos("Riesgos del progreso", "Daños imprevisibles o inevitables según el estado de la ciencia o de la técnica en el momento de producirse; no indemnizables (LRJSP, art. 34.1). Expresión doctrinal.", "s3", "Indemnización")
T.glos("Responsabilidad concurrente", "La de varias Administraciones en un mismo daño: solidaria en las fórmulas conjuntas (LRJSP, art. 33).", "s4", "Concurrencia")
T.glos("Acción de regreso", "Exigencia de oficio, por la Administración que indemnizó, de la responsabilidad de su personal por dolo, o culpa o negligencia graves (LRJSP, art. 36.2). Expresión doctrinal.", "s6", "Personal")
T.glos("Índice de Garantía de la Competitividad", "Índice del INE con el que se actualiza la indemnización (LRJSP, art. 34.3).", "s5", "Indemnización")
T.glos("Procedimiento simplificado de responsabilidad patrimonial", "El que acuerda de oficio el órgano cuando la causalidad, la valoración y la cuantía son inequívocas; se resuelve en 30 días (LPAC, art. 96.4 y 6).", "s11", "Procedimiento")

T.hito("1954", "Ley de 16 de diciembre de 1954 sobre expropiación forzosa, art. 121", f"Ya preveía indemnizar la lesión consecuencia del {c('LEF', 'acientoveintiuno', 'funcionamiento normal o anormal de los servicios públicos')}, limitada a los bienes y derechos objeto de esa Ley (art. 121.1 y exposición de motivos; artículo que sigue en el texto consolidado)", "normativo", "s1")
T.hito("1978", "Constitución Española, arts. 106.2 y 121", "Garantía constitucional de la responsabilidad patrimonial, salvo fuerza mayor", "normativo", "s1")
T.hito("2015", "Leyes 39/2015 y 40/2015, de 1 de octubre (BOE de 2-10-2015)", "Separan el procedimiento (Ley 39) y el régimen sustantivo (Ley 40) de la responsabilidad patrimonial; entraron en vigor al año de su publicación", "normativo", "s2")

T.publicar()
