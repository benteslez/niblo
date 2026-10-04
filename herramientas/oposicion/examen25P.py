# -*- coding: utf-8 -*-
"""Examen GACE-P 2025 (promoción interna), primer ejercicio, y plantilla DEFINITIVA."""
from examen_comun import leer
# Transcrita a mano de la IMAGEN de la plantilla (filas de diez; X = ANULADA; reserva al final).
VISTA = ("abbdabcdbc" "bdbbabbdca" "bcbabbdbba" "cccbbcddbb" "daddbcbbdb"
         "bXdcadcdbb" "dbcbbcddcd" "ccbabacdbc" "bccaabccda" "dddbdbbbca" "ccbda")
qs, plant, avisos = leer("ex25P.txt", "pl25P.txt", r"^\s*2025 - GACE-P\s+Página \d+ de \d+\s*$", VISTA,
                         "PLANTILLA DEFINITIVA DE RESPUESTAS DEL PRIMER EJERCICIO Cuerpo de Gestión de la Administración Civil del Estado - Promoción Interna")
