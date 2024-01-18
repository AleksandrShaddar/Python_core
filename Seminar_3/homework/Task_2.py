# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов.

# Слова разделяются пробелами. Такие слова как 
# don t, it s, didn t итд (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.

# Отсортируйте по убыванию значения количества повторяющихся слов.

# Пример

# На входе:

text = 'Hello world. Hello Python. Hello again.'

# На выходе:
# [('hello', 3), ('world', 1), ('python', 1), ('again', 1)]

data = text.lower()
negativ_symbols = {'.', ',', '!', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', "'"}
res = list()

for symbol in negativ_symbols:    
    if symbol in data:
       data = data.replace(symbol, ' ')

for word in data.split():
    if (word, data.split().count(word)) not in res:
        res.append((word, data.split().count(word)))


print(sorted(res, key=lambda x: x[1], reverse=True))
