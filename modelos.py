import joblib
import numpy as np
from datetime import datetime
import random

# Cargar modelos
modelo_lluvia = joblib.load('modelos/modelo_lluvia_cluster.pkl')
modelo_temperatura = joblib.load('modelos/modelo_temperatura.pkl')
modelo_calidad_aire = joblib.load('modelos/modelo_pm10.pkl')

# Función para convertir hora a número (hora)
def hora_a_numero(hora):
    return datetime.strptime(hora, "%H:%M").hour  # Extrae solo la hora en formato de 24 horas

# Funciones para generar valores aleatorios dentro de los rangos definidos
def generar_valores_aleatorios():
    # Promedios de las variables
    temperatura_ciudad = 25.076938
    pm10_ciudad = 35.120406
    no2_ciudad = 16.774860
    o3_ciudad = 26.775354
    lluvia_ciudad = 0.038155

    # Rangos razonables para cada variable
    rango_temperatura = (temperatura_ciudad - 2, temperatura_ciudad + 2)  # Rango entre 23°C y 27°C
    rango_pm10 = (pm10_ciudad - 10, pm10_ciudad + 10)  # Rango entre 25 y 45
    rango_no2 = (no2_ciudad - 5, no2_ciudad + 5)  # Rango entre 11 y 21
    rango_o3 = (o3_ciudad - 5, o3_ciudad + 5)  # Rango entre 21 y 31
    rango_lluvia = (lluvia_ciudad - 0.02, lluvia_ciudad + 0.02)  # Rango entre 0.018 y 0.058

    # Generar valores aleatorios dentro de los rangos definidos
    TEMPERATURA_CIUDAD = random.uniform(*rango_temperatura)
    PM10_CIUDAD = random.uniform(*rango_pm10)
    NO2_CIUDAD = random.uniform(*rango_no2)
    O3_CIUDAD = random.uniform(*rango_o3)
    LLUVIA_CIUDAD = random.uniform(*rango_lluvia)

    return TEMPERATURA_CIUDAD, PM10_CIUDAD, NO2_CIUDAD, O3_CIUDAD, LLUVIA_CIUDAD

# Funciones para predecir
def predecir_lluvia(hora):
    hora_num = hora_a_numero(hora)  # Convertir hora a número
    TEMPERATURA_CIUDAD, PM10_CIUDAD, NO2_CIUDAD, O3_CIUDAD, LLUVIA_CIUDAD = generar_valores_aleatorios()  # Nuevos valores aleatorios
    datos = np.array([[hora_num, TEMPERATURA_CIUDAD, NO2_CIUDAD, O3_CIUDAD, PM10_CIUDAD]])
    prediccion = modelo_lluvia.predict(datos)
    return prediccion

def predecir_temperatura(hora):
    hora_num = hora_a_numero(hora)  # Convertir hora a número
    TEMPERATURA_CIUDAD, PM10_CIUDAD, NO2_CIUDAD, O3_CIUDAD, LLUVIA_CIUDAD = generar_valores_aleatorios()  # Nuevos valores aleatorios
    datos = np.array([[hora_num, LLUVIA_CIUDAD, NO2_CIUDAD, O3_CIUDAD]])
    prediccion = modelo_temperatura.predict(datos)
    return prediccion

def predecir_calidad_aire(hora):
    hora_num = hora_a_numero(hora)  # Convertir hora a número
    TEMPERATURA_CIUDAD, PM10_CIUDAD, NO2_CIUDAD, O3_CIUDAD, LLUVIA_CIUDAD = generar_valores_aleatorios()  # Nuevos valores aleatorios
    datos = np.array([[hora_num, TEMPERATURA_CIUDAD, NO2_CIUDAD, O3_CIUDAD]])
    prediccion = modelo_calidad_aire.predict(datos)
    return prediccion
