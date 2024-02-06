# Доработайте прошлую задачу добавив декоратор wraps 
# в каждый из декораторов.

from functools import wraps
import json
import os
from random import randint


def count(num: int = 1):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            counter = 0
            while counter < num:
                result = func(*args, **kwargs)
                counter += 1
            return result
        return wrapper
    return deco


def json_cache(func):

    json_file = func.__name__ + '.json'
    json_data = {}

    if json_file not in os.listdir():
        with open(json_file, 'w') as f_init:
            json.dump(json_data, f_init)
    else:         
        with open(json_file) as f:
            json_data = json.load(f)

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = f'{args=}, {kwargs=}'
        if key in json_data:
            return json_data[key]        
        res = func(*args, **kwargs)
        json_data[key] = res
        with open(json_file, 'w') as f_out:
            json.dump(json_data, f_out, indent=4)
        return res  
    return wrapper


def main(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 1 < args[0] < 100 and 1 < args[1] < 10:
            result = func(*args, **kwargs)  
        else:
            print("Переданы не верные параметры. Игра запущена с произвольными значениями") 
            result = func(randint(1, 100), randint(1, 10))
        return result
    return wrapper


@count(num=2)
@json_cache
@main
def game_with_deco_and_wraps(numbers, trying):
    numb = randint(1, numbers)
    counter = 1
    while counter <= trying:
        answer = input("Введите число: ")
        if answer == str(numb):
            print(f"Поздравляем! Вы угадали c {counter} попытки!")
            return True
        elif answer == '':
            print("Вы не ввели число!")
        elif not answer.isdigit():
            print("Вы ввели не число!")
        else:
            print(f"Неверно! Попробуй еще! Осталось {trying - counter} попыток!")
            counter += 1
    print(f"К сожалению все поппытки закончились. Вы проиграли!")
    return False

if __name__ == '__main__':
    game_with_deco_and_wraps(101, 3)
