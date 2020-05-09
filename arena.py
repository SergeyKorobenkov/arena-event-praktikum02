from random import randint, uniform

names = ['oleg', 'ivan', 'anatoly', 'zorg', 'mihail', 'angel', 'rembo', 'luiz', 'igor', 'zena',
         'varvar', 'garry', 'tommy', 'lokky', 'andrey', 'valter', 'vasya', 'john', 'jeck', 'serg'
         ]


class Person:
    def __init__(self, name, hp=1, attack_damage=0.1, protection_person=0.1):
        self.name = name
        self.hp = hp
        self.attack_damage = attack_damage
        self.protection_person = protection_person
        self.finalProtection = 0
        self.HitPoints = 0

    def setThings(self):
        self.number = randint(1, 4)
        self.things = [
            {'name': 'shoes', 'protection': 0.05,
                'attack': 0.05, 'thing_hp': 0.01},
            {'name': 'jacket', 'protection': 0.06,
             'attack': 0.06, 'thing_hp': 0.01},
            {'name': 'shield', 'protection': 0.1,
                'attack': 0.06, 'thing_hp': 0.01},
            {'name': 'gloves', 'protection': 0.05,
             'attack': 0.01, 'thing_hp': 0.01},
            {'name': 'hat', 'protection': 0.04,
             'attack': 0.01, 'thing_hp': 0.01},
            {'name': 'knife', 'protection': 0.01,
             'attack': 0.9, 'thing_hp': 0.01},
            {'name': 'bat', 'protection': 0.01,
             'attack': 0.8, 'thing_hp': 0.02},
            {'name': 'sword', 'protection': 0.02,
             'attack': 0.1, 'thing_hp': 0.02},
            {'name': 'gun', 'protection': 0.01,
             'attack': 0.1, 'thing_hp': 0.03},
            {'name': 'spear', 'protection': 0.01,
             'attack': 0.09, 'thing_hp': 0.04}
        ]
        self.list_things = []
        for i in range(self.number):
            self.list_things.append(self.things[randint(0, 9)])
            i = i + 1

        for j in self.list_things:
            self.HitPoints += self.hp + round((self.hp * j['thing_hp']), 2)
            self.attack_damage += round((self.attack_damage * j['attack']), 2)
            self.finalProtection = self.protection_person + round(
                (self.protection_person * j['protection']), 2)

    def attack(self, attack):
        self.damage = attack - attack*self.finalProtection
        self.HitPoints -= (self.damage - self.damage*self.finalProtection)


class Paladin(Person):
    def __init__(self, name, hp=1, attack_damage=0.1, protection_person=0.1):
        super().__init__(name, hp * 2, attack_damage, protection_person * 2)


class Warrior(Person):
    def __init__(self, name, hp=1, attack_damage=0.1, protection_person=0.1):
        super().__init__(name, hp, attack_damage * 2, protection_person)


def create_person():
    list_person = []
    list_pw = [Paladin, Person]
    for i in range(10):
        name = names[randint(0, len(names) - 1)]
        name = list_pw[randint(0, 1)](name, randint(
            1, 2), uniform(0.05, 0.1), uniform(0.05, 0.1))
        list_person.append(name)
        i += 1
    return list_person


def main():
    list_person = create_person()
    for person in list_person:
        person.setThings()
    while len(list_person) > 1:
        attack = list_person[randint(0, len(list_person)-1)]
        protection = list_person[randint(0, len(list_person) - 1)]
        protection.attack(attack.attack_damage)
        print(
            f'{attack.name} наносит удар по {protection.name} на {attack.attack_damage:.2f} урона')
        if protection.HitPoints <= 0:
            list_person.remove(protection)
            print(f'\nУчастник {protection.name} выбыл\n')
    print(f'Победитель {list_person[0].name}!')


if __name__ == '__main__':
    main()
