-- 019 — Documentos: categorías «Identificación» y «Vacunas».
-- Las añade a todos los hogares que no las tengan (sin duplicar: un tipo no
-- puede repetirse en un hogar, sin importar mayúsculas). Idempotente.
-- Ejecutar ENTERO en el SQL Editor de Supabase.
insert into public.document_types (hogar_id, name, plural_label, emoji, sort_order)
select h.id, v.name, v.plural_label, v.emoji, v.sort_order
  from public.hogares h
 cross join (values
   ('Identificación', 'IDENTIFICACIÓN', E'\U0001FAAA', 5),
   ('Vacunas',        'VACUNAS',        E'\U0001F489', 85)
 ) as v(name, plural_label, emoji, sort_order)
on conflict do nothing;

-- Verificación
select h.nombre as hogar, t.name, t.plural_label, t.sort_order
  from public.document_types t join public.hogares h on h.id = t.hogar_id
 order by h.nombre, t.sort_order;
