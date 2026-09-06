-- ============================================================================
-- Niblo · 004 — Tiempo real (version robusta)
--
-- La primera version daba por hecho que la publicacion "supabase_realtime" ya
-- existia. Si no existe, "alter publication ... add table" falla y no se añade
-- nada. Esta la crea si hace falta y avisa de lo que va haciendo.
--
-- Ejecutar entera. Al final devuelve las tablas que han quedado publicadas:
-- tienen que salir SEIS filas.
-- ============================================================================

do $$
declare
  t text;
  hay_pub boolean;
begin
  select exists (select 1 from pg_publication where pubname = 'supabase_realtime')
    into hay_pub;

  if not hay_pub then
    raise notice 'La publicacion supabase_realtime no existia: se crea.';
    execute 'create publication supabase_realtime';
  else
    raise notice 'La publicacion supabase_realtime ya existia.';
  end if;

  foreach t in array array['pablo_estado','documents','document_types',
                           'recetas','ingredientes','estado_usuario'] loop
    if not exists (select 1 from pg_tables where schemaname='public' and tablename=t) then
      raise notice 'SALTADA: la tabla public.% no existe', t;
      continue;
    end if;

    if exists (
      select 1 from pg_publication_tables
       where pubname='supabase_realtime' and schemaname='public' and tablename=t
    ) then
      raise notice 'Ya estaba publicada: %', t;
    else
      execute format('alter publication supabase_realtime add table public.%I', t);
      raise notice 'Añadida: %', t;
    end if;

    -- Necesario para que el filtro por hogar_id funcione tambien en los DELETE.
    execute format('alter table public.%I replica identity full', t);
  end loop;
end $$;

-- ---------------------------------------------------------------------------
-- RESULTADO: tienen que salir seis filas
-- ---------------------------------------------------------------------------
select tablename as tabla_publicada
  from pg_publication_tables
 where pubname = 'supabase_realtime' and schemaname = 'public'
 order by tablename;
