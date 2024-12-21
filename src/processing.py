from datetime import datetime
from typing import Dict, List


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
    Сортирует список словарей по ключу 'date'.

    :param data: Список словарей с ключами 'id', 'state', 'date'.
    :param reverse: Порядок сортировки. По умолчанию True (убывание).
    :return: Новый список, отсортированный по ключу 'date'.
    :raises ValueError: Если формат даты некорректен.
    """
    try:
        return sorted(data, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)
    except Exception as e:
        raise ValueError(f"Invalid date format: {e}")
