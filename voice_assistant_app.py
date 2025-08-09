import streamlit as st
import speech_recognition as sr
import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Listening... Speak now!")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        st.success(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        st.error("Sorry, I didn't catch that.")
    except sr.RequestError:
        st.error("Could not request results. Check internet.")
    return ""

# Streamlit UI
st.title("🧠 Voice Assistant")

if st.button("Start Listening"):
    user_text = recognize_speech()
    if user_text:
        # AI response can be plugged in here
        response = f"You said: {user_text}. That's interesting!"
        st.write(response)
        speak(response)
