from src.processing import filter_by_state, sort_by_date
from src.file_utils import load_transactions
from src.transaction_utils import filter_transactions_by_keyword

data = [
    {"id": 1, "state": "EXECUTED", "date": "2024-01-01T00:00:00"},
    {"id": 2, "state": "CANCELED", "date": "2024-01-02T00:00:00"},
]

# Существующий функционал
print("Filtered data:", filter_by_state(data))
print("Sorted data:", sort_by_date(data))

# Новый функционал: загрузка транзакций из файла
file_path = input("Введите путь к JSON-файлу с транзакциями: ")
transactions = load_transactions(file_path, "json")

if transactions:
    # Пример фильтрации по ключевому слову
    keyword = input("Введите ключевое слово для фильтрации по описанию: ").strip()
    filtered_transactions = filter_transactions_by_keyword(transactions, keyword)

    print("Транзакции, отфильтрованные по ключевому слову:")
    for transaction in filtered_transactions:
        print(transaction)
else:
    print("Не удалось загрузить транзакции. Проверьте путь к файлу.")
