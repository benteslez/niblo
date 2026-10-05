# -*- coding: utf-8 -*-
"""Tema I.3 (B1T03). El contenido del módulo M101 se escribe en m101/part*.py y se reparte en m101/dividir.py."""
import os, sys
AQUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path[:0] = [AQUI, os.path.join(AQUI, "boe"), os.path.join(AQUI, "m101")]
from m101 import dividir
dividir.generar(3).publicar()
