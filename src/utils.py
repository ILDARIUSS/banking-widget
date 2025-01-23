# src/utils.py
from src.logger_setup import setup_logger
import json
import os

# Настраиваем логгер для модуля
logger = setup_logger("utils")

def read_json_file(file_path):
    """
    Открывает JSON файл и возвращает данные в виде списка словарей.
    Если файл пустой или не существует, возвращает пустой список.
    """
    if not os.path.exists(file_path):
        logger.warning(f"Файл {file_path} не найден.")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info(f"Файл {file_path} успешно прочитан. Найдено {len(data)} записей.")
                return data
            else:
                logger.warning(f"Файл {file_path} не содержит список.")
                return []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка при разборе JSON файла {file_path}: {e}")
        return []
