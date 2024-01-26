# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из
# модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры
# вызова функции.
# Для преобразования строковых аргументов командной
# строки в числовые параметры используйте генераторное
# выражение.

from random import randint
from sys import argv


def random_numbers(numb_low: int, numb_high: int = 10, numb_try: int = 3) -> bool:
    rand_numbers = randint(numb_low, numb_high)
    counter = 0
    while counter < numb_try:
        answer = int(input("Введите число: "))
        if answer == rand_numbers:
            return True
        elif answer > rand_numbers:
            print("Загаданное число меньше!")
        elif answer < rand_numbers:
            print("Загаданное число больше!")
        counter += 1
    else:
        return False
    
if __name__ == '__main__':
    print(random_numbers(*list(map(int, argv[1:])))) 
