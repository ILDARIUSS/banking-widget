import re

def filter_transactions_by_keyword(transactions, keyword):
    """
    Фильтрует список транзакций по наличию строки в поле 'description'.

    :param transactions: список словарей с данными о транзакциях.
    :param keyword: строка для поиска в описании.
    :return: список транзакций, содержащих строку в описании.
    """
    keyword_pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    return [transaction for transaction in transactions if keyword_pattern.search(transaction.get("description", ""))]

def count_transactions_by_category(transactions, categories):
    """
    Подсчитывает количество транзакций в каждой категории.

    :param transactions: список словарей с данными о транзакциях.
    :param categories: список категорий для подсчета.
    :return: словарь {категория: количество транзакций}.
    """
    category_counts = {category: 0 for category in categories}

    for transaction in transactions:
        description = transaction.get("description", "").lower()
        for category in categories:
            if category.lower() in description:
                category_counts[category] += 1

    return category_counts
