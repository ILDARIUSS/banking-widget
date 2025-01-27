import re
from collections import Counter


def filter_transactions_by_keyword(transactions, keyword):
    """
    Фильтрует транзакции по ключевому слову в описании.

    :param transactions: список транзакций (словарей).
    :param keyword: строка для поиска в описании.
    :return: список транзакций, содержащих ключевое слово в описании.
    """
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    return [t for t in transactions if pattern.search(t.get("description", ""))]


def count_transactions_by_category(transactions, categories):
    """
    Подсчитывает количество транзакций по категориям.

    :param transactions: список транзакций (словарей).
    :param categories: список категорий.
    :return: словарь {категория: количество}.
    """
    category_counter = Counter()
    for transaction in transactions:
        description = transaction.get("description", "").lower()
        for category in categories:
            if category.lower().strip() in description:
                category_counter[category.strip()] += 1
    return dict(category_counter)
