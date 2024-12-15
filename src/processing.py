from typing import List, Dict


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список операций по указанному статусу.

    :param data: Список словарей, содержащий операции.
    :param state: Статус, по которому фильтруются операции. По умолчанию 'EXECUTED'.
    :return: Список операций с указанным статусом.
    """
    return [operation for operation in data if operation.get("state") == state]


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список операций по дате.

    :param data: Список словарей, содержащий операции.
    :param reverse: Указывает порядок сортировки: True — по убыванию, False — по возрастанию.
    :return: Отсортированный список операций.
    """
    return sorted(data, key=lambda operation: operation["date"], reverse=reverse)
