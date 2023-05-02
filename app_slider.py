import streamlit as st

age = st.slider('How old are you?', 1, 120, 18)
st.write("I'm ", age, 'years old')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

from datetime import time
appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

from datetime import datetime
start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

color = st.select_slider(
     'Select a color of the rainbow',
     options=['red', 'orange', 'yellow',
              'green', 'blue', 'indigo',
              'violet'])
st.write('My favorite color is', color)

