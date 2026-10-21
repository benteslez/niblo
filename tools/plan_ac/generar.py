"""Genera el plan diario de alimentacion complementaria de Pablo y lo escribe
en index.html (bloque pb-plan-data). Uso:

    python3 tools/plan_ac/generar.py            # genera, verifica y escribe
    python3 tools/plan_ac/generar.py --solo-ver # genera y verifica, no escribe

Los dias anteriores a HOY_PLAN se conservan tal cual (son historia). Desde
HOY_PLAN hasta FIN se generan con la pauta de la pediatra:
  7 meses (hasta el 4 nov.): desayuno, media mañana, almuerzo, merienda,
    antes de dormir, noche.
  desde 8 meses (5 nov.): desayuno, media mañana (opcional), almuerzo,
    merienda, cena, noche.
"""
import datetime as dt, json, math, os, re, sys
from collections import defaultdict, Counter

sys.path.insert(0, os.path.dirname(__file__))
from alimentos import ALIMENTOS, ALERGENO_TXT, formato, edad_minima
from recetas import RECETAS, receta_simple, POR_RACION_FRUTA

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INDEX = os.path.join(RAIZ, "index.html")

NACE = dt.date(2026, 3, 5)
INICIO_AC = dt.date(2026, 9, 5)          # dia 1 del plan
HOY_PLAN = dt.date(2026, 10, 21)         # primer dia que se regenera (cenas desde hoy y almuerzos variados, 21-10-2026)
FIN = dt.date(2027, 6, 2)                # ultimo dia del plan (FECHA_FIN en la app)
# Tres comidas (desayuno, almuerzo y cena) desde el 21-10-2026, a peticion de
# la familia (antes, el 5 de noviembre, a los 8 meses). La variable conserva
# el nombre de siempre.
OCHO_MESES = dt.date(2026, 10, 21)
HOTEL = (dt.date(2026, 10, 8), dt.date(2026, 10, 12))
PRIMERA_SESION = dt.date(2026, 10, 12)   # lunes 12: se cocina para el resto de la semana (peticion de la familia)

# Ya introducidos y tolerados (fuente: plan anterior + registros + confirmacion de la familia)
INTRODUCIDOS = ["aguacate", "pollo", "ahuyama", "papa", "trigo_pasta", "pan", "calabacin", "banano",
                "huevo", "zanahoria", "pera", "manzana", "aove", "agua"]

# Cola de introduccion: (clave, comida). Los alergenos nuevos ocupan 3 dias sin
# otro nuevo; el resto, 2 (AEP 2023: 2-3 dias seguidos). Comida "de" o "c":
# nunca la ultima del dia.
COLA = [("res", "c"), ("pescado_blanco", "c"), ("papaya", "de"), ("avena", "de"), ("cacahuete", "de"),
        ("mango", "de"), ("maiz", "de"), ("yogur", "de"), ("yuca", "c"), ("habichuela", "c"),
        ("tahini", "c"), ("lenteja", "c"), ("salmon", "c"), ("pitahaya", "de"), ("almendra", "de"),
        ("brocoli", "c"), ("maranon", "de"), ("queso", "de"), ("nuez", "de"), ("durazno", "de"),
        ("tofu", "c"), ("arroz", "c"), ("camaron", "c"), ("arveja", "c"),
        # de diciembre en adelante
        ("batata", "c"), ("avellana", "de"), ("coliflor", "c"), ("garbanzo", "c"), ("pistacho", "de"),
        ("pimenton", "c"), ("melon", "de"), ("moluscos", "c"), ("quinua", "c"), ("cerdo", "c"),
        ("kiwi", "de"), ("tomate", "c"), ("frijol", "c"), ("apio", "c"), ("berenjena", "c"),
        ("pavo", "c"), ("mandarina", "de"), ("pina", "de"), ("puerro", "c"), ("patilla", "de"),
        ("champinon", "c"), ("chia", "de"), ("fresa", "de"), ("platano_macho", "c"), ("name", "c"),
        ("arandano", "de"), ("guayaba", "de"), ("repollo", "c"), ("arracacha", "c"), ("pepino", "c"),
        ("uva", "de"), ("granadilla", "de"), ("ciruela", "de"), ("breva", "de"), ("atun", "c"),
        ("cebolla", "c"), ("lulo", "de"), ("guanabana", "de"), ("mostaza", "c"), ("espinaca", "c"),
        ("acelga", "c")]

BASE_ALERGENO = {"huevo": "huevo", "trigo_pasta": "gluten", "pan": "gluten", "salmon": "pescado",
                 "queso": "leche", "atun": "pescado"}

def grupo_alergeno(k):
    al = ALIMENTOS[k]["al"]
    if not al:
        return None
    if al == "ya":
        return BASE_ALERGENO[k]
    if al.startswith("ya:"):
        return al[3:]
    return al

def es_alergeno_nuevo(k):
    al = ALIMENTOS[k]["al"]
    if k == "salmon":   # otra especie de pescado: como alergeno nuevo, practica habitual
        return True
    return bool(al) and not al.startswith("ya")

def texto_alergeno(k):
    if k == "salmon": return "pescado (otra especie: salmón o trucha)"
    return ALERGENO_TXT.get(grupo_alergeno(k))

def edad(d):
    m = (d.year - NACE.year) * 12 + d.month - NACE.month
    if d.day < NACE.day:
        m -= 1
    ultimo = dt.date(NACE.year + (NACE.month - 1 + m) // 12, (NACE.month - 1 + m) % 12 + 1, NACE.day)
    return m, (d - ultimo).days

def iso(d): return d.isoformat()
def fecha_txt(d):
    DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    MESES = ["ene.", "feb.", "mar.", "abr.", "may.", "jun.", "jul.", "ago.", "sep.", "oct.", "nov.", "dic."]
    return f"{DIAS[d.weekday()]} {d.day} {MESES[d.month - 1]}"

# ---------------------------------------------------------------- calendario
def calendario():
    """Asigna fecha a cada alimento de la cola. Devuelve lista de
    introducciones y un dict fecha -> (k, dia_de, total, comida)."""
    intro, por_dia = [], {}
    d = HOTEL[1] + dt.timedelta(days=1)
    pendientes = list(COLA)
    while pendientes and d <= FIN:
        meses, _ = edad(d)
        elegido = None
        for i, (k, comida) in enumerate(pendientes):
            if edad_minima(k) <= meses:
                elegido = pendientes.pop(i); break
        if not elegido:
            d += dt.timedelta(days=1); continue
        k, comida = elegido
        total = 3 if es_alergeno_nuevo(k) else 2
        intro.append(dict(k=k, n=ALIMENTOS[k]["n"], id=ALIMENTOS[k]["id"], fecha=iso(d),
                          alergeno=texto_alergeno(k) if es_alergeno_nuevo(k) else None,
                          comida=comida, dias=total))
        for j in range(total):
            por_dia[d + dt.timedelta(days=j)] = (k, j + 1, total, comida)
        d += dt.timedelta(days=total)
    return intro, por_dia

# ---------------------------------------------------------------- menus
# Cantidades en gramos (peticion de la familia, 17-10-2026: «4-6 cucharadas,
# verdura y harina juntas» no servia). Salen de la misma tabla por edad de
# antes (notasMes): ración del plato (verdura + harina), proteína animal y
# legumbre. Conversiones orientativas (práctica habitual, no de una guía):
# 1 cucharada sopera de chafado ≈ 15 g; ½ taza ≈ 120 g; la ración del plato
# se reparte a medias entre verdura y harina. Pesos ya cocinados salvo que
# se diga «en seco» o «en crudo».
PLATO_G = {6: (30, 60), 7: (60, 90), 8: (120, 120), 9: (120, 120), 10: (120, 180), 11: (180, 180), 12: (180, 240)}
ANIMAL_G = {6: (10, 20), 7: (10, 20), 8: (20, 20), 9: (20, 25), 10: (25, 30), 11: (30, 35), 12: (30, 35)}
LEGUMBRE_G = {6: (15, 30), 7: (30, 30), 8: (30, 30), 9: (30, 45), 10: (30, 45), 11: (45, 45), 12: (75, 90)}
# Fruta: peso aproximado de la parte que se come de la ración (pieza mediana).
FRUTA_G = {"banano": 50, "pera": 70, "manzana": 70, "papaya": 80, "mango": 50, "pitahaya": 60, "durazno": 60,
           "melon": 80, "kiwi": 35, "mandarina": 60, "pina": 60, "patilla": 80, "fresa": 35, "arandano": 12,
           "guayaba": 60, "uva": 25, "granadilla": 30, "ciruela": 50, "breva": 40, "lulo": 40, "guanabana": 80}
# Harinas que se pesan en seco: cocidas pesan unas veces mas (practica habitual).
EN_SECO = {"trigo_pasta": ("de pasta", 2.5), "arroz": ("de arroz", 3), "quinua": ("de quinua", 3)}
# Desayunos que van por piezas: peso aproximado de cada pieza segun su receta.
DESAYUNO_CANT = {
    "tortita-trigo": "1-2 tortitas (≈ 25-30 g cada una): ofrece tiras y repón",
    "tortita-avena": "1-2 tortitas (≈ 25-30 g cada una): ofrece tiras y repón",
    "muffins": "½-1 muffin (≈ 30-60 g)",
    "arepa": "½ arepa (≈ 25-30 g), la parte blanda",
    "pan-tostado": "≈ 20 g de pan (1-2 tiras)",
    "avena-formula": "15 g de avena en seco (≈ 100-120 g de papilla)",
}

# Genero del nombre del alimento, para «cocido/cocida».
FEM_CANT = {"zanahoria", "ahuyama", "habichuela", "coliflor", "berenjena", "cebolla", "espinaca", "acelga",
            "arracacha", "yuca", "papa", "trigo_pasta", "quinua", "batata"}
VA_DENTRO = "va dentro de la receta: ya está contado en ella, no se sirve aparte"

def rango(a, b, u="g"):
    return f"≈ {a} {u}" if a == b else f"{a}-{b} {u}"

LEGUMBRES = {"lenteja", "garbanzo", "frijol", "arveja", "tofu"}

def cantidad(k, meses, nuevo_dia, frase_mm=False, slot=None, rec=None):
    a = ALIMENTOS[k]
    m = min(max(meses, 6), 12)
    if nuevo_dia == 1 and es_alergeno_nuevo(k):
        base = "una cantidad pequeña (p. ej. ½ cucharadita o 1-2 trocitos, ≈ 2-5 g)"
        return f"1.er día: {base}; si va bien, días 2 y 3 la ración normal (práctica habitual)"
    if a["cat"] == "gra":
        if k == "aguacate": return "≈ 30 g (2-3 bastones o 2 cucharadas chafado)"
        if k == "chia": return "½ cucharadita (≈ 2 g), remojada ≥30 min"
        if k == "mostaza": return "una punta de cuchillo (≈ 1 g)"
        if k == "aove": return "1 cucharadita (≈ 5 ml)"
        return "½ – 1 cucharadita (≈ 3-5 g)"
    if a["cat"] == "prot":
        if k == "huevo": return "1 huevo (≈ 50 g sin cáscara): ofrece tiras y repón; no tiene por qué acabárselo"
        if k == "yogur": return "2-3 cucharadas (≈ 30-45 g)"
        if k == "queso": return "1-2 cucharadas desmenuzado (≈ 10-20 g) o 2 tiras"
        if k in LEGUMBRES:
            x, y = LEGUMBRE_G[m] if not (k == "tofu" and m == 12) else (30, 45)   # el tofu no se pesa en crudo
            estado = "" if k == "tofu" else (" cocida" if k in ("lenteja", "arveja") else " cocido")
            return f"{rango(x, y)}{estado}" + (" (30 g en crudo)" if m == 12 and k != "tofu" else f" (≈ {round(x/15)}-{max(round(y/15), round(x/15))} cucharadas)".replace(f"≈ {round(x/15)}-{round(x/15)} ", f"≈ {round(x/15)} "))
        x, y = ANIMAL_G[m]
        pieza = {"hamb-pollo": "1 hamburguesita", "hamb-res": "1 hamburguesita", "pescado-tortitas": "1 tortita",
                 "camaron-papa": "1 pastelito", "atun-pastelito": "1 pastelito"}.get(rec)
        return rango(x, y) + (f" (≈ {pieza}; ofrece y repón)" if pieza else " (≈ 1-2 cucharadas desmenuzado)" if y <= 20 else "")
    if a["cat"] == "fru":
        q, u = POR_RACION_FRUTA.get(k, (60, "g"))
        txt = f"{q:g} {u}".replace("0.5 unidad", "½ pieza").replace("0.25 unidad", "¼ de pieza").replace("1 unidad", "1 pieza")
        g = FRUTA_G.get(k)
        if g and u != "g": txt += f" (≈ {g} g)"
        return ("pequeña: " if frase_mm else "") + txt
    if slot == "de" and rec in DESAYUNO_CANT:
        return DESAYUNO_CANT[rec]
    x, y = PLATO_G[m]
    x, y = x // 2, y // 2   # verdura y harina, a medias
    cuch = (round(x / 15), round(y / 15))
    crudo = (rec or "").startswith("verdura-cruda")
    if crudo:   # lo de la receta: unos gajos o un baston para roer
        return "≈ 40 g (2-3 gajos pelados)" if k == "tomate" else "1 bastón grande para roer (≈ 40 g)"
    txt = f"{rango(x, y)} {'crud' if crudo else 'cocid'}{'a' if k in FEM_CANT else 'o'}"
    txt += f" (≈ {cuch[0]}{'-' + str(cuch[1]) if cuch[1] != cuch[0] else ''} cucharada{'s' if cuch[1] > 1 else ''} sopera{'s' if cuch[1] > 1 else ''})"
    if k in EN_SECO:
        nom, f = EN_SECO[k]
        sx, sy = round(x / f / 5) * 5 or 5, round(y / f / 5) * 5 or 5
        txt += f"; en seco, {rango(sx, sy)} {nom}"
    return txt

def item(k, cat=None, rec=None, nombre=None, nota=None):
    a = ALIMENTOS[k]
    return dict(k=k, n=nombre or a["n"], id=a["id"], cat=cat or a["cat"], rec=rec or f"simple-{k}", nota=nota)

# Platos: (receta, [(clave, cat)], requisitos extra)
DESAYUNO_PROT = [  # proteina del desayuno -> items
    ("tortilla-calabacin", [("huevo", "prot")]),
    ("huevo-duro", [("huevo", "prot")]),
    ("yogur-fruta", [("yogur", "prot")]),
    ("simple-queso", [("queso", "prot")]),
    ("pollo-desmenuzado", [("pollo", "prot")]),
]
DESAYUNO_HAR = [
    ("arepa", [("maiz", "har")]), ("pan-tostado", [("pan", "har")]), ("avena-formula", [("avena", "har")]),
    ("tortita-trigo", [("trigo_pasta", "har")]), ("tortita-avena", [("avena", "har")]),
    ("muffins", [("trigo_pasta", "har")]), ("bastones-papa", [("papa", "har")]),
]
CON_HUEVO = {"tortita-trigo", "tortita-avena", "muffins", "tortilla-calabacin", "huevo-duro"}

PROT_MAIN = [
    ("hamb-pollo", "pollo"), ("pollo-desmenuzado", "pollo"), ("hamb-res", "res"), ("res-guisada", "res"),
    ("pescado-crema", "pescado_blanco"), ("pescado-tortitas", "pescado_blanco"), ("pescado-laminas", "pescado_blanco"),
    ("salmon-horno", "salmon"), ("lenteja-chafada", "lenteja"),
    ("hamb-lenteja", "lenteja"), ("tofu-dorado", "tofu"), ("camaron-papa", "camaron"),
    ("pasta-mariscos", "moluscos"), ("hummus", "garbanzo"), ("cerdo-guisado", "cerdo"),
    ("pavo-guisado", "pavo"), ("atun-pastelito", "atun"), ("tortilla-calabacin", "huevo"),
    ("arveja-chafada", "arveja"), ("frijol-chafado", "frijol"),
]
HAR_MAIN = [("bastones-papa", "papa"), ("bastones-yuca", "yuca"), ("pasta-verdura", "trigo_pasta"),
            ("arroz-blando", "arroz"), ("bastones-batata", "batata"), ("quinua-verdura", "quinua"),
            ("tuberculo-cocido", "name"), ("tuberculo-cocido", "arracacha"), ("tuberculo-cocido", "platano_macho")]
VER_MAIN = {"calabacin": "verduras-vapor", "zanahoria": "verduras-vapor", "habichuela": "verduras-vapor",
            "brocoli": "verduras-vapor", "coliflor": "verduras-vapor", "repollo": "verduras-vapor",
            "ahuyama": "ahuyama-asada", "pimenton": "verdura-asada", "berenjena": "verdura-asada",
            "tomate": "verdura-cruda", "pepino": "verdura-cruda", "apio": "verdura-en-guiso",
            "puerro": "verdura-en-guiso", "champinon": "verdura-en-guiso", "cebolla": "verdura-en-guiso",
            "espinaca": "verdura-en-guiso", "acelga": "verdura-en-guiso"}
FRUTAS = [k for k, a in ALIMENTOS.items() if a["cat"] == "fru"]
NUECES = ["cacahuete", "tahini", "almendra", "maranon", "nuez", "avellana", "pistacho"]
GUISOS = {"pollo-desmenuzado", "res-guisada", "cerdo-guisado", "pavo-guisado", "hamb-pollo", "hamb-res", "lenteja-chafada"}

def requiere_ok(rec, disp):
    r = RECETAS.get(rec)
    return r is None or r["requiere"] <= disp

class Historia:
    def __init__(self):
        self.dias = []   # lista de (fecha, dict slot -> set de claves de plato, set de grupos alergeno, set alimentos)
    def usado(self, slot, clave, ultimos):
        return sum(1 for f, s, g, a in self.dias[-ultimos:] if clave in s.get(slot, set()))
    def usado_dia(self, clave, ultimos):
        return sum(1 for f, s, g, a in self.dias[-ultimos:] if any(clave in v for v in s.values()))
    def grupo(self, g, ultimos):
        return sum(1 for f, s, gs, a in self.dias[-ultimos:] if g in gs)
    def alimento(self, k, ultimos):
        return sum(1 for f, s, g, al in self.dias[-ultimos:] if k in al)

def grupos_de_items(items):
    gs = set()
    for it in items:
        g = grupo_alergeno(it["k"]) if it["k"] in ALIMENTOS else None
        if g: gs.add(g)
        r = RECETAS.get(it["rec"])
        if r:
            for k in r["requiere"]:
                g = grupo_alergeno(k)
                if g: gs.add(g)
    return gs

def elegir(cands, puntua):
    mejor, mp = None, None
    for c in cands:
        p = puntua(c)
        if p is None: continue
        if mp is None or p > mp:
            mejor, mp = c, p
    return mejor

GENERICAS = {"verduras-vapor", "verdura-asada", "verdura-en-guiso", "verdura-cruda", "tuberculo-cocido"}
CADUCA_CONGELADO = 30   # dias (practica habitual)

class Batch:
    """Lo cocinado en cada sesion y lo que queda: cada tanda deja raciones en
    la nevera (hasta el dia siguiente: 48 h) o en el congelador (1 mes). Los
    menus gastan primero lo que ya hay.
    Un alimento no se cocina en una sesion anterior a su primer dia (si da
    reaccion, se tiraria todo): el primer dia se cocina la receta entera,
    recien hecha, y lo que sobra (nevera 48 h o congelador) cubre los dias
    siguientes; lo mismo si la sesion de la semana fue antes del estreno."""
    def __init__(self, estrenos=None):
        self.ses = sesiones()
        self.estrenos = estrenos or {}     # k -> fecha del primer dia
        self.stock = defaultdict(list)    # clave -> [{ses, quedan, dia}]
        self.tareas = defaultdict(dict)   # ses -> clave -> {...}
        self.cocina_dia = defaultdict(dict)   # dia -> clave -> {...}: recetas enteras cocinadas ese dia
        self.descongelar = defaultdict(list)
    def clave(self, rec, k):
        return f"{rec}|{k}" if rec in GENERICAS else rec
    def sesion(self, d):
        c = [x for x in self.ses if x <= d]
        return c[-1] if c else None
    def _usable(self, lote, d, r):
        gap = (d - lote["ses"]).days
        return lote["quedan"] > 0 and (gap <= 1 or (r["congela"] and gap <= CADUCA_CONGELADO))
    def disponible(self, rec, k, d):
        r = RECETAS.get(rec or "")
        if not r or not r["batch"]:
            return False
        return any(self._usable(l, d, r) for l in self.stock[self.clave(rec, k)])
    def consumir(self, it, d, fresco=False):
        rec = it.get("rec")
        r = RECETAS.get(rec or "")
        if not r:
            if rec: it["origen"] = "Preparar al momento"
            return
        S = self.sesion(d)
        if not r["batch"] or S is None:
            it["origen"] = "Cocinar hoy"
            return
        clave = self.clave(rec, it["k"])
        # El estreno de CUALQUIER ingrediente de la receta cuenta: las tortitas
        # de avena llevan huevo y el plato se apuntaba por el huevo, asi que
        # entraban en una sesion anterior al primer dia de la avena.
        estreno = max([self.estrenos[x] for x in (r["requiere"] | {it["k"]}) if x in self.estrenos], default=None)
        lotes = [] if fresco else [l for l in self.stock[clave] if self._usable(l, d, r)]
        if lotes:
            lote = lotes[0]
        elif (fresco and S != d) or (estreno and S < estreno):
            # receta entera hoy: lo que sobre, para los dias siguientes
            lote = dict(ses=d, quedan=r["rinde"], dia=True)
            self.stock[clave].append(lote)
            t = self.cocina_dia[d].setdefault(clave, dict(rec=rec, k=it["k"], tandas=0, raciones=0, dias=[], congelar=0))
            t["tandas"] += 1
        else:
            if (d - S).days >= 2 and not r["congela"]:
                it["origen"] = "Cocinar hoy"; return
            lote = dict(ses=S, quedan=r["rinde"])
            self.stock[clave].append(lote)
            t = self.tareas[S].setdefault(clave, dict(rec=rec, k=it["k"], tandas=0, raciones=0, dias=[], congelar=0))
            t["tandas"] += 1
        lote["quedan"] -= 1
        gap = (d - lote["ses"]).days
        t = (self.cocina_dia if lote.get("dia") else self.tareas)[lote["ses"]][clave]
        t["raciones"] += 1
        if iso(d) not in t["dias"]: t["dias"].append(iso(d))
        cuando = fecha_txt(lote["ses"])
        if lote.get("dia"):
            if gap == 0:
                it["origen"] = ("Cocinar hoy: el primer día de un alimento nuevo, recién hecho" if fresco
                                else "Cocinar hoy (la receta entera: sobra para otros días)")
                it["lote"] = "dia"
            elif gap == 1:
                it["origen"] = f"Sobra de lo cocinado el {cuando}: en la nevera"
            else:
                t["congelar"] += 1
                it["origen"] = f"Sobra de lo cocinado el {cuando}: sacar del congelador la noche anterior"
                self.descongelar[iso(d - dt.timedelta(days=1))].append(titulo_clave(rec, it["k"]))
            return
        if gap == 0:
            it["origen"] = "Cocinar hoy (sesión de cocina; primer día de un alimento nuevo)" if fresco else "Cocinar hoy (sesión de cocina)"
        elif gap == 1:
            it["origen"] = f"Del batch del {cuando}: en la nevera"
        else:
            t["congelar"] += 1
            it["origen"] = f"Del batch del {cuando}: sacar del congelador la noche anterior"
            self.descongelar[iso(d - dt.timedelta(days=1))].append(titulo_clave(rec, it["k"]))

def titulo_clave(rec, k):
    t = RECETAS[rec]["titulo"]
    return f"{t}: {ALIMENTOS[k]['n'].lower()}" if rec in GENERICAS else t

def semilla_historia(historia):
    """Los ultimos 7 dias conservados entran en la historia, para que lo de
    hoy no repita lo de ayer. Ademas, lo que la familia dice que comio de
    verdad (COMIDO) sustituye al almuerzo del plan."""
    out = []
    for e in historia[-7:]:
        if e.get("v") != 2: continue
        slots, al = defaultdict(set), set()
        for col in e.get("cols", []):
            for i in e.get(col, []) or []:
                if not isinstance(i, dict) or i.get("k") not in ALIMENTOS: continue
                al.add(i["k"])
                rec = (i.get("rec") or "").split("~")[0]
                if col in ("c", "ce"):
                    if i["cat"] == "prot": slots[col + "-prot"].add(rec)
                    elif i["cat"] in ("har", "ver"): slots[col + "-" + i["cat"]].add(i["k"])
                elif col == "de" and i["cat"] in ("har", "prot"):
                    slots["de-" + i["cat"]].add(rec)
                r = RECETAS.get(rec)
                if r: al |= r["requiere"]
        f = dt.date.fromisoformat(e["fecha"])
        if iso(f) in COMIDO:
            for slot, v in COMIDO[iso(f)].items(): slots[slot] = set(v)
            al |= COMIDO_AL
        gs = {grupo_alergeno(k) for k in al if grupo_alergeno(k)}
        out.append((f, dict(slots), gs, al))
    return out

# Lo que comio de verdad (la familia, 21-10-2026): tres dias seguidos las
# hamburguesitas de pollo con ahuyama, zanahoria, pasta y aguacate.
COMIDO = {f: {"c-prot": {"hamb-pollo"}, "c-har": {"trigo_pasta"}, "c-ver": {"zanahoria"}}
          for f in ("2026-10-18", "2026-10-19", "2026-10-20")}
COMIDO_AL = {"pollo", "ahuyama", "zanahoria", "trigo_pasta", "aguacate"}
# Descanso tras esos tres dias: hasta esa fecha (incluida) no vuelven al
# almuerzo ni a la cena.
# Tilapia (pescado_blanco): fuera del 21 al 23-10, a peticion de la familia
# (21-10-2026); vuelve desde el 24. Para que la cena tenga proteina esos dias,
# el pollo vuelve ya (en guiso); la hamburguesita de pollo sigue en descanso.
DESCANSO = {"hamb-pollo": "2026-10-27", "pescado_blanco": "2026-10-23", "trigo_pasta": "2026-10-21",
            "zanahoria": "2026-10-22", "aguacate": "2026-10-22"}
def descansa(clave, d):
    return iso(d) <= DESCANSO.get(clave, "")

def generar_menus(intro, por_dia, batch, semilla=()):
    fecha_intro = {x["k"]: dt.date.fromisoformat(x["fecha"]) for x in intro}
    hist = Historia()
    hist.dias = list(semilla)
    dias = []
    d = HOY_PLAN
    while d <= FIN:
        meses, sem_dias = edad(d)
        nuevo = por_dia.get(d)
        # disponibles: introducidos antes de hoy (el nuevo solo en su comida)
        disp = set(INTRODUCIDOS) | {k for k, f in fecha_intro.items() if f < d}
        if nuevo:
            disp.discard(nuevo[0])
        ocho = d >= OCHO_MESES
        hotel = HOTEL[0] <= d <= HOTEL[1]
        slots = defaultdict(set)   # para la historia
        huevos = 0
        dia_items = {}
        reqgrupo = {}   # deficit de alergenos ya introducidos: grupo -> veces en 6 dias previos
        introducidos_grupos = {grupo_alergeno(k) for k in disp if grupo_alergeno(k)}
        for g in introducidos_grupos:
            reqgrupo[g] = hist.grupo(g, 6)
        def deficit(gs):
            return sum(1 for g in gs if reqgrupo.get(g, 9) < 2)

        frutas_hoy = []
        usados_gra = set()
        def fruta(slot, mm=False, forzada=None):
            if forzada:
                k = forzada
            else:
                vale = lambda f: f in disp and edad_minima(f) <= meses and not (hotel and f == "manzana")
                cands = [f for f in FRUTAS if vale(f) and f not in frutas_hoy]
                if not cands:
                    cands = [f for f in FRUTAS if vale(f)]
                def p(f):
                    s = -3 * hist.alimento(f, 2) - hist.alimento(f, 6)
                    g = grupo_alergeno(f)
                    if g and reqgrupo.get(g, 9) < 2: s += 6
                    return s
                k = elegir(sorted(cands), p)
            frutas_hoy.append(k)
            it = item(k, "fru", f"simple-{k}")
            if hotel: it["nota"] = "Cómprala madura y córtala en la habitación con tu cuchillo."
            return it

        def nuevo_en(slot):
            return nuevo and nuevo[3] == slot and nuevo[0]

        # ---------------- desayuno
        de = []
        nk = nuevo_en("de")
        if hotel:
            de += [item("huevo", "prot", "huevo-duro", "Huevo duro (pídelo en la cocina del hotel, bien cocido)"),
                   item("papa", "har", "hotel-cocina", "Papa cocida sin sal (cocina del hotel)") if d.day % 2 == 0
                   else item("trigo_pasta", "har", "hotel-cocina", "Pasta cocida solo en agua, sin sal (cocina del hotel)"),
                   fruta("de")]
            huevos += 1
        else:
            fr_nueva = nk if nk and ALIMENTOS[nk]["cat"] == "fru" else None
            har_forzada = nk if nk and ALIMENTOS[nk]["cat"] == "har" else None
            prot_forzada = nk if nk and ALIMENTOS[nk]["cat"] == "prot" else None
            # harina
            def p_har(c):
                rec, its = c
                if not requiere_ok(rec, disp | ({har_forzada} if har_forzada else set())): return None
                if har_forzada and its[0][0] != har_forzada: return None
                if any(k not in disp and k != har_forzada for k, _ in its): return None
                s = -4 * hist.usado("de-har", rec, 2) - hist.usado("de-har", rec, 6) + (3 if batch.disponible(rec, its[0][0], d) else 0)
                if rec == "bastones-papa": s -= 8   # la papa ya sale mucho en almuerzo y cena
                s += 2 * deficit(grupos_de_items([item(k, c2, rec) for k, c2 in its]))
                return s
            hr = elegir(DESAYUNO_HAR, p_har)
            NOMBRE_HAR = {"tortita-trigo": "Tortita (pancake) de banano y harina de trigo", "tortita-avena": "Tortita de avena y banano",
                          "muffins": "Muffin jugoso de zanahoria, manzana y banano (harina de trigo)", "avena-formula": "Avena con fórmula",
                          "pan-tostado": "Pan sin sal tostado (trigo)", "arepa": "Arepa de maíz casera sin sal"}
            har_items = [item(k, c2, hr[0], NOMBRE_HAR.get(hr[0])) for k, c2 in hr[1]]
            con_huevo = hr[0] in CON_HUEVO
            # proteina
            def p_prot(c):
                rec, its = c
                k = its[0][0]
                if prot_forzada and k != prot_forzada: return None
                if not prot_forzada and k not in disp: return None
                if not requiere_ok(rec, disp | ({prot_forzada} if prot_forzada else set())): return None
                if k == "huevo" and con_huevo: return None
                s = -4 * hist.usado("de-prot", rec, 2) - hist.usado("de-prot", rec, 5) + (3 if batch.disponible(rec, k, d) else 0)
                g = grupo_alergeno(k)
                if g and reqgrupo.get(g, 9) < 2: s += 5
                if rec == "pollo-desmenuzado": s -= 4
                return s
            if con_huevo and not prot_forzada:
                prot_items = [item("huevo", "prot", hr[0], "Huevo (va dentro de la " + ("tortita" if "tortita" in hr[0] else "masa del muffin") + ")")]
            else:
                pr = elegir(DESAYUNO_PROT, p_prot)
                prot_items = [item(k, c2, pr[0]) for k, c2 in pr[1]]
            if any(i["k"] == "huevo" for i in prot_items): huevos += 1
            de += prot_items + har_items
            slots["de-har"].add(hr[0]); slots["de-prot"].add(prot_items[0]["rec"])
            de.append(fruta("de", forzada=fr_nueva))
            # grasa: fruto seco nuevo o de mantenimiento, o aguacate
            gra = nk if nk and ALIMENTOS[nk]["cat"] == "gra" else None
            # frutos secos de mantenimiento: hasta dos, ya tolerados por separado
            # (practica habitual: mantenerlos 2 o mas veces por semana)
            gras = [gra] if gra else []
            if not gra:
                cands = [k for k in NUECES if k in disp and k != "tahini"]
                def p_gra(k):
                    g = grupo_alergeno(k)
                    if g and reqgrupo.get(g, 9) < 2 and k not in gras: return 10 - reqgrupo.get(g, 0) - hist.alimento(k, 2)
                    return None
                for _ in range(2):
                    x = elegir(sorted(cands), p_gra)
                    if x: gras.append(x)
                if "chia" in disp and hist.alimento("chia", 2) == 0 and len(gras) < 2:
                    gras.append("chia")
            for gk in gras:
                de.append(item(gk, "gra", "crema-fruto-seco" if gk != "chia" else "simple-chia",
                               nota=("Remojada ≥30 min, sin grumos, en la avena o el yogur." if gk == "chia" else
                                     "En la avena, el yogur o untada en capa finísima sobre una tira de pan o tortita.")))
                usados_gra.add(gk)
            if not gras and hist.alimento("aguacate", 2) == 0:
                de.append(item("aguacate", "gra", "simple-aguacate"))
        dia_items["de"] = de

        # ---------------- media mañana
        # Frutas: hasta el 4 nov., dos (desayuno y almuerzo, de postre); desde
        # el 5 nov., tres (desayuno, merienda y cena), como indico la pediatra.
        dia_items["mm"] = []

        # ---------------- almuerzo / cena
        def principal(slot, evita_prot=None):
            its = []
            nk = nuevo_en(slot)
            if hotel:
                its = [item("pollo", "prot", "hotel-cocina", "Pollo cocido o a la plancha sin sal ni adobo (cocina del hotel)"),
                       item("trigo_pasta", "har", "hotel-cocina", "Pasta cocida solo en agua, sin sal ni mantequilla (cocina del hotel)") if d.day % 2 == 0
                       else item("papa", "har", "hotel-cocina", "Papa cocida sin sal (cocina del hotel)"),
                       item(["zanahoria", "calabacin", "ahuyama"][d.day % 3], "ver", "hotel-cocina",
                            ALIMENTOS[["zanahoria", "calabacin", "ahuyama"][d.day % 3]]["n"] + " al vapor sin sal (cocina del hotel)"),
                       item("aguacate", "gra", "simple-aguacate")]
                return its
            fz = {ALIMENTOS[nk]["cat"]: nk} if nk else {}
            if nk and ALIMENTOS[nk]["cat"] == "gra":
                fz = {"gra": nk}
            # proteina
            nonlocal_huevos = huevos
            def p_prot(c):
                rec, k = c
                if "prot" in fz and k != fz["prot"]: return None
                if "prot" not in fz and k not in disp: return None
                ok = disp | ({fz["prot"]} if "prot" in fz else set())
                if not requiere_ok(rec, ok): return None
                if k == "huevo" and nonlocal_huevos >= 1: return None
                if evita_prot and k == evita_prot: return None
                if (descansa(rec, d) or descansa(k, d)) and "prot" not in fz: return None
                if k in ("arroz",) : return None
                if "har" in fz and rec in ("camaron-papa", "pasta-mariscos", "pescado-tortitas"): return None
                if k == "atun" and "prot" not in fz and hist.alimento("atun", 7) >= 1: return None   # ocasional
                # El mismo alimento dias seguidos (aunque cambie la receta) pesa mas.
                s = -5 * hist.usado(slot + "-prot", rec, 2) - 2 * hist.usado_dia(rec, 3) - 3 * hist.alimento(k, 2) - hist.alimento(k, 4) - 0.7 * hist.alimento(k, 14)
                if batch.disponible(rec, k, d): s += 3
                # Varias recetas del mismo alimento (tilapia): que roten en la semana.
                if sum(1 for r_, k_ in PROT_MAIN if k_ == k) > 1: s -= 2 * hist.usado_dia(rec, 7)
                g = grupo_alergeno(k)
                if g and reqgrupo.get(g, 9) < 2: s += 6
                if g and reqgrupo.get(g, 9) >= 2: s -= 2
                return s
            def arroz_semana():
                return hist.alimento("arroz", 6) + (1 if "arroz" in usados_hoy else 0)
            pr = elegir(PROT_MAIN, p_prot)
            if pr is None:
                raise SystemExit(f"Sin proteína para {d} {slot}: nuevo={nk} fz={fz} disp={sorted(disp)}")
            rec, kp = pr
            its.append(item(kp, "prot", rec))
            usados_hoy.add(kp)
            COMBO = {"camaron-papa": ("papa", "Papa (va en los pastelitos)"), "pasta-mariscos": ("trigo_pasta", "Pasta (va en la misma receta)"),
                     "pescado-tortitas": ("papa", "Papa (va en las tortitas)")}
            if rec in COMBO:
                its.append(item(COMBO[rec][0], "har", rec, COMBO[rec][1]))
                usados_hoy.add(COMBO[rec][0])
            else:
                def p_har(c):
                    rec2, k = c
                    if "har" in fz and k != fz["har"]: return None
                    if "har" not in fz and k not in disp: return None
                    if k == "arroz" and arroz_semana() >= 3: return None
                    if descansa(k, d) and "har" not in fz: return None
                    if edad_minima(k) > meses: return None
                    s = -5 * hist.usado(slot + "-har", k, 2) - hist.alimento(k, 4) + (3 if batch.disponible(rec2, k, d) else 0)
                    if k in usados_hoy: s -= 4
                    return s
                hr = elegir(HAR_MAIN, p_har)
                its.append(item(hr[1], "har", hr[0]))
                usados_hoy.add(hr[1])
            # verduras: una (dos desde los 9 meses, una de ellas "en guiso" si toca)
            cands = [k for k in VER_MAIN if (k in disp or fz.get("ver") == k) and edad_minima(k) <= meses]
            def p_ver(k):
                if "ver" in fz: return 100 if k == fz["ver"] else None
                if descansa(k, d): return None
                s = -5 * hist.usado(slot + "-ver", k, 2) - hist.alimento(k, 4) + (2 if batch.disponible(VER_MAIN[k], k, d) else 0)
                if k in usados_hoy: s -= 6
                g = grupo_alergeno(k)
                if g and reqgrupo.get(g, 9) < 2: s += 6
                if k in ("espinaca", "acelga") and hist.alimento("espinaca", 1) + hist.alimento("acelga", 1): return None
                return s
            vk = elegir(sorted(cands), p_ver)
            its.append(item(vk, "ver", VER_MAIN[vk])); usados_hoy.add(vk)
            if meses >= 9 and "ver" not in fz:
                cands2 = [k for k in cands if k != vk]
                vk2 = elegir(sorted(cands2), p_ver)
                if vk2:
                    its.append(item(vk2, "ver", VER_MAIN[vk2])); usados_hoy.add(vk2)
            # grasa: alergeno nuevo de grasa, tahini/mostaza de mantenimiento, o aguacate
            if "gra" in fz:
                its.append(item(fz["gra"], "gra", "crema-fruto-seco" if fz["gra"] == "tahini" else
                                ("mostaza-punta" if fz["gra"] == "mostaza" else f"simple-{fz['gra']}"),
                                nota="Tahini: ½ cucharadita en capa finísima sobre los bastones de ahuyama o diluida en el puré." if fz["gra"] == "tahini" else None))
            else:
                opciones = [("tahini", "crema-fruto-seco"), ("mostaza", "mostaza-punta")] + [(n, "crema-fruto-seco") for n in NUECES if n != "tahini"]
                for g_k, rec_g in opciones:
                    if g_k in disp and reqgrupo.get(grupo_alergeno(g_k), 9) < 2 and hist.alimento(g_k, 2) == 0 and g_k not in usados_hoy and g_k not in usados_gra:
                        its.append(item(g_k, "gra", rec_g, nota="En capa finísima sobre los bastones de verdura o diluida en el puré." if rec_g == "crema-fruto-seco" else None))
                        usados_hoy.add(g_k); usados_gra.add(g_k); reqgrupo[grupo_alergeno(g_k)] = reqgrupo.get(grupo_alergeno(g_k), 0) + 1; break
                else:
                    if "aguacate" not in usados_hoy and hist.alimento("aguacate", 1) == 0 and not descansa("aguacate", d):
                        its.append(item("aguacate", "gra", "simple-aguacate")); usados_hoy.add("aguacate")
            slots[slot + "-prot"].add(rec); slots[slot + "-har"].add(its[1]["k"]); slots[slot + "-ver"].add(vk)
            return its

        usados_hoy = set(i["k"] for i in de)
        dia_items["c"] = principal("c")
        if not ocho:
            dia_items["c"].append(fruta("c"))
        huevos += sum(1 for i in dia_items["c"] if i["k"] == "huevo")
        # ---------------- merienda
        dia_items["me"] = [fruta("me")] if ocho else []
        if ocho:
            prot_c = dia_items["c"][0]["k"]
            ce = principal("ce", evita_prot=prot_c)
            ce.append(fruta("ce"))
            dia_items["ce"] = ce
            cols = ["de", "mm", "c", "me", "ce", "no"]
        else:
            dia_items["ad"] = []
            cols = ["de", "mm", "c", "me", "ad", "no"]
        dia_items["no"] = []

        # de donde sale cada preparacion (el primer dia de un alimento nuevo, recien hecho)
        if not hotel:
            for s_ in ("de", "c", "ce"):
                hecho = {}   # una racion por preparacion y comida, aunque la compartan dos alimentos
                for i in dia_items.get(s_, []):
                    if i.get("rec") in hecho:
                        i["origen"] = hecho[i["rec"]]; continue
                    fresco = bool(nuevo and nuevo[0] == i["k"] and nuevo[1] == 1)
                    batch.consumir(i, d, fresco)
                    if i.get("rec") in SIMPLES and (i.get("origen") or "") == "Cocinar hoy":
                        i["ingRacion"] = ing_hoy_txt(i["rec"], i["k"], 1, [iso(d)])
                    if i.get("rec") and i["rec"] not in GENERICAS: hecho[i["rec"]] = i.get("origen")
            for s_ in ("mm", "me"):
                for i in dia_items.get(s_, []):
                    batch.consumir(i, d)
        else:
            for s_ in dia_items:
                for i in dia_items[s_]:
                    if i.get("rec") == "hotel-cocina" or i.get("rec") == "huevo-duro": i["origen"] = "Cocina del hotel"
                    elif i.get("rec"): i["origen"] = "Sin cocinar: cortar en la mesa"
        # agua en las comidas principales
        for s in ("de", "c", "ce"):
            if s in dia_items:
                dia_items[s].append(item("agua", "agua", None))
                dia_items[s][-1]["rec"] = None

        # historia
        todos = [i for s in dia_items.values() for i in s]
        gs = grupos_de_items([i for i in todos if i["k"] != "agua"])
        if nuevo: gs.discard(grupo_alergeno(nuevo[0]))
        al = set(i["k"] for i in todos)
        for i in todos:
            r = RECETAS.get(i["rec"] or "")
            if r: al |= r["requiere"]
        hist.dias.append((d, dict(slots), gs, al))

        entrada = dict(v=2, fecha=iso(d), d=(d - INICIO_AC).days + 1, m=meses, cols=cols,
                       nuevo=None, pri=False, nuevoId=None, hotel=hotel)
        if nuevo:
            k, dn, tot, comida = nuevo
            entrada.update(nuevo=ALIMENTOS[k]["n"], nuevoId=ALIMENTOS[k]["id"], nuevoK=k, pri=dn == 1,
                           nuevoDia=dn, nuevoTotal=tot, nuevoComida=comida,
                           alergeno=texto_alergeno(k) if es_alergeno_nuevo(k) else None)
        for s in cols:
            its = dia_items.get(s, [])
            for i in its:
                if i["k"] != "agua":
                    i["cant"] = cantidad(i["k"], meses, nuevo[1] if nuevo and nuevo[0] == i["k"] else 0, frase_mm=(s == "mm"), slot=s, rec=i.get("rec"))
                    if "(va " in i["n"]: i["cant"] = VA_DENTRO
                    if nuevo and nuevo[0] == i["k"]:
                        i["nuevo"] = True
                        i["nuevoDia"] = nuevo[1]
            entrada[s] = its
        dias.append(entrada)
        d += dt.timedelta(days=1)
    return dias

# ---------------------------------------------------------------- batch
def sesiones():
    out = [PRIMERA_SESION]
    # Tras la primera (lunes 12, para el resto de esa semana), una sola sesion por semana,
    # el domingo, para toda la semana (domingo a sabado): domingo y lunes de la
    # nevera (48 h) y de martes a sabado del congelador. Lo que no se congela
    # (receta con congela=False) se cocina el mismo dia (peticion de la familia).
    d = dt.date(2026, 10, 18)
    while d <= FIN:
        if d.weekday() == 6:   # domingo
            out.append(d)
        d += dt.timedelta(days=1)
    out.append(dt.date(2026, 10, 21))   # mie 21: de hoy al sabado (peticion de la familia)
    return sorted(out)

# ---------------------------------------------------------------- cuanto cocinar
# Recetas de un solo alimento (papa, yuca, batata, tuberculos, verdura,
# ahuyama, pasta, arroz): lo que se cocina sale de la RACION de ese dia (la
# misma que dice «Cuánto»), pasada a peso en crudo o en seco, y no de la
# cantidad fija de la receta, que no crecia con la edad (peticion de la
# familia, 21-10-2026: «150 g de papa para 2 raciones de 30-45 g»).
# Factores orientativos (practica habitual): papa, yuca y tuberculos cocidos
# en agua pesan casi lo mismo que en crudo pelados; la verdura al vapor
# pierde ~10 %; asada (ahuyama, batata, pimenton, berenjena) ~25-30 %;
# la pasta cocida pesa ~2,5 veces su peso en seco y el arroz ~3.
SIMPLES = {"bastones-papa": ("papa", "pelada", 1.0), "bastones-yuca": ("yuca", "pelada y sin la fibra central", 1.0),
           "bastones-batata": ("batata", "pelada", 1.3), "tuberculo-cocido": (None, "pelado", 1.0),
           "verduras-vapor": (None, "", 1.1), "ahuyama-asada": ("ahuyama", "pelada y sin pepas", 1.3),
           "verdura-asada": (None, "", 1.3), "pasta-verdura": ("pasta corta (fusilli, conchitas)", "en seco", 1 / 2.5),
           "arroz-blando": ("arroz", "en seco", 1 / 3)}

def racion_cruda(rec, d):
    m, _ = edad(d)
    _, y = PLATO_G[min(max(m, 6), 12)]
    return max(5, int(round(y / 2 * SIMPLES[rec][2] / 5.0)) * 5)

def ing_cocinar(rec, k, raciones, fechas):
    """[(producto, gramos, 'g', seccion), ...] de lo que hay que cocinar, y la racion media."""
    r = RECETAS[rec]
    porr = [racion_cruda(rec, dt.date.fromisoformat(f)) for f in fechas] or [racion_cruda(rec, HOY_PLAN)]
    media = sum(porr) / len(porr)
    nombre = SIMPLES[rec][0] or ALIMENTOS[k]["n"].split(" (")[0].lower()
    sec = r["ing"][0][3] or "Frutas y verduras"
    total = int(round(media * raciones / 5.0)) * 5 or 5
    otros = [(p, c * raciones / r["rinde"], u, s2) for p, c, u, s2 in r["ing"][1:]]
    return [(nombre, total, "g", sec)] + otros, media

def ing_hoy_txt(rec, k, raciones, fechas):
    ings, media = ing_cocinar(rec, k, raciones, fechas)
    (nombre, total, _, _), otros = ings[0], ings[1:]
    estado = SIMPLES[rec][1]
    if estado == "pelado" and k in FEM: estado = "pelada"
    if estado == "en seco":
        prim = f"{total} g de {nombre}, en seco"
    else:
        prim = f"{total} g de {nombre}{' ' + estado if estado else ''}, en crudo"
    if raciones > 1: prim += f" ({raciones} raciones de ≈ {int(round(media / 5.0)) * 5} g)"
    def ot(p, c, u):
        if u in ("cucharadita", "cucharada"):
            c = max(0.5, round(c * 2) / 2)
        return ing_txt(p, c, u)
    return [prim] + [ot(p, c, u) for p, c, u, _ in otros]

def plan_batch(dias, batch):
    out = []
    for S in batch.ses:
        t = batch.tareas.get(S)
        if not t: continue
        cocinar = []
        for clave, x in sorted(t.items(), key=lambda kv: titulo_clave(kv[1]["rec"], kv[1]["k"])):
            r = RECETAS[x["rec"]]
            e = dict(rec=x["rec"], k=x["k"], titulo=titulo_clave(x["rec"], x["k"]), raciones=x["raciones"],
                     tandas=x["tandas"], rinde=r["rinde"], dias=x["dias"], congelar=x["congelar"],
                     sobran=x["tandas"] * r["rinde"] - x["raciones"])
            if x["rec"] in SIMPLES:
                e.update(ingHoy=ing_hoy_txt(x["rec"], x["k"], x["raciones"], x["dias"]), sobran=0)
            cocinar.append(e)
        out.append(dict(fecha=iso(S), cocinar=cocinar))
    return out

def plan_cocina_dia(batch):
    out = []
    for d in sorted(batch.cocina_dia):
        for clave, x in sorted(batch.cocina_dia[d].items()):
            r = RECETAS[x["rec"]]
            e = dict(fecha=iso(d), rec=x["rec"], k=x["k"], titulo=titulo_clave(x["rec"], x["k"]), raciones=x["raciones"],
                     tandas=x["tandas"], rinde=r["rinde"], dias=x["dias"], congelar=x["congelar"],
                     sobran=x["tandas"] * r["rinde"] - x["raciones"])
            if x["rec"] in SIMPLES:
                e.update(ingHoy=ing_hoy_txt(x["rec"], x["k"], x["raciones"], x["dias"]), sobran=0)
            out.append(e)
    return out

def marcar_dias(dias, batch, out):
    for e in dias:
        if e["fecha"] in batch.descongelar:
            e["descongelar"] = sorted(set(batch.descongelar[e["fecha"]]))
        if any(b["fecha"] == e["fecha"] for b in out):
            e["sesion"] = True
    return out

# ---------------------------------------------------------------- compra
CANON = {"calabacín rallado": "calabacín", "calabacín (zucchini)": "calabacín", "banano maduro": "banano",
         "banano (plátano)": "banano", "papa (patata)": "papa", "papa cocida": "papa", "zanahoria rallada": "zanahoria",
         "ahuyama (calabaza)": "ahuyama", "lenteja cocida y escurrida": "lenteja", "garbanzo cocido": "garbanzo",
         "harina de trigo o avena": "harina de trigo", "agua o fórmula": None, "agua": None, "agua tibia": None,
         "fórmula preparada": None, "agua de la cocción": None, "aceite de oliva": None}
UNIDAD_G = {"zanahoria": 80, "calabacín": 200, "papa": 150}

def lista_compra(dias, plan_b, cocina_dia=()):
    """Por semana (domingo a sabado): lo que hace falta comprar, por seccion."""
    semanas = defaultdict(lambda: defaultdict(float))
    para = defaultdict(lambda: defaultdict(float))   # (semana, clave) -> plato -> cantidad
    def suma(d, prod, cant, uni, sec, de=None):
        if not sec: return
        prod = prod.lower()
        prod = CANON.get(prod, prod)
        if prod is None: return
        if uni in ("unidad", "unidades") and prod in UNIDAD_G:
            cant, uni = cant * UNIDAD_G[prod], "g"
        if uni in ("cucharada", "cucharadas", "cucharadita"):
            if "harina" in prod: cant, uni = cant * (10 if uni.startswith("cucharada") else 3), "g"
            else: return
        dom = d - dt.timedelta(days=(d.weekday() + 1) % 7)
        clave = (sec, prod, "unidad" if uni == "unidades" else uni)
        semanas[iso(dom)][clave] += cant
        if de: para[(iso(dom), clave)][de] += cant
    for b in list(plan_b) + [dict(fecha=c["fecha"], cocinar=[c]) for c in cocina_dia]:
        d = dt.date.fromisoformat(b["fecha"])
        for c in b["cocinar"]:
            r = RECETAS[c["rec"]]
            de = titulo_clave(c["rec"], c["k"])
            if c["rec"] in SIMPLES:
                for prod, cant, uni, sec in ing_cocinar(c["rec"], c["k"], c["raciones"], c["dias"])[0]:
                    suma(d, prod, cant, uni, sec, de)
                continue
            if c["rec"] in GENERICAS:
                suma(d, ALIMENTOS[c["k"]]["n"], r["ing"][0][1] * c["tandas"] * r["rinde"], "g", "Frutas y verduras", de)
                for prod, cant, uni, sec in r["ing"][1:]: suma(d, prod, cant * c["tandas"], uni, sec, de)
                continue
            for prod, cant, uni, sec in r["ing"]:
                suma(d, prod, cant * c["tandas"], uni, sec, de)
    for e in dias:
        if e.get("hotel"): continue
        d = dt.date.fromisoformat(e["fecha"])
        for s in e["cols"]:
            for i in e[s]:
                rec = i.get("rec")
                if not rec: continue
                if rec.startswith("simple-"):
                    k = rec[7:]
                    if k in ("cacahuete", "almendra", "maranon", "nuez", "avellana", "pistacho", "chia", "tahini", "mostaza"): continue
                    q, u = POR_RACION_FRUTA.get(k, (25, "g"))
                    suma(d, ALIMENTOS[k]["n"], q, u, ALIMENTOS[k]["sec"], "fruta del día" if ALIMENTOS[k]["cat"] == "fru" else "en el plato, al natural"); continue
                r = RECETAS.get(rec)
                if not r or i.get("lote") == "dia" or (i.get("origen") or "").startswith(("Del batch", "Cocinar hoy (sesión", "Sobra de lo cocinado")):
                    continue
                if rec in SIMPLES:
                    for prod, cant, uni, sec in ing_cocinar(rec, i["k"], 1, [e["fecha"]])[0]:
                        suma(d, prod, cant, uni, sec, titulo_clave(rec, i["k"]))
                    continue
                if rec in GENERICAS:
                    suma(d, ALIMENTOS[i["k"]]["n"], r["ing"][0][1], "g", "Frutas y verduras", titulo_clave(rec, i["k"])); continue
                for prod, cant, uni, sec in r["ing"]:
                    suma(d, prod, cant / r["rinde"], uni, sec, r["titulo"])
    BOTES = {"cacahuete": "crema 100 % de maní (cacahuete), sin sal ni azúcar", "tahini": "tahini 100 % sésamo",
             "almendra": "crema 100 % de almendra", "maranon": "crema 100 % de marañón (anacardo)",
             "nuez": "nueces (para moler) o crema 100 % de nuez", "avellana": "crema 100 % de avellana (sin cacao ni azúcar)",
             "pistacho": "crema 100 % de pistacho", "chia": "semillas de chía", "mostaza": "mostaza suave"}
    for e in dias:
        if e.get("pri") and e.get("nuevoK") in BOTES:
            suma(dt.date.fromisoformat(e["fecha"]), BOTES[e["nuevoK"]], 1, "bote", "Despensa", "alimento nuevo de la semana")
    out = []
    for sem in sorted(semanas):
        secs = defaultdict(list)
        items = []
        for (sec, prod, uni), cant in sorted(semanas[sem].items()):
            if prod.startswith("crema 100 % del fruto seco"): continue
            if uni == "g" and cant >= 1000: txt = f"{cant/1000:.1f} kg".replace(".0 kg", " kg")
            elif uni == "g": txt = f"{int(math.ceil(cant/50.0)*50)} g"
            elif uni == "ml": txt = f"{int(math.ceil(cant/50.0)*50)} ml"
            elif uni == "unidad": n = math.ceil(cant); txt = f"{n} {'unidad' if n == 1 else 'unidades'}"
            else: n = math.ceil(cant); txt = f"{n} {uni}{'s' if n > 1 and not uni.endswith('s') else ''}"
            secs[sec].append(f"{prod}: {txt}")
            det = para.get((sem, (sec, prod, uni)), {})
            def cuanto(q):
                if uni in ("g", "ml"): return f"{int(round(q))} {uni}"
                if uni == "unidad": return f"{q:g}".replace(".", ",") if q != int(q) else f"{int(q)}"
                return f"{q:g}"
            items.append(dict(sec=sec, prod=prod, txt=txt, para=[[x, cuanto(det[x])] for x in sorted(det, key=lambda x: -det[x])]))
        secs["Despensa"].append("aceite de oliva virgen extra (el de casa; se usa a diario)")
        out.append(dict(semana=sem, secciones={k: v for k, v in sorted(secs.items())}, items=items))
    return out

# ---------------------------------------------------------------- pautas
PAUTAS = [
    dict(desde="2026-10-08", hasta="2026-10-20", etiqueta="7 meses: 2 comidas", bloques={
        "de": dict(et="Desayuno", hora="06:00-08:00", orden=1, tipo="comida", fruta=True, bib="150-180 ml justo DESPUÉS"),
        "mm": dict(et="Media mañana", hora="09:30-10:00", orden=2, tipo="leche", fruta=False, bib="120-180 ml (el primero que bajará según hambre)"),
        "c": dict(et="Almuerzo", hora="12:00-13:00", orden=3, tipo="comida", fruta=True, bib=None,
                  nota="Fruta de postre: la OMS (2023) pide fruta y verdura a diario sin fijar en qué comida, y la vitamina C de la fruta ayuda a absorber el hierro de la comida. La pediatra indicó almuerzo sin fruta: comentádselo."),
        "me": dict(et="Merienda", hora="15:30-16:00", orden=4, tipo="leche", fruta=False, bib="150-180 ml"),
        "ad": dict(et="Antes de dormir", hora="18:30", orden=5, tipo="leche", fruta=False, bib="150-180 ml antes de dormir (se duerme ~19:00)"),
        "no": dict(et="Noche", hora="si lo pide", orden=6, tipo="leche", fruta=False, bib="Si lo pide"),
    }),
    dict(desde="2026-10-21", hasta=FIN.isoformat(), etiqueta="3 comidas: desayuno, almuerzo y cena", bloques={
        "de": dict(et="Desayuno", hora="06:00-08:00", orden=1, tipo="comida", fruta=True, bib="150-180 ml justo DESPUÉS"),
        "mm": dict(et="Media mañana (opcional)", hora="09:30-10:00", orden=2, tipo="leche", fruta=False, bib="Opcional: 120-180 ml si tiene hambre"),
        "c": dict(et="Almuerzo", hora="12:00-13:00", orden=3, tipo="comida", fruta=False, bib=None),
        "me": dict(et="Merienda", hora="15:30-16:00", orden=4, tipo="leche", fruta=True, bib="150-180 ml"),
        "ce": dict(et="Cena", hora="~18:00", orden=5, tipo="comida", fruta=True, bib="150-180 ml DESPUÉS de la cena"),
        "no": dict(et="Noche", hora="si lo pide", orden=6, tipo="leche", fruta=False, bib="Si lo pide"),
    }),
]

HOTEL_GUIA = dict(desde=iso(HOTEL[0]), hasta=iso(HOTEL[1]), titulo="Días de hotel (8-12 oct.): sin cocina", puntos=[
    "Sin alimentos nuevos estos días: se retoman al volver (la carne de res pasa al 13 de octubre).",
    "Base: lo que no hace falta cocinar (banano, papaya, pera muy madura, aguacate) y lo que pidáis a la cocina del hotel solo cocido en agua o al vapor: huevo duro, papa, pasta, pollo, zanahoria, ahuyama, calabacín.",
    "Al pedir: para un bebé, SIN sal, sin caldo de cubito, sin mantequilla, crema ni queso (los lácteos aún no están introducidos) y sin adobo. Si no pueden garantizarlo, ese día fruta, aguacate y huevo duro.",
    "Llevad: cuchillo pequeño de pelar con funda, tabla pequeña, tenedor para chafar, cucharas de bebé, recipientes con tapa, baberos, vaso abierto y bolsa isotérmica. Comprad la fruta en un supermercado cercano.",
    "La manzana no (hay que cocerla); la pera, solo si está muy madura.",
    "Plan de emergencia si un día no hay nada adecuado: fruta, aguacate y biberones como siempre. Unos pocos días así no son un problema: la fórmula sigue siendo la base de su alimentación (~500 ml/día como mínimo). Los purés de fruta en bolsita (100 % fruta, sin azúcar añadido) son industriales: solo como último recurso.",
    "Fórmula y agua de los biberones: igual que en casa.",
])

# ---------------------------------------------------------------- verificacion
def verificar(dias, intro, batch):
    errores, avisos = [], []
    recetas_usadas = set()
    prohibidos = re.compile(r"pez espada|emperador|tibur|caz[oó]n|marrajo|tintorera|at[uú]n rojo|lucio|borraja|miel|az[uú]car a[nñ]adid|embutido|salchich", re.I)
    for e in dias:
        d = dt.date.fromisoformat(e["fecha"])
        cols = e["cols"]
        orden = [PAUTA_DE(d)["bloques"][s]["orden"] for s in cols]
        if orden != sorted(orden): errores.append(f"{d}: bloques fuera de orden")
        if d >= OCHO_MESES and ("ce" not in cols or "ad" in cols): errores.append(f"{d}: falta cena o sobra 'antes de dormir'")
        if d < OCHO_MESES and ("ce" in cols or "ad" not in cols): errores.append(f"{d}: cena antes del {OCHO_MESES}")
        if d >= OCHO_MESES and any(i["cat"] == "fru" for i in e.get("c", [])): errores.append(f"{d}: fruta en el almuerzo")
        if d < OCHO_MESES and sum(1 for i in e.get("c", []) if i["cat"] == "fru") != 1: errores.append(f"{d}: falta la fruta del almuerzo")
        frutas = sum(1 for s in cols for i in e[s] if i["cat"] == "fru")
        if frutas != (3 if d >= OCHO_MESES else 2): errores.append(f"{d}: {frutas} frutas")
        for s in ("de", "c", "ce"):
            if s not in cols: continue
            cats = {i["cat"] for i in e[s]}
            if not {"prot", "har"} <= cats: errores.append(f"{d} {s}: falta proteína o harina ({cats})")
            if s in ("c", "ce") and "ver" not in cats: errores.append(f"{d} {s}: falta verdura")
            if s in ("de", "ce") and "fru" not in cats: errores.append(f"{d} {s}: falta fruta")
            if "agua" not in cats: errores.append(f"{d} {s}: falta agua")
            for i in e[s]:
                if i["cat"] != "agua" and not i.get("rec"): errores.append(f"{d} {s}: {i['n']} sin receta")
        for s in cols:
            for i in e[s]:
                if i.get("rec"): recetas_usadas.add(i["rec"])
                if prohibidos.search(i["n"]): errores.append(f"{d}: prohibido {i['n']}")
                if i["k"] in ALIMENTOS and edad_minima(i["k"]) > e["m"] and i["k"] != "agua":
                    errores.append(f"{d}: {i['n']} antes de su edad mínima")
        if e.get("nuevoK"):
            k = e["nuevoK"]
            dondes = [s for s in cols if any(i["k"] == k for i in e[s])]
            if dondes != [e["nuevoComida"]]: errores.append(f"{d}: el nuevo {k} aparece en {dondes}")
        # BLW en cada comida principal y forma de darlo en cada alimento
        for s_ in ("de", "c", "ce"):
            if s_ not in cols: continue
            con_blw = 0
            for i in e[s_]:
                if i["cat"] == "agua": continue
                r = RECETAS.get(i["rec"] or "")
                blw = (r and r["blw"]) or formato(i["k"], e["m"], "blw")
                cu = (r and r["cuchara"]) or formato(i["k"], e["m"], "cuch")
                if blw: con_blw += 1
                if not (blw or cu): errores.append(f"{d} {s_}: {i['n']} sin forma de darlo")
            if not con_blw: errores.append(f"{d} {s_}: ninguna opción BLW")
        if PAUTA_DE(d)["bloques"]["c"]["bib"]: errores.append(f"{d}: biberón en el almuerzo")
        if e.get("hotel") and e.get("nuevoK"): errores.append(f"{d}: alimento nuevo en el hotel")
        # chia antes de 10 meses
        if e["m"] < 10 and any(i["k"] == "chia" for s in cols for i in e[s]): errores.append(f"{d}: chía antes de 10 meses")
        if e["m"] < 12 and any(i["k"] in ("espinaca", "acelga") for s in cols for i in e[s]): errores.append(f"{d}: hoja verde antes de 12 meses")
    # alergenos: ninguno nuevo en los 2 dias siguientes a otro nuevo; ninguno en cena
    fechas = sorted((dt.date.fromisoformat(x["fecha"]), x) for x in intro)
    for (f1, a), (f2, b) in zip(fechas, fechas[1:]):
        if a["alergeno"] and (f2 - f1).days < 3: errores.append(f"{b['k']} el {f2} demasiado cerca del alérgeno {a['k']}")
        if b["alergeno"] and (f2 - f1).days < 2: errores.append(f"alérgeno {b['k']} pegado a {a['k']}")
    for x in intro:
        if x["alergeno"] and x["comida"] not in ("de", "c"): errores.append(f"alérgeno {x['k']} fuera de desayuno/almuerzo")
    # arroz <= 3 en 7 dias
    for i in range(len(dias)):
        ventana = dias[max(0, i - 6): i + 1]
        n = sum(1 for e in ventana if any(it["k"] == "arroz" for s in e["cols"] for it in e[s]))
        if n > 3: errores.append(f"{dias[i]['fecha']}: arroz {n} veces en 7 días")
    # mismo menu mas de 2 dias seguidos
    firma = lambda e: tuple((s, tuple(sorted((i["rec"] or "") + ":" + i["k"] for i in e[s]))) for s in e["cols"] if s in ("de", "c", "ce"))
    for a, b, c in zip(dias, dias[1:], dias[2:]):
        if firma(a) == firma(b) == firma(c): errores.append(f"{c['fecha']}: mismo menú 3 días seguidos")
    # recetas citadas existen
    for r in recetas_usadas:
        if not (r in RECETAS or r.startswith("simple-")): errores.append(f"receta inexistente {r}")
    # mantenimiento de alergenos (aviso)
    return errores, avisos, recetas_usadas

def PAUTA_DE(d):
    return PAUTAS[0] if d < OCHO_MESES else PAUTAS[1]

# ---------------------------------------------------------------- salida
def ing_txt(p, c, u):
    if not c: return p
    if u in ("unidad", "unidades"):
        if c > 1:   # "2 huevos", "2 bananos maduros"
            w = p.split(" ", 1)
            p = w[0] + ("s" if w[0][-1] in "aeiou" else "es") + (" " + w[1] if len(w) > 1 else "")
        return f"{c:g} {p}"
    if c > 1 and u in ("cucharadita", "cucharada"): u += "s"
    if u == "ración": return p[:1].upper() + p[1:]
    if u == "punta de cuchillo": return f"Una punta de cuchillo de {p}"
    if c == 0.5 and u == "cucharadita": return f"½ cucharadita de {p}"
    return f"{c:g} {u} de {p}"

# Almuerzo del 17-10 (3.er dia de la tilapia): las laminas solas las
# rechazaba; en crema de ahuyama con la pasta (peticion de la familia).
RETOQUES = {
    ("2026-10-17", "c", "pescado_blanco"): dict(rec="pescado-crema", origen="Cocinar hoy (la receta entera: lo que sobre, para mañana en la nevera)"),
    ("2026-10-17", "c", "trigo_pasta"): dict(nota="Mézclala con la crema de ahuyama y el pescado: pasta con salsa naranja."),
}

# ---------------------------------------------------------------- recetas propias
# Las recetas genericas (verdura al vapor, asada, cruda, picada, tuberculo y
# crema de fruto seco) se usaban tal cual para cada alimento, y la ficha de
# la zanahoria decia «bastón o arbolito», la del pepino «gajo de tomate» y la
# lista de ingredientes «verdura del día» (peticion de la familia, 17-10-2026).
# Al exportar, cada una pasa a ser una receta de ESE alimento: «rec~clave».
ESPECIALIZAR = set(GENERICAS) | {"crema-fruto-seco"}
VAPOR_MIN = {"calabacin": "6-8 min", "zanahoria": "15-20 min", "ahuyama": "15-20 min", "habichuela": "12-15 min",
             "brocoli": "8-10 min", "coliflor": "8-10 min"}
CORTE = {"brocoli": "en arbolitos, con el tallo como mango", "coliflor": "en arbolitos, con el tallo como mango",
         "repollo": "en tiras de hoja cortas, sin el tronco duro", "habichuela": "quitando las puntas y los hilos; enteras o en trozos de 6-8 cm"}

def nombre_corto(k):
    n = ALIMENTOS[k]["n"]
    return {"tomate": "Tomate", "pimenton": "Pimentón", "repollo": "Repollo", "pepino": "Pepino",
            "apio": "Apio", "espinaca": "Espinaca", "acelga": "Acelga", "platano_macho": "Plátano maduro"}.get(k, n.split(" (")[0])

FEM = {"arracacha", "cebolla", "espinaca", "acelga", "berenjena", "zanahoria", "coliflor", "habichuela", "ahuyama"}

def receta_de(rec, k, base):
    nom = nombre_corto(k); nl = nom.lower()
    fem = k in FEM
    oa = lambda m, f: f if fem else m
    r = dict(base)
    r["requiere"] = sorted({k}); r["alergenos"] = [ALERGENO_TXT[grupo_alergeno(k)]] if grupo_alergeno(k) else []
    r["blw"] = None; r["cuchara"] = None          # la forma la pone el alimento, segun su edad
    r["ing"] = [x.replace("verdura del día", nl).replace("ñame, arracacha o plátano maduro", nl).replace("pimentón o berenjena", nl)
                .replace("crema 100 % del fruto seco o tahini, sin sal ni azúcar", (ALIMENTOS[k]["n"] + (", sin sal" if "azúcar" in ALIMENTOS[k]["n"] else ", sin sal ni azúcar")).lower())
                for x in base["ing"]]
    if rec == "verduras-vapor":
        r["titulo"] = f"{nom} al vapor"
        r["pasos"] = [f"Lava{', pela' if k in ('zanahoria', 'ahuyama') else ''} y corta {CORTE.get(k, 'en bastones del grosor de un dedo adulto y 6-8 cm de largo')}.",
                      f"Cuece al vapor{' ' + VAPOR_MIN[k] if k in VAPOR_MIN else ''}, hasta que se aplaste con facilidad entre tus dedos índice y pulgar.",
                      "Al servir, un hilo de aceite de oliva en crudo."]
    elif rec == "verdura-asada":
        r["titulo"] = "Pimentón asado y pelado" if k == "pimenton" else f"{nom} asada"
        r["pasos"] = [base["pasos"][0], base["pasos"][1 if k == "pimenton" else 2], base["pasos"][3]]
    elif rec == "verdura-cruda":
        r["titulo"] = "Tomate pelado en gajos" if k == "tomate" else "Pepino en bastón para roer"
        r["pasos"] = [base["pasos"][0 if k == "tomate" else 1]]
    elif rec == "verdura-en-guiso":
        r["titulo"] = f"{nom} {oa('picado y bien cocido', 'picada y bien cocida')} ({oa('va mezclado', 'va mezclada')} en el plato)"
        prep = {"apio": "Quita las hebras con el pelador, pícalo muy fino", "champinon": "Límpialo con un papel húmedo, córtalo en láminas, cuécelo bien y luego pícalo",
                "cebolla": "Pélala y pícala muy fina", "puerro": "Quita la parte verde dura y las raíces, lávalo bien entre las capas y pícalo muy fino",
                "espinaca": "Lava bien las hojas, quita los tallos duros y pícalas", "acelga": "Separa la penca de la hoja, lávalas bien y pícalas"}[k]
        r["pasos"] = [f"{prep}. {oa('Cuécelo', 'Cuécela')} al vapor o {oa('rehógalo', 'rehógala')} con unas gotas de aceite hasta que esté muy {oa('blando', 'blanda')}.",
                      f"{oa('Mézclalo', 'Mézclala')} al servir con la proteína, la harina o el puré; o {oa('cuájalo', 'cuájala')} dentro de una tortilla."] + ([base["pasos"][2]] if k in ("espinaca", "acelga") else [])
    elif rec == "tuberculo-cocido":
        r["titulo"] = f"{nom} {oa('cocido', 'cocida')} en bastones"
        r["pasos"] = [f"Lava y pela {oa('el ', 'la ') + nl}.", f"{oa('Córtalo', 'Córtala')} en bastones del grosor de un dedo adulto y unos 6-8 cm de largo.",
                      f"{oa('Cuécelo', 'Cuécela')} en agua hirviendo sin sal 20-30 min, hasta que se aplaste con facilidad entre tus dedos.", f"{oa('Escúrrelo', 'Escúrrela')} bien."]
    elif rec == "crema-fruto-seco":
        r["titulo"] = ("Tahini diluido" if k == "tahini" else ALIMENTOS[k]["n"].replace(" 100 %", "") + ", diluida")
    return r

def especializar(plan):
    nuevos = {}
    def cambia(o):
        rec, k = o.get("rec"), o.get("k")
        if rec in ESPECIALIZAR and k in ALIMENTOS:
            o["rec"] = f"{rec}~{k}"
            nuevos[o["rec"]] = (rec, k)
            return True
        return False
    viejos_tit = {}
    for e in plan["dias"]:
        for c in e.get("cols", []):
            for i in e.get(c, []) or []:
                if isinstance(i, dict): cambia(i)
    for b in plan["batch"]:
        for c in b["cocinar"]:
            if cambia(c): viejos_tit[c["titulo"]] = c["rec"]
    for c in plan["cocinaDia"]:
        if cambia(c): viejos_tit[c["titulo"]] = c["rec"]
    for rid, (rec, k) in nuevos.items():
        plan["recetas"][rid] = receta_de(rec, k, plan["recetas"][rec])
    for b in plan["batch"]:
        for c in b["cocinar"]:
            if c["rec"] in nuevos: c["titulo"] = plan["recetas"][c["rec"]]["titulo"]
    for c in plan["cocinaDia"]:
        if c["rec"] in nuevos: c["titulo"] = plan["recetas"][c["rec"]]["titulo"]
    nuevo_tit = {t: plan["recetas"][rid]["titulo"] for t, rid in viejos_tit.items()}
    for e in plan["dias"]:
        if e.get("descongelar"): e["descongelar"] = [nuevo_tit.get(t, t) for t in e["descongelar"]]
    for sem in plan["compra"]:
        for it in sem["items"]:
            it["para"] = [[nuevo_tit.get(x, x), q] for x, q in it["para"]]
    usadas = {i.get("rec") for e in plan["dias"] for c in e.get("cols", []) for i in (e.get(c) or []) if isinstance(i, dict)}
    for rec in ESPECIALIZAR:
        if rec in plan["recetas"] and rec not in usadas: del plan["recetas"][rec]
    return plan

def main():
    s = open(INDEX, encoding="utf-8").read()
    m = re.search(r'(<script id="pb-plan-data" type="application/json">)(.*?)(</script>)', s, re.S)
    viejo, _ = json.JSONDecoder().raw_decode(m.group(2).strip())
    n_hist = (HOY_PLAN - INICIO_AC).days
    historia = [dict(x, fecha=iso(INICIO_AC + dt.timedelta(days=i))) for i, x in enumerate(viejo["dias"][:n_hist])]

    # Recetas propias de una ejecucion anterior («rec~clave»): vuelven a la
    # generica y especializar() las rehace al exportar.
    for e in historia:
        for col in e.get("cols", []):
            for i in e.get(col, []) or []:
                if isinstance(i, dict) and "~" in (i.get("rec") or ""): i["rec"] = i["rec"].split("~")[0]
    # Cambios pedidos por la familia en dias ya conservados.
    for e in historia:
        for (f, col, k), cambio in RETOQUES.items():
            if e["fecha"] == f:
                for i in e.get(col, []):
                    if i.get("k") == k: i.update(cambio)
    # Cantidades en gramos tambien en los dias conservados del plan v2.
    for e in historia:
        if e.get("v") != 2: continue
        meses_e = e.get("m")
        for col in e.get("cols", []):
            for i in e.get(col, []) or []:
                if isinstance(i, dict) and i.get("k") in ALIMENTOS and i.get("k") != "agua" and i.get("cant") and meses_e is not None:
                    i["cant"] = cantidad(i["k"], meses_e, i.get("nuevoDia") or 0 if i.get("nuevo") else 0,
                                         frase_mm=(col == "mm"), slot=col, rec=i.get("rec"))
                    if "(va " in (i.get("n") or ""): i["cant"] = VA_DENTRO
    intro, por_dia = calendario()
    bt = Batch({x["k"]: dt.date.fromisoformat(x["fecha"]) for x in intro})
    dias = generar_menus(intro, por_dia, bt, semilla_historia(historia))
    batch = marcar_dias(dias, bt, plan_batch(dias, bt))
    cocina_dia = plan_cocina_dia(bt)
    compra = lista_compra(dias, batch, cocina_dia)
    errores, avisos, usadas = verificar(dias, intro, batch)

    # Las recetas de los dias conservados tambien tienen que seguir ahi.
    for e in historia:
        for c_ in e.get("cols", []):
            for i in e.get(c_, []) or []:
                if isinstance(i, dict) and i.get("rec") and (i["rec"] in RECETAS or i["rec"].startswith("simple-")):
                    usadas.add(i["rec"])
    recetas = {}
    for rid in sorted(usadas):
        if rid.startswith("simple-"):
            r = receta_simple(rid[7:], ALIMENTOS)
        else:
            r = RECETAS[rid]
        al = sorted({ALERGENO_TXT[g] for g in (grupo_alergeno(k) for k in r["requiere"]) if g})
        recetas[rid] = dict(titulo=r["titulo"], rinde=r["rinde"],
                            ing=[ing_txt(p, c, u) for p, c, u, _ in r["ing"]],
                            pasos=r["pasos"], blw=r["blw"], cuchara=r["cuchara"], alergenos=al,
                            conserva=r["conserva"], batch=r["batch"], congela=r["congela"], extra=r.get("extra"))
    alimentos = {k: dict(n=a["n"], id=a["id"], cat=a["cat"], al=ALERGENO_TXT.get(grupo_alergeno(k)) if grupo_alergeno(k) else None,
                         blw={str(b): t for b, t in a["blw"].items()}, cuch={str(b): t for b, t in a["cuch"].items()}, nota=a["nota"])
                 for k, a in ALIMENTOS.items()}
    plan = dict(dias=historia + dias, semanas=[], notasMes=viejo["notasMes"], version=2,
                desde=iso(HOY_PLAN), pautas=PAUTAS, recetas=recetas, alimentos=alimentos,
                introducciones=intro, introducidosAntes=[k for k in INTRODUCIDOS if k != "agua"],
                batch=batch, cocinaDia=cocina_dia, compra=compra, hotel=HOTEL_GUIA)
    plan = especializar(plan)
    txt = json.dumps(plan, ensure_ascii=False, separators=(",", ":"))
    print(f"días: {len(plan['dias'])} ({len(historia)} conservados + {len(dias)} nuevos) · recetas: {len(recetas)} · "
          f"introducciones: {len(intro)} · sesiones de batch: {len(batch)} · semanas de compra: {len(compra)} · {len(txt)//1024} KB")
    if errores:
        print(f"ERRORES ({len(errores)}):"); [print("  -", e) for e in errores[:60]]
        sys.exit(1)
    print("Verificación: sin errores.")
    if "--solo-ver" in sys.argv: return plan
    s = s[:m.start(2)] + txt + s[m.end(2):]
    open(INDEX, "w", encoding="utf-8").write(s)
    print("Escrito en index.html")
    return plan

if __name__ == "__main__":
    main()
