# -*- coding: utf-8 -*-
"""Tema III.8 (B3T08): La protección de datos personales y su régimen jurídico: principios,
derechos, responsable y encargado del tratamiento, delegado y autoridades de protección de
datos. Derechos digitales.
Método del I.2. Normas: CE, art. 18.4 (BOE); Reglamento (UE) 2016/679, RGPD (EUR-Lex, DOUE);
Ley Orgánica 3/2018, de Protección de Datos Personales y garantía de los derechos digitales
(BOE); Real Decreto 389/2021, Estatuto de la AEPD, art. 6 (BOE)."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *

CORTO["LOPD"] = "LO 3/2018"
CORTO["RD389"] = "RD 389/2021, Estatuto de la AEPD"

# Rúbricas oficiales de los artículos del RGPD (EUR-Lex: campo «sti» del texto extraído)
STI = {a["art"]: a["sti"] for a in json.load(open(os.path.join(boe.AQUI, "RGPD.json"), encoding="utf-8"))}

def R(n, resaltar=(), solo=None):
    """Bloque literal de un artículo del RGPD, con su rúbrica oficial."""
    a = f"Artículo {n}"
    return lit("RGPD", a, resaltar, solo, titulo=f"{a} (RGPD). {STI[a]}" + (" (fragmento)" if solo else ""))

def L(n, resaltar=(), solo=None):
    """Bloque literal de un artículo de la LO 3/2018."""
    a = f"Artículo {n}"
    cab = parrafos("LOPD", a)[0].rstrip(".")
    return lit("LOPD", a, resaltar, solo, titulo=f"{cab} (LO 3/2018)" + (" (fragmento)" if solo else ""))

def cR(n, frag): return c("RGPD", f"Artículo {n}", frag)
def cL(n, frag): return c("LOPD", f"Artículo {n}", frag)

ESQ = "*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*"

T = Tema("B3T08",
  "Seis preguntas: I. Qué se protege y con qué normas (art. 18.4 CE; RGPD, arts. 1, 2 y 4; LO 3/2018, arts. 1 y 2) · II. Con qué principios se tratan los datos (RGPD, arts. 5 a 9; LO 3/2018, arts. 4 a 9) · III. Qué derechos tiene el interesado (RGPD, arts. 12 a 22, 77, 78 y 82; LO 3/2018, arts. 11 a 18) · IV. Quién responde del tratamiento: responsable y encargado (RGPD, arts. 24 a 35; LO 3/2018, arts. 28 a 33) · V. Quién vigila: delegado y autoridades (RGPD, arts. 37 a 39, 51, 52 y 68; LO 3/2018, arts. 34 a 37, 44, 47, 48, 55 y 57; RD 389/2021, art. 6) · VI. Qué derechos digitales reconoce la ley (LO 3/2018, arts. 79 a 97). Cada artículo: texto literal (BOE o DOUE) y ficha.",
  ["Art. 18.4 CE", "RGPD", "LO 3/2018", "Principios", "Responsabilidad proactiva", "Consentimiento", "Catorce años", "Categorías especiales", "Derechos ARSOPL", "Portabilidad", "Responsable", "Encargado", "Violación de seguridad: 72 horas", "Delegado de protección de datos", "Diez días", "AEPD", "Circulares", "Derechos digitales", "Desconexión digital", "Derecho al olvido"])

# =============================================================================
T.ap("s0", "Mapa del tema: seis preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque III, tema 8):
> La protección de datos personales y su régimen jurídico: principios, derechos, responsable y encargado del tratamiento, delegado y autoridades de protección de datos. Derechos digitales.

### El hilo conductor

El epígrafe se lee como **seis preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Reglamento (UE) 2016/679 (RGPD) | Otras normas |
|---|---|---|---|
| **I** | ¿Qué se protege y con qué normas? (régimen jurídico) | Arts. 1, 2 y 4 | CE, art. 18.4; LO 3/2018, arts. 1 y 2 |
| **II** | ¿Con qué principios se tratan los datos? | Arts. 5 a 9 | LO 3/2018, arts. 4 a 9 |
| **III** | ¿Qué derechos tiene el interesado? | Arts. 12 a 18, 20 a 22, 77, 78 y 82 | LO 3/2018, arts. 11 a 18 |
| **IV** | ¿Quién responde del tratamiento? (responsable y encargado) | Arts. 24 a 26, 28, 30 y 32 a 35 | LO 3/2018, arts. 28, 29 y 31 a 33 |
| **V** | ¿Quién vigila? (delegado y autoridades de protección de datos) | Arts. 37 a 39, 51, 52 y 68 | LO 3/2018, arts. 34 a 37, 44, 47, 48, 55 y 57; RD 389/2021, art. 6 |
| **VI** | ¿Qué derechos digitales reconoce la ley? | — | LO 3/2018, título X (arts. 79 a 97) |

{ESQ}

!> **La idea que une los seis bloques:** la Constitución manda a la ley **limitar el uso de la informática** (art. 18.4). Hoy esa protección la da sobre todo un **reglamento europeo directamente aplicable** (RGPD), que la LO 3/2018 **adapta y completa** (I). Todo tratamiento tiene que respetar unos **principios** y apoyarse en una **base de licitud** (II); el interesado tiene **derechos** frente al tratamiento (III); el **responsable** decide y responde, y el **encargado** trata por su cuenta (IV); el **delegado** supervisa dentro de la organización y las **autoridades de control** (en España, la **AEPD** y las autonómicas) desde fuera (V). La LO 3/2018 añade, además, los **derechos digitales** (VI).

### Cómo está escrito

- Cada artículo: primero el **texto literal** y debajo su **ficha**. El RGPD se cita de **EUR-Lex** (etiqueta **DOUE**); la CE, la LO 3/2018 y el RD 389/2021, del **BOE**.
- Ficha de **derecho** (Titulares · Contenido · Límites · Protección · ⚠ Ojo) o de **institución o procedimiento** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo).
- El RGPD habla de «**interesado**» y la LO 3/2018, de «**afectado**»: es la misma persona.
- Los esquemas y cuadros **no son texto legal**: resumen los artículos citados.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué se protege y con qué normas? (art. 18.4 CE; RGPD, arts. 1, 2 y 4; LO 3/2018, arts. 1 y 2)", donde(
  "Primera pregunta del tema: el **fundamento** del derecho a la protección de datos y las **normas** que lo regulan (régimen jurídico), con su ámbito y sus conceptos básicos.",
  ["1 Fundamento y objeto (art. 18.4 CE; RGPD, art. 1; LO 3/2018, art. 1)", "2 Ámbito de aplicación y definiciones (RGPD, arts. 2 y 4; LO 3/2018, art. 2)"]))

T.ap("s1", "I.1 Fundamento y objeto (art. 18.4 CE; RGPD, art. 1; LO 3/2018, art. 1)", f"""
{unidad("1.1 El mandato constitucional (art. 18.4 CE)",
  lit("CE", "Artículo 18", ["La ley limitará el uso de la informática"], solo=[4]),
  ficha("Los **ciudadanos**",
        "La ley debe **limitar el uso de la informática** para garantizar el **honor**, la **intimidad personal y familiar** y el **pleno ejercicio de sus derechos**",
        "—",
        f"La LO 3/2018 lo califica de {cL(1, 'derecho fundamental de las personas físicas a la protección de datos personales')} amparado por el art. 18.4 (→ I.1.3)",
        "El art. 18.4 no dice «protección de datos»: dice «**limitará el uso de la informática**». Es la base que invoca la LO 3/2018 tanto para la protección de datos como para los **derechos digitales**."))}

{unidad("1.2 Objeto del Reglamento general de protección de datos (RGPD, art. 1)",
  R(1, ["su derecho a la protección de los datos personales", "no podrá ser restringida ni prohibida"]),
  fichab("Objeto del RGPD: dos finalidades",
         "Las **personas físicas** (no las jurídicas)",
         ["Proteger a las personas físicas en el **tratamiento** de sus datos personales (1.1 y 2)", "Garantizar la **libre circulación** de los datos en la Unión (1.1 y 3)"],
         "—",
         "La protección de datos **no** puede servir de motivo para **restringir ni prohibir** la libre circulación de datos **en la Unión** (1.3)."))}

{unidad("1.3 Objeto de la LO 3/2018 (art. 1)",
  L(1, ["Adaptar el ordenamiento jurídico español al Reglamento (UE) 2016/679", "y completar sus disposiciones", "se ejercerá con arreglo a lo establecido en el Reglamento (UE) 2016/679 y en esta ley orgánica", "Garantizar los derechos digitales de la ciudadanía"]),
  fichab("Para qué sirve la ley orgánica",
         "—",
         ["**Adaptar** el ordenamiento español al RGPD y **completar** sus disposiciones (a)", "El derecho fundamental del art. 18.4 CE se ejerce con arreglo al **RGPD** y a **esta ley orgánica** (a, párrafo segundo)", "**Garantizar los derechos digitales** de la ciudadanía (b; → VI.1)"],
         "—",
         "La LO 3/2018 **no sustituye** al RGPD: lo **adapta y completa**. Tiene **dos** objetos: protección de datos y **derechos digitales**."))}
""", 2)

T.ap("s2", "I.2 Ámbito de aplicación y definiciones (RGPD, arts. 2 y 4; LO 3/2018, art. 2)", f"""
{unidad("2.1 Ámbito material del RGPD (art. 2)",
  R(2, ["total o parcialmente automatizado", "contenidos o destinados a ser incluidos en un fichero", "exclusivamente personales o domésticas"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("A qué tratamientos se aplica",
         "—",
         ["**Sí**: tratamiento **total o parcialmente automatizado**, y el **no automatizado** de datos contenidos o destinados a un **fichero** (2.1)", "**No**: actividades fuera del Derecho de la Unión; actividades de los Estados del capítulo 2 del título V del TUE; actividades **exclusivamente personales o domésticas**; autoridades competentes en materia **penal** (2.2)"],
         "—",
         "El tratamiento **manual** también entra si los datos están (o van a estar) en un **fichero**. Lo **doméstico** queda fuera."))}

{unidad("2.2 Conceptos básicos (RGPD, art. 4)",
  R(4, ["persona física identificada o identificable", "«responsable del tratamiento»", "determine los fines y medios del tratamiento", "«encargado del tratamiento»", "por cuenta del responsable del tratamiento", "libre, específica, informada e inequívoca", "«violación de la seguridad de los datos personales»"], solo=[1, 2, 3, 8, 9, 10, 12, 13]),
  fichab("Las definiciones que más se preguntan",
         "—",
         ["**Dato personal**: información sobre una persona física **identificada o identificable** (el «interesado») (4.1)", "**Tratamiento**: cualquier operación, automatizada **o no** (4.2)", "**Responsable**: quien determina **los fines y medios** (4.7; → IV.1)", "**Encargado**: quien trata **por cuenta del responsable** (4.8; → IV.2)", "**Consentimiento**: voluntad **libre, específica, informada e inequívoca** (4.11; → II.2)", "**Violación de la seguridad**: destrucción, pérdida, alteración o acceso no autorizado (4.12; → IV.3.4)"],
         "—",
         "Responsable = **decide** fines y medios; encargado = trata **por cuenta** de otro. Las cuatro notas del consentimiento: **libre, específica, informada e inequívoca**."))}

{unidad("2.3 Ámbito de la LO 3/2018 (art. 2)",
  L(2, ["A los tratamientos de datos de personas fallecidas", "A los tratamientos sometidos a la normativa sobre protección de materias clasificadas", "se regirán por lo dispuesto en su legislación específica si la hubiere y supletoriamente"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("A qué se aplica la ley orgánica",
         "—",
         ["Mismo criterio que el RGPD: tratamiento total o parcialmente **automatizado** y el **no automatizado** en fichero (2.1)", "**No** se aplica: tratamientos excluidos por el art. 2.2 RGPD; datos de **personas fallecidas** (salvo el art. 3); **materias clasificadas** (2.2)", "Actividades ajenas al Derecho de la UE (régimen **electoral**, instituciones **penitenciarias**, **Registro Civil** y Registros de la Propiedad y Mercantiles): su legislación **específica** y, **supletoriamente**, el RGPD y esta ley (2.3)"],
         "—",
         "Fallecidos y materias **clasificadas**: **fuera** de la LO 3/2018. Electoral, penitenciario y registros: legislación **específica** + RGPD y LO **supletorios**. El art. 2 delimita el ámbito de los **títulos I a IX** y de los **arts. 89 a 94**."))}

{resumen([
  "Art. 18.4 CE: la ley **limitará el uso de la informática** para garantizar el honor, la intimidad y el pleno ejercicio de los derechos.",
  "El **RGPD** protege a las **personas físicas** y garantiza la **libre circulación** de datos en la Unión; la **LO 3/2018** lo **adapta y completa** y garantiza los **derechos digitales**.",
  "Ámbito: tratamiento **automatizado** o **no automatizado en fichero**; fuera, lo **doméstico**, lo **penal**, los **fallecidos** y las **materias clasificadas**.",
  "**Responsable**: determina **fines y medios**; **encargado**: trata **por cuenta** del responsable."],
  "Siguiente: II. ¿Con qué principios se tratan los datos?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Con qué principios se tratan los datos? (RGPD, arts. 5 a 9; LO 3/2018, arts. 4 a 9)", donde(
  "Segunda pregunta. Todo tratamiento debe respetar los **principios** del art. 5 RGPD y apoyarse en una **base de licitud** (art. 6). El **consentimiento** tiene requisitos propios, y las **categorías especiales** de datos están, en principio, **prohibidas**.",
  ["1 Principios del tratamiento (RGPD, art. 5; LO 3/2018, arts. 4 y 5)", "2 Licitud y consentimiento (RGPD, arts. 6 a 8; LO 3/2018, arts. 6 a 8)", "3 Categorías especiales de datos (RGPD, art. 9; LO 3/2018, art. 9)"]))

T.ap("s3", "II.1 Principios del tratamiento (RGPD, art. 5; LO 3/2018, arts. 4 y 5)", f"""
{unidad("1.1 Los principios (RGPD, art. 5)",
  R(5, ["(«licitud, lealtad y transparencia»)", "(«limitación de la finalidad»)", "(«minimización de datos»)", "(«exactitud»)", "(«limitación del plazo de conservación»)", "(«integridad y confidencialidad»)", "(«responsabilidad proactiva»)"]),
  fichab("Siete principios con nombre propio",
         "El **responsable** del tratamiento: cumple y debe poder **demostrarlo** (5.2)",
         ["**Licitud, lealtad y transparencia** (a)", "**Limitación de la finalidad**: fines determinados, explícitos y legítimos (b)", "**Minimización**: adecuados, pertinentes y limitados a lo necesario (c)", "**Exactitud** (d)", "**Limitación del plazo de conservación** (e)", "**Integridad y confidencialidad** (f)", "**Responsabilidad proactiva** (5.2)"],
         "Conservación: no más tiempo **del necesario**; más tiempo solo con fines de **archivo en interés público**, **investigación** o **estadística** (e)",
         "Cada principio lleva su **nombre entre comillas** en el texto: es lo que pregunta el examen. «Adecuados, pertinentes y limitados» = **minimización** (no limitación de la finalidad). «Capaz de demostrarlo» = **responsabilidad proactiva**."))}

{unidad("1.2 Exactitud de los datos (LO 3/2018, art. 4)",
  L(4, ["no será imputable al responsable del tratamiento", "directamente del afectado", "de un registro público"]),
  fichab("Cuándo la inexactitud no es imputable al responsable",
         "El **responsable**, si ha adoptado **todas las medidas razonables** para suprimir o rectificar sin dilación",
         ["Datos obtenidos **directamente del afectado** (a)", "De un **mediador o intermediario** previsto en la normativa del sector, que asume la responsabilidad (b)", "Recibidos de otro responsable por **portabilidad** (c)", "Obtenidos de un **registro público** (d)"],
         "—",
         "Son **cuatro** supuestos tasados, y siempre que el responsable haya adoptado las medidas **razonables**."))}

{unidad("1.3 Deber de confidencialidad (LO 3/2018, art. 5)",
  L(5, ["todas las personas que intervengan en cualquier fase de este", "complementaria de los deberes de secreto profesional", "aun cuando hubiese finalizado la relación"]),
  fichab("Confidencialidad",
         "**Responsables**, **encargados** y **todas las personas** que intervengan en cualquier fase del tratamiento",
         ["Deber de confidencialidad del art. 5.1 f) RGPD (5.1)", "Es **complementario** del secreto profesional (5.2)"],
         "Se mantiene **aun cuando haya finalizado** la relación con el responsable o encargado (5.3)",
         "El deber **sobrevive** al fin de la relación laboral o de servicios."))}
""", 2)

T.ap("s4", "II.2 Licitud y consentimiento (RGPD, arts. 6 a 8; LO 3/2018, arts. 6 a 8)", f"""
{unidad("2.1 Bases de licitud (RGPD, art. 6.1)",
  R(6, ["al menos una de las siguientes condiciones", "no será de aplicación al tratamiento realizado por las autoridades públicas en el ejercicio de sus funciones"], solo=[1, 2, 3, 4, 5, 6, 7, 8]),
  fichab("Seis bases de licitud (basta una)",
         "El **responsable** del tratamiento",
         ["a) **Consentimiento** del interesado", "b) Ejecución de un **contrato** o medidas precontractuales", "c) **Obligación legal** del responsable", "d) **Intereses vitales** del interesado o de otra persona", "e) **Misión en interés público** o ejercicio de **poderes públicos**", "f) **Intereses legítimos** del responsable o de un tercero, si no prevalecen los del interesado"],
         "—",
         "Basta **una** base, y el consentimiento es **solo una** de las seis. La letra **f)** (interés legítimo) **no** vale para las **autoridades públicas** en el ejercicio de sus funciones."))}

{unidad("2.2 Condiciones del consentimiento (RGPD, art. 7)",
  R(7, ["el responsable deberá ser capaz de demostrar que aquel consintió", "retirar su consentimiento en cualquier momento", "no afectará a la licitud del tratamiento basada en el consentimiento previo a su retirada", "Será tan fácil retirar el consentimiento como darlo"]),
  ficha("El **interesado** que consiente",
        ["La solicitud, si va en una declaración escrita con otros asuntos, debe **distinguirse claramente** (7.2)", "Puede **retirar** el consentimiento **en cualquier momento**, y será **tan fácil retirarlo como darlo** (7.3)"],
        ["La retirada **no** afecta a la licitud del tratamiento **anterior** (7.3)", "Se valora si el contrato se **supedita** a consentir tratamientos **innecesarios** para ejecutarlo (7.4)"],
        "Carga de la prueba: el **responsable** debe poder **demostrar** que el interesado consintió (7.1)",
        "La retirada **no tiene efectos retroactivos**. La prueba del consentimiento corresponde al **responsable**."))}

{unidad("2.3 Consentimiento de los niños en servicios de la sociedad de la información (RGPD, art. 8)",
  R(8, ["tenga como mínimo 16 años", "siempre que esta no sea inferior a 13 años"], solo=[1, 2, 3]),
  ficha("**Niños**, en la oferta directa de servicios de la sociedad de la información",
        "Su consentimiento es válido desde los **16 años**; por debajo, debe darlo o autorizarlo el titular de la **patria potestad o tutela**",
        "Los Estados pueden fijar por ley una edad **inferior**, **no inferior a 13 años** (8.1, párrafo segundo)",
        "El responsable hará **esfuerzos razonables** para verificar el consentimiento del titular de la patria potestad (8.2)",
        "RGPD: **16** años, con un mínimo nacional de **13**. España ha fijado **14** (→ II.2.5)."))}

{unidad("2.4 El consentimiento en la LO 3/2018 (art. 6)",
  L(6, ["conste de manera específica e inequívoca que dicho consentimiento se otorga para todas ellas", "No podrá supeditarse la ejecución del contrato"]),
  ficha("El **afectado**",
        ["Misma definición que el art. 4.11 RGPD (6.1)", "Para **varias finalidades**: debe constar de manera **específica e inequívoca** que se consiente **para todas** (6.2)"],
        "No se puede **supeditar la ejecución del contrato** a consentir tratamientos para finalidades **ajenas** a la relación contractual (6.3)",
        "—",
        "Consentimiento para varias finalidades: **específico e inequívoco para todas**. Prohibido condicionar el contrato a fines que no guarden relación con él."))}

{unidad("2.5 Consentimiento de los menores de edad (LO 3/2018, art. 7)",
  L(7, ["cuando sea mayor de catorce años", "solo será lícito si consta el del titular de la patria potestad o tutela"]),
  ficha("**Menores de edad**",
        ["**Mayores de 14 años**: pueden consentir por sí mismos (7.1)", "**Menores de 14 años**: solo es lícito con el consentimiento del titular de la **patria potestad o tutela** (7.2)"],
        "Excepción: cuando la ley exija la **asistencia** de los titulares de la patria potestad o tutela para el acto o negocio en que se recaba el consentimiento (7.1, párrafo segundo)",
        "—",
        "En España, **14** años (no 16 ni 13). La ley dice «**mayor** de catorce años»."))}

{unidad("2.6 Obligación legal, interés público y poderes públicos (LO 3/2018, art. 8)",
  L(8, ["o una norma con rango de ley", "cuando derive de una competencia atribuida por una norma con rango de ley"]),
  fichab("Bases c) y e) del art. 6.1 RGPD en España",
         "Las Administraciones y demás responsables que tratan datos por **obligación legal** o en ejercicio de **poderes públicos**",
         ["**Obligación legal** (6.1 c RGPD): debe preverla una norma de **Derecho de la UE** o una norma **con rango de ley** (8.1)", "**Interés público o poderes públicos** (6.1 e RGPD): debe derivar de una **competencia atribuida por norma con rango de ley** (8.2)"],
         "—",
         "Rango exigido: **ley** (o Derecho de la UE para la obligación legal). Un reglamento **no basta**."))}
""", 2)

T.ap("s5", "II.3 Categorías especiales de datos (RGPD, art. 9; LO 3/2018, art. 9)", f"""
{unidad("3.1 Prohibición y excepciones (RGPD, art. 9)",
  R(9, ["Quedan prohibidos", "consentimiento explícito", "que el interesado ha hecho manifiestamente públicos"], solo=list(range(1, 13))),
  fichab("Datos especialmente protegidos",
         "—",
         ["**Prohibido** tratar datos que revelen origen étnico o racial, opiniones políticas, convicciones religiosas o filosóficas, afiliación sindical, y datos **genéticos**, **biométricos** (para identificar), de **salud** y de **vida u orientación sexual** (9.1)", "**Excepciones** (9.2): consentimiento **explícito**; Derecho laboral y de protección social; intereses vitales; fundaciones y asociaciones sin ánimo de lucro con sus miembros; datos hechos **manifiestamente públicos** por el interesado; reclamaciones y función judicial; interés público esencial; medicina y asistencia sanitaria o social; salud pública; archivo, investigación y estadística"],
         "—",
         "Aquí el consentimiento ha de ser **explícito** (no basta el del art. 6). Los datos biométricos son especiales cuando se dirigen a **identificar de manera unívoca**."))}

{unidad("3.2 Categorías especiales en la LO 3/2018 (art. 9)",
  L(9, ["el solo consentimiento del afectado no bastará para levantar la prohibición", "deberán estar amparados en una norma con rango de ley"]),
  fichab("Lo que añade la ley española",
         "—",
         ["Datos cuya **finalidad principal** sea identificar **ideología, afiliación sindical, religión, orientación sexual, creencias u origen racial o étnico**: el **solo consentimiento no basta** para levantar la prohibición (9.1)", "Tratamientos de las letras **g), h) e i)** del art. 9.2 RGPD fundados en Derecho español: necesitan **norma con rango de ley** (9.2)"],
         "—",
         "«El **solo** consentimiento **no bastará**» (para evitar situaciones discriminatorias), aunque pueden valer los demás supuestos del art. 9.2 RGPD."))}

{resumen([
  "Siete principios (art. 5 RGPD): licitud, lealtad y transparencia; limitación de la finalidad; **minimización**; exactitud; limitación del plazo de conservación; integridad y confidencialidad; **responsabilidad proactiva**.",
  "Seis bases de licitud (art. 6.1): basta **una**; el **interés legítimo** no vale para las autoridades públicas en sus funciones.",
  "Consentimiento: **libre, específico, informado e inequívoco**; se retira **en cualquier momento** y sin efecto retroactivo; menores: **14 años** en España (RGPD: 16, mínimo 13).",
  "Categorías especiales: **prohibidas** salvo excepciones (art. 9.2); el **solo** consentimiento no basta para datos cuya finalidad principal sea identificar ideología, religión, etc. (art. 9.1 LO 3/2018)."],
  "Siguiente: III. ¿Qué derechos tiene el interesado?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Qué derechos tiene el interesado? (RGPD, arts. 12 a 22, 77, 78 y 82; LO 3/2018, arts. 11 a 18)", donde(
  "Tercera pregunta. El interesado tiene derecho a ser **informado** (arts. 13 y 14) y a ejercer los derechos de **acceso, rectificación, supresión, limitación, portabilidad y oposición**, además de no ser objeto de **decisiones automatizadas**. Si no se le atiende, puede **reclamar** ante la autoridad de control o acudir a los **tribunales**.",
  ["1 Transparencia, información y reglas comunes de ejercicio (RGPD, arts. 12 a 14; LO 3/2018, arts. 11 y 12)", "2 Acceso, rectificación y supresión (RGPD, arts. 15 a 17; LO 3/2018, arts. 13 a 15)", "3 Limitación, portabilidad, oposición y decisiones automatizadas (RGPD, arts. 18, 20 a 22; LO 3/2018, arts. 16 a 18)", "4 Reclamación, tutela judicial e indemnización (RGPD, arts. 77, 78 y 82)"]))

T.ap("s6", "III.1 Transparencia, información y reglas comunes de ejercicio (RGPD, arts. 12 a 14; LO 3/2018, arts. 11 y 12)", f"""
{unidad("1.1 Plazo, forma y gratuidad (RGPD, art. 12)",
  R(12, ["en el plazo de un mes a partir de la recepción de la solicitud", "Dicho plazo podrá prorrogarse otros dos meses en caso necesario", "serán a título gratuito", "cobrar un canon razonable", "negarse a actuar respecto de la solicitud"], solo=[1, 2, 3, 4, 5, 6, 7, 8, 9]),
  fichab("Reglas comunes a todos los derechos",
         "El **responsable** del tratamiento",
         ["Información **concisa, transparente, inteligible y de fácil acceso**, con lenguaje **claro y sencillo** (12.1)", "Si se pidió por medios **electrónicos**, se responde por medios electrónicos cuando sea posible (12.3)", "Si no da curso a la solicitud, informa de las razones y de la posibilidad de **reclamar** ante la autoridad de control y de acudir a los **tribunales** (12.4)", "**Gratuito**; si las solicitudes son **manifiestamente infundadas o excesivas**: canon razonable o negativa, y la **carga de la prueba** es del responsable (12.5)"],
         "Responder: **1 mes** desde la recepción, prorrogable **2 meses más** (informando de la prórroga dentro del primer mes)",
         "**Un mes + dos** de prórroga (en total, hasta tres). No confundir con los **diez días** de la comunicación del delegado (→ V.1.1) ni con las **72 horas** de la violación de seguridad (→ IV.3.4)."))}

{unidad("1.2 Información al interesado (RGPD, arts. 13 y 14)",
  R(13, ["en el momento en que estos se obtengan", "la identidad y los datos de contacto del responsable", "los fines del tratamiento a que se destinan los datos personales y la base jurídica del tratamiento", "el derecho a presentar una reclamación ante una autoridad de control"], solo=[1, 2, 3, 4, 8, 9, 10, 12, 16]),
  R(14, ["a más tardar dentro de un mes", "a más tardar en el momento de la primera comunicación", "en el momento en que los datos personales sean comunicados por primera vez"], solo=[1, 16, 17, 18, 19]),
  fichab("El deber de informar al interesado",
         "El **responsable** del tratamiento",
         ["Datos obtenidos **del interesado** (art. 13): identidad y contacto del responsable, contacto del **delegado**, **fines** y **base jurídica**, destinatarios… y, para un tratamiento leal y transparente, **plazo de conservación**, **derechos**, retirada del consentimiento, **reclamación** ante la autoridad de control, etc. (13.1 y 2)", "Datos **no** obtenidos del interesado (art. 14): lo mismo, más las **categorías** de datos y la **fuente** de la que proceden (14.1 d y 14.2 f)", "No hay que informar de lo que el interesado **ya sepa** (13.4 y 14.5 a)"],
         ["Art. 13: **en el momento** en que se obtienen los datos (13.1)", "Art. 14: en un plazo razonable y **a más tardar dentro de un mes**; si se usan para comunicarse con él, **en la primera comunicación**; si se van a comunicar a otro destinatario, **la primera vez** que se comuniquen (14.3)"],
         "Recogida **directa**: información **en el momento**. Recogida **indirecta**: como máximo **un mes**, y se añaden **categorías** y **fuente**. En España puede darse **por capas** (→ III.1.3)."))}

{unidad("1.3 Información por capas (LO 3/2018, art. 11)",
  L(11, ["facilitando al afectado la información básica", "La identidad del responsable del tratamiento", "La finalidad del tratamiento", "Las fuentes de las que procedieran los datos"]),
  fichab("Cómo se cumple el deber de informar",
         "El **responsable**",
         ["Se da una **información básica** y una dirección electrónica u otro medio para acceder **de forma sencilla e inmediata** al resto (11.1)", "Información básica mínima: **identidad** del responsable, **finalidad** y posibilidad de ejercer los **derechos** de los arts. 15 a 22 RGPD; si hay **perfiles**, también esta circunstancia (11.2)", "Si los datos **no** se obtuvieron del afectado: además, **categorías de datos** y **fuentes** (11.3)"],
         "—",
         "Información **básica** + acceso al **resto**. Si los datos no proceden del afectado, se añaden **categorías** y **fuentes**."))}

{unidad("1.4 Ejercicio de los derechos (LO 3/2018, art. 12)",
  L(12, ["directamente o por medio de representante legal o voluntario", "El ejercicio del derecho no podrá ser denegado por el solo motivo de optar el afectado por otro medio", "recaerá sobre el responsable", "menores de catorce años", "Serán gratuitas"]),
  ficha("El **afectado**, directamente o por **representante legal o voluntario**; por los **menores de 14 años**, los titulares de la **patria potestad** (12.6)",
        ["Medios **fácilmente accesibles**; no se puede denegar el derecho por usar **otro medio** (12.2)", "El **encargado** puede tramitar las solicitudes si así lo prevé el contrato (12.3)", "Actuaciones **gratuitas** (12.7)"],
        "Regímenes especiales previstos en las leyes aplicables a determinados tratamientos (12.5)",
        "La **prueba** de haber respondido corresponde al **responsable** (12.4)",
        "Por los **menores de catorce** años actúan los titulares de la patria potestad. Nunca se puede denegar el derecho **solo** por elegir otro medio."))}
""", 2)

T.ap("s7", "III.2 Acceso, rectificación y supresión (RGPD, arts. 15 a 17; LO 3/2018, arts. 13 a 15)", f"""
{unidad("2.1 Derecho de acceso (RGPD, art. 15; LO 3/2018, art. 13)",
  R(15, ["confirmación de si se están tratando o no datos personales que le conciernen", "facilitará una copia de los datos personales objeto de tratamiento", "un canon razonable basado en los costes administrativos"]),
  L(13, ["un sistema de acceso remoto, directo y seguro", "en más de una ocasión durante el plazo de seis meses"]),
  ficha("El **interesado**",
        ["**Confirmación** de si se tratan sus datos y, en ese caso, **acceso** a ellos y a la información del art. 15.1 (fines, categorías, destinatarios, plazo de conservación, derechos, reclamación, origen, decisiones automatizadas)", "Una **copia** gratuita; por las **demás** copias, canon razonable (15.3)", "Se entiende otorgado si se facilita un **sistema de acceso remoto, directo y seguro** y permanente (13.2 LO)"],
        ["La copia no puede afectar negativamente a los derechos y libertades **de otros** (15.4)", "Puede considerarse **repetitivo** ejercerlo más de una vez en **seis meses**, salvo causa legítima (13.3 LO)", "Si elige un medio que suponga un **coste desproporcionado**, asume el exceso (13.4 LO)"],
        "Reclamación ante la autoridad de control y tutela judicial (→ III.4)",
        "**Seis meses** para considerar repetitivo el acceso (LO 3/2018). La **primera** copia es gratuita; las demás pueden tener canon."))}

{unidad("2.2 Derecho de rectificación (RGPD, art. 16; LO 3/2018, art. 14)",
  R(16, ["sin dilación indebida", "la rectificación de los datos personales inexactos", "que se completen los datos personales que sean incompletos"]),
  L(14, ["a qué datos se refiere y la corrección que haya de realizarse"]),
  ficha("El **interesado**",
        ["**Rectificar** datos **inexactos**, **sin dilación indebida**", "**Completar** datos **incompletos**, incluso mediante una declaración adicional"],
        "En la solicitud debe indicar **qué datos** y **qué corrección**, con documentación justificativa cuando sea preciso (art. 14 LO)",
        "Reclamación ante la autoridad de control y tutela judicial (→ III.4)",
        "La rectificación también comprende **completar** datos incompletos."))}

{unidad("2.3 Derecho de supresión o «derecho al olvido» (RGPD, art. 17; LO 3/2018, art. 15)",
  R(17, ["ya no sean necesarios en relación con los fines", "el interesado retire el consentimiento", "hayan sido tratados ilícitamente", "para ejercer el derecho a la libertad de expresión e información", "para la formulación, el ejercicio o la defensa de reclamaciones"]),
  L(15, ["podrá conservar los datos identificativos del afectado"]),
  ficha("El **interesado**",
        ["**Supresión sin dilación indebida** si: los datos ya **no son necesarios**; **retira el consentimiento** (sin otra base); se **opone** (art. 21); tratamiento **ilícito**; **obligación legal**; datos de servicios de la sociedad de la información ofrecidos a **niños** (17.1)", "Si el responsable hizo públicos los datos, debe **informar** a otros responsables de la solicitud de supresión de enlaces, copias o réplicas (17.2)"],
        ["No se aplica cuando el tratamiento sea necesario para: **libertad de expresión e información**; obligación legal o **misión de interés público**; **salud pública**; **archivo, investigación o estadística**; **reclamaciones** (17.3)", "Tras una oposición a la **mercadotecnia directa**, pueden conservarse los datos **identificativos** necesarios para impedir tratamientos futuros (15.2 LO)"],
        "Reclamación ante la autoridad de control y tutela judicial (→ III.4); al suprimir, el responsable **bloquea** los datos (→ IV.3.2)",
        "El RGPD lo llama «**derecho al olvido**» entre paréntesis. El derecho al olvido en **buscadores** y **redes sociales** es de la LO 3/2018 (→ VI.4.2)."))}
""", 2)

T.ap("s8", "III.3 Limitación, portabilidad, oposición y decisiones automatizadas (RGPD, arts. 18, 20 a 22; LO 3/2018, arts. 16 a 18)", f"""
{unidad("3.1 Derecho a la limitación del tratamiento (RGPD, art. 18; LO 3/2018, art. 16)",
  R(18, ["impugne la exactitud de los datos personales", "se oponga a la supresión de los datos personales y solicite en su lugar la limitación de su uso", "será informado por el responsable antes del levantamiento de dicha limitación"]),
  L(16, ["debe constar claramente en los sistemas de información del responsable"]),
  ficha("El **interesado**",
        ["Obtener la **limitación** cuando: **impugna la exactitud** (mientras se verifica); tratamiento **ilícito** pero prefiere limitar a suprimir; el responsable ya no los necesita pero el interesado sí, para **reclamaciones**; se ha **opuesto** (mientras se verifica qué motivos prevalecen) (18.1)"],
        "Datos limitados: solo se **conservan**; otro tratamiento exige **consentimiento**, reclamaciones, protección de derechos de otra persona o **interés público importante** (18.2)",
        "Ser **informado antes** de que se levante la limitación (18.3); la limitación debe **constar claramente** en los sistemas del responsable (16.2 LO)",
        "Limitar ≠ suprimir: el dato se **conserva** marcado (art. 4.3 RGPD) y no se usa."))}

{unidad("3.2 Derecho a la portabilidad de los datos (RGPD, art. 20; LO 3/2018, art. 17)",
  R(20, ["en un formato estructurado, de uso común y lectura mecánica", "el tratamiento se efectúe por medios automatizados", "directamente de responsable a responsable cuando sea técnicamente posible", "Tal derecho no se aplicará al tratamiento que sea necesario para el cumplimiento de una misión realizada en interés público"]),
  L(17),
  ficha("El **interesado**, respecto de los datos que **él mismo haya facilitado**",
        ["**Recibirlos** en formato **estructurado, de uso común y lectura mecánica** y **transmitirlos** a otro responsable (20.1)", "Que se transmitan **directamente** de responsable a responsable cuando sea **técnicamente posible** (20.2)"],
        ["Solo si el tratamiento se basa en el **consentimiento** o en un **contrato** **y** se efectúa por **medios automatizados** (20.1)", "**No** se aplica a tratamientos necesarios para una **misión de interés público** o ejercicio de **poderes públicos** (20.3)", "No puede afectar negativamente a los derechos de **otros** (20.4)"],
        "Reclamación ante la autoridad de control y tutela judicial (→ III.4)",
        "La definición literal del 20.1 es la pregunta oficial X 49 (→ Cierre 1). Requisitos **acumulativos**: consentimiento o contrato **y** medios automatizados."))}

{unidad("3.3 Derecho de oposición (RGPD, art. 21; LO 3/2018, art. 18)",
  R(21, ["por motivos relacionados con su situación particular", "salvo que acredite motivos legítimos imperiosos", "tenga por objeto la mercadotecnia directa", "dejarán de ser tratados para dichos fines"], solo=[1, 2, 3, 4]),
  L(18),
  ficha("El **interesado**",
        ["Oponerse **en cualquier momento**, por motivos de su **situación particular**, a tratamientos basados en el art. 6.1 **e) o f)** (interés público, poderes públicos o interés legítimo), incluidos perfiles (21.1)", "Oponerse **en todo momento** a la **mercadotecnia directa**: los datos **dejan de tratarse** para esos fines (21.2 y 3)"],
        "En el caso general, el responsable puede seguir si acredita **motivos legítimos imperiosos** que prevalezcan, o para **reclamaciones** (21.1)",
        "El derecho debe mencionarse **explícitamente** al interesado, como muy tarde en la **primera comunicación** (21.4)",
        "Frente a la **mercadotecnia directa** la oposición es **absoluta**: no cabe alegar motivos imperiosos."))}

{unidad("3.4 Decisiones individuales automatizadas (RGPD, art. 22)",
  R(22, ["basada únicamente en el tratamiento automatizado", "se basa en el consentimiento explícito del interesado", "derecho a obtener intervención humana por parte del responsable, a expresar su punto de vista y a impugnar la decisión"]),
  ficha("El **interesado**",
        "No ser objeto de una decisión basada **únicamente** en el tratamiento automatizado (incluidos **perfiles**) que produzca **efectos jurídicos** o le afecte **significativamente** de modo similar (22.1)",
        ["Excepciones: necesaria para un **contrato**; **autorizada por el Derecho** de la UE o del Estado con garantías; **consentimiento explícito** (22.2)", "No pueden basarse en **categorías especiales** salvo art. 9.2 a) o g) y con medidas adecuadas (22.4)"],
        "En el contrato y el consentimiento, como mínimo: **intervención humana**, **expresar su punto de vista** e **impugnar** la decisión (22.3)",
        "La clave es «**únicamente**» automatizada. Garantías mínimas: **intervención humana**, punto de vista e impugnación."))}
""", 2)

T.ap("s9", "III.4 Reclamación, tutela judicial e indemnización (RGPD, arts. 77, 78 y 82)", f"""
{unidad("4.1 Reclamación ante la autoridad de control y tutela judicial (RGPD, arts. 77 y 78)",
  R(77, ["en particular en el Estado miembro en el que tenga su residencia habitual, lugar de trabajo o lugar de la supuesta infracción"]),
  R(78, ["en el plazo de tres meses", "ante los tribunales del Estado miembro en que esté establecida la autoridad de control"], solo=[1, 2, 3]),
  fichab("Cómo se defiende el interesado",
         "El **interesado**, ante la **autoridad de control** (art. 77) o los **tribunales** (art. 78)",
         ["**Reclamación** ante una autoridad de control, en particular la del Estado de su **residencia habitual**, **lugar de trabajo** o **lugar de la infracción** (77.1)", "**Tutela judicial** contra decisiones vinculantes de la autoridad de control (78.1), o si no da curso a la reclamación o **no informa en tres meses** (78.2)", "Las acciones contra una autoridad de control, ante los tribunales **de su Estado** (78.3)"],
         "La autoridad debe informar del curso o resultado de la reclamación: si no lo hace en **3 meses**, cabe la tutela judicial (78.2)",
         "En España, los actos de la **Presidencia de la AEPD** se recurren ante la **Audiencia Nacional** (→ V.2.4). El interesado puede dirigirse antes al **delegado** (→ V.1.4)."))}

{unidad("4.2 Derecho a indemnización (RGPD, art. 82)",
  R(82, ["daños y perjuicios materiales o inmateriales", "Un encargado únicamente responderá", "si demuestra que no es en modo alguno responsable del hecho", "cada responsable o encargado será considerado responsable de todos los daños y perjuicios"], solo=[1, 2, 3, 4, 5]),
  ficha("**Toda persona** que haya sufrido daños y perjuicios **materiales o inmateriales** por una infracción del RGPD",
        "Indemnización a cargo del **responsable** o del **encargado** (82.1)",
        ["El **encargado** solo responde si incumple sus obligaciones específicas o actúa al margen o en contra de las **instrucciones** del responsable (82.2)", "Exención: demostrar que **no es en modo alguno responsable** del hecho (82.3)"],
        "Si participan varios, **cada uno** responde de **todos** los daños, con acción de **repetición** contra los demás (82.4 y 5)",
        "Daños **materiales o inmateriales**. Responsabilidad **por el todo** de cada participante frente al interesado."))}

{resumen([
  "Respuesta del responsable: **un mes**, prorrogable **dos meses** más; **gratuita**, salvo solicitudes manifiestamente infundadas o excesivas (art. 12 RGPD).",
  "Acceso: copia gratuita; repetitivo si se ejerce más de una vez en **seis meses** (LO 3/2018). Supresión («derecho al olvido») con excepciones como la **libertad de expresión**.",
  "Portabilidad: datos **facilitados** por el interesado, con base en **consentimiento o contrato** y por **medios automatizados**. Oposición a la **mercadotecnia directa**: absoluta.",
  "Defensa: **reclamación** ante la autoridad de control (tutela judicial si no informa en **tres meses**) e **indemnización** de daños materiales o inmateriales."],
  "Siguiente: IV. ¿Quién responde del tratamiento? Responsable y encargado")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Quién responde del tratamiento? Responsable y encargado (RGPD, arts. 24 a 35; LO 3/2018, arts. 28 a 33)", donde(
  "Cuarta pregunta. El **responsable** decide los fines y medios y debe **demostrar** que cumple; el **encargado** trata los datos **por su cuenta** y bajo sus **instrucciones**. Los dos llevan un **registro**, aplican medidas de **seguridad** y responden ante las **violaciones de seguridad**.",
  ["1 El responsable y los corresponsables (RGPD, arts. 24 a 26; LO 3/2018, arts. 28 y 29)", "2 El encargado del tratamiento (RGPD, art. 28; LO 3/2018, art. 33)", "3 Registro, bloqueo, seguridad, violaciones y evaluación de impacto (RGPD, arts. 30 y 32 a 35; LO 3/2018, arts. 31 y 32)"]))

T.ap("s10", "IV.1 El responsable y los corresponsables (RGPD, arts. 24 a 26; LO 3/2018, arts. 28 y 29)", f"""
{unidad("1.1 Responsabilidad del responsable (RGPD, art. 24; LO 3/2018, art. 28)",
  R(24, ["aplicará medidas técnicas y organizativas apropiadas a fin de garantizar y poder demostrar"]),
  L(28, ["determinarán las medidas técnicas y organizativas apropiadas", "los mayores riesgos", "de menores de edad y personas con discapacidad"], solo=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
  fichab("Enfoque de riesgo",
         "El **responsable** (art. 24 RGPD) y, en la LO 3/2018, **responsables y encargados** (art. 28)",
         ["Medidas **técnicas y organizativas** apropiadas para **garantizar y poder demostrar** el cumplimiento, revisadas cuando sea necesario (24.1)", "Pueden incluir **políticas** de protección de datos (24.2); los **códigos de conducta** y **certificaciones** sirven para demostrar el cumplimiento (24.3)", "Valorar si procede la **evaluación de impacto** y la consulta previa (28.1 LO)", "Riesgos mayores, entre otros: discriminación o fraude; categorías especiales; **perfiles**; **menores** y personas con **discapacidad**; tratamiento **masivo**; transferencias habituales sin nivel adecuado (28.2 LO)"],
         "—",
         "Es la **responsabilidad proactiva** del art. 5.2 llevada a la práctica: no basta cumplir, hay que poder **demostrarlo**."))}

{unidad("1.2 Protección de datos desde el diseño y por defecto (RGPD, art. 25)",
  R(25, ["tanto en el momento de determinar los medios de tratamiento como en el momento del propio tratamiento", "por defecto, solo sean objeto de tratamiento los datos personales que sean necesarios para cada uno de los fines específicos del tratamiento", "no sean accesibles, sin la intervención de la persona, a un número indeterminado de personas físicas"]),
  fichab("Privacidad desde el diseño y por defecto",
         "El **responsable**",
         ["**Desde el diseño**: medidas (como la **seudonimización**) al **determinar los medios** y durante el tratamiento, para aplicar los principios como la **minimización** (25.1)", "**Por defecto**: solo los datos **necesarios** para cada fin: cantidad, extensión, plazo de conservación y accesibilidad (25.2)", "Una **certificación** puede acreditar el cumplimiento (25.3)"],
         "—",
         "**Por defecto**, los datos no deben ser accesibles a un **número indeterminado** de personas sin intervención del interesado."))}

{unidad("1.3 Corresponsables del tratamiento (RGPD, art. 26; LO 3/2018, art. 29)",
  R(26, ["determinen conjuntamente los objetivos y los medios del tratamiento", "de mutuo acuerdo", "frente a, y en contra de, cada uno de los responsables"]),
  L(29, ["atendiendo a las actividades que efectivamente desarrolle cada uno de los corresponsables"]),
  fichab("Varios responsables a la vez",
         "Dos o más responsables que determinan **conjuntamente** objetivos y medios",
         ["Fijan **de mutuo acuerdo** y de modo transparente sus responsabilidades; el acuerdo puede designar un **punto de contacto** (26.1)", "Los aspectos esenciales del acuerdo se ponen a disposición del interesado (26.2)", "Las responsabilidades se determinan según las **actividades que efectivamente** desarrolle cada uno (art. 29 LO)"],
         "—",
         "Diga lo que diga el acuerdo, el interesado puede ejercer sus derechos frente a **cada uno** de los corresponsables (26.3)."))}
""", 2)

T.ap("s11", "IV.2 El encargado del tratamiento (RGPD, art. 28; LO 3/2018, art. 33)", f"""
{unidad("2.1 Régimen del encargado (RGPD, art. 28)",
  R(28, ["garantías suficientes", "sin la autorización previa por escrito, específica o general, del responsable", "únicamente siguiendo instrucciones documentadas del responsable", "suprimirá o devolverá todos los datos personales", "seguirá siendo plenamente responsable ante el responsable del tratamiento", "constará por escrito, inclusive en formato electrónico", "será considerado responsable del tratamiento con respecto a dicho tratamiento"], solo=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 18, 19]),
  fichab("Tratamiento por cuenta del responsable",
         ["El **responsable** elige un encargado que ofrezca **garantías suficientes** (28.1)", "El **encargado** trata los datos por su cuenta"],
         ["Relación regida por un **contrato u otro acto jurídico**, **por escrito** (incluso electrónico) (28.3 y 9)", "El encargado trata los datos **solo** con **instrucciones documentadas**, garantiza la **confidencialidad**, aplica la **seguridad**, ayuda al responsable y, al terminar, **suprime o devuelve** los datos a elección del responsable (28.3)", "**Subencargado**: solo con **autorización previa por escrito, específica o general**, del responsable; el encargado inicial sigue siendo **plenamente responsable** (28.2 y 4)"],
         "—",
         "Si el encargado determina **fines y medios**, pasa a ser considerado **responsable** de ese tratamiento (28.10)."))}

{unidad("2.2 El encargado en la LO 3/2018 (art. 33)",
  L(33, ["no se considerará comunicación de datos", "quien figurando como encargado utilizase los datos para sus propias finalidades", "debidamente bloqueados", "mediante la adopción de una norma reguladora de dichas competencias"]),
  fichab("Lo que añade la ley española",
         ["El **encargado**", "En el **sector público**: un **órgano** o **organismo** al que una **norma** atribuya las competencias de encargado (33.5)"],
         ["Su acceso a los datos necesarios para el servicio **no es comunicación de datos** (33.1)", "Es **responsable** (no encargado) quien actúa en **nombre propio** ante los afectados sin constar que actúa por cuenta de otro, salvo encargos en el marco de la **contratación del sector público**; y quien usa los datos **para sus propias finalidades** (33.2)", "Al terminar el servicio, el **responsable** decide si se destruyen, se devuelven o pasan a otro encargado; no se destruyen si una ley obliga a conservarlos (33.3)", "Puede conservarlos **bloqueados** mientras puedan derivarse responsabilidades (33.4)"],
         "—",
         "El encargado que usa los datos **para sus propios fines** se convierte en **responsable**."))}
""", 2)

T.ap("s12", "IV.3 Registro, bloqueo, seguridad, violaciones y evaluación de impacto (RGPD, arts. 30 y 32 a 35; LO 3/2018, arts. 31 y 32)", f"""
{unidad("3.1 Registro de las actividades de tratamiento (RGPD, art. 30; LO 3/2018, art. 31)",
  R(30, ["llevarán un registro de las actividades de tratamiento", "constarán por escrito, inclusive en formato electrónico", "a menos de 250 personas"], solo=[1, 9, 14, 15, 16]),
  L(31, ["harán público un inventario de sus actividades de tratamiento accesible por medios electrónicos"]),
  fichab("El registro",
         ["Cada **responsable** y cada **encargado** (y, en su caso, sus representantes) (30.1 y 2)", "Los sujetos del **art. 77.1** LO 3/2018 (sector público): además, un **inventario público** (31.2)"],
         ["**Por escrito**, incluso en formato electrónico (30.3)", "A disposición de la **autoridad de control** que lo solicite (30.4)", "Si hay **delegado**, se le comunica cualquier cambio del registro (31.1 LO)", "Inventario del sector público: accesible por medios **electrónicos**, con la información del art. 30 RGPD y la **base legal** (31.2 LO)"],
         "Exención: organizaciones de **menos de 250** personas, salvo tratamiento con **riesgo**, **no ocasional** o con **categorías especiales** o datos penales (30.5)",
         "**250** personas. Las Administraciones, además del registro, publican un **inventario** con la **base legal**."))}

{unidad("3.2 Bloqueo de los datos (LO 3/2018, art. 32)",
  L(32, ["estará obligado a bloquear los datos cuando proceda a su rectificación o supresión", "y solo por el plazo de prescripción de las mismas", "deberá procederse a la destrucción de los datos"]),
  fichab("Qué es bloquear",
         "El **responsable**; la **AEPD** y las autoridades **autonómicas** pueden fijar excepciones (32.5)",
         ["Obligación: bloquear al **rectificar o suprimir** (32.1)", "Bloqueo = **identificación y reserva** de los datos para impedir su tratamiento, incluida la **visualización**, salvo su puesta a disposición de **jueces**, **Ministerio Fiscal** y **Administraciones** competentes (32.2)", "Los datos bloqueados no se usan para **ninguna otra** finalidad (32.3)"],
         "Solo durante el **plazo de prescripción** de las responsabilidades; después, **destrucción** (32.2)",
         "Primero **bloqueo**, después **destrucción** al prescribir las responsabilidades."))}

{unidad("3.3 Seguridad del tratamiento (RGPD, art. 32)",
  R(32, ["un nivel de seguridad adecuado al riesgo", "la seudonimización y el cifrado de datos personales"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Medidas de seguridad",
         "El **responsable** y el **encargado**",
         ["Medidas **técnicas y organizativas** para un nivel de seguridad **adecuado al riesgo** (32.1)", "Entre otras: **seudonimización y cifrado**; confidencialidad, integridad, disponibilidad y resiliencia; **restaurar** el acceso tras un incidente; **verificación** periódica de la eficacia (32.1 a-d)"],
         "—",
         f"No hay una lista cerrada de medidas: se ajustan al **riesgo**. En el sector público, los responsables del art. 77.1 LO 3/2018 {c('LOPD', 'Disposición adicional primera', 'deberán aplicar a los tratamientos de datos personales las medidas de seguridad que correspondan de las previstas en el Esquema Nacional de Seguridad')} (disposición adicional primera)."))}

{unidad("3.4 Violaciones de la seguridad: notificación y comunicación (RGPD, arts. 33 y 34)",
  R(33, ["a más tardar 72 horas después de que haya tenido constancia de ella", "El encargado del tratamiento notificará sin dilación indebida al responsable del tratamiento"], solo=[1, 2, 3, 4, 5, 6, 7, 9]),
  R(34, ["entrañe un alto riesgo para los derechos y libertades de las personas físicas", "suponga un esfuerzo desproporcionado"], solo=[1, 2, 3, 4, 5, 6]),
  fichab("Brechas de seguridad",
         ["El **responsable** notifica a la **autoridad de control** y comunica al **interesado**", "El **encargado** notifica al **responsable** (33.2)"],
         ["A la **autoridad**: salvo que sea **improbable** que constituya un riesgo; con contenido mínimo (naturaleza, delegado, consecuencias, medidas) (33.1 y 3)", "Al **interesado**: cuando sea probable un **alto riesgo**, en lenguaje claro y sencillo (34.1 y 2); no es necesario si los datos eran **ininteligibles** (p. ej., **cifrado**), si se ha eliminado el alto riesgo o si supone un **esfuerzo desproporcionado** (en ese caso, comunicación **pública**) (34.3)", "El responsable **documenta** toda violación (33.5)"],
         "Autoridad: **sin dilación indebida** y, de ser posible, **72 horas** desde que tuvo constancia; si se retrasa, con los motivos (33.1)",
         "**72 horas** a la autoridad (umbral: **riesgo**); al interesado, sin dilación (umbral: **alto riesgo**)."))}

{unidad("3.5 Evaluación de impacto relativa a la protección de datos (RGPD, art. 35)",
  R(35, ["antes del tratamiento, una evaluación del impacto", "recabará el asesoramiento del delegado de protección de datos", "observación sistemática a gran escala de una zona de acceso público"], solo=[1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14]),
  fichab("Evaluación de impacto (EIPD)",
         ["El **responsable**, con el asesoramiento del **delegado** si existe (35.2)", "La **autoridad de control** publica la lista de tratamientos que la **requieren** (35.4) y puede publicar la de los que **no** (35.5)"],
         ["**Antes** del tratamiento, cuando sea probable un **alto riesgo** (35.1)", "Obligatoria en particular en: evaluación sistemática con **perfiles** y decisiones con efectos jurídicos; categorías especiales o datos penales **a gran escala**; **observación sistemática a gran escala** de zonas de acceso público (35.3)", "Contenido mínimo: descripción, **necesidad y proporcionalidad**, riesgos y medidas (35.7)"],
         "—",
         "Se hace **antes** del tratamiento. Umbral: **alto riesgo** (igual que la comunicación al interesado de una brecha)."))}

{resumen([
  "**Responsable**: medidas para **garantizar y poder demostrar** el cumplimiento; protección **desde el diseño y por defecto**; los **corresponsables** responden cada uno frente al interesado.",
  "**Encargado**: contrato **por escrito**, solo **instrucciones documentadas**, subencargado con **autorización previa por escrito**; si usa los datos para **sus fines**, es **responsable**.",
  "Registro de actividades (exención: **menos de 250** personas salvo riesgo); sector público: **inventario público** con base legal. **Bloqueo** al rectificar o suprimir.",
  "Brecha: a la autoridad en **72 horas** (riesgo); al interesado si hay **alto riesgo**. **EIPD** antes de tratamientos de **alto riesgo**."],
  "Siguiente: V. ¿Quién vigila? Delegado y autoridades de protección de datos")}
""", 2)

# =============================================================================
T.ap("bV", "V. ¿Quién vigila? Delegado y autoridades de protección de datos (RGPD, arts. 37 a 39, 51, 52 y 68; LO 3/2018, arts. 34 a 37, 44, 47, 48, 55 y 57; RD 389/2021, art. 6)", donde(
  "Quinta pregunta. El **delegado de protección de datos** supervisa **dentro** de la organización del responsable o del encargado; las **autoridades de control** (la **AEPD** y las **autonómicas**), **desde fuera** y con total independencia.",
  ["1 El delegado de protección de datos (RGPD, arts. 37 a 39; LO 3/2018, arts. 34 a 37)", "2 Las autoridades de protección de datos (RGPD, arts. 51, 52 y 68; LO 3/2018, arts. 44, 47, 48, 55 y 57; RD 389/2021, art. 6)"]))

T.ap("s13", "V.1 El delegado de protección de datos (RGPD, arts. 37 a 39; LO 3/2018, arts. 34 a 37)", f"""
{unidad("1.1 Designación (RGPD, art. 37; LO 3/2018, art. 34)",
  R(37, ["una autoridad u organismo público, excepto los tribunales que actúen en ejercicio de su función judicial", "observación habitual y sistemática de interesados a gran escala", "un único delegado de protección de datos para varias de estas autoridades u organismos", "en el marco de un contrato de servicios"]),
  L(34, ["Los colegios profesionales y sus consejos generales", "así como las Universidades públicas y privadas", "Las federaciones deportivas cuando traten datos de menores de edad", "comunicarán en el plazo de diez días a la Agencia Española de Protección de Datos", "una lista actualizada de delegados de protección de datos"]),
  fichab("Cuándo es obligatorio el delegado",
         ["Lo designan el **responsable** y el **encargado**", "Puede ser de la **plantilla** o actuar mediante **contrato de servicios** (37.6); un **grupo empresarial** o **varias autoridades públicas** pueden compartir uno (37.2 y 3)"],
         ["RGPD (37.1): **autoridades u organismos públicos** (salvo **tribunales** en función judicial); **observación habitual y sistemática a gran escala**; **categorías especiales** o datos penales a gran escala", "LO 3/2018 (34.1), **en todo caso**: colegios profesionales, **centros docentes y Universidades**, entidades de crédito, aseguradoras, distribuidores y comercializadores de electricidad y gas natural, centros **sanitarios** con historias clínicas, empresas de **seguridad privada**, **federaciones deportivas** con datos de **menores**, entre otros", "Voluntario en los demás casos, con el mismo régimen (34.2)", "Designado por sus **cualidades profesionales** y conocimientos especializados (37.5); datos de contacto **publicados** y comunicados a la autoridad (37.7)"],
         "Comunicar designación, nombramiento y cese a la AEPD o autoridad autonómica: **10 días**, sea obligatorio o voluntario (34.3)",
         "**Diez días** (pregunta oficial X 50, → Cierre 1). No necesitan delegado los **profesionales sanitarios a título individual** (34.1 l) ni los **tribunales** en función judicial (37.1 a)."))}

{unidad("1.2 Cualificación y posición (RGPD, art. 38; LO 3/2018, arts. 35 y 36)",
  R(38, ["no reciba ninguna instrucción en lo que respecta al desempeño de dichas funciones", "No será destituido ni sancionado", "rendirá cuentas directamente al más alto nivel jerárquico", "no den lugar a conflicto de intereses"]),
  L(35, ["mecanismos voluntarios de certificación"]),
  L(36, ["actuará como interlocutor", "salvo que incurriera en dolo o negligencia grave en su ejercicio", "no pudiendo oponer a este acceso el responsable o el encargado del tratamiento la existencia de cualquier deber de confidencialidad o secreto"]),
  fichab("Independencia del delegado",
         "El **delegado**, persona física o jurídica (art. 35 LO)",
         ["Participa **de forma adecuada y en tiempo oportuno** en todas las cuestiones de protección de datos (38.1), con **recursos** y acceso a los datos (38.2)", "**No recibe instrucciones**; rinde cuentas al **más alto nivel jerárquico** (38.3)", "Los interesados pueden dirigirse a él (38.4); guarda **secreto** (38.5); puede tener otras funciones **sin conflicto de intereses** (38.6)", "Cualificación acreditable con **certificación voluntaria**, que valora la **titulación universitaria** especializada (art. 35 LO)", "**Interlocutor** ante la AEPD y las autoridades autonómicas; puede **inspeccionar** procedimientos y emitir **recomendaciones** (36.1 LO); no se le puede oponer el **deber de confidencialidad** (36.3 LO); comunica **inmediatamente** las vulneraciones relevantes (36.4 LO)"],
         "—",
         "Si está integrado en la organización, no puede ser **removido ni sancionado** por desempeñar sus funciones **salvo dolo o negligencia grave** (36.2 LO)."))}

{unidad("1.3 Funciones (RGPD, art. 39)",
  R(39, ["informar y asesorar", "supervisar el cumplimiento", "cooperar con la autoridad de control", "actuar como punto de contacto de la autoridad de control"]),
  fichab("Qué hace el delegado (como mínimo)",
         "El **delegado**",
         ["**Informar y asesorar** al responsable, al encargado y a los empleados (a)", "**Supervisar** el cumplimiento, incluidas la formación del personal y las **auditorías** (b)", "**Asesorar** sobre la **evaluación de impacto** y supervisar su aplicación (c)", "**Cooperar** con la autoridad de control (d)", "Ser su **punto de contacto**, incluida la consulta previa (e)"],
         "—",
         "El delegado **asesora y supervisa**, pero la responsabilidad de cumplir sigue siendo del **responsable** (art. 24)."))}

{unidad("1.4 Intervención del delegado en las reclamaciones (LO 3/2018, art. 37)",
  L(37, ["con carácter previo a la presentación de una reclamación", "en el plazo máximo de dos meses a contar desde la recepción de la reclamación", "a fin de que este responda en el plazo de un mes"]),
  fichab("El delegado como vía previa",
         ["El **afectado**, si hay delegado", "La **AEPD** o la autoridad autonómica, que puede remitirle la reclamación"],
         ["**Voluntaria** para el afectado: «podrá» dirigirse al delegado antes de reclamar ante la autoridad (37.1)", "La autoridad **puede** remitir la reclamación al delegado (37.2); si no responde a tiempo, la autoridad **continúa** el procedimiento del título VIII (37.2 y 3)"],
         ["Respuesta del delegado al **afectado**: máximo **2 meses** desde la recepción (37.1)", "Respuesta del delegado a la **autoridad** que le remite la reclamación: **1 mes** (37.2)"],
         "**Dos meses** si se dirige el afectado; **un mes** si se la remite la autoridad."))}
""", 2)

T.ap("s14", "V.2 Las autoridades de protección de datos (RGPD, arts. 51, 52 y 68; LO 3/2018, arts. 44, 47, 48, 55 y 57; RD 389/2021, art. 6)", f"""
{unidad("2.1 La autoridad de control y su independencia (RGPD, arts. 51 y 52)",
  R(51, ["una o varias autoridades públicas independientes"], solo=[1, 2, 3]),
  R(52, ["con total independencia", "no solicitarán ni admitirán ninguna instrucción", "un presupuesto anual, público e independiente"]),
  fichab("Autoridades de control",
         "**Una o varias** autoridades públicas **independientes** por Estado (51.1); si hay varias, el Estado designa la que lo **representa** en el Comité (51.3)",
         ["Supervisan la aplicación del RGPD para proteger los derechos y facilitar la **libre circulación** de datos (51.1)", "Actúan con **total independencia**; sus miembros **no solicitan ni admiten instrucciones** (52.1 y 2)", "Eligen su propio **personal** y tienen **presupuesto anual, público e independiente** (52.5 y 6)"],
         "—",
         "La independencia es **total**: ni instrucciones del Gobierno ni de nadie. En España hay **varias** autoridades: la AEPD y las autonómicas (→ V.2.6)."))}

{unidad("2.2 El Comité Europeo de Protección de Datos (RGPD, art. 68)",
  R(68, ["que gozará de personalidad jurídica", "por el director de una autoridad de control de cada Estado miembro y por el Supervisor Europeo de Protección de Datos", "sin derecho a voto"], solo=[1, 2, 3, 4, 5]),
  fichab("El Comité («Comité Europeo de Protección de Datos»)",
         ["**Director** de una autoridad de control de cada Estado y el **Supervisor Europeo de Protección de Datos** (68.3)", "La **Comisión** participa **sin derecho a voto** (68.5)"],
         "Organismo de la Unión **con personalidad jurídica**, representado por su **presidente** (68.1 y 2)",
         "—",
         "En España, el representante común en el Comité es la **AEPD** (art. 44.2 LO 3/2018, → V.2.3)."))}

{unidad("2.3 La Agencia Española de Protección de Datos: naturaleza y funciones (LO 3/2018, arts. 44 y 47)",
  L(44, ["autoridad administrativa independiente de ámbito estatal", "Se relaciona con el Gobierno a través del Ministerio de Justicia", "representante común de las autoridades de protección de datos del Reino de España"]),
  L(47, ["ejercer las funciones establecidas en el artículo 57 y las potestades previstas en el artículo 58"]),
  fichab("La AEPD",
         "**Autoridad administrativa independiente de ámbito estatal** (Ley 40/2015), con **personalidad jurídica** y plena capacidad pública y privada (44.1)",
         ["Actúa con **plena independencia** de los poderes públicos (44.1)", "Se relaciona con el Gobierno a través del **Ministerio de Justicia** (44.1)", "**Representante común** de las autoridades españolas en el **Comité Europeo** (44.2)", "Supervisa la LO 3/2018 y el RGPD: **funciones** del art. 57 y **potestades** del art. 58 RGPD (art. 47)"],
         "—",
         "Denominación oficial: «Agencia Española de Protección de Datos, **Autoridad Administrativa Independiente**». Ministerio de relación: **Justicia**."))}

{unidad("2.4 La Presidencia y el Adjunto (LO 3/2018, art. 48)",
  L(48, ["estará auxiliada por un Adjunto", "a excepción de las relacionadas con los procedimientos regulados por el título VIII", "serán nombrados por el Gobierno, a propuesta del Ministerio de Justicia", "por mayoría de tres quintos de sus miembros en primera votación o, de no alcanzarse ésta, por mayoría absoluta en segunda votación", "tiene una duración de cinco años y puede ser renovado para otro período de igual duración", "recurribles, directamente, ante la Sala de lo Contencioso-administrativo de la Audiencia Nacional"]),
  fichab("Órgano de dirección de la AEPD",
         ["**Presidencia**: dirige la Agencia, la representa y dicta sus **resoluciones, circulares y directrices** (48.1)", "**Adjunto**: auxilia y sustituye; la Presidencia puede delegarle funciones **salvo** las de los procedimientos del **título VIII** (48.2)"],
         ["Propuesta del **Gobierno** (a propuesta del **Ministerio de Justicia**) tras **convocatoria pública** en el BOE; **audiencia** de los candidatos y **ratificación** por la **Comisión de Justicia** del Congreso (48.3)", "Nombramiento: **Consejo de Ministros**, por **real decreto** (48.4)", "Cese anticipado: a petición propia o separación por el Consejo de Ministros por incumplimiento grave, incapacidad, incompatibilidad o **condena firme por delito doloso**; en los tres primeros casos, con **ratificación parlamentaria** (48.5)", "Sus actos y disposiciones **ponen fin a la vía administrativa** (48.6)"],
         ["Ratificación: **3/5** de los miembros de la Comisión en primera votación o **mayoría absoluta** en segunda (con votos de al menos **dos grupos**) (48.3)", "Convocatoria: **dos meses** antes de expirar el mandato (48.3)", "Mandato: **5 años**, renovable **una vez** por igual período (48.5)"],
         "Recurso: directamente ante la **Sala de lo Contencioso-administrativo de la Audiencia Nacional** (48.6). Mandato de **cinco** años (el RGPD exige una duración {cR(54, 'no inferior a cuatro años')}: art. 54.1 d)."))}

{unidad("2.5 Las circulares de la AEPD (LO 3/2018, art. 55; RD 389/2021, art. 6)",
  L(55, ["«Circulares de la Agencia Española de Protección de Datos»", "Las circulares serán obligatorias una vez publicadas en el Boletín Oficial del Estado"]),
  lit("RD389", "a6", ["suscrito por la persona titular de la Adjuntía a la Presidencia de la Agencia Española de Protección de Datos o el Subdirector General o Director de División correspondiente", "plazo mínimo de quince días hábiles", "hasta un mínimo de siete días hábiles", "Se recabará el dictamen del Consejo de Estado", "sin que en ningún caso sea posible la delegación de esta facultad"]),
  fichab("Potestad normativa de la AEPD",
         ["La **Presidencia** de la AEPD dicta las circulares y las aprueba **sin posibilidad de delegación** (55.1 LO; 6.9 RD)", "El informe técnico inicial lo suscribe la persona titular de la **Adjuntía** a la Presidencia **o** el **Subdirector General o Director de División** correspondiente (6.2 RD)"],
         ["Fijan los **criterios** de actuación de la Agencia al aplicar el RGPD y la LO 3/2018 (55.1)", "Trámites: **informe técnico** (normas habilitantes, justificación y proyecto) → **informe jurídico** del Gabinete Jurídico → **audiencia e información pública** en la web → **dictamen del Consejo de Estado** → aprobación final por la Presidencia → publicación en el **BOE** (6.2 a 6.10 RD)"],
         ["Audiencia e información pública: mínimo **15 días hábiles**, reducible a **7** por razones motivadas (6.4 RD)", "Obligatorias una vez **publicadas en el BOE** (55.3 LO)"],
         "Quién suscribe el informe técnico: Adjuntía **o** Subdirector General **o** Director de División (preguntas oficiales L 40 y P 37, → Cierre 1). La aprobación final es **indelegable**."))}

{unidad("2.6 Autoridades autonómicas de protección de datos (LO 3/2018, art. 57)",
  L(57, ["entidades integrantes del sector público de la correspondiente Comunidad Autónoma o de las Entidades Locales", "con el alcance y los efectos establecidos para la Agencia Española de Protección de Datos en el artículo 55"]),
  fichab("Autoridades de las Comunidades Autónomas",
         "Las **autoridades autonómicas** de protección de datos, de acuerdo con la normativa autonómica",
         ["Ejercen las funciones y potestades de los arts. 57 y 58 RGPD sobre: tratamientos del **sector público autonómico** y de las **entidades locales** de su territorio (a); funciones públicas en materias de **competencia autonómica o local** (b); lo previsto en sus **Estatutos de Autonomía** (c) (57.1)", "Pueden dictar **circulares** con el mismo alcance que las de la AEPD (57.2)"],
         "—",
         "Su ámbito: el **sector público** autonómico y **local** de su territorio, las **funciones públicas** en materias de su competencia y lo previsto en su **Estatuto**."))}

{resumen([
  "**Delegado**: obligatorio en las **autoridades y organismos públicos** (salvo tribunales en función judicial) y en las entidades del art. 34.1 LO 3/2018; designación y cese se comunican en **diez días**.",
  "Delegado **independiente**: sin instrucciones; no removible por sus funciones **salvo dolo o negligencia grave**; responde al afectado en **dos meses** y a la autoridad en **un mes**.",
  "**AEPD**: autoridad administrativa **independiente**, relacionada con el Gobierno por el **Ministerio de Justicia**; Presidencia con mandato de **cinco años** renovable una vez, ratificada por **3/5** (o mayoría absoluta) de la **Comisión de Justicia**; recurso ante la **Audiencia Nacional**.",
  "**Circulares**: obligatorias tras su publicación en el **BOE**; audiencia mínima de **15 días hábiles** (reducible a 7). Autoridades **autonómicas**: sector público autonómico y local."],
  "Siguiente: VI. ¿Qué derechos digitales reconoce la ley?")}
""", 2)

# =============================================================================
T.ap("bVI", "VI. ¿Qué derechos digitales reconoce la ley? (LO 3/2018, título X, arts. 79 a 97)", donde(
  "Sexta pregunta. El título X de la LO 3/2018 garantiza los **derechos digitales**: unos generales en Internet, otros propios del **ámbito laboral** y otros sobre la **memoria digital** (olvido, portabilidad en redes y testamento digital).",
  ["1 Derechos en la era digital (arts. 79 a 83)", "2 Menores, rectificación y actualización en Internet (arts. 84 a 86)", "3 Derechos digitales en el ámbito laboral (arts. 87 a 91)", "4 Menores en Internet, olvido, portabilidad en redes y testamento digital (arts. 92 a 97)"]))

T.ap("s15", "VI.1 Derechos en la era digital (arts. 79 a 83)", f"""
{unidad("1.1 Los derechos en la Era digital (art. 79)",
  L(79, ["son plenamente aplicables en Internet"]),
  fichab("Cláusula general del título X",
         "Los **prestadores de servicios de la sociedad de la información** y los **proveedores de servicios de Internet** contribuyen a garantizarlos",
         "Los derechos y libertades de la **Constitución** y de los **Tratados y Convenios Internacionales** en que España sea parte son **plenamente aplicables en Internet**",
         "—",
         "No crea derechos nuevos: proclama que los existentes valen **también en Internet**."))}

{unidad("1.2 Neutralidad, acceso universal y seguridad digital (arts. 80 a 82)",
  L(80, ["sin discriminación por motivos técnicos o económicos"]),
  L(81, ["independientemente de su condición personal, social, económica o geográfica", "universal, asequible, de calidad y no discriminatorio", "la brecha de género", "la brecha generacional", "entornos rurales"]),
  L(82, ["derecho a la seguridad de las comunicaciones"]),
  ficha(["Los **usuarios** (neutralidad y seguridad)", "**Todos** (acceso a Internet)"],
        ["**Neutralidad**: oferta **transparente** de servicios **sin discriminación** por motivos técnicos o económicos (art. 80)", "**Acceso universal**: independientemente de la condición personal, social, económica o geográfica; **universal, asequible, de calidad y no discriminatorio** (art. 81)", "**Seguridad digital** de las comunicaciones transmitidas y recibidas por Internet (art. 82)"],
        "—",
        "El acceso procurará superar la brecha de **género** y la **generacional**, y atenderá a los **entornos rurales** y a las **necesidades especiales** (81.3 a 6)",
        "Obligados en neutralidad y seguridad: los **proveedores de servicios de Internet**."))}

{unidad("1.3 Derecho a la educación digital (art. 83)",
  L(83, ["El sistema educativo garantizará la plena inserción del alumnado en la sociedad digital", "incorporarán a los temarios de las pruebas de acceso a los cuerpos superiores"]),
  ficha("El **alumnado**; también el **profesorado** (formación) y los **estudiantes universitarios**",
        ["El sistema educativo garantiza la **plena inserción** del alumnado en la sociedad digital y el aprendizaje de un **consumo responsable** y un **uso crítico y seguro** de los medios digitales (83.1)", "El profesorado recibe las **competencias digitales** necesarias (83.2); los planes de estudio universitarios garantizan formación en seguridad digital y derechos en Internet (83.3)"],
        "—",
        "—",
        "Art. 83.4: las Administraciones incorporan a los **temarios** de acceso a los **cuerpos superiores** (y a los que acceden a datos personales) la garantía de los **derechos digitales** y la **protección de datos**."))}
""", 2)

T.ap("s16", "VI.2 Menores, rectificación y actualización en Internet (arts. 84 a 86)", f"""
{unidad("2.1 Protección de los menores en Internet (art. 84)",
  L(84, ["uso equilibrado y responsable de los dispositivos digitales", "determinará la intervención del Ministerio Fiscal"]),
  ficha("Los **menores de edad**",
        "Padres, madres, tutores, curadores o representantes legales **procurarán** un uso **equilibrado y responsable** de dispositivos y servicios (84.1)",
        "—",
        "Si se difunden imágenes o información de menores en **redes sociales** que puedan suponer una intromisión ilegítima: intervención del **Ministerio Fiscal**, con las medidas de la LO 1/1996 (84.2)",
        "Quien actúa ante la difusión ilegítima: el **Ministerio Fiscal**."))}

{unidad("2.2 Rectificación en Internet y actualización en medios digitales (arts. 85 y 86)",
  L(85, ["Todos tienen derecho a la libertad de expresión en Internet", "adoptarán protocolos adecuados", "un aviso aclaratorio"]),
  L(86, ["la inclusión de un aviso de actualización suficientemente visible"]),
  ficha(["**Todos** (libertad de expresión en Internet)", "**Toda persona** respecto de las noticias que le conciernan (actualización)"],
        ["**Libertad de expresión** en Internet (85.1)", "**Rectificación**: las redes sociales adoptan **protocolos** para ejercerla frente a usuarios que difundan contenidos contra el honor, la intimidad o la información veraz, según la **LO 2/1984** (85.2)", "**Actualización**: pedir **motivadamente** a los medios digitales un **aviso de actualización** visible cuando la noticia ya no refleje la situación actual y cause perjuicio (art. 86)"],
        "La actualización procede, en particular, si la noticia trataba de actuaciones **policiales o judiciales** luego afectadas **en beneficio** del interesado por decisiones judiciales posteriores (86, párrafo segundo)",
        "Los medios digitales que deban rectificar publican en sus archivos un **aviso aclaratorio** junto a la información original (85.2, párrafo segundo)",
        "Rectificación (85) ≠ actualización (86): la actualización no corrige un error, sino que **añade un aviso** porque la situación **ha cambiado**."))}
""", 2)

T.ap("s17", "VI.3 Derechos digitales en el ámbito laboral (arts. 87 a 91)", f"""
{unidad("3.1 Intimidad y uso de dispositivos digitales (art. 87)",
  L(87, ["Los trabajadores y los empleados públicos", "a los solos efectos de controlar el cumplimiento de las obligaciones laborales o estatutarias", "deberán participar los representantes de los trabajadores"]),
  ficha("**Trabajadores** y **empleados públicos**",
        "Protección de su **intimidad** en el uso de los **dispositivos digitales** que les facilita el empleador (87.1)",
        ["El empleador puede acceder a los contenidos **solo** para **controlar el cumplimiento** de las obligaciones y garantizar la **integridad** de los dispositivos (87.2)", "Si admite el **uso privado**, debe especificar los **usos autorizados** y establecer **garantías** (87.3)"],
        "**Criterios de utilización** fijados por el empleador con participación de los **representantes** de los trabajadores, e **información** a los trabajadores (87.3)",
        "Incluye expresamente a los **empleados públicos**."))}

{unidad("3.2 Derecho a la desconexión digital (art. 88)",
  L(88, ["tendrán derecho a la desconexión digital", "fuera del tiempo de trabajo legal o convencionalmente establecido, el respeto de su tiempo de descanso, permisos y vacaciones, así como de su intimidad personal y familiar", "previa audiencia de los representantes de los trabajadores", "incluidos los que ocupen puestos directivos", "trabajo a distancia"]),
  ficha("**Trabajadores** y **empleados públicos**",
        "Desconexión digital para garantizar, **fuera del tiempo de trabajo**, el respeto de su **tiempo de descanso, permisos y vacaciones** y de su **intimidad personal y familiar** (88.1)",
        "Modalidades según la **naturaleza y objeto** de la relación laboral; se sujetan a la **negociación colectiva** o, en su defecto, al **acuerdo** entre la empresa y los representantes (88.2)",
        ["**Política interna** del empleador, **previa audiencia** de los representantes, dirigida también a los **directivos**, con formación sobre el riesgo de **fatiga informática** (88.3)", "Se preserva también en el **trabajo a distancia** total o parcial y en el **domicilio** (88.3)"],
        "Es un **derecho** de todos los trabajadores **y** empleados públicos (no solo funcionarios), no un principio programático, y no prohíbe toda comunicación: sus modalidades las fija la **negociación colectiva** (preguntas oficiales L 41 y P 35, → Cierre 1)."))}

{unidad("3.3 Videovigilancia, grabación de sonidos y geolocalización (arts. 89 y 90)",
  L(89, ["habrán de informar con carácter previo, y de forma expresa, clara y concisa", "En ningún caso se admitirá la instalación de sistemas de grabación de sonidos ni de videovigilancia en lugares destinados al descanso o esparcimiento", "se admitirá únicamente cuando resulten relevantes los riesgos para la seguridad"]),
  L(90, ["de forma expresa, clara e inequívoca"]),
  ficha("**Trabajadores** y **empleados públicos** (y sus representantes, que deben ser informados)",
        ["El empleador puede usar **cámaras** y **geolocalización** para las funciones de **control** del art. 20.3 ET o de la legislación de función pública, dentro de su marco legal (89.1 y 90.1)"],
        ["**Nunca** cámaras ni grabación de sonidos en lugares de **descanso o esparcimiento**: vestuarios, aseos, comedores y análogos (89.2)", "**Sonidos**: solo ante riesgos **relevantes** para la seguridad, con **proporcionalidad** e **intervención mínima** (89.3)"],
        ["Información **previa** y **expresa, clara y concisa** (cámaras) o **expresa, clara e inequívoca** (geolocalización) (89.1 y 90.2)", "Si se capta un acto **ilícito flagrante**, basta el **dispositivo informativo** del art. 22.4 (89.1)"],
        "Vestuarios, aseos y comedores: «**en ningún caso**»."))}

{unidad("3.4 Derechos digitales en la negociación colectiva (art. 91)",
  L(91, ["podrán establecer garantías adicionales"]),
  fichab("Papel de los convenios",
         "Los **convenios colectivos**",
         "Pueden establecer **garantías adicionales** de los derechos relacionados con los datos de los trabajadores y de los derechos digitales en el ámbito laboral",
         "—",
         "Los convenios pueden establecer «**garantías adicionales**»."))}
""", 2)

T.ap("s18", "VI.4 Menores en Internet, olvido, portabilidad en redes y testamento digital (arts. 92 a 97)", f"""
{unidad("4.1 Protección de datos de los menores en Internet (art. 92)",
  L(92, ["garantizarán la protección del interés superior del menor", "deberán contar con el consentimiento del menor o sus representantes legales"]),
  ficha("Los **menores de edad**",
        "Centros educativos y quienes desarrollen actividades con menores garantizan su **interés superior** al publicar o difundir sus datos por servicios de la sociedad de la información",
        "—",
        "En **redes sociales** o servicios equivalentes: **consentimiento** del menor o de sus representantes legales, según el **art. 7** (→ II.2.5)",
        "Remite a la regla de los **catorce años** del art. 7."))}

{unidad("4.2 Derecho al olvido en buscadores y en redes sociales (arts. 93 y 94)",
  L(93, ["los motores de búsqueda en Internet eliminen de las listas de resultados", "inadecuados, inexactos, no pertinentes, no actualizados o excesivos", "aun cuando fuera lícita la conservación de la información publicada en el sitio web", "otros criterios de búsqueda distintos del nombre"]),
  L(94, ["a su simple solicitud", "en el ejercicio de actividades personales o domésticas", "durante su minoría de edad"]),
  ficha("**Toda persona**",
        ["**Buscadores**: eliminar de los resultados obtenidos **a partir de su nombre** los enlaces con información **inadecuada, inexacta, no pertinente, no actualizada o excesiva** (93.1)", "**Redes sociales**: suprimir **a su simple solicitud** los datos que **ella misma** facilitó (94.1), y los facilitados por **terceros** cuando sean inadecuados, inexactos, etc. (94.2)"],
        ["Se ponderan los **fines**, el **tiempo transcurrido** y la **naturaleza e interés público** de la información (93.1 y 94.2)", "No impide acceder a la información con **otros criterios de búsqueda** distintos del nombre (93.2)", "En redes, se exceptúan los datos facilitados por personas físicas en actividades **personales o domésticas** (94.2)"],
        "Datos facilitados durante la **minoría de edad**: supresión **sin dilación** a su **simple solicitud**, sin más requisitos (94.3)",
        "En buscadores, el derecho **subsiste** aunque la web de origen pueda conservar lícitamente la información (93.1)."))}

{unidad("4.3 Portabilidad en redes sociales (art. 95)",
  L(95, ["siempre que sea técnicamente posible", "sin difundirla a través de Internet"]),
  ficha("Los **usuarios** de redes sociales y servicios equivalentes",
        "**Recibir y transmitir** los contenidos que facilitaron, y que el prestador los **transmita directamente** a otro designado por el usuario",
        "Transmisión directa: **siempre que sea técnicamente posible**",
        "El prestador puede conservar copia, **sin difundirla**, si lo exige una **obligación legal**",
        "No confundir con la portabilidad del art. 20 RGPD (→ III.3.2): aquí son **contenidos** en redes sociales."))}

{unidad("4.4 Derecho al testamento digital (art. 96)",
  L(96, ["Las personas vinculadas al fallecido por razones familiares o de hecho, así como sus herederos", "cuando la persona fallecida lo hubiese prohibido expresamente o así lo establezca una ley", "El albacea testamentario", "por el Ministerio Fiscal", "deberá proceder sin dilación a la misma"], solo=[1, 2, 3, 4, 5, 6, 7, 8, 9]),
  ficha(["Personas vinculadas al fallecido por razones **familiares o de hecho** y sus **herederos** (a)", "El **albacea** o la persona o institución **designada** por el fallecido (b)", "Menores fallecidos: también sus representantes legales o el **Ministerio Fiscal** (c); personas con discapacidad: también quienes prestaban **apoyo** (d)"],
        ["**Acceder** a los contenidos de prestadores de servicios sobre personas fallecidas e impartir **instrucciones** sobre su utilización, destino o supresión (96.1)", "Decidir sobre el **mantenimiento o eliminación** de los **perfiles** en redes sociales (96.2)"],
        "No pueden acceder ni pedir modificación o eliminación si el fallecido lo **prohibió expresamente** o lo establece una **ley**; la prohibición no afecta al acceso de los **herederos** al **caudal relicto** (96.1 a)",
        "El prestador al que se pide eliminar el perfil debe hacerlo **sin dilación** (96.2); requisitos de los mandatos e instrucciones, por **real decreto** (96.3)",
        "La **voluntad del fallecido** prevalece: si prohibió el acceso o decidió sobre sus perfiles, se estará a ella."))}

{unidad("4.5 Políticas de impulso de los derechos digitales (art. 97)",
  L(97, ["un Plan de Acceso a Internet", "un bono social de acceso a Internet", "un Plan de Actuación", "un informe anual ante la comisión parlamentaria correspondiente del Congreso de los Diputados"]),
  fichab("Mandatos al Gobierno",
         "El **Gobierno**, en colaboración con las **comunidades autónomas** (Plan de Acceso)",
         ["**Plan de Acceso a Internet**: superar brechas digitales (entre otras medidas, un **bono social**), espacios de conexión de acceso público y formación digital (97.1)", "**Plan de Actuación** para un uso equilibrado y responsable de dispositivos y redes por los **menores** (97.2)"],
         "**Informe anual** ante la comisión parlamentaria correspondiente del **Congreso** (97.3)",
         "Dos planes (**Acceso a Internet** y **Actuación** para menores) y un **informe anual** al Congreso."))}

{resumen([
  "Los derechos constitucionales son **plenamente aplicables en Internet** (art. 79): neutralidad, acceso universal, seguridad y **educación digital** (arts. 80 a 83).",
  "Menores: intervención del **Ministerio Fiscal** ante difusiones ilegítimas (art. 84); en redes, consentimiento según el **art. 7** (art. 92).",
  "Ámbito laboral (trabajadores **y empleados públicos**): intimidad en dispositivos, **desconexión digital** (política interna previa audiencia de los representantes), cámaras **nunca** en vestuarios o aseos, geolocalización con información previa.",
  "Memoria digital: **olvido** en buscadores (por el **nombre**) y en redes (a **simple solicitud**), portabilidad en redes y **testamento digital**."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX = [
 ("L", 40, "Circulares de la AEPD: informe técnico (→ V.2.5)", {
   "a": f"Se queda corto: además de la Adjuntía, el informe puede suscribirlo {c('RD389', 'a6', 'o el Subdirector General o Director de División correspondiente')}; la norma no dice «únicamente».",
   "b": f"Añade un requisito que no existe: el informe no necesita la aprobación de la Presidencia. La Presidencia interviene al final: {c('RD389', 'a6', 'el proyecto de circular será sometido a la aprobación final de la Presidencia de la Agencia Española de Protección de Datos')} (art. 6.9).",
   "c": f"Omite la otra alternativa: el informe puede estar {c('RD389', 'a6', 'suscrito por la persona titular de la Adjuntía a la Presidencia')}; tampoco dice «únicamente».",
   "d": f"Literal del art. 6.2: {c('RD389', 'a6', 'suscrito por la persona titular de la Adjuntía a la Presidencia de la Agencia Española de Protección de Datos o el Subdirector General o Director de División correspondiente')}."},
   [("Adjuntía a la Presidencia", "RD389", "a6", "suscrito por la persona titular de la Adjuntía a la Presidencia"),
    ("Subdirector General", "RD389", "a6", "o el Subdirector General o Director de División correspondiente"),
    ("Director de División", "RD389", "a6", "Director de División correspondiente")]),
 ("P", 37, "Circulares de la AEPD: informe técnico (misma pregunta que la L 40) (→ V.2.5)", {
   "a": f"Se queda corto: además de la Adjuntía, el informe puede suscribirlo {c('RD389', 'a6', 'o el Subdirector General o Director de División correspondiente')}; la norma no dice «únicamente».",
   "b": f"Añade un requisito que no existe: el informe no necesita la aprobación de la Presidencia. La Presidencia interviene al final: {c('RD389', 'a6', 'el proyecto de circular será sometido a la aprobación final de la Presidencia de la Agencia Española de Protección de Datos')} (art. 6.9).",
   "c": f"Omite la otra alternativa: el informe puede estar {c('RD389', 'a6', 'suscrito por la persona titular de la Adjuntía a la Presidencia')}; tampoco dice «únicamente».",
   "d": f"Literal del art. 6.2: {c('RD389', 'a6', 'suscrito por la persona titular de la Adjuntía a la Presidencia de la Agencia Española de Protección de Datos o el Subdirector General o Director de División correspondiente')}."},
   [("Adjuntía a la Presidencia", "RD389", "a6", "suscrito por la persona titular de la Adjuntía a la Presidencia"),
    ("Subdirector General", "RD389", "a6", "o el Subdirector General o Director de División correspondiente"),
    ("Director de División", "RD389", "a6", "Director de División correspondiente")]),
 ("L", 41, "Desconexión digital (→ VI.3.2)", {
   "a": f"Cambia los titulares: el derecho es de {cL(88, 'Los trabajadores y los empleados públicos')}, no solo del personal funcionario.",
   "b": f"Literal del art. 88.1: {cL(88, 'a fin de garantizar, fuera del tiempo de trabajo legal o convencionalmente establecido, el respeto de su tiempo de descanso, permisos y vacaciones, así como de su intimidad personal y familiar')}.",
   "c": f"El art. 88 no prohíbe toda comunicación: remite las modalidades de ejercicio a {cL(88, 'lo establecido en la negociación colectiva o, en su defecto, a lo acordado entre la empresa y los representantes de los trabajadores')} (art. 88.2).",
   "d": f"Es un derecho exigible, no un principio programático: {cL(88, 'tendrán derecho a la desconexión digital')}, y el empleador {cL(88, 'elaborará una política interna')} (art. 88.3)."},
   [("tiempo de descanso", "LOPD", "Artículo 88", "el respeto de su tiempo de descanso"),
    ("intimidad personal y familiar", "LOPD", "Artículo 88", "de su intimidad personal y familiar"),
    ("fuera del tiempo de trabajo", "LOPD", "Artículo 88", "fuera del tiempo de trabajo")]),
 ("P", 35, "Desconexión digital (misma pregunta que la L 41) (→ VI.3.2)", {
   "a": f"Cambia los titulares: el derecho es de {cL(88, 'Los trabajadores y los empleados públicos')}, no solo del personal funcionario.",
   "b": f"Literal del art. 88.1: {cL(88, 'a fin de garantizar, fuera del tiempo de trabajo legal o convencionalmente establecido, el respeto de su tiempo de descanso, permisos y vacaciones, así como de su intimidad personal y familiar')}.",
   "c": f"El art. 88 no prohíbe toda comunicación: remite las modalidades de ejercicio a {cL(88, 'lo establecido en la negociación colectiva o, en su defecto, a lo acordado entre la empresa y los representantes de los trabajadores')} (art. 88.2).",
   "d": f"Es un derecho exigible, no un principio programático: {cL(88, 'tendrán derecho a la desconexión digital')}, y el empleador {cL(88, 'elaborará una política interna')} (art. 88.3)."},
   [("tiempo de descanso", "LOPD", "Artículo 88", "el respeto de su tiempo de descanso"),
    ("intimidad personal y familiar", "LOPD", "Artículo 88", "de su intimidad personal y familiar"),
    ("fuera del tiempo de trabajo", "LOPD", "Artículo 88", "fuera del tiempo de trabajo")]),
 ("X", 49, "Derecho a la portabilidad (→ III.3.2)", {
   "a": f"El derecho de acceso es otro: {cR(15, 'derecho a obtener del responsable del tratamiento confirmación de si se están tratando o no datos personales que le conciernen')} (art. 15.1).",
   "b": f"Es la definición literal del art. 20.1, y el art. 20.2 le da nombre: {cR(20, 'Al ejercer su derecho a la portabilidad de los datos de acuerdo con el apartado 1')}.",
   "c": f"La limitación consiste en {cR(18, 'obtener del responsable del tratamiento la limitación del tratamiento de los datos')} en los casos del art. 18.1, no en recibir y transmitir los datos.",
   "d": f"La supresión es {cR(17, 'obtener sin dilación indebida del responsable del tratamiento la supresión de los datos personales que le conciernan')} (art. 17.1), no su transmisión a otro responsable."},
   [("portabilidad de los datos", "RGPD", "Artículo 20", "Al ejercer su derecho a la portabilidad de los datos de acuerdo con el apartado 1")]),
 ("X", 50, "Comunicación del delegado de protección de datos (→ V.1.1)", {
   "a": f"Literal del art. 34.3: {cL(34, 'Los responsables y encargados del tratamiento comunicarán en el plazo de diez días a la Agencia Española de Protección de Datos')}.",
   "b": "Cambia el plazo: treinta días no aparece en el art. 34.",
   "c": f"Cambia el plazo: un mes es el que tiene el delegado para responder a la reclamación que le remita la autoridad ({cL(37, 'a fin de que este responda en el plazo de un mes')}, art. 37.2), no el de comunicar su designación.",
   "d": "Cambia el plazo: quince días no aparece en el art. 34."},
   [("Diez días", "LOPD", "Artículo 34", "comunicarán en el plazo de diez días a la Agencia Española de Protección de Datos")]),
]
bloques = []
NOM = {"L": "GACE-L", "P": "GACE-P", "X": "GACE-L extraordinario"}
for cod, n, tit, por, ap_ in EX:
    bloques += [f"### {NOM[cod]} 2025, pregunta {n} · {tit}", examen(cod, n, por, ap_)]
T.ap("s19", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join(
  ["En los primeros ejercicios de **2025** cayeron **siete** preguntas de este tema (dos de ellas repetidas en el turno libre y en la promoción interna). Aquí están las **seis** que se pueden comprobar con el texto legal; todas son literales. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal.",
   "?> La pregunta **P 36** (principios rectores del Plan Estratégico de la AEPD 2025-2030) no está aquí: trata del contenido de un **plan** de la Agencia, no de una norma publicada en el BOE ni en el DOUE, y no se dispone de su texto oficial."]
  + bloques + ["### Cómo se pregunta", "!> Citan el **artículo** y cambian **un plazo** (diez días, quince, treinta, un mes), **quién** interviene (Adjuntía, Subdirector General, Presidencia), los **titulares** de un derecho (funcionarios frente a trabajadores y empleados públicos) o el **nombre** del derecho (acceso, portabilidad, limitación, supresión). Aprende los **plazos** y los **nombres literales**."]))

T.ap("s20", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Régimen jurídico | Art. 18.4 CE; **RGPD** (directamente aplicable) y **LO 3/2018** (lo adapta y completa; derechos digitales) | Fuera: lo **doméstico**, los **fallecidos**, las **materias clasificadas** |
| II. Principios | Siete principios (art. 5) y seis bases de licitud (art. 6) | **Minimización**; **responsabilidad proactiva**; consentimiento de menores: **14 años** |
| III. Derechos | Acceso, rectificación, supresión, limitación, portabilidad, oposición; decisiones automatizadas | Respuesta en **1 mes** (+2); acceso repetitivo: **6 meses**; reclamación sin respuesta: **3 meses** |
| IV. Responsable y encargado | Responsable decide fines y medios; encargado trata por su cuenta con contrato **escrito** | Brecha: **72 horas**; registro: **250** personas; subencargado con autorización **por escrito** |
| V. Delegado y autoridades | Delegado obligatorio en el **sector público**; AEPD independiente (Ministerio de **Justicia**) | Comunicación del delegado: **10 días**; mandato de la Presidencia: **5 años**; ratificación: **3/5**; recurso: **Audiencia Nacional** |
| VI. Derechos digitales | Título X: Internet, ámbito laboral, olvido, testamento digital | Desconexión: trabajadores **y empleados públicos**; cámaras **nunca** en vestuarios o aseos |

{ESQ}

?> **Trampas frecuentes:** «el consentimiento de los menores en España se presta a partir de los 16 años» (son **14**: art. 7 LO 3/2018); «la violación de seguridad se notifica en un mes» (**72 horas**); «la designación del delegado se comunica en un mes» (**diez días**; el mes es para responder a la reclamación que le remita la autoridad); «la desconexión digital es solo de los funcionarios» (trabajadores **y** empleados públicos); «la AEPD se relaciona con el Gobierno a través del Ministerio de Hacienda» (de **Justicia**); «el interés legítimo es una base válida para las autoridades públicas en sus funciones» (**no**: art. 6.1, párrafo segundo).
""")

# =============================================================================
Q = [
 ("CE", "Artículo 18", "Régimen jurídico", "Según el artículo 18.4 de la Constitución, la ley limitará el uso de la informática para garantizar:",
  ["El honor y la intimidad personal y familiar de los ciudadanos y el pleno ejercicio de sus derechos.", "El secreto de las comunicaciones postales, telegráficas y telefónicas.", "La libertad de expresión y el derecho a comunicar información veraz.", "La seguridad pública y la defensa nacional."], "Art. 18.4 CE.", "La ley limitará el uso de la informática para garantizar el honor y la intimidad personal y familiar de los ciudadanos y el pleno ejercicio de sus derechos"),
 ("RGPD", "Artículo 2", "Régimen jurídico", "Según el artículo 2.2 c) del Reglamento (UE) 2016/679, el Reglamento no se aplica al tratamiento de datos personales efectuado por una persona física en el ejercicio de actividades:",
  ["Exclusivamente personales o domésticas.", "Profesionales o empresariales.", "Asociativas o sindicales.", "De cualquier clase, siempre que no tengan ánimo de lucro."], "Art. 2.2 c) RGPD.", "efectuado por una persona física en el ejercicio de actividades exclusivamente personales o domésticas"),
 ("RGPD", "Artículo 4", "Régimen jurídico", "Según el artículo 4 del Reglamento (UE) 2016/679, el «encargado del tratamiento» es la persona física o jurídica, autoridad pública, servicio u otro organismo que:",
  ["Trate datos personales por cuenta del responsable del tratamiento.", "Determine los fines y medios del tratamiento.", "Supervise con total independencia la aplicación del Reglamento.", "Reciba la comunicación de datos personales, se trate o no de un tercero."], "Art. 4.8 RGPD (los fines y medios los determina el responsable: art. 4.7).", "que trate datos personales por cuenta del responsable del tratamiento"),
 ("RGPD", "Artículo 4", "Régimen jurídico", "Según el artículo 4.11 del Reglamento (UE) 2016/679, el consentimiento del interesado es toda manifestación de voluntad:",
  ["Libre, específica, informada e inequívoca.", "Libre, expresa y otorgada por escrito.", "Expresa, gratuita y revocable.", "Tácita o presunta, salvo oposición del interesado."], "Art. 4.11 RGPD; lo repite el art. 6.1 de la LO 3/2018.", "toda manifestación de voluntad libre, específica, informada e inequívoca"),
 ("RGPD", "Artículo 5", "Principios", "Según el artículo 5.1 c) del Reglamento (UE) 2016/679, que los datos personales sean adecuados, pertinentes y limitados a lo necesario en relación con los fines para los que son tratados constituye el principio de:",
  ["Minimización de datos.", "Limitación de la finalidad.", "Exactitud.", "Integridad y confidencialidad."], "Art. 5.1 c) RGPD.", "adecuados, pertinentes y limitados a lo necesario en relación con los fines para los que son tratados («minimización de datos»)"),
 ("RGPD", "Artículo 5", "Principios", "Según el artículo 5.2 del Reglamento (UE) 2016/679, que el responsable del tratamiento sea responsable del cumplimiento de los principios y capaz de demostrarlo se denomina:",
  ["Responsabilidad proactiva.", "Lealtad y transparencia.", "Limitación del plazo de conservación.", "Limitación de la finalidad."], "Art. 5.2 RGPD.", "El responsable del tratamiento será responsable del cumplimiento de lo dispuesto en el apartado 1 y capaz de demostrarlo («responsabilidad proactiva»)"),
 ("RGPD", "Artículo 6", "Principios", "Según el artículo 6.1 del Reglamento (UE) 2016/679, la base de licitud que NO es de aplicación al tratamiento realizado por las autoridades públicas en el ejercicio de sus funciones es:",
  ["La satisfacción de intereses legítimos perseguidos por el responsable del tratamiento o por un tercero.", "El cumplimiento de una obligación legal aplicable al responsable del tratamiento.", "El cumplimiento de una misión realizada en interés público.", "La protección de intereses vitales del interesado o de otra persona física."], "Art. 6.1, párrafo segundo, RGPD.", "Lo dispuesto en la letra f) del párrafo primero no será de aplicación al tratamiento realizado por las autoridades públicas en el ejercicio de sus funciones"),
 ("RGPD", "Artículo 7", "Principios", "Según el artículo 7.3 del Reglamento (UE) 2016/679, la retirada del consentimiento:",
  ["No afectará a la licitud del tratamiento basada en el consentimiento previo a su retirada.", "Anula con efectos retroactivos todo el tratamiento anterior.", "Solo es posible transcurrido un mes desde que se otorgó.", "Exige que el interesado acredite un motivo legítimo."], "Art. 7.3 RGPD: se puede retirar en cualquier momento y será tan fácil retirarlo como darlo.", "La retirada del consentimiento no afectará a la licitud del tratamiento basada en el consentimiento previo a su retirada"),
 ("RGPD", "Artículo 8", "Principios", "Según el artículo 8.1 del Reglamento (UE) 2016/679, los Estados miembros podrán establecer por ley una edad inferior a 16 años para el consentimiento de los niños en relación con los servicios de la sociedad de la información, siempre que no sea inferior a:",
  ["13 años.", "12 años.", "15 años.", "10 años."], "Art. 8.1, párrafo segundo, RGPD (España ha fijado 14: art. 7 LO 3/2018).", "siempre que esta no sea inferior a 13 años"),
 ("LOPD", "Artículo 7", "Principios", "Según el artículo 7.1 de la Ley Orgánica 3/2018, el tratamiento de los datos personales de un menor de edad únicamente podrá fundarse en su consentimiento cuando sea:",
  ["Mayor de catorce años.", "Mayor de trece años.", "Mayor de dieciséis años.", "Mayor de doce años."], "Art. 7.1 LO 3/2018.", "únicamente podrá fundarse en su consentimiento cuando sea mayor de catorce años"),
 ("LOPD", "Artículo 6", "Principios", "Según el artículo 6.3 de la Ley Orgánica 3/2018, la ejecución del contrato:",
  ["No podrá supeditarse a que el afectado consienta el tratamiento de los datos personales para finalidades que no guarden relación con el mantenimiento, desarrollo o control de la relación contractual.", "Podrá supeditarse al consentimiento para cualquier finalidad si así consta por escrito.", "Podrá supeditarse al consentimiento para fines publicitarios del responsable.", "Exige en todo caso el consentimiento expreso del afectado para todas las finalidades del responsable."], "Art. 6.3 LO 3/2018.", "No podrá supeditarse la ejecución del contrato a que el afectado consienta el tratamiento de los datos personales para finalidades que no guarden relación con el mantenimiento, desarrollo o control de la relación contractual"),
 ("LOPD", "Artículo 8", "Principios", "Según el artículo 8.2 de la Ley Orgánica 3/2018, el tratamiento de datos personales solo podrá considerarse fundado en el cumplimiento de una misión realizada en interés público o en el ejercicio de poderes públicos conferidos al responsable cuando:",
  ["Derive de una competencia atribuida por una norma con rango de ley.", "Lo autorice una orden ministerial.", "Lo prevea cualquier disposición reglamentaria.", "Lo acuerde el delegado de protección de datos."], "Art. 8.2 LO 3/2018.", "cuando derive de una competencia atribuida por una norma con rango de ley"),
 ("LOPD", "Artículo 9", "Principios", "Según el artículo 9.1 de la Ley Orgánica 3/2018, para levantar la prohibición del tratamiento de datos cuya finalidad principal sea identificar la ideología, afiliación sindical, religión, orientación sexual, creencias u origen racial o étnico del afectado:",
  ["El solo consentimiento del afectado no bastará.", "Bastará el consentimiento expreso y por escrito del afectado.", "Bastará la autorización de la Agencia Española de Protección de Datos.", "Bastará el consentimiento de los titulares de la patria potestad."], "Art. 9.1 LO 3/2018 (a fin de evitar situaciones discriminatorias).", "el solo consentimiento del afectado no bastará para levantar la prohibición del tratamiento de datos cuya finalidad principal sea identificar su ideología"),
 ("RGPD", "Artículo 9", "Principios", "Según el artículo 9.1 del Reglamento (UE) 2016/679, ¿cuál de los siguientes NO figura entre las categorías especiales de datos cuyo tratamiento queda prohibido?",
  ["Los datos de localización.", "La afiliación sindical.", "Los datos genéticos.", "Los datos relativos a la salud."], "Art. 9.1 RGPD (los datos de localización aparecen en la definición de dato personal, art. 4.1).", "o la afiliación sindical, y el tratamiento de datos genéticos, datos biométricos dirigidos a identificar de manera unívoca a una persona física, datos relativos a la salud"),
 ("RGPD", "Artículo 12", "Derechos", "Según el artículo 12.3 del Reglamento (UE) 2016/679, el responsable facilitará al interesado información relativa a sus actuaciones sobre una solicitud de ejercicio de derechos en el plazo de:",
  ["Un mes a partir de la recepción de la solicitud, prorrogable otros dos meses en caso necesario.", "Diez días, prorrogables otros diez.", "Dos meses, prorrogables otro mes.", "Tres meses, sin posibilidad de prórroga."], "Art. 12.3 RGPD.", "en el plazo de un mes a partir de la recepción de la solicitud. Dicho plazo podrá prorrogarse otros dos meses en caso necesario"),
 ("RGPD", "Artículo 14", "Derechos", "Según el artículo 14.3 a) del Reglamento (UE) 2016/679, cuando los datos personales no se hayan obtenido del interesado, el responsable le facilitará la información dentro de un plazo razonable, una vez obtenidos los datos, y a más tardar:",
  ["Dentro de un mes.", "Dentro de diez días.", "Dentro de tres meses.", "Dentro de seis meses."], "Art. 14.3 a) RGPD. Si los datos se obtienen del propio interesado, la información se da en el momento de obtenerlos (art. 13.1).", "y a más tardar dentro de un mes"),
 ("LOPD", "Artículo 13", "Derechos", "Según el artículo 13.3 de la Ley Orgánica 3/2018, a efectos del artículo 12.5 del RGPD se podrá considerar repetitivo el ejercicio del derecho de acceso en más de una ocasión durante el plazo de:",
  ["Seis meses, a menos que exista causa legítima para ello.", "Un mes.", "Tres meses, en todo caso.", "Un año, en todo caso."], "Art. 13.3 LO 3/2018.", "en más de una ocasión durante el plazo de seis meses, a menos que exista causa legítima para ello"),
 ("RGPD", "Artículo 17", "Derechos", "Según el artículo 17.3 del Reglamento (UE) 2016/679, el derecho de supresión no se aplicará cuando el tratamiento sea necesario:",
  ["Para ejercer el derecho a la libertad de expresión e información.", "Para fines de mercadotecnia directa.", "Para satisfacer intereses comerciales del responsable.", "Para mejorar la calidad del servicio del responsable."], "Art. 17.3 a) RGPD.", "para ejercer el derecho a la libertad de expresión e información"),
 ("RGPD", "Artículo 20", "Derechos", "Según el artículo 20.3 del Reglamento (UE) 2016/679, el derecho a la portabilidad de los datos no se aplicará:",
  ["Al tratamiento que sea necesario para el cumplimiento de una misión realizada en interés público o en el ejercicio de poderes públicos conferidos al responsable.", "Al tratamiento basado en el consentimiento del interesado.", "Al tratamiento basado en un contrato en el que el interesado es parte.", "Al tratamiento efectuado por medios automatizados."], "Art. 20.3 RGPD (el consentimiento, el contrato y los medios automatizados son precisamente sus requisitos: art. 20.1).", "Tal derecho no se aplicará al tratamiento que sea necesario para el cumplimiento de una misión realizada en interés público o en el ejercicio de poderes públicos conferidos al responsable del tratamiento"),
 ("RGPD", "Artículo 21", "Derechos", "Según el artículo 21.3 del Reglamento (UE) 2016/679, cuando el interesado se oponga al tratamiento con fines de mercadotecnia directa:",
  ["Los datos personales dejarán de ser tratados para dichos fines.", "El responsable podrá seguir tratándolos si acredita motivos legítimos imperiosos.", "Los datos quedarán limitados durante tres meses.", "El responsable deberá pedir autorización a la autoridad de control para seguir tratándolos."], "Art. 21.3 RGPD.", "los datos personales dejarán de ser tratados para dichos fines"),
 ("RGPD", "Artículo 22", "Derechos", "Según el artículo 22.3 del Reglamento (UE) 2016/679, en las decisiones automatizadas necesarias para un contrato o basadas en el consentimiento explícito, el responsable adoptará medidas adecuadas que incluyan, como mínimo:",
  ["El derecho a obtener intervención humana por parte del responsable, a expresar su punto de vista y a impugnar la decisión.", "La autorización previa de la autoridad de control.", "El informe previo del delegado de protección de datos.", "Una evaluación de impacto anual."], "Art. 22.3 RGPD.", "como mínimo el derecho a obtener intervención humana por parte del responsable, a expresar su punto de vista y a impugnar la decisión"),
 ("RGPD", "Artículo 78", "Derechos", "Según el artículo 78.2 del Reglamento (UE) 2016/679, el interesado tendrá derecho a la tutela judicial efectiva si la autoridad de control competente no le informa sobre el curso o el resultado de la reclamación en el plazo de:",
  ["Tres meses.", "Un mes.", "Seis meses.", "Dos meses."], "Art. 78.2 RGPD.", "no informe al interesado en el plazo de tres meses sobre el curso o el resultado de la reclamación"),
 ("RGPD", "Artículo 25", "Responsable y encargado", "Según el artículo 25.2 del Reglamento (UE) 2016/679, el responsable aplicará las medidas técnicas y organizativas apropiadas con miras a garantizar que, por defecto:",
  ["Solo sean objeto de tratamiento los datos personales que sean necesarios para cada uno de los fines específicos del tratamiento.", "Se traten todos los datos que el interesado facilite voluntariamente.", "Los datos sean accesibles a cualquier persona interesada.", "Los datos se conserven de manera indefinida."], "Art. 25.2 RGPD (protección de datos por defecto).", "por defecto, solo sean objeto de tratamiento los datos personales que sean necesarios para cada uno de los fines específicos del tratamiento"),
 ("RGPD", "Artículo 28", "Responsable y encargado", "Según el artículo 28.2 del Reglamento (UE) 2016/679, el encargado del tratamiento no recurrirá a otro encargado sin:",
  ["La autorización previa por escrito, específica o general, del responsable.", "La autorización de la autoridad de control.", "La comunicación posterior al interesado.", "El informe favorable del delegado de protección de datos."], "Art. 28.2 RGPD.", "sin la autorización previa por escrito, específica o general, del responsable"),
 ("LOPD", "Artículo 33", "Responsable y encargado", "Según el artículo 33.2 de la Ley Orgánica 3/2018, quien figurando como encargado del tratamiento utilizase los datos para sus propias finalidades:",
  ["Tendrá la consideración de responsable del tratamiento.", "Seguirá siendo encargado, con la obligación de informar al responsable.", "Tendrá la consideración de tercero destinatario de los datos.", "Será corresponsable solo si así se pacta por escrito."], "Art. 33.2, párrafo segundo, LO 3/2018.", "Tendrá asimismo la consideración de responsable del tratamiento quien figurando como encargado utilizase los datos para sus propias finalidades"),
 ("RGPD", "Artículo 30", "Responsable y encargado", "Según el artículo 30.5 del Reglamento (UE) 2016/679, la obligación de llevar el registro de las actividades de tratamiento no se aplica, salvo excepciones, a las empresas u organizaciones que empleen a menos de:",
  ["250 personas.", "50 personas.", "500 personas.", "100 personas."], "Art. 30.5 RGPD (sí deben llevarlo si el tratamiento entraña riesgo, no es ocasional o incluye categorías especiales o datos penales).", "a menos de 250 personas"),
 ("LOPD", "Artículo 31", "Responsable y encargado", "Según el artículo 31.2 de la Ley Orgánica 3/2018, los sujetos enumerados en su artículo 77.1:",
  ["Harán público un inventario de sus actividades de tratamiento accesible por medios electrónicos, en el que constará también su base legal.", "Quedan exentos de llevar el registro de actividades de tratamiento.", "Solo deben llevar el registro si emplean a 250 personas o más.", "Comunicarán cada año su registro al Defensor del Pueblo."], "Art. 31.2 LO 3/2018.", "harán público un inventario de sus actividades de tratamiento accesible por medios electrónicos en el que constará la información establecida en el artículo 30 del Reglamento (UE) 2016/679 y su base legal"),
 ("LOPD", "Artículo 32", "Responsable y encargado", "Según el artículo 32.1 de la Ley Orgánica 3/2018, el responsable del tratamiento estará obligado a bloquear los datos:",
  ["Cuando proceda a su rectificación o supresión.", "Cuando lo solicite cualquier tercero.", "Solo cuando lo ordene la autoridad de control.", "Cuando el afectado ejerza el derecho de acceso."], "Art. 32.1 LO 3/2018.", "estará obligado a bloquear los datos cuando proceda a su rectificación o supresión"),
 ("RGPD", "Artículo 33", "Responsable y encargado", "Según el artículo 33.1 del Reglamento (UE) 2016/679, el responsable notificará una violación de la seguridad de los datos personales a la autoridad de control competente sin dilación indebida y, de ser posible, a más tardar:",
  ["72 horas después de que haya tenido constancia de ella.", "24 horas después de que se haya producido.", "Diez días después de que haya tenido constancia de ella.", "Un mes después de que se haya producido."], "Art. 33.1 RGPD.", "a más tardar 72 horas después de que haya tenido constancia de ella"),
 ("RGPD", "Artículo 34", "Responsable y encargado", "Según el artículo 34.1 del Reglamento (UE) 2016/679, el responsable comunicará al interesado una violación de la seguridad de los datos personales cuando:",
  ["Sea probable que entrañe un alto riesgo para los derechos y libertades de las personas físicas.", "Se produzca cualquier violación, sea cual sea su riesgo.", "Lo ordene previamente un juez.", "Afecte a más de 250 interesados."], "Art. 34.1 RGPD.", "Cuando sea probable que la violación de la seguridad de los datos personales entrañe un alto riesgo para los derechos y libertades de las personas físicas"),
 ("RGPD", "Artículo 37", "Delegado y autoridades", "Según el artículo 37.1 a) del Reglamento (UE) 2016/679, el responsable y el encargado designarán un delegado de protección de datos siempre que el tratamiento lo lleve a cabo una autoridad u organismo público, excepto:",
  ["Los tribunales que actúen en ejercicio de su función judicial.", "Las entidades locales.", "Los organismos autónomos.", "Las universidades públicas."], "Art. 37.1 a) RGPD.", "excepto los tribunales que actúen en ejercicio de su función judicial"),
 ("LOPD", "Artículo 34", "Delegado y autoridades", "Según el artículo 34.1 de la Ley Orgánica 3/2018, deberán designar en todo caso un delegado de protección de datos:",
  ["Los centros docentes que ofrezcan enseñanzas en cualquiera de los niveles establecidos en la legislación reguladora del derecho a la educación, así como las Universidades públicas y privadas.", "Los profesionales de la salud que ejerzan su actividad a título individual.", "Las federaciones deportivas, aunque no traten datos de menores de edad.", "Las personas físicas que traten datos en actividades exclusivamente domésticas."], "Art. 34.1 b) LO 3/2018 (los profesionales sanitarios individuales están exceptuados en la letra l; las federaciones, solo con datos de menores, letra o).", "así como las Universidades públicas y privadas"),
 ("LOPD", "Artículo 36", "Delegado y autoridades", "Según el artículo 36.2 de la Ley Orgánica 3/2018, el delegado de protección de datos persona física integrada en la organización del responsable no podrá ser removido ni sancionado por desempeñar sus funciones:",
  ["Salvo que incurriera en dolo o negligencia grave en su ejercicio.", "Salvo que lo autorice la Agencia Española de Protección de Datos.", "En ningún caso, ni siquiera por dolo.", "Salvo pérdida de confianza del responsable."], "Art. 36.2 LO 3/2018.", "salvo que incurriera en dolo o negligencia grave en su ejercicio"),
 ("LOPD", "Artículo 37", "Delegado y autoridades", "Según el artículo 37.1 de la Ley Orgánica 3/2018, si el afectado se dirige al delegado de protección de datos antes de reclamar ante la autoridad de protección de datos, el delegado le comunicará la decisión adoptada en el plazo máximo de:",
  ["Dos meses a contar desde la recepción de la reclamación.", "Un mes a contar desde la recepción de la reclamación.", "Diez días a contar desde la recepción de la reclamación.", "Tres meses a contar desde la recepción de la reclamación."], "Art. 37.1 LO 3/2018 (si la reclamación se la remite la autoridad, un mes: art. 37.2).", "en el plazo máximo de dos meses a contar desde la recepción de la reclamación"),
 ("LOPD", "Artículo 44", "Delegado y autoridades", "Según el artículo 44.1 de la Ley Orgánica 3/2018, la Agencia Española de Protección de Datos se relaciona con el Gobierno a través del:",
  ["Ministerio de Justicia.", "Ministerio de Hacienda.", "Ministerio del Interior.", "Ministerio de Asuntos Exteriores."], "Art. 44.1 LO 3/2018.", "Se relaciona con el Gobierno a través del Ministerio de Justicia"),
 ("LOPD", "Artículo 48", "Delegado y autoridades", "Según el artículo 48.5 de la Ley Orgánica 3/2018, el mandato de la Presidencia y del Adjunto de la Agencia Española de Protección de Datos tiene una duración de:",
  ["Cinco años, renovable para otro período de igual duración.", "Cuatro años, no renovable.", "Seis años, no renovable.", "Cinco años, no renovable."], "Art. 48.5 LO 3/2018.", "tiene una duración de cinco años y puede ser renovado para otro período de igual duración"),
 ("LOPD", "Artículo 48", "Delegado y autoridades", "Según el artículo 48.3 de la Ley Orgánica 3/2018, la propuesta de Presidencia y Adjunto de la Agencia Española de Protección de Datos deberá ser ratificada por la Comisión de Justicia del Congreso de los Diputados por mayoría de:",
  ["Tres quintos de sus miembros en primera votación o, de no alcanzarse, mayoría absoluta en segunda votación.", "Dos tercios de sus miembros en primera votación o mayoría absoluta en segunda.", "Mayoría absoluta en primera votación o mayoría simple en segunda.", "Mayoría simple en una única votación."], "Art. 48.3 LO 3/2018 (en segunda votación, con votos de al menos dos grupos parlamentarios).", "por mayoría de tres quintos de sus miembros en primera votación o, de no alcanzarse ésta, por mayoría absoluta en segunda votación"),
 ("LOPD", "Artículo 48", "Delegado y autoridades", "Según el artículo 48.6 de la Ley Orgánica 3/2018, los actos y disposiciones dictados por la Presidencia de la Agencia Española de Protección de Datos:",
  ["Ponen fin a la vía administrativa y son recurribles directamente ante la Sala de lo Contencioso-administrativo de la Audiencia Nacional.", "Son recurribles en alzada ante el Ministerio de Justicia.", "Ponen fin a la vía administrativa y son recurribles ante la Sala de lo Contencioso-administrativo del Tribunal Supremo.", "Son recurribles ante el Tribunal Superior de Justicia de Madrid."], "Art. 48.6 LO 3/2018.", "ponen fin a la vía administrativa, siendo recurribles, directamente, ante la Sala de lo Contencioso-administrativo de la Audiencia Nacional"),
 ("LOPD", "Artículo 55", "Delegado y autoridades", "Según el artículo 55.3 de la Ley Orgánica 3/2018, las Circulares de la Agencia Española de Protección de Datos serán obligatorias:",
  ["Una vez publicadas en el Boletín Oficial del Estado.", "Desde que las firma la Presidencia de la Agencia.", "Una vez dictaminadas por el Consejo de Estado.", "Una vez publicadas en la sede electrónica de la Agencia."], "Art. 55.3 LO 3/2018.", "Las circulares serán obligatorias una vez publicadas en el Boletín Oficial del Estado"),
 ("RD389", "a6", "Delegado y autoridades", "Según el artículo 6.4 del Real Decreto 389/2021, por el que se aprueba el Estatuto de la Agencia Española de Protección de Datos, el trámite de audiencia e información pública en la elaboración de las circulares tendrá un plazo mínimo de:",
  ["Quince días hábiles, que podrá reducirse hasta un mínimo de siete días hábiles cuando razones debidamente motivadas así lo justifiquen.", "Diez días hábiles, sin posibilidad de reducción.", "Un mes, que podrá reducirse hasta quince días.", "Veinte días naturales, que podrá reducirse hasta diez."], "Art. 6.4, párrafo segundo, RD 389/2021.", "tendrá un plazo mínimo de quince días hábiles, que podrá ser reducido hasta un mínimo de siete días hábiles cuando razones debidamente motivadas así lo justifiquen"),
 ("LOPD", "Artículo 88", "Derechos digitales", "Según el artículo 88.3 de la Ley Orgánica 3/2018, la política interna sobre el derecho a la desconexión digital la elaborará el empleador:",
  ["Previa audiencia de los representantes de los trabajadores.", "Previa autorización de la Inspección de Trabajo.", "Previo informe de la Agencia Española de Protección de Datos.", "Previo acuerdo unánime de la plantilla."], "Art. 88.3 LO 3/2018 (se dirige también a quienes ocupen puestos directivos).", "El empleador, previa audiencia de los representantes de los trabajadores, elaborará una política interna"),
 ("LOPD", "Artículo 89", "Derechos digitales", "Según el artículo 89.2 de la Ley Orgánica 3/2018, la instalación de sistemas de grabación de sonidos o de videovigilancia en lugares destinados al descanso o esparcimiento de los trabajadores, como vestuarios, aseos o comedores:",
  ["No se admitirá en ningún caso.", "Se admitirá con autorización judicial.", "Se admitirá si se informa previamente a los trabajadores.", "Se admitirá si lo autoriza el convenio colectivo."], "Art. 89.2 LO 3/2018.", "En ningún caso se admitirá la instalación de sistemas de grabación de sonidos ni de videovigilancia en lugares destinados al descanso o esparcimiento de los trabajadores"),
 ("LOPD", "Artículo 93", "Derechos digitales", "Según el artículo 93.2 de la Ley Orgánica 3/2018, el ejercicio del derecho al olvido en búsquedas de Internet:",
  ["No impedirá el acceso a la información publicada en el sitio web a través de otros criterios de búsqueda distintos del nombre de quien ejerciera el derecho.", "Obliga a borrar la información del sitio web de origen.", "Impide cualquier búsqueda de la información en Internet.", "Solo procede si la información publicada es ilícita."], "Art. 93.2 LO 3/2018 (el derecho subsiste aunque la conservación en la web de origen sea lícita: art. 93.1).", "no impedirá el acceso a la información publicada en el sitio web a través de la utilización de otros criterios de búsqueda distintos del nombre de quien ejerciera el derecho"),
 ("LOPD", "Artículo 94", "Derechos digitales", "Según el artículo 94.3 de la Ley Orgánica 3/2018, cuando el derecho al olvido en redes sociales se ejercite respecto de datos facilitados durante la minoría de edad del afectado, el prestador deberá proceder a su supresión:",
  ["Sin dilación, por su simple solicitud.", "Solo si los datos son inexactos o no pertinentes.", "Previa autorización del Ministerio Fiscal.", "En el plazo de tres meses desde la solicitud."], "Art. 94.3 LO 3/2018.", "el prestador deberá proceder sin dilación a su supresión por su simple solicitud"),
 ("LOPD", "Artículo 96", "Derechos digitales", "Según el artículo 96.1 a) de la Ley Orgánica 3/2018, las personas vinculadas al fallecido no podrán acceder a los contenidos del causante gestionados por prestadores de servicios de la sociedad de la información cuando:",
  ["La persona fallecida lo hubiese prohibido expresamente o así lo establezca una ley.", "No sean herederos del fallecido.", "Hayan transcurrido seis meses desde el fallecimiento.", "No lo autorice la Agencia Española de Protección de Datos."], "Art. 96.1 a), párrafo segundo, LO 3/2018 (la prohibición no afecta al acceso de los herederos al caudal relicto).", "cuando la persona fallecida lo hubiese prohibido expresamente o así lo establezca una ley"),
]
for k, art, cat, enun, ops, expl, frag in Q: T.q(k, art, cat, enun, ops, expl, frag)
for cod, n, *_ in EX: T.real(cod, n, "Preguntas oficiales")

for q_, a_, cat in [
  ("Fundamento constitucional", "Art. 18.4 CE: la ley limitará el uso de la informática para garantizar el honor, la intimidad personal y familiar y el pleno ejercicio de los derechos.", "Régimen jurídico"),
  ("Objeto de la LO 3/2018 (art. 1)", "Adaptar el ordenamiento español al RGPD y completar sus disposiciones; garantizar los derechos digitales.", "Régimen jurídico"),
  ("Responsable y encargado (art. 4 RGPD)", "Responsable: determina los fines y medios. Encargado: trata datos por cuenta del responsable.", "Régimen jurídico"),
  ("Principios del art. 5 RGPD", "Licitud, lealtad y transparencia; limitación de la finalidad; minimización; exactitud; limitación del plazo de conservación; integridad y confidencialidad; responsabilidad proactiva.", "Principios"),
  ("Bases de licitud (art. 6.1 RGPD)", "Consentimiento; contrato; obligación legal; intereses vitales; interés público o poderes públicos; interés legítimo (no para autoridades públicas en sus funciones).", "Principios"),
  ("Edad del consentimiento", "RGPD: 16 años (los Estados pueden bajarla, no por debajo de 13). España: mayores de 14 años (art. 7 LO 3/2018).", "Principios"),
  ("Categorías especiales (art. 9 LO 3/2018)", "El solo consentimiento no basta si la finalidad principal es identificar ideología, afiliación sindical, religión, orientación sexual, creencias u origen racial o étnico.", "Principios"),
  ("Información al interesado (arts. 13 y 14 RGPD)", "Datos recogidos del interesado: en el momento de obtenerlos. Datos no recogidos de él: en un plazo razonable y a más tardar dentro de un mes (o en la primera comunicación, o al comunicarlos por primera vez a otro destinatario), añadiendo categorías de datos y fuente.", "Derechos"),
  ("Plazo de respuesta a los derechos (art. 12.3 RGPD)", "Un mes desde la recepción, prorrogable otros dos meses.", "Derechos"),
  ("Acceso repetitivo (art. 13.3 LO 3/2018)", "Más de una vez en seis meses, salvo causa legítima.", "Derechos"),
  ("Portabilidad (art. 20 RGPD)", "Datos facilitados por el interesado, en formato estructurado, de uso común y lectura mecánica; si el tratamiento se basa en consentimiento o contrato y es automatizado; no en misiones de interés público.", "Derechos"),
  ("Reclamación sin respuesta (art. 78.2 RGPD)", "Tutela judicial si la autoridad de control no informa en tres meses.", "Derechos"),
  ("Encargado y subencargado (art. 28 RGPD)", "Contrato por escrito; instrucciones documentadas; subencargado con autorización previa por escrito, específica o general, del responsable.", "Responsable y encargado"),
  ("Registro de actividades (art. 30.5 RGPD; art. 31 LO 3/2018)", "Exentas las organizaciones de menos de 250 personas, salvo riesgo, tratamiento no ocasional o categorías especiales. Sector público: inventario público con base legal.", "Responsable y encargado"),
  ("Violación de la seguridad (arts. 33 y 34 RGPD)", "A la autoridad: 72 horas desde que se tuvo constancia. Al interesado: si hay alto riesgo, sin dilación indebida.", "Responsable y encargado"),
  ("Delegado obligatorio (art. 37 RGPD)", "Autoridades y organismos públicos (salvo tribunales en función judicial); observación habitual y sistemática a gran escala; categorías especiales a gran escala.", "Delegado y autoridades"),
  ("Comunicación del delegado (art. 34.3 LO 3/2018)", "Diez días, a la AEPD o a la autoridad autonómica, tanto si es obligatorio como voluntario.", "Delegado y autoridades"),
  ("Plazos del delegado ante reclamaciones (art. 37 LO 3/2018)", "Dos meses para responder al afectado; un mes si la autoridad le remite la reclamación.", "Delegado y autoridades"),
  ("AEPD (art. 44 LO 3/2018)", "Autoridad administrativa independiente de ámbito estatal; se relaciona con el Gobierno a través del Ministerio de Justicia; representante común en el Comité Europeo.", "Delegado y autoridades"),
  ("Presidencia de la AEPD (art. 48 LO 3/2018)", "Mandato de 5 años renovable una vez; ratificación por la Comisión de Justicia (3/5 o mayoría absoluta); nombramiento por real decreto; recurso ante la Audiencia Nacional.", "Delegado y autoridades"),
  ("Circulares de la AEPD", "Obligatorias tras su publicación en el BOE (art. 55 LO 3/2018). Informe técnico: Adjuntía o Subdirector General o Director de División; audiencia mínima de 15 días hábiles (art. 6 RD 389/2021).", "Delegado y autoridades"),
  ("Desconexión digital (art. 88 LO 3/2018)", "Trabajadores y empleados públicos; respeto del descanso, permisos, vacaciones e intimidad fuera del tiempo de trabajo; política interna previa audiencia de los representantes.", "Derechos digitales"),
  ("Derecho al olvido (arts. 93 y 94 LO 3/2018)", "Buscadores: enlaces obtenidos a partir del nombre. Redes sociales: supresión a simple solicitud de lo facilitado por uno mismo; sin requisitos si se facilitó siendo menor.", "Derechos digitales"),
  ("Testamento digital (art. 96 LO 3/2018)", "Familiares, personas vinculadas y herederos acceden y dan instrucciones, salvo prohibición expresa del fallecido o de una ley.", "Derechos digitales"),
]: T.fc(q_, a_, cat)

T.glos("Dato personal", "Toda información sobre una persona física identificada o identificable, «el interesado» (RGPD, art. 4.1).", "s2", "Régimen jurídico")
T.glos("Tratamiento", "Cualquier operación o conjunto de operaciones sobre datos personales, automatizada o no (RGPD, art. 4.2).", "s2", "Régimen jurídico")
T.glos("Responsable del tratamiento", "Quien, solo o junto con otros, determina los fines y medios del tratamiento (RGPD, art. 4.7).", "s10", "Responsable y encargado")
T.glos("Encargado del tratamiento", "Quien trata datos personales por cuenta del responsable (RGPD, art. 4.8; LO 3/2018, art. 33).", "s11", "Responsable y encargado")
T.glos("Consentimiento", "Manifestación de voluntad libre, específica, informada e inequívoca (RGPD, art. 4.11; LO 3/2018, art. 6.1).", "s4", "Principios")
T.glos("Responsabilidad proactiva", "Principio por el que el responsable cumple los principios y es capaz de demostrarlo (RGPD, art. 5.2).", "s3", "Principios")
T.glos("Minimización de datos", "Principio según el cual los datos han de ser adecuados, pertinentes y limitados a lo necesario para los fines (RGPD, art. 5.1 c).", "s3", "Principios")
T.glos("Categorías especiales de datos", "Datos sobre origen étnico o racial, opiniones políticas, convicciones religiosas o filosóficas, afiliación sindical, genéticos, biométricos identificativos, de salud o de vida y orientación sexual; su tratamiento está prohibido salvo excepciones (RGPD, art. 9).", "s5", "Principios")
T.glos("Portabilidad", "Derecho a recibir los datos facilitados en formato estructurado, de uso común y lectura mecánica y a transmitirlos a otro responsable (RGPD, art. 20).", "s8", "Derechos")
T.glos("Bloqueo de datos", "Identificación y reserva de los datos para impedir su tratamiento, salvo su puesta a disposición de jueces, Ministerio Fiscal y Administraciones competentes durante el plazo de prescripción (LO 3/2018, art. 32).", "s12", "Responsable y encargado")
T.glos("Violación de la seguridad de los datos personales", "Violación de la seguridad que ocasiona la destrucción, pérdida o alteración accidental o ilícita de datos, o su comunicación o acceso no autorizados (RGPD, art. 4.12); se notifica a la autoridad en 72 horas (art. 33).", "s12", "Responsable y encargado")
T.glos("Delegado de protección de datos", "Figura que informa, asesora y supervisa el cumplimiento dentro de la organización del responsable o encargado y es interlocutor ante la autoridad (RGPD, arts. 37 a 39; LO 3/2018, arts. 34 a 37).", "s13", "Delegado y autoridades")
T.glos("Autoridad de control", "Autoridad pública independiente que supervisa la aplicación del RGPD (RGPD, arts. 4.21 y 51); en España, la AEPD y las autoridades autonómicas.", "s14", "Delegado y autoridades")
T.glos("Circulares de la AEPD", "Disposiciones de la Presidencia de la AEPD que fijan los criterios de actuación de la Agencia; obligatorias tras su publicación en el BOE (LO 3/2018, art. 55; RD 389/2021, art. 6).", "s14", "Delegado y autoridades")
T.glos("Desconexión digital", "Derecho de trabajadores y empleados públicos a que se respete, fuera del tiempo de trabajo, su descanso, permisos, vacaciones e intimidad (LO 3/2018, art. 88).", "s17", "Derechos digitales")

T.hito("1978", "Constitución Española, art. 18.4", "La ley limitará el uso de la informática para garantizar el honor, la intimidad y el pleno ejercicio de los derechos", "normativo", "s1")
T.hito("2016", "Reglamento (UE) 2016/679, de 27 de abril de 2016 (RGPD)", "Entra en vigor a los veinte días de su publicación en el DOUE (art. 99.1)", "normativo", "s1")
T.hito("2018", "El RGPD es aplicable desde el 25 de mayo de 2018 (art. 99.2)", "Obligatorio en todos sus elementos y directamente aplicable en cada Estado miembro", "normativo", "s1")
T.hito("2018", "Ley Orgánica 3/2018, de 5 de diciembre (BOE de 6-12-2018; vigente desde el 7-12-2018)", "Adapta el ordenamiento español al RGPD y garantiza los derechos digitales", "normativo", "s1")
T.hito("2021", "Real Decreto 389/2021, de 1 de junio, Estatuto de la AEPD (BOE de 2-6-2021; vigente desde el 3-6-2021)", "Regula, entre otras cosas, el procedimiento de elaboración de las circulares (art. 6)", "normativo", "s14")

T.publicar()
