"""Postet den obersten CHANGELOG-Eintrag als goldenes Embed in Discord (#updates).

Umgebungsvariablen: HOOK (Discord-Webhook-URL), URL (Dashboard-Link).
"""
import json
import os
import pathlib
import re
import urllib.request

text = pathlib.Path("CHANGELOG.md").read_text(encoding="utf-8")
m = re.search(r"^##\s+(\S+)\s*·\s*(\S+)\s*·\s*(.+?)\s*$\n(.*?)(?=^##\s|\Z)", text, re.M | re.S)
version, date, headline, body = m.group(1), m.group(2), m.group(3), m.group(4).strip()
link = os.environ.get("URL") or ""

payload = {
    "username": "Deavest Trading Desk",
    "embeds": [{
        "title": f"✦ Trading Desk {version} is live — {headline}",
        "url": link or None,
        "description": (body[:3500] + ("\n\n" if body else "") +
                        (f"**Open the dashboard:** {link}\nNo download needed — the page updates itself." if link else "")),
        "color": 0xC9A24A,
        "footer": {"text": f"Deavest Asset Management · {date} · No financial advice"},
    }],
}
req = urllib.request.Request(
    os.environ["HOOK"],
    data=json.dumps(payload).encode(),
    headers={"Content-Type": "application/json", "User-Agent": "deavest-desk-ci"},
)
urllib.request.urlopen(req, timeout=20).read()
print("Discord announcement sent")
