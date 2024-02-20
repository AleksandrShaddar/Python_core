# В организации есть два типа людей: сотрудники и обычные люди. 
# Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:

# Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая) 
# Возраст (целое положительное число) Сотрудники имеют также уникальный идентификационный номер (ID), 
# который должен быть шестизначным положительным целым числом.

# Ваша задача:

# Создать класс Person, который будет иметь атрибуты и методы для управления данными о 
# людях (Фамилия, Имя, Отчество, Возраст). Класс должен проверять валидность входных данных 
# и генерировать исключения InvalidNameError и InvalidAgeError, если данные неверные.

# Создать класс Employee, который будет наследовать класс Person и добавлять уникальный 
# идентификационный номер (ID). Класс Employee также должен проверять валидность ID и 
# генерировать исключение InvalidIdError, если ID неверный.

# Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.

# Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника 
# на основе суммы цифр в его ID (по остатку от деления на 7).

# Создать несколько объектов класса Person и Employee с разными данными и проверить, 
# что исключения работают корректно при передаче неверных данных.

class UserError(Exception):
    pass

class InvalidNameError(UserError):
    pass

class InvalidAgeError(UserError):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f'Invalid age: {self.age}. Age should be a positive integer.'

class InvalidIdError(UserError):
    def __init__(self, id_):
        self.id_ = id_

    def __str__(self):
        return f'Invalid id: {self.id_}. Id should be a 6-digit positive integer between 100000 and 999999.'


class Person:
    def __init__(self, second_name, name, sername, age):
        self.second_name = second_name
        self.name = name
        self.sername = sername
        if not isinstance(age, int) or age < 0:
           raise InvalidAgeError(age) 
        else:
            self.__age = age

    def get_age(self):
        return self.__age

    def birthday(self):
        self.__age += 1

    def full_name(self):
        print(f"name: {self.name}\nsername: {self.sername}\nage: {self.__age}")

class Employee(Person):
    def __init__(self, second_name, name, sername, age, id_num):
        if len(str(id_num)) == 6 and 100000 <= id_num <= 999999:
           self.id_num = id_num                
        else:
           raise InvalidIdError(id_num) 
        super().__init__(second_name, name, sername, age)
        self.level = sum(map(int, id_num)) % 7

    def get_level(self):
        self.lvl = 0
        for self.i in self.id_num:
            self.lvl += int(self.i)
        return self.lvl // 7

# Director = Employee('534534', 'Andrey', 'General', 54)
# print(Director.id_num)
# print(Director.level)

# person = Person("Alice", "Smith", "Johnson", -5)
# employee = Employee("Bob", "Johnson", "Brown", 40, 12345)  # Invalid id: 12345. Id should be a 6-digit positive integer between 100000 and 999999. 


person = Person("Alice", "Smith", "Johnson", 25)
print(person.get_age())
# person = Person("", "John", "Doe", 30)
# print(person)


# или 

class Person:
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        if not isinstance(last_name, str) or len(last_name.strip()) == 0:
            raise InvalidNameError(last_name)
        if not isinstance(first_name, str) or len(first_name.strip()) == 0:
            raise InvalidNameError(first_name)
        if not isinstance(patronymic, str) or len(patronymic.strip()) == 0:
            raise InvalidNameError(patronymic)
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(age)