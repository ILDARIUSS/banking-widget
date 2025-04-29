# src/masks.py
from src.logger_setup import setup_logger

# Настраиваем логгер для модуля
logger = setup_logger("masks")


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты.
    Логирует успешное выполнение или ошибки.
    :param card_number: Строка с номером карты.
    :return: Маскированный номер карты.
    """
    try:
        if len(card_number) < 16:
            raise ValueError("Номер карты должен содержать минимум 16 символов.")

        masked_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        logger.info(f"Маскировка номера карты выполнена успешно. Маскированный номер: {masked_card}")
        return masked_card
    except Exception as e:
        logger.error(f"Ошибка при маскировке номера карты: {e}")
        raise


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета.
    Логирует успешное выполнение или ошибки.
    :param account_number: Строка с номером счета.
    :return: Маскированный номер счета.
    """
    try:
        if len(account_number) < 4:
            raise ValueError("Номер счета должен содержать минимум 4 символа.")

        masked_account = f"**{account_number[-4:]}"
        logger.info(f"Маскировка номера счета выполнена успешно. Маскированный номер: {masked_account}")
        return masked_account
    except Exception as e:
        logger.error(f"Ошибка при маскировке номера счета: {e}")
        raise
