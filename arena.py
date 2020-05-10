import random

item_name_pool_1 = ['меч','щит','шлем','доспех','сапоги','перчатки','кольцо','амулет']
item_name_pool_2 = ['храбости','безумца','отчаяния','мертвеца','убийцы','наёмника','ученика','стражника','бродяги','следопыта']
person_name_pool = ['Говард','Роланд','Гром','Артур','Макс','Теодор','Ургаш','Ингвар','Олаф','Аспен','Драгло','Бран','Альф','Пит','Хак','Атон','Чак','Кирк','Роберт','Джек']

class Item():
    def __init__(self, name='null', mod_dmg='null', mod_def='null', mod_hp='null', dodge_rate='null'):
        if name != 'null':
            self.name = name
        else:
            self.name = random.choice(item_name_pool_1) + ' ' + random.choice(item_name_pool_2)
        if mod_dmg != 'null':
            self.mod_dmg = mod_dmg
        else:
            self.mod_dmg = random.randint(0,10)
        if mod_def != 'null':
            self.mod_def = mod_def
        else:
            self.mod_def = random.randint(0,10)
        if mod_hp != 'null':
            self.mod_hp = mod_hp
        else:
            self.mod_hp = random.randint(0,50)
        if dodge_rate != 'null':
            self.dodge_rate = dodge_rate
        else:
            self.dodge_rate = random.randint(0,7)
        print(f'{self.name}: мод. урона={self.mod_dmg}, мод. брони={self.mod_def}, мод. здоровья={self.mod_hp}, шанс уворота={self.dodge_rate}%')


class Person():
    def __init__(self, name='null', dmg='null', defense='null', hp='null'):
        if name != 'null':
            self.name = name
        else:
            self.name = random.choice(person_name_pool)
        if dmg != 'null':
            self.dmg = dmg
        else:
            self.dmg = random.randint(20,40)
        if defense != 'null':
            self.defense = defense
        else:
            self.defense = random.randint(0,10)
        if hp != 'null':
            self.hp = hp
        else:
            self.hp = random.randint(100,150)
        self.dodge_rate = 0
        self.items = []

    def put_on(self, item):
        a = self.dmg
        b = self.defense
        c = self.hp
        d = self.dodge_rate
        self.dmg += item.mod_dmg
        self.defense += item.mod_def
        self.hp += item.mod_hp
        self.dodge_rate += item.dodge_rate
        a = f'урон: {a} -> {self.dmg}'
        b = f'броня: {b} -> {self.defense}'
        c = f'здоровье: {c} -> {self.hp}'
        d = f'шанс уворота: {d}% -> {self.dodge_rate}%'
        self.items.append(item)
        print(f'{self.name} надевает предмет <{item.name}>: {a}, {b}, {c}, {d}, предметов надето: {len(self.items)}')

    def attack(self, opp):
        if self != opp:
            if not opp.dodge():
                damage = round(self.dmg * (100 - opp.defense) / 100)
                opp.hp = opp.hp - damage
                if opp.hp < 0:
                    opp.hp = 0
                    report = ''
                else:
                    report = f'Остаток здоровья героя {opp.name} - {opp.hp}'
                print(f'{self.name} наносит герою {opp.name} {damage} урона. {report}')
            else:
                print(f'{opp.name} увернулся от атаки героя {self.name}!')

    def killed(self):
        killed = False
        if self.hp == 0:
            killed = True
        return killed

    def dodge(self):
        dodge = False
        if self.dodge_rate / 100 > random.random():
            dodge = True
        return dodge



class Warrior(Person):
    def __init__(self, name='null', dmg='null', defense='null', hp='null'):
        super().__init__()
        self.dmg = self.dmg * 2
        print(f'{self.name}: класс - Воин, урон - {self.dmg}, броня - {self.defense}, здоровье - {self.hp}, шанс уворота - {self.dodge_rate}%')


class Paladin(Person):
    def __init__(self, name='null', dmg='null', defense='null', hp='null'):
        super().__init__()
        self.hp = self.hp * 2
        self.defense = self.defense *2
        print(f'{self.name}: класс - Паладин, урон - {self.dmg}, броня - {self.defense}, здоровье - {self.hp}, шанс уворота - {self.dodge_rate}%')


class Rogue(Person):
    def __init__(self, name='null', dmg='null', defense='null', hp='null'):
        super().__init__()
        self.dodge_rate = 15
        print(f'{self.name}: класс - Разбойник, урон - {self.dmg}, броня - {self.defense}, здоровье - {self.hp}, шанс уворота - {self.dodge_rate}%')


class Arena():
    def __init__(self, persons_pool=[], items_pool=[]):
        if persons_pool != []:
            self.persons_pool = persons_pool
        else:
            self.persons_pool = []
            name_pool = person_name_pool
            for i in range(1,10):
                k = random.randint(1,3)
                if k == 1:
                    new_warrior = Warrior()
                    self.persons_pool.append(new_warrior)
                    name_pool.remove(new_warrior.name)
                elif k == 2:
                    new_paladin = Paladin()
                    self.persons_pool.append(new_paladin)
                    name_pool.remove(new_paladin.name)
                elif k == 3:
                    new_rogue = Rogue()
                    self.persons_pool.append(new_rogue)
                    name_pool.remove(new_rogue.name)
        if items_pool != []:
            self.items_pool = items_pool
        else:
            self.items_pool = [Item() for i in range(1,20)]

    def items_draft(self):
        while self.items_pool != []:
            person = random.choice(self.persons_pool)
            item = random.choice(self.items_pool)
            if len(person.items) < 4:
                person.put_on(item)
                self.items_pool.remove(item)

    def fight(self):
        while len(self.persons_pool) > 1:
            attacker = random.choice(self.persons_pool)
            defender = random.choice(self.persons_pool)
            attacker.attack(defender)
            if defender.killed():
                print(f'{defender.name} умирает.')
                self.persons_pool.remove(defender)
        print(f'{self.persons_pool[0].name} побеждает!')

a = Arena()
a.items_draft()
a.fight()
