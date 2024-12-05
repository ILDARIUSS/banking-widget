from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета.

    :param data: строка вида "Visa Platinum 7000792289606361" или "Счет 73654108430135874305"
    :return: строка с замаскированным номером
    """
    if data.lower().startswith("счет"):
        # Обработка счета
        account_number = data.split(maxsplit=1)[1]
        return f"Счет {get_mask_account(account_number)}"
    else:
        # Обработка карты
        card_type, card_number = data.rsplit(maxsplit=1)
        return f"{card_type} {get_mask_card_number(card_number)}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата "2024-03-11T02:26:18.671407" в формат "ДД.ММ.ГГГГ".

    :param date_str: строка с датой в ISO формате
    :return: строка с датой в формате "ДД.ММ.ГГГГ"
    """

    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")
