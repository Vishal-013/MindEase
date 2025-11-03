import joblib
import streamlit as st

@st.cache_resource
def load_model():
    return joblib.load("models/mental_health_model.pkl")

ml_model = load_model()

def get_assessment_feedback(responses):
    """
    Predicts risk level using pre-trained ML model.
    responses: dict with q1–q5 answers
    """
    try:
        features = [[responses["q1"], responses["q2"], responses["q3"], responses["q4"], responses["q5"]]]
        risk_pred = ml_model.predict(features)[0]
        proba = ml_model.predict_proba(features)[0]

        if risk_pred == 0:
            return f"✅ Low Risk ({proba[0]*100:.1f}% confidence). Keep practicing self-care!"
        elif risk_pred == 1:
            return f"⚠️ Moderate Risk ({proba[1]*100:.1f}% confidence). Consider healthy coping strategies."
        else:
            return f"🚨 High Risk ({proba[2]*100:.1f}% confidence). Please reach out to supportive resources or professionals."

    except Exception as e:
        return f"⚠️ ML model error: {str(e)}"
