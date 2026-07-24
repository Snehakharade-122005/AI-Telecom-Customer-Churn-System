import streamlit as st

st.set_page_config(
    page_title="AI Telecom Customer Churn System",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Telecom Customer Churn System")

st.markdown("---")

st.header("Welcome")

st.write("""
The AI Telecom Customer Churn System predicts whether a telecom customer
is likely to leave the company using Machine Learning.

This project also provides:
- Customer Churn Prediction
- Bulk Customer Prediction
- Customer Management
- Analytics Dashboard
- FastAPI Integration
- MySQL Database
- AI Recommendations
""")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🤖 TensorFlow ANN")

with col2:
    st.success("⚡ FastAPI")

with col3:
    st.warning("🗄 MySQL Database")

st.markdown("---")

st.subheader("Project Features")

st.write("""
✅ Customer Churn Prediction

✅ Bulk Customer Prediction

✅ Analytics Dashboard

✅ Customer Management System

✅ AI Recommendation Engine

✅ SHAP Feature Importance

✅ REST API
""")

st.markdown("---")

st.caption(
    "Developed by Sneha Kharade | DMVCT - DS Batch"
)