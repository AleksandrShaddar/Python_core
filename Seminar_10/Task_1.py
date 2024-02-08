# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.


class Bowl:
    pi = 3.14

    def __init__(self, radius, ):
        self.radius = radius

    def leight(self):
        self.C = 2 * self.pi * self.radius
        return self.C

    def squad(self):
        self.S = (self.pi * self.radius * self.radius) / 2
        return self.S

ex_1 = Bowl(5)
ex_2 = Bowl(2)
ex_3 = Bowl(10)


print(ex_1.leight(), ex_1.squad())
print(ex_2.leight(), ex_2.squad())
print(ex_3.leight(), ex_3.squad())




