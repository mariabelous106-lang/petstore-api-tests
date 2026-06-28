# Petstore API Tests

Автотесты для тестового REST API на Python + Pytest + Requests.

## Стек
- Python 3.14
- Pytest
- Requests
- FastAPI (локальный сервер)

## Установка и запуск

```bash
git clone https://github.com/mariabelous106-lang/petstore-api-tests.git
cd petstore-api-tests
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn server:app --reload
pytest -v