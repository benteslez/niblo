# -*- coding: utf-8 -*-
"""Tema III.7 (B3T07): El Gobierno Abierto: concepto, principios informadores y planes de
acción de España. La Ley 19/2013, de 9 de diciembre, de transparencia, acceso a la
información pública y buen gobierno.
Método del I.2: mapa → bloques (I a V) con guía; cada artículo, texto literal + ficha de
casillas fijas; cierre 1 (preguntas oficiales) y cierre 2 (repaso).
Normas (BOE): Ley 19/2013 (L19_2013); Real Decreto 615/2024, Estatuto del Consejo de
Transparencia y Buen Gobierno, A.A.I. (RD615); Real Decreto 371/2026, por el que se crea y
regula el Foro de Gobierno Abierto (RD371); CE, art. 105 b).
Fuentes oficiales que no son texto legal (Portal de la Transparencia, transparencia.gob.es,
etiqueta TRANSPARENCIA): «¿Qué es y cómo se organiza el Gobierno Abierto?», «Conoce los
Planes de Gobierno Abierto de España», página del V Plan y documento del V Plan de Gobierno
Abierto de España 2025-2029 (PDF). Se guardan en boe/GA_QUE.json, GA_PLANES.json y
GA_VPLAN.json (párrafos literales de las páginas descargadas)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *
from plantilla import _norm

CORTO["L19_2013"] = "Ley 19/2013"
CORTO["RD615"] = "Estatuto del CTBG, RD 615/2024"
CORTO["RD371"] = "RD 371/2026, Foro de Gobierno Abierto"
L = "L19_2013"

# --- Fuentes oficiales que no son texto legal -----------------------------------
PT = "https://transparencia.gob.es"
URL = {"GA_QUE": PT + "/gobierno-abierto/que-es_organizacion",
       "GA_PLANES": PT + "/gobierno-abierto/planes-accion",
       "GA_VPLAN": PT + "/content/dam/transparencia_home/gobierno-abierto/vpga/V%20PLAN.pdf"}
T_ = "Texto"


def doc(k, cab, frases, resaltar=()):
    """Bloque literal de una fuente oficial que no es texto legal: primera línea
    [[TRANSPARENCIA|url]], cabecera en negrita que lo dice y frases comprobadas una a una."""
    t = texto(k, T_)
    out = []
    for f in frases:
        assert _norm(f) in _norm(t), ("FUENTE NO LITERAL", k, f)
        for r in resaltar:
            if r in f and "**" + r not in f: f = f.replace(r, "**" + r + "**", 1)
        out.append(f)
    for r in resaltar: assert any(r in f for f in frases), ("NEGRITA NO LITERAL", k, r)
    return "\n".join([f"> [[TRANSPARENCIA|{URL[k]}]]", "> **" + cab + " · fuente oficial, no es texto legal**"] + ["> " + x for x in out])


def cs(k, frag): return c(k, T_, frag)


NOLEGAL = "*Esquema de elaboración propia: resume los artículos y documentos citados; no es texto legal.*"

T = Tema("B3T07",
  "Cinco preguntas: I. Qué es el Gobierno Abierto y qué principios lo informan (Portal de la Transparencia; RD 371/2026) · II. Qué planes de acción ha tenido España (I a V Plan) · III. Cómo se garantiza la transparencia: publicidad activa y derecho de acceso (Ley 19/2013, arts. 1 a 24) · IV. Qué exige el buen gobierno (arts. 25 a 32) · V. Quién vela por todo ello: el Consejo de Transparencia y Buen Gobierno (arts. 33 a 40 y Estatuto, RD 615/2024). Cada artículo: texto literal y ficha.",
  ["Gobierno Abierto", "OGP", "Planes de Gobierno Abierto", "V Plan 2025-2029", "Foro de Gobierno Abierto", "Ley 19/2013", "Publicidad activa", "Portal de la Transparencia", "Derecho de acceso", "Límites al acceso", "Silencio negativo", "Reclamación ante el CTBG", "Buen gobierno", "Infracciones y sanciones", "Consejo de Transparencia y Buen Gobierno", "RD 615/2024"])

# =============================================================================
T.ap("s0", "Mapa del tema: cinco preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque III, tema 7):
> El Gobierno Abierto: concepto, principios informadores y planes de acción de España. La Ley 19/2013, de 9 de diciembre, de transparencia, acceso a la información pública y buen gobierno.

### El hilo conductor

El epígrafe se lee como **cinco preguntas encadenadas**. Cada una es un bloque de los apuntes:

| Bloque | Pregunta | Normas | Otras fuentes oficiales |
|---|---|---|---|
| **I** | ¿Qué es el Gobierno Abierto y qué principios lo informan? | RD 371/2026 (preámbulo y arts. 2, 3, 5, 6, 12, 17 y 19); Ley 19/2013 (preámbulo) | Portal de la Transparencia: «¿Qué es y cómo se organiza el Gobierno Abierto?» |
| **II** | ¿Qué planes de acción ha tenido España? | RD 371/2026 (preámbulo) | Portal de la Transparencia: planes de acción; documento del V Plan 2025-2029 |
| **III** | ¿Cómo se garantiza la transparencia? Publicidad activa y derecho de acceso | Ley 19/2013, arts. 1 a 24 y disp. adic. 4.ª; CE, art. 105 b) | — |
| **IV** | ¿Qué exige el buen gobierno? | Ley 19/2013, arts. 25 a 32 | — |
| **V** | ¿Quién vela por la transparencia y el buen gobierno? El Consejo de Transparencia y Buen Gobierno | Ley 19/2013, arts. 33 a 40; Estatuto del CTBG (RD 615/2024) | — |

!> **La idea que une los cinco bloques:** el Gobierno Abierto es una **forma de gobernar** basada en la transparencia, la integridad, la rendición de cuentas y la participación (I). España la concreta en **planes de acción** sucesivos, ligados a la Alianza para el Gobierno Abierto (II). Su pieza legal básica es la **Ley 19/2013**, con tres vertientes: **transparencia** —publicidad activa y derecho de acceso— (III), **buen gobierno** (IV) y un órgano garante, el **Consejo de Transparencia y Buen Gobierno** (V).

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo en el examen; para el derecho de acceso, ficha de derecho).
- El concepto de Gobierno Abierto y los planes de acción **no están en una ley**: se citan **literales** de la fuente oficial (Portal de la Transparencia, etiqueta **TRANSPARENCIA**), marcados como «fuente oficial, no es texto legal», y del Real Decreto 371/2026 (BOE).
- Los esquemas y cuadros comparativos **no son texto legal**: resumen los artículos citados.
- Al final: **Cierre 1** (las preguntas oficiales de 2025 sobre este tema) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué es el Gobierno Abierto y qué principios lo informan?", donde(
  "Primera pregunta del tema. Antes de estudiar los planes y la Ley 19/2013 hay que saber **qué es** el Gobierno Abierto, **qué principios** lo informan y **cómo se organiza** en España. No hay una ley que lo defina: la definición oficial está en el Portal de la Transparencia y la organización, en el Real Decreto 371/2026.",
  ["1 Concepto de Gobierno Abierto", "2 Principios informadores", "3 Cómo se organiza en España: órganos y Foro de Gobierno Abierto"]))

T.ap("s1", "I.1 Concepto de Gobierno Abierto", f"""
{unidad("1.1 La definición oficial (Portal de la Transparencia)",
  doc("GA_QUE", "Portal de la Transparencia · ¿Qué es el Gobierno Abierto?",
      ["El Gobierno Abierto es una cultura de gobernanza que promueve los principios de transparencia, integridad, rendición de cuentas y participación de las partes interesadas en apoyo de la democracia y el crecimiento inclusivo (definición recogida en la Recomendación del Consejo de la OCDE sobre Gobierno Abierto de 14 de diciembre de 2017."],
      ["cultura de gobernanza", "transparencia, integridad, rendición de cuentas y participación de las partes interesadas", "Recomendación del Consejo de la OCDE sobre Gobierno Abierto de 14 de diciembre de 2017"]),
  fichab("Una **cultura de gobernanza**, no un órgano ni una norma",
         "Definición del Consejo de la **OCDE** que recoge el Portal de la Transparencia",
         ["::Promueve cuatro principios:", "Transparencia", "Integridad", "Rendición de cuentas", "Participación de las partes interesadas"],
         f"Recomendación de {cs('GA_QUE', '14 de diciembre de 2017')}",
         "La definición procede de la **OCDE** (no de la OGP ni de la ONU). No es texto legal: ninguna ley española define el Gobierno Abierto."))}

{unidad("1.2 Por qué importa: la transparencia como eje (Ley 19/2013, preámbulo)",
  lit(L, "preambulo", ["deben ser los ejes fundamentales de toda acción política", "triple alcance"], solo=[6, 8], titulo="Preámbulo, I (Ley 19/2013)"),
  fichab("La Ley 19/2013 es la pieza legal básica de la transparencia y el buen gobierno",
         "Las Cortes Generales (ley estatal)",
         ["::Triple alcance (→ III, IV y V):", "Publicidad activa", "Derecho de acceso a la información", "Obligaciones de buen gobierno y consecuencias de su incumplimiento"],
         "—",
         f"Literal del preámbulo: transparencia, acceso a la información y buen gobierno {c(L, 'preambulo', 'deben ser los ejes fundamentales de toda acción política')}. El preámbulo no es norma, pero resume la estructura de la ley."))}
""", 2)

T.ap("s2", "I.2 Principios informadores del Gobierno Abierto", f"""
{unidad("2.1 Los pilares del Gobierno Abierto (RD 371/2026, art. 19.4)",
  lit("RD371", "Artículo 19", ["Transparencia.", "Participación ciudadana.", "Rendición de cuentas.", "Integridad pública.", "Colaboración y cocreación."], solo=[4, 5, 6, 7, 8, 9]),
  fichab("Los ámbitos en que el Observatorio de Gobierno Abierto difunde buenas prácticas",
         "Observatorio de Gobierno Abierto (→ I.3.4)",
         ["Transparencia", "Participación ciudadana", "Rendición de cuentas", "Integridad pública", "Colaboración y cocreación"],
         "—",
         f"La lista es abierta: {c('RD371', 'Artículo 19', 'entre otros')}. Coincide con los cuatro principios de la definición de la OCDE (→ I.1.1) y añade la **colaboración y cocreación**."))}

{unidad("2.2 Principios del Foro de Gobierno Abierto (RD 371/2026, preámbulo)",
  lit("RD371", "pr", ["accesibilidad universal, transparencia, integridad, imparcialidad, cooperación, rendición de cuentas y lealtad institucional"], solo=[12], titulo="Preámbulo (Real Decreto 371/2026)"),
  fichab("Principios con los que el Foro ejerce sus funciones",
         "El Foro de Gobierno Abierto (→ I.3.2)",
         ["Accesibilidad universal", "Transparencia", "Integridad", "Imparcialidad", "Cooperación", "Rendición de cuentas", "Lealtad institucional"],
         "—",
         f"Lo dice el **preámbulo** del Real Decreto: esos principios {c('RD371', 'pr', 'informarán todas sus actuaciones, deliberaciones y decisiones')}."))}
""", 2)

T.ap("s3", "I.3 Cómo se organiza el Gobierno Abierto en España", f"""
{unidad("3.1 Competencias y órganos (Portal de la Transparencia)",
  doc("GA_QUE", "Portal de la Transparencia · El Gobierno Abierto en España",
      ["Cada Administración pública tiene competencia exclusiva en materia de Gobierno Abierto, excepto en lo relativo a la transparencia, para la que la Ley 19/2013, de 9 de diciembre, de transparencia, acceso a la información pública y buen gobierno establece obligaciones comunes para todas las Administraciones públicas. Así, el Estado, las Comunidades Autónomas y las Entidades Locales desarrollan sus propias políticas y cuentan con sus propios órganos competentes en materia de Gobierno Abierto.",
       "A la Dirección General de Gobernanza Pública del Ministerio para la Transformación Digital y de la Función Pública le corresponde el impulso, la coordinación y el seguimiento de los planes de acción de Gobierno Abierto de España, así como actuar como punto de contacto con organizaciones internacionales para asuntos relacionados con el Gobierno Abierto.",
       "La Comisión Sectorial de Gobierno Abierto es un espacio de coordinación, colaboración y debate entre las Administraciones públicas españolas (estatal, autonómicas y locales) para el intercambio de experiencias y el desarrollo y seguimiento de iniciativas conjuntas en materia de gobierno abierto."],
      ["excepto en lo relativo a la transparencia", "Dirección General de Gobernanza Pública", "Comisión Sectorial de Gobierno Abierto"]),
  fichab("Reparto de papeles en materia de Gobierno Abierto",
         ["Cada Administración: sus propias políticas y órganos", "AGE: **Dirección General de Gobernanza Pública** (impulso, coordinación y seguimiento de los planes)", "Entre Administraciones: **Comisión Sectorial de Gobierno Abierto**", "Con la sociedad civil: **Foro de Gobierno Abierto** (→ I.3.2)"],
         "—", "—",
         "La transparencia es la excepción: la Ley 19/2013 fija **obligaciones comunes** para todas las Administraciones (→ III.1)."))}

{unidad("3.2 El Foro de Gobierno Abierto: naturaleza, adscripción y fines (RD 371/2026, arts. 2 y 3.1)",
  lit("RD371", "Artículo 2", ["órgano colegiado", "con carácter paritario", "Secretaría de Estado de Función Pública"]),
  lit("RD371", "Artículo 3", ["institucionalización de la colaboración"], solo=[1]),
  fichab("Órgano colegiado de participación paritaria de la sociedad civil en materia de gobierno abierto",
         f"Adscrito a la {c('RD371', 'Artículo 2', 'Secretaría de Estado de Función Pública')}",
         "Diseño, seguimiento y evaluación de las políticas de transparencia, participación, rendición de cuentas e innovación democrática; entre sus funciones (art. 3.2), analizar, examinar y seguir los **Planes de Acción de Gobierno Abierto** (→ II)",
         "—",
         "Lo crea y regula el **Real Decreto 371/2026**, que deja sin efectos la Orden HFP/134/2018 (disp. final segunda). Es órgano colegiado del art. 22.2 de la Ley 40/2015."))}

{unidad("3.3 Composición y funcionamiento del Pleno (RD 371/2026, arts. 5.1, 6.1 y 12)",
  lit("RD371", "Artículo 5", ["Secretaría de Estado de Función Pública"], solo=[1]),
  lit("RD371", "Artículo 6", ["sesenta y cuatro vocales, treinta y dos en representación de las administraciones públicas y treinta y dos en representación de la sociedad civil"], solo=[1]),
  lit("RD371", "Artículo 12", ["al menos dos veces al año", "al menos, un tercio de sus miembros", "preferentemente por consenso", "mayoría simple de los miembros asistentes con derecho a voto"], solo=[1, 4]),
  fichab("Cómo se compone y decide el Pleno del Foro",
         ["Presidencia: titular de la **Secretaría de Estado de Función Pública**", "Vicepresidencia Primera: titular de la **Dirección General de Gobernanza Pública** (art. 5.2)", "Vicepresidencia Segunda: una vocalía de la sociedad civil, rotativa anual (art. 5.3)", "**64 vocales**: 32 de las administraciones públicas y 32 de la sociedad civil"],
         "Pleno, Comisión Permanente y grupos de trabajo (art. 4); decide preferentemente por consenso",
         ["Pleno ordinario: al menos **dos veces al año**", "Extraordinario: a iniciativa de la Presidencia o de al menos **un tercio** de los miembros", "Sin consenso: **mayoría simple** de los asistentes con derecho a voto"],
         "Composición **paritaria**: 32 + 32. No confundir con la Comisión de Transparencia y Buen Gobierno (→ V.2)."))}

{unidad("3.4 Grupo Interministerial y Observatorio de Gobierno Abierto (RD 371/2026, arts. 17.1 y 19.1)",
  lit("RD371", "Artículo 17", ["responsables de las Unidades de Información de Transparencia de todos los ministerios", "Dirección General de Gobernanza Pública"], solo=[1]),
  lit("RD371", "Artículo 19", ["espacio virtual"], solo=[1, 2]),
  fichab("Dos piezas de apoyo: coordinación interna de la AGE y repositorio de buenas prácticas",
         ["Grupo Interministerial: responsables de las Unidades de Información de Transparencia de todos los ministerios; lo coordina la **Dirección General de Gobernanza Pública**", "Observatorio: lo diseña y mantiene el Ministerio para la Transformación Digital y de la Función Pública, a través de la Secretaría de Estado de Función Pública"],
         "El Observatorio tiene un entorno propio **dentro del Portal de la Transparencia**",
         "—",
         "Las Unidades de Información de Transparencia son las del art. 21 de la Ley 19/2013 (→ III.4.5)."))}

{resumen([
  "Gobierno Abierto: **cultura de gobernanza** que promueve **transparencia, integridad, rendición de cuentas y participación** (definición de la **OCDE**, 2017).",
  "Pilares del Observatorio: transparencia, participación, rendición de cuentas, integridad y **colaboración y cocreación** (RD 371/2026, art. 19.4).",
  "Cada Administración tiene sus propias políticas; la transparencia tiene **obligaciones comunes** (Ley 19/2013).",
  "Foro de Gobierno Abierto (RD 371/2026): órgano colegiado **paritario** (32 + 32), adscrito a la **Secretaría de Estado de Función Pública**, que la preside."],
  "Siguiente: II. ¿Qué planes de acción ha tenido España?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Qué planes de acción ha tenido España?", donde(
  "Segunda pregunta. El Gobierno Abierto se concreta en **planes de acción** con compromisos concretos, en el marco de la **Alianza para el Gobierno Abierto (OGP)**. España ha aprobado cinco; el vigente es el **V Plan 2025-2029**. Todo lo de este bloque sale de fuentes oficiales y del preámbulo del Real Decreto 371/2026: no hay una ley que regule los planes.",
  ["1 Qué son los planes y en qué marco se aprueban (OGP)", "2 Los planes de España: del I al V"]))

T.ap("s4", "II.1 Los planes de acción y la Alianza para el Gobierno Abierto", f"""
{unidad("1.1 Qué es un Plan de Gobierno Abierto (Portal de la Transparencia)",
  doc("GA_PLANES", "Portal de la Transparencia · Conoce los Planes de Gobierno Abierto de España",
      ["Los Planes de Gobierno Abierto de España recogen el conjunto de actuaciones a las que se compromete la Administración General del Estado, en colaboración con otras Administraciones públicas y con la sociedad civil, para avanzar, en un determinado período, en la participación, la transparencia, la integridad y la sensibilización social, y lograr una sociedad más justa, pacífica e inclusiva."],
      ["la Administración General del Estado", "en un determinado período"]),
  fichab("Conjunto de actuaciones a las que se compromete la Administración General del Estado para un período",
         "La **AGE**, en colaboración con otras Administraciones públicas y con la sociedad civil",
         "Por compromisos e iniciativas (→ II.2.2)",
         "Cada plan tiene un período (p. ej., 2025-2029)",
         "Quien se compromete es la **AGE**; las demás Administraciones y la sociedad civil **colaboran**."))}

{unidad("1.2 La Alianza para el Gobierno Abierto (OGP)",
  doc("GA_QUE", "Portal de la Transparencia · Alianza para el Gobierno Abierto (OGP)",
      ["La Alianza para el Gobierno Abierto (Open Government Partnership, OGP), fundada en septiembre de 2011, es una organización multilateral integrada por reformadores de las Administraciones públicas y de la sociedad civil, cuyo objetivo es lograr que las Administraciones públicas actúen con transparencia, fomenten la colaboración y la participación ciudadana, rindan cuentas y sean inclusivas. Para conseguir este objetivo, la OGP ha establecido un sistema de planes de acción a través de los cuales cada uno de sus miembros adquiere compromisos concretos para avanzar en el Gobierno Abierto. La evaluación del cumplimento de estos compromisos la realiza el Mecanismo de Revisión Independiente (MRI) de la Alianza.",
       "España se unió a la OGP en el mismo año de su fundación y, desde entonces, ha desarrollado varios planes de acción, cuya implementación ha supuesto grandes avances en Gobierno Abierto."],
      ["fundada en septiembre de 2011", "sistema de planes de acción", "Mecanismo de Revisión Independiente (MRI)", "en el mismo año de su fundación"]),
  fichab("Organización multilateral que trabaja mediante planes de acción con compromisos concretos",
         "Reformadores de las Administraciones públicas y de la sociedad civil; España, miembro desde **2011**",
         "Cada miembro adquiere compromisos en sus planes de acción; los evalúa el **Mecanismo de Revisión Independiente (MRI)**",
         "Fundada en **septiembre de 2011**",
         "Los planes de acción son el **instrumento de la OGP**; el concepto de Gobierno Abierto citado en I.1 es de la **OCDE**."))}
""", 2)

T.ap("s5", "II.2 Los planes de Gobierno Abierto de España: del I al V", f"""
{unidad("2.1 Del I al IV Plan (V Plan, visión global; RD 371/2026, preámbulo)",
  doc("GA_VPLAN", "V Plan de Gobierno Abierto de España 2025-2029 · El Gobierno Abierto en España (ámbito nacional)",
      ["• I Plan (2012-2014): aprobación de la Ley de Transparencia",
       "• II Plan (2014-2016): puesta en marcha del Portal de la Transparencia",
       "• III Plan (2017-2019): creación del Foro de Gobierno Abierto",
       "• IV Plan (2020-2024): ratificación por España del Convenio de Tromsø; aprobación del Sistema de Integridad de la Administración General del Estado; mejora de la participación y refuerzo de la inclusión de todos los niveles administrativos, desde el nacional hasta el local"],
      ["aprobación de la Ley de Transparencia", "puesta en marcha del Portal de la Transparencia", "creación del Foro de Gobierno Abierto", "Convenio de Tromsø"]),
  lit("RD371", "pr", ["en 2011", "cinco Planes de Acción nacionales", "más de 500 iniciativas"], solo=[2], titulo="Preámbulo (Real Decreto 371/2026)"),
  fichab("Los cuatro primeros planes y su medida principal",
         "La AGE, en el marco de la OGP",
         ["I Plan (2012-2014): Ley de Transparencia", "II Plan (2014-2016): Portal de la Transparencia", "III Plan (2017-2019): Foro de Gobierno Abierto", "IV Plan (2020-2024): Convenio de Tromsø y Sistema de Integridad de la AGE"],
         f"Con los cinco planes, {c('RD371', 'pr', 'se han impulsado más de 500 iniciativas')}",
         "Asocia cada plan con su hito: **ley** (I), **portal** (II), **foro** (III), **Tromsø e integridad** (IV)."))}

{unidad("2.2 El V Plan de Gobierno Abierto 2025-2029",
  doc("GA_VPLAN", "V Plan de Gobierno Abierto de España 2025-2029 · Aprobación, estructura y contenido",
      ["El V Plan de Gobierno Abierto 2025-2029 fue aprobado en la reunión del pleno del Foro de 6 de octubre de 2025.",
       "El Plan se articula en compromisos e iniciativas.",
       "El V Plan de Gobierno Abierto de España 2025-2029 contiene 10 compromisos en los que se agrupan las 218 iniciativas presentadas en conjunto por las diversas administraciones: 123 del ámbito central (AGE, recogiendo iniciativas de 16 ministerios), 82 del ámbito autonómico y 13 del ámbito local (a través de la FEMP).",
       "Los compromisos resultantes que abarcan todas las líneas de acción son:",
       "1. PARTICIPACIÓN Y ESPACIO CÍVICO.", "2. TRANSPARENCIA Y ACCESO A LA INFORMACIÓN.", "3. INTEGRIDAD Y RENDICIÓN DE CUENTAS.",
       "4. ADMINISTRACIÓN ABIERTA.", "5. GOBERNANZA DIGITAL E INTELIGENCIA ARTIFICIAL.", "6. APERTURA FISCAL: CUENTAS CLARAS Y ABIERTAS.",
       "7. INFORMACIÓN VERAZ / ECOSISTEMA INFORMATIVO.", "8. DIFUSION, FORMACIÓN Y PROMOCIÓN DEL GOBIERNO ABIERTO.",
       "9. OBSERVATORIO DE GOBIERNO ABIERTO.", "10. ESTADO ABIERTO.",
       "Los nueve primeros compromisos recogen iniciativas de la Administración General del Estado (AGE); el décimo agrupa las aportaciones de comunidades autónomas y entidades locales."],
      ["6 de octubre de 2025", "10 compromisos", "218 iniciativas"]),
  lit("RD371", "pr", ["IX Cumbre Global de la Alianza para el Gobierno Abierto", "Compromiso 1"], solo=[5, 6], titulo="Preámbulo (Real Decreto 371/2026)"),
  fichab("Plan vigente de Gobierno Abierto de España (2025-2029)",
         "Aprobado por el **pleno del Foro de Gobierno Abierto**; iniciativas de la AGE, las comunidades autónomas y las entidades locales (a través de la FEMP)",
         f"**10 compromisos** y **218 iniciativas** (123 AGE, 82 autonómicas y 13 locales); el compromiso 10, {cs('GA_VPLAN', 'ESTADO ABIERTO')}, agrupa las autonómicas y locales",
         "Aprobado el **6 de octubre de 2025**; período **2025-2029**",
         "Cayeron en 2025 (→ Cierre 1): **diez** compromisos y **218** iniciativas. El compromiso 1 es **participación y espacio cívico**; el 9, el **Observatorio**."))}

{resumen([
  "Los planes recogen las actuaciones a las que se compromete la **AGE**, con otras Administraciones y la sociedad civil, para un período.",
  "Marco: la **OGP** (fundada en **septiembre de 2011**; España, miembro desde ese año); evaluación por el **MRI**.",
  "I Plan (2012-2014): Ley de Transparencia · II (2014-2016): Portal · III (2017-2019): Foro · IV (2020-2024): Tromsø e integridad.",
  "V Plan 2025-2029: aprobado por el pleno del Foro el **6-10-2025**; **10 compromisos** y **218 iniciativas**."],
  "Siguiente: III. ¿Cómo se garantiza la transparencia? La Ley 19/2013")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Cómo se garantiza la transparencia? Publicidad activa y derecho de acceso (Ley 19/2013, arts. 1 a 24)", donde(
  "Tercera pregunta. La Ley 19/2013 hace dos cosas en su título I: obliga a **publicar** información sin que nadie la pida (**publicidad activa**) y reconoce a todas las personas el **derecho a pedirla** (**derecho de acceso**), con su procedimiento y su reclamación ante el Consejo de Transparencia y Buen Gobierno.",
  ["1 Objeto y ámbito subjetivo (arts. 1 a 4)", "2 Publicidad activa (arts. 5 a 11)", "3 Derecho de acceso: régimen general y límites (arts. 12 a 16)", "4 Ejercicio del derecho: solicitud, inadmisión, tramitación y resolución (arts. 17 a 22)", "5 Impugnaciones: la reclamación ante el CTBG (arts. 23 y 24; disp. adic. 4.ª)"]))

T.ap("s6", "III.1 Objeto y ámbito subjetivo de la Ley 19/2013 (arts. 1 a 4)", f"""
{unidad("1.1 Objeto (art. 1)",
  lit(L, "Artículo 1", ["ampliar y reforzar la transparencia de la actividad pública", "regular y garantizar el derecho de acceso", "establecer las obligaciones de buen gobierno"]),
  fichab("Las tres finalidades de la ley", "—",
         ["Transparencia de la actividad pública (→ III.2)", "Derecho de acceso a la información (→ III.3)", "Obligaciones de buen gobierno y consecuencias de su incumplimiento (→ IV)"],
         "—", "Los tres verbos: **ampliar y reforzar** la transparencia; **regular y garantizar** el acceso; **establecer** el buen gobierno."))}

{unidad("1.2 Sujetos del título I (art. 2)",
  lit(L, "Artículo 2", ["superior al 50 por 100", "en relación con sus actividades sujetas a Derecho Administrativo", "letras a) a d)"]),
  fichab("A quién se aplican la publicidad activa y el derecho de acceso",
         ["Administraciones territoriales, Seguridad Social y mutuas, organismos y entidades de Derecho Público, universidades públicas, corporaciones de Derecho Público (en sus actividades sujetas a Derecho Administrativo)", "Casa del Rey, Congreso, Senado, TC, CGPJ, Banco de España, Consejo de Estado, Defensor del Pueblo, Tribunal de Cuentas, CES (en su actividad administrativa)", "Sociedades mercantiles con participación **superior al 50 %**, fundaciones del sector público y asociaciones de Administraciones"],
         "—", "—",
         "Para la ley, «Administraciones Públicas» son solo las letras **a) a d)** (art. 2.2). Los órganos de la letra f), solo **en sus actividades sujetas a Derecho Administrativo**."))}

{unidad("1.3 Otros sujetos obligados (art. 3)",
  lit(L, "Artículo 3", ["capítulo II", "100.000 euros", "40 %", "5.000 euros"]),
  fichab("Sujetos privados obligados solo a la publicidad activa",
         ["Partidos políticos, organizaciones sindicales y empresariales", "Entidades privadas subvencionadas por encima de los umbrales"],
         "Se les aplica el **capítulo II** (publicidad activa), no el derecho de acceso",
         ["Más de **100.000 €** de ayudas en un año, o", "Al menos el **40 %** de sus ingresos anuales de ayudas, con un mínimo de **5.000 €**"],
         "Umbrales: **100.000 €** / **40 % y 5.000 €**. Solo **publicidad activa** (capítulo II)."))}

{unidad("1.4 Obligación de suministrar información (art. 4)",
  lit(L, "Artículo 4", ["previo requerimiento", "adjudicatarios de contratos del sector público"]),
  fichab("Deber de colaboración de quienes prestan servicios públicos o ejercen potestades administrativas",
         "Personas físicas y jurídicas que presten servicios públicos o ejerzan potestades administrativas; también los adjudicatarios de contratos",
         "Suministran la información a la Administración a la que estén vinculadas", "Previo requerimiento",
         "No publican ellos: **suministran** la información **previo requerimiento** a la Administración vinculada."))}
""", 2)

T.ap("s7", "III.2 Publicidad activa (arts. 5 a 11)", f"""
{unidad("2.1 Principios generales (art. 5)",
  lit(L, "Artículo 5", ["de forma periódica y actualizada", "previa disociación", "preferiblemente, en formatos reutilizables", "50.000 euros", "de acceso fácil y gratuito"]),
  fichab("Deber de publicar, sin solicitud previa, la información relevante para la transparencia",
         "Los sujetos del **art. 2.1**",
         ["En sedes electrónicas o páginas web", "Clara, estructurada y entendible; preferiblemente en formatos reutilizables", "Comprensible, de acceso fácil y **gratuito**, accesible a personas con discapacidad"],
         "De forma periódica y actualizada; entidades sin ánimo de lucro con presupuesto inferior a **50.000 €**: pueden usar los medios electrónicos de la Administración que más las subvencione",
         "Se aplican los **límites del art. 14** y la **protección de datos del art. 15**; los datos especialmente protegidos, solo **previa disociación**."))}

{unidad("2.2 Información institucional, organizativa y de planificación (art. 6)",
  lit(L, "Artículo 6", ["organigrama actualizado", "inspecciones generales de servicios"]),
  fichab("Qué se publica sobre la organización y la planificación",
         "Todos los sujetos del título I (6.1); las Administraciones Públicas (6.2)",
         ["Funciones, normativa y estructura organizativa, con **organigrama actualizado**", "Planes y programas anuales y plurianuales, con su evaluación"],
         "—",
         "En la AGE evalúan el cumplimiento de los planes las **inspecciones generales de servicios**."))}

{unidad("2.3 Información de relevancia jurídica (art. 7)",
  lit(L, "Artículo 7", ["cuando se soliciten los dictámenes", "sin que ello suponga, necesariamente, la apertura de un trámite de audiencia pública"]),
  fichab("Qué se publica sobre normas y criterios jurídicos", "Las Administraciones Públicas",
         ["Directrices, instrucciones, circulares y respuestas a consultas que interpreten el Derecho", "Anteproyectos de ley y proyectos de decretos legislativos", "Proyectos de reglamentos", "Memorias e informes de los expedientes normativos", "Documentos sometidos a información pública"],
         "Anteproyectos: cuando se soliciten los dictámenes (sin dictamen preceptivo, al aprobarse)",
         "Publicar un proyecto de reglamento **no supone necesariamente** abrir audiencia pública."))}

{unidad("2.4 Información económica, presupuestaria y estadística (art. 8)",
  lit(L, "Artículo 8", ["podrá realizarse trimestralmente", "Las subvenciones y ayudas públicas concedidas", "Las retribuciones percibidas anualmente por los altos cargos", "relación de los bienes inmuebles"], solo=[1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]),
  fichab("Qué se publica, como mínimo, de la gestión económica", "Los sujetos del título I; los del art. 3, en lo que reciben de una Administración (8.2)",
         ["Contratos (los **menores**, trimestralmente)", "Convenios y encomiendas", "Subvenciones y ayudas", "Presupuestos y su ejecución", "Cuentas anuales e informes de auditoría y fiscalización", "Retribuciones de altos cargos e indemnizaciones por cese", "Compatibilidades", "Declaraciones de bienes de representantes locales", "Bienes inmuebles de las Administraciones (8.3)"],
         "Contratos menores: publicación que **podrá** ser trimestral",
         "Es una lista de **mínimos** («como mínimo»). Los sujetos del art. 3 publican contratos, convenios y subvenciones **con una Administración Pública**."))}

{unidad("2.5 Control (art. 9)",
  lit(L, "Artículo 9", ["Consejo de Transparencia y Buen Gobierno", "infracción grave"]),
  fichab("Control del cumplimiento de la publicidad activa por la AGE",
         "El **Consejo de Transparencia y Buen Gobierno** (→ V)",
         "Resoluciones con las medidas para el cese del incumplimiento y el inicio de actuaciones disciplinarias",
         "—",
         "El incumplimiento **reiterado** es **infracción grave** a efectos disciplinarios (igual que no resolver en plazo de forma reiterada, art. 20.6)."))}

{unidad("2.6 Portal de la Transparencia y principios técnicos (arts. 10 y 11)",
  lit(L, "Artículo 10", ["dependiente del Ministerio de la Presidencia", "cuyo acceso se solicite con mayor frecuencia"], solo=[1, 2]),
  lit(L, "Artículo 11", ["Accesibilidad", "Interoperabilidad", "Reutilización"]),
  fichab("Punto de acceso de la AGE a la información de publicidad activa",
         "La **Administración General del Estado** lo desarrolla; dependiente del Ministerio de la Presidencia (según el texto del art. 10.1)",
         "Incluye la información de los artículos anteriores y la que se solicite con mayor frecuencia",
         "—",
         "Tres principios técnicos: **accesibilidad, interoperabilidad y reutilización**."))}
""", 2)

T.ap("s8", "III.3 Derecho de acceso a la información pública: régimen general y límites (arts. 12 a 16)", f"""
{unidad("3.1 Fundamento constitucional (CE, art. 105 b)",
  lit("CE", "Artículo 105", ["El acceso de los ciudadanos a los archivos y registros administrativos"], solo=[1, 3]),
  fichab("Mandato al legislador de regular el acceso a archivos y registros", "La ley (las Cortes)",
         "Salvo lo que afecte a la seguridad y defensa del Estado, la averiguación de los delitos y la intimidad de las personas", "—",
         "La Ley 19/2013 desarrolla el **art. 105 b)** CE (art. 12): no lo configura como derecho fundamental del Título I."))}

{unidad("3.2 Titulares y objeto (arts. 12 y 13)",
  lit(L, "Artículo 12", ["Todas las personas", "artículo 105.b)"]),
  lit(L, "Artículo 13", ["cualquiera que sea su formato o soporte", "elaborados o adquiridos en el ejercicio de sus funciones"]),
  ficha(c(L, "Artículo 12", "Todas las personas"),
        f"Acceder a la información pública: {c(L, 'Artículo 13', 'los contenidos o documentos, cualquiera que sea su formato o soporte')} que obren en poder de los sujetos del título I",
        "Los del art. 14 y la protección de datos del art. 15 (→ III.3.3 y → III.3.4)",
        "Reclamación potestativa ante el CTBG y recurso contencioso-administrativo (→ III.5)",
        "Titulares: **todas las personas** (no solo los ciudadanos ni los interesados). La información tiene que haber sido **elaborada o adquirida en el ejercicio de sus funciones**."))}

{unidad("3.3 Límites al derecho de acceso (art. 14)",
  lit(L, "Artículo 14", ["podrá ser limitado", "La seguridad nacional.", "La protección del medio ambiente.", "justificada y proporcionada", "interés público o privado superior"]),
  ficha("—",
        "—",
        ["::Doce límites, si el acceso supone un **perjuicio** para:", "Seguridad nacional; defensa; relaciones exteriores; seguridad pública", "Prevención, investigación y sanción de ilícitos; igualdad de las partes y tutela judicial efectiva", "Funciones de vigilancia, inspección y control", "Intereses económicos y comerciales; política económica y monetaria", "Secreto profesional y propiedad intelectual e industrial", "Confidencialidad o secreto en procesos de toma de decisión", "Protección del medio ambiente"],
        "Aplicación **justificada y proporcionada**, atendiendo al caso concreto y a un interés público o privado superior (14.2); las resoluciones se publican previa disociación (14.3)",
        "El límite no opera de forma automática: el acceso «**podrá** ser limitado» si hay **perjuicio**. Son **doce** letras (a a l)."))}

{unidad("3.4 Protección de datos personales (art. 15)",
  lit(L, "Artículo 15", ["consentimiento expreso y por escrito del afectado", "consentimiento expreso del afectado o si aquel estuviera amparado por una norma con rango de ley", "datos meramente identificativos", "previa ponderación suficientemente razonada", "previa disociación"], solo=[1, 2, 3, 4, 10]),
  ficha("Los afectados cuyos datos aparecen en la información",
        ["Ideología, afiliación sindical, religión o creencias: **consentimiento expreso y por escrito** (salvo que los hubiera hecho manifiestamente públicos)", "Origen racial, salud, vida sexual, datos genéticos o biométricos, infracciones: **consentimiento expreso** o **norma con rango de ley**", "Datos meramente identificativos de la organización: con carácter general, se da acceso", "Resto: **ponderación** razonada del interés público y los derechos de los afectados"],
        "—",
        "Con **disociación** previa que impida identificar a los afectados no se aplican estas reglas (15.4)",
        "Distingue **«expreso y por escrito»** (ideología, sindicato, religión) de **«expreso»** o ley (salud, origen racial…)."))}

{unidad("3.5 Acceso parcial (art. 16)",
  lit(L, "Artículo 16", ["acceso parcial", "información distorsionada o que carezca de sentido", "deberá indicarse al solicitante"]),
  fichab("Acceso a la parte de la información no afectada por un límite", "El órgano que resuelve",
         "Omite la información afectada e indica al solicitante que se ha omitido una parte", "—",
         "No cabe si el resultado es una información **distorsionada o que carezca de sentido**."))}
""", 2)

T.ap("s9", "III.4 Ejercicio del derecho de acceso (arts. 17 a 22)", f"""
{unidad("4.1 La solicitud (art. 17)",
  lit(L, "Artículo 17", ["al titular del órgano administrativo o entidad que posea la información", "no está obligado a motivar su solicitud", "lenguas cooficiales"]),
  fichab("Inicio del procedimiento de acceso", "El solicitante, ante el titular del órgano o entidad que posea la información",
         ["Por cualquier medio que deje constancia de la **identidad**, la **información** solicitada, una **dirección de contacto** y, en su caso, la **modalidad** de acceso", "Sin obligación de motivar"],
         "—",
         "La falta de motivación **no es por sí sola** causa de rechazo; los motivos **pueden** tenerse en cuenta al resolver."))}

{unidad("4.2 Causas de inadmisión (art. 18)",
  lit(L, "Artículo 18", ["mediante resolución motivada", "en curso de elaboración o de publicación general", "reelaboración", "manifiestamente repetitivas"]),
  fichab("Supuestos en que la solicitud se inadmite a trámite", "El órgano competente, por resolución motivada",
         ["Información en curso de elaboración o de publicación general", "Información auxiliar o de apoyo (notas, borradores, opiniones, informes internos…)", "Información que exige una acción previa de **reelaboración**", "Solicitud a un órgano que no tiene la información, si se desconoce el competente", "Solicitudes manifiestamente repetitivas o abusivas"],
         "—",
         "En el caso de la letra d), la resolución debe **indicar el órgano** que se considera competente (18.2)."))}

{unidad("4.3 Tramitación (art. 19)",
  lit(L, "Artículo 19", ["en un plazo de diez días", "plazo de quince días"]),
  fichab("Incidencias de la tramitación", "El órgano al que se dirige la solicitud",
         ["Si no tiene la información: la remite al competente, si lo conoce, e informa al solicitante", "Solicitud imprecisa: se pide que se concrete", "Afecta a terceros: alegaciones", "Información elaborada por otro: se le remite para que decida"],
         ["Concretar la solicitud: **10 días** (si no, desistimiento)", "Alegaciones de terceros: **15 días**", "Ambos casos suspenden el plazo para resolver"],
         "**Diez** días para concretar; **quince** para alegaciones de terceros."))}

{unidad("4.4 Resolución y silencio (art. 20)",
  lit(L, "Artículo 20", ["en el plazo máximo de un mes desde la recepción de la solicitud por el órgano competente para resolver", "podrá ampliarse por otro mes", "se entenderá que la solicitud ha sido desestimada", "recurribles directamente ante la Jurisdicción Contencioso-administrativa", "infracción grave"]),
  fichab("Resolución que concede o deniega el acceso", "El órgano competente; se notifica al solicitante y a los terceros afectados que lo pidan",
         ["Motivadas: las que deniegan, las de acceso parcial o por otra modalidad y las que conceden pese a la oposición de un tercero", "Recurribles directamente en vía contencioso-administrativa, sin perjuicio de la reclamación del art. 24"],
         ["**Un mes** desde la recepción por el órgano competente", "Ampliable **otro mes** por volumen o complejidad, previa notificación", "Silencio: **desestimatorio**"],
         "El silencio es **negativo** (desestimación). El plazo cuenta desde la recepción **por el órgano competente para resolver**."))}

{unidad("4.5 Unidades de información (art. 21)",
  lit(L, "Artículo 21", ["unidades especializadas", "Llevar un registro de las solicitudes de acceso a la información"], solo=[1, 2, 3, 4, 7, 9, 11]),
  fichab("Unidades especializadas que gestionan la transparencia en la AGE", "En la **Administración General del Estado**; el resto de entidades identifican el órgano competente (21.3)",
         ["Recabar y difundir la información de publicidad activa", "Recibir y tramitar las solicitudes", "Llevar un registro de solicitudes", "Mantener un mapa de contenidos"],
         "—", "Sus responsables forman el **Grupo Interministerial de Gobierno Abierto** (→ I.3.4)."))}

{unidad("4.6 Formalización del acceso (art. 22)",
  lit(L, "Artículo 22", ["preferentemente por vía electrónica", "en un plazo no superior a diez días", "El acceso a la información será gratuito"]),
  fichab("Cómo se da efectivamente el acceso", "El órgano que lo concede",
         ["Preferentemente por vía electrónica", "Si ya está publicada, basta indicar cómo acceder", "Con oposición de tercero, solo tras el plazo del recurso contencioso-administrativo"],
         "Si no se da al notificar: en un plazo **no superior a diez días**",
         "El acceso es **gratuito**; pueden cobrarse **copias** o cambio de formato (Ley 8/1989)."))}
""", 2)

T.ap("s10", "III.5 Impugnaciones: la reclamación ante el Consejo de Transparencia y Buen Gobierno (arts. 23 y 24; disp. adic. 4.ª)", f"""
{unidad("5.1 Recursos (art. 23)",
  lit(L, "Artículo 23", ["sustitutiva de los recursos administrativos", "sólo cabrá la interposición de recurso contencioso-administrativo"]),
  fichab("La reclamación sustituye a los recursos administrativos", "—",
         "Contra las resoluciones de los órganos del **art. 2.1 f)** (Casa del Rey, Cortes, TC, CGPJ…), solo recurso contencioso-administrativo", "—",
         "No hay alzada ni reposición: la reclamación del art. 24 es **sustitutiva** de los recursos administrativos."))}

{unidad("5.2 La reclamación (art. 24)",
  lit(L, "Artículo 24", ["con carácter potestativo y previo a su impugnación en vía contencioso-administrativa", "en el plazo de un mes", "será de tres meses", "comunicará al Defensor del Pueblo"]),
  fichab("Reclamación ante el Consejo de Transparencia y Buen Gobierno",
         "Ante el **CTBG** (salvo que la comunidad autónoma la atribuya a un órgano propio, → III.5.3); la resuelve su Presidente (art. 38.2 c, → V.3.1)",
         ["Frente a toda resolución **expresa o presunta** en materia de acceso", "Potestativa y previa a la vía contencioso-administrativa", "Audiencia a terceros si la denegación se basa en sus derechos"],
         ["Interposición: **un mes** desde la notificación o desde los efectos del silencio", "Resolución: **tres meses**; si no, **desestimada**"],
         "Es **potestativa** (no obligatoria). **Un mes** para reclamar, **tres meses** para resolver. Las resoluciones se comunican al **Defensor del Pueblo**."))}

{unidad("5.3 Comunidades autónomas y entidades locales (disp. adic. 4.ª)",
  lit(L, "dacuaa", ["al órgano independiente que determinen las Comunidades Autónomas", "convenio"], solo=[1, 3], titulo="Disposición adicional cuarta. Reclamación (Ley 19/2013)"),
  fichab("Quién resuelve la reclamación en el ámbito autonómico y local",
         ["El **órgano independiente** que determine cada comunidad autónoma", "O el CTBG, si la comunidad se lo atribuye por **convenio**"],
         "Por convenio con la AGE, en el que la comunidad sufraga los gastos", "—",
         "Sin convenio, el CTBG **no** resuelve las reclamaciones contra comunidades autónomas ni entidades locales de su territorio."))}

{resumen([
  "Sujetos: Administraciones y entidades del **art. 2**; partidos, sindicatos, organizaciones empresariales y entidades subvencionadas (**100.000 €** o **40 % y 5.000 €**), solo publicidad activa (**art. 3**).",
  "Publicidad activa: institucional y de planificación (6), jurídica (7), económica (8); **Portal de la Transparencia** (10); control del **CTBG** (9).",
  "Derecho de acceso: **todas las personas**, sin motivar; **12 límites** (14) y protección de datos (15).",
  "Plazos: concretar **10 días**, alegaciones **15 días**, resolver **1 mes** (+1), silencio **negativo**; formalizar en **10 días**.",
  "Reclamación ante el CTBG: **potestativa**, **1 mes** para interponer, **3 meses** para resolver (silencio desestimatorio)."],
  "Siguiente: IV. ¿Qué exige el buen gobierno?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Qué exige el buen gobierno? (Ley 19/2013, arts. 25 a 32)", donde(
  "Cuarta pregunta. El título II convierte en ley los **principios de buen gobierno** de los miembros del Gobierno y altos cargos y les anuda un **régimen sancionador**.",
  ["1 Ámbito y principios (arts. 25 y 26)", "2 Infracciones (arts. 27 a 29)", "3 Sanciones, procedimiento y prescripción (arts. 30 a 32)"]))

T.ap("s11", "IV.1 Ámbito y principios de buen gobierno (arts. 25 y 26)", f"""
{unidad("1.1 Ámbito de aplicación (art. 25)",
  lit(L, "Artículo 25", ["miembros del Gobierno", "Secretarios de Estado", "miembros de las Juntas de Gobierno de las Entidades Locales", "no afectará, en ningún caso, a la condición de cargo electo"]),
  fichab("A quién obliga el título II",
         ["Miembros del Gobierno, Secretarios de Estado y altos cargos de la AGE y del sector público estatal", "Altos cargos o asimilados autonómicos y locales, incluidos los miembros de las **Juntas de Gobierno** locales"],
         "Altos cargos: los que tengan esa consideración según la normativa de **conflictos de intereses**", "—",
         "Se aplica también a CC. AA. y entidades locales (25.2); no afecta a la condición de **cargo electo**."))}

{unidad("1.2 Principios de buen gobierno (art. 26)",
  lit(L, "Artículo 26", ["Principios generales:", "Principios de actuación:", "regalos que superen los usos habituales, sociales o de cortesía", "informarán la interpretación y aplicación del régimen sancionador"]),
  fichab("Principios que deben observar los altos cargos",
         "Las personas del art. 25",
         ["::Dos grupos:", "**Generales** (7): transparencia, dedicación al servicio público, imparcialidad, igualdad de trato, diligencia, conducta digna, responsabilidad", "**De actuación** (9): plena dedicación e incompatibilidades, reserva, denuncia de irregularidades, uso de poderes para su fin, abstención, regalos, transparencia, gestión de recursos públicos, no obtener ventajas"],
         "—",
         "Los principios **informan la interpretación y aplicación** del régimen sancionador (26.3). El incumplimiento de los principios **de actuación** (26.2 b) puede ser infracción **leve** (art. 29.3 b), si no es grave o muy grave ni está tipificado en otra norma."))}
""", 2)

T.ap("s12", "IV.2 Infracciones (arts. 27 a 29)", f"""
{unidad("2.1 Conflicto de intereses (art. 27)",
  lit(L, "Artículo 27", ["normativa en materia de conflictos de intereses"]),
  fichab("Remisión a la normativa de conflictos de intereses", "—",
         "El incumplimiento de incompatibilidades o declaraciones se sanciona según esa normativa (AGE) o la propia de cada Administración", "—",
         "La Ley 19/2013 **no tipifica** estas infracciones: **remite**."))}

{unidad("2.2 Gestión económico-presupuestaria (art. 28)",
  lit(L, "Artículo 28", ["infracciones muy graves", "cuando sean culpables", "La incursión en alcance", "sin crédito suficiente", "La omisión del trámite de intervención previa"], solo=[1, 2, 4, 5, 7, 18]),
  fichab("Infracciones muy graves en la gestión de fondos públicos", "Los altos cargos del art. 25",
         ["Todas son **muy graves**", "Exigen culpa («cuando sean culpables»)", "Ej.: alcance, gastos sin crédito, omisión de la intervención previa, incumplimientos de la LO 2/2012, no rendir cuentas"],
         "—",
         "Todas las del art. 28 son **muy graves** y conllevan restituir e indemnizar a la Hacienda Pública (art. 30.8)."))}

{unidad("2.3 Infracciones disciplinarias (art. 29)",
  lit(L, "Artículo 29", ["Son infracciones muy graves:", "El acoso laboral.", "Son infracciones graves:", "El abuso de autoridad en el ejercicio del cargo.", "Son infracciones leves:"], solo=[1, 2, 3, 12, 13, 14, 15, 16, 20, 21, 22, 23]),
  fichab("Infracciones disciplinarias de los altos cargos", "Los altos cargos del art. 25",
         ["Muy graves: p. ej., incumplir el deber de respeto a la Constitución, discriminación y acoso, acoso laboral", "Graves: p. ej., abuso de autoridad, intervenir habiendo causa de abstención", "Leves: incorrección con superiores, compañeros o subordinados; descuido o negligencia"],
         "Reincidencia: dos infracciones graves (o leves) sancionadas en el año anterior elevan la siguiente",
         "El **abuso de autoridad** es **grave**; el **acoso laboral**, **muy grave**."))}
""", 2)

T.ap("s13", "IV.3 Sanciones, procedimiento y prescripción (arts. 30 a 32)", f"""
{unidad("3.1 Sanciones (art. 30)",
  lit(L, "Artículo 30", ["amonestación", "su publicación en el «Boletín Oficial del Estado»", "durante un periodo de entre cinco y diez años", "Fiscal General del Estado"], solo=[1, 2, 3, 4, 5, 6, 15, 17, 18, 19]),
  fichab("Qué sanción corresponde a cada infracción", "El órgano del art. 31.4",
         ["Leves: **amonestación**", "Graves: declaración del incumplimiento y su publicación en el BOE o diario oficial; no percepción de la indemnización por cese", "Muy graves: las de las graves + **destitución** + prohibición de ser alto cargo de **5 a 10 años**"],
         "Inhabilitación para alto cargo: **entre cinco y diez años**",
         "Si puede haber delito, se pasa al **Fiscal General del Estado** y se suspende el procedimiento."))}

{unidad("3.2 Órgano competente y procedimiento (art. 31)",
  lit(L, "Artículo 31", ["se iniciará de oficio", "el Consejo de Ministros a propuesta del Ministro de Hacienda y Administraciones Públicas", "Oficina de Conflictos de Intereses", "orden jurisdiccional contencioso-administrativo"], solo=[1, 3, 4, 5, 7, 8, 9, 10, 12]),
  fichab("Quién incoa, instruye y sanciona en el ámbito estatal",
         ["Miembros del Gobierno y Secretarios de Estado: incoa y sanciona el **Consejo de Ministros**", "Resto de altos cargos de la AGE: el **Ministro de Hacienda y Administraciones Públicas** (según el texto del artículo)", "Instruye: la **Oficina de Conflictos de Intereses**"],
         "De oficio: por propia iniciativa, orden superior, petición razonada o **denuncia** de los ciudadanos",
         "—",
         "El Presidente del CTBG puede **instar** el inicio del procedimiento (art. 38.2 e, → V.3.1). Las resoluciones son recurribles en vía **contencioso-administrativa**."))}

{unidad("3.3 Prescripción (art. 32)",
  lit(L, "Artículo 32", ["cinco años para las infracciones muy graves, tres años para las graves y un año para las leves"], solo=[1, 2]),
  fichab("Plazos de prescripción de infracciones y sanciones", "—", "—",
         ["Muy graves: **5 años**", "Graves: **3 años**", "Leves: **1 año**", "Los mismos plazos para las sanciones"],
         "**5-3-1**, iguales para infracciones y sanciones."))}

{resumen([
  "Buen gobierno: miembros del Gobierno, Secretarios de Estado y altos cargos (también autonómicos y locales).",
  "Principios **generales** (7) y **de actuación** (9); informan el régimen sancionador.",
  "Infracciones: conflicto de intereses (remisión), gestión económico-presupuestaria (todas **muy graves**) y disciplinarias.",
  "Sanciones: leve → **amonestación**; grave → publicación en el BOE y sin indemnización; muy grave → **destitución** e inhabilitación de **5 a 10 años**.",
  "Prescripción: **5, 3 y 1 años**."],
  "Siguiente: V. ¿Quién vela por todo ello? El Consejo de Transparencia y Buen Gobierno")}
""", 2)

# =============================================================================
T.ap("bV", "V. ¿Quién vela por la transparencia y el buen gobierno? El Consejo de Transparencia y Buen Gobierno (arts. 33 a 40; RD 615/2024)", donde(
  "Quinta pregunta. El título III crea el **Consejo de Transparencia y Buen Gobierno**. Su **Estatuto** vigente lo aprobó el Real Decreto 615/2024, que lo configura como **autoridad administrativa independiente**.",
  ["1 Naturaleza y fines (arts. 33 y 34; Estatuto, arts. 1 y 2)", "2 Órganos: la Comisión y el Presidente (arts. 35 a 37; Estatuto, arts. 12, 18 y 20)", "3 Funciones, régimen jurídico y relaciones con las Cortes (arts. 38 a 40; Estatuto, art. 9)", "4 Cuadro de plazos y mayorías del tema"]))

T.ap("s14", "V.1 Naturaleza y fines del Consejo (arts. 33 y 34; Estatuto, arts. 1 y 2)", f"""
{unidad("1.1 Creación y naturaleza (Ley 19/2013, art. 33)",
  lit(L, "Artículo 33", ["Se crea el Consejo de Transparencia y Buen Gobierno", "personalidad jurídica propia y plena capacidad de obrar", "autonomía y plena independencia"]),
  fichab("Organismo público creado por la Ley 19/2013", "—",
         "Con personalidad jurídica propia y plena capacidad de obrar; actúa con autonomía y plena independencia", "—",
         "El art. 33.1 conserva su redacción original (adscripción al Ministerio de Hacienda y Administraciones Públicas); la naturaleza y la vinculación actuales están en el Estatuto (→ V.1.2)."))}

{unidad("1.2 Autoridad administrativa independiente (Estatuto, art. 1.1)",
  lit("RD615", "Artículo 1", ["autoridad administrativa independiente de ámbito estatal", "«Consejo de Transparencia y Buen Gobierno, A.A.I.»", "Ministerio para la Transformación Digital y de la Función Pública"], solo=[1, 2, 3]),
  fichab("Naturaleza actual del Consejo", "—",
         ["Autoridad administrativa independiente de ámbito estatal (arts. 109 y 110 de la Ley 40/2015)", "Denominación oficial: «Consejo de Transparencia y Buen Gobierno, A.A.I.»", "Vinculado a la AGE a través del **Ministerio para la Transformación Digital y de la Función Pública**"],
         "—", "Sede en **Madrid** (art. 1.4). El Estatuto vigente es el del **RD 615/2024**, que derogó el del RD 919/2014."))}

{unidad("1.3 Fines (Ley 19/2013, art. 34)",
  lit(L, "Artículo 34", ["promover la transparencia de la actividad pública", "velar por el cumplimiento de las obligaciones de publicidad", "salvaguardar el ejercicio de derecho de acceso", "garantizar la observancia de las disposiciones de buen gobierno"]),
  fichab("Las cuatro finalidades del Consejo", "—",
         ["Promover la transparencia", "Velar por la publicidad activa", "Salvaguardar el derecho de acceso", "Garantizar el buen gobierno"], "—",
         "Cuatro verbos: **promover**, **velar**, **salvaguardar**, **garantizar**."))}
""", 2)

T.ap("s15", "V.2 Órganos: la Comisión de Transparencia y Buen Gobierno y el Presidente (arts. 35 a 37; Estatuto, arts. 12, 18 y 20)", f"""
{unidad("2.1 Composición del Consejo (art. 35)",
  lit(L, "Artículo 35", ["La Comisión de Transparencia y Buen Gobierno.", "que lo será también de su Comisión"]),
  fichab("Los dos órganos del Consejo", "—", ["La **Comisión** de Transparencia y Buen Gobierno", "El **Presidente**, que también preside la Comisión"], "—",
         "Dos órganos, no tres: el Presidente del Consejo **es** el de la Comisión."))}

{unidad("2.2 La Comisión de Transparencia y Buen Gobierno (art. 36)",
  lit(L, "Artículo 36", ["Un Diputado.", "Un Senador.", "Un representante del Tribunal de Cuentas.", "Un representante de la Autoridad Independiente de Responsabilidad Fiscal.", "no exigirá dedicación exclusiva ni dará derecho a remuneración", "Al menos una vez al año"]),
  fichab("Órgano colegiado del Consejo",
         ["Presidente", "Un Diputado y un Senador", "Representantes del Tribunal de Cuentas, del Defensor del Pueblo, de la AEPD, de la Secretaría de Estado de Administraciones Públicas (según el texto del artículo) y de la AIReF"],
         "Sin dedicación exclusiva ni remuneración (salvo el Presidente)",
         "Al menos **una vez al año**, convoca a los órganos análogos de las comunidades autónomas",
         "**Ocho** miembros con el Presidente. La reunión **anual** es con los órganos autonómicos; la Comisión se reúne **cada trimestre** (→ V.2.4)."))}

{unidad("2.3 El Presidente (art. 37; Estatuto, art. 12.1 y 12.3)",
  lit(L, "Artículo 37", ["por un período no renovable de cinco años mediante Real Decreto", "El Congreso, a través de la Comisión competente y por acuerdo adoptado por mayoría absoluta, deberá refrendar el nombramiento", "en el plazo de un mes natural", "condena por delito doloso"], solo=[1, 2]),
  lit("RD615", "Artículo 12", ["alto cargo, con rango de Subsecretario", "sólo podrán ser impugnadas en vía contencioso-administrativa"], solo=[1, 3, 4]),
  fichab("Nombramiento, mandato y cese del Presidente del Consejo",
         "Nombra el Gobierno por **Real Decreto**, a propuesta del Ministro (según el art. 37.1, el de Hacienda y Administraciones Públicas); comparece ante la Comisión del Congreso, que **refrenda**",
         ["Entre personas de reconocido prestigio y competencia profesional", "Cese: expiración del mandato, a petición propia o separación por el Gobierno (incumplimiento grave, incapacidad permanente, incompatibilidad sobrevenida o condena por delito doloso)", "Alto cargo con rango de **Subsecretario** (Estatuto, art. 12.1)"],
         ["Mandato: **cinco años, no renovable**", "Refrendo: **Congreso**, en Comisión, por **mayoría absoluta**, en **un mes natural**"],
         "Refrenda el **Congreso** (no las Cortes ni el Senado), por **mayoría absoluta**. Cayó en 2025 (→ Cierre 1). Sus actos agotan la vía administrativa (reposición potestativa), salvo las reclamaciones del art. 24, solo impugnables en vía contencioso-administrativa."))}

{unidad("2.4 Funcionamiento de la Comisión y mandato de sus vocales (Estatuto, arts. 18.1 y 20.2 a 20.4)",
  lit("RD615", "Artículo 18", ["será de cinco años"], solo=[1]),
  lit("RD615", "Artículo 20", ["en sesión plenaria", "al menos una vez al trimestre", "la mitad de las vocalías nombradas", "una tercera parte de las vocalías nombradas"], solo=[2, 3, 4]),
  fichab("Cómo funciona la Comisión según el Estatuto", "La Comisión; la convoca la Presidencia o la mayoría de sus vocalías",
         "Acuerdos en sesión plenaria; presencial o a distancia (20.5)",
         ["Reuniones: al menos **una vez al trimestre**", "Quórum: Presidencia, Secretaría y la **mitad** de las vocalías (1.ª convocatoria) o **un tercio** (2.ª)", "Mandato de los vocales: **cinco años**, prorrogable por otro periodo igual (art. 18.1)"],
         "**Trimestre** (Estatuto, art. 20.3), no semestre ni año. Cayó en 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s16", "V.3 Funciones, régimen jurídico y relaciones con las Cortes (arts. 38 a 40; Estatuto, art. 9)", f"""
{unidad("3.1 Funciones del Consejo y del Presidente (art. 38)",
  lit(L, "Artículo 38", ["Informar preceptivamente los proyectos normativos de carácter estatal", "será presentada ante las Cortes Generales", "Adoptar criterios de interpretación uniforme", "Conocer de las reclamaciones", "Instar el inicio del procedimiento sancionador"]),
  fichab("Qué hace el Consejo y qué hace su Presidente",
         "Consejo (38.1) y Presidente (38.2)",
         ["Consejo: recomendaciones, asesoramiento, **informe preceptivo** de proyectos normativos estatales, evaluación y memoria anual, formación, colaboración", "Presidente: **criterios de interpretación uniforme**, velar por la publicidad activa, **conocer de las reclamaciones** del art. 24, responder consultas, **instar** el procedimiento sancionador, aprobar el anteproyecto de presupuesto"],
         "Memoria anual presentada ante las Cortes Generales",
         "Las reclamaciones las conoce el **Presidente** (38.2 c). Si insta un sancionador y no se incoa, la decisión debe **motivarse**."))}

{unidad("3.2 Régimen jurídico y Estatuto (art. 39.2)",
  lit(L, "Artículo 39", ["mediante Real Decreto el Estatuto del Consejo de Transparencia y Buen Gobierno"], solo=[7]),
  fichab("Habilitación para aprobar el Estatuto", "El **Consejo de Ministros**, mediante Real Decreto",
         "Organización, estructura, funcionamiento y demás aspectos necesarios", "—",
         "El Estatuto vigente es el aprobado por el **Real Decreto 615/2024, de 2 de julio** (→ V.1.2)."))}

{unidad("3.3 Relaciones con las Cortes Generales (art. 40; Estatuto, art. 9.2)",
  lit(L, "Artículo 40", ["anualmente a las Cortes Generales una memoria", "comparecerá ante la Comisión correspondiente"]),
  lit("RD615", "Artículo 9", ["se remitirá a las Cortes Generales"], solo=[5]),
  fichab("Rendición de cuentas del Consejo ante el Parlamento", "El Consejo eleva la memoria; el Presidente comparece",
         "Memoria sobre sus actividades y el grado de cumplimiento de la ley", "**Anual**; el Presidente comparece también cuantas veces sea requerido",
         "La memoria va a las **Cortes Generales** (no solo al Congreso). La Comisión la **aprueba** (Estatuto, art. 15 c)."))}
""", 2)

T.ap("s17", "V.4 Cuadro de plazos y mayorías del tema (esquema)", f"""
{NOLEGAL}

| Dato | Plazo o cifra | Fuente |
|---|---|---|
| Concretar una solicitud imprecisa | 10 días | Ley 19/2013, art. 19.2 |
| Alegaciones de terceros | 15 días | art. 19.3 |
| Resolver la solicitud de acceso | 1 mes, ampliable 1 mes; silencio desestimatorio | art. 20.1 y 20.4 |
| Formalizar el acceso | No más de 10 días | art. 22.1 |
| Interponer la reclamación ante el CTBG | 1 mes | art. 24.2 |
| Resolver la reclamación | 3 meses; silencio desestimatorio | art. 24.4 |
| Mandato del Presidente del CTBG | 5 años, no renovable | art. 37.1 |
| Refrendo del Presidente | Comisión del Congreso, mayoría absoluta, 1 mes natural | art. 37.1 |
| Reunión de la Comisión del CTBG | Al menos una vez al trimestre | Estatuto, art. 20.3 |
| Reunión con órganos autonómicos | Al menos una vez al año | art. 36.4 |
| Prescripción de infracciones y sanciones | 5, 3 y 1 años | art. 32 |
| Inhabilitación por infracción muy grave | 5 a 10 años | art. 30.4 |
| Pleno del Foro de Gobierno Abierto | Al menos dos veces al año; 64 vocales (32 + 32) | RD 371/2026, arts. 12.1 y 6.1 |
| V Plan de Gobierno Abierto | 10 compromisos y 218 iniciativas | Documento del V Plan |

{resumen([
  "El CTBG es hoy una **autoridad administrativa independiente** («A.A.I.»), con Estatuto aprobado por el **RD 615/2024**.",
  "Dos órganos: **Comisión** (Presidente, Diputado, Senador y 5 representantes) y **Presidente**.",
  "Presidente: **5 años no renovables**, por Real Decreto, con refrendo del **Congreso por mayoría absoluta**.",
  "El Presidente conoce de las **reclamaciones**, fija **criterios de interpretación** e **insta** sancionadores; memoria **anual** a las **Cortes**."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
EX_L39 = examen("L", 39, {
  "a": f"Literal del documento del V Plan: {cs('GA_VPLAN', 'contiene 10 compromisos')}; y en su prólogo: {cs('GA_VPLAN', 'el Plan recoge diez compromisos')}.",
  "b": f"Seis no: el V Plan enumera diez compromisos, del {cs('GA_VPLAN', '1. PARTICIPACIÓN Y ESPACIO CÍVICO.')} al {cs('GA_VPLAN', '10. ESTADO ABIERTO.')}",
  "c": f"Ocho no: el compromiso 8 es uno más ({cs('GA_VPLAN', '8. DIFUSION, FORMACIÓN Y PROMOCIÓN DEL GOBIERNO ABIERTO.')}); siguen el 9 y el 10.",
  "d": f"Cuatro no: el V Plan {cs('GA_VPLAN', 'contiene 10 compromisos')}. «Cuatro» recuerda al número de planes anteriores (I a IV)."},
  [("Diez", "GA_VPLAN", T_, "el Plan recoge diez compromisos")])
EX_P38 = examen("P", 38, {
  "a": f"125 no coincide con ningún dato del Plan: {cs('GA_VPLAN', 'las 218 iniciativas presentadas en conjunto por las diversas administraciones')}.",
  "b": f"347 no: el total es 218 ({cs('GA_VPLAN', '123 del ámbito central')}, 82 autonómicas y 13 locales).",
  "c": f"63 no: el total es 218, suma de {cs('GA_VPLAN', '123 del ámbito central (AGE, recogiendo iniciativas de 16 ministerios), 82 del ámbito autonómico y 13 del ámbito local')}.",
  "d": f"Literal del documento del V Plan: {cs('GA_VPLAN', 'se agrupan las 218 iniciativas presentadas en conjunto por las diversas administraciones')}."},
  [("218", "GA_VPLAN", T_, "las 218 iniciativas presentadas en conjunto por las diversas administraciones")])
EX_P39 = examen("P", 39, {
  "a": f"Semestre no: el art. 20.3 del Estatuto dice {c('RD615', 'Artículo 20', 'al menos una vez al trimestre')}.",
  "b": f"Literal del art. 20.3 del Estatuto: {c('RD615', 'Artículo 20', 'La comisión se reunirá al menos una vez al trimestre')}.",
  "c": f"«Al menos una vez al año» es la reunión con los órganos autonómicos análogos (Ley 19/2013, art. 36.4: {c(L, 'Artículo 36', 'Al menos una vez al año')}), no la periodicidad de la Comisión.",
  "d": f"Mes no: {c('RD615', 'Artículo 20', 'al menos una vez al trimestre')}."},
  [("Trimestre", "RD615", "Artículo 20", "La comisión se reunirá al menos una vez al trimestre")])
EX_X48 = examen("X", 48, {
  "a": f"No son las Cortes ni tres quintos: {c(L, 'Artículo 37', 'El Congreso, a través de la Comisión competente y por acuerdo adoptado por mayoría absoluta')}.",
  "b": f"Literal del art. 37.1: {c(L, 'Artículo 37', 'El Congreso, a través de la Comisión competente y por acuerdo adoptado por mayoría absoluta, deberá refrendar el nombramiento del candidato propuesto')}.",
  "c": f"El Senado no interviene: refrenda {c(L, 'Artículo 37', 'El Congreso')}, y por {c(L, 'Artículo 37', 'mayoría absoluta')}, no por dos tercios.",
  "d": f"Ni las Cortes ni dos tercios: {c(L, 'Artículo 37', 'El Congreso, a través de la Comisión competente y por acuerdo adoptado por mayoría absoluta')}."},
  [("Congreso de los Diputados", L, "Artículo 37", "ante la Comisión correspondiente del Congreso de los Diputados"),
   ("mayoría absoluta", L, "Artículo 37", "por acuerdo adoptado por mayoría absoluta, deberá refrendar el nombramiento del candidato propuesto")])

T.ap("s18", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **cuatro** preguntas de este tema: dos sobre el **V Plan de Gobierno Abierto** y dos sobre el **Consejo de Transparencia y Buen Gobierno**. Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra la fuente (texto legal o documento oficial del V Plan).",
  "### GACE-L 2025, pregunta 39 · Compromisos del V Plan (→ II.2.2)", EX_L39,
  "### GACE-P 2025, pregunta 38 · Iniciativas del V Plan (→ II.2.2)", EX_P38,
  "### GACE-P 2025, pregunta 39 · Reuniones de la Comisión de Transparencia y Buen Gobierno (→ V.2.4)", EX_P39,
  "### GACE-L 2025 extraordinario, pregunta 48 · Refrendo del Presidente del CTBG (→ V.2.3)", EX_X48,
  "### Cómo se pregunta",
  "!> Dos estilos: **datos del plan vigente** (número de compromisos e iniciativas, fecha de aprobación) y **cifras del CTBG** (quién refrenda y con qué mayoría, cada cuánto se reúne la Comisión). Los distractores cambian el **órgano** (Cortes, Senado), la **mayoría** (tres quintos, dos tercios) o el **periodo** (mes, semestre, año).",
]))

T.ap("s19", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Concepto y principios | Cultura de gobernanza (OCDE, 2017); transparencia, integridad, rendición de cuentas y participación; Foro de Gobierno Abierto (RD 371/2026) | Foro **paritario** 32 + 32, presidido por la **Secretaría de Estado de Función Pública** |
| II. Planes de acción | OGP (2011); I a IV Plan; V Plan 2025-2029 | V Plan: **10 compromisos**, **218 iniciativas**, aprobado el **6-10-2025** |
| III. Transparencia | Sujetos (arts. 2-4); publicidad activa (5-11); derecho de acceso (12-22); reclamación (24) | **1 mes** para resolver, silencio **negativo**; reclamación **potestativa**: 1 mes / 3 meses |
| IV. Buen gobierno | Principios (26); infracciones (27-29); sanciones (30); prescripción (32) | Inhabilitación **5 a 10 años**; prescripción **5-3-1** |
| V. CTBG | A.A.I. (RD 615/2024); Comisión y Presidente; funciones (38) | Refrendo: **Congreso, mayoría absoluta**; Comisión: **trimestral** |

?> **Trampas frecuentes:** «la definición de Gobierno Abierto es de la **OGP**» (es de la **OCDE**); «el V Plan tiene **ocho** compromisos» (son **diez**); «el silencio en el acceso es **positivo**» (es **desestimatorio**); «la reclamación ante el CTBG es **obligatoria**» (es **potestativa**); «refrendan las **Cortes** por **tres quintos**» (el **Congreso**, por **mayoría absoluta**); «la Comisión se reúne **una vez al año**» (al menos **una vez al trimestre**; la anual es con los órganos autonómicos); «el art. 3 obliga también al **derecho de acceso**» (solo a la **publicidad activa**).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
GA = "Gobierno Abierto"
T.q("GA_QUE", T_, GA, "Según la definición que recoge el Portal de la Transparencia, el Gobierno Abierto es:",
    ["Una cultura de gobernanza que promueve los principios de transparencia, integridad, rendición de cuentas y participación de las partes interesadas.", "Un órgano colegiado de participación de la sociedad civil adscrito a la Secretaría de Estado de Función Pública.", "El conjunto de obligaciones de publicidad activa de la Ley 19/2013.", "Una autoridad administrativa independiente encargada de garantizar el derecho de acceso."],
    "Portal de la Transparencia (definición de la Recomendación del Consejo de la OCDE de 14-12-2017). El órgano colegiado es el Foro; la autoridad independiente, el CTBG.", "El Gobierno Abierto es una cultura de gobernanza que promueve los principios de transparencia, integridad, rendición de cuentas y participación de las partes interesadas")
T.q("GA_QUE", T_, GA, "La definición de Gobierno Abierto que recoge el Portal de la Transparencia procede de:",
    ["La Recomendación del Consejo de la OCDE sobre Gobierno Abierto de 14 de diciembre de 2017.", "La Ley 19/2013, de 9 de diciembre.", "El Real Decreto 371/2026, de 6 de mayo.", "La Carta de los Derechos Fundamentales de la Unión Europea."],
    "Portal de la Transparencia: definición «recogida en la Recomendación del Consejo de la OCDE sobre Gobierno Abierto de 14 de diciembre de 2017». Ninguna ley española define el Gobierno Abierto.", "Recomendación del Consejo de la OCDE sobre Gobierno Abierto de 14 de diciembre de 2017")
T.q("GA_QUE", T_, "Planes de acción", "Según el Portal de la Transparencia, la Alianza para el Gobierno Abierto (OGP) fue fundada en:",
    ["Septiembre de 2011.", "Diciembre de 2013.", "Diciembre de 2017.", "Octubre de 2025."],
    "Portal de la Transparencia: la OGP, «fundada en septiembre de 2011»; España se unió ese mismo año. 2013 es la Ley 19/2013; 2017, la Recomendación de la OCDE; 2025, la IX Cumbre y el V Plan.", "fundada en septiembre de 2011")
T.q("GA_QUE", T_, "Planes de acción", "Según el Portal de la Transparencia, la evaluación del cumplimiento de los compromisos de los planes de acción de la OGP la realiza:",
    ["El Mecanismo de Revisión Independiente (MRI) de la Alianza.", "El Consejo de Transparencia y Buen Gobierno.", "El Tribunal de Cuentas.", "La Comisión Sectorial de Gobierno Abierto."],
    "Portal de la Transparencia: «La evaluación del cumplimento de estos compromisos la realiza el Mecanismo de Revisión Independiente (MRI) de la Alianza».", "la realiza el Mecanismo de Revisión Independiente (MRI) de la Alianza")
T.q("GA_QUE", T_, GA, "Según el Portal de la Transparencia, el impulso, la coordinación y el seguimiento de los planes de acción de Gobierno Abierto de España corresponden a:",
    ["La Dirección General de Gobernanza Pública.", "El Consejo de Transparencia y Buen Gobierno.", "La Oficina de Conflictos de Intereses.", "La Secretaría General de la Presidencia del Gobierno."],
    "Portal de la Transparencia: a la Dirección General de Gobernanza Pública del Ministerio para la Transformación Digital y de la Función Pública.", "A la Dirección General de Gobernanza Pública del Ministerio para la Transformación Digital y de la Función Pública le corresponde el impulso, la coordinación y el seguimiento de los planes de acción")
T.q("RD371", "Artículo 2", GA, "Según el artículo 2 del Real Decreto 371/2026, el Foro de Gobierno Abierto está adscrito a:",
    ["La Secretaría de Estado de Función Pública.", "El Consejo de Transparencia y Buen Gobierno.", "La Presidencia del Gobierno.", "La Secretaría de Estado de Hacienda."],
    "Art. 2.2 RD 371/2026.", "El Foro está adscrito a la Secretaría de Estado de Función Pública")
T.q("RD371", "Artículo 6", GA, "Según el artículo 6.1 del Real Decreto 371/2026, el Pleno del Foro de Gobierno Abierto está integrado, además de por la Presidencia y la Secretaría, por:",
    ["Sesenta y cuatro vocales, treinta y dos en representación de las administraciones públicas y treinta y dos en representación de la sociedad civil.", "Treinta y dos vocales, dieciséis de las administraciones públicas y dieciséis de la sociedad civil.", "Sesenta y cuatro vocales, cuarenta de las administraciones públicas y veinticuatro de la sociedad civil.", "Ocho vocales, como la Comisión de Transparencia y Buen Gobierno."],
    "Art. 6.1 RD 371/2026: composición paritaria 32 + 32.", "sesenta y cuatro vocales, treinta y dos en representación de las administraciones públicas y treinta y dos en representación de la sociedad civil")
T.q("RD371", "Artículo 12", GA, "Según el artículo 12.1 del Real Decreto 371/2026, el Pleno del Foro de Gobierno Abierto se reunirá con carácter ordinario:",
    ["Al menos dos veces al año.", "Al menos una vez al trimestre.", "Al menos una vez al mes.", "Al menos una vez al año."],
    "Art. 12.1 RD 371/2026. La «una vez al trimestre» es la Comisión de Transparencia y Buen Gobierno (Estatuto del CTBG, art. 20.3).", "se reunirá, con carácter ordinario, al menos dos veces al año")
T.q("RD371", "Artículo 12", GA, "Según el artículo 12.4 del Real Decreto 371/2026, si en el Foro de Gobierno Abierto no se alcanza el consenso, las decisiones se adoptan por:",
    ["Mayoría simple de los miembros asistentes con derecho a voto.", "Mayoría absoluta de los miembros del Pleno.", "Mayoría de dos tercios de los miembros asistentes.", "Unanimidad de las vocalías de la sociedad civil."],
    "Art. 12.4 RD 371/2026: preferentemente por consenso; si no, mayoría simple de los asistentes con derecho a voto.", "requiriéndose mayoría simple de los miembros asistentes con derecho a voto")
T.q("RD371", "Artículo 19", GA, "Según el artículo 19.2 del Real Decreto 371/2026, el Observatorio de Gobierno Abierto contará con un entorno propio dentro de:",
    ["El Portal de la Transparencia.", "La sede electrónica del Consejo de Transparencia y Buen Gobierno.", "El Boletín Oficial del Estado.", "La Plataforma de Contratación del Sector Público."],
    "Art. 19.2 RD 371/2026.", "El Observatorio contará con un entorno propio dentro del Portal de la Transparencia")
T.q("GA_VPLAN", T_, "Planes de acción", "Según el documento del V Plan de Gobierno Abierto de España, el hito del II Plan (2014-2016) fue:",
    ["La puesta en marcha del Portal de la Transparencia.", "La aprobación de la Ley de Transparencia.", "La creación del Foro de Gobierno Abierto.", "La ratificación por España del Convenio de Tromsø."],
    "V Plan, visión global: I Plan, Ley de Transparencia; II Plan, Portal; III Plan, Foro; IV Plan, Tromsø y Sistema de Integridad.", "II Plan (2014-2016): puesta en marcha del Portal de la Transparencia")
T.q("GA_VPLAN", T_, "Planes de acción", "Según el documento del V Plan de Gobierno Abierto de España, el III Plan (2017-2019) se caracterizó por:",
    ["La creación del Foro de Gobierno Abierto.", "La puesta en marcha del Portal de la Transparencia.", "La aprobación de la Ley de Transparencia.", "La aprobación del Sistema de Integridad de la Administración General del Estado."],
    "V Plan, visión global: «III Plan (2017-2019): creación del Foro de Gobierno Abierto».", "III Plan (2017-2019): creación del Foro de Gobierno Abierto")
T.q("GA_VPLAN", T_, "Planes de acción", "Según el documento del V Plan de Gobierno Abierto de España 2025-2029, el V Plan fue aprobado:",
    ["En la reunión del pleno del Foro de 6 de octubre de 2025.", "Por el Consejo de Ministros el 6 de mayo de 2026.", "Por la Comisión de Transparencia y Buen Gobierno el 9 de diciembre de 2025.", "Por las Cortes Generales mediante ley."],
    "V Plan: «fue aprobado en la reunión del pleno del Foro de 6 de octubre de 2025». El 6 de mayo de 2026 es la fecha del RD 371/2026.", "El V Plan de Gobierno Abierto 2025-2029 fue aprobado en la reunión del pleno del Foro de 6 de octubre de 2025")
T.q("GA_VPLAN", T_, "Planes de acción", "Según el documento del V Plan de Gobierno Abierto de España 2025-2029, el compromiso 10 se denomina:",
    ["Estado Abierto.", "Observatorio de Gobierno Abierto.", "Participación y espacio cívico.", "Administración Abierta."],
    "V Plan: el décimo, «ESTADO ABIERTO», agrupa las aportaciones de comunidades autónomas y entidades locales; el 9 es el Observatorio, el 1 participación y espacio cívico y el 4 Administración Abierta.", "10. ESTADO ABIERTO.")
T.q(L, "Artículo 1", "Ley 19/2013", "Según el artículo 1 de la Ley 19/2013, esta Ley tiene por objeto, entre otros:",
    ["Regular y garantizar el derecho de acceso a la información relativa a la actividad pública.", "Regular el procedimiento administrativo común de las Administraciones Públicas.", "Regular la reutilización de la información del sector público.", "Crear el Foro de Gobierno Abierto."],
    "Art. 1: ampliar y reforzar la transparencia, regular y garantizar el derecho de acceso y establecer las obligaciones de buen gobierno.", "regular y garantizar el derecho de acceso a la información relativa a aquella actividad")
T.q(L, "Artículo 2", "Ley 19/2013", "Según el artículo 2.1 g) de la Ley 19/2013, se incluyen en su ámbito de aplicación las sociedades mercantiles en cuyo capital social la participación de las entidades del artículo sea:",
    ["Superior al 50 por 100.", "Igual o superior al 25 por 100.", "Superior al 40 por 100.", "Mayoritaria o minoritaria, en todo caso."],
    "Art. 2.1 g): participación, directa o indirecta, «superior al 50 por 100».", "sea superior al 50 por 100")
T.q(L, "Artículo 3", "Ley 19/2013", "Según el artículo 3 b) de la Ley 19/2013, las entidades privadas quedan sujetas a la publicidad activa si perciben durante un año ayudas o subvenciones públicas en una cuantía superior a:",
    ["100.000 euros.", "50.000 euros.", "5.000 euros.", "300.000 euros."],
    "Art. 3 b): más de 100.000 euros, o al menos el 40 % de sus ingresos con un mínimo de 5.000 euros.", "en una cuantía superior a 100.000 euros")
T.q(L, "Artículo 3", "Ley 19/2013", "Según el artículo 3 de la Ley 19/2013, a los partidos políticos, organizaciones sindicales y organizaciones empresariales les son aplicables:",
    ["Las disposiciones del capítulo II del título I (publicidad activa).", "Todas las disposiciones del título I, incluido el derecho de acceso.", "Únicamente las disposiciones del título II (buen gobierno).", "Las disposiciones del título III."],
    "Art. 3: «Las disposiciones del capítulo II de este título serán también aplicables a…».", "Las disposiciones del capítulo II de este título serán también aplicables a")
T.q(L, "Artículo 6", "Publicidad activa", "Según el artículo 6.2 de la Ley 19/2013, en el ámbito de la Administración General del Estado la evaluación del cumplimiento de los planes y programas corresponde a:",
    ["Las inspecciones generales de servicios.", "El Consejo de Transparencia y Buen Gobierno.", "La Intervención General de la Administración del Estado.", "El Tribunal de Cuentas."],
    "Art. 6.2, párrafo segundo.", "corresponde a las inspecciones generales de servicios la evaluación del cumplimiento de estos planes y programas")
T.q(L, "Artículo 8", "Publicidad activa", "Según el artículo 8.1 a) de la Ley 19/2013, la publicación de la información relativa a los contratos menores:",
    ["Podrá realizarse trimestralmente.", "Deberá realizarse mensualmente.", "Podrá realizarse anualmente.", "No es obligatoria."],
    "Art. 8.1 a): «La publicación de la información relativa a los contratos menores podrá realizarse trimestralmente».", "La publicación de la información relativa a los contratos menores podrá realizarse trimestralmente")
T.q(L, "Artículo 9", "Publicidad activa", "Según el artículo 9.3 de la Ley 19/2013, el incumplimiento reiterado de las obligaciones de publicidad activa tendrá la consideración de:",
    ["Infracción grave a efectos del régimen disciplinario.", "Infracción muy grave a efectos del régimen disciplinario.", "Infracción leve a efectos del régimen disciplinario.", "Delito de desobediencia."],
    "Art. 9.3.", "tendrá la consideración de infracción grave")
T.q(L, "Artículo 11", "Publicidad activa", "Según el artículo 11 de la Ley 19/2013, la información del Portal de la Transparencia debe adecuarse a los principios de:",
    ["Accesibilidad, interoperabilidad y reutilización.", "Publicidad, concurrencia y transparencia.", "Eficacia, economía y eficiencia.", "Gratuidad, celeridad y proporcionalidad."],
    "Art. 11: a) Accesibilidad, b) Interoperabilidad, c) Reutilización.", ["Accesibilidad:", "Interoperabilidad:", "Reutilización:"])
T.q(L, "Artículo 12", "Derecho de acceso", "Según el artículo 12 de la Ley 19/2013, son titulares del derecho a acceder a la información pública:",
    ["Todas las personas.", "Los ciudadanos españoles.", "Los interesados en un procedimiento administrativo.", "Las personas físicas mayores de edad."],
    "Art. 12: «Todas las personas tienen derecho a acceder a la información pública».", "Todas las personas tienen derecho a acceder a la información pública")
T.q(L, "Artículo 14", "Derecho de acceso", "¿Cuál de los siguientes es un límite al derecho de acceso recogido en el artículo 14.1 de la Ley 19/2013?",
    ["La protección del medio ambiente.", "La eficiencia en el uso de los recursos públicos.", "La carga de trabajo del órgano.", "El interés particular del solicitante."],
    "Art. 14.1 l): «La protección del medio ambiente».", "La protección del medio ambiente")
T.q(L, "Artículo 15", "Derecho de acceso", "Según el artículo 15.1 de la Ley 19/2013, si la información solicitada contuviera datos personales que revelen la ideología, afiliación sindical, religión o creencias, el acceso únicamente se podrá autorizar con:",
    ["El consentimiento expreso y por escrito del afectado, salvo que este los hubiese hecho manifiestamente públicos con anterioridad.", "El consentimiento tácito del afectado.", "La autorización del Consejo de Transparencia y Buen Gobierno.", "Una ponderación del interés público, sin necesidad de consentimiento."],
    "Art. 15.1, párrafo primero.", "consentimiento expreso y por escrito del afectado")
T.q(L, "Artículo 17", "Derecho de acceso", "Según el artículo 17.3 de la Ley 19/2013, el solicitante de acceso a la información:",
    ["No está obligado a motivar su solicitud.", "Debe motivar siempre su solicitud.", "Debe acreditar la condición de interesado.", "Debe motivar su solicitud cuando la información contenga datos personales."],
    "Art. 17.3: «El solicitante no está obligado a motivar su solicitud de acceso a la información».", "El solicitante no está obligado a motivar su solicitud de acceso a la información")
T.q(L, "Artículo 18", "Derecho de acceso", "Según el artículo 18.1 de la Ley 19/2013, se inadmitirán a trámite las solicitudes relativas a información para cuya divulgación sea necesaria:",
    ["Una acción previa de reelaboración.", "La consulta a un tercero afectado.", "Una ampliación del plazo de resolución.", "La disociación de datos personales."],
    "Art. 18.1 c). La consulta a terceros (art. 19.3), la ampliación de plazo (20.1) y la disociación (15.4) no son causas de inadmisión.", "Relativas a información para cuya divulgación sea necesaria una acción previa de reelaboración")
T.q(L, "Artículo 19", "Derecho de acceso", "Según el artículo 19.3 de la Ley 19/2013, si la información solicitada pudiera afectar a derechos o intereses de terceros, se les concederá para alegaciones un plazo de:",
    ["Quince días.", "Diez días.", "Un mes.", "Cinco días."],
    "Art. 19.3: quince días. Diez días es el plazo para concretar la solicitud (19.2).", "se les concederá un plazo de quince días")
T.q(L, "Artículo 20", "Derecho de acceso", "Según el artículo 20.1 de la Ley 19/2013, la resolución que conceda o deniegue el acceso deberá notificarse en el plazo máximo de:",
    ["Un mes desde la recepción de la solicitud por el órgano competente para resolver.", "Tres meses desde la presentación de la solicitud.", "Quince días desde la recepción de la solicitud.", "Un mes desde la presentación de la solicitud en cualquier registro."],
    "Art. 20.1: un mes desde la recepción por el órgano competente, ampliable por otro mes.", "en el plazo máximo de un mes desde la recepción de la solicitud por el órgano competente para resolver")
T.q(L, "Artículo 20", "Derecho de acceso", "Según el artículo 20.4 de la Ley 19/2013, transcurrido el plazo máximo para resolver sin resolución expresa, la solicitud de acceso:",
    ["Se entenderá desestimada.", "Se entenderá estimada.", "Se entenderá estimada parcialmente.", "Se archivará por caducidad."],
    "Art. 20.4: silencio desestimatorio.", "se entenderá que la solicitud ha sido desestimada")
T.q(L, "Artículo 22", "Derecho de acceso", "Según el artículo 22.4 de la Ley 19/2013, el acceso a la información:",
    ["Será gratuito, aunque la expedición de copias podrá dar lugar a exacciones.", "Estará sujeto siempre a una tasa.", "Será gratuito solo para las personas físicas.", "Será gratuito solo si se realiza por vía electrónica."],
    "Art. 22.4.", "El acceso a la información será gratuito")
T.q(L, "Artículo 24", "Reclamación", "Según el artículo 24.1 de la Ley 19/2013, la reclamación ante el Consejo de Transparencia y Buen Gobierno tiene carácter:",
    ["Potestativo y previo a su impugnación en vía contencioso-administrativa.", "Obligatorio y previo a la vía contencioso-administrativa.", "Potestativo y posterior al recurso de alzada.", "Obligatorio y sustitutivo de la vía judicial."],
    "Art. 24.1.", "con carácter potestativo y previo a su impugnación en vía contencioso-administrativa")
T.q(L, "Artículo 24", "Reclamación", "Según el artículo 24.4 de la Ley 19/2013, el plazo máximo para resolver y notificar la reclamación ante el Consejo de Transparencia y Buen Gobierno será de:",
    ["Tres meses, transcurrido el cual se entenderá desestimada.", "Un mes, transcurrido el cual se entenderá estimada.", "Tres meses, transcurrido el cual se entenderá estimada.", "Seis meses, transcurrido el cual se entenderá desestimada."],
    "Art. 24.4. Un mes es el plazo para interponerla (24.2).", "El plazo máximo para resolver y notificar la resolución será de tres meses, transcurrido el cual, la reclamación se entenderá desestimada")
T.q(L, "Artículo 26", "Buen gobierno", "Según el artículo 26.3 de la Ley 19/2013, los principios de buen gobierno:",
    ["Informarán la interpretación y aplicación del régimen sancionador regulado en ese título.", "Tienen carácter meramente programático, sin efectos jurídicos.", "Solo se aplican a los miembros del Gobierno.", "Se sancionan siempre como infracciones muy graves."],
    "Art. 26.3.", "informarán la interpretación y aplicación del régimen sancionador")
T.q(L, "Artículo 29", "Buen gobierno", "Según el artículo 29 de la Ley 19/2013, el abuso de autoridad en el ejercicio del cargo es una infracción:",
    ["Grave.", "Muy grave.", "Leve.", "No está tipificado en esa ley."],
    "Art. 29.2 a): infracción grave. El acoso laboral es muy grave (29.1 k).", "El abuso de autoridad en el ejercicio del cargo.")
T.q(L, "Artículo 30", "Buen gobierno", "Según el artículo 30.4 de la Ley 19/2013, los sancionados por una infracción muy grave no podrán ser nombrados alto cargo o asimilado durante un periodo de:",
    ["Entre cinco y diez años.", "Entre uno y tres años.", "Entre tres y cinco años.", "Diez años, en todo caso."],
    "Art. 30.4.", "durante un periodo de entre cinco y diez años")
T.q(L, "Artículo 30", "Buen gobierno", "Según el artículo 30.1 de la Ley 19/2013, las infracciones leves serán sancionadas con:",
    ["Una amonestación.", "La destitución del cargo.", "La publicación del incumplimiento en el «Boletín Oficial del Estado».", "La pérdida de la indemnización por cese."],
    "Art. 30.1. La publicación en el BOE y la pérdida de la indemnización son sanciones de las graves (30.2); la destitución, de las muy graves (30.4).", "Las infracciones leves serán sancionadas con una amonestación")
T.q(L, "Artículo 31", "Buen gobierno", "Según el artículo 31.3 de la Ley 19/2013, la instrucción de los procedimientos sancionadores contra miembros del Gobierno, Secretarios de Estado y demás altos cargos de la Administración General del Estado corresponde a:",
    ["La Oficina de Conflictos de Intereses.", "El Consejo de Transparencia y Buen Gobierno.", "El Tribunal de Cuentas.", "La Inspección General de Servicios de cada Ministerio."],
    "Art. 31.3. El Presidente del CTBG solo puede instar el inicio (art. 38.2 e).", "la instrucción de los correspondientes procedimientos corresponderá a la Oficina de Conflictos de Intereses")
T.q(L, "Artículo 32", "Buen gobierno", "Según el artículo 32.1 de la Ley 19/2013, las infracciones graves prescriben a los:",
    ["Tres años.", "Cinco años.", "Un año.", "Seis meses."],
    "Art. 32.1: cinco años las muy graves, tres las graves y uno las leves.", "tres años para las graves")
T.q("RD615", "Artículo 1", "CTBG", "Según el artículo 1.1 de su Estatuto (Real Decreto 615/2024), el Consejo de Transparencia y Buen Gobierno es:",
    ["Una autoridad administrativa independiente de ámbito estatal.", "Un órgano colegiado de la Secretaría de Estado de Función Pública.", "Un organismo autónomo dependiente del Ministerio de Hacienda.", "Una comisión del Congreso de los Diputados."],
    "Art. 1.1 del Estatuto: autoridad administrativa independiente de ámbito estatal (arts. 109 y 110 de la Ley 40/2015); denominación «Consejo de Transparencia y Buen Gobierno, A.A.I.».", "es una autoridad administrativa independiente de ámbito estatal")
T.q(L, "Artículo 35", "CTBG", "Según el artículo 35 de la Ley 19/2013, el Consejo de Transparencia y Buen Gobierno está compuesto por:",
    ["La Comisión de Transparencia y Buen Gobierno y el Presidente del Consejo, que lo será también de su Comisión.", "El Pleno, la Comisión Permanente y los grupos de trabajo.", "El Presidente, el Vicepresidente y el Secretario General.", "La Comisión de Transparencia y Buen Gobierno y el Defensor del Pueblo."],
    "Art. 35. Pleno, Comisión Permanente y grupos de trabajo son del Foro de Gobierno Abierto (RD 371/2026, art. 4).", "El Presidente del Consejo de Transparencia y Buen Gobierno que lo será también de su Comisión")
T.q(L, "Artículo 36", "CTBG", "Según el artículo 36.2 de la Ley 19/2013, ¿cuál de los siguientes forma parte de la Comisión de Transparencia y Buen Gobierno?",
    ["Un representante de la Autoridad Independiente de Responsabilidad Fiscal.", "Un representante del Consejo General del Poder Judicial.", "Un representante del Consejo de Estado.", "Un representante de la Federación Española de Municipios y Provincias."],
    "Art. 36.2 h). A la reunión anual con los órganos autonómicos (36.4) solo «podrá ser convocado» un representante de la Administración Local propuesto por la FEMP; no es miembro de la Comisión.", "Un representante de la Autoridad Independiente de Responsabilidad Fiscal")
T.q(L, "Artículo 37", "CTBG", "Según el artículo 37.1 de la Ley 19/2013, el Presidente del Consejo de Transparencia y Buen Gobierno será nombrado:",
    ["Por un período no renovable de cinco años mediante Real Decreto.", "Por un período de cinco años, renovable por una sola vez, mediante Real Decreto.", "Por un período no renovable de seis años por las Cortes Generales.", "Por un período de cuatro años mediante Orden ministerial."],
    "Art. 37.1.", "será nombrado por un período no renovable de cinco años mediante Real Decreto")
T.q(L, "Artículo 38", "CTBG", "Según el artículo 38.2 de la Ley 19/2013, conocer de las reclamaciones que se presenten en aplicación del artículo 24 es función de:",
    ["El Presidente del Consejo de Transparencia y Buen Gobierno.", "La Comisión de Transparencia y Buen Gobierno.", "El Defensor del Pueblo.", "La Agencia Española de Protección de Datos."],
    "Art. 38.2 c): función del Presidente.", "Conocer de las reclamaciones que se presenten en aplicación del artículo 24 de esta Ley")
T.q(L, "Artículo 40", "CTBG", "Según el artículo 40 de la Ley 19/2013, el Consejo de Transparencia y Buen Gobierno elevará anualmente una memoria sobre el desarrollo de sus actividades a:",
    ["Las Cortes Generales.", "El Consejo de Ministros.", "El Tribunal de Cuentas.", "El Defensor del Pueblo."],
    "Art. 40.", "elevará anualmente a las Cortes Generales una memoria")
T.real("L", 39, "Planes de acción"); T.real("P", 38, "Planes de acción"); T.real("P", 39, "CTBG"); T.real("X", 48, "CTBG")

# Flashcards
for q_, a_, cat in [
  ("¿Qué es el Gobierno Abierto según el Portal de la Transparencia?", "Una cultura de gobernanza que promueve los principios de transparencia, integridad, rendición de cuentas y participación de las partes interesadas (Recomendación del Consejo de la OCDE, 14-12-2017).", GA),
  ("Pilares del Gobierno Abierto en el Observatorio (RD 371/2026, art. 19.4)", "Transparencia; participación ciudadana; rendición de cuentas; integridad pública; colaboración y cocreación.", GA),
  ("Foro de Gobierno Abierto: norma, adscripción y presidencia", "RD 371/2026; adscrito a la Secretaría de Estado de Función Pública, cuyo titular lo preside.", GA),
  ("Composición del Pleno del Foro de Gobierno Abierto", "Presidencia, Secretaría y 64 vocales: 32 de las administraciones públicas y 32 de la sociedad civil.", GA),
  ("¿Cuándo nació la OGP y cuándo se unió España?", "Septiembre de 2011; España se unió ese mismo año.", "Planes de acción"),
  ("Hitos de los planes I a IV", "I (2012-2014): Ley de Transparencia; II (2014-2016): Portal de la Transparencia; III (2017-2019): Foro de Gobierno Abierto; IV (2020-2024): Convenio de Tromsø y Sistema de Integridad de la AGE.", "Planes de acción"),
  ("V Plan de Gobierno Abierto: aprobación, compromisos e iniciativas", "Pleno del Foro, 6-10-2025; 10 compromisos y 218 iniciativas (123 AGE, 82 autonómicas, 13 locales).", "Planes de acción"),
  ("Objeto de la Ley 19/2013 (art. 1)", "Ampliar y reforzar la transparencia; regular y garantizar el derecho de acceso; establecer las obligaciones de buen gobierno.", "Ley 19/2013"),
  ("Umbrales del art. 3 b) para entidades privadas", "Más de 100.000 € de ayudas en un año, o al menos el 40 % de sus ingresos con un mínimo de 5.000 €. Solo publicidad activa.", "Ley 19/2013"),
  ("Principios técnicos del Portal de la Transparencia (art. 11)", "Accesibilidad, interoperabilidad y reutilización.", "Publicidad activa"),
  ("Titulares del derecho de acceso (art. 12)", "Todas las personas, sin necesidad de motivar la solicitud (art. 17.3).", "Derecho de acceso"),
  ("Plazos del procedimiento de acceso", "Concretar: 10 días; alegaciones de terceros: 15 días; resolver: 1 mes ampliable 1 mes; formalizar: no más de 10 días.", "Derecho de acceso"),
  ("Sentido del silencio en el derecho de acceso (art. 20.4)", "Desestimatorio.", "Derecho de acceso"),
  ("Causas de inadmisión (art. 18)", "Información en elaboración; auxiliar o de apoyo; que exige reelaboración; órgano sin la información y competente desconocido; solicitudes repetitivas o abusivas.", "Derecho de acceso"),
  ("Reclamación ante el CTBG (art. 24)", "Potestativa y previa al contencioso; 1 mes para interponer; 3 meses para resolver; silencio desestimatorio.", "Reclamación"),
  ("Sanciones del título II (art. 30)", "Leve: amonestación. Grave: publicación del incumplimiento en el BOE y sin indemnización por cese. Muy grave: además, destitución e inhabilitación para alto cargo de 5 a 10 años.", "Buen gobierno"),
  ("Prescripción de infracciones y sanciones (art. 32)", "Muy graves 5 años; graves 3; leves 1.", "Buen gobierno"),
  ("Naturaleza actual del CTBG", "Autoridad administrativa independiente de ámbito estatal: «Consejo de Transparencia y Buen Gobierno, A.A.I.» (Estatuto, RD 615/2024, art. 1).", "CTBG"),
  ("Composición de la Comisión de Transparencia y Buen Gobierno (art. 36.2)", "Presidente; un Diputado; un Senador; representantes del Tribunal de Cuentas, del Defensor del Pueblo, de la AEPD, de la Secretaría de Estado de Administraciones Públicas y de la AIReF.", "CTBG"),
  ("Presidente del CTBG: nombramiento y mandato (art. 37.1)", "Real Decreto; cinco años no renovables; refrendo de la Comisión competente del Congreso por mayoría absoluta en un mes natural.", "CTBG"),
  ("¿Cada cuánto se reúne la Comisión de Transparencia y Buen Gobierno?", "Al menos una vez al trimestre (Estatuto, art. 20.3). Al menos una vez al año convoca a los órganos autonómicos análogos (Ley 19/2013, art. 36.4).", "CTBG"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Gobierno Abierto", "Cultura de gobernanza que promueve los principios de transparencia, integridad, rendición de cuentas y participación de las partes interesadas (definición de la OCDE recogida en el Portal de la Transparencia).", "s1", GA)
T.glos("Alianza para el Gobierno Abierto (OGP)", "Organización multilateral fundada en septiembre de 2011 que trabaja mediante planes de acción con compromisos concretos; España es miembro desde ese año.", "s4", "Planes de acción")
T.glos("Plan de Gobierno Abierto", "Conjunto de actuaciones a las que se compromete la AGE, con otras Administraciones y la sociedad civil, para avanzar en un período en participación, transparencia, integridad y sensibilización social.", "s4", "Planes de acción")
T.glos("Foro de Gobierno Abierto", "Órgano colegiado de participación paritaria de la sociedad civil en materia de gobierno abierto, adscrito a la Secretaría de Estado de Función Pública (RD 371/2026).", "s3", GA)
T.glos("Observatorio de Gobierno Abierto", "Espacio virtual, dentro del Portal de la Transparencia, para identificar y difundir buenas prácticas de Gobierno Abierto (RD 371/2026, art. 19).", "s3", GA)
T.glos("Publicidad activa", "Obligación de publicar de forma periódica y actualizada, sin solicitud previa, la información relevante para la transparencia de la actividad pública (Ley 19/2013, arts. 5 a 11).", "s7", "Publicidad activa")
T.glos("Portal de la Transparencia", "Portal de la AGE que facilita el acceso a la información de publicidad activa y a la que se solicita con más frecuencia (Ley 19/2013, art. 10).", "s7", "Publicidad activa")
T.glos("Información pública", "Contenidos o documentos, cualquiera que sea su formato o soporte, en poder de los sujetos del título I, elaborados o adquiridos en el ejercicio de sus funciones (Ley 19/2013, art. 13).", "s8", "Derecho de acceso")
T.glos("Acceso parcial", "Acceso a la información no afectada por un límite, omitiendo la afectada e indicándolo al solicitante (Ley 19/2013, art. 16).", "s8", "Derecho de acceso")
T.glos("Reclamación ante el CTBG", "Impugnación potestativa y previa a la vía contencioso-administrativa, sustitutiva de los recursos administrativos, frente a resoluciones expresas o presuntas en materia de acceso (Ley 19/2013, arts. 23 y 24).", "s10", "Reclamación")
T.glos("Alto cargo (a efectos del buen gobierno)", "El que tenga esa consideración según la normativa de conflictos de intereses (Ley 19/2013, art. 25.1).", "s11", "Buen gobierno")
T.glos("Consejo de Transparencia y Buen Gobierno, A.A.I.", "Autoridad administrativa independiente de ámbito estatal que promueve la transparencia, vela por la publicidad activa, salvaguarda el derecho de acceso y garantiza el buen gobierno (Ley 19/2013, arts. 33 y 34; Estatuto, art. 1).", "s14", "CTBG")
T.glos("Comisión de Transparencia y Buen Gobierno", "Órgano colegiado del CTBG presidido por su Presidente, con un Diputado, un Senador y representantes de cinco instituciones (Ley 19/2013, art. 36).", "s15", "CTBG")

# Cronología (fechas de los metadatos del BOE y del Portal de la Transparencia)
T.hito("2013", "Ley 19/2013, de 9 de diciembre, de transparencia, acceso a la información pública y buen gobierno (BOE de 10-12-2013)", "Título II en vigor al día siguiente; títulos preliminar, I y III, al año de su publicación (disp. final novena)", "normativo", "s6")
T.hito("2014", "Real Decreto 919/2014, de 31 de octubre, primer Estatuto del Consejo de Transparencia y Buen Gobierno (BOE de 5-11-2014)", "Derogado por el Real Decreto 615/2024", "normativo", "s14")
T.hito("2022", "Ley 14/2022, de 8 de julio, de modificación de la Ley 19/2013 (BOE de 9-7-2022)", "Estadísticas de participación de pymes en la contratación pública (art. 8.1 a)", "normativo", "s7")
T.hito("2024", "Real Decreto 615/2024, de 2 de julio, Estatuto del Consejo de Transparencia y Buen Gobierno, A.A.I. (BOE de 2-8-2024)", "El Consejo, autoridad administrativa independiente", "normativo", "s14")
T.hito("2025", "Aprobación del V Plan de Gobierno Abierto 2025-2029 por el pleno del Foro de Gobierno Abierto (6-10-2025, según el Portal de la Transparencia)", "10 compromisos y 218 iniciativas", "institucional", "s5")
T.hito("2026", "Real Decreto 371/2026, de 6 de mayo, por el que se crea y regula el Foro de Gobierno Abierto (BOE de 7-5-2026)", "Deja sin efectos la Orden HFP/134/2018", "normativo", "s3")

T.publicar()
