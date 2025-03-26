import streamlit as st
from datetime import datetime
from modelos import predecir_lluvia, predecir_temperatura, predecir_calidad_aire

# Diseño de la página
st.set_page_config(page_title="Calidad del Aire - Air3", layout="wide", page_icon="🌤️")


# Funciones para mostrar las predicciones
def mostrar_prediccion_lluvia(hora_input):
    lluvia_pred = predecir_lluvia(hora_input)
    if lluvia_pred[0] == 0:
        st.image('img/no_lluvia.png', caption="No Lluvia", width=100)
    elif lluvia_pred[0] == 1:
        st.image('img/lluvia_ligera.png', caption="Lluvia Ligera", width=100)
    elif lluvia_pred[0] == 2:
        st.image('img/lluvia_moderada.png', caption="Lluvia Moderada", width=100)
    else:
        st.image('img/lluvia_fuerte.png', caption="Lluvia Fuerte", width=100)

def mostrar_prediccion_temperatura(hora_input):
    temperatura_pred = predecir_temperatura(hora_input)
    ans = round(temperatura_pred[0], 1)
    st.markdown(f"**Temperatura Predicha para las {hora_input}: {ans}°C**")

def mostrar_prediccion_calidad_aire(hora_input):
    calidad_aire_pred = predecir_calidad_aire(hora_input)
    if calidad_aire_pred[0] < 50:
        st.image('img/buena.png', caption="Aire Bueno", width=100)
    elif calidad_aire_pred[0] < 100:
        st.image('img/regular.png', caption="Aire Regular", width=100)
    elif calidad_aire_pred[0] < 150:
        st.image('img/mala.png', caption="Aire Malo", width=100)
    else:
        st.image('img/muy_mala.png', caption="Aire Muy Malo", width=100)
