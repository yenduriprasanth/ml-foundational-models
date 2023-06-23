import streamlit as st
import requests
import streamlit.components.v1 as components

with st.form("my_form"):
    st.header("Med Affairs Outreach Email Content Generator")
    st.text_input("Please enter Patient Id", key="id")
    #st.text_input("Please enter Number of Results", key="n_results")
    submitted = st.form_submit_button("Submit")

# You can access the value at any point with:
#st.session_state.name
def func():
    z=requests.post("https://api.npdata.guardanthealth.com/dev/foundational-models/email",json={"patient_id": st.session_state.id})
    #return z.json()['draft_email']
    return z.json()['draft_email']

def ChangeButtonColour(widget_label, font_color, background_color='transparent'):
    htmlstr = f"""
        <script>
            var elements = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < elements.length; ++i) {{ 
                if (elements[i].innerText == '{widget_label}') {{ 
                    elements[i].style.color ='{font_color}';
                    elements[i].style.background = '{background_color}'
                }}
            }}
        </script>
        """
    components.html(f"{htmlstr}", height=0, width=0)




if submitted:
    z=func()
    st.title("Here's the email content ")
    z
    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        st.button('Edit')
    with col2:
        st.button('Approve')
    with col3:
        st.button('Reject')
    ChangeButtonColour('Edit', 'red', 'blue')

#[st.button('Edit') ,    st.button('Approve')   , st.button('Reject')]
    #st.json(z, expanded=True)
    #for i in range(int(st.session_state.n_results)):
    #    z[i]
    #    print("/n")
    
