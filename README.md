# Spatial Informatics Group - Natural Assets Laboratory
# NFW Roadless Rule Analysis

This repository contains the code, data structure, and reproducible workflows used for the NFW analysis. It supports a complete pipeline from raw data ingestion through preprocessing, analysis, and final outputs.

## Purpose

This repository is designed to provide:

- A clear, reproducible workflow for geospatial and tabular data processing  
- A well-structured environment for collaborative development  
- A self-contained, installable Python package (`nfw_project`) for shared utilities  
- A directory layout suitable for long-term maintenance and delivery to project partners  

All notebooks and scripts follow a consistent organizational pattern to keep the analysis transparent and easy to run.

---

## Repository Structure

01-requirements/ ← environment.yml, requirements.txt
02-data-loading/ ← raw dataset loading and verification
03-preprocessing/ ← cleaning, masking, reprojection, harmonization
04-analysis/ ← analysis, modeling, visualization
05-outputs/ ← generated figures, tables, models

data/ ← user-provided datasets (not tracked in git)
* raw/ ← raw inputs as obtained
* interim/ ← intermediate artifacts
* processed/ ← analysis-ready datasets

src/
* nfw_project/ ← project package: config_paths, utilities

HOWTO_run.md ← setup instructions and execution guide

All code in this repo uses importable utilities from the `src/nfw_project/` package.

---

## Getting Started

To set up the environment and run the workflow:

➡ **See: [`HOWTO_run.md`](01-requirements\HOWTO_run.md)**  
This includes:

- Environment setup  
- Package installation (`pip install -e .`)  
- Required data directory layout  
- Execution order  
- Troubleshooting  

---

## Results

Final outputs — including figures, tables, and any derived layers — are stored under:

05-outputs/
The specific deliverables and findings will depend on the workflows executed in `04-analysis/`.

---

## Contribution & Collaboration

This repository is structured to support collaboration across multiple contributors.  
If adding new preprocessing or analysis steps:

- Place notebooks/scripts in the appropriate folder (`02`, `03`, or `04`)
- Add any new required constants to `config_paths.py`
- Follow the existing naming and documentation patterns

---