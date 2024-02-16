# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.

class Rectangle:
    __slots__ = ('_length', '_width')

    def __init__(self, length, width=None):
        self._length = length
        self._width = width if width else length
       
    def area(self):        
        return self._length * self._width

    def perim(self):       
        return 2 * (self._length  + self._width)

    def __add__(self, other: 'Rectangle'):
        new_perim = self.perim() + other.perim()  
        new_length = self._length + other._length  
        new_width = new_perim / 2 - new_length  
        return Rectangle(new_length, new_width)

    def __sub__(self, other: 'Rectangle'):
        new_perim = abs(self.perim() - other.perim()) 
        new_length = self._length - other._length  
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

    @property   
    def length(self):        
        return self._length

    @property   
    def width(self):        
        return self._width
    
    @width.setter
    def width(self, width):
        if width > 0:
            self._width = width                      
            return self._width
        else:
            raise ValueError('Ширина не может быть отрицательной')

    @length.setter
    def length(self, length):
        if length > 0:
            self._length = length                       
            return self._length
        else:
            raise ValueError('Длина не может быть отрицательной')

pr_1 = Rectangle(4, 5)
print(pr_1.__slots__)
