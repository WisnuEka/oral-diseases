import streamlit as st
import requests

from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem
from azure.core.exceptions import HttpResponseError

credential = TranslatorCredential(st.secrets.azure.TRANSLATOR_KEY, st.secrets.azure.REGION)
text_translator = TextTranslationClient(endpoint=st.secrets.azure.TRANSLATOR_ENDPOINT, credential=credential)

# Title
st.markdown(
    """
    <p style='text-align: center; font-size: 2.5rem'>
    <strong>
    Ask Orally
    </strong>
    </p>
    """,
    unsafe_allow_html=True,
)

# Initialize the message list
if "message" not in st.session_state:
    st.session_state.message = []

# Display the chat messages from history
for message in st.session_state.message:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


def translate(text, from_param, to):
    try:
        result = text_translator.translate(content=[InputTextItem(text=text)], to=[to], from_parameter=from_param)
        translation = result[0] if result else None
        if translation:
            return translation.translations[0].text
    except HttpResponseError as e:
        print(f"Error Code: {e.error.code}")
        print(f"Message: {e.error.message}")


# react to user input
if prompt := st.chat_input("Apakah ada yang bisa saya bantu?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.message.append({"role": "user", "content": prompt})

    # translate the prompt to English
    prompt = translate(prompt, "id", "en")

    response = requests.post(
        st.secrets.azure.LANGUAGE_ENDPOINT,
        headers={"Ocp-Apim-Subscription-Key": st.secrets.azure.LANGUAGE_KEY},
        json={"question": prompt, "top": 1, "includeUnstructuredSources": True, "confidenceScoreThreshold": 0.5},
    )

    if response.ok:
        answer = response.json().get("answers")[0].get("answer")

        # Translate the answer to Indonesian
        answer = translate(answer, "en", "id")

        # Display the answer
        with st.chat_message("assistant"):
            st.markdown(answer)
        st.session_state.message.append({"role": "assistant", "content": answer})
    else:
        st.error("Failed to get response from the server.")
