import streamlit as st
import numpy as np

col1, col2 = st.columns(2)

with col1:
    st.subheader('col1')
    with st.container():
        st.write("This is inside the container")
        st.bar_chart(np.random.randn(20, 3))

    st.write("This is outside the container")

with col2:
    st.subheader('col2')
    container = st.container()
    container.write("1. This is inside the container")
    st.write("2. This is outside the container")

    # Now insert some more in the container
    container.write("3. This is inside too")
