import streamlit as st


from textblob import TextBlob
import nltk
nltk.download('punkt')  # Only required once


# Page config
st.set_page_config(page_title="Emotion Detector", layout="centered")

# Custom CSS for center alignment
st.markdown("""
    <style>
        .centered-title {
            text-align: center;
            font-size: 40px;
            color: #4B9CD3;
        }
        .sub-title {
            text-align: center;
            font-size: 20px;
            color: #333333;
        }
        .stTextArea, .stButton {
            margin: auto;
        }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.markdown("<h1 class='centered-title'>Welcome to Emotion Detector</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Enter a sentence and I'll detect the emotion behind it!</p>", unsafe_allow_html=True)

# Input
user_input = st.text_area("✍️ Your Text", placeholder="Type something...")

# Emotion detection function
def detect_emotion(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.5:
        return "Very Happy 😊"
    elif polarity > 0:
        return "Happy 🙂"
    elif polarity == 0:
        return "Neutral 😐"
    elif polarity > -0.5:
        return "Sad 🙁"
    else:
        return "Very Sad 😢"

# Button
if st.button("Detect Emotion 🎯"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        emotion = detect_emotion(user_input)
        st.success(f"**Detected Emotion:** {emotion}")
