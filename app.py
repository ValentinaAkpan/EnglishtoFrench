import streamlit as st
from deep_translator import GoogleTranslator

# ---------- Translation Logic ----------
def translate_preserving_format(text):
    lines = text.strip().split('\n')
    translated_lines = []
    progress = st.progress(0)

    for i, line in enumerate(lines):
        line = line.strip()
        if line == "":
            translated_lines.append("")
        else:
            translated = GoogleTranslator(source='english', target='french').translate(line)
            translated_lines.append(translated)
        progress.progress((i + 1) / len(lines))

    return "\n".join(translated_lines)

# ---------- Streamlit Config ----------
st.set_page_config(page_title="Translator Pro", page_icon="🌍", layout="wide")

# ---------- Custom CSS ----------
st.markdown("""
    <style>
    html, body, .stApp {
        background: linear-gradient(to bottom right, #f0f7ff, #e3ecf8);
        font-family: 'Segoe UI', sans-serif;
    }

    .app-container {
        background-color: #ffffff;
        border-radius: 20px;
        padding: 3rem;
        margin: 2rem auto;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
        max-width: 960px;
    }

    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        color: #223;
    }

    .subtext {
        text-align: center;
        font-size: 1.1rem;
        color: #555;
        margin-bottom: 2rem;
    }

    .stTextArea textarea {
        font-size: 16px;
        border-radius: 12px;
        padding: 1.1rem;
    }

    .stButton>button {
        font-size: 1.1rem;
        padding: 0.6rem 1.5rem;
        border-radius: 8px;
        background-color: #2e77d0;
        color: white;
        border: none;
    }

    .stButton>button:hover {
        background-color: #245fa6;
    }

    .download-btn {
        margin-top: 1rem;
    }

    footer {
        text-align: center;
        color: #aaa;
        font-size: 0.85rem;
        margin-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- App UI ----------
st.markdown('<div class="app-container">', unsafe_allow_html=True)

# 🎯 Banner Image (free Unsplash image)
st.markdown('<div style="text-align: center; margin-bottom: 1.5rem;">', unsafe_allow_html=True)
st.markdown('''
    <div style="text-align: center; margin-bottom: 2rem;">
        <img src="https://images.unsplash.com/photo-1593642634367-d91a135587b5?auto=format&fit=crop&w=1200&q=80"
             style="width: 100%; max-height: 250px; object-fit: cover; border-radius: 10px;" />
    </div>
''', unsafe_allow_html=True)


st.markdown('</div>', unsafe_allow_html=True)

# 🌍 Title + Subtitle
st.markdown('<div class="main-title">🌍 Translator Pro</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">Paste English text with formatting and get a clean, downloadable French translation.</div>', unsafe_allow_html=True)

# ✏️ Input Text
input_text = st.text_area("✏️ Enter English text below", height=200)

# 🔁 Translate
if st.button("🔁 Translate to French"):
    if not input_text.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Translating..."):
            translated_output = translate_preserving_format(input_text)

        st.success("✅ Translation complete!")
        st.markdown("### 🇫🇷 Translated Text")
        st.text_area(" ", translated_output, height=300)
        st.download_button("💾 Download Translation", translated_output, file_name="translation.txt", key="download_btn")

# 📎 Close card
st.markdown("</div>", unsafe_allow_html=True)

# 🔻 Footer
