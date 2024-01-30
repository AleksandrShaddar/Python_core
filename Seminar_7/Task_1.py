# Напишите функцию, которая заполняет файл (добавляет в конец) 
# случайными парами чисел. Первое число int, второе - float 
# разделены вертикальной чертой. 
# Минимальное число - -1000, максимальное - +1000. 
# Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform

MIN_NUMBER = -1000
MAX_NUMBER = 1000


def create_txt(numbers, strings):
    with open(numbers, 'w', encoding='utf-8') as f:
        for _ in range(strings):
            f.write(f'{randint(MIN_NUMBER, MAX_NUMBER)} | '
                    f'{uniform(MIN_NUMBER, MAX_NUMBER)}\n')

if __name__ == '__main__':
    create_txt('numbers.txt', 5)