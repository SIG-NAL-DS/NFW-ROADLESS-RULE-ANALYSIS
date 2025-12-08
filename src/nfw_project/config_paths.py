# src/nfw_project/config_paths.py

"""
Central configuration for paths and directory structure.

This file is meant to be *templated*:
- Core directory structure is generic and repo-relative.
- Project-specific datasets should be added in the section marked
  "PROJECT-SPECIFIC DATASETS" by this project's maintainers.
"""

from pathlib import Path
import os

# ---------------------------------------------------------------------------
# Core locations (repo + pipeline folders)
# ---------------------------------------------------------------------------

# This file lives at: <repo>/src/nfw_project/config_paths.py
# parents[0] = .../src/nfw_project
# parents[1] = .../src
# parents[2] = .../<repo-root>
PROJECT_ROOT: Path = Path(__file__).resolve().parents[2]

# Default data root is <repo>/data; can be overridden by NFW_DATA_ROOT
DATA_ROOT: Path = Path(
    os.environ.get("NFW_DATA_ROOT", PROJECT_ROOT / "data")
).resolve()

# Main pipeline folders
REQUIREMENTS_DIR: Path   = PROJECT_ROOT / "01-requirements"
DATA_LOADING_DIR: Path   = PROJECT_ROOT / "02-data-loading"
PREPROCESSING_DIR: Path  = PROJECT_ROOT / "03-preprocessing"
ANALYSIS_DIR: Path       = PROJECT_ROOT / "04-analysis"   # or 04-models if you prefer
OUTPUTS_DIR: Path        = PROJECT_ROOT / "05-outputs"


# ---------------------------------------------------------------------------
# Data subdirectories (generic)
# ---------------------------------------------------------------------------

# Suggested internal structure within DATA_ROOT:
# data/
#   raw/        # raw inputs, as obtained from source
#   interim/    # intermediate artifacts (cleaned, reprojected, etc.)
#   processed/  # ready-for-analysis datasets
RAW_DIR: Path       = DATA_ROOT / "raw"
INTERIM_DIR: Path   = DATA_ROOT / "interim"
PROCESSED_DIR: Path = DATA_ROOT / "processed"


# You can further subdivide these as needed, for example:
RAW_RASTERS_DIR: Path   = RAW_DIR / "rasters"
RAW_VECTORS_DIR: Path   = RAW_DIR / "vectors"
RAW_METADATA_DIR: Path  = RAW_DIR / "metadata"

# Example mid-pipeline structure (optional, adjust as needed)
PROCESSED_RASTERS_DIR: Path = PROCESSED_DIR / "rasters"
PROCESSED_TABLES_DIR: Path  = PROCESSED_DIR / "tables"


# ---------------------------------------------------------------------------
# Outputs subdirectories (generic)
# ---------------------------------------------------------------------------

# Where analysis outputs should go
MODEL_OUTPUTS_DIR: Path   = OUTPUTS_DIR / "models"
FIGURES_OUTPUT_DIR: Path  = OUTPUTS_DIR / "figures"
TABLES_OUTPUT_DIR: Path   = OUTPUTS_DIR / "tables"
LOGS_OUTPUT_DIR: Path     = OUTPUTS_DIR / "logs"


# ---------------------------------------------------------------------------
# PROJECT-SPECIFIC DATASETS (TO BE CUSTOMIZED)
# ---------------------------------------------------------------------------

"""
Add project-specific file and directory constants here.

For example:

    # Study boundary, as delivered in raw data:
    STUDY_BOUNDARY_PATH: Path = RAW_VECTORS_DIR / "study_boundary.shp"

    # Example: raw raster inputs
    LANDCOVER_2020_RASTER: Path = RAW_RASTERS_DIR / "landcover_2020.tif"
    ELEVATION_RASTER: Path      = RAW_RASTERS_DIR / "dem_30m.tif"

    # Example: processed dataset ready for modeling
    TRAINING_FEATURES_PARQUET: Path = PROCESSED_TABLES_DIR / "training_features.parquet"

Keep the names descriptive and UPPER_SNAKE_CASE. add them to __all__ so tab-complete works nicely.
"""

NFS_ROADS_SHP: Path = RAW_DIR / "National_Forest_System_Roads_(Feature_Layer)" / "National_Forest_System_Roads_(Feature_Layer).shp"
NFS_ROADS_GEOJSON: Path = RAW_DIR / "National_Forest_System_Roads_(Feature_Layer).geojson"
ROADLESS_AREA: Path = RAW_DIR /  "S_USA.RoadlessArea_2001" / 'S_USA.RoadlessArea_2001.shp'
USFS_FOREST_ADMIN_BOUNDARY: Path = RAW_DIR /  "Forest_Administrative_Boundaries_(Feature_Layer)" / 'Forest_Administrative_Boundaries_(Feature_Layer).shp'

USFS_GPKG: Path = INTERIM_DIR / "USFS.gpkg"

US_STATES: Path = RAW_DIR /  "tl_2025_us_state" / 'tl_2025_us_state.shp'
TIGERLINE_ALL_ROADS: Path = RAW_DIR / "Tiger_Line_All_Roads.parquet"
TIGERLINE_GPKG: Path = INTERIM_DIR / "TIGERLINE.gpkg"

# Roadless / roads analysis output
ROADLESS_ANALYSIS_GPKG: Path = PROCESSED_DIR / "Roadless_Roads_Analysis.gpkg"

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def ensure_output_dirs() -> None:
    """
    Create standard output directories if they don't exist.

    Safe to call multiple times.
    """
    for d in [
        OUTPUTS_DIR,
        MODEL_OUTPUTS_DIR,
        FIGURES_OUTPUT_DIR,
        TABLES_OUTPUT_DIR,
        LOGS_OUTPUT_DIR,
    ]:
        d.mkdir(parents=True, exist_ok=True)


__all__ = [
    # core
    "PROJECT_ROOT",
    "DATA_ROOT",
    "REQUIREMENTS_DIR",
    "DATA_LOADING_DIR",
    "PREPROCESSING_DIR",
    "ANALYSIS_DIR",
    "OUTPUTS_DIR",
    # data dirs
    "RAW_DIR",
    "INTERIM_DIR",
    "PROCESSED_DIR",
    "RAW_RASTERS_DIR",
    "RAW_VECTORS_DIR",
    "RAW_METADATA_DIR",
    "PROCESSED_RASTERS_DIR",
    "PROCESSED_TABLES_DIR",
    # outputs
    "MODEL_OUTPUTS_DIR",
    "FIGURES_OUTPUT_DIR",
    "TABLES_OUTPUT_DIR",
    "LOGS_OUTPUT_DIR",
    # helpers
    "ensure_output_dirs",
    # (PROJECT-SPECIFIC DATASETS will be added here as you define them)
    "NFS_ROADS_SHP",
    "USFS_GPKG",
    "TIGERLINE_GPKG",
    "TIGERLINE_ALL_ROADS",
    "ROADLESS_ANALYSIS_GPKG"
]
