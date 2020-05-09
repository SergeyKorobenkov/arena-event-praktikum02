from random import choice, randint

from world.settings import HACKATONE_MODE, MAX_ITEMS_TO_FIGHTER
from world.texts import (PersonNameGenerator, broke_atk_item_msg,
                         broke_def_item_msg, make_hit_msg)


class Person():

    suffix = ''
    hp_bonus = 1
    attack_bonus = 1
    defence_bonus = 1

    def __init__(self, name, hp, attack, defence):
        self.name = self.suffix+' '+name
        self.base_hp = hp*self.hp_bonus
        self.hp = self.base_hp
        self.attack = attack*self.attack_bonus
        self.defence = defence*self.defence_bonus
        self.items = []
        if not HACKATONE_MODE:
            self.atk_item = None
            self.def_item = None

    def __str__(self):
        return f'{self.name}:{self.hp}HP/{self.attack}ATK/{self.defence}DEF'

    def __sub__(self, attacker):
        atk_dmg = attacker.makeDamage()
        def_hp = self.hp
        self.takeDamage(atk_dmg)
        print(make_hit_msg(attacker, self, def_hp, atk_dmg))
        if not HACKATONE_MODE:
            if self.def_item is not None:
                if self.def_item.def_durability == 0:
                    print(broke_def_item_msg(self.name,
                                             self.def_item.name,
                                             attacker.name))
                    self.items.remove(self.def_item)
            if attacker.atk_item is not None:
                if attacker.atk_item.atk_durability == 0:
                    print(broke_atk_item_msg(attacker.name,
                                             attacker.atk_item.name,
                                             self.name))
                    attacker.items.remove(attacker.atk_item)

    def setThings(self, things) -> bool:
        if len(self.items) >= MAX_ITEMS_TO_FIGHTER:
            return False
        self.items.extend(things)
        for thing in things:
            self.hp += thing.hp_bonus
            if HACKATONE_MODE:
                self.attack += thing.attack_bonus
                self.defence += thing.defence_bonus
        return True

    def takeDamage(self, attack_damage: int) -> None:
        finalProtection = self.defence
        if not HACKATONE_MODE:
            if self.items:
                self.def_item = choice(self.items)
                finalProtection += self.def_item.defence_bonus
                self.def_item.def_durability -= 1
            else:
                self.def_item = None

        damage = attack_damage - attack_damage * finalProtection
        self.hp = round(self.hp - damage, 2)

    def makeDamage(self) -> int:
        damage = self.attack
        if not HACKATONE_MODE:
            if self.items:
                self.atk_item = choice(self.items)
                damage += self.atk_item.attack_bonus
                self.atk_item.atk_durability -= 1
            else:
                self.atk_item = None
        if damage < 0:
            damage = 0
        return damage


class Paladin(Person):
    suffix = 'Сэр'
    hp_bonus = 2
    defence_bonus = 2


class Warrior(Person):
    suffix = 'Грязный'
    attack_bonus = 2


class Paladina(Paladin):
    suffix = 'Лэди'


class Warriora(Warrior):
    suffix = 'Грязная'


namesGen = PersonNameGenerator()


def generatePersons(number):
    person_list = []

    unique_name_set = set()
    classSelector = {
        'male': [Paladin, Warrior],
        'female': [Paladina, Warriora]
        }
    for _ in range(number):
        # check unique name:
        while True:
            gender, name = namesGen.give_name()
            if name not in unique_name_set:
                break
        unique_name_set.add(name)

        hp = randint(1, 100)
        atk = randint(1, 15)
        defence = round(randint(1, 100)*0.0049, 2)
        person = choice(classSelector[gender])(name, hp, atk, defence)

        person_list.append(person)
    return person_list
