from fastapi import FastAPI, HTTPException, Query
from CreateStrings import createCorrectStrings, createWrongStrings
from Automaton import validationString
from PrintTree import printTree
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modelo para recibir los vectores
class StringsInput(BaseModel):
    correct: List[str]
    wrong: List[str]

@app.get("/generate-correct")
async def generate_correct():
    try:
        return {"strings": createCorrectStrings()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en generate_correct: {str(e)}")

@app.get("/generate-wrong")
async def generate_wrong():
    try:
        return {"strings": createWrongStrings()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en generate_wrong: {str(e)}")

@app.post("/validation1")
def validate(data: StringsInput):
    print("📥 Datos recibidos en la API:", data)
    return {
        "message": f"Se recibieron {len(data.correct)} cadenas correctas y {len(data.wrong)} cadenas incorrectas.",
    }