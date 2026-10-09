# -*- coding: utf-8 -*-
"""Anotaciones del módulo M103 «Artículos CE · Lectura y explicación» (PDF subrayado + vídeo, aportados por el usuario)
sobre los artículos 1 a 52 de la Constitución. NO es texto de la CE: son marcas y comentarios de la academia.

Código de colores del documento (según el vídeo):
  naranja (exam)  artículo que ha sido objeto de pregunta en algún examen oficial del INAP
  rojo      (am)  cuestiones importantes (el documento las subraya en amarillo; en la app van en rojo) (preguntadas o susceptibles de serlo)
  verde     (vd)  «coletillas»: con qué se regula, desarrolla o limita un derecho (ley, tratado, resolución judicial…)
  naranja   (az)  artículos (el documento los subraya en azul; en la app van en naranja) que aparecen en el cuadro de suspensión (art. 55 + art. 116: excepción y sitio)
  rosa      (lo)  materia que expresamente se regula por ley orgánica (art. 8)

Cada frase de `marks` tiene que ser LITERAL del texto del artículo (la comprueba ce_datos.py).
Las marcas naranjas no vienen subrayadas en todos los artículos del PDF: se completan con el art. 55.1 CE (prevalece la norma).
"""
M103 = {
 1: dict(exam=True, marks=[("valores superiores de su ordenamiento jurídico", "am"), ("Monarquía parlamentaria", "am")],
         nota="Preguntaron por los **valores superiores del ordenamiento jurídico**: son **cuatro** (libertad, justicia, igualdad y pluralismo político). No los confundas con los **fundamentos del orden político y de la paz social** del art. 10, que también son cuatro."),
 2: dict(marks=[("solidaridad", "am")],
         nota="Una palabra clave puede sustituirse por otra para liarte (p. ej. «reciprocidad», como se ha hecho en otros artículos): aquí es **solidaridad** entre las nacionalidades y regiones."),
 3: dict(marks=[("deber de conocerla y el derecho a usarla", "am")],
         nota="Coletilla clásica: el castellano **se debe conocer y se puede usar**. Pueden invertirla («derecho a conocerla y deber de usarla»)."),
 5: dict(nota="La capital es Madrid. Truco: el 5 es la mitad del 10."),
 6: dict(marks=[("dentro del respeto a la Constitución y a la ley", "vd")],
         nota="Estudia el 6 y el 7 **juntos**: solo cambia la primera frase (partidos políticos / sindicatos y asociaciones empresariales). Pregunta fácil: «dentro del respeto a la **Constitución y a la ley**» (no a otra cosa)."),
 7: dict(marks=[("dentro del respeto a la Constitución y a la ley", "vd")],
         nota="Igual que el art. 6 salvo la primera frase: sindicatos de trabajadores y asociaciones empresariales."),
 8: dict(exam=True, marks=[("misión", "am"), ("ley orgánica", "lo")],
         nota="Preguntaron la **misión de las Fuerzas Armadas** (dos cosas: garantizar la soberanía e independencia de España y defender su integridad territorial y el ordenamiento constitucional). Es la **única materia de estos artículos que se regula expresamente por ley orgánica** (además de las del art. 81 y las demás previstas en la Constitución)."),
 9: dict(marks=[("garantiza el principio de legalidad", "am")],
         nota="Lista de **siete principios** del 9.3: te pueden preguntar «cuál no pertenece» e intercalar uno ajeno."),
 10: dict(exam=True, marks=[("fundamento del orden político y de la paz social", "am")],
          nota="Preguntaron los **fundamentos del orden político y de la paz social**: dignidad de la persona, derechos inviolables, libre desarrollo de la personalidad y respeto a la ley y a los derechos de los demás. No los mezcles con los valores del art. 1.1."),
 11: dict(exam=True, marks=[("por la ley", "vd")],
          nota="Coletilla preguntada: la nacionalidad se adquiere, se conserva y se pierde **por la ley**. Fíjate qué fácil sería sustituirla por «la Constitución», «una norma europea» o «un tratado» (los tratados aparecen mucho en este capítulo)."),
 12: dict(nota="Mayoría de edad: **18 años**."),
 13: dict(exam=True, marks=[("los tratados y la ley", "vd"), ("criterios de reciprocidad", "am"), ("un tratado o de la ley", "vd"), ("La ley establecerá los términos", "vd")],
          nota="Este artículo menciona **tratado y ley** varias veces: ojo a las sustituciones («tratados» por «normas», «ley» por «reglamento»)."),
 14: dict(nota="Es muy difícil que se pregunte en detalle; su importancia está en el cuadro de garantías (→ tema I.2)."),
 17: dict(exam=True, marks=[("Toda persona detenida debe ser informada de forma inmediata, y de modo que le sea comprensible, de sus derechos y de las razones de su detención, no pudiendo ser obligada a declarar.", "am")],
          lim="Se puede suspender en **excepción y sitio**; en la **excepción** no se suspende el **17.3** (derechos del detenido).",
          nota="Preguntaron cuál de cuatro oraciones era correcta (el 17.3 es el de los derechos del detenido)."),
 18: dict(exam=True, marks=[("sin consentimiento del titular o resolución judicial, salvo en caso de flagrante delito", "vd"), ("salvo resolución judicial", "vd"), ("La ley limitará el uso de la informática para garantizar el honor y la intimidad personal y familiar de los ciudadanos y el pleno ejercicio de sus derechos", "am")],
          lim="Se pueden suspender el **18.2** (domicilio) y el **18.3** (comunicaciones) en excepción y sitio.",
          nota="Preguntaron el **18.4** (la informática: lo desarrollan el RGPD y la LO 3/2018, LOPDGDD). Coletillas fáciles: para entrar o registrar el domicilio hace falta el **consentimiento del titular** o **resolución judicial** (no administrativa), salvo **flagrante delito** (18.2)."),
 19: dict(lim="Se puede limitar en excepción y sitio.", nota="La libertad de residencia y circulación."),
 20: dict(exam=True, marks=[("en virtud de resolución judicial", "vd")],
          lim="Se pueden suspender el **20.1.a)** y **d)** y el **20.5**.",
          nota="Hay que saber **qué letras** son las limitables (dentro del apartado 1 las letras **a)** y **d)**, y el apartado **5**). Coletilla: el secuestro de publicaciones, solo **en virtud de resolución judicial** (no administrativa)."),
 21: dict(lim="Se puede limitar en excepción y sitio."),
 22: dict(exam=True, marks=[("ilegales", "am"), ("registro a los solos efectos de publicidad", "am"), ("resolución judicial motivada", "vd"), ("Se prohíben", "am")],
          nota="**Campo de minas** (muchas trampas): son **ilegales** las asociaciones que persiguen fines o utilizan medios tipificados como delito; en cambio **se prohíben** las **secretas** y las de carácter **paramilitar**. La inscripción en el registro es «a los solos efectos de **publicidad**» (no de constitución) y solo se disuelven o suspenden por **resolución judicial motivada**."),
 25: dict(exam=True, marks=[("El condenado a pena de prisión", "am"), ("beneficios correspondientes de la Seguridad Social", "am")],
          nota="Preguntaron algo que casi nadie conoce: quiénes tienen derecho a los **beneficios de la Seguridad Social**: **los condenados a pena de prisión** (25.2)."),
 27: dict(exam=True, marks=[("derecho a la educación", "am"), ("libertad de enseñanza", "am"), ("principios democráticos", "am"), ("libertad de creación de centros docentes", "am"), ("Los poderes públicos inspeccionarán y homologarán el sistema educativo para garantizar el cumplimiento de las leyes", "am"), ("la autonomía de las Universidades", "am")],
          nota="Uno de los **artículos más largos**: léelo con calma. Lo subrayado son los puntos que más fácilmente se pueden manipular."),
 28: dict(lim="Solo se puede limitar el **28.2** (derecho de **huelga**), no la libertad sindical (28.1).", nota="Se limita únicamente el segundo apartado."),
 30: dict(marks=[("derecho y el deber de defender a España", "am")],
          nota="Coletilla para liarte: los españoles tienen **el derecho y el deber** de defender a España. Menos preguntable que los anteriores (sección 2.ª)."),
 31: dict(marks=[("principios de igualdad y progresividad", "am")],
          nota="El sistema tributario: **igualdad y progresividad**. En la Constitución aparecen muy pocos «principios»: hazte una lista con todos los que vayas encontrando."),
 33: dict(nota="Conviene «desmenuzarlo»: propiedad privada y herencia, su función social y la expropiación."),
 34: dict(exam=True, marks=[("interés general, con arreglo a la ley", "vd")],
          nota="Única pregunta de la sección 2.ª: la coletilla «**con arreglo a la ley**»."),
 37: dict(lim="Solo se puede limitar el **37.2** (conflicto colectivo) en excepción y sitio."),
 39: dict(nota="Principios rectores (capítulo III): prácticamente no se pregunta (solo el art. 41)."),
 40: dict(nota="Estudia el **40, 41 y 42 juntos**: son los principios del derecho del trabajo y de la seguridad social, según la doctrina."),
 41: dict(exam=True, marks=[("especialmente en caso de desempleo", "am")],
          nota="Única pregunta del capítulo III: las **situaciones de necesidad** cubiertas por el régimen público de Seguridad Social, «especialmente en caso de **desempleo**» (te pueden poner otras situaciones)."),
 42: dict(nota="Estudia el 40, 41 y 42 juntos."),
 43: dict(marks=[("Se reconoce el derecho a la protección de la salud", "am")],
          nota="**Ojo:** el derecho a la **protección de la salud** (art. 43) es un **principio rector** de la política social y económica, **no un derecho fundamental**."),
 47: dict(marks=[("derecho a disfrutar de una vivienda digna y adecuada", "am")],
          nota="**Ojo:** igual que la salud, la vivienda es un **principio rector**, **no un derecho fundamental**."),
}

LEYENDA = [
 ("exam", "Preguntado en examen oficial", "Artículo que ha sido objeto de pregunta en algún examen oficial del INAP (recorrido hecho por la academia)."),
 ("am", "Importante", "Cuestión importante, por haber sido preguntada o por poder serlo."),
 ("vd", "Coletilla", "Con qué se regula, desarrolla o limita un derecho (ley, tratado, resolución judicial…): pregunta muy fácil de examen."),
 ("az", "Se limita en excepción y sitio", "Aparece en el cuadro de suspensión de derechos (art. 55 junto con el art. 116)."),
 ("lo", "Ley orgánica", "Materia que expresamente se regula por ley orgánica (art. 8, además de las del art. 81)."),
]
NIVELES = [
 "**Nivel 1 · Estructura.** Título, capítulo y sección de cada artículo: de ahí depende qué garantías tiene.",
 "**Nivel 2 · Contenido.** Asociar cada artículo con su materia («el 3 es la lengua, el 8 las Fuerzas Armadas, el 33 la propiedad y la herencia»).",
 "**Nivel 3 · Lectura profunda** (último nivel; pocas preguntas): esta lectura, para detectar los puntos calientes.",
 "**Dónde se pregunta más:** la mayoría de las preguntas oficiales se concentran **hasta el art. 29**; de la sección 2.ª solo hay una (art. 34) y del capítulo III solo una (art. 41). ⚠ Es la valoración de la academia: los exámenes aportados ya tienen más (art. 30.2 en GACE-P 2025, pregunta 44, y art. 49 en GACE-P 2024, pregunta 48).",
]


# ----------------------------------------------------------------------------------------------------------------------
# Módulo M107 «Contenido de repaso sobre la CE» (PDF + vídeo): reglas para memorizar la estructura y ubicar el contenido.
# Notas por unidad (clave de CE_UNI: P, I, I.1, I.2, I.2.1, I.2.2, I.3, I.4, I.5, II…X) y por artículo. No son texto de la CE.
M107_UNIDADES = {
 "preambulo": "Léelo: ha habido preguntas que aludían al Preámbulo (por ejemplo, quién ratifica la Constitución). Basta con estar familiarizado con el texto.",
 "P": "**Los nueve artículos, con ganchos de memoria:** **1** España y la forma del Estado · **2** unidad y autonomía · **3** las lenguas (las «lenguas de fuego» del Espíritu Santo: el 3) · **4** la bandera · **5** la capital (la que está en el centro) · **6** partidos políticos · **7** sindicatos y asociaciones empresariales · **8** Fuerzas Armadas · **9** jerarquía normativa, legalidad y libertad e igualdad efectivas.",
 "I": "**El título más importante.** Dos artículos «colgantes» que quedan fuera de la estructura posterior: el **10** (fuera de los capítulos) y el **14** (dentro del capítulo II, fuera de las secciones). Acaba en el **55**: la «rima del cinco».",
 "I.1": "Capítulo de «calentamiento»: **11** nacionalidad, **12** mayoría de edad y **13** derechos de los extranjeros. Poco importantes, pero **muy tramposos**: no olvides que existe.",
 "I.2": "Capítulo II (14 a 38): el 14 «colgante» y dos secciones. **Trampas típicas del amparo:** la propiedad privada (33) y el derecho al trabajo (35) **no** tienen amparo, y el conflicto colectivo (37.2) tampoco; la libertad sindical y la huelga (28) **sí**.",
 "I.2.1": "**Sección 1.ª (15 a 29), la más importante:** ley orgánica, tutela preferente y sumaria (también el 14), amparo (también el 14 y el 30.2), vinculan a los poderes públicos, recurso de inconstitucionalidad y reserva de ley. Domina la redacción de los arts. **17, 18 y 20**.",
 "I.2.2": "**Sección 2.ª (30 a 38):** derechos y deberes de los ciudadanos. Vinculan, reserva de ley e inconstitucionalidad; **amparo solo el 30.2** (objeción de conciencia). Se pregunta menos que la sección 1.ª.",
 "I.3": "**Capítulo III (39 a 52), por descarte:** lo que queda tras el art. 38 y antes de los «protectores» (53 y 54). Son **principios** y no derechos: sin aplicabilidad inmediata, solo alegables según las leyes que los desarrollen (art. 53.3); orientan e informan la legislación, la práctica judicial y la actuación de los poderes públicos.",
 "I.4": "**Los dos «protectores»:** el **53** (tutela y amparo) y el **54** (Defensor del Pueblo).",
 "I.5": "**El «destructor»:** el **55** suspende los derechos. Es el único artículo del capítulo y el último del Título I.",
 "II": "**56 a 65 · La Corona**, lo más «espiritual». Rima: **55, 65**, ambos terminan en cinco.",
 "III": "**66 a 96 · Las Cortes Generales** (66 + **30**): el poder más extenso.",
 "IV": "**97 a 107 · Gobierno y Administración** (97 + **10**).",
 "V": "**108 a 116 · Relaciones Gobierno–Cortes** (108 + **8**): el número «comodín».",
 "VI": "**117 a 127 · Poder Judicial** (117 + **10**).",
 "VII": "**128 a 136 · Economía y Hacienda** (128 + **8**).",
 "VIII": "**137 a 158 · Organización territorial** (137 + **21**). Acaba en el **158**: «el 8 siempre viene al rescate». La cuestión territorial ya se asoma en el Título preliminar (lenguas, banderas, autonomía).",
 "IX": "**159 a 165 · Tribunal Constitucional** (159 + **6**).",
 "X": "**166 a 169 · Reforma constitucional** (166 + **3**): 166 iniciativa, 167 reforma «light», 168 reforma agravada y 169 límites (cuándo no puede iniciarse la reforma).",
 "D": "**4 adicionales, 9 transitorias, 1 derogatoria y 1 final (4-9-1-1):** estamos en la Transición, por eso lo que más hay son transitorias.",
}
M107_ARTS = {
 14: "Tiene tutela preferente y sumaria y amparo, pero **no** reserva de ley orgánica. Es uno de los dos artículos «colgantes» del Título I.",
 30: "El **30.2** (objeción de conciencia) es el único precepto de la sección 2.ª con **amparo**.",
 33: "Trampa del amparo: la **propiedad privada** y la herencia **no** tienen recurso de amparo (está en la sección 2.ª).",
 35: "Trampa del amparo: el **derecho al trabajo** **no** tiene recurso de amparo (sección 2.ª).",
 37: "El **conflicto colectivo** (37.2) **no** es objeto de amparo, a diferencia de la libertad sindical y la huelga (art. 28, sección 1.ª).",
}
