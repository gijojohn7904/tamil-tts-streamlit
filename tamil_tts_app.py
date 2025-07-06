import streamlit as st
from gtts import gTTS
import tempfile
import os

st.set_page_config(page_title="Tamil Text-to-Speech", page_icon="🔊", layout="centered")

st.title("🔊 Tamil Text-to-Speech (TTS) Generator")

# Input for Tamil text
tamil_text = st.text_area(
    "Paste your Tamil message here:",
    height=150,
    value="""இது swiggy-யிடமிருந்து ஒரு முக்கியமான அறிவிப்பு, கடந்த ஒரு வாரமாக நீங்கள் வேலை செய்யவில்லை என்பதை நாங்கள் கவனித்தோம். எனவே புதிய பணியாளர்களை எளிதாக்க உங்கள் கணக்கை தற்காலிகமாக செயலிழக்கச் செய்ய முடிவு செய்துள்ளோம். இந்த செயலிழப்பு செயல்முறையை நிறுத்த, இன்றே உள்நுழைந்து பரிவர்த்தனையைத் தொடங்குங்கள். ஏதேனும் கவலைகள் அல்லது கோரிக்கைகளுக்கு உங்கள் ஃப்ளீட் மேலாளர்களைத் தொடர்பு கொள்ளவும்."""
)

if st.button("🎙️ Convert to Speech"):
    with st.spinner("Generating audio..."):
        tts = gTTS(text=tamil_text, lang='ta')
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
            tts.save(tmpfile.name)
            audio_file = tmpfile.name

        st.success("✅ Audio generated! Listen below:")
        audio_bytes = open(audio_file, "rb").read()
        st.audio(audio_bytes, format="audio/mp3")

        # Download link
        st.download_button(
            label="⬇️ Download Audio",
            data=audio_bytes,
            file_name="swiggy_tamil_notification.mp3",
            mime="audio/mp3"
        )

        os.remove(audio_file)

st.markdown("---")
st.caption("Powered by gTTS & Streamlit. | Gizmo AI x Swiggy S&O |")
