import random


THINGS_LIST = ['Дубина', 'Меч', 'Нож', 'Кастет', 'Бронежелет', 'Шлем', 'Латы',
               'Шокер', 'Щит']
THINGS = {
    'Дубина': {'защита': 1, 'атака': 20, 'жизнь': 20},
    'Меч': {'защита': 1, 'атака': 30, 'жизнь': 9},
    'Нож': {'защита': 1, 'атака': 20, 'жизнь': 19},
    'Кастет': {'защита': 2, 'атака': 20, 'жизнь': 15},
    'Бронежелет': {'защита': 10, 'атака': 0, 'жизнь': 30},
    'Шлем': {'защита': 9, 'атака': 0, 'жизнь': 30},
    'Латы': {'защита': 7, 'атака': 0, 'жизнь': 40},
    'Шокер': {'защита': 0, 'атака': 20, 'жизнь': 20},
    'Щит': {'защита': 10, 'атака': 5, 'жизнь': 25},
}

NAMES = ['Васёк', 'Петрович', 'Витёк', 'Макарыч', 'Иван', 'Люся', 'Петька',
         'Василий Иваныч', 'Серёга', 'Машка']

ENEMY_NAMES = ['Абадон', 'Дум', 'Пудж', 'Шэдоу Демон', 'Снайпер', 'Ульфзаар',
               'Троль', 'Лиорик', 'Сларк', 'Некрофос']


class Thing:

    def __init__(self, name, protection, attack, life):
        self.name = name
        self.protection = protection
        self.attack = attack
        self.life = life


class Person:

    def __init__(self, name, hp, base_damage, base_protection, team):
        self.name = name
        self.hp = hp
        self.base_protection = base_protection
        self.base_damage = base_damage
        self.final_protection = base_protection
        self.final_damage = base_damage
        self.target = None
        self.things_list = None
        self.team = team
        self.damage_points = 0

    def __str__(self):
        return f'Я - {self.name}. Здоровье: {round(self.hp, 2)} ' \
               f'Всего нанёс урона {round(self.damage_points, 2)}'

    def set_things(self, things_list):
        self.things_list = things_list
        if self.things_list:
            for thing in self.things_list:
                self.final_protection += thing.protection
                self.final_damage += thing.attack
                self.hp += thing.life

    def attack(self, targets_list):
        if self.hp <= 0:
            return f'Персонаж {self.name} отправился к праотцам :-('
        if targets_list:
            target = random.choice(targets_list)
            targets_list.remove(target)
            points = self.final_damage - self.final_damage * target.final_protection / 100
            self.damage_points += points
            target.hp -= points
            print(f'{self.name} атаковал(а) персонажа {target.name} '
                  f'и нанес(ла) ему урон {points}')
            if target.hp >= 0:
                targets_list.append(target)
            else:
                print(f'{self.name} убил(a) персонажа {target.name}')
        else:
            print(f'Мне некого атаковать!!! Дайте мне цель!')


class Paladin(Person):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_protection = self.base_protection * 2
        self.hp = self.hp * 2


class Warrior(Person):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_damage = self.base_damage * 2


def generate_perk_things():
    things_list = []
    for i in range(4):
        if random.randint(0, 1):
            name = random.choice(THINGS_LIST)
            things_list.append(
                Thing(name=name,
                      protection=THINGS[name]['защита'],
                      attack=THINGS[name]['атака'],
                      life=THINGS[name]['жизнь']
                      )
            )
    return things_list


def generate_team(team, names, team_name):
    for i in range(10):
        if random.randint(0, 1):
            team.append(Paladin(name=names[i], hp=100, base_damage=20,
                                base_protection=20, team=team_name))
        else:
            team.append(Warrior(name=names[i], hp=100, base_damage=20,
                                base_protection=20, team=team_name))
    team = [perk.set_things(generate_perk_things()) for perk in team]


def get_info(team):
    print(f'Команда: {team[0].team}')
    print('-' * 82)
    print(
        f"|{'Имя':^15}|{'Здоровье':^12}|{'Нанесённый урон':^20}|{'Вещи':^30}|")
    print('-' * 82)
    for perk in team:
        print(
            f'|{perk.name:^15}|{round(perk.hp, 2):^12}|{round(perk.damage_points, 2):^20}|'
            f'{", ".join([thing.name for thing in perk.things_list]):<30}|')
        print('-' * 82)
    print('\n\n')


def save_info(team, step):
    name = team[0].team
    with open(f'{name}.txt', mode='a') as file:
        file.write(
            f'Ход:{step}\n'
            f'Команда: {team[0].team} \n'
            "---------------------------------------------------------------------------------------\n"
            f"|{'Ход':^6}|{'Имя':^15}|{'Здоровье':^12}|{'Нанесённый урон':^20}|{'Вещи':^30}|\n"
            "---------------------------------------------------------------------------------------\n"
        )
        for perk in team:
            file.write(
                f'|{step:^6}|{perk.name:^15}|{round(perk.hp, 2):^12}|{round(perk.damage_points, 2):^20}|'
                f'{", ".join([thing.name for thing in perk.things_list]):<30}|\n'
                '---------------------------------------------------------------------------------------\n'
            )


