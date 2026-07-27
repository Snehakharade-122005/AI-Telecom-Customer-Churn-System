import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import time

from database import save_prediction
from model_utils import model, scaler, label_encoders
from shap_explanation import get_shap_explanation

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------

st.set_page_config(
    page_title="Customer Prediction",
    page_icon="👤",
    layout="wide"
)

# -------------------------------------------------------
# HEADER
# -------------------------------------------------------

st.title("👤 Customer Churn Prediction")

st.write(
    """
Predict whether a telecom customer is likely to churn using
our Artificial Intelligence prediction engine.
    """
)

st.markdown("---")