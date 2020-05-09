
names = []

class Person:
    def __init__(self,
                 hp,
                 base_attack,
                 base_def_percent):
        self.hp = hp
        self.base_attack = base_attack
        self.base_def_percent = base_def_percent

    def getDamage(self, damage):
        pass

    def setThings(self, things):
        pass

class Paladin(Person):
    def __init__(self,
                 hp,
                 base_attack,
                 base_def_percent):
        super().__init__(hp*2, base_attack, base_def_percent*2)
        if self.hp > 100:
            self.hp = 100


class Warrior(Person):
    def __init__(self,
                 hp,
                 base_attack,
                 base_def_percent):
        super().__init__(hp, base_attack*2, base_def_percent)

