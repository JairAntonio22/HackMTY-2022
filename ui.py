import streamlit as st
from joblib import load
import numpy as np

model_diabetes=load("model_diabetes.joblib")

diabetes, cancer, derrame=st.tabs(['Diabetes','Cancer de Mama','Derrame cerebral'])

with diabetes:
    st.title("Herramienta de diagnostico para diabetes")

    genero=st.radio('Genero',('Hombre','Mujer'))
    if genero=='Mujer':
        embarazos=st.number_input('Numero de embarazos hasta la fecha',0)
    else:
        embarazos=0
    edad=st.number_input('Edad',0)
    glucosa=st.number_input('Nivel de glucosa',0)
    presion_arterial=st.number_input('presion arterial',0)
    grosor=st.number_input('grosor de la piel',0)
    insulina=st.number_input('Nivel de insulina',0)
    altura=st.number_input('Altura:',0)
    peso=st.number_input('Peso',0)

    if altura!=0:
        bmi=peso/(altura**2)
    else:
        bmi=0

    load=st.button("Calcular")

    if load:
        p=model_diabetes.predict(np.array([[embarazos,glucosa,presion_arterial,grosor,insulina,bmi,edad]]))
        if p[0]==0:
            r='Usted presenta riesgo de diabetes, por favor contacte a su medico'
        else:
            r='Nuestro modelo no encontro riesgo, sin embargo esta calculadora no es una prescripcion medica, si tiene dudas contacte a su medico'
        st.info(r)

with cancer:
    'test'

with derrame:
    'test'
