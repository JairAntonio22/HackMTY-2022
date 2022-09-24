import streamlit as st

st.title("Herramienta de diagnostico para diabetes")

genero=st.radio('Genero',('Hombre','Mujer'))
if genero=='Mujer':
    embarazos=st.number_input('Numero de embarazos hasta la fecha',0)
glucosa=st.number_input('Nivel de glucosa',0)
presion_arterial=st.number_input('presion arterial',0)
grosor=st.number_input('grosor de la piel',0)
insulina=st.number_input('Nivel de insulina',0)
altura=st.number_input('Altura:',0)
peso=st.number_input('Peso',0)

bmi=peso/(altura**2)
