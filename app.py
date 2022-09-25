import streamlit as st
from joblib import load
import numpy as np

model_diabetes=load("model_diabetes.joblib")
model_cancer=load("model_lung.joblib")
model_derrame=load("model_stroke.joblib")

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
    altura=st.number_input('Altura(cm):',0)
    peso=st.number_input('Peso(kg)',0)

    if altura!=0:
        altura=altura/100
        bmi=peso/(altura**2)
    else:
        bmi=0

    load=st.button("Calcular")

    if load:
        p=model_diabetes.predict(np.array([[embarazos,glucosa,presion_arterial,grosor,insulina,bmi,edad]]))
        if p[0]!=0:
            r='Usted presenta riesgo de diabetes, por favor contacte a su medico'
        else:
            r='Nuestro modelo no encontro riesgo, sin embargo esta calculadora no es una prescripcion medica, si tiene dudas contacte a su medico'
        st.info(r)

with cancer:
    dict_genero={
        'Hombre':1,
        'Mujer':0
    }

    dict_binario={
        'Si':2,
        'No':1
    }
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
    tragar=st.radio('Presenta dificultad para tragar:',('Si','No'))
    dolor=st.radio('Presenta dolor de pecho:',('Si','No'))

    load=st.button("Calcular  ")

    if load:
        genero=dict_genero[genero]
        fuma=dict_binario[fuma]
        dedos=dict_binario[dedos]
        ansiedad=dict_binario[ansiedad]
        conocidos=dict_binario[conocidos]
        enfermedad=dict_binario[enfermedad]
        fatiga=dict_binario[fatiga]
        alergia=dict_binario[alergia]
        sibilancia=dict_binario[sibilancia]
        alcohol=dict_binario[alcohol]
        tos=dict_binario[tos]
        respirar=dict_binario[respirar]
        tragar=dict_binario[tragar]
        dolor=dict_binario[dolor]
        #gender(Hombre=1,mujer=0),edad,fumar(yes=2,no=1),dedos(yes=2,no=1),ansiedad,presion social, enfermedad,fatiga,alergia,silbicio,alcohol,tos,perdida de aliento,tragar,dolor
        p=model_cancer.predict(np.array([[edad,fuma,dedos,ansiedad,conocidos,enfermedad,fatiga,alergia,sibilancia,alcohol,tos,respirar,tragar,dolor,genero]]))

        if p[0]!=0:
            r='Usted presenta riesgo de cancer de pulmon, por favor contacte a su medico'
        else:
            r='Nuestro modelo no encontro riesgo, sin embargo esta calculadora no es una prescripcion medica, si tiene dudas contacte a su medico'
        st.info(r)

with derrame:
    dict_genero={
        'Hombre':1,
        'Mujer':0
    }
    dict_binario={
        'No':0,
        'Si':1
    }
    dict_trabajo={
        'Privado':2,
        'Autoempleado':3,
        'Gobierno':0,
        'Niñ@':4,
        'Nunca he trabajado':1
    }

    dict_residencia={
        'Rural':0,
        'Urbano':1
    }

    dict_fuma={
        'Nunca':2,
        'Antes':1,
        'Si':3
    }
    st.title("Herramienta para diagnostico de riesgo de derrame cerebral")

    genero=st.radio('Genero',('Hombre','Mujer'))
    edad=st.number_input('Edad:  ',1)
    hipertension=st.radio('Presenta hipertension:',('Si','No'))
    antecedentes=st.radio('Presenta antecedentes cardiacos:',('Si','No'))
    casado=st.radio('Esta o alguna vez ha estado casad@:',('Si','No'))
    trabajo=st.radio('Tipo de trabajo:',('Gobierno','Privado','Autoempleado','Niñ@','Nunca he trabajado'))
    residencia=st.radio('Lugar de residencia:',('Rural','Urbano'))
    fumador=st.radio('Usted es fumador:',('Nunca','Antes','Si'))
    glucosa=st.number_input('Glucosa:',0)

    altura=st.number_input('Altura(cm): ',0)
    peso=st.number_input('Peso(kg): ',0)

    if altura!=0:
        altura=altura/100
        bmi=peso/(altura**2)
    else:
        bmi=0

    load=st.button("Calcular ")

    if load:
        genero=dict_genero[genero]
        hipertension=dict_binario[hipertension]
        antecedentes=dict_binario[antecedentes]
        casado=dict_binario[casado]
        trabajo=dict_trabajo[trabajo]
        residencia=dict_residencia[residencia]
        fumador=dict_fuma[fumador]
        #gender, age, hipertension, heart_disease, married, work_type, residencia(urbano=1, rural=0), glucosa, bmi, fumador(antes=1,nunca=2,fuma=3)
        p=model_derrame.predict(np.array([[genero,edad,hipertension,antecedentes,casado,trabajo,residencia,glucosa,bmi,fumador]]))

        if p[0]!=0:
            r='Usted presenta riesgo de derrame, por favor contacte a su medico'
        else:
            r='Nuestro modelo no encontro riesgo, sin embargo esta calculadora no es una prescripcion medica, si tiene dudas contacte a su medico'
        st.info(r)
