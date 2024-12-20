import pytest

from src.processing import filter_by_state, sort_by_date

# Тесты для filter_by_state


@pytest.mark.parametrize(
    "state,expected",
    [
        (
            "EXECUTED",
            [
                {"id": 1, "state": "EXECUTED", "date": "2024-01-01T00:00:00"},
                {"id": 3, "state": "EXECUTED", "date": "2024-01-03T00:00:00"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 2, "state": "CANCELED", "date": "2024-01-02T00:00:00"},
            ],
        ),
        ("PENDING", []),  # Проверка для состояния, отсутствующего в данных
    ],
)
def test_filter_by_state(sample_data, state, expected):
    assert filter_by_state(sample_data, state) == expected


def test_filter_by_state_empty():
    """Проверка работы с пустым списком"""
    assert filter_by_state([]) == []


def test_filter_by_state_invalid_key():
    """Проверка работы с отсутствующим ключом state"""
    data = [{"id": 1, "date": "2024-01-01T00:00:00"}]
    assert filter_by_state(data) == []


# Тесты для sort_by_date
@pytest.mark.parametrize(
    "reverse,expected",
    [
        (
            True,
            [
                {"id": 3, "state": "EXECUTED", "date": "2024-01-03T00:00:00"},
                {"id": 2, "state": "CANCELED", "date": "2024-01-02T00:00:00"},
                {"id": 1, "state": "EXECUTED", "date": "2024-01-01T00:00:00"},
            ],
        ),
        (
            False,
            [
                {"id": 1, "state": "EXECUTED", "date": "2024-01-01T00:00:00"},
                {"id": 2, "state": "CANCELED", "date": "2024-01-02T00:00:00"},
                {"id": 3, "state": "EXECUTED", "date": "2024-01-03T00:00:00"},
            ],
        ),
    ],
)
def test_sort_by_date(sample_data, reverse, expected):
    assert sort_by_date(sample_data, reverse) == expected


def test_sort_by_date_empty():
    """Проверка работы с пустым списком"""
    assert sort_by_date([]) == []


def test_sort_by_date_invalid_date():
    """Проверка обработки некорректного формата даты"""
    data = [{"id": 1, "state": "EXECUTED", "date": "invalid_date"}]
    with pytest.raises(ValueError, match="Invalid date format"):
        sort_by_date(data)
