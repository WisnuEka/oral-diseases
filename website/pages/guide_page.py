import streamlit as st

# Title
st.title('Panduan Penggunaan App Senyummu')

# Disini ilustrasi gambar penggunaan
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    col1.image('./assets/logo.png', width=150)
    col1.write('ilustrasi 1')
with col2:
    col2.image('./assets/logo.png', width=150)
    col2.write('ilustrasi 2')
with col3:
    col3.image('./assets/logo.png', width=150)
    col3.write('ilustrasi 3')
with col4:
    col4.image('./assets/logo.png', width=150)
    col4.write('ilustrasi 4')
with col5:
    col5.image('./assets/logo.png', width=150)
    col5.markdown("""
                  Ilustrasi 5
                  """)

# Step by step text cara penggunaan 
st.markdown("""
            Step by step / Langkah / Syarat / Lainnya :
            1. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod    
            2. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolo   
            3. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolo   
            4. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolo   
            5. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolo
            """)

st.caption("""
_Catatan Penting :...._
""")
