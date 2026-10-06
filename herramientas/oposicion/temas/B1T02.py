# -*- coding: utf-8 -*-
"""Tema I.2 (B1T02). El contenido del módulo M101 se escribe en m101/part*.py y se reparte en m101/dividir.py."""
import os, sys
AQUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path[:0] = [AQUI, os.path.join(AQUI, "boe"), os.path.join(AQUI, "m101")]
from m101 import dividir

NOTA_ART = "La academia lo recoge entre los artículos preguntados en exámenes oficiales (recorrido del módulo M103). [[M103]]"
# Pill «Examen»: artículos que la academia da como preguntados en exámenes oficiales (M103) y cuestiones de las preguntas oficiales de 2025
MARCAS = [
    (r"Art\. 10 ·", NOTA_ART),
    (r"Art\. 11 ·", NOTA_ART),
    (r"Art\. 13 ·", NOTA_ART),
    (r"Art\. 17 ·", NOTA_ART),
    (r"Art\. 18 ·", NOTA_ART),
    (r"Art\. 20 ·", NOTA_ART),
    (r"Art\. 22 ·", NOTA_ART),
    (r"Art\. 25 ·", NOTA_ART),
    (r"Art\. 27 ·", NOTA_ART),
    (r"Art\. 34 ·", NOTA_ART),
    (r"Art\. 41 ·", NOTA_ART),
]
T = dividir.generar(2)
T.marcar_examen(MARCAS)
T.publicar()
