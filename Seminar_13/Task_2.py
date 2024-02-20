# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

def get_analog(my_dict, key, default_value = None):
    try:
        return my_dict[key]
    except KeyError:
        print(f"Ключа {key} не найдено")
        return default_value

dict_1 = {'one': 1,
          'two': 2,
          'three': 3,
          }

print(get_analog(dict_1, 'one', 999))
print(get_analog(dict_1, 'four', 999))
print(get_analog(dict_1, 'three'))
