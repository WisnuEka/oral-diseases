from os import path

import streamlit as st

dir = path.dirname(path.abspath(__file__))
asset_dir = path.join(dir, "../assets/")
st.set_page_config(page_title="User Guide", page_icon="😊")

# Title
st.markdown(
    """
    <p style='text-align: center; font-size: 2.5rem'>
    <strong>
    PANDUAN PENGGUNAAN
    </strong>
    </p>
    """,
    unsafe_allow_html=True,
)

st.markdown(" ")

step_data = (
    (
        "step_1",
        "Pastikan Cahaya Cukup",
        """Pastikan ruangan atau lokasi pengambilan foto memiliki pencahayaan yang cukup untuk
        menghasilkan foto yang jelas.""",
    ),
    (
        "step_2",
        "Minta Bantuan Orang Lain",
        """Usahakan pengambilan foto dilakukan dengan bantuan orang lain agar hasil foto
        lebih baik dan sesuai.""",
    ),
    (
        "step_3",
        "Sesuaikan dengan Contoh Gambar",
        """Usahakan hasil foto serupa dengan contoh gambar yang telah disediakan.""",
    ),
    ("step_4", "Klik Menu Upload Photo", """Buka halaman pengunggahan dengan mengklik menu **Upload Photo**."""),
    ("step_5", "Klik Tab Upload Photo", """Setelah berada di halaman pengunggahan, klik Tab **Upload Photo**."""),
    (
        "step_6",
        "Klik Tombol Browse Files",
        """Untuk memilih gambar yang akan diunggah, klik tombol **Browse Files**.""",
    ),
    ("step_7", "Pilih Gambar dari Gallery", """Cari dan pilih gambar yang sudah diambil sesuai petunjuk."""),
    (
        "step_8",
        "Klik Tombol Submit",
        """Setelah memilih gambar, klik tombol **Submit** untuk mengunggah gambar tersebut.""",
    ),
)

# Step by step text cara penggunaan
for step in step_data:
    columns = st.columns((0.2, 0.5), vertical_alignment="center", gap="small")
    with columns[0]:
        st.image(path.join(asset_dir, f"{step[0]}.png"))
    with columns[1]:
        st.subheader(f"**{step[1]}**")
        st.success(f"_{step[2]}_", icon=":material/info:")
    st.divider()

with st.container(border=True):
    st.page_link(
        "site/02-Upload_Photo.py",
        label=":blue-background[UPLOAD PHOTO]",
        icon=":material/chevron_right:",
    )
