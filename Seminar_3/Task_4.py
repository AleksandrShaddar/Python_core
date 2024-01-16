# Создайте вручную список с повторяющимися элементами. 
# Удалите из него все элементы, которые встречаются дважды.

list_1 = [1, 2, 3, 2, 5, 7, 1, 7, 8, 1, 3, 7, 9]

for item in set(list_1):
    if list_1.count(item) > 1:
        for _ in range(list_1.count(item)):
            list_1.remove(item)

print(list_1)