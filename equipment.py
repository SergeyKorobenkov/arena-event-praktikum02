class Equipment():
    def __init__(self, name, protection, attack, hp):
        self.name = name
        self.protection = protection
        self.attack = attack
        self.hp = hp


class Headdress(Equipment):
    def __init__(self, name, protection, attack, hp):
        super().__init__(name, protection, attack, hp)


class Armor(Equipment):
    pass


class Legs(Equipment):
    pass


class Weapon(Equipment):
    pass
