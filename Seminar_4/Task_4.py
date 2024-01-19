# Функция получает на вход список чисел. 
# Отсортируйте его элементы in place без 
# использования встроенных в язык сортировок. 
# Как вариант напишите сортировку пузырьком. 
# Её описание есть в википедии.

def bubble_sort(numbers: list) -> None:
    """
    """
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


numbers = [1, 90, 34, 2, 768, 32, 0, 10]
print(numbers)
bubble_sort(numbers)
print(numbers)