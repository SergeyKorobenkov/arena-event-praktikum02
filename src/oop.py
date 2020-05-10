import random

from src import game_settings


# Items
class Thing:
    def __init__(self, name, health, attack, defence):
        self.name = name
        self.defence_proc = round(defence, 2)
        self.attack = attack
        self.health = health

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


# Hero
class Person:
    def __init__(self, name, health, basic_attack, basic_defence):
        self.name = name
        self.health = health
        self.basic_attack = basic_attack
        self.basic_defence_proc = round(basic_defence, 2)
        self.stat_damage = 0
        self.stat_max_damage = 0
        self.stat_fights = 0
        self.stat_wins = 0

    def apply_items_modifications(self, mod_list):
        
        for item in mod_list:
            self.full_health = self.health + item.health
            self.full_attack = self.basic_attack + item.attack
            self.full_defence_proc = \
                round(self.basic_defence_proc + item.defence_proc, 2)
        if self.full_defence_proc > 0.99:
            self.full_defence_proc = 0.99
        return len(mod_list)

    def setThings(self, things):
        self.items_list = []
        item_number = random.choice(range(game_settings.MIN_ITEMS_PER_HERO, game_settings.MAX_ITEMS_PER_HERO + 1))
        self.items_list = random.sample(things, item_number)
        if len(self.items_list):
            self.apply_items_modifications(self.items_list)

    def attack_enemy(self, enemy):
        attack_damage =\
            round(self.full_attack - self.full_attack * enemy.full_defence_proc, 2)
        if attack_damage <= 0:
            raise ValueError("Некорректное значение процента защиты")
        enemy.full_health = round(enemy.full_health - attack_damage, 2)

        # Collect statistics
        self.stat_damage = round(self.stat_damage + attack_damage, 2)
        if attack_damage > self.stat_max_damage:
            self.stat_max_damage = attack_damage
        self.stat_fights += 1
        enemy.stat_fights += 1

        if enemy.full_health <= 0:
            self.stat_wins += 1
            return 1
        return 0

    def __str__(self):
        return self.name

    def __repr__(self):
        return '({}, {}, {}, {})'.format(self.name, self.stat_fights, self.stat_wins, self.stat_max_damage)


class Paladin(Person):
    def __init__(self, name, health, basic_attack, basic_defence):
        super().__init__(name, health, basic_attack, basic_defence)
        self.health = health * game_settings.PALADIN_HP_MODIFICATOR
        self.basic_defence_proc = \
            basic_defence * game_settings.PALADIN_DEFENCE_MODIFICATOR
        if self.basic_defence_proc > 0.99:
            self.basic_defence_proc = 0.99


class Warrior(Person):
    def __init__(self, name, health, basic_attack, basic_defence):
        super().__init__(name, health, basic_attack, basic_defence)
        self.basic_attack = basic_attack * game_settings.WARRIOR_ATTACK_MODIFICATOR


def set_fighter_params():
    params = {
        "health": random.choice(range(1, game_settings.MAX_HEALTH_POINTS + 1)),
        "basic_attack": random.choice(range(1, game_settings.MAX_HEALTH_POINTS + 1)),
        "basic_defence": random.choice(range(1, game_settings.MAX_DEFENCE_PROC_H + 1)) / 100.00
                }
    return params


def create_fighter_pool(FIGHTERS_NUMBER):
    fighter_pool = []
    for _i in range(FIGHTERS_NUMBER):
        fighter_id = random.choice([True, False])
        fighter_name = random.choice(game_settings.NAME_TITLE)\
            + ' ' + random.choice(game_settings.HERO_NAMES)
        fighter_params = set_fighter_params()
        if fighter_id:
            fighter_pool.append(Paladin(fighter_name + " Paladin",\
                                        fighter_params["health"], \
                                        fighter_params["basic_attack"],\
                                        fighter_params["basic_defence"]))
        else:
            fighter_pool.append(Warrior(fighter_name + " Warrior",\
                                        fighter_params["health"],\
                                        fighter_params["basic_attack"],\
                                        fighter_params["basic_defence"]))
    return fighter_pool


def set_item_params():
    params = {
            "health": random.choice(range(1, game_settings.MAX_HEALTH_POINTS + 1)),
            "attack": random.choice(range(1, game_settings.MAX_HEALTH_POINTS + 1)),
            "defence_proc": random.choice(range(1, game_settings.MAX_DEFENCE_PROC + 1)) / 100.00
                }
    return params


def create_item_pool(MAX_ITEMS_PER_HERO):
    items_pool = []
    for _i in range(MAX_ITEMS_PER_HERO * game_settings.FIGHTERS_NUMBER):
        item_name = random.choice(game_settings.ITEM_QUALITIES) + ' '\
                                        + random.choice(game_settings.ITEM_NAMES)
        item_params = set_item_params()
        items_pool.append(Thing(item_name,\
                                item_params["health"],\
                                item_params["attack"],\
                                item_params["defence_proc"]))
    return items_pool
