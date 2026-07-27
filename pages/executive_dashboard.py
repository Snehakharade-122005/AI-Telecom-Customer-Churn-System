import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector

from database import get_connection
st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Executive Customer Intelligence Dashboard")

st.write(
    "Real-time business intelligence dashboard for customer churn analytics."
)

st.divider()
@st.cache_data
def load_data():

    conn = get_connection()

    query = "SELECT * FROM predictions"

    df = pd.read_sql(query, conn)

    conn.close()

    return df


df = load_data()
if df.empty:

    st.warning("No prediction data found.")

    st.stop()
    st.subheader("Latest Customer Predictions")

st.dataframe(
    df,
    use_container_width=True
)
