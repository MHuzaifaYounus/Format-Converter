import pandas as pd 
import streamlit as st 
import os
from io import BytesIO
from PIL import Image
import pathlib 



st.set_page_config(page_title="Huza Image Format Converter" , layout="wide")
st.title("Huza Image Format Converter 📂")
st.write("Convert Your Image Formats i.e PNG , JPG , JPEG , Webp , PDF ")

uploaded_file = st.file_uploader("Upload Your File Here : ", type = [ "PNG" , "JPG" , "Webp" , "gif" , "bmp" , "tiff"] , accept_multiple_files=True)

def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

css_path = pathlib.Path("styles.css")
load_css(css_path)



format_mapping = {
    "jpg": ("JPEG", "image/jpeg"),
    "png": ("PNG", "image/png"),
    "webp": ("WEBP", "image/webp"),
    "gif": ("GIF", "image/gif"),
    "bmp": ("BMP", "image/bmp"),
    "tiff": ("TIFF", "image/tiff"),
    "pdf": ("PDF", "application/pdf")  
}



if uploaded_file:
    for file in uploaded_file:
        file_ext = os.path.splitext(file.name)[-1].lower().replace(".","")      
        image = Image.open(file)

        st.subheader(f"📂File Name : {file.name}")
        st.subheader(f"🎞 File Extension : {file_ext}")


        st.subheader("📀Conversion Options:")
        convert_ext = st.radio(f"Choose Format In which You Want to Convert {file.name}",[ "png" , "jpg" , "webp" , "gif" , "bmp" , "tiff","pdf"],key=file.name)

        if st.button("Convert" , key="green"):
            buffer = BytesIO()
            file_name = file.name.replace(f".{file_ext}" , f".{convert_ext}")
            mime_type = format_mapping[convert_ext][1]
            if convert_ext == "pdf":
                image.save(buffer, format="PDF")
            else:
                image.save(buffer, format=format_mapping[convert_ext][0], quality=95)
            buffer.seek(0)

            st.download_button(
                label = "Download File",
                data = buffer,
                file_name = file_name,
                mime = mime_type
            )
            st.success(f"✅ {file_name} converted successfully! 🎉")


       
