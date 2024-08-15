import streamlit as st
from PIL import Image
st.title(" Mi primera página")
st.header("Hola mundo")
st.write("Diferente tipo de letra")
image = Image.open("Imagen1.png")
st.image(image, caption="Interfaces multimodales")
