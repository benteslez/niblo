-- 017 — Gestiones: NIF de los inquilinos.
-- Ejecutar ENTERO en el SQL Editor de Supabase. Idempotente. Requiere la 011.
alter table public.gs_inquilinos add column if not exists nif text;

-- Verificación
select column_name from information_schema.columns
 where table_schema = 'public' and table_name = 'gs_inquilinos' and column_name = 'nif';
