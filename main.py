# # Imports that r necessary to install
# pip install streamlit
# pip install qrcode
# pip install numpy
# pip install opencv-python

import streamlit as st
import numpy as np
import qrcode
import cv2
from PIL import Image
import io

# Function to load image from a URL or file uploader

def load_image(image_file):
    """
    This function loads an image from a URL or file uploader.

    :param image_file: The image file to be loaded.
    :return: The loaded image.
    """

    img = Image.open(image_file)
    return img

# Main Function
def main():

    """
    The main function that contains the main logic of the application.

    """
    
    opencv_image = None
    menu = ["Home", "DecodeQR", "About"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        st.write("Welcome to QR Code App")

        # Text input
        with st.form(key='myqr_form'):
            text = st.text_area(label='Enter Text')
            submit_button = st.form_submit_button(label='Generate QR Code')

        # Layout
        if submit_button:
            col1, col2 = st.columns(2)

            with col1:
                st.info("QR Code")
                qr_code = qrcode.make(text)
                qr_code_bytes = io.BytesIO()
                qr_code.save(qr_code_bytes, format='PNG')
                st.image(qr_code_bytes)

            with col2:
                st.info("Original Text")
                st.write(text)

    elif choice == "DecodeQR":
        st.subheader("DecodeQR")
        st.write("Upload QR Code Image")
        img_file = st.file_uploader("Choose a QR Code Image", type=['png', 'jpg', 'jpeg'])

        if img_file is not None:
            # Method 2: Using OpenCV
            file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
            opencv_image = cv2.imdecode(file_bytes, 1)

            c1, c2 = st.columns(2)

            with c1:
                st.info("QR Code Image")
                st.image(opencv_image, channels='BGR')

            with c2:
                st.info("QR Code Data")
                detector = cv2.QRCodeDetector()
                retval, points, straight_qrcode = detector.detectAndDecode(opencv_image)
                st.write(retval)

    else:
        st.subheader("About")
        st.markdown(
            """
            🎉 Welcome to the QR Code App! 🎉\n
            This app allows you to generate QR codes from text and decode QR codes from images.\n
            With a simple and intuitive interface, you can create and scan QR codes easily!\n\n
            🌟 **Key Features** 🌟\n
            - Generate QR codes from text
            - Decode QR codes from images
            - Interactive and user-friendly interface\n
            Explore the functionalities and have fun with QR codes! 🚀\n
            """
        )

        if "qrcode.png" is not None:
            st.image("qrcode.png", use_column_width=True)
        else:
            st.write("Please upload a QR Code image to view.")

        st.markdown(
            """
            For any feedback or suggestions, feel free to reach out to me on [GitHub](https://github.com/Anujesh-Ansh). 😊\n
            Made with ❤️ by [Anujesh](https://github.com/Anujesh-Ansh)
            """
        )

    # Footer
    st.markdown(
        f'<div style="position: fixed; bottom: 0; left: 0; right: 0; text-align: center; padding: 10px;">Made with ❤️ by <a href="https://github.com/Anujesh-Ansh">Anujesh</a></div>',
        unsafe_allow_html=True
    )


if __name__ == '__main__':
    main()
