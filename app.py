import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="FitBuddy AI", page_icon="💪")
st.title("💪 FitBuddy - AI Fitness Plan Generator")
st.write("Using Gemini Models")

api_key = st.text_input("Enter your Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    name = st.text_input("Your Name")
    age = st.number_input("Age", 10, 80, 20)
    goal = st.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "Stay Fit"])
    level = st.selectbox("Your Level", ["Beginner", "Intermediate", "Advanced"])
    
    if st.button("Generate My Fitness Plan"):
        with st.spinner("Creating your plan..."):
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"Create fitness plan for Name:{name}, Age:{age}, Goal:{goal}, Level:{level}. Give diet and workout plan simple."
            response = model.generate_content(prompt)
            st.success(f"Here is your plan, {name}!")
            st.markdown(response.text)
else:
    st.info("Please enter API Key to start")
