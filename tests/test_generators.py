import pytest
from generators import filter_by_currency, transaction_descriptions, card_number_generator

@pytest.fixture
def sample_transactions():
    """
    Фикстура для предоставления списка примерных транзакций.
    """
    return [
        {"id": 1, "amount": 100, "currency": "USD", "description": "Payment for services"},
        {"id": 2, "amount": 200, "currency": "EUR", "description": "Refund"},
        {"id": 3, "amount": 150, "currency": "USD", "description": "Salary"},
    ]


def test_filter_by_currency(sample_transactions):
    """
    Тест для функции filter_by_currency.
    """
    result = filter_by_currency(sample_transactions, "USD")
    assert len(result) == 2
    assert all(transaction["currency"] == "USD" for transaction in result)


def test_transaction_descriptions(sample_transactions):
    """
    Тест для функции transaction_descriptions.
    """
    result = transaction_descriptions(sample_transactions)
    assert result == ["Payment for services", "Refund", "Salary"]


def test_card_number_generator():
    """
    Тест для функции card_number_generator.
    """
    result = list(card_number_generator(1, 3))
    assert result == ["0000000000000001", "0000000000000002", "0000000000000003"]
