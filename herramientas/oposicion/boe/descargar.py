# -*- coding: utf-8 -*-
"""Descarga (si faltan) los textos de las normas de ids.txt a esta carpeta:
BOE-A-… → API de datos abiertos del BOE (texto consolidado; si la norma no está
consolidada, el XML del diario con el texto original). CELEX:… → se extraen con
eurlex.js + eurext.js (navegador) y se guardan como <clave>.json.
Uso: python3 descargar.py [CLAVE …]"""
import os, sys, subprocess, urllib.request, urllib.error
AQUI = os.path.dirname(os.path.abspath(__file__))
IDS = dict(l.split() for l in open(os.path.join(AQUI, "ids.txt")) if l.strip())


def baja(url, dest, accept="application/xml"):
    r = urllib.request.Request(url, headers={"Accept": accept})
    datos = urllib.request.urlopen(r, timeout=120).read()
    open(dest, "wb").write(datos)
    return datos


for k in (sys.argv[1:] or IDS):
    ref = IDS[k]
    if ref.startswith("CELEX:"):
        dest = os.path.join(AQUI, k + ".json")
        if os.path.exists(dest):
            continue
        html = os.path.join(AQUI, k + ".html")
        url = "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=" + ref
        subprocess.run(["node", os.path.join(AQUI, "eurlex.js"), url, html], check=True)
        subprocess.run(["node", os.path.join(AQUI, "eurext.js"), html, dest], check=True)
        print("descargado", k, ref)
        continue
    dest = os.path.join(AQUI, k + ".xml")
    if os.path.exists(dest):
        continue
    try:
        d = baja(f"https://boe.es/datosabiertos/api/legislacion-consolidada/id/{ref}/texto", dest)
    except urllib.error.HTTPError:
        d = b""   # sin texto consolidado
    if b"<code>200</code>" not in d[:400]:
        baja(f"https://boe.es/diario_boe/xml.php?id={ref}", dest)
    print("descargado", k, ref)
