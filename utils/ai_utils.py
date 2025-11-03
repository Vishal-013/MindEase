# utils/ai_utils.py
import os
import google.generativeai as genai

# Configure Gemini with API Key
genai.configure(api_key=os.getenv("AIzaSyB--wYQ0E"))

# Create model object
model = genai.GenerativeModel("gemini-1.5-flash")

def get_ai_response(prompt: str) -> str:
    """
    Sends a prompt to Google Gemini and returns the generated response text.
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error from Gemini API: {e}"
