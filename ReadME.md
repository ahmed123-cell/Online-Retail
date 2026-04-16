# 🛍️ Online Retail Customer Segmentation Project

## 📌 Overview

This project focuses on analyzing an online retail dataset to extract meaningful business insights and segment customers based on their purchasing behavior.

The workflow starts with exploratory data analysis (EDA) and data preprocessing, followed by building an RFM (Recency, Frequency, Monetary) model. Multiple clustering algorithms are then applied to segment customers, including K-Means, DBSCAN, and Agglomerative Clustering. After evaluation, the **K-Means model** was selected as the final model due to its performance and interpretability.

Finally, the model is deployed using a **Streamlit web application** and containerized using **Docker** for easy and consistent deployment.

---

## 🎯 Objectives

* Analyze customer purchasing behavior
* Generate actionable business insights
* Segment customers using clustering techniques
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

---

## 📊 RFM Analysis

RFM segmentation is based on:

* **Recency (R):** How recently a customer made a purchase
* **Frequency (F):** How often they purchase
* **Monetary (M):** How much they spend

These features are used to cluster customers into meaningful groups.
```

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the Repository

```
git clone https://github.com/ahmed123-cell/Online-Retail
cd your-repo
```

---

### 2️⃣ Run Locally (Without Docker)

#### Install Dependencies

```
pip install -r requirements.txt
```

#### Run the Streamlit App

```
streamlit run app/app.py
```

Then open your browser at:

```
http://localhost:8501
```

---

### 3️⃣ Run Using Docker 🐳

#### Build the Docker Image

```
docker build -t retail-segmentation-app .
```

#### Run the Container

```
docker run -p 8501:8501 retail-segmentation-app
```

Then open:

```
http://localhost:8501
```

---

## 📈 Key Insights

* Identified distinct customer segments based on purchasing behavior
* High-value customers can be targeted with loyalty programs
* Low-frequency customers may need re-engagement strategies
* Clear segmentation improves marketing efficiency