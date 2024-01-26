# Cоздайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и
# верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число
# попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки
# исчерпаны - ложь.

from random import randint

def random_numbers(numb_low: int, numb_high: int, numb_try: int) -> bool:
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
    print(random_numbers(1, 4, 3))
        
        