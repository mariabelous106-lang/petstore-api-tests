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
        # Иногда Petstore требует api_key, добавим его на будущее
        "api_key": "special-key"
    }

    def __init__(self):
        """
        Когда мы создаем объект класса (client = PetstoreClient()),
        он создает свою сессию для запросов.
        """
        self.session = requests.Session()
        self.session.headers.update(self.HEADERS)

    # 2. МЕТОДЫ ДЛЯ РАБОТЫ С ПИТОМЦАМИ (CRUD)
    
    def create_pet(self, pet_data: dict) -> dict:
        """
        Создает нового питомца.
        Принимает словарь с данными (name, status и т.д.).
        Возвращает JSON-ответ от сервера.
        """
        url = f"{self.BASE_URL}/pet"
        response = self.session.post(url, json=pet_data)
        return response  # Пока возвращаем весь response, чтобы проверить статус-код

    def get_pet(self, pet_id: int) -> dict:
        """Получает питомца по его ID."""
        url = f"{self.BASE_URL}/pet/{pet_id}"
        response = self.session.get(url)
        return response

    def update_pet(self, pet_data: dict) -> dict:
        """Полностью обновляет данные питомца."""
        url = f"{self.BASE_URL}/pet"
        response = self.session.put(url, json=pet_data)
        return response

    def delete_pet(self, pet_id: int) -> dict:
        """Удаляет питомца по ID."""
        url = f"{self.BASE_URL}/pet/{pet_id}"
        response = self.session.delete(url)
        return response