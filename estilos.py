import streamlit as st

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
