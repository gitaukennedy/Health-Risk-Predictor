import streamlit as st

st.title("🏥 Find Nearby Hospitals")

st.write("Search for hospitals based on your location.")

# 📍 USER INPUT
location = st.text_input("Enter your location (e.g., Nairobi, Westlands)")

if location:
    query = location.replace(" ", "+")
    maps_url = f"https://www.google.com/maps/search/hospitals+in+{query}"

    st.success(f"Showing hospitals near: {location}")

    st.markdown(f"[🔎 Open in Google Maps]({maps_url})")

    # Embed map preview
    st.components.v1.iframe(
        f"https://www.google.com/maps?q=hospitals+in+{query}&output=embed",
        height=400
    )

# 🚑 Emergency Info
st.subheader("🚑 Emergency Contacts")

st.write("""
- Kenya Emergency: **999 / 112**  
- Ambulance Services: **911 (Private Providers)**  
""")

st.info("In case of emergency, call immediately.")