-- 007 — Añade el hub de estudio de la oposición (oposicion.html) al hogar de casa.
--
-- El hub solo pinta las áreas que están en hogares.areas, para que un hogar
-- invitado no vea las secciones de otro. La tarjeta nueva no aparecerá
-- hasta ejecutar esto.
--
-- Ejecutar en el SQL Editor de Supabase.

update public.hogares
   set areas = (
     select array_agg(distinct a order by a)
       from unnest(areas || array['oposicion']) as a
   )
 where nombre = 'Casa';   -- si tu hogar se llama de otra forma, cámbialo aquí

-- Verificación: debe aparecer 'oposicion' entre las áreas.
select nombre, areas from public.hogares;
