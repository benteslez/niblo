-- ============================================================================
-- Niblo · 009 — Sincronización del hub de la oposición (oposicion.html)
--
-- Dos tablas:
--   oposicion_temas     contenido desarrollado de cada tema. Es del HOGAR, como
--                       los documentos: lo ven y editan sus miembros.
--   oposicion_progreso  flashcards que cada persona marca como sabidas. Es de
--                       cada USUARIO: nadie más lo ve, ni del mismo hogar.
--
-- Conflictos: gana la última modificación (columna "modificado", que pone el
-- dispositivo). El trigger lo hace cumplir en el servidor: si llega tarde una
-- subida más vieja que lo guardado, se ignora en vez de pisarlo.
-- "actualizado" lo pone siempre el servidor y sirve de cursor para bajar solo
-- lo cambiado.
--
-- Requiere 001_hogares.sql. Ejecutar entero en el SQL Editor. Es idempotente.
-- Al final devuelve las dos tablas publicadas en tiempo real: DOS filas.
-- ============================================================================

create table if not exists public.oposicion_temas (
  hogar_id    uuid not null references public.hogares(id) on delete cascade,
  tema_id     text not null check (tema_id ~ '^B[1-6]T[0-9]{2}$'),
  datos       jsonb,                              -- null si está borrado
  borrado     boolean not null default false,     -- marca para propagar el borrado
  modificado  timestamptz not null,
  actualizado timestamptz not null default now(),
  autor       uuid default auth.uid(),
  primary key (hogar_id, tema_id)
);
create index if not exists oposicion_temas_cursor on public.oposicion_temas(hogar_id, actualizado);

create table if not exists public.oposicion_progreso (
  user_id     uuid not null default auth.uid() references auth.users(id) on delete cascade,
  tarjeta     text not null,                      -- "B4T11:<resumen de la pregunta>"
  sabida      boolean not null,
  modificado  timestamptz not null,
  actualizado timestamptz not null default now(),
  primary key (user_id, tarjeta)
);
create index if not exists oposicion_progreso_cursor on public.oposicion_progreso(user_id, actualizado);

-- Última escritura gana, decidido en el servidor.
create or replace function public.oposicion_ultima_gana()
returns trigger language plpgsql as $$
begin
  if tg_op = 'UPDATE' and new.modificado < old.modificado then
    return null;                 -- llega una versión más vieja: no se aplica
  end if;
  new.actualizado = now();
  return new;
end $$;

drop trigger if exists oposicion_temas_lww on public.oposicion_temas;
create trigger oposicion_temas_lww
  before insert or update on public.oposicion_temas
  for each row execute function public.oposicion_ultima_gana();

drop trigger if exists oposicion_progreso_lww on public.oposicion_progreso;
create trigger oposicion_progreso_lww
  before insert or update on public.oposicion_progreso
  for each row execute function public.oposicion_ultima_gana();

-- ---------------------------------------------------------------------------
-- RLS
-- ---------------------------------------------------------------------------
alter table public.oposicion_temas    enable row level security;
alter table public.oposicion_progreso enable row level security;

do $$
declare p record;
begin
  for p in select policyname, tablename from pg_policies
            where schemaname = 'public' and tablename in ('oposicion_temas','oposicion_progreso') loop
    execute format('drop policy if exists %I on public.%I', p.policyname, p.tablename);
  end loop;
end $$;

-- Temas: miembros del hogar.
create policy oposicion_temas_leer on public.oposicion_temas
  for select to authenticated using (hogar_id in (select public.mis_hogares()));
create policy oposicion_temas_insertar on public.oposicion_temas
  for insert to authenticated with check (hogar_id in (select public.mis_hogares()));
create policy oposicion_temas_actualizar on public.oposicion_temas
  for update to authenticated
  using (hogar_id in (select public.mis_hogares()))
  with check (hogar_id in (select public.mis_hogares()));
create policy oposicion_temas_borrar on public.oposicion_temas
  for delete to authenticated using (hogar_id in (select public.mis_hogares()));

-- Progreso: solo el propio usuario.
create policy oposicion_progreso_propio on public.oposicion_progreso
  for all to authenticated
  using (user_id = auth.uid())
  with check (user_id = auth.uid());

grant select, insert, update, delete on public.oposicion_temas    to authenticated;
grant select, insert, update, delete on public.oposicion_progreso to authenticated;

-- ---------------------------------------------------------------------------
-- Tiempo real: los cambios llegan al instante a los demás dispositivos.
-- ---------------------------------------------------------------------------
do $$
declare t text;
begin
  if not exists (select 1 from pg_publication where pubname = 'supabase_realtime') then
    execute 'create publication supabase_realtime';
  end if;
  foreach t in array array['oposicion_temas','oposicion_progreso'] loop
    if not exists (select 1 from pg_publication_tables
                    where pubname = 'supabase_realtime' and schemaname = 'public' and tablename = t) then
      execute format('alter publication supabase_realtime add table public.%I', t);
    end if;
  end loop;
end $$;

-- Comprobación: deben salir DOS filas.
select tablename from pg_publication_tables
 where pubname = 'supabase_realtime' and tablename like 'oposicion_%'
 order by tablename;
