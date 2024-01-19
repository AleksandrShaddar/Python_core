# Функция получает на вход список чисел и два индекса. 
# Вернуть сумму чисел между между переданными индексами. 
# Если индекс выходит за пределы списка, 
# сумма считается до конца и/или начала списка. 
# Если нижняя граница меньше нуля, суммируем от начала. 
# Если верхняя граница больше длины списка, до конца.

def get_sum(numbers: list, num1: int, num2: int) -> int:
    """
    """
    res = 0
    if min(num1, num2) < 0 and max(num1, num2):
        res = sum(numbers)
    elif min(num1, num2) < 0:
        res = sum(numbers[:max(num1, num2)])
    elif max(num1, num2) > len(numbers) - 1:
        res = sum(numbers[min(num1, num2):])
    else:
        res = sum(numbers[min(num1, num2):max(num1, num2)])
    return res

numbers = [1, 4, 65, 7, 4, 3, 8, 9]

print(get_sum(numbers, 1, 3))