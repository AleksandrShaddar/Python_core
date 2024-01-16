# Вручную создайте список с целыми числами, которые повторяются. 
# Получите новый список, который содержит уникальные (без повтора) 
# элементы исходного списка. 
# *Подготовьте два решения, короткое и длинное, которое не использует 
# другие коллекции помимо списков

list_1 = [1, 3, 4, 5, 5, 6, 7, 8, 8, 9]
list_3 = list_1.copy()

list_2 = list(set(list_1))
print(list_2)

for item in list_3:
    if list_3.count(item) > 1:
        list_3.remove(item)


list_4 = []

for item in list_1:
    if item not in list_4:
        list_4.append(item)

print(list_1)
print(list_3)
print(list_4)