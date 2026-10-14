-- 012 — Gestiones: enlazar cada pago recurrente con el siguiente que genera.
--
-- Antes, al marcar como hecho un pago que se repite, se creaba el siguiente
-- salvo que ya hubiera otro con el mismo nombre, categoría y fecha. Eso
-- descartaba el segundo cuando hay dos pagos iguales cada mes (p. ej. dos de
-- «Comunidad»). Ahora cada siguiente apunta a la fila de la que sale
-- (origen_id), y solo se evita crear dos siguientes de la MISMA fila.
--
-- Ejecutar en el SQL Editor de Supabase. Es idempotente.

alter table public.gs_gestiones
  add column if not exists origen_id uuid references public.gs_gestiones(id) on delete set null;

create index if not exists gs_gestiones_origen on public.gs_gestiones(origen_id);

-- Verificación: debe salir la columna origen_id.
select column_name, data_type
  from information_schema.columns
 where table_schema = 'public' and table_name = 'gs_gestiones' and column_name = 'origen_id';
