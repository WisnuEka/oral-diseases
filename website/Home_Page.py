import streamlit as st
from os import path

script_dir = path.dirname(path.abspath(__file__))

st.set_page_config(page_title="Senyummu", page_icon="😊")


st.markdown("<h1 style='text-align: center;'>SENYUMMU</h1>", unsafe_allow_html=True)

with st.columns(3)[1]:
    st.image(path.join(script_dir, "assets/logo.png"), width=200)

st.write("## Senyummu: Kenali Masalah Mulutmu, Jaga Senyummu")


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

left, middle, right = st.columns(3)

with middle:
    st.page_link("pages/01-User_Guide.py", label="User Guide")
