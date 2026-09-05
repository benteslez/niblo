-- ############################################################################
-- NIBLO — TODO EL SQL, EN ORDEN. Copia y pega esto entero en:
--   Supabase → SQL Editor → New query → Run
--
-- Es idempotente: si lo ejecutas dos veces no rompe nada.
-- Al terminar, mira la pestaña "Messages" por si hay algun NOTICE.
-- ############################################################################


-- ===========================================================================
-- ARCHIVO: 001_hogares.sql
-- ===========================================================================

-- ============================================================================
-- Niblo · 001 — Hogares y aislamiento de datos
--
-- POR QUE: hasta ahora las cuatro tablas tenian politicas "to authenticated
-- using (true)", es decir, CUALQUIER usuario autenticado leia y escribia los
-- datos de todos. Un registro nuevo veria el historial de Pablo y, al apuntar
-- algo, lo sobrescribiria.
--
-- QUE HACE: introduce el hogar como unidad de propiedad. Cada fila pertenece a
-- un hogar y solo la ven sus miembros. Ruben y Sergio quedan en un mismo hogar
-- con todo lo que ya existe; cualquier alta futura crea el suyo, aislado.
--
-- Ejecutar entero de una vez en el SQL Editor. Es idempotente.
-- ============================================================================

-- ---------------------------------------------------------------------------
-- 1. Hogares y miembros
-- ---------------------------------------------------------------------------
create table if not exists public.hogares (
  id         uuid primary key default gen_random_uuid(),
  nombre     text not null,
  -- Que pestañas ve este hogar. El hogar de una familia que solo quiera el
  -- seguimiento del bebe llevara unicamente {pablo}.
  areas      text[] not null default array['pablo']::text[],
  created_at timestamptz not null default now()
);

create table if not exists public.hogar_miembros (
  hogar_id   uuid not null references public.hogares(id) on delete cascade,
  user_id    uuid not null references auth.users(id) on delete cascade,
  rol        text not null default 'miembro',
  created_at timestamptz not null default now(),
  primary key (hogar_id, user_id)
);

create index if not exists hogar_miembros_user on public.hogar_miembros(user_id);

-- Los hogares del usuario actual. SECURITY DEFINER a proposito: si la politica
-- de hogar_miembros consultara hogar_miembros, RLS entraria en recursion.
create or replace function public.mis_hogares()
returns setof uuid
language sql
stable
security definer
set search_path = public
as $$
  select hogar_id from public.hogar_miembros where user_id = auth.uid()
$$;

revoke all on function public.mis_hogares() from public;
grant execute on function public.mis_hogares() to authenticated;

alter table public.hogares        enable row level security;
alter table public.hogar_miembros enable row level security;

drop policy if exists hogares_leer            on public.hogares;
drop policy if exists hogares_actualizar      on public.hogares;
drop policy if exists hogar_miembros_leer     on public.hogar_miembros;

create policy hogares_leer on public.hogares
  for select to authenticated using (id in (select public.mis_hogares()));
create policy hogares_actualizar on public.hogares
  for update to authenticated
  using (id in (select public.mis_hogares()))
  with check (id in (select public.mis_hogares()));

create policy hogar_miembros_leer on public.hogar_miembros
  for select to authenticated using (hogar_id in (select public.mis_hogares()));

-- Nadie crea hogares ni membresias directamente desde el cliente: lo hace la
-- funcion de alta de mas abajo, que controla que solo te añadas a ti mismo.

-- ---------------------------------------------------------------------------
-- 2. El hogar de Ruben y Sergio, con todo lo que ya existe
-- ---------------------------------------------------------------------------
do $$
declare
  h_id  uuid;
  u_id  uuid;
  correos text[] := array['benteslez@gmail.com', 'semartez@gmail.com'];
  c     text;
begin
  select id into h_id from public.hogares where nombre = 'Casa' limit 1;
  if h_id is null then
    insert into public.hogares (nombre, areas)
    values ('Casa', array['pablo','plan','recetas','documentos']::text[])
    returning id into h_id;
  end if;

  foreach c in array correos loop
    select id into u_id from auth.users where lower(email) = c;
    if u_id is null then
      raise notice 'Aviso: no existe ningun usuario con el correo %. Cuando se registre, vuelve a ejecutar este bloque.', c;
    else
      insert into public.hogar_miembros (hogar_id, user_id, rol)
      values (h_id, u_id, 'propietario')
      on conflict (hogar_id, user_id) do nothing;
    end if;
  end loop;
end $$;

-- ---------------------------------------------------------------------------
-- 3. Añadir hogar_id a las tablas existentes y cerrar sus politicas
-- ---------------------------------------------------------------------------
alter table public.pablo_estado   add column if not exists hogar_id uuid references public.hogares(id) on delete cascade;
alter table public.recetas        add column if not exists hogar_id uuid references public.hogares(id) on delete cascade;
alter table public.ingredientes   add column if not exists hogar_id uuid references public.hogares(id) on delete cascade;
alter table public.estado_usuario add column if not exists hogar_id uuid references public.hogares(id) on delete cascade;

-- Todo lo que ya hay es vuestro.
do $$
declare h_id uuid;
begin
  select id into h_id from public.hogares where nombre = 'Casa' limit 1;
  update public.pablo_estado   set hogar_id = h_id where hogar_id is null;
  update public.recetas        set hogar_id = h_id where hogar_id is null;
  update public.ingredientes   set hogar_id = h_id where hogar_id is null;
  update public.estado_usuario set hogar_id = h_id where hogar_id is null;
end $$;

alter table public.pablo_estado   alter column hogar_id set not null;
alter table public.recetas        alter column hogar_id set not null;
alter table public.ingredientes   alter column hogar_id set not null;
alter table public.estado_usuario alter column hogar_id set not null;

-- Claves unicas por hogar: dos hogares pueden tener una receta con el mismo id
-- sin pisarse. Es tambien la clave que usa el upsert del cliente.
create unique index if not exists recetas_hogar_id_uk        on public.recetas(hogar_id, id);
create unique index if not exists ingredientes_hogar_clave_uk on public.ingredientes(hogar_id, clave);
create unique index if not exists estado_usuario_hogar_uk     on public.estado_usuario(hogar_id, perfil, id_receta);
-- pablo_estado tenia id='pablo' como clave primaria, asi que un segundo hogar
-- chocaria contra la fila del primero. La identidad pasa a ser el hogar: un
-- documento por hogar, que es lo que significa de verdad.
do $$
declare pk text;
begin
  select conname into pk from pg_constraint
   where conrelid = 'public.pablo_estado'::regclass and contype = 'p';
  if pk is not null then
    execute format('alter table public.pablo_estado drop constraint %I', pk);
  end if;
end $$;
alter table public.pablo_estado
  add constraint pablo_estado_pkey primary key (hogar_id);

create index if not exists recetas_hogar        on public.recetas(hogar_id);
create index if not exists ingredientes_hogar   on public.ingredientes(hogar_id);
create index if not exists estado_usuario_hogar on public.estado_usuario(hogar_id);

-- Fuera las politicas abiertas y dentro las de pertenencia.
do $$
declare t text; p record;
begin
  foreach t in array array['pablo_estado','recetas','ingredientes','estado_usuario'] loop
    for p in select policyname from pg_policies where schemaname='public' and tablename=t loop
      execute format('drop policy if exists %I on public.%I', p.policyname, t);
    end loop;
    execute format('alter table public.%I enable row level security', t);
    execute format($f$create policy %I on public.%I for select to authenticated
                      using (hogar_id in (select public.mis_hogares()))$f$, t||'_leer', t);
    execute format($f$create policy %I on public.%I for insert to authenticated
                      with check (hogar_id in (select public.mis_hogares()))$f$, t||'_insertar', t);
    execute format($f$create policy %I on public.%I for update to authenticated
                      using (hogar_id in (select public.mis_hogares()))
                      with check (hogar_id in (select public.mis_hogares()))$f$, t||'_actualizar', t);
    execute format($f$create policy %I on public.%I for delete to authenticated
                      using (hogar_id in (select public.mis_hogares()))$f$, t||'_borrar', t);
  end loop;
end $$;

-- ---------------------------------------------------------------------------
-- 4. Alta de un hogar nuevo (la usa la app cuando entra alguien sin hogar)
--
-- SECURITY DEFINER porque tiene que insertar en hogares y hogar_miembros, que
-- el cliente no puede tocar. Solo te añade a ti mismo: el user_id sale de
-- auth.uid(), no de un parametro.
-- ---------------------------------------------------------------------------
create or replace function public.crear_hogar(
  p_nombre text,
  p_bebe_nombre text,
  p_bebe_sexo text,
  p_bebe_nacimiento date
)
returns uuid
language plpgsql
security definer
set search_path = public
as $$
declare h_id uuid;
begin
  if auth.uid() is null then
    raise exception 'Hace falta iniciar sesion';
  end if;
  if exists (select 1 from public.hogar_miembros where user_id = auth.uid()) then
    raise exception 'Ya perteneces a un hogar';
  end if;
  if p_bebe_sexo not in ('nino','nina') then
    raise exception 'El sexo debe ser nino o nina';
  end if;

  insert into public.hogares (nombre, areas)
  values (coalesce(nullif(trim(p_nombre), ''), 'Mi casa'), array['pablo']::text[])
  returning id into h_id;

  insert into public.hogar_miembros (hogar_id, user_id, rol)
  values (h_id, auth.uid(), 'propietario');

  -- Estado inicial del bebe, con lo que ha rellenado en el alta.
  insert into public.pablo_estado (id, hogar_id, datos, modificado)
  values ('pablo', h_id,
          jsonb_build_object('config', jsonb_build_object(
            'nombre', p_bebe_nombre,
            'sexo', p_bebe_sexo,
            'fechaNacimiento', to_char(p_bebe_nacimiento, 'YYYY-MM-DD'))),
          now());

  return h_id;
end $$;

revoke all on function public.crear_hogar(text, text, text, date) from public;
grant execute on function public.crear_hogar(text, text, text, date) to authenticated;

-- ---------------------------------------------------------------------------
-- Comprobacion
-- ---------------------------------------------------------------------------
-- select h.nombre, h.areas, count(m.user_id) as miembros
--   from public.hogares h left join public.hogar_miembros m on m.hogar_id = h.id
--  group by h.id;

-- ===========================================================================
-- ARCHIVO: 002_documentos.sql
-- ===========================================================================

-- ============================================================================
-- Niblo · 002 — Documentos
--
-- Enlaces a documentacion personal (Drive u otro sitio). Ninguna URL vive en
-- el repositorio: solo aqui, y solo se sirven a los miembros del hogar.
--
-- Requiere haber ejecutado antes 001_hogares.sql.
-- ============================================================================

create table if not exists public.document_types (
  id           uuid primary key default gen_random_uuid(),
  hogar_id     uuid not null references public.hogares(id) on delete cascade,
  name         text not null,          -- singular: "Pasaporte"
  plural_label text not null,          -- encabezado: "PASAPORTES"
  emoji        text not null,
  sort_order   integer not null default 100,
  created_at   timestamptz not null default now()
);

-- Un tipo no puede repetirse dentro del mismo hogar, sin importar mayusculas.
create unique index if not exists document_types_hogar_name_uk
  on public.document_types(hogar_id, lower(name));
create index if not exists document_types_hogar_orden
  on public.document_types(hogar_id, sort_order);

create table if not exists public.documents (
  id         uuid primary key default gen_random_uuid(),
  hogar_id   uuid not null references public.hogares(id) on delete cascade,
  -- RESTRICT a proposito: no se borra un tipo que todavia tenga documentos.
  type_id    uuid not null references public.document_types(id) on delete restrict,
  title      text not null,
  url        text not null,
  notes      text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index if not exists documents_hogar_tipo on public.documents(hogar_id, type_id);

-- updated_at al vuelo
create or replace function public.tocar_updated_at()
returns trigger language plpgsql as $$
begin new.updated_at = now(); return new; end $$;

drop trigger if exists documents_updated_at on public.documents;
create trigger documents_updated_at
  before update on public.documents
  for each row execute function public.tocar_updated_at();

-- ---------------------------------------------------------------------------
-- RLS: solo los miembros del hogar, en las cuatro operaciones
-- ---------------------------------------------------------------------------
alter table public.document_types enable row level security;
alter table public.documents      enable row level security;

do $$
declare t text; p record;
begin
  foreach t in array array['document_types','documents'] loop
    for p in select policyname from pg_policies where schemaname='public' and tablename=t loop
      execute format('drop policy if exists %I on public.%I', p.policyname, t);
    end loop;
    execute format($f$create policy %I on public.%I for select to authenticated
                      using (hogar_id in (select public.mis_hogares()))$f$, t||'_leer', t);
    execute format($f$create policy %I on public.%I for insert to authenticated
                      with check (hogar_id in (select public.mis_hogares()))$f$, t||'_insertar', t);
    execute format($f$create policy %I on public.%I for update to authenticated
                      using (hogar_id in (select public.mis_hogares()))
                      with check (hogar_id in (select public.mis_hogares()))$f$, t||'_actualizar', t);
    execute format($f$create policy %I on public.%I for delete to authenticated
                      using (hogar_id in (select public.mis_hogares()))$f$, t||'_borrar', t);
  end loop;
end $$;

-- ---------------------------------------------------------------------------
-- Comprobacion
-- ---------------------------------------------------------------------------
-- select tablename, policyname, cmd from pg_policies
--  where tablename in ('documents','document_types') order by tablename, cmd;

-- ===========================================================================
-- ARCHIVO: 003_perfiles.sql
-- ===========================================================================

-- ============================================================================
-- Niblo · 003 — El perfil de cada miembro sale de la base de datos
--
-- POR QUE: el nombre que se muestra ("Rubén" / "Sergio") y la clave con la que
-- se guardan favoritos y valoraciones salian de una lista de correos escrita
-- en index.html. Los correos ya estan en Supabase Auth: no hacen falta en el
-- repositorio, y ademas cualquier usuario nuevo aparecia como "Invitado" hasta
-- que alguien tocara el codigo.
--
-- Requiere 001_hogares.sql. Idempotente.
-- ============================================================================

alter table public.hogar_miembros add column if not exists perfil text;
alter table public.hogar_miembros add column if not exists nombre text;

-- Dos miembros del mismo hogar no pueden compartir clave de perfil: es la que
-- separa los favoritos de cada uno en estado_usuario.
create unique index if not exists hogar_miembros_perfil_uk
  on public.hogar_miembros(hogar_id, perfil);

-- Los correos se leen aqui, de auth.users, no del repositorio.
do $$
declare
  h_id uuid;
  pares text[][] := array[
    array['benteslez@gmail.com', 'ruben',  'Rubén'],
    array['semartez@gmail.com',  'sergio', 'Sergio']
  ];
  par text[];
  u_id uuid;
begin
  select id into h_id from public.hogares where nombre = 'Casa' limit 1;
  if h_id is null then return; end if;
  foreach par slice 1 in array pares loop
    select id into u_id from auth.users where lower(email) = par[1];
    if u_id is not null then
      update public.hogar_miembros
         set perfil = coalesce(perfil, par[2]),
             nombre = coalesce(nombre, par[3])
       where hogar_id = h_id and user_id = u_id;
    end if;
  end loop;
end $$;

-- Cualquier miembro que se quede sin perfil recibe uno estable a partir de su
-- id, para que nunca haya dos filas con perfil nulo en el mismo hogar.
update public.hogar_miembros
   set perfil = 'u' || replace(left(user_id::text, 8), '-', ''),
       nombre = coalesce(nombre, 'Cuidador')
 where perfil is null;

-- El alta de un hogar nuevo ya deja el perfil puesto.
-- Antes hay que tirar la version de 4 argumentos de 001: si conviven las dos,
-- PostgREST no sabe a cual llamar y devuelve PGRST203.
drop function if exists public.crear_hogar(text, text, text, date);

create or replace function public.crear_hogar(
  p_nombre text,
  p_bebe_nombre text,
  p_bebe_sexo text,
  p_bebe_nacimiento date,
  p_mi_nombre text default null
)
returns uuid
language plpgsql
security definer
set search_path = public
as $$
declare h_id uuid;
begin
  if auth.uid() is null then
    raise exception 'Hace falta iniciar sesion';
  end if;
  if exists (select 1 from public.hogar_miembros where user_id = auth.uid()) then
    raise exception 'Ya perteneces a un hogar';
  end if;
  if p_bebe_sexo not in ('nino','nina') then
    raise exception 'El sexo debe ser nino o nina';
  end if;

  insert into public.hogares (nombre, areas)
  values (coalesce(nullif(trim(p_nombre), ''), 'Mi casa'), array['pablo']::text[])
  returning id into h_id;

  insert into public.hogar_miembros (hogar_id, user_id, rol, perfil, nombre)
  values (h_id, auth.uid(), 'propietario',
          'u' || replace(left(auth.uid()::text, 8), '-', ''),
          coalesce(nullif(trim(p_mi_nombre), ''), 'Cuidador'));

  insert into public.pablo_estado (id, hogar_id, datos, modificado)
  values ('pablo', h_id,
          jsonb_build_object('config', jsonb_build_object(
            'nombre', p_bebe_nombre,
            'sexo', p_bebe_sexo,
            'fechaNacimiento', to_char(p_bebe_nacimiento, 'YYYY-MM-DD'))),
          now());

  return h_id;
end $$;

revoke all on function public.crear_hogar(text, text, text, date, text) from public;
grant execute on function public.crear_hogar(text, text, text, date, text) to authenticated;

-- Cada uno puede cambiar su propio nombre visible.
drop policy if exists hogar_miembros_actualizar on public.hogar_miembros;
create policy hogar_miembros_actualizar on public.hogar_miembros
  for update to authenticated
  using (user_id = auth.uid()) with check (user_id = auth.uid());

-- ---------------------------------------------------------------------------
-- Comprobacion
-- ---------------------------------------------------------------------------
-- select h.nombre as hogar, m.perfil, m.nombre, m.rol
--   from public.hogar_miembros m join public.hogares h on h.id = m.hogar_id;
