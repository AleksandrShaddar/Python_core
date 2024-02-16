# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.

class Factorial:

    def __init__(self, stop, start=1, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.result = 1
        if self.start > self.stop:
            self.start, self.stop = self.stop, self.start
    
    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.stop:
            self.result *= self.start
            self.start += 1
            return self.result
        raise StopIteration

fact = Factorial(1, 5, 4)
for res in fact:
    print(res)
