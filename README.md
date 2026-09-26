![Run API Tests](https://github.com/mariabelous106-lang/petstore-api-tests/actions/workflows/tests.yml/badge.svg)

# Petstore API Tests

Автотесты для тестового REST API на Python + Pytest + Requests.

## Стек
- Python 3.14
- Pytest
- Requests
- FastAPI (локальный сервер)
- `postman/` — коллекция Postman для ручного тестирования API

## Установка и запуск

```bash
git clone https://github.com/mariabelous106-lang/petstore-api-tests.git
cd petstore-api-tests
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pytest -v
```

## Allure Report

![Allure Report](https://github.com/user-attachments/assets/8e3a699b-4f2f-47e1-a90d-89e316ea9863)

Отчёт генерируется командами:

```bash
pytest --alluredir=allure-results
allure serve allure-results
```
## Known Bugs in Petstore API

Найдены и задокументированы через `xfail`-тесты:

- **BUG-01:** API создаёт питомца с пустым именем (ожидался код 422, получен 200)
- **BUG-02:** API авторизует пользователя с неверным паролем (ожидался код 401, получен 200)

Тесты: `tests/test_pet.py::test_create_pet_with_empty_name`, `tests/test_user.py::test_login_with_wrong_password`