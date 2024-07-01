import streamlit as st
from os import path

dir = path.dirname(path.abspath(__file__))
asset_dir = path.join(dir, "../assets/")
st.set_page_config(page_title="Information", page_icon="😊")

st.markdown(
    """
    <p style='text-align: center; font-size: 2.5rem'>
    <strong>
    INFORMATION
    </strong>
    </p>
    """,
    unsafe_allow_html=True,
)

for i in range(1, 9):
    st.image(path.join(asset_dir, f"info_0{i}.png"), use_column_width=True)
