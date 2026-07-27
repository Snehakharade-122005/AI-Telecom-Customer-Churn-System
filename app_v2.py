import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import time

from database import save_prediction
from model_utils import model, scaler, label_encoders
from shap_explanation import get_shap_explanation


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Telecom Customer Intelligence Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main{
    background-color:#F8FAFC;
}

.block-container{
    padding-top:2rem;
}

h1{
    color:#0F172A;
    font-weight:700;
}

h2,h3{
    color:#1E293B;
}


div[data-testid="metric-container"]{

    background:white;
    border-radius:12px;
    padding:15px;
    border:1px solid #E2E8F0;
    box-shadow:0px 3px 8px rgba(0,0,0,0.08);

}


.stButton>button{

    width:100%;
    height:55px;
    font-size:20px;
    border-radius:12px;
    background:#2563EB;
    color:white;
    font-weight:bold;

}


.stButton>button:hover{

    background:#1D4ED8;

}


section[data-testid="stSidebar"]{

    background:#0F172A;

}


</style>
""", unsafe_allow_html=True)



# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:


    st.title("🤖 AI Telecom")


    st.markdown("---")


    st.success(
        "Enterprise Customer Intelligence Platform"
    )


    st.markdown("---")


    st.markdown("""
    
### Modules

🏠 Home

👤 Customer Prediction

📊 Dashboard

📁 Bulk Prediction

👥 Customer Management

🤖 AI Insights

⚙ Settings


""")



# ============================================================
# HERO SECTION
# ============================================================


st.title(
    "📊 AI Telecom Customer Intelligence Platform"
)


st.markdown(
"""
### Predict • Analyze • Retain Customers using Artificial Intelligence
"""
)


st.write(
"""
This enterprise platform predicts customer churn using
Artificial Neural Network, calculates churn probability,
estimates revenue risk and provides AI-powered retention strategies.
"""
)


st.divider()



# ============================================================
# KPI CARDS
# ============================================================


k1,k2,k3,k4 = st.columns(4)


k1.metric(
    "Model",
    "TensorFlow ANN"
)


k2.metric(
    "Database",
    "MySQL"
)


k3.metric(
    "API",
    "FastAPI"
)


k4.metric(
    "Explainability",
    "SHAP AI"
)


st.divider()
# ============================================================
# CUSTOMER PROFILE SECTION
# ============================================================

st.header("👤 Customer Profile")


left, right = st.columns(2)



# ============================================================
# LEFT COLUMN
# ============================================================

with left:

    st.subheader("Personal Information")


    gender = st.selectbox(
        "Gender",
        ["Male","Female"]
    )


    senior = st.selectbox(
        "Senior Citizen",
        ["No","Yes"]
    )


    partner = st.selectbox(
        "Partner",
        ["No","Yes"]
    )


    dependents = st.selectbox(
        "Dependents",
        ["No","Yes"]
    )


    tenure = st.slider(
        "Customer Tenure (Months)",
        0,
        72,
        12
    )


    st.divider()


    st.subheader("Contract Details")


    contract = st.selectbox(
        "Contract Type",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )


    monthly = st.number_input(
        "Monthly Charges ($)",
        min_value=0.0,
        value=70.0
    )


    total = st.number_input(
        "Total Charges ($)",
        min_value=0.0,
        value=500.0
    )



# ============================================================
# RIGHT COLUMN
# ============================================================


with right:


    st.subheader("Services")


    internet = st.selectbox(
        "Internet Service",
        [
            "DSL",
            "Fiber optic",
            "No"
        ]
    )


    phone = st.selectbox(
        "Phone Service",
        [
            "Yes",
            "No"
        ]
    )


    multiple = st.selectbox(
        "Multiple Lines",
        [
            "No",
            "Yes",
            "No phone service"
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


    st.divider()


    st.subheader("Billing")


    payment = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )


    paperless = st.selectbox(
        "Paperless Billing",
        [
            "Yes",
            "No"
        ]
    )



# ============================================================
# PREDICTION BUTTON
# ============================================================


st.markdown("---")


st.header("🚀 AI Prediction Engine")


st.write(
    "Analyze customer churn probability using Artificial Intelligence."
)



predict = st.button(
    "🚀 Analyze Customer",
    use_container_width=True
)



# ============================================================
# DEFAULT VALUES (REMOVE NAME ERROR)
# ============================================================


probability = 0
result = ""
risk = ""
risk_score = 0
revenue_risk = 0
scaled_data = None
customer_data = None
# ============================================================
# PREDICTION PROCESS
# ============================================================


if predict:


    with st.spinner(
        "Analyzing customer using Artificial Intelligence..."
    ):


        time.sleep(2)



        # ====================================================
        # CREATE CUSTOMER DATAFRAME
        # ====================================================


        customer_data = pd.DataFrame({

            "gender":[gender],

            "SeniorCitizen":[
                1 if senior=="Yes" else 0
            ],

            "Partner":[partner],

            "Dependents":[dependents],

            "tenure":[tenure],

            "PhoneService":[phone],

            "MultipleLines":[multiple],

            "InternetService":[internet],

            "OnlineSecurity":[online_security],

            "OnlineBackup":[online_backup],

            "DeviceProtection":[device_protection],

            "TechSupport":[tech_support],

            "StreamingTV":[streaming_tv],

            "StreamingMovies":[streaming_movies],

            "Contract":[contract],

            "PaperlessBilling":[paperless],

            "PaymentMethod":[payment],

            "MonthlyCharges":[monthly],

            "TotalCharges":[total]

        })



        # ====================================================
        # LABEL ENCODING
        # ====================================================


        for col in customer_data.columns:


            if col in label_encoders:


                customer_data[col] = (
                    label_encoders[col]
                    .transform(customer_data[col])
                )



        # ====================================================
        # SCALING
        # ====================================================


        scaled_data = scaler.transform(
            customer_data
        )



        # ====================================================
        # MODEL PREDICTION
        # ====================================================


        probability = float(
            model.predict(scaled_data)[0][0]
        )



        result = (
            "Customer Will Churn"
            if probability >= 0.5
            else "Customer Will Stay"
        )



        risk_score = probability * 100


        revenue_risk = probability * total



        if risk_score >= 75:

            risk = "🔴 High Risk"


        elif risk_score >= 40:

            risk = "🟡 Medium Risk"


        else:

            risk = "🟢 Low Risk"



        # ====================================================
        # SAVE TO MYSQL
        # ====================================================


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
            probability,
            risk,
            revenue_risk

        )


        save_prediction(
            prediction_data
        )



        # ====================================================
        # EXECUTIVE DASHBOARD
        # ====================================================


        st.markdown("---")


        st.header(
            "📊 Executive Dashboard"
        )


        c1,c2,c3,c4 = st.columns(4)



        c1.metric(
            "Prediction",
            result
        )


        c2.metric(
            "Probability",
            f"{probability*100:.2f}%"
        )


        c3.metric(
            "Risk Level",
            risk
        )


        c4.metric(
            "Revenue At Risk",
            f"${revenue_risk:,.2f}"
        )



        # ====================================================
        # GAUGE CHART
        # ====================================================


        fig = go.Figure(

            go.Indicator(

                mode="gauge+number",

                value=risk_score,

                title={
                    "text":
                    "Customer Risk Score"
                },


                gauge={

                    "axis":{
                        "range":[0,100]
                    },

                    "steps":[

                        {
                        "range":[0,40],
                        "color":"lightgreen"
                        },

                        {
                        "range":[40,70],
                        "color":"gold"
                        },

                        {
                        "range":[70,100],
                        "color":"tomato"
                        }

                    ]

                }

            )

        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )



        # ====================================================
        # AI GENERATED INSIGHTS
        # ====================================================


        st.markdown("---")


        st.header(
            "🤖 AI Generated Business Insights"
        )


        if probability >= 0.75:


            st.error(
                "High churn probability detected."
            )


            st.write(
            """
            This customer is highly likely to leave.

            Immediate retention action is recommended.
            """
            )


        elif probability >= 0.50:


            st.warning(
                "Medium churn probability detected."
            )


            st.write(
            """
            Customer shows moderate churn risk.

            Retention offers should be considered.
            """
            )


        else:


            st.success(
                "Customer is likely to stay."
            )


            st.write(
            """
            Customer engagement is healthy.

            Continue loyalty programs.
            """
            )



        # ====================================================
        # RETENTION STRATEGY
        # ====================================================


        st.subheader(
            "🎯 Recommended Retention Strategy"
        )


        recommendations=[]



        if contract=="Month-to-month":

            recommendations.append(
                "Offer long-term contract discount."
            )


        if monthly > 80:

            recommendations.append(
                "Recommend a lower pricing plan."
            )


        if tech_support=="No":

            recommendations.append(
                "Provide free technical support."
            )


        if tenure < 12:

            recommendations.append(
                "Launch new customer welcome campaign."
            )


        if internet=="Fiber optic":

            recommendations.append(
                "Provide premium network stability offer."
            )


        if len(recommendations)==0:

            recommendations.append(
                "Customer is healthy. Continue loyalty rewards."
            )



        for item in recommendations:

            st.success(item)
                    # ====================================================
        # BUSINESS IMPACT
        # ====================================================


        st.markdown("---")


        st.header(
            "💰 Business Impact"
        )


        col1,col2 = st.columns(2)



        col1.metric(
            "Estimated Revenue At Risk",
            f"${revenue_risk:,.2f}"
        )



        saved_revenue = revenue_risk * 0.75



        col2.metric(
            "Potential Revenue Saved",
            f"${saved_revenue:,.2f}"
        )



        # ====================================================
        # AI EXPLAINABILITY
        # ====================================================


        st.markdown("---")


        st.header(
            "🧠 AI Explainability"
        )


        try:


            shap_result = get_shap_explanation(

                model,

                scaled_data,

                scaled_data,

                customer_data.columns

            )


            st.success(
                "Top Features Influencing Prediction"
            )


            st.dataframe(

                shap_result,

                use_container_width=True

            )


        except Exception:


            st.info(
                "SHAP explanation is currently unavailable."
            )



        # ====================================================
        # DOWNLOAD REPORT
        # ====================================================


        st.markdown("---")


        st.header(
            "📄 Download Prediction Report"
        )


        report = f"""

====================================
AI TELECOM CUSTOMER REPORT
====================================


Prediction:
{result}


Churn Probability:
{probability*100:.2f}%


Risk Level:
{risk}


Revenue At Risk:
${revenue_risk:.2f}



Customer Details
----------------

Gender:
{gender}


Senior Citizen:
{senior}


Partner:
{partner}


Dependents:
{dependents}


Tenure:
{tenure} months


Contract:
{contract}


Monthly Charges:
${monthly}


Total Charges:
${total}



====================================
Generated using AI Telecom Platform
====================================

"""


        st.download_button(

            label="⬇ Download Report",

            data=report,

            file_name="customer_prediction_report.txt",

            mime="text/plain"

        )



        # ====================================================
        # SESSION HISTORY
        # ====================================================


        st.markdown("---")


        st.header(
            "🕒 Current Session Prediction"
        )



        history = pd.DataFrame({

            "Prediction":[result],

            "Probability":[
                round(probability*100,2)
            ],

            "Risk":[risk],

            "Revenue Risk":[
                round(revenue_risk,2)
            ]

        })


        st.dataframe(

            history,

            use_container_width=True

        )



        # ====================================================
        # EXECUTIVE ANALYTICS
        # ====================================================


        st.markdown("---")


        st.header(
            "📈 Executive Analytics Dashboard"
        )


        chart1,chart2 = st.columns(2)



        with chart1:


            fig1 = go.Figure()



            fig1.add_trace(

                go.Bar(

                    x=["Churn Probability"],

                    y=[
                        probability*100
                    ],

                    text=[
                        f"{probability*100:.1f}%"
                    ],

                    textposition="outside"

                )

            )


            fig1.update_layout(

                title="Customer Churn Probability",

                yaxis_title="Percentage",

                height=400

            )


            st.plotly_chart(

                fig1,

                use_container_width=True

            )



        with chart2:


            safe_revenue = total - revenue_risk



            fig2 = go.Figure(

                data=[

                    go.Pie(

                        labels=[

                            "Revenue Safe",

                            "Revenue At Risk"

                        ],

                        values=[

                            safe_revenue,

                            revenue_risk

                        ],

                        hole=0.5

                    )

                ]

            )


            fig2.update_layout(

                title="Revenue Distribution",

                height=400

            )


            st.plotly_chart(

                fig2,

                use_container_width=True

            )



        # ====================================================
        # CUSTOMER HEALTH SCORE
        # ====================================================


        st.markdown("---")


        st.subheader(
            "💚 Customer Health Score"
        )



        health_score = 100 - risk_score



        st.progress(
            health_score / 100
        )



        st.metric(

            "Health Score",

            f"{health_score:.1f}%"

        )



        # ====================================================
        # AI DECISION SUMMARY
        # ====================================================


        st.markdown("---")


        st.subheader(
            "🧠 AI Decision Summary"
        )



        summary = f"""

Customer Prediction:
{result}


Overall Risk:
{risk}


Estimated Churn Probability:
{probability*100:.2f}%


Revenue At Risk:
${revenue_risk:.2f}


Recommended Action:
Use AI recommended retention strategy.

"""


        st.write(summary)



        if probability >= 0.75:


            st.error(
                "Immediately assign customer to retention team."
            )


        elif probability >= 0.50:


            st.warning(
                "Offer discounts and customer support."
            )


        else:


            st.success(
                "Customer is healthy. Continue loyalty rewards."
            )