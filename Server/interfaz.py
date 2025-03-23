import random

import requests
import streamlit as st

st.title("Generador de Cadenas - Con API")

# Dirección de la API
API_URL = "http://localhost:8000"

# Inicializar el estado si no existe
if "RigtStrings" not in st.session_state:
    st.session_state.RigtStrings = []
if "WrongsStrings" not in st.session_state:
    st.session_state.WrongsStrings = []
if "combinedList" not in st.session_state:
    st.session_state.combinedList = []
if "iterator" not in st.session_state:
    st.session_state.iterator = 0
if "buttonNext" not in st.session_state:
    st.session_state.buttonNext = 0

def sendValidateString():
    if st.session_state.combinedList:
        payload = {
            "string": st.session_state.combinedList[st.session_state.iterator]
        }
        
        # 🔎 Mostrar lo que se enviará
        st.write("📤 Enviando datos a la API:")
        st.json(payload)

        # Enviar los datos a la API
        validation = requests.post(f"{API_URL}/validation1", json=payload)

        if validation.status_code == 200:
            st.success("✅ Validación de Cadenas:")
            st.write(validation.json().get("message"))
        else:
            st.error(f"⚠️ Error al conectar con la API: {validation.status_code}")
    else:
        st.error("⚠️ Primero debes generar las cadenas.")

st.write("Haz clic en un botón para solicitar cadenas a la API:")

    # Switch para alternar entre "Generar" e "Ingresar"
modo = st.radio("Selecciona el modo:", ["Generar", "Ingresar"])

if modo == "Generar":
    st.header("🔢 Generar Cadenas")
    
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

        # Fusionar y mezclar las listas
        combinedList = st.session_state.RigtStrings + st.session_state.WrongsStrings
        random.shuffle(combinedList)  # Mezclar en orden aleatorio
        st.session_state.combinedList = combinedList
        st.write("Lista combinada y mezclada:")
        st.write(st.session_state.combinedList)
    # Botón para validar cadenas (envía un POST)
    if st.button("Validar Cadenas"):
        sendValidateString()
        st.session_state.buttonNext=1
    if st.session_state.buttonNext==1:
        if st.session_state.iterator !=len(st.session_state.combinedList)-1:
            if st.button("Siguiente"):
                st.session_state.iterator += 1
                if st.session_state.iterator < len(st.session_state.combinedList):
                    sendValidateString()
        else:
            st.write("Ya validaste todas las cadenas")
            st.session_state.iterator -= 1

    if st.session_state.iterator != 0:
        if st.button("Atras"):
            if st.session_state.iterator > 0:
                st.session_state.iterator -= 1
                sendValidateString()
            else:
                st.write("Ya validaste todas las cadenas")

elif modo == "Ingresar":
    st.header("✍️ Ingresar Cadenas Manualmente")
    # Campo de texto para ingresar la cadena
    cadena_manual = st.text_input("Introduce una cadena para validar:")
    combinedList = [cadena_manual]
    st.session_state.combinedList = combinedList
    st.write("Lista de cadenas:")
    st.write(st.session_state.combinedList)
    # Botón para validar cadenas (envía un POST)
    if st.button("Validar Cadenas"):
        sendValidateString()
        st.session_state.buttonNext=1