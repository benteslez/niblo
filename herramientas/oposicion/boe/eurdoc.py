# -*- coding: utf-8 -*-
"""Textos de EUR-Lex que no tienen artículos (sentencias del TJUE, declaraciones anejas
a los Tratados, síntesis y glosario de EUR-Lex) → <CLAVE>.json con el formato de
eurext.js ([{doc, art, ps}]), un único bloque «Texto» con sus párrafos literales.
La página se descarga antes con eurlex.js (navegador, por el desafío antibots):
    node eurlex.js "<url>" pagina.html
    python3 eurdoc.py CLAVE pagina.html "primer párrafo…" "párrafo final (excluido)…"
Solo se guardan los párrafos (p, li, h1-h4) desde el que empieza por «inicio» hasta el
anterior al que empieza por «fin»; las llamadas de nota («( 1 )») se quitan."""
import json, os, re, sys
from html.parser import HTMLParser

AQUI = os.path.dirname(os.path.abspath(__file__))
BLOQUES = {"p", "li", "h1", "h2", "h3", "h4", "td"}


class _P(HTMLParser):
    def __init__(self):
        super().__init__(); self.ps = []; self.pila = 0; self.buf = []; self.salta = 0
    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript"): self.salta += 1
        a = dict(attrs)
        if tag == "a" and (a.get("id") or "").startswith("ntc"): self.salta += 1; self._nota = True
        if tag in BLOQUES:
            if self.pila == 0: self.buf = []
            else: self.buf.append(" ")   # lista dentro de un párrafo: «consta de: los Tratados…»
            self.pila += 1
    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript"): self.salta -= 1
        if tag == "a" and getattr(self, "_nota", False): self.salta -= 1; self._nota = False
        if tag in BLOQUES and self.pila:
            self.pila -= 1
            if self.pila == 0:
                t = " ".join("".join(self.buf).replace("\xa0", " ").split())
                if t: self.ps.append(t)
    def handle_data(self, d):
        if self.pila and not self.salta: self.buf.append(d)


def extrae(html, inicio, fin):
    p = _P(); p.feed(open(html, encoding="utf-8").read())
    ps = [re.sub(r"\s*\(\s*\d*\s*\)(?=\s*\))", "", x) for x in p.ps]   # llamada de nota: «asunto 6/64 ( 1 ) )» → «asunto 6/64 )»
    i = next(k for k, x in enumerate(ps) if x.startswith(inicio))
    j = next((k for k, x in enumerate(ps) if k > i and x.startswith(fin)), len(ps))
    return ps[i:j]


if __name__ == "__main__":
    k, html, inicio, fin = sys.argv[1:5]
    ps = extrae(html, inicio, fin)
    json.dump([{"doc": ps[0], "art": "Texto", "ps": ps}], open(os.path.join(AQUI, k + ".json"), "w", encoding="utf-8"), ensure_ascii=False)
    print(k, len(ps), "párrafos")
    for n, x in enumerate(ps, 1): print(f" [{n}] {x[:110]}")
