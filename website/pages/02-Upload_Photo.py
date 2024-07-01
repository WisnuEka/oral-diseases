import streamlit as st
from azure.cognitiveservices.vision.customvision.prediction import (
    CustomVisionPredictionClient,
)
from msrest.authentication import ApiKeyCredentials
from PIL import Image, ImageDraw
from report import caries, gingivitis, ulcer, tooth_discoloration

# Replace with your values
PREDICTION_KEY = "ac148f9128e44654b7c102171c0cbd4c"
ENDPOINT = "https://skilvulcustomvision-prediction.cognitiveservices.azure.com"
PROJECT_ID = "d07526a4-69e5-4031-8eaf-2ac073653d5f"
PUBLISHED_NAME = "Iteration1"

prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": PREDICTION_KEY})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)


def mark(tag_name, width, height, b_left, b_top, b_width, b_height):
    color = None
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
        width=2,
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
        ["Normal", "Only Annotation", "Raw Data", "All"],
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

            st.divider()
            st.header("Hasil Analisis")
            st.markdown("")
            st.image(image_file, use_column_width=True)
            st.markdown("")
            if report_mode in ["Normal", "Only Annotation", "Raw Data", "All"]:
                with st.container(border=True):
                    st.markdown(
                        """
                        Keterangan:
                        - :violet-background[Ungu = Tooth Discoloration]
                        - :orange-background[Kuning = Ulcer]
                        - :red-background[Merah = Caries]
                        - :blue-background[Biru = Gingivitis]
                        """
                    )
            if report_mode in ["Raw Data", "All"]:
                st.write(find)
                st.write(tags)

            if report_mode in ["Normal", "All"]:
                st.divider()
                st.header("Report")
                if "Caries" in tags:
                    st.header("Caries")
                    st.markdown(caries)
                    st.divider()
                if "Gingivitis" in tags:
                    st.header("Gingivitis")
                    st.markdown(gingivitis)
                    st.divider()
                if "Ulcer" in tags:
                    st.header("Ulcer")
                    st.markdown(ulcer)
                    st.divider()
                if "Tooth Discoloration" in tags:
                    st.header("Tooth Dicoloration")
                    st.markdown(tooth_discoloration)
                    st.divider()
                if tags == []:
                    st.success("Selamat Gigi Anda Sehat")
                    st.divider()
