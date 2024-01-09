# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if. Попробуйте разные значения e и n.

n, e = int(input('Введите n: ')), int(input('Введите e: '))
list_1 = [i for i in range(2, n + 1, 2)]
print(list_1)
print(sum(list(filter(lambda x: x % e != 0, list_1))))
