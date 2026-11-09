


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

FILE_SOCIETES = '../data_raw/societes.csv'
FILE_REPARTITION = '../data_raw/repartition.csv'

print(">>> Loading and merging datasets...")
df_societes = pd.read_csv(FILE_SOCIETES)
df_repartition = pd.read_csv(FILE_REPARTITION)

# Clean whitespaces in column names
df_societes.columns = df_societes.columns.str.strip()
df_repartition.columns = df_repartition.columns.str.strip()

# Standardize region column name before merge
df_repartition = df_repartition.rename(columns={'Délégation': "Zone d'intervention"})

# Perform structural left join on Year and Region
df_combined = pd.merge(df_societes, df_repartition, on=['Année', "Zone d'intervention"], how='left')

# Data Cleaning Pipeline
print(">>> Cleaning data...")
df_combined = df_combined.drop_duplicates()

# Convert numeric columns, forcing errors to NaN to clean text anomalies
df_combined['Capital (dinars)'] = pd.to_numeric(df_combined['Capital (dinars)'], errors='coerce')
df_combined["Nombre d'adhérents_x"] = pd.to_numeric(df_combined["Nombre d'adhérents_x"], errors='coerce')

# Fill missing values
df_combined['Capital (dinars)'] = df_combined['Capital (dinars)'].fillna(df_combined['Capital (dinars)'].median())
df_combined["Nombre d'adhérents_x"] = df_combined["Nombre d'adhérents_x"].fillna(df_combined["Nombre d'adhérents_x"].median())
df_combined = df_combined.fillna('Non spécifié')

# Export clean master dataset
output_path = '../data_processed/tunisia_smsa_clean.csv'
df_combined.to_csv(output_path, index=False)
print(f"[SUCCESS] Cleaned data saved to: {output_path}")

# --- Comprehensive Analysis Insights ---
print("\n>>> Generating Strategic Insights for Ministry & Investors:")

# 1. Geographic Density Insight
print("\n1. Top 5 Regions by SMSA Concentration:")
top_regions = df_combined["Zone d'intervention"].value_counts().head(5)
print(top_regions)

# 2. Financial Insight: Capital Distribution
print("\n2. Total Capital Investment by Region (Top 5):")
capital_dist = df_combined.groupby("Zone d'intervention")['Capital (dinars)'].sum().sort_values(ascending=False).head(5)
print(capital_dist)

# 3. Structural Insight: Membership Volume (Total Adherents)
print("\n3. Total Registered Members (Adherents) by Region (Top 5):")
adherents_dist = df_combined.groupby("Zone d'intervention")["Nombre d'adhérents_x"].sum().sort_values(ascending=False).head(5)
print(adherents_dist)

# 4. Operational Insight: Top Agriculture Activities
print("\n4. Most Common Agricultural Activities:")
top_activities = df_combined['Activités'].value_counts().head(5)
print(top_activities)

# --- Visualization Section ---
print("\n>>> Generating Charts...")
sns.set_theme(style="whitegrid")

# Chart 1: Top Regions by SMSA Count
plt.figure(figsize=(10, 6))
sns.barplot(x=top_regions.values, y=top_regions.index, palette="viridis")
plt.title("Top 5 Tunisian Regions by SMSA Density", fontsize=14)
plt.xlabel("Number of Societies")
plt.ylabel("Region / Delegation")
plt.tight_layout()
plt.savefig('../notebooks/top_regions_chart.png')
plt.close()

# Chart 2: Capital Investment distribution
plt.figure(figsize=(10, 6))
sns.barplot(x=capital_dist.values, y=capital_dist.index, palette="rocket")
plt.title("Top 5 Regions by Total Capital Investment (TND)", fontsize=14)
plt.xlabel("Total Capital in Dinars")
plt.ylabel("Region / Delegation")
plt.tight_layout()
plt.savefig('../notebooks/capital_distribution_chart.png')
plt.close()

print("[SUCCESS] Charts generated and saved in 'notebooks/' folder.")

