from fastapi import FastAPI, HTTPException

app = FastAPI()

pets = {
    1: {"id": 1, "name": "Барсик", "status": "available"},
    2: {"id": 2, "name": "Шарик", "status": "sold"},
}


@app.get("/pet/{pet_id}")
def get_pet(pet_id: int):
    if pet_id in pets:
        return pets[pet_id]
    raise HTTPException(status_code=404, detail="Питомец не найден")