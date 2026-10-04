# -*- coding: utf-8 -*-
"""Tema VI.4 (B6T04): Control del gasto público en España. La Intervención General de
la Administración del Estado. Función interventora, control financiero permanente y
auditoría pública. El Tribunal de Cuentas.
Método del I.2. Normas (textos consolidados del BOE): CE, arts. 136 y 153; Ley 47/2003,
General Presupuestaria (título VI, arts. 140 a 170); RD 2188/1995 (control interno de la
IGAE); RD 206/2024 (estructura del Ministerio de Hacienda: IGAE); LO 2/1982 del Tribunal
de Cuentas; Ley 7/1988 de Funcionamiento del Tribunal de Cuentas; Ley 15/2014, art. 22."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO.update({"LOTCu": "LO 2/1982", "LFTCu": "Ley 7/1988", "RD2188": "RD 2188/1995",
              "RD206_2024": "RD 206/2024", "L15_2014": "Ley 15/2014"})

T = Tema("B6T04",
  "Cinco preguntas: I. Cómo se controla el gasto público: control externo e interno (CE, art. 136; LGP, arts. 140 a 142) · II. Quién hace el control interno: la IGAE (LGP, arts. 143 a 147; RD 206/2024, arts. 8 y 11) · III. Cómo se controla antes de decidir: la función interventora (LGP, arts. 148 a 156; RD 2188/1995) · IV. Cómo se controla después: control financiero permanente y auditoría pública (LGP, arts. 157 a 170) · V. Quién hace el control externo: el Tribunal de Cuentas (CE, arts. 136 y 153; LO 2/1982; Ley 7/1988). Cada artículo: texto literal del BOE y ficha.",
  ["Control externo", "Control interno", "IGAE", "Intervenciones Delegadas", "Función interventora", "Fiscalización previa", "Reparo", "Discrepancia", "Omisión de fiscalización", "Requisitos básicos", "Control financiero permanente", "Auditoría pública", "Plan de Acción", "Tribunal de Cuentas", "Cuenta General del Estado", "Responsabilidad contable", "Alcance"])

# =============================================================================
T.ap("s0", "Mapa del tema: cinco preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque VI, tema 4):
> Control del gasto público en España. La Intervención General de la Administración del Estado. Función interventora, control financiero permanente y auditoría pública. El Tribunal de Cuentas.

### El hilo conductor

El epígrafe se lee como **cinco preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Normas |
|---|---|---|
| **I** | ¿Cómo se controla el gasto público? (control externo e interno) | LGP, arts. 140 a 142 |
| **II** | ¿Quién hace el control interno? (la IGAE) | LGP, arts. 143 a 147; RD 206/2024, arts. 8.6 y 11 |
| **III** | ¿Cómo se controla antes de decidir? (función interventora) | LGP, arts. 148 a 156; RD 2188/1995, arts. 8, 13, 14 y 16 |
| **IV** | ¿Cómo se controla después? (control financiero permanente y auditoría pública) | LGP, arts. 157 a 170; RD 2188/1995, art. 35 |
| **V** | ¿Quién hace el control externo? (el Tribunal de Cuentas) | CE, arts. 136 y 153 d); LO 2/1982, del Tribunal de Cuentas; Ley 7/1988, de Funcionamiento; Ley 15/2014, art. 22 |

!> **La idea que une los cinco bloques:** el gasto del sector público estatal tiene **dos** controles. El **interno** lo hace la **IGAE** con plena autonomía, de tres formas: **función interventora** (antes de aprobar cada acto), **control financiero permanente** (de forma continua) y **auditoría pública** (después y de forma sistemática). El **externo** lo hace el **Tribunal de Cuentas**, que depende de las **Cortes Generales**, fiscaliza y, además, **juzga** la responsabilidad contable.

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
- Lo que el tema VI.6 (gestión del gasto y su control) y el VI.5 (ejecución del gasto) explican con más detalle se remite allí en texto llano.
""")

# =============================================================================
T.ap("bI", "I. ¿Cómo se controla el gasto público? Control externo e interno (LGP, arts. 140 a 142)", donde(
  "Primera pregunta del tema. Antes de estudiar a cada controlador hay que saber **cuántos controles** hay sobre la gestión económica del sector público estatal, **quién** hace cada uno y **para qué** sirve.",
  ["1 Control externo (Tribunal de Cuentas) y control interno (IGAE) (LGP, art. 140)", "2 Objetivos del control interno y sus tres formas (LGP, arts. 141 y 142)"]))

T.ap("s1", "I.1 Control externo y control interno (LGP, art. 140)", f"""
{unidad("1.1 Los dos controles del sector público estatal (art. 140)",
  lit("LGP", "a140", ["corresponde al Tribunal de Cuentas el control externo del sector público estatal", "el control interno de la gestión económica y financiera del sector público estatal", "con plena autonomía respecto de las autoridades y demás entidades cuya gestión controle"]),
  fichab("Reparto del control de la gestión económico-financiera del sector público estatal",
         [f"::Dos controladores:", f"Externo: {c('LGP', 'a140', 'corresponde al Tribunal de Cuentas el control externo del sector público estatal')}", f"Interno: {c('LGP', 'a140', 'La Intervención General de la Administración del Estado')}"],
         f"El externo, {c('LGP', 'a140', 'en los términos establecidos en la Constitución, en su ley orgánica y en las demás leyes que regulen su competencia')}; el interno, {c('LGP', 'a140', 'en los términos previstos en esta ley')}",
         "—",
         "**Externo = Tribunal de Cuentas** (→ V.1); **interno = IGAE** (→ II.1). La IGAE actúa «con **plena autonomía**» respecto de los gestores que controla, aunque forma parte del Ministerio de Hacienda."))}

{unidad("1.2 El Tribunal de Cuentas en la Constitución (art. 136.1 CE)",
  lit("CE", "Artículo 136", ["supremo órgano fiscalizador"], solo=[1]),
  fichab("Rango constitucional del control externo",
         c("CE", "Artículo 136", "El Tribunal de Cuentas"),
         f"Fiscaliza {c('CE', 'Artículo 136', 'las cuentas y de la gestión económica de Estado, así como del sector público')}",
         "—",
         "El art. 140.1 LGP repite la fórmula de la Constitución: «**supremo** órgano fiscalizador». Se estudia a fondo en → V.1."))}
""", 2)

T.ap("s2", "I.2 Objetivos del control interno y sus tres formas (LGP, arts. 141 y 142)", f"""
{unidad("2.1 Control de subvenciones y ayudas (art. 141)",
  lit("LGP", "a141", ["entidades colaboradoras y beneficiarios de subvenciones y ayudas"]),
  fichab("Control de la IGAE sobre perceptores de subvenciones y ayudas",
         c("LGP", "a141", "La Intervención General de la Administración del Estado"),
         f"Sobre {c('LGP', 'a141', 'entidades colaboradoras y beneficiarios de subvenciones y ayudas')}, también las {c('LGP', 'a141', 'financiadas con cargo a fondos comunitarios')}",
         "—",
         "Se rige por la **Ley General de Subvenciones** y la normativa comunitaria (el control de subvenciones se estudia en el tema IV.7)."))}

{unidad("2.2 Objetivos y formas del control (art. 142)",
  lit("LGP", "a142", ["Verificar el cumplimiento de la normativa", "principios de buena gestión financiera", "Verificar el cumplimiento de los objetivos asignados a los centros gestores del gasto", "la función interventora, el control financiero permanente y la auditoría pública"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Para qué se controla y con qué instrumentos",
         "La IGAE",
         ["::Objetivos (142.1):", "a) Cumplimiento de la normativa", "b) Adecuado registro y contabilización de las operaciones", "c) Buena gestión financiera y principios de la Ley General de Estabilidad Presupuestaria", "d) Cumplimiento de los objetivos de los centros gestores del gasto en los PGE"],
         "—",
         f"Tres formas, y **solo tres** (142.2): {c('LGP', 'a142', 'la función interventora, el control financiero permanente y la auditoría pública')} (capítulos II, III y IV del título VI → III.1, → IV.1 y → IV.3)."))}

### 2.3 Cuadro de las tres formas del control interno (esquema)

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| | Función interventora | Control financiero permanente | Auditoría pública |
|---|---|---|---|
| Momento | **Antes** de que se aprueben los actos (148) | De forma **continua** (157) | **Con posterioridad** (162) |
| Quién | IGAE e interventores delegados (149.1) | La intervención delegada (157) | IGAE, según el **plan anual de auditorías** (163 y 165) |
| Sobre quién | AGE, organismos autónomos, entidades gestoras y servicios comunes de la Seguridad Social (149.1) | Lista del art. 158 | Todo el sector público estatal (163) |
| Resultado | Fiscalización favorable o **reparo** (154) | **Informes** y plan anual (159.2 y 3) | **Informes** escritos (166) |

{resumen([
  "**Externo**: Tribunal de Cuentas, «supremo órgano fiscalizador» (CE 136.1; LGP 140.1). **Interno**: IGAE, con **plena autonomía** (140.2).",
  "Objetivos del control interno: normativa, registro contable, buena gestión financiera y objetivos de los centros gestores (142.1).",
  "Tres formas: **función interventora**, **control financiero permanente** y **auditoría pública** (142.2)."],
  "Siguiente: II. ¿Quién hace el control interno? La IGAE")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Quién hace el control interno? La Intervención General de la Administración del Estado", donde(
  "Segunda pregunta. Ya sabemos que el control interno es de la **IGAE**; ahora, **qué es**, **dónde está** en la Administración, **cómo se organiza** y con qué **principios y prerrogativas** actúa.",
  ["1 Naturaleza, funciones y órganos (RD 206/2024, arts. 8.6 y 11)", "2 Ámbito, principios y prerrogativas del control (LGP, arts. 143 y 144)", "3 Deberes, colaboración e informes generales (LGP, arts. 145 a 147)"]))

T.ap("s3", "II.1 Naturaleza, funciones y órganos de la IGAE (RD 206/2024, arts. 8.6 y 11)", f"""
El título VI de la LGP dice **qué** control hace la IGAE; el real decreto de estructura del Ministerio de Hacienda dice **dónde está** y **cómo se organiza**.

{unidad("1.1 Adscripción y rango (RD 206/2024, art. 8.6)",
  lit("RD206_2024", "a8", ["con rango de Subsecretaría"], solo=[8], titulo="Artículo 8.6 (RD 206/2024, estructura del Ministerio de Hacienda)"),
  fichab("Lugar de la IGAE en el Ministerio de Hacienda",
         c("RD206_2024", "a8", "la Intervención General de la Administración del Estado"),
         f"Adscrita a la {c('RD206_2024', 'a8', 'Secretaría de Estado de Presupuestos y Gastos')}",
         "—",
         "Rango de **Subsecretaría**; adscrita a la Secretaría de Estado de **Presupuestos y Gastos** (no a la de Hacienda)."))}

{unidad("1.2 Funciones (RD 206/2024, art. 11.1)",
  lit("RD206_2024", "a1-3", ["El control interno mediante el ejercicio de la función interventora, del control financiero permanente y de la auditoría pública", "la administración y custodia de la Base de Datos Nacional de Subvenciones", "La dirección y la gestión de la contabilidad pública", "Integración, gestión y publicación del Inventario de entidades del Sector Público Estatal, Autonómico y Local"], solo=[1, 2, 3, 4, 12], titulo="Artículo 11.1, letras a) a c) y k) (RD 206/2024)"),
  fichab("Qué hace la IGAE, además del control interno",
         "La IGAE",
         ["Control interno: función interventora, control financiero permanente y auditoría pública (letra a)", "Control de subvenciones y **Base de Datos Nacional de Subvenciones** (letra b)", "Dirección y gestión de la **contabilidad pública** (letra c; LGP, art. 125)", "**Inventario** de entidades del sector público (letra k; Ley 40/2015)"],
         "—",
         "Son preguntas de otros temas que nombran a la IGAE: la **BDNS** (tema IV.7) y el **Inventario de entidades** (tema I.9). En ambos casos el órgano es la IGAE."))}

{unidad("1.3 Órganos a través de los que actúa (RD 206/2024, art. 11.2)",
  lit("RD206_2024", "a1-3", ["La Intervención General de la Defensa", "La Intervención General de la Seguridad Social", "Las Intervenciones Delegadas en los departamentos ministeriales"], solo=list(range(22, 30)), titulo="Artículo 11.2 (RD 206/2024)"),
  fichab("Estructura territorial y sectorial del control",
         "Estructura central de la IGAE y los órganos de la lista",
         ["Intervención General de la Defensa (y Subdirección General de Contabilidad de Defensa)", "Intervención General de la Seguridad Social", "Intervenciones Delegadas en ministerios, organismos, entidades, regiones y territorios", "Intervenciones Delegadas en la Secretaría General del Tesoro y en Clases Pasivas"],
         "—",
         "La Intervención General de la **Defensa** y la de la **Seguridad Social** dependen **funcionalmente** de la IGAE (LGP, art. 143 → II.2.1)."))}
""", 2)

T.ap("s4", "II.2 Ámbito, principios y prerrogativas del control (LGP, arts. 143 y 144)", f"""
{unidad("2.1 Sobre quién y a través de quién (art. 143)",
  lit("LGP", "a143", ["sobre la totalidad de los órganos o entidades del sector público estatal", "a través de sus servicios centrales o de sus Intervenciones Delegadas", "dependientes funcionalmente"]),
  fichab("Ámbito subjetivo del control interno",
         f"La IGAE, {c('LGP', 'a143', 'a través de sus servicios centrales o de sus Intervenciones Delegadas')}; en Defensa y Seguridad Social, sus Intervenciones Generales",
         f"Sobre {c('LGP', 'a143', 'la totalidad de los órganos o entidades del sector público estatal')}",
         "—",
         "Defensa y Seguridad Social tienen **su propia** Intervención General, pero **dependiente funcionalmente** de la IGAE."))}

{unidad("2.2 Principios y prerrogativas (art. 144)",
  lit("LGP", "a144", ["autonomía, ejercicio desconcentrado y jerarquía interna", "gozarán de independencia funcional", "El procedimiento contradictorio rige la solución de las diferencias", "podrán recabar directamente", "podrán interponer los recursos y reclamaciones"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Cómo actúa la IGAE",
         "El Interventor General y sus interventores delegados",
         ["Principios: **autonomía, ejercicio desconcentrado y jerarquía interna** (144.1)", "Plena autonomía e **independencia funcional** de los controladores (144.2)", "**Procedimiento contradictorio** en la función interventora: resolución de discrepancias del art. 155 (144.3 → III.4.2)", "Prerrogativas: recabar asesoramientos, informes y documentos (144.4) e interponer recursos y reclamaciones (144.5)"],
         "—",
         "Los principios son **tres**: autonomía, ejercicio desconcentrado y **jerarquía interna** (el RD 2188/1995, art. 3.1, decía «procedimiento contradictorio» como tercero; la LGP lo trata en el apartado 3)."))}
""", 2)

T.ap("s5", "II.3 Deberes, colaboración e informes generales (LGP, arts. 145 a 147)", f"""
{unidad("3.1 Deberes del personal controlador y deber de colaboración (art. 145)",
  lit("LGP", "a145", ["guardar la confidencialidad y el secreto", "solicitará dicho acceso a la Intervención General de la Administración del Estado", "Toda persona natural o jurídica, pública o privada, estará obligada a proporcionar", "durante el plazo de cinco años"], solo=[1, 2, 3, 5, 6, 8]),
  fichab("Secreto de los controladores y obligación de colaborar",
         "Los funcionarios de control; autoridades y entidades del sector público; **toda persona** natural o jurídica",
         ["Confidencialidad y secreto; los datos solo para el control y, en su caso, para denunciar infracciones, responsabilidad contable o delito (145.1)", "El Tribunal de Cuentas pide los informes de control financiero permanente o auditoría **a la IGAE** (145.1)", "Apoyo y colaboración de autoridades y entidades (145.2)", "Datos de terceros, previo requerimiento (145.3)"],
         f"Conservación de la documentación: {c('LGP', 'a145', 'durante el plazo de cinco años')}",
         "**Cinco años** de custodia de los papeles de trabajo, contados desde la emisión del informe."))}

{unidad("3.2 Informe general al Consejo de Ministros (art. 146)",
  lit("LGP", "a146", ["presentará anualmente al Consejo de Ministros", "serán objeto de publicación en la página web"], solo=[1, 2, 4, 5]),
  fichab("Rendición anual de resultados del control",
         "La IGAE, a través del Ministro de Hacienda, al **Consejo de Ministros**",
         ["Informe general con los resultados del Plan anual de Control Financiero Permanente y del Plan anual de Auditorías", "Incluye la situación de los planes de acción (→ IV.2)", "Se publica en la web de la IGAE"],
         "**Anual**",
         "El informe general va al **Consejo de Ministros** (no a las Cortes ni al Tribunal de Cuentas)."))}

{unidad("3.3 Seguridad Social (art. 147.1)",
  lit("LGP", "a147", [], solo=[1, 2]),
  fichab("Normas de control de la Seguridad Social",
         f"{c('LGP', 'a147', 'El Gobierno a propuesta de la Intervención General de la Administración del Estado')}, a iniciativa de la Intervención General de la Seguridad Social",
         "Aprueba las normas para el control en las entidades del sistema de la Seguridad Social; en lo no previsto, se aplica el título VI de la LGP (147.2)",
         "—",
         "Propone la **IGAE**; la **iniciativa** es de la Intervención General de la Seguridad Social; aprueba el **Gobierno**."))}

{resumen([
  "La IGAE está adscrita a la Secretaría de Estado de **Presupuestos y Gastos**, con rango de **Subsecretaría** (RD 206/2024, art. 8.6).",
  "Controla **todo** el sector público estatal a través de servicios centrales e **Intervenciones Delegadas**; Defensa y Seguridad Social, mediante sus Intervenciones Generales, dependientes funcionalmente de ella (143).",
  "Principios: **autonomía, ejercicio desconcentrado y jerarquía interna**; independencia funcional; procedimiento contradictorio (144).",
  "Secreto; deber general de colaboración; custodia **cinco años**; informe general **anual** al **Consejo de Ministros** (145 y 146)."],
  "Siguiente: III. ¿Cómo se controla antes de decidir? La función interventora")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Cómo se controla antes de decidir? La función interventora (LGP, arts. 148 a 156)", donde(
  "Tercera pregunta. La primera forma de control interno actúa **antes** de que se aprueben los actos: es la **función interventora**. Aquí se ve qué es, a quién se aplica, qué fases tiene, qué gastos no se fiscalizan y qué pasa cuando el interventor no está de acuerdo o no se le ha consultado.",
  ["1 Definición, ámbito y modalidades (arts. 148 a 150)", "2 Competencias: Interventor General e interventores delegados (art. 150 bis; RD 2188/1995, art. 8)", "3 Gastos no sujetos y fiscalización de requisitos básicos (arts. 151 a 153)", "4 Plazos, reparos y discrepancias (arts. 154 y 155; RD 2188/1995, arts. 13, 14 y 16)", "5 Omisión de fiscalización (art. 156)"]))

T.ap("s6", "III.1 Definición, ámbito y modalidades (LGP, arts. 148 a 150)", f"""
{unidad("1.1 Definición (art. 148)",
  lit("LGP", "a148", ["antes de que sean aprobados", "con el fin de asegurar que su gestión se ajuste a las disposiciones aplicables en cada caso", "salvo en los actos de ordenación del pago y pago material correspondientes a devoluciones de ingresos indebidos"]),
  fichab("Control previo de legalidad de cada acto",
         "La IGAE y sus interventores (→ III.2)",
         f"Controla {c('LGP', 'a148', 'los actos del sector público estatal que den lugar al reconocimiento de derechos o a la realización de gastos, así como los ingresos y pagos que de ellos se deriven')}",
         "**Antes** de que sean aprobados",
         "La fiscalización de **derechos e ingresos del Tesoro** puede sustituirse reglamentariamente por el control financiero permanente y la auditoría, **salvo** en las devoluciones de ingresos indebidos."))}

{unidad("1.2 Ámbito y sustitución por el control financiero permanente (art. 149)",
  lit("LGP", "a149", ["la Administración General del Estado, sus organismos autónomos, y las entidades gestoras y servicios comunes de la Seguridad Social", "en sustitución de la función interventora"]),
  fichab("Dónde se aplica la función interventora",
         f"{c('LGP', 'a149', 'la Intervención General de la Administración del Estado y sus interventores delegados')}",
         ["AGE, organismos autónomos y entidades gestoras y servicios comunes de la Seguridad Social (149.1)", "Sustitución por control financiero permanente: acuerdo motivado del **Consejo de Ministros** a propuesta de la IGAE, por tipos de expedientes u órganos, o en organismos autónomos cuya actividad lo justifique (149.2)", "Si participan varias Administraciones, solo se interviene lo del ámbito estatal (149.3)"],
         "—",
         "**No** se aplica a entidades públicas empresariales, sociedades ni fundaciones: allí hay control financiero permanente o auditoría (→ IV.1 y → IV.3). La sustitución la acuerda el **Consejo de Ministros**."))}

{unidad("1.3 Modalidades y fases (art. 150)",
  lit("LGP", "a150", ["intervención formal y material", "La fiscalización previa", "La intervención del reconocimiento de las obligaciones y de la comprobación de la inversión", "La intervención formal de la ordenación del pago", "La intervención material del pago", "concurriendo el representante de la Intervención General"], solo=[1, 2, 3, 4, 5, 6, 7, 8]),
  fichab("Cómo y en qué momentos se interviene",
         "Los órganos de intervención; en la comprobación de la inversión, el representante de la Intervención General y, en su caso, un asesor",
         ["::Modalidades: **formal** (requisitos legales y documentos del expediente) y **material** (real y efectiva aplicación de los fondos). Fases (150.2):", "a) Fiscalización previa de actos que reconozcan derechos, aprueben gastos, adquieran compromisos o acuerden movimientos de fondos y valores", "b) Intervención del reconocimiento de obligaciones y de la comprobación de la inversión", "c) Intervención formal de la ordenación del pago", "d) Intervención material del pago"],
         "—",
         "Cuatro fases, en el orden del gasto (tema VI.5). La comprobación material de la inversión exige que **concurra** el representante de la Intervención."))}
""", 2)

T.ap("s7", "III.2 Competencias: Interventor General e interventores delegados (art. 150 bis; RD 2188/1995, art. 8)", f"""
{unidad("2.1 Reparto, delegación y avocación (art. 150 bis)",
  lit("LGP", "a150bis", ["se determinará por vía reglamentaria", "podrán ser delegadas en favor de los interventores delegados", "podrá avocar para sí cualquier acto o expediente que considere oportuno"]),
  fichab("Quién fiscaliza cada acto",
         "El **Interventor General** y los **interventores delegados**",
         ["Reparto: por **reglamento** (RD 2188/1995, art. 8 → III.2.2)", "Delegación de competencias del Interventor General en los interventores delegados", "**Avocación**: el Interventor General puede avocar **cualquier** acto o expediente"],
         "—",
         "La avocación **no** está prohibida ni limitada a lo delegado: el Interventor General puede avocar «cualquier acto o expediente que considere oportuno». Cayó en 2025 (→ Cierre 1)."))}

{unidad("2.2 El reparto reglamentario (RD 2188/1995, art. 8.1)",
  lit("RD2188", "a8", ["Los que hayan de ser aprobados por el Consejo de Ministros o por las Comisiones Delegadas del Gobierno", "Los que deban ser informados por el Consejo de Estado"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Qué fiscaliza el Interventor General y qué los delegados",
         "Interventor General / interventores delegados",
         ["::Interventor General, fiscalización previa de la aprobación de gastos:", "Los que aprueban el Consejo de Ministros o las Comisiones Delegadas del Gobierno", "Los que modifican otros que fiscalizó la IGAE", "Los que debe informar el Consejo de Estado o la Dirección General del Servicio Jurídico del Estado", "Todo lo demás: el interventor delegado competente por razón orgánica o territorial"],
         "—",
         "El RD 2188/1995 es **anterior** a la LGP de 2003 y remite al texto refundido de 1988 («artículo 94 de la Ley General Presupuestaria»). La LGP derogó expresamente su art. 21 y su disposición adicional primera, y lo que se le oponga (LGP, disposición derogatoria única, 1.b y 2)."))}
""", 2)

T.ap("s8", "III.3 Gastos no sujetos y fiscalización de requisitos básicos (LGP, arts. 151 a 153)", f"""
{unidad("3.1 Gastos no sometidos a fiscalización previa (art. 151)",
  lit("LGP", "a151", ["los contratos menores", "los gastos menores de 5.000 euros cuyo pago se realice mediante el procedimiento especial de anticipo de caja fija", "los gastos correspondientes a la celebración de procesos electorales", "las subvenciones con asignación nominativa", "los contratos de acceso a bases de datos y de suscripción a publicaciones", "régimen excepcional de emergencia", "con cargo a fondos librados a justificar"]),
  fichab("Excepciones a la fiscalización previa (fase a del art. 150.2)",
         "—",
         ["a) Contratos menores y asimilados", "b) Gastos periódicos y de tracto sucesivo, una vez fiscalizado el período inicial", "c) Gastos menores de **5.000 euros** pagados por **anticipo de caja fija**", "d) Gastos de procesos electorales", "e) Subvenciones con **asignación nominativa**", "f) Acceso a bases de datos y suscripción a publicaciones no sujetos a regulación armonizada", "g) Emergencia (art. 120.1 LCSP), salvo la orden de pago a justificar", "Y: gastos menores de **5.000 euros** a justificar en el **extranjero**"],
         "Límite: **5.000 euros** (caja fija y, en el extranjero, a justificar)",
         "La exención es **solo** de la fiscalización **previa**; las demás fases (obligación, pago) se intervienen. Lo que no está en la lista se fiscaliza. Cayó en 2025 (→ Cierre 1)."))}

{unidad("3.2 Régimen de requisitos básicos (art. 152)",
  lit("LGP", "a152", ["podrá acordar, que la fiscalización e intervención previas", "La existencia de crédito presupuestario y que el propuesto es el adecuado y suficiente", "Que los gastos u obligaciones se proponen a órgano competente", "será aplicable el régimen general de fiscalización previa respecto de gastos que deban ser aprobados por el Consejo de Ministros", "validaciones efectuadas de modo automático"], solo=[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12]),
  fichab("Fiscalización limitada a extremos básicos",
         "Lo acuerda el **Consejo de Ministros**, a propuesta de la IGAE",
         ["::Extremos (152.1):", "a) Crédito existente, adecuado y suficiente (y, si es plurianual, el art. 47)", "b) Órgano competente", "c) Competencia del órgano de contratación, concedente, etc., si no aprueba el gasto", "d) Obligaciones de gastos aprobados y fiscalizados favorablemente", "e) y f) Autorizaciones del Consejo de Ministros o del titular del departamento o Secretaría de Estado", "g) Otros que determine el Consejo de Ministros"],
         "—",
         "Los gastos que aprueba el **Consejo de Ministros** siguen siempre el **régimen general** (152.2). La comprobación puede hacerse con **validaciones automáticas** (152.3)."))}

{unidad("3.3 Pagos a justificar y anticipos de caja fija (art. 153)",
  lit("LGP", "a153", ["Reglamentariamente se determinarán"]),
  fichab("Remisión al reglamento", "—", "Requisitos de la fiscalización previa de órdenes de pago a justificar, de los anticipos de caja fija y de la intervención de sus cuentas justificativas", "—",
         "Estos instrumentos de pago se estudian en el tema VI.6."))}
""", 2)

T.ap("s9", "III.4 Plazos, reparos y discrepancias (LGP, arts. 154 y 155; RD 2188/1995, arts. 13, 14 y 16)", f"""
{unidad("4.1 Plazo y conformidad (RD 2188/1995, arts. 13.2 y 14)",
  lit("RD2188", "a13", ["en el plazo máximo de 10 días", "se reducirá a cinco días"], solo=[3]),
  lit("RD2188", "a14", ["mediante una diligencia firmada sin necesidad de motivarla"]),
  fichab("Cuándo fiscaliza la Intervención y cómo da su conformidad",
         "La Intervención competente",
         "Conformidad: diligencia firmada **sin motivar**",
         ["Plazo general: **10 días** desde el siguiente a la recepción", "**Cinco días** si la tramitación es **urgente** o rige la fiscalización de **requisitos básicos**"],
         "**10** días / **5** días. La conformidad **no** se motiva; el reparo **sí** (→ III.4.2)."))}

{unidad("4.2 Reparos (LGP, art. 154)",
  lit("LGP", "a154", ["deberá formular sus reparos por escrito", "suspenderá la tramitación del expediente hasta que sea solventado", "Cuando se base en la insuficiencia de crédito o el propuesto no se considere adecuado", "requisitos o trámites no esenciales", "sólo procederá la formulación de reparo cuando no se cumpla alguno de los extremos de necesaria comprobación", "sin que las mismas tengan, en ningún caso, efectos suspensivos"]),
  fichab("Desacuerdo formal de la Intervención",
         "La Intervención que fiscaliza",
         ["Por **escrito**, con cita de los preceptos legales", "Suspende la tramitación hasta que se subsane o se resuelva la discrepancia (→ III.4.3)", "Régimen general: casos de las letras a) a e) (crédito, órgano incompetente, graves irregularidades, comprobaciones materiales, nulidad o quebranto)", "Defectos **no esenciales**: informe favorable condicionado a la subsanación", "Requisitos básicos: reparo solo si falla un extremo del 152.1; las **observaciones complementarias** no suspenden"],
         "—",
         "El reparo **suspende**; las observaciones complementarias **nunca** suspenden. El informe favorable condicionado **no** cabe en el régimen de requisitos básicos (154.3)."))}

{unidad("4.3 Discrepancias (LGP, art. 155; RD 2188/1995, art. 16.1)",
  lit("LGP", "a155", ["por conducto de la Subsecretaría del departamento", "corresponderá a la Intervención General de la Administración del Estado conocer la discrepancia, siendo su resolución obligatoria para aquélla", "corresponderá al Consejo de Ministros adoptar resolución definitiva"]),
  lit("RD2188", "a16", ["en el plazo de quince días"], solo=[1]),
  fichab("Solución del desacuerdo entre gestor e Intervención (procedimiento contradictorio)",
         ["Plantea: el órgano gestor, por la **Subsecretaría** (ministerios) o el presidente o director (organismos)", "Reparo de un **interventor delegado** → resuelve la **IGAE** (obligatorio)", "Delegada en Defensa o Seguridad Social → su Intervención General; si subsiste, la IGAE", "Reparo de la **IGAE** (o confirmado por ella) → **Consejo de Ministros**, resolución definitiva"],
         "Discrepancia motivada por escrito, con cita de preceptos",
         f"El gestor plantea la discrepancia {c('RD2188', 'a16', 'en el plazo de quince días')} (RD 2188/1995)",
         "La última palabra es del **Consejo de Ministros**, solo cuando el reparo es de la IGAE o ella lo confirma."))}
""", 2)

T.ap("s10", "III.5 Omisión de fiscalización (LGP, art. 156)", f"""
{unidad("5.1 Qué pasa si no se fiscalizó (art. 156)",
  lit("LGP", "a156", ["no se podrá reconocer la obligación, ni tramitar el pago, ni intervenir favorablemente", "que no tendrá naturaleza de fiscalización", "sin que dicha competencia pueda ser objeto de delegación", "no eximirá de la exigencia de las responsabilidades"]),
  fichab("Convalidación de gastos con omisión de la función interventora",
         ["El órgano de intervención que conoce la omisión: **informe**", "El **titular del departamento** (indelegable): decide someterlo al Consejo de Ministros", "El **Consejo de Ministros**: resolución"],
         ["::El informe (que **no** es fiscalización) recoge como mínimo:", "a) Las infracciones que se habrían puesto de manifiesto", "b) Las prestaciones realizadas", "c) La procedencia de revisar los actos", "d) La existencia de crédito adecuado y suficiente"],
         "—",
         "Hasta que se subsane no se puede reconocer la obligación **ni** pagar. El acuerdo favorable del Consejo de Ministros **no** exime de responsabilidades. La competencia del ministro es **indelegable**."))}

{resumen([
  "Función interventora: control **previo** de los actos que reconocen derechos o generan gastos (148), en la **AGE, organismos autónomos y entidades gestoras y servicios comunes de la Seguridad Social** (149).",
  "Modalidades **formal y material**; cuatro fases: fiscalización previa, obligación y comprobación de la inversión, ordenación del pago y pago material (150).",
  "El Interventor General puede **delegar** y **avocar cualquier** acto o expediente (150 bis).",
  "No sujetos a fiscalización previa: contratos menores, gastos periódicos, caja fija < **5.000 €**, procesos electorales, subvenciones **nominativas**, bases de datos, emergencia (151).",
  "Reparo **por escrito** y **suspensivo** (154); discrepancias: la **IGAE** o, en último término, el **Consejo de Ministros** (155); omisión: informe y Consejo de Ministros (156)."],
  "Siguiente: IV. ¿Cómo se controla después? Control financiero permanente y auditoría pública")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Cómo se controla después? Control financiero permanente y auditoría pública (LGP, arts. 157 a 170)", donde(
  "Cuarta pregunta. Las otras dos formas de control interno no examinan cada acto antes de aprobarlo: el **control financiero permanente** verifica de forma **continua** y la **auditoría pública**, **con posterioridad** y de forma sistemática.",
  ["1 Control financiero permanente: definición, ámbito y contenido (arts. 157 a 159; RD 2188/1995, art. 35)", "2 Planes de acción (art. 161)", "3 Auditoría pública: definición, ámbito y modalidades (arts. 162 a 164)", "4 Plan anual de auditorías e informes (arts. 165 y 166)", "5 Auditoría de cuentas anuales y auditorías específicas (arts. 167 a 170)"]))

T.ap("s11", "IV.1 Control financiero permanente (LGP, arts. 157 a 159; RD 2188/1995, art. 35)", f"""
{unidad("1.1 Definición (art. 157)",
  lit("LGP", "a157", ["de una forma continua realizada a través de la correspondiente intervención delegada", "cumplimiento del objetivo de estabilidad presupuestaria y de equilibrio financiero"]),
  fichab("Verificación continua de la gestión económico-financiera",
         c("LGP", "a157", "la correspondiente intervención delegada"),
         f"Verifica {c('LGP', 'a157', 'la situación y el funcionamiento de las entidades del sector público estatal en el aspecto económico-financiero')}",
         "—",
         "Clave: «de una forma **continua**», a través de la **intervención delegada**."))}

{unidad("1.2 Ámbito (art. 158)",
  lit("LGP", "a158", ["La Administración General del Estado", "Las entidades públicas empresariales", "Las autoridades administrativas independientes", "Las mutuas colaboradoras con la Seguridad Social", "se sustituya por las actuaciones de auditoría pública"]),
  fichab("Dónde se ejerce el control financiero permanente",
         "—",
         ["a) AGE", "b) Organismos autónomos", "c) Entidades públicas empresariales", "d) Autoridades administrativas independientes, salvo su ley", "e) Entidades gestoras y servicios comunes de la Seguridad Social", "f) Mutuas colaboradoras, en los supuestos del art. 100 LGSS", "g) Entidades del art. 2.2.i) LGP, salvo su ley"],
         "—",
         "En entidades públicas empresariales y entidades del 2.2.i), el **Consejo de Ministros** puede sustituirlo por **auditoría pública** (158.2). Coincide con la función interventora en la AGE, los organismos autónomos y la Seguridad Social: allí conviven."))}

{unidad("1.3 Contenido, informes y plan anual (art. 159)",
  lit("LGP", "a159", ["a los que no se extiende la función interventora", "Seguimiento de la ejecución presupuestaria", "Comprobación de la planificación, gestión y situación de la tesorería", "Anualmente se elaborará un informe comprensivo", "plan anual de control financiero permanente"]),
  fichab("Qué incluye el control financiero permanente",
         "Las intervenciones delegadas, según el **plan anual** de la IGAE",
         ["a) Normativa en lo que no alcanza la función interventora", "b) Ejecución presupuestaria y objetivos de los programas", "c) Informe sobre la propuesta de distribución de resultados (art. 129)", "d) Tesorería", "e) Otras actuaciones atribuidas a las intervenciones delegadas", "f) Racionalidad económico-financiera y buena gestión", "g) Verificación, con técnicas de auditoría, de los datos que soportan la información contable"],
         ["Las actuaciones se documentan en **informes**", "Informe **anual** comprensivo de resultados", "**Plan anual** de control financiero permanente de la IGAE, modificable"],
         "Cubre **lo que no alcanza** la función interventora (159.1 a)."))}

{unidad("1.4 Formas de ejercicio del control financiero en el reglamento (RD 2188/1995, art. 35.1)",
  lit("RD2188", "a35", ["mediante auditorías u otras técnicas de control"], solo=[1]),
  fichab("Técnicas del control financiero",
         "La IGAE",
         f"{c('RD2188', 'a35', 'mediante auditorías u otras técnicas de control')}, según el reglamento y {c('RD2188', 'a35', 'las normas de auditoría e Instrucciones que dicte la Intervención General de la Administración del Estado')}",
         "—",
         "**No** «únicamente» auditorías, ni externas, ni por mandato del Tribunal de Cuentas. Cayó en 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s12", "IV.2 Planes de acción (LGP, art. 161)", f"""
{unidad("2.1 Medidas correctoras de cada ministerio (art. 161)",
  lit("LGP", "a161", ["Cada departamento ministerial elaborará un Plan de Acción", "en el plazo de 3 meses", "dispondrá de un plazo de un mes para modificar el Plan", "lo elevará al Consejo de Ministros"]),
  fichab("Corrección de las deficiencias detectadas en el control",
         ["Elabora: **cada departamento ministerial** (también para sus organismos y entidades)", "Valora: la IGAE", "Toma razón: el Consejo de Ministros, si las deficiencias son graves o falta el plan"],
         "Medidas concretas y, en su caso, calendario; el departamento hace el seguimiento",
         ["Remisión: **3 meses** desde que el ministro recibe los informes", "Modificación tras la objeción de la IGAE: **un mes**"],
         "Se aplica también a los informes de **auditoría pública** (166.3). **3 meses** para el plan; **1 mes** para corregirlo."))}
""", 2)

T.ap("s13", "IV.3 Auditoría pública: definición, ámbito y modalidades (LGP, arts. 162 a 164)", f"""
{unidad("3.1 Definición (art. 162)",
  lit("LGP", "a162", ["realizada con posterioridad y efectuada de forma sistemática", "procedimientos de revisión selectivos"]),
  fichab("Verificación posterior y sistemática",
         "La IGAE",
         f"Con {c('LGP', 'a162', 'procedimientos de revisión selectivos contenidos en las normas de auditoría e instrucciones')} de la IGAE",
         "**Con posterioridad**",
         "Tres adverbios para distinguir: función interventora, **antes**; control financiero permanente, **continuo**; auditoría, **después** y **sistemática**."))}

{unidad("3.2 Ámbito (art. 163)",
  lit("LGP", "a163", ["sobre todos los órganos y entidades integrantes del sector público estatal", "en función de lo previsto en el plan anual de auditorías"]),
  fichab("Sobre quién se hace auditoría pública", "La IGAE",
         "Todo el sector público estatal, según el plan anual, sin perjuicio de la función interventora, el control financiero permanente y la auditoría privada de las sociedades mercantiles",
         "—", "Es la forma de control con el ámbito **más amplio**: **todos** los órganos y entidades del sector público estatal."))}

{unidad("3.3 Modalidades (art. 164)",
  lit("LGP", "a164", ["La auditoría de regularidad contable", "La auditoría de cumplimiento", "La auditoría operativa", "se combinen objetivos"]),
  fichab("Tipos de auditoría pública", "La IGAE",
         ["a) **Regularidad contable**: adecuación de la información contable a la normativa", "b) **Cumplimiento**: actos y procedimientos conformes a las normas", "c) **Operativa**: racionalidad económico-financiera y buena gestión", "Pueden combinarse (164.2)"],
         "—", "La operativa es la que da una «valoración **independiente** de su racionalidad económico-financiera»; la de cumplimiento mira la **legalidad**."))}
""", 2)

T.ap("s14", "IV.4 Plan anual de auditorías e informes (LGP, arts. 165 y 166)", f"""
{unidad("4.1 Plan anual de auditorías (art. 165)",
  lit("LGP", "a165", ["elaborará anualmente un plan de auditorías", "ayudas y subvenciones públicas", "podrá modificar"]),
  fichab("Programa anual de la auditoría pública", "La IGAE (incluye lo que ejecutan las Intervenciones Generales de Defensa y Seguridad Social)",
         "Recoge las auditorías del ejercicio y las de ayudas y subvenciones públicas", "**Anual**; modificable si hay circunstancias que lo justifiquen",
         "Lo elabora la **IGAE** (no el Consejo de Ministros ni el Tribunal de Cuentas)."))}

{unidad("4.2 Informes de auditoría (art. 166)",
  lit("LGP", "a166", ["se reflejarán en informes escritos", "al titular del organismo o entidad controlada, al Ministro de Hacienda y Administraciones Públicas y al del departamento", "se rendirán en todo caso al Tribunal de Cuentas junto con las cuentas anuales", "un informe resumen de las auditorías de cuentas anuales"], solo=[1, 2, 4, 5, 6]),
  fichab("Resultado de la auditoría pública",
         "La IGAE",
         ["Informes **escritos**, según las normas de la IGAE", "Destinatarios: titular de la entidad, Ministro de Hacienda y ministro del departamento", "Planes de acción como en el art. 161 (→ IV.2)", "Los de **cuentas anuales** se rinden al **Tribunal de Cuentas** con las cuentas", "Informe resumen **anual** al **Consejo de Ministros**"],
         "—",
         "Los informes de auditoría de cuentas anuales llegan al **Tribunal de Cuentas** con las cuentas (art. 139 LGP): es el enlace entre control interno y externo."))}
""", 2)

T.ap("s15", "IV.5 Auditoría de cuentas anuales y auditorías específicas (LGP, arts. 167 a 170)", f"""
{unidad("5.1 Auditoría de las cuentas anuales (arts. 167.1 y 168)",
  lit("LGP", "a167", ["la imagen fiel del patrimonio, de la situación financiera, de los resultados de la entidad"], solo=[1]),
  lit("LGP", "a168", ["realizará anualmente la auditoría de las cuentas anuales"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Modalidad de la auditoría de regularidad contable",
         "La IGAE, **anualmente**",
         ["Objeto: si las cuentas expresan la **imagen fiel** (167.1)", "Sobre: organismos autónomos, agencias, entidades públicas empresariales, autoridades independientes, entidades del 2.2.i), universidades no transferidas, mutuas (168 a)", "Fundaciones que cumplan **dos** de tres circunstancias (168 b)", "Sociedades no obligadas a auditarse incluidas en el plan, consorcios obligados y fondos sin personalidad (168 c a e)"],
         "Fundaciones: activo > **11.400.000 €**; ingresos > **22.800.000 €**; plantilla media > **250** (dos de tres)",
         "Es una modalidad de la auditoría de **regularidad contable** (no de la operativa)."))}

{unidad("5.2 Auditoría de cumplimiento y operativa (arts. 169 y 170)",
  lit("LGP", "a169", ["la verificación selectiva de la adecuación a la legalidad"]),
  lit("LGP", "a170", ["Auditoría de programas presupuestarios", "Auditoría de sistemas y procedimientos", "Auditoría de economía, eficacia y eficiencia"]),
  fichab("Auditorías públicas específicas",
         "La IGAE, para los órganos y entidades incluidos en el **Plan anual de Auditorías**",
         ["Cumplimiento (169): legalidad de la gestión presupuestaria, contratación, personal, ingresos y subvenciones", "::Operativa (170), tres modalidades:", "1. De programas presupuestarios", "2. De sistemas y procedimientos", "3. De economía, eficacia y eficiencia"],
         "—",
         "La LGP regula además las auditorías de contratos-programa, planes iniciales de actuación, cuenta de los tributos estatales, empresas colaboradoras de la Seguridad Social y privatizaciones (arts. 171 a 175)."))}

### 5.3 Cuadro comparativo de las tres formas de control interno (esquema)

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| | Función interventora | Control financiero permanente | Auditoría pública |
|---|---|---|---|
| Artículos LGP | 148 a 156 | 157 a 161 | 162 a 175 |
| Momento | Antes de aprobar el acto | Continuo | Posterior y sistemático |
| Ámbito | AGE, OO. AA., entidades gestoras y servicios comunes de la SS | AGE, OO. AA., EPE, autoridades independientes, SS, mutuas, entidades 2.2.i) | Todo el sector público estatal |
| Programación | Expediente a expediente | Plan anual de control financiero permanente | Plan anual de auditorías |
| Desacuerdo | Reparo → discrepancia → IGAE / Consejo de Ministros | Plan de acción del ministerio | Plan de acción del ministerio |

{resumen([
  "Control financiero permanente: verificación **continua** por la **intervención delegada** (157) en las entidades del art. 158; informes y **plan anual** (159).",
  "El reglamento: control financiero «mediante **auditorías u otras técnicas de control**» (RD 2188/1995, art. 35.1).",
  "Planes de acción de cada ministerio: **3 meses**; si la IGAE los objeta, **un mes** para corregirlos (161).",
  "Auditoría pública: **posterior y sistemática**, sobre **todo** el sector público estatal (162 y 163); modalidades: **regularidad contable, cumplimiento y operativa** (164).",
  "Plan anual de auditorías de la **IGAE** (165); los informes de cuentas anuales van al **Tribunal de Cuentas** (166.4)."],
  "Siguiente: V. ¿Quién hace el control externo? El Tribunal de Cuentas")}
""", 2)

# =============================================================================
T.ap("bV", "V. ¿Quién hace el control externo? El Tribunal de Cuentas (CE, arts. 136 y 153; LO 2/1982; Ley 7/1988)", donde(
  "Quinta pregunta. El control **externo** lo hace un órgano que **no** forma parte del Gobierno: el **Tribunal de Cuentas**, que depende de las **Cortes Generales**. Tiene dos funciones: **fiscalizar** y **enjuiciar** la responsabilidad contable.",
  ["1 Posición constitucional y naturaleza (CE, arts. 136 y 153 d; LO 2/1982, arts. 1 a 8)", "2 La función fiscalizadora (LO 2/1982, arts. 9 a 14; Ley 7/1988, arts. 33 y 44 y disposición adicional undécima)", "3 Composición y organización (LO 2/1982, arts. 19 a 36)", "4 El enjuiciamiento contable y la responsabilidad contable (LO 2/1982, arts. 15 a 18 y 38 a 43; Ley 7/1988, arts. 49 y 72)"]))

T.ap("s16", "V.1 Posición constitucional y naturaleza (CE, arts. 136 y 153 d; LO 2/1982, arts. 1 a 8)", f"""
{unidad("1.1 El artículo 136 de la Constitución",
  lit("CE", "Artículo 136", ["Dependerá directamente de las Cortes Generales", "por delegación de ellas en el examen y comprobación de la Cuenta General del Estado", "un informe anual", "la misma independencia e inamovilidad", "Una ley orgánica"]),
  fichab("El órgano constitucional de control externo",
         "El Tribunal de Cuentas; depende de las **Cortes Generales**",
         ["Fiscaliza las cuentas y la gestión económica del Estado y del sector público (136.1)", "Examina la **Cuenta General del Estado** por **delegación** de las Cortes (136.1)", "Censura las cuentas del Estado y del sector público estatal (136.2)", "**Informe anual** a las Cortes, con las infracciones o responsabilidades (136.2)", "«sin perjuicio de su propia jurisdicción» (136.2)"],
         "Ley **orgánica** para su composición, organización y funciones (136.4)",
         "Sus miembros: misma **independencia e inamovilidad** e incompatibilidades que los **Jueces** (136.3)."))}

{unidad("1.2 Control de las Comunidades Autónomas (art. 153 d CE)",
  lit("CE", "Artículo 153", ["Por el Tribunal de Cuentas, el económico y presupuestario"], solo=[1, 5]),
  fichab("Control económico y presupuestario de las CC. AA.", c("CE", "Artículo 153", "el Tribunal de Cuentas"), "Control económico y presupuestario de la actividad de los órganos de las Comunidades Autónomas", "—",
         "Distractor habitual del art. 153: el **TC** (normas con fuerza de ley), el **Gobierno** previo dictamen del Consejo de Estado (funciones delegadas del 150.2) y la **contencioso-administrativa** (administración autonómica y reglamentos)."))}

{unidad("1.3 Naturaleza, funciones y ámbito (LO 2/1982, arts. 1, 2 y 4)",
  lit("LOTCu", "aprimero", ["supremo órgano fiscalizador", "partidos políticos", "Es único en su orden", "Depende directamente de las Cortes Generales"]),
  lit("LOTCu", "asegundo", ["La fiscalización externa, permanente y consuntiva", "El enjuiciamiento de la responsabilidad contable"]),
  lit("LOTCu", "acuarto", ["Las Comunidades Autónomas", "Las Corporaciones Locales"], solo=[1, 2, 3, 4, 5, 6, 7, 8]),
  fichab("Qué es y qué hace el Tribunal de Cuentas",
         "El Tribunal de Cuentas, **único en su orden**, con jurisdicción en todo el territorio",
         ["::Dos funciones (art. 2):", "a) Fiscalización **externa, permanente y consuntiva** del sector público", "b) **Enjuiciamiento** de la responsabilidad contable", "Fiscaliza también a los **partidos políticos** y sus fundaciones (art. 1) y las subvenciones, créditos y avales del sector público (art. 4.2)"],
         "—",
         "El «sector público» del art. 4 incluye las **Comunidades Autónomas** y las **Corporaciones Locales**, no solo el Estado. Es compatible con los órganos de control externo autonómicos (art. 1.2)."))}

{unidad("1.4 Independencia, presupuesto, colaboración y conflictos (LO 2/1982, arts. 5 a 8)",
  lit("LOTCu", "aquinto", ["plena independencia y sometimiento al ordenamiento jurídico"]),
  lit("LOTCu", "asexto", ["en una sección independiente"]),
  lit("LOTCu", "aseptimo", ["podrá exigir la colaboración de todas las personas físicas o jurídicas, públicas o privadas"], solo=[1]),
  lit("LOTCu", "aoctavo", ["serán resueltos por el Tribunal Constitucional"]),
  fichab("Garantías del Tribunal de Cuentas",
         "El Tribunal de Cuentas; los conflictos de competencias, el **Tribunal Constitucional**",
         ["**Plena independencia** (art. 5)", "Presupuesto propio, en **sección independiente** de los PGE, aprobado por las Cortes (art. 6)", "Deber de colaboración de todas las personas físicas o jurídicas (art. 7.1)"],
         "—",
         "Los conflictos sobre sus competencias los resuelve el **Tribunal Constitucional**; los requerimientos de inhibición **no suspenden** el procedimiento (art. 8)."))}
""", 2)

T.ap("s17", "V.2 La función fiscalizadora (LO 2/1982, arts. 9 a 14; Ley 7/1988, arts. 33 y 44 y disposición adicional undécima)", f"""
{unidad("2.1 Principios de la fiscalización (LO 2/1982, art. 9)",
  lit("LOTCu", "anoveno", ["legalidad, eficiencia, economía, transparencia, así como a la sostenibilidad ambiental y la igualdad de género"]),
  fichab("Parámetros de la fiscalización", "El Tribunal de Cuentas",
         "Legalidad, eficiencia, economía, transparencia, sostenibilidad ambiental e igualdad de género, en la ejecución de los programas de ingresos y gastos", "—",
         "La lista vigente incluye **transparencia, sostenibilidad ambiental e igualdad de género** (no solo legalidad, eficiencia y economía)."))}

{unidad("2.2 La Cuenta General del Estado (LO 2/1982, art. 10; Ley 7/1988, art. 33.1)",
  lit("LOTCu", "adiez", ["por delegación, de las Cortes Generales", "dentro del plazo de seis meses", "El Pleno, oído el Fiscal, dictará la declaración definitiva"]),
  lit("LFTCu", "a33", ["antes del día 31 de agosto del año siguiente", "dentro de los dos meses siguientes a su conclusión"], solo=[1]),
  fichab("Examen y comprobación de la Cuenta General del Estado",
         ["Forma la cuenta: la **IGAE** (Ley 7/1988, art. 33.1; LGP, art. 125.2 d)", "Examina y comprueba: el Tribunal de Cuentas, por **delegación de las Cortes Generales**", "Declaración definitiva: el **Pleno**, oído el Fiscal"],
         "La declaración se eleva a las Cámaras con la propuesta y se da traslado al Gobierno",
         ["IGAE: ultima la cuenta antes del **31 de agosto** del año siguiente y la remite en **dos meses**", "Tribunal: **seis meses** desde que se rinde"],
         "Delegan las **Cortes** (no el Ministro de Hacienda) y el plazo es de **seis** meses. Cayó en 2025 (→ Cierre 1)."))}

{unidad("2.3 Qué fiscaliza en particular y cómo expone los resultados (LO 2/1982, arts. 11 y 12)",
  lit("LOTCu", "aonce", ["Los contratos", "La situación y las variaciones del patrimonio", "Los créditos extraordinarios y suplementarios"]),
  lit("LOTCu", "adoce", ["informes o memorias ordinarias o extraordinarias y de mociones o notas", "se publicarán en el «Boletín Oficial del Estado»"]),
  fichab("Objeto particular y resultado de la fiscalización", "El Tribunal de Cuentas → **Cortes Generales** (y, si afecta a una CA, su Asamblea Legislativa)",
         ["Fiscaliza en particular: contratos, patrimonio y modificaciones presupuestarias (art. 11)", "Resultado: **informes o memorias** (ordinarias o extraordinarias) y **mociones o notas** (art. 12.1)", "Hace constar infracciones, abusos o prácticas irregulares y la responsabilidad (art. 12.2)"],
         "—", "Los informes se elevan a las **Cortes** y se publican en el **BOE**."))}

{unidad("2.4 El informe o memoria anual y las propuestas de mejora (LO 2/1982, arts. 13 y 14)",
  lit("LOTCu", "atrece", ["comprenderá el análisis de la Cuenta General del Estado y de las demás del sector público", "Memoria de las actuaciones jurisdiccionales"], solo=[1, 6, 7]),
  lit("LOTCu", "acatorce", ["propondrá las medidas a adoptar"], solo=[1]),
  fichab("Informe anual del art. 136.2 CE", "El Tribunal de Cuentas → Cortes Generales y Asambleas Legislativas autonómicas",
         ["Análisis de la Cuenta General del Estado y demás del sector público y de la gestión económica", "Idéntico informe a las Asambleas de las CC. AA.", "Incluye una **Memoria de las actuaciones jurisdiccionales**", "Propuesta de medidas para mejorar la gestión (art. 14)"],
         "**Anual**", "El informe anual incluye también la memoria de la actividad **jurisdiccional** (art. 13.3)."))}

{unidad("2.5 Alegaciones de los fiscalizados (Ley 7/1988, art. 44.1)",
  lit("LFTCu", "a44", ["en un plazo no superior a treinta días prorrogable con justa causa por un periodo igual"], solo=[1]),
  fichab("Trámite de audiencia en el procedimiento fiscalizador", "Los responsables del sector fiscalizado o las personas o entidades fiscalizadas",
         "Antes del proyecto de informe se les ponen de manifiesto las actuaciones para que aleguen y presenten documentos",
         "**No más de 30 días**, prorrogables con justa causa por otro tanto",
         "El informe aprobado por el Pleno debe contener las alegaciones (art. 44.4)."))}

{unidad("2.6 Informe preceptivo del Tribunal sobre las normas que le afectan (Ley 7/1988, disposición adicional undécima, añadida por la Ley 15/2014, art. 22)",
  lit("LFTCu", "undecima", ["en el plazo improrrogable de treinta días", "el plazo será de quince días"]),
  fichab("Informe del Tribunal de Cuentas sobre su propio régimen",
         "El Tribunal de Cuentas; si es anteproyecto de ley, el Gobierno remite el informe a las **Cortes Generales**",
         "Sobre anteproyectos de ley y proyectos de disposiciones reglamentarias relativos a su régimen jurídico o a sus funciones fiscalizadora o jurisdiccional",
         ["**30 días** improrrogables", "**15 días** si la orden de remisión indica urgencia", "Prórroga excepcional que puede conceder el órgano remitente"],
         "**30 / 15** días. Cayó en 2025 citando el art. 22 de la Ley 15/2014, que añadió esta disposición (→ Cierre 1)."))}
""", 2)

T.ap("s18", "V.3 Composición y organización (LO 2/1982, arts. 19 a 36)", f"""
{unidad("3.1 Órganos (art. 19)",
  lit("LOTCu", "adiecinueve", []),
  fichab("Lista de órganos del Tribunal de Cuentas", "—",
         ["Presidente", "Pleno", "Comisión de Gobierno", "Sección de **Fiscalización**", "Sección de **Enjuiciamiento**", "Consejeros de Cuentas", "Fiscalía", "Secretaría General"],
         "—", "Ocho órganos; dos **Secciones**: Fiscalización y Enjuiciamiento (una por cada función del art. 2)."))}

{unidad("3.2 El Pleno (art. 21)",
  lit("LOTCu", "aveintiuno", ["doce Consejeros de Cuentas, uno de los cuales será el Presidente, y el Fiscal", "dos tercios de sus componentes", "mayoría de asistentes", "Ejercer la función fiscalizadora"], solo=[1, 2, 3, 4]),
  fichab("Órgano colegiado superior", "**Doce** Consejeros de Cuentas (uno es el Presidente) y el **Fiscal**",
         "Ejerce la función fiscalizadora; plantea conflictos de competencias; recursos de alzada; aprueba los reglamentos del Tribunal",
         ["Quórum: **dos tercios** de sus componentes", "Acuerdos: **mayoría de asistentes**"],
         "El **Fiscal** forma parte del Pleno. Quórum de dos tercios, acuerdos por mayoría de asistentes."))}

{unidad("3.3 Presidente y Consejeros de Cuentas (arts. 29, 30 y 36)",
  lit("LOTCu", "aveintinueve", ["por el Rey, a propuesta del mismo Tribunal en Pleno y por un período de tres años"]),
  lit("LOTCu", "atreinta", ["seis por el Congreso de los Diputados y seis por el Senado", "mayoría de tres quintos de cada una de las Cámaras", "por un período de nueve años", "con más de quince años de ejercicio profesional", "como mínimo el cuarenta por ciento", "independientes e inamovibles"]),
  lit("LOTCu", "atreintayseis", ["agotamiento de su mandato"]),
  fichab("Nombramiento y estatuto de los miembros",
         ["Consejeros: las **Cortes**, **seis** por el Congreso y **seis** por el Senado", "Presidente: el **Rey**, entre los Consejeros, a propuesta del **Pleno**"],
         "Consejeros entre censores, magistrados y fiscales, profesores, funcionarios de cuerpos superiores, abogados, economistas y profesores mercantiles, de reconocida competencia; presencia equilibrada (**40 %** mínimo de cada sexo por Cámara)",
         ["Consejeros: **tres quintos** de cada Cámara, **nueve años**, más de **quince** años de ejercicio profesional", "Presidente: **tres años**"],
         "Consejeros **9** años; Presidente **3** años. Solo cesan por las causas tasadas del art. 36 (mandato, renuncia aceptada por las Cortes, incapacidad, incompatibilidad o incumplimiento grave)."))}
""", 2)

T.ap("s19", "V.4 El enjuiciamiento contable y la responsabilidad contable (LO 2/1982, arts. 15 a 18 y 38 a 43; Ley 7/1988, arts. 49 y 72)", f"""
{unidad("4.1 La jurisdicción contable (LO 2/1982, arts. 15 a 18)",
  lit("LOTCu", "aquince", ["como jurisdicción propia del Tribunal de Cuentas", "a los alcances de caudales o efectos públicos"]),
  lit("LOTCu", "adieciseis", ["Los hechos constitutivos de delito o falta"]),
  lit("LOTCu", "adiecisiete", ["necesaria e improrrogable, exclusiva y plena"], solo=[1]),
  lit("LOTCu", "adieciocho", ["es compatible respecto de unos mismos hechos con el ejercicio de la potestad disciplinaria y con la actuación de la jurisdicción penal", "la responsabilidad civil será determinada por la jurisdicción contable"]),
  fichab("Función jurisdiccional del Tribunal de Cuentas",
         "Los Consejeros de Cuentas (primera o única instancia) y las Salas de la Sección de Enjuiciamiento",
         ["Sobre las cuentas de quienes recauden, intervengan, administren, custodien, manejen o utilicen bienes, caudales o efectos públicos (art. 15)", "Excluidos: asuntos del TC, contencioso-administrativos, delitos y cuestiones civiles, laborales o de otros órdenes (art. 16)", "Caracteres: **necesaria e improrrogable, exclusiva y plena** (art. 17.1)"],
         "—",
         "**Compatible** con la potestad disciplinaria y con la jurisdicción penal; si hay delito, la responsabilidad **civil** la fija la jurisdicción **contable** (art. 18)."))}

{unidad("4.2 Pretensiones de responsabilidad contable y alcance (Ley 7/1988, arts. 49.1 y 72.1)",
  lit("LFTCu", "a49", ["con dolo, culpa o negligencia graves", "Sólo conocerá de las responsabilidades subsidiarias, cuando la responsabilidad directa, previamente declarada y no hecha efectiva, sea contable"], solo=[1]),
  lit("LFTCu", "a72", ["el saldo deudor injustificado de una cuenta"], solo=[1]),
  fichab("Cuándo hay responsabilidad contable",
         "Quienes tengan a su cargo el manejo de caudales o efectos públicos",
         ["Menoscabo de caudales o efectos públicos por acciones u omisiones contrarias a las leyes presupuestarias y de contabilidad", "Con **dolo, culpa o negligencia graves**", "**Alcance**: saldo deudor injustificado o ausencia de numerario o de justificación en las cuentas"],
         "—",
         "Se exige dolo, culpa o negligencia **graves**. La subsidiaria solo se conoce cuando la directa, declarada y no hecha efectiva, es contable."))}

{unidad("4.3 Clases y alcance de la responsabilidad (LO 2/1982, arts. 38 y 39)",
  lit("LOTCu", "atreintayocho", ["directa o subsidiaria", "La responsabilidad directa será siempre solidaria y comprenderá todos los perjuicios causados", "Respecto a los responsables subsidiarios", "se transmiten a los causahabientes"]),
  lit("LOTCu", "atreintaynueve", ["obediencia debida, siempre que hubieren advertido por escrito"], solo=[1]),
  ficha("Quien por acción u omisión contraria a la Ley origine menoscabo de caudales o efectos públicos; y sus causahabientes",
        "Indemnizar los daños y perjuicios causados",
        ["Directa: **siempre solidaria** y por **todos** los perjuicios", "Subsidiaria: limitada a los perjuicios consecuencia de sus actos; **moderable** de forma prudencial y equitativa", "Causahabientes: si aceptan la herencia, solo hasta su **importe líquido**"],
        "Exención por obediencia debida si se advirtió **por escrito** la imprudencia o ilegalidad de la orden (art. 39.1)",
        "La moderación prudencial es de la **subsidiaria**, no de la directa. Cayó en 2025 (→ Cierre 1)."))}

{unidad("4.4 Responsables directos y subsidiarios (LO 2/1982, arts. 42.1 y 43)",
  lit("LOTCu", "acuarentaydos", ["quienes hayan ejecutado, forzado o inducido a ejecutar o cooperado"], solo=[1]),
  lit("LOTCu", "acuarentaytres", ["por negligencia o demora", "sólo procede cuando no hayan podido hacerse efectivas las directas"]),
  ficha("Directos: autores, inductores, cooperadores y encubridores posteriores. Subsidiarios: quienes por negligencia o demora en obligaciones expresas dieron ocasión al menoscabo",
        "—",
        "La subsidiaria **solo** procede cuando no se han podido hacer efectivas las directas (art. 43.2)",
        "—",
        "Directo = **participación** en los hechos; subsidiario = **negligencia o demora**."))}

{resumen([
  "Tribunal de Cuentas: «**supremo** órgano fiscalizador»; depende de las **Cortes Generales**; único en su orden (CE 136; LO 2/1982, art. 1).",
  "Dos funciones: fiscalización **externa, permanente y consuntiva** y **enjuiciamiento** de la responsabilidad contable (art. 2).",
  "Cuenta General del Estado: por **delegación de las Cortes**, en **seis meses** (art. 10); informe anual a las Cortes (art. 13).",
  "Pleno: **12** Consejeros (uno, Presidente) y el **Fiscal**; Consejeros: **6** Congreso + **6** Senado, **3/5**, **9 años**; Presidente: el Rey, a propuesta del Pleno, **3 años**.",
  "Jurisdicción contable **necesaria, improrrogable, exclusiva y plena**; responsabilidad **directa** (solidaria, todos los perjuicios) o **subsidiaria** (moderable); se transmite a los causahabientes hasta el **líquido** de la herencia."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_L88 = examen("L", 88, {
  "a": f"Literal del art. 150 bis: {c('LGP', 'a150bis', 'el Interventor General podrá avocar para sí cualquier acto o expediente que considere oportuno')}.",
  "b": f"Cambia el alcance: la avocación no se limita a lo delegado; la ley habla de {c('LGP', 'a150bis', 'cualquier acto o expediente')}.",
  "c": f"Falso: el art. 150 bis la permite expresamente ({c('LGP', 'a150bis', 'podrá avocar para sí')}).",
  "d": "Cambia el objeto: la intervención material es solo una modalidad de la función interventora (art. 150.1); la avocación alcanza a cualquier acto o expediente."},
  [("Cualquier acto o expediente que considere oportuno", "LGP", "a150bis", "el Interventor General podrá avocar para sí cualquier acto o expediente que considere oportuno")])
EX_P91 = examen("P", 91, {
  "a": f"No sujeta: art. 151 e), {c('LGP', 'a151', 'las subvenciones con asignación nominativa')}.",
  "b": f"No sujeto: art. 151 f), {c('LGP', 'a151', 'los contratos de acceso a bases de datos y de suscripción a publicaciones que no tengan el carácter de contratos sujetos a regulación armonizada')}.",
  "c": f"No sujeto: art. 151 d), {c('LGP', 'a151', 'los gastos correspondientes a la celebración de procesos electorales')}.",
  "d": f"No está en la lista del art. 151. La excepción por importe es solo para {c('LGP', 'a151', 'los gastos menores de 5.000 euros cuyo pago se realice mediante el procedimiento especial de anticipo de caja fija')}: un pago en firme de 9.000 euros no entra en ella. ⚠ Matiz (posible impugnación): también están exentos {c('LGP', 'a151', 'los contratos menores')} (art. 151 a), y son menores los de suministro de valor estimado {c('LCSP', 'Artículo 118', 'a 15.000 euros, cuando se trate de contratos de suministro o de servicios')} (LCSP, art. 118.1, «inferior a»). Si esa compra se tramitara como contrato menor, tampoco se fiscalizaría; el enunciado no lo dice y la plantilla da la d)."},
  [("9.000 euros", "LGP", "a151", "los gastos menores de 5.000 euros cuyo pago se realice mediante el procedimiento especial de anticipo de caja fija")])
EX_X94 = examen("X", 94, {
  "a": f"Literal del art. 35.1: {c('RD2188', 'a35', 'El control financiero se ejercerá mediante auditorías u otras técnicas de control')}.",
  "b": f"Cambia dos datos: no «únicamente» auditorías (también {c('RD2188', 'a35', 'otras técnicas de control')}) y no bajo mandato del Tribunal de Cuentas, sino según {c('RD2188', 'a35', 'las normas de auditoría e Instrucciones que dicte la Intervención General de la Administración del Estado')}.",
  "c": f"Cambia «auditorías u otras técnicas» por «únicamente auditorías externas»: el art. 35 admite {c('RD2188', 'a35', 'otras técnicas de control')} y las hace la propia IGAE.",
  "d": "Falso: el art. 35 regula expresamente las auditorías y las somete a las normas e instrucciones de la IGAE."},
  [("auditorías u otras técnicas de control", "RD2188", "a35", "El control financiero se ejercerá mediante auditorías u otras técnicas de control")])
EX_P90 = examen("P", 90, {
  "a": f"Literal del art. 10: {c('LOTCu', 'adiez', 'por delegación, de las Cortes Generales, procederá al examen y comprobación de la Cuenta General del Estado dentro del plazo de seis meses')}.",
  "b": f"Cambia el plazo: son {c('LOTCu', 'adiez', 'seis meses')}, no tres.",
  "c": f"Cambia el órgano: delegan {c('LOTCu', 'adiez', 'las Cortes Generales')} (también art. 136.1 CE), no el Ministro de Hacienda.",
  "d": "Cambia el órgano y el plazo: ni el Ministro de Hacienda ni tres meses."},
  [("Cortes Generales", "LOTCu", "adiez", "por delegación, de las Cortes Generales"), ("seis meses", "LOTCu", "adiez", "dentro del plazo de seis meses")])
EX_X93 = examen("X", 93, {
  "a": f"Cambia los plazos: son {c('L15_2014', 'a22', 'el plazo improrrogable de treinta días')} y, con urgencia, quince.",
  "b": f"Cambia los plazos: sesenta y treinta días no aparecen; la ley dice treinta y {c('L15_2014', 'a22', 'el plazo será de quince días')}.",
  "c": "Cambia los plazos: ni dos meses ni diez días.",
  "d": f"Literal de la disposición adicional undécima de la Ley 7/1988, añadida por el art. 22 de la Ley 15/2014: {c('L15_2014', 'a22', 'El Tribunal de Cuentas emitirá su informe en el plazo improrrogable de treinta días. Si en la orden de remisión se hiciere constar la urgencia del informe, el plazo será de quince días')}."},
  [("Treinta días", "L15_2014", "a22", "emitirá su informe en el plazo improrrogable de treinta días"), ("quince días", "L15_2014", "a22", "el plazo será de quince días")])
EX_L89 = examen("L", 89, {
  "a": f"Literal del art. 38.5: {c('LOTCu', 'atreintayocho', 'se transmiten a los causahabientes de los responsables por la aceptación expresa o tácita de la herencia, pero sólo en la cuantía a que ascienda el importe líquido de la misma')}.",
  "b": f"Generaliza a toda responsabilidad lo que es solo de la directa: {c('LOTCu', 'atreintayocho', 'La responsabilidad directa será siempre solidaria y comprenderá todos los perjuicios causados')}.",
  "c": f"Cambia «subsidiaria» por «directa»: la limitación y la moderación son {c('LOTCu', 'atreintayocho', 'Respecto a los responsables subsidiarios')}.",
  "d": f"El alcance no convierte la responsabilidad en subsidiaria: la ley distingue {c('LOTCu', 'atreintayocho', 'La responsabilidad podrá ser directa o subsidiaria')} según la participación (arts. 42 y 43), y el alcance es objeto de la jurisdicción contable (art. 15.2)."},
  [("causahabientes", "LOTCu", "atreintayocho", "se transmiten a los causahabientes de los responsables"), ("importe líquido", "LOTCu", "atreintayocho", "sólo en la cuantía a que ascienda el importe líquido de la misma")])

T.ap("s20", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **seis** preguntas de este tema: dos de la función interventora, una del control financiero y tres del Tribunal de Cuentas. Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-L 2025, pregunta 88 · Avocación por el Interventor General (→ III.2.1)", EX_L88,
  "### GACE-P 2025, pregunta 91 · Gastos no sujetos a fiscalización previa (→ III.3.1)", EX_P91,
  "### GACE-L 2025 extraordinario, pregunta 94 · Formas del control financiero (→ IV.1.4)", EX_X94,
  "### GACE-P 2025, pregunta 90 · Cuenta General del Estado (→ V.2.2)", EX_P90,
  "### GACE-L 2025 extraordinario, pregunta 93 · Informe preceptivo del Tribunal de Cuentas (→ V.2.6)", EX_X93,
  "### GACE-L 2025, pregunta 89 · Responsabilidad contable (→ V.4.3)", EX_L89,
  "### Cómo se pregunta",
  "!> Las preguntas de este tema citan el **artículo** y cambian **un dato**: el plazo (seis/tres meses; treinta/quince días), el órgano (Cortes/Ministro de Hacienda), el alcance («cualquier acto» frente a «solo lo delegado»; «auditorías u otras técnicas» frente a «únicamente auditorías») o la clase de responsabilidad (directa/subsidiaria).",
]))

T.ap("s21", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Control externo e interno | Tribunal de Cuentas (externo) e IGAE (interno, plena autonomía) (140); objetivos y tres formas (142) | Tres formas: **función interventora, control financiero permanente, auditoría pública** |
| II. La IGAE | Secretaría de Estado de Presupuestos y Gastos, rango de Subsecretaría; Intervenciones Delegadas; Defensa y SS dependen funcionalmente (143) | Principios: **autonomía, ejercicio desconcentrado y jerarquía interna** (144) |
| III. Función interventora | Control previo; formal y material; cuatro fases; no sujetos (151); requisitos básicos (152); reparos, discrepancias, omisión | **Avocar cualquier acto** (150 bis); caja fija < **5.000 €**; última palabra, **Consejo de Ministros** |
| IV. CFP y auditoría | CFP continuo por la intervención delegada (157-159); planes de acción (161); auditoría posterior y sistemática (162-170) | «**auditorías u otras técnicas de control**» (RD 2188/1995, art. 35); plan de acción **3 meses** |
| V. Tribunal de Cuentas | Depende de las Cortes; fiscalización y enjuiciamiento; Pleno de 12 + Fiscal; responsabilidad directa y subsidiaria | Cuenta General: **delegación de las Cortes, seis meses**; informe preceptivo **30/15 días** |

?> **Trampas frecuentes:** «la avocación está prohibida» (el Interventor General puede avocar **cualquier** acto); «el control financiero se ejerce **únicamente** mediante auditorías» (también **otras técnicas**); «el **Ministro de Hacienda** delega en el Tribunal la Cuenta General» (son las **Cortes**); «la responsabilidad **directa** puede moderarse» (eso es la **subsidiaria**); «el Presidente del Tribunal lo nombran las Cortes por nueve años» (lo nombra el **Rey**, a propuesta del **Pleno**, por **tres** años; los nueve años son de los **Consejeros**).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
T.q("LGP", "a140", "Control externo e interno", "Según el artículo 140 de la Ley 47/2003, General Presupuestaria, el control interno de la gestión económica y financiera del sector público estatal corresponde:",
    ["A la Intervención General de la Administración del Estado.", "Al Tribunal de Cuentas.", "A la Dirección General de Presupuestos.", "A la Autoridad Independiente de Responsabilidad Fiscal."],
    "Art. 140.2 LGP; el control externo es del Tribunal de Cuentas (140.1).", "La Intervención General de la Administración del Estado ejercerá en los términos previstos en esta ley el control interno")
T.q("LGP", "a140", "Control externo e interno", "Según el artículo 140.2 de la Ley General Presupuestaria, la IGAE ejercerá el control interno respecto de las autoridades y entidades cuya gestión controle:",
    ["Con plena autonomía.", "Bajo la dependencia jerárquica del Ministro del departamento controlado.", "Por delegación del Tribunal de Cuentas.", "Con sujeción a las instrucciones del órgano gestor."],
    "Art. 140.2 LGP.", "con plena autonomía respecto de las autoridades y demás entidades cuya gestión controle")
T.q("LGP", "a142", "Control externo e interno", "Según el artículo 142.2 de la Ley General Presupuestaria, el control interno se realizará mediante:",
    ["La función interventora, el control financiero permanente y la auditoría pública.", "La función interventora, la fiscalización externa y el enjuiciamiento contable.", "El control de eficacia, la auditoría privada y la contabilidad analítica.", "La fiscalización previa, la censura de cuentas y el control parlamentario."],
    "Art. 142.2 LGP.", "El control se realizará mediante el ejercicio de la función interventora, el control financiero permanente y la auditoría pública")
T.q("RD206_2024", "a8", "La IGAE", "Según el Real Decreto 206/2024, de estructura del Ministerio de Hacienda, la Intervención General de la Administración del Estado está adscrita a:",
    ["La Secretaría de Estado de Presupuestos y Gastos, con rango de Subsecretaría.", "La Secretaría de Estado de Hacienda, con rango de Dirección General.", "La Subsecretaría de Hacienda, con rango de Subdirección General.", "La Presidencia del Gobierno, con rango de Secretaría de Estado."],
    "Art. 8.6 RD 206/2024.", "Está adscrita a la Secretaría de Estado de Presupuestos y Gastos, la Intervención General de la Administración del Estado, con rango de Subsecretaría")
T.q("LGP", "a143", "La IGAE", "Según el artículo 143 de la Ley General Presupuestaria, en el ámbito del Ministerio de Defensa y de la Seguridad Social, el control se ejercerá a través de sus respectivas Intervenciones Generales:",
    ["Dependientes funcionalmente, a estos efectos, de la Intervención General de la Administración del Estado.", "Independientes de la Intervención General de la Administración del Estado.", "Dependientes funcionalmente del Tribunal de Cuentas.", "Dependientes orgánicamente de la Subsecretaría de Hacienda."],
    "Art. 143 LGP.", "dependientes funcionalmente, a estos efectos, de la Intervención General de la Administración del Estado")
T.q("LGP", "a144", "La IGAE", "Según el artículo 144.1 de la Ley General Presupuestaria, la IGAE ejercerá sus funciones de control conforme a los principios de:",
    ["Autonomía, ejercicio desconcentrado y jerarquía interna.", "Autonomía, ejercicio centralizado y coordinación.", "Legalidad, eficiencia y economía.", "Jerarquía, descentralización y procedimiento sumario."],
    "Art. 144.1 LGP.", "conforme a los principios de autonomía, ejercicio desconcentrado y jerarquía interna")
T.q("LGP", "a145", "La IGAE", "Según el artículo 145.5 de la Ley General Presupuestaria, la IGAE conservará y custodiará la documentación integrante de las auditorías públicas o de los controles financieros permanentes durante el plazo de:",
    ["Cinco años.", "Cuatro años.", "Diez años.", "Dos años."], "Art. 145.5 LGP.", "conservará y custodiará durante el plazo de cinco años")
T.q("LGP", "a146", "La IGAE", "Según el artículo 146.1 de la Ley General Presupuestaria, la IGAE presentará anualmente un informe general con los resultados más significativos de la ejecución del Plan anual de Control Financiero Permanente y del Plan anual de Auditorías:",
    ["Al Consejo de Ministros, a través del Ministro de Hacienda.", "A las Cortes Generales, a través de la Comisión Mixta.", "Al Tribunal de Cuentas.", "Al Consejo de Estado."],
    "Art. 146.1 LGP.", "presentará anualmente al Consejo de Ministros a través del Ministro de Hacienda")
T.q("LGP", "a148", "Función interventora", "Según el artículo 148 de la Ley General Presupuestaria, la función interventora tiene por objeto controlar los actos del sector público estatal que den lugar al reconocimiento de derechos o a la realización de gastos:",
    ["Antes de que sean aprobados.", "Después de su aprobación y antes del pago.", "Una vez finalizado el ejercicio presupuestario.", "De forma continua, a través de técnicas de auditoría."],
    "Art. 148 LGP.", "controlar, antes de que sean aprobados")
T.q("LGP", "a149", "Función interventora", "Según el artículo 149.1 de la Ley General Presupuestaria, la función interventora se ejercerá respecto de los actos realizados por:",
    ["La Administración General del Estado, sus organismos autónomos, y las entidades gestoras y servicios comunes de la Seguridad Social.", "Todas las entidades del sector público estatal, incluidas las sociedades mercantiles.", "Las entidades públicas empresariales y las fundaciones del sector público estatal.", "La Administración General del Estado exclusivamente."],
    "Art. 149.1 LGP.", "la Administración General del Estado, sus organismos autónomos, y las entidades gestoras y servicios comunes de la Seguridad Social")
T.q("LGP", "a149", "Función interventora", "Según el artículo 149.2 de la Ley General Presupuestaria, ¿quién puede acordar la aplicación del control financiero permanente en sustitución de la función interventora?",
    ["El Consejo de Ministros, a propuesta de la IGAE.", "El Ministro de Hacienda, a propuesta del Tribunal de Cuentas.", "El Interventor General, mediante resolución.", "Las Cortes Generales, mediante ley."],
    "Art. 149.2 LGP.", "El Consejo de Ministros, a propuesta de la Intervención General de la Administración del Estado, podrá acordar de forma motivada la aplicación del control financiero permanente")
T.q("LGP", "a150", "Función interventora", "Según el artículo 150.1 de la Ley General Presupuestaria, la verificación del cumplimiento de los requisitos legales necesarios para la adopción del acuerdo, mediante el examen de los documentos del expediente, es:",
    ["La intervención formal.", "La intervención material.", "La comprobación material de la inversión.", "La auditoría de cumplimiento."],
    "Art. 150.1 LGP; en la material «se comprobará la real y efectiva aplicación de los fondos públicos».", "La intervención formal consistirá en la verificación del cumplimiento de los requisitos legales necesarios para la adopción del acuerdo")
T.q("LGP", "a150", "Función interventora", "Según el artículo 150.2 de la Ley General Presupuestaria, ¿cuál de las siguientes NO es una de las fases que comprende el ejercicio de la función interventora?",
    ["La auditoría de las cuentas anuales.", "La intervención formal de la ordenación del pago.", "La intervención material del pago.", "La intervención del reconocimiento de las obligaciones y de la comprobación de la inversión."],
    "Art. 150.2 LGP: fiscalización previa; reconocimiento de obligaciones y comprobación de la inversión; ordenación del pago; pago material. La auditoría es otra forma de control (arts. 162 y ss.).", "La intervención formal de la ordenación del pago")
T.q("LGP", "a150bis", "Función interventora", "Según el artículo 150 bis de la Ley General Presupuestaria, la distribución de competencias entre el Interventor General y los interventores delegados se determinará:",
    ["Por vía reglamentaria.", "Por la Ley de Presupuestos Generales del Estado de cada año.", "Por acuerdo del Tribunal de Cuentas.", "Por orden del Ministro de cada departamento."],
    "Art. 150 bis LGP.", "se determinará por vía reglamentaria")
T.q("RD2188", "a8", "Función interventora", "Según el artículo 8.1 a) del Real Decreto 2188/1995, el Interventor General de la Administración del Estado ejercerá la fiscalización previa de la aprobación de los gastos:",
    ["Que hayan de ser aprobados por el Consejo de Ministros o por las Comisiones Delegadas del Gobierno.", "De cuantía inferior a 5.000 euros.", "Que aprueben los Delegados del Gobierno.", "De los organismos autónomos, en todo caso."],
    "Art. 8.1 a) 1.º RD 2188/1995.", "Los que hayan de ser aprobados por el Consejo de Ministros o por las Comisiones Delegadas del Gobierno")
T.q("LGP", "a151", "Función interventora", "Según el artículo 151 de la Ley General Presupuestaria, no estarán sometidos a fiscalización previa los gastos menores de 5.000 euros cuyo pago se realice mediante:",
    ["El procedimiento especial de anticipo de caja fija.", "Transferencia bancaria ordinaria.", "Pagos a justificar en territorio nacional.", "Compensación de deudas."],
    "Art. 151 c) LGP.", "los gastos menores de 5.000 euros cuyo pago se realice mediante el procedimiento especial de anticipo de caja fija")
T.q("LGP", "a151", "Función interventora", "Según el artículo 151 de la Ley General Presupuestaria, NO están sometidas a fiscalización previa:",
    ["Las subvenciones con asignación nominativa.", "Las subvenciones de concesión directa por razones de interés público.", "Las subvenciones en régimen de concurrencia competitiva.", "Todas las subvenciones superiores a 5.000 euros."],
    "Art. 151 e) LGP.", "las subvenciones con asignación nominativa")
T.q("LGP", "a152", "Función interventora", "Según el artículo 152.2 de la Ley General Presupuestaria, aunque se haya acordado el régimen de fiscalización de requisitos básicos, será aplicable el régimen general de fiscalización previa respecto de los gastos que deban ser aprobados por:",
    ["El Consejo de Ministros.", "Los Secretarios de Estado.", "Los Subsecretarios.", "Los Directores Generales."],
    "Art. 152.2 LGP.", "será aplicable el régimen general de fiscalización previa respecto de gastos que deban ser aprobados por el Consejo de Ministros")
T.q("LGP", "a154", "Función interventora", "Según el artículo 154.1 de la Ley General Presupuestaria, la formulación del reparo:",
    ["Suspenderá la tramitación del expediente hasta que sea solventado.", "No tendrá efectos suspensivos en ningún caso.", "Solo suspenderá la tramitación si lo acuerda el órgano gestor.", "Determinará la nulidad automática del acto."],
    "Art. 154.1 LGP; las observaciones complementarias, en cambio, no suspenden (154.3).", "La formulación del reparo suspenderá la tramitación del expediente hasta que sea solventado")
T.q("LGP", "a154", "Función interventora", "Según el artículo 154.3 de la Ley General Presupuestaria, en el régimen especial de fiscalización de requisitos básicos, las observaciones complementarias que formulen los interventores:",
    ["No tendrán, en ningún caso, efectos suspensivos.", "Suspenderán la tramitación del expediente.", "Deberán ser resueltas por el Consejo de Ministros.", "Equivalen a un reparo."],
    "Art. 154.3 LGP.", "sin que las mismas tengan, en ningún caso, efectos suspensivos")
T.q("LGP", "a155", "Función interventora", "Según el artículo 155 de la Ley General Presupuestaria, cuando el reparo haya sido formulado por una intervención delegada y el órgano gestor no lo acepte, la discrepancia la conoce:",
    ["La Intervención General de la Administración del Estado, siendo su resolución obligatoria para aquélla.", "El Consejo de Ministros, directamente.", "El Ministro de Hacienda.", "El Tribunal de Cuentas."],
    "Art. 155 a) LGP.", "corresponderá a la Intervención General de la Administración del Estado conocer la discrepancia, siendo su resolución obligatoria para aquélla")
T.q("LGP", "a155", "Función interventora", "Según el artículo 155 b) de la Ley General Presupuestaria, cuando el reparo haya sido formulado por la IGAE y subsista la discrepancia, la resolución definitiva corresponde:",
    ["Al Consejo de Ministros.", "Al Ministro de Hacienda.", "Al Presidente del Gobierno.", "A la Comisión General de Subsecretarios."],
    "Art. 155 b) LGP.", "corresponderá al Consejo de Ministros adoptar resolución definitiva")
T.q("RD2188", "a13", "Función interventora", "Según el artículo 13.2 del Real Decreto 2188/1995, la Intervención fiscalizará el expediente en el plazo máximo de:",
    ["10 días, reducido a cinco si la tramitación es urgente o se aplica el régimen de requisitos básicos.", "15 días, reducido a diez si la tramitación es urgente.", "Un mes, reducido a quince días si la tramitación es urgente.", "5 días en todo caso."],
    "Art. 13.2 RD 2188/1995.", "La Intervención fiscalizará el expediente en el plazo máximo de 10 días")
T.q("LGP", "a156", "Función interventora", "Según el artículo 156.2 de la Ley General Presupuestaria, el informe que emite el órgano de control cuando se ha omitido la función interventora preceptiva:",
    ["No tendrá naturaleza de fiscalización.", "Tendrá la naturaleza de un reparo suspensivo.", "Tendrá naturaleza de fiscalización favorable.", "Deberá remitirse al Tribunal de Cuentas para su resolución."],
    "Art. 156.2 LGP.", "Este informe, que no tendrá naturaleza de fiscalización")
T.q("LGP", "a156", "Función interventora", "Según el artículo 156.3 de la Ley General Presupuestaria, la competencia para acordar el sometimiento al Consejo de Ministros del asunto en que se omitió la fiscalización corresponde al titular del departamento:",
    ["Sin que dicha competencia pueda ser objeto de delegación.", "Que podrá delegarla en el Subsecretario.", "Previo informe preceptivo del Tribunal de Cuentas.", "Solo si el gasto supera 12 millones de euros."],
    "Art. 156.3 LGP.", "sin que dicha competencia pueda ser objeto de delegación")
T.q("LGP", "a157", "Control financiero permanente", "Según el artículo 157 de la Ley General Presupuestaria, el control financiero permanente tiene por objeto la verificación de la situación y el funcionamiento de las entidades del sector público estatal en el aspecto económico-financiero:",
    ["De una forma continua, a través de la correspondiente intervención delegada.", "Antes de que se aprueben sus actos, a través del Interventor General.", "Con posterioridad, mediante auditorías del Tribunal de Cuentas.", "De forma esporádica, a petición del órgano gestor."],
    "Art. 157 LGP.", "de una forma continua realizada a través de la correspondiente intervención delegada")
T.q("LGP", "a158", "Control financiero permanente", "Según el artículo 158.1 de la Ley General Presupuestaria, ¿sobre cuál de las siguientes entidades se ejercerá el control financiero permanente?",
    ["Las entidades públicas empresariales.", "Las sociedades mercantiles estatales.", "Las fundaciones del sector público estatal.", "Los consorcios adscritos a una Comunidad Autónoma."],
    "Art. 158.1 c) LGP.", "Las entidades públicas empresariales")
T.q("LGP", "a161", "Control financiero permanente", "Según el artículo 161.2 de la Ley General Presupuestaria, el Plan de Acción del departamento ministerial se remitirá a la IGAE en el plazo de:",
    ["3 meses desde que el titular del departamento reciba los informes de control financiero permanente.", "Un mes desde la recepción de los informes.", "6 meses desde el cierre del ejercicio.", "15 días desde la recepción de los informes."],
    "Art. 161.2 LGP.", "en el plazo de 3 meses desde que el titular del departamento ministerial reciba la remisión de los informes")
T.q("RD2188", "a35", "Control financiero permanente", "Según el artículo 35.1 del Real Decreto 2188/1995, el control financiero se ejercerá:",
    ["Mediante auditorías u otras técnicas de control.", "Únicamente mediante auditorías externas.", "Únicamente mediante la fiscalización previa de los expedientes.", "Mediante auditorías encargadas por el Tribunal de Cuentas."],
    "Art. 35.1 RD 2188/1995.", "El control financiero se ejercerá mediante auditorías u otras técnicas de control")
T.q("LGP", "a162", "Auditoría pública", "Según el artículo 162 de la Ley General Presupuestaria, la auditoría pública consistirá en la verificación de la actividad económico-financiera del sector público estatal:",
    ["Realizada con posterioridad y efectuada de forma sistemática.", "Realizada con carácter previo a la aprobación de cada acto.", "Realizada de forma continua por la intervención delegada.", "Realizada por auditores privados designados por el órgano gestor."],
    "Art. 162 LGP.", "realizada con posterioridad y efectuada de forma sistemática")
T.q("LGP", "a164", "Auditoría pública", "Según el artículo 164.1 de la Ley General Presupuestaria, la auditoría cuyo objeto consiste en la verificación de que los actos, operaciones y procedimientos de gestión económico-financiera se han desarrollado de conformidad con las normas que les son de aplicación es:",
    ["La auditoría de cumplimiento.", "La auditoría de regularidad contable.", "La auditoría operativa.", "La auditoría de cuentas anuales."],
    "Art. 164.1 b) LGP.", "La auditoría de cumplimiento, cuyo objeto consiste en la verificación de que los actos, operaciones y procedimientos")
T.q("LGP", "a165", "Auditoría pública", "Según el artículo 165 de la Ley General Presupuestaria, el plan anual de auditorías lo elabora:",
    ["La Intervención General de la Administración del Estado.", "El Tribunal de Cuentas.", "El Consejo de Ministros.", "La Comisión Mixta Congreso-Senado para las Relaciones con el Tribunal de Cuentas."],
    "Art. 165 LGP.", "La Intervención General de la Administración del Estado elaborará anualmente un plan de auditorías")
T.q("LGP", "a166", "Auditoría pública", "Según el artículo 166.4 de la Ley General Presupuestaria, los informes de auditoría de cuentas anuales se rendirán en todo caso:",
    ["Al Tribunal de Cuentas junto con las cuentas anuales.", "Al Consejo de Ministros junto con el informe general.", "A las Cortes Generales.", "A la Autoridad Independiente de Responsabilidad Fiscal."],
    "Art. 166.4 LGP.", "se rendirán en todo caso al Tribunal de Cuentas junto con las cuentas anuales")
T.q("LGP", "a170", "Auditoría pública", "Según el artículo 170 de la Ley General Presupuestaria, ¿cuál de las siguientes NO es una modalidad de la auditoría operativa?",
    ["Auditoría de regularidad contable.", "Auditoría de programas presupuestarios.", "Auditoría de sistemas y procedimientos.", "Auditoría de economía, eficacia y eficiencia."],
    "Art. 170 LGP; la de regularidad contable es otra modalidad de auditoría pública (164.1 a).", "Auditoría de programas presupuestarios")
T.q("CE", "Artículo 136", "Tribunal de Cuentas", "Según el artículo 136.1 de la Constitución, el Tribunal de Cuentas:",
    ["Dependerá directamente de las Cortes Generales.", "Dependerá directamente del Gobierno.", "Dependerá del Consejo General del Poder Judicial.", "Dependerá del Ministerio de Hacienda."],
    "Art. 136.1 CE.", "Dependerá directamente de las Cortes Generales")
T.q("CE", "Artículo 136", "Tribunal de Cuentas", "Según el artículo 136.4 de la Constitución, la composición, organización y funciones del Tribunal de Cuentas se regularán por:",
    ["Una ley orgánica.", "Una ley ordinaria.", "El Reglamento del Congreso.", "Un real decreto del Gobierno."],
    "Art. 136.4 CE.", "Una ley orgánica regulará la composición, organización y funciones del Tribunal de Cuentas")
T.q("CE", "Artículo 153", "Tribunal de Cuentas", "Según el artículo 153 de la Constitución, el control económico y presupuestario de la actividad de los órganos de las Comunidades Autónomas se ejercerá por:",
    ["El Tribunal de Cuentas.", "El Gobierno, previo dictamen del Consejo de Estado.", "La jurisdicción contencioso-administrativa.", "El Tribunal Constitucional."],
    "Art. 153 d) CE.", "Por el Tribunal de Cuentas, el económico y presupuestario")
T.q("LOTCu", "asegundo", "Tribunal de Cuentas", "Según el artículo segundo de la Ley Orgánica 2/1982, del Tribunal de Cuentas, son funciones propias del Tribunal:",
    ["La fiscalización externa, permanente y consuntiva de la actividad económico-financiera del sector público y el enjuiciamiento de la responsabilidad contable.", "El control interno de la gestión económica del sector público y la formación de la Cuenta General del Estado.", "La función interventora y el control financiero permanente.", "La elaboración de los Presupuestos Generales del Estado y su control."],
    "Art. 2 LO 2/1982.", "La fiscalización externa, permanente y consuntiva de la actividad económico-financiera del sector público")
T.q("LOTCu", "aoctavo", "Tribunal de Cuentas", "Según el artículo octavo de la Ley Orgánica 2/1982, los conflictos que se susciten sobre las competencias o atribuciones del Tribunal de Cuentas serán resueltos por:",
    ["El Tribunal Constitucional.", "El Tribunal Supremo.", "Las Cortes Generales.", "El Pleno del propio Tribunal de Cuentas."],
    "Art. 8.1 LO 2/1982.", "serán resueltos por el Tribunal Constitucional")
T.q("LOTCu", "aveintiuno", "Tribunal de Cuentas", "Según el artículo veintiuno de la Ley Orgánica 2/1982, el Tribunal de Cuentas en Pleno estará integrado por:",
    ["Doce Consejeros de Cuentas, uno de los cuales será el Presidente, y el Fiscal.", "Nueve Consejeros de Cuentas y el Presidente.", "Doce Consejeros de Cuentas y el Secretario General.", "Seis Consejeros designados por el Congreso y el Presidente."],
    "Art. 21.1 LO 2/1982.", "doce Consejeros de Cuentas, uno de los cuales será el Presidente, y el Fiscal")
T.q("LOTCu", "aveintinueve", "Tribunal de Cuentas", "Según el artículo veintinueve de la Ley Orgánica 2/1982, el Presidente del Tribunal de Cuentas será nombrado de entre sus miembros:",
    ["Por el Rey, a propuesta del mismo Tribunal en Pleno y por un período de tres años.", "Por el Rey, a propuesta del Congreso, por un período de nueve años.", "Por las Cortes Generales, por mayoría de tres quintos, por un período de cinco años.", "Por el Gobierno, a propuesta del Ministro de Hacienda, por un período de tres años."],
    "Art. 29 LO 2/1982.", "por el Rey, a propuesta del mismo Tribunal en Pleno y por un período de tres años")
T.q("LOTCu", "atreinta", "Tribunal de Cuentas", "Según el artículo treinta de la Ley Orgánica 2/1982, los Consejeros de Cuentas serán designados por las Cortes Generales mediante votación por mayoría de tres quintos de cada una de las Cámaras por un período de:",
    ["Nueve años.", "Seis años.", "Tres años.", "Cinco años."],
    "Art. 30.1 LO 2/1982.", "por un período de nueve años")
T.q("LOTCu", "adiecisiete", "Tribunal de Cuentas", "Según el artículo diecisiete de la Ley Orgánica 2/1982, la jurisdicción contable es:",
    ["Necesaria e improrrogable, exclusiva y plena.", "Voluntaria y prorrogable.", "Compartida con la jurisdicción contencioso-administrativa.", "Supletoria de la jurisdicción penal."],
    "Art. 17.1 LO 2/1982.", "La jurisdicción contable es necesaria e improrrogable, exclusiva y plena")
T.q("LOTCu", "atreintayocho", "Tribunal de Cuentas", "Según el artículo treinta y ocho de la Ley Orgánica 2/1982, la responsabilidad contable directa:",
    ["Será siempre solidaria y comprenderá todos los perjuicios causados.", "Podrá moderarse en forma prudencial y equitativa.", "Solo procede cuando no puedan hacerse efectivas las subsidiarias.", "No se transmite a los causahabientes."],
    "Art. 38.3 LO 2/1982; la moderación es de la subsidiaria (38.4).", "La responsabilidad directa será siempre solidaria y comprenderá todos los perjuicios causados")
T.q("LFTCu", "a72", "Tribunal de Cuentas", "Según el artículo 72.1 de la Ley 7/1988, de Funcionamiento del Tribunal de Cuentas, se entenderá por alcance:",
    ["El saldo deudor injustificado de una cuenta o, en términos generales, la ausencia de numerario o de justificación en las cuentas.", "La sustracción de caudales públicos por quien los tenga a su cargo.", "El retraso en la rendición de cuentas al Tribunal.", "El exceso de gasto sobre el crédito presupuestario autorizado."],
    "Art. 72.1 Ley 7/1988; la sustracción es la malversación (72.2).", "se entenderá por alcance el saldo deudor injustificado de una cuenta")
T.real("L", 88, "Función interventora"); T.real("P", 91, "Función interventora"); T.real("X", 94, "Control financiero permanente")
T.real("P", 90, "Tribunal de Cuentas"); T.real("X", 93, "Tribunal de Cuentas"); T.real("L", 89, "Tribunal de Cuentas")

# Flashcards
for q_, a_, cat in [
  ("¿Quién hace el control externo y quién el interno del sector público estatal? (LGP, art. 140)", "Externo: Tribunal de Cuentas. Interno: IGAE, con plena autonomía.", "Control externo e interno"),
  ("Tres formas del control interno (LGP, art. 142.2)", "Función interventora, control financiero permanente y auditoría pública.", "Control externo e interno"),
  ("Adscripción y rango de la IGAE (RD 206/2024, art. 8.6)", "Secretaría de Estado de Presupuestos y Gastos; rango de Subsecretaría.", "La IGAE"),
  ("Principios de actuación de la IGAE (LGP, art. 144.1)", "Autonomía, ejercicio desconcentrado y jerarquía interna.", "La IGAE"),
  ("¿Cuánto tiempo custodia la IGAE los papeles de auditoría y control financiero? (art. 145.5)", "Cinco años desde la emisión del informe.", "La IGAE"),
  ("Definición de función interventora (LGP, art. 148)", "Control, antes de que sean aprobados, de los actos que dan lugar a reconocimiento de derechos o realización de gastos, y de los ingresos y pagos derivados.", "Función interventora"),
  ("Fases de la función interventora (LGP, art. 150.2)", "Fiscalización previa; intervención del reconocimiento de obligaciones y de la comprobación de la inversión; intervención formal de la ordenación del pago; intervención material del pago.", "Función interventora"),
  ("¿Puede avocar el Interventor General? (art. 150 bis)", "Sí: cualquier acto o expediente que considere oportuno.", "Función interventora"),
  ("Gastos no sujetos a fiscalización previa (art. 151)", "Contratos menores; gastos periódicos tras el período inicial; caja fija < 5.000 €; procesos electorales; subvenciones nominativas; bases de datos y publicaciones no SARA; emergencia; a justificar < 5.000 € en el extranjero.", "Función interventora"),
  ("Plazo de fiscalización (RD 2188/1995, art. 13.2)", "10 días; 5 si es urgente o rige el régimen de requisitos básicos.", "Función interventora"),
  ("¿Quién resuelve la discrepancia con un reparo de la IGAE? (art. 155 b)", "El Consejo de Ministros, con carácter definitivo.", "Función interventora"),
  ("Omisión de fiscalización (art. 156)", "Informe (no es fiscalización); el titular del departamento, de forma indelegable, puede llevarlo al Consejo de Ministros; su acuerdo no exime de responsabilidades.", "Función interventora"),
  ("Control financiero permanente (art. 157)", "Verificación continua, a través de la intervención delegada, de la situación y funcionamiento económico-financiero de las entidades.", "Control financiero permanente"),
  ("Plan de Acción (art. 161)", "Lo elabora cada ministerio y lo remite a la IGAE en 3 meses; si la IGAE lo objeta, un mes para modificarlo.", "Control financiero permanente"),
  ("Auditoría pública (art. 162) y modalidades (art. 164)", "Verificación posterior y sistemática; regularidad contable, cumplimiento y operativa.", "Auditoría pública"),
  ("Dependencia del Tribunal de Cuentas (CE 136.1)", "Depende directamente de las Cortes Generales.", "Tribunal de Cuentas"),
  ("Cuenta General del Estado y Tribunal de Cuentas (LO 2/1982, art. 10)", "La examina por delegación de las Cortes Generales en seis meses desde su rendición; el Pleno, oído el Fiscal, dicta la declaración definitiva.", "Tribunal de Cuentas"),
  ("Composición del Pleno del Tribunal de Cuentas (art. 21)", "Doce Consejeros de Cuentas (uno, el Presidente) y el Fiscal; quórum de dos tercios; acuerdos por mayoría de asistentes.", "Tribunal de Cuentas"),
  ("Consejeros de Cuentas (art. 30)", "6 por el Congreso y 6 por el Senado, por tres quintos de cada Cámara, nueve años, más de quince años de ejercicio profesional.", "Tribunal de Cuentas"),
  ("Responsabilidad contable directa y subsidiaria (art. 38)", "Directa: siempre solidaria y por todos los perjuicios. Subsidiaria: limitada a sus actos y moderable. Ambas se transmiten a los causahabientes hasta el líquido de la herencia.", "Tribunal de Cuentas"),
  ("Informe preceptivo del Tribunal de Cuentas (Ley 7/1988, DA 11.ª)", "Plazo improrrogable de 30 días; 15 si se indica urgencia.", "Tribunal de Cuentas"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Control externo", "Control de la gestión económico-financiera del sector público estatal que corresponde al Tribunal de Cuentas (LGP, art. 140.1; CE, art. 136).", "s1", "Control externo e interno")
T.glos("Control interno", "Control de la gestión económica y financiera del sector público estatal que ejerce la IGAE con plena autonomía, mediante función interventora, control financiero permanente y auditoría pública (LGP, arts. 140.2 y 142.2).", "s2", "Control externo e interno")
T.glos("Intervenciones Delegadas", "Órganos de la IGAE en ministerios, organismos, entidades y territorios a través de los que ejerce el control (LGP, art. 143; RD 206/2024, art. 11.2).", "s3", "La IGAE")
T.glos("Función interventora", "Control, antes de que sean aprobados, de los actos que dan lugar al reconocimiento de derechos o a la realización de gastos y de los ingresos y pagos derivados (LGP, art. 148).", "s6", "Función interventora")
T.glos("Intervención formal y material", "Formal: verificación de los requisitos legales mediante el examen de los documentos del expediente. Material: comprobación de la real y efectiva aplicación de los fondos públicos (LGP, art. 150.1).", "s6", "Función interventora")
T.glos("Fiscalización de requisitos básicos", "Régimen especial, acordado por el Consejo de Ministros, en que la fiscalización previa se limita a los extremos del art. 152.1 LGP.", "s8", "Función interventora")
T.glos("Reparo", "Desacuerdo por escrito de la Intervención con el contenido o el procedimiento del acto, que suspende la tramitación hasta que se solvente (LGP, art. 154).", "s9", "Función interventora")
T.glos("Discrepancia", "Escrito motivado del órgano gestor que no acepta el reparo; la resuelve la IGAE o, en su caso, el Consejo de Ministros (LGP, art. 155).", "s9", "Función interventora")
T.glos("Omisión de fiscalización", "Falta de la función interventora preceptiva; impide reconocer la obligación y pagar hasta que se subsane con el procedimiento del art. 156 LGP.", "s10", "Función interventora")
T.glos("Control financiero permanente", "Verificación continua, a través de la intervención delegada, de la situación y funcionamiento económico-financiero de las entidades del sector público estatal (LGP, art. 157).", "s11", "Control financiero permanente")
T.glos("Plan de Acción", "Documento de cada departamento ministerial con las medidas para corregir las deficiencias de los informes de control (LGP, arts. 161 y 166.3).", "s12", "Control financiero permanente")
T.glos("Auditoría pública", "Verificación posterior y sistemática de la actividad económico-financiera del sector público estatal con procedimientos de revisión selectivos (LGP, art. 162).", "s13", "Auditoría pública")
T.glos("Cuenta General del Estado", "Cuenta que forma la IGAE y que el Tribunal de Cuentas examina por delegación de las Cortes en seis meses (LO 2/1982, art. 10; Ley 7/1988, art. 33).", "s17", "Tribunal de Cuentas")
T.glos("Responsabilidad contable", "Obligación de indemnizar el menoscabo de caudales o efectos públicos causado por acción u omisión contraria a la ley; directa o subsidiaria (LO 2/1982, art. 38).", "s19", "Tribunal de Cuentas")
T.glos("Alcance", "Saldo deudor injustificado de una cuenta o ausencia de numerario o de justificación en las cuentas de quien maneja caudales o efectos públicos (Ley 7/1988, art. 72.1).", "s19", "Tribunal de Cuentas")

# Cronología (fechas de los metadatos del BOE)
T.hito("1978", "Constitución Española (27-12-1978; BOE de 29-12-1978)", "Art. 136: el Tribunal de Cuentas, supremo órgano fiscalizador", "normativo", "s16")
T.hito("1982", "Ley Orgánica 2/1982, de 12 de mayo, del Tribunal de Cuentas (BOE de 21-5-1982)", "Funciones, composición y responsabilidad contable", "normativo", "s16")
T.hito("1988", "Ley 7/1988, de 5 de abril, de Funcionamiento del Tribunal de Cuentas (BOE de 7-4-1988)", "Procedimientos fiscalizadores y jurisdiccionales", "normativo", "s17")
T.hito("1996", "Real Decreto 2188/1995, de 28 de diciembre, de control interno de la IGAE (BOE de 25-1-1996)", "Reglamento de la función interventora y del control financiero", "normativo", "s7")
T.hito("2003", "Ley 47/2003, de 26 de noviembre, General Presupuestaria (BOE de 27-11-2003; vigente desde 1-1-2005)", "Título VI: control interno de la IGAE", "normativo", "s1")
T.hito("2014", "Ley 15/2014, de 16 de septiembre, de racionalización del Sector Público (BOE de 17-9-2014)", "Art. 22: informe preceptivo del Tribunal de Cuentas (DA 11.ª Ley 7/1988)", "normativo", "s17")
T.hito("2024", "Real Decreto 206/2024, de 27 de febrero, estructura del Ministerio de Hacienda (BOE de 28-2-2024)", "Art. 11: funciones y órganos de la IGAE", "normativo", "s3")

T.publicar()
