import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="Emotion Detector", layout="centered")

# CSS Animations
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
        color: #333;
    }

    .emotion-box {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        margin-top: 30px;
        animation: fadeIn 1s ease-in-out;
        position: relative;
        overflow: visible;
        height: 120px;
    }

    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }

    .emoji-container {
        position: relative;
        height: 100px;
    }

    .emoji-float {
        position: absolute;
        bottom: 0;
        font-size: 24px;
        animation: floatUp 2.5s ease-in-out forwards;
        opacity: 0;
    }

    @keyframes floatUp {
        0%   { transform: translateY(0); opacity: 0; }
        30%  { opacity: 1; }
        100% { transform: translateY(-100px); opacity: 0; }
    }
</style>
""", unsafe_allow_html=True)


st.markdown("<h1 class='centered-title'>Welcome to Emotion Detector</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Enter a sentence and I'll detect the emotion behind it!</p>", unsafe_allow_html=True)

# Input
user_input = st.text_area("✍️ Your Text", placeholder="Type something...")

# Emotion Logic
def detect_emotion(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.5:
        return "Very Happy 😊", ['🌸', '🌼', '🌺'], 'float-emoji'
    elif polarity > 0:
        return "Happy 🙂", ['❤️', '💖', '💘'], 'float-emoji'
    elif polarity == 0:
        return "Neutral 😐", [], ''
    elif polarity > -0.5:
        return "Sad 🙁", ['💧', '💦'], 'fall-emoji'
    else:
        return "Very Sad 😢", ['💧', '💧', '😞'], 'fall-emoji'

if st.button("Detect Emotion 🎯"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        emotion_text, emoji_list, anim_class = detect_emotion(user_input)

        # Generate many floating emojis with random left positions
        import random
        emoji_html = ""
        if anim_class == 'float-emoji':
            emoji_html = "<div class='emoji-container'>"
            for i in range(20):  # 20 floating emojis
                emoji = random.choice(emoji_list)
                left = random.randint(0, 90)  # random left percentage
                emoji_html += f"<span class='emoji-float' style='left: {left}%;'>{emoji}</span>"
            emoji_html += "</div>"
        elif anim_class == 'fall-emoji':
            emoji_html = ' '.join([f"<span class='fall-emoji'>{e}</span>" for e in emoji_list])

        st.markdown(f"<div class='emotion-box'>Detected Emotion: {emotion_text}<br>{emoji_html}</div>", unsafe_allow_html=True)
