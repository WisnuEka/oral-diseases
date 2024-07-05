import streamlit as st
import requests

st.title("Tanya Orally")

# Initialize the message list
if "message" not in st.session_state:
    st.session_state.message = []

# Display the chat messages from history
for message in st.session_state.message:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# react to user input
if prompt := st.chat_input("Apakah ada yang bisa saya bantu?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.message.append({"role": "user", "content": prompt})

    response = requests.post(
        st.secrets.azure.LANGUAGE_ENDPOINT,
        headers={"Ocp-Apim-Subscription-Key": st.secrets.azure.LANGUAGE_KEY},
        json={"question": prompt,
              "top": 1,
              "includeUnstructuredSources": True,
              "confidenceScoreThreshold": 0.5},
    )

    if response.ok:
        answer = response.json().get("answers")[0].get("answer")
        with st.chat_message("assistant"):
            st.markdown(answer)
        st.session_state.message.append({"role": "assistant", "content": answer})
    else:
        st.error("Failed to get response from the server.")
