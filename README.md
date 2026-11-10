
# Tunisia Agricultural Societies (SMSA) Data Engineering & Advanced EDA

A comprehensive data engineering and advanced exploratory data analysis (EDA) project evaluating the structural, financial, and geographical distribution of Agricultural Mutual Service Societies (SMSA) in Tunisia. This pipeline consolidates fragmented regional administrative records to assist policymakers (e.g., Ministry of Agriculture) and institutional investors in identifying cooperative density and resource allocation gaps.

## Project Structure
* `data_raw/`: Input datasets converted to CSV format (`societes.csv`, `repartition.csv`).
* `data_processed/`: Final unified master dataset (`tunisia_smsa_clean.csv`).
* `notebooks/`: Production-ready Python scripts and generated analytical charts.

## Core Issues Addressed & Cleaning Pipeline
1. **Geographical Data Fragmentation:** Resolved naming mismatches between local datasets by aligning localized key dimensions (`Délégation` merged into `Zone d'intervention`).
2. **Text Standardization:** Applied dynamic substring rules to clean structural human-entry anomalies (e.g., merging multiple text variations of `Béja Sud`).
3. **Data Type Constraints:** Transformed financial capital and membership statistics from text types to structured float metrics, filtering out non-numeric anomalies.

## Advanced Exploratory Data Analysis (EDA) Insights
* **Geographical Density Map:** Pinpoints regional hotspots where farmers are highly centralized into active cooperatives versus underserved areas.
* **Financial Outliers Profile:** Statistical boxplot isolation identified a small concentration of financially dominant societies holding a disproportionate share of the industry's total capital.
* **Capital-to-Membership Correlation:** Heatmap analysis evaluated the statistical link between cooperative capital capacity and membership volumes, measuring whether well-funded hubs attract higher farmer integration.

## Data-Driven Strategic Recommendations
1. **Target Subsidies to Under-Funded Hubs:** Direct financial credit and international development grants toward regions identified with zero or critically low capital concentration to prevent local farmer exploitation by intermediaries.
2. **Standardize National Administrative Registers:** Implement unified regional drop-down forms across government registers to eliminate structural text entry variances, preventing information silos.

## Generated Analytical Charts (Available in `notebooks/`)
1. `top_regions_chart.png`: Visual distribution of active agricultural societies.
2. `capital_distribution_chart.png`: Bar plot comparison of total capital funding.
3. `correlation_heatmap.png`: Statistical matrix checking financial-to-membership correlation.
4. `capital_outliers_boxplot.png`: Distribution curve mapping financial outliers.

## How to Execute
Make sure you have `pandas`, `matplotlib`, and `seaborn` installed, then run:
```bash
cd notebooks
python3 real_agri_analysis.py
```



