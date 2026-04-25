import streamlit as st
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Diabetes Insurance Support", page_icon="🛡️", layout="wide")

st.title("🛡️ Diabetes Insurance & Financial Support")
st.markdown("---")

# --- 1. DYNAMIC REGIONAL DATA ---
# This dictionary links users to policies that specifically cover pre-existing diabetes
REGIONAL_DATA = {
    "Kenya": {
        "statutory": "Social Health Authority (SHA/SHIF)",
        "statutory_link": "https://sha.go.ke/",
        "private_providers": [
            {"name": "Jubilee Health (J-Care Premium)", "note": "Covers chronic illness after 12-month waiting period.", "link": "https://jubileeinsurance.com/ke/"},
            {"name": "Britam (Bima ya Mwananchi)", "note": "Affordable inpatient/outpatient for chronic conditions.", "link": "https://ke.britam.com/"},
            {"name": "AAR Insurance", "note": "Offers specialized chronic disease management programs.", "link": "https://aar-insurance.com/"}
        ],
        "emergency_fund": "SHA Critical Illness Fund (for catastrophic diabetes complications)"
    },
    "International": {
        "statutory": "Varies by Country",
        "statutory_link": "#",
        "private_providers": [
            {"name": "Cigna Global (Platinum Plan)", "note": "Comprehensive global coverage for pre-existing conditions.", "link": "https://www.cignaglobal.com/"},
            {"name": "Allianz Care", "note": "World-class chronic condition support and drug delivery.", "link": "https://www.allianzcare.com/"},
            {"name": "Bupa Global", "note": "Elite tier plans with specialized endocrine consultations.", "link": "https://www.bupaglobal.com/"}
        ],
        "emergency_fund": "Check local government health mandates"
    }
}

# --- 2. USER INTERACTION ---
st.subheader("🔎 Find Coverage in Your Region")
region = st.selectbox("Select your region to see specific diabetes policies:", ["Kenya", "International"])

current_data = REGIONAL_DATA[region]

col1, col2 = st.columns(2)

with col1:
    st.info(f"### 🏛️ {region} National Support")
    st.write(f"The primary government cover in your area is: **{current_data['statutory']}**")
    st.markdown(f"[Register / Access {current_data['statutory']}]({current_data['statutory_link']})")
    
    if region == "Kenya":
        st.write("**2026 Update:** NHIF has been replaced by SHA. Ensure you have completed 'Means Testing' on the Afya Yangu portal to access Level 4-6 hospital benefits.")

with col2:
    st.success(f"### 🏥 Recommended Private Providers ({region})")
    for provider in current_data['private_providers']:
        st.markdown(f"**[{provider['name']}]({provider['link']})**")
        st.caption(provider['note'])

st.markdown("---")

# --- 3. DIABETES SPECIFIC RIDERS ---
st.subheader("💡 What to Look For in a Policy")
st.write("When choosing a plan for diabetes, ensure it includes these three critical components:")

tab1, tab2, tab3 = st.tabs(["💊 Medication Coverage", "🧪 Lab Benefits", "🏃 Wellness Programs"])

with tab1:
    st.markdown("""
    **Check for Insulin & Oral Drug Coverage:**
    * Does the plan cover CGM (Continuous Glucose Monitors)?
    * Are insulin pumps included or excluded?
    * Is there a 'Drug Delivery' service to your home?
    """)
    

with tab2:
    st.markdown("""
    **Diagnostic Support:**
    * Ensure the plan covers **HbA1c tests** (at least 4 times a year).
    * Look for coverage for renal (kidney) function and retinal (eye) screenings.
    """)

with tab3:
    st.markdown("""
    **Chronic Management Programs:**
    * Many modern 2026 plans (like Jubilee's *Maisha Fiti*) offer free glucose strips and nutrition coaching.
    * These programs are often 'Value Added Services' that don't deduct from your outpatient limit.
    """)

# --- 4. CALL TO ACTION ---
st.info("📣 **Pro Tip:** Always declare your diabetes diagnosis during the application. Underwriting in 2026 is stricter; non-disclosure can lead to claim rejection even after years of paying premiums.")

st.caption("Last Updated: April 2026 | Built to support Universal Health Coverage (UHC) goals.")