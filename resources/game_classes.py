from decimal import Decimal


class Item():

    def __init__(self, name, defence=0, damage=0, hp=0):
        self.name = name
        self.defence = Decimal(defence)
        self.damage = Decimal(damage)
        self.hp = Decimal(hp)

    def __str__(self):
        return f'{self.name} dmg {self.damage} def {self.defence} hp {self.hp}'


class Person():

    def __init__(self, name, hp, damage=0, defence=0):
        self.name = name
        self.hp = Decimal(hp)
        self.damage = Decimal(damage)
        self.defence = Decimal(defence)

        self.base_hp = self.hp
        self.base_damage = self.damage
        self.base_defence = self.defence

        self.inventory = []

    def set_inventory(self, things):
        self.inventory.clear()

        self.defence = self.base_defence
        self.damage = self.base_damage
        self.hp = self.base_hp

        self.inventory.extend(things)
        self.inventory.sort(key=lambda item: item.defence)
        for item in self.inventory:
            self.defence += item.defence
            self.damage += item.damage
            self.hp += item.hp

    def restore_hp(self):
        self.hp = self.base_hp

    def attack(self, victim):
        damage = round(self.damage - self.damage*victim.defence/100, 2)
        print(
            f'            {self.name}(hp {self.hp}) наносит удар по {victim.name}(hp {victim.hp}) на {damage} урона')
        return victim.take_damage(damage)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f'\n        {self.name} мертв')
            return True
        return False


class Paladin(Person):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hp *= 2
        self.base_hp = self.hp

    def __str__(self):
        return f'Паладин {self.name} hp {self.hp} dmg {self.damage} def {self.defence}'


class Warrior(Person):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.damage *= 2

    def __str__(self):
        return f'Воин {self.name} hp {self.hp} dmg {self.damage} def {self.defence}'
