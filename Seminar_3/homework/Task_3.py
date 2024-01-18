# Дан список повторяющихся элементов lst. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

lst = [1, 1, 2, 2, 3, 3]

res = list()

for item in lst:
    if item not in res and lst.count(item) > 1:
        res.append(item)

print(res)
