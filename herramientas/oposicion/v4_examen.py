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
