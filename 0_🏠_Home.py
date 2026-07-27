import streamlit as st

st.set_page_config(
    page_title="AI Telecom Customer Churn Platform",
    page_icon="📊",
    layout="wide"
)

# ===========================
# HERO
# ===========================

st.title("📊 AI Telecom Customer Churn Intelligence Platform")

st.markdown("""
### Enterprise AI Platform for Customer Retention

Predict customer churn, monitor business KPIs, analyze customer behavior,
and generate AI-powered retention strategies in real time.
""")

st.markdown("---")

# ===========================
# KPI CARDS
# ===========================

col1, col2, col3, col4 = st.columns(4)

col1.metric("AI Model Accuracy", "81.2%", "↑ 2.4%")
col2.metric("Prediction Speed", "<1 sec")
col3.metric("Modules", "6")
col4.metric("API Status", "🟢 Online")

st.markdown("---")

# ===========================
# PLATFORM MODULES
# ===========================

st.subheader("🚀 Platform Modules")

c1, c2 = st.columns(2)

with c1:

    st.success("""
### 📈 Customer Prediction

✔ Predict Churn

✔ Risk Score

✔ Probability

✔ AI Recommendation
""")

    st.info("""
### 📂 Bulk Prediction

✔ CSV Upload

✔ Batch Prediction

✔ Download Results
""")

    st.warning("""
### 👥 Customer Management

✔ Search Customers

✔ Update Records

✔ Database Integration
""")

with c2:

    st.success("""
### 📊 Analytics Dashboard

✔ Revenue Analysis

✔ Churn Rate

✔ Risk Distribution

✔ Interactive Charts
""")

    st.info("""
### 🤖 AI Engine

✔ TensorFlow ANN

✔ SHAP Explainability

✔ Feature Importance
""")

    st.warning("""
### 🌐 REST API

✔ FastAPI

✔ JSON Response

✔ External Integration
""")

st.markdown("---")

# ===========================
# TECHNOLOGY STACK
# ===========================

st.subheader("🛠 Technology Stack")

tech1, tech2, tech3, tech4 = st.columns(4)

tech1.info("""
Python

TensorFlow

Scikit-Learn
""")

tech2.info("""
Streamlit

FastAPI

Plotly
""")

tech3.info("""
MySQL

Pandas

NumPy
""")

tech4.info("""
Docker

GitHub

REST API
""")

st.markdown("---")

st.subheader("🏢 Business Problem")

st.write("""
Customer churn is one of the biggest challenges for telecom companies.
This platform helps businesses identify customers who are likely to leave,
estimate churn probability, calculate business risk, and recommend
retention strategies using Artificial Intelligence.
""")

st.markdown("---")

st.success("✅ Enterprise AI Platform Developed by Sneha Kharade")