from pathlib import Path
import os

# This file lives in repo-root/src/nfw_project/config_paths.py
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Default data root is inside the repo; can be overridden by env var
DATA_ROOT = Path(os.getenv("NFW_DATA_ROOT", PROJECT_ROOT / "data"))

# Example logical structure
BOUNDARY_DIR      = DATA_ROOT / "study_boundary"
RAW_DIR           = DATA_ROOT / "raw"
PROCESSED_DIR     = DATA_ROOT / "processed"
FEATURES_DIR      = DATA_ROOT / "features"
OUTPUTS_DIR       = PROJECT_ROOT / "05-outputs"

# Specific files
STUDY_BOUNDARY_PATH = BOUNDARY_DIR / "study_boundary.shp"

# Examples
""" HANSEN_TREECOVER_FILEPATH = [
    RAW_DIR / "hansen" / "treecover2000.tif"
]

HANSEN_LOSSYEAR_FILEPATHS = [
    RAW_DIR / "hansen" / "lossyear.tif"
]

PRECIPITATION_FILEPATH = RAW_DIR / "chirps" / "average_annual_precipitation.tif"
 """
# ...and so on, but now all relative to DATA_ROOT/PROJECT_ROOT
