# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.

from math import pi

class Сircle:
   
    def __init__(self, radius, ):
        self.radius = radius

    def length(self):
        return 2 * pi * self.radius

    def area(self):        
        return pi * self.radius ** 2

ex_1 = Сircle(5)
ex_2 = Сircle(4)
ex_3 = Сircle(10)


print(ex_1.length(), ex_1.area())
print(ex_2.length(), ex_2.area())
print(ex_3.length(), ex_3.area())
