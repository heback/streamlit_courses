import streamlit as st

number = st.number_input(
    'Insert a number',
    value=0
    # value=0: 정수 입력
    # value=0.0: 실수 입력
    )
st.write('The current number is ', number)


