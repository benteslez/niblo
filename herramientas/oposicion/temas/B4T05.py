# -*- coding: utf-8 -*-
"""Tema IV.5 (B4T05): Los contratos del sector público (I): concepto, clases y elementos.
Preparación, adjudicación, efectos, cumplimiento y extinción. La revisión de precios y otras
alteraciones contractuales. Régimen de invalidez y recursos.
Método del I.2: mapa → bloques (I a VI, uno por frase del epígrafe) con guía; cada artículo,
texto literal del BOE (Ley 9/2017, texto consolidado vigente, umbrales de 2026) + ficha de
casillas fijas; cierre 1 (preguntas oficiales) y cierre 2 (repaso)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

K = "LCSP"
def A(n): return f"Artículo {n}"
def L(n, resaltar=(), solo=None): return lit(K, A(n), resaltar, solo)
def C(n, frag): return c(K, A(n), frag)
def ap(id, title, partes, nivel=2): T.ap(id, title, "\n\n".join(p.strip("\n") for p in partes), nivel)
ESQ = "*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*"

T = Tema("B4T05",
  "Seis preguntas: I. Qué es un contrato del sector público, qué clases hay y qué elementos tiene (arts. 1 a 37, 61 a 107 y 323) · II. Cómo se prepara: expediente y pliegos (arts. 28 y 116 a 124) · III. Cómo se adjudica (arts. 131 a 168) · IV. Efectos, cumplimiento y extinción (arts. 188 a 213) · V. Revisión de precios y otras alteraciones (arts. 103 a 105 y 203 a 215) · VI. Invalidez y recurso especial (arts. 38 a 59). Ley 9/2017 con los umbrales vigentes desde el 1-1-2026. Cada artículo: texto literal del BOE y ficha.",
  ["LCSP", "Contrato del sector público", "Poder adjudicador", "Regulación armonizada", "Umbrales 2026", "Contratos administrativos y privados", "Valor estimado", "Expediente y pliegos", "Contrato menor", "Procedimiento abierto", "Abierto simplificado", "Prerrogativas", "Resolución", "Revisión de precios", "Modificación", "Invalidez", "Recurso especial"])

# =============================================================================
T.ap("s0", "Mapa del tema: seis preguntas", """
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque IV, tema 5):
> Los contratos del sector público (I): concepto, clases y elementos. Preparación, adjudicación, efectos, cumplimiento y extinción. La revisión de precios y otras alteraciones contractuales. Régimen de invalidez y recursos.

### El hilo conductor

El epígrafe tiene cuatro frases y recorre la **vida de un contrato**: qué es, cómo se prepara, cómo se adjudica, cómo se ejecuta y se acaba, qué puede cambiar durante su vida y qué pasa si nace viciado. Se lee como **seis preguntas**; cada una es un bloque. Todo sale de la **Ley 9/2017, de 8 de noviembre, de Contratos del Sector Público (LCSP)**.

| Bloque | Pregunta | Artículos de la LCSP |
|---|---|---|
| **I** | ¿Qué es un contrato del sector público, qué clases hay y qué elementos tiene? | 1 a 3, 5, 10 a 12, 19 a 22, 24 a 27, 29, 35 a 37, 61, 65, 74, 88, 99 a 102, 106, 107 y 323 |
| **II** | ¿Cómo se prepara? Expediente y pliegos | 28, 116 a 122 y 124 |
| **III** | ¿Cómo se adjudica? | 131, 145, 150, 151, 153, 156, 158 a 160, 162, 166 y 168 |
| **IV** | ¿Qué efectos tiene y cómo se cumple y se extingue? | 188 a 193, 196 a 198 y 209 a 213 |
| **V** | ¿Cómo se revisan los precios y qué otras alteraciones caben? | 103 a 105, 203 a 208, 214 y 215 |
| **VI** | ¿Cuándo es inválido y cómo se recurre? | 38 a 45, 48 a 50, 53 y 57 a 59 |

!> **La idea que une los seis bloques:** un contrato es del sector público si es **oneroso** y lo celebra una entidad del **art. 3** (I). Antes de contratar hay un **expediente** con sus **pliegos** (II); se elige al contratista por un **procedimiento** con publicidad y concurrencia (III); la Administración conserva **prerrogativas** durante la ejecución hasta que el contrato se **cumple o se resuelve** (IV); el precio y el contrato solo cambian por las vías tasadas de **revisión** y **modificación** (V); y los vicios de preparación o adjudicación se depuran por la **invalidez** y el **recurso especial** (VI).

### Cómo está escrito

- Los bloques siguen el **orden del epígrafe**; dentro de cada bloque, el **orden de los artículos**.
- Cada artículo: primero el **texto literal del BOE** (texto consolidado vigente; los umbrales son los aplicables **desde el 1 de enero de 2026**) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- La LCSP es muy larga: de cada artículo se copian **los apartados que se preguntan**; el resto se cita en la ficha.
- Los esquemas y cuadros **no son texto legal**: resumen los artículos citados.
- Los tipos de contrato (obras, concesiones, suministro, servicios) y sus reglas propias son el **tema IV.6**.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques y cuadro de cifras).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué es un contrato del sector público, qué clases hay y qué elementos tiene?", donde(
  "Primera pregunta, la de la primera frase del epígrafe: **concepto, clases y elementos**. Antes de preparar o adjudicar nada hay que saber qué contratos entran en la ley, cuáles quedan fuera, cuáles son armonizados, administrativos o privados, y cuáles son sus elementos: partes, objeto y precio.",
  ["1 Objeto y concepto; sector público, Administraciones y poderes adjudicadores (arts. 1 a 3)", "2 Negocios excluidos (arts. 5, 10 y 11)", "3 Calificación y regulación armonizada; umbrales de 2026 (arts. 12 y 19 a 22)", "4 Contratos administrativos y privados; jurisdicción (arts. 24 a 27)", "5 Duración, contenido, perfección y forma (arts. 29 y 35 a 37)", "6 Las partes (arts. 61, 65, 74 y 88)", "7 Objeto, presupuesto, valor estimado, precio y garantías (arts. 99 a 107)", "8 Órganos de contratación del Estado (art. 323)"]))

ap("s1", "I.1 Objeto y concepto: qué es un contrato del sector público (arts. 1 a 3)", [
  "La LCSP regula la contratación del **sector público**. Un contrato entra en la ley por dos datos: es **oneroso** y lo celebra una **entidad del art. 3**. El art. 3 dibuja tres círculos: sector público ⊃ poderes adjudicadores ⊃ Administraciones Públicas.",
  unidad("1.1 Objeto y finalidad de la ley (art. 1)",
    L(1, ["libertad de acceso a las licitaciones, publicidad y transparencia de los procedimientos, y no discriminación e igualdad de trato entre los licitadores", "la selección de la oferta económicamente más ventajosa"], solo=[1, 2]),
    fichab("Para qué existe la LCSP: principios y fines de la contratación pública",
           "Todas las entidades del sector público (art. 3)",
           ["::Principios (1.1):", "Libertad de acceso a las licitaciones", "Publicidad y transparencia de los procedimientos", "No discriminación e igualdad de trato entre los licitadores", "Fines: estabilidad presupuestaria y control del gasto, integridad, libre competencia y selección de la oferta económicamente más ventajosa"],
           "—",
           f"El 1.2 añade como objeto el régimen de {C(1, 'los efectos, cumplimiento y extinción de los contratos administrativos')}: solo de los **administrativos** (los privados se rigen en eso por el derecho privado, → I.4.2).")),
  unidad("1.2 Concepto: contratos onerosos (art. 2.1)",
    L(2, ["los contratos onerosos, cualquiera que sea su naturaleza jurídica", "algún tipo de beneficio económico, ya sea de forma directa o indirecta"], solo=[1, 2]),
    fichab("Concepto legal de contrato del sector público",
           f"Lo celebran {C(2, 'las entidades enumeradas en el artículo 3')}",
           "Contrato **oneroso**, cualquiera que sea su naturaleza jurídica (administrativo o privado)",
           "—",
           "Oneroso = el contratista obtiene **algún tipo de beneficio económico, directo o indirecto**. También se sujetan los contratos **subvencionados** del art. 23 (2.2).")),
  unidad("1.3 Las entidades del sector público (art. 3.1)",
    L(3, ["Las Mutuas colaboradoras con la Seguridad Social", "superior al 50 por 100"], solo=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]),
    fichab("Entidades que forman el sector público a efectos de la LCSP",
           "Las de las letras a) a l) del 3.1",
           ["::Tres círculos:", "Sector público: todas las del 3.1", "Poderes adjudicadores: las del 3.3 (→ I.1.4)", "Administraciones Públicas: las del 3.2 (→ I.1.4)"],
           "Sociedades mercantiles: participación pública **superior al 50 por 100** (letra h)",
           "Las **Mutuas colaboradoras con la Seguridad Social** forman parte del sector público (letra f): cayó en 2025 (→ Cierre 1).")),
  unidad("1.4 Administraciones Públicas y poderes adjudicadores (art. 3.2 y 3)",
    L(3, ["tendrán la consideración de Administraciones Públicas", "Se considerarán poderes adjudicadores"], solo=[17, 18, 19, 20, 21, 22, 23, 24, 25]),
    fichab("Quién es Administración Pública y quién poder adjudicador: de ello depende el régimen del contrato",
           ["::Administraciones Públicas (3.2):", "AGE, Administraciones de las CC. AA., Ceuta y Melilla y entidades locales (letra a del 3.1)", "Entidades Gestoras y Servicios Comunes de la Seguridad Social (b)", "Organismos Autónomos, Universidades Públicas y autoridades administrativas independientes (c)", "Diputaciones Forales y Juntas Generales del País Vasco (l)", "Consorcios y entidades de derecho público no financiados mayoritariamente con ingresos de mercado (3.2 b)"],
           ["::Poderes adjudicadores (3.3):", "Las Administraciones Públicas", "Las fundaciones públicas", "Las Mutuas colaboradoras con la Seguridad Social", "Entidades creadas para necesidades de interés general no industriales ni mercantiles, financiadas, controladas o con órgano nombrado mayoritariamente por un poder adjudicador", "Sus asociaciones"],
           "—",
           "Toda Administración Pública es poder adjudicador, pero no al revés: las **fundaciones públicas** y las **Mutuas** son poder adjudicador **sin** ser Administración Pública. Contratos **administrativos** solo los celebra una **Administración Pública** (→ I.4.1).")),
])

ap("s2", "I.2 Negocios y contratos excluidos (arts. 5, 10 y 11)", [
  "Hay negocios que, aunque los celebre el sector público, **no se rigen por la LCSP**. Los que más se preguntan:",
  unidad("2.1 Defensa y seguridad: procedimientos internacionales (art. 5.4)",
    L(5, ["estacionamiento de tropas"], solo=[9, 10, 11, 12]),
    fichab("Exclusión de contratos de defensa y seguridad con procedimiento fijado por normas internacionales",
           "Contratos y convenios en los ámbitos de la defensa o de la seguridad",
           ["Acuerdo o convenio internacional para un proyecto conjunto con Estados no signatarios del TFUE (a)", "Acuerdo o convenio internacional de **estacionamiento de tropas** (b)", "Normas de una organización o institución financiera internacional que los financia íntegramente o en su mayor parte (c)"],
           "—",
           "El estacionamiento de tropas cayó en 2025 como contrato **excluido** (→ Cierre 1). El art. 5 recoge más exclusiones de defensa y seguridad (5.1 a 5.3).")),
  unidad("2.2 Ámbito financiero (art. 10)",
    L(10, ["compra, venta o transferencia de valores o de otros instrumentos financieros", "los contratos de préstamo y operaciones de tesorería"]),
    fichab("Exclusión de servicios financieros sobre valores, préstamos y tesorería",
           "—",
           ["Servicios financieros de emisión, compra, venta o transferencia de valores o instrumentos financieros", "Servicios del Banco de España; operaciones con la Facilidad Europea de Estabilización Financiera y el Mecanismo Europeo de Estabilidad", "Préstamos y operaciones de tesorería"],
           "—",
           "La compraventa de **valores** está **excluida**: cayó en 2025 (→ Cierre 1).")),
  unidad("2.3 Otros negocios excluidos (art. 11)",
    L(11, ["La relación de servicio de los funcionarios públicos y los contratos regulados en la legislación laboral", "cuando sean adjudicados por un partido político"]),
    fichab("Otras exclusiones",
           "—",
           ["Relación de servicio de los funcionarios y contratos laborales (11.1)", "Servicio público con tarifa, tasa o precio público de aplicación general (11.2)", "Arbitraje y conciliación (11.3)", "Contratos por los que una entidad del sector público se obliga a entregar bienes o prestar servicios (11.4)", "Servicios de campañas políticas adjudicados por un partido político (11.5)", "Servicios sociales por entidades privadas sin contrato público (11.6)"],
           "—",
           "Campañas políticas: excluidas **cuando las adjudica un partido político**. La relación **funcionarial** y los contratos **laborales** nunca son contratos de la LCSP.")),
])

ap("s3", "I.3 Calificación y contratos sujetos a regulación armonizada (arts. 12 y 19 a 22)", [
  "Primera clasificación: por su **tipo** (art. 12) y por su **cuantía** (armonizados o no). Un contrato **sujeto a regulación armonizada (SARA)** sigue las reglas de las Directivas europeas: publicidad en el DOUE, plazos más largos, etc.",
  unidad("3.1 Calificación de los contratos (art. 12)",
    L(12, ["obras, concesión de obras, concesión de servicios, suministro y servicios"]),
    fichab("Cómo se califican los contratos",
           "Entidades del sector público",
           "Los cinco contratos típicos se califican por las normas de su sección (arts. 13 a 18; su estudio es el tema IV.6); los demás, por las normas de derecho administrativo o privado que les sean aplicables",
           "—",
           "Cinco típicos: **obras, concesión de obras, concesión de servicios, suministro y servicios**.")),
  unidad("3.2 Qué es un contrato armonizado (art. 19.1)",
    L(19, ["siempre que la entidad contratante tenga el carácter de poder adjudicador"], solo=[1]),
    fichab("Contrato sujeto a regulación armonizada (SARA)",
           "Solo si contrata un **poder adjudicador** (y los subvencionados del art. 23)",
           f"Valor estimado (art. 101, → I.7.3) {C(19, 'igual o superior a las cuantías que se indican en los artículos siguientes')}",
           "Umbrales: arts. 20 a 22 (→ I.3.3)",
           "«Igual **o superior**»: el importe exacto del umbral ya es armonizado. El 19.2 excluye ciertos contratos cualquiera que sea su valor (audiovisuales, defensa del art. 346 TFUE, secretos o reservados, comunicaciones electrónicas, ciertos servicios jurídicos…).")),
  unidad("3.3 Los umbrales vigentes desde el 1 de enero de 2026 (arts. 20.1, 21.1 y 22.1)",
    L(20, ["5.404.000 euros"], solo=[1]),
    L(21, ["140.000 euros", "216.000 euros"], solo=[1, 2, 3]),
    L(22, ["140.000 euros", "216.000 euros", "750.000 euros"], solo=[1, 2, 3, 4]),
    fichab("Cuantías que hacen armonizado un contrato (redacción dada por la Orden HAC/1517/2025, BOE de 26-12-2025)",
           "Umbral **bajo** para la AGE, sus Organismos Autónomos y las Entidades Gestoras y Servicios Comunes de la Seguridad Social; umbral **alto** para las demás entidades",
           ["Obras, concesión de obras y concesión de servicios: **5.404.000 €**", "Suministros y servicios de la AGE, OO. AA. y entidades de la Seguridad Social: **140.000 €**", "Suministros y servicios de las demás entidades: **216.000 €**", "Servicios sociales y otros específicos del anexo IV: **750.000 €**"],
           "Valor estimado **igual o superior** al umbral",
           "Las **concesiones de servicios** van con las **obras** (5.404.000 €), no con los servicios. Un **organismo autónomo** (p. ej., el FOGASA) usa el umbral de **140.000 €**: cayó en 2025 (→ Cierre 1).")),
])

ap("s4", "I.4 Contratos administrativos y contratos privados; jurisdicción (arts. 24 a 27)", [
  "Segunda clasificación, por su **régimen jurídico**: administrativo o privado. Decide qué normas rigen cada fase del contrato y **qué jueces** resuelven los litigios.",
  unidad("4.1 Régimen jurídico y contratos administrativos (arts. 24 y 25)",
    L(24),
    L(25, ["siempre que se celebren por una Administración Pública", "Aquellos cuyo objeto sea la suscripción a revistas, publicaciones periódicas y bases de datos.", "naturaleza administrativa especial"], solo=[1, 2, 3, 4, 5, 6]),
    fichab("Contratos administrativos: los típicos y los especiales, celebrados por una Administración Pública",
           f"Solo {C(25, 'siempre que se celebren por una Administración Pública')}",
           ["::Dos grupos (25.1):", "a) Obra, concesión de obra, concesión de servicios, suministro y servicios (salvo ciertos servicios financieros, de creación artística y literaria y de espectáculos, y la suscripción a revistas, publicaciones periódicas y bases de datos, que son **privados**)", "b) Administrativos especiales: declarados por una ley, o vinculados al giro o tráfico específico de la Administración o a una finalidad pública de su competencia"],
           "Régimen (25.2): LCSP y su desarrollo; supletoriamente, derecho administrativo y, en su defecto, privado",
           "Los administrativos **especiales** se rigen **en primer término por sus normas específicas** (25.2).")),
  unidad("4.2 Contratos privados (art. 26)",
    L(26, ["En lo que respecta a su efectos, modificación y extinción, estos contratos se regirán por el derecho privado."], solo=[1, 2, 3, 4, 5]),
    fichab("Contratos privados del sector público",
           ["Administraciones Públicas, con objeto distinto de los del 25.1 (a)", "Poderes adjudicadores que no son Administración Pública (b)", "Entidades del sector público que no son poder adjudicador (c)"],
           "Contratos privados de las AAPP (26.2): **preparación y adjudicación** por la LCSP; **efectos, modificación y extinción** por el derecho privado",
           "—",
           "Lo **preparatorio y la adjudicación** van por la LCSP (y por el contencioso, → I.4.3); los **efectos y la extinción**, por el derecho privado (y por el orden civil).")),
  unidad("4.3 Jurisdicción competente (art. 27)",
    L(27, ["Las relativas a la preparación, adjudicación, efectos, modificación y extinción de los contratos administrativos.", "Las que se susciten en relación con la preparación y adjudicación de los contratos privados de las Administraciones Públicas.", "El orden jurisdiccional civil será el competente para resolver:"], solo=[1, 2, 3, 6, 7, 9, 10, 11]),
    fichab("Reparto de los litigios entre el orden contencioso-administrativo y el civil",
           "Orden contencioso-administrativo (27.1) u orden civil (27.2)",
           ["::Contencioso-administrativo (27.1):", "Todo el contrato administrativo: preparación, adjudicación, efectos, modificación y extinción", "Preparación y adjudicación de los contratos privados de las AAPP", "Preparación y adjudicación de los contratos de entidades que no son poder adjudicador", "Recursos contra las resoluciones de los órganos del recurso especial (art. 44)", "**Civil (27.2):** efectos y extinción de los contratos privados de los poderes adjudicadores y de los contratos de entidades que no son poder adjudicador"],
           "—",
           "Contra la resolución del recurso especial cabe el **contencioso-administrativo** (→ VI.3.7). Los **efectos y la extinción** de los contratos **privados** van al orden **civil**.")),
])

ap("s5", "I.5 Duración, contenido, perfección y forma (arts. 29 y 35 a 37)", [
  unidad("5.1 Duración y prórroga (art. 29)",
    L(29, ["al menos con dos meses de antelación", "En ningún caso podrá producirse la prórroga por el consentimiento tácito de las partes.", "un plazo máximo de duración de cinco años", "no podrán tener una duración superior a un año ni ser objeto de prórroga"], solo=[1, 2, 3, 4, 7, 25]),
    fichab("Duración y prórroga de los contratos",
           "La prórroga la acuerda el **órgano de contratación** y es **obligatoria** para el empresario (con el preaviso legal)",
           ["Prórroga prevista en el contrato, con características inalterables (29.2)", "Nunca por consentimiento tácito"],
           ["Preaviso de la prórroga: al menos **dos meses** antes del fin (salvo plazo mayor en el pliego)", "Suministros y servicios de prestación sucesiva: máximo **cinco años**, prórrogas incluidas (29.4)", "Contratos menores: máximo **un año**, sin prórroga (29.8)"],
           "No hay prórroga **tácita**. El art. 29.6 fija topes para las concesiones (cuarenta, veinticinco y diez años, según el caso).")),
  unidad("5.2 Contenido mínimo del contrato (art. 35)",
    L(35, ["El precio cierto, o el modo de determinarlo."]),
    fichab("Menciones obligatorias del documento de formalización",
           "Las partes (entidad contratante y adjudicatario)",
           "Catorce menciones (letras a a n), salvo que ya estén en los pliegos",
           "—",
           f"El documento {C(35, 'no podrá incluir estipulaciones que establezcan derechos y obligaciones para las partes distintos de los previstos en los pliegos')}.")),
  unidad("5.3 Perfección (art. 36)",
    L(36, ["se perfeccionan con su formalización", "se perfeccionan con su adjudicación"]),
    fichab("Momento en que nace el contrato",
           "Poderes adjudicadores",
           ["Regla: con la **formalización** (36.1)", "Excepciones: contratos menores, y contratos **basados en un acuerdo marco** y específicos de un sistema dinámico de adquisición, que se perfeccionan con la **adjudicación** (36.3)", "Subvencionados armonizados: según su propia legislación (36.2)"],
           "—",
           "Cayó en 2025: los basados en un acuerdo marco se perfeccionan con su **adjudicación** (→ Cierre 1). Lugar de celebración: la **sede del órgano de contratación** (36.4).")),
  unidad("5.4 Forma escrita (art. 37)",
    L(37, ["no podrán contratar verbalmente"]),
    fichab("Carácter formal de la contratación",
           "Entidades del sector público",
           "Prohibido contratar verbalmente; las AAPP formalizan según el art. 153 (→ III.2.3); los menores, según el art. 118",
           "—",
           "Única excepción a la forma escrita: la **emergencia** (art. 120.1, → II.2.3).")),
], 2)

ap("s6", "I.6 Las partes: órgano de contratación y contratista (arts. 61, 65, 74 y 88)", [
  "Elementos **subjetivos**: de un lado, el **órgano de contratación**; de otro, el **contratista**, que debe ser apto (capacidad, ausencia de prohibiciones y solvencia o clasificación).",
  unidad("6.1 Órgano de contratación (art. 61)",
    L(61, ["órganos de contratación, unipersonales o colegiados"]),
    fichab("Quién representa a la entidad contratante",
           "Órganos de contratación, **unipersonales o colegiados**",
           "Por norma legal o reglamentaria o disposición estatutaria; pueden **delegar o desconcentrar** (61.2)",
           "—",
           "En la AGE: Ministros y Secretarios de Estado (art. 323, → I.8.1).")),
  unidad("6.2 Aptitud del contratista (art. 65)",
    L(65, ["plena capacidad de obrar, no estén incursas en alguna prohibición de contratar, y acrediten su solvencia económica y financiera y técnica o profesional"], solo=[1, 3]),
    fichab("Condiciones de aptitud para contratar",
           "Personas naturales o jurídicas, **españolas o extranjeras**",
           ["Plena capacidad de obrar", "No estar incursas en prohibición de contratar (art. 71)", "Solvencia económica y financiera y técnica o profesional, o clasificación cuando se exija", "Habilitación empresarial o profesional exigible (65.2)"],
           "—",
           "La falta de capacidad, solvencia, habilitación o clasificación, o la prohibición de contratar, es causa de **nulidad** (art. 39.2 a, → VI.1.2).")),
  unidad("6.3 Exigencia de solvencia (art. 74)",
    L(74, ["Este requisito será sustituido por el de la clasificación"]),
    fichab("Solvencia mínima",
           "La determina el **órgano de contratación**",
           "Se indica en el anuncio y se especifica en el pliego; vinculada al objeto y proporcional",
           "—",
           "La **clasificación**, cuando sea exigible, **sustituye** a la solvencia.")),
  unidad("6.4 Solvencia técnica en los contratos de obras (art. 88.1 a)",
    L(88, ["en el curso de los cinco últimos años", "en los últimos diez años"], solo=[1, 2]),
    fichab("Medios para acreditar la solvencia técnica en obras",
           "A elección del órgano de contratación (uno o varios medios)",
           "Primer medio: relación de obras ejecutadas, avalada por certificados de buena ejecución",
           "**Cinco** últimos años; los de los últimos **diez** si es necesario para garantizar un nivel adecuado de competencia",
           f"Cayó en 2025: **cinco** años (→ Cierre 1). Los «tres últimos años» son de otro medio: la plantilla media {C(88, 'durante los tres últimos años')} (88.1 e).")),
], 2)

ap("s7", "I.7 Objeto, presupuesto, valor estimado, precio y garantías (arts. 99 a 102, 106 y 107)", [
  "Elementos **objetivos**: el **objeto** y las tres cifras que no hay que confundir: **presupuesto base de licitación** (con IVA), **valor estimado** (sin IVA y con prórrogas) y **precio** (lo que se paga). Se añaden las **garantías**.",
  unidad("7.1 Objeto del contrato y lotes (art. 99)",
    L(99, ["No podrá fraccionarse un contrato con la finalidad de disminuir la cuantía del mismo", "mediante su división en lotes"], solo=[1, 2, 3]),
    fichab("Objeto del contrato",
           "Órgano de contratación",
           ["Determinado; puede definirse por necesidades o funcionalidades", "Prohibido fraccionar para eludir la publicidad o el procedimiento", "Regla: división en **lotes** si la naturaleza o el objeto lo permiten"],
           "—",
           "No dividir en lotes exige **motivos válidos justificados en el expediente**, salvo en la concesión de obras (99.3).")),
  unidad("7.2 Presupuesto base de licitación (art. 100)",
    L(100, ["incluido el Impuesto sobre el Valor Añadido"], solo=[1]),
    fichab("Límite máximo de gasto del contrato",
           "Órgano de contratación",
           "Adecuado a los precios del mercado; desglosado en el pliego (costes directos e indirectos y otros gastos)",
           "—",
           "Presupuesto base: **con IVA**. Valor estimado (→ I.7.3): **sin IVA**.")),
  unidad("7.3 Valor estimado (art. 101)",
    L(101, ["sin incluir el Impuesto sobre el Valor Añadido, pagadero según sus estimaciones", "las eventuales prórrogas del contrato"], solo=[1, 2, 3, 4, 5, 6, 7]),
    fichab("La cifra que decide umbrales, procedimiento y publicidad",
           "Órgano de contratación",
           ["Obras, suministros y servicios: importe total **sin IVA** (101.1 a)", "Concesiones: cifra de negocios del concesionario, sin IVA (101.1 b)", "Incluye prórrogas, opciones, primas y modificaciones previstas al alza (101.2)"],
           "—",
           "El valor estimado (**sin IVA** y **con prórrogas**) es el que se compara con los umbrales SARA (→ I.3.3), con las cifras del contrato menor y con las del recurso especial.")),
  unidad("7.4 Precio (art. 102)",
    L(102, ["tendrán siempre un precio cierto", "Se prohíbe el pago aplazado del precio"], solo=[1, 7, 15]),
    fichab("Precio del contrato",
           "—",
           ["Cierto; se abona según la prestación **realmente ejecutada**", "IVA incluido, como partida independiente", "Revisable en los términos del capítulo II (→ V.1)"],
           "—",
           "Pago **aplazado** prohibido en los contratos de las AAPP, salvo arrendamiento financiero, arrendamiento con opción de compra o autorización legal.")),
  unidad("7.5 Garantía provisional y garantía definitiva (arts. 106 y 107)",
    L(106, ["no procederá la exigencia de garantía provisional", "no podrá ser superior a un 3 por 100 del presupuesto base de licitación"], solo=[1, 2]),
    L(107, ["una garantía de un 5 por 100 del precio final ofertado"], solo=[1]),
    fichab("Garantías del licitador y del adjudicatario",
           "Provisional: los licitadores, solo si se exige; definitiva: quien presenta la mejor oferta",
           ["Provisional: **excepcional**, por motivos de interés público justificados", "Definitiva: regla en los contratos de las AAPP; puede eximirse justificándolo en el pliego (107.1)"],
           ["Provisional: hasta el **3 %** del presupuesto base de licitación, sin IVA", "Definitiva: **5 %** del precio final ofertado, sin IVA"],
           "Provisional → % del **presupuesto base**; definitiva → % del **precio ofertado**. En el abierto simplificado no hay garantía provisional (→ III.3.3).")),
], 2)

ap("s8", "I.8 Los órganos de contratación del Estado (art. 323)", [
  unidad("8.1 Órganos de contratación estatales (art. 323.1 y 2)",
    L(323, ["Los Ministros y los Secretarios de Estado son los órganos de contratación", "corresponderá al Ministro, salvo en los casos en que la misma se atribuya a la Junta de Contratación"], solo=[1, 2, 3]),
    fichab("Quién contrata en el sector público estatal",
           ["Ministros y Secretarios de Estado (AGE)", "Presidentes o Directores de OO. AA., EPE y demás entidades estatales; Directores generales de las Entidades Gestoras y Servicios Comunes de la Seguridad Social (a falta de norma específica)"],
           "Suministros y servicios que afecten a más de un órgano de contratación del departamento: el **Ministro**, salvo atribución a la **Junta de Contratación**",
           "—",
           "Cayó en 2025: el **Ministro** (no el Subsecretario ni el Secretario de Estado) (→ Cierre 1).")),
  resumen([
    "Contrato del sector público = **oneroso** + entidad del **art. 3**; tres círculos: sector público, poderes adjudicadores y Administraciones Públicas.",
    "Excluidos, entre otros: relación funcionarial y laboral, valores e instrumentos financieros, estacionamiento de tropas, campañas políticas de los partidos.",
    "SARA desde el 1-1-2026: obras y concesiones **5.404.000 €**; suministros y servicios **140.000 €** (AGE, OO. AA., Seguridad Social) o **216.000 €** (resto); anexo IV **750.000 €**.",
    "Administrativos: los típicos y los especiales **de una Administración Pública**; privados: los demás. Contencioso para todo el administrativo y para preparar y adjudicar los privados de las AAPP; civil para efectos y extinción de los privados.",
    "Perfección con la **formalización** (basados en acuerdo marco: **adjudicación**); nunca verbal salvo **emergencia**.",
    "Presupuesto base **con IVA**; valor estimado **sin IVA** y con prórrogas; garantía provisional ≤ **3 %** del presupuesto base; definitiva **5 %** del precio ofertado."],
    "Siguiente: II. ¿Cómo se prepara? Expediente y pliegos"),
], 2)

# =============================================================================
T.ap("bII", "II. ¿Cómo se prepara el contrato? Expediente y pliegos", donde(
  "Segunda pregunta: la **preparación**. Antes de adjudicar, la Administración documenta por qué necesita el contrato (expediente) y fija sus reglas (pliegos). La tramitación puede ser ordinaria, urgente o de emergencia, y los contratos menores tienen un expediente mínimo.",
  ["1 El expediente de contratación (arts. 28, 116 y 117)", "2 Contratos menores, tramitación urgente y de emergencia (arts. 118 a 120)", "3 Los pliegos (arts. 121, 122 y 124)"]))

ap("s9", "II.1 El expediente de contratación (arts. 28, 116 y 117)", [
  unidad("1.1 Necesidad e idoneidad del contrato (art. 28.1)",
    L(28, ["que sean necesarios para el cumplimiento y realización de sus fines institucionales"], solo=[1]),
    fichab("Necesidad e idoneidad del contrato",
           "Entidades del sector público",
           "Naturaleza y extensión de las necesidades e idoneidad del objeto, determinadas con precisión en la documentación preparatoria",
           "Antes de iniciar el procedimiento de adjudicación",
           "Solo pueden celebrarse contratos **necesarios** para los fines institucionales.")),
  unidad("1.2 Iniciación y contenido del expediente (art. 116)",
    L(116, ["requerirá la previa tramitación del correspondiente expediente", "el informe de insuficiencia de medios"], solo=[1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
    fichab("Expediente de contratación",
           "Lo inicia el **órgano de contratación**, motivando la necesidad; se publica en el perfil de contratante",
           ["Se incorporan el PCAP y el PPT (116.3)", "Certificado de existencia de crédito y fiscalización previa, en su caso", "Se justifican: procedimiento, clasificación, solvencia y criterios de adjudicación, valor estimado, necesidad, insuficiencia de medios (servicios) y no división en lotes (116.4)"],
           "—",
           "En los contratos de **servicios** se justifica la **insuficiencia de medios**.")),
  unidad("1.3 Aprobación del expediente (art. 117.1)",
    L(117, ["Dicha resolución implicará también la aprobación del gasto"], solo=[1]),
    fichab("Aprobación del expediente",
           "El **órgano de contratación**, por resolución motivada",
           "Aprueba el expediente y dispone la apertura del procedimiento de adjudicación; se publica en el perfil de contratante",
           "—",
           "La aprobación del expediente **implica la aprobación del gasto**, salvo las excepciones del 117.1.")),
], 2)

ap("s10", "II.2 Contratos menores, tramitación urgente y de emergencia (arts. 118 a 120)", [
  unidad("2.1 El expediente del contrato menor (art. 118)",
    L(118, ["inferior a 40.000 euros", "a 15.000 euros"], solo=[1, 2, 3, 5]),
    fichab("Contrato menor: expediente mínimo por razón de la cuantía",
           "Órgano de contratación; adjudicación directa a cualquier empresario con capacidad y habilitación (art. 131.3, → III.1.1)",
           ["Informe motivado de la necesidad y de que no se altera el objeto para eludir los umbrales", "Aprobación del gasto y factura", "Obras: además, el presupuesto (y el proyecto y el informe de supervisión cuando procedan)"],
           ["Obras: valor estimado **inferior a 40.000 €**", "Suministros y servicios: **inferior a 15.000 €**", "Duración: máximo **un año**, sin prórroga (art. 29.8)"],
           "«**Inferior** a»: un contrato de obras de 40.000 € justos ya no es menor. Pagos por anticipo de caja fija de hasta 5.000 €: sin el informe del 118.2.")),
  unidad("2.2 Tramitación urgente (art. 119)",
    L(119, ["necesidad inaplazable", "se reducirán a la mitad", "no podrá exceder de un mes"]),
    fichab("Tramitación urgente del expediente",
           "El **órgano de contratación** declara la urgencia, motivada",
           ["Preferencia en el despacho", "Plazos de licitación, adjudicación y formalización **a la mitad**, con las excepciones del 119.2 b)"],
           ["Informes: **5 días** (prorrogables hasta 10)", "Inicio de la ejecución: no más de **un mes** desde la formalización"],
           "No se reduce el plazo de espera de **15 días hábiles** antes de formalizar (art. 153.3). En el abierto simplificado no se reducen sus plazos (119.2 b 6.º).")),
  unidad("2.3 Tramitación de emergencia (art. 120.1)",
    L(120, ["acontecimientos catastróficos, de situaciones que supongan grave peligro o de necesidades que afecten a la defensa nacional", "sin obligación de tramitar expediente de contratación", "en el plazo máximo de treinta días", "no podrá ser superior a un mes"], solo=[1, 2, 3, 4]),
    fichab("Tramitación de emergencia: régimen excepcional",
           "El órgano de contratación; en el Estado, da cuenta al **Consejo de Ministros**",
           ["Sin expediente: ordena ejecutar lo necesario o contrata libremente", "Sin requisitos formales, ni siquiera el de crédito suficiente (se dota después)"],
           ["Dar cuenta al Consejo de Ministros: máximo **30 días**", "Inicio de la ejecución: máximo **un mes** desde el acuerdo; si se excede, procedimiento ordinario"],
           "Única contratación **verbal** admitida (art. 37.1) y sin **recurso especial** (art. 44.4, → VI.2.1).")),
], 2)

ap("s11", "II.3 Los pliegos (arts. 121, 122 y 124)", [
  "Los **pliegos** son las reglas del contrato: los **administrativos** (generales y particulares) fijan los derechos y obligaciones; los **técnicos**, cómo se ejecuta la prestación.",
  unidad("3.1 Pliegos de cláusulas administrativas generales (art. 121.1)",
    L(121, ["previo dictamen del Consejo de Estado"], solo=[1]),
    fichab("Pliegos de cláusulas administrativas generales",
           "El **Consejo de Ministros**, a iniciativa de los Ministerios interesados y a propuesta del Ministro de Hacienda y Función Pública",
           "Previo dictamen del **Consejo de Estado**; para los contratos de la AGE y de las entidades estatales que son Administración Pública",
           "—",
           "Generales: **Consejo de Ministros**; particulares: **órgano de contratación** (122.5).")),
  unidad("3.2 Pliego de cláusulas administrativas particulares (art. 122)",
    L(122, ["deberán aprobarse previamente a la autorización del gasto o conjuntamente con ella", "por error material, de hecho o aritmético", "cuyas cláusulas se consideran parte integrante de los mismos", "corresponderá al órgano de contratación", "informe previo del Servicio Jurídico respectivo"], solo=[1, 14, 15, 16, 17]),
    fichab("Pliego de cláusulas administrativas particulares (PCAP)",
           "Lo aprueba el **órgano de contratación**; en el Estado, con informe previo del **Servicio Jurídico** (salvo que se ajuste a un modelo ya informado)",
           ["Antes de la autorización del gasto o con ella, y siempre antes de la licitación", "Recoge criterios de solvencia y adjudicación, consideraciones sociales, laborales y ambientales y los derechos y obligaciones de las partes (122.2)", "Sus cláusulas son parte integrante del contrato"],
           "—",
           "Solo se modifica por **error material, de hecho o aritmético**; si no, **retroacción** de actuaciones. Cláusulas contrarias a los pliegos generales: informe previo de la **Junta Consultiva de Contratación Pública del Estado** (122.6).")),
  unidad("3.3 Pliego de prescripciones técnicas particulares (art. 124)",
    L(124, ["definan sus calidades"]),
    fichab("Pliego de prescripciones técnicas particulares (PPT)",
           "El **órgano de contratación**",
           "Rige la realización de la prestación y define sus calidades y sus condiciones sociales y ambientales",
           "Mismo momento que el PCAP: antes o con la autorización del gasto, y siempre antes de la licitación",
           "Mismo régimen de modificación que el PCAP: solo por error material, de hecho o aritmético.")),
  resumen([
    "Expediente: lo inicia el **órgano de contratación** motivando la **necesidad** (arts. 28 y 116); incluye pliegos, crédito y, en servicios, **insuficiencia de medios**; su aprobación **aprueba el gasto** (117).",
    "Menores: obras **< 40.000 €**, suministros y servicios **< 15.000 €**; informe, gasto y factura (118).",
    "Urgente: plazos **a la mitad** e inicio en **un mes** (119); emergencia: sin expediente, cuenta al **Consejo de Ministros** en **30 días** e inicio en **un mes** (120).",
    "Pliegos generales: **Consejo de Ministros** con dictamen del **Consejo de Estado**; particulares y técnicos: **órgano de contratación**, antes de la licitación; solo se corrigen errores materiales, de hecho o aritméticos."],
    "Siguiente: III. ¿Cómo se adjudica?"),
], 2)

# =============================================================================
T.ap("bIII", "III. ¿Cómo se adjudica el contrato?", donde(
  "Tercera pregunta: la **adjudicación**. Con el expediente aprobado, se elige al contratista por un **procedimiento** y unos **criterios**; después se adjudica, se notifica y se **formaliza**.",
  ["1 Procedimientos y criterios (arts. 131 y 145)", "2 Clasificación, adjudicación, notificación y formalización (arts. 150, 151 y 153)", "3 Abierto y abierto simplificado (arts. 156, 158 y 159)", "4 Restringido y procedimientos con negociación (arts. 160, 162, 166 y 168)", "5 Cuadro de procedimientos"]))

ap("s12", "III.1 Procedimientos y criterios de adjudicación (arts. 131 y 145)", [
  unidad("1.1 Procedimientos de adjudicación (art. 131)",
    L(131, ["utilizando el procedimiento abierto o el procedimiento restringido", "Los contratos menores podrán adjudicarse directamente"], solo=[1, 2, 3, 4]),
    fichab("Qué procedimiento se usa",
           "Administraciones Públicas",
           ["Ordinarios: **abierto** o **restringido**, con pluralidad de criterios (mejor relación calidad-precio)", "Negociado sin publicidad: supuestos del art. 168 (→ III.4.4)", "Diálogo competitivo o licitación con negociación: art. 167", "Asociación para la innovación: art. 177", "Menores: adjudicación directa (art. 118, → II.2.1)"],
           "—",
           "Los procedimientos con negociación, el diálogo y la asociación para la innovación solo caben en sus **supuestos tasados**.")),
  unidad("1.2 Criterios de adjudicación (art. 145.1 y 2)",
    L(145, ["mejor relación calidad-precio", "criterios económicos y cualitativos"], solo=[1, 2, 3]),
    fichab("Criterios de adjudicación",
           "Los fija el órgano de contratación en los pliegos y figuran en el anuncio (145.5)",
           ["Regla: **pluralidad** de criterios, mejor relación **calidad-precio**", "Criterios económicos y cualitativos (pueden incluir aspectos medioambientales o sociales)", "Previa justificación: mejor relación coste-eficacia (precio o coste del ciclo de vida)"],
           "—",
           "Los criterios deben estar **vinculados al objeto del contrato** y formularse de manera objetiva (145.5 y 6).")),
], 2)

ap("s13", "III.2 Clasificación, adjudicación, notificación y formalización (arts. 150, 151 y 153)", [
  unidad("2.1 Clasificación de las ofertas y adjudicación (art. 150)",
    L(150, ["por orden decreciente", "dentro del plazo de diez días hábiles", "3 por ciento del presupuesto base de licitación, IVA excluido", "dentro de los cinco días hábiles siguientes a la recepción de la documentación", "No podrá declararse desierta una licitación"], solo=[1, 2, 11, 12, 13, 14, 15]),
    fichab("Del examen de las ofertas a la adjudicación",
           "La **mesa de contratación** (o el órgano de contratación) clasifica; el **órgano de contratación** adjudica",
           ["Clasificación de las proposiciones por orden decreciente", "Requerimiento al mejor licitador: documentación y garantía definitiva", "Si no cumplimenta: se entiende que retira la oferta, paga el 3 % del presupuesto base (sin IVA) y se pasa al siguiente"],
           ["Documentación: **10 días hábiles** desde el requerimiento", "Adjudicación: **5 días hábiles** desde la recepción de la documentación"],
           "No cabe declarar **desierta** la licitación si hay alguna oferta admisible. Con el precio como único criterio, la mejor oferta es la de **precio más bajo**.")),
  unidad("2.2 Resolución y notificación de la adjudicación (art. 151.1)",
    L(151, ["deberá ser motivada", "en el plazo de 15 días"], solo=[1]),
    fichab("Resolución de adjudicación",
           "Órgano de contratación",
           "Motivada; se notifica a candidatos y licitadores y se publica en el perfil de contratante",
           "Publicación en el perfil: **15 días**",
           "La notificación debe permitir interponer un **recurso suficientemente fundado** (151.2) e indicar el plazo de formalización.")),
  unidad("2.3 Formalización (art. 153)",
    L(153, ["en documento administrativo", "quince días hábiles desde que se remita la notificación de la adjudicación", "en plazo no superior a cinco días", "no más tarde de los quince días hábiles siguientes", "no podrá procederse a la ejecución del contrato con carácter previo a su formalización"], solo=[1, 2, 4, 5, 6, 7, 10]),
    fichab("Formalización del contrato",
           "Órgano de contratación y adjudicatario (que puede pedir escritura pública a su costa)",
           ["Documento administrativo, título suficiente para acceder a cualquier registro público", "Sin cláusulas que alteren los términos de la adjudicación", "Basados en un acuerdo marco: no requieren formalización"],
           ["Si cabe recurso especial: no antes de **15 días hábiles** desde la notificación; después, formalización en **5 días** desde el requerimiento", "Si no cabe: no más tarde de **15 días hábiles** desde la notificación", "No formalización imputable al adjudicatario: penalidad del **3 %** del presupuesto base (sin IVA)"],
           "Sin formalización **no hay ejecución** (salvo menores, basados y emergencia). Las CC. AA. pueden ampliar el plazo de espera hasta un mes.")),
], 2)

ap("s14", "III.3 El procedimiento abierto y el abierto simplificado (arts. 156, 158 y 159)", [
  unidad("3.1 Procedimiento abierto: delimitación y plazos (art. 156)",
    L(156, ["todo empresario interesado podrá presentar una proposición", "quedando excluida toda negociación", "no será inferior a treinta y cinco días", "no será inferior a quince días", "como mínimo, de veintiséis días"], solo=[1, 2, 9]),
    fichab("Procedimiento abierto",
           "**Todo empresario interesado** presenta proposición",
           "Sin negociación de los términos del contrato",
           ["Armonizados: al menos **35 días** (obras, suministros y servicios) o **30** (concesiones), desde el envío del anuncio a la Oficina de Publicaciones de la UE", "No armonizados de las AAPP: al menos **15 días** desde el día siguiente a la publicación en el perfil; obras y concesiones, al menos **26 días**"],
           "El plazo SARA se cuenta desde el **envío** a la Oficina de Publicaciones de la UE; el no SARA, desde la **publicación en el perfil de contratante**. El SARA puede reducirse (156.3: información previa, urgencia, medios electrónicos).")),
  unidad("3.2 Plazo para adjudicar (art. 158)",
    L(158, ["en el plazo máximo de quince días", "será de dos meses", "tendrán derecho a retirar su proposición"], solo=[1, 2, 5]),
    fichab("Plazo máximo de adjudicación en el abierto",
           "Órgano de contratación",
           "Se cuenta desde la apertura de las proposiciones",
           ["Precio como único criterio: **15 días**", "Pluralidad de criterios (o solo el coste del ciclo de vida): **2 meses**, salvo otro plazo en el pliego"],
           "Si no se adjudica a tiempo, los licitadores pueden **retirar** su proposición y recuperar la garantía provisional.")),
  unidad("3.3 Procedimiento abierto simplificado (art. 159)",
    L(159, ["igual o inferior a 2.000.000 de euros", "veinticinco por ciento", "únicamente precisará de publicación en el perfil de contratante", "En los contratos de obras el plazo será como mínimo de veinte días", "No procederá la constitución de garantía provisional", "inferior a 80.000 euros", "inferior a 60.000 euros", "Se eximirá a los licitadores de la acreditación de la solvencia", "No se requerirá la constitución de garantía definitiva."], solo=[1, 2, 3, 4, 5, 8, 29, 30, 31, 36]),
    fichab("Procedimiento abierto simplificado y su tramitación sumaria (159.6)",
           "Órgano de contratación (es potestativo: «podrán acordar»); licitadores inscritos en el Registro Oficial de Licitadores y Empresas Clasificadas del Sector Público (o registro autonómico)",
           ["Anuncio solo en el perfil de contratante", "Sin garantía provisional", "159.6: sin solvencia y sin garantía definitiva; oferta en un único sobre valorada por fórmulas"],
           ["Obras: **≤ 2.000.000 €**; suministros y servicios: **< umbral SARA de la AGE** (140.000 €, arts. 21.1 a y 22.1 a)", "Criterios de juicio de valor: **≤ 25 %** (≤ 45 % en prestaciones intelectuales)", "Proposiciones: al menos **15 días** (obras, **20**)", "159.6: obras **< 80.000 €**, suministros y servicios **< 60.000 €**; proposiciones, al menos **10 días hábiles**"],
           "Obras: «igual **o inferior**» a 2.000.000 €; en el 159.6, «**inferior**» a 80.000/60.000 €. El 159.6 no se aplica a las prestaciones de carácter **intelectual**.")),
], 2)

ap("s15", "III.4 Procedimiento restringido y procedimientos con negociación (arts. 160, 162, 166 y 168)", [
  unidad("4.1 Procedimiento restringido (art. 160)",
    L(160, ["solicitud de participación", "en atención a su solvencia, sean seleccionados por el órgano de contratación", "estará prohibida toda negociación"], solo=[1, 2, 4, 5]),
    fichab("Procedimiento restringido",
           "Cualquier empresa solicita participar; solo presentan proposición las **seleccionadas** por su solvencia",
           "Dos fases: solicitudes de participación → invitación a los seleccionados",
           "Mínimo de invitados: **cinco** (art. 162.2, → III.4.2)",
           "Sin negociación. Especialmente adecuado para servicios intelectuales de especial complejidad (consultoría, arquitectura, ingeniería).")),
  unidad("4.2 Selección de candidatos (art. 162.2)",
    L(162, ["que no podrá ser inferior a cinco"], solo=[2]),
    fichab("Número de candidatos invitados",
           "Órgano de contratación",
           "Fija en el anuncio un número mínimo (y, si quiere, un máximo)",
           "Mínimo: **cinco**; si cumplen menos, puede seguir con los que reúnan las condiciones",
           "Nunca puede invitar a quien **no haya solicitado** participar ni a quien no cumpla las condiciones.")),
  unidad("4.3 Procedimientos con negociación (art. 166.1 y 3)",
    L(166, ["tras negociar las condiciones del contrato con uno o varios candidatos", "deberán publicar un anuncio de licitación"], solo=[1, 4]),
    fichab("Procedimientos con negociación",
           "Órgano de contratación; adjudica al licitador justificadamente elegido",
           "Negocia las condiciones del contrato con uno o varios candidatos",
           "—",
           "Regla: **con anuncio** (licitación con negociación, art. 167); **sin** anuncio solo en los casos excepcionales del art. 168.")),
  unidad("4.4 Negociado sin publicidad (art. 168 a y b)",
    L(168, ["únicamente en los siguientes casos", "No se haya presentado ninguna oferta", "Una imperiosa urgencia resultante de acontecimientos imprevisibles"], solo=[1, 2, 3, 5, 7, 8]),
    fichab("Negociado sin publicidad: supuestos tasados",
           "Órgano de contratación",
           ["::Entre otros:", "Abierto o restringido sin ofertas o sin ofertas adecuadas, sin modificar sustancialmente las condiciones ni incrementar el presupuesto base", "Un único empresario posible: obra de arte o actuación artística única, falta de competencia técnica, derechos exclusivos", "Contrato secreto o reservado", "Imperiosa urgencia imprevisible y no imputable al órgano (obras, suministros y servicios)", "Supuestos propios del suministro, de los servicios y de la repetición de obras o servicios (168 c a e)"],
           "—",
           "«**Únicamente**» en esos casos. La imperiosa urgencia solo cabe cuando la tramitación urgente del art. 119 **no basta**.")),
], 2)

ap("s16", "III.5 Cuadro de procedimientos (esquema)", [
  ESQ,
  """| Procedimiento | Artículos | Quién presenta oferta | Rasgo y cifras que se preguntan |
|---|---|---|---|
| Abierto | 156 a 158 | Todo empresario interesado | Sin negociación; SARA ≥ 35 días (concesiones ≥ 30); no SARA ≥ 15 días (obras y concesiones ≥ 26); adjudicar en 15 días (solo precio) o 2 meses |
| Abierto simplificado | 159 | Inscritos en el Registro Oficial de Licitadores | Obras ≤ 2.000.000 €; suministros y servicios < 140.000 €; juicio de valor ≤ 25 %; sin garantía provisional |
| Simplificado sumario | 159.6 | Ídem | Obras < 80.000 €; suministros y servicios < 60.000 €; ≥ 10 días hábiles; sin solvencia ni garantía definitiva |
| Restringido | 160 a 162 | Los seleccionados por su solvencia | Mínimo cinco invitados; sin negociación |
| Licitación con negociación | 166 y 167 | Los candidatos | Con anuncio; supuestos del 167 |
| Negociado sin publicidad | 166 y 168 | Los invitados | Sin anuncio; «únicamente» los supuestos del 168 |
| Contrato menor | 118 y 131.3 | Adjudicación directa | Obras < 40.000 €; suministros y servicios < 15.000 €; máximo un año, sin prórroga |""",
  resumen([
    "Procedimientos ordinarios: **abierto** y **restringido**, con pluralidad de criterios (mejor relación **calidad-precio**) (131 y 145).",
    "Requerimiento al mejor licitador: **10 días hábiles**; adjudicación: **5 días hábiles**; publicación: **15 días**; no cabe declarar **desierta** la licitación si hay alguna oferta admisible (150 y 151).",
    "Formalización: si cabe recurso especial, espera de **15 días hábiles** y después **5 días**; si no, como máximo **15 días hábiles**; penalidad del **3 %** (153).",
    "Abierto simplificado: obras **≤ 2.000.000 €**, juicio de valor **≤ 25 %**; sumario: obras **< 80.000 €** y suministros y servicios **< 60.000 €** (159).",
    "Restringido: mínimo **cinco** invitados (162); negociado sin publicidad: **únicamente** los supuestos del 168."],
    "Siguiente: IV. Efectos, cumplimiento y extinción"),
], 2)

# =============================================================================
T.ap("bIV", "IV. ¿Qué efectos tiene el contrato y cómo se cumple y se extingue?", donde(
  "Cuarta pregunta: la **vida del contrato administrativo** una vez formalizado. Se cumple a tenor de sus cláusulas, pero la Administración tiene **prerrogativas**; hay reglas sobre penalidades, riesgo y pago, y el contrato termina por **cumplimiento** o por **resolución**.",
  ["1 Régimen de los efectos y prerrogativas (arts. 188 a 191)", "2 Ejecución: penalidades, daños, riesgo y ventura y pago (arts. 192, 193 y 196 a 198)", "3 Extinción: cumplimiento y resolución (arts. 209 a 213)"]))

ap("s17", "IV.1 Efectos: régimen jurídico y prerrogativas (arts. 188 a 191)", [
  unidad("1.1 Régimen de los efectos y vinculación al contrato (arts. 188 y 189)",
    L(188),
    L(189, ["a tenor de sus cláusulas"]),
    fichab("Qué rige los efectos del contrato administrativo",
           "—",
           "Las normas del art. 25.2 (LCSP y su desarrollo; supletoriamente, derecho administrativo y privado) y los pliegos",
           "—",
           "Los contratos se cumplen **a tenor de sus cláusulas**, sin perjuicio de las **prerrogativas** de la Administración (→ IV.1.2).")),
  unidad("1.2 Prerrogativas (art. 190)",
    L(190, ["interpretar los contratos administrativos, resolver las dudas que ofrezca su cumplimiento, modificarlos por razones de interés público, declarar la responsabilidad imputable al contratista a raíz de la ejecución del contrato, suspender la ejecución del mismo, acordar su resolución y determinar los efectos de esta"], solo=[1]),
    fichab("Prerrogativas de la Administración",
           "El **órgano de contratación**",
           ["Interpretar el contrato", "Resolver las dudas sobre su cumplimiento", "Modificarlo por razones de interés público", "Declarar la responsabilidad del contratista", "Suspender la ejecución", "Acordar la resolución y determinar sus efectos"],
           "—",
           "Tiene también facultades de **inspección**, sin un derecho general a inspeccionar las instalaciones del contratista (190, párrafo segundo).")),
  unidad("1.3 Procedimiento de ejercicio (art. 191)",
    L(191, ["deberá darse audiencia al contratista", "cuando se formule oposición por parte del contratista", "superior a un 20 por ciento del precio inicial del contrato, IVA excluido, y su precio sea igual o superior a 6.000.000 de euros", "igual o superior a 50.000 euros", "pondrán fin a la vía administrativa y serán inmediatamente ejecutivos"]),
    fichab("Cómo se ejercen las prerrogativas",
           "Órgano de contratación; informe del **Servicio Jurídico** (sector público estatal); dictamen del **Consejo de Estado** u órgano consultivo autonómico equivalente en los casos del 191.3",
           ["Audiencia al contratista", "Dictamen preceptivo: interpretación, nulidad y resolución con **oposición** del contratista; modificaciones no previstas de más del 20 % con precio de 6.000.000 € o más; reclamaciones por responsabilidad contractual de 50.000 € o más"],
           "—",
           "Los acuerdos **ponen fin a la vía administrativa** y son **inmediatamente ejecutivos**. Sin **oposición** del contratista no hace falta el dictamen para interpretar o resolver.")),
], 2)

ap("s18", "IV.2 Ejecución: penalidades, daños, riesgo y ventura y pago (arts. 192, 193 y 196 a 198)", [
  unidad("2.1 Cumplimiento defectuoso: penalidades (art. 192.1)",
    L(192, ["no podrán ser superiores al 10 por ciento del precio del contrato, IVA excluido, ni el total de las mismas superar el 50 por cien del precio del contrato"], solo=[1]),
    fichab("Penalidades por cumplimiento defectuoso o incumplimiento de compromisos",
           "Las prevén los pliegos; las impone el órgano de contratación",
           "Proporcionales a la gravedad del incumplimiento",
           ["Cada penalidad: máximo **10 %** del precio (sin IVA)", "Total: máximo **50 %** del precio"],
           "Ante un incumplimiento **parcial** imputable al contratista, la Administración puede optar por **resolver** o **penalizar** (192.2).")),
  unidad("2.2 Demora en la ejecución (art. 193)",
    L(193, ["no precisará intimación previa", "0,60 euros por cada 1.000 euros del precio del contrato", "múltiplo del 5 por 100 del precio del contrato"], solo=[1, 2, 3, 5]),
    fichab("Demora del contratista",
           "El contratista debe cumplir el plazo total y los parciales",
           "La Administración opta: **resolución** o **penalidades diarias**",
           ["**0,60 €** por cada **1.000 €** del precio (sin IVA), por día", "Cada vez que las penalidades alcanzan un múltiplo del **5 %** del precio: puede resolver o seguir con nuevas penalidades"],
           "La mora **no requiere intimación** previa. El pliego puede fijar otras penalidades si se justifica (193.3).")),
  unidad("2.3 Daños a terceros (art. 196)",
    L(196, ["Será obligación del contratista indemnizar todos los daños y perjuicios que se causen a terceros", "consecuencia inmediata y directa de una orden de la Administración", "dentro del año siguiente a la producción del hecho"], solo=[1, 2, 3]),
    fichab("Responsabilidad por daños a terceros",
           "Regla: el **contratista**; la **Administración**, si derivan de una orden suya inmediata y directa o de vicios del proyecto",
           "Los terceros pueden pedir al órgano de contratación que, oído el contratista, informe sobre a quién corresponde la responsabilidad",
           "Requerimiento: dentro del **año** siguiente al hecho; interrumpe la prescripción",
           "La orden de la Administración debe ser causa **inmediata y directa** del daño.")),
  unidad("2.4 Riesgo y ventura (art. 197)",
    L(197, ["a riesgo y ventura del contratista"]),
    fichab("Principio de riesgo y ventura",
           "El **contratista** asume el riesgo de la ejecución",
           "—",
           "—",
           "Salvedad: lo establecido para el contrato de **obras** en el art. 239 (fuerza mayor; tema IV.6).")),
  unidad("2.5 Pago del precio (art. 198.4 a 6)",
    L(198, ["dentro de los treinta días siguientes a la fecha de aprobación de las certificaciones de obra", "superior a cuatro meses", "superior a seis meses"], solo=[1, 6, 9, 10]),
    fichab("Pago del precio y demora de la Administración",
           "La Administración paga; el contratista debe presentar la factura en plazo",
           "Abono total o parcial, a cuenta o en cada vencimiento (198.2)",
           ["Pago: **30 días** desde la aprobación de certificaciones o documentos de conformidad; después, intereses de demora", "Demora de más de **4 meses**: el contratista puede suspender (con un mes de preaviso)", "Demora de más de **6 meses**: puede resolver y ser resarcido"],
           "Escalera **30 días → 4 meses → 6 meses**. Las CC. AA. pueden reducir esos plazos (198.8).")),
], 2)

ap("s19", "IV.3 Extinción: cumplimiento y resolución (arts. 209 a 213)", [
  unidad("3.1 Formas de extinción (art. 209)",
    L(209, ["por su cumplimiento o por resolución"]),
    fichab("Cómo se extingue el contrato",
           "—",
           "Dos formas: **cumplimiento** o **resolución**",
           "—",
           "La invalidez no es una forma de extinción del art. 209: se estudia aparte (→ VI.1).")),
  unidad("3.2 Cumplimiento y recepción (art. 210.1 a 3)",
    L(210, ["a satisfacción de la Administración, la totalidad de la prestación", "dentro del mes siguiente a la entrega o realización del objeto del contrato", "plazo de garantía"], solo=[1, 2, 3]),
    fichab("Cumplimiento y recepción",
           "El contratista cumple; la Administración recibe (la Intervención puede asistir)",
           "Acto formal y positivo de recepción o conformidad",
           ["Recepción: **un mes** desde la entrega (u otro plazo del pliego)", "Plazo de garantía desde la recepción; liquidación en **30 días** desde el acta, salvo obras (210.4)"],
           "Transcurrido el plazo de garantía sin objeciones, queda **extinguida la responsabilidad** del contratista.")),
  unidad("3.3 Causas de resolución (art. 211)",
    L(211, ["El mutuo acuerdo entre la Administración y el contratista.", "un plazo superior a un tercio del plazo de duración inicial del contrato", "en cuantía superior, en más o en menos, al 20 por ciento del precio inicial del contrato", "la que haya aparecido con prioridad en el tiempo"], solo=[1, 2, 3, 4, 5, 6, 7, 8, 12, 13, 14, 15]),
    fichab("Causas de resolución",
           "—",
           ["Muerte, incapacidad o extinción de la personalidad del contratista", "Concurso o insolvencia", "Mutuo acuerdo", "Demora del contratista (retraso de más de un tercio del plazo inicial sobre el plan de trabajos)", "Demora de la Administración en el pago (más de 6 meses)", "Incumplimiento de la obligación principal (u obligaciones esenciales tipificadas)", "Imposibilidad de ejecutar sin poder modificar, o modificaciones del 205 de más del 20 %", "Las específicas de cada tipo de contrato", "Impago de salarios o incumplimiento de convenios"],
           "—",
           "Si concurren varias causas, se atiende a la que apareció **primero en el tiempo** (211.2).")),
  unidad("3.4 Aplicación de las causas (art. 212)",
    L(212, ["de oficio o a instancia del contratista", "darán siempre lugar a la resolución del contrato", "solo podrá tener lugar cuando no concurra otra causa de resolución que sea imputable al contratista", "ocho meses"], solo=[1, 3, 7, 14]),
    fichab("Cómo se acuerda la resolución",
           "El **órgano de contratación**, de oficio o a instancia del contratista",
           ["Insolvencia y modificaciones sin los requisitos de los arts. 204 y 205: resolución **siempre**", "Mutuo acuerdo: solo sin otra causa imputable al contratista y por razones de interés público"],
           "Expediente: instruido y resuelto en un máximo de **ocho meses**",
           "La resolución por mutuo acuerdo es **subsidiaria**: no cabe si hay otra causa imputable al contratista.")),
  unidad("3.5 Efectos de la resolución (art. 213.1 a 4)",
    L(213, ["le será incautada la garantía", "indemnización del 3 por ciento del importe de la prestación dejada de realizar"], solo=[1, 2, 3, 4]),
    fichab("Efectos de la resolución",
           "—",
           ["Mutuo acuerdo: lo válidamente estipulado", "Incumplimiento de la Administración: daños y perjuicios al contratista", "Incumplimiento culpable del contratista: **incautación de la garantía** e indemnización de lo que exceda", "Causa del 211.1 g): indemnización del **3 %** de la prestación dejada de realizar"],
           "—",
           "El acuerdo de resolución se pronuncia **siempre** sobre la garantía (213.5).")),
  resumen([
    "Efectos: normas del 25.2 y pliegos; el contrato se cumple a tenor de sus cláusulas, con las **prerrogativas** del órgano de contratación: interpretar, resolver dudas, modificar, declarar responsabilidad, suspender y resolver (188 a 190).",
    "Prerrogativas: audiencia al contratista; **Consejo de Estado** si hay oposición (interpretación, nulidad, resolución) y en los casos de 191.3; los acuerdos **agotan la vía administrativa** (191).",
    "Penalidades: **10 %** cada una y **50 %** en total; demora: **0,60 € por cada 1.000 €** diarios y cada **5 %**, opción de resolver (192 y 193).",
    "Riesgo y ventura del **contratista** (197); pago en **30 días**; suspensión a los **4 meses**; resolución a los **6 meses** (198).",
    "Extinción por **cumplimiento** (recepción en **un mes**) o **resolución** (causas del 211; expediente en **ocho meses**; incautación de la garantía si hay culpa del contratista)."],
    "Siguiente: V. La revisión de precios y otras alteraciones contractuales"),
], 2)

# =============================================================================
T.ap("bV", "V. ¿Cómo se revisan los precios y qué otras alteraciones caben?", donde(
  "Quinta pregunta, la tercera frase del epígrafe. Durante la ejecución el contrato puede **alterarse** por vías tasadas: la **revisión de precios**, la **modificación**, la **suspensión**, la **cesión** y la **subcontratación**.",
  ["1 La revisión de precios (arts. 103 a 105)", "2 La modificación del contrato (arts. 203 a 207)", "3 Suspensión, cesión y subcontratación (arts. 208, 214 y 215)"]))

ap("s20", "V.1 La revisión de precios (arts. 103 a 105)", [
  unidad("1.1 Procedencia y límites (art. 103)",
    L(103, ["revisión periódica y predeterminada", "igual o superior a cinco años", "al menos, en el 20 por ciento de su importe y hubiese transcurrido un año desde su formalización", "El Instituto Nacional de Estadística elaborará los índices mensuales"], solo=[1, 2, 4, 7, 8, 9, 15]),
    fichab("Revisión de precios",
           "La establece el **órgano de contratación** en el pliego, con su fórmula; los índices los elabora el **INE** y se aprueban por Orden del Ministro de Hacienda y Función Pública, previo informe del Comité Superior de Precios de Contratos del Estado",
           ["Solo **periódica y predeterminada**", "Contratos: obra, suministro de fabricación de armamento y equipamiento, suministro de energía y aquellos con recuperación de la inversión de cinco años o más (103.2)", "Fórmula invariable durante la vigencia del contrato (103.4)"],
           ["Requisitos: ejecutado al menos el **20 %** y transcurrido **un año** desde la formalización (salvo suministro de energía)", "El primer 20 % y el primer año quedan **excluidos** de la revisión"],
           "No son revisables las amortizaciones, los costes financieros, los gastos generales o de estructura ni el beneficio industrial (103.2). Cayó en 2025: los índices los elabora el **INE** (→ Cierre 1).")),
  unidad("1.2 Revisión con demora del contratista (art. 104)",
    L(104, ["salvo que los correspondientes al período real de ejecución produzcan un coeficiente inferior"]),
    fichab("Revisión en periodos de mora del contratista",
           "—",
           "Se aplican los índices de las fechas previstas en el contrato, salvo que los del período real den un coeficiente inferior",
           "—",
           "La mora **no beneficia** al contratista: se aplica el coeficiente **menor**.")),
  unidad("1.3 Pago de la revisión (art. 105)",
    L(105, ["de oficio"]),
    fichab("Pago del importe de la revisión",
           "La Administración, **de oficio**",
           "Abono o descuento en las certificaciones o pagos parciales; expediente de gasto al comienzo del ejercicio",
           "Desajustes: en la certificación final o en la liquidación",
           "No requiere solicitud del contratista: es **de oficio**, y puede ser al alza (abono) o a la baja (descuento).")),
], 2)

ap("s21", "V.2 La modificación del contrato (arts. 203 a 207)", [
  unidad("2.1 Potestad de modificación (art. 203.1 y 2)",
    L(203, ["solo podrán ser modificados por razones de interés público", "deberá procederse a su resolución y a la celebración de otro"], solo=[1, 2, 3, 4, 5]),
    fichab("Potestad de modificación",
           "Órgano de contratación (procedimiento del art. 191, con las particularidades del 207)",
           ["Prevista en el pliego (art. 204)", "No prevista, excepcionalmente, si cumple el art. 205"],
           "Durante la vigencia del contrato",
           "Fuera de esos casos: **resolver** y celebrar otro contrato. Sucesión del contratista, cesión, revisión de precios y ampliación del plazo tienen su propio régimen (203.1).")),
  unidad("2.2 Modificaciones previstas en el pliego (art. 204)",
    L(204, ["hasta un máximo del veinte por ciento del precio inicial", "alterar la naturaleza global del contrato inicial"], solo=[1, 2, 3, 5]),
    fichab("Modificaciones previstas en el PCAP",
           "Órgano de contratación, si el pliego lo advirtió expresamente",
           "Cláusula clara, precisa e inequívoca: alcance, límites, naturaleza, condiciones objetivas y procedimiento; sin nuevos precios unitarios",
           "Máximo **20 %** del precio inicial",
           "Nunca puede alterar la **naturaleza global** del contrato (sustituir el objeto o cambiar el tipo de contrato).")),
  unidad("2.3 Modificaciones no previstas (art. 205)",
    L(205, ["del 50 por ciento de su precio inicial, IVA excluido", "una Administración diligente no hubiera podido prever", "Cuando las modificaciones no sean sustanciales", "del 15 por ciento del precio inicial del mismo, IVA excluido, si se trata del contrato de obras o de un 10 por ciento"], solo=[1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 21]),
    fichab("Modificaciones no previstas: tres supuestos tasados",
           "Órgano de contratación",
           ["Solo las variaciones **estrictamente indispensables** (205.1 b)", "a) Prestaciones adicionales cuando el cambio de contratista no es posible", "b) Circunstancias sobrevenidas e imprevisibles", "c) Modificaciones no sustanciales"],
           ["a) y b): máximo **50 %** del precio inicial (sin IVA)", "c): es sustancial, entre otros casos, si supera el **15 %** (obras) o el **10 %** (demás contratos) del precio inicial"],
           "En b), la imprevisibilidad se mide con una **Administración diligente**, y la modificación no puede alterar la naturaleza global del contrato.")),
  unidad("2.4 Obligatoriedad para el contratista (art. 206)",
    L(206, ["no exceda del 20 por ciento del precio inicial del contrato"]),
    fichab("Cuándo obliga la modificación al contratista",
           "—",
           "Las del art. 205 son obligatorias si no exceden del 20 %; si exceden, requieren conformidad por escrito del contratista o se resuelve el contrato (211.1 g)",
           "**20 %** del precio inicial, sin IVA",
           "Más del 20 % sin conformidad → resolución con indemnización del **3 %** de la prestación no realizada (art. 213.4, → IV.3.5).")),
  unidad("2.5 Especialidades de procedimiento (art. 207.2 y 3)",
    L(207, ["en un plazo no inferior a tres días", "en el plazo de 5 días desde la aprobación de la misma"], solo=[2, 4]),
    fichab("Especialidades procedimentales",
           "Órgano de contratación; audiencia al redactor del proyecto o de las especificaciones si es un tercero",
           ["Audiencia al redactor (modificaciones del 205): al menos 3 días", "Anuncio de modificación en el perfil de contratante, siempre, con las alegaciones e informes"],
           "Publicación en el perfil: **5 días** desde la aprobación",
           "Las armonizadas modificadas por el 205.2 a) y b) se anuncian además en el **DOUE** (207.3).")),
], 2)

ap("s22", "V.3 Suspensión, cesión y subcontratación (arts. 208, 214 y 215)", [
  unidad("3.1 Suspensión (art. 208)",
    L(208, ["se extenderá un acta", "prescribe en un año"]),
    fichab("Suspensión del contrato",
           "La acuerda la Administración, o se produce por la demora en el pago de más de 4 meses (198.5)",
           ["Acta de oficio o a solicitud del contratista", "La Administración abona los daños y perjuicios efectivamente sufridos, por los conceptos tasados (salvo otra cosa en el pliego)"],
           "Reclamación: prescribe en **un año** desde la orden de reanudar",
           "Solo se indemnizan los periodos **documentados en el acta**.")),
  unidad("3.2 Cesión (art. 214)",
    L(214, ["cuando obedezca a una opción inequívoca de los pliegos", "El plazo para la notificación de la resolución sobre la solicitud de autorización será de dos meses", "al menos un 20 por 100 del importe del contrato", "en escritura pública"], solo=[1, 4, 5, 6, 8, 9, 10]),
    fichab("Cesión del contrato",
           "Cedente (contratista), cesionario y órgano de contratación (autoriza)",
           ["Solo si los pliegos la prevén de forma inequívoca", "Autorización previa y expresa", "Cesionario con capacidad, solvencia (y clasificación, si se exigió) y sin prohibición de contratar", "Escritura pública"],
           ["Autorización: **2 meses**; silencio **positivo**", "Cedente: ejecutado al menos el **20 %** (concesiones: explotación durante una **quinta parte** del plazo)"],
           "El cesionario queda **subrogado** en todos los derechos y obligaciones. No cabe si las cualidades del cedente fueron determinantes de la adjudicación (214.1).")),
  unidad("3.3 Subcontratación (art. 215)",
    L(215, ["realización parcial de la prestación", "una penalidad de hasta un 50 por 100 del importe del subcontrato", "Los subcontratistas quedarán obligados solo ante el contratista principal", "tendrán en todo caso naturaleza privada", "no tendrán acción directa frente a la Administración contratante"], solo=[1, 3, 5, 13, 14, 16, 20, 21]),
    fichab("Subcontratación",
           "Contratista principal y subcontratistas",
           ["Realización **parcial**, según los pliegos", "Comunicación escrita al órgano de contratación, a más tardar al iniciar la ejecución", "Los pliegos pueden reservar tareas críticas al contratista principal (215.2 e)"],
           "Infracción: penalidad de hasta el **50 %** del subcontrato o resolución, si lo prevén los pliegos",
           "Los subcontratos son **privados**; el subcontratista responde solo ante el contratista y **no tiene acción directa** contra la Administración.")),
  resumen([
    "Revisión de precios: solo **periódica y predeterminada**; requiere el **20 %** ejecutado y **un año** desde la formalización; índices del **INE**; se paga **de oficio** (103 a 105).",
    "Modificación: por **interés público**; prevista en el pliego hasta el **20 %** (204) o no prevista en los tres supuestos del 205 (adicionales e imprevisibles hasta el **50 %**; no sustanciales).",
    "Obligatoria para el contratista hasta el **20 %**; por encima, conformidad escrita o resolución (206).",
    "Suspensión con **acta**; cesión con autorización (**2 meses**, silencio positivo) y **20 %** ejecutado; subcontratación **parcial**, privada y sin acción directa contra la Administración."],
    "Siguiente: VI. Régimen de invalidez y recursos"),
], 2)

# =============================================================================
T.ap("bVI", "VI. ¿Cuándo es inválido el contrato y cómo se recurre?", donde(
  "Sexta pregunta, la última frase del epígrafe: **régimen de invalidez y recursos**. La invalidez administrativa nace de los vicios de la preparación o de la adjudicación; el **recurso especial en materia de contratación** permite atacarlos antes de que el contrato se formalice.",
  ["1 Invalidez: nulidad, anulabilidad, revisión de oficio y efectos (arts. 38 a 43)", "2 Recurso especial: actos recurribles y órgano (arts. 44 y 45)", "3 Tramitación y resolución del recurso especial (arts. 48 a 50, 53 y 57 a 59)"]))

ap("s23", "VI.1 Invalidez de los contratos (arts. 38 a 43)", [
  unidad("1.1 Supuestos de invalidez (art. 38)",
    L(38, ["serán inválidos"]),
    fichab("Tres vías de invalidez",
           "Contratos de los poderes adjudicadores (y subvencionados del art. 23)",
           ["Causas de derecho civil (a)", "Causas de derecho administrativo en los actos preparatorios o del procedimiento de adjudicación (b)", "Ilegalidad del clausulado (c)"],
           "—",
           "La invalidez **administrativa** procede de los **actos preparatorios o de adjudicación**.")),
  unidad("1.2 Causas de nulidad de derecho administrativo (art. 39.1 y 2 a a c)",
    L(39, ["las indicadas en el artículo 47 de la Ley 39/2015", "La carencia o insuficiencia de crédito", "salvo los supuestos de emergencia", "La falta de publicación del anuncio de licitación"], solo=[1, 2, 3, 4, 5]),
    fichab("Causas de nulidad de derecho administrativo",
           "—",
           ["Las del art. 47 de la Ley 39/2015", "Falta de capacidad, solvencia, habilitación o clasificación; prohibición de contratar", "Carencia o insuficiencia de crédito (salvo emergencia)", "Falta de publicación del anuncio de licitación en el medio preceptivo", "Otras (letras d a h): formalización sin respetar plazos o la suspensión del recurso especial, incumplimientos en contratos basados, incumplimiento grave declarado por el TJUE, omisiones del pliego"],
           "—",
           "La falta de **crédito** es **nulidad** (no anulabilidad), salvo en la **emergencia**.")),
  unidad("1.3 Causas de anulabilidad (art. 40)",
    L(40, ["las demás infracciones del ordenamiento jurídico", "en los artículos 204 y 205"], solo=[1, 2, 3, 4, 5]),
    fichab("Causas de anulabilidad",
           "—",
           ["Las demás infracciones del ordenamiento (art. 48 de la Ley 39/2015)", "Modificaciones sin los requisitos de los arts. 204 y 205", "Ventajas a empresas que contrataron antes con cualquier Administración", "Encargos a medios propios sin los requisitos del art. 32"],
           "—",
           "Modificar sin cumplir los arts. 204 y 205 es **anulabilidad** (y, además, acto recurrible en recurso especial, art. 44.2 d).")),
  unidad("1.4 Revisión de oficio (art. 41.1 y 3)",
    L(41, ["Capítulo I del Título V de la Ley 39/2015", "el órgano de contratación"], solo=[1, 3]),
    fichab("Revisión de oficio de los actos preparatorios y de adjudicación",
           "Declara la nulidad o la lesividad el **órgano de contratación** (AAPP) o el titular del departamento u organismo de adscripción o tutela (entidades que no son AAPP)",
           "Conforme al capítulo I del título V de la Ley 39/2015",
           "—",
           "Esta competencia se entiende **delegada** con la de contratar, salvo la indemnización por nulidad, que resuelve el órgano delegante (41.4).")),
  unidad("1.5 Efectos de la nulidad (art. 42.1 a 3)",
    L(42, ["entrará en fase de liquidación", "La parte que resulte culpable deberá indemnizar", "grave trastorno al servicio público"], solo=[1, 2, 3]),
    fichab("Efectos de la declaración de nulidad",
           "—",
           ["Nulidad firme de actos preparatorios o de adjudicación → nulidad del contrato, que entra en **liquidación**", "Restitución recíproca (o su valor)", "La parte culpable indemniza a la otra", "La nulidad de actos no preparatorios solo afecta a esos actos (42.2)"],
           "—",
           "Si la nulidad causa un **grave trastorno al servicio público**, pueden mantenerse los efectos del contrato con sus cláusulas hasta adoptar medidas urgentes (42.3).")),
  unidad("1.6 Causas de invalidez de derecho civil (art. 43)",
    L(43, ["requisitos y plazos de ejercicio de las acciones establecidos en el ordenamiento civil"]),
    fichab("Invalidez por causas civiles",
           "—",
           "Requisitos y plazos: los del derecho civil; procedimiento, si contrata una Administración Pública: el de los actos y contratos administrativos anulables",
           "Los del ordenamiento civil",
           "Combinación: **plazos civiles** y **procedimiento administrativo**.")),
], 2)

ap("s24", "VI.2 El recurso especial en materia de contratación: actos recurribles y órgano (arts. 44 y 45)", [
  unidad("2.1 Contratos y actos recurribles (art. 44)",
    L(44, ["superior a tres millones de euros", "superior a cien mil euros", "por sus características no sea posible fijar su precio de licitación", "procedimientos de adjudicación que se sigan por el trámite de emergencia", "no procederá la interposición de recursos administrativos ordinarios", "tendrá carácter potestativo y será gratuito"], solo=[1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15, 16, 19]),
    fichab("Recurso especial: qué contratos y qué actos",
           "Contratos de las Administraciones Públicas y demás poderes adjudicadores",
           ["::Actos recurribles (44.2):", "Anuncios de licitación, pliegos y documentos contractuales", "Actos de trámite cualificados (incluidas la admisión o exclusión de licitadores y de ofertas)", "Acuerdos de adjudicación", "Modificaciones que debieron ser objeto de nueva adjudicación", "Encargos a medios propios que no cumplan los requisitos", "Acuerdos de rescate de concesiones"],
           ["Obras y concesiones: valor estimado **superior a 3.000.000 €**", "Suministros y servicios: **superior a 100.000 €**", "Administrativos especiales: si no puede fijarse su precio de licitación o si su valor estimado supera el fijado para los servicios"],
           "**Potestativo y gratuito**; excluye los recursos administrativos ordinarios; **no** cabe en la **emergencia**. Cayó en 2025 (→ Cierre 1).")),
  unidad("2.2 Órgano competente en el Estado (art. 45.1 y 5)",
    L(45, ["Tribunal Administrativo Central de Recursos Contractuales", "seis años y no podrá prorrogarse"], solo=[1, 15]),
    fichab("Quién resuelve en el sector público estatal",
           "El **Tribunal Administrativo Central de Recursos Contractuales** (TACRC), adscrito al Ministerio de Hacienda y Función Pública",
           "Plena independencia funcional; un Presidente y un mínimo de cinco vocales; al menos dos Secciones",
           "Mandato: **seis años**, improrrogable",
           "Las Comunidades Autónomas y las entidades locales tienen su propio régimen (art. 46).")),
], 2)

ap("s25", "VI.3 Tramitación y resolución del recurso especial (arts. 48 a 50, 53 y 57 a 59)", [
  unidad("3.1 Legitimación (art. 48)",
    L(48, ["cualquier persona física o jurídica cuyos derechos o intereses legítimos"]),
    fichab("Quién puede recurrir",
           "Cualquier persona física o jurídica con derechos o intereses legítimos afectados; también las organizaciones sindicales (incumplimientos sociales o laborales) y la organización empresarial sectorial representativa",
           "—",
           "—",
           "Basta un perjuicio o afectación **directa o indirecta**, actual o posible.")),
  unidad("3.2 Medidas cautelares (art. 49.1 y 2)",
    L(49, ["Antes de interponer el recurso especial", "dentro de los cinco días hábiles siguientes", "no cabrá recurso alguno"], solo=[1, 2, 3, 5]),
    fichab("Medidas cautelares",
           "Las piden los legitimados al órgano competente para resolver el recurso",
           "Incluso **antes** de recurrir; pueden suspender el procedimiento o decisiones del órgano de contratación",
           ["Decisión motivada: **5 días hábiles**", "Alegaciones del órgano de contratación: **2 días hábiles**"],
           "Contra la decisión sobre las medidas cautelares **no cabe recurso alguno** (sin perjuicio de recurrir la resolución principal).")),
  unidad("3.3 Plazo de interposición (art. 50.1 a y d)",
    L(50, ["en el plazo de quince días hábiles", "a partir del día siguiente a aquel en que se haya notificado esta"], solo=[1, 2, 8]),
    fichab("Cuándo se recurre",
           "El recurrente, por escrito",
           ["Contra el anuncio: desde el día siguiente a su publicación en el perfil de contratante", "Contra la adjudicación: desde el día siguiente a su notificación"],
           "**15 días hábiles** (plazos especiales para las nulidades del 39.2 c a f: 30 días o 6 meses, 50.2)",
           "Con carácter general, quien ya presentó oferta **no puede recurrir después los pliegos** (50.1 b).")),
  unidad("3.4 Suspensión automática (art. 53)",
    L(53, ["quedará en suspenso la tramitación del procedimiento cuando el acto recurrido sea el de adjudicación"]),
    fichab("Efecto suspensivo del recurso",
           "—",
           "Si se recurre la **adjudicación**, el procedimiento queda en suspenso",
           "—",
           "Excepto en los contratos basados en un acuerdo marco y los específicos de un sistema dinámico. La suspensión **automática** es solo para la **adjudicación**; para lo demás, medidas cautelares.")),
  unidad("3.5 Resolución y silencio (art. 57.1 y 5)",
    L(57, ["dentro de los cinco días hábiles siguientes", "Transcurridos dos meses"], solo=[1, 5]),
    fichab("Resolución del recurso",
           "El órgano competente (en el Estado, el TACRC)",
           "Estima total o parcialmente, desestima o inadmite, de forma motivada y congruente (57.2)",
           ["Resolver: **5 días hábiles** tras las alegaciones y, en su caso, la prueba", "Silencio: **2 meses** desde el día siguiente a la interposición"],
           "El silencio es **desestimatorio**, a efectos de interponer el recurso contencioso-administrativo.")),
  unidad("3.6 Multas por temeridad o mala fe (art. 58.2)",
    L(58, ["temeridad o mala fe", "entre 1.000 y 30.000 euros"], solo=[2, 3]),
    fichab("Multas al recurrente temerario",
           "El órgano que resuelve el recurso",
           "Si aprecia temeridad o mala fe en el recurso o en la solicitud de medidas cautelares",
           "Multa de **1.000 a 30.000 €**",
           "A solicitud del interesado, también puede imponer a la **entidad contratante** la obligación de **indemnizar** al recurrente (58.1).")),
  unidad("3.7 Efectos de la resolución (art. 59)",
    L(59, ["solo cabrá la interposición de recurso contencioso-administrativo", "directamente ejecutiva", "No procederá la revisión de oficio"], solo=[1, 2, 3]),
    fichab("Qué cabe contra la resolución",
           "—",
           "Solo **recurso contencioso-administrativo**; la resolución es **directamente ejecutiva**",
           "—",
           "Ni revisión de oficio ni fiscalización por los órganos de control interno (59.3).")),
  ESQ,
  """| Recurso especial | Dato | Artículo |
|---|---|---|
| Obras y concesiones | Valor estimado > 3.000.000 € | 44.1 |
| Suministros y servicios | Valor estimado > 100.000 € | 44.1 |
| Carácter | Potestativo y gratuito; excluye los recursos ordinarios | 44.5 y 7 |
| Excluido | Procedimientos tramitados por emergencia | 44.4 |
| Órgano estatal | TACRC (mandato de seis años) | 45 |
| Plazo | 15 días hábiles | 50.1 |
| Medidas cautelares | 5 días hábiles; sin recurso | 49.2 |
| Suspensión automática | Solo si se recurre la adjudicación | 53 |
| Resolución | 5 días hábiles; silencio negativo a los 2 meses | 57 |
| Multa por temeridad o mala fe | 1.000 a 30.000 € | 58.2 |
| Contra la resolución | Solo contencioso-administrativo | 59.1 |""",
  resumen([
    "Invalidez: civil, administrativa (actos preparatorios o de adjudicación) o por clausulado ilegal (38).",
    "Nulidad: las del art. 47 de la Ley 39/2015 más las del 39.2 (falta de capacidad o solvencia, **falta de crédito** salvo emergencia, falta de **anuncio**…); anulabilidad: las demás, y las modificaciones sin los arts. 204 y 205 (40).",
    "Revisión de oficio por el **órgano de contratación** (41); la nulidad firme lleva a la **liquidación** del contrato (42).",
    "Recurso especial: obras y concesiones **> 3.000.000 €**, suministros y servicios **> 100.000 €**; **potestativo y gratuito**; no en emergencia; TACRC; **15 días hábiles**; suspensión automática si se recurre la **adjudicación**; contra la resolución, **contencioso**."],
    "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test."),
], 2)

# =============================================================================
EX_L50 = examen("L", 50, {
  "a": f"El art. 44.1 exige que el valor estimado sea {C(44, 'superior a lo establecido para los contratos de servicios')}: «igual» no basta.",
  "b": f"Literal del art. 44.1, párrafo segundo: {C(44, 'por sus características no sea posible fijar su precio de licitación')}.",
  "c": "Es lo contrario de la ley: el valor estimado tiene que ser **superior**, no inferior, al fijado para los servicios.",
  "d": f"Cambia «precio de licitación» por «valor estimado». La ley dice {C(44, 'no sea posible fijar su precio de licitación')}."},
  [("no sea posible fijar su precio de licitación", "LCSP", A(44), "por sus características no sea posible fijar su precio de licitación")])
EX_L51 = examen("L", 51, {
  "a": f"La formalización es la regla general del art. 36.1, pero exceptúa expresamente {C(36, 'los contratos basados en un acuerdo marco')}.",
  "b": "El art. 36 no vincula la perfección de ningún contrato a su publicación en el Diario Oficial de la Unión Europea.",
  "c": f"Literal del art. 36.3: {C(36, 'Los contratos basados en un acuerdo marco y los contratos específicos en el marco de un sistema dinámico de adquisición, se perfeccionan con su adjudicación')}.",
  "d": f"Es la regla de los contratos subvencionados armonizados del art. 36.2, que {C(36, 'se perfeccionarán de conformidad con la legislación por la que se rijan')}."},
  [("Con su adjudicación", "LCSP", A(36), "se perfeccionan con su adjudicación")])
EX_L52 = examen("L", 52, {
  "a": f"Cambia el número de años: la ley dice {C(88, 'en el curso de los cinco últimos años')}.",
  "b": f"Literal del art. 88.1 a): {C(88, 'Relación de las obras ejecutadas en el curso de los cinco últimos años')}.",
  "c": f"Tres años es el periodo de otro medio de solvencia, la plantilla media {C(88, 'durante los tres últimos años')} (88.1 e).",
  "d": f"Cuatro años no aparece en el art. 88.1 a), que dice {C(88, 'cinco últimos años')} (o los {C(88, 'últimos diez años')} para garantizar la competencia)."},
  [("cinco últimos años", "LCSP", A(88), "Relación de las obras ejecutadas en el curso de los cinco últimos años")])
EX_P56 = examen("P", 56, {
  "a": f"Excluido: el art. 5.4 b) saca de la ley los contratos adjudicados {C(5, 'En virtud de un acuerdo o convenio internacional relativo al estacionamiento de tropas')}.",
  "b": f"Excluido: el art. 10 excluye los servicios financieros de {C(10, 'compra, venta o transferencia de valores o de otros instrumentos financieros')}.",
  "c": f"Excluido: el art. 11.5 excluye {C(11, 'los contratos que tengan por objeto servicios relacionados con campañas políticas')}, {C(11, 'cuando sean adjudicados por un partido político')}.",
  "d": f"Incluido: las Mutuas forman parte del sector público (art. 3.1 f: {C(3, 'Las Mutuas colaboradoras con la Seguridad Social')}) y su contrato de limpieza es un contrato oneroso de servicios (art. 2.1)."},
  [("Mutua colaboradora con la Seguridad Social", "LCSP", A(3), "f) Las Mutuas colaboradoras con la Seguridad Social.")])
EX_P57 = examen("P", 57, {
  "a": f"Sí armonizado: 5.410.000 € supera el umbral de obras, {C(20, 'igual o superior a 5.404.000 euros')} (art. 20.1).",
  "b": f"Sí armonizado: servicios de un Ministerio (AGE) de 158.500 €, por encima de {C(22, 'a) 140.000 euros, cuando los contratos hayan de ser adjudicados por la Administración General del Estado')} (art. 22.1 a).",
  "c": f"No armonizado: el FOGASA es {c('ET', A(33), 'organismo autónomo')} (art. 33.1 del Estatuto de los Trabajadores) y su umbral de suministros es {C(21, 'a) 140.000 euros, cuando se trate de contratos adjudicados por la Administración General del Estado, sus Organismos Autónomos')}; 139.000 € no llega.",
  "d": f"Sí armonizado: las concesiones de servicios van con las obras, {C(20, 'de concesión de servicios cuyo valor estimado sea igual o superior a 5.404.000 euros')} (art. 20.1)."},
  [("139.000", "LCSP", A(21), "a) 140.000 euros, cuando se trate de contratos adjudicados por la Administración General del Estado, sus Organismos Autónomos"),
   ("suministros", "LCSP", A(21), "Están sujetos a regulación armonizada los contratos de suministro cuyo valor estimado sea igual o superior a las siguientes cantidades")])
EX_P58 = examen("P", 58, {
  "a": f"El Secretario de Estado es órgano de contratación ({C(323, 'Los Ministros y los Secretarios de Estado son los órganos de contratación')}), pero para los contratos que afectan a varios órganos la ley designa al Ministro.",
  "b": f"Añade al Secretario de Estado: el art. 323.1 atribuye esa competencia solo al Ministro: {C(323, 'corresponderá al Ministro')}.",
  "c": "El Subsecretario no aparece en el art. 323.1 como órgano de contratación.",
  "d": f"Literal del art. 323.1, párrafo segundo: {C(323, 'corresponderá al Ministro, salvo en los casos en que la misma se atribuya a la Junta de Contratación')}."},
  [("El Ministro, salvo", "LCSP", A(323), "corresponderá al Ministro, salvo en los casos en que la misma se atribuya a la Junta de Contratación")])
EX_X56 = examen("X", 56, {
  "a": f"Literal del art. 103.8: {C(103, 'El Instituto Nacional de Estadística elaborará los índices mensuales de los precios de los componentes básicos de costes')}.",
  "b": "Las Juntas de Contratación son órganos de contratación (art. 323.4); el art. 103 no les atribuye la elaboración de índices.",
  "c": f"El Comité Superior de Precios de Contratos del Estado elabora las **fórmulas tipo** ({C(103, 'elaborará las fórmulas y las remitirá para su aprobación al Consejo de Ministros')}) e informa los índices, pero no los elabora.",
  "d": f"La Secretaría de Estado de Hacienda no aparece en el art. 103; los índices se aprueban {C(103, 'por Orden del Ministro de Hacienda y Función Pública')}."},
  [("Instituto Nacional de Estadística", "LCSP", A(103), "El Instituto Nacional de Estadística elaborará los índices mensuales de los precios de los componentes básicos de costes")])

T.ap("s26", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **siete** preguntas de este tema: tres en el turno libre, tres en promoción interna y una en el extraordinario. Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal vigente.",
  "### GACE-L 2025, pregunta 50 · Recurso especial: contratos administrativos especiales (→ VI.2.1)", EX_L50,
  "### GACE-L 2025, pregunta 51 · Perfección de los contratos basados (→ I.5.3)", EX_L51,
  "### GACE-L 2025, pregunta 52 · Solvencia técnica en obras (→ I.6.4)", EX_L52,
  "### GACE-P 2025, pregunta 56 · Ámbito de aplicación y exclusiones (→ I.1.3 y → I.2.1)", EX_P56,
  "### GACE-P 2025, pregunta 57 · Regulación armonizada: umbrales (→ I.3.3)", EX_P57,
  "### GACE-P 2025, pregunta 58 · Órganos de contratación estatales (→ I.8.1)", EX_P58,
  "### GACE-L 2025 extraordinario, pregunta 56 · Revisión de precios: índices (→ V.1.1)", EX_X56,
  "### Cómo se pregunta",
  "!> Las preguntas de contratos son de **dato exacto**: una cifra (umbral, años, porcentaje), un **órgano** (Ministro, INE, TACRC) o una **palabra** («superior» frente a «igual», «precio de licitación» frente a «valor estimado», «adjudicación» frente a «formalización»). Las de umbrales se resuelven con el cuadro de **I.3.3**: identifica el **tipo** de contrato, la **entidad** (¿AGE, organismo autónomo o Seguridad Social?) y compara el **valor estimado**.",
]))

T.ap("s27", "Cierre 2. Repaso en 10 minutos (por bloques)", "\n\n".join([
  """| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Concepto, clases y elementos | Oneroso + entidad del art. 3; exclusiones; SARA; administrativos y privados; perfección; partes; presupuesto, valor estimado y precio | Umbrales 2026: **5.404.000 / 140.000 / 216.000 / 750.000 €**; basados en acuerdo marco: perfección con la **adjudicación** |
| II. Preparación | Expediente motivado; menores; urgencia y emergencia; pliegos | Menores: obras **< 40.000 €**, resto **< 15.000 €**; emergencia: cuenta al Consejo de Ministros en **30 días** |
| III. Adjudicación | Abierto y restringido; criterios calidad-precio; clasificación, adjudicación, formalización; simplificado; negociado | Formalización: **15 días hábiles** de espera; simplificado: obras **≤ 2.000.000 €** |
| IV. Efectos y extinción | Prerrogativas; penalidades; riesgo y ventura; pago; cumplimiento y resolución | Demora: **0,60 € por 1.000 €**; pago **30 días / 4 meses / 6 meses** |
| V. Revisión y alteraciones | Revisión periódica y predeterminada; modificación prevista o no prevista; suspensión, cesión, subcontratación | Revisión: **20 %** y **un año**; índices del **INE**; modificación prevista **20 %**, no prevista **50 %** |
| VI. Invalidez y recursos | Nulidad y anulabilidad; revisión de oficio; recurso especial | Recurso especial: obras **> 3.000.000 €**, resto **> 100.000 €**; **15 días hábiles**; TACRC |""",
  ESQ,
  """| Cifra | Qué es | Artículo |
|---|---|---|
| 15.000 € / 40.000 € | Contrato menor (suministros y servicios / obras), «inferior a» | 118.1 |
| 60.000 € / 80.000 € | Abierto simplificado sumario (suministros y servicios / obras), «inferior a» | 159.6 |
| 100.000 € / 3.000.000 € | Recurso especial (suministros y servicios / obras y concesiones), «superior a» | 44.1 |
| 140.000 € / 216.000 € | SARA de suministros y servicios (AGE, OO. AA. y Seguridad Social / resto) | 21.1 y 22.1 |
| 750.000 € | SARA de los servicios del anexo IV | 22.1 c |
| 2.000.000 € | Abierto simplificado de obras, «igual o inferior» | 159.1 a |
| 5.404.000 € | SARA de obras y concesiones | 20.1 |
| 3 % / 5 % | Garantía provisional (presupuesto base) / definitiva (precio ofertado) | 106.2 y 107.1 |
| 20 % / 50 % | Modificación prevista / modificación no prevista de los apartados a) y b) | 204.1 y 205.2 |""",
  "?> **Trampas frecuentes:** «valor estimado **igual**» para el recurso especial (es **superior**); «se perfeccionan con su **formalización**» los basados en un acuerdo marco (con su **adjudicación**); «presupuesto base **sin** IVA» (es **con** IVA; el valor estimado es **sin** IVA); «el **Comité Superior de Precios** elabora los índices» (los elabora el **INE**); «prórroga **tácita**» (nunca); «el contrato menor de obras es **hasta** 40.000 €» (es **inferior a** 40.000 €); «recurso especial en la tramitación de **emergencia**» (no cabe); «el silencio en el recurso especial es **positivo**» (es **desestimatorio**).",
]))

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
q = T.q
q(K, A(2), "Concepto", "Según el artículo 2.1 de la Ley 9/2017, de Contratos del Sector Público, son contratos del sector público los contratos que celebren las entidades enumeradas en el artículo 3 que sean:",
  ["Onerosos, cualquiera que sea su naturaleza jurídica.", "Administrativos, con exclusión de los privados.", "Gratuitos u onerosos, si su valor estimado supera los 15.000 euros.", "Sujetos a regulación armonizada."],
  "Art. 2.1 LCSP: «los contratos onerosos, cualquiera que sea su naturaleza jurídica».", "los contratos onerosos, cualquiera que sea su naturaleza jurídica")
q(K, A(2), "Concepto", "Según el artículo 2.1 de la LCSP, se entenderá que un contrato tiene carácter oneroso cuando el contratista obtenga:",
  ["Algún tipo de beneficio económico, ya sea de forma directa o indirecta.", "Un beneficio económico directo, en todo caso.", "Un precio en dinero superior al coste de la prestación.", "Una contraprestación abonada exclusivamente por la Administración."],
  "Art. 2.1, párrafo segundo, LCSP.", "algún tipo de beneficio económico, ya sea de forma directa o indirecta")
q(K, A(3), "Concepto", "Según el artículo 3.2 de la LCSP, ¿cuál de las siguientes entidades tiene la consideración de Administración Pública a efectos de la ley?",
  ["Las Entidades Gestoras y los Servicios Comunes de la Seguridad Social.", "Las fundaciones públicas.", "Las Mutuas colaboradoras con la Seguridad Social.", "Las sociedades mercantiles con participación pública superior al 50 por 100."],
  "Art. 3.2 a) LCSP: son Administraciones Públicas las de las letras a), b), c) y l) del 3.1; la b) son las Entidades Gestoras y Servicios Comunes de la Seguridad Social. Fundaciones públicas y Mutuas son poderes adjudicadores (3.3), no Administraciones Públicas.",
  ["Las mencionadas en las letras a), b), c), y l) del apartado primero del presente artículo", "b) Las Entidades Gestoras y los Servicios Comunes de la Seguridad Social."])
q(K, A(11), "Exclusiones", "Según el artículo 11.5 de la LCSP, los contratos que tengan por objeto servicios relacionados con campañas políticas quedan excluidos de la ley:",
  ["Cuando sean adjudicados por un partido político.", "En todo caso, cualquiera que sea el adjudicador.", "Cuando los adjudique una Administración Pública durante el periodo electoral.", "Solo si su valor estimado es inferior a 15.000 euros."],
  "Art. 11.5 LCSP.", "cuando sean adjudicados por un partido político")
q(K, A(20), "Regulación armonizada", "Según el artículo 20.1 de la LCSP, en su redacción vigente desde el 1 de enero de 2026, están sujetos a regulación armonizada los contratos de obras, de concesión de obras y de concesión de servicios cuyo valor estimado sea igual o superior a:",
  ["5.404.000 euros.", "3.000.000 euros.", "2.000.000 euros.", "216.000 euros."],
  "Art. 20.1 LCSP (umbral vigente desde el 1-1-2026).", "cuyo valor estimado sea igual o superior a 5.404.000 euros")
q(K, A(21), "Regulación armonizada", "Según el artículo 21.1 a) de la LCSP, vigente desde el 1 de enero de 2026, están sujetos a regulación armonizada los contratos de suministro adjudicados por la Administración General del Estado, sus Organismos Autónomos o las Entidades Gestoras y Servicios Comunes de la Seguridad Social cuyo valor estimado sea igual o superior a:",
  ["140.000 euros.", "216.000 euros.", "750.000 euros.", "100.000 euros."],
  "Art. 21.1 a) LCSP.", "a) 140.000 euros, cuando se trate de contratos adjudicados por la Administración General del Estado")
q(K, A(22), "Regulación armonizada", "Según el artículo 22.1 de la LCSP, vigente desde el 1 de enero de 2026, ¿cuál es el umbral de regulación armonizada de los contratos de servicios sociales y otros servicios específicos enumerados en el anexo IV?",
  ["750.000 euros.", "216.000 euros.", "140.000 euros.", "5.404.000 euros."],
  "Art. 22.1 c) LCSP.", "c) 750.000 euros, cuando se trate de contratos que tengan por objeto los servicios sociales y otros servicios específicos enumerados en el anexo IV")
q(K, A(25), "Administrativos y privados", "Según el artículo 25.1 a) de la LCSP, aunque los celebre una Administración Pública, tendrán carácter privado:",
  ["Los contratos cuyo objeto sea la suscripción a revistas, publicaciones periódicas y bases de datos.", "Los contratos de suministro de bienes consumibles.", "Los contratos de obras de valor estimado inferior a 40.000 euros.", "Los contratos de servicios de limpieza de edificios públicos."],
  "Art. 25.1 a) 2.º LCSP.", "Aquellos cuyo objeto sea la suscripción a revistas, publicaciones periódicas y bases de datos")
q(K, A(27), "Administrativos y privados", "Según el artículo 27.1 de la LCSP, las cuestiones que se susciten en relación con la preparación y adjudicación de los contratos privados de las Administraciones Públicas son competencia del orden jurisdiccional:",
  ["Contencioso-administrativo.", "Civil.", "Social.", "Civil, salvo que el contrato esté sujeto a regulación armonizada."],
  "Art. 27.1 b) LCSP.", "Las que se susciten en relación con la preparación y adjudicación de los contratos privados de las Administraciones Públicas")
q(K, A(29), "Elementos", "Según el artículo 29.2 de la LCSP, la prórroga acordada por el órgano de contratación será obligatoria para el empresario siempre que su preaviso se produzca al menos con una antelación, respecto de la finalización del plazo de duración del contrato, de:",
  ["Dos meses, salvo que el pliego establezca uno mayor.", "Un mes, salvo que el pliego establezca uno mayor.", "Tres meses, en todo caso.", "Quince días hábiles."],
  "Art. 29.2 LCSP.", "siempre que su preaviso se produzca al menos con dos meses de antelación a la finalización del plazo de duración del contrato")
q(K, A(29), "Elementos", "Según el artículo 29.4 de la LCSP, los contratos de suministros y de servicios de prestación sucesiva tendrán, con carácter general, un plazo máximo de duración, incluidas las posibles prórrogas, de:",
  ["Cinco años.", "Cuatro años.", "Seis años.", "Diez años."],
  "Art. 29.4 LCSP.", "tendrán un plazo máximo de duración de cinco años, incluyendo las posibles prórrogas")
q(K, A(36), "Elementos", "Según el artículo 36.1 de la LCSP, con carácter general los contratos que celebren los poderes adjudicadores se perfeccionan:",
  ["Con su formalización.", "Con su adjudicación.", "Con la aprobación del expediente.", "Con el inicio de su ejecución."],
  "Art. 36.1 LCSP (excepciones: menores y basados en acuerdo marco o en sistema dinámico, 36.3).", "se perfeccionan con su formalización")
q(K, A(37), "Elementos", "Según el artículo 37.1 de la LCSP, las entidades del sector público no podrán contratar verbalmente, salvo que el contrato tenga carácter:",
  ["De emergencia.", "De contrato menor.", "Urgente.", "Privado."],
  "Art. 37.1 LCSP.", "salvo que el contrato tenga, conforme a lo señalado en el artículo 120.1, carácter de emergencia")
q(K, A(100), "Elementos", "Según el artículo 100.1 de la LCSP, el presupuesto base de licitación es el límite máximo de gasto que en virtud del contrato puede comprometer el órgano de contratación:",
  ["Incluido el Impuesto sobre el Valor Añadido, salvo disposición en contrario.", "Excluido el Impuesto sobre el Valor Añadido, en todo caso.", "Excluidas las prórrogas y el Impuesto sobre el Valor Añadido.", "Incluidas las modificaciones no previstas."],
  "Art. 100.1 LCSP.", "incluido el Impuesto sobre el Valor Añadido, salvo disposición en contrario")
q(K, A(101), "Elementos", "Según el artículo 101.1 a) de la LCSP, en los contratos de obras, suministros y servicios, el valor estimado será el importe total:",
  ["Sin incluir el Impuesto sobre el Valor Añadido, pagadero según las estimaciones del órgano de contratación.", "Incluido el Impuesto sobre el Valor Añadido.", "Del presupuesto base de licitación.", "De la oferta del adjudicatario, sin incluir las prórrogas."],
  "Art. 101.1 a) LCSP.", "sin incluir el Impuesto sobre el Valor Añadido, pagadero según sus estimaciones")
q(K, A(107), "Elementos", "Según el artículo 107.1 de la LCSP, la garantía definitiva será de:",
  ["Un 5 por 100 del precio final ofertado, excluido el Impuesto sobre el Valor Añadido.", "Un 3 por 100 del presupuesto base de licitación, excluido el Impuesto sobre el Valor Añadido.", "Un 5 por 100 del presupuesto base de licitación, incluido el Impuesto sobre el Valor Añadido.", "Un 10 por 100 del valor estimado del contrato."],
  "Art. 107.1 LCSP. El 3 % del presupuesto base es el máximo de la garantía provisional (106.2).", "una garantía de un 5 por 100 del precio final ofertado por aquellos, excluido el Impuesto sobre el Valor Añadido")
q(K, A(118), "Preparación", "Según el artículo 118.1 de la LCSP, se consideran contratos menores los de suministro o de servicios de valor estimado:",
  ["Inferior a 15.000 euros.", "Igual o inferior a 15.000 euros.", "Inferior a 40.000 euros.", "Inferior a 18.000 euros."],
  "Art. 118.1 LCSP: obras, inferior a 40.000 €; suministro o servicios, inferior a 15.000 €.", "o a 15.000 euros, cuando se trate de contratos de suministro o de servicios")
q(K, A(119), "Preparación", "Según el artículo 119.2 b) de la LCSP, en los expedientes calificados de urgentes, los plazos establecidos para la licitación, adjudicación y formalización del contrato, con las excepciones previstas:",
  ["Se reducirán a la mitad.", "Se reducirán a la tercera parte.", "Se reducirán en cinco días.", "No se reducen; solo se da preferencia al despacho."],
  "Art. 119.2 b) LCSP.", "se reducirán a la mitad")
q(K, A(120), "Preparación", "Según el artículo 120.1 b) de la LCSP, si un contrato de emergencia ha sido celebrado por la Administración General del Estado, se dará cuenta de dichos acuerdos al Consejo de Ministros en el plazo máximo de:",
  ["Treinta días.", "Quince días.", "Un mes desde el inicio de la ejecución.", "Tres meses."],
  "Art. 120.1 b) LCSP.", "se dará cuenta de dichos acuerdos al Consejo de Ministros en el plazo máximo de treinta días")
q(K, A(121), "Preparación", "Según el artículo 121.1 de la LCSP, los pliegos de cláusulas administrativas generales para la Administración General del Estado los aprueba:",
  ["El Consejo de Ministros, previo dictamen del Consejo de Estado.", "El Ministro de Hacienda y Función Pública, previo informe de la Junta Consultiva de Contratación Pública del Estado.", "Cada órgano de contratación, previo informe del Servicio Jurídico.", "Las Cortes Generales, mediante ley."],
  "Art. 121.1 LCSP.", "El Consejo de Ministros, a iniciativa de los Ministerios interesados, a propuesta del Ministro de Hacienda y Función Pública, y previo dictamen del Consejo de Estado")
q(K, A(122), "Preparación", "Según el artículo 122.1 de la LCSP, los pliegos de cláusulas administrativas particulares, una vez aprobados, solo podrán ser modificados con posterioridad:",
  ["Por error material, de hecho o aritmético.", "Por razones de interés público debidamente motivadas.", "A instancia de cualquier licitador, antes de la adjudicación.", "Con informe favorable del Servicio Jurídico."],
  "Art. 122.1 LCSP: en otro caso, la modificación conlleva la retroacción de actuaciones.", "solo podrán ser modificados con posterioridad por error material, de hecho o aritmético")
q(K, A(131), "Adjudicación", "Según el artículo 131.2 de la LCSP, la adjudicación se realizará ordinariamente utilizando:",
  ["El procedimiento abierto o el procedimiento restringido.", "El procedimiento negociado con publicidad.", "El diálogo competitivo.", "El procedimiento abierto simplificado, en todo caso."],
  "Art. 131.2 LCSP.", "utilizando el procedimiento abierto o el procedimiento restringido")
q(K, A(150), "Adjudicación", "Según el artículo 150.2 de la LCSP, el licitador que haya presentado la mejor oferta deberá presentar la documentación requerida dentro del plazo de:",
  ["Diez días hábiles, a contar desde el siguiente a aquel en que hubiera recibido el requerimiento.", "Cinco días hábiles, a contar desde la apertura de las proposiciones.", "Quince días naturales, a contar desde la notificación de la adjudicación.", "Diez días naturales, a contar desde la publicación en el perfil de contratante."],
  "Art. 150.2 LCSP.", "dentro del plazo de diez días hábiles, a contar desde el siguiente a aquel en que hubiera recibido el requerimiento")
q(K, A(150), "Adjudicación", "Según el artículo 150.3 de la LCSP, una licitación no podrá declararse desierta:",
  ["Cuando exista alguna oferta o proposición que sea admisible de acuerdo con los criterios que figuren en el pliego.", "Cuando se hayan presentado al menos tres ofertas.", "Una vez transcurridos dos meses desde la apertura de las proposiciones.", "Si el contrato está sujeto a regulación armonizada."],
  "Art. 150.3, párrafo segundo, LCSP.", "No podrá declararse desierta una licitación cuando exista alguna oferta o proposición que sea admisible de acuerdo con los criterios que figuren en el pliego")
q(K, A(153), "Adjudicación", "Según el artículo 153.3 de la LCSP, si el contrato es susceptible de recurso especial en materia de contratación, la formalización no podrá efectuarse antes de que transcurran:",
  ["Quince días hábiles desde que se remita la notificación de la adjudicación a los licitadores y candidatos.", "Diez días naturales desde la publicación de la adjudicación.", "Cinco días hábiles desde la adjudicación.", "Un mes desde la notificación de la adjudicación, en todo caso."],
  "Art. 153.3 LCSP (las CC. AA. pueden incrementarlo sin exceder de un mes).", "la formalización no podrá efectuarse antes de que transcurran quince días hábiles desde que se remita la notificación de la adjudicación a los licitadores y candidatos")
q(K, A(156), "Adjudicación", "Según el artículo 156.6 de la LCSP, en los contratos de obras de las Administraciones Públicas no sujetos a regulación armonizada adjudicados por procedimiento abierto, el plazo de presentación de proposiciones será, como mínimo, de:",
  ["Veintiséis días.", "Quince días.", "Treinta y cinco días.", "Veinte días."],
  "Art. 156.6 LCSP: regla general, no inferior a quince días; obras y concesiones, como mínimo veintiséis.", "En los contratos de obras y de concesión de obras y concesión de servicios, el plazo será, como mínimo, de veintiséis días")
q(K, A(159), "Adjudicación", "Según el artículo 159.1 a) de la LCSP, podrá utilizarse el procedimiento abierto simplificado en los contratos de obras cuyo valor estimado sea:",
  ["Igual o inferior a 2.000.000 de euros.", "Inferior a 5.404.000 euros.", "Inferior a 80.000 euros.", "Igual o inferior a 3.000.000 de euros."],
  "Art. 159.1 a) LCSP.", "igual o inferior a 2.000.000 de euros en el caso de contratos de obras")
q(K, A(159), "Adjudicación", "Según el artículo 159.6 de la LCSP, la tramitación sumaria del procedimiento abierto simplificado puede seguirse en los contratos de suministros y de servicios de valor estimado inferior a:",
  ["60.000 euros, salvo los que tengan por objeto prestaciones de carácter intelectual.", "80.000 euros, incluidos los de prestaciones de carácter intelectual.", "15.000 euros.", "100.000 euros."],
  "Art. 159.6 LCSP: obras, inferior a 80.000 €; suministros y servicios, inferior a 60.000 €.", "en contratos de suministros y de servicios de valor estimado inferior a 60.000 euros, excepto los que tengan por objeto prestaciones de carácter intelectual")
q(K, A(162), "Adjudicación", "Según el artículo 162.2 de la LCSP, en el procedimiento restringido el número mínimo de empresarios a los que el órgano de contratación invitará a participar no podrá ser inferior a:",
  ["Cinco.", "Tres.", "Seis.", "Diez."],
  "Art. 162.2 LCSP.", "que no podrá ser inferior a cinco")
q(K, A(191), "Efectos", "Según el artículo 191.3 a) de la LCSP, será preceptivo el dictamen del Consejo de Estado u órgano consultivo equivalente de la Comunidad Autónoma en la interpretación, nulidad y resolución de los contratos:",
  ["Cuando se formule oposición por parte del contratista.", "En todo caso.", "Solo si el contrato está sujeto a regulación armonizada.", "Cuando su precio sea igual o superior a 6.000.000 de euros."],
  "Art. 191.3 a) LCSP.", "La interpretación, nulidad y resolución de los contratos, cuando se formule oposición por parte del contratista")
q(K, A(193), "Efectos", "Según el artículo 193.3 de la LCSP, cuando el contratista haya incurrido en demora por causas imputables a él, la Administración podrá imponer penalidades diarias en la proporción de:",
  ["0,60 euros por cada 1.000 euros del precio del contrato, IVA excluido.", "0,20 euros por cada 1.000 euros del precio del contrato, IVA incluido.", "1 euro por cada 1.000 euros del precio del contrato, IVA excluido.", "El 5 por 100 del precio del contrato por cada día de retraso."],
  "Art. 193.3 LCSP.", "en la proporción de 0,60 euros por cada 1.000 euros del precio del contrato, IVA excluido")
q(K, A(197), "Efectos", "Según el artículo 197 de la LCSP, la ejecución del contrato se realizará:",
  ["A riesgo y ventura del contratista.", "A riesgo y ventura de la Administración.", "A riesgo compartido entre la Administración y el contratista.", "A riesgo del contratista solo si así lo establece el pliego."],
  "Art. 197 LCSP (sin perjuicio del art. 239 para obras).", "La ejecución del contrato se realizará a riesgo y ventura del contratista")
q(K, A(198), "Efectos", "Según el artículo 198.6 de la LCSP, el contratista tendrá derecho a resolver el contrato si la demora de la Administración en el pago fuese superior a:",
  ["Seis meses.", "Cuatro meses.", "Treinta días.", "Un año."],
  "Art. 198.6 LCSP (con más de cuatro meses solo puede suspender, 198.5).", "Si la demora de la Administración fuese superior a seis meses, el contratista tendrá derecho, asimismo, a resolver el contrato")
q(K, A(210), "Extinción", "Según el artículo 210.2 de la LCSP, la constatación del cumplimiento del contrato exigirá un acto formal y positivo de recepción o conformidad:",
  ["Dentro del mes siguiente a la entrega o realización del objeto del contrato, o en el plazo que determine el pliego.", "Dentro de los quince días siguientes a la entrega, en todo caso.", "Dentro de los tres meses siguientes a la entrega.", "Al término del plazo de garantía."],
  "Art. 210.2 LCSP.", "dentro del mes siguiente a la entrega o realización del objeto del contrato")
q(K, A(212), "Extinción", "Según el artículo 212.8 de la LCSP, los expedientes de resolución contractual deberán ser instruidos y resueltos en el plazo máximo de:",
  ["Ocho meses.", "Seis meses.", "Tres meses.", "Un año."],
  "Art. 212.8 LCSP.", "Los expedientes de resolución contractual deberán ser instruidos y resueltos en el plazo máximo de ocho meses")
q(K, A(103), "Revisión de precios", "Según el artículo 103.5 de la LCSP, salvo en los contratos de suministro de energía, la revisión periódica y predeterminada de precios tendrá lugar cuando el contrato se hubiese ejecutado, al menos, en:",
  ["El 20 por ciento de su importe y hubiese transcurrido un año desde su formalización.", "El 50 por ciento de su importe y hubiese transcurrido un año desde su adjudicación.", "El 20 por ciento de su importe y hubiesen transcurrido dos años desde su formalización.", "El 10 por ciento de su importe, sin requisito temporal."],
  "Art. 103.5 LCSP.", "al menos, en el 20 por ciento de su importe y hubiese transcurrido un año desde su formalización")
q(K, A(204), "Modificación", "Según el artículo 204.1 de la LCSP, los contratos de las Administraciones Públicas podrán modificarse durante su vigencia, cuando lo haya advertido expresamente el pliego de cláusulas administrativas particulares, hasta un máximo del:",
  ["Veinte por ciento del precio inicial.", "Cincuenta por ciento del precio inicial.", "Diez por ciento del precio inicial.", "Quince por ciento del precio inicial."],
  "Art. 204.1 LCSP.", "hasta un máximo del veinte por ciento del precio inicial")
q(K, A(205), "Modificación", "Según el artículo 205.2 b) de la LCSP, una modificación no prevista por circunstancias sobrevenidas e imprevisibles no podrá implicar una alteración de la cuantía del contrato que exceda, aislada o conjuntamente, del:",
  ["50 por ciento de su precio inicial, IVA excluido.", "20 por ciento de su precio inicial, IVA excluido.", "15 por ciento de su precio inicial, IVA incluido.", "10 por ciento de su precio inicial, IVA excluido."],
  "Art. 205.2 b) 3.º LCSP.", "del 50 por ciento de su precio inicial, IVA excluido")
q(K, A(206), "Modificación", "Según el artículo 206.1 de la LCSP, las modificaciones del artículo 205 acordadas por el órgano de contratación serán obligatorias para los contratistas cuando impliquen una alteración de su cuantía que no exceda del:",
  ["20 por ciento del precio inicial del contrato, IVA excluido.", "10 por ciento del precio inicial del contrato, IVA excluido.", "50 por ciento del precio inicial del contrato, IVA incluido.", "30 por ciento del precio inicial del contrato, IVA excluido."],
  "Art. 206.1 LCSP.", "una alteración en su cuantía que no exceda del 20 por ciento del precio inicial del contrato, IVA excluido")
q(K, A(214), "Otras alteraciones", "Según el artículo 214.2 de la LCSP, para que el contratista pueda ceder el contrato (fuera de los casos de concesión y concurso) es necesario que el cedente tenga ejecutado al menos:",
  ["Un 20 por 100 del importe del contrato.", "Un 50 por 100 del importe del contrato.", "Un 10 por 100 del importe del contrato.", "La mitad del plazo de duración del contrato."],
  "Art. 214.2 b) LCSP.", "Que el cedente tenga ejecutado al menos un 20 por 100 del importe del contrato")
q(K, A(215), "Otras alteraciones", "Según el artículo 215.8 de la LCSP, los subcontratistas, por las obligaciones contraídas con ellos por el contratista:",
  ["No tendrán acción directa frente a la Administración contratante.", "Tendrán acción directa frente a la Administración contratante en todo caso.", "Podrán reclamar a la Administración si el contratista se demora más de seis meses.", "Podrán reclamar a la Administración con autorización del órgano de contratación."],
  "Art. 215.8 LCSP (sin perjuicio de la disposición adicional quincuagésima primera).", "los subcontratistas no tendrán acción directa frente a la Administración contratante")
q(K, A(39), "Invalidez", "Según los artículos 39 y 40 de la LCSP, ¿cuál de las siguientes es causa de NULIDAD de derecho administrativo de los contratos?",
  ["La carencia o insuficiencia de crédito, salvo en los supuestos de emergencia.", "El incumplimiento de los requisitos exigidos para la modificación de los contratos en los artículos 204 y 205.", "Los encargos a medios propios que no observen los requisitos del artículo 32.", "Los actos que otorguen ventajas a las empresas que hayan contratado previamente con cualquier Administración."],
  "Art. 39.2 b) LCSP. Las otras tres son causas de anulabilidad (art. 40 a, b y c).", ["La carencia o insuficiencia de crédito", "salvo los supuestos de emergencia"])
q(K, A(44), "Recurso especial", "Según el artículo 44.1 a) de la LCSP, son susceptibles de recurso especial en materia de contratación los contratos de obras cuyo valor estimado sea:",
  ["Superior a tres millones de euros.", "Igual o superior a 5.404.000 euros.", "Superior a dos millones de euros.", "Superior a cien mil euros."],
  "Art. 44.1 a) LCSP (suministro y servicios: superior a cien mil euros).", "Contratos de obras cuyo valor estimado sea superior a tres millones de euros")
q(K, A(44), "Recurso especial", "Según el artículo 44 de la LCSP, el recurso especial en materia de contratación:",
  ["Tiene carácter potestativo y es gratuito para los recurrentes.", "Es obligatorio antes de acudir a la jurisdicción contencioso-administrativa.", "Es potestativo y exige el pago de una tasa.", "Procede también en los procedimientos tramitados por emergencia."],
  "Art. 44.7 LCSP (y 44.4: no cabe en la emergencia).", "La interposición del recurso especial en materia de contratación tendrá carácter potestativo y será gratuito para los recurrentes")
q(K, A(45), "Recurso especial", "Según el artículo 45 de la LCSP, en el ámbito del sector público estatal los recursos especiales en materia de contratación los resuelve:",
  ["El Tribunal Administrativo Central de Recursos Contractuales.", "La Junta Consultiva de Contratación Pública del Estado.", "El Consejo de Estado.", "El Ministro del departamento del órgano de contratación."],
  "Art. 45.1 LCSP.", "estará encomendado al Tribunal Administrativo Central de Recursos Contractuales")
q(K, A(50), "Recurso especial", "Según el artículo 50.1 de la LCSP, el escrito de interposición del recurso especial en materia de contratación deberá presentarse en el plazo de:",
  ["Quince días hábiles.", "Diez días hábiles.", "Un mes.", "Veinte días naturales."],
  "Art. 50.1 LCSP.", "deberá presentarse en el plazo de quince días hábiles")
q(K, A(53), "Recurso especial", "Según el artículo 53 de la LCSP, una vez interpuesto el recurso especial quedará en suspenso la tramitación del procedimiento cuando el acto recurrido sea:",
  ["El de adjudicación, salvo en los contratos basados en un acuerdo marco o específicos de un sistema dinámico de adquisición.", "El anuncio de licitación.", "El pliego de cláusulas administrativas particulares.", "Cualquier acto de trámite, en todo caso."],
  "Art. 53 LCSP.", "quedará en suspenso la tramitación del procedimiento cuando el acto recurrido sea el de adjudicación")
q(K, A(57), "Recurso especial", "Según el artículo 57.5 de la LCSP, transcurridos dos meses desde el siguiente a la interposición del recurso especial sin que se haya notificado su resolución, el interesado:",
  ["Podrá considerarlo desestimado a los efectos de interponer recurso contencioso-administrativo.", "Podrá considerarlo estimado.", "Deberá interponer recurso de alzada.", "Deberá esperar a la resolución expresa, que es obligatoria."],
  "Art. 57.5 LCSP.", "el interesado podrá considerarlo desestimado a los efectos de interponer recurso contencioso-administrativo")
q(K, A(58), "Recurso especial", "Según el artículo 58.2 de la LCSP, si el órgano competente aprecia temeridad o mala fe en la interposición del recurso especial, podrá imponer una multa de:",
  ["Entre 1.000 y 30.000 euros.", "Entre 600 y 6.000 euros.", "Entre 3.000 y 60.000 euros.", "Hasta el 3 por ciento del presupuesto base de licitación."],
  "Art. 58.2 LCSP.", "El importe de la multa será de entre 1.000 y 30.000 euros")
T.real("L", 50, "Recurso especial"); T.real("L", 51, "Elementos"); T.real("L", 52, "Elementos")
T.real("P", 56, "Concepto"); T.real("P", 57, "Regulación armonizada"); T.real("P", 58, "Elementos")
T.real("X", 56, "Revisión de precios")

# Flashcards
for q_, a_, cat in [
  ("Concepto de contrato del sector público (art. 2.1 LCSP)", "Contrato oneroso, cualquiera que sea su naturaleza jurídica, celebrado por una entidad del art. 3. Oneroso: el contratista obtiene algún beneficio económico, directo o indirecto.", "Concepto"),
  ("¿Quiénes son poder adjudicador sin ser Administración Pública? (art. 3.3)", "Las fundaciones públicas, las Mutuas colaboradoras con la Seguridad Social, las entidades del 3.3 d) y sus asociaciones.", "Concepto"),
  ("Umbrales SARA desde el 1-1-2026 (arts. 20 a 22)", "Obras y concesiones: 5.404.000 €. Suministros y servicios: 140.000 € (AGE, OO. AA., Entidades Gestoras y Servicios Comunes de la Seguridad Social) o 216.000 € (resto). Servicios del anexo IV: 750.000 €.", "Regulación armonizada"),
  ("¿Quién celebra contratos administrativos? (art. 25)", "Solo una Administración Pública: los típicos (obra, concesiones, suministro y servicios) y los administrativos especiales.", "Administrativos y privados"),
  ("Contrato privado de una Administración: ¿qué norma rige cada fase? (art. 26.2)", "Preparación y adjudicación: LCSP (contencioso); efectos, modificación y extinción: derecho privado (civil).", "Administrativos y privados"),
  ("¿Cuándo se perfeccionan los contratos? (art. 36)", "Regla: con su formalización. Los basados en un acuerdo marco y los específicos de un sistema dinámico: con su adjudicación.", "Elementos"),
  ("Duración máxima de suministros y servicios de prestación sucesiva (art. 29.4)", "Cinco años, incluidas las prórrogas; los menores, un año y sin prórroga (29.8).", "Elementos"),
  ("Presupuesto base de licitación y valor estimado: ¿con o sin IVA?", "Presupuesto base: con IVA (art. 100). Valor estimado: sin IVA y con prórrogas y modificaciones previstas (art. 101).", "Elementos"),
  ("Garantías: provisional y definitiva (arts. 106 y 107)", "Provisional: excepcional, hasta el 3 % del presupuesto base sin IVA. Definitiva: 5 % del precio final ofertado sin IVA.", "Elementos"),
  ("Contrato menor (art. 118.1)", "Obras: valor estimado inferior a 40.000 €. Suministro o servicios: inferior a 15.000 €.", "Preparación"),
  ("Tramitación de emergencia (art. 120)", "Sin expediente ni requisitos formales; en el Estado, cuenta al Consejo de Ministros en 30 días; inicio de la ejecución en un mes como máximo.", "Preparación"),
  ("¿Quién aprueba el PCAP y cuándo puede modificarse? (art. 122)", "El órgano de contratación, antes de la licitación; solo se modifica por error material, de hecho o aritmético (si no, retroacción).", "Preparación"),
  ("Plazos de la adjudicación (arts. 150 y 151)", "Documentación del mejor licitador: 10 días hábiles; adjudicación: 5 días hábiles desde su recepción; publicación de la adjudicación: 15 días.", "Adjudicación"),
  ("Formalización si cabe recurso especial (art. 153.3)", "No antes de 15 días hábiles desde la notificación de la adjudicación; después, en 5 días desde el requerimiento.", "Adjudicación"),
  ("Abierto simplificado (art. 159)", "Obras ≤ 2.000.000 €; suministros y servicios < umbral SARA de la AGE; juicio de valor ≤ 25 %. Sumario (159.6): obras < 80.000 €, suministros y servicios < 60.000 €.", "Adjudicación"),
  ("Prerrogativas de la Administración (art. 190)", "Interpretar, resolver dudas, modificar por interés público, declarar la responsabilidad del contratista, suspender, acordar la resolución y determinar sus efectos.", "Efectos"),
  ("Penalidades por demora (art. 193.3)", "0,60 € diarios por cada 1.000 € del precio, IVA excluido; cada 5 % del precio, la Administración puede resolver.", "Efectos"),
  ("Demora de la Administración en el pago (art. 198)", "30 días para pagar; más de 4 meses: el contratista puede suspender; más de 6 meses: puede resolver.", "Efectos"),
  ("Revisión de precios: requisitos (art. 103.5)", "Ejecutado al menos el 20 % y transcurrido un año desde la formalización (salvo suministro de energía). Índices: los elabora el INE.", "Revisión de precios"),
  ("Modificación: límites (arts. 204 a 206)", "Prevista en el pliego: hasta el 20 %. No prevista por prestaciones adicionales o imprevisibles: hasta el 50 %. Obligatoria para el contratista hasta el 20 %.", "Modificación"),
  ("Recurso especial: cuantías y plazo (arts. 44 y 50)", "Obras y concesiones > 3.000.000 €; suministros y servicios > 100.000 €. Plazo: 15 días hábiles. Potestativo y gratuito; no cabe en la emergencia.", "Recurso especial"),
  ("Silencio en el recurso especial (art. 57.5)", "Dos meses desde la interposición: desestimado a efectos del recurso contencioso-administrativo.", "Recurso especial"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Contrato del sector público", "Contrato oneroso, cualquiera que sea su naturaleza jurídica, celebrado por una entidad del art. 3 LCSP (art. 2.1).", "s1", "Concepto")
T.glos("Poder adjudicador", "Entidad del art. 3.3 LCSP: las Administraciones Públicas, las fundaciones públicas, las Mutuas colaboradoras con la Seguridad Social y ciertas entidades de interés general financiadas o controladas por otro poder adjudicador.", "s1", "Concepto")
T.glos("Contrato sujeto a regulación armonizada", "Contrato de un poder adjudicador cuyo valor estimado iguala o supera los umbrales de los arts. 20 a 22 LCSP (art. 19.1).", "s3", "Clases")
T.glos("Contrato administrativo especial", "Contrato de una Administración Pública declarado administrativo por una ley o vinculado a su giro o tráfico específico o a una finalidad pública de su competencia (art. 25.1 b).", "s4", "Clases")
T.glos("Contrato privado", "Contrato del sector público no administrativo (art. 26); si lo celebra una Administración, su preparación y adjudicación se rigen por la LCSP y sus efectos y extinción por el derecho privado.", "s4", "Clases")
T.glos("Perfección", "Momento en que nace el contrato: con su formalización o, en los basados en un acuerdo marco, con su adjudicación (art. 36).", "s5", "Elementos")
T.glos("Presupuesto base de licitación", "Límite máximo de gasto que puede comprometer el órgano de contratación, incluido el IVA (art. 100.1).", "s7", "Elementos")
T.glos("Valor estimado", "Importe total del contrato sin IVA según las estimaciones del órgano de contratación, con prórrogas y modificaciones previstas; determina umbrales y procedimientos (art. 101).", "s7", "Elementos")
T.glos("Contrato menor", "Contrato de obras de valor estimado inferior a 40.000 € o de suministro o servicios inferior a 15.000 €, con expediente simplificado (art. 118).", "s10", "Preparación")
T.glos("Tramitación de emergencia", "Régimen excepcional para actuar de inmediato ante catástrofes, grave peligro o necesidades de la defensa nacional, sin expediente ni requisitos formales (art. 120).", "s10", "Preparación")
T.glos("Pliego de cláusulas administrativas particulares", "Documento aprobado por el órgano de contratación antes de la licitación que contiene los criterios y los derechos y obligaciones de las partes; sus cláusulas son parte del contrato (art. 122).", "s11", "Preparación")
T.glos("Procedimiento abierto simplificado", "Procedimiento abierto con anuncio solo en el perfil de contratante para obras de hasta 2.000.000 € y suministros y servicios por debajo del umbral SARA de la AGE (art. 159).", "s14", "Adjudicación")
T.glos("Riesgo y ventura", "Principio por el que la ejecución del contrato corre a cargo y riesgo del contratista (art. 197).", "s18", "Efectos")
T.glos("Revisión de precios", "Ajuste periódico y predeterminado del precio por variaciones de costes, mediante fórmula fijada en el pliego, tras ejecutar el 20 % y pasar un año (arts. 103 a 105).", "s20", "Alteraciones")
T.glos("Recurso especial en materia de contratación", "Recurso potestativo y gratuito contra anuncios, pliegos, actos de trámite cualificados, adjudicaciones y otros actos de contratos de cierta cuantía, que resuelve en el Estado el TACRC (arts. 44 a 60).", "s24", "Recursos")

# Cronología (fechas de los metadatos del BOE)
T.hito("2014", "Directivas 2014/23/UE y 2014/24/UE, de 26 de febrero de 2014 (citadas en el título de la Ley 9/2017)", "La LCSP las transpone al ordenamiento español", "normativo", "s1")
T.hito("2017", "Ley 9/2017, de 8 de noviembre, de Contratos del Sector Público (BOE de 9-11-2017)", "Régimen vigente de los contratos del sector público", "normativo", "s1")
T.hito("2018", "Entrada en vigor de la Ley 9/2017 (fecha de vigencia del BOE: 9-3-2018)", "Primera versión vigente del texto consolidado", "normativo", "s1")
T.hito("2025", "Orden HAC/1517/2025, de 18 de diciembre (BOE de 26-12-2025)", "Límites de los contratos a partir del 1-1-2026: nueva redacción de los arts. 20 a 22 (5.404.000, 140.000 y 216.000 €)", "normativo", "s3")

T.publicar()
