# src/smoke_test.py
from pathlib import Path
import cairosvg

print("CairoSVG version:", cairosvg.__version__)

# minimal inline SVG render test
OUT = Path(__file__).resolve().parents[1] / "out" / "smoke_test.png"
OUT.parent.mkdir(parents=True, exist_ok=True)

svg = """<svg xmlns="http://www.w3.org/2000/svg" width="200" height="120">
  <rect width="100%" height="100%" fill="#222"/>
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle"
        font-family="DejaVu Sans" font-size="24" fill="#fff">OK</text>
</svg>"""

cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=str(OUT), dpi=96)
print("Rendered:", OUT)