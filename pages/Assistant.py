import streamlit as st
import os

# 1. PAGE CONFIG (Must be the first Streamlit command)
st.set_page_config(page_title="AI Health Assistant", page_icon="🤖", layout="wide")

# 2. PATH CONFIG FOR IMAGES
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# 3. INITIALIZE SESSION STATE
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your Health AI. I can explain your risk levels, suggest diet plans, or explain diabetes symptoms. How can I help you today?"}
    ]

# Safely get prediction data
prediction = st.session_state.get("prediction", None)
prob = st.session_state.get("probability", 0.0)

# --- UI LAYOUT ---
st.title("🤖 Clinical AI Assistant")
st.caption("Empowering your health journey with AI-driven insights.")
st.warning("⚠️ Educational use only. Not a substitute for professional medical advice.")

# --- KNOWLEDGE BASE ---
KNOWLEDGE = {
    "diet": {
        "text": "For diabetes management, the **Plate Method** is key: 50% non-starchy veggies, 25% lean protein, and 25% whole grains. Focus on fiber to slow sugar absorption.",
        "image": "diet.jpg"
    },
    "symptoms": {
        "text": "Watch for the '3 Polys': **Polyuria** (frequent urination), **Polydipsia** (excessive thirst), and **Polyphagia** (extreme hunger). Also, watch for blurred vision.",
        "image": "monitoring.jpg"
    },
    "medication": {
        "text": "Common medications include **Metformin** and **Insulin**. These help manage how your body processes sugar. Always consult a doctor for prescriptions.",
        "image": "monitoring.jpg"
    }
}

# --- ASSISTANT LOGIC FUNCTION ---
def generate_ai_response(user_input):
    query = user_input.lower()
    
    # A. Handle Gratitude & Social
    if any(word in query for word in ["thank", "thanks", "ok", "cool", "bye"]):
        return "You're very welcome! Stay proactive with your health. Anything else you need?", None

    # B. Handle "What are you?" questions
    if any(word in query for word in ["what kind", "who are you", "chatbot", "ai"]):
        return "I am a **Clinical Decision Support Assistant**. I analyze your health metrics (like your current risk) and provide guidance based on WHO and ADA medical standards.", None

    # C. Handle Risk Specifics
    if "risk" in query or "result" in query:
        if prediction is not None:
            status = "High" if prediction == 1 else "Low"
            msg = f"Your current analysis shows a **{status} Risk** (Probability: {prob*100:.1f}%). "
            if prediction == 1:
                msg += "This suggests you should monitor your glucose levels closely and consult a professional."
            else:
                msg += "This is a great result! Keep maintaining your current lifestyle habits."
            return msg, None
        return "I don't see your prediction yet. Please complete the analysis on the **Predict** page first!", None

    # D. Handle Health Knowledge
    for key in KNOWLEDGE:
        if key in query:
            return KNOWLEDGE[key]["text"], KNOWLEDGE[key]["image"]

    # E. Fallback
    return "I can provide detailed info on your diet, symptoms, medications, or your risk result. Could you clarify which you'd like to discuss?", None

# --- CHAT INTERFACE ---
# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("image"):
            img_path = os.path.join(ASSETS_DIR, msg["image"])
            if os.path.exists(img_path):
                st.image(img_path, width='stretch')

# Chat Input
if prompt := st.chat_input("Ask me a health question..."):
    # User message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant message
    with st.chat_message("assistant"):
        response_text, image_file = generate_ai_response(prompt)
        st.markdown(response_text)
        
        # Handle Image Display
        if image_file:
            img_path = os.path.join(ASSETS_DIR, image_file)
            if os.path.exists(img_path):
                st.image(img_path, width='stretch')
        
        # Save to history
        st.session_state.messages.append({
            "role": "assistant", 
            "content": response_text, 
            "image": image_file
        })