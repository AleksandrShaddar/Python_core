# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

class Archive:
    _instance = None
    
    def __new__(cls, text, name):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.all_text = []
            cls._instance.all_name = []
        else:
            cls._instance.all_text.append(cls._instance.text)
            cls._instance.all_name.append(cls._instance.name)
   
        return cls._instance

    def __init__(self, text: str, name: str):
        self.text = text
        self.name = name

        
    

ex_1 = Archive('1', 'one')
ex_2 = Archive('2', 'two')

print(ex_2.all_text)
