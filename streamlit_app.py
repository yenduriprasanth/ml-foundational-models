import streamlit as st
import requests

with st.form("my_form"):
    st.header("Med Affairs Outreach Email Generator")
    option = st.selectbox(
        'Patient Name',
        ('James', 'Warren'))
    submitted = st.form_submit_button("Submit")

# You can access the value at any point with:
#st.session_state.name
def func():
    z=requests.post("https://api.hackathon.guardanthealth.com/dev/foundational-models/email",json={"patient_id": option})
    return z.json()['draft_email']

if submitted:
    z=func()
    st.title("Email Response")
    #st.json(z, expanded=True)
    z
