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
    _name = NameValid()
    _protect = ProtectThingValid()
    _damage = DamageValid()
    _hp = HpValid()

    def __init__(self, name, protect, damage, hp):
        """Initialize class attributes

        Args:
            name (str): name of person
            protect (float): how many protect as percent add thing to person
            damage (int): how many damage add thing to person
            hp (int): how many hit point add thing to person
        """

        self._name = name
        self._protect = protect
        self._damage = damage
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def protect(self):
        return self._protect

    @property
    def damage(self):
        return self._damage

    @property
    def hp(self):
        return self._hp
