"""
Тесты для эндпоинтов /pet (питомцы).
"""


def test_get_pet_by_id(client):
    """Проверяем получение существующего питомца по ID."""
    response = client.get_pet(pet_id=1)
    assert response.status_code == 200, f"Ожидался 200, а пришёл {response.status_code}"
    data = response.json()
    assert data["id"] == 1
    assert "name" in data


def test_get_nonexistent_pet(client):
    """Проверяем запрос несуществующего питомца."""
    response = client.get_pet(pet_id=99999)
    assert response.status_code == 404