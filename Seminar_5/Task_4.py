# Напишите программу, которая выводит 
# на экран числа от 1 до 100. 
# ✔ При этом вместо чисел, кратных трем, 
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz». 
# ✔ Если число кратно и 3, и 5, то программа 
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

list_1 = iter(i if i % 15 != 0 else 'FizzBuzz' if i % 3 != 0 else 'Fizz' if i % 5 != 0 else 'Buzz' for i in range(1, 100) ) 

for _  in range(1, 100):
    print(next(list_1))

print(*['FizzBuzz' if i % 15 == 0 
        else 'Fizz' if i % 3 == 0 
        else 'Buzz' if i % 5 == 0 
        else i for i in range(101)], sep='\n')
        