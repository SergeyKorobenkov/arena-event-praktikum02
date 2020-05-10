import random
from typing import List, Type, Sized, Tuple

from models.person import Person, Paladin, Warrior

PERSON_NAMES = ("Гранис", "Джорин", "Сеймур", "Малак", "Гевинрад", "Морлун",
                "Агамонд", "Балладор", "Манадар", "Занн", "Ариус", "Кранвельд",
                "Рогволд", "Эмундсон", "Вариан", "Утер", "Артас", "Броксигар")

PALADIN_NAMES = ("Молотобоец", "Мститель", "Правдивый", "Справедливый",
                 "Могучий", "Заступник", "Пресветлый", "Целитель",
                 "Бесстрашный", "Храбрый", " Искатель", "Бесстрашный",
                 "Пилигрим")

WARRIOR_NAMES = ("Яростный", "Кровожадный", "Ярость Бури", "Знаменосец",
                 "Берсерк", "Секира", "Трёхпалый", "Адский Крик",
                 "Кровавая Длань", "Чёрная Метка", "Неистовый", "Кровавый",
                 "Песнь Войны")

HP_VALUES = (10000, 20000)
DEF_VALUES = (10, 30)
ATTACK_VALUES = (200, 300)


CLASSES_NAMES = {Paladin: PALADIN_NAMES,
                 Warrior: WARRIOR_NAMES}

classes_names = CLASSES_NAMES.keys()


def get_random_index(items: Sized) -> int:
    return random.randint(0, len(items) - 1)


def get_person_class() -> Type[Person]:
    classes_list = list(CLASSES_NAMES.keys())
    person_class = classes_list[get_random_index(classes_list)]
    return person_class


def get_random_stat(values_range: Tuple[int, int]) -> int:
    return random.randint(*values_range)


def get_random_name(items: Tuple[str, ...]) -> str:
    random_index = get_random_index(items)
    return items[random_index]


def get_person_name(person_class: Type[Person]) -> str:
    first_name = get_random_name(PERSON_NAMES)
    last_name = get_random_name(CLASSES_NAMES[person_class])
    return f'{first_name} {last_name}'


def generate_persons(count: int = 20) -> List[Person]:
    characters = []
    for _ in range(count):
        person_class = get_person_class()
        person_name = get_person_name(person_class)
        attack = get_random_stat(ATTACK_VALUES)
        defence = get_random_stat(DEF_VALUES)
        hp = get_random_stat(HP_VALUES)
        characters.append(person_class(name=person_name, hp=hp,
                                       attack=attack, defence_percent=defence))

    return characters

