import streamlit as st

# Initialization
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Session State also supports attribute based syntax
if 'key' not in st.session_state:
    st.session_state.key = 'value'

# Read
st.write(st.session_state.key)

# Outputs: value

st.session_state.key = 'value2'     # Attribute API
st.session_state['key'] = 'value2'  # Dictionary like API

# Delete a single key-value pair
del st.session_state[key]

# Delete all the items in Session state
for key in st.session_state.keys():
    del st.session_state[key]

# Every widget with a key is automatically
# added to Session State:
st.text_input("Your name", key="name")

# This exists now:
st.session_state.name


def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)


with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    submit_button = st.form_submit_button(
        label='Submit',
        on_click=form_callback
    )

slider = st.slider(
    label='My Slider', min_value=1,
    max_value=10, value=5, key='my_slider')

st.session_state.my_slider = 7

# Throws an exception!

