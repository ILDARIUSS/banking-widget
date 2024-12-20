import pytest
from src.processing import filter_by_state, sort_by_date

@pytest.mark.parametrize(
    "state,expected",
    [
        ("EXECUTED", [
            {"id": 1, "state": "EXECUTED", "date": "2024-01-01T00:00:00"},
            {"id": 3, "state": "EXECUTED", "date": "2024-01-03T00:00:00"},
        ]),
        ("CANCELED", [
            {"id": 2, "state": "CANCELED", "date": "2024-01-02T00:00:00"},
        ]),
        ("PENDING", []),  # Тест для состояния, отсутствующего в данных
    ]
)
def test_filter_by_state(sample_data, state, expected):
    assert filter_by_state(sample_data, state) == expected

@pytest.mark.parametrize(
    "reverse,expected",
    [
        (True, [
            {"id": 3, "state": "EXECUTED", "date": "2024-01-03T00:00:00"},
            {"id": 2, "state": "CANCELED", "date": "2024-01-02T00:00:00"},
            {"id": 1, "state": "EXECUTED", "date": "2024-01-01T00:00:00"},
        ]),
        (False, [
            {"id": 1, "state": "EXECUTED", "date": "2024-01-01T00:00:00"},
            {"id": 2, "state": "CANCELED", "date": "2024-01-02T00:00:00"},
            {"id": 3, "state": "EXECUTED", "date": "2024-01-03T00:00:00"},
        ]),
    ]
)
def test_sort_by_date(sample_data, reverse, expected):
    assert sort_by_date(sample_data, reverse) == expected
