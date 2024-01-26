#  Добавьте в модуль с загадками функцию, которая
# принимает на вход строку (текст загадки) и число (номер
# попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах
# отгадывания.
# Для хранения используйте защищённый словарь уровня
# модуля.
#  Отдельно напишите функцию, которая выводит результаты
# угадывания из защищённого словаря в удобном для чтения
# виде.
#  Для формирования результатов используйте генераторное
# выражение.

results = dict()


def game(text: str, answers: list, numb_try: int) -> int:
    print(text)
    for i in range(1, numb_try + 1):
        answer = input("Введите ответ: ")
        if answer in answers:
            get_result(text, i)
            return i
    get_result(text, 0)
    return 0


def test_storage():
    dict_1 = {'Зимой и летом одним цветом': ['ель', 'ёлка', 'сосна'],
        'Не лает, не кусает, в дом не пускает': ['замок'],
        'Сидит дед во сто шуб одет': ['лук', 'луковица'],
        }
    for test_data in dict_1.items():
        print(game(*test_data, 3))


def get_result(text: str, counter = int):
    global results
    results[text] = counter


def print_results(res: dict):
    global results
    for k,v in res.items():
        print(f'{k} - {v}')

if __name__ == '__main__':
    test_storage()
    print_results(results)