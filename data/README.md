# VeriDoc AI — Datasets

This directory manages all raw, interim, processed, and external datasets, as well as their versioned metadata manifests.

## 📂 Directory Layout

*   **`raw/`** *(Gitignored)*: Original, unmodified datasets as downloaded or imported from data sources.
*   **`interim/`** *(Gitignored)*: Intermediate stages of datasets currently being cleaned, transformed, or augmented.
*   **`processed/`** *(Gitignored)*: Canonical, training-ready datasets formatted specifically for ingestion by model training pipelines.
*   **`external/`** *(Gitignored)*: Publicly available datasets, vocabulary mappings, or other external reference files.
*   **`manifests/`** *(Versioned)*: Metadata descriptions, split counts, source information, and schemas for each dataset.

## ⚙️ Git Version Control Rules

To prevent repository bloat and ensure fast cloning:
1.  All data files inside `raw/`, `interim/`, `processed/`, and `external/` are **excluded** from Git history via `.gitignore`.
2.  The directory structures are preserved via `.gitkeep` placeholders.
3.  Metadata configurations, schemas, and descriptions are stored in `manifests/` and **tracked** under Git.
