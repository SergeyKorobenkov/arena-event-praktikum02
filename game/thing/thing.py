"""This module describe class Thing
"""

from game.descriptors import (
    NameValid,
    DamageValid,
    HpValid,
    ProtectThingValid
)


class Thing:
    """This class contain all base attributes and functionality for things in this game"""
    name = NameValid()
    protect = ProtectThingValid()
    damage = DamageValid()
    hp = HpValid()

    def __init__(self, name, protect, damage, hp):
        """Initialize class attributes

        Args:
            name (str): name of person
            protect (float): how many protect as percent add thing to person
            damage (int): how many damage add thing to person
            hp (int): how many hit point add thing to person
        """

        self.name = name
        self.protect = protect
        self.damage = damage
        self.hp = hp

    def __repr__(self):
        return f"{self.name}: protect: {self.protect}, damage: {self.damage}, hit points: {self.hp}"