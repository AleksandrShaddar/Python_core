# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# - шестизначный идентификационный номер
# - уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

class DataPerson:
    def __init__(self, name, sername, age):
        self.name = name
        self.sername = sername
        self.__age = age

    def birthday(self):
        self.__age += 1

    def full_name(self):
        print(f"name: {self.name}\nsername: {self.sername}\nage: {self.__age}")

class Employee(DataPerson):
    def __init__(self, id_num, *args, **kwargs):
        self.id_num = id_num        
        super().__init__(*args, **kwargs)
        self.level = sum(map(int, id_num)) % 7

    # def level(self):
    #     self.lvl = 0
    #     for self.i in self.id_num:
    #         self.lvl += int(self.i)
    #     return self.lvl // 7

Director = Employee('534534', 'Andrey', 'General', 54)

print(Director.id_num)
print(Director.level)