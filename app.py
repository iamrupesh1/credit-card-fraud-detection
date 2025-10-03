import os
import joblib
import requests
import hashlib
import streamlit as st
import pandas as pd

# -------------------------
# MODEL DOWNLOAD SETTINGS
# -------------------------
MODEL_PATH = "model.pkl"
MODEL_URL = "https://github.com/iamrupesh1/credit-card-fraud-detection/releases/download/v1.0/model.pkl"
MODEL_SHA256 = "9f8770092e3b8461a1ac34100db56b52d5e5d6180c7c63a7ddaca4038a3f613c"

def download_model():
    """Download the model from GitHub release if it does not exist."""
    if not os.path.exists(MODEL_PATH):
        st.info("Downloading model...")
        r = requests.get(MODEL_URL, stream=True)
        with open(MODEL_PATH, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

        # Verify SHA256
        sha256_hash = hashlib.sha256()
        with open(MODEL_PATH,"rb") as f:
            for byte_block in iter(lambda: f.read(4096),b""):
                sha256_hash.update(byte_block)

        if sha256_hash.hexdigest() != MODEL_SHA256:
            st.error("Downloaded model checksum does not match!")
            raise ValueError("Model file corrupted during download!")
        st.success("Model downloaded and verified!")

# -------------------------
# LOAD MODEL
# -------------------------
download_model()
model = joblib.load(MODEL_PATH)

# -------------------------
# STREAMLIT UI
# -------------------------
st.set_page_config(page_title="💳 Credit Card Fraud Detection", layout="centered")
st.title("💳 Credit Card Fraud Detection")
st.write("Enter transaction details (Amount + optional V1-V28). Optional fields can be left blank; zeros will be used automatically.")

# Build input form dynamically
features = ['V'+str(i) for i in range(1,29)] + ['Amount']
input_data = {}

with st.form("transaction_form"):
    for feature in features:
        input_data[feature] = st.number_input(f"{feature} (optional, press Enter for 0):", value=0.0)
    submitted = st.form_submit_button("Predict")

# -------------------------
# PREDICTION FUNCTION
# -------------------------
def predict_fraud(input_dict):
    df = pd.DataFrame([input_dict])
    pred = model.predict(df)[0]
    pred_proba = model.predict_proba(df)[0][1]  # Fraud probability
    return {"Prediction": "Fraud" if pred==1 else "Normal", "Fraud Probability": round(pred_proba*100,2)}

# -------------------------
# SHOW RESULT
# -------------------------
if submitted:
    result = predict_fraud(input_data)
    if result["Prediction"] == "Fraud":
        st.error(f"⚠️ Transaction is Fraudulent!\nProbability of Fraud: {result['Fraud Probability']}%")
    else:
        st.success(f"✅ Transaction is Normal\nProbability of Fraud: {result['Fraud Probability']}%")
