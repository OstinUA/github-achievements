"""Check shared data, complete translations, generated Markdown and local links."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

from build_catalog import ROOT, GROUPS, build

errors = []


def expect(condition, message):
    if not condition:
        errors.append(message)


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def anchors(text):
    result = set(re.findall(r'<a\s+id="([^"]+)"', text))
    counts = {}
    for heading in re.findall(r'^#{1,6}\s+(.+)$', text, re.M):
        slug = re.sub(r'[^\w\-\s]', '', heading.lower()).replace(' ', '-')
        number = counts.get(slug, 0)
        counts[slug] = number + 1
        result.add(slug + (f'-{number}' if number else ''))
    return result


def main():
    data = read(ROOT / "data/achievements.json")
    languages = read(ROOT / "i18n/languages.json")
    english = read(ROOT / "i18n/en.json")
    source_ids = {s["id"] for s in data["sources"]}
    ids = {a["id"] for a in data["achievements"]}
    hids = {h["id"] for h in data["highlights"]}
    expect(len(ids) == len(data["achievements"]), "Duplicate achievement IDs")
    expect(len(hids) == len(data["highlights"]), "Duplicate highlight IDs")
    expect(len(source_ids) == len(data["sources"]), "Duplicate source IDs")
    expect(len({l["code"] for l in languages}) == len(languages), "Duplicate language codes")
    expect(len({l["file"] for l in languages}) == len(languages), "Duplicate language filenames")
    for a in data["achievements"]:
        expect(a["status"] in GROUPS, f'{a["id"]}: unknown status')
        expect(a["publicly_earnable"] == (a["status"] == "active"), f'{a["id"]}: earnability/status conflict')
        expect(bool(a["sources"]) and set(a["sources"]) <= source_ids, f'{a["id"]}: invalid sources')
        expect(not a["tiers"] or (len(a["tiers"]) == 4 and a["tiers"] == sorted(set(a["tiers"]))), f'{a["id"]}: invalid tier sequence')
        if a.get("reported_tiers"):
            expect(a["status"] == "experimental" and not a["tiers"] and len(a["reported_tiers"]) == 4, f'{a["id"]}: experimental tiers must remain separate')
    for h in data["highlights"]:
        expect(h["status"] in ("active", "retired") and set(h["sources"]) <= source_ids, f'{h["id"]}: invalid highlight status/sources')
    mars = read(ROOT / "data/mars-2020-repositories.json")
    expect(mars["event_closed"] is True, "Historical Mars event must remain marked closed")
    expect(mars["entry_count"] == len(mars["repositories"]), "Mars entry count mismatch")
    expect(mars["repository_count"] == len({r["repository"] for r in mars["repositories"]}), "Mars unique repository count mismatch")
    expect(len({(r["repository"], r["version"], r["tag"]) for r in mars["repositories"]}) == len(mars["repositories"]), "Duplicate Mars version records")
    for lang in languages:
        path = ROOT / f'i18n/{lang["code"]}.json'
        translation = read(path)
        expect(translation["code"] == lang["code"], f'{path.name}: language code mismatch')
        for section in ("ui", "descriptions", "highlights", "units"):
            expect(set(translation[section]) == set(english[section]), f'{path.name}: incomplete {section} keys')
            expect(all(isinstance(v, str) and v.strip() for v in translation[section].values()), f'{path.name}: empty {section} values')
        expect(set(translation["descriptions"]) == ids, f'{path.name}: achievement coverage mismatch')
        expect(set(translation["highlights"]) == hids, f'{path.name}: highlight coverage mismatch')
        for value in translation["descriptions"].values():
            expect(not re.search(r'\]\(#[^)]*\)', value), f'{path.name}: legacy description anchor')
    manifest = read(ROOT / "assets/manifest.json")
    manifest_paths = {m["path"] for m in manifest}
    expect(len(manifest_paths) == len(manifest), "Duplicate artwork provenance entries")
    for item in manifest:
        path = ROOT / item["path"]
        expect(path.exists(), f'Missing artwork: {item["path"]}')
        if path.exists():
            expect(path.read_bytes().startswith(b'\x89PNG\r\n\x1a\n'), f'Invalid PNG: {item["path"]}')
        expect(urlsplit(item["origin"]).scheme == "https", f'Invalid asset origin: {item["path"]}')
    expect({p.relative_to(ROOT).as_posix() for folder in ("badges", "variants", "legacy") for p in (ROOT / "assets" / folder).glob("*.png")} == manifest_paths, "Artwork/provenance coverage mismatch")
    # Check every Markdown link and HTML image, including translated navigation.
    md_files = list(ROOT.rglob("*.md"))
    link_count = 0
    for path in md_files:
        text = path.read_text(encoding="utf-8")
        cleaned = re.sub(r'```.*?```', '', text, flags=re.S)
        targets = re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', cleaned)
        targets += re.findall(r'<img\s[^>]*src="([^"]+)"', cleaned)
        for target in targets:
            target = target.strip().strip('<>')
            if urlsplit(target).scheme or target.startswith('//'):
                continue
            local, _, fragment = target.partition('#')
            resolved = (path.parent / unquote(local)).resolve() if local else path
            expect(resolved.exists(), f'{path.relative_to(ROOT)}: missing target {target}')
            if resolved.exists() and fragment and resolved.suffix == '.md':
                expect(unquote(fragment) in anchors(resolved.read_text(encoding="utf-8")), f'{path.relative_to(ROOT)}: missing anchor {target}')
            link_count += 1
    if errors:
        raise SystemExit("\n".join(errors))
    build(check=True)
    print(f'OK: {len(languages)} complete translations; {len(md_files)} Markdown files; {link_count} local links/images; {len(manifest)} attributed PNG assets')


if __name__ == '__main__':
    try:
        main()
    except (KeyError, ValueError, OSError) as error:
        print(f'Catalogue validation failed: {error}', file=sys.stderr)
        raise SystemExit(1)
