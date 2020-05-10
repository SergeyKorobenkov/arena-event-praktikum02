import random

from characters import Paladin, Warrior
from equipment import Equipment


def create_names_from_file(filename):
    '''
    The function parses names from file and returns list of names.

    Parametrs:
        filename (str): name of file containing names.

    Returns:
        names (list): list of names.
    '''

    with open(filename) as file:
        names = [line.rstrip() for line in file]

    return names


def create_different_equipments():
    '''
    The function creates Equipment objects with random attributes
    and returns list of this objects.

    Returns:
        equipments (list): list of Equipment objects.
    '''

    equipments = []
    names = create_names_from_file('equipments_names.txt')

    for _ in range(45):
        name = random.choice(names)
        protection = random.randint(1, 100) / 1000
        attack = random.randint(1, 10)
        hp = random.randint(1, 100)

        equipments.append(Equipment(
            name=name,
            protection=protection,
            attack=attack,
            hp=hp,
        ))

    return equipments


def create_different_characters():
    '''
    The function creates Paladin or Warrior objects with random attributes
    and returns list of this objects.

    Returns:
        characters (list): list of Paladin or Warrior objects.
    '''

    characters = []
    names = create_names_from_file('characters_names.txt')

    for _ in range(10):
        character_class = random.choice([Paladin, Warrior])
        name = random.choice(names)
        hp = random.randint(1, 100)
        attack = random.randint(1, 20)
        protection = random.randint(1, 250) / 1000

        characters.append(character_class(
            name=name,
            base_hp=hp,
            base_attack=attack,
            base_protection=protection
        ))

    return characters


def make_equipment_set(equipments):
    '''
    The function make set of random Equipment objects
    in an amount from 1 to 4.

    Parametrs:
        equipments (list): list of Equipment objects.

    Returns:
        equipment_set (list): list of Equipment objects.
    '''

    equipment_set = []

    for _ in range(random.randint(1, 4)):
        equipment_set.append(random.choice(equipments))

    return equipment_set


def equip_characters(characters, equipments):
    '''
    The function equips evere character in list with unique equipment set.

    Parametrs:
        characters (list): list of Paladin or Warrior objects.
        equipments (list): list of Equipment objects.
    '''

    for character in characters:
        equipment_set = make_equipment_set(equipments)
        character.set_equipments(equipment_set)
