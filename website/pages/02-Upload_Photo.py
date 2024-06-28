import streamlit as st
from azure.cognitiveservices.vision.customvision.prediction import (
    CustomVisionPredictionClient,
)
from msrest.authentication import ApiKeyCredentials
from PIL import Image, ImageDraw

# Replace with your values
PREDICTION_KEY = "ac148f9128e44654b7c102171c0cbd4c"
ENDPOINT = "https://skilvulcustomvision-prediction.cognitiveservices.azure.com"
PROJECT_ID = "d07526a4-69e5-4031-8eaf-2ac073653d5f"
PUBLISHED_NAME = "Iteration1"

prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": PREDICTION_KEY})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)


st.set_page_config(page_title="Upload Photo", page_icon="😊")

st.markdown("<h1 style='text-align: center;'>UPLOAD PHOTO</h1>", unsafe_allow_html=True)


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

# submit input foto/gambar
if st.button("Submit"):
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

            for prediction in result.predictions:
                if prediction.probability < 0.75:
                    pass
                else:
                    draw.rectangle(
                        xy=[
                            int(IMAGE_WIDTH * prediction.bounding_box.left),
                            int(IMAGE_HEIGHT * prediction.bounding_box.top),
                            int(IMAGE_WIDTH * prediction.bounding_box.left)
                            + int(IMAGE_WIDTH * prediction.bounding_box.width),
                            int(IMAGE_HEIGHT * prediction.bounding_box.top)
                            + int(IMAGE_HEIGHT * prediction.bounding_box.height),
                        ],
                        outline="red",
                        width=1,
                    )
            st.image(image_file, use_column_width=True)
