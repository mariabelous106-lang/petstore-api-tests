import requests

BASE_URL = "http://127.0.0.1:8000"


def test_get_pet_by_id():
    """Проверяем, что API возвращает питомца по ID."""
    response = requests.get(f"{BASE_URL}/pet/1")
    assert response.status_code == 200, f"Ожидался 200, а пришёл {response.status_code}"
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Барсик"
    print(f"Найден питомец: {data['name']}")


def test_get_nonexistent_pet():
    """Проверяем, что несуществующий питомец возвращает 404."""
    response = requests.get(f"{BASE_URL}/pet/999")
    assert response.status_code == 404, f"Ожидался 404, а пришёл {response.status_code}"