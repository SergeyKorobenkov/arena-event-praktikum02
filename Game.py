import random


class Thing:
    def __init__(self, name, defence_percent, attack, hp):
        self.name = name
        self.defence_percent = defence_percent
        self.attack = attack
        self.hp = hp


class Person:
    def __init__(self, name, pers_hp, pers_attack, pers_defence):
        self.name = name
        self.pers_hp = pers_hp
        self.pers_attack = pers_attack
        self.pers_defence = pers_defence


    def set_things(self, things):
        self.things = things
        self.pers_defence = self.pers_defence + self.things.defence_percent
        self.pers_attack = self.pers_attack + self.things.attack
        self.pers_hp = self.pers_hp + self.things.hp

    def by_attack(self, attack_damage):
        self.pers_hp = self.pers_hp - (attack_damage - attack_damage*self.pers_defence)

class Paladin(Person):
    def __init__(self, name, pers_hp, pers_attack, pers_defence):
        super().__init__(name, pers_hp, pers_attack, pers_defence)
        self.pers_hp = self.pers_hp * 2
        self.pers_defence = self.pers_defence * 2


class Warrior(Person):
    def __init__(self, name, pers_hp, pers_attack, pers_defence):
        super().__init__(name, pers_hp, pers_attack, pers_defence)
        self.pers_attack = pers_attack * 2


names_persons = ['Дарт Вейдер', 'Чубакка', 'Люк Скайуокер',
                 'C-3PO', 'R2-D2', 'Хан Соло', 'Принцесса Лея',
                 'Оби Ван', 'Джабба', 'Йода', 'Палпатин', 'Дарт Сидиус',
                 'Дарт Молл', 'Граф Дуку', 'Джа-Джа Бинкс', 'Уотто',
                 'Кайло Рен', 'Верховный лидер Сноук', 'ДиДжей', 'Мандалорец'
                 ]
random.shuffle(names_persons)

names_things = ['лапти', 'кольчуга', 'рубаха', 'подтяжки',
                'штаны', 'подштаники', 'ремень', 'шапка-ушанка',
                'варежки', 'руковицы', 'майка', 'петушок',
                'валенки', 'нижнее белье', 'шарф', 'рейтузы'
                ]
random.shuffle(names_things)

# Создаем произвольное количество вещей с различными параметрами, процент защиты не должен превышать 10%(0.1).
# Сортируем по проценту защиты, по возрастанию
things = []
for i in range(0, 41):
    things.append(Thing(random.choice(names_things), random.uniform(0, 1 / 10), random.randint(1, 100), random.randint(1, 100)))
sorted(things, key=lambda thing: thing.defence_percent)

# Cоздаем произвольно 10 персонажей, кол-во воинов и паладинов произвольно.
# Имена персонажам тоже рандомные из созданного списка 20 имен.

paladin_list = []
warrior_list = []

for i in range(1, 11):
    r = random.randint(1, 2)
    if r == 1:
        paladin_list.append(Paladin(names_persons[i], random.randint(1, 100), random.randint(1, 100), random.uniform(0, 1 / 10)))
    else:
        warrior_list.append(Warrior(names_persons[i], random.randint(1, 100), random.randint(1, 100), random.uniform(0, 1 / 10)))

# Список со всеми участниками битвы:
all = paladin_list + warrior_list


# Одеваем персонажей рандомными вещами.
# Кому-то 1, кому-то больше, но не более 4 вещей в одни руки
for i in paladin_list:
    for x in range(1, random.randint(1, 4)):
        i.set_things(random.choice(things))
for i in warrior_list:
    for x in range(1, random.randint(1, 4)):
        i.set_things(random.choice(things))


print('В битве участвуют:')
for i in all:
    print(f'{i.name}, здоровье:{i.pers_hp}, атака:{i.pers_attack}, защита:{round(i.pers_defence,2)}')
print()

arena = 10
while arena != 1:
    attack_pers = random.choice(all)
    defence_pers = random.choice(all)
    if attack_pers == defence_pers:
        defence_pers = random.choice(all)
    defence_pers.by_attack(attack_pers.pers_attack)
    print(f'Атакующий персонаж {attack_pers.name} наносит удар по {defence_pers.name} на {attack_pers.pers_attack} урона')
    if defence_pers.pers_hp > 0:
        print(f'У {defence_pers.name} остается {round(defence_pers.pers_hp)} здоровья')
    else:
        print()
        print(f'{defence_pers.name} выбывает из битвы')
        all.remove(defence_pers)
        arena = arena-1
        print('В битве остаются:', len(all))
        for i in all: print(i.name, end='  ')
        print()

print(f'Победитель битвы - {all[0].name}')


