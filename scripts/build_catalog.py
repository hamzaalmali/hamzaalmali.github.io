#!/usr/bin/env python3
"""Regenerate only the main catalogue from apps.json; app pages remain independent."""
import json, re
from html import escape
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
apps = json.loads((ROOT / "apps.json").read_text())
cards=[]
seen=set()
for app in apps:
    slug=app["slug"]
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug) and slug not in seen, slug
    seen.add(slug)
    assert (ROOT / slug / "index.html").is_file(), f"Missing page: {slug}"
    icon=app.get("icon")
    img=""
    if icon:
        assert (ROOT / slug / icon).is_file(), f"Missing icon: {slug}"
        img=f'<img class="app-icon" src="/{slug}/{escape(icon, quote=True)}" alt="">'
    cards.append(f'<a class="card" href="/{slug}/">{img}<div class="eyebrow">{escape(app["platforms"])}</div><h2>{escape(app["name"])}</h2><p>{escape(app["description"])}</p></a>')
template=(ROOT / "catalog.template.html").read_text()
(ROOT / "index.html").write_text(template.replace("<!-- APP_CARDS -->", "\n".join(cards)))
print(f"Built catalogue: {len(apps)} apps")
