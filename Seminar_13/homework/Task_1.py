# Добавьте в задачу Rectangle, которую писали ранее, 
# исключение NegativeValueError, которое выбрасывается при некорректных значениях
# ширины и высоты, как при создании объекта, так и при установке их через сеттеры.

class NegativeValueError(Exception):
    def __init__(self, name, value):
        self.value = value
        self.name = name

    def __str__(self):
        if self.name == '_height':
            self.name = 'Высота'
        else:
            self.name = 'Ширина'
        
        return f'{self.name} должна быть положительной, а не {self.value}'
    

class Side:
    def __init__(self, min_val: int = 1, max_val: int = 100):
        self._min_val = min_val
        self._max_val = max_val

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)

    def validate(self, value):
        if not self._min_val <= value <= self._max_val:
            raise NegativeValueError(self.name, value)


class Rectangle:
    height = Side()
    width = Side()

    def __init__(self, *args):
        self.width = args[0]
        self.height = args[1] if len(args) > 1 else self.width

    def area(self):
        return self.height * self.width

    def perim(self):
        return 2 * (self.height + self.width)

    def __add__(self, other: 'Rectangle'):
        new_perimetr = self.perim() + other.perim()
        new_height = self.height + other.height
        new_width = new_perimetr / 2 - new_height
        return Rectangle(new_height, new_width)

    def __sub__(self, other):
        new_perimetr = abs(self.perim() - other.perim())
        new_height = abs(self.height - other.height)
        new_width = new_perimetr / 2 - new_height
        if new_width < 0:
            raise ValueError('Вычитание данных прямоугольников невозможно!')
        return Rectangle(new_height, new_width)

    def __str__(self):
        return f'Rectangle({self.height=}, {self.width=})'
    
# r = Rectangle(-2) # Ширина должна быть положительной, а не -2
# r = Rectangle(5, -3) # Высота должна быть положительной, а не -3

r = Rectangle(5, 6)
r.width = -3 # Ширина должна быть положительной, а не -3

# или

class Rectangle:
    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')
        
#  и так далее