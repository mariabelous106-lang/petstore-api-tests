"""
Тесты для эндпоинтов /pet (питомцы).
"""


def test_create_and_get_pet(client):
    """Создаём питомца и проверяем, что его можно получить по ID."""
    create_payload = {
        "name": "TestDog",
        "status": "available"
    }
    create_response = client.create_pet(create_payload)
    assert create_response.status_code == 200, f"Ожидался 200, а пришёл {create_response.status_code}"

    created_pet = create_response.json()
    pet_id = created_pet["id"]
    assert created_pet["name"] == "TestDog"

    get_response = client.get_pet(pet_id=pet_id)
    assert get_response.status_code == 200, f"Ожидался 200, а пришёл {get_response.status_code}"

    fetched_pet = get_response.json()
    assert fetched_pet["id"] == pet_id
    assert fetched_pet["name"] == "TestDog"

    client.delete_pet(pet_id=pet_id)


def test_get_nonexistent_pet(client):
    """Проверяем запрос несуществующего питомца."""
    response = client.get_pet(pet_id=999999999)
    assert response.status_code == 404, f"Ожидался 404, а пришёл {response.status_code}"