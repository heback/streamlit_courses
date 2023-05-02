import streamlit as st

title = st.text_input(
    # label
    'Movie title',
    # value
    '',
    placeholder='input movie title')

st.write('The current movie title is', title)
