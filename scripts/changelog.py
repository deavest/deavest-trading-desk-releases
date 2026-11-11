"""Liest den obersten Eintrag aus CHANGELOG.md.

Format eines Eintrags:
    ## v4.0 · 2026-11-11 · Kurze Überschrift
    - Punkt 1
    - Punkt 2

Ausgabe als GitHub-Actions-Output (version, date, headline, body).
"""
import json
import pathlib
import re
import sys

text = pathlib.Path("CHANGELOG.md").read_text(encoding="utf-8")
m = re.search(r"^##\s+(\S+)\s*·\s*(\S+)\s*·\s*(.+?)\s*$\n(.*?)(?=^##\s|\Z)", text, re.M | re.S)
if not m:
    sys.exit("CHANGELOG.md: kein Eintrag im Format '## vX.Y · JJJJ-MM-TT · Überschrift' gefunden")
version, date, headline, body = m.group(1), m.group(2), m.group(3), m.group(4).strip()
print(f"version={version}")
print(f"date={date}")
print(f"headline={headline}")
print(f"body={json.dumps(body, ensure_ascii=False)}")
