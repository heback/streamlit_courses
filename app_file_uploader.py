import streamlit as st
import os

# 업로드 폴더 지정
upload_dir = 'files'

# 파일 업로드 위젯
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:

    try:
        # 업로드 폴더가 없으면 새로 생성
        if not os.path.exists(upload_dir):
            os.mkdir(upload_dir)
        # 업로드 파일을 업로드 폴더에 쓰기
        with open(os.path.join('files', uploaded_file.name), 'wb') as f:
            f.write(uploaded_file.getbuffer())
        st.success('File Upload Success!')

    except Exception as e:
        st.error('File Upload Error!')


