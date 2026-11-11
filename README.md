


# خط الإنتاج الشامل لتحليل البيانات: الشركات التعاونية الفلاحية في تونس (SMSA)
# Comprehensive Data Analytics Pipeline: Tunisian Agricultural Cooperative Societies (SMSA)

👉 [**اضغط هنا لزيارة لوحة التحكم التفاعلية الحية / View Live Interactive Dashboard Here**](https://docs.google.com/spreadsheets/d/1xl6FTgRiQ785RDBSkLr2IM2qdCVR6BdTQiTUdM312Bw/edit?usp=sharing)

---

##  التقرير الاستشاري الاستراتيجي

### 📌 نظرة عامة على المشروع
يمثل هذا المشروع خط إنتاج متكامل لتحليل البيانات الفلاحية في تونس. تم جلب البيانات الخام من وزارة الفلاحة، وتنظيفها ومعايرتها جغرافيّاً وماليّاً بالكامل باستخدام لغة **بايثون (Pandas)**، ومن ثم بناء لوحة تحكم تفاعلية ذكية وحية باستخدام الجداول المحورية والمقسّمات التفاعلية لتمكين صناع القرار من اتخاذ خطوات استباقية مدعومة بالأرقام.

### 🧭 أسئلة العمل التجارية المعالجة (Business Questions)
تم تصميم هذا التحليل للإجابة بدقة على الأسئلة الاستراتيجية التالية التي تشغل بال مسؤولي قطاع الفلاحة والدعم:
1. **الكثافة الإقليمية:** أين تتركز الشركات التعاونية جغرافيّاً في تونس لتوجيه الاستثمارات اللوجستية؟
2. **هيكلة رؤوس الأموال:** كيف تتوزع الميزانيات التمويلية بين المعتمديات، وأين تقع الفجوات التمويلية؟
3. **الحصص السوقية للأنشطة:** ما هي القطاعات الفلاحية المهيمنة (حبوب، تربية ماشية، زيتون) وأيها يعاني من نقص الخدمات؟
4. **الارتباط الهيكلي:** هل القوة المالية ورأس المال القوي للشركة هو المحرك الأساسي لجذب الفلاحين وزيادة عدد المنخرطين؟
5. **الاحتكار والهيمنة المالية:** هل توجد شركات عملاقة تشوه متوسطات السوق وتستحوذ على الدعم؟

### 📊 الاستنتاجات التحليلية والتوصيات الاستراتيجية (Insights & Actions)

#### 1. مفاجأة تحليل الارتباط الإحصائي (رأس المال مقابل المنخرطين)
* **النتيجة الإحصائية:** عند حساب معامل ارتباط بيرسون (Pearson Correlation) بين رأس المال وعدد المنخرطين، كانت النتيجة قريبة جداً من الصفر (علاقة شبه منعدمة).
* **التوصية التجارية لصانع القرار:** القوة المالية للشركة **ليست** السبب الذي يدفع الفلاح التونسي للانضمام للتعاونيات. الفلاح يبحث عن القرب الجغرافي وتوفر الخدمات الميدانية (مثل جمع الحبوب أو توفير الأعلاف). ننصح الوزارة بتوجيه الدعم لبناء فروع قريبة من الفلاحين بدلاً من ضخ أموال ضخمة في خزائن شركات مركزية كبرى.

#### 2. عزل وتحجيم القيم الشاذة والاحتكار (Financial Outliers)
* **النتيجة الإحصائية:** عبر معادلة الصندوق الإحصائي (IQR)، تبين أن النطاق الطبيعي لأغلب الشركات يتراوح بين 4,000 و 16,000 دينار، ولكن تم عزل شركات شاذة تخطت حاجز الـ 25,000 دينار.
* **التوصية التجارية لصانع القرار:** هناك فئة محدودة جداً من الشركات "العمالقة" تهيمن ماليّاً على السوق وتخفي خلفها ضعف الشركات الصغرى. يجب فرض رقابة صارمة على توزيع القروض والدعم الفلاحي لضمان وصوله للشركات الصغيرة الناشئة الواقعة داخل النطاق الطبيعي لحماية عدالة السوق.

#### 3. سد فجوة الأنشطة والخدمات
* **النتيجة الإحصائية:** كشف مخطط الدونات التفاعلي عن تكدس هائل للشركات في قطاعي الحبوب وتربية الماشية التقليدية، مقابل نقص حاد في شركات الخدمات اللوجستية الحديثة.
* **التوصية التجارية لصانع القرار:** يجب تقديم حوافز وإعفاءات ضريبية تشجع الفلاحين على تأسيس شركات تعاونية متخصصة في خدمات النقل والتبريد والتسليم المباشر للمستهلك لكسر احتكار السماسرة.

---

## Strategic Analytical Report

### 📌 Project Overview
This repository showcases an end-to-end production-grade data analytics architecture. The pipeline ingests multi-structured localized datasets from the Tunisian Ministry of Agriculture, executes advanced algorithmic data cleaning and geo-standardization via **Python (Pandas)**, performs Exploratory Data Analysis (EDA) including financial outlier identification and statistical correlations, and deploys a live corporate reporting layer.

### 🧭 Core Business Questions Addressed
1. **Regional Density:** Which governance zones and delegations demonstrate the highest concentration of cooperative infrastructure?
2. **Capitalization Profiles:** What is the macroeconomic distribution of total capital investment across regions?
3. **Market Share Dynamics:** How are diverse agricultural activities segmented across national networks?
4. **Structural Correlation:** Does a cooperative’s baseline financial capitalization directly drive its capacity to attract members?
5. **Asset Domination:** Are there extreme financial anomalies that statistically distort standard market averages?

### 📊 Analytical Insights & Strategic Discoveries

#### 1. Structural Correlation Insight (Capital vs. Membership)
* **Statistical Finding:** The Pearson Correlation analysis between total baseline capital and active registered membership yielded a coefficient approaching zero.
* **Strategic Interpretation:** Financial power is **not** the primary mechanism driving Tunisian farmers to join agricultural cooperatives. Geographical convenience and operational capabilities are the true drivers of membership scale, signaling that government funding should focus on infrastructure availability over raw asset capitalization.

#### 2. Financial Outliers & Domination Isolation
* **Statistical Finding:** Utilizing the Interquartile Range (IQR) bounding method, the financial distribution isolated select dominant outlier cooperatives maintaining capital balances significantly exceeding standard margins (upper bounds ranging from 4,000 to 16,000 TND, with outliers peaking at 25,000 TND).
* **Strategic Interpretation:** A small tier of highly capitalized cooperative hubs holds disproportionate asset control. Public subsidies must be carefully audited and targeted toward under-funded granular hubs inside the standard IQR box to ensure equitable national market development.

---

## 📁 هيكلية مجلدات المشروع / Repository Structure
```text
├── data_raw/          # البيانات الخام والمشتتة القادمة من الإدارة الفلاحية
├── data_processed/    # البيانات النظيفة والمترجمة بالكامل والجاهزة للتحليل
└── notebooks/         # أكواد بايثون والرسومات البيانية عالية الدقة والداشبورد
```

