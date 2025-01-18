# tests/test_utils.py
import os
import pytest
from unittest.mock import patch, mock_open
from src.utils import read_transactions_from_json
from src.external_api import convert_to_rub


# Тестирование функции чтения данных из JSON
def test_read_transactions_from_json():
    mock_data = '[{"id": 1, "amount": 100.0, "currency": "USD"}]'

    with patch('builtins.open', mock_open(read_data=mock_data)):
        result = read_transactions_from_json('data/operations.json')
        assert len(result) == 1
        assert result[0]['currency'] == 'USD'

    # Тестируем случай, когда файл пустой
    with patch('builtins.open', mock_open(read_data='')):
        result = read_transactions_from_json('data/empty.json')
        assert result == []

    # Тестируем случай, когда JSON некорректен
    with patch('builtins.open', mock_open(read_data='{invalid json}')):
        result = read_transactions_from_json('data/invalid.json')
        assert result == []


# Тестирование функции конвертации валют
@patch('src.external_api.requests.get')
def test_convert_to_rub(mock_get):
    # Настроим mock для ответа API
    mock_get.return_value.json.return_value = {'result': 75.0}

    # Пример транзакции в USD
    transaction = {"amount": 100.0, "currency": "USD"}
    result = convert_to_rub(transaction)
    assert result == 7500.0

    # Пример транзакции в EUR
    transaction = {"amount": 100.0, "currency": "EUR"}
    result = convert_to_rub(transaction)
    assert result == 7500.0

    # Пример транзакции в рублях
    transaction = {"amount": 100.0, "currency": "RUB"}
    result = convert_to_rub(transaction)
    assert result == 200.0
