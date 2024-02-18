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
    def __init__(self, level, id, name, file_name):
        self.level = level
        self.id = id
        self.name = name
        self.load_or_create(file_name)

    def load_or_create(self, file_name: str):
        if file_name in os.listdir():
            with open(file_name, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return self.save_to_file(data, file_name)
        with open(file_name, 'w') as f:
            json.dump({}, f)
        data = {}
        return self.save_to_file(data, file_name)

    def save_to_file(self, data, file_name):
        for value in data.values():
            if id in value:
                raise ValueError("id уже существует")

        data.setdefault(self.level, {})
        data[self.level].setdefault(self.id, self.name)

        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return

def get_users(file_name):
    users = set()
    with open(file_name, 'r') as f:
        data = json.load(f)
        for value in data.values():
            for iden in value.values():
                users.add(iden)
    return users


if __name__ == '__main__':
    # enter_users('3', '41234977', 'Ruslan', 'Task_4.json')
    # print(get_users('Task_4.json'))
    # user_2 = User('6', '77734147', 'Diana', 'Task_4.json')
    # print(user_2.id)
    # print(user_2.level)
    # print(user_2.name)
    