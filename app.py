import streamlit as st
import pandas as pd

st.set_page_config(page_title="Quranic AI", page_icon="📖")

# 1. Load the Data
@st.cache_data
def load_data():
    return pd.read_csv("quran_text.csv")

# We use a simple check to make sure the file loads
try:
    df = load_data()
    st.title("📖 Quranic Auto-Correction AI")
    st.success("Database Loaded Successfully!")

    # 2. Search Section
    st.subheader("Find a Verse")
    surah_num = st.number_input("Surah Number", min_value=1, max_value=114, value=1)
    ayah_num = st.number_input("Ayah Number", min_value=1, value=1)

    if st.button("Show Verse"):
        result = df[(df['surah'] == surah_num) & (df['ayah'] == ayah_num)]
        if not result.empty:
            st.info(result.iloc[0]['text'])
        else:
            st.warning("Verse not found in your CSV.")

except Exception as e:
    st.error("Error: Could not find 'quran_text.csv'.")
    st.write("Please make sure the file name on GitHub matches exactly.")
