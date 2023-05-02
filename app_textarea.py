import streamlit as st

txt = st.text_area('Text to analyze',
    # value
    'It was the best of times, it was the worst of times, it was'
    'the age of wisdom, it was the age of foolishness, it was'
    'the epoch of belief, it was the epoch of incredulity, it'
    'was the season of Light, it was the season of Darkness, it'
    'was the spring of hope, it was the winter of despair, (...)')

st.download_button('Download your text', txt,
                   file_name='MyText.txt')

import pandas as pd

df = pd.read_csv('data/iris.csv')
st.dataframe(df)
st.download_button(
    'Download data to csv',
    df.to_csv().encode(encoding='utf-8'),
    file_name='iris.csv',
    mime='text/csv'
)

from PIL import Image

img = Image.open('data/image_01.jpg')
st.image(img)

st.download_button(
    'Download this image',
    data=open('data/image_01.jpg', 'rb'),
    file_name='Image.jpg',
    mime='image/jpg'
)


