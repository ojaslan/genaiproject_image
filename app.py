from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai  # ✅ Corrected import

# Load environment variable
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")  # ✅ Removed "="

# Validate API key
if not api_key:
    st.error("GOOGLE_API_KEY is missing in your .env file.")
    st.stop()

# Configure Gemini
genai.configure(api_key=api_key)

# Load model
model = genai.GenerativeModel("gemini-pro")  # ✅ Or "gemini-1.5-pro" if available

# Function to get response
def get_gemini_response(question):
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.set_page_config(page_title="Gemini LLM Application")
st.title("Ask anything to Gemini")

user_input = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

if submit and user_input:
    response = get_gemini_response(user_input)
    st.subheader("Response")
    st.write(response)
