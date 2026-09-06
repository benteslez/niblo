-- ============================================================================
-- Niblo · 004 — Tiempo real
--
-- Sin esto el WebSocket conecta pero no llega ningun cambio: Supabase solo
-- emite eventos de las tablas que estan en la publicacion supabase_realtime.
--
-- REPLICA IDENTITY FULL hace que el evento incluya tambien la fila antigua,
-- necesario para que el filtro por hogar_id funcione en los DELETE.
-- ============================================================================

do $$
declare t text;
begin
  foreach t in array array['pablo_estado','documents','document_types',
                           'recetas','ingredientes','estado_usuario'] loop
    -- Idempotente: si ya esta en la publicacion, no falla.
    if not exists (
      select 1 from pg_publication_tables
       where pubname = 'supabase_realtime' and schemaname = 'public' and tablename = t
    ) then
      execute format('alter publication supabase_realtime add table public.%I', t);
    end if;
    execute format('alter table public.%I replica identity full', t);
  end loop;
end $$;

-- ---------------------------------------------------------------------------
-- Comprobacion: deben salir las seis tablas
-- ---------------------------------------------------------------------------
select tablename from pg_publication_tables
 where pubname = 'supabase_realtime' and schemaname = 'public'
 order by tablename;
