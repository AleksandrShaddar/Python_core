# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.

from datetime import datetime, date
import logging

# MONTHS = {
#     "января": 1,
#     "февраля": 2,
#     "марта": 3,
#     "апреля": 4,
#     "мая": 5,
#     "июня": 6,
#     "июля": 7,
#     "августа": 8,
#     "сентября": 9,
#     "октября": 10,
#     "ноября": 11,
#     "декабря": 12
# }

# WEEKDAYS = {
#     "понедельник": 1,
#     "вторник": 2,
#     "среда": 3,
#     "четверг": 4,
#     "пятница": 5,
#     "суббота": 6,
#     "воскресенье": 7
# }

MONTHS = ["января", "февраля", "марта", "апреля", "мая", "июня",
          "июля", "августа", "сентября", "октября", "ноября", "декабря"]
DAYS = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]

FORMAT = '{levelname:<8} - {asctime}. В функции {msg}'
logging.basicConfig(format=FORMAT, filename='Task_4.log', encoding='utf-8', style='{', level=logging.NOTSET)

def log_decorator(func):
    logger = logging.getLogger(__name__)   
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        logger.debug(f'{func.__name__} {args} {kwargs} {res}')
        # logger.debug(f'{args} {kwargs} {res}')
        return res
    return wrapper

@log_decorator
def string_to_date(text: str) -> datetime:
    weeks, weekday, month = text.split()

    weeks = int(weeks[0])
    y = datetime.now().year
    month_num = MONTHS.index(month) + 1
    weekday = DAYS.index(weekday) + 1
    # first_day = datetime(day=1, month=month_num, year=y).weekday() # 0-6
    first_day = date(day=1, month=month_num, year=y).isoweekday() # 1-7
    day_by_date = ((1 + 7 * weeks - (first_day - weekday))
                    if weekday < first_day else 1 + 7 * (weeks - 1) - (first_day - weekday))
    
    return datetime(day=day_by_date, month=month_num, year=y)

if __name__ == '__main__':
    string_to_date('1-й четверг ноября')
    string_to_date('1-я суббота декабря')
    string_to_date('1-й понедельник мая')


# def string_to_date(s: str) -> datetime:
#     weeks, weekday, month = s.split()

#     weeks = int(weeks[0])
#     y = datetime.now().year
#     month_num = MONTHS.index(month) + 1
#     weekday = DAYS.index(weekday) + 1
#     first_day = date(day=1, month=month_num, year=y).isoweekday()  # 1-7

#     day_by_date = ((1 + 7 * weeks - (first_day - weekday))
#                    if weekday < first_day else 1 + 7 * (weeks - 1) - (first_day - weekday))
          
#     return datetime(day=day_by_date, month=month_num, year=y)


# if __name__ == '__main__':
#     string_to_date('1-й четверг ноября')
#     string_to_date('1-е воскресенье февраля')
#     string_to_date('5-й четверг февраля')
#     string_to_date('5-е воскресенье марта')
#     string_to_date('5-е воскресенье марта')
#     string_to_date('5-е пятница мая')    