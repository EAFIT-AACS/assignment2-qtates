import random
import requests
import streamlit as st
import pandas as pd

st.title("🔢 Strings Generator and Validator")

# API Address.
API_URL = "http://localhost:8000"

# Initialize the status if it does not exist.
if "RightStrings" not in st.session_state:
    st.session_state.RightStrings = []
if "WrongsStrings" not in st.session_state:
    st.session_state.WrongsStrings = []
if "combinedList" not in st.session_state:
    st.session_state.combinedList = []
if "iterator" not in st.session_state:
    st.session_state.iterator = 0
if "buttonNext" not in st.session_state:
    st.session_state.buttonNext = 0
if "validation" not in st.session_state:
    st.session_state.validation = None

# Function to generate strings
def generateStrings():
    #Request strings
    RightStringsRes = requests.get(f"{API_URL}/generate-correct")
    WrongsStringsRes = requests.get(f"{API_URL}/generate-wrong")

    # Validate responses to the request and update the value of variables
    if RightStringsRes.status_code == 200:
        st.session_state.RightStrings = RightStringsRes.json().get("strings", [])
    else:
        st.error("⚠️ Error to contect to the API (Right Strings).")

    if WrongsStringsRes.status_code == 200:
        st.session_state.WrongsStrings = WrongsStringsRes.json().get("strings", [])
    else:
        st.error("⚠️ Error to contect to the API (Wrong Strings).")

    # Merging and shuffling lists in random order.
    combinedList = st.session_state.RightStrings + st.session_state.WrongsStrings
    random.shuffle(combinedList)
    st.session_state.combinedList = combinedList
    st.session_state.iterator = 0
    st.session_state.buttonNext = 0
    st.rerun()

# Function to send strings and validate them.
def sendValidateString():
    if st.session_state.combinedList:
        # Defines the string to send.
        payload = {
            "string": st.session_state.combinedList[st.session_state.iterator]
        }
        
        # 🔎 Show what will be sent.
        st.write("📤 Sending data to the API...")
        st.json(payload) #Transform data to json

        # Send the data to the API and get an answer.
        st.session_state.validation = requests.post(f"{API_URL}/validation1", json=payload)
    else:
        st.error("⚠️ First you must generate the strings.")
    st.rerun()


modo = st.radio("Select a mode:", ["Generate Strings", "Enter String"])

st.info("List of current strings:")

# Print strings specifying whether they are valid or invalid and whether they are currently being processed.
if st.session_state.combinedList:
    if len(st.session_state.combinedList) != 1:
        for i in range (len(st.session_state.combinedList)):
            if i == st.session_state.iterator:
                if st.session_state.combinedList[i] in st.session_state.RightStrings:
                    st.write(i,": ",st.session_state.combinedList[i], "(Valid)","✅")
                else:
                    st.write(i,": ",st.session_state.combinedList[i], "(Invalid)","✅")
            else:
                if st.session_state.combinedList[i] in st.session_state.RightStrings:
                    st.write(i,": ",st.session_state.combinedList[i], "(Valid)")
                else:
                    st.write(i,": ",st.session_state.combinedList[i], "(Invalid)")
    else:
        st.write(0,": ",st.session_state.combinedList[0],"✅")
else:
    st.write("No strings generated.")

st.info("Results of the validation:")
if st.session_state.validation:
    data = st.session_state.validation.json()  # Get the data from the response
    # Create a dataframe with the data
    df = pd.DataFrame({
        "Tree": data["tree"],
        "Stack": data["stack"],
        "Rules": data["rules"]
    })

    # Show the table
    st.table(df)
    if data["result"] == "The string belong to the language":
        st.success(data["result"])
    else:
        st.error(data["result"])
else:
    st.write("No datas to show.")

col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

# Button for processing passed string.
with col2:
    if st.button("Back"):
        if st.session_state.iterator > 0:
            st.session_state.iterator -= 1
            sendValidateString()
            st.rerun()
        else:
            st.write("You are now on the first string.")

with col3:
    if st.button("Next"):
        if st.session_state.iterator < len(st.session_state.combinedList) - 1:
            st.session_state.iterator += 1
            sendValidateString()
            st.rerun()
        else:
            st.write("You are now on the last string.")

if modo == "Generate Strings":
    st.header("🔢 Generate Strings randomly")
    # Button to generate strings (send a GET)
    if st.button("Generate Strings"):
        # Do the request to the API
        generateStrings()

    # Button to validate the string (send a POST)
    if st.button("Validate Strings"):
        st.session_state.iterator = 0
        sendValidateString()

elif modo == "Enter String":
    st.header("✍️ Introduce your own string...")
    st.session_state.iterator = 0
    # Textbox to enter a string to validate
    cadena_manual = st.text_input("Introduce a string to validate.")
    combinedList = [cadena_manual]
    st.session_state.combinedList = combinedList
    st.write("String to process : ", st.session_state.combinedList)
    # Button to validate the string (send a POST)
    if st.button("Validate String."):
        sendValidateString()