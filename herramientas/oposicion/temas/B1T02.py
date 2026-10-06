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
    (r"1\.1 El art\. 54 CE", "Pregunta oficial de 2025: GACE-L extraordinario, pregunta 6 (institución que supervisa la Administración y defiende los derechos del Título I)."),
    (r"1\.3 La elección", "Pregunta oficial de 2025: GACE-L, pregunta 2 (art. 2, apartados 4 y 5, de la LO 3/1981)."),
    (r"3\.1 Por qué importa el 17\.3", "Pregunta oficial de 2025: GACE-L extraordinario, pregunta 4 (derechos que no se pueden suspender; arts. 55.1 y 15)."),
]
T = dividir.generar(2)
T.marcar_examen(MARCAS)
T.publicar()
