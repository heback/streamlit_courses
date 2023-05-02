import streamlit as st
import os
from PIL import Image

@st.cache
def load_image(img_file):
    return Image.open(img_file)

def save_uploaded_file(uploaded_file):
    with open(os.path.join('tmp', uploaded_file), 'wb') as f:
        f.write(uploaded_file.getbuffer())
    return st.success('Saved file : {} in tmp'.format(uploaded_file.name))

st.title('Multiple File Upload')
menu = ['Home', 'About']
choice = st.sidebar.selectbox('Menu', menu)

if choice == 'Home':
    st.subheader('Upload Multiple Files')

    uploaded_files = st.file_uploader('Upload Multiple Images',
                                      type=['png','jpg','jpeg'],
                                      accept_multiple_files=True)
    if uploaded_files is not None and len(uploaded_files) != 0:
        st.write(uploaded_files)
        for img_file in uploaded_files:
            st.write(img_file.name)
            st.image(load_image(img_file))

else:
    st.subheader('About App')
