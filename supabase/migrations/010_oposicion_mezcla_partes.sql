-- ============================================================================
-- Niblo · 010 — Hub de la oposición: mezcla por partes al sincronizar
--
-- Con la 009, si dos dispositivos editaban el mismo tema casi a la vez (uno el
-- glosario y otro los apuntes, o uno sin conexión), ganaba el tema ENTERO del
-- último y se perdía lo del otro. Ahora cada parte del tema (apuntes,
-- glosario, cronología, flashcards, test y datos del archivo) lleva su propia
-- fecha en datos->'mod', y el servidor se queda con la más reciente de cada
-- parte. El navegador hace la misma mezcla al bajar.
--
-- Borrar o restaurar un tema sigue decidiéndose por la fecha del tema entero.
--
-- Además, el progreso de cada persona guarda ahora más cosas que las
-- flashcards: apartados repasados, textos resaltados, respuestas del test y
-- resultados. Las que llevan datos (el texto resaltado, los aciertos…) los
-- guardan en la columna nueva oposicion_progreso.datos.
--
-- Requiere 009_oposicion_sync.sql. Ejecutar entero en el SQL Editor. Idempotente.
-- ============================================================================

alter table public.oposicion_progreso add column if not exists datos jsonb;

create or replace function public.oposicion_temas_mezcla()
returns trigger language plpgsql as $$
declare
  k      text;
  mezcla jsonb;
  mn     bigint;
  mo     bigint;
begin
  if tg_op = 'INSERT' then
    new.actualizado = now();
    return new;
  end if;

  -- Borrar o restaurar: decide la fecha del tema entero.
  if new.borrado or old.borrado or new.datos is null or old.datos is null then
    if new.modificado < old.modificado then return null; end if;
    new.actualizado = now();
    return new;
  end if;

  mezcla := old.datos;
  if jsonb_typeof(mezcla->'mod') is distinct from 'object' then
    mezcla := mezcla || '{"mod":{}}'::jsonb;
  end if;

  foreach k in array array['meta','sections','glossary','timeline','flashcards','questions'] loop
    mn := coalesce((new.datos->'mod'->>k)::bigint, (extract(epoch from new.modificado) * 1000)::bigint);
    mo := coalesce((old.datos->'mod'->>k)::bigint, (extract(epoch from old.modificado) * 1000)::bigint);
    if mn > mo then
      if k = 'meta' then
        mezcla := mezcla || jsonb_build_object(
          'title',    new.datos->'title',
          'subtitle', new.datos->'subtitle',
          'etiquetas', new.datos->'etiquetas',
          'fileName', new.datos->'fileName',
          'html',     new.datos->'html',
          'cargado',  new.datos->'cargado');
      else
        mezcla := jsonb_set(mezcla, array[k], coalesce(new.datos->k, '[]'::jsonb), true);
      end if;
      mezcla := jsonb_set(mezcla, array['mod', k], to_jsonb(mn), true);
    else
      mezcla := jsonb_set(mezcla, array['mod', k], to_jsonb(mo), true);
    end if;
  end loop;

  -- Nada nuevo (p. ej. una subida repetida o más vieja): no se toca la fila.
  if mezcla = old.datos and new.modificado <= old.modificado then
    return null;
  end if;

  new.datos       := mezcla;
  new.modificado  := greatest(new.modificado, old.modificado);
  new.actualizado := now();
  return new;
end $$;

drop trigger if exists oposicion_temas_lww on public.oposicion_temas;
drop trigger if exists oposicion_temas_mezcla on public.oposicion_temas;
create trigger oposicion_temas_mezcla
  before insert or update on public.oposicion_temas
  for each row execute function public.oposicion_temas_mezcla();

-- Comprobación: debe salir una fila con oposicion_temas_mezcla y la columna datos = true.
select (select string_agg(tgname, ', ') from pg_trigger
         where tgrelid = 'public.oposicion_temas'::regclass and not tgisinternal) as trigger_temas,
       exists (select 1 from information_schema.columns
                where table_schema = 'public' and table_name = 'oposicion_progreso' and column_name = 'datos') as columna_datos;
