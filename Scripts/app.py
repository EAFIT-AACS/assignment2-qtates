from fastapi import FastAPI, HTTPException
from CreateStrings import createCorrectStrings, createWrongStrings

app = FastAPI()

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
