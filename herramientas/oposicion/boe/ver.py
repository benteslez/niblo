import sys, boe
# uso: ver.py LEY bloque [bloque…]   |   ver.py LEY ?fragmento
k = sys.argv[1]
for a in sys.argv[2:]:
    if a.startswith("?"):
        print(k, a, "→", boe.buscar(k, a[1:])[:8]); continue
    a = a if a in boe.ley(k) else boe.bloque(k, a)
    tit, ps = boe.ley(k)[a]
    print(f"=== {k} {a} «{tit}»")
    for i, (cl, t) in enumerate(ps): print(f" [{i}] {t}")
