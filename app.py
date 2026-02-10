import streamlit as st
st.title("Quranic AI Checker")
user_text = st.text_input("Type a verse here:")
if user_text:
    st.write(f"You entered: {user_text}")
