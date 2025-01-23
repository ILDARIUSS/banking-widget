import pandas as pd
from typing import List, Dict

def read_transactions_from_csv(file_path: str) -> List[Dict]:
    """
    Считывает финансовые транзакции из CSV-файла.

    :param file_path: Путь к CSV-файлу.
    :return: Список словарей с транзакциями.
    """
    try:
        data = pd.read_csv(file_path)
        transactions = data.to_dict(orient="records")
        return transactions
    except Exception as e:
        raise ValueError(f"Ошибка при чтении CSV-файла: {e}")

def read_transactions_from_excel(file_path: str) -> List[Dict]:
    """
    Считывает финансовые транзакции из Excel-файла.

    :param file_path: Путь к Excel-файлу.
    :return: Список словарей с транзакциями.
    """
    try:
        data = pd.read_excel(file_path)
        transactions = data.to_dict(orient="records")
        return transactions
    except Exception as e:
        raise ValueError(f"Ошибка при чтении Excel-файла: {e}")
