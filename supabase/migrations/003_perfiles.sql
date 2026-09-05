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
