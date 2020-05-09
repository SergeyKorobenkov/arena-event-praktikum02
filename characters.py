class Person():
    def __init__(self, name, base_hp, base_attack, base_protection):
        self.name = name
        self.base_hp = base_hp
        self.base_attack = base_attack
        self.base_protection = base_protection

    def set_equipments(self, equipments):
        self.equipments = equipments

        for equipment in self.equipments:
            self.hp = self.base_hp + equipment.hp
            self.attack = self.base_attack + equipment.attack
            self.protection = self.base_protection + equipment.protection

    def make_attack(self, victim):
        victim.reduction_hp(self.attack)

    def reduction_hp(self, incoming_attack):
        damage = incoming_attack * (1 - self.protection)
        self.hp -= damage


class Paladin(Person):
    def __init__(self, name, base_hp, base_attack, base_protection):
        super().__init__(name, base_hp, base_attack, base_protection)
        self.base_hp = base_hp
        self.set_base_protection()

    def set_base_protection(self):
        self.base_protection *= 2

        if self.base_protection > 0.5:
            self.base_protection = 0.5

