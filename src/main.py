from src.file_utils import load_transactions
from src.transaction_utils import (
    filter_transactions_by_keyword,
    count_transactions_by_category,
)
from src.processing import filter_by_state, sort_by_date


def main():
    print("Добро пожаловать в систему обработки транзакций!\n")

    # Загрузка транзакций
    file_path = input("Введите путь к JSON-файлу с транзакциями: ").strip()
    transactions = load_transactions(file_path, "json")
    if not transactions:
        print("Ошибка: данные не загружены. Проверьте путь к файлу.")
        return

    while True:
        print("\nДоступные действия:")
        print("1. Отфильтровать транзакции по статусу")
        print("2. Найти транзакции по ключевому слову в описании")
        print("3. Подсчитать количество транзакций по категориям")
        print("4. Вывести все транзакции, отсортированные по дате")
        print("0. Выйти из программы")

        choice = input("Введите номер действия: ").strip()

        if choice == "1":
            status = input("Введите статус для фильтрации (например, EXECUTED или CANCELED): ").strip()
            filtered = filter_by_state(transactions, status)
            if filtered:
                print("Отфильтрованные транзакции:")
                for t in filtered:
                    print(t)
            else:
                print("Нет транзакций с указанным статусом.")
        elif choice == "2":
            keyword = input("Введите ключевое слово для поиска в описании: ").strip()
            result = filter_transactions_by_keyword(transactions, keyword)
            if result:
                print("Найденные транзакции:")
                for t in result:
                    print(t)
            else:
                print("Транзакции с таким описанием не найдены.")
        elif choice == "3":
            categories = input("Введите категории через запятую (например, 'вклад, ЖКХ, перевод'): ").strip().split(",")
            counts = count_transactions_by_category(transactions, categories)
            print("Количество транзакций по категориям:")
            for category, count in counts.items():
                print(f"{category}: {count}")
        elif choice == "4":
            sorted_transactions = sort_by_date(transactions)
            print("Транзакции, отсортированные по дате:")
            for t in sorted_transactions:
                print(t)
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из списка.")


if __name__ == "__main__":
    main()
