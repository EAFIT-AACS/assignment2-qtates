from fastapi import FastAPI, HTTPException
from Scripts.ALGORITHM_1_LFCO_2025_GV_LC_SM import createCorrectStrings, createWrongStrings
from Scripts.ALGORITHM_2_LFCO_2025_GV_LC_SM import validationString
from Scripts.ALGORITHM_3_LFCO_2025_GV_LC_SM import printTree
from pydantic import BaseModel

# Create a FastAPI instance.
app = FastAPI()

# Create a class to define the data model expected to be received in the API.
class StringInput(BaseModel):
    string: str

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