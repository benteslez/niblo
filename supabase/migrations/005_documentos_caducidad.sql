-- 005 — Fechas de expedición y caducidad en los documentos.
--
-- Las dos son opcionales: un título académico no caduca y un DNI sí. La app
-- avisa 60 días antes de la fecha de caducidad.
--
-- Ejecutar en el SQL Editor de Supabase. Es idempotente: se puede correr dos
-- veces sin romper nada.

alter table public.documents
  add column if not exists issued_on  date,
  add column if not exists expires_on date;

comment on column public.documents.issued_on  is 'Fecha de expedición. Opcional.';
comment on column public.documents.expires_on is 'Fecha de caducidad. Opcional; la app avisa 60 días antes.';

-- Índice para poder preguntar "qué caduca pronto" sin recorrer la tabla.
create index if not exists documents_expires_on_idx
  on public.documents (hogar_id, expires_on)
  where expires_on is not null;

-- Verificación: deben salir las dos columnas.
select column_name, data_type, is_nullable
  from information_schema.columns
 where table_schema = 'public' and table_name = 'documents'
   and column_name in ('issued_on', 'expires_on')
 order by column_name;
