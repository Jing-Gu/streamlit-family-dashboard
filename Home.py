import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title("Family Dashboard 👋")

st.markdown(
    """
    ### Toolbox
    - Selfie Camera
    - Shopping list
    """
)

col1, col2 = st.columns(2)

with col1:
    # st.image("images/photo.png")
    st.write("col one")

with col2:
    st.subheader("introduction")
    content = """
    Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
    """
    st.info(content)



