# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, 
# считаем что у нас квадрат.

class Rectangle:

    def __init__(self, leight, weight=None):
        self.leight = leight
        self.weight = weight
        if self.weight == None:
            self.weight = self.leight
        else:
            self.weight = weight

    def squad(self):
        self.S = self.leight * self.weight
        return self.S

    def perim(self):
        self.P = self.leight * 2 + self.weight * 2
        return self.P
    
pr_1 = Rectangle(4, 5)
pr_2 = Rectangle(2, 3)
pr_3 = Rectangle(6)

print(pr_1.squad(), pr_1.perim())
print(pr_2.squad(), pr_2.perim())
print(pr_3.squad(), pr_3.perim())