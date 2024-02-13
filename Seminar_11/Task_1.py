# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)

import time


class MyString(str):
    
    def __new__(cls, text):
        instance = super().__new__(cls, text)
        instance.time = time.time()
        # instance.author = 
        print(f'Создал класс {cls}')
        return instance



text_1 = MyString('Hello')
text_2 = MyString('World')

print(text_1 + text_2)
print(text_1.time)
    