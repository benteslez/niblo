-- 014 — Menos tráfico (egress) del tiempo real con los datos de Pablo.
--
-- La migración 004 puso `replica identity full` en todas las tablas para que el
-- filtro por hogar funcione también en los DELETE. En pablo_estado eso hace que
-- cada cambio mande por tiempo real el documento NUEVO Y el ANTERIOR a cada
-- dispositivo conectado. Esa tabla tiene una sola fila por hogar, se escribe
-- con upsert y nunca se borra, así que no necesita el filtro en DELETE: con la
-- identidad por defecto (su clave primaria, hogar_id) cada cambio manda solo el
-- documento nuevo.
--
-- Ejecutar en el SQL Editor de Supabase. Es idempotente y opcional.

alter table public.pablo_estado replica identity default;

-- Verificación: debe salir 'd' (default).
select relname, relreplident
  from pg_class
 where oid = 'public.pablo_estado'::regclass;
