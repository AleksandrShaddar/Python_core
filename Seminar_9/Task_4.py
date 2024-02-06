# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой функции.


def count(num: int = 1):
    def deco(func):
        def wrapper(*args, **kwargs):            
            for _ in range(num):
                result = func(*args, **kwargs)                
            return result
        return wrapper
    return deco


@count(5)
def str_conc(text_1, text_2):
    mmessage = text_1 + ' ' + text_2
    print(mmessage)

if __name__ == '__main__':
    str_conc('Day', 'Night')
