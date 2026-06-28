import requests

BASE_URL = "http://127.0.0.1:8000"


# ---------- GET ----------
def test_get_pet_by_id():
    response = requests.get(f"{BASE_URL}/pet/1")
    assert response.status_code == 200, f"Ожидался 200, а пришёл {response.status_code}"
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Барсик"


def test_get_nonexistent_pet():
    response = requests.get(f"{BASE_URL}/pet/999")
    assert response.status_code == 404


# ---------- POST ----------
def test_create_pet():
    payload = {"name": "Мурка", "status": "available"}
    response = requests.post(f"{BASE_URL}/pet", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Мурка"
    assert data["status"] == "available"
    assert "id" in data


def test_create_pet_without_status():
    """Статус по умолчанию — available."""
    payload = {"name": "Рекс"}
    response = requests.post(f"{BASE_URL}/pet", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "available"


# ---------- PUT ----------
def test_update_pet():
    payload = {"name": "Барсик Обновлённый", "status": "sold"}
    response = requests.put(f"{BASE_URL}/pet/1", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Барсик Обновлённый"
    assert data["status"] == "sold"


def test_update_nonexistent_pet():
    payload = {"name": "Фантом"}
    response = requests.put(f"{BASE_URL}/pet/777", json=payload)
    assert response.status_code == 404


# ---------- DELETE ----------
def test_delete_pet():
    # Сначала создаём питомца для удаления
    create_resp = requests.post(f"{BASE_URL}/pet", json={"name": "НаУдаление"})
    pet_id = create_resp.json()["id"]

    response = requests.delete(f"{BASE_URL}/pet/{pet_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Питомец удалён"}

    # Проверяем, что питомец действительно удалён
    get_resp = requests.get(f"{BASE_URL}/pet/{pet_id}")
    assert get_resp.status_code == 404


def test_delete_nonexistent_pet():
    response = requests.delete(f"{BASE_URL}/pet/999")
    assert response.status_code == 404