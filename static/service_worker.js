self.addEventListener('install', function(event) {
  console.log('FatimBot installé');
});

self.addEventListener('fetch', function(event) {
  event.respondWith(fetch(event.request));
});
