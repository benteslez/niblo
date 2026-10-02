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
