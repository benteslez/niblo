# -*- coding: utf-8 -*-
"""Tema I.3 (B1T03): El Tribunal Constitucional. Organización, composición y atribuciones.
Método del I.2: mapa → bloques (I a IV) con guía; cada artículo, texto literal del
BOE + ficha de casillas fijas; cierre 1 (preguntas oficiales) y cierre 2 (repaso).
Normas (textos consolidados del BOE): CE, Título IX (arts. 159 a 165) y art. 95;
Ley Orgánica 2/1979, del Tribunal Constitucional (LOTC). Apoyo de una pregunta oficial:
Ley 7/1985 (LRBRL), art. 106.2, y LJCA, art. 1.1 (solo citas en línea)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

L = "LOTC"
# Bloques de la LOTC (los artículos van en letra en el BOE)
A = {1: "aprimero", 2: "asegundo", 3: "atercero", 4: "acuarto", 5: "aquinto", 6: "asexto", 7: "aseptimo", 8: "aoctavo",
     9: "anoveno", 10: "adiez", 11: "aonce", 12: "adoce", 13: "atrece", 14: "acatorce", 15: "aquince", 16: "adieciseis",
     17: "adiecisiete", 18: "adieciocho", 19: "adiecinueve", 20: "aveinte", 21: "aveintiuno", 22: "aveintidos",
     23: "aveintitres", 24: "aveinticuatro", 26: "aveintiseis", 27: "aveintisiete", 29: "aveintinueve", 30: "atreinta",
     31: "atreintayuno", 32: "atreintaydos", 33: "atreintaytres", 34: "atreintaycuatro", 35: "atreintaycinco",
     37: "atreintaysiete", 38: "atreintayocho", 39: "atreintaynueve", 40: "acuarenta", 41: "acuarentayuno",
     42: "acuarentaydos", 43: "acuarentaytres", 44: "acuarentaycuatro", 46: "acuarentayseis", 48: "acuarentayocho",
     50: "acincuenta", 59: "acincuentaynueve", 60: "asesenta", 62: "asesentaydos", 63: "asesentaytres",
     73: "asetentaytres", 75: "asetentaycincobis", 751: "asetentaycincoter", 752: "asetentaycincoquater",
     76: "asetentayseis", 77: "asetentaysiete", 78: "asetentayocho", 79: "asetentaynueve", 86: "aochentayseis",
     87: "aochentaysiete", 90: "anoventa", 92: "anoventaydos", 93: "anoventaytres", 96: "anoventayseis"}
def ll(n, resaltar=(), solo=None, nombre=None):
    """Bloque literal de la LOTC con cabecera legible: «Artículo 16 (LOTC)»."""
    num = nombre or (str(n) if n < 700 else {751: "75 ter", 752: "75 quater"}[n])
    if n == 75: num = "75 bis"
    return lit(L, A[n], resaltar, solo=solo, titulo=f"Artículo {num} (LOTC)")
def cl(n, frag): return c(L, A[n], frag)
def cc(n, frag): return c("CE", f"Artículo {n}", frag)

T = Tema("B1T03",
  "Cuatro preguntas: I. Qué es el Tribunal Constitucional (art. 165 CE; LOTC, arts. 1 a 4) · II. Quiénes lo componen (arts. 159 y 160 CE; LOTC, arts. 5, 9 y 16 a 26) · III. Cómo se organiza y funciona (LOTC, arts. 6 a 15, 90 y 96) · IV. Qué atribuciones tiene y cómo las ejerce (arts. 95 y 161 a 164 CE; LOTC). Cada artículo: texto literal del BOE y ficha.",
  ["Título IX CE", "LOTC", "Art. 159", "12 Magistrados", "Nueve años", "Presidente del TC", "Pleno, Salas y Secciones", "Recurso de inconstitucionalidad", "Cuestión de inconstitucionalidad", "Amparo", "Conflictos de competencia", "Art. 161.2", "Autonomía local", "Tratados", "Recurso previo"])

# =============================================================================
T.ap("s0", "Mapa del tema: cuatro preguntas", """
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque I, tema 3):
> El Tribunal Constitucional. Organización, composición y atribuciones.

### El hilo conductor

El epígrafe se lee como **cuatro preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Constitución | Ley Orgánica 2/1979, del Tribunal Constitucional (LOTC) |
|---|---|---|---|
| **I** | ¿Qué es el Tribunal Constitucional? | Art. 165 | Arts. 1 a 4 y 10.3 |
| **II** | ¿Quiénes lo componen? (composición) | Arts. 159 y 160 | Arts. 5, 9 y 16 a 26 |
| **III** | ¿Cómo se organiza y funciona? (organización) | — | Arts. 6 a 15, 90 y 96 |
| **IV** | ¿Qué atribuciones tiene y cómo las ejerce? (atribuciones) | Arts. 95 y 161 a 164 | Arts. 2, 27 a 50, 59 a 79, 86, 87, 92 y 93 |

!> **La idea que une los cuatro bloques:** el Tribunal Constitucional es el **intérprete supremo de la Constitución** y está sometido solo a ella y a su ley orgánica (I). Por eso su **composición** busca la independencia: doce Magistrados propuestos por **cuatro** órganos distintos, con mandato largo y estatuto blindado (II). Trabaja en **Pleno, Salas y Secciones** (III) y sus **atribuciones** son tasadas: controla las leyes, protege los derechos en amparo y resuelve conflictos (IV).

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen).
- Los esquemas y cuadros **no son texto legal**: resumen los artículos citados.
- Fronteras con otros temas: el recurso de amparo y las garantías de los derechos se estudian a fondo en el tema I.2 (aquí, solo lo esencial); el Consejo General del Poder Judicial, en el tema I.7; las Comunidades Autónomas, en los temas I.10 y I.11.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué es el Tribunal Constitucional? (art. 165 CE; LOTC, arts. 1 a 4)", donde(
  "Primera pregunta del tema. Antes de ver quién lo compone o qué hace, hay que saber **qué es**: un órgano constitucional que la Constitución regula en su **Título IX** (arts. 159 a 165) y que una **ley orgánica** desarrolla.",
  ["1 Una ley orgánica propia (art. 165 CE)", "2 Intérprete supremo, independiente y único (LOTC, art. 1)", "3 Jurisdicción propia y autonomía (LOTC, arts. 2.2, 3, 4 y 10.3)"]))

T.ap("s1", "I.1 Una ley orgánica propia (art. 165 CE)", f"""
La Constitución regula lo básico del Tribunal en el Título IX y remite el resto a una ley orgánica: hoy, la Ley Orgánica 2/1979, de 3 de octubre, del Tribunal Constitucional (LOTC).

{unidad("1.1 Lo que regula la ley orgánica (art. 165)",
  lit("CE", "Artículo 165", ["Una ley orgánica", "el funcionamiento del Tribunal Constitucional, el estatuto de sus miembros, el procedimiento ante el mismo y las condiciones para el ejercicio de las acciones"]),
  fichab("Reserva de ley orgánica para el Tribunal Constitucional",
         "Las Cortes Generales, mediante ley orgánica (la LOTC)",
         ["::Cuatro materias:", "El funcionamiento del Tribunal", "El estatuto de sus miembros", "El procedimiento ante el mismo", "Las condiciones para el ejercicio de las acciones"],
         "Ley **orgánica**",
         "Son **cuatro** materias y la norma es una **ley orgánica**, no un reglamento del propio Tribunal (los reglamentos del TC solo pueden dictarse «dentro del ámbito de la presente Ley»: → I.3.1)."))}
""", 2)

T.ap("s2", "I.2 Intérprete supremo, independiente y único (LOTC, art. 1)", f"""
{unidad("2.1 Naturaleza del Tribunal (LOTC, art. 1)",
  ll(1, ["intérprete supremo de la Constitución", "está sometido sólo a la Constitución y a la presente Ley Orgánica", "Es único en su orden"]),
  fichab("Posición del Tribunal Constitucional",
         "El Tribunal Constitucional",
         [f"::{cl(1, 'como intérprete supremo de la Constitución')}:", f"{cl(1, 'es independiente de los demás órganos constitucionales')}", f"{cl(1, 'está sometido sólo a la Constitución y a la presente Ley Orgánica')}", f"{cl(1, 'Es único en su orden')} y su jurisdicción alcanza a todo el territorio nacional"],
         "—",
         "Está sometido **solo** a la Constitución **y a la LOTC** (no «a la ley» en general). Es el intérprete **supremo** de la Constitución. La jurisdicción en todo el territorio la dice también el art. 161.1 CE (→ IV.1.1)."))}
""", 2)

T.ap("s3", "I.3 Jurisdicción propia y autonomía (LOTC, arts. 2.2, 3, 4 y 10.3)", f"""
{unidad("3.1 Potestad reglamentaria propia (LOTC, art. 2.2)",
  ll(2, ["podrá dictar reglamentos sobre su propio funcionamiento y organización", "aprobados por el Tribunal en Pleno"], solo=[12]),
  fichab("Reglamentos del Tribunal Constitucional",
         "El Tribunal **en Pleno** los aprueba; los autoriza su **Presidente**",
         "Sobre su funcionamiento y organización y el régimen de su personal y servicios, dentro del ámbito de la LOTC",
         "Se publican en el «Boletín Oficial del Estado»",
         "Los aprueba el **Pleno** (no las Salas) y los autoriza el **Presidente** para su publicación en el BOE."))}

{unidad("3.2 Cuestiones prejudiciales e incidentales (LOTC, art. 3)",
  ll(3, ["a los solos efectos del enjuiciamiento constitucional de ésta"]),
  fichab("Extensión de la competencia del Tribunal",
         "El Tribunal Constitucional",
         f"Conoce de cuestiones {cl(3, 'no pertenecientes al orden constitucional, directamente relacionadas con la materia de que conoce')}",
         "—",
         "Solo **a los efectos** del enjuiciamiento constitucional: no resuelve esas cuestiones con carácter general."))}

{unidad("3.3 Nadie le discute la jurisdicción (LOTC, art. 4)",
  ll(4, ["En ningún caso se podrá promover cuestión de jurisdicción o competencia al Tribunal Constitucional", "no podrán ser enjuiciadas por ningún órgano jurisdiccional del Estado", "previa audiencia al Ministerio Fiscal y al órgano autor del acto o resolución"]),
  fichab("Defensa de la jurisdicción del Tribunal",
         "El propio Tribunal Constitucional (las anulaciones del art. 4.3 son del **Pleno**: → III.2.1)",
         ["Él mismo delimita el ámbito de su jurisdicción y puede anular los actos o resoluciones que la menoscaben", "Aprecia su competencia o incompetencia de oficio o a instancia de parte", "Anula motivadamente y previa audiencia al Ministerio Fiscal y al órgano autor"],
         "—",
         "**Nadie** puede plantearle cuestión de jurisdicción o competencia, y **ningún** órgano jurisdiccional del Estado puede enjuiciar sus resoluciones."))}

{unidad("3.4 Presupuesto propio (LOTC, art. 10.3)",
  ll(10, ["en ejercicio de su autonomía como órgano constitucional", "sección independiente dentro de los Presupuestos Generales del Estado"], solo=[18]),
  fichab("Autonomía presupuestaria",
         "El Tribunal **en Pleno**",
         "Elabora su presupuesto",
         "Se integra como sección independiente en los Presupuestos Generales del Estado",
         "La LOTC lo llama **órgano constitucional** con **autonomía**; su presupuesto es una **sección independiente** de los Presupuestos Generales del Estado."))}

{resumen([
  "La Constitución lo regula en el **Título IX** (arts. 159 a 165) y remite a una **ley orgánica** su funcionamiento, el estatuto de sus miembros, el procedimiento y las acciones (165).",
  "**Intérprete supremo de la Constitución**, independiente, sometido **solo a la Constitución y a la LOTC**, único en su orden (LOTC, art. 1).",
  "Nadie le plantea cuestiones de jurisdicción; sus resoluciones no las enjuicia ningún órgano jurisdiccional (art. 4); dicta sus **reglamentos** y elabora su **presupuesto** en Pleno (arts. 2.2 y 10.3)."],
  "Siguiente: II. ¿Quiénes lo componen?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Quiénes lo componen? (arts. 159 y 160 CE; LOTC, arts. 5, 9 y 16 a 26)", donde(
  "Segunda pregunta: la **composición**. Es la parte que más cae: cuántos Magistrados, quién los propone, con qué mayoría, por cuánto tiempo y con qué incompatibilidades.",
  ["1 Doce Magistrados: quién propone y quién nombra", "2 Requisitos", "3 Mandato y renovación", "4 Incompatibilidades e independencia", "5 Presidente y Vicepresidente", "6 Juramento, cese, suspensión y responsabilidad"]))

T.ap("s4", "II.1 Doce Magistrados: quién los propone y quién los nombra (art. 159.1 CE; LOTC, arts. 5 y 16.1 y 2)", f"""
{unidad("1.1 Composición y propuestas (art. 159.1)",
  lit("CE", "Artículo 159", ["12 miembros nombrados por el Rey", "cuatro a propuesta del Congreso por mayoría de tres quintos de sus miembros", "cuatro a propuesta del Senado, con idéntica mayoría", "dos a propuesta del Gobierno", "dos a propuesta del Consejo General del Poder Judicial"], solo=[1]),
  fichab("Composición del Tribunal",
         f"{cc(159, '12 miembros nombrados por el Rey')}",
         ["::Proponen:", "Congreso: 4, por mayoría de tres quintos de sus miembros", "Senado: 4, con idéntica mayoría", "Gobierno: 2", "Consejo General del Poder Judicial: 2"],
         "Tres quintos de los miembros de cada Cámara para sus cuatro propuestas; la Constitución no fija mayoría para el Gobierno ni para el CGPJ",
         "**4 + 4 + 2 + 2**. Nombra el **Rey**; proponen **cuatro** órganos. El CGPJ propone (no el Presidente del Tribunal Supremo). Cayó en 2025 (→ Cierre 1)."))}

{unidad("1.2 Doce Magistrados (LOTC, art. 5)",
  ll(5, ["doce miembros", "Magistrados del Tribunal Constitucional"]),
  fichab("Título de los miembros", "Los doce miembros del Tribunal", f"Llevan {cl(5, 'el título de Magistrados del Tribunal Constitucional')}", "—", "Son **doce**, también en la LOTC."))}

{unidad("1.3 Propuestas con presencia equilibrada; candidatos del Senado; comparecencias (LOTC, art. 16.1 y 2)",
  ll(16, ["como mínimo un cuarenta por ciento de cada uno de los sexos", "entre las candidaturas presentadas por las Asambleas Legislativas de las comunidades autónomas", "deberán comparecer previamente ante las correspondientes Comisiones"], solo=[1, 2, 3, 4]),
  fichab("Cómo se hacen las propuestas",
         "Las Cámaras, el Gobierno y el Consejo General del Poder Judicial proponen; el Rey nombra",
         ["Cada órgano proponente garantiza la presencia equilibrada de mujeres y hombres", "Los del **Senado**, elegidos entre las candidaturas de las **Asambleas Legislativas** de las comunidades autónomas", "Los candidatos del Congreso y del Senado **comparecen** antes ante las Comisiones"],
         f"Mínimo {cl(16, 'un cuarenta por ciento de cada uno de los sexos')} en las propuestas",
         "Las **Asambleas autonómicas** presentan candidaturas solo para los Magistrados que propone el **Senado**. La comparecencia previa es para los del **Congreso y el Senado**, no para los del Gobierno ni los del CGPJ."))}
""", 2)

T.ap("s5", "II.2 Requisitos para ser Magistrado (art. 159.2 CE; LOTC, art. 18)", f"""
{unidad("2.1 Juristas de reconocida competencia (art. 159.2)",
  lit("CE", "Artículo 159", ["Magistrados y Fiscales, Profesores de Universidad, funcionarios públicos y Abogados", "con más de quince años de ejercicio profesional"], solo=[2]),
  fichab("Requisitos constitucionales",
         "Magistrados y Fiscales, Profesores de Universidad, funcionarios públicos y Abogados",
         f"Todos {cc(159, 'juristas de reconocida competencia')}",
         f"{cc(159, 'con más de quince años de ejercicio profesional')}",
         "**Más de quince** años (no diez ni doce). Son **cuatro** procedencias: Magistrados y Fiscales, Profesores de Universidad, funcionarios públicos y Abogados."))}

{unidad("2.2 Españoles y en activo (LOTC, art. 18)",
  ll(18, ["ciudadanos españoles", "o en activo en la respectiva función"]),
  fichab("Requisitos de la LOTC",
         f"{cl(18, 'ciudadanos españoles')} de las procedencias del art. 159.2 CE",
         "Juristas de reconocida competencia",
         f"{cl(18, 'con más de quince años de ejercicio profesional o en activo en la respectiva función')}",
         "La LOTC añade que sean **ciudadanos españoles** y precisa los quince años: de ejercicio profesional **o en activo** en la función."))}
""", 2)

T.ap("s6", "II.3 Mandato y renovación (art. 159.3 CE; LOTC, arts. 16.3 a 5 y 17)", f"""
{unidad("3.1 Nueve años, renovación por tercios (art. 159.3)",
  lit("CE", "Artículo 159", ["por un período de nueve años", "se renovarán por terceras partes cada tres"], solo=[3]),
  fichab("Duración del mandato", "Los Magistrados", "Designación por nueve años; el Tribunal se renueva por tercios", f"{cc(159, 'nueve años')}; renovación {cc(159, 'por terceras partes cada tres')}",
         "**Nueve** años de mandato; se renueva **un tercio** (cuatro Magistrados) **cada tres** años."))}

{unidad("3.2 Reelección, vacantes y retrasos (LOTC, art. 16.3 a 5)",
  ll(16, ["por nueve años, renovándose el Tribunal por terceras partes cada tres", "salvo que hubiera ocupado el cargo por un plazo no superior a tres años", "por el tiempo que a éste restase"], solo=[5, 6, 7]),
  fichab("Reglas del mandato",
         "Los Magistrados; el órgano que propuso al que causa vacante",
         ["Prohibida la propuesta para otro período inmediato, salvo mandato no superior a tres años", "Vacante anticipada: mismo procedimiento que para el Magistrado que la causa y por el tiempo que le restase", "Si la renovación se retrasa, a los nuevos se les resta del mandato el tiempo de retraso", "Tras cada renovación se eligen Presidente y Vicepresidente (art. 9)"],
         "Mandato de nueve años; reelección inmediata solo si se ocupó el cargo **tres años o menos**",
         "El sustituto de una vacante **termina el mandato** del anterior (no empieza uno nuevo de nueve años)."))}

{unidad("3.3 Inicio de la renovación y prórroga de funciones (LOTC, art. 17)",
  ll(17, ["Antes de los cuatro meses previos a la fecha de expiración de los nombramientos", "continuarán en el ejercicio de sus funciones hasta que hayan tomado posesión quienes hubieren de sucederles"]),
  fichab("Procedimiento de renovación",
         "El **Presidente del Tribunal** lo solicita a los Presidentes de los órganos proponentes",
         "Solicitud de inicio del procedimiento de designación; los salientes siguen en funciones",
         f"{cl(17, 'Antes de los cuatro meses previos a la fecha de expiración de los nombramientos')}",
         "**Cuatro meses** antes. Los Magistrados salientes **no cesan** hasta que toman posesión sus sucesores."))}
""", 2)

T.ap("s7", "II.4 Incompatibilidades e independencia (art. 159.4 y 5 CE; LOTC, arts. 19, 20 y 22)", f"""
{unidad("4.1 Incompatibilidades e independencia en la Constitución (art. 159.4 y 5)",
  lit("CE", "Artículo 159", ["con todo mandato representativo", "con el ejercicio de las carreras judicial y fiscal", "las incompatibilidades propias de los miembros del poder judicial", "independientes e inamovibles"], solo=[4, 5, 6]),
  fichab("Estatuto constitucional del Magistrado",
         "Los miembros del Tribunal Constitucional",
         ["::Incompatible con:", "Todo mandato representativo", "Los cargos políticos o administrativos", "Funciones directivas en un partido político o en un sindicato y el empleo a su servicio", "El ejercicio de las carreras judicial y fiscal", "Cualquier actividad profesional o mercantil"],
         "—",
         "En lo demás, las incompatibilidades **de los miembros del poder judicial**. Son **independientes e inamovibles** en el ejercicio de su mandato."))}

{unidad("4.2 La lista de la LOTC y el plazo para optar (LOTC, art. 19)",
  ll(19, ["con el de Defensor del Pueblo", "con el de Diputado y Senador", "en el plazo de diez días siguientes a la propuesta"]),
  fichab("Incompatibilidades legales",
         "El propuesto o el Magistrado en quien concurra la causa",
         ["::Siete incompatibilidades (art. 19.1):", "Defensor del Pueblo", "Diputado y Senador", "Cualquier cargo político o administrativo del Estado, las Comunidades Autónomas, las provincias u otras Entidades locales", "Jurisdicción o actividad propia de la carrera judicial o fiscal", "Empleos en Tribunales y Juzgados", "Funciones directivas en partidos, sindicatos, asociaciones, fundaciones y colegios profesionales, y empleo a su servicio", "Actividades profesionales o mercantiles"],
         f"Debe cesar antes de tomar posesión; si no lo hace {cl(19, 'en el plazo de diez días siguientes a la propuesta')}, se entiende que no acepta",
         "**Diez días** desde la **propuesta**. La misma regla se aplica a la incompatibilidad **sobrevenida**."))}

{unidad("4.3 Servicios especiales (LOTC, art. 20)",
  ll(20, ["situación de servicios especiales"]),
  fichab("Situación en la carrera de origen", "Jueces, fiscales y funcionarios nombrados Magistrados **o letrados** del Tribunal", f"Pasan a la {cl(20, 'situación de servicios especiales en su carrera de origen')}", "—", "**Servicios especiales**, no excedencia. Vale también para los **letrados**."))}

{unidad("4.4 Imparcialidad, inviolabilidad e inamovilidad (LOTC, art. 22)",
  ll(22, ["imparcialidad y dignidad", "no podrán ser perseguidos por las opiniones expresadas en el ejercicio de sus funciones", "serán inamovibles"]),
  fichab("Garantías del ejercicio de la función", "Los Magistrados",
         ["Imparcialidad y dignidad", "No pueden ser perseguidos por las opiniones expresadas en el ejercicio de sus funciones", "Inamovibles: solo destituidos o suspendidos por las causas de la LOTC (→ II.6.2 y → II.6.3)"],
         "—", "La inamovilidad se concreta en que solo cesan o se suspenden por las causas **tasadas** de los arts. 23 y 24."))}
""", 2)

T.ap("s8", "II.5 Presidente y Vicepresidente (art. 160 CE; LOTC, art. 9)", f"""
{unidad("5.1 El Presidente en la Constitución (art. 160)",
  lit("CE", "Artículo 160", ["entre sus miembros por el Rey", "a propuesta del mismo Tribunal en pleno", "por un período de tres años"]),
  fichab("Nombramiento del Presidente", f"Lo nombra {cc(160, 'el Rey')}; lo propone {cc(160, 'el mismo Tribunal en pleno')}", "Entre los propios Magistrados", f"{cc(160, 'por un período de tres años')}",
         "Lo propone el **Tribunal en Pleno** (no el Gobierno ni las Cámaras) y dura **tres** años."))}

{unidad("5.2 Elección del Presidente y del Vicepresidente (LOTC, art. 9)",
  ll(9, ["por votación secreta", "En primera votación se requerirá la mayoría absoluta", "podrá ser reelegido por una sola vez", "un Vicepresidente"]),
  fichab("Procedimiento de elección",
         "El Tribunal **en Pleno** elige; el **Rey** nombra al Presidente",
         ["Votación secreta", "1.ª votación: mayoría absoluta; 2.ª: más votos; empate: última votación y, si persiste, el de mayor antigüedad en el cargo y, a igualdad, el de mayor edad", "El Vicepresidente se elige por el mismo procedimiento y período"],
         "Tres años; reelegible **por una sola vez**",
         "Reelección **una sola vez**. El Vicepresidente sustituye al Presidente y **preside la Sala Segunda**."))}
""", 2)

T.ap("s9", "II.6 Juramento, cese, suspensión y responsabilidad (LOTC, arts. 21, 23, 24 y 26)", f"""
{unidad("6.1 Juramento o promesa (LOTC, art. 21)",
  ll(21, ["ante el Rey"]),
  fichab("Toma de posesión", "El Presidente y los demás Magistrados", f"Juramento o promesa {cl(21, 'al asumir su cargo ante el Rey')}", "—", "Se jura **ante el Rey**, no ante las Cortes."))}

{unidad("6.2 Causas de cese (LOTC, art. 23)",
  ll(23, ["por renuncia aceptada por el Presidente del Tribunal", "por mayoría simple en los casos tercero y cuarto", "por mayoría de las tres cuartas partes de sus miembros en los demás casos"]),
  fichab("Cese de los Magistrados",
         "El **Presidente** (renuncia, expiración del plazo y fallecimiento) o el **Pleno** (los demás casos)",
         ["::Siete causas:", "Renuncia aceptada por el Presidente", "Expiración del plazo", "Incapacidad prevista para los miembros del Poder Judicial", "Incompatibilidad sobrevenida", "Falta de diligencia", "Violación de la reserva de su función", "Responsabilidad civil por dolo o condena por delito doloso o por culpa grave"],
         "Pleno: **mayoría simple** en incapacidad e incompatibilidad sobrevenida; **tres cuartas partes** de sus miembros en los demás",
         "Renuncia, expiración y fallecimiento: lo **decreta el Presidente**. Las causas disciplinarias exigen **tres cuartos** del Pleno."))}

{unidad("6.3 Suspensión (LOTC, art. 24)",
  ll(24, ["en caso de procesamiento", "las tres cuartas partes de los miembros del Tribunal reunido en Pleno"]),
  fichab("Suspensión como medida previa", "El Tribunal en Pleno",
         "En caso de procesamiento o por el tiempo indispensable para resolver sobre una causa de cese", f"{cl(24, 'el voto favorable de las tres cuartas partes de los miembros del Tribunal reunido en Pleno')}",
         "**Tres cuartas partes** de los miembros, en **Pleno**."))}

{unidad("6.4 Responsabilidad criminal (LOTC, art. 26)",
  ll(26, ["Sala de lo Penal del Tribunal Supremo"]),
  fichab("Fuero de los Magistrados", "La Sala de lo Penal del Tribunal Supremo", "Solo ante ella es exigible la responsabilidad criminal", "—", "Sala de lo **Penal** del **Tribunal Supremo** (no el propio TC ni la Audiencia Nacional)."))}

{resumen([
  "**12** Magistrados nombrados por el **Rey**: **4** a propuesta del Congreso y **4** del Senado (tres quintos), **2** del Gobierno y **2** del CGPJ (159.1).",
  "Juristas de reconocida competencia con **más de quince años** de ejercicio (159.2); **nueve** años, renovación **por tercios cada tres** (159.3).",
  "Incompatibles con todo mandato representativo, cargos políticos o administrativos, cargos en partidos y sindicatos, carreras judicial y fiscal y actividad profesional o mercantil; **independientes e inamovibles** (159.4 y 5).",
  "Presidente: elegido por el **Pleno**, nombrado por el **Rey**, **tres** años, reelegible **una vez** (160; LOTC, art. 9).",
  "Cese disciplinario y suspensión: **tres cuartos** del Pleno; responsabilidad criminal: **Sala de lo Penal del Tribunal Supremo**."],
  "Siguiente: III. ¿Cómo se organiza y funciona?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Cómo se organiza y funciona? (LOTC, arts. 6 a 15, 90 y 96)", donde(
  "Tercera pregunta: la **organización**. La Constitución no la regula: está en la LOTC. El Tribunal actúa en **Pleno**, en **dos Salas** y en **Secciones**, y cada formación tiene sus asuntos.",
  ["1 Pleno, Salas y Secciones", "2 Qué conoce el Pleno y qué las Salas", "3 Quórum, Presidente, votaciones y personal", "4 Cuadro de la organización"]))

T.ap("s10", "III.1 Pleno, Salas y Secciones (LOTC, arts. 6 a 8)", f"""
{unidad("1.1 Tres formaciones; el Pleno (LOTC, art. 6)",
  ll(6, ["actúa en Pleno, en Sala o en Sección", "todos los Magistrados del Tribunal"]),
  fichab("Formaciones del Tribunal", "Pleno: **todos** los Magistrados", "Lo preside el Presidente; en su defecto, el Vicepresidente; a falta de ambos, el Magistrado más antiguo en el cargo y, a igual antigüedad, el de mayor edad", "—",
         "Orden de sustitución en el Pleno: Presidente → **Vicepresidente** → más **antiguo** → mayor **edad**."))}

{unidad("1.2 Dos Salas de seis Magistrados (LOTC, art. 7)",
  ll(7, ["dos Salas", "seis Magistrados nombrados por el Tribunal en Pleno", "de la Sala Primera", "presidirá en la Sala Segunda"]),
  fichab("Las Salas", "Seis Magistrados en cada una, nombrados por el **Pleno**",
         ["Sala Primera: la preside el Presidente del Tribunal", "Sala Segunda: la preside el Vicepresidente"], "—",
         "**Dos** Salas de **seis**. Presidente → Sala **Primera**; Vicepresidente → Sala **Segunda**."))}

{unidad("1.3 Secciones de tres (LOTC, art. 8)",
  ll(8, ["el respectivo Presidente o quien le sustituya y dos Magistrados", "asuntos de amparo"]),
  fichab("Las Secciones", "El Presidente del Pleno o de la Sala (o quien le sustituya) y dos Magistrados",
         ["Despacho ordinario y admisibilidad de los procesos", "Asuntos de amparo que les defiera la Sala"], "—",
         "Las Secciones son de **tres** (Presidente y **dos** Magistrados). Deciden sobre la **admisión**; del Pleno se da cuenta de las propuestas de admisión de sus asuntos."))}
""", 2)

T.ap("s11", "III.2 Qué conoce el Pleno y qué las Salas (LOTC, arts. 10 a 13)", f"""
{unidad("2.1 Competencias del Pleno (LOTC, art. 10.1 y 2)",
  ll(10, ["De la constitucionalidad o inconstitucionalidad de los tratados internacionales", "excepto los de mera aplicación de doctrina", "De las cuestiones de constitucionalidad que reserve para sí", "De la recusación de los Magistrados", "a propuesta del Presidente o de tres Magistrados"], solo=list(range(1, 18))),
  fichab("Asuntos del Pleno",
         "El Tribunal en Pleno",
         ["Tratados internacionales; recursos de inconstitucionalidad (salvo mera aplicación de doctrina); cuestiones que reserve para sí", "Conflictos de competencia, entre órganos constitucionales y en defensa de la autonomía local; impugnaciones del art. 161.2 CE; recursos previos contra Estatutos", "Asuntos internos: verificación de nombramientos, composición de las Salas, recusación, cese, reglamentos", "Lo que recabe para sí a propuesta del Presidente o de **tres** Magistrados"],
         "—",
         "Las **cuestiones** de inconstitucionalidad que el Pleno no reserva para sí van a las **Salas** por turno objetivo. En conflictos de competencia, impugnaciones del 161.2 y autonomía local, la decisión de fondo puede atribuirse a una Sala (10.2)."))}

{unidad("2.2 Competencias de las Salas y reparto (LOTC, arts. 11 y 12)",
  ll(11, ["no sean de la competencia del Pleno"]),
  ll(12, ["según un turno establecido por el Pleno a propuesta de su Presidente"]),
  fichab("Asuntos de las Salas", "Las dos Salas", "Lo que no es del Pleno (en especial, el amparo: → IV.5) y lo que las Secciones les eleven por su importancia",
         "Reparto por turno fijado por el **Pleno** a propuesta del Presidente",
         "Competencia **residual**: las Salas conocen de lo que **no** es del Pleno."))}

{unidad("2.3 Cambio de doctrina (LOTC, art. 13)",
  ll(13, ["la cuestión se someterá a la decisión del Pleno"]),
  fichab("Unidad de doctrina", "La Sala que quiera apartarse; decide el Pleno", f"Cuando una Sala considere necesario {cl(13, 'apartarse en cualquier punto de la doctrina constitucional precedente')}", "—",
         "Para cambiar la doctrina decide el **Pleno**, no la Sala."))}
""", 2)

T.ap("s12", "III.3 Quórum, Presidente, votaciones y personal (LOTC, arts. 14, 15, 90 y 96)", f"""
{unidad("3.1 Quórum (LOTC, art. 14)",
  ll(14, ["dos tercios de los miembros que en cada momento lo compongan", "la presencia de dos miembros"]),
  fichab("Presencia necesaria para adoptar acuerdos", "Pleno, Salas y Secciones",
         ["Pleno y Salas: al menos **dos tercios** de sus miembros", "Secciones: **dos** miembros; si hay discrepancia, los **tres**"], "—",
         "**Dos tercios** de los miembros **que en cada momento** lo compongan (no de los doce)."))}

{unidad("3.2 Funciones del Presidente (LOTC, art. 15)",
  ll(15, ["ejerce la representación del Tribunal", "comunica a las Cámaras, al Gobierno o al Consejo General del Poder Judicial, en cada caso, las vacantes", "nombra a los letrados"]),
  fichab("Atribuciones del Presidente", "El Presidente del Tribunal Constitucional",
         ["Representa al Tribunal; convoca y preside el Pleno; convoca las Salas", "Adopta las medidas para el funcionamiento del Tribunal, las Salas y las Secciones", "Comunica las vacantes a los órganos proponentes", "Nombra a los letrados; convoca los concursos de personal; ejerce las potestades administrativas sobre el personal"],
         "—", "El Presidente **nombra a los letrados** y comunica las vacantes."))}

{unidad("3.3 Mayoría y voto particular (LOTC, art. 90)",
  ll(90, ["por la mayoría de los miembros del Pleno, Sala o Sección que participen en la deliberación", "decidirá el voto del Presidente", "voto particular"]),
  fichab("Cómo se adoptan las decisiones", "Pleno, Sala o Sección",
         ["Mayoría de los que participen en la deliberación, salvo regla especial", "Empate: decide el voto del Presidente", "Voto particular de la opinión discrepante defendida en la deliberación; se publica con la resolución en el BOE"],
         "Mayoría de los **participantes** en la deliberación", "**Voto de calidad** del Presidente en caso de empate."))}

{unidad("3.4 Personal al servicio del Tribunal (LOTC, art. 96.1 y 2)",
  ll(96, ["El Secretario General", "Los letrados"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Funcionarios del Tribunal", "Secretario General, letrados, secretarios de justicia y demás funcionarios adscritos",
         "Se rigen por la LOTC y su Reglamento; supletoriamente, por la legislación del personal de la Administración de Justicia", "—",
         "Supletoria: la legislación de la **Administración de Justicia**."))}
""", 2)

T.ap("s13", "III.4 Cuadro de la organización (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Formación | Composición | Preside | Asuntos (ejemplos) | Quórum |
|---|---|---|---|---|
| **Pleno** | Los doce Magistrados (art. 6.2) | Presidente; Vicepresidente; el más antiguo; el de mayor edad | Tratados, recursos de inconstitucionalidad, conflictos, art. 161.2, recursos previos, reglamentos, recusación, cese (art. 10) | Dos tercios (art. 14) |
| **Salas** (2) | Seis Magistrados nombrados por el Pleno (art. 7.1) | Primera: el Presidente; Segunda: el Vicepresidente | Lo que no es del Pleno, como el amparo (arts. 11 y 48) | Dos tercios (art. 14) |
| **Secciones** | Presidente respectivo y dos Magistrados (art. 8.1) | El Presidente del Pleno o de la Sala | Admisión; amparos que la Sala les defiera (art. 8) | Dos; tres si hay discrepancia (art. 14) |

{resumen([
  "Actúa en **Pleno** (doce), en **dos Salas** (seis) y en **Secciones** (tres) (arts. 6 a 8).",
  "El **Pleno** conoce de tratados, recursos de inconstitucionalidad, conflictos e impugnaciones del 161.2; las **Salas**, de lo demás, como el amparo; para cambiar doctrina, el **Pleno** (arts. 10 a 13).",
  "Quórum de **dos tercios**; decisiones por **mayoría** de los participantes; en empate decide el **Presidente** (arts. 14 y 90)."],
  "Siguiente: IV. ¿Qué atribuciones tiene y cómo las ejerce?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Qué atribuciones tiene y cómo las ejerce? (arts. 95 y 161 a 164 CE; LOTC)", donde(
  "Cuarta pregunta: las **atribuciones**. La Constitución da la lista básica (art. 161) y la legitimación (art. 162); la LOTC la completa y regula cada proceso. Aquí se ven en lo esencial: **qué se impugna, quién, en qué plazo y con qué efectos**.",
  ["1 El catálogo de atribuciones", "2 Recurso de inconstitucionalidad", "3 Cuestión de inconstitucionalidad", "4 Sentencias de inconstitucionalidad", "5 Recurso de amparo (lo esencial)", "6 Conflictos de competencia", "7 Conflictos entre órganos constitucionales y en defensa de la autonomía local", "8 Impugnación del art. 161.2", "9 Tratados y recurso previo contra Estatutos", "10 Resoluciones y su cumplimiento", "11 Cuadro de legitimación y plazos"]))

T.ap("s14", "IV.1 El catálogo de atribuciones (art. 161.1 CE; LOTC, art. 2.1)", f"""
{unidad("1.1 Lo que dice la Constitución (art. 161.1)",
  lit("CE", "Artículo 161", ["tiene jurisdicción en todo el territorio español", "Del recurso de inconstitucionalidad contra leyes y disposiciones normativas con fuerza de ley", "Del recurso de amparo", "De los conflictos de competencia entre el Estado y las Comunidades Autónomas o de los de éstas entre sí", "De las demás materias que le atribuyan la Constitución o las leyes orgánicas"], solo=[1, 2, 3, 4, 5]),
  fichab("Competencias constitucionales del Tribunal",
         "El Tribunal Constitucional",
         ["Recurso de inconstitucionalidad", "Recurso de amparo (derechos del art. 53.2)", "Conflictos de competencia Estado-Comunidades Autónomas o entre estas", "Las demás que le atribuyan la Constitución o las **leyes orgánicas**"],
         "—",
         "La lista **no es cerrada**: se amplía por la Constitución (p. ej., art. 161.2 → IV.8; art. 95 → IV.9) o por **ley orgánica**."))}

{unidad("1.2 Lo que añade la LOTC (art. 2.1)",
  ll(2, ["De los conflictos entre los órganos constitucionales del Estado", "De los conflictos en defensa de la autonomía local", "De la declaración sobre la constitucionalidad de los tratados internacionales", "Del control previo de inconstitucionalidad", "De la verificación de los nombramientos de los Magistrados"], solo=list(range(1, 12))),
  fichab("Catálogo legal de atribuciones",
         "El Tribunal Constitucional",
         ["Recurso y cuestión de inconstitucionalidad (→ IV.2 y → IV.3)", "Amparo (→ IV.5)", "Conflictos de competencia, entre órganos constitucionales y en defensa de la autonomía local (→ IV.6 y → IV.7)", "Tratados internacionales y control previo de Estatutos (→ IV.9)", "Impugnaciones del art. 161.2 CE (→ IV.8)", "Verificación de los nombramientos de sus Magistrados"],
         "—",
         "La LOTC añade a la Constitución: conflictos **entre órganos constitucionales**, conflictos **en defensa de la autonomía local**, **control previo** de Estatutos y verificación de nombramientos."))}
""", 2)

T.ap("s15", "IV.2 Recurso de inconstitucionalidad (arts. 161.1 a) y 162.1 a) CE; LOTC, arts. 27 a 34)", f"""
{unidad("2.1 Qué normas se controlan (LOTC, art. 27)",
  ll(27, ["garantiza la primacía de la Constitución", "Los Estatutos de Autonomía y las demás Leyes orgánicas", "Los Tratados Internacionales", "Los Reglamentos de las Cámaras y de las Cortes Generales", "Los Reglamentos de las Asambleas legislativas de las Comunidades Autónomas"]),
  fichab("Objeto del control de constitucionalidad",
         "El Tribunal Constitucional",
         ["::Son susceptibles de declaración de inconstitucionalidad (27.2):", "Estatutos de Autonomía y demás leyes orgánicas", "Demás leyes, disposiciones normativas y actos del Estado con fuerza de ley", "Tratados internacionales", "Reglamentos de las Cámaras y de las Cortes Generales", "Leyes y disposiciones con fuerza de ley de las Comunidades Autónomas", "Reglamentos de las Asambleas legislativas autonómicas"],
         "—",
         "Normas con **rango o fuerza de ley** y reglamentos **parlamentarios**. Un reglamento del Gobierno o una **ordenanza** local no están en la lista. Cayó en 2025 (→ Cierre 1)."))}

{unidad("2.2 Dos vías y efecto no suspensivo (LOTC, arts. 29.1 y 30)",
  ll(29, ["El recurso de inconstitucionalidad", "La cuestión de inconstitucionalidad promovida por Jueces o Tribunales"], solo=[1, 2, 3]),
  ll(30, ["no suspenderá la vigencia ni la aplicación de la Ley", "excepto en el caso en que el Gobierno se ampare en lo dispuesto por el artículo ciento sesenta y uno, dos"]),
  fichab("Cómo se promueve y qué efecto tiene la admisión",
         "Recurso: los legitimados del art. 162.1 a) CE; cuestión: Jueces o Tribunales",
         "Recurso de inconstitucionalidad o cuestión de inconstitucionalidad",
         "—",
         "La admisión **no suspende** la ley, **salvo** que el Gobierno invoque el **art. 161.2 CE** contra leyes de una Comunidad Autónoma."))}

{unidad("2.3 Quién puede interponerlo (art. 162.1 a) CE; LOTC, art. 32)",
  lit("CE", "Artículo 162", ["el Presidente del Gobierno, el Defensor del Pueblo, 50 Diputados, 50 Senadores, los órganos colegiados ejecutivos de las Comunidades Autónomas y, en su caso, las Asambleas de las mismas"], solo=[1, 2]),
  ll(32, ["Cincuenta Diputados", "Cincuenta Senadores", "que puedan afectar a su propio ámbito de autonomía", "previo acuerdo adoptado al efecto"]),
  fichab("Legitimación",
         ["Presidente del Gobierno", "Defensor del Pueblo", "50 Diputados", "50 Senadores", "Órganos colegiados ejecutivos y Asambleas de las Comunidades Autónomas: contra leyes del Estado que puedan afectar a su propio ámbito de autonomía, previo acuerdo"],
         "Demanda ante el Tribunal Constitucional",
         "—",
         "**Cincuenta** Diputados o **cincuenta** Senadores. **No** están legitimados los ciudadanos (ellos acuden en **amparo**) ni los jueces (plantean la **cuestión**). Cayó en 2025 (→ Cierre 1)."))}

{unidad("2.4 Plazo (LOTC, arts. 31 y 33)",
  ll(31, ["a partir de su publicación oficial"]),
  ll(33, ["dentro del plazo de tres meses a partir de la publicación", "en el plazo de nueve meses", "Comisión Bilateral de Cooperación"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Plazo de interposición",
         "Los legitimados; el plazo ampliado, solo el **Presidente del Gobierno** y los **órganos colegiados ejecutivos** de las Comunidades Autónomas",
         "Demanda que identifica a los recurrentes, la norma impugnada y el precepto constitucional infringido",
         ["**Tres meses** desde la publicación", "**Nueve meses** si se reúne la Comisión Bilateral de Cooperación, acuerda iniciar negociaciones y se comunica al Tribunal en los tres meses siguientes a la publicación"],
         "Tres meses desde la **publicación** (no desde la entrada en vigor). Los nueve meses no valen para Diputados, Senadores ni Defensor del Pueblo."))}

{unidad("2.5 Tramitación (LOTC, art. 34)",
  ll(34, ["al Congreso de los Diputados y al Senado por conducto de sus Presidentes, al Gobierno por conducto del Ministerio de Justicia", "en el plazo de quince días", "en ningún caso, podrá exceder de treinta días"]),
  fichab("Procedimiento", "El Tribunal; se personan las Cámaras, el Gobierno y, si la norma es autonómica, los órganos legislativo y ejecutivo de la Comunidad",
         "Traslado de la demanda y alegaciones", "Alegaciones: **15 días**; sentencia: **10 días** (ampliable por resolución motivada, nunca más de **30**)",
         "Traslado al Gobierno **por conducto del Ministerio de Justicia**."))}
""", 2)

T.ap("s16", "IV.3 Cuestión de inconstitucionalidad (art. 163 CE; LOTC, arts. 35 y 37)", f"""
{unidad("3.1 La cuestión en la Constitución (art. 163)",
  lit("CE", "Artículo 163", ["Cuando un órgano judicial considere", "una norma con rango de ley, aplicable al caso, de cuya validez dependa el fallo", "que en ningún caso serán suspensivos"]),
  fichab("Control de constitucionalidad a instancia de los jueces",
         c("CE", "Artículo 163", "un órgano judicial"),
         "Plantea la cuestión ante el Tribunal Constitucional sobre una norma con rango de ley aplicable al caso y de cuya validez dependa el fallo",
         "—",
         "Los efectos que fije la ley **en ningún caso serán suspensivos** (art. 163). Ojo: la LOTC sí suspende el **proceso judicial** (→ IV.3.2), no la ley."))}

{unidad("3.2 Planteamiento por el juez (LOTC, art. 35)",
  ll(35, ["de oficio o a instancia de parte", "una vez concluso el procedimiento y dentro del plazo para dictar sentencia", "en el plazo común e improrrogable de 10 días", "suspensión provisional de las actuaciones en el proceso judicial"]),
  fichab("Requisitos y trámite ante el juez",
         "Juez o Tribunal, de oficio o a instancia de parte",
         ["Concluso el procedimiento y dentro del plazo para dictar sentencia", "Concreta la norma, el precepto constitucional y el juicio de relevancia", "Oye a las partes y al Ministerio Fiscal y resuelve por auto, sin recurso"],
         "Audiencia: **10 días** comunes e improrrogables; resolución: **3 días**",
         "Se plantea **concluso** el procedimiento. El auto **no admite recurso**, pero la cuestión puede intentarse en las sucesivas instancias. El proceso judicial queda **suspendido**."))}

{unidad("3.3 Admisión y tramitación en el Tribunal (LOTC, art. 37)",
  ll(37, ["sin otra audiencia que la del Fiscal General del Estado", "notoriamente infundada", "plazo común improrrogable de quince días"], solo=[1, 3]),
  fichab("Procedimiento ante el Tribunal", "El Tribunal; alegan las Cámaras, el Fiscal General del Estado, el Gobierno y, si la norma es autonómica, sus órganos legislativo y ejecutivo",
         "Puede rechazarla en admisión, por auto motivado, si faltan condiciones procesales o es notoriamente infundada",
         "Alegaciones: **15 días** comunes e improrrogables; sentencia: **15 días** (ampliable a 30 como máximo)",
         "En el rechazo de admisión solo se oye al **Fiscal General del Estado**."))}
""", 2)

T.ap("s17", "IV.4 Sentencias de inconstitucionalidad (art. 164 CE; LOTC, arts. 38 a 40)", f"""
{unidad("4.1 Publicación y efectos (art. 164)",
  lit("CE", "Artículo 164", ["con los votos particulares", "a partir del día siguiente de su publicación", "no cabe recurso alguno contra ellas", "plenos efectos frente a todos", "subsistirá la vigencia de la ley en la parte no afectada"]),
  fichab("Valor de las sentencias del Tribunal",
         "El Tribunal Constitucional; se publican en el BOE",
         ["Cosa juzgada y sin recurso", "Plenos efectos frente a todos: las que declaran inconstitucional una ley o norma con fuerza de ley y las que no se limitan a la estimación subjetiva de un derecho", "Salvo que el fallo diga otra cosa, la ley subsiste en la parte no afectada"],
         f"Cosa juzgada {cc(164, 'a partir del día siguiente de su publicación')}",
         "Desde el **día siguiente** a su publicación. Se publican **con los votos particulares**."))}

{unidad("4.2 Vinculación y efectos generales (LOTC, art. 38)",
  ll(38, ["vincularán a todos los Poderes Públicos", "desde la fecha de su publicación", "fundado en la misma infracción de idéntico precepto constitucional"]),
  fichab("Efectos de las sentencias de inconstitucionalidad", "Todos los poderes públicos; en la cuestión, el órgano judicial y las partes",
         ["Cosa juzgada, vinculación a todos los poderes públicos y efectos generales", "La desestimatoria de un recurso (o de un conflicto en defensa de la autonomía local) impide replantear la misma infracción del mismo precepto por cualquiera de las dos vías"],
         "Efectos generales desde la publicación en el BOE",
         "Lo que impide el replanteamiento es la sentencia **desestimatoria** de un **recurso** (o de un conflicto de autonomía local), no la de una cuestión."))}

{unidad("4.3 Nulidad (LOTC, art. 39)",
  ll(39, ["declarará igualmente la nulidad de los preceptos impugnados", "por conexión o consecuencia", "haya o no sido invocado en el curso del proceso"]),
  fichab("Contenido de la sentencia estimatoria", "El Tribunal",
         ["Inconstitucionalidad = nulidad de los preceptos impugnados y, por conexión o consecuencia, de otros de la misma norma", "Puede fundarse en cualquier precepto constitucional, invocado o no"], "—",
         "El Tribunal **no** está limitado a los preceptos constitucionales invocados."))}

{unidad("4.4 Procesos fenecidos (LOTC, art. 40)",
  ll(40, ["no permitirán revisar procesos fenecidos mediante sentencia con fuerza de cosa juzgada", "salvo en el caso de los procesos penales o contencioso-administrativos referentes a un procedimiento sancionador"]),
  fichab("Efectos sobre sentencias firmes anteriores", "Jueces y Tribunales",
         ["No se revisan procesos fenecidos con sentencia firme", "Excepción: procesos penales o contencioso-administrativos sancionadores en que resulte reducción de la pena o sanción o exclusión, exención o limitación de la responsabilidad", "La jurisprudencia se entiende corregida por la doctrina del Tribunal"], "—",
         "Única excepción: lo **sancionador** (penal o contencioso) **favorable** al condenado o sancionado."))}
""", 2)

T.ap("s18", "IV.5 Recurso de amparo: lo esencial (arts. 161.1 b) y 162.1 b) CE; LOTC, arts. 41 a 50)", f"""
El amparo se estudia a fondo en el tema I.2 (garantías de los derechos). Aquí, lo que lo sitúa entre las atribuciones del Tribunal.

{unidad("5.1 Legitimación constitucional (art. 162.1 b)",
  lit("CE", "Artículo 162", ["toda persona natural o jurídica que invoque un interés legítimo, así como el Defensor del Pueblo y el Ministerio Fiscal"], solo=[3]),
  fichab("Quién puede pedir amparo",
         ["Toda persona natural o jurídica que invoque un interés legítimo", "El Defensor del Pueblo", "El Ministerio Fiscal"],
         "Recurso de amparo por violación de los derechos del art. 53.2 CE (art. 161.1 b)", "—",
         "Persona **natural o jurídica** con **interés legítimo**. El Defensor del Pueblo está legitimado **en los dos** recursos (inconstitucionalidad y amparo); el **Ministerio Fiscal**, solo en el amparo."))}

{unidad("5.2 Qué derechos protege y frente a qué (LOTC, art. 41.1 y 2)",
  ll(41, ["artículos catorce a veintinueve", "objeción de conciencia", "disposiciones, actos jurídicos, omisiones o simple vía de hecho de los poderes públicos"], solo=[1, 2]),
  fichab("Objeto del amparo", "Frente a los poderes públicos del Estado, las Comunidades Autónomas y demás entes públicos, y sus funcionarios o agentes",
         "Derechos de los **arts. 14 a 29** y objeción de conciencia del **art. 30**", "—",
         "Arts. **14 a 29** + **objeción de conciencia** (art. 30). Sin perjuicio de la tutela general de los Tribunales de Justicia."))}

{unidad("5.3 Plazos según el origen de la violación (LOTC, arts. 42, 43.2 y 44.2)",
  ll(42, ["dentro del plazo de tres meses"]),
  ll(43, ["veinte días siguientes a la notificación"], solo=[2]),
  ll(44, ["será de 30 días"], solo=[5]),
  fichab("Plazos del amparo", "Quien haya sido parte en el proceso judicial o la persona afectada; también el Defensor del Pueblo y el Ministerio Fiscal (LOTC, art. 46)",
         ["Actos sin valor de ley de las Cortes o de las Asambleas autonómicas (42)", "Actos del Gobierno o de las Administraciones, tras agotar la vía judicial (43)", "Actos u omisiones de un órgano judicial (44)"],
         ["Parlamentario: **3 meses** desde que sean firmes", "Gubernativo o administrativo: **20 días** desde la notificación de la resolución judicial", "Judicial: **30 días** desde la notificación"],
         "**3 meses / 20 días / 30 días**: es el cruce de plazos que más se pregunta."))}

{unidad("5.4 Admisión: la especial trascendencia constitucional (LOTC, arts. 48 y 50.1)",
  ll(48, ["corresponde a las Salas del Tribunal Constitucional y, en su caso, a las Secciones"]),
  ll(50, ["por unanimidad de sus miembros", "especial trascendencia constitucional"], solo=[1, 2, 3]),
  fichab("Quién conoce y cuándo se admite", "Salas y, en su caso, Secciones; la Sección admite por **unanimidad**",
         "La demanda debe cumplir los arts. 41 a 46 y 49 y el recurso debe tener **especial trascendencia constitucional**", "—",
         "El amparo es de las **Salas** (no del Pleno). Sin **especial trascendencia constitucional** no se admite."))}
""", 2)

T.ap("s19", "IV.6 Conflictos de competencia (art. 161.1 c) CE; LOTC, arts. 59 a 63)", f"""
{unidad("6.1 Clases de conflictos (LOTC, art. 59)",
  ll(59, ["Al Estado con una o más Comunidades Autónomas", "A dos o más Comunidades Autónomas entre sí", "Al Gobierno con el Congreso de los Diputados, el Senado o el Consejo General del Poder Judicial", "conflictos en defensa de la autonomía local"]),
  fichab("Conflictos constitucionales",
         "El Tribunal Constitucional",
         ["De competencia: Estado-Comunidades Autónomas o Comunidades entre sí", "Entre órganos constitucionales: Gobierno, Congreso, Senado y Consejo General del Poder Judicial (→ IV.7.1)", "En defensa de la autonomía local: municipios y provincias frente al Estado o una Comunidad (→ IV.7.2)"],
         "—",
         "Los órganos del conflicto de atribuciones son **cuatro**: Gobierno, Congreso, Senado y **CGPJ**."))}

{unidad("6.2 Quién los plantea (LOTC, art. 60)",
  ll(60, ["por el Gobierno o por los órganos colegiados ejecutivos de las Comunidades Autónomas", "Los conflictos negativos podrán ser instados también por las personas físicas o jurídicas interesadas"]),
  fichab("Legitimación en los conflictos de competencia", "Gobierno y órganos colegiados ejecutivos autonómicos; en los negativos, también los particulares interesados",
         "Conflicto positivo o negativo", "—", "En los **negativos** pueden instarlos también **personas físicas o jurídicas**."))}

{unidad("6.3 Plazos del conflicto positivo (LOTC, arts. 62 y 63)",
  ll(62, ["en el plazo de dos meses", "sin perjuicio de que el Gobierno pueda invocar el artículo ciento sesenta y uno, dos"]),
  ll(63, ["dentro de los dos meses siguientes al día de la publicación o comunicación", "en el plazo máximo de un mes a partir de su recepción", "Dentro del mes siguiente a la notificación del rechazo"], solo=[2, 4, 5]),
  fichab("Procedimiento del conflicto positivo",
         "Gobierno (directamente o con requerimiento previo); Comunidad Autónoma (con requerimiento previo)",
         "El Gobierno puede formalizar el conflicto directamente o requerir antes; la Comunidad Autónoma requiere primero de incompetencia",
         ["Gobierno: **2 meses** para formalizarlo", "Requerimiento: **2 meses** desde la publicación o comunicación", "Respuesta del requerido: **1 mes**", "Planteamiento ante el Tribunal: **1 mes** desde el rechazo"],
         "Solo el **Gobierno** puede ir **directamente** al Tribunal y, además, invocar el art. 161.2 CE (suspensión)."))}
""", 2)

T.ap("s20", "IV.7 Conflictos entre órganos constitucionales y en defensa de la autonomía local (LOTC, arts. 73 y 75 bis a 75 quater)", f"""
{unidad("7.1 Conflicto entre órganos constitucionales (LOTC, art. 73)",
  ll(73, ["por acuerdo de sus respectivos Plenos", "dentro del mes siguiente", "dentro del plazo de un mes"], solo=[1, 3]),
  fichab("Conflicto de atribuciones", "Gobierno, Congreso, Senado y CGPJ, por acuerdo de sus **Plenos**",
         "Cuando un órgano estima que otro asume atribuciones que la Constitución o las leyes orgánicas le confieren: primero le pide que revoque la decisión y después plantea el conflicto",
         ["Notificación: **1 mes** desde que conoce la decisión", "Respuesta: **1 mes**", "Planteamiento: **1 mes** siguiente"],
         "Todo va por **meses**: uno, uno y uno. Lo acuerda el **Pleno** del órgano."))}

{unidad("7.2 Conflicto en defensa de la autonomía local (LOTC, arts. 75 bis, 75 ter y 75 quater)",
  ll(75, ["normas del Estado con rango de ley o las disposiciones con rango de ley de las Comunidades Autónomas"]),
  ll(751, ["destinatario único de la ley", "al menos un séptimo", "como mínimo un sexto de la población oficial", "al menos la mitad de las existentes", "mayoría absoluta del número legal de miembros", "con carácter preceptivo pero no vinculante"], solo=[1, 2, 3, 4, 5, 6]),
  ll(752, ["dentro de los tres meses siguientes al día de la publicación de la ley", "Dentro del mes siguiente a la recepción del dictamen"]),
  fichab("Defensa de la autonomía local frente a la ley",
         ["Municipio o provincia destinatario único de la ley", "Municipios: al menos **un séptimo** de los del ámbito y **un sexto** de la población", "Provincias: al menos **la mitad** de las del ámbito y **la mitad** de la población"],
         ["Objeto: normas con rango de ley que lesionen la autonomía local constitucionalmente garantizada", "Acuerdo del Pleno de la Corporación por **mayoría absoluta** del número legal", "Dictamen preceptivo, no vinculante, del Consejo de Estado o del órgano consultivo autonómico"],
         ["Solicitud del dictamen: **3 meses** desde la publicación de la ley", "Planteamiento: **1 mes** desde la recepción del dictamen"],
         "**Séptimo** de municipios y **sexto** de población; provincias, **mitad** y **mitad**. El dictamen es **preceptivo pero no vinculante**."))}
""", 2)

T.ap("s21", "IV.8 Impugnación de disposiciones y resoluciones autonómicas (art. 161.2 CE; LOTC, arts. 76 y 77)", f"""
{unidad("8.1 La regla constitucional (art. 161.2)",
  lit("CE", "Artículo 161", ["El Gobierno podrá impugnar", "La impugnación producirá la suspensión de la disposición o resolución recurrida", "en un plazo no superior a cinco meses"], solo=[6]),
  fichab("Impugnación con suspensión automática",
         f"{cc(161, 'El Gobierno')}",
         "Impugna disposiciones y resoluciones de los órganos de las Comunidades Autónomas; la impugnación las suspende",
         f"El Tribunal debe ratificar o levantar la suspensión {cc(161, 'en un plazo no superior a cinco meses')}",
         "**Cinco meses** (no tres ni uno). La suspensión es **automática**; solo la puede provocar el **Gobierno**. Cayó en 2025 (→ Cierre 1)."))}

{unidad("8.2 Plazo y procedimiento (LOTC, arts. 76 y 77)",
  ll(76, ["Dentro de los dos meses siguientes a la fecha de su publicación", "disposiciones normativas sin fuerza de Ley y resoluciones"]),
  ll(77, ["producirá la suspensión de la disposición o resolución recurrida", "en plazo no superior a cinco meses"]),
  fichab("Impugnación del Título V de la LOTC",
         "El Gobierno",
         "Contra disposiciones **sin fuerza de ley** y resoluciones autonómicas, por cualquier motivo; se tramita como el conflicto positivo (arts. 62 a 67)",
         ["Impugnación: **2 meses** desde la publicación o, en su defecto, desde que llegue a su conocimiento", "Suspensión: el Tribunal la ratifica o levanta en **5 meses** como máximo"],
         "Sirve aunque el motivo **no** sea competencial («sea cual fuere el motivo en que se base»)."))}
""", 2)

T.ap("s22", "IV.9 Tratados internacionales y recurso previo contra Estatutos (art. 95 CE; LOTC, arts. 78 y 79)", f"""
{unidad("9.1 Control previo de los tratados (art. 95)",
  lit("CE", "Artículo 95", ["exigirá la previa revisión constitucional", "El Gobierno o cualquiera de las Cámaras"]),
  fichab("Requerimiento sobre tratados", "El Gobierno o cualquiera de las Cámaras", "Piden al Tribunal que declare si el tratado contiene estipulaciones contrarias a la Constitución", "—",
         "Si las contiene, el tratado exige la **previa revisión constitucional**."))}

{unidad("9.2 La declaración sobre tratados (LOTC, art. 78)",
  ll(78, ["cuyo texto estuviera ya definitivamente fijado, pero al que no se hubiere prestado aún el consentimiento del Estado", "en el término de un mes", "tendrá carácter vinculante"], solo=[1, 2]),
  fichab("Procedimiento", "Requieren el Gobierno o cualquiera de ambas Cámaras; resuelve el **Pleno** (art. 10.1 a)",
         "Sobre un tratado de texto definitivamente fijado y aún sin consentimiento del Estado",
         "Opinión de los legitimados: **1 mes**; declaración: en el mes siguiente",
         "La declaración es **vinculante**. Es control **previo**: antes del consentimiento del Estado."))}

{unidad("9.3 Recurso previo contra Estatutos de Autonomía (LOTC, art. 79)",
  ll(79, ["con carácter previo", "una vez aprobado por las Cortes Generales", "tres días desde la publicación del texto aprobado", "suspenderá automáticamente todos los trámites subsiguientes", "en el plazo improrrogable de seis meses"], solo=[1, 2, 3, 4, 6]),
  fichab("Control previo de Estatutos",
         "Los legitimados para recurrir Estatutos de Autonomía (→ IV.2.3)",
         "Contra el texto definitivo del Proyecto o Propuesta de reforma de Estatuto aprobado por las Cortes Generales; suspende automáticamente los trámites siguientes",
         ["Interposición: **3 días** desde la publicación en el «Boletín Oficial de las Cortes Generales»", "Resolución: **6 meses** improrrogables"],
         "**Tres días** para recurrir y **seis meses** para resolver. Si el Estatuto va a referéndum, no se convoca hasta que resuelva el Tribunal."))}
""", 2)

T.ap("s23", "IV.10 Resoluciones y su cumplimiento (LOTC, arts. 86, 87, 92 y 93)", f"""
{unidad("10.1 Forma y publicación (LOTC, art. 86)",
  ll(86, ["en forma de sentencia", "dentro de los 30 días siguientes a la fecha del fallo"], solo=[1, 2]),
  fichab("Sentencias, autos y providencias", "El Tribunal",
         ["Decisión del proceso: sentencia", "Inadmisión inicial, desistimiento y caducidad: auto", "Otras: auto si son motivadas; providencia si no lo son"],
         "Publicación en el BOE en los **30 días** siguientes al fallo", "Sentencias y declaraciones sobre tratados: al BOE en **30 días**."))}

{unidad("10.2 Obligación de cumplimiento (LOTC, art. 87)",
  ll(87, ["Todos los poderes públicos están obligados al cumplimiento", "títulos ejecutivos"]),
  fichab("Fuerza de las resoluciones", "Todos los poderes públicos; los Juzgados y Tribunales prestan auxilio",
         "Las sentencias y resoluciones del Tribunal son títulos ejecutivos", "Auxilio jurisdiccional preferente y urgente", "Son **títulos ejecutivos**."))}

{unidad("10.3 Ejecución y medidas ante el incumplimiento (LOTC, art. 92.1 y 4)",
  ll(92, ["velará por el cumplimiento efectivo de sus resoluciones", "multa coercitiva de tres mil a treinta mil euros", "suspensión en sus funciones", "ejecución sustitutoria", "responsabilidad penal"], solo=[1, 5, 6, 7, 8, 9, 10]),
  fichab("Ejecución de las resoluciones", "El propio Tribunal, de oficio o a instancia de parte",
         ["Requiere a quien deba cumplir para que informe", "Si aprecia incumplimiento: multa coercitiva, suspensión en funciones, ejecución sustitutoria (con la colaboración del Gobierno) o testimonio para exigir responsabilidad penal"],
         "Multa coercitiva de **3.000 a 30.000 euros**, reiterable",
         "La multa es de **tres mil a treinta mil** euros y puede **reiterarse** hasta el cumplimiento íntegro."))}

{unidad("10.4 Recursos contra sus resoluciones (LOTC, art. 93)",
  ll(93, ["no cabe recurso alguno", "en el plazo de dos días", "recurso de súplica, que no tendrá efecto suspensivo"]),
  fichab("Impugnación de las resoluciones", "Las partes",
         ["Sentencias: ningún recurso; solo aclaración", "Providencias y autos: recurso de súplica, sin efecto suspensivo"],
         ["Aclaración: **2 días** desde la notificación", "Súplica: **3 días**; se resuelve en los **2** siguientes"],
         "Contra las **sentencias** no cabe recurso (también lo dice el art. 164 CE); la **súplica** es contra providencias y autos."))}
""", 2)

T.ap("s24", "IV.11 Cuadro de legitimación y plazos (esquema)", f"""
*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*

| Proceso | Quién lo plantea | Plazo | Artículos |
|---|---|---|---|
| Recurso de inconstitucionalidad | Presidente del Gobierno, Defensor del Pueblo, 50 Diputados, 50 Senadores; ejecutivos y Asambleas autonómicos (ámbito propio) | 3 meses desde la publicación (9 con Comisión Bilateral) | 162.1 a) CE; LOTC 32 y 33 |
| Cuestión de inconstitucionalidad | Juez o Tribunal | Concluso el procedimiento, en plazo para dictar sentencia | 163 CE; LOTC 35 |
| Amparo | Persona natural o jurídica con interés legítimo, Defensor del Pueblo, Ministerio Fiscal | 3 meses (Cortes), 20 días (Gobierno o Administración), 30 días (órgano judicial) | 162.1 b) CE; LOTC 42 a 46 |
| Conflicto positivo de competencia | Gobierno; ejecutivos autonómicos | Gobierno, 2 meses; requerimiento, 2 meses; respuesta, 1 mes; planteamiento, 1 mes | LOTC 60, 62 y 63 |
| Conflicto entre órganos constitucionales | Gobierno, Congreso, Senado, CGPJ (acuerdo del Pleno) | 1 mes + 1 mes + 1 mes | LOTC 59 y 73 |
| Conflicto en defensa de la autonomía local | Municipios y provincias (art. 75 ter) | Dictamen: 3 meses; conflicto: 1 mes | LOTC 75 ter y quater |
| Impugnación del art. 161.2 | Gobierno | 2 meses; suspensión hasta 5 meses | 161.2 CE; LOTC 76 y 77 |
| Requerimiento sobre tratados | Gobierno o cualquiera de las Cámaras | Antes del consentimiento del Estado | 95 CE; LOTC 78 |
| Recurso previo contra Estatutos | Los legitimados contra Estatutos | 3 días; resolución en 6 meses | LOTC 79 |

{resumen([
  "Atribuciones del art. 161 CE y del art. 2 LOTC: **inconstitucionalidad**, **amparo**, **conflictos** (competencia, órganos constitucionales, autonomía local), **161.2**, **tratados** y **recurso previo** contra Estatutos.",
  "Recurso de inconstitucionalidad: **50 Diputados o 50 Senadores**, Presidente del Gobierno, Defensor del Pueblo y, para su ámbito, las CC. AA.; **3 meses**; no suspende la ley salvo el **161.2**.",
  "Cuestión: el **juez**, concluso el procedimiento; amparo: **3 meses / 20 días / 30 días**, con **especial trascendencia constitucional**.",
  "Sentencias: cosa juzgada desde el **día siguiente** a su publicación, sin recurso y con **plenos efectos frente a todos** (164 CE)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX = [
 ("L", 3, "Quién propone a los Magistrados (→ II.1.1)", {
   "a": f"Literal del art. 159.1: {cc(159, 'cuatro a propuesta del Congreso por mayoría de tres quintos de sus miembros; cuatro a propuesta del Senado, con idéntica mayoría; dos a propuesta del Gobierno, y dos a propuesta del Consejo General del Poder Judicial')}.",
   "b": f"Cambia el reparto y deja fuera a dos proponentes: Congreso y Senado proponen **cuatro** cada uno, y además proponen el Gobierno y el CGPJ ({cc(159, 'dos a propuesta del Gobierno, y dos a propuesta del Consejo General del Poder Judicial')}).",
   "c": f"Cambia el número del Gobierno (son {cc(159, 'dos a propuesta del Gobierno')}) y omite al Consejo General del Poder Judicial.",
   "d": f"Cambia las cifras y un órgano: el Congreso propone cuatro, no seis, y el cuarto proponente es el **Consejo General del Poder Judicial**, no el Presidente del Tribunal Supremo ({cc(159, 'dos a propuesta del Consejo General del Poder Judicial')})."},
   [("4 el Congreso", "CE", "Artículo 159", "cuatro a propuesta del Congreso"), ("4 el Senado", "CE", "Artículo 159", "cuatro a propuesta del Senado"),
    ("2 el Gobierno", "CE", "Artículo 159", "dos a propuesta del Gobierno"), ("2 el Consejo General del Poder Judicial", "CE", "Artículo 159", "dos a propuesta del Consejo General del Poder Judicial")]),
 ("X", 7, "Legitimación para el recurso de inconstitucionalidad (→ IV.2.3)", {
   "a": f"Literal del art. 162.1 a): {cc(162, 'el Presidente del Gobierno, el Defensor del Pueblo, 50 Diputados, 50 Senadores, los órganos colegiados ejecutivos de las Comunidades Autónomas y, en su caso, las Asambleas de las mismas')}.",
   "b": f"Los ciudadanos no pueden interponer el recurso de inconstitucionalidad; lo que pueden interponer es el **amparo**: {cc(162, 'toda persona natural o jurídica que invoque un interés legítimo')} (art. 162.1 b).",
   "c": f"El juez no interpone un recurso: plantea la **cuestión** de inconstitucionalidad (art. 163: {c('CE', 'Artículo 163', 'Cuando un órgano judicial considere')}…).",
   "d": "Los partidos políticos no figuran entre los legitimados del art. 162.1 a)."},
   [("50 Diputados, 50 Senadores", "CE", "Artículo 162", "50 Diputados, 50 Senadores"), ("Presidente del Gobierno", "CE", "Artículo 162", "el Presidente del Gobierno")]),
 ("X", 8, "Impugnación del art. 161.2 (→ IV.8.1)", {
   "a": f"Cambia el plazo: tres meses es el plazo para interponer el recurso de inconstitucionalidad ({cl(33, 'dentro del plazo de tres meses a partir de la publicación')}), no el de la suspensión del art. 161.2.",
   "b": f"Literal del art. 161.2: {cc(161, 'La impugnación producirá la suspensión de la disposición o resolución recurrida, pero el Tribunal, en su caso, deberá ratificarla o levantarla en un plazo no superior a cinco meses')}.",
   "c": f"Invierte la regla: {cc(161, 'La impugnación producirá la suspensión de la disposición o resolución recurrida')}.",
   "d": f"Cambia el plazo: es {cc(161, 'en un plazo no superior a cinco meses')}, no un mes."},
   [("5 meses", "CE", "Artículo 161", "en un plazo no superior a cinco meses"), ("Produce la suspensión", "CE", "Artículo 161", "La impugnación producirá la suspensión de la disposición o resolución recurrida")]),
 ("X", 9, "Normas susceptibles de declaración de inconstitucionalidad (→ IV.2.1)", {
   "a": f"Sí es susceptible: art. 27.2 d), {cl(27, 'Los Reglamentos de las Cámaras y de las Cortes Generales')}.",
   "b": f"Sí es susceptible: art. 27.2 c), {cl(27, 'Los Tratados Internacionales')}.",
   "c": f"Sí es susceptible: art. 27.2 a), {cl(27, 'Los Estatutos de Autonomía y las demás Leyes orgánicas')}.",
   "d": f"No está en el art. 27.2 LOTC: la ordenanza fiscal es una norma **reglamentaria** local, no una norma con fuerza de ley ({c('LRBRL', 'a106', 'La potestad reglamentaria de las entidades locales en materia tributaria se ejercerá a través de Ordenanzas fiscales reguladoras de sus tributos propios')}: Ley 7/1985, art. 106.2). Su control corresponde a la jurisdicción contencioso-administrativa, que conoce {c('LJCA', 'Artículo 1', 'con las disposiciones generales de rango inferior a la Ley')} (LJCA, art. 1.1)."},
   [("Ordenanza fiscal", "LRBRL", "a106", "La potestad reglamentaria de las entidades locales en materia tributaria se ejercerá a través de Ordenanzas fiscales")]),
]
bloques = []
for cod, n, tit, por, ap_ in EX:
    bloques += [f"### {('GACE-L' if cod == 'L' else 'GACE-P' if cod == 'P' else 'GACE-L extraordinario')} 2025, pregunta {n} · {tit}", examen(cod, n, por, ap_)]
T.ap("s25", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join(
  ["En los primeros ejercicios de **2025** cayeron **cuatro** preguntas de este tema: una en el turno libre (composición) y tres en el extraordinario (legitimación, art. 161.2 y objeto del control). Están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal."]
  + bloques + ["### Cómo se pregunta", "!> Las preguntas citan el **artículo** (159, 161.2, 162 CE; 27 LOTC) y cambian **una cifra** (4/4/2/2; 50 Diputados; cinco meses), **un órgano** (CGPJ por Presidente del Tribunal Supremo; ciudadano o juez por los legitimados) o meten en la lista una norma **sin rango de ley** (una ordenanza)."]))

T.ap("s26", "Cierre 2. Repaso en 10 minutos (por bloques)", """
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Qué es | Título IX (159 a 165); ley orgánica (165); intérprete supremo, sometido solo a la CE y a la LOTC (LOTC 1) | **Intérprete supremo**; nadie le plantea cuestión de jurisdicción (LOTC 4) |
| II. Composición | 12 Magistrados nombrados por el Rey; 4 + 4 + 2 + 2; más de 15 años; 9 años; tercios cada 3 | **Tres quintos** en Congreso y Senado; Presidente: **3 años**, reelegible **una vez** |
| III. Organización | Pleno (12), dos Salas (6), Secciones (3); quórum de dos tercios | Presidente → Sala **Primera**; Vicepresidente → Sala **Segunda** |
| IV. Atribuciones | Inconstitucionalidad, amparo, conflictos, 161.2, tratados, recurso previo | **50** Diputados o Senadores; **3 meses**; suspensión del 161.2 hasta **5 meses** |

?> **Trampas frecuentes:** «el **Presidente del Tribunal Supremo** propone dos Magistrados» (es el **CGPJ**); «mandato de **doce** años» (son **nueve**); «más de **diez** años de ejercicio» (más de **quince**); «el Presidente lo nombra el Rey a propuesta del **Gobierno**» (a propuesta del **Tribunal en Pleno**); «cualquier ciudadano puede interponer el recurso de inconstitucionalidad» (solo el **amparo**); «la cuestión de inconstitucionalidad suspende la ley» (en ningún caso tiene efectos suspensivos sobre ella: se suspende el **proceso judicial**); «el 161.2 suspende hasta **tres** meses» (son **cinco**).
""")

# =============================================================================
Q = [
 ("CE", "Artículo 159", "Composición", "Según el artículo 159.1 de la Constitución, el Tribunal Constitucional se compone de:",
  ["12 miembros nombrados por el Rey.", "12 miembros nombrados por las Cortes Generales.", "15 miembros nombrados por el Rey.", "9 miembros nombrados por el Rey."], "Art. 159.1 CE.", "se compone de 12 miembros nombrados por el Rey"),
 ("CE", "Artículo 159", "Composición", "Según el artículo 159.1 de la Constitución, el Congreso propone cuatro miembros del Tribunal Constitucional por mayoría de:",
  ["Tres quintos de sus miembros.", "Dos tercios de sus miembros.", "Mayoría absoluta.", "Tres cuartos de sus miembros."], "Art. 159.1 CE.", "cuatro a propuesta del Congreso por mayoría de tres quintos de sus miembros"),
 ("CE", "Artículo 159", "Composición", "Según el artículo 159.1 de la Constitución, dos miembros del Tribunal Constitucional se nombran a propuesta de:",
  ["El Consejo General del Poder Judicial.", "El Presidente del Tribunal Supremo.", "El Defensor del Pueblo.", "El Ministerio Fiscal."], "Art. 159.1 CE.", "dos a propuesta del Consejo General del Poder Judicial"),
 ("CE", "Artículo 159", "Requisitos y mandato", "Según el artículo 159.2 de la Constitución, los miembros del Tribunal Constitucional deberán ser juristas de reconocida competencia con:",
  ["Más de quince años de ejercicio profesional.", "Más de diez años de ejercicio profesional.", "Más de veinte años de ejercicio profesional.", "Más de doce años de ejercicio profesional."], "Art. 159.2 CE.", "con más de quince años de ejercicio profesional"),
 ("CE", "Artículo 159", "Requisitos y mandato", "Según el artículo 159.3 de la Constitución, los miembros del Tribunal Constitucional serán designados por un período de:",
  ["Nueve años, y se renovarán por terceras partes cada tres.", "Doce años, y se renovarán por mitades cada seis.", "Nueve años, y se renovarán por mitades cada cuatro años y medio.", "Seis años, y se renovarán por terceras partes cada dos."], "Art. 159.3 CE.", "por un período de nueve años y se renovarán por terceras partes cada tres"),
 ("CE", "Artículo 159", "Incompatibilidades", "Según el artículo 159.4 de la Constitución, en lo no previsto expresamente, los miembros del Tribunal Constitucional tendrán las incompatibilidades propias de:",
  ["Los miembros del poder judicial.", "Los Diputados y Senadores.", "Los miembros del Gobierno.", "Los funcionarios de la Administración General del Estado."], "Art. 159.4 CE.", "tendrán las incompatibilidades propias de los miembros del poder judicial"),
 ("CE", "Artículo 159", "Incompatibilidades", "Según el artículo 159.5 de la Constitución, los miembros del Tribunal Constitucional serán en el ejercicio de su mandato:",
  ["Independientes e inamovibles.", "Independientes y responsables ante las Cortes.", "Inamovibles y reelegibles.", "Independientes y revocables por el Pleno del Congreso."], "Art. 159.5 CE.", "serán independientes e inamovibles en el ejercicio de su mandato"),
 ("CE", "Artículo 160", "Presidente", "Según el artículo 160 de la Constitución, el Presidente del Tribunal Constitucional será nombrado entre sus miembros por el Rey:",
  ["A propuesta del mismo Tribunal en pleno y por un período de tres años.", "A propuesta del Gobierno y por un período de tres años.", "A propuesta del Tribunal en pleno y por un período de nueve años.", "A propuesta del Congreso y por un período de cuatro años."], "Art. 160 CE.", "a propuesta del mismo Tribunal en pleno y por un período de tres años"),
 ("LOTC", A[9], "Presidente", "Según el artículo 9 de la LOTC, expirado el período de tres años, el Presidente del Tribunal Constitucional:",
  ["Podrá ser reelegido por una sola vez.", "No podrá ser reelegido.", "Podrá ser reelegido indefinidamente.", "Podrá ser reelegido dos veces."], "Art. 9.3 LOTC.", "podrá ser reelegido por una sola vez"),
 ("LOTC", A[9], "Presidente", "Según el artículo 9 de la LOTC, en la primera votación para elegir al Presidente del Tribunal Constitucional se requerirá:",
  ["La mayoría absoluta.", "La mayoría de tres quintos.", "La mayoría simple.", "La unanimidad."], "Art. 9.2 LOTC.", "En primera votación se requerirá la mayoría absoluta"),
 ("LOTC", A[1], "Naturaleza", "Según el artículo 1 de la LOTC, el Tribunal Constitucional, como intérprete supremo de la Constitución, está sometido:",
  ["Sólo a la Constitución y a la Ley Orgánica del Tribunal Constitucional.", "A la Constitución y al resto del ordenamiento jurídico.", "A la Constitución y a las leyes aprobadas por las Cortes Generales.", "Sólo a la Constitución y a los tratados internacionales."], "Art. 1.1 LOTC.", "está sometido sólo a la Constitución y a la presente Ley Orgánica"),
 ("CE", "Artículo 165", "Naturaleza", "Según el artículo 165 de la Constitución, el funcionamiento del Tribunal Constitucional, el estatuto de sus miembros y el procedimiento ante el mismo los regulará:",
  ["Una ley orgánica.", "Un reglamento aprobado por el Tribunal en Pleno.", "Una ley ordinaria.", "Un real decreto del Gobierno."], "Art. 165 CE.", "Una ley orgánica regulará el funcionamiento del Tribunal Constitucional"),
 ("LOTC", A[4], "Naturaleza", "Según el artículo 4 de la LOTC, las resoluciones del Tribunal Constitucional:",
  ["No podrán ser enjuiciadas por ningún órgano jurisdiccional del Estado.", "Podrán ser revisadas por el Tribunal Supremo en casación.", "Podrán ser enjuiciadas por el Consejo General del Poder Judicial.", "Podrán recurrirse ante la Sala Especial de Conflictos de Jurisdicción."], "Art. 4.2 LOTC.", "no podrán ser enjuiciadas por ningún órgano jurisdiccional del Estado"),
 ("LOTC", A[16], "Composición", "Según el artículo 16.1 de la LOTC, los Magistrados propuestos por el Senado serán elegidos entre las candidaturas presentadas por:",
  ["Las Asambleas Legislativas de las comunidades autónomas.", "Los grupos parlamentarios del Senado.", "El Consejo General del Poder Judicial.", "Los Gobiernos de las comunidades autónomas."], "Art. 16.1 LOTC.", "entre las candidaturas presentadas por las Asambleas Legislativas de las comunidades autónomas"),
 ("LOTC", A[16], "Requisitos y mandato", "Según el artículo 16.4 de la LOTC, ningún Magistrado podrá ser propuesto al Rey para otro período inmediato, salvo que hubiera ocupado el cargo por un plazo no superior a:",
  ["Tres años.", "Seis años.", "Cuatro años.", "Un año."], "Art. 16.4 LOTC.", "salvo que hubiera ocupado el cargo por un plazo no superior a tres años"),
 ("LOTC", A[17], "Requisitos y mandato", "Según el artículo 17.1 de la LOTC, el Presidente del Tribunal solicitará a los órganos proponentes que inicien el procedimiento para designar a los nuevos Magistrados:",
  ["Antes de los cuatro meses previos a la fecha de expiración de los nombramientos.", "Antes de los seis meses previos a la fecha de expiración de los nombramientos.", "Dentro del mes siguiente a la expiración de los nombramientos.", "Antes de los dos meses previos a la fecha de expiración de los nombramientos."], "Art. 17.1 LOTC.", "Antes de los cuatro meses previos a la fecha de expiración de los nombramientos"),
 ("LOTC", A[19], "Incompatibilidades", "Según el artículo 19.2 de la LOTC, si quien fuere propuesto como Magistrado incurso en causa de incompatibilidad no cesa en el cargo o actividad incompatible, se entenderá que no acepta el cargo transcurrido el plazo de:",
  ["Diez días siguientes a la propuesta.", "Quince días siguientes a la propuesta.", "Un mes siguiente al nombramiento.", "Diez días siguientes a la toma de posesión."], "Art. 19.2 LOTC.", "en el plazo de diez días siguientes a la propuesta"),
 ("LOTC", A[20], "Incompatibilidades", "Según el artículo 20 de la LOTC, los funcionarios públicos nombrados Magistrados del Tribunal Constitucional pasarán, en su carrera de origen, a la situación de:",
  ["Servicios especiales.", "Excedencia voluntaria.", "Servicio en otras Administraciones Públicas.", "Suspensión de funciones."], "Art. 20 LOTC.", "pasarán a la situación de servicios especiales en su carrera de origen"),
 ("LOTC", A[23], "Estatuto", "Según el artículo 23.2 de la LOTC, el cese de un Magistrado por dejar de atender con diligencia los deberes de su cargo lo decide el Tribunal en Pleno por mayoría de:",
  ["Las tres cuartas partes de sus miembros.", "Mayoría simple.", "Dos tercios de sus miembros.", "Mayoría absoluta."], "Art. 23.2 LOTC: mayoría simple solo en los casos tercero y cuarto (incapacidad e incompatibilidad sobrevenida).", "por mayoría de las tres cuartas partes de sus miembros en los demás casos"),
 ("LOTC", A[26], "Estatuto", "Según el artículo 26 de la LOTC, la responsabilidad criminal de los Magistrados del Tribunal Constitucional sólo será exigible ante:",
  ["La Sala de lo Penal del Tribunal Supremo.", "El propio Tribunal Constitucional en Pleno.", "La Sala de lo Penal de la Audiencia Nacional.", "El Tribunal Superior de Justicia de Madrid."], "Art. 26 LOTC.", "sólo será exigible ante la Sala de lo Penal del Tribunal Supremo"),
 ("LOTC", A[7], "Organización", "Según el artículo 7 de la LOTC, el Tribunal Constitucional consta de:",
  ["Dos Salas, compuestas cada una por seis Magistrados nombrados por el Tribunal en Pleno.", "Tres Salas, compuestas cada una por cuatro Magistrados.", "Dos Salas, compuestas cada una por seis Magistrados nombrados por el Presidente.", "Cuatro Secciones de tres Magistrados nombrados por el Rey."], "Art. 7.1 LOTC.", "consta de dos Salas. Cada Sala está compuesta por seis Magistrados nombrados por el Tribunal en Pleno"),
 ("LOTC", A[7], "Organización", "Según el artículo 7 de la LOTC, la Sala Segunda del Tribunal Constitucional la preside:",
  ["El Vicepresidente del Tribunal.", "El Presidente del Tribunal.", "El Magistrado de mayor edad.", "El Magistrado más moderno."], "Art. 7.3 LOTC.", "El Vicepresidente del Tribunal presidirá en la Sala Segunda"),
 ("LOTC", A[14], "Organización", "Según el artículo 14 de la LOTC, el Tribunal en Pleno puede adoptar acuerdos cuando estén presentes, al menos:",
  ["Dos tercios de los miembros que en cada momento lo compongan.", "La mitad más uno de sus miembros.", "Tres cuartos de los miembros que en cada momento lo compongan.", "Diez Magistrados."], "Art. 14 LOTC.", "cuando estén presentes, al menos, dos tercios de los miembros que en cada momento lo compongan"),
 ("LOTC", A[90], "Organización", "Según el artículo 90.1 de la LOTC, en caso de empate en las decisiones del Tribunal Constitucional:",
  ["Decidirá el voto del Presidente.", "Se repetirá la votación hasta que haya mayoría.", "Decidirá el voto del Magistrado más antiguo.", "Se entenderá desestimada la pretensión."], "Art. 90.1 LOTC.", "En caso de empate, decidirá el voto del Presidente"),
 ("LOTC", A[13], "Organización", "Según el artículo 13 de la LOTC, cuando una Sala considere necesario apartarse en cualquier punto de la doctrina constitucional precedente sentada por el Tribunal:",
  ["La cuestión se someterá a la decisión del Pleno.", "Podrá hacerlo motivándolo expresamente.", "Deberá consultar a la otra Sala.", "La cuestión se someterá a la decisión del Presidente."], "Art. 13 LOTC.", "la cuestión se someterá a la decisión del Pleno"),
 ("CE", "Artículo 161", "Atribuciones", "Según el artículo 161.1 de la Constitución, el Tribunal Constitucional es competente para conocer de los conflictos de competencia:",
  ["Entre el Estado y las Comunidades Autónomas o de los de éstas entre sí.", "Entre los Juzgados y Tribunales y la Administración.", "Entre los órganos jurisdiccionales de distinto orden.", "Entre las Corporaciones locales de una misma provincia."], "Art. 161.1 c) CE.", "De los conflictos de competencia entre el Estado y las Comunidades Autónomas o de los de éstas entre sí"),
 ("LOTC", A[27], "Recurso de inconstitucionalidad", "Según el artículo 27.2 de la LOTC, ¿cuál de las siguientes normas es susceptible de declaración de inconstitucionalidad?",
  ["Los Reglamentos de las Asambleas legislativas de las Comunidades Autónomas.", "Los Reales Decretos aprobados por el Consejo de Ministros.", "Las Órdenes ministeriales.", "Las ordenanzas municipales."], "Art. 27.2 f) LOTC; las demás son normas reglamentarias.", "Los Reglamentos de las Asambleas legislativas de las Comunidades Autónomas"),
 ("CE", "Artículo 162", "Recurso de inconstitucionalidad", "Según el artículo 162.1 a) de la Constitución, está legitimado para interponer el recurso de inconstitucionalidad:",
  ["El Defensor del Pueblo.", "El Ministerio Fiscal.", "El Consejo General del Poder Judicial.", "Toda persona natural o jurídica que invoque un interés legítimo."], "Art. 162.1 a) CE. El Ministerio Fiscal y las personas con interés legítimo lo están para el amparo (162.1 b).", "el Presidente del Gobierno, el Defensor del Pueblo, 50 Diputados"),
 ("LOTC", A[33], "Recurso de inconstitucionalidad", "Según el artículo 33.1 de la LOTC, el recurso de inconstitucionalidad se formulará dentro del plazo de:",
  ["Tres meses a partir de la publicación de la Ley, disposición o acto con fuerza de Ley impugnado.", "Dos meses a partir de la publicación de la Ley impugnada.", "Tres meses a partir de la entrada en vigor de la Ley impugnada.", "Nueve meses a partir de la publicación de la Ley impugnada, en todo caso."], "Art. 33.1 LOTC (nueve meses solo con el procedimiento del 33.2).", "dentro del plazo de tres meses a partir de la publicación de la Ley, disposición o acto con fuerza de Ley impugnado"),
 ("LOTC", A[30], "Recurso de inconstitucionalidad", "Según el artículo 30 de la LOTC, la admisión de un recurso o de una cuestión de inconstitucionalidad:",
  ["No suspenderá la vigencia ni la aplicación de la Ley, salvo que el Gobierno se ampare en el artículo 161.2 de la Constitución para impugnar leyes de las Comunidades Autónomas.", "Suspenderá en todo caso la vigencia de la Ley.", "Suspenderá la aplicación de la Ley durante cinco meses.", "No suspenderá la vigencia de la Ley en ningún caso."], "Art. 30 LOTC.", "no suspenderá la vigencia ni la aplicación de la Ley"),
 ("LOTC", A[35], "Cuestión de inconstitucionalidad", "Según el artículo 35.2 de la LOTC, el órgano judicial sólo podrá plantear la cuestión de inconstitucionalidad:",
  ["Una vez concluso el procedimiento y dentro del plazo para dictar sentencia.", "Al inicio del procedimiento, antes de la práctica de la prueba.", "Una vez dictada sentencia firme.", "En cualquier momento del procedimiento, a instancia del Ministerio Fiscal."], "Art. 35.2 LOTC.", "una vez concluso el procedimiento y dentro del plazo para dictar sentencia"),
 ("CE", "Artículo 163", "Cuestión de inconstitucionalidad", "Según el artículo 163 de la Constitución, los efectos de la cuestión de inconstitucionalidad que establezca la ley:",
  ["En ningún caso serán suspensivos.", "Serán siempre suspensivos.", "Serán suspensivos si lo acuerda el Tribunal Constitucional.", "Serán suspensivos durante un plazo máximo de cinco meses."], "Art. 163 CE.", "que en ningún caso serán suspensivos"),
 ("CE", "Artículo 164", "Sentencias", "Según el artículo 164.1 de la Constitución, las sentencias del Tribunal Constitucional tienen el valor de cosa juzgada:",
  ["A partir del día siguiente de su publicación.", "Desde la fecha en que se dictan.", "A partir de los veinte días de su publicación.", "Desde su notificación a las partes."], "Art. 164.1 CE.", "Tienen el valor de cosa juzgada a partir del día siguiente de su publicación"),
 ("LOTC", A[40], "Sentencias", "Según el artículo 40.1 de la LOTC, las sentencias declaratorias de la inconstitucionalidad de leyes permiten revisar procesos fenecidos mediante sentencia con fuerza de cosa juzgada:",
  ["Solo en procesos penales o contencioso-administrativos sancionadores en que resulte una reducción de la pena o de la sanción o una exclusión, exención o limitación de la responsabilidad.", "En todo caso.", "Solo en procesos civiles.", "Solo si lo solicita el Ministerio Fiscal en el plazo de un mes."], "Art. 40.1 LOTC.", "salvo en el caso de los procesos penales o contencioso-administrativos referentes a un procedimiento sancionador"),
 ("CE", "Artículo 162", "Amparo", "Según el artículo 162.1 b) de la Constitución, está legitimado para interponer el recurso de amparo, además de toda persona natural o jurídica que invoque un interés legítimo:",
  ["El Defensor del Pueblo y el Ministerio Fiscal.", "50 Diputados y 50 Senadores.", "El Presidente del Gobierno.", "Los órganos colegiados ejecutivos de las Comunidades Autónomas."], "Art. 162.1 b) CE.", "así como el Defensor del Pueblo y el Ministerio Fiscal"),
 ("LOTC", A[44], "Amparo", "Según el artículo 44.2 de la LOTC, el plazo para interponer el recurso de amparo contra violaciones originadas por un órgano judicial será de:",
  ["30 días, a partir de la notificación de la resolución recaída en el proceso judicial.", "20 días, a partir de la notificación de la resolución recaída en el proceso judicial.", "Tres meses desde que la resolución sea firme.", "Dos meses desde la notificación."], "Art. 44.2 LOTC (20 días es el del art. 43.2; tres meses, el del art. 42).", "será de 30 días, a partir de la notificación de la resolución recaída en el proceso judicial"),
 ("LOTC", A[50], "Amparo", "Según el artículo 50.1 de la LOTC, la Sección acordará la admisión del recurso de amparo:",
  ["Por unanimidad de sus miembros, cuando el recurso justifique una decisión sobre el fondo en razón de su especial trascendencia constitucional.", "Por mayoría de sus miembros, cuando el recurso no carezca manifiestamente de contenido.", "Por unanimidad, en todo caso, si la demanda cumple los requisitos formales.", "Por mayoría absoluta, previa audiencia del Ministerio Fiscal."], "Art. 50.1 LOTC.", "La Sección, por unanimidad de sus miembros, acordará mediante providencia la admisión"),
 ("LOTC", A[59], "Conflictos", "Según el artículo 59.1 c) de la LOTC, los conflictos entre órganos constitucionales pueden oponer al Gobierno con:",
  ["El Congreso de los Diputados, el Senado o el Consejo General del Poder Judicial.", "El Tribunal Supremo o la Audiencia Nacional.", "El Defensor del Pueblo o el Tribunal de Cuentas.", "Las Comunidades Autónomas."], "Art. 59.1 c) LOTC.", "Al Gobierno con el Congreso de los Diputados, el Senado o el Consejo General del Poder Judicial"),
 ("LOTC", A[62], "Conflictos", "Según el artículo 62 de la LOTC, el Gobierno podrá formalizar directamente ante el Tribunal Constitucional el conflicto de competencia en el plazo de:",
  ["Dos meses.", "Un mes.", "Tres meses.", "Veinte días."], "Art. 62 LOTC.", "en el plazo de dos meses, el conflicto de competencia"),
 ("LOTC", A[751], "Conflictos", "Según el artículo 75 ter de la LOTC, para plantear un conflicto en defensa de la autonomía local están legitimados un número de municipios que supongan al menos:",
  ["Un séptimo de los existentes en el ámbito territorial de aplicación y representen como mínimo un sexto de la población oficial.", "La mitad de los existentes y la mitad de la población oficial.", "Un sexto de los existentes y un séptimo de la población oficial.", "Un tercio de los existentes y un cuarto de la población oficial."], "Art. 75 ter.1 b) LOTC (la mitad y la mitad es para las provincias).", "al menos un séptimo de los existentes en el ámbito territorial de aplicación de la disposición con rango de ley, y representen como mínimo un sexto de la población oficial"),
 ("LOTC", A[76], "Art. 161.2", "Según el artículo 76 de la LOTC, el Gobierno podrá impugnar ante el Tribunal Constitucional las disposiciones normativas sin fuerza de Ley y resoluciones de las Comunidades Autónomas dentro de:",
  ["Los dos meses siguientes a la fecha de su publicación o, en defecto de la misma, desde que llegare a su conocimiento.", "Los tres meses siguientes a la fecha de su publicación.", "El mes siguiente a la fecha de su publicación.", "Los cinco meses siguientes a su entrada en vigor."], "Art. 76 LOTC.", "Dentro de los dos meses siguientes a la fecha de su publicación"),
 ("LOTC", A[78], "Tratados y recurso previo", "Según el artículo 78.2 de la LOTC, la declaración del Tribunal Constitucional sobre la contradicción entre la Constitución y un tratado internacional:",
  ["Tendrá carácter vinculante.", "Tendrá carácter consultivo.", "Requerirá la ratificación del Congreso.", "Solo vinculará al Gobierno."], "Art. 78.2 LOTC.", "tendrá carácter vinculante"),
 ("LOTC", A[79], "Tratados y recurso previo", "Según el artículo 79.4 de la LOTC, el plazo para interponer el recurso previo de inconstitucionalidad contra Proyectos de Estatutos de Autonomía será de:",
  ["Tres días desde la publicación del texto aprobado en el Boletín Oficial de las Cortes Generales.", "Tres meses desde la publicación del texto aprobado.", "Un mes desde la aprobación por las Cortes Generales.", "Quince días desde la publicación en el Boletín Oficial del Estado."], "Art. 79.4 LOTC.", "será de tres días desde la publicación del texto aprobado"),
 ("LOTC", A[92], "Cumplimiento", "Según el artículo 92.4 de la LOTC, si el Tribunal aprecia el incumplimiento de sus resoluciones, podrá imponer a quienes las incumplan una multa coercitiva de:",
  ["Tres mil a treinta mil euros.", "Seiscientos a seis mil euros.", "Mil a diez mil euros.", "Treinta mil a trescientos mil euros."], "Art. 92.4 a) LOTC.", "multa coercitiva de tres mil a treinta mil euros"),
 ("LOTC", A[93], "Cumplimiento", "Según el artículo 93 de la LOTC, contra las sentencias del Tribunal Constitucional:",
  ["No cabe recurso alguno, pero las partes podrán solicitar su aclaración en el plazo de dos días.", "Cabe recurso de súplica en el plazo de tres días.", "Cabe recurso ante el Tribunal Europeo de Derechos Humanos como segunda instancia interna.", "Cabe recurso de revisión ante el Pleno en el plazo de un mes."], "Art. 93.1 LOTC.", "Contra las sentencias del Tribunal Constitucional no cabe recurso alguno"),
]
for k, art, cat, enun, ops, exp, fr in Q: T.q(k, art, cat, enun, ops, exp, fr)
for cod, n, cat in [("L", 3, "Composición"), ("X", 7, "Recurso de inconstitucionalidad"), ("X", 8, "Art. 161.2"), ("X", 9, "Recurso de inconstitucionalidad")]:
    T.real(cod, n, cat)

# Flashcards
for q_, a_, cat in [
  ("¿Dónde regula la Constitución el Tribunal Constitucional?", "Título IX, arts. 159 a 165; el art. 165 remite a una ley orgánica (LOTC).", "Naturaleza"),
  ("Naturaleza del Tribunal (LOTC, art. 1)", "Intérprete supremo de la Constitución; independiente; sometido sólo a la Constitución y a la LOTC; único en su orden.", "Naturaleza"),
  ("Composición (art. 159.1 CE)", "12 miembros nombrados por el Rey: 4 Congreso y 4 Senado (tres quintos), 2 Gobierno y 2 CGPJ.", "Composición"),
  ("¿De dónde salen los candidatos que propone el Senado? (LOTC, art. 16.1)", "De las candidaturas de las Asambleas Legislativas de las comunidades autónomas.", "Composición"),
  ("Requisitos (art. 159.2 CE; LOTC, art. 18)", "Españoles; Magistrados y Fiscales, Profesores de Universidad, funcionarios públicos y Abogados; juristas de reconocida competencia con más de 15 años de ejercicio.", "Requisitos y mandato"),
  ("Mandato y renovación (art. 159.3)", "Nueve años; renovación por terceras partes cada tres.", "Requisitos y mandato"),
  ("¿Puede reelegirse un Magistrado para el período inmediato? (LOTC, art. 16.4)", "No, salvo que hubiera ocupado el cargo tres años o menos.", "Requisitos y mandato"),
  ("Incompatibilidades del art. 159.4 CE", "Mandato representativo; cargos políticos o administrativos; funciones directivas o empleo en partidos o sindicatos; carreras judicial y fiscal; actividad profesional o mercantil.", "Incompatibilidades"),
  ("Plazo para cesar en la actividad incompatible (LOTC, art. 19.2)", "Diez días siguientes a la propuesta; si no, se entiende que no acepta.", "Incompatibilidades"),
  ("Presidente del TC (art. 160 CE; LOTC, art. 9)", "Lo propone el Tribunal en Pleno (votación secreta) y lo nombra el Rey; tres años; reelegible una sola vez.", "Presidente"),
  ("¿Quién preside cada Sala? (LOTC, art. 7)", "Sala Primera: el Presidente del Tribunal; Sala Segunda: el Vicepresidente.", "Organización"),
  ("Composición de las Secciones (LOTC, art. 8)", "El Presidente respectivo (o quien le sustituya) y dos Magistrados.", "Organización"),
  ("Quórum del Pleno y de las Salas (LOTC, art. 14)", "Dos tercios de los miembros que en cada momento los compongan.", "Organización"),
  ("Cese por causas disciplinarias y suspensión (LOTC, arts. 23 y 24)", "Pleno, por tres cuartas partes de sus miembros.", "Estatuto"),
  ("Atribuciones del art. 161 CE", "Recurso de inconstitucionalidad; amparo; conflictos de competencia Estado-CC. AA. o entre CC. AA.; demás que atribuyan la CE o las leyes orgánicas; impugnación del 161.2.", "Atribuciones"),
  ("Legitimados para el recurso de inconstitucionalidad (art. 162.1 a)", "Presidente del Gobierno, Defensor del Pueblo, 50 Diputados, 50 Senadores, órganos colegiados ejecutivos de las CC. AA. y, en su caso, sus Asambleas.", "Recurso de inconstitucionalidad"),
  ("Plazo del recurso de inconstitucionalidad (LOTC, art. 33)", "Tres meses desde la publicación; nueve meses (Presidente del Gobierno y ejecutivos autonómicos) con acuerdo de la Comisión Bilateral.", "Recurso de inconstitucionalidad"),
  ("¿Cuándo plantea el juez la cuestión de inconstitucionalidad? (LOTC, art. 35.2)", "Concluso el procedimiento y dentro del plazo para dictar sentencia, tras oír 10 días a las partes y al Fiscal.", "Cuestión de inconstitucionalidad"),
  ("Valor de las sentencias del TC (art. 164.1 CE)", "Cosa juzgada desde el día siguiente a su publicación en el BOE; sin recurso; plenos efectos frente a todos las de inconstitucionalidad.", "Sentencias"),
  ("Plazos del amparo (LOTC, arts. 42, 43 y 44)", "Actos parlamentarios: 3 meses; Gobierno o Administración: 20 días; órganos judiciales: 30 días.", "Amparo"),
  ("Impugnación del art. 161.2 CE", "El Gobierno impugna disposiciones y resoluciones autonómicas (2 meses, LOTC 76); suspensión automática que el TC ratifica o levanta en no más de 5 meses.", "Art. 161.2"),
  ("Recurso previo contra Estatutos (LOTC, art. 79)", "3 días desde la publicación en el BOCG; suspende los trámites; se resuelve en 6 meses improrrogables.", "Tratados y recurso previo"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Intérprete supremo de la Constitución", "Calificación del Tribunal Constitucional en el art. 1 LOTC: independiente de los demás órganos constitucionales y sometido sólo a la Constitución y a su Ley Orgánica.", "s2", "Naturaleza")
T.glos("Renovación por tercios", "Cada tres años se renueva un tercio del Tribunal; el mandato es de nueve años (art. 159.3 CE; LOTC, art. 16.3).", "s6", "Composición")
T.glos("Inamovilidad", "Garantía de los Magistrados: no pueden ser destituidos ni suspendidos sino por las causas de la LOTC (art. 159.5 CE; LOTC, art. 22).", "s7", "Composición")
T.glos("Pleno", "Formación integrada por todos los Magistrados; conoce de los asuntos del art. 10 LOTC y decide los cambios de doctrina (art. 13).", "s11", "Organización")
T.glos("Sala", "Cada una de las dos formaciones de seis Magistrados; conocen de lo que no es del Pleno, como el amparo (LOTC, arts. 7 y 11).", "s10", "Organización")
T.glos("Sección", "Formación de tres (el Presidente respectivo y dos Magistrados) para el despacho ordinario y la admisión (LOTC, art. 8).", "s10", "Organización")
T.glos("Voto particular", "Opinión discrepante de un Magistrado defendida en la deliberación; se publica con la resolución (LOTC, art. 90.2; art. 164.1 CE).", "s12", "Organización")
T.glos("Recurso de inconstitucionalidad", "Impugnación directa de leyes y normas con fuerza de ley por los legitimados del art. 162.1 a) CE, en tres meses desde su publicación (LOTC, arts. 31 a 34).", "s15", "Atribuciones")
T.glos("Cuestión de inconstitucionalidad", "La que plantea un órgano judicial sobre una norma con rango de ley aplicable al caso y de cuya validez dependa el fallo (art. 163 CE; LOTC, art. 35).", "s16", "Atribuciones")
T.glos("Especial trascendencia constitucional", "Requisito de admisión del amparo: importancia del recurso para la interpretación, aplicación o eficacia de la Constitución y para los derechos fundamentales (LOTC, art. 50.1 b).", "s18", "Atribuciones")
T.glos("Conflicto negativo de competencia", "El que surge cuando una Administración declina su competencia; pueden instarlo también las personas físicas o jurídicas interesadas (LOTC, arts. 60 y 68).", "s19", "Atribuciones")
T.glos("Conflicto en defensa de la autonomía local", "El que plantean municipios y provincias contra normas con rango de ley que lesionen la autonomía local constitucionalmente garantizada (LOTC, arts. 75 bis a 75 quinquies).", "s20", "Atribuciones")
T.glos("Recurso previo de inconstitucionalidad", "Control previo de los Proyectos y Propuestas de reforma de Estatutos de Autonomía aprobados por las Cortes Generales (LOTC, art. 79).", "s22", "Atribuciones")

# Cronología (fechas de los metadatos del BOE)
T.hito("1978", "Constitución Española (27-12-1978; BOE de 29-12-1978)", "Título IX (arts. 159 a 165): el Tribunal Constitucional", "normativo", "s4")
T.hito("1979", "Ley Orgánica 2/1979, de 3 de octubre, del Tribunal Constitucional (BOE de 5-10-1979)", "Organización, Magistrados y procesos constitucionales", "normativo", "s2")
T.hito("1999", "Ley Orgánica 7/1999, de 21 de abril (BOE de 22-4-1999)", "Añade a la LOTC los conflictos en defensa de la autonomía local (arts. 2.1 d bis y 75 bis y siguientes)", "normativo", "s20")
T.hito("2007", "Ley Orgánica 6/2007, de 24 de mayo (BOE de 25-5-2007)", "Da la redacción vigente, entre otros, del art. 50 LOTC (admisión del amparo)", "normativo", "s18")
T.hito("2015", "Ley Orgánica 12/2015, de 22 de septiembre (BOE de 23-9-2015)", "Añade el control previo de inconstitucionalidad (art. 2.1 e bis) y da la redacción vigente del art. 79 LOTC", "normativo", "s22")
T.hito("2015", "Ley Orgánica 15/2015, de 16 de octubre (BOE de 17-10-2015)", "Da la redacción vigente del art. 92 LOTC (ejecución de las resoluciones)", "normativo", "s23")
T.hito("2024", "Ley Orgánica 2/2024, de 1 de agosto, de representación paritaria y presencia equilibrada de mujeres y hombres (BOE de 2-8-2024)", "Da la redacción vigente del art. 16 LOTC (propuestas con presencia equilibrada de mujeres y hombres)", "normativo", "s4")

T.publicar()
