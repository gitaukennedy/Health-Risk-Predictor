import streamlit as st

st.set_page_config(
    page_title="Health AI Hub",
    page_icon="🩺",
    layout="wide"
)

# --- INITIALIZE SESSION STATE ---
if "prediction" not in st.session_state:
    st.session_state["prediction"] = None
if "probability" not in st.session_state:
    st.session_state["probability"] = 0.0

# --- HERO SECTION ---
st.title("🩺 Health Risk Prediction System")
st.markdown("---")

col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("Your AI-Powered Preventative Health Suite")
    st.write("""
        Empowering patients with data-driven insights. Our system analyzes clinical indicators 
        to identify early warning signs of diabetes, helping you take control of your future.
    """)
    
    # Direct Navigation Buttons
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🚀 Run Risk Assessment", width='stretch'):
            st.switch_page("pages/Predict.py")
    with c2:
        if st.button("🤖 Talk to Health AI", width='stretch'):
            st.switch_page("pages/Assistant.py")

with col_right:
    st.image("https://images.unsplash.com/photo-1576091160550-2173dad99962?w=800", width='stretch')

st.markdown("---")

# --- DASHBOARD METRICS ---
st.subheader("📊 Performance & Utility")
m1, m2, m3 = st.columns(3)
m1.metric(label="System Reliability", value="High", delta="AI Verified")
m2.metric(label="Processing Speed", value="< 2s", delta="Real-time")
m3.metric(label="User Accessibility", value="Global", delta="24/7 Available")

# --- FEATURES ---
st.subheader("🌐 Explore the Ecosystem")
f1, f2, f3 = st.columns(3)

with f1:
    with st.container(border=True):
        st.write("🏥 **Facility Finder**")
        st.write("Locate the nearest emergency care and specialized hospitals.")
        if st.button("View Map", key="hosp_btn"):
            st.switch_page("pages/Hospitals.py")

with f2:
    with st.container(border=True):
        st.write("🛡️ **Insurance Support**")
        st.write("Find diabetes-specific coverage and financial aid programs.")
        if st.button("Explore Plans", key="ins_btn"):
            st.switch_page("pages/Insurance.py")

with f3:
    with st.container(border=True):
        st.write("📘 **Knowledge Base**")
        st.write("Understand the clinical science behind your prediction results.")
        if st.button("Read More", key="about_btn"):
            st.switch_page("pages/About.py")

st.markdown("---")
st.caption("Built with ❤️ using Machine Learning, FastAPI & Streamlit | 2026 Edition")