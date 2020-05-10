import yaml
import random

from person import Warrior, Paladin
from thing import Thing, Armor, Weapon


def reload_game(engine):
    global names_list
    engine.objects = []
    generator = Objects()
    objects_map = generator.get_objects_map()
    for key in objects_map:
        engine.add_objects(key, objects_map[key])
    engine.wear_persons()
    engine.game_process = True


def start_fighting(engine):
    engine.start_fighting()


def service_init():
    global names_list

    file = open('names.yml', 'r')

    names_list = yaml.load(file.read())
    file.close()


class Objects:

    def __init__(self):
        self.objects_map = {
            'persons': [],
            'things': [],
            'armors': [],
            'weapons': []
        }

    def get_objects_map(self):

        for thing_name in names_list['things']:
            if thing_name == 'Лошарик':
                object_instance = Thing(name=thing_name, hp=10, damage=10, protection=10)
                self.objects_map['things'].append(object_instance)
            else:
                capacity = random.randint(4, 8)
                for _ in range(capacity):
                    hp = random.randint(1, 10)
                    damage = random.randint(1, 10)
                    protection = random.randint(1, 4)
                    object_instance = Thing(name=thing_name, hp=hp, damage=damage, protection=protection)
                    self.objects_map['things'].append(object_instance)

        for armor_name in names_list['armors']:
            capacity = random.randint(4, 8)
            for _ in range(capacity):
                hp = random.randint(1, 10)
                damage = random.randint(1, 10)
                protection = random.randint(1, 4)
                object_instance = Armor(name=armor_name, hp=hp, damage=damage, protection=protection)
                self.objects_map['armors'].append(object_instance)

        for armor_name in names_list['weapons']:
            capacity = random.randint(4, 8)
            for _ in range(capacity):
                hp = random.randint(1, 10)
                damage = random.randint(1, 10)
                protection = random.randint(1, 10)
                object_instance = Weapon(name=armor_name, hp=hp, damage=damage, protection=protection)
                self.objects_map['weapons'].append(object_instance)

        for person_name in names_list['persons']:
            hp = random.randint(1, 10)
            damage = random.randint(1, 10)
            protection = random.randint(1, 10)
            is_paladin = random.randint(1, 2) == 2
            object_instance = Paladin(name=person_name, hp=hp, damage=damage, protection=protection) if is_paladin \
                else Warrior(name=person_name, hp=hp, damage=damage, protection=protection)
            self.objects_map['persons'].append(object_instance)

        return self.objects_map
