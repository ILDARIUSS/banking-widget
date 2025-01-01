import pytest
from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)

# Фикстура для тестовых данных
@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "currency": "USD", "description": "Transaction 1"},
        {"id": 2, "currency": "EUR", "description": "Transaction 2"},
        {"id": 3, "currency": "USD", "description": "Transaction 3"},
        {"id": 4, "currency": "GBP", "description": "Transaction 4"},
    ]


# Тест для функции filter_by_currency
@pytest.mark.parametrize(
    "currency,expected_count",
    [("USD", 2), ("EUR", 1), ("GBP", 1), ("JPY", 0)],
)
def test_filter_by_currency(sample_transactions, currency, expected_count):
    result = filter_by_currency(sample_transactions, currency)
    assert len(result) == expected_count


# Тест для функции transaction_descriptions
@pytest.mark.parametrize(
    "transactions,expected_descriptions",
    [
        (
            [
                {"id": 1, "currency": "USD", "description": "Transaction 1"},
                {"id": 2, "currency": "EUR", "description": "Transaction 2"},
            ],
            ["Transaction 1", "Transaction 2"],
        ),
        (
            [{"id": 1, "currency": "USD"}],
            [""],  # Ожидается пустая строка, если description отсутствует
        ),
        ([], []),  # Пустой список должен вернуть пустой результат
    ],
)
def test_transaction_descriptions(transactions, expected_descriptions):
    result = transaction_descriptions(transactions)
    assert result == expected_descriptions


# Тест для функции card_number_generator
@pytest.mark.parametrize(
    "start,end,expected_cards",
    [
        (1, 3, ["0000000000000001", "0000000000000002", "0000000000000003"]),
        (5, 5, ["0000000000000005"]),
        (10, 12, ["0000000000000010", "0000000000000011", "0000000000000012"]),
    ],
)
def test_card_number_generator(start, end, expected_cards):
    result = list(card_number_generator(start, end))
    assert result == expected_cards
