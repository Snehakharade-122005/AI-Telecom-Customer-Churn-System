from fastapi import FastAPI
from pydantic import BaseModel

from model_utils import model, scaler, label_encoders

import pandas as pd


# -------------------------------------------------
# Create API
# -------------------------------------------------

app = FastAPI(
    title="AI Telecom Customer Churn API",
    description="TensorFlow ANN based churn prediction API",
    version="1.0"
)


# -------------------------------------------------
# Input Data Format
# -------------------------------------------------

class CustomerData(BaseModel):

    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float



# -------------------------------------------------
# Home API
# -------------------------------------------------

@app.get("/")
def home():

    return {
        "message":
        "AI Telecom Customer Churn API Running Successfully"
    }



# -------------------------------------------------
# Prediction API
# -------------------------------------------------

@app.post("/predict")
def predict_customer(data: CustomerData):


    customer = pd.DataFrame(
        [data.dict()]
    )


    # Encoding

    for col in customer.columns:

        if col in label_encoders:

            customer[col] = label_encoders[col].transform(
                customer[col]
            )


    # Scaling

    scaled = scaler.transform(
        customer
    )


    # Prediction

    probability = model.predict(
        scaled
    )[0][0]


    if probability >= 0.5:

        prediction = "Customer Will Churn"

    else:

        prediction = "Customer Will Stay"



    risk_score = probability * 100


    if risk_score >= 75:

        risk = "High Risk"

    elif risk_score >= 40:

        risk = "Medium Risk"

    else:

        risk = "Low Risk"



    return {

        "prediction": prediction,

        "probability":
        round(float(probability*100),2),

        "risk":
        risk

    }