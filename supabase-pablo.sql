-- ============================================================================
-- Niblo — tabla para sincronizar los registros de Pablo
--
-- Ejecútalo una sola vez en Supabase → SQL Editor → New query → Run.
--
-- Por qué una sola fila con un JSON y no varias tablas: lo que se registra de
-- Pablo (tomas de leche, sueño, pañales, crecimiento, hitos, dientes, vacunas,
-- notas, visitas al pediatra y el estado de cada alimento) no es relacional y
-- la app ya lo trata como un documento único, el mismo que exporta el botón de
-- copia de seguridad. Y es UNA fila compartida, no una por perfil: son datos
-- del bebé, no de cada padre, así que Rubén y Sergio ven y escriben lo mismo.
-- ============================================================================

create table if not exists public.pablo_estado (
  id          text        primary key,
  datos       jsonb       not null default '{}'::jsonb,
  modificado  timestamptz not null default now()
);

comment on table  public.pablo_estado is 'Registros de Pablo (Niblo): documento único, última escritura gana.';
comment on column public.pablo_estado.id         is 'Siempre "pablo": una sola fila compartida.';
comment on column public.pablo_estado.datos      is 'Estado completo del módulo, el mismo JSON del botón de exportar.';
comment on column public.pablo_estado.modificado is 'Marca de tiempo del último guardado local. Decide quién gana.';

-- ---------------------------------------------------------------------------
-- Seguridad: solo usuarios autenticados. Sin esto, la clave anónima
-- (que va dentro del HTML y es pública) daría acceso a cualquiera.
-- ---------------------------------------------------------------------------
alter table public.pablo_estado enable row level security;

drop policy if exists "pablo_estado_leer"       on public.pablo_estado;
drop policy if exists "pablo_estado_insertar"   on public.pablo_estado;
drop policy if exists "pablo_estado_actualizar" on public.pablo_estado;

create policy "pablo_estado_leer"
  on public.pablo_estado for select
  to authenticated using (true);

create policy "pablo_estado_insertar"
  on public.pablo_estado for insert
  to authenticated with check (true);

create policy "pablo_estado_actualizar"
  on public.pablo_estado for update
  to authenticated using (true) with check (true);

-- Sin política de DELETE a propósito: estos registros no se borran desde la app.

-- ---------------------------------------------------------------------------
-- Comprobación rápida (debe devolver una fila con la tabla y RLS activo)
-- ---------------------------------------------------------------------------
-- select tablename, rowsecurity from pg_tables where tablename = 'pablo_estado';
