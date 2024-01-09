# Пользователь вводит число от 1 до 999. Используя операции с числами сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print


while True:
    number = int(input('Введите чило: '))
    if not 1 <= number < 1000:
        continue
    if number < 10:
        res = number**2
    elif number < 100:
        res = (number // 10) * (number % 10)
    else:
        res = (number % 10 * 100) + (number // 10 % 10 * 10) + number // 100
    break

print(res)

