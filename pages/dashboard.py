import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="AI Telecom Customer Churn Dashboard",
    page_icon="📊",
    layout="wide"
)

# Auto Refresh every 30 seconds
st_autorefresh(
    interval=30000,
    key="dashboard_refresh"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.main{
    background:#f6f8fb;
}

div[data-testid="metric-container"]{
    background:white;
    padding:18px;
    border-radius:12px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# DATABASE CONNECTION
# =====================================================

def get_connection():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql@123",
        database="telecom_churn"
    )

# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_data():

    conn = get_connection()

    df = pd.read_sql(
        "SELECT * FROM predictions",
        conn
    )

    conn.close()

    return df

df = load_data()

# If database is empty

if df.empty:

    st.warning("No Prediction Data Found.")

    st.stop()

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("📊 AI Telecom Dashboard")

st.sidebar.markdown("---")

search = st.sidebar.text_input(
    "🔍 Search Customer"
)

risk_filter = st.sidebar.multiselect(
    "Risk Level",
    options=df["risk"].unique(),
    default=df["risk"].unique()
)

prediction_filter = st.sidebar.multiselect(
    "Prediction",
    options=df["prediction"].unique(),
    default=df["prediction"].unique()
)

gender_filter = st.sidebar.multiselect(
    "Gender",
    options=df["gender"].unique(),
    default=df["gender"].unique()
)

st.sidebar.markdown("---")

st.sidebar.success("TensorFlow ANN")
st.sidebar.success("FastAPI")
st.sidebar.success("MySQL")
st.sidebar.success("Streamlit")

# =====================================================
# FILTER DATA
# =====================================================

filtered_df = df.copy()

filtered_df = filtered_df[
    filtered_df["risk"].isin(risk_filter)
]

filtered_df = filtered_df[
    filtered_df["prediction"].isin(prediction_filter)
]

filtered_df = filtered_df[
    filtered_df["gender"].isin(gender_filter)
]

if search:

    filtered_df = filtered_df[
        filtered_df["gender"]
        .astype(str)
        .str.contains(search, case=False, na=False)
    ]

# =====================================================
# HEADER
# =====================================================

st.title("📊 AI Telecom Customer Churn Analytics Dashboard")

st.caption(
    "TensorFlow • FastAPI • Streamlit • MySQL"
)

st.markdown("---")

# =====================================================
# KPI CALCULATIONS
# =====================================================

total_customers = len(filtered_df)

high_risk = len(
    filtered_df[
        filtered_df["risk"] == "🔴 High Risk"
    ]
)

medium_risk = len(
    filtered_df[
        filtered_df["risk"] == "🟡 Medium Risk"
    ]
)

low_risk = len(
    filtered_df[
        filtered_df["risk"] == "🟢 Low Risk"
    ]
)

revenue = filtered_df["revenue_risk"].sum()

churn_rate = (
    len(
        filtered_df[
            filtered_df["prediction"] ==
            "Customer Will Churn"
        ]
    )
    /
    max(total_customers,1)
) * 100

average_probability = (
    filtered_df["probability"].mean() * 100
)

# =====================================================
# KPI CARDS
# =====================================================

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.metric(
        "👥 Total Customers",
        total_customers
    )

with c2:

    st.metric(
        "🔴 High Risk",
        high_risk
    )

with c3:

    st.metric(
        "💰 Revenue At Risk",
        f"₹ {revenue:,.2f}"
    )

with c4:

    st.metric(
        "📉 Churn Rate",
        f"{churn_rate:.2f}%"
    )

st.markdown("---")
# =====================================================
# DASHBOARD TABS
# =====================================================

tab1, tab2, tab3 = st.tabs(
    ["📊 Overview", "📈 Analytics", "💰 Revenue"]
)

# =====================================================
# TAB 1 : OVERVIEW
# =====================================================

with tab1:

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🥧 Customer Churn Distribution")

        churn = filtered_df["prediction"].value_counts()

        fig = px.pie(
            values=churn.values,
            names=churn.index,
            hole=0.45,
            color_discrete_sequence=px.colors.qualitative.Set2
        )

        fig.update_layout(
            template="plotly_white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        st.subheader("📊 Risk Level Distribution")

        risk = filtered_df["risk"].value_counts()

        fig = px.bar(
            x=risk.index,
            y=risk.values,
            color=risk.index,
            labels={
                "x":"Risk Level",
                "y":"Customers"
            }
        )

        fig.update_layout(
            template="plotly_white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# =====================================================
# TAB 2 : ANALYTICS
# =====================================================

with tab2:

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📄 Contract Analysis")

        fig = px.histogram(
            filtered_df,
            x="contract",
            color="prediction",
            barmode="group"
        )

        fig.update_layout(
            template="plotly_white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        st.subheader("👨 Gender Analysis")

        fig = px.histogram(
            filtered_df,
            x="gender",
            color="prediction",
            barmode="group"
        )

        fig.update_layout(
            template="plotly_white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.subheader("📈 Prediction Trend")

    trend = (
        filtered_df
        .groupby("prediction_date")
        .size()
        .reset_index(name="Predictions")
    )

    fig = px.line(
        trend,
        x="prediction_date",
        y="Predictions",
        markers=True
    )

    fig.update_layout(
        template="plotly_white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================================================
# TAB 3 : REVENUE
# =====================================================

with tab3:

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("💰 Revenue at Risk")

        fig = px.bar(
            filtered_df,
            x="id",
            y="revenue_risk",
            color="risk"
        )

        fig.update_layout(
            template="plotly_white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        st.subheader("📊 Probability Distribution")

        fig = px.histogram(
            filtered_df,
            x="probability",
            nbins=20,
            color="prediction"
        )

        fig.update_layout(
            template="plotly_white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

st.markdown("---")
# =====================================================
# SEARCH & FILTER SECTION
# =====================================================

st.header("🔍 Search & Filter Predictions")

search = st.text_input(
    "Search by Gender / Prediction / Risk"
)

search_df = filtered_df.copy()

if search:

    search_df = search_df[
        search_df["gender"].astype(str).str.contains(search, case=False, na=False) |
        search_df["prediction"].astype(str).str.contains(search, case=False, na=False) |
        search_df["risk"].astype(str).str.contains(search, case=False, na=False)
    ]

st.markdown("---")

# =====================================================
# LATEST PREDICTIONS
# =====================================================

st.header("📋 Latest Predictions")

latest = search_df.sort_values(
    by="prediction_date",
    ascending=False
).head(10)

st.dataframe(
    latest,
    use_container_width=True
)

st.markdown("---")

# =====================================================
# HIGH RISK CUSTOMERS
# =====================================================

st.header("🚨 High Risk Customers")

high_risk_df = search_df[
    search_df["risk"] == "🔴 High Risk"
]

if len(high_risk_df) > 0:

    st.dataframe(
        high_risk_df,
        use_container_width=True
    )

else:

    st.success("No High Risk Customers Found")

st.markdown("---")

# =====================================================
# TOP REVENUE RISK CUSTOMERS
# =====================================================

st.header("🏆 Top Revenue Risk Customers")

top = search_df.sort_values(
    by="revenue_risk",
    ascending=False
).head(10)

st.dataframe(
    top,
    use_container_width=True
)

st.markdown("---")

# =====================================================
# DOWNLOAD REPORT
# =====================================================

csv = search_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Prediction Report",
    data=csv,
    file_name="telecom_prediction_report.csv",
    mime="text/csv"
)

st.markdown("---")
# =====================================================
# EXECUTIVE DASHBOARD
# =====================================================

st.header("📊 Executive Summary")

col1, col2 = st.columns([2, 3])

with col1:

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=churn_rate,
        title={"text": "Overall Churn Rate (%)"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "red"},
            "steps": [
                {"range": [0, 40], "color": "#90EE90"},
                {"range": [40, 70], "color": "#FFD580"},
                {"range": [70, 100], "color": "#FF7F7F"}
            ]
        }
    ))

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    st.info(f"""
### 📈 Prediction Summary

👥 **Total Customers:** {total_customers}

🔴 **High Risk:** {high_risk}

🟡 **Medium Risk:** {medium_risk}

🟢 **Low Risk:** {low_risk}

💰 **Revenue at Risk:** ₹ {revenue:,.2f}

📉 **Churn Rate:** {churn_rate:.2f}%

🎯 **Average Probability:** {average_probability:.2f}%
""")

st.markdown("---")

# =====================================================
# REVENUE SUMMARY
# =====================================================

st.header("💰 Revenue Summary")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Average Revenue Risk",
        f"₹ {search_df['revenue_risk'].mean():,.2f}"
    )

with c2:
    st.metric(
        "Maximum Revenue Risk",
        f"₹ {search_df['revenue_risk'].max():,.2f}"
    )

with c3:
    st.metric(
        "Minimum Revenue Risk",
        f"₹ {search_df['revenue_risk'].min():,.2f}"
    )

st.markdown("---")

# =====================================================
# COMPLETE HISTORY
# =====================================================

st.header("📑 Complete Prediction History")

st.dataframe(
    search_df,
    use_container_width=True
)

st.markdown("---")

# =====================================================
# FOOTER
# =====================================================

st.success("✅ AI Telecom Customer Churn Dashboard Loaded Successfully")

st.markdown(
"""
---
### 👨‍💻 Project Information

**Project:** AI Telecom Customer Churn Prediction System

**Technologies Used**

- TensorFlow ANN
- FastAPI
- Streamlit
- MySQL
- Plotly
- Python

**Developed By**

**Sneha Kharade**

**DMVCT – DS Batch**
"""
)