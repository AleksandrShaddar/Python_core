# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)

from datetime import datetime


class MyString(str):
    
    def __new__(cls, text, author=None):
        instance = super().__new__(cls, text)
        instance.time = datetime.now()
        instance.author = author
        return instance


text_1 = MyString('Hello', 'Petr')
text_2 = MyString('World', 'Ivan')

print(text_1 + ' ' + text_2)
print(text_1.time)
print(text_1.author)
    