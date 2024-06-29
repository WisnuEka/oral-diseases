from os import path

import streamlit as st

script_dir = path.dirname(path.abspath(__file__))
ph_gambar = path.join(script_dir, "../assets/logo.png")

st.set_page_config(page_title="User Guide", page_icon="😊")

# Title
st.markdown("<h1 style='text-align: center;'>PANDUAN PENGGUNAAN</h1>", unsafe_allow_html=True)

# Disini ilustrasi gambar penggunaan
style = "<style>p {text-align: center;}</style>"
with st.columns([3,8,3])[1]:
    st.image(path.join(script_dir, "../assets/guide_images/1.png"))
    st.markdown(style+"<p>Pastikan cahaya cukup untuk mengambil foto dengan jelas</p>", unsafe_allow_html=True)
    
with st.columns([3,8,3])[1]:
    st.image(path.join(script_dir, "../assets/guide_images/2.png"))
    st.markdown(style+"<p>Usahakan pengambilan foto dibantu oleh orang lain</p>", unsafe_allow_html=True)
    
with st.columns([3,8,3])[1]:
    st.image(path.join(script_dir, "../assets/guide_images/3.png"))
    st.markdown(style+"<p>Usahakan hasil foto serupa dengan contoh gambar</p>", unsafe_allow_html=True)

with st.columns([3,8,3])[1]:
    st.image(path.join(script_dir, "../assets/guide_images/4.png"))
    st.markdown(style+"<p>Menuju ke Halaman Upload Page</p>", unsafe_allow_html=True)
    
with st.columns([3,8,3])[1]:
    st.image(path.join(script_dir, "../assets/guide_images/5.png"))
    st.markdown(style+"<p>Pilih Unggah Gambar atau Ambil Foto (lakukan salah satu)</p>", unsafe_allow_html=True)
    
with st.columns([3,8,3])[1]:
    st.image(path.join(script_dir, "../assets/guide_images/8.png"))
    st.markdown(style+"<p>Klik Tombol Submit untuk memulai pengecekan</p>", unsafe_allow_html=True)
    
with st.columns([3,8,3])[1]:
    st.image(path.join(script_dir, "../assets/guide_images/7.png"))
    st.markdown(style+"<p>Pengecekan Selesai, Menampilkan Report </p>", unsafe_allow_html=True)

# Step by step text cara penggunaan
st.caption("_Catatan Penting : .... just in case_")
with st.columns([4,6,4])[1]:
    st.page_link("pages/02-Upload_Photo.py", label=" -> Cek Kesehatan Gigi dan Mulut kamu disini <-")
