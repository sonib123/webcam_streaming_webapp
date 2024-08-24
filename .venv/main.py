import cv2
import streamlit as st
from datetime import datetime

st.title("Motion Detector")
start = st.button('Start Camera')

if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Get the current time
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Display the current time on the frame
        cv2.putText(img=frame, text=current_time, org=(50, 50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(20, 100, 200),
                    thickness=2, lineType=cv2.LINE_AA)

        # Update the image in Streamlit
        streamlit_image.image(frame)
