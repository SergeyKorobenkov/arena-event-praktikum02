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
    if random.random() > 0.5:
        return True
    else:
        return False


class Thing:
    def __init__(self, item_name, item_armor, item_damage, item_hp):
        self.item_name = item_name
        self.item_armor = item_armor
        self.item_damage = item_damage
        self.item_hp = item_hp


class Person:

    def __init__(self, name):
        self.things_set = []
        self.name = name
        self.hp = 100 + random.randint(1, 10)
        self.base_attack = 10 + random.randint(1, 5)
        self.base_armor = 0.1
        self.kills = 0

    # Одеваем персонажа перед боем и пересчитываем его статы
    def setThings(self, things):
        self.things_set = things
        for item in self.things_set:
            self.base_armor += item.item_armor
            self.base_attack += item.item_damage
            self.hp += item.item_hp
        self.base_armor = self.base_armor

    # Считаем урон и возвращаем True если персонаж умер
    def take_and_check(self, attacker):
        hit = attacker.base_attack
        result_hit = hit - hit * self.base_armor
        print('{} наносит удар по {} на {:.2f} урона'.format(
            attacker.name, self.name, hit))
        self.hp -= result_hit
        print('{} теряет {:.2f} HP'.format(self.name, result_hit))
        if self.hp <= 0:
            attacker.kills += 1
            return True
        return False

    def __str__(self):
        return 'base attack: {:.2f} armor: {:.2f)} hp: {:.2}'.format(
            self.base_attack, self.base_armor, self.hp)


class Paladin(Person):
    def __init__(self, *args):
        super().__init__(*args)
        self.base_armor *= 2
        self.hp *= 2

    def __str__(self):
        return '{} paladin {}'.format(self.name, super().__str__())


class Warrior(Person):
    def __init__(self, *args):
        super().__init__(*args)
        self.base_attack *= 2

    def __str__(self):
        return '{} warrior {}'.format(self.name, super().__str__())


#  Шаг 1 - создаем произвольное количество вещей с различными параметрами,
#  процент защиты не должен превышать 10%(0.1)

def armory():
    item_list = []
    for i in range(1, 40 + random.randint(1, 20)):
        name = 'item-' + str(i)
        damage = random.randint(1, 10)
        armor = random.randrange(1, 10, 1) / 100  # не более 0.1
        hp = random.randint(10, 60)
        item_list.append([name, armor, damage, hp])

    item_list.sort(key=lambda i: i[2])
    things_list = []
    for item in item_list:
        things_list.append(Thing(*item))
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
# Кому-то 1, кому-то больше, но не более 4 вещей в одни руки;

def prepare_for_battle(persons_list, things_list):
    for person in persons_list:
        peronal_items_set = []
        for j in range(random.randint(1, 4)):
            n = random.randint(0, len(things_list) - 1)
            item = things_list[n]
            things_list.pop(n)
            peronal_items_set.append(item)

        person.setThings(peronal_items_set)


things_list = armory()
persons_list = heroes_of_arena()
prepare_for_battle(persons_list, things_list)


#  Шаг 4 - отправляем персонажей на арену, и в цикле в произвольном порядке
#  выбирается пара Нападающий и Защищающийся.

# Вынести побежденного с Арены
def clean_arena(is_dead, second):
    if is_dead:
        print('{} побежден!\n'.format(second.name))
        persons_list.pop(persons_list.index(second))
        return False
    return True


while len(persons_list) > 1:
    first_player, second_player = random.sample(persons_list, 2)
    fight = True
    print(first_player.name, 'vs', second_player.name)
    print('FIGHT!!!')
    while fight:
        if coin_trow():
            fight = clean_arena(first_player.take_and_check(second_player),
                                first_player)
        else:
            fight = clean_arena(second_player.take_and_check(first_player),
                                second_player)
    print('Осталось бойцов ', len(persons_list))

print('{:-<60} \n Турнир окончен! Победитель: {} сразил {} противника'
      .format('', persons_list[0].name, persons_list[0].kills))
