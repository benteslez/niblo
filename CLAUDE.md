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
