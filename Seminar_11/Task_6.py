# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

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

    def __eq__(self, other: 'Rectangle'): # Обязательное
        return self.area() == other.area()
    
    def __ne__(self, other: 'Rectangle'):
        return self.area() != other.area()
    
    def __gt__(self, other: 'Rectangle'): # Обязательное
        return self.area() > other.area()

    def __lt__(self, other: 'Rectangle'):
        return self.area() < other.area()

    def __ge__(self, other: 'Rectangle'): # Обязательное
        return self.area() >= other.area()

    def __le__(self, other: 'Rectangle'):
        return self.area() <= other.area()
       

pr_1 = Rectangle(4, 5)
pr_2 = Rectangle(2, 3)
pr_3 = Rectangle(6)

print(pr_1.area(), pr_1.perim())
print(pr_2.area(), pr_2.perim())
print(pr_3.area(), pr_3.perim())

print(pr_1 + pr_2)
print(pr_1 - pr_2)

print(pr_1 == pr_2)