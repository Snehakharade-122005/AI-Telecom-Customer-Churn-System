import streamlit as st
import pandas as pd

from database import save_prediction
from model_utils import model, scaler, label_encoders
from shap_explanation import get_shap_explanation
# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="AI Telecom Customer Churn System",
    page_icon="📊",
    layout="wide"
)
# Sidebar
st.sidebar.title("📊 AI Telecom Customer Churn System")
st.sidebar.success("Select a page")


# -------------------------------------------------
# Title
# -------------------------------------------------

st.title("📊 AI Telecom Customer Churn Prediction System")

st.markdown("---")

st.write(
"""
This AI application predicts whether a telecom customer is likely to churn,
calculates churn probability,
assigns risk level,
and provides AI-powered recommendations.
"""
)

st.markdown("---")


# -------------------------------------------------
# Customer Information
# -------------------------------------------------

st.header("📝 Customer Information")


col1, col2 = st.columns(2)


with col1:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )


    senior = st.selectbox(
        "Senior Citizen",
        ["No", "Yes"]
    )


    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )


    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )


    tenure = st.slider(
        "Tenure (Months)",
        0,
        72,
        12
    )


    phone = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )


    multiple = st.selectbox(
        "Multiple Lines",
        [
            "No",
            "Yes",
            "No phone service"
        ]
    )


    internet = st.selectbox(
        "Internet Service",
        [
            "DSL",
            "Fiber optic",
            "No"
        ]
    )


    online_security = st.selectbox(
        "Online Security",
        [
            "No",
            "Yes",
            "No internet service"
        ]
    )


    online_backup = st.selectbox(
        "Online Backup",
        [
            "No",
            "Yes",
            "No internet service"
        ]
    )



with col2:


    device_protection = st.selectbox(
        "Device Protection",
        [
            "No",
            "Yes",
            "No internet service"
        ]
    )


    tech_support = st.selectbox(
        "Tech Support",
        [
            "No",
            "Yes",
            "No internet service"
        ]
    )


    streaming_tv = st.selectbox(
        "Streaming TV",
        [
            "No",
            "Yes",
            "No internet service"
        ]
    )


    streaming_movies = st.selectbox(
        "Streaming Movies",
        [
            "No",
            "Yes",
            "No internet service"
        ]
    )


    contract = st.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )


    paperless = st.selectbox(
        "Paperless Billing",
        [
            "Yes",
            "No"
        ]
    )


    payment = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )


    monthly = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
    )


    total = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=500.0
    )


st.markdown("---")


predict = st.button(
    "🚀 Predict Customer Churn"
)
# -------------------------------------------------
# Prediction
# -------------------------------------------------

if predict:


    customer_data = pd.DataFrame({

        "gender": [gender],
        "SeniorCitizen": [1 if senior == "Yes" else 0],
        "Partner": [partner],
        "Dependents": [dependents],
        "tenure": [tenure],
        "PhoneService": [phone],
        "MultipleLines": [multiple],
        "InternetService": [internet],
        "OnlineSecurity": [online_security],
        "OnlineBackup": [online_backup],
        "DeviceProtection": [device_protection],
        "TechSupport": [tech_support],
        "StreamingTV": [streaming_tv],
        "StreamingMovies": [streaming_movies],
        "Contract": [contract],
        "PaperlessBilling": [paperless],
        "PaymentMethod": [payment],
        "MonthlyCharges": [monthly],
        "TotalCharges": [total]

    })


    # -------------------------------------------------
    # Encoding
    # -------------------------------------------------

    for col in customer_data.columns:

        if col in label_encoders:

            customer_data[col] = label_encoders[col].transform(
                customer_data[col]
            )



    # -------------------------------------------------
    # Scaling
    # -------------------------------------------------

    scaled_data = scaler.transform(customer_data)



       # -------------------------------------------------
    # ANN Prediction
    # -------------------------------------------------

    prediction_output = model.predict(scaled_data)

    probability = prediction_output[0][0]
    st.write("Prediction:", probability)

    test_input = scaled_data.copy()

    test_input[0][0] = test_input[0][0] + 5

    test_prediction = model.predict(test_input)[0][0]

    st.write("Prediction after changing first feature:", test_prediction)


    # Debug information
    st.write("Model Output:", probability)

    st.write("Scaled Input Shape:", scaled_data.shape)



    # -------------------------------------------------
    # Prediction Result
    # -------------------------------------------------

    if probability >= 0.5:

        result = "Customer Will Churn"

    else:

        result = "Customer Will Stay"



    # -------------------------------------------------
    # Risk Score
    # -------------------------------------------------

    risk_score = int(probability * 100)


    if risk_score >= 75:

        risk = "🔴 High Risk"

    elif risk_score >= 40:

        risk = "🟡 Medium Risk"

    else:

        risk = "🟢 Low Risk"



    # -------------------------------------------------
    # Revenue Risk
    # -------------------------------------------------

    revenue_risk = total * probability



    # -------------------------------------------------
    # Display Result
    # -------------------------------------------------

    st.markdown("---")

    st.header("📊 Prediction Result")


    c1, c2, c3, c4 = st.columns(4)


    with c1:

        st.success(result)


    with c2:

        st.info(
            f"Probability: {probability*100:.2f}%"
        )


    with c3:

        st.warning(
            f"Risk: {risk}"
        )


    with c4:

        st.metric(
            "Revenue at Risk",
            f"₹ {revenue_risk:.2f}"
        )



    # -------------------------------------------------
 # -------------------------------------------------
# Save Prediction into MySQL
# -------------------------------------------------
st.write("Gender selected:", gender)
prediction_data = (

    gender,
    senior,
    partner,
    dependents,
    tenure,
    phone,
    multiple,
    internet,
    contract,
    monthly,
    total,
    result,
    float(probability),
    risk,
    float(revenue_risk),

)

save_prediction(prediction_data)


st.success(
    "✅ Prediction saved to MySQL database"
)


# -------------------------------------------------
# AI Recommendation
# -------------------------------------------------

st.subheader(
    "🤖 AI Recommendation"
)


if contract == "Month-to-month":

    st.write(
        "✅ Offer long-term contract discounts to improve retention."
    )


if monthly > 80:

    st.write(
        "✅ Provide personalized pricing plans because monthly charges are high."
    )


if tech_support == "No":

    st.write(
        "✅ Recommend adding technical support service."
    )


if tenure < 12:

    st.write(
        "✅ Provide new customer engagement offers."
    )


if risk_score >= 75:

    st.write(
        "⚠️ Assign customer executive because customer has high churn probability."
    )

else:

    st.write(
        "✅ Continue loyalty programs for this customer."
    )


# -------------------------------------------------
# SHAP EXPLANATION
# -------------------------------------------------

st.markdown("---")

st.subheader(
    "🔍 Why is this customer at risk?"
)


try:

    shap_result = get_shap_explanation(
        model,
        scaled_data,
        scaled_data,
        customer_data.columns
    )


    st.write(
        "Top factors influencing prediction:"
    )


    st.dataframe(
        shap_result,
        width="stretch"
    )


except Exception as e:

    st.warning(
        "SHAP explanation could not be generated."
    )

    st.write(e)