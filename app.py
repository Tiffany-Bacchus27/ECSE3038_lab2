from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app = FastAPI()


data = []


class Person(BaseModel):
    name: str
    occupation: str
    address: str

@app.post("/person")
async def add_person(person_request: Person):
    
    if not person_request.name or not person_request.occupation or not person_request.address:
        return {
            "success": False,
            "result": {
                "error_message": "invalid request"
            }
        }
    
    
    person_json = jsonable_encoder(person_request)
    data.append(person_json)
    
    return {
        "success": True,
        "result": person_json
    }

@app.get("/person")
async def get_people():
    return data
