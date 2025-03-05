import streamlit as st
import random
import string

def generate_password(length,use_digits,use_special):
    characters = string.ascii_letters# + string.digits + string.punctuation
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    return''.join(random.choice(characters) for _ in range(length))

st.title("Password Generator")
length = st.slider("select Password Length", 4, 20)

use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)

    st.write(f"Generated Password : {password}")

    st.write("Copy the password and use it")

st.write("Build with ❤️ by Maryam Faizan")
