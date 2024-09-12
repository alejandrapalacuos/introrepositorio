import streamlit as st
from PIL import Image
st.title(" Por qué debemos tener un estilo de vida saludable ")
st.header("Beneficios")
st.write("En la siguiente imagen se mostrarán los beneficios de tener un estilo de vida saludable ")
image = Image.open("Imagen1.png")
st.image(image, caption="Buena alimentación")

texto = st.text_input("¿Por qué crees que es importante?", "Este es mi texto")
st.write("El texto escrito es: ", texto)

st.subheader("Test")

col1, col2 = st.columns (2)

with col1:
  st.subheader("Alimentación")
  st.write("Comer hamburguesa todo los días está bien")
  resp = st.checkbox("no")
  noresp = st.checkbox("si")
  if resp:
    st.write("¡Excelente!")
    
  if noresp:
    st.write("Recuerda que una dieta balanceada es lo mejor para tu salud")
with col2:
  st.subheader("Ejercicio")
  modo = st.radio("¿Qué es mejor?", ("Estar todo el día en el computador", "Hacer ejercicio 1 vez cada semestre", "Realizar un plan de entrenamiento y seguirlo"))
  if modo == "Estar todo el día en el computador":
    st.write("Eso es cultura sedentaria, no es lo mejor para tu salud")
  if modo == "Hacer ejercicio 1 vez cada semestre":
    st.write("Esta bien, pero no creo que sea lo mejor para tu salud")
  if modo == "Realizar un plan de entrenamiento y seguirlo":
    st.write("¡Felicitaciones!")

with st.sidebar:
  st.subheader("YYY")
  mod_radio = st.radio("Escoge", ("V","A","H"))
