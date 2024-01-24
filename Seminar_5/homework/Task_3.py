# Создайте функцию генератор чисел Фибоначчи fibonacci.

def fibonacci():
    numb_1 = -1
    numb_2 = 0    
    while True:
        if numb_1 + numb_2 < 1:
            numb_1 += 1
            yield numb_1
        elif numb_1 + numb_2 == 1:
            numb_2 += 1
            yield numb_2
        else:
            number = numb_1 + numb_2
            numb_1 = numb_2
            numb_2 = number
            yield number

f = fibonacci()
for i in range(10):  
    print(next(f))

# или 
    
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
