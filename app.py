import streamlit as st
from visualizacion import mostrar_prediccion_lluvia, mostrar_prediccion_temperatura, mostrar_prediccion_calidad_aire
from config import horas

from datetime import datetime

# Estilos personalizados
st.markdown(
    """
    <style>
    .main {
        background-color: #2495ff;  # Azul claro de fondo
    }
    .titulo-principal {
        font-size: 3em;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        margin-top: 0.5em;
    }
    .subtitulo {
        font-size: 1.3em;
        color: #34495e;
        text-align: center;
        margin-bottom: 2em;
    }
    
    .texto {
        color: #000000;
    }
    .card {
        background-color: #f5f5f5;  # Color más oscuro para las tarjetas
        border-radius: 15px;
        padding: 1.5em;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        margin: 1em;
        text-align: center;
    }
    .card h3 {
        color: #FF7F0E;
    }
    .card p {
        font-size: 1.2em;
    }
    .stButton>button {
        background-color: #FF7F0E;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Agregar el logo con el nombre "AIR3" en la parte superior
st.image('img/logo.png', width=100)  # Asegúrate de que la imagen del logo esté en la ruta correcta
st.markdown('<div class="titulo-principal">AIR3</div>', unsafe_allow_html=True)


# Menú lateral
menu = st.sidebar.selectbox(
    "Menú",
    ["Inicio", "Predicción de Lluvia", "Predicción de Temperatura", "Predicción de Calidad del Aire", "Acerca de"]
)

# Pantalla de inicio
if menu == "Inicio":
    st.markdown('<div class="titulo-principal">🌿 Calidad del Aire en Bucaramanga</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitulo">Consulta en tiempo real el estado del aire y el clima en el Área Metropolitana de Bucaramanga</div>', unsafe_allow_html=True)

    # Renderizar las tarjetas
    col1, col2, col3 = st.columns(3)

    with col1:
        # Asegúrate de que los datos se mantengan en session_state
        if "calidad_aire" not in st.session_state:
            st.session_state.calidad_aire = "Aire Regular"  # Valor predeterminado
        st.markdown(f'<div class="card"><h3>💨 Calidad del Aire</h3><span class="texto">{st.session_state.calidad_aire}</span></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card"><h3>🌧️ ¿Clima Actual?</h3><span class="texto">Mayormente Nublado</span></div>', unsafe_allow_html=True)

    with col3:
        if "temperatura" not in st.session_state:
            st.session_state.temperatura = 25  # Temperatura predeterminada
        st.markdown(f'<div class="card"><h3>🌡️ Temperatura Actual</h3><span class="texto">{st.session_state.temperatura}°C</span></div>', unsafe_allow_html=True)
        
        
# Predicción de lluvia
elif menu == "Predicción de Lluvia":
    st.header("🌧️ Predicción de Lluvia")
    hora_input = st.selectbox("Selecciona una hora para la predicción", horas)
    mostrar_prediccion_lluvia(hora_input)

# Predicción de temperatura
elif menu == "Predicción de Temperatura":
    st.header("🌡️ Predicción de Temperatura")
    hora_input = st.selectbox("Selecciona una hora para la predicción", horas)
    mostrar_prediccion_temperatura(hora_input)

# Predicción de calidad del aire
elif menu == "Predicción de Calidad del Aire":
    st.header("💨 Predicción de Calidad del Aire")
    hora_input = st.selectbox("Selecciona una hora para la predicción", horas)
    mostrar_prediccion_calidad_aire(hora_input)

# Acerca de
elif menu == "Acerca de":
    st.header("📘 Acerca de Air3")
    st.markdown("""  
        **Air3** es una empresa dedicada a la monitorización de la calidad del aire y las condiciones meteorológicas.
        Nuestro objetivo es proporcionar información precisa y en tiempo real sobre el ambiente, ayudando a las personas a tomar decisiones informadas para su salud y bienestar.
    """)
    st.caption("Versión demo | {}".format(datetime.now().strftime("%d/%m/%Y")))



