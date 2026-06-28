from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

pets = {
    1: {"id": 1, "name": "Барсик", "status": "available"},
    2: {"id": 2, "name": "Шарик", "status": "sold"},
}
next_id = 3


class PetCreate(BaseModel):
    name: str
    status: Optional[str] = "available"


class PetUpdate(BaseModel):
    name: Optional[str] = None
    status: Optional[str] = None


@app.get("/pet/{pet_id}")
def get_pet(pet_id: int):
    if pet_id in pets:
        return pets[pet_id]
    raise HTTPException(status_code=404, detail="Питомец не найден")


@app.post("/pet")
def create_pet(pet: PetCreate):
    global next_id
    new_pet = {"id": next_id, "name": pet.name, "status": pet.status}
    pets[next_id] = new_pet
    next_id += 1
    return new_pet


@app.put("/pet/{pet_id}")
def update_pet(pet_id: int, pet: PetUpdate):
    if pet_id not in pets:
        raise HTTPException(status_code=404, detail="Питомец не найден")
    if pet.name is not None:
        pets[pet_id]["name"] = pet.name
    if pet.status is not None:
        pets[pet_id]["status"] = pet.status
    return pets[pet_id]


@app.delete("/pet/{pet_id}")
def delete_pet(pet_id: int):
    if pet_id not in pets:
        raise HTTPException(status_code=404, detail="Питомец не найден")
    del pets[pet_id]
    return {"message": "Питомец удалён"}