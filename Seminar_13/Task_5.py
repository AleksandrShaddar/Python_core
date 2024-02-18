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

from Task_3 import UserError, AccessError 
import json

class Project:

    def get_users():
        users = set()
        with open('Task_4.json', 'r') as f:
            data = json.load(f)
            for value in data.values():
                for iden in value.values():
                    users.add(iden)
        return users
    
    def __eq__(self, name):
        if name in self.get_users():
            with open ('Task_4.json', 'r') as f:
                data = json.load(f)
                for value in data.values():
                    for iden, user in value.items():
                        if name == user:
                            return iden
        else:
            raise UserError()
    