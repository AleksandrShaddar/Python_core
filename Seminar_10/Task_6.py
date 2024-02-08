# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

class Animal:
    def __init__(self, name, region):
        self.name = name
        self.region = region


class Bird(Animal):
    def __init__(self, color, *args):        
        self.color = color   
        super().__init__(*args) 

    def specific(self):
        print(f'{self.color=}')


class Fish(Animal):
    def __init__(self, water, *args):        
        self.water = water  
        super().__init__(*args) 

    def specific(self):
        print(f'{self.water=}')


class Snake(Animal):
    def __init__(self, leight, *args):        
        self.leight = leight   
        super().__init__(*args) 

    def specific(self):
        print(f'{self.leight=}')


parrot = Bird('green', 'Chirik', 'Africa')
luna = Fish('ocean', 'Luna', 'Thailand')
cobra = Snake(90, 'Cobra', 'India')

print(parrot.name)
print(luna.region)
print(cobra.leight)

parrot.specific()
luna.specific()
cobra.specific()
