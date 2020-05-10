"""Provide realisation of class Warrior"""

from game.person.person import Person


class Warrior(Person):
    """Class provide functionality of Warrior class"""

    def __init__(self, name, protect, damage, hp):
        damage *= 2
        super().__init__(name, protect, damage, hp)