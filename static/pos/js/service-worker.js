const cacheName = "generate-bill-cache-test-v2.9";
const cacheFiles = [
  '/pos',
  '/pos/dashboard/',
  '/pos/report/',
  '/pos/view_inward/',
  '/pos/view_invoice/',
  '/pos/view_packing/',
  '/pos/view_exception/',
  '/pos/load_table_data/',
  '/pos/loadinvoice_table_data/',
  '/pos/mark_as_done/',
  '/pos/mark_as_done_inv/',
  '/pos/generate_bill/',
  '/pos/save_bill/',
  '/pos/fetch_dispatch_data/',
  '/pos/analysis/',
  '/pos/item-wise-analysis/',
  '/pos/price-wise-analysis/',
  '/pos/supplier-wise-analysis/',
  '/pos/city-wise-analysis/',
  '/pos/login/',
  '/pos/validate_password/',
  '/pos/logout/',
  '/static/pos/css/style.css',
  '/static/pos/js/main.js',
  '/static/pos/js/jquery-3.7.1.min.js',
  '/static/pos/css/generate_bill.css',
  '/static/pos/js/generate_bill.js',
  '/static/pos/assets/vendor/bootstrap/css/bootstrap.min.css',
  '/static/pos/assets/vendor/bootstrap/js/bootstrap.bundle.min.js',
  // Include other necessary CSS and JS files
  '/static/pos/assets/vendor/apexcharts/apexcharts.min.js',
  '/static/pos/assets/vendor/chart.js/chart.umd.js',
  '/static/pos/assets/vendor/echarts/echarts.min.js',
  '/static/pos/assets/vendor/quill/quill.min.js',
  '/static/pos/assets/vendor/simple-datatables/simple-datatables.js',
  // Include images, icons, etc.
  '/static/pos/assets/favicon.png',
  '/static/pos/assets/apple-touch-icon.png',
  // Include manifest.json and service-worker.js
  '/static/pos/js/manifest.json',
  '/static/pos/js/service-worker.js',
];

self.addEventListener("install", function (event) {
  event.waitUntil(
    caches.open(cacheName).then(function (cache) {
      return Promise.all(
        cacheFiles.map(function (url) {
          return fetch(url)
            .then(function (response) {
              if (!response.ok) {
                throw new Error('Request failed: ' + response.statusText);
              }
              return cache.put(url, response);
            })
            .catch(function (error) {
              console.log('Failed to cache file:', error);
            });
        })
      );
    })
  );
});

self.addEventListener("fetch", function (event) {
  event.respondWith(
    caches.match(event.request).then(function (response) {
      return response || fetch(event.request).catch(function () {
        // Provide a fallback response for failed fetch requests
        console.log("Offline Mode: Unable to fetch resource.");
      });
    })
  );
});
self.addEventListener("activate", function (event) {
  event.waitUntil(
    // Claim clients immediately to activate the new service worker
    self.clients.claim()
  );
});
