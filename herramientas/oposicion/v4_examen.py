# -*- coding: utf-8 -*-
"""Preguntas reales del examen GACE-L 2025 que corresponden al tema I.2.
Enunciado y opciones: literales del cuestionario oficial. Respuesta: plantilla
definitiva. Explicación: una por opción, con citas comprobadas (c / rub)."""
from v4_util import *

EX1 = examen(1, {
    "a": f"Es la rúbrica literal del Título I: {rub('TÍTULO I', 'De los derechos y deberes fundamentales')} (arts. 10 a 55).",
    "b": f"{rub('Sección 2.ª', 'De los derechos y deberes de los ciudadanos')} es la rúbrica de la **Sección 2.ª** del Capítulo segundo (arts. 30 a 38), no la del Título.",
    "c": f"{rub('CAPÍTULO PRIMERO', 'De los españoles y los extranjeros')} es la rúbrica del **Capítulo primero** (arts. 11 a 13).",
    "d": f"{rub('CAPÍTULO SEGUNDO', 'Derechos y libertades')} es la rúbrica del **Capítulo segundo** (arts. 14 a 38).",
}, apoyo=[("De los derechos y deberes fundamentales", "CE*", None, "TÍTULO I De los derechos y deberes fundamentales")])

EX2 = examen(2, {
    "a": f"No existe ningún «Pleno conjunto»: el art. 2.5 manda volver a la Comisión Mixta: {c('LO3', 'segundo', 'se procederá en nueva sesión de la Comisión')}. Tampoco se exige mayoría absoluta en las dos Cámaras.",
    "b": f"Mismo error que la a): no hay «Pleno conjunto». Y la designación nunca se hace por mayoría simple de las Cámaras: la mayoría simple solo rige para los acuerdos de la Comisión ({c('LO3', 'segundo', 'Los acuerdos de la Comisión se adoptarán por mayoría simple')}, art. 2.3).",
    "c": f"Reproduce el art. 2.5: {c('LO3', 'segundo', 'en el plazo máximo de un mes, a formular sucesivas propuestas')}; {c('LO3', 'segundo', 'una vez conseguida la mayoría de los tres quintos en el Congreso, la designación quedará realizada al alcanzarse la mayoría absoluta del Senado')}.",
    "d": "Cambia dos datos: «un mes» por «quince días» y «mayoría absoluta» por «mayoría simple» en el Senado.",
}, apoyo=[("nueva sesión de la Comisión", "LO3", "segundo", "se procederá en nueva sesión de la Comisión"),
          ("plazo máximo de un mes", "LO3", "segundo", "en el plazo máximo de un mes"),
          ("tres quintos en el Congreso", "LO3", "segundo", "la mayoría de los tres quintos en el Congreso"),
          ("mayoría absoluta en el Senado", "LO3", "segundo", "al alcanzarse la mayoría absoluta del Senado")])

EX10 = examen(10, {
    "a": f"Demasiado amplia: el art. 3.2 LOPJ no la extiende a todo asunto con militares implicados; la ciñe {c('LOPJ', 3, 'en el ámbito estrictamente castrense y, en su caso, en las materias que establezca la declaración del estado de sitio')}.",
    "b": f"Reproduce el art. 3.2 LOPJ: los órganos de la jurisdicción militar {c('LOPJ', 3, 'administran Justicia en el ámbito estrictamente castrense y, en su caso, en las materias que establezca la declaración del estado de sitio')}. Conecta con el art. 35 LO 4/1981: en la declaración del sitio el Congreso puede determinar {c('LO4', 'treinta y cinco', 'los delitos que durante su vigencia quedan sometidos a la Jurisdicción Militar')}.",
    "c": f"Demasiado estrecha: el art. 3.2 LOPJ no la reduce a lo disciplinario; cita {c('LOPJ', 3, 'las leyes penales, procesales y disciplinarias militares')}, y el art. 35 LO 4/1981 le atribuye precisamente **delitos** durante el estado de sitio.",
    "d": f"Olvida el ámbito **estrictamente castrense**, que es el principal; el estado de sitio es el supuesto añadido: {c('LOPJ', 3, 'y, en su caso, en las materias que establezca la declaración del estado de sitio')}.",
}, apoyo=[("estrictamente castrense", "LOPJ", 3, "administran Justicia en el ámbito estrictamente castrense"),
          ("en las materias que establezca la declaración del estado de sitio", "LOPJ", 3, "en su caso, en las materias que establezca la declaración del estado de sitio")])
EX10_NOTA = lit("LOPJ", 3, solo=[1], titulo="Artículo 3.2 (LOPJ)", resaltar=["en el ámbito estrictamente castrense y, en su caso, en las materias que establezca la declaración del estado de sitio"])

# ---------------------------------------------------------------------------
# Examen GACE-L 2025 EXTRAORDINARIO (primer ejercicio): preguntas 4, 5 y 6, del tema I.2.
EX_X4 = examen(4, {
    "a": f"El art. 15 no figura en la lista del art. 55.1, que solo permite suspender {c('CE', 55, 'Los derechos reconocidos en los artículos 17, 18, apartados 2 y 3, artículos 19, 20, apartados 1, a) y d), y 5, artículos 21, 28, apartado 2, y artículo 37, apartado 2')}. La vida y la integridad física y moral (art. 15 → I.4.1) **nunca** se suspenden.",
    "b": f"La libertad personal es el art. 17 ({c('CE', 17, 'Toda persona tiene derecho a la libertad y a la seguridad')}), el primero de la lista del art. 55.1: **sí** puede suspenderse (en el estado de excepción, salvo su apartado 3).",
    "c": f"El derecho a la protección de la salud ({c('CE', 43, 'Se reconoce el derecho a la protección de la salud')}, art. 43.1) tampoco figura en el art. 55.1, pero **no es un derecho fundamental**: está en el Capítulo tercero, {rub('CAPÍTULO TERCERO', 'De los principios rectores de la política social y económica')} (→ I.10.6), y la pregunta pide un derecho fundamental.",
    "d": f"El derecho de reunión es el art. 21, que figura en la lista del art. 55.1 ({c('CE', 55, 'artículos 21, 28, apartado 2')}): **sí** puede suspenderse.",
}, apoyo=[("vida", "CE", 15, "Todos tienen derecho a la vida")], cod="X")

EX_X5 = examen(5, {
    "a": f"El art. 30.1 no fija el plazo en días, sino en meses: {c('LO3', 'treinta', 'en término no superior al de un mes')}.",
    "b": f"Reproduce el art. 30.1: {c('LO3', 'treinta', 'las autoridades y los funcionarios vendrán obligados a responder por escrito en término no superior al de un mes')}. La Dirección General del INAP pertenece a una Administración Pública.",
    "c": f"Quince días es otro plazo de la misma ley: el del informe escrito que pide el Defensor al admitir una queja ({c('LO3', 'dieciocho', 'en el plazo máximo de quince días')}, art. 18.1 → IV.5.1).",
    "d": f"Tres meses no aparece en el art. 30: el plazo es {c('LO3', 'treinta', 'un mes')}.",
}, apoyo=[("Un mes", "LO3", "treinta", "en término no superior al de un mes")], cod="X")

EX_X6 = examen(6, {
    "a": f"El Tribunal Constitucional protege los derechos por el recurso de amparo ({c('CE', 161, 'Del recurso de amparo por violación de los derechos y libertades referidos en el artículo 53, 2')}, art. 161.1 b) → II.5), pero no supervisa la actividad de la Administración.",
    "b": f"Es la definición del art. 54: {c('CE', 54, 'Una ley orgánica regulará la institución del Defensor del Pueblo, como alto comisionado de las Cortes Generales, designado por éstas para la defensa de los derechos comprendidos en este Título, a cuyo efecto podrá supervisar la actividad de la Administración')}.",
    "c": f"El Consejo General del Poder Judicial es el gobierno de los jueces: {c('CE', 122, 'El Consejo General del Poder Judicial es el órgano de gobierno del mismo')} (art. 122.2); no supervisa a la Administración.",
    "d": f"El Tribunal Supremo es un órgano jurisdiccional: {c('CE', 123, 'El Tribunal Supremo, con jurisdicción en toda España, es el órgano jurisdiccional superior en todos los órdenes, salvo lo dispuesto en materia de garantías constitucionales')} (art. 123.1).",
}, apoyo=[("Defensor del Pueblo", "CE", 54, "la institución del Defensor del Pueblo")], cod="X")
