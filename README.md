 
# Creation of Language with Context Free Grammar 📖

In this assignment, you will see the step-by-step process of creating a context-free language, from its definition to building its grammar, generating strings, and designing an automaton to verify whether they belong to the language.

## Contents 🤔
- [Team](#team)
- [Development environment](#development-environment)
- [Instructions for running](#instructions-for-running)
- [User's Manual](#users-manual)
- [Explanation of the context free grammar](#explanation-of-the-context-free-grammar)
- [Explanation of the algorithm](#explanation-of-the-algorithm)
    - [First algorithm: Creating the accepted and rejected Strings](#first-algorithm-creating-the-accepted-and-rejected-Strings)
    - [Second Algorithm: The automaton](#second-algorithm-the-automaton)
    - [Third Algorithm: Automaton configuration tree algorithm](#third-algorithm-automaton-configuration-tree-algorithm)
    - [Extra Code: The API and the Graphic interface](#extra-code-the-api-and-the-graphic-interface)

## Team 💡🧠
- Ginna Alejandra Valencia Macuace
- Laura Andrea Castrillón Fajardo
- Samuel Martínez Arteaga

## Development environment 💻🐍
- **Operative System:** Windows 11
- **Programming language:** Python 3.12
- **Tools:** Visual Studio Code
- **FrameWork:** Streamlit and FastAPI

## Instructions for running ▶️🏃‍♂️
- 1. Install FastAPI. To do this, type the following command in the terminal:
```
pip install fastapi uvicorn
```
- 2. Install Streamlit. To do this, type the following command in the terminal:
```
pip install streamlit
```
- 3. Install pandas. To do this, type the following command in the terminal:
```
pip install pandas
```
- 4. It is necessary to turn on the API locally. To do this open a terminal pointing to the folder created after cloning the repository. To do this, type the following command in the terminal:
```
uvicorn Server.app:app --reload
```
- 5. Now we run streamlit also from the same address. To do this, type the following command in the terminal:
```
streamlit run Server/interfaceCFG.py
```

## User's Manual 📖👨

After completing the previous steps, the following page should open in your browser.

![6a7919a9-582d-4fcb-b771-6e515a94531a](https://github.com/user-attachments/assets/8e9ce167-5b31-43e8-ae83-e63a2aeb2f86)

- 1. You will find two options for using the API: generating strings using the first algorithm or letting your imagination run wild and entering them manually. To proceed, choose an option.

(If your choice is to generate strings, follow steps 2 to 5. If you choose to enter them manually, follow steps 5 to 6.)

- 2. First, generate the strings by clicking the "Generate Strings" button. After that, the list of generated strings (ranging from 4 to 6) will appear in the first blue box.

- 3. With the strings already generated, we are ready to validate them using the "Validate String" button. This button should be used only once; otherwise, the process will restart (it will not generate an error).

- 4. From this point, you can click "Next" or "Back" to view the validation process for all strings. You can use the emoji: ✅ indicator to see which string is currently being processed.

- 5. By selecting "Enter String," you will see the following interface.

![b164153d-4cd9-4391-88d7-e4e42fa99e6d](https://github.com/user-attachments/assets/4684525f-4ee8-49b5-a3eb-38babbe14169)


In the text input, you can enter the string you want to verify. Enter it without spaces: " ".

- 6. To validate it, click the "Validate String" button. Below, you will see the vector being validated along with its corresponding response and configuration tree for the string.


## Explanation of the context free grammar 📝 🆓

The proposed language consists of: A language that accepts strings with an even number of 'a's (minimum 2) and an odd number of 'b's. These strings result from the concatenation of an odd number of substrings, each formed by an even number of 'a's (minimum 2) followed by an odd number of 'b's.

<img src="https://latex.codecogs.com/svg.latex?\color{white}L(M)%20=%20\left\{%20\left(a^{2n}%20b^{2m+1}%20\right)^*%20\mid%20n%20\geq%201,%20m%20\geq%200%20\right\}%20-%20\{\epsilon\}" />

The context-free grammar (CFG) that defines the language is:

$$G=(N,\Sigma,P,S)$$
$$N={S,A,B,X}$$
$$\Sigma={a,b}\\newline$$
$$P= S \to  ABX\\newline$$
$$A \to  aaA | aa\\newline$$
$$B \to bbB | b$$

And the stack automaton proposed is:

$$N=(Q,\Sigma,\Gamma,\delta, S,F)$$
$$Q={q}$$
$$\Sigma={a,b}$$
$$\Gamma ={a,b}$$
$$S={q}$$
$$F=\phi$$
$$\delta=i.\  ((q,a,b)(q,ab))$$
$$ii.\  ((q,a,a)(q,\epsilon ))$$
$$iii. \ ((q,b,\epsilon )(q,b))$$
$$iv. \ ((q,b,b)(q,\epsilon ))$$
$$v. \ ((q,a,\epsilon )(q,abx))$$
$$vi. \ ((q,a,x)(q,ab))$$
$$vii. \ ((q,b,x)(q,bx))$$

## Explanation of the algorithm 🤖💭

### First algorithm: Creating the accepted and rejected Strings


In this algorithm we create some sets of accepted and rejected Strings. These sets are forced to be accepted or rejected with some parameters, however, these strings have some random factors in it, so almost every run is a unique set of Strings

```
def createCorrectStrings():
    strings = []
    for i in range (r.randint(2,3)):
        cadena = ""
        # Generate a random number of sets of strings to concatenate in a complete string
        stringAmounts = r.randint(1,4)
        # If the number of strings is even, add one to make it odd
        if stringAmounts%2 == 0:
            stringAmounts += 1
        for k in range (stringAmounts):
            # Generate a random number of "a" to concatenate
            aAmounts = r.randint(1,5)
            # If the number of "a" is odd, add one to make it even
            if aAmounts%2 != 0:
                aAmounts += 1
            # Generate a random number of "b" to concatenate
            bAmounts = r.randint(1,4)
            # If the number of "b" is even, add one to make it odd
            if bAmounts%2 == 0:
                bAmounts += 1
            for j in range (aAmounts):
                cadena += "a"
            for j in range (bAmounts):
                cadena += "b"
        # Append the string to the list of strings
        strings.append(cadena)
    return strings
```

As we can see, the most important things in this method is: a odd number of sets of strings to create a single string (This is to secure that they will have an even number of "a" and odd number of "b"), a even number of "a" pher set and a odd number of "b" pher set

```
def createWrongStrings():
    strings = []
    for i in range (r.randint(2,3)):
        cadena = ""
        # Generate a random number of sets of strings to concatenate in a complete string
        stringAmounts = r.randint(1,4)
        # If the number of strings is odd, add one to make it even (to secure that the string is going to be rejected by the automaton)
        if stringAmounts%2 != 0:
            stringAmounts += 1
        # Generate a random number of "a" and "b" to concatenate without any restriction
        for k in range (stringAmounts):
            aAmounts = r.randint(1,6)
            bAmounts = r.randint(1,7)
            for j in range (aAmounts):
                cadena += "a"
            for j in range (bAmounts):
                cadena += "b"
        # Append the string to the list of strings
        strings.append(cadena)
    return strings
```

This is a very similar method to the last one, but in this case we force the automaton to reject the string by establishing an even number of string sets to create a single string, so we don´t care the number of "a" and "b" pher set. It will always be rejected by the automaton

### Second Algorithm: The automaton

This is one of the most important algorithms in this project, the automaton.

```
    # Definition of automaton: Stack with its initial symbol, started state q, transitions.
    stack = ["b"] #In every iteration get the initial symbol in the stack.
    q=word
    #Definition of transitions/rules using a dictionary.
    functiontransition = {("a","b"):["ab",1],("a","a"):["",2],("b",""):["b",3],("b","b"):["",4],("a",""):["abx",5],("a","x"):["ab",6],("b","x"):["bx",7]}

    #Definition of the variable for having the sequence/steps of the stack and rule transition, necessary for the third algorithm.
    stackSequence=["b"]
    ruleTransitionsSequence=[]
    state=0
```

We define the automaton's parameters, like the initial state, the initial simbol of the stack, all the transition rules (as a dictionary in python to facilitate the application of the automaton in code) and some variables to do the tracing of the stack, the transitions and the states that the automaton reaches through the validation of a string

```
 for j in range(len(word)):
        letter=word[j] #Processed letter for letter.
```

We star iterating the string letter for letter

```
        if(len(stack) == 0):
            highStack=""
            stack.append(" ") #If the stack is empty, so add a (" ") to represent it and avoid issues.
        else:
            highStack= stack[0] #Otherwise take the first character in the stack.
```

Python doesn't recognize the null string, so if the stack is empty we append a blank space " "; this to avoid issues, like index out of range and so on. Otherwise, we take the first character of the stack

```
        #Search the corresponding transition/rule for the letter and hihgStack, and add the number's rule.
        if (letter,highStack) in functiontransition:
            transition=functiontransition[letter,highStack][0]
            ruleTransitionsSequence.append(functiontransition[letter,highStack][1])
        else:
            #Not finding a transition with these values, so not exist and the string doesn't belong to the language.
            break
        print(letter,",",highStack,":",transition)
```

After getting the first character, we look for the transition rule in the dictionary of rules, if it doesn't exists, the String is rejected instantly, breaking the loop and keeping characters in the stack. If it exists, we take the result of the transition rule. Moreover, we append the number of the rule aplied (this to use it at the third algorithm)

```
        stack.pop(0)
        for k in range(len(transition)):
            stack.insert(k,transition[k])
        print(stack)
        stackSequence.append(stack[:])
```

In this fragment of code we unstack the first element of the stack, and append the result of the transition rule that we got from the last fragment of code. Furthermore, we append the stack to keep the track of the states of the stack (this to facilitate the third algorithm)

```
    #If stack is empty, then the string was accepted.
    if len(stack)==0:
        print("The string belong to the language")
        state=0
    else:
        print("The string doesn't belong to the language")
        state=1

    return stackSequence, ruleTransitionsSequence, state, word
```
Finally, we confirm if the stack is empty (it means that the automaton accepted the String) or if it is not (it means that the automaton rejected the String). So, if the state = 0, the automaton accepted the String, if the state = 1, the automaton rejected the String. All this algorithm retunrs the stackSequence, the ruleTransitionsSequence, the state and the string that proccesed. These data is received by the third algorithm.

### Third Algorithm: Automaton configuration tree algorithm

This third algorithm is responsible for separate and organize the output of the second algorithm. And this is the final algorithm, this delivery the final output of the chain of algorithms

```
def printTree(results):
    word = results[3]
    tree = []
    stack = []
    rules = []
    for i in range(len(results[0])):
        if i == 0:
            rules.append("Original")
            stack.append(results[0][i])
            tree.append(word)
        else:
            rules.append(results[1][i-1])
            stack.append(results[0][i])
            tree.append(word)
        word = word[1:]
    if results[2] == 0:
        result = "The string belong to the language"
    else:
        result = "The string doesn't belong to the language"
    return tree, stack, rules, result
```

This algorithm is very simple, as mentioned, it receives the output of the second algorithm, create the final variables (tree, stack and rules), and start appending each element to it's corresponding list. Finally, returns the final product.

### Extra Code: The API and the Graphic interface

We wanted to go further, so we implement these three algorithms with an API and a graphic interface. It was a difficult road, but through a lot of research we were able to move forward with the implementation.

#### The API

Firts of all we are going to talk about the API. As we mentioned before, we used FastAPI.

```
from fastapi import FastAPI, HTTPException
from Scripts.ALGORITHM_1_LFCO_2025_GV_LC_SM import createCorrectStrings, createWrongStrings
from Scripts.ALGORITHM_2_LFCO_2025_GV_LC_SM import validationString
from Scripts.ALGORITHM_3_LFCO_2025_GV_LC_SM import printTree
from pydantic import BaseModel

# Create a FastAPI instance.
app = FastAPI()
```

We import the algorithms and create a FastAPI instance.

```
# Create a class to define the data model expected to be received in the API.
class StringInput(BaseModel):
    string: str
```

Create the structure of the json that the API will receive before long

```
# Define the API path that will call the createCorrectStrings() method and return the correct strings.
@app.get("/generate-correct")
async def generate_correct():
    try:
        return {"strings": createCorrectStrings()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en generate_correct: {str(e)}")

# Define the API path that will call the createWrongStrings() method and return the incorrect strings.
@app.get("/generate-wrong")
async def generate_wrong():
    try:
        return {"strings": createWrongStrings()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en generate_wrong: {str(e)}")
```

We create two get methods, with its paths each one, to generate the accepted and rejected Strings (for this, the API uses the first algorithm); and returns them to the graphic interface. Moreover we aplied a little try catch to handle errors.

```
# Define the API path that will validate the received string. And it will return if it is correct, incorrect and its derivation tree.
@app.post("/validation1")
def validate(data: StringInput):
    resultValidation=validationString(data.string)
    tree=printTree(resultValidation)
    return {
        "tree": tree[0],
        "stack" : tree[1],
        "rules": tree[2],
        "result": tree[3],
    }
```

Finally, we create a post method, that receives a json with a String. Then calls the validationString method from the second algorithm and passes the string mentioned previously. Then passes the result to the printTree method from the third algorithm, and finally returns the final result to the graphic interface.

#### The graphic interface

The graphic interface was made with Streamlit, a python library that help us with the frontend. It is a "server" by itself, so all the visualitation will be on a web navigator.

```

import random
import requests
import streamlit as st
import pandas as pd

st.title("🔢 Strings Generator and Validator")

# API Address.
API_URL = "http://localhost:8000"
```

We import the necesaries libraries and define the API address to comunicate with it.

```
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

```

As streamlit clears the variables, we declare them as state variables to make them persistent during execution.

```
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
```

We define a method to generate the Strings making a request to the API, store them in a list, and mix them. Note that we are storing them in the state variables mentioned before.

```
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
```

We define a method to send to the API a json with the String to validate and store the result on a variable. Note that the string depends on an iterator, it will be mentioned forward.

```
modo = st.radio("Select a mode:", ["Generate Strings", "Enter String"])
```

Our application has two modes, generating strings with the first algorithm, or introducing the string yourself. With this input we change to one or another mode.


```

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
```

Wheter generate the strings or introduce the string yourself, in both cases the list of strings will be showed here. The mark will be appearing beside the string that is been validating at that moment. Moreover, if we generate the strings, the program will show if the string is valid or invalid.

```
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

```

At this space we will be watching the result of the derivation as a table made with the library pandas, we will be waching a table with three columns, the string and it's transformations, the state of the stack and the rule applied step by step, and if the string was accepted or rejected.

```
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
```

If we generate the strings, there will be appearing at least four Strings (two valid and two invalid). To iterate between one string and another we create a iterator and buttons to increment or decrement the iterator. This allow us to show one validation at a time and iterate between the strings.

```
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
```

So, if the user chooses the "Generate Strings" mode, there will be appearing a button to generate the strings, calling the method generateStrings() mentioned before, requesting and showing the strings generated. Furthermore, it will be appearing a button to validate the strings, this "initialize" the validation, put the iterator en 0 and start the procces of validation, calling the method sendValidateString() mentioned before.


```
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
```

On the other hand, if the user chooses the "Enter String", there will be appearing a text box for the user to enter the string of their choice. Then the button to validate the string and show the result.
