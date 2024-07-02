from os.path import abspath, dirname, join

import streamlit as st
from azure.cognitiveservices.vision.customvision.prediction import (
    CustomVisionPredictionClient,
)
from msrest.authentication import ApiKeyCredentials
from PIL import Image, ImageDraw

dir = dirname(abspath(__file__))

# Replace with your values
PREDICTION_KEY = st.secrets.azure.PREDICTION_KEY
ENDPOINT = st.secrets.azure.ENDPOINT
PROJECT_ID = st.secrets.azure.PROJECT_ID
PUBLISHED_NAME = st.secrets.azure.PUBLISHED_NAME

prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": PREDICTION_KEY})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)


def mark(tag_name, width, height, b_left, b_top, b_width, b_height):
    color = None
    line_width = 2

    if width <= 400 or height <= 300:
        line_width = 1
    elif 401 <= width <= 800 or 301 <= height <= 600:
        line_width = 2
    else:
        line_width = 3

    if tag_name == "Caries":
        color = "red"
    elif tag_name == "Gingivitis":
        color = "blue"
    elif tag_name == "Tooth Discoloration":
        color = "purple"
    elif tag_name == "Ulcer":
        color = "yellow"
    else:
        color = "black"

    draw.rectangle(
        xy=[
            int(width * b_left),
            int(height * b_top),
            int(width * b_left) + int(width * b_width),
            int(height * b_top) + int(height * b_height),
        ],
        outline=color,
        width=line_width,
    )


st.set_page_config(page_title="Upload Photo", page_icon="😊")

st.markdown(
    """
    <p style='text-align: center; font-size: 2.5rem;'>
    <strong>
    UPLOAD PHOTO
    </strong>
    </p>
    """,
    unsafe_allow_html=True,
)


UploadPhoto, TakePhoto = st.tabs(["**Upload Photo**", "**Take Photo**"])

# Upload image
with UploadPhoto:
    uploaded_image = st.file_uploader("_Choose a Photo_", type=["png", "jpg", "jpeg"], accept_multiple_files=False)
    if uploaded_image is not None:
        st.image(uploaded_image, use_column_width=True)
        submitted_image = uploaded_image

# Camera Input
with TakePhoto:
    uploaded_image = st.camera_input("_Take a Photo_")
    if uploaded_image is not None:
        st.image(uploaded_image, use_column_width=True)
        submitted_image = uploaded_image

prob = st.slider("_Confidence Level_", min_value=0, max_value=100, step=5, value=(50, 100))

col = st.columns(2, gap="medium")
with col[0]:
    detect_options = st.multiselect(
        "_Select Diseases_",
        ["Caries", "Ulcer", "Gingivitis", "Tooth Discoloration"],
        ["Caries", "Ulcer", "Gingivitis", "Tooth Discoloration"],
    )
with col[1]:
    report_mode = st.radio(
        "_Choose Report Detail_",
        ["Normal", "Annotation", "Raw Data", "All"],
        captions=[
            "Report berisi semua informasi penting",
            "Report hanya berisi _marked_ foto",
            "Report hanya berisi detail _bounding box_",
            "Report berisi semua informasi",
        ],
    )

# submit input foto/gambar
if st.button("Submit", type="primary"):
    st.session_state.name = "Submit"
    with st.spinner("Processing..."):
        try:
            image_file = Image.open(submitted_image)
        except NameError:
            st.error("**Foto Belum di Unggah!!!**", icon=":material/error:")
        else:
            bytes_image = submitted_image.getbuffer()
            IMAGE_HEIGHT = image_file.height
            IMAGE_WIDTH = image_file.width

            # Create a drawing context
            draw = ImageDraw.Draw(image_file)

            result = predictor.detect_image(
                project_id=PROJECT_ID,
                published_name=PUBLISHED_NAME,
                image_data=bytes_image,
            )

            find = []
            tags = []
            for prediction in result.predictions:
                find.append(f"{prediction.tag_name}, {prediction.probability * 100:.2f}%")
                if (
                    prediction.probability >= prob[0] / 100
                    and prediction.probability <= prob[1] / 100
                    and prediction.tag_name in detect_options
                ):
                    if prediction.tag_name not in tags:
                        tags.append(prediction.tag_name)
                    mark(
                        tag_name=prediction.tag_name,
                        width=IMAGE_WIDTH,
                        height=IMAGE_HEIGHT,
                        b_top=prediction.bounding_box.top,
                        b_left=prediction.bounding_box.left,
                        b_width=prediction.bounding_box.width,
                        b_height=prediction.bounding_box.height,
                    )
                else:
                    pass

            st.header("Hasil Analisis")
            st.markdown("")
            st.image(image_file, use_column_width=True)
            st.markdown("")
            if report_mode in ["Normal", "Only Annotation", "Raw Data", "All"]:
                with st.expander("Legend", icon=":material/format_list_bulleted:", expanded=True):
                    legend = [
                        ":red-background[Merah = Caries]",
                        ":orange-background[Kuning = Ulcer]",
                        ":blue-background[Biru = Gingivitis]",
                        ":violet-background[Ungu = Tooth Discoloration]",
                    ]
                    for el in legend:
                        st.caption(f"{el}")
            if report_mode in ["Raw Data", "All"]:
                with st.expander("Raw Data", icon=":material/info:"):
                    st.write(find)
                    st.write(tags)

            if report_mode in ["Normal", "All"]:
                st.header("Report")
                if "Caries" in tags:
                    with st.expander("Caries Report", icon=":material/arrow_forward_ios:"):
                        st.header("Caries")
                        with open(join(dir, "../assets/report_caries.pdf"), mode="rb") as d_file:
                            st.download_button(
                                label="Download Caries Report PDF",
                                data=d_file,
                                file_name="report_caries.pdf",
                                mime="application/pdf",
                            )

                        with open(join(dir, "../assets/caries.md"), mode="r") as docs:
                            st.markdown(docs.read())
                if "Gingivitis" in tags:
                    with st.expander("Gingivitis Report", icon=":material/arrow_forward_ios:"):
                        st.header("Gingivitis")
                        with open(join(dir, "../assets/report_gingivitis.pdf"), mode="rb") as d_file:
                            st.download_button(
                                label="Download Gingivitis Report PDF",
                                data=d_file,
                                file_name="report_gingivitis.pdf",
                                mime="application/pdf",
                            )
                        with open(join(dir, "../assets/gingivitis.md"), mode="r") as docs:
                            st.markdown(docs.read())
                if "Ulcer" in tags:
                    with st.expander("Ulcer Report", icon=":material/arrow_forward_ios:"):
                        st.header("Ulcer")
                        with open(join(dir, "../assets/report_ulcer.pdf"), mode="rb") as d_file:
                            st.download_button(
                                label="Download Ulcer Report PDF",
                                data=d_file,
                                file_name="report_ulcer.pdf",
                                mime="application/pdf",
                            )
                        with open(join(dir, "../assets/ulcer.md"), mode="r") as docs:
                            st.markdown(docs.read())
                if "Tooth Discoloration" in tags:
                    with st.expander("Tooth Discoloration Report", icon=":material/arrow_forward_ios:"):
                        st.header("Tooth Discoloration")
                        with open(join(dir, "../assets/report_tooth_discoloration.pdf"), mode="rb") as d_file:
                            st.download_button(
                                label="Download Tooth Discoloration Report PDF",
                                data=d_file,
                                file_name="report_tooth_discoloration.pdf",
                                mime="application/pdf",
                            )
                        with open(join(dir, "../assets/tooth_discoloration.md"), mode="r") as docs:
                            st.markdown(docs.read())
                if tags == []:
                    st.success("Selamat Gigi Anda Sehat", icon=":material/sentiment_very_satisfied:")
