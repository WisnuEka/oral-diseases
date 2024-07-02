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

st.subheader("Infografis")
with open(path.join(asset_dir, "information.pdf"), mode="rb") as d_file:
    st.download_button(
        label="Download Infografis PDF",
        data=d_file,
        file_name="information.pdf",
        mime="application/pdf",
    )

st.image(path.join(asset_dir, "information.png"), use_column_width=True)


st.subheader("Poster")
with open(path.join(asset_dir, "poster_01.pdf"), mode="rb") as d_file:
    st.download_button(
        label="Download Poster PDF",
        data=d_file,
        file_name="poster_01.pdf",
        mime="application/pdf",
    )

st.image(path.join(asset_dir, "poster_01.jpg"), use_column_width=True)
