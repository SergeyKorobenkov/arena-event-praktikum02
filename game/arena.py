"""Provide realisation of class Game
"""
from game.thing import Thing
from game.person import Warrior
from game.person import Paladin
import random
import time


class Arena:
    """Class provide functionality to game logic
    """

    def __init__(self):
        """Initialization of attributes
        """
        self._things = []
        self._participants = []

    def generate_things(self):
        """Function generate list things to fight.

        Persons will get things from this list.

        Returns:
            things (list): list of things object
        """
        names = [
            "Sword", "Armor", "Boots", "Gloves", "Ax"
        ]

        for i in range(50):
            thing = Thing(
                name=random.choice(names),
                protect=round(random.uniform(0, 1) / 10, 2),
                damage=random.randrange(0, 100),
                hp=random.randrange(0, 500)
            )
            self._things.append(thing)

    def get_participants(self):
        return self._participants

    @classmethod
    def factory_standard(cls):
        arena = cls()
        arena.generate_things()
        arena.generate_persons()
        return arena

    def generate_persons(self):
        """Function generate list of persons.

        Returns:
            things (list): list of things object
        """

        names = [
            "The Blade", "Wildstare", "Silentmight", "Shieldhammer", "The Shadow", "The Vermin",
            "The Phantom", "The Hollow", "Frost Mane", "Rockgrip", "The Nightowl", "Ember Hammer",
            "Bone Scar", "Dragon Hair", "The Tower", "The Freak", "Bearfist", "Deathcrest",
            "Hell Talon", "Lightsorrow"
        ]
        for i in range(10):
            choose = random.randrange(1)
            if choose == 0:
                person = Warrior(
                    name=random.choice(names),
                    protect=round(random.uniform(0, 1) / 10, 2),
                    damage=random.randrange(0, 100),
                    hp=random.randrange(1500, 2500)
                )
            else:
                person = Paladin(
                    name=random.choice(names),
                    protect=random.uniform(0, 1) / 10,
                    damage=random.randrange(0, 100),
                    hp=random.randrange(0, 500)
                )
            person.set_things(random.choices(self._things, k=4))
            self._participants.append(person)

    def run(self):
        while len(self._participants) > 1:
            attacker = self._participants.pop()
            defender = self._participants.pop()
            defender.reduce_hp(attacker.get_damage())
            self._participants.append(attacker)

            print(f"{attacker.name} damage {attacker.get_damage()} to {defender.name}")
            time.sleep(2)

            if defender.hp > 0:
                self._participants.append(defender)
