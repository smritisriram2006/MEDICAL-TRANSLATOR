# translator.py — Version 6.2 (Safe Multi-word Medical Terms)
import streamlit as st
import pandas as pd
import re
from pathlib import Path
from functools import lru_cache
from deep_translator import GoogleTranslator

# --- Load Medical Dictionary ---
@st.cache_data(ttl=3600)
def load_medical_dictionary():
    """Loads and caches the medical dictionary from CSV safely."""
    try:
        csv_path = Path(__file__).resolve().parent / "data" / "medical_translations.csv"
        df = pd.read_csv(csv_path, quotechar='"', encoding='utf-8', on_bad_lines='skip')
        df['english'] = df['english'].astype(str).str.lower().str.strip()
        df['tamil'] = df['tamil'].astype(str).str.strip()
        return dict(zip(df['english'], df['tamil']))
    except FileNotFoundError:
        st.error("CRITICAL ERROR: 'medical_translations.csv' not found in the 'data' folder.")
        return {}

medical_dict = load_medical_dictionary()
translator = GoogleTranslator(source='en', target='ta')

# --- Cached Google Translate ---
@lru_cache(maxsize=500)
def google_translate_cached(text: str) -> str:
    """Cached wrapper around GoogleTranslator to avoid repeat API calls."""
    return translator.translate(text)

# --- Main Translation Function ---
def translate_text(english_text: str) -> str:
    """Translates English medical text to Tamil safely, handling multi-word medical terms."""
    if not english_text.strip():
        return ""

    # Step 1: Lowercase input
    text = english_text.strip().lower()

    # Step 2: Protect multi-word medical terms with unique placeholders
    placeholder_map = {}
    for eng_term in sorted(medical_dict.keys(), key=len, reverse=True):
        placeholder = f"@@TERM{len(placeholder_map)}@@"
        placeholder_map[placeholder] = medical_dict[eng_term]
        # Replace full term with placeholder using word boundaries
        text = re.sub(rf'\b{re.escape(eng_term)}\b', placeholder, text)

    # Step 3: Translate the remaining text via Google Translate
    try:
        translated = google_translate_cached(text)
    except Exception as e:
        st.error(f"API Translation failed: {e}")
        return "மொழிபெயர்ப்பு தோல்வி"

    # Step 4: Replace placeholders with Tamil medical terms
    for placeholder, tam_term in placeholder_map.items():
        translated = translated.replace(placeholder, tam_term)

    return translated.strip()
