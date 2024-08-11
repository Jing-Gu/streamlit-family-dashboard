import streamlit as st

st.set_page_config(
    page_title="Camera",
    page_icon="📷",
)

st.title("Take a selfie 📷")

with st.expander("Start the camera"):
    # Start the webcam
    selfie = st.camera_input("Camera")

# Render image on the webpage
if selfie:
    st.image(selfie)
