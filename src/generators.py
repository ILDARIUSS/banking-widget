from typing import Dict, Iterator, List


def filter_by_currency(transactions: List[Dict], currency: str) -> List[Dict]:
    """
    Фильтрует список транзакций по указанной валюте.

    :param transactions: Список транзакций, где каждая транзакция представлена словарем.
    :param currency: Валюта, по которой фильтруются транзакции (например, 'USD').
    :return: Список транзакций, соответствующих указанной валюте.
    """
    return [transaction for transaction in transactions if transaction.get("currency") == currency]


def transaction_descriptions(transactions: List[Dict]) -> List[str]:
    """
    Возвращает список описаний транзакций.

    :param transactions: Список транзакций.
    :return: Список строк, содержащих описание каждой транзакции.
    """
    return [transaction.get("description", "") for transaction in transactions]


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генерирует номера карт в указанном диапазоне.

    :param start: Начальное число (включительно).
    :param end: Конечное число (включительно).
    :return: Итератор, возвращающий сгенерированные номера карт.
    """
    for number in range(start, end + 1):
        yield f"{number:016}"
