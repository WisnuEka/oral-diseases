import streamlit as st
from streamlit.components.v1 import iframe


st.set_page_config(page_title="Information", page_icon="😊", layout="wide", initial_sidebar_state="collapsed")

# Title
st.markdown(
    """
    <p style='text-align: center; font-size: 2.5rem'>
    <strong>
    Nearby Hospital
    </strong>
    </p>
    """,
    unsafe_allow_html=True,
)

iframe("https://gunungpw.github.io/nearby-map/", height=550)
