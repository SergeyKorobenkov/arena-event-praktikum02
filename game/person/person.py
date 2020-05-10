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
    name = NameValid()
    protect = ProtectValid()
    damage = DamageValid()
    hp = HpValid()

    def __init__(self, name, protect, damage, hp):
        """Class constructor

        Args:
            name (str): name of person
            hp (int): base hit points of person
            damage: base damage of person
            protect: base protect of person
        """

        self.name = name
        self.protect = protect
        self.damage = damage
        self.hp = hp
        self._things = []

    def set_things(self, things):
        """Adding list of things to current person

        Args:
            things (list<Thing>): list of Thing objects
        """
        self._things = things

    def get_things(self):
        """Getting list of things from current person

        Returns:
            things (list<Thing>): list of Thing objects
        """
        return self._things

    def get_damage(self):
        thing_damage = 0.0
        for thing in self.get_things():
            thing_damage += thing.damage
        return self.damage + thing_damage

    def reduce_hp(self, attack_damage):
        thing_protection = 0.0
        for thing in self.get_things():
            thing_protection += thing.protect
        self.hp -= int(attack_damage - attack_damage * ((self.protect+thing_protection)*100))

    def __repr__(self):
        return f"{self.name}({self.__class__.__name__}), protect: {self.protect}, damage: {self.damage}, hit points: {self.hp}"
