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

### Guía de la academia (PDF) = índice del tema (regla del usuario, 6-10-2026)

- Cuando el usuario aporta un **PDF de la academia** para un tema, **su orden y sus puntos son el índice del tema**: los epígrafes en grande (bloques) y los
  puntos en negrita de la guía son los bloques y apartados de los apuntes, **en ese orden y con esos nombres**; no se reordena ni se inventa otra estructura.
  Cada punto lleva el contenido que le corresponde (texto literal de la norma, fichas, cuadros y esquemas de la guía en su sitio).
- Se puede **ampliar** un punto con la **legislación vigente** (texto literal consolidado, fuentes oficiales) cuando sea oportuno y necesario para estudiarlo
  mejor; lo añadido no está en la guía y se dice (p. ej. «ampliación de la guía» en el título o un aviso). Si la guía discrepa de la norma, prevalece la norma.
- Si un punto de la guía solo se desarrolla en otro tema (p. ej. instituciones), se remite allí en lugar de duplicarlo.

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
- Al final: el **Cierre** (repaso por bloques, con «Cómo se pregunta»). Las **preguntas de exámenes oficiales NO van en los apuntes**
  (petición del usuario, 5-10-2026): viven en el **test** del tema («Práctica activa»). Los generadores pueden seguir escribiendo un
  apartado «Cierre 1» con recuadros `%>`: `Tema._cierre1_al_test` (en `plantilla.py`, al publicar) lo quita, pasa al test las preguntas
  que falten (con su `real` y el porqué de cada opción) y reescribe las remisiones «→ Cierre 1» («está en el test»).
- **Preguntas de exámenes oficiales, siempre con el mismo formato** (en el
  apartado del artículo; en «Cierre 1» solo en el generador, no se publica): recuadro **interactivo** (`%>`) con
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
- **Cronómetro** discreto abajo a la izquierda (`crCrear`; petición del usuario): cerrado es un botón ⏱ pequeño y tenue, y
  si corre solo un punto rojo; se abre al tocarlo (hora, Estudiar/Parar y ajustes) y se cierra al tocar fuera; **no se ve**
  en las sesiones a pantalla completa (`body.real-abierto`) aunque siga contando. Cuenta el tema que abres (`cronSeguir`), se
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
- **Flashcards de cada tema** (`hubFc`, pestaña Flashcards): por defecto se **deslizan** como en el Test Constitución (derecha = la sabía →
  dominada y sale del mazo; izquierda = no la sabía → al final; arriba = dudé → vuelve a salir 4 tarjetas más adelante), con botones
  ✗ / 🤔 / ✓ siempre visibles y toda la tarjeta pulsable para voltear; el chip «👆 Deslizar» cambia al modo clásico de botones
  (`gestion_hub_fc_modo_v1`). Sin giro 3D: cada cara crece con su contenido. Reutiliza `ceDeslizar`.
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
- **Sin duplicados en los apuntes** (petición del usuario; `_limpia` en `m101/dividir.py`): estos tres temas no llevan
  «Repaso por bloques» ni «Preguntas de la guía» (las preguntas están en el test), el mapa no repite «Qué vas a aprender»
  (lo dice su tabla «El hilo del tema»), no hay línea «Qué vas a ver» (el índice lateral ya la da) y un apartado
  «Cuadro…» no lleva «En resumen». Los bloques pueden cerrarse con su «En resumen» (no es obligatorio: un apartado «Cuadro…» ya es el resumen) y el último apartado enlaza con el tema siguiente. Los textos de `dividir.py` que ya usan los códigos nuevos (`s0`) no se pasan por `_remisiones`.
  Esto prevalece sobre «Cierre 1 / Cierre 2» de la plantilla general para estos temas.
- **Estilo de estos temas** (petición del usuario): explicados, no solo esquemas; texto legal literal del BOE
  (`lit`/`c`, comprobado); cuadros comparativos; reglas mnemotécnicas; cierre con cronología e hitos.
  Pills: `{{IMPORTANTE}}` (la guía o el vídeo dicen «importante/atención») y `{{PRESCINDIBLE}}` (no hace falta
  estudiarlo a fondo; con nota). `{{c:<clave>~texto}}` pinta con el color de un título/capítulo de la CE;
  `{{ir:#/ruta|texto}}` es un botón. Fuente nueva `[[M101]]` = guía y vídeo del módulo (no es texto legal).
- **Vídeo M101-02** (TC, Defensor, reforma; transcripción aportada por el usuario): sus reglas de memoria están en I.1 · IV.1.4 y IV.6, I.2 · V.1 (2.4) y I.3 · I.3 y II.2; las notas del propio documento mandan: el PDF/la ley prevalecen sobre el vídeo (Defensor: mayoría **absoluta** del Senado; reforma agravada: la del PDF) y el art. 49 del PDF «con epígrafes» está sin actualizar (se usa el BOE consolidado).
- **Módulo M106** (ampliación del Defensor del Pueblo; PDF aportado por el usuario): ya estaba casi todo en I.2 · V; se añadió la admisión y rechazo de quejas (art. 17 LO 3/1981, I.2 · V.2 apartado 2.7) y dos flashcards. El PDF dice «reelegible»: la LO 3/1981 no lo regula (prevalece la ley, aviso en el mapa de I.2).
- **Descargar apuntes de la Constitución** (botón en `#/ce`, `ceApuntesHTML`/`descargarApuntesCE`): documento A4 generado **de los datos**, así que lo que se añada entra solo: guía y leyenda M103, estructura y reglas M107 (tabla con «inicio + N»), el organigrama de la app (se reutiliza `ceVerOrg` y sus CSS `.og*`), niveles de protección, arts. 1-55 anotados (subrayado, pills, comentarios; siempre con las anotaciones aunque el interruptor esté apagado) y todos los apartados «Cuadro…» de I.1-I.3 más «Los títulos y sus artículos» y «El Título I por dentro». Lleva la **Constitución completa** (Preámbulo, arts. 1-169 y disposiciones; las anotaciones M103/M107 salen donde las haya y lo que se añada entra solo): la parte dogmática y, en **página nueva**, la parte orgánica (Título II). La estructura (sección 2) y cada mitad del organigrama (dogmática / orgánica, en página nueva, ajustada con `zoom` a su hoja) caben en una página. Comparte `abrirApuntes` con los apuntes de tema.
- **Módulo M107** (repaso de la estructura de la CE; PDF + vídeo): las reglas de memoria van en `m103_datos.py` (`M107_UNIDADES`: una nota por título, capítulo, sección, preámbulo y disposiciones; `M107_ARTS`) → `ce.json` → `m103.m107`, y se ven en `#/ce/texto` con el mismo interruptor (pill 🛡 «nivel de protección» calculado por artículo en `ceNivel`); en I.1 solo la regla «inicio + N = fin» (II.2, 2.1) y las reglas del Título I (II.3, 3.1). Las dos preguntas GACE 2018 del PDF están en los tests (I.1 y I.2) con su `real`.
- **Módulo M103** (lectura y explicación de los arts. 1-52: PDF subrayado + vídeo): vive **solo en `temas/ce.json` → `m103`** (generado por
  `ce_datos.py` desde `herramientas/oposicion/m103_datos.py`; cada frase marcada tiene que ser literal del artículo): pills **«Examen»** (roja, antes 🟧),
  🟨 importante, 🟩 coletilla, 🟦 se limita en excepción y sitio (completado con el art. 55.1), 🌸 ley orgánica, subrayado en el texto y comentario
  de la academia por artículo. Se ve en `#/ce/texto` (botón «🚫 Apagar leyendas» / «🖍 Encender leyendas»: texto limpio sin subrayados, pills ni comentarios; el mismo botón está en el dorso de las tarjetas del Test Constitución; se recuerda en `KEY_M103`) y en el reverso del Test Constitución; el tema I.1 (III.1, 1.1 y 1.2) solo
  explica los niveles y el código de colores y remite a la Constitución. No copiar estas anotaciones en los temas.
- **Si la guía o el vídeo discrepan de la norma vigente, prevalece la norma** y se avisa en el mapa del tema
  (hoy: reforma del 69.3 «19 de mayo de 2026», LO 3/2007 solo parcialmente orgánica, capítulo II del Título I
  = arts. 14 a 38, reelección del Defensor no regulada).
- **Constitución**: `temas/ce.json` (texto literal del BOE consolidado, generado por
  `herramientas/oposicion/ce_datos.py`; su sello va en `indice.json` → `ce`). Los títulos de artículo (arts. 1-52)
  son de la guía M101 (p. 10), NO de la CE; los de 53-55 son un rótulo propio (`propio`). Vistas: texto con
  epígrafes al margen y un color por título/capítulo (`CE_COL`), organigrama (escritorio y móvil) y Test
  Constitución (SRS propio `ceSiguiente`, más corto que el del test real: sabía 2·4·8·14·21 días y luego ×1,3 con máximo de 30; dudé la mitad, mín. 2; no la sabía mañana; dominada = intervalo ≥ 14; lo guardado con más de 30 días vence a los 30 desde el último repaso; clave `CEQ:<n>` en `prog.mapa`; la tarjeta baja al pulsar y gira
  con «Ver artículo»). El test abre primero una **ventana de selección** (qué estudiar: hoy, todas, nuevas,
  rebeldes o 🎲 aleatorio; unidades por color; 10/20/30/todos; barajar) y la sesión va en **pantalla completa** (`.ce-pc`: barra arriba, tarjeta que ocupa el resto —cada cara se desplaza por dentro, nunca se corta— y botones de respuesta siempre visibles abajo; **toda la tarjeta** es pulsable: revela y luego gira entre frente y artículo, sin giro 3D por el iPhone)
  La ventana de selección tiene **modo**: «SRS con botones» o «Flashcards: deslizar» (`cfg.modo`; arrastrar la tarjeta a la derecha =
  la sabía, a la izquierda = no la sabía y vuelve a salir, hacia arriba = dudé (si la cara cabe sin desplazarse; `ceAjustaFija`); mismos filtros, mismo SRS `ceSiguiente`, mismo revelar/girar al tocar; `ceDeslizar`;
  también ← → ↑).   (`CT.cfg` se recuerda en `gestion_hub_ce_test_v1`). Al regenerar el texto: `python3 ce_datos.py`.
- Prueba: `herramientas/oposicion/pruebas/ce.js` y `m101.js`.

## Test de cada tema: preguntas de la academia y de examen real

- **Preguntas «Academia»** (módulos M104 «Test de repaso» y M105 «Test de tema», PDF aportados por el usuario): 52 preguntas en
  `herramientas/oposicion/m101/part12.py` (`AC(...)`), repartidas por `t` entre I.1 (18), I.2 (23) e I.3 (11). Enunciado y opciones
  literales del documento, respuesta de **su clave** (M104: tabla final; M105: tabla final y rojo en las soluciones) comprobada contra
  el texto vigente (`T.q` exige fragmentos literales); la explicación es la solución del documento (artículo citado, literal
  verificado) y sale **siempre**, acierte o falle. Campo `ac` = «M105 · pregunta 12»; chip **🎓 Academia** en la selección del test.
  Si el documento cita mal un artículo o la clave se ha quedado corta, va un `⚠` en la explicación y **prevalece la norma**
  (hoy: M104 14 y 16 citan 159.6 y 159.3, son 159.1 y 159.4; M105 27 y 32, tras la reforma de 2026 del art. 69.3).
- **Preguntas retenidas del test de un tema** (`retenida: "motivo"`, `AC(..., retenida=…)` en `m101/part12.py`): la pregunta queda en los datos pero **fuera del test** (`qsTest`). Hoy ninguna: M105 27 y 32 se **reescribieron actualizadas** a la reforma de 2026 (art. 69.3) como «M105 · pregunta 27 (actualizada…)», «32 (actualizada: reforma de 2024)» y «32 (actualizada: última reforma)»; el resto de preguntas de la academia sigue literal del documento.
- **Literales parciales con «[…]»** (`plantilla.ELISION`, lo activa `m101/dividir.py`): cuando `lit()` omite párrafos del artículo, lo marca con una línea «[…]». Marcas «Examen» con pista `en` (regex sobre el título de la unidad) cuando un artículo se cita en varias unidades; `marcas_examen.EXCLUIR` lista las marcas heurísticas duplicadas que no deben volver a crearse.
- **I.3 · I.4 Organización del Tribunal** (arts. 6-15 y 23 LOTC) y los apartados de requerimiento previo sobre tratados, recurso previo contra Estatutos, conflictos negativos y alcance de las sentencias (arts. 38.2-3, 40, 93) son **ampliación de la guía** (la dicen los apuntes): el epígrafe oficial incluye «organización» y el test lo pregunta.
- **Preguntas del test real global en cada tema** (`realesDeTema`): las de `tests-reales` cuyo `tema` es el del tema (I.1, I.2, I.3;
  no anuladas ni retenidas) entran en «📋 De examen real» y en «Todas», con su texto legal y su discrepancia. Su progreso es **propio
  del tema** (`B1T0n:q:<hash>`), independiente del test real global (`R:<examen>:<n>`): lo que se conteste en un sitio no cambia el
  otro. Corregido: L1 (nombre del Título I) y P51 (art. 9.3) pasan a I.1.
- El test de un tema (herramienta «Test» del lector) se abre en **pantalla completa** (`.panel.completo`, petición del usuario; oculta el cronómetro mientras está abierto).
- Prueba: `herramientas/oposicion/pruebas/test_academia.js`.

## Estética de los apuntes (lector y PDF)

- **Tablas más anchas que la pantalla** (móvil vertical): `.ap-cuerpo .tabla-wrap` se **desliza en horizontal** (`overflow-x:auto`) y lleva la pista «↔ Desliza para ver más columnas» hasta que se desliza (clase `desliza`, puesta por JS). En el PDF no se desliza (`overflow:visible`).

- Petición del usuario: apuntes limpios y visuales, con conceptos en escala de colores. Recuadros con etiqueta (`CJ_CSS` en `oposicion.html`, común al lector y al PDF): `+>` **Concepto clave** (azul), `!>` **Atención examen** (rojo), `@> **▸ En resumen.**` **Síntesis** (amarillo), `?>` **Ojo** (ámbar), `@> **▸ Dónde estamos.**` guía (gris). `&>` = **esquema de procedimiento** (pasos numerados con un color por institución; véase «Tema II.1 y módulo M108»). `~>` = **mapa conceptual** (`~> Título`, `~> # Raíz`, una rama por línea `Rama | descripción | subcaja`); I.1-I.3 lo generan solo de la tabla «El hilo del tema» (`_con_mapa` en `m101/dividir.py`).
- Los términos del glosario salen solos como «Concepto clave» al empezar su apartado (`conConceptos`, máx. 2 por apartado). Tablas con cabecera azul y filas alternas; subtítulos de artículo (`###`) con la misma tipografía que los subapartados; los títulos de apartado de la lista (01 Mapa del tema…) usan la tipografía del título de la cabecera, sin serif (peticiones del usuario).
- Reformas de la CE (I.1 · I.2): los textos de cada reforma (exposición de motivos, preámbulo, artículo único) van en **violeta** (`lit-ref`, se detecta por el título del bloque) y el artículo definitivo en el color normal; `^>` = «Cómo era antes» (resumen propio, sin citar el texto anterior, para no confundirlo con el redactado vigente).
- Los códigos de fuente pueden llevar dígitos (`[[M101]]`).

## Tema II.1 (B2T01) y módulo M108

- **Módulo M108** (guía de estudio y vídeo del tema II.1; PDF y transcripción aportados por el usuario): fuente `[[M108]]`
  (no es texto legal). El texto del PDF está en `herramientas/oposicion/m108/guia.txt` y `temas/B2T01.py` comprueba contra él
  cada cita (`cg()`) y cada celda de sus cuadros (`tabla(..., ver=...)`, `TRAT`). Ojo: el cuadro impreso dice «Procedimiento **de**
  alerta temprana» y la capa de texto del PDF no; se compara con la variante sin «de».
- **Orden de los apuntes = índice de la guía** (petición del usuario, 6-10-2026): cinco bloques, los de la guía. I La Unión Europea: antecedentes
  (I.1 Schuman y Día de Europa) · II Objetivos y naturaleza jurídica. Los Tratados originarios y modificativos (II.1 naturaleza jurídica; II.2 art. 1;
  II.3 valores, art. 2; II.4 objetivos, art. 3; II.5 Tratados originarios y modificativos, con el cuadro maestro) · III El TUE y el TFUE (III.1 origen y
  estructura; III.2 arts. 4 y 5; III.3 art. 6; III.4 art. 7 y mayoría cualificada; III.5 art. 8; III.6 arts. 9 a 12; III.7 disposiciones finales y revisión, art. 48;
  III.8 TFUE) · IV El proceso de ampliación (IV.1 art. 49 y Copenhague; IV.2 art. 50; IV.3 ampliaciones, retiradas y candidaturas) · V Las cooperaciones reforzadas
  (V.1 concepto y condiciones, art. 20 TUE y arts. 326 a 328; V.2 arts. 329 a 331; V.3 arts. 332 a 334). Los cuadros, el cuadro maestro y los esquemas están en el
  punto de la guía al que pertenecen. **Ajustado a la guía y sin duplicados** (petición del usuario, 6-10-2026): cada punto abre con **el texto de la guía** reescrito y
  precisado con la norma (`N1`, `N2`, `N3` en `B2T01.py`; I.1 · 1.1, II.2 · 2.1, II.5 · 5.1, y los de II.1) y se quitó lo que no está en la guía o repetía otra cosa: CED y Mesina,
  preámbulo del TUE, la historia de cada Tratado de las fichas del PE (la dan el cuadro y la guía), la tabla de fechas que repetía el cuadro, los arts. 52, 54 y 55,
  el cuadro «Consejo / Consejo Europeo» (queda la regla del vídeo), TFUE 8.2-8.3, el proceso de adhesión «en la práctica» y la tabla de ampliaciones de la ficha del PE
  (la da la guía). Las remisiones a lo retirado se redirigen en `REMAP_U`/`REMAP_A`. **Cómo se genera:** `temas/B2T01.py` escribe las unidades con su numeración de trabajo y `temas/B2T01_indice.py` (`PLAN`)
  las reordena y renumera según este índice y reasigna todas las remisiones («→ III.2.4»), el glosario y la cronología; `OMITIR` retira unidades, `PARCHES` retoca su texto;
  las remisiones sin flecha («en el bloque IV», «en **III.7**») se corrigen a mano en `BARE`. Los ids de apartado (`s7`, `s10b`…) son estables: los destinos de `CM_IR` y `ESQUEMAS` en `oposicion.html` apuntan a
  ellos (II.5 = `s7`, III.4 = `s6`, III.7 = `s10b`, IV.1 = `s13`, IV.2 = `s15`, V.1 = `s16`, V.2 = `s18`). El art. 48 vive en III.7 y los arts. 4 a 8 en III.2 a III.5.
- **Esquemas de procedimiento**: marcador `&>` (`&> Título` y un paso por línea `Actor + Actor | qué hace | regla`; `↳ Actor | …` es una
  alternativa del paso anterior). Un color por institución (Consejo Europeo azul, Consejo verde, Comisión rojo, Parlamento Europeo morado,
  Parlamentos nacionales azul oscuro, Estados gris, Alto Representante rosa, BCE naranja). Son de elaboración propia a partir de los artículos
  y de los esquemas de la guía; en el generador, `flujo(titulo, *pasos)`. Salen también en el PDF.
- **Si la guía o el vídeo discrepan de la norma, prevalece la norma** y va un `?>` con el aviso. Hoy: mayoría cualificada del art. 7
  (art. 354 TFUE → 238.3.b, 72 %), Schengen (el cuadro y la ficha del PE lo sitúan en Ámsterdam; el vídeo, en Maastricht), «originarios»
  (la guía cuenta París, Roma y Maastricht; la ficha 1.1.1 del PE, solo París y Roma), rúbrica de la 1.ª parte del TFUE («Principios», no
  «Disposiciones comunes»), «candidato potencial» (Kosovo) y que los tratados de adhesión «no modifican» los Tratados (art. 49).
  El estado de las candidaturas es **REVISAR** (cambia).
- **Cuadro maestro interactivo** (III.4 · 4.3): marcador `@@cuadro tratados_ue@@` → `cuadroHTML()` (datos en `CUADROS`, `oposicion.html`): réplica de la tabla de la guía con sus rowspans y colores; **cada casilla lleva al apartado o tema del que habla** (`data-go="TEMA:apartado"`, destinos en `CM_IR`) y «⛶ Ampliar» la abre a pantalla completa con zoom, arrastre y Esc. Sustituye a la imagen. Para otro cuadro: añadir su clave a `CUADROS` y usar el marcador.
- **Esquemas de procedimiento interactivos**: los 13 esquemas de la guía están como **SVG vectorial** generado del PDF (`herramientas/oposicion/m108/esquemas_svg.py` → `temas/img/m108/<clave>.svg` + `esquemas.json`, incrustado en `ESQUEMAS` de `oposicion.html`) con el marcador `@@esquema <clave>@@`: réplica exacta (cajas, flechas, colores), **casillas clicables** (cada caja lleva al tema de su institución o al apartado del procedimiento), «⛶ Ampliar» a pantalla completa con zoom y botón en la barra lateral («Esquemas de procedimiento»).  En B2T01 ya no hay versión en pasos `&>` (se quitó para no duplicar; el marcador `&>` sigue disponible para otros temas).
- **Teclado**: ← → ↑ en las flashcards (la sabía / no la sabía / dudé), → en el test (siguiente pregunta ya contestada) y espacio (gira la tarjeta) funcionan sin tener el foco en la tarjeta.
- **Preguntas de la guía** (`QG` en `B2T01.py`; 3, que la guía da como de examen oficial pero sin convocatoria): van al test del tema con
  `ac = "M108 · pregunta n"` (chip 🎓 Academia) y **no** al test real global (no hay convocatoria que citar).

## Revisión de los exámenes oficiales contra los apuntes (6-10-2026)

- Se cotejaron las preguntas de L, P y X de 2025 que caen en los cuatro temas encendidos (I.1-I.3 y II.1) y las no etiquetadas (`tema` vacío) que son de esas normas con lo desarrollado. Faltaba y se añadió: Preámbulo y fórmula de promulgación (I.1 · II.1, X3), art. 30 LO 3/1981 y plazo de un mes (I.2 · V.2 · 2.8, X5), art. 27.2 LOTC y qué puede declararse inconstitucional (I.3 · II.1 · 1.1, X9) y arts. 2 a 6 TFUE, categorías de competencias (II.1 · III.2 · 2.4, L28, P8 y P19). Cada vez que se añada un examen, repetir este cotejo para los temas encendidos.
- Las preguntas L28, P8 y P19 (art. 3 TFUE) siguen **sin `tema`** en `tests-reales`: no se sabe con seguridad si son de II.1 o de otro tema de la UE; hasta que el usuario lo diga, no se etiquetan.

## Pill roja «Examen» (petición del usuario, 6-10-2026)

- `{{EXAMEN}}` → pill con **fondo rojo y letras blancas** «Examen» (`.pill-exa`, app y PDF; misma pill en `#/ce/texto` para los artículos que la academia da como preguntados en examen oficial, `m103.arts[n].exam`).
- Se pone en los **artículos o cuestiones muy preguntados o preguntados con frecuencia**, siempre con su motivo en la línea que acompaña a la pill: (a) la academia lo da como preguntado en examen oficial (M103) o como «muy preguntado / casi todos los años» (valoración de la guía, p. ej. M108); (b) hay pregunta en los exámenes oficiales aportados (L, P, X de 2025, con n.º de pregunta). **No se marca nada sin una de esas dos fuentes** y la frecuencia real solo se conoce con esos datos: cuando el usuario aporte más exámenes, revisar las marcas.
- En los generadores: `T.marcar_examen([(clave, nota), …])` antes de `publicar()` (`plantilla.py`); `clave` = regex sobre el título de una unidad (`### N.M título`) o `sec:<id>` para un apartado entero; si no hay exactamente una unidad, el generador se detiene. Hoy: B1T01, B1T02, B1T03 (`temas/B1T0n.py`) y B2T01 (final de `temas/B2T01.py`).

- **Pulsar la pill (o su frase) abre un diálogo** con la pregunta, las cuatro opciones y la respuesta de la plantilla de cada examen citado (petición del usuario, 7-10-2026). El generador escribe `{{EXAMEN:L24.48,P24.3}}` (código de examen + n.º de pregunta; `formatear` → `.pill-exa[data-ex]`; `abrirExamenRefs` en `oposicion.html`). Las de 2025 (L, P, X) salen de `tests-reales`; las anteriores, de `temas/examenes_previos.json`, que genera `herramientas/oposicion/previos_datos.py DIR_TXT` con **solo las preguntas citadas por el registro** (rehacerlo cada vez que `gace_marcas.py --aplicar` añada marcas, y regenerar los temas). Los apartados de supuestos y la primera parte del 2.º ejercicio van como `SP.<conv>.<I|II|P>.<n>` (`L25`, `LP24`, `X24`, `LP22`, `X22`, `L19`): el diálogo muestra el **enunciado literal de la cuestión** (`supuestos` en `examenes_previos.json`, lo extrae `previos_supuestos.py` de los PDF) y avisa de que no hay plantilla oficial; para un 2.º ejercicio nuevo, añadir su fuente a `FUENTES` de `previos_supuestos.py` y su etiqueta a `CONV` de `Tema._marcas_examen`. Las pills sin referencias (notas manuales de `marcar_examen`) no son pulsables. Prueba: `pruebas/pill_examen.js`.

### Registro permanente de marcas «Examen» en TODOS los temas (petición del usuario, 6-10-2026)

- **Regla:** cada pregunta de los exámenes oficiales (test de L, P y X y los **supuestos prácticos del 2.º ejercicio**, con su **respuesta correcta**) deja una pill «Examen» en el artículo o en la teoría que la resuelve, **en el tema que corresponde aunque esté apagado** (o aún sin apuntes). Se aplica a todos los temas desarrollados (`temas/*.json`).
- **Las marcas NO se borran nunca.** Viven en `herramientas/oposicion/marcas_examen.json` (registro aditivo). Cuando el usuario sube el temario de la academia de un tema y se regenera, las marcas **se reubican solas** donde toque: las de artículo (`k` + `bloque`) por el texto literal del artículo (`lit()` registra dónde se cita en `plantilla.LITS`), las de teoría (`clave`) por el título de la unidad o `sec:<id>`. Si al reorganizar un tema una `clave` deja de existir, **hay que cambiarla** en `marcas_examen_manuales.py` (no quitar la marca). Lo que un tema todavía no desarrolla queda **pendiente** en el registro y se coloca cuando exista (`NIBLO_SIN_SITIO=<fichero>` al generar lista las pendientes).
- **Cómo se alimenta:** `python3 marcas_examen.py [--lits DIR]` (en `herramientas/oposicion`) lee `tests_reales.json` + `boe/leyes25L/P/X.py` y añade marcas por (tema del test, norma, bloque); las preguntas sin `tema` van a su tema por `ASIGNA` (o a `SIN_TEMA` si no hay seguridad: hoy ET arts. 48 y 49 y RD 126/2026, preguntas P24, X47 y P25, a la espera de que el usuario diga el tema); lo que no es un artículo citado (teoría, datos, planes) y los **supuestos** van a mano en `marcas_examen_manuales.py` (`M(...)` y `S(...)`, con la cuestión y el apartado del supuesto). `Tema._marcas_examen` (en `publicar()`) las coloca y fusiona con las marcas manuales de `T.marcar_examen`. **Cada examen nuevo que suba el usuario:** añadirlo a `tests_reales.json`/`leyesYYX.py` y repetir `marcas_examen.py`; para los supuestos, anotar el artículo de cada apartado **solo si el texto de la norma lo confirma** (se comprueba contra `boe/`).
- Las respuestas de los supuestos no tienen plantilla oficial: la marca apunta al artículo que resuelve cada apartado según la norma vigente del repositorio, no a una «clave» de la convocatoria; revisar si el usuario aporta una solución oficial.

#### Exámenes anteriores a 2025 (ampliación del registro, 6-10-2026)

- Fuente: `GACE_examenes_enlaces_2.html` (aportado por el usuario) con los enlaces de sede.inap.gob.es y www.inap.es; se bajan los PDF a una carpeta de trabajo (no al repo) y se leen con `herramientas/oposicion/gace_historico.py` (`pymupdf` → `.txt`; cuestionario + plantilla → `{n, q, o, c}`).
- Cubiertos (test, 1.er ejercicio): **2024** (L, P), **2022** (L, P, E), **2019** (L, P, E, E extraordinario) y, desde www.inap.es (7-10-2026), **2013, 2011 y 2008** (L, P; códigos `L13/P13/L11/P11/L08/P08`). Códigos de convocatoria en las marcas: `L24`, `P24`, `L22`, `P22`, `ST22`, `L19`, `P19`, `ST19`, `STX19` (nombres en `NOM`, `plantilla.py`). Supuestos (2.º ejercicio): **2024**, 2025 y, con la primera parte (5 preguntas) en 2019, **2019 L** y **2022** (L/P y extraordinario L), mapeados a mano apartado a apartado con `SX(...)` en `marcas_examen_manuales.py` (solo artículos que la norma vigente confirma; pendientes de revisar: 2019 P/E y 2022 extraordinario P, cuyo texto difiere).
- **Vigencia de los exámenes antiguos** (7-10-2026, petición del usuario): el GACE-L 2008 se revisó pregunta a pregunta contra la norma vigente (`L08(...)` en `marcas_examen_manuales.py`): solo se marcan las que **siguen teniendo la misma respuesta hoy**; se dejan fuera las de normas derogadas o cambiadas (LOFAGE, Ley 30/1992, Ley 30/2007, plazos de la LPAC, retribuciones, planes y datos de 2008). Hacer lo mismo con 2011, 2013 y los exámenes antiguos que se añadan. `gace_historico.py` quita los pies de página pegados a la última opción (`PIE`); repasar si un examen nuevo trae otro formato.
- **No cubiertos todavía:** 2018, 2010 y 2009 (PDF escaneados, sin capa de texto; haría falta OCR), 2022 extraordinario L y P (solo plantilla, sin cuestionario), los supuestos de 2008 a 2013 (escaneados salvo 2008 P) y 2009 P (sin plantilla). Para 2008-2013 `gace_marcas.py` no ubica por texto las preguntas que citan normas derogadas (LOFAGE, Ley 30/1992, LCSP 30/2007…) ni las de LCSP (la vigente no es la de entonces).
- `gace_marcas.py DIR_TXT DIR_LITS [--aplicar]`: una marca solo si (a) el enunciado cita «artículo N» y una norma que está en `boe/` (se ubica en el tema que cita ese artículo literal), o (b) sin cita, la respuesta correcta está casi entera (≥ 80-90 % de sus palabras clave) en un artículo ya citado en los apuntes, con ventaja clara (se excluyen preámbulos, sentencias, planes y órdenes contables). **Normas derogadas o no incluidas en `boe/` (p. ej. la Ley 30/1992) no se marcan.** Es heurístico: revisar a mano las marcas dudosas. `DIR_LITS` = volcados `NIBLO_LITS=<fichero>` de cada generador.
- Nota técnica: `plantilla.py` recorta `sys.argv`; los scripts que lo importen deben guardar `ARGV = sys.argv[:]` antes.

## Temas encendidos y apagados

- Cada tema está **encendido** (tarjeta en color) o **apagado** (tarjeta en gris, con la etiqueta «⏻ Apagado») en las tarjetas de los bloques; sirve para saber cuáles se han completado (petición del usuario). El usuario lo cambia con el botón de la parte de arriba de **Progreso** (herramienta del lector del tema); se guarda como `TON:<id>` en `prog.mapa` y se sincroniza.
- **Estado por defecto** (lo que pide el usuario que se encienda o apague «en bloque»): `temas/indice.json` → `apagados` (lista de ids) y `apagadosSello` (ISO). Para encender o apagar temas a petición: editar `apagados` **y poner un `apagadosSello` nuevo** (así se descartan los interruptores del usuario anteriores a ese sello y el cambio llega a todos sus dispositivos); no tocar el sello de los temas. Hoy: todos apagados salvo B1T01, B1T02, B1T03 (I.1 a I.3) y B2T01 (II.1) (5-10-2026). `temaEncendido`, `alternarTema`, `tarjetaTema` en `oposicion.html`.

## Marcar apartados como repasados

- En la lista de apartados del lector, cada uno lleva solo un **tic redondo** (gris; verde y relleno al marcarlo; vuelve a gris al pulsar de nuevo), sin el texto «Marcar como repasada», para no ocupar espacio (petición del usuario). Misma función: `data-rep`, clave `id:sec:<apartado>`.

## Flashcards, test, glosario, mapas y cronología (petición del usuario, 5-10-2026)

- **Flashcards** del tema: se abren como **tarjeta centrada** (`.panel.centrado`, no barra lateral); cara trasera oscurecida para el texto blanco; `**negrita**` se pinta (`negE`); al deslizar, la tarjeta se tiñe de **rojo** (izquierda), **verde** (derecha) o **ámbar** (arriba).
- **Test** del tema: pantalla completa con la pregunta **centrada**, enunciado sobre tarjeta de color con texto blanco y opciones en tarjetas blancas.
- **Glosario global** (`hubGlosario(c, ambito, temas, actual)`): en el panel de un tema muestra los términos de **todos** los temas con el filtro «Este tema / Todos los temas»; el botón **＋ Añadir** guarda términos propios en `prog.mapa` (`<tema>:glu:<marca>` con `{t, d}`; se sincronizan, se pueden quitar con 🗑). I.1-I.3 tienen glosario ampliado en `m101/part13.py` (cada definición se comprueba literal contra el artículo).
- **Colores**: `PALETA`/`colorDe()` dan un color distinto por rama de los mapas conceptuales (`~>`, `panelMapa`) y por categoría en cronología y glosario (app y PDF).
- **PDF de apuntes**: usa el **color del bloque** (`BAC`, mismo que `--accent`; `--ac`/`--ac-d`), cuerpo a 10 pt, Glosario y Cronología en **página nueva**, filas de tabla que no se parten (las tablas de más de 6 filas sí pueden partirse entre filas), sin `.cuerpo` vacío y con el título de bloque, «SECCIÓN n» y su primer subtítulo en un mismo bloque (`.enc`) para que no queden títulos huérfanos al final de página.

## Barra lateral del tema

- Diseño actual (petición del usuario, 5-10-2026): título y eyebrow sin subrayado grueso, buscador en píldora con lupa, progreso fino, herramientas en **lista** (icono en cápsula + nombre + ›) en vez de tarjetas, «Práctica activa» como grupo con punto de color, índice con línea guía a la izquierda. Es el mismo HTML (`htmlLateral`) que la hoja «Buscar y herramientas» del móvil; solo cambia el CSS.

## Abrir un tema

- Un tema **desarrollado** (con apuntes) se abre **directamente en el lector** (`#/tema/<id>` redirige a `#/tema/<id>/leer`); la ficha con el programa, las fuentes y la vigencia queda aparte, en el botón «Ficha y fuentes» del lector (`#/tema/<id>/ficha`), para que no meta ruido al entrar (petición del usuario). Un tema sin apuntes sigue abriendo la ficha. «Atrás» en el lector vuelve al bloque. La cabecera del lector (degradado del color del bloque con texto blanco; la barra lateral lleva el mismo color más atenuado) lleva **solo el título oficial del tema** (epígrafe literal de la convocatoria, `epigrafeDe`) y los botones; sin bloque, código, subtítulo ni etiquetas (petición del usuario).

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
  **Sin duplicados** (`apLimpia`): no entran «Repaso por bloques» ni «Preguntas de la guía» (repiten los cuadros y los
  «En resumen»); un apartado «Cuadro…» pierde su «En resumen» (el cuadro ya es el resumen); se quitan los botones de la
  app y «Las etiquetas de los apuntes» del mapa. En la app todo se mantiene.
  La portada **no** lleva altura fija ni hay dos saltos de página seguidos: con otro papel o márgenes del cuadro de impresión
  una altura fija desbordaba y dejaba páginas en blanco. Probar también con `Letter` y márgenes grandes.
  Tipografía para A4: cuerpo 9,2 pt, literales 8,9 pt, tablas 8,4 pt, márgenes 18/15/16 mm (el A4 es el papel por defecto).
  La barra superior lleva «← Volver a la app» (cierra la pestaña si la abrió la app; si no —PWA, ventana bloqueada, archivo
  descargado— navega a `#/tema/<id>`).
  Al tocar el CSS (`APUNTES_CSS`), regenerar los PDF con `pruebas/apuntes.js` y revisar portada y saltos de página.
- Prueba: `herramientas/oposicion/pruebas/apuntes.js` (genera también el PDF con Chromium).

## Estudio avanzado: datos, repaso rápido y «Detecta el cambio» (petición del usuario, 6-10-2026)

- **`#/datos/<pestaña>`** («Datos de estudio», botón en el inicio; `renderDatos` en `oposicion.html`): **plazos y mayorías** (todas las casillas «Plazos y mayorías» de las fichas, con filtro), **frecuencia en examen** (pills `{{EXAMEN:…}}` por apartado, calor), **mis errores** y **vigencia**. Todo se calcula en el cliente de los apuntes ya cargados; no hay datos nuevos.
- **Errores por tipo** (`tipoError`, `registrarError`): al fallar un test de tema, aleatorio, test real o «Detecta el cambio» se compara la redacción correcta con la elegida y se clasifica la diferencia (mayoría > plazo > cifra > órgano > otro). Claves en `prog.mapa`: `ERRT:<tipo>` (`{n}`) y `ERRL` (últimos 40 fallos). Heurístico: revisar `RE_MAY/RE_PLAZO/RE_ORG` si clasifica mal.
- **Herramientas del lector**: ⚡ **Repaso rápido** (`panelRapido`: «Atención examen», «Ojo en el examen», «Plazos y mayorías», pills «Examen» y «En resumen» de cada apartado), 🔍 **Detecta el cambio** (`panelCambio`: frases de los bloques `>` de **BOE y DOUE**, la mitad con un plazo, mayoría u órgano alterado por `mutaciones`; las versiones alteradas se fabrican en el cliente, nunca se guardan ni se presentan como texto legal) y 🕒 **Vigencia y revisión**.
- **Vigencia**: `temas/indice.json` → `verificados` = `{id: "AAAA-MM-DD"}` con la fecha de la **última auditoría** contra la norma. **Actualizarlo cada vez que se audite un tema.** Pasados 90 días (`DIAS_CADUCA`) se pide revisar; los apartados con «REVISAR» o «Dato **cambiante**» se listan como datos que caducan.
- Prueba: `herramientas/oposicion/pruebas/estudio.js`.

## Constitución · pestaña «🧠 Memorizar» (`#/ce/memorizar`; petición del usuario, 6-10-2026)

- **Tres niveles por artículo (1-169), cada uno con su calendario de repaso** (`cemCalificar`, mismo SRS `ceSiguiente` que el Test Constitución; claves `CEM:<art>:<u|t|x>` en `prog.mapa`): 📍 ubicación (título, capítulo, sección), 🏷️ de qué va (etiqueta, en las dos direcciones al azar) y 📜 texto.
- **Texto con huecos progresivos** (`cemClozeHTML`, `cemOcultas`): etapa 0 (≈20 % de las palabras clave ocultas), 1 (≈45 %, incluye las anteriores), 2 (solo iniciales) y 3 (recitado escrito, comparado con el artículo por subsecuencia común de palabras en `cemComparar`: rojo = lo olvidado, sugiere ✗/🤔/✓ con 85 % y 97 %). En automático la etapa sube con los aciertos (`r` del nivel texto); se puede fijar. Las palabras ocultas son heurísticas (≥ 5 letras o números, sin palabras vacías), no las marcas M103.
- **Etiquetas «de qué va»**: arts. 1-52 = guía M101 (p. 10); **arts. 53-169 = etiquetas propias** redactadas del texto literal (`PROPIAS` en `ce_datos.py`, `propio: true`; la app las marca «etiqueta propia»). Revisar si la academia aporta sus propios títulos.
- **Orden aleatorio** (`cfg.barajar`, casilla «🔀 Orden aleatorio» en Practicar, se recuerda en `gestion_hub_ce_mem_v1`): primero se eligen las tarjetas que tocan (y se recorta a 10/15/20/30) y después se mezcla el orden; sin ella salen por artículo. «Al azar» en «Cuáles» ya elige y mezcla.
- **Pantalla completa** al practicar (`cfg.pc`; botón «⛶ Pantalla completa»/«✕ Cerrar» en la tarjeta y casilla en la selección): capa fija `#cem-pc` (`.real-full.cem-pc`, oculta el cronómetro con `body.real-abierto`) más la API de pantalla completa donde exista (no en iPhone); tarjeta que ocupa todo, cuerpo desplazable y botones de respuesta siempre visibles. Se cierra al terminar, al cambiar de pestaña o de ruta (`cemSalirPC`).
- **Tablero** (169 casillas por título, tres barras por casilla: sin empezar / flojo / en curso / dominado ≥ 14 días) y **mini-juegos** (`JUEGOS`: ubica el artículo, rango de una unidad, artículo ↔ tema, ordenar títulos o capítulos). Los juegos no alteran el SRS.
- Prueba: `herramientas/oposicion/pruebas/ce_memorizar.js`.
