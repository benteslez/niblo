# -*- coding: utf-8 -*-
"""Preguntas del test real con DISCREPANCIA entre la plantilla oficial y la norma (o la fuente oficial).

Decisión del usuario (4-10-2026): se mantiene la respuesta de la plantilla, con la etiqueta
«Discrepancia» y la explicación debajo, como el texto legal. No quedan retenidas.

DISC[examen][n] = {"t": título, "p": [párrafos con **negrita**],
                   "citas": [(clave de norma, bloque, fragmento literal)]}
Cada fragmento citado se comprueba literal en la norma (boe.py) o, con clave "TEMA", en el
tema publicado que ya lo comprobó contra la fuente oficial (temas/<id>.json)."""
import os, json, re, unicodedata
import boe

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

DISC = {
 "X": {
  96: {"t": "La plantilla no casa con el art. 78.3 de la Ley General Presupuestaria",
       "p": ["La plantilla definitiva da la **b)** (10 % del capítulo de gastos corrientes en bienes y servicios, en cada ministerio).",
             "El art. 78.3 LGP fija como límite general «**el siete por ciento** del total de créditos del capítulo destinado a gastos corrientes en bienes y servicios del presupuesto vigente en cada momento».",
             "El 10 % solo se admite así: «podrá incrementarse hasta un máximo del **10 por ciento de los créditos del artículo 23**, \"indemnizaciones por razón del servicio\", **del programa 222A, \"Seguridad ciudadana\", del Ministerio del Interior**».",
             "Ninguna opción recoge esa regla: la b) aplica el 10 % al total del capítulo y a cualquier ministerio. Posible error de la plantilla o motivo de impugnación."],
       "citas": [("LGP", "Artículo 78", "el siete por ciento del total de créditos del capítulo destinado a gastos corrientes en bienes y servicios del presupuesto vigente en cada momento"),
                 ("LGP", "Artículo 78", "podrá incrementarse hasta un máximo del 10 por ciento de los créditos del artículo 23, \"indemnizaciones por razón del servicio\", del programa 222A, \"Seguridad ciudadana\", del Ministerio del Interior")]},
  31: {"t": "La fuente oficial no da la fecha de la plantilla",
       "p": ["La plantilla definitiva da la **a)** («Tratado de Fusión del 1 de julio de 1967»).",
             "Parlamento Europeo, ficha temática 1.1.2 (fuente oficial, no es texto legal): «La primera modificación institucional fue la realizada por el Tratado de Fusión, de **8 de abril de 1965**, que fusionó los órganos ejecutivos de las tres comunidades. Entró en vigor en **1967**».",
             "La a) y la d) se refieren al mismo tratado: la d) da la fecha de firma, que coincide con la fuente; la a), la de entrada en vigor, de la que la fuente solo dice el año. Ninguna fuente oficial consultada da el «1 de julio de 1967»."],
       "citas": [("PE", "1.1.2", "La primera modificación institucional fue la realizada por el Tratado de Fusión, de 8 de abril de 1965, que fusionó los órganos ejecutivos de las tres comunidades. Entró en vigor en 1967")]},
  44: {"t": "La caracterización de la plantilla no está en la LGSS",
       "p": ["La plantilla definitiva da la **d)** («Intervienen en la función redistribuidora de los tributos y tienen carácter finalista»).",
             "La LGSS no caracteriza así las aportaciones del Estado. Art. 109.1 a): «Las aportaciones progresivas del Estado, que se consignarán con carácter permanente en sus Presupuestos Generales, y las que se acuerden para atenciones especiales o resulten precisas por exigencia de la coyuntura».",
             "Art. 109.2: la modalidad «no contributiva y universal, se financiará mediante aportaciones del Estado al Presupuesto de la Seguridad Social».",
             "La respuesta de la plantilla es una caracterización doctrinal que no figura literal en la norma."],
       "citas": [("LGSS", "Artículo 109", "Las aportaciones progresivas del Estado, que se consignarán con carácter permanente en sus Presupuestos Generales, y las que se acuerden para atenciones especiales o resulten precisas por exigencia de la coyuntura"),
                 ("LGSS", "Artículo 109", "no contributiva y universal, se financiará mediante aportaciones del Estado al Presupuesto de la Seguridad Social")]},
  60: {"t": "El enunciado cita la Ley 23/1982, que literalmente dice otra cosa",
       "p": ["La plantilla definitiva da la **a)** (Ley 33/2003), que es lo vigente.",
             "Pero el art. 6.Uno de la Ley 23/1982, por la que pregunta el enunciado, sigue diciendo: «Se aplicará, con carácter supletorio, **la Ley del Patrimonio del Estado**» (opción b).",
             "La Ley 33/2003, disposición adicional cuarta: el régimen del Patrimonio Nacional será el de la Ley 23/1982, «**aplicándose con carácter supletorio las disposiciones de esta ley y sus normas de desarrollo**».",
             "Según se lea la pregunta (letra de la Ley 23/1982 o Derecho vigente) valen la b) o la a). Posible motivo de impugnación."],
       "citas": [("L23_1982", "asexto", "Se aplicará, con carácter supletorio, la Ley del Patrimonio del Estado"),
                 ("LPAP", "dacuarta", "aplicándose con carácter supletorio las disposiciones de esta ley y sus normas de desarrollo")]},
 },
 "P": {
  91: {"t": "Matiz del contrato menor",
       "p": ["La plantilla definitiva da la **d)** (un pago en firme en material fungible de 9.000 euros sí se fiscaliza).",
             "Pero el art. 151 a) LGP excluye de la fiscalización previa «**los contratos menores** así como los asimilados a ellos en virtud de la legislación contractual».",
             "Y el art. 118.1 LCSP considera menores los contratos de valor estimado inferior «a **15.000 euros**, cuando se trate de contratos de suministro o de servicios».",
             "Si esa compra se tramitara como contrato menor, tampoco se fiscalizaría; el enunciado no lo dice. Posible motivo de impugnación."],
       "citas": [("LGP", "a151", "los contratos menores así como los asimilados a ellos en virtud de la legislación contractual"),
                 ("LCSP", "Artículo 118", "a 15.000 euros, cuando se trate de contratos de suministro o de servicios")]},
 },
}


def _n(s):
    s = unicodedata.normalize("NFC", s).replace(" ", " ").replace("“", "\"").replace("”", "\"").replace("«", "\"").replace("»", "\"")
    return re.sub(r"\s+", " ", s).strip().lower()


def comprobar():
    """Cada cita, literal en su fuente; los párrafos que la reproducen, también."""
    for ex, d in DISC.items():
        for n, e in d.items():
            for k, b, frag in e["citas"]:
                if k == "PE":   # ficha temática del Parlamento Europeo, texto guardado en fuentes/pe/<ficha>.txt
                    fuente = open(os.path.join(RAIZ, "herramientas", "oposicion", "fuentes", "pe", b + ".txt"), encoding="utf-8").read()
                elif k == "TEMA":
                    fuente = json.dumps(json.load(open(os.path.join(RAIZ, "temas", b + ".json"), encoding="utf-8")), ensure_ascii=False).replace("**", "")
                else:
                    bid = b if b in boe.ley(k) else boe.bloque(k, b)
                    fuente = " ".join(boe.parrafos(k, bid))
                assert _n(frag) in _n(fuente), ("CITA NO LITERAL", ex, n, k, b, frag)
                assert any(_n(frag) in _n(p.replace("**", "")) for p in e["p"]), ("CITA COMPROBADA QUE NO APARECE EN LA EXPLICACIÓN", ex, n, frag)
    return DISC


if __name__ == "__main__":
    comprobar(); print("discrepancias comprobadas:", {k: sorted(v) for k, v in DISC.items()})
