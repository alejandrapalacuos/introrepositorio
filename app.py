import streamlit as st
from PIL import Image
st.title(" Mi primera página")
st.header("Hola mundo")
st.write("Diferente tipo de letra")
image = Image.open("Imagen1.png")
st.image(image, caption="Interfaces multimodales")

texto = st.text_input("Escribe algo", "Este es mi texto")
st.write("El texto escrito es: ", texto)

st.subheader("2 columnas")

col1, col2 = st.columns (2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales")
  resp = st.checkbox("si")
  if resp:
    st.write("Epa")
with col2:
  st.subheader("esta es la segunda")
  modo = st.radio("Que modalidad", ("visual", "auditiva", "tactil"))
  if modo == "visual":
    st.write("que bien")
  if modo == "auditiva":
    st.write("wow")
  if modo == "tactil":
    st.write("que putas")

with st.sidebar:
  st.subheader("YYY")
  mod_radio = st.radio("Escoge", ("V","A","H"))
