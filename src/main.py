from src.processing import filter_by_state, sort_by_date

data = [
    {"id": 1, "state": "EXECUTED", "date": "2024-01-01T00:00:00"},
    {"id": 2, "state": "CANCELED", "date": "2024-01-02T00:00:00"},
]

print("Filtered data:", filter_by_state(data))
print("Sorted data:", sort_by_date(data))
