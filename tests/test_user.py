"""
Тесты для эндпоинтов /user (пользователи).
"""
import allure
import pytest
from jsonschema import validate
from schemas.pet_schema import USER_SCHEMA


@allure.feature("User")
@allure.story("Create and get user")
def test_create_and_get_user(client):
    """Создаём пользователя и проверяем, что его можно получить по username."""
    with allure.step("Создаём нового пользователя"):
        user_payload = {
            "id": 12345,
            "username": "testuser_qa",
            "firstName": "Test",
            "lastName": "User",
            "email": "test@example.com",
            "password": "password123",
            "phone": "1234567890",
            "userStatus": 1
        }
        create_response = client.create_user(user_payload)
        assert create_response.status_code == 200, f"Ожидался 200, а пришёл {create_response.status_code}"

    with allure.step("Получаем пользователя по username"):
        get_response = client.get_user(username="testuser_qa")
        assert get_response.status_code == 200, f"Ожидался 200, а пришёл {get_response.status_code}"

    with allure.step("Проверяем данные пользователя"):
        fetched_user = get_response.json()
        assert fetched_user["username"] == "testuser_qa"
        assert fetched_user["email"] == "test@example.com"

    with allure.step("Проверяем структуру ответа по JSON-схеме"):
        validate(instance=fetched_user, schema=USER_SCHEMA)

    with allure.step("Удаляем пользователя после теста"):
        client.delete_user(username="testuser_qa")


@allure.feature("User")
@allure.story("Login and logout")
def test_login_and_logout(client):
    """Проверяем авторизацию и выход пользователя."""
    with allure.step("Создаём пользователя для логина"):
        user_payload = {
            "id": 54321,
            "username": "loginuser_qa",
            "password": "secret123",
            "userStatus": 1
        }
        client.create_user(user_payload)

    with allure.step("Авторизуемся с правильными данными"):
        login_response = client.login(username="loginuser_qa", password="secret123")
        assert login_response.status_code == 200, f"Ожидался 200, а пришёл {login_response.status_code}"

    with allure.step("Проверяем, что в ответе есть сообщение об успехе"):
        login_data = login_response.json()
        assert "message" in login_data

    with allure.step("Выходим из системы"):
        logout_response = client.logout()
        assert logout_response.status_code == 200

    with allure.step("Удаляем пользователя после теста"):
        client.delete_user(username="loginuser_qa")


@allure.feature("User")
@allure.story("Get nonexistent user")
def test_get_nonexistent_user(client):
    """Проверяем запрос несуществующего пользователя."""
    with allure.step("Отправляем GET-запрос на несуществующий username"):
        response = client.get_user(username="nonexistent_user_99999")

    with allure.step("Проверяем, что сервер вернул 404"):
        assert response.status_code == 404, f"Ожидался 404, а пришёл {response.status_code}"


@pytest.mark.xfail(reason="Petstore API allows login with wrong password (BUG-02)")
@allure.feature("User")
@allure.story("Login with wrong password")
def test_login_with_wrong_password(client):
    """Проверяем, что вход с неверным паролем не проходит."""
    with allure.step("Создаём пользователя"):
        user_payload = {
            "id": 11111,
            "username": "wrongpass_user",
            "password": "correct123",
            "userStatus": 1
        }
        client.create_user(user_payload)

    with allure.step("Пробуем войти с неверным паролем"):
        response = client.login(username="wrongpass_user", password="wrong_password")

    with allure.step("Проверяем, что сервер вернул ошибку"):
        assert response.status_code in [400, 401, 403], f"Ожидалась ошибка авторизации, а пришёл {response.status_code}"

    with allure.step("Удаляем пользователя после теста"):
        client.delete_user(username="wrongpass_user")