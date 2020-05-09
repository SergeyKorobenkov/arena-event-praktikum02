"""Модуль содержит классы для мини-игры "Арена"."""

import random as rnd


class Things:
    """
    Класс описывает объекты вещей персонажа.

    Класс содержит в себе следующие параметры -
    название, процент защиты, атаку и жизнь.
    """

    def __init__(self, name, defence_pct, attack_pct, hitpoints):
        self.name = name
        self.defence_pct = defence_pct
        self.attack_pct = attack_pct
        self.hitpoints = hitpoints


class Person:
    """
    Класс описывает базового персонажа.

    Класс, содержащий в себе следующие параметры:
    Имя, кол-во hp/жизней, базовую атаку, базовый процент защиты.
    Параметры передаются через конструктор.
    """

    def __init__(self, name, base_defence_pct, base_attack_pct, hitpoints):
        self.name = name
        self.defence_pct = base_defence_pct
        self.attack_pct = base_attack_pct
        self.hitpoints = hitpoints
        self.things = []

    def setThings(self, things):
        """
        Метод устанавливает список вещей персонажа.

        Метод заполняет атрибут things[] обекта класса Person, располагая при
        этом вещи в порядке возрастания значения Things.defence_pct.
        :param things: спсок из объектов класса Things.
        :return:
        """
        self.things = sorted(things, key=lambda things: things.defence_pct)


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
