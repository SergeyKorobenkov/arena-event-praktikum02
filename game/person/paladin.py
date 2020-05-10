"""Provide realisation of class Paladin"""

from game.person.person import Person


class Paladin(Person):
    """Class provide functionality of Paladin class"""

    def __init__(self, name, hp, damage, protect):
        protect *= 2
        hp *= 2
        super().__init__(name, hp, damage, protect)