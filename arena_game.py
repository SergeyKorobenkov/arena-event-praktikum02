"""Модуль содержит классы для мини-игры "Арена"."""

import random as rnd


class Things:
    """
    Класс описывает объекты вещей персонажа.

    Класс содержит в себе следующие параметры -
    название, процент защиты, атаку и жизнь.
    """

    def __init__(self, name, defence_pct, attack_pct, hitpoints):
        pass


class Person:
    """
    Класс описывает базового персонажа.

    Класс, содержащий в себе следующие параметры:
    Имя, кол-во hp/жизней, базовую атаку, базовый процент защиты.
    Параметры передаются через конструктор.
    """

    def __init__(self, name, base_defence_pct, base_attack_pct, hitpoints):
        pass


class Paladin(Person):
    """
    Класс описывает персонажа 'Паладин'.

    Класс наследуется от персонажа, при этом количество присвоенных жизней
    и процент защиты умножается на 2 в конструкторе.
    """

    def __init__(self, name, base_defence_pct, base_attack_pct, hitpoints,
                 def_factor=2):
        super().__init__(name, base_defence_pct, base_attack_pct, hitpoints)
        pass


class Warrior(Person):
    """
    Класс описывает персонажа 'Воин'.

    Класс наследуется от персонажа, при этом атака умножается на 2
    в конструкторе.
    """

    def __init__(self, name, base_defence_pct, base_attack_pct, hitpoints,
                 att_factor=2):
        super().__init__(name, base_defence_pct, base_attack_pct, hitpoints)
        pass
