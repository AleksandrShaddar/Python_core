# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

class Archive:
    
    archive = []

    def __init__(self, number, string):
        self.number = number
        self.string = string

        
    def __new__(cls, *args, **kwargs):
        cls.instance = super().__new__(cls)
        cls.instance.archive.append(args)
        return cls.instance
    

ex_1 = Archive(1, 'one')
ex_2 = Archive(2, 'two')

print(ex_1.archive)
