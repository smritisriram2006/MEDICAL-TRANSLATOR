# Doctor–Patient Medical Translator (English ⇄ Tamil)

An AI-powered translation web app designed to bridge the communication gap between English-speaking doctors and Tamil-speaking patients.  
This project ensures accurate translation of complex medical terminology while maintaining conversational fluency — helping improve healthcare accessibility and understanding.

---

## Key Features

- **Hybrid Translation Engine:**  
  Combines a local 18,000+ term custom medical dictionary (via Pandas) with the `deep-translator` API for context-aware translations.

- **Medical Term Accuracy:**  
  Detects and translates specialized terms (e.g., “anaphylaxis” → “கடும் ஒவ்வாமை”) instead of simple transliteration.

- **Voice Input:**  
  Users can speak in English using their microphone via `streamlit-mic-recorder`.

- **Audio Output:**  
  Translated Tamil text is read aloud automatically using `gTTS` (Google Text-to-Speech), helping patients with low literacy.

- **Full Sentence Translation:**  
  Uses a hybrid word-by-word and placeholder-based parsing system to preserve both meaning and grammar.

- **Simple, Web-Based UI:**  
  Built with Streamlit for a clean, fast, and intuitive user experience.

---

## Technologies Used

| Category | Tools |
|-----------|-------|
| Programming Language | Python |
| Framework | Streamlit |
| Libraries | Pandas, deep-translator, gTTS, streamlit-mic-recorder |
| Text Processing | Regex, String Manipulation |
| Data Source | Custom 18,000-term Medical Dictionary (CSV) |

---

## How It Works

### 1. Load Dictionary  
The custom medical dictionary (`medical_translations.csv`) is loaded into memory using `@st.cache_data` for fast lookups.

### 2. Parse Input  
When the user enters a sentence (e.g.,  
"You have a fever and anaphylaxis."),  
the app tokenizes the text word by word.

### 3. Match Medical Terms  
Each cleaned word is checked against the medical dictionary.  
- If found → use its accurate Tamil translation  
- If not → keep the word in English  

### 4. Mixed Sentence Construction  
Creates a mixed sentence, e.g.  
"You have காய்ச்சல் and கடும் ஒவ்வாமை."

### 5. Final Translation  
This hybrid text is sent to Google Translate via the `deep-translator` API, which correctly handles the mixed structure, producing a fully natural Tamil sentence.

### 6. Display & Speak  
The final translation is displayed on the web app and spoken aloud using `gTTS`.

---

## Project Structure

```
medical_translator_app/
│
├── data/
│   └── medical_translations.csv       # Custom 18,000+ term medical dictionary
│
├── app.py                             # Streamlit web app (UI & logic)
├── translator.py                      # Core translation and parsing logic
├── requirements.txt                   # Python dependencies
├── README.md                          # Documentation
└── .gitignore                         # Ignore cache and environment files
```

---

## Setup & Installation

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd medical_translator_app
```

### 2. Create a Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
streamlit run app.py
```

Streamlit will open your app automatically in a new browser tab.

---

## Example

**Input:**  
"You have a fever and anaphylaxis."

**Output:**  
"உங்களுக்கு காய்ச்சலும் கடும் ஒவ்வாமையும் உள்ளது."

**Audio:**  
Tamil translation read aloud using `gTTS`.

---

## Skills Demonstrated
- Python Programming  
- Natural Language Processing (NLP)  
- API Integration (`deep-translator`, `gTTS`, `streamlit-mic-recorder`)  
- Regex & Text Parsing  
- Data Handling with Pandas  
- Accessibility-Focused Design  
- Streamlit Web App Development  

---

## Future Improvements
- Add more languages 
- Expand dictionary coverage and synonym handling  
- Integrate offline translation mode for low-connectivity areas  
- Implement context-based phrase prediction  

---

## Author

**Smriti Sriram**  
 Passionate about building inclusive, AI-driven solutions that connect people and technology.  
**Email:** [smritisriram2006@gmail.com](mailto:smritisriram2006@gmail.com)  
**LinkedIn:** [Smriti Sriram](https://www.linkedin.com/in/smritisriram)

