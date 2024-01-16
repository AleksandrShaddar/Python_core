# Создайте вручную кортеж содержащий элементы разных типов. 
# Получите из него словарь списков, где ключ - тип элемента, 
# а значение - список элементов данного типа.

elements = (1, 1.2, 'qwerty', 'hello', 4, 5.2)

dict_1 = dict()

for elem in elements:
    dict_1.setdefault(type(elem), [])
    dict_1[type(elem)].append(elem)

print(dict_1)