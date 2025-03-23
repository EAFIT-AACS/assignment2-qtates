from fastapi import FastAPI, HTTPException, Query
from CreateStrings import createCorrectStrings, createWrongStrings
from Automaton import validationString
from PrintTree import printTree
from pydantic import BaseModel

app = FastAPI()

#Creamos una clase para definir el modelo de datos que se espera recibir en la API.
class StringInput(BaseModel):
    string: str

#Definimos la ruta de la API que llamará al método createCorrectStrings() y retornará las cadenas correctas.
@app.get("/generate-correct")
async def generate_correct():
    try:
        return {"strings": createCorrectStrings()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en generate_correct: {str(e)}")

#Definimos la ruta de la API que llamará al método createWrongStrings() y retornará las cadenas incorrectas.
@app.get("/generate-wrong")
async def generate_wrong():
    try:
        return {"strings": createWrongStrings()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en generate_wrong: {str(e)}")

#Definimos la ruta de la API que validará la cadena recibida. Y retornará si es correcta, incorrecta y su arbol de derivación.
@app.post("/validation1")
def validate(data: StringInput):
    print("📥 Datos recibidos en la API:", data)
    resultValidation=validationString(data.string)
    tree=printTree(resultValidation)
    return {
        "message": f"Se recibió la cadena: {tree}",
    }