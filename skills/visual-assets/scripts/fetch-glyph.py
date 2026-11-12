#!/usr/bin/env python3
"""Source a line glyph from any Iconify set, normalize it for a 140px stage, recolor to tokens.

  fetch-glyph.py search "whistle" [--limit 64] [--sets lucide,tabler,...]
  fetch-glyph.py get lucide:whistle [--height 140] [--stroke 1.75] [--color "var(--color-control, #8E8A81)"] [--out DIR]

Path 1 is the Iconify API (api.iconify.design). Path 2, used automatically when the API
rate-limits (429/403), is the same data from npm via jsDelivr (@iconify-json/<prefix>/icons.json),
cached in ~/.cache/iconify-json. Stdlib only. `get` re-weights a stroke set to a true pixel stroke at
the target height and writes a .raw.svg plus a tokenized copy. Record the license in ATTRIBUTIONS.md
beside the output.
"""
import json, os, re, sys, urllib.request, urllib.parse

API = "https://api.iconify.design"
CDN = "https://cdn.jsdelivr.net/npm/@iconify-json/{p}/icons.json"
CACHE = os.path.expanduser("~/.cache/iconify-json")
DEFAULT_SETS = "lucide,lucide-lab,tabler,ph,hugeicons,iconoir,mingcute,solar,material-symbols,mdi,game-icons,streamline-freehand,iconmind"

def http(url, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": "fetch-glyph/1"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read()

def set_json(prefix):
    os.makedirs(CACHE, exist_ok=True)
    p = os.path.join(CACHE, prefix + ".json")
    if not os.path.exists(p):
        _, body = http(CDN.format(p=prefix), timeout=180)
        open(p, "wb").write(body)
    return json.load(open(p))

def svg_from_json(prefix, name):
    d = set_json(prefix)
    ic = d["icons"].get(name)
    if ic is None:
        al = d.get("aliases", {}).get(name)
        if not al: raise SystemExit(f"{prefix}:{name} not in set")
        ic = d["icons"][al["parent"]]
    w = ic.get("width", d.get("width", 16)); h = ic.get("height", d.get("height", 16))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="{ic.get("left",0)} {ic.get("top",0)} {w} {h}">{ic["body"]}</svg>'), d.get("info", {})

def get_raw(prefix, name):
    try:
        st, body = http(f"{API}/{prefix}/{name}.svg", timeout=20)
        s = body.decode()
        if st == 200 and "<svg" in s and len(s) > 40:
            return s, "api"
    except Exception as e:
        pass
    s, _ = svg_from_json(prefix, name)
    return s, "jsdelivr"

def normalize(svg, height=140, stroke_px=1.75, color="var(--color-control, #8E8A81)"):
    vb = re.search(r'viewBox="([\d.\- ]+)"', svg)
    x, y, w, h = map(float, vb.group(1).split())
    scale = height / h
    width = round(w * scale, 2)
    is_stroke = 'stroke="currentColor"' in svg or "stroke:currentColor" in svg
    if is_stroke:
        sw = round(stroke_px / scale, 3)           # stroke as a fraction of the grid, so 1.75 CSS px at `height`
        svg = re.sub(r'stroke-width="[\d.]+"', f'stroke-width="{sw}"', svg)
        if 'stroke-width=' not in svg:
            svg = svg.replace("<svg ", f'<svg stroke-width="{sw}" ', 1)
    svg = svg.replace("currentColor", color)
    # size only the root <svg> tag; Iconify roots carry width="1em", and a numeric-only match would hit a child rect
    def _size_root(m):
        tag = m.group(0)
        tag = re.sub(r'\swidth="[^"]*"', '', tag)
        tag = re.sub(r'\sheight="[^"]*"', '', tag)
        return tag.replace('<svg', f'<svg width="{width}" height="{height}"', 1)
    svg = re.sub(r'<svg\b[^>]*>', _size_root, svg, count=1)
    if "shape-rendering" not in svg:
        svg = svg.replace("<svg ", '<svg shape-rendering="geometricPrecision" ', 1)
    return svg, {"kind": "stroke" if is_stroke else "filled-outline", "grid": h, "scale": round(scale, 2),
                 "stroke_units": (round(stroke_px / scale, 3) if is_stroke else None)}

def search(q, limit=64, sets=None):
    try:
        st, body = http(f"{API}/search?query={urllib.parse.quote(q)}&limit={limit}", timeout=20)
        d = json.loads(body); return d.get("icons", []), "api"
    except Exception:
        pass
    out = []
    for p in (sets or DEFAULT_SETS).split(","):
        try: d = set_json(p)
        except Exception: continue
        names = list(d["icons"]) + list(d.get("aliases", {}))
        out += [f"{p}:{n}" for n in names if re.search(q.replace(" ", "-"), n)]
    return out[:limit], "jsdelivr-grep"

def arg(flag, default):
    return sys.argv[sys.argv.index(flag) + 1] if flag in sys.argv else default

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"
    if cmd == "search":
        icons, via = search(sys.argv[2], int(arg("--limit", 64)), arg("--sets", None))
        print(f"# via {via}, {len(icons)} hits"); print("\n".join(icons))
    elif cmd == "get":
        prefix, name = sys.argv[2].split(":")
        out = arg("--out", "."); os.makedirs(out, exist_ok=True)
        raw, via = get_raw(prefix, name)
        norm, meta = normalize(raw, int(arg("--height", 140)), float(arg("--stroke", 1.75)), arg("--color", "var(--color-control, #8E8A81)"))
        base = os.path.join(out, f"{prefix}-{name}")
        open(base + ".raw.svg", "w").write(raw); open(base + ".svg", "w").write(norm)
        print(f"{prefix}:{name} via {via} {meta} -> {base}.svg")
    else:
        print(__doc__)
