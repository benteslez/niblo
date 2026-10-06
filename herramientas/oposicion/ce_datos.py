# -*- coding: utf-8 -*-
"""Genera temas/ce.json: la Constitución Española COMPLETA, literal del texto
consolidado vigente del BOE (BOE-A-1978-31229), con su estructura (partes, títulos,
capítulos, secciones). Lo usa la vista «Constitución» (#/ce) de oposicion.html.

Los «títulos de artículo» (rúbricas didácticas) NO son texto de la CE (la CE no los
tiene): son los de la guía de estudio M101 (arts. 1 a 52, tabla de la p. 10). Los de
los arts. 53 a 169 no figuran en esa tabla: llevan `propio: true` (rótulo breve nuestro, redactado del texto literal del artículo; pedido por el usuario el 6-10-2026).

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
 42: "Salvaguardia de los derechos de los trabajadores españoles en el extranjero", 43: "Derecho a la salud", 44: "Cultura e investigación científica",
 45: "Protección del medio ambiente", 46: "Protección del patrimonio histórico-artístico", 47: "Derecho a una vivienda digna y adecuada",
 48: "Fomentar la participación de la juventud",
 49: "Las personas con discapacidad ejercen los derechos previstos en este Título en condiciones de libertad e igualdad reales y efectivas",
 50: "Pensiones públicas, periódicas y actualizadas para la tercera edad", 51: "Consumidores y usuarios, defensores y protegidos",
 52: "Organizaciones profesionales cuya estructura interna y funcionamiento deberá ser democrático"}
# Art. 42: la guía dice «inmigrantes españoles»; la CE habla de «trabajadores españoles en el extranjero» (prevalece la norma).
# Los arts. 53 a 169 no están en la tabla de la guía: rótulo breve propio (marcado «propio»).
PROPIAS = {53: "Vinculación, reserva de ley y tutela de los derechos", 54: "El Defensor del Pueblo", 55: "Suspensión de derechos y libertades",
 56: "El Rey: Jefe del Estado, inviolabilidad y refrendo", 57: "Sucesión en la Corona", 58: "La Reina consorte o el consorte de la Reina",
 59: "La Regencia", 60: "La tutela del Rey menor", 61: "Proclamación y juramento del Rey",
 62: "Funciones del Rey", 63: "El Rey y las relaciones internacionales: embajadores, tratados, guerra y paz", 64: "El refrendo de los actos del Rey",
 65: "La Casa del Rey y la dotación de la Familia Real", 66: "Las Cortes Generales: composición y funciones", 67: "Incompatibilidad entre Cámaras y prohibición del mandato imperativo",
 68: "El Congreso de los Diputados: composición y elección", 69: "El Senado: composición y elección", 70: "Inelegibilidad e incompatibilidades de Diputados y Senadores",
 71: "Inviolabilidad, inmunidad y fuero de los parlamentarios", 72: "Reglamentos y autonomía de las Cámaras", 73: "Períodos de sesiones",
 74: "Sesiones conjuntas de las Cámaras", 75: "Funcionamiento en Pleno y por Comisiones", 76: "Comisiones de investigación",
 77: "Peticiones dirigidas a las Cámaras", 78: "Las Diputaciones Permanentes", 79: "Quórum y mayorías para adoptar acuerdos",
 80: "Publicidad de las sesiones plenarias", 81: "Las leyes orgánicas", 82: "Delegación legislativa de las Cortes en el Gobierno",
 83: "Límites de las leyes de bases", 84: "Proposiciones de ley o enmiendas contrarias a una delegación", 85: "Los decretos legislativos",
 86: "Los decretos-leyes", 87: "La iniciativa legislativa", 88: "Los proyectos de ley",
 89: "Tramitación de las proposiciones de ley", 90: "Aprobación de los proyectos de ley: veto y enmiendas del Senado", 91: "Sanción y promulgación de las leyes",
 92: "El referéndum consultivo", 93: "Tratados que atribuyen competencias derivadas de la Constitución", 94: "Autorización de las Cortes para obligarse por tratados",
 95: "Tratados internacionales contrarios a la Constitución", 96: "Eficacia y denuncia de los tratados internacionales", 97: "Funciones del Gobierno",
 98: "Composición y estatuto del Gobierno", 99: "Propuesta e investidura del Presidente del Gobierno", 100: "Nombramiento y cese de los demás miembros del Gobierno",
 101: "Cese del Gobierno", 102: "Responsabilidad criminal de los miembros del Gobierno", 103: "La Administración Pública y la función pública",
 104: "Las Fuerzas y Cuerpos de seguridad", 105: "Audiencia, acceso a archivos y procedimiento administrativo", 106: "Control judicial de la Administración y responsabilidad patrimonial",
 107: "El Consejo de Estado", 108: "Responsabilidad solidaria del Gobierno ante el Congreso", 109: "Información y ayuda a las Cámaras",
 110: "Presencia de miembros del Gobierno en las Cámaras", 111: "Interpelaciones y preguntas", 112: "La cuestión de confianza",
 113: "La moción de censura", 114: "Consecuencias de la pérdida de la confianza del Congreso", 115: "La disolución de las Cámaras",
 116: "Los estados de alarma, excepción y sitio", 117: "Principios del Poder Judicial", 118: "Obligación de cumplir las sentencias",
 119: "Justicia gratuita", 120: "Publicidad y forma de las actuaciones judiciales", 121: "Error judicial y funcionamiento anormal de la justicia",
 122: "Ley Orgánica del Poder Judicial y Consejo General del Poder Judicial", 123: "El Tribunal Supremo", 124: "El Ministerio Fiscal",
 125: "Acción popular, jurado y tribunales consuetudinarios", 126: "La policía judicial", 127: "Incompatibilidades y asociación de jueces, magistrados y fiscales",
 128: "Subordinación de la riqueza al interés general e iniciativa pública", 129: "Participación en la Seguridad Social, en la empresa y en los medios de producción", 130: "Modernización y desarrollo de los sectores económicos",
 131: "La planificación económica", 132: "Bienes de dominio público, comunales y patrimonio del Estado", 133: "La potestad tributaria",
 134: "Los Presupuestos Generales del Estado", 135: "Estabilidad presupuestaria y deuda pública", 136: "El Tribunal de Cuentas",
 137: "Organización territorial del Estado", 138: "Solidaridad y equilibrio económico entre territorios", 139: "Igualdad de derechos en todo el territorio",
 140: "Autonomía de los municipios", 141: "La provincia", 142: "Las Haciendas locales",
 143: "Acceso a la autonomía: iniciativa del proceso autonómico", 144: "Facultades de las Cortes por motivos de interés nacional", 145: "Prohibición de federación y convenios entre Comunidades Autónomas",
 146: "Elaboración del proyecto de Estatuto", 147: "Contenido y reforma de los Estatutos", 148: "Competencias que pueden asumir las Comunidades Autónomas",
 149: "Competencias exclusivas del Estado", 150: "Leyes marco, transferencia o delegación y leyes de armonización", 151: "Acceso rápido a la autonomía",
 152: "Organización institucional de las Comunidades Autónomas y Tribunal Superior de Justicia", 153: "Control de la actividad de las Comunidades Autónomas", 154: "El Delegado del Gobierno",
 155: "Control extraordinario: incumplimiento de obligaciones por una Comunidad Autónoma", 156: "Autonomía financiera de las Comunidades Autónomas", 157: "Recursos de las Comunidades Autónomas",
 158: "Asignaciones del Estado y Fondo de Compensación", 159: "Composición del Tribunal Constitucional", 160: "El Presidente del Tribunal Constitucional",
 161: "Competencias del Tribunal Constitucional", 162: "Legitimación para el recurso de inconstitucionalidad y el amparo", 163: "La cuestión de inconstitucionalidad",
 164: "Las sentencias del Tribunal Constitucional", 165: "Ley orgánica del Tribunal Constitucional", 166: "Iniciativa de la reforma constitucional",
 167: "Procedimiento ordinario de reforma", 168: "Procedimiento agravado de reforma", 169: "Límites temporales a la reforma"}

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

# Anotaciones del módulo M103 (marcas y comentarios de la academia sobre los arts. 1-52); cada frase marcada tiene que ser literal.
from m103_datos import M103, LEYENDA, NIVELES, M107_UNIDADES, M107_ARTS
_txt = {A["n"]: " ".join(" ".join(A["p"]).split()) for t in titulos for A in todos(t)}
for _n, _d in M103.items():
    assert _n in _txt, _n
    for _f, _c in _d.get("marks", []):
        assert _f in _txt[_n], ("M103: la frase no es literal", _n, _f)
        assert _c in ("am", "vd", "az", "lo"), (_n, _c)
M103_OUT = {"_fuente": "Módulo M103 «Artículos CE · Lectura y explicación» (documento subrayado y vídeo): marcas y comentarios de la academia, no texto de la CE. Las marcas azules se completan con el art. 55.1 CE.",
            "leyenda": [list(x) for x in LEYENDA], "niveles": NIVELES,
            "m107": {"_fuente": "Módulo M107 «Contenido de repaso sobre la CE» (PDF y vídeo): reglas para memorizar la estructura; no es texto de la CE.", "unidades": M107_UNIDADES, "arts": {str(k): v for k, v in M107_ARTS.items()}},
            "arts": {str(n): {k: v for k, v in d.items() if k != "marks"} | ({"marks": [list(m) for m in d["marks"]]} if d.get("marks") else {}) for n, d in M103.items()}}

sello = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")
out = {"_format": "ce_v1", "_exportedAt": sello, "_fuente": "BOE-A-1978-31229 (texto consolidado vigente)", "preambulo": preambulo,
       "titulos": titulos, "disposiciones": disp, "firma": firma, "m103": M103_OUT}
open(os.path.join(RAIZ, "temas", "ce.json"), "w", encoding="utf-8").write(json.dumps(out, ensure_ascii=False, separators=(",", ":")))
ip = os.path.join(RAIZ, "temas", "indice.json"); idx = json.load(open(ip, encoding="utf-8")); idx["ce"] = sello
json.dump(idx, open(ip, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ce.json:", len(nums), "artículos,", len(disp), "disposiciones,", sum(len(p[1]) for p in [("", preambulo)]), "párrafos de preámbulo")
