"""
Тесты для эндпоинтов /store (заказы).
"""
import allure
from jsonschema import validate
from schemas.pet_schema import ORDER_SCHEMA

@allure.feature("Store")
@allure.story("Get inventory")
def test_get_inventory(client):
    """Проверяем, что склад возвращает статусы питомцев."""
    with allure.step("Отправляем GET-запрос на /store/inventory"):
        response = client.get_inventory()

    with allure.step("Проверяем, что сервер вернул 200"):
        assert response.status_code == 200, f"Ожидался 200, а пришёл {response.status_code}"

    with allure.step("Проверяем, что ответ — это словарь со статусами"):
        data = response.json()
        assert isinstance(data, dict)
        assert len(data) > 0


@allure.feature("Store")
@allure.story("Create and get order")
def test_create_and_get_order(client):
    """Создаём заказ и проверяем, что его можно получить по ID."""
    with allure.step("Создаём новый заказ"):
        order_payload = {
            "id": 12345,
            "petId": 1,
            "quantity": 2,
            "status": "placed"
        }
        create_response = client.create_order(order_payload)
        assert create_response.status_code == 200, f"Ожидался 200, а пришёл {create_response.status_code}"

    with allure.step("Проверяем данные созданного заказа"):
        created_order = create_response.json()
        assert created_order["id"] == 12345
        assert created_order["status"] == "placed"

    with allure.step("Получаем заказ по ID"):
        get_response = client.get_order(order_id=12345)
        assert get_response.status_code == 200, f"Ожидался 200, а пришёл {get_response.status_code}"

    with allure.step("Проверяем, что данные совпадают"):
        fetched_order = get_response.json()
        assert fetched_order["id"] == 12345

    with allure.step("Удаляем заказ после теста"):
        client.delete_order(order_id=12345)
    with allure.step("Проверяем структуру ответа по JSON-схеме"):
        validate(instance=fetched_order, schema=ORDER_SCHEMA)

@allure.feature("Store")
@allure.story("Get nonexistent order")
def test_get_nonexistent_order(client):
    """Проверяем запрос несуществующего заказа."""
    with allure.step("Отправляем GET-запрос на несуществующий ID"):
        response = client.get_order(order_id=999999999)

    with allure.step("Проверяем, что сервер вернул 404"):
        assert response.status_code == 404, f"Ожидался 404, а пришёл {response.status_code}"