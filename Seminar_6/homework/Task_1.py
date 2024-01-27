# Вы работаете над разработкой программы для проверки корректности даты, 
# введенной пользователем. На вход будет подаваться дата в формате "день.месяц.год". 
# Ваша задача - создать программу, которая проверяет, 
# является ли введенная дата корректной или нет.

# Ваша программа должна предоставить ответ "True" (дата корректна) 
# или "False" (дата некорректна) в зависимости от результата проверки.


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

# или
    
def is_leap(year: int) :
    return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))

def valid(full_date: str) :
    date, month, year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1 or date > 31:
        return False
    if month in (4, 6, 9, 11) and date > 30:
        return False
    if month == 2 and is_leap(year) and date > 29:
        return False
    if month == 2 and not is_leap(year) and date > 28:
        return False
    return True