import streamlit as st
from joblib import load
import numpy as np

model_diabetes=load("model_diabetes.joblib")

diabetes, cancer, derrame=st.tabs(['Diabetes','Cancer de pulmón','Derrame cerebral'])


with diabetes:
    st.title("Herramienta de diagnostico para diabetes")

    genero=st.radio('Genero:',('Hombre','Mujer'))
    if genero=='Mujer':
        embarazos=st.number_input('Numero de embarazos hasta la fecha',0)
    else:
        embarazos=0
    edad=st.number_input('Edad:',0)
    glucosa=st.number_input('Nivel de glucosa',0)
    presion_arterial=st.number_input('presion arterial',0)
    grosor=st.number_input('grosor de la piel',0)
    insulina=st.number_input('Nivel de insulina',0)
    altura=st.number_input('Altura(m):',0)
    peso=st.number_input('Peso(kg)',0)

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
    st.title("Herramienta de diagnostico para eventos cardiacos")

    genero=st.radio('Genero: ',('Hombre','Mujer'))
    edad=st.number_input('Edad: ',0)
    fuma=st.radio('Usted fuma:',('Si','No'))
    dedos=st.radio('Presenta dedos amarillos:',('Si','No'))
    ansiedad=st.radio('Sufre de ansiedad:',('Si','No'))
    conocidos=st.radio('Su circulo cercano contiene fumadores:',('Si','No'))
    enfermedad=st.radio('Sufre de alguna enfermedad cronica:',('Si','No'))
    fatiga=st.radio('Presenta fatiga:',('Si','No'))
    alergia=st.radio('Presenta alergias:',('Si','No'))
    sibilancia=st.radio('Presenta sibilancia:',('Si','No'))
    alcohol=st.radio('Consume alcohol:',('Si','No'))
    tos=st.radio('Presenta tos:',('Si','No'))
    respirar=st.radio('Presenta dificultad para respirar:',('Si','No'))
    dolor=st.radio('Presenta dolor de pecho:',('Si','No'))

    load=st.button("Calcular  ")

    if load:
        'test'

with derrame:
    st.title("Herramienta para diagnostico de riesgo de derrame cerebral")

    genero=st.radio('Genero',('Hombre ','Mujer '))
    edad=st.number_input('Edad:  ',1)
    hipertension=st.radio('Presenta hipertension:',('Si','No'))
    antecedentes=st.radio('Presenta antecedentes cardiacos:',('Si','No'))
    casado=st.radio('Esta o alguna vez ha estado casad@:',('Si','No'))
    trabajo=st.radio('Tipo de trabajo:',('Gobierno','Privado','Autoempleado','Am@ de casa','Nunca he trabajado'))
    residencia=st.radio('Lugar de residencia:',('Rural','Urbano'))

    altura=st.number_input('Altura(m): ',0)
    peso=st.number_input('Peso(kg): ',0)

    if altura!=0:
        bmi=peso/(altura**2)
    else:
        bmi=0

    load=st.button("Calcular ")

    if load:
        'test'
