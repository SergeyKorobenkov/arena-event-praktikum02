"""Provide realisation of class Warrior"""

from game.person.person import Person


class Warrior(Person):
    """Class provide functionality of Warrior class"""

    def __init__(self, name, hp, damage, protect):
        damage *= 2
        super().__init__(name, hp, damage, protect)