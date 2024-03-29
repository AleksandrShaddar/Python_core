# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить. В
# этом случае берётся первый в месяце день недели, текущий
# день недели и/или текущий месяц.
# *Научите функцию распознавать не только текстовое
# названия дня недели и месяца, но и числовые,
# т.е не мая, а 5.

import argparse
from Task_4 import string_to_date

def cl_parser():
    parser = argparse.ArgumentParser(description='String to date')
    parser.add_argument('-w', '--weeks', default='1')
    parser.add_argument('-wd', '--weeksdays', default='понедельник')
    parser.add_argument('-m', '--month', default='января')

    args = parser.parse_args()
    weekdays = args.weekdays if not args.weekdays.isdigit() else DAYS[int(args.weekdays) - 1]
    months = args.months if not args.months.isdigit() else MONTHS[int(args.months) - 1]
    
    return string_to_date(f'{args.weeks} {weekdays} {months}')
    
if __name__ == '__main__':
    string_to_date('1-й четверг ноября')
    string_to_date('1-е воскресенье февраля')
    string_to_date('5-й четверг февраля')
    string_to_date('5-е воскресенье марта')
    string_to_date('5-е воскресенье марта')
    string_to_date('5-е пятница мая') 

    print(cl_parser())

    # python .\Task_5.py -w '2' -wd 'вторник' -m 'марта' # Запуск в консоли