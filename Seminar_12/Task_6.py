# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.

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
            raise ValueError('Некорректное значение.')


class Rectangle:
    length = Side()
    width = Side(2, 9)

    def __init__(self, *args):
        self.length = args[0]
        self.width = args[1] if len(args) > 1 else self.length

    def area(self):
        return self.length * self.width

    def perim(self):
        return 2 * (self.length + self.width)

    def __add__(self, other: 'Rectangle'):
        new_perimetr = self.perim() + other.perim()
        new_length = self.length + other.length
        new_width = new_perimetr / 2 - new_length
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        new_perimetr = abs(self.perim() - other.perim())
        new_length = abs(self.length - other.length)
        new_width = new_perimetr / 2 - new_length
        if new_width < 0:
            raise ValueError('Вычитание данных прямоугольников невозможно!')
        return Rectangle(new_length, new_width)

    def __str__(self):
        return f'Rectangle({self.length=}, {self.width=})'


if __name__ == '__main__':
    P1 = Rectangle(4, 8)
    P2 = Rectangle(6, 11)
    # print(P1 + P2)
    # print(P1 - P2)

    print(P1.length)
    # print(P1.width)
    P1.length = 10
    print(P1.length)
