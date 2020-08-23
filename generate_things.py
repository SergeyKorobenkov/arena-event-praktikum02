from random import randint

from generate_persons import get_random_index, get_random_stat
from models.person import Person
from models.thing import Thing

THING_TITLES = ('Шлем', 'Кираса', 'Сапог', 'Оружие')

HP_VALUES = (100, 1000)
DEF_VALUES = (1, 10)
ATTACK_VALUES = (30, 300)
CRITICAL_CHANCE = (1, 5)


def generate_thing() -> Thing:
    thing_name = THING_TITLES[get_random_index(THING_TITLES)]
    hp = get_random_stat(HP_VALUES)
    defence = get_random_stat(DEF_VALUES)
    attack = get_random_stat(ATTACK_VALUES)
    critical_chance = get_random_stat(CRITICAL_CHANCE)
    return Thing(name=thing_name, life=hp, defence=defence,
                 attack=attack, critical_chance=critical_chance)


def dress_things(person: Person):
    dressed_things = person.things
    for _ in range(randint(1, 4)):
        thing = generate_thing()
        if thing.name not in [thing.name for thing in dressed_things]:
            person.dress_thing(thing)

