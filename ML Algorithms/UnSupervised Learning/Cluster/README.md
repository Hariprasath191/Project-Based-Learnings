# 🛍️ Mall Customer Segmentation using Clustering Algorithms

This project focuses on **customer segmentation** using unsupervised machine learning techniques to identify distinct customer groups based on demographic and spending behavior.  
The goal is to derive **actionable marketing insights** from data.

---

## 📌 Problem Statement
Retail businesses often struggle with applying the same marketing strategy to all customers.  
This project segments customers into meaningful groups to enable **targeted and personalized marketing**.

---

## 📊 Dataset
**Mall Customer Segmentation Dataset**

**Features used:**
- Gender
- Age
- Annual Income (k$)
- Spending Score (1–100)

The dataset contains customer demographic and behavioral information suitable for clustering.

---

## 🧠 Approach Overview

The project follows a **complete data science pipeline**:

1. Data Understanding
2. Exploratory Data Analysis (EDA)
3. Feature Selection & Preprocessing
4. Clustering using multiple algorithms
5. Cluster Evaluation
6. Marketing Insights Extraction

---

## 🔍 Exploratory Data Analysis (EDA)

- Analyzed distributions of Age, Income, and Spending Score.
- Identified wide variation in spending behavior.
- Observed cloud-like groupings in feature relationships.
- Confirmed clustering feasibility through visual and statistical analysis.

---

## ⚙️ Data Preprocessing

- Removed non-informative identifiers.
- Encoded categorical variables (Gender).
- Scaled numerical features using `StandardScaler`.
- Prepared final feature matrix for clustering.

---

## 🤖 Clustering Algorithms Used

### 1️⃣ K-Means Clustering
- Optimal number of clusters determined using the **Elbow Method**.
- Selected **K = 5** based on balance between compactness and interpretability.
- Provided stable and interpretable clusters.

### 2️⃣ Hierarchical Clustering
- Used Ward linkage method.
- Dendrogram supported similar cluster structure.
- Achieved slightly higher silhouette score than K-Means.

### 3️⃣ DBSCAN
- Applied density-based clustering.
- Identified noise points.
- Less effective due to lack of strong density separation in data.

---

## 📏 Cluster Evaluation (Silhouette Score)

| Algorithm     | Silhouette Score |
|--------------|------------------|
| K-Means      | 0.2719 |
| Hierarchical | 0.2870 |
| DBSCAN       | 0.2273 |

**Conclusion:**  
Hierarchical clustering performed marginally better numerically, while K-Means was chosen for its simplicity, stability, and business interpretability.

---

## 📉 Dimensionality Reduction for Visualization

- Applied **PCA (Principal Component Analysis)** to project 4D data into 2D.
- Enabled visualization of clusters formed in higher-dimensional space.

---

## 📈 Marketing Insights (One-Line per Cluster)

- **Cluster 0 – Older, Conservative Spenders:** Focus on retention through loyalty programs and trust-based offers.
- **Cluster 1 – High-Income, Low-Spending Customers:** Target with personalized premium offers to unlock untapped revenue.
- **Cluster 2 – Young, High-Spending Customers:** Use promotions and trend-driven campaigns to maximize purchase frequency.
- **Cluster 3 – High-Value Loyal Customers:** Prioritize retention with VIP benefits and exclusive rewards.
- **Cluster 4 – Young, Impulsive Spenders:** Drive volume using affordable bundles and social-media-led marketing.

---

## 🧠 Key Business Takeaway

Customer segmentation enables **targeted marketing strategies**, improving conversion rates, customer retention, and overall ROI.

---

## 🛠️ Technologies Used

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- PCA, K-Means, Hierarchical Clustering, DBSCAN

---

## 📁 Project Structure
├── Mall customer segmentation.ipynb
├── README.md
└── data/
└── Mall_Customers.csv
## 🚀 Future Improvements

- Add cluster-based recommendation system
- Perform RFM analysis
- Integrate with real-time customer data
- Deploy insights via dashboard

---

## 👤 Author

**Hari Prasath**  
AI & Data Science Enthusiast  

---

⭐ If you find this project useful, feel free to star the repository!
