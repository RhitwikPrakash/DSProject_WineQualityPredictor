import streamlit as st
import numpy as np
import joblib
from pathlib import Path

# MUST BE FIRST STREAMLIT COMMAND
st.set_page_config(page_title="Wine Quality Predictor", layout="centered")

# Load model
@st.cache_resource
def load_model():
    return joblib.load("model.joblib")

model = load_model()

st.title("🍷 Wine Quality Predictor")
st.markdown("Enter wine chemical properties to predict quality:")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    with col1:
        fixed_acidity = st.number_input("Fixed Acidity", value=7.0)
        citric_acid = st.number_input("Citric Acid", value=0.25)
        chlorides = st.number_input("Chlorides", value=0.05)
        total_sulphur_dioxide = st.number_input("Total Sulphur Dioxide", value=120.0)
        pH = st.number_input("pH", value=3.3)
        alcohol = st.number_input("Alcohol", value=10.0)
    with col2:
        volatile_acidity = st.number_input("Volatile Acidity", value=0.7)
        residual_sugar = st.number_input("Residual Sugar", value=2.0)
        free_sulphur_dioxide = st.number_input("Free Sulphur Dioxide", value=30.0)
        density = st.number_input("Density", value=0.996)
        sulphates = st.number_input("Sulphates", value=0.6)

    submit = st.form_submit_button("Predict")

if submit:
    input_data = np.array([[
        fixed_acidity, volatile_acidity, citric_acid,
        residual_sugar, chlorides, free_sulphur_dioxide,
        total_sulphur_dioxide, density, pH, sulphates, alcohol
    ]])
    prediction = model.predict(input_data)[0]
    st.success(f"🎯 Predicted Wine Quality: **{round(prediction, 2)}**")
