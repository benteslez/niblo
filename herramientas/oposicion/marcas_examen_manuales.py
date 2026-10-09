# -*- coding: utf-8 -*-
"""Marcas «Examen» que no salen de un artículo citado literalmente (teoría, datos, planes y estrategias, supuestos prácticos).
Se fusionan en marcas_examen.json con `python3 marcas_examen.py` (aditivo: no se borra nada). `clave` = regex sobre el título de la
unidad («### N.M título», sin el número) o «sec:<id>» para un apartado; si el tema aún no tiene esa unidad (o no tiene apuntes) la
marca queda PENDIENTE en el registro y se coloca sola cuando exista. No tocar la `clave` de una marca ya colocada: al reorganizar un
tema (temario de la academia) se reubica el texto, no la marca."""

def M(tema, clave, *ex, nota=None):
    m = {"tema": tema, "clave": clave, "ex": [e for e in ex]}
    if nota: m["nota"] = nota
    return m

MARCAS = [
    # --- preguntas de test sin texto legal (teoría o datos) ---
    M("B1T01", "sec:s4", ["L", 1]),                                    # nombre del Título I
    M("B1T01", "sec:s4", ["X", 1]),                                    # contenido del Título VIII
    M("B1T01", r"Las disposiciones: 4-9-1-1", ["X", 2]),         # 4 adicionales, 9 transitorias, 1 derogatoria, 1 final
    M("B1T03", r"Cuadro de las competencias", ["X", 7]),               # legitimados del recurso de inconstitucionalidad
    M("B2T01", r"Los países fundadores y la Declaración Schuman", ["L", 18]),
    M("B2T01", r"Cómo leer el cuadro", ["X", 31]),               # Tratado de Fusión (1-7-1967)
    M("B2T03", r"Presidente y Mesa", ["X", 33]),
    M("B2T04", "sec:s1", ["P", 10]),                                   # el TUE es Derecho primario
    M("B2T04", r"La Declaración n\.º 17, relativa a la primacía", ["P", 16]),   # Costa/ENEL: primacía
    M("B2T04", "sec:s12", ["L", 25]),                                  # Van Gend & Loos: efecto directo
    M("B2T05", r"Horizonte Europa", ["L", 27]),
    M("B2T06", r"Qué es un Estado acogido a una excepción", ["L", 17]),   # Dinamarca no forma parte de la eurozona
    M("B2T06", r"Quién lo firmó", ["L", 30]),                     # TECG: República Checa no lo firmó
    M("B3T01", "España Digital 2026", ["L", 31]),                       # eje «Economía del dato e inteligencia artificial»
    M("B3T03", "Programa Nacional de Control de la Contaminación Atmosférica", ["L", 34]),   # 61 medidas en 12 paquetes
    M("B3T04", r"Recursos generales", ["X", 44]),                 # aportaciones del Estado: carácter finalista
    M("B3T06", "sec:s4", ["X", 39]),                                   # Sistema de Acogida 2025: más de 124.000 personas
    M("B3T07", r"El V Plan de Gobierno Abierto", ["L", 39], ["P", 38]),
    M("B3T08", "Plan Estratégico de la Agencia Española de Protección de Datos", ["P", 36]),
    M("B3T09", r"Renovación del Pacto de Estado", ["L", 103]),
    M("B3T09", r"Plan conjunto plurianual", ["X", 53]),
    M("B3T10", "Estrategia de Acción Exterior de España 2025-2028", ["L", 44]),
    M("B3T10", "Plan Director de la Cooperación Española", ["P", 32]),
    M("B3T10", "Estrategia de Desarrollo Sostenible 2030", ["P", 40]),
    M("B5T08", r"Mesa General de las Administraciones Públicas", ["L", 104]),   # sindicatos de la Mesa General de la AGE
    M("B6T02", r"Las tres clasificaciones del gasto", ["L", 84]),            # clasificación orgánica
    M("B6T02", r"Programas y códigos económicos que se preguntan", ["P", 86]),
    M("B6T05", r"Claves del documento MC y de las fases", ["L", 92]),        # MC030
    M("B6T07", r"Concepto y clases de derechos", ["X", 97]),                 # qué es ingreso público
    M("B6T08", r"Cierre de la nómina ordinaria", ["L", 100]),
    M("B6T08", r"Devengo y mensualidades", ["X", 100]),                       # indemnización por residencia

    # --- 2.º ejercicio (supuestos prácticos, GACE-L 2025): artículo o teoría que resuelve cada cuestión ---
]

import plantilla as P

def S(tema, k, art, *ref):
    """Marca de supuesto: art = «Artículo N» o el id de bloque; ref = «I c1 a)» (supuesto I, cuestión 1, apartado a)…"""
    b = art if art in P.boe.ley(k) else P.bid(k, art)
    return {"tema": tema, "k": k, "bloque": b, "ex": ["Supuesto práctico " + r.split(" ", 1)[0] + " (2.º ejercicio GACE-L 2025), cuestión " + r.split(" ", 1)[1] for r in ref]}

MARCAS += [
    # Supuesto I · cuestión 1 (anticipo de caja fija y contrato menor) y supuesto II · cuestión 4 (anticipo de caja fija)
    S("B6T06", "RD725", "a1", "I 1 a)", "II 4 a)"),
    S("B6T06", "RD725", "a2", "I 1 a), b) y c)", "II 4 a)"),
    S("B6T06", "RD725", "a5", "II 4 b)"),
    S("B6T06", "LGP", "a78", "I 1 b)", "II 4 a)"),
    S("B4T05", "LCSP", "Artículo 118", "I 1 a) y d)"),
    S("B6T04", "LGP", "a151", "II 4 b)"),
    S("B6T04", "RD2188", "a23", "II 4 b)"),
    # Supuesto I · cuestión 2 (concurso general de méritos)
    S("B5T04", "RD364", "a42", "I 2 a)"),
    S("B5T04", "RD364", "a44", "I 2 b)"),
    S("B5T04", "RD364", "a47", "I 2 c)"),
    S("B5T04", "RD364", "a48", "I 2 d)"),
    # Supuesto I · cuestión 3 (incompatibilidades)
    S("B5T05", "L53", "acatorce", "I 3 a)"),
    S("B5T05", "L53", "adieciseis", "I 3 a)"),
    S("B5T05", "RD598", "art14", "I 3 b)"),
    S("B5T05", "L53", "acuarto", "I 3 c)"),
    S("B5T05", "L53", "anoveno", "I 3 c)"),
    S("B5T05", "L53", "aseptimo", "I 3 d)"),
    # Supuesto I · cuestión 4 (cesión del contrato, plan de igualdad, revisión de precios)
    S("B4T05", "LCSP", "Artículo 214", "I 4 a) y b)"),
    S("B4T05", "LCSP", "Artículo 71", "I 4 c)"),
    S("B3T09", "LO3_2007", "a45", "I 4 c)"),
    S("B4T05", "LCSP", "Artículo 103", "I 4 d)"),
    # Supuesto I · cuestión 5 (becas: urgencia, plazos y recursos)
    S("B4T11", "L39", "a33", "I 5 a)"),
    S("B4T11", "L39", "a32", "I 5 b)"),
    S("B4T11", "L39", "a68", "I 5 b)"),
    # Supuesto II · cuestión 1 (contrato de obras: modificación y demora)
    S("B4T06", "LCSP", "Artículo 13", "II 1 a)"),
    S("B4T05", "LCSP", "Artículo 205", "II 1 b)"),
    S("B4T05", "LCSP", "Artículo 193", "II 1 c)"),
    # Supuesto II · cuestión 2 (responsabilidad patrimonial)
    S("B4T10", "L39", "a67", "II 2 a)"),
    S("B4T10", "L39", "a81", "II 2 a)"),
    S("B4T10", "L39", "a91", "II 2 b)"),
    S("B4T05", "LCSP", "Artículo 196", "II 2 a)"),
    # Supuesto II · cuestión 3 (recurso de alzada)
    S("B4T12", "L39", "a122", "II 3 a) y d)"),
    S("B4T12", "L39", "a117", "II 3 b)"),
    S("B4T04", "L39", "a40", "II 3 c)"),
    S("B4T04", "L39", "a41", "II 3 c)"),
    # Supuesto II · cuestión 5 (violencia de género de una funcionaria)
    S("B3T09", "LO1_2004", "a21", "II 5 a)"),
    S("B3T09", "LO1_2004", "a24", "II 5 a)"),
    S("B5T02", "TREBEP", "a49", "II 5 a)"),
    S("B5T05", "TREBEP", "a89", "II 5 b)"),
    S("B5T04", "TREBEP", "a82", "II 5 c)"),
]


def S24(tema, k, art, *ref):
    """Supuestos de 2024: ref = «LP I 1» (supuesto I del GACE-L y GACE-P, cuestión 1) o «X II 4» (extraordinario)."""
    b = art if art in P.boe.ley(k) else P.bid(k, art)
    out = []
    for r in ref:
        ex, sup, c = r.split(" ", 2)
        out.append(f"Supuesto práctico {sup} (2.º ejercicio {'GACE-L y GACE-P 2024' if ex == 'LP' else 'GACE-L extraordinario 2024'}), cuestión {c}")
    return {"tema": tema, "k": k, "bloque": b, "ex": out}


MARCAS += [
    # 2.º ejercicio 2024 (turno libre y promoción interna: mismo supuesto; extraordinario aparte). Solo apartados que resuelve un artículo claro.
    S24("B4T12", "L39", "a14", "LP I 1"), S24("B4T04", "L39", "a43", "LP I 1"),
    S24("B6T03", "LGP", "a55", "LP I 2", "X II 3"),
    S24("B5T02", "TREBEP", "a48", "LP I 3"),
    S24("B4T05", "LCSP", "Artículo 159", "LP I 4"), S24("B4T05", "LCSP", "Artículo 147", "LP I 4"),
    S24("B4T06", "LCSP", "Artículo 15", "LP II 1"),
    S24("B4T05", "LCSP", "Artículo 120", "LP II 2"),
    S24("B4T07", "LGS", "a3", "LP II 3"), S24("B4T07", "LGS", "a8", "LP II 3"),
    S24("B4T10", "L40", "a32", "LP II 4", "X I 3"), S24("B4T10", "L39", "a67", "LP II 4"), S24("B4T10", "L39", "a91", "LP II 4", "X I 3"),
    S24("B4T07", "LGS", "a20", "X I 2"),
    S24("B5T06", "TREBEP", "a24", "X I 4"),
    S24("B5T05", "L53", "adiecinueve", "X I 5"),
    S24("B4T05", "LCSP", "Artículo 44", "X II 2"), S24("B4T05", "LCSP", "Artículo 50", "X II 2"),
    S24("B6T06", "RD725", "a1", "X II 4"), S24("B6T06", "RD725", "a2", "X II 4"),
    S24("B5T05", "TREBEP", "a89", "X II 5"),
]



def SX(conv, tema, k, art, *ref):
    """Supuestos y primera parte del 2.º ejercicio anteriores a 2024. conv = clave de EJ; ref = «I 1 a)» (supuesto, cuestión, apartado) o «P2 a)» (primera parte, pregunta)."""
    b = art if art in P.boe.ley(k) else P.bid(k, art)
    out = []
    for r in ref:
        sup, c = r.split(" ", 1)
        if sup.startswith("P"): out.append(f"2.º ejercicio {EJ[conv]}, primera parte, pregunta {sup[1:]} {c}".strip())
        else: out.append(f"Supuesto práctico {sup} (2.º ejercicio {EJ[conv]}), cuestión {c}")
    return {"tema": tema, "k": k, "bloque": b, "ex": out}

EJ = {"LP22": "GACE-L y GACE-P 2022", "L22": "GACE-L 2022", "X22": "GACE-L extraordinario 2022", "L19": "GACE-L 2019"}

MARCAS += [
    # --- 2.º ejercicio 2022 (turno libre y promoción interna, mismo supuesto I y supuesto II; la cuestión 5 del I solo en L) ---
    SX("LP22", "B4T07", "LGS", "a57", "I 1 a)"), SX("LP22", "B4T07", "LGS", "a59", "I 1 a)"), SX("LP22", "B4T07", "LGS", "a66", "I 1 a)"),
    SX("LP22", "B4T07", "LGS", "a31", "I 1 b)"),
    SX("LP22", "B4T05", "LCSP", "Artículo 118", "I 2 a)", "II 3 a)"), SX("LP22", "B4T05", "LCSP", "Artículo 159", "I 2 b)"),
    SX("LP22", "B5T02", "RD33", "a47", "I 3 b)"), SX("LP22", "B5T02", "TREBEP", "a96", "I 3 b)"),
    SX("L22", "B4T10", "L39", "a92", "I 5 a)"), SX("L22", "B4T10", "L39", "a114", "I 5 b) y c)"),
    SX("LP22", "B4T06", "LCSP", "Artículo 13", "II 1 a)"), SX("LP22", "B4T05", "LCSP", "Artículo 135", "II 1 b)"),
    SX("LP22", "B4T05", "LCSP", "Artículo 158", "II 1 b)"), SX("LP22", "B4T05", "LCSP", "Artículo 63", "II 3 b)"),
    SX("LP22", "B4T05", "LCSP", "Artículo 107", "II 4 a)"),
    # --- extraordinario 2022 (L): supuesto I y II ---
    SX("X22", "B4T05", "LCSP", "Artículo 101", "I 1"), SX("X22", "B4T05", "LCSP", "Artículo 118", "I 1"), SX("X22", "B4T05", "LCSP", "Artículo 326", "I 1"),
    SX("X22", "B4T05", "LCSP", "Artículo 198", "I 2"), SX("X22", "B4T13", "LJCA", "a29", "I 2"),
    SX("X22", "B5T01", "TREBEP", "a10", "I 3"), SX("X22", "B5T06", "TREBEP", "a25", "I 3"),
    SX("X22", "B6T03", "LGP", "a52", "I 4"), SX("X22", "B6T03", "LGP", "a63", "I 4"),
    SX("X22", "B4T07", "LGS", "a29", "II 3"), SX("X22", "B4T07", "LGS", "a31", "II 3"),
    # --- 2019 (GACE-L): primera parte y supuestos ---
    SX("L19", "B1T01", "CE", "a167", "P1 a) y b)"), SX("L19", "B1T03", "CE", "a162", "P2 a) y b)"),
    SX("L19", "B1T08", "L40", "a63", "P3 a) y b)"), SX("L19", "B2T02", "PROT2", "Artículo 6", "P4 a)"), SX("L19", "B2T06", "TFUE", "Artículo 127", "P4 b)"),
    SX("L19", "B6T03", "LGP", "a52", "I 1"), SX("L19", "B6T03", "LGP", "a63", "I 1"),
    SX("L19", "B4T09", "LPAP", "a66", "I 3 b)"),
    SX("L19", "B4T05", "LCSP", "Artículo 29", "I 4 a)"), SX("L19", "B4T05", "LCSP", "Artículo 326", "I 4 b)"),
    SX("L19", "B5T02", "TREBEP", "a49", "I 5 a)"), SX("L19", "B5T05", "TREBEP", "a89", "I 5 b)"),
    SX("L19", "B4T11", "L39", "a21", "II 1 a)"), SX("L19", "B4T12", "L40", "a24", "II 1 b)"), SX("L19", "B4T12", "L39", "a122", "II 2"),
    SX("L19", "B4T05", "LCSP", "Artículo 118", "II 4"), SX("L19", "B5T04", "RD364", "a70", "II 5 b)"),
]


# --- GACE-L 2008 (revisadas una a una contra la norma vigente: solo las preguntas cuya respuesta de la plantilla sigue siendo correcta hoy;
# quedan fuera las de normas derogadas o cambiadas: LOFAGE, Ley 30/1992, Ley 30/2007, plazos de la LPAC, complementos, planes y datos de 2008) ---
def L08(tema, k, art, *ns):
    b = art if art in P.boe.ley(k) else P.bid(k, art)
    return {"tema": tema, "k": k, "bloque": b, "ex": [["L08", n] for n in ns]}

MARCAS += [
    L08("B1T01", "CE", "a166", 1), L08("B1T02", "CE", "a17", 2), L08("B1T03", "LOTC", "aveintiseis", 3), L08("B1T04", "CE", "a60", 4),
    L08("B1T05", "CE", "a87", 5), L08("B1T07", "LOPJ", "acincuentaycinco", 7), L08("B1T08", "L40", "a62", 9), L08("B1T08", "L40", "a67", 10),
    L08("B1T10", "CE", "a152", 11), L08("B1T08", "L40", "a70", 12), L08("B1T10", "CE", "a147", 15), L08("B1T10", "CE", "a153", 16),
    L08("B1T10", "CE", "a149", 17, 18, 62), L08("B1T11", "CE", "a141", 19), L08("B1T11", "LRBRL", "a29", 20),
    L08("B2T01", "TUE", "Artículo 49", 22), L08("B2T02", "TFUE", "Artículo 297", 23), L08("B2T02", "TUE", "Artículo 17", 24),
    L08("B2T05", "TFUE", "Artículo 177", 26), L08("B2T04", "TFUE", "Artículo 288", 27), L08("B2T06", "TFUE", "Artículo 39", 28),
    L08("B3T04", "LGSS", "a109", 40), L08("B3T06", "LOEX", "a29", 45), L08("B1T02", "LO3_2007", "dfsegunda", 49),
    L08("B4T03", "CE", "a96", 52), L08("B4T03", "L39", "a128", 53), L08("B4T03", "LGOB", "a24", 54),
    L08("B4T04", "L39", "a35", 55), L08("B4T04", "L39", "a48", 56), L08("B4T04", "L39", "a40", 57),
    L08("B4T08", "LEF", "aveintiuno", 64), L08("B4T10", "L40", "a32", 66), L08("B4T12", "L39", "a4", 67),
    L08("B5T01", "TREBEP", "dfcuaa", 73), L08("B5T01", "TREBEP", "a10", 74), L08("B5T01", "TREBEP", "a67", 75),
    L08("B5T03", "TREBEP", "a70", 76), L08("B5T05", "TREBEP", "a87", 77), L08("B5T05", "TREBEP", "a89", 78), L08("B5T02", "RD33", "a7", 80),
    L08("B5T09", "RDL670", "a41", 84), L08("B5T08", "RDL17", "acuatro", 88),
    L08("B6T01", "LGP", "a28", 90), L08("B6T05", "LGP", "a73", 95), L08("B6T07", "LGT", "a36", 97), L08("B3T04", "LGSS", "a55", 99),
    # teoría (hechos de la historia de la Unión, en el cuadro de los Tratados): Maastricht entró en vigor en noviembre de 1993; el AUE creó el Tribunal de Primera Instancia
    M("B2T01", r"Cómo leer el cuadro", ["L08", 21], ["L08", 25]),
]
