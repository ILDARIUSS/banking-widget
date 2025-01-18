# src/utils.py
import json
import os

def read_transactions_from_json(file_path: str):
    """
    Читает данные о транзакциях из указанного JSON-файла.

    :param file_path: Путь до JSON-файла.
    :return: Список словарей с данными о транзакциях или пустой список, если файл не найден
             или содержит некорректные данные.
    """
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (json.JSONDecodeError, FileNotFoundError):
        return []
