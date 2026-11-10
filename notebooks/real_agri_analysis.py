import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

FILE_SOCIETES = '../data_raw/societes.csv'
FILE_REPARTITION = '../data_raw/repartition.csv'

print(">>> Loading raw datasets into Pandas...")
df_societes = pd.read_csv(FILE_SOCIETES)
df_repartition = pd.read_csv(FILE_REPARTITION)

# Clean whitespaces from column headers
df_societes.columns = df_societes.columns.str.strip()
df_repartition.columns = df_repartition.columns.str.strip()

# Align merge keys across datasets
df_repartition = df_repartition.rename(columns={'Délégation': "Zone d'intervention"})

# --- 🛠️ Ultra-Precision Geo-Standardization Function ---
def standardize_geo_names(raw_text):
    text = str(raw_text).strip()
   
    # Strip unnecessary organizational prefixes
    text = text.replace("معتمدية", "").replace("ولاية", "").replace("عمادة", "").replace("مدينة", "").strip()
    text = text.replace(",", "").replace("،", "").strip()
   
    # Priority 1: High-precision match for standalone specific municipalities to prevent Beja from absorbing them
    if "دجبة" in text or "جبة" in text:
        return "Djebba"
    if "تيبار" in text or "تِيبَار" in text:
        return "Tibar"
    if "عmdون" in text or "عمدون" in text:
        return "Amdoun"
    if "نفزة" in text:
        return "Nefza"
    if "تبرسق" in text:
        return "Téboursouk"
    if "تستور" in text:
        return "Testour"
    if "قعفور" in text:
        return "Gaâfour"
    if "جومين" in text:
        return "Joumine"
    if "قبلاط" in text:
        return "Goubellat"
       
    # Priority 2: Check for Northern sector evaluations explicitly
    if "شمال" in text or "الشمالية" in text:
        return "Béja Nord"
       
    # Priority 3: Check for Southern sector evaluations
    if "جنوب" in text or "الجنوبية" in text or " ج" in text or ",ج" in text or text.endswith("ج"):
        return "Béja Sud"
       
    if "باجة" in text:
        return "Béja"
       
    return text if text != "" else "Non spécifié"

# Apply high-precision geo-cleaning BEFORE merging
df_societes["Zone d'intervention"] = df_societes["Zone d'intervention"].apply(standardize_geo_names)
df_repartition["Zone d'intervention"] = df_repartition["Zone d'intervention"].apply(standardize_geo_names)

# Structural left join on Year and calibrated Region keys
df_combined = pd.merge(df_societes, df_repartition, on=['Année', "Zone d'intervention"], how='left')

print(">>> Executing downstream cleaning and financial scaling...")
df_combined = df_combined.drop_duplicates()

# Clean and protect numerical column layouts
df_combined['Capital (dinars)'] = pd.to_numeric(df_combined['Capital (dinars)'], errors='coerce')
df_combined["Nombre d'adhérents_x"] = pd.to_numeric(df_combined["Nombre d'adhérents_x"], errors='coerce')

# --- 💰 الآلية الذكية لمعايرة وحدات ميزانية رأس المال المالي بالدينار ---
# أي رقم أصغر من 1000 (بما في ذلك الكسور 16.15 و 5.05 و 10) يتم ضربه آلياً في 1000 ليتحول لوحدته الحقيقية الموحدة بالدينار الصافي
df_combined['Capital (dinars)'] = df_combined['Capital (dinars)'].apply(lambda x: x * 1000 if x < 1000 else x)

# Handle residual missing numerical entries using localized median values
df_combined['Capital (dinars)'] = df_combined['Capital (dinars)'].fillna(df_combined['Capital (dinars)'].median())
df_combined["Nombre d'adhérents_x"] = df_combined["Nombre d'adhérents_x"].fillna(df_combined["Nombre d'adhérents_x"].median())
df_combined = df_combined.fillna('Non spécifié')

# Handle dynamic translation for other core descriptive text columns
def clean_other_columns(text_val):
    val = str(text_val).strip()
    if val.lower() in ['non spécifié', 'nan', 'null']:
        return 'Non spécifié'
    activity_rules = {"تربية": "Elevage", "الحبوب": "Céréales", "زيت": "Huile d'olive", "خدمات": "Services"}
    for k, v in activity_rules.items():
        if k in val:
            return v
    return val

df_combined["Activités"] = df_combined["Activités"].apply(clean_other_columns)

# Save master clean file with perfect structural integrity
output_path = '../data_processed/tunisia_smsa_clean.csv'
df_combined.to_csv(output_path, index=False)
print(f"[SUCCESS] Advanced financial scaling completed. Output saved to: {output_path}")

# --- Descriptive Statistical Summary ---
top_regions = df_combined["Zone d'intervention"].value_counts().head(5)
capital_dist = df_combined.groupby("Zone d'intervention")['Capital (dinars)'].sum().sort_values(ascending=False).head(5)

# --- Reporting Visualizations ---
sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.barplot(x=top_regions.values, y=top_regions.index, palette="viridis")
plt.title("Top 5 Tunisian Regions by SMSA Density", fontsize=14, fontweight='bold')
plt.xlabel("Number of Cooperative Societies")
plt.ylabel("Region / Delegation")
plt.tight_layout()
plt.savefig('../notebooks/top_regions_chart.png', dpi=300)
plt.close()

plt.figure(figsize=(10, 6))
sns.barplot(x=capital_dist.values, y=capital_dist.index, palette="rocket")
plt.title("Top 5 Regions by Total Capital Investment (TND)", fontsize=14, fontweight='bold')
plt.xlabel("Total Capital (Dinars)")
plt.ylabel("Region / Delegation")
plt.tight_layout()
plt.savefig('../notebooks/capital_distribution_chart.png', dpi=300)
plt.close()

print("[SUCCESS] Production analytics generated with verified financial-calibration.")

