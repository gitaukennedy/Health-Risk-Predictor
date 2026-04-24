import streamlit as st

st.set_page_config(
    page_title="Health Risk Predictor",
    page_icon="🩺",
    layout="wide"
)

# 🏥 HEADER
st.title("🩺 Health Risk Prediction System")

st.markdown("""
Welcome to your **AI-powered health assistant**.

This application helps you:
- 🧪 Predict diabetes risk
- ❤️ Learn symptoms & prevention
- 🏥 Find nearby hospitals
- 🛡 Explore health insurance options
""")

# 🔹 HERO SECTION
st.subheader("🚀 Get Started")

col1, col2 = st.columns(2)

with col1:
    st.info("👉 Go to **Predict** page to check your risk")

with col2:
    st.success("👉 Explore health resources from sidebar")

# 📊 QUICK INFO CARDS
st.subheader("📊 Why This App Matters")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Early Detection", value="Improves Outcomes")

with col2:
    st.metric(label="AI Assistance", value="Fast & Reliable")

with col3:
    st.metric(label="User Friendly", value="Simple Inputs")

# 🧠 MODEL INFO
st.subheader("🧠 About the Model")

st.write("""
This system uses a machine learning model trained on health data 
to estimate the probability of diabetes risk based on:

- Glucose level  
- BMI  
- Age  
- Blood pressure  
- Other health indicators  

⚠️ This tool is for **educational purposes only** and does not replace medical advice.
""")

# 🌍 QUICK LINKS
st.subheader("🌐 Quick Access")

st.markdown("[🏥 Find Hospitals](https://www.google.com/maps/search/hospitals+near+me)")
st.markdown("[📘 Diabetes Info - WHO](https://www.who.int/news-room/fact-sheets/detail/diabetes)")

# 📌 FOOTER
st.markdown("---")
st.caption("Built with ❤️ using Machine Learning, FastAPI & Streamlit")