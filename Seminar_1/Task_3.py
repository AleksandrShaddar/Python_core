# Пользователь вводит число от 1 до 999.
# Используя операции с числами сообщите что введено:
# цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

import time

while True:
    number = int(input('Введите чило: '))
    current_time = time.time()
    if not 1 <= number < 1000:
        continue
    if number < 10:
        res = number**2
    elif number < 100:
        res = (number // 10) * (number % 10)
    else:
        res = (number % 10 * 100) + (number // 10 % 10 * 10) + number // 100
    break

time.sleep(0.1)
end_time = time.time()

print(res)

print("Время выполения :", end_time - current_time)


# Через строки


while True:
    number_2 = input('Введите чило: ')
    current_time = time.time()
    if not 1 <= int(number_2) < 1000:
        continue
    if len(number_2) == 1:
        res = int(number_2)**2
    elif len(number_2) == 2:
        res = int(number_2[0]) * int(number_2[1])
    else:
        res = number_2[::-1]
    break

time.sleep(0.1)
end_time = time.time()

print(res)

print("Время выполения :", end_time - current_time)
