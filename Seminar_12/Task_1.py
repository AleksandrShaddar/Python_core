# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.


class Factorial:

    def __init__(self):
        self.factorial = 1

    def __call__(self, value):
        if 0 <= value <=1:
            return self.factorial
        elif value > 1:
            for i in range(2, value + 1):
                self.factorial *= i
            return self.factorial
        return None
        
number = Factorial()
print(number(0))
print(number(1))
print(number(5))
print(number(-5))