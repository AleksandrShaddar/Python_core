# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# - от 1 до 100 для загадывания,
# - от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток. 

from random import randint

def check_try():
    numbers = int(input("До какого числа загадываем? Максимум 100. "))
    trying = int(input("Сколько попыток вам дать? "))
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
    return get_random(numbers, trying)

check_try()