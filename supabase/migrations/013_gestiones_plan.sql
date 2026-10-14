-- 013 — Gestiones: objetivo y condiciones de cada préstamo.
--
-- Añade a gs_prestamos: banco, objetivo (fecha y, opcionalmente, un total a
-- amortizar), inicio del plan, mínimo por amortización, máximo anual sin
-- comisión y condiciones.
--
-- Los datos de cada préstamo NO van en el repositorio (es público): se crean
-- desde la app (pestaña Préstamo de cada piso) o con un SQL que se pasa por el
-- chat y no se guarda aquí.
--
-- Ejecutar en el SQL Editor de Supabase. Es idempotente.

alter table public.gs_prestamos
  add column if not exists entidad       text,
  add column if not exists obj_fecha     date,
  add column if not exists obj_importe   numeric(14,2),
  add column if not exists plan_inicio   date,
  add column if not exists min_amort     numeric(12,2),
  add column if not exists max_anual_pct numeric(5,2),
  add column if not exists condiciones   text;

-- Verificación: deben salir las siete columnas.
select column_name
  from information_schema.columns
 where table_schema = 'public' and table_name = 'gs_prestamos'
   and column_name in ('entidad', 'obj_fecha', 'obj_importe', 'plan_inicio', 'min_amort', 'max_anual_pct', 'condiciones')
 order by column_name;
