"""Lint a README for what references/readme.md says a script can catch.

Usage: python3 -I readme-check.py README.md

FAIL (exit 1): a local link or image that doesn't exist, an SVG with live <text>
(GitHub serves SVG with no web fonts), an emoji in a heading.
WARN: a LICENSE file with no license badge, more than three badges, a count in the top fold ("33 skills"), an image with
no dark version (#gh-dark-mode-only), a <picture> switch (it follows the OS, not
GitHub's theme), a PNG too narrow for 2x at its display width, an image over 1MB.
"""

import re
import struct
import sys
from pathlib import Path

if len(sys.argv) != 2:
    raise SystemExit(__doc__)
readme = Path(sys.argv[1]).resolve()
root = readme.parent
text = readme.read_text()
fails, warns = [], []

COLUMN = 838  # GitHub's README column on desktop, measured November 2026
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐✅❌]")
COUNT = re.compile(
    r"\b(\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|"
    r"(?:twenty|thirty|forty|fifty)(?:[- ]\w+)?)\s+(?:\w+\s+)?(skills|agents|plugins|commands|tools|roles)\b",
    re.I,
)


RAW = re.compile(r"^https://github\.com/[^/]+/[^/]+/raw/[^/]+/(.+)$")


def local(url):
    """A repo-relative path, or the path inside a github.com/<repo>/raw/<branch>/ URL."""
    url = url.split("#", 1)[0]
    m = RAW.match(url)
    if m:
        return m.group(1)
    if re.match(r"^[a-z]+:", url) or url.startswith("//"):
        return None
    return url


def png_width(path):
    with open(path, "rb") as f:
        head = f.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return struct.unpack(">I", head[16:20])[0]


# Headings
for line in text.splitlines():
    if line.startswith("#") and EMOJI.search(line):
        fails.append(f"emoji in heading: {line.strip()}")

# Badges
badges = re.findall(r"(shields\.io|badge\.svg|badgen\.net|/badge/)", text)
if len(badges) > 3:
    warns.append(f"{len(badges)} badges; keep to three or fewer, one style")
if any((root / n).exists() for n in ("LICENSE", "LICENSE.md", "LICENSE.txt")) and not re.search(r"badge/license", text, re.I):
    warns.append("LICENSE file but no license badge in the top fold (shields.io badge/license-<name>-blue, linked to LICENSE)")

# Counts in the top fold: everything before the first ## heading
top = text.split("\n## ", 1)[0]
top_prose = re.sub(r"<[^>]+>", " ", top)
for m in COUNT.finditer(top_prose):
    warns.append(f"count in the top fold drifts as the repo grows: '{m.group(0)}'")

# Local links and images
targets = re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", text)
targets += re.findall(r'(?:src|srcset|href)="([^"#]+)"', text)
for t in set(targets):
    rel = local(t)
    if rel and not (root / rel).exists():
        fails.append(f"missing file in the repo: {t}")
if "prefers-color-scheme" in text:
    warns.append("<picture> with prefers-color-scheme follows the OS, not GitHub's theme; use two <img> tags ending #gh-light-mode-only and #gh-dark-mode-only")

# Images: dark variants, 2x, size, SVG text
for m in re.finditer(r"<img\b[^>]*>", text):
    tag = m.group(0)
    src = re.search(r'src="([^"]+)"', tag)
    if not src or not local(src.group(1)):
        continue
    path = root / local(src.group(1))
    before = text[: m.start()]
    in_picture = before.rfind("<picture") > before.rfind("</picture>")
    themed = src.group(1).endswith(("#gh-light-mode-only", "#gh-dark-mode-only"))
    if not (in_picture or themed):
        warns.append(f"{src.group(1)}: no dark version; pair it with a #gh-dark-mode-only image")
    if not path.exists():
        continue
    if path.stat().st_size > 1_000_000:
        warns.append(f"{src.group(1)}: {path.stat().st_size // 1024}KB; keep images under about 1MB")
    width = re.search(r'width="(\d+)(%?)"', tag)
    shown = COLUMN if not width or width.group(2) else int(width.group(1))
    if path.suffix.lower() == ".png":
        native = png_width(path)
        if native and native < 2 * shown:
            warns.append(f"{src.group(1)}: {native}px wide shown at {shown}; export at {2 * shown}px or more for 2x")

for svg in set(re.findall(r'(?:src|srcset)="([^"#]+\.svg)(?:#[^"]*)?"', text)):
    if not local(svg):
        continue
    p = root / local(svg)
    if p.exists() and re.search(r"<text\b", p.read_text()):
        fails.append(f"{svg}: live <text>; outline it to paths (GitHub loads no web fonts in SVG)")

for w in warns:
    print(f"WARN  {w}")
for f in fails:
    print(f"FAIL  {f}")
print(f"{len(fails)} fail, {len(warns)} warn")
sys.exit(1 if fails else 0)
