#  Создайте модуль и напишите в нём функцию, которая
# получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать
# или ложь, если такая дата невозможна.
#  Для простоты договоримся, что год может быть в диапазоне
# [1, 9999].
#  Весь период (1 января 1 года - 31 декабря 9999 года) 
# действует Григорианский календарь.
#  Проверку года на високосность вынести в отдельную
# защищённую функцию.

import datetime

MONTH = {
    1: range(1, 32),
    2: range(1, 29),
    3: range(1, 32),
    4: range(1, 31),
    5: range(1, 32),
    6: range(1, 31),
    7: range(1, 32),
    8: range(1, 32),
    9: range(1, 31),
    10: range(1, 32),
    11: range(1, 31),
    12: range(1, 32),
    }


def parse_data(date: str) -> bool:
    d, m, y = map(int, date.split('.'))
    return date_valid(d, m, y) and valid_month(m) and valid_year(y)


def date_valid(d, m, y) -> bool:
    if leap_year(y) and m ==2:
        return d in range(1, 30)
    if valid_month(m):
        return d in MONTH[m]
    else:
        return False


def valid_year(year: int) -> bool:
    return year in range (1, 10_000)


def valid_month(month) -> bool:
    return month in range (1, 13)  


def leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0
        or year % 400 == 0)


if __name__ == '__main__':
    print(parse_data('29.2.2021'))
    