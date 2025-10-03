import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load("model.pkl")

# Feature names
features = ['Time'] + [f'V{i}' for i in range(1,29)] + ['Amount']

st.title("💳 Credit Card Fraud Detection")
st.write("Enter transaction details (Amount + optional V1-V28). Optional features can be left blank; zeros will be used automatically.")

# Input fields
user_input = {}
user_input['Time'] = 0  # default

user_input['Amount'] = st.number_input("Transaction Amount", min_value=0.0, value=0.0)

for i in range(1,29):
    user_input[f'V{i}'] = st.number_input(f"V{i} (optional)", value=0.0)

# Predict button
if st.button("Predict"):
    # Convert to DataFrame
    input_df = pd.DataFrame([user_input], columns=features)

    # Prediction
    prediction = model.predict(input_df)[0]
    prediction_proba = model.predict_proba(input_df)[0][1]  # Fraud probability

    status = "Fraud" if prediction == 1 else "Normal"

    st.success(f"✅ Transaction is {status}")
    st.info(f"Probability of Fraud: {prediction_proba*100:.2f} %")
