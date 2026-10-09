import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, ".")
sys.argv = [sys.argv[0]]
import boe, leyes25L as L
from examen25L import qs
norm = lambda x: " ".join(x.lower().replace("«", "").replace("»", "").replace('"', "").replace("\xa0", " ").split())
def bid(k, b): return b if b in boe.ley(k) else boe.bloque(k, b)
def plano(k, b): return norm(" ".join(boe.parrafos(k, bid(k, b))))
Q = {q["n"]: q for q in qs}
def acepta(n, ok):
    q = Q[n]
    if n in L.SI:
        datos = [d for d, *_ in L.SI[n] if d]
        if not datos: return None
        if not all(norm(d) in norm(q["o"][ok]) for d in datos): return False
        return not any(all(norm(d) in norm(q["o"][x]) for d in datos) for x in "abcd" if x != ok)
    dis, (aus, k2, b2) = L.NO[n]
    if ok in [x for x, *_ in dis]: return False
    return norm(aus) in norm(q["o"][ok]) and norm(aus) not in plano(k2, b2)
malas, manual = [], []
for n in L.LEY:
    real = "abcd"[Q[n]["c"]]
    r = {x: acepta(n, x) for x in "abcd"}
    if r[real] is None: manual.append(n); continue
    if not r[real] or any(r[x] for x in "abcd" if x != real): malas.append((n, r))
print("mutaciones detectadas en todas salvo:", malas, "| sin dato automático (revisión manual):", manual)
