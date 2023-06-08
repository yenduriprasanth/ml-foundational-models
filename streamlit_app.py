import streamlit as st
import requests
from PIL import Image

image = Image.open('friendly-chatbot.jpg')

st.image(image, caption='Sunrise by the mountains')

with st.form("my_form"):
    st.header("Med Affairs Outreach Email Generator")
    st.text_input("Input text", key="name")
    submitted = st.form_submit_button("Submit")

# You can access the value at any point with:
#st.session_state.name
def func():
    z=requests.post("https://api.hackathon.guardanthealth.com/dev/foundational-models/email")
    return z.text

if submitted:
    z=func()
    st.title("Email Response")
    #st.json(z, expanded=True)
    z
