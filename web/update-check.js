/* Deavest Trading Desk · Web-Update-Check
   Läuft nur in der Browser-Version (GitHub Pages). In der Windows-App (window.deavest)
   übernimmt der eingebaute Updater. Prüft alle 3 Minuten und beim Zurückkehren in den Tab
   die Datei version.json. Gibt es eine neue Version, erscheint unten eine goldene Leiste
   „Neue Version – jetzt laden“. Niemand muss etwas herunterladen oder neu installieren. */
(function () {
  if (window.deavest) return;
  var current = null, shown = false;
  function url() { return 'version.json?t=' + Date.now(); }
  function show(v) {
    if (shown) return; shown = true;
    var b = document.createElement('div');
    b.id = 'webUpdBar'; b.className = 'updbar';
    b.setAttribute('role', 'status'); b.style.zIndex = '99999';
    b.innerHTML = '<span>✦</span><div><b>Neue Version ' + (v.version || '') + '</b><small>' +
      (v.note || 'Das Dashboard wurde aktualisiert.') + '</small></div>' +
      '<button class="btn-gold" id="webUpdGo">Jetzt laden</button>';
    document.body.appendChild(b);
    document.getElementById('webUpdGo').onclick = function () { location.reload(); };
  }
  function check() {
    fetch(url(), { cache: 'no-store' }).then(function (r) { return r.ok ? r.json() : null; })
      .then(function (v) {
        if (!v || !v.version) return;
        if (current === null) { current = v.version; return; }
        if (v.version !== current) show(v);
      }).catch(function () {});
  }
  check();
  setInterval(check, 180000);
  document.addEventListener('visibilitychange', function () { if (!document.hidden) check(); });
})();
