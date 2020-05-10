"""
Персонажи и одежда.
"""

from .settings import ArenaSet


class Person:
    """
    Персонаж. Имя, количество жизней (hp), базовая атака,
    базовый процент защиты.
    :param name: Имя персонажа.
    """

    def __init__(self, *, name: str):
        self.name = name
        self.life = ArenaSet.BASE_LIFE
        self.attack = ArenaSet.BASE_ATTACK
        self.armor = ArenaSet.BASE_ARMOR
        self.things_titles = list()

    def set_things(self, things: list) -> None:
        """
        Принимает список вещей персонажа.
        :param things: Список вещей персонажа.
        """
        for thing in things:
            self.things_titles.append(thing.title)
            if not self.things_titles:
                self.things_titles = ['голые методики']
            self.life += thing.life
            self.attack += thing.attack
            self.armor += thing.armor
            if self.armor > 0.99:
                self.armor = 0.99

    def set_life_count(self, attack: float) -> None:
        """
        Корректирует количество жизней персонажа на основе
        полученных данных.
        :param attack: Уменьшает количество жизней персонажа
        на размер переданного значения.
        """
        self.life = self.life - (attack - attack * self.armor)

    def __str__(self):
        string = f'Имя: {self.name}.\n'\
                 f'Броня: {round(self.armor, 2)} и жизни: {self.life}.\n'\
                 f'Сила атаки: {round(self.attack, 2)}.\n'\
                 f'Мои вещи: {", ".join(self.things_titles)}.'
        return string


class Paladin(Person):
    """
    Палладин. Наследник класса Person.
    Количество жизней и защита удваиваются.
    """
    def __init__(self, *, name: str):
        super().__init__(name=name)
        self.life *= 2
        self.armor *= 2


class Warrior(Person):
    """
    Воин. Наследник класса Person.
    Значение аттаки удваивается.
    """
    def __init__(self, *, name: str):
        super().__init__(name=name)
        self.attack *= 2


class Thing:
    """
    Одежда: название, процент защиты, атака и жизнь.
    """

    title = None
    armor = None
    attack = None
    life = None

    def __init__(self, *, title: str, life: float,
                 attack: float, armor: float):
        self.title = title
        self.life = life
        self.attack = attack
        self.armor = armor

    def __str__(self):
        return f'{self.title}'
