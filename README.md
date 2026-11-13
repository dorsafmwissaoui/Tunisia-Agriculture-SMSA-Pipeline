


# تحليل بيانات الشركات التعاونية الفلاحية في تونس (SMSA)
# Tunisian Agricultural Cooperatives (SMSA) Data Analysis

🔗 [**لوحة التحكم التفاعلية / Live Interactive Dashboard**](https://docs.google.com/spreadsheets/d/1xl6FTgRiQ785RDBSkLr2IM2qdCVR6BdTQiTUdM312Bw/edit?usp=sharing)

---

##  ملخص المشروع

### فكرة المشروع
قمت في هذا المشروع بتنظيف وتحليل بيانات الشركات التعاونية الفلاحية في تونس (بيانات وزارة الفلاحة). الهدف الأساسي هو تحويل الجداول الخام غير الموحدة إلى بيانات نظيفة، واستخراج مؤشرات تساعد في فهم توزيع رؤوس الأموال والأنشطة الفلاحية، مع بناء لوحة تحكم (Dashboard) تفاعلية لمتابعة الأرقام بسهولة.

### خطوات العمل وتنظيف البيانات (Python)
اعتمدت على مكتبة `Pandas` في بايثون لمعالجة المشاكل الموجودة في الملف الأصلي:
* **توحيد أسماء المناطق:** كان هناك اختلاف كبير في كتابة نفس المعتمدية (مثلاً: "باجة ج"، "معتمدية باجة الجنوبية"، "بالجنوب"). قمت بتوحيدها وترجمتها إلى أسماء لاتينية قياسية (`Béja Nord`, `Béja Sud`, `Djebba`, `Tibar`...) لتسهيل التجميع والرسم.
* **تصحيح الوحدات المالية:** بعض القيم المالية كانت مسجلة بالآلاف المختصرة (مثل `10` أو `16.15` بدلاً من `10000` و `16150`)، فتم توحيدها لتكون جميعها بالدينار التونسي الكامل.
* **معالجة القيم المفقودة:** تعويض الخانات الفارغة في رأس المال باستخدام الوسيط (Median) الخاص بكل منطقة حتى لا تتأثر الحسابات بالقيم الشاذة.

### أبرز النتائج من التحليل
1. **العلاقة بين رأس المال وعدد المنخرطين:** معامل الارتباط (Pearson) طلع قريباً جداً من الصفر. هذا يعني أن حجم رأس مال الشركة ليس هو السبب الذي يجذب الفلاحين للانخراط، بل قرب الشركة جغرافياً وتوفر الخدمات اليومية هو العامل الأهم.
2. **الشركات ذات رؤوس الأموال الضخمة (Outliers):** باستخدام طريقة الـ IQR، لاحظت أن أغلب الشركات يتراوح رأس مالها بين 4,000 و 16,000 دينار، بينما توجد قلة قليلة تتجاوز 25,000 دينار وتؤثر على المتوسط العام.
3. **توزيع الأنشطة:** أغلب الشركات تتركز في قطاع الحبوب وتربية الماشية، مع وجود نقص واضح في شركات الخدمات الفلاحية واللوجستية.

---

## Project Summary

### Overview
This project focuses on cleaning, analyzing, and visualizing dataset records of Tunisian Agricultural Cooperative Societies (SMSA). Starting from messy raw administrative files, I built a Python script to clean the data and connected the output to an interactive Google Sheets dashboard to track capital distribution and activity shares across regions.

### Data Cleaning Pipeline (Python / Pandas)
The raw data required several preprocessing steps in `real_agri_analysis.py`:
* **Geo-Standardization:** Merged inconsistent Arabic text entries for the same delegations (e.g., variations of Béja Sud) into clean, standardized Latin names to prevent split groupings during analysis.
* **Unit Scaling:** Fixed inconsistent financial entries where some capital values were recorded in thousands (e.g., `16.15` instead of `16150`), scaling all entries uniformly to TND.
* **Handling Missing Data:** Imputed missing capital values using regional medians to avoid skewing the distribution.

### Key Findings
1. **Capital vs. Membership:** The Pearson correlation between a cooperative's capital and its number of members is nearly zero. Farmers join cooperatives based on location and available services rather than the company's financial size.
2. **Financial Outliers (IQR):** While most cooperatives operate with a capital between 4,000 and 16,000 TND, a few large outliers exceed 25,000 TND, pulling the overall average upward.
3. **Activity Breakdown:** The majority of cooperatives are concentrated in cereals and livestock, leaving a noticeable gap in agricultural logistics and support services.

---

## 📁 ملفات المشروع / Repository Structure
```text
├── data_raw/          # الملفات الخام الأصلية / Raw dataset files
├── data_processed/    # البيانات النظيفة بعد المعالجة / Cleaned CSV output
└── notebooks/         # كود بايثون والرسومات البيانية / Python scripts & plots
```

