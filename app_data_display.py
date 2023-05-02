import streamlit as st
import pandas as pd

st.title(' Data Display Elements')

st.header('Iris data display')

df = pd.read_csv('iris.csv')
st.subheader('Method 1')
st.dataframe(df)

st.subheader('Method 2')
st.dataframe(df.style.highlight_max(axis=0))

st.subheader('Method 3: static table')
st.table(df)

