# HOWTO Run This Project

This document provides instructions for setting up the environment, organizing data, and running the notebooks and scripts in this repository. All users should read this first before executing any part of the workflow.

---

## 1. Create and Activate the Environment

The environment specifications are stored in `01-requirements/`.

If you're using Conda:

```bash
conda env create -f 01-requirements/environment.yml
conda activate nfw-env
```

If using `pip`, install dependencies listed in `01-requirements/requirements.txt` into your own environment.

## 2. Install the Local Project Package
To enable imports such as:

```python
from nfw_project import config_paths as cfg
```
you must install this repository as a local, editable Python package.


From the repo root:

```bash
pip install -e .
```

This does not publish anything externally — it simply registers the local `src/nfw_project/` directory so that imports work across all notebooks and scripts.

## 3. Data Directory Structure
All project data is expected to live under:

```
data/
  raw/
  interim/
  processed/
```

`raw/`

Direct inputs as obtained from the source.
Examples:

* Earth Engine exports

* Downloads from an external provider

* Shapefiles, rasters, tables provided by partners

* Unmodified third-party datasets

All raw data should remain unchanged.

`interim/`
Intermediate artifacts generated during preprocessing.
Examples:

* Reprojected inputs

* Cleaned/standardized variants

* Masked rasters

* Partial feature tables

These files are produced automatically by scripts/notebooks.

`processed/`
Analysis-ready datasets created from interim/.
Examples:

* Final cleaned rasters

* Harmonized layers

* Modeling feature sets

* Tables ready for analysis in 04-analysis/

*Subfolders*
Within these folders you may see or create:

```
rasters/
vectors/
tables/
metadata/
```

These are optional organizational aids and can be expanded as needed.

## 4. Running the Workflow
The project follows a structured pipeline aligned with the directory layout.

`02-data-loading/`
Load initial raw datasets and verify that paths in `config_paths.py` match your local `data/raw/`.

`03-preprocessing/`
Cleaning, clipping, masking, reprojecting, conversions, building intermediate layers, etc.
Outputs generally go to:

* `data/interim/`

* `data/processed/`

`04-analysis/`
Notebooks and scripts for:

* Exploratory analysis

* Modeling and prediction

* Generating summary tables

* Producing figures and maps

Outputs are typically saved to:

* 05-outputs/figures/

* 05-outputs/tables/

* 05-outputs/models/

# 5. Using config_paths.py in Notebooks
Each notebook should import the project’s path configuration at the top:

```python
from nfw_project import config_paths as cfg

cfg.DATA_ROOT
cfg.RAW_DIR
cfg.INTERIM_DIR
cfg.PROCESSED_DIR
cfg.ensure_output_dirs()
```

Project-specific constants will appear here as they are added.

# 6. Changing the Data Location (Optional)
If your data lives outside the repository (e.g., external drive, network share), set the NFW_DATA_ROOT environment variable before running Python:

*macOS/Linux:*
```bash
export NFW_DATA_ROOT="/path/to/data"
```
*Windows PowerShell:*
```powershell
$env:NFW_DATA_ROOT = "D:\nfw_data"
```

If not set, the project defaults to:

```bash
<repo-root>/data
```

## 7. Recommended Execution Order
1. Start in 02-data-loading/

2. Continue to 03-preprocessing/

3. Complete workflows in 04-analysis/

4. Review or export results from 05-outputs/

## 8. Troubleshooting
Imports failing?
Make sure you ran:

```bash
pip install -e .
```
Paths wrong or files missing?
Check the directory layout under `data/` and update/extend `config_paths.py` if needed.

Environment issues?
Recreate the environment:

```bash
conda env remove -n nfw-env
conda env create -f 01-requirements/environment.yml
```