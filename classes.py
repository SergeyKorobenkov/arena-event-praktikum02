class Thing:
    def __init__(self, name, defence_percent, attack, hp):
        self.name = name
        self.defence_percent = defence_percent
        self.attack = attack
        self.hp = hp


class Person:
    def __init__(self, name, hp, attack, defence_percent):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence_percent = defence_percent


class Paladin(Person):
    def __init__(self, name, hp, attack, defence_percent):
        super().__init__(name, hp, attack, defence_percent)
        self.hp = hp * 2
        self.defence_percent = defence_percent * 2


class Warrior(Person):
    def __init__(self, name, hp, attack, defence_percent):
        super().__init__(name, hp, attack, defence_percent)
        self.attack = attack * 2
