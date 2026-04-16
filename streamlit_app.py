import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import plotly.express as px

# ========================== Page Configuration ==========================
st.set_page_config(page_title="RFM Customer Segmentation", layout="wide", page_icon="🛒")

# ====================== Custom CSS for Beautiful Design ======================
st.markdown("""
    <style>
        .main {
            background-color: #f1f5f9;
        }
        .stApp h1 {
            color: #14b9c2;
            font-size: 42px;
            font-weight: bold;
        }
        .stApp h2, .stApp h3 {
            color: #14b9c2;
        }
        .css-1d391kg {  /* Sidebar */
            background-color: #1e3a8a;
        }
        .stButton>button {
            background-color: #14b9c2;
            color: white;
        }
        .success-box {
            background-color: #d1fae5;
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #10b981;
        }
    </style>
""", unsafe_allow_html=True)

# ========================== Header ==========================
st.markdown("""
    <h1 style='text-align: center; color: #14b9c2;'>
        🛍️ RFM Customer Segmentation Dashboard
    </h1>
    <p style='text-align: center; color: #475569; font-size: 18px;'>
        Powerful insights to understand your customers better
    </p>
    <hr>
""", unsafe_allow_html=True)

st.markdown("### Upload your RFM file and discover customer segments instantly")

# ========================== Sidebar ==========================
st.sidebar.header("📂 Upload RFM File")
uploaded_file = st.sidebar.file_uploader(
    "Upload your RFM file (CSV or Excel)",
    type=["csv", "xlsx", "xls"],
    help="File must contain: Recency, Frequency, Monetary"
)

if uploaded_file is not None:
    with st.spinner("🔄 Processing your data..."):
        # Read file
        if uploaded_file.name.endswith('.csv'):
            rfm = pd.read_csv(uploaded_file)
        else:
            rfm = pd.read_excel(uploaded_file)

        # Column standardization
        rfm.columns = [col.title().strip() for col in rfm.columns]
        
        required_cols = ['Recency', 'Frequency', 'Monetary']
        if not all(col in rfm.columns for col in required_cols):
            st.error("❌ Missing required columns: Recency, Frequency, Monetary")
            st.stop()

        rfm = rfm[['CustomerID'] + required_cols if 'CustomerID' in rfm.columns else required_cols].copy()

        st.success(f"✅ File loaded successfully! **{len(rfm):,} customers** analyzed.")

        # ====================== Processing ======================
        rfm_log = np.log1p(rfm[required_cols])
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(rfm_log)

        kmeans = KMeans(n_clusters=4, init='k-means++', random_state=42)
        rfm['Cluster'] = kmeans.fit_predict(X_scaled)

        cluster_names = {
            0: 'Regular Customers',
            1: 'Promising Customers',
            2: 'Loyal Customers',
            3: 'Lost Customers'
        }
        rfm['Segment'] = rfm['Cluster'].map(cluster_names)

        # ====================== Custom Colors for 3D Plot ======================
        custom_colors = {
            "Loyal Customers": "#22c55e",    # Green
            "Regular Customers": "#ef4444",  # Red
            "Promising Customers": "#3b82f6",# Blue
            "Lost Customers": "#eab308"      # Yellow
        }

        # ========================== Layout ==========================
        col1, col2 = st.columns([3, 2])

        with col1:
            st.subheader("🌐 3D Customer Segmentation")
            fig = px.scatter_3d(
                rfm, x='Recency', y='Frequency', z='Monetary',
                color='Segment',
                color_discrete_map=custom_colors,
                hover_data=['CustomerID'] if 'CustomerID' in rfm.columns else None,
                title="3D Visualization of Customer Segments",
                labels={'Recency': 'Recency (days)', 'Frequency': 'Frequency', 'Monetary': 'Monetary'}
            )
            fig.update_traces(marker=dict(size=6, opacity=0.85))
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("📊 Segment Distribution")
            segment_count = rfm['Segment'].value_counts()
            st.bar_chart(segment_count, color="#14b9c2")

        # Cluster Profile
        st.subheader("📋 Cluster Profiles")
        profile = rfm.groupby('Segment').agg({
            'Recency': 'mean',
            'Frequency': 'mean',
            'Monetary': 'mean',
            'Cluster': 'count'
        }).round(2)
        profile.rename(columns={'Cluster': 'Number of Customers'}, inplace=True)
        st.dataframe(profile.style.background_gradient(cmap='Blues'), use_container_width=True)

        # Marketing Recommendations
        st.subheader("🎯 Marketing Recommendations")
        recommendations = {
            "Loyal Customers": "🎁 VIP Loyalty Program, Exclusive Offers & Early Access",
            "Regular Customers": "🔥 Upsell Campaigns, Bundle Offers & Volume Discounts",
            "Promising Customers": "🌟 Welcome Offers, Onboarding Emails & Engagement Campaigns",
            "Lost Customers": "📧 Win-Back Campaigns, Special Reactivation Discounts"
        }

        for segment, rec in recommendations.items():
            if segment in profile.index:
                count = int(profile.loc[segment, 'Number of Customers'])
                st.info(f"**{segment}** ({count:,} customers)\n\n{rec}")

        # Download
        st.download_button(
            label="📥 Download Segmented Data",
            data=rfm.to_csv(index=False).encode('utf-8'),
            file_name="rfm_segmented_customers.csv",
            mime="text/csv"
        )

else:
    st.info("👆 Please upload your RFM file (CSV or Excel) to begin analysis.")
    st.markdown("""
    **Required columns**: `Recency`, `Frequency`, `Monetary`  
    Optional: `CustomerID`
    """)