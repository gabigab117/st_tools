import streamlit as st
from PIL import Image
from io import BytesIO


st.set_page_config(page_icon="🖼", page_title="Compresseur d'images")
st.write("Compresseur d'images")

image_up = st.file_uploader(label="Image à compresser", accept_multiple_files=False, type=["png", "jpg"])
quality = st.number_input(step=1, label="Qualité de compression", min_value=10, max_value=95)

if image_up and quality:
    st.write(image_up.name)

    image = Image.open(image_up)
    im_io = BytesIO()
    image.save(im_io, format=image.format, optimize=True, quality=quality)
    st.image(image=image)
