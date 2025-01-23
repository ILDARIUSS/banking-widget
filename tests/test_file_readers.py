import pytest
from unittest.mock import patch, MagicMock
from src.file_readers import read_transactions_from_csv, read_transactions_from_excel

@patch("src.file_readers.pd.read_csv")
def test_read_transactions_from_csv(mock_read_csv):
    # Мок данные
    mock_data = [
        {"id": 1, "amount": 100, "currency": "USD"},
        {"id": 2, "amount": 200, "currency": "EUR"}
    ]
    mock_read_csv.return_value = pd.DataFrame(mock_data)

    # Тестируем функцию
    result = read_transactions_from_csv("fake_path.csv")
    assert result == mock_data
    mock_read_csv.assert_called_once_with("fake_path.csv")

@patch("src.file_readers.pd.read_excel")
def test_read_transactions_from_excel(mock_read_excel):
    # Мок данные
    mock_data = [
        {"id": 1, "amount": 100, "currency": "USD"},
        {"id": 2, "amount": 200, "currency": "EUR"}
    ]
    mock_read_excel.return_value = pd.DataFrame(mock_data)

    # Тестируем функцию
    result = read_transactions_from_excel("fake_path.xlsx")
    assert result == mock_data
    mock_read_excel.assert_called_once_with("fake_path.xlsx")
