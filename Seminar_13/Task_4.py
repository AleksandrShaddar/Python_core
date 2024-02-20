# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.

import json
import os


class User:
    def __init__(self, id_: str, level: str, name: str):
        self.id, self.level, self.name = id_, level, name

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f'User({self.id}, {self.level}, {self.name})'

def load_or_create(file_name: str):
    if file_name in os.listdir():
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data

    with open(file_name, 'w') as f:
        json.dump({}, f)
    return {}


def enter_users(level: str, id: str, name: str, file_name: str) -> None:
    data = load_or_create(file_name)
    for value in data.values():
        if id in value:
            raise ValueError("id уже существует")

    data.setdefault(level, {})
    data[level].setdefault(id, name)

    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    return


def load_users(file_name):
    res = set()
    data = load_or_create(file_name)
    for level, value in data.items():
        for iden, name in value.items():
            res.add(User(iden, level, name))
    return res


# if __name__ == '__main__':
    # enter_users('3', '41234977', 'Ruslan', 'Task_4.json')
    # print(get_users('Task_4.json'))
    # user_2 = User('6', '77734147', 'Diana', 'Task_4.json')
    # print(user_2.id)
    # print(user_2.level)
    # print(user_2.name)
    