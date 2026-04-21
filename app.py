import streamlit as st
import requests

st.set_page_config(page_title="Health Risk Predictor", layout="centered")

st.title("🩺 Health Risk Predictor")
st.write("Enter patient details below:")

# Inputs
pregnancies = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose Level", min_value=0.0)
blood_pressure = st.number_input("Blood Pressure", min_value=0.0)
skin_thickness = st.number_input("Skin Thickness", min_value=0.0)
insulin = st.number_input("Insulin", min_value=0.0)
bmi = st.number_input("BMI", min_value=0.0)
diabetes_pedigree = st.number_input("Diabetes Pedigree", min_value=0.0)
age = st.number_input("Age", min_value=0)

# Button
if st.button("Predict"):

    data = {
        "pregnancies": pregnancies,
        "glucose": glucose,
        "blood_pressure": blood_pressure,
        "skin_thickness": skin_thickness,
        "insulin": insulin,
        "bmi": bmi,
        "diabetes_pedigree": diabetes_pedigree,
        "age": age
    }

    try:
        response = requests.post(
            "https://health-risk-predictor-3wvi.onrender.com/predict",
            json=data
        )

        result = response.json()

        if "prediction" in result:
            if result["prediction"] == 1:
                st.error(f" High Risk (Probability: {result['probability']})")
            else:
                st.success(f"Low Risk (Probability: {result['probability']})")
        else:
            st.warning(result)

    except Exception as e:
        st.error(f"API connection failed: {e}")