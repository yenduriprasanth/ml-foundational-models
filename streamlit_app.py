import streamlit as st
import requests
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

z=requests.get("https://api.fda.gov/drug/label.json?search=openfda.generic_name:'Erlotinib'").json()

st.json(z, *, expanded=True)
