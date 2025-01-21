# tests/test_external_api.py
import pytest
from unittest import mock
from src.external_api import convert_to_rub

@mock.patch("requests.get")
def test_convert_to_rub_success(mock_get):
    # Мокируем успешный ответ от API
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 75.0}

    transaction = {"amount": 100.0, "currency": "USD"}
    result = convert_to_rub(transaction)
    assert result == 75.0

@mock.patch("requests.get")
def test_convert_to_rub_failure(mock_get):
    # Мокируем ошибку API
    mock_get.return_value.status_code = 500
    transaction = {"amount": 100.0, "currency": "USD"}
    result = convert_to_rub(transaction)
    assert result == 100.0  # Возвращаем оригинальную сумму при ошибке API
