import pytest
from src.decorators import log


# Тестируем успешное выполнение функции
@log()
def add(a, b):
    return a + b


# Тестируем вызов функции с исключением
@log()
def divide(a, b):
    return a / b


def test_log_to_console(capsys):
    # Проверяем логирование в консоль при успешном выполнении
    result = add(2, 3)
    assert result == 5
    captured = capsys.readouterr()
    assert "Calling function add with args: (2, 3)" in captured.out
    assert "Function add completed successfully. Result: 5" in captured.out

    # Проверяем логирование в консоль при ошибке
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
    captured = capsys.readouterr()
    assert "Function divide raised an error: ZeroDivisionError" in captured.out
    assert "Inputs: (1, 0)" in captured.out


def test_log_to_file(tmp_path):
    # Создаем временный файл для логов
    log_file = tmp_path / "test_log.txt"

    # Декоратор с указанием имени файла
    @log(filename=str(log_file))
    def multiply(a, b):
        return a * b

    # Вызываем функцию
    result = multiply(4, 5)
    assert result == 20

    # Проверяем содержимое лог-файла
    with open(log_file, "r") as f:
        logs = f.read()
        assert "Calling function multiply with args: (4, 5)" in logs
        assert "Function multiply completed successfully. Result: 20" in logs
