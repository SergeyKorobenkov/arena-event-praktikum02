"""This module describe class Thing
"""


class Thing:
    """This class contain all base attributes and functionality for things in this game"""

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
