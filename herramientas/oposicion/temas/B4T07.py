# -*- coding: utf-8 -*-
"""Tema IV.7 (B4T07): Procedimientos y formas de la actividad administrativa. La actividad
de intervención, arbitral, de servicio público y de fomento. Formas de gestión de los
servicios públicos. Ayudas y subvenciones públicas: régimen jurídico.
Método del I.2: mapa → bloques (I a VI) con guía; cada artículo, texto literal del BOE
(o de EUR-Lex: TFUE) + ficha de casillas fijas; cierre 1 (preguntas oficiales) y cierre 2.
Normas: CE (arts. 103.1 y 128.2); Ley 39/2015 (arts. 1, 69, 86, 112 y disp. derogatoria);
Ley 40/2015 (arts. 3, 4 y 47); Ley 17/2009 (arts. 3 y 5); LRBRL (arts. 84, 84 bis, 85 y 86);
TRLGDCU (arts. 57 y 58); LCSP (arts. 15 y 284 y DA 34.ª); TFUE (arts. 107 y 108);
Ley 38/2003 General de Subvenciones y su Reglamento (RD 887/2006)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO["L17_2009"] = "Ley 17/2009"
CORTO["TRLGDCU"] = "TRLGDCU, RDLeg 1/2007"
CORTO["RD887"] = "Reglamento de la Ley General de Subvenciones, RD 887/2006"
CORTO["LRBRL"] = "LRBRL"
CORTO["TFUE"] = "TFUE"

T = Tema("B4T07",
  "Seis preguntas: I. Cómo actúa la Administración: principios, procedimientos y formas (art. 103.1 CE; Leyes 39/2015 y 40/2015) · II. Cómo interviene en la actividad privada (Ley 40/2015, art. 4; Ley 17/2009; Ley 39/2015, art. 69; LRBRL, arts. 84 y 84 bis) · III. Cuándo arbitra conflictos (Ley 39/2015, art. 112.2; TRLGDCU, arts. 57 y 58) · IV. Cómo presta servicios públicos y de qué formas los gestiona (art. 128.2 CE; LRBRL, arts. 85 y 86; LCSP) · V. Cómo fomenta: ayudas de Estado y subvenciones (TFUE, arts. 107 y 108; Ley 38/2003) · VI. Cómo se conceden, justifican, reintegran y sancionan las subvenciones (Ley 38/2003 y RD 887/2006). Cada artículo: texto literal del BOE y ficha.",
  ["Intervención", "Proporcionalidad", "Declaración responsable", "Licencia", "Arbitraje de consumo", "Servicio público", "Gestión directa", "Gestión indirecta", "Concesión de servicios", "Ayudas de Estado", "Subvención", "Ley 38/2003", "Concurrencia competitiva", "Concesión directa", "BDNS", "Reintegro", "Infracciones"])

# =============================================================================
T.ap("s0", "Mapa del tema: seis preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque IV, tema 7):
> Procedimientos y formas de la actividad administrativa. La actividad de intervención, arbitral, de servicio público y de fomento. Formas de gestión de los servicios públicos. Ayudas y subvenciones públicas: régimen jurídico.

### El hilo conductor

El epígrafe se lee como **seis preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Normas |
|---|---|---|
| **I** | ¿Cómo actúa la Administración? (procedimientos y formas de la actividad) | CE, art. 103.1; Ley 40/2015, arts. 3 y 47; Ley 39/2015, arts. 1 y 86 |
| **II** | ¿Cómo interviene en la actividad de los particulares? (actividad de intervención) | Ley 40/2015, art. 4; Ley 17/2009, arts. 3 y 5; Ley 39/2015, art. 69; LRBRL, arts. 84 y 84 bis |
| **III** | ¿Cuándo resuelve conflictos como árbitro? (actividad arbitral) | Ley 39/2015, art. 112.2; TRLGDCU (RDLeg 1/2007), arts. 57 y 58 |
| **IV** | ¿Cómo presta servicios públicos y de qué formas los gestiona? | CE, art. 128.2; LRBRL, arts. 85 y 86; LCSP, arts. 15 y 284 y disp. adic. 34.ª |
| **V** | ¿Cómo fomenta? Ayudas de Estado y régimen jurídico de las subvenciones | TFUE, arts. 107 y 108; Ley 38/2003, arts. 1 a 6, 8 a 14, 17 y 20; RD 887/2006, art. 3 |
| **VI** | ¿Cómo se conceden, justifican, reintegran y sancionan las subvenciones? | Ley 38/2003, arts. 22, 23, 30, 34, 36 a 39, 42, 52, 54, 56 a 59 y 65; RD 887/2006, arts. 65 y 69 |

!> **La idea que une los seis bloques:** la Administración actúa siempre con **sometimiento pleno a la ley y al Derecho** y por medio de **actos, procedimientos, acuerdos y convenios** (I). Con esos instrumentos **limita** la actividad privada, con proporcionalidad y prefiriendo la declaración responsable a la licencia (II); en ocasiones **arbitra** conflictos (III); **presta** servicios de su titularidad, directamente o por concesión (IV), y **fomenta** actividades de interés público con dinero público sin contraprestación: la **subvención** (V y VI).

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE; el TFUE, con la etiqueta DOUE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- El acto administrativo (tema IV.4), los contratos (temas IV.5 y IV.6) y la potestad sancionadora general se estudian en sus temas; aquí se remite a ellos.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Cómo actúa la Administración? Procedimientos y formas de la actividad administrativa", donde(
  "Primera pregunta del tema. Antes de ver **qué** hace la Administración (intervenir, arbitrar, prestar servicios, fomentar), hay que saber **con qué principios** actúa y **por qué cauces** (procedimiento, acto, acuerdo, convenio).",
  ["1 Los principios de toda actuación administrativa (art. 103.1 CE; Ley 40/2015, art. 3)", "2 Procedimiento, terminación convencional y convenios (Ley 39/2015, arts. 1 y 86; Ley 40/2015, art. 47)", "3 Cuadro de las formas de la actividad administrativa"]))

T.ap("s1", "I.1 Los principios de toda actuación administrativa (art. 103.1 CE; Ley 40/2015, art. 3)", f"""
Cualquier forma de actividad (intervención, arbitraje, servicio público, fomento) está sujeta a los mismos principios constitucionales y legales.

{unidad("1.1 La Administración sirve los intereses generales (art. 103.1 CE)",
  lit("CE", "Artículo 103", ["sirve con objetividad los intereses generales", "con sometimiento pleno a la ley y al Derecho"], solo=[1]),
  fichab("Mandato constitucional sobre la actuación de la Administración",
         c("CE", "Artículo 103", "La Administración Pública"),
         ["::Actúa de acuerdo con los principios de:", "Eficacia", "Jerarquía", "Descentralización", "Desconcentración", "Coordinación"],
         "—",
         "Son **cinco** principios; la Constitución dice «con sometimiento pleno a la **ley y al Derecho**»."))}

{unidad("1.2 Principios generales del sector público (Ley 40/2015, art. 3.1)",
  lit("L40", "Artículo 3", ["con sometimiento pleno a la Constitución, a la Ley y al Derecho", "Buena fe, confianza legítima y lealtad institucional", "Racionalización y agilidad de los procedimientos administrativos y de las actividades materiales de gestión"], solo=list(range(1, 14))),
  fichab("Desarrollo legal de los principios del art. 103.1 CE",
         c("L40", "Artículo 3", "Las Administraciones Públicas"),
         ["Repite los cinco principios del 103.1 CE y añade el sometimiento a la **Constitución**", "Añade once principios de actuación y relaciones (letras a a k)"],
         "—",
         "La letra d) habla de procedimientos **y** de «actividades materiales de gestión»: la Administración actúa por actos jurídicos y también por actividad material."))}
""", 2)

T.ap("s2", "I.2 Procedimiento, terminación convencional y convenios (Ley 39/2015, arts. 1 y 86; Ley 40/2015, art. 47)", f"""
La forma ordinaria de actuar es el **acto** dictado en un **procedimiento** (tema IV.4); la ley admite también formas **consensuales**: acuerdos que terminan el procedimiento y convenios.

{unidad("2.1 El procedimiento administrativo común (Ley 39/2015, art. 1.1)",
  lit("L39", "Artículo 1", ["los requisitos de validez y eficacia de los actos administrativos", "el procedimiento administrativo común a todas las Administraciones Públicas"], solo=[1]),
  fichab("Objeto de la Ley 39/2015",
         "Todas las Administraciones Públicas",
         ["Requisitos de validez y eficacia de los **actos** administrativos", "**Procedimiento** administrativo común (incluidos el **sancionador** y el de **responsabilidad patrimonial**)", "Principios de la iniciativa legislativa y de la potestad reglamentaria"],
         "—",
         "El procedimiento sancionador y el de responsabilidad patrimonial **no** son procedimientos especiales aparte: están **incluidos** en el común."))}

{unidad("2.2 Terminación convencional (Ley 39/2015, art. 86)",
  lit("L39", "Artículo 86", ["acuerdos, pactos, convenios o contratos con personas tanto de Derecho público como privado", "ni versen sobre materias no susceptibles de transacción", "la aprobación expresa del Consejo de Ministros", "no supondrán alteración de las competencias"], solo=[1, 2, 3, 4]),
  fichab("Forma consensual de terminar (o preparar la terminación de) un procedimiento",
         f"Las Administraciones Públicas con {c('L39', 'Artículo 86', 'personas tanto de Derecho público como privado')}",
         ["::Requisitos (86.1):", "No contrarios al ordenamiento jurídico", "No sobre materias no susceptibles de transacción", "Que satisfagan el interés público encomendado", "::Contenido mínimo (86.2): partes, ámbito personal, funcional y territorial y plazo de vigencia"],
         f"Aprobación expresa del **Consejo de Ministros** (u órgano autonómico equivalente) si versan sobre materias de su competencia directa (86.3)",
         "Pueden **finalizar** el procedimiento o insertarse en él **con carácter previo**, vinculante o no, a la resolución. **No alteran** las competencias de los órganos (86.4)."))}

{unidad("2.3 Los convenios (Ley 40/2015, art. 47.1 y 2)",
  lit("L40", "Artículo 47", ["acuerdos con efectos jurídicos", "para un fin común", "No tienen la consideración de convenios, los Protocolos Generales de Actuación", "no podrán tener por objeto prestaciones propias de los contratos"], solo=[1, 2, 3, 4, 5, 7, 8, 9]),
  fichab("Acuerdo con efectos jurídicos para un fin común",
         "Administraciones Públicas, organismos públicos y entidades de derecho público vinculados o dependientes y Universidades públicas, entre sí o con sujetos de derecho privado",
         ["::Tipos (47.2):", "Interadministrativos", "Intradministrativos", "Con sujetos de Derecho privado", "Con sujetos de Derecho internacional (no tratados ni acuerdos internacionales)"],
         "—",
         "Los **protocolos generales de actuación** no son convenios si no formalizan compromisos jurídicos concretos y exigibles. Si el objeto son **prestaciones propias de los contratos**, se aplica la legislación de contratos (temas IV.5 y IV.6)."))}
""", 2)

T.ap("s3", "I.3 Cuadro de las formas de la actividad administrativa (esquema)", f"""
*Esquema de elaboración propia: ordena las formas de actividad que enumera el epígrafe y remite a los artículos citados en este tema; no es texto legal.*

| Forma de actividad (epígrafe) | Qué hace la Administración | Instrumentos que se ven en este tema | Bloque |
|---|---|---|---|
| **Intervención** | Limita derechos o exige requisitos para desarrollar una actividad | Proporcionalidad (Ley 40/2015, art. 4); autorización, declaración responsable y comunicación (Ley 17/2009; Ley 39/2015, art. 69); medios de intervención locales (LRBRL, art. 84) | → II.1 |
| **Arbitral** | Resuelve controversias en lugar de un juez o de un recurso | Sustitución de recursos por arbitraje (Ley 39/2015, art. 112.2); Sistema Arbitral del Consumo (TRLGDCU, arts. 57 y 58) | → III.1 |
| **Servicio público** | Presta servicios de su titularidad o competencia | Reserva al sector público (art. 128.2 CE; LRBRL, art. 86); gestión directa e indirecta (LRBRL, art. 85); concesión de servicios (LCSP) | → IV.1 |
| **Fomento** | Estimula actividades de utilidad pública o interés social | Ayudas de Estado (TFUE, arts. 107 y 108); subvenciones (Ley 38/2003) | → V.1 |

{resumen([
  "La Administración sirve con **objetividad** los intereses generales, con **sometimiento pleno a la ley y al Derecho** (103.1 CE); la Ley 40/2015 añade el sometimiento a la **Constitución** y once principios de actuación (art. 3).",
  "Forma ordinaria: el **acto** dictado en el **procedimiento administrativo común**, que incluye el sancionador y el de responsabilidad patrimonial (Ley 39/2015, art. 1).",
  "Formas consensuales: **terminación convencional** (no en materias no susceptibles de transacción; Consejo de Ministros si es de su competencia directa) y **convenios** (fin común; nunca prestaciones propias de los contratos)."],
  "Siguiente: II. ¿Cómo interviene la Administración en la actividad de los particulares?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Cómo interviene la Administración en la actividad de los particulares? La actividad de intervención", donde(
  "Segunda pregunta. La Administración puede **limitar** derechos o **exigir requisitos** para ejercer una actividad. La ley vigente le impone una regla: elegir la medida **menos restrictiva**; por eso la licencia previa es la excepción y la declaración responsable o la comunicación, la regla.",
  ["1 Principios de la intervención (Ley 40/2015, art. 4; Ley 17/2009, arts. 3 y 5)", "2 Declaración responsable y comunicación (Ley 39/2015, art. 69)", "3 La intervención de las Entidades locales (LRBRL, arts. 84 y 84 bis)"]))

T.ap("s4", "II.1 Principios de la intervención (Ley 40/2015, art. 4; Ley 17/2009, arts. 3 y 5)", f"""
{unidad("1.1 Proporcionalidad y medida menos restrictiva (Ley 40/2015, art. 4)",
  lit("L40", "Artículo 4", ["aplicar el principio de proporcionalidad y elegir la medida menos restrictiva", "sin que en ningún caso se produzcan diferencias de trato discriminatorias", "evaluar periódicamente los efectos y resultados obtenidos", "comprobar, verificar, investigar e inspeccionar"]),
  fichab("Reglas para cualquier medida que limite derechos o exija requisitos para una actividad",
         "Todas las Administraciones Públicas, en el ejercicio de sus competencias",
         ["Aplicar el principio de **proporcionalidad** y elegir la medida **menos restrictiva**", "**Motivar** su necesidad para la protección del interés público", "**Justificar** su adecuación a los fines", "Sin diferencias de trato discriminatorias", "**Evaluar periódicamente** los efectos y resultados", "Potestad de **comprobar, verificar, investigar e inspeccionar** (4.2), con los límites de la protección de datos"],
         "Evaluación «periódica» (la ley no fija un plazo)",
         "Las tres exigencias son **proporcionalidad**, **necesidad** (motivada) y **adecuación** (justificada). La evaluación de efectos es **periódica**, no única."))}

{unidad("1.2 Autorización y régimen de autorización (Ley 17/2009, art. 3.7 y 3.10)",
  lit("L17_2009", "Artículo 3", ["con carácter previo"], solo=[8, 11], titulo="Artículo 3. Definiciones (Ley 17/2009), apartados 7 y 10"),
  fichab("Qué es una autorización en el acceso a las actividades de servicios",
         c("L17_2009", "Artículo 3", "la autoridad competente"),
         f"Acto {c('L17_2009', 'Artículo 3', 'expreso o tácito')}, exigido {c('L17_2009', 'Artículo 3', 'con carácter previo')} para el acceso o el ejercicio",
         "—",
         "La autorización puede ser **expresa o tácita**; lo que la define es que se exige **antes** de acceder a la actividad o ejercerla."))}

{unidad("1.3 Cuándo puede exigirse autorización (Ley 17/2009, art. 5)",
  lit("L17_2009", "Artículo 5", ["salvo excepcionalmente", "No discriminación", "Necesidad", "Proporcionalidad", "cuando sea suficiente una comunicación o una declaración responsable"]),
  fichab("La autorización previa como excepción en las actividades de servicios",
         "La normativa reguladora de la actividad; las condiciones deben motivarse en la **ley** que establezca el régimen",
         ["::Tres condiciones acumulativas:", "**No discriminación** (nacionalidad, territorio, domicilio social)", "**Necesidad**: orden público, seguridad pública, salud pública, medio ambiente, escasez de recursos naturales o impedimentos técnicos", "**Proporcionalidad**: no hay medidas menos restrictivas que logren el mismo resultado"],
         "—",
         f"{c('L17_2009', 'Artículo 5', 'en ningún caso')} se exigirá autorización cuando baste una **comunicación** o una **declaración responsable**. Las condiciones se motivan en la **ley**, no en un reglamento."))}
""", 2)

T.ap("s5", "II.2 Declaración responsable y comunicación (Ley 39/2015, art. 69)", f"""
{unidad("2.1 Concepto, efectos y consecuencias de la inexactitud (art. 69)",
  lit("L39", "Artículo 69", ["bajo su responsabilidad", "ponen en conocimiento de la Administración Pública competente sus datos identificativos", "desde el día de su presentación", "de carácter esencial", "sin que sea posible la exigencia de ambas acumulativamente"], solo=[1, 2, 3, 4, 5, 6, 7, 9]),
  fichab("Técnicas de intervención que sustituyen a la autorización previa",
         "El **interesado** las presenta; la **Administración** comprueba, controla e inspecciona",
         ["**Declaración responsable**: el interesado manifiesta, bajo su responsabilidad, que **cumple los requisitos**, que **dispone de la documentación** y que se compromete a **mantener** su cumplimiento", "**Comunicación**: pone en conocimiento de la Administración sus **datos** identificativos o datos relevantes", "Inexactitud, falsedad u omisión **esencial**: imposibilidad de continuar desde que se tenga constancia"],
         f"Efectos {c('L39', 'Artículo 69', 'desde el día de su presentación')}; la comunicación puede presentarse después del inicio si la ley lo prevé expresamente",
         "Solo **una** de las dos para la misma actividad: nunca las **dos acumulativamente** (69.6). El efecto es **inmediato**: desde la **presentación**, sin esperar respuesta."))}
""", 2)

T.ap("s6", "II.3 La intervención de las Entidades locales (LRBRL, arts. 84 y 84 bis)", f"""
{unidad("3.1 Medios de intervención local (LRBRL, art. 84)",
  lit("LRBRL", "Artículo 84", ["Ordenanzas y bandos", "Sometimiento a previa licencia y otros actos de control preventivo", "Sometimiento a comunicación previa o a declaración responsable", "Sometimiento a control posterior al inicio de la actividad", "Órdenes individuales constitutivas de mandato", "igualdad de trato, necesidad y proporcionalidad"]),
  fichab("Cómo intervienen las Entidades locales la actividad de los ciudadanos",
         c("LRBRL", "Artículo 84", "Las Entidades locales"),
         ["::Cinco medios (84.1):", "a) Ordenanzas y bandos", "b) Licencia previa y otros controles preventivos", "c) Comunicación previa o declaración responsable", "d) Control posterior al inicio de la actividad", "e) Órdenes individuales de mandato o prohibición"],
         "—",
         f"Principios: **igualdad de trato, necesidad y proporcionalidad** (84.2). La letra c) remite al art. 71 bis de la Ley 30/1992: esa ley está derogada y las referencias a ella {c('L39', 'Disposición derogatoria única', 'deberán entenderse efectuadas a las disposiciones de esta Ley que regulan la misma materia')} (Ley 39/2015: hoy art. 69, → II.2.1)."))}

{unidad("3.2 La licencia, solo como excepción (LRBRL, art. 84 bis.1)",
  lit("LRBRL", "Artículo 84 bis", ["no se someterá a la obtención de licencia u otro medio de control preventivo", "no puedan salvaguardarse mediante la presentación de una declaración responsable o de una comunicación", "el número de operadores económicos del mercado sea limitado"], solo=[1, 2, 3, 4]),
  fichab("Regla general: actividad sin licencia",
         "Entidades locales",
         ["::Solo cabe licencia u otro control preventivo de actividades económicas:", "a) Por orden público, seguridad pública, salud pública o medio ambiente **en el lugar concreto**, si no bastan la declaración responsable o la comunicación", "b) Si el número de operadores es **limitado** (escasez de recursos naturales, dominio público, impedimentos técnicos, servicios públicos con tarifas reguladas)"],
         "—",
         "Regla general: **sin licencia** («con carácter general»). Las instalaciones físicas solo se someten a autorización cuando lo establezca una **Ley** (84 bis.2)."))}

{resumen([
  "Toda limitación exige **proporcionalidad** y la **medida menos restrictiva**, motivando su necesidad y justificando su adecuación, y se evalúa **periódicamente** (Ley 40/2015, art. 4).",
  "En los servicios, la **autorización** es excepcional: **no discriminación, necesidad y proporcionalidad**, motivadas en la **ley**; nunca si basta una comunicación o una declaración responsable (Ley 17/2009, art. 5).",
  "**Declaración responsable** y **comunicación**: efectos desde la **presentación**; nunca las dos a la vez (Ley 39/2015, art. 69).",
  "Entes locales: **cinco** medios de intervención (LRBRL, art. 84); con carácter general, **sin licencia** (art. 84 bis)."],
  "Siguiente: III. ¿Cuándo resuelve conflictos la Administración como árbitro?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Cuándo resuelve conflictos la Administración? La actividad arbitral", donde(
  "Tercera pregunta. En algunos casos la Administración no decide sobre sus propios asuntos, sino que **resuelve controversias**: sustituyendo el recurso administrativo por un arbitraje ante órganos no sometidos a instrucciones jerárquicas, o en conflictos entre particulares (consumidores y empresarios).",
  ["1 El arbitraje en lugar del recurso administrativo (Ley 39/2015, art. 112.2)", "2 El Sistema Arbitral del Consumo (TRLGDCU, arts. 57 y 58)"]))

T.ap("s7", "III.1 El arbitraje en lugar del recurso administrativo (Ley 39/2015, art. 112.2)", f"""
{unidad("1.1 Sustitución de la alzada y de la reposición (art. 112.2)",
  lit("L39", "Artículo 112", ["Las leyes podrán sustituir el recurso de alzada", "conciliación, mediación y arbitraje", "no sometidas a instrucciones jerárquicas", "respetando su carácter potestativo para el interesado"], solo=[3, 4, 5]),
  fichab("Procedimientos alternativos de impugnación",
         f"Los establecen {c('L39', 'Artículo 112', 'Las leyes')}; resuelven {c('L39', 'Artículo 112', 'órganos colegiados o Comisiones específicas no sometidas a instrucciones jerárquicas')}",
         ["Sustituyen la **alzada** en supuestos o ámbitos sectoriales determinados, cuando la especificidad de la materia lo justifique", "Pueden sustituir la **reposición**, respetando su carácter **potestativo**", "Respetan los principios, garantías y plazos de la Ley 39/2015"],
         "—",
         "Solo por **ley** (no por reglamento). En la Administración local no pueden desconocer las facultades resolutorias de los **órganos representativos electos**."))}
""", 2)

T.ap("s8", "III.2 El Sistema Arbitral del Consumo (TRLGDCU, arts. 57 y 58)", f"""
{unidad("2.1 Qué es y quién lo integra (art. 57)",
  lit("TRLGDCU", "Artículo 57", ["sin formalidades especiales y con carácter vinculante y ejecutivo para ambas partes", "intoxicación, lesión o muerte o existan indicios racionales de delito", "se establecerá reglamentariamente por el Gobierno", "representantes de los sectores empresariales interesados, de las organizaciones de consumidores y usuarios y de las Administraciones públicas", "No serán vinculantes para los consumidores los convenios arbitrales suscritos con un empresario antes de surgir el conflicto"]),
  fichab("Sistema extrajudicial de resolución de conflictos entre consumidores y empresarios",
         "Órganos arbitrales con representantes de los **empresarios**, de los **consumidores** y de las **Administraciones públicas**; organización, gestión y procedimiento: **reglamento del Gobierno**",
         ["Sin formalidades especiales", "Laudo **vinculante y ejecutivo** para ambas partes", "Puede preverse la decisión **en equidad**, salvo que las partes opten por el arbitraje de derecho"],
         "—",
         "Excluidos: **intoxicación, lesión o muerte** e **indicios racionales de delito**. El convenio arbitral firmado **antes** del conflicto **no vincula al consumidor**, pero sí vale como aceptación del empresario."))}

{unidad("2.2 La sumisión es voluntaria (art. 58)",
  lit("TRLGDCU", "Artículo 58", ["será voluntaria y deberá constar expresamente", "declarados en concurso de acreedores"]),
  fichab("Cómo se somete un conflicto al Sistema Arbitral del Consumo",
         "Las **partes** (consumidor y empresario)",
         ["Sumisión **voluntaria** y **expresa**", "Por escrito, por medios electrónicos o en otra forma admitida que deje constancia"],
         "—",
         "Quedan sin efecto los convenios arbitrales y las ofertas públicas de adhesión de quienes sean declarados **en concurso de acreedores**."))}

{resumen([
  "Las **leyes** pueden sustituir la **alzada** (y la **reposición**, que sigue siendo **potestativa**) por impugnación, reclamación, conciliación, mediación y **arbitraje** ante órganos **no sometidos a instrucciones jerárquicas** (Ley 39/2015, art. 112.2).",
  "Sistema Arbitral del Consumo: extrajudicial, **sin formalidades**, laudo **vinculante y ejecutivo**; excluye **intoxicación, lesión o muerte** e **indicios de delito** (TRLGDCU, art. 57).",
  "Sumisión **voluntaria y expresa** (art. 58); el convenio previo al conflicto **no vincula al consumidor**."],
  "Siguiente: IV. ¿Cómo presta la Administración servicios públicos y de qué formas los gestiona?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Cómo presta servicios públicos y de qué formas los gestiona? Servicio público y formas de gestión", donde(
  "Cuarta pregunta. La Constitución reconoce la **iniciativa pública** en la economía y permite **reservar** al sector público servicios esenciales. La ley local enumera las **formas de gestión** (directa e indirecta) y la LCSP regula la gestión indirecta por **concesión de servicios**.",
  ["1 Iniciativa pública y reserva de servicios esenciales (art. 128.2 CE; LRBRL, art. 86)", "2 Formas de gestión de los servicios públicos locales (LRBRL, art. 85)", "3 La gestión indirecta: la concesión de servicios (LCSP, arts. 15 y 284 y disp. adic. 34.ª)"]))

T.ap("s9", "IV.1 Iniciativa pública y reserva de servicios esenciales (art. 128.2 CE; LRBRL, art. 86)", f"""
{unidad("1.1 Iniciativa pública y reserva por ley (art. 128.2 CE)",
  lit("CE", "Artículo 128", ["Se reconoce la iniciativa pública en la actividad económica", "Mediante ley se podrá reservar al sector público recursos o servicios esenciales"], solo=[2]),
  fichab("Base constitucional de la actividad de servicio público",
         "Los poderes públicos; la reserva, **mediante ley**",
         ["Reconoce la **iniciativa pública** en la actividad económica", "Permite **reservar** al sector público recursos o servicios **esenciales**, especialmente en caso de **monopolio**", "Permite acordar la **intervención de empresas** cuando lo exija el interés general"],
         "—",
         "La reserva exige **ley** («Mediante ley»). El 128.1 subordina **toda la riqueza del país** al interés general."))}

{unidad("1.2 Iniciativa económica local y servicios reservados (LRBRL, art. 86)",
  lit("LRBRL", "Artículo 86", ["siempre que esté garantizado el cumplimiento del objetivo de estabilidad presupuestaria", "Corresponde al pleno de la respectiva Corporación local", "abastecimiento domiciliario y depuración de aguas; recogida, tratamiento y aprovechamiento de residuos, y transporte público de viajeros", "la aprobación por el órgano competente de la Comunidad Autónoma"], solo=[1, 2, 3, 4]),
  fichab("Cuándo pueden las Entidades locales desarrollar actividades económicas y qué servicios tienen reservados",
         "El **Pleno** aprueba el expediente y la forma concreta de gestión; para el **monopolio**, además, el órgano competente de la **Comunidad Autónoma**",
         ["Iniciativa pública con **estabilidad presupuestaria y sostenibilidad financiera** garantizadas", "Expediente con **análisis del mercado** (oferta, demanda, rentabilidad, efectos sobre la concurrencia)", "::Servicios reservados (86.2):", "Abastecimiento domiciliario y depuración de aguas", "Recogida, tratamiento y aprovechamiento de residuos", "Transporte público de viajeros"],
         "—",
         "Son **tres** servicios reservados por la LRBRL; el Estado y las CC. AA. pueden reservar otros **mediante Ley**. El monopolio necesita **Pleno + Comunidad Autónoma**."))}
""", 2)

T.ap("s10", "IV.2 Formas de gestión de los servicios públicos locales (LRBRL, art. 85)", f"""
{unidad("2.1 Gestión directa y gestión indirecta (art. 85)",
  lit("LRBRL", "Artículo 85", ["de la forma más sostenible y eficiente", "Gestión directa", "Gestión por la propia Entidad Local", "Organismo autónomo local", "Entidad pública empresarial local", "Sociedad mercantil local, cuyo capital social sea de titularidad pública", "memoria justificativa", "informe del interventor local", "Gestión indirecta"]),
  fichab("Cómo se gestionan los servicios públicos locales",
         "La Entidad local; la memoria justificativa se eleva al **Pleno**; informa el **interventor** local",
         ["::A) Gestión directa:", "a) Por la propia Entidad Local", "b) Organismo autónomo local", "c) Entidad pública empresarial local", "d) Sociedad mercantil local, cuyo capital social sea de **titularidad pública**", "::B) Gestión indirecta: las formas del contrato de gestión de servicios públicos (hoy, concesión de servicios, → IV.3.3)"],
         "Las formas c) y d), solo si una **memoria justificativa** acredita que son más sostenibles y eficientes que a) y b)",
         "Criterio legal: la forma **más sostenible y eficiente**. EPE y sociedad mercantil son **subsidiarias** de la gestión por la propia entidad y del organismo autónomo. Hay que respetar las funciones reservadas a **funcionarios** (art. 9 EBEP)."))}
""", 2)

T.ap("s11", "IV.3 La gestión indirecta: la concesión de servicios (LCSP, arts. 15 y 284 y disp. adic. 34.ª)", f"""
El régimen completo del contrato de concesión de servicios está en el tema IV.6; aquí, solo su definición y su ámbito como **forma de gestión indirecta**.

{unidad("3.1 Definición del contrato (LCSP, art. 15)",
  lit("LCSP", "Artículo 15", ["encomiendan a título oneroso", "la gestión de un servicio cuya prestación sea de su titularidad o competencia", "el derecho a explotar los servicios objeto del contrato", "la transferencia al concesionario del riesgo operacional"]),
  fichab("Contrato por el que se encomienda a otro la gestión de un servicio",
         "Uno o varios **poderes adjudicadores** → una o varias personas naturales o jurídicas (concesionario)",
         ["Encomienda **a título oneroso** la **gestión** de un servicio de su titularidad o competencia", "Contrapartida: el **derecho a explotar** el servicio, solo o con el de percibir un **precio**"],
         "—",
         "La explotación implica la **transferencia del riesgo operacional** al concesionario: es el rasgo que lo distingue."))}

{unidad("3.2 Ámbito de la concesión de servicios (LCSP, art. 284)",
  lit("LCSP", "Artículo 284", ["siempre que sean susceptibles de explotación económica por particulares", "En ningún caso podrán prestarse mediante concesión de servicios los que impliquen ejercicio de la autoridad inherente a los poderes públicos", "queda asumida por la Administración respectiva como propia de la misma"]),
  fichab("Qué servicios pueden gestionarse por concesión",
         "La Administración (gestión **indirecta**)",
         ["Servicios de su titularidad o competencia **susceptibles de explotación económica** por particulares", "Si es un **servicio público**, antes debe establecerse su **régimen jurídico**: asunción como propia, alcance de las prestaciones y aspectos jurídicos, económicos y administrativos", "El contrato fija el ámbito funcional y territorial"],
         "—",
         "Nunca por concesión los servicios que impliquen **ejercicio de la autoridad** inherente a los poderes públicos."))}

{unidad("3.3 La antigua «gestión de servicios públicos» (LCSP, disposición adicional trigésima cuarta)",
  lit("LCSP", "da-34", ["al contrato de concesión de servicios"]),
  fichab("Cómo se leen hoy las remisiones al contrato de gestión de servicios públicos",
         "—",
         f"Las referencias al contrato de gestión de servicios públicos (como la del art. 85.2 B LRBRL, → IV.2.1) se entienden hechas {c('LCSP', 'da-34', 'al contrato de concesión de servicios')}",
         "—",
         f"La LCSP derogó {c('LCSP', 'dd', 'el texto refundido de la Ley de Contratos del Sector Público aprobado por Real Decreto Legislativo 3/2011')}, al que remite literalmente el art. 85 LRBRL."))}

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| | Gestión directa (LRBRL 85.2 A) | Gestión indirecta (LRBRL 85.2 B; LCSP) |
|---|---|---|
| Quién presta | La propia entidad o un ente instrumental suyo (OA, EPE, sociedad de capital público) | Un concesionario, por contrato |
| Requisito especial | EPE y sociedad: **memoria justificativa** + informe del **interventor** | Servicio **susceptible de explotación económica**; régimen jurídico previo si es servicio público |
| Riesgo operacional | — (el art. 85 no lo menciona) | Se transfiere al **concesionario** (LCSP, art. 15.2) |
| Límite | Funciones reservadas a funcionarios (art. 9 EBEP) | Nunca **ejercicio de autoridad** |

{resumen([
  "**Mediante ley** se pueden reservar al sector público recursos o servicios **esenciales** (128.2 CE). La LRBRL reserva a los entes locales **aguas, residuos y transporte público de viajeros** (86.2).",
  "Formas de gestión local: **directa** (propia entidad, organismo autónomo, EPE, sociedad de capital público) o **indirecta**; se elige la **más sostenible y eficiente**; EPE y sociedad, solo con **memoria justificativa** (85).",
  "Gestión indirecta = **concesión de servicios**: gestión onerosa con **derecho de explotación** y **riesgo operacional**; nunca para el **ejercicio de autoridad** (LCSP, arts. 15 y 284)."],
  "Siguiente: V. ¿Cómo fomenta la Administración? Ayudas de Estado y subvenciones")}
""", 2)

# =============================================================================
T.ap("bV", "V. ¿Cómo fomenta la Administración? Ayudas de Estado y régimen jurídico de las subvenciones", donde(
  "Quinta pregunta. La actividad de **fomento** estimula actividades privadas de interés público. Su instrumento típico es la **subvención**: dinero público **sin contraprestación**, afectado a un fin. Antes, el Derecho de la UE: las **ayudas de Estado** que falsean la competencia son, en principio, incompatibles.",
  ["1 Las ayudas de Estado (TFUE, arts. 107 y 108.3)", "2 Concepto de subvención y exclusiones (Ley 38/2003, arts. 1, 2 y 4; RD 887/2006, art. 3)", "3 Ámbito y régimen jurídico (Ley 38/2003, arts. 3, 5 y 6)", "4 Principios, requisitos y órganos competentes (arts. 8 a 10)", "5 Beneficiarios y entidades colaboradoras (arts. 11 a 14)", "6 Bases reguladoras y Base de Datos Nacional de Subvenciones (arts. 17 y 20)"]))

T.ap("s12", "V.1 Las ayudas de Estado (TFUE, arts. 107 y 108.3)", f"""
{unidad("1.1 Incompatibilidad y excepciones (TFUE, art. 107)",
  lit("TFUE", "Artículo 107", ["serán incompatibles con el mercado interior", "que falseen o amenacen falsear la competencia, favoreciendo a determinadas empresas o producciones", "Serán compatibles con el mercado interior", "Podrán considerarse compatibles con el mercado interior"]),
  fichab("Prohibición general de las ayudas públicas que falsean la competencia",
         f"Ayudas {c('TFUE', 'Artículo 107', 'otorgadas por los Estados o mediante fondos estatales, bajo cualquier forma')}",
         ["::Incompatibles (107.1), si:", "Afectan a los intercambios entre Estados miembros", "Falsean o amenazan falsear la competencia", "Favorecen a determinadas empresas o producciones", "::Compatibles de pleno derecho (107.2): sociales a consumidores individuales; desastres naturales o acontecimientos excepcionales; división de Alemania", "::Pueden considerarse compatibles (107.3): regiones con nivel de vida anormalmente bajo o grave subempleo, proyectos de interés común europeo, desarrollo de actividades o regiones, cultura y patrimonio, y otras que determine el Consejo"],
         "—",
         "Distingue **«Serán compatibles»** (107.2, automáticas) de **«Podrán considerarse compatibles»** (107.3, valoración). Ayudas a **desastres naturales**: 107.2 (compatibles), no 107.3."))}

{unidad("1.2 Notificación previa y cláusula de suspensión (TFUE, art. 108.3)",
  lit("TFUE", "Artículo 108", ["con la suficiente antelación para poder presentar sus observaciones", "no podrá ejecutar las medidas proyectadas"], solo=[6]),
  fichab("Control previo de las ayudas nuevas por la Comisión",
         "La **Comisión** es informada; el **Estado miembro** espera",
         "El Estado informa a la Comisión de los proyectos de ayudas; si la Comisión los considera incompatibles, inicia el procedimiento del 108.2",
         "Con la «suficiente antelación»; no se ejecuta hasta la **decisión definitiva**",
         f"La Ley 38/2003 lo recoge: si hay que comunicar el proyecto, {c('LGS', 'Artículo 9', 'no se podrá hacer efectiva una subvención en tanto no sea considerada compatible con el mercado común')} (art. 9.1, → V.4.2)."))}
""", 2)

T.ap("s13", "V.2 Concepto de subvención y exclusiones (Ley 38/2003, arts. 1, 2 y 4; RD 887/2006, art. 3)", f"""
{unidad("2.1 Objeto de la ley y concepto de subvención (arts. 1 y 2.1)",
  lit("LGS", "Artículo 1", ["régimen jurídico general de las subvenciones otorgadas por las Administraciones públicas"]),
  lit("LGS", "Artículo 2", ["toda disposición dineraria", "sin contraprestación directa de los beneficiarios", "sujeta al cumplimiento de un determinado objetivo", "el fomento de una actividad de utilidad pública o interés social o de promoción de una finalidad pública"], solo=[1, 2, 3, 4]),
  fichab("Qué es una subvención",
         "La otorgan los sujetos del art. 3 (→ V.3.1) a favor de **personas públicas o privadas**",
         ["Disposición **dineraria**", "a) **Sin contraprestación directa** de los beneficiarios", "b) **Afectada** a un objetivo, proyecto, actividad, comportamiento o situación, con obligaciones materiales y formales", "c) Con objeto de **fomento** de una actividad de utilidad pública o interés social o de promoción de una finalidad pública"],
         "Los tres requisitos son **acumulativos**",
         "Sin contraprestación **directa** (no basta cualquier ausencia de contraprestación). La finalidad de **fomento** es requisito del concepto."))}

{unidad("2.2 Lo que no es subvención o queda fuera de la ley (arts. 2.2, 2.4 y 4)",
  lit("LGS", "Artículo 2", ["para financiar globalmente la actividad de la Administración a la que vayan destinadas", "Las prestaciones contributivas y no contributivas del Sistema de la Seguridad Social", "Los beneficios fiscales y beneficios en la cotización a la Seguridad Social", "El crédito oficial"], solo=[5, 7, 8, 12, 13, 14, 15]),
  lit("LGS", "Artículo 4", ["Los premios que se otorguen sin la previa solicitud del beneficiario", "Financiación de los Partidos Políticos"]),
  fichab("Exclusiones del concepto y del ámbito",
         "—",
         ["**No son subvención** (2.4): prestaciones de la Seguridad Social, clases pasivas, Fondo de Garantía Salarial, **beneficios fiscales** y en la cotización, **crédito oficial** (salvo subvención de intereses), entre otros", "**Fuera del ámbito** (2.2): aportaciones entre Administraciones para financiar **globalmente** su actividad", "**Excluidas de la ley** (art. 4): **premios sin solicitud** previa, subvenciones electorales (LOREG), de **partidos políticos** y a **grupos parlamentarios** y políticos"],
         "—",
         "Premios: excluidos solo los otorgados **sin previa solicitud**. Crédito oficial: no es subvención **salvo** que se subvencionen los intereses."))}

{unidad("2.3 Las ayudas en especie (RD 887/2006, art. 3.1)",
  lit("RD887", "a3", ["con la finalidad exclusiva de ser entregados a terceros", "tendrán la consideración de ayudas en especie"], solo=[1]),
  fichab("Entregas de bienes, derechos o servicios asimiladas a la subvención",
         "—",
         "Bienes, derechos o servicios **adquiridos con la finalidad exclusiva** de entregarlos a terceros, que cumplen los requisitos a), b) y c) del art. 2.1 de la Ley",
         "—",
         "Se sujetan a la Ley y al Reglamento; si procede el reintegro, se devuelve el **precio de adquisición** más el interés de demora (3.3)."))}
""", 2)

T.ap("s14", "V.3 Ámbito y régimen jurídico (Ley 38/2003, arts. 3, 5 y 6)", f"""
{unidad("3.1 Quién otorga subvenciones sujetas a la ley (art. 3.1 y 2)",
  lit("LGS", "Artículo 3", ["La Administración General del Estado", "Las entidades que integran la Administración local", "La Administración de las comunidades autónomas", "en la medida en que las subvenciones que otorguen sean consecuencia del ejercicio de potestades administrativas"], solo=[1, 2, 3, 4, 5, 6, 7]),
  fichab("Ámbito subjetivo",
         ["Administración General del Estado", "Entidades de la Administración local", "Administración de las comunidades autónomas", "Organismos y entidades de derecho público vinculados o dependientes, **si ejercen potestades administrativas**"],
         "A los entes de esas Administraciones que se rijan por **derecho privado** se les aplican los **principios de gestión** y los de **información** (art. 20) en sus entregas sin contraprestación",
         "—",
         "Los entes de derecho público quedan sujetos **en la medida** en que la subvención sea **ejercicio de potestades administrativas**."))}

{unidad("3.2 Régimen jurídico: el orden de fuentes (art. 5)",
  lit("LGS", "Artículo 5", ["por esta ley y sus disposiciones de desarrollo, las restantes normas de derecho administrativo, y, en su defecto, se aplicarán las normas de derecho privado"]),
  fichab("Qué normas rigen las subvenciones",
         "—",
         ["1.º Ley 38/2003 y sus disposiciones de desarrollo (RD 887/2006)", "2.º Restantes normas de **derecho administrativo**", "3.º En su defecto, **derecho privado**", "Consorcios, mancomunidades y convenios: su instrumento de creación o el convenio, ajustados a la ley (5.2)"],
         "—",
         "El derecho privado es **supletorio de segundo grado**: solo en defecto de las normas administrativas."))}

{unidad("3.3 Subvenciones financiadas con fondos de la Unión Europea (art. 6)",
  lit("LGS", "Artículo 6", ["por las normas comunitarias aplicables en cada caso y por las normas nacionales de desarrollo o transposición de aquéllas", "tendrán carácter supletorio"]),
  fichab("Régimen de las subvenciones con fondos europeos",
         "—",
         ["Se rigen por las **normas comunitarias** aplicables y por las **normas nacionales de desarrollo o transposición**", "Los procedimientos de **concesión y control** de la Ley 38/2003 son **supletorios** de las normas de aplicación directa"],
         "—",
         "La Ley 38/2003 es **supletoria**, no preferente (pregunta oficial P 64, → Cierre 1)."))}
""", 2)

T.ap("s15", "V.4 Principios, requisitos y órganos competentes (Ley 38/2003, arts. 8 a 10)", f"""
{unidad("4.1 Plan estratégico y principios de gestión (art. 8)",
  lit("LGS", "Artículo 8", ["plan estratégico de subvenciones", "corregir fallos claramente identificados", "Publicidad, transparencia, concurrencia, objetividad, igualdad y no discriminación", "Eficacia en el cumplimiento de los objetivos fijados", "Eficiencia en la asignación y utilización de los recursos públicos"]),
  fichab("Planificación y principios de las subvenciones",
         "Los órganos o entes que **propongan** establecer subvenciones",
         ["Con carácter **previo**: **plan estratégico** (objetivos y efectos, plazo, costes previsibles y fuentes de financiación), supeditado a la **estabilidad presupuestaria**", "Si afectan al mercado: corregir **fallos claramente identificados**, con efectos **mínimamente distorsionadores**", "::Principios de gestión (8.3):", "Publicidad, transparencia, concurrencia, objetividad, igualdad y no discriminación", "Eficacia", "Eficiencia"],
         "—",
         "El plan estratégico es **previo** al establecimiento. Las bases deben referirse a él o **motivar** por qué la subvención no estaba prevista."))}

{unidad("4.2 Requisitos para otorgar una subvención (art. 9)",
  lit("LGS", "Artículo 9", ["no se podrá hacer efectiva una subvención en tanto no sea considerada compatible con el mercado común", "deberán aprobarse las normas que establezcan las bases reguladoras", "La competencia del órgano administrativo concedente", "La existencia de crédito adecuado y suficiente", "La fiscalización previa", "La aprobación del gasto"]),
  fichab("Qué debe existir antes de conceder",
         "Órgano competente; la Comisión Europea si hay que comunicar el proyecto (→ V.1.2)",
         ["Comunicación a la Comisión y declaración de compatibilidad, cuando proceda (9.1)", "**Bases reguladoras** aprobadas **con carácter previo** y publicadas en el BOE o diario oficial (9.2 y 9.3)", "::Además (9.4):", "Competencia del órgano", "Crédito adecuado y suficiente", "Procedimiento conforme a las normas", "Fiscalización previa", "Aprobación del gasto"],
         "—",
         "**Cinco** requisitos del 9.4. Las bases son **previas** al otorgamiento."))}

{unidad("4.3 Órganos competentes en la AGE (art. 10.1 y 2)",
  lit("LGS", "Artículo 10", ["Los Ministros y los Secretarios de Estado", "previa consignación presupuestaria para este fin", "de cuantía superior a 12 millones de euros", "la previa autorización del Consejo de Ministros"], solo=[1, 2, 3, 5]),
  fichab("Quién concede en la Administración General del Estado",
         ["**Ministros** y **Secretarios de Estado**", "Presidentes o directores de los organismos y entidades públicas vinculados o dependientes"],
         "En sus respectivos ámbitos, **previa consignación presupuestaria**",
         "Más de **12 millones de euros**: autorización previa del **Consejo de Ministros** (o de la Comisión Delegada para Asuntos Económicos si lo prevé la normativa); en concurrencia competitiva, antes de aprobar la **convocatoria**",
         "La autorización del Consejo de Ministros **no implica la aprobación del gasto**. Las facultades pueden **desconcentrarse** por real decreto (10.3)."))}
""", 2)

T.ap("s16", "V.5 Beneficiarios y entidades colaboradoras (Ley 38/2003, arts. 11 a 14)", f"""
{unidad("5.1 Beneficiario y entidad colaboradora (arts. 11.1 y 12.1)",
  lit("LGS", "Artículo 11", ["la persona que haya de realizar la actividad que fundamentó su otorgamiento o que se encuentre en la situación que legitima su concesión"], solo=[1]),
  lit("LGS", "Artículo 12", ["actuando en nombre y por cuenta del órgano concedente", "en ningún caso, se considerarán integrantes de su patrimonio"], solo=[1]),
  fichab("Quién recibe la subvención y quién colabora en su gestión",
         ["**Beneficiario**: quien realiza la actividad o está en la situación que legitima la concesión", "**Entidad colaboradora**: actúa **en nombre y por cuenta** del órgano concedente"],
         ["La entidad colaboradora **entrega y distribuye** los fondos o colabora en la gestión sin entrega previa", "Pueden ser beneficiarios agrupaciones **sin personalidad** si las bases lo prevén (11.3)"],
         "—",
         "Los fondos que maneja la entidad colaboradora **nunca** integran su patrimonio."))}

{unidad("5.2 Prohibiciones para ser beneficiario (art. 13.2)",
  lit("LGS", "Artículo 13", ["pérdida de la posibilidad de obtener subvenciones o ayudas públicas", "No hallarse al corriente en el cumplimiento de las obligaciones tributarias o frente a la Seguridad Social", "como paraíso fiscal", "No hallarse al corriente de pago de obligaciones por reintegro de subvenciones"], solo=[2, 3, 4, 5, 6, 7, 8, 9, 10]),
  fichab("Quién no puede ser beneficiario ni entidad colaboradora",
         "—",
         ["a) Condenados por sentencia firme (pérdida de subvenciones, prevaricación, cohecho, malversación, tráfico de influencias, fraudes, delitos urbanísticos)", "b) Concurso, insolvencia, inhabilitación", "c) Resolución firme de un contrato con la Administración por causa de la que fueron culpables", "d) Incompatibilidades de altos cargos y personal, o cargos electivos", "e) No estar al corriente con **Hacienda** o la **Seguridad Social**", "f) Residencia fiscal en **paraíso fiscal**", "g) No estar al corriente en el pago de **reintegros**", "h) Sancionados con la pérdida de la posibilidad de obtener subvenciones"],
         "Prohibiciones de a) y h): alcance según la sentencia o resolución; si no deriva de sentencia, **máximo cinco años** (13.5)",
         "Las prohibiciones operan **salvo** que la normativa reguladora las exceptúe por la naturaleza de la subvención."))}

{unidad("5.3 Obligaciones del beneficiario (art. 14.1)",
  lit("LGS", "Artículo 14", ["Cumplir el objetivo", "Justificar ante el órgano concedente", "Someterse a las actuaciones de comprobación", "Comunicar al órgano concedente o la entidad colaboradora la obtención de otras subvenciones", "Conservar los documentos justificativos", "Proceder al reintegro"], solo=list(range(1, 12))),
  fichab("Qué debe hacer quien recibe una subvención",
         "El **beneficiario**",
         ["Cumplir el objetivo o realizar la actividad", "**Justificar** el cumplimiento", "Someterse a la **comprobación** y al **control financiero**", "**Comunicar otras subvenciones** que financien la misma actividad", "Acreditar estar al corriente con Hacienda y Seguridad Social **antes de la propuesta de resolución**", "Llevar contabilidad y **conservar** justificantes", "Medidas de **difusión**", "**Reintegrar** en los casos del art. 37"],
         f"Comunicación de otras ayudas: {c('LGS', 'Artículo 14', 'tan pronto como se conozca y, en todo caso, con anterioridad a la justificación')}",
         "Incumplir la **comunicación de otras ayudas** es infracción **grave** (art. 57 a, → VI.4.3)."))}
""", 2)

T.ap("s17", "V.6 Bases reguladoras y Base de Datos Nacional de Subvenciones (Ley 38/2003, arts. 17 y 20)", f"""
{unidad("6.1 Bases reguladoras (art. 17.1 a 3)",
  lit("LGS", "Artículo 17", ["los ministros correspondientes establecerán las oportunas bases reguladoras", "se aprobarán por orden ministerial", "previo informe de los servicios jurídicos y de la Intervención Delegada correspondiente", "a través de una ordenanza general de subvenciones o mediante una ordenanza específica"], solo=[1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 19]),
  fichab("Norma que fija las reglas de cada subvención",
         ["AGE: los **ministros** correspondientes, por **orden ministerial**", "Corporaciones locales: en el marco de las bases de ejecución del presupuesto, por **ordenanza general** o **específica**"],
         ["Procedimiento del art. 24 de la Ley 50/1997, con informe de los **servicios jurídicos** y de la **Intervención Delegada**", "Publicación en el **BOE**", "Contenido mínimo (17.3): objeto, requisitos de los beneficiarios, procedimiento, criterios objetivos, cuantía, órganos, justificación, criterios de graduación de incumplimientos, entre otros"],
         "—",
         "En la AGE, **orden ministerial** (no real decreto); no hace falta si las normas sectoriales ya incluyen las bases con el alcance del 17.3."))}

{unidad("6.2 La Base de Datos Nacional de Subvenciones (art. 20.1, 3 y 8)",
  lit("LGS", "Artículo 20", ["promover la transparencia", "La Intervención General de la Administración del Estado es el órgano responsable de la administración y custodia de la BDNS", "Sistema Nacional de Publicidad de Subvenciones y Ayudas Públicas"], solo=[1, 5, 27, 28, 29, 30, 31]),
  fichab("Registro y sistema de publicidad de las subvenciones",
         "Administra y custodia la **Intervención General de la Administración del Estado** (IGAE)",
         ["Finalidades: **transparencia**, planificación, mejora de la gestión y lucha contra el **fraude**", "Opera como **Sistema Nacional de Publicidad de Subvenciones y Ayudas Públicas**", "La IGAE publica en su web convocatorias y subvenciones concedidas"],
         "Las prohibiciones de los apartados a) y h) del art. 13.2 permanecen inscritas hasta **10 años** desde el fin del plazo de prohibición (20.2)",
         "Responsable: la **IGAE**, no el Ministerio de Hacienda ni la AIReF (pregunta oficial L 53, → Cierre 1). No comunicar la información a la BDNS es infracción **grave** (art. 57 f)."))}

{resumen([
  "Ayudas de Estado: **incompatibles** si falsean la competencia y afectan al comercio entre Estados (107.1 TFUE); se notifican y **no se ejecutan** antes de la decisión de la Comisión (108.3).",
  "Subvención: disposición **dineraria**, **sin contraprestación directa**, **afectada** a un fin y con objeto de **fomento** (art. 2.1). No lo son beneficios fiscales, crédito oficial ni prestaciones de la Seguridad Social (2.4).",
  "Régimen: Ley 38/2003 y desarrollo → derecho administrativo → **derecho privado** (art. 5); con fondos de la UE, normas comunitarias y la Ley 38/2003 **supletoria** (art. 6).",
  "Antes de conceder: **plan estratégico**, **bases reguladoras** (orden ministerial en la AGE), crédito, fiscalización y aprobación del gasto; > **12 M€**, Consejo de Ministros.",
  "BDNS: la administra y custodia la **IGAE**."],
  "Siguiente: VI. ¿Cómo se conceden, justifican, reintegran y sancionan las subvenciones?")}
""", 2)

# =============================================================================
T.ap("bVI", "VI. ¿Cómo se conceden, justifican, reintegran y sancionan las subvenciones?", donde(
  "Sexta pregunta. Ya sabemos qué es una subvención y qué hace falta antes de otorgarla. Ahora, su **vida**: cómo se **concede** (concurrencia competitiva o concesión directa), cómo se **justifica** y se **paga**, cuándo se **reintegra** y qué conductas se **sancionan**.",
  ["1 Procedimientos de concesión (Ley 38/2003, arts. 22 y 23; RD 887/2006, art. 65)", "2 Justificación y pago (arts. 30 y 34; RD 887/2006, art. 69)", "3 Invalidez y reintegro (arts. 36 a 39 y 42)", "4 Infracciones y sanciones (arts. 52, 54, 56 a 59 y 65)"]))

T.ap("s18", "VI.1 Procedimientos de concesión (Ley 38/2003, arts. 22 y 23; RD 887/2006, art. 65)", f"""
{unidad("1.1 Concurrencia competitiva y concesión directa (art. 22)",
  lit("LGS", "Artículo 22", ["se tramitará en régimen de concurrencia competitiva", "mediante la comparación de las solicitudes presentadas", "por un órgano colegiado a través del órgano instructor", "procederá al prorrateo", "Podrán concederse de forma directa las siguientes subvenciones", "previstas nominativamente en los Presupuestos Generales del Estado", "por una norma de rango legal", "Con carácter excepcional"]),
  fichab("Los dos procedimientos de concesión",
         "Propone un **órgano colegiado** a través del **órgano instructor**; resuelve el órgano concedente",
         ["::Ordinario: **concurrencia competitiva** (22.1): comparación de solicitudes, prelación según criterios de las bases y la convocatoria y adjudicación dentro del crédito", "Prorrateo del importe global, **excepcionalmente** y si lo prevén las bases", "::Concesión **directa** (22.2):", "a) **Nominativas** en los Presupuestos", "b) Impuestas por una norma de **rango legal**", "c) **Excepcionalmente**, por razones de interés público, social, económico o humanitario que dificulten la convocatoria pública"],
         "Nunca por cuantía superior a la de la convocatoria (22.3)",
         "Las **nominativas** se conceden de forma **directa** (pregunta oficial P 61, → Cierre 1). Nominativa = al menos **dotación** y **beneficiario** determinados en los estados de gasto."))}

{unidad("1.2 Iniciación de oficio y convocatoria (art. 23.1 y 2)",
  lit("LGS", "Artículo 23", ["se inicia siempre de oficio", "mediante convocatoria aprobada por el órgano competente", "La convocatoria deberá publicarse en la BDNS"], solo=list(range(1, 16))),
  fichab("Cómo empieza el procedimiento de concurrencia competitiva",
         "El **órgano competente** aprueba la convocatoria",
         ["Siempre **de oficio**, mediante **convocatoria**", "Publicación en la **BDNS** y extracto en el **BOE** (art. 20.8)", "Contenido mínimo: bases, créditos y cuantía máxima, objeto, requisitos, órganos, plazos, criterios de valoración, etc. (23.2 a a m)"],
         "Subsanación de solicitudes: plazo máximo e improrrogable de **10 días** (23.5)",
         "Nunca a instancia de parte en concurrencia competitiva: **siempre de oficio**."))}

{unidad("1.3 Las subvenciones nominativas (RD 887/2006, art. 65.1 y 3)",
  lit("RD887", "a65", ["cuyo objeto, dotación presupuestaria y beneficiario aparecen determinados expresamente en el estado de gastos del presupuesto", "terminará con la resolución de concesión o el convenio", "tendrá el carácter de bases reguladoras"], solo=[1, 3, 4]),
  fichab("Concesión directa de las subvenciones nominativas",
         "Inicia el **centro gestor** del crédito, de oficio, o el interesado",
         ["Termina con **resolución de concesión** o **convenio**", "La resolución o el convenio tienen el carácter de **bases reguladoras**"],
         "—",
         "El Reglamento exige que figuren en el estado de gastos el **objeto**, la **dotación** y el **beneficiario**; la Ley (22.2 a) habla de «al menos su dotación presupuestaria y beneficiario». El convenio es el instrumento **habitual** (Ley, art. 28.1)."))}
""", 2)

T.ap("s19", "VI.2 Justificación y pago (Ley 38/2003, arts. 30 y 34; RD 887/2006, art. 69)", f"""
{unidad("2.1 La justificación (art. 30.1 a 3 y 8)",
  lit("LGS", "Artículo 30", ["cuenta justificativa del gasto realizado", "por módulos", "estados contables", "constituye un acto obligatorio del beneficiario", "en el plazo de tres meses desde la finalización del plazo para la realización de la actividad", "llevará aparejado el reintegro"], solo=[1, 2, 3, 4, 11]),
  lit("RD887", "a69", ["Cuenta justificativa", "Acreditación por módulos", "Presentación de estados contables"]),
  fichab("Cómo acredita el beneficiario que cumplió",
         "El **beneficiario** o la **entidad colaboradora** (acto obligatorio)",
         ["::Tres modalidades (Ley, 30.1; Reglamento, art. 69):", "**Cuenta justificativa**", "**Módulos**", "**Estados contables**", "Gastos acreditados con **facturas** y documentos de valor probatorio equivalente (30.3)"],
         f"Si las bases no dicen nada, {c('LGS', 'Artículo 30', 'como máximo, en el plazo de tres meses desde la finalización del plazo para la realización de la actividad')}",
         "No justificar o justificar de forma insuficiente → **reintegro** (30.8). Subvenciones por **situación** del perceptor: basta acreditar la situación **antes** de la concesión (30.7)."))}

{unidad("2.2 Aprobación del gasto y pago (art. 34.1 a 4)",
  lit("LGS", "Artículo 34", ["Con carácter previo a la convocatoria de la subvención o a la concesión directa", "conllevará el compromiso del gasto correspondiente", "El pago de la subvención se realizará previa justificación", "pagos a cuenta", "pagos anticipados"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Cuándo se paga",
         "Órgano concedente",
         ["Aprobación del gasto **antes** de la convocatoria o de la concesión directa", "La resolución de concesión conlleva el **compromiso** del gasto", "Regla: pago **previa justificación**", "Si lo prevé la normativa: **pagos a cuenta** (según el ritmo de ejecución) y **pagos anticipados** (antes de justificar)"],
         "—",
         "No se paga si el beneficiario no está al corriente con Hacienda y Seguridad Social o es **deudor por reintegro** (34.5)."))}
""", 2)

T.ap("s20", "VI.3 Invalidez y reintegro (Ley 38/2003, arts. 36 a 39 y 42)", f"""
{unidad("3.1 Invalidez de la resolución de concesión (art. 36)",
  lit("LGS", "Artículo 36", ["La carencia o insuficiencia de crédito", "llevará consigo la obligación de devolver las cantidades percibidas", "No procederá la revisión de oficio"]),
  fichab("Cuándo es nula o anulable la concesión",
         "El **órgano concedente** revisa de oficio o declara la lesividad",
         ["**Nulidad**: causas generales de nulidad (hoy, art. 47 Ley 39/2015) y **carencia o insuficiencia de crédito**", "**Anulabilidad**: las demás infracciones del ordenamiento", "Efecto: **devolver** lo percibido"],
         "—",
         f"La falta de crédito es causa de **nulidad**, no de anulabilidad. Las remisiones a la Ley 30/1992 {c('L39', 'Disposición derogatoria única', 'deberán entenderse efectuadas a las disposiciones de esta Ley que regulan la misma materia')} (Ley 39/2015). No hay revisión de oficio si concurre causa de **reintegro** (36.5)."))}

{unidad("3.2 Causas de reintegro (art. 37.1)",
  lit("LGS", "Artículo 37", ["la exigencia del interés de demora correspondiente desde el momento del pago de la subvención", "falseando las condiciones requeridas", "Incumplimiento total o parcial del objetivo", "Incumplimiento de la obligación de justificación o la justificación insuficiente", "Resistencia, excusa, obstrucción o negativa"], solo=list(range(1, 11))),
  fichab("Cuándo hay que devolver la subvención",
         "El beneficiario o la entidad colaboradora",
         ["a) Obtención **falseando** u ocultando condiciones", "b) **Incumplimiento** del objetivo, actividad, proyecto o comportamiento", "c) Falta de **justificación** o justificación insuficiente", "d) Falta de medidas de **difusión**", "e) **Resistencia u obstrucción** al control", "f) y g) Incumplimiento de obligaciones y compromisos", "h) Decisión europea que obligue al reintegro", "i) Otros supuestos de la normativa reguladora"],
         "Se devuelve lo percibido **más el interés de demora** desde el **pago** hasta que se acuerda el reintegro (o el ingreso, si es anterior)",
         "Si el cumplimiento se **aproxima significativamente** al total, se aplica la **graduación** de las bases (37.2 y 17.3 n)."))}

{unidad("3.3 Naturaleza del reintegro e interés de demora (art. 38)",
  lit("LGS", "Artículo 38", ["ingresos de derecho público", "el interés legal del dinero incrementado en un 25 por ciento", "tendrán siempre carácter administrativo"]),
  fichab("Régimen de las cantidades a reintegrar",
         "—",
         ["Son **ingresos de derecho público** (cobranza según la Ley General Presupuestaria)", "Procedimientos de reintegro: **siempre administrativos**"],
         f"Interés de demora: {c('LGS', 'Artículo 38', 'el interés legal del dinero incrementado en un 25 por ciento')}, salvo que la Ley de Presupuestos fije otro",
         "Interés legal **+ 25 %** (no el interés de demora tributario)."))}

{unidad("3.4 Prescripción del reintegro (art. 39.1 y 2)",
  lit("LGS", "Artículo 39", ["Prescribirá a los cuatro años", "Desde el momento en que venció el plazo para presentar la justificación"], solo=[1, 2, 3, 4, 5]),
  fichab("Plazo para exigir el reintegro",
         "La **Administración** (derecho a reconocer o liquidar el reintegro)",
         ["::Cómputo desde:", "El vencimiento del plazo de **justificación**", "La **concesión**, si la subvención se da por la situación del perceptor (art. 30.7)", "El vencimiento del período de mantenimiento de condiciones u obligaciones"],
         "**Cuatro años**; se interrumpe por actuaciones de la Administración con conocimiento formal del beneficiario, recursos, actuaciones penales o actuaciones del beneficiario (39.3)",
         "Cuatro años desde que **venció el plazo para justificar** (no desde el pago)."))}

{unidad("3.5 Procedimiento de reintegro (art. 42.2 a 5)",
  lit("LGS", "Artículo 42", ["se iniciará de oficio", "el derecho del interesado a la audiencia", "será de 12 meses desde la fecha del acuerdo de iniciación", "se producirá la caducidad del procedimiento", "pondrá fin a la vía administrativa"], solo=[2, 3, 4, 5, 6]),
  fichab("Cómo se exige el reintegro",
         "Órgano competente, de oficio (propia iniciativa, orden superior, petición razonada, denuncia o informe de control financiero de la IGAE)",
         ["Audiencia del interesado **en todo caso**", "La resolución **pone fin a la vía administrativa**"],
         "Plazo máximo para resolver y notificar: **12 meses** desde el acuerdo de iniciación; si vence, **caducidad**",
         "**12 meses** desde la **iniciación**. Tras la caducidad, las actuaciones realizadas **no interrumpen** la prescripción."))}
""", 2)

T.ap("s21", "VI.4 Infracciones y sanciones (Ley 38/2003, arts. 52, 54, 56 a 59 y 65)", f"""
{unidad("4.1 Concepto de infracción y exención de responsabilidad (arts. 52 y 54)",
  lit("LGS", "Artículo 52", ["incluso a título de simple negligencia"]),
  lit("LGS", "Artículo 54", ["quienes carezcan de capacidad de obrar", "Cuando concurra fuerza mayor", "para quienes hubieran salvado su voto o no hubieran asistido a la reunión"]),
  fichab("Qué es infracción y cuándo no hay responsabilidad",
         "Responsables: beneficiarios, entidades colaboradoras y demás sujetos del art. 53",
         ["Acciones y omisiones **tipificadas** en la ley, sancionables **incluso por simple negligencia**", "::Exención (54):", "Falta de **capacidad de obrar**", "**Fuerza mayor**", "Decisión **colectiva**, para quien **salvó su voto** o **no asistió**"],
         "—",
         "Basta la **simple negligencia**. Exime la **fuerza mayor** (no el «error de derecho», ni el reintegro voluntario, ni haber votado a favor: pregunta oficial P 65, → Cierre 1)."))}

{unidad("4.2 Infracciones leves (art. 56)",
  lit("LGS", "Artículo 56", ["La presentación fuera de plazo de las cuentas justificativas", "La presentación de cuentas justificativas inexactas o incompletas", "El incumplimiento de la obligación de llevar o conservar la contabilidad", "La resistencia, obstrucción, excusa o negativa a las actuaciones de control financiero"], solo=[1, 2, 3, 4, 5, 6, 7, 10, 12]),
  fichab("Infracciones leves",
         "—",
         ["Cláusula **residual**: incumplimientos que no sean graves o muy graves", "Cuentas justificativas **fuera de plazo** o **inexactas o incompletas**", "Incumplimientos **contables o registrales** (incluido no llevar o conservar la contabilidad)", "No conservar justificantes", "**Resistencia u obstrucción** al control financiero"],
         "—",
         "La resistencia u obstrucción al **control financiero** es **leve** (56 g); la resistencia a las actuaciones de control **que impida verificar el empleo de los fondos** se tipifica como **muy grave** (58 c)."))}

{unidad("4.3 Infracciones graves (art. 57)",
  lit("LGS", "Artículo 57", ["El incumplimiento de la obligación de comunicar al órgano concedente", "alterando sustancialmente los fines", "La falta de justificación del empleo dado a los fondos recibidos una vez transcurrido el plazo establecido para su presentación", "La falta de suministro de información"]),
  fichab("Infracciones graves",
         "—",
         ["a) No **comunicar otras ayudas** para la misma finalidad", "b) Incumplir condiciones **alterando sustancialmente los fines**", "c) **Falta de justificación** una vez transcurrido el plazo", "d) y e) Conductas de las **entidades colaboradoras**", "f) No suministrar información a la **BDNS**"],
         "—",
         "Presentar la cuenta **fuera de plazo** = **leve**; **no** justificar una vez pasado el plazo = **grave** (pregunta oficial P 63, → Cierre 1)."))}

{unidad("4.4 Infracciones muy graves (art. 58)",
  lit("LGS", "Artículo 58", ["La obtención de una subvención falseando las condiciones", "La no aplicación, en todo o en parte, de las cantidades recibidas a los fines", "cuando de ello se derive la imposibilidad de verificar el empleo dado a los fondos percibidos"], solo=[1, 2, 3, 4, 5]),
  fichab("Infracciones muy graves",
         "—",
         ["a) **Obtener** la subvención **falseando** u ocultando condiciones", "b) **No aplicar** los fondos a los fines", "c) Resistencia al control **que impida verificar** el empleo de los fondos", "d) Entidad colaboradora que **no entrega** los fondos a los beneficiarios"],
         "—",
         "Falsear para **obtener** la subvención = **muy grave** (y también causa de reintegro, 37.1 a)."))}

{unidad("4.5 Sanciones (art. 59)",
  lit("LGS", "Artículo 59", ["multa fija o proporcional", "entre 75 y 6.000 euros", "del tanto al triple", "será independiente de la obligación de reintegro", "Pérdida durante un plazo de hasta cinco años", "Prohibición durante un plazo de hasta cinco años para contratar"]),
  fichab("Cómo se sancionan",
         "—",
         ["**Pecuniarias**: multa **fija** (75 a 6.000 €) o **proporcional** (del **tanto al triple** de lo indebidamente obtenido, aplicado o no justificado)", "**No pecuniarias** (solo graves o muy graves), hasta **cinco años**: pérdida de la posibilidad de obtener subvenciones, de ser entidad colaboradora o de contratar con las Administraciones"],
         "No pecuniarias: hasta **cinco años**",
         "La multa es **independiente** del reintegro: se pueden exigir las dos cosas."))}

{unidad("4.6 Prescripción de infracciones y sanciones (art. 65)",
  lit("LGS", "Artículo 65", ["en el plazo de cuatro años a contar desde el día en que la infracción se hubiera cometido", "desde el día siguiente a aquel en que hubiera adquirido firmeza la resolución", "se aplicará de oficio"], solo=[1, 2, 4]),
  fichab("Prescripción",
         "—",
         ["Infracciones: desde que se **cometieron**", "Sanciones: desde el día siguiente a la **firmeza** de la resolución", "Se aplica **de oficio**"],
         "**Cuatro años** las infracciones y **cuatro años** las sanciones (igual que el reintegro, art. 39)",
         "En subvenciones **todo prescribe a los cuatro años**: reintegro, infracciones y sanciones."))}

{resumen([
  "Concesión: **concurrencia competitiva** (ordinaria; propone un órgano colegiado) o **directa** (nominativas, impuestas por norma con rango de ley, excepcionales) (art. 22). Se inicia **siempre de oficio**, por **convocatoria** (art. 23).",
  "Justificación: cuenta justificativa, **módulos** o **estados contables**; sin previsión, **tres meses** (art. 30). Pago **previa justificación**, salvo pagos a cuenta o anticipados previstos (art. 34).",
  "Reintegro: lo percibido + interés de demora (interés legal **+ 25 %**); prescribe a los **cuatro años**; procedimiento de **12 meses** que pone fin a la vía administrativa (arts. 37 a 39 y 42).",
  "Infracciones: **simple negligencia**; exime la **fuerza mayor**; cuenta fuera de plazo = **leve**; no justificar = **grave**; falsear para obtener = **muy grave**; multas de **75 a 6.000 €** o del **tanto al triple**; prescripción de **cuatro años**."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_L53 = examen("L", 53, {
  "a": "El Ministerio de Hacienda no aparece en el art. 20.3: el órgano responsable es la Intervención General, no el Ministerio.",
  "b": f"Literal del art. 20.3: {c('LGS', 'Artículo 20', 'La Intervención General de la Administración del Estado es el órgano responsable de la administración y custodia de la BDNS')}.",
  "c": "El Ministerio de Economía no tiene ninguna función sobre la BDNS en el art. 20; el dato cambiado es el órgano.",
  "d": "La AIReF no aparece en la Ley 38/2003 como responsable de la BDNS; el art. 20.3 atribuye la administración y custodia a la IGAE."},
  [("Intervención General de la Administración del Estado", "LGS", "Artículo 20", "La Intervención General de la Administración del Estado es el órgano responsable de la administración y custodia de la BDNS")])
EX_P61 = examen("P", 61, {
  "a": f"La concurrencia competitiva es el procedimiento **ordinario** (art. 22.1: {c('LGS', 'Artículo 22', 'El procedimiento ordinario de concesión de subvenciones se tramitará en régimen de concurrencia competitiva')}), no el de las nominativas.",
  "b": "La «evaluación individualizada» no es un procedimiento de concesión de la Ley 38/2003: el art. 22 solo conoce la concurrencia competitiva y la concesión directa.",
  "c": "La subasta pública no es un procedimiento de concesión de subvenciones en el art. 22.",
  "d": f"Literal del art. 22.2 a): {c('LGS', 'Artículo 22', 'Podrán concederse de forma directa las siguientes subvenciones: a) Las previstas nominativamente en los Presupuestos Generales del Estado')}."},
  [("directa", "LGS", "Artículo 22", "Podrán concederse de forma directa las siguientes subvenciones")])
EX_P63 = examen("P", 63, {
  "a": f"Es infracción **leve**: art. 56 g) {c('LGS', 'Artículo 56', 'La resistencia, obstrucción, excusa o negativa a las actuaciones de control financiero')} (la resistencia que impida verificar el empleo de los fondos se tipifica como muy grave en el art. 58 c).",
  "b": f"Es infracción **leve**: art. 56 b) {c('LGS', 'Artículo 56', 'La presentación de cuentas justificativas inexactas o incompletas')}.",
  "c": f"Literal del art. 57 c), infracción **grave**: {c('LGS', 'Artículo 57', 'La falta de justificación del empleo dado a los fondos recibidos una vez transcurrido el plazo establecido para su presentación')}.",
  "d": f"Es infracción **leve**: art. 56 d) 2.º {c('LGS', 'Artículo 56', 'El incumplimiento de la obligación de llevar o conservar la contabilidad')}."},
  [("La falta de justificación del empleo dado a los fondos recibidos una vez transcurrido el plazo establecido para su presentación", "LGS", "Artículo 57", "La falta de justificación del empleo dado a los fondos recibidos una vez transcurrido el plazo establecido para su presentación")])
EX_P64 = examen("P", 64, {
  "a": f"No se rigen por la Ley 38/2003 y el derecho privado: el art. 6.1 dice que {c('LGS', 'Artículo 6', 'se regirán por las normas comunitarias aplicables en cada caso')}.",
  "b": f"Literal del art. 6: {c('LGS', 'Artículo 6', 'se regirán por las normas comunitarias aplicables en cada caso y por las normas nacionales de desarrollo o transposición de aquéllas')}, y los procedimientos de la ley {c('LGS', 'Artículo 6', 'tendrán carácter supletorio respecto de las normas de aplicación directa')}.",
  "c": f"Añade «**exclusivamente**» y deja fuera las normas comunitarias: el art. 6.1 dice que {c('LGS', 'Artículo 6', 'se regirán por las normas comunitarias aplicables en cada caso y por las normas nacionales de desarrollo o transposición de aquéllas')}.",
  "d": f"Invierte la relación: la ley no es preferente, sino que {c('LGS', 'Artículo 6', 'tendrán carácter supletorio respecto de las normas de aplicación directa')}."},
  [("normas comunitarias aplicables", "LGS", "Artículo 6", "se regirán por las normas comunitarias aplicables en cada caso"),
   ("normas de aplicación directa", "LGS", "Artículo 6", "tendrán carácter supletorio respecto de las normas de aplicación directa")])
EX_P65 = examen("P", 65, {
  "a": "El «error de derecho excusable» no figura entre las causas de exención del art. 54 (capacidad de obrar, fuerza mayor y decisión colectiva).",
  "b": f"Literal del art. 54 b): {c('LGS', 'Artículo 54', 'Cuando concurra fuerza mayor')}.",
  "c": "El reintegro voluntario no exime de responsabilidad en el art. 54; además, la infracción es sancionable incluso por simple negligencia (art. 52).",
  "d": f"Cambia el dato: en la decisión colectiva solo quedan exentos {c('LGS', 'Artículo 54', 'quienes hubieran salvado su voto o no hubieran asistido a la reunión')}, no quien votó a favor."},
  [("fuerza mayor", "LGS", "Artículo 54", "Cuando concurra fuerza mayor")])

T.ap("s22", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **cinco** preguntas de este tema, todas sobre la **Ley General de Subvenciones** (una en el turno libre y cuatro en promoción interna). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-L 2025, pregunta 53 · Base de Datos Nacional de Subvenciones (→ V.6.2)", EX_L53,
  "### GACE-P 2025, pregunta 61 · Subvenciones nominativas (→ VI.1.1)", EX_P61,
  "### GACE-P 2025, pregunta 63 · Infracciones graves (→ VI.4.3)", EX_P63,
  "### GACE-P 2025, pregunta 64 · Subvenciones con fondos de la UE (→ V.3.3)", EX_P64,
  "### GACE-P 2025, pregunta 65 · Exención de responsabilidad (→ VI.4.1)", EX_P65,
  "### Cómo se pregunta",
  "!> Las preguntas de subvenciones citan **el artículo** en el enunciado y juegan con **otros datos del mismo artículo o del de al lado**: infracciones leves frente a graves (arts. 56 y 57), concurrencia competitiva frente a concesión directa (art. 22), órganos parecidos (IGAE, Ministerio de Hacienda, AIReF). Saber **en qué artículo** está cada dato resuelve la pregunta.",
]))

T.ap("s23", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Procedimientos y formas | Principios (103.1 CE; Ley 40/2015, art. 3); procedimiento común (Ley 39/2015, art. 1); terminación convencional (art. 86); convenios (Ley 40/2015, art. 47) | Convenios: **nunca** prestaciones propias de los contratos |
| II. Intervención | Proporcionalidad y medida menos restrictiva (Ley 40/2015, art. 4); autorización excepcional (Ley 17/2009, art. 5); declaración responsable y comunicación (Ley 39/2015, art. 69); LRBRL, arts. 84 y 84 bis | Efectos **desde la presentación**; nunca las dos acumulativamente |
| III. Arbitral | Sustitución de la alzada por arbitraje, por **ley** (Ley 39/2015, art. 112.2); Sistema Arbitral del Consumo (TRLGDCU, arts. 57 y 58) | Excluidos **intoxicación, lesión o muerte** e indicios de delito |
| IV. Servicio público | Reserva **mediante ley** (128.2 CE); servicios reservados a los entes locales (LRBRL, art. 86); gestión directa e indirecta (art. 85); concesión de servicios (LCSP) | EPE y sociedad mercantil solo con **memoria justificativa** |
| V. Fomento y subvenciones | Ayudas de Estado (107 y 108 TFUE); concepto (art. 2); régimen (arts. 5 y 6); requisitos (arts. 8 a 10); beneficiarios (arts. 11 a 14); bases y BDNS (arts. 17 y 20) | BDNS: la **IGAE**; fondos UE: la ley es **supletoria** |
| VI. Concesión, reintegro y sanciones | Concurrencia competitiva y directa (art. 22); justificación (art. 30); invalidez y reintegro (arts. 36 a 39 y 42); infracciones y sanciones (arts. 52, 54, 56 a 59 y 65) | Nominativas: **directa**; no justificar: **grave**; exime la **fuerza mayor** |

?> **Trampas frecuentes:** «las declaraciones responsables producen efectos **desde que la Administración las comprueba**» (desde la **presentación**); «los servicios reservados a los entes locales pueden ampliarse **por ordenanza**» (por **Ley** del Estado o de las CC. AA.); «la concesión de servicios puede incluir el **ejercicio de autoridad**» (nunca); «la subvención **nominativa** se concede en **concurrencia competitiva**» (es **directa**); «la presentación **fuera de plazo** de la cuenta justificativa es **grave**» (es **leve**; lo grave es **no justificar**); «el interés de demora es el **legal**» (es el legal **incrementado en un 25 %**); «el reintegro prescribe a los **cinco** años» (son **cuatro**).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
Q = T.q
Q("L40", "Artículo 4", "Intervención", "Según el artículo 4.1 de la Ley 40/2015, las Administraciones Públicas que establezcan medidas que limiten el ejercicio de derechos individuales o colectivos deberán:",
  ["Aplicar el principio de proporcionalidad y elegir la medida menos restrictiva.", "Aplicar el principio de eficacia y elegir la medida más eficaz.", "Aplicar el principio de jerarquía y elegir la medida que determine el órgano superior.", "Aplicar el principio de precaución y elegir la medida más protectora."],
  "Art. 4.1 Ley 40/2015.", "deberán aplicar el principio de proporcionalidad y elegir la medida menos restrictiva")
Q("L40", "Artículo 4", "Intervención", "Según el artículo 4.1 de la Ley 40/2015, respecto de las medidas que limiten derechos o exijan requisitos para una actividad, las Administraciones deberán evaluar sus efectos y resultados:",
  ["Periódicamente.", "Solo al año de su aprobación.", "Cada cuatro años, mediante informe al Consejo de Ministros.", "Únicamente cuando lo solicite un interesado."],
  "Art. 4.1 Ley 40/2015: «deberán evaluar periódicamente los efectos y resultados obtenidos».", "deberán evaluar periódicamente los efectos y resultados obtenidos")
Q("L17_2009", "Artículo 5", "Intervención", "Según el artículo 5 de la Ley 17/2009, sobre el libre acceso a las actividades de servicios y su ejercicio, las condiciones que permiten imponer un régimen de autorización habrán de motivarse suficientemente:",
  ["En la ley que establezca dicho régimen.", "En el reglamento que desarrolle la actividad.", "En la resolución que otorgue cada autorización.", "En la ordenanza municipal correspondiente."],
  "Art. 5 Ley 17/2009.", "que habrán de motivarse suficientemente en la ley que establezca dicho régimen")
Q("L17_2009", "Artículo 5", "Intervención", "Según el artículo 5 de la Ley 17/2009, ¿cuál de las siguientes NO es una de las condiciones que deben concurrir para imponer un régimen de autorización a una actividad de servicios?",
  ["Rentabilidad.", "No discriminación.", "Necesidad.", "Proporcionalidad."],
  "Art. 5 Ley 17/2009: no discriminación, necesidad y proporcionalidad.", ["No discriminación", "Necesidad", "Proporcionalidad"])
Q("L39", "Artículo 69", "Intervención", "Según el artículo 69.3 de la Ley 39/2015, las declaraciones responsables y las comunicaciones permitirán el inicio de una actividad:",
  ["Desde el día de su presentación.", "Desde que la Administración compruebe su contenido.", "Transcurrido un mes desde su presentación sin oposición de la Administración.", "Desde su inscripción en el registro correspondiente."],
  "Art. 69.3 Ley 39/2015.", "desde el día de su presentación")
Q("L39", "Artículo 69", "Intervención", "Según el artículo 69.6 de la Ley 39/2015, para iniciar una misma actividad:",
  ["Únicamente será exigible, bien una declaración responsable, bien una comunicación, sin que sea posible exigir ambas acumulativamente.", "Podrán exigirse acumulativamente una declaración responsable y una comunicación.", "Será exigible siempre una declaración responsable y, además, una licencia.", "Será exigible una comunicación previa y, transcurridos quince días, una declaración responsable."],
  "Art. 69.6 Ley 39/2015.", "sin que sea posible la exigencia de ambas acumulativamente")
Q("LRBRL", "Artículo 84", "Intervención", "Según el artículo 84.2 de la Ley 7/1985, Reguladora de las Bases del Régimen Local, la actividad de intervención de las Entidades locales se ajustará, en todo caso, a los principios de:",
  ["Igualdad de trato, necesidad y proporcionalidad con el objetivo que se persigue.", "Eficacia, jerarquía y coordinación.", "Autonomía local, suficiencia financiera y subsidiariedad.", "Legalidad, publicidad y concurrencia."],
  "Art. 84.2 LRBRL.", "igualdad de trato, necesidad y proporcionalidad con el objetivo que se persigue")
Q("LRBRL", "Artículo 84 bis", "Intervención", "Según el artículo 84 bis.1 de la Ley 7/1985, Reguladora de las Bases del Régimen Local, con carácter general, el ejercicio de actividades:",
  ["No se someterá a la obtención de licencia u otro medio de control preventivo.", "Se someterá a la obtención de licencia previa.", "Se someterá a autorización de la Comunidad Autónoma.", "Requerirá siempre declaración responsable y comunicación previa."],
  "Art. 84 bis.1 LRBRL.", "con carácter general, el ejercicio de actividades no se someterá a la obtención de licencia u otro medio de control preventivo")
Q("L39", "Artículo 86", "Procedimientos y formas", "Según el artículo 86.3 de la Ley 39/2015, los acuerdos de terminación convencional que versen sobre materias de la competencia directa del Consejo de Ministros requerirán en todo caso:",
  ["La aprobación expresa del Consejo de Ministros.", "El dictamen previo del Consejo de Estado.", "La autorización de las Cortes Generales.", "El informe de la Abogacía del Estado."],
  "Art. 86.3 Ley 39/2015.", "Requerirán en todo caso la aprobación expresa del Consejo de Ministros")
Q("L40", "Artículo 47", "Procedimientos y formas", "Según el artículo 47.1 de la Ley 40/2015, los convenios:",
  ["No podrán tener por objeto prestaciones propias de los contratos.", "Podrán tener por objeto prestaciones propias de los contratos si su importe no supera el umbral armonizado.", "Solo pueden suscribirse entre Administraciones Públicas.", "Carecen de efectos jurídicos."],
  "Art. 47.1 Ley 40/2015.", "Los convenios no podrán tener por objeto prestaciones propias de los contratos")
Q("L39", "Artículo 112", "Arbitral", "Según el artículo 112.2 de la Ley 39/2015, el recurso de alzada podrá ser sustituido por procedimientos de impugnación, reclamación, conciliación, mediación y arbitraje mediante:",
  ["Ley.", "Real decreto acordado en Consejo de Ministros.", "Orden ministerial.", "Acuerdo del órgano que dictó el acto."],
  "Art. 112.2 Ley 39/2015: «Las leyes podrán sustituir el recurso de alzada».", "Las leyes podrán sustituir el recurso de alzada")
Q("L39", "Artículo 112", "Arbitral", "Según el artículo 112.2 de la Ley 39/2015, los procedimientos que sustituyan al recurso de alzada se sustanciarán ante:",
  ["Órganos colegiados o Comisiones específicas no sometidas a instrucciones jerárquicas.", "El superior jerárquico del órgano que dictó el acto.", "Los Juzgados de lo Contencioso-administrativo.", "El Consejo de Estado."],
  "Art. 112.2 Ley 39/2015.", "ante órganos colegiados o Comisiones específicas no sometidas a instrucciones jerárquicas")
Q("TRLGDCU", "Artículo 57", "Arbitral", "Según el artículo 57.1 del texto refundido de la Ley General para la Defensa de los Consumidores y Usuarios, el Sistema Arbitral del Consumo NO resuelve los conflictos que versen sobre:",
  ["Intoxicación, lesión o muerte.", "Servicios de telecomunicaciones.", "Compraventas a distancia.", "Reparación de vehículos."],
  "Art. 57.1 TRLGDCU.", "siempre que el conflicto no verse sobre intoxicación, lesión o muerte")
Q("TRLGDCU", "Artículo 57", "Arbitral", "Según el artículo 57.4 del texto refundido de la Ley General para la Defensa de los Consumidores y Usuarios, los convenios arbitrales suscritos con un empresario antes de surgir el conflicto:",
  ["No serán vinculantes para los consumidores.", "Serán vinculantes para ambas partes.", "Serán nulos de pleno derecho para ambas partes.", "Solo serán vinculantes si constan en documento público."],
  "Art. 57.4 TRLGDCU.", "No serán vinculantes para los consumidores los convenios arbitrales suscritos con un empresario antes de surgir el conflicto")
Q("CE", "Artículo 128", "Servicio público", "Según el artículo 128.2 de la Constitución, la reserva al sector público de recursos o servicios esenciales podrá hacerse:",
  ["Mediante ley.", "Mediante real decreto.", "Mediante acuerdo del Consejo de Ministros.", "Mediante ordenanza de las Entidades locales."],
  "Art. 128.2 CE.", "Mediante ley se podrá reservar al sector público recursos o servicios esenciales")
Q("LRBRL", "Artículo 86", "Servicio público", "Según el artículo 86.2 de la Ley 7/1985, Reguladora de las Bases del Régimen Local, ¿cuál de las siguientes actividades o servicios esenciales está reservada en favor de las Entidades Locales?",
  ["El transporte público de viajeros.", "El suministro de energía eléctrica.", "La asistencia sanitaria primaria.", "La enseñanza obligatoria."],
  "Art. 86.2 LRBRL: aguas, residuos y transporte público de viajeros.", "transporte público de viajeros")
Q("LRBRL", "Artículo 86", "Servicio público", "Según el artículo 86.2 de la Ley 7/1985, la efectiva ejecución en régimen de monopolio de las actividades reservadas a las Entidades Locales requiere, además del acuerdo de aprobación del pleno de la Corporación:",
  ["La aprobación por el órgano competente de la Comunidad Autónoma.", "La autorización del Consejo de Ministros.", "El informe favorable de la Comisión Nacional de los Mercados y la Competencia.", "La aprobación por ley estatal."],
  "Art. 86.2 LRBRL.", "la aprobación por el órgano competente de la Comunidad Autónoma")
Q("LRBRL", "Artículo 85", "Formas de gestión", "Según el artículo 85.2 de la Ley 7/1985, ¿cuál de las siguientes es una forma de gestión directa de los servicios públicos locales?",
  ["Organismo autónomo local.", "Concesión de servicios.", "Sociedad mercantil de capital mayoritariamente privado.", "Concierto con una entidad privada."],
  "Art. 85.2 A) LRBRL.", "Organismo autónomo local")
Q("LRBRL", "Artículo 85", "Formas de gestión", "Según el artículo 85.2 de la Ley 7/1985, solo podrá hacerse uso de la entidad pública empresarial local y de la sociedad mercantil local cuando quede acreditado mediante memoria justificativa que resultan:",
  ["Más sostenibles y eficientes que la gestión por la propia Entidad Local y el organismo autónomo local.", "Más económicas que la gestión indirecta.", "Necesarias por razones de urgencia.", "Más rentables que la concesión de servicios."],
  "Art. 85.2 LRBRL.", "resultan más sostenibles y eficientes que las formas dispuestas en las letras a) y b)")
Q("LCSP", "Artículo 284", "Formas de gestión", "Según el artículo 284.1 de la Ley 9/2017, de Contratos del Sector Público, en ningún caso podrán prestarse mediante concesión de servicios:",
  ["Los que impliquen ejercicio de la autoridad inherente a los poderes públicos.", "Los que sean susceptibles de explotación económica por particulares.", "Los servicios de titularidad local.", "Los que generen ingresos para el concesionario."],
  "Art. 284.1 LCSP.", "En ningún caso podrán prestarse mediante concesión de servicios los que impliquen ejercicio de la autoridad inherente a los poderes públicos")
Q("LCSP", "Artículo 15", "Formas de gestión", "Según el artículo 15.2 de la Ley 9/2017, el derecho de explotación de los servicios en el contrato de concesión de servicios implicará:",
  ["La transferencia al concesionario del riesgo operacional.", "La transferencia al concesionario de la titularidad del servicio.", "La asunción por la Administración de todo el riesgo económico.", "La exención del concesionario de cualquier riesgo de demanda."],
  "Art. 15.2 LCSP.", "implicará la transferencia al concesionario del riesgo operacional")
Q("TFUE", "Artículo 107", "Ayudas de Estado", "Según el artículo 107.2 del Tratado de Funcionamiento de la Unión Europea, son compatibles con el mercado interior:",
  ["Las ayudas destinadas a reparar los perjuicios causados por desastres naturales o por otros acontecimientos de carácter excepcional.", "Las ayudas que favorezcan a determinadas empresas o producciones.", "Las ayudas que falseen la competencia en los intercambios entre Estados miembros.", "Todas las ayudas otorgadas mediante fondos estatales."],
  "Art. 107.2 b) TFUE.", "las ayudas destinadas a reparar los perjuicios causados por desastres naturales o por otros acontecimientos de carácter excepcional")
Q("LGS", "Artículo 2", "Subvenciones: concepto", "Según el artículo 2.1 de la Ley 38/2003, General de Subvenciones, uno de los requisitos de la subvención es que la entrega se realice:",
  ["Sin contraprestación directa de los beneficiarios.", "Con contraprestación equivalente de los beneficiarios.", "Mediante bienes o servicios, nunca en dinero.", "Siempre a favor de personas privadas."],
  "Art. 2.1 a) Ley 38/2003.", "Que la entrega se realice sin contraprestación directa de los beneficiarios")
Q("LGS", "Artículo 2", "Subvenciones: concepto", "Según el artículo 2.4 de la Ley 38/2003, NO tienen carácter de subvenciones:",
  ["Los beneficios fiscales y beneficios en la cotización a la Seguridad Social.", "Las ayudas a la realización de proyectos de investigación.", "Las ayudas a asociaciones para actividades de interés social.", "Las ayudas concedidas en régimen de concurrencia competitiva a empresas."],
  "Art. 2.4 g) Ley 38/2003.", "Los beneficios fiscales y beneficios en la cotización a la Seguridad Social")
Q("LGS", "Artículo 4", "Subvenciones: concepto", "Según el artículo 4 de la Ley 38/2003, quedan excluidos del ámbito de aplicación de la ley:",
  ["Los premios que se otorguen sin la previa solicitud del beneficiario.", "Los premios que se otorguen previa solicitud del beneficiario.", "Las subvenciones nominativas.", "Las subvenciones de las Entidades locales."],
  "Art. 4 a) Ley 38/2003.", "Los premios que se otorguen sin la previa solicitud del beneficiario")
Q("LGS", "Artículo 5", "Subvenciones: régimen", "Según el artículo 5.1 de la Ley 38/2003, las subvenciones se regirán por esta ley y sus disposiciones de desarrollo, las restantes normas de derecho administrativo y, en su defecto:",
  ["Por las normas de derecho privado.", "Por la normativa de la Unión Europea.", "Por la Ley General Presupuestaria.", "Por las bases de ejecución del presupuesto."],
  "Art. 5.1 Ley 38/2003.", "en su defecto, se aplicarán las normas de derecho privado")
Q("LGS", "Artículo 8", "Subvenciones: régimen", "Según el artículo 8.1 de la Ley 38/2003, con carácter previo al establecimiento de subvenciones, los órganos que las propongan deberán concretar sus objetivos y efectos, plazo, costes previsibles y fuentes de financiación en:",
  ["Un plan estratégico de subvenciones.", "Una memoria de análisis de impacto normativo.", "Un programa anual normativo.", "Un plan de control financiero."],
  "Art. 8.1 Ley 38/2003.", "deberán concretar en un plan estratégico de subvenciones")
Q("LGS", "Artículo 10", "Subvenciones: régimen", "Según el artículo 10.2 de la Ley 38/2003, la concesión de subvenciones de cuantía superior a 12 millones de euros requerirá:",
  ["La previa autorización del Consejo de Ministros.", "El previo dictamen del Consejo de Estado.", "La previa autorización de las Cortes Generales.", "El previo informe de la Intervención General de la Administración del Estado."],
  "Art. 10.2 Ley 38/2003.", "de cuantía superior a 12 millones de euros requerirá la previa autorización del Consejo de Ministros")
Q("LGS", "Artículo 17", "Subvenciones: régimen", "Según el artículo 17.1 de la Ley 38/2003, en el ámbito de la Administración General del Estado las bases reguladoras de la concesión de subvenciones se aprobarán por:",
  ["Orden ministerial.", "Real decreto.", "Resolución del Secretario de Estado.", "Acuerdo del Consejo de Ministros."],
  "Art. 17.1 Ley 38/2003.", "Las citadas bases se aprobarán por orden ministerial")
Q("LGS", "Artículo 13", "Beneficiarios", "Según el artículo 13.2 de la Ley 38/2003, no podrán obtener la condición de beneficiario quienes:",
  ["Tengan la residencia fiscal en un país o territorio calificado reglamentariamente como paraíso fiscal.", "Tengan su domicilio social en otro Estado miembro de la Unión Europea.", "Hayan recibido otra subvención para la misma finalidad.", "Sean personas jurídicas sin ánimo de lucro."],
  "Art. 13.2 f) Ley 38/2003.", "Tener la residencia fiscal en un país o territorio calificado reglamentariamente como paraíso fiscal")
Q("LGS", "Artículo 14", "Beneficiarios", "Según el artículo 14.1 d) de la Ley 38/2003, la comunicación al órgano concedente de la obtención de otras subvenciones que financien las actividades subvencionadas deberá efectuarse:",
  ["Tan pronto como se conozca y, en todo caso, con anterioridad a la justificación de la aplicación dada a los fondos percibidos.", "En el plazo de un mes desde que se conozca.", "Con la solicitud de la subvención, exclusivamente.", "Dentro de los tres meses siguientes a la justificación."],
  "Art. 14.1 d) Ley 38/2003.", "tan pronto como se conozca y, en todo caso, con anterioridad a la justificación de la aplicación dada a los fondos percibidos")
Q("LGS", "Artículo 22", "Concesión", "Según el artículo 22.1 de la Ley 38/2003, el procedimiento ordinario de concesión de subvenciones se tramitará en régimen de:",
  ["Concurrencia competitiva.", "Concesión directa.", "Subasta.", "Libre adjudicación."],
  "Art. 22.1 Ley 38/2003.", "El procedimiento ordinario de concesión de subvenciones se tramitará en régimen de concurrencia competitiva")
Q("LGS", "Artículo 22", "Concesión", "Según el artículo 22.1 de la Ley 38/2003, en el régimen de concurrencia competitiva, la propuesta de concesión se formulará al órgano concedente:",
  ["Por un órgano colegiado a través del órgano instructor.", "Por el órgano instructor directamente, sin intervención de órgano colegiado.", "Por la Intervención Delegada.", "Por el Secretario General Técnico del Ministerio."],
  "Art. 22.1 Ley 38/2003.", "la propuesta de concesión se formulará al órgano concedente por un órgano colegiado a través del órgano instructor")
Q("LGS", "Artículo 23", "Concesión", "Según el artículo 23.1 de la Ley 38/2003, el procedimiento para la concesión de subvenciones en régimen de concurrencia competitiva se inicia:",
  ["Siempre de oficio.", "Siempre a solicitud del interesado.", "De oficio o a solicitud del interesado, indistintamente.", "Por denuncia."],
  "Art. 23.1 Ley 38/2003.", "se inicia siempre de oficio")
Q("LGS", "Artículo 30", "Justificación y pago", "Según el artículo 30.2 de la Ley 38/2003, a falta de previsión de las bases reguladoras, la cuenta justificativa se presentará, como máximo, en el plazo de:",
  ["Tres meses desde la finalización del plazo para la realización de la actividad.", "Un mes desde la finalización del plazo para la realización de la actividad.", "Seis meses desde el cobro de la subvención.", "Tres meses desde la resolución de concesión."],
  "Art. 30.2 Ley 38/2003.", "como máximo, en el plazo de tres meses desde la finalización del plazo para la realización de la actividad")
Q("LGS", "Artículo 34", "Justificación y pago", "Según el artículo 34.3 de la Ley 38/2003, con carácter general, el pago de la subvención se realizará:",
  ["Previa justificación, por el beneficiario, de la realización de la actividad.", "En el momento de la resolución de concesión.", "Siempre por anticipado.", "Al finalizar el ejercicio presupuestario, en todo caso."],
  "Art. 34.3 Ley 38/2003.", "El pago de la subvención se realizará previa justificación, por el beneficiario")
Q("LGS", "Artículo 36", "Reintegro", "Según el artículo 36.1 de la Ley 38/2003, es causa de nulidad de la resolución de concesión:",
  ["La carencia o insuficiencia de crédito.", "La presentación de la cuenta justificativa fuera de plazo.", "El incumplimiento de las medidas de difusión.", "La falta de comunicación de otras subvenciones."],
  "Art. 36.1 b) Ley 38/2003.", "La carencia o insuficiencia de crédito")
Q("LGS", "Artículo 38", "Reintegro", "Según el artículo 38.2 de la Ley 38/2003, salvo que la Ley de Presupuestos Generales del Estado establezca otro diferente, el interés de demora aplicable en materia de subvenciones será:",
  ["El interés legal del dinero incrementado en un 25 por ciento.", "El interés legal del dinero.", "El interés legal del dinero incrementado en un 50 por ciento.", "El tipo de interés del Banco Central Europeo."],
  "Art. 38.2 Ley 38/2003.", "el interés legal del dinero incrementado en un 25 por ciento")
Q("LGS", "Artículo 39", "Reintegro", "Según el artículo 39.1 de la Ley 38/2003, el derecho de la Administración a reconocer o liquidar el reintegro prescribirá a los:",
  ["Cuatro años.", "Cinco años.", "Tres años.", "Diez años."],
  "Art. 39.1 Ley 38/2003.", "Prescribirá a los cuatro años")
Q("LGS", "Artículo 42", "Reintegro", "Según el artículo 42.4 de la Ley 38/2003, el plazo máximo para resolver y notificar la resolución del procedimiento de reintegro será de:",
  ["12 meses desde la fecha del acuerdo de iniciación.", "6 meses desde la fecha del acuerdo de iniciación.", "12 meses desde el vencimiento del plazo de justificación.", "3 meses desde la fecha del acuerdo de iniciación."],
  "Art. 42.4 Ley 38/2003.", "será de 12 meses desde la fecha del acuerdo de iniciación")
Q("LGS", "Artículo 52", "Infracciones", "Según el artículo 52 de la Ley 38/2003, las infracciones administrativas en materia de subvenciones serán sancionables:",
  ["Incluso a título de simple negligencia.", "Solo cuando medie dolo.", "Solo cuando medie culpa grave.", "Solo si el beneficiario ha sido previamente requerido."],
  "Art. 52 Ley 38/2003.", "serán sancionables incluso a título de simple negligencia")
Q("LGS", "Artículo 56", "Infracciones", "Según el artículo 56 de la Ley 38/2003, la presentación fuera de plazo de las cuentas justificativas de la aplicación dada a los fondos percibidos constituye infracción:",
  ["Leve.", "Grave.", "Muy grave.", "No constituye infracción, sino solo causa de reintegro."],
  "Art. 56 a) Ley 38/2003.", "La presentación fuera de plazo de las cuentas justificativas de la aplicación dada a los fondos percibidos")
Q("LGS", "Artículo 58", "Infracciones", "Según el artículo 58 de la Ley 38/2003, la obtención de una subvención falseando las condiciones requeridas para su concesión u ocultando las que la hubiesen impedido o limitado constituye infracción:",
  ["Muy grave.", "Grave.", "Leve.", "Grave o leve, según la cuantía."],
  "Art. 58 a) Ley 38/2003.", "La obtención de una subvención falseando las condiciones requeridas para su concesión u ocultando las que la hubiesen impedido o limitado")
Q("LGS", "Artículo 59", "Infracciones", "Según el artículo 59.2 de la Ley 38/2003, la multa proporcional por infracciones en materia de subvenciones puede ir:",
  ["Del tanto al triple de la cantidad indebidamente obtenida, aplicada o no justificada.", "Del tanto al doble de la cantidad indebidamente obtenida.", "Del doble al quíntuple de la cantidad indebidamente obtenida.", "Hasta el 50 por ciento de la cantidad indebidamente obtenida."],
  "Art. 59.2 Ley 38/2003.", "puede ir del tanto al triple de la cantidad indebidamente obtenida, aplicada o no justificada")
Q("LGS", "Artículo 65", "Infracciones", "Según el artículo 65.1 de la Ley 38/2003, las infracciones en materia de subvenciones prescribirán en el plazo de:",
  ["Cuatro años a contar desde el día en que la infracción se hubiera cometido.", "Tres años a contar desde el día en que la infracción se hubiera cometido.", "Cuatro años a contar desde que la Administración tuvo conocimiento de la infracción.", "Cinco años a contar desde el día en que la infracción se hubiera cometido."],
  "Art. 65.1 Ley 38/2003.", "Las infracciones prescribirán en el plazo de cuatro años a contar desde el día en que la infracción se hubiera cometido")
T.real("L", 53, "Subvenciones: régimen"); T.real("P", 61, "Concesión"); T.real("P", 63, "Infracciones"); T.real("P", 64, "Subvenciones: régimen"); T.real("P", 65, "Infracciones")

# Flashcards
for q_, a_, cat in [
  ("Principios de la Administración en el art. 103.1 CE", "Eficacia, jerarquía, descentralización, desconcentración y coordinación, con sometimiento pleno a la ley y al Derecho.", "Procedimientos y formas"),
  ("Terminación convencional (Ley 39/2015, art. 86): límites", "No contraria al ordenamiento, no sobre materias no susceptibles de transacción y para satisfacer el interés público; aprobación expresa del Consejo de Ministros si es materia de su competencia directa.", "Procedimientos y formas"),
  ("¿Pueden los convenios tener por objeto prestaciones propias de los contratos? (Ley 40/2015, art. 47.1)", "No; si las tienen, se rigen por la legislación de contratos del sector público.", "Procedimientos y formas"),
  ("Principios de la intervención (Ley 40/2015, art. 4)", "Proporcionalidad y medida menos restrictiva; motivar la necesidad; justificar la adecuación; sin discriminación; evaluación periódica.", "Intervención"),
  ("Condiciones para exigir autorización a una actividad de servicios (Ley 17/2009, art. 5)", "No discriminación, necesidad y proporcionalidad, motivadas en la ley; nunca si basta una comunicación o una declaración responsable.", "Intervención"),
  ("Efectos de la declaración responsable y la comunicación (Ley 39/2015, art. 69.3)", "Desde el día de su presentación, sin perjuicio de la comprobación, control e inspección.", "Intervención"),
  ("Medios de intervención de las Entidades locales (LRBRL, art. 84.1)", "Ordenanzas y bandos; licencia y control preventivo; comunicación previa o declaración responsable; control posterior; órdenes individuales.", "Intervención"),
  ("Sustitución de la alzada por arbitraje (Ley 39/2015, art. 112.2)", "Solo por ley, en ámbitos sectoriales determinados, ante órganos colegiados o comisiones no sometidos a instrucciones jerárquicas.", "Arbitral"),
  ("Sistema Arbitral del Consumo: exclusiones (TRLGDCU, art. 57.1)", "Intoxicación, lesión o muerte, o indicios racionales de delito.", "Arbitral"),
  ("Servicios reservados a las Entidades Locales (LRBRL, art. 86.2)", "Abastecimiento domiciliario y depuración de aguas; recogida, tratamiento y aprovechamiento de residuos; transporte público de viajeros.", "Servicio público"),
  ("Formas de gestión directa de los servicios locales (LRBRL, art. 85.2 A)", "Propia Entidad Local; organismo autónomo local; entidad pública empresarial local; sociedad mercantil local de capital público.", "Formas de gestión"),
  ("¿Qué no puede prestarse por concesión de servicios? (LCSP, art. 284.1)", "Los servicios que impliquen ejercicio de la autoridad inherente a los poderes públicos.", "Formas de gestión"),
  ("Requisitos de la subvención (Ley 38/2003, art. 2.1)", "Disposición dineraria; sin contraprestación directa; afectada a un objetivo, proyecto, actividad, comportamiento o situación; con objeto de fomento de utilidad pública, interés social o finalidad pública.", "Subvenciones: concepto"),
  ("Orden de fuentes de las subvenciones (Ley 38/2003, art. 5.1)", "Ley 38/2003 y desarrollo; restantes normas de derecho administrativo; en su defecto, derecho privado.", "Subvenciones: régimen"),
  ("Subvenciones con fondos de la UE (Ley 38/2003, art. 6)", "Normas comunitarias y normas nacionales de desarrollo o transposición; la ley, supletoria respecto de las normas de aplicación directa.", "Subvenciones: régimen"),
  ("¿Quién administra y custodia la BDNS? (Ley 38/2003, art. 20.3)", "La Intervención General de la Administración del Estado.", "Subvenciones: régimen"),
  ("Procedimientos de concesión (Ley 38/2003, art. 22)", "Ordinario: concurrencia competitiva. Directa: nominativas, impuestas por norma de rango legal y excepcionales por razones de interés público, social, económico o humanitario.", "Concesión"),
  ("Modalidades de justificación (Ley 38/2003, art. 30.1; RD 887/2006, art. 69)", "Cuenta justificativa, módulos y estados contables.", "Justificación y pago"),
  ("Interés de demora en subvenciones (Ley 38/2003, art. 38.2)", "Interés legal del dinero incrementado en un 25 %, salvo que la Ley de Presupuestos fije otro.", "Reintegro"),
  ("Prescripción en subvenciones (arts. 39 y 65)", "Cuatro años: reintegro, infracciones y sanciones.", "Reintegro"),
  ("Exención de responsabilidad (Ley 38/2003, art. 54)", "Falta de capacidad de obrar; fuerza mayor; decisión colectiva, para quien salvó su voto o no asistió.", "Infracciones"),
  ("Multas en subvenciones (Ley 38/2003, art. 59.2)", "Fija: de 75 a 6.000 €. Proporcional: del tanto al triple de lo indebidamente obtenido, aplicado o no justificado.", "Infracciones"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Terminación convencional", "Acuerdo, pacto, convenio o contrato de la Administración con personas de Derecho público o privado que pone fin a un procedimiento o se inserta en él (Ley 39/2015, art. 86).", "s2", "Procedimientos y formas")
T.glos("Convenio", "Acuerdo con efectos jurídicos de Administraciones y entes públicos entre sí o con sujetos privados para un fin común; no puede tener por objeto prestaciones propias de los contratos (Ley 40/2015, art. 47).", "s2", "Procedimientos y formas")
T.glos("Autorización", "Acto expreso o tácito de la autoridad competente exigido con carácter previo para el acceso a una actividad de servicios o su ejercicio (Ley 17/2009, art. 3.7).", "s4", "Intervención")
T.glos("Declaración responsable", "Documento en que el interesado manifiesta, bajo su responsabilidad, que cumple los requisitos, dispone de la documentación y se compromete a mantener su cumplimiento (Ley 39/2015, art. 69.1).", "s5", "Intervención")
T.glos("Comunicación", "Documento por el que el interesado pone en conocimiento de la Administración sus datos identificativos o datos relevantes para iniciar una actividad o ejercer un derecho (Ley 39/2015, art. 69.2).", "s5", "Intervención")
T.glos("Sistema Arbitral del Consumo", "Sistema extrajudicial de resolución de conflictos entre consumidores y empresarios, sin formalidades especiales y con carácter vinculante y ejecutivo (TRLGDCU, art. 57).", "s8", "Arbitral")
T.glos("Servicio público local", "El que prestan las entidades locales en el ámbito de sus competencias (LRBRL, art. 85.1).", "s10", "Servicio público")
T.glos("Gestión directa", "Prestación del servicio por la propia Entidad Local, un organismo autónomo local, una entidad pública empresarial local o una sociedad mercantil local de capital público (LRBRL, art. 85.2 A).", "s10", "Formas de gestión")
T.glos("Concesión de servicios", "Contrato por el que poderes adjudicadores encomiendan a título oneroso la gestión de un servicio de su titularidad o competencia a cambio del derecho a explotarlo, con transferencia del riesgo operacional (LCSP, art. 15).", "s11", "Formas de gestión")
T.glos("Ayuda de Estado", "Ayuda otorgada por los Estados o mediante fondos estatales que falsea o amenaza falsear la competencia favoreciendo a determinadas empresas o producciones; incompatible si afecta a los intercambios entre Estados (TFUE, art. 107.1).", "s12", "Ayudas de Estado")
T.glos("Subvención", "Disposición dineraria sin contraprestación directa, afectada a un fin y con objeto de fomento de una actividad de utilidad pública o interés social o de promoción de una finalidad pública (Ley 38/2003, art. 2.1).", "s13", "Subvenciones: concepto")
T.glos("Entidad colaboradora", "La que, en nombre y por cuenta del órgano concedente, entrega y distribuye los fondos a los beneficiarios o colabora en la gestión de la subvención (Ley 38/2003, art. 12.1).", "s16", "Beneficiarios")
T.glos("Bases reguladoras", "Norma que fija objeto, requisitos, procedimiento, criterios, cuantía y justificación de cada subvención; en la AGE, orden ministerial (Ley 38/2003, art. 17).", "s17", "Subvenciones: régimen")
T.glos("Concurrencia competitiva", "Procedimiento ordinario de concesión: comparación de solicitudes y prelación según criterios previamente fijados, dentro del crédito disponible (Ley 38/2003, art. 22.1).", "s18", "Concesión")
T.glos("Reintegro", "Devolución de las cantidades percibidas más el interés de demora en los casos del art. 37 de la Ley 38/2003; prescribe a los cuatro años (art. 39).", "s20", "Reintegro")

# Cronología (fechas de los metadatos del BOE)
T.hito("1985", "Ley 7/1985, de 2 de abril, Reguladora de las Bases del Régimen Local (BOE de 3-4-1985)", "Arts. 84 a 86: intervención local, formas de gestión y reserva de servicios", "normativo", "s10")
T.hito("2003", "Ley 38/2003, de 17 de noviembre, General de Subvenciones (BOE de 18-11-2003)", "Régimen jurídico general de las subvenciones", "normativo", "s13")
T.hito("2006", "Real Decreto 887/2006, de 21 de julio, Reglamento de la Ley General de Subvenciones (BOE de 25-7-2006)", "Desarrollo reglamentario: concesión, justificación y reintegro", "normativo", "s18")
T.hito("2007", "Real Decreto Legislativo 1/2007, de 16 de noviembre, texto refundido de la Ley General para la Defensa de los Consumidores y Usuarios (BOE de 30-11-2007)", "Arts. 57 y 58: Sistema Arbitral del Consumo", "normativo", "s8")
T.hito("2009", "Ley 17/2009, de 23 de noviembre, sobre el libre acceso a las actividades de servicios y su ejercicio (BOE de 24-11-2009)", "Art. 5: la autorización, solo excepcionalmente", "normativo", "s4")
T.hito("2015", "Leyes 39/2015 y 40/2015, de 1 de octubre (BOE de 2-10-2015)", "Declaración responsable (art. 69 LPAC) y principios de intervención (art. 4 LRJSP)", "normativo", "s5")
T.hito("2017", "Ley 9/2017, de 8 de noviembre, de Contratos del Sector Público (BOE de 9-11-2017)", "Contrato de concesión de servicios (arts. 15 y 284)", "normativo", "s11")

T.publicar()
