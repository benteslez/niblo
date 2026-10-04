# -*- coding: utf-8 -*-
"""Tema IV.9 (B4T09): El régimen patrimonial de las Administraciones públicas. El dominio
público. Los bienes patrimoniales del Estado. El Patrimonio Nacional. Los bienes comunales.
Método del I.2: mapa → bloques (I a V) con guía; cada artículo, texto literal del BOE +
ficha de casillas fijas; cierre 1 (preguntas oficiales) y cierre 2 (repaso).
Normas (textos consolidados del BOE): CE, art. 132; Ley 33/2003, del Patrimonio de las
Administraciones Públicas (LPAP); Ley 23/1982, reguladora del Patrimonio Nacional; Ley 7/1985,
Reguladora de las Bases del Régimen Local (arts. 79 a 82); Real Decreto 1372/1986, Reglamento
de Bienes de las Entidades Locales."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO["L23_1982"] = "Ley 23/1982, del Patrimonio Nacional"
CORTO["LRBRL"] = "Ley 7/1985, LRBRL"
CORTO["RD1372"] = "Reglamento de Bienes de las Entidades Locales"

BOE_Q = 'se publicará gratuitamente en el "Boletín Oficial del Estado"'

T = Tema("B4T09",
  "Cinco preguntas: I. Qué es el patrimonio de las Administraciones públicas, quién lo gestiona y cómo se defiende (art. 132 CE; Ley 33/2003, arts. 1 a 59) · II. Qué es el dominio público y cómo se usa (Ley 33/2003, arts. 5, 6, 30, 65 a 100) · III. Qué son los bienes patrimoniales del Estado y cómo se enajenan (arts. 7, 8, 30, 31, 131 a 153) · IV. Qué es el Patrimonio Nacional (Ley 23/1982) · V. Qué son los bienes comunales (Ley 7/1985, arts. 79 a 82; Reglamento de Bienes de las Entidades Locales). Cada artículo: texto literal del BOE y ficha.",
  ["Art. 132 CE", "Ley 33/2003", "Dominio público", "Inalienabilidad", "Afectación", "Desafectación", "Mutación demanial", "Uso común", "Uso privativo", "Autorización", "Concesión demanial", "Bienes patrimoniales", "Deslinde", "Recuperación de oficio", "Desahucio administrativo", "Patrimonio Nacional", "Ley 23/1982", "Bienes comunales", "RD 1372/1986"])

# =============================================================================
T.ap("s0", "Mapa del tema: cinco preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque IV, tema 9):
> El régimen patrimonial de las Administraciones públicas. El dominio público. Los bienes patrimoniales del Estado. El Patrimonio Nacional. Los bienes comunales.

### El hilo conductor

El epígrafe se lee como **cinco preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Constitución | Otras normas |
|---|---|---|---|
| **I** | ¿Qué es el patrimonio de las Administraciones públicas, quién lo gestiona y cómo se defiende? | Art. 132 | Ley 33/2003, arts. 1 a 4, 9, 10, 28, 32, 36, 41, 43, 45, 47 y 50 a 59 |
| **II** | ¿Qué es el dominio público y cómo se usa? | Art. 132.1 y 2 | Ley 33/2003, arts. 5, 6, 30.1, 65, 66, 69, 71, 84 a 86, 92, 93 y 100 |
| **III** | ¿Qué son los bienes patrimoniales del Estado y cómo se enajenan? | — | Ley 33/2003, arts. 7, 8, 30.2 y 3, 31, 131, 137, 145 y 153 |
| **IV** | ¿Qué es el Patrimonio Nacional? | Art. 132.3 | Ley 23/1982, arts. 1, 2, 4, 5, 6 y 8; Ley 33/2003, disposición adicional cuarta |
| **V** | ¿Qué son los bienes comunales? | Art. 132.1 | Ley 7/1985, arts. 79 a 82; Real Decreto 1372/1986, arts. 2, 8, 94, 98, 100, 102 y 103 |

!> **La idea que une los cinco bloques:** la Constitución manda que una **ley** regule los bienes públicos (art. 132). La Ley 33/2003 divide el patrimonio de las Administraciones en **dos clases**: bienes de **dominio público** (afectados a un uso general o a un servicio público: **inalienables, imprescriptibles e inembargables**) y bienes **patrimoniales** (los demás: pueden enajenarse). Al lado hay dos regímenes especiales: el **Patrimonio Nacional** (bienes del Estado afectados al uso y servicio del **Rey** y de la Real Familia, Ley 23/1982) y los **bienes comunales** (de dominio público local, cuyo aprovechamiento corresponde al **común de los vecinos**).

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
- Gran parte de la Ley 33/2003 solo rige para la **Administración General del Estado** y sus organismos; lo que se aplica también a comunidades autónomas y entidades locales lo dice su disposición final segunda (→ I.2.2).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué es el patrimonio de las Administraciones públicas, quién lo gestiona y cómo se defiende? (art. 132 CE; Ley 33/2003)", donde(
  "Primera pregunta del tema. Antes de distinguir dominio público y bienes patrimoniales, hay que saber **qué manda la Constitución**, **qué es** el patrimonio de una Administración, **quién** lo gestiona en el Estado y con qué **potestades** se defiende.",
  ["1 El mandato constitucional (art. 132)", "2 Objeto, ámbito, concepto y clases (Ley 33/2003, arts. 1 a 4)", "3 El Patrimonio del Estado y sus órganos (arts. 9 y 10)", "4 Protección: inventario y Registro de la Propiedad (arts. 28, 32 y 36)", "5 Las prerrogativas: investigación, deslinde, recuperación y desahucio (arts. 41 a 59)", "6 Cuadro de las prerrogativas"]))

T.ap("s1", "I.1 El mandato constitucional (art. 132)", f"""
La Constitución no regula los bienes públicos: **remite a la ley** y le marca los principios.

{unidad("1.1 Dominio público, comunales, Patrimonio del Estado y Patrimonio Nacional (art. 132)",
  lit("CE", "Artículo 132", ["La ley regulará el régimen jurídico de los bienes de dominio público y de los comunales", "inalienabilidad, imprescriptibilidad e inembargabilidad", "la zona marítimo-terrestre, las playas, el mar territorial y los recursos naturales de la zona económica y la plataforma continental", "Por ley se regularán el Patrimonio del Estado y el Patrimonio Nacional"]),
  fichab("Reserva de ley del régimen de los bienes públicos y lista mínima del dominio público estatal",
         "El legislador (Cortes Generales): «La ley regulará…» (132.1), «los que determine la ley» (132.2), «Por ley se regularán…» (132.3)",
         ["Dominio público y comunales: régimen inspirado en la **inalienabilidad, imprescriptibilidad e inembargabilidad**, y su **desafectación** (132.1)", "Dominio público estatal **en todo caso**: zona marítimo-terrestre, playas, mar territorial y recursos naturales de la zona económica y la plataforma continental (132.2)", "Patrimonio del Estado y Patrimonio Nacional: su administración, defensa y conservación, **por ley** (132.3)"],
         "—",
         "Por **ley** (no ley orgánica, ni decreto, ni acuerdo del Consejo de Ministros): cayó en 2025 (→ Cierre 1). La lista del 132.2 es un **mínimo** («en todo caso»): la ley puede añadir más bienes de dominio público estatal."))}
""", 2)

T.ap("s2", "I.2 Objeto, ámbito, concepto y clases (Ley 33/2003, arts. 1 a 4)", f"""
{unidad("2.1 Objeto de la ley (art. 1)",
  lit("LPAP", "a1", ["las bases del régimen patrimonial de las Administraciones públicas", "la administración, defensa y conservación del Patrimonio del Estado"]),
  fichab("Doble objeto de la Ley 33/2003",
         "Las Cortes, en desarrollo del art. 132 CE",
         ["Establecer las **bases** del régimen patrimonial de **todas** las Administraciones públicas", "Regular la administración, defensa y conservación del **Patrimonio del Estado**"],
         "—",
         "La ley cumple el mandato del **132.3** CE para el Patrimonio del Estado; el **Patrimonio Nacional** tiene su propia ley (→ IV.2)."))}

{unidad("2.2 Ámbito de aplicación (art. 2)",
  lit("LPAP", "a2", ["Administración General del Estado y de los organismos públicos vinculados a ella", "los artículos o partes de los mismos enumerados en la disposición final segunda"]),
  fichab("A quién se aplica",
         ["Íntegra: Administración General del Estado y sus organismos públicos (2.1)", "Comunidades autónomas, entidades locales y sus entidades de derecho público: solo los preceptos de la **disposición final segunda** (2.2)"],
         "—", "—",
         f"Para comunidades autónomas y entes locales rige solo lo enumerado en la disposición final segunda; su apartado 5 dice qué preceptos {c('LPAP', 'dfsegunda', 'Tienen el carácter de la legislación básica')} (entre ellos, los arts. 6, 41, 50, 55, 58 y 84)."))}

{unidad("2.3 Concepto de patrimonio (art. 3)",
  lit("LPAP", "a3", ["el conjunto de sus bienes y derechos, cualquiera que sea su naturaleza y el título de su adquisición", "el dinero, los valores, los créditos y los demás recursos financieros de su hacienda"]),
  fichab("Qué forma el patrimonio de una Administración",
         "Cada Administración pública",
         ["**Incluye**: el conjunto de sus bienes y derechos, sea cual sea su naturaleza y título de adquisición", "**Excluye**: dinero, valores, créditos y demás recursos financieros de su hacienda (y la tesorería de las entidades públicas empresariales autonómicas y locales)"],
         "—",
         "El **dinero** y los **créditos** de la hacienda **no** forman parte del patrimonio a efectos de esta ley."))}

{unidad("2.4 Dos clases de bienes (art. 4)",
  lit("LPAP", "a4", ["de dominio público o demaniales y de dominio privado o patrimoniales"]),
  fichab("Clasificación por razón del régimen jurídico",
         "—",
         ["Bienes y derechos de **dominio público** o **demaniales** (→ II.1)", "Bienes y derechos de **dominio privado** o **patrimoniales** (→ III.1)"],
         "—",
         "«Demanial» = dominio público; «patrimonial» = dominio privado. El criterio es el **régimen jurídico** al que están sujetos."))}
""", 2)

T.ap("s3", "I.3 El Patrimonio del Estado y sus órganos (arts. 9 y 10)", f"""
{unidad("3.1 Concepto y gestión del Patrimonio del Estado (art. 9)",
  lit("LPAP", "a9", ["el patrimonio de la Administración General del Estado y los patrimonios de los organismos públicos", "corresponderán al Ministerio de Hacienda, a través de la Dirección General del Patrimonio del Estado"]),
  fichab("Qué es el Patrimonio del Estado y quién lo gestiona",
         ["Bienes de titularidad de la **Administración General del Estado**: el **Ministerio de Hacienda**, a través de la **Dirección General del Patrimonio del Estado** (9.2)", "Bienes de titularidad de los **organismos públicos**: los propios organismos (9.3)"],
         "Gestión, administración y explotación conforme a esta ley y, para los organismos, a sus normas de creación o estatutos",
         "—",
         "Cayó en 2025 (→ Cierre 1): Ministerio de **Hacienda** + Dirección General del **Patrimonio del Estado**. No confundir con el **Patrimonio Nacional** (→ IV.1)."))}

{unidad("3.2 Reparto de competencias (art. 10)",
  lit("LPAP", "a10", ["Corresponde al Consejo de Ministros, a propuesta del Ministro de Hacienda", "Definir la política aplicable a los bienes y derechos del Patrimonio del Estado", "Velar por el cumplimiento de la política patrimonial definida por el Gobierno", "Solicitar del Ministro de Hacienda la afectación"], solo=[1, 2, 3, 4, 5, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20, 21, 22, 23]),
  fichab("Quién hace qué en la política patrimonial del Estado",
         ["**Consejo de Ministros** (a propuesta del Ministro de Hacienda): define la política y los criterios de actuación coordinada (10.1)", "**Ministro de Hacienda**: propone reglamentos, vela por la política patrimonial, dicta instrucciones y directrices (10.3)", "**Departamentos ministeriales**: ejecutan la política y defienden los bienes que tienen afectados (10.4)", "**Dirección General del Patrimonio del Estado**: propone al Ministro y supervisa la ejecución (10.5)"],
         "—", "—",
         "**Define** la política el Consejo de Ministros; **vela** por su cumplimiento el Ministro de Hacienda; la **ejecutan** los departamentos. Los departamentos **solicitan** al Ministro de Hacienda la afectación y la desafectación."))}
""", 2)

T.ap("s4", "I.4 Protección: inventario y Registro de la Propiedad (arts. 28, 32 y 36)", f"""
{unidad("4.1 Deber de proteger y defender (art. 28)",
  lit("LPAP", "a28", ["están obligadas a proteger y defender su patrimonio", "procurarán su inscripción registral"]),
  fichab("Obligación general de defensa del patrimonio",
         "Todas las Administraciones públicas (precepto básico)",
         ["Proteger adecuadamente sus bienes y derechos", "Procurar su **inscripción registral**", "Ejercer las **potestades administrativas** y **acciones judiciales** procedentes (→ I.5)"],
         "—",
         "Es una **obligación** («están obligadas»), no una facultad."))}

{unidad("4.2 Inventario (art. 32)",
  lit("LPAP", "a32", ["están obligadas a inventariar los bienes y derechos que integran su patrimonio", "incluirá, al menos, los bienes inmuebles y los derechos reales sobre los mismos"], solo=[1, 5]),
  fichab("Obligación de formar inventario",
         "Todas las Administraciones públicas",
         ["Inventario de **todos** sus bienes y derechos, con las menciones para identificarlos y reflejar su situación jurídica y su destino o uso (32.1)", "Comunidades autónomas y entidades locales: **al menos** los inmuebles y los derechos reales sobre ellos (32.4)"],
         "—",
         "En el Estado, el instrumento es el **Inventario General de Bienes y Derechos del Estado** (32.2)."))}

{unidad("4.3 Inscripción en el Registro de la Propiedad (art. 36.1)",
  lit("LPAP", "a36", ["ya sean demaniales o patrimoniales", "la inscripción será potestativa para las Administraciones públicas en el caso de arrendamientos inscribibles"], solo=[1]),
  fichab("Obligación de inscribir",
         "Todas las Administraciones públicas; lo solicita el órgano que adquirió el bien o que lo administra (36.2)",
         "Se inscriben los bienes y derechos **demaniales y patrimoniales** susceptibles de inscripción, y los actos y contratos referidos a ellos",
         "—",
         "También se inscriben los **demaniales**. Excepción: inscripción **potestativa** de los **arrendamientos** inscribibles."))}
""", 2)

T.ap("s5", "I.5 Las prerrogativas: investigación, deslinde, recuperación y desahucio (arts. 41 a 59)", f"""
{unidad("5.1 Las cuatro prerrogativas y su control judicial (arts. 41 y 43)",
  lit("LPAP", "a41", ["Investigar la situación de los bienes y derechos", "Deslindar en vía administrativa los inmuebles de su titularidad", "Recuperar de oficio la posesión indebidamente perdida", "Desahuciar en vía administrativa a los poseedores de los inmuebles demaniales", "sólo podrán ejercer las potestades enumeradas en el apartado 1 de este artículo para la defensa de bienes que tengan el carácter de demaniales"]),
  lit("LPAP", "a43", ["no cabrá la acción para la tutela sumaria de la posesión", "sólo podrán ser recurridos ante la jurisdicción contencioso-administrativa por infracción de las normas sobre competencia y procedimiento"], solo=[1, 2]),
  fichab("Facultades y prerrogativas para defender el patrimonio",
         "Las Administraciones públicas (precepto básico); las **entidades públicas empresariales**, solo para bienes **demaniales** (41.3)",
         ["**Investigar** (→ I.5.2)", "**Deslindar** en vía administrativa los **inmuebles** (→ I.5.3)", "**Recuperar de oficio** la posesión (→ I.5.5)", "**Desahuciar** en vía administrativa a los poseedores de inmuebles **demaniales** (→ I.5.6)"],
         "—",
         ["Las cuestiones de naturaleza **civil** van al orden **civil** (41.2).", "Contra estas actuaciones **no cabe** la tutela sumaria de la posesión (antiguo interdicto) del art. 250.4.º LEC (43.1).", "Si afectan a derechos civiles, el contencioso solo por infracción de normas de **competencia y procedimiento** (43.2)."]))}

{unidad("5.2 Investigación (arts. 45 y 47)",
  lit("LPAP", "a45", ["a fin de determinar la titularidad de los mismos cuando ésta no les conste de modo cierto"]),
  lit("LPAP", "a47", ["por iniciativa propia o por denuncia de particulares", BOE_Q, "en el plazo de dos años"], solo=[2, 3, 7]),
  fichab("Averiguar si un bien es de la Administración cuando no le consta su titularidad",
         "Las Administraciones públicas; en el Estado, si hay denuncia, la **Dirección General del Patrimonio del Estado** decide sobre su admisibilidad",
         ["De oficio: por iniciativa propia o por **denuncia de particulares**", "El acuerdo de incoación se publica **gratuitamente** en el BOE"],
         "Si no se resuelve en **dos años** desde el día siguiente a la publicación, **archivo** de las actuaciones",
         "**Dos años** para la investigación; **18 meses** para el deslinde (→ I.5.4)."))}

{unidad("5.3 Deslinde: potestad y órganos (arts. 50 y 51)",
  lit("LPAP", "a50", ["cuando los límites entre ellos sean imprecisos o existan indicios de usurpación", "no podrá instarse procedimiento judicial con igual pretensión"]),
  lit("LPAP", "a51", ["se acordará por el Director General del Patrimonio del Estado", "corresponderá al Ministro de Hacienda la resolución del mismo", "La instrucción del procedimiento corresponderá a los Delegados de Economía y Hacienda", "por el titular del departamento ministerial que los tenga afectados"]),
  fichab("Fijar los límites de los inmuebles de la Administración frente a los de terceros",
         ["Bienes **patrimoniales** de la AGE: **incoa** el **Director General del Patrimonio del Estado**; **instruyen** los **Delegados de Economía y Hacienda**; **resuelve** el **Ministro de Hacienda** (51.1)", "Bienes **demaniales** de la AGE: incoa el titular del departamento que los tenga afectados (51.2)", "Organismos públicos: sus presidentes o directores (51.3)"],
         "Cuando los límites sean **imprecisos** o haya **indicios de usurpación** (50.1)",
         "—",
         "Cayó en 2025 (→ Cierre 1): incoa el **Director General**, instruyen los **Delegados**, resuelve el **Ministro**. Mientras dura el deslinde **no** puede instarse procedimiento judicial con igual pretensión."))}

{unidad("5.4 Deslinde: procedimiento (art. 52)",
  lit("LPAP", "a52", ["por iniciativa propia o a petición de los colindantes", "se comunicará al Registro de la Propiedad", BOE_Q + " y en el tablón de edictos del ayuntamiento", "previo informe de la Abogacía del Estado", "se procederá al amojonamiento", "El plazo máximo para resolver el procedimiento de deslinde será de 18 meses"], solo=[2, 3, 4, 6, 7, 8]),
  fichab("Cómo se tramita el deslinde",
         "La Administración titular; los **colindantes** pueden pedirlo (a su costa)",
         ["Inicio de oficio: por iniciativa propia o a petición de los colindantes", "Nota al margen en el **Registro de la Propiedad**", "Publicación gratuita en el **BOE** y en el **tablón de edictos del ayuntamiento**", "Resolución previo **informe de la Abogacía del Estado**", "Con el deslinde firme: **amojonamiento** e inscripción"],
         "Plazo máximo para resolver: **18 meses** desde el acuerdo de iniciación; si no, **caducidad** y archivo",
         "Si lo piden los colindantes, los gastos son **a su costa** (cobro por vía de apremio). La resolución firme es título para **inmatricular** (art. 53.2)."))}

{unidad("5.5 Recuperación posesoria (arts. 55 y 56)",
  lit("LPAP", "a55", ["podrá ejercitarse en cualquier tiempo", "antes de que transcurra el plazo de un año, contado desde el día siguiente al de la usurpación", "ante los órganos del orden jurisdiccional civil"]),
  lit("LPAP", "a56", ["un plazo no superior a ocho días", "multas coercitivas de hasta un cinco por 100 del valor de los bienes ocupados"], solo=[2, 3]),
  fichab("Recuperar por sí misma la posesión indebidamente perdida",
         "Las Administraciones públicas (precepto básico); en la AGE, el **Delegado de Economía y Hacienda** o el **Director General del Patrimonio del Estado** (art. 57)",
         ["Audiencia al interesado y comprobación de la usurpación", "Requerimiento al ocupante para que cese", "Si resiste: ejecución forzosa, auxilio de las Fuerzas y Cuerpos de Seguridad o multas coercitivas"],
         ["Bienes **demaniales**: **en cualquier tiempo**", "Bienes **patrimoniales**: iniciación notificada antes de **un año** desde el día siguiente a la usurpación; después, vía **civil**", "Requerimiento: plazo **no superior a ocho días**", "Multas coercitivas: hasta el **5 %** del valor, reiteradas cada **ocho días**"],
         "Demaniales: **en cualquier tiempo**; patrimoniales: **un año**. Los gastos son **de cuenta del usurpador**."))}

{unidad("5.6 Desahucio administrativo (arts. 58 y 59)",
  lit("LPAP", "a58", ["la posesión de sus bienes demaniales", "cuando decaigan o desaparezcan el título, las condiciones o las circunstancias que legitimaban su ocupación por terceros"]),
  lit("LPAP", "a59", ["la previa declaración de extinción o caducidad del título", "un plazo no superior a ocho días"], solo=[1, 3, 5]),
  fichab("Recuperar los bienes demaniales cuando se extingue el título del ocupante",
         "Las Administraciones públicas (precepto básico)",
         ["Previa **declaración de extinción o caducidad** del título, con audiencia al interesado", "Requerimiento para desocupar; si no lo atiende, ejecución forzosa"],
         "Desalojo: plazo **no superior a ocho días**",
         "Solo para bienes **demaniales** (no patrimoniales). Los gastos del desalojo son **a cargo del detentador**."))}
""", 2)

T.ap("s6", "I.6 Cuadro de las prerrogativas (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Prerrogativa | Para qué | Bienes | Plazo que se pregunta | Órgano en la AGE |
|---|---|---|---|---|
| Investigación (45 y 47) | Determinar la titularidad cuando no consta de modo cierto | Todos | **Dos años** desde la publicación en el BOE; si no, archivo | Dirección General del Patrimonio del Estado (admite la denuncia) |
| Deslinde (50 a 52) | Fijar límites imprecisos o con indicios de usurpación | **Inmuebles** | **18 meses** desde la iniciación; si no, caducidad | Patrimoniales: incoa el Director General, instruyen los Delegados de Economía y Hacienda, resuelve el Ministro de Hacienda |
| Recuperación de oficio (55 a 57) | Recuperar la posesión indebidamente perdida | Todos | Demaniales: **en cualquier tiempo**; patrimoniales: **un año** | Delegado de Economía y Hacienda o Director General |
| Desahucio (58 y 59) | Recuperar la posesión al extinguirse el título del ocupante | **Demaniales** | Desalojo en un plazo no superior a **ocho días** | — |

{resumen([
  "Art. 132 CE: **por ley**; dominio público y comunales con **inalienabilidad, imprescriptibilidad e inembargabilidad**; lista mínima del dominio público estatal.",
  "Patrimonio = conjunto de **bienes y derechos** (no el dinero ni los créditos de la hacienda); dos clases: **demaniales** y **patrimoniales** (arts. 3 y 4).",
  "Patrimonio del Estado de la AGE: **Ministerio de Hacienda**, a través de la **Dirección General del Patrimonio del Estado** (art. 9.2).",
  "Prerrogativas: **investigar, deslindar, recuperar de oficio y desahuciar** (art. 41); deslinde de patrimoniales: incoa el **Director General**, instruyen los **Delegados**, resuelve el **Ministro**."],
  "Siguiente: II. ¿Qué es el dominio público y cómo se usa?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Qué es el dominio público y cómo se usa? (Ley 33/2003)", donde(
  "Segunda pregunta. Ya sabemos que hay dos clases de bienes; ahora, la primera: el **dominio público**. Qué bienes lo forman, con qué principios se gestiona, cómo entra un bien en él y cómo sale, y cómo pueden usarlo los particulares.",
  ["1 Concepto, principios e indisponibilidad (arts. 5, 6 y 30.1)", "2 Afectación, desafectación y mutación demanial (arts. 65, 66, 69 y 71)", "3 Tipos de uso y título necesario (arts. 84 a 86)", "4 Autorizaciones y concesiones demaniales (arts. 92, 93 y 100)"]))

T.ap("s7", "II.1 Concepto, principios e indisponibilidad del dominio público (arts. 5, 6 y 30.1)", f"""
{unidad("1.1 Qué bienes son de dominio público (art. 5)",
  lit("LPAP", "a5", ["se encuentren afectados al uso general o al servicio público", "aquellos a los que una ley otorgue expresamente el carácter de demaniales", "los mencionados en el artículo 132.2 de la Constitución", "se considerarán, en todo caso, bienes de dominio público"]),
  fichab("Concepto de bien demanial",
         "Titularidad **pública**",
         ["Bienes afectados al **uso general** o al **servicio público** (5.1)", "Los que una **ley** declare expresamente demaniales (5.1)", "En todo caso, los del **art. 132.2 CE** (5.2)", "Los inmuebles de la AGE y sus organismos donde se alojen servicios, oficinas o dependencias de sus órganos o de los órganos constitucionales (5.3)"],
         "—",
         ["Régimen: primero sus **leyes especiales**; a falta de ellas, esta ley; como supletorio, el **Derecho administrativo** y, en su defecto, el **privado** (5.4).", "Los edificios administrativos del Estado son dominio público **en todo caso**."]))}

{unidad("1.2 Principios de gestión del dominio público (art. 6)",
  lit("LPAP", "a6", ["Inalienabilidad, inembargabilidad e imprescriptibilidad", "Dedicación preferente al uso común frente a su uso privativo", "Identificación y control a través de inventarios o registros adecuados"]),
  fichab("Principios del dominio público (precepto básico)",
         "Todas las Administraciones públicas",
         ["Inalienabilidad, inembargabilidad e imprescriptibilidad", "Adecuación y suficiencia para su uso o servicio", "Aplicación efectiva al uso general o servicio público", "Dedicación **preferente al uso común** frente al privativo", "Ejercicio diligente de las prerrogativas", "Identificación y control mediante inventarios o registros", "Cooperación y colaboración entre Administraciones"],
         "—",
         "**Siete** principios (letras a a g). No confundir con los del art. 8 (patrimoniales: eficiencia, rentabilidad, publicidad y concurrencia → III.1)."))}

{unidad("1.3 Inalienables, imprescriptibles e inembargables (art. 30.1)",
  lit("LPAP", "a30", ["inalienables, imprescriptibles e inembargables"], solo=[1]),
  fichab("Régimen de disponibilidad del dominio público",
         "—",
         ["**Inalienables**: no pueden venderse ni transmitirse mientras sean demaniales", "**Imprescriptibles**: no se adquieren por usucapión", "**Inembargables**"],
         "—",
         "Para enajenarlos hay que **desafectarlos** antes (→ II.2.2): entonces pasan a ser patrimoniales."))}
""", 2)

T.ap("s8", "II.2 Afectación, desafectación y mutación demanial (arts. 65, 66, 69 y 71)", f"""
{unidad("2.1 Afectación: cómo entra un bien en el dominio público (arts. 65 y 66)",
  lit("LPAP", "a65", ["su consiguiente integración en el dominio público"]),
  lit("LPAP", "a66", ["Salvo que la afectación derive de una norma con rango legal, ésta deberá hacerse en virtud de acto expreso", "La utilización pública, notoria y continuada", "La adquisición de bienes o derechos por usucapión", "La adquisición de bienes y derechos por expropiación forzosa", "La aprobación por el Consejo de Ministros de programas o planes de actuación general", "La adquisición de los bienes muebles necesarios"], solo=[1, 2, 3, 4, 5, 6, 7]),
  fichab("Vinculación de un bien a un uso general o a un servicio público",
         "El órgano competente (o una norma con rango de ley)",
         ["::Por **acto expreso** que indica el bien, el fin, su integración en el dominio público y el órgano competente (66.1). Producen los mismos efectos (66.2):", "Utilización **pública, notoria y continuada**", "Usucapión vinculada al uso general o servicio público", "**Expropiación forzosa**", "Aprobación por el Consejo de Ministros de programas, planes o proyectos", "Adquisición de **muebles** para los servicios o la decoración de dependencias oficiales"],
         "—",
         "Regla: afectación **expresa**; las cinco situaciones del 66.2 equivalen a ella. En la expropiación, el bien queda afectado al fin de la **declaración de utilidad pública o interés social**."))}

{unidad("2.2 Desafectación: cómo sale (art. 69)",
  lit("LPAP", "a69", ["adquiriendo la de patrimoniales", "la desafectación deberá realizarse siempre de forma expresa"]),
  fichab("Pérdida de la condición demanial",
         "El órgano competente",
         "Por dejar de destinarse al uso general o al servicio público; el bien pasa a ser **patrimonial**",
         "—",
         "La desafectación es **expresa** («siempre», salvo los supuestos de la ley). Es el paso previo para poder enajenar un bien demanial."))}

{unidad("2.3 Mutación demanial (art. 71)",
  lit("LPAP", "a71", ["con simultánea afectación a otro uso general, fin o servicio público", "deberán efectuarse de forma expresa, salvo lo previsto en el apartado siguiente para el caso de reestructuración de órganos", "no alterará la titularidad de los bienes ni su carácter demanial"], solo=[1, 2, 3, 4]),
  fichab("Cambio de destino de un bien demanial",
         "La Administración General del Estado y sus organismos; reglamentariamente, también a favor de otras Administraciones (71.4)",
         ["Desafectación + **simultánea afectación** a otro uso, fin o servicio público (71.1)", "Expresa, salvo **reestructuración de órganos**: los bienes siguen al órgano que asume las competencias sin declaración expresa (71.2 y 3)"],
         "—",
         "La mutación entre Administraciones **no altera la titularidad** ni el carácter **demanial** del bien."))}
""", 2)

T.ap("s9", "II.3 Tipos de uso y título necesario (arts. 84 a 86)", f"""
{unidad("3.1 Necesidad de título habilitante (art. 84)",
  lit("LPAP", "a84", ["Nadie puede, sin título que lo autorice otorgado por la autoridad competente, ocupar bienes de dominio público"], solo=[1, 3]),
  fichab("Regla general: sin título no se ocupa el dominio público",
         "La autoridad competente otorga el título; las autoridades responsables de su tutela vigilan y actúan contra quien ocupe sin título (84.2, → I.5.1)",
         "Concesiones y autorizaciones: primero su **legislación especial**; en su defecto o insuficiencia, esta ley (84.3)",
         "—",
         "Precepto **básico**: rige para todas las Administraciones."))}

{unidad("3.2 Uso común, aprovechamiento especial y uso privativo (art. 85)",
  lit("LPAP", "a85", ["el que corresponde por igual y de forma indistinta a todos los ciudadanos", "sin impedir el uso común", "la ocupación de una porción del dominio público, de modo que se limita o excluye la utilización del mismo por otros interesados"]),
  fichab("Tres tipos de uso del dominio público",
         "—",
         ["**Uso común**: por igual y de forma indistinta a todos; el uso de unos no impide el de los demás", "**Aprovechamiento especial**: sin impedir el uso común, hay peligrosidad, intensidad, preferencia por escasez, rentabilidad singular u otras semejantes", "**Uso privativo**: ocupación de una porción que limita o excluye a los demás"],
         "—",
         "Aprovechamiento especial = **no impide** el uso común; privativo = **limita o excluye** a otros."))}

{unidad("3.3 Qué título exige cada uso (art. 86)",
  lit("LPAP", "a86", ["podrá realizarse libremente", "estarán sujetos a autorización o, si la duración del aprovechamiento o uso excede de cuatro años, a concesión", "con obras o instalaciones fijas deberá estar amparado por la correspondiente concesión administrativa"]),
  fichab("Título habilitante según el uso",
         "—",
         ["Uso común: **libre**", "Aprovechamiento especial y uso privativo con instalaciones **desmontables** o muebles: **autorización**; si dura **más de cuatro años**, **concesión**", "Uso privativo con obras o instalaciones **fijas**: **concesión**"],
         "Frontera: **cuatro años**",
         "Instalaciones **fijas** → concesión siempre; **desmontables** → autorización (hasta cuatro años)."))}
""", 2)

T.ap("s10", "II.4 Autorizaciones y concesiones demaniales (arts. 92, 93 y 100)", f"""
{unidad("4.1 Autorizaciones (art. 92)",
  lit("LPAP", "a92", ["Las autorizaciones se otorgarán directamente a los peticionarios que reúnan las condiciones requeridas", "mediante sorteo", "Su plazo máximo de duración, incluidas las prórrogas, será de cuatro años", "sin generar derecho a indemnización"], solo=[1, 2, 3, 4]),
  fichab("Título para usos de menor intensidad o duración",
         "La Administración titular (a los peticionarios que reúnan las condiciones)",
         ["Otorgamiento **directo**; si su número es limitado, en **concurrencia**, y si no procede, por **sorteo** (92.1)", "No transmisibles si cuentan las circunstancias personales o su número es limitado, salvo que lo admitan sus condiciones (92.2)", "Revocables unilateralmente por interés público **sin indemnización** (92.4)"],
         "Por tiempo determinado: máximo **cuatro años**, incluidas las prórrogas (92.3)",
         "Autorización: **directa** por regla, **4 años**, revocable **sin indemnización**."))}

{unidad("4.2 Concesiones demaniales (art. 93)",
  lit("LPAP", "a93", ["se efectuará en régimen de concurrencia", "Este documento será título suficiente para inscribir la concesión en el Registro de la Propiedad", "no podrá exceder de 75 años"], solo=[1, 2, 3]),
  fichab("Título para el uso privativo más intenso o duradero",
         "La Administración titular",
         ["En **concurrencia** por regla; otorgamiento **directo** en los supuestos del art. 137.4, por circunstancias excepcionales justificadas o cuando lo prevean las leyes (93.1)", "Se formaliza en **documento administrativo**, título para inscribir en el Registro de la Propiedad (93.2)"],
         "Por tiempo determinado: máximo **75 años**, incluidas las prórrogas, salvo que las normas especiales fijen uno menor (93.3)",
         "Concesión: **concurrencia** por regla y **75 años**. Autorización: directa y **4 años**."))}

{unidad("4.3 Extinción (art. 100)",
  lit("LPAP", "a100", ["Caducidad por vencimiento del plazo", "Rescate de la concesión, previa indemnización, o revocación unilateral de la autorización", "Falta de pago del canon", "Desafectación del bien"]),
  fichab("Causas de extinción de autorizaciones y concesiones (precepto básico)",
         "El órgano que otorgó la concesión o autorización declara el incumplimiento (100 f)",
         ["Muerte, incapacidad o extinción de la personalidad jurídica", "Transmisión o modificación sin autorización previa", "**Caducidad** por vencimiento del plazo", "**Rescate** (previa indemnización) o revocación de la autorización", "Mutuo acuerdo", "Falta de pago del canon o incumplimiento grave", "Desaparición del bien o agotamiento del aprovechamiento", "**Desafectación** del bien", "Otras de las condiciones"],
         "—",
         "El **rescate** de la concesión es **previa indemnización**; la **revocación** de la autorización, por interés público, **sin** indemnización (92.4)."))}

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| | Autorización | Concesión |
|---|---|---|
| Cuándo (art. 86) | Aprovechamiento especial o uso privativo con instalaciones desmontables o muebles, hasta 4 años | Uso privativo con obras o instalaciones fijas; o los anteriores si exceden de 4 años |
| Otorgamiento | Directo (concurrencia si su número es limitado; si no procede, sorteo) | Concurrencia (directo en casos tasados) |
| Plazo máximo | 4 años con prórrogas | 75 años con prórrogas |
| Fin anticipado | Revocación por interés público sin indemnización | Rescate previa indemnización |

{resumen([
  "Dominio público: afectado al **uso general o servicio público**, o declarado por ley; edificios administrativos del Estado, **en todo caso** (art. 5).",
  "**Inalienable, imprescriptible e inembargable** (arts. 6 y 30.1); para venderlo hay que **desafectarlo** de forma **expresa** (art. 69).",
  "Uso **común** libre; aprovechamiento especial o privativo con instalaciones desmontables: **autorización** (máx. **4 años**); con obras fijas o más de 4 años: **concesión** (máx. **75 años**).",
  "Autorización: directa y revocable **sin indemnización**; concesión: en **concurrencia** y rescatable **previa indemnización**."],
  "Siguiente: III. ¿Qué son los bienes patrimoniales del Estado y cómo se enajenan?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Qué son los bienes patrimoniales del Estado y cómo se enajenan? (Ley 33/2003)", donde(
  "Tercera pregunta. La otra clase de bienes: los **patrimoniales** o de dominio privado. Son los que **no** son demaniales; se gestionan con criterios de **rentabilidad** y pueden **enajenarse**, cederse o permutarse.",
  ["1 Concepto, principios y régimen (arts. 7, 8, 30.2 y 3, y 31)", "2 Enajenación, cesión gratuita y permuta (arts. 131, 137, 145 y 153)"]))

T.ap("s11", "III.1 Concepto, principios y régimen de los bienes patrimoniales (arts. 7, 8, 30.2 y 3, y 31)", f"""
{unidad("1.1 Qué son (art. 7)",
  lit("LPAP", "a7", ["no tengan el carácter de demaniales", "los derechos de arrendamiento", "Supletoriamente, se aplicarán las normas del derecho administrativo", "las normas del Derecho privado en lo que afecte a los restantes aspectos"]),
  fichab("Concepto de bien patrimonial (concepto residual)",
         "Titularidad de las Administraciones públicas",
         ["Los que **no** tengan carácter demanial (7.1)", "En todo caso, en la AGE: derechos de **arrendamiento**, **acciones y participaciones** en sociedades mercantiles, obligaciones, futuros y opciones sobre acciones, **propiedad incorporal** y derechos derivados de los bienes patrimoniales (7.2)"],
         "—",
         "Supletorio: Derecho **administrativo** para **competencia y procedimiento**; Derecho **privado** para lo demás (7.3)."))}

{unidad("1.2 Principios de gestión (art. 8)",
  lit("LPAP", "a8", ["Eficiencia y economía en su gestión", "Eficacia y rentabilidad en la explotación", "Publicidad, transparencia, concurrencia y objetividad", "en particular, al de la política de vivienda"]),
  fichab("Principios de los bienes patrimoniales",
         "Todas las Administraciones públicas (el apartado 1 es básico)",
         ["Eficiencia y economía", "Eficacia y **rentabilidad**", "Publicidad, transparencia, concurrencia y objetividad", "Identificación y control por inventarios o registros", "Colaboración y coordinación entre Administraciones", "Coadyuvar a las políticas públicas, en particular la de **vivienda** (8.2)"],
         "—",
         "La **rentabilidad** es principio de los patrimoniales; la **dedicación preferente al uso común**, de los demaniales (→ II.1.2)."))}

{unidad("1.3 Enajenables, prescriptibles y, con límites, embargables (art. 30.2 y 3)",
  lit("LPAP", "a30", ["podrán ser enajenados", "podrán ser objeto de prescripción adquisitiva por terceros", "cuando se encuentren materialmente afectados a un servicio público o a una función pública"], solo=[2, 3]),
  fichab("Régimen de disponibilidad de los patrimoniales",
         "—",
         ["**Enajenables**, con el procedimiento y requisitos legales", "**Prescriptibles**: usucapión por terceros según el Código Civil y leyes especiales", "**Embargables**, salvo los materialmente afectados a un servicio o función pública, los de rendimientos afectados a fines determinados y los títulos de sociedades estatales que ejecuten políticas públicas o presten servicios de interés económico general (30.3)"],
         "—",
         "Contraste con el dominio público (inalienable, imprescriptible, inembargable: → II.1.3)."))}

{unidad("1.4 Transacción y arbitraje (art. 31)",
  lit("LPAP", "a31", ["sino mediante real decreto acordado en Consejo de Ministros, a propuesta del de Hacienda, previo dictamen del Consejo de Estado en pleno"]),
  fichab("Límite para transigir o ir a arbitraje sobre bienes del Patrimonio del Estado",
         "El **Consejo de Ministros**, a propuesta del Ministro de Hacienda",
         "Por **real decreto** acordado en Consejo de Ministros",
         "Previo dictamen del **Consejo de Estado en pleno**",
         "Real decreto + dictamen del Consejo de Estado **en pleno** (no de la Comisión Permanente). Se refiere a todo el Patrimonio del Estado."))}
""", 2)

T.ap("s12", "III.2 Enajenación, cesión gratuita y permuta (arts. 131, 137, 145 y 153)", f"""
{unidad("2.1 Qué se puede enajenar (art. 131)",
  lit("LPAP", "a131", ["que no sean necesarios para el ejercicio de las competencias y funciones propias", "con reserva del uso temporal de los mismos"]),
  fichab("Bienes enajenables del Patrimonio del Estado",
         "La Administración General del Estado y sus organismos públicos",
         ["Bienes y derechos **patrimoniales** no necesarios para sus competencias y funciones (131.1)", "Excepcionalmente, con **reserva del uso temporal** (arrendamiento u otro contrato simultáneo) (131.2)"],
         "—",
         "Solo los **patrimoniales** y **no necesarios**."))}

{unidad("2.2 Formas de enajenar inmuebles (art. 137.1, 3 y 4)",
  lit("LPAP", "a137", ["mediante subasta, concurso o adjudicación directa", "Cuando el adquirente sea otra Administración pública", "Cuando fuera declarada desierta la subasta o concurso", "siempre que no hubiese transcurrido más de un año desde la celebración de los mismos"], solo=[1, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15]),
  fichab("Procedimientos de enajenación de inmuebles",
         "La Administración titular; el **Consejo de Ministros** identifica los bienes que se enajenan por concurso (137.3)",
         ["**Subasta**", "**Concurso** (bienes calificados por su conexión con políticas públicas)", "**Adjudicación directa** en los supuestos tasados del 137.4 (otra Administración o entidad del sector público, entidades sin ánimo de lucro de utilidad pública o confesiones religiosas, subasta o concurso desiertos o fallidos, solares inedificables o fincas rústicas a colindantes, copropietarios, adquisición preferente, ocupante)"],
         "Adjudicación directa tras subasta o concurso desiertos: si no ha pasado más de **un año**",
         "Tres formas: **subasta, concurso y adjudicación directa**."))}

{unidad("2.3 Cesión gratuita (art. 145)",
  lit("LPAP", "a145", ["cuya afectación o explotación no se juzgue previsible podrán ser cedidos gratuitamente", "a comunidades autónomas, entidades locales, fundaciones públicas o asociaciones declaradas de utilidad pública", "sólo podrán ser cesionarios las comunidades autónomas, entidades locales o fundaciones públicas"], solo=[1, 3, 4]),
  fichab("Cesión gratuita de bienes patrimoniales de la AGE",
         ["Cesionarios: comunidades autónomas, entidades locales, fundaciones públicas o asociaciones declaradas de utilidad pública (145.1)", "Si se cede la **propiedad**: solo comunidades autónomas, entidades locales o fundaciones públicas (145.4)"],
         ["Bienes cuya afectación o explotación no se juzgue previsible", "Para fines de **utilidad pública o interés social**", "Puede cederse la propiedad o solo el uso; el cesionario debe destinarlos al fin del acuerdo"],
         "—",
         "Las **asociaciones** de utilidad pública solo pueden recibir el **uso**, no la propiedad."))}

{unidad("2.4 Permuta (art. 153)",
  lit("LPAP", "a153", ["no sea superior al 50 por ciento de los que lo tengan mayor", "se tramitará como enajenación con pago de parte del precio en especie"]),
  fichab("Permuta de bienes del Patrimonio del Estado",
         "La Administración titular",
         "Cuando convenga al interés público, justificado en el expediente; puede tener por objeto edificios a construir",
         "Diferencia de valor según tasación **no superior al 50 %** de los que lo tengan mayor",
         "Si la diferencia supera el **50 %**, no es permuta: se tramita como **enajenación** con pago de parte del precio en especie."))}

{resumen([
  "Patrimoniales: los que **no** son demaniales; en la AGE, en todo caso, arrendamientos, acciones y participaciones, propiedad incorporal (art. 7).",
  "Principios: eficiencia, **rentabilidad**, publicidad y concurrencia; coadyuvar a la política de **vivienda** (art. 8).",
  "**Enajenables** y **prescriptibles**; embargables salvo las excepciones del 30.3. Transacción y arbitraje: **real decreto** + Consejo de Estado **en pleno** (art. 31).",
  "Inmuebles: **subasta, concurso o adjudicación directa** (art. 137); cesión gratuita (art. 145); permuta si la diferencia no supera el **50 %** (art. 153)."],
  "Siguiente: IV. ¿Qué es el Patrimonio Nacional?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Qué es el Patrimonio Nacional? (Ley 23/1982)", donde(
  "Cuarta pregunta. El art. 132.3 CE distingue el **Patrimonio del Estado** del **Patrimonio Nacional**. Este último lo forman bienes del Estado afectados al **uso y servicio del Rey** y de la Real Familia, y tiene ley propia.",
  ["1 El Consejo de Administración y los bienes que lo integran (Ley 23/1982, arts. 1, 2, 4 y 5)", "2 Régimen jurídico y funciones del Consejo (arts. 6 y 8; Ley 33/2003, disposición adicional cuarta)"]))

T.ap("s13", "IV.1 El Consejo de Administración y los bienes del Patrimonio Nacional (Ley 23/1982, arts. 1, 2, 4 y 5)", f"""
{unidad("1.1 El Consejo de Administración del Patrimonio Nacional (art. 1)",
  lit("L23_1982", "aprimero", ["Entidad de Derecho público, con personalidad jurídica y capacidad de obrar", "orgánicamente dependiente de la Presidencia del Gobierno"], titulo="Artículo primero (Ley 23/1982, del Patrimonio Nacional)"),
  fichab("El organismo que gestiona el Patrimonio Nacional",
         "**Consejo de Administración del Patrimonio Nacional**: entidad de Derecho público con personalidad jurídica, dependiente de la **Presidencia del Gobierno**",
         "Fin: la gestión y administración de los bienes y derechos del Patrimonio Nacional",
         "—",
         "Depende de la **Presidencia del Gobierno**, no del Ministerio de Hacienda (que gestiona el **Patrimonio del Estado**: → I.3.1)."))}

{unidad("1.2 Qué bienes son del Patrimonio Nacional (art. 2)",
  lit("L23_1982", "asegundo", ["afectados al uso y servicio del Rey y de los miembros de la Real Familia", "los derechos y cargas de Patronato"], titulo="Artículo segundo (Ley 23/1982, del Patrimonio Nacional)"),
  fichab("Concepto de bienes del Patrimonio Nacional",
         "Titular: el **Estado**",
         ["Bienes de titularidad del Estado afectados al **uso y servicio del Rey** y de los miembros de la **Real Familia** para el ejercicio de la alta representación que la Constitución y las leyes les atribuyen", "Los derechos y cargas de Patronato sobre las Fundaciones y Reales Patronatos"],
         "—",
         "Los bienes son **del Estado** (no de la Corona): lo que los define es su **afectación** al uso y servicio del Rey y de la Real Familia."))}

{unidad("1.3 Los bienes enumerados por la ley (art. 4)",
  lit("L23_1982", "acuao", ["El Palacio Real de Oriente y el Parque de Campo del Moro", "El Palacio de la Almudaina", "Las donaciones hechas al Estado a través del Rey"], solo=[1, 2, 3, 4, 5, 6, 7, 8, 9], titulo="Artículo cuarto (Ley 23/1982, del Patrimonio Nacional)"),
  fichab("Lista legal de bienes",
         "—",
         ["Palacios y sitios reales (Oriente y Campo del Moro, Aranjuez, El Escorial, La Granja y Riofrío, El Pardo, la Zarzuela, la Almudaina)", "Los **bienes muebles** de titularidad estatal de los reales palacios o depositados en otros inmuebles públicos, según el inventario del Consejo", "Las **donaciones hechas al Estado a través del Rey** y los demás bienes afectados al uso y servicio de la Corona"],
         "—",
         "Las donaciones **a través del Rey** son del **Estado** e integran el Patrimonio Nacional."))}

{unidad("1.4 Los Reales Patronatos (art. 5)",
  lit("L23_1982", "aquinto", ["denominadas Reales Patronatos", "El Monasterio de San Lorenzo de El Escorial", "El Monasterio de Las Huelgas, en Burgos"], solo=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], titulo="Artículo quinto (Ley 23/1982, del Patrimonio Nacional)"),
  fichab("Derechos de patronato sobre fundaciones",
         "El Consejo de Administración ejerce su administración (art. 8.Dos h)",
         "Forman parte del Patrimonio Nacional los **derechos de patronato** o de gobierno y administración sobre las fundaciones enumeradas (doce apartados)",
         "—",
         "Lo que integra el Patrimonio Nacional son los **derechos de patronato**, no la propiedad de esas fundaciones."))}
""", 2)

T.ap("s14", "IV.2 Régimen jurídico y funciones del Consejo (Ley 23/1982, arts. 6 y 8; Ley 33/2003, disposición adicional cuarta)", f"""
{unidad("2.1 Régimen jurídico: inalienables, imprescriptibles e inembargables (art. 6)",
  lit("L23_1982", "asexto", ["Se aplicará, con carácter supletorio, la Ley del Patrimonio del Estado", "inalienables, imprescriptibles e inembargables", "deberán ser inscritos en el Registro de la Propiedad como de titularidad estatal", "recuperación, investigación y deslinde"], titulo="Artículo sexto (Ley 23/1982, del Patrimonio Nacional)"),
  fichab("Régimen de los bienes del Patrimonio Nacional",
         "El Consejo de Administración; las prerrogativas las ejerce el **Ministerio de Hacienda** a su instancia",
         ["**Inalienables, imprescriptibles e inembargables**", "Mismas exenciones tributarias que el dominio público del Estado", "Inscripción en el Registro de la Propiedad como de **titularidad estatal**", "Prerrogativas de **recuperación, investigación y deslinde** a instancia del Consejo", "Si tienen valor histórico-artístico, también su legislación específica"],
         "—",
         "El art. 6 remite como supletoria a la «Ley del Patrimonio del Estado» de 1964, que fue derogada por la Ley 33/2003; hoy la supletoria es la **Ley 33/2003** (→ IV.2.2)."))}

{unidad("2.2 La Ley 33/2003 como supletoria (disposición adicional cuarta y derogatoria única)",
  lit("LPAP", "dacuarta", ["Ley 23/1982, de 16 de junio", "aplicándose con carácter supletorio las disposiciones de esta ley y sus normas de desarrollo"]),
  lit("LPAP", "ddunica", ["y su Texto Articulado, aprobado por Decreto 1022/1964, de 15 de abril"], solo=[1, 2]),
  fichab("Qué norma se aplica al Patrimonio Nacional",
         "—",
         ["Primero: la **Ley 23/1982**, su Reglamento (Real Decreto 496/1987) y disposiciones complementarias", "Supletoriamente: la **Ley 33/2003** y sus normas de desarrollo", "La antigua Ley del Patrimonio del Estado (texto articulado aprobado por Decreto 1022/1964) está **derogada**"],
         "—",
         "Cayó en 2025 (→ Cierre 1): supletoria = **Ley 33/2003**, no la Ley del Patrimonio del Estado de 1964 (derogada) ni las Leyes 39/2015 o 40/2015."))}

{unidad("2.3 Composición y funciones del Consejo de Administración (art. 8)",
  lit("L23_1982", "aoctavo", ["un número de Vocales no superior a trece", "mediante Real Decreto, previa deliberación del Consejo de Ministros a propuesta del Presidente del Gobierno", "La propuesta al Gobierno de desafectación", "En ningún caso podrán desafectarse los bienes muebles o inmuebles de valor histórico-artístico"], solo=[1, 3, 4, 5, 6, 13, 14, 15], titulo="Artículo octavo (Ley 23/1982, del Patrimonio Nacional)"),
  fichab("Quién gobierna el Patrimonio Nacional y qué hace",
         ["Presidente, Gerente y **no más de trece** Vocales, profesionales de reconocido prestigio", "Nombrados por **Real Decreto**, previa deliberación del Consejo de Ministros, a propuesta del **Presidente del Gobierno**"],
         ["Conservación, defensa y mejora de los bienes", "Administración ordinaria", "Inventario, que eleva al Gobierno para su rectificación anual", "**Propone al Gobierno** la afectación y la desafectación"],
         "Vocales: **no más de trece**",
         "El Consejo solo **propone**: afecta y desafecta el **Gobierno**. Los bienes de **valor histórico-artístico** no pueden desafectarse **en ningún caso**."))}

{resumen([
  "Patrimonio Nacional: bienes **del Estado** afectados al **uso y servicio del Rey** y de la Real Familia, y derechos de patronato sobre los **Reales Patronatos** (arts. 2, 4 y 5).",
  "Lo gestiona el **Consejo de Administración del Patrimonio Nacional**, dependiente de la **Presidencia del Gobierno** (art. 1).",
  "Bienes **inalienables, imprescriptibles e inembargables**, inscritos como de **titularidad estatal** (art. 6).",
  "Supletoria: la **Ley 33/2003** (disposición adicional cuarta). Los bienes de valor histórico-artístico **no pueden desafectarse** (art. 8)."],
  "Siguiente: V. ¿Qué son los bienes comunales?")}
""", 2)

# =============================================================================
T.ap("bV", "V. ¿Qué son los bienes comunales? (Ley 7/1985 y Reglamento de Bienes de las Entidades Locales)", donde(
  "Quinta y última pregunta. El art. 132.1 CE cita los **comunales** junto al dominio público. Son bienes **locales** de dominio público cuyo aprovechamiento corresponde al **común de los vecinos**. Se estudian dentro de los bienes de las entidades locales.",
  ["1 Los bienes de las entidades locales (Ley 7/1985, arts. 79 a 82; Reglamento, art. 2)", "2 Aprovechamiento y desafectación de los comunales (Reglamento, arts. 94, 98, 100, 102 y 103)"]))

T.ap("s15", "V.1 Los bienes de las entidades locales (Ley 7/1985, arts. 79 a 82; Reglamento de Bienes, art. 2)", f"""
{unidad("1.1 Clases: dominio público, comunales y patrimoniales (LRBRL, art. 79)",
  lit("LRBRL", "Artículo 79", ["Los bienes de las entidades locales son de dominio público o patrimoniales", "Tienen la consideración de comunales aquellos cuyo aprovechamiento corresponda al común de los vecinos"]),
  fichab("Patrimonio y clases de bienes locales",
         "Las entidades locales",
         ["Patrimonio: bienes, derechos y **acciones** que les pertenezcan", "Dominio público: destinados a un **uso o servicio público**", "**Comunales**: su aprovechamiento corresponde al **común de los vecinos**", "Patrimoniales: los demás"],
         "—",
         "La ley local habla de bienes, derechos **y acciones** (la Ley 33/2003, de «bienes y derechos»)."))}

{unidad("1.2 Régimen: inalienables, inembargables, imprescriptibles y sin tributos (LRBRL, art. 80)",
  lit("LRBRL", "Artículo 80", ["son inalienables, inembargables e imprescriptibles y no están sujetos a tributo alguno", "por las normas de Derecho privado"]),
  fichab("Régimen de los bienes locales",
         "—",
         ["Comunales y demás de dominio público: **inalienables, inembargables, imprescriptibles** y **no sujetos a tributo alguno**", "Patrimoniales: su legislación específica y, en su defecto, el **Derecho privado**"],
         "—",
         "A las tres notas del art. 132 CE la ley local añade una cuarta: **no sujetos a tributo alguno**."))}

{unidad("1.3 Alteración de la calificación jurídica (LRBRL, art. 81)",
  lit("LRBRL", "Artículo 81", ["requiere expediente en el que se acrediten su oportunidad y legalidad", "Adscripción de bienes patrimoniales por más de veinticinco años a un uso o servicio públicos"]),
  fichab("Cambio de clase de un bien local",
         "La entidad local",
         ["Regla: **expediente** que acredite **oportunidad y legalidad**", "Automática: aprobación definitiva de planes de ordenación urbana y de proyectos de obras y servicios", "Automática: adscripción de patrimoniales **más de veinticinco años** a un uso o servicio públicos"],
         "Adscripción durante **más de 25 años**",
         "El Reglamento añade un tercer supuesto automático (usucapión) y exige información pública de un mes y **mayoría absoluta** del número legal de miembros (art. 8)."))}

{unidad("1.4 Prerrogativas de las entidades locales (LRBRL, art. 82)",
  lit("LRBRL", "Artículo 82", ["en cualquier momento cuando se trate de los de dominio público, y en el plazo de un año, los patrimoniales", "se ajustará a lo dispuesto en la legislación del Patrimonio del Estado"]),
  fichab("Defensa de los bienes locales",
         "Las entidades locales",
         ["**Recuperación** de oficio de la posesión", "**Deslinde**, según la legislación del Patrimonio del Estado y, en su caso, la de montes"],
         ["Dominio público: **en cualquier momento**", "Patrimoniales: **un año**"],
         "Mismos plazos que en la Ley 33/2003 (→ I.5.5)."))}

{unidad("1.5 Comunales: concepto y titulares (Reglamento de Bienes, art. 2)",
  lit("RD1372", "art2", ["siendo de dominio público, su aprovechamiento corresponde al común de los vecinos", "Los bienes comunales solo podrán pertenecer a los Municipios y a las Entidades locales menores"], titulo="Artículo 2 (Reglamento de Bienes de las Entidades Locales, RD 1372/1986)"),
  fichab("Qué son y de quién son los comunales",
         "**Municipios** y **entidades locales menores**, solo ellos",
         "Bienes de **dominio público** cuyo aprovechamiento corresponde al común de los vecinos",
         "—",
         "Los comunales **son dominio público**. No pueden ser de **provincias** ni de **comunidades autónomas**."))}
""", 2)

T.ap("s16", "V.2 Aprovechamiento y desafectación de los comunales (Reglamento de Bienes, arts. 94, 98, 100, 102 y 103)", f"""
{unidad("2.1 Formas de aprovechamiento (art. 94)",
  lit("RD1372", "art94", ["en régimen de explotación común o cultivo colectivo", "Aprovechamiento peculiar, según costumbre o reglamentación local", "Adjudicación por lotes o suertes", "se acudirá a la adjudicación mediante precio"], titulo="Artículo 94 (Reglamento de Bienes de las Entidades Locales)"),
  fichab("Orden de las formas de disfrute de los comunales",
         "Los vecinos",
         ["1.º **Explotación común o cultivo colectivo** (regla)", "2.º Si es impracticable: **aprovechamiento peculiar** (costumbre o reglamentación local) o **adjudicación por lotes o suertes**", "3.º Si tampoco es posible: **adjudicación mediante precio**"],
         "—",
         "El orden es **escalonado**: el precio es el **último** recurso."))}

{unidad("2.2 Adjudicación mediante precio (art. 98)",
  lit("RD1372", "art98", ["habrá de ser autorizada por el órgano competente de la Comunidad Autónoma", "por subasta pública", "sin que pueda detraerse por la Corporación más de un 5 por 100 del importe"], titulo="Artículo 98 (Reglamento de Bienes de las Entidades Locales)"),
  fichab("Cuando los comunales se adjudican por precio",
         "Autoriza el órgano competente de la **Comunidad Autónoma**",
         ["**Subasta pública**, con preferencia de los postores **vecinos** en igualdad de condiciones", "Sin licitadores: adjudicación directa", "El producto, a servicios para quienes tengan derecho al aprovechamiento"],
         "La Corporación no puede detraer más del **5 %** del importe",
         "Autoriza la **Comunidad Autónoma**; máximo detraíble, **5 %**."))}

{unidad("2.3 Pérdida del carácter comunal por falta de disfrute (art. 100)",
  lit("RD1372", "art100", ["durante más de diez años", "voto favorable de la mayoría absoluta del número legal de miembros de la Corporación y posterior aprobación por la Comunidad Autónoma", "otorgándose preferencia a los vecinos del municipio"], titulo="Artículo 100 (Reglamento de Bienes de las Entidades Locales)"),
  fichab("Desafectación de comunales no disfrutados",
         "Acuerdo de la **Corporación**; aprobación posterior de la **Comunidad Autónoma**",
         ["Información pública", "Si resultan patrimoniales: arrendamiento a quien se comprometa a su aprovechamiento agrícola, con preferencia de los vecinos"],
         ["Sin disfrute comunal durante **más de diez años** (aunque haya actos aislados de aprovechamiento)", "**Mayoría absoluta** del número legal de miembros"],
         "Cayó en 2025 (→ Cierre 1): **diez** años, no cinco, quince ni veinte."))}

{unidad("2.4 Cesión del aprovechamiento y titulares del derecho (arts. 102 y 103.1)",
  lit("RD1372", "art102", ["deberá ser acordada por el Pleno de la Corporación", "mayoría absoluta del número legal de miembros"], titulo="Artículo 102 (Reglamento de Bienes de las Entidades Locales)"),
  lit("RD1372", "art103", ["sin distinción de sexo, estado civil o edad", "Los extranjeros domiciliados en el termino municipal gozarán también de estos derechos"], solo=[1], titulo="Artículo 103 (Reglamento de Bienes de las Entidades Locales)"),
  fichab("Quién puede aprovechar los comunales y cómo se cede ese aprovechamiento",
         ["Titulares del derecho: los **vecinos**, sin distinción de sexo, estado civil o edad", "También los **extranjeros domiciliados** en el término municipal"],
         "Cesión por cualquier título del aprovechamiento: acuerdo del **Pleno**",
         "**Mayoría absoluta** del número legal de miembros",
         "Los **extranjeros domiciliados** también tienen derecho al aprovechamiento."))}

*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| | Dominio público local | Comunales | Patrimoniales locales |
|---|---|---|---|
| Qué son (LRBRL 79) | Destinados a un uso o servicio público | Aprovechamiento del común de los vecinos (son dominio público: RBEL 2.3) | Los demás |
| Titulares | Entidades locales | Solo municipios y entidades locales menores (RBEL 2.4) | Entidades locales |
| Régimen (LRBRL 80) | Inalienables, inembargables, imprescriptibles, sin tributos | Igual | Legislación específica y, en su defecto, Derecho privado |
| Recuperación de oficio (LRBRL 82) | En cualquier momento | En cualquier momento | Un año |

{resumen([
  "Bienes locales: **dominio público** (uso o servicio público), **comunales** (aprovechamiento del común de los vecinos) y **patrimoniales** (LRBRL 79).",
  "Comunales y dominio público: **inalienables, inembargables, imprescriptibles** y **no sujetos a tributo alguno** (LRBRL 80); solo de **municipios** y **entidades locales menores** (RBEL 2.4).",
  "Aprovechamiento: **explotación común** → peculiar o **lotes** → **precio** (RBEL 94); por precio, autoriza la **Comunidad Autónoma** (98).",
  "Pierden el carácter comunal tras **más de diez años** sin disfrute: acuerdo por **mayoría absoluta** y aprobación de la **Comunidad Autónoma** (RBEL 100)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_P69 = examen("P", 69, {
  "a": "Un acuerdo del Consejo de Ministros no es una ley: el art. 132.3 exige ley.",
  "b": f"Cambia el tipo de ley: el art. 132.3 dice {c('CE', 'Artículo 132', 'Por ley se regularán')}, sin exigir ley orgánica (las materias de ley orgánica son las del art. 81).",
  "c": f"Literal del art. 132.3: {c('CE', 'Artículo 132', 'Por ley se regularán el Patrimonio del Estado y el Patrimonio Nacional, su administración, defensa y conservación')}.",
  "d": "Un decreto del Consejo de Ministros es una norma reglamentaria, no una ley."},
  [("Por Ley.", "CE", "Artículo 132", "Por ley se regularán el Patrimonio del Estado y el Patrimonio Nacional, su administración, defensa y conservación")])
EX_P70 = examen("P", 70, {
  "a": "Cambia el ministerio: no es Cultura, sino Hacienda.",
  "b": f"Confunde con el **Patrimonio Nacional**, cuyo Consejo de Administración depende de la Presidencia del Gobierno: {c('L23_1982', 'aprimero', 'orgánicamente dependiente de la Presidencia del Gobierno')} (Ley 23/1982, art. 1). El Patrimonio del Estado es otra cosa.",
  "c": "Cambia el ministerio y el órgano: la Presidencia de Patrimonio Nacional gestiona el Patrimonio Nacional, no el Patrimonio del Estado.",
  "d": f"Literal del art. 9.2: {c('LPAP', 'a9', 'corresponderán al Ministerio de Hacienda, a través de la Dirección General del Patrimonio del Estado')}."},
  [("Ministerio de Hacienda", "LPAP", "a9", "corresponderán al Ministerio de Hacienda, a través de la Dirección General del Patrimonio del Estado"),
   ("Dirección General del Patrimonio del Estado", "LPAP", "a9", "corresponderán al Ministerio de Hacienda, a través de la Dirección General del Patrimonio del Estado")])
EX_L55 = examen("L", 55, {
  "a": f"Invierte la regla: {c('LPAP', 'a50', 'no podrá instarse procedimiento judicial con igual pretensión')} (art. 50.2).",
  "b": f"Cambia el órgano: la incoación {c('LPAP', 'a51', 'se acordará por el Director General del Patrimonio del Estado')}; al Ministro de Hacienda le corresponde la **resolución** (art. 51.1).",
  "c": f"Cambia el órgano: {c('LPAP', 'a51', 'corresponderá al Ministro de Hacienda la resolución del mismo')}; el Director General **incoa** (art. 51.1).",
  "d": f"Literal del art. 51.1: {c('LPAP', 'a51', 'La instrucción del procedimiento corresponderá a los Delegados de Economía y Hacienda')}."},
  [("La instrucción del procedimiento corresponderá a los Delegados de Economía y Hacienda", "LPAP", "a51", "La instrucción del procedimiento corresponderá a los Delegados de Economía y Hacienda")])
EX_X60 = examen("X", 60, {
  "a": f"La Ley 33/2003 (disposición adicional cuarta) fija el régimen del Patrimonio Nacional en la Ley 23/1982 y su Reglamento, {c('LPAP', 'dacuarta', 'aplicándose con carácter supletorio las disposiciones de esta ley y sus normas de desarrollo')}.",
  "b": f"El art. 6 de la Ley 23/1982 todavía dice {c('L23_1982', 'asexto', 'Se aplicará, con carácter supletorio, la Ley del Patrimonio del Estado')}, pero ese texto articulado está derogado: la Ley 33/2003 deroga {c('LPAP', 'ddunica', 'su Texto Articulado, aprobado por Decreto 1022/1964, de 15 de abril')} y la sustituye como supletoria.",
  "c": "La Ley 39/2015 regula el procedimiento administrativo común; ninguna de las dos leyes la designa supletoria del régimen del Patrimonio Nacional.",
  "d": "La Ley 40/2015 regula el régimen jurídico del sector público; ninguna de las dos leyes la designa supletoria del régimen del Patrimonio Nacional."},
  [("Ley 33/2003", "LPAP", "dacuarta", "aplicándose con carácter supletorio las disposiciones de esta ley y sus normas de desarrollo"),
   ("Ley 33/2003", "LPAP", "ddunica", "La Ley 89/1962, de 24 de diciembre, de Bases del Patrimonio del Estado, y su Texto Articulado, aprobado por Decreto 1022/1964, de 15 de abril")])
EX_X59 = examen("X", 59, {
  "a": "Cambia el plazo: el art. 100.1 dice diez años, no cinco.",
  "b": f"Literal del art. 100.1: {c('RD1372', 'art100', 'no han sido objeto de disfrute de esta índole durante más de diez años')}.",
  "c": "Cambia el plazo: quince años no aparece en el art. 100.1.",
  "d": "Cambia el plazo: veinte años no aparece en el art. 100.1."},
  [("Diez años", "RD1372", "art100", "durante más de diez años")])

T.ap("s17", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **cinco** preguntas de este tema: una de la Constitución, dos de la Ley 33/2003, una del Patrimonio Nacional y una de los bienes comunales. Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-P 2025, pregunta 69 · Reserva de ley del art. 132.3 (→ I.1.1)", EX_P69,
  "### GACE-P 2025, pregunta 70 · Gestión del Patrimonio del Estado (→ I.3.1)", EX_P70,
  "### GACE-L 2025, pregunta 55 · Órganos del deslinde (→ I.5.3)", EX_L55,
  "### GACE-L 2025 extraordinario, pregunta 60 · Norma supletoria del Patrimonio Nacional (→ IV.2.2)", EX_X60,
  "?> **Nota sobre esta pregunta.** El enunciado dice «según la Ley 23/1982», cuyo art. 6 sigue remitiendo literalmente a la «Ley del Patrimonio del Estado» (la opción b la identifica con el Decreto 1022/1964). La plantilla da la a), que es lo vigente: ese texto de 1964 está derogado por la Ley 33/2003, cuya disposición adicional cuarta la declara supletoria para el Patrimonio Nacional. Conviene saber las dos cosas.",
  "### GACE-L 2025 extraordinario, pregunta 59 · Comunales no disfrutados (→ V.2.3)", EX_X59,
  "### Cómo se pregunta",
  "!> Las preguntas de la Ley 33/2003 cambian el **órgano** (Ministro, Director General, Delegados; Hacienda frente a Presidencia o Cultura) y las del Reglamento de Bienes, el **plazo**. Para el Patrimonio Nacional, distinguir **Patrimonio del Estado** (Hacienda) de **Patrimonio Nacional** (Consejo de Administración, Presidencia del Gobierno).",
]))

T.ap("s18", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Régimen patrimonial | Art. 132 CE; patrimonio = bienes y derechos; dos clases; Patrimonio del Estado; prerrogativas | **Por ley** (132.3); Hacienda + **DG del Patrimonio del Estado** (9.2); deslinde: incoa el **DG**, instruyen los **Delegados**, resuelve el **Ministro** |
| II. Dominio público | Afectado a uso general o servicio público; principios; afectación y desafectación; usos y títulos | Inalienable, imprescriptible, inembargable; autorización **4 años**, concesión **75 años** |
| III. Bienes patrimoniales | Concepto residual; rentabilidad; enajenación, cesión y permuta | Subasta, concurso o adjudicación directa; permuta hasta el **50 %**; transacción: real decreto + Consejo de Estado **en pleno** |
| IV. Patrimonio Nacional | Bienes del Estado al uso y servicio del Rey; Consejo de Administración | Depende de la **Presidencia del Gobierno**; supletoria la **Ley 33/2003** |
| V. Bienes comunales | Dominio público local de aprovechamiento vecinal | Solo **municipios y entidades locales menores**; pierden el carácter tras **más de 10 años** sin disfrute |

?> **Trampas frecuentes:** «por **ley orgánica**» (art. 132.3: **por ley**); «el **Ministro** incoa el deslinde» (incoa el **Director General**; el Ministro **resuelve**); «durante el deslinde **podrá** instarse un procedimiento judicial» (**no podrá**); «los patrimoniales se recuperan **en cualquier tiempo**» (**un año**; en cualquier tiempo, los **demaniales**); «la autorización dura hasta **75 años**» (**4**; los 75 son de la **concesión**); «el Patrimonio Nacional lo gestiona **Hacienda**» (su **Consejo de Administración**, dependiente de la **Presidencia del Gobierno**); «comunales de la **provincia**» (solo **municipios** y **entidades locales menores**).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
Q = [
 ("CE", "Artículo 132", "Constitución", "Según el artículo 132.1 de la Constitución, la ley regulará el régimen jurídico de los bienes de dominio público y de los comunales inspirándose en los principios de:",
  ["Inalienabilidad, imprescriptibilidad e inembargabilidad.", "Inalienabilidad, prescriptibilidad e inembargabilidad.", "Eficiencia, economía y rentabilidad.", "Publicidad, concurrencia y objetividad."],
  "Art. 132.1 CE.", "inalienabilidad, imprescriptibilidad e inembargabilidad"),
 ("CE", "Artículo 132", "Constitución", "Según el artículo 132.2 de la Constitución, ¿cuál de los siguientes bienes es, en todo caso, de dominio público estatal?",
  ["Las playas.", "Los montes vecinales en mano común.", "Los edificios de las Diputaciones Provinciales.", "Los palacios reales."],
  "Art. 132.2 CE: zona marítimo-terrestre, playas, mar territorial y recursos naturales de la zona económica y la plataforma continental.", "la zona marítimo-terrestre, las playas, el mar territorial"),
 ("LPAP", "a3", "Concepto y clases", "Según el artículo 3 de la Ley 33/2003, del Patrimonio de las Administraciones Públicas, NO se entenderán incluidos en el patrimonio de las Administraciones públicas:",
  ["El dinero, los valores, los créditos y los demás recursos financieros de su hacienda.", "Los bienes inmuebles adquiridos por herencia.", "Los derechos de propiedad incorporal.", "Las acciones en sociedades mercantiles."],
  "Art. 3.2 LPAP.", "No se entenderán incluidos en el patrimonio de las Administraciones públicas el dinero, los valores, los créditos y los demás recursos financieros de su hacienda"),
 ("LPAP", "a4", "Concepto y clases", "Según el artículo 4 de la Ley 33/2003, por razón del régimen jurídico al que están sujetos, los bienes y derechos que integran el patrimonio de las Administraciones públicas pueden ser:",
  ["De dominio público o demaniales y de dominio privado o patrimoniales.", "De uso público, de servicio público y comunales.", "Muebles, inmuebles y derechos.", "Estatales, autonómicos y locales."],
  "Art. 4 LPAP.", "de dominio público o demaniales y de dominio privado o patrimoniales"),
 ("LPAP", "a9", "Patrimonio del Estado", "Según el artículo 9.1 de la Ley 33/2003, el Patrimonio del Estado está integrado por:",
  ["El patrimonio de la Administración General del Estado y los patrimonios de los organismos públicos dependientes o vinculados a ella.", "Solo el patrimonio de la Administración General del Estado.", "Los bienes afectados al uso y servicio del Rey.", "El patrimonio de todas las Administraciones públicas."],
  "Art. 9.1 LPAP.", "El Patrimonio del Estado está integrado por el patrimonio de la Administración General del Estado y los patrimonios de los organismos públicos"),
 ("LPAP", "a10", "Patrimonio del Estado", "Según el artículo 10.1 de la Ley 33/2003, definir la política aplicable a los bienes y derechos del Patrimonio del Estado corresponde:",
  ["Al Consejo de Ministros, a propuesta del Ministro de Hacienda.", "Al Ministro de Hacienda, a propuesta de la Dirección General del Patrimonio del Estado.", "A la Dirección General del Patrimonio del Estado.", "A cada departamento ministerial."],
  "Art. 10.1 a) LPAP.", "Corresponde al Consejo de Ministros, a propuesta del Ministro de Hacienda"),
 ("LPAP", "a36", "Protección", "Según el artículo 36.1 de la Ley 33/2003, la inscripción en el Registro de la Propiedad será potestativa para las Administraciones públicas en el caso de:",
  ["Arrendamientos inscribibles conforme a la legislación hipotecaria.", "Bienes demaniales.", "Bienes patrimoniales adquiridos por expropiación.", "Concesiones demaniales."],
  "Art. 36.1 LPAP: se inscriben demaniales y patrimoniales; potestativa solo para los arrendamientos.", "la inscripción será potestativa para las Administraciones públicas en el caso de arrendamientos inscribibles"),
 ("LPAP", "a41", "Prerrogativas", "Según el artículo 41.1 de la Ley 33/2003, ¿cuál de las siguientes NO es una facultad o prerrogativa de las Administraciones públicas para la defensa de su patrimonio?",
  ["Embargar los bienes de los ocupantes sin título.", "Deslindar en vía administrativa los inmuebles de su titularidad.", "Recuperar de oficio la posesión indebidamente perdida sobre sus bienes y derechos.", "Investigar la situación de los bienes y derechos que presumiblemente pertenezcan a su patrimonio."],
  "Art. 41.1 LPAP: investigar, deslindar, recuperar de oficio y desahuciar.", "Deslindar en vía administrativa los inmuebles de su titularidad"),
 ("LPAP", "a41", "Prerrogativas", "Según el artículo 41.3 de la Ley 33/2003, las entidades públicas empresariales dependientes de la Administración General del Estado podrán ejercer las potestades de defensa de su patrimonio:",
  ["Solo para la defensa de bienes que tengan el carácter de demaniales.", "Solo para la defensa de bienes patrimoniales.", "Para la defensa de todos sus bienes.", "En ningún caso."],
  "Art. 41.3 LPAP.", "sólo podrán ejercer las potestades enumeradas en el apartado 1 de este artículo para la defensa de bienes que tengan el carácter de demaniales"),
 ("LPAP", "a43", "Prerrogativas", "Según el artículo 43.1 de la Ley 33/2003, frente a las actuaciones de las Administraciones públicas en ejercicio de sus prerrogativas de defensa del patrimonio:",
  ["No cabrá la acción para la tutela sumaria de la posesión.", "Cabrá la acción para la tutela sumaria de la posesión ante el orden civil.", "Solo cabrá recurso ante el Tribunal Constitucional.", "Cabrá reclamación económico-administrativa."],
  "Art. 43.1 LPAP.", "no cabrá la acción para la tutela sumaria de la posesión"),
 ("LPAP", "a47", "Prerrogativas", "Según el artículo 47 de la Ley 33/2003, si el expediente de investigación no se resuelve en el plazo de ____ desde el día siguiente al de la publicación del acuerdo de incoación, el órgano instructor acordará el archivo de las actuaciones:",
  ["Dos años.", "Dieciocho meses.", "Un año.", "Seis meses."],
  "Art. 47 e) LPAP: dos años.", "no fuese resuelto en el plazo de dos años"),
 ("LPAP", "a50", "Prerrogativas", "Según el artículo 50.1 de la Ley 33/2003, las Administraciones públicas podrán deslindar los bienes inmuebles de su patrimonio de otros pertenecientes a terceros cuando:",
  ["Los límites entre ellos sean imprecisos o existan indicios de usurpación.", "Lo solicite el Registro de la Propiedad.", "Hayan transcurrido más de diez años desde su adquisición.", "Así lo acuerde el juez civil."],
  "Art. 50.1 LPAP.", "cuando los límites entre ellos sean imprecisos o existan indicios de usurpación"),
 ("LPAP", "a51", "Prerrogativas", "Según el artículo 51.1 de la Ley 33/2003, la resolución del procedimiento para deslindar los bienes patrimoniales de la Administración General del Estado corresponde:",
  ["Al Ministro de Hacienda.", "Al Director General del Patrimonio del Estado.", "A los Delegados de Economía y Hacienda.", "Al Consejo de Ministros."],
  "Art. 51.1 LPAP: incoa el Director General, instruyen los Delegados y resuelve el Ministro.", "corresponderá al Ministro de Hacienda la resolución del mismo"),
 ("LPAP", "a52", "Prerrogativas", "Según el artículo 52 de la Ley 33/2003, el plazo máximo para resolver el procedimiento de deslinde será de:",
  ["18 meses, contados desde la fecha del acuerdo de iniciación.", "Dos años, contados desde la publicación en el BOE.", "Seis meses, contados desde la fecha del acuerdo de iniciación.", "Un año, contado desde la solicitud de los colindantes."],
  "Art. 52 e) LPAP.", "El plazo máximo para resolver el procedimiento de deslinde será de 18 meses, contados desde la fecha del acuerdo de iniciación"),
 ("LPAP", "a55", "Prerrogativas", "Según el artículo 55 de la Ley 33/2003, si los bienes cuya posesión se trata de recuperar tienen la condición de demaniales, la potestad de recuperación podrá ejercitarse:",
  ["En cualquier tiempo.", "En el plazo de un año desde la usurpación.", "En el plazo de cuatro años desde la usurpación.", "Solo mientras no haya prescrito la acción civil."],
  "Art. 55.2 LPAP; para los patrimoniales, un año (55.3).", "la potestad de recuperación podrá ejercitarse en cualquier tiempo"),
 ("LPAP", "a55", "Prerrogativas", "Según el artículo 55.3 de la Ley 33/2003, la recuperación en vía administrativa de la posesión de bienes patrimoniales requiere que la iniciación del procedimiento haya sido notificada antes de que transcurra el plazo de:",
  ["Un año, contado desde el día siguiente al de la usurpación.", "Seis meses, contados desde el día siguiente al de la usurpación.", "Dos años, contados desde la usurpación.", "Treinta años, plazo de la prescripción adquisitiva."],
  "Art. 55.3 LPAP.", "antes de que transcurra el plazo de un año, contado desde el día siguiente al de la usurpación"),
 ("LPAP", "a58", "Prerrogativas", "Según el artículo 58 de la Ley 33/2003, la potestad de desahucio permite a las Administraciones públicas recuperar en vía administrativa la posesión de:",
  ["Sus bienes demaniales, cuando decaigan o desaparezcan el título, las condiciones o las circunstancias que legitimaban su ocupación por terceros.", "Sus bienes patrimoniales arrendados, cuando el arrendatario deje de pagar la renta.", "Cualquier bien usurpado, en el plazo de un año.", "Los bienes de los particulares necesarios para un servicio público."],
  "Art. 58 LPAP.", "podrán recuperar en vía administrativa la posesión de sus bienes demaniales cuando decaigan o desaparezcan el título"),
 ("LPAP", "a5", "Dominio público", "Según el artículo 5.1 de la Ley 33/2003, son bienes y derechos de dominio público los que, siendo de titularidad pública:",
  ["Se encuentren afectados al uso general o al servicio público, así como aquellos a los que una ley otorgue expresamente el carácter de demaniales.", "Produzcan rentas para la Hacienda pública.", "Estén inscritos en el Inventario General de Bienes y Derechos del Estado.", "Hayan sido adquiridos por expropiación forzosa, en todo caso."],
  "Art. 5.1 LPAP.", "se encuentren afectados al uso general o al servicio público, así como aquellos a los que una ley otorgue expresamente el carácter de demaniales"),
 ("LPAP", "a5", "Dominio público", "Según el artículo 5.4 de la Ley 33/2003, a falta de normas especiales y de esta ley, a los bienes de dominio público se aplicarán como derecho supletorio:",
  ["Las normas generales del derecho administrativo y, en su defecto, las normas del derecho privado.", "Las normas del derecho privado y, en su defecto, las del derecho administrativo.", "Solo las normas del Código Civil.", "Las ordenanzas de la entidad titular."],
  "Art. 5.4 LPAP.", "Las normas generales del derecho administrativo y, en su defecto, las normas del derecho privado, se aplicarán como derecho supletorio"),
 ("LPAP", "a6", "Dominio público", "Según el artículo 6 de la Ley 33/2003, es principio de la gestión y administración de los bienes demaniales:",
  ["La dedicación preferente al uso común frente a su uso privativo.", "La eficacia y rentabilidad en su explotación.", "La dedicación preferente al uso privativo frente al uso común.", "La enajenación de los bienes no necesarios."],
  "Art. 6 d) LPAP. La rentabilidad es principio de los patrimoniales (art. 8).", "Dedicación preferente al uso común frente a su uso privativo"),
 ("LPAP", "a65", "Dominio público", "Según el artículo 65 de la Ley 33/2003, la afectación determina:",
  ["La vinculación de los bienes y derechos a un uso general o a un servicio público, y su consiguiente integración en el dominio público.", "La pérdida de la condición demanial de un bien.", "El cambio de destino de un bien demanial a otro servicio público.", "La puesta a disposición de un bien a favor de un organismo público."],
  "Art. 65 LPAP. La pérdida es la desafectación (69) y el cambio de destino, la mutación (71).", "La afectación determina la vinculación de los bienes y derechos a un uso general o a un servicio público"),
 ("LPAP", "a66", "Dominio público", "Según el artículo 66.2 de la Ley 33/2003, surtirá los mismos efectos que la afectación expresa:",
  ["La utilización pública, notoria y continuada por la Administración General del Estado de bienes de su titularidad para un servicio público.", "La inscripción del bien en el Registro de la Propiedad.", "La inclusión del bien en el Inventario General.", "El arrendamiento del bien a un particular."],
  "Art. 66.2 a) LPAP.", "La utilización pública, notoria y continuada por la Administración General del Estado"),
 ("LPAP", "a69", "Dominio público", "Según el artículo 69.2 de la Ley 33/2003, salvo en los supuestos previstos en esta ley, la desafectación deberá realizarse:",
  ["Siempre de forma expresa.", "De forma tácita, por el simple desuso.", "Mediante ley.", "Por real decreto acordado en Consejo de Ministros."],
  "Art. 69.2 LPAP.", "la desafectación deberá realizarse siempre de forma expresa"),
 ("LPAP", "a71", "Dominio público", "Según el artículo 71.1 de la Ley 33/2003, el acto por el que se efectúa la desafectación de un bien del Patrimonio del Estado con simultánea afectación a otro uso general, fin o servicio público es:",
  ["La mutación demanial.", "La adscripción.", "La desafectación.", "La cesión gratuita."],
  "Art. 71.1 LPAP.", "La mutación demanial es el acto en virtud del cual se efectúa la desafectación"),
 ("LPAP", "a85", "Uso del dominio público", "Según el artículo 85.3 de la Ley 33/2003, el uso que determina la ocupación de una porción del dominio público, de modo que se limita o excluye la utilización del mismo por otros interesados, es el:",
  ["Uso privativo.", "Uso común.", "Aprovechamiento especial.", "Uso general."],
  "Art. 85.3 LPAP.", "Es uso privativo el que determina la ocupación de una porción del dominio público"),
 ("LPAP", "a86", "Uso del dominio público", "Según el artículo 86.3 de la Ley 33/2003, el uso privativo de los bienes de dominio público que determine su ocupación con obras o instalaciones fijas deberá estar amparado por:",
  ["La correspondiente concesión administrativa.", "Una autorización, si no excede de cuatro años.", "Una licencia municipal.", "Un contrato de arrendamiento."],
  "Art. 86.3 LPAP.", "con obras o instalaciones fijas deberá estar amparado por la correspondiente concesión administrativa"),
 ("LPAP", "a86", "Uso del dominio público", "Según el artículo 86.2 de la Ley 33/2003, el aprovechamiento especial de los bienes de dominio público estará sujeto a concesión si la duración del aprovechamiento excede de:",
  ["Cuatro años.", "Un año.", "Diez años.", "Setenta y cinco años."],
  "Art. 86.2 LPAP.", "si la duración del aprovechamiento o uso excede de cuatro años, a concesión"),
 ("LPAP", "a92", "Uso del dominio público", "Según el artículo 92.3 de la Ley 33/2003, el plazo máximo de duración de las autorizaciones, incluidas las prórrogas, será de:",
  ["Cuatro años.", "Diez años.", "Setenta y cinco años.", "Noventa y nueve años."],
  "Art. 92.3 LPAP.", "Su plazo máximo de duración, incluidas las prórrogas, será de cuatro años"),
 ("LPAP", "a92", "Uso del dominio público", "Según el artículo 92.4 de la Ley 33/2003, las autorizaciones podrán ser revocadas unilateralmente por la Administración concedente en cualquier momento por razones de interés público:",
  ["Sin generar derecho a indemnización.", "Previa indemnización.", "Solo con el acuerdo del autorizado.", "Previo dictamen del Consejo de Estado."],
  "Art. 92.4 LPAP. El rescate de la concesión, en cambio, es previa indemnización (art. 100 d).", "sin generar derecho a indemnización"),
 ("LPAP", "a93", "Uso del dominio público", "Según el artículo 93.3 de la Ley 33/2003, el plazo máximo de duración de las concesiones demaniales, incluidas las prórrogas, no podrá exceder, salvo que se establezca otro menor en las normas especiales, de:",
  ["75 años.", "50 años.", "99 años.", "4 años."],
  "Art. 93.3 LPAP.", "no podrá exceder de 75 años"),
 ("LPAP", "a93", "Uso del dominio público", "Según el artículo 93.1 de la Ley 33/2003, el otorgamiento de concesiones sobre bienes de dominio público se efectuará, como regla general:",
  ["En régimen de concurrencia.", "De forma directa a los peticionarios que reúnan las condiciones.", "Mediante sorteo.", "Por real decreto acordado en Consejo de Ministros."],
  "Art. 93.1 LPAP. El otorgamiento directo es la regla de las autorizaciones (art. 92.1).", "se efectuará en régimen de concurrencia"),
 ("LPAP", "a7", "Bienes patrimoniales", "Según el artículo 7.1 de la Ley 33/2003, son bienes y derechos de dominio privado o patrimoniales los que, siendo de titularidad de las Administraciones públicas:",
  ["No tengan el carácter de demaniales.", "Estén afectados a un servicio público.", "Se destinen al uso general.", "Hayan sido declarados como tales por ley."],
  "Art. 7.1 LPAP: concepto residual.", "no tengan el carácter de demaniales"),
 ("LPAP", "a30", "Bienes patrimoniales", "Según el artículo 30.2 de la Ley 33/2003, los bienes y derechos patrimoniales:",
  ["Podrán ser objeto de prescripción adquisitiva por terceros de acuerdo con lo dispuesto en el Código Civil y en las leyes especiales.", "Son imprescriptibles.", "Son inalienables.", "Solo pueden enajenarse por ley."],
  "Art. 30.2 LPAP.", "podrán ser objeto de prescripción adquisitiva por terceros"),
 ("LPAP", "a31", "Bienes patrimoniales", "Según el artículo 31 de la Ley 33/2003, para transigir judicial o extrajudicialmente sobre los bienes y derechos del Patrimonio del Estado se requiere:",
  ["Real decreto acordado en Consejo de Ministros, a propuesta del de Hacienda, previo dictamen del Consejo de Estado en pleno.", "Orden del Ministro de Hacienda, previo informe de la Abogacía del Estado.", "Real decreto acordado en Consejo de Ministros, previo dictamen de la Comisión Permanente del Consejo de Estado.", "Ley de las Cortes Generales."],
  "Art. 31 LPAP.", "sino mediante real decreto acordado en Consejo de Ministros, a propuesta del de Hacienda, previo dictamen del Consejo de Estado en pleno"),
 ("LPAP", "a137", "Bienes patrimoniales", "Según el artículo 137.1 de la Ley 33/2003, la enajenación de los inmuebles podrá realizarse mediante:",
  ["Subasta, concurso o adjudicación directa.", "Solo subasta pública.", "Subasta o permuta.", "Concurso o sorteo."],
  "Art. 137.1 LPAP.", "La enajenación de los inmuebles podrá realizarse mediante subasta, concurso o adjudicación directa"),
 ("LPAP", "a145", "Bienes patrimoniales", "Según el artículo 145.4 de la Ley 33/2003, cuando la cesión gratuita tenga por objeto la propiedad del bien o derecho, sólo podrán ser cesionarios:",
  ["Las comunidades autónomas, entidades locales o fundaciones públicas.", "Las asociaciones declaradas de utilidad pública.", "Los Estados extranjeros.", "Cualquier entidad sin ánimo de lucro."],
  "Art. 145.4 LPAP.", "sólo podrán ser cesionarios las comunidades autónomas, entidades locales o fundaciones públicas"),
 ("LPAP", "a153", "Bienes patrimoniales", "Según el artículo 153 de la Ley 33/2003, los bienes del Patrimonio del Estado podrán ser permutados cuando la diferencia de valor entre los bienes, según tasación, no sea superior al:",
  ["50 por ciento de los que lo tengan mayor.", "25 por ciento de los que lo tengan menor.", "10 por ciento de los que lo tengan mayor.", "75 por ciento de los que lo tengan mayor."],
  "Art. 153 LPAP.", "no sea superior al 50 por ciento de los que lo tengan mayor"),
 ("L23_1982", "aprimero", "Patrimonio Nacional", "Según el artículo primero de la Ley 23/1982, reguladora del Patrimonio Nacional, el Consejo de Administración del Patrimonio Nacional depende orgánicamente:",
  ["De la Presidencia del Gobierno.", "Del Ministerio de Hacienda.", "De la Casa de Su Majestad el Rey.", "Del Ministerio de Cultura."],
  "Art. 1 de la Ley 23/1982.", "orgánicamente dependiente de la Presidencia del Gobierno"),
 ("L23_1982", "asegundo", "Patrimonio Nacional", "Según el artículo segundo de la Ley 23/1982, tienen la calificación jurídica de bienes del Patrimonio Nacional los de titularidad del Estado afectados:",
  ["Al uso y servicio del Rey y de los miembros de la Real Familia para el ejercicio de la alta representación que la Constitución y las leyes les atribuyen.", "A los servicios de las Cortes Generales.", "Al uso general de los ciudadanos con fines culturales.", "A la Presidencia del Gobierno."],
  "Art. 2 de la Ley 23/1982.", "afectados al uso y servicio del Rey y de los miembros de la Real Familia"),
 ("L23_1982", "asexto", "Patrimonio Nacional", "Según el artículo sexto de la Ley 23/1982, los bienes y derechos integrados en el Patrimonio Nacional serán:",
  ["Inalienables, imprescriptibles e inembargables.", "Enajenables previa autorización del Rey.", "Prescriptibles conforme al Código Civil.", "Embargables solo por deudas tributarias."],
  "Art. 6.Dos de la Ley 23/1982.", "serán inalienables, imprescriptibles e inembargables"),
 ("L23_1982", "aoctavo", "Patrimonio Nacional", "Según el artículo octavo de la Ley 23/1982, el Consejo de Administración del Patrimonio Nacional estará constituido por su Presidente, el Gerente y por un número de Vocales no superior a:",
  ["Trece.", "Nueve.", "Quince.", "Veinte."],
  "Art. 8.Uno de la Ley 23/1982.", "un número de Vocales no superior a trece"),
 ("L23_1982", "aoctavo", "Patrimonio Nacional", "Según el artículo octavo de la Ley 23/1982, respecto de los bienes muebles o inmuebles de valor histórico-artístico del Patrimonio Nacional:",
  ["En ningún caso podrán desafectarse.", "Podrá proponerse su desafectación cuando dejen de cumplir sus finalidades primordiales.", "Podrán desafectarse por real decreto.", "Podrán desafectarse por acuerdo del Consejo de Administración."],
  "Art. 8.Dos k) de la Ley 23/1982.", "En ningún caso podrán desafectarse los bienes muebles o inmuebles de valor histórico-artístico"),
 ("LRBRL", "Artículo 79", "Bienes comunales", "Según el artículo 79.3 de la Ley 7/1985, Reguladora de las Bases del Régimen Local, tienen la consideración de comunales aquellos bienes:",
  ["Cuyo aprovechamiento corresponda al común de los vecinos.", "Destinados a un uso o servicio público.", "Que puedan constituir fuentes de ingresos para el erario de la entidad.", "Que pertenezcan conjuntamente a varios municipios."],
  "Art. 79.3 LRBRL.", "Tienen la consideración de comunales aquellos cuyo aprovechamiento corresponda al común de los vecinos"),
 ("LRBRL", "Artículo 80", "Bienes comunales", "Según el artículo 80.1 de la Ley 7/1985, los bienes comunales y demás bienes de dominio público son inalienables, inembargables e imprescriptibles y:",
  ["No están sujetos a tributo alguno.", "Están sujetos al Impuesto sobre Bienes Inmuebles.", "Pueden cederse en propiedad a los vecinos.", "Se rigen por el Derecho privado."],
  "Art. 80.1 LRBRL.", "no están sujetos a tributo alguno"),
 ("LRBRL", "Artículo 81", "Bienes comunales", "Según el artículo 81.2 de la Ley 7/1985, la alteración de la calificación jurídica de los bienes de las entidades locales se produce automáticamente en caso de adscripción de bienes patrimoniales a un uso o servicio públicos por más de:",
  ["Veinticinco años.", "Diez años.", "Veinte años.", "Treinta años."],
  "Art. 81.2 b) LRBRL.", "Adscripción de bienes patrimoniales por más de veinticinco años"),
 ("RD1372", "art2", "Bienes comunales", "Según el artículo 2.4 del Reglamento de Bienes de las Entidades Locales (Real Decreto 1372/1986), los bienes comunales sólo podrán pertenecer a:",
  ["Los Municipios y las Entidades locales menores.", "Los Municipios y las Provincias.", "Las Comunidades Autónomas.", "Las Comarcas y las Mancomunidades."],
  "Art. 2.4 RBEL.", "Los bienes comunales solo podrán pertenecer a los Municipios y a las Entidades locales menores"),
 ("RD1372", "art94", "Bienes comunales", "Según el artículo 94.1 del Reglamento de Bienes de las Entidades Locales, el aprovechamiento y disfrute de bienes comunales se efectuará precisamente en régimen de:",
  ["Explotación común o cultivo colectivo.", "Adjudicación mediante precio.", "Adjudicación por lotes o suertes.", "Concesión administrativa."],
  "Art. 94.1 RBEL; las demás formas son subsidiarias (94.2 y 3).", "se efectuará precisamente en régimen de explotación común o cultivo colectivo"),
 ("RD1372", "art98", "Bienes comunales", "Según el artículo 98.1 del Reglamento de Bienes de las Entidades Locales, la adjudicación mediante precio del aprovechamiento de bienes comunales habrá de ser autorizada por:",
  ["El órgano competente de la Comunidad Autónoma.", "El Pleno de la Corporación.", "El Delegado del Gobierno.", "El Ministerio de Hacienda."],
  "Art. 98.1 RBEL.", "habrá de ser autorizada por el órgano competente de la Comunidad Autónoma"),
 ("RD1372", "art102", "Bienes comunales", "Según el artículo 102 del Reglamento de Bienes de las Entidades Locales, la cesión por cualquier título del aprovechamiento de bienes comunales deberá ser acordada por el Pleno de la Corporación, requiriéndose:",
  ["El voto favorable de la mayoría absoluta del número legal de miembros.", "Mayoría simple.", "El voto favorable de dos tercios del número legal de miembros.", "Unanimidad."],
  "Art. 102 RBEL.", "requiriéndose el voto favorable de la mayoría absoluta del número legal de miembros"),
 ("RD1372", "art103", "Bienes comunales", "Según el artículo 103.1 del Reglamento de Bienes de las Entidades Locales, el derecho al aprovechamiento y disfrute de los bienes comunales:",
  ["Corresponderá simultáneamente a los vecinos sin distinción de sexo, estado civil o edad, y también a los extranjeros domiciliados en el término municipal.", "Corresponderá solo a los vecinos mayores de edad de nacionalidad española.", "Corresponderá solo a los cabezas de familia.", "Corresponderá a quien lo adquiera en subasta."],
  "Art. 103.1 RBEL.", "corresponderá simultáneamente a los vecinos sin distinción de sexo, estado civil o edad"),
]
for k, art, cat, q_, ops, e, fr in Q: T.q(k, art, cat, q_, ops, e, fr)
T.real("P", 69, "Constitución"); T.real("P", 70, "Patrimonio del Estado"); T.real("L", 55, "Prerrogativas")
T.real("X", 60, "Patrimonio Nacional"); T.real("X", 59, "Bienes comunales")

# Flashcards
for q_, a_, cat in [
  ("¿Qué manda el art. 132.1 CE?", "Que la ley regule el régimen de los bienes de dominio público y de los comunales, inspirándose en la inalienabilidad, imprescriptibilidad e inembargabilidad, así como su desafectación.", "Constitución"),
  ("Dominio público estatal «en todo caso» (art. 132.2 CE)", "Zona marítimo-terrestre, playas, mar territorial y recursos naturales de la zona económica y la plataforma continental.", "Constitución"),
  ("¿Cómo se regulan el Patrimonio del Estado y el Patrimonio Nacional? (art. 132.3 CE)", "Por ley (su administración, defensa y conservación).", "Constitución"),
  ("¿Qué no forma parte del patrimonio de las Administraciones? (art. 3.2 LPAP)", "El dinero, los valores, los créditos y los demás recursos financieros de su hacienda.", "Concepto y clases"),
  ("¿Quién gestiona los bienes del Patrimonio del Estado de titularidad de la AGE? (art. 9.2 LPAP)", "El Ministerio de Hacienda, a través de la Dirección General del Patrimonio del Estado.", "Patrimonio del Estado"),
  ("Las cuatro prerrogativas del art. 41 LPAP", "Investigar, deslindar (inmuebles), recuperar de oficio la posesión y desahuciar (inmuebles demaniales).", "Prerrogativas"),
  ("Deslinde de bienes patrimoniales de la AGE: órganos (art. 51.1 LPAP)", "Incoa el Director General del Patrimonio del Estado; instruyen los Delegados de Economía y Hacienda; resuelve el Ministro de Hacienda.", "Prerrogativas"),
  ("Plazo para resolver el deslinde (art. 52 e LPAP)", "18 meses desde el acuerdo de iniciación; si no, caducidad.", "Prerrogativas"),
  ("Plazo de la investigación (art. 47 e LPAP)", "Dos años desde el día siguiente a la publicación en el BOE; si no, archivo.", "Prerrogativas"),
  ("Recuperación de oficio: plazos (art. 55 LPAP)", "Demaniales: en cualquier tiempo. Patrimoniales: un año desde el día siguiente a la usurpación; después, vía civil.", "Prerrogativas"),
  ("Concepto de bien demanial (art. 5.1 LPAP)", "De titularidad pública y afectado al uso general o al servicio público, o declarado demanial por ley.", "Dominio público"),
  ("Desafectación: forma (art. 69.2 LPAP)", "Siempre expresa, salvo los supuestos previstos en la ley.", "Dominio público"),
  ("Mutación demanial (art. 71.1 LPAP)", "Desafectación de un bien con simultánea afectación a otro uso general, fin o servicio público.", "Dominio público"),
  ("Tres usos del dominio público (art. 85 LPAP)", "Común (todos por igual), aprovechamiento especial (sin impedir el común) y privativo (ocupa una porción y limita o excluye a otros).", "Uso del dominio público"),
  ("Autorización frente a concesión: plazos (arts. 92.3 y 93.3 LPAP)", "Autorización: máximo 4 años con prórrogas. Concesión: máximo 75 años con prórrogas.", "Uso del dominio público"),
  ("Bienes patrimoniales (art. 7.1 LPAP)", "Los de titularidad de las Administraciones que no tengan carácter demanial.", "Bienes patrimoniales"),
  ("Transacción y arbitraje sobre bienes del Patrimonio del Estado (art. 31 LPAP)", "Real decreto acordado en Consejo de Ministros, a propuesta del de Hacienda, previo dictamen del Consejo de Estado en pleno.", "Bienes patrimoniales"),
  ("Formas de enajenar inmuebles (art. 137.1 LPAP)", "Subasta, concurso o adjudicación directa.", "Bienes patrimoniales"),
  ("Bienes del Patrimonio Nacional (art. 2 Ley 23/1982)", "Los de titularidad del Estado afectados al uso y servicio del Rey y de los miembros de la Real Familia, más los derechos de patronato sobre los Reales Patronatos.", "Patrimonio Nacional"),
  ("¿De quién depende el Consejo de Administración del Patrimonio Nacional? (art. 1 Ley 23/1982)", "Orgánicamente, de la Presidencia del Gobierno.", "Patrimonio Nacional"),
  ("Norma supletoria del Patrimonio Nacional (LPAP, disposición adicional cuarta)", "La Ley 33/2003 y sus normas de desarrollo.", "Patrimonio Nacional"),
  ("Bienes comunales (art. 79.3 LRBRL; art. 2 RBEL)", "Bienes de dominio público local cuyo aprovechamiento corresponde al común de los vecinos; solo de municipios y entidades locales menores.", "Bienes comunales"),
  ("¿Cuándo pierden los comunales su carácter? (art. 100 RBEL)", "Si no se han disfrutado como tales durante más de diez años: acuerdo de la Corporación por mayoría absoluta, información pública y aprobación de la Comunidad Autónoma.", "Bienes comunales"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Dominio público (bienes demaniales)", "Bienes y derechos de titularidad pública afectados al uso general o al servicio público, o declarados demaniales por ley; inalienables, imprescriptibles e inembargables (arts. 5 y 30.1 LPAP).", "s7", "Dominio público")
T.glos("Bienes patrimoniales", "Bienes y derechos de las Administraciones públicas que no tienen carácter demanial (art. 7.1 LPAP); enajenables y prescriptibles (art. 30.2).", "s11", "Bienes patrimoniales")
T.glos("Patrimonio del Estado", "Patrimonio de la Administración General del Estado y de sus organismos públicos (art. 9.1 LPAP).", "s3", "Régimen patrimonial")
T.glos("Afectación", "Vinculación de un bien a un uso general o a un servicio público, con su integración en el dominio público (art. 65 LPAP).", "s8", "Dominio público")
T.glos("Desafectación", "Pérdida de la condición demanial por dejar de destinarse al uso general o al servicio público; el bien pasa a ser patrimonial. Debe ser expresa (art. 69 LPAP).", "s8", "Dominio público")
T.glos("Mutación demanial", "Desafectación de un bien con simultánea afectación a otro uso general, fin o servicio público (art. 71 LPAP).", "s8", "Dominio público")
T.glos("Uso privativo", "Uso que ocupa una porción del dominio público y limita o excluye su utilización por otros (art. 85.3 LPAP).", "s9", "Uso del dominio público")
T.glos("Concesión demanial", "Título para el uso privativo con obras o instalaciones fijas, o para usos de más de cuatro años; en concurrencia y por un máximo de 75 años (arts. 86 y 93 LPAP).", "s10", "Uso del dominio público")
T.glos("Deslinde", "Potestad de fijar los límites de los inmuebles de la Administración cuando son imprecisos o hay indicios de usurpación (art. 50 LPAP).", "s5", "Prerrogativas")
T.glos("Recuperación de oficio", "Potestad de recuperar por sí misma la posesión indebidamente perdida: en cualquier tiempo para los demaniales y en un año para los patrimoniales (art. 55 LPAP).", "s5", "Prerrogativas")
T.glos("Desahucio administrativo", "Potestad de recuperar la posesión de bienes demaniales cuando decae el título que legitimaba su ocupación por terceros (art. 58 LPAP).", "s5", "Prerrogativas")
T.glos("Patrimonio Nacional", "Bienes de titularidad del Estado afectados al uso y servicio del Rey y de la Real Familia, y derechos de patronato sobre los Reales Patronatos (Ley 23/1982, arts. 2 y 5).", "s13", "Patrimonio Nacional")
T.glos("Reales Patronatos", "Fundaciones sobre las que el Patrimonio Nacional ostenta derechos de patronato o de gobierno y administración (Ley 23/1982, art. 5).", "s13", "Patrimonio Nacional")
T.glos("Bienes comunales", "Bienes de dominio público local cuyo aprovechamiento corresponde al común de los vecinos; solo de municipios y entidades locales menores (art. 79.3 LRBRL; art. 2 RBEL).", "s15", "Bienes comunales")

# Cronología (fechas de los metadatos del BOE)
T.hito("1978", "Constitución Española (27-12-1978; BOE de 29-12-1978)", "Art. 132: dominio público, comunales, Patrimonio del Estado y Patrimonio Nacional", "normativo", "s1")
T.hito("1982", "Ley 23/1982, de 16 de junio, reguladora del Patrimonio Nacional (BOE de 22-6-1982)", "Régimen del Patrimonio Nacional y de su Consejo de Administración", "normativo", "s13")
T.hito("1985", "Ley 7/1985, de 2 de abril, Reguladora de las Bases del Régimen Local (BOE de 3-4-1985)", "Arts. 79 a 82: bienes de las entidades locales y comunales", "normativo", "s15")
T.hito("1986", "Real Decreto 1372/1986, de 13 de junio, Reglamento de Bienes de las Entidades Locales (BOE de 7-7-1986)", "Régimen de los bienes locales y aprovechamiento de los comunales", "normativo", "s16")
T.hito("2003", "Ley 33/2003, de 3 de noviembre, del Patrimonio de las Administraciones Públicas (BOE de 4-11-2003)", "Bases del régimen patrimonial; deroga la Ley del Patrimonio del Estado de 1964", "normativo", "s2")

T.publicar()
