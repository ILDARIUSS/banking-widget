import pytest
from src.transaction_utils import filter_transactions_by_keyword, count_transactions_by_category

TRANSACTIONS = [
    {"id": 1, "description": "Открытие вклада", "amount": "40542 руб."},
    {"id": 2, "description": "Перевод с карты на карту", "amount": "130 USD"},
    {"id": 3, "description": "Оплата услуг ЖКХ", "amount": "8390 руб."},
]


def test_filter_transactions_by_keyword():
    # Проверка, что фильтр правильно ищет ключевое слово
    result = filter_transactions_by_keyword(TRANSACTIONS, "вклад")
    assert len(result) == 1
    assert result[0]["id"] == 1

    # Проверка, что поиск регистронезависим
    result = filter_transactions_by_keyword(TRANSACTIONS, "ВКЛАД")
    assert len(result) == 1
    assert result[0]["id"] == 1

    # Проверка, что неверное ключевое слово возвращает пустой результат
    result = filter_transactions_by_keyword(TRANSACTIONS, "путешествия")
    assert len(result) == 0


def test_count_transactions_by_category():
    # Проверка подсчёта по категориям
    categories = ["вклад", "ЖКХ", "перевод"]
    result = count_transactions_by_category(TRANSACTIONS, categories)

    assert result["вклад"] == 1
    assert result["ЖКХ"] == 1
    assert result["перевод"] == 1

    # Проверка, что несуществующая категория возвращает 0
    categories = ["неизвестная категория"]
    result = count_transactions_by_category(TRANSACTIONS, categories)
    assert result["неизвестная категория"] == 0
