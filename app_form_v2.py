import streamlit as st
import sqlite3
import pandas as pd

# read_sql_table을 위한 db 연결
from sqlalchemy import create_engine
engine = create_engine('sqlite:///db.db')

# db-api를 위한 db 연결
con = sqlite3.connect('db.db')
cur = con.cursor()


def check_id(user_id):
    cur.execute(f"SELECT COUNT(*) FROM users WHERE uid='{user_id}'")
    res = cur.fetchone()
    return res[0]


menu = st.sidebar.selectbox('Menu', options=['회원 목록', '회원가입 폼'])
if menu == '회원 목록':

    st.subheader('회원목록')
    df = pd.read_sql_table('users', engine)
    st.dataframe(df)

elif menu == '회원가입 폼':
    st.subheader('회원가입 폼')

    with st.form('my_form', clear_on_submit=True):
        st.info('다음 양식을 모두 입력 후 제출합니다.')
        uid = st.text_input('아이디', max_chars=12)
        hakbun = st.text_input('학번', max_chars=4)
        uname = st.text_input('성명', max_chars=10)
        upw = st.text_input('비밀번호', type='password')
        upw_chk = st.text_input('비밀번호 확인', type='password')
        ubd = st.date_input('생년월일')
        ugender = st.radio('성별', options=['남','여'], horizontal=True)

        submitted = st.form_submit_button('제출')
        if submitted:

            if check_id(uid):
                st.warning('동일한 아이디가 존재합니다.')
                st.stop()

            if upw != upw_chk:
                st.warning('비밀번호를 확인하세요.')
                st.stop()

            st.success(f'{uid} {hakbun} {uname} {upw} {ubd} {ugender}')
            cur.execute(f"INSERT INTO users VALUES ("
                        f"'{uid}', '{hakbun}', '{uname}','{upw}',"
                        f"'{ubd}','{ugender}',CURRENT_DATE)")
            con.commit()




