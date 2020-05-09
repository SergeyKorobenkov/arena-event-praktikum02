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
