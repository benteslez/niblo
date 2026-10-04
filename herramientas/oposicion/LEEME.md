# Herramientas del hub de la oposición

Generan el contenido de `oposicion.html` (temas y test real) con el texto legal
LITERAL comprobado por programa. Se ejecutan desde esta carpeta.

## Fuentes de las normas (`boe/`)

- `boe/ids.txt`: clave → identificador (`BOE-A-…` o `CELEX:…`).
- `python3 boe/descargar.py [CLAVE…]`: descarga lo que falte.
  - BOE: API de datos abiertos (`boe.es`, sin `www`). Texto consolidado; si la
    norma no lo tiene, el XML del diario (texto original).
  - EUR-Lex: con Chromium (`eurlex.js`, desafío antibots) y `eurext.js`
    (artículos a JSON). Se guardan `TUE.json`, `TFUE.json`…
- `boe/boe.py`: `ley(k)`, `parrafos(k, bloque)`, `bloque(k, "Artículo 55 bis")`,
  `buscar(k, fragmento)`. Última versión de cada bloque, sin las notas del BOE.
- `boe/ver.py LEY "Artículo 24" ?fragmento`: ver un artículo o buscar.

## Test real

- `examen25L.py`: cuestionario y plantilla del GACE-L 2025 (PDF + imagen).
- `boe/leyes25L.py` + `boe/verif_nuevas.py`: texto legal y comprobación
  plantilla ↔ ley; `boe/mutacion.py`, prueba de mutación.
- `python3 tests_reales.py` → `tests_reales.json` (se incrusta en
  `<script id="tests-reales">`).

## Temas

- Tema I.2: `tema_I2_v4.py` (+ `v4_p*.py`, `v4_util.py`, `fuentes.py`), con
  las normas en `BOE-A-*.txt` (PDF consolidados).
- Temas nuevos: `temas/<id>.py` con la API del BOE (ver `plantilla.py`).

## Pruebas (`pruebas/`)

Playwright contra `python3 -m http.server 8765` en la raíz del repo.
