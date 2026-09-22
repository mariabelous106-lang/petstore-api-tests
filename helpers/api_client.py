# helpers/api_client.py
import requests
import json

class PetstoreClient:
    """
    Это наш персональный помощник для работы с API Petstore.
    Он инкапсулирует (скрывает) детали отправки запросов.
    """
    
    # 1. БАЗОВЫЕ НАСТРОЙКИ
    BASE_URL = "https://petstore.swagger.io/v2"
    HEADERS = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "api_key": "special-key"
    }

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(self.HEADERS)

    # 2. МЕТОДЫ ДЛЯ РАБОТЫ С ПИТОМЦАМИ (CRUD)
    
    def create_pet(self, pet_data: dict) -> dict:
        url = f"{self.BASE_URL}/pet"
        response = self.session.post(url, json=pet_data)
        return response

    def get_pet(self, pet_id: int) -> dict:
        url = f"{self.BASE_URL}/pet/{pet_id}"
        response = self.session.get(url)
        return response

    def update_pet(self, pet_data: dict) -> dict:
        url = f"{self.BASE_URL}/pet"
        response = self.session.put(url, json=pet_data)
        return response

    def delete_pet(self, pet_id: int) -> dict:
        url = f"{self.BASE_URL}/pet/{pet_id}"
        response = self.session.delete(url)
        return response

    # 3. МЕТОДЫ ДЛЯ РАБОТЫ С ЗАКАЗАМИ (STORE)

    def get_inventory(self):
        """Возвращает статусы питомцев и их количество."""
        url = f"{self.BASE_URL}/store/inventory"
        response = self.session.get(url)
        return response

    def create_order(self, order_data: dict):
        """Создаёт новый заказ."""
        url = f"{self.BASE_URL}/store/order"
        response = self.session.post(url, json=order_data)
        return response

    def get_order(self, order_id: int):
        """Получает заказ по ID."""
        url = f"{self.BASE_URL}/store/order/{order_id}"
        response = self.session.get(url)
        return response

    def delete_order(self, order_id: int):
        """Удаляет заказ по ID."""
        url = f"{self.BASE_URL}/store/order/{order_id}"
        response = self.session.delete(url)
        return response

    # 4. МЕТОДЫ ДЛЯ РАБОТЫ С ПОЛЬЗОВАТЕЛЯМИ (USER)

    def create_user(self, user_data: dict):
        """Создаёт нового пользователя."""
        url = f"{self.BASE_URL}/user"
        response = self.session.post(url, json=user_data)
        return response

    def get_user(self, username: str):
        """Получает пользователя по username."""
        url = f"{self.BASE_URL}/user/{username}"
        response = self.session.get(url)
        return response

    def update_user(self, username: str, user_data: dict):
        """Обновляет данные пользователя."""
        url = f"{self.BASE_URL}/user/{username}"
        response = self.session.put(url, json=user_data)
        return response

    def delete_user(self, username: str):
        """Удаляет пользователя по username."""
        url = f"{self.BASE_URL}/user/{username}"
        response = self.session.delete(url)
        return response

    def login(self, username: str, password: str):
        """Авторизует пользователя."""
        url = f"{self.BASE_URL}/user/login"
        params = {"username": username, "password": password}
        response = self.session.get(url, params=params)
        return response

    def logout(self):
        """Выходит из системы."""
        url = f"{self.BASE_URL}/user/logout"
        response = self.session.get(url)
        return response