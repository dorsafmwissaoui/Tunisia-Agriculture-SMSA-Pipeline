


# Tunisia Agricultural Societies (SMSA) Data & Insights Pipeline

A comprehensive data engineering and analysis project evaluating the structural, financial, and geographical distribution of Agricultural Mutual Service Societies (SMSA) in Tunisia. This pipeline consolidates fragmented regional administrative records to assist policymakers (e.g., Ministry of Agriculture) and institutional investors in identifying cooperative density and resource allocation gaps.

## Project Structure
* `data_raw/`: Input datasets converted to CSV format (`societes.csv`, `repartition.csv`).
* `data_processed/`: Final unified master dataset (`tunisia_smsa_clean.csv`).
* `notebooks/`: Production-ready Python scripts and generated analytical charts.

## Core Issues Addressed & Cleaning Pipeline
1. **Geographical Data Fragmentation:** Resolved naming mismatches between local datasets by aligning localized key dimensions (`Délégation` merged into `Zone d'intervention`).
2. **Data Type Constraints:** Transformed financial capital and membership statistics from text types to structured float metrics, filtering out non-numeric anomalies.
3. **Missing Value Resolution:** Applied local median imputation for numeric attributes to safeguard statistical consistency without skewing distribution metrics.

## Strategic Insights Extracted
The pipeline evaluates four core operational dimensions of the Tunisian agricultural sector:
* **Geographical Density Map:** Pinpoints regional hotspots where farmers are highly centralized into active cooperatives versus underserved areas.
* **Capital Distribution Metrics:** Aggregates financial capacity across zones to spotlight areas lacking investment or needing economic subsidies.
* **Cooperative Engagement Analysis:** Measures structural membership volume (`Nombre d'adhérents`) to assess farmer integration success against market intermediaries.
* **Operational Diversification:** Catalogs primary crop, livestock, and processing activities to highlight sector vulnerability to climate or market shocks.

## Generated Charts (Available in `notebooks/`)
1. `top_regions_chart.png`: Visual distribution of active agricultural societies.
2. `capital_distribution_chart.png`: Bar plot comparison of total capital funding across leading delegations.

## How to Execute
Make sure you have `pandas`, `matplotlib`, and `seaborn` installed, then run:
```bash
cd notebooks
python3 real_agri_analysis.py
```
