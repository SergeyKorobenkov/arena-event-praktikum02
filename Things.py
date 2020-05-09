from random import randint

class Thing:
    def __init__(self, name: str):
        self.name = name
        self.def_percent = randint(1, 10) * 0.01
        self.damage = randint(1, 50)
        self.hp = randint(1, 100)
        print(f'{name} with dp = {self.def_percent} damage = {self.damage} and hp = {self.hp}' +
              ' was created')


def forgeSomeStuff(quantity: int):
    things = []
    for i in range(1, quantity + 1):
        things.append(Thing(f'Хрень {i}'))
    return things


if __name__ == '__main__':
    forgeSomeStuff(10)

