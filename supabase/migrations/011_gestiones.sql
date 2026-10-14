-- 011 — Gestiones: pisos, inquilinos, gastos/ingresos, gestiones (Lima, familia)
--       y préstamos con tabla de amortización.
--
-- Qué crea (todo con hogar_id y RLS: solo los miembros del hogar lo ven y lo
-- editan, igual que Documentos):
--   gs_propiedades          pisos: los que alquilamos y aquel donde somos inquilinos
--   gs_inquilinos           inquilinos de cada piso (contrato, renta, fianza)
--   gs_gestiones            gastos, ingresos y gestiones de cualquier ámbito
--                           (piso | lima | familia), con fecha, importe y estado
--   gs_prestamos            préstamos / hipotecas (capital, interés, plazo, inicio)
--   gs_prestamo_revisiones  cambios de tipo de interés (Euríbor, etc.)
--   gs_pagos_prestamo       dinero extra que se mete a amortizar
--
-- También publica las tablas en Realtime (para que Sergio vea los cambios al
-- instante) y añade el área «gestiones» al hogar de casa.
--
-- Ejecutar ENTERO en el SQL Editor de Supabase. Es idempotente: se puede
-- correr dos veces sin romper nada. Requiere 001 y 002 (mis_hogares y
-- tocar_updated_at).

-- ---------------------------------------------------------------------------
-- Tablas
-- ---------------------------------------------------------------------------
create table if not exists public.gs_propiedades (
  id         uuid primary key default gen_random_uuid(),
  hogar_id   uuid not null references public.hogares(id) on delete cascade,
  nombre     text not null,
  rol        text not null default 'propietario'
             check (rol in ('propietario', 'inquilino')),
  direccion  text,
  notas      text,
  sort_order integer not null default 100,
  created_at timestamptz not null default now()
);

create table if not exists public.gs_inquilinos (
  id           uuid primary key default gen_random_uuid(),
  hogar_id     uuid not null references public.hogares(id) on delete cascade,
  propiedad_id uuid not null references public.gs_propiedades(id) on delete cascade,
  nombre       text not null,
  telefono     text,
  email        text,
  inicio       date,           -- inicio del contrato
  fin          date,           -- fin del contrato
  renta        numeric(12,2),  -- renta mensual
  fianza       numeric(12,2),
  activo       boolean not null default true,
  notas        text,
  created_at   timestamptz not null default now()
);

create table if not exists public.gs_gestiones (
  id           uuid primary key default gen_random_uuid(),
  hogar_id     uuid not null references public.hogares(id) on delete cascade,
  ambito       text not null check (ambito in ('piso', 'lima', 'familia')),
  propiedad_id uuid references public.gs_propiedades(id) on delete cascade,
  inquilino_id uuid references public.gs_inquilinos(id) on delete set null,
  tipo         text not null check (tipo in ('gasto', 'ingreso', 'gestion')),
  categoria    text,
  titulo       text not null,
  fecha        date not null,           -- fecha del hecho o vencimiento
  importe      numeric(12,2),           -- opcional (siempre positivo)
  estado       text not null default 'pendiente'
               check (estado in ('pendiente', 'hecho')),
  repite       text check (repite in ('mensual', 'trimestral', 'semestral', 'anual')),
  asignado     text,
  url          text,
  notas        text,
  created_at   timestamptz not null default now(),
  updated_at   timestamptz not null default now()
);

create table if not exists public.gs_prestamos (
  id           uuid primary key default gen_random_uuid(),
  hogar_id     uuid not null references public.hogares(id) on delete cascade,
  propiedad_id uuid references public.gs_propiedades(id) on delete set null,
  nombre       text not null,
  capital      numeric(14,2) not null,
  interes      numeric(7,4) not null,   -- % nominal anual
  meses        integer not null check (meses > 0),
  inicio       date not null,           -- fecha de la primera cuota
  cuota        numeric(12,2),           -- si el banco da la cuota exacta; si no, se calcula
  notas        text,
  created_at   timestamptz not null default now()
);

create table if not exists public.gs_prestamo_revisiones (
  id          uuid primary key default gen_random_uuid(),
  hogar_id    uuid not null references public.hogares(id) on delete cascade,
  prestamo_id uuid not null references public.gs_prestamos(id) on delete cascade,
  desde       date not null,
  interes     numeric(7,4) not null,
  created_at  timestamptz not null default now()
);

create table if not exists public.gs_pagos_prestamo (
  id          uuid primary key default gen_random_uuid(),
  hogar_id    uuid not null references public.hogares(id) on delete cascade,
  prestamo_id uuid not null references public.gs_prestamos(id) on delete cascade,
  fecha       date not null,
  importe     numeric(14,2) not null check (importe > 0),
  modo        text not null default 'plazo' check (modo in ('plazo', 'cuota')),
  notas       text,
  created_at  timestamptz not null default now()
);

create index if not exists gs_propiedades_hogar    on public.gs_propiedades(hogar_id);
create index if not exists gs_inquilinos_prop      on public.gs_inquilinos(propiedad_id);
create index if not exists gs_gestiones_hogar_fecha on public.gs_gestiones(hogar_id, fecha);
create index if not exists gs_gestiones_prop       on public.gs_gestiones(propiedad_id);
create index if not exists gs_prestamos_hogar      on public.gs_prestamos(hogar_id);
create index if not exists gs_revisiones_prestamo  on public.gs_prestamo_revisiones(prestamo_id);
create index if not exists gs_pagos_prestamo_idx   on public.gs_pagos_prestamo(prestamo_id, fecha);

drop trigger if exists gs_gestiones_updated_at on public.gs_gestiones;
create trigger gs_gestiones_updated_at
  before update on public.gs_gestiones
  for each row execute function public.tocar_updated_at();

-- ---------------------------------------------------------------------------
-- RLS: solo los miembros del hogar, en las cuatro operaciones
-- ---------------------------------------------------------------------------
do $$
declare t text; p record;
begin
  foreach t in array array['gs_propiedades', 'gs_inquilinos', 'gs_gestiones',
                           'gs_prestamos', 'gs_prestamo_revisiones', 'gs_pagos_prestamo'] loop
    execute format('alter table public.%I enable row level security', t);
    for p in select policyname from pg_policies where schemaname = 'public' and tablename = t loop
      execute format('drop policy if exists %I on public.%I', p.policyname, t);
    end loop;
    execute format($f$create policy %I on public.%I for select to authenticated
                      using (hogar_id in (select public.mis_hogares()))$f$, t || '_leer', t);
    execute format($f$create policy %I on public.%I for insert to authenticated
                      with check (hogar_id in (select public.mis_hogares()))$f$, t || '_insertar', t);
    execute format($f$create policy %I on public.%I for update to authenticated
                      using (hogar_id in (select public.mis_hogares()))
                      with check (hogar_id in (select public.mis_hogares()))$f$, t || '_actualizar', t);
    execute format($f$create policy %I on public.%I for delete to authenticated
                      using (hogar_id in (select public.mis_hogares()))$f$, t || '_borrar', t);
  end loop;
end $$;

-- ---------------------------------------------------------------------------
-- Tiempo real (como la 004): publicar las tablas para que el otro móvil se entere
-- ---------------------------------------------------------------------------
do $$
declare t text;
begin
  if not exists (select 1 from pg_publication where pubname = 'supabase_realtime') then
    execute 'create publication supabase_realtime';
  end if;
  foreach t in array array['gs_propiedades', 'gs_inquilinos', 'gs_gestiones',
                           'gs_prestamos', 'gs_prestamo_revisiones', 'gs_pagos_prestamo'] loop
    if not exists (select 1 from pg_publication_tables
                    where pubname = 'supabase_realtime' and schemaname = 'public' and tablename = t) then
      execute format('alter publication supabase_realtime add table public.%I', t);
    end if;
    execute format('alter table public.%I replica identity full', t);
  end loop;
end $$;

-- ---------------------------------------------------------------------------
-- Área «gestiones» en el hogar de casa (sustituye a la tarjeta de Documentos,
-- que pasa a ser una pestaña de Gestiones)
-- ---------------------------------------------------------------------------
update public.hogares
   set areas = (
     select array_agg(distinct a order by a)
       from unnest(areas || array['gestiones']) as a
   )
 where nombre = 'Casa';   -- si tu hogar se llama de otra forma, cámbialo aquí

-- Verificación: seis tablas gs_* y el área «gestiones» en el hogar.
select tablename as tabla
  from pg_tables
 where schemaname = 'public' and tablename like 'gs\_%'
 order by tablename;

select nombre, areas from public.hogares;
