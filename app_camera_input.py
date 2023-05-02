import streamlit as st
import os.path

picture = st.camera_input("Take a picture")

if picture:
    # 사진 출력
    st.image(picture)

    # 사진 저장
    if not os.path.exists('pics'):
        os.mkdir('pics')
    with open(os.path.join('pics', picture.name), 'wb') as f:
        f.write(picture.getbuffer())

