# api/app.py
from fastapi import FastAPI
from CreateStrings import createCorrectStrings, createWrongStrings

app = FastAPI()

@app.get("/generate-correct")
async def generate_correct():
    return {"strings": createCorrectStrings()}

@app.get("/generate-wrong")
async def generate_wrong():
    return {"strings": createWrongStrings()}
