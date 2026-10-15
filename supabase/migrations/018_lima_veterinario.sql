-- 018 — Lima: veterinario (visitas) y síntomas, como Pediatra en la parte de Pablo.
--
--   gs_lima_visitas    visitas al veterinario: fecha y hora (con fecha futura es una
--                      cita programada), motivo, veterinario, clínica, dirección,
--                      teléfono, cómo quedó, enlace a resultados, peso y notas
--   gs_lima_sintomas   síntomas: fecha y hora, temperatura, lista de síntomas y notas
--
-- Ejecutar ENTERO en el SQL Editor de Supabase. Idempotente. Requiere la 011
-- (mis_hogares) y la 002 (tocar_updated_at).

create table if not exists public.gs_lima_visitas (
  id          uuid primary key default gen_random_uuid(),
  hogar_id    uuid not null references public.hogares(id) on delete cascade,
  fecha       date not null,
  hora        text,
  motivo      text not null default 'revision',
  detalle     text,
  veterinario text,
  clinica     text,
  direccion   text,
  telefono    text,
  resultado   text check (resultado in ('bien', 'revision', 'tratamiento')),
  enlace      text,
  peso        numeric(5,2),
  notas       text,
  created_at  timestamptz not null default now(),
  updated_at  timestamptz not null default now()
);

create table if not exists public.gs_lima_sintomas (
  id         uuid primary key default gen_random_uuid(),
  hogar_id   uuid not null references public.hogares(id) on delete cascade,
  fecha      date not null,
  hora       text,
  temp       numeric(3,1),
  lista      text[] not null default '{}',
  notas      text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index if not exists gs_lima_visitas_fecha  on public.gs_lima_visitas(hogar_id, fecha);
create index if not exists gs_lima_sintomas_fecha on public.gs_lima_sintomas(hogar_id, fecha);

drop trigger if exists gs_lima_visitas_updated_at on public.gs_lima_visitas;
create trigger gs_lima_visitas_updated_at before update on public.gs_lima_visitas
  for each row execute function public.tocar_updated_at();
drop trigger if exists gs_lima_sintomas_updated_at on public.gs_lima_sintomas;
create trigger gs_lima_sintomas_updated_at before update on public.gs_lima_sintomas
  for each row execute function public.tocar_updated_at();

-- RLS: solo los miembros del hogar, en las cuatro operaciones
do $$
declare t text; p record;
begin
  foreach t in array array['gs_lima_visitas', 'gs_lima_sintomas'] loop
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

-- Tiempo real (para que Sergio lo vea al instante)
do $$
declare t text;
begin
  if not exists (select 1 from pg_publication where pubname = 'supabase_realtime') then
    execute 'create publication supabase_realtime';
  end if;
  foreach t in array array['gs_lima_visitas', 'gs_lima_sintomas'] loop
    if not exists (select 1 from pg_publication_tables
                    where pubname = 'supabase_realtime' and schemaname = 'public' and tablename = t) then
      execute format('alter publication supabase_realtime add table public.%I', t);
    end if;
    execute format('alter table public.%I replica identity full', t);
  end loop;
end $$;

-- Verificación: las dos tablas.
select tablename as tabla from pg_tables
 where schemaname = 'public' and tablename in ('gs_lima_visitas', 'gs_lima_sintomas')
 order by tablename;
