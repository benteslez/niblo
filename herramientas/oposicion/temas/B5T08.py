# -*- coding: utf-8 -*-
"""Tema V.8 (B5T08): Negociación colectiva, representación y participación institucional
de los empleados públicos. El derecho de huelga y su ejercicio.
Método del I.2. Normas (textos consolidados del BOE): CE, arts. 7, 28, 37 y 103.3; TREBEP
(RDLeg 5/2015), arts. 15, 30.2, 31 a 46, 95.2 l) y m), disposición adicional duodécima y
transitoria quinta; LO 11/1985, de Libertad Sindical (arts. 1, 2, 6 y 7); Estatuto de los
Trabajadores (arts. 62 y 63); IV Convenio Único AGE (art. 85); Real Decreto-ley 17/1977
(título I, en lo vigente: las notas del texto consolidado del BOE sobre la STC 11/1981 se
comprueban contra el XML del BOE con nota())."""
import os, sys
import xml.etree.ElementTree as _ET
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *
import plantilla as _P

CORTO.update({"RDL17": "RDL 17/1977", "LOLS": "LO 11/1985, de Libertad Sindical", "CONV": "IV Convenio Único AGE", "ET": "Estatuto de los Trabajadores"})
URL_RDL17 = "https://www.boe.es/buscar/act.php?id=BOE-A-1977-6061"


def nota(k, bid, frag):
    """Cita de una NOTA del texto consolidado del BOE (no es texto legal: boe.py las excluye).
    Se comprueba que el fragmento está literal en las notas de la última versión del bloque."""
    raiz = _ET.parse(os.path.join(_P.AQUI, "boe", k + ".xml")).getroot()
    bs = [b for b in raiz.iter("bloque") if b.get("id") == bid]
    assert len(bs) == 1, (k, bid)
    v = bs[0].findall("version")[-1]
    txt = " ".join(" ".join(bq.itertext()) for bq in v.iter("blockquote"))
    assert _P._norm(frag) in _P._norm(txt), ("NOTA DEL BOE NO LITERAL", k, bid, frag)
    return "«" + frag + "»"


def aviso_tc(bid, frag):
    return f"?> **Nota del texto consolidado del BOE** [[BOE|{URL_RDL17}]] (no es texto legal; resume el fallo de la STC 11/1981): {nota('RDL17', bid, frag)}"


T = Tema("B5T08",
  "Cuatro preguntas: I. Qué derechos colectivos tienen los empleados públicos y en qué se apoyan (CE, arts. 7, 28.1 y 103.3; TREBEP, arts. 15, 31 y 32; LO 11/1985) · II. Cómo se negocian sus condiciones de trabajo (CE, art. 37.1; TREBEP, arts. 33 a 38 y 45 y disposición adicional duodécima) · III. Quién los representa (TREBEP, arts. 39 a 44 y 46 y disposición transitoria quinta; Estatuto de los Trabajadores, arts. 62 y 63; IV Convenio Único, art. 85) · IV. Cómo se ejerce el derecho de huelga (CE, arts. 28.2 y 37.2; RDL 17/1977; TREBEP, arts. 30.2 y 95.2). Cada artículo: texto literal del BOE y ficha.",
  ["Negociación colectiva", "Representación", "Participación institucional", "Libertad sindical", "Sindicatos más representativos", "Mesas de Negociación", "Art. 37 TREBEP", "Pactos y Acuerdos", "Delegados de Personal", "Juntas de Personal", "Cuatro años", "Derecho de reunión", "Huelga", "RDL 17/1977", "STC 11/1981", "Servicios esenciales"])

# =============================================================================
T.ap("s0", "Mapa del tema: cuatro preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque V, tema 8):
> Negociación colectiva, representación y participación institucional de los empleados públicos. El derecho de huelga y su ejercicio.

### El hilo conductor

El epígrafe se lee como **cuatro preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Constitución | Otras normas |
|---|---|---|---|
| **I** | ¿Qué derechos colectivos tienen los empleados públicos y en qué se apoyan? (negociación, representación y participación institucional) | Arts. 7, 28.1 y 103.3 | TREBEP, arts. 15, 31 y 32; LO 11/1985, de Libertad Sindical, arts. 1, 2, 6 y 7 |
| **II** | ¿Cómo se negocian las condiciones de trabajo? (negociación colectiva) | Art. 37.1 | TREBEP, arts. 33 a 38 y 45; disposición adicional duodécima |
| **III** | ¿Quién representa a los empleados públicos? (representación unitaria y reunión) | — | TREBEP, arts. 39 a 44 y 46; disposición transitoria quinta; Estatuto de los Trabajadores, arts. 62 y 63; IV Convenio Único, art. 85 |
| **IV** | ¿Cómo se ejerce el derecho de huelga? | Arts. 28.2 y 37.2 | Real Decreto-ley 17/1977, arts. 1 a 11 (en lo vigente); TREBEP, arts. 30.2 y 95.2 k) a m) |

!> **La idea que une los cuatro bloques:** los empleados públicos tienen derechos individuales que **se ejercen de forma colectiva** (TREBEP, art. 15): libertad sindical, negociación colectiva, huelga, conflictos colectivos y reunión (I). Los sindicatos **negocian** en Mesas y firman **Pactos y Acuerdos** (II); los empleados **eligen** a sus representantes unitarios: Delegados y Juntas de Personal, o Delegados de personal y Comités de empresa si son laborales (III); y el último recurso es la **huelga**, con la garantía de los **servicios esenciales** (IV).

?> **Aviso de vigencia (huelga)** [[BOE|{URL_RDL17}]]. El Real Decreto-ley 17/1977 sigue vigente, pero, según las notas de su texto consolidado, la STC 11/1981 declaró inconstitucionales algunos incisos de sus artículos 3, 5, 6, 10 y 11. Aquí se cita **solo lo vigente** y, donde hay inciso anulado, se reproduce la **nota del BOE** (→ IV.2).

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha**: de **derecho** (Titulares · Contenido · Límites · Protección · ⚠ Ojo en el examen) o de **institución o procedimiento** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Los esquemas y cuadros **no son texto legal**: resumen los artículos citados.
- Lo que corresponde a otros temas se remite: derechos y régimen disciplinario (tema V.2), retribuciones (tema V.6), personal laboral y IV Convenio Único (tema V.7).
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué derechos colectivos tienen los empleados públicos y en qué se apoyan?", donde(
  "Primera pregunta del tema. Antes de ver cómo se negocia, quién representa y cómo se hace huelga, hay que saber **qué derechos colectivos** reconocen la Constitución y el TREBEP a los empleados públicos, qué significan **negociación, representación y participación institucional**, y qué papel tienen los **sindicatos**.",
  ["1 Fundamento constitucional (CE, arts. 7, 28.1 y 103.3)", "2 Derechos individuales ejercidos colectivamente (TREBEP, art. 15)", "3 Negociación, representación y participación institucional: conceptos (TREBEP, arts. 31 y 32)", "4 Libertad sindical y sindicatos más representativos (LO 11/1985, arts. 1, 2, 6 y 7)"]))

T.ap("s1", "I.1 Fundamento constitucional (CE, arts. 7, 28.1 y 103.3)", f"""
{unidad("1.1 Los sindicatos (art. 7)",
  lit("CE", "Artículo 7", ["contribuyen a la defensa y promoción de los intereses económicos y sociales que les son propios", "Su estructura interna y funcionamiento deberán ser democráticos"]),
  fichab("Reconocimiento constitucional de los sindicatos (y de las asociaciones empresariales)",
         c("CE", "Artículo 7", "Los sindicatos de trabajadores y las asociaciones empresariales"),
         f"Su creación y su actividad {c('CE', 'Artículo 7', 'son libres dentro del respeto a la Constitución y a la ley')}",
         "—",
         "Está en el **Título preliminar**. Exige estructura interna y funcionamiento **democráticos**."))}

{unidad("1.2 Libertad sindical (art. 28.1)",
  lit("CE", "Artículo 28", ["Todos tienen derecho a sindicarse libremente", "regulará las peculiaridades de su ejercicio para los funcionarios públicos", "Nadie podrá ser obligado a afiliarse a un sindicato"], solo=[1]),
  ficha(c("CE", "Artículo 28", "Todos"),
        ["::La libertad sindical comprende:", "Fundar sindicatos y afiliarse al de su elección", "Que los sindicatos formen confederaciones y funden organizaciones sindicales internacionales o se afilien a ellas", "Libertad negativa: nadie puede ser obligado a afiliarse"],
        ["La ley puede **limitar o exceptuar** el derecho a las Fuerzas o Institutos armados y demás Cuerpos sometidos a disciplina militar", "La ley **regula las peculiaridades** de su ejercicio para los **funcionarios públicos**"],
        "Es derecho fundamental (Sección 1.ª del Capítulo segundo del Título I); su desarrollo es la LO 11/1985 (→ I.4)",
        "Para los **militares**, la ley puede **limitar o exceptuar**; para los **funcionarios**, solo **regula peculiaridades**."))}

{unidad("1.3 El estatuto de los funcionarios y su sindicación (art. 103.3)",
  lit("CE", "Artículo 103", ["las peculiaridades del ejercicio de su derecho a sindicación"], solo=[3]),
  fichab("Reserva de ley del estatuto de los funcionarios, que incluye las peculiaridades de su sindicación",
         "Las Cortes, por ley",
         "La ley regula el estatuto de los funcionarios y, entre otras cosas, las peculiaridades del ejercicio de su derecho a sindicación",
         "—",
         "Concuerda con el art. 28.1: la sindicación de los funcionarios tiene **peculiaridades**, reguladas por ley."))}
""", 2)

T.ap("s2", "I.2 Derechos individuales ejercidos colectivamente (TREBEP, art. 15)", f"""
Los derechos de los empleados públicos se estudian en el tema V.2. Aquí interesa el art. 15, porque **enumera los derechos de este tema**.

{unidad("2.1 La lista del art. 15",
  lit("TREBEP", "Artículo 15", ["derechos individuales que se ejercen de forma colectiva", "A la libertad sindical", "con la garantía del mantenimiento de los servicios esenciales de la comunidad"]),
  ficha(c("TREBEP", "Artículo 15", "Los empleados públicos"),
        ["::Cinco derechos:", "a) Libertad sindical", "b) Negociación colectiva y participación en la determinación de las condiciones de trabajo (→ II.1)", "c) Huelga, con la garantía de los servicios esenciales (→ IV.1)", "d) Planteamiento de conflictos colectivos de trabajo", "e) Reunión, en los términos del art. 46 (→ III.4)"],
        "Huelga: con la garantía del mantenimiento de los **servicios esenciales de la comunidad**; conflictos colectivos: de acuerdo con la legislación aplicable en cada caso",
        "—",
        "Son derechos **individuales** que se **ejercen de forma colectiva**. La **libre asociación profesional** no está aquí: es un derecho **individual** del art. 14 (pregunta oficial X 68, → Cierre 1)."))}
""", 2)

T.ap("s3", "I.3 Negociación, representación y participación institucional: conceptos (TREBEP, arts. 31 y 32)", f"""
{unidad("3.1 Las tres definiciones legales (art. 31.1 a 4)",
  lit("TREBEP", "Artículo 31", ["derecho a la negociación colectiva, representación y participación institucional", "el derecho a negociar la determinación de condiciones de trabajo", "la facultad de elegir representantes y constituir órganos unitarios", "a través de las organizaciones sindicales, en los órganos de control y seguimiento"], solo=[1, 2, 3, 4]),
  ficha(c("TREBEP", "Artículo 31", "Los empleados públicos"),
        ["::Tres derechos para determinar sus condiciones de trabajo:", "**Negociación colectiva**: negociar la determinación de condiciones de trabajo (31.2; → II)", "**Representación**: elegir representantes y constituir **órganos unitarios** para la interlocución con la Administración (31.3; → III)", "**Participación institucional**: participar, **a través de las organizaciones sindicales**, en los órganos de **control y seguimiento** de las entidades u organismos que legalmente se determine (31.4)"],
        "—",
        "—",
        "La participación institucional se ejerce **a través de los sindicatos**, no de los órganos unitarios; la representación es la que se ejerce mediante **órganos unitarios**."))}

{unidad("3.2 Garantía, legitimación y límites (art. 31.5 a 8)",
  lit("TREBEP", "Artículo 31", ["a través de los órganos y sistemas específicos regulados en el presente capítulo", "están legitimadas para la interposición de recursos en vía administrativa y jurisdiccional contra las resoluciones de los órganos de selección", "convenios y acuerdos de carácter internacional ratificados por España"], solo=[5, 6, 7, 8]),
  fichab("Cómo se garantizan estos derechos y quién puede recurrir los procesos selectivos",
         f"{c('TREBEP', 'Artículo 31', 'Las organizaciones sindicales más representativas en el ámbito de la Función Pública')} (legitimación para recurrir)",
         ["Por los órganos y sistemas específicos del capítulo, sin perjuicio de otras formas de colaboración (31.5)", "Respetando el Estatuto y sus leyes de desarrollo (31.7)", "Teniendo en cuenta los convenios y acuerdos internacionales ratificados por España (31.8)"],
         "—",
         "Pueden recurrir **en vía administrativa y jurisdiccional** las resoluciones de los **órganos de selección** solo las organizaciones sindicales **más representativas** en el ámbito de la Función Pública."))}

{unidad("3.3 Personal laboral (art. 32)",
  lit("TREBEP", "Artículo 32", ["se regirá por la legislación laboral", "por causa grave de interés público derivada de una alteración sustancial de las circunstancias económicas", "deberán informar a las organizaciones sindicales"]),
  fichab("Régimen de la negociación, representación y participación del personal laboral",
         "Empleados públicos con contrato laboral; órganos de gobierno de las Administraciones Públicas (suspensión o modificación)",
         ["Legislación **laboral**, sin perjuicio de los preceptos del capítulo que les son aplicables expresamente", "Se garantiza el cumplimiento de convenios y acuerdos, salvo suspensión o modificación excepcional"],
         f"Suspensión o modificación solo {c('TREBEP', 'Artículo 32', 'en la medida estrictamente necesaria para salvaguardar el interés público')}",
         "La excepción exige causa grave de interés público derivada de una **alteración sustancial de las circunstancias económicas**, y obliga a **informar** a los sindicatos (es la misma cláusula que la del art. 38.10 para Pactos y Acuerdos, → II.4.3)."))}
""", 2)

T.ap("s4", "I.4 Libertad sindical y sindicatos más representativos (LO 11/1985, arts. 1, 2, 6 y 7)", f"""
La Ley Orgánica 11/1985, de Libertad Sindical, desarrolla el art. 28.1 CE. El TREBEP se remite a sus arts. 6 y 7 para saber qué sindicatos negocian (art. 33.1), promueven elecciones (art. 43) o se sientan en las Mesas (art. 36).

{unidad("4.1 Quién tiene libertad sindical (art. 1)",
  lit("LOLS", "Artículo primero", ["de carácter administrativo o estatutario al servicio de las Administraciones públicas", "los miembros de las Fuerzas Armadas y de los Institutos Armados de carácter militar", "no podrán pertenecer a sindicato alguno mientras se hallen en activo", "se regirá por su normativa específica"], titulo="Artículo 1 (LO 11/1985, de Libertad Sindical)"),
  ficha(["::Todos los trabajadores (1.1); incluye a los sujetos de una relación:", "Laboral", "Administrativa o estatutaria al servicio de las Administraciones públicas (1.2)"],
        c("LOLS", "Artículo primero", "sindicarse libremente para la promoción y defensa de sus intereses económicos y sociales"),
        ["**Excluidos**: miembros de las Fuerzas Armadas y de los Institutos Armados de carácter militar (1.3)", "Jueces, Magistrados y Fiscales: no pueden pertenecer a sindicato **mientras estén en activo** (1.4)", "Cuerpos y Fuerzas de Seguridad sin carácter militar: su **normativa específica** (1.5)"],
        "—",
        "Los **funcionarios** son «trabajadores» a efectos de esta ley (1.2). Militares: **exceptuados**; jueces en activo: **no pueden afiliarse**; policías civiles: **normativa específica**."))}

{unidad("4.2 Contenido de la libertad sindical (art. 2)",
  lit("LOLS", "Artículo segundo", ["sin autorización previa", "no pudiendo nadie ser obligado a afiliarse a un sindicato", "sino mediante resolución firme de la Autoridad Judicial", "el derecho a la negociación colectiva, al ejercicio del derecho de huelga"], titulo="Artículo 2 (LO 11/1985, de Libertad Sindical)"),
  ficha(["::Individual (2.1) y colectiva (2.2):", "Trabajadores: fundar sindicatos, afiliarse o separarse, elegir representantes, actividad sindical", "Sindicatos: estatutos, federarse, no ser suspendidos ni disueltos sin resolución judicial firme, actividad sindical"],
        ["::La actividad sindical comprende en todo caso (2.2 d):", "Negociación colectiva", "Huelga", "Conflictos individuales y colectivos", "Presentar candidaturas a Comités de Empresa, Delegados de Personal y órganos de las Administraciones Públicas"],
        "Suspensión o disolución de un sindicato: solo por **resolución firme de la Autoridad Judicial**, fundada en incumplimiento grave de las Leyes",
        "—",
        "Fundar sindicatos **sin autorización previa**. La huelga y la negociación colectiva forman parte de la **actividad sindical** (2.2 d)."))}

{unidad("4.3 Sindicatos más representativos a nivel estatal y participación institucional (art. 6)",
  lit("LOLS", "Artículo sexto", ["tanto de participación institucional como de acción sindical", "del 10 por 100 o más del total de delegados de personal", "Ostentar representación institucional ante las Administraciones públicas", "Participar como interlocutores en la determinación de las condiciones de trabajo en las Administraciones públicas"], titulo="Artículo 6 (LO 11/1985, de Libertad Sindical)"),
  fichab("La mayor representatividad sindical y lo que permite",
         ["::Más representativos a nivel estatal (6.2):", "Los que obtengan en ese ámbito el **10 por 100 o más** del total de delegados de personal, miembros de comités de empresa y órganos correspondientes de las Administraciones públicas", "Los afiliados, federados o confederados a una organización estatal más representativa"],
         ["::Capacidad representativa a todos los niveles (6.3), entre otras:", "a) **Representación institucional** ante las Administraciones públicas", "c) Interlocución en la determinación de las condiciones de trabajo en las Administraciones públicas", "d) Sistemas no jurisdiccionales de solución de conflictos", "e) Promover elecciones"],
         "Estatal: **10 por 100**",
         "La mayor representatividad da una posición singular **tanto de participación institucional como de acción sindical** (6.1). La **participación institucional** del art. 31.4 TREBEP se ejerce **a través de las organizaciones sindicales**; ostentar **representación institucional** ante las Administraciones públicas es una facultad de los más representativos (6.3 a y 7.1)."))}

{unidad("4.4 Más representativos de Comunidad Autónoma y sindicatos con el 10 por 100 en un ámbito (art. 7)",
  lit("LOLS", "Artículo séptimo", ["al menos, el 15 por 100 de los delegados de personal", "siempre que cuenten con un mínimo de 1.500 representantes", "el 10 por 100 o más de delegados de personal y miembros de comité de empresa"], titulo="Artículo 7 (LO 11/1985, de Libertad Sindical)"),
  fichab("Otros dos niveles de representatividad",
         ["Más representativos de Comunidad Autónoma (7.1)", "Sindicatos con el 10 por 100 en un ámbito territorial y funcional específico (7.2)"],
         ["CA: funciones del 6.3 en su ámbito y representación institucional ante entidades de carácter estatal", "10 por 100 en un ámbito: funciones de las letras b), c), d), e) y g) del 6.3 en ese ámbito"],
         ["Comunidad Autónoma: **al menos el 15 por 100** y **mínimo de 1.500 representantes**, sin estar federados con organizaciones estatales", "Ámbito específico: **10 por 100 o más**"],
         "Tres cifras: **10 %** estatal (art. 6), **15 %** y **1.500** autonómico (art. 7.1), **10 %** en un ámbito concreto (art. 7.2). El sindicato del 7.2 **no** tiene la letra a) (representación institucional)."))}

{resumen([
  "CE: sindicatos con estructura **democrática** (7); **libertad sindical** de todos, con límites o excepciones para los cuerpos militares y **peculiaridades** para los funcionarios (28.1 y 103.3).",
  "TREBEP, art. 15: cinco derechos **individuales ejercidos colectivamente**: libertad sindical, negociación colectiva, huelga, conflictos colectivos y reunión.",
  "Art. 31: **negociación** (negociar condiciones), **representación** (órganos unitarios) y **participación institucional** (a través de los sindicatos, en órganos de control y seguimiento). El personal laboral, por la **legislación laboral** (32).",
  "LO 11/1985: los funcionarios son trabajadores a sus efectos; más representativos: **10 %** estatal, **15 %** y **1.500** autonómico."],
  "Siguiente: II. ¿Cómo se negocian las condiciones de trabajo? La negociación colectiva")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Cómo se negocian las condiciones de trabajo? La negociación colectiva (CE, art. 37.1; TREBEP, arts. 33 a 38 y 45 y DA 12.ª)", donde(
  "Segunda pregunta. La Constitución garantiza la negociación colectiva **laboral** (art. 37.1); para los funcionarios, el TREBEP regula **principios**, **Mesas de Negociación**, **materias** y el resultado: **Pactos y Acuerdos**.",
  ["1 Fundamento y principios: quién negocia (CE, art. 37.1; TREBEP, art. 33)", "2 Las Mesas de Negociación (arts. 34 a 36 y disposición adicional duodécima)", "3 Materias negociables y excluidas (art. 37)", "4 Pactos y Acuerdos (art. 38)", "5 Solución extrajudicial de conflictos (art. 45)"]))

T.ap("s5", "II.1 Fundamento y principios: quién negocia (CE, art. 37.1; TREBEP, art. 33)", f"""
{unidad("1.1 La negociación colectiva laboral en la Constitución (art. 37.1)",
  lit("CE", "Artículo 37", ["la fuerza vinculante de los convenios"], solo=[1]),
  ficha("Los representantes de los trabajadores y los empresarios",
        "Derecho a la negociación colectiva **laboral** y fuerza vinculante de los convenios",
        "—",
        c("CE", "Artículo 37", "La ley garantizará"),
        "Está en la **Sección 2.ª** del Capítulo segundo (no es la Sección 1.ª). Para los funcionarios, la negociación la regula el TREBEP (→ II.1.2)."))}

{unidad("1.2 Principios, Mesas y legitimación (art. 33)",
  lit("TREBEP", "Artículo 33", ["legalidad, cobertura presupuestaria, obligatoriedad, buena fe negocial, publicidad y transparencia", "el 10 por 100 o más de los representantes", "de naturaleza estrictamente técnica"]),
  fichab("La negociación colectiva de condiciones de trabajo de los funcionarios",
         ["::En las Mesas de Negociación están legitimados:", "Los representantes de la Administración Pública correspondiente", "Las organizaciones sindicales más representativas a nivel **estatal**", "Las más representativas de **comunidad autónoma**", "Los sindicatos con el **10 por 100 o más** de los representantes en las elecciones a Delegados y Juntas de Personal del ámbito"],
         ["::Seis principios (33.1):", "Legalidad", "Cobertura presupuestaria", "Obligatoriedad", "Buena fe negocial", "Publicidad", "Transparencia", "La Administración puede encargarla a órganos **estrictamente técnicos**, con ratificación de los acuerdos por el órgano competente (33.2)"],
         "Sindicatos: **10 por 100** de los representantes en el ámbito",
         "Seis principios: **legalidad, cobertura presupuestaria, obligatoriedad, buena fe negocial, publicidad y transparencia** (no «gratuidad» ni «confidencialidad»)."))}
""", 2)

T.ap("s6", "II.2 Las Mesas de Negociación (arts. 34 a 36 y disposición adicional duodécima)", f"""
{unidad("2.1 Mesas Generales y Sectoriales (art. 34)",
  lit("TREBEP", "Artículo 34", ["se constituirá una Mesa General de Negociación en el ámbito de la Administración General del Estado", "condiciones de trabajo comunes a los funcionarios de su ámbito", "podrán constituirse Mesas Sectoriales", "en el plazo máximo de un mes", "bajo el principio de la buena fe"]),
  fichab("Mesas de negociación de los funcionarios",
         ["Mesa General: en la AGE, en cada Comunidad Autónoma, en Ceuta y Melilla y en las Entidades Locales (34.1)", "Legitimación negocial de las asociaciones de municipios y de las Entidades Locales supramunicipales (34.2)", "Mesas Sectoriales: dependen de las Generales y se crean **por acuerdo** de ellas (34.4)"],
         ["Mesa General: materias de condiciones de trabajo **comunes** a los funcionarios de su ámbito (34.3)", "Sectorial: temas comunes del sector **no decididos** por la Mesa General o que esta le **reenvíe o delegue** (34.5)", "Buena fe e información mutua (34.7)"],
         "Apertura: en la fecha de común acuerdo; si no, en el **plazo máximo de un mes** desde que lo promueva la mayoría de una de las partes (34.6)",
         "Las Sectoriales **dependen** de las Generales y se constituyen **por acuerdo** de estas. Plazo para abrir la negociación sin acuerdo: **un mes**."))}

{unidad("2.2 Constitución y composición (art. 35)",
  lit("TREBEP", "Artículo 35", ["como mínimo, la mayoría absoluta de los miembros de los órganos unitarios de representación", "cada dos años", "con voz, pero sin voto", "sin que ninguna de las partes pueda superar el número de quince miembros"]),
  fichab("Cuándo queda válidamente constituida una Mesa",
         "La Administración y las organizaciones sindicales legitimadas, en proporción a su representatividad",
         ["Válida constitución: los sindicatos deben representar **como mínimo la mayoría absoluta** de los miembros de los órganos unitarios del ámbito (35.1)", "Los componentes los designan las partes; asesores con **voz pero sin voto** (35.3)"],
         ["Variaciones de representatividad: acreditadas **cada dos años** con certificado de la Oficina Pública de Registro (35.2)", "Máximo **quince** miembros por cada parte (35.4)"],
         "**Mayoría absoluta** de los órganos unitarios; **cada dos años**; **quince** miembros por parte; asesores **sin voto**."))}

{unidad("2.3 Mesa General de las Administraciones Públicas y Mesas Generales de cada Administración (art. 36)",
  lit("TREBEP", "Artículo 36", ["estará presidida por la Administración General del Estado", "el incremento global de las retribuciones del personal al servicio de las Administraciones Públicas", "comunes al personal funcionario, estatutario y laboral", "siempre que hubieran obtenido el 10 por 100"]),
  fichab("Dos clases de Mesas Generales del art. 36",
         ["::Mesa General de Negociación de las **Administraciones Públicas** (36.1):", "Representación unitaria de las Administraciones, **presidida por la AGE**, con representantes de las CC. AA., Ceuta y Melilla y la **FEMP**", "Sindicatos legitimados (LO 11/1985, arts. 6 y 7), según los resultados electorales en el conjunto de las Administraciones Públicas", "Además, Mesas Generales de **cada Administración** para personal **funcionario, estatutario y laboral** (36.3)"],
         ["Mesa de las AA. PP.: materias del art. 37 susceptibles de regulación estatal con carácter de **norma básica** (36.2)", "Específicamente: el **incremento global de las retribuciones** que deba incluirse en el Proyecto de Ley de Presupuestos Generales del Estado de cada año"],
         "Presencia en las Mesas Generales de cada Administración de los sindicatos de la Mesa de las AA. PP. con el **10 por 100** de los representantes en ese ámbito (36.3)",
         "No confundir la Mesa General **de los funcionarios** de la AGE (art. 34.1) con la Mesa General **común** a funcionarios, estatutarios y laborales (art. 36.3) ni con la de **las Administraciones Públicas** (36.1), que negocia el **incremento global** de retribuciones."))}

{unidad("2.4 Mesas en ámbitos específicos (disposición adicional duodécima)",
  lit("TREBEP", "daduodecima", ["Del personal docente no universitario", "Del personal de la Administración de Justicia", "Del personal estatutario de los servicios de Salud", "Ámbito de Negociación"], solo=[1, 2, 3, 4, 5], titulo="Disposición adicional duodécima. Mesas de negociación en ámbitos específicos (TREBEP)"),
  fichab("Tres Mesas estatales para colectivos con régimen propio",
         "La Administración General del Estado y los sindicatos del art. 33.1, párrafo segundo, según los resultados electorales del ámbito considerados a nivel estatal",
         ["Docente no universitario", "Administración de Justicia", "Estatutario de los servicios de Salud: «Ámbito de Negociación»"],
         "—",
         "La del personal estatutario de los servicios de Salud se denomina **«Ámbito de Negociación»**."))}
""", 2)

T.ap("s7", "II.3 Materias negociables y excluidas (art. 37)", f"""
Es el artículo que **más cae** de este tema: dos preguntas oficiales de 2025 piden reconocer una materia **excluida** (→ Cierre 1).

{unidad("3.1 Materias objeto de negociación (art. 37.1) y excluidas (art. 37.2)",
  lit("TREBEP", "Artículo 37", ["Serán objeto de negociación", "La determinación y aplicación de las retribuciones complementarias de los funcionarios", "Los criterios generales sobre ofertas de empleo público", "Quedan excluidas de la obligatoriedad de la negociación", "La regulación del ejercicio de los derechos de los ciudadanos y de los usuarios de los servicios públicos", "La regulación y determinación concreta, en cada caso, de los sistemas, criterios, órganos y procedimientos de acceso al empleo público y la promoción profesional"]),
  fichab("Qué se negocia obligatoriamente y qué no",
         "Cada Administración, en su ámbito y competencias, con los sindicatos legitimados",
         ["::Negociables (37.1), trece letras; entre ellas:", "a) Aplicación del incremento de retribuciones de las Leyes de Presupuestos", "b) Retribuciones complementarias", "c) Criterios generales de acceso, carrera, provisión, clasificación de puestos y planificación", "d) Criterios y mecanismos generales de evaluación del desempeño", "g) Criterios generales de prestaciones sociales y pensiones de clases pasivas", "l) Criterios generales sobre ofertas de empleo público", "m) Calendario laboral, horarios, jornadas, vacaciones, permisos, movilidad"],
         ["::Excluidas de la obligatoriedad (37.2):", "a) Potestades de organización (pero se negocian sus consecuencias sobre condiciones de trabajo)", "b) Regulación de los derechos de los ciudadanos y usuarios y procedimiento de formación de actos y disposiciones", "c) Condiciones de trabajo del personal directivo", "d) Poderes de dirección y control de la relación jerárquica", "e) Regulación y determinación **concreta** de sistemas, criterios, órganos y procedimientos de **acceso** y promoción profesional"],
         "La clave: los **criterios generales** (de acceso, de OEP, de formación…) se negocian; la regulación y determinación **concreta, en cada caso**, del acceso y la promoción, **no** (pregunta oficial L 76). La regulación de los **derechos de los ciudadanos** y el **procedimiento** de formación de actos y disposiciones, tampoco (pregunta oficial X 84)."))}
""", 2)

T.ap("s8", "II.4 Pactos y Acuerdos (art. 38)", f"""
{unidad("4.1 Pactos y Acuerdos: diferencias (art. 38.1 a 3)",
  lit("TREBEP", "Artículo 38", ["Los Pactos se celebrarán sobre materias que se correspondan estrictamente con el ámbito competencial del órgano administrativo que lo suscriba", "Los Acuerdos versarán sobre materias competencia de los órganos de gobierno", "su aprobación expresa y formal", "su contenido carecerá de eficacia directa", "en el plazo de un mes"], solo=[1, 2, 3, 4, 5]),
  fichab("Los dos instrumentos que resultan de la negociación",
         "Los representantes de las Administraciones y la representación de las organizaciones sindicales legitimadas, **en el seno de las Mesas**",
         ["**Pactos**: materias del ámbito competencial del **órgano administrativo** que los suscribe; se aplican **directamente** (38.2)", "**Acuerdos**: materias de los **órganos de gobierno**; necesitan **aprobación expresa y formal** de estos (38.3)", "Acuerdo ratificado en materia con **reserva de ley**: **sin eficacia directa**; el órgano de gobierno con iniciativa legislativa remite el proyecto de ley"],
         "Falta de ratificación o negativa a incorporar lo acordado al proyecto de ley: renegociación en el plazo de **un mes**, si lo pide al menos la mayoría de una de las partes",
         "**Pacto** = órgano administrativo, aplicación directa. **Acuerdo** = órgano de gobierno, **ratificación** expresa y formal; si hay reserva de ley, no tiene eficacia directa."))}

{unidad("4.2 Contenido, seguimiento, publicación y falta de acuerdo (art. 38.4 a 9)",
  lit("TREBEP", "Artículo 38", ["el ámbito personal, funcional, territorial y temporal", "Comisiones Paritarias de seguimiento", "ordenará su publicación en el Boletín Oficial que corresponda", "corresponderá a los órganos de gobierno de las Administraciones Públicas establecer las condiciones de trabajo de los funcionarios", "en el artículo 83 del Estatuto de los Trabajadores"], solo=[6, 7, 8, 9, 10, 11]),
  fichab("Qué deben contener y qué pasa si no hay acuerdo",
         ["Las partes (contenido y Comisiones Paritarias)", "La Oficina Pública que determine cada Administración y la Autoridad respectiva (publicación)", "Los órganos de gobierno (si no hay acuerdo)"],
         ["Contenido mínimo: partes, ámbito **personal, funcional, territorial y temporal**, forma, plazo de preaviso y condiciones de denuncia (38.4)", "**Comisiones Paritarias de seguimiento** (38.5)", "Remisión a la Oficina Pública y publicación en el Boletín Oficial que corresponda (38.6)", "Sin acuerdo, y agotados en su caso los procedimientos extrajudiciales: los **órganos de gobierno** fijan las condiciones (38.7)", "Pactos y Acuerdos comunes a funcionarios y laborales: para los laborales, efectos del **art. 83 del Estatuto de los Trabajadores** (38.8)"],
         "—",
         "Si no hay acuerdo, **no** decide un árbitro obligatorio: establecen las condiciones los **órganos de gobierno** (38.7)."))}

{unidad("4.3 Cumplimiento, prórroga, vigencia y sucesión (art. 38.10 a 13)",
  lit("TREBEP", "Artículo 38", ["por causa grave de interés público derivada de una alteración sustancial de las circunstancias económicas", "se prorrogarán de año en año si no mediara denuncia expresa", "los derogan en su integridad"], solo=[12, 13, 14, 15, 16]),
  fichab("Vida de los Pactos y Acuerdos",
         "Los órganos de gobierno (suspensión o modificación excepcional); las partes",
         ["Cumplimiento garantizado, salvo suspensión o modificación excepcional, informando a los sindicatos de las causas (38.10)", "Prórroga **de año en año** salvo denuncia expresa, salvo acuerdo en contrario (38.11)", "Vigencia tras su duración: la que hayan establecido (38.12)", "Los que suceden a otros anteriores los derogan **en su integridad**, salvo lo que se acuerde mantener (38.13)"],
         "Prórroga: **de año en año**",
         "La suspensión exige **causa grave de interés público** por **alteración sustancial de las circunstancias económicas**, y solo **en la medida estrictamente necesaria**."))}
""", 2)

T.ap("s9", "II.5 Solución extrajudicial de conflictos colectivos (art. 45)", f"""
{unidad("5.1 Mediación y arbitraje (art. 45)",
  lit("TREBEP", "Artículo 45", ["podrán acordar la creación, configuración y desarrollo de sistemas de solución extrajudicial de conflictos colectivos", "excepto para aquellas en que exista reserva de ley", "La mediación será obligatoria cuando lo solicite una de las partes", "comprometiéndose de antemano a aceptar el contenido de la misma", "tendrá la misma eficacia jurídica y tramitación de los Pactos y Acuerdos", "Estos acuerdos serán susceptibles de impugnación"]),
  fichab("Sistemas de solución extrajudicial de conflictos colectivos",
         "Las Administraciones Públicas y las organizaciones sindicales del capítulo (los acuerdan)",
         ["Conflictos de negociación, aplicación e interpretación de Pactos y Acuerdos sobre materias del art. 37, **salvo** las de **reserva de ley** (45.2)", "**Mediación**: obligatoria si la pide **una** de las partes; sus propuestas pueden aceptarse o rechazarse libremente (45.3)", "**Arbitraje**: **voluntario**; las partes se comprometen de antemano a aceptar la resolución (45.3)", "El acuerdo de mediación o el laudo tienen la misma eficacia que los Pactos y Acuerdos, si las partes estaban legitimadas (45.4)"],
         "—",
         "Mediación **obligatoria** a petición de una parte, pero su propuesta **no vincula**; el arbitraje es **voluntario**, pero su resolución **sí** vincula. Nunca en materias con **reserva de ley**."))}

{resumen([
  "Principios (33.1): **legalidad, cobertura presupuestaria, obligatoriedad, buena fe negocial, publicidad y transparencia**; negocian los sindicatos más representativos estatales y de CA y los que tengan el **10 %** en el ámbito.",
  "Mesas: General en la AGE, CC. AA., Ceuta y Melilla y EE. LL. (34); Sectoriales **por acuerdo** de las Generales; válida constitución con la **mayoría absoluta** de los órganos unitarios; máximo **15** por parte (35).",
  "Mesa General de las **AA. PP.**: presidida por la AGE, con la FEMP; negocia el **incremento global** de retribuciones (36).",
  "Excluidas (37.2): potestades de organización, derechos de los ciudadanos y procedimiento, personal directivo, poderes de dirección y la regulación **concreta** del acceso y la promoción.",
  "**Pactos** (órgano administrativo, aplicación directa) y **Acuerdos** (órganos de gobierno, ratificación); prórroga **de año en año** (38). Mediación y arbitraje, nunca en materias con reserva de ley (45)."],
  "Siguiente: III. ¿Quién representa a los empleados públicos? Representación unitaria y reunión")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Quién representa a los empleados públicos? Representación unitaria y reunión (TREBEP, arts. 39 a 44 y 46 y DT 5.ª; ET, arts. 62 y 63; IV Convenio Único, art. 85)", donde(
  "Tercera pregunta. La **representación** es la facultad de elegir representantes y constituir **órganos unitarios** (art. 31.3, → I.3.1). Para los funcionarios son los **Delegados** y las **Juntas de Personal**; para el personal laboral, los **Delegados de personal** y los **Comités de empresa**.",
  ["1 Órganos de representación (TREBEP, art. 39; ET, arts. 62 y 63; IV Convenio Único, art. 85)", "2 Funciones, legitimación y garantías (arts. 40 y 41)", "3 Mandato, promoción de elecciones y procedimiento electoral (arts. 42 a 44 y disposición transitoria quinta)", "4 Derecho de reunión (art. 46)"]))

T.ap("s10", "III.1 Órganos de representación (TREBEP, art. 39; ET, arts. 62 y 63; IV Convenio Único, art. 85)", f"""
{unidad("1.1 Delegados de Personal y Juntas de Personal (art. 39)",
  lit("TREBEP", "Artículo 39", ["son los Delegados de Personal y las Juntas de Personal", "igual o superior a 6 e inferior a 50", "Hasta 30 funcionarios se elegirá un Delegado, y de 31 a 49 se elegirán tres", "un censo mínimo de 50 funcionarios", "con el máximo de 75", "al menos, dos tercios de sus miembros"]),
  fichab("Órganos específicos de representación de los funcionarios",
         ["**Delegados de Personal**: unidades electorales de **6 a 49** funcionarios; representación **conjunta y mancomunada**", "**Juntas de Personal**: unidades electorales con censo mínimo de **50** funcionarios; eligen **Presidente y Secretario**"],
         ["Unidades electorales: las regula el Estado y cada Comunidad Autónoma; pueden modificarse previo acuerdo con los sindicatos legitimados (39.4)", "Reglamento de procedimiento propio de cada Junta, con copia al órgano competente en materia de personal (39.6)"],
         ["::Escala:", "Delegados: hasta 30 funcionarios, **1**; de 31 a 49, **3**", "Juntas: 50-100, **5**; 101-250, **9**; 251-500, **13**; 501-750, **17**; 751-1.000, **21**; más de 1.000, dos por cada 1.000 o fracción, máximo **75**", "Reglamento de la Junta: **dos tercios** de sus miembros"],
         "**6** es el mínimo para tener Delegado; **50** el mínimo para Junta. Reglamento de la Junta: **dos tercios**. Máximo de la Junta: **75**."))}

{unidad("1.2 Personal laboral: delegados de personal y comités de empresa (ET, arts. 62.1 y 63.1)",
  lit("ET", "Artículo 62", ["menos de cincuenta y más de diez trabajadores", "entre seis y diez trabajadores, si así lo decidieran estos por mayoría", "hasta treinta trabajadores, uno; de treinta y uno a cuarenta y nueve, tres"], solo=[1, 2]),
  lit("ET", "Artículo 63", ["cincuenta o más trabajadores"], solo=[1]),
  fichab("Representación unitaria del personal laboral según la legislación laboral (TREBEP, art. 32, → I.3.3)",
         ["**Delegados de personal**: más de 10 y menos de 50 trabajadores (de 6 a 10, si lo deciden estos por mayoría)", "**Comité de empresa**: centros de **50 o más** trabajadores"],
         "Sufragio libre, personal, secreto y directo",
         "Delegados: hasta 30 trabajadores, **uno**; de 31 a 49, **tres**",
         "Entre **seis y diez** trabajadores, el delegado es **potestativo** (si lo deciden por mayoría); el comité de empresa empieza en **50**, como la Junta de Personal."))}

{unidad("1.3 Representación unitaria en el IV Convenio Único de la AGE (art. 85)",
  lit("CONV", "Artículo 85", ["Los Delegados y Delegadas de personal", "Los Comités de empresa", "a la escala prevista en el artículo 66 del Estatuto de los Trabajadores"], solo=[1, 2, 3, 4, 5], titulo="Artículo 85. Representación unitaria (IV Convenio Único AGE)"),
  fichab("Órganos de representación unitaria del personal laboral del Convenio (tema V.7)",
         ["Delegados y Delegadas de personal: centros de **menos de cincuenta** trabajadores", "Comités de empresa: centros de **cincuenta o más**"],
         "Elección según los acuerdos en la materia en el ámbito de la AGE (85.2)",
         "Composición de los Comités: escala del **art. 66 ET** (85.3)",
         "Representación **unitaria** = Delegados de personal y Comités de empresa. Delegado **sindical** y sección sindical son representación **sindical**; el comité de Seguridad y Salud tampoco es órgano unitario (pregunta oficial L 75, → Cierre 1)."))}
""", 2)

T.ap("s11", "III.2 Funciones, legitimación y garantías (arts. 40 y 41)", f"""
{unidad("2.1 Funciones y legitimación (art. 40)",
  lit("TREBEP", "Artículo 40", ["Ser informados de todas las sanciones impuestas por faltas muy graves", "Tener conocimiento y ser oídos en el establecimiento de la jornada laboral y horario de trabajo", "por decisión mayoritaria de sus miembros", "mancomunadamente"]),
  fichab("Qué hacen los órganos de representación de los funcionarios",
         "Las Juntas de Personal y los Delegados de Personal, en sus respectivos ámbitos",
         ["::Funciones (40.1):", "a) Recibir información sobre política de personal, retribuciones, empleo y programas de mejora del rendimiento", "b) Emitir informe, **a solicitud** de la Administración, sobre traslado de instalaciones y sistemas de organización y métodos de trabajo", "c) Ser informados de **todas las sanciones** por faltas **muy graves**", "d) Conocer y ser oídos sobre jornada, horario, vacaciones y permisos", "e) Vigilar el cumplimiento de normas de condiciones de trabajo, prevención, Seguridad Social y empleo, y ejercer acciones legales", "f) Colaborar en el mantenimiento e incremento de la productividad"],
         "Legitimación (40.2): la Junta, **colegiadamente, por decisión mayoritaria**; los Delegados, **mancomunadamente**; como **interesados** en procedimientos administrativos y acciones administrativas o judiciales",
         "Se les informa de las sanciones por faltas **muy graves** (no de todas las sanciones). El informe sobre organización es **a solicitud** de la Administración."))}

{unidad("2.2 Garantías y derechos (art. 41)",
  lit("TREBEP", "Artículo 41", ["durante el año inmediatamente posterior", "Un crédito de horas mensuales", "Hasta 100 funcionarios: 15", "De 751 en adelante: 40", "a la acumulación de los créditos horarios", "ni en el año siguiente a su extinción, exceptuando la extinción que tenga lugar por revocación o dimisión", "observarán sigilo profesional"]),
  fichab("Garantías de los representantes de los funcionarios",
         "Los miembros de las Juntas de Personal y los Delegados de Personal, como **representantes legales** de los funcionarios",
         ["a) Acceso y libre circulación por las dependencias de su unidad electoral", "b) Distribución libre de publicaciones profesionales y sindicales", "c) **Audiencia** en sus expedientes disciplinarios durante el mandato y el año posterior", "d) **Crédito de horas** mensuales retribuidas, acumulable entre miembros de la misma candidatura", "e) No ser **trasladados ni sancionados** por causas relacionadas con su mandato, durante él ni en el año siguiente (salvo revocación o dimisión)", "No discriminación en formación y promoción (41.2); **sigilo profesional**, aun tras el mandato (41.3)"],
         ["::Crédito de horas mensuales:", "Hasta 100 funcionarios: **15**", "101-250: **20**", "251-500: **30**", "501-750: **35**", "751 en adelante: **40**"],
         "La protección frente a traslado o sanción dura el mandato **y el año siguiente**, salvo extinción por **revocación o dimisión**. Crédito: de **15** a **40** horas."))}
""", 2)

T.ap("s12", "III.3 Mandato, promoción de elecciones y procedimiento electoral (arts. 42 a 44 y disposición transitoria quinta)", f"""
{unidad("3.1 Duración del mandato (art. 42)",
  lit("TREBEP", "Artículo 42", ["será de cuatro años, pudiendo ser reelegidos", "se entenderá prorrogado"]),
  fichab("Mandato de los representantes de los funcionarios",
         "Los miembros de las Juntas de Personal y los Delegados de Personal",
         "Si a su término no se promueven nuevas elecciones, el mandato se **prorroga**; los prorrogados **no** cuentan para la capacidad representativa de los sindicatos",
         "**Cuatro años**, con **reelección** posible",
         "**Cuatro** años y **pueden ser reelegidos** (pregunta oficial X 83, → Cierre 1)."))}

{unidad("3.2 Quién promueve las elecciones (art. 43)",
  lit("TREBEP", "Artículo 43", ["Los Sindicatos más representativos a nivel estatal", "al menos el 10 por 100 de los representantes a los que se refiere este Estatuto en el conjunto de las Administraciones Públicas", "al menos un porcentaje del 10 por 100 en la unidad electoral", "Los funcionarios de la unidad electoral, por acuerdo mayoritario", "el censo de personal"]),
  fichab("Promoción de elecciones a Delegados y Juntas de Personal",
         ["a) Sindicatos más representativos a nivel **estatal**", "b) Más representativos de **comunidad autónoma** (unidad electoral en su ámbito)", "c) Sindicatos con al menos el **10 por 100** de los representantes en el **conjunto** de las Administraciones Públicas", "d) Sindicatos con al menos el **10 por 100** en la **unidad electoral**", "e) Los **funcionarios** de la unidad electoral, por **acuerdo mayoritario**"],
         "Los promotores tienen derecho a que la Administración les suministre el **censo** de personal de las unidades electorales (43.2)",
         "—",
         "También pueden promover los **funcionarios**, por **acuerdo mayoritario**. El 10 % se cuenta en el **conjunto** de las AA. PP. (letra c) o en la **unidad electoral** (letra d)."))}

{unidad("3.3 Criterios del procedimiento electoral (art. 44)",
  lit("TREBEP", "Artículo 44", ["sufragio personal, directo, libre y secreto que podrá emitirse por correo o por otros medios telemáticos", "en la situación de servicio activo", "al triple de los miembros a elegir", "listas cerradas a través de un sistema proporcional corregido", "listas abiertas y sistema mayoritario", "procedimiento arbitral"]),
  fichab("Elección de Juntas y Delegados de Personal",
         ["Electores y elegibles: funcionarios en **servicio activo**; no lo son los nombrados por **real decreto** o por decreto de los consejos de gobierno autonómicos y de Ceuta y Melilla", "Candidaturas: sindicatos o coaliciones, y grupos de electores de la unidad (al menos el **triple** de los miembros a elegir)"],
         ["Sufragio personal, directo, libre y secreto, también por correo o medios telemáticos", "**Juntas**: listas **cerradas**, sistema **proporcional corregido**", "**Delegados**: listas **abiertas**, sistema **mayoritario**", "Órganos electorales: Mesas Electorales y oficinas públicas permanentes", "Impugnaciones: procedimiento **arbitral**; denegación de inscripción de actas: directamente ante la **jurisdicción social**"],
         "Grupos de electores: al menos el **triple** de los miembros a elegir",
         "Juntas → listas **cerradas** y **proporcional corregido**; Delegados → listas **abiertas** y **mayoritario**. Las impugnaciones van a **arbitraje**, salvo la denegación de inscripción de actas (**jurisdicción social**)."))}

{unidad("3.4 Normas de la Ley 9/1987 que siguen aplicándose (disposición transitoria quinta)",
  lit("TREBEP", "dtquinta", ["se mantendrán con carácter de normativa básica"], titulo="Disposición transitoria quinta. Procedimiento Electoral General (TREBEP)"),
  fichab("Régimen transitorio del procedimiento electoral",
         "—",
         "Mientras no se determine el procedimiento electoral general del art. 39, siguen como **normativa básica** los artículos de la Ley 9/1987 que enumera esta disposición",
         "—",
         "La Ley 9/1987 quedó derogada por el TREBEP salvo su art. 7 y lo previsto en esta disposición transitoria (disposición derogatoria única, letra c)."))}
""", 2)

T.ap("s13", "III.4 Derecho de reunión (art. 46)", f"""
{unidad("4.1 Quién convoca y cuándo (art. 46)",
  lit("TREBEP", "Artículo 46", ["directamente o a través de los Delegados Sindicales", "en número no inferior al 40 por 100 del colectivo convocado", "se autorizarán fuera de las horas de trabajo", "serán responsables de su normal desarrollo"]),
  ficha(["::Legitimados para convocar (46.1):", "Las organizaciones sindicales, directamente o a través de los Delegados Sindicales", "a) Los Delegados de Personal", "b) Las Juntas de Personal", "c) Los Comités de Empresa", "d) Los empleados públicos, en número **no inferior al 40 por 100** del colectivo convocado"],
        "Reunión en el centro de trabajo (art. 15 e, → I.2.1)",
        ["Fuera de las horas de trabajo, salvo acuerdo entre el órgano competente en materia de personal y los convocantes (46.2)", "No puede perjudicar la prestación de los servicios"],
        "Los convocantes responden de su **normal desarrollo**",
        "Los empleados convocan si son **al menos el 40 %** del colectivo. La regla es **fuera** de las horas de trabajo."))}

{resumen([
  "Funcionarios: **Delegados de Personal** (6 a 49; 1 hasta 30, 3 de 31 a 49) y **Juntas de Personal** (50 o más; máximo 75) (39). Laborales: **delegados de personal** y **comités de empresa** (ET 62-63; Convenio, art. 85).",
  "Funciones (40): información, informe a solicitud, conocer las sanciones por faltas **muy graves**, ser oídos en jornada y horarios; legitimación como **interesados**.",
  "Garantías (41): audiencia en expedientes, **crédito de 15 a 40 horas**, no traslado ni sanción durante el mandato y el **año siguiente**.",
  "Mandato de **cuatro años**, con **reelección** (42); promueven sindicatos y funcionarios por **acuerdo mayoritario** (43); Juntas por listas **cerradas** y Delegados por listas **abiertas** (44).",
  "Reunión: convocan sindicatos, órganos unitarios y el **40 %** del colectivo; **fuera** de las horas de trabajo salvo acuerdo (46)."],
  "Siguiente: IV. ¿Cómo se ejerce el derecho de huelga?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Cómo se ejerce el derecho de huelga? (CE, arts. 28.2 y 37.2; RDL 17/1977; TREBEP, arts. 30.2 y 95.2)", donde(
  "Cuarta pregunta. La huelga es un **derecho fundamental** de los trabajadores (art. 28.2 CE) y el TREBEP la reconoce a los empleados públicos con la garantía de los **servicios esenciales** (art. 15 c, → I.2.1). Su ejercicio se regula en el título I del **Real Decreto-ley 17/1977**, en lo que dejó vigente la **STC 11/1981**.",
  ["1 Reconocimiento constitucional (arts. 28.2 y 37.2)", "2 El ejercicio del derecho de huelga (RDL 17/1977, arts. 1 a 11)", "3 Consecuencias para el empleado público (TREBEP, arts. 30.2 y 95.2 k, l y m)", "4 Cuadro: lo vigente y lo anulado del RDL 17/1977"]))

T.ap("s14", "IV.1 Reconocimiento constitucional (arts. 28.2 y 37.2)", f"""
{unidad("1.1 El derecho de huelga (art. 28.2)",
  lit("CE", "Artículo 28", ["Se reconoce el derecho a la huelga de los trabajadores para la defensa de sus intereses", "las garantías precisas para asegurar el mantenimiento de los servicios esenciales de la comunidad"], solo=[2]),
  ficha(c("CE", "Artículo 28", "los trabajadores"),
        c("CE", "Artículo 28", "para la defensa de sus intereses"),
        "La ley que regule su ejercicio debe establecer las garantías precisas para asegurar el mantenimiento de los **servicios esenciales de la comunidad**",
        "Derecho fundamental (Sección 1.ª del Capítulo segundo del Título I)",
        "La garantía es el mantenimiento de los **servicios esenciales de la comunidad** (no «servicios mínimos» ni «servicios públicos»: esas palabras no están en el art. 28.2)."))}

{unidad("1.2 Medidas de conflicto colectivo (art. 37.2)",
  lit("CE", "Artículo 37", ["adoptar medidas de conflicto colectivo", "para asegurar el funcionamiento de los servicios esenciales de la comunidad"], solo=[2]),
  ficha(c("CE", "Artículo 37", "los trabajadores y empresarios"),
        "Adoptar medidas de conflicto colectivo",
        "La ley puede establecer limitaciones e incluirá las garantías precisas para asegurar el **funcionamiento** de los servicios esenciales",
        "Sección 2.ª del Capítulo segundo",
        "La **huelga** es de los **trabajadores** (28.2); las **medidas de conflicto colectivo**, de **trabajadores y empresarios** (37.2). En los empleados públicos, el planteamiento de conflictos colectivos es la letra d) del art. 15 TREBEP (→ I.2.1)."))}
""", 2)

T.ap("s15", "IV.2 El ejercicio del derecho de huelga (RDL 17/1977, arts. 1 a 11)", f"""
El título I («El derecho de huelga») del Real Decreto-ley 17/1977, sobre relaciones de trabajo, sigue en el texto consolidado del BOE. Su art. 1 lo refiere al **ámbito de las relaciones laborales**. Se cita **solo el texto vigente**: donde el BOE indica un inciso declarado inconstitucional por la STC 11/1981, se omite y se reproduce la nota del BOE.

{unidad("2.1 Ámbito y nulidad de la renuncia (arts. 1 y 2)",
  lit("RDL17", "Artículo uno", ["en el ámbito de las relaciones laborales"], titulo="Artículo 1 (RDL 17/1977)"),
  lit("RDL17", "Artículo dos", ["Son nulos los pactos"], titulo="Artículo 2 (RDL 17/1977)"),
  ficha("Los trabajadores, en el ámbito de las relaciones laborales",
        "Ejercicio del derecho de huelga en los términos del Real Decreto-ley",
        "—",
        f"{c('RDL17', 'Artículo dos', 'Son nulos los pactos establecidos en contratos individuales de trabajo que contengan la renuncia o cualquier otra restricción al derecho de huelga')}",
        "La renuncia en un **contrato individual** es **nula**. Otra cosa es el convenio colectivo, que puede incluir la renuncia **durante su vigencia** (art. 8, → IV.2.5)."))}

{unidad("2.2 Declaración, comunicación y preaviso (arts. 3 y 4)",
  lit("RDL17", "Artículo tres", ["por escrito y notificada con cinco días naturales de antelación", "composición del comité de huelga"], solo=[5, 6], titulo="Artículo 3, apartado tres (RDL 17/1977)"),
  aviso_tc("atres", "Se declara la inconstitucionalidad de las exigencias establecidas en los incisos destacados de los apartados 1 y 2 por Sentencia del TC 11/1981"),
  lit("RDL17", "Artículo cuatro", ["de diez días naturales", "la publicidad necesaria para que sea conocida por los usuarios del servicio"], titulo="Artículo 4 (RDL 17/1977)"),
  fichab("Cómo se declara y se comunica una huelga",
         [f"Declaran la huelga (art. 3.2): {c('RDL17', 'Artículo tres', 'Los trabajadores, a través de sus representantes')}, por decisión mayoritaria, o {c('RDL17', 'Artículo tres', 'Directamente los propios trabajadores del centro de trabajo, afectados por el conflicto')}, en votación secreta por mayoría simple", "Comunican: los representantes de los trabajadores, al empresario y a la autoridad laboral (3.3)"],
         ["Comunicación **por escrito**, con objetivos, gestiones realizadas, fecha de inicio y composición del **comité de huelga** (3.3)", "Servicios públicos: publicidad suficiente para los **usuarios** (art. 4)"],
         ["::Preaviso:", "General: **cinco días naturales** al menos (3.3)", "Empresas de **servicios públicos**: **diez días naturales** al menos (art. 4)"],
         "**5** días naturales en general; **10** en servicios públicos. Los incisos anulados del art. 3 (acuerdo «en cada centro de trabajo», asistencia del **75 %** de los representantes y decisión del **25 %** de la plantilla para votar) **no** se citan como vigentes."))}

{unidad("2.3 El comité de huelga (art. 5)",
  lit("RDL17", "Artículo cinco", ["no podrá exceder de doce personas", "participar en cuantas actuaciones sindicales, administrativas o judiciales"], solo=[2, 3], titulo="Artículo 5, párrafos segundo y tercero (RDL 17/1977)"),
  aviso_tc("acinco", "Se declara la inconstitucionalidad del párrafo 1, cuando las huelgas comprendan varios centros de trabajo"),
  fichab("Órgano que representa a los huelguistas",
         "Trabajadores elegidos como miembros del comité",
         "Participa en las actuaciones sindicales, administrativas o judiciales para la solución del conflicto y negocia con el empresario (art. 8.2, → IV.2.5)",
         "Máximo **doce** personas",
         "El comité no puede exceder de **doce** personas. La exigencia de ser trabajadores «del propio centro» del párrafo primero no vale cuando la huelga comprende **varios centros** (nota del BOE)."))}

{unidad("2.4 Efectos de la huelga (art. 6)",
  lit("RDL17", "Artículo seis", ["no extingue la relación de trabajo", "se entenderá suspendido el contrato de trabajo y el trabajador no tendrá derecho al salario", "en situación de alta especial en la Seguridad Social", "Se respetará la libertad de trabajo", "el empresario no podrá sustituir a los huelguistas", "en forma pacífica"], solo=[1, 2, 3, 4, 5, 6], titulo="Artículo 6, apartados uno a seis (RDL 17/1977)"),
  aviso_tc("aseis", "Se declara la inconstitucionalidad del apartado 7, en cuanto atribuye de manera exclusiva al empresario la facultad de designar los trabajadores que deban efectuar dichos servicios"),
  ficha("El trabajador en huelga y los que no se suman",
        ["No extingue la relación ni puede sancionarse, salvo falta laboral durante la huelga (6.1)", "Contrato **suspendido**, sin derecho al **salario** (6.2)", "**Alta especial** en la Seguridad Social, sin cotización; sin prestación por desempleo ni por incapacidad laboral transitoria (6.3)", "Publicidad pacífica y recogida de fondos sin coacción (6.6)"],
        ["Se respeta la **libertad de trabajo** de quien no se suma (6.4)", "El empresario **no puede sustituir** a los huelguistas por trabajadores no vinculados a la empresa al comunicarse la huelga, salvo incumplimiento del 6.7 (6.5)", f"El comité de huelga garantiza {c('RDL17', 'Artículo seis', 'la prestación de los servicios necesarios para la seguridad de las personas y de las cosas')} (6.7)"],
        "—",
        "Durante la huelga: contrato **suspendido**, **sin salario**, **alta especial** sin cotizar. La designación de los trabajadores de los servicios de seguridad y mantenimiento **no** es exclusiva del empresario (nota del BOE)."))}

{unidad("2.5 Huelgas ilícitas, negociación y mediación (arts. 7, 8 y 9)",
  lit("RDL17", "Artículo siete", ["sin ocupación por los mismos del centro de trabajo", "Las huelgas rotatorias", "las de celo o reglamento", "se considerarán actos ilícitos o abusivos"], titulo="Artículo 7 (RDL 17/1977)"),
  lit("RDL17", "Artículo ocho", ["la renuncia, durante su vigencia, al ejercicio de tal derecho", "deberán negociar para llegar a un acuerdo", "tendrá la misma eficacia que lo acordado en Convenio Colectivo"], titulo="Artículo 8 (RDL 17/1977)"),
  lit("RDL17", "Artículo nueve", ["La Inspección de Trabajo podrá ejercer su función de mediación"], titulo="Artículo 9 (RDL 17/1977)"),
  fichab("Cómo debe hacerse la huelga y cómo se busca salida",
         ["Los trabajadores afectados (cesación del trabajo)", "El comité de huelga y el empresario (negociación)", "La **Inspección de Trabajo** (mediación)"],
         ["Huelga = **cesación** de la prestación de servicios, **sin ocupación** del centro (7.1)", "**Ilícitas o abusivas**: rotatorias, las de trabajadores de sectores estratégicos para interrumpir el proceso productivo, las de **celo o reglamento** y cualquier alteración colectiva distinta de la huelga (7.2)", "Los Convenios pueden prever solución de conflictos y la **renuncia** a la huelga **durante su vigencia** (8.1)", "Deber de negociar desde el preaviso; el pacto que pone fin a la huelga tiene la **eficacia de un Convenio Colectivo** (8.2)"],
         "Mediación de la Inspección: desde que se comunica la huelga hasta la solución del conflicto (art. 9)",
         "La huelga **de celo o reglamento** y la **rotatoria** son **ilícitas o abusivas**. El pacto de fin de huelga = **Convenio Colectivo**."))}

{unidad("2.6 Servicios esenciales: medidas de la autoridad gubernativa (art. 10, párrafo segundo)",
  lit("RDL17", "Artículo diez", ["de reconocida e inaplazable necesidad", "la Autoridad gubernativa podrá acordar las medidas necesarias para asegurar el funcionamiento de los servicios"], solo=[2], titulo="Artículo 10, párrafo segundo (RDL 17/1977)"),
  aviso_tc("adiez", "Se declara la inconstitucionalidad del párrafo 1, en cuanto faculta al Gobierno para imponer la reanudación del trabajo, pero no en cuanto le faculta para instituir un arbitraje obligatorio, siempre que en él se respete el requisito de imparcialidad de los árbitros"),
  fichab("Garantía del funcionamiento de los servicios cuando la huelga afecta a servicios públicos",
         "La **Autoridad gubernativa**; el Gobierno puede adoptar medidas de intervención adecuadas",
         "Medidas necesarias para asegurar el funcionamiento de los servicios",
         "Presupuestos: empresas de servicios públicos o de reconocida e inaplazable necesidad **y** circunstancias de **especial gravedad**",
         f"Es la garantía de los **servicios esenciales** del art. 28.2 CE. Del párrafo primero, el Gobierno **no** puede imponer la **reanudación** del trabajo; sí {c('RDL17', 'Artículo diez', 'el establecimiento de un arbitraje obligatorio')}, con árbitros **imparciales** (nota del BOE)."))}

{unidad("2.7 La huelga ilegal (art. 11)",
  lit("RDL17", "Artículo once", ["por motivos políticos", "alterar, dentro de su período de vigencia, lo pactado en un Convenio Colectivo", "contraviniendo lo dispuesto en el presente Real Decreto-ley"], solo=[1, 2, 4, 5], titulo="Artículo 11, letras a), c) y d) (RDL 17/1977)"),
  aviso_tc("aonce", "Se declara la inconstitucionalidad del inciso destacado del apartado b)"),
  fichab("Supuestos de huelga ilegal",
         "—",
         ["a) Por motivos **políticos** o finalidad ajena al interés profesional de los afectados", f"b) {c('RDL17', 'Artículo once', 'Cuando sea de solidaridad o apoyo, salvo que afecte')} al interés profesional de quienes la promuevan o sostengan (el inciso «directamente» fue anulado)", "c) Para **alterar** lo pactado en un **Convenio** o laudo **durante su vigencia**", "d) Contraviniendo el Real Decreto-ley o lo pactado en Convenio para la solución de conflictos"],
         "—",
         "Cuatro supuestos: **políticos**, **solidaridad** (salvo interés profesional), **alterar un convenio vigente** y **contravenir** el RDL o el convenio."))}
""", 2)

T.ap("s16", "IV.3 Consecuencias para el empleado público (TREBEP, arts. 30.2 y 95.2 k, l y m)", f"""
Las retribuciones se estudian en el tema V.6 y el régimen disciplinario en el tema V.2; aquí, solo lo que el TREBEP dice de la huelga.

{unidad("3.1 Deducción de retribuciones (art. 30.2)",
  lit("TREBEP", "Artículo 30", ["no devengarán ni percibirán las retribuciones", "sin que la deducción de haberes que se efectúe tenga carácter de sanción", "ni afecte al régimen respectivo de sus prestaciones sociales"], solo=[2]),
  fichab("Efecto económico de la huelga en el empleado público",
         c("TREBEP", "Artículo 30", "Quienes ejerciten el derecho de huelga"),
         "No devengan ni perciben las retribuciones del tiempo en huelga",
         "—",
         "La deducción **no es sanción** y **no afecta** a sus prestaciones sociales."))}

{unidad("3.2 Faltas muy graves relacionadas con la huelga (art. 95.2 k, l y m)",
  lit("TREBEP", "Artículo 95", ["La obstaculización al ejercicio de las libertades públicas y derechos sindicales", "coartar el libre ejercicio del derecho de huelga", "El incumplimiento de la obligación de atender los servicios esenciales en caso de huelga"], solo=[13, 14, 15], titulo="Artículo 95.2, letras k), l) y m) (TREBEP)"),
  fichab("Protección disciplinaria de los derechos sindicales y de huelga",
         "Cualquier empleado público (quien coarta la huelga u obstaculiza los derechos sindicales, y quien incumple los servicios esenciales)",
         ["k) Obstaculizar las libertades públicas y los derechos sindicales", "l) Actos para **coartar** el libre ejercicio del derecho de huelga", "m) **No atender los servicios esenciales** en caso de huelga"],
         "Son faltas **muy graves**",
         "Las tres son **muy graves**: tanto impedir la huelga como no cumplir los **servicios esenciales**."))}
""", 2)

T.ap("s17", "IV.4 Cuadro: lo vigente y lo anulado del RDL 17/1977 (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados y las notas del texto consolidado del BOE sobre la STC 11/1981; no es texto legal.*

| Artículo | Qué regula | Lo que el BOE marca como inconstitucional (STC 11/1981) |
|---|---|---|
| 1 y 2 | Ámbito; nulidad de la renuncia en contrato individual | — |
| 3 | Declaración y comunicación (preaviso de 5 días naturales) | Los incisos destacados de los apartados 1 y 2 |
| 4 | Servicios públicos: preaviso de 10 días naturales | — |
| 5 | Comité de huelga (máximo 12) | Párrafo 1, cuando la huelga comprende varios centros de trabajo |
| 6 | Efectos: suspensión, sin salario, alta especial | Apartado 7, en cuanto atribuye **en exclusiva** al empresario la designación de los trabajadores de los servicios de seguridad y mantenimiento |
| 7 a 9 | Formas ilícitas; negociación; mediación de la Inspección | — |
| 10 | Párrafo 1: reanudación y arbitraje obligatorio; párrafo 2: servicios esenciales | Párrafo 1, en cuanto faculta al Gobierno para **imponer la reanudación** (no el arbitraje obligatorio con árbitros imparciales) |
| 11 | Huelga ilegal | El inciso destacado de la letra b) |

{resumen([
  "CE: **huelga** de los **trabajadores** para la defensa de sus intereses, con garantía de los **servicios esenciales de la comunidad** (28.2); medidas de **conflicto colectivo** de trabajadores y empresarios (37.2).",
  "RDL 17/1977: preaviso de **5** días naturales (**10** en servicios públicos); comité de huelga de **12** como máximo; contrato **suspendido** y **sin salario**; huelgas **rotatorias** y **de celo** ilícitas; pacto de fin de huelga = **Convenio**.",
  "Servicios esenciales: la **autoridad gubernativa** acuerda las medidas (10, párrafo 2.º). El Gobierno **no** puede imponer la reanudación (nota del BOE sobre la STC 11/1981).",
  "TREBEP: la deducción de haberes **no es sanción** (30.2); son faltas **muy graves** coartar la huelga y no atender los servicios esenciales (95.2 l y m)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX = [
 ("L", 76, "Materias excluidas de la negociación (→ II.3.1)", {
   "a": f"Es materia **negociable**: {c('TREBEP', 'Artículo 37', 'La determinación y aplicación de las retribuciones complementarias de los funcionarios')} (art. 37.1 b).",
   "b": f"Literal del art. 37.2 e): quedan excluidas {c('TREBEP', 'Artículo 37', 'La regulación y determinación concreta, en cada caso, de los sistemas, criterios, órganos y procedimientos de acceso al empleo público y la promoción profesional')}.",
   "c": f"Es materia **negociable**: {c('TREBEP', 'Artículo 37', 'Los criterios generales sobre ofertas de empleo público')} (art. 37.1 l).",
   "d": f"Es materia **negociable**: {c('TREBEP', 'Artículo 37', 'Los criterios generales para la determinación de prestaciones sociales y pensiones de clases pasivas')} (art. 37.1 g)."},
   [("La regulación y determinación concreta, en cada caso, de los sistemas, criterios, órganos y procedimientos de acceso al empleo público y la promoción profesional", "TREBEP", "Artículo 37", "e) La regulación y determinación concreta, en cada caso, de los sistemas, criterios, órganos y procedimientos de acceso al empleo público y la promoción profesional")]),
 ("X", 84, "Materias excluidas de la negociación (→ II.3.1)", {
   "a": f"Es materia **negociable**: {c('TREBEP', 'Artículo 37', 'La aplicación del incremento de las retribuciones del personal al servicio de las Administraciones Públicas que se establezca en la Ley de Presupuestos Generales del Estado')} (art. 37.1 a).",
   "b": f"Literal del art. 37.2 b): quedan excluidas {c('TREBEP', 'Artículo 37', 'La regulación del ejercicio de los derechos de los ciudadanos y de los usuarios de los servicios públicos, así como el procedimiento de formación de los actos y disposiciones administrativas')}.",
   "c": f"Es materia **negociable**: {c('TREBEP', 'Artículo 37', 'Las normas que fijen los criterios y mecanismos generales en materia de evaluación del desempeño')} (art. 37.1 d).",
   "d": f"Es materia **negociable**: {c('TREBEP', 'Artículo 37', 'Los criterios generales sobre ofertas de empleo público')} (art. 37.1 l)."},
   [("La regulación del ejercicio de los derechos de los ciudadanos y de los usuarios de los servicios públicos", "TREBEP", "Artículo 37", "b) La regulación del ejercicio de los derechos de los ciudadanos y de los usuarios de los servicios públicos, así como el procedimiento de formación de los actos y disposiciones administrativas")]),
 ("X", 83, "Duración del mandato (→ III.3.1)", {
   "a": f"Literal del art. 42: el mandato {c('TREBEP', 'Artículo 42', 'será de cuatro años, pudiendo ser reelegidos')}.",
   "b": f"Cambia la reelección: el art. 42 dice {c('TREBEP', 'Artículo 42', 'pudiendo ser reelegidos')}.",
   "c": f"Cambia la duración: son {c('TREBEP', 'Artículo 42', 'cuatro años')}, no dos.",
   "d": "Cambia la duración (cuatro años, no dos) y la reelección (que la ley permite)."},
   [("Cuatro años", "TREBEP", "Artículo 42", "será de cuatro años"), ("con posibilidad de reelección", "TREBEP", "Artículo 42", "pudiendo ser reelegidos")]),
 ("L", 75, "Representación unitaria del personal laboral (→ III.1.3)", {
   "a": f"El delegado sindical es representación **sindical**, no unitaria: las Secciones Sindicales {c('LOLS', 'Artículo diez', 'estarán representadas, a todos los efectos, por delegados sindicales')} (LO 11/1985, art. 10.1).",
   "b": f"Literal del art. 85.1 a) del Convenio: son órganos de representación unitaria {c('CONV', 'Artículo 85', 'Los Delegados y Delegadas de personal')}.",
   "c": f"La sección sindical es representación **sindical**: {c('CONV', 'Artículo 89', 'La representación sindical en el ámbito de este Convenio estará integrada por las Secciones Sindicales')} (art. 89.1 del Convenio).",
   "d": f"El art. 85.1 solo enumera dos órganos unitarios: {c('CONV', 'Artículo 85', 'Los Delegados y Delegadas de personal')} y {c('CONV', 'Artículo 85', 'Los Comités de empresa')}. El comité de Seguridad y Salud no está entre ellos."},
   [("delegado o delegada de personal", "CONV", "Artículo 85", "Los Delegados y Delegadas de personal que ostentarán la representación colectiva del personal laboral")]),
 ("X", 68, "Derechos individuales ejercidos colectivamente (relacionada; tema V.2) (→ I.2.1)", {
   "a": f"Es un derecho **individual** del art. 14: {c('TREBEP', 'Artículo 14', 'A la libre asociación profesional')} (art. 14 p).",
   "b": f"Literal del art. 15 a): entre los derechos individuales que se ejercen de forma colectiva, {c('TREBEP', 'Artículo 15', 'A la libertad sindical')}.",
   "c": f"Es un derecho **individual** del art. 14 e): {c('TREBEP', 'Artículo 14', 'A participar en la consecución de los objetivos atribuidos a la unidad donde preste sus servicios')}.",
   "d": f"Es un derecho **individual** del art. 14 f): {c('TREBEP', 'Artículo 14', 'A la defensa jurídica y protección de la Administración Pública')}."},
   [("libertad sindical", "TREBEP", "Artículo 15", "a) A la libertad sindical")]),
]
bloques = []
for cod, n, tit, por, ap_ in EX:
    bloques += [f"### {('GACE-L' if cod == 'L' else 'GACE-P' if cod == 'P' else 'GACE-L extraordinario')} 2025, pregunta {n} · {tit}", examen(cod, n, por, ap_)]
T.ap("s18", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join(
  ["En los primeros ejercicios de **2025** cayeron **cuatro** preguntas de este tema (dos sobre las materias excluidas de la negociación, una sobre el mandato de los representantes y una sobre la representación unitaria del IV Convenio Único) y una **relacionada** (la X 68, del tema V.2, sobre el art. 15 TREBEP). Todas son literales. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal."]
  + bloques + ["### Cómo se pregunta", "!> El art. 37 se pregunta poniendo **una** materia excluida (37.2) entre **tres** negociables (37.1). Truco: lo que empieza por «**criterios generales**» se negocia; la regulación **concreta** del acceso, los **derechos de los ciudadanos**, el **procedimiento**, el **personal directivo**, la **organización** y la **dirección** jerárquica, no. En representación, distingue la **unitaria** (Delegados y Juntas de Personal; delegados de personal y comités de empresa) de la **sindical** (secciones y delegados sindicales)."]))

T.ap("s19", "Cierre 2. Repaso en 10 minutos (por bloques)", """
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Derechos colectivos | CE 7, 28.1 y 103.3; TREBEP 15 (cinco derechos), 31 (tres conceptos) y 32; LO 11/1985 (más representativos) | **Libertad sindical** = derecho individual ejercido colectivamente; más representativos: **10 %** estatal, **15 %** y **1.500** autonómico |
| II. Negociación colectiva | Principios (33), Mesas (34-36), materias (37), Pactos y Acuerdos (38), mediación y arbitraje (45) | **Materias excluidas** (37.2); Mesa válida con **mayoría absoluta** de los órganos unitarios; **15** por parte; prórroga **de año en año** |
| III. Representación | Delegados (6-49) y Juntas de Personal (50+), funciones, garantías, elecciones, reunión | Mandato de **cuatro años con reelección**; crédito de **15 a 40** horas; reunión: **40 %** |
| IV. Huelga | CE 28.2; RDL 17/1977 (lo vigente tras la STC 11/1981); TREBEP 30.2 y 95.2 | Preaviso **5** días (**10** en servicios públicos); comité de **12**; deducción de haberes **no** es sanción |

?> **Trampas frecuentes:** «los criterios generales sobre ofertas de empleo público están excluidos de la negociación» (se **negocian**, 37.1 l); «el mandato es de cuatro años sin reelección» (**con** reelección, 42); «el delegado sindical es órgano de representación unitaria» (es representación **sindical**); «la mediación es siempre voluntaria» (es **obligatoria** si la pide una parte, 45.3); «la Mesa General de las Administraciones Públicas la preside la FEMP» (la preside la **AGE**, 36.1); «la deducción de haberes por huelga es una sanción» (**no** lo es, 30.2).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
Q = [
 ("TREBEP", "Artículo 15", "Derechos colectivos", "Según el artículo 15 del TREBEP, ¿cuál de los siguientes es un derecho individual de los empleados públicos que se ejerce de forma colectiva?",
  ["Al ejercicio de la huelga, con la garantía del mantenimiento de los servicios esenciales de la comunidad.", "A la libre asociación profesional.", "A la progresión en la carrera profesional y promoción interna.", "A la formación continua y a la actualización permanente de sus conocimientos."],
  "Art. 15 c) TREBEP. Los otros tres son derechos individuales del art. 14.", "c) Al ejercicio de la huelga, con la garantía del mantenimiento de los servicios esenciales de la comunidad"),
 ("TREBEP", "Artículo 31", "Derechos colectivos", "Según el artículo 31.4 del TREBEP, la participación institucional es el derecho a participar en los órganos de control y seguimiento de las entidades u organismos que legalmente se determine:",
  ["A través de las organizaciones sindicales.", "A través de las Juntas de Personal.", "A través de los Delegados de Personal.", "Directamente, por cada empleado público."],
  "Art. 31.4 TREBEP.", "el derecho a participar, a través de las organizaciones sindicales, en los órganos de control y seguimiento"),
 ("TREBEP", "Artículo 31", "Derechos colectivos", "Según el artículo 31.3 del TREBEP, se entiende por representación:",
  ["La facultad de elegir representantes y constituir órganos unitarios a través de los cuales se instrumente la interlocución entre las Administraciones Públicas y sus empleados.", "El derecho a negociar la determinación de condiciones de trabajo de los empleados de la Administración Pública.", "El derecho a participar, a través de las organizaciones sindicales, en los órganos de control y seguimiento de las entidades u organismos.", "La facultad de constituir secciones sindicales en cada centro de trabajo."],
  "Art. 31.3 TREBEP. El derecho a negociar la determinación de condiciones de trabajo es la negociación colectiva (31.2), y el de participar a través de las organizaciones sindicales en los órganos de control y seguimiento, la participación institucional (31.4).", "la facultad de elegir representantes y constituir órganos unitarios a través de los cuales se instrumente la interlocución"),
 ("TREBEP", "Artículo 31", "Derechos colectivos", "Según el artículo 31.6 del TREBEP, ¿quiénes están legitimadas para interponer recursos en vía administrativa y jurisdiccional contra las resoluciones de los órganos de selección?",
  ["Las organizaciones sindicales más representativas en el ámbito de la Función Pública.", "Cualquier organización sindical legalmente constituida.", "Las Juntas de Personal, por decisión mayoritaria.", "Las organizaciones sindicales firmantes del último Acuerdo de la Mesa General."],
  "Art. 31.6 TREBEP.", "Las organizaciones sindicales más representativas en el ámbito de la Función Pública están legitimadas para la interposición de recursos"),
 ("LOLS", "Artículo primero", "Libertad sindical", "Según el artículo 1 de la Ley Orgánica 11/1985, de Libertad Sindical, quedan exceptuados del ejercicio del derecho de sindicación:",
  ["Los miembros de las Fuerzas Armadas y de los Institutos Armados de carácter militar.", "Los funcionarios públicos de carrera.", "Los miembros de los Cuerpos y Fuerzas de Seguridad sin carácter militar.", "El personal estatutario de los servicios de salud."],
  "Art. 1.3 LOLS. Los Cuerpos y Fuerzas de Seguridad sin carácter militar se rigen por su normativa específica (1.5).", "Quedan exceptuados del ejercicio de este derecho los miembros de las Fuerzas Armadas y de los Institutos Armados de carácter militar"),
 ("LOLS", "Artículo primero", "Libertad sindical", "Según el artículo 1.4 de la Ley Orgánica de Libertad Sindical, los Jueces, Magistrados y Fiscales:",
  ["No podrán pertenecer a sindicato alguno mientras se hallen en activo.", "Pueden afiliarse a sindicatos, pero no fundarlos.", "Ejercen la libertad sindical según su normativa específica.", "Pueden pertenecer a sindicatos de ámbito judicial únicamente."],
  "Art. 1.4 LOLS, en relación con el art. 127.1 CE.", "no podrán pertenecer a sindicato alguno mientras se hallen en activo"),
 ("LOLS", "Artículo segundo", "Libertad sindical", "Según el artículo 2.2 c) de la Ley Orgánica de Libertad Sindical, las organizaciones sindicales tienen derecho a no ser suspendidas ni disueltas sino mediante:",
  ["Resolución firme de la Autoridad Judicial, fundada en incumplimiento grave de las Leyes.", "Resolución del Ministerio de Trabajo, previo informe de la oficina pública.", "Acuerdo del Consejo de Ministros.", "Resolución de la oficina pública de depósito de estatutos."],
  "Art. 2.2 c) LOLS.", "No ser suspendidas ni disueltas sino mediante resolución firme de la Autoridad Judicial, fundada en incumplimiento grave de las Leyes"),
 ("LOLS", "Artículo sexto", "Libertad sindical", "Según el artículo 6.2 a) de la Ley Orgánica de Libertad Sindical, tienen la consideración de sindicatos más representativos a nivel estatal los que obtengan en dicho ámbito:",
  ["El 10 por 100 o más del total de delegados de personal, de los miembros de los comités de empresa y de los correspondientes órganos de las Administraciones públicas.", "El 15 por 100 o más del total de delegados de personal y miembros de comités de empresa.", "Al menos 1.500 representantes.", "El 5 por 100 de los votos en las elecciones a órganos de representación."],
  "Art. 6.2 a) LOLS. El 15 por 100 y los 1.500 representantes son del nivel autonómico (art. 7.1).", "del 10 por 100 o más del total de delegados de personal de los miembros de los comités de empresa y de los correspondientes órganos de las Administraciones públicas"),
 ("LOLS", "Artículo séptimo", "Libertad sindical", "Según el artículo 7.1 de la Ley Orgánica de Libertad Sindical, son más representativos a nivel de Comunidad Autónoma los sindicatos que obtengan en ella al menos:",
  ["El 15 por 100 de los delegados de personal y representantes, con un mínimo de 1.500 representantes.", "El 10 por 100 de los delegados de personal y representantes, con un mínimo de 1.000 representantes.", "El 15 por 100 de los delegados de personal, sin mínimo de representantes.", "El 20 por 100 de los delegados de personal y representantes, con un mínimo de 1.500 representantes."],
  "Art. 7.1 LOLS.", "al menos, el 15 por 100 de los delegados de personal"),
 ("TREBEP", "Artículo 33", "Negociación colectiva", "Según el artículo 33.1 del TREBEP, la negociación colectiva de condiciones de trabajo de los funcionarios públicos estará sujeta, entre otros, a los principios de:",
  ["Legalidad, cobertura presupuestaria, obligatoriedad, buena fe negocial, publicidad y transparencia.", "Legalidad, eficacia, jerarquía, confidencialidad y buena fe negocial.", "Igualdad, mérito, capacidad y publicidad.", "Voluntariedad, cobertura presupuestaria, reserva y buena fe negocial."],
  "Art. 33.1 TREBEP.", "legalidad, cobertura presupuestaria, obligatoriedad, buena fe negocial, publicidad y transparencia"),
 ("TREBEP", "Artículo 33", "Negociación colectiva", "Según el artículo 33.1 del TREBEP, además de los más representativos, están legitimados para estar presentes en las Mesas de Negociación los sindicatos que hayan obtenido en las elecciones para Delegados y Juntas de Personal de su ámbito:",
  ["El 10 por 100 o más de los representantes.", "El 15 por 100 o más de los representantes.", "El 5 por 100 o más de los votos.", "La mayoría absoluta de los representantes."],
  "Art. 33.1 TREBEP.", "los sindicatos que hayan obtenido el 10 por 100 o más de los representantes en las elecciones para Delegados y Juntas de Personal"),
 ("TREBEP", "Artículo 34", "Negociación colectiva", "Según el artículo 34.4 del TREBEP, las Mesas Sectoriales podrán constituirse:",
  ["Dependiendo de las Mesas Generales de Negociación y por acuerdo de las mismas.", "Por decisión unilateral de cada Departamento ministerial.", "Por acuerdo de las Juntas de Personal del sector.", "Por resolución de la Secretaría de Estado de Función Pública, sin necesidad de acuerdo."],
  "Art. 34.4 TREBEP.", "Dependiendo de las Mesas Generales de Negociación y por acuerdo de las mismas podrán constituirse Mesas Sectoriales"),
 ("TREBEP", "Artículo 34", "Negociación colectiva", "Según el artículo 34.6 del TREBEP, a falta de acuerdo sobre la fecha, el proceso de negociación se iniciará en el plazo máximo de:",
  ["Un mes desde que la mayoría de una de las partes legitimadas lo promueva.", "Quince días desde que cualquiera de las partes lo promueva.", "Dos meses desde que la mayoría de una de las partes legitimadas lo promueva.", "Diez días hábiles desde la constitución de la Mesa."],
  "Art. 34.6 TREBEP.", "el proceso se iniciará en el plazo máximo de un mes desde que la mayoría de una de las partes legitimadas lo promueva"),
 ("TREBEP", "Artículo 35", "Negociación colectiva", "Según el artículo 35.1 del TREBEP, las Mesas quedan válidamente constituidas cuando las organizaciones sindicales representen, como mínimo:",
  ["La mayoría absoluta de los miembros de los órganos unitarios de representación en el ámbito de que se trate.", "Dos tercios de los miembros de los órganos unitarios de representación.", "La mayoría simple de los votos emitidos en las últimas elecciones.", "El 10 por 100 de los representantes del ámbito."],
  "Art. 35.1 TREBEP.", "como mínimo, la mayoría absoluta de los miembros de los órganos unitarios de representación en el ámbito de que se trate"),
 ("TREBEP", "Artículo 35", "Negociación colectiva", "Según el artículo 35.4 del TREBEP, en la composición numérica de las Mesas ninguna de las partes podrá superar el número de:",
  ["Quince miembros.", "Doce miembros.", "Veinte miembros.", "Nueve miembros."],
  "Art. 35.4 TREBEP.", "sin que ninguna de las partes pueda superar el número de quince miembros"),
 ("TREBEP", "Artículo 36", "Negociación colectiva", "Según el artículo 36.1 del TREBEP, la Mesa General de Negociación de las Administraciones Públicas estará presidida por:",
  ["La Administración General del Estado.", "La Federación Española de Municipios y Provincias.", "La Comunidad Autónoma que ostente la presidencia rotatoria.", "El sindicato más representativo a nivel estatal."],
  "Art. 36.1 TREBEP.", "estará presidida por la Administración General del Estado"),
 ("TREBEP", "Artículo 36", "Negociación colectiva", "Según el artículo 36.2 del TREBEP, será específicamente objeto de negociación en la Mesa General de Negociación de las Administraciones Públicas:",
  ["El incremento global de las retribuciones del personal al servicio de las Administraciones Públicas que corresponda incluir en el Proyecto de Ley de Presupuestos Generales del Estado de cada año.", "La oferta de empleo público de la Administración General del Estado.", "El calendario laboral de cada Departamento ministerial.", "Las retribuciones complementarias de los funcionarios de cada Comunidad Autónoma."],
  "Art. 36.2 TREBEP.", "el incremento global de las retribuciones del personal al servicio de las Administraciones Públicas que corresponda incluir en el Proyecto de Ley de Presupuestos Generales del Estado de cada año"),
 ("TREBEP", "Artículo 37", "Materias de negociación", "Según el artículo 37.2 del TREBEP, ¿cuál de las siguientes materias queda excluida de la obligatoriedad de la negociación?",
  ["La determinación de condiciones de trabajo del personal directivo.", "Los criterios generales de acción social.", "Los planes de Previsión Social Complementaria.", "Las propuestas sobre derechos sindicales y de participación."],
  "Art. 37.2 c) TREBEP. Las demás son negociables (37.1 i, e y h).", "c) La determinación de condiciones de trabajo del personal directivo"),
 ("TREBEP", "Artículo 37", "Materias de negociación", "Según el artículo 37.2 d) del TREBEP, queda excluida de la obligatoriedad de la negociación:",
  ["Los poderes de dirección y control propios de la relación jerárquica.", "Los criterios generales de los planes y fondos para la formación y la promoción interna.", "Las referidas a calendario laboral, horarios, jornadas, vacaciones y permisos.", "Las que así se establezcan en la normativa de prevención de riesgos laborales."],
  "Art. 37.2 d) TREBEP. Las demás son negociables (37.1 f, m y j).", "d) Los poderes de dirección y control propios de la relación jerárquica"),
 ("TREBEP", "Artículo 37", "Materias de negociación", "Según el artículo 37.2 a) del TREBEP, cuando las decisiones de las Administraciones que afecten a sus potestades de organización tengan repercusión sobre condiciones de trabajo de los funcionarios:",
  ["Procederá la negociación de dichas condiciones con las organizaciones sindicales.", "No procederá en ningún caso la negociación.", "Bastará con informar a las Juntas de Personal.", "Procederá la negociación de la propia decisión organizativa."],
  "Art. 37.2 a), párrafo segundo, TREBEP: se negocian las **condiciones**, no la decisión organizativa.", "procederá la negociación de dichas condiciones con las organizaciones sindicales a que se refiere este Estatuto"),
 ("TREBEP", "Artículo 37", "Materias de negociación", "Según el artículo 37.1 del TREBEP, ¿cuál de las siguientes es materia objeto de negociación?",
  ["Las normas que fijen los criterios generales en materia de acceso, carrera, provisión, sistemas de clasificación de puestos de trabajo, y planes e instrumentos de planificación de recursos humanos.", "La regulación y determinación concreta, en cada caso, de los sistemas, criterios, órganos y procedimientos de acceso al empleo público.", "Las decisiones de las Administraciones Públicas que afecten a sus potestades de organización.", "El procedimiento de formación de los actos y disposiciones administrativas."],
  "Art. 37.1 c) TREBEP. Las demás están excluidas (37.2 e, a y b).", "c) Las normas que fijen los criterios generales en materia de acceso, carrera, provisión, sistemas de clasificación de puestos de trabajo, y planes e instrumentos de planificación de recursos humanos"),
 ("TREBEP", "Artículo 38", "Pactos y Acuerdos", "Según el artículo 38.3 del TREBEP, para la validez y eficacia de los Acuerdos será necesaria:",
  ["Su aprobación expresa y formal por los órganos de gobierno de las Administraciones Públicas.", "Su publicación en el Boletín Oficial del Estado, sin necesidad de aprobación.", "Su firma por todas las organizaciones sindicales presentes en la Mesa.", "Su ratificación por las Cortes Generales en todo caso."],
  "Art. 38.3 TREBEP.", "Para su validez y eficacia será necesaria su aprobación expresa y formal por estos órganos"),
 ("TREBEP", "Artículo 38", "Pactos y Acuerdos", "Según el artículo 38.2 del TREBEP, los Pactos:",
  ["Se celebrarán sobre materias que se correspondan estrictamente con el ámbito competencial del órgano administrativo que lo suscriba y se aplicarán directamente al personal del ámbito correspondiente.", "Versarán sobre materias competencia de los órganos de gobierno y necesitarán su aprobación expresa y formal.", "Solo tendrán eficacia una vez convalidados por el Congreso de los Diputados.", "Se aplicarán solo al personal laboral."],
  "Art. 38.2 TREBEP. Las materias competencia de los órganos de gobierno, con aprobación expresa y formal, son las de los Acuerdos (38.3).", "Los Pactos se celebrarán sobre materias que se correspondan estrictamente con el ámbito competencial del órgano administrativo que lo suscriba y se aplicarán directamente"),
 ("TREBEP", "Artículo 38", "Pactos y Acuerdos", "Según el artículo 38.11 del TREBEP, salvo acuerdo en contrario, los Pactos y Acuerdos:",
  ["Se prorrogarán de año en año si no mediara denuncia expresa de una de las partes.", "Se extinguirán al término de su vigencia sin posibilidad de prórroga.", "Se prorrogarán por periodos de dos años si no mediara denuncia expresa.", "Se prorrogarán indefinidamente hasta que se firme otro que los sustituya."],
  "Art. 38.11 TREBEP.", "Salvo acuerdo en contrario, los Pactos y Acuerdos se prorrogarán de año en año si no mediara denuncia expresa de una de las partes"),
 ("TREBEP", "Artículo 38", "Pactos y Acuerdos", "Según el artículo 38.7 del TREBEP, si no se produce acuerdo en la negociación y se agotan, en su caso, los procedimientos de solución extrajudicial de conflictos, corresponderá establecer las condiciones de trabajo de los funcionarios a:",
  ["Los órganos de gobierno de las Administraciones Públicas.", "Un árbitro designado por la Inspección de Trabajo.", "La Mesa Sectorial correspondiente.", "Los tribunales del orden social."],
  "Art. 38.7 TREBEP.", "corresponderá a los órganos de gobierno de las Administraciones Públicas establecer las condiciones de trabajo de los funcionarios"),
 ("TREBEP", "Artículo 45", "Negociación colectiva", "Según el artículo 45.3 del TREBEP, en los sistemas de solución extrajudicial de conflictos colectivos la mediación:",
  ["Será obligatoria cuando lo solicite una de las partes.", "Será siempre voluntaria para ambas partes.", "Será obligatoria solo si lo solicitan ambas partes.", "Será vinculante para las partes en todo caso."],
  "Art. 45.3 TREBEP: obligatoria a petición de una parte; sus propuestas pueden aceptarse o rechazarse libremente.", "La mediación será obligatoria cuando lo solicite una de las partes"),
 ("TREBEP", "Artículo 39", "Representación", "Según el artículo 39.2 del TREBEP, en las unidades electorales donde el número de funcionarios sea igual o superior a 6 e inferior a 50, la representación corresponderá a:",
  ["Los Delegados de Personal.", "Las Juntas de Personal.", "Los Comités de Empresa.", "Los Delegados Sindicales."],
  "Art. 39.2 TREBEP.", "En las unidades electorales donde el número de funcionarios sea igual o superior a 6 e inferior a 50, su representación corresponderá a los Delegados de Personal"),
 ("TREBEP", "Artículo 39", "Representación", "Según el artículo 39.2 del TREBEP, en una unidad electoral de 40 funcionarios se elegirán:",
  ["Tres Delegados de Personal.", "Un Delegado de Personal.", "Una Junta de Personal de cinco miembros.", "Dos Delegados de Personal."],
  "Art. 39.2 TREBEP: hasta 30, un Delegado; de 31 a 49, tres.", "de 31 a 49 se elegirán tres"),
 ("TREBEP", "Artículo 39", "Representación", "Según el artículo 39.6 del TREBEP, el reglamento de procedimiento de las Juntas de Personal y sus modificaciones deberán ser aprobados por los votos favorables de, al menos:",
  ["Dos tercios de sus miembros.", "La mayoría absoluta de sus miembros.", "Tres quintos de sus miembros.", "La mayoría simple de los asistentes."],
  "Art. 39.6 TREBEP.", "deberán ser aprobados por los votos favorables de, al menos, dos tercios de sus miembros"),
 ("TREBEP", "Artículo 40", "Representación", "Según el artículo 40.1 c) del TREBEP, las Juntas de Personal y los Delegados de Personal tienen la función de ser informados de:",
  ["Todas las sanciones impuestas por faltas muy graves.", "Todas las sanciones impuestas, cualquiera que sea su gravedad.", "Las sanciones impuestas por faltas graves y muy graves.", "Solo las sanciones de separación del servicio."],
  "Art. 40.1 c) TREBEP.", "c) Ser informados de todas las sanciones impuestas por faltas muy graves"),
 ("TREBEP", "Artículo 41", "Representación", "Según el artículo 41.1 d) del TREBEP, en una unidad electoral de hasta 100 funcionarios, el crédito de horas mensuales de los representantes es de:",
  ["15 horas.", "20 horas.", "10 horas.", "40 horas."],
  "Art. 41.1 d) TREBEP: hasta 100 funcionarios, 15; de 751 en adelante, 40.", "Hasta 100 funcionarios: 15"),
 ("TREBEP", "Artículo 41", "Representación", "Según el artículo 41.1 e) del TREBEP, los miembros de las Juntas de Personal y los Delegados de Personal no podrán ser trasladados ni sancionados por causas relacionadas con el ejercicio de su mandato:",
  ["Ni durante su vigencia ni en el año siguiente a su extinción, salvo extinción por revocación o dimisión.", "Durante su vigencia y los dos años siguientes, en todo caso.", "Solo durante su vigencia.", "Durante su vigencia y los seis meses siguientes, salvo dimisión."],
  "Art. 41.1 e) TREBEP.", "ni durante la vigencia del mismo, ni en el año siguiente a su extinción, exceptuando la extinción que tenga lugar por revocación o dimisión"),
 ("TREBEP", "Artículo 43", "Representación", "Según el artículo 43.1 e) del TREBEP, también pueden promover la celebración de elecciones a Delegados y Juntas de Personal:",
  ["Los funcionarios de la unidad electoral, por acuerdo mayoritario.", "Cualquier funcionario de la unidad electoral, individualmente.", "El órgano competente en materia de personal de la unidad electoral.", "Las asociaciones profesionales de funcionarios."],
  "Art. 43.1 e) TREBEP.", "e) Los funcionarios de la unidad electoral, por acuerdo mayoritario"),
 ("TREBEP", "Artículo 44", "Representación", "Según el artículo 44 d) del TREBEP, las Juntas de Personal se elegirán mediante:",
  ["Listas cerradas a través de un sistema proporcional corregido.", "Listas abiertas y sistema mayoritario.", "Listas cerradas y sistema mayoritario.", "Listas abiertas y sistema proporcional puro."],
  "Art. 44 d) TREBEP. Las listas abiertas y el sistema mayoritario son para los Delegados de Personal.", "Las Juntas de Personal se elegirán mediante listas cerradas a través de un sistema proporcional corregido"),
 ("TREBEP", "Artículo 46", "Representación", "Según el artículo 46.1 d) del TREBEP, los empleados públicos están legitimados para convocar una reunión en número no inferior al:",
  ["40 por 100 del colectivo convocado.", "33 por 100 del colectivo convocado.", "25 por 100 del colectivo convocado.", "50 por 100 del colectivo convocado."],
  "Art. 46.1 d) TREBEP.", "en número no inferior al 40 por 100 del colectivo convocado"),
 ("CE", "Artículo 28", "Huelga", "Según el artículo 28.2 de la Constitución, la ley que regule el ejercicio del derecho de huelga establecerá las garantías precisas para asegurar:",
  ["El mantenimiento de los servicios esenciales de la comunidad.", "El funcionamiento de todos los servicios públicos.", "La prestación de los servicios mínimos fijados por el empresario.", "La continuidad de la actividad de las Administraciones Públicas."],
  "Art. 28.2 CE.", "las garantías precisas para asegurar el mantenimiento de los servicios esenciales de la comunidad"),
 ("RDL17", "Artículo tres", "Huelga", "Según el artículo 3 del Real Decreto-ley 17/1977, la comunicación de huelga deberá hacerse por escrito y notificada con una antelación mínima a su fecha de iniciación de:",
  ["Cinco días naturales.", "Diez días naturales.", "Cinco días hábiles.", "Quince días naturales."],
  "Art. 3.3 RDL 17/1977. Diez días naturales es el preaviso en empresas de servicios públicos (art. 4).", "notificada con cinco días naturales de antelación, al menos"),
 ("RDL17", "Artículo cuatro", "Huelga", "Según el artículo 4 del Real Decreto-ley 17/1977, cuando la huelga afecte a empresas encargadas de cualquier clase de servicios públicos, el preaviso habrá de ser, al menos, de:",
  ["Diez días naturales.", "Cinco días naturales.", "Quince días hábiles.", "Un mes."],
  "Art. 4 RDL 17/1977.", "habrá de ser, al menos, de diez días naturales"),
 ("RDL17", "Artículo cinco", "Huelga", "Según el artículo 5 del Real Decreto-ley 17/1977, la composición del comité de huelga no podrá exceder de:",
  ["Doce personas.", "Quince personas.", "Nueve personas.", "Veinte personas."],
  "Art. 5 RDL 17/1977.", "La composición del comité de huelga no podrá exceder de doce personas"),
 ("RDL17", "Artículo seis", "Huelga", "Según el artículo 6.2 del Real Decreto-ley 17/1977, durante la huelga:",
  ["Se entenderá suspendido el contrato de trabajo y el trabajador no tendrá derecho al salario.", "Se extingue la relación de trabajo.", "El trabajador conserva el derecho al salario si la huelga es legal.", "El contrato se suspende, pero el trabajador percibe el 50 por 100 del salario."],
  "Art. 6.2 RDL 17/1977.", "Durante la huelga se entenderá suspendido el contrato de trabajo y el trabajador no tendrá derecho al salario"),
 ("RDL17", "Artículo siete", "Huelga", "Según el artículo 7.2 del Real Decreto-ley 17/1977, se considerarán actos ilícitos o abusivos:",
  ["Las huelgas rotatorias y las de celo o reglamento.", "Las huelgas convocadas por los representantes de los trabajadores.", "Las huelgas en empresas de servicios públicos.", "Las huelgas comunicadas con diez días de preaviso."],
  "Art. 7.2 RDL 17/1977.", "Las huelgas rotatorias"),
 ("RDL17", "Artículo ocho", "Huelga", "Según el artículo 8.2 del Real Decreto-ley 17/1977, el pacto que ponga fin a la huelga tendrá:",
  ["La misma eficacia que lo acordado en Convenio Colectivo.", "La eficacia de un laudo arbitral obligatorio.", "Eficacia solo entre los firmantes del comité de huelga.", "Eficacia una vez homologado por la Inspección de Trabajo."],
  "Art. 8.2 RDL 17/1977.", "El pacto que ponga fin a la huelga tendrá la misma eficacia que lo acordado en Convenio Colectivo"),
 ("RDL17", "Artículo once", "Huelga", "Según el artículo 11 del Real Decreto-ley 17/1977, la huelga es ilegal:",
  ["Cuando se inicie o se sostenga por motivos políticos o con cualquier otra finalidad ajena al interés profesional de los trabajadores afectados.", "Cuando afecte a empresas encargadas de servicios públicos.", "Cuando la convoque directamente la plantilla del centro de trabajo.", "Cuando su preaviso sea superior a diez días."],
  "Art. 11 a) RDL 17/1977.", "a) Cuando se inicie o se sostenga por motivos políticos o con cualquier otra finalidad ajena al interés profesional de los trabajadores afectados"),
 ("TREBEP", "Artículo 30", "Huelga", "Según el artículo 30.2 del TREBEP, la deducción de haberes a quienes ejerciten el derecho de huelga:",
  ["No tendrá carácter de sanción ni afectará al régimen respectivo de sus prestaciones sociales.", "Tendrá carácter de sanción disciplinaria leve.", "Afectará al cómputo de sus prestaciones sociales.", "Solo procederá si la huelga es declarada ilegal."],
  "Art. 30.2 TREBEP.", "sin que la deducción de haberes que se efectúe tenga carácter de sanción, ni afecte al régimen respectivo de sus prestaciones sociales"),
 ("TREBEP", "Artículo 95", "Huelga", "Según el artículo 95.2 del TREBEP, el incumplimiento de la obligación de atender los servicios esenciales en caso de huelga es una falta:",
  ["Muy grave.", "Grave.", "Leve.", "Grave o muy grave, según lo establezca el convenio colectivo."],
  "Art. 95.2 m) TREBEP.", "m) El incumplimiento de la obligación de atender los servicios esenciales en caso de huelga"),
]
for k_, a_, cat, enun, ops, ex, fr in Q: T.q(k_, a_, cat, enun, ops, ex, [fr])
T.real("L", 76, "Materias de negociación"); T.real("X", 84, "Materias de negociación"); T.real("X", 83, "Representación"); T.real("L", 75, "Representación")

# Flashcards
for q_, a_, cat in [
  ("Derechos individuales ejercidos colectivamente (TREBEP, art. 15)", "Libertad sindical; negociación colectiva y participación en las condiciones de trabajo; huelga, con garantía de los servicios esenciales; conflictos colectivos; reunión (art. 46).", "Derechos colectivos"),
  ("Negociación colectiva, representación y participación institucional (art. 31)", "Negociar condiciones de trabajo; elegir representantes y constituir órganos unitarios; participar, a través de los sindicatos, en órganos de control y seguimiento.", "Derechos colectivos"),
  ("¿Quién puede recurrir las resoluciones de los órganos de selección? (art. 31.6)", "Las organizaciones sindicales más representativas en el ámbito de la Función Pública.", "Derechos colectivos"),
  ("Exclusiones de la libertad sindical (LOLS, art. 1)", "Exceptuados: Fuerzas Armadas e Institutos Armados de carácter militar. Jueces, Magistrados y Fiscales en activo: no pueden afiliarse. Cuerpos y Fuerzas de Seguridad civiles: normativa específica.", "Libertad sindical"),
  ("Sindicato más representativo estatal y autonómico (LOLS, arts. 6 y 7)", "Estatal: 10 % o más. Comunidad Autónoma: al menos 15 % y mínimo de 1.500 representantes.", "Libertad sindical"),
  ("Principios de la negociación colectiva (art. 33.1)", "Legalidad, cobertura presupuestaria, obligatoriedad, buena fe negocial, publicidad y transparencia.", "Negociación colectiva"),
  ("Mesas Sectoriales (art. 34.4)", "Dependen de las Mesas Generales y se constituyen por acuerdo de estas.", "Negociación colectiva"),
  ("Válida constitución de una Mesa (art. 35.1)", "Sindicatos que representen, como mínimo, la mayoría absoluta de los miembros de los órganos unitarios del ámbito.", "Negociación colectiva"),
  ("Máximo de miembros por parte en las Mesas (art. 35.4)", "Quince.", "Negociación colectiva"),
  ("Mesa General de Negociación de las Administraciones Públicas (art. 36.1 y 2)", "Presidida por la AGE, con CC. AA., Ceuta y Melilla y FEMP; negocia el incremento global de retribuciones del Proyecto de Ley de Presupuestos.", "Negociación colectiva"),
  ("Materias excluidas de la negociación (art. 37.2)", "Potestades de organización; derechos de ciudadanos y usuarios y procedimiento de formación de actos y disposiciones; personal directivo; poderes de dirección y control; regulación concreta del acceso y la promoción profesional.", "Materias de negociación"),
  ("Pactos y Acuerdos (art. 38.2 y 3)", "Pactos: órgano administrativo, aplicación directa. Acuerdos: órganos de gobierno, aprobación expresa y formal.", "Pactos y Acuerdos"),
  ("Prórroga de Pactos y Acuerdos (art. 38.11)", "De año en año si no media denuncia expresa, salvo acuerdo en contrario.", "Pactos y Acuerdos"),
  ("Mediación y arbitraje (art. 45.3)", "Mediación obligatoria si la pide una parte (propuestas libres); arbitraje voluntario y vinculante.", "Negociación colectiva"),
  ("Delegados y Juntas de Personal (art. 39)", "Delegados: 6 a 49 funcionarios (1 hasta 30; 3 de 31 a 49). Juntas: 50 o más; máximo 75.", "Representación"),
  ("Mandato de los representantes de los funcionarios (art. 42)", "Cuatro años, pudiendo ser reelegidos; se prorroga si no se promueven nuevas elecciones.", "Representación"),
  ("Crédito de horas (art. 41.1 d)", "15 horas (hasta 100 funcionarios), 20, 30, 35 y 40 (751 en adelante).", "Representación"),
  ("Sistema electoral de Juntas y Delegados (art. 44 d)", "Juntas: listas cerradas y proporcional corregido. Delegados: listas abiertas y mayoritario.", "Representación"),
  ("Representación unitaria del personal laboral del IV Convenio (art. 85)", "Delegados y Delegadas de personal (menos de 50) y Comités de empresa (50 o más).", "Representación"),
  ("Preaviso de huelga (RDL 17/1977, arts. 3 y 4)", "Cinco días naturales; diez en empresas de servicios públicos.", "Huelga"),
  ("Efectos de la huelga en el contrato (RDL 17/1977, art. 6)", "Contrato suspendido, sin salario, alta especial en la Seguridad Social sin cotización.", "Huelga"),
  ("Huelga y retribuciones del empleado público (TREBEP, art. 30.2)", "No devenga ni percibe las retribuciones de ese tiempo; la deducción no es sanción ni afecta a sus prestaciones sociales.", "Huelga"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Negociación colectiva", "Derecho a negociar la determinación de condiciones de trabajo de los empleados de la Administración Pública (TREBEP, art. 31.2).", "s3", "Conceptos")
T.glos("Representación", "Facultad de elegir representantes y constituir órganos unitarios para la interlocución entre las Administraciones y sus empleados (TREBEP, art. 31.3).", "s3", "Conceptos")
T.glos("Participación institucional", "Derecho a participar, a través de las organizaciones sindicales, en los órganos de control y seguimiento de las entidades u organismos que legalmente se determine (TREBEP, art. 31.4).", "s3", "Conceptos")
T.glos("Sindicato más representativo", "El que alcanza la audiencia electoral de los arts. 6 (10 % estatal) o 7 (15 % y 1.500 representantes autonómico) de la LO 11/1985; tiene capacidad de participación institucional y de acción sindical.", "s4", "Libertad sindical")
T.glos("Mesa General de Negociación", "Mesa de negociación de las condiciones de trabajo comunes a los funcionarios de su ámbito (AGE, CC. AA., Ceuta y Melilla y EE. LL.) (TREBEP, art. 34).", "s6", "Negociación colectiva")
T.glos("Mesa Sectorial", "Mesa que depende de la General y se crea por acuerdo de esta, por las condiciones específicas de un sector (TREBEP, art. 34.4 y 5).", "s6", "Negociación colectiva")
T.glos("Pacto", "Resultado de la negociación sobre materias del ámbito competencial del órgano administrativo que lo suscribe; se aplica directamente (TREBEP, art. 38.2).", "s8", "Pactos y Acuerdos")
T.glos("Acuerdo", "Resultado de la negociación sobre materias de los órganos de gobierno; necesita su aprobación expresa y formal (TREBEP, art. 38.3).", "s8", "Pactos y Acuerdos")
T.glos("Delegado de Personal", "Órgano de representación de los funcionarios en unidades electorales de 6 a 49 funcionarios (TREBEP, art. 39.2).", "s10", "Representación")
T.glos("Junta de Personal", "Órgano colegiado de representación de los funcionarios en unidades electorales de 50 o más funcionarios (TREBEP, art. 39.3).", "s10", "Representación")
T.glos("Comité de empresa", "Órgano representativo y colegiado de los trabajadores en centros de 50 o más trabajadores (ET, art. 63.1; IV Convenio Único, art. 85).", "s10", "Representación")
T.glos("Comité de huelga", "Órgano de los huelguistas, de doce personas como máximo, que participa en las actuaciones para la solución del conflicto (RDL 17/1977, art. 5).", "s15", "Huelga")
T.glos("Servicios esenciales de la comunidad", "Los que la ley que regule la huelga debe garantizar (CE, art. 28.2); no atenderlos en caso de huelga es falta muy grave del empleado público (TREBEP, art. 95.2 m).", "s14", "Huelga")

# Cronología (fechas de los metadatos del BOE)
T.hito("1977", "Real Decreto-ley 17/1977, de 4 de marzo, sobre relaciones de trabajo (BOE de 9-3-1977)", "Título I: el derecho de huelga", "normativo", "s15")
T.hito("1978", "Constitución Española (27-12-1978; BOE de 29-12-1978)", "Arts. 7, 28 y 37: sindicatos, libertad sindical, huelga y negociación colectiva", "normativo", "s1")
T.hito("1981", "STC 11/1981, de 8 de abril (BOE de 25-4-1981, según el texto consolidado del RDL 17/1977)", "Declara inconstitucionales varios incisos del RDL 17/1977 (arts. 3, 5, 6, 10 y 11)", "jurisprudencia", "s17")
T.hito("1985", "Ley Orgánica 11/1985, de 2 de agosto, de Libertad Sindical (BOE de 8-8-1985)", "Libertad sindical de los funcionarios y sindicatos más representativos", "normativo", "s4")
T.hito("2015", "Real Decreto Legislativo 5/2015, de 30 de octubre, TREBEP (BOE de 31-10-2015)", "Arts. 31 a 46: negociación colectiva, representación y participación institucional", "normativo", "s3")
T.hito("2019", "IV Convenio colectivo único del personal laboral de la AGE (Resolución de 13-5-2019; BOE de 17-5-2019)", "Art. 85: representación unitaria del personal laboral", "normativo", "s10")

T.publicar()
