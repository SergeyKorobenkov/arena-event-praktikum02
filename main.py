import random


FIGHTER_NAME_LIST = ['Александр Пистолетов', 'Гладиатор', 'Viper', 'Phoenix', 'Techies',
                     'Bounty Hunter', 'Keeper of the Light', 'Axe', 'Shadow Demon', 'Beastmaster']
THING_NAME_LIST = ['BLOODSTONE', 'Assault Cuirass',
                   'Aghanim Scepter', 'Crystalys', 'Manta Style', 'EUL', 'DAGON']


class Thing:
    def __init__(self, name, hp, damage, armor_percent):
        self.name = name
        self.armor_percent = armor_percent
        self.damage = damage
        self.hp = hp


class Person:
    def __init__(self, name, hp, damage, armor_percent):
        self.name = name
        self.armor_percent = armor_percent
        self.damage = damage
        self.hp = hp
        self.things = []
        self.damage_done = 0
        self.kill_count = 0

    def set_things(self, things):
        self.things = things

    def incoming_attack(self, attack_damage, Attacker):

        # Если есть crystalis в инвентаре, то атака умножается на 3
        for thing in Attacker.things:
            if thing.name == 'Crystalys':
                attack_damage = attack_damage*3
                break

        attack_total_summ = (attack_damage - attack_damage *
                             self.git_final_protection())

        Attacker.damage_done += attack_total_summ

        self.hp = (self.hp - attack_total_summ)
        print(f'{Attacker.name} hits {self.name} for {attack_damage}, summ of attack with defenders protections {attack_total_summ}, {self.name} HP after attack {self.hp}')

    def get_summ_damage(self):

        things_damage = 0

        for thing in self.things:
            things_damage += thing.damage

        return things_damage + self.damage

    def git_final_protection(self):

        things_protection = 0

        for thing in self.things:
            things_protection += thing.armor_percent

        return self.armor_percent + things_protection


class Paladin(Person):
    def __init__(self, name, hp, damage, armor_percent):
        super().__init__(name, hp, damage, armor_percent)
        self.hp = hp*2
        self.armor_percent = min(0.8, armor_percent*2)


class Warrior(Person):
    def __init__(self, name, hp, damage, armor_percent):
        super().__init__(name, hp, damage, armor_percent)
        self.damage = damage*2


def get_person_name(used_names):

    random_name = FIGHTER_NAME_LIST[random.randrange(
        0, len(FIGHTER_NAME_LIST) - 1)]

    # простите
    while True:

        random_name = FIGHTER_NAME_LIST[random.randrange(
            0, len(FIGHTER_NAME_LIST) - 1)]
        if not random_name in used_names:
            return random_name


def get_thing_name(used_names):

    # простите
    while True:

        random_name = THING_NAME_LIST[random.randrange(
            0, len(THING_NAME_LIST) - 1)]
        if not random_name in used_names:
            return random_name


def get_fighter_thinglist(thing_list):

    fighter_thing_list = []
    cnt = 0
    num_of_things = random.randrange(1, 4)

    while cnt < num_of_things:
        random_thing = thing_list[random.randrange(0, len(thing_list) - 1)]
        if random_thing not in fighter_thing_list:
            fighter_thing_list.append(random_thing)
            cnt += 1

    return fighter_thing_list


fighter_list = []
used_fighter_names = []
used_things_names = []
thing_list = []

# Создаем предметы
for cnt in range(1, 5):

    new_thing_name = get_thing_name(used_things_names)
    used_things_names.append(new_thing_name)
    thing_armor_percent = random.randrange(1, 10) / 100
    thing_damage = random.randrange(1, 500)
    thing_hp = random.randrange(100, 1000)

    thing_list.append(Thing(new_thing_name, thing_hp,
                            thing_damage, thing_armor_percent))


# Создаем бойцов
for cnt in range(1, 9):

    new_person_name = get_person_name(used_fighter_names)
    used_fighter_names.append(new_person_name)

    fighter_armor_percent = random.randrange(1, 49) / 100
    fighter_damage = random.randrange(1, 200)
    fighter_hp = random.randrange(200, 1500)

    random_num = random.randrange(1, 100)

    if random_num % 2 == 0:
        Fighter = Paladin(new_person_name, fighter_hp,
                          fighter_damage, fighter_armor_percent)
    else:
        Fighter = Warrior(new_person_name, fighter_hp,
                          fighter_damage, fighter_armor_percent)

    fighter_list.append(Fighter)

# Экипируем бойцов
for fighter in fighter_list:

    fighter.set_things(get_fighter_thinglist(thing_list))
    print(f'Fighter total protection {fighter.git_final_protection()}')


round = 1
# Смертельная битва
while len(fighter_list) > 1:

    fighters_for_round = random.sample(fighter_list, 2)
    Attacker = fighters_for_round[0]
    Defender = fighters_for_round[1]

    print(f'Round {round} Fight! {Attacker.name} vs {Defender.name}')

    Defender.incoming_attack(Attacker.get_summ_damage(), Attacker)

    if Defender.hp < 0:
        fighter_list.remove(Defender)
        Attacker.kill_count += 1
        print(f'{Defender.name} has been removed from the arena')

    round += 1

winner = fighter_list[0]
print(f'The winner is {winner.name}, hp left {winner.hp}, winner total damage {winner.damage_done}, winner kills {winner.kill_count}, winner protection {winner.git_final_protection()}')
