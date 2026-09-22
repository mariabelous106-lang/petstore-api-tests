"""
Тесты для эндпоинтов /pet (питомцы).
"""
import allure
from jsonschema import validate
from schemas.pet_schema import PET_SCHEMA


@allure.feature("Pet")
@allure.story("Create and get pet")
def test_create_and_get_pet(client):
    """Создаём питомца и проверяем, что его можно получить по ID."""
    with allure.step("Создаём нового питомца"):
        create_payload = {
            "name": "TestDog",
            "status": "available"
        }
        create_response = client.create_pet(create_payload)
        assert create_response.status_code == 200, f"Ожидался 200, а пришёл {create_response.status_code}"

    with allure.step("Проверяем данные созданного питомца"):
        created_pet = create_response.json()
        pet_id = created_pet["id"]
        assert created_pet["name"] == "TestDog"

    with allure.step("Получаем питомца по ID"):
        get_response = client.get_pet(pet_id=pet_id)
        assert get_response.status_code == 200, f"Ожидался 200, а пришёл {get_response.status_code}"

    with allure.step("Проверяем, что данные совпадают"):
        fetched_pet = get_response.json()
        assert fetched_pet["id"] == pet_id
        assert fetched_pet["name"] == "TestDog"

    with allure.step("Удаляем питомца после теста"):
        client.delete_pet(pet_id=pet_id)

    with allure.step("Проверяем структуру ответа по JSON-схеме"):
        validate(instance=fetched_pet, schema=PET_SCHEMA)


@allure.feature("Pet")
@allure.story("Get nonexistent pet")
def test_get_nonexistent_pet(client):
    """Проверяем запрос несуществующего питомца."""
    with allure.step("Отправляем GET-запрос на несуществующий ID"):
        response = client.get_pet(pet_id=999999999)

    with allure.step("Проверяем, что сервер вернул 404"):
        assert response.status_code == 404, f"Ожидался 404, а пришёл {response.status_code}"