import streamlit as st
import pandas as pd

# 1. Load the Quran Dataset
@st.cache_data
def load_data():
    df = pd.read_csv("quran_text.csv")
    return df

df = load_data()

st.title("📖 Quranic Auto-Correct AI")

# 2. Search Feature
st.subheader("Check a Verse")
surah_num = st.number_input("Enter Surah Number", min_value=1, max_value=114, value=1)
ayah_num = st.number_input("Enter Ayah Number", min_value=1, value=1)

# 3. Logic to compare
if st.button("Verify Verse"):
    # Filter the dataset for the specific verse
    result = df[(df['surah'] == surah_num) & (df['ayah'] == ayah_num)]
    
    if not result.empty:
        correct_text = result.iloc[0]['text']
        st.success(f"Correct Text: {correct_text}")
    else:
        st.error("Verse not found in our current test dataset.")
