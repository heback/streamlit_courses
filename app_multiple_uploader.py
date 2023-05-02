import streamlit as st
import os

# 업로드 폴더 지정
upload_dir = 'files'

# 파일 업로드 위젯
uploaded_files = st.file_uploader(
    'Upload Multiple Images',
    type=['png', 'jpg', 'jpeg'],
    accept_multiple_files=True
)

if uploaded_files is not None and len(uploaded_files) != 0:

    try:
        # 업로드 폴더가 없으면 새로 생성
        if not os.path.exists(upload_dir):
            os.mkdir(upload_dir)
        # 업로드 파일을 업로드 폴더에 쓰기
        for img_file in uploaded_files:
            with open(os.path.join('files', img_file.name), 'wb') as f:
                f.write(img_file.getbuffer())
        st.success('Image file upload success!')

    except OSError:
        st.error('File Upload Error!')


