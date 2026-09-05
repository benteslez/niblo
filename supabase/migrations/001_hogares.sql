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
