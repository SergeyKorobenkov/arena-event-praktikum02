import random
import time


class GameEngine:
    objects_map = {
        'persons': [],
        'things': [],
        'armors': [],
        'weapons': []
    }
    working = True
    game_process = False
    fighting = False
    __attacker_index = 0
    attack_start = None
    round_number = 1

    @property
    def attacker(self):
        return self.fighters[self.__attacker_index]

    @property
    def defender(self):
        return self.fighters[self.__get_defender_index()]

    @property
    def alive_persons(self):
        return [person for person in self.objects_map['persons'] if not person.is_defeated]

    @property
    def fighters(self):
        return [person for person in self.objects_map['persons'] if person.is_fighting]

    @property
    def is_game_over(self):
        return len(self.alive_persons) == 1

    def add_object(self, key, obj):
        self.objects_map[key].append(obj)

    def add_objects(self, key, objects):
        self.objects_map[key].extend(objects)

    def delete_object(self, key, obj):
        self.objects_map[key].remove(obj)

    def wear_persons(self):
        for person in self.objects_map['persons']:
            person.things = self.__collect_things(random.randint(1, 4))

    def start_fighting(self):
        if not self.fighting and len(self.fighters) == 0 and not self.is_game_over:
            fighters = random.sample(self.alive_persons, 2)
            fighters[0].is_fighting = True
            fighters[1].is_fighting = True
            self.fighting = True

    def end_fighting(self):
        if not self.fighting and len(self.fighters) == 2:
            if not self.fighters[0].is_defeated:
                self.fighters[0].attack_damage = 0
            if not self.fighters[1].is_defeated:
                self.fighters[1].attack_damage = 0
            self.fighters[0].is_fighting = False
            self.fighters[0].is_fighting = False
            self.__attacker_index = 0
            self.round_number = 1

    def attack(self):
        if not self.attack_start:
            self.attack_start = time.time()
        if time.time() - self.attack_start > 3:
            attack_damage = self.attacker.damage - self.defender.protection
            self.defender.attack_damage += attack_damage if attack_damage >= 0 else 0
            self.__attacker_index = self.__get_defender_index()
            if self.__attacker_index == 0:
                self.round_number += 1
            self.attack_start = None
            self.fighting = not (self.fighters[self.__attacker_index].is_defeated or self.round_number == 6)

    def __get_defender_index(self):
        return 1 if self.__attacker_index == 0 else 0

    def __collect_things(self, capacity):
        things = []
        if capacity == 1:
            things = self.objects_map['weapons'][:1]
            self.delete_object('weapons', things[0])
        elif capacity == 2:
            things = self.objects_map['weapons'][:1] + self.objects_map['armors'][:1]
            self.delete_object('weapons', things[0])
            self.delete_object('armors', things[1])
        elif capacity == 3:
            things = self.objects_map['weapons'][:1] + self.objects_map['armors'][:1] + self.objects_map['things'][:1]
            self.delete_object('weapons', things[0])
            self.delete_object('armors', things[1])
            self.delete_object('things', things[2])
        elif capacity == 4:
            things = self.objects_map['weapons'][:1] + self.objects_map['armors'][:1] + self.objects_map['things'][:2]
            self.delete_object('weapons', things[0])
            self.delete_object('armors', things[1])
            self.delete_object('things', things[2])
            self.delete_object('things', things[3])
        return things
