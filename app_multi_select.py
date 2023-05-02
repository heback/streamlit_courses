import streamlit as st

options = st.multiselect(
    'What are your favorite colors',
     # options
    ['Green', 'Yellow', 'Red', 'Blue'],
    # defaults
    ['Yellow', 'Red'])

st.write('You selected:', options)

