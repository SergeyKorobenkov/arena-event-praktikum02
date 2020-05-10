"""Provide realisation of abstract class Person"""

from abc import ABC
from game.descriptors import (
    NameValid,
    ProtectValid,
    DamageValid,
    HpValid
)


class Person(ABC):
    """Provide base functionality to other classes of person
    """
    _name = NameValid()
    _protect = ProtectValid()
    _damage = DamageValid()
    _hp = HpValid()

    def __init__(self, name, hp, damage, protect):
        """Class constructor

        Args:
            name (str): name of person
            hp (int): base hit points of person
            damage: base damage of person
            protect: base protect of person
        """

        self._name = name
        self._hp = hp
        self._damage = damage
        self._protect = protect

    def set_things(self):
        pass

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
