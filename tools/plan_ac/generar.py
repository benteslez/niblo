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
HOY_PLAN = dt.date(2026, 10, 8)          # primer dia que se regenera
FIN = dt.date(2027, 6, 2)                # ultimo dia del plan (FECHA_FIN en la app)
OCHO_MESES = dt.date(2026, 11, 5)
HOTEL = (dt.date(2026, 10, 8), dt.date(2026, 10, 12))
PRIMERA_SESION = dt.date(2026, 10, 13)   # vuelta del hotel (martes)

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
CANT = {6: ("2-4 cucharadas soperas", "1-2 cucharadas (10-20 g)", "1-2 cucharadas"),
        7: ("4-6 cucharadas soperas", "2 cucharadas (10-20 g)", "2 cucharadas"),
        8: ("≈ ½ taza (120 ml)", "2 cucharadas (≈20 g)", "2 cucharadas"),
        9: ("≈ ½ taza", "20-25 g", "2-3 cucharadas cocida"),
        10: ("½ – ¾ taza", "25-30 g", "2-3 cucharadas cocida"),
        11: ("¾ taza", "30-35 g", "3 cucharadas cocida"),
        12: ("¾ – 1 taza (180-240 ml)", "30-35 g", "30 g en crudo")}

LEGUMBRES = {"lenteja", "garbanzo", "frijol", "arveja", "tofu"}

def cantidad(k, meses, nuevo_dia, frase_mm=False):
    a = ALIMENTOS[k]
    plato, animal, vegetal = CANT[min(max(meses, 6), 12)]
    if nuevo_dia == 1 and es_alergeno_nuevo(k):
        base = "una cantidad pequeña (p. ej. ½ cucharadita o 1-2 trocitos)"
        return f"1.er día: {base}; si va bien, días 2 y 3 la ración normal (práctica habitual)"
    if a["cat"] == "gra":
        if k == "aguacate": return "2-3 bastones o 2 cucharadas chafado"
        if k == "chia": return "½ cucharadita, remojada ≥30 min"
        if k == "mostaza": return "una punta de cuchillo"
        return "½ – 1 cucharadita"
    if a["cat"] == "prot":
        if k == "huevo": return "1 huevo: ofrece tiras y repón; no tiene por qué acabárselo"
        if k == "yogur": return "2-3 cucharadas"
        if k == "queso": return "1-2 cucharadas desmenuzado o 2 tiras"
        return vegetal if k in LEGUMBRES else animal
    if a["cat"] == "fru":
        q, u = POR_RACION_FRUTA.get(k, (60, "g"))
        txt = f"{q:g} {u}".replace("0.5 unidad", "½ pieza").replace("0.25 unidad", "¼ de pieza").replace("1 unidad", "1 pieza")
        return ("pequeña: " if frase_mm else "") + txt
    return f"parte de la ración del plato ({plato}, verdura y harina juntas)"

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
    ("pescado-laminas", "pescado_blanco"), ("salmon-horno", "salmon"), ("lenteja-chafada", "lenteja"),
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
    menus gastan primero lo que ya hay."""
    def __init__(self):
        self.ses = sesiones()
        self.stock = defaultdict(list)    # clave -> [{ses, quedan}]
        self.tareas = defaultdict(dict)   # ses -> clave -> {...}
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
        if not r["batch"] or S is None or fresco:
            it["origen"] = "Cocinar hoy: el primer día de un alimento nuevo, recién hecho" if fresco and r["batch"] else "Cocinar hoy"
            return
        clave = self.clave(rec, it["k"])
        lotes = [l for l in self.stock[clave] if self._usable(l, d, r)]
        if lotes:
            lote = lotes[0]
        else:
            if (d - S).days >= 2 and not r["congela"]:
                it["origen"] = "Cocinar hoy"; return
            lote = dict(ses=S, quedan=r["rinde"])
            self.stock[clave].append(lote)
            t = self.tareas[S].setdefault(clave, dict(rec=rec, k=it["k"], tandas=0, raciones=0, dias=[], congelar=0))
            t["tandas"] += 1
        lote["quedan"] -= 1
        gap = (d - lote["ses"]).days
        t = self.tareas[lote["ses"]][clave]
        t["raciones"] += 1
        if iso(d) not in t["dias"]: t["dias"].append(iso(d))
        cuando = fecha_txt(lote["ses"])
        if gap == 0:
            it["origen"] = "Cocinar hoy (sesión de cocina)"
        elif gap == 1:
            it["origen"] = f"Del batch del {cuando}: en la nevera"
        else:
            t["congelar"] += 1
            it["origen"] = f"Del batch del {cuando}: sacar del congelador la noche anterior"
            self.descongelar[iso(d - dt.timedelta(days=1))].append(titulo_clave(rec, it["k"]))

def titulo_clave(rec, k):
    t = RECETAS[rec]["titulo"]
    return f"{t}: {ALIMENTOS[k]['n'].lower()}" if rec in GENERICAS else t

def generar_menus(intro, por_dia, batch):
    fecha_intro = {x["k"]: dt.date.fromisoformat(x["fecha"]) for x in intro}
    hist = Historia()
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
                if rec == "bastones-papa": s -= 3
                s += 2 * deficit(grupos_de_items([item(k, c2, rec) for k, c2 in its]))
                return s
            hr = elegir(DESAYUNO_HAR, p_har)
            NOMBRE_HAR = {"tortita-trigo": "Tortita (pancake) de banano y harina de trigo", "tortita-avena": "Tortita de avena y banano",
                          "muffins": "Muffin salado de verdura (harina de trigo)", "avena-formula": "Avena con fórmula",
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
        mm = []
        if not ocho:
            mm.append(fruta("mm", mm=True))
        dia_items["mm"] = mm

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
                if k in ("arroz",) : return None
                if "har" in fz and rec in ("camaron-papa", "pasta-mariscos"): return None
                if k == "atun" and "prot" not in fz and hist.alimento("atun", 7) >= 1: return None   # ocasional
                s = -5 * hist.usado(slot + "-prot", rec, 2) - 2 * hist.usado_dia(rec, 3) - hist.alimento(k, 4) - 0.7 * hist.alimento(k, 14)
                if batch.disponible(rec, k, d): s += 3
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
            COMBO = {"camaron-papa": ("papa", "Papa (va en los pastelitos)"), "pasta-mariscos": ("trigo_pasta", "Pasta (va en la misma receta)")}
            if rec in COMBO:
                its.append(item(COMBO[rec][0], "har", rec, COMBO[rec][1]))
                usados_hoy.add(COMBO[rec][0])
            else:
                def p_har(c):
                    rec2, k = c
                    if "har" in fz and k != fz["har"]: return None
                    if "har" not in fz and k not in disp: return None
                    if k == "arroz" and arroz_semana() >= 3: return None
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
                    if "aguacate" not in usados_hoy and hist.alimento("aguacate", 1) == 0:
                        its.append(item("aguacate", "gra", "simple-aguacate")); usados_hoy.add("aguacate")
            slots[slot + "-prot"].add(rec); slots[slot + "-har"].add(its[1]["k"]); slots[slot + "-ver"].add(vk)
            return its

        usados_hoy = set(i["k"] for i in de)
        dia_items["c"] = principal("c")
        huevos += sum(1 for i in dia_items["c"] if i["k"] == "huevo")
        # ---------------- merienda
        dia_items["me"] = [fruta("me")]
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
                    i["cant"] = cantidad(i["k"], meses, nuevo[1] if nuevo and nuevo[0] == i["k"] else 0, frase_mm=(s == "mm"))
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
    d = dt.date(2026, 10, 18)   # tras la primera (martes 13, vuelta del hotel), domingos y miercoles
    while d <= FIN:
        if d.weekday() in (6, 2):   # domingo, miercoles
            out.append(d)
        d += dt.timedelta(days=1)
    return out

def plan_batch(dias, batch):
    out = []
    for S in batch.ses:
        t = batch.tareas.get(S)
        if not t: continue
        cocinar = []
        for clave, x in sorted(t.items(), key=lambda kv: titulo_clave(kv[1]["rec"], kv[1]["k"])):
            r = RECETAS[x["rec"]]
            cocinar.append(dict(rec=x["rec"], k=x["k"], titulo=titulo_clave(x["rec"], x["k"]), raciones=x["raciones"],
                                tandas=x["tandas"], rinde=r["rinde"], dias=x["dias"], congelar=x["congelar"],
                                sobran=x["tandas"] * r["rinde"] - x["raciones"]))
        out.append(dict(fecha=iso(S), cocinar=cocinar))
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

def lista_compra(dias, plan_b):
    """Por semana (domingo a sabado): lo que hace falta comprar, por seccion."""
    semanas = defaultdict(lambda: defaultdict(float))
    def suma(d, prod, cant, uni, sec):
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
        semanas[iso(dom)][(sec, prod, "unidad" if uni == "unidades" else uni)] += cant
    for b in plan_b:
        d = dt.date.fromisoformat(b["fecha"])
        for c in b["cocinar"]:
            r = RECETAS[c["rec"]]
            if c["rec"] in GENERICAS:
                suma(d, ALIMENTOS[c["k"]]["n"], r["ing"][0][1] * c["tandas"] * r["rinde"], "g", "Frutas y verduras")
                for prod, cant, uni, sec in r["ing"][1:]: suma(d, prod, cant * c["tandas"], uni, sec)
                continue
            for prod, cant, uni, sec in r["ing"]:
                suma(d, prod, cant * c["tandas"], uni, sec)
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
                    suma(d, ALIMENTOS[k]["n"], q, u, ALIMENTOS[k]["sec"]); continue
                r = RECETAS.get(rec)
                if not r or (i.get("origen") or "").startswith(("Del batch", "Cocinar hoy (sesión")):
                    continue
                if rec in GENERICAS:
                    suma(d, ALIMENTOS[i["k"]]["n"], r["ing"][0][1], "g", "Frutas y verduras"); continue
                for prod, cant, uni, sec in r["ing"]:
                    suma(d, prod, cant / r["rinde"], uni, sec)
    BOTES = {"cacahuete": "crema 100 % de maní (cacahuete), sin sal ni azúcar", "tahini": "tahini 100 % sésamo",
             "almendra": "crema 100 % de almendra", "maranon": "crema 100 % de marañón (anacardo)",
             "nuez": "nueces (para moler) o crema 100 % de nuez", "avellana": "crema 100 % de avellana (sin cacao ni azúcar)",
             "pistacho": "crema 100 % de pistacho", "chia": "semillas de chía", "mostaza": "mostaza suave"}
    for e in dias:
        if e.get("pri") and e.get("nuevoK") in BOTES:
            suma(dt.date.fromisoformat(e["fecha"]), BOTES[e["nuevoK"]], 1, "bote", "Despensa")
    out = []
    for sem in sorted(semanas):
        secs = defaultdict(list)
        for (sec, prod, uni), cant in sorted(semanas[sem].items()):
            if prod.startswith("crema 100 % del fruto seco"): continue
            if uni == "g" and cant >= 1000: txt = f"{cant/1000:.1f} kg".replace(".0 kg", " kg")
            elif uni == "g": txt = f"{int(math.ceil(cant/50.0)*50)} g"
            elif uni == "ml": txt = f"{int(math.ceil(cant/50.0)*50)} ml"
            elif uni == "unidad": n = math.ceil(cant); txt = f"{n} {'unidad' if n == 1 else 'unidades'}"
            else: n = math.ceil(cant); txt = f"{n} {uni}{'s' if n > 1 and not uni.endswith('s') else ''}"
            secs[sec].append(f"{prod}: {txt}")
        secs["Despensa"].append("aceite de oliva virgen extra (el de casa; se usa a diario)")
        out.append(dict(semana=sem, secciones={k: v for k, v in sorted(secs.items())}))
    return out

# ---------------------------------------------------------------- pautas
PAUTAS = [
    dict(desde="2026-10-08", hasta="2026-11-04", etiqueta="7 meses: 2 comidas", bloques={
        "de": dict(et="Desayuno", hora="06:00-08:00", orden=1, tipo="comida", fruta=True, bib="150-180 ml justo DESPUÉS"),
        "mm": dict(et="Media mañana", hora="09:30-10:00", orden=2, tipo="leche", fruta=True, bib="120-180 ml (el primero que bajará según hambre)"),
        "c": dict(et="Almuerzo", hora="12:00-13:00", orden=3, tipo="comida", fruta=False, bib=None),
        "me": dict(et="Merienda", hora="15:30-16:00", orden=4, tipo="leche", fruta=True, bib="150-180 ml"),
        "ad": dict(et="Antes de dormir", hora="18:30", orden=5, tipo="leche", fruta=False, bib="150-180 ml antes de dormir (se duerme ~19:00)"),
        "no": dict(et="Noche", hora="si lo pide", orden=6, tipo="leche", fruta=False, bib="Si lo pide"),
    }),
    dict(desde="2026-11-05", hasta=FIN.isoformat(), etiqueta="Desde 8 meses: 3 comidas", bloques={
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
        if d < OCHO_MESES and ("ce" in cols or "ad" not in cols): errores.append(f"{d}: cena antes del 5 nov.")
        if any(i["cat"] == "fru" for i in e.get("c", [])): errores.append(f"{d}: fruta en el almuerzo")
        frutas = sum(1 for s in cols for i in e[s] if i["cat"] == "fru")
        if frutas != 3: errores.append(f"{d}: {frutas} frutas")
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
    if u in ("unidad", "unidades"): return f"{c:g} {p}"
    if u == "ración": return p[:1].upper() + p[1:]
    if u == "punta de cuchillo": return f"Una punta de cuchillo de {p}"
    if c == 0.5 and u == "cucharadita": return f"½ cucharadita de {p}"
    return f"{c:g} {u} de {p}"

def main():
    s = open(INDEX, encoding="utf-8").read()
    m = re.search(r'(<script id="pb-plan-data" type="application/json">)(.*?)(</script>)', s, re.S)
    viejo, _ = json.JSONDecoder().raw_decode(m.group(2).strip())
    n_hist = (HOY_PLAN - INICIO_AC).days
    historia = [dict(x, fecha=iso(INICIO_AC + dt.timedelta(days=i))) for i, x in enumerate(viejo["dias"][:n_hist])]

    intro, por_dia = calendario()
    bt = Batch()
    dias = generar_menus(intro, por_dia, bt)
    batch = plan_batch(dias, bt)
    compra = lista_compra(dias, batch)
    errores, avisos, usadas = verificar(dias, intro, batch)

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
                batch=batch, compra=compra, hotel=HOTEL_GUIA)
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
