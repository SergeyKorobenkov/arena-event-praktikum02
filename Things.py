from random import randint
import operator

class Thing:
    def __init__(self, name: str):
        self.name = name
        self.def_percent = randint(1, 10)*0.01
        self.damage = randint(20, 50)
        self.hp = randint(20, 50)

    def print_thing(self):
        print(f'Название: {self.name} атака:{self.damage} защита:{self.def_percent} жизни:{self.hp}')


def forgeSomeStuff(quantity: int):
    things = []
    for i in range(1, quantity + 1):
        things.append(Thing(f'Предмет {i}'))

    things.sort(key=operator.attrgetter('def_percent'))

    return things


