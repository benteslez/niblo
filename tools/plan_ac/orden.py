# -*- coding: utf-8 -*-
"""Orden de cocina de cada dia: todo lo que se cocina ese dia, junto.

Peticion de la familia (21-10-2026): el plan decia «cuece la zanahoria 20
min», «cuece la papa 20 min» y, en la cena, otra vez la papa. Aqui se junta
todo lo del dia (la sesion de batch, lo que se cocina para el dia y lo de
cada comida) por forma de cocinar:

- una olla de agua sin sal para todo lo que se hierve, con la vaporera
  encima (se mete cada cosa a su minuto para que acabe a la vez, y al final
  se separa cada cosa para su receta);
- lo que va despues en la misma agua (la pasta);
- los guisos y cazos propios (llevan su caldo: no se comparte el agua);
- una horneada (o dos seguidas si piden temperaturas distintas);
- la sarten, una cosa tras otra.

Los tiempos son los de cada receta. Lo que no es de este modulo (cantidades,
dias, nevera o congelador) sigue saliendo en cada receta.
"""
import re
from collections import defaultdict

# Forma de cocinar de cada receta. i = indice del ingrediente (para la cantidad);
# t = minutos (de, a); dep = necesita lo de la olla o la vaporera antes.
def O(m, que, i=None, t=None, forma="", **kw):
    return dict(m=m, que=que, i=i, t=t, forma=forma, **kw)

VAPOR_T = {"calabacin": (6, 8), "zanahoria": (15, 20), "ahuyama": (15, 20), "habichuela": (12, 15),
           "brocoli": (8, 10), "coliflor": (8, 10), "repollo": (8, 10)}

COCCION = {
    "arepa": [O("sarten", "arepas", t=(10, 12), forma="5-6 min por lado")],
    "tortita-trigo": [O("sarten", "tortitas", t=(4, 6), forma="2-3 min por lado, por tandas")],
    "tortita-avena": [O("sarten", "tortitas", t=(4, 6), forma="2-3 min por lado, por tandas")],
    "tortilla-calabacin": [O("sarten", "tortilla", t=(5, 6), forma="tapada, a fuego bajo, bien cuajada")],
    "huevo-duro": [O("olla", "huevo", 0, (10, 10), "entero, con cáscara")],
    "avena-formula": [O("cazo", "avena", 0, (5, 5), "en su agua, removiendo")],
    "muffins": [O("horno", "muffins", t=(15, 18), temp=180)],
    "pan-tostado": [O("tostar", "pan", t=(2, 3), forma="ligeramente")],
    "hamb-pollo": [O("vapor", "ahuyama", 1, (15, 15), "en dados"),
                   O("horno", "hamburguesitas de pollo", t=(20, 20), temp=180, dep=True, alt="sartén tapada, 5-6 min por lado")],
    "pollo-desmenuzado": [O("guiso", "pollo con la zanahoria", 0, (30, 35), "el muslo entero, en agua que lo cubra, a fuego suave")],
    "hamb-res": [O("olla", "papa", 1, (15, 20), "pelada, en trozos"),
                 O("horno", "hamburguesitas de res", t=(20, 20), temp=180, dep=True, alt="sartén tapada, 6 min por lado")],
    "res-guisada": [O("guiso", "carne de res con la zanahoria", 0, (90, 90), "dorada antes 3-4 min; olla a presión: 35 min")],
    "pescado-laminas": [O("horno", "tilapia en papillote", t=(12, 14), temp=180)],
    "pescado-tortitas": [O("olla", "papa", 1, (15, 20), "pelada, en trozos"), O("olla", "zanahoria", 2, (15, 20), "pelada, en trozos"),
                         O("vapor", "tilapia", 0, (8, 10), "sin espinas"),
                         O("horno", "tortitas de tilapia", t=(15, 15), temp=200, dep=True, alt="sartén, 3 min por lado")],
    "pescado-crema": [O("vapor", "ahuyama", 1, (15, 15), "en dados"), O("vapor", "tilapia", 0, (8, 10), "sin espinas, encima de la ahuyama")],
    "salmon-horno": [O("horno", "salmón en papillote", t=(12, 15), temp=180)],
    "lenteja-chafada": [O("olla", "zanahoria", 1, (15, 20), "pelada, en rodajas"),
                        O("vapor", "lenteja de bote", 0, (3, 4), "ya enjuagada, solo para calentarla")],
    "hamb-lenteja": [O("olla", "papa", 1, (15, 20), "pelada, en trozos"),
                     O("horno", "hamburguesitas de lenteja", t=(20, 20), temp=180, dep=True, alt="sartén, 3-4 min por lado")],
    "tofu-dorado": [O("sarten", "bastones de tofu", t=(4, 5), forma="2 min por lado")],
    "camaron-papa": [O("olla", "papa", 1, (15, 20), "pelada, en trozos"),
                     O("cazo", "camarón", 0, (3, 4), "en agua sin sal, aparte (es alérgeno: no en la olla común)"),
                     O("sarten", "pastelitos de camarón", t=(6, 8), dep=True)],
    "pasta-mariscos": [O("cazo", "mejillones o almejas", 1, (4, 6), "al vapor hasta que se abran, aparte (alérgeno)"),
                       O("despues", "pasta", 0, None, "2-3 min más de lo que diga el paquete")],
    "garbanzo-chafado": [O("vapor", "ahuyama", 1, (15, 15), "en dados"),
                         O("vapor", "garbanzo de bote", 0, (3, 4), "ya enjuagado, solo para calentarlo")],
    "cerdo-guisado": [O("guiso", "lomo de cerdo con la zanahoria", 0, (40, 40), "a fuego suave, tapado")],
    "pavo-guisado": [O("guiso", "pavo con la zanahoria", 0, (40, 40), "a fuego suave, tapado")],
    "atun-pastelito": [O("olla", "papa", 1, (15, 20), "pelada, en trozos"),
                       O("sarten", "pastelitos de atún", t=(6, 8), dep=True, forma="3-4 min por lado")],
    "quinua-verdura": [O("cazo", "quinua con la zanahoria", 0, (15, 18), "en el doble de agua, tapada; luego 5 min de reposo")],
    "bastones-papa": [O("olla", "papa", 0, (15, 20), "en bastones")],
    "bastones-yuca": [O("olla", "yuca", 0, (25, 30), "en trozos, sin la fibra central")],
    "bastones-batata": [O("horno", "bastones de batata", t=(25, 30), temp=200)],
    "tuberculo-cocido": [O("olla", None, 0, (20, 30), "en bastones")],
    "pasta-verdura": [O("despues", "pasta", 0, None, "2-3 min más de lo que diga el paquete")],
    "arroz-blando": [O("cazo", "arroz", 0, None, "en el triple de agua, hasta que esté muy blando")],
    "verduras-vapor": [O("vapor", None, 0, None, "en bastones")],
    "ahuyama-asada": [O("horno", "bastones de ahuyama", t=(25, 30), temp=200)],
    "pure-verduras": [O("vapor", "ahuyama", 0, (15, 20), "en trozos"), O("vapor", "zanahoria", 1, (15, 20), "en trozos"),
                      O("vapor", "calabacín", 2, (15, 20), "en trozos")],
    "arveja-chafada": [O("olla", "arveja", 0, (12, 15), "desgranada o congelada (si es de bote, 3-4 min en la vaporera)")],
    "frijol-chafado": [O("guiso", "fríjol con la zanahoria", 0, (30, 30), "remojado 12 h; olla a presión 25-30 min (normal, 1 h 30 min o más)")],
    "verdura-asada": [O("horno", None, t=(25, 35), temp=200)],
    "verdura-en-guiso": [O("vapor", None, 0, (8, 12), "picada muy fina, hasta que esté muy blanda")],
    "verdura-cruda": [O("escaldar", None, 0, None, "30 s para pelarlo")],
    # viaje (puente, 30-10-2026): una olla con el pollo, la papa y la zanahoria; la res en su cazo
    "viaje-pollo-papa": [O("olla", "pollo", 0, (20, 25), "en trozos pequeños"), O("olla", "papa", 1, (15, 20), "pelada, en trozos"),
                         O("olla", "zanahoria", 2, (15, 20), "pelada, en trozos")],
    "viaje-res-ahuyama": [O("cazo", "carne de res molida", 0, (12, 15), "con un dedo de agua, deshaciéndola con el tenedor, hasta que no quede nada rosado"),
                          O("vapor", "ahuyama", 1, (15, 15), "pelada, en trozos"),
                          O("despues", "pasta", 2, None, "2-3 min más de lo que diga el paquete")],
    "viaje-pollo-pasta": [O("olla", "pollo", 0, (20, 25), "en trozos pequeños"), O("vapor", "calabacín", 2, (6, 8), "con piel, en trozos"),
                          O("despues", "pasta", 1, None, "2-3 min más de lo que diga el paquete")],
    "viaje-res-papa": [O("cazo", "carne de res molida", 0, (12, 15), "con un dedo de agua, deshaciéndola con el tenedor, hasta que no quede nada rosado"),
                       O("olla", "papa", 1, (15, 20), "pelada, en trozos"), O("vapor", "calabacín", 2, (6, 8), "con piel, en trozos")],
    # cenas (26-10-2026)
    "cena-pollo-horno": [O("horno", "bandeja de pollo, papa y zanahoria", t=(25, 30), temp=200)],
    "cena-pasta-pollo": [O("sarten", "daditos de pollo", t=(8, 10), forma="tapada, a fuego medio-bajo"),
                         O("vapor", "calabacín", 2, (6, 8), "en trozos, para la salsa"),
                         O("despues", "pasta", 0, None, "2-3 min más de lo que diga el paquete")],
    "cena-croquetas-pollo": [O("guiso", "pollo", 0, (25, 30), "el muslo entero, en agua que lo cubra"),
                             O("olla", "papa", 1, (15, 20), "pelada, en trozos"),
                             O("horno", "croquetas de pollo", t=(15, 20), temp=200, dep=True)],
    "cena-albondigas-res": [O("guiso", "albóndigas de res en su salsa de zanahoria", 0, (25, 25), "doradas 3-4 min y luego tapadas a fuego suave")],
    "cena-guiso-res": [O("guiso", "guiso de res (la papa y la zanahoria, los últimos 20 min)", 0, (80, 80), "olla a presión: 45 min en total")],
    "cena-pescado-pasta": [O("vapor", "tilapia", 1, (8, 10), "sin espinas"), O("vapor", "calabacín", 2, (6, 8), "en trozos, para la salsa"),
                           O("despues", "pasta", 0, None, "2-3 min más de lo que diga el paquete")],
    "cena-crema-pollo": [O("guiso", "pollo con la papa y el calabacín", 0, (20, 25), "en agua que los cubra justo"),
                         O("tostar", "pan", t=(2, 3), forma="ligeramente")],
    "cena-falafel": [O("horno", "falafel", t=(15, 20), temp=200)],
    "cena-bolitas-batata": [O("guiso", "pollo", 0, (25, 30), "el muslo entero, en agua que lo cubra"),
                            O("vapor", "batata", 1, (15, 20), "pelada, en trozos"),
                            O("horno", "bolitas de batata y pollo", t=(15, 15), temp=200, dep=True)],
    "cena-salmon-batata": [O("vapor", "batata", 1, (15, 15), "pelada, en trozos"), O("vapor", "brócoli", 2, (8, 10), "en arbolitos"),
                           O("vapor", "salmón", 0, (8, 10), "sin piel ni espinas")],
    "cena-arroz-pollo": [O("cazo", "arroz con el pollo y la zanahoria", 0, (20, 20), "el pollo rehogado antes 3-4 min; 4 veces su volumen de agua")],
    "cena-tortilla-papa": [O("vapor", "papa", 1, (10, 12), "en láminas finas"), O("vapor", "calabacín", 2, (10, 12), "en daditos"),
                           O("sarten", "tortilla", t=(8, 10), dep=True, forma="tapada, a fuego bajo, bien cuajada")],
}

NUM = re.compile(r"^(\d+(?:[.,]\d+)?|½|¼|¾)\s+(g|ml|huevos?|unidad(?:es)?)?")
FR = {"½": 0.5, "¼": 0.25, "¾": 0.75}

def _cant(txt, f):
    m = NUM.match(txt or "")
    if not m: return None, None
    v = FR.get(m.group(1)) or float(m.group(1).replace(",", "."))
    u = m.group(2) or ""
    return v * f, ("huevo" if u.startswith("huevo") else u)

def _fmt(v, u):
    if u == "huevo": return f"{v:g} {'huevo' if v == 1 else 'huevos'}"
    return f"{round(v):d} {u}" if u else f"{v:g}"

def _rng(t):
    return f"{t[0]} min" if t[0] == t[1] else f"{t[0]}-{t[1]} min"

def _tareas(plan, fecha, alimentos):
    """Lo que se cocina ese dia: (receta, alimento, titulo, ingredientes ya escalados)."""
    R = plan["recetas"]
    out = []
    def add(rid, k, ings, titulo=None):
        r = R.get(rid)
        if not r: return
        out.append(dict(rid=rid, base=rid.split("~")[0], k=k if "~" not in rid else rid.split("~")[1],
                        titulo=titulo or r["titulo"], ing=ings))
    def escala(rid, c):
        r = R[rid]
        if c.get("ingHoy"): return c["ingHoy"], 1
        return r["ing"], c.get("tandas", 1)
    vistos = set()
    for b in plan["batch"]:
        if b["fecha"] != fecha: continue
        for c in b["cocinar"]:
            ing, f = escala(c["rec"], c)
            add(c["rec"], c["k"], [(x, f) for x in ing], c["titulo"]); vistos.add((c["rec"], c["k"]))
    for c in plan["cocinaDia"]:
        if c["fecha"] != fecha or (c["rec"], c["k"]) in vistos: continue
        ing, f = escala(c["rec"], c)
        add(c["rec"], c["k"], [(x, f) for x in ing], c["titulo"]); vistos.add((c["rec"], c["k"]))
    dia = next((d for d in plan["dias"] if d["fecha"] == fecha), None)
    if dia:
        comidas = defaultdict(set)
        racion = {}
        for col in dia.get("cols", []):
            for it in dia.get(col) or []:
                if not isinstance(it, dict) or not it.get("rec"): continue
                o = it.get("origen") or ""
                if not o.startswith("Cocinar hoy") or "sesión" in o: continue
                clave = it["rec"]
                if any(v[0] == clave for v in vistos): continue
                comidas[clave].add(col)
                if it.get("ingRacion"): racion[clave] = (it["ingRacion"], it.get("k"))
                else: racion.setdefault(clave, (None, it.get("k")))
        for rid, cols in comidas.items():
            n = len(cols)
            ing, k = racion[rid]
            r = R.get(rid)
            if not r: continue
            if ing: add(rid, k, [(x, n) for x in ing])
            else:
                rinde = r.get("rinde") or 1
                veces = -(-n // rinde) if n >= rinde else (int((n / rinde) * 4 + 0.999)) / 4
                add(rid, k, [(x, veces) for x in r["ing"]])
    return out

def orden_dia(plan, fecha, alimentos):
    tareas = _tareas(plan, fecha, alimentos)
    ops = []
    for t in tareas:
        for o in COCCION.get(t["base"], []):
            que = o["que"] or (alimentos[t["k"]]["n"].split(" (")[0].lower() if t["k"] in alimentos else t["titulo"].lower())
            if t["base"] == "verdura-cruda" and t["k"] != "tomate": continue
            tm = o["t"]
            if t["base"] == "verduras-vapor": tm = VAPOR_T.get(t["k"], (10, 12))
            cant = None
            if o["i"] is not None and o["i"] < len(t["ing"]):
                txt, f = t["ing"][o["i"]]
                v, u = _cant(txt, f)
                if v: cant = (v, u)
            ops.append(dict(o, que=que, t=tm, cant=cant, para=t["titulo"]))
    fuego = [o for o in ops if o["m"] != "tostar"]
    if len(fuego) < 2: return None    # una sola cosa: basta su receta

    secciones = []
    olla = [o for o in ops if o["m"] == "olla"]
    vapor = [o for o in ops if o["m"] == "vapor"]
    guiso = [o for o in ops if o["m"] == "guiso"]
    cazo = [o for o in ops if o["m"] == "cazo"]
    despues = [o for o in ops if o["m"] == "despues"]
    escaldar = [o for o in ops if o["m"] == "escaldar"]
    horno = [o for o in ops if o["m"] == "horno"]
    sarten = [o for o in ops if o["m"] == "sarten"]
    tostar = [o for o in ops if o["m"] == "tostar"]

    def junta(lista):
        """Mismo alimento y mismo minuto: una linea con lo de cada receta."""
        g = {}
        for o in lista:
            key = (o["que"], o["t"])
            g.setdefault(key, []).append(o)
        return g

    def linea(key, os_):
        que, tm = key
        partes = []
        total, uni = 0, None
        for o in os_:
            if o["cant"]:
                total += o["cant"][0]; uni = o["cant"][1]
            partes.append((_fmt(*o["cant"]) + " " if o["cant"] else "") + (o["forma"] + " " if o["forma"] else "") + f"→ {o['para']}")
        cab = f"<b>{que}</b>" + (f" ({_fmt(total, uni)})" if uni is not None and len(os_) > 1 else "")
        return cab + ": " + "; ".join(partes)

    # 1) guisos: lo primero, por largos
    pasos = []
    for o in sorted(guiso, key=lambda x: -(x["t"] or (0, 0))[1]):
        pasos.append(f"<b>{o['que'].capitalize()}</b> ({_rng(o['t'])}; {o['forma']}) → {o['para']}.")
    if horno:
        temps = sorted({o["temp"] for o in horno}, reverse=True)
        libres = [o["temp"] for o in horno if not o.get("dep") or not (olla or vapor)]
        tp0 = max(libres) if libres else max(o["temp"] for o in horno)
        pasos.insert(0, f"Enciende el horno a {tp0} °C para que se vaya calentando.")
    if pasos:
        secciones.append(dict(tit="Lo primero", pasos=pasos))

    # 2) olla comun + vaporera encima (si no hay olla, encima del guiso)
    if olla or vapor:
        T = max(o["t"][1] for o in olla + vapor)
        pasos = []
        if olla:
            pasos.append("Una olla grande con agua sin sal (que cubra todo) y, si tienes, la vaporera encima. Cuando hierva, ve metiendo cada cosa a su minuto para que todo acabe a la vez:")
        elif guiso:
            pasos.append("La vaporera, encima de la olla del guiso (tapada): aprovecha su vapor. Ve metiendo cada cosa a su minuto:")
        else:
            pasos.append("Una olla con 3 dedos de agua y la vaporera encima. Cuando hierva, ve metiendo cada cosa a su minuto:")
        por_min = defaultdict(list)
        for key, os_ in junta(olla).items():
            por_min[T - key[1][1]].append(("en el agua", key, os_))
        for key, os_ in junta(vapor).items():
            por_min[T - key[1][1]].append(("en la vaporera", key, os_))
        for mn in sorted(por_min):
            cosas = por_min[mn]
            cab = "Al empezar" if mn == 0 else f"Minuto {mn}"
            for donde, key, os_ in cosas:
                pasos.append(f"{cab}, {donde} ({_rng(key[1])}): {linea(key, os_)}.")
        solo_huevo = all(o["que"] == "huevo" for o in olla + vapor)
        con_pasta = solo_huevo and despues
        if con_pasta:   # el huevo se saca entero: la pasta puede ir a la vez
            pasos.append("A la vez, en la misma agua: " + "; ".join(
                f"<b>{o['que']}</b>" + (f" {_fmt(*o['cant'])}" if o["cant"] else "") + f", {o['forma']} (métela cuando le queden esos minutos al huevo, o sácala después) → {o['para']}" for o in despues) + ".")
        if solo_huevo:
            pasos.append(f"Minuto {T}: saca el huevo a un cuenco con agua fría y pélalo cuando se temple.")
        else:
            pasos.append(f"Minuto {T}: apaga. Comprueba que todo se aplasta entre tus dedos (si algo está duro, unos minutos más solo eso) y saca cada cosa con la espumadera a un plato distinto, separada por receta, como dice arriba."
                         + (" El huevo, a un cuenco con agua fría." if any(o["que"] == "huevo" for o in olla) else "")
                         + " Guarda un poco del agua: sirve para aflojar los chafados.")
        if escaldar:
            pasos.append("Antes de apagar, " + "; ".join(f"<b>{o['que']}</b>: {o['forma']} en el agua hirviendo → {o['para']}" for o in escaldar) + ".")
        if despues and not con_pasta:
            pasos.append(("Después, añade agua hasta media olla y, cuando hierva: " if not olla else "Después, en la misma agua (que vuelva a hervir): ") + "; ".join(
                f"<b>{o['que']}</b>" + (f" {_fmt(*o['cant'])}" if o["cant"] else "") + f", {o['forma']} → {o['para']}" for o in despues) + ".")
        secciones.append(dict(tit="Olla y vaporera (una sola vez)", pasos=pasos))
    elif despues or escaldar:
        pasos = [f"Olla con agua sin sal. Cuando hierva: " + "; ".join(
            f"<b>{o['que']}</b>" + (f" {_fmt(*o['cant'])}" if o["cant"] else "") + f", {o['forma']} → {o['para']}" for o in escaldar + despues) + "."]
        if len(despues + escaldar) > 1: pasos.append("Lo que dure menos, primero, y lo demás en la misma agua.")
        secciones.append(dict(tit="Olla", pasos=pasos))

    # 3) cazos propios
    if cazo:
        pasos = []
        for key, os_ in junta(cazo).items():
            pasos.append(f"{linea(key, os_)}" + (f" ({_rng(key[1])})" if key[1] else "") + ".")
        secciones.append(dict(tit="Aparte, en su cazo", pasos=pasos))

    # 4) horno: una horneada; si hay dos temperaturas, la mas alta primero
    if horno:
        pasos = []
        # Primero lo que puede entrar ya (no espera a la olla); a igualdad, la temperatura mas alta.
        temps = sorted({o["temp"] for o in horno},
                       key=lambda tp: (all(o.get("dep") for o in horno if o["temp"] == tp) and bool(olla or vapor), -tp))
        for n, tp in enumerate(temps):
            grupo = [o for o in horno if o["temp"] == tp]
            libres = [o for o in grupo if not o.get("dep")]
            dep = [o for o in grupo if o.get("dep")]
            txt = "; ".join(f"<b>{o['que']}</b> ({_rng(o['t'])}) → {o['para']}" for o in libres + dep)
            cuando = "En cuanto esté caliente" if n == 0 else f"Al sacar lo anterior, {'baja' if tp < temps[n - 1] else 'sube'} a {tp} °C y mete"
            nota = " (las de masa, cuando tengas lista la papa o la verdura de la olla)" if dep and (olla or vapor) else ""
            juntas = " Van a la vez, en la misma bandeja o en dos alturas; saca cada una a su tiempo." if len(grupo) > 1 else ""
            pasos.append(f"{cuando}{' (a ' + str(tp) + ' °C)' if n == 0 else ''}: {txt}{nota}.{juntas}")
        if len(temps) > 1:
            tmin, tmax = min(temps), max(temps)
            pasos.append(f"Si te caben a la vez, puedes hornearlo todo junto a {tmin} °C: lo de {tmax} °C tardará unos minutos más (sácalo cuando se aplaste entre tus dedos o, si es masa, cuando esté hecho por dentro).")
        secciones.append(dict(tit="Horno (una sola horneada)", pasos=pasos))

    # 5) sarten: una cosa tras otra; lo que lleva alergenos, al final
    if sarten or tostar:
        orden = sorted(sarten, key=lambda o: (o.get("dep", False), "huevo" in o["que"] or "tortit" in o["que"] or "tortilla" in o["que"]))
        pasos = []
        if tostar:
            pasos.append("Primero, con la sartén seca (o en la tostadora): " + "; ".join(f"<b>{o['que']}</b>, {o['forma']} → {o['para']}" for o in tostar) + ".")
        if orden:
            pasos.append(("Después, en la misma sartén, una tras otra (pasa un papel entre una y otra): " if tostar or len(orden) > 1 else "En la sartén: ") + "; ".join(
                f"<b>{o['que']}</b>" + (f" ({o['forma']})" if o["forma"] else "") + f" → {o['para']}" for o in orden) + ".")
        secciones.append(dict(tit="Sartén", pasos=pasos))

    secciones.append(dict(tit="Para terminar", pasos=[
        "Con todo cocinado, termina cada receta (chafar, mezclar, formar, repartir y guardar) siguiendo sus pasos de abajo: salta los de cocer, que ya están hechos."]))
    return secciones

def orden_cocina(plan, desde, alimentos):
    fechas = sorted({d["fecha"] for d in plan["dias"] if d["fecha"] >= desde})
    out = {}
    for f in fechas:
        s = orden_dia(plan, f, alimentos)
        if s: out[f] = s
    return out
