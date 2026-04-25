import streamlit as st
import requests

st.set_page_config(page_title="Diabetes Risk Predictor", layout="wide")

st.title("🧪 Diabetes Risk Analysis")
st.markdown("---")

st.write("Please provide the following clinical indicators for a precise risk assessment.")

# --- INPUT SECTION: Organized into Columns for better UI ---
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Number of Pregnancies", min_value=0, step=1, help="Total number of pregnancies")
    glucose = st.number_input("Glucose Level (mg/dL)", min_value=0.0, help="Plasma glucose concentration")
    blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=0.0)
    skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0.0)

with col2:
    insulin = st.number_input("Insulin Level (mu U/ml)", min_value=0.0)
    bmi = st.number_input("Body Mass Index (BMI)", min_value=0.0, format="%.1f")
    diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f")
    age = st.number_input("Age (Years)", min_value=0, step=1)

st.markdown("---")

# --- PREDICTION LOGIC ---
if st.button("🚀 Run AI Diagnosis", use_container_width='stretch'):
    
    # Payload for the FastAPI backend
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

    with st.spinner("Connecting to Health-AI Server..."):
        try:
            # API Call
            response = requests.post(
                "https://health-risk-predictor-3wvi.onrender.com/predict",
                json=data,
                timeout=15 # Added timeout to prevent hanging
            )
            
            if response.status_code == 200:
                result = response.json()
                
                # STORE IN SESSION STATE: This connects to your Precautions page
                st.session_state["prediction"] = result.get("prediction")
                st.session_state["probability"] = result.get("probability", 0.0)

                # DISPLAY RESULTS
                if st.session_state["prediction"] == 1:
                    st.error(f"### ⚠️ High Risk Detected")
                    st.write(f"The model predicts a **{st.session_state['probability'] * 100:.1f}%** likelihood of diabetes.")
                    st.info("💡 **Action Required:** Go to the **Precautions** page in the sidebar for your personalized health plan.")
                else:
                    st.success(f"### ✅ Low Risk Detected")
                    st.write(f"The model predicts a **{st.session_state['probability'] * 100:.1f}%** likelihood of diabetes.")
                    st.balloons()
            
            else:
                st.error(f"Server Error: {response.status_code}. Please try again later.")

        except requests.exceptions.Timeout:
            st.error("The request timed out. The server might be waking up (Render free tier). Please wait a moment and try again.")
        except Exception as e:
            st.error(f"Connection failed: {e}")

# --- FOOTER ---
st.markdown("---")
st.caption("Data is processed securely. Prediction based on the Pima Indians Diabetes Dataset.")