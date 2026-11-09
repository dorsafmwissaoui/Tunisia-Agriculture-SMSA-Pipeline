


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
df_combined = df_combined.fillna('Non spécificado')


# --- Dynamic Text Standardization & Localization Function ---
def dynamic_clean_and_translate(raw_text):
    text = str(raw_text).strip()
    text = text.replace("معتمدية", "").replace("ولاية", "").strip()
   
    region_rules = {
        "باجة": "Béja", "تبرسق": "Téboursouk", "قعفور": "Gaâfour",
        "جومين": "Joumine", "غزالة": "Ghezala", "العلا": "Al Ala",
        "قليبية": "Kélibia", "تستور": "Testour", "مجاز": "Medjez El Bab",
        "قبلاط": "Goubellat", "نفزة": "Nefza", "عمدون": "Amdoon", "تيبار": "Tibar"
    }
   
    for key, value in region_rules.items():
        if key in text:
            if key == "باجة" and ("جنوب" in text or "ج" in text): return "Béja Sud"
            elif key == "باجة" and ("شمال" in text or "ش" in text): return "Béja Nord"
            return value
    return text if text != "" else "Non spécifié"


df_combined["Zone d'intervention"] = df_combined["Zone d'intervention"].apply(dynamic_clean_and_translate)

# Save the finalized structured dataset
output_path = '../data_processed/tunisia_smsa_clean.csv'
df_combined.to_csv(output_path, index=False)
print(f"[SUCCESS] Clean pipeline completed. Target output saved to: {output_path}")

# --- ADVANCED EXPLORATORY DATA ANALYSIS (EDA) ---
print("\n>>> Running Advanced Exploratory Data Analysis (EDA)...")

top_regions = df_combined["Zone d'intervention"].value_counts().head(5)
capital_dist = df_combined.groupby("Zone d'intervention")['Capital (dinars)'].sum().sort_values(ascending=False).head(5)

# 1. Structural Correlation Insight
# Calculate Pearson correlation coefficient between Capital and Registered Members
correlation = df_combined['Capital (dinars)'].corr(df_combined["Nombre d'adhérents_x"])
print(f"Statistical Correlation between Capital and Members: {correlation:.4f}")

# 2. Financial Outliers Identification
# Identify companies with massive capital that skew the industrial average
q1 = df_combined['Capital (dinars)'].quantile(0.25)
q3 = df_combined['Capital (dinars)'].quantile(0.75)
iqr = q3 - q1
upper_bound = q3 + (1.5 * iqr)
outliers_count = len(df_combined[df_combined['Capital (dinars)'] > upper_bound])
print(f"Identified {outliers_count} financially dominant companies (Outliers) exceeding standard capital distributions.")

# --- ADVANCED PRESENTATION REPORTING VISUALIZATIONS ---
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

# Chart 3: Correlation Matrix Heatmap (New Advanced Plot)
plt.figure(figsize=(6, 5))
corr_matrix = df_combined[['Capital (dinars)', "Nombre d'adhérents_x"]].corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5)
plt.title("Correlation Matrix: Capital vs Members", fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('../notebooks/correlation_heatmap.png', dpi=300)
plt.close()

# Chart 4: Capital Distribution Boxplot (New Advanced Plot for Outliers)
plt.figure(figsize=(8, 4))
sns.boxplot(x=df_combined['Capital (dinars)'], color="seagreen")
plt.title("Financial Capital Distribution & Outliers Profile", fontsize=12, fontweight='bold')
plt.xlabel("Capital in Dinars")
plt.tight_layout()
plt.savefig('../notebooks/capital_outliers_boxplot.png', dpi=300)
plt.close()

print("[SUCCESS] Advanced EDA charts generated and stored in 'notebooks/' directory.")


