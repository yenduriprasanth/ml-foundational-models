import streamlit as st
import requests
st.header("Patient Information")
st.text_input("Name", key="name")
st.text_input("Cancer type", key="cancer_type")
st.text_input("Alteration", key="alteration")
st.text_input("Approved therapy", key="therapy")
st.text_input("Diagnostic type", key="diagnostic_type")

# You can access the value at any point with:
#st.session_state.name
def func():
    z=requests.get("https://api.fda.gov/drug/label.json?search=openfda.generic_name:'Erlotinib'").json()
    return z

st.form_submit_button(label="Submit", on_click=func())

st.title("Email Response")
st.json(z, expanded=True)
