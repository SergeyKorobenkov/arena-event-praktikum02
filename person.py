from thing import Thing


class Person:
    """Герой."""
    def __init__(self, name, hp, attack, protection):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.protection = protection

    def setThings(self, things: list):
        for thing in things:
            self.hp += thing.life
            self.attack += thing.attack
            if self.protection + thing.protection < 100:
                self.protection += thing.protection

    def finalProtection(self):
        return self.protection / 100

    def received_damage(self, attack_damage):
        self.hp -= attack_damage

    def attack_damage(self):
        return self.attack - self.attack * self.finalProtection()


class Paladin(Person):
    """Паладин."""
    def __init__(self, name, hp, attack, protection):
        super().__init__(name, hp * 2, attack, protection * 2)
        if self.protection > 99:
            self.protection = 99


class Warrior(Person):
    """Воин."""
    def __init__(self, name, hp, attack, protection):
        super().__init__(name, hp, attack * 2, protection)
