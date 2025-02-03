import json
import csv

def load_transactions(file_path, file_type):
    """
    Загружает транзакции из указанного файла.

    :param file_path: путь к файлу.
    :param file_type: тип файла ('json', 'csv', 'xlsx').
    :return: список транзакций (словарей).
    """
    try:
        if file_type == "json":
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        elif file_type == "csv":
            transactions = []
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    transactions.append(row)
            return transactions
        else:
            print(f"Формат файлов '{file_type}' пока не поддерживается.")
            return []
    except FileNotFoundError:
        print("Файл не найден.")
        return []
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")
        return []
