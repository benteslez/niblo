"""Menú de Pablo desde los 8 meses (petición de la familia, 10-11-2026).

Lee tools/menu8/calendario.json (la tabla «Calendario día a día» del PDF
«Menú semanal de Pablo (8 meses)», copiada tal cual con leer_pdf.py) y
escribe en index.html el bloque <script id="pb-menu8-data">:

  dias      un objeto por día: qué toca en desayuno, comida y cena, separado
            en componentes («+» del PDF), con su papel (base del lote, para
            la mano, fruta, al momento, alérgeno…) y lo que hay que hacer la
            noche anterior (descongelar, remojar).
  sesiones  los días de cocinar: las 4 bases (A-D) con sus raciones (las que
            se comen en su periodo), ingredientes del lote y pasos.
  compra    una lista por sesión: todo lo que hace falta para cocinar ese día
            y para los desayunos, cenas al momento y fruta de su periodo.

El menú (qué se come cada día) es el del PDF, sin tocar. Las CANTIDADES no
están en el calendario: son orientativas, escaladas de las 4 recetas de
la primera semana del PDF (p. ej. base A: 120-150 g de res para 3
raciones ≈ 45 g por ración) y de su tabla «Desayunos rápidos». Se dicen así
en la app.

Uso: python3 tools/menu8/generar.py [--solo-ver]
"""
import datetime as dt, json, math, os, re, sys
from collections import OrderedDict, defaultdict

AQUI = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(os.path.dirname(os.path.dirname(AQUI)), "index.html")
CAL = json.load(open(os.path.join(AQUI, "calendario.json"), encoding="utf-8"))["dias"]

D = lambda s: dt.date.fromisoformat(s)

# ---------------------------------------------------------------------------
# Ingredientes: nombre en la lista, sección del súper, qué comprar exactamente
# (petición: «si es carne de res, qué tipo de carne es mejor»), peso de una
# unidad para traducir gramos a piezas.
# ---------------------------------------------------------------------------
SEC = ["Carne y pescado", "Huevos y lácteos", "Verdura", "Fruta", "Despensa"]
ING = {
  # Carne y pescado
  "res": ("Carne de res magra para guisar", 0, None,
          "Un trozo magro: bola, centro de pierna o muchacho, sin grasa ni nervios. Pide que te lo corten en dados pequeños. Nada de carne ya adobada."),
  "res_molida": ("Carne de res molida magra", 0, None,
          "Magra (≤ 10 % de grasa): mejor pide que muelan delante bola o pierna, una sola vez. Sin adobo ni sal. Para las albóndigas."),
  "ternera": ("Ternera magra para guisar", 0, None,
          "Pierna o lomo de ternera, sin grasa ni nervios, en dados. Si no hay ternera, vale la misma res magra."),
  "cerdo": ("Lomo de cerdo", 0, None,
          "Lomo (la pieza más magra), sin grasa visible, en un trozo o en dados. No costilla ni panceta, ni ahumado."),
  "pollo_muslo": ("Pollo: contramuslo o muslo sin piel", 0, None,
          "El PDF usa muslo sin piel: más jugoso que la pechuga y con algo más de hierro. Deshuesado si lo hay (si no, con hueso y lo deshuesas tú; compra ≈ 40 % más de peso). Fresco, sin marinar."),
  "gambas": ("Gambas (camarones) crudas", 0, None,
          "Crudas, peladas y desvenadas; frescas o congeladas al natural (sin glaseado salado ni precocidas). Se pican finas."),
  "tilapia": ("Tilapia en filete", 0, None,
          "Filete sin piel ni espinas, fresco o congelado al natural (sin glaseado con sal ni empanado). Ya la tolera."),
  "salmon": ("Salmón en filete (lomo)", 0, None,
          "Lomo sin piel ni espinas, fresco o congelado al natural. Nunca ahumado (lleva sal)."),
  "trucha": ("Trucha en filete", 0, None,
          "Trucha arcoíris en filete, sin espinas, fresca o congelada al natural. Nunca ahumada."),
  # Huevos y lácteos
  "huevo": ("Huevos", 1, 1,
          "De gallina, frescos. Siempre bien cuajados, sin partes líquidas."),
  "yogur": ("Yogur Alpina Baby Gü natural", 1, 1,
          "El natural, no el de vainilla (lo dice el PDF): sin azúcar añadido."),
  "yogur_soja": ("Yogur de soja natural sin azúcar", 1, 1,
          "Natural y sin azúcar ni sabores (lo dice el PDF). Para el primer día de soja."),
  "parmesano": ("Queso parmesano", 0, None,
          "En cuña para rallar al momento (o rallado 100 % parmesano). Solo una pizca: es de los quesos más salados."),
  # Verdura (peso orientativo de una pieza para pasar a unidades)
  "papa": ("Papa", 0, 170, "Papa pastusa o sabanera (harinosa, se aplasta bien)."),
  "batata": ("Batata", 0, 250, "Firme, sin golpes."),
  "yuca": ("Yuca", 0, 400, "Fresca, blanca por dentro; se le quita la fibra central. Vale congelada pelada."),
  "arracacha": ("Arracacha", 0, 150, "Firme y amarilla por dentro."),
  "platano": ("Plátano maduro", 0, 250, "Con la cáscara casi negra: así está dulce y blando."),
  "zanahoria": ("Zanahoria", 0, 80, "Mediana. Siempre cocida hasta que se aplaste."),
  "auyama": ("Auyama", 0, None, "Un trozo de auyama de pulpa naranja intensa; te la cortan al peso."),
  "calabacin": ("Calabacín", 0, 200, "Mediano, firme y brillante."),
  "brocoli": ("Brócoli", 0, 300, "Cabeza verde oscura y apretada."),
  "coliflor": ("Coliflor", 0, 500, "Blanca y apretada, sin manchas."),
  "habichuela": ("Habichuela", 0, None, "Verde, fina y tierna (que se parta al doblarla)."),
  "arveja": ("Arveja verde", 0, None, "Desgranada fresca o congelada al natural. Siempre dentro del puré o aplastada."),
  "pimiento": ("Pimiento rojo", 0, 150, "Rojo, carnoso; se pela o se tritura bien."),
  "cebolla": ("Cebolla cabezona blanca", 0, 150, "Mediana."),
  "tomate": ("Tomate chonto maduro", 0, 120, "Maduro; se pela antes de usarlo."),
  "aguacate": ("Aguacate", 0, 200, "Hass, que ceda un poco al apretar. ¼ por desayuno."),
  # Fruta (peso de una pieza; ración orientativa en RAC_FRUTA)
  "banano": ("Banano", 0, 120, "Maduro (con pintas): más dulce y blando."),
  "fresa": ("Fresas", 0, None, "Rojas y firmes. Se dan en cuartos."),
  "pitahaya": ("Pitahaya amarilla", 0, 250, "Que ceda un poco al apretarla."),
  "pera": ("Pera", 0, 180, "Cocida en gajos, o cruda solo si está muy madura y blanda."),
  "manzana": ("Manzana", 0, 150, "Para dar siempre cocida (en gajos, rallada fina o en compota)."),
  "kiwi": ("Kiwi", 0, 90, "Maduro, que ceda al apretar."),
  "sandia": ("Sandía", 0, None, "Un trozo; sin pepitas."),
  "papaya": ("Papaya", 0, None, "Madura (piel amarilla); un trozo o una pequeña."),
  "naranja": ("Naranja", 0, 200, "De jugo, para dar la pulpa machacada sin membranas ni pepitas."),
  "mango": ("Mango", 0, 300, "Maduro (Tommy o de azúcar)."),
  "melon": ("Melón", 0, None, "Maduro; un trozo."),
  "durazno": ("Durazno", 0, 150, "Muy maduro; si está firme, cocido."),
  "arandanos": ("Arándanos", 0, None, "Siempre aplastados."),
  "mandarina": ("Mandarina", 0, 100, "Gajos sin piel, membranas ni pepitas."),
  "feijoa": ("Feijoa", 0, 60, "Madura (cede al apretar); se da la pulpa, sin piel."),
  "guayaba": ("Guayaba", 0, 120, "Madura; sin piel y sin la parte central de semillas."),
  # Despensa
  "lentejas": ("Lentejas", 0, None, "Secas, de las pequeñas (o en frasco al natural, sin sal, bien enjuagadas)."),
  "garbanzos": ("Garbanzos", 0, None, "Secos (remojo de 12 h) o en frasco al natural, sin sal, enjuagados. Siempre aplastados."),
  "frijol": ("Fríjol rojo", 0, None, "Seco (remojo de 12 h) o cocido al natural sin sal ni guiso. Siempre aplastado o en el puré."),
  "pasta_peq": ("Pasta pequeña de trigo", 0, None, "Estrellitas, municiones o letras, sin huevo añadido ni sabores."),
  "pasta_gr": ("Pasta grande de trigo (fusilli)", 0, None, "Fusilli o similar, para coger con la mano; muy blanda."),
  "quinoa": ("Quinoa", 0, None, "Lavada (o lávala bien antes de cocerla para quitar el amargor)."),
  "arroz": ("Arroz blanco", 0, None, "Con moderación (arsénico, lo dice el PDF): lávalo y cuécelo en mucha agua."),
  "avena": ("Avena en hojuelas", 0, None, "Tradicional, sin azúcar ni sabores. Para pancakes y muffins se muele."),
  "harina_maiz": ("Harina de maíz precocida blanca", 0, None, "Para la arepa casera sin sal: la comercial suele llevar sal (lo dice el PDF)."),
  "aceite": ("Aceite de oliva virgen extra", 0, None, "En crudo sobre el puré ya servido y un chorrito para rehogar."),
  "crema_cacahuete": ("Crema de cacahuete (maní) 100 %", 0, None, "Solo cacahuete: sin sal, azúcar ni aceite de palma; lisa, no crunchy. Siempre diluida."),
  "tahini": ("Tahini 100 % sésamo", 0, None, "Sin sal; se da diluido."),
  "crema_almendra": ("Crema de almendra 100 %", 0, None, "Sin sal ni azúcar; lisa. Siempre diluida."),
  "crema_anacardo": ("Crema de anacardo 100 %", 0, None, "Sin sal ni azúcar; lisa. Siempre diluida."),
  "crema_nuez": ("Crema de nuez 100 %", 0, None, "Sin sal ni azúcar; lisa. Siempre diluida."),
  "crema_avellana": ("Crema de avellana 100 %", 0, None, "Solo avellana (no la de cacao y azúcar). Siempre diluida."),
  "crema_pistacho": ("Crema de pistacho 100 %", 0, None, "Sin sal ni azúcar; lisa. Siempre diluida."),
}
SECCION = {**{k: "Carne y pescado" for k in ["res", "res_molida", "ternera", "cerdo", "pollo_muslo", "gambas", "tilapia", "salmon", "trucha"]},
           **{k: "Huevos y lácteos" for k in ["huevo", "yogur", "yogur_soja", "parmesano"]},
           **{k: "Verdura" for k in ["papa", "batata", "yuca", "arracacha", "platano", "zanahoria", "auyama", "calabacin", "brocoli", "coliflor",
                                      "habichuela", "arveja", "pimiento", "cebolla", "tomate", "aguacate"]},
           **{k: "Fruta" for k in ["banano", "fresa", "pitahaya", "pera", "manzana", "kiwi", "sandia", "papaya", "naranja", "mango", "melon",
                                    "durazno", "arandanos", "mandarina", "feijoa", "guayaba"]}}
for k in ING:
    SECCION.setdefault(k, "Despensa")

# ---------------------------------------------------------------------------
# Bases del lote: gramos (en crudo) por ración. Escala de las 4 recetas del
# PDF: A 120-150 g res / 3; B 2 muslos / 4; C ~100 g tilapia / 2; D 50 g de
# lentejas / 3; una papa (~170 g) para 3 raciones.
# ---------------------------------------------------------------------------
POR_RACION = {"res": 45, "res_molida": 45, "ternera": 45, "cerdo": 45, "pollo_muslo": 45, "tilapia": 50, "salmon": 50, "trucha": 50,
              "papa": 60, "batata": 60, "yuca": 60, "arracacha": 60, "platano": 50, "pasta_peq": 15, "quinoa": 15, "arroz": 15,
              "zanahoria": 40, "auyama": 50, "calabacin": 40, "brocoli": 40, "coliflor": 40, "habichuela": 30, "arveja": 20,
              "pimiento": 20, "cebolla": 15, "tomate": 30, "manzana": 40, "lentejas": 17, "garbanzos": 17, "frijol": 17}
PALABRA = [  # orden importa: lo más específico primero
  (r"albóndigas blandas de res", "res_molida"), (r"\bres\b", "res"), (r"ternera", "ternera"), (r"lomo de cerdo", "cerdo"),
  (r"pollo", "pollo_muslo"), (r"tilapia", "tilapia"), (r"salmón", "salmon"), (r"trucha", "trucha"),
  (r"lentejas", "lentejas"), (r"garbanzos", "garbanzos"), (r"fríjol", "frijol"),
  (r"\bpapa\b", "papa"), (r"batata", "batata"), (r"yuca", "yuca"), (r"arracacha", "arracacha"), (r"plátano maduro", "platano"),
  (r"pasta", "pasta_peq"), (r"quinoa", "quinoa"), (r"arroz", "arroz"),
  (r"zanahoria", "zanahoria"), (r"auyama", "auyama"), (r"calabacín", "calabacin"), (r"brócoli", "brocoli"), (r"coliflor", "coliflor"),
  (r"habichuela", "habichuela"), (r"arveja", "arveja"), (r"pimiento", "pimiento"), (r"cebolla", "cebolla"), (r"tomate", "tomate"),
  (r"manzana", "manzana")]
PROTE = {"res", "res_molida", "ternera", "cerdo", "pollo_muslo", "tilapia", "salmon", "trucha"}
LEGUM = {"lentejas", "garbanzos", "frijol"}

def ings_base(titulo):
    t = titulo.lower()
    ks = []
    for rx, k in PALABRA:
        if re.search(rx, t) and k not in ks:
            if k == "res" and "res_molida" in ks: continue
            ks.append(k)
    if "res_molida" in ks and "cebolla" not in ks: ks.append("cebolla")   # la salsa de tomate se hace con cebolla
    out = OrderedDict()
    for k in ks:
        g = POR_RACION[k]
        if k == "pollo_muslo" and any(x in ks for x in LEGUM): g = 25   # base D: pollo + legumbre
        out[k] = g
    return out

def tipo_base(titulo):
    ks = ings_base(titulo)
    if any(k in LEGUM for k in ks): return "legumbre"
    if "res_molida" in ks: return "albondigas"
    if any(k in ("tilapia", "salmon", "trucha") for k in ks): return "pescado"
    if "pollo_muslo" in ks: return "pollo"
    return "carne"

EMO_BASE = {"legumbre": "🫘", "albondigas": "🧆", "pescado": "🐟", "pollo": "🍗", "carne": "🥩"}

# Pasos de las bases. Las 4 de la primera semana son las recetas del PDF;
# el resto sigue el mismo método según el tipo (y se dice así).
RECETA_PDF = {
  "Res guisada con pimiento, cebolla, tomate, zanahoria y papa": [
    "Rehoga a fuego suave ½ cebolla, ½ pimiento rojo y 1 tomate pelado, picados, con un chorrito de aceite.",
    "Añade unos 120-150 g de res magra en dados, 1 zanahoria y 1 papa en trozos; cubre con agua.",
    "Cuece hasta que la carne esté muy tierna (olla a presión acorta mucho).",
    "Tritura con parte del caldo hasta la textura que maneje. Cuece aparte papa y zanahoria extra en bastones."],
  "Pollo con auyama, calabacín y arracacha": [
    "Cuece 2 muslos de pollo sin piel con ½ cebolla, 1 arracacha, un trozo de auyama y 1 calabacín.",
    "Deshuesa con cuidado y tritura con el caldo.",
    "Asa aparte bastones de auyama al horno con un poco de aceite, hasta que se aplasten con los dedos."],
  "Tilapia con papa, brócoli y cebolla": [
    "Cuece 1 papa y ¼ de cebolla; añade brócoli y, al final, unos 100 g de tilapia (pocos minutos).",
    "Revisa espinas con los dedos antes de triturar. Reserva ramitos de brócoli y lascas de pescado sin triturar."],
  "Pollo con lentejas, zanahoria, tomate y pasta": [
    "Cuece unos 50 g de lentejas lavadas con 1 zanahoria, ½ tomate y ¼ de cebolla.",
    "Añade pollo en dados y, al final, pasta pequeña (o yuca en trozos si aún no ha probado trigo).",
    "Tritura. Cuece aparte bastones de yuca o pasta grande (tipo fusilli) muy blanda."],
}
CORTO = {"cebolla": "la cebolla", "pimiento": "el pimiento", "tomate": "el tomate (pelado)", "papa": "la papa", "batata": "la batata",
         "yuca": "la yuca (sin la fibra central)", "arracacha": "la arracacha", "platano": "el plátano maduro", "zanahoria": "la zanahoria",
         "auyama": "la auyama", "calabacin": "el calabacín", "brocoli": "el brócoli", "coliflor": "la coliflor", "habichuela": "la habichuela",
         "arveja": "la arveja", "manzana": "la manzana (pelada)", "quinoa": "la quinoa (lavada)", "arroz": "el arroz (lavado)",
         "pasta_peq": "la pasta pequeña"}
LEG_TXT = {"lentejas": "las lentejas (lavadas)", "garbanzos": "los garbanzos (remojados 12 h si son secos)", "frijol": "el fríjol (remojado 12 h si es seco)"}
def nombres(ks):
    n = [CORTO[k] for k in ks]
    return ", ".join(n[:-1]) + " y " + n[-1] if len(n) > 1 else (n[0] if n else "")
SOFRITO = ("cebolla", "pimiento", "tomate")
FIN_MANO = "Aparta sin triturar lo que va para la mano (abajo, «Para la mano»)."

def pasos_base(titulo):
    """Pasos de una base. Las 4 de la primera semana son las del PDF; el resto
    siguen su mismo método según el tipo de base."""
    if titulo in RECETA_PDF: return RECETA_PDF[titulo], True
    ks = list(ings_base(titulo)); tb = tipo_base(titulo)
    verd = [k for k in ks if k not in PROTE and k not in LEGUM]
    if tb == "carne":
        sof = [k for k in verd if k in SOFRITO]; resto = [k for k in verd if k not in SOFRITO]
        p = ([f"Rehoga a fuego suave, picados, {nombres(sof)} con un chorrito de aceite."] if sof else []) + [
             f"Añade la carne en dados" + (f" y {nombres(resto)} en trozos" if resto else "") + "; cubre con agua.",
             "Cuece hasta que la carne esté muy tierna, que se deshaga con el tenedor (la olla a presión acorta mucho).",
             "Tritura con parte del caldo hasta la textura que maneje. " + FIN_MANO]
    elif tb == "albondigas":
        p = ["Ralla el calabacín y escúrrelo bien. Mézclalo con la carne molida y forma albóndigas pequeñas y blandas (sin sal).",
             "Rehoga la cebolla picada con un chorrito de aceite, añade el tomate pelado y picado y cuece la salsa unos minutos.",
             "Cuece las albóndigas en la salsa, tapadas, hasta que estén hechas por dentro (sin nada rosado). Cuece la papa aparte o en la misma salsa.",
             "Tritura una parte con la salsa y la papa; guarda albóndigas enteras para la «media albóndiga aplastada»."]
    elif tb == "pollo":
        p = [f"Cuece el pollo sin piel con {nombres(verd)}, cubierto de agua.",
             "Deshuesa con cuidado (si tenía hueso) y tritura con el caldo hasta la textura que maneje.",
             FIN_MANO]
    elif tb == "pescado":
        duro = [k for k in verd if k in ("papa", "batata", "yuca", "arracacha", "quinoa")]
        resto = [k for k in verd if k not in duro]
        p = [f"Cuece {nombres(duro)}" + (f" con {nombres(resto)}" if resto else "") + "; al final, añade el pescado (pocos minutos).",
             "Revisa espinas con los dedos antes de triturar. Reserva lascas de pescado y la verdura para la mano sin triturar."]
    else:
        leg = [k for k in ks if k in LEGUM][0]
        pasta = "pasta_peq" in verd
        v = [k for k in verd if k != "pasta_peq"]
        p = [f"Cuece {LEG_TXT[leg]} con {nombres(v)}.",
             "Añade el pollo en dados" + (" y, al final, la pasta pequeña." if pasta else "."),
             "Tritura. " + FIN_MANO]
    return p, False

# ---------------------------------------------------------------------------
# Componentes del calendario: papel, emoji, ingredientes por ración y cómo darlo.
# ---------------------------------------------------------------------------
FRUTA = [  # (regex, clave, emoji, gramos por ración)
  (r"^banano", "banano", "🍌", 60), (r"^fresas", "fresa", "🍓", 40), (r"^pitahaya", "pitahaya", "🌵", 60), (r"^pera", "pera", "🍐", 60),
  (r"^manzana cocida", "manzana", "🍎", 60), (r"^kiwi", "kiwi", "🥝", 45), (r"^sandía", "sandia", "🍉", 60), (r"^papaya", "papaya", "🥭", 60),
  (r"^naranja", "naranja", "🍊", 60), (r"^mango", "mango", "🥭", 60), (r"^melón", "melon", "🍈", 60), (r"^durazno", "durazno", "🍑", 60),
  (r"^arándanos", "arandanos", "🫐", 30), (r"^mandarina", "mandarina", "🍊", 50), (r"^feijoa", "feijoa", "🥝", 40),
  (r"^guayaba", "guayaba", "🍈", 50)]
MANO = [  # guarniciones para la mano: (regex, emoji, ingredientes por toma)
  (r"bastones de papa", "🥔", {"papa": 50}), (r"bastones de zanahoria", "🥕", {"zanahoria": 40}), (r"bastones de yuca", "🍠", {"yuca": 50}),
  (r"bastones de batata", "🍠", {"batata": 50}), (r"bastones de plátano maduro", "🍌", {"platano": 50}), (r"bastones de arracacha", "🥔", {"arracacha": 50}),
  (r"bastones de calabacín|calabacín al vapor", "🥒", {"calabacin": 50}), (r"auyama asada", "🎃", {"auyama": 50}),
  (r"ramitos de brócoli", "🥦", {"brocoli": 30}), (r"ramitos de coliflor", "🥦", {"coliflor": 30}), (r"pasta grande", "🍝", {"pasta_gr": 20}),
  (r"habichuela cocida blanda", "🫛", {"habichuela": 30}), (r"garbanzos aplastados", "🫘", {"garbanzos": 10}),
  (r"lascas de tilapia", "🐟", {"tilapia": 20}), (r"lascas de salmón", "🐟", {"salmon": 20}), (r"lascas de trucha", "🐟", {"trucha": 20}),
  (r"tiras de pollo desmechado", "🍗", {"pollo_muslo": 20}), (r"media albóndiga aplastada", "🧆", {}),
  (r"tiras de arepa sin sal", "🫓", {"harina_maiz": 20}), (r"una pizca de parmesano", "🧀", {"parmesano": 3})]
CREMAS = [(r"cacahuete", "crema_cacahuete", "cacahuete", "Cacahuete"), (r"tahini", "tahini", "ajonjoli", "Sésamo (tahini)"),
          (r"almendra", "crema_almendra", "oleaginosas", "Almendra"), (r"anacardo", "crema_anacardo", "anacardo_pistacho", "Anacardo"),
          (r"\bnuez\b", "crema_nuez", "nuez_avellana", "Nuez"), (r"avellana", "crema_avellana", "avellana", "Avellana"),
          (r"pistacho", "crema_pistacho", "pistacho", "Pistacho")]
# Los ids son los del seguimiento de alérgenos de la app (introducciones del plan).
# id del alimento en la app (para «¿Cómo le fue?») de las frutas nuevas.
ID_APP = {"guayaba": "guayaba", "melon": "melon", "durazno": "durazno", "arandanos": "blueberry", "mandarina": "naranja_y_mandarina"}

# Desayunos y platos al momento: emoji, ingredientes por toma y receta (la del PDF, «Desayunos rápidos»).
PLATOS = [
  (r"^pancakes de banano, avena y huevo", "🥞", {"banano": 120, "huevo": 1, "avena": 15},
   "10 min o la noche antes", ["1 banano maduro + 1 huevo + 2-3 cucharadas de avena molida.", "Sartén antiadherente.", "Nevera máx. 1 día; si no, congelar."], "pdf"),
  (r"^tortilla de huevo con calabacín", "🍳", {"huevo": 1, "calabacin": 30},
   "5 min", ["1 huevo batido + 2-3 cucharadas de calabacín rallado y escurrido.", "Cuajar bien por ambos lados con poco aceite.", "Cortar en tiras."], "pdf"),
  (r"^yogur baby gü natural con banano y avena", "🥣", {"yogur": 1, "avena": 10, "banano": 60},
   "La noche antes", ["Yogur Alpina Baby Gü natural + 1-2 cucharadas de avena en hojuelas; nevera toda la noche.", "Por la mañana, el banano aplastado y la fruta."], "pdf"),
  (r"^yogur de soja natural sin azúcar con avena", "🥣", {"yogur_soja": 1, "avena": 10},
   "La noche antes", ["Yogur de soja natural sin azúcar + 1-2 cucharadas de avena en hojuelas; nevera toda la noche.", "La fruta, por la mañana. Es el único alimento nuevo del día."], "propia"),
  (r"^yogur baby gü natural con avena", "🥣", {"yogur": 1, "avena": 10},
   "La noche antes", ["Yogur Alpina Baby Gü natural + 1-2 cucharadas de avena en hojuelas; nevera toda la noche.", "La fruta, por la mañana."], "pdf"),
  (r"^huevo revuelto con tomate$", "🍳", {"huevo": 1, "tomate": 20},
   "5 min", ["Huevo revuelto con un poco de tomate pelado y picado, bien hecho (sin partes líquidas).", "Papa cocida en bastones (reserva de la base o cocida aparte)."], "pdf~"),
  (r"^huevo revuelto$", "🍳", {"huevo": 1},
   "5 min", ["Huevo revuelto bien hecho (sin partes líquidas).", "Papa cocida reservada de la base, en bastones."], "pdf"),
  (r"^muffin de huevo, auyama y avena", "🧁", {},
   "Lote congelado", ["3 huevos + ~100 g de auyama cocida aplastada + 3 cucharadas de avena.", "Horno a 180 °C hasta que estén cuajados.", "Congelar; pasar a nevera la noche antes."], "pdf"),
  (r"^avena con su fórmula", "🥣", {"avena": 15},
   "5 min", ["Cocer avena en agua, dejar templar y mezclar con su fórmula ya preparada.", "La crema de fruto seco (si toca): ½ cucharadita, 100 % (sin sal ni azúcar), bien disuelta."], "pdf"),
  (r"^arepa sin sal con huevo revuelto y aguacate", "🫓", {"harina_maiz": 25, "huevo": 1, "aguacate": 50},
   "10 min", ["Arepa casera: harina de maíz precocida y agua, sin sal; hazla fina y blanda.", "Huevo revuelto bien cuajado.", "Aguacate aplastado encima o en tiras gruesas."], "propia"),
  (r"^gambas peladas y picadas con papa y calabacín", "🦐", {"gambas": 40, "papa": 60, "calabacin": 40},
   "15 min", ["Cuece la papa y el calabacín hasta que estén muy blandos.", "Añade las gambas peladas y picadas finas los últimos minutos, hasta que estén opacas y firmes por dentro.",
              "Aplasta todo junto o dalo en trocitos blandos. De día, sin otro alimento nuevo, y vigila después (alérgeno)."], "propia"),
  (r"^tortilla de huevo, papa y calabacín \(al momento\)", "🍳", {"huevo": 1, "papa": 40, "calabacin": 30},
   "10 min", ["Papa cocida en dados pequeños y calabacín rallado y escurrido.", "Mezcla con 1 huevo batido y cuaja bien por los dos lados con poco aceite.", "En tiras."], "propia"),
  (r"^huevo revuelto con tomate y cebolla \(al momento\)", "🍳", {"huevo": 1, "tomate": 20, "cebolla": 10},
   "5 min", ["Rehoga un poco de cebolla y tomate pelado, muy picados, con poco aceite.", "Añade 1 huevo batido y remueve hasta que esté bien hecho, sin partes líquidas."], "propia"),
]
MUFFIN_LOTE = {"huevo": 3, "auyama": 100, "avena": 20}

# Cómo dar lo que puede quedar duro (tabla del PDF, «Seguridad»).
COMO = [
  (r"\bpera\b", "Cocida: pelada, en gajos gruesos, al vapor o en microondas tapada con un poco de agua hasta que se aplaste entre los dedos. Cruda solo si está muy madura y blanda."),
  (r"manzana", "Siempre cocida en gajos, rallada fina o en compota."),
  (r"guayaba", "Madura, sin piel y sin la parte central de semillas; si está firme, cocida o en compota colada."),
  (r"durazno", "Muy maduro y pelado, en gajos grandes; si está firme, cocido como la pera."),
  (r"zanahoria", "Siempre cocida hasta que se aplaste; nunca cruda en bastones."),
  (r"yuca", "Cocida muy blanda y sin la fibra del centro."),
  (r"arveja|fríjol|garbanzo", "Dentro del puré o aplastados con tenedor; no enteros sueltos."),
  (r"arándanos", "Siempre aplastados."),
  (r"naranja|mandarina", "Pulpa sin membranas ni pepitas, machacada."),
  (r"melón|sandía|mango|kiwi|papaya", "Bien maduros, sin piel ni pepitas, en tiras o gajos grandes."),
  (r"lascas|tilapia|salmón|trucha", "Revisa espinas con los dedos antes de servir, también en las lascas."),
  (r"crema de|tahini", "Siempre diluida o extendida muy fina; nunca a cucharadas ni frutos secos enteros."),
  (r"bastones|ramitos|auyama asada|calabacín al vapor|habichuela", "Del tamaño de un dedo adulto y tan blandos que se aplasten entre pulgar e índice."),
]
def como(txt):
    return next((c for rx, c in COMO if re.search(rx, txt.lower())), None)

def emoji_plato(t):
    tl = t.lower()
    for rx, e, *_ in PLATOS:
        if re.search(rx, tl): return e
    return "🍽️"

# ---------------------------------------------------------------------------
# Sesiones de cocina
# ---------------------------------------------------------------------------
MES = {"ene": 1, "feb": 2, "mar": 3, "abr": 4, "may": 5, "jun": 6, "jul": 7, "ago": 8, "sep": 9, "oct": 10, "nov": 11, "dic": 12}
sesiones = []
for i, d in enumerate(CAL):
    if not d["cocinar"]: continue
    m = re.match(r"Para (.*?): (A .*)$", d["cocinar"])
    assert m, d["cocinar"]
    bases = OrderedDict()
    for parte in re.split(r"; (?=[ABCD] )", m.group(2)):
        bases[parte[0]] = parte[2:].strip()
    assert list(bases) == ["A", "B", "C", "D"], bases
    sesiones.append({"fecha": d["fecha"], "para": m.group(1), "bases": bases})
for i, s in enumerate(sesiones):
    s["desde"] = s["fecha"] if i == 0 else (D(s["fecha"]) + dt.timedelta(1)).isoformat()
    s["hasta"] = sesiones[i + 1]["fecha"] if i + 1 < len(sesiones) else CAL[-1]["fecha"]

def sesion_de(f):
    return next(s for s in reversed(sesiones) if s["desde"] <= f)

# ---------------------------------------------------------------------------
# Días
# ---------------------------------------------------------------------------
def comp(txt, slot, f):
    """Un componente del plato («+» del PDF) → objeto para la app."""
    t = txt.strip()
    o = {"t": t}
    nota = re.match(r"^(.*?)\. (Cumple 12 meses: .*)$", t)
    if nota:
        t = o["t"] = nota.group(1); o["nota"] = nota.group(2)
    tl = t.lower()
    for rx, k, e, g in FRUTA:
        if re.search(rx, tl):
            o.update(rol="fruta", e=e, ing={k: g})
            if "(nueva)" in tl:
                o["nuevo"] = True; o["t"] = re.sub(r"\s*\(nueva\)", "", t)
                if k in ID_APP: o["id"] = ID_APP[k]
            break
    else:
        for rx, k, idapp, nom in CREMAS:
            if re.search(rx, tl) and ("crema" in tl or "tahini" in tl):
                o.update(rol="alergeno", e="🥜", ing={k: 3}, id=idapp, al=nom)
                if "único alimento nuevo" in tl: o["nuevo"] = True
                o["t"] = re.sub(r"\s*\((único alimento nuevo del día|mantener alérgeno)\)", "", t)
                o["mantener"] = "mantener" in tl
                break
        else:
            for rx, e, ing in MANO:
                if re.search(rx, tl):
                    o.update(rol="mano", e=e, ing=ing); break
    if "rol" not in o: o["rol"] = "?"
    c = como(o["t"])
    if c: o["como"] = c
    return o

dias = []
for d in CAL:
    f = d["fecha"]; ses = sesion_de(f)
    dia = {"f": f}
    if d["cocinar"]:
        dia["cocinar"] = True
    for slot in ("de", "c", "ce"):
        partes = [p.strip() for p in d[slot].split(" + ")]
        tit = partes[0]; plato = {"t": tit}
        if tit.startswith("NUEVO ALÉRGENO: "):
            tit = tit[len("NUEVO ALÉRGENO: "):]; tit = tit[0].upper() + tit[1:]
            plato["alergenoNuevo"] = True
            if "gambas" in tit.lower():
                tit = tit.replace(" (al momento; único nuevo del día)", " (al momento)")
                plato.update(id="camaron", al="Crustáceos (gambas)")
            if "soja" in tit:
                tit = tit.replace(" (único alimento nuevo del día)", "")
                plato.update(id="tofu", al="Soja")
            plato["t"] = tit
        letra = next((L for L, b in ses["bases"].items() if b == tit), None)
        if slot != "de" and letra:
            plato.update(base=letra, e=EMO_BASE[tipo_base(tit)], lote=ses["fecha"])
        else:
            plato["e"] = emoji_plato(tit)
            plato["momento"] = "(al momento)" in tit
            plato["t"] = tit.replace(" (al momento)", "")
            receta = next((r for r in PLATOS if re.search(r[0], tit.lower())), None)
            assert receta, (f, slot, tit)
            plato["tiempo"], plato["pasos"], plato["src"] = receta[3], receta[4], receta[5]
        plato["con"] = [comp(p, slot, f) for p in partes[1:]]
        for x in plato["con"]:
            assert x["rol"] != "?", (f, slot, x["t"])
        dia[slot] = plato
    dias.append(dia)

# Lo de la noche anterior: bases a descongelar, muffin, yogur a remojar.
por_f = {d["f"]: d for d in dias}
for d in dias:
    man = por_f.get((D(d["f"]) + dt.timedelta(1)).isoformat())
    if not man: continue
    tareas = []
    for slot, et in (("c", "comida"), ("ce", "cena")):
        p = man[slot]
        if "base" in p:
            if p["lote"] == d["f"]:
                tareas.append({"t": f"Guarda en la nevera la ración de la base {p['base']} para la {et} de mañana (no hace falta congelarla).", "e": "🧊"})
            else:
                tareas.append({"t": f"Pasa del congelador a la nevera la base {p['base']} ({p['t'].split(' con ')[0].lower()}) para la {et} de mañana.", "e": "🧊"})
    de = man["de"]["t"].lower()
    if de.startswith("muffin"): tareas.append({"t": "Pasa un muffin del congelador a la nevera para el desayuno.", "e": "🧁"})
    if de.startswith("yogur") and "soja" not in de: tareas.append({"t": "Deja el yogur con la avena en la nevera, en remojo para el desayuno.", "e": "🥣"})
    if tareas: d["noche"] = tareas

# ---------------------------------------------------------------------------
# Raciones de cada base, guarniciones y compra por sesión
# ---------------------------------------------------------------------------
def ud(k, g):
    """Gramos → texto de compra."""
    nom, es_ud, peso, _ = ING[k]
    if es_ud: return f"{int(math.ceil(g))} ud"
    g = int(math.ceil(g / 10.0) * 10)
    if peso:
        n = max(0.5, math.ceil(g / peso * 2) / 2)
        n_txt = str(int(n)) if n == int(n) else (f"{int(n)} y ½" if n > 1 else "½")
        return f"{g} g · ≈ {n_txt} {'pieza' if n <= 1 else 'piezas'}"
    return f"{g} g"

for s in sesiones:
    rac = defaultdict(int); mano = defaultdict(lambda: defaultdict(int))
    lote = OrderedDict((L, {"t": t, "rac": 0}) for L, t in s["bases"].items())
    compra = defaultdict(float); por = defaultdict(set)
    hay_muffin = False
    for d in dias:
        if not (s["desde"] <= d["f"] <= s["hasta"]): continue
        for slot in ("de", "c", "ce"):
            p = d[slot]
            if "base" in p and p["lote"] == s["fecha"]:
                lote[p["base"]]["rac"] += 1
                for x in p["con"]:
                    if x["rol"] == "mano" and "pizca" not in x["t"]: mano[p["base"]][x["t"]] += 1
            elif "base" not in p:
                ing = next(r[2] for r in PLATOS if re.search(r[0], p["t"].lower() + (" (al momento)" if p.get("momento") else "")))
                if p["t"].lower().startswith("muffin"): hay_muffin = True
                for k, g in ing.items():
                    compra[k] += g; por[k].add("desayunos y platos al momento")
            for x in p["con"]:
                for k, g in x.get("ing", {}).items():
                    compra[k] += g; por[k].add({"fruta": "fruta", "mano": "para la mano", "alergeno": "desayunos"}[x["rol"]])
    if hay_muffin:
        for k, g in MUFFIN_LOTE.items(): compra[k] += g; por[k].add("lote de muffins")
    for L, b in lote.items():
        b["e"] = EMO_BASE[tipo_base(b["t"])]
        b["pasos"], b["pdf"] = pasos_base(b["t"])
        # Con la receta del PDF se cocina su lote entero (sus cantidades son
        # para N raciones): las que sobren, al congelador.
        n = b["rac"]
        if b["pdf"]:
            b["pdfRac"] = {"A": 3, "B": 4, "C": 2, "D": 3}[L]; n = max(n, b["pdfRac"])
        b["ing"] = [[ING[k][0], ud(k, g * n)] for k, g in ings_base(b["t"]).items()]
        b["mano"] = [[t, c] for t, c in mano[L].items()]
        for k, g in ings_base(b["t"]).items():
            compra[k] += g * n; por[k].add(f"base {L}")
    compra["aceite"] += 1; por["aceite"].add("rehogar y aliñar")
    secs = OrderedDict((n, []) for n in SEC)
    for k in sorted(compra, key=lambda k: list(ING).index(k)):
        nom, es_ud, peso, spec = ING[k]
        cant = "1 botella (si no queda)" if k == "aceite" else ("1 frasco (si no queda)" if k.startswith("crema") or k == "tahini" else
               ("1 cuña pequeña" if k == "parmesano" else ud(k, compra[k])))
        if k in ("avena", "harina_maiz", "quinoa", "arroz", "pasta_peq", "pasta_gr", "lentejas", "garbanzos", "frijol"):
            cant = ud(k, compra[k]); por[k].add("revisa la despensa")
        secs[SECCION[k]].append({"k": k, "n": nom, "q": cant, "spec": spec, "para": sorted(por[k])})
    s["lote"] = lote
    s["compra"] = OrderedDict((n, xs) for n, xs in secs.items() if xs)
    del s["bases"]

# ---------------------------------------------------------------------------
# Comprobaciones
# ---------------------------------------------------------------------------
assert len(dias) == 121 and dias[0]["f"] == "2026-11-10" and dias[-1]["f"] == "2027-03-10"
for s in sesiones:
    for L, b in s["lote"].items():
        assert b["rac"] > 0, (s["fecha"], L, b["t"])
# Cada comida/cena es una base de su sesión o un plato al momento.
for d in dias:
    for slot in ("c", "ce"):
        assert "base" in d[slot] or d[slot].get("momento"), (d["f"], slot, d[slot]["t"])
n_al = sum(1 for d in dias if d["de"].get("alergenoNuevo"))
print(f"{len(dias)} días, {len(sesiones)} sesiones, {n_al} alérgenos nuevos", file=sys.stderr)

doc = {"desde": dias[0]["f"], "hasta": dias[-1]["f"], "dias": dias, "sesiones": sesiones,
       "fuente": "Menú semanal de Pablo (8 meses), PDF de la familia (10-11-2026)"}
if "--solo-ver" in sys.argv:
    json.dump(doc, sys.stdout, ensure_ascii=False, indent=1); sys.exit()
s = open(INDEX, encoding="utf-8").read()
js = json.dumps(doc, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
nuevo = f'<script id="pb-menu8-data" type="application/json">{js}</script>'
if 'id="pb-menu8-data"' in s:
    s = re.sub(r'<script id="pb-menu8-data" type="application/json">.*?</script>', lambda m: nuevo, s, flags=re.S)
else:
    ancla = '<script id="pb-plan-data"'
    assert s.count(ancla) == 1
    s = s.replace(ancla, nuevo + "\n  " + ancla)
open(INDEX, "w", encoding="utf-8").write(s)
print("escrito en index.html")
