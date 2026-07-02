# 🛍️ Online Retail Customer Segmentation Project

## 📌 Overview

This project focuses on analyzing an online retail dataset to extract meaningful business insights and segment customers based on their purchasing behavior.

The workflow starts with exploratory data analysis (EDA) and data preprocessing, followed by building an RFM (Recency, Frequency, Monetary) model. Multiple clustering algorithms are then applied to segment customers, including K-Means, DBSCAN, and Agglomerative Clustering. After evaluation, the **K-Means model** was selected as the final model due to its performance and interpretability.

Additionally, a comprehensive **Power BI Dashboard** was developed to visualize key business metrics, sales trends, and customer performance.

Finally, the model is deployed using a **Streamlit web application** and containerized using **Docker** for easy and consistent deployment.

---

## 🎯 Objectives

* Analyze customer purchasing behavior
* Generate actionable business insights
* Segment customers using clustering techniques
* Create interactive visualizations for business stakeholders
* Deploy an interactive application for real-time predictions

---

## 🧠 Techniques & Methods

* Data Cleaning & Preprocessing
* Exploratory Data Analysis (EDA)
* Feature Engineering (RFM Analysis)
* Clustering Algorithms:

  * K-Means ✅ (Selected Model)
  * DBSCAN
  * Agglomerative Clustering
* Model Evaluation & Comparison
* Interactive Dashboard Development (Power BI)

---

## 📊 Power BI Dashboard

A professional **Power BI Dashboard** was created to provide clear, interactive visualizations of the retail business performance.

### Dashboard Highlights:
- **Key Metrics**: Total Revenue ($2.56M), Orders (40K+), Products Sold (1.29M), AOV, Cancelled Revenue, etc.
- **Time Series Analysis**: Revenue trend over time (Dec 2009 – Dec 2011)
- **Product Performance**: Top products by revenue and quantity
- **Geographic Analysis**: Revenue proportion by country (UK dominates at 88.47%)
- **Customer Analysis**: Top customers by orders and RFM clustering
- **Cancellation Insights**: Analysis of lost revenue due to cancellations

**Data Preparation for Dashboard:**
- Used **Power Query** to clean the data (removed negative prices, outliers, and duplicates).
- Built using **Microsoft Power BI**.

### Screenshots

![Online Retail Dashboard - Revenue & Product Overview](images/page1.png)

![Online Retail Dashboard - Customer & Cancellation Analysis](images/page2.png)

> You can open the `.pbix` file (if included in the repository) using Power BI Desktop for full interactivity.

---

## 📈 RFM Analysis

RFM segmentation is based on:

* **Recency (R):** How recently a customer made a purchase
* **Frequency (F):** How often they purchase
* **Monetary (M):** How much they spend

These features are used to cluster customers into meaningful groups (Champions, Loyal Customers, Potential Loyalists, Lost Customers, etc.).

## ⚙️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ahmed123-cell/Online-Retail
cd Online-Retail
```

---

### 2️⃣ Run Locally (Without Docker)

#### Install Dependencies

```bash
pip install -r requirements.txt
```

#### Run the Streamlit App

```bash
streamlit run streamlit_app.py
```

---

### 3️⃣ Run Using Docker 🐳

#### Build the Docker Image

```bash
docker build -t retail-segmentation-app .
```

#### Run the Container

```bash
docker run -p 8501:8501 retail-segmentation-app
```

Then open `http://localhost:8501`

---

## 📈 Key Insights

* Identified distinct customer segments based on purchasing behavior
* High-value customers (Champions) can be targeted with loyalty programs
* Significant cancellation rate represents major revenue leakage
* Business is heavily dependent on the United Kingdom market
* Clear segmentation + interactive dashboard improves marketing and strategic decision-making

---