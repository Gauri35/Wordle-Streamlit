import streamlit as st

st.markdown("""
    <h1 style='
        text-align: center;
        background: linear-gradient(to right, red, orange, yellow, green);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: "Segoe UI", sans-serif;
    '>
        🎮Streamle - A Wordle Game
    </h1>
""", unsafe_allow_html=True)

st.subheader("Guess the 5-letter word in 6 tries or less.")
