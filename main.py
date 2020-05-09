import random

names_list = [
    'COVID19',
    'T110',
    'Mad Mask',
    'Maximus',
    'Proteus',
    'Bacilus',
    'Garrett',
    'Xena',
    'Парис',
    'Гектор',
    'Главк',
    'Одиссей',
    'Аякс',
    'Ахиллес',
    'Фоант',
    'Мерион',
    'Диомед',
    'Агамемнон',
    'Менелай',
    'Эврипил'
]


def coin_trow():
    if 1 * random.random() > 0.5:
        return True
    else:
        return False


class Thing(object):
    def __init__(self, item_name, item_armor, item_damage, item_hp):
        self.item_name = item_name
        self.item_armor = round(item_armor, 4)
        self.item_damage = item_damage
        self.item_hp = item_hp

    def __str__(self):
        return f'{self.item_name}: armor {self.item_armor}, damage {self.item_damage}, hp {self.item_hp}'


class Person(object):

    def __init__(self, name):
        self.things_set = []
        self.name = name
        self.hp = 100
        self.base_attack = 10
        self.base_armor = 0.1

    def setThings(self, things):
        self.things_set = things
        # print('\n')
        # print(self)
        # print('Я взял следующие предметы')
        for i in self.things_set:
            # print(i)
            self.base_armor += i.item_armor
            self.base_attack += i.item_damage
            self.hp += i.item_hp
        self.base_armor = round(self.base_armor, 4)
        # print('Теперь я', self)

    def take_hit_is_alive(self, hit):  # Сразу считаем оставшиеся жизни
        self.hp -= hit * self.base_armor
        print(f'{self.name} -{round(hit * self.base_armor, 4)} HP')
        if self.hp <= 0:
            # print(self.name + ' is dead! ')
            return False
        return True

    def calculate_hp(self, attack_damage):
        pass

    def __str__(self):
        return f'base attack: {self.base_attack}, base armor: {self.base_armor}, base hp: {round(self.hp, 4)}'


class Paladin(Person):
    def __init__(self, *args):
        super().__init__(*args)
        self.base_armor *= 2
        self.hp *= 2

    def __str__(self):
        return self.name + ' paladin ' + super().__str__()


class Warrior(Person):
    def __init__(self, *args):
        super().__init__(*args)
        self.base_attack *= 2

    def __str__(self):
        return self.name + ' warrior ' + super().__str__()


# obj = Paladin('John')

# Шаг 1 - создаем произвольное количество вещей с различными параметрами, процент защиты не должен превышать 10%(0.1)

item_list = []
for i in range(1, 40 + int(20 * random.random())):
    name = 'item-' + str(i)
    damage = random.randint(1, 10)
    armor = random.randrange(1, 10, 1) / 100  # не более 0.1
    hp = random.randint(10, 60)
    item_list.append([name, armor, damage, hp])

item_list.sort(key=lambda i: i[2])
things_list = []
for i in item_list:
    things_list.append(Thing(*i))

#    Шаг 2 - создаем произвольно 10 персонажей, кол-во воинов и паладинов произвольно.
#    Имена персонажам тоже рандомные из созданного списка 20 имен.

persons_list = []
for i in range(10):
    n = random.randint(0, len(names_list) - 1)
    name = names_list[n]
    names_list.pop(n)
    if coin_trow():
        persons_list.append(Warrior(name))
    else:
        persons_list.append(Paladin(name))

# Шаг 3 - одеваем персонажей рандомными вещами.
#    Кому-то 1, кому-то больше, но не более 4 вещей в одни руки;

for person in persons_list:
    peronal_items_set = []
    for j in range(random.randint(1, 4)):
        n = random.randint(0, len(things_list) - 1)
        item = things_list[n]
        things_list.pop(n)
        peronal_items_set.append(item)

    person.setThings(peronal_items_set)

# // Шаг 4 - отправляем персонажей на арену, и в цикле в произвольном порядке выбирается пара Нападающий и Защищающийся.
#     У Защищающегося вызывается метод вычитания жизни на основе атаки (attack_damage) Нападающего .
#     Количество получаемого урона рассчитывается по формуле (attack_damage - attack_damage*finalProtection)
#     Общий процент защиты (finalProtection) вычисляется по формуле (базовый процент защиты + процент защиты от всех надетых вещей)
#     Жизнь вычитается по формуле (HitPoints - (attack_damage - attack_damage*finalProtection)), где finalProtection - коэффициент защиты в десятичном виде;
#
#     Цикл идет до тех пор, пока не останется последнего выжившего.
#     Как только кол-во жизней меньше или равно 0, персонаж удаляется из арены (списка).
#     Для отслеживания процесса битвы выведите информацию в таком виде: ({атакующий персонаж} наносит удар по {защищающийся персонаж} на {кол-во урона} урона)

battle = 1

while battle != 0:
    first_player, second_player = random.sample(persons_list, 2)
    print('Арена выбрала: \n', first_player, ' и \n', second_player)
    fight = 1
    print(first_player.name, 'vs', second_player.name)
    print('FIGHT!!!')
    while fight != 0:
        if coin_trow():
            print(f'{first_player.name} наносит удар по {second_player.name} на {first_player.base_attack} урона')
            if not second_player.take_hit_is_alive(first_player.base_attack):
                print(second_player.name + ' Побежден!')
                persons_list.pop(persons_list.index(second_player))
                fight = 0
        else:
            print(f'{second_player.name} наносит удар по {first_player.name} на {second_player.base_attack} урона')
            if not first_player.take_hit_is_alive(second_player.base_attack):
                print(first_player.name + ' Побежден!')
                persons_list.pop(persons_list.index(first_player))
                fight = 0

    print('\n Осталось бойцов ', len(persons_list))
    if len(persons_list) == 1:
        print('Турнир окончен! Победитель ', persons_list[0])
        battle = 0
