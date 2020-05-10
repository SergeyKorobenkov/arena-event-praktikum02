from random import randint

# Из греческой мифологии
names = ['Геракл',
         'Ахилл',
         'Персей',
         'Одиссей',
         'Орфей',
         'Тесей',
         'Ясон',
         'Гиперион',
         'Иапет',
         'Кей',
         'Криос',
         'Кронос',
         'Океан',
         'Агрий',
         'Алкионей',
         'Гратион',
         'Ипполит',
         'Клитий',
         'Мимант',
         'Паллант',
         ]


class Person:
    def __init__(self,
                 name: str,
                 hp: int,
                 base_attack: int,
                 base_def: int):
        self.name = name
        self.hp = hp
        self.base_attack = base_attack
        self.base_def = base_def / 100.
        self.is_a_life = True

    def getDamage(self, Person):
        damage = round(Person.base_attack - Person.base_attack * self.base_def, 2)
        self.hp -= damage
        print(f'{Person.name} наносит удар по {self.name} на {damage} урона')

        if self.hp <= 0:
            self.is_a_life = False
            print(f'{self.name} пал смертью храбрых')
        else:
            print(f'У {self.name} осталость {round(self.hp, 2)}  жизней')

    # Одеть персонажа
    def setThings(self, things):
        for thing in things:
            self.hp += thing.hp
            self.base_attack += thing.damage
            self.base_def += self.base_def * thing.def_percent
        if (self.base_def > 1):
            self.base_def = 0.99


class Paladin(Person):
    def __init__(self,
                 name,
                 hp,
                 base_attack,
                 base_def):
        super().__init__(name, hp * 2, base_attack, base_def * 2)
        if self.base_def > 100:
            self.base_def = 100

    def getStat(self):
        return f'паладин {self.name} c hp:{round(self.hp, 2)} атакой:{self.base_attack} защитой:{round(self.base_def, 2)}'


class Warrior(Person):
    def __init__(self,
                 name,
                 hp,
                 base_attack,
                 base_def):
        super().__init__(name, hp, base_attack * 2, base_def)

    def getStat(self):
        return f'воин {self.name} c hp:{round(self.hp, 2)} атакой:{self.base_attack} защитой:{round(self.base_def, 2)}'


def create_persons():
    persons = []
    for i in range(1, 11):
        base_hp = randint(50, 100)
        base_attack = randint(20, 50)
        base_def = randint(20, 40)
        if (randint(0, 1) & 1):
            persons.append(Paladin(get_name(), base_hp, base_attack, base_def))
        else:
            persons.append(Warrior(get_name(), base_hp, base_attack, base_def))
    return persons


def get_name() -> str:
    return names.pop(randint(1, len(names) - 1))
