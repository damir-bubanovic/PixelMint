from pathlib import Path
import cairosvg

tpl = Path(__file__).resolve().parents[1] / "assets" / "template.svg"
out = Path(__file__).resolve().parents[1] / "out" / "template_test.png"
svg = tpl.read_text(encoding="utf-8")
svg = svg.replace("{{NUMBER}}", "1234")
out.parent.mkdir(parents=True, exist_ok=True)
cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=str(out), dpi=96)
print("OK ->", out)