-- 006 — Añade las dos apps externas (Viajes e Idiomas) al hogar de casa.
--
-- El hub solo pinta las áreas que están en hogares.areas, para que un hogar
-- invitado no vea las secciones de otro. Las tarjetas nuevas no aparecerán
-- hasta ejecutar esto.
--
-- Ejecutar en el SQL Editor de Supabase.

update public.hogares
   set areas = (
     select array_agg(distinct a order by a)
       from unnest(areas || array['viajes','idiomas']) as a
   )
 where nombre = 'Casa';   -- si tu hogar se llama de otra forma, cámbialo aquí

-- Verificación: debe listar las seis áreas.
select nombre, areas from public.hogares;
