import pytest


@pytest.fixture
def sample_data():
    """Пример данных для тестов"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01T00:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2024-01-02T00:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-03T00:00:00"},
    ]
