import random

from characters import Paladin, Warrior
from equipment import Equipment


def create_different_equipment():
    equipments = []

    for _ in range(10):
        name = random.choice(['dsfsd', 'dsfsf', 'sdfsdf', 'dsfsdf', 'sdfdsf'])
        protection = random.randint(1, 100) / 1000
        attack = random.randint(1, 100)
        hp = random.randint(1, 100)

        equipments.append(Equipment(
            name=name,
            protection=protection,
            attack=attack,
            hp=hp,
        ))

    return equipments


def create_different_characters():
    characters = []

    for _ in range(10):
        character_class = random.choice([Paladin, Warrior])
        name = random.choice(['вася', 'петя', 'Ира', 'лола', 'маша'])
        hp = random.randint(1, 100)
        attack = random.randint(1, 100)
        protection = random.randint(1, 100) / 1000

        characters.append(character_class(
            name=name,
            base_hp=hp,
            base_attack=attack,
            base_protection=protection
        ))

    return characters


def make_equipment_set(equipments):
    equipment_set = []

    for _ in range(random.randint(1, 4)):
        equipment_set.append(random.choice(equipments))

    return equipment_set


