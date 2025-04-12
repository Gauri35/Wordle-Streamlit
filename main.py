import streamlit as st
import random

# Load 5-letter words
@st.cache_data
def load_words():
    with open("words.txt") as f:
        return [word.strip().upper() for word in f if len(word.strip()) == 5 and word.strip().isalpha()]

WORDS = load_words()

# Select secret word
if "secret" not in st.session_state:
    st.session_state.secret = random.choice(WORDS)

SECRET_WORD = st.session_state.secret
#print(SECRET_WORD)

st.markdown("""
    <h1 style='
        text-align: center;
        background: linear-gradient(to right, red, orange, yellow, green);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: "Segoe UI", sans-serif;
    '>
        🎮 Streamle - A Wordle Game
    </h1>
""", unsafe_allow_html=True)

st.subheader("Guess the 5-letter word in 6 tries or less.")

# Session state init
if "guesses" not in st.session_state:
    st.session_state.guesses = []

# Submit logic
def submit_guess():
    guess = st.session_state.guess_input.upper()
    if len(guess) == 5 and guess.isalpha():
        st.session_state.guesses.append(guess)
    else:
        st.warning("Please enter a valid 5-letter word.")
    st.session_state.guess_input = ""

# Input field (must appear **only once** with key='guess_input')
st.text_input(
    "Enter a 5-letter word:",
    max_chars=5,
    key="guess_input",
    on_change=submit_guess
)

# Display guesses
def get_colored_boxes(guess, answer):
    result = []
    for i, letter in enumerate(guess):
        if letter == answer[i]:
            color = "#6aaa64"  # green
        elif letter in answer:
            color = "#c9b458"  # yellow
        else:
            color = "#787c7e"  # gray
        result.append(f"<div style='display:inline-block; width:40px; height:40px; \
                        margin:2px; background:{color}; color:white; text-align:center; \
                        vertical-align:middle; line-height:40px; font-size:24px; \
                        font-weight:bold; border-radius:4px;'>{letter}</div>")
    return "".join(result)

st.markdown("### Your Guesses:")
for g in st.session_state.guesses:
    st.markdown(get_colored_boxes(g, SECRET_WORD), unsafe_allow_html=True)

# Game end
if len(st.session_state.guesses) >= 6 or SECRET_WORD in st.session_state.guesses:
    if SECRET_WORD in st.session_state.guesses:
        st.success("🎉 You guessed it!")
    else:
        st.error(f"😢 Out of attempts. The word was **{SECRET_WORD}**.")
