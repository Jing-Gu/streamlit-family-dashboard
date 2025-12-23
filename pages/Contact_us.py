import streamlit as st

st.set_page_config(
    page_title="Contact us",
    page_icon="📬",
)

st.title("Contact us 📬")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        message = message + user_email