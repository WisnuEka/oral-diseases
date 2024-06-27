import streamlit as st
import time

st.title("Upload Foto")
tab1, tab2 = st.tabs(["Ambil Foto", "Unggah Gambar"])

# Camera Input
with tab1:
    captured_image = st.camera_input(
        "Ambil Foto",
    )
    if captured_image:
        with st.spinner("Processing.."):
            time.sleep(1)
            st.image(captured_image)
        submitted = captured_image

# Upload image
with tab2:
    uploaded_image = st.file_uploader("Unggah Gambar", type=["png", "jpg"])
    if uploaded_image:
        with st.spinner("Processing.."):
            time.sleep(1)
            st.image(uploaded_image)
        submitted = uploaded_image

# submit input foto/gambar
if st.button("Submit"):
    # seharusnya disini proses olah gambarnya nanti
    st.session_state.name = "Submit"
    with st.spinner("Processing"):
        time.sleep(1)
    st.image(submitted)
