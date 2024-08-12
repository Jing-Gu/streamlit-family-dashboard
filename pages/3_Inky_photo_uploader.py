import streamlit as st


st.set_page_config(
    page_title="Inky photo uploader",
    page_icon="🏞",
)

st.title("Inky photo uploader 🏞")

uploaded_file = st.file_uploader(label="Choose a file", label_visibility="hidden")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)