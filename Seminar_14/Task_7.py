import json
import os

class ProjectException(Exception):
    pass

class LevelError(ProjectException):
    def __init__(self, level_user, level_admin):
        self.level_user = level_user
        self.level_admin = level_admin

    def __str__(self):
        return f'Уровень пользователя ({self.level_user}) меньше чем ваш уровень ({self.level_admin})'


class AccessError(ProjectException):
    def __init__(self, user):
        self.user = user

    def __str__(self):
        return f'Пользователя {self.user} не существует'

class Project:

    def __init__(self, file_name):
        self.data = load_users(file_name)
        self.admin = None

    def auth(self, id_, name):
        user_temp = User(id_, '', name)
        if user_temp not in self.data:
            raise AccessError(user_temp)
        for user in self.data:
            if user == user_temp:
                self.admin = user

    def add_user(self, id_, level, name):
        if not self.admin:
            raise ProjectException
        if int(level) < int(self.admin.level):
            raise LevelError(level, self.admin.level)
        self.data.add(User(id_, level, name))


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


