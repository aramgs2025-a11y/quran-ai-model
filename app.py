import streamlit as st
st.title("Quranic AI Checker")
user_text = st.text_input("Type a verse here:")
if user_text:
    st.write(f"You entered: {user_text}")
import streamlit as st
import pandas as pd

# 1. Load the Quran Dataset from the file you uploaded
@st.cache_data
def load_data():
    # This matches the 'quran_text.csv' file in your GitHub
    df = pd.read_csv("quran_text.csv")
    return df

try:
    df = load_data()
    
    st.title("📖 Quranic Search & Verify")
    st.write("Enter the Surah and Ayah to find the correct text.")

    # 2. Search Inputs
    col1, col2 = st.columns(2)
    with col1:
        surah_num = st.number_input("Surah", min_value=1, max_value=114, value=1)
    with col2:
        ayah_num = st.number_input("Ayah", min_value=1, value=1)

    if st.button("Get Verse"):
        # This searches your CSV file
        result = df[(df['surah'] == surah_num) & (df['ayah'] == ayah_num)]
        
        if not result.empty:
            st.success(result.iloc[0]['text'])
        else:
            st.warning("Verse not found. Check your CSV data.")

except Exception as e:
    st.error(f"Error loading data: {e}")
    st.info("Make sure your CSV file has 'surah', 'ayah', and 'text' columns.")
