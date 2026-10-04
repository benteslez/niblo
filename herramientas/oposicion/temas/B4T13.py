# -*- coding: utf-8 -*-
"""Tema IV.13 (B4T13): La jurisdicción contencioso-administrativa: funciones, órganos y
competencias. El recurso contencioso-administrativo. Actividad administrativa impugnable.
Las partes: capacidad, legitimación, representación y defensa.
Método del I.2. Normas (textos consolidados del BOE): CE, arts. 106.1 y 153; Ley 29/1998
(LJCA); LOPJ, art. 9; LO 1/2025 (disposición adicional primera y transitoria primera:
Tribunales de Instancia). Doctrina: STC 52/2014 (resumen oficial del buscador del TC)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO["LO1_2025"] = "LO 1/2025"
STC52 = "https://hj.tribunalconstitucional.es/es-ES/Resolucion/Show/23903"


def tc_doc(k, url, cab, frases, resaltar=()):
    """Bloque literal de una resolución del TC (no es texto legal): cada frase tiene que ser
    un párrafo (o parte de un párrafo) del texto guardado en boe/<k>.json, descargado del
    buscador oficial hj.tribunalconstitucional.es. Comparación exacta (distingue mayúsculas)."""
    ps = [" ".join(x.split()) for x in boe.parrafos(k, "Texto")]
    out = []
    for f in frases:
        assert any(" ".join(f.split()) in x for x in ps), ("TC NO LITERAL", k, f)
        for r in resaltar:
            if r in f: f = f.replace(r, "**" + r + "**", 1)
        out.append(f)
    for r in resaltar: assert any(r in f for f in frases), ("NEGRITA NO LITERAL", k, r)
    return "\n".join([f"> [[TC|{url}]]", "> **" + cab + "**"] + ["> " + x for x in out])

T = Tema("B4T13",
  "Cuatro preguntas: I. Para qué sirve la jurisdicción contencioso-administrativa (arts. 106.1 y 153 CE; LJCA, arts. 1 a 5) · II. Qué órganos la forman y qué conoce cada uno (LJCA, arts. 6 a 14; LO 1/2025) · III. Contra qué se recurre y en qué plazo (LJCA, arts. 25 a 30, 45 y 46) · IV. Quiénes son las partes (LJCA, arts. 18 a 24). Cada artículo: texto literal del BOE y ficha.",
  ["LJCA", "Art. 106.1 CE", "Improrrogable", "Tribunales de Instancia", "Audiencia Nacional", "Tribunal Supremo", "Actividad impugnable", "Inactividad", "Vía de hecho", "Actos confirmatorios", "Plazo de dos meses", "Legitimación", "Lesividad", "Procurador y Abogado"])

T.ap("s0", "Mapa del tema: cuatro preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque IV, tema 13):
> La jurisdicción contencioso-administrativa: funciones, órganos y competencias. El recurso contencioso-administrativo. Actividad administrativa impugnable. Las partes: capacidad, legitimación, representación y defensa.

### El hilo conductor

| Bloque | Pregunta | Normas |
|---|---|---|
| **I** | ¿Para qué sirve? (funciones y ámbito) | CE, arts. 106.1 y 153; LJCA, arts. 1 a 5; LOPJ, art. 9 |
| **II** | ¿Qué órganos la forman y qué conoce cada uno? (órganos y competencias) | LJCA, arts. 6 a 14; LO 1/2025, disposiciones adicional primera y transitoria primera |
| **III** | ¿Contra qué se recurre y en qué plazo? (recurso y actividad impugnable) | LJCA, arts. 25 a 30, 45 y 46 |
| **IV** | ¿Quiénes son las partes? (capacidad, legitimación, representación y defensa) | LJCA, arts. 18 a 24 |

!> **La idea que une los cuatro bloques:** la Constitución manda que los Tribunales **controlen** la actuación administrativa (art. 106.1). La LJCA dice **qué** se controla (actuación sujeta al Derecho Administrativo, reglamentos, decretos legislativos *ultra vires*), **quién** lo controla (cinco clases de órganos con un reparto de competencias por materia y por órgano autor), **contra qué** se recurre (disposiciones, actos, inactividad y vía de hecho) y **quién** puede litigar (capacidad, legitimación, representación y defensa).

?> **Aviso de vigencia (Tribunales de Instancia).** La LJCA sigue hablando de «**Juzgados** de lo Contencioso-administrativo» y «Juzgados **Centrales**». Desde la LO 1/2025, esas referencias se entienden hechas a las **Secciones de lo Contencioso-Administrativo de los Tribunales de Instancia** y del **Tribunal Central de Instancia** (→ II.1.2). Se cita la LJCA literalmente, como está en el BOE.
""")

# =============================================================================
T.ap("bI", "I. ¿Para qué sirve? Funciones y ámbito (arts. 106.1 y 153 CE; LJCA, arts. 1 a 5)", donde(
  "Primera pregunta del tema: la **función** de esta jurisdicción y su **ámbito**, es decir, qué asuntos le corresponden y cuáles no.",
  ["1 Fundamento constitucional (arts. 106.1 y 153 c CE)", "2 Ámbito: qué conoce y qué no (LJCA, arts. 1 a 3)", "3 Cuestiones prejudiciales e improrrogabilidad (LJCA, arts. 4 y 5; LOPJ, art. 9)"]))

T.ap("s1", "I.1 Fundamento constitucional (arts. 106.1 y 153 c CE)", f"""
{unidad("1.1 Control de la potestad reglamentaria y de la actuación administrativa (art. 106.1)",
  lit("CE", "Artículo 106", ["controlan la potestad reglamentaria y la legalidad de la actuación administrativa", "sometimiento de ésta a los fines que la justifican"], solo=[1]),
  fichab("Función de los Tribunales frente a la Administración", "Los **Tribunales**",
         ["Controlan la **potestad reglamentaria**", "Controlan la **legalidad** de la actuación administrativa", "Controlan su **sometimiento a los fines** que la justifican (desviación de poder)"],
         "—", "Tres objetos del control: **reglamentos**, **legalidad** y **fines**. El 106.2 (responsabilidad patrimonial) es del tema IV.10."))}

{unidad("1.2 Control de las Comunidades Autónomas (art. 153 c)",
  lit("CE", "Artículo 153", ["Por la jurisdicción contencioso-administrativa, el de la administración autónoma y sus normas reglamentarias"]),
  fichab("Quién controla a las Comunidades Autónomas",
         ["**Tribunal Constitucional**: disposiciones con fuerza de ley", "**Gobierno**, previo dictamen del Consejo de Estado: funciones delegadas (art. 150.2)", "**Jurisdicción contencioso-administrativa**: administración autónoma y normas **reglamentarias**", "**Tribunal de Cuentas**: control económico y presupuestario"],
         "—", "—",
         "Administración autonómica y **reglamentos** autonómicos → **contencioso** (pregunta oficial X 65, → Cierre 1). Las **leyes** autonómicas → **TC**."))}
""", 2)

T.ap("s2", "I.2 Ámbito: qué conoce y qué no (LJCA, arts. 1 a 3)", f"""
{unidad("2.1 Objeto de la jurisdicción (art. 1)",
  lit("LJCA", "Artículo 1", ["actuación de las Administraciones públicas sujeta al Derecho Administrativo", "con las disposiciones generales de rango inferior a la Ley", "con los Decretos legislativos cuando excedan los límites de la delegación"]),
  fichab("Qué controla",
         ["::Administraciones públicas (1.2):", "Administración General del Estado", "Administraciones de las Comunidades Autónomas", "Entidades que integran la Administración local", "Entidades de Derecho público dependientes o vinculadas a ellas"],
         ["Actuación administrativa sujeta al **Derecho Administrativo**", "Disposiciones generales de **rango inferior a la ley**", "**Decretos legislativos** que excedan los límites de la delegación", "Actos de personal, administración y gestión patrimonial de **órganos constitucionales** y autonómicos análogos, actos del **CGPJ** y Administración **electoral** (1.3)"],
         "—",
         "Los decretos legislativos solo cuando **excedan la delegación** (*ultra vires*). De los órganos constitucionales, solo **personal, administración y gestión patrimonial**."))}

{unidad("2.2 Materias atribuidas (art. 2)",
  lit("LJCA", "Artículo 2", ["los elementos reglados y la determinación de las indemnizaciones", "cualquiera que fuese la naturaleza de dichos actos", "los actos de preparación y adjudicación de los demás contratos", "adoptados en el ejercicio de funciones públicas", "no pudiendo ser demandadas aquellas por este motivo ante los órdenes jurisdiccionales civil o social"]),
  fichab("Cuestiones que conoce este orden",
         "—",
         ["**Actos del Gobierno** y de los Consejos de Gobierno autonómicos: derechos fundamentales, **elementos reglados** e **indemnizaciones** (a)", "**Contratos administrativos** y preparación y adjudicación de los demás contratos de las AAPP (b)", "**Corporaciones de Derecho público** en funciones públicas (c)", "Control de los **concesionarios** (d)", "**Responsabilidad patrimonial**, sea cual sea la actividad (e; → tema IV.10)", "Las demás que le atribuya una ley (f)"],
         "—",
         "Actos del Gobierno: **solo** derechos fundamentales, elementos reglados e indemnizaciones. Contratos privados de las AAPP: solo **preparación y adjudicación**."))}

{unidad("2.3 Materias excluidas (art. 3)",
  lit("LJCA", "Artículo 3", ["expresamente atribuidas a los órdenes jurisdiccionales civil, penal y social", "El recurso contencioso-disciplinario militar", "Los conflictos de jurisdicción", "Normas Forales fiscales"]),
  fichab("Qué no le corresponde",
         "—",
         ["Cuestiones atribuidas a los órdenes **civil, penal y social**, aunque se relacionen con la Administración", "El recurso **contencioso-disciplinario militar**", "**Conflictos de jurisdicción** y **de atribuciones**", "**Normas Forales fiscales** de Álava, Guipúzcoa y Vizcaya (corresponden al **Tribunal Constitucional**)"],
         "—",
         "Normas Forales fiscales → **TC**, en exclusiva. Conflictos de **atribuciones** entre órganos de una misma Administración: **excluidos**."))}
""", 2)

T.ap("s3", "I.3 Cuestiones prejudiciales e improrrogabilidad (LJCA, arts. 4 y 5; LOPJ, art. 9)", f"""
{unidad("3.1 Cuestiones prejudiciales e incidentales (art. 4)",
  lit("LJCA", "Artículo 4", ["salvo las de carácter constitucional y penal", "no producirá efectos fuera del proceso en que se dicte"]),
  fichab("Extensión de la competencia", "El órgano contencioso que conoce del recurso",
         "Decide cuestiones prejudiciales e incidentales **no administrativas** directamente relacionadas con el recurso",
         "—", "Excepción: las de carácter **constitucional** y **penal**. Lo decidido **no** surte efectos fuera del proceso ni vincula al otro orden."))}

{unidad("3.2 Improrrogabilidad (art. 5)",
  lit("LJCA", "Artículo 5", ["es improrrogable", "por plazo común de diez días", "en el plazo de un mes desde que fuera notificada"]),
  fichab("La jurisdicción no se puede prorrogar", "El órgano judicial, **de oficio**, con audiencia de las partes y del Ministerio Fiscal",
         ["Aprecia de oficio la **falta de jurisdicción** (5.2)", "Si la demanda se presenta ante el orden indicado **en un mes**, se entiende presentada en la fecha inicial (5.3)"],
         "Audiencia: **10 días** (plazo común) · nueva demanda: **1 mes**",
         "**Improrrogable**: ni las partes pueden someterle asuntos de otro orden. Audiencia común de **diez** días."))}

{unidad("3.3 El orden contencioso en la LOPJ (art. 9.4)",
  lit("LOPJ", "anoveno", ["con los reales decretos legislativos en los términos previstos en el artículo 82.6 de la Constitución", "contra la inactividad de la Administración y contra sus actuaciones materiales que constituyan vía de hecho", "Si a la producción del daño hubieran concurrido sujetos privados"], solo=[5, 6, 7], titulo="Artículo 9 (LOPJ)"),
  fichab("Atribución orgánica del orden contencioso", "Los jueces y Tribunales del orden contencioso-administrativo",
         ["Mismo objeto que el art. 1 LJCA, con remisión al **art. 82.6 CE** para los decretos legislativos", "Inactividad y **vía de hecho**", "Responsabilidad patrimonial, también frente a **sujetos privados** concurrentes y la **aseguradora**"],
         "—", "Si concurren **particulares** en el daño, el demandante también los demanda **ante este orden**."))}

{resumen([
  "Art. 106.1 CE: los Tribunales controlan la **potestad reglamentaria**, la **legalidad** y el sometimiento a los **fines**; art. 153 c: la administración autonómica y sus **reglamentos**.",
  "Objeto (art. 1): actuación sujeta al Derecho Administrativo, **reglamentos** y **decretos legislativos ultra vires**.",
  "Excluidos (art. 3): lo atribuido a los órdenes civil, penal y social; contencioso-disciplinario militar; conflictos de jurisdicción y atribuciones; Normas Forales fiscales (**TC**).",
  "Jurisdicción **improrrogable**: se aprecia de oficio con audiencia de **diez días** (art. 5)."],
  "Siguiente: II. ¿Qué órganos la forman y qué conoce cada uno?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Qué órganos la forman y qué conoce cada uno? (LJCA, arts. 6 a 14; LO 1/2025)", donde(
  "Segunda pregunta. La LJCA enumera **cinco** clases de órganos y reparte los asuntos entre ellos según el **órgano autor** del acto, la **materia** y la **cuantía**. La LO 1/2025 ha cambiado el nombre de los dos primeros.",
  ["1 Órganos del orden contencioso (LJCA, art. 6; LO 1/2025)", "2 Reglas generales de competencia (art. 7)", "3 Juzgados y Juzgados Centrales (arts. 8 y 9)", "4 Salas de los TSJ, de la Audiencia Nacional y del Tribunal Supremo (arts. 10 a 12)", "5 Criterios de reparto y competencia territorial (arts. 13 y 14)"]))

T.ap("s4", "II.1 Órganos del orden contencioso (LJCA, art. 6; LO 1/2025)", f"""
{unidad("1.1 Los cinco órganos (art. 6)",
  lit("LJCA", "Artículo 6", ["Juzgados de lo Contencioso-administrativo", "Juzgados Centrales de lo Contencioso-administrativo", "Tribunales Superiores de Justicia", "Audiencia Nacional", "Tribunal Supremo"]),
  fichab("Planta del orden contencioso",
         ["Unipersonales: **Juzgados** y **Juzgados Centrales** (hoy, Secciones de los Tribunales de Instancia: → 1.2)", "Colegiados: **Salas** de lo Contencioso de los **TSJ**, de la **Audiencia Nacional** y del **Tribunal Supremo**"],
         "—", "—",
         f"**Cinco** clases de órganos. «Centrales» = competencia en **todo el territorio nacional**, con sede en Madrid: hoy, Sección de lo Contencioso-Administrativo del Tribunal Central de Instancia (LOPJ, art. 95: {c('LOPJ', 'anoventaycinco', 'En la Villa de Madrid y con jurisdicción en todo el territorio nacional existirá un Tribunal Central de Instancia')})."))}

{unidad("1.2 Juzgados → Secciones de los Tribunales de Instancia (LO 1/2025)",
  lit("LO1_2025", "da", ["de lo Contencioso-Administrativo", "se entenderán referidas a las Secciones del orden jurisdiccional correspondiente de los Tribunales de Instancia", "las referencias a los Juzgados Centrales respecto de las correspondientes Secciones del Tribunal Central de Instancia"], titulo="Disposición adicional primera (LO 1/2025). Menciones a Juzgados y Tribunales"),
  lit("LO1_2025", "dt", ["El día 31 de diciembre de 2025, los restantes Juzgados"], solo=[3, 4, 5, 6], titulo="Disposición transitoria primera (LO 1/2025). Constitución de los Tribunales de Instancia (fragmento)"),
  fichab("Nueva denominación de los órganos unipersonales",
         ["**Secciones de lo Contencioso-Administrativo** de los **Tribunales de Instancia** (antes, Juzgados de lo Contencioso-administrativo)", "**Secciones** del **Tribunal Central de Instancia** (antes, Juzgados Centrales)"],
         "Transformación escalonada de los Juzgados en Secciones; los Juzgados no incluidos en las dos primeras fases (como los de lo contencioso) se transforman el **31 de diciembre de 2025**",
         "1-7-2025, 1-10-2025 y **31-12-2025** (tres fases)",
         "La LJCA no se ha reescrito: donde dice «Juzgado» hay que leer «**Sección** del Tribunal de Instancia». Las **Salas** (TSJ, AN y TS) no cambian."))}
""", 2)

T.ap("s5", "II.2 Reglas generales de competencia (art. 7)", f"""
{unidad("2.1 Competencia para incidencias y ejecución; improrrogabilidad (art. 7)",
  lit("LJCA", "Artículo 7", ["para hacer ejecutar las sentencias que dictaren", "no será prorrogable", "adoptará la forma de auto y deberá efectuarse antes de la sentencia", "en el plazo de diez días comparezcan"]),
  fichab("Competencia objetiva", "El órgano competente para el asunto",
         ["Conoce también de las **incidencias** y **ejecuta** sus sentencias (7.1)", "La competencia **no es prorrogable** y se aprecia **de oficio** (7.2)", "La incompetencia se declara por **auto**, **antes de la sentencia**, remitiendo las actuaciones al competente (7.3)"],
         "Audiencia: **10 días** · comparecencia ante el competente: **10 días**",
         "Forma: **auto** (no sentencia ni providencia) y **antes** de la sentencia."))}
""", 2)

T.ap("s6", "II.3 Juzgados y Juzgados Centrales (arts. 8 y 9)", f"""
{unidad("3.1 Juzgados de lo Contencioso-administrativo (art. 8)",
  lit("LJCA", "Artículo 8", ["frente a los actos de las entidades locales", "excluidas las impugnaciones de cualquier clase de instrumentos de planeamiento urbanístico", "salvo cuando procedan del respectivo Consejo de Gobierno", "multas no superiores a 60.000 euros", "cuya cuantía no exceda de 30.050 euros", "en materia de extranjería", "Juntas Electorales de Zona", "las autorizaciones para la entrada en domicilios"], solo=list(range(1, 11))),
  fichab("Qué conocen los Juzgados (hoy, Secciones de los Tribunales de Instancia)",
         "Juzgados de lo Contencioso-administrativo, en **única o primera instancia**",
         ["Actos de las **entidades locales** (salvo planeamiento urbanístico) (8.1)", "Actos de las **CCAA** (no del Consejo de Gobierno) sobre **personal** (salvo nacimiento o extinción de la relación de funcionarios de carrera), **sanciones** (multas hasta **60.000 €**, ceses o privaciones hasta **6 meses**) y **responsabilidad patrimonial** hasta **30.050 €** (8.2)", "Administración **periférica** del Estado y de las CCAA (8.3); se exceptúan los actos de la periférica **del Estado** y de los organismos públicos estatales de cuantía superior a **60.000 €** o sobre dominio público, obras públicas del Estado, expropiación forzosa y propiedades especiales", "**Extranjería** de la periférica del Estado y de las CCAA (8.4)", "Juntas Electorales de **Zona** (8.5)", "**Autorizaciones** de entrada en domicilio y ratificación de medidas sanitarias (8.6)"],
         "Cuantías: **60.000 €** (multas; excepción de la periférica del Estado) · **30.050 €** (responsabilidad patrimonial) · **6 meses** (ceses)",
         "**Extranjería** de las CCAA → **Juzgado** (no TSJ; pregunta oficial P 76, → Cierre 1). Planeamiento urbanístico local → **TSJ**."))}

{unidad("3.2 Juzgados Centrales de lo Contencioso-administrativo (art. 9)",
  lit("LJCA", "Artículo 9", ["actos dictados por Ministros y Secretarios de Estado", "organismos públicos con personalidad jurídica propia y entidades pertenecientes al sector público estatal con competencia en todo el territorio nacional", "cuando lo reclamado no exceda de 30.050 euros", "inadmisión de las peticiones de asilo político", "Comité Español de Disciplina Deportiva"], solo=list(range(1, 8))),
  fichab("Qué conocen los Juzgados Centrales (hoy, Secciones del Tribunal Central de Instancia)",
         "Juzgados Centrales, en **única o primera instancia**",
         ["**Personal**: actos de **Ministros y Secretarios de Estado**, con excepciones (a)", "Órganos centrales de la AGE en los supuestos del 8.2 b (sanciones) (b)", "Organismos y entidades del **sector público estatal** con competencia en todo el territorio (c)", "**Responsabilidad patrimonial** de Ministros y Secretarios de Estado hasta **30.050 €** (d)", "**Inadmisión de asilo**, en primera instancia (e)", "**Comité Español de Disciplina Deportiva** (f)"],
         "Responsabilidad patrimonial: hasta **30.050 €**",
         "Ministros y SE: por regla van a la **Audiencia Nacional** (art. 11); al Juzgado Central solo **personal** y responsabilidad patrimonial **≤ 30.050 €**."))}
""", 2)

T.ap("s7", "II.4 Salas de los TSJ, de la Audiencia Nacional y del Tribunal Supremo (arts. 10 a 12)", f"""
{unidad("4.1 Salas de los Tribunales Superiores de Justicia (art. 10)",
  lit("LJCA", "Artículo 10", ["cuyo conocimiento no esté atribuido a los Juzgados de lo Contencioso-Administrativo", "Las disposiciones generales emanadas de las Comunidades Autónomas y de las Entidades locales", "Tribunales Económico-Administrativos Regionales y Locales", "en materia de tributos cedidos", "Tribunales Administrativos Territoriales de Recursos Contractuales", "Cualesquiera otras actuaciones administrativas no atribuidas expresamente", "en segunda instancia, de las apelaciones"], solo=list(range(1, 21))),
  fichab("Qué conocen las Salas de los TSJ",
         "Sala de lo Contencioso-Administrativo del TSJ",
         ["**Única instancia**: actos locales y autonómicos no atribuidos a los Juzgados; **disposiciones generales** de CCAA y entidades locales; TEAR y TEAL; TEAC en **tributos cedidos**; Juntas Electorales Provinciales y de CCAA; convenios autonómicos; derecho de reunión; órganos de la AGE de nivel **inferior a Ministro o SE** en personal, propiedades especiales y expropiación; defensa de la competencia autonómica; tribunales **territoriales** de recursos contractuales; y la **cláusula residual** (n) (10.1)", "**Segunda instancia**: apelaciones contra los **Juzgados** (10.2)", "Revisión contra sentencias firmes de los Juzgados; cuestiones de competencia entre Juzgados; casación para la unificación de doctrina (art. 99) y en interés de la ley (art. 101) (10.3 a 6)"],
         "—",
         "**Reglamentos** autonómicos y **locales** → **TSJ** en única instancia (pregunta oficial P 76, → Cierre 1). Competencia **residual**: TSJ (letra n)."))}

{unidad("4.2 Sala de la Audiencia Nacional (art. 11)",
  lit("LJCA", "Artículo 11", ["las disposiciones generales y los actos de los Ministros", "y de los Secretarios de Estado", "Tribunal Económico-Administrativo Central", "Tribunal Administrativo Central de Recursos Contractuales", "en segunda instancia, de las apelaciones contra autos y sentencias dictados por los Juzgados Centrales"]),
  fichab("Qué conoce la Sala de la Audiencia Nacional",
         "Sala de lo Contencioso-administrativo de la AN",
         ["**Única instancia**: disposiciones y actos de **Ministros** y **Secretarios de Estado** (aunque haya informe o acuerdo del Consejo de Ministros); convenios no atribuidos a los TSJ; **TEAC** (salvo tributos cedidos); **TACRC** (salvo el 10.1 k); Banco de España, CNMV y FROB en resolución de entidades; CNMC en unidad de mercado (11.1)", "**Segunda instancia**: apelaciones contra los **Juzgados Centrales** (11.2)", "Revisión y cuestiones de competencia de los Juzgados Centrales (11.3 y 4)"],
         "—",
         "**TACRC** → **Audiencia Nacional**; tribunales **territoriales** de recursos contractuales → **TSJ**."))}

{unidad("4.3 Sala del Tribunal Supremo (art. 12)",
  lit("LJCA", "Artículo 12", ["Los actos y disposiciones del Consejo de Ministros y de las Comisiones Delegadas del Gobierno", "del Consejo General del Poder Judicial y del Fiscal General del Estado", "Los recursos de casación de cualquier modalidad", "Junta Electoral Central"]),
  fichab("Qué conoce la Sala Tercera del Tribunal Supremo",
         "Sala de lo Contencioso-administrativo del TS",
         ["**Única instancia**: **Consejo de Ministros** y **Comisiones Delegadas**; **CGPJ** y **Fiscal General del Estado**; personal, administración y gestión patrimonial de **Congreso, Senado, TC, Tribunal de Cuentas y Defensor del Pueblo** (12.1)", "Casación **de cualquier modalidad** y queja; casación y revisión contra el **Tribunal de Cuentas**; revisión contra sentencias firmes de TSJ, AN y TS (12.2)", "**Junta Electoral Central** y proclamación de electos (12.3)"],
         "—",
         "**Consejo de Ministros** → **TS**; **Ministros** → **AN**. Casación «de **cualquier** modalidad» → TS."))}
""", 2)

T.ap("s8", "II.5 Criterios de reparto y competencia territorial (arts. 13 y 14)", f"""
{unidad("5.1 Criterios para aplicar las reglas (art. 13)",
  lit("LJCA", "Artículo 13", ["comprenden a las Entidades y Corporaciones dependientes o vinculadas", "incluye la relativa a la inactividad y a las actuaciones constitutivas de vía de hecho", "la atribución de competencia por razón de la materia prevalece"]),
  fichab("Cómo se interpretan las reglas de competencia", "—",
         ["Las referencias a cada Administración incluyen sus **entes dependientes o vinculados**", "La competencia sobre actos incluye la **inactividad** y la **vía de hecho**", "Salvo disposición en contrario, la **materia** prevalece sobre el **órgano** autor"],
         "—", "Conflicto entre criterios: gana la **materia**."))}

{unidad("5.2 Competencia territorial de Juzgados y TSJ (art. 14)",
  lit("LJCA", "Artículo 14", ["en cuya circunscripción tenga su sede el órgano que hubiere dictado la disposición o el acto originario impugnado", "a elección del demandante", "radiquen los inmuebles afectados"]),
  fichab("Qué Juzgado o TSJ en concreto",
         "—",
         ["Regla general: el de la **sede del órgano** autor del acto originario", "Responsabilidad patrimonial, personal, propiedades especiales y sanciones: **a elección del demandante**, su **domicilio** o la sede del órgano (limitado a la circunscripción del TSJ si el acto es autonómico o local)", "Urbanismo, expropiación e intervención en la propiedad: donde **radiquen los inmuebles**", "Pluralidad de destinatarios: la **sede del órgano**"],
         "—", "Elección por el **domicilio** del demandante solo en **cuatro** materias."))}

{resumen([
  "Cinco órganos (art. 6); los **Juzgados** y **Juzgados Centrales** son hoy **Secciones** de los Tribunales de Instancia y del Tribunal Central de Instancia (LO 1/2025).",
  "**Juzgados**: entidades locales, extranjería, sanciones ≤ 60.000 €, responsabilidad ≤ 30.050 € de las CCAA. **Centrales**: personal de Ministros y SE, sector público estatal, asilo.",
  "**TSJ**: reglamentos autonómicos y locales, TEAR, apelaciones de los Juzgados y la cláusula **residual**. **AN**: **Ministros** y **SE**, TEAC, TACRC. **TS**: **Consejo de Ministros**, CGPJ, órganos constitucionales y **casación**.",
  "Prevalece la **materia** sobre el órgano (art. 13 c); territorio: sede del órgano, con elección del demandante en cuatro materias (art. 14)."],
  "Siguiente: III. ¿Contra qué se recurre y en qué plazo?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Contra qué se recurre y en qué plazo? (LJCA, arts. 25 a 30, 45 y 46)", donde(
  "Tercera pregunta. La **actividad administrativa impugnable** es el objeto del recurso: disposiciones, actos, inactividad y vía de hecho. Después, cómo y cuándo se interpone.",
  ["1 Actividad impugnable: disposiciones y actos (arts. 25 a 28)", "2 Inactividad y vía de hecho (arts. 29 y 30)", "3 Interposición y plazos (arts. 45 y 46)"]))

T.ap("s9", "III.1 Actividad impugnable: disposiciones y actos (arts. 25 a 28)", f"""
{unidad("1.1 Qué es recurrible (art. 25)",
  lit("LJCA", "Artículo 25", ["con las disposiciones de carácter general y con los actos expresos y presuntos de la Administración pública que pongan fin a la vía administrativa", "ya sean definitivos o de trámite", "contra la inactividad de la Administración y contra sus actuaciones materiales que constituyan vía de hecho"]),
  fichab("Actividad administrativa impugnable",
         "—",
         ["**Disposiciones de carácter general**", "**Actos expresos y presuntos** que **pongan fin a la vía administrativa**: definitivos o de **trámite cualificados** (deciden el fondo, impiden continuar, producen indefensión o perjuicio irreparable)", "**Inactividad** de la Administración", "**Vía de hecho** (actuaciones materiales)"],
         "—",
         "Los actos han de **poner fin a la vía administrativa**. Trámite: solo los **cualificados** (los mismos cuatro supuestos del art. 112.1 LPAC; tema IV.12)."))}

{unidad("1.2 Recurso indirecto contra reglamentos y cuestión de ilegalidad (arts. 26 y 27)",
  lit("LJCA", "Artículo 26", ["los actos que se produzcan en aplicación de las mismas", "no impiden la impugnación de los actos de aplicación"]),
  lit("LJCA", "Artículo 27", ["deberá plantear la cuestión de ilegalidad", "la sentencia declarará la validez o nulidad de la disposición general", "el Tribunal Supremo anulará cualquier disposición general"]),
  fichab("Impugnación indirecta de disposiciones generales",
         ["Juez o Tribunal que estima el recurso indirecto: plantea la **cuestión de ilegalidad** al competente para el recurso directo", "Si es competente también para el directo, o es el **Tribunal Supremo**: declara directamente la validez o nulidad"],
         ["Se recurre el **acto de aplicación** alegando que el reglamento no es conforme a Derecho (26.1)", "No impide hacerlo que no se impugnara el reglamento o que se desestimara el recurso directo (26.2)", "Sentencia firme estimatoria → **cuestión de ilegalidad** (27.1)"],
         "—",
         "La cuestión de ilegalidad se plantea **tras** la sentencia **firme estimatoria**. El **TS** anula sin necesidad de plantearla."))}

{unidad("1.3 Actos no impugnables (art. 28)",
  lit("LJCA", "Artículo 28", ["reproducción de otros anteriores definitivos y firmes", "los confirmatorios de actos consentidos por no haber sido recurridos en tiempo y forma"]),
  fichab("Inadmisibilidad por razón del acto", "—",
         ["Actos que **reproducen** otros anteriores **definitivos y firmes**", "Actos **confirmatorios** de actos **consentidos** (no recurridos en tiempo y forma)"],
         "—", "Es la respuesta de la pregunta oficial X 63 (→ Cierre 1): las otras opciones describen lo que **sí** es admisible (arts. 25 y 26)."))}
""", 2)

T.ap("s10", "III.2 Inactividad y vía de hecho (arts. 29 y 30)", f"""
{unidad("2.1 Recurso contra la inactividad (art. 29)",
  lit("LJCA", "Artículo 29", ["esté obligada a realizar una prestación concreta en favor de una o varias personas determinadas", "Si en el plazo de tres meses desde la fecha de la reclamación", "si ésta no se produce en el plazo de un mes desde tal petición", "procedimiento abreviado"]),
  fichab("Inactividad de la Administración",
         "Quienes tengan **derecho a la prestación** (29.1) o los **afectados** por la falta de ejecución (29.2)",
         ["**Prestación debida**: por disposición general sin actos de aplicación, acto, contrato o convenio → **reclamación previa** a la Administración (29.1)", "**Falta de ejecución de actos firmes** → solicitud de ejecución; el recurso va por el procedimiento **abreviado** (29.2)"],
         "Prestación: **3 meses** desde la reclamación · ejecución: **1 mes** desde la petición",
         "Prestación → **tres meses**; ejecución de actos firmes → **un mes** y procedimiento **abreviado**."))}

{unidad("2.2 Recurso contra la vía de hecho (art. 30)",
  lit("LJCA", "Artículo 30", ["podrá formular requerimiento a la Administración actuante, intimando su cesación", "dentro de los diez días siguientes a la presentación del requerimiento", "podrá deducir directamente recurso contencioso-administrativo"]),
  fichab("Actuación material sin cobertura (vía de hecho)", "El interesado",
         ["Requerimiento **potestativo** («podrá») de cesación", "Si no se formula o no se atiende en **10 días**, recurso **directo**"],
         "Atender el requerimiento: **10 días**",
         "El requerimiento es **potestativo**: puede recurrirse **directamente** (plazos en → III.3.2)."))}
""", 2)

T.ap("s11", "III.3 Interposición y plazos (arts. 45 y 46)", f"""
{unidad("3.1 El escrito de interposición (art. 45)",
  lit("LJCA", "Artículo 45", ["por un escrito reducido a citar la disposición, acto, inactividad o actuación constitutiva de vía de hecho", "El recurso de lesividad se iniciará por demanda", "podrá iniciarse también mediante demanda"]),
  fichab("Cómo empieza el proceso",
         "El recurrente; el **Secretario judicial** (hoy, Letrado de la Administración de Justicia) examina la comparecencia (45.3)",
         ["Regla: **escrito de interposición** que cita lo impugnado y pide que se tenga por interpuesto (45.1), con los documentos del 45.2 (representación, legitimación, copia del acto, requisitos de personas jurídicas, autorización de afiliados)", "**Lesividad**: por **demanda**, con la declaración de lesividad y el expediente (45.4)", "Sin terceros interesados: puede iniciarse **por demanda** (45.5)"],
         "—",
         "Normalmente se inicia por **escrito de interposición**, no por demanda; por **demanda**: lesividad y supuestos sin terceros interesados."))}

{unidad("3.2 Plazos para recurrir (art. 46)",
  lit("LJCA", "Artículo 46", ["será de dos meses contados desde el día siguiente al de la publicación de la disposición impugnada", "Si no lo fuera, el plazo será de seis meses", "será de diez días a contar desde el día siguiente a la terminación del plazo establecido en el artículo 30", "el plazo será de veinte días", "en que éste deba entenderse presuntamente desestimado", "El plazo para interponer recurso de lesividad será de dos meses"]),
  tc_doc("STC52_2014", STC52, "STC 52/2014, de 10 de abril (BOE núm. 111, de 7 de mayo de 2014) · resumen del buscador de jurisprudencia del Tribunal Constitucional (doctrina; no es texto legal)",
         ['Se desestima la cuestión de inconstitucionalidad. El precepto impugnado no vulnera el derecho a la tutela judicial efectiva en su vertiente de acceso a la justicia. De acuerdo con la jurisprudencia del Tribunal Constitucional, el silencio administrativo negativo es una mera ficción legal que responde a la finalidad de que el ciudadano pueda acceder a la vía judicial, pero que no exonera de la obligación de resolver expresamente. Con arreglo a la ordenación del silencio administrativo introducida en la Ley de procedimiento administrativo, no tienen encaje en el concepto legal de acto presunto los supuestos en los que, como en el presente, el ordenamiento jurídico determina el efecto desestimatorio de la solicitud formulada, de modo que la impugnación jurisdiccional de las desestimaciones por silencio administrativo no está sujeta al plazo de caducidad de seis meses previsto en dicho precepto.'],
         ["no está sujeta al plazo de caducidad de seis meses"]),
  fichab("Cuándo se recurre",
         "El recurrente",
         ["Desde el día **siguiente** a la publicación o notificación", "Si hubo **reposición**, desde su resolución expresa o desestimación presunta (46.4)"],
         ["::Plazos:", "Disposición o acto **expreso**: **2 meses** (46.1)", "Acto no expreso: **6 meses** según el texto (46.1; ver la STC 52/2014 arriba)", "Inactividad (art. 29): **2 meses** desde el vencimiento de los plazos del art. 29 (46.2)", "Vía de hecho: **10 días** tras el plazo del requerimiento; sin requerimiento, **20 días** (46.3)", "**Lesividad**: **2 meses** desde la declaración (46.5)", "Litigios entre Administraciones: **2 meses** (46.6)"],
         "**Dos meses** desde el día siguiente (pregunta oficial P 77, → Cierre 1). Vía de hecho: **10** o **20** días."))}

?> **Cómo leer el plazo de seis meses.** El texto del art. 46.1 sigue diciendo «seis meses» para el acto no expreso, y así hay que citarlo en el examen. Pero, según la STC 52/2014, contra la **desestimación por silencio** no corre ese plazo de caducidad de seis meses.

{resumen([
  "Impugnables (art. 25): **disposiciones generales**, **actos** que **ponen fin a la vía** (definitivos o de trámite cualificados), **inactividad** y **vía de hecho**.",
  "Recurso **indirecto** contra reglamentos (art. 26) y **cuestión de ilegalidad** tras sentencia firme estimatoria (art. 27).",
  "**No** impugnables (art. 28): actos que **reproducen** otros **definitivos y firmes** y **confirmatorios** de actos **consentidos**.",
  "Plazos (art. 46): **dos meses** (acto expreso, lesividad, entre Administraciones); vía de hecho **10/20 días**; el de seis meses no se aplica a la desestimación por silencio (STC 52/2014)."],
  "Siguiente: IV. ¿Quiénes son las partes?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Quiénes son las partes? Capacidad, legitimación, representación y defensa (LJCA, arts. 18 a 24)", donde(
  "Cuarta pregunta. Para litigar hace falta **capacidad** (poder ser parte en el proceso), **legitimación** (relación con el asunto) y, salvo excepciones, **representación** por Procurador y **defensa** por Abogado.",
  ["1 Capacidad procesal (art. 18)", "2 Legitimación activa y pasiva (arts. 19 a 22)", "3 Representación y defensa (arts. 23 y 24)"]))

T.ap("s12", "IV.1 Capacidad procesal (art. 18)", f"""
{unidad("1.1 Quién tiene capacidad procesal (art. 18)",
  lit("LJCA", "Artículo 18", ["los menores de edad para la defensa de aquellos de sus derechos e intereses legítimos", "cuando la Ley así lo declare expresamente"]),
  fichab("Capacidad para comparecer en el proceso",
         ["Quienes la tengan según la **Ley de Enjuiciamiento Civil**", "**Menores de edad**, para los derechos cuya actuación les permita el ordenamiento sin asistencia de quien ejerza la patria potestad, tutela o curatela", "**Grupos de afectados**, uniones sin personalidad o patrimonios autónomos, **cuando la ley lo declare expresamente**"],
         "—", "—",
         "Más amplia que en la LEC: añade **menores** (en lo que pueden actuar solos) y entes **sin personalidad** (si la ley lo dice)."))}
""", 2)

T.ap("s13", "IV.2 Legitimación activa y pasiva (arts. 19 a 22)", f"""
{unidad("2.1 Legitimación activa (art. 19)",
  lit("LJCA", "Artículo 19", ["Las personas físicas o jurídicas que ostenten un derecho o interés legítimo", "intereses legítimos colectivos", "El Ministerio Fiscal para intervenir en los procesos que determine la Ley", "en ejercicio de la acción popular, en los casos expresamente previstos por las Leyes", "previa su declaración de lesividad para el interés público"], solo=list(range(1, 19))),
  fichab("Quién puede recurrir",
         ["Personas físicas o jurídicas con **derecho o interés legítimo** (a)", "Corporaciones, asociaciones, sindicatos y grupos, por **intereses colectivos** (b)", "AGE, CCAA, entidades locales y entidades de Derecho público, en defensa de su ámbito (c, d, e, g)", "**Ministerio Fiscal**, en los procesos que determine la ley (f)", "**Cualquier ciudadano**, por **acción popular**, solo en los casos **previstos por las leyes** (h)", "Igualdad de trato y discriminación; sindicatos por sus afiliados (i, j, k)"],
         ["La **Administración autora** de un acto lo impugna **previa declaración de lesividad** (19.2)", "Vecinos en nombre de las entidades locales: legislación de régimen local (19.3)"],
         "—",
         "Basta un **derecho o interés legítimo**, no un derecho subjetivo (pregunta oficial L 60, → Cierre 1). La acción popular **no** es general: solo si la ley la prevé."))}

{unidad("2.2 Quién no puede recurrir (art. 20)",
  lit("LJCA", "Artículo 20", ["Los órganos de la misma y los miembros de sus órganos colegiados, salvo que una Ley lo autorice expresamente", "cuando obren por delegación o como meros agentes o mandatarios de ella", "respecto de la actividad de la Administración de la que dependan"]),
  fichab("Falta de legitimación frente a la propia Administración", "—",
         ["Sus **órganos** y los **miembros de sus órganos colegiados**, salvo autorización legal", "Particulares que actúan por **delegación** o como **agentes o mandatarios** suyos", "Sus **entidades dependientes o vinculadas**, salvo estatuto específico de autonomía"],
         "—", "Los miembros de un órgano **colegiado** no pueden recurrir sus acuerdos **salvo que una ley lo autorice**."))}

{unidad("2.3 Parte demandada y sucesión procesal (arts. 21 y 22)",
  lit("LJCA", "Artículo 21", ["contra cuya actividad se dirija el recurso", "cuyos derechos o intereses legítimos pudieran quedar afectados por la estimación de las pretensiones del demandante", "que siempre serán parte codemandada", "se considerará también parte demandada a la Administración autora de la misma"]),
  lit("LJCA", "Artículo 22", ["el causahabiente podrá suceder en cualquier estado del proceso"]),
  fichab("Legitimación pasiva",
         ["La **Administración** (u órgano del 1.3) cuya actividad se recurre", "Los **afectados** por una eventual estimación (codemandados)", "Las **aseguradoras** de la Administración: **siempre** codemandadas", "Si se alega la ilegalidad de una disposición general, también su **Administración autora**"],
         ["Organismos sujetos a fiscalización: el autor si la fiscalización aprueba; la fiscalizadora si no aprueba íntegramente (21.2)", "Órganos de recursos contractuales: **no** son demandados (21.3)", "**Sucesión**: el causahabiente puede suceder en **cualquier estado** del proceso si la relación es transmisible (art. 22)"],
         "—",
         "Aseguradora → **siempre** parte codemandada. Los tribunales de recursos contractuales **no** son parte demandada."))}
""", 2)

T.ap("s14", "IV.3 Representación y defensa (arts. 23 y 24)", f"""
{unidad("3.1 Procurador y Abogado (art. 23)",
  lit("LJCA", "Artículo 23", ["podrán conferir su representación a un Procurador y serán asistidas, en todo caso, por Abogado", "deberán conferir su representación a un Procurador y ser asistidas por Abogado", "Podrán, no obstante, comparecer por sí mismos los funcionarios públicos", "que no impliquen separación de empleados públicos inamovibles"]),
  fichab("Representación y defensa de los particulares",
         "Las partes; excepción: los **funcionarios** en defensa de sus derechos estatutarios",
         ["**Órganos unipersonales** (Juzgados): Procurador **potestativo** («podrán»), Abogado **en todo caso**", "**Órganos colegiados** (Salas): Procurador y Abogado **obligatorios**", "**Funcionarios**: pueden comparecer **por sí mismos** en cuestiones de personal que **no** impliquen **separación** de empleados públicos inamovibles, con uso obligatorio de medios electrónicos", "La representación puede conferirse **electrónicamente** (23.4)"],
         "—",
         "Ante el **Juzgado**, Procurador **opcional** pero **Abogado siempre**; ante las **Salas**, los dos. Los funcionarios no pueden litigar solos si se trata de su **separación**."))}

{unidad("3.2 Representación y defensa de las Administraciones (art. 24)",
  lit("LJCA", "Artículo 24", ["se rige por lo dispuesto en la Ley Orgánica del Poder Judicial y en la Ley de Asistencia Jurídica al Estado e Instituciones Públicas"]),
  fichab("Defensa de las Administraciones y órganos constitucionales", "Administraciones públicas y órganos constitucionales",
         "Se rige por la **LOPJ**, la **Ley de Asistencia Jurídica al Estado e Instituciones Públicas** y las normas autonómicas",
         "—", "No se aplica el art. 23: las Administraciones tienen su **propia** representación y defensa (en el Estado, la Abogacía del Estado según esa ley)."))}

{resumen([
  "Capacidad (art. 18): la de la LEC, más **menores** en lo que pueden actuar solos y entes sin personalidad **si la ley lo declara**.",
  "Legitimación (art. 19): **derecho o interés legítimo**; acción popular solo **si la ley la prevé**; la Administración autora, **previa declaración de lesividad**.",
  "No pueden recurrir (art. 20): sus órganos y los miembros de sus colegiados (salvo ley), sus agentes y sus entes dependientes. Aseguradoras: **siempre** codemandadas (art. 21).",
  "Juzgados: Procurador **potestativo**, Abogado **siempre**; Salas: ambos **obligatorios**; funcionarios, por sí mismos salvo **separación** (art. 23)."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX = [
 ("L", 60, "Legitimación activa (→ IV.2.1)", {
   "a": f"La legitimación de {c('LJCA', 'Artículo 19', 'Cualquier ciudadano')} es la **acción popular**, solo {c('LJCA', 'Artículo 19', 'en los casos expresamente previstos por las Leyes')}; no hay legitimación general «sin interés».",
   "b": "Restringe la ley: basta un derecho **o** un **interés legítimo**, no solo un derecho subjetivo.",
   "c": f"Literal del art. 19.1 a): {c('LJCA', 'Artículo 19', 'Las personas físicas o jurídicas que ostenten un derecho o interés legítimo')}.",
   "d": "La Administración demandada es parte **pasiva** (art. 21), y el art. 19 enumera muchos otros legitimados."},
   [("derecho o interés legítimo", "LJCA", "Artículo 19", "Las personas físicas o jurídicas que ostenten un derecho o interés legítimo")]),
 ("P", 76, "Competencias de los TSJ en única instancia (→ II.4.1)", {
   "a": f"Literal del art. 10.1 b): {c('LJCA', 'Artículo 10', 'Las disposiciones generales emanadas de las Comunidades Autónomas y de las Entidades locales')}.",
   "b": f"El TACRC es de la **Audiencia Nacional**: {c('LJCA', 'Artículo 11', 'Las resoluciones dictadas por el Tribunal Administrativo Central de Recursos Contractuales')} (art. 11.1 f). Al TSJ le corresponden los tribunales **territoriales** (10.1 l).",
   "c": f"Los recursos de casación, en general, son del **Tribunal Supremo**: {c('LJCA', 'Artículo 12', 'Los recursos de casación de cualquier modalidad')} (art. 12.2 a). El TSJ solo conoce de las modalidades de los arts. 99 y 101 (10.5 y 6), que no son asuntos «en única instancia».",
   "d": f"La extranjería de las CCAA es de los **Juzgados**: {c('LJCA', 'Artículo 8', 'de todas las resoluciones que se dicten en materia de extranjería por la Administración periférica del Estado o por los órganos competentes de las Comunidades Autónomas')} (art. 8.4)."},
   [("disposiciones generales emanadas de las", "LJCA", "Artículo 10", "Las disposiciones generales emanadas de las Comunidades Autónomas y de las Entidades locales"),
    ("Entidades Locales", "LJCA", "Artículo 10", "y de las Entidades locales")]),
 ("P", 77, "Plazo de dos meses (→ III.3.2)", {
   "a": "Seis meses es el plazo que el texto fija para el acto **no expreso**, no para el expreso.",
   "b": "Cambia el plazo: un mes es el de la reposición (LPAC), no el del recurso contencioso.",
   "c": f"Literal del art. 46.1: {c('LJCA', 'Artículo 46', 'El plazo para interponer el recurso contencioso-administrativo será de dos meses contados desde el día siguiente al de la publicación')}.",
   "d": "Cambia el plazo: tres meses no aparece en el art. 46."},
   [("dos meses", "LJCA", "Artículo 46", "será de dos meses contados desde el día siguiente")]),
 ("X", 63, "Actos no impugnables (→ III.1.3)", {
   "a": f"Sí es admisible: {c('LJCA', 'Artículo 25', 'los actos expresos y presuntos de la Administración pública que pongan fin a la vía administrativa')} (art. 25.1).",
   "b": f"Sí es admisible: {c('LJCA', 'Artículo 26', 'también es admisible la de los actos que se produzcan en aplicación de las mismas, fundada en que tales disposiciones no son conformes a Derecho')} (art. 26.1).",
   "c": f"Sí es admisible: {c('LJCA', 'Artículo 25', 'También es admisible el recurso contra la inactividad de la Administración y contra sus actuaciones materiales que constituyan vía de hecho')} (art. 25.2).",
   "d": f"Literal del art. 28: {c('LJCA', 'Artículo 28', 'No es admisible el recurso contencioso-administrativo respecto de los actos que sean reproducción de otros anteriores definitivos y firmes y los confirmatorios de actos consentidos por no haber sido recurridos en tiempo y forma')}."},
   [("reproducción de otros anteriores definitivos y firmes", "LJCA", "Artículo 28", "reproducción de otros anteriores definitivos y firmes")]),
 ("X", 65, "Control de las Comunidades Autónomas (relacionada; tema I.10) (→ I.1.2)", {
   "a": f"El TC controla {c('CE', 'Artículo 153', 'la constitucionalidad de sus disposiciones normativas con fuerza de ley')}, no la actividad administrativa ni los reglamentos.",
   "b": f"El Gobierno controla, previo dictamen del Consejo de Estado, {c('CE', 'Artículo 153', 'el del ejercicio de funciones delegadas')}.",
   "c": "El art. 153 no atribuye ningún control a un Ministerio.",
   "d": f"Literal del art. 153 c): {c('CE', 'Artículo 153', 'Por la jurisdicción contencioso-administrativa, el de la administración autónoma y sus normas reglamentarias')}."},
   [("jurisdicción contencioso-administrativa", "CE", "Artículo 153", "Por la jurisdicción contencioso-administrativa")]),
]
bloques = []
for cod, n, tit, por, ap_ in EX:
    bloques += [f"### {('GACE-L' if cod == 'L' else 'GACE-P' if cod == 'P' else 'GACE-L extraordinario')} 2025, pregunta {n} · {tit}", examen(cod, n, por, ap_)]
T.ap("s15", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join(
  ["En los primeros ejercicios de **2025** cayeron **cuatro** preguntas de este tema y una **relacionada** (la X 65, del tema I.10, sobre el art. 153 c CE). Todas son literales. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal."]
  + bloques + ["### Cómo se pregunta", "!> Citan el **artículo** de la LJCA y cambian **un plazo** (uno, dos, tres o seis meses), **un órgano** (TSJ, AN, TS, Juzgado) o **invierten** lo admisible y lo inadmisible. Aprende el reparto de competencias por **órgano autor** y los **plazos** del art. 46."]))

T.ap("s16", "Cierre 2. Repaso en 10 minutos (por bloques)", """
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Funciones y ámbito | Art. 106.1 CE; actuación sujeta al Derecho Administrativo, reglamentos y decretos legislativos *ultra vires* (art. 1) | Jurisdicción **improrrogable**; Normas Forales fiscales → **TC** |
| II. Órganos y competencias | Juzgados (hoy Secciones de los Tribunales de Instancia), Centrales, TSJ, AN y TS | **Reglamentos** autonómicos y locales → **TSJ**; **Ministros** → **AN**; **Consejo de Ministros** → **TS**; extranjería → **Juzgado** |
| III. Recurso y actividad impugnable | Disposiciones, actos que ponen fin a la vía, inactividad y vía de hecho (art. 25) | **No**: actos que reproducen otros firmes y confirmatorios de consentidos (art. 28); **2 meses** (art. 46) |
| IV. Partes | Capacidad (art. 18), legitimación (art. 19), representación y defensa (art. 23) | **Derecho o interés legítimo**; Juzgado: **Abogado siempre** |

?> **Trampas frecuentes:** «el TSJ conoce de los recursos contra el TACRC» (es la **AN**); «los actos del Consejo de Ministros van a la Audiencia Nacional» (van al **TS**); «el plazo es de un mes» (son **dos**); «cualquier ciudadano está legitimado» (solo por **acción popular** prevista en la ley); «ante el Juzgado no hace falta Abogado» (hace falta **siempre**; lo potestativo es el **Procurador**).
""")

# =============================================================================
Q = [
 ("CE", "Artículo 106", "Funciones", "Según el artículo 106.1 de la Constitución, los Tribunales controlan:",
  ["La potestad reglamentaria y la legalidad de la actuación administrativa, así como el sometimiento de ésta a los fines que la justifican.", "La potestad legislativa y la legalidad de la actuación administrativa.", "La oportunidad política de la actuación administrativa.", "Únicamente la legalidad de los actos administrativos expresos."], "Art. 106.1 CE.", "Los Tribunales controlan la potestad reglamentaria y la legalidad de la actuación administrativa, así como el sometimiento de ésta a los fines que la justifican"),
 ("LJCA", "Artículo 1", "Funciones", "Según el artículo 1.1 de la LJCA, los Juzgados y Tribunales del orden contencioso-administrativo conocerán de las pretensiones que se deduzcan en relación con los Decretos legislativos:",
  ["Cuando excedan los límites de la delegación.", "En todo caso.", "Solo cuando así lo solicite el Gobierno.", "Cuando sean anteriores a la Constitución."], "Art. 1.1 LJCA.", "con los Decretos legislativos cuando excedan los límites de la delegación"),
 ("LJCA", "Artículo 1", "Funciones", "Según el artículo 1.3 de la LJCA, respecto de los órganos competentes del Congreso, del Senado, del Tribunal Constitucional, del Tribunal de Cuentas y del Defensor del Pueblo, la jurisdicción contencioso-administrativa conocerá de sus actos y disposiciones en materia de:",
  ["Personal, administración y gestión patrimonial sujetos al derecho público.", "Cualquier materia, sin excepción.", "Exclusivamente de personal.", "Funciones constitucionales que les son propias."], "Art. 1.3 a) LJCA.", "en materia de personal, administración y gestión patrimonial sujetos al derecho público"),
 ("LJCA", "Artículo 2", "Funciones", "Según el artículo 2 a) de la LJCA, en relación con los actos del Gobierno, el orden contencioso-administrativo conocerá de:",
  ["La protección jurisdiccional de los derechos fundamentales, los elementos reglados y la determinación de las indemnizaciones que fueran procedentes.", "Su oportunidad política y su conformidad con el programa de gobierno.", "Exclusivamente de la determinación de las indemnizaciones.", "Los actos de dirección política, sin limitación."], "Art. 2 a) LJCA.", "La protección jurisdiccional de los derechos fundamentales, los elementos reglados y la determinación de las indemnizaciones que fueran procedentes"),
 ("LJCA", "Artículo 3", "Funciones", "Según el artículo 3 de la LJCA, NO corresponden al orden jurisdiccional contencioso-administrativo:",
  ["Los conflictos de jurisdicción entre los Juzgados y Tribunales y la Administración pública.", "Los contratos administrativos.", "La responsabilidad patrimonial de las Administraciones públicas.", "Los actos de las Corporaciones de Derecho público adoptados en el ejercicio de funciones públicas."], "Art. 3 c) LJCA; las demás opciones están en el art. 2.", "Los conflictos de jurisdicción entre los Juzgados y Tribunales y la Administración pública"),
 ("LJCA", "Artículo 3", "Funciones", "Según el artículo 3 d) de la LJCA, los recursos contra las Normas Forales fiscales de las Juntas Generales de los Territorios Históricos de Álava, Guipúzcoa y Vizcaya corresponderán, en exclusiva:",
  ["Al Tribunal Constitucional.", "Al Tribunal Superior de Justicia del País Vasco.", "A la Sala de lo Contencioso-administrativo del Tribunal Supremo.", "A la Audiencia Nacional."], "Art. 3 d) LJCA.", "que corresponderán, en exclusiva, al Tribunal Constitucional"),
 ("LJCA", "Artículo 4", "Funciones", "Según el artículo 4.1 de la LJCA, la competencia del orden contencioso-administrativo se extiende a las cuestiones prejudiciales e incidentales no pertenecientes al orden administrativo, salvo las de carácter:",
  ["Constitucional y penal.", "Civil y social.", "Mercantil y laboral.", "Tributario y penal."], "Art. 4.1 LJCA.", "salvo las de carácter constitucional y penal"),
 ("LJCA", "Artículo 5", "Funciones", "Según el artículo 5 de la LJCA, la Jurisdicción Contencioso-administrativa es:",
  ["Improrrogable.", "Prorrogable por acuerdo de las partes.", "Prorrogable a instancia del Ministerio Fiscal.", "Prorrogable solo en primera instancia."], "Art. 5.1 LJCA.", "La Jurisdicción Contencioso-administrativa es improrrogable"),
 ("LJCA", "Artículo 6", "Órganos", "Según el artículo 6 de la LJCA, ¿cuál de los siguientes órganos NO integra el orden jurisdiccional contencioso-administrativo?",
  ["El Tribunal Constitucional.", "Los Juzgados Centrales de lo Contencioso-administrativo.", "La Sala de lo Contencioso-administrativo de la Audiencia Nacional.", "Las Salas de lo Contencioso-administrativo de los Tribunales Superiores de Justicia."], "Art. 6 LJCA.", "Sala de lo Contencioso-administrativo de la Audiencia Nacional"),
 ("LO1_2025", "da", "Órganos", "Según la disposición adicional primera de la Ley Orgánica 1/2025, las referencias realizadas en las leyes a los Juzgados de lo Contencioso-Administrativo se entenderán referidas a:",
  ["Las Secciones del orden jurisdiccional correspondiente de los Tribunales de Instancia.", "Las Salas de lo Contencioso-Administrativo de los Tribunales Superiores de Justicia.", "Las Oficinas de Justicia en los municipios.", "Los Juzgados Centrales de lo Contencioso-Administrativo."], "Disposición adicional primera de la LO 1/2025.", "se entenderán referidas a las Secciones del orden jurisdiccional correspondiente de los Tribunales de Instancia"),
 ("LJCA", "Artículo 7", "Órganos", "Según el artículo 7.3 de la LJCA, la declaración de incompetencia adoptará la forma de:",
  ["Auto, y deberá efectuarse antes de la sentencia.", "Sentencia.", "Providencia, en cualquier momento del proceso.", "Diligencia de ordenación."], "Art. 7.3 LJCA.", "La declaración de incompetencia adoptará la forma de auto y deberá efectuarse antes de la sentencia"),
 ("LJCA", "Artículo 8", "Competencias", "Según el artículo 8.2 de la LJCA, los Juzgados de lo Contencioso-administrativo conocerán de los recursos contra actos de la Administración de las Comunidades Autónomas sobre sanciones que consistan en multas no superiores a:",
  ["60.000 euros.", "30.050 euros.", "100.000 euros.", "6.000 euros."], "Art. 8.2 b) LJCA.", "multas no superiores a 60.000 euros"),
 ("LJCA", "Artículo 8", "Competencias", "Según el artículo 8.2 de la LJCA, los Juzgados de lo Contencioso-administrativo conocerán de las reclamaciones por responsabilidad patrimonial frente a las Comunidades Autónomas cuya cuantía no exceda de:",
  ["30.050 euros.", "60.000 euros.", "50.000 euros.", "18.030 euros."], "Art. 8.2 c) LJCA.", "Las reclamaciones por responsabilidad patrimonial cuya cuantía no exceda de 30.050 euros"),
 ("LJCA", "Artículo 8", "Competencias", "Según el artículo 8.1 de la LJCA, de los recursos frente a los actos de las entidades locales conocerán los Juzgados de lo Contencioso-administrativo, excluidas las impugnaciones de:",
  ["Cualquier clase de instrumentos de planeamiento urbanístico.", "Las sanciones de tráfico.", "Los actos en materia de personal.", "Las licencias de obras."], "Art. 8.1 LJCA.", "excluidas las impugnaciones de cualquier clase de instrumentos de planeamiento urbanístico"),
 ("LJCA", "Artículo 9", "Competencias", "Según el artículo 9.1 e) de la LJCA, los Juzgados Centrales de lo Contencioso-administrativo conocerán, en primera instancia, de las resoluciones que acuerden:",
  ["La inadmisión de las peticiones de asilo político.", "La expulsión de extranjeros por la Administración periférica.", "La concesión de la nacionalidad por residencia.", "La denegación de visados."], "Art. 9.1 e) LJCA.", "las resoluciones que acuerden la inadmisión de las peticiones de asilo político"),
 ("LJCA", "Artículo 10", "Competencias", "Según el artículo 10.1 de la LJCA, las Salas de lo Contencioso-Administrativo de los Tribunales Superiores de Justicia conocerán en única instancia de las resoluciones dictadas por el Tribunal Económico-Administrativo Central en materia de:",
  ["Tributos cedidos.", "Tributos estatales no cedidos.", "Aduanas.", "Impuestos especiales."], "Art. 10.1 e) LJCA.", "Las resoluciones dictadas por el Tribunal Económico-Administrativo Central en materia de tributos cedidos"),
 ("LJCA", "Artículo 10", "Competencias", "Según el artículo 10.2 de la LJCA, las Salas de lo Contencioso-Administrativo de los Tribunales Superiores de Justicia conocerán, en segunda instancia, de las apelaciones promovidas contra sentencias y autos dictados por:",
  ["Los Juzgados de lo Contencioso-administrativo.", "Los Juzgados Centrales de lo Contencioso-administrativo.", "La Sala de lo Contencioso-administrativo de la Audiencia Nacional.", "Los Tribunales Económico-Administrativos Regionales."], "Art. 10.2 LJCA (las de los Juzgados Centrales van a la AN, art. 11.2).", "en segunda instancia, de las apelaciones promovidas contra sentencias y autos dictados por los Juzgados de lo Contencioso-administrativo"),
 ("LJCA", "Artículo 11", "Competencias", "Según el artículo 11.1 de la LJCA, la Sala de lo Contencioso-administrativo de la Audiencia Nacional conocerá en única instancia de los recursos en relación con las disposiciones generales y los actos de:",
  ["Los Ministros y de los Secretarios de Estado.", "El Consejo de Ministros.", "Las Comisiones Delegadas del Gobierno.", "Los Delegados del Gobierno en las Comunidades Autónomas."], "Art. 11.1 a) LJCA (Consejo de Ministros y Comisiones Delegadas: TS, art. 12.1 a).", "las disposiciones generales y los actos de los Ministros"),
 ("LJCA", "Artículo 12", "Competencias", "Según el artículo 12.1 de la LJCA, la Sala de lo Contencioso-administrativo del Tribunal Supremo conocerá en única instancia de los recursos en relación con los actos y disposiciones de:",
  ["El Consejo de Ministros y de las Comisiones Delegadas del Gobierno.", "Los Ministros.", "Los Secretarios de Estado.", "El Tribunal Económico-Administrativo Central."], "Art. 12.1 a) LJCA.", "Los actos y disposiciones del Consejo de Ministros y de las Comisiones Delegadas del Gobierno"),
 ("LJCA", "Artículo 12", "Competencias", "Según el artículo 12.1 de la LJCA, de los recursos contra los actos y disposiciones del Consejo General del Poder Judicial conocerá:",
  ["La Sala de lo Contencioso-administrativo del Tribunal Supremo.", "La Sala de lo Contencioso-administrativo de la Audiencia Nacional.", "El Tribunal Constitucional.", "Los Juzgados Centrales de lo Contencioso-administrativo."], "Art. 12.1 b) LJCA.", "Los actos y disposiciones del Consejo General del Poder Judicial y del Fiscal General del Estado"),
 ("LJCA", "Artículo 13", "Competencias", "Según el artículo 13 c) de la LJCA, salvo disposición expresa en contrario, la atribución de competencia por razón de la materia:",
  ["Prevalece sobre la efectuada en razón del órgano administrativo autor del acto.", "Cede ante la efectuada en razón del órgano administrativo autor del acto.", "Se aplica solo en defecto de regla territorial.", "Se aplica solo a los Juzgados Centrales."], "Art. 13 c) LJCA.", "la atribución de competencia por razón de la materia prevalece sobre la efectuada en razón del órgano administrativo autor del acto"),
 ("LJCA", "Artículo 14", "Competencias", "Según el artículo 14.1 de la LJCA, cuando se impugnen planes de ordenación urbana y actuaciones expropiatorias, la competencia territorial corresponderá al órgano jurisdiccional en cuya circunscripción:",
  ["Radiquen los inmuebles afectados.", "Tenga su domicilio el demandante.", "Tenga su sede el órgano que dictó el acto, en todo caso.", "Elija libremente el demandante."], "Art. 14.1, regla tercera, LJCA.", "en cuya circunscripción radiquen los inmuebles afectados"),
 ("LJCA", "Artículo 25", "Actividad impugnable", "Según el artículo 25.1 de la LJCA, el recurso contencioso-administrativo es admisible en relación con los actos de la Administración que:",
  ["Pongan fin a la vía administrativa, ya sean definitivos o de trámite cualificados.", "Sean definitivos, aunque no pongan fin a la vía administrativa.", "Sean de trámite, en todo caso.", "Hayan sido recurridos previamente en reposición, en todo caso."], "Art. 25.1 LJCA.", "que pongan fin a la vía administrativa, ya sean definitivos o de trámite"),
 ("LJCA", "Artículo 27", "Actividad impugnable", "Según el artículo 27.1 de la LJCA, cuando un Juez o Tribunal de lo Contencioso-administrativo hubiere dictado sentencia firme estimatoria por considerar ilegal el contenido de la disposición general aplicada, deberá:",
  ["Plantear la cuestión de ilegalidad ante el Tribunal competente para conocer del recurso directo contra la disposición.", "Plantear la cuestión de inconstitucionalidad ante el Tribunal Constitucional.", "Anular directamente la disposición general en todo caso.", "Comunicarlo al Consejo de Estado."], "Art. 27.1 LJCA.", "deberá plantear la cuestión de ilegalidad ante el Tribunal competente para conocer del recurso directo contra la disposición"),
 ("LJCA", "Artículo 29", "Actividad impugnable", "Según el artículo 29.1 de la LJCA, si la Administración no da cumplimiento a la prestación reclamada ni llega a un acuerdo con los interesados, estos podrán deducir recurso contencioso-administrativo contra la inactividad transcurrido, desde la fecha de la reclamación, el plazo de:",
  ["Tres meses.", "Un mes.", "Seis meses.", "Dos meses."], "Art. 29.1 LJCA.", "Si en el plazo de tres meses desde la fecha de la reclamación"),
 ("LJCA", "Artículo 29", "Actividad impugnable", "Según el artículo 29.2 de la LJCA, cuando la Administración no ejecute sus actos firmes, el recurso que formulen los afectados se tramitará por:",
  ["El procedimiento abreviado regulado en el artículo 78.", "El procedimiento ordinario.", "El procedimiento para la protección de los derechos fundamentales.", "La cuestión de ilegalidad."], "Art. 29.2 LJCA (tras un mes desde la petición de ejecución).", "que se tramitará por el procedimiento abreviado regulado en el artículo 78"),
 ("LJCA", "Artículo 30", "Actividad impugnable", "Según el artículo 30 de la LJCA, en caso de vía de hecho, si el requerimiento de cesación no fuere atendido, podrá deducirse directamente recurso contencioso-administrativo una vez transcurridos desde su presentación:",
  ["Diez días.", "Un mes.", "Veinte días.", "Tres meses."], "Art. 30 LJCA.", "dentro de los diez días siguientes a la presentación del requerimiento"),
 ("LJCA", "Artículo 45", "Actividad impugnable", "Según el artículo 45.4 de la LJCA, el recurso de lesividad se iniciará:",
  ["Por demanda.", "Por escrito de interposición.", "Por requerimiento previo.", "Por declaración del Consejo de Estado."], "Art. 45.4 LJCA.", "El recurso de lesividad se iniciará por demanda"),
 ("LJCA", "Artículo 46", "Actividad impugnable", "Según el artículo 46.3 de la LJCA, si no hubiere requerimiento previo, el plazo para interponer recurso contra una actuación en vía de hecho será de:",
  ["Veinte días desde el día en que se inició la actuación administrativa en vía de hecho.", "Diez días desde el día en que se inició la actuación.", "Dos meses desde el día en que se inició la actuación.", "Un mes desde que el interesado tuvo conocimiento de la actuación."], "Art. 46.3 LJCA.", "Si no hubiere requerimiento, el plazo será de veinte días desde el día en que se inició la actuación administrativa en vía de hecho"),
 ("LJCA", "Artículo 46", "Actividad impugnable", "Según el artículo 46.5 de la LJCA, el plazo para interponer recurso de lesividad será de dos meses a contar desde:",
  ["El día siguiente a la fecha de la declaración de lesividad.", "La fecha del acto declarado lesivo.", "La notificación del acto al interesado.", "El dictamen del Consejo de Estado."], "Art. 46.5 LJCA.", "a contar desde el día siguiente a la fecha de la declaración de lesividad"),
 ("LJCA", "Artículo 18", "Partes", "Según el artículo 18 de la LJCA, los grupos de afectados, uniones sin personalidad o patrimonios independientes o autónomos tendrán capacidad procesal ante el orden contencioso-administrativo:",
  ["Cuando la Ley así lo declare expresamente.", "En todo caso.", "Nunca.", "Solo si están inscritos en un registro público."], "Art. 18 LJCA.", "cuando la Ley así lo declare expresamente"),
 ("LJCA", "Artículo 19", "Partes", "Según el artículo 19.1 h) de la LJCA, cualquier ciudadano está legitimado, en ejercicio de la acción popular:",
  ["En los casos expresamente previstos por las Leyes.", "En todo caso.", "Cuando se trate de actos de las entidades locales.", "Cuando lo autorice el Ministerio Fiscal."], "Art. 19.1 h) LJCA.", "en ejercicio de la acción popular, en los casos expresamente previstos por las Leyes"),
 ("LJCA", "Artículo 19", "Partes", "Según el artículo 19.2 de la LJCA, la Administración autora de un acto está legitimada para impugnarlo ante el orden contencioso-administrativo:",
  ["Previa su declaración de lesividad para el interés público.", "Previa revisión de oficio.", "Sin necesidad de requisito previo alguno.", "Previa autorización del Consejo de Ministros."], "Art. 19.2 LJCA.", "previa su declaración de lesividad para el interés público"),
 ("LJCA", "Artículo 20", "Partes", "Según el artículo 20 de la LJCA, los miembros de los órganos colegiados de una Administración pública no pueden interponer recurso contencioso-administrativo contra la actividad de esa Administración:",
  ["Salvo que una Ley lo autorice expresamente.", "En ningún caso.", "Salvo que hayan votado en contra del acuerdo.", "Salvo que lo autorice el presidente del órgano."], "Art. 20 a) LJCA.", "salvo que una Ley lo autorice expresamente"),
 ("LJCA", "Artículo 21", "Partes", "Según el artículo 21.1 c) de la LJCA, las aseguradoras de las Administraciones públicas:",
  ["Siempre serán parte codemandada junto con la Administración a quien aseguren.", "Nunca podrán ser parte en el proceso contencioso-administrativo.", "Serán parte codemandada solo si lo solicita el demandante.", "Serán demandadas ante el orden civil."], "Art. 21.1 c) LJCA.", "que siempre serán parte codemandada junto con la Administración a quien aseguren"),
 ("LJCA", "Artículo 23", "Partes", "Según el artículo 23.1 de la LJCA, en sus actuaciones ante órganos unipersonales, las partes:",
  ["Podrán conferir su representación a un Procurador y serán asistidas, en todo caso, por Abogado.", "Deberán conferir su representación a un Procurador y ser asistidas por Abogado.", "Podrán comparecer por sí mismas, sin Procurador ni Abogado.", "Serán representadas por el Ministerio Fiscal."], "Art. 23.1 LJCA (ante órganos colegiados, Procurador y Abogado obligatorios: 23.2).", "las partes podrán conferir su representación a un Procurador y serán asistidas, en todo caso, por Abogado"),
 ("LJCA", "Artículo 23", "Partes", "Según el artículo 23.3 de la LJCA, los funcionarios públicos podrán comparecer por sí mismos en defensa de sus derechos estatutarios cuando se refieran a cuestiones de personal:",
  ["Que no impliquen separación de empleados públicos inamovibles.", "De cualquier clase, sin excepción.", "Que impliquen separación del servicio.", "Solo ante órganos colegiados."], "Art. 23.3 LJCA.", "que no impliquen separación de empleados públicos inamovibles"),
]
for k, art, cat, enun, ops, expl, frag in Q: T.q(k, art, cat, enun, ops, expl, frag)
for cod, n, *_ in EX:
    if (cod, n) != ("X", 65): T.real(cod, n, "Preguntas oficiales")

for q_, a_, cat in [
  ("Tres objetos del control del art. 106.1 CE", "Potestad reglamentaria; legalidad de la actuación administrativa; sometimiento a los fines que la justifican.", "Funciones"),
  ("Objeto de la jurisdicción (art. 1.1 LJCA)", "Actuación de las AAPP sujeta al Derecho Administrativo; disposiciones generales de rango inferior a la ley; decretos legislativos que excedan la delegación.", "Funciones"),
  ("Actos del Gobierno (art. 2 a)", "Derechos fundamentales, elementos reglados e indemnizaciones.", "Funciones"),
  ("Excluidos (art. 3)", "Lo atribuido a los órdenes civil, penal y social; contencioso-disciplinario militar; conflictos de jurisdicción y de atribuciones; Normas Forales fiscales (TC).", "Funciones"),
  ("Cuestiones prejudiciales (art. 4)", "Las conoce, salvo las constitucionales y penales; sin efectos fuera del proceso.", "Funciones"),
  ("Órganos del orden contencioso (art. 6)", "Juzgados, Juzgados Centrales, Salas de los TSJ, de la AN y del TS.", "Órganos"),
  ("Juzgados tras la LO 1/2025", "Secciones de lo Contencioso-Administrativo de los Tribunales de Instancia (Centrales: del Tribunal Central de Instancia).", "Órganos"),
  ("Cuantías de los Juzgados (art. 8)", "Multas hasta 60.000 €; responsabilidad patrimonial hasta 30.050 €; periférica del Estado: actos de hasta 60.000 €.", "Competencias"),
  ("Reglamentos autonómicos y locales", "TSJ en única instancia (art. 10.1 b).", "Competencias"),
  ("Ministros y Secretarios de Estado", "Audiencia Nacional en única instancia (art. 11.1 a); personal y responsabilidad hasta 30.050 €: Juzgados Centrales (art. 9).", "Competencias"),
  ("Consejo de Ministros, CGPJ y Fiscal General", "Tribunal Supremo en única instancia (art. 12.1).", "Competencias"),
  ("TACRC y tribunales territoriales de recursos contractuales", "TACRC: Audiencia Nacional (11.1 f); territoriales: TSJ (10.1 l).", "Competencias"),
  ("Actividad impugnable (art. 25)", "Disposiciones generales; actos expresos y presuntos que ponen fin a la vía (definitivos o de trámite cualificados); inactividad; vía de hecho.", "Actividad impugnable"),
  ("Actos no impugnables (art. 28)", "Reproducción de actos definitivos y firmes; confirmatorios de actos consentidos.", "Actividad impugnable"),
  ("Plazos del art. 46", "2 meses (expreso, lesividad, entre AAPP); 6 meses (no expreso, según el texto); vía de hecho 10 días o 20 sin requerimiento.", "Actividad impugnable"),
  ("Legitimación activa general (art. 19.1 a)", "Personas físicas o jurídicas con derecho o interés legítimo.", "Partes"),
  ("Lesividad (art. 19.2)", "La Administración autora impugna su acto previa declaración de lesividad para el interés público.", "Partes"),
  ("Procurador y Abogado (art. 23)", "Unipersonales: Procurador potestativo, Abogado siempre; colegiados: ambos obligatorios.", "Partes"),
]: T.fc(q_, a_, cat)

T.glos("Jurisdicción improrrogable", "La que no puede extenderse a asuntos de otro orden ni por voluntad de las partes; se aprecia de oficio (LJCA, art. 5).", "s3", "Funciones")
T.glos("Tribunal de Instancia", f"Órgano judicial en que se integran, como Secciones, los antiguos Juzgados (LO 1/2025, disposiciones adicional primera y transitoria primera). Según el preámbulo de la LO 1/2025, {c('LO1_2025', 'pr', 'se configuran como órganos judiciales colegiados, desde el punto de vista organizativo')}.", "s4", "Órganos")
T.glos("Actividad administrativa impugnable", "Disposiciones generales, actos que ponen fin a la vía administrativa, inactividad y vía de hecho (LJCA, art. 25).", "s9", "Actividad impugnable")
T.glos("Acto de trámite cualificado", "El de trámite que decide directa o indirectamente el fondo, impide continuar el procedimiento o produce indefensión o perjuicio irreparable; es recurrible (LJCA, art. 25.1). Expresión doctrinal.", "s9", "Actividad impugnable")
T.glos("Recurso indirecto", "Impugnación de un acto de aplicación fundada en que la disposición general no es conforme a Derecho (LJCA, art. 26). Expresión doctrinal.", "s9", "Actividad impugnable")
T.glos("Cuestión de ilegalidad", "La que plantea el juez que estimó un recurso indirecto ante el tribunal competente para el recurso directo contra la disposición (LJCA, art. 27).", "s9", "Actividad impugnable")
T.glos("Inactividad", "Incumplimiento de una prestación concreta debida o falta de ejecución de actos firmes (LJCA, art. 29).", "s10", "Actividad impugnable")
T.glos("Vía de hecho", "Actuación material de la Administración sin cobertura; recurrible con o sin requerimiento previo (LJCA, arts. 25.2 y 30).", "s10", "Actividad impugnable")
T.glos("Declaración de lesividad", "Requisito previo para que la Administración autora impugne su propio acto ante esta jurisdicción (LJCA, art. 19.2); el recurso se inicia por demanda (art. 45.4).", "s13", "Partes")
T.glos("Acción popular", "Legitimación de cualquier ciudadano, solo en los casos previstos expresamente por las leyes (LJCA, art. 19.1 h).", "s13", "Partes")

T.hito("1978", "Constitución Española, arts. 106.1 y 153 c)", "Control judicial de la potestad reglamentaria y de la actuación administrativa", "normativo", "s1")
T.hito("1998", "Ley 29/1998, de 13 de julio, reguladora de la Jurisdicción Contencioso-administrativa (BOE de 14-7-1998)", "Entró en vigor a los cinco meses de su publicación (disposición final tercera)", "normativo", "s2")
T.hito("2014", "STC 52/2014, de 10 de abril (BOE de 7-5-2014)", "El plazo de seis meses del art. 46.1 no se aplica a la desestimación por silencio", "jurisprudencia", "s11")
T.hito("2025", "Ley Orgánica 1/2025, de 2 de enero (BOE de 3-1-2025)", "Tribunales de Instancia: los Juzgados de lo Contencioso pasan a Secciones; transformación de los restantes Juzgados el 31-12-2025", "normativo", "s4")

T.publicar()
