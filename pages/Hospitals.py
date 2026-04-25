import streamlit as st
import os

st.set_page_config(page_title="Global Emergency Hub", page_icon="🏥", layout="wide")

st.title("🏥 Global Hospital & Emergency Locator")
st.markdown("---")

# 1. GLOBAL EMERGENCY DATABASE
# Standardized global emergency codes for the dynamic matcher
GLOBAL_REGIONS = {
    "kenya": {"code": "999 / 112", "ambulance": "Red Cross: 1501 / 112"},
    "usa": {"code": "911", "ambulance": "EMS: 911"},
    "uk": {"code": "999 / 111", "ambulance": "NHS: 999"},
    "india": {"code": "112", "ambulance": "Ambulance: 102 / 108"},
    "nigeria": {"code": "112 / 199", "ambulance": "NEMA: 0800"},
    "south africa": {"code": "10111", "ambulance": "Netcare: 911"}
}

# 2. SEARCH INTERFACE
st.subheader("🌍 Enter Your Current Location")
user_input = st.text_input(
    "City, State, or Country", 
    placeholder="e.g. Westlands, Nairobi or Brooklyn, NY",
    help="Type your location to find nearby hospitals and correct emergency codes."
)

if user_input:
    # --- DYNAMIC MATCHING LOGIC ---
    input_lower = user_input.lower()
    selected_contact = {"code": "112 / 911", "ambulance": "Local Dispatch"} # Global Default
    
    # Matching the typed location to our global database
    for country, info in GLOBAL_REGIONS.items():
        if country in input_lower:
            selected_contact = info
            break

    # 3. DYNAMIC LAYOUT
    col1, col2 = st.columns([2, 1])

    with col1:
        st.success(f"📍 Mapping Emergency Facilities in {user_input}")
        
        # We search specifically for "Emergency Hospitals" to ensure active ERs show up
        search_query = f"Emergency Hospitals and Ambulances in {user_input}".replace(" ", "+")
        
        # UPDATED: Using the new st.iframe (Replaces st.components.v1.iframe)
        map_embed_url = f"https://www.google.com/maps/embed/v1/search?key=YOUR_API_KEY&q={search_query}" 
        # Note: If no API key, we use the public preview format:
        public_map_url = f"https://maps.google.com/maps?q={search_query}&output=embed"
        
        st.iframe(public_map_url, height=500)
        
        st.markdown(f"👉 [Open Direct Hospital Directory for {user_input}](https://www.google.com/maps/search/{search_query})")

    with col2:
        # 4. EMERGENCY CONTACT CARD
        st.error(f"### 🚨 {user_input.split(',')[0].strip().title()} Emergency")
        
        st.markdown(f"""
        **Primary Emergency Line:**
        ## {selected_contact['code']}
        
        **Ambulance & Medical:**
        #### {selected_contact['ambulance']}
        """)
        
        st.markdown("---")
        st.subheader("📞 Local Facility Contacts")
        st.write("To call a specific hospital directly:")
        st.markdown("1. Click a hospital pin on the map.")
        st.markdown("2. Select **'Call'** in the information panel.")
        st.markdown("3. For private ambulances, check the Red Cross or local provider links.")

else:
    st.info("Please enter a location to load the regional emergency infrastructure.")

# 5. CLINICAL EMERGENCY GUIDE
st.markdown("---")
with st.expander("🛑 How to identify a Diabetic Emergency"):
    st.write("If you or someone nearby is diabetic and shows these signs, use the emergency numbers above immediately:")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Hyperglycemia (High Sugar / DKA)**")
        st.write("- Fruity-smelling breath\n- Extreme thirst & frequent urination\n- Nausea or vomiting")
    with c2:
        st.markdown("**Hypoglycemia (Low Sugar / Insulin Shock)**")
        st.write("- Confusion or sudden irritability\n- Shakiness and cold sweats\n- Loss of consciousness")
    
    

st.caption("Updated April 2026 | Location services powered by Google Maps")