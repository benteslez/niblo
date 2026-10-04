# Uso: python3 boe/probar.py P   → verifica boe/leyes25P.py contra examen25P (o X / L)
import sys; ex = sys.argv[1]; import os; sys.path[:0] = [os.getcwd(), os.path.join(os.getcwd(), "boe")]; sys.argv = ["x"]
import importlib, verif_examen as V
L = importlib.import_module("leyes25" + ex); E = importlib.import_module("examen25" + ex)
LE = V.verificar(L, E.qs)
cubiertas = set(L.LEY) | set(getattr(L, "SIN_LEY", {}))
print("con texto legal:", len(LE), "| sin ley:", len(getattr(L, "SIN_LEY", {})), "| pendientes:", [q["n"] for q in E.qs if not q["anulada"] and q["n"] not in cubiertas][:40])
print("mutación (malas, manual):", V.mutacion(L, E.qs))
