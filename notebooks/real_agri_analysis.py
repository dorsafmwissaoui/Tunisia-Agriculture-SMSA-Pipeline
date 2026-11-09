


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

FILE_SOCIETES = '../data_raw/societes.csv'
FILE_REPARTITION = '../data_raw/repartition.csv'

print(">>> Loading and merging datasets...")
df_societes = pd.read_csv(FILE_SOCIETES)
df_repartition = pd.read_csv(FILE_REPARTITION)

# Clean column headers
df_societes.columns = df_societes.columns.str.strip()
df_repartition.columns = df_repartition.columns.str.strip()

# Align merge keys across datasets
df_repartition = df_repartition.rename(columns={'Délégation': "Zone d'intervention"})

# Structural left join on Year and Region
df_combined = pd.merge(df_societes, df_repartition, on=['Année', "Zone d'intervention"], how='left')

print(">>> Executing data cleaning pipeline...")
df_combined = df_combined.drop_duplicates()

# Standardize data types for numerical metrics
df_combined['Capital (dinars)'] = pd.to_numeric(df_combined['Capital (dinars)'], errors='coerce')
df_combined["Nombre d'adhérents_x"] = pd.to_numeric(df_combined["Nombre d'adhérents_x"], errors='coerce')

# Handle missing numerical entries using localized median values
df_combined['Capital (dinars)'] = df_combined['Capital (dinars)'].fillna(df_combined['Capital (dinars)'].median())
df_combined["Nombre d'adhérents_x"] = df_combined["Nombre d'adhérents_x"].fillna(df_combined["Nombre d'adhérents_x"].median())
df_combined = df_combined.fillna('Non spécifié')


# --- Dynamic Text Standardization & Localization Function ---
def dynamic_clean_and_translate(raw_text):
    text = str(raw_text).strip()
   
    # Strip redundant categorical prefixes
    text = text.replace("معتمدية", "").replace("ولاية", "").strip()
   
    # Regional translation rules with partial substring matching
    region_rules = {
        "باجة": "Béja",
        "تبرسق": "Téboursouk",
        "قعفور": "Gaâfour",
        "جومين": "Joumine",
        "غزالة": "Ghezala",
        "العلا": "Al Ala",
        "قليبية": "Kélibia",
        "تستور": "Testour",
        "مجاز": "Medjez El Bab",
        "قبلاط": "Goubellat",
        "نفزة": "Nefza",
        "عمدون": "Amdoon",
        "تيبار": "Tibar" 
    }
   
    for key, value in region_rules.items():
        if key in text:
            # Handle localized text variations for Beja subdivisions
            if key == "باجة" and ("جنوب" in text or "ج" in text):
                return "Béja Sud"
            elif key == "باجة" and ("شمال" in text or "ش" in text):
                return "Béja Nord"
            return value
           
    return text if text != "" else "Non spécifié"


# Normalize text fields across the target alignment column
df_combined["Zone d'intervention"] = df_combined["Zone d'intervention"].apply(dynamic_clean_and_translate)

# Save the finalized structured dataset
output_path = '../data_processed/tunisia_smsa_clean.csv'
df_combined.to_csv(output_path, index=False)
print(f"[SUCCESS] Clean pipeline completed. Target output saved to: {output_path}")

# --- Descriptive Statistical Summary ---
print("\n>>> Extracting Key Strategic Insights:")
top_regions = df_combined["Zone d'intervention"].value_counts().head(5)
capital_dist = df_combined.groupby("Zone d'intervention")['Capital (dinars)'].sum().sort_values(ascending=False).head(5)

print("\n1. Top 5 Operational Hubs by SMSA Volume:")
print(top_regions)

print("\n2. Total Financial Capital Investment Profile (Top 5 TND):")
print(capital_dist)

# --- Reporting Visualizations ---
print("\n>>> Building presentation chart layers...")
sns.set_theme(style="whitegrid")

# Chart 1: Cooperative Concentration Plot
plt.figure(figsize=(10, 6))
sns.barplot(x=top_regions.values, y=top_regions.index, palette="viridis")
plt.title("Top 5 Tunisian Regions by SMSA Density", fontsize=14, fontweight='bold')
plt.xlabel("Number of Cooperative Societies")
plt.ylabel("Region / Delegation")
plt.tight_layout()
plt.savefig('../notebooks/top_regions_chart.png', dpi=300)
plt.close()

# Chart 2: Capital Deployment Profile Plot
plt.figure(figsize=(10, 6))
sns.barplot(x=capital_dist.values, y=capital_dist.index, palette="rocket")
plt.title("Top 5 Regions by Total Capital Investment (TND)", fontsize=14, fontweight='bold')
plt.xlabel("Total Capital (Dinars)")
plt.ylabel("Region / Delegation")
plt.tight_layout()
plt.savefig('../notebooks/capital_distribution_chart.png', dpi=300)
plt.close()

print("[SUCCESS] All analysis outputs updated and stabilized.")

