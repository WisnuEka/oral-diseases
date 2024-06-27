import streamlit as st
import time
from os import path
from PIL import Image, ImageDraw

from azure.cognitiveservices.vision.customvision.prediction import (
    CustomVisionPredictionClient,
)
from msrest.authentication import ApiKeyCredentials

dir = path.dirname(path.abspath(__file__))

# Replace with your values
PREDICTION_KEY = "ac148f9128e44654b7c102171c0cbd4c"
ENDPOINT = "https://skilvulcustomvision-prediction.cognitiveservices.azure.com"
PROJECT_ID = "d07526a4-69e5-4031-8eaf-2ac073653d5f"
PUBLISHED_NAME = "Iteration1"


prediction_credentials = ApiKeyCredentials(
    in_headers={"Prediction-key": PREDICTION_KEY}
)
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

st.title("Upload Foto")
tab1, tab2 = st.tabs(["Ambil Foto", "Unggah Gambar"])

# Camera Input
with tab1:
    captured_image = st.camera_input("Ambil Foto")
    if captured_image:
        with st.spinner("Processing.."):
            time.sleep(1)
            st.image(captured_image)
            submitted_image = captured_image

# Upload image
with tab2:
    uploaded_image = st.file_uploader("Unggah Gambar", type=["png", "jpg"])
    if uploaded_image:
        with st.spinner("Processing.."):
            time.sleep(1)
            st.image(uploaded_image)
            submitted_image = uploaded_image

# submit input foto/gambar
if st.button("Submit"):
    submitted_image.seek(0)
    image_file = Image.open(submitted_image)
    bytes_image = bytes(image_file.tobytes())
    IMAGE_HEIGHT = image_file.height
    IMAGE_WIDTH = image_file.width

    # Create a drawing context
    draw = ImageDraw.Draw(image_file)

    st.session_state.name = "Submit"
    with st.spinner("Processing..."):
        result = predictor.detect_image(
            project_id=PROJECT_ID,
            published_name=PUBLISHED_NAME,
            image_data=bytes_image,
        )

        for prediction in result.predictions:
            if prediction.probability < 0.75:
                pass
            else:
                print(
                    "\t"
                    + prediction.tag_name
                    + ": {0:.2f}% bbox.left = {1:.2f}, bbox.top = {2:.2f}, bbox.width = {3:.2f}, bbox.height = {4:.2f}".format(
                        prediction.probability,
                        prediction.bounding_box.left,
                        prediction.bounding_box.top,
                        prediction.bounding_box.width,
                        prediction.bounding_box.height,
                    )
                )
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
        st.image(image_file)
