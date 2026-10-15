-- 015 — Gestiones: gastos e ingresos en pesos colombianos (COP) con el cambio
--       del día del pago.
--
-- «importe» sigue siendo SIEMPRE el importe en euros (así los totales, el
-- balance y los préstamos no cambian). Si el movimiento se hizo en COP:
--   moneda       'EUR' (por defecto) o 'COP'
--   importe_cop  lo pagado en pesos
--   tasa_cop     pesos por 1 € el día del pago
--   tasa_prov    true = cambio provisional (aún no se ha pagado o el día no ha llegado)
--   tasa_manual  true = el cambio lo escribiste tú (por ejemplo el de tu banco)
--
-- Ejecutar ENTERO en el SQL Editor de Supabase. Idempotente.
alter table public.gs_gestiones
  add column if not exists moneda      text not null default 'EUR',
  add column if not exists importe_cop numeric(16,2),
  add column if not exists tasa_cop    numeric(14,4),
  add column if not exists tasa_prov   boolean not null default false,
  add column if not exists tasa_manual boolean not null default false;

do $$
begin
  if not exists (select 1 from pg_constraint where conname = 'gs_gestiones_moneda_chk') then
    alter table public.gs_gestiones
      add constraint gs_gestiones_moneda_chk check (moneda in ('EUR', 'COP'));
  end if;
end $$;

-- Verificación: las cinco columnas nuevas.
select column_name from information_schema.columns
 where table_schema = 'public' and table_name = 'gs_gestiones'
   and column_name in ('moneda', 'importe_cop', 'tasa_cop', 'tasa_prov', 'tasa_manual');
