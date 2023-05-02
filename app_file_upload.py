import streamlit as st
import os
import pandas as pd
import docx2txt as docx2txt
from PyPDF2 import PdfReader
from PIL import Image

@st.cache_data
def load_image(img_file):
    return Image.open(img_file)

def read_pdf(file):
    pdf = PdfReader(file)
    count = len(pdf.pages)
    all_page_text = ''
    for i in range(count):
        page = pdf.pages[i]
        all_page_text += page.extract_text()
    return all_page_text


# 업로드된 파일 저장하기
def save_uploaded_file(uploadedfile):
    with open(os.path.join('tmp', uploadedfile.name), 'wb') as f:
        f.write(uploadedfile.getbuffer())
    return st.success('Saved file : {} in tmp'.format(uploadedfile.name))


st.title('File Upload')
menu = ['Home', 'Dataset', 'DocumentFiles', 'About']
choice = st.sidebar.selectbox('Menu', menu)

if choice == 'Home':
    st.subheader('Home')
    img_file = st.file_uploader('Upload Images',
                                type=['png','jpg','jpeg'])
    if img_file is not None:
        st.write(type(img_file))
        img_details = {'filename': img_file.name,
                       'filetype': img_file.type,
                       'filesize': img_file.size}
        st.write(img_details)
        st.image(load_image(img_file))
        save_uploaded_file(img_file)

elif choice == 'Dataset':
    st.subheader('Dataset')
    data_file = st.file_uploader('Upload CSV', type=['csv'])
    if data_file is not None:
        st.write(type(data_file))

        file_details = {'filename': data_file.name,
                       'filetype': data_file.type,
                       'filesize': data_file.size}
        st.write(file_details)

        df = pd.read_csv(data_file)
        st.dataframe(df.describe())
        save_uploaded_file(data_file)

elif choice == 'DocumentFiles':
    st.subheader('DocumentFiles')
    docs_file = st.file_uploader('Upload Document',
                                 type=['pdf','docx','txt'])
    if st.button('Process'):
        if docs_file is not None:
            file_details = {'filename': docs_file.name,
                            'filetype': docs_file.type,
                            'filesize': docs_file.size}
            st.write(file_details)
            if docs_file.type == 'text/plain':
                raw_text = str(docs_file.read(), 'utf-8')
                st.write(raw_text)
            elif docs_file.type == 'application/pdf':
                raw_text = read_pdf(docs_file)
                st.write(raw_text)
            else:
                raw_text = docx2txt.process(docs_file)
                st.write(raw_text)
            save_uploaded_file(docs_file)

else:
    st.subheader('About')
    st.text('대구과학고 교사 이준구')
    st.text('streamlit 실습 코드')