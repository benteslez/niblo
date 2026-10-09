# -*- coding: utf-8 -*-
# Tema I.2 (v4) · Parte 3: bloque I, Sección 2.ª, Capítulo tercero y deberes.
from v4_util import *

ap("s4", "I.8 Sección 2.ª (I): defensa, tributos, matrimonio, propiedad y fundación (arts. 30 a 34)", f"""
La Sección 2.ª, «De los derechos y deberes de los ciudadanos», tiene **protección intermedia** (→ II.1): vinculación de todos los poderes públicos, reserva de ley con contenido esencial y recurso de inconstitucionalidad, pero **sin** procedimiento preferente y sumario, **sin** amparo (salvo la objeción de conciencia) y **sin** reforma agravada. También es donde la Constitución concentra los **deberes** (→ I.12).

{unidad("8.1 Defensa de España y objeción de conciencia (art. 30)",
  lit("CE", 30, ["el derecho y el deber de defender a España", "la objeción de conciencia", "prestación social sustitutoria", "servicio civil", "grave riesgo, catástrofe o calamidad pública"]),
  ficha(f"{c('CE', 30, 'Los españoles')} (30.1); los ciudadanos (30.4)",
        ["30.1, **derecho y deber** de defender a España", "30.2, la ley fija las obligaciones militares y regula la objeción de conciencia y las exenciones del servicio militar obligatorio; puede imponer una prestación social sustitutoria", "30.3, puede establecerse un servicio civil para fines de interés general", "30.4, la ley puede regular deberes en casos de grave riesgo, catástrofe o calamidad pública"],
        "La objeción de conciencia, «con las debidas garantías» que fije la ley",
        [f"::{P_S2}", "**Excepción:** la objeción de conciencia tiene **amparo** (arts. 53.2 CE y 41.1 LOTC → II.5)", NO_SUSP],
        "La objeción de conciencia es el **único** derecho de la Sección 2.ª con amparo. «Podrá establecerse» un servicio civil: no es obligatorio."))}

{unidad("8.2 Sistema tributario y gasto público (art. 31)",
  lit("CE", 31, ["capacidad económica", "igualdad y progresividad", "en ningún caso, tendrá alcance confiscatorio", "eficiencia y economía", "con arreglo a la ley"]),
  ficha(f"{c('CE', 31, 'Todos')}",
        ["31.1, **deber** de contribuir según la capacidad económica, con un sistema tributario justo", "31.2, gasto público: asignación equitativa de los recursos", "31.3, reserva de ley para las prestaciones personales o patrimoniales de carácter público"],
        ["Sistema tributario (31.1): igualdad, progresividad y **no confiscatoriedad**", "Gasto (31.2): **eficiencia y economía**"],
        [f"::{P_S2}", NO_SUSP],
        f"No mezclar los principios del **tributo** (igualdad, progresividad, no confiscatorio) con los criterios del **gasto** (eficiencia y economía). Literal: {c('CE', 31, 'en ningún caso, tendrá alcance confiscatorio')}."))}

{unidad("8.3 Matrimonio (art. 32)",
  lit("CE", 32, ["con plena igualdad jurídica"]),
  ficha(f"{c('CE', 32, 'El hombre y la mujer')}",
        "Derecho a contraer matrimonio con plena igualdad jurídica",
        "La ley regula las formas, la edad y capacidad, los derechos y deberes de los cónyuges y las causas de separación y disolución",
        [f"::{P_S2}", NO_SUSP],
        "«con **plena** igualdad jurídica»."))}

{unidad("8.4 Propiedad privada y herencia (art. 33)",
  lit("CE", 33, ["función social", "utilidad pública o interés social", "correspondiente indemnización"]),
  ficha("No se nombra titular («Se reconoce el derecho a la propiedad privada y a la herencia»)",
        ["33.1, propiedad privada y herencia", "33.3, garantía expropiatoria: base de la **expropiación forzosa** (tema IV.8)"],
        ["33.2, la **función social** delimita su contenido", "33.3, privación solo por **causa justificada de utilidad pública o interés social**, con **indemnización** y conforme a las leyes"],
        [f"::{P_S2}", NO_SUSP],
        "Tres requisitos de la expropiación: causa (utilidad pública o interés social), indemnización y conformidad con las leyes."))}

{unidad("8.5 Fundación (art. 34)",
  lit("CE", 34, ["para fines de interés general", "apartados 2 y 4 del artículo 22"]),
  ficha("No se nombra titular",
        "Derecho de fundación para fines de **interés general**, con arreglo a la ley",
        "Se le aplican los apartados **2 y 4** del art. 22: ilegales si sus fines o medios son delito; disolución o suspensión solo por resolución judicial motivada (→ I.5.3)",
        [f"::{P_S2}", NO_SUSP],
        "Apartados «**2 y 4**» del art. 22, no el 3 (la inscripción registral)."))}
""", 2)

# ---------------------------------------------------------------------------
ap("s4-1", "I.9 Sección 2.ª (II): trabajo, colegios, negociación colectiva y empresa (arts. 35 a 38)", f"""
Segunda parte de la Sección 2.ª: los derechos del **ámbito económico y laboral**. Misma protección intermedia (→ II.1).

{unidad("9.1 Trabajo (art. 35)",
  lit("CE", 35, ["el deber de trabajar y el derecho al trabajo", "remuneración suficiente", "por razón de sexo", "estatuto de los trabajadores"]),
  ficha(f"{c('CE', 35, 'Todos los españoles')}",
        ["35.1, **deber** de trabajar y **derecho** al trabajo; libre elección de profesión u oficio; promoción a través del trabajo; remuneración suficiente para el trabajador y su familia", "35.2, la ley regulará un **estatuto de los trabajadores**"],
        "Sin discriminación por razón de sexo",
        [f"::{P_S2}", NO_SUSP],
        f"Remuneración {c('CE', 35, 'suficiente para satisfacer sus necesidades y las de su familia')}. Discriminación expresamente prohibida: {c('CE', 35, 'por razón de sexo')}."))}

{unidad("9.2 Colegios profesionales (art. 36)",
  lit("CE", 36, ["deberán ser democráticos"]),
  fichab("Reserva de ley para el régimen de los colegios profesionales y el ejercicio de las profesiones tituladas",
         "El legislador; los colegios",
         "Estructura interna y funcionamiento **democráticos**",
         "—",
         "Exigen estructura democrática: colegios (36), organizaciones profesionales (52) y, fuera del Título I, partidos (6) y sindicatos y asociaciones empresariales (7)."))}

{unidad("9.3 Negociación colectiva y conflicto colectivo (art. 37)",
  lit("CE", 37, ["fuerza vinculante de los convenios", "trabajadores y empresarios a adoptar medidas de conflicto colectivo"]),
  ficha("Los representantes de los trabajadores y empresarios (37.1); los **trabajadores y empresarios** (37.2)",
        ["37.1, negociación colectiva laboral y fuerza vinculante de los convenios", "37.2, medidas de conflicto colectivo"],
        f"La ley incluirá garantías para {c('CE', 37, 'asegurar el funcionamiento de los servicios esenciales de la comunidad')}",
        [f"::{P_S2}", "Suspendible: **sí, el 37.2**, en excepción y sitio (55.1 → III.2): es el **único** de la Sección 2.ª"],
        "Huelga (28.2): de los «trabajadores». Conflicto colectivo (37.2): de «trabajadores **y empresarios**»."))}

{unidad("9.4 Libertad de empresa (art. 38)",
  lit("CE", 38, ["en el marco de la economía de mercado", "la planificación"]),
  ficha("No se nombra titular («Se reconoce la libertad de empresa»)",
        "Libertad de empresa **en el marco de la economía de mercado**; los poderes públicos garantizan y protegen su ejercicio y la defensa de la productividad",
        "Las exigencias de la economía general y, en su caso, la **planificación**",
        [f"::{P_S2}", NO_SUSP],
        "«economía de **mercado**»; el límite puede ser «en su caso, de la planificación»."))}
""", 2)

# ---------------------------------------------------------------------------
ap("s4-2", "I.10 Capítulo tercero (I): naturaleza y arts. 39 a 45", f"""
### 10.1 Naturaleza de los principios rectores

El Capítulo tercero, «De los principios rectores de la política social y económica», no reconoce, en general, derechos exigibles directamente ante un juez, sino **mandatos** que orientan el Estado social ({c("CE", 1, "Estado social y democrático de Derecho")}, art. 1.1). Su eficacia la fija el art. 53.3 (→ II.1):
- {c("CE", 53, "informarán la legislación positiva, la práctica judicial y la actuación de los poderes públicos")};
- {c("CE", 53, "Sólo podrán ser alegados ante la Jurisdicción ordinaria de acuerdo con lo que dispongan las leyes que los desarrollen")}.

En sus fichas, «Titulares» indica a **quién beneficia** el principio; los obligados son siempre los poderes públicos. Ninguno puede suspenderse.

{unidad("10.2 Familia e infancia (art. 39)",
  lit("CE", 39, ["con independencia de su filiación", "investigación de la paternidad", "asistencia de todo orden", "acuerdos internacionales"]),
  ficha("La familia, los hijos, las madres y los niños",
        ["39.1, protección social, económica y jurídica de la **familia**", "39.2, protección integral de los **hijos**, iguales con independencia de su filiación, y de las **madres**, cualquiera que sea su estado civil; investigación de la paternidad", "39.3, **deber** de los padres de prestar asistencia de todo orden a los hijos, dentro o fuera del matrimonio", "39.4, los niños gozan de la protección de los **acuerdos internacionales**"],
        "—",
        P_C3,
        f"{c('CE', 39, 'La ley posibilitará la investigación de la paternidad')}. Madres {c('CE', 39, 'cualquiera que sea su estado civil')}."))}

{unidad("10.3 Política económica y laboral (art. 40)",
  lit("CE", 40, ["política orientada al pleno empleo", "vacaciones periódicas retribuidas"]),
  ficha("Los trabajadores y el conjunto de la sociedad",
        ["40.1, progreso social y económico y distribución más equitativa de la renta, en el marco de la estabilidad económica; política orientada al **pleno empleo**", "40.2, formación y readaptación profesionales; seguridad e higiene en el trabajo; descanso, limitación de la jornada, **vacaciones periódicas retribuidas** y centros adecuados"],
        "—",
        P_C3,
        f"{c('CE', 40, 'De manera especial realizarán una política orientada al pleno empleo')}."))}

{unidad("10.4 Seguridad Social (art. 41)",
  lit("CE", 41, ["régimen público de Seguridad Social para todos los ciudadanos", "especialmente en caso de desempleo", "serán libres"]),
  ficha("Todos los ciudadanos",
        "Régimen **público** de Seguridad Social, con asistencia y prestaciones suficientes ante situaciones de necesidad, especialmente el desempleo",
        "—",
        P_C3,
        f"{c('CE', 41, 'La asistencia y prestaciones complementarias serán libres')}."))}

{unidad("10.5 Trabajadores en el extranjero (art. 42)",
  lit("CE", 42, ["orientará su política hacia su retorno"]),
  ficha("Los trabajadores españoles en el extranjero",
        "El Estado vela por sus derechos económicos y sociales",
        "—",
        P_C3,
        "Lo encomienda al **Estado** y orienta su política hacia el **retorno**."))}

{unidad("10.6 Salud (art. 43)",
  lit("CE", 43, ["derecho a la protección de la salud", "adecuada utilización del ocio"]),
  ficha("No se nombra titular («Se reconoce el derecho a la protección de la salud»)",
        ["43.1, protección de la salud", "43.2, salud pública: medidas preventivas y prestaciones y servicios; la ley fija derechos y deberes", "43.3, educación sanitaria, educación física y deporte; adecuada utilización del ocio"],
        "—",
        P_C3,
        "«adecuada utilización del **ocio**» está en el art. 43.3."))}

{unidad("10.7 Cultura y ciencia (art. 44)",
  lit("CE", 44, ["a la que todos tienen derecho"]),
  ficha(f"{c('CE', 44, 'todos')}",
        ["44.1, acceso a la cultura", "44.2, promoción de la ciencia y la investigación científica y técnica"],
        "—",
        P_C3,
        f"La ciencia, {c('CE', 44, 'en beneficio del interés general')}."))}

{unidad("10.8 Medio ambiente (art. 45)",
  lit("CE", 45, ["así como el deber de conservarlo", "sanciones penales o, en su caso, administrativas", "obligación de reparar el daño causado"]),
  ficha(f"{c('CE', 45, 'Todos')}",
        ["45.1, **derecho** a un medio ambiente adecuado y **deber** de conservarlo", f"45.2, utilización racional de los recursos naturales, con {c('CE', 45, 'la indispensable solidaridad colectiva')}", "45.3, sanciones y obligación de reparar el daño"],
        "—",
        P_C3,
        "Sanciones «penales **o, en su caso,** administrativas» y obligación de **reparar** el daño."))}
""", 2)

# ---------------------------------------------------------------------------
ap("s4-4", "I.11 Capítulo tercero (II): arts. 46 a 52", f"""
Segunda parte del Capítulo tercero: patrimonio, vivienda, juventud y colectivos con protección específica. Misma eficacia del art. 53.3 (→ I.10.1).

{unidad("11.1 Patrimonio histórico, cultural y artístico (art. 46)",
  lit("CE", 46, ["La ley penal sancionará"]),
  ficha("Los pueblos de España",
        f"Conservación y enriquecimiento del patrimonio, {c('CE', 46, 'cualquiera que sea su régimen jurídico y su titularidad')}",
        "—",
        P_C3,
        "Protección **penal** expresa: «La ley penal sancionará los atentados contra este patrimonio»."))}

{unidad("11.2 Vivienda (art. 47)",
  lit("CE", 47, ["vivienda digna y adecuada", "impedir la especulación", "plusvalías"]),
  ficha(f"{c('CE', 47, 'Todos los españoles')}",
        ["Vivienda **digna y adecuada**", "Regulación del suelo según el interés general para impedir la **especulación**", "Participación de la comunidad en las **plusvalías** de la acción urbanística pública"],
        "—",
        P_C3,
        "Titulares: «Todos los **españoles**». Las plusvalías: las que genere la acción urbanística **de los entes públicos**."))}

{unidad("11.3 Juventud (art. 48)",
  lit("CE", 48, ["libre y eficaz"]),
  ficha("La juventud",
        "Participación **libre y eficaz** en el desarrollo político, social, económico y cultural",
        "—",
        P_C3,
        "«libre **y eficaz**»."))}

{unidad("11.4 Personas con discapacidad (art. 49)",
  lit("CE", 49, ["libertad e igualdad reales y efectivas", "entornos universalmente accesibles", "las mujeres y los menores con discapacidad"]),
  ficha("Las personas con discapacidad",
        ["49.1, ejercen los derechos del Título I en condiciones de libertad e igualdad reales y efectivas", "49.2, políticas de plena autonomía personal e inclusión social, en entornos universalmente accesibles; participación de sus organizaciones; atención a las necesidades específicas de mujeres y menores con discapacidad"],
        "—",
        P_C3,
        "Redacción de la **reforma constitucional de 2024** (Reforma del artículo 49 de la Constitución Española, de 15 de febrero de 2024, BOE-A-2024-3099 [[BOE]]; dato, no texto legal: la redacción anterior hablaba de los disminuidos físicos, sensoriales y psíquicos)."))}

{unidad("11.5 Tercera edad (art. 50)",
  lit("CE", 50, ["pensiones adecuadas y periódicamente actualizadas", "con independencia de las obligaciones familiares"]),
  ficha("Los ciudadanos durante la tercera edad",
        ["Suficiencia económica mediante pensiones **adecuadas y periódicamente actualizadas**", "Servicios sociales para salud, vivienda, cultura y ocio, **con independencia de las obligaciones familiares**"],
        "—",
        P_C3,
        "Pensiones «adecuadas **y periódicamente actualizadas**»."))}

{unidad("11.6 Consumidores y usuarios (art. 51)",
  lit("CE", 51, ["la seguridad, la salud y los legítimos intereses económicos", "comercio interior"]),
  ficha("Los consumidores y usuarios",
        ["51.1, defensa de su seguridad, salud y legítimos intereses económicos", "51.2, información, educación y fomento de sus organizaciones", "51.3, la ley regula el **comercio interior** y la autorización de productos comerciales"],
        "—",
        P_C3,
        "El **comercio interior** aparece en este artículo (51.3)."))}

{unidad("11.7 Organizaciones profesionales (art. 52)",
  lit("CE", 52, ["deberán ser democráticos"]),
  ficha("Las organizaciones profesionales",
        "Contribuyen a la defensa de los intereses económicos que les sean propios",
        f"{c('CE', 52, 'Su estructura interna y funcionamiento deberán ser democráticos')}",
        P_C3,
        "No confundir con los **colegios profesionales** (art. 36, Sección 2.ª). Los dos exigen estructura democrática."))}
""", 2)

# ---------------------------------------------------------------------------
ap("s4-3", "I.12 Los deberes constitucionales (visión de conjunto)", f"""
El epígrafe dice «Derechos **y deberes** fundamentales». Los deberes no tienen capítulo propio: están repartidos por el Título I. Estos son los que la Constitución formula expresamente:

| Art. | Deber | Texto literal |
|---|---|---|
| 27.4 | Escolarización básica | {c("CE", 27, "La enseñanza básica es obligatoria y gratuita.")} |
| 30.1 | Defensa de España | {c("CE", 30, "Los españoles tienen el derecho y el deber de defender a España.")} |
| 30.4 | Deberes ante grave riesgo, catástrofe o calamidad | {c("CE", 30, "Mediante ley podrán regularse los deberes de los ciudadanos en los casos de grave riesgo, catástrofe o calamidad pública.")} |
| 31.1 | Contribuir a los gastos públicos | {c("CE", 31, "Todos contribuirán al sostenimiento de los gastos públicos de acuerdo con su capacidad económica")} |
| 35.1 | Trabajar | {c("CE", 35, "Todos los españoles tienen el deber de trabajar y el derecho al trabajo")} |
| 39.3 | Asistencia de los padres a los hijos | {c("CE", 39, "Los padres deben prestar asistencia de todo orden a los hijos habidos dentro o fuera del matrimonio")} |
| 45.1 | Conservar el medio ambiente | {c("CE", 45, "un medio ambiente adecuado para el desarrollo de la persona, así como el deber de conservarlo.")} |

Fuera del Título I: el deber de conocer el castellano (art. 3.1) y la sujeción a la Constitución (art. 9.1): {c("CE", 9, "Los ciudadanos y los poderes públicos están sujetos a la Constitución y al resto del ordenamiento jurídico")}.

!> **Idea clave.** Tres deberes van unidos a un derecho: defender a España (30.1), trabajar (35.1) y el medio ambiente (45.1).

{resumen(["El Título I (arts. 10-55) ordena los derechos en **tres niveles**: art. 14 y Sección 1.ª (máximo), Sección 2.ª (intermedio) y Capítulo tercero (mínimo).",
          "La titularidad cambia según el artículo: «todos», «toda persona», «los españoles», «los ciudadanos»… Es un clásico del examen.",
          "Solo pueden suspenderse los que enumera el art. 55.1 (17, 18.2, 18.3, 19, 20.1 a y d, 20.5, 21, 28.2 y 37.2); todos de la Sección 1.ª salvo el 37.2.",
          "Los deberes están repartidos: 27.4, 30, 31, 35, 39.3 y 45."],
         "Siguiente: bloque II. Ya sabes qué derechos hay y en qué nivel está cada uno; ahora, cómo se protege cada nivel.")}
""", 2)
