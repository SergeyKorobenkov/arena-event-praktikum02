"""Модуль содержит классы для мини-игры "Арена"."""

import random as rnd


class Things:
    """
    Класс описывает объекты вещей персонажа.

    Класс содержит в себе следующие параметры -
    название, процент защиты, атаку и жизнь.
    """

    THING_DEF_MAX = 0.1  # максимальный процент защиты для одной вещи.

    def __init__(self, name, defence_pct, attack_damage, hitpoints):
        self.name = name
        self.hitpoints = hitpoints
        self.attack_damage = attack_damage
        # макс.процент защиты для одной вещи не должен превышать THING_DEF_MAX
        if defence_pct > self.THING_DEF_MAX:
            self.defence_pct = self.THING_DEF_MAX
        else:
            self.defence_pct = defence_pct

class Person:
    """
    Класс описывает базового персонажа.

    Класс, содержащий в себе следующие параметры:
    Имя, кол-во hp/жизней, базовую атаку, базовый процент защиты.
    Параметры передаются через конструктор.
    """
    # Согласно ТЗ, финальная защита складывается из базовой защиты и вещей
    # персонажа, при этом вещей может быть не более 4-х, а процент защиты
    # у одной вещи не более 0.1. Исходя из того, что стопроцентная защита
    # соответствует неуязвивому персонажу, а значит, не должна достигаться,
    # начальный процент защиты любого персонажа не должен превышать
    # 1 - (4 * 0.1) = 0.6. Т.к. существует персонаж с двойной защитой
    # относительно базового, то следует, что процент защиты рядового персонажа
    # не должен превышать 0.3
    BASE_DEFENCE_MAX = 0.29  # максимальная базовая защита рядового персонажа

    def __init__(self, name, base_defence_pct, base_attack_damage, hitpoints):
        self.name = name
        self.hitpoints = hitpoints
        self.things = []
        self.attack_damage = base_attack_damage
        # начальный процент защиты не должен превышать BASE_DEFENCE_MAX
        if base_defence_pct > self.BASE_DEFENCE_MAX:
            self.defence_pct = self.BASE_DEFENCE_MAX
        else:
            self.defence_pct = base_defence_pct

    def setThings(self, things):
        """
        Метод устанавливает список вещей персонажа.

        Метод заполняет атрибут things[] обекта класса Person, располагая при
        этом вещи в порядке возрастания значения Things.defence_pct.
        :param things: спсок из объектов класса Things.
        :return:
        """
        self.things = sorted(things, key=lambda things: things.defence_pct)

    def getDressed(self):
        """
        Метод 'одевает' персонаж, используя вещи из списка things[].

        Метод рассчитывает финальные значения hitpoints, атаки
        и процента защиты персонажа с учетом вещей из списка things[].
        :return:
        """

        for thing in self.things:
            self.defence_pct += thing.defence_pct
            self.attack_damage += thing.attack_damage
            self.hitpoints += thing.hitpoints

    def letsFight(self, attacker):
        """
        Метод для определения последствий атаки.

        Метод вычисляет количество получаемого урона после атаки.
        :param attacker: атакующий, объект класса Person или его
                         классов-наследников.
        :return: строка, содержащая количество урона в hitpoints.
        """

        damage = attacker.attack_damage - \
                 attacker.attack_damage * self.defence_pct
        self.hitpoints -= damage
        return (f"{attacker.name} наносит удар по {self.name} "
                f"на {damage} урона")


class Paladin(Person):
    """
    Класс описывает персонажа 'Паладин'.

    Класс наследуется от персонажа, при этом количество присвоенных жизней
    и процент защиты умножается на def_factor=2 в конструкторе.
    """

    def __init__(self, name, base_defence_pct, base_attack_damage, hitpoints,
                 def_factor=2):
        super().__init__(name, base_defence_pct, base_attack_damage, hitpoints)
        self.defence_pct = self.defence_pct * def_factor


class Warrior(Person):
    """
    Класс описывает персонажа 'Воин'.

    Класс наследуется от персонажа, при этом атака умножается на att_factor=2
    в конструкторе.
    """

    def __init__(self, name, base_defence_pct, base_attack_damage, hitpoints,
                 att_factor=2):
        super().__init__(name, base_defence_pct, base_attack_damage, hitpoints)
        self.attack_damage = self.attack_damage * att_factor
