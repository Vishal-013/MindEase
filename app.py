import time
import streamlit as st
from utils.ai_utils import get_ai_response   # now uses Gemini
from utils.mi_utils import get_assessment_feedback

# --- Page Config ---
st.set_page_config(
    page_title="Mindful Me 🧠",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS Styling ---
st.markdown("""
<style>
    .reportview-container { background: #f0f2f6; }
    .main .block-container { padding-top: 1rem; padding-bottom: 1rem; }
    h1, h2 { font-family: 'Inter', sans-serif; color: #2c3e50; text-align: center; }
    .stButton>button {
        background-color: #3498db; color: white; border-radius: 12px; border: none;
        padding: 10px 24px; font-size: 16px;
        transition: all 0.3s ease; box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        background-color: #2980b9; transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0,0,0,0.15);
    }
</style>
""", unsafe_allow_html=True)

# --- Session State ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "assessment_submitted" not in st.session_state:
    st.session_state.assessment_submitted = False

# --- Homepage ---
st.title("💖 Mindful Me: Your AI Mental Wellness Companion")
st.image("assets/logo.jpg", width=120)
st.markdown("""
Welcome to **Mindful Me** 🌱  
A safe, youth-friendly space to check in with your feelings, chat with AI, and reflect on your well-being.  
""")

# --- Layout ---
tab1, tab2, tab3 = st.tabs(["💬 Chat", "📝 Assessment", "📚 Resources"])

# --- Chat Tab ---
with tab1:
    st.subheader("Chat with Mindful Me (Powered by Gemini ✨)")
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    user_input = st.chat_input("How are you feeling today?")
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"): 
            st.write(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Thinking with Gemini..."):
                ai_response = get_ai_response(user_input)
                st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
                st.write(ai_response)

# --- Assessment Tab ---
with tab2:
    st.subheader("📝 Well-being Check-in")
    with st.form("well_being_form"):
        q1 = st.slider("1. Stressed or overwhelmed?", 1, 5, key="q1")
        q2 = st.slider("2. Anxious or worried?", 1, 5, key="q2")
        q3 = st.slider("3. Sad or down?", 1, 5, key="q3")
        q4 = st.slider("4. Lonely or isolated?", 1, 5, key="q4")
        q5 = st.slider("5. Not getting enough sleep?", 1, 5, key="q5")
        submitted = st.form_submit_button("Submit Assessment")

    if submitted:
        responses = {"q1": q1, "q2": q2, "q3": q3, "q4": q4, "q5": q5}
        feedback = get_assessment_feedback(responses)
        st.session_state.assessment_submitted = True
        st.balloons()
        st.info(feedback)

# --- Resources Tab ---
with tab3:
    st.subheader("📚 Resources for You")
    st.markdown("""
    ### 🌬 Breathing Exercise (4-7-8)
    1. Inhale for 4 sec  
    2. Hold for 7 sec  
    3. Exhale for 8 sec  

    ### 📝 Journaling Prompts
    - One thing I’m grateful for today?  
    - Something I’m looking forward to this week?  
    - A kind message I’d give my younger self?  

    ### 🚨 Professional Support
    - **Crisis Text Line:** Text HOME to 741741 (US)  
    - **The Trevor Project:** 1-866-488-7386  
    - **NAMI Helpline:** Mental health resources & local support  
    """)
