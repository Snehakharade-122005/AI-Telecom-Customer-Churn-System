import os
import joblib
from tensorflow.keras.models import load_model


# -------------------------------------------------
# Load Model, Scaler and Label Encoders
# -------------------------------------------------

def load_resources():

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    MODEL_PATH = os.path.join(
        BASE_DIR,
        "models",
        "customer_churn_ann.keras"
    )

    SCALER_PATH = os.path.join(
        BASE_DIR,
        "models",
        "scaler.pkl"
    )

    ENCODER_PATH = os.path.join(
        BASE_DIR,
        "models",
        "label_encoders.pkl"
    )

    # -------------------------------------------------
    # Debug paths
    # -------------------------------------------------

    print("Model Path:", MODEL_PATH)
    print("Scaler Path:", SCALER_PATH)
    print("Encoder Path:", ENCODER_PATH)

    # -------------------------------------------------
    # Check files exist
    # -------------------------------------------------

    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("❌ Model file not found")

    if not os.path.exists(SCALER_PATH):
        raise FileNotFoundError("❌ Scaler file not found")

    if not os.path.exists(ENCODER_PATH):
        raise FileNotFoundError("❌ Encoder file not found")

    # -------------------------------------------------
    # Load TensorFlow Model
    # -------------------------------------------------

    model = load_model(
        MODEL_PATH,
        compile=False
    )

    # -------------------------------------------------
    # Load Scaler
    # -------------------------------------------------

    scaler = joblib.load(SCALER_PATH)

    # -------------------------------------------------
    # Load Encoders
    # -------------------------------------------------

    label_encoders = joblib.load(ENCODER_PATH)

    # -------------------------------------------------
    # Debug Information
    # -------------------------------------------------

    print("✅ Model Loaded")
    print("Scaler Features:", scaler.n_features_in_)
    print("Encoders:", label_encoders.keys())

    return model, scaler, label_encoders


# -------------------------------------------------
# Initialize Resources
# -------------------------------------------------

model, scaler, label_encoders = load_resources()