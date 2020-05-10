import random


class Thing:
    def __init__(self, description):
        self.description = description
        self.protection_mod = random.randint(1, 10)
        self.attack_mod = random.randint(1, 10)
        self.life_mod = random.randint(10, 20)
        self.speed_mod = random.randint(1, 10)
    
    
class Person:
    def __init__(self, name):
        self.name = name
        self.life_points = random.randint(70, 100)
        self.attack = random.randint(1, 49)
        self.protection = random.randint(1, 49)
        self.speed = 100 - self.attack - self.protection
        self.things = []
        self.total_life = self.life_points
        self.score = 0
    
    def add_thing(self, Thing):
        self.things.append(Thing)

    def equip_fighters(self, things_list):
        for _ in range(random.randint(1, 4)):
            thing_to_equip = random.choice(things_list)
            self.add_thing(thing_to_equip)
            self.total_life += thing_to_equip.life_mod
            self.speed += thing_to_equip.speed_mod
            self.speed -= 5  # чем больше вещей, тем медленнее персонаж

    def attack_damage(self):
        things_attack = 0
        for thing in self.things:
            things_attack += thing.attack_mod
        final_damage = self.attack + things_attack
        return final_damage

    def final_protection(self):
        things_protection = 0
        for thing in self.things:
            things_protection += thing.protection_mod
        overall_protection = self.protection + things_protection
        return overall_protection

    def damage_received(self, Person):
        if Person.speed > self.speed:
            critical_chance = random.randint(1, (Person.speed - self.speed))
        else:
            critical_chance = 0
        damage_got = (
            Person.attack_damage()
            - Person.attack_damage() * self.final_protection() // 100
            + critical_chance
        )
        if damage_got <= 0:
            damage_got = random.randint(1, 5)  # костыль
        return damage_got
        

class Warrior(Person):
    def __init__(self, name):
        super().__init__(name)
        self.attack = random.randint(2, 99)
        self.speed = 125 - self.attack - self.protection
        self.spec = "В"

    
class Paladin(Person):
    def __init__(self, name):
        super().__init__(name)
        self.protection = random.randint(10, 99)
        self.life_points = random.randint(100, 150)
        self.spec = "П"

    
class Assasin(Person):
    def __init__(self, name):
        super().__init__(name)
        self.protection = random.randint(1, 25)
        self.speed = 125 - self.attack - self.protection
        self.spec = "У"


class Arena:
    def __init__(self, limit):
        self.limit = limit
        self.list_of_fighters = []
    
    def add_fighter(self, Person):
        self.list_of_fighters.append(Person)
    
    def generateFightersList(self, names_list):
        for name in random.sample(names_list, self.limit):
            choice = random.randint(1, 3)
            if choice == 1:
                fighter = Warrior(name=name)
            elif choice == 2:
                fighter = Paladin(name=name)
            else:
                fighter = Assasin(name=name)
            fighter.equip_fighters(self.things_list)
            self.add_fighter(fighter)
        return(self.list_of_fighters)

    def create_thing(self, Thing):
        self.things_list.append(Thing)
    
    def create_list_of_things(self, description_list):
        self.things_list = []
        for i in description_list:
            item = Thing(description=i)
            self.create_thing(item)
        self.things_list.sort(key=lambda x: x.protection_mod)
        return(self.things_list)

    def fight (self):
        attacker = random.choice(self.list_of_fighters)
        defender = random.choice(self.list_of_fighters)
        while defender == attacker:
            defender = random.choice(self.list_of_fighters)
        print(
            f'{attacker.name} {attacker.spec} '
            f'нападает на {defender.name} {defender.spec} '
        )
        retaliation = random.randint(1, 100) < (defender.speed - attacker.speed)
        if retaliation:
            print(
                f'{defender.name} парирует и переходит в контратаку. '
            )
            attacker, defender = defender, attacker
        defender.total_life = defender.total_life - defender.damage_received(attacker)
        print(
            f'{attacker.name} нанес {defender.name} ущерб {defender.damage_received(attacker)}. \n'
        )
        if defender.total_life <= 0:
            epitaph_list = [
                'ПОГИБ В МУКАХ',
                'ИСТЕК КРОВЬЮ',
                'МГНОВЕННО УМЕР',
                'РАССЕЧЕН НАДВОЕ',
                'РАЗРУБЛЕН НА КУСОЧКИ',
                'ОБЕЗГЛАВЛЕН',
                'БЕССЛАВНО СКОНЧАЛСЯ',
                'ПОВЕРЖЕН',
                'ГЕРОИЧЕСКИ ПОГИБ',
                'БЫЛ УБИТ В СРАЖЕНИИ',
                'СДОХ ПРИ ПОПЫТКЕ БЕЖАТЬ',
                'УБИТ УДАРОМ В СПИНУ',
                'УМЕР ОТ РАЗРЫВА СЕРДЦА',
                'СТАЛ ПРАХОМ И РАЗВЕЯН ПО ВЕТРУ'
                ]
            epitaph = random.choice(epitaph_list)
            print(f'{defender.name} {epitaph}. \n')
            self.list_of_fighters.remove(defender)
            print(f'БОЙЦОВ ОСТАЛОСЬ В ЖИВЫХ: {len(self.list_of_fighters)} \n')
            attacker.score += 1
            if len(attacker.things) < 4:
                attacker.things.append(defender.things[0])
                print(
                    f'{attacker.name} подобрал {defender.things[0].description}.'
                )


names_list = [
    'Юлий Цезарь', 'Навуходоносор', 'Александр Македонский', 'Петр I', 'Дарий',
    'Ганнибал', 'Атилла', 'Чингисхан', 'Александр Невский', 'Наполеон',
    'Кир', 'Вильгельм', 'Сунь Цзы', 'Сципион', 'Жанна Д.Арк',
    'Сулейман', 'Ричард', 'Артур', 'Роланд', 'Саладин',
    'Ямамото', 'Карл Великий', 'Рамзес', 'Ашшурбанипал', 'Леонид',
    'Спартак', 'Бисмарк', 'Арагорн', 'Иван Грозный', 'Дмитрий Долгорукий'
    ]

description_list = [
    'палка', 'меч', 'кинжал', 'булава', 'лук',
    'арбалет', 'алебарда', 'топор', 'копье', 'щит',
    'красный щит', 'синий щит', 'зеленый щит', 'желтый щит', 'белый щит',
    'алмазный меч', 'деревянный меч', 'золотой меч', 'железный меч', 'стальной меч',
    'шлем', 'кольчуга', 'наколенники', 'сапоги', 'кираса',
    'алмазный шлем', 'деревянный шлем', 'золотой шлем', 'железный шлем', 'стальной шлем',
    'красная кираса', 'синяя кираса', 'зеленая кираса', 'желтая кираса', 'белая кираса',
    'ржавый шлем', 'ржавая кольчуга', 'ржавая кираса', 'ржавые наколенники', 'перчатки',
    'дырявые перчатки', 'новые перчатки', 'стальные перчатки', 'дырявые сапоки', 'новые сапоги',
    'новая кольчуга', 'новый шлем', 'новая кираса', 'новые наколенники', 'fotheringhay',
    'красный плащ', 'синий плащ', 'зеленый плащ', 'желтый плащ', 'белый плащ',
    'черный плащ', 'черная кираса', 'черный щит', 'черные перчатки', 'черный флаг',
    'рыжий плащ', 'рыжая кираса', 'рыжий щит', 'рыжие перчатки', 'рыжий флаг',
    'фиолетовый плащ', 'фиолетовая кираса', 'фиолетовый щит', 'фиолетовые перчатки', 'фиолетовый флаг',
    'алмазный арбалет', 'деревянный арбалет', 'золотой арбалет', 'железный арбалет', 'стальной арбалет',
    'алмазное копье', 'деревянное копье', 'золотое копье', 'железное копье', 'стальное копье',
    'алмазный лук', 'деревянный лук', 'золотой лук', 'железный лук', 'стальной лук',
    'вилы', 'сеть', 'коса', 'молот', 'веник',
    'нож', 'большой нож', 'мясницкий нож', 'острая вилка', 'сковородка',
    ]

def start_fight(lim, names_list=names_list, description_list=description_list):
    print(
        '\nКОРОЛЬ УМЕР \n'
        'И МНОЖЕСТВО ДОСТОЙНЫХ ПРЕТЕНДЕНТОВ \n'
        'СОБРАЛИСЬ, ЧТОБЫ В БИТВЕ ВЫЯСНИТЬ, \n'
        'КТО ДОСТОИН ЗАНЯТЬ ЕГО МЕСТО\n\n'
        'Вы будете просто наблюдать?\n'
        'Или хотите выставить своего кандидата?\n'
        )
    choice = input(
        'Нажмите любую клавишу, чтобы создать своего бойца, \n'
        'или Ввод, чтобы просто наблюдать:   '
        )
    if choice:
        arena = Arena(lim - 1)
        arena.create_list_of_things(description_list=description_list)
        player_name = input('Введите имя бойца:  ')
        player_class = int(input(
            'Выберите класс бойца: \n'
            '1 - Воин, 2 - Паладин, 3 - Убийца    '))
        if player_class == 1:
            fighter = Warrior(name=player_name)
            # fighter.attack = 100
        elif player_class == 2:
            fighter = Paladin(name=player_name)
            # fighter.protection = 100
        else:
            fighter = Assasin(name=player_name)
            # fighter.speed = 100
        fighter.equip_fighters(arena.things_list)
        arena.add_fighter(fighter)
    else:
        arena = Arena(lim)
        arena.create_list_of_things(description_list=description_list)
    arena.generateFightersList(names_list=names_list)

    print('\nБИТВА НАЧИНАЕТСЯ!\n')

    while len(arena.list_of_fighters) > 1:
        arena.fight()

    winner = arena.list_of_fighters[0]
    print(
        f'\nБИТВА ЗАКОНЧЕНА. ПОБЕДИЛ: {winner.name} '
        f'с количеством побед: {winner.score} '
        )
    print(f'и такими предметами: ')
    for i, item in enumerate(winner.things):
        print(
            f'{i + 1} : {item.description}'
        )
    if choice:
        if winner.name == player_name:
            print('\nВЫ ЗАВОЕВАЛИ КОРОНУ! ПОЗДРАВЛЯЕМ!\n')
        else:
            print('\nУВЫ, ВЫ ПОГИБЛИ, И КОРОНА ДОСТАЛАСЬ ДРУГОМУ\n')

start_fight(10)