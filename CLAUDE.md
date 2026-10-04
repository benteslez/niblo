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
  acceso:"libre"|"promocion"|"extraordinaria", convocatoria, ejercicio, fecha,
  plantilla:"provisional"|"definitiva", fuente, corte?, minutos?, penalizacion?,
  preguntas:[{ n, q, o:[…], c, tema?, reserva?, anulada?, e? }] }]}`.
  `c` es el índice (0 = a) de la respuesta de la plantilla; `tema` es el
  código del programa (`"I.2"`) si se puede asignar con seguridad; `corte`,
  la puntuación directa mínima publicada para ese examen (solo si hay fuente);
  `minutos` y `penalizacion`, solo para accesos sin condiciones vigentes
  (extraordinaria), copiados de su convocatoria.
- Antes de publicar: enunciado y opciones copiados literales del cuestionario,
  respuesta de la plantilla comprobada contra la ley (como en los apuntes) y
  avisar al usuario de cualquier respuesta que no case.
- Modo **Repaso (SRS)**: el mismo SM-2 del SRS de vocabulario (fallada → mañana;
  dudada → 3 días; sabida → 7 días; luego intervalo × facilidad; facilidad
  1,3–2,8). No cambiar los parámetros sin que lo pida el usuario.
- Modo **Examen oficial**: condiciones vigentes del primer ejercicio
  (BOE-A-2025-26262): turno libre, 100 preguntas, 90 minutos y −1/3 (anexo VII,
  2.1.1); promoción interna, 100, 90 y −1/4 (anexo VIII, 3.1.1). Los blancos no
  penalizan. La calificación oficial (0-50) depende del mínimo que fije la
  Comisión: no se inventa una conversión.
