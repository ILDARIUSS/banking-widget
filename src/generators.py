from typing import Dict, Iterator, List


def filter_by_currency(transactions: List[Dict], currency_code: str) -> Iterator[Dict]:
    """
    Генератор для фильтрации транзакций по указанной валюте.

    :param transactions: Список словарей с транзакциями.
    :param currency_code: Код валюты, например, "USD".
    :yield: Транзакции, где валюта совпадает с currency_code.
    """
    for transaction in transactions:
        currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")
        if currency == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генератор, возвращающий описание каждой транзакции.

    :param transactions: Список словарей с транзакциями.
    :yield: Описание транзакции, если оно есть, иначе строка "Описание отсутствует".
    """
    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.

    :param start: Начальное значение диапазона (включительно).
    :param end: Конечное значение диапазона (включительно).
    :yield: Номер карты в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, end + 1):
        yield f"{number:016d}".replace("", " ")[1:-1].strip()
