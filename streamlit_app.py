import streamlit as st
import requests

with st.form("my_form"):
    st.header("Med Affairs Outreach Email Generator")
    st.text_input("Input text", key="name")
    submitted = st.form_submit_button("Submit")

# You can access the value at any point with:
#st.session_state.name
def func():
    z=requests.get("https://api.fda.gov/drug/label.json?search=openfda.generic_name:'Erlotinib'").json()
    return z

if submitted:
    z=func()
    st.title("Email Response")
    st.json(z, expanded=True)
