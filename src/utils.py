# src/utils.py
import json
import os


def read_json_file(file_path):
    """
    Открывает JSON файл и возвращает данные в виде списка словарей.
    Если файл пустой или не существует, возвращает пустой список.
    """
    if not os.path.exists(file_path):
        return []

    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
        except json.JSONDecodeError:
            return []
