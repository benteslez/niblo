# -*- coding: utf-8 -*-
"""Examen GACE-L 2025 EXTRAORDINARIO, primer ejercicio, y plantilla DEFINITIVA."""
from examen_comun import leer
VISTA = ("bacabbabdc" "ddbdbbbbcd" "bdbcbcccda" "abdbddccac" "babdcacbba"
         "adcababbba" "dbdbdcdbda" "ddacbabbac" "cdabdadaad" "bcdaabddac" "ddcad")
qs, plant, avisos = leer("ex25X.txt", "pl25X.txt", r"^\s*2025 - GACE-L EXTRAORDINARIO\s+Página \d+ de \d+\s*$", VISTA,
                         "PLANTILLA DEFINITIVA DE RESPUESTAS DEL PRIMER EJERCICIO EXTRAORDINARIO Cuerpo de Gestión de la Administración Civil del Estado - Ingreso Libre")
