# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.

from random import randint

def main(func):
    def wrapper(*args, **kwargs):
        if 1 < args[0] < 100 and 1 < args[1] < 10:
            result = func(*args, **kwargs)  
        else:
            print("Переданы не верные параметры. Игра запущена с произвольными значениями") 
            result = func(randint(1, 100), randint(1, 10))
        return result
    return wrapper

@main
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

get_random(50, 10)