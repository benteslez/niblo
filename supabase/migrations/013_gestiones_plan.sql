-- 013 — Gestiones: objetivo y condiciones de cada préstamo + las hipotecas de
--       Sants (UCI) y Rafael Alberti (BBVA) del Excel «Plan de amortización».
--
-- 1) Añade a gs_prestamos: banco, objetivo (fecha y, opcionalmente, un total a
--    amortizar), inicio del plan, mínimo por amortización, máximo anual sin
--    comisión y condiciones.
-- 2) Crea las dos hipotecas dentro de su piso, buscando el piso por nombre
--    (Sants/Badalona y Alberti/Rafael). Si no encuentra el piso, avisa y no
--    inserta nada: se puede crear a mano desde la app.
--
-- Ejecutar en el SQL Editor de Supabase. Es idempotente: si la hipoteca ya
-- existe en ese piso (mismo nombre), no la duplica.

alter table public.gs_prestamos
  add column if not exists entidad       text,
  add column if not exists obj_fecha     date,
  add column if not exists obj_importe   numeric(14,2),
  add column if not exists plan_inicio   date,
  add column if not exists min_amort     numeric(12,2),
  add column if not exists max_anual_pct numeric(5,2),
  add column if not exists condiciones   text;

do $$
declare piso record;
begin
  -- ---------------------------------------------------------------- Sants
  select id, hogar_id, nombre into piso
    from public.gs_propiedades
   where nombre ilike '%sants%' or nombre ilike '%badalona%'
   order by created_at limit 1;
  if not found then
    raise notice 'No encuentro el piso de Sants/Badalona: crea la hipoteca a mano desde la app.';
  elsif exists (select 1 from public.gs_prestamos where propiedad_id = piso.id and nombre = 'Hipoteca UCI (Sants)') then
    raise notice 'Sants: la hipoteca ya estaba en «%».', piso.nombre;
  else
    insert into public.gs_prestamos
      (hogar_id, propiedad_id, nombre, entidad, capital, interes, meses, inicio, cuota,
       obj_fecha, plan_inicio, min_amort, condiciones)
    values
      (piso.hogar_id, piso.id, 'Hipoteca UCI (Sants)', 'UCI', 123588.59, 2.39, 211, date '2026-10-01', 719.36,
       date '2029-09-01', date '2026-10-01', 1500,
       'Comisión por amortización anticipada: 0 % en todos los casos (tipo fijo, tipo variable, y por encima o por debajo del 25 % anual), según la escritura. Saldo pendiente a 15/09/2026. Objetivo: liquidarla en septiembre de 2029.');
    raise notice 'Sants: hipoteca creada en «%».', piso.nombre;
  end if;

  -- ---------------------------------------------------------- Rafael Alberti
  select id, hogar_id, nombre into piso
    from public.gs_propiedades
   where nombre ilike '%alberti%' or nombre ilike '%rafael%'
   order by created_at limit 1;
  if not found then
    raise notice 'No encuentro el piso de Rafael Alberti: crea la hipoteca a mano desde la app.';
  elsif exists (select 1 from public.gs_prestamos where propiedad_id = piso.id and nombre = 'Hipoteca BBVA (Rafael Alberti)') then
    raise notice 'Rafael Alberti: la hipoteca ya estaba en «%».', piso.nombre;
  else
    insert into public.gs_prestamos
      (hogar_id, propiedad_id, nombre, entidad, capital, interes, meses, inicio, cuota,
       obj_fecha, obj_importe, plan_inicio, max_anual_pct, condiciones)
    values
      (piso.hogar_id, piso.id, 'Hipoteca BBVA (Rafael Alberti)', 'BBVA', 270000, 2.3, 336, date '2026-10-30', null,
       date '2029-09-01', 77701.68, date '2026-10-01', 25,
       'Máximo sin comisión por año: 25 % (ver escritura). Capital inicial 270.000 € a 28 años. Objetivo: amortizar 77.701,68 € en 36 meses (septiembre de 2029).');
    raise notice 'Rafael Alberti: hipoteca creada en «%».', piso.nombre;
  end if;
end $$;

-- Verificación: debe salir cada hipoteca con su piso.
select pr.nombre as prestamo, p.nombre as piso, pr.capital, pr.interes, pr.meses, pr.obj_fecha, pr.obj_importe
  from public.gs_prestamos pr
  left join public.gs_propiedades p on p.id = pr.propiedad_id
 order by pr.created_at;
