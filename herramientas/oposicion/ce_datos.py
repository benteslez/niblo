# -*- coding: utf-8 -*-
"""Genera temas/ce.json: la Constitución Española COMPLETA, literal del texto
consolidado vigente del BOE (BOE-A-1978-31229), con su estructura (partes, títulos,
capítulos, secciones). Lo usa la vista «Constitución» (#/ce) de oposicion.html.

Los «títulos de artículo» (rúbricas didácticas) NO son texto de la CE (la CE no los
tiene): son los de la guía de estudio M101 (arts. 1 a 52, tabla de la p. 10). Los de
los arts. 53 a 55 no figuran en esa tabla: llevan `propio: true` (rótulo breve nuestro).

    cd herramientas/oposicion && python3 ce_datos.py
"""
import json, os, re, sys, datetime
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.join(AQUI, "boe"), AQUI]
import boe

RAIZ = os.path.dirname(os.path.dirname(AQUI))
L = boe.ley("CE")

# Guía M101, p. 10 (tabla «Capítulo IV. Garantías de los derechos y libertades CE»). Literal de la guía.
RUBRICAS = {
 1: "España se constituye en un Estado social y democrático de derecho", 2: "Unidad indisoluble de la nación española", 3: "Lengua", 4: "Bandera",
 5: "La capital del Estado es la villa de Madrid", 6: "Partidos políticos", 7: "Sindicatos y asociaciones empresariales", 8: "Fuerzas Armadas",
 9: "Los ciudadanos y los poderes públicos están sujetos a la constitución", 10: "Dignidad de la persona", 11: "Nacionalidad",
 12: "Los españoles son mayores de edad a los 18 años", 13: "Libertades de los extranjeros en España", 14: "Igualdad de todos ante la ley",
 15: "Derecho a la vida", 16: "Libertad ideológica, religiosa y de culto", 17: "Derecho a la libertad y seguridad",
 18: "Derecho al honor, a la intimidad personal y familiar y a la propia imagen", 19: "Los españoles tienen derecho a entrar y salir libremente de España",
 20: "Libertad de expresión", 21: "Derecho de reunión pacífica y sin armas", 22: "Derecho de asociación", 23: "Derecho a participar en asuntos públicos",
 24: "Derecho a la tutela judicial y efectiva", 25: "Principio de legalidad penal", 26: "Se prohíben los tribunales de honor en la Administración Civil",
 27: "Derecho a la educación y libertad de enseñanza", 28: "Libertad sindical y derecho a la huelga", 29: "Derecho de petición",
 30: "Los españoles tenemos el derecho y el deber de defender España", 31: "Deber de contribuir en el sostenimiento de los gastos públicos",
 32: "El hombre y la mujer tienen derecho a contraer matrimonio en igualdad jurídica", 33: "Derecho a la propiedad privada y a la herencia",
 34: "Derecho de fundación para fines de interés general", 35: "Derecho al trabajo y deber de trabajar", 36: "Colegios profesionales y agrupación de las profesiones tituladas",
 37: "Derecho a la negociación colectiva", 38: "Libertad de empresa en el marco de una economía de libre mercado", 39: "Protección de la familia e hijos",
 40: "Redistribución equitativa de la riqueza", 41: "Régimen público de la Seguridad Social para todos los ciudadanos",
 42: "Salvaguardia de los derechos de los inmigrantes españoles en el extranjero", 43: "Derecho a la salud", 44: "Cultura e investigación científica",
 45: "Protección del medio ambiente", 46: "Protección del patrimonio histórico-artístico", 47: "Derecho a una vivienda digna y adecuada",
 48: "Fomentar la participación de la juventud",
 49: "Las personas con discapacidad ejercen los derechos previstos en este Título en condiciones de libertad e igualdad reales y efectivas",
 50: "Pensiones públicas, periódicas y actualizadas para la tercera edad", 51: "Consumidores y usuarios, defensores y protegidos",
 52: "Organizaciones profesionales cuya estructura interna y funcionamiento deberá ser democrático"}
# Los arts. 53 a 55 no están en la tabla de la guía: rótulo breve propio (marcado «propio»).
PROPIAS = {53: "Vinculación, reserva de ley y tutela de los derechos", 54: "El Defensor del Pueblo", 55: "Suspensión de derechos y libertades"}

def limpia(t): return " ".join(t.replace("\xa0", " ").split())

preambulo = [[cl, limpia(t)] for cl, t in L["preambulo"][1]]
firma = [[cl, limpia(t)] for cl, t in L["firma"][1]]

# Recorrido en orden del documento: la estructura sale de los encabezados.
titulos = []; cur_t = cur_c = cur_s = None
for bid in L:
    tit, ps = L[bid]
    if bid in ("preambulo", "firma"): continue
    cl = ps[0][0] if ps else ""
    if bid == "tpreliminar":
        cur_t = {"id": "P", "num": "TÍTULO PRELIMINAR", "nombre": "", "caps": [], "arts": []}; titulos.append(cur_t); cur_c = cur_s = None
    elif re.fullmatch(r"t[ivx]+", bid) and cl == "titulo_num":
        cur_t = {"id": ps[0][1].replace("TÍTULO ", ""), "num": ps[0][1], "nombre": limpia(ps[1][1]), "caps": [], "arts": []}; titulos.append(cur_t); cur_c = cur_s = None
    elif cl == "capitulo_num":
        cur_c = {"num": ps[0][1], "nombre": limpia(ps[1][1]), "secs": [], "arts": []}; cur_t["caps"].append(cur_c); cur_s = None
    elif cl == "seccion":
        cur_s = {"nombre": limpia(ps[0][1]), "arts": []}; cur_c["secs"].append(cur_s)
    elif re.fullmatch(r"a\d+", bid):
        n = int(bid[1:]); A = {"n": n, "p": [limpia(t) for cl2, t in ps[1:]]}
        if n in RUBRICAS: A["t"] = RUBRICAS[n]
        elif n in PROPIAS: A["t"] = PROPIAS[n]; A["propio"] = True
        (cur_s or cur_c or cur_t)["arts"].append(A)

disp = []
for bid in ("primera", "segunda", "tercera", "cuarta", "primera-2", "segunda-2", "tercera-2", "cuarta-2", "quinta", "sexta", "septima", "octava", "novena", "dd", "df"):
    tit, ps = L[bid]
    disp.append({"id": bid, "t": limpia(tit), "p": [limpia(t) for cl, t in ps[1:]]})

# Comprobaciones: 169 artículos, rúbricas 1-52, orden y rangos
def todos(x):
    for A in x.get("arts", []): yield A
    for c in x.get("caps", []):
        yield from todos(c)
    for s in x.get("secs", []): yield from todos(s)
nums = [A["n"] for t in titulos for A in todos(t)]
assert nums == list(range(1, 170)), nums[:5]
assert [len(d["p"]) > 0 for d in disp] and len(disp) == 15
assert sum(1 for d in disp if "adicional" in d["t"]) == 4 and sum(1 for d in disp if "transitoria" in d["t"]) == 9

sello = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")
out = {"_format": "ce_v1", "_exportedAt": sello, "_fuente": "BOE-A-1978-31229 (texto consolidado vigente)", "preambulo": preambulo,
       "titulos": titulos, "disposiciones": disp, "firma": firma}
open(os.path.join(RAIZ, "temas", "ce.json"), "w", encoding="utf-8").write(json.dumps(out, ensure_ascii=False, separators=(",", ":")))
ip = os.path.join(RAIZ, "temas", "indice.json"); idx = json.load(open(ip, encoding="utf-8")); idx["ce"] = sello
json.dump(idx, open(ip, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ce.json:", len(nums), "artículos,", len(disp), "disposiciones,", sum(len(p[1]) for p in [("", preambulo)]), "párrafos de preámbulo")
