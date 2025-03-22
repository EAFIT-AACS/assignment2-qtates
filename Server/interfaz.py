# streamlit_app.py
import streamlit as st
import requests

st.title("Generador de Cadenas - Con API")

# Dirección de la API
API_URL = "http://localhost:8000"

st.write("Haz clic en un botón para solicitar cadenas a la API:")

# Botón para pedir cadenas correctas
if st.button("Generar Cadenas Correctas"):
    respuesta = requests.get(f"{API_URL}/generate-correct")
    if respuesta.status_code == 200:
        st.success("✅ Cadenas Correctas Generadas:")
        st.write(respuesta.json()["strings"])
    else:
        st.error("⚠️ Error al conectar con la API.")

# Botón para pedir cadenas incorrectas
if st.button("Generar Cadenas Incorrectas"):
    respuesta = requests.get(f"{API_URL}/generate-wrong")
    if respuesta.status_code == 200:
        st.error("❌ Cadenas Incorrectas Generadas:")
        st.write(respuesta.json()["strings"])
    else:
        st.error("⚠️ Error al conectar con la API.")
