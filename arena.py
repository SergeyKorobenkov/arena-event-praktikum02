import random

item_name_pool_1 = ['меч','щит','шлем','доспех','сапоги','перчатки','кольцо','амулет']
item_name_pool_2 = ['храбости','безумца','отчаяния','мертвеца','убийцы','наёмника','ученика','стражника','бродяги','следопыта']
person_name_pool = ['Говард','Роланд','Крик','Артур','Макс','Теодор','Ургаш','Ингвар','Олаф','Аспен','Драгло','Бран','Альф','Пит','Хак','Атон','Чак','Кирк','Роберт','Джек']

class Item():
    def __init__(self, name='null', mod_dmg='null', mod_def='null', mod_hp='null'):
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
        print(f'{self.name}: мод. урона={self.mod_dmg}, мод. брони={self.mod_def}, мод. здоровья={self.mod_hp}')


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
        self.items = []

    def put_on(self, item):
        a = self.dmg
        b = self.defense
        c = self.hp
        self.dmg += item.mod_dmg
        self.defense += item.mod_def
        self.hp += item.mod_hp
        a = f'урон: {a} -> {self.dmg}'
        b = f'броня: {b} -> {self.defense}'
        c = f'здоровье: {c} -> {self.hp}'
        self.items.append(item)
        print(f'{self.name} надевает предмет <{item.name}>: {a}, {b}, {c}, предметов надето: {len(self.items)}')

    def attack(self, opp):
        if self != opp:
            damage = round(self.dmg * (100 - opp.defense) / 100)
            opp.hp = opp.hp - damage
            if opp.hp < 0:
                opp.hp = 0
                report = ''
            else:
                report = f'Остаток здоровья героя {opp.name} - {opp.hp}'
            print(f'{self.name} наносит герою {opp.name} {damage} урона. {report}')

    def killed(self):
        killed = False
        if self.hp == 0:
            killed = True
            print(f'{self.name} умирает.')
        return killed



class Warrior(Person):
    def __init__(self, name='null', dmg='null', defense='null', hp='null'):
        super().__init__()
        self.dmg = self.dmg * 2


class Paladin(Person):
    def __init__(self, name='null', dmg='null', defense='null', hp='null'):
        super().__init__()
        self.hp = self.hp * 2
        self.defense = self.defense *2


class Arena():
    def __init__(self, persons_pool=[], items_pool=[]):
        if persons_pool != []:
            self.persons_pool = persons_pool
        else:
            self.persons_pool = []
            name_pool = person_name_pool
            for i in range(1,10):
                k = random.randint(1,2)
                if k == 1:
                    new_warrior = Warrior()
                    self.persons_pool.append(new_warrior)
                    name_pool.remove(new_warrior.name)
                else:
                    new_paladin = Paladin()
                    self.persons_pool.append(new_paladin)
                    name_pool.remove(new_paladin.name)
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
                self.persons_pool.remove(defender)
        print(f'{self.persons_pool[0].name} побеждает!')

a = Arena()
a.items_draft()
a.fight()
