## Usage

```bash
# Activate virtual environment
source .venv/bin/activate

# Default: convert all SVGs in assets/ to out/
python -m src.convert_svgs

# Convert a specific folder
python -m src.convert_svgs assets/icons

# Convert a glob (quote the pattern)
python -m src.convert_svgs "assets/*.svg"

# Convert multiple sources (folders, files, globs)
python -m src.convert_svgs assets logos/*.svg other_dir/file.svg

# Choose a different output directory
python -m src.convert_svgs assets --outdir build_png

# Change raster DPI
python -m src.convert_svgs assets --dpi 144

# Show help
python -m src.convert_svgs -h
```

### OK