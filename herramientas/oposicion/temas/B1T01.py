# -*- coding: utf-8 -*-
"""Tema I.1 (B1T01). El contenido del módulo M101 se escribe en m101/part*.py y se reparte en m101/dividir.py."""
import os, sys
AQUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path[:0] = [AQUI, os.path.join(AQUI, "boe"), os.path.join(AQUI, "m101")]
from m101 import dividir

NOTA_ART = "La academia lo recoge entre los artículos preguntados en exámenes oficiales (recorrido del módulo M103). [[M103]]"
# Pill «Examen»: artículos que la academia da como preguntados en exámenes oficiales (M103) y la estructura (preguntas oficiales de 2025)
MARCAS = [
    (r"Art\. 1 ·", NOTA_ART),
    (r"Art\. 8 ·", NOTA_ART),
    ("sec:s4", "Preguntas oficiales de 2025 sobre la estructura de la Constitución (GACE-L pregunta 1; GACE-L extraordinario, preguntas 1, 2 y 3)."),
    ("sec:s5", "Preguntas oficiales de 2025 sobre el Título I y la estructura (GACE-L pregunta 1; GACE-L extraordinario, preguntas 1 a 3)."),
]
T = dividir.generar(1)
T.marcar_examen(MARCAS)
T.publicar()
