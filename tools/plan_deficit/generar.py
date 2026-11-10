#!/usr/bin/env python3
"""Plan de deficit de Ruben: prolonga <script id="pc-plan-data"> de index.html.

Uso:  python3 tools/plan_deficit/generar.py        (desde la raiz del repo)

No calcula ningun dia nuevo: cada dia generado es la copia exacta (comidas,
gramos y macros) de un dia ya publicado del plan de septiembre de 2026, que
sirve de plantilla. Lo unico que se asigna aqui es la fecha, la rutina de
entreno del dia de la semana y las marcas del ciclo (dia N de M, semana de
descarga, comidas libres de Navidad).

Es idempotente: borra lo que haya desde INICIO y lo vuelve a escribir.
"""
import datetime as dt
import json
import pathlib
import re

RAIZ = pathlib.Path(__file__).resolve().parents[2]
HTML = RAIZ / "index.html"

INICIO = dt.date(2026, 11, 10)
FIN = dt.date(2027, 2, 9)          # 3 meses: 92 dias

DIAS = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

# Rutina por dia de la semana (0 = lunes). Claves de PC_ENTRENOS en index.html.
ENTRENO = ["fz_pecho_triceps", "fz_espalda_biceps", "fz_pecho_hombro",
           "fz_pierna_espalda_abs", "fz_hombro_brazos_abs", "descanso", "descanso"]

# Cuatro semanas plantilla (lunes..domingo): dia de septiembre de 2026 que se copia.
# D reordena dias de la primera semana para no repetir plato con las semanas vecinas.
SEMANAS = {
    "A": [7, 8, 9, 10, 11, 12, 13],
    "B": [14, 15, 16, 17, 18, 19, 20],
    "C": [21, 22, 23, 24, 25, 26, 27],
    "D": [14, 2, 3, 4, 10, 5, 6],
}
ORDEN = ["D", "A", "B", "C"]       # la semana del 9-nov es la D

# Semanas de descarga (lunes de cada una): menos series, mismo peso.
DESCARGA = {dt.date(2026, 12, 21), dt.date(2027, 2, 1)}

# Navidad: las dos comidas libres del domingo se pasan a la cena de la vispera
# y a la comida del festivo; ese domingo es un dia normal (plantilla de sabado).
LIBRES = {
    dt.date(2026, 12, 24): ("cena", "Nochebuena: la cena de hoy es la comida libre. "
                            "Esta semana las dos comidas libres pasan del domingo a hoy y a mañana."),
    dt.date(2026, 12, 25): ("comida", "Navidad: la comida de hoy es libre. "
                            "A cambio, el domingo 27 es un día normal del plan."),
    dt.date(2026, 12, 31): ("cena", "Nochevieja: la cena de hoy es la comida libre. "
                            "Esta semana las dos comidas libres pasan del domingo a hoy y a mañana."),
    dt.date(2027, 1, 1): ("comida", "Año Nuevo: la comida de hoy es libre. "
                          "A cambio, el domingo 3 es un día normal del plan."),
}
DOMINGO_NORMAL = {dt.date(2026, 12, 27): 5, dt.date(2027, 1, 3): 19}


def main():
    html = HTML.read_text(encoding="utf-8")
    patron = re.compile(r'(<script id="pc-plan-data" type="application/json">\s*)(.*?)(\s*</script>)', re.S)
    m = patron.search(html)
    plan = [d for d in json.loads(m.group(2)) if d["date"] < INICIO.isoformat()]
    sep = {int(d["date"][-2:]): d for d in plan if d["date"].startswith("2026-09")}

    total = (FIN - INICIO).days + 1
    lunes0 = INICIO - dt.timedelta(days=INICIO.weekday())
    nuevos = []
    for i in range(total):
        f = INICIO + dt.timedelta(days=i)
        lunes = f - dt.timedelta(days=f.weekday())
        nsem = (lunes - lunes0).days // 7
        origen = DOMINGO_NORMAL.get(f) or SEMANAS[ORDEN[nsem % 4]][f.weekday()]
        base = json.loads(json.dumps(sep[origen]))
        dia = {
            "date": f.isoformat(), "day_num": f.day, "weekday": DIAS[f.weekday()],
            "flexible": base["flexible"], "target_kcal": base["target_kcal"],
            "sat_prep": base["sat_prep"] and f.weekday() == 5,
            "training_key": ENTRENO[f.weekday()],
            "ciclo_dia": i + 1, "ciclo_total": total, "semana": nsem + 1,
        }
        if lunes in DESCARGA:
            dia["descarga"] = True
        if "totales" in base:
            dia["totales"] = base["totales"]
        dia["meals"] = base["meals"]
        if f in LIBRES:
            cual, nota = LIBRES[f]
            dia["flexible"] = True
            dia["target_kcal"] = 2200
            dia.pop("totales", None)
            dia["meals"][cual] = {"flex": True}
            dia["nota"] = nota
        nuevos.append(dia)

    plan += nuevos
    texto = json.dumps(plan, ensure_ascii=False)
    html = html[:m.start(2)] + texto + html[m.end(2):]
    HTML.write_text(html, encoding="utf-8")
    libres = sum(1 for d in nuevos if d["flexible"])
    print(f"{len(nuevos)} dias: {nuevos[0]['date']} -> {nuevos[-1]['date']} ({libres} con comida libre)")


if __name__ == "__main__":
    main()
