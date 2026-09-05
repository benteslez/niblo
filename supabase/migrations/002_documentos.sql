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
