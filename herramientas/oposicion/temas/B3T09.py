# -*- coding: utf-8 -*-
"""Tema III.9 (B3T09): Políticas de igualdad y contra la violencia de género: régimen
jurídico. Políticas de igualdad de trato y no discriminación de las personas LGTBI.
Discapacidad y dependencia: régimen jurídico.
Método del I.2. Normas (textos consolidados del BOE): CE, arts. 9.2, 14 y 49; LO 3/2007;
LO 1/2004; RD 246/2024 (Ministerio de Igualdad); Ley 15/2022; Ley 4/2023; RD 1026/2024;
RDLeg 1/2013 (LGD); Ley 39/2006; RD 1051/2013 (anexo II). Resolución de 16-3-2023 (BOE-A-2023-7326,
plan conjunto plurianual 2023-2027). Fuente oficial no legal: «Medidas del Pacto de Estado
contra la violencia de género 2025» (Delegación del Gobierno contra la Violencia de Género, igualdad.gob.es)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plantilla import *
from plantilla import _norm

CORTO.update({"LO3_2007": "LO 3/2007", "LO1_2004": "LO 1/2004", "L15_2022": "Ley 15/2022", "L4_2023": "Ley 4/2023",
              "LGD": "RDLeg 1/2013", "L39_2006": "Ley 39/2006", "RD246": "RD 246/2024", "RD1026": "RD 1026/2024",
              "RD1051": "RD 1051/2013"})

# --- Fuente oficial que no es texto legal (boe/PACTO2025.json, extraído del PDF oficial) ---
URL = {"PACTO2025": "https://violenciagenero.igualdad.gob.es/wp-content/uploads/Medidas-Renovacion-Pacto-de-Estado-en-materia-de-violencia-de-genero.pdf"}
T_ = "Texto"


def doc(k, cab, frases, resaltar=()):
    t = texto(k, T_)
    out = []
    for f in frases:
        assert _norm(f) in _norm(t), ("FUENTE NO LITERAL", k, f)
        for r in resaltar:
            if r in f: f = f.replace(r, "**" + r + "**", 1)
        out.append(f)
    for r in resaltar: assert any(r in f for f in frases), ("NEGRITA NO LITERAL", k, r)
    return "\n".join([f"> [[GOBES|{URL[k]}]]", "> **" + cab + "**"] + ["> " + x for x in out])


NOLEGAL = "*Esquema de elaboración propia: resume los artículos citados; no es texto legal.*"
D = "Disposición adicional primera"

T = Tema("B3T09",
  "Cinco preguntas: I. Qué exige la igualdad entre mujeres y hombres (CE, arts. 9.2 y 14; LO 3/2007) · II. Cómo se combate la violencia de género (LO 1/2004; RD 246/2024; Pacto de Estado y plan conjunto) · III. Cómo se garantiza la igualdad de trato y de las personas LGTBI (Ley 15/2022; Ley 4/2023; RD 1026/2024) · IV. Qué régimen tiene la discapacidad (CE, art. 49; RDLeg 1/2013) · V. Cómo se atiende la dependencia (Ley 39/2006; RD 1051/2013). Cada artículo: texto literal del BOE y ficha.",
  ["LO 3/2007", "Igualdad efectiva", "Composición equilibrada", "Planes de igualdad", "LO 1/2004", "Violencia de género", "Delegación del Gobierno", "Pacto de Estado", "Ley 15/2022", "Autoridad Independiente", "Ley 4/2023", "LGTBI", "Acoso discriminatorio", "Discapacidad", "Art. 49 CE", "Cuota de reserva", "Ley 39/2006", "Dependencia", "Grados de dependencia"])

# =============================================================================
T.ap("s0", "Mapa del tema: cinco preguntas", f"""
**Epígrafe oficial** (BOE-A-2025-26262, anexo VII, Bloque III, tema 9):
> Políticas de igualdad y contra la violencia de género: régimen jurídico. Políticas de igualdad de trato y no discriminación de las personas LGTBI. Discapacidad y dependencia: régimen jurídico.

### El hilo conductor

| Bloque | Pregunta | Constitución | Otras normas |
|---|---|---|---|
| **I** | ¿Qué exige la igualdad entre mujeres y hombres? | Arts. 9.2 y 14 | LO 3/2007, arts. 1, 3, 6 a 8, 11, 12, 14, 15, 17, 19, 45, 46, 51 a 53, 55, 64, 76 a 78 y disp. adic. 1.ª |
| **II** | ¿Cómo se combate la violencia de género? | — | LO 1/2004, arts. 1 a 3, 17 a 21, 23 a 27, 29 y 30; RD 246/2024, art. 2.3; Resolución de 16-3-2023 (plan conjunto); Pacto de Estado (fuente oficial) |
| **III** | ¿Cómo se garantiza la igualdad de trato y la de las personas LGTBI? | — | Ley 15/2022, arts. 1, 2, 4, 6, 40 y 41; Ley 4/2023, arts. 1, 3, 9, 15, 43 y 44; RD 1026/2024, arts. 1 y 2 y anexo I |
| **IV** | ¿Qué régimen jurídico tiene la discapacidad? | Art. 49 | RDLeg 1/2013 (LGD), arts. 1 a 4, 35, 37, 42, 55, 56, 63 y 73 |
| **V** | ¿Cómo se atiende la dependencia? | — | Ley 39/2006, arts. 1 a 3, 5, 6, 8, 9, 14, 15, 17 a 19, 23, 26 a 29 y 33; RD 1051/2013, anexo II |

!> **La idea que une los cinco bloques:** la Constitución obliga a los poderes públicos a hacer la igualdad **real y efectiva** (art. 9.2) y prohíbe la discriminación (art. 14). Cada ley del tema desarrolla ese mandato para un grupo: las **mujeres** (LO 3/2007), las **víctimas de violencia de género** (LO 1/2004), **toda persona** frente a cualquier causa de discriminación (Ley 15/2022), las **personas LGTBI** (Ley 4/2023), las **personas con discapacidad** (CE, art. 49, y LGD) y las **personas en situación de dependencia** (Ley 39/2006). Todas repiten el mismo esquema: **definiciones** (discriminación directa, indirecta, acoso, acción positiva), **derechos**, **órganos** y **medidas** de los poderes públicos.

### Cómo está escrito

- Cada artículo: primero el **texto literal del BOE** (con la etiqueta BOE) y debajo su **ficha** (de derecho: Titulares · Contenido · Límites · Protección · ⚠ Ojo; o de institución: Qué · Quién · Cómo · Plazos y mayorías · ⚠ Ojo).
- El Pacto de Estado de 2025 se cita de la publicación oficial de la Delegación del Gobierno contra la Violencia de Género (etiqueta **Gobierno de España**): **no es texto legal**.
- Los esquemas y cuadros **no son texto legal**: resumen los artículos citados.
- Remisiones a otros temas: la presencia equilibrada en los órganos directivos de la AGE (Ley 40/2015, art. 55 bis) está en el tema I.8; el acceso al empleo público de las personas con discapacidad, en el tema V.10.
- Al final: **Cierre 1** (las preguntas oficiales de 2025) y **Cierre 2** (repaso por bloques).
""")

# =============================================================================
T.ap("bI", "I. ¿Qué exige la igualdad entre mujeres y hombres? (CE, arts. 9.2 y 14; LO 3/2007)", donde(
  "Primera pregunta del tema. Las políticas de igualdad parten de dos artículos de la Constitución y se desarrollan, para mujeres y hombres, en la **Ley Orgánica 3/2007**, de 22 de marzo, para la igualdad efectiva de mujeres y hombres.",
  ["1 Fundamento constitucional (arts. 9.2 y 14)", "2 Objeto, principio y conceptos de la LO 3/2007", "3 Políticas públicas de igualdad", "4 Planes de igualdad de las empresas", "5 Igualdad en el empleo público", "6 Órganos y composición equilibrada"]))

T.ap("s1", "I.1 Fundamento constitucional (arts. 9.2 y 14)", f"""
{unidad("1.1 La igualdad real y efectiva (art. 9.2)",
  lit("CE", "Artículo 9", ["sean reales y efectivas", "remover los obstáculos"], solo=[2]),
  fichab("Mandato a los poderes públicos de hacer real la igualdad (igualdad material)",
         c("CE", "Artículo 9", "los poderes públicos"),
         ["Promover las condiciones para que la libertad y la igualdad sean reales y efectivas", "Remover los obstáculos que impidan o dificulten su plenitud", "Facilitar la participación de todos los ciudadanos en la vida política, económica, cultural y social"],
         "—",
         "Es la base de las **acciones positivas** (→ I.2.6). Lo citan como fundamento la LO 3/2007 (art. 1), la Ley 15/2022 (art. 1) y la LGD (art. 1)."))}

{unidad("1.2 Igualdad ante la ley y prohibición de discriminación (art. 14)",
  lit("CE", "Artículo 14", ["sin que pueda prevalecer discriminación alguna", "sexo"]),
  ficha(c("CE", "Artículo 14", "Los españoles"),
        "Igualdad ante la ley y prohibición de discriminación por nacimiento, raza, sexo, religión, opinión o cualquier otra condición o circunstancia personal o social",
        "—",
        "Derecho de la Sección 1.ª ampliada: tutela preferente y sumaria y recurso de amparo (art. 53.2 CE)",
        "La lista es **abierta**: «cualquier otra condición o circunstancia personal o social». La Ley 15/2022 la concreta (→ III.1.2)."))}
""", 2)

T.ap("s2", "I.2 Objeto, principio y conceptos de la LO 3/2007", f"""
{unidad("2.1 Objeto de la Ley (art. 1)",
  lit("LO3_2007", "Artículo 1", ["iguales en dignidad humana", "derecho de igualdad de trato y de oportunidades entre mujeres y hombres", "en el desarrollo de los artículos 9.2 y 14 de la Constitución"]),
  fichab("Ley para hacer efectivo el derecho de igualdad de trato y de oportunidades entre mujeres y hombres",
         "Obliga a los Poderes Públicos y a las personas físicas y jurídicas, públicas y privadas (1.2); se aplica a toda persona que se encuentre o actúe en territorio español (art. 2.2)",
         f"Eliminando la discriminación de la mujer {c('LO3_2007', 'Artículo 1', 'en cualesquiera de los ámbitos de la vida')}",
         "—",
         "Desarrolla los arts. **9.2 y 14** CE (no el 10). La finalidad: «una sociedad más democrática, más justa y más solidaria»."))}

{unidad("2.2 El principio de igualdad de trato (art. 3)",
  lit("LO3_2007", "Artículo 3", ["ausencia de toda discriminación, directa o indirecta, por razón de sexo", "la maternidad, la asunción de obligaciones familiares y el estado civil"]),
  ficha("Mujeres y hombres", "Ausencia de toda discriminación, directa o indirecta, por razón de sexo",
        "—", "Nulidad de los actos discriminatorios y reparación (art. 10); tutela judicial (art. 12)",
        "Menciona **especialmente** tres causas: **maternidad**, **obligaciones familiares** y **estado civil**."))}

{unidad("2.3 Discriminación directa e indirecta (art. 6)",
  lit("LO3_2007", "Artículo 6", ["en atención a su sexo, de manera menos favorable que otra en situación comparable", "aparentemente neutros", "toda orden de discriminar"]),
  fichab("Definición legal de las dos formas de discriminación por razón de sexo",
         "—",
         ["Directa: trato menos favorable **en atención a su sexo** que otra persona en situación comparable", "Indirecta: disposición, criterio o práctica **aparentemente neutros** que ponen a personas de un sexo en desventaja particular", "Toda **orden de discriminar** es discriminatoria"],
         "—",
         f"La indirecta **no** lo es si se justifica {c('LO3_2007', 'Artículo 6', 'objetivamente en atención a una finalidad legítima')} con medios necesarios y adecuados."))}

{unidad("2.4 Acoso sexual y acoso por razón de sexo (art. 7)",
  lit("LO3_2007", "Artículo 7", ["de naturaleza sexual", "en función del sexo de una persona", "Se considerarán en todo caso discriminatorios"]),
  fichab("Dos conductas de acoso que la ley considera discriminatorias",
         "—",
         ["Acoso **sexual**: comportamiento, verbal o físico, **de naturaleza sexual** que atente contra la dignidad", "Acoso **por razón de sexo**: comportamiento realizado **en función del sexo** de una persona", "Condicionar un derecho a aceptar el acoso también es discriminación (7.4)"],
         "—",
         "La diferencia está en el **contenido** (naturaleza sexual) frente al **motivo** (el sexo de la persona). Los dos son **en todo caso** discriminatorios."))}

{unidad("2.5 Discriminación por embarazo o maternidad (art. 8)",
  lit("LO3_2007", "Artículo 8", ["discriminación directa"]),
  fichab("Calificación legal del trato desfavorable por embarazo o maternidad", "—", c("LO3_2007", "Artículo 8", "todo trato desfavorable a las mujeres relacionado con el embarazo o la maternidad"), "—",
         "Es discriminación **directa** (no indirecta)."))}

{unidad("2.6 Acciones positivas (art. 11)",
  lit("LO3_2007", "Artículo 11", ["medidas específicas en favor de las mujeres", "en tanto subsistan dichas situaciones", "razonables y proporcionadas"]),
  fichab("Medidas específicas en favor de las mujeres para corregir desigualdades de hecho",
         "Los Poderes Públicos (obligación: «adoptarán»); las personas físicas y jurídicas privadas (facultad: «podrán»)",
         f"Para {c('LO3_2007', 'Artículo 11', 'corregir situaciones patentes de desigualdad de hecho respecto de los hombres')}",
         "Temporales: mientras subsistan las situaciones de desigualdad",
         "Tres notas: **temporales**, **razonables** y **proporcionadas**. Los poderes públicos **adoptarán**; los privados **podrán**."))}

{unidad("2.7 Tutela judicial efectiva (art. 12)",
  lit("LO3_2007", "Artículo 12", ["incluso tras la terminación de la relación", "La persona acosada será la única legitimada"]),
  ficha("Cualquier persona", "Recabar de los tribunales la tutela del derecho a la igualdad entre mujeres y hombres (art. 53.2 CE)",
        "En los litigios sobre acoso sexual y por razón de sexo, solo está legitimada la persona acosada",
        "Tutela judicial incluso tras terminar la relación; inversión de la carga de la prueba salvo en los procesos penales (art. 13)",
        "Acoso: la persona acosada es la **única** legitimada."))}
""", 2)

T.ap("s3", "I.3 Políticas públicas de igualdad (arts. 14, 15, 17 y 19)", f"""
{unidad("3.1 Criterios generales de actuación de los Poderes Públicos (art. 14)",
  lit("LO3_2007", "Artículo 14", ["participación equilibrada de mujeres y hombres", "violencia de género", "lenguaje no sexista"], solo=[1, 2, 5, 6, 9, 12]),
  fichab("Doce criterios que guían a todos los Poderes Públicos",
         "Los Poderes Públicos",
         ["Compromiso con la efectividad del derecho de igualdad", "Participación equilibrada en candidaturas y toma de decisiones", "Erradicación de la violencia de género y del acoso", "Conciliación y corresponsabilidad", "Lenguaje no sexista en el ámbito administrativo"],
         "—",
         "El lenguaje no sexista se **implanta** en el ámbito **administrativo** y se **fomenta** en las demás relaciones sociales, culturales y artísticas."))}

{unidad("3.2 Transversalidad (art. 15)",
  lit("LO3_2007", "Artículo 15", ["con carácter transversal", "en la definición y presupuestación de políticas públicas"]),
  fichab("Principio de igualdad integrado en toda la actuación pública (mainstreaming)",
         "Todos los Poderes Públicos; las Administraciones públicas lo integran **de forma activa**",
         "En la adopción y ejecución de normas, en la definición y presupuestación de políticas y en todas sus actividades", "—",
         "**Transversal** = en todas las políticas, no solo en las específicas de igualdad."))}

{unidad("3.3 Plan Estratégico de Igualdad de Oportunidades (art. 17)",
  lit("LO3_2007", "Artículo 17", ["aprobará periódicamente un Plan Estratégico de Igualdad de Oportunidades"]),
  fichab("Plan del Gobierno con medidas para la igualdad y contra la discriminación por razón de sexo",
         c("LO3_2007", "Artículo 17", "El Gobierno"), "En las materias de competencia del Estado", "Periódicamente (la ley no fija la duración)",
         "Lo aprueba el **Gobierno**, **periódicamente**. No confundir con el Plan de Igualdad de la AGE, que se aprueba **al inicio de cada legislatura** (→ I.5.5)."))}

{unidad("3.4 Informes de impacto de género (art. 19)",
  lit("LO3_2007", "Artículo 19", ["informe sobre su impacto por razón de género"]),
  fichab("Informe que acompaña a normas y planes del Consejo de Ministros",
         "Quien eleve el proyecto al Consejo de Ministros",
         "Se incorpora a los proyectos de disposiciones de carácter general y a los planes de especial relevancia económica, social, cultural y artística", "—",
         "También deben llevarlo las **convocatorias de pruebas selectivas** del empleo público, salvo urgencia (art. 55 → I.5.4)."))}
""", 2)

T.ap("s4", "I.4 Planes de igualdad de las empresas (arts. 45 y 46)", f"""
{unidad("4.1 Cuándo es obligatorio el plan de igualdad (art. 45)",
  lit("LO3_2007", "Artículo 45", ["cincuenta o más trabajadores", "cuando así se establezca en el convenio colectivo", "sustitución de las sanciones accesorias", "será voluntaria"]),
  fichab("Obligación de las empresas de adoptar medidas de igualdad y, en ciertos casos, un plan de igualdad",
         "Las empresas, negociando con la representación legal de las personas trabajadoras",
         ["Empresas de **50 o más** trabajadores (45.2)", "Cuando lo establezca el **convenio colectivo** (45.3)", "Cuando la autoridad laboral **sustituya sanciones accesorias** por el plan (45.4)", "Voluntario en las demás (45.5)"],
         "Umbral: cincuenta o más trabajadores",
         "**Cincuenta o más** (≥ 50). En la Ley 4/2023 el umbral de las medidas LGTBI es **más de cincuenta** (> 50, → III.3.4)."))}

{unidad("4.2 Concepto, contenido y registro (art. 46)",
  lit("LO3_2007", "Artículo 46", ["conjunto ordenado de medidas, adoptadas después de realizar un diagnóstico de situación", "Registro de Planes de Igualdad de las Empresas", "obligadas a inscribir"], solo=[1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16]),
  fichab("Plan de igualdad: medidas ordenadas tras un diagnóstico",
         "Comisión Negociadora del Plan de Igualdad (diagnóstico); la empresa lo inscribe",
         ["Diagnóstico previo negociado con al menos nueve materias (selección, clasificación, formación, promoción, condiciones de trabajo con auditoría salarial, corresponsabilidad, infrarrepresentación, retribuciones, acoso)", "Abarca la totalidad de la empresa", "Inscripción obligatoria en el Registro de Planes de Igualdad"],
         "—",
         "Primero el **diagnóstico**, después las medidas. La inscripción en el Registro es **obligatoria**."))}
""", 2)

T.ap("s5", "I.5 Igualdad en el empleo público (arts. 51, 52, 53, 55 y 64)", f"""
{unidad("5.1 Criterios de actuación de las Administraciones públicas (art. 51)",
  lit("LO3_2007", "Artículo 51", ["presencia equilibrada de mujeres y hombres en los órganos de selección y valoración", "acoso sexual y al acoso por razón de sexo"]),
  fichab("Deberes de todas las Administraciones en su empleo público",
         "Las Administraciones públicas, en sus respectivas competencias",
         ["Remover obstáculos en el acceso y la carrera", "Facilitar la conciliación sin menoscabo de la promoción", "Formación en igualdad", "Presencia equilibrada en órganos de selección y valoración", "Protección frente al acoso", "Eliminar la discriminación retributiva", "Evaluar periódicamente"],
         "—", "Son siete deberes (letras a a g)."))}

{unidad("5.2 Titulares de órganos directivos (art. 52)",
  lit("LO3_2007", "Artículo 52", ["considerados en su conjunto"]),
  fichab("Presencia equilibrada en los nombramientos de órganos directivos de la AGE",
         c("LO3_2007", "Artículo 52", "El Gobierno"),
         "Atiende al principio de presencia equilibrada en los nombramientos que le corresponden", "—",
         "Se mide en los órganos directivos **considerados en su conjunto**. La regla del art. 55 bis de la Ley 40/2015 (por departamento ministerial) se estudia en el tema I.8."))}

{unidad("5.3 Órganos de selección y comisiones de valoración (art. 53)",
  lit("LO3_2007", "Artículo 53", ["salvo por razones fundadas y objetivas, debidamente motivadas", "composición equilibrada de ambos sexos"]),
  fichab("Presencia equilibrada en tribunales y comisiones de valoración de la AGE",
         "Tribunales y órganos de selección de la AGE y sus organismos; su representación en las comisiones de valoración",
         "Responden al principio de presencia equilibrada", "—",
         "Admite excepción **motivada** («razones fundadas y objetivas, debidamente motivadas»)."))}

{unidad("5.4 Informe de impacto de género en las pruebas de acceso (art. 55)",
  lit("LO3_2007", "Artículo 55", ["informe de impacto de género, salvo en casos de urgencia"]),
  fichab("Informe que acompaña a las convocatorias de pruebas selectivas",
         "El órgano que aprueba la convocatoria", "Se acompaña a la aprobación de la convocatoria", "—",
         "Excepción: **urgencia**; la prohibición de discriminación se mantiene siempre."))}

{unidad("5.5 Plan de Igualdad en la AGE (art. 64)",
  lit("LO3_2007", "Artículo 64", ["al inicio de cada legislatura", "evaluado anualmente por el Consejo de Ministros"]),
  fichab("Plan para la igualdad entre mujeres y hombres en la AGE y sus organismos públicos",
         "Lo aprueba el **Gobierno**; se negocia con la representación de los empleados públicos; lo evalúa el **Consejo de Ministros**",
         "Fija objetivos y estrategias en materia de igualdad en el empleo público",
         "Aprobación **al inicio de cada legislatura**; evaluación **anual**",
         "Inicio de **cada legislatura** + evaluación **anual** por el **Consejo de Ministros**."))}
""", 2)

T.ap("s6", "I.6 Órganos y composición equilibrada (arts. 76 a 78 y disposición adicional primera)", f"""
{unidad("6.1 Comisión Interministerial de Igualdad entre mujeres y hombres (art. 76)",
  lit("LO3_2007", "Artículo 76", ["órgano colegiado responsable de la coordinación"]),
  fichab("Órgano colegiado de coordinación de las políticas de igualdad de los ministerios",
         "Representantes de los departamentos ministeriales (composición reglamentaria)",
         "Coordina las políticas y medidas de los departamentos ministeriales", "—",
         "Es de **coordinación** (no consultivo). Está adscrita al Ministerio de Igualdad, cuyo titular la preside (RD 246/2024, art. 1.6)."))}

{unidad("6.2 Unidades de Igualdad (art. 77)",
  lit("LO3_2007", "Artículo 77", ["En todos los Ministerios se encomendará a uno de sus órganos directivos"]),
  fichab("Funciones de igualdad en cada Ministerio",
         "Uno de los órganos directivos de cada Ministerio",
         ["Recabar información estadística", "Elaborar estudios", "Asesorar en el informe de impacto de género", "Fomentar el conocimiento del principio de igualdad", "Velar por el cumplimiento de la ley"],
         "—", "No es un órgano nuevo: se **encomienda** a un **órgano directivo** que ya existe en **todos** los Ministerios."))}

{unidad("6.3 Consejo de Participación de la Mujer (art. 78)",
  lit("LO3_2007", "Artículo 78", ["órgano colegiado de consulta y asesoramiento"]),
  fichab("Cauce de participación de las mujeres en la igualdad",
         "Administraciones públicas y asociaciones y organizaciones de mujeres de ámbito estatal",
         "Consulta y asesoramiento", "—", "Es **consultivo** (consulta y asesoramiento), a diferencia de la Comisión Interministerial (coordinación)."))}

{unidad("6.4 Composición equilibrada: el 60/40 (disposición adicional primera)",
  lit("LO3_2007", D, ["no superen el sesenta por ciento ni sean menos del cuarenta por ciento"]),
  fichab("Definición legal de composición equilibrada", "—",
         "En el conjunto de que se trate, las personas de cada sexo no superan el 60 % ni son menos del 40 %", "**60 % máximo / 40 % mínimo** de cada sexo",
         "Ni más del **sesenta** ni menos del **cuarenta** por ciento, **de cada sexo**."))}

{NOLEGAL}

| Órgano o instrumento | Artículo | Naturaleza | Dato que se pregunta |
|---|---|---|---|
| Plan Estratégico de Igualdad de Oportunidades | 17 | Plan del Gobierno | Periódicamente |
| Plan de Igualdad de la AGE | 64 | Plan del Gobierno | Al inicio de cada legislatura; evaluación anual por el Consejo de Ministros |
| Comisión Interministerial de Igualdad | 76 | Órgano colegiado | Coordinación |
| Unidades de Igualdad | 77 | Funciones encomendadas a un órgano directivo | En todos los Ministerios |
| Consejo de Participación de la Mujer | 78 | Órgano colegiado | Consulta y asesoramiento |

{resumen([
  "La igualdad se apoya en los arts. **9.2** (real y efectiva) y **14** CE; la LO 3/2007 los desarrolla.",
  "Conceptos: discriminación **directa** e **indirecta** (6), **acoso sexual** y **por razón de sexo** (7), embarazo o maternidad = discriminación **directa** (8), **acciones positivas** temporales, razonables y proporcionadas (11).",
  "Empresas de **50 o más** trabajadores: plan de igualdad obligatorio, con diagnóstico e inscripción en el Registro (45 y 46).",
  "AGE: presencia equilibrada en órganos directivos y tribunales; plan de igualdad **al inicio de cada legislatura** (64).",
  "Composición equilibrada: **60/40** (disposición adicional primera)."],
  "Siguiente: II. ¿Cómo se combate la violencia de género?")}
""", 2)

# =============================================================================
T.ap("bII", "II. ¿Cómo se combate la violencia de género? (LO 1/2004 y normas conexas)", donde(
  "Segunda pregunta. La violencia de género es la manifestación más grave de la desigualdad. La **Ley Orgánica 1/2004**, de 28 de diciembre, de Medidas de Protección Integral contra la Violencia de Género, define qué es, reconoce derechos a las víctimas y crea órganos especializados.",
  ["1 Objeto, principios y planes de sensibilización (arts. 1 a 3)", "2 Derechos de las mujeres víctimas (arts. 17 a 27)", "3 Tutela institucional: Delegación del Gobierno y Observatorio (arts. 29 y 30; RD 246/2024)", "4 Pacto de Estado y plan conjunto plurianual"]))

T.ap("s7", "II.1 Objeto, principios y sensibilización (arts. 1 a 3)", f"""
{unidad("1.1 Qué es violencia de género para la ley (art. 1)",
  lit("LO1_2004", "Artículo 1", ["quienes sean o hayan sido sus cónyuges", "aun sin convivencia", "violencia física y psicológica", "familiares o allegados menores de edad"]),
  fichab("Objeto de la ley y concepto de violencia de género",
         "Víctimas: las mujeres, sus hijos menores y los menores sujetos a su tutela o guarda y custodia; agresores: quienes sean o hayan sido cónyuges o pareja",
         ["Violencia como manifestación de la discriminación y de las relaciones de poder de los hombres sobre las mujeres", "Comprende todo acto de violencia física y psicológica, incluidas agresiones a la libertad sexual, amenazas, coacciones o privación arbitraria de libertad", "También la ejercida sobre familiares o allegados menores para dañar a la mujer (1.4)"],
         "—",
         "Basta una relación de afectividad **presente o pasada**, **aun sin convivencia**. Finalidad: **prevenir, sancionar y erradicar** y **prestar asistencia**."))}

{unidad("1.2 Principios rectores (art. 2)",
  lit("LO1_2004", "Artículo 2", ["Delegación Especial del Gobierno contra la Violencia sobre la Mujer", "Observatorio Estatal de la Violencia sobre la Mujer", "principio de transversalidad"], solo=[1, 2, 3, 5, 7, 12]),
  fichab("Fines del conjunto integral de medidas", "Los poderes públicos",
         ["Sensibilización y prevención", "Derechos de las víctimas exigibles ante las Administraciones", "Derechos laborales, funcionariales y económicos", "Tutela institucional (Delegación y Observatorio)", "Marco penal y procesal", "Transversalidad"],
         "—",
         "El art. 2 f) conserva el nombre antiguo («Delegación **Especial** del Gobierno contra la Violencia **sobre la Mujer**»); el órgano se llama hoy **Delegación del Gobierno contra la Violencia de Género** (art. 29 → II.3.1)."))}

{unidad("1.3 Plan Estatal de Sensibilización y Prevención (art. 3)",
  lit("LO1_2004", "Artículo 3", ["Plan Estatal de Sensibilización y Prevención de la Violencia de Género con carácter permanente", "en un plazo máximo de un mes", "Informe anual de evaluación"], solo=[1, 5, 6]),
  fichab("Plan permanente de sensibilización y prevención",
         "Responsabilidad del Gobierno; lo controla una Comisión de amplia participación; la Delegación del Gobierno elabora el informe anual",
         "Con escalas de valores basadas en la igualdad, dirigido a hombres y mujeres, con formación de profesionales",
         "Comisión creada en el plazo máximo de **un mes**; informe de evaluación **anual** remitido a las **Cortes Generales**",
         "Plan **permanente**; el informe anual lo hace la **Delegación del Gobierno** y va a las **Cortes**."))}
""", 2)

T.ap("s8", "II.2 Derechos de las mujeres víctimas (arts. 17 a 27)", f"""
{unidad("2.1 Garantía de los derechos y derecho a la información (arts. 17 y 18)",
  lit("LO1_2004", "Artículo 17", ["sin que pueda existir discriminación en el acceso a los mismos", "carácter de servicios esenciales"], solo=[1, 3]),
  lit("LO1_2004", "Artículo 18", ["plena información y asesoramiento adecuado a su situación personal"], solo=[1]),
  ficha("Todas las mujeres víctimas de violencia de género", "Información y asesoramiento; los servicios de información, atención psicosocial, asesoramiento jurídico 24 horas y acogida son **servicios esenciales**",
        "—", "Garantía de acceso sin discriminación; formato accesible para mujeres con discapacidad (18.2)",
        "Los servicios de atención a las víctimas tienen carácter de **servicios esenciales**."))}

{unidad("2.2 Derecho a la asistencia social integral (art. 19)",
  lit("LO1_2004", "Artículo 19", ["atención permanente, actuación urgente, especialización de prestaciones y multidisciplinariedad profesional"], solo=[1]),
  ficha("Las víctimas y los menores bajo su patria potestad o guarda y custodia (19.5)",
        "Servicios sociales de atención, de emergencia, de apoyo y acogida y de recuperación integral",
        "—", "Los organizan las comunidades autónomas y las Corporaciones Locales",
        "Cuatro principios: **atención permanente, actuación urgente, especialización** y **multidisciplinariedad**."))}

{unidad("2.3 Asistencia jurídica (art. 20)",
  lit("LO1_2004", "Artículo 20", ["asesoramiento jurídico gratuito en el momento inmediatamente previo a la interposición de la denuncia", "una misma dirección letrada"], solo=[1]),
  ficha("Las víctimas y, si fallecen, sus causahabientes no partícipes en los hechos",
        "Asesoramiento gratuito antes de denunciar y defensa y representación gratuitas por abogado y procurador",
        "—", "Ley 1/1996 de Asistencia Jurídica Gratuita; designación urgente de letrado (20.4)",
        "El asesoramiento es **previo** a la denuncia; una **misma dirección letrada** asume la defensa."))}

{unidad("2.4 Derechos laborales y de Seguridad Social (art. 21)",
  lit("LO1_2004", "Artículo 21", ["reducción o a la reordenación de su tiempo de trabajo", "situación legal de desempleo", "bonificación del 100 por 100", "se considerarán justificadas y serán remuneradas"], solo=[1, 2, 3, 4]),
  ficha("La trabajadora víctima de violencia de género (y la trabajadora por cuenta propia, 21.5)",
        ["Reducción o reordenación del tiempo de trabajo", "Movilidad geográfica y cambio de centro", "Suspensión con reserva de puesto y extinción del contrato", "Ausencias justificadas y remuneradas"],
        "En los términos del Estatuto de los Trabajadores",
        "Suspensión y extinción = situación legal de **desempleo**; bonificación del **100 %** de las cuotas por contingencias comunes a la empresa que contrate a una sustituta",
        "Las ausencias son **justificadas y remuneradas** cuando lo determinen los servicios sociales o de salud."))}

{unidad("2.5 Acreditación de la violencia de género (art. 23)",
  lit("LO1_2004", "Artículo 23", ["una orden de protección", "informe del Ministerio Fiscal", "informe de los servicios sociales"], solo=[1]),
  fichab("Títulos que acreditan la situación de violencia de género para acceder a los derechos",
         "Juez (sentencia, orden de protección, medida cautelar), Ministerio Fiscal, servicios sociales, especializados o de acogida",
         ["Sentencia condenatoria", "Orden de protección u otra resolución judicial con medida cautelar", "Informe del Ministerio Fiscal", "Informe de los servicios sociales, especializados o de acogida"],
         "—",
         "No hace falta sentencia: basta un **informe de los servicios sociales** o del **Fiscal**."))}

{unidad("2.6 Derechos de las funcionarias públicas (arts. 24 a 26)",
  lit("LO1_2004", "Artículo 24", ["reducción o a la reordenación de su tiempo de trabajo", "movilidad geográfica de centro de trabajo", "excedencia"]),
  lit("LO1_2004", "Artículo 25", ["se considerarán justificadas"]),
  lit("LO1_2004", "Artículo 26", ["en los términos establecidos en el artículo 23"]),
  ficha("La funcionaria víctima de violencia de género",
        ["Reducción o reordenación del tiempo de trabajo", "Movilidad geográfica de centro de trabajo", "Excedencia", "Faltas de asistencia justificadas"],
        "En los términos de su legislación específica (TREBEP)",
        "Acreditación como en el art. 23 (→ II.2.5)",
        "Para la funcionaria, la ley habla de **excedencia**; para la trabajadora, de **suspensión** y **extinción** (art. 21)."))}

{unidad("2.7 Ayuda social de pago único (art. 27)",
  lit("LO1_2004", "Artículo 27", ["75 por 100 del salario mínimo interprofesional", "seis meses de subsidio por desempleo", "doce meses", "18 meses", "24 meses"], solo=[1, 2, 5]),
  ficha("Víctimas con rentas no superiores al 75 % del SMI y especiales dificultades para obtener empleo",
        "Ayuda de pago único financiada por los Presupuestos Generales del Estado",
        "Que por su edad, preparación o circunstancias sociales no participe en los programas de empleo",
        "La conceden las Administraciones competentes en servicios sociales, con informe del Servicio Público de Empleo",
        "Importe: **6** meses de subsidio; **12** con discapacidad ≥ 33 %; hasta **18** con responsabilidades familiares; **24** si además hay discapacidad ≥ 33 %."))}
""", 2)

T.ap("s9", "II.3 Tutela institucional: Delegación del Gobierno y Observatorio (arts. 29 y 30; RD 246/2024, art. 2)", f"""
{unidad("3.1 La Delegación del Gobierno contra la Violencia de Género (art. 29; RD 246/2024, art. 2.3)",
  lit("LO1_2004", "Artículo 29", ["formulará las políticas públicas", "Macroencuesta de Violencia contra las Mujeres", "estará legitimada ante los órganos jurisdiccionales", "Reglamentariamente se determinará el rango"]),
  lit("RD246", "Artículo 2", ["con rango de dirección general", "La Delegación del Gobierno contra la Violencia de Género"], solo=[22, 23, 24, 25]),
  fichab("Órgano de la AGE que formula y coordina las políticas contra la violencia de género",
         "Adscrita al Ministerio de Igualdad; depende de la Secretaría de Estado de Igualdad y para la Erradicación de la Violencia contra las Mujeres",
         ["Formula las políticas públicas y elabora la **Macroencuesta**", "Coordina e impulsa las acciones en la materia", "Su titular está legitimado ante los órganos jurisdiccionales"],
         "Rango: **dirección general** (lo fija el reglamento: RD 246/2024, art. 2.3)",
         "La ley remite el rango al reglamento; el RD 246/2024 le da **rango de dirección general** (no de Secretaría General ni de Subdirección). Cayó en 2025 (→ Cierre 1)."))}

{unidad("3.2 Observatorio Estatal de Violencia sobre la Mujer (art. 30)",
  lit("LO1_2004", "Artículo 30", ["órgano colegiado", "con periodicidad anual"], solo=[1, 2]),
  fichab("Órgano colegiado de asesoramiento, evaluación, informes y propuestas",
         "Composición reglamentaria, con participación de CC. AA., entidades locales, agentes sociales y organizaciones de mujeres (30.3)",
         "Asesoramiento, evaluación, colaboración institucional, informes, estudios y propuestas, con datos desagregados por sexo",
         "Informe **anual** al Gobierno y a las Comunidades Autónomas",
         "La **Delegación** es un órgano directivo; el **Observatorio**, un órgano **colegiado**. El informe anual del Observatorio va al **Gobierno y a las CC. AA.**; el del Plan de sensibilización, a las **Cortes** (→ II.1.3)."))}
""", 2)

T.ap("s10", "II.4 Pacto de Estado y plan conjunto plurianual", f"""
{unidad("4.1 Renovación del Pacto de Estado contra la Violencia de Género (2025)",
  doc("PACTO2025", "Medidas del Pacto de Estado contra la violencia de género 2025, Introducción (Delegación del Gobierno contra la Violencia de Género, igualdad.gob.es) · fuente oficial, no es texto legal", [
    "El 26 de febrero de 2025 el pleno del Congreso de los Diputados aprobó de manera casi unánime la renovación y actualización del Pacto de Estado contra la Violencia de Género.",
    "El acuerdo amplía las medidas que incluía en 2017 de 290 a 461, e introduce nuevos ejes como son la violencia vicaria, la violencia económica y la digital.",
    "Las medidas se reparten en diez capítulos"], resaltar=["26 de febrero de 2025", "de 290 a 461", "diez capítulos"]),
  fichab("Acuerdo parlamentario (no es una norma) que fija medidas contra la violencia de género",
         "Aprobado por el Pleno del Congreso de los Diputados; su seguimiento lo impulsa la Secretaría de Estado de Igualdad (RD 246/2024, art. 2.2 c)",
         "Medidas repartidas en diez capítulos; nuevos ejes: violencia vicaria, económica y digital",
         "**290** medidas en 2017 → **461** en la renovación de **2025**",
         "Cayó en 2025 (→ Cierre 1): de **290 a 461**."))}

{unidad("4.2 Plan conjunto plurianual en materia de violencia contra las mujeres (2023-2027)",
  lit("PCP2023", "preambulo", ["3 de marzo de 2023", "(2023-2027)", "Plan Conjunto plurianual que incluye un Catálogo de referencia de políticas y servicios"], solo=[0, 9], titulo="Resolución de 16 de marzo de 2023, de la Secretaría de Estado de Igualdad y contra la Violencia de Género (BOE-A-2023-7326) · fragmentos"),
  fichab("Plan conjunto de la AGE y las comunidades autónomas (art. 151.2 a de la Ley 40/2015)",
         "La **Conferencia Sectorial de Igualdad** (acuerdo de 3 de marzo de 2023)",
         "Se articula con un Catálogo de referencia de políticas y servicios y un Sistema común de información y evaluación",
         "Periodo **2023-2027**",
         "Lo aprueba la **Conferencia Sectorial de Igualdad**, no el Consejo de Ministros. Periodo: **2023 a 2027** (cayó en 2025 → Cierre 1)."))}

{resumen([
  "Violencia de género (LO 1/2004): la ejercida sobre las mujeres por quien sea o haya sido su cónyuge o pareja, **aun sin convivencia**; incluye la ejercida sobre menores para dañarlas (art. 1).",
  "Derechos: información, asistencia social integral, asistencia jurídica gratuita, derechos laborales y de funcionarias, ayuda de pago único (arts. 17 a 27); se acreditan con sentencia, orden de protección, informe del Fiscal o de los servicios sociales (art. 23).",
  "Delegación del Gobierno contra la Violencia de Género: **rango de dirección general** (RD 246/2024); Observatorio Estatal: órgano **colegiado** con informe **anual**.",
  "Pacto de Estado renovado el **26-2-2025**: de **290 a 461** medidas; plan conjunto plurianual **2023-2027** (Conferencia Sectorial de Igualdad)."],
  "Siguiente: III. ¿Cómo se garantiza la igualdad de trato y la de las personas LGTBI?")}
""", 2)

# =============================================================================
T.ap("bIII", "III. ¿Cómo se garantiza la igualdad de trato y la de las personas LGTBI? (Ley 15/2022; Ley 4/2023)", donde(
  "Tercera pregunta. La **Ley 15/2022**, de 12 de julio, integral para la igualdad de trato y la no discriminación, es la ley general frente a **cualquier** causa de discriminación. La **Ley 4/2023**, de 28 de febrero, la concreta para las personas **LGTBI** y regula la rectificación registral del sexo.",
  ["1 Ley 15/2022: objeto, ámbito, derecho y definiciones", "2 Autoridad Independiente para la Igualdad de Trato y la No Discriminación", "3 Ley 4/2023: objeto, definiciones, Consejo de Participación y empresas", "4 Medidas LGTBI en las empresas (RD 1026/2024)", "5 Rectificación registral de la mención relativa al sexo"]))

T.ap("s11", "III.1 Ley 15/2022: objeto, ámbito, derecho y definiciones (arts. 1, 2, 4 y 6)", f"""
{unidad("1.1 Objeto (art. 1)",
  lit("L15_2022", "Artículo 1", ["en desarrollo de los artículos 9.2, 10 y 14 de la Constitución"]),
  fichab("Ley general de igualdad de trato y no discriminación", "Personas físicas o jurídicas, públicas o privadas; poderes públicos",
         "Garantiza y promueve el derecho; prevé medidas para prevenir, eliminar y corregir toda discriminación, directa o indirecta", "—",
         "Desarrolla los arts. **9.2, 10 y 14** CE (la LO 3/2007 cita solo el 9.2 y el 14)."))}

{unidad("1.2 Ámbito subjetivo: causas de discriminación (art. 2)",
  lit("L15_2022", "Artículo 2", ["con independencia de su nacionalidad, de si son menores o mayores de edad o de si disfrutan o no de residencia legal", "estado serológico", "situación socioeconómica"], solo=[1, 4]),
  ficha("Toda persona, con independencia de nacionalidad, edad o residencia legal",
        "No ser discriminado por nacimiento, origen racial o étnico, sexo, religión, convicción u opinión, edad, discapacidad, orientación o identidad sexual, expresión de género, enfermedad o condición de salud, estado serológico y/o predisposición genética, lengua, situación socioeconómica o cualquier otra condición",
        "Caben diferencias de trato con criterios razonables y objetivos y propósito legítimo (2.2)",
        "Obliga al sector público y a los particulares (2.4)",
        "La lista incluye **lengua**, **situación socioeconómica** y **estado serológico**; también es **abierta**."))}

{unidad("1.3 El derecho a la igualdad de trato y no discriminación (art. 4)",
  lit("L15_2022", "Artículo 4", ["por asociación y por error", "la discriminación múltiple o interseccional", "adecuado, necesario y proporcionado", "principio informador del ordenamiento jurídico"], solo=[1, 2, 3, 4]),
  ficha("Toda persona", "Ausencia de toda discriminación por las causas del art. 2.1; enumera las vulneraciones",
        "No es discriminación la diferencia de trato justificada objetivamente por una finalidad legítima y con medio adecuado, necesario y proporcionado",
        "Principio informador del ordenamiento, de aplicación transversal",
        "Vulneraciones: discriminación directa o indirecta, **por asociación**, **por error**, **múltiple o interseccional**, denegación de ajustes razonables, acoso, inducción, represalias, inacción…"))}

{unidad("1.4 Definiciones (art. 6)",
  lit("L15_2022", "Artículo 6", ["debido a su relación con otra", "apreciación incorrecta", "de manera simultánea o consecutiva por dos o más causas", "concurren o interactúan diversas causas", "entorno intimidatorio, hostil, degradante, humillante u ofensivo", "en su dimensión colectiva o social"], solo=[1, 2, 4, 5, 6, 7, 8, 9, 10, 13, 14, 21, 22]),
  fichab("Conceptos legales de discriminación", "—",
         ["Por **asociación**: por la relación con otra persona en quien concurre la causa", "Por **error**: apreciación incorrecta de las características", "**Múltiple**: dos o más causas, simultánea o consecutivamente", "**Interseccional**: las causas concurren o interactúan y generan una forma específica", "**Acoso** y **acción positiva**: definiciones que repite literalmente la Ley 4/2023 (→ III.3.2)"],
         "—",
         "Múltiple = **suma** de causas; interseccional = **interacción** que crea una discriminación **específica**. La denegación de **ajustes razonables** es discriminación **directa**."))}
""", 2)

T.ap("s12", "III.2 Autoridad Independiente para la Igualdad de Trato y la No Discriminación (arts. 40 y 41)", f"""
{unidad("2.1 Creación y funciones (art. 40)",
  lit("L15_2022", "Artículo 40", ["como autoridad independiente", "con el consentimiento expreso de las partes", "sustituirá al recurso de alzada", "tendrán carácter vinculante para las partes", "que remitirá al Congreso de los Diputados, al Gobierno y al Defensor del Pueblo"], solo=[1, 3, 4, 5, 18]),
  fichab("Autoridad independiente que protege y promueve la igualdad de trato en los ámbitos de competencia del Estado",
         "La Autoridad Independiente (sector público y privado)",
         ["Asistencia y orientación a las víctimas", "Mediación o conciliación (con consentimiento expreso; no en asuntos penales o laborales)", "Investigaciones de oficio o a instancia de terceros", "Acciones judiciales", "Dictamen sobre proyectos normativos e informe preceptivo de la Estrategia Estatal"],
         "Informe anual al **Congreso**, al **Gobierno** y al **Defensor del Pueblo**",
         "Su mediación o conciliación **sustituye** al recurso de alzada (y, en su caso, al de reposición) y es **vinculante**."))}

{unidad("2.2 Naturaleza, presidencia y mandato (art. 41)",
  lit("L15_2022", "Artículo 41", ["entidad de derecho público, de las previstas en el artículo 109", "nombrada por el Gobierno mediante Real Decreto", "por mayoría absoluta", "en el plazo de un mes natural", "cinco años sin posibilidad de renovación"], solo=[1, 4, 5]),
  fichab("Entidad de derecho público independiente (Ley 40/2015, art. 109)",
         "Presidencia: nombrada por el **Gobierno** mediante **Real Decreto**, previa comparecencia ante las comisiones del Congreso y del Senado",
         "El Congreso, por la Comisión competente, puede aprobar o rechazar el nombramiento",
         "Mayoría **absoluta** de la Comisión del Congreso en **un mes natural**; mandato de **cinco años**, **no renovable**",
         "**Cinco años sin renovación**. Su presidencia tiene rango de **subsecretario** (RD 246/2024, art. 1.7)."))}
""", 2)

T.ap("s13", "III.3 Ley 4/2023: objeto, definiciones, Consejo de Participación y empresas (arts. 1, 3, 9 y 15)", f"""
{unidad("3.1 Objeto (art. 1)",
  lit("L4_2023", "Artículo 1", ["lesbianas, gais, trans, bisexuales e intersexuales", "rectificación registral relativa al sexo"]),
  fichab("Ley de igualdad real y efectiva de las personas LGTBI y de sus familias", "Toda persona física o jurídica, pública o privada, que resida, se encuentre o actúe en España (art. 2)",
         "Principios de actuación, derechos y deberes, medidas contra la discriminación y rectificación registral del sexo", "—",
         "LGTBI = **lesbianas, gais, trans, bisexuales e intersexuales**; protege también a sus **familias**."))}

{unidad("3.2 Definiciones (art. 3)",
  lit("L4_2023", "Artículo 3", ["Acoso discriminatorio", "Medidas de acción positiva", "Identidad sexual", "Expresión de género", "Persona trans", "LGTBIfobia"], solo=[2, 4, 8, 11, 16, 17, 18, 20]),
  fichab("Conceptos legales de la Ley 4/2023", "—",
         ["Discriminación directa e indirecta por orientación sexual e identidad sexual, expresión de género o características sexuales", "**Acoso discriminatorio** (letra d)", "**Acción positiva** (letra f)", "Identidad sexual, expresión de género y persona trans (i, j, k)", "LGTBIfobia (m)"],
         "—",
         "Cayó dos veces en 2025 (→ Cierre 1): los distractores eran **otras definiciones del mismo art. 3** (LGTBIfobia, discriminación directa y acción positiva)."))}

{unidad("3.3 Consejo de Participación de las Personas LGTBI (art. 9)",
  lit("L4_2023", "Artículo 9", ["órgano de participación ciudadana", "artículo 22.3 de la Ley 40/2015", "con carácter semestral"]),
  fichab("Órgano de participación ciudadana en derechos de las personas LGTBI",
         "Administraciones públicas y sociedad civil; depende del Ministerio de Igualdad (hoy, adscrito a través de la Secretaría de Estado de Igualdad y para la Erradicación de la Violencia contra las Mujeres: RD 246/2024, art. 2.5)",
         "Institucionaliza la colaboración y el diálogo entre Administraciones y sociedad civil",
         "Memoria **semestral**, que se remite a las Cortes Generales",
         "Órgano colegiado del art. **22.3** de la Ley 40/2015; memoria **semestral** (no anual)."))}

{unidad("3.4 Igualdad y no discriminación LGTBI en las empresas (art. 15)",
  lit("L4_2023", "Artículo 15", ["Las empresas de más de cincuenta personas trabajadoras", "en el plazo de doce meses", "protocolo de actuación para la atención del acoso o la violencia contra las personas LGTBI"], solo=[1]),
  fichab("Conjunto planificado de medidas y recursos para la igualdad de las personas LGTBI",
         "Empresas de **más de cincuenta** personas trabajadoras; medidas pactadas en la negociación colectiva",
         "Incluye un protocolo frente al acoso o la violencia contra las personas LGTBI; desarrollo reglamentario (→ III.4)",
         "Plazo: **doce meses** desde la entrada en vigor de la ley",
         "**Más de cincuenta** (no cuarenta, treinta ni cien). Cayó en 2025 (→ Cierre 1)."))}
""", 2)

T.ap("s14", "III.4 Medidas LGTBI en las empresas (RD 1026/2024)", f"""
{unidad("4.1 Objeto y ámbito (arts. 1 y 2)",
  lit("RD1026", "Artículo 1", ["artículo 15.1 de la Ley 4/2023"]),
  lit("RD1026", "Artículo 2", ["más de cincuenta personas trabajadoras", "será voluntaria"], solo=[1, 2]),
  fichab("Desarrollo reglamentario de las «medidas planificadas» del art. 15.1 de la Ley 4/2023",
         "Empresas con más de cincuenta personas trabajadoras",
         "Negociación de medidas planificadas; voluntaria en las de cincuenta o menos", "—",
         "Obligatorio con **más de 50**; voluntario con **50 o menos**."))}

{unidad("4.2 Contenido mínimo de las medidas planificadas (anexo I)",
  lit("RD1026", "ai", ["contexto favorable a la diversidad", "erradicar estereotipos", "heterogeneidad de las plantillas", "garantizando el acceso"], solo=[3, 4, 5, 6, 17, 18, 19, 20], titulo="Anexo I. Medidas planificadas (RD 1026/2024) · fragmentos"),
  fichab("Contenidos que deben desarrollar las medidas planificadas", "Convenios colectivos o acuerdos de empresa",
         ["Cláusulas de igualdad de trato y no discriminación", "Acceso al empleo sin estereotipos", "Clasificación y promoción", "Formación, sensibilización y lenguaje", "Entornos laborales diversos", "Permisos y beneficios sociales", "Régimen disciplinario"],
         "—",
         "Cayó en 2025 (→ Cierre 1): los distractores invertían el anexo («**potenciar** estereotipos», «**homogeneidad**», «**sin garantizar**»)."))}
""", 2)

T.ap("s15", "III.5 Rectificación registral de la mención relativa al sexo (arts. 43 y 44)", f"""
{unidad("5.1 Legitimación (art. 43)",
  lit("L4_2023", "Artículo 43", ["mayor de dieciséis años", "menores de dieciséis años y mayores de catorce", "menores de catorce años y mayores de doce"], solo=[1, 2, 5]),
  ficha("Personas de nacionalidad española",
        ["Mayores de 16 años: por sí mismas", "Entre 14 y 16: por sí mismas, asistidas por sus representantes legales", "Entre 12 y 14: autorización judicial (Ley 15/2015 de Jurisdicción Voluntaria)"],
        "—", "Defensor judicial si hay desacuerdo de progenitores o representantes (43.2)",
        "Tramos: **16**, **14** y **12** años."))}

{unidad("5.2 Procedimiento (art. 44)",
  lit("L4_2023", "Artículo 44", ["en ningún caso podrá estar condicionado a la previa exhibición de informe médico o psicológico", "En el plazo máximo de tres meses", "dentro del plazo máximo de un mes", "recurso de alzada ante la Dirección General de Seguridad Jurídica y Fe Pública"], solo=[3, 10, 11, 12]),
  fichab("Procedimiento registral de rectificación del sexo",
         "Persona encargada de la Oficina del Registro Civil donde se presente la solicitud (art. 45)",
         "Comparecencia inicial, nueva comparecencia de ratificación y resolución; sin informe médico o psicológico ni modificación corporal previa",
         "Ratificación en **tres meses** como máximo desde la comparecencia inicial; resolución en **un mes** desde la segunda comparecencia; recurso de **alzada** ante la DG de Seguridad Jurídica y Fe Pública",
         "**3 meses** para ratificar, **1 mes** para resolver. **No** se exige informe médico o psicológico."))}

{resumen([
  "Ley 15/2022: ley general frente a **cualquier** causa (lista abierta del art. 2.1); define discriminación por **asociación**, por **error**, **múltiple** e **interseccional**, acoso y acción positiva (art. 6).",
  "Autoridad Independiente: entidad del art. 109 Ley 40/2015; mediación que **sustituye a la alzada** y es **vinculante**; presidencia por **Real Decreto**, mandato de **cinco años no renovable**.",
  "Ley 4/2023: definiciones del art. 3 (acoso discriminatorio: letra d); Consejo de Participación LGTBI con memoria **semestral**; empresas de **más de cincuenta** trabajadores con medidas y protocolo (art. 15), desarrolladas por el RD 1026/2024.",
  "Rectificación registral: **16** años por sí, **14-16** asistidos, **12-14** con autorización judicial; ratificación en **tres meses** y resolución en **un mes**."],
  "Siguiente: IV. ¿Qué régimen jurídico tiene la discapacidad?")}
""", 2)

# =============================================================================
T.ap("bIV", "IV. ¿Qué régimen jurídico tiene la discapacidad? (CE, art. 49; RDLeg 1/2013)", donde(
  "Cuarta pregunta. La Constitución se ocupa de las personas con discapacidad en el **art. 49**. La norma general es el **Texto Refundido de la Ley General de derechos de las personas con discapacidad y de su inclusión social** (RDLeg 1/2013, de 29 de noviembre: **LGD**).",
  ["1 El art. 49 de la Constitución", "2 LGD: objeto, definiciones, principios y titulares", "3 Derecho al trabajo y cuota de reserva", "4 Órganos y garantías"]))

T.ap("s16", "IV.1 El art. 49 de la Constitución", f"""
{unidad("1.1 Personas con discapacidad (art. 49)",
  lit("CE", "Artículo 49", ["en condiciones de libertad e igualdad reales y efectivas", "Se regulará por ley la protección especial", "plena autonomía personal y la inclusión social", "las mujeres y los menores con discapacidad"]),
  ficha("Las personas con discapacidad",
        "Ejercen los derechos del Título I en condiciones de libertad e igualdad reales y efectivas",
        "—",
        "Protección especial regulada **por ley**; políticas de autonomía personal e inclusión en entornos universalmente accesibles; participación de sus organizaciones",
        "Es un principio rector (Capítulo III del Título I). Atención particular a **las mujeres y los menores** con discapacidad."))}
""", 2)

T.ap("s17", "IV.2 LGD: objeto, definiciones, principios y titulares (arts. 1 a 4)", f"""
{unidad("2.1 Objeto (art. 1)",
  lit("LGD", "a1", ["conforme a los artículos 9.2, 10, 14 y 49 de la Constitución Española", "régimen de infracciones y sanciones"]),
  fichab("Garantizar la igualdad de oportunidades y de trato de las personas con discapacidad", "Poderes públicos y particulares",
         "Promoción de la autonomía personal, accesibilidad universal, empleo, inclusión y vida independiente y erradicación de la discriminación; y régimen sancionador", "—",
         "Fundamento: CE arts. **9.2, 10, 14 y 49** y la **Convención Internacional** sobre los Derechos de las Personas con Discapacidad."))}

{unidad("2.2 Definiciones (art. 2)",
  lit("LGD", "a2", ["interacción entre las personas con deficiencias previsiblemente permanentes y cualquier tipo de barreras", "Accesibilidad universal", "Ajustes razonables", "Diálogo civil"], solo=[1, 2, 12, 14, 15]),
  fichab("Conceptos legales de la LGD", "—",
         ["Discapacidad: **interacción** entre deficiencias previsiblemente permanentes y **barreras**", "Accesibilidad universal (incluye la **cognitiva**)", "Ajustes razonables: sin **carga desproporcionada o indebida**", "Diálogo civil: participación de las organizaciones representativas"],
         "—",
         "La discapacidad no es solo la deficiencia: es su **interacción con las barreras** (modelo social)."))}

{unidad("2.3 Principios (art. 3)",
  lit("LGD", "a3", ["La vida independiente", "La accesibilidad universal", "El diálogo civil", "La transversalidad de las políticas en materia de discapacidad"]),
  fichab("Trece principios de la ley", "—", "Dignidad y autonomía, vida independiente, no discriminación, igualdad de oportunidades y entre mujeres y hombres, normalización, accesibilidad y diseño universal, participación e inclusión, diálogo civil, transversalidad…", "—",
         "Son **trece** (letras a a m)."))}

{unidad("2.4 Titulares: quién es persona con discapacidad (art. 4)",
  lit("LGD", "a4", ["previsiblemente permanentes", "igual o superior al 33 por ciento", "validez en todo el territorio nacional"], solo=[1, 3, 4, 6]),
  ficha("Las personas con deficiencias físicas, mentales, intelectuales o sensoriales previsiblemente permanentes que, con barreras, ven limitada su participación",
        "A efectos de la ley, además, quienes tengan reconocido un grado de discapacidad **igual o superior al 33 %**",
        "Se asimilan, para ciertos capítulos, los pensionistas de incapacidad permanente total, absoluta o gran invalidez y los de clases pasivas por incapacidad",
        "Reconocimiento por el órgano competente; validez en todo el territorio nacional",
        "**33 %** o más. La asimilación de los pensionistas **no** es general: solo a efectos de la sección 1.ª del capítulo V, el capítulo VIII del título I y el título II."))}
""", 2)

T.ap("s18", "IV.3 Derecho al trabajo y cuota de reserva (arts. 35, 37 y 42)", f"""
{unidad("3.1 Garantías del derecho al trabajo (art. 35)",
  lit("LGD", "a35", ["tienen derecho al trabajo", "se considera en todo caso acto discriminatorio"], solo=[1, 3, 7]),
  ficha("Las personas con discapacidad (y, a efectos del capítulo VI, los pensionistas de incapacidad permanente total, absoluta o gran invalidez)",
        "Derecho al trabajo con igualdad de trato y no discriminación",
        "—", "Nulidad de las cláusulas y decisiones discriminatorias (35.5)",
        "El **acoso** por razón de discapacidad es **en todo caso** acto discriminatorio."))}

{unidad("3.2 Tipos de empleo (art. 37)",
  lit("LGD", "a37", ["Empleo ordinario", "Empleo protegido, en centros especiales de empleo y en enclaves laborales", "Empleo autónomo"], solo=[2, 3, 4, 5, 6]),
  fichab("Tres vías de ejercicio del derecho al trabajo", "—",
         ["**Ordinario**: empresas y administraciones (incluido el empleo con apoyo)", "**Protegido**: centros especiales de empleo y enclaves laborales", "**Autónomo**"],
         "—", "Los **enclaves laborales** son empleo **protegido**; el empleo **con apoyo**, ordinario. El acceso al empleo público, por su normativa (tema V.10)."))}

{unidad("3.3 Cuota de reserva (art. 42)",
  lit("LGD", "a42", ["50 o más trabajadores", "al menos, el 2 por 100", "medidas alternativas", "se reservará un cupo"], solo=[1, 2, 3]),
  fichab("Obligación de reserva de puestos para trabajadores con discapacidad",
         "Empresas públicas y privadas de **50 o más** trabajadores; en el empleo público, las ofertas de empleo",
         "Cómputo sobre la plantilla total; exención excepcional por negociación colectiva o por opción voluntaria comunicada, con medidas alternativas",
         "Al menos el **2 %** de la plantilla",
         "**50 o más** trabajadores y **2 %**. En el empleo público, un **cupo** según su normativa."))}
""", 2)

T.ap("s19", "IV.4 Órganos y garantías (arts. 55, 56, 63 y 73)", f"""
{unidad("4.1 Consejo Nacional de la Discapacidad (art. 55)",
  lit("LGD", "a55", ["órgano colegiado interministerial, de carácter consultivo"]),
  fichab("Órgano consultivo de colaboración entre el movimiento asociativo y la AGE",
         "Movimiento asociativo de las personas con discapacidad y sus familias y la AGE",
         "Definición y coordinación de políticas; promoción de la igualdad de oportunidades y no discriminación", "—",
         "Colegiado, **interministerial** y **consultivo**."))}

{unidad("4.2 Oficina de Atención a la Discapacidad (art. 56)",
  lit("LGD", "a56", ["órgano del Consejo Nacional de la Discapacidad, de carácter permanente y especializado"]),
  fichab("Órgano permanente y especializado del Consejo Nacional", "Integrada en el Consejo Nacional de la Discapacidad; colaboran las organizaciones más representativas",
         "Promueve la igualdad de oportunidades, no discriminación y accesibilidad universal", "—",
         "Es un órgano **del Consejo Nacional**, no de un ministerio."))}

{unidad("4.3 Vulneración del derecho a la igualdad de oportunidades (art. 63)",
  lit("LGD", "a63", ["incumplimientos de las exigencias de accesibilidad y de realizar ajustes razonables"]),
  ficha("Las personas con discapacidad definidas en el art. 4.1",
        "Igualdad de oportunidades frente a discriminaciones, acosos, falta de accesibilidad y de ajustes razonables",
        "—", "Medidas contra la discriminación y de acción positiva (art. 64); arbitraje y tutela judicial (arts. 74 y 75)",
        "También vulnera el derecho **no realizar ajustes razonables** o incumplir la **accesibilidad**."))}

{unidad("4.4 Observatorio Estatal de la Discapacidad (art. 73)",
  lit("LGD", "a73", ["instrumento técnico de la Administración General del Estado", "Con carácter anual"], solo=[1, 2]),
  fichab("Instrumento técnico de información sobre la discapacidad",
         "AGE, a través de la Dirección General de Derechos de las Personas con Discapacidad",
         "Recopila, sistematiza y difunde información; orienta las políticas públicas",
         "Informe **anual** al Consejo Nacional de la Discapacidad",
         "Es un **instrumento técnico** (no un órgano colegiado como el Observatorio de violencia sobre la mujer, → II.3.2)."))}

{resumen([
  "Art. 49 CE: las personas con discapacidad ejercen sus derechos con libertad e igualdad **reales y efectivas**; protección especial **por ley**.",
  "LGD: discapacidad = **interacción** de deficiencias permanentes con **barreras**; persona con discapacidad, a efectos de la ley, con grado **≥ 33 %** (art. 4).",
  "Empleo: ordinario, **protegido** (centros especiales y enclaves) y autónomo; cuota del **2 %** en empresas de **50 o más** trabajadores.",
  "Órganos: Consejo Nacional (consultivo, interministerial), Oficina de Atención a la Discapacidad (del Consejo) y Observatorio Estatal (instrumento técnico, informe anual)."],
  "Siguiente: V. ¿Cómo se atiende la dependencia?")}
""", 2)

# =============================================================================
T.ap("bV", "V. ¿Cómo se atiende la dependencia? (Ley 39/2006)", donde(
  "Quinta pregunta. La **Ley 39/2006**, de 14 de diciembre, de Promoción de la Autonomía Personal y Atención a las personas en situación de dependencia, crea el **Sistema para la Autonomía y Atención a la Dependencia** (SAAD) y un derecho subjetivo de ciudadanía.",
  ["1 Objeto, definiciones, principios y titulares", "2 El Sistema y sus niveles", "3 Prestaciones y servicios", "4 Grados, valoración y procedimiento"]))

T.ap("s20", "V.1 Objeto, definiciones, principios y titulares (arts. 1, 2, 3 y 5)", f"""
{unidad("1.1 Objeto (art. 1)",
  lit("L39_2006", "Artículo 1", ["derecho subjetivo de ciudadanía", "contenido mínimo común de derechos", "acción coordinada y cooperativa"]),
  fichab("Condiciones básicas del derecho a la promoción de la autonomía personal y atención a la dependencia",
         "Todas las Administraciones; la AGE garantiza un contenido mínimo común; acción coordinada de AGE y CC. AA., con participación de las Entidades Locales",
         "Mediante la creación del Sistema para la Autonomía y Atención a la Dependencia", "—",
         "Es un **derecho subjetivo de ciudadanía**."))}

{unidad("1.2 Definiciones (art. 2)",
  lit("L39_2006", "Artículo 2", ["el estado de carácter permanente", "las tareas más elementales de la persona", "no vinculadas a un servicio de atención profesionalizada"], solo=[1, 3, 4, 6]),
  fichab("Conceptos legales", "—",
         ["Dependencia: estado **permanente** por edad, enfermedad o discapacidad que exige atención de otra persona o ayudas importantes para las ABVD", "ABVD: cuidado personal, actividades domésticas básicas, movilidad esencial, reconocer personas y objetos, orientarse, entender y ejecutar órdenes", "Cuidados no profesionales: familia o entorno"],
         "—", "La dependencia es un estado de carácter **permanente**."))}

{unidad("1.3 Principios (art. 3)",
  lit("L39_2006", "Artículo 3", ["El carácter público de las prestaciones", "La universalidad en el acceso", "La permanencia de las personas en situación de dependencia, siempre que sea posible, en el entorno", "serán atendidas de manera preferente"], solo=[1, 2, 3, 10, 19]),
  fichab("Principios inspiradores de la ley", "—",
         ["Carácter **público** de las prestaciones", "**Universalidad** en el acceso", "Atención integral e integrada", "Permanencia en el entorno", "Perspectiva de género", "Gran dependencia: atención **preferente**"],
         "—", "Las personas en **gran dependencia** se atienden **de manera preferente**."))}

{unidad("1.4 Titulares de derechos (art. 5)",
  lit("L39_2006", "Artículo 5", ["durante cinco años, de los cuales dos deberán ser inmediatamente anteriores"], solo=[1, 2, 3, 4]),
  ficha("Los españoles en situación de dependencia en alguno de los grados",
        "Los derechos de la ley",
        "Residencia en España durante **cinco años**, **dos** inmediatamente anteriores a la solicitud (menores de cinco años: se exige a quien tenga su guarda); menores de 3 años, disposición adicional decimotercera",
        "Los extranjeros, según la LO 4/2000 y los tratados (5.2)",
        "**Cinco años** de residencia, **dos** de ellos inmediatamente anteriores."))}
""", 2)

T.ap("s21", "V.2 El Sistema y sus niveles (arts. 6, 8 y 9)", f"""
{unidad("2.1 Finalidad del Sistema (art. 6)",
  lit("L39_2006", "Artículo 6", ["red de utilización pública"]),
  fichab("El SAAD: cauce de colaboración y red de centros y servicios", "Administraciones públicas; centros y servicios públicos y privados",
         "Garantiza condiciones básicas y contenido común; optimiza recursos", "—",
         "Red de **utilización pública** que integra centros **públicos y privados**, sin alterar su titularidad."))}

{unidad("2.2 Consejo Territorial (art. 8)",
  lit("L39_2006", "Artículo 8", ["instrumento de cooperación", "que ostentará su presidencia", "tendrán mayoría los representantes de las comunidades autónomas", "Acordar el baremo"], solo=[1, 2, 8]),
  fichab("Consejo Territorial de Servicios Sociales y del Sistema para la Autonomía y Atención a la Dependencia",
         "Preside el titular del Ministerio; lo integran los Consejeros de las CC. AA. (una de ellas, vicepresidencia)",
         "Acuerda el marco de cooperación, los criterios de intensidad, las prestaciones económicas, la participación en el coste y el **baremo**",
         "Mayoría de los representantes de las **comunidades autónomas**",
         "Preside el **Ministro**, pero la **mayoría** es de las **CC. AA.** El baremo se **acuerda** aquí y lo **aprueba el Gobierno** por real decreto (art. 27 → V.4.2)."))}

{unidad("2.3 Nivel mínimo de protección (art. 9)",
  lit("L39_2006", "Artículo 9", ["nivel mínimo de protección garantizado", "correrá a cuenta de la Administración General del Estado"]),
  fichab("Nivel mínimo garantizado por el Estado", "El **Gobierno**, oído el Consejo Territorial; lo financia la **AGE**",
         "Según el grado de dependencia; se asigna a las CC. AA. por beneficiarios, grado y prestación", "Recursos fijados **anualmente** en la Ley de Presupuestos Generales del Estado",
         "Tres niveles: **mínimo** (AGE, art. 9), **acordado** por convenios AGE-CC. AA. (art. 10) y **adicional** de cada comunidad autónoma."))}
""", 2)

T.ap("s22", "V.3 Prestaciones y servicios (arts. 14, 15, 17 a 19 y 23; RD 1051/2013, anexo II)", f"""
{unidad("3.1 Prestaciones de atención a la dependencia (art. 14)",
  lit("L39_2006", "Artículo 14", ["tendrán carácter prioritario", "excepcionalmente, recibir una prestación económica para ser atendido por cuidadores no profesionales", "por el grado de dependencia y, a igual grado, por la capacidad económica", "son inembargables"], solo=[1, 2, 4, 6, 8]),
  fichab("Servicios y prestaciones económicas", "Servicios: red de servicios sociales de las CC. AA. (centros públicos o privados concertados acreditados)",
         ["Servicios del Catálogo: **prioritarios**", "Prestación vinculada al servicio (art. 17)", "Cuidados en el entorno familiar: **excepcional** (art. 18)", "Asistencia personal (art. 19)"],
         "Prioridad: **grado** y, a igual grado, **capacidad económica**",
         "Los **servicios** son prioritarios; los cuidados familiares, **excepcionales**. Las prestaciones económicas son **inembargables**."))}

{unidad("3.2 Catálogo de servicios (art. 15)",
  lit("L39_2006", "Artículo 15", ["Servicio de Teleasistencia", "Servicio de Ayuda a domicilio", "Servicio de Centro de Día y de Noche", "Servicio de Atención Residencial"], solo=[1, 2, 3, 4, 7, 12]),
  fichab("Servicios sociales de promoción de la autonomía y atención a la dependencia", "—",
         ["Prevención y promoción de la autonomía personal", "Teleasistencia", "Ayuda a domicilio", "Centro de Día y de Noche", "Atención Residencial"],
         "—", "Cinco servicios (letras a a e)."))}

{unidad("3.3 Prestaciones económicas (arts. 17, 18 y 19)",
  lit("L39_2006", "Artículo 17", ["únicamente cuando no sea posible el acceso a un servicio público o concertado"], solo=[1]),
  lit("L39_2006", "Artículo 18", ["Excepcionalmente"], solo=[1]),
  lit("L39_2006", "Artículo 19", ["en cualquiera de sus grados"]),
  fichab("Tres prestaciones económicas", "Beneficiarios según su PIA",
         ["**Vinculada al servicio**: periódica, solo si no hay servicio público o concertado", "**Cuidados en el entorno familiar**: excepcional", "**Asistencia personal**: contratar una asistencia personal, en **cualquier grado**"],
         "—", "La de asistencia personal sirve para el acceso a la **educación y al trabajo** y a una vida más autónoma."))}

{unidad("3.4 Servicio de Ayuda a Domicilio (art. 23; RD 1051/2013, anexo II)",
  lit("L39_2006", "Artículo 23", ["sólo podrán prestarse conjuntamente"]),
  lit("RD1051", "anii", ["Grado II: De 38 a 64 horas mensuales"], titulo="Anexo II. Intensidad del servicio de ayuda a domicilio (RD 1051/2013, redacción vigente)"),
  fichab("Atención en el domicilio de la persona dependiente", "Entidades o empresas acreditadas",
         "Atención personal y, conjuntamente, atención de necesidades domésticas (separadas solo excepcionalmente, si lo dispone el PIA)",
         "Grado I: **20-37** h/mes; Grado II: **38-64**; Grado III: **65-94**",
         "Cayó dos veces en 2025 (→ Cierre 1): Grado II = **38 a 64** horas mensuales."))}
""", 2)

T.ap("s23", "V.4 Grados, valoración y procedimiento (arts. 26 a 29 y 33)", f"""
{unidad("4.1 Grados de dependencia (art. 26)",
  lit("L39_2006", "Artículo 26", ["Grado I. Dependencia moderada", "Grado II. Dependencia severa", "Grado III. Gran dependencia", "al menos una vez al día", "dos o tres veces al día", "varias veces al día"], solo=[1, 2, 3, 4]),
  fichab("Clasificación de la dependencia en tres grados", "—",
         ["Grado I, **moderada**: ayuda al menos **una vez al día**", "Grado II, **severa**: **dos o tres veces al día**", "Grado III, **gran dependencia**: **varias veces al día** y apoyo indispensable y continuo"],
         "Intervalos fijados en el baremo (art. 27)",
         "Moderada (I) → severa (II) → gran dependencia (III)."))}

{unidad("4.2 Valoración (art. 27)",
  lit("L39_2006", "Artículo 27", ["Las comunidades autónomas determinarán los órganos de valoración", "aprobación por el Gobierno mediante real decreto", "Clasificación Internacional del Funcionamiento, la Discapacidad y la Salud (CIF)"], solo=[1, 2]),
  fichab("Valoración del grado mediante un baremo único", "Órganos de valoración de las **CC. AA.** (públicos); baremo acordado en el Consejo Territorial y aprobado por el **Gobierno**",
         "Dictamen sobre el grado con los cuidados que requiera; referente: la CIF de la OMS", "—",
         "Solo vale el **baremo**: no puede determinarse el grado por otros procedimientos."))}

{unidad("4.3 Procedimiento de reconocimiento (art. 28)",
  lit("L39_2006", "Artículo 28", ["a instancia de la persona", "Administración Autonómica correspondiente a la residencia del solicitante", "no pudiendo ser objeto de delegación, contratación o concierto"], solo=[1, 2, 6]),
  fichab("Reconocimiento de la situación de dependencia y del derecho a las prestaciones",
         "Se inicia a instancia del interesado o su representante; resuelve la **Administración autonómica** de su residencia",
         "Resolución con los servicios o prestaciones según el grado; validez en todo el Estado", "—",
         "Se inicia **a instancia** de parte. La valoración y la gestión **no** pueden delegarse, contratarse ni concertarse con entidades privadas."))}

{unidad("4.4 Programa Individual de Atención (art. 29)",
  lit("L39_2006", "Artículo 29", ["programa individual de atención", "Con motivo del cambio de residencia"], solo=[1, 3, 4, 5, 6]),
  fichab("Programa que concreta los servicios y prestaciones de cada persona", "Servicios sociales del sistema público, con participación del beneficiario",
         "Determina las modalidades de intervención más adecuadas entre las de su grado",
         "Revisión a instancia del interesado, de oficio o por cambio de comunidad autónoma",
         "Tres causas de revisión: **a instancia**, **de oficio** y **cambio de residencia** a otra CC. AA."))}

{unidad("4.5 Participación en el coste (art. 33)",
  lit("L39_2006", "Artículo 33", ["según el tipo y coste del servicio y su capacidad económica personal", "Ningún ciudadano quedará fuera de la cobertura del Sistema"], solo=[1, 5]),
  ficha("Los beneficiarios", "Participan en la financiación según el tipo y coste del servicio y su capacidad económica",
        "Criterios fijados por el Consejo Territorial", "Nadie queda fuera del Sistema por falta de recursos",
        "Copago según **capacidad económica**; garantía: **ningún ciudadano** queda fuera por no tener recursos."))}

{resumen([
  "Ley 39/2006: **derecho subjetivo de ciudadanía**; el **SAAD** es una red de utilización pública; principios de carácter **público**, **universalidad** y atención **preferente** a la gran dependencia.",
  "Titulares: españoles dependientes con **cinco años** de residencia (**dos** inmediatamente anteriores).",
  "Consejo Territorial: preside el **Ministro**, **mayoría autonómica**; acuerda el **baremo**. Nivel **mínimo** a cargo de la **AGE**.",
  "Servicios **prioritarios**; cuidados familiares **excepcionales**; ayuda a domicilio en Grado II: **38-64 h/mes** (RD 1051/2013).",
  "Grados: I **moderada**, II **severa**, III **gran dependencia**; resuelve la **comunidad autónoma** de residencia; PIA revisable."],
  "Fin del tema. Para fijarlo: Cierre 1 (preguntas oficiales de 2025) y Cierre 2 (repaso por bloques); después, el test.")}
""", 2)

# =============================================================================
L3D = "Cualquier conducta realizada por razón de alguna de las causas de discriminación previstas en esta ley, con el objetivo o la consecuencia de atentar contra la dignidad de una persona o grupo en que se integra y de crear un entorno intimidatorio, hostil, degradante, humillante u ofensivo"
POR_ACOSO = {
  "a": f"Literal del art. 3 d) de la Ley 4/2023 (acoso discriminatorio): {c('L4_2023', 'Artículo 3', 'Acoso discriminatorio: Cualquier conducta realizada por razón de alguna de las causas de discriminación previstas en esta ley')}.",
  "b": f"Es la definición de **LGTBIfobia**, art. 3 m): {c('L4_2023', 'Artículo 3', 'LGTBIfobia: Toda actitud, conducta o discurso de rechazo, repudio, prejuicio, discriminación o intolerancia hacia las personas LGTBI')}.",
  "c": f"Es la definición de **discriminación directa**, art. 3 a): {c('L4_2023', 'Artículo 3', 'Discriminación directa: Situación en que se encuentra una persona o grupo en que se integra que sea, haya sido o pudiera ser tratada de manera menos favorable')}.",
  "d": f"Es la definición de **medidas de acción positiva**, art. 3 f): {c('L4_2023', 'Artículo 3', 'Medidas de acción positiva: Diferencias de trato orientadas a prevenir, eliminar y, en su caso, compensar cualquier forma de discriminación')}."}
EX_L43 = examen("L", 43, POR_ACOSO, [("entorno intimidatorio, hostil, degradante, humillante u ofensivo", "L4_2023", "Artículo 3", "Acoso discriminatorio: " + L3D)])
EX_P42 = examen("P", 42, POR_ACOSO, [("entorno intimidatorio, hostil, degradante, humillante u ofensivo", "L4_2023", "Artículo 3", "Acoso discriminatorio: " + L3D)])
EX_X52 = examen("X", 52, {
  "a": f"Cambia el umbral: el art. 15.1 dice {c('L4_2023', 'Artículo 15', 'Las empresas de más de cincuenta personas trabajadoras')}, no cuarenta.",
  "b": "Cambia el umbral: treinta no aparece en el art. 15.1; el umbral es más de cincuenta.",
  "c": "Cambia el umbral: cien no aparece en el art. 15.1; el umbral es más de cincuenta.",
  "d": f"Literal del art. 15.1: {c('L4_2023', 'Artículo 15', 'Las empresas de más de cincuenta personas trabajadoras deberán contar')} con el conjunto planificado de medidas y el protocolo frente al acoso o la violencia."},
  [("más de cincuenta personas trabajadoras", "L4_2023", "Artículo 15", "Las empresas de más de cincuenta personas trabajadoras deberán contar")])
EX_P41 = examen("P", 41, {
  "a": f"Invierte el anexo I: las empresas contribuirán {c('RD1026', 'ai', 'a erradicar estereotipos en el acceso al empleo de las personas LGTBI')}, no a «potenciar» estereotipos.",
  "b": f"Invierte el anexo I: {c('RD1026', 'ai', 'Se promoverá la heterogeneidad de las plantillas para lograr entornos laborales diversos, inclusivos y seguros')}; no la «homogeneidad» para entornos «no diversos».",
  "c": f"Invierte el anexo I: los convenios atenderán a las familias diversas {c('RD1026', 'ai', 'garantizando el acceso a los permisos, beneficios sociales y derechos sin discriminación')}, no «sin garantizar».",
  "d": f"Literal del anexo I (Primero): {c('RD1026', 'ai', 'Los convenios colectivos o acuerdos de empresa recogerán en su articulado cláusulas de igualdad de trato y no discriminación que contribuyan a crear un contexto favorable a la diversidad')}."},
  [("contexto favorable a la diversidad", "RD1026", "ai", "cláusulas de igualdad de trato y no discriminación que contribuyan a crear un contexto favorable a la diversidad")])
EX_X51 = examen("X", 51, {
  "a": f"RD 246/2024, art. 2.3: de la Secretaría de Estado dependen órganos directivos {c('RD246', 'Artículo 2', 'con rango de dirección general')}, el primero {c('RD246', 'Artículo 2', 'La Delegación del Gobierno contra la Violencia de Género')}.",
  "b": "Secretaría General es otro rango de órgano directivo; el RD 246/2024 da a la Delegación rango de dirección general.",
  "c": "Subdirección General es un rango inferior; en el RD 246/2024 ese nivel lo tiene, por ejemplo, el Gabinete de la Secretaría de Estado (art. 2.6), no la Delegación.",
  "d": f"La Secretaría de Estado es el órgano superior del que **depende** la Delegación: {c('RD246', 'Artículo 2', 'De la Secretaría de Estado de Igualdad y para la Erradicación de la Violencia contra las Mujeres dependen los siguientes órganos directivos')}."},
  [("De Dirección General", "RD246", "Artículo 2", "dependen los siguientes órganos directivos, con rango de dirección general")])
EX_X53 = examen("X", 53, {
  "a": "Cambia el año final: el plan es (2023-2027), no hasta 2028.",
  "b": "Cambia el año inicial: el plan arranca en 2023 (aprobado el 3 de marzo de 2023), no en 2024.",
  "c": f"Literal de la Resolución de 16-3-2023 (BOE-A-2023-7326): {c('PCP2023', 'preambulo', 'el plan conjunto plurianual en materia de violencia contra las mujeres (2023-2027)')}.",
  "d": "Cambia los dos años: el periodo es 2023-2027."},
  [("2023 a 2027", "PCP2023", "preambulo", "en su reunión de 3 de marzo de 2023, ha aprobado el acuerdo por el que se aprueba el plan conjunto plurianual en materia de violencia contra las mujeres (2023-2027)")])
EX_L103 = examen("L", 103, {
  "a": "Cifras inventadas: la publicación oficial habla de 290 medidas en 2017 y 461 en 2025.",
  "b": "Cifras inventadas: ni 15 ni 62 aparecen en la publicación oficial.",
  "c": f"Literal de la publicación oficial de la Delegación del Gobierno (no es texto legal): {c('PACTO2025', T_, 'El acuerdo amplía las medidas que incluía en 2017 de 290 a 461')}.",
  "d": "Cifras inventadas: ni 100 ni 180 aparecen en la publicación oficial."},
  [("290 a 461", "PACTO2025", T_, "El acuerdo amplía las medidas que incluía en 2017 de 290 a 461")])
POR_SAD = {
  "a": f"Es la intensidad del **Grado I**: {c('RD1051', 'anii', 'Grado I: De 20 a 37 horas mensuales')}.",
  "b": f"Es la intensidad del **Grado III**: {c('RD1051', 'anii', 'Grado III: De 65 a 94 horas mensuales')}.",
  "c": "Cifras que no están en el anexo II: el Grado II va de 38 a 64 horas.",
  "d": f"Literal del anexo II del RD 1051/2013: {c('RD1051', 'anii', 'Grado II: De 38 a 64 horas mensuales')}."}
EX_L42 = examen("L", 42, POR_SAD, [("De 38 a 64 horas mensuales", "RD1051", "anii", "Grado II: De 38 a 64 horas mensuales")])
EX_P43 = examen("P", 43, POR_SAD, [("De 38 a 64 horas mensuales", "RD1051", "anii", "Grado II: De 38 a 64 horas mensuales")])

T.ap("s24", "Cierre 1. Preguntas de los exámenes de 2025 sobre este tema", "\n\n".join([
  "En los primeros ejercicios de **2025** cayeron **siete** preguntas de este tema (una de ellas de reserva) y **dos** relacionadas (dependencia, sin tema asignado). Aquí están **literales**. Pulsa la opción que creas correcta: se marca en verde o en rojo y aparece el porqué de cada opción. La respuesta de la plantilla se ha comprobado contra el texto legal (o, en el Pacto de Estado, contra la publicación oficial).",
  "### GACE-L 2025, pregunta 43 · Acoso discriminatorio en la Ley 4/2023 (→ III.3.2)", EX_L43,
  "### GACE-P 2025, pregunta 42 · Acoso discriminatorio en la Ley 4/2023 (→ III.3.2)", EX_P42,
  "### GACE-X 2025, pregunta 52 · Empresas obligadas a las medidas LGTBI (→ III.3.4)", EX_X52,
  "### GACE-P 2025, pregunta 41 · Anexo del RD 1026/2024 (→ III.4.2)", EX_P41,
  "### GACE-X 2025, pregunta 51 · Rango de la Delegación del Gobierno contra la Violencia de Género (→ II.3.1)", EX_X51,
  "### GACE-X 2025, pregunta 53 · Plan conjunto plurianual (→ II.4.2)", EX_X53,
  "### GACE-L 2025, pregunta 103 (reserva) · Pacto de Estado de 2025 (→ II.4.1)", EX_L103,
  "### GACE-L 2025, pregunta 42 · Ayuda a domicilio en el Grado II (relacionada; → V.3.4)", EX_L42,
  "### GACE-P 2025, pregunta 43 · Ayuda a domicilio en el Grado II (relacionada; → V.3.4)", EX_P43,
  "### Cómo se pregunta",
  "!> Dos técnicas: **definiciones vecinas** (en el art. 3 de la Ley 4/2023 los distractores eran otras letras del mismo artículo) y **cifras cambiadas** (más de **cincuenta** trabajadores, **38-64** horas, **2023-2027**, **290 a 461**). Memoriza las cifras del Cierre 2.",
]))

T.ap("s25", "Cierre 2. Repaso en 10 minutos (por bloques)", f"""
| Bloque | Lo esencial | Dato que más cae |
|---|---|---|
| I. Igualdad de mujeres y hombres | CE 9.2 y 14; LO 3/2007: conceptos (6-8), acción positiva (11), planes (45-46), AGE (51-64), órganos (76-78) | **60/40**; plan de igualdad en empresas de **50 o más**; Plan AGE al **inicio de cada legislatura** |
| II. Violencia de género | LO 1/2004: concepto (1), derechos (17-27), acreditación (23), Delegación y Observatorio (29-30) | Delegación con **rango de dirección general**; Pacto **290 → 461**; plan conjunto **2023-2027** |
| III. Igualdad de trato y LGTBI | Ley 15/2022 (causas, definiciones, Autoridad Independiente); Ley 4/2023 (definiciones, Consejo, empresas, rectificación) | Empresas de **más de cincuenta**; acoso discriminatorio = art. 3 d); Autoridad: **5 años no renovable** |
| IV. Discapacidad | CE 49; LGD: definiciones, titulares, empleo, órganos | **33 %**; cuota **2 %** en empresas de **50 o más** |
| V. Dependencia | Ley 39/2006: SAAD, Consejo Territorial, prestaciones, grados, procedimiento | Residencia **5 años (2 inmediatos)**; Grado II = **severa**; ayuda a domicilio Grado II **38-64 h** |

?> **Trampas frecuentes:** «plan de igualdad en empresas de **más de** cincuenta» (son **cincuenta o más**; el «más de cincuenta» es de la Ley 4/2023); «embarazo = discriminación **indirecta**» (es **directa**); «Delegación con rango de **Secretaría General**» (es **dirección general**); «Consejo Territorial con mayoría de la **AGE**» (la mayoría es de las **CC. AA.**); «cuidados familiares como prestación **prioritaria**» (son **excepcionales**); «mandato renovable» de la Autoridad Independiente (**no** renovable).
""")

# =============================================================================
# Test: cada pregunta se apoya en un fragmento literal del artículo citado.
q = T.q
q("CE", "Artículo 9", "Fundamento", "Según el artículo 9.2 de la Constitución, corresponde a los poderes públicos promover las condiciones para que la libertad y la igualdad del individuo y de los grupos en que se integra sean:",
  ["Reales y efectivas.", "Formales y materiales.", "Plenas y universales.", "Iguales y proporcionadas."], "Art. 9.2 CE.", "sean reales y efectivas")
q("LO3_2007", "Artículo 1", "LO 3/2007", "Según el artículo 1 de la Ley Orgánica 3/2007, esta ley se dicta en desarrollo de los artículos de la Constitución:",
  ["9.2 y 14.", "10 y 14.", "9.2, 10 y 14.", "14 y 53.2."], "Art. 1.1 LO 3/2007: «en el desarrollo de los artículos 9.2 y 14 de la Constitución». (La Ley 15/2022 cita además el 10.)", "en el desarrollo de los artículos 9.2 y 14 de la Constitución")
q("LO3_2007", "Artículo 3", "LO 3/2007", "Según el artículo 3 de la Ley Orgánica 3/2007, el principio de igualdad de trato supone la ausencia de toda discriminación por razón de sexo y, especialmente, las derivadas de:",
  ["La maternidad, la asunción de obligaciones familiares y el estado civil.", "La edad, la nacionalidad y el estado civil.", "La maternidad, la orientación sexual y la religión.", "La asunción de obligaciones familiares, la discapacidad y la edad."], "Art. 3 LO 3/2007.", "la maternidad, la asunción de obligaciones familiares y el estado civil")
q("LO3_2007", "Artículo 8", "LO 3/2007", "Según el artículo 8 de la Ley Orgánica 3/2007, todo trato desfavorable a las mujeres relacionado con el embarazo o la maternidad constituye:",
  ["Discriminación directa por razón de sexo.", "Discriminación indirecta por razón de sexo.", "Acoso por razón de sexo.", "Una infracción leve."], "Art. 8 LO 3/2007.", "Constituye discriminación directa por razón de sexo todo trato desfavorable a las mujeres relacionado con el embarazo o la maternidad")
q("LO3_2007", "Artículo 7", "LO 3/2007", "Según el artículo 7.2 de la Ley Orgánica 3/2007, constituye acoso por razón de sexo cualquier comportamiento realizado:",
  ["En función del sexo de una persona, con el propósito o el efecto de atentar contra su dignidad y de crear un entorno intimidatorio, degradante u ofensivo.", "De naturaleza sexual, verbal o físico, que atente contra la dignidad de la persona.", "Con ocasión de la presentación de una queja o reclamación por discriminación.", "Por una persona superior jerárquica, siempre que exista reiteración."],
  "Art. 7.2 LO 3/2007. La b) es el acoso **sexual** (7.1).", "Constituye acoso por razón de sexo cualquier comportamiento realizado en función del sexo de una persona")
q("LO3_2007", "Artículo 11", "LO 3/2007", "Según el artículo 11 de la Ley Orgánica 3/2007, las medidas de acción positiva que adopten los Poderes Públicos serán aplicables:",
  ["En tanto subsistan las situaciones de desigualdad de hecho, y habrán de ser razonables y proporcionadas.", "Con carácter indefinido, por ser medidas estructurales.", "Durante un plazo máximo de ocho años.", "Solo en el ámbito del empleo público."], "Art. 11.1 LO 3/2007.", "que serán aplicables en tanto subsistan dichas situaciones")
q("LO3_2007", "Artículo 12", "LO 3/2007", "Según el artículo 12.3 de la Ley Orgánica 3/2007, en los litigios sobre acoso sexual y acoso por razón de sexo estará legitimada:",
  ["Únicamente la persona acosada.", "La persona acosada y los sindicatos más representativos.", "Cualquier persona con interés legítimo.", "La persona acosada y el Ministerio Fiscal, conjuntamente."], "Art. 12.3 LO 3/2007.", "La persona acosada será la única legitimada")
q("LO3_2007", "Artículo 45", "LO 3/2007", "Según el artículo 45.2 de la Ley Orgánica 3/2007, deben elaborar y aplicar un plan de igualdad las empresas de:",
  ["Cincuenta o más trabajadores.", "Más de doscientos cincuenta trabajadores.", "Más de cien trabajadores.", "Veinticinco o más trabajadores."], "Art. 45.2 LO 3/2007.", "En el caso de las empresas de cincuenta o más trabajadores")
q("LO3_2007", "Artículo 46", "LO 3/2007", "Según el artículo 46 de la Ley Orgánica 3/2007, los planes de igualdad de las empresas son un conjunto ordenado de medidas adoptadas:",
  ["Después de realizar un diagnóstico de situación.", "Antes de realizar un diagnóstico de situación.", "Por la autoridad laboral, sin negociación.", "Por la Comisión Interministerial de Igualdad."], "Art. 46.1 LO 3/2007.", "adoptadas después de realizar un diagnóstico de situación")
q("LO3_2007", "Artículo 64", "LO 3/2007", "Según el artículo 64 de la Ley Orgánica 3/2007, el Plan para la Igualdad entre mujeres y hombres en la Administración General del Estado se aprueba:",
  ["Por el Gobierno, al inicio de cada legislatura.", "Por el Ministerio de Igualdad, cada cuatro años.", "Por las Cortes Generales, al inicio de cada legislatura.", "Por el Gobierno, cada dos años."], "Art. 64 LO 3/2007; su cumplimiento lo evalúa anualmente el Consejo de Ministros.", "El Gobierno aprobará, al inicio de cada legislatura")
q("LO3_2007", "Artículo 55", "LO 3/2007", "Según el artículo 55 de la Ley Orgánica 3/2007, la aprobación de convocatorias de pruebas selectivas para el acceso al empleo público deberá acompañarse de:",
  ["Un informe de impacto de género, salvo en casos de urgencia.", "Un informe de la Comisión Interministerial de Igualdad.", "Un plan de igualdad específico.", "Un informe del Consejo de Participación de la Mujer."], "Art. 55 LO 3/2007.", "deberá acompañarse de un informe de impacto de género, salvo en casos de urgencia")
q("LO3_2007", "Artículo 78", "LO 3/2007", "Según el artículo 78 de la Ley Orgánica 3/2007, el Consejo de Participación de la Mujer es un órgano colegiado:",
  ["De consulta y asesoramiento.", "De coordinación de los departamentos ministeriales.", "De control de los planes de igualdad de las empresas.", "Sancionador en materia de igualdad."], "Art. 78.1 LO 3/2007. La coordinación es de la Comisión Interministerial (art. 76).", "como órgano colegiado de consulta y asesoramiento")
q("LO3_2007", D, "LO 3/2007", "Según la disposición adicional primera de la Ley Orgánica 3/2007, se entiende por composición equilibrada la presencia de mujeres y hombres de forma que las personas de cada sexo:",
  ["No superen el sesenta por ciento ni sean menos del cuarenta por ciento.", "No superen el setenta por ciento ni sean menos del treinta por ciento.", "Representen exactamente el cincuenta por ciento.", "No superen el sesenta y cinco por ciento ni sean menos del treinta y cinco por ciento."], "Disp. adic. 1.ª LO 3/2007.", "no superen el sesenta por ciento ni sean menos del cuarenta por ciento")
q("LO1_2004", "Artículo 1", "Violencia de género", "Según el artículo 1.1 de la Ley Orgánica 1/2004, la violencia de género que regula es la ejercida sobre las mujeres por quienes sean o hayan sido sus cónyuges o estén o hayan estado ligados a ellas por relaciones similares de afectividad:",
  ["Aun sin convivencia.", "Siempre que exista convivencia.", "Siempre que haya hijos en común.", "Durante los dos años siguientes a la ruptura."], "Art. 1.1 LO 1/2004.", "ligados a ellas por relaciones similares de afectividad, aun sin convivencia")
q("LO1_2004", "Artículo 19", "Violencia de género", "Según el artículo 19.1 de la Ley Orgánica 1/2004, la organización de los servicios sociales de atención a las víctimas responderá a los principios de:",
  ["Atención permanente, actuación urgente, especialización de prestaciones y multidisciplinariedad profesional.", "Gratuidad, universalidad y confidencialidad.", "Eficacia, eficiencia y coordinación.", "Atención permanente, gratuidad y descentralización."], "Art. 19.1 LO 1/2004.", "atención permanente, actuación urgente, especialización de prestaciones y multidisciplinariedad profesional")
q("LO1_2004", "Artículo 20", "Violencia de género", "Según el artículo 20.1 de la Ley Orgánica 1/2004, las víctimas de violencia de género tienen derecho a recibir asesoramiento jurídico gratuito:",
  ["En el momento inmediatamente previo a la interposición de la denuncia.", "Solo después de interponer la denuncia.", "Solo si acreditan insuficiencia de recursos.", "Una vez dictada la orden de protección."], "Art. 20.1 LO 1/2004.", "asesoramiento jurídico gratuito en el momento inmediatamente previo a la interposición de la denuncia")
q("LO1_2004", "Artículo 23", "Violencia de género", "Según el artículo 23 de la Ley Orgánica 1/2004, las situaciones de violencia de género que dan lugar al reconocimiento de derechos pueden acreditarse, entre otros, mediante:",
  ["El informe del Ministerio Fiscal que indique la existencia de indicios de que la demandante es víctima de violencia de género.", "Únicamente una sentencia condenatoria firme.", "Una declaración responsable de la víctima.", "El informe de la Delegación del Gobierno contra la Violencia de Género."], "Art. 23 LO 1/2004.", "o bien por el informe del Ministerio Fiscal que indique la existencia de indicios de que la demandante es víctima de violencia de género")
q("LO1_2004", "Artículo 24", "Violencia de género", "Según el artículo 24 de la Ley Orgánica 1/2004, la funcionaria víctima de violencia de género tendrá derecho, en los términos de su legislación específica, a:",
  ["La reducción o la reordenación de su tiempo de trabajo, la movilidad geográfica de centro de trabajo y la excedencia.", "La suspensión de la relación funcionarial con reserva de puesto y la extinción.", "Un permiso retribuido de seis meses.", "La jubilación anticipada."], "Art. 24 LO 1/2004.", "a la reducción o a la reordenación de su tiempo de trabajo, a la movilidad geográfica de centro de trabajo y a la excedencia")
q("LO1_2004", "Artículo 27", "Violencia de género", "Según el artículo 27.2 de la Ley Orgánica 1/2004, el importe de la ayuda de pago único a las víctimas, con carácter general, será equivalente al de:",
  ["Seis meses de subsidio por desempleo.", "Doce meses de subsidio por desempleo.", "Tres meses del salario mínimo interprofesional.", "Veinticuatro meses de subsidio por desempleo."], "Art. 27.2: seis meses; doce si la víctima tiene discapacidad ≥ 33 %.", "El importe de esta ayuda será equivalente al de seis meses de subsidio por desempleo")
q("LO1_2004", "Artículo 30", "Violencia de género", "Según el artículo 30.2 de la Ley Orgánica 1/2004, el Observatorio Estatal de Violencia sobre la Mujer remitirá su informe sobre la evolución de la violencia ejercida sobre la mujer:",
  ["Al Gobierno y a las Comunidades Autónomas, con periodicidad anual.", "A las Cortes Generales, con periodicidad semestral.", "Al Defensor del Pueblo, con periodicidad anual.", "Al Consejo General del Poder Judicial, cada dos años."], "Art. 30.2 LO 1/2004.", "remitirá al Gobierno y a las Comunidades Autónomas, con periodicidad anual")
q("L15_2022", "Artículo 6", "Igualdad de trato", "Según el artículo 6.3 de la Ley 15/2022, se produce discriminación interseccional cuando:",
  ["Concurren o interactúan diversas causas de las previstas en la ley, generando una forma específica de discriminación.", "Una persona es discriminada de manera simultánea o consecutiva por dos o más causas.", "Una persona es discriminada por su relación con otra en quien concurre una causa.", "La discriminación se funda en una apreciación incorrecta de las características de la persona."],
  "Art. 6.3 b). La b) es la discriminación **múltiple**; la c), por **asociación**; la d), por **error**.", "Se produce discriminación interseccional cuando concurren o interactúan diversas causas de las previstas en esta ley, generando una forma específica de discriminación")
q("L15_2022", "Artículo 6", "Igualdad de trato", "Según el artículo 6.1 a) de la Ley 15/2022, la denegación de ajustes razonables a las personas con discapacidad se considerará:",
  ["Discriminación directa.", "Discriminación indirecta.", "Discriminación por asociación.", "Una infracción leve, sin carácter discriminatorio."], "Art. 6.1 a) Ley 15/2022.", "Se considerará discriminación directa la denegación de ajustes razonables a las personas con discapacidad")
q("L15_2022", "Artículo 40", "Igualdad de trato", "Según el artículo 40 b) de la Ley 15/2022, la mediación o la conciliación de la Autoridad Independiente para la Igualdad de Trato y la No Discriminación:",
  ["Sustituirá al recurso de alzada y, en su caso, al de reposición.", "Será previa y obligatoria a cualquier recurso judicial.", "Solo podrá iniciarse de oficio.", "Procederá también en asuntos de contenido penal o laboral."], "Art. 40 b) Ley 15/2022.", "sustituirá al recurso de alzada y, en su caso, al de reposición")
q("L15_2022", "Artículo 41", "Igualdad de trato", "Según el artículo 41.4 de la Ley 15/2022, el mandato de la persona titular de la presidencia de la Autoridad Independiente para la Igualdad de Trato y la No Discriminación será de:",
  ["Cinco años sin posibilidad de renovación.", "Cinco años renovables una sola vez.", "Seis años sin posibilidad de renovación.", "Cuatro años renovables una sola vez."], "Art. 41.4 Ley 15/2022.", "Su mandato será de cinco años sin posibilidad de renovación")
q("L15_2022", "Artículo 41", "Igualdad de trato", "Según el artículo 41.4 de la Ley 15/2022, la persona que ocupe la presidencia de la Autoridad Independiente para la Igualdad de Trato y la No Discriminación será nombrada:",
  ["Por el Gobierno mediante Real Decreto.", "Por el Congreso de los Diputados, por mayoría de tres quintos.", "Por la persona titular del Ministerio de Igualdad mediante orden.", "Por el Rey, a propuesta del Defensor del Pueblo."], "Art. 41.4 Ley 15/2022 (previa comparecencia ante las comisiones del Congreso y del Senado).", "que será nombrada por el Gobierno mediante Real Decreto")
q("L4_2023", "Artículo 9", "LGTBI", "Según el artículo 9 de la Ley 4/2023, el Consejo de Participación de las Personas LGTBI presentará una memoria detallando su actividad con carácter:",
  ["Semestral.", "Anual.", "Trimestral.", "Bienal."], "Art. 9.3 Ley 4/2023.", "El Consejo presentará una memoria con carácter semestral")
q("L4_2023", "Artículo 15", "LGTBI", "Según el artículo 15.1 de la Ley 4/2023, las empresas obligadas debían contar con el conjunto planificado de medidas y recursos para la igualdad de las personas LGTBI en el plazo de:",
  ["Doce meses a partir de la entrada en vigor de la ley.", "Seis meses a partir de la entrada en vigor de la ley.", "Dos años a partir de la publicación de la ley.", "Tres meses a partir de su desarrollo reglamentario."], "Art. 15.1 Ley 4/2023.", "en el plazo de doce meses a partir de la entrada en vigor de la presente ley")
q("L4_2023", "Artículo 43", "LGTBI", "Según el artículo 43 de la Ley 4/2023, podrá solicitar por sí misma ante el Registro Civil la rectificación de la mención registral relativa al sexo toda persona de nacionalidad española:",
  ["Mayor de dieciséis años.", "Mayor de dieciocho años.", "Mayor de catorce años.", "Mayor de doce años."], "Art. 43.1. Entre 14 y 16, asistida por sus representantes; entre 12 y 14, con autorización judicial.", "Toda persona de nacionalidad española mayor de dieciséis años podrá solicitar por sí misma")
q("L4_2023", "Artículo 44", "LGTBI", "Según el artículo 44.8 de la Ley 4/2023, la persona encargada del Registro Civil deberá citar a la persona legitimada para que ratifique su solicitud de rectificación registral en el plazo máximo de:",
  ["Tres meses desde la comparecencia inicial.", "Un mes desde la comparecencia inicial.", "Seis meses desde la presentación de la solicitud.", "Quince días desde la comparecencia inicial."], "Art. 44.8; después, resolución en un mes (44.9).", "En el plazo máximo de tres meses desde la comparecencia inicial")
q("CE", "Artículo 49", "Discapacidad", "Según el artículo 49.1 de la Constitución, las personas con discapacidad ejercen los derechos previstos en el Título I en condiciones de:",
  ["Libertad e igualdad reales y efectivas.", "Igualdad formal ante la ley.", "Protección especial y tutela pública.", "Integración y rehabilitación."], "Art. 49.1 CE.", "ejercen los derechos previstos en este Título en condiciones de libertad e igualdad reales y efectivas")
q("LGD", "a4", "Discapacidad", "Según el artículo 4.2 del texto refundido aprobado por el Real Decreto Legislativo 1/2013, tendrán la consideración de personas con discapacidad, a los efectos de la ley, aquellas a quienes se haya reconocido un grado de discapacidad:",
  ["Igual o superior al 33 por ciento.", "Superior al 33 por ciento.", "Igual o superior al 25 por ciento.", "Igual o superior al 65 por ciento."], "Art. 4.2 LGD.", "un grado de discapacidad igual o superior al 33 por ciento")
q("LGD", "a42", "Discapacidad", "Según el artículo 42.1 del texto refundido aprobado por el Real Decreto Legislativo 1/2013, las empresas públicas y privadas que empleen a 50 o más trabajadores vendrán obligadas a que, de entre ellos, sean trabajadores con discapacidad al menos:",
  ["El 2 por 100.", "El 5 por 100.", "El 7 por 100.", "El 3 por 100."], "Art. 42.1 LGD.", "al menos, el 2 por 100 sean trabajadores con discapacidad")
q("LGD", "a37", "Discapacidad", "Según el artículo 37.2 del texto refundido aprobado por el Real Decreto Legislativo 1/2013, el empleo en centros especiales de empleo y en enclaves laborales es:",
  ["Empleo protegido.", "Empleo ordinario.", "Empleo autónomo.", "Empleo con apoyo."], "Art. 37.2 b) LGD.", "Empleo protegido, en centros especiales de empleo y en enclaves laborales")
q("LGD", "a55", "Discapacidad", "Según el artículo 55 del texto refundido aprobado por el Real Decreto Legislativo 1/2013, el Consejo Nacional de la Discapacidad es un órgano colegiado:",
  ["Interministerial, de carácter consultivo.", "Interministerial, de carácter ejecutivo.", "Interadministrativo, de carácter decisorio.", "Técnico, adscrito a la Oficina de Atención a la Discapacidad."], "Art. 55 LGD. La Oficina de Atención a la Discapacidad es un órgano del Consejo (art. 56).", "es el órgano colegiado interministerial, de carácter consultivo")
q("L39_2006", "Artículo 5", "Dependencia", "Según el artículo 5.1 c) de la Ley 39/2006, para ser titular de los derechos de la ley es necesario residir en territorio español y haberlo hecho durante:",
  ["Cinco años, de los cuales dos deberán ser inmediatamente anteriores a la fecha de presentación de la solicitud.", "Diez años, de los cuales dos deberán ser inmediatamente anteriores a la solicitud.", "Cinco años, de los cuales uno deberá ser inmediatamente anterior a la solicitud.", "Tres años inmediatamente anteriores a la solicitud."], "Art. 5.1 c) Ley 39/2006.", "haberlo hecho durante cinco años, de los cuales dos deberán ser inmediatamente anteriores a la fecha de presentación de la solicitud")
q("L39_2006", "Artículo 8", "Dependencia", "Según el artículo 8.1 de la Ley 39/2006, en la composición del Consejo Territorial de Servicios Sociales y del Sistema para la Autonomía y Atención a la Dependencia tendrán mayoría:",
  ["Los representantes de las comunidades autónomas.", "Los representantes de la Administración General del Estado.", "Los representantes de las Entidades Locales.", "Las organizaciones del tercer sector."], "Art. 8.1 Ley 39/2006 (lo preside el titular del Ministerio).", "En la composición del Consejo Territorial tendrán mayoría los representantes de las comunidades autónomas")
q("L39_2006", "Artículo 14", "Dependencia", "Según el artículo 14 de la Ley 39/2006, la prioridad en el acceso a los servicios vendrá determinada por:",
  ["El grado de dependencia y, a igual grado, por la capacidad económica del solicitante.", "La capacidad económica y, a igual capacidad, por la edad del solicitante.", "El orden de presentación de las solicitudes.", "La edad y, a igual edad, por el grado de dependencia."], "Art. 14.6 Ley 39/2006.", "La prioridad en el acceso a los servicios vendrá determinada por el grado de dependencia y, a igual grado, por la capacidad económica del solicitante")
q("L39_2006", "Artículo 18", "Dependencia", "Según el artículo 18.1 de la Ley 39/2006, la prestación económica para cuidados en el entorno familiar se reconocerá:",
  ["Excepcionalmente, cuando el beneficiario esté siendo atendido por su entorno familiar y se reúnan las condiciones del artículo 14.4.", "Con carácter prioritario sobre los servicios del Catálogo.", "Únicamente a las personas con Grado III.", "Siempre que el cuidador sea un profesional acreditado."], "Art. 18.1 Ley 39/2006.", "Excepcionalmente, cuando el beneficiario esté siendo atendido por su entorno familiar")
q("L39_2006", "Artículo 26", "Dependencia", "Según el artículo 26.1 de la Ley 39/2006, la dependencia severa corresponde al:",
  ["Grado II, cuando la persona necesita ayuda para realizar varias actividades básicas de la vida diaria dos o tres veces al día.", "Grado I, cuando la persona necesita ayuda al menos una vez al día.", "Grado III, cuando la persona necesita ayuda varias veces al día.", "Grado II, cuando la persona necesita el apoyo indispensable y continuo de otra persona."], "Art. 26.1 b) Ley 39/2006.", "Grado II. Dependencia severa: cuando la persona necesita ayuda para realizar varias actividades básicas de la vida diaria dos o tres veces al día")
q("L39_2006", "Artículo 28", "Dependencia", "Según el artículo 28.2 de la Ley 39/2006, el reconocimiento de la situación de dependencia se efectuará mediante resolución expedida por:",
  ["La Administración Autonómica correspondiente a la residencia del solicitante.", "El Instituto de Mayores y Servicios Sociales.", "El Consejo Territorial de Servicios Sociales y del Sistema para la Autonomía y Atención a la Dependencia.", "La Entidad Local del domicilio del solicitante."], "Art. 28.2 Ley 39/2006; validez en todo el territorio del Estado.", "mediante resolución expedida por la Administración Autonómica correspondiente a la residencia del solicitante")
q("L39_2006", "Artículo 33", "Dependencia", "Según el artículo 33 de la Ley 39/2006, los beneficiarios de las prestaciones de dependencia participarán en su financiación:",
  ["Según el tipo y coste del servicio y su capacidad económica personal.", "En un porcentaje fijo del 10 % del coste del servicio.", "Solo en las prestaciones económicas.", "Nunca: las prestaciones son gratuitas."], "Art. 33.1; ningún ciudadano queda fuera por no disponer de recursos (33.4).", "según el tipo y coste del servicio y su capacidad económica personal")
T.real("L", 43, "LGTBI"); T.real("P", 42, "LGTBI"); T.real("X", 52, "LGTBI"); T.real("P", 41, "LGTBI")
T.real("X", 51, "Violencia de género"); T.real("X", 53, "Violencia de género"); T.real("L", 103, "Violencia de género")
T.real("L", 42, "Dependencia"); T.real("P", 43, "Dependencia")

# Flashcards
for q_, a_, cat in [
  ("¿Qué artículos de la CE desarrolla la LO 3/2007?", "Los arts. 9.2 y 14 (art. 1.1).", "LO 3/2007"),
  ("Discriminación indirecta por razón de sexo (LO 3/2007, art. 6.2)", "Disposición, criterio o práctica aparentemente neutros que pone a personas de un sexo en desventaja particular, salvo justificación objetiva por finalidad legítima con medios necesarios y adecuados.", "LO 3/2007"),
  ("Acoso sexual frente a acoso por razón de sexo (art. 7)", "Sexual: comportamiento de naturaleza sexual. Por razón de sexo: comportamiento realizado en función del sexo. Ambos, en todo caso discriminatorios.", "LO 3/2007"),
  ("Composición equilibrada (disp. adic. 1.ª LO 3/2007)", "Cada sexo: no más del 60 % ni menos del 40 %.", "LO 3/2007"),
  ("Plan de igualdad obligatorio en la empresa (art. 45)", "Empresas de 50 o más trabajadores; o si lo prevé el convenio; o si sustituye sanciones accesorias.", "LO 3/2007"),
  ("Plan de Igualdad en la AGE (art. 64)", "Lo aprueba el Gobierno al inicio de cada legislatura; lo evalúa anualmente el Consejo de Ministros.", "LO 3/2007"),
  ("Concepto de violencia de género (LO 1/2004, art. 1)", "La ejercida sobre las mujeres por quienes sean o hayan sido cónyuges o pareja, aun sin convivencia; incluye la ejercida sobre familiares o allegados menores para dañar a la mujer.", "Violencia de género"),
  ("¿Cómo se acredita la violencia de género? (art. 23)", "Sentencia condenatoria, orden de protección o resolución con medida cautelar, informe del Ministerio Fiscal o informe de los servicios sociales, especializados o de acogida.", "Violencia de género"),
  ("Rango de la Delegación del Gobierno contra la Violencia de Género", "Dirección general (RD 246/2024, art. 2.3).", "Violencia de género"),
  ("Pacto de Estado contra la Violencia de Género renovado en 2025", "Aprobado por el Pleno del Congreso el 26-2-2025; amplía las medidas de 290 a 461 (fuente oficial, no legal).", "Violencia de género"),
  ("Plan conjunto plurianual en materia de violencia contra las mujeres", "2023-2027; aprobado por la Conferencia Sectorial de Igualdad el 3-3-2023 (BOE-A-2023-7326).", "Violencia de género"),
  ("Discriminación múltiple e interseccional (Ley 15/2022, art. 6.3)", "Múltiple: dos o más causas, simultánea o consecutivamente. Interseccional: causas que concurren o interactúan y generan una forma específica.", "Igualdad de trato"),
  ("Autoridad Independiente para la Igualdad de Trato: presidencia", "Nombrada por el Gobierno por Real Decreto; el Congreso puede rechazarla por mayoría absoluta de la Comisión en un mes; mandato de cinco años no renovable.", "Igualdad de trato"),
  ("Acoso discriminatorio (Ley 4/2023, art. 3 d)", "Cualquier conducta por alguna de las causas de la ley que atente contra la dignidad y cree un entorno intimidatorio, hostil, degradante, humillante u ofensivo.", "LGTBI"),
  ("Empresas obligadas a medidas LGTBI (Ley 4/2023, art. 15)", "Las de más de cincuenta personas trabajadoras, con protocolo frente al acoso o la violencia (RD 1026/2024).", "LGTBI"),
  ("Rectificación registral del sexo: edades (art. 43)", "Más de 16: por sí; 14-16: asistidos; 12-14: autorización judicial.", "LGTBI"),
  ("¿Quién es persona con discapacidad a efectos de la LGD? (art. 4.2)", "Quien tenga reconocido un grado de discapacidad igual o superior al 33 %.", "Discapacidad"),
  ("Cuota de reserva en la empresa (LGD, art. 42)", "Al menos el 2 % en empresas de 50 o más trabajadores.", "Discapacidad"),
  ("Grados de dependencia (Ley 39/2006, art. 26)", "I moderada (una vez al día); II severa (dos o tres veces al día); III gran dependencia (varias veces al día, apoyo continuo).", "Dependencia"),
  ("Ayuda a domicilio: intensidad (RD 1051/2013, anexo II)", "Grado I: 20-37 h/mes; Grado II: 38-64; Grado III: 65-94.", "Dependencia"),
  ("Consejo Territorial del SAAD (art. 8)", "Preside el titular del Ministerio; mayoría de las comunidades autónomas; acuerda el baremo.", "Dependencia"),
]: T.fc(q_, a_, cat)

# Glosario
T.glos("Discriminación indirecta", "Disposición, criterio o práctica aparentemente neutros que sitúan a personas de un sexo (o con una causa protegida) en desventaja particular, salvo justificación objetiva (LO 3/2007, art. 6.2; Ley 15/2022, art. 6.1 b).", "s2", "Igualdad")
T.glos("Acción positiva", "Medida específica y temporal, razonable y proporcionada, para corregir desigualdades de hecho (LO 3/2007, art. 11; Ley 15/2022, art. 6.7).", "s2", "Igualdad")
T.glos("Transversalidad", "Integración del principio de igualdad en todas las políticas y actuaciones de los poderes públicos (LO 3/2007, art. 15).", "s3", "Igualdad")
T.glos("Plan de igualdad", "Conjunto ordenado de medidas, adoptadas tras un diagnóstico, para la igualdad en la empresa; obligatorio con 50 o más trabajadores (LO 3/2007, arts. 45 y 46).", "s4", "Igualdad")
T.glos("Composición equilibrada", "Presencia de mujeres y hombres en la que cada sexo no supera el 60 % ni baja del 40 % (LO 3/2007, disp. adic. 1.ª).", "s6", "Igualdad")
T.glos("Violencia de género", "Violencia ejercida sobre las mujeres por quienes sean o hayan sido sus cónyuges o parejas, aun sin convivencia (LO 1/2004, art. 1).", "s7", "Violencia de género")
T.glos("Discriminación interseccional", "La que se produce cuando concurren o interactúan varias causas generando una forma específica de discriminación (Ley 15/2022, art. 6.3 b).", "s11", "Igualdad de trato")
T.glos("Acoso discriminatorio", "Conducta por una causa de discriminación que atenta contra la dignidad y crea un entorno intimidatorio, hostil, degradante, humillante u ofensivo (Ley 4/2023, art. 3 d).", "s13", "LGTBI")
T.glos("Ajustes razonables", "Modificaciones y adaptaciones necesarias y adecuadas que no imponen una carga desproporcionada o indebida (LGD, art. 2 m); su denegación es discriminación directa (Ley 15/2022, art. 6.1).", "s17", "Discapacidad")
T.glos("Accesibilidad universal", "Condición de entornos, procesos, bienes y servicios para ser comprensibles, utilizables y practicables por todas las personas; incluye la accesibilidad cognitiva (LGD, art. 2 k).", "s17", "Discapacidad")
T.glos("Dependencia", "Estado permanente en que, por edad, enfermedad o discapacidad, se precisa atención de otra persona o ayudas importantes para las actividades básicas de la vida diaria (Ley 39/2006, art. 2.2).", "s20", "Dependencia")
T.glos("Programa Individual de Atención (PIA)", "Programa que determina las modalidades de intervención más adecuadas entre los servicios y prestaciones del grado reconocido (Ley 39/2006, art. 29).", "s23", "Dependencia")

# Cronología (fechas de los metadatos del BOE; el Pacto, de su publicación oficial)
T.hito("2004", "Ley Orgánica 1/2004, de 28 de diciembre, de Medidas de Protección Integral contra la Violencia de Género (BOE de 29-12-2004)", "Concepto de violencia de género, derechos de las víctimas, Delegación y Observatorio", "normativo", "s7")
T.hito("2006", "Ley 39/2006, de 14 de diciembre, de Promoción de la Autonomía Personal y Atención a las personas en situación de dependencia (BOE de 15-12-2006)", "Crea el Sistema para la Autonomía y Atención a la Dependencia", "normativo", "s20")
T.hito("2007", "Ley Orgánica 3/2007, de 22 de marzo, para la igualdad efectiva de mujeres y hombres (BOE de 23-3-2007)", "Conceptos, planes de igualdad, composición equilibrada 60/40", "normativo", "s2")
T.hito("2013", "Real Decreto Legislativo 1/2013, de 29 de noviembre, texto refundido de la Ley General de derechos de las personas con discapacidad (BOE de 3-12-2013)", "Definiciones, 33 %, cuota de reserva del 2 %", "normativo", "s17")
T.hito("2022", "Ley 15/2022, de 12 de julio, integral para la igualdad de trato y la no discriminación (BOE de 13-7-2022)", "Ley general antidiscriminación; Autoridad Independiente", "normativo", "s11")
T.hito("2023", "Ley 4/2023, de 28 de febrero, para la igualdad real y efectiva de las personas trans y para la garantía de los derechos de las personas LGTBI (BOE de 1-3-2023)", "Definiciones, medidas en empresas de más de cincuenta trabajadores, rectificación registral", "normativo", "s13")
T.hito("2023", "Plan conjunto plurianual en materia de violencia contra las mujeres 2023-2027 (Conferencia Sectorial de Igualdad, 3-3-2023; BOE de 20-3-2023)", "Catálogo de referencia y sistema común de información y evaluación", "institucional", "s10")
T.hito("2024", "Real Decreto 246/2024, de 8 de marzo, estructura del Ministerio de Igualdad (BOE de 9-3-2024)", "Delegación del Gobierno contra la Violencia de Género con rango de dirección general", "normativo", "s9")
T.hito("2025", "Renovación del Pacto de Estado contra la Violencia de Género por el Pleno del Congreso (26-2-2025)", "De 290 a 461 medidas (publicación oficial de la Delegación del Gobierno)", "institucional", "s10")

T.publicar()
