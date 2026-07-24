import streamlit as st
import pandas as pd

from model_utils import model, scaler, label_encoders


# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="AI Telecom Bulk Prediction",
    page_icon="📂",
    layout="wide"
)


# -------------------------------------------------
# TITLE
# -------------------------------------------------

st.title("📂 AI Telecom Bulk Customer Prediction")

st.markdown("---")


st.write(
"""
Upload multiple telecom customer records using a CSV file.

The AI system will predict:
- Customer Churn
- Churn Probability
- Risk Level
- Revenue at Risk
"""
)


st.markdown("---")


# -------------------------------------------------
# FILE UPLOAD
# -------------------------------------------------

uploaded_file = st.file_uploader(
    "📁 Upload Customer CSV File",
    type=["csv"]
)


# -------------------------------------------------
# MAIN PROGRAM
# -------------------------------------------------

if uploaded_file is not None:


    df = pd.read_csv(uploaded_file)


    st.success("✅ File Uploaded Successfully")


    st.subheader("📋 Customer Data Preview")


    st.dataframe(
        df,
        width="stretch"
    )


    st.info(
        f"Total Customers Uploaded: {len(df)}"
    )


    st.markdown("---")


    predict_button = st.button(
        "🚀 Predict All Customers"
    )
        # -------------------------------------------------
    # DATA PREPROCESSING AND PREDICTION
    # -------------------------------------------------

    if predict_button:


        prediction_df = df.copy()


        # Save customer IDs for output
        if "customerID" in prediction_df.columns:

            customer_ids = prediction_df["customerID"]

        else:

            customer_ids = None



        # Remove columns not required for prediction

        if "customerID" in prediction_df.columns:

            prediction_df = prediction_df.drop(
                "customerID",
                axis=1
            )


        # Remove target column if uploaded

        if "Churn" in prediction_df.columns:

            prediction_df = prediction_df.drop(
                "Churn",
                axis=1
            )



        # Convert TotalCharges to numeric

        if "TotalCharges" in prediction_df.columns:

            prediction_df["TotalCharges"] = pd.to_numeric(
                prediction_df["TotalCharges"],
                errors="coerce"
            )


            prediction_df["TotalCharges"] = (
                prediction_df["TotalCharges"]
                .fillna(0)
            )



        # Apply Label Encoding

        for column in prediction_df.columns:


            if column in label_encoders:


                prediction_df[column] = label_encoders[column].transform(
                    prediction_df[column]
                )



        # Scale Data

        scaled_data = scaler.transform(
            prediction_df
        )


        st.success(
            "✅ Data preprocessing completed"
        )



        # -------------------------------------------------
        # MODEL PREDICTION
        # -------------------------------------------------

        probability = model.predict(
            scaled_data
        )


        probability = probability.flatten()


        results = df.copy()


        results["Probability"] = (
            probability * 100
        ).round(2)



        results["Prediction"] = results["Probability"].apply(
            lambda x:
            "Customer Will Churn"
            if x >= 50
            else
            "Customer Will Stay"
        )
                # -------------------------------------------------
        # RISK LEVEL
        # -------------------------------------------------

        def calculate_risk(probability):

            if probability >= 75:

                return "🔴 High Risk"

            elif probability >= 40:

                return "🟡 Medium Risk"

            else:

                return "🟢 Low Risk"



        results["Risk"] = results["Probability"].apply(
            calculate_risk
        )



        # -------------------------------------------------
        # REVENUE AT RISK
        # -------------------------------------------------

        results["Revenue at Risk"] = (
            results["MonthlyCharges"]
            *
            (results["Probability"] / 100)
        ).round(2)



        # -------------------------------------------------
        # DISPLAY RESULTS
        # -------------------------------------------------

        st.markdown("---")


        st.subheader(
            "📊 Bulk Prediction Results"
        )


        st.dataframe(
            results,
            width="stretch"
        )



        # Summary

        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "Total Customers",
                len(results)
            )


        with col2:

            churn_count = len(
                results[
                    results["Prediction"]
                    ==
                    "Customer Will Churn"
                ]
            )

            st.metric(
                "Customers Churned",
                churn_count
            )


        with col3:

            avg_probability = results[
                "Probability"
            ].mean()

            st.metric(
                "Average Risk %",
                f"{avg_probability:.2f}%"
            )



        # -------------------------------------------------
        # DOWNLOAD RESULTS
        # -------------------------------------------------

        csv = results.to_csv(
            index=False
        ).encode("utf-8")


        st.download_button(

            label="📥 Download Prediction Results",

            data=csv,

            file_name="bulk_prediction_results.csv",

            mime="text/csv"

        )


        st.success(
            "✅ Bulk Prediction Completed Successfully"
        )


else:

    st.warning(
        "Please upload a CSV file to continue."
    )