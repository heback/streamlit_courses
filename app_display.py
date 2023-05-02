import time
import streamlit as st

st.subheader('st.echo()')
def get_user_name():
    return 'John'

with st.echo():

    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

foo = 'bar'
st.write('Done!')
st.write('='*50)

st.subheader('st.empty()')

placeholder = st.empty()

# Replace the placeholder with some text:
placeholder.text("Hello")

# Replace the text with a chart:
placeholder.line_chart({"data": [1, 5, 2, 6]})

# Replace the chart with several elements:
with placeholder.container():
     st.write("This is one element")
     st.write("This is another")

time.sleep(1)

# Clear all those elements:
placeholder.empty()