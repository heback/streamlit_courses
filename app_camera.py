import streamlit as st
import os.path

# 이미지 저장 폴더 생성
save_dir = 'tmp'
if not os.path.exists(save_dir):
     os.mkdir(save_dir)


# (함수)업로드된 파일 저장하기
def save_uploaded_file(uploadedfile, new_name):
    with open(os.path.join(save_dir, uploadedfile.name), 'wb') as f:
        f.write(uploadedfile.getbuffer())
    fname, ext = os.path.splitext(uploadedfile.name)
    # print(fname)
    # print(ext)
    if os.path.isfile( os.path.join(save_dir, new_name + ext)):
        os.remove( os.path.join(save_dir, new_name + ext) )

    os.rename(os.path.join(save_dir,uploadedfile.name),
              os.path.join(save_dir, new_name + ext))
    return st.success('Saved file in tmp as [{}]'.format(new_name + ext))


st.subheader('학생 사진 찍기')

col1, col2, col3 = st.columns(3)
hakbun = ''
name = ''
w_hakbun = None
w_name = None
with col1:
    w_hakbun = st.empty()
    hakbun = w_hakbun.text_input('학번', max_chars=4)
with col2:
    w_name = st.empty()
    name = w_name.text_input('성명', max_chars=5)

# 카메라 위젯
picture = st.camera_input("사진 찍기")

if picture:
    if hakbun is None or name is None or len(hakbun) < 4 or len(name) < 2:
        st.warning('학번과 성명을 확인하세요')
        st.stop()

    # st.image(picture)
    save_uploaded_file(picture, hakbun+name)
    hakbun = w_hakbun.text_input('학번', max_chars=4, key='w_hakbun_2')
    name = w_name.text_input('성명', max_chars=5, key='w_name_2')



