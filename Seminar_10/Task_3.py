# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого изменения, 
# но есть возможность получить текущий возраст.

class DataPerson:

    def __init__(self, name, sername, age):
        self.name = name
        self.sername = sername
        self.__age = age

    def birthday(self):
        self.__age += 1

    def full_name(self):
        print(f"name: {self.name}\nsername: {self.sername}\nage: {self.__age}")

human_1 = DataPerson('Petr', 'Petrov', 27)
human_2 = DataPerson('Sergey', 'Serov', 30)

human_1.full_name()
human_2.full_name()

# print(human_1.__age)

human_1.__age = 29

print(human_1.__age)
human_1.full_name()
human_1.birthday()
human_1.full_name()