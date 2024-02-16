# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

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
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        
        
number = Factorial()
print(number(0))
print(number(1))
print(number(5))
print(number(-5))