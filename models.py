import random

NAMES = ['Стивен с сигой',
         'Роберт в сауне младший',
         'Сильвестр в столовой',
         'Иосиф в прихожей',
         'Дима бил лам',
         'Квентин буратино',
         'Жан-Крот Ван Дамм',
         'Максим Алкин',
         'Сильвестр стал пони',
         'Мила йоуйоуйоу бич',
         'Джим Фейри',
         'Вячеслав Муляжик',
         'Анне Занавески',
         'Гарик Сука Чорт',
         'Дженифер Хлопец',
         'Григорий Плебс',
         'Барри Алебастров',
         'Армен Джекичян',
         'Анатолий Уменейвсехвассерман',
         'Мурчалло Постоянни']


class Thing:
    DEFENCE_LIMIT = 10
    TITLES = ('Бармица',
              'Горжет',
              'Гульфик',
              'Бувигер',
              'Кираса ',
              'Латная юбка',
              'Набедренник',
              'Набедренные щитки',
              'Нагрудник',
              'Наколенники',
              'Наплечники',
              'Наручи',
              'Плакарт',
              'Поножи',
              'Реимиро',
              'Сабатон')

    def __init__(self, title, defence_percentage):
        self.defence_percentage = defence_percentage
        self.title = title

    def __str__(self):
        return f'{self.title}: def: {self.defence_percentage}'

    @staticmethod
    def generate_random():
        return Thing(
            Thing.TITLES[random.randint(0, len(Thing.TITLES) - 1)],
            random.randint(1, 10),
        )


class Person:
    BASE_DEFENCE = 10
    BASE_ATTACK = 10
    BASE_HP = 100

    def __init__(self, name, base_hp, base_attack, base_defence):
        self.name = name
        self.hp = base_hp
        self.attack = base_attack
        self.defence = base_defence
        self.things = []

    def __str__(self):
        return f'{self.__class__.__name__} : ' \
               f'{self.name}: hp: {self.hp}, attack: {self.attack}, def: {self.defence}, things: {len(self.things)} '

    def set_things(self, things):
        self.things = things

    def final_protection(self):
        # min на случай если начальное бронирование близко к 100
        return min([self.defence + sum([thing.defence_percentage for thing in self.things]), 100])

    def damage_received(self, attack_damage):
        self.hp = self.hp - (attack_damage - attack_damage * self.final_protection() / 100)

    @classmethod
    def generate_random(cls):
        if len(NAMES) == 0:
            # что-бы имена не повторялись, забираем их из списка
            raise Exception('Имена кончились, сократите количество участников')
        return cls(
            NAMES.pop(random.randint(0, len(NAMES) - 1)),
            Person.BASE_HP,
            Person.BASE_ATTACK,
            Person.BASE_DEFENCE
        )


class Paladin(Person):
    def __init__(self, name, base_hp, base_attack, base_defence):
        super().__init__(name, base_hp, base_attack, base_defence)
        self.hp = 2 * base_hp
        self.defence = 2 * base_defence


class Warrior(Person):
    def __init__(self, name, base_hp, base_attack, base_defence):
        super().__init__(name, base_hp, base_attack, base_defence)
        self.attack = 2 * base_attack
