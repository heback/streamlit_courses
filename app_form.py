import streamlit as st
import sqlite3
import datetime

con = sqlite3.connect('user.db')
cur = con.cursor()
table_name = 'users'


def check_table(table_name):
    cur.execute(f"SELECT COUNT(*) FROM sqlite_master "
                f"WHERE type='table' AND name='{table_name}'")
    if cur.fetchone()[0] == 0:
        cur.execute(f"CREATE TABLE {table_name} ("
                    f"id INTEGER PRIMARY KEY AUTOINCREMENT,"
                    f"user_id TEXT UNIQUE,"
                    f"user_name TEXT NOT NULL,"
                    f"user_gender TEXT NOT NULL,"
                    f"user_pw TEXT NOT NULL,"
                    f"user_email TEXT UNIQUE,"
                    f"user_birthday TEXT)")
        con.commit()


st.subheader('회원가입 폼')

with st.form('my_form', clear_on_submit=True):
    st.info('다음 양식을 모두 입력 후 제출합니다.')
    user_id = st.text_input('아이디', max_chars=12)
    user_name = st.text_input('성명', max_chars=10)
    user_gender = st.radio('성별', options=['남', '여'], horizontal=True)
    user_pw = st.text_input('비밀번호', type='password')
    user_pw_chk = st.text_input('비밀번호 확인', type='password')
    user_email = st.text_input('이메일', max_chars=50)
    user_birthday = st.date_input('생년월일', min_value=datetime.date(1930, 1, 1))

    submitted = st.form_submit_button('제출')
    if submitted:

        if user_pw != user_pw_chk:
            st.warning('비밀번호가 일치하지 않습니다.')
        else:

            check_table(table_name)
            st.success(f'{user_id} {user_name} {user_gender} '
                       f'{user_pw} {user_email} {user_birthday}')
            cur.execute(f"INSERT INTO users ("
                        f"user_id, user_name, user_gender,"
                        f"user_pw, user_email, user_birthday) VALUES ("
                        f"'{user_id}','{user_name}','{user_gender}',"
                        f"'{user_pw}','{user_email}', '{user_birthday}')")
            con.commit()

