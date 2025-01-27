import pytest
from unittest import mock
from src.utils import read_json_file

@mock.patch("builtins.open", mock.mock_open(read_data='[{"id": 1, "amount": 100.0, "currency": "USD"}]'))
def test_read_json_file_success():
    result = read_json_file("mock_path.json")
    assert result == [{"id": 1, "amount": 100.0, "currency": "USD"}]


@mock.patch("builtins.open", mock.mock_open(read_data=''))
def test_read_json_file_empty():
    result = read_json_file("test.json")

    assert result == []


@mock.patch("builtins.open", mock.mock_open())
def test_read_json_file_file_not_found():
    result = read_json_file("nonexistent.json")
    assert result == []
