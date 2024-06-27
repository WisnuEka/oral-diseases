import streamlit as st
from os import path

script_dir = path.dirname(path.abspath(__file__))

st.set_page_config(
    page_title="Senyummu",
    page_icon="😊",
)

with st.columns(3)[1]:
    st.write("## SENYUMMU")
    st.image(path.join(script_dir, "assets/logo.png"), width=200)
    st.write("## Tag Liner")


st.markdown(
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
    nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
    reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
    pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
    culpa qui officia deserunt mollit anim id est laborum.
"""
)
with st.columns(3)[1]:
    st.page_link("pages/upload_page.py", label="Upload Image", use_container_width=True)
