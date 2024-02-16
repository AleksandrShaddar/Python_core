# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.


class Factorial:

    def __init__(self, k):
        self.k = k
        self.factorial = 1        
        self.dict_num = {}

    def __call__(self, value):
        if 0 <= value <=1:            
            return self.factorial
        elif value > 1:
            for i in range(2, value + 1):
                self.factorial *= i                
                self.dict_num[i] = self.factorial
            return self.factorial
        return None

    def __str__(self):
        return f'{self.dict_num}'
        
number = Factorial(3)
# print(number(0))
# print(number(1))
print(number(5))
# print(number(-5))
print(number)