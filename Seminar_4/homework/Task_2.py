# Напишите функцию key_params, принимающую на вход только ключевые параметры
# и возвращающую словарь, где ключ - значение переданного аргумента, 
# а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

# Пример использования.
# На входе:

from typing import Hashable

def key_params(**kwargs):
    reverse_dict = {}
    for key, value in kwargs.items():
        if isinstance(value, Hashable) and value != None:
            reverse_dict[value] = key
        else:
            reverse_dict[str(value)] = key
    return reverse_dict

params = key_params(a=None, b='hello', c=[1, 2, 3], d={})

# На выходе:

# {1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}

print(params)

# или

def key_params(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if isinstance(value, (int, str, float, bool, tuple)):
            result[value] = key
        else:
            result[str(value)] = key
    return result