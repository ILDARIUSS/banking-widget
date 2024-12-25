def filter_by_currency(transactions: list[dict], currency_code: str):
    """
    Фильтрует транзакции по заданной валюте.
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions: list[dict]):
    """
    Возвращает описания транзакций.
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int):
    """
    Генерирует номера карт в заданном диапазоне.
    """
    for number in range(start, end + 1):
        yield f"{number:016}"
