# -*- coding: utf-8 -*-
"""Texto legal y comprobación plantilla ↔ ley de un examen, a partir de su
especificación (módulo con NOMBRE, LEY, SI, NO; ver leyes25L.py).

    LEY[n] = [(norma, bloque, [párrafos] | None, título, [negritas])]
    SI[n]  = [(dato en la opción correcta | None, norma, bloque, fragmento literal)]
    NO[n]  = ([(letra, dato en ese distractor, norma, bloque, fragmento)],
              (fragmento de la opción correcta que NO está en la ley, norma, bloque))

Comprueba, y se detiene si algo falla: fragmentos y negritas literales en la
norma; dato de la plantilla en la opción correcta; ningún distractor con todos
los datos; en las preguntas en negativo, los tres distractores en la norma y la
correcta ausente. mutacion() cambia la respuesta a cada otra letra y exige que
la comprobación falle (las preguntas sin dato automático se listan aparte)."""
import boe

norm = lambda x: " ".join(x.lower().replace("«", "").replace("»", "").replace('"', "").replace("“", "").replace("”", "").replace("\xa0", " ").split())


def bid(k, b): return b if b in boe.ley(k) else boe.bloque(k, b)
def plano(k, b): return norm(" ".join(boe.parrafos(k, bid(k, b))))


def bloques(L, n):
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


def acepta(L, q, ok):
    """¿La comprobación da por buena la letra ok? (None: sin dato automático)."""
    n = q["n"]
    if n in L.SI:
        datos = [d for d, *_ in L.SI[n] if d]
        if not datos: return None
        if not all(norm(d) in norm(q["o"][ok]) for d in datos): return False
        return not any(all(norm(d) in norm(q["o"][x]) for d in datos) for x in "abcd" if x != ok)
    dis, (aus, k2, b2) = L.NO[n]
    if ok in [x for x, *_ in dis]: return False
    return norm(aus) in norm(q["o"][ok]) and norm(aus) not in plano(k2, b2)


def verificar(L, qs):
    Q = {q["n"]: q for q in qs}
    LEYES = {}
    RET = getattr(L, "RETENIDA", {})   # respuesta oficial que NO casa con la ley: solo se muestra el texto
    assert set(L.LEY) - set(RET) == set(L.SI) | set(L.NO) and not set(L.SI) & set(L.NO) and not set(RET) & (set(L.SI) | set(L.NO)), "LEY/SI/NO no casan"
    for n in L.LEY:
        q = Q[n]; ok = "abcd"[q["c"]]
        assert not q["anulada"], n
        LEYES[n] = bloques(L, n)
        if n in RET: continue
        if n in L.SI:
            for dato, k, b, frag in L.SI[n]:
                assert norm(frag) in plano(k, b), ("APOYO NO LITERAL", n, k, b, frag)
                if dato: assert norm(dato) in norm(q["o"][ok]), ("LA PLANTILLA NO CASA CON LA LEY", n, ok, dato)
        else:
            dis, (aus, k2, b2) = L.NO[n]
            assert sorted([x for x, *_ in dis] + [ok]) == list("abcd"), ("NO: letras", n)
            for x, dato, k, b, frag in dis:
                assert norm(frag) in plano(k, b), ("APOYO NO LITERAL", n, k, b, frag)
                assert norm(dato) in norm(q["o"][x]), ("DISTRACTOR NO CASA", n, x, dato)
        assert acepta(L, q, ok) is not False, ("LA COMPROBACIÓN NO ACEPTA LA PLANTILLA", n, ok)
    return LEYES


def mutacion(L, qs):
    Q = {q["n"]: q for q in qs}
    malas, manual = [], []
    for n in L.LEY:
        if n in getattr(L, "RETENIDA", {}): continue
        real = "abcd"[Q[n]["c"]]
        r = {x: acepta(L, Q[n], x) for x in "abcd"}
        if r[real] is None: manual.append(n); continue
        if not r[real] or any(r[x] for x in "abcd" if x != real): malas.append((n, r))
    return malas, manual
