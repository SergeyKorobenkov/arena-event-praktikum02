# В данной реализации я решил отказаться от одного из навыков Паладина:
# удваивать свою защиту. Иначе Палладин, на мой взгляд, получает
# сильное преимущество в бою.
#
# Однако, реализованы категории сняряжения: нагрудник, шлем и оружие.
# Последнее имеет два типа — меч и молот.
# Так же некоторое снаряжение может накладывать на персонажа отрицательный
# эффект (уменьшение жизни или урона).

from random import randint, choice, sample


class Thing:
    def __init__(self, name, hp, dmg, df=0):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.df = round(float(df), 2)


class Person:
    def __init__(self, hp, dmg, df):
        self.name = choice(Person.names)
        self.hp = hp
        self.dmg = dmg
        self.df = df
        Person.names.remove(self.name)
        print(self.name)

    def set_things(self, things):
        # Подбрасываем монетку четыре раза на каждый тип шмотки
        print(f'{self.name} получает:')
        cnt = 0
        if randint(0, 1):
            item_one = choice(things['breastplate'])
            self.hp += item_one.hp
            self.dmg += item_one.dmg
            self.df += item_one.df
            things['breastplate'].remove(item_one)
            print(f'\t{item_one.name}')
            cnt += 1

        if randint(0, 1):
            item_two = choice(things['helmet'])
            self.hp += item_two.hp
            self.dmg += item_two.dmg
            self.df += item_two.df
            things['helmet'].remove(item_two)
            print(f'\t{item_two.name}')
            cnt += 1

        for cnt in range(randint(1, 2)):
            item_three_four = choice(things['weapon'])
            self.hp += item_three_four.hp
            self.dmg += item_three_four.dmg
            self.df += item_three_four.df
            things['weapon'].remove(item_three_four)
            print(f'\t{item_three_four.name}')
            cnt += 1

        if cnt == 0:
            print('Кукиш с маслом.')

        print()

    def attack(self, enemy):
        enemy.hp = enemy.hp - (self.dmg - self.dmg*enemy.df)

    names = [
        'Лаувейя', 'Кратос', 'Локи', 'Бальдр', 'Один',
        'Фрея', 'Тор', 'Тир', 'Ёрмунганд', 'Мимир',
        'Магни', 'Моди', 'Синдри', 'Брок', 'Хейла',
        'Хермот', 'Од', 'Видар', 'Хеймдалль', 'Риг',
    ]


class Paladin(Person):
    def __init__(self, hp, dmg, df):
        super().__init__(hp, dmg, df)
        self.hp = hp * 2
        print('\tКласс: Paladin')
        print(f'\tHP — {self.hp}\n\tDMG — {self.dmg}\n\tDF — {self.df}')
        print()


class Warrior(Person):
    def __init__(self, hp, dmg, df):
        super().__init__(hp, dmg, df)
        self.dmg = dmg * 2
        print('\tКласс: Warrior')
        print(f'\tHP — {self.hp}\n\tDMG — {self.dmg}\n\tDF — {self.df}')
        print()


class Fight:
    def __init__(self, two_units):
        self.attacker = two_units[0]
        self.defender = two_units[1]
        self.name = f'{two_units[0].name} vs {two_units[1].name}'

    def start_fight(self):
        # Изначальные показатели здоровья персонажей
        original_attacker_hp = self.attacker.hp
        original_defender_hp = self.defender.hp

        while True:
            # Attacker turn
            if randint(0, 1) == 1:
                self.attacker.attack(self.defender)
                if self.defender.hp <= 0:
                    print(f'В битве "{self.name}" побеждает:\n' +
                          f'\t{self.attacker.name}!')
                    if self.attacker.hp / original_attacker_hp < 0.3:
                        print(f'\tНо не обошлось без синяков.')
                    print()
                    # Лечим атаковавшего
                    self.attacker.hp = original_attacker_hp
                    return self.defender

            # Defender Turn
            if randint(0, 1) == 1:
                self.defender.attack(self.attacker)
                if self.attacker.hp <= 0:
                    print(f'В битве "{self.name}" побеждает:\n' +
                          f'\t{self.defender.name}!')
                    if self.defender.hp / original_defender_hp < 0.3:
                        print(f'\tНо не обошлось без синяков.')
                    print()
                    # Лечим защищавшегося
                    self.defender.hp = original_defender_hp
                    return self.attacker


# Чертежи вещей
breastplates = {
    'Нагрудник Ринариум': (20, 3, 0.02),
    'Нагрудник Акана': (25, 1, 0.03),
    'Нагрудник Теграка': (25, 2, 0.05),
    'Нагрудник Императора ужасных драконов': (10, 8, 0.03),
    'Дрениумовый нагрудник': (-9, 0, 0.07),
    'Нагрудник арены': (15, 3, 0.03),
    'Нагрудник Императора черных драконов': (20, 7, 0.03),
    'Нагрудник Мариссы': (40, 0, 0.01),
    'Нагрудник Фенрира': (40, 0, 0.01),
    'Ржавый нагрудник': (5, 0, 0.01),
    'Старый деревянный нагрудник': (3, 0, 0.01),
    'Нагрудник истощения': (-10, 0, 0.03),
    'Проклятый нагрудник': (-19, 0, 0.02),
}

helmets = {
    'Шлем Ринариум': (5, 0, 0.02),
    'Шлем Акана': (7, 0, 0.01),
    'Шлем Теграка': (7, 0, 0.01),
    'Шлем Императора ужасных драконов': (4, 0, 0.03),
    'Дрениумовый шлем': (-3, 0, 0.03),
    'Шлем арены': (3, 0, 0.02),
    'Шлем Императора черных драконов': (5, 0, 0.01),
    'Шлем Мариссы': (10, 0, 0.01),
    'Шлем Фенрира': (10, 0, 0.01),
    'Ржавый шлем': (2, 0, 0.01),
    'Старый деревянный шлем': (2, 0, 0),
    'Шлем истощения': (-3, 0, 0.02),
    'Проклятый шлем': (-5, 0, 0.01),
}

weapons = {
    'Меч Императора ужасных драконов': (0, 4),
    'Молот Императора ужасных драконов': (0, 4),
    'Меч Императора черных драконов': (0, 4),
    'Молот Императора черных драконов': (0, 4),

    'Меч Ринариум': (0, 3), 'Молот Ринариум': (0, 4),
    'Меч Акана': (0, 3), 'Молот Акана': (0, 4),
    'Меч Теграка': (0, 2), 'Молот Теграка': (0, 2),
    'Дрениумовый меч': (0, 8), 'Дрениумовый молот': (0, 9),
    'Меч арены': (0, 3), 'Молот арены': (0, 4),
    'Меч Мариссы': (0, 6), 'Молот Мариссы': (0, 7),
    'Меч Фенрира': (0, 4), 'Молот Фенрира': (0, 5),
    'Ржавый меч': (0, 1), 'Ржавый молот': (0, 1),
    'Старый деревянный меч': (0, 0), 'Старый деревянный молот': (0, 1),
    'Меч истощения': (0, 1), 'Молот истощения': (0, 1),
    'Проклятый меч': (0, -3), 'Проклятый молот': (0, -5),
}

AMOUNT_WARRIORS = 10

units = []
items = {'breastplate': [], 'helmet': [], 'weapon': []}
print()
print('К БИТВЕ ГОТОВЯТСЯ:')
print()

# Создаем персонажей и куем случайные вещи по имеющимся чертежам
for i in range(AMOUNT_WARRIORS):
    health = randint(20, 50)
    damage = randint(3, 8)
    defend = round(float(0), 2)
    if randint(0, 1) == 1:
        units.append(Paladin(health, damage, defend))
    else:
        units.append(Warrior(health, damage, defend))

    # Нагрудник
    b = choice(list(breastplates.items()))
    breastplate = Thing(b[0], b[1][0], b[1][1], b[1][2])
    items['breastplate'].append(breastplate)
    del breastplates[b[0]], b, breastplate

    # Шлем
    h = choice(list(helmets.items()))
    helmet = Thing(h[0], h[1][0], h[1][1], h[1][2])
    items['helmet'].append(helmet)
    del helmets[h[0]], h, helmet

    # Оружие
    for j in range(2):
        w = choice(list(weapons.items()))
        weapon = Thing(w[0], w[1][0], w[1][1])
        items['weapon'].append(weapon)
        del weapons[w[0]], w, weapon

# Снаряжаем воинов, либо отправляем драться в чем мать родила
print('Снарядим воинов?\n' +
      '(Y) — Конечно.\n' +
      '(N) — ... ну я вообще по своей натуре ' +
      'довольно жестокий человек.')

if input('Ваш ответ: ').lower() != 'n':
    print()
    for unit in units:
        unit.set_things(items)

# Старт битвы
input('БИТВА НАЧИНАЕТСЯ\n(press Enter)')

while len(units) != 1:
    pare = sample(units, 2)
    combat = Fight(pare)
    loser = combat.start_fight()
    units.remove(loser)

# Подведение итогов
print('БИТВА ОКОНЧЕНА')
print(f'Победитель: {units[0].name}!')
