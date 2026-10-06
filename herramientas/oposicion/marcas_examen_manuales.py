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
