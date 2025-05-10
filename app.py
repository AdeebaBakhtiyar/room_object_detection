import os
import cv2
import streamlit as st
import tempfile
from PIL import Image
from detect import detect_objects
from chatbot import simple_chatbot
from speak import speak
from streamlit.components.v1 import html

st.set_page_config(page_title = "Room Object Detection with voice assistant")
st.title("Room object detection")

FRAME_WINDOW = st.image([])

camera = st.camera_input("Capture Image")

if camera:
    img = Image.open(camera)
    st.image(img, caption="Image captured", use_column_width=True)

    labels = detect_objects(img)
    st.success(f"Detected Objects: {', '.join(labels) if labels else 'None'}")

    chat = simple_chatbot(labels)
    st.info(f"Chatbot: {chat}")

    audio_path = speak(chat)
    audio_file = opejn(audio_path, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
    audio_file.close()
    os.remove(audio_path)
