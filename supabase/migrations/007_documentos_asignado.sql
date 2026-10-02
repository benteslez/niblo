-- 007 — A quién pertenece cada documento.
--
-- assignee guarda una clave fija (ruben, sergio, pablo, lima, otros) y no el
-- nombre, para que la app pueda agrupar y ordenar sin depender de tildes o
-- mayúsculas. Si es "otros", assignee_other dice quién (opcional: "Mamá",
-- "Coche"…). Las dos son opcionales: un documento puede no ser de nadie.
--
-- Ejecutar en el SQL Editor de Supabase. Es idempotente: se puede correr dos
-- veces sin romper nada.

alter table public.documents
  add column if not exists assignee       text,
  add column if not exists assignee_other text;

alter table public.documents drop constraint if exists documents_assignee_chk;
alter table public.documents add constraint documents_assignee_chk
  check (assignee is null or assignee in ('ruben', 'sergio', 'pablo', 'lima', 'otros'));

comment on column public.documents.assignee       is 'A quién pertenece: ruben | sergio | pablo | lima | otros. Opcional.';
comment on column public.documents.assignee_other is 'Quién, cuando assignee = otros. Opcional.';

-- Verificación: deben salir las dos columnas.
select column_name, data_type, is_nullable
  from information_schema.columns
 where table_schema = 'public' and table_name = 'documents'
   and column_name in ('assignee', 'assignee_other')
 order by column_name;
