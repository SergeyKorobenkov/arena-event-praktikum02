from __future__ import annotations
import random
from typing import List, Optional, Tuple

from models.thing import Thing


class Person:
    def __init__(self, name: str, hp: int,
                 attack: int, defence_percent: int,
                 critical_chance: Optional[int] = None):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence_percent = defence_percent
        self.critical_chance = self.default_critical_chance(critical_chance)
        self.things: List[Thing] = []

    def __str__(self):
        return self.name

    @staticmethod
    def default_critical_chance(critical_chance: Optional[int]) -> int:
        if critical_chance is None or critical_chance < 5:
            return 5
        return critical_chance

    def dress_thing(self, thing: Thing):
        self.hp += thing.life
        self.attack += thing.attack
        self.defence_percent += thing.defence
        self.critical_chance += thing.critical_chance
        self.things.append(thing)

    def undress_thing(self, thing: Thing):
        self.hp -= thing.life
        self.attack -= thing.attack
        self.defence_percent -= thing.defence
        self.critical_chance -= thing.critical_chance
        self.things.append(thing)

    def set_things(self, things: List[Thing]):
        # Для соответсвия ТЗ, использовать буду dress_thing
        for thing in things:
            self.dress_thing(thing)

    def take_damage(self, attack: int) -> int:
        damage = round(attack - attack * 1 / self.defence_percent)
        self.hp -= damage
        return damage

    def deal_damage(self) -> Tuple[int, bool]:
        critical = False
        if self.is_dead:
            return 0, critical
        damage = self.attack
        chance = random.randint(0, 100)
        if chance < self.critical_chance:
            critical = True
            damage = round(damage * 1.5)
        return damage, critical

    @property
    def is_dead(self) -> bool:
        return self.hp <= 0

    def get_enemies(self, persons: Optional[List[Person]]) -> List[Person]:
        if persons:
            return [p for p in persons if p is not self]
        return []

    def extended_info(self) -> dict:
        things = [thing.info for thing in self.things]
        data = {
            f'{self.my_class_name} {self.name}': {
                'Здоровье': self.hp,
                'Атака': self.attack,
                'Защита': f'{self.defence_percent}%',
                'Критический шанс': f'{self.critical_chance}%',
                'Инвентарь': things
            }
        }
        return data

    @property
    def my_class_name(self):
        return 'Обыватель'


class Paladin(Person):
    def __init__(self, name: str, hp: int,
                 attack: int, defence_percent: int,
                 critical_chance: Optional[int] = None):
        hp = hp * 2
        defence_percent = defence_percent * 2
        super().__init__(name, hp, attack, defence_percent, critical_chance)

    @property
    def my_class_name(self):
        return 'Паладин'


class Warrior(Person):
    def __init__(self, name: str, hp: int,
                 attack: int, defence_percent: int,
                 critical_chance: Optional[int] = None):
        attack = attack * 2
        critical_chance = self.default_critical_chance(critical_chance)
        super().__init__(name, hp, attack, defence_percent, critical_chance)

    @staticmethod
    def default_critical_chance(critical_chance: Optional[int]) -> int:
        if critical_chance is None or critical_chance < 5:
            return 10
        return critical_chance

    @property
    def my_class_name(self):
        return 'Воин'
