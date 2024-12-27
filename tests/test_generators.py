import pytest

from generators import card_number_generator, filter_by_currency, transaction_descriptions


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


@pytest.fixture
def card_generator_data():
    """
    Фикстура для предоставления диапазона генерации номеров карт.
    """
    return {"start": 1, "end": 3}


def test_filter_by_currency(sample_transactions):
    """
    Тест для функции filter_by_currency.
    """
    result = filter_by_currency(sample_transactions, "USD")
    assert len(result) == 2
    assert all(transaction["currency"] == "USD" for transaction in result)


@pytest.mark.parametrize("currency,expected_count", [("USD", 2), ("EUR", 1), ("GBP", 0)])
def test_filter_by_currency_parametrized(sample_transactions, currency, expected_count):
    """
    Параметризованный тест для функции filter_by_currency.
    """
    result = filter_by_currency(sample_transactions, currency)
    assert len(result) == expected_count


def test_transaction_descriptions(sample_transactions):
    """
    Тест для функции transaction_descriptions.
    """
    result = transaction_descriptions(sample_transactions)
    assert result == ["Payment for services", "Refund", "Salary"]


@pytest.mark.parametrize(
    "transactions,expected_descriptions",
    [
        ([{"description": "Test"}], ["Test"]),
        ([{"description": "Another Test"}, {"description": ""}], ["Another Test", ""]),
    ],
)
def test_transaction_descriptions_parametrized(transactions, expected_descriptions):
    """
    Параметризованный тест для функции transaction_descriptions.
    """
    result = transaction_descriptions(transactions)
    assert result == expected_descriptions


def test_card_number_generator(card_generator_data):
    """
    Тест для функции card_number_generator.
    """
    result = list(card_number_generator(card_generator_data["start"], card_generator_data["end"]))
    assert result == ["0000000000000001", "0000000000000002", "0000000000000003"]
