import streamlit as st
from os import path

script_dir = path.dirname(path.abspath(__file__))

st.set_page_config(page_title="Senyummu", page_icon="😊")

st.image(path.join(script_dir, "../assets/hero_banner_v2.png"))

st.markdown("")
st.divider()
st.markdown(
    """
    <p style='text-align: center; font-size: 1.1rem;'>
    <strong>Senyummu</strong> adalah aplikasi yang digunakan
    untuk mendeteksi penyakit dan kerusakan gigi melalui analisis foto gigi. Aplikasi
    ini memberikan diagnosis akurat dan rekomendasi perawatan yang tepat, membantu pengguna
    menjaga kesehatan gigi dengan lebih mudah dan efektif.
    </p>
    """,
    unsafe_allow_html=True,
)
st.divider()

st.write("## Feature")

st.markdown("")

first = st.columns(3, gap="medium", vertical_alignment="center")
second = st.columns(3, gap="medium", vertical_alignment="center")

with first[0]:
    st.image(path.join(script_dir, "../assets/f_bolt.png"))
    st.text("➜ INSTANT ANALYSIS")
with first[1]:
    st.image(path.join(script_dir, "../assets/f_money.png"))
    st.text("➜ MULTI-FILE PROCESSING")
with first[2]:
    st.image(path.join(script_dir, "../assets/f_time.png"))
    st.text("➜ ASK ORALLY")
with second[0]:
    st.image(path.join(script_dir, "../assets/f_target.png"))
    st.text("➜ NEARBY HOSPITAL")
with second[1]:
    st.image(path.join(script_dir, "../assets/f_privacy.png"))
    st.text("➜ PRIVACY-FIRST")
with second[2]:
    st.image(path.join(script_dir, "../assets/f_friendly.png"))
    st.text("➜ USER-FRIENDLY")

st.markdown("")


with st.container(border=True):
    st.page_link(
        "site/01-User_Guide.py",
        label=":blue-background[TRY NOW]",
        icon=":material/chevron_right:",
    )
