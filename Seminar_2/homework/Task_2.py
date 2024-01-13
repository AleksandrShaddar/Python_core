# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
# Для проверки своего кода используйте модуль fractions.

# На входе:

# frac1 = "1/2"
# frac2 = "1/3"
# На выходе:

# Сумма дробей: 5/6
# Произведение дробей: 1/6
# Сумма дробей: 5/6
# Произведение дробей: 1/6

import fractions

frac1 = "1/2"
frac2 = "1/3"

frac1_split = frac1.split('/')
frac2_split = frac2.split('/')

numerator_1 = int(frac1_split[0])
denominator_1 = int(frac1_split[1])
numerator_2 = int(frac2_split[0])
denominator_2 = int(frac2_split[1])

if denominator_1 != denominator_2:
    counter = min(denominator_1, denominator_2)
    while True:
        if counter % denominator_1 == 0 and counter % denominator_2 == 0:
            break
        else:
            counter +=1
    multiply_1 = counter // denominator_1
    multiply_2 = counter // denominator_2
    if denominator_1 * multiply_1 == denominator_2:
        new_numerator_1 = numerator_1 * multiply_1        
        new_frac_sum = str(new_numerator_1 + numerator_2) + '/' + str(denominator_2)
    elif denominator_2 * multiply_2 == denominator_1:
        new_numerator_2 = numerator_2 * multiply_2       
        new_frac_sum = str(new_numerator_2 + numerator_1) + '/' + str(denominator_1)
    else:
        new_numerator_1 = numerator_1 * multiply_1
        new_numerator_2 = numerator_2 * multiply_2
        new_denominator = str(counter)
        new_frac_sum = str(new_numerator_1 + new_numerator_2) + '/' + new_denominator
else:
    new_frac_sum = str(numerator_1 + numerator_2) + '/' + str(denominator_1)

new_frac_mult = str(numerator_1 * numerator_2) + '/' + str(denominator_1 * denominator_2)

print("Сумма дробей:", new_frac_sum)
print("Произведение дробей:", new_frac_mult)
print("Сумма дробей:", fractions.Fraction(numerator_1, denominator_1) + fractions.Fraction(numerator_2, denominator_2))
print("Произведение дробей:", fractions.Fraction(numerator_1, denominator_1) * fractions.Fraction(numerator_2, denominator_2))

# или 

from fractions import Fraction
#frac1 = '2/5'
#frac2 = '3/5'

# Разбиваем строки на числитель и знаменатель без использования map
numerator1_str, denominator1_str = frac1.split('/')
numerator2_str, denominator2_str = frac2.split('/')

# Преобразуем строки в целые числа
numerator1 = int(numerator1_str)
denominator1 = int(denominator1_str)
numerator2 = int(numerator2_str)
denominator2 = int(denominator2_str)

common_denominator = denominator1 * denominator2

new_numerator1 = numerator1 * denominator2
new_numerator2 = numerator2 * denominator1

summation_numerator = new_numerator1 + new_numerator2
multiplication_numerator = numerator1 * numerator2

print(f"Сумма дробей: {summation_numerator}/{common_denominator}")
print(f"Произведение дробей: {multiplication_numerator}/{common_denominator}")

# Преобразуем введенные строки в объекты Fraction
fraction1 = Fraction(frac1)
fraction2 = Fraction(frac2)

# Вычисляем сумму и произведение дробей
summation = fraction1 + fraction2
multiplication = fraction1 * fraction2

print(f"Сумма дробей: {summation}")
print(f"Произведение дробей: {multiplication}")