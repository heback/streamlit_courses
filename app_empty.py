import streamlit as st

empty = st.empty()

col1, col2 = st.columns(2)

with col1:
    btn1 = st.button('첫번째 정보 표시')
    if btn1:
        empty.success('첫 번째 버튼을 클릭했습니다.')

with col2:
    btn2 = st.button('두번째 정보 표시')
    if btn2:
        empty.info('두 번째 버튼을 클릭했습니다.')

btn3 = st.button('초기화')
if btn3:
    empty.empty()

