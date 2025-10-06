# src/convert_svgs.py
import argparse
import sys
import pathlib
import cairosvg

Path = pathlib.Path
REPO_ROOT = Path(__file__).resolve().parents[1]  # project root (has assets/, out/)

def iter_svg_paths(items):
    seen = set()
    for it in items:
        p = Path(it)
        if not p.is_absolute():
            p = (REPO_ROOT / p) if not Path.cwd().samefile(REPO_ROOT) else (Path.cwd() / it)

        # glob patterns (evaluate relative to REPO_ROOT)
        if any(ch in p.name for ch in "*?[]"):
            for g in sorted(REPO_ROOT.glob(str(p.relative_to(REPO_ROOT)))):
                if g.suffix.lower() == ".svg" and g not in seen:
                    seen.add(g); yield g
        elif p.is_dir():
            for g in sorted(p.rglob("*.svg")):
                if g not in seen:
                    seen.add(g); yield g
        elif p.is_file() and p.suffix.lower() == ".svg":
            if p not in seen:
                seen.add(p); yield p

def resolve_outdir(outdir_arg: str) -> Path:
    p = Path(outdir_arg)
    return p if p.is_absolute() else (REPO_ROOT / p)

def to_png(svg_path: Path, outdir: Path) -> Path:
    outdir.mkdir(parents=True, exist_ok=True)
    return outdir / (svg_path.stem + ".png")

def main(argv=None):
    ap = argparse.ArgumentParser(description="Convert SVG files to PNG.")
    ap.add_argument("inputs", nargs="*", help="SVG files, directories, or globs. Default: assets/")
    ap.add_argument("--outdir", default="out", help="Output directory. Default: out")
    ap.add_argument("--dpi", type=int, default=96, help="Raster DPI. Default: 96")
    args = ap.parse_args(argv)

    inputs = args.inputs or [str(REPO_ROOT / "assets")]
    outdir = resolve_outdir(args.outdir)

    count = 0
    for svg_path in iter_svg_paths(inputs):
        png_path = to_png(svg_path, outdir)
        svg_text = svg_path.read_text(encoding="utf-8")
        cairosvg.svg2png(bytestring=svg_text.encode("utf-8"),
                         write_to=str(png_path),
                         dpi=args.dpi)
        print(f"{svg_path} -> {png_path}")
        count += 1

    if count == 0:
        print("No SVGs found.", file=sys.stderr); sys.exit(1)
    print(f"Done: {count} PNG files -> {outdir}")

if __name__ == "__main__":
    main()
