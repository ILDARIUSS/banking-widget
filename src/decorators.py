import functools
import logging
from datetime import datetime


def log(filename: str = None):
    """
    Декоратор для логирования выполнения функций.

    :param filename: Если указан, лог записывается в файл, иначе в консоль.
    """
    # Настройка логирования
    logger = logging.getLogger("function_logger")
    logger.setLevel(logging.INFO)

    # Установка обработчика (файл или консоль)
    if filename:
        handler = logging.FileHandler(filename)
    else:
        handler = logging.StreamHandler()

    formatter = logging.Formatter("%(asctime)s - %(message)s")
    handler.setFormatter(formatter)
    logger.handlers = [handler]

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            try:
                # Логирование начала выполнения
                logger.info(f"Calling function {func.__name__} with args: {args}, kwargs: {kwargs}")
                result = func(*args, **kwargs)
                # Логирование успешного завершения
                logger.info(f"Function {func.__name__} completed successfully. Result: {result}")
                return result
            except Exception as e:
                # Логирование ошибок
                logger.error(
                    f"Function {func.__name__} raised an error: {type(e).__name__}. "
                    f"Inputs: {args}, {kwargs}. Message: {str(e)}"
                )
                raise
            finally:
                end_time = datetime.now()
                duration = (end_time - start_time).total_seconds()
                logger.info(f"Execution time of {func.__name__}: {duration:.2f} seconds")

        return wrapper

    return decorator
