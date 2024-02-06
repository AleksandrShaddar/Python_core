# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.

from random import randint

def main(func):
    def wrapper(*args, **kwargs):
        if 1 <= args[0] <= 100 and 1 <= args[1] <= 10:
            result = func(*args, **kwargs)  
        else:
            print("Переданы не верные параметры. Игра запущена с произвольными значениями") 
            result = func(randint(1, 100), randint(1, 10))
        return result
    return wrapper


@main
def game(numbers, trying):
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
    game(50, 10)

# Из семинара:

# from random import randint


# def game(func):

#     def wrapper(number_secret, count):
#         if not 1 <= number_secret <= 100:
#             number_secret = randint(1, 100)
#         if not 1 <= count <= 10:
#             count = randint(1, 10)
#         return func(number_secret, count)
#     print('Enter game()')
#     return wrapper


# @game
# def run(number_secret: int, count: int):
#     for _ in range(count):
#         answer = int(input('Угадайте число: '))
#         if number_secret == answer:
#             return True
#     return False


# if __name__ == '__main__':
#     run(7, 15)