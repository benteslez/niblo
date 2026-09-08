/* Service Worker — Niblo
   - HTML: stale-while-revalidate (abre al instante con la copia guardada y
     descarga la versión nueva por detrás; el aviso de "versión nueva" que ya
     tiene la app avisa cuando esté lista).
   - Iconos/manifest: cache-first (no cambian).
   Cambia CACHE_NAME tras un cambio importante para invalidar el cache.
*/
const CACHE_NAME = "niblo-v110";  // linea de la hora actual en el patron
const ASSETS_ESTATICOS = [
  "./manifest.json",
  "./icon.svg",
  "./icon-192.png",
  "./icon-512.png",
  "./apple-touch-icon.png",
  "./favicon.png"
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) =>
      cache.addAll(ASSETS_ESTATICOS)
        /* El documento se guarda ya en la instalacion: asi la app abre sin
           conexion desde la primera visita y no hace falta haber entrado dos
           veces. Aparte, para que un fallo aqui no tumbe la instalacion. */
        .then(() => cache.add("./").catch(() => {}))
    )
  );
});

self.addEventListener("message", (event) => {
  if (event.data && event.data.type === "SKIP_WAITING") {
    self.skipWaiting();
  }
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys()
      .then((names) => Promise.all(names.filter(n => n !== CACHE_NAME).map(n => caches.delete(n))))
      .then(() => self.clients.claim())
  );
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
    /* STALE-WHILE-REVALIDATE para HTML. Antes se esperaba a la red en cada
       arranque y el documento pasa de 2 MB, asi que con cobertura mala se
       veia la pantalla de carga varios segundos. Ahora se sirve la copia
       guardada al momento y la version nueva se descarga por detras: cuando
       llega, el service worker nuevo dispara el aviso de "version nueva" que
       ya existe en la app. */
    event.respondWith(
      caches.open(CACHE_NAME).then((cache) =>
        cache.match(event.request).then((guardado) => {
          const red = fetch(event.request)
            .then((resp) => {
              if (resp && resp.ok) cache.put(event.request, resp.clone());
              return resp;
            })
            .catch(() => guardado || caches.match("./"));
          return guardado || red;
        })
      )
    );
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
