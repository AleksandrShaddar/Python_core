# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, 
# считаем что у нас квадрат.

class Rectangle:

    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length

        # if self.width == None:
        #     self.width = self.length
        # else:
        #     self.width = width

    def area(self):        
        return self.length * self.width

    def perim(self):       
        return 2 * (self.length  + self.width)


pr_1 = Rectangle(4, 5)
pr_2 = Rectangle(2, 3)
pr_3 = Rectangle(6)

print(pr_1.area(), pr_1.perim())
print(pr_2.area(), pr_2.perim())
print(pr_3.area(), pr_3.perim())