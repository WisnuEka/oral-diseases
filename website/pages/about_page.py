import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="About",
)

st.markdown("<h1 style='text-align: center; color: white;'>ABOUT PAGE</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: white;'>SENYUMMU</h1>", unsafe_allow_html=True)

st.write("""
         Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
         labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
         reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
         """)

st.markdown("<h2 style='text-align: center; color: white;'>OUR TEAM</h1>", unsafe_allow_html=True)

st.write(""" ## DATA """)

columns = st.columns((1,1,1))

with columns[0]:
    img = Image.open("/workspaces/codespaces-blank/image/our team/Gishel.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Gishelawati """)
with columns[0]:
    img = Image.open("/workspaces/codespaces-blank/image/our team/kageyama.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Adi Kurniawan """)
with columns[1]:
    img = Image.open("/workspaces/codespaces-blank/image/our team/kageyama.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Bagus Akhlaq""")
with columns[2]:
    img = Image.open("/workspaces/codespaces-blank/image/our team/Nibras.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Nibras Alfaruqiyah""")
with columns[2]:
    img = Image.open("/workspaces/codespaces-blank/image/our team/kageyama.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Azhani Syahputra""")

st.write(""" ## AI """)

columns = st.columns((1,1,1))

with columns[0]:
    img = Image.open("/workspaces/codespaces-blank/image/our team/Gunung.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Gunung Pambudi Wibisono """)
with columns[0]:
    img = Image.open("/workspaces/codespaces-blank/image/our team/Wisnu.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Wisnu Eka Saputra S.""")
with columns[1]:
    img = Image.open("/workspaces/codespaces-blank/image/our team/kageyama.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Aisyah Amalia Al Fitri""")
with columns[2]:
    img = Image.open("/workspaces/codespaces-blank/image/our team/Vauwez.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Vauwez Sam El Fareez """)
with columns[2]:
    img = Image.open("/workspaces/codespaces-blank/image/our team/kageyama.png")
    img_resized = img.resize((400, 600))
    st.image(img_resized)
    st.write(""" Irvan Achmad Ashari""")



