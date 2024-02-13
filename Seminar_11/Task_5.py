# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

class Rectangle:

    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length
       
    def area(self):        
        return self.length * self.width

    def perim(self):       
        return 2 * (self.length  + self.width)

    def __add__(self, other: 'Rectangle'):
        new_perim = self.perim() + other.perim()  
        new_length = self.length + other.length  
        new_width = new_perim / 2 - new_length  
        return Rectangle(new_length, new_width)

    def __sub__(self, other: 'Rectangle'):
        new_perim = abs(self.perim() - other.perim()) 
        new_length = self.length - other.length  
        new_width = new_perim / 2 - new_length
        if new_width < 0:
            raise ValueError('Нельзя вычесть данные треугольники')  
        return Rectangle(new_length, new_width)


pr_1 = Rectangle(4, 5)
pr_2 = Rectangle(2, 3)
pr_3 = Rectangle(6)

print(pr_1.area(), pr_1.perim())
print(pr_2.area(), pr_2.perim())
print(pr_3.area(), pr_3.perim())

print(pr_1 + pr_2)
print(pr_1 - pr_2)