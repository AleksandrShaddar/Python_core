# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging.

import logging


def log_decorator(func):
    def wrapper(*args, **kwargs):
        logging.basicConfig(filename=f'Task_2_{func.__name__}.log', encoding='utf-8', level=logging.DEBUG)
        logging.debug(f'Переданы аргументы: {args} {kwargs}')
        res = func(*args, **kwargs)
        logging.debug(f'Результат: {res}')
        return res
    return wrapper

@log_decorator
def division(x: int | float, y: int | float):
    try:
        res = x / y        
        return res
    except ZeroDivisionError as err:
        return float('inf')

if __name__ == '__main__':
    division(3, 0)
    division(3, 5)
    division(3, 1)