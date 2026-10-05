# Niblo — instrucciones para Claude

## Subir los cambios

- Al terminar un cambio, sin preguntar: commit, push a la rama de trabajo,
  abrir una pull request contra `main` y fusionarla.
- Parar y avisar solo si la pull request tiene conflictos o algún check falla.
- Si el cambio necesita SQL nuevo, va en `supabase/migrations/NNN_nombre.sql`
  (idempotente) y hay que decir claramente que se ejecuta en el SQL Editor de
  Supabase: eso lo hace el usuario.

## Hub de la oposición (`oposicion.html`): contenido de los temas

Regla del usuario para **todos los temas, siempre**: prima la **literalidad**.

- El texto de la norma se copia **literal** del texto consolidado del BOE
  (PDF o web), como bloques `>` en los apuntes, y se comprueba palabra por
  palabra contra la fuente. Nada de paráfrasis donde el examen pregunta letra.
- Lo que no sea texto legal (doctrina del TC, datos de la institución,
  esquemas) se marca como tal y lleva su fuente. No inventar: si falta la
  fuente, se deja «pendiente» y se pide al usuario.
- **Etiqueta de fuente** en todo lo que salga de una fuente oficial (pedido por
  el usuario): `[[COD]]` o `[[COD|https://…]]` en línea, y `> [[COD]]` como
  primera línea de un bloque literal que no sea del BOE (por defecto, BOE). Los
  códigos están en `FUENTES` (`oposicion.html`): BOE, DOUE, PE, CONSEJO_UE,
  COMISION, TJUE, TC, CONGRESO, SENADO, CGPJ, SEGSOCIAL, SEPE, MUFACE, HACIENDA,
  IGAE, TCU, AIREF, DEFENSOR, TRANSPARENCIA, CTBG, GOBES. Fuente nueva → código nuevo.
- **Dónde viven los temas:** cada tema desarrollado es `temas/<id>.json`
  (formato `gestion_hub_config`, un tema, con `_exportedAt`) y se apunta en
  `temas/indice.json` con ese mismo sello. Cambiar un tema = nuevo sello. No se
  incrustan en `oposicion.html`. Herramientas y estado del trabajo:
  `herramientas/oposicion/` y `PROGRESO_TEMAS.md`.
- Cada pregunta de test cita su artículo (`cat`) y se apoya en un fragmento
  literal; los distractores cambian un plazo, una mayoría, un órgano o una
  palabra, como en el examen real (GACE-L).
- Las preguntas de exámenes oficiales se copian literales, con `real`
  (convocatoria, ejercicio y número) y la respuesta de la plantilla oficial.
- Ajustarse al epígrafe literal del programa de la convocatoria.

### Estructura fija de los apuntes (plantilla de todos los temas)

Modelo: tema I.2. Se aplica igual en todos los temas para que se estudien del mismo modo.

- **Mapa del tema** al principio: el epígrafe literal convertido en preguntas
  (una por bloque: I, II, III…), con los artículos y las leyes de cada una.
- **Bloques**: cada uno es un apartado de nivel 1 que se abre con un recuadro
  de guía `@> **▸ Dónde estamos.**` / `@> **▸ Qué vas a ver.**` y se cierra
  (al final de su último subapartado) con `@> **▸ En resumen.**` y el enlace
  `**→ Siguiente: …**`.
- **Numeración estricta**: bloque (I) → apartado (`I.4`, nivel 2) → artículo
  (`### 4.3 …`). Remisiones con el formato `→ II.4` o `→ II.4.2`.
- **Orden**: el de los artículos. Las leyes de desarrollo van dentro de su
  bloque, también en el orden de sus artículos.
- **Cada artículo, siempre igual**: primero el texto literal (`lit`), después
  la ficha (`=> Casilla: texto`, y `=> - punto` para los puntos). La ficha no
  repite la ley: la desmonta.
  - Ficha de **derecho**: Titulares · Contenido · Límites · Protección ·
    ⚠ Ojo en el examen.
  - Ficha de **institución o procedimiento**: Qué · Quién · Cómo ·
    Plazos y mayorías · ⚠ Ojo en el examen.
  - Casilla sin contenido: «—». Nunca se cambia el orden de las casillas.
- Al final: «Cierre 1» (preguntas de exámenes oficiales) y «Cierre 2» (repaso
  por bloques).
- **Preguntas de exámenes oficiales, siempre con el mismo formato** (en el
  apartado del artículo y en «Cierre 1»): recuadro **interactivo** (`%>`) con
  el enunciado y las cuatro opciones **literales** del cuestionario. La
  correcta **no se ve** hasta pulsar una opción: entonces la elegida sale en
  verde o rojo, la correcta en verde, y aparece el porqué de **cada** opción
  (qué dato cambia cada distractor), con citas literales. La corrección del
  test de esas preguntas lleva la misma explicación.
- **Coherencia plantilla ↔ ley, siempre:** la respuesta de la plantilla se
  comprueba contra el texto legal (`examen(..., apoyo=[...])`): los datos que
  la hacen correcta tienen que estar literales en la norma y en esa opción, y
  ningún distractor puede tenerlos todos. Si no casa, el generador se detiene
  y se avisa al usuario (posible error de la plantilla o impugnación); nunca
  se publica una respuesta que contradiga la ley.

### Test real global (`#/real`)

- Solo preguntas **literales** de exámenes oficiales que aporte el usuario
  (cuestionario + plantilla). **Nunca** se añade ninguna inventada ni se
  rellena «de ejemplo»; hasta que las aporte, el test real está vacío.
- Datos en `oposicion.html`, `<script type="application/json" id="tests-reales">`:
  `{"_formato":"tests_reales_v1","examenes":[{ id, titulo, anio,
  acceso:"libre"|"promocion"|"extraordinaria"|"estabilizacion", convocatoria, ejercicio, fecha,
  plantilla:"provisional"|"definitiva", fuente, corte?, minutos?, penalizacion?,
  preguntas:[{ n, q, o:[…], c, tema?, reserva?, anulada?, e? }] }]}`.
  `c` es el índice (0 = a) de la respuesta de la plantilla; `tema` es el
  código del programa (`"I.2"`) si se puede asignar con seguridad; `corte`,
  la puntuación directa mínima publicada para ese examen (solo si hay fuente);
  `minutos` y `penalizacion`, solo para accesos sin condiciones vigentes
  (extraordinaria), copiados de su convocatoria.
- Antes de publicar: enunciado y opciones copiados literales del cuestionario,
  respuesta de la plantilla comprobada contra la ley (como en los apuntes) y
  avisar al usuario de cualquier respuesta que no case. Mientras el usuario no
  decide, la pregunta se publica **retenida** (`retenida: "motivo"`, `RETENIDA` en
  `boe/leyes25X.py`): se ve con su texto legal, pero queda fuera del repaso y del
  examen (como una anulada).
- **Discrepancias** (decisión del usuario, 4-10-2026): cuando la plantilla no casa
  del todo con la norma o la fuente oficial, se **mantiene la respuesta de la
  plantilla** y la pregunta lleva la etiqueta **«⚠ Discrepancia»** y, debajo, la
  explicación (como el texto legal), con citas literales comprobadas
  (`boe/discrepancias.py` → campo `disc: {t, p}`). Hoy: X31, X44, X60, X96 y P91.
- Modo **Repaso (SRS para test)**: SM-2 adaptado a preguntas de cuatro
  opciones (pedido por el usuario): fallada → vuelve en la misma sesión con
  las opciones rebarajadas hasta acertarla y después mañana; dudada → mañana
  y luego el intervalo se acorta (×0,8, mín. 2 días); sabida → 4, 10 días y
  luego × facilidad (tras un fallo, 2 días); facilidad 1,3–2,5; máximo 90
  días; 🔥 rebelde (3+ fallos) sale cada día hasta dos aciertos seguros
  seguidos; se recuerda la opción equivocada. No cambiar sin que lo pida.
- **Opciones siempre barajadas** en cualquier test (la corrección indica la
  letra del examen original). Las preguntas del test real se muestran en
  **pantalla completa**.
- Examen completo: si hay preguntas anuladas, se sustituyen por las de reserva
  por su orden, como en la corrección oficial.
- Al añadir un examen: extraer cuestionario y plantilla del PDF, comprobar la
  plantilla también **sobre su imagen** (transcripción independiente) y, tras
  incrustarlo, volver a comparar las respuestas del HTML publicado con ella.
  Códigos de archivo: L = turno libre, P = promoción interna,
  X = extraordinaria, ST = estabilización.
- **Texto legal de cada pregunta** (campo `ley`: bloques `{t, f, p}`): el
  artículo o apartado LITERAL del texto consolidado del BOE que la resuelve,
  con el dato decisivo en `**negrita**`. Se abre solo al fallar (al acertar,
  plegado). Solo con la norma en las fuentes; si falta, la pregunta va sin
  texto legal y se pide la norma al usuario (nunca de memoria).
  Fuente: la API de datos abiertos del BOE
  (`https://boe.es/datosabiertos/api/legislacion-consolidada/id/<BOE-A-…>/texto`,
  dominio `boe.es` **sin** `www`, que está permitido en la red del entorno).
  Se toma la última versión **vigente** de cada bloque (no las de vigencia futura;
  ver `NO_VIGENTES` en `boe/boe.py`) y se excluyen las notas del BOE
  («Téngase en cuenta…», «Redacción anterior», notas al pie). Antes de
  publicar: dato decisivo literal en la ley y en la opción de la plantilla,
  ningún distractor con todos los datos y prueba de mutación (cambiar la
  respuesta a cualquier otra letra tiene que hacer fallar la comprobación).
  Derecho de la UE (TUE, TFUE, reglamentos): de EUR-Lex (versión consolidada
  cuando exista), con Chromium porque la web tiene un desafío antibots
  (dominios permitidos: `eur-lex.europa.eu` y `*.token.awswaf.com`). Esos
  bloques llevan `f: "CELEX:…"` y se muestran con la etiqueta **DOUE** (no BOE).
- Modo **Examen oficial**: condiciones vigentes del primer ejercicio
  (BOE-A-2025-26262): turno libre, 100 preguntas, 90 minutos y −1/3 (anexo VII,
  2.1.1); promoción interna, 100, 90 y −1/4 (anexo VIII, 3.1.1); extraordinaria,
  las del turno libre, porque es su «llamamiento extraordinario» (base 8.7) y no
  tiene condiciones propias (decisión del usuario, 4-10-2026). Los blancos no
  penalizan. La calificación oficial (0-50) depende del mínimo que fije la
  Comisión: no se inventa una conversión.

## Plan de estudio, Registro y cronómetro (`#/plan`, `#/registro`)

Basado en el módulo M100 «Guía de estudio del temario. El sistema» (PDF y vídeo, aportados por el usuario).

- **Plantilla** (`PLAN_DEF` en `oposicion.html`): 6 vueltas; los bloques I-III van en negro en las
  vueltas 3 y 5; las casillas «barradas» (vuelta extra, que se da al terminar toda la vuelta) van
  partidas en dos mitades horizontales. Las casillas guardan **tiempos**, nunca «visto». Los temas
  fusionados (I.1-3, IV.1-3, IV.5-6, IV.11-13, VI.1-2) **solo se fusionan en la plantilla**; el hub
  conserva los 58 temas del programa. No cambiar la matriz de vueltas sin cotejarla con el PDF.
- **Cronómetro** fijo abajo a la izquierda (`crCrear`): cuenta el tema que abres (`cronSeguir`), se
  puede cambiar a mano (tema, vuelta, vuelta extra) y vuelca al registro cada 2 min y al parar o
  cambiar de tema. Estado en `localStorage` (`gestion_hub_cron_v1`); si nadie lo lleva, se cierra
  en el último latido.
- **Datos** (todo en `prog.mapa`, sin SQL nuevo; se sincroniza clave a clave): `REG:<fecha>:<dispositivo>`
  (tiempos del día por casilla; un registro por día y dispositivo para no pisarse), `PLM:<casilla>`
  (ajuste manual), `PLCFG` (vuelta en curso, extra, seguir tema, fecha del examen), `SIM:<n>:<c>`
  (simulacros), `SUP:<examen>:<intento>:<I|II>` y `SUPA:<examen>:<I|II>` (tabla de supuestos).
- **Orden sugerido, Encaje de vueltas y Supuestos** copian las páginas 2, 5 y 6 del PDF. En la tabla de
  encaje, «Vuelta completa 6» dice «2016-15» (posible errata de «2014-15»): se mantiene literal.
- **Guía de estudio**: resumen estructurado de la transcripción, **sin** lo relativo a cómo era y cómo es
  el examen (petición del usuario).
- **Pill «IMPORTANCIA CRÍTICA»** (`CRITICOS`): los temas con recuadro rojo en el orden sugerido.
- **Constelaciones** en las flashcards: los «art. N» de una tarjeta se enlazan, en el cliente, con el
  texto literal de ese artículo en los apuntes del mismo tema (si el número existe en varias normas,
  hace falta que la tarjeta cite la norma); `CONSTELACIONES` añade artículos relacionados de otros temas.
- Prueba: `herramientas/oposicion/pruebas/plan.js` (con `python3 -m http.server 8765` en la raíz).

## Constitución (`#/ce`) y temas fusionados del módulo M101

- **Temas I.1, I.2 e I.3 (B1T01, B1T02, B1T03) separados**, con el contenido del módulo M101: I.1 estructura, contenido
  (arts. 1 a 55) y reforma; I.2 derechos y deberes, garantías, suspensión y Defensor del Pueblo; I.3 Tribunal
  Constitucional. El contenido se escribe una vez en `herramientas/oposicion/m101/part*.py` y `m101/dividir.py` lo reparte
  (apartados, numeración, remisiones entre temas «→ tema I.2 · III.1», preguntas, flashcards, glosario, hitos);
  `temas/B1T0n.py` solo llama a `dividir.generar(n).publicar()`. Solo la **plantilla del plan** fusiona I.1-3 en una fila.
  `FUSION` (`oposicion.html`) está vacío, pero la lógica sigue por si hace falta; `indice.json` → `retirados` solo se usa
  para quitar temas de los dispositivos (no dejar ids vigentes).
- **Estilo de estos temas** (petición del usuario): explicados, no solo esquemas; texto legal literal del BOE
  (`lit`/`c`, comprobado); cuadros comparativos; reglas mnemotécnicas; cierre con cronología e hitos.
  Pills: `{{IMPORTANTE}}` (la guía o el vídeo dicen «importante/atención») y `{{PRESCINDIBLE}}` (no hace falta
  estudiarlo a fondo; con nota). `{{c:<clave>~texto}}` pinta con el color de un título/capítulo de la CE;
  `{{ir:#/ruta|texto}}` es un botón. Fuente nueva `[[M101]]` = guía y vídeo del módulo (no es texto legal).
- **Si la guía o el vídeo discrepan de la norma vigente, prevalece la norma** y se avisa en el mapa del tema
  (hoy: reforma del 69.3 «19 de mayo de 2026», LO 3/2007 solo parcialmente orgánica, capítulo II del Título I
  = arts. 14 a 38, reelección del Defensor no regulada).
- **Constitución**: `temas/ce.json` (texto literal del BOE consolidado, generado por
  `herramientas/oposicion/ce_datos.py`; su sello va en `indice.json` → `ce`). Los títulos de artículo (arts. 1-52)
  son de la guía M101 (p. 10), NO de la CE; los de 53-55 son un rótulo propio (`propio`). Vistas: texto con
  epígrafes al margen y un color por título/capítulo (`CE_COL`), organigrama (escritorio y móvil) y Test
  Constitución (SRS reutilizando `srsSiguiente`; clave `CEQ:<n>` en `prog.mapa`; la tarjeta baja al pulsar y gira
  con «Ver artículo»). El test abre primero una **ventana de selección** (qué estudiar: hoy, todas, nuevas,
  rebeldes o 🎲 aleatorio; unidades por color; 10/20/30/todos; barajar) y la sesión va en **pantalla completa**
  (`CT.cfg` se recuerda en `gestion_hub_ce_test_v1`). Al regenerar el texto: `python3 ce_datos.py`.
- Prueba: `herramientas/oposicion/pruebas/ce.js` y `m101.js`.

## Descargar apuntes (botón en cada tema)

- Botón «⬇ Descargar apuntes» en la ficha y en el lector de cada tema desarrollado (`data-apuntes`).
  `apuntesHTML(id)` genera un documento A4 (sin los bloques «Lectura profunda de los artículos…», para no incluir la Constitución completa: los artículos de estudio van en cada apartado y la lectura profunda sigue en la app) con el estilo de los temas de ejemplo (portada, índice,
  «SECCIÓN n», recuadros, tablas, glosario, cronología e hitos; **sin** preguntas de repaso, a petición del usuario) usando
  `formatear()`; se abre en una pestaña y lanza «Imprimir → Guardar como PDF» (sin librerías). Si el
  navegador bloquea la ventana, baja un `.html`. Cabecera y pie con `@page` (Chrome/Edge).
- **Maquetación del PDF** (petición del usuario): el índice ocupa **solo la portada** (altura fija, índice compacto);
  **nunca** títulos ni tablas huérfanos: los títulos van con lo que sigue, los párrafos que introducen una tabla, cita o
  lista no se separan de ella, las tablas de hasta 14 filas no se parten (`apCuida`) y las largas repiten la cabecera.
  Para ahorrar páginas, las secciones **no** empiezan en página nueva (solo la 1.ª) y el PDF omite las ayudas de navegación
  de la app («Dónde estamos», «Qué vas a ver», «→ Siguiente», `apSinNav`).
  Al tocar el CSS (`APUNTES_CSS`), regenerar los PDF con `pruebas/apuntes.js` y revisar portada y saltos de página.
- Prueba: `herramientas/oposicion/pruebas/apuntes.js` (genera también el PDF con Chromium).
