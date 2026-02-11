import streamlit as st
import pandas as pd
from fuzzywuzzy import fuzz

st.set_page_config(page_title="Quranic AI Checker", page_icon="📖")

@st.cache_data
def load_data():
    return pd.read_csv("quran_text.csv")

df = load_data()

st.title("📖 Quranic Auto-Correction AI")

# --- SEARCH SECTION ---
st.subheader("1. Select Verse")
col1, col2 = st.columns(2)
with col1:
    surah = st.number_input("Surah", min_value=1, max_value=114, value=1)
with col2:
    ayah = st.number_input("Ayah", min_value=1, value=1)

result = df[(df['surah'] == surah) & (df['ayah'] == ayah)]

if not result.empty:
    correct_text = result.iloc[0]['text']
    
    # --- TESTING SECTION ---
    st.subheader("2. Test Your Accuracy")
    user_input = st.text_area("Type the verse here:")

    if st.button("Check My Typing"):
        if user_input:
            # AI Similarity Calculation
            score = fuzz.ratio(user_input, correct_text)
            
            if score == 100:
                st.success(f"Perfect! Accuracy: {score}% ✅")
            elif score > 80:
                st.warning(f"Almost there! Accuracy: {score}%. Check your diacritics.")
                st.write(f"**Correct version:** {correct_text}")
            else:
                st.error(f"Low Accuracy: {score}%. Keep practicing!")
                st.write(f"**Target text:** {correct_text}")
        else:
            st.info("Please type something to check.")
