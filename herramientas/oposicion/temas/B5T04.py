# -*- coding: utf-8 -*-
"""Tema V.4 (B5T04): Formas de provisión de puestos de trabajo y movilidad en la
Administración del Estado. Promoción interna y carrera profesional.
Método del I.2: mapa → bloques (I a IV) con guía; cada artículo, texto literal del
BOE + ficha de casillas fijas; cierre 1 (preguntas oficiales) y cierre 2 (repaso).
Normas (textos consolidados del BOE): TREBEP (RDLeg 5/2015), arts. 16 a 19, 78 a 84,
disposición derogatoria única, disposiciones transitoria octava y final cuarta;
Ley 30/1984, art. 20 (párrafos no incluidos en la derogatoria del TREBEP);
Real Decreto 364/1995 (títulos III, IV y V); Real Decreto-ley 6/2023 (libro segundo:
arts. 105, 108, 111, 122, 123, 127 y disposición transitoria sexta)."""
import os, sys
import xml.etree.ElementTree as ET
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO["RD364"] = "RD 364/1995"
CORTO["RDL6"] = "RDL 6/2023"
CORTO["L30"] = "Ley 30/1984"


def tabla(k, bloque):
    """Tabla literal de un bloque del BOE, sacada del XML consolidado (última versión)."""
    raiz = ET.parse(os.path.join(boe.AQUI, k + ".xml")).getroot()
    for b in raiz.iter("bloque"):
        if b.get("id") == bloque:
            t = b.findall("version")[-1].find(".//table")
            filas = [[" ".join("".join(c.itertext()).split()) for c in tr] for tr in t.iter("tr")]
            out = ["| " + " | ".join(filas[0]) + " |", "|" + "---|" * len(filas[0])]
            out += ["| " + " | ".join(f) + " |" for f in filas[1:]]
            return "\n".join(out)
    raise AssertionError(("TABLA NO ENCONTRADA", k, bloque))


T = Tema("B5T04",
  "Cuatro preguntas: I. Qué normas rigen y cuáles son las formas de provisión (TREBEP, art. 78 y disposición final cuarta; RD 364/1995, arts. 1, 26, 36 y 38) · II. Cómo se provee con carácter definitivo: concurso y libre designación (TREBEP, arts. 79 y 80; RD 364/1995, arts. 39 a 58; RDL 6/2023, arts. 111, 123 y 127) · III. Qué otras formas de provisión y movilidad hay (TREBEP, arts. 81 a 84; RD 364/1995, arts. 59 a 69) · IV. Cómo se progresa: carrera profesional y promoción interna (TREBEP, arts. 16 a 19; RDL 6/2023, arts. 108 y 122; RD 364/1995, arts. 70 a 80). Cada artículo: texto literal del BOE y ficha.",
  ["Provisión de puestos", "Concurso", "Concurso específico", "Concurso unitario", "Libre designación", "Personal directivo público", "Redistribución de efectivos", "Reasignación de efectivos", "Comisión de servicios", "Adscripción provisional", "Movilidad", "Carrera profesional", "Carrera horizontal", "Grado personal", "Promoción interna"])

# =============================================================================
T.ap("s0", "Mapa del tema: cuatro preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque V, tema 4):
> Formas de provisión de puestos de trabajo y movilidad en la Administración del Estado. Promoción interna y carrera profesional.

### El hilo conductor

El epígrafe se lee como **cuatro preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | TREBEP | Normas de la Administración del Estado |
|---|---|---|---|
| **I** | ¿Qué normas rigen y cuáles son las formas de provisión? | Art. 78; disposición derogatoria única y disposición final cuarta | RD 364/1995, arts. 1, 26, 36 y 38 |
| **II** | ¿Cómo se provee con carácter definitivo? (concurso y libre designación) | Arts. 79 y 80 | RD 364/1995, arts. 39 a 58; Ley 30/1984, art. 20.1 b) y f); RDL 6/2023, arts. 111, 123 y 127 |
| **III** | ¿Qué otras formas de provisión y movilidad hay? | Arts. 81 a 84; disposición transitoria octava | RD 364/1995, arts. 59 a 69 y 72 |
| **IV** | ¿Cómo se progresa? (carrera profesional y promoción interna) | Arts. 16 a 19 | RDL 6/2023, arts. 108 y 122 y disposición transitoria sexta; RD 364/1995, arts. 70 y 73 a 80 |

!> **La idea que une los cuatro bloques:** el funcionario ocupa un **puesto de trabajo**. Lo obtiene con carácter **definitivo** por **concurso** (el sistema normal) o por **libre designación** (II); puede cambiar de puesto por otras vías, algunas **definitivas** (redistribución, reasignación) y otras **temporales** (comisión de servicios, adscripción provisional) (III); y progresa **sin cambiar de cuerpo** (carrera: grado, tramos, puestos de más nivel) o **cambiando de cuerpo** (promoción interna) (IV).

?> **Aviso de vigencia.** El TREBEP es la norma básica, pero su disposición final cuarta dice que lo establecido en los capítulos II y III del título III, excepto el artículo 25.2 (entre ellos, carrera y promoción, arts. 16 a 20), y en el capítulo III del título V (provisión y movilidad, arts. 78 a 84) **producirá efectos a partir de la entrada en vigor de las leyes de Función Pública** que lo desarrollen (→ I.1.2). Por eso, en la Administración del Estado, el detalle está en el **RD 364/1995**, en los párrafos de la **Ley 30/1984** que no figuran en la derogatoria del TREBEP y en el **libro segundo del RDL 6/2023**. Se citan todos literalmente, como están en el BOE (con las denominaciones de órganos que figuran en su texto: «Ministerio para las Administraciones Públicas», «Gobernador civil»…).

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen; o, para los derechos, Titulares · Contenido · Límites · Protección · ⚠ Ojo en el examen).
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- Fuera de este tema: clases de personal (tema V.1), situaciones administrativas (tema V.5), retribuciones e indemnizaciones (tema V.6), personal laboral (tema V.7), selección y oferta de empleo público (tema V.3), discapacidad (tema V.10).
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué normas rigen y cuáles son las formas de provisión?", donde(
  "Primera pregunta del tema. Antes de estudiar cada procedimiento hay que saber **qué norma se aplica** en la Administración del Estado (el TREBEP tiene efectos diferidos en esta materia) y **cuál es el catálogo** de formas de provisión.",
  ["1 Principios y procedimientos en el TREBEP y sus efectos diferidos (art. 78; disposición final cuarta)", "2 Las formas de provisión en la Administración General del Estado (RD 364/1995, arts. 1, 36, 38 y 26)"]))

T.ap("s1", "I.1 Principios y procedimientos en el TREBEP y sus efectos diferidos (art. 78; disposiciones derogatoria y final cuarta)", f"""
{unidad("1.1 Principios y procedimientos de provisión (TREBEP, art. 78)",
  lit("TREBEP", "Artículo 78", ["igualdad, mérito, capacidad y publicidad", "concurso y de libre designación con convocatoria pública", "otros procedimientos de provisión"]),
  fichab("Reglas básicas de la provisión de puestos del personal funcionario de carrera",
         c("TREBEP", "Artículo 78", "Las Administraciones Públicas"),
         ["::Dos procedimientos ordinarios (78.2):", "Concurso", "Libre designación con convocatoria pública", "**Otros que pueden prever las leyes de Función Pública (78.3):**", "Movilidad del art. 81.2 (traslado por necesidades del servicio)", "Permutas entre puestos", "Movilidad por motivos de salud o rehabilitación", "Reingreso al servicio activo", "Cese o remoción y supresión de puestos"],
         "—",
         "**Cuatro** principios: igualdad, mérito, capacidad **y publicidad**. La libre designación es **con convocatoria pública**."))}

{unidad("1.2 Efectos diferidos del TREBEP y derogación de la Ley 30/1984 (disposición final cuarta y derogatoria única)",
  lit("TREBEP", "dfcuaa", ["en el capítulo III del título V producirá efectos a partir de la entrada en vigor de las leyes de Función Pública", "se mantendrán en vigor en cada Administración Pública las normas vigentes sobre ordenación, planificación y gestión de recursos humanos"], solo=[1, 3], titulo="Disposición final cuarta. Entrada en vigor (TREBEP)"),
  lit("TREBEP", "ddunica-2", ["con el alcance establecido en el apartado 2 de la disposición final cuarta", "20.1.a), b) párrafo primero, c), e) y g) en sus párrafos primero a cuarto, e i), 2 y 3; 21; 22.1 a excepción de los dos últimos párrafos"], solo=[1, 3], titulo="Disposición derogatoria única (TREBEP)"),
  fichab("Cuándo se aplican los artículos del TREBEP de este tema y qué queda de la Ley 30/1984",
         "Cada Administración, con sus **leyes de Función Pública**",
         ["Carrera y promoción (cap. II del título III) y provisión y movilidad (cap. III del título V): efectos **a partir de las leyes de Función Pública** de desarrollo", "Mientras tanto, siguen en vigor las normas vigentes sobre gestión de recursos humanos **en tanto no se opongan** al TREBEP", "La Ley 30/1984 se deroga **con el alcance** de ese apartado 2; de su art. 20, la lista **no incluye** el **20.1 b) párrafo segundo**, la **f)**, la **h)** ni la **g)** desde su párrafo quinto"],
         "—",
         "La excepción del art. **25.2** (trienios de los interinos) no es de este tema. De la Ley 30/1984 se citan en estos apuntes solo párrafos **no incluidos** en la lista de la derogatoria (→ II.2.3 y → II.5.2)."))}
""", 2)

T.ap("s2", "I.2 Las formas de provisión en la Administración General del Estado (RD 364/1995, arts. 1, 36, 38 y 26)", f"""
{unidad("2.1 Ámbito del Reglamento (RD 364/1995, art. 1.1 y 3)",
  lit("RD364", "Artículo 1", ["a la provisión de puestos de trabajo, la promoción interna y la carrera profesional", "carácter supletorio"], solo=[1, 7]),
  fichab("A quién se aplica el Reglamento de ingreso, provisión, promoción y carrera",
         "Funcionarios de la **Administración General del Estado y sus Organismos autónomos** incluidos en la Ley 30/1984",
         ["Regula ingreso, **provisión**, **promoción interna** y **carrera profesional**", "Es **supletorio** para los demás funcionarios civiles del Estado y para los de las restantes Administraciones"],
         "—",
         "Un solo reglamento para **cuatro** materias: ingreso (tema V.3), provisión, promoción interna y carrera (este tema)."))}

{unidad("2.2 Formas de provisión (RD 364/1995, art. 36)",
  lit("RD364", "Artículo 36", ["que es el sistema normal de provisión", "redistribución de efectivos o por reasignación de efectivos", "Temporalmente podrán ser cubiertos mediante comisión de servicios y adscripción provisional"]),
  fichab("Catálogo de formas de provisión en la Administración General del Estado",
         "La Administración, según lo que determinen las **relaciones de puestos de trabajo**",
         ["::Ordinarias (36.1):", "**Concurso** (sistema normal) → II.1 a II.4", "**Libre designación** → II.5", "**Por necesidades del servicio (36.2):**", "Redistribución de efectivos y reasignación de efectivos (Plan de Empleo) → III.2", "**Temporales (36.3):**", "Comisión de servicios y adscripción provisional → III.3"],
         "—",
         "**Temporales**: solo la **comisión de servicios** y la **adscripción provisional**. Cayó en 2025 (→ Cierre 1): el puesto obtenido en comisión de servicios **no** es definitivo."))}

{unidad("2.3 Publicidad de las convocatorias (RD 364/1995, art. 38)",
  lit("RD364", "Artículo 38", ["se publicarán en el «Boletín Oficial del Estado»"]),
  fichab("Régimen de las convocatorias de concurso y libre designación",
         "El órgano convocante",
         "Cada procedimiento se rige por su **convocatoria**, ajustada al Reglamento y a las normas específicas",
         "—",
         "Se publican en el **BOE** las convocatorias **y sus resoluciones**, de concurso y de libre designación; otros diarios oficiales, solo si se estima necesario."))}

{unidad("2.4 El primer destino de los funcionarios de nuevo ingreso (RD 364/1995, art. 26.1)",
  lit("RD364", "Artículo 26", ["según el orden obtenido en el proceso selectivo", "Estos destinos tendrán carácter definitivo"], solo=[1, 2]),
  fichab("Adjudicación del primer puesto tras el proceso selectivo",
         "Los funcionarios de nuevo ingreso",
         "Eligen entre los puestos ofertados **por el orden** obtenido en el proceso selectivo, si reúnen los requisitos de la relación de puestos de trabajo",
         "—",
         "Ese primer destino es **definitivo**, «equivalente a todos los efectos a los obtenidos por concurso»."))}

{resumen([
  "TREBEP: provisión con **igualdad, mérito, capacidad y publicidad**, por **concurso** y **libre designación con convocatoria pública** (art. 78).",
  "Sus arts. 78 a 84 y 16 a 20 producen efectos con las **leyes de Función Pública**; mientras, siguen las normas vigentes que no se opongan (disposición final cuarta).",
  "RD 364/1995: **concurso** (sistema normal) y **libre designación**; redistribución y reasignación de efectivos; **temporalmente**, comisión de servicios y adscripción provisional (art. 36).",
  "Convocatorias y resoluciones, en el **BOE** (art. 38). El primer destino tras la oposición es **definitivo** (art. 26)."],
  "Siguiente: II. ¿Cómo se provee con carácter definitivo? Concurso y libre designación")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Cómo se provee con carácter definitivo? Concurso y libre designación", donde(
  "Segunda pregunta. Los dos procedimientos ordinarios: el **concurso**, que valora méritos y es el sistema normal, y la **libre designación**, que aprecia discrecionalmente la idoneidad. El RDL 6/2023 añade el **concurso unitario abierto y permanente** y reglas propias para el **personal directivo público profesional**.",
  ["1 El concurso en el TREBEP (art. 79)", "2 Convocatoria y participación en el concurso (RD 364/1995, arts. 39 a 42; RDL 6/2023, art. 111)", "3 Méritos, concurso específico y Comisiones de Valoración (arts. 44 a 46)", "4 Resolución, toma de posesión, destinos y remoción (arts. 47 a 50)", "5 La libre designación (TREBEP, art. 80; RD 364/1995, arts. 51 a 58)", "6 El personal directivo público profesional (RDL 6/2023, arts. 123 y 127)"]))

T.ap("s3", "II.1 El concurso en el TREBEP (art. 79)", f"""
{unidad("1.1 Concepto, órganos y garantías del concurso (TREBEP, art. 79)",
  lit("TREBEP", "Artículo 79", ["como procedimiento normal de provisión de puestos de trabajo", "por órganos colegiados de carácter técnico", "principio de profesionalidad y especialización", "criterio de paridad entre mujer y hombre", "el plazo mínimo de ocupación de los puestos obtenidos por concurso", "víctima del terrorismo", "se deberá asignar un puesto de trabajo"]),
  fichab("Procedimiento normal de provisión: valoración de méritos y capacidades",
         c("TREBEP", "Artículo 79", "órganos colegiados de carácter técnico"),
         [f"Valoración de {c('TREBEP', 'Artículo 79', 'los méritos y capacidades y, en su caso, aptitudes de los candidatos')}", "Composición: profesionalidad, especialización y **paridad** entre mujer y hombre; funcionamiento: imparcialidad y objetividad", "Puntuación para víctimas del terrorismo o amenazados: como máximo, la fijada para la **antigüedad** (con informe del **Ministerio del Interior** para protegerlas)", "Supresión o remoción: se asigna un puesto conforme al sistema de carrera"],
         "Plazo mínimo de ocupación para volver a concursar: lo fijan las **leyes de Función Pública** (en la AGE, dos años: → II.2.3)",
         "Es el procedimiento **normal**. Los órganos son **colegiados** y **técnicos** (no unipersonales ni políticos)."))}
""", 2)

T.ap("s4", "II.2 Convocatoria y participación en el concurso (RD 364/1995, arts. 39 a 42; RDL 6/2023, art. 111)", f"""
{unidad("2.1 Quién convoca y qué contiene la convocatoria (RD 364/1995, arts. 39 y 40)",
  lit("RD364", "Artículo 39", ["autorizará las convocatorias de los concursos", "el baremo con arreglo al cual se puntuarán"]),
  lit("RD364", "Artículo 40", ["Cada Ministerio procederá a la convocatoria y a la resolución de los concursos", "podrá convocar concursos unitarios"]),
  fichab("Convocatoria del concurso",
         ["Autoriza: la **Secretaría de Estado para la Administración Pública**, a iniciativa de los Departamentos (39)", "Convoca y resuelve: **cada Ministerio**, para sus puestos y los de sus Organismos autónomos y Entidades Gestoras y Servicios Comunes de la Seguridad Social (40.1)", "Coordina los puestos administrativos y auxiliares de los grupos C y D, y puede convocar concursos unitarios: el Ministerio para las Administraciones Públicas (40.2)"],
         "Bases con denominación, nivel, descripción y localización de los puestos, requisitos, méritos y **baremo**, memorias o entrevistas si las hay y composición de las comisiones de valoración",
         "—",
         "**Autoriza** la Secretaría de Estado; **convoca y resuelve** cada Ministerio."))}

{unidad("2.2 El concurso unitario abierto y permanente (RDL 6/2023, art. 111)",
  lit("RDL6", "Artículo 111", ["concursos unitarios, de carácter abierto y permanente", "fomentar una mayor ocupación de las plazas de necesaria cobertura y de favorecer una movilidad ordenada y coordinada"]),
  fichab("Concurso permanente de la Administración del Estado",
         f"{c('RDL6', 'Artículo 111', 'La Secretaría de Estado de Función Pública')}, en colaboración con los departamentos ministeriales y organismos públicos",
         "Concursos **unitarios**, **abiertos y permanentes**, en los que se podrán incluir puestos vacantes",
         "—",
         "Nombre exacto: **concursos unitarios, de carácter abierto y permanente**. Cayó en 2025 (→ Cierre 1)."))}

{unidad("2.3 Quién puede participar y cuánto hay que permanecer en el puesto (RD 364/1995, art. 41.1 a 3; Ley 30/1984, art. 20.1 f)",
  lit("RD364", "Artículo 41", ["excepto los suspensos en firme", "un mínimo de dos años", "por razones de convivencia familiar"], solo=[1, 2, 3, 4]),
  lit("L30", "aveinte", ["un mínimo de dos años"], solo=[22], titulo="Artículo veinte. Provisión de puestos de trabajo, apartado 1 f) (Ley 30/1984)"),
  fichab("Requisitos para concursar",
         ["Funcionarios **en cualquier situación administrativa**", "Excepto los **suspensos en firme**, mientras dure la suspensión"],
         ["Requisitos referidos a la fecha en que **termina el plazo de solicitudes**", "Sin limitación por Ministerio o municipio, salvo concursos reservados por un Plan de Empleo", "Petición **condicionada** de dos funcionarios por convivencia familiar (mismo municipio)"],
         "Permanencia mínima: **dos años** en el puesto de destino **definitivo**; salvo en el ámbito de una Secretaría de Estado o de un Departamento, remoción del art. 20.1 e) y supresión del puesto",
         "Los dos años no se exigen para concursar **dentro de la misma Secretaría de Estado** (o del Departamento, si no la hay). Al funcionario de promoción interna que sigue en su puesto se le computa el tiempo anterior."))}

{unidad("2.4 Solicitudes (RD 364/1995, art. 42)",
  lit("RD364", "Artículo 42", ["el orden de preferencia", "quince días hábiles"]),
  fichab("Presentación de solicitudes en el concurso",
         "Los participantes, ante el **órgano convocante**",
         "Si se piden varios puestos, con su **orden de preferencia**",
         "**Quince días hábiles** desde el siguiente a la publicación de la convocatoria en el BOE",
         "Concurso y libre designación coinciden: **quince días hábiles** (→ II.5.3). El personal directivo público profesional: **diez días naturales** (→ II.6.2)."))}
""", 2)

T.ap("s5", "II.3 Méritos, concurso específico y Comisiones de Valoración (RD 364/1995, arts. 44 a 46)", f"""
{unidad("3.1 Méritos y su valoración (RD 364/1995, art. 44)",
  lit("RD364", "Artículo 44", ["la posesión de un determinado grado personal, la valoración del trabajo desarrollado, los cursos de formación y perfeccionamiento superados y la antigüedad", "hasta que el hijo cumpla doce años", "hasta el segundo grado inclusive", "del 40 por 100 de la puntuación máxima total ni ser inferior al 10 por 100", "fecha del cierre del plazo de presentación de instancias", "una puntuación mínima para la adjudicación de destino"]),
  fichab("Qué se valora en el concurso",
         "La Comisión de Valoración (→ II.3.3), con el baremo de la convocatoria",
         ["::Méritos generales (44.1):", "Méritos **específicos** adecuados al puesto (solo los de la convocatoria)", "**Grado personal** consolidado (siempre en sentido positivo)", "**Trabajo desarrollado**", "**Cursos** de formación y perfeccionamiento (solo los incluidos en la convocatoria)", "**Antigüedad** (por años de servicios)", "**Puntuación por conciliación (44.2), como máximo la de la antigüedad:**", "Destino previo del **cónyuge** funcionario en el municipio", "Cuidado de **hijos** hasta que cumplan **doce** años", "Cuidado de un **familiar** hasta el **segundo grado**"],
         "Cada concepto: **ni más del 40 %** de la puntuación máxima total **ni menos del 10 %**; méritos referidos al **cierre del plazo** de instancias; **puntuación mínima** obligatoria para adjudicar",
         "Empate: méritos del 44.1 **por su orden**; después, fecha de **ingreso** en el Cuerpo o Escala; por último, número obtenido en el proceso selectivo. Cuidado de familiar e hijos: **incompatibles** entre sí."))}

{unidad("3.2 Concurso específico en dos fases (RD 364/1995, art. 45)",
  lit("RD364", "Artículo 45", ["los concursos podrán constar de dos fases", "elaboración de memorias o la celebración de entrevistas", "debiendo desecharse a estos efectos la máxima y la mínima", "sumados los resultados finales de las dos fases"]),
  fichab("Concurso con fase de méritos específicos",
         "La convocatoria lo decide **en atención a la naturaleza de los puestos**",
         ["1.ª fase: méritos generales (grado, trabajo desarrollado, cursos y antigüedad)", "2.ª fase: méritos **específicos** del puesto; puede haber **memoria** o **entrevista**", "La convocatoria fija puntuaciones **máximas y mínimas** de las dos fases"],
         "Puntuación: **media aritmética** de los miembros de la Comisión, desechando la **máxima y la mínima**",
         "Propuesta: el candidato con **mayor puntuación sumadas las dos fases**. Memoria y entrevista deben estar **en la convocatoria**."))}

{unidad("3.3 Comisiones de Valoración (RD 364/1995, art. 46)",
  lit("RD364", "Artículo 46", ["como mínimo por cuatro miembros", "más del diez por ciento de representantes", "no podrá ser igual o superior", "Grupo de titulación igual o superior", "con voz pero sin voto", "al candidato que haya obtenido mayor puntuación"]),
  fichab("Órgano que valora los méritos",
         ["Al menos **cuatro** miembros designados por la autoridad convocante", "Organizaciones sindicales **más representativas** y las de **más del 10 %** de representantes: derecho a participar", "Presidente y Secretario: entre los designados por la **Administración**", "Asesores expertos: **con voz pero sin voto**"],
         "Propone al candidato con **mayor puntuación**",
         "Representantes sindicales: **menos** que los miembros designados a propuesta de la Administración",
         "Miembros de **grupo igual o superior** al exigido para los puestos; en el concurso específico, además, **grado o puesto de nivel igual o superior**."))}
""", 2)

T.ap("s6", "II.4 Resolución, toma de posesión, destinos y remoción (RD 364/1995, arts. 47 a 50)", f"""
{unidad("4.1 Resolución del concurso (RD 364/1995, art. 47)",
  lit("RD364", "Artículo 47", ["dos meses", "La resolución del concurso se motivará"]),
  fichab("Plazo y motivación de la resolución",
         "El órgano convocante",
         "Resolución **motivada** con referencia a las normas y bases; deben constar la observancia del procedimiento y la **valoración final** de los méritos",
         "**Dos meses** desde el día siguiente al fin del plazo de solicitudes, salvo que la convocatoria fije otro",
         "Libre designación: **un mes**, prorrogable otro (→ II.5.3)."))}

{unidad("4.2 Cese y toma de posesión (RD 364/1995, art. 48)",
  lit("RD364", "Artículo 48", ["tres días hábiles si no implica cambio de residencia del funcionario, o de un mes si comporta cambio de residencia o el reingreso al servicio activo", "hasta veinte días hábiles", "hasta un máximo de tres meses", "prórroga de incorporación hasta un máximo de veinte días hábiles"]),
  fichab("Plazos para incorporarse al nuevo destino",
         ["**Subsecretario** del Departamento de origen: puede diferir el cese **hasta 20 días hábiles**", "**Secretaría de Estado para la Administración Pública**: puede aplazarlo hasta **tres meses** (incluida esa prórroga)", "**Subsecretario** del Departamento de destino: prórroga de incorporación de **hasta 20 días hábiles** si hay cambio de residencia"],
         "El cese se produce dentro de los **tres días hábiles** siguientes a la publicación de la resolución en el BOE; la toma de posesión se cuenta desde el día siguiente al cese",
         ["Toma de posesión: **3 días hábiles** sin cambio de residencia", "**Un mes** con cambio de residencia o reingreso al servicio activo"],
         "El plazo posesorio cuenta como **servicio activo**, salvo reingreso desde excedencia voluntaria o por cuidado de hijos pasado el primer año."))}

{unidad("4.3 Destinos irrenunciables y voluntarios (RD 364/1995, art. 49)",
  lit("RD364", "Artículo 49", ["serán irrenunciables", "se considerarán de carácter voluntario"]),
  fichab("Naturaleza de los destinos obtenidos",
         "El funcionario adjudicatario",
         ["**Irrenunciables**, salvo que antes de acabar el plazo de toma de posesión obtenga otro destino por convocatoria pública", "**Voluntarios**: no generan indemnización, salvo las excepciones del régimen de indemnizaciones (tema V.6)"],
         "—",
         "Única salida a la irrenunciabilidad: **otro destino por convocatoria pública** antes de la toma de posesión."))}

{unidad("4.4 Remoción del puesto obtenido por concurso (RD 364/1995, art. 50)",
  lit("RD364", "Artículo 50", ["alteración en el contenido del puesto", "rendimiento insuficiente, que no comporte inhibición", "diez días hábiles", "Junta de Personal", "no inferior en más de dos niveles al de su grado personal"]),
  fichab("Pérdida del puesto obtenido por concurso por causas sobrevenidas",
         ["Propuesta motivada: titular del **centro directivo**, Delegado del Gobierno o Gobernador civil", "Parecer: **Junta de Personal**", "Resuelve: la autoridad que hizo el **nombramiento**"],
         ["::Causas:", "**Alteración del contenido** del puesto en la relación de puestos de trabajo que modifique los supuestos de la convocatoria", "**Falta de capacidad** manifestada por **rendimiento insuficiente** que no comporte inhibición"],
         ["Alegaciones del interesado: **10 días hábiles**", "Parecer de la Junta de Personal: **10 días hábiles**", "Notificación de la resolución: **10 días hábiles**"],
         "La resolución **pone fin a la vía administrativa**. Al removido se le da un puesto **provisional** de su Cuerpo o Escala, en el **mismo municipio**, **no inferior en más de dos niveles** a su grado."))}
""", 2)

T.ap("s7", "II.5 La libre designación (TREBEP, art. 80; RD 364/1995, arts. 51 a 58; Ley 30/1984, art. 20.1 b)", f"""
{unidad("5.1 Concepto y cese discrecional (TREBEP, art. 80)",
  lit("TREBEP", "Artículo 80", ["apreciación discrecional por el órgano competente de la idoneidad de los candidatos", "especial responsabilidad y confianza", "podrán ser cesados discrecionalmente"]),
  fichab("Provisión por apreciación discrecional de la idoneidad",
         [f"{c('TREBEP', 'Artículo 80', 'el órgano competente')} (puede recabar la intervención de **especialistas**)", "Las leyes de Función Pública fijan los criterios para determinar los puestos"],
         "Convocatoria pública; se aprecia la idoneidad en relación con los **requisitos** del puesto",
         "—",
         "Puestos de **especial responsabilidad y confianza**. Cese **discrecional**, pero con derecho a que se le asigne un puesto conforme al sistema de carrera."))}

{unidad("5.2 Qué puestos y quién los provee (RD 364/1995, art. 51; Ley 30/1984, art. 20.1 b, párrafo segundo)",
  lit("RD364", "Artículo 51", ["a los Ministros de los Departamentos de los que dependan y a los Secretarios de Estado", "Subdirector general", "Secretarías de Altos Cargos"]),
  lit("L30", "aveinte", ["sólo podrán cubrirse por este sistema"], solo=[4], titulo="Artículo veinte. Provisión de puestos de trabajo, apartado 1 b), párrafo segundo (Ley 30/1984)"),
  fichab("Ámbito de la libre designación en la Administración General del Estado",
         "Proveen: los **Ministros** de los Departamentos de los que dependan los puestos y los **Secretarios de Estado** en su ámbito",
         ["::Solo estos puestos:", "**Subdirector general**", "**Delegados y Directores** territoriales, provinciales o Comisionados", "**Secretarías de Altos Cargos**", "Otros de carácter **directivo o de especial responsabilidad** según la relación de puestos de trabajo"],
         "—",
         "La lista es **cerrada** («Sólo podrán cubrirse»). Los Subdirectores generales tienen hoy, además, las reglas del personal directivo público profesional (→ II.6.2)."))}

{unidad("5.3 Convocatoria, solicitudes, informes y nombramiento (RD 364/1995, arts. 52 a 57)",
  lit("RD364", "Artículo 52", ["previa convocatoria pública"]),
  lit("RD364", "Artículo 53", ["dentro de los quince días hábiles siguientes"]),
  lit("RD364", "Artículo 54", ["el previo informe del titular del centro, organismo o unidad", "informe favorable de éste", "De no emitirse en el plazo de quince días naturales se considerará favorable", "previa autorización del Secretario de Estado para la Administración Pública"]),
  lit("RD364", "Artículo 55", ["informe favorable del Ministerio al que esté adscrito el Cuerpo o Escala"]),
  lit("RD364", "Artículo 56", ["un mes", "hasta un mes más", "Las resoluciones de nombramiento se motivarán"]),
  lit("RD364", "Artículo 57", ["el establecido en el artículo 48"]),
  fichab("Procedimiento de la libre designación",
         ["Informe previo del **titular del centro, organismo o unidad** del puesto", "Si el candidato está en **otro Departamento**: informe **favorable** de este", "Cuerpos con puestos en exclusiva: informe favorable del Ministerio de adscripción del Cuerpo"],
         ["Convocatoria pública con la descripción y requisitos del puesto", "Nombramiento **motivado**: cumplimiento de requisitos por el elegido y competencia", "Toma de posesión: como en el concurso (art. 48, → II.4.2)"],
         ["Solicitudes: **15 días hábiles** desde la publicación", "Informes: si no se emiten en **15 días naturales**, **favorables**", "Nombramiento: **un mes** desde el fin del plazo de solicitudes, prorrogable **un mes más**"],
         "Informe desfavorable del otro Departamento: cabe nombrar **con autorización del Secretario de Estado para la Administración Pública**. Ojo: solicitudes en días **hábiles**, informes en días **naturales**."))}

{unidad("5.4 Cese y garantía (RD 364/1995, art. 58)",
  lit("RD364", "Artículo 58", ["con carácter discrecional", "se referirá a la competencia para adoptarla", "no inferior en más de dos niveles al de su grado personal en el mismo municipio", "no será de aplicación cuando se trate del cese de funcionarios destinados en el exterior"]),
  fichab("Fin del desempeño de un puesto de libre designación",
         "El órgano que nombró",
         ["Cese **discrecional**; la motivación se refiere solo a la **competencia**", "Adscripción **provisional** a un puesto de su Cuerpo o Escala hasta obtener otro definitivo, con efectos del día siguiente al cese"],
         "—",
         "Puesto **no inferior en más de dos niveles a su grado personal** y en el **mismo municipio**, salvo cese de destinados **en el exterior**. Cayó en 2025 (→ Cierre 1)."))}

""", 2)

T.ap("s8", "II.6 El personal directivo público profesional (RDL 6/2023, arts. 123.3 y 127)", f"""
{unidad("6.1 Los Subdirectores generales son personal directivo público profesional (RDL 6/2023, art. 123.3)",
  lit("RDL6", "Artículo 123", ["las personas titulares de las subdirecciones generales"], solo=[3]),
  fichab("Quiénes son personal directivo público profesional en la Administración General del Estado",
         c("RDL6", "Artículo 123", "las personas titulares de las subdirecciones generales"),
         "Por remisión al artículo 67 de la Ley 40/2015",
         "—",
         "Subdirector general = **personal directivo público profesional** (y su puesto, de libre designación: → II.5.2). El personal directivo como clase de personal es del tema V.1."))}

{unidad("6.2 Nombramiento, duración y cese (RDL 6/2023, art. 127)",
  lit("RDL6", "Artículo 127", ["en todo caso por el procedimiento de libre designación", "sin que quepa la cobertura de carácter provisional", "diez días naturales desde la publicación de la convocatoria", "una justificación por escrito de la idoneidad", "duración máxima de cinco años", "De forma excepcional, por pérdida de la confianza"], solo=[1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]),
  fichab("Provisión de los puestos de personal directivo público profesional",
         "Nombra y cesa el **mismo órgano** competente",
         ["**Libre designación**, en todo caso, **sin cobertura provisional**", "Convocatoria con requisitos y competencias a valorar; solicitud con **justificación escrita de la idoneidad**", "Sin los informes del art. 20 de la Ley 30/1984", "**Causas de cese, motivadas (127.3):**", "Fin del plazo", "Petición propia", "Evaluación negativa", "Supresión o modificación del puesto por reorganización", "Separación del servicio o despido disciplinario", "Pérdida de requisitos", "**Excepcionalmente**, pérdida de la confianza"],
         ["Solicitudes: **10 días naturales** desde la publicación de la convocatoria", "Nombramiento: **máximo cinco años**, renovable por períodos idénticos"],
         "Dos preguntas de 2025 (→ Cierre 1): **no cabe** cobertura provisional y el plazo de solicitudes es de **diez días naturales** (no quince hábiles, como en la libre designación general)."))}

{resumen([
  "Concurso: procedimiento **normal**; órganos colegiados técnicos; méritos generales y, en el **específico**, segunda fase con **memoria o entrevista**.",
  "Requisitos: cualquier situación salvo **suspensos en firme**; **dos años** en el puesto definitivo (salvo en la misma Secretaría de Estado o Departamento); solicitudes en **15 días hábiles**.",
  "Cada concepto del baremo entre el **10 y el 40 %**; resolución en **dos meses**; toma de posesión en **3 días hábiles** o **un mes**.",
  "Libre designación: idoneidad apreciada **discrecionalmente**; lista cerrada de puestos; nombramiento en **un mes** (+ uno); cese discrecional y puesto provisional no inferior en más de **dos niveles** al grado, en el mismo municipio.",
  "Los titulares de **subdirecciones generales** son personal directivo público profesional (art. 123.3).",
  "Se nombran **siempre** por **libre designación**, **sin cobertura provisional**, con solicitudes en **10 días naturales** y por **cinco años** como máximo, renovables (art. 127).",
  "La pérdida de la confianza es causa de cese solo **de forma excepcional**."],
  "Siguiente: III. ¿Qué otras formas de provisión y movilidad hay?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Qué otras formas de provisión y movilidad hay?", donde(
  "Tercera pregunta. Además del concurso y la libre designación, la Administración puede **mover** a sus funcionarios por necesidades del servicio o a petición de ellos, con carácter **definitivo** o **temporal**.",
  ["1 La movilidad en el TREBEP (arts. 81 a 84)", "2 Redistribución, reasignación y cambio de adscripción (RD 364/1995, arts. 59 a 61)", "3 Reingreso, adscripción provisional, comisiones de servicios y atribución temporal de funciones (arts. 62 a 66 y 72)", "4 Movilidad por salud y por violencia de género (arts. 66 bis y 66 ter)", "5 Movilidad con las Comunidades Autónomas (arts. 67 a 69)", "6 Cuadro: definitivo o temporal"]))

T.ap("s9", "III.1 La movilidad en el TREBEP (arts. 81 a 84 y disposición transitoria octava)", f"""
{unidad("1.1 Movilidad voluntaria, traslado por necesidades del servicio y provisión provisional (TREBEP, art. 81)",
  lit("TREBEP", "Artículo 81", ["sectores prioritarios de la actividad pública con necesidades específicas de efectivos", "de manera motivada", "se dará prioridad a la voluntariedad de los traslados", "En caso de urgente e inaplazable necesidad"]),
  fichab("Movilidad del personal funcionario de carrera",
         "Cada Administración Pública",
         ["Reglas para ordenar la **movilidad voluntaria** hacia **sectores prioritarios** (81.1)", "**Traslado motivado** por necesidades de servicio o funcionales a otras unidades, departamentos u organismos, **respetando retribuciones y condiciones esenciales** (81.2)", "Provisión **provisional** en caso de **urgente e inaplazable necesidad**, con convocatoria pública posterior (81.3)"],
         "Convocatoria pública del puesto provisional: en el plazo que señalen las normas aplicables",
         "Si los planes de ordenación implican **cambio de residencia**, prioridad a la **voluntariedad**; indemnizaciones de los **traslados forzosos**."))}

{unidad("1.2 Movilidad por violencia de género, violencia sexual y violencia terrorista (TREBEP, art. 82)",
  lit("TREBEP", "Artículo 82", ["sin necesidad de que sea vacante de necesaria cobertura", "Este traslado tendrá la consideración de traslado forzoso", "cuando la vacante sea de necesaria cobertura o, en caso contrario, dentro de la comunidad autónoma"], solo=[1, 2, 3, 4, 5]),
  ficha(["Mujeres víctimas de **violencia de género o violencia sexual** (82.1)", "Funcionarios víctimas del **terrorismo** y sus familiares funcionarios, y funcionarios **amenazados**, previo reconocimiento del Ministerio del Interior o sentencia firme (82.2)"],
        "Traslado a otro puesto propio de su cuerpo, escala o categoría, **de análogas características**",
        ["Violencia de género o sexual: **sin necesidad** de que sea vacante de necesaria cobertura", "Terrorismo: si la vacante es de necesaria cobertura o, si no, **dentro de la comunidad autónoma**"],
        "La Administración debe comunicar las vacantes de la localidad o de las que se soliciten; se protege la **intimidad** de las víctimas",
        "En ambos casos el traslado es **forzoso** (a efectos de indemnización). Desarrollo en la AGE para la violencia de género: → III.4.2."))}

{unidad("1.3 Personal laboral (TREBEP, art. 83)",
  lit("TREBEP", "Artículo 83", ["convenios colectivos", "en su defecto por el sistema de provisión de puestos y movilidad del personal funcionario de carrera"]),
  fichab("Provisión y movilidad del personal laboral", "Personal laboral",
         "Según los **convenios colectivos**; **en su defecto**, el sistema de los funcionarios de carrera", "—",
         "Primero el **convenio**; el sistema funcionarial es **supletorio** (tema V.7)."))}

{unidad("1.4 Movilidad entre Administraciones Públicas (TREBEP, art. 84 y disposición transitoria octava)",
  lit("TREBEP", "Artículo 84", ["preferentemente mediante convenio de Conferencia Sectorial", "situación administrativa de servicio en otras Administraciones Públicas", "en el plazo máximo de un mes a contar desde el día siguiente al del cese", "excedencia voluntaria por interés particular"]),
  lit("TREBEP", "dtoctava", ["resultarán de aplicación en las Administraciones Públicas en las que se hayan aprobado la correspondiente ley de desarrollo"], titulo="Disposición transitoria octava. Aplicación del artículo 84.3 (TREBEP)"),
  fichab("Movilidad interadministrativa voluntaria",
         ["Administración General del Estado, comunidades autónomas y entidades locales (medidas de movilidad)", "**Conferencia Sectorial de Administración Pública**: criterios generales de homologación"],
         ["Preferentemente por **convenio de Conferencia Sectorial** u otros instrumentos de colaboración", "Con destino en otra Administración: **servicio en otras Administraciones Públicas** respecto de la de origen", "Remoción o supresión del puesto obtenido por concurso: se queda en la Administración de **destino**, que le asigna puesto"],
         ["Cese en libre designación: la Administración de destino tiene **un mes** para adscribirlo a otro puesto o comunicar que no lo hará", "Después, el funcionario tiene **un mes** para pedir el reingreso en la de origen", "Si no lo pide: **excedencia voluntaria por interés particular** de oficio"],
         "Las reglas del **84.3** sobre cese en libre designación solo se aplican donde se haya aprobado la **ley de desarrollo** (disposición transitoria octava). Situaciones: tema V.5."))}
""", 2)

T.ap("s10", "III.2 Redistribución, reasignación y cambio de adscripción (RD 364/1995, arts. 59 a 61)", f"""
{unidad("2.1 Redistribución de efectivos (RD 364/1995, art. 59)",
  lit("RD364", "Artículo 59", ["puestos no singularizados", "misma naturaleza, nivel de complemento de destino y complemento específico", "sin que ello suponga cambio de municipio", "tendrá asimismo carácter definitivo"]),
  fichab("Adscripción por necesidades del servicio a otro puesto equivalente",
         ["Funcionarios que ocupan **con carácter definitivo** puestos **no singularizados**", "**Acuerdan:**", "**Secretaría de Estado para la Administración Pública**: entre servicios centrales de distintos Departamentos (previo informe)", "**Subsecretarios**: en su Departamento y con sus Organismos autónomos y Entidades Gestoras", "**Presidentes o Directores** de Organismos autónomos y Entidades Gestoras y Servicios Comunes", "**Delegados del Gobierno** y Gobernadores civiles: entre servicios de distintos Departamentos (previo informe favorable)"],
         "A otro puesto de la **misma naturaleza, nivel de complemento de destino y específico** y mismo procedimiento de provisión, **sin cambio de municipio**",
         "Los **dos años** para concursar se cuentan desde que se accedió al puesto anterior",
         "Puesto no singularizado: el que **no se individualiza** en la relación de puestos. El destino por redistribución es **definitivo** (→ Cierre 1)."))}

{unidad("2.2 Reasignación de efectivos por un Plan de Empleo (RD 364/1995, art. 60)",
  lit("RD364", "Artículo 60", ["como consecuencia de un Plan de Empleo", "La adscripción al puesto adjudicado por reasignación tendrá carácter definitivo", "En el plazo máximo de seis meses", "en un plazo máximo de tres meses", "obligatorio para puestos en el mismo municipio y voluntario para puestos que radiquen en otro distinto", "expectativa de destino", "obligatorio cuando el puesto esté situado en la misma provincia"]),
  fichab("Recolocación de funcionarios cuyo puesto se suprime por un Plan de Empleo",
         ["1.ª fase: **Subsecretario** del Departamento", "2.ª fase: **Secretaría de Estado para la Administración Pública** (otro Departamento)", "3.ª fase: adscripción al Ministerio para las Administraciones Públicas en **expectativa de destino**"],
         ["Criterios objetivos: **aptitudes, formación, experiencia y antigüedad**", "1.ª y 2.ª fase: **obligatoria** en el mismo **municipio**, voluntaria en otro; se siguen cobrando las retribuciones del puesto suprimido", "3.ª fase: **obligatoria** en la misma **provincia**, voluntaria en otra; conlleva el reingreso al servicio activo"],
         ["1.ª fase: **seis meses** desde la supresión", "2.ª fase: **tres meses**"],
         "Adscripción **definitiva**. Ojo al cambio de referencia: **municipio** en las dos primeras fases, **provincia** en la tercera. Indemnizaciones: tema V.6; expectativa de destino: tema V.5."))}

{unidad("2.3 Cambio de adscripción de puestos (RD 364/1995, art. 61)",
  lit("RD364", "Artículo 61", ["puestos de trabajo no singularizados y de los funcionarios titulares de los mismos", "con la conformidad de los titulares de los puestos", "identificados como deficitarios"]),
  fichab("Traslado del puesto con su titular a otra unidad",
         "Departamentos ministeriales, Organismos autónomos y Entidades Gestoras y Servicios Comunes; si hay cambio de Departamento, el Ministerio para las Administraciones Públicas",
         ["Se adscribe el **puesto no singularizado con su titular** a otras unidades o centros", "En Planes de Empleo: concursos para centros **deficitarios** abiertos a funcionarios de áreas **excedentarias** (61.2)"],
         "—",
         "Si supone **cambio de municipio**, solo con la **conformidad** del titular."))}
""", 2)

T.ap("s11", "III.3 Reingreso, adscripción provisional, comisiones de servicios y atribución temporal de funciones (RD 364/1995, arts. 62 a 66 y 72)", f"""
{unidad("3.1 Reingreso al servicio activo (RD 364/1995, art. 62)",
  lit("RD364", "Artículo 62", ["mediante su participación en las convocatorias de concurso o de libre designación", "por adscripción provisional", "en el plazo máximo de un año"]),
  fichab("Cómo vuelve al servicio activo quien no tiene reserva de puesto",
         "Funcionarios **sin reserva** de puesto de trabajo",
         ["Concurso o libre designación", "Reasignación de efectivos (expectativa de destino o excedencia forzosa)", "**Adscripción provisional**, según las necesidades del servicio"],
         "El puesto provisional se convoca en el plazo máximo de **un año**; el funcionario **debe participar** pidiéndolo",
         "Si no obtiene destino definitivo, se aplica el art. 72.1 (desempeño provisional de otro puesto)."))}

{unidad("3.2 Adscripción provisional y garantía del puesto (RD 364/1995, arts. 63 y 72)",
  lit("RD364", "Artículo 63", ["únicamente en los siguientes supuestos"]),
  lit("RD364", "Artículo 72", ["se les atribuirá el desempeño provisional", "tendrán la obligación de participar en las correspondientes convocatorias", "durante un plazo máximo de tres meses"]),
  fichab("Cobertura provisional en tres supuestos tasados",
         ["Atribuyen el puesto provisional (72.1): **Subsecretarios**; Presidentes o Directores de Organismos autónomos y Entidades Gestoras y Servicios Comunes; Delegados del Gobierno y Gobernadores civiles"],
         ["::Solo en (63):", "**Remoción o cese** en puesto de concurso o libre designación", "**Supresión** del puesto", "**Reingreso** al servicio activo sin reserva de puesto"],
         ["Los puestos así cubiertos se convocan; quien los ocupa **debe participar** (72.2)", "Cese por alteración o supresión del puesto: se mantienen las retribuciones complementarias del de procedencia **hasta tres meses** como máximo (72.3)"],
         "Lista **cerrada** («únicamente»). La adscripción provisional **no** existe para el personal directivo público profesional (→ II.6.2)."))}

{unidad("3.3 Comisiones de servicios (RD 364/1995, art. 64)",
  lit("RD364", "Artículo 64", ["en caso de urgente e inaplazable necesidad, en comisión de servicios de carácter voluntario", "comisiones de servicios de carácter forzoso", "ésta se declare desierta", "menores cargas familiares", "duración máxima de un año prorrogable por otro", "plazo de tres días", "de ocho días en las comisiones de carácter voluntario y de treinta en las de carácter forzoso", "se les reservará el puesto de trabajo"]),
  fichab("Cobertura temporal de un puesto vacante",
         ["**Secretaría de Estado para la Administración Pública**: si hay cambio de Departamento (servicios centrales, o periféricos fuera del ámbito de una Comunidad Autónoma)", "**Subsecretarios**: en su Departamento y con sus Organismos autónomos y Entidades Gestoras", "**Presidentes o Directores** de Organismos autónomos y Entidades Gestoras y Servicios Comunes", "**Delegados del Gobierno** y Gobernadores civiles: entre servicios de distintos Departamentos"],
         ["**Voluntaria**: urgente e inaplazable necesidad, con funcionario que reúna los requisitos de la relación de puestos (64.1)", "**Forzosa**: concurso **desierto** y provisión urgente; se elige al del mismo Departamento, municipio más próximo o mejor comunicado, **menores cargas familiares** y, a igualdad, **menor antigüedad** (64.2)", "Se **reserva** el puesto y se cobran todas las retribuciones con cargo al programa del puesto desempeñado (64.6)"],
         ["Duración: **un año**, prorrogable **otro** si no se cubre con carácter definitivo", "Cese y toma de posesión: **3 días** sin cambio de residencia; con cambio, **8** (voluntaria) o **30** (forzosa)"],
         "Es **temporal**: el puesto se incluye en la **siguiente convocatoria** (64.5). Se **reserva** el puesto de origen (64.6)."))}

{unidad("3.4 Misiones de cooperación internacional y atribución temporal de funciones (RD 364/1995, arts. 65 y 66)",
  lit("RD364", "Artículo 65", ["no será superior a seis meses"]),
  lit("RD364", "Artículo 66", ["En casos excepcionales", "continuarán percibiendo las retribuciones correspondientes a su puesto de trabajo"]),
  fichab("Comisiones especiales sin cambio de puesto",
         "Los **Subsecretarios** de los Departamentos ministeriales",
         ["Misiones de **cooperación internacional**: si consta el interés de la Administración; la resolución decide qué retribución se cobra (65)", "**Atribución temporal de funciones**: funciones especiales no asignadas a puestos o tareas que no pueden atenderse por su mayor volumen temporal (66)"],
         "Misiones internacionales: **no más de seis meses**, salvo casos excepcionales",
         "En la atribución temporal de funciones se cobran las retribuciones **del propio puesto** (más, en su caso, indemnizaciones)."))}
""", 2)

T.ap("s12", "III.4 Movilidad por salud y por violencia de género (RD 364/1995, arts. 66 bis y 66 ter)", f"""
{unidad("4.1 Movilidad por razones de salud o de rehabilitación (RD 364/1995, art. 66 bis)",
  lit("RD364", "Artículo 66 bis", ["del funcionario, su cónyuge, o los hijos a su cargo", "informe previo del servicio médico oficial", "Servicio de prevención de riesgos laborales", "no sea superior al del puesto de origen", "un mínimo de dos años"]),
  fichab("Cambio de puesto a petición por salud o rehabilitación",
         ["Solicita el funcionario por motivos propios, de su **cónyuge** o de los **hijos a su cargo**", "Resuelven los órganos del art. 64.3 (→ III.3.3)"],
         ["Informe previo del **servicio médico oficial**; si el motivo es del propio funcionario, también del **Servicio de prevención de riesgos laborales**", "Puesto **vacante**, dotado, de **necesaria provisión** y de nivel de complementos de destino y específico **no superior** al de origen"],
         ["Cese y toma de posesión: **3 días hábiles** sin cambio de residencia, **un mes** con cambio", "Si es definitiva: permanencia mínima de **dos años**"],
         "La adscripción es **definitiva** si el funcionario ocupaba **con tal carácter** su puesto de origen."))}

{unidad("4.2 Movilidad de la funcionaria víctima de violencia de género (RD 364/1995, art. 66 ter)",
  lit("RD364", "Artículo 66 ter", ["copia de la orden de protección", "informe del Ministerio Fiscal", "La adscripción tendrá carácter definitivo cuando la funcionaria ocupara con tal carácter su puesto de origen", "tendrán la consideración de forzosos"]),
  fichab("Traslado de la funcionaria víctima de violencia de género",
         ["Solicita la **funcionaria**", "Resuelven los órganos del art. 64.3"],
         ["Solicitud con la **orden de protección** o, excepcionalmente, **informe del Ministerio Fiscal**", "Puesto propio de su cuerpo o escala, vacante, dotado, de necesaria provisión y de nivel **no superior** al de origen"],
         ["Cese y toma de posesión: **3 días hábiles** o **un mes**", "Si es definitiva: permanencia mínima de **dos años**, con excepciones"],
         "Definitiva si ocupaba su puesto con carácter definitivo (→ Cierre 1). Con cambio de residencia, traslado **forzoso**."))}
""", 2)

T.ap("s13", "III.5 Movilidad con las Comunidades Autónomas (RD 364/1995, arts. 67 a 69)", f"""
{unidad("5.1 Destinos en las Comunidades Autónomas (RD 364/1995, arts. 67 y 68)",
  lit("RD364", "Artículo 67", ["haya permanecido dos años en el puesto de destino", "De no emitirse dicho informe en el plazo de quince días naturales"]),
  lit("RD364", "Artículo 68", ["a propuesta de las Administraciones de las Comunidades Autónomas", "pasarán a la situación de servicio en Comunidades Autónomas"]),
  fichab("Funcionarios de la AGE en puestos autonómicos",
         ["Los funcionarios de la AGE participan en concursos o libre designación autonómicos (67)", "El Ministro para las Administraciones Públicas puede convocar concursos de puestos autonómicos a propuesta de las Comunidades (68)"],
         ["Por concurso: **dos años** en el puesto desde el que se participa", "Por libre designación: informe **favorable** del Departamento"],
         "Informe del Departamento: favorable si no se emite en **15 días naturales**",
         "Tras la toma de posesión, situación de **servicio en Comunidades Autónomas**, y paga la **Comunidad** (tema V.5)."))}

{unidad("5.2 Comisiones de servicios en Comunidades Autónomas (RD 364/1995, art. 69)",
  lit("RD364", "Artículo 69", ["de hasta dos años de duración"]),
  fichab("Comisión de servicios a petición de una Comunidad Autónoma",
         "Autorizan los **Departamentos ministeriales** a petición de la Comunidad", "Carácter **voluntario**",
         "Hasta **dos años**", "No se aplica la regla del art. 64.5 (inclusión del puesto en la siguiente convocatoria)."))}
""", 2)

T.ap("s14", "III.6 Cuadro: provisión definitiva o temporal (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Forma | Artículo (RD 364/1995) | Carácter | Quién decide | Dato que se pregunta |
|---|---|---|---|---|
| Primer destino tras el proceso selectivo | 26 | **Definitivo** | Por orden de puntuación | Equivale al obtenido por concurso |
| Concurso | 39 a 50 | **Definitivo** | Cada Ministerio | Sistema normal; dos años para volver a concursar |
| Libre designación | 51 a 58 | **Definitivo** (cese discrecional) | Ministros y Secretarios de Estado | Lista cerrada de puestos |
| Redistribución de efectivos | 59 | **Definitivo** | Secretaría de Estado, Subsecretarios… | Sin cambio de municipio |
| Reasignación de efectivos (Plan de Empleo) | 60 | **Definitivo** | Subsecretario → Secretaría de Estado | 6 + 3 meses; expectativa de destino |
| Movilidad por salud / violencia de género | 66 bis y 66 ter | **Definitivo** si el de origen lo era | Órganos del art. 64.3 | Dos años de permanencia |
| Comisión de servicios | 64 | **Temporal** | Órganos del art. 64.3 | Un año + uno; voluntaria o forzosa |
| Adscripción provisional | 63 y 72 | **Temporal** | Subsecretarios… | Solo remoción o cese, supresión y reingreso |
| Atribución temporal de funciones | 66 | **Temporal** | Subsecretarios | Cobra las retribuciones de su puesto |

{resumen([
  "TREBEP: movilidad voluntaria a sectores prioritarios, **traslado motivado** respetando retribuciones, provisión **provisional** por urgencia (81); víctimas de violencia, traslado **forzoso** (82); laborales, por **convenio** (83); movilidad entre Administraciones (84).",
  "Definitivas: **redistribución** (sin cambio de municipio) y **reasignación** por Plan de Empleo (fases de **6** y **3** meses).",
  "Temporales: **adscripción provisional** (tres supuestos) y **comisión de servicios** (un año prorrogable otro; voluntaria o forzosa).",
  "Salud y violencia de género: puesto de nivel **no superior**; definitivo si el de origen lo era; **dos años** de permanencia."],
  "Siguiente: IV. ¿Cómo se progresa? Carrera profesional y promoción interna")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Cómo se progresa? Carrera profesional y promoción interna", donde(
  "Cuarta pregunta. El funcionario progresa **sin cambiar de cuerpo** (carrera horizontal o vertical) o **cambiando de cuerpo o escala** (promoción interna). El TREBEP da el marco; en la Administración del Estado, el RDL 6/2023 regula la **carrera horizontal por tramos** y el RD 364/1995 el **grado personal** y la **promoción interna**.",
  ["1 La carrera profesional en el TREBEP (arts. 16, 17 y 19)", "2 La carrera horizontal en la Administración del Estado (RDL 6/2023, art. 122)", "3 El grado personal (RD 364/1995, art. 70; RDL 6/2023, disposición transitoria sexta)", "4 La promoción interna (TREBEP, art. 18; RD 364/1995, arts. 73 a 80; RDL 6/2023, art. 108.3)"]))

T.ap("s15", "IV.1 La carrera profesional en el TREBEP (arts. 16, 17 y 19)", f"""
{unidad("1.1 Concepto y modalidades de la carrera (TREBEP, art. 16)",
  lit("TREBEP", "Artículo 16", ["tendrán derecho a la promoción profesional", "conjunto ordenado de oportunidades de ascenso y expectativas de progreso profesional", "Carrera horizontal", "Carrera vertical", "Promoción interna vertical", "Promoción interna horizontal", "simultáneamente"]),
  ficha("Los **funcionarios de carrera** (el personal laboral, por el art. 19: → IV.1.3)",
        ["::Cuatro modalidades (16.3), aisladas o simultáneas:", "**Carrera horizontal**: progresión de grado, categoría, escalón… **sin cambiar de puesto**", "**Carrera vertical**: ascenso en la estructura de **puestos** por los procedimientos de provisión", "**Promoción interna vertical**: a un cuerpo o escala de Subgrupo o Grupo **superior**", "**Promoción interna horizontal**: a cuerpos o escalas del **mismo Subgrupo**"],
        "La regulan las **leyes de Función Pública** de desarrollo",
        "Principios de **igualdad, mérito y capacidad**; las Administraciones promueven la actualización y perfeccionamiento de la cualificación",
        "Son **cuatro** modalidades y caben **a la vez** la horizontal y la vertical (16.4). Cayó en 2025 (→ Cierre 1); los distractores inventan «consolidación de grado», «formación permanente» o carrera «per saltum»."))}

{unidad("1.2 Carrera horizontal (TREBEP, art. 17)",
  lit("TREBEP", "Artículo 17", ["sistema de grados, categorías o escalones de ascenso", "Los ascensos serán consecutivos con carácter general", "el resultado de la evaluación del desempeño"]),
  fichab("Reglas que pueden aplicar las leyes de Función Pública a la carrera horizontal",
         "Las **leyes de Función Pública** de desarrollo (es potestativo: «podrán»)",
         ["Sistema de **grados, categorías o escalones**, con remuneración para cada uno", "Ascensos **consecutivos** con carácter general", "Se valoran trayectoria, calidad de los trabajos, conocimientos y **evaluación del desempeño**"],
         "—",
         "La evaluación del desempeño (art. 20, tema V.2) tiene efectos en la carrera horizontal. En la AGE: tramos del RDL 6/2023 (→ IV.2)."))}

{unidad("1.3 Carrera y promoción del personal laboral (TREBEP, art. 19)",
  lit("TREBEP", "Artículo 19", ["tendrá derecho a la promoción profesional", "Estatuto de los Trabajadores o en los convenios colectivos"]),
  ficha("El **personal laboral**",
        "Derecho a la **promoción profesional**",
        "Se hace efectiva por los procedimientos del **Estatuto de los Trabajadores** o de los **convenios colectivos**",
        "—",
        "No por los del TREBEP. Cayó en 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s16", "IV.2 La carrera horizontal en la Administración del Estado (RDL 6/2023, arts. 105.3 y 122)", f"""
{unidad("2.1 El libro segundo del RDL 6/2023 (art. 105.3)",
  lit("RDL6", "Artículo 105", ["la evaluación del desempeño y carrera profesional"], solo=[3]),
  fichab("Objeto del libro segundo del Real Decreto-ley 6/2023",
         "La Administración del Estado",
         "Cuatro elementos: **planificación estratégica**, **acceso y selección**, **evaluación del desempeño y carrera profesional** y **directivo público profesional**",
         "—",
         "Por eso varias preguntas de 2025 de este tema citan el **RDL 6/2023** (concurso unitario, directivos)."))}

{unidad("2.2 Carrera horizontal por tramos (RDL 6/2023, art. 122)",
  lit("RDL6", "Artículo 122", ["sin necesidad de cambiar de puesto de trabajo", "tendrá carácter voluntario", "existirán 4 tramos", "cinco años de servicios efectivos en el caso del primer tramo y de seis años en los siguientes", "previa solicitud de la persona interesada", "Con carácter anual", "a partir del 1 de enero del año siguiente", "complemento de carrera"]),
  fichab("Progresión por tramos sin cambiar de puesto",
         "El personal funcionario de carrera, **a su solicitud** (también el de otras Administraciones con puesto definitivo en la del Estado)",
         ["**Cuatro tramos** por grupo o subgrupo; ascensos **consecutivos**", "Méritos: trayectoria y **evaluación del desempeño**; itinerario de **formación**; competencias y cualificaciones", "Convocatoria **anual**", "Se retribuye con el **complemento de carrera**, igual para el mismo tramo y grupo o subgrupo"],
         ["Primer tramo: **cinco años** de servicios efectivos; los siguientes: **seis**", "Efectos económicos: **1 de enero del año siguiente**"],
         "Es **voluntaria**. Computan servicios especiales y excedencias por cuidado de familiares y por violencia de género o terrorista; en la promoción interna se conservan los tramos y la fracción de tiempo."))}
""", 2)

TABLA_DT6 = "**Tabla de la disposición transitoria sexta**, copiada por el generador del XML del texto consolidado del BOE:\n\n" + tabla("RDL6", "dt-6")

T.ap("s17", "IV.3 El grado personal (RD 364/1995, art. 70; RDL 6/2023, disposición transitoria sexta)", f"""
{unidad("3.1 Adquisición y consolidación del grado (RD 364/1995, art. 70)",
  lit("RD364", "Artículo 70", ["30 niveles", "durante dos años continuados o tres con interrupción", "superior en más de dos niveles", "como grado personal inicial", "siempre que se obtenga con carácter definitivo dicho puesto u otro de igual o superior nivel", "No se computará el tiempo de desempeño en comisión de servicios", "si su duración es inferior a seis meses", "por el Subsecretario", "como mínimo del complemento de destino"]),
  fichab("El grado personal: nivel consolidado por el desempeño de puestos",
         ["Todos los **funcionarios de carrera**", "Lo reconoce el **Subsecretario** del Departamento (comunicación al Registro Central de Personal en **3 días hábiles**)"],
         ["Grado inicial: el nivel del puesto adjudicado tras el proceso selectivo (salvo que pase voluntariamente a uno inferior)", "Puesto **superior en más de dos niveles**: consolida **dos niveles cada dos años**, sin superar el del puesto ni el intervalo", "**Comisión de servicios**: computa si se obtiene con carácter definitivo **ese puesto u otro de igual o superior nivel**; nunca si el puesto era de nivel **inferior** al grado en consolidación", "Computan servicios especiales y el **primer año** de excedencia por cuidado de hijos"],
         ["Consolidación: **dos años continuados o tres con interrupción**", "Adscripción provisional de **menos de seis meses** tras remoción o cese: no interrumpe"],
         "**30 niveles**. El grado da derecho a cobrar **como mínimo** el complemento de destino de su nivel. Comisión de servicios y grado: cayó en 2025 (→ Cierre 1)."))}

{unidad("3.2 Intervalos de niveles por grupo o subgrupo (RDL 6/2023, disposición transitoria sexta)",
  lit("RDL6", "dt-6", ["Hasta tanto no se apruebe la normativa reglamentaria correspondiente"], titulo="Disposición transitoria sexta. Intervalos de niveles (RDL 6/2023)"),
  TABLA_DT6,
  fichab("Nivel mínimo y máximo de los puestos de cada grupo o subgrupo",
         "Grupos y subgrupos A1, A2, B, C1 y C2",
         "Cada cuerpo o escala solo puede desempeñar puestos dentro de su intervalo (regla que recoge el art. 71.2 del RD 364/1995)",
         "Transitoria: **hasta** que se apruebe la normativa reglamentaria",
         f"Prevalece sobre la tabla del art. 71.1 del RD 364/1995 (grupos A a E), que el BOE mantiene en su texto: el RDL 6/2023 deroga {c('RDL6', 'dd', 'todas las normas de igual o inferior rango en lo que contradigan o se opongan')}. A1: **24 a 30**; C2: **14 a 18**."))}
""", 2)

T.ap("s18", "IV.4 La promoción interna (TREBEP, art. 18; RD 364/1995, arts. 73 a 80; RDL 6/2023, art. 108.3)", f"""
{unidad("4.1 Promoción interna en el TREBEP (art. 18)",
  lit("TREBEP", "Artículo 18", ["mediante procesos selectivos", "al menos, dos años de servicio activo en el inferior Subgrupo", "adoptarán medidas que incentiven la participación"]),
  fichab("Acceso de funcionarios de carrera a otro cuerpo o escala",
         "Funcionarios de carrera; las **leyes de Función Pública** articulan los sistemas",
         ["**Procesos selectivos** con igualdad, mérito y capacidad y los principios del art. 55.2", "Requisitos de ingreso + antigüedad + superar las pruebas", "Las leyes pueden fijar los cuerpos de **su mismo Subgrupo** a los que se accede (promoción horizontal)"],
         "Antigüedad: **al menos dos años de servicio activo** en el Subgrupo (o Grupo) inferior",
         "**Dos años**, de **servicio activo**, en el Subgrupo **inferior**. Las Administraciones deben **incentivar** la participación."))}

{unidad("4.2 Concepto, sistemas, convocatorias y requisitos (RD 364/1995, arts. 73 a 76)",
  lit("RD364", "Artículo 73", ["a otro del inmediato superior o en el acceso a Cuerpos o Escalas del mismo Grupo de titulación"]),
  lit("RD364", "Artículo 74", ["oposición o concurso-oposición", "En ningún caso la puntuación obtenida en la fase de concurso podrá aplicarse para superar los ejercicios"]),
  lit("RD364", "Artículo 75", ["convocatorias independientes de las de ingreso"]),
  lit("RD364", "Artículo 76", ["al menos, dos años en el Cuerpo o Escala a que pertenezcan"]),
  fichab("Régimen general de la promoción interna en la AGE",
         ["Funcionarios con **dos años** en su Cuerpo o Escala", "Autoriza convocatorias independientes: el **Gobierno**"],
         ["Sistemas: **oposición o concurso-oposición** (nunca concurso solo)", "Concurso-oposición: puede fijarse una puntuación mínima para acceder a la fase de oposición", "Convocatorias **independientes** de las de ingreso, si lo autoriza el Gobierno por conveniencia de la planificación"],
         "Antigüedad de **dos años** referida al día en que **finaliza el plazo de solicitudes**",
         "Los puntos del concurso **no** sirven para aprobar los ejercicios de la oposición. Supletoriamente rige el título I (ingreso, tema V.3)."))}

{unidad("4.3 Exención de pruebas, derechos y vacantes desiertas (RD 364/1995, arts. 77 a 79)",
  lit("RD364", "Artículo 77", ["la exención de las pruebas"]),
  lit("RD364", "Artículo 78", ["preferencia para cubrir los puestos vacantes", "en el puesto que vinieran desempeñando", "Cuerpos de Seguridad del Estado", "podrán conservar, a petición propia, el grado personal"]),
  lit("RD364", "Artículo 79", ["se acumularán a las que se ofrezcan al resto de los aspirantes de acceso libre"]),
  fichab("Ventajas de quien promociona y destino de las plazas no cubiertas",
         "Funcionarios aprobados por el turno de promoción interna",
         ["Exención de pruebas sobre materias ya acreditadas en el ingreso al Cuerpo de origen (77)", "**Preferencia** sobre los de acceso libre para elegir vacantes (78.1)", "Pueden pedir destino en **su puesto** o en vacantes del municipio, con autorización (78.2; no en los Cuerpos de Seguridad del Estado)", "Conservan, **a petición propia**, el grado consolidado si está en el intervalo del nuevo Cuerpo (78.3)"],
         "Vacantes **desiertas** de promoción interna: se **acumulan** a las de acceso libre, salvo convocatorias independientes (79)",
         "Quien elige quedarse en su puesto sale del sistema de adjudicación **por orden de puntuación**. Las convocatorias pueden excluir esa posibilidad."))}

{unidad("4.4 Promoción a Cuerpos o Escalas del mismo grupo (RD 364/1995, art. 80)",
  lit("RD364", "Artículo 80", ["actividades sustancialmente coincidentes o análogas", "cuando se deriven ventajas para la gestión de los servicios", "deberá establecerse la exención de las pruebas"]),
  fichab("Promoción interna horizontal en la AGE",
         ["El **Gobierno**, a propuesta del Ministro para las Administraciones Públicas, determina los Cuerpos o Escalas", "El Ministerio para las Administraciones Públicas fija requisitos y pruebas"],
         ["Entre funcionarios con actividades **sustancialmente coincidentes o análogas**", "Con titulación académica del Cuerpo de destino", "**Exención obligatoria** («deberá») de las pruebas sobre conocimientos ya exigidos"],
         "—",
         "En el art. 77 la exención es **potestativa** («podrá»); en el art. 80, **obligatoria** («deberá»)."))}

{unidad("4.5 Plazas de promoción interna en la oferta de empleo público (RDL 6/2023, art. 108.3)",
  lit("RDL6", "Artículo 108", ["un porcentaje no inferior al treinta por ciento de las plazas de acceso libre para promoción interna"], solo=[5]),
  fichab("Reserva mínima de plazas para promoción interna",
         "La oferta de empleo público de la Administración del Estado (tema V.3)",
         "Plazas de promoción interna calculadas sobre las de **acceso libre**",
         "**No inferior al 30 %** de las plazas de acceso libre",
         "Es un **mínimo** («no inferior») y se calcula sobre las de **acceso libre**. Pregunta de 2025 (→ Cierre 1). La reserva por discapacidad (10 %) es del tema V.10."))}

{resumen([
  "Carrera (TREBEP, art. 16): **horizontal**, **vertical**, **promoción interna vertical** y **horizontal**; la horizontal y la vertical, simultáneas. Personal laboral: Estatuto de los Trabajadores o convenios (art. 19).",
  "AGE: carrera horizontal **voluntaria** en **cuatro tramos** (5 y 6 años), convocatoria **anual**, complemento de carrera (RDL 6/2023, art. 122).",
  "Grado personal: **30 niveles**; **dos años continuados o tres con interrupción**; comisión de servicios computa si se obtiene **ese puesto u otro de igual o superior nivel** (RD 364/1995, art. 70).",
  "Promoción interna: **dos años**, **oposición o concurso-oposición**, preferencia en la elección de vacantes y **30 %** mínimo de las plazas de acceso libre."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_L63 = examen("L", 63, {
  "a": f"Literal del art. 16.3: {c('TREBEP', 'Artículo 16', 'a) Carrera horizontal')}, {c('TREBEP', 'Artículo 16', 'b) Carrera vertical')}, {c('TREBEP', 'Artículo 16', 'c) Promoción interna vertical')} y {c('TREBEP', 'Artículo 16', 'd) Promoción interna horizontal')}.",
  "b": "Cambia dos modalidades: la «consolidación de grado» y la «formación permanente» no están en la lista del art. 16.3 (la consolidación del grado es un efecto de la carrera, → IV.3).",
  "c": "Deja fuera la carrera vertical y las dos promociones internas, e inventa unos «ascensos internos específicos» que el art. 16.3 no menciona.",
  "d": "Omite las dos modalidades de promoción interna e inventa una carrera «per saltum» que no existe en el art. 16.3."},
  [("promoción interna vertical", "TREBEP", "Artículo 16", "Promoción interna vertical, que consiste en el ascenso"), ("promoción interna horizontal", "TREBEP", "Artículo 16", "Promoción interna horizontal, que consiste en el acceso"), ("carrera horizontal", "TREBEP", "Artículo 16", "Carrera horizontal, que consiste en la progresión")])
EX_P82 = examen("P", 82, {
  "a": f"Falso: el art. 19.1 dice que {c('TREBEP', 'Artículo 19', 'El personal laboral tendrá derecho a la promoción profesional')}.",
  "b": f"Cambia la norma: no son los procedimientos del Estatuto Básico, sino {c('TREBEP', 'Artículo 19', 'los procedimientos previstos en el Estatuto de los Trabajadores o en los convenios colectivos')}.",
  "c": f"Literal del art. 19.2: {c('TREBEP', 'Artículo 19', 'se hará efectiva a través de los procedimientos previstos en el Estatuto de los Trabajadores o en los convenios colectivos')}.",
  "d": "La libre designación es un procedimiento de provisión de puestos de funcionarios (art. 80), no el sistema de promoción del personal laboral."},
  [("Estatuto de los Trabajadores o en los convenios colectivos", "TREBEP", "Artículo 19", "previstos en el Estatuto de los Trabajadores o en los convenios colectivos")])
EX_L68 = examen("L", 68, {
  "a": "No existen en el art. 111 unos «planes de ámbito general»: el instrumento son concursos.",
  "b": f"Literal del art. 111: la Secretaría de Estado de Función Pública {c('RDL6', 'Artículo 111', 'convocará concursos unitarios, de carácter abierto y permanente')}.",
  "c": "No son «planes específicos de vacantes»: el art. 111 habla de concursos unitarios en los que se podrán incluir puestos vacantes.",
  "d": "No son concursos «de reestructuración de sectores concretos»; los del art. 111 son unitarios, abiertos y permanentes."},
  [("Concursos unitarios", "RDL6", "Artículo 111", "convocará concursos unitarios, de carácter abierto y permanente")])
EX_L67 = examen("L", 67, {
  "a": f"No hay excepción «mientras se resuelve»: el art. 127.1 excluye la provisionalidad sin matices, {c('RDL6', 'Artículo 127', 'sin que quepa la cobertura de carácter provisional')}.",
  "b": f"Que la convocatoria quede desierta no abre la cobertura provisional: el nombramiento se hace {c('RDL6', 'Artículo 127', 'en todo caso por el procedimiento de libre designación')}.",
  "c": f"Correcta: los titulares de subdirecciones generales son personal directivo público profesional (art. 123.3: {c('RDL6', 'Artículo 123', 'las personas titulares de las subdirecciones generales')}) y para ellos no cabe la cobertura provisional (art. 127.1).",
  "d": f"La adscripción provisional sí es una forma de provisión: el RD 364/1995 la regula en su art. 63 ({c('RD364', 'Artículo 63', 'Los puestos de trabajo podrán proveerse por medio de adscripción provisional')}). La razón de que no quepa aquí es otra."},
  [("personal directivo público profesional", "RDL6", "Artículo 127", "sin que quepa la cobertura de carácter provisional"), ("personal directivo público profesional", "RDL6", "Artículo 123", "Tendrán la consideración de personal directivo público profesional las personas titulares de las subdirecciones generales")])
EX_X71 = examen("X", 71, {
  "a": f"No hay plazo de cobertura provisional «mientras se resuelve»: el art. 127.1 dice {c('RDL6', 'Artículo 127', 'sin que quepa la cobertura de carácter provisional')}.",
  "b": "No hay excepción por «razones extraordinarias»: la exclusión del art. 127.1 no admite supuestos.",
  "c": "Cambia el plazo (doce meses) de una cobertura provisional que el art. 127.1 no permite.",
  "d": f"Literal del art. 127.1: nombramiento {c('RDL6', 'Artículo 127', 'en todo caso por el procedimiento de libre designación')}, {c('RDL6', 'Artículo 127', 'sin que quepa la cobertura de carácter provisional')}."},
  [("No cabe", "RDL6", "Artículo 127", "sin que quepa la cobertura de carácter provisional")])
EX_X76 = examen("X", 76, {
  "a": f"Literal del art. 127.1: {c('RDL6', 'Artículo 127', 'El plazo máximo de presentación de solicitudes será de diez días naturales desde la publicación de la convocatoria')}.",
  "b": "Quince es el número de días de la libre designación general (RD 364/1995, art. 53), y son hábiles; para el personal directivo son diez naturales.",
  "c": "Cambia el plazo: veinte días no aparece en el art. 127.1.",
  "d": "Cambia el plazo: treinta días no aparece en el art. 127.1."},
  [("Diez días naturales", "RDL6", "Artículo 127", "será de diez días naturales desde la publicación de la convocatoria")])
EX_X73 = examen("X", 73, {
  "a": f"Literal del art. 58.2: {c('RD364', 'Artículo 58', 'no inferior en más de dos niveles al de su grado personal en el mismo municipio')}, y el municipio {c('RD364', 'Artículo 58', 'no será de aplicación cuando se trate del cese de funcionarios destinados en el exterior')}.",
  "b": "Cambia la garantía: no es un puesto «de nivel igual o superior» al grado, sino «no inferior en más de dos niveles» a él.",
  "c": "Cambia el ámbito: no es el «mismo departamento ministerial», sino el «mismo municipio» (y omite la excepción del exterior).",
  "d": "Cambia la referencia: no es el nivel «del puesto del que cesan», sino el de su «grado personal»."},
  [("no inferior en más de dos niveles al de su grado personal en el mismo municipio", "RD364", "Artículo 58", "no inferior en más de dos niveles al de su grado personal en el mismo municipio"), ("destinados en el exterior", "RD364", "Artículo 58", "cuando se trate del cese de funcionarios destinados en el exterior")])
EX_X66 = examen("X", 66, {
  "a": f"Definitivo: art. 26.1, {c('RD364', 'Artículo 26', 'Estos destinos tendrán carácter definitivo')}, equivalente a los obtenidos por concurso.",
  "b": f"Definitivo: art. 59.1, el puesto de la redistribución {c('RD364', 'Artículo 59', 'tendrá asimismo carácter definitivo')}.",
  "c": f"Correcta: la comisión de servicios es una cobertura temporal (art. 36.3: {c('RD364', 'Artículo 36', 'Temporalmente podrán ser cubiertos mediante comisión de servicios')}), y el puesto se incluye en la siguiente convocatoria (art. 64.5).",
  "d": f"Definitivo: art. 66 ter.2, {c('RD364', 'Artículo 66 ter', 'La adscripción tendrá carácter definitivo cuando la funcionaria ocupara con tal carácter su puesto de origen')}."},
  [("comisión de servicios", "RD364", "Artículo 36", "Temporalmente podrán ser cubiertos mediante comisión de servicios"), ("comisión de servicios de carácter voluntario", "RD364", "Artículo 64", "en comisión de servicios de carácter voluntario")])
EX_X74 = examen("X", 74, {
  "a": "No es «en ningún caso»: el art. 70.6 lo permite si se obtiene con carácter definitivo ese puesto u otro de igual o superior nivel.",
  "b": "Inventa una excepción («más de dos niveles superior») que el art. 70.6 no contiene para la comisión de servicios.",
  "c": f"Literal del art. 70.6: {c('RD364', 'Artículo 70', 'el tiempo prestado en comisión de servicios será computable para consolidar el grado correspondiente al puesto desempeñado siempre que se obtenga con carácter definitivo dicho puesto u otro de igual o superior nivel')}.",
  "d": f"Es al revés: {c('RD364', 'Artículo 70', 'No se computará el tiempo de desempeño en comisión de servicios cuando el puesto fuera de nivel inferior al correspondiente al grado en proceso de consolidación')}."},
  [("siempre que se obtenga con carácter definitivo dicho puesto u otro de igual o superior nivel", "RD364", "Artículo 70", "siempre que se obtenga con carácter definitivo dicho puesto u otro de igual o superior nivel")])
EX_X75 = examen("X", 75, {
  "a": "Cambia el porcentaje: el art. 108.3 no dice veinte, sino treinta por ciento.",
  "b": f"Literal del art. 108.3: {c('RDL6', 'Artículo 108', 'La oferta de empleo público incluirá un porcentaje no inferior al treinta por ciento de las plazas de acceso libre para promoción interna')}.",
  "c": "Cambia el porcentaje: el diez por ciento es la reserva para personas con discapacidad (art. 108.4), no la de promoción interna.",
  "d": "Cambia el porcentaje: cinco por ciento no aparece en el art. 108."},
  [("treinta por ciento", "RDL6", "Artículo 108", "un porcentaje no inferior al treinta por ciento de las plazas de acceso libre para promoción interna")])

T.ap("s19", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **nueve** preguntas de este tema (dos en el turno libre sobre el RDL 6/2023 y una sobre el art. 16 TREBEP; una en promoción interna sobre el art. 19; cinco en el extraordinario) y **una** relacionada (plazas de promoción interna en la oferta de empleo público, asignada al tema V.3). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
  "### GACE-L 2025, pregunta 63 · Modalidades de carrera (→ IV.1.1)", EX_L63,
  "### GACE-P 2025, pregunta 82 · Carrera del personal laboral (→ IV.1.3)", EX_P82,
  "### GACE-L 2025, pregunta 68 · Concurso unitario (→ II.2.2)", EX_L68,
  "### GACE-L 2025, pregunta 67 · Subdirector general y cobertura provisional (→ II.6.2)", EX_L67,
  "### GACE-L 2025 extraordinario, pregunta 71 · Cobertura provisional del personal directivo (→ II.6.2)", EX_X71,
  "### GACE-L 2025 extraordinario, pregunta 76 · Plazo de solicitudes del personal directivo (→ II.6.2)", EX_X76,
  "### GACE-L 2025 extraordinario, pregunta 73 · Cese en libre designación (→ II.5.4)", EX_X73,
  "### GACE-L 2025 extraordinario, pregunta 66 · Destinos definitivos y temporales (→ I.2.2 y → III.3.3)", EX_X66,
  "### GACE-L 2025 extraordinario, pregunta 74 · Comisión de servicios y grado (→ IV.3.1)", EX_X74,
  "### GACE-L 2025 extraordinario, pregunta 75 · Plazas de promoción interna (relacionada; → IV.4.5)", EX_X75,
  "### Cómo se pregunta",
  "!> Los distractores cambian **un dato** de la norma: el plazo (diez días **naturales** frente a quince **hábiles**), la referencia de la garantía (**grado personal** y **mismo municipio**, no el puesto del que se cesa ni el Departamento), un porcentaje (**30 %**) o el carácter **definitivo/temporal** del destino. Cuatro preguntas de 2025 de este tema y la relacionada salen del **RDL 6/2023**: conviene leer sus arts. 108, 111, 122, 123 y 127.",
]))

T.ap("s20", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Normas y formas de provisión | TREBEP art. 78 (efectos con las leyes de Función Pública); RD 364/1995, art. 36 | Concurso = sistema **normal**; temporales: **comisión de servicios** y **adscripción provisional** |
| II. Concurso y libre designación | Arts. 39 a 58 RD 364/1995; RDL 6/2023, arts. 111 y 127 | **Dos años** para concursar; **15 días hábiles**; directivos: **10 días naturales** y **sin cobertura provisional** |
| III. Otras formas y movilidad | TREBEP arts. 81 a 84; RD 364/1995, arts. 59 a 69 | Redistribución **definitiva** sin cambio de municipio; comisión **un año + uno** |
| IV. Carrera y promoción interna | TREBEP arts. 16 a 19; RDL 6/2023, art. 122; RD 364/1995, arts. 70 y 73 a 80 | **Cuatro** modalidades de carrera; grado: **2 años continuados o 3 con interrupción**; **30 %** para promoción interna |

?> **Trampas frecuentes:** «la libre designación es el sistema normal» (lo es el **concurso**); «el puesto en comisión de servicios es definitivo» (es **temporal**); «el cesado en libre designación va a un puesto no inferior en dos niveles al **del puesto** del que cesa» (es a su **grado personal**, en el **mismo municipio**); «los directivos pueden cubrirse provisionalmente mientras se resuelve la convocatoria» (**no cabe**); «el personal laboral promociona por los procedimientos del TREBEP» (por el **Estatuto de los Trabajadores o los convenios**); «la promoción interna se hace por concurso» (por **oposición o concurso-oposición**).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
Q = [
  ("TREBEP", "Artículo 78", "Provisión", "Según el artículo 78.1 del TREBEP, las Administraciones Públicas proveerán los puestos de trabajo mediante procedimientos basados en los principios de:",
   ["Igualdad, mérito, capacidad y publicidad.", "Igualdad, mérito y capacidad.", "Publicidad, transparencia e imparcialidad.", "Mérito, capacidad y antigüedad."],
   "Art. 78.1 TREBEP: «igualdad, mérito, capacidad y publicidad».", "igualdad, mérito, capacidad y publicidad"),
  ("TREBEP", "Artículo 78", "Provisión", "Según el artículo 78.2 del TREBEP, la provisión de puestos de trabajo se llevará a cabo por los procedimientos de:",
   ["Concurso y libre designación con convocatoria pública.", "Concurso, oposición y libre designación.", "Concurso y comisión de servicios.", "Libre designación y redistribución de efectivos."],
   "Art. 78.2 TREBEP.", "concurso y de libre designación con convocatoria pública"),
  ("RD364", "Artículo 36", "Provisión", "Según el artículo 36.3 del Real Decreto 364/1995, los puestos de trabajo podrán ser cubiertos temporalmente mediante:",
   ["Comisión de servicios y adscripción provisional.", "Redistribución y reasignación de efectivos.", "Libre designación y comisión de servicios.", "Concurso específico y adscripción provisional."],
   "Art. 36.3 RD 364/1995. La redistribución y la reasignación (36.2) son definitivas.", "Temporalmente podrán ser cubiertos mediante comisión de servicios y adscripción provisional"),
  ("RD364", "Artículo 36", "Provisión", "Según el artículo 36.1 del Real Decreto 364/1995, el sistema normal de provisión de los puestos de trabajo adscritos a funcionarios es:",
   ["El concurso.", "La libre designación.", "La redistribución de efectivos.", "La comisión de servicios."],
   "Art. 36.1 RD 364/1995: «concurso, que es el sistema normal de provisión».", "concurso, que es el sistema normal de provisión"),
  ("RD364", "Artículo 26", "Provisión", "Según el artículo 26.1 del Real Decreto 364/1995, los destinos adjudicados a los funcionarios de nuevo ingreso tendrán carácter:",
   ["Definitivo, equivalente a todos los efectos a los obtenidos por concurso.", "Provisional, hasta que obtengan destino por concurso.", "Provisional durante dos años.", "Definitivo, salvo a efectos de consolidación del grado personal."],
   "Art. 26.1 RD 364/1995.", "Estos destinos tendrán carácter definitivo, equivalente a todos los efectos a los obtenidos por concurso"),
  ("TREBEP", "Artículo 79", "Concurso", "Según el artículo 79.1 del TREBEP, en el concurso los méritos y capacidades de los candidatos se valoran por:",
   ["Órganos colegiados de carácter técnico.", "El titular del órgano convocante.", "Órganos unipersonales de carácter técnico.", "La Junta de Personal correspondiente."],
   "Art. 79.1 TREBEP.", "por órganos colegiados de carácter técnico"),
  ("RD364", "Artículo 41", "Concurso", "Según el artículo 41.2 del Real Decreto 364/1995, para poder participar en los concursos los funcionarios deberán permanecer en cada puesto de destino definitivo un mínimo de:",
   ["Dos años.", "Un año.", "Tres años.", "Seis meses."],
   "Art. 41.2 RD 364/1995 (y art. 20.1 f de la Ley 30/1984).", "un mínimo de dos años para poder participar en los concursos de provisión"),
  ("RD364", "Artículo 41", "Concurso", "Según el artículo 41.1 del Real Decreto 364/1995, pueden participar en los concursos los funcionarios cualquiera que sea su situación administrativa, excepto:",
   ["Los suspensos en firme, mientras dure la suspensión.", "Los excedentes voluntarios por interés particular.", "Los que se encuentren en servicios especiales.", "Los que estén en comisión de servicios."],
   "Art. 41.1 RD 364/1995.", "excepto los suspensos en firme que no podrán participar mientras dure la suspensión"),
  ("RD364", "Artículo 42", "Concurso", "Según el artículo 42.2 del Real Decreto 364/1995, el plazo de presentación de instancias en los concursos será de:",
   ["Quince días hábiles desde el siguiente al de la publicación de la convocatoria en el BOE.", "Diez días naturales desde la publicación de la convocatoria.", "Veinte días hábiles desde la publicación de la convocatoria.", "Un mes desde el siguiente al de la publicación de la convocatoria."],
   "Art. 42.2 RD 364/1995.", "El plazo de presentación de instancias será de quince días hábiles"),
  ("RD364", "Artículo 39", "Concurso", "Según el artículo 39 del Real Decreto 364/1995, autoriza las convocatorias de los concursos, a iniciativa de los Departamentos ministeriales:",
   ["La Secretaría de Estado para la Administración Pública.", "El Consejo de Ministros.", "La Comisión Superior de Personal.", "El Subsecretario de cada Departamento."],
   "Art. 39 RD 364/1995.", "La Secretaría de Estado para la Administración Pública, a iniciativa de los Departamentos ministeriales, autorizará las convocatorias de los concursos"),
  ("RD364", "Artículo 44", "Concurso", "Según el artículo 44.3 del Real Decreto 364/1995, la puntuación de cada uno de los conceptos valorables en el concurso:",
   ["No podrá exceder del 40 por 100 de la puntuación máxima total ni ser inferior al 10 por 100.", "No podrá exceder del 50 por 100 de la puntuación máxima total ni ser inferior al 10 por 100.", "No podrá exceder del 30 por 100 de la puntuación máxima total ni ser inferior al 5 por 100.", "No podrá exceder del 40 por 100 de la puntuación máxima total ni ser inferior al 20 por 100."],
   "Art. 44.3 RD 364/1995.", "no podrá exceder en ningún caso del 40 por 100 de la puntuación máxima total ni ser inferior al 10 por 100"),
  ("RD364", "Artículo 44", "Concurso", "Según el artículo 44.2 del Real Decreto 364/1995, puede puntuarse en el concurso el cuidado de hijos hasta que el hijo cumpla:",
   ["Doce años.", "Seis años.", "Ocho años.", "Dieciocho años."],
   "Art. 44.2 b) RD 364/1995.", "hasta que el hijo cumpla doce años"),
  ("RD364", "Artículo 45", "Concurso", "Según el artículo 45.5 del Real Decreto 364/1995, en los concursos específicos la valoración de los méritos se obtendrá:",
   ["Con la media aritmética de las puntuaciones de los miembros de la Comisión, desechando la máxima y la mínima.", "Con la puntuación otorgada por el Presidente de la Comisión.", "Con la suma de las puntuaciones de todos los miembros de la Comisión.", "Con la media aritmética de todas las puntuaciones, sin desechar ninguna."],
   "Art. 45.5 RD 364/1995.", "media aritmética de las otorgadas por cada uno de los miembros de la Comisión de Valoración, debiendo desecharse a estos efectos la máxima y la mínima"),
  ("RD364", "Artículo 46", "Concurso", "Según el artículo 46.1 del Real Decreto 364/1995, las Comisiones de Valoración estarán constituidas como mínimo por:",
   ["Cuatro miembros designados por la autoridad convocante.", "Tres miembros designados por la autoridad convocante.", "Cinco miembros, dos de ellos a propuesta de las organizaciones sindicales.", "Seis miembros designados por la Secretaría de Estado para la Administración Pública."],
   "Art. 46.1 RD 364/1995.", "como mínimo por cuatro miembros designados por la autoridad convocante"),
  ("RD364", "Artículo 47", "Concurso", "Según el artículo 47.1 del Real Decreto 364/1995, salvo que la convocatoria establezca otro distinto, el plazo para la resolución del concurso será de:",
   ["Dos meses desde el día siguiente al de la finalización del plazo de presentación de solicitudes.", "Un mes desde el día siguiente al de la finalización del plazo de presentación de solicitudes.", "Tres meses desde la publicación de la convocatoria.", "Seis meses desde la publicación de la convocatoria."],
   "Art. 47.1 RD 364/1995.", "El plazo para la resolución del concurso será de dos meses"),
  ("RD364", "Artículo 48", "Concurso", "Según el artículo 48.1 del Real Decreto 364/1995, el plazo para tomar posesión del nuevo destino, si implica cambio de residencia, será de:",
   ["Un mes.", "Tres días hábiles.", "Quince días hábiles.", "Ocho días."],
   "Art. 48.1 RD 364/1995: tres días hábiles sin cambio de residencia; un mes con cambio o reingreso.", "o de un mes si comporta cambio de residencia o el reingreso al servicio activo"),
  ("RD364", "Artículo 48", "Concurso", "Según el artículo 48.2 del Real Decreto 364/1995, el Subsecretario del Departamento donde preste servicios el funcionario podrá diferir el cese por necesidades del servicio hasta:",
   ["Veinte días hábiles.", "Tres meses.", "Un mes.", "Diez días hábiles."],
   "Art. 48.2 RD 364/1995. Los tres meses son el máximo del aplazamiento por la Secretaría de Estado.", "podrá diferir el cese por necesidades del servicio hasta veinte días hábiles"),
  ("RD364", "Artículo 49", "Concurso", "Según el artículo 49.1 del Real Decreto 364/1995, los destinos adjudicados en el concurso:",
   ["Son irrenunciables, salvo que antes de finalizar el plazo de toma de posesión se hubiere obtenido otro destino mediante convocatoria pública.", "Son renunciables hasta la toma de posesión.", "Son renunciables en el plazo de un mes desde la publicación de la resolución.", "Son irrenunciables en todo caso."],
   "Art. 49.1 RD 364/1995.", "Los destinos adjudicados serán irrenunciables, salvo que, antes de finalizar el plazo de toma de posesión, se hubiere obtenido otro destino mediante convocatoria pública"),
  ("RD364", "Artículo 50", "Concurso", "Según el artículo 50.1 del Real Decreto 364/1995, los funcionarios que accedan a un puesto por concurso podrán ser removidos por:",
   ["Una falta de capacidad para su desempeño manifestada por rendimiento insuficiente, que no comporte inhibición.", "Pérdida de la confianza de su superior jerárquico.", "Decisión discrecional del órgano que efectuó el nombramiento.", "Haber transcurrido cinco años desde el nombramiento."],
   "Art. 50.1 RD 364/1995: alteración del contenido del puesto o falta de capacidad por rendimiento insuficiente.", "falta de capacidad para su desempeño manifestada por rendimiento insuficiente, que no comporte inhibición"),
  ("RDL6", "Artículo 111", "Concurso", "Según el artículo 111 del Real Decreto-ley 6/2023, convocará los concursos unitarios, de carácter abierto y permanente:",
   ["La Secretaría de Estado de Función Pública, en colaboración con los departamentos ministeriales y organismos públicos.", "Cada departamento ministerial, para sus propios puestos.", "El Consejo de Ministros, a propuesta del Ministerio de Hacienda.", "La Comisión Superior de Personal."],
   "Art. 111 RDL 6/2023.", "La Secretaría de Estado de Función Pública, en colaboración con los departamentos ministeriales y organismos públicos, convocará concursos unitarios"),
  ("TREBEP", "Artículo 80", "Libre designación", "Según el artículo 80.1 del TREBEP, la libre designación con convocatoria pública consiste en:",
   ["La apreciación discrecional por el órgano competente de la idoneidad de los candidatos en relación con los requisitos exigidos para el desempeño del puesto.", "La valoración de los méritos y capacidades de los candidatos por órganos colegiados de carácter técnico.", "La apreciación reglada de los méritos de los candidatos por una Comisión de Valoración.", "El nombramiento directo por el Ministro sin necesidad de convocatoria."],
   "Art. 80.1 TREBEP. La valoración por órganos colegiados técnicos es la del concurso (art. 79).", "la apreciación discrecional por el órgano competente de la idoneidad de los candidatos"),
  ("RD364", "Artículo 51", "Libre designación", "Según el artículo 51.1 del Real Decreto 364/1995, la facultad de proveer los puestos de libre designación corresponde:",
   ["A los Ministros de los Departamentos de los que dependan y a los Secretarios de Estado en el ámbito de sus competencias.", "A los Subsecretarios de los Departamentos ministeriales.", "Al Consejo de Ministros, a propuesta del Ministro del Departamento.", "A la Secretaría de Estado para la Administración Pública."],
   "Art. 51.1 RD 364/1995.", "corresponde a los Ministros de los Departamentos de los que dependan y a los Secretarios de Estado en el ámbito de sus competencias"),
  ("RD364", "Artículo 54", "Libre designación", "Según el artículo 54.1 del Real Decreto 364/1995, si el informe del Departamento en que está destinado el funcionario no se emite en plazo, se considerará favorable transcurridos:",
   ["Quince días naturales.", "Quince días hábiles.", "Diez días naturales.", "Un mes."],
   "Art. 54.1 RD 364/1995.", "De no emitirse en el plazo de quince días naturales se considerará favorable"),
  ("RD364", "Artículo 56", "Libre designación", "Según el artículo 56.1 del Real Decreto 364/1995, los nombramientos de libre designación deberán efectuarse en el plazo máximo de:",
   ["Un mes desde la finalización del de presentación de solicitudes, prorrogable hasta un mes más.", "Dos meses desde la finalización del de presentación de solicitudes.", "Quince días hábiles desde la publicación de la convocatoria.", "Tres meses desde la publicación de la convocatoria."],
   "Art. 56.1 RD 364/1995.", "Los nombramientos deberán efectuarse en el plazo máximo de un mes contado desde la finalización del de presentación de solicitudes. Dicho plazo podrá prorrogarse hasta un mes más"),
  ("RDL6", "Artículo 127", "Personal directivo", "Según el artículo 127.2 del Real Decreto-ley 6/2023, el nombramiento del personal directivo público tendrá una duración máxima de:",
   ["Cinco años, renovable por períodos idénticos.", "Cuatro años, no renovable.", "Tres años, renovable una sola vez.", "Seis años, renovable por períodos de tres años."],
   "Art. 127.2 RDL 6/2023.", "tendrá una duración máxima de cinco años, que podrá ser renovable por períodos idénticos"),
  ("RDL6", "Artículo 127", "Personal directivo", "Según el artículo 127.3 del Real Decreto-ley 6/2023, la pérdida de la confianza como causa de cese del personal directivo público profesional:",
   ["Procede de forma excepcional.", "No está prevista como causa de cese.", "Es la causa ordinaria de cese.", "Solo procede a petición del interesado."],
   "Art. 127.3 g) RDL 6/2023.", "De forma excepcional, por pérdida de la confianza"),
  ("TREBEP", "Artículo 81", "Movilidad", "Según el artículo 81.3 del TREBEP, en caso de urgente e inaplazable necesidad, los puestos de trabajo podrán proveerse:",
   ["Con carácter provisional, debiendo procederse a su convocatoria pública dentro del plazo que señalen las normas aplicables.", "Con carácter definitivo, sin convocatoria pública.", "Por libre designación sin convocatoria.", "Mediante contratación laboral temporal."],
   "Art. 81.3 TREBEP.", "podrán proveerse con carácter provisional debiendo procederse a su convocatoria pública"),
  ("TREBEP", "Artículo 82", "Movilidad", "Según el artículo 82.1 del TREBEP, el traslado de la mujer víctima de violencia de género a otro puesto de trabajo propio de su cuerpo, escala o categoría:",
   ["Tendrá la consideración de traslado forzoso.", "Tendrá la consideración de traslado voluntario.", "Exige que la vacante sea de necesaria cobertura.", "Tendrá carácter provisional durante un año."],
   "Art. 82.1 TREBEP: «sin necesidad de que sea vacante de necesaria cobertura» y «Este traslado tendrá la consideración de traslado forzoso».", "Este traslado tendrá la consideración de traslado forzoso"),
  ("TREBEP", "Artículo 83", "Movilidad", "Según el artículo 83 del TREBEP, la provisión de puestos y movilidad del personal laboral se realizará:",
   ["De conformidad con los convenios colectivos y, en su defecto, por el sistema de provisión y movilidad del personal funcionario de carrera.", "Exclusivamente por el sistema de provisión del personal funcionario de carrera.", "Por libre designación en todo caso.", "De acuerdo con lo que disponga el Estatuto de los Trabajadores, sin que quepa aplicar el sistema funcionarial."],
   "Art. 83 TREBEP.", "de conformidad con lo que establezcan los convenios colectivos que sean de aplicación y, en su defecto por el sistema de provisión de puestos y movilidad del personal funcionario de carrera"),
  ("RD364", "Artículo 59", "Movilidad", "Según el artículo 59.1 del Real Decreto 364/1995, la redistribución de efectivos permite adscribir a funcionarios que ocupen con carácter definitivo puestos no singularizados a otros de la misma naturaleza, nivel de complemento de destino y complemento específico:",
   ["Sin que ello suponga cambio de municipio.", "Aunque suponga cambio de provincia.", "Con carácter provisional por un año.", "Previa conformidad de la Junta de Personal."],
   "Art. 59.1 RD 364/1995.", "sin que ello suponga cambio de municipio"),
  ("RD364", "Artículo 60", "Movilidad", "Según el artículo 60.3 del Real Decreto 364/1995, en la primera fase de la reasignación de efectivos, el Subsecretario podrá reasignar al funcionario en el plazo máximo de:",
   ["Seis meses desde la supresión del puesto de trabajo.", "Tres meses desde la supresión del puesto de trabajo.", "Un año desde la aprobación del Plan de Empleo.", "Dos meses desde la supresión del puesto de trabajo."],
   "Art. 60.3 RD 364/1995: seis meses (1.ª fase) y tres meses (2.ª fase).", "En el plazo máximo de seis meses desde la supresión del puesto de trabajo"),
  ("RD364", "Artículo 64", "Movilidad", "Según el artículo 64.3 del Real Decreto 364/1995, las comisiones de servicios tendrán una duración máxima de:",
   ["Un año prorrogable por otro en caso de no haberse cubierto el puesto con carácter definitivo.", "Seis meses prorrogables por otros seis.", "Dos años improrrogables.", "Un año improrrogable."],
   "Art. 64.3 RD 364/1995.", "duración máxima de un año prorrogable por otro en caso de no haberse cubierto el puesto con carácter definitivo"),
  ("RD364", "Artículo 64", "Movilidad", "Según el artículo 64.2 del Real Decreto 364/1995, cuando un concurso se declare desierto y sea urgente la provisión, podrá destinarse en comisión de servicios forzosa, en igualdad de condiciones, al funcionario:",
   ["De menor antigüedad.", "De mayor antigüedad.", "De mayor grado personal.", "Que lo solicite en primer lugar."],
   "Art. 64.2 RD 364/1995: municipio más próximo o mejor comunicado, menores cargas familiares y, en igualdad de condiciones, menor antigüedad.", "en igualdad de condiciones, al de menor antigüedad"),
  ("RD364", "Artículo 66 bis", "Movilidad", "Según el artículo 66 bis del Real Decreto 364/1995, la adscripción por motivos de salud o rehabilitación está condicionada a que exista puesto vacante cuyo nivel de complemento de destino y específico:",
   ["No sea superior al del puesto de origen.", "Sea igual al del puesto de origen.", "No sea inferior en más de dos niveles al del puesto de origen.", "Sea superior al del puesto de origen."],
   "Art. 66 bis.2 RD 364/1995.", "cuyo nivel de complemento de destino y específico no sea superior al del puesto de origen"),
  ("TREBEP", "Artículo 16", "Carrera", "Según el artículo 16.3 a) del TREBEP, la carrera horizontal consiste en:",
   ["La progresión de grado, categoría, escalón u otros conceptos análogos, sin necesidad de cambiar de puesto de trabajo.", "El ascenso en la estructura de puestos de trabajo por los procedimientos de provisión.", "El ascenso desde un cuerpo o escala de un Subgrupo a otro superior.", "El acceso a cuerpos o escalas del mismo Subgrupo profesional."],
   "Art. 16.3 a) TREBEP. Las demás opciones definen la carrera vertical y las promociones internas vertical y horizontal.", "Carrera horizontal, que consiste en la progresión de grado, categoría, escalón u otros conceptos análogos, sin necesidad de cambiar de puesto de trabajo"),
  ("TREBEP", "Artículo 16", "Carrera", "Según el artículo 16.3 b) del TREBEP, la carrera vertical consiste en:",
   ["El ascenso en la estructura de puestos de trabajo por los procedimientos de provisión.", "La progresión de grado sin necesidad de cambiar de puesto de trabajo.", "El ascenso desde un cuerpo o escala de un Subgrupo a otro superior.", "La progresión en tramos retribuidos con el complemento de carrera."],
   "Art. 16.3 b) TREBEP.", "Carrera vertical, que consiste en el ascenso en la estructura de puestos de trabajo por los procedimientos de provisión"),
  ("RDL6", "Artículo 122", "Carrera", "Según el artículo 122.2 del Real Decreto-ley 6/2023, en cada grupo o subgrupo de personal funcionario la carrera horizontal tendrá:",
   ["Cuatro tramos.", "Tres tramos.", "Cinco tramos.", "Seis tramos."],
   "Art. 122.2 a) RDL 6/2023.", "En cada grupo o subgrupo de personal funcionario existirán 4 tramos"),
  ("RDL6", "Artículo 122", "Carrera", "Según el artículo 122.2 c) del Real Decreto-ley 6/2023, para ascender al tramo superior se exige un periodo mínimo de servicios efectivos de:",
   ["Cinco años en el caso del primer tramo y seis años en los siguientes.", "Seis años en el caso del primer tramo y cinco en los siguientes.", "Cuatro años en todos los tramos.", "Cinco años en todos los tramos."],
   "Art. 122.2 c) RDL 6/2023.", "un periodo mínimo de cinco años de servicios efectivos en el caso del primer tramo y de seis años en los siguientes"),
  ("RDL6", "Artículo 122", "Carrera", "Según el artículo 122.6 del Real Decreto-ley 6/2023, los efectos económicos del reconocimiento de cada tramo de carrera horizontal se producirán:",
   ["A partir del 1 de enero del año siguiente.", "Desde la fecha de la solicitud.", "Desde la fecha de la resolución de reconocimiento.", "A partir del mes siguiente al de la resolución."],
   "Art. 122.6 b) RDL 6/2023.", "a partir del 1 de enero del año siguiente"),
  ("RD364", "Artículo 70", "Grado personal", "Según el artículo 70.2 del Real Decreto 364/1995, los funcionarios adquieren el grado personal por el desempeño de uno o más puestos del nivel correspondiente durante:",
   ["Dos años continuados o tres con interrupción.", "Tres años continuados o cuatro con interrupción.", "Un año continuado o dos con interrupción.", "Dos años continuados, sin que quepa interrupción."],
   "Art. 70.2 RD 364/1995.", "durante dos años continuados o tres con interrupción"),
  ("RD364", "Artículo 70", "Grado personal", "Según el artículo 70.11 del Real Decreto 364/1995, el reconocimiento del grado personal se efectuará por:",
   ["El Subsecretario del Departamento donde preste servicios el funcionario.", "El Ministro del Departamento donde preste servicios el funcionario.", "El Registro Central de Personal.", "La Secretaría de Estado para la Administración Pública."],
   "Art. 70.11 RD 364/1995.", "El reconocimiento del grado personal se efectuará por el Subsecretario del Departamento donde preste servicios el funcionario"),
  ("TREBEP", "Artículo 18", "Promoción interna", "Según el artículo 18.2 del TREBEP, para la promoción interna los funcionarios deberán tener una antigüedad de, al menos:",
   ["Dos años de servicio activo en el inferior Subgrupo, o Grupo de clasificación profesional si este no tiene Subgrupo.", "Tres años de servicio activo en el inferior Subgrupo.", "Dos años de servicios efectivos en cualquier Administración Pública.", "Cinco años de servicio activo en el mismo cuerpo o escala."],
   "Art. 18.2 TREBEP.", "tener una antigüedad de, al menos, dos años de servicio activo en el inferior Subgrupo"),
  ("RD364", "Artículo 74", "Promoción interna", "Según el artículo 74.1 del Real Decreto 364/1995, la promoción interna se efectuará mediante el sistema de:",
   ["Oposición o concurso-oposición.", "Concurso de méritos.", "Concurso, oposición o concurso-oposición.", "Libre designación con convocatoria pública."],
   "Art. 74.1 RD 364/1995.", "mediante el sistema de oposición o concurso-oposición"),
  ("RD364", "Artículo 78", "Promoción interna", "Según el artículo 78.1 del Real Decreto 364/1995, los funcionarios que accedan a otros Cuerpos y Escalas por el turno de promoción interna tendrán, respecto de los puestos vacantes de la respectiva convocatoria:",
   ["Preferencia sobre los aspirantes que no procedan de este turno.", "Los mismos derechos que los aspirantes de acceso libre, según la puntuación obtenida.", "Preferencia solo si tienen grado personal consolidado.", "Derecho a elegir después de los aspirantes de acceso libre."],
   "Art. 78.1 RD 364/1995.", "tendrán, en todo caso, preferencia para cubrir los puestos vacantes de la respectiva convocatoria sobre los aspirantes que no procedan de este turno"),
  ("RD364", "Artículo 79", "Promoción interna", "Según el artículo 79 del Real Decreto 364/1995, las vacantes convocadas para promoción interna que queden desiertas, salvo en convocatorias independientes:",
   ["Se acumularán a las que se ofrezcan al resto de los aspirantes de acceso libre.", "Se incluirán en la oferta de empleo público del año siguiente.", "Se amortizarán.", "Se cubrirán por concurso de traslados."],
   "Art. 79 RD 364/1995.", "se acumularán a las que se ofrezcan al resto de los aspirantes de acceso libre"),
]
for k_, a_, cat_, q_, o_, e_, f_ in Q: T.q(k_, a_, cat_, q_, o_, e_, f_)
T.real("L", 63, "Carrera"); T.real("P", 82, "Carrera"); T.real("L", 68, "Concurso"); T.real("L", 67, "Personal directivo")
T.real("X", 71, "Personal directivo"); T.real("X", 76, "Personal directivo"); T.real("X", 73, "Libre designación")
T.real("X", 66, "Movilidad"); T.real("X", 74, "Grado personal")

# Flashcards
for q_, a_, cat in [
  ("Principios de la provisión de puestos (TREBEP, art. 78.1)", "Igualdad, mérito, capacidad y publicidad.", "Provisión"),
  ("¿Desde cuándo producen efectos los arts. 78 a 84 del TREBEP?", "Desde la entrada en vigor de las leyes de Función Pública de desarrollo; mientras, siguen las normas vigentes que no se opongan (disposición final cuarta).", "Provisión"),
  ("Formas de provisión en la AGE (RD 364/1995, art. 36)", "Concurso (normal) y libre designación; redistribución y reasignación de efectivos; temporalmente, comisión de servicios y adscripción provisional.", "Provisión"),
  ("Permanencia mínima para concursar (RD 364/1995, art. 41.2)", "Dos años en el puesto de destino definitivo, salvo en el ámbito de una Secretaría de Estado o Departamento, remoción y supresión del puesto.", "Concurso"),
  ("Límites de cada concepto del baremo (art. 44.3)", "No más del 40 % de la puntuación máxima total ni menos del 10 %.", "Concurso"),
  ("Concurso específico (art. 45)", "Dos fases: méritos generales y méritos específicos (con memoria o entrevista); media aritmética desechando la máxima y la mínima.", "Concurso"),
  ("Plazos del concurso", "Solicitudes: 15 días hábiles; resolución: 2 meses; toma de posesión: 3 días hábiles o un mes.", "Concurso"),
  ("Concurso unitario (RDL 6/2023, art. 111)", "Lo convoca la Secretaría de Estado de Función Pública; es abierto y permanente.", "Concurso"),
  ("Remoción del puesto de concurso (art. 50)", "Por alteración del contenido del puesto o por rendimiento insuficiente que no comporte inhibición; parecer de la Junta de Personal.", "Concurso"),
  ("Puestos de libre designación en la AGE (art. 51.2)", "Subdirector general, Delegados y Directores territoriales o provinciales, Secretarías de Altos Cargos y otros directivos o de especial responsabilidad según la RPT.", "Libre designación"),
  ("Cese en libre designación (art. 58)", "Discrecional; adscripción provisional a un puesto no inferior en más de dos niveles a su grado, en el mismo municipio (salvo destinados en el exterior).", "Libre designación"),
  ("Personal directivo público profesional (RDL 6/2023, art. 127)", "Libre designación sin cobertura provisional; solicitudes en 10 días naturales; máximo cinco años renovables.", "Personal directivo"),
  ("Redistribución de efectivos (art. 59)", "Puestos no singularizados, misma naturaleza y nivel, sin cambio de municipio; destino definitivo.", "Movilidad"),
  ("Fases de la reasignación de efectivos (art. 60)", "1.ª Subsecretario (6 meses); 2.ª Secretaría de Estado (3 meses); 3.ª expectativa de destino.", "Movilidad"),
  ("Supuestos de adscripción provisional (art. 63)", "Remoción o cese, supresión del puesto y reingreso sin reserva de puesto.", "Movilidad"),
  ("Comisión de servicios (art. 64)", "Voluntaria (urgente e inaplazable necesidad) o forzosa (concurso desierto); un año prorrogable otro; reserva del puesto.", "Movilidad"),
  ("Modalidades de carrera (TREBEP, art. 16.3)", "Carrera horizontal, carrera vertical, promoción interna vertical y promoción interna horizontal.", "Carrera"),
  ("Carrera del personal laboral (TREBEP, art. 19)", "Derecho a la promoción profesional, por el Estatuto de los Trabajadores o los convenios colectivos.", "Carrera"),
  ("Carrera horizontal en la AGE (RDL 6/2023, art. 122)", "Voluntaria; cuatro tramos; 5 años el primero y 6 los siguientes; convocatoria anual; complemento de carrera.", "Carrera"),
  ("Consolidación del grado personal (RD 364/1995, art. 70)", "Dos años continuados o tres con interrupción; lo reconoce el Subsecretario.", "Grado personal"),
  ("Promoción interna: requisitos y sistemas", "Dos años en el Subgrupo inferior (TREBEP, art. 18.2); oposición o concurso-oposición (RD 364/1995, art. 74).", "Promoción interna"),
  ("Plazas de promoción interna en la OEP (RDL 6/2023, art. 108.3)", "No inferior al 30 % de las plazas de acceso libre.", "Promoción interna"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Concurso", "Procedimiento normal de provisión: valoración de méritos y capacidades por órganos colegiados de carácter técnico (TREBEP, art. 79; RD 364/1995, art. 36.1).", "s3", "Provisión")
T.glos("Concurso específico", "Concurso en dos fases, la segunda de méritos específicos del puesto, con memoria o entrevista si la convocatoria lo prevé (RD 364/1995, art. 45).", "s5", "Provisión")
T.glos("Concurso unitario abierto y permanente", "Concurso que convoca la Secretaría de Estado de Función Pública para favorecer la ocupación de plazas de necesaria cobertura y la movilidad (RDL 6/2023, art. 111).", "s4", "Provisión")
T.glos("Libre designación", "Apreciación discrecional por el órgano competente de la idoneidad de los candidatos, con convocatoria pública; cese discrecional (TREBEP, art. 80).", "s7", "Provisión")
T.glos("Personal directivo público profesional", "En la AGE, entre otros, los titulares de subdirecciones generales; se nombra por libre designación, sin cobertura provisional (RDL 6/2023, arts. 123.3 y 127).", "s8", "Provisión")
T.glos("Puesto no singularizado", "El que no se individualiza o distingue de los restantes en las relaciones de puestos de trabajo (RD 364/1995, art. 59.1).", "s10", "Movilidad")
T.glos("Redistribución de efectivos", "Adscripción por necesidades del servicio a otro puesto no singularizado de igual naturaleza y nivel, sin cambio de municipio; definitiva (RD 364/1995, art. 59).", "s10", "Movilidad")
T.glos("Reasignación de efectivos", "Destino de funcionarios cuyo puesto se suprime por un Plan de Empleo, en tres fases; definitiva (RD 364/1995, art. 60).", "s10", "Movilidad")
T.glos("Adscripción provisional", "Cobertura temporal solo en caso de remoción o cese, supresión del puesto o reingreso sin reserva (RD 364/1995, art. 63).", "s11", "Movilidad")
T.glos("Comisión de servicios", "Cobertura temporal de un puesto vacante, voluntaria o forzosa, de un año prorrogable otro, con reserva del puesto de origen (RD 364/1995, art. 64).", "s11", "Movilidad")
T.glos("Carrera profesional", "Conjunto ordenado de oportunidades de ascenso y expectativas de progreso profesional conforme a igualdad, mérito y capacidad (TREBEP, art. 16.2).", "s15", "Carrera")
T.glos("Tramo", "Etapa sucesiva de reconocimiento del desarrollo profesional en la carrera horizontal de la AGE; hay cuatro por grupo o subgrupo (RDL 6/2023, art. 122).", "s16", "Carrera")
T.glos("Grado personal", "Nivel que el funcionario consolida por desempeñar puestos de ese nivel dos años continuados o tres con interrupción; garantiza como mínimo su complemento de destino (RD 364/1995, art. 70).", "s17", "Carrera")
T.glos("Promoción interna", "Ascenso desde un cuerpo o escala a otro del grupo inmediato superior, o acceso a otro del mismo grupo (RD 364/1995, art. 73; TREBEP, art. 16.3 c y d).", "s18", "Promoción interna")

# Cronología (fechas de los metadatos del BOE y de los títulos de las normas)
T.hito("1984", "Ley 30/1984, de 2 de agosto, de medidas para la reforma de la Función Pública (BOE de 3-8-1984)", "Art. 20: provisión de puestos; párrafos no incluidos en la derogatoria del TREBEP", "normativo", "s1")
T.hito("1995", "Real Decreto 364/1995, de 10 de marzo: Reglamento General de Ingreso, Provisión de Puestos y Promoción Profesional de la AGE (BOE de 10-4-1995)", "Títulos III (provisión), IV (carrera: grado) y V (promoción interna)", "normativo", "s2")
T.hito("2007", "Ley 7/2007, de 12 de abril, del Estatuto Básico del Empleado Público", "Derogada por el TREBEP, que la refunde", "normativo", "s1")
T.hito("2015", "Real Decreto Legislativo 5/2015, de 30 de octubre: texto refundido del EBEP (BOE de 31-10-2015)", "Arts. 16 a 19 (carrera y promoción) y 78 a 84 (provisión y movilidad), con efectos diferidos", "normativo", "s1")
T.hito("2023", "Real Decreto-ley 6/2023, de 19 de diciembre (BOE de 20-12-2023)", "Libro segundo: concurso unitario, carrera horizontal por tramos, personal directivo público profesional y 30 % de promoción interna", "normativo", "s16")

T.publicar()
