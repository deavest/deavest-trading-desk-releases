# deavest-trading-desk-releases

Hier liegen (1) die Installer der Windows-App unter *Releases* und (2) die Online-Version des Dashboards im Ordner `web/`.

## Deavest Trading Desk · Online-Version

**Ein Link für alle. Immer die neueste Version. Kein Download.**

```
web/                 das Dashboard (index.html) + Update-Check
CHANGELOG.md         was ist neu – oberster Eintrag = aktuelle Version
scripts/             Hilfsskripte (optional, für späteren Auto-Post)
```

## So läuft ein Update

1. Du sagst Claude, was sich ändern soll („Spiel ein Update ein: …“).
2. Claude ändert `web/index.html`, erhöht die Version in `web/version.json` und schreibt oben einen Eintrag in `CHANGELOG.md`.
3. GitHub Desktop → *Commit to main* → *Push origin*. Nach ca. 1 Minute ist die neue Version online:
   - der Link zeigt sofort die neue Version
   - wer das Dashboard gerade offen hat, bekommt unten eine goldene Leiste **„Neue Version – Jetzt laden“**
   - Claude postet das Update in Discord **#updates**

Niemand muss etwas herunterladen, installieren oder nachfragen.

## Einmalige Einrichtung

**GitHub Pages einschalten:** Repo → *Settings* → *Pages* → *Source: Deploy from a branch* → Branch `main`, Ordner `/ (root)` → *Save*.

**Link fürs Dashboard:** https://deavest.github.io/deavest-trading-desk-releases/web/

## Windows-App

Die EXE erkennt sich selbst (`window.deavest`) und nutzt weiter ihren eingebauten Updater;
der Web-Update-Check ist dort automatisch aus.
