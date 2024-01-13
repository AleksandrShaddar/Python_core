# Напишите программу, которая получает целое число num и 
# возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

# На входе:
# num = 255
# На выходе:
# Шестнадцатеричное представление числа: FF
# Проверка результата: 0xff

num = 16
test_num = num
num_hex = ''
dict_hex = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
while num != 0:
    if num % 16 >= 10:
        num_hex = dict_hex[num % 16] + num_hex
        num //= 16
    else:
        num_hex = str(num % 16) + num_hex
        num //= 16

print("Шестнадцатеричное представление числа:", num_hex)
print("Проверка результата:", hex(test_num))

# или

HEX = 16
hex_digits = "0123456789ABCDEF"

hex_num = ""
test_hex_num = hex(num)

while num > 0:
    remainder = num % HEX
    hex_num = hex_digits[remainder] + hex_num
    num //= HEX

print("Шестнадцатеричное представление числа:", hex_num)
print("Проверка результата:", test_hex_num)