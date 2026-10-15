-- 016 — Gestiones: suministros de un piso (agua, luz, gas, internet…).
--
-- Qué añade:
--   gs_propiedades.suministros_activos   «Activar suministros» (vivimos ahí)
--   gs_suministros                       accesos directos del piso: nombre,
--                                        empresa, web, nº de contrato y días de aviso
--   gs_gestiones.suministro_id           el pago registrado o programado de un
--                                        suministro (es un gasto del piso, así
--                                        que sale en el historial y en el balance)
--
-- Ejecutar ENTERO en el SQL Editor de Supabase. Idempotente. Requiere la 011.

alter table public.gs_propiedades
  add column if not exists suministros_activos boolean not null default false;

create table if not exists public.gs_suministros (
  id           uuid primary key default gen_random_uuid(),
  hogar_id     uuid not null references public.hogares(id) on delete cascade,
  propiedad_id uuid not null references public.gs_propiedades(id) on delete cascade,
  nombre       text not null,            -- Agua, Luz, Gas, Internet…
  empresa      text,
  url          text,
  contrato     text,                     -- número de contrato
  aviso_dias   integer not null default 3 check (aviso_dias >= 0),
  icono        text,                     -- vacío = según el nombre
  notas        text,
  sort_order   integer not null default 100,
  created_at   timestamptz not null default now()
);
create index if not exists gs_suministros_prop on public.gs_suministros(propiedad_id);

alter table public.gs_gestiones
  add column if not exists suministro_id uuid references public.gs_suministros(id) on delete set null;
create index if not exists gs_gestiones_sumin on public.gs_gestiones(suministro_id);

-- RLS: solo los miembros del hogar (igual que el resto de tablas gs_*)
alter table public.gs_suministros enable row level security;
drop policy if exists gs_suministros_leer       on public.gs_suministros;
drop policy if exists gs_suministros_insertar   on public.gs_suministros;
drop policy if exists gs_suministros_actualizar on public.gs_suministros;
drop policy if exists gs_suministros_borrar     on public.gs_suministros;
create policy gs_suministros_leer on public.gs_suministros for select to authenticated
  using (hogar_id in (select public.mis_hogares()));
create policy gs_suministros_insertar on public.gs_suministros for insert to authenticated
  with check (hogar_id in (select public.mis_hogares()));
create policy gs_suministros_actualizar on public.gs_suministros for update to authenticated
  using (hogar_id in (select public.mis_hogares()))
  with check (hogar_id in (select public.mis_hogares()));
create policy gs_suministros_borrar on public.gs_suministros for delete to authenticated
  using (hogar_id in (select public.mis_hogares()));

-- Tiempo real (para que Sergio lo vea al instante)
do $$
begin
  if not exists (select 1 from pg_publication where pubname = 'supabase_realtime') then
    execute 'create publication supabase_realtime';
  end if;
  if not exists (select 1 from pg_publication_tables
                  where pubname = 'supabase_realtime' and schemaname = 'public' and tablename = 'gs_suministros') then
    execute 'alter publication supabase_realtime add table public.gs_suministros';
  end if;
  execute 'alter table public.gs_suministros replica identity full';
end $$;

-- Verificación: la tabla y las columnas nuevas.
select table_name, column_name from information_schema.columns
 where table_schema = 'public'
   and ((table_name = 'gs_suministros')
     or (table_name = 'gs_propiedades' and column_name = 'suministros_activos')
     or (table_name = 'gs_gestiones' and column_name = 'suministro_id'))
 order by table_name, ordinal_position;
