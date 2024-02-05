# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.

import json
from random import randint


def deco(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open ('Task2.json', 'w') as f:
            json.dump(result, f)
            json.dump(args or kwargs, f)
            json.dump('\n', f)
            json.dump(kwargs, f)
        return result
    return wrapper


@deco
def get_random(numbers, trying):
        numb = randint(1, numbers)
        counter = 1
        while counter <= trying:
            answer = int(input("Введите число: "))
            if answer == numb:
                print(f"Поздравляем! Вы угадали c {counter} попытки!")
                return True
            else:
                print(f"Неверно! Попробуй еще! Осталось {trying - counter} попыток!")
                counter += 1
        print(f"К сожалению все поппытки закончились. Вы проиграли!")
        return False


get_random(numbers=10, trying=5)
