from random import randint, uniform, choice

names = ['Рембо', 'Стрелок', 'Паша', 'Арнольд', 'Жорик', 'Михан',
         'Косой', 'Лысый', 'Муха', 'Братюня',
         'Белый', 'Жук', 'Тони', 'Боб', 'Алик',
         'Сиплый', 'Шустрый', 'Майкл', 'Малек', 'Серый'
         ]
name_thing = ['shoes', 'jacket', 'shield', 'gloves',
              'hat', 'knife', 'bat', 'sword', 'gun', 'spear']


class Thing:
    def __init__(self, name,  protection=uniform(0.05, 0.1),
                 attack=uniform(0.01, 0.1), hp=uniform(0.05, 0.1)):
        self.name = name
        self.protection = protection
        self.attack = attack
        self.hp = hp


class Person:

    def __init__(self, name, hp, attack_damage, protection_person):
        self.name = name
        self.hp = hp
        self.attack_damage = attack_damage
        self.protection_person = protection_person
        self.finalProtection = 0
        self.HitPoints = self.hp

    def setThings(self, things):
        self.things = things
        for j in self.things:
            self.HitPoints +=  (self.hp * j.hp)
            self.attack_damage += (self.attack_damage * j.attack)
            self.finalProtection = self.protection_person + j.protection

    def attack(self, attack):
        self.damage = attack - attack * self.finalProtection
        self.HitPoints -= (self.damage - self.damage*self.finalProtection)


class Paladin(Person):
    def __init__(self, name, hp, attack_damage, protection_person):
        super().__init__(name, hp, attack_damage, protection_person)
        self.protection_person *= 2
        self.hp *= 2


class Warrior(Person):
    def __init__(self, name, hp, attack_damage, protection_person):
        super().__init__(name, hp, attack_damage, protection_person)
        self.attack_damage *= 2


class Create_list():
    def __init__(self, number=10):
        self.number = number

    def create_person(self, paladin, warrior):
        self.list_person = []
        list_pw = [paladin, warrior]
        for i in range(self.number):
            name = names[randint(0, len(names) - 1)]
            player = f'player_{i}'
            player = choice(list_pw)(name, randint(
                30, 49), uniform(1.1, 10.3), uniform(0.01, 0.1))
            self.list_person.append(player)
            i += 1
        return self.list_person

    def create_things(self, Thing):
        self.things = []
        for i in range(randint(1, 4)):
            thing = f'thing_{i}'
            thing = Thing(choice(name_thing))
            self.things.append(thing)
        return(self.things)


def main():
    lists = Create_list()
    list_person = lists.create_person(Paladin, Warrior)
    list_things = lists.create_things(Thing)

    for person in list_person:
        person.setThings(list_things)

    print(f'Список участников:')
    for i in list_person:
        print(f'Участник {i.name} здоровье - {i.HitPoints:.2f}, защита - {(i.finalProtection * 100):.2f} %, атака - {i.attack_damage:.2f}') 

    while len(list_person) > 1:
        attack = list_person[randint(0, len(list_person)-1)]
        protection = list_person[randint(0, len(list_person) - 1)]
        protection.attack(attack.attack_damage)
        print(
            f'{attack.name} наносит удар по {protection.name}'
            f' на {attack.attack_damage:.2f} урона')
        if protection.HitPoints <= 0:
            list_person.remove(protection)
            print(f'\nУчастник {protection.name} выбыл\n')
    print(f'Победитель {list_person[0].name}!')


if __name__ == '__main__':
    main()
