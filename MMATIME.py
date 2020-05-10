import random
pers_name = ['нигретонок']

arena_person = []
things = []
arena_person_to_battle = []


class Thing:
    """
    Класс описывабщий амуницию вещей
    Имеет свойства
    name - название
    defense - процент защиты
    damage - уровень атаки
    hp - добавка к здоровью
    """
    def __init__(self):
        self.things = {}
        self.items = []

    def create_random_items_and_do_set(self, count):
        """
        Создает count вещей со случайными характеристиками
        :param :
        :return: список обьектов в виде словаря
        """
        for num in range(count):
            name = "предмет " + str(num)

            self.things[name] = {
                'name': name,
                'hp': random.randrange(0, 1000),
                'defense': random.randrange(0, 10) / 100,
                'damage': random.randrange(0, 500),
            }
            self.items.append(self.things[name])


class Person:
    """
    Класс о персанажах и работах с ними. Родитель
    """

    def __init__(self, name, hp, base_damage, base_defense):

        self.name = name
        self.hp = hp
        self.base_damage = base_damage
        self.base_defense = base_defense
        self.chars = {}

    def setthings(self, sort_eqip):
        """
        Одевает слуайно от 0 до 4 вещей на персонажа и складывает характеристики
        :param : сортированный список вещей по защите
        :return:
        """
        quent = random.randrange(0, 5)
        for num in range(0, quent):
            x = random.choice(sort_eqip)
            self.hp += x['hp']
            self.base_damage += x['damage']
            self.base_defense += x['defense']
            if self.base_defense > 0.1:
                self.base_defense = 0.1

        self.chars = {
            'name': self.name,
            'hp': self.hp,
            'damage': self.base_damage,
            'defense': self.base_defense,
        }

        arena_person_to_battle.append(self)

    def hp_damage(self, attack_damage):
        """
        Механика нанесения урона
        :param attack_damage: урон оппанента
        :return:
        """
        full_damage = attack_damage - attack_damage * self.base_defense
        self.hp -= full_damage


class Paladin(Person):
    """
    Паладин. Бонус на здоровье и защиту Х2
    """
    def __init__(self, name, hp=1000, base_damage=100, base_defense=0.005):
        super().__init__(self, name, base_damage, base_defense)
        self.name = name
        self.hp = hp * 2
        self.base_defense = base_defense * 2


class Warrior(Person):
    """
    Воин. Бонус на атаку Х2
    """
    def __init__(self, name, hp=1000, base_damage=100, base_defense=0.05):
        super().__init__(self, name, hp, base_defense)
        self.name = name
        self.hp = hp
        self.base_damage = base_damage * 2


def generate_persons():
    """
    Автоматическая генерация персонажей по введенному числу
    """
    print(f'Введите количество участников')
    x = int(input())
    pal = random.randrange(0, x)

    for x in range(1, pal + 1):
        name = f'Негритенок_{x}'
        hp = random.randrange(800, 1200)
        damage = random.randrange(80, 120)
        deff = random.randrange(0, 5)/100
        arena_person.append(Paladin(name, hp, damage, deff))

    for x in range(pal + 1, x + 1):
        name = f'Негритенок_{x}'
        hp = random.randrange(800, 1200)
        damage = random.randrange(80, 120)
        deff = random.randrange(0, 5)/100
        arena_person.append(Warrior(name, hp, damage, deff))


def eqiping(persons, eqip):
    for x in persons:
        Person.setthings(x, eqip)


# создаем персонажей
generate_persons()
print(f'Бойцы готовы')

#  создаем амуницию
things = Thing()
things.create_random_items_and_do_set(len(arena_person) * 3)
sort_eqip = sorted(things.items, key=lambda x: x['defense'])

# одеваем персонажей
eqiping(arena_person, sort_eqip)
print(f'Амуниция готова')

# Шаг 4 Битва
print(f'{len(arena_person_to_battle)} негритят собрались на арене')
while len(arena_person_to_battle) > 1:
    deff = random.choice(arena_person_to_battle)
    arena_person_to_battle.remove(deff)

    att = random.choice(arena_person_to_battle)
    arena_person_to_battle.remove(att)

    while deff.hp > 0:
        deff, att = att, deff
        deff.hp_damage(att.base_damage)
        print(f'{att.name} наносит удар по {deff.name} на {att.base_damage} урона')

    arena_person_to_battle.append(att)
    if len(arena_person_to_battle) != 1:
        print(f'И их остался {len(arena_person_to_battle)}')
    else:
        print(f'Последний {arena_person_to_battle[0].name} поглядел устало,')
        print(f'Он пошел повесился и никого не стало')
