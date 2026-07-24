import os
import joblib
from tensorflow.keras.models import load_model


# -------------------------------------------------
# Load Model, Scaler and Label Encoders
# -------------------------------------------------

def load_resources():

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))


    model_path = os.path.join(
        BASE_DIR,
        "models",
        "customer_churn_ann.keras"
    )


    scaler_path = os.path.join(
        BASE_DIR,
        "models",
        "scaler.pkl"
    )


    encoder_path = os.path.join(
        BASE_DIR,
        "models",
        "label_encoders.pkl"
    )


    # Load TensorFlow ANN Model
    model = load_model(model_path)


    # Load StandardScaler
    scaler = joblib.load(scaler_path)


    # Load Label Encoders
    label_encoders = joblib.load(encoder_path)


    return model, scaler, label_encoders



# Initialize resources

model, scaler, label_encoders = load_resources()