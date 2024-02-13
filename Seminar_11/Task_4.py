# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.



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

    def __str__(self):
        return f'Перед нами экземпляр класса Archive с атрибутами ({self.text},{self.name})'
    
    def __repr__(self):        
        return f'Archive({self.text}, {self.name})'

ex_1 = Archive('Hello', 'Alex')

print(ex_1)
print(repr(ex_1))