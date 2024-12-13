from src.processing import filter_by_state, sort_by_date


def test_filter_by_state():
    data = [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01T00:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2024-01-02T00:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-03T00:00:00"},
    ]
    assert filter_by_state(data) == [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01T00:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-03T00:00:00"},
    ]
    assert filter_by_state(data, "CANCELED") == [
        {"id": 2, "state": "CANCELED", "date": "2024-01-02T00:00:00"},
    ]


def test_sort_by_date():
    data = [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01T00:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2024-01-02T00:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-03T00:00:00"},
    ]
    assert sort_by_date(data) == [
        {"id": 3, "state": "EXECUTED", "date": "2024-01-03T00:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2024-01-02T00:00:00"},
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01T00:00:00"},
    ]
    assert sort_by_date(data, reverse=False) == [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01T00:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2024-01-02T00:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-03T00:00:00"},
    ]
