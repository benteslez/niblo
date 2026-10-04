# -*- coding: utf-8 -*-
"""Comprueba leyes25L.py contra el texto del BOE y contra la plantilla definitiva."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.argv = [sys.argv[0]]
import boe, leyes25L as L
from examen25L import qs
Q = {q["n"]: q for q in qs}
norm = lambda x: " ".join(x.lower().replace("«", "").replace("»", "").replace('"', "").replace("\xa0", " ").split())
def bid(k, b): return b if b in boe.ley(k) else boe.bloque(k, b)
def plano(k, b): return norm(" ".join(boe.parrafos(k, bid(k, b))))

def bloques(n):
    out = []
    for k, b, idx, tit, negr in L.LEY[n]:
        ps = boe.parrafos(k, bid(k, b))
        if idx is None:
            idx = [i for i, p in enumerate(ps) if any(r in p for r in negr)]
        sel, usados = [], set()
        for i in idx:
            t = ps[i]
            for r in negr:
                if r in t and r not in usados:
                    t = t.replace(r, "**" + r + "**", 1); usados.add(r)
            sel.append(t)
        assert not set(negr) - usados, ("NEGRITA NO LITERAL", n, k, b, set(negr) - usados)
        out.append({"t": L.NOMBRE[k] + " · " + tit, "f": boe.IDS[k], "p": sel})
    return out

LEYES = {}
for n in L.LEY:
    q = Q[n]; ok = "abcd"[q["c"]]
    assert not q["anulada"], n
    LEYES[n] = bloques(n)
    if n in L.SI:
        ap = L.SI[n]
        for dato, k, b, frag in ap:
            assert norm(frag) in plano(k, b), ("APOYO NO LITERAL", n, k, b, frag)
            if dato: assert norm(dato) in norm(q["o"][ok]), ("LA PLANTILLA NO CASA CON LA LEY", n, ok, dato)
        datos = [d for d, *_ in ap if d]
        for x in "abcd":
            if x != ok and datos:
                assert not all(norm(d) in norm(q["o"][x]) for d in datos), ("DISTRACTOR IGUAL DE APOYADO", n, x)
    else:
        dis, (aus, k2, b2) = L.NO[n]
        assert sorted([x for x, *_ in dis] + [ok]) == list("abcd"), ("NO: letras", n)
        for x, dato, k, b, frag in dis:
            assert norm(frag) in plano(k, b), ("APOYO NO LITERAL", n, k, b, frag)
            assert norm(dato) in norm(q["o"][x]), ("DISTRACTOR NO CASA", n, x, dato)
        assert norm(aus) in norm(q["o"][ok]), ("NO: la correcta no contiene", n, aus)
        assert norm(aus) not in plano(k2, b2), ("NO: la correcta SÍ está en la ley", n, aus)
assert set(L.LEY) == set(L.SI) | set(L.NO) and not set(L.SI) & set(L.NO)
print("coherentes con el BOE:", len(LEYES), sorted(LEYES), file=sys.stderr)
