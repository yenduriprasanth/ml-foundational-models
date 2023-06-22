import streamlit as st
import requests

with st.form("my_form"):
    st.header("Med Affairs Outreach Email Content Generator")
    st.text_input("Please enter Patient Id", key="id")
    st.text_input("Please enter Number of Results", key="n_results")
    submitted = st.form_submit_button("Submit")

# You can access the value at any point with:
#st.session_state.name
def func():
    z=requests.post("https://api.npdata.guardanthealth.com/dev/foundational-models/email",json={"patient_id": st.session_state.id})
    #return z.json()['draft_email']
    return z

if submitted:
    z=func()
    st.title("Here's the email content ")
    #st.json(z, expanded=True)
    for i in range(int(st.session_state.n_results)):
        z.json()
        print("/n")
    
