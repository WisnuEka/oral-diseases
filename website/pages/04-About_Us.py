import streamlit as st
from os import path

dir = path.dirname(path.abspath(__file__))
image_path = path.join(dir, "../assets/profile2.jpeg")


st.set_page_config(page_title="About Us", page_icon="😊")

st.markdown("<h1 style='text-align: center;'>ABOUT US</h1>", unsafe_allow_html=True)

st.markdown("### OUR MISSION")

st.markdown(
    """
    <blockquote style='text-align: center; font-size: 1.75rem; font-family: serif'>
    <i>
    Misi kami adalah menyediakan akses yang mudah dan terjangkau bagi seluruh lapisan
    masyarakat untuk memantau dan meningkatkan kesehatan gigi mereka secara mandiri,
    didukung oleh teknologi AI terdepan yang revolusioner dan inovatif.
    </i>
    </blockquote>
    """,
    unsafe_allow_html=True,
)

st.markdown("### OUR TEAM")

st.write("## AI")

data_team_ai = {
    "Gunung Pambudi Wibisono": [
        "../assets/profile.png",
        "gunungpambudiw@gmail.com",
        "https://www.linkedin.com/in/gunungpw/",
    ],
    "Wisnu Eka Saputra. S": [
        "../assets/profile.png",
        "wisnuekasaputra@hotmail.com",
        "https://id.linkedin.com/in/wisnuekasaputra",
    ],
    "Vauwez Sam El Fareez": [
        "../assets/profile.png",
        "vsefareez@outlook.com",
        "https://www.linkedin.com/in/samfareez/",
    ],
    "Aisyah Amalia Al Fitri": ["../assets/profile.png", "arsyah291200@gmail.com", "linkedin.com"],
    "Irvan Achmad Ashari": [
        "../assets/profile.png",
        "irvanachmadashari@gmail.com",
        "https://www.linkedin.com/in/maragopan",
    ],
}

for person in data_team_ai:
    columns = st.columns((0.3, 0.7), vertical_alignment="center")
    with columns[0]:
        st.image(image_path)
    with columns[1]:
        st.write(person)
        for i, info in enumerate(data_team_ai.get(person)):
            if i == 0:
                pass
            elif i == 2:
                st.page_link(info, label="Linkedin")
            else:
                st.write(info)


# with columns[0]:
#     st.image(image_path)
#     st.write("Gunung Pambudi Wibisono")
# with columns[0]:
#     st.image(image_path)
#     st.write("Wisnu Eka Saputra S.")
# with columns[1]:
#     st.image(image_path)
#     st.write("Aisyah Amalia Al Fitri")
# with columns[2]:
#     st.image(image_path)
#     st.write("Vauwez Sam El Fareez")
# with columns[2]:
#     st.image(image_path)
#     st.write("Irvan Achmad Ashari")


# st.write("#### Team Data")

# columns = st.columns((1, 1, 1))

# with columns[0]:
#     st.image(image_path)
#     st.write("Gishelawati")
# with columns[0]:
#     st.image(image_path)
#     st.write("Adi Kurniawan")
# with columns[1]:
#     st.image(image_path)
#     st.write("Bagus Akhlaq")
# with columns[2]:
#     st.image(image_path)
#     st.write("Nibras Alfaruqiyah")
# with columns[2]:
#     st.image(image_path)
#     st.write("Azhani Syahputra")
