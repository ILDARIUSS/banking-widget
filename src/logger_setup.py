# src/logger_setup.py
import logging
import os

# Убедимся, что папка logs существует
LOGS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
os.makedirs(LOGS_DIR, exist_ok=True)


def setup_logger(module_name):
    """
    Настраивает логгер для указанного модуля.

    :param module_name: Имя модуля, для которого создается логгер.
    :return: Логгер с заданными настройками.
    """
    # Создаем логгер с именем модуля
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.DEBUG)

    # Создаем обработчик для записи логов в файл
    log_file_path = os.path.join(LOGS_DIR, f"{module_name}.log")
    file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)

    # Задаем формат логов
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(formatter)

    # Добавляем обработчик к логгеру
    logger.addHandler(file_handler)

    return logger
