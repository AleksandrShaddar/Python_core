# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

# import logging

# logging.basicConfig(level=logging.DEBUG, 
#                     filename='task_1.log',
#                     # filemode='w', для перезаписи
#                     encoding='utf-8')
# logger = logging.getLogger(__name__)

# def del_nums(x, y):
#     try:
#         res = x / y
#         logger.debug(res) 
#         return res
#     except ZeroDivisionError:
#         logger.error('Деление на ноль')

# if __name__ == '__main__':
#     del_nums(10, 2)
#     del_nums(5, 0)


import logging

logging.basicConfig(filename='Task_1.log', encoding='utf-8', level=logging.NOTSET)


def division(x: int | float, y: int | float):
    try:
        res = x / y
        logging.debug(f"x / y = {res}")
        return res
    except ZeroDivisionError as err:
        logging.error(f'{err}: На ноль делить нельзя')


if __name__ == '__main__':
    division(3, 0)
    division(3, 5)
    division(3, 1)