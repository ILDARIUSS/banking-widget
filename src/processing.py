from typing import List, Dict


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список словарей по указанному состоянию.

    :param data: Список словарей с ключами 'id', 'state', 'date'.
    :param state: Состояние, по которому фильтруются данные. По умолчанию 'EXECUTED'.
    :return: Новый список, содержащий только словари с указанным состоянием.
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по ключу 'date'.

    :param data: Список словарей с ключами 'id', 'state', 'date'.
    :param reverse: Порядок сортировки. По умолчанию True (убывание).
    :return: Новый список, отсортированный по ключу 'date'.
    """
    return sorted(data, key=lambda x: x["date"], reverse=reverse)
