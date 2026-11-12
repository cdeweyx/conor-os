"""Wordmark from a real font's outlines: set the word, track it, optionally mask one cut, emit SVG.

Usage:
  python wordmark.py <font.ttf|otf|woff2> "<Word>" [--track -0.02] [--cut x,y,w,h[,skew]] [--out wordmark.svg]

--track is in ems (negative tightens). --cut is a rectangle masked out of the word, in fractions of the
word's width (x, w) and cap height (y from the baseline up, h), with an optional skewY in degrees: the
one deliberate cut, slice, or notch that makes a font sample into a mark. Fill is currentColor, so the
mark takes its color from the page. Check the font's license first (references/levers.md): Fontshare
and OFL faces allow outlines in a wordmark. Needs fonttools (and brotli for woff2).
"""

import argparse

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

p = argparse.ArgumentParser()
p.add_argument("font")
p.add_argument("word")
p.add_argument("--track", type=float, default=0.0)
p.add_argument("--cut")
p.add_argument("--out", default="wordmark.svg")
a = p.parse_args()

f = TTFont(a.font)
glyphs, cmap, upm = f.getGlyphSet(), f.getBestCmap(), f["head"].unitsPerEm
cap = getattr(f["OS/2"], "sCapHeight", 0) or int(upm * 0.7)
track = a.track * upm

x, paths = 0.0, []
for ch in a.word:
    name = cmap.get(ord(ch))
    if name is None:
        raise SystemExit(f"glyph missing for {ch!r}: pick a face that covers the name")
    pen = SVGPathPen(glyphs)
    glyphs[name].draw(TransformPen(pen, (1, 0, 0, -1, x, 0)))
    paths.append(pen.getCommands())
    x += glyphs[name].width + track
width = x - track

mask, use_mask = "", ""
if a.cut:
    v = [float(n) for n in a.cut.split(",")]
    cx, cy, cw, ch = v[0] * width, -v[1] * cap, v[2] * width, v[3] * cap
    skew = f' transform="skewY({v[4]})"' if len(v) > 4 else ""
    mask = (
        f'<defs><mask id="cut"><rect x="0" y="{-cap * 1.3:.0f}" width="{width:.0f}" height="{cap * 1.6:.0f}" fill="#fff"/>'
        f'<rect x="{cx:.0f}" y="{cy - ch:.0f}" width="{cw:.0f}" height="{ch:.0f}" fill="#000"{skew}/></mask></defs>'
    )
    use_mask = ' mask="url(#cut)"'

top, h = -cap * 1.15, cap * 1.4
svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 {top:.0f} {width:.0f} {h:.0f}">{mask}'
    f'<g fill="currentColor"{use_mask}>{"".join(f"<path d={chr(34)}{d}{chr(34)}/>" for d in paths)}</g></svg>'
)
open(a.out, "w").write(svg)
print(f"{a.out}: {len(svg)} bytes, {len(a.word)} glyphs, cap {cap}, upm {upm}")
