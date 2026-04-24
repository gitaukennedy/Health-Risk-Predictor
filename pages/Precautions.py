import streamlit as st

st.title("❤️ Diabetes Awareness & Prevention")

# 🚨 Disclaimer
st.warning("⚠️ This information is for educational purposes only. Always consult a doctor.")

# 🔍 Symptoms
st.header("🔍 Common Symptoms")

st.write("""
- Frequent urination  
- Excessive thirst  
- Unexplained weight loss  
- Fatigue  
- Blurred vision  
""")

# 🛡 Prevention
st.header("🛡 Prevention Tips")

st.write("""
- Maintain a balanced diet  
- Exercise regularly  
- Monitor blood sugar  
- Avoid excessive sugar intake  
- Maintain healthy weight  
""")

# 🔗 External trusted resources
st.header("🌐 Learn More")

st.markdown("[WHO Diabetes Info](https://www.who.int/news-room/fact-sheets/detail/diabetes)")
st.markdown("[CDC Diabetes Guide](https://www.cdc.gov/diabetes/basics/index.html)")

# 💊 Medication info (SAFE VERSION)
st.header("💊 Common Treatment Types (Doctor Prescribed)")

st.write("""
These are commonly prescribed treatments (for awareness only):

- **Metformin** – helps control blood sugar  
- **Insulin therapy** – used in advanced cases  
""")

# 🖼 Images
st.image("assets/images/metformin.jpg", caption="Metformin (example)", use_column_width=True)
st.image("assets/images/insulin.jpg", caption="Insulin Injection", use_column_width=True)