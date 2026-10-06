# -*- coding: utf-8 -*-
"""Tema I.3 (B1T03). El contenido del módulo M101 se escribe en m101/part*.py y se reparte en m101/dividir.py."""
import os, sys
AQUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path[:0] = [AQUI, os.path.join(AQUI, "boe"), os.path.join(AQUI, "m101")]
from m101 import dividir

# Pill «Examen»: cuestiones de las preguntas oficiales de 2025
MARCAS = [
    (r"2\.1 Los 12 miembros", "Pregunta oficial de 2025: GACE-L, pregunta 3 (quién propone a los Magistrados; art. 159.1 CE)."),
    (r"1\.1 Cuadro de las competencias", "Preguntas oficiales de 2025: GACE-L extraordinario, preguntas 7 (legitimados del recurso de inconstitucionalidad, art. 162.1.a) CE) y 9 (supuestos de declaración de inconstitucionalidad)."),
    (r"1\.6 La impugnación de disposiciones", "Pregunta oficial de 2025: GACE-L extraordinario, pregunta 8 (art. 161.2 CE)."),
]
T = dividir.generar(3)
T.marcar_examen(MARCAS)
T.publicar()
