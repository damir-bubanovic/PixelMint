from pathlib import Path
import cairosvg

# Config
TEMPLATE_PATH = Path(__file__).resolve().parents[1] / "assets" / "template.svg"
OUTPUT_DIR = Path(__file__).resolve().parents[1] / "out"
COUNT = 10            # total images
START = 1             # starting number
ZERO_PAD = 4          # 0001..10; set 0 to disable
PREFIX = "image_"     # filename prefix
DPI = 96              # PNG DPI

def main():
    svg_template = TEMPLATE_PATH.read_text(encoding="utf-8")
    if "{{NUMBER}}" not in svg_template:
        raise ValueError("Missing {{NUMBER}} in template.svg")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for n in range(START, START + COUNT):
        num = str(n).zfill(ZERO_PAD) if ZERO_PAD > 0 else str(n)
        svg = svg_template.replace("{{NUMBER}}", num)
        out_path = OUTPUT_DIR / f"{PREFIX}{num}.png"
        cairosvg.svg2png(bytestring=svg.encode("utf-8"),
                         write_to=str(out_path),
                         dpi=DPI)

    print(f"Done: {COUNT} PNGs in {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
