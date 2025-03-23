import streamlit as st
import requests
import json

st.title("Generador de Cadenas - Con API")

# Dirección de la API
API_URL = "http://localhost:8000"

# Inicializar el estado si no existe
if "RigtStrings" not in st.session_state:
    st.session_state.RigtStrings = []
if "WrongsStrings" not in st.session_state:
    st.session_state.WrongsStrings = []

st.write("Haz clic en un botón para solicitar cadenas a la API:")

# Botón para pedir cadenas correctas
if st.button("Generar Cadenas"):
    # Hacemos las peticiones a la API
    RigtStringsRes = requests.get(f"{API_URL}/generate-correct")
    WrongsStringsRes = requests.get(f"{API_URL}/generate-wrong")

    # Validar respuestas
    if RigtStringsRes.status_code == 200:
        st.session_state.RigtStrings = RigtStringsRes.json().get("strings", [])
        st.success("✅ Cadenas Correctas Generadas:")
        st.write(st.session_state.RigtStrings)
    else:
        st.error("⚠️ Error al conectar con la API (cadenas correctas).")

    if WrongsStringsRes.status_code == 200:
        st.session_state.WrongsStrings = WrongsStringsRes.json().get("strings", [])
        st.success("✅ Cadenas Incorrectas Generadas:")
        st.write(st.session_state.WrongsStrings)
    else:
        st.error("⚠️ Error al conectar con la API (cadenas incorrectas).")

# Botón para validar cadenas (envía un POST)
if st.button("Validar Cadenas"):
    if st.session_state.RigtStrings and st.session_state.WrongsStrings:
        payload = {
            "correct": [str(item) for item in st.session_state.RigtStrings],
            "wrong": [str(item) for item in st.session_state.WrongsStrings],
        }
        
        # 🔎 Mostrar lo que se enviará
        st.write("📤 Enviando datos a la API:")
        st.json(payload)

        # Enviar los datos a la API
        # En Streamlit
        validation = requests.post(f"{API_URL}/validation1", json=payload)

        # Depurar la respuesta
        st.write("📥 Respuesta de la API:")
        st.write(validation.status_code, validation.text)

        if validation.status_code == 200:
            st.success("✅ Validación de Cadenas:")
            st.write(validation.json().get("message", "Validación exitosa."))
        else:
            st.error(f"⚠️ Error al conectar con la API: {validation.status_code}")
    else:
        st.error("⚠️ Primero debes generar las cadenas.")
    
if st.button("Siguiente"):
    if "hola":
        print("hola")