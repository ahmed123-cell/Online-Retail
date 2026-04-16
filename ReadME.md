# 🛍️ RFM Customer Segmentation Dashboard

**A powerful Streamlit web application for customer segmentation using RFM Analysis and K-Means Clustering.**

---

## 📋 Project Overview

This project provides an interactive dashboard that helps businesses understand their customers by applying the **RFM (Recency, Frequency, Monetary)** model combined with **K-Means clustering**.

Users simply upload a pre-computed RFM file (CSV or Excel), and the app instantly:
- Applies log transformation + standardization
- Performs K-Means clustering (4 segments)
- Visualizes customers in an interactive 3D plot
- Shows detailed cluster profiles
- Provides actionable marketing recommendations

---

## ✨ Key Features

- ✅ Support for **CSV** and **Excel** files
- ✅ Automatic data validation
- ✅ Log transformation + Standard Scaling
- ✅ K-Means Clustering (4 optimized segments)
- ✅ Beautiful interactive **3D visualization**
- ✅ Cluster profile table with averages
- ✅ Smart marketing recommendations per segment
- ✅ Download segmented results as CSV
- ✅ Modern, clean UI with professional design

---

## 🛠️ Technologies Used

- **Python 3.10+**
- **Streamlit** – Web application framework
- **Pandas** & **NumPy** – Data processing
- **Scikit-learn** – K-Means clustering + preprocessing
- **Plotly** – Interactive 3D visualization
- **Docker** – Containerization

---

## 📊 Input Requirements

Your uploaded file must contain the following columns:

| Column      | Description                     | Required |
|-------------|----------------------------------|----------|
| `Recency`   | Days since last purchase         | Yes      |
| `Frequency` | Number of purchases              | Yes      |
| `Monetary`  | Total spending amount            | Yes      |
| `CustomerID`| Customer identifier (optional)   | No       |

---

## 🚀 How to Run the Project

### Option 1: Run Locally (Recommended for Development)

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd rfm-customer-segmentation