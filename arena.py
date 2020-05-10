__doc__ = 'Simple geme - ARENA!'
__version__ = 'v0.0.0'
__author__ = 'Konstantin Tornovskiy'
__email__ = 'coolship@yandex.ru'
__date__ = '10 May 2020'

from random import randint, choices, sample

# things names list
THING_NAMES = ('Mjolnir', 'Sting', 'Trident', 'Excalibur', 'Viking shield',
               'Gungnir', 'Dainsliv', 'Gram', 'Notebook', 'Longbow',
               'Longsword', 'Katana', 'Spear', 'Mace', 'Battle Axe',
               'Scimitar', 'Gladius', 'War Hammer', 'Flail', 'Knightly Sword',
               'Haladie', 'Ranseur', 'Shuriken', 'Pike', 'Caltrops',
               'Zweihaender', 'Bardiche', 'Horesemans Pick', 'Hunga Munga',
               'Triple Dagger', 'Urumi', 'Chakram', 'Lantern Shield',
               'Sodegarami'
               )

# person names list
PERSON_NAMES = ('Thor', 'Artur', 'Bilbo', 'Aquaman', 'Iron Man', 'Flash',
                'Magneto', 'Fenrir', 'Loki', 'Fenix', 'Dedpul', 'Thanos',
                'Hawkeye', 'Halk', 'Black Widow', 'Spider-man',
                'Captain Marvel', 'Wolverine', 'Ant-man', 'Callisto'
                )


class Thing:
    def __init__(self, name, defence_rate, attack_power, health_power):
        self.name = name
        self.defence_rate = defence_rate
        self.attack_power = attack_power
        self.health_power = health_power

    def __str__(self):
        return f'{self.name}. Defence rate - {self.defence_rate}'


class Person:
    def __init__(self, name, defence_rate, attack_power, health_power):
        self.name = name
        self.defence_rate = defence_rate
        self.attack_power = attack_power
        self.health_power = health_power
        self.things = []

    def __str__(self):
        return f'{self.name}: ' \
               f'defence - {self.defence_rate}. ' \
               f'attack - {self.attack_power}. ' \
               f'health power - {self.health_power:.2f}.'

    def set_things(self, _things):
        for thing in _things:
            self.things.append(thing)
            self.defence_rate = round(thing.defence_rate +
                                      self.defence_rate, 2)
            self.attack_power += thing.attack_power
            self.health_power += thing.health_power

    def attack_damage(self, enemy_damage):
        damage = enemy_damage - self.defence_rate * enemy_damage
        self.health_power -= damage
        return f'{damage:.2f}'


class Paladin(Person):
    def __init__(self, name, defence_rate, attack_power, health_power):
        super().__init__(
            name,
            defence_rate * 2,
            attack_power,
            health_power * 2
        )


class Warrior(Person):
    def __init__(self, name, defence_rate, attack_power, health_power):
        super().__init__(
            name,
            defence_rate,
            attack_power * 2,
            health_power
        )


def main():
    things = []
    current_things = choices(THING_NAMES, k=randint(10, len(THING_NAMES)))
    for thing_name in current_things:
        defence_rate = randint(1, 10) / 100
        attack_power = randint(1, 20)
        health_power = randint(1, 10)
        things.append(Thing(thing_name,
                            defence_rate,
                            attack_power,
                            health_power
                            )
                      )
    things.sort(key=lambda thing: thing.defence_rate)

    person_list = []
    current_names = sample(PERSON_NAMES, 10)
    for person_name in current_names:
        defence_rate = randint(1, 10) / 100
        attack_power = randint(1, 20)
        health_power = randint(80, 100)
        person_index = randint(0, 1)
        if person_index == 0:
            person_list.append(Paladin(person_name,
                                       defence_rate,
                                       attack_power,
                                       health_power
                                       )
                               )
        else:
            person_list.append(Warrior(person_name,
                                       defence_rate,
                                       attack_power,
                                       health_power
                                       )
                               )
    person_list.sort(key=lambda hero: hero.health_power)
    for person in person_list:
        person_things = choices(things, k=randint(1, 4))
        person.set_things(person_things)

    fight_is_started = False
    while True:
        if fight_is_started:
            attacker = fighter_1
            print(f'{fighter_1.name} fight with {fighter_2.name}')
            while fighter_1.health_power > 0 and fighter_2.health_power > 0:
                if attacker == fighter_1:
                    damage = fighter_2.attack_damage(fighter_1.attack_power)
                    print(
                        f'{fighter_1.name} наносит удар по {fighter_2.name} на'
                        f' {damage} урона')
                    attacker = fighter_2
                else:
                    damage = fighter_1.attack_damage(fighter_2.attack_power)
                    print(
                        f'{fighter_2.name} наносит удар по {fighter_1.name} на'
                        f' {damage} урона')
                    attacker = fighter_1
            fight_is_started = False
            if fighter_1.health_power > 0:
                person_list.append(fighter_1)
                print(f'{fighter_1.name} is WIN!!!')
            else:
                person_list.append(fighter_2)
                print(f'{fighter_2.name} is WIN!!!')
        else:
            if len(person_list) > 1:
                fighter_1 = person_list[randint(0, len(person_list) - 1)]
                person_list.remove(fighter_1)
                fighter_2 = person_list[randint(0, len(person_list) - 1)]
                person_list.remove(fighter_2)
                fight_is_started = True
            else:
                print('All fight is finished!')
                print(f'{person_list[0].name} WIN!!!')
                print(person_list[0])
                break


if __name__ == '__main__':
    main()
