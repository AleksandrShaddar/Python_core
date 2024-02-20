# Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня доступа.

from Task_6 import LevelError, AccessError, ProjectException
from Task_4 import User, load_users
import json

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


if __name__ == '__main__':
    project_1 = Project('Task_4.json')
    project_1.auth("12345656", "Alex")
    project_1.add_user("46812344", "1", "Vika")
