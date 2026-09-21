# Petstore API Tests

Автотесты для тестового REST API на Python + Pytest + Requests.

![Run API Tests](https://github.com/mariabelous106-lang/petstore-api-tests/actions/workflows/tests.yml/badge.svg)

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
uvicorn server:app --reload
pytest -v

## Allure Report

![Allure Report](https://github.com/user-attachments/assets/8e3a699b-4f2f-47e1-a90d-89e316ea9863)

Отчёт генерируется командой:
```bash
pytest --alluredir=allure-results
allure serve allure-results