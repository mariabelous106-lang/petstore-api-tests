import pytest
from helpers.api_client import PetstoreClient


@pytest.fixture(scope="function")
def client():
    """
    Фикстура, которая создаёт объект клиента API.
    scope="function" означает, что для каждого теста
    будет создаваться новый экземпляр клиента.
    Это изолирует тесты друг от друга.
    """
    return PetstoreClient()