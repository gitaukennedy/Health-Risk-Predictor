import streamlit as st
import os

# --- PATH CONFIG ---
# This looks for the 'assets' folder in the root directory (up one level from /pages)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

st.set_page_config(layout="wide", page_title="Precautions & Remedies")

st.title("❤️ Personalized Health Guidance")
st.warning("⚠️ Educational use only. Always consult a medical professional.")

# --- CHECK FOR DATA ---
if st.session_state.get("prediction") is None:
    st.info("👉 Please visit the **Predict** page first to generate your risk analysis.")
    st.stop()

prediction = st.session_state["prediction"]
prob = st.session_state["probability"]

# 📊 RESULT CARD
st.subheader("🧪 Your Health Summary")
col1, col2 = st.columns(2)
with col1:
    status = "High Risk" if prediction == 1 else "Low Risk"
    st.metric("Risk Level", status)
with col2:
    st.metric("Confidence Score", f"{prob*100:.1f}%")
st.progress(float(prob))

st.markdown("---")

# 🧠 REMEDIES & PRECAUTIONS
if prediction == 1:
    st.error("### 🛡 High Risk Detected: Immediate Precautions")
    
    # Use Tabs for a professional look
    tab1, tab2, tab3 = st.tabs(["🍎 Diet & Remedies", "🏃 Exercise & Habits", "🩺 Medical Practices"])
# ... inside the High Risk tab logic ...
    with tab1:
        st.subheader("Nutritional Guidance")
        img_path = os.path.join(ASSETS_DIR, "diet.jpg")
        if os.path.exists(img_path):
            # UPDATED PARAMETER HERE
            st.image(img_path, caption="Focus on high-fiber, low-sugar meals", width='stretch')
        
    with tab2:
        st.subheader("Lifestyle Adjustments")
        img_path = os.path.join(ASSETS_DIR, "exercise.jpg")
        if os.path.exists(img_path):
            # UPDATED PARAMETER HERE
            st.image(img_path, caption="Consistent, moderate movement", width='stretch')

    with tab3:
        st.subheader("Health Monitoring")
        img_path = os.path.join(ASSETS_DIR, "monitoring.jpg")
        if os.path.exists(img_path):
            # UPDATED PARAMETER HERE
            st.image(img_path, caption="Regular health checks", width='stretch')
else:
    st.success("### ✅ Low Risk Detected: Maintenance Mode")
    st.write("You're in good standing! Keep practicing these healthy habits to stay low-risk.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(os.path.join(ASSETS_DIR, "diet.jpg"), caption="Maintain a balanced diet")
    with col2:
        st.image(os.path.join(ASSETS_DIR, "exercise.jpg"), caption="Keep an active lifestyle")

st.markdown("---")
st.subheader("🌐 Trusted Sources")
st.markdown("[World Health Organization (WHO)](https://www.who.int/news-room/fact-sheets/detail/diabetes)")
st.markdown("[CDC Diabetes Resources](https://www.cdc.gov/diabetes/basics/index.html)")