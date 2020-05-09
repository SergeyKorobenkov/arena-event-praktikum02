from random import randint

from world.settings import HACKATONE_MODE
from world.texts import ThingsNameGenerator

thingsGen = ThingsNameGenerator()


class Thing:
    def __init__(self):
        self.name = thingsGen.take_name()
        self.attack_bonus = randint(-10, 10)
        self.defence_bonus = round(randint(-10, 100)*0.002, 2)
        self.hp_bonus = randint(0, 30)
        self.atk_durability = randint(1, 10)
        self.def_durability = randint(1, 10)

    def __str__(self):
        return f'{self.name}'


class Warehouse:
    def __init__(self):
        self.items_list = []

    def items(self) -> str:
        s = ''
        count_item = 1
        for item in self.items_list:
            if HACKATONE_MODE:
                item_string = f'{item.name}:\t+{item.hp_bonus}HP/' \
                              f'{item.attack_bonus}ATK/{item.defence_bonus}DEF'
            else:
                item_string = f'{item.name}:\t+{item.hp_bonus}HP/' \
                              f'{item.attack_bonus}ATK/' \
                              f'{item.defence_bonus}DEF/' \
                              f'{item.atk_durability}DA/' \
                              f'{item.def_durability}DD'
            if count_item % 4 == 0:
                s += item_string + '\n'
            else:
                s += item_string + '\t\t'
            count_item += 1
        return s

    def generate_things(self, num):
        for _ in range(num):
            self.items_list.append(Thing())

    def take_item(self) -> Thing:
        if len(self.items_list) == 0:
            return []
        i = randint(0, len(self.items_list) - 1)
        item = [self.items_list.pop(i)]
        return item

    def take_items(self, num) -> [Thing, ...]:
        list_to_take = []
        if len(self.items_list) == 0:
            return []
        if len(self.items_list) < num:
            list_to_take = self.items_list.copy()
            self.items_list = []
            return list_to_take
        for _ in range(num):
            i = randint(0, len(self.items_list)-1)
            list_to_take.append(self.items_list.pop(i))
        return list_to_take
