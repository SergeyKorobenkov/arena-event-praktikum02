import random
from random import randint

name_list = [
    'Чак Норрис',
    'Чубакка',
    'Люк Скайуокер',
    'Йода',
    'Ктулху',
    'Тираннозавр Рекс',
    'Конор Макгрегор',
    'Хищник',
    'Пикачу',
    'Cлоупок',
    'Лара Крофт',
    'Чудо-Женщина',
    'Дайнерис Таргариен',
    'Арья Старк',
    'Король Ночи',
    'Волан-Де-Морт',
    'Тинки-Винки',
    'Рик Санчес',
    'Котзилла',
    'Мистер Крабс'
]


class Thing:

    def __init__(self, name, armor, attack, hp):
        self.name = name
        self.armor = armor
        self.attack = attack
        self.hp = hp

    def info(self):
        print(f'{self.name}\nБроня - {self.armor}\n'
              f'Атака - {self.attack}\nЗдоровье - {self.hp}\n')


class Person:

    all_things = [
        Thing('Секретный ингредиент', 0.4, 6, 10),
        Thing('Сюрикен', 0, 3, 3),
        Thing('Экскалибур', 0, 7, 10),
        Thing('Жало', 0, 4, 8),
        Thing('Кольчуга', 0.1, 0, 12),
        Thing('Трезубец', 0, 8, 7),
        Thing('Лук Геракла', 0, 6, 8),
        Thing('Доспехи Тора', 0.095, 0, 15),
        Thing('Шлем самурая', 0.09, 0, 5),
        Thing('Ботинки', 0.11, 0, 5)
    ]

    #Возвращает атаку базовую + предметов
    def finalAttack(self):
        if self.things:
            thing_attack = 0
            for thing in self.things:
                thing_attack = thing_attack + thing.attack
            return (self.attack+thing_attack)
        else:
            return self.attack

    #Возвращает защиту базовую + предметов
    def finalProtection(self):
        if self.things:
            thing_armor = 0
            for thing in self.things:
                thing_armor = thing_armor + thing.armor
            return (self.armor + thing_armor)
        else:
            return self.armor

    def __init__(self, name, armor, attack, hp):
        self.name = name
        self.armor = armor
        self.attack = attack
        self.hp = hp
        self.things = [random.choice(self.all_things)
                       for i in range(1, randint(1, 4))]

    def more_info(self):
        print(f'Имя - {self.name}\nБроня - {self.armor}\nАтака - {self.attack}'
              f'\nЗдоровье - {self.hp}')
        if len(self.things) > 0:
            print('\nСнаряжение:')
            for thing in self.things:
                thing.info()
        print('__________________________________________'
              '____________________________________________')

    def info(self):
        print(f'{self.name}/{round(self.finalProtection(),2)}'
              f'/{self.finalAttack()}/{self.hp}')

    def defense(self, attack_damage):
        damage = round(attack_damage - attack_damage*self.finalProtection(), 2)
        if damage > 0:
            self.hp = self.hp - damage
        else:
            damage = 0
        return damage

    def setThings(self, things):
        if len(self.things) < 4:
            self.things.append(things)


class Paladin(Person):
    def __init__(self, name, armor, attack, hp):
        super().__init__(name, armor, attack, hp)
        self.hp = hp * 2
        self.armor = armor*2

    def classInfo(self):
        print(f'Ваш класс - Паладин')
        self.more_info()


class Warrior(Person):

    def __init__(self, name, armor, attack, hp):
        super().__init__(name, armor, attack, hp)
        self.attack = attack * 2

    def classInfo(self):
        print(f'Ваш класс - Воин')
        self.more_info()


def creat_person():
    if randint(0, 1) > 0:
        return Paladin(random.choice(name_list),
                       round(random.uniform(0.1, 0.2), 2),
                       randint(1, 7),
                       randint(3, 10))
    else:
        return Warrior(random.choice(name_list),
                       round(random.uniform(0.1, 0.2), 2),
                       randint(1, 7),
                       randint(3, 10))


arens = [
        'Пустыня Сахара',
        'Вулкан Килиманджаро',
        'Джунгли Амазонки',
        'Тайга',
        'Антарктида',
        'Пирамида Хеопса',
        'Гора Олимп',
        'Звезда Смерти',
        'Железные Острова',
    ]


class Arena:

    #Рандомный конструктор
    def __init__(self):
        self.name = random.choice(arens)
        self.Fighters = [creat_person() for i in range(1, randint(3, 5))]
    
    def __init__(self, fighter_amount):
        self.name = random.choice(arens)
        self.Fighters = [creat_person() for i in range(0, fighter_amount)]

    def info(self):
        print(f'Локация - {self.name}')
        print(f'Количество участников:{len(self.Fighters)}')
        print(f'Список участников:\nИмя[Броня (базовая + предметы)'
              f'/Атака (базовая + предметы)/Здоровье]')

        for fighter in self.Fighters:
            fighter.info()

    def fight(self):
        fighter_count = len(self.Fighters)
        while(fighter_count > 1):
            fighter_attack = random.choice(self.Fighters)
            fighter_defend = random.choice(self.Fighters)

            #Избавляемся от повторений
            while fighter_attack == fighter_defend:
                fighter_defend = random.choice(self.Fighters)
            damage = fighter_defend.defense(fighter_attack.finalProtection())
            print(f'{fighter_attack.name} наносит удар по '
                  f'{fighter_defend.name} на {damage} урона')

            if fighter_defend.hp < 0:
                self.Fighters.remove(fighter_defend)
                fighter_count = len(self.Fighters)


a1 = Arena(10)
#a1.Fighters[0].classInfo()
#a1.Fighters[1].classInfo()
#a1.Fighters[2].classInfo()
a1.info()
a1.fight()