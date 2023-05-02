import pandas as pd
import streamlit as st
import sqlite3

con = sqlite3.connect('db.db')
cur = con.cursor()


def check_uid(uid):
    cur.execute(f"SELECT COUNT(*) FROM users WHERE uid='{uid}'")
    res = cur.fetchone()
    return res[0]

img_dir = 'tmp'

st.subheader('회원 검색')

col1,col2,col3 = st.columns(3)
with col1:
    text_input = st.empty()
    uid = text_input.text_input('아이디')
with col2:
    search = st.button('검색')
    init = st.button('다시 검색')

    if init:
        uid = None
        search = None
        uid = text_input.text_input('아이디', key=2)


if search:

    if uid is None or len(uid) < 5:
        st.warning('회원 아이디를 입력하세요.')
        st.stop()

    print(check_uid(uid))

    if check_uid(uid) == 0:
        st.warning('해당 아이디는 존재하지 않습니다.')
        st.stop()

    st.subheader('검색 결과')
    with st.container():

        cur.execute(f"SELECT u.uid, u.hakbun, u.uname, u.ubd, u.ugender, p.im_name \
                      FROM users as u, photos as p \
                      WHERE u.hakbun=p.hakbun AND u.uid='{uid}'")
        for row in cur:
            df = pd.DataFrame(data=row, columns= ['내용'], index=['아이디','학번','성명','생년월일','성별','사진'])
            st.dataframe(df)
            st.image(img_dir + '/' + row[5])

    uid = None
    search = None