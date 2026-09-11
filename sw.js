/* Service Worker — Niblo
   - HTML: stale-while-revalidate contra un cache PROPIO y estable.
   - Iconos/manifest: cache-first, en un cache con version.

   Por que dos caches: CACHE_NAME cambia en cada publicacion para que el
   navegador detecte el service worker nuevo y salga el aviso de "hay una
   version nueva". Si el documento viviera ahi, cada publicacion lo borraria
   y la siguiente entrada seria una descarga completa — y sin conexion, un
   error. Con once versiones en dos dias eso es justo lo que pasaba. El
   documento vive en CACHE_DOC, que no se borra nunca.
*/
const CACHE_NAME = "niblo-v131";  // campos de formulario: sin desbordes ni zoom
const CACHE_DOC  = "niblo-doc";   // el documento; estable entre versiones
const ASSETS_ESTATICOS = [
  "./manrope.woff2",
  "./manifest.json",
  "./icon.svg",
  "./icon-192.png",
  "./icon-512.png",
  "./apple-touch-icon.png",
  "./favicon.png"
];

/* Una sola clave para el documento, sea cual sea la URL con la que se entre:
   "/niblo/", "/niblo/index.html" o "/niblo/?loquesea" son la misma pagina.
   Guardando por la request tal cual, entrar con una URL distinta de la
   guardada fallaba el match y se iba a la red. */
const DOC_KEY = new URL("./", self.location).href;

self.addEventListener("install", (event) => {
  event.waitUntil((async () => {
    const estaticos = await caches.open(CACHE_NAME);
    /* Uno a uno y tolerando fallos: con addAll, si UNO de los archivos no esta
       (un icono renombrado, la fuente sin subir) revienta la instalacion
       entera y el usuario se queda sin service worker y sin offline. */
    await Promise.all(ASSETS_ESTATICOS.map(u => estaticos.add(u).catch(() => {})));
    /* El documento se guarda ya en la instalacion: asi la app abre sin
       conexion desde la primera visita. Si falla, no se tumba la instalacion. */
    try {
      const resp = await fetch(DOC_KEY, { cache: "reload" });
      if (resp && resp.ok) (await caches.open(CACHE_DOC)).put(DOC_KEY, resp);
    } catch (_) {}
  })());
});

self.addEventListener("message", (event) => {
  if (event.data && event.data.type === "SKIP_WAITING") {
    self.skipWaiting();
  }
});

self.addEventListener("activate", (event) => {
  event.waitUntil((async () => {
    const doc = await caches.open(CACHE_DOC);
    /* Rescatar el documento del cache de la version anterior antes de tirarlo:
       si no, al estrenar esto habria una carga fria mas. */
    if (!(await doc.match(DOC_KEY))) {
      for (const n of await caches.keys()) {
        if (n === CACHE_DOC) continue;
        const viejo = await caches.open(n);
        const r = (await viejo.match(DOC_KEY)) || (await viejo.match("./"));
        if (r) { await doc.put(DOC_KEY, r.clone()); break; }
      }
    }
    const names = await caches.keys();
    await Promise.all(names
      .filter(n => n !== CACHE_NAME && n !== CACHE_DOC)
      .map(n => caches.delete(n)));
    await self.clients.claim();
  })());
});

self.addEventListener("fetch", (event) => {
  const url = new URL(event.request.url);
  // Solo same-origin y GET.
  if (url.origin !== self.location.origin) return;
  if (event.request.method !== "GET") return;

  const esHTML = event.request.mode === "navigate"
    || event.request.destination === "document"
    || url.pathname.endsWith(".html")
    // Raiz del scope del SW, sea cual sea la carpeta publicada: asi no depende
    // del nombre del repositorio.
    || url.pathname === new URL("./", self.location).pathname;

  if (esHTML) {
    /* STALE-WHILE-REVALIDATE: se sirve la copia guardada al momento y la
       version nueva se descarga por detras. Cuando llega, el service worker
       nuevo dispara el aviso de "version nueva" que ya existe en la app. */
    event.respondWith((async () => {
      const cache = await caches.open(CACHE_DOC);
      const guardado = await cache.match(DOC_KEY);
      const red = fetch(event.request)
        .then((resp) => {
          if (resp && resp.ok) cache.put(DOC_KEY, resp.clone());
          return resp;
        })
        .catch(() => guardado);
      return guardado || red;
    })());
    return;
  }

  // CACHE-FIRST para iconos/manifest/etc.
  event.respondWith(
    caches.match(event.request).then((cached) => {
      if (cached) return cached;
      return fetch(event.request).then((resp) => {
        if (resp.ok) {
          const copy = resp.clone();
          caches.open(CACHE_NAME).then(c => c.put(event.request, copy));
        }
        return resp;
      });
    })
  );
});
