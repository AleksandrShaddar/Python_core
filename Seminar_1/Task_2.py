# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

MAIN_CONDITION = 4
SECOND_CONDITION = 100
THIRD_CONDITION = 400

year = int(input('Введите год: '))

if (year % MAIN_CONDITION == 0 and year % SECOND_CONDITION != 0
        or year % THIRD_CONDITION == 0):
    pass
else:
    pass

print(f'Год {year} считается високосным' if year % MAIN_CONDITION == 0 and year % SECOND_CONDITION != 0 or year % THIRD_CONDITION == 0 else f'Год {year} не является високосным')
