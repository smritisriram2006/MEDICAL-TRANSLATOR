# app.py — Version 6.0 (Refined + Safe Audio Handling)
import streamlit as st
from gtts import gTTS
import base64
import tempfile
from streamlit_mic_recorder import speech_to_text
from translator import translate_text

# --- Page Configuration ---
st.set_page_config(
    page_title="Doctor → Patient Medical Translator",
    page_icon="💊",
    layout="centered",
)

# --- App Title & Version ---
st.title("💊 Doctor → Patient Medical Translator")

st.markdown("Speak or type in **English**, and the system will translate to **Tamil** using both AI and a custom medical dictionary.")

# --- Session State Initialization ---
if 'english_input' not in st.session_state:
    st.session_state['english_input'] = ""
if 'translated_text' not in st.session_state:
    st.session_state['translated_text'] = ""

# --- Voice Input Section ---
st.subheader("🎙️ Voice Input")
voice_text = speech_to_text(language='en-IN', use_container_width=True, just_once=True, key="voice_input")

if voice_text:
    st.session_state['english_input'] = voice_text

# --- Text Input Area ---
st.subheader("✍️ Text Input")
english_input = st.text_area(
    "Type your English text below:",
    value=st.session_state['english_input'],
    height=100,
    placeholder="e.g. The patient has high blood pressure and needs medication twice a day.",
)

# --- Translate Button ---
if st.button("🔄 Translate to Tamil"):
    st.session_state['english_input'] = english_input
    if not english_input.strip():
        st.warning("Please type or speak something first.")
    else:
        with st.spinner("🔍 Translating..."):
            translation = translate_text(english_input)
            st.session_state['translated_text'] = translation

# --- Translation Output ---
if st.session_state['translated_text']:
    st.subheader("📝 Tamil Translation:")
    st.text_area(
        "Tamil Output",
        st.session_state['translated_text'],
        height=100,
    )

    # --- Audio Output ---
    st.subheader("🔊 Listen to Translation:")
    try:
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
            tts = gTTS(text=st.session_state['translated_text'], lang='ta')
            tts.save(tmp.name)
            tmp.seek(0)
            audio_bytes = tmp.read()

        audio_base64 = base64.b64encode(audio_bytes).decode()
        st.markdown(
            f'<audio controls autoplay>'
            f'<source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">'
            f'</audio>',
            unsafe_allow_html=True,
        )

    except Exception as e:
        st.error(f"⚠️ Could not generate Tamil speech. Error: {e}")