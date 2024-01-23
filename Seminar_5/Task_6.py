# Создайте функцию-генератор. 
# ✔ Функция генерирует N простых чисел, 
# начиная с числа 2. 
# ✔ Для проверки числа на простоту используйте 
# правило: «число является простым, если делится 
# нацело только на единицу и на себя».

# def generation(numbers: int) -> int:

#     for i in range(numbers):
#         for j in range(3, int(numbers**0.5) + 1):
#             # print(j)
#             if i % j == 0:
#                 continue         
#             else:
#                 yield i
                 

# numb = 24


# for _ in range(numb):
#     print(next(generation(numb)))

# def is_simple(n:int) -> bool:
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def simple_generate(number: int):
#     i = 2
#     yield i
#     i += 1
#     while i <= number:
#         if is_simple(i):
#             yield i
#         i += 2

# a = simple_generate(27)

# for _ in range(27):
#     print(next(a), end=' ')

def is_prime(num: int) -> bool:
    for div in range(3, int(num ** 0.5) + 1):
        if num % div == 0:
            return False
    return True


def primes_generator(n: int) -> int:
    if n == 2:
        yield 2
    for num in range(3, n, 2):
        if is_prime(num):
            yield num