# Добавьте в модуль с загадками функцию, которая хранит
# словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы
# передать ей все свои загадки.

def game(text: str, answers: list, numb_try: int) -> int:
    print(text)
    for i in range(1, numb_try + 1):
        answer = input("Введите ответ: ")
        if answer in answers:
            return i
    return 0


def test_storage():
    dict_1 = {'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
        'Не лает, не кусает, в дом не пускает': ['замок'],
        'Сидит дед во сто шуб одет': ['лук', 'луковица'],
        }
    for test_data in dict_1.items():
        print(game(*test_data, 3))

test_storage()