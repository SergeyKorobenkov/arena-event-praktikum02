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


def coin_trow():  # Ранодомный выбор одно из двух
    if random.random() > 0.5:
        return True
    else:
        return False


class Thing(object):
    def __init__(self, item_name, item_armor, item_damage, item_hp):
        self.item_name = item_name
        self.item_armor = item_armor
        self.item_damage = item_damage
        self.item_hp = item_hp

    def __str__(self):
        return f'{self.item_name}: armor {self.item_armor},\
         damage {self.item_damage}, hp {self.item_hp}'


class Person(object):

    def __init__(self, name):
        self.things_set = []
        self.name = name
        self.hp = 100
        self.base_attack = 10
        self.base_armor = 0

    # Одеваем персонажа перед боем и пересчитываем его статы
    def setThings(self, things):
        self.things_set = things
        for item in self.things_set:
            self.base_armor += item.item_armor
            self.base_attack += item.item_damage
            self.hp += item.item_hp
        self.base_armor = self.base_armor

    # Считаем урон и возаращаем False если персонаж умер
    def take_hit_is_alive(self, hit):
        self.hp -= hit * self.base_armor
        print(f'{self.name} теряет {round(hit * self.base_armor, 4)} HP')
        if self.hp <= 0:
            # print(self.name + ' is dead! ')
            return False
        return True

    def __str__(self):
        return f'base attack: {self.base_attack},' \
               f' base armor: {round(self.base_armor, 4)},' \
               f' base hp: {round(self.hp, 4)}'


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


#  Шаг 1 - создаем произвольное количество вещей с различными параметрами,
#  процент защиты не должен превышать 10%(0.1)

def armory():
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
    return things_list


#    Шаг 2 - создаем произвольно 10 персонажей,
#    кол-во воинов и паладинов произвольно.
#    Имена персонажам тоже рандомные из созданного списка 20 имен.

def heroes_of_arena():
    persons_list = []
    for i in range(10):
        n = random.randint(0, len(names_list) - 1)
        name = names_list[n]
        names_list.pop(n)
        if coin_trow():
            persons_list.append(Warrior(name))
        else:
            persons_list.append(Paladin(name))
    return persons_list


# Шаг 3 - одеваем персонажей рандомными вещами.
#    Кому-то 1, кому-то больше, но не более 4 вещей в одни руки;

def prepair_for_battle(persons_list, things_list):
    for person in persons_list:
        peronal_items_set = []
        for j in range(random.randint(1, 4)):
            n = random.randint(0, len(things_list) - 1)
            item = things_list[n]
            things_list.pop(n)
            peronal_items_set.append(item)

        person.setThings(peronal_items_set)

# Функция передачи одного удара по игроку
def one_hit(first_player, second_player):
    print(f'{first_player.name} наносит удар по '
          f'{second_player.name} на {first_player.base_attack} урона')
    if not second_player.take_hit_is_alive(first_player.base_attack):
        print(second_player.name + ' побежден!')
        persons_list.pop(persons_list.index(second_player))
        return 0


things_list = armory()
persons_list = heroes_of_arena()
prepair_for_battle(persons_list, things_list)

# Шаг 4 - отправляем персонажей на арену, и в цикле в произвольном порядке
#  выбирается пара Нападающий и Защищающийся.
battle = 1

while battle != 0:
    first_player, second_player = random.sample(persons_list, 2)
    print('Арена выбрала: \n', first_player, ' и \n', second_player)
    fight = 1
    print(first_player.name, 'vs', second_player.name)
    print('FIGHT!!!')
    while fight != 0:
        if coin_trow():
            fight = one_hit(first_player, second_player)
        else:
            fight = one_hit(second_player, first_player)

    if len(persons_list) == 1:
        print('Турнир окончен! Победитель: ', persons_list[0].name)
        battle = 0
    else:
        print('\n Осталось бойцов ', len(persons_list))
