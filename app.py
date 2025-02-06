from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app = FastAPI()

data = [
    {"name": "Sam Holland", "occupation": "Librarian", "age": 28},
    {"name": "Alex Jordan", "occupation": "Graphic Artist", "age": 26},
    {"name": "Clover Butler", "occupation": "Fashion Designer", "age": 27}
]

class Person(BaseModel):
    name: str
    occupation: str
    age: int

@app.post("/person")
async def add_person(person_request: Person):
   
    if not person_request.name or not person_request.occupation or not person_request.age:
        return {"success": False, "result": {"error_message": "invalid request"}}
    
    person_json = jsonable_encoder(person_request)
    data.append(person_json) 

    return {"success": True, "result": person_json}

@app.get("/person")
async def get_people():
    return data

    
