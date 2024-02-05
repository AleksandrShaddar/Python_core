# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой функции.


def count(num: int = 1):
    def deco(func):
        def wrapper(*args, **kwargs):
            counter = 0
            while counter < num:
                result = func(*args, **kwargs)
                counter += 1
            return result
        return wrapper
    return deco


@count(5)
def str_conc(text_1, text_2):
    mmessage = text_1 + ' ' + text_2
    print(mmessage)


str_conc('Day', 'Night')