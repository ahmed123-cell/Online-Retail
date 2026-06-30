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
    help="File must contain: Recency, Frequency, Monetary (optionally Cluster & Cluster Name)"
)

if uploaded_file is not None:
    with st.spinner("🔄 Processing your data..."):
        # Read file
        if uploaded_file.name.endswith('.csv'):
            rfm = pd.read_csv(uploaded_file)
        else:
            rfm = pd.read_excel(uploaded_file)

        # Column standardization (preserve 'Cluster Name' wording, just trim/title each word)
        rfm.columns = [' '.join(w.capitalize() for w in col.strip().split()) for col in rfm.columns]

        required_cols = ['Frequency', 'Recency', 'Monetary']
        if not all(col in rfm.columns for col in required_cols):
            st.error("❌ Missing required columns: Recency, Frequency, Monetary")
            st.stop()

        has_precomputed_clusters = 'Cluster' in rfm.columns and 'Cluster Name' in rfm.columns

        # Keep relevant columns
        keep_cols = required_cols.copy()
        if 'Customerid' in rfm.columns:
            rfm.rename(columns={'Customerid': 'CustomerID'}, inplace=True)
        if 'CustomerID' in rfm.columns:
            keep_cols = ['CustomerID'] + keep_cols
        if has_precomputed_clusters:
            keep_cols += ['Cluster', 'Cluster Name']

        rfm = rfm[keep_cols].copy()

        st.success(f"✅ File loaded successfully! **{len(rfm):,} customers** analyzed.")

        # ====================== Processing ======================
        rfm_log = np.log1p(rfm[required_cols])
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(rfm_log)

        if has_precomputed_clusters:
            # Use the clusters already present in the uploaded file
            rfm['Segment'] = rfm['Cluster Name']
            st.caption("ℹ️ Using the existing `Cluster` / `Cluster Name` columns from your file (KMeans skipped).")
        else:
            # Compute clusters with KMeans since the file doesn't already have them
            kmeans = KMeans(n_clusters=4, init='k-means++', random_state=42, n_init=10)
            rfm['Cluster'] = kmeans.fit_predict(X_scaled)

            cluster_names = {
                0: 'Loyal Customers',
                1: 'Lost Customers',
                2: 'Champions',
                3: 'Potential Loyalists'
            }
            rfm['Segment'] = rfm['Cluster'].map(cluster_names)
            rfm['Cluster Name'] = rfm['Segment']

        # ====================== Build a plot-ready dataframe ======================
        plot_df = pd.DataFrame(X_scaled, columns=['Recency', 'Frequency', 'Monetary'])
        plot_df['Segment'] = rfm['Segment'].values
        if 'CustomerID' in rfm.columns:
            plot_df['CustomerID'] = rfm['CustomerID'].values

        # ====================== Custom Colors (dynamic, supports any segment names) ======================
        palette = ["#22c55e", "#ef4444", "#3b82f6", "#eab308", "#a855f7", "#14b9c2", "#f97316", "#64748b"]
        unique_segments = sorted(rfm['Segment'].unique())
        custom_colors = {seg: palette[i % len(palette)] for i, seg in enumerate(unique_segments)}

        # ========================== Layout ==========================
        col1, col2 = st.columns([3, 2])

        with col1:
            st.subheader("🌐 3D Customer Segmentation")
            fig = px.scatter_3d(
                plot_df, x='Recency', y='Frequency', z='Monetary',
                color='Segment',
                color_discrete_map=custom_colors,
                hover_data=['CustomerID'] if 'CustomerID' in plot_df.columns else None,
                title="3D Visualization of Customer Segments",
                labels={'Recency': 'Recency (scaled)', 'Frequency': 'Frequency (scaled)', 'Monetary': 'Monetary (scaled)'}
            )
            fig.update_traces(marker=dict(size=6, opacity=0.85))
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("📊 Segment Distribution")
            segment_count = rfm['Segment'].value_counts()
            st.bar_chart(segment_count, color="#14b9c2")

        # Cluster Profile (use original, unscaled R/F/M values for interpretability)
        st.subheader("📋 Cluster Profiles")
        profile = rfm.groupby('Segment').agg({
            'Recency': 'mean',
            'Frequency': 'mean',
            'Monetary': 'mean',
            'Cluster': 'count'
        }).round(2)
        profile.rename(columns={'Cluster': 'Number of Customers'}, inplace=True)
        st.dataframe(profile.style.background_gradient(cmap='Blues'), use_container_width=True)

        # Marketing Recommendations (matched to whatever segment names are present)
        st.subheader("🎯 Marketing Recommendations")
        recommendations = {
            "Champions": "🏆 Reward with VIP perks, early access & exclusive premium offers",
            "Loyal Customers": "🎁 VIP Loyalty Program, Exclusive Offers & Early Access",
            "Regular Customers": "🔥 Upsell Campaigns, Bundle Offers & Volume Discounts",
            "Potential Loyalists": "🌟 Welcome Offers, Onboarding Emails & Engagement Campaigns",
            "Promising Customers": "🌟 Welcome Offers, Onboarding Emails & Engagement Campaigns",
            "Lost Customers": "📧 Win-Back Campaigns, Special Reactivation Discounts",
            "At Risk": "⚠️ Personalized Re-engagement Offers & Feedback Surveys",
        }

        for segment in profile.index:
            count = int(profile.loc[segment, 'Number of Customers'])
            rec = recommendations.get(segment, "💡 Tailor a targeted campaign based on this segment's RFM behavior.")
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
    Optional: `CustomerID`, `Cluster`, `Cluster Name` (if your data is already segmented, these will be used directly instead of recomputing with KMeans).
    """)