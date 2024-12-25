import pytest
from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


def test_filter_by_currency():
    transactions = [
        {
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Transaction 1",
        },
        {
            "operationAmount": {"currency": {"code": "RUB"}},
            "description": "Transaction 2",
        },
    ]
    usd_transactions = filter_by_currency(transactions, "USD")
    assert next(usd_transactions)["description"] == "Transaction 1"


def test_transaction_descriptions():
    transactions = [
        {"description": "Transaction 1"},
        {"description": "Transaction 2"},
    ]
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == "Transaction 1"
    assert next(descriptions) == "Transaction 2"


def test_card_number_generator():
    generator = card_number_generator(1, 3)
    assert next(generator) == "0000000000000001"
    assert next(generator) == "0000000000000002"
    assert next(generator) == "0000000000000003"
