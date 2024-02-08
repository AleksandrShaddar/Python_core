# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.


class Bird:
    def __init__(self, name, region, color):
        self.name = name
        self.region = region
        self.color = color    

    def specific(self):
        print(f'{self.color=}')


class Fish:
    def __init__(self, name, region, water):
        self.name = name
        self.region = region
        self.water = water

    def specific(self):
        print(f'{self.water=}')


class Snake:
    def __init__(self, name, region, leight):
        self.name = name
        self.region = region
        self.leight = leight

    def specific(self):
        print(f'{self.leight=}')

parrot = Bird('Chirik', 'Africa', 'green')
luna = Fish('Luna', 'Thailand', 'ocean')
cobra = Snake('Cobra', 'India', 90)

print(parrot.name)
print(luna.region)
print(cobra.leight)

parrot.specific()
luna.specific()
cobra.specific()
