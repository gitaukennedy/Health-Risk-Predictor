import streamlit as st

st.set_page_config(page_title="Technical Architecture", page_icon="📘", layout="centered")

st.title("📘 Project Architecture")

st.markdown("""
### 🧠 The Intelligence Layer: Random Forest Classifier
Unlike simple linear models, this system utilizes a **Random Forest Ensemble**. By aggregating the results of multiple decision trees, the model achieves higher stability and handles non-linear relationships in health data with superior accuracy.

**Why Random Forest?**
* **Reduced Overfitting:** Averaging multiple trees ensures the model generalizes well to new patients.
* **Feature Importance:** It allows us to see exactly which health metrics (like Glucose or BMI) drive the risk score.
* **Non-Linear Complexity:** It effectively captures the complex interactions between insulin levels and age.
""")



st.markdown("---")

# --- TECHNICAL SPECS ---
st.subheader("⚙️ Modern Technology Stack")
col1, col2 = st.columns(2)

with col1:
    st.write("**Model Engineering**")
    st.code("""
# Model: RandomForestClassifier
# Framework: Scikit-Learn
# Optimizer: GridSearchCV
    """)

with col2:
    st.write("**System Infrastructure**")
    st.code("""
# API: FastAPI (Python)
# UI: Streamlit (2026 Build)
# Hosting: Render / Cloud
    """)

# --- DATA SCHEMA ---
st.subheader("📊 Pima Indians Dataset Schema")
st.write("The AI analyzes 8 primary clinical dimensions to calculate your risk percentage:")

st.table({
    "Clinical Metric": ["Glucose", "BMI", "Insulin", "Age", "Pregnancies", "Blood Pressure", "Skin Thickness", "Pedigree"],
    "Analysis Role": ["Primary Driver", "High Impact", "High Impact", "Secondary", "Historical", "Baseline", "Secondary", "Genetic"]
})

st.markdown("---")

# --- DISCLAIMER ---
st.warning("""
**⚠️ Medical Disclaimer:** This application is an educational Machine Learning project. The predictions are based on statistical patterns in data and should NOT be taken as a medical diagnosis. Always consult a licensed endocrinologist.
""")

st.caption("Developed as an end-to-end ML deployment project 🚀 | April 2026")