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
  `ce_datos.py` desde `herramientas/oposicion/m103_datos.py`; cada frase marcada tiene que ser literal del artículo): pills 🟧 examen oficial,
  🟨 importante, 🟩 coletilla, 🟦 se limita en excepción y sitio (completado con el art. 55.1), 🌸 ley orgánica, subrayado en el texto y comentario
  de la academia por artículo. Se ve en `#/ce/texto` (interruptor) y en el reverso del Test Constitución; el tema I.1 (III.1, 1.1 y 1.2) solo
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
- **Preguntas del test real global en cada tema** (`realesDeTema`): las de `tests-reales` cuyo `tema` es el del tema (I.1, I.2, I.3;
  no anuladas ni retenidas) entran en «📋 De examen real» y en «Todas», con su texto legal y su discrepancia. Su progreso es **propio
  del tema** (`B1T0n:q:<hash>`), independiente del test real global (`R:<examen>:<n>`): lo que se conteste en un sitio no cambia el
  otro. Corregido: L1 (nombre del Título I) y P51 (art. 9.3) pasan a I.1.
- Prueba: `herramientas/oposicion/pruebas/test_academia.js`.

## Estética de los apuntes (lector y PDF)

- Petición del usuario: apuntes limpios y visuales, con conceptos en escala de colores. Recuadros con etiqueta (`CJ_CSS` en `oposicion.html`, común al lector y al PDF): `+>` **Concepto clave** (azul), `!>` **Atención examen** (rojo), `@> **▸ En resumen.**` **Síntesis** (amarillo), `?>` **Ojo** (ámbar), `@> **▸ Dónde estamos.**` guía (gris). `~>` = **mapa conceptual** (`~> Título`, `~> # Raíz`, una rama por línea `Rama | descripción | subcaja`); I.1-I.3 lo generan solo de la tabla «El hilo del tema» (`_con_mapa` en `m101/dividir.py`).
- Los términos del glosario salen solos como «Concepto clave» al empezar su apartado (`conConceptos`, máx. 2 por apartado). Tablas con cabecera azul y filas alternas; subtítulos de artículo (`###`) con la misma tipografía que los subapartados (petición del usuario).
- Los códigos de fuente pueden llevar dígitos (`[[M101]]`).

## Abrir un tema

- Un tema **desarrollado** (con apuntes) se abre **directamente en el lector** (`#/tema/<id>` redirige a `#/tema/<id>/leer`); la ficha con el programa, las fuentes y la vigencia queda aparte, en el botón «Ficha y fuentes» del lector (`#/tema/<id>/ficha`), para que no meta ruido al entrar (petición del usuario). Un tema sin apuntes sigue abriendo la ficha. «Atrás» en el lector vuelve al bloque.

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
